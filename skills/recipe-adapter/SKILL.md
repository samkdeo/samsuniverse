---
name: recipe-adapter
description: Reworks a recipe for a dietary constraint, a missing ingredient, a different quantity, or different equipment, explaining what each substitution changes structurally rather than swapping one to one. Use this skill when someone says "can I make this without", "how do I make this vegan / gluten-free / dairy-free", "I don't have X, what can I use", "can I halve this", "I only have a 20cm tin", "can I make this ahead", or hands over a recipe with a constraint attached. It says when a swap will not work and what to make instead, rather than producing something that technically follows the instructions and fails.
---

# Recipe Adapter

Adapts one recipe to one constraint, and says what the change does to the result. The failure mode it exists to prevent is the confident one-to-one substitution table: a swap that is chemically wrong produces a dish that looks like the recipe, follows the instructions, and does not work, and the cook does not find out until it is too late to do anything about it.

It is not a recipe generator and it does not invent dishes. It also does not give nutritional or medical advice, and where a constraint is a medical one it says what matters and where the real answer comes from.

## First: is this an allergy or a preference?

Ask, or read it from the request, because the two need different answers and getting it wrong is the one genuinely dangerous outcome here.

**A medical allergy or intolerance** means cross-contamination matters, hidden sources matter, and "a small amount is fine" is not available. Where this is the case:

- Say that ingredient labels are the authority and must be read each time, because formulations change and the same product differs between manufacturers and countries.
- Name the non-obvious places the allergen commonly hides in this kind of dish, as things to check rather than as claims about specific products.
- Do not assert that a named commercial product is free of something. That is a label-reading job, it changes, and being wrong is serious.
- Where the allergy is severe, say plainly that shared equipment, shared oil, and shared surfaces are part of the question and not merely the ingredient list.

**Coeliac disease** deserves specific mention because it is routinely treated as a preference: it requires avoiding cross-contamination and checking processing, not just leaving out obvious wheat.

**A prescribed dietary restriction that is not an allergy** is a third category and the allergy-or-preference question misses it entirely. Sodium, potassium, protein, sugar, fibre, fat, fluid, and texture-modified diets all arrive from a clinician with a number attached, and they behave differently from both of the others: cross-contamination is irrelevant, but the quantity is the whole point, and the person's own team sets it rather than a recipe. So do not state a target, a limit, or a daily figure. Adapt the recipe to reduce or remove the thing, say roughly which ingredients are carrying most of it so they can spend an allowance where it matters, and leave the number to whoever set it.

Two things belong here and nowhere else. **A substitute can itself be clinically risky**, which is the trap in this category: a replacement product that removes the restricted thing by adding something else can be actively contraindicated for the very condition that prompted the restriction, and the user should check a substitute product with their clinician before adopting it, not after. Say this whenever the obvious swap for a prescribed restriction is a manufactured replacement rather than a technique. And **taste recalibrates**, over weeks rather than days, for reductions in salt, sugar, and fat. Say so in advance, because the first attempt tastes wrong to everyone and someone who judges the recipe on it will abandon a version that was fine.

**A preference or a soft intolerance** allows trade-offs a medical constraint does not, including "this works better with a little of the thing, up to you."

**Alcohol needs its own note**, because it is routinely treated as a preference and is often not one — recovery, medication, pregnancy, and religious observance are all absolute, and the person asking usually knows that. The important thing to say, because almost everyone believes otherwise: cooking does not remove all the alcohol. A meaningful fraction survives even long simmering, more in anything covered, and a dish made with wine or spirits is not an alcohol-free dish however long it cooked. Where someone has said "not even cooked", take it literally, and treat the low-alcohol and de-alcoholised products as a label-reading question for the person concerned rather than as a solution, since several are not actually at zero.

Say which you have assumed, once, and move on. This is a paragraph, not a disclaimer wall.

## Step 1: Work out what the ingredient is doing

The whole method. Before substituting anything, identify the job the ingredient performs in this specific recipe, because the same ingredient does different jobs in different dishes and the right swap follows from the job rather than from the ingredient.

The jobs worth distinguishing:

- **Structure.** Holding the thing together or letting it rise: gluten networks, egg proteins, gelatine.
- **Leavening**, and by which route: chemical, biological, mechanical, or steam.
- **Fat**, which carries flavour, shortens gluten strands, holds air when creamed, and browns. Solid at room temperature or liquid is often the load-bearing property, not the fat itself.
- **Liquid and hydration.**
- **Sugar**, which sweetens and also holds moisture, browns, softens texture, and stabilises foams. A sugar that is reduced is not only less sweet.
- **Acid**, which reacts with alkaline leaveners, tenderises, sets some proteins, and cuts richness.
- **Salt**, which seasons and also controls fermentation and strengthens gluten.
- **Emulsification**, keeping fat and water together.
- **Flavour**, the one everyone thinks of and often the easiest to replace.
- **Bulk**, where something is largely there for volume.

There is a reliable way to do this rather than guessing, and it is worth doing explicitly: **audit the whole ingredient list by job, and look for the jobs with only one source.** Anything that is the sole supplier of a job in that recipe is load-bearing, and removing it takes the job with it. This catches the failures that a per-ingredient view misses, because the problem is rarely the ingredient and usually the gap it leaves. A recipe whose only liquid arrives inside another ingredient, or whose only acid is in the thing being swapped out, will fail in a way that no amount of care about the substitute itself would predict. Run that audit before proposing anything.

Most ingredients do several of these at once, and that is where substitutions fail: swapping for the obvious job while silently losing the others. Say which jobs the substitute covers and which it does not, and what the consequence of each loss will be.

## Step 2: Decide whether the recipe survives the change at all

Be honest about this before adapting, because the useful answer is sometimes that the swap does not work.

The distinction that matters is **how much the dish depends on the chemistry it is asking for.**

- **Forgiving dishes** — most braises, soups, stews, stir-fries, sauces, and roasted vegetables — tolerate substitution well. Here the answer is usually yes, adjust seasoning, and taste as you go.
- **Structural dishes** — most baking, custards, emulsions, anything set or aerated, anything that relies on a specific protein or starch behaviour — do not. Here the same swap that was fine in a stew produces something that does not set, does not rise, splits, or turns to liquid, and the cook has no way of knowing until the end.

Where a recipe genuinely will not survive, say so and offer the alternative: a different recipe designed for the constraint, which is nearly always better than a heavily patched one. A cake formulated without eggs from the start beats an egg-based cake with eggs removed, because the whole formula was rebalanced rather than one line changed.

Say what will be different even when the swap works. Every substitution has a cost, and the cook should know whether they are getting a very good version or an acceptable one.

## Step 3: Give quantities and technique, not just the swap

A substitution that names an ingredient and no amount is half an answer, and it is where most published swap tables stop.

Where you are supplying a quantity that came from general knowledge rather than from the user's recipe, say so and give it as a starting point to check rather than as a specification, particularly for anything where being wrong is expensive: quantities per person when cooking for a group, anything that determines whether a batch fits its container, and anything the user cannot correct once it is committed. A cook can sanity-check a portion size against their own experience in a second if they are told it is an estimate, and cannot if it is presented as fact.

Include, for each change:

- **The amount**, and whether it is by weight or by volume, since many substitutions are not one to one by either and the difference between them is where things go wrong.
- **What else has to change because of it.** Substitutions rarely stand alone: a swap that adds liquid means less liquid elsewhere, one that removes acid means the leavening needs rethinking, one that changes fat state means the mixing method changes.
- **Whether the method changes.** This is the part that gets missed. Sometimes the substitution is fine and the technique is what has to move — a different mixing order, a longer rest, a lower temperature, a different pan.
- **Timing and temperature**, where the swap changes browning or moisture, which many do.
- **What to look for**, since with an altered recipe the stated time is no longer reliable. Give the sensory cue: the colour, the texture, the sound, how it should behave when moved. This matters more in an adapted recipe than in an original one and it is what rescues the cook when the numbers no longer apply.

## Step 4: Scaling is not multiplication

Treat quantity changes as their own problem, because the arithmetic works and the cooking does not.

- **Ingredients mostly scale; times and temperatures do not.** A doubled tray takes longer than the recipe says and less than twice as long, and the only reliable guide is the doneness cue rather than the clock.
- **Pan size is the constraint that actually matters.** What governs is the depth of the mixture and its area, so scale by the pan's volume and then check what the depth is doing: the same batter in a deeper tin needs a lower temperature and a longer time, and in a shallower one the reverse.
- **Some things do not scale at all.** Anything that has to fit in a pan in a single layer, anything reduced, anything where a volume of liquid evaporates, and anything relying on browning, which needs surface contact and space. Doubling these means two batches, and saying so is more useful than a scaled recipe that steams instead of browning.
- **Strong seasonings, leaveners, and salt in fermentation scale less than proportionally** in practice. Scale the base, then taste and adjust, and say so rather than multiplying blindly.
- **Halving an egg** is the small recurring nuisance: beat one and use half by weight, or find a use for the rest.

## Step 4b: Cooking for a crowd is a different problem

Scaling up for a large group is the commonest real adaptation request and it is not the same as multiplying a recipe. Two things change.

**The vessel governs, not the serving count.** For anything wet, the amount of liquid is set by how far up the food it comes in the container being used, not by a multiplier — the same weight of food spread across several wide trays needs far less liquid than the arithmetic suggests, and drowning it is the standard error. Fill to the level the method requires and stop, whatever number that turns out to be. Likewise depth: a deeper mass takes real extra time to reach and hold temperature, so times extend even though they do not multiply.

**And at this scale it becomes a food safety problem rather than only a cooking one.** This is the part missing from most scaled-up advice and it matters more than any substitution:

- **Cooling is the risk, not cooking.** A large volume of hot food holds heat for hours and stays warm in the middle long after the outside is cool, which is exactly the condition to avoid. The fix is to divide into shallow containers and cool fast in the coolest place available, uncovered until steaming stops, rather than putting a deep hot container into a fridge, where it will neither cool nor leave the rest of the fridge safe.
- **Reheating has to reach the middle**, not the edges, and should be checked there rather than assumed. Reheat once.
- **Holding food warm for service** is its own window and a real constraint on what can be made ahead.
- **Say when making it ahead is actively better**, which for many slow-cooked dishes it is, because it converts a timing problem on the day into a reheating one.

Where the user is cooking for a group in a venue rather than a kitchen, ask what equipment is actually there, since the plan depends on it entirely.

**Containers are part of the answer.** Whether a container can be lifted safely when full, whether it can be covered, and whether the material is suitable for the contents and the cooking time are all real constraints, and a long cook with acidic contents in a thin reactive container is a genuine flavour and integrity risk rather than a fussy detail.

## Step 5: Equipment substitutions

Same method. Ask what the equipment is doing, and match that rather than the object.

The properties that actually matter are the ones people ignore: the material and how it conducts heat, whether it is dark or light, how deep the food sits, whether the surface is loose-bottomed, and how much air circulates around it. A tin swapped for one of a similar volume but a different depth is a real change and needs a temperature adjustment.

Where the recipe assumes something the cook does not have — a stand mixer, a food processor, a specific oven behaviour — say whether the manual version is genuinely equivalent, harder, or not achievable, rather than implying they are all the same.

## Step 6: The constraints worth knowing specifically

Not a substitution table, but the things that recur, framed as what to reason about:

- **Eggs** do several different jobs, and the right replacement depends entirely on which one. Binding, leavening, enriching, setting, and aerating each need a different answer, and a general egg substitute works for some and not others. Establish the job first, and be direct that the aerating one is the hardest to replace.
- **Dairy** splits into fat, water, protein, and sugar, and the alternatives differ enormously in all four. The plant milks are not interchangeable with each other, several behave differently when heated or acidified, and the low-fat ones fail in exactly the applications where fat was the point.
- **Gluten** is structure, so removing it means replacing a network rather than a flour. Expect a different hydration, a different rest, and often a binder, and expect single-flour swaps to disappoint.
- **Sugar** reductions change texture and browning as well as sweetness, and the intense sweeteners contribute no bulk, so anything relying on sugar for structure will need rebalancing.
- **Fat reductions** change mouthfeel, browning, and keeping quality, and the common fixes add moisture rather than fat, which is not the same thing.
- **Salt** is the most common prescribed restriction and the most misunderstood, because it is doing more than seasoning: it suppresses bitterness, strengthens gluten, controls fermentation, draws out water, and preserves. Removing it from a dish where it was only seasoning is easy; removing it from a dough, a cure, or a ferment changes the process rather than the flavour. What replaces the seasoning job is not a salt substitute but acid, aromatics, browning, and concentrated savoury ingredients, and acid does the most work of the four. Two technique points beat any substitution: added at the end rather than cooked in, a small amount of salt reads as far more, and food that tastes flat rather than under-seasoned usually needs acid rather than salt, which is a distinction people cannot make by instinct and can learn in one meal.

  Watch for the recipe where several separate ingredients are all supplying the same savoury job. Each looks individually removable and together they were the entire backbone, which is the audit from step 1 doing its most useful work.

- **Alcohol** is often carrying flavour and dissolving compounds water cannot; replacing it usually means replacing acidity or depth, not adding grape juice.

## Step 7: Deliver

Give back:

1. Whether this works, honestly, and how well
2. The adapted recipe or the specific changed lines, with amounts
3. What each change does and what it costs
4. The doneness cues, since the times no longer apply
5. Anything to check on a label, where a medical constraint is in play
6. The alternative, where the adaptation is a compromise and a purpose-built recipe would be better

Keep it proportionate. A stew with a missing herb needs a sentence, not a structural analysis.

## Common failure modes to avoid

- One-to-one substitutions with no quantity, no consequence, and no adjustment elsewhere.
- Swapping for the flavour job while silently losing the structural one.
- Treating a baking substitution with the confidence appropriate to a stew.
- Producing a patched recipe when a recipe built for the constraint would be better, and not mentioning that it exists.
- Scaling by multiplying the times along with the ingredients.
- Ignoring pan depth, which is the thing that actually changes when the tin changes.
- Doubling something that needed space to brown, so it steams.
- Keeping the original timings in an adapted recipe without giving a sensory cue to replace them.
- Asserting that a specific commercial product is free of an allergen.
- Substituting an ingredient without checking whether it was the only source of a job in that recipe.
- Scaling a wet dish by multiplying the liquid, when the container's fill level is what governs.
- Treating cooking for a crowd as arithmetic, and saying nothing about cooling, reheating, or holding.
- Telling someone the alcohol cooks off.
- Treating a prescribed dietary restriction as either an allergy or a preference, when it is neither and the quantity is the whole question.
- Recommending a manufactured substitute for a prescribed restriction without saying it needs checking with whoever set the restriction.
- Letting someone judge a reduced-salt or reduced-sugar version on the first attempt, before their taste has adjusted.
- Treating coeliac disease as a preference, or a stated allergy as fussiness.
