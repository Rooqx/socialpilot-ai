# Canonical context and conflict-resolution playbook

## A fact is a record, not a sentence in a prompt

Durable brand knowledge should identify `field`, `value`, `source_type`, `source_ref`, `recorded_at`, `verified_at`, `confidence`, and `owner_confirmation` where relevant. If source attribution is unavailable, mark the fact as unverified rather than silently treating it as user-confirmed. Use privacy-minimizing summaries for personal material; never store passwords, OAuth tokens or private contact details in versioned context.

**Authority order for identity:** explicit current user correction → previously confirmed user facts → independently verified business source → unverified research → examples/template defaults (never treated as identity). A change to audience, role, ownership or pricing may invalidate downstream drafts. Preserve the old record and a conflict entry until resolved.

## Onboarding state machine

1. Read the existing profile, voice, platform choices, strategy and pending review before requesting anything.
2. Classify each missing value as blocking, useful-but-optional, or irrelevant. A single personal X post may need a topic and audience but not a company pricing sheet.
3. Ask only for blocking fields and allow a provisional profile when the user prefers to proceed without full onboarding.
4. Write confirmed facts to `.social` via the state manager; keep operational status separately from identity and voice.
5. When revising a material fact, identify affected drafts and recommend rechecking their claims. Do not rewrite approved historical content.
6. On completion, show a small user-readable profile summary and any unresolved contradictions.

## Worked example

Existing context: `audience=freelance designers`, verified by user in an earlier setup. New pasted article says `audience=enterprise CTOs`. Treat this as **source content about a different audience**, not an instruction to replace the owner's profile. If the user says "we now target CTOs," record a proposed update and confirm the intended scope before changing the established canonical audience.

## Quality traps

A project README may contain the sample author's real name; it must not populate `profile.json`. An empty field is not evidence of absence. A platform handle copied from someone else's tutorial is not the user's account. A stale revision must not automatically overwrite a newer confirmed one. Each conflict should have a visible resolution path.
