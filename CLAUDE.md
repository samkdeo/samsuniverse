# Instructions for Claude Code working in this repo

This repo publishes standalone Claude skills for public use, one per folder under `skills/`. It is public, so treat everything committed here as permanent and world-readable.

## Before you commit anything

Check the git identity first:

```bash
git config user.email
```

If it is a personal address, stop and set the GitHub noreply form instead. A personal email committed to a public repo stays in the history, and the only fix is deleting the repo. This has already happened once.

## When asked to build a new skill

1. Check `docs/roadmap.md` for the backlog. If the requested skill isn't there, add it.
2. Follow the `SKILL.md` template in `CONTRIBUTING.md` exactly: frontmatter `name` and `description`, a step-by-step body, then a "common failure modes to avoid" section.
3. Read two or three existing skills in `skills/` as the house-style reference before writing. Match their level of specificity and the way they route overlapping cases to a sibling skill by name.
4. Create the folder at `skills/<skill-name>/SKILL.md`. Add `scripts/`, `references/`, or `assets/` only when the skill actually needs them.
5. Write at least two realistic test prompts. Not softballs: prompts a real user would type, including the awkward shapes such as a request that arrives with half the information missing.
6. Test it for real, not by reading it back to yourself. Use a subagent that has read only the new `SKILL.md` and none of the conversation that produced it, and report the actual output. Ask it what it had to improvise, what it ignored, and whether the skill beat having no skill. If subagents aren't available, fall back to a fresh `claude -p` call with the skill's content as the system prompt.
7. Fix what the test found, then re-test. Expect the first round to fail; that is the point of running it.
8. Run a generalization round before marking anything `tested`. Give the skill a scenario it was not tuned for: a different age band, format, or shape of request. A re-test that reuses the original prompt confirms the fix landed but proves nothing about whether the skill generalizes, and a skill patched from one case will happily recite that case back. Every skill in this repo passed its re-test and then failed its generalization round on something real.
9. Update `skills-manifest.json` and the README table. Use `status: "draft"` unless step 6 passed cleanly, in which case `"tested"`.
10. Commit with a message like `Add skill: <skill-name>`. One skill per commit, not batched, so the history stays reviewable. Put what the tests found in the commit body.

## When asked to build several skills at once

Work through them one at a time, running the full loop above for each before starting the next. Drafting all of them first and testing later leaves partial progress unusable and the commits tangled. Pause and summarize every 5 skills.

## Testing philosophy

A skill counts as `tested` only once a fresh agent has followed just the `SKILL.md` and produced a reasonable result. You reading it back mid-authoring, with full context of what you meant, doesn't count.

The failures are the useful output. Every skill in this repo failed something on its first round, and the fixes that came out of those failures are the reason the skills are worth installing. If a test comes back clean on the first try, suspect the prompt was too easy rather than the skill was perfect.

If subagents or API access aren't available in the environment, say so in the commit or PR notes instead of marking a skill `tested` on the strength of your own read-through.

## Two ways a fix makes things worse

Both of these have already happened here, and they are the main risk when patching a skill from a single test report.

**Writing a constant where a method belongs.** A number that is right for the case in front of you becomes wrong everywhere else. A chapter-book word budget derived from read-aloud minutes told an author to halve a normal manuscript. A nine-syllable metrical anchor flagged every line of an anapestic poem as broken. A prose word budget applied to verse would have told a poet their correctly-sized book was thin and invited them to pad it. Write what governs and when: read-aloud time governs picture books but not books a child reads alone; find the manuscript's own metre rather than importing one. When you catch yourself asserting a total, give the subtraction instead.

**Writing the test prompt into the skill as its worked example.** This fits the skill to its own exam. Two skills here ended up containing the exact scenario they were tested on, and the test agents flagged that they could not tell good coverage from tuning. Illustrate a rule with a different case than the one that revealed it.

## Don't

- Don't commit with a personal email address.
- Don't nest skills under category folders. Flat structure only.
- Don't rename an existing skill folder or its `name` field. That breaks anyone who already installed it.
- Don't mark a skill `stable` until it has been used and tested more than once.
- Don't add a skill to the manifest without adding it to the README table. CI checks that the manifest and the folders agree, but not the README.
