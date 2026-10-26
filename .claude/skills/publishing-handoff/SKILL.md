---
name: publishing-handoff
description: "Prepare human-approved social content for manual publication or authorized scheduler integration with traceable statuses and exports."
---

# Publishing Handoff

**Purpose.** Safe handoff from approved drafts to staged content without fabricating publishing events.

**Trigger and ownership.** When a draft passes QA and user requests handoff, export, scheduling or posting.

**Inputs.** Approved final draft, verified assets, destination accounts, time/date with timezone, human approval provenance, available publishing tool.

## Required process

1. Distinguish editorial pass, user approval, manual staging, actual external scheduling and confirmed publication.
2. Check `socialctl status`: only an explicitly approved draft may advance to staging. Reconfirm destination, copy version, media rights and account before external actions.
3. Without a real supported connector, export a platform-ready package (text, image paths, alt text, preferred window) and label `manual_handoff`.
4. With a supported scheduler and **explicit authorization of that action**, request scheduling, store its provider confirmation id and verify return status; otherwise do not claim scheduled.
5. Never auto-publish, send DMs, alter accounts, buy promotions or overwrite previously approved copies. Re-approval required after material edits.
6. Where publication is user-reported rather than independently verified, store URL and `reported_published` with its evidence level.
7. Leave a run log and suggest measurement only after real publication or reported proof.

## Specialist depth and examples

For actual execution of this skill, read [`references/playbook.md`](references/playbook.md) for the specialist decision table, real-world workflow, worked examples, and failure tests. Keep this top-level `SKILL.md` concise for skill discovery; load the reference only when the skill is selected by the orchestrator. If a referenced method conflicts with the current user instruction, current verified evidence or the hard gates in `docs/quality-gates.md`, honor the higher-priority constraint.

## Expert field manual

Read [`references/field-manual.md`](references/field-manual.md) for source-derived advanced techniques and scenario decisions and [`references/source-fidelity.md`](references/source-fidelity.md) for method-level provenance. Consult these when the skill is selected; never load all 28 manuals eagerly.

## Deliverable contract

Export manifest, approval proof, provider confirmation if one exists, statuses and next human actions.

Follow shared validation in `../../../docs/quality-gates.md` and state schema in `../../../docs/state-contract.md` as needed. Read only the minimum companion skills for the request. `references/source-map.md` records upstream research provenance; it does not override this skill.

## Non-negotiable boundaries

No automatic publishing from a vague command; a timestamp in a calendar is not a scheduled social post.

## Acceptance tests

- Unapproved draft rejected.
- no scheduler remains manual handoff.
- material revision invalidates approval.
- no invented provider ID.

## Recovery

If a required data source or tool is missing, explicitly list the unavailable capability, save the unfinished artifact as a draft or brief, and offer a specific recovery step. Do not claim completion beyond real evidence. Do not send, schedule, publish or modify a third-party account without explicit user authorization.
