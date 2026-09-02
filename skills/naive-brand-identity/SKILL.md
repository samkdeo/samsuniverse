---
name: naive-brand-identity
description: Builds a brand identity in the naive, hand-drawn style — wobbly single-weight line illustration, rounded or blobby display logotypes, handwriting and script wordmarks, sticker sets, and repeating patterns — and specifies it as a system that survives being drawn twice. Covers the drawing rules that keep a set coherent, palettes checked against WCAG contrast thresholds rather than eyeballed, type pairings with the licensing and character-set traps named, and seamless pattern construction for stripes, spirals, dots, checks, squiggles, and abstract marks. Use this skill whenever someone wants a hand-drawn, doodle, childlike, naive, marker, crayon, sticker, cutesy, quirky, or illustrated brand, asks for a bold rounded or blobby logotype, wants brand colors that are "ADA friendly", accessible, or WCAG compliant, asks for font pairings or brand guidelines for an illustrated brand, or asks for brand patterns, seamless repeats, packaging illustration, or a sticker sheet. Trigger it on "hand drawn logo", "doodle branding", "naive illustration brand", "cute packaging", "make my brand look hand made", "accessible brand palette", "font pairing for my logo", and on any request to build or extend a visual identity in this style.
---

# Naive Brand Identity

Builds and specifies a brand identity in the naive hand-drawn style: the line rules that make twenty drawings look like one hand made them, a palette verified as pairs against contrast thresholds, a type system where exactly one voice is loud, and patterns that actually tile. The hard part of this style is not making one charming drawing. It is making the fortieth one match the first, and keeping a look built on low-contrast pastels and near-illegible handwriting from failing the people who need to read the label.

It does not name the brand or write its copy. It does not produce finished illustration: it produces the drawing rules, the generation prompts, or the illustrator brief, depending on who is holding the pen. For repeating a *character* consistently across a long narrative sequence rather than across a brand's surfaces, character-bible-builder goes deeper, and childrens-book-illustration-brief covers the same anchor-drift problem for books.

## Step 0: Answer the question you were actually asked

Most requests here are small, and a small one gets a small answer. Someone asking for a font pairing gets a font pairing. Someone asking whether two hex codes pass gets the ratio and the verdict. Someone asking for a stripe pattern gets the stripe pattern. Skip to the last section of this file and stay there.

Run the full sequence when the request is to build an identity, or when a piece of one has to be designed against a system that already exists and must not break.

When the request is broad but the brand is thin — a name and a vibe and nothing else — do not answer with a questionnaire. Ask only for the two things that actually change the output, which are what the brand sells and where the identity has to live, then build. Everything else can be proposed and corrected.

## Step 1: Decide who is holding the pen, before designing anything

This changes the deliverable, not just its wording. Say which one you are producing.

**A human illustrator** needs the rules written as constraints they can hold in their hand plus reference for tone, and they will make better decisions than the spec inside those constraints. Do not over-specify individual drawings.

**An image-generation tool** needs locked prompt strings where the style anchor is byte-identical in every prompt, and it needs the precision in Step 6. This style is genuinely hard for generators, which default to rendered, shaded, gradient-filled "cute mascot" work. Budget several attempts per usable mark and say so.

**Vector drawn by hand, or SVG written directly**, is realistic for patterns, geometric marks, and simple objects, and unrealistic for expressive figures. Write the patterns as SVG. Do not promise a charming wonky character in path data.

Most brands end up mixed: patterns and marks in vector, figures drawn or generated. Say which route each asset takes.

## Step 2: Fix the pen before you fix anything else

This is the step that separates a system from a pile of nice drawings, and it is the one that gets skipped. Every drawing in the set has to read as made by one hand in one sitting. That is a set of decisions, not a feeling, and it has to be written down before the first mark, because it is unrecoverable afterwards — twenty drawings at drifting line weights cannot be reconciled without redrawing them.

Settle and record each of these:

- **Line weight**, as a real value with the artwork size it belongs to, and as a ratio so it can scale. "2pt at 100mm wide" plus "roughly 1/500 of artwork width" survives being put on a business card and a van. One weight across the whole set is the default and the strongest choice. If you allow two, define exactly what the second is for, such as interior detail only, never outline.
- **Terminal and joint**, meaning round or flat line ends and whether corners are rounded. Rounded terminals read warm and childlike. Flat reads more editorial. Mixing them is what makes a set feel bought from three stock libraries.
- **Wobble, and how much.** This is the defining variable of the style and the one described vaguely. Say it as deviation: a line that would be straight may drift up to about 2% of its own length, curves may be slightly asymmetric, circles may be off-round, and nothing closes perfectly. Then say the thing that matters more: the wobble is *consistent in amount* across the set. Random amounts of wobble is not what a real hand does. A hand is consistently imprecise.
- **Fill policy.** Outline only, solid fill, or outline plus a single offset fill that deliberately misses its edges. Pick one. The offset fill is a strong, cheap way to signal "printed by hand" and it needs its own rule for how far it may miss, or it turns into a mistake.
- **Proportion rules for figures.** Naive figures are not badly drawn realistic figures. They are consistently distorted, and the distortion is the signature: heads large relative to bodies, hands and feet simplified to mittens or hooks, limbs of even thickness with no taper, no visible joints. Write the ratios you are using.
- **Face policy.** Two dots and a line is a different brand from a face with a nose, a blush and eyebrows. This decides how much the character can emote later, so decide it against what the brand needs the character to do. Dots cannot look worried.
- **What is banned.** Perspective, cast shadows, gradients, rendered volume, texture beyond a single flat grain, and outlines of varying weight within one drawing. Naming the bans is more useful than describing the goal, because these are exactly what an illustrator or a generator reverts to under pressure.

Then write the **repeatability test**, and make the user run it before commissioning or generating the full set: draw two objects of very different kinds under the rules, one organic and one hard-edged, such as a leaf and a pair of scissors. If they do not look related, the rules are underspecified and the missing rule is usually the wobble or the fill policy. Finding that after forty assets is expensive; finding it after two is free.

## Step 3: Build the palette as pairs, and verify it rather than asserting it

A palette is not accessible. A *pairing* is accessible, at a size, for a purpose. This distinction is the whole job, and skipping it is how brands ship a "WCAG AA palette" whose actual button is unreadable.

### What the standard is

"ADA friendly" is a colloquial way of asking for WCAG conformance. The ADA itself sets no contrast numbers; WCAG 2.1 Level AA is the benchmark that regulation and litigation have converged on, and it is what to design against. Say that plainly once and move on. You are not giving legal advice, and the arithmetic is the part that is actually actionable.

The thresholds that govern:

- **4.5:1** for body text and any text below the large threshold.
- **3:1** for large text, meaning 24px or larger at regular weight, or 18.66px or larger at bold. This one gets misapplied constantly: it is a size-and-weight exemption, not a headline exemption.
- **3:1** for interface components and for graphics that carry meaning — a button border, an icon that is the only label, a chart segment.
- **No requirement** for a logotype, for purely decorative illustration, or for disabled controls.

That last exemption matters enormously here and is routinely got wrong in both directions. A hand-drawn wordmark in a soft mid-tone is compliant, and forcing it to 4.5:1 destroys the brand for no accessibility gain. The same soft mid-tone used for the price on a product page is a failure. The colour did not change. Its job did.

### Compute the ratio, do not estimate it

State a contrast ratio only when you have actually calculated it. An eyeballed ratio is a guess, it will be wrong by enough to flip a verdict, and it is worse than saying nothing because the user will ship on it.

For each channel, take the sRGB value as 0–1, then linearise: if the value is at or below 0.03928, divide by 12.92; otherwise raise `(value + 0.055) / 1.055` to the power 2.4. Relative luminance is `0.2126 R + 0.7152 G + 0.0722 B` on those linearised values. The ratio is `(L_lighter + 0.05) / (L_darker + 0.05)`.

`scripts/contrast.py` in this skill runs the whole palette as a matrix. Use it when you can execute code, and do the arithmetic explicitly when you cannot.

### Assemble the palette

Build it as roles, not as a row of swatches, because the roles are what get checked:

| Role | Use | Contrast obligation |
|---|---|---|
| Ground | The dominant surface | Reference for everything on it |
| Ink | Line art and body text on ground | 4.5:1 against ground |
| Accent | Highlight, one or two only | 3:1 if it carries meaning, none if decorative |
| Utility | Error, warning, success | 4.5:1 plus a non-colour signal |

Then produce the **pair matrix**: every foreground against every ground you will actually use, with the computed ratio and the verdict at each threshold, and a plain statement of what each pair may be used for. "Accent on ground: 2.4:1 — decorative shapes and the logotype only, never text, never an icon that is the only label." That sentence is the deliverable. A list of hex codes is not.

### The trap this aesthetic walks into

The naive style's favourite palettes are mid-tone on mid-tone: sage on blush, terracotta on cream, dusty blue on oat. They are its whole appeal, and they are exactly the pairings that land between 2:1 and 3.5:1 — comfortably failing while looking, to the designer who chose them, perfectly legible.

Do not resolve this by darkening the brand into something else. Resolve it structurally. Keep the soft pairing for what has no obligation, which is genuinely most of the surface area in this style: the illustration, the pattern, the ground, the logotype. Then add one deep neutral to the palette that is *only* for text and meaningful icons. One extra colour buys compliance without touching the look. Brands that instead push every colour toward legibility end up with a palette that passes and no longer looks hand made, and the user will quietly abandon it.

Two more rules that get dropped:

- Colour cannot be the only carrier of information, so if a state, a category or a status is colour-coded, it also needs a shape, a label, or a distinct hand-drawn mark. This style is well placed to do that, because it already has a mark vocabulary.
- Specify how the palette inverts. Dark grounds are not the light palette with the values swapped; the same hue at the same lightness reads heavier on dark, and thin naive line work in particular thickens and closes up. State the ink for dark ground explicitly and re-run the matrix for it.

## Step 4: Type, where exactly one voice is allowed to be loud

The logotype in this style carries the entire personality. That is the load-bearing fact of the type system, and everything else follows from it: the supporting faces are quiet on purpose, and a second expressive face does not add character, it splits it. The most common failure is a marker-drawn wordmark, a script sub-line and a handwritten body face, all three shouting, and the brand reading as chaotic rather than warm.

Give the system as three roles:

- **Display / logotype.** The loud one. Rounded and blobby with tight spacing, a marker or brush hand, or genuinely custom lettering. This is the one place to spend budget or drawing time.
- **Support.** One quiet, sturdy face for headings and interface. A neutral grotesque or a soft humanist sans, with a real weight range. Its job is to disappear.
- **Utility.** Small text, tables, numbers, legal panels. Often the same family as support, at a size and weight chosen for the worst-case reading condition.

For each recommendation, give the reason it fits *this* brand and what it will struggle with, so the user is choosing rather than reading a menu. Then run every candidate through these, because expressive faces fail on exactly these and it is always discovered late:

- **Weights available.** Many display and handwriting faces ship in a single weight. If the system needs emphasis inside a heading, that face cannot provide it and the workaround will be bad.
- **Character set.** Check the languages, accents and diacritics the brand actually needs, plus currency symbols. Hand-drawn faces have the thinnest coverage of any category, and a missing accent in a market you sell to is a visible defect.
- **Figures.** Tables, prices, and nutrition panels need tabular lining figures. A handwriting face with proportional figures makes any column of numbers ragged.
- **Legibility floor.** Script and handwriting faces have a size below which they stop being readable, and it is much higher than designers assume. Confine them to display sizes. Never set body copy, never set legally required text, and never set anything a user must read under stress in them. This is not a preference; it is the accessibility half of the brief, and low-vision and dyslexic readers are who it protects.
- **Licence.** Say the licence and what it permits, since desktop, web, app embedding and logo use are separately granted and a font legal in a mockup can be illegal on a shipped app. Prefer openly licensed families when the user has no type budget, and say when the paid option is genuinely worth it. Never draw a logotype from a face whose licence forbids modification without saying so.
- **Fallback stack.** Whatever is used on screen needs the fallback named, and the metric difference between the face and its fallback checked, or every layout shifts when the webfont fails.

Set the **scale and pairing rules** as ratios rather than a fixed list of sizes: the relationship between display, heading, and body, the tracking the logotype needs at large and small sizes, and the minimum size the display face may be used at. A fixed size list is wrong on the next surface; a ratio survives.

## Step 5: Patterns

Patterns are where this style earns its keep, because they cover large surfaces cheaply and they are where the brand's personality gets applied without another commissioned drawing.

**Draw them with the same pen.** A pattern built from geometrically perfect circles beside illustration built from wobbly ones instantly reads as two brands. The stripes are not parallel. The dots are not identical. The spiral does not have a constant pitch. The Step 2 rules govern here exactly as they govern the figures, and this is the most common place they are quietly abandoned.

**Make it actually tile.** A tile is seamless only when every element crossing an edge is duplicated at the opposite edge, offset by exactly the tile width or height. In SVG, use a `<pattern>` with `patternUnits="userSpaceOnUse"` and a fixed width and height, and draw the edge-crossing elements twice. A straight repeat puts the seam on a grid and shows tramlines in the diagonal; a half-drop, offsetting alternate columns by half the tile height, hides them and is the better default for anything organic. Verify by tiling at least three by three and looking for the two artefacts that always appear: a visible seam, and an accidental diagonal alley of aligned elements.

**Build a scale ladder, not a pattern library.** One motif at three scales does more work than three motifs, and it holds together, which three motifs will not. Say which scale belongs to which surface, and give the largest one a low enough density that it does not turn into texture-coloured mush on a big surface.

**Then check the patterns against Step 3, because this is where a verified palette gets destroyed.** Text over a pattern does not have a contrast ratio; it has a different ratio against every element it crosses, and the binding one is the worst of them. Either keep text off the pattern entirely, put it on a solid panel, or constrain the pattern's colours so that its lightest and darkest elements both clear the threshold against the text. Say which of the three the brand is doing. A pattern is also a texture that thin naive line work disappears into, so check the line art on it as well, not just the type.

**Production.** Say the colour count, since a two-colour pattern is a different price on packaging than a four-colour one, and screen printing and embroidery both set minimums on line weight and gap that thin wobbly lines fail. Say how the pattern behaves on a curve and at a seam, because a can, a cup and a tote all cut it somewhere, and the answer to where the seam falls should be a decision rather than a surprise.

## Step 6: Assemble, and say how it stays coherent

Deliver the system as the smallest thing that is actually usable, which is: the pen rules, the palette with its pair matrix, the type roles with their bans, the pattern set with its scales, and the applications the brand needs on day one. Resist writing a fifty-page manual for a business with three touchpoints.

Include the parts that get discovered missing:

- The **one-colour version** of every mark, for embroidery, foil, engraving, and any surface that gets one ink. If the identity only works in its full palette it is not finished.
- The **small-size version.** Naive line work closes up and fills in when reduced. Name the size below which detail is dropped, and provide the simplified mark.
- The **clear space and minimum size** for the logotype.
- **What not to do**, drawn from the actual risks: do not recolour the line art, do not add a stroke to the wordmark, do not set the display face in a paragraph, do not put type on the dense pattern.
- The **legal and regulatory panels**, which have their own rules that WCAG does not cover and this aesthetic reliably violates. Food, drink, cosmetic and supplement labelling in most markets sets its own requirements for the information panel — minimum type sizes, permitted type styles, and a requirement that the panel be in a colour that contrasts sharply with its background. A cream nutrition table on a mid-green panel is precisely what those rules exclude, and it is the single most common compliance failure in this style's packaging. Tell the user to check the rule for their market and product category, and design the panel as its own zone that the brand palette visits rather than governs.

If the identity has to survive a handoff, name what a new designer must not change, and separate it from what they are free to invent. That is the same anchor problem childrens-book-illustration-brief solves for a book, and it fails the same way when it is left implicit.

## Common failure modes to avoid

- Drawing charming individual assets with no shared pen rules, then discovering at asset thirty that nothing matches and the fix is redrawing all of them.
- Confusing naive with careless. The style is consistently distorted, not randomly wrong, and irregularity has to be as governed as everything else. Random wobble is the tell of a machine imitating a hand.
- Stating a contrast ratio without computing it, which produces confidently wrong numbers that a user ships on.
- Certifying a *palette* as accessible instead of certifying pairs at sizes and jobs.
- Applying 4.5:1 to the logotype, which is exempt, and thereby destroying the brand to fix a problem that did not exist — while leaving the actual body text on a soft accent that does fail.
- Solving a failing pairing by darkening the entire brand, when adding one text-only neutral keeps the look and fixes the problem.
- Pairing three expressive faces so nothing leads, or picking a display face that turns out to have one weight, no accents, and proportional figures.
- Patterns drawn with perfect geometry beside hand-drawn illustration.
- Patterns that do not tile, or that tile with a diagonal alley nobody checked for at three by three.
- Verifying the palette, then putting the text on a pattern and voiding it.
- Producing a guidelines document with no one-colour mark, no small-size behaviour, and no rule for the regulated panel.

## If the user only wants one thing

Answer it at its own size, and pull in only the check that changes the answer.

**A font pairing:** give two or three pairings, each with why it fits this brand and what it will struggle with, and run the display candidate against weights, character set, figures, and licence. If the brand has an existing logotype, the pairing question is really "what is quiet enough to sit under this", so ask what the logotype is before recommending.

**A colour question:** compute the ratio, give the verdict at 4.5:1 and 3:1, and say what that pair may and may not be used for. If they asked whether their palette is accessible, answer with the pair matrix rather than a yes.

**A single pattern:** ask the surface and the colour count, draw it under whatever pen rules already exist, give it as SVG with the tile mechanics right, and check it against any text that will sit on it.

**A logotype direction:** propose two or three routes with what each one commits the brand to later, since a custom-lettered mark and a licensed-face mark have very different consequences for the rest of the system.

Everything else in this file stays out of the reply.
