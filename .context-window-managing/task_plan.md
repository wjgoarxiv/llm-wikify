# Task Plan

## Goal
Create a new skill repo `llm-wikify` that turns the current task-working directory into a mini LLM-maintained wiki.

The skill must:
1. Bootstrap an MECE wiki structure when none exists.
2. Ingest new resources dropped into `raw/` and integrate them into the mini wiki.
3. Keep the wiki task-local instead of forcing one giant global wiki.
4. Ship with a polished README, a generated cover PNG, and validation artifacts.
5. Include overheating / devil's-advocate style pressure testing after implementation.

## Phases
- [x] Explore local repo state and sibling skill examples
- [x] Extract README and cover-image conventions from sibling projects
- [ ] Define llm-wikify scope, folder schema, acceptance criteria, and baseline eval prompts
- [ ] Run RED-phase baseline prompts without the new skill and capture failure patterns
- [ ] Implement llm-wikify repo structure, SKILL.md, templates, and supporting assets
- [ ] Write polished README and build cover.png via local generator script
- [ ] Run validation, pressure tests, and overheating/devil's-advocate checks

## Acceptance Criteria
- A top-level `llm-wikify/` skill repo exists with at least `SKILL.md`, `README.md`, `generate_cover.py`, and `cover.png`.
- The skill instructions clearly distinguish raw sources, generated wiki pages, schema/rules, and maintenance workflows.
- The skill explicitly supports both bootstrap mode (no wiki yet) and maintenance mode (wiki already exists).
- The README follows the strong local style: hero image, centered framing, features, install, usage, and workflow explanation.
- A reusable cover-image script exists and successfully generates `cover.png` locally.
- Baseline prompts and post-skill validation prompts are captured in `evals/evals.json`.
- At least one pressure-testing pass documents failure modes or review findings, not just a self-claim that the skill is good.

## Notes
- Local reference repos: `../14_autoresearch-skill/`, `../15_autoconference-skill/`, `../17_my-frontend-design-skill/`.
- Primary README template source: `14_autoresearch-skill/README.md`.
- Primary cover-script source: `17_my-frontend-design-skill/generate_cover.py` font-fallback structure + `14_autoresearch-skill` visual recipe.
- Use `llm-wikify/` as the new top-level destination because the current repo root is otherwise empty except for workspace notes.
