---
name: childrens-book-illustration-brief
description: Turns a finished or in-progress picture book manuscript into a page-by-page illustration brief covering character appearance, mood, palette, and composition notes, so an illustrator or an image-generation tool can follow it consistently across every spread. Make sure to use this skill when the user has picture book text and needs art direction, illustration notes, or an image-generation prompt set for each page, or asks to turn a manuscript into "storyboards" or a "shot list."
---

# Children's Book Illustration Brief

Converts manuscript text into a spread-by-spread visual brief. The job is governed consistency, and what that means depends on the book. In most stories it means the same character looks, dresses, and reads the same way on page 2 and page 28. In a book whose subject changes over time, such as a tree across two centuries or a building across a war, it means the opposite: the subject must change, lawfully and legibly, while a named set of landmarks holds steady so the reader knows it is still the same thing. Either way each spread also has to compose as a real two-page illustration rather than just describing what happens.

## Step 0: Decide which brief this is, before writing any of it

Ask who is drawing this, because it changes the deliverable rather than just its wording. A brief for a human illustrator is art direction plus commercial terms. A brief for an image-generation tool is a set of locked prompt strings, and it needs the precision in Step 5 instead. Say which you are producing.

## Step 1: Gather inputs

Required:

- The manuscript, broken out page-by-page or spread-by-spread. If it isn't broken into spreads yet, do that first, or use picture-book-writer's output format as the source.

Worth asking for if it's missing:

- A character bible (see character-bible-builder) for every recurring character, or, in a book with no character, a bible for whatever the recurring subject is. If there isn't one, offer to build a lightweight version first. Improvising physical details page by page is exactly how consistency breaks. For a brief specifically, weight the bible toward whatever survives being drawn small, from behind, or in shadow: hair shape, ear shape, body proportion, one distinctive garment. Those are what keep a character recognisable across forty drawings at different sizes, and they matter more than colour, which the reader will not be comparing page to page.
- A stated visual style or reference, like "gouache, warm palette" or "flat vector, bold outlines." If the user has no preference, propose two or three directions that fit the story's tone and let them pick.

### When the subject is not a character

Some books have no character to lock: one tree across two hundred years, one street, one river. The anchor problem is harder here rather than absent, because the subject is supposed to change, and a brief that treats change as drift will fight the book.

Build the bible in two halves.

First, the landmarks that must not change, which are what tell a reader this is the same thing and not a new one. For a tree that might be a fork in the trunk at a set height, a lean away from the prevailing wind, and a healed scar on one flank. Add the things around the subject that barely move at all, such as a boulder, a bend in a stream, or a ridge on the horizon: the setting usually carries more of the continuity than the subject does, and briefs routinely forget it. Fix the compass once, since the light direction follows from it for the whole book.

Second, a stage sheet giving the subject's state at each point the book visits, so the illustrator is not interpolating. Give the values as a starting point to be checked by whoever is signing off accuracy, not as fact.

Some anchors do not exist yet at the start. An acorn has no trunk fork and a foundation has no roofline, so early spreads have nothing on the subject to hold onto. Note the spread at which each landmark is born, lock it from that point, and let the setting carry the continuity alone until then. This is why the surroundings matter so much in the opening spreads: for a while they are the only proof it is the same place.

Also name a recurring scale reference the reader can measure against on every spread, since the subject's own size is what's changing. A wall, a boulder, or a repeating animal works better than a person when the timespan outlives one.

Nominate four or five spreads that repeat the identical camera position, height, and framing, spaced across the book, and leave everything between them free. Change the reader can see by comparing two pictures is worth more than change described in the text, and this is the strongest comprehension device available for a subject that transforms slowly. It has to be decided before the first thumbnail, because it constrains the composition of every spread in the set.

### When there is no manuscript yet

Common, and not a reason to reply with a questionnaire. The style anchor and the character bible do not depend on the text, so build those now and hold the spread briefs. That is most of the value and all of the drift protection, and it lets the user test the look before a single page is briefed.

### Style directions, written so they can be chosen between

A style direction is not a mood word. Give each one the medium and finish, what it is good at, and what it will struggle with in this particular book, then recommend one. The last part is what makes it a choice rather than a menu: a story whose climax is a change in the light will fight a flat vector style, and saying so is worth more than three tasteful descriptions.

Don't name a living illustrator or a specific in-copyright property as the style reference. It's an unreliable instruction for a generator and an unnecessary rights problem on a book someone means to publish. Describe the qualities instead.

## Step 1b: Check the page arithmetic before briefing anything

Do this early, because it is the most common structural problem in an unagented manuscript and it is expensive to find late.

Picture books print in multiples of 8, most often 32 or 40 pages. Work the arithmetic rather than reaching for a remembered number.

Pages 1 and the final page are always singletons; everything between pairs into spreads. Subtract the front matter, which is usually three or four pages for a half-title, title spread, and copyright, and subtract any back matter, which non-fiction almost always needs and fiction usually doesn't. Halve what's left.

Work it each time rather than quoting a total. A 32-page book with a half-title, a title spread, and a copyright page loses four pages at the front and two singletons at the ends, leaving about 14 story spreads. A 40-page non-fiction book losing the same front matter plus two spreads of back matter lands near 16. Change any of those inputs and the answer moves, which is why the subtraction matters more than the number.

When the count comes up one or two spreads short, running the title type over the first story spread instead of taking a separate title spread usually recovers them. That is normal in non-fiction and worth proposing before asking anyone to cut.

Count the manuscript's spreads against the stated page count and say plainly when they disagree. Ten spreads of text is a 20 to 24 page book, not a 32 page one. When there is room to spare, spend it on the beats that want slowing down rather than padding evenly: split a list across several turns, and add a wordless spread at the emotional low point or as a closing beat. When there are too many spreads, say which ones merge.

This is an editorial change to someone's book, so propose it and get agreement rather than quietly repaginating. Finding the mismatch at layout, after the art is finished, is the failure this check exists to prevent.

## Step 1c: Find the decisions that block multiple spreads

Before briefing page one, read the whole manuscript for the one or two visual questions that govern many spreads at once, and put them at the top of the brief as decisions for the author.

These are rarely stated in the text and stay invisible until someone tries to draw it. They tend to be questions the prose never had to settle: whether a character who has changed is still visible in the same way, where an interior scene actually is, whether a creature has a face, how literal a piece of magic looks. One answer can govern half the book, and a brief that quietly picks one has made the author's biggest visual decision for them.

Answer them provisionally so the brief is usable, state which option you assumed, and mark clearly that the brief is a draft pending those answers. Brief every spread rather than holding them: an author with a waiting illustrator needs something to send, and re-cutting briefs is cheap while re-drawing art is not. Hold work back only when there is no manuscript at all, where the spreads cannot be written in any form.

## Step 1d: If the book is non-fiction

Four things change, and none of them are cosmetic.

**Accuracy needs an owner and a stage.** Give any figures you supply, in a stage sheet or anywhere else, as a starting point for that person to correct rather than as fact: the stage sheet is exactly where a confident invented number will slip through unchallenged. Name who signs off on the facts, and put them on the roughs rather than the finals. A wrong leaf shape at rough stage is a note; at final it is a repaint. Say who sources photo reference, since rights on reference images matter even with an in-house illustrator.

**Period detail needs a stamp per spread.** A book spanning decades needs the date on every brief, or the illustrator will default to generic storybook rural and the costume, tools, vehicles, and buildings will be quietly wrong throughout. That means settling where and when the book is set before briefing anything.

**Elapsed time has to be solved visually.** The hardest comprehension problem for a young reader is not what the subject looks like, it is that this spread is forty years after the last one. Give every brief the time elapsed since the previous spread, and say how the picture carries it: a changed season, a fully different sky, a child from the previous spread now grown.

**Back matter is part of the page count.** A timeline, a glossary, or a how-to spread is what teachers and librarians look at, and it comes out of the same signature, so count it in step 1b rather than discovering it later.

Add these fields to the per-spread template below: the date and the subject's age, the time elapsed since the previous spread, what has changed, what must not have changed, and the accuracy notes with who is sourcing the reference.

## Step 2: Brief format, repeated per spread

```
### Spread [N], pages [X-Y]
**Text on this spread:** [quote or paraphrase the manuscript line(s)]
**Scene:** [where we are, time of day, key setting elements]
**Characters present:** [name, pose/action, expression] for each character in frame
**Composition:** [wide establishing, close-up, character on left facing right, and so on. Vary this across the book instead of letting every spread be the same medium shot.]
**Palette/mood:** [dominant colors, lighting quality, warm or cool, bright or dim]
**Continuity flags:** [anything that has to match a prior spread or the character bible, e.g. "same red boots as spread 3"]
```

## Step 3: Passes across the whole set

Once all the briefs are drafted, review the full set:

- Are the shots varied in framing and character position, or did every spread default to the same setup? Vary them deliberately. A picture book that's all medium shots reads as flat even when each individual brief looks fine.
- Does the visual pacing match the story's emotional pacing? Quiet, tender moments usually want closer framing. Big action or discovery moments usually want a wide spread.
- In a book without an emotional arc, the axis is scale rather than feeling: something in a palm or under a microscope at one end, a whole valley at the other. Alternate deliberately. Eighteen mid-distance views of the same subject is the failure this kind of book is prone to, and every spread will look fine on its own while the set sits inert.
- Is there at least one hero spread, normally the turning-point beat, that gets a bigger and more dramatic treatment than the pages around it?

Palette needs the same treatment as composition. The template gives every spread its own palette, which produces a book of individually reasonable pages with no arc. Write the arc explicitly: where the colour is fullest, where it drains, which spread is the coolest and quietest, and where the warmth returns.

Where the story has a continuity rule that runs across spreads, such as the direction of the light once the sun has moved, state it once as a rule the illustrator can check every page against, rather than repeating it in each brief.

Check the gutter. A face or a key object centred on a two-page spread lands in the fold. Flag the spreads where that is a live risk, particularly any full-bleed or symmetrical composition.

Flag any spread you had to leave generic because information was missing, such as an undescribed setting, instead of inventing specifics the user hasn't confirmed.

## Step 4: The details that aren't art direction

These come in two groups, and conflating them is a real error: someone told their illustrator is in-house or salaried will skip the whole section and lose the gutter margins along with the fee.

**Production specs, which every brief needs regardless of who is drawing:**

- Trim size and orientation
- Page count and how many pieces of art that means
- Bleed and gutter safety margins
- Whether the illustrator supplies flat art or works to a designer's layout, plus format and resolution
- Who places the type, and which spreads need designated clear space left for it
- The schedule through thumbnails, roughs, and finals, and how many revision rounds are included

**Commercial terms, only when the illustrator is being commissioned rather than employed:**

- Rights, credit, and fee
- What happens if the book is cancelled part-way, usually a kill fee at each stage. First-time authors leave this out and it is the term that hurts most when it is needed.

You are not advising on the fee. You are making sure a commissioning brief doesn't go out without one, since a brief with no page count and no fee reads as unserious and good illustrators decline them. For an in-house team, drop the commercial group entirely and keep every production spec.

## Step 5: If the briefs are going into an image-generation tool

Convert each brief into a single dense prompt line, front-loading the fixed character and style anchors so they don't drift between generations:

```
[style anchor], [character name]: [locked appearance from character bible], [pose/action], [setting], [palette/lighting], [composition]
```

The anchors are byte-identical across every prompt in the set. Not paraphrased, not shortened, not "warm Scandi style" on spread 7 where spread 6 had the full string. Reworded anchors are the single most common way an AI-illustrated book falls apart, and the damage is invisible until the pages sit side by side.

Then, before briefing the whole book:

- Have the user generate two test prompts, one wide establishing shot and one close quiet moment, and check that the character survives both. If the anchors don't hold across two images, tighten the appearance string before writing fourteen of them.
- Set the aspect ratio for the real format. A spread is landscape and roughly 2:1, and generating squares for a landscape book means recomposing every page.
- Ask for text-free images so type can be dropped in later, and keep key elements clear of the centre where the gutter falls.
- Expect several attempts per usable image, and say so, so the user budgets for it.

## Common failure modes to avoid

- Briefs that restate the text ("the bear is happy") instead of giving the illustrator something to stage: pose, framing, environment detail.
- Filling in the template completely and correctly while never engaging with what the book is actually about. A formally complete brief can be creatively inert, and the template will not catch it. The light rule, the recurring composition, the thing that has to rhyme between spread 4 and spread 14: none of that comes from filling in fields.
- Briefing spread counts that don't fit the page count, so the mismatch surfaces at layout after the art is paid for.
- Treating a subject that is supposed to change as a consistency problem, and briefing it to look the same throughout.
- Making the author's biggest visual decision for them silently, because answering it was the only way to finish the brief.
