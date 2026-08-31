---
name: cold-outreach-personalizer
description: Turns a cold email, LinkedIn message, or DM into one that could only have been sent to this specific person, by finding the detail that explains why you are writing to them rather than to anyone else and making it the reason for the message rather than decoration on it. Use this skill when someone is writing to a stranger to sell, pitch, recruit, ask for advice, ask for an introduction, pitch a journalist, or approach an investor, and when they say "make this less generic", "personalise this", "why is nobody replying", "I've sent 200 of these", "help me write to X at Y", or hand over a template to improve. It never invents facts about a real person or company, and it does not write bulk sequences whose personalisation is a merge field.
---

# Cold Outreach Personalizer

Produces one message to one named person, where the specific thing about them is the reason the message exists. The common failure is not a lack of research but a lack of connection between the research and the ask: a genuinely specific first line bolted onto a pitch that would have gone to anyone is still a template, and the recipient can feel the join.

The test the whole skill runs on: **could this message be sent to someone else with the name and company swapped?** If yes, it is not personalised, however much detail is in the first paragraph. The stronger version of the test is better still: does the specific detail explain why you are writing to *this* person rather than to their most obvious competitor?

It does not write bulk sequences. If the request is for a template with variables, say plainly that the approach here does not survive being merge-fielded, and offer either one real message or a set built for a short list.

**The short list is its own case**, and it is common: too many recipients to write each from scratch, few enough that a single letter to all of them is the reason nobody replied. Do not resolve it by producing one better letter. Segment first, by which argument actually applies to each recipient rather than by size or sector, since the argument is what changes the message. Then write one message per segment, and personalise only the opening line per recipient. That opening line is the entire personalisation budget and it is enough, provided it is true and specific.

Segmenting usually surfaces a third group the user had not separated: the recipients where somebody already has a connection. Those should not be cold messages at all, and saying so removes them from the pile rather than improving them.

Where a segment has no honest version of the main argument, say so and write the message that admits it. A message that opens by conceding the obvious objection, and then makes the smaller true case, outperforms one that asserts a benefit the recipient can see is not there.

## Never invent the research

This is the hardest rule and the one that matters most, because getting it wrong is worse than sending nothing.

Do not state a fact about a real person or a real company unless the user supplied it or you have actually retrieved it. Not a talk they gave, not a post they wrote, not a funding round, not a product launch, not a headcount, not a job opening. A confident, plausible, wrong detail is the single most damaging thing this skill can produce: it does not read as a near miss, it reads as a bot, and it costs the sender the contact permanently.

So when you do not have real information, do not fill the gap. Do one of these instead:

- Write the message with the specific slot clearly marked, saying exactly what kind of detail belongs there and where the user can find it. A named blank the user fills in ten minutes beats a fabricated sentence.
- Tell the user what to go and look at, in priority order, and offer to write it properly once they paste what they find.
- Where browsing is genuinely available, use it, and cite what you found so the user can check it before sending.
- Where the user is themselves in a position to generate the detail rather than look it up, set them that task. Someone who can sign up for the recipient's product, read their documentation, go through their onboarding, or use the thing being sold can produce first-hand observation that no research would have found, and it is the strongest hook in step 2. This is more useful than any amount of searching on their behalf.

Never present an assumed detail as though it were retrieved, and never hedge one into the draft, since "I saw you recently launched something" is both invented and obviously generic.

## When the user arrives with a template and a bad reply rate

This is one of the commonest entry points and it needs diagnosis before rewriting, because handing back a better template leaves them running the same machine.

Diagnose in this order:

1. **Run the swap test on their own text.** Strip the merge fields and read what is left. If the meaning is unchanged, say so plainly, because it is the whole finding: the personalisation is decoration and the recipients can feel the join.
2. **Rank the fields they are merging.** Almost always they are pulling from the weakest tier in step 2, because those are the fields a database has. A merge field is by definition a fact that was scraped rather than read, which is the thing the recipient is actually detecting.
3. **Find the inference presented as insight.** Templates habitually tell the recipient something about their own company, deduced from a public signal. The recipient knows the real reason and the sender has a good chance of being wrong, which spends credibility for nothing.
4. **Check the claims.** Any figure with "up to" in front of it is a ceiling, so it is compatible with almost nothing, and buyers have learned to read it as the single best case ever recorded. An unfalsifiable number does not persuade. Ask what the median is and what the sample was, and use those or drop the claim.

Then name the trade explicitly rather than pretending it away. The approach in this skill does not survive being merge-fielded, so a rebuilt template blasted at the same volume returns the same result. The honest arithmetic is that a much smaller number of messages to people who were actually looked at beats a large number of scraped ones, and it usually costs less total time, because the time currently goes into send volume rather than into reading. Say the numbers and let the user choose.

Where they want to keep some volume, the workable middle is a hook drawn from something specific but reliably findable in a few minutes per prospect — the wording of their own job posting, their public documentation, their stack — rather than from a database column. Say which tier that is and what it gives up.

## Step 1: Establish the four things the message hangs on

- **Who, exactly.** A named person with a role, not a company. If the user only has a company, the first job is choosing the right person, and writing to a level too senior is a common reason for silence rather than a bold move.
- **What the ask actually is**, stated as the specific action the recipient would take. "A chat" is not an ask. Booking twenty minutes, answering one question, forwarding to a colleague, and taking a trial are four different asks with four different hit rates.
- **What the sender has that is genuinely relevant to this recipient.** Not the general pitch. The part of it that touches this person's actual situation.
- **Why now.** The best cold messages have a reason for arriving today rather than at any point in the previous two years. Absent a real trigger, say so rather than manufacturing urgency, which recipients read instantly.

## Step 2: Find the detail worth using, and rank what you have

Not all specifics are equal, and the ones easiest to find are the ones every other sender is also using. Rank candidates by how much work they did to find it and how directly it bears on the ask:

- **Strongest: something the person themselves said or made**, and the more considered the better. A talk, a written piece, a public answer, a decision they explained, an open-source contribution, a comment they left. This is strong because it is about them rather than about their employer, and because engaging with an argument someone made is the one form of attention that cannot be automated.
- **Strong: something specific about how the company actually works** that the sender noticed by using the product, reading the documentation, going through the signup, or being a customer. Direct observation beats anything from a press release, and it proves effort in a way nothing else does.
- **Medium: a company event with a clear consequence for this person's job.** A launch, a market entry, a reorganisation, a role they are hiring for. Usable, but only if the message connects it to the ask rather than merely noting it.
- **Weak: funding rounds, awards, anniversaries, and anything else on a public feed.** Every sender uses these, the recipient received eleven of them that week, and mentioning one signals that the sender searched rather than that they looked.
- **Weakest, and often negative: personal details harvested from social media**, and any compliment on appearance, family, or lifestyle. These read as surveillance rather than as attention.

A shared connection is a special case. It is genuinely strong when the connection actually knows the sender and has agreed to be named, and it is actively damaging when the connection is a second-degree link the sender has never spoken to. If the user wants to use a name, ask whether that person has agreed. The version that works is usually to ask the connection for the introduction instead, which is a different and better message.

Then check the detail is still current. A reference to something from years ago, or to a role the person has since left, does more damage than no specificity at all, because it says the sender did the research once and never looked again.

## Step 3: Make the specific thing load-bearing

This is the step that separates this skill from adding a compliment.

The detail must do one of these jobs, not sit decoratively above the pitch:

- **It is the reason the ask makes sense.** What they said or built tells you they have the specific problem, or the specific interest, that the sender is writing about.
- **It is a genuine disagreement or addition.** They made an argument and the sender has something to add to it, or evidence against it. This is the highest-response-rate form of cold outreach in existence and it is almost never used, because it feels riskier than a compliment. Done respectfully it is far more flattering than praise, because it treats the person as someone worth arguing with.
- **It qualifies them out of the generic pitch.** The sender noticed something specific enough that the standard pitch does not apply, and says so.

If the detail cannot do one of those three jobs, it is decoration, and the honest move is to cut it and write a shorter, plainer message. A brief message that says who the sender is, what they want, and why it might be relevant, with no personalisation at all, outperforms a message with a bolted-on compliment, because the compliment is the part that signals a template.

Never open with praise as the first line. "I loved your post" is the exact phrasing of every automated tool on the market, and it now functions as a signal that the message is automated even when it is sincere.

## Step 4: Write it

Constraints that hold across every kind of cold message:

- **Short enough to read without scrolling on a phone.** The recipient decides whether to reply in about the first two lines, and length itself is a signal: a long message from a stranger asks for more than it offers.
- **The first line is about them or about the reason for writing, never about the sender.** An opening that begins with the sender's name and company is the one most reliably deleted.
- **No throat-clearing.** Drop "I hope this finds you well", "I know you're busy", and any apology for the intrusion. They cost lines and add nothing.
- **State what the sender wants, explicitly, in one sentence.** Vagueness about the ask does not soften it; it just makes the recipient work out what is being asked before they can decline.
- **Make the ask small and concrete**, and proportionate to a relationship that does not exist yet. The smallest useful ask usually wins, and a question that can be answered in one line is a much better first step than a meeting.
- **Where the ask cannot be made smaller, make it exact.** Some asks are the whole point and cannot be shrunk into a question: money, sponsorship, a donation, a commitment with a number attached. Vagueness is the wrong response to that, because "any support would be appreciated" hands the recipient the job of setting the price and the usual answer to that job is no. Name the amount, name precisely what it pays for, name what the sender gives back, and name the date it is needed by. A specific ask is easier to decline and much easier to accept.
- **Give a real out.** A sentence that makes it easy and costless to say no raises reply rates rather than lowering them, and it should be genuine rather than a rhetorical device.
- **Choose the channel deliberately**, since it is part of the message. For a recipient who is physically nearby or runs a small local business, a letter handed over or a conversation in person outperforms email by a wide margin and gives the sender the recipient's actual name. For anyone whose inbox is their workplace, email to a named person is right. Never address a message to nobody: if the name cannot be found remotely and the recipient is reachable in person, going to ask for it is the research.
- **Write it in the sender's own register.** A message that does not sound like the person will not survive the reply.
- **No fake familiarity.** Not "just circling back" on a first message, not a subject line implying a previous conversation, not a false reply thread. These get an open and cost the trust in the same second.
- **The subject line describes the content**, plainly and in a few words. Curiosity-gap subject lines get opened and resented.

## Step 5: Adjust for what kind of outreach this is

The norms differ enough that a message correct in one register fails in another.

- **Sales.** The recipient gets many of these daily and is skilled at spotting them. The specific observation about their situation is the whole message, and the ask should usually be a question rather than a demo.
- **Recruiting.** Say the role, the level, and the compensation range if it can be said. Vagueness about money is the main reason good candidates do not reply. Say why this person specifically, and be honest if the answer is that their background matches.
- **Asking for advice or mentorship.** Ask a single specific question that can be answered in a reply. A request for a standing relationship or a recurring call from a stranger is a large ask and reads as one. Say what the sender has already tried, so the question is not one a search would have answered.
- **Pitching a journalist or writer.** Their inbox is the most hostile of any on this list. Lead with the story rather than the company, show that the sender has read what they cover, and be specific about what is actually new. A pitch that does not fit their beat is deleted regardless of quality.
- **Job hunting, including when there is no opening.** Very common and unlike the others, because the sender is asking to be remembered rather than to be answered. Say plainly that there is no role and that no reply is needed, since pretending otherwise is transparent and owning it is disarming. The credential is the mechanism rather than the outcome: a hiring manager reads past a headline number to how it was achieved, so lead with what was actually changed and why it worked. And where the sender can experience the recipient's product directly, that is the strongest hook available to them and almost nobody uses it.

- **Investors.** Norms are heavily convention-bound and a warm introduction genuinely outperforms cold contact, so the honest advice is often to spend the effort finding the introduction rather than perfecting the message.
- **Asking for an introduction.** Write it so the person can forward it without editing. That means a short, self-contained paragraph they can pass on, and an explicit statement that it is fine to say no, since the person is spending their own credibility.

## Step 6: Follow-up, and when to stop

Follow-ups are where good outreach turns into spam, so set the plan before sending.

A follow-up must add something rather than repeat the ask. New information, a different angle, a shorter version of the request. Re-sending the same message with "just bumping this" is what makes a sender easy to ignore.

Set a small number, decide it now, and then stop. Silence is an answer, and continuing past it converts a neutral non-response into an active negative impression. Say this plainly to a user who is planning a long sequence.

Respect the obvious things: an explicit no ends it, an unsubscribe request is honoured immediately and permanently, and the relevant rules on unsolicited commercial email are the sender's to check for their jurisdiction and their recipient's.

## Step 7: Deliver

Keep the delivery proportionate to the message. The deliverable is a message someone will read on a phone, and it should not arrive buried under several times its length in commentary. Lead with the message itself, keep the notes to what changes what the user does next, and drop any item below that has nothing to say rather than filling it in for completeness. When the user asked for a draft, the draft comes first.

Give back the message first, then the notes, in this priority order, stopping when there is nothing more that changes what the user does:

1. Anything left as a marked blank, and where to find it. This is what stands between them and sending.
2. The specificity test applied out loud: what in this message could not be sent to anyone else, and what would have to change if the recipient did.
3. Anything you could not verify and would not assert.
4. The follow-up plan, with the stopping point.
5. One alternative opening, only if the choice is genuinely close.

Items four and five are frequently droppable. Do not write all five out of a sense of completeness.

## Common failure modes to avoid

- Inventing a post, a talk, a launch, or a funding round because it would make the opening work. This is the worst outcome available here.
- A specific first line above a pitch that would have gone to anyone, which reads as a template with a wig on.
- Opening with praise, which is now the signature of automated tools.
- Using the easiest-to-find fact, which is the one every other sender used that week.
- Naming a mutual connection who has not agreed to it, or has never spoken to the sender.
- Referencing something out of date, which proves the research was done once and not checked.
- An ask so vague the recipient has to work out what is wanted before they can say no.
- A large ask from a stranger, when a one-line question would have started something.
- Fake reply threads, false "circling back", and curiosity-gap subject lines.
- A follow-up sequence that repeats the ask in different words until the recipient dislikes the sender.
- Rewriting a failing template into a better template, without saying that the method does not survive the volume it will be sent at.
- Telling recipients something about their own company that was inferred from a public signal, which they know better and which is often wrong.
- Headline claims with "up to" in front of them, which are ceilings and persuade nobody.
- Burying a short message under several times its length in commentary about the message.
- Answering a short-list request with one better letter, which is the thing that already failed.
- Shrinking an ask that cannot be shrunk, so a request for money arrives with no amount and no date and gets declined by default.
