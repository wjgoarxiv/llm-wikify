"""Synthetic rough snippet: parse a small list of source records.

Purpose: demonstrate that code chunks may carry design intent and uncertainty.
This is intentionally incomplete and should be summarized as source material,
not treated as production-ready implementation.
"""

from dataclasses import dataclass


@dataclass
class SourceRecord:
    path: str
    source_type: str
    confidence: str = "medium"


def classify_source(path: str) -> str:
    if path.endswith(".pdf"):
        return "paper-or-article"
    if path.endswith(".docx"):
        return "document-notes"
    if path.endswith((".py", ".js")):
        return "code-snippet"
    return "notes"


def build_records(paths: list[str]) -> list[SourceRecord]:
    # TODO: add provenance anchors and conflict markers.
    return [SourceRecord(path=p, source_type=classify_source(p)) for p in paths]
