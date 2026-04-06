# Wiki Rules

## Scope
- This wiki covers the current working directory only.
- It is a task-local or repo-local wiki, not a global personal knowledge base.
- Exact boundary for this wiki:

## Layers
- `raw/` = immutable source inputs
- `wiki/` = maintained synthesized knowledge
- `schema/` = local conventions and operating rules
- `log/` = append-only activity history

## Naming
- Use stable, descriptive kebab-case file names.
- Prefer one concept per page.
- Avoid `misc`, `notes`, `stuff`, or other catch-all names.

## Page creation threshold
- Create a new page only if it improves navigation or prevents an existing page from becoming overloaded.
- Otherwise update an existing page.
- Do not create pages that merely mirror existing folder names or README headings without adding synthesis.

## Linking
- Prefer wiki-style internal linking where supported by the user’s markdown environment.
- Otherwise use relative markdown links.
- Chosen link format for this wiki:

## Provenance
- Important claims should point back to a source page or raw file.
- Preserve uncertainty when a source is partial, conflicting, or ambiguous.
- Durable pages should include a `Built from:` line near the top.
- Chosen source ID / provenance style for this wiki:

## Re-ingest behavior
- Re-processing the same source should update an existing source note and linked pages, not create duplicates.
- Preferred duplicate-handling rule for this wiki:

## Maintenance
- Safe fixes: broken links, weak page openings, orphan-page navigation, obvious duplicates.
- Human-review items: ambiguous merges, contradictory claims, scope changes, or destructive reorganizations.
