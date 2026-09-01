---
name: decision-journal
description: Records a decision while it is still being made, capturing the options, the reasoning, the expected outcome with a confidence number, and the date the decision should be reviewed, then runs that review later and scores the prediction against what actually happened. Use this skill when someone says they are about to make a call, weighing a choice, deciding between offers, about to hire or fire, choosing a vendor or a framework, taking or turning down a job, or when they say "log this decision", "write this down so I remember why", "I want to check later whether I was right", "how do I get better at deciding", "review that decision I made", or "was I right about X". Use it too when someone is second-guessing a past decision and wants to know whether it was actually bad or just unlucky.
---

# Decision Journal

Captures one decision at the moment it is made, in a form that can be scored later, and runs the review when the time comes. The value is not the record. It is the gap between what someone predicted and what happened, which is invisible without a written prediction because memory rewrites the prediction to match the outcome.

Three modes, and picking the wrong one wastes the entire answer:

- **Logging** a decision that has not yet resolved. The user is describing something in the present or recent past tense and the outcome is not known.
- **Reviewing** a decision that was logged, where an entry with a written prediction exists.
- **Reconstructing** a decision that was never logged and has already resolved, usually badly. This is how most people arrive here. It runs a different procedure and produces a weaker result, and both of those facts have to be said out loud rather than quietly papered over. See "Reviewing a decision that was never logged" below.

This is not a decision-making framework. It does not tell anyone which option to pick, and it should not drift into advice: the moment it starts recommending, the record stops being a record of the user's reasoning and becomes a record of yours, which is useless for calibration. If they want help choosing, help them, then log what they chose and why in their words.

## The escape hatch

Most decisions do not deserve an entry. A journal that logs everything gets abandoned in a fortnight, and abandoning it costs more than never starting because the half-finished record teaches nothing.

Log a decision when at least two of these hold:

- It is hard or slow to reverse
- It was genuinely close, meaning the user can argue the other side
- It rests on a belief about the future that could turn out wrong
- The user will be tempted to rewrite the story afterward

If the user brings a small or reversible decision, say a one-line entry is enough and write the one line. Do not run the full procedure on which laptop to buy.

## When you only get one message

The steps below are written as questions, but this skill is most often used in a single message with half the fields missing, and stopping to interview is the wrong response to that. It gets abandoned before the second reply.

So draft the entry from what you were given, and mark every field you could not fill as a named blank rather than a generic prompt. A blank that says what belongs in it, and why that field matters, gets filled. A question at the end of a message does not.

Fill in the user's own words where you have them. Where you have to supply a candidate — a plausible assumption they did not state, a prediction they have not written — label it as a draft for them to accept, change, or delete, and keep it to the mechanics rather than the judgment. Drafting "you assumed the funding round would close" is fine. Drafting "you were right to worry" is not, and it is the same rule as the advice ban: a prediction the model wrote and the user waved through scores the model, not the user.

Say which blanks are load-bearing. Usually two are: the runner-up, and the confidence number.

## Step 1: Get the decision stated as a choice between options

A decision written as "we decided to use Postgres" cannot be scored. A decision written as "Postgres over DynamoDB, having also considered staying on SQLite" can.

Get:

- **The decision**, in one sentence, in the active voice with the decider named
- **The options considered**, including the one nobody wanted to say out loud. Do nothing is an option and belongs on the list whenever it was available.
- **The option that came second**, specifically. This is the single most useful field in the whole entry and the one people skip. A review has nothing to compare against without it, because "was this good" is unanswerable and "was this better than the thing I nearly did instead" is answerable.
- **Who is actually deciding**, which is not always the person talking to you. A large share of the decisions people want logged are joint or made on someone else's behalf: a couple choosing a school, a panel picking a candidate, an adult child keeping the record for a parent's medical choice. Get this right, because everything downstream hangs on it.

  For a **proxy** decision, where the user is the record-keeper and someone else decides, the entry records the decider's reasoning in the decider's words, and the confidence number is theirs. An entry that quietly captures the record-keeper's reasoning instead will score the wrong person at review time, and it will teach the record-keeper that they were right about a call they did not make. Name both roles in the entry.

  For a **joint** decision, record whether the parties actually agreed or one conceded, and record the reasons separately when they differ. Two people who chose the same option for different reasons have made two different bets, and only one of them can be wrong. Get the confidence number from each of them rather than negotiating a single figure, because the spread between two numbers is itself the finding.

  Keep the calibration record per person. Confidence numbers from different people do not pool, and a shared curve tells nobody anything about their own judgement.

- **The date**, and whether the decision is already made or still open. Log it before the outcome is known. An entry written after the fact is a rationalization with a date on it, and it is worth saying so plainly rather than accepting it silently.

## Step 2: Capture the reasoning in the user's words

Ask for the actual reasons and write them down close to how they were said. Resist tidying them into a clean argument. A messy reason like "honestly I just don't trust that vendor's roadmap" is more useful at review time than a polished restatement, because it is falsifiable and the polished version usually isn't.

Separate three things people run together:

- **What was known.** Facts available at the time.
- **What was assumed.** Beliefs treated as facts. Push here, because the assumptions are where decisions actually go wrong and they are rarely volunteered. If the reasoning contains "obviously", "clearly", or "everyone knows", there is an assumption underneath it.
- **What was unknown and accepted.** Things they decided not to find out, and why not. Usually time or cost.

Record the constraints too, including the ones that will be invisible in hindsight: the deadline, the budget, who was unavailable, what the user did not have permission to do. A review that forgets the constraint judges the decision against a menu that never existed.

Note the emotional state if it is relevant and the user offers it. Tired, angry, relieved to have any option at all, wanting the meeting to end. This is not therapy, it is signal: a person who learns that their rushed decisions are systematically worse has learned something a purely analytical journal would have hidden.

## Step 3: Write the prediction

This is what makes the entry scoreable, and it is the part that gets skipped.

Get a specific, falsifiable statement of what the user expects to be true, with a confidence percentage. Not "I think this will go well" but "by March we will have cut deploy time under ten minutes, 70% confident".

Rules for a usable prediction:

- It must be checkable by someone who was not there, using evidence that will exist
- It must have a number or a yes/no in it
- It gets a confidence figure. Push back on 90% and above; people are overconfident and most confident predictions are the ones worth catching. If the user gives 100%, ask what would have to happen for it to be wrong, and if they can name something, the number is not 100.
- Write the failure prediction as well: what would be true if this turns out badly. Someone who can only describe success has not really considered the downside, and at review time this line is what distinguishes a bad decision from bad luck.

Where the decision has several distinct consequences, write several predictions rather than one blurred one. Two or three is usually right. A single prediction that bundles cost, speed, and team happiness cannot be scored, because it will be part right.

**Predict only what you will actually get to observe.** For a large share of decisions the road not taken is never visible: the house you did not bid on, the candidate you did not hire, the treatment you declined. You will see one branch and never the other, so a prediction phrased as a comparison between them — "this will go better than the alternative would have" — can never be scored and will be settled at review time by whichever story feels better.

Point the prediction at something observable instead, and there are usually two good targets. The first is the chosen path's own outcome against a number written now: what counts as this having gone fine, and what counts as it having gone badly. The second, and the more useful one, is the belief that made the runner-up lose. That belief is often checkable even when the counterfactual is not. If a vendor was rejected because their support was judged unreliable, their public status page and their other customers will say something within the year. If a supplier was passed over because they seemed likely to raise prices, that is observable. Score the belief, and the decision is scoreable even though the counterfactual never happens.

Say plainly which of the user's predictions are unobservable, and do not let one through unmarked. An unscoreable prediction is worse than none, because it will be scored anyway, by feel.

## Step 4: Set the review date by when the answer arrives

Do not default to a fixed interval. The review date is governed by when the outcome becomes legible, and that varies enormously: a hiring decision is not readable at three months and is usually clear by nine; a framework choice shows its cost on the second major feature, not on a calendar; a pricing change needs a full renewal cycle; a medical or financial decision may not resolve for years.

So ask directly: what is the soonest date by which the evidence will exist? Set the review a little after that. If the honest answer is two years, set two years and set an interim checkpoint on a leading indicator rather than pretending the real answer arrives sooner.

Where there is a signal that would arrive much earlier than the verdict, name it and give it its own earlier date. A leading indicator that is checked and found already wrong is the whole reason to keep a journal: it converts a review into a chance to change course while changing course is still cheap.

Say plainly how the user will be reminded. A review date that lives only inside a document is not a reminder, and this is the most common way a decision journal fails. Put it in whatever the user actually looks at: a calendar entry, a task, a recurring note. If they are keeping the journal as a file, say that the file will not remind them.

## Step 5: The entry

Keep it short enough to actually write. Long templates are the second most common reason journals die.

```
DECISION: [one sentence]
Date: [date]  |  Review on: [date]  |  Early check: [date, signal]
Decider: [who]

Options: [chosen] / [runner-up] / [others, including do nothing]
Why the runner-up lost: [one or two lines]

Known: [facts]
Assumed: [beliefs treated as facts]
Not investigated: [and why not]
Constraints: [time, money, people, permission]

Prediction: [falsifiable statement] — [confidence]%
If this goes badly, what I'd expect to see: [signal]
```

## Step 6: Running the review

At review time, do this in a strict order, because doing it in any other order contaminates the answer.

1. **Read the prediction before looking at the outcome**, and say so. If the user has already told you the outcome, note that the review is now partly compromised and continue anyway.
2. **Ask what actually happened**, in facts. Resist the summary judgment for now.
3. **Score each prediction**: right, wrong, or unresolved. Unresolved is a legitimate and common result and should not be forced into one of the other two. When it comes back unresolved, the finding is often that the prediction was not checkable, which is a lesson about how the user writes predictions.
4. **Separate the decision from the outcome.** This is the point of the whole exercise. A good decision can produce a bad outcome, and a bad decision can be rescued by luck. Judge the decision on what was knowable at the time, using the "known / assumed / not investigated" fields, and judge the outcome separately. Say which of the four boxes this lands in: good decision and good outcome, good decision and bad outcome (bad luck, change nothing), bad decision and good outcome (the dangerous one, because it teaches the wrong lesson), bad decision and bad outcome.
5. **Check the assumptions individually.** Which held? Which turned out false? An assumption that was false and did not matter is as interesting as one that was true and load-bearing.
6. **Ask what would have had to be different** for the runner-up to have won. If the answer is nothing, the decision was overdetermined and there is less to learn than it seemed. If the answer is a piece of information that an hour's work would have produced, the flaw was never the choice, it was making a large irreversible call on a single impression, and that is a different and much more fixable habit.

Where the runner-up's outcome is unobservable, say so at this point rather than reasoning about it. You are comparing a real result against an estimate that never had to survive contact with reality, and those are not the same kind of number: a quote is what something costs when nothing goes wrong, and a final invoice is what it cost when something did. Score the belief that made the runner-up lose, following the rule on observable predictions in step 3, and leave the counterfactual explicitly unresolved.

Then, calibration. Once there are several reviewed entries, group them by confidence band and check the hit rate: of the things called 70% likely, roughly 70% should have happened. Fewer means overconfidence, which is the usual finding. Do not attempt this on two entries. A calibration curve drawn from a handful of predictions is noise, and reporting it as a finding is worse than not reporting it, because the user will believe it. Say how many entries it will take before the number means anything, which for a rough read is on the order of a dozen or two in the same confidence band.

Look across entries for patterns instead, which show up much sooner than calibration does: decisions made under time pressure, decisions where one person's opinion dominated, decisions where the assumption that broke was about someone else's behavior rather than about the world. Three entries is enough to notice a repeated shape, and the shape is more actionable than the percentage anyway.

## Reviewing a decision that was never logged

Most people arrive at a decision journal for the first time immediately after a bad outcome, holding no record and a strong feeling. Do not refuse this, and do not run the normal review on it either. Reconstruct, and be honest about what reconstruction can and cannot deliver.

Say the limit first, in one or two sentences rather than a lecture. There is no prediction to read, the outcome is already known, and six months of memory has been quietly promoting whichever detail the outcome vindicated. The recalled reason may be the true reason. It is also the exact shape a rationalization takes, and nobody in the conversation can tell the difference from here. That is not a reason to stop; it is the reason the result gets labelled.

Then:

1. **Build the entry backwards**, using the same template, and mark every field `recalled` rather than `recorded`. The distinction matters more than the content. This is the one place where the drafting habit from "when you only get one message" is switched off: do not supply plausible candidate content for a resolved decision, because a field you draft and the user recognises is indistinguishable from one they remember. Leave the blank and name what belongs in it. There is no review date, so write `n/a` rather than inventing one.
2. **Fill the "not investigated" and "constraints" fields first**, before anything else, because those are the two that hindsight erases fastest. What was the deadline? Who was unavailable? What did they choose not to find out, and was that reasonable with the clock they had?
3. **Note the empty failure prediction as the finding.** The absence of a written "this went badly" threshold is usually the actual problem. Without a number agreed in advance, any overrun reads as pure indictment, and there is nothing to point at to say a result was within the range that was accepted going in.
4. **Separate the outcome from the decision anyway**, using step 6's four boxes. This still works without a record, and it is the part the user came for.
5. **Refuse to place the box when the evidence does not support it**, and say which single missing fact would place it. There is almost always one, and it is almost always retrievable: the invoice lines that show whether an overrun was scope the user themselves added, discovered conditions nobody could have priced, or an estimate that was wrong when it was made. Sorting those three apart moves the answer more than any further reasoning will. Sending the user to go find that fact is a better answer than a confident verdict built on what they happen to remember.
6. **Then look for what is still live.** A resolved decision often has an unresolved one attached to it — a renewal, a warranty period, a final payment, a second phase — and that one can be logged properly, now, before its outcome is known. This is the most valuable thing to come out of a reconstruction, so offer it rather than ending on the post-mortem.

Do not score a reconstruction into the calibration record. It contaminates it, and one entry written with the answer already in view will pull a small sample further than any honest entry.

## Step 7: Close the loop

End a review with one sentence naming what changes next time, or say explicitly that nothing changes because the decision was sound and the outcome was luck. That second one is a real result and should be said out loud rather than left as a shrug, since the instinct after a bad outcome is to fix a process that was not broken.

## Common failure modes to avoid

- Sliding into advice. This skill records reasoning; it does not supply it. An entry full of the model's logic teaches the user nothing about their own.
- Predictions that cannot fail. "This will help us move faster" has no date, no number, and no way to be wrong.
- A default 90-day review on everything, so hiring decisions get reviewed before the person has settled in and infrastructure decisions get reviewed before anything has been built on them.
- Logging the decision after the outcome is known and treating it as a genuine entry, rather than a labelled reconstruction.
- Running the normal review on a decision that was never logged, so steps that depend on a written prediction quietly produce a verdict out of nothing.
- Writing a prediction about the branch that was never taken, which cannot be observed and so gets settled at review time by whichever story feels better.
- Interviewing the user through six steps when they sent one message and expected an answer.
- Judging the decision by the outcome. The bad-decision-good-outcome case is the one that quietly teaches people to repeat something reckless.
- Omitting the runner-up, which leaves the review with nothing to compare against.
- Drawing a calibration curve from four data points and presenting it as a finding.
- A review date recorded only in the journal, where nothing will ever surface it.
- Recording the record-keeper's reasoning on a decision somebody else made, so the review scores the wrong person.
- Averaging two people's confidence into one number, which throws away the disagreement that was the most informative thing in the entry.
- A template so long that the second entry never gets written.
