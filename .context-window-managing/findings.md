# Findings

## Local repo state
- Current repo root is effectively empty except for `.context-window-managing/`.
- No local `SKILL.md`, `README.md`, `assets/`, `scripts/`, plugin manifest, or skill directory exists yet.
- Cleanest repo shape is a dedicated top-level folder: `llm-wikify/`.

## Local reference repos

### `../14_autoresearch-skill/`
- Strongest README template for a “stargazing-like” skill repo.
- Top-level structure includes `SKILL.md`, `README.md`, `assets/`, `scripts/`, `.claude-plugin/`, `.codex/`, `generate_cover.py`, and `cover.png`.
- README pattern:
  - full-width hero image
  - centered title and tagline
  - anchor-nav row + badges
  - early proof/demo section before long prose
  - features, quick start, install matrix, usage, and workflow explanation
- `generate_cover.py` is a concise Pillow+NumPy script with dark-base + blurred-color-blob + glow-text style.

### `../15_autoconference-skill/`
- Confirms the same README visual language is reused across multiple successful sibling repos.
- Helpful for “commands table” and “how it works” section structure.
- Includes richer example/demo embeds inside the README.

### `../17_my-frontend-design-skill/`
- Best local source for a more reusable `generate_cover.py` implementation.
- Uses cleaner helper functions and better cross-platform font discovery than the older scripts.
- Also includes `evals/evals.json`, which is a useful local precedent for skill validation artifacts.

## Implications for llm-wikify
- `llm-wikify` should be a standalone skill repo, not a loose single-file skill.
- Minimum practical structure should likely include:
  - `llm-wikify/SKILL.md`
  - `llm-wikify/README.md`
  - `llm-wikify/generate_cover.py`
  - `llm-wikify/cover.png`
  - `llm-wikify/assets/` for templates or starter schemas
  - `llm-wikify/evals/evals.json` for baseline + post-skill tests
- The skill’s differentiator versus Karpathy’s original pattern should be explicit:
  - treat the current working directory as a mini wiki
  - optimize for task-scoped maintenance, not one giant universal vault
  - support bootstrap mode and maintenance mode
  - ingest from `raw/` and organize/update wiki pages incrementally

## Initial skill-design direction
- Use a small MECE folder model rooted in the task directory, likely separating:
  - `raw/` immutable source inputs
  - `wiki/` generated/maintained knowledge pages
  - `schema/` conventions and maintenance rules
  - `log/` ingest/query/lint history
- Keep SKILL.md focused on:
  - when to trigger
  - how to bootstrap if structure is missing
  - how to ingest one new source cleanly
  - how to answer user questions against the local wiki and file the result back in
  - how to lint and health-check the wiki

## Validation direction
- RED phase should capture baseline failures from “no skill” runs on prompts that require disciplined wiki maintenance.
- Post-implementation validation should include:
  - direct skill-file review
  - eval prompts in `evals/evals.json`
  - overheating / devil’s-advocate stress test requested by user
  - explicit review of whether the skill over-builds a giant centralized wiki instead of a task-local one
