# Technique-by-technique source fidelity — publishing-handoff

This ledger maps **re-authored editorial/operational techniques** to their upstream intellectual sources. It is not a claim of verbatim import or exhaustive preservation of every upstream sentence. Each method is reviewed for portability, current platform evidence, and risks.

| Method | Specialist implementation | Origin / rationale |
|---|---|---|
| M01 Package identity | Bind platform, account destination, post format, exact copy hash, approved media manifest, alt text and planned local time/timezone | Anthropic social-content-engine publishing handoff |
| M02 Approval separation | QA readiness and user authorization are separate checkpoints | Corey loop-guardrails |
| M03 Preflight live limitations | Verify platform specs and account capabilities where relevant; missing media or inaccurate destinations halt rather than silently substituting | Kostja platform output rules |
| M04 Idempotent staging | Generate a unique stable handoff key | Corey loop-state idempotency |
| M05 Truthful outcome | Report manual_export, scheduled_confirmed or published_confirmed only from appropriate evidence | Anthropic publishing reference and current socialctl semantics |

## Pinned upstream links

- [coreyhaines31/marketingskills: `skills/marketing-loops/SKILL.md`](https://github.com/coreyhaines31/marketingskills/blob/e85f3cbc2e4a79bf33b2a12e9bdd9087d414735b/skills/marketing-loops/SKILL.md)

## Editorial review obligation

Before release, independently compare the consolidated methods and examples against these original files. The presence of links does not prove every sentence was retained. Register omissions, conflicts and tool prerequisites explicitly.
