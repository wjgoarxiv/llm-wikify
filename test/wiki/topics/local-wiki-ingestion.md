# Local Wiki Ingestion

Type: topic
Status: active
Built from: [[sources/offline-retrieval-latency]], [[sources/messy-notes-bundle]], [[sources/experiment-data]]
Last reviewed: 2026-04-25
Confidence: medium

## Summary

The stress-test corpus supports a source-note-first workflow: keep raw synthetic inputs immutable, create source notes with provenance, then synthesize durable topics from those notes.

## Evidence

- `raw/papers/offline_retrieval_latency.pdf` claims maintained local summaries reduce repeated scanning.
- `raw/notes/meeting_scribbles.txt` says source material should remain untouched while generated notes cite it.
- `raw/data/source_inventory.json` records the fixture scope as `test directory only`.

## Practical rule for this sandbox

Use source notes for mixed-format inputs before turning claims into topic pages. This keeps PDFs, DOCX, messy notes, code, and data traceable without flattening everything into one long summary.

## Limitations

The retrieval-latency claim and CSV scores are synthetic. They demonstrate provenance handling, not real performance.
