#!/usr/bin/env python3
"""Generate synthetic PDF and DOCX fixtures for the llm-wikify stress test.

The files are intentionally small, public-repo-safe, and self-contained. The
script avoids network access and does not read or write outside the test/
directory tree.
"""

from __future__ import annotations

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parents[1]


def pdf_escape(text: str) -> str:
    return text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def write_simple_pdf(path: Path, title: str, lines: list[str]) -> None:
    """Write a minimal valid single-page PDF using built-in Python only."""
    content_lines = ["BT", "/F1 12 Tf", "72 760 Td"]
    content_lines.append(f"({pdf_escape(title)}) Tj")
    for line in lines:
        content_lines.append("0 -18 Td")
        content_lines.append(f"({pdf_escape(line)}) Tj")
    content_lines.append("ET")
    stream = "\n".join(content_lines).encode("latin-1", errors="replace")

    objects = [
        b"1 0 obj << /Type /Catalog /Pages 2 0 R >> endobj\n",
        b"2 0 obj << /Type /Pages /Kids [3 0 R] /Count 1 >> endobj\n",
        b"3 0 obj << /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >> endobj\n",
        b"4 0 obj << /Type /Font /Subtype /Type1 /BaseFont /Helvetica >> endobj\n",
        b"5 0 obj << /Length " + str(len(stream)).encode("ascii") + b" >> stream\n" + stream + b"\nendstream endobj\n",
    ]

    out = bytearray(b"%PDF-1.4\n")
    offsets = [0]
    for obj in objects:
        offsets.append(len(out))
        out.extend(obj)
    xref_offset = len(out)
    out.extend(f"xref\n0 {len(objects) + 1}\n".encode("ascii"))
    out.extend(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        out.extend(f"{offset:010d} 00000 n \n".encode("ascii"))
    out.extend(
        f"trailer << /Size {len(objects) + 1} /Root 1 0 R >>\nstartxref\n{xref_offset}\n%%EOF\n".encode("ascii")
    )
    path.write_bytes(out)


def write_docx(path: Path, paragraphs: list[str]) -> None:
    """Write a minimal DOCX package using built-in zipfile only."""
    def p(text: str) -> str:
        escaped = (
            text.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
        )
        return f"<w:p><w:r><w:t>{escaped}</w:t></w:r></w:p>"

    document_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:body>
    {body}
    <w:sectPr><w:pgSz w:w="12240" w:h="15840"/><w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440"/></w:sectPr>
  </w:body>
</w:document>
""".format(body="\n    ".join(p(text) for text in paragraphs))

    with ZipFile(path, "w", ZIP_DEFLATED) as zf:
        zf.writestr(
            "[Content_Types].xml",
            """<?xml version="1.0" encoding="UTF-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>
""",
        )
        zf.writestr(
            "_rels/.rels",
            """<?xml version="1.0" encoding="UTF-8"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>
""",
        )
        zf.writestr("word/document.xml", document_xml)


def main() -> None:
    papers = ROOT / "raw" / "papers"
    docs = ROOT / "raw" / "docs"
    papers.mkdir(parents=True, exist_ok=True)
    docs.mkdir(parents=True, exist_ok=True)

    write_simple_pdf(
        papers / "offline_retrieval_latency.pdf",
        "Offline Retrieval Latency in Maintained Local Wikis",
        [
            "Abstract: This synthetic article studies local wiki retrieval latency under noisy source drops.",
            "Section 1: Local-first summaries reduced repeated scanning in the simulated corpus.",
            "Section 2: A cache warmed by source notes improved median lookup time by 32 percent.",
            "Contradiction note: The article claims graph extraction is unnecessary for small corpora.",
            "Reference: Synthetic Benchmark Working Note, 2026.",
        ],
    )
    write_simple_pdf(
        papers / "relationship_lens_article.pdf",
        "Relationship Lens for Noisy Research Folders",
        [
            "Abstract: This synthetic article proposes a graph-style lens after wiki pages exist.",
            "Section 1: Relationship maps helped locate surprising links in medium-sized corpora.",
            "Section 2: Early graph setup confused novice users in simulated onboarding.",
            "Contradiction note: The article recommends graph extraction once a corpus exceeds 20 pages.",
            "Reference: Public Dummy Methods Digest, 2026.",
        ],
    )
    write_docx(
        docs / "product_meeting_notes.docx",
        [
            "Product Notes: Local Wiki Onboarding Review",
            "Goal: Help a novice user organize a messy folder without learning internal folder names first.",
            "Decision: Ask at most three onboarding questions, then create a useful start page.",
            "Risk: If empty-folder starter packs create many placeholders, users may see a hollow wiki.",
            "Open question: Should code snippets become source notes, topic evidence, or both?",
            "Conflicting note: One reviewer wants a graph lens immediately; another says graphing should wait.",
        ],
    )
    print("Generated 2 PDFs and 1 DOCX under test/raw/.")


if __name__ == "__main__":
    main()
