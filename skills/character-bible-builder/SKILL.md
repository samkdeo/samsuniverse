---
name: character-bible-builder
description: Builds and maintains a locked reference sheet for a children's book character or a small cast, covering physical appearance, personality traits, speech patterns, relationships, and the specs that only exist between characters such as relative height, so descriptions stay consistent across every page and, where there is one, every book in a series. Make sure to use this skill when the user is starting a children's book series, reusing a character across multiple stories or drafts, mentions that a character's look or voice has "drifted" between drafts, or asks for a "character bible," "style guide," or "reference sheet" for a story character. Use it equally for a SINGLE book with no series behind it, for a cast of two or three characters in one story, and when an illustrator has asked what a character looks like and the author keeps changing their mind.
---

# Character Bible Builder

Produces and maintains a locked reference for a character or a small cast, so every future draft, illustration brief, or spin-off story pulls from the same source instead of re-inventing details. The failure it prevents: a character with "curly red hair" in book 1 and "straight brown hair" in book 3, because nobody ever wrote it down.

## Step 1: Decide which of three jobs this is

**Planning a series that isn't written yet.** The bible is a forcing function, not a record: answering a few questions now forecloses contradictions later. Build the full structure from Step 2, then name the handful of fields that actually constrain the other books and tell the user to answer only those before drafting book one. A flat list of twenty TBDs is a to-do list, not a plan. The usual shortlist is the signature accessory, the flaw, whether the character ages across the series, and the rules of any premise mechanic. Warn against over-specifying the later books: details invented for book six before books two through five exist are the ones the author resents later.

**Locking a character for one book, usually with an illustrator waiting.** This is a different job from the series cases and most of this file's machinery does not apply. See Step 1a.

**Reconciling a character who has drifted.** Send the user to the source material rather than collecting what they remember, since their recollection is the weakest evidence available. Reconcile with them rather than quietly picking one, then log the change in the changelog. See Step 1b, which is the most common real case and the one people get wrong.

## Step 1a: One book, and often a whole cast

The goal here is not completeness, it's getting a few decisions off the author's desk permanently. An illustrator drawing a 32-page picture book does not need the character fully specified. She needs the handful of features that must be identical on every spread, and she will make better choices than the author on everything else.

**Lock the read, hand over the rest.** Four fields do nearly all the work: hair, one signature garment or accessory worn on every spread, one small distinguishing mark, and a two or three colour palette. Mark those as decisions the author must make. Then mark everything else as the illustrator's call, explicitly and in writing. An author who is told which fields are theirs stops agonising over the ones that aren't.

**Weight the sheets by how often each character is drawn.** A protagonist on almost every spread, a co-lead, and an animal do not get equal treatment. Something like sixty, thirty, and ten is closer than three matching documents.

**Capture what only exists between characters.** A cast bible needs the fields no single-character sheet has, and these are the specs that drift first because nobody wrote them down: relative height, stated as a ratio rather than in centimetres, such as the child coming up to the grandfather's hip; relative size for any animal; and who is physically capable of what, since a man in his sixties and a man in his eighties kneel, lift, and move differently and the illustrator has to decide that on page one.

**Do not say the bible will grow as they draft.** That is right for an author at the start of a series and wrong for one with an illustrator on the clock. Here it needs to be usable this afternoon.

## Step 1a2: When the author keeps changing their mind

This is not the same problem as contradicting themselves, and the reconciliation machinery in Step 1b does not work on it. There is no earlier version to rank, no published art to check, no evidence to weigh. There is just someone who has not committed.

- Cut what has to be decided down to the four locked fields above. Most authorial mind-changing is about details that were never load-bearing.
- Date each decision and treat it as closed. Anything changed afterwards goes in the changelog with a reason. That is not bureaucracy: it's how you tell, when a rough comes back looking wrong, whether the author changed it or the illustrator did.
- Over-specifying is the failure mode here, not under-specifying. Every extra field is another thing to reopen.
- When they genuinely cannot choose the signature item or the hair, that usually means the character is not settled in the text yet rather than that they need more options. Ask what actually happens in the story, and say which appearance choices the story is already making for them.

## Step 1b: Retrofitting a bible onto a series already in progress

Most requests arrive here: some of it is published, some is half-drafted, and the author can't remember which version is right. Two things do most of the work.

**Rank the sources of truth.** Published illustrations beat published text, which beats the author's memory, which beats the current draft. If book one is printed and the art shows a brown hat, brown is canon no matter what the author intended or what the text says. Say this out loud, because authors reach for their memory first and it's the weakest source in the stack. Often the answer isn't a decision at all, it's ten minutes with the finished file, and telling them that is more useful than any ruling you could make.

Where the published art and the published text contradict each other, ask which one the bible should follow, and log the loser as a known error so a future reprint can fix it.

**Present a real choice, not an open question.** "Which did you mean?" strands a user who doesn't know. Lay out the options: this version is canon and the other gets swept from the draft, or the other is canon and the first was a one-off, or both are canon under a rule you can state in one sentence, such as one catchphrase for finding a suspect and another for finding a clue. The third option is the only one that keeps both, and it only works if the rule goes in the bible and gets followed. If the user can't state the rule in a sentence, it's one of the first two.

**Mark the document's status.** A bible with open conflicts is `v0.1, DRAFT, N conflicts unresolved`, and it says at the top that it isn't ready to send to an illustrator. A half-locked bible is worse than none, because it gets treated as authoritative and the conflicts get drawn in. Only a bible with no open conflicts is `v1.0, locked`.

## Step 2: Capture the fields

Don't demand all of this up front if the user just wants to start writing. Capture what they know now, mark the rest `TBD`, and let the bible grow. Do create the full structure with every field present, even the empty ones, so nothing gets forgotten later.

Weight the sections to the format. For a picture book, appearance carries the most detail, since an illustrator draws this character forty times. For a chapter book, voice and vocabulary carry it, because the reader meets the character almost entirely through how they talk. Don't hand a chapter-book author twice as much appearance detail as voice detail. A series that spans both, which is common as an illustrated series grows up with its readers, needs both at full weight rather than a compromise between them.

Identity:

- Full name and any nicknames used in-story
- Species or type (human, animal, object come to life) and age or age equivalent
- Whether the character ages across the series. For a multi-book plan this is the largest single structural decision available: a fixed age lets the books be read in any order, and one year per book gives you growth but a hard ceiling on how many books you have. Decide it before book one.
- Role in the story: protagonist, sidekick, recurring antagonist

Physical appearance, specific enough that an illustrator or image-gen tool never has to guess:

- Body and build, height relative to other characters
- Hair, fur, or feathers: color, texture, style, and whether it ever changes, such as going messy after adventures
- Signature clothing or an accessory that appears in every book. A hat, a scarf color, or a backpack is often the single strongest consistency anchor.
- Distinguishing marks: freckles, a chipped tooth, a patch over one eye
- The color palette associated with the character, which is useful for illustration consistency

Personality and voice:

- Three core traits. Avoid generic ones like "brave" on its own, and pair each with a specific flavor: "brave, but only once someone else goes first."
- A flaw or fear that creates story tension across books
- Speech pattern: vocabulary level, any verbal tic or catchphrase, how they talk when scared, excited, or sad
- What makes them laugh and what makes them cry

Relationships:

- Key relationships (family, best friend, rival) with one line on each dynamic
- How other characters address them, including nickname usage

Premise mechanic, when the character has one:

Any ability, condition, curse, talent, or piece of magic that the series runs on needs its own section, because it is the highest-risk drift surface in the whole book. Authors invent around it under deadline in book four and contradict book one without noticing. Capture:

- What it actually does, precisely enough to rule out a case
- Where its boundary sits. If she hears what machines think, is a clock a machine? A bicycle? A pencil sharpener? A reader will test the line, so draw it.
- Range and conditions: does it need touch, proximity, quiet
- The cost or limit. A power with no cost stops generating stories by book three.
- Who else knows, which changes every scene they appear in
- The origin, including the deliberate choice never to explain it. Write down which, so book five doesn't accidentally explain what book one left alone.

Continuity notes:

- Anything established in-story that constrains future books, such as an allergy, a lost object, or a promise made. This is the list future drafts must not contradict.

## Step 3: Output format

Deliver a clean markdown reference document headed with the character's name and organized under the categories above. It gets pasted at the top of future drafting sessions, or attached alongside picture-book-writer and childrens-book-illustration-brief requests, so keep it scannable: short bullet points rather than prose paragraphs.

## Step 4: Maintain it over time

When the user brings a new draft or asks you to check consistency:

- Cross-check every character description and behavior in the new material against the bible
- Name the contradictions precisely ("the bible says green backpack, this draft says blue") instead of quietly updating one side
- Update the bible only after the user confirms which version is correct
- Keep a short changelog at the bottom of the bible with the date or version, what changed, and why: "v2, hair color corrected from brown to red per illustrator's final art"

## Common failure modes to avoid

- Vague traits that don't constrain future writing. "Kind" and "curious" with no specificity are useless; push for the detail that would change how a scene gets written.
- Filling in plausible details because the user gave you almost nothing. This is the one that does real damage: an invented backstory for a character who already exists in print contradicts the published book silently, and the author may not catch it. Every field the user did not supply is `TBD`, including the ones you could guess convincingly.
- Naming a colour and calling the field done. "A red hat" is not a spec an illustrator can draw, because a deerstalker, a fedora, and a flat cap are three different characters. The same goes for "a scruffy dog".
- Specifying every character to the same depth regardless of how often each is drawn, and handing an author three equal sheets of TBDs with no indication of which ones block the illustrator.
- Recording heights and sizes absolutely rather than against each other. What recurs in every shared spread is the ratio, and it's the first thing to drift.
- Treating two props as interchangeable when they stage differently. A magnifying glass is held, so it occupies a paw and can be dropped or lost; a monocle is worn, so it's always there and frees both hands. Choosing between them changes every scene, and it needs settling before anything gets drawn.
- Overwriting old details with no changelog entry, which makes it impossible to tell later whether a change was intentional or a mistake.
