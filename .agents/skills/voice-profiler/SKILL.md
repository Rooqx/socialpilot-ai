---
name: voice-profiler
description: "Infer an author-specific voice profile from their own writing samples and use it to keep social media drafts authentic across platforms."
---

# Voice Profiler

**Purpose.** Evidence-based voice description without overfitting or impersonating a repository maintainer.

**Trigger and ownership.** First brand onboarding, major voice refresh, or posts that feel unlike their actual author.

**Inputs.** At least three author-supplied texts ideally, content goals, platforms, optional samples the user approves as representative.

## Required process

1. Ask for 3–5 representative samples, or start with an explicitly provisional voice when none exists. Do not substitute generic sample-content files for the user.
2. Observe sentence length, cadence, punctuation, point of view, favored technical level, humor, storytelling, openings, endings and recurring phrasing.
3. Distinguish deliberate traits from accidents: do not replicate typos or sensitive disclosures merely because they occur in samples.
4. Write `voice.json` with evidence-backed rules: `do`, `avoid`, `examples`, `tone_by_platform`, and `confidence`. Quote only short user-owned examples.
5. Test with two short post drafts in distinct contexts and ask the user which more closely matches them. Update explicit preferences, not guesses.
6. Recheck after authentic posts are approved; keep manual edits as evidence, but do not infer a new immutable voice from one edit.

## Specialist depth and examples

For actual execution of this skill, read [`references/playbook.md`](references/playbook.md) for the specialist decision table, real-world workflow, worked examples, and failure tests. Keep this top-level `SKILL.md` concise for skill discovery; load the reference only when the skill is selected by the orchestrator. If a referenced method conflicts with the current user instruction, current verified evidence or the hard gates in `docs/quality-gates.md`, honor the higher-priority constraint.

## Expert field manual

Read [`references/field-manual.md`](references/field-manual.md) for source-derived advanced techniques and scenario decisions and [`references/source-fidelity.md`](references/source-fidelity.md) for method-level provenance. Consult these when the skill is selected; never load all 28 manuals eagerly.

## Deliverable contract

Persistent voice profile with examples, evidence sources, prohibited habits and platform adaptations.

Follow shared validation in `../../../docs/quality-gates.md` and state schema in `../../../docs/state-contract.md` as needed. Read only the minimum companion skills for the request. `references/source-map.md` records upstream research provenance; it does not override this skill.

## Non-negotiable boundaries

Never claim perfect imitation, borrow someone else’s identity, or treat invented samples as authentic.

## Acceptance tests

- No samples produces provisional label.
- samples influence draft.
- conflicting voice evidence flagged.
- personal voice survives copy editing.

## Recovery

If a required data source or tool is missing, explicitly list the unavailable capability, save the unfinished artifact as a draft or brief, and offer a specific recovery step. Do not claim completion beyond real evidence. Do not send, schedule, publish or modify a third-party account without explicit user authorization.
