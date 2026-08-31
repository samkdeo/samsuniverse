---
name: subscription-audit
description: Works through someone's recurring charges, finds the ones that are duplicated, forgotten, bundled elsewhere, or quietly repriced, and turns that into a cancel, keep, downgrade, or renegotiate decision for each one with the right date and method attached. Use this skill when someone says they are paying for too many things, wants to cut their subscriptions, asks "what am I actually paying for", "help me cancel some of this", "where is my money going", "I want to trim my outgoings", mentions a free trial they forgot about, or notices a charge they do not recognise. Use it too when they ask about one specific subscription and whether to keep it. It is not budgeting or financial advice and it never handles card numbers, logins, or full account details.
---

# Subscription Audit

Turns a set of recurring charges into a decision per line: cancel, downgrade, pause, renegotiate, or keep and stop thinking about it. The decisions are the easy part. The two things that actually make this work are getting a complete list rather than a remembered one, and getting each cancellation to happen on the right date by the right method, because a decision that does not survive contact with a retention flow saves nothing.

It is not budgeting, debt advice, or a financial plan. If the underlying question is that the money does not add up, say so and treat the subscriptions as one input rather than the answer.

## Never handle the credentials

Do not ask for, and do not accept, card numbers, full account numbers, logins, passwords, or one-time codes. If a user pastes a statement, work from the merchant names and amounts, and tell them plainly that they should redact anything else before pasting it anywhere, here included. There is no step in this skill that needs a card number, and any version of this that asks for one is doing something else.

## You cannot do the cancelling

Users will ask you to cancel something, and it is worth saying in the first line that you cannot: it needs their login, and this skill never touches credentials. What you can do is tell them exactly what to cancel, in what order, on what date, and by which route, which is the part they were actually stuck on. Say it once, plainly, and move straight to that rather than dwelling on it.

## Route an unrecognised charge here first, before anything else

A charge the user cannot identify is not a keep-or-cancel question and must not be treated as one, whatever else the message asks for. There is nothing to reason about until it has a name, and the failure mode is specific: an agent that guesses a plausible merchant lets an unauthorised charge survive the audit with a verdict written next to it.

So when the user says they do not recognise something, do the identification and nothing else:

- Search the exact merchant string, including any processor prefix. Many descriptors are the payment processor's name rather than the product's, which is the usual reason a legitimate charge looks unfamiliar.
- Search every email address they have ever used for the merchant name, and for anything that company may have acquired or been renamed from. Acquisitions silently rename a charge, and a service someone signed up to years ago can bill under a name they have never seen. Offer any specific acquisition as something to check rather than as a fact, since these are exactly the details a model gets confidently wrong, and a wrong one sends the user searching for the wrong thing.
- Check the amount and date against the app store and payment account subscription lists, where charges appear under names that never reach a bank statement.
- Look back twelve months for earlier instances, which say how long it has been running and whether it is annual.

If it is still unidentified after that, it goes to the bank as a query. Say that plainly rather than leaving it on the list with a guess attached.

Once it does have a name, the rest of the skill applies, and the load-bearing and annual-already-paid checks in step 4 usually matter immediately, because an unrecognised charge is disproportionately often an annual renewal of something that quietly holds something else up.

## The escape hatch

If the user asks about one subscription they can identify, answer about that one. Get what they actually use it for, what it costs now versus what it cost when they signed up, and what they lose by leaving, and give them a straight answer. Do not run a full audit on someone who asked a single question.

The full procedure is for "I'm paying for too much and I don't know what".

## Step 1: Get a real list, from the sources, not from memory

This is the step that decides whether the audit is worth doing, and it is the one users want to skip. The subscriptions someone can recall are, almost by definition, the ones they are aware of paying for. The money is in the others.

When a user arrives having already written a list from memory, which is the common case, do not send them away to redo it. Audit what they brought — it is real work and refusing it wastes it — and run the sourcing sweep alongside as the next action rather than as a gate. Say what the remembered list is structurally likely to be missing, which is not a general caution but a specific prediction you can make from what is on it: annual charges, anything billed through a platform under an unrecognisable name, and the categories implied by their life that are conspicuously absent from the list. Someone whose work or hobbies obviously require a class of paid service, with none of that class on the list, has not searched everywhere they pay from.

Ask them to pull the full list from the places charges actually originate, rather than from what comes to mind. There are more of these than people expect, and missing one hides an entire category:

- The card statement, and every card, including the one barely used
- The bank's own list of direct debits and standing orders, which is separate from card payments and holds different things
- The app store subscription pages on each platform they use, which hold subscriptions that never appear under a recognisable merchant name
- The online payment accounts, which hide recurring payments behind a single merchant name
- Anything charged to a partner's or a shared account
- Anything billed annually, which will not appear at all in a month of statements

Then tell them to search **twelve months**, not one. This is the single highest-value instruction in the skill. Annual renewals are invisible in a monthly scan and they are where the largest forgotten charges live, because a yearly charge is both the biggest and the easiest to overlook. A one-month scan systematically finds the small stuff and misses the expensive stuff.

Where a charge cannot be identified from the merchant name, which is common, say so rather than guessing, and describe how to trace it: search the exact string, check the amount and date against the app store lists, and if it remains unknown, treat it as a live question for the bank rather than as a subscription to reason about. An unrecognised recurring charge is occasionally fraud, and guessing at a plausible merchant is how it stays undetected.

## Step 2: Normalise before comparing

Put everything on the same footing before judging anything, because the list will not arrive that way.

- Convert every price to an annual figure. This is what makes the decisions obvious, and it is the step people skip. Small monthly amounts are designed to be individually unobjectionable, and the annual total is the number that changes minds.
- Note the billing period and the **next renewal date** for each. This determines the whole plan in step 5.
- Note what it costs now against what it cost when they signed up, where they know. Price creep on an existing subscription is the most common way a reasonable set of subscriptions becomes an unreasonable one without anyone deciding anything.
- Note who else uses it. A charge on the user's card is not necessarily their subscription, and cancelling something a household member depends on is the fastest way to lose their goodwill for the whole exercise.

## Step 3: Judge each line on use, not intention

The question is not whether it seemed worth it. Ask when they last used it, and prefer evidence over recall: the app's own history, the last login, the number of items downloaded or episodes watched. People are consistently generous about their own usage, and the answer "I use it sometimes" is almost always an intention rather than a record.

Then sort into the patterns that actually recur, because naming the pattern decides the action:

- **The converted trial.** Signed up for one thing, never cancelled. Pure waste, cancel immediately, and check the twelve months for how long it has been running.
- **The duplicate.** Two or more services doing substantially the same job. Very common in media, storage, and anything with a free tier that quietly filled up. The decision is which one, not whether.
- **The already-bundled.** Something paid for separately that is included in something else they already have: a phone plan, a broadband package, a membership, a workplace benefit, an existing software licence. This is the highest-value category to look for and the least likely to be noticed, because the bundled version is invisible by design.
- **The aspirational.** Bought for the person they intended to become. The gym in February, the course, the language app, the fitness platform. Treat it with a straight face rather than a joke, and set the test as a date: if it has been unused for a stretch, the subscription is not what is missing.
- **The seasonal.** Genuinely used, but only part of the year. This is a pause or a re-subscribe candidate rather than a cancel, and re-subscribing later usually costs less than paying through the dead months.
- **The load-bearing.** It quietly holds something up: a domain, an email address, a backup, a licence that keeps files openable, a phone number. Cancelling these has consequences well beyond the fee, and they should be identified explicitly so they are not swept up in an enthusiastic cull.
- **The genuinely worth it.** Say so, and say to stop revisiting it. An audit that questions everything every year is its own tax on attention.

## Step 4: Before cancelling, ask what cancelling actually costs

Several of these are not obvious and each one turns a good cancellation into a bad one.

- **A price that cannot be got back.** Legacy and grandfathered rates are the big one. Someone on an old plan at an old price who cancels and later returns pays today's price, and the difference can exceed everything the cancellation saves. Where a subscription is unusually cheap for what it is, that is the tell, and it argues for downgrading or pausing rather than cancelling.
- **Data.** Photos, files, documents, exported history, saved work. Get the data out first, verify it opened somewhere else, and only then cancel. This ordering is not optional and it is the most expensive mistake available in this whole exercise.
- **Purchased content that lives inside the subscription.** Some things bought outright stay accessible after cancelling and some do not.
- **A contract, a minimum term, or a notice period.** Common with gyms, telecoms, and anything sold as a plan rather than a service. Cancelling in the wrong window costs the remaining term.
- **A bundle discount.** Cancelling one part of a bundle sometimes reprices the rest, and the saving is smaller than it looks or negative.
- **Somebody else's access.** A family plan, a shared login, a service someone's work or study depends on.
- **The annual already paid.** Cancelling the day after an annual renewal wastes almost the whole year. Cancel the auto-renewal, keep the access until it lapses, and set the reminder.

## Step 4b: Check whether they are on the wrong price before deciding to cancel

Ask this of every line before any cancellation is decided, because it frequently delivers more than the cancellations do and costs the user nothing they were using.

Many services have a rate the user qualifies for and is not on: a charity or education rate, a student rate, a household or family plan replacing several individual ones, a loyalty or long-tenure rate, a regional price, or simply the annual price where they are paying monthly. Monthly billing carries a substantial premium on most subscriptions, so anything genuinely used and being kept should be checked for an annual switch as a matter of routine — it is a saving that changes nothing about how they use it.

Where an organisation is involved, this is usually the single biggest lever, because a stack assembled quickly by one person tends to sit on commercial rates that nobody has revisited. Run this pass before the cancellation pass, so the target is partly met without removing a tool anyone depends on.

## Step 4c: When the subscriptions are not the user's own

A business, a charity, a shared household, or an inherited set of accounts changes the procedure in ways the household version does not cover.

- **Access is a blocker, not just a cost.** The account may be registered to someone who has left, and the login, the billing contact, and the cancel button all sit with them. Identify these first, because recovering account ownership can take days and sometimes needs the original holder to cooperate, which gets harder with time. A charge the organisation cannot see or cancel is a finding in its own right, separate from what it costs.
- **Some charges never appear on the organisation's statements at all.** Anything on a personal card that gets reimbursed appears as an expense claim, so the expense history has to be searched alongside the bank feed. Auditing only the bank feed audits the wrong money.
- **Seats are the fastest reversible saving.** Per-user tools accumulate licences for people who have left or who never arrived. Check the assigned seat count against the actual headcount on every per-user line.
- **Ask what people actually use, separately from what is paid for.** The two lists will not match, and the gap is the answer.
- **Say who has the authority to cancel each line**, since deciding and being permitted to act are different things here.

## Step 5: Turn the decisions into dated actions with a method

A list of things to cancel is not an outcome. The gap between deciding and saving is where audits die, so make each line an action with a date and a mechanism.

For each cancellation, say **when** and **how**.

The when is governed by the renewal date and the term, not by today. Cancelling immediately is right for a monthly service and often wrong for an annual one, where the move is to turn off auto-renewal now and let the paid period run out. Where there is a notice period, the date is set by the notice period counted back from the renewal.

The how matters because cancellation friction is deliberate. Some things cancel in two taps; some are only cancellable by phone, by post, or through a retention conversation; some are cancelled through the platform that bills them rather than through the service itself, which is where people get stuck, since cancelling in the app does nothing when the billing sits with the store. Say which applies, and where a phone call is required, say what to have ready and that the retention offer will come.

On the retention offer: it is worth deciding in advance whether an offer would change the decision. For something genuinely used but overpriced, a retention discount is a real outcome and the call is worth making for that reason alone. For something unused, a discount is a cheaper version of a thing they do not want, and the answer is no. Deciding this before the call is what stops the call deciding it.

Then: turn off the payment method as a backstop only, never as the cancellation. Blocking a card leaves the contract alive, and for anything with a term it can leave an unpaid balance in collections rather than a cancelled service.

Finally, put a reminder on each dated action, and one further out for the renewals that were kept. The subscription that renews in eight months at a higher price needs a note now, because the next audit will otherwise start from the same blank page.

## Step 6: Deliver

Give back a table, one row per subscription: what it is, annual cost, last used, the verdict, the date, and the method. Then three lines underneath:

1. The total being cancelled, given as two numbers rather than one, because they are not the same and only one of them may be what the user is measured against. **Cash saved before a given date** is what actually leaves the account less; **annualised run-rate removed** is how much smaller the commitment is going forward. Turning off auto-renewal on something already paid for a year removes run-rate and saves no cash this year. Where the user has a target with a deadline on it, ask which one it means, because a plan optimised for the wrong one can be entirely correct and still miss.
2. The things deliberately kept, so the decision is recorded and does not get re-litigated next month.
3. Anything that could not be identified, flagged as a question for the bank rather than left as a guess.

Where a cancellation depends on getting data out first, say that explicitly in the row rather than in a footnote, because the row is what the user will work from.

## Common failure modes to avoid

- Auditing from memory, which surfaces the subscriptions the user was already thinking about and none of the ones costing them.
- Scanning one month of statements, so every annual renewal is invisible and the expensive forgotten charges survive.
- Cancelling before exporting the data, and finding out afterwards which files were only ever in that account.
- Cancelling a grandfathered price to save a small monthly amount, and paying more than that to come back.
- Treating an unrecognised charge as a subscription to reason about rather than as something to identify, when it is occasionally fraud.
- Producing a list of things to cancel with no dates and no methods, so nothing gets cancelled.
- Cancelling the day after an annual renewal instead of turning off auto-renewal and letting the term run.
- Cancelling in the app when the billing sits with the platform, so the charge continues.
- Blocking the card and treating that as a cancellation.
- Cancelling something another person in the household relies on without asking.
- Answering "should I keep this" about a charge nobody has identified yet.
- Sending a user away to redo their list before touching the one they brought.
- Reporting one savings figure when the user is working to a deadline, so a plan full of auto-renewal changes is presented as cash that will not arrive this year.
- Deciding to cancel something before checking whether the user simply qualifies for a cheaper rate on it.
- Treating somebody else's access as a reason to be careful, when on an inherited account it is the thing that stops the cancellation happening at all.
- Asking for a card number or a login. Nothing here requires one.
