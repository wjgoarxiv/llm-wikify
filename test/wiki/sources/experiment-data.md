# Source: Experiment Data

Type: source
Status: active
Built from: raw/data/experiment_results.csv, raw/data/source_inventory.json
Last reviewed: 2026-04-25
Confidence: medium

## Source identity

- CSV: `raw/data/experiment_results.csv`
- JSON: `raw/data/source_inventory.json`
- Kind: synthetic structured data fixture

## Summary

The CSV lists three dummy source groups and novice confusion scores. The JSON inventories fixture sources and confirms the sandbox scope is `test` only.

## Key takeaways

- The dummy rows suggest early graph lens setup has a higher novice confusion score than local wiki baseline or delayed graph lens. Evidence: `raw/data/experiment_results.csv`.
- The inventory records all source files as synthetic public content. Evidence: `raw/data/source_inventory.json`.

## Uncertainty / caveats

- The data is illustrative only and has no statistical validity.

## Wiki updates triggered

- Updated [[topics/graph-lens-deferral]].
- Updated [[topics/local-wiki-ingestion]].
