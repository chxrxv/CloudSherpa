"""Central configuration, loaded from environment variables / `.env`.

Every knob that changes behaviour (models, retrieval strategy, thresholds, backends) lives
here so eval runs can be reproduced from a config snapshot.
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict

REPO_ROOT = Path(__file__).resolve().parent.parent


class FreeTierViolation(RuntimeError):
    """A configuration or call that could incur charges while FREE_TIER_ONLY is set."""


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=REPO_ROOT / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # --- LLM access -------------------------------------------------------------------
    # Free tier only: a Gemini API key from Google AI Studio on a project WITHOUT billing.
    # The Vertex AI path is kept in code but blocked while FREE_TIER_ONLY is true.
    gemini_api_key: str | None = None
    google_genai_use_vertexai: bool = False
    google_cloud_project: str | None = None
    google_cloud_location: str = "us-central1"

    free_tier_only: bool = True
    # Models whose Gemini API pricing page lists a free tier ("Free of charge"), verified
    # 2026-10-13 at https://ai.google.dev/gemini-api/docs/pricing. Pro has no free tier.
    free_tier_models: list[str] = [
        "gemini-3.8-flash",
        "gemini-3.6-flash",
        "gemini-3.5-flash-lite",
        "gemini-3.1-flash-lite",
        "gemini-embedding-2",
    ]

    # Model routing (free tier: Flash-class only). `flash_model` answers questions;
    # `strong_model` is reserved for the architect step (phase 3).
    flash_model: str = "gemini-3.8-flash"
    strong_model: str = "gemini-3.8-flash"
    llm_temperature: float = 0.2
    llm_timeout_s: float = 120.0

    # --- Free-tier rate limiting (per model) -----------------------------------------
    # Google no longer publishes numeric free-tier limits; they are shown per project in
    # AI Studio. These defaults are conservative placeholders, NOT documented limits: copy
    # your project's values from AI Studio into .env.
    llm_rpm: float = 5.0  # requests per minute, sliding 60 s window
    llm_daily_request_budget: int = 100  # per model per Pacific-time day; run aborts cleanly
    llm_max_retries: int = 6  # attempts on 429/5xx before giving up
    llm_backoff_base_s: float = 4.0  # exponential: base * 2**attempt (+ jitter), capped
    llm_backoff_max_s: float = 120.0
    usage_dir: Path = REPO_ROOT / "data" / "usage"  # persisted daily request counts

    # --- LLM-as-judge -----------------------------------------------------------------
    # Pinned, free-tier, and deliberately a different model from the one under test.
    # backend "openai_compat" targets a local OpenAI-compatible server (e.g. Ollama) as a
    # fallback when the free quota is exhausted; set JUDGE_MODEL to the local model name.
    judge_backend: Literal["gemini", "openai_compat"] = "gemini"
    judge_model: str = "gemini-3.6-flash"
    judge_base_url: str = "http://localhost:11434/v1"
    judge_api_key: str | None = None
    judge_cache_dir: Path = REPO_ROOT / "evals" / "cache" / "judge"

    # --- Corpus & index ---------------------------------------------------------------
    data_dir: Path = REPO_ROOT / "data"
    corpus_sources: Path = REPO_ROOT / "rag" / "sources.yaml"

    # --- Retrieval --------------------------------------------------------------------
    # "hash" is a dependency-free bag-of-words embedder for CI smoke runs only.
    embedding_provider: Literal["local", "gemini", "hash"] = "local"
    local_embedding_model: str = "BAAI/bge-small-en-v1.5"
    gemini_embedding_model: str = "gemini-embedding-2"
    vector_store: Literal["faiss", "vertex"] = "faiss"

    chunking_strategy: Literal["fixed", "markdown"] = "fixed"
    chunk_size: int = 1200  # characters
    chunk_overlap: int = 200
    # Prepend "Title — Section" to each chunk before embedding.
    contextual_headers: bool = False

    retrieval_mode: Literal["dense", "bm25", "hybrid"] = "hybrid"
    candidate_k: int = 20  # per retriever, before fusion
    rrf_k: int = 60
    reranker: Literal["cross-encoder", "none"] = "cross-encoder"
    reranker_model: str = "Xenova/ms-marco-MiniLM-L-6-v2"
    top_k: int = 5  # chunks passed to the generator
    # Refuse when the best reranked chunk's relevance probability falls below this.
    min_confidence: float = 0.10

    # --- Vertex AI Vector Search (only when vector_store == "vertex") -----------------
    vertex_index_id: str | None = None
    vertex_index_endpoint_id: str | None = None
    vertex_deployed_index_id: str | None = None

    @property
    def corpus_dir(self) -> Path:
        return self.data_dir / "corpus"

    @property
    def index_dir(self) -> Path:
        # One index per (embedder, chunking) combination so eval variants don't collide.
        emb = {
            "local": self.local_embedding_model,
            "gemini": self.gemini_embedding_model,
            "hash": "hash-256",
        }[self.embedding_provider]
        tag = f"{self.embedding_provider}-{emb.replace('/', '_')}-{self.chunking_strategy}"
        tag += f"-{self.chunk_size}-{self.chunk_overlap}"
        tag += "-ctx" if self.contextual_headers else ""
        return self.data_dir / "index" / tag

    @property
    def has_llm_credentials(self) -> bool:
        if self.google_genai_use_vertexai:
            return bool(self.google_cloud_project) and not self.free_tier_only
        return bool(self.gemini_api_key)

    def check_free_tier(self, model: str | None = None) -> None:
        """Raise FreeTierViolation if the configured path or `model` could incur charges."""
        if not self.free_tier_only:
            return
        if self.google_genai_use_vertexai:
            raise FreeTierViolation(
                "Vertex AI is a billed path; FREE_TIER_ONLY=true allows only a Gemini API key "
                "from Google AI Studio (project without billing)."
            )
        if self.vector_store == "vertex":
            raise FreeTierViolation("VECTOR_STORE=vertex is billed; use faiss.")
        if model is not None and model not in self.free_tier_models:
            raise FreeTierViolation(
                f"Model {model!r} is not in FREE_TIER_MODELS {self.free_tier_models}."
            )

    def snapshot(self) -> dict[str, object]:
        """Config values that affect results (no secrets) — recorded with every eval run."""
        keys = [
            "free_tier_only",
            "flash_model",
            "strong_model",
            "judge_backend",
            "judge_model",
            "llm_temperature",
            "embedding_provider",
            "local_embedding_model",
            "gemini_embedding_model",
            "vector_store",
            "chunking_strategy",
            "chunk_size",
            "chunk_overlap",
            "contextual_headers",
            "retrieval_mode",
            "candidate_k",
            "rrf_k",
            "reranker",
            "reranker_model",
            "top_k",
            "min_confidence",
        ]
        return {k: getattr(self, k) for k in keys}


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
