# Sam's Universe

Claude skills for design and product work. Each one is a self-contained folder that teaches Claude a specific workflow it would otherwise do generically, or skip.

These are the skills I wanted and couldn't find, built for the parts of the job where a generic answer is worse than no answer: writing up a project so it shows judgment rather than process, reading a round of stakeholder interviews without smoothing the disagreements away, shipping behind a flag without discovering at 3am that the dashboards were green the whole time, and cleaning up product terminology without breaking every customer's integration.

## Install

Copy the skill folder you want into your skills directory:

- Claude.ai: `/mnt/skills/user/`
- Claude Code and Cowork: the equivalent path for your setup

Keep the folder name as it is. The `name` field inside `SKILL.md` has to match the folder it sits in, and renaming either one breaks the skill.

You don't invoke a skill by hand. Claude loads it when your request matches its description, which is why the descriptions here list so many trigger phrases: Claude under-triggers skills far more often than it over-triggers them.

## The skills

| Skill | Status | What it does |
|---|---|---|
| [portfolio-case-study-outline](skills/portfolio-case-study-outline) | tested | Structures one project write-up: the sections, the word budget, the visual beside each, and the captions |
| [stakeholder-interview-synthesizer](skills/stakeholder-interview-synthesizer) | tested | Turns rough interview notes into themes tied to decisions, with the disagreements named rather than averaged away |
| [feature-flag-rollout-planner](skills/feature-flag-rollout-planner) | tested | Ramp schedule, guardrail metrics, kill criteria written as numbers, and the date the flag gets deleted |
| [naming-and-taxonomy-checker](skills/naming-and-taxonomy-checker) | tested | Audits product terminology for collisions and split terms, then prices the migration by what each rename costs |

Status key: `idea` not written, `draft` written but untested, `tested` run against real prompts by a fresh agent, `stable` used repeatedly over time.

## What "tested" means here

A skill is only marked `tested` once a fresh agent has read the `SKILL.md` file and nothing else, answered a realistic prompt with it, and reported back on what the file left ambiguous.

Reading a skill back to yourself doesn't count. You know what you meant, so you fill the gaps without noticing they're gaps. Every skill in this repo failed something on its first test round, and the failures were the useful part. The rollout planner never said that a service returning plausible but wrong values keeps every error-rate and latency dashboard green, which meant a rollout following it would have watched the wrong metrics while charging customers incorrectly. That fix only exists because someone who hadn't written the file tried to use it.

## Structure

Every skill is its own top-level folder under `skills/`, with no nesting by category:

```
skills/
├── portfolio-case-study-outline/
│   └── SKILL.md
├── feature-flag-rollout-planner/
│   └── SKILL.md
└── ...
```

A folder can also hold `scripts/`, `references/`, and `assets/` as it grows.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT. See [LICENSE](LICENSE).
