# Code as Source Material

Type: topic
Status: active
Built from: [[sources/code-snippets]], [[sources/product-meeting-notes]]
Last reviewed: 2026-04-25
Confidence: medium

## Summary

Rough code chunks in the fixture were handled as source evidence, not production implementation. Their comments explain design intent and uncertainty, which makes them useful for topic synthesis.

## Evidence

- `raw/code/chunk_ingest_pipeline.py` describes itself as intentionally incomplete and asks for provenance anchors and conflict markers.
- `raw/code/relationship_map.js` describes a local-only optional relationship lens and includes a TODO for relation confidence labels.
- `raw/docs/product_meeting_notes.docx` asks whether code snippets should become source notes, topic evidence, or both.

## Handling decision

Create one source note for code snippets and one topic page for the broader rule. Do not execute or promote the snippets as production code.
