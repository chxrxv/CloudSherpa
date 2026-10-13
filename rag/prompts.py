"""Versioned prompts for the Knowledge (RAG) answerer. Evals record which version ran."""

from __future__ import annotations

INSUFFICIENT = "INSUFFICIENT_CONTEXT"

KNOWLEDGE_SYSTEM_V1 = f"""\
You are CloudSherpa, a Google Cloud solution-architect assistant.
Answer the user's question using ONLY the numbered sources provided.
Cite sources inline with their markers, e.g. [S1] or [S2][S3], right after the claim they support.
If the sources do not contain the information needed to answer, reply with exactly:
{INSUFFICIENT}
Be concise and practical."""

PROMPTS: dict[str, str] = {"v1": KNOWLEDGE_SYSTEM_V1}


def format_sources(blocks: list[tuple[str, str, str, str]]) -> str:
    """blocks: (marker, title, section, text) -> prompt-ready source list."""
    parts = []
    for marker, title, section, text in blocks:
        heading = title + (f" — {section}" if section else "")
        parts.append(f"[{marker}] {heading}\n{text}")
    return "\n\n".join(parts)


def build_user_prompt(
    question: str, sources_block: str, history: list[tuple[str, str]] | None = None
) -> str:
    convo = ""
    if history:
        lines = [f"{role.capitalize()}: {content}" for role, content in history]
        convo = "Conversation so far:\n" + "\n".join(lines) + "\n\n"
    return f"Sources:\n\n{sources_block}\n\n---\n{convo}Question: {question}"
