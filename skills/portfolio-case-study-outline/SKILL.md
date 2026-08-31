---
name: portfolio-case-study-outline
description: Builds a portfolio case study outline for a design, product, engineering, or research project, covering the problem, the constraints, what you actually did, the tradeoffs you made, and the outcome, with a section-by-section plan and a plan for the visuals. Use this skill whenever someone wants to write up a project for a portfolio, a personal site, Behance or Dribbble, a job application, a promotion packet, or an interview presentation, and also when they say things like "how do I write this project up", "I need to show this work", "help me structure my case study", or "I have a bunch of screenshots and no idea what to say about them". Use it too when a draft case study already exists and reads like a feature list or a process diary.
---

# Portfolio Case Study Outline

Produces the skeleton of one case study: the sections, what goes in each, roughly how long each runs, and which image or artifact sits beside it. It stops at the outline and the captions. It does not write the finished prose, and it is not a resume or a cover letter. If the user wants their whole portfolio site structured, or a set of projects prioritized, handle that as a separate conversation before picking one project to outline here.

## Step 1: Find out who reads this and what they decide

When the user already has a draft, go to the last section of this file first, then come back. The diagnosis is deliverable immediately and should not wait behind the intake.

Steps 1 and 2 are an intake pass. Steps 3 through 6 come after the user answers. Don't try to run the whole thing in one turn on thin input, since that produces a hollow outline that has to be thrown away.

The reader changes the outline more than the project does. Work out which of these applies. When the user has already implied the answer, say what you inferred and ask them to confirm rather than making them answer a question they've effectively answered. When there's no signal at all, ask.

- A hiring manager skimming twenty portfolios in an afternoon. They read the first screen and the images. Everything has to survive a 40-second scan.
- An interview panel you will present to live. The outline becomes a talk track, so it needs beats you can speak to and places to pause for questions.
- A promotion or performance packet. Scope, ownership, and measurable result carry the weight. Craft matters less.
- A public write-up for peers. Craft and reasoning carry the weight. Business metrics matter less.

These are not exclusive. Someone job hunting usually needs both the skim version on their site and the talk track for the panel, built from the same material. When that's the case, outline the skim version and mark which beats expand for the live version, rather than producing two separate outlines.

When someone is writing to move up a level rather than sideways, the piece has one job: show judgment under constraint. Knowing the process is assumed at every level above junior, so a write-up that demonstrates method and hides decisions reads as someone executing a process another person defined. That is why the constraints and decisions sections carry the weight, and why a reflection about what the user learned costs them more than it gives.

Also ask what the user is trying to be hired or promoted as, since that decides which parts of the project get the space. The same project written for an IC design role and for a design lead role has a different center of gravity: one shows the craft, the other shows the calls made and who was aligned.

## Step 2: Pull the raw material out of the user

Most people have more material than they think and can't see it. Ask for these directly, and accept "I don't have that" rather than pushing:

- What was broken or wanted before the project existed, in the words of whoever complained about it
- The constraint that actually shaped the work, such as a deadline, a legacy system, a team of two, a legal review, or a stakeholder who kept changing their mind
- Two or three decisions where a different choice was genuinely on the table
- Anything measured, before and after. Numbers, support ticket volume, launch dates, adoption, anything.
- What shipped versus what was designed
- What the user would do differently
- What they are allowed to show. Internal tools, enterprise work, and anything under NDA often cannot use real screens. Ask early, because the answer decides the entire visual plan and it is expensive to discover after the outline is written. The usual options are redacted screens, a sanitized rebuild, or diagram-led visuals. Numbers are covered by the same question and are often the part an employer actually objects to, so check whether a result can be stated as a percentage change rather than an absolute.

The decisions and the "what would you do differently" items are the ones people skip and the ones that make a case study worth reading. Push for those twice before giving up. When the list of questions is long enough to stall someone who already said they don't know where to start, mark the two or three that matter most and let the rest be optional.

If the user has almost nothing beyond screenshots, say so plainly and outline a shorter, image-led piece instead of stretching thin material across a long structure.

## Step 3: Choose the shape

Pick one and name the reason. Do not default to the same shape for every project.

- Problem to outcome. The standard. Works when there was a clear problem and a measurable result. Most common and least memorable, so it needs strong specifics.
- One hard decision. The whole case study hangs on a single tradeoff, with the rest compressed to context. Best when the project was long and messy but contained one genuinely interesting call. Strong for interviews.
- Before and after. Built around a visual comparison. Best for redesigns and for cases where the old version was visibly bad.
- Constraint-led. Opens with the constraint, such as two weeks or no engineering time, and treats the work as the response. Good when the outcome was modest but the reasoning was sharp.
- Process-led. Research through synthesis through concepts through ship. Only use this when the reader is specifically hiring for research or process rigor. It bores everyone else.

Say which shape you picked and why it fits this project. If two could work, describe the split and let the user choose.

## Step 4: Lay out the sections

Produce the outline as sections, each with a one-line purpose, the beats to hit, an approximate word count, and the visual that goes next to it. Use this format:

```
### 1. Opening
Purpose: what the reader knows after 40 seconds
Beats:
- ...
- ...
Length: ~80 words
Visual: hero image, the final screen or artifact
Caption: [one line the image needs to say]
```

Default section set, adjusted to the shape you picked:

1. Opening. What the project was, your role, the timeframe, and the result, all in the first screen. Do not save the outcome for the end. A reader who bounces should still leave knowing what happened.
2. Context and problem. Enough to make the difficulty legible. Name who had the problem and how it showed up.
3. Constraints. The real ones. This is what makes the work look hard rather than easy.
4. The work. Two or three passes, not every artifact you produced. Each pass shows one thing: an exploration that failed, a mechanism you designed, a system you built.
5. The decisions. Two or three, each written as: the options, what you chose, why, and what it cost. A decision with no cost isn't a decision.
6. What shipped. Concrete. Screens, code, a launched flow, a document people use.
7. Outcome. Numbers when they exist. When they don't, say so and use whatever evidence you do have, such as adoption, a quote from a user, or a decision the work unlocked.
8. Reflection. Short. One or two things you'd change, stated without self-flagellation.

Sizing guide, for a skim-first reader: the whole piece runs 600 to 900 words with 6 to 10 images. For an interview talk track, aim for 8 to 12 beats you can cover in ten minutes. For a promotion packet, 400 words is often plenty, and scope and result take two-thirds of it.

## Step 5: Plan the images before the prose is written

For each visual, note what it has to prove, not just what it shows. A screenshot that only shows a screen is filler. A screenshot that shows the state the user was stuck in earns its place.

Flag the gaps here: if a section has no visual and needs one, say what the user should go find or rebuild. This is the moment to catch that the interesting mid-process artifact was never screenshotted, while there is still time to remake it.

## Step 6: Write the opening paragraph and every caption

Draft only these two things, since they carry the most weight per word and set the voice for the rest. Hand the section prose back to the user with the outline. If they ask you to write the full draft afterward, do it against the approved outline rather than restructuring as you write.

## Common failure modes to avoid

- A process diary. "First I did discovery, then I did wireframes, then I did high fidelity." Nobody reads it. The reader wants the problem, the hard part, and the result.
- Burying the outcome at the bottom. Skimmers never reach it.
- Claiming the whole project. If four people worked on it, say what you owned. Vague "we" throughout reads as hiding something, and interviewers ask about it.
- Decisions with no cost. "We chose the simpler flow because it was better for users" is not a decision. What did you give up?
- Inventing metrics. If nothing was measured, write that nothing was measured. A fabricated 40% is the fastest way to fail a follow-up question in an interview.
- Twenty screens of the final design and nothing else. Volume of polish does not substitute for reasoning.
- The same structure across every project in the portfolio. Three case studies with identical headings read as a template, and the reader stops after the first.

## If the user already has a draft

Deliver the diagnosis now and gate only the outline. The cut list needs no information the draft doesn't already contain, so produce it in the same turn, then ask for the missing material before building the section plan. Handing back only a list of questions to someone who just gave you a draft is a bad trade.

Don't rewrite it. Map the existing draft onto the section set above, then say which sections are missing, which are overweight, and which paragraphs are process filler that should be cut. Give the cut list before the addition list, since most weak case studies are too long rather than too short.
