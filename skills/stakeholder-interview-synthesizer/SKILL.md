---
name: stakeholder-interview-synthesizer
description: Turns rough notes from a handful of stakeholder or discovery interviews into decision-ready themes, showing where people agree, where they quietly disagree, and what the disagreement blocks. Use this skill whenever someone has messy notes, transcripts, or recollections from conversations with colleagues, executives, customers, partners, or internal teams and wants to know what to do about them. Trigger it on phrases like "I talked to eight people and now what", "synthesize my interview notes", "what are the themes here", "I need to present findings to leadership", or "everyone told me something different". Also use it when someone is about to write a requirements doc, a project brief, or a kickoff deck off the back of a round of conversations.
---

# Stakeholder Interview Synthesizer

Reads a set of interview notes and returns themes tied to decisions: what the group agrees on, where it splits, what each split blocks, and what to do next. This is the fast version, sized for 4 to 15 conversations and a synthesis you need this week. It is not formal qualitative research. It does not code transcripts line by line, produce an affinity map of every utterance, or claim statistical weight. If the user needs defensible research rigor for a study with dozens of participants, say so and treat this output as a first pass rather than the finished analysis.

## Step 0: Check whether the notes can carry the weight

Do this before anything else, because it changes every step that follows. Read the notes and judge whether they contain enough to support the deliverable the user named.

Notes are thin when they are one line per person, written from memory, missing roles, or missing any description of what people currently do.

A different shape needs naming at the top too: notes that are rich but single-source, meaning one person per function, each speaking first-hand about their own area. This is the normal shape for an internal-tool round. The notes are not thin, but nothing in them corroborates anything else, so say at the top that counts carry no weight here and that the weighting comes from ownership instead, as described in step 5. Thin notes still produce a useful synthesis, but a smaller one: fewer themes, weak evidence labels throughout, no manufactured disagreements, and a longer list of next conversations. Say so at the top of the output rather than filling the structure below to its full size. The structure in the later steps assumes a real corpus, and following it at full width on four one-line notes is how a synthesis ends up asserting things nobody said.

When the notes are thin and the user named a requirements doc or a PRD, say plainly which parts of that document these notes can support, which is usually the problem definition and the open questions, and which they cannot, which is usually the requirements themselves.

## Step 1: Establish what the synthesis is for

Work out what decision or document this feeds, because it changes what counts as a theme. When the user has already said, do not ask again; state the assumption in one line and get on with it. Someone with a readout on Thursday does not need a question round. Common answers:

- A build-or-not decision, or a scope cut
- A roadmap or prioritization exercise
- A requirements or PRD draft
- A readout to leadership, where the goal is alignment rather than a decision
- A problem definition, where the user genuinely does not know what they're solving yet

If the user doesn't know, ask what happens the week after they hand this in. That usually surfaces it.

Also get the roster: who was interviewed, their role, and their relationship to the work. A theme that four engineers raise and no customer raises means something different from the reverse, and you cannot see that without knowing who said what. The roster usually arrives with the notes, so only ask when it is genuinely absent, and when it is absent, deliver the synthesis anyway with the gap named at the top.

## Step 2: Read for five things, not for topics

Topic clustering is what makes synthesis useless. "Six people mentioned onboarding" is not a finding. Read each set of notes and pull out:

1. Stated needs. What someone asked for directly. Treat these as data about the person, not as requirements.
2. Underlying problems. The situation that caused the ask. Someone requesting a bulk export usually has a reporting problem, not an export problem.
3. Constraints. Budget, headcount, a compliance rule, a system nobody will touch, a deadline tied to something external.
4. Contradictions. Two people who cannot both be satisfied. These are the most valuable thing in the notes and the thing most syntheses smooth over.
5. Emotional signal, in both directions. Where someone got animated, frustrated, evasive, or repeated themselves. Also where someone described a real cost and did not complain about it. An unadvocated cost, such as the person who mentions in passing that they spend six hours a month cleaning up after a broken process, is one of the most reliable findings in a round, precisely because nobody is arguing for it. Silence from the person paying a cost is not evidence that the cost is acceptable. Note it as a signal about priority, and label it as your read rather than as fact. Distinguish what the interviewer observed at the time from what they recalled afterward. "Asked about pricing a lot", written up days later, is a memory of an impression and carries less weight than a noted reaction.

Keep a note of who said each item. You need it in step 4.

## Step 3: Separate what you heard from what you concluded

Every theme you write has two parts, and they stay visually separate:

- Evidence: what people actually said, close to their words, with attribution by role
- Reading: what you think it means

Never merge them into one confident sentence. "Ops is drowning in manual reconciliation" is a reading. "Three of four ops staff described spending over an hour a day reconciling exports by hand" is evidence. When you only have a reading and no evidence, say the evidence is thin and name what would confirm it.

## Step 4: Put the constraints somewhere before the table

Constraints are not themes and they do not belong in the theme table. A contract renewal date, a frozen budget, a system nobody will touch, or a migration that takes a quarter are boundaries on the solution space, and they usually decide more than the themes do. List them in a short block above the table, each with its source and what it rules out.

## Step 5: Build the theme table

Output the core of the synthesis as a table, one row per theme:

| Theme | Who raised it | Evidence strength | What it blocks | Decision needed |
|---|---|---|---|---|

Rules for the columns:

- Who raised it: roles and counts, such as "3 of 4 ops, 1 of 2 finance". Note who did not raise it when that is interesting.
- Evidence strength: strong when several people described it unprompted with specifics, moderate when it came up on prompting or lacks detail, weak when one person raised it or you inferred it. Be willing to write weak.
- Adjust that calibration for the roster you actually have. With one person per function, almost everything is single-source by construction, and "1 of 7" stops being informative. What matters instead is whether the single source owns the thing they described. A renewal date from the person who holds the contract is near-certain; a three-week cycle time reported secondhand by someone outside the process is not, and both are single-source. Say which kind you have.
- When every row comes out weak, the column has stopped ranking anything. Order by what it blocks instead, and say in one line why the whole set is weak.
- What it blocks: the concrete thing that stays stuck if nobody resolves this. A theme that blocks nothing is background, not a theme, and belongs in a short "also mentioned" list instead.
- Decision needed: phrased as a question someone can answer in a meeting, with a named owner where you can.

Order rows by what blocks the most, not by how many people mentioned them. Frequency and importance come apart constantly, especially when the person with the most context was interviewed once and the loudest opinion came from someone adjacent to the work.

## Step 6: Write the disagreements up as their own section

Give contradictions a heading of their own rather than burying them. For each one:

- The two positions, stated fairly enough that both people would recognize themselves
- What each position is optimizing for, since most stakeholder disagreements are two reasonable goals in conflict, not one person being wrong
- Whether it needs to be resolved before work starts, or can be deferred
- Who can actually settle it

This is the section that earns the synthesis its keep. A readout where everyone agrees is usually a readout where the interviewer avoided the hard questions.

The exception, and it is a real one: with few interviews and thin notes there may be no established disagreement to report. "No genuine contradiction surfaced, and here is why the notes could not show one" is a valid finding. Write that instead of promoting a difference in emphasis into a conflict with two named camps. An unestablished tension can be noted as such, clearly labeled, as long as it is not dressed up as a finding.

## Step 7: Close with gaps and next conversations

Two short lists:

- What you still don't know, and which of those gaps would change a decision if filled
- Who to talk to next, and the specific question to ask them

Keep this honest and short. If the round of interviews missed the people who will do the work or pay for it, say that plainly.

## Step 8: Recommend, when a recommendation was asked for

A synthesis for a leadership readout usually gets the follow-up question "so what do we do", and the honest answer is often already visible in the themes. When the user asked for a recommendation, or is presenting to someone who will demand one, write it as a short numbered list after the disagreements.

Rules for it:

- Every recommendation stays inside the constraints from step 4. A recommendation that ignores the renewal date or the frozen budget wastes the reader's time.
- Separate what you are recommending they decide from what you are recommending they do. A readout is more useful when it names the two decisions only the person in the room can make.
- Where the evidence is weak, recommend finding out rather than acting. "Instrument this for two weeks before we spend anything" is a real recommendation.
- Do not recommend building the thing a stakeholder asked for, unless the underlying problem supports it.

When the user only asked for themes, stop at step 7. An unrequested recommendation section on someone else's project reads as overreach.

## Output sizing

For a leadership readout, keep it to three to five themes plus the disagreements, gaps, and any recommendation. That runs a page or two, and it is worth cutting the fourth and fifth themes to hold it there. For a requirements draft, go longer and keep more evidence quotes, since the detail gets used. Do not produce fifteen themes. If you have fifteen, you have topics, so go back to step 2 and find the problems underneath them.

## Common failure modes to avoid

- Clustering by topic and calling it synthesis. Themes are about problems and decisions, not subject headings.
- Averaging away a conflict into a bland statement everyone nods at. "Stakeholders want a balance of speed and quality" tells the reader nothing and hides the real fight.
- Treating a request as a requirement. Stakeholders describe solutions, and the job is to find the problem underneath.
- Weighting by volume of speech. The most talkative person is not the best-informed one, and one quiet sentence from the person who owns the system may outrank twenty minutes from someone else.
- Presenting an inference with the confidence of a quote.
- Inventing a quote or a number to make a theme land. If nobody said it, it does not go in quotation marks.
- Anonymizing so heavily that role and context vanish. "A stakeholder noted" strips out the thing that made the note useful. If the user needs anonymity, use roles rather than names.
- A recommendations section that ignores the constraints listed in step 4.

## If more notes arrive later

Update the existing themes rather than starting over. New interviews usually change the evidence strength column and the roster counts, and occasionally split one theme into two. Say what moved and what stayed, since the reader has already seen the first version and needs to know which of their conclusions just changed.
