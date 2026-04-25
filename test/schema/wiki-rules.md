# Wiki Rules

## Scope
- This wiki covers the `test/` sandbox directory only.
- All source material, generated wiki pages, logs, and reports must stay inside `test/`.
- No parent, sibling, global wiki, external vault, graph database, or home-directory skill location may be written by this stress test.

## Layers
- `raw/` = immutable synthetic source fixture material.
- `wiki/` = maintained summaries, topics, source notes, and local-only bridge candidates.
- `schema/` = local operating rules for this sandbox wiki.
- `log/` = append-only activity history.

## Source handling
- Treat PDFs, DOCX, text notes, code snippets, CSV, and JSON as source material.
- Preserve provenance with relative paths such as `raw/papers/offline_retrieval_latency.pdf`.
- Do not rewrite files under `raw/` during ingestion.
- Record uncertainty and contradictions visibly on both source notes and topic pages when relevant.

## Public-repo safety
- Use synthetic public dummy content only.
- Do not include personal names, private paths, credentials, tokens, private datasets, or machine-specific examples.
- Keep reusable examples generic and clone/fork friendly.

## Bridge / promotion policy
- `wiki/bridges/` may contain local candidate packets only.
- Bridge packets are not external writes and do not update any global store.
- External export would require explicit approval and is out of scope for this stress test.

## Local vocabulary
- Page types: `home`, `index`, `source`, `topic`, `bridge`, `report`, `rules`, `log`.
- Status values: `draft`, `active`, `candidate`, `needs-review`.
- Confidence values: `high`, `medium`, `low`.
