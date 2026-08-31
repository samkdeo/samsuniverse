# Contributing a Skill

## Folder rules

- One skill is one folder directly under `skills/`. No category subfolders.
- The folder name is kebab-case and has to match the `name` field in that skill's `SKILL.md` frontmatter exactly.
- Folder names are unique across the repo.

## SKILL.md template

```markdown
---
name: skill-name-here
description: What it does, plus the specific contexts that should trigger it. Be a little pushy here. Describe more trigger phrases and situations rather than fewer, since Claude tends to under-trigger skills more often than it over-triggers them.
---

# Skill Title

One-paragraph summary of what this skill produces and what it does not do. Route the "not this" cases to sibling skills by name where that's relevant.

## Step 1: ...
## Step 2: ...
...

## Common failure modes to avoid
- ...
```

## House rules

1. Keep `SKILL.md` under about 500 lines. When it runs long, move detail into `references/` and point to it from the main file.
2. The description does the triggering work. Everything about when to use the skill belongs in the frontmatter `description`, not buried in the body.
3. Say what the skill does not do, and point at the sibling skill that does, whenever there's a plausible overlap.
4. Include a "common failure modes" section. Most of a skill's real quality lives there, so be specific about what a lazy or generic pass would get wrong.
5. Put the escape hatch near the top. If a small version of the request should get a small answer, say so before the heavyweight procedure, not after it. An agent that acts while reading will otherwise answer a one-line question with a full audit.
6. Write at least two realistic test prompts before marking a skill `tested`. Prompts someone would actually type, not softballs.

## Testing

A skill is `tested` only after a fresh agent has read the `SKILL.md` and nothing else, answered your test prompts with it, and reported back on what the file left ambiguous. Reading it back yourself doesn't count, because you already know what you meant.

Ask the test agent for three things beyond the answer itself: what it had to improvise, what it ignored as redundant, and whether the skill beat having no skill at all. The last one is worth asking bluntly. A skill that only restates what the model would have done anyway is not worth installing.

Expect the first round to fail. That's the point of running it.

Then run a second round on a scenario the skill was **not** tuned for, before you call it tested. Re-running the original prompt shows the fix landed; it does not show the skill generalizes, and a skill patched from one report will recite that report back convincingly. Every skill in this repo passed its re-test and then failed a generalization round on something that mattered.

Two things to watch when you write the fix. Don't turn a correct observation into a universal constant, because a number that fits one case misfires everywhere else; say what governs and when. And don't use your test prompt as the skill's worked example, which fits the skill to its own exam.

## Privacy

Commits here are public. Configure git with a `@users.noreply.github.com` address before you commit, or your personal email ends up permanently in the history of a public repo.

```bash
git config user.email "<username>@users.noreply.github.com"
```

## Submitting

1. Create your skill folder under `skills/`.
2. Add an entry to `skills-manifest.json`.
3. Add a row to the README table.
4. Run at least one test prompt through the skill and paste the result into your PR description.
5. Open a PR. CI checks frontmatter validity, name uniqueness, and the line-count ceiling.

## Updating an existing skill

Preserve the folder name and the `name` field. Renaming on update breaks anyone who already installed the skill. Bump the version in `skills-manifest.json`.
