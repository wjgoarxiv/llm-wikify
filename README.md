<p align="center"><img src="./cover.png" width="100%" /></p>

<h1 align="center">llm-wikify</h1>
<p align="center">
  <em>Turn the current working directory into a small, compounding LLM wiki — without building a giant universal vault.</em>
</p>
<p align="center">
  <a href="#novice-quickstart">Novice Quickstart</a> · <a href="#when-to-use">When to Use</a> · <a href="#features">Features</a> · <a href="#workflow">Workflow</a> · <a href="#repo-layout">Repo Layout</a> · <a href="./README-ko.md">한국어</a>
</p>
<p align="center">
  <img src="https://img.shields.io/badge/skill-local%20wiki-blueviolet" />
  <img src="https://img.shields.io/badge/format-markdown-green" />
  <img src="https://img.shields.io/badge/scope-task--local-orange" />
  <img src="https://img.shields.io/badge/works%20with-Claude%20Code%20%7C%20Codex%20%7C%20OpenCode-black" />
</p>

---

> [!NOTE]
> `llm-wikify` is inspired by Karpathy’s `llm-wiki` pattern, but optimized for **task-driven work**. Instead of forcing the model to constantly reason over one ever-growing mega-wiki, this skill treats the **current working directory as a mini wiki boundary**. New sources dropped into `raw/` get integrated into a small, local markdown knowledge base that stays useful for the project at hand.

## Novice Quickstart

If you do not know how the internals work yet, start with one plain request:

```text
Turn this folder into a maintained local wiki. Keep the setup simple and ask only what you need before starting.
```

The agent should ask at most three first-run questions:

1. What should this wiki remember over time?
2. What source material exists now, and what kind of sources will keep arriving?
3. How autonomous should I be while organizing it?
   - A) Do it and show results
   - B) Show key takeaways before shaping
   - C) Process one source at a time with review

You do not need to know the internal folder names before the first useful result. After bootstrapping, start from `wiki/home.md`.

If the folder is empty, choose a starter pack first:

- personal knowledge
- research/deep dive
- project handoff
- book/course notes
- business/team wiki

If there is still not enough seed material, answer this instead:

```text
Here are three things this wiki should remember first:
1. ...
2. ...
3. ...
```

Advanced bridge/export and graph-style relationship maps are optional later layers. They are not required for first use, and external/global writes require explicit approval.

## Why this exists

Karpathy’s core idea is excellent: let the LLM maintain a persistent wiki instead of rediscovering knowledge from raw documents on every question.

The practical problem is scope. In day-to-day engineering, research, due diligence, and project work, a single giant knowledge base becomes expensive to maintain and noisy to query. `llm-wikify` narrows the unit of maintenance to the **active repo or task folder**.

That gives you a better default:

- smaller wiki surface area
- faster navigation for humans and agents
- easier provenance and maintenance
- cleaner ingestion of new materials into the current project
- less temptation to over-abstract everything into a personal PKM empire

## Features

- **Task-local wiki boundary** — the working directory is the wiki unless the user explicitly asks for something broader
- **Bootstrap mode** — creates a small, MECE wiki structure when no wiki exists yet
- **Ingest mode** — reads new materials from `raw/` and integrates them into source pages, topic pages, and indexes
- **Scientific paper ingest mode** — ingests PDFs, TeX bundles, bibliography files, supplements, or converted paper Markdown and attempts to create structured paper source notes, topic updates, citation context, and local research maps; completeness depends on extraction quality and available metadata
- **Maintenance mode** — audits stale pages, broken links, orphans, duplicates, and weak navigation
- **Provenance-first workflow** — preserves where claims came from instead of turning source material into unsupported summary sludge
- **Minimal structure bias** — creates only the folders and pages justified by the current project
- **Optional umbrella-domain clusters** — for one large coherent domain, adds evidence-driven cluster mini-wikis without making them the default
- **Grounding requirement** — durable pages should say what repo landmarks, source notes, or raw inputs they were built from
- **Idempotent ingest bias** — the same source should update stable notes and pages, not create duplicate wiki clutter
- **Compound knowledge** — useful query answers can be filed back into the wiki instead of vanishing into chat history
- **Bridge / promotion packets** — reusable local knowledge can be packaged for a global `llm-wiki` or cross-project map without silently breaking the local boundary
- **Stronger health gates** — maintenance can check boundary, provenance, promotion, contradiction, taxonomy/schema drift, and source drift
- **Optional research graph artifacts** — mature paper wikis can keep local `edges.jsonl`, `citations.jsonl`, `gaps.md`, `context.md`, or `.ingest-manifest.json` files without requiring an external graph backend

## When to Use

Use `llm-wikify` when you want to:

- turn a repo or task directory into a persistent markdown knowledge base
- ingest new source files, notes, URLs, exports, or transcripts into `raw/`
- ingest scientific papers from PDF, TeX/LaTeX source bundles, bibliography files, supplements, or converted Markdown while attempting to preserve citations and provenance; completeness depends on extraction quality and source format
- keep project understanding stable across sessions
- maintain a small wiki for research, engineering, due diligence, planning, or documentation work
- organize one large coherent domain into an umbrella map and cluster reading paths, when a flat topic list is no longer enough
- health-check and clean up an existing local wiki

Do **not** use it when you only need:

- a one-shot summary
- generic markdown cleanup
- a full personal-vault redesign
- a global PKM taxonomy spanning many unrelated projects

## Quick Start

### 1. Optional skill installation

> [!TIP]
> If your LLM agent can run shell commands, you can copy the block below, paste it into the chat, and let the agent install the skill automatically.

```text
Install the llm-wikify skill for me.
1. git clone <repo-url> /tmp/llm-wikify
2. mkdir -p ~/.claude/skills/llm-wikify
3. cp -r /tmp/llm-wikify/SKILL.md /tmp/llm-wikify/assets /tmp/llm-wikify/evals ~/.claude/skills/llm-wikify/
4. cp /tmp/llm-wikify/generate_cover.sh ~/.claude/skills/llm-wikify/
5. chmod +x ~/.claude/skills/llm-wikify/generate_cover.sh
6. test -f ~/.claude/skills/llm-wikify/SKILL.md && echo "OK: llm-wikify installed"
7. Say "llm-wikify installed successfully"
```

For other tools, change the target skills path:

- Codex CLI: `~/.codex/skills/llm-wikify/`
- OpenCode: `~/.config/opencode/skills/llm-wikify/`
- Gemini CLI: `~/.gemini/skills/llm-wikify/`

### 2. Add source material when you have it

Examples:

- clipped articles
- PDFs converted to markdown
- scientific PDFs, TeX bundles, `.bib` files, and paper supplements
- meeting notes
- interview transcripts
- copied docs
- URLs the agent should ingest

### 3. Ask your agent to wikify the current directory

Example prompts:

```text
Turn this working directory into a small local wiki.
Bootstrap only the minimum structure we need.
```

```text
Ingest the files in raw/ into this project wiki.
Preserve provenance and avoid one giant dump page.
```

```text
Ingest the scientific papers in raw/papers/ into this local wiki.
Use paper source notes, preserve metadata/citations, connect reusable methods and open questions into topic pages, and do not rewrite raw files.
```

```text
Lint and maintain the wiki in this directory.
Fix safe issues and leave a short maintenance report.
```

### 4. Let the wiki compound

Over time, the agent should update:

- `wiki/home.md`
- `wiki/index.md`
- topic pages
- source notes
- bridge/export packets when knowledge should be promoted
- maintenance logs

The raw material stays raw. The wiki becomes the maintained synthesis layer.

## Workflow

### Bootstrap

If the wiki does not exist, `llm-wikify` should:

1. inspect the current directory first
2. preserve existing docs instead of duplicating them
3. create a minimal folder structure
4. seed `home.md`, `index.md`, and a few grounded pages
5. define local rules in `schema/wiki-rules.md`

### Ingest

When new material appears in `raw/`, the skill should:

1. read the source
2. create or update a source note
3. update related topic/entity pages
4. mark uncertainty where evidence is weak or partial
5. record the ingest in `log/log.md`

### Scientific paper ingest

When `raw/` contains research papers, the skill should:

1. classify the source as PDF, TeX bundle, converted Markdown, bibliography, supplement, or mixed paper source
2. use a safe extraction path when needed, such as MarkItDown, a paper-converter skill, direct TeX reading, or an existing Markdown conversion
3. create or update one stable paper source note in `wiki/sources/`, using the paper template when available
4. record extractable fields such as metadata, abstract, problem, method, assumptions, datasets, results, limitations, open questions, figures/tables, equations, and citation context; mark missing or uncertain items for review
5. deduplicate before creating new topic/entity/shared pages, then update only durable reusable concepts or claims
6. optionally maintain local research artifacts such as `wiki/graph/edges.jsonl`, `wiki/graph/citations.jsonl`, `wiki/gaps.md`, `wiki/context.md`, or `.ingest-manifest.json` when the wiki is large enough to benefit

This mode is inspired by structured research-wiki patterns, but keeps `llm-wikify` local-first: no mandatory parser, no required graph backend, and no external/global writes without approval.

### Query

When the user asks a project question, the agent should:

1. read `wiki/index.md`
2. follow relevant local pages
3. answer using the maintained wiki
4. file durable analyses back into the wiki when they are worth keeping

### Optional large-domain / cluster mode

For a large but coherent domain inside one working directory — for example Gas Hydrates, LLM Agents, or Process Simulation — the agent may add an umbrella map plus cluster mini-wikis. This is optional and evidence-driven: stay flat while `wiki/topics/` remains navigable, use clusters only when stable sub-domains recur across sources or queries, and split a cluster into a separate project wiki when it has its own ownership, audience, confidentiality boundary, source stream, or maintenance cadence.

Clustered wikis still obey the same local boundary. `wiki/shared/` is only for cross-cluster glossary terms, canonical concepts, shared decisions, or reusable comparisons; it is not a `misc` bucket. Graph or relationship maps remain optional local reports, not a required backend.

### Bridge / promote

When local knowledge becomes useful outside the project, the agent should:

1. keep the project wiki as the source of truth for local facts
2. create a local `wiki/bridges/<slug>.md` export packet
3. separate portable concepts from repo-specific details
4. cite local topic/source/raw evidence
5. ask for explicit approval before writing to any external wiki, vault, graph database, or another project

### Optional graph / relationship lens

After the local wiki has enough maintained pages, an agent may optionally generate graph-style relationship maps or reports inside the current working directory. This remains an advanced lens, not a required dependency or first-run concept. External graph databases or vault writes require explicit approval.

### Lint / maintain

The skill should periodically check for:

- stale pages
- broken links
- orphan pages
- duplicate topics
- inconsistent naming
- weak summaries
- raw-ingestion leftovers

Then it should make safe fixes and leave a maintenance report.

It should not pass maintenance by producing neat-looking indexes and reports without real cleanup.

## Repo Layout

```text
.
├── SKILL.md
├── README.md
├── README-ko.md
├── cover.png
├── generate_cover.sh
├── assets/
│   ├── home-template.md
│   ├── maintenance-report-template.md
│   ├── paper-source-note-template.md
│   ├── source-note-template.md
│   └── wiki-rules-template.md
└── evals/
    └── evals.json
```

## Default Folder Contract for Wikified Projects

The skill’s default target shape is intentionally small:

```text
raw/
wiki/
  home.md
  index.md
  topics/
  entities/
  sources/
  bridges/   # optional local export packets for global/cross-project promotion
schema/
  wiki-rules.md
log/
  log.md
```

This is a **starter contract**, not a prison. If the project clearly needs less, use less.

For one large coherent domain, the agent may use an optional clustered shape only when the source material justifies it:

```text
raw/
wiki/
  home.md                 # umbrella start page
  index.md                # umbrella catalog and cluster map
  topics/                 # domain-wide topics only
  shared/                 # cross-cluster glossary, canonical concepts, shared comparisons
  clusters/
    <cluster>/
      home.md             # cluster start page
      topics/             # cluster-local topics, only if justified
      sources/            # cluster-local source notes, only if useful for provenance
      comparisons/        # cluster-local comparisons, only if repeatedly useful
  bridges/                # local export packets; external writes still require approval
schema/
  wiki-rules.md
log/
  log.md
```

Use this only when there are recurring sub-domains under the same local boundary. If a cluster has a different lifecycle, audience, privacy boundary, source stream, or maintenance owner, make it a separate project wiki or ask before reorganizing.

Scientific paper wikis may additionally keep local-only research artifacts such as `wiki/graph/edges.jsonl`, `wiki/graph/citations.jsonl`, `wiki/gaps.md`, `wiki/context.md`, or `.ingest-manifest.json` when the paper corpus is large enough to benefit. These are maintained wiki outputs, not raw sources, and they are not part of the default starter structure.

## Design Principles

### 1. Local first
The project directory is the knowledge boundary.

### 2. Incremental over regenerative
Update related pages when new sources arrive. Do not rebuild everything by default.

### 3. Provenance over vibes
Important claims should point back to source notes or raw material.

### 4. Navigation over volume
Make pages easier to enter and follow. More pages are not automatically better.

### 5. Maintenance is the product
The wiki is only useful if the agent keeps it coherent as new material arrives.

## Inspiration

This skill is directly inspired by Karpathy’s `llm-wiki` idea: a persistent wiki maintained by the model instead of repeated chunk retrieval from raw sources.

`llm-wikify` narrows that pattern to a more practical default for everyday work: **one task directory, one maintained mini wiki**.

## Validation

The repo includes pressure prompts in `evals/evals.json` covering the main failure-prone modes:

- novice onboarding without exposing internals too early
- empty-folder starter-pack flow
- bootstrap of a local wiki from a messy repo
- ingest of mixed materials from `raw/`
- scientific paper ingest for PDF/Markdown papers, TeX bundles, and idempotent re-ingest drift
- maintenance without flattening the wiki into one file
- bridge/export boundaries for cross-project synthesis
- optional graph-lens deferral
- privacy and public-repo portability

Those prompts are meant to catch the common baseline failure: a generic agent says sensible things, but lacks a disciplined local-wiki operating contract.

The expanded eval set also checks the boundary tension: the agent should not over-globalize by editing external stores silently, but also should not over-localize by refusing useful cross-project synthesis. The expected move is a grounded local bridge packet plus an explicit approval boundary.
