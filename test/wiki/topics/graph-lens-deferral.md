# Graph Lens Deferral

Type: topic
Status: needs-review
Built from: [[sources/relationship-lens-article]], [[sources/offline-retrieval-latency]], [[sources/messy-notes-bundle]], [[sources/code-snippets]], [[sources/experiment-data]]
Last reviewed: 2026-04-25
Confidence: medium

## Summary

The corpus supports treating graph-style relationship maps as an optional later lens. It does not support making graph setup part of first-run novice onboarding.

## Evidence

- `raw/papers/relationship_lens_article.pdf` says relationship maps can reveal surprising links in medium-sized corpora.
- `raw/papers/relationship_lens_article.pdf` also says early graph setup confused novice users.
- `raw/code/relationship_map.js` sketches local relationship edges but states it should not imply a required graph backend.
- `raw/data/experiment_results.csv` assigns higher novice confusion to early graph lens setup than to local wiki baseline or delayed graph lens.

## Contradiction

- `raw/papers/relationship_lens_article.pdf` and `raw/notes/conflicting_claims.md` include a 20-page threshold.
- `raw/notes/conflicting_claims.md` also says a 10-page threshold may be acceptable if the user asks about connections.

## Review-needed decision

Do not normalize the threshold into one number. Keep the decision as: graph-style analysis is optional after the wiki exists, and threshold choice requires context or user intent.
