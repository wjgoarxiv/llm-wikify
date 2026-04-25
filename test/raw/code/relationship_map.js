// Synthetic rough snippet: generate simple relationship edges from wiki pages.
// Purpose: show how a graph-style lens could remain optional and local-only.
// This snippet is intentionally incomplete and should not imply a required graph backend.

export function buildRelationshipEdges(pages) {
  const edges = [];

  for (const page of pages) {
    if (!page.links) continue;
    for (const target of page.links) {
      edges.push({
        from: page.slug,
        to: target,
        relation: "MENTIONS",
        confidence: page.confidence ?? "medium",
      });
    }
  }

  return edges;
}

// TODO: distinguish EXTRACTED, INFERRED, and AMBIGUOUS relation types.
