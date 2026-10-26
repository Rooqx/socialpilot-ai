# X single-post writing patterns

## Decide what deserves one post

One post should make one defensible point. A small observation, precise tip, meaningful question or compact example fits. A setup with three independent steps and caveats likely belongs in a thread. Don't force all details into a sentence that misleads by omission.

## Native structures

**Observation → explanation:** a specific engineering behavior followed by why it matters. **Mistake → corrected heuristic:** name the concrete bug, explain the principle, avoid overstating universal rules. **Question → considered answer:** pose a real dilemma with a qualified stance. **Resource → takeaway:** link a credible source only when actually verified and offer the useful summary in the post itself.

## Practical workflow

1. Identify the intended reader and a single takeaway. Load verified voice and any prior examples.
2. Draft the main claim without a hook; ensure the claim itself is worth sharing.
3. Add a short opening with immediate context. Remove generic intros, decorative hashtags, automated thread markers and needless emojis unless consistent with voice.
4. Review Unicode/URL limits with current account-aware rules if the output is to be handed off. Do not promise a single universal character limit for every account.
5. For technical examples, check that the code behavior or measurement is accurate. For first-person stories, confirm actual authorship.
6. Supply the post alone in the publish-ready text field, with verification notes separately, then save as draft.

## Worked example

Topic: deploying a server-side app with environment variables. Generic: "Deployments are tough but never give up!" Concrete alternative: "A deployment can pass CI and still fail on first request if the production environment doesn't have the values your local `.env` supplied. Check the required runtime variables before the release." Confirm project-specific details before making this first-person.

## QA questions

Does every sentence reinforce one point? Is an unsupported number slipped in? Would the text stand on its own without clicking a link? Are instructions for readers accurate? Does the requested output contain precisely the requested number of posts?
