# llm-wikify Stress Test Report

## Scope

This stress test treated `test/` as the current working directory and wiki boundary. All generated source material, scripts, wiki output, schema, log, bridge candidate, and this report were written inside `test/` only.

## Fixture files created

### Synthetic PDFs
- `raw/papers/offline_retrieval_latency.pdf`
- `raw/papers/relationship_lens_article.pdf`

### Synthetic DOCX
- `raw/docs/product_meeting_notes.docx`

### Messy notes
- `raw/notes/messy_research_notes.md`
- `raw/notes/meeting_scribbles.txt`
- `raw/notes/conflicting_claims.md`

### Code chunks
- `raw/code/chunk_ingest_pipeline.py`
- `raw/code/relationship_map.js`

### Structured data
- `raw/data/experiment_results.csv`
- `raw/data/source_inventory.json`

### Fixture generation script
- `tools/create_binary_fixtures.py`

## Wiki pages produced

### Navigation and rules
- `wiki/home.md`
- `wiki/index.md`
- `schema/wiki-rules.md`
- `log/log.md`

### Source notes
- `wiki/sources/offline-retrieval-latency.md`
- `wiki/sources/relationship-lens-article.md`
- `wiki/sources/product-meeting-notes.md`
- `wiki/sources/messy-notes-bundle.md`
- `wiki/sources/code-snippets.md`
- `wiki/sources/experiment-data.md`

### Topic pages
- `wiki/topics/local-wiki-ingestion.md`
- `wiki/topics/novice-onboarding.md`
- `wiki/topics/graph-lens-deferral.md`
- `wiki/topics/code-as-source-material.md`
- `wiki/topics/contradictions-and-uncertainty.md`

### Local bridge candidate
- `wiki/bridges/graph-lens-deferral-candidate.md`

## How PDFs, DOCX, and code chunks were handled

- PDFs were generated as real `.pdf` files with a minimal built-in Python writer. Their source notes summarize title, abstract-like claims, sections, and reference notes with provenance back to the PDF paths.
- The DOCX was generated as a real `.docx` OpenXML zip package using built-in Python. Its source note treats it as product/meeting notes and cites the generated DOCX path.
- Code chunks were treated as source material rather than production code. Their comments and TODOs were summarized in `wiki/sources/code-snippets.md` and synthesized into `wiki/topics/code-as-source-material.md`.

## Contradictions or uncertainty found

- Graph-lens threshold conflict: some sources suggest waiting until roughly 20 maintained pages, while another claim says 10 pages may be enough if the user asks about connections.
- Graph necessity conflict: one PDF says graph extraction is unnecessary for small corpora, while another says relationship maps help medium-sized corpora after wiki pages exist.
- Code handling uncertainty: the DOCX asks whether code snippets should become source notes, topic evidence, or both. This test used both.

## What went well

- Mixed source types were organized into a small local wiki without modifying `raw/` inputs.
- Source notes and topic pages cite relative input file paths.
- Contradictions were surfaced in `wiki/topics/contradictions-and-uncertainty.md` instead of normalized away.
- A bridge candidate was kept local under `wiki/bridges/` and did not write to any external destination.

## What broke / limitations

- No external PDF or DOCX parser was used. The summaries are grounded in the generated fixture content and generator script, not in an independent document extraction pipeline.
- The PDF writer is intentionally minimal and creates simple single-page PDFs for stress testing, not polished publication PDFs.
- The DOCX package is minimal and suitable for a fixture, not for styled business documents.
- The CSV scores and threshold claims are synthetic and should not be treated as real benchmark data.

## Exact commands or scripts used

```bash
mkdir -p "test/raw/papers" "test/raw/docs" "test/raw/notes" "test/raw/code" "test/raw/data" "test/tools" "test/wiki/sources" "test/wiki/topics" "test/schema" "test/log"
python3 "test/tools/create_binary_fixtures.py"
mkdir -p "test/wiki/bridges"
```

Markdown fixtures and wiki pages were created directly as files under `test/` during the stress-test session.

## Boundary statement

No parent, sibling, global wiki, external vault, graph database, or home-directory skill location was intentionally written by this stress test. The only generated artifacts are under `test/`.
