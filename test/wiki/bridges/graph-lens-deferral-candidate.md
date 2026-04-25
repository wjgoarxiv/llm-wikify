# Bridge: Optional Graph Lens After Local Wiki Creation

Type: bridge
Status: candidate
Built from: [[topics/graph-lens-deferral]], [[sources/relationship-lens-article]], [[sources/code-snippets]], [[sources/experiment-data]]
Last reviewed: 2026-04-25
Confidence: medium

## Local grounding

- `raw/papers/relationship_lens_article.pdf` describes relationship maps as useful after wiki pages exist.
- `raw/code/relationship_map.js` sketches a local-only relationship edge generator and warns against required graph backends.
- `raw/data/experiment_results.csv` shows higher synthetic novice confusion for early graph setup.
- [[topics/contradictions-and-uncertainty]] preserves the unresolved 10-page versus 20-page threshold.

## Portable knowledge

Graph-style relationship analysis should be a later optional lens over maintained wiki pages, not the first-run path for a novice user.

## What must stay local

- Synthetic fixture file names and dummy benchmark scores.
- The unresolved threshold numbers unless a broader evidence base supports them.

## Merge risks / contradictions

- A global rule with one fixed page threshold would over-normalize conflicting local evidence.
- Any external export requires explicit approval and is not performed by this stress test.

## Suggested destination

- `<destination-wiki>/concepts/optional-graph-lens.md` or equivalent, if a user explicitly approves export later.
