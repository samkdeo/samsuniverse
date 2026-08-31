---
name: naming-and-taxonomy-checker
description: Audits the names a product uses for its features, objects, statuses, labels, permissions, settings, and events, finds where the same thing is called different things or different things share a name, and proposes a consistent system plus a migration plan ranked by cost. Use this skill whenever someone says their terminology is a mess, that the UI and the API disagree, that nobody can agree what to call something, that their status labels are confusing, or that support and engineering use different words for the same object. Trigger it on "we call it three different things", "audit our naming", "clean up our labels", "our statuses don't make sense", "rename this feature", and on requests to standardize terminology across a product, a design system, or a set of docs. Not for naming a new company or product.
---

# Naming and Taxonomy Checker

Takes the terms a product already uses and returns an audit: which names collide, which duplicate each other, which break the pattern, and which are wrong for the thing they label, followed by a proposed canonical set and a migration plan ordered by what each rename costs. It works on the vocabulary of an existing system. It is not brand or product naming, so if the user wants a name for a new company, product, or feature that does not exist yet, that is a different job. It is also not translation or localization, though it will flag a term that will not survive translation.

## Step 0: Size the job before starting it

Two very different requests trigger this skill, and running the wrong one wastes the user's time.

A single name, such as "what should we call this new status" or "is this the right word for this button", gets a short answer. Skip everything below and follow the last section of this file instead. Do not ask someone who typed a one-line question for their database schema.

A full audit, meaning terminology that is inconsistent across a product, gets the whole sequence below.

When it is genuinely unclear which one you are being asked for, answer the narrow question first and offer the audit second.

## Step 1: Collect the inventory before judging anything

Names live in more places than people remember, and the audit is worthless if it only looks at the UI. Ask the user which of these they can give you, and work with whatever arrives:

- UI strings: navigation, buttons, empty states, settings pages
- Object and entity names, in the UI and in the data model
- Status and state values, including the ones that only appear in a dropdown filter
- Permission and role names
- API fields, endpoints, and enum values
- Analytics event names and properties
- Database columns and table names
- Docs, help center articles, and support macros
- Marketing site and sales material
- What customers actually say, from tickets, calls, or reviews

That last one is the tiebreaker later, so ask for it even when the user thinks it is unavailable. A handful of support tickets is enough.

When the user has already volunteered a set of terms, which is how these requests usually arrive, audit what they gave you now and put the requests for the gaps at the end. Do not open with a list of ten questions to someone who just handed you their mess and asked where to start.

If the user offers only a short list of the terms that bother them, start there, but say what you did not see. An audit of ten terms out of two hundred is a spot check, and it should be labeled as one.

## Step 2: Sort every term by what kind of thing it names

Mixing these up is the root of most naming messes. Sort into:

- Objects: the nouns the user creates or owns, such as a project, invoice, or workspace
- States: what an object currently is, such as draft, active, expired
- Actions: what someone does, such as archive, publish, invite
- Roles and permissions: who someone is and what they may do
- Groupings: categories, tags, folders, labels, collections
- System concepts: things that exist only because of how the software is built

Watch for one term doing two jobs. When "archive" is a verb, a state, and a place, the confusion is structural rather than cosmetic, and no amount of copy editing fixes it.

## Step 3: Run the four checks

Go through the inventory looking for exactly these, and record each hit with where it appears.

1. Split terms. One concept with several names. "Organization" in the UI, `account_id` in the API, "workspace" in the docs, "company" in sales decks. Record every variant and where it lives.
2. Collisions. One name covering several concepts. "Owner" meaning the billing contact in one screen and the record creator in another. These are more dangerous than split terms, because both sides look correct in isolation and users only find the conflict at the worst moment.
3. Pattern breaks. Names that do not follow the shape of their neighbors. A settings page of "Notifications, Billing, Manage team, Security" has one verb phrase among three nouns. Same for tense, plurality, and casing.
Say which of these you could not run. Pattern breaks in particular live in settings pages, button labels, and empty states, so an inventory of an object hierarchy and two enums cannot support that check. Naming the check you could not run is more useful than quietly skipping it.

4. Wrong-level terms. Names that describe the implementation rather than what the user is doing, or names borrowed from an internal project that leaked into production. If a term only makes sense to someone who has read the code, note it.

## Step 4: Give status sets their own pass

Status values fail in specific ways, so check each set separately against these:

- One dimension per set. "Draft, Published, Archived, Featured" is broken, because featured is a separate axis and an item can be both published and featured. Split it into two fields.
- Mutually exclusive and exhaustive. Every object must be in exactly one value, including the awkward edge cases. Ask where a half-finished, expired, refunded, or deleted item sits.
- No two values a user cannot tell apart. "Inactive" and "Disabled" and "Paused" in one product means somebody will pick wrong.
- The state is named for what it is, not for how it got there.
- A state shares a root with the action that produces it. When the button says Pause, the state is Paused. When the two differ, every user and every support rep has to learn a mapping for no benefit.
- Terminal states are recognizable as terminal.

Show status sets back as a small table with the value, what it means, what puts an object into it, and what it can move to next. Undefined transitions surface here reliably, and the blanks are the finding. Leave them blank rather than filling them with a plausible guess, since an empty cell is what proves the set was never fully defined, and a helpful guess hides exactly the problem you were asked to find.

When the user says they are no longer sure what one of their own terms means, treat that as the most useful sentence in the request. Do not define it for them. Ask the three or four questions that discriminate between the possibilities, such as whether the thing can be edited, whether it appears in the normal list, whether it can be converted back, and what happens to it at the end of its life. The answers usually reveal whether it is a state, a separate kind of object, or a flag that grew behavior.

## Step 5: Propose the canonical set

Two deliverables.

First, the rules the names follow, written so someone else can apply them to a term you never saw. Cover the grammar of objects, actions, and states, casing, plurality, and whether a term is user-facing or internal. Keep it to a handful of rules. A long style guide goes unread.

Second, the term table:

| Concept | Canonical term | Where it appears now | Aliases to retire | Notes |
|---|---|---|---|---|

Choosing the canonical term, in order:

1. What customers already call it, when they have a clear word for it. Fighting your users' vocabulary is an expensive way to be right.
2. Whichever existing variant is most used and hardest to change, since the cheapest rename is the one you don't do.
3. The plainest word that a new user would guess. Ordinary language beats clever, and clever names age badly and translate worse.

When the term is new and there is no incumbent variant, rule 2 does not apply. Fall back to the word customers would guess, the word the rest of the industry uses for the same concept, since integrators and new hires arrive already knowing it, and the pattern of the existing set, including word count and casing.

Say when you are not confident, and name the two candidates rather than picking silently.

## Step 6: Price the migration

Never hand back a rename list without this, because the cost is what decides whether any of it happens. Sort every proposed change into:

- Cheap and safe: UI copy, docs, help center, marketing. Change now.
- Moderate: URLs and slugs, which need redirects; email templates; saved views and filters; support macros.
- Expensive or breaking: public API fields and enum values, webhook payloads, database columns, SDK method names. These need versioning, a deprecation window, and customer notice.
- Needs a backfill: any split or merge of a field, where every existing row has to be assigned a new value by a rule somebody writes. Design that rule as part of the proposal, because it is where the ambiguity finally gets resolved, and skipping it is how a clean new taxonomy arrives full of rows nobody could classify.
- Destroys history: analytics event names, metric definitions, and anything a dashboard or a data warehouse query depends on. Renaming an event splits its history in two, and someone's quarterly report breaks silently. Where a rename is worth it, plan to emit both names for a period and to annotate the change where the data is read.

Order the findings themselves by what they cost, not by the order you happened to check them. A collision usually outranks a split term, because a split term is annoying while a collision is producing wrong decisions in support and in the data. Lead with the one doing damage.

Then recommend a sequence, starting with the cheap changes that remove the most confusion, and be explicit that some expensive renames may not be worth making at all. An internal name that is wrong but stable and invisible to users is often a rename to skip. Say so when that is your read.

## Step 7: Say how this stays fixed

A one-time cleanup regresses within two quarters. Close with the small set of things that keep it from drifting: where the glossary lives, who reviews new user-facing terms, and which check belongs in a design or code review. Keep it short and realistic for the team's size. A two-person team will not run a terminology council.

## Common failure modes to avoid

- Fixing a collision by adding a qualifier to both sides. "Account Owner" and "Record Owner" is a repair, not a solution, and it is usually a sign that two different concepts need two different words.
- Treating an analytics event rename as free. It quietly destroys trend data, and nobody notices until a quarterly review.
- Renaming for elegance without pricing it. A tidy set of names that requires breaking an API for every customer is not an improvement.
- Ignoring what customers call it and standardizing on the internal word, which leaves the support team translating forever.
- Renaming something with an established external identity, such as a term customers have written into their own scripts and runbooks, without saying what it breaks for them.
- Clever names. They lose to plain ones in search, in support calls, and in translation.

## If the user only wants one thing named

Answer the question, and keep the answer proportionate to it. Check the new name against the existing set for a collision first, since a single name that conflicts with an existing status value or role is worse than the original problem. When the name is a state, run the step 4 checks on the set it is joining as well, because the common mistake is not the name itself but the extra value that quietly adds a second dimension to the set. Then check step 6 for anything the addition touches, particularly analytics events and any metric that filters on the old set.

Everything else in this file stays out of the reply.
