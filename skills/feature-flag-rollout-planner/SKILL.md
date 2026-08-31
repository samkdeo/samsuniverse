---
name: feature-flag-rollout-planner
description: Plans a staged feature rollout behind a flag, including the ramp schedule and cohorts, the guardrail metrics to watch, the kill criteria that trigger a rollback, who is watching during each stage, and when the flag gets deleted. Use this skill whenever someone is about to ship something behind a feature flag, LaunchDarkly toggle, kill switch, canary, percentage rollout, or gradual release, and also when they ask "how should I roll this out", "what percentage should I start at", "when is it safe to go to 100", "what should I monitor during launch", or "how do I know if I should roll this back". Use it too when a rollout is already underway and going badly, or when someone wants a release plan reviewed before they ship.
---

# Feature Flag Rollout Planner

Produces a rollout plan for one change: the stages and their percentages, what gets measured at each stage, the numbers that mean stop, who is on the hook during each ramp, and the cleanup that removes the flag afterward. It covers the release mechanics. It is not experiment design, so if the goal is to measure whether a change is better rather than whether it is safe, the sample sizes and analysis belong in a proper A/B test and this plan only handles the safety side. It is also not incident response. If something is already broken in production right now, kill the flag first and plan afterward.

## Step 1: Classify the change

The plan hangs on this, so get it before anything else.

Ask what the change touches, and place it in one of these:

- Presentation only. UI, copy, layout. Cheap to reverse, low blast radius.
- Behavior change on an existing path. New logic in a flow people already use. Reversible, but users may have acted on it.
- New write path or data model change. This is the dangerous one, because turning the flag off does not undo the rows already written.
- Infrastructure or dependency swap. A new service, cache, or provider behind the same interface. Failure modes are often latency and error rate rather than anything visible.
- Money, permissions, or anything regulated. Billing, access control, data retention, anything with a compliance owner. Slowest ramp, most explicit sign-off.

Then decide how the assignment is stored. For anything with a multi-step or multi-day experience behind it, write the assignment onto the record once, at the moment of entry, and have every downstream consumer read that field rather than re-evaluating the flag. This is what stops a user from being flipped mid-flow, keeps two services from disagreeing during a deploy, and makes a flag-off clean by construction, since the existing cohort finishes and only new entrants get the old path.

Then ask the question people skip: what does turning the flag off actually restore? For anything that writes data, sends notifications, calls a third party, or charges someone, the flag is not a real undo button. Say so plainly and plan a data cleanup or a compensating action alongside the flag. A rollback plan that assumes the flag is sufficient, when it is not, is the single most common way a staged rollout still turns into an incident.

## Step 2: Fix the metrics before the ramp

First, decide whether the change can be wrong rather than broken. If it can return a plausible but incorrect answer, meaning a price, a total, a permission decision, a recommendation, or a calculation, then error rate and latency are not guardrails. They stay green through the entire failure. You need a correctness oracle instead, and you need it named before the ramp.

When the new path implements the same contract as the old one, which is the usual case for a service replacement, the oracle is the old implementation. Run both on real traffic, serve the old result, and compare. Do the new call out of band with a hard timeout so it can never affect the response or the latency. Log every comparison with the dimensions that matter, such as category, currency, jurisdiction, discount type, and customer tier. The exit condition is not a low mismatch rate. It is zero mismatches across a full traffic cycle, plus evidence that the long-tail combinations actually appeared in the sample. Every mismatch is either a bug or an intentional change nobody knew they were making, and each one needs a written decision before the ramp starts.

When there is no old implementation to compare against, name whatever substitute exists: a recomputation in a batch job, a sample checked by hand, an invariant that must always hold. Doing this after the ramp is remediation, not verification.

Then two sets of metrics, and both need a baseline number written down before stage one starts. A threshold with no baseline is unusable at 2am.

Guardrail metrics, which must not get worse:

- Error rate on the affected endpoints, and overall
- Latency, p50 and p95 or p99, on the affected path
- The completion rate of whatever flow the change sits in
- Support ticket or complaint volume, when the change is user-visible
- Anything downstream that the change could starve or flood, such as a queue depth or a database connection pool
- A metric specific to whatever the change does irreversibly. This is the one people skip, and it catches the worst realistic failure. If the change sends mail, count messages per recipient and alert on more than expected. If it charges, count charges per order. If it calls a partner API, count calls per record. A generic error rate will not catch a duplicate send, because every one of those requests succeeded.

Segment every metric by cohort, and alert on the new cohort's own numbers rather than the blended figure. At 1%, a bad new path is invisible in an aggregate error rate, and a monitor that cannot see the stage it is meant to watch turns the stage into a delay. Keeping the old cohort live also gives you a control that moves with seasonality and promotions, which a baseline captured last Tuesday does not.

Success metrics, which tell you the change did what it was for. For a like-for-like replacement, success is parity plus whatever motivated the swap, so write down the actual reason, whether that is cost, latency, or one fewer service to operate, and the number that would settle it. Name these too, since a rollout with no success metric ramps to 100% on the absence of complaints, and absence of complaints is not evidence that anything worked.

For each metric, record the current value, the acceptable range, and where you look at it. If a metric does not exist yet and the rollout needs it, that is work to do before stage one, not during it.

## Step 3: Build the ramp

First decide whether a percentage is even the right unit. Below roughly a few thousand events a day, percentages stop meaning anything and the ramp becomes counts and named cohorts: an internal allowlist, then a handful of specific records, then a segment. Rate-based metrics go with them. At twenty signups a day a 5% error rate is one user, so the guardrails become counts, and the first two stages are you reading each affected record by hand. Hand inspection of six records is the highest-value monitoring available at that volume and no dashboard replaces it.

When someone wants a large percentage immediately in order to get data faster, work out the arithmetic before arguing about it. At low volume, exposure percentage is rarely the constraint on how quickly a result arrives, and the measurement takes weeks whether the ramp took one day or eight. At high volume the argument is the opposite one and stronger: the small stages cost you no signal at all, because 1% of two million is plenty to see, so what the low stages buy is purely blast radius. The question there is not how fast the data arrives but how many wrong records you are willing to find. Either way, show the numbers and offer the date by which they will have the split they want.

Give the stages as a table, and make the correctness phase from step 2 the first row rather than a prerequisite mentioned elsewhere. It has a soak, a gate, and an owner like any other stage, and on a change that can be silently wrong it is usually the longest and most valuable one:

| Stage | Cohort | % | Minimum soak | Gate to advance | Who is watching |
|---|---|---|---|---|---|

Defaults to start from, adjusted by the classification in step 1:

1. Internal only. Employees or a test account list. Soak until someone has actually used it, not just until the clock runs out.
2. 1%. The first real exposure. This stage catches the errors that only appear with real data shapes.
3. 5 to 10%. Enough traffic for rate-based metrics to mean something.
4. 25 to 50%.
5. 100%.

Adjust the ladder for the classification, not just the volume. A presentation change can start at 10%. Anything touching money, permissions, or data integrity earns an extra stage below 1%, because that stage is controlling blast radius rather than gathering signal: at high traffic 1% is thousands of affected records a day, and the question is how many wrong ones you are willing to find. Never advance by a factor of ten, either. Something that is a rounding error at 10% can saturate a connection pool or a rate limit at 100%, and a 10x jump leaves you with no intermediate data point to interpret it against.

Soak times are governed by the slower of two clocks: the traffic cycle, and the change's own latency. If the change starts a multi-day email sequence, a trial, a billing cycle, or anything else that unfolds over days, then no stage advances until at least one record has been all the way through it. A flow that looks fine on day one and sends a wrong message on day four has not been tested by a one-day soak.

On the traffic clock, allow at least one full cycle per stage, which for most consumer products means a full day including the peak, and for business tools means a weekday. Anything with a weekly rhythm, such as payroll or reporting, needs a stage that spans the weekly peak. Do not let a rollout skip a stage because the metrics looked fine for an hour, since slow failures like memory growth, cache pollution, and queue backup take longer than that to show.

Gates are written as conditions, not as vibes: "error rate within 10% of baseline for 24 hours, no new sev-2 tickets referencing checkout, p95 under 400ms".

Plan for the deploy window, when the flag can be on in one service and off in another, or when two services disagree about who is in the cohort. Say what happens to a request caught in the middle. This is the partial failure that a plan written for the happy path misses.

On a hot path, check what the flag evaluation itself costs. An SDK evaluating locally against a cached ruleset is free; one making a network call per request adds its own latency and its own failure mode to the very path you are trying to protect.

Note the targeting mechanism too. Percentage rollouts need sticky bucketing on a stable identifier, so a user does not flip between old and new on every request. Say which identifier, and flag it when the change spans multiple services that need to agree on the same bucket.

## Step 4: Write the kill criteria as numbers

This is the section that gets skipped and the one that matters. Kill criteria are decided before the ramp starts, when nobody is stressed, and they are specific enough that the person on call at 3am can act without waking anyone up:

- The metric, the threshold, the duration, and the action. "5xx rate above 2% on /checkout for 5 minutes: kill the flag."
- Separate a kill, meaning flag to 0 immediately, from a hold, meaning stop ramping and investigate. Most signals are holds. Reserve kills for user-visible breakage, data corruption, and anything touching money.
- Name who is allowed to pull the trigger, and make that list long rather than short. If only one person can kill the flag and they're asleep, the criteria are decorative.
- State explicitly that killing the flag needs no approval. The default has to be that rolling back is cheap and blameless, otherwise people hesitate and a five-minute problem becomes a fifty-minute one.

Wire the top-tier kill conditions to fire automatically where you can. A monitor that flips the flag to zero and then pages is worth the day it takes to build, and it is close to mandatory for a small team running multi-day soaks with no overnight cover. The criteria are already written as machine-checkable conditions, so the step from a human executing them to a monitor executing them is short. Then rehearse it: have everyone on the kill list turn the flag off once during the internal stage, and time it. If it takes more than a minute from decision to zero traffic, fix that before real users are exposed.

Include the qualitative trigger too: if the on-call engineer thinks something is wrong but cannot point at a metric, that is grounds for a hold. Encode it so it doesn't need to be argued for in the moment.

## Step 5: Plan the watching

For each stage, say what is being watched, how, and by whom:

- Which dashboard, with the link if the user has it
- Which alerts fire automatically, and which conditions only a human will notice
- Who is on point during business hours, and what happens overnight and over the weekend

When one person owns the whole rollout, which is common, say so and fix it before stage one rather than writing a coverage plan that is really one name repeated. Get at least two more people access to the flag and a one-line runbook naming the flag and saying that turning it off needs no approval. A solo rollout also drifts, because nobody prompts the advance decision, so put each gate check on a calendar rather than trusting memory.

Set the ramp schedule around the coverage, not around eagerness. Do not schedule a stage advance for a Friday afternoon or the day before a holiday unless someone is genuinely available for the whole soak.

## Step 6: Plan the flag's death

Every flag gets a removal plan at creation time, or the codebase accumulates permanent dead branches that nobody can safely delete two years later. Include:

- The date or condition for removing the flag and the old code path, typically one to four weeks after 100%
- Who owns the removal, as a named person and a ticket, not a team
- Whether the flag is meant to be permanent, such as a genuine kill switch or an entitlement toggle. Those are legitimate but rare, and they should be labeled as permanent so they are not mistaken for cleanup debt.

## Step 7: Deliver

The plan comes back as: the classification and what a rollback actually restores, the metric table with baselines, the ramp table, the kill criteria, the monitoring assignments with the gate checks placed on a calendar, and the cleanup ticket. Add a short list of open questions where the user's answers were missing rather than assuming values, and state any assumption you had to make.

## Common failure modes to avoid

- Treating the flag as a rollback for a change that writes data, sends email, or moves money. Turning it off stops new damage and undoes none of the old damage.
- Kill criteria written as "if things look bad". At 3am nothing looks obviously bad until it is very bad.
- Copying the percentage ladder onto a product that does not have the traffic for it, so every stage produces no signal and the ramp is just a delay.
- Watching only generic health metrics on a change whose worst failure is a successful request doing the wrong thing. Every dashboard stays green while customers are charged incorrectly.
- Monitoring the blended metric during a 1% stage, where the new cohort cannot move it.
- Advancing by a factor of ten, so the first sign of a saturation problem arrives at full exposure.
- Ramping to 100% because nobody complained, without ever checking the success metric.
- A plan that covers the happy path and says nothing about the deploy window, when the flag is on in one service and off in another.
- Leaving the flag in the code forever, so the next person cannot tell whether it is load-bearing.

## If a rollout is already in trouble

Skip to triage. Get the current percentage, what changed and when, and which metric moved. Recommend the hold or the kill first, then work backward through the steps above to rebuild the plan before the next attempt.
