# Intent routing and orchestration

**Core:** single orchestration decision per top-level user request. Load `social-orchestrator` and restore state first. Leaf skills do not create their own canonical identity files or restart the calendar.

| Natural-language intent | Minimum pipeline | Terminal state |
|---|---|---|
| “I want to start posting” | recover → missing profile/voice? `context-manager`, `voice-profiler` → `content-strategy` → `idea-pipeline` → `editorial-calendar` → writers → facts/editor/QA | onboarding questions or drafts for review |
| “Write five X posts” | recover → `idea-pipeline` only if needed → `x-post-writer` → `fact-checker` → `copy-editor` → `post-qa` | five separate drafts, no publication |
| “Create an X thread” | recover → `x-thread-writer` → claim QA → editing → QA | ordered thread draft |
| “LinkedIn post about my project” | recover → confirm actual project details → `linkedin-post-writer` → QA | post draft, source flags |
| “Instagram carousel about this” | recover → `carousel-storyboard` → `visual-brief` → optional `visual-asset-production` → `instagram-caption-writer` → QA | storyboard plus verified art when available; otherwise brief-only |
| “Make a Reel” | recover → `reel-scriptwriter` → caption/creative as authorized → QA | timed script, not fake finished video |
| “Use this article everywhere” | recover → `content-repurposer` → native writers → QA | adapted family of drafts |
| “What works lately?” | recover → `social-listening` / `source-research` → `idea-pipeline` | attributed ideas, data limitations |
| “What should I post this week?” | recover → inspect existing calendar/drafts → `editorial-calendar` | standing-calendar delta, not a reset |
| “Analyze my posts” | recover → `analytics-and-experiments` → `continuous-improvement` | observed report or explicit missing-data template |
| “Post this” | recover → `post-qa` → `publishing-handoff` **only after explicit approval** | local export unless supported service acts and confirms |

## State machine and recovery

- Fresh clone: `.social/` absent → `init` creates blank durable state → minimum onboarding. Author facts remain blank.
- Returning run: load `.social/state.json` and `.social/drafts/index.json` → list pending drafts and approvals → resume current stage.
- Repeated intent: stable idempotency key prevents identical draft creation from triggering multiple times.
- Draft transitions: `draft → needs_review (QA pass) → approved (human recorded) → manual_handoff (export) → reported_published (user-supplied link)`. Material revision returns to `draft` and invalidates QA/approval.
- Calendar is **planned only** unless a separate, supported external scheduler provides actual confirmation. `calendar` CLI never schedules anything.
- Without tools: no browsing → labeled unverified sources; no image tool → visual brief only; no analytics → request export; no scheduler → manual handoff.
- External account changes require a direct user request **at the time of action** regardless of approval record. A natural-language “start posting” does not authorize publication.

## Skill selection

Use one canonical skill for each task responsibility, not every plausible trigger. Orchestrator coordinates, context manager stores facts, profiler owns style, platform writers own text, fact checker owns claims, editor owns voice/readability, post QA owns readiness, handoff owns exports. `continuous-improvement` is never allowed to self-certify its own changes.
