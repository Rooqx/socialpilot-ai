# Exact-content approval and external-action boundaries

## Two distinct permissions

**Editorial approval** covers this exact text/media version for the creator's review process. **Platform action authorization** specifies the destination account, action (post or schedule), chosen material and time. Neither should be inferred from "start posting" or a saved profile.

## Manual export contract

1. Confirm the draft identity and content SHA from the local state. QA must pass and the user must explicitly approve the exact version.
2. Verify the intended platform and account, visual rights and media readiness, current mandatory platform constraints, and whether an external integration exists.
3. Without a supported and authorized integration, call local `stage` only to export a handoff package. Explicitly state "not scheduled and not published."
4. Record `manual_handoff`, not `published`. If user later provides a post URL, mark only `reported_published`; do not imply the platform was queried.
5. Treat any material edit after approval as a *new review cycle*. An updated image caption, time-sensitive claim or replacement media may require reapproval even if title stays the same.

## External integrations (future)

Before adding a provider adapter, implement a permission boundary, provider-specific idempotency token, dry-run mode where possible, retry policy without duplicate posts, explicit callback result handling and durable provider receipt. Separate `scheduled_confirmed` from `published_confirmed`; an HTTP request submitted is not proof of successful publication. The current repository contains no such connector.

## Failure scenarios

A user says "post all" but no accounts selected; a draft was changed after approval; a rate limit occurs mid-batch; a provider returns an ambiguous success; the image is missing; a manual URL points to a different account. Never advance status optimistically. Preserve evidence and ask for specific next action.
