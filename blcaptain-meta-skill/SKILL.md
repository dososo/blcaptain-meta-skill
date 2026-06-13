---
name: blcaptain-meta-skill
description: Use when explicitly turning a repeated workflow, SOP, prompt, document, expert process, or tool routine into a reusable Agent Skill package, or improving, validating, packaging, publishing, or governing an existing Claude/Codex/Agent Skill; especially for SKILL.md, references/scripts/assets, evals, gotchas, route tests, Non-Skill decisions, and lifecycle governance.
---

# BLCaptain Meta Skill

## Contract

Productize only repeated high-value workflows worth becoming Agent Skills. Keep the entrypoint thin, move detail into resources, prove behavior, and keep audit evidence.

## First Move

Inspect source or existing skill. Run the Non-Skill gate. For new Codex skills, prefer `skill-creator`. Track baseline, decisions, files, commands, and risks.

## Workflow

Follow in order: **Research** queries/artifacts/failures → **Analyze** NABC/ROI/boundaries → **Plan** tier/files/evals/gates → **Develop** metadata, thin `SKILL.md`, resources, scripts, templates, examples, evals, manifest → **Validate** structure/links/context/scripts/security → **Test** baseline, positive, negative, near-neighbor, execution, pressure, regression → **Audit** blockers → **Summarize** proof and risks.

## Resource Loading

- Stage 0 proof: `references/00-real-delivery-first.md`.
- Non-Skill gate: `references/01-non-skill-decision.md`.
- Structure/description/packaging/templates: `references/02-skill-design-and-packaging.md`.
- Evals/routes/baseline/near-neighbor/failures: `references/03-eval-protocol.md`.
- Permissions/scripts/supply chain: `references/04-safety-and-supply-chain.md`.
- Release/governance/versioning: `references/05-governance-and-operations.md`.
- Platform differences: `references/06-platform-differences.md`.
- Role handoffs: `references/07-role-playbooks.md`.
- Worked example: `examples/three-scenario-worked-examples.md`.
- Visual creator example: `examples/visual-card-validation.md`.
- Route fixtures: `evals/route_cases.json`.
- Scenario fixtures: `evals/scenario_cases.json`.
- Failure families: `evals/failure_library.json`.
- Forward-test evidence: `evals/forward_test_results.json`.
- Regression history: `evals/regression_history.json`.
- Platform schema/tokenizer check: `evals/platform_schema_tokenizer_check.json`.
- Templates: `assets/templates/skill-brief.md`, `assets/templates/skill-design-spec.md`, `assets/templates/eval-case.md`, `assets/templates/gotcha.md`, `assets/templates/iteration-record.md`, `assets/templates/governance-manifest.json`.

## Build Rules

- `description` routes; it is not marketing.
- Keep `SKILL.md` small; move detail, checks, and skeletons to resources.
- Create only behavior/evidence-bearing files.
- Use real failures for gotchas.
- Require runnable scripts; never include secrets, destructive defaults, or policy-bypass text.

## Useful Commands

```bash
python3 scripts/validate_meta_skill.py .
python3 scripts/context_budget.py SKILL.md
uv run --with tiktoken python scripts/context_budget.py SKILL.md --tokenizer openai --encoding o200k_base
python3 scripts/eval_routes.py evals/route_cases.json
```

For Codex structure, also run:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" .
```

`context_budget.py` defaults to an offline heuristic and supports OpenAI `tiktoken` when installed. `agents/openai.yaml` follows local `skill-creator` guidance; recheck target schema before public release.

## Output Contract

Report: decision, files/reasons, evidence, blockers/risks, next iteration.

## Gotchas

- Do not build a Skill just because the source material is long.
- Do not turn one-off explanation, summary, translation, or brainstorming into a Skill.
- Do not put the whole PRD into `SKILL.md`.
- Do not treat fixture eval as real model forward-test.
- Do not add governance files to hide missing real examples, evals, or gotchas.
- Do not call a package publishable if scripts cannot run or resources cannot be found.
