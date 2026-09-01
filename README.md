# Sam's Universe

Claude skills for design and product work, and for writing children's books. Each one is a self-contained folder that teaches Claude a specific workflow it would otherwise do generically, or skip.

These are the skills I wanted and couldn't find, built for the parts of a job where a generic answer is worse than no answer: writing up a project so it shows judgment rather than process, reading a round of stakeholder interviews without smoothing the disagreements away, shipping behind a flag without discovering at 3am that the dashboards were green the whole time, and cleaning up product terminology without breaking every customer's integration.

The picture book skills come from the same instinct. A story for a four-year-old has real structural rules, such as word counts, page-turn beats, and how much work the illustration does instead of the text, and a model that doesn't know them writes something that reads fine on screen and falls apart out loud.

## Install

Copy the skill folder you want into your skills directory:

- Claude.ai: `/mnt/skills/user/`
- Claude Code and Cowork: the equivalent path for your setup

Keep the folder name as it is. The `name` field inside `SKILL.md` has to match the folder it sits in, and renaming either one breaks the skill.

You don't invoke a skill by hand. Claude loads it when your request matches its description, which is why the descriptions here list so many trigger phrases: Claude under-triggers skills far more often than it over-triggers them.

## Design and product

| Skill | Status | What it does |
|---|---|---|
| [portfolio-case-study-outline](skills/portfolio-case-study-outline) | tested | Structures one project write-up: the sections, the word budget, the visual beside each, and the captions |
| [stakeholder-interview-synthesizer](skills/stakeholder-interview-synthesizer) | tested | Turns rough interview notes into themes tied to decisions, with the disagreements named rather than averaged away |
| [feature-flag-rollout-planner](skills/feature-flag-rollout-planner) | tested | Ramp schedule, guardrail metrics, kill criteria written as numbers, and the date the flag gets deleted |
| [naming-and-taxonomy-checker](skills/naming-and-taxonomy-checker) | tested | Audits product terminology for collisions and split terms, then prices the migration by what each rename costs |

## Children's books

| Skill | Status | What it does |
|---|---|---|
| [story-arc-for-young-readers](skills/story-arc-for-young-readers) | tested | Structures a story into an age-appropriate arc before any prose is drafted, for picture books and chapter books |
| [picture-book-writer](skills/picture-book-writer) | tested | Drafts age-banded manuscript text with the rhythm and repetition picture books rely on |
| [character-bible-builder](skills/character-bible-builder) | tested | Locks a character or a small cast, for one book or across a series |
| [childrens-book-illustration-brief](skills/childrens-book-illustration-brief) | tested | Turns a manuscript into a page-by-page illustration and art-direction brief |
| [read-aloud-pacing-checker](skills/read-aloud-pacing-checker) | tested | Reviews a manuscript for read-aloud rhythm, page-turn pacing, and metre in verse |

They're built to hand off to each other: outline the arc first, draft against it, then check the pacing.

## Writing and speaking

| Skill | Status | What it does |
|---|---|---|
| [eulogy-and-toast-writer](skills/eulogy-and-toast-writer) | tested | Eulogies, toasts, and leaving speeches built from specific things that happened, sized to the slot, in the speaker's own vocabulary |
| [long-form-editor-for-voice](skills/long-form-editor-for-voice) | tested | Profiles a writer's voice from countable features in their real work, then edits against that rather than toward generic good prose |
| [cold-outreach-personalizer](skills/cold-outreach-personalizer) | tested | Makes the specific detail the reason the message exists rather than decoration on it, and never invents a fact about a real person to make an opening work |

## Working with other people

| Skill | Status | What it does |
|---|---|---|
| [disagreement-de-escalator](skills/disagreement-de-escalator) | tested | Lowers the temperature in a heated thread without giving up the position: concedes what is genuinely true, strips the escalators, and aims at an outcome rather than at winning |
| [decision-journal](skills/decision-journal) | tested | Records a decision and a falsifiable prediction while it is still open, then scores the prediction later and separates a bad decision from bad luck |

## Money and admin

| Skill | Status | What it does |
|---|---|---|
| [tax-document-checklist-by-situation](skills/tax-document-checklist-by-situation) | tested | What to gather, who issues it, and which records stop being obtainable — derived from actual income sources. Organisation only, never rates or treatment |
| [freelance-invoice-and-follow-up](skills/freelance-invoice-and-follow-up) | tested | An invoice with no excuse left in it, and a chase sequence that runs on dates rather than on nerve — including where chasing stops |
| [contract-negotiation-prep](skills/contract-negotiation-prep) | tested | The walk-away by arithmetic, the levers that are not the rate, the order concessions get traded in, and the sentences to say when the number is questioned |

## Learning

| Skill | Status | What it does |
|---|---|---|
| [book-notes-synthesizer](skills/book-notes-synthesizer) | tested | The two or three ideas from a book actually worth keeping, sorted by whether they confirm, contradict, or name something — and what did not survive the test |
| [explain-like-im-at-my-level](skills/explain-like-im-at-my-level) | tested | Calibrates to what the person already knows and to what they need the explanation *for*, which sets the depth more than their level does |
| [spaced-repetition-deck-builder](skills/spaced-repetition-deck-builder) | tested | Decides what should not be a card, writes the ones that survive being asked in four months, and states the daily review load before anyone signs up to it |

## Life and household

| Skill | Status | What it does |
|---|---|---|
| [home-project-scoper](skills/home-project-scoper) | tested | Turns a vague renovation into decisions ordered by when they are actually needed, a sequence with the drying time visible, and the things people discover halfway through |
| [photo-culling-assistant](skills/photo-culling-assistant) | tested | Fixes what the set is for before anything is judged, then groups before ranking — which is what stops a cull producing eleven versions of one moment |
| [recipe-adapter](skills/recipe-adapter) | tested | Works out what each ingredient is actually doing before swapping it, and says when the recipe will not survive the change at all |
| [habit-relapse-recovery-planner](skills/habit-relapse-recovery-planner) | tested | The restart plan for the moment right after a habit breaks: what actually broke it, how small week one has to be, and the minimum version that still counts |
| [gift-idea-tracker](skills/gift-idea-tracker) | tested | Captures the hints people drop in their own words, with what is actually stopping them, and turns the record into one recommendation rather than five |
| [travel-packing-by-trip-type](skills/travel-packing-by-trip-type) | tested | Builds the list from the trip's activity blocks, the real forecast, the container and the wash cycle, and audits an existing list for what is missing before cutting anything |
| [subscription-audit](skills/subscription-audit) | tested | Turns recurring charges into a dated decision per line, with the cancellation method attached and the export done before anything is switched off |

Status key: `idea` not written, `draft` written but untested, `tested` run against real prompts by a fresh agent, `stable` used repeatedly over time.

## What "tested" means here

A skill is only marked `tested` once a fresh agent has read the `SKILL.md` file and nothing else, answered a realistic prompt with it, and reported back on what the file left ambiguous.

Reading a skill back to yourself doesn't count. You know what you meant, so you fill the gaps without noticing they're gaps. Every skill here failed something on its first round, and the failures were the useful part. The rollout planner never said that a service returning plausible but wrong values keeps every error-rate and latency dashboard green, which meant a rollout following it would have watched the wrong metrics while charging customers incorrectly. That fix only exists because someone who hadn't written the file tried to use it.

There's a second round that matters just as much: running the skill on a scenario it wasn't tuned for. Re-testing the original prompt shows a fix landed, but a skill patched from one report will recite that report back convincingly. The five children's-book skills each passed their re-test and then failed a generalization round on something real, including a chapter-book word budget that would have told an author to halve a perfectly normal manuscript.

**What each skill has actually been through**, since `tested` is otherwise doing a lot of unexamined work:

- The five children's-book skills have had three rounds: two prompts each, a re-test after fixes, and a generalization round on a different format or age band, plus fixes after that.
- The four design and product skills have had two rounds: two prompts each and a re-test. They have not had a generalization round, so their coverage outside the cases they were tested on is less established.
- Everything after those nine has had the full three rounds: two prompts, a re-test, and a generalization round in a domain the skill was not written against.

## Structure

Every skill is its own top-level folder under `skills/`, with no nesting by category:

```
skills/
├── portfolio-case-study-outline/
│   └── SKILL.md
├── picture-book-writer/
│   └── SKILL.md
└── ...
```

A folder can also hold `scripts/`, `references/`, and `assets/` as it grows.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT. See [LICENSE](LICENSE).
