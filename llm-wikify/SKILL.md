---
name: llm-wikify
description: |
  Convert the current working directory into a task-local LLM-maintained wiki.
  Use when the user wants to organize project knowledge, ingest files or URLs into
  a local markdown wiki, bootstrap a wiki structure in-place, maintain an existing
  mini wiki, or build a repo-scoped knowledge base instead of a giant global vault.
  Trigger on phrases like "wiki this repo", "ingest raw/", "build a local wiki",
  "maintain this knowledge base", "turn this directory into an LLM wiki", or when
  repeated project knowledge needs to compound across sessions. DO NOT TRIGGER when:
  the user only wants a one-shot summary, a global PKM redesign, or generic markdown
  cleanup with no persistent wiki intent.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - WebFetch
  - WebSearch
---

# llm-wikify

Turn the **current working directory** into a mini LLM wiki that compounds project knowledge over time.

The key difference from a giant second-brain vault is scope discipline: this skill treats the active task directory as the wiki boundary unless the user explicitly asks for something broader.

---

## Core Rule

**The working directory is the wiki.**

- Do **not** assume one universal knowledge base.
- Do **not** create a sprawling personal-vault taxonomy unless the user asks.
- Do **not** flatten the wiki into one giant markdown file.
- Do build a small, legible, repo-local structure that helps future agents and humans navigate the task.

If the user gives you one project, one working directory, or one repo, then default to a **task-local wiki**.

### Locality boundary rules

- Never create or reorganize wiki content outside the current working directory unless the user explicitly expands scope.
- In a monorepo, default to the subproject or folder the user is actively working in, not the whole monorepo, unless they clearly ask for repo-wide coverage.
- Do not silently pull in parent-directory PKM structure, sibling projects, or a pre-existing personal vault.
- If the boundary is ambiguous, prefer the narrowest valid scope and state that assumption in the created `schema/wiki-rules.md`.

---

## When to Use

Use this skill when the user wants any of the following:

- bootstrap a wiki in the current repo or task folder
- ingest new sources dropped into `raw/`
- keep summaries, concepts, decisions, entities, and references synchronized over time
- answer project questions against a persistent local markdown knowledge base
- lint or maintain an existing local wiki
- organize research, due diligence, product notes, technical docs, meeting notes, or mixed-source project knowledge without building a global PKM system

Do **not** use this skill when:

- the user only wants a one-shot summary or memo
- the task is ordinary docs cleanup with no persistent knowledge workflow
- the user explicitly wants a cross-project or personal-vault redesign
- there is no desire to maintain a persistent markdown artifact

---

## Operating Modes

### 1. Bootstrap mode
Use when the working directory has **no clear wiki structure yet**.

Your job:
- inspect what already exists
- create the smallest useful wiki structure
- preserve existing docs and point to them instead of duplicating them
- seed a home page, index, and only the minimum grounded pages needed
- write down the chosen locality boundary in `schema/wiki-rules.md`

### 2. Ingest mode
Use when the user adds new files, notes, exports, or URLs into `raw/`.

Your job:
- treat `raw/` as immutable source material
- extract useful knowledge into the wiki
- preserve provenance for claims and summaries
- update related pages incrementally rather than rewriting everything

### 3. Query mode
Use when the user asks questions against the local wiki.

Your job:
- read the index first
- follow the most relevant local pages
- answer with citations to wiki pages and raw sources where appropriate
- file high-value analyses back into the wiki when they would be useful later

### 4. Lint / maintain mode
Use when the wiki already exists and needs health checks.

Your job:
- detect stale pages, orphan pages, broken links, duplicate topics, inconsistent naming, weak summaries, and unresolved ingestion leftovers
- make targeted fixes
- leave a short maintenance report with what changed and what still needs human review

---

## Default Folder Contract

If no wiki exists, bootstrap this minimal structure inside the current working directory:

```text
raw/                 # immutable source material dropped in by the user
wiki/
  index.md           # content-oriented catalog of the wiki
  home.md            # start-here overview for humans and agents
  topics/            # concept/topic pages
  entities/          # companies, tools, people, systems, components when relevant
  sources/           # per-source summaries or source notes
schema/
  wiki-rules.md      # local conventions for this wiki
log/
  log.md             # append-only ingest/query/lint history
```

This is the **default**, not a law. If the repo already has a better local structure, adapt to it instead of forcing this exact layout.

If the domain is simpler, reduce it. For small tasks, `wiki/index.md`, `wiki/home.md`, `wiki/topics/`, and `raw/` may be enough.

Do not create every folder just because it appears in this example. Create `entities/`, `sources/`, or `log/` only when they serve the actual project.

---

## MECE Structuring Heuristic

When bootstrapping or reorganizing, aim for **mutually exclusive, collectively exhaustive enough** categories — but only to the scale justified by the project.

Good:
- `topics/` for ideas, mechanisms, workflows
- `entities/` for named actors or systems
- `sources/` for source-level summaries and provenance

Bad:
- `misc/`
- `random-notes/`
- `things/`
- 20 top-level folders created before the directory is understood

If two folders are hard to distinguish, merge them.

---

## Non-Negotiable Conventions

### 1. Raw is immutable
`raw/` is source material. Read from it. Do not rewrite it unless the user explicitly asks.

### 2. Wiki is generated and maintained
`wiki/` is the maintained knowledge artifact. This is where synthesized understanding lives.

### 3. Provenance is preserved
Every important claim, summary, or extracted insight should point back to a raw source note, source file, or URL when practical.

Each created topic/entity page should also declare its **grounding inputs** near the top, for example:

```markdown
Built from: README.md, raw/interview-2026-04-06.md, src/api/
```

### 4. Incremental updates beat rewrites
When a new source arrives, update the relevant pages and log the change. Do not regenerate the entire wiki unless the structure is badly broken.

Repeated ingestion should be idempotent:

- one stable source note per source or source bundle
- update existing pages when the same source is re-processed
- do not create duplicate topic pages just because wording changed slightly

### 5. The wiki stays local
Do not silently widen scope from the current project to a personal knowledge base.

### 6. Navigation must stay legible
Every page should have an obvious path in and out: from `home.md`, `index.md`, a topic page, or a source note.

---

## Page Types

### `wiki/home.md`
The start page for a human or agent entering the wiki cold.

Should include:
- what this wiki is about
- what the current focus is
- where to start reading
- the most important linked pages

### `wiki/index.md`
The catalog. Organize pages by section with one-line descriptions.

### `wiki/sources/*.md`
One page per important source or source bundle.

Should capture:
- source identity
- short summary
- what changed in the wiki because of it
- open questions or contradictions

### `wiki/topics/*.md`
Persistent concepts, workflows, comparisons, decisions, or thematic summaries.

Create a new topic page only if at least one of these is true:

- the concept appears across multiple sources or repo landmarks
- the concept is important enough to be linked from more than one page
- the material would make an existing page overloaded or incoherent

Otherwise, extend an existing page instead of creating a new one.

### `wiki/entities/*.md`
Named systems, tools, people, teams, products, services, code components, or organizations when entity pages are actually useful.

Do **not** create entity pages just because the folder exists.

Entity pages should be rare in small repos. If the entity is mentioned only once or adds no navigation value, keep it inside a topic or source page.

---

## Bootstrap Workflow

When no wiki exists:

1. Inspect the working directory first.
2. Identify existing docs, configs, code structure, notes, exports, and obvious landmarks.
3. Create the smallest useful folder structure.
4. Create `schema/wiki-rules.md` describing the local contract.
5. Create `wiki/home.md` and `wiki/index.md`.
6. Create only a few grounded pages tied to the actual directory contents.
7. Log the bootstrap in `log/log.md`.

Before creating any page, ask:

- What exact files, folders, notes, or sources justify this page?
- Would updating an existing page be better than creating a new one?
- Will this page improve navigation, or is it just tidy-looking scaffolding?

Bootstrap should feel like laying down navigational rails, not building a cathedral.

---

## Ingest Workflow

When new material appears in `raw/`:

1. Read the new source.
2. Decide what kind of source it is: article, paper, transcript, meeting notes, product doc, export, mixed scratch notes, etc.
3. Create or update a source page in `wiki/sources/`.
4. Update related topic/entity pages with the durable knowledge from that source.
5. Mark uncertainty where the source is ambiguous, partial, or contradictory.
6. Update `wiki/index.md` if a new persistent page was added.
7. Append an ingest record to `log/log.md`.

If one source touches many pages, that is normal.

Do not treat provenance as a decorative backlink. Major sections should make it clear which source note or raw input they came from.

---

## Query Workflow

When the user asks a question that should compound into the wiki:

1. Read `wiki/index.md` first.
2. Follow the relevant topic/entity/source pages.
3. Check whether the maintained wiki is actually sufficient for the question.
4. If it is not sufficient, read the missing raw/source material, update the wiki first, then answer.
4. If the answer creates a valuable new artifact — comparison, synthesis, decision memo, glossary, taxonomy, timeline — file it back into `wiki/`.
5. Log the query if it materially changed the wiki.

High-value answers should not disappear into chat history if they would clearly help later.

---

## Maintenance Workflow

Periodically check for:

- broken or stale links
- orphan pages with no inbound path
- duplicate or near-duplicate topics
- weak openings that do not tell the reader what the page is for
- source notes that were never integrated into topic pages
- pages that became obsolete after newer sources arrived
- index drift, where `index.md` no longer reflects reality

Fix what is clearly safe. Flag what needs human judgment.

Always leave a concise maintenance report.

---

## Provenance Pattern

Use lightweight provenance. Do not turn every sentence into citation soup.

Good enough patterns include:

- `Source: [[sources/article-name]]`
- `Derived from: raw/interview-2026-04-06.md`
- `Evidence: [[sources/vendor-api-notes]]`
- `Uncertain: this claim appears in one partial transcript only`

When sources conflict, say so explicitly.

At minimum, each durable page should let a future reader answer:

- which sources or repo landmarks shaped this page?
- where should I go to verify the main claims?

---

## Minimal `log/log.md` Format

Use parseable headings so recent activity is easy to scan.

```markdown
## [2026-04-06] bootstrap | initialized local wiki
- Created wiki/home.md, wiki/index.md, schema/wiki-rules.md
- Seeded topic pages for project structure and workflow

## [2026-04-06] ingest | vendor-api-export
- Added source page: wiki/sources/vendor-api-export.md
- Updated topics/integration-pitfalls.md
```

Keep it append-only.

---

## `schema/wiki-rules.md` Must Capture

When bootstrapping, document the local rules for future sessions:

- the scope boundary of the wiki
- the exact locality boundary (current folder, subproject, or full repo)
- what belongs in `raw/` vs `wiki/`
- page naming conventions
- whether wiki links or normal markdown links are preferred
- provenance style
- when a new page is allowed versus when an existing page must be updated
- how repeated ingest updates existing pages without duplication
- how maintenance reports should be recorded

This is what turns a generic markdown pile into a disciplined maintained wiki.

---

## Anti-Patterns

Do **not** do these:

- create a giant universal vault when the user asked about one project
- dump all ingested knowledge into one long summary page
- duplicate existing README content without adding navigation value
- invent folders and pages with no grounding in the actual directory
- create scaffolding that mirrors folder names or README headings without adding synthesis
- rewrite `raw/` as if it were polished wiki content
- erase uncertainty from partial or conflicting sources
- merge pages aggressively when overlap might reflect different purposes
- add indexes everywhere; add them only where navigation actually benefits

---

## Good Output Standard

After using this skill, the working directory should feel like this:

- a future agent can open `wiki/home.md` and orient quickly
- the wiki structure is small, local, and legible
- new sources can be added without redesigning everything
- important claims can be traced back to source notes or raw material
- the wiki gets richer over time instead of noisier

That is the point of llm-wikify: **persistent, compounding project knowledge without the cost of maintaining a giant all-purpose knowledge base.**
