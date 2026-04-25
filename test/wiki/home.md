# llm-wikify Stress Test Wiki

Type: home
Status: active
Built from: raw/papers/offline_retrieval_latency.pdf, raw/papers/relationship_lens_article.pdf, raw/docs/product_meeting_notes.docx, raw/notes/, raw/code/, raw/data/
Last reviewed: 2026-04-25
Confidence: medium

## Start here

This local sandbox wiki remembers how a deliberately messy mixed-source folder was organized into a maintained project-local wiki.

Best first pages:
- [[index]]
- [[topics/novice-onboarding]]
- [[topics/graph-lens-deferral]]
- [[topics/contradictions-and-uncertainty]]

## What this wiki covers

The wiki covers synthetic stress-test material only: two generated PDFs, one generated DOCX, messy notes, conflicting claims, code snippets, and small CSV/JSON data. It demonstrates local-first ingestion, source notes, topic synthesis, provenance, uncertainty handling, and a local-only bridge candidate.

## Built from

- `raw/papers/offline_retrieval_latency.pdf`
- `raw/papers/relationship_lens_article.pdf`
- `raw/docs/product_meeting_notes.docx`
- `raw/notes/messy_research_notes.md`
- `raw/notes/meeting_scribbles.txt`
- `raw/notes/conflicting_claims.md`
- `raw/code/chunk_ingest_pipeline.py`
- `raw/code/relationship_map.js`
- `raw/data/experiment_results.csv`
- `raw/data/source_inventory.json`

## Current focus

- Organize mixed source material without mutating raw inputs.
- Preserve contradictions about when to suggest a graph-style relationship lens.
- Keep every generated artifact inside the `test/` sandbox boundary.

## Suggested reading path

1. [[index]]
2. [[topics/local-wiki-ingestion]]
3. [[topics/novice-onboarding]]
4. [[topics/graph-lens-deferral]]
5. [[topics/contradictions-and-uncertainty]]

## Advanced: reuse candidates

- [[bridges/graph-lens-deferral-candidate]] is a local-only candidate packet. It does not write outside `test/`.

## Notes for future agents

- Source material lives in `raw/` and should remain immutable.
- Generated wiki pages cite relative source paths.
- Any export outside `test/` requires explicit approval and is out of scope for this stress test.
