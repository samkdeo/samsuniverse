---
name: naive-brand-identity
description: Builds brand identities in the naive hand-drawn style — wobbly single-weight line illustration, rounded and blobby logotypes, handwriting and script wordmarks, sticker sets, and repeating patterns — and specifies them as a system that survives being drawn twice. Covers the pen rules that keep a set coherent, palettes verified by computed contrast rather than eyeballed, type pairings with the licensing and character-set traps named, seamless pattern construction, colour that survives conversion to print, a check on whether the look actually suits the buyer, and the three separate accessibility regimes this style runs into — labelling rules for products and packaging, signage standards for physical premises, and WCAG for screens. Use whenever someone wants a hand-drawn, doodle, childlike, naive, marker, crayon, sticker, cutesy or illustrated brand, a bold rounded or blobby logotype, brand colours that are "ADA friendly", accessible or WCAG compliant, font pairings or brand guidelines for an illustrated brand, or brand patterns, seamless repeats, packaging illustration or a sticker sheet. Trigger on "hand drawn logo", "doodle branding", "cute packaging", "make my brand look hand made", "accessible brand palette", "font pairing for my logo", and on any request to build or extend a visual identity in this style.
---

# Naive Brand Identity

Builds and specifies a brand identity in the naive hand-drawn style: the line rules that make twenty drawings look like one hand made them, a palette verified as pairs against contrast thresholds, a type system where exactly one voice is loud, and patterns that actually tile. The hard part of this style is not making one charming drawing. It is making the fortieth one match the first, and keeping a look built on low-contrast pastels and near-illegible handwriting from failing the people who need to read the label.

It does not name the brand or write its copy. It does not produce finished illustration: it produces the drawing rules, the generation prompts, or the illustrator brief, depending on who is holding the pen. For repeating a *character* consistently across a long narrative sequence rather than across a brand's surfaces, character-bible-builder goes deeper, and childrens-book-illustration-brief covers the same anchor-drift problem for books.

## Step 0: Answer the question you were actually asked

Most requests here are small, and a small one gets a small answer. Someone asking for a font pairing gets a font pairing. Someone asking whether two hex codes pass gets the ratio and the verdict. Someone asking for a stripe pattern gets the stripe pattern. Go to the last section of this file and answer from there, pulling in only the one check that changes the answer — usually the arithmetic in Step 3 or the type checks in Step 4. Everything else stays out of the reply. Keep the answer close to the size of the question: a one-line question does not need six hundred words back.

Run the full sequence when the request is to build an identity. When a system already exists, scale the extraction in Step 1a to the size of what is being added rather than running it whole: a body of new work earns the full measurement pass, while a single asset needs only the rules that asset touches, read off the existing artwork in a couple of minutes. Nobody adding one pattern needs a font-licence audit.

When the request is broad but the brand is thin, do not answer with a questionnaire. Two things actually change the output — what the brand sells, and where the identity has to live — and any brief detailed enough to trigger a full build has usually answered both already. Ask only if one is genuinely missing. Everything still ambiguous after that gets a stated assumption rather than a question: say what you are building on and what it would change if wrong, then build. Proceeding on a stated assumption beats going back for a third question, and the user will correct an assumption far faster than they will answer an interrogation.

This bars questions that gate the answer, not the shortlist of real inputs you need to finalise it. Building on stand-ins and closing with "send me your actual hex codes, your market, and your converter's minimum line width and I will finalise these three things" is the correct shape. Asking for them first and delivering nothing is not.

### Say once whether the style fits, then build what was asked

This aesthetic carries a message before it says anything: approachable, small-batch, unintimidating, low-stakes, warm. That is an asset in most categories and a liability in a few, and the request never mentions it because the user has already fallen for the look.

Two questions decide whether it is worth a paragraph. Who is buying, and what does the purchase feel like to them? Where a product sits against something people find difficult — a medical or health experience, money trouble, legal exposure, grief, a body they are unhappy with — the same drawings that read as friendly on a snack can read as making light of it, or as talking down to a buyer who is already tired of being talked down to. That risk is highest exactly where a brand reaches for this style hardest, because the style is chosen to make the difficult thing feel lighter.

Say it in a paragraph, name what the look signals and who it might lose, offer the version that keeps the warmth without the childishness — the same hand, drawn at a restrained scale, on an adult palette, with more space and fewer faces — and then build what they asked for. This is a judgement to raise, not a veto, and a user who has heard it and still wants the doodles has made a legitimate decision.

The buyer also changes the numbers, not just the tone. Near vision declines from the mid-forties in more or less everyone, so an older buyer band tightens the legibility budget on an identical design: the reading zones need more size and more contrast margin than the same layout would need for a younger audience, and small printed text is read in a shop, at arm's length, often without glasses. Where the audience skews older, treat the thresholds in Step 3 as a floor to clear comfortably rather than a target to meet.

### Numbers you are not allowed to invent

This file asks for specifics everywhere: line weights, minimum sizes, ratios. Two kinds of number are not yours to supply.

**Production limits belong to a process and a vendor.** Minimum line weight for cut vinyl, screen printing, embroidery, foil and etching all differ, and they differ again between two vendors running the same process. Name the constraint, name who owns the number, and tell the user what to ask for — "ask your printer for their minimum line width and gap on this stock" is a usable instruction. Supply a figure only where you actually have grounds for it. Hedging an invented number does not launder it: a "typical" figure you have no source for is still a number the user will design against, and the hedge will not survive being repeated.

**Regulatory figures belong to a jurisdiction and a category.** Name the regime and tell the user which one applies to them. Do not quote a type size or a dimension as settled law.

Colour is the exception, and the reason the script exists: contrast ratios are computable exactly, so compute them and state them without hedging.

## Step 1: Decide who is holding the pen, before designing anything

This changes the deliverable, not just its wording. Say which one you are producing.

**A human illustrator** needs the rules written as constraints they can hold in their hand plus reference for tone, and they will make better decisions than the spec inside those constraints. Do not over-specify individual drawings.

**An image-generation tool** needs locked prompt strings, and it needs Step 2b. This style is one of the hardest things to get out of a generator: they default to rendered, shaded, gradient-filled "cute mascot" work, and they will not hold a line weight. Budget several attempts per usable asset and say so, and steer the user toward drawing and tracing instead when they have the time, because it is faster than it looks.

**Vector drawn by hand, or SVG written directly**, is realistic for patterns, geometric marks, and simple objects, and unrealistic for expressive figures. Write the patterns as SVG. Do not promise a charming wonky character in path data.

Most brands end up mixed, and in a mixed brief this is the load-bearing decision rather than a preamble to it. Set it out as a table of every asset against its route before designing anything, because the routes have different constraints and an asset quietly assigned to the wrong one is discovered late. Patterns and geometric marks go to vector, figures to drawing or generation — and anything carrying a letter goes to hand-lettering or a real font, never to a generator, for the reason in Step 2b.

## Step 1a: If the system already exists

Only when the brand has artwork already and the job is to extend it, and at the depth the addition justifies — take the two or three rules the new asset actually touches for a single piece, and the full pass below only when a body of work is being added or a new hand is taking over. This is a different problem from building, and the difference is encouraging: the rules were decided, they were simply never written down, and the artwork is the record. Nothing is unrecoverable while the files exist. What the user is missing is not a person, it is a spec, and most of it can be measured back out in an afternoon.

Every decision in Step 2 inverts into a measurement. Take them off six or eight of the strongest existing pieces rather than one, because one piece cannot show you a tolerance:

- **Line weight** — divide each piece's stroke width by its artwork width and see whether the results cluster. A tight cluster is the ratio and its tolerance. A scatter means the weight was fixed in absolute terms regardless of size, which is also a rule; record it that way. Check whether interior detail is thinner than outlines, which would make it a governed second weight.
- **Terminals and joints** — read straight off the stroke settings.
- **Wobble** — measure how far a line that wants to be straight actually deviates, as a percentage of its own length, and how far circles run off-round. Then check the amount is consistent across the set, and write "consistent" down explicitly, because someone coming to the style cold will vary it deliberately to look natural, which is the exact tell of an imitated hand.
- **Fill policy** — whether fills are offset, in which direction, and by how much as a proportion of the shape.
- **Proportions and face policy** — measure the ratios and note what the faces can and cannot express, since the new work will probably need an expression the original set never had to make.
- **The bans** — list what never appears anywhere in the existing work.

Then validate the extraction with a **re-draw test**, which is available only in this case and is stronger than anything a new brand can run: have the new hand redraw two existing pieces from the written spec alone, without tracing, and compare against the originals. Whatever reads as different is a rule you failed to extract, and it is usually the wobble or the fill policy. Follow it with the two-object test in Step 2 to check the spec holds on subjects the original set never covered. Both, in that order, before any of the new work is commissioned.

**Separate a drift from a documented exception.** New work often genuinely needs something the original lacks — a state the faces cannot currently make, or a weight adjustment for a ground the original never used. That is legitimate, and the difference between an extension and a decay is only whether it was written down as a named exception with its scope attached. Record it as one, with the condition it applies under, rather than quietly widening the rule.

**Check what was actually inherited**, because "we have the files" is a leaky claim. Confirm the right to make derivative work, since commissioned illustration is often licensed rather than assigned. Check which fonts are in the files and whether their licences transfer. Check the sources are complete — linked assets, brushes and custom appearances travel badly. None of these is likely to bite, and all are cheap now and expensive after the work is done.

## Step 1b: If it goes on a physical thing, list the surfaces first

Skip on a screens-only brand. Otherwise do it before the pen, because the surfaces decide the size the artwork is read at, and that is what the line weight is derived from.

**Write down every format and what each one does.** Front of pack sells and is where the identity performs; back or base informs and is where a regime governs; and on a small format the two collide on one face, which is the constraint that shapes everything else.

**Each format has geometry that cuts into the design, and it is not negotiable after the fact.** A wrapped label has a seam and a curve, so nothing that has to be read whole may cross the seam, and artwork approaching the curve compresses before it disappears. A sachet has seal zones on its edges and a tear notch, all of which eat live area that looks available in a flat layout. A carton has panels, glue flaps and a dieline, and the flaps are structure rather than design surface. Get the dieline or template from the converter before designing rather than after, because a layout built without one is redrawn, not adjusted.

**Design the smallest format first.** What survives there works on the larger ones; the reverse fails, and it fails late, after the big surface has been approved and everyone is attached to it. The smallest format is also usually where the regime is hardest to satisfy, since the mandatory information does not shrink with the pack.

**Decide the panel hierarchy once** — what appears on every format, what only on the largest — so the small pack is a deliberate reduction rather than whatever happened to fit.

**Treat the finish as a decision.** Matte, gloss, soft-touch and spot varnish each change how the colour reads and how legible small type is, a matte or soft-touch laminate measurably lowers contrast, and it is applied after every choice above was made. Name it early and account for it in Step 3 rather than discovering it on the proof.

## Step 2: Fix the pen before you fix anything else

**Decide and write down: line weight, terminals and joints, wobble amount, fill policy, figure proportions, face policy, the bans. Then run the two-object repeatability test.**

This is the step that separates a system from a pile of nice drawings, and it is the one that gets skipped. Every drawing in the set has to read as made by one hand in one sitting. That is a set of decisions, not a feeling, and it has to be written down before the first mark, because it is unrecoverable afterwards — twenty drawings at drifting line weights cannot be reconciled without redrawing them.

Settle and record each of these:

- **Line weight**, given as a ratio to artwork width so it survives moving between a business card and a van, plus one worked instance so the ratio is unambiguous. Derive the ratio, do not recall one — by measuring the existing artwork if there is any (Step 1a), and otherwise by drawing the mark at the size it will most often appear, picking the weight that looks right there, and dividing. Then state both, and check they agree — a stated ratio and a stated point size that contradict each other is a spec that produces two different brands, and unit conversion is where it happens. Convert before you compare: a point is 1/72 inch, about 0.353mm, so a 2pt line on a 100mm-wide artwork is about 1/140 of the width. Write both forms only after they agree.

  Then check the ratio against the coarsest process the identity has to survive — this is the check that matters on anything printed or made, and the only one to skip outright for a screens-only brand — because a ratio that looks elegant on screen can fall under a physical floor at real sizes. Cut vinyl has to be weeded by hand and tears below a certain width; embroidery cannot hold a thin stitched line; screen printing and foil each have their own floor. Get those numbers from the vendor, not from memory, and if the ratio falls below one of them, either raise it for everything or draw a dedicated heavier version for that process and say which assets use it.

  One weight across the whole set is the default and the strongest choice. If you allow two, define exactly what the second is for, such as interior detail only, never outline — and note that interior detail is thinner than the outline in most drawings, so it hits the production floor first.
- **Terminal and joint**, meaning round or flat line ends and whether corners are rounded. Rounded terminals read warm and childlike. Flat reads more editorial. Mixing them is what makes a set feel bought from three stock libraries.
- **Wobble, and how much.** This is the defining variable of the style and the one described vaguely. Say it as deviation rather than as a feeling. Around two per cent of a line's own length is a reasonable place to start; draw it, look at it at real size, and tune from there, because the right amount depends on the line weight and the scale the artwork is read at. Curves may be slightly asymmetric, circles may be off-round, and nothing closes perfectly. Then say the thing that matters more: the wobble is *consistent in amount* across the set. Random amounts of wobble is not what a real hand does. A hand is consistently imprecise.
- **Fill policy.** Outline only, solid fill, or outline plus a single offset fill that deliberately misses its edges. Pick one. The offset fill is a strong, cheap way to signal "printed by hand" and it needs its own rule for how far it may miss, or it turns into a mistake.
- **Proportion rules for figures**, where there are figures — a botanical or object-based identity skips this rather than inventing a rule it will never apply. Naive figures are not badly drawn realistic figures. They are consistently distorted, and the distortion is the signature: heads large relative to bodies, hands and feet simplified to mittens or hooks, limbs of even thickness with no taper, no visible joints. Write the ratios you are using.
- **Face policy.** Two dots and a line is a different brand from a face with a nose, a blush and eyebrows. This decides how much the character can emote later, so decide it against what the brand needs the character to do. Dots cannot look worried.
- **What is banned.** Perspective, cast shadows, gradients, rendered volume, texture beyond a single flat grain, and outlines of varying weight within one drawing. Naming the bans is more useful than describing the goal, because these are exactly what an illustrator or a generator reverts to under pressure.

Then write the **repeatability test**, and make the user run it before commissioning or generating the full set: draw two objects of very different kinds under the rules, one organic and one hard-edged, such as a leaf and a pair of scissors. If they do not look related, the rules are underspecified and the missing rule is usually the wobble or the fill policy. Finding that after forty assets is expensive; finding it after two is free.

## Step 2b: If a generator is drawing it

Only when Step 1 chose that route. The pen rules above are now a prompt fragment, and the fragment has to be **byte-identical in every prompt in the set**. Not paraphrased, not shortened, not "same style as before". A reworded anchor is the single most common way a generated set falls apart, and the damage is invisible until the assets sit side by side.

**No letter in the identity comes out of a generator.** Generators cannot spell reliably, and they are far worse on anything beyond unaccented Latin — diacritics land on the wrong character, get swapped for a similar-looking mark, or vanish. A brand name is the one string that must be right on every surface, and a misspelling is not a design defect that gets nudged in review, it is a reprint of everything already produced. So the generator draws objects only; every letter is hand-lettered or set in a real font, and `no text, no letters, no words` goes in every prompt even for a plain object, because generators garnish scenes with invented signage.

This inverts the economics of hand-lettering for any brand whose name carries diacritics or uses a non-Latin script. Lettering the wordmark by hand stops being the expensive option and becomes the safe one, because a drawn mark cannot be a missing glyph, a wrong glyph, or a silent font substitution. It is also more achievable than it sounds: a short name is a tracing job, not a drawing job — write it out at size many times, photograph the best, and trace that.

Build one anchor string from the Step 2 decisions — line quality, terminal shape, fill policy, the bans — and put it first in every prompt, then the subject, then the framing. Say the bans explicitly and in the negative, because "flat" and "simple" are not read as instructions to omit shading, whereas "no shading, no gradient, no perspective, no cast shadow" often is. The anchor is a slot-filled skeleton rather than a fixed string, and only the values change between brands:

```
[medium and line quality], [terminal and corner shape], [wobble description],
[fill policy], [palette constraint], [ground], every ban stated negatively,
no text, no letters, no words
```

Then each prompt is `[ANCHOR], [subject], [framing], single object only`. Where the tool takes a separate negative prompt, the bans move there rather than being repeated in both.

Generate the two repeatability-test subjects before anything else, for the same reason a human illustrator draws them: if one organic and one hard-edged subject do not look related, tighten the anchor before generating forty assets.

Three things generators will not do reliably, so plan around them rather than fighting. They will not hold an exact line weight across assets, so trace each result to vector and set every path to the one weight — that normalising pass, not the prompt, is what makes separately generated assets read as one set. They will not produce a seamless tile, so build patterns in vector from generated elements rather than asking for the repeat. And they will not hand you a cut-out: expect an opaque rectangle, so background removal and any die line are vector work afterwards. Tracing conveniently solves resolution too, which otherwise bites when a raster result meets a print size.

On budget, give the shape of the cost rather than an average you do not have. A usable asset commonly takes several attempts and a difficult one takes many, and generation is the smaller half: the tracing and normalising pass below is usually the larger, and any estimate that leaves it out is wrong in the direction that matters. Say that the cost is dominated by the pass that comes after generation, and let the user time their first asset and multiply. Generate a surplus and cull rather than iterating one asset toward perfection: selecting six coherent results out of twenty is faster than forcing six individually, and it produces a better set, because you are choosing for consistency with each other instead of judging each one alone.

### Taking generated work to print

Tracing to vector is not optional on this route, and it does four jobs at once rather than the one it looks like. It normalises the line weight across assets, which is what makes separately generated images read as a set. It removes the resolution problem, since a raster result has a fixed pixel size and a printed surface does not care what that was. It gives you a path to build a die line or a cut outline from. And it is the only point at which the colour can be fixed.

**Reduce to the palette exactly.** A generator returns thousands of near-identical colours where you specified four, and a trace preserves that spread. Snap every fill and stroke to the exact brand hex values, with no close-enough substitutes, before anything goes to print. Two reasons, and the second is the one that gets missed: a print run is quoted on the number of colours, so an uncontrolled spread is a direct cost; and the pair matrix verified in Step 3 describes the palette, not the artwork, so until the artwork actually uses those values the verification does not apply to what is being printed.

**Check what you can rely on owning.** Whether AI-generated work attracts copyright, and whether a mark produced that way can be registered as a trademark, is unsettled and differs by jurisdiction — and a brand mark is an asset the user may later need to defend or license. This is a commercial question rather than a design one, so flag it rather than answering it: recommend that the wordmark and the primary mark be hand-drawn or redrawn, which the no-letters rule above already pushes toward, keep generation for secondary illustration where the exposure is lower, and tell the user to check the position in their market before they rely on a generated mark as an asset. Also check the generator's own terms, since commercial use and ownership vary by tool and by plan.

## Step 3: Build the palette as pairs, and verify it rather than asserting it

**Establish which regimes apply, assign colour roles, compute every pair you will actually use, and say what each pair may be used for.**

A palette is not accessible. A *pairing* is accessible, at a size, for a purpose. This distinction is the whole job, and skipping it is how brands ship a "WCAG AA palette" whose actual button is unreadable.

### Work out which regime the brand is actually in

"ADA friendly" is what people say, and it collapses three different regimes with different rules. Establish which apply before quoting any threshold, because a brand can sit in all three at once with a different answer in each. Then drop the ones that do not apply rather than covering them for completeness — a product brand with no premises does not need a paragraph on room signage, and including it to be thorough is padding a reply about a jar. Most brands in this style are on a product before they are anywhere else, so start there.

**Products and packaging — labelling rules.** Food, drink, cosmetics, supplements and several other categories carry their own requirements for the information panel: minimum type sizes, permitted type styles, and a requirement that the panel contrast clearly with its background. These are stricter than WCAG in some respects, unrelated to it in others, and they vary by market and by category. They are also the regime this aesthetic violates most reliably, because a soft ink on a mid-tone panel is the look and is precisely what the rules exclude.

How the product is sold can matter as much as what it is. Food packed in front of the customer is commonly treated very differently from the same food pre-packed for sale off a shelf, and the difference decides how much of the regime applies at all. Establish that before specifying the panel, name the regime for the user's market, and point them at the body that actually rules on it, which is often a local authority rather than a national one. Do not quote a type size as settled.

**Two things about print that the arithmetic below does not cover.** The contrast ratios are defined for sRGB on a screen, so on a printed surface they are a useful proxy and not the governing standard: ink on stock, coating, finish and ambient light all move real legibility, and a pairing that clears 4.5:1 in the calculator can still fail at 6pt on uncoated card under supermarket lighting. And print has no user-adjustable text size, so the headroom a screen gets from zoom does not exist. Take margin above the threshold on anything small and printed rather than landing on it, and treat a pairing that only just clears as failing.

**Physical premises — accessible signage standards, whichever ones apply where the business is.** Any business the public walks into, which for a product brand means the day it opens a shop, a stall or a counter.

Establish the country before naming a statute, and do not reach for the American one by reflex: people say "ADA" everywhere, and it governs only in the United States. Elsewhere the equivalent sits under that country's own disability discrimination law and building code, with its own technical standard. Name the regime that actually applies, and where you are not certain, say what kind of rule to look for rather than inventing a citation.

The shape is broadly consistent wherever you land, and the shape is what affects the design. Permanent signs identifying rooms and spaces are held to requirements on the letterforms themselves, not just on colour: characters must be sans serif and must not be italic, script, or decorative; tactile characters are accompanied by Braille; finishes must be non-glare; and characters must contrast with their background, stated qualitatively as light-on-dark or dark-on-light rather than as a ratio. Character heights and mounting positions are specified, and those figures belong to the standard and the fabricator rather than to you.

The consequence is blunt and worth saying early, because it protects the brand from being blamed later: **an expressive hand-drawn or script face is not permitted on these signs at all.** No contrast ratio rescues it. Design the compliant signage as its own zone that the brand visits rather than governs, and give the fabricator the neutral face and the two colours rather than the brand file.

**Screens — WCAG.** Website, shop, social, email. The ADA sets no contrast numbers itself; WCAG 2.1 Level AA is the benchmark regulation and litigation have converged on, and its thresholds are numeric and exactly computable, which is why the mechanics below are written against it. A product brand still lands here the moment it has a shop or a listing, and here the numbers govern rather than approximate.

You are not giving legal advice. Say which regimes apply, one line each, and move on to the arithmetic, which is the part that is actually actionable.

The WCAG thresholds:

- **4.5:1** for body text and any text below the large threshold.
- **3:1** for large text, meaning 24px or larger at regular weight, or 18.66px or larger at bold. This one gets misapplied constantly: it is a size-and-weight exemption, not a headline exemption.
- **3:1** for interface components and for graphics that carry meaning — a button border, an icon that is the only label, a chart segment.
- **No requirement** for a logotype, for purely decorative illustration, or for disabled controls.

That last exemption matters enormously here and is routinely got wrong in both directions. A hand-drawn wordmark in a soft mid-tone is compliant, and forcing it to 4.5:1 destroys the brand for no accessibility gain. The same soft mid-tone used for the price on a product page is a failure. The colour did not change. Its job did.

### Compute the ratio, do not estimate it

State a contrast ratio only when you have actually calculated it. An eyeballed ratio is a guess, it will be wrong by enough to flip a verdict, and it is worse than saying nothing because the user will ship on it.

For each channel, take the sRGB value as 0–1, then linearise: if the value is at or below 0.03928, divide by 12.92; otherwise raise `(value + 0.055) / 1.055` to the power 2.4. Relative luminance is `0.2126 R + 0.7152 G + 0.0722 B` on those linearised values. The ratio is `(L_lighter + 0.05) / (L_darker + 0.05)`.

`scripts/contrast.py` in this skill does it for you. Pass the colours positionally, optionally labelled, and it prints the full pair matrix with a verdict per pair:

```
python3 scripts/contrast.py ground=#FBF4E9 ink=#1E2A3A accent=#7FBBD9
python3 scripts/contrast.py --darken '#7FBBD9' '#FBF4E9'
```

`--darken` answers the question that always follows a failure: it holds the brand hue and walks lightness down until the pairing clears 3:1, 4.5:1 and 7:1, so the text colour is derived from the brand rather than picked by eye. It returns the *first* value clearing each tier, which means the 4.5 result sits fractionally above the line — fine on screen, and to be treated as failing on anything printed or read by an older audience, where the 7:1 result is the one to take. Use the script whenever you can execute code, and do the arithmetic explicitly when you cannot.

### When the colours arrive as words

Users name colours in English — mustard, sage, terracotta, oat — far more often than in hex, and the instruction to compute rather than estimate then has nothing to compute on. Do not let that stall the answer, and do not quietly invent hex codes and present the resulting ratio as authoritative, which is the worst available outcome because it looks exactly like a verified one.

Pick a reasonable stand-in for each named colour, say in the reply that it is a stand-in, run the matrix on it, and offer to recompute on the real values. The verdicts usually survive the substitution when a pairing is far from a threshold, and that is worth saying: a pairing computing at 1.8:1 will not become compliant with a slightly different mustard, so the guidance holds. Flag the ones that land near a threshold as genuinely dependent on the real value, because those can flip.

### Deciding whether a mark is decoration or vocabulary

This style makes the distinction hard, because everything on the surface is a hand-drawn mark and the exemption for decoration is broad. Resolve it with one test rather than by feel: **remove the mark, and ask whether information disappears from that surface.** If the same distinction is also carried by a word or a number beside it, the mark is decoration and carries no requirement. If the mark is the only thing telling two states, categories or controls apart, it is vocabulary and needs 3:1.

The status of a mark is therefore not a property of how it was drawn, and it can change without redrawing it. A squiggle that borders a label is decoration; the same squiggle used on one variant and not another to signal heat level is vocabulary. Say which of your marks are which in the guidelines, because the person applying them later will not re-derive it.

### Assemble the palette

Build it as roles, not as a row of swatches, because the roles are what get checked:

| Role | Use | Contrast obligation |
|---|---|---|
| Ground | The dominant surface | Reference for everything on it |
| Ink | Line art and body text on ground | 4.5:1 against ground where it sets text; none where the line art is decorative |
| Accent | Highlight; one or two, unless a product line needs one per variant | 3:1 where it distinguishes variants, none where decorative |
| Utility | Error, warning, success | 4.5:1 plus a non-colour signal |

A product line is the common reason to exceed two accents: a colour per SKU is how shoppers find the variant they bought last time. Treat that set as its own problem rather than as more accents. Each variant colour has to be distinguishable from every other variant colour, not merely from the ground — check them against each other in the matrix, since two pastels can each sit prettily on cream and be indistinguishable side by side on a shelf. And because a variant colour is doing identification work, it is vocabulary, so pair it with a distinct mark or word rather than relying on the colour alone.

Then produce the **pair matrix**: every foreground against every ground you will actually use, with the computed ratio and the verdict at each threshold, and a plain statement of what each pair may be used for. "Accent on ground: 2.4:1 — decorative shapes and the logotype only, never text, never an icon that is the only label." That sentence is the deliverable. A list of hex codes is not.

### The trap this aesthetic walks into

The naive style's favourite palettes are mid-tone on mid-tone: sage on blush, terracotta on cream, dusty blue on oat. They are its whole appeal, and they are exactly the pairings that land between 2:1 and 3.5:1 — comfortably failing while looking, to the designer who chose them, perfectly legible.

Do not resolve this by darkening the brand into something else. Resolve it structurally. Keep the soft pairing for what has no obligation, which is genuinely most of the surface area in this style: the illustration, the pattern, the ground, the logotype. Then add one deep neutral to the palette that is *only* for text and meaningful icons. One extra colour buys compliance without touching the look. Brands that instead push every colour toward legibility end up with a palette that passes and no longer looks hand made, and the user will quietly abandon it.

Two more rules that get dropped:

- Colour cannot be the only carrier of information, so if a state, a category or a status is colour-coded, it also needs a shape, a label, or a distinct hand-drawn mark. This style is well placed to do that, because it already has a mark vocabulary.
- Specify how the palette inverts. On screen that is a mode; in print it is a substrate and ink decision made once per format, and reversing fine line work out of a dark ink is a production question for the printer as much as a design one, since thin reversed lines fill in. Either way, dark grounds are not the light palette with the values swapped; the same hue at the same lightness reads heavier on dark, and thin naive line work in particular thickens and closes up. State the ink for dark ground explicitly and re-run the matrix for it.

### Taking the palette to print

Everything computed above is sRGB, and a printed pack is not sRGB. Skip this on a screens-only brand; on anything printed it is the step between a verified palette and a correct one.

**Convert deliberately rather than letting it happen.** Soft, light, desaturated colours — this style's entire palette — are the ones that move most in conversion, and pastels are where a chalky cream turns muddy or picks up a cast nobody chose. Specify the print values yourself and put them in the guidelines beside the screen values, so the brand carries a mapped pair for each colour rather than one set of numbers that silently means something different on each surface.

**Where a colour has to match across different materials, specify a spot colour rather than a process build.** The same build prints differently on a paper carton, a plastic film sachet and a wrapped label, and a customer holding two of your formats sees the mismatch immediately even though neither is wrong on its own. Spot inks cost more and are the cheap option here, because a brand colour that drifts by substrate is not a brand colour.

**Then re-check any pairing that was near a threshold**, because the conversion moves the values and a pairing that only just cleared can land under. This is why margin matters more on print than the number does.

**Get a physical proof on the actual substrate and finish before signing anything off.** A screen lies, a desktop print lies differently, and coating changes it again — a matte or soft-touch laminate knocks contrast down measurably, and it is applied after every decision above was made. Read the proof at arm's length in ordinary shop lighting, and where the audience skews older, have someone in that age band read it without reading glasses. That test costs nothing and finds what the arithmetic cannot.

**What the print deliverable actually is.** On a printed surface the ratios screen and rank rather than certify: they eliminate pairings that cannot work and they cannot approve the ones that survive, because the governing standard is the labelling regime and the real test is the proof in the hand. So deliver three things rather than a matrix alone — the pair table with margin applied and near-threshold pairings treated as failures, the panel spec taken from the regime rather than from taste, and the proof test above with a named person to run it.

## Step 4: Type, where exactly one voice is allowed to be loud

The logotype in this style carries the entire personality. That is the load-bearing fact of the type system, and everything else follows from it: the supporting faces are quiet on purpose, and a second expressive face does not add character, it splits it. The most common failure is a marker-drawn wordmark, a script sub-line and a handwritten body face, all three shouting, and the brand reading as chaotic rather than warm.

Give the system as three roles:

- **Display / logotype.** The loud one. Rounded and blobby with tight spacing, a marker or brush hand, or genuinely custom lettering. This is the one place to spend budget or drawing time.
- **Support.** One quiet, sturdy face for headings and interface. A neutral grotesque or a soft humanist sans, with a real weight range. Its job is to disappear.
- **Utility.** Small text, tables, numbers, legal panels. Often the same family as support, at a size and weight chosen for the worst-case reading condition.

For each recommendation, give the reason it fits *this* brand and what it will struggle with, so the user is choosing rather than reading a menu. Then run every candidate through these, because expressive faces fail on exactly these and it is always discovered late:

- **Weights available.** Many display and handwriting faces ship in a single weight. If the system needs emphasis inside a heading, that face cannot provide it and the workaround will be bad.
- **Character set, tested rather than assumed.** Hand-drawn and display faces have the thinnest coverage of any category. Checking that a face "has accents" does not catch the real failure: several languages stack more than one mark on a single vowel, and a font can render the simple accented forms perfectly while collapsing on the stacked ones — so you type one character, watch it appear, and pass a font that cannot set the actual copy. Test by pasting a line of the brand's own real text, including its longest words and a price, and inspect every mark. Watch for silent substitution as much as for a missing-glyph box: a fallback face quietly supplying the character is what survives all the way to print, because nothing looked broken.

  Where a name or its copy carries diacritics or a non-Latin script, two of the Step 6 specs change shape. Clear space is measured from the outermost mark rather than from the cap height, since a diacritic is what something crashes into. And minimum size is set by the mark, not the letter: the mark merges into the character below it before anything else becomes illegible, and a name whose mark has merged is a different word.

  When the brand sets two languages, the face has to carry both and the layout has to hold both. Set both in the same family — one language in the expressive face and the other in a plain one reads as a decision about which language is real. Fix the order once and keep it everywhere, and build the layout to whichever language runs longer so the shorter one does not leave a hole.
- **Figures.** Tables, prices, and nutrition panels need tabular lining figures. A handwriting face with proportional figures makes any column of numbers ragged.
- **Legibility floor.** Script and handwriting faces have a size below which they stop being readable, and it is much higher than designers assume. Confine them to display sizes. Never set body copy, never set legally required text, and never set anything a user must read under stress in them. This is not a preference; it is the accessibility half of the brief, and low-vision and dyslexic readers are who it protects.
- **Licence.** Say the licence and what it permits, since desktop, web, app embedding and logo use are separately granted and a font legal in a mockup can be illegal on a shipped app. Prefer openly licensed families when the user has no type budget, and say when the paid option is genuinely worth it. Never draw a logotype from a face whose licence forbids modification without saying so.
- **Fallback stack**, *screen only, so skip it for a brand with no digital surface rather than padding the answer.* Whatever is used on screen needs the fallback named and the metric difference between the face and its fallback checked, or every layout shifts when the webfont fails.
- **The tool the user actually has.** A face is only usable if it is available where they work. Custom font upload is a paid feature in some design tools, and OpenType controls such as tabular figures are unavailable in others. Confirm the face and the features are reachable in their tool before designing around them, and where a feature is missing, say what to do instead — for a short run of numerals, drawing them by hand suits this style better than fighting the software.

Set the **scale and pairing rules** as ratios rather than a fixed list of sizes: the relationship between display, heading, and body, the tracking the logotype needs at large and small sizes, and the minimum size the display face may be used at. A fixed size list is wrong on the next surface; a ratio survives.

## Step 5: Patterns

Patterns are where this style earns its keep, because they cover large surfaces cheaply and they are where the brand's personality gets applied without another commissioned drawing.

**Choose the motif against the surfaces, not the mood board.** "Stripes or dots?" is the most common question here and it has a real answer, because the families behave differently once they are wobbly and once they are small.

Scattered marks — dots, rounds, small objects — are the safe default. Density can be dropped right down behind text and tightened elsewhere without redrawing anything, and irregular placement hides the repeat.

Ruled families — stripes, checks, grids — are the risky ones in this style, and the risk is invisible at the size you design them. Hand-drawn stripes that are pleasantly uneven at hero scale turn into tramlines and can moiré against the printer's screen or a display's pixel grid when they shrink, and horizontal rules fight lines of text in a way scattered marks do not. Use them where they stay large, keep them off small printed pieces, and if the brand wants stripes everywhere, draw a separate coarser version for the small surfaces rather than scaling the same tile down.

Spirals and continuous line motifs sit in between: they carry the hand beautifully and they are the hardest family to tile, because a continuous line has to leave and re-enter the tile edge at matching positions. Budget more time or place them as single elements rather than a repeat.

**Draw them with the same pen.** A pattern built from geometrically perfect circles beside illustration built from wobbly ones instantly reads as two brands. The stripes are not parallel. The dots are not identical. The spiral does not have a constant pitch. The Step 2 rules govern here exactly as they govern the figures, and this is the most common place they are quietly abandoned.

**Make it actually tile.** A tile is seamless only when every element crossing an edge is duplicated at the opposite edge, offset by exactly the tile width or height. In SVG, use a `<pattern>` with `patternUnits="userSpaceOnUse"` and a fixed width and height, and draw the edge-crossing elements twice. A straight repeat puts the seam on a grid and shows tramlines in the diagonal; a half-drop, offsetting alternate columns by half the tile height, hides them and is the better default for anything organic. Verify by tiling at least three by three and looking for the two artefacts that always appear: a visible seam, and an accidental diagonal alley of aligned elements.

**Compensate the stroke when you scale.** Scaling a motif scales its outline with it, so a scale ladder built by scaling the tile silently breaks the one-weight rule the whole system rests on — a motif at 0.45 draws its line at 0.45 too, and the small end of your ladder is a lighter brand than the large end. Set each instance's stroke width to the base weight divided by its scale factor, so the apparent weight is identical at every size. This is the most common way a hand-drawn pattern violates its own pen rules, and it happens precisely to people following the scale-ladder advice below.

The mechanics below are the same wherever the pattern ends up; the SVG is how it ships to a screen, and for print you build the identical tile in the vector tool the artwork lives in. Replace the placeholder path with the motif and keep the structure:

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="360" height="360">
  <defs>
    <path id="mark" d="…"/>            <!-- one motif, drawn once, centred on 0,0 -->
    <pattern id="tile" patternUnits="userSpaceOnUse" width="180" height="180">
      <g fill="none" stroke="#000" stroke-linecap="round">
        <use href="#mark" transform="translate(40,32)"             stroke-width="3"/>
        <use href="#mark" transform="translate(112,96) scale(0.75)" stroke-width="4"/>
        <!-- any mark crossing an edge is drawn again at the opposite edge, -->
        <!-- offset by exactly the tile width or height -->
        <use href="#mark" transform="translate(176,140) scale(0.6)" stroke-width="5"/>
        <use href="#mark" transform="translate(-4,140)  scale(0.6)" stroke-width="5"/>
      </g>
    </pattern>
  </defs>
  <rect width="360" height="360" fill="url(#tile)"/>
</svg>
```

Every `stroke-width` there is the base weight divided by that instance's scale, which is the compensation described above: 3 at full size, 4 at 0.75, 5 at 0.6.

**Build a scale ladder, not a pattern library.** One motif at three scales does more work than three motifs, and it holds together, which three motifs will not. Say which scale belongs to which surface, and give the largest one a low enough density that it does not turn into texture-coloured mush on a big surface.

**Then check the patterns against Step 3, because this is where a verified palette gets destroyed.** Text over a pattern does not have a contrast ratio; it has a different ratio against every element it crosses, and the binding one is the worst of them. Either keep text off the pattern entirely, put it on a solid panel, or constrain the pattern's colours so that its lightest and darkest elements both clear the threshold against the text. Say which of the three the brand is doing. A pattern is also a texture that thin naive line work disappears into, so check the line art on it as well, not just the type.

**Say how it ships**, which means different things on each route and only one of them will apply.

*Printed or made:* give the colour count, since a two-colour pattern is a different price on packaging than a four-colour one, and note that screen printing and embroidery both set minimums on line weight and gap that thin wobbly lines fail. Say how the pattern behaves on a curve and at a seam, because a can, a cup and a tote all cut it somewhere, and where the seam falls should be a decision rather than a surprise.

*On screen:* ship the tile as SVG rather than a raster export, so it stays sharp at every density and the stroke widths remain editable when the ladder is retuned. Give the tile dimensions and the per-scale stroke widths alongside it. Watch total file weight where the pattern is dense, since a tile with a few hundred elements is cheaper to repeat than to flatten, and check the pattern renders identically on both platforms before it goes into a shipped build.

## Step 6: Assemble, and say how it stays coherent

Deliver the system as the smallest thing that is actually usable, which is: the pen rules, the palette with its pair matrix, the type roles with their bans, the pattern set with its scales, and the applications the brand needs on day one. Resist writing a fifty-page manual for a business with three touchpoints.

Include the parts that get discovered missing:

- The **one-colour version** of every mark. On a physical route that is for embroidery, foil, engraving and any surface that gets one ink; on screen it is for monochrome tab-bar and notification icons, and for anywhere the mark sits on an unpredictable ground. Both routes need it, so an identity that only works in its full palette is not finished either way.
- The **small-size version.** Naive line work closes up and fills in when reduced. Name the size below which detail is dropped, and provide the simplified mark.
- The **clear space and minimum size** for the logotype.
- **What not to do**, drawn from the actual risks: do not recolour the line art, do not add a stroke to the wordmark, do not set the display face in a paragraph, do not put type on the dense pattern.
- The **zones the brand does not govern**, one for each regime in Step 3 that applies. For a product, that is the information panel: a cream nutrition table on a mid-green panel is precisely what labelling rules exclude, and it is the most common compliance failure in this style's packaging. For premises, it is the permanent room signage, where the brand face is not permitted at all. Write each one as a fixed spec — the neutral face, the two colours, no pattern, no illustration — so that whoever builds it is not improvising from the brand file. This is the section most likely to be missing, because the identity looks finished without it.

If the identity has to survive a handoff, name what a new designer must not change, and separate it from what they are free to invent. That is the same anchor problem childrens-book-illustration-brief solves for a book, and it fails the same way when it is left implicit.

## Common failure modes to avoid

These are the ones that survive following the steps above, not restatements of them.

- **Executing an aesthetic brief that does not suit the buyer, without saying so once.** The user chose the look before they wrote to you, and the categories where it misfires are exactly the ones where it was chosen hardest. One paragraph, then build what they asked.
- **Handing sRGB values to a press.** The computed matrix describes screen colour, and a printed pack is a conversion away from it, on a substrate, under a finish. A palette that was verified and never converted is not the palette being printed.
- **Designing the largest format first**, so the small pack becomes whatever survived rather than a deliberate reduction, and the regime's mandatory content is discovered not to fit.
- **Producing a beautifully structured answer full of invented numbers.** This file demands specifics, and the specifics it cannot supply are production minimums and regulatory figures. A rigorous-looking spec with a fabricated vinyl minimum in it is more dangerous than a vague one, because nobody checks it until the plates are cut. Mark every such number as a starting point with an owner.
- **Stating a ratio and a point size that disagree.** A weight given both ways has to be reconciled, and unit conversion is where the contradiction hides. Two contradictory specs for one rule produce two different brands.
- **Answering the accessibility question for the wrong regime.** A screen answer to a business whose exposure is its front door, or a WCAG ratio quoted at a nutrition panel as though it governed. Establish the regime before quoting a number.
- **Treating a mark's status as fixed.** Decoration becomes vocabulary the moment it is the only thing distinguishing two options, without being redrawn, and the guidelines are usually written before that happens.
- **Building the scale ladder by scaling the tile**, so the small end of the pattern is a lighter brand than the large end.
- **Verifying the palette, then putting the text on the pattern and voiding it.**
- **Letting the completeness instinct leak into a small question.** The heavy sections model a register that bleeds upward, and a user who typed one line gets six hundred words back. Match the answer to the question.
- **Confusing naive with careless.** The style is consistently distorted, not randomly wrong. Random wobble is the tell of a machine imitating a hand; a real hand is consistently imprecise.
- **Solving a failing pairing by darkening the whole brand**, producing a palette that passes and that the user quietly abandons because it no longer looks hand made.
- **Delivering a system with no one-colour mark and no small-size behaviour**, which is discovered the first time anyone orders embroidery or looks at the profile picture.

## If the user only wants one thing

Answer it at its own size, and bring only the named sections. Nothing else in this file enters the reply, and an existing brand does not turn a small request into a full extraction — take the two or three rules the asset touches and move on.

**A font pairing:** give two or three pairings, each with why it fits this brand and what it will struggle with, and run the display candidate against weights, character set, figures, and licence. If the brand has an existing logotype, the pairing question is really "what is quiet enough to sit under this", so ask what the logotype is before recommending.

**A colour question:** compute the ratio, give the verdict at 4.5:1 and 3:1, and say what that pair may and may not be used for. If they asked whether their palette is accessible, answer with the pair matrix rather than a yes.

**A single pattern** — bring Step 5's motif choice, tile mechanics and stroke compensation, plus the decoration-or-vocabulary test in Step 3 if any text sits on it. Get the surfaces and the existing pen rules, note that the colour count is usually obvious from the brand, draw it under those rules, and give it as SVG with the edge duplication and the per-instance stroke widths right.

**A logotype direction:** propose two or three routes with what each one commits the brand to later, since a custom-lettered mark and a licensed-face mark have very different consequences for the rest of the system.

Everything else in this file stays out of the reply.
