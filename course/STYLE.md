# Writing for Agent Harness 101

How a session page and a reading guide are written. Read this before you write or review either.
[S01](sessions/s01-what-a-harness-is.md) and [A1](readings/A1.md) are the worked examples; when this page and
an example disagree, fix whichever is wrong.

## What a page is for

A learner should be able to start a session from its page alone: understand the problem, read the source
with a purpose, make one change to their harness, measure it, and know whether they are done. The tutor
coaches and reviews. It does not carry the teaching.

Three things make this course different, and every page keeps them:

1. **The source.** Each idea comes from a paper or post the learner reads. Say what it claims, what
   supports the claim, and where it is weak.
2. **The measurement.** Each change is measured on the same tasks. Give the command and say what would
   count as noise.
3. **The learner writes the harness.** A page never contains the finished code for its build. It can show
   the starter code, pseudocode, and how behaviour should change.

## Voice

- Plain words first, then the proper term in bold the first time it appears.
- Second person, present tense, short sentences. Say what happens and why.
- No filler, no hype, no hedging. If something is not known or not yet measured, say so in those words.
- No em-dashes. No finance or trading examples. Examples are everyday and neutral.
- Never rely on colour alone to carry meaning. Diagrams are text diagrams or have labels on every part.
- Every claim about the course's own code must match the code. Quote file names and line contents exactly.
- Every number has a source next to it: a section of a reading, or a run in this repo.

## A session page

File: `course/sessions/sNN-slug.md`. Keep the frontmatter keys as they are. Aim for 800 to 1,600 words.
The sections, in order, with these exact headings:

| Heading | What goes in it |
|---|---|
| (opening, no heading) | Two or three sentences: what this session is and why it comes now. Then one line with the time for reading, building and measuring, what must be finished first, and what the session spends. |
| `## The problem` | The failure or gap this session addresses, shown concretely. Use a recorded run of the agent when one exists. |
| `## Predict first` | One question to answer before reading on. The answer goes in a `<details>` block. |
| `## The idea` | The concept in plain words, then the term. A text diagram where a mechanism needs one. |
| `## What the reading says` | Why this source, what to look for, and a link to its guide. Two or three sentences per reading, not a summary that replaces reading it. |
| `## How real harnesses do it` | One or two links into open-source harness code or official documentation, each with a sentence on what to notice. Never leaked or private code. |
| `## Build` | What to change and where. Then `### What done looks like`: the commands that show the build works and what they must print. |
| `## Measure` | The eval command, what to compare against, and what counts as noise. |
| `## Check yourself` | Three questions: one recall, one why, one "what would this do in `agent.py`". Answers in `<details>` blocks, with a reason for every wrong choice. |
| `## Design choices` | Two or three decisions this session made for you, with the alternative and when the alternative is better. |
| `## Log` | The questions the log entry answers. |
| `## Next` | One or two sentences on what the next session adds. |

A session with no build (a reading or analysis session) keeps the headings and says so under `## Build`.

### Questions and answers

Write a question as a bold line, the choices as a lettered list, and the answer in a `<details>` block
with a blank line after `<summary>` so the Markdown inside renders:

```markdown
**1. What decides when the loop stops?**

- A. The harness counts the files changed.
- B. The model replies without asking for a tool.
- C. The eval runner sends a stop signal.

<details>
<summary>Answer</summary>

**B.** The loop ends when a reply has no tool request. A is wrong because nothing in `agent.py` looks
at the files. C is wrong because the runner only starts the agent and checks the result afterwards.

</details>
```

## A reading guide

File: `course/readings/KEY.md`. Keep the frontmatter (`key`, `title`). Aim for 400 to 700 words.
The sections, in order, with these exact headings:

| Heading | What goes in it |
|---|---|
| `## In one paragraph` | What the source claims, in our own words. 60 to 100 words. |
| `## How to read it for this course` | Reading time. Which sections to read and which to skip, each linked. Then one line per session that uses it, saying what to look for. |
| `## What it shows` | The two or three results or observations that carry the source, each with a link to its section. Say whether each is a measurement or the authors' experience. |
| `## Where it is weak` | What it did not test, what has changed since, where other readings in the course disagree. |
| `## What it means for your harness` | The consequence for the learner's own agent, tied to sessions. |
| `## In their words` | Two or three short quotes. See the rules below. |
| `## Where it comes up` | The sessions that use it. Keep the existing list. |
| `## Links` | Keep the existing list. |

### Quoting

The license column in `readings.tsv` decides how much may be quoted.

- `copyright` and `arXiv-nonexclusive-1.0`: at most three quotes, each 50 words or fewer. No figures or tables.
- `CC-BY-4.0`: at most three quotes, each 80 words or fewer, with credit. Figures may be reproduced with a credit line.
- Other licenses: treat as `copyright`.

Every quote is exact and continuous: no ellipses, no words changed, no sentences joined. Write it as a
blockquote in straight double quotes, with the source section on the next line:

```markdown
> "They are typically just LLMs using tools based on environmental feedback in a loop."
>
> Source: [Agents](https://www.anthropic.com/engineering/building-effective-agents#agents)
```

Link to the section, not only the page. arXiv papers have an HTML version at
`https://arxiv.org/html/<id>` whose sections have anchors such as `#S3` and `#S5.SS1`.

## Before you open a pull request

- Read the source yourself. A guide written from an abstract is worse than no guide.
- Check every quote against the source, character for character.
- Check every number against the section you cite.
- Run `make test`, `make check` and `make site`.
