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


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=REPO_ROOT / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # --- LLM access -------------------------------------------------------------------
    # Either GEMINI_API_KEY (Gemini Developer API) or Vertex AI (ADC credentials).
    gemini_api_key: str | None = None
    google_genai_use_vertexai: bool = False
    google_cloud_project: str | None = None
    google_cloud_location: str = "us-central1"

    # Model routing: Flash for cheap/simple steps, Pro for the architect step.
    flash_model: str = "gemini-3.8-flash"
    pro_model: str = "gemini-3.1-pro-preview"
    llm_temperature: float = 0.2
    llm_timeout_s: float = 120.0
    # LLM-as-judge: pinned, and deliberately a different model from the one under test.
    judge_model: str = "gemini-3.1-pro-preview"
    price_table: Path = REPO_ROOT / "core" / "pricing.yaml"

    # --- Corpus & index ---------------------------------------------------------------
    data_dir: Path = REPO_ROOT / "data"
    corpus_sources: Path = REPO_ROOT / "rag" / "sources.yaml"

    # --- Retrieval --------------------------------------------------------------------
    # "hash" is a dependency-free bag-of-words embedder for CI smoke runs only.
    embedding_provider: Literal["local", "gemini", "hash"] = "local"
    local_embedding_model: str = "BAAI/bge-small-en-v1.5"
    gemini_embedding_model: str = "gemini-embedding-001"
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
            return bool(self.google_cloud_project)
        return bool(self.gemini_api_key)

    def snapshot(self) -> dict[str, object]:
        """Config values that affect results (no secrets) — recorded with every eval run."""
        keys = [
            "flash_model",
            "pro_model",
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
