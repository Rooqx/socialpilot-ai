# Editorial gold-standard fixtures — fictional educational examples, NOT user-owned stories

These examples illustrate the expected editorial bar and can be used in human evaluation. They are **not evidence of live agent execution**, not guaranteed to grow an account, and should not be published as an author's personal experience without author approval.

## X single post — complete insight, no bait

A timeout doesn't always mean your API operation failed. The server may have committed before the response was lost. If retries can cause side effects, use an idempotency key so repeating a request doesn't repeat the outcome.

**What works:** real technical insight, useful distinction, specific action, no fabricated result, natural close. **What needs checking:** domain-specific correctness for the actual target system and standard X composer count.

## LinkedIn — decision, tradeoff and transferable lesson

**A timeout can hide a successful write.**

A client sends a request. The server commits the change. The response disappears on the way back.

From the client's perspective, it looks like a failure. But retrying blindly may repeat the operation.

For side-effecting endpoints, an idempotency key gives the server a way to recognize an already-processed request and return a consistent outcome.

There is a tradeoff: key storage needs an expiry policy, and requests with reused keys but changed payloads need clear handling.

The lesson isn't “never retry.” It's to design retries around the actual business operation, not just the network response.

**What works:** specific scenario, practical mechanism, caveat, no fictitious personal success. **What needs checking:** technical scope; invite owner to add a genuine experience if available.

## Instagram carousel — explanatory narrative + matching caption

| Slide | Headline | Key point | Suggested visual |
|---|---|---|---|
| 1 | A timeout can fool you | The response vanished; the operation may not have | Request path with lost reply |
| 2 | What the client sees | No response | Phone/client with timeout icon |
| 3 | What the server did | The write may already be committed | Database write checkmark |
| 4 | The retry hazard | Blind retry may duplicate a side effect | Two arrows to one operation |
| 5 | Safer approach | Recognize repeated intent with an idempotency key | Key-to-result mapping |
| 6 | The caveat | Handle expiry and changed payloads explicitly | Small conditions checklist |

**Caption:** “A network timeout tells you the reply didn't arrive—not necessarily that the operation failed. These six slides show why that matters when you build retryable APIs, plus one design pattern worth considering.”

**Media status:** storyboard/brief only, not rendered. Verify technical details and dimensions before actual release. Add truthful alt text to produced assets.

## What to measure (if posted with permission)

Use post-level reach/impressions if provided, actual replies and saves, qualified profile visits and measured follower changes. Account for sample size and publication date. Never infer causality from one post or a single viral spike.
