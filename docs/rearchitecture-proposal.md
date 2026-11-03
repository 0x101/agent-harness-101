# Agent Harness 101: rearchitecture proposal

Status: accepted 2026-11-02. Phase 1 built the same day and published as `0x101/agent-harness-101`. Phases 2 to 4 are still proposals.

## What you asked for

1. Read the course material in the browser, with links and citations.
2. Have a coding agent next to the reading, in the browser.
3. Let other people fork the lab and run it, or learn from a website.

And the constraint that CLAUDE.md already states: the deliverable is your understanding, not the tooling. A rearchitecture that eats ten sessions of build time defeats the lab. So this proposal is phased, and the only phase that has to happen before you start S01 is the cheap one.

## What exists today

One repo, one commit, S01 not started. It mixes three things that have different owners:

| What | Where today | Who should own it |
|---|---|---|
| Content: 42 sessions, 34 readings, the tutor rules | `curriculum.md`, `papers/manifest.tsv`, `CLAUDE.md`, `.claude/commands/` | The course (upstream, public) |
| Kit: eval runner, 12 tasks, naive agent v0, fake-client tests, fetch script | `evals/`, `harness/agent.py`, `harness/tests/`, `papers/fetch.sh` | The course (upstream, public) |
| Run: the agent as it grows, logs, results, failure taxonomy, scripts you write | `harness/`, `log/`, `evals/results/`, `scripts/` | Each learner, in their own copy |

The tutor is Claude Code plus CLAUDE.md plus `/today`. That part works and should stay. It is also hard-wired to you by name, and the papers are fetched to disk because most of them cannot be redistributed.

## The split: three roles, one template repo

Keep one repository. Make it a GitHub template. Draw a hard line between directories upstream owns and directories a learner owns, so a learner can pull curriculum updates without merge conflicts in their own work.

```
agent-harness-101/                the template; others create their copy from it
├── README.md                     three ways in: read the site, fork and run, open in Codespaces
├── LICENSE                       MIT, for the code
├── CLAUDE.md                     thin: imports tutor/SYSTEM.md, lists repo facts
├── Makefile                      init, papers, check, eval, test, serve, site
├── .devcontainer/                one-click Codespaces: venv, papers, lab server on a forwarded port
├── .claude/commands/             today.md, review.md
│
├── course/                       CONTENT. CC BY 4.0. Upstream-owned.
│   ├── LICENSE
│   ├── curriculum.md             the overview and module list only
│   ├── modules.yaml              M0..M9: title, goal, session ids
│   ├── sessions/                 one file per session, frontmatter + body
│   │   ├── s01-what-a-harness-is.md
│   │   └── ... s42-capstone.md
│   ├── readings.tsv              manifest.tsv plus license, read, skip, bibkey columns
│   ├── readings/                 one guide per key: how to read it for this course
│   │   ├── A1.md
│   │   └── ... P22.md, R1.md, R2.md
│   └── readings.bib              generated from arXiv metadata
│
├── tutor/                        THE TUTOR HARNESS. Upstream-owned.
│   ├── SYSTEM.md                 the rules now in CLAUDE.md, with no learner name in them
│   ├── hooks/guard_harness.py    PreToolUse hook: refuse Edit/Write under harness/ unless unlocked
│   └── tests/                    hook tests; slash commands stay in .claude/commands/
│
├── evals/                        KIT. Upstream-owned, except results/ and trajectories/.
│   ├── run.py
│   ├── tasks/                    the 12 tasks; learners add their own in S32
│   ├── results/                  learner state
│   └── trajectories/             learner state, gitignored
│
├── harness/                      LEARNER. Ships as v0. Grows in each copy.
├── scripts/                      LEARNER. tokens_per_step.py (S13), pareto.py (S31), propose.py (S36)
├── log/                          LEARNER. STATE.md, TEMPLATE.md, one entry per session
│
├── server/                       KIT, phase 2. The local lab server, Python only.
│   ├── app.py                    /api/state, /api/results, /api/trajectories, /api/run (SSE)
│   ├── static/                   trajectory viewer and scoreboard, plain HTML and JS, no Node
│   └── tutor.py                  phase 3: an Agent SDK session that uses tutor/SYSTEM.md
│
├── site/                         KIT. Astro site built from ../course. Deploys from upstream.
│   └── src/content.config.ts     glob loaders pointing at ../course/sessions and ../course/readings
│
└── papers/                       fetch.sh; pdf/, web/, repos/ stay gitignored
```

What moves: `curriculum.md` splits into 42 session files. `papers/manifest.tsv` becomes `course/readings.tsv`. The tutor rules move out of `CLAUDE.md` into `tutor/SYSTEM.md`. Nothing under `evals/tasks/` or `harness/` changes.

Why per-session files rather than one curriculum file: the site needs typed entries, `/review` needs to edit one session without touching the others, and a learner's log entry can link to its session. The tutor reads the same files, so there is one source of truth.

A session file looks like this:

```markdown
---
id: S15
module: M3
title: Rule-based elision
reads: [{ key: P10, where: "the context-management section" }]
build: Replace tool outputs older than K steps with a one-line stub.
measure: Run the full set once.
---
Why this session exists, in two or three sentences, and the prediction question
the tutor asks before the reading.
```

### Who owns what, enforced by git

Learners create their copy from the template, add the template as `upstream`, and pull curriculum updates with `git merge upstream/main`. The learner-owned directories carry a merge driver in `.gitattributes` so an upstream change to v0 never overwrites their agent:

```
harness/**        merge=ours
log/**            merge=ours
scripts/**        merge=ours
evals/results/**  merge=ours
```

`make init` sets the driver (`git config merge.ours.driver true`), resets `log/STATE.md` to S01, clears results, and asks for the learner's name once. That name lands in `.lab/config.toml`, which is gitignored, and the tutor reads it. The rules in `tutor/SYSTEM.md` say "the learner", never a name.

## The three surfaces

```
   ┌──────────────────────┐      ┌───────────────────────────┐      ┌──────────────────────┐
   │  Site (static, hosted)│      │  Local lab server (Python) │      │  Claude Code          │
   │  built from course/   │ ───▶ │  localhost:8787            │ ◀──▶ │  CLAUDE.md → tutor/   │
   │  read, navigate, cite │      │  trajectories, scoreboard, │      │  /today, /review      │
   │  "Lab" page detects ──┼──────┤  run evals, tutor chat (P3)│      │  edits, bash, evals   │
   │   the local server    │      │  reads log/, evals/, course│      │                       │
   └──────────────────────┘      └───────────────────────────┘      └──────────────────────┘
            everyone                   anyone who forked                  the primary tutor
```

**The site** is static and hosted (Vercel or GitHub Pages) from the upstream repo. Pages: home, curriculum, one page per session, one page per reading, a lab page, and an optional "author's run" page that renders your logs and scoreboard as the worked example. Anyone can read it without cloning anything.

**The local lab server** is the piece that makes "a coding agent in the browser" real without hosting anyone's code execution. It runs in the learner's clone, serves a trajectory viewer and the scoreboard, and can start eval runs. The site's lab page probes `localhost:8787` and, when it answers, shows those panels inline. Hosted site plus local execution, no accounts, no sandboxes to pay for. In Codespaces the forwarded port plays the same role.

**Claude Code** stays the primary tutor and coding agent. It already has the file tools, bash, and the session rules. Phase 3 adds a browser chat that drives the same tutor through the Claude Agent SDK, with the same `tutor/SYSTEM.md`, so the two never drift.

## Reading and citing

`course/readings.tsv` gains four columns over today's manifest:

| column | example | why |
|---|---|---|
| `license` | `CC-BY-4.0`, `arxiv-nonexclusive`, `copyright` | decides whether the site may embed the PDF or must link out |
| `read` | `abstract; §1; §3 (ACI design)` | the orientation the tutor gives today, made durable |
| `skip` | `§5 experiments` | same |
| `bibkey` | `yang2024sweagent` | links `readings.bib` entries |

Each reading gets a page: metadata, the arXiv and DOI links, "how to read it for this course", which sessions use it, and a BibTeX block. For arXiv papers under a CC license the page can embed the PDF. For the others, and for every blog post, the page links out. The site never hosts a copy of a copyrighted post. Locally, `papers/fetch.sh` keeps working exactly as now, so the tutor can still open the PDF with page ranges.

Citation syntax, used everywhere: `[P10 §4.2]` or `[P1 p.3]`. In session files and log entries it is plain text. The site turns it into a link to the reading page with the section in the anchor. The tutor resolves the key through `readings.tsv` to the local file. One syntax, three resolvers.

Quiz questions and answers stay in the tutor, not on the site. Putting them on a public page would let a learner read the quiz before the reading.

## The tutor, generalized

Move the "Your role" and "Session flow" sections of `CLAUDE.md` into `tutor/SYSTEM.md`. The root `CLAUDE.md` becomes `@tutor/SYSTEM.md` plus the repo facts (model, oracle and noop expectations, where trajectories live). Claude Code resolves the import; the Agent SDK tutor loads the same file as its system prompt.

Two tutor rules can be enforced rather than requested:

- **"Do not edit `harness/` unless told to."** A PreToolUse hook on Edit and Write refuses paths under `harness/` unless the learner has run `make unlock`, which touches `.lab/unlock-harness` and opens a one-hour window. Before phase 1 this rule lived only in prose.
- **"Never edit `hidden/` or `solution/`."** Same hook, no unlock.

This is also a teaching moment: by S12 the learner has read Engineering Pitfalls and can be pointed at the tutor's hook as an example of a harness constraint enforced by schema or hook rather than by instruction.

## Open-sourcing

- **Template repo**, not forks. "Use this template" gives a clean history and no accidental PRs of personal logs upstream. Template plus `upstream` remote covers updates.
- **Licenses.** MIT for `evals/`, `harness/`, `server/`, `site/`, `tutor/`. CC BY 4.0 for `course/`. State both in the README.
- **Papers stay out of git.** `readings.tsv` records the license per item; `fetch.sh` is the only distribution path.
- **CONTRIBUTING.md.** New tasks go in new folders, must pass `--mode oracle` and fail `--mode noop`, and must say which failure class they target. New readings need a guide. Curriculum edits need the session's measure step to still be runnable.
- **Public tasks have a shelf life.** Once the hidden tests are on GitHub, future models may have trained on them and pass rates will inflate. The curriculum already answers this: S32 has every learner write private tasks. Say so in CONTRIBUTING and in the S32 session file.
- **Your own copy.** You are the author and a learner. The public template is `0x101/agent-harness-101`, created as a fresh root commit from this tree. The author edits `course/` there. The learner works in `0x101/harness-lab`, this repository, which has the template as its `upstream` remote and grows `harness/` and `log/` exactly like any other copy. The site's "author's run" page pulls `log/` and `evals/results/history.tsv` from here at build time. When `/review` proposes curriculum edits in this copy, apply them upstream.

## Phases

### Phase 1: restructure and publish (about two evenings, before or alongside S01)

1. Split `curriculum.md` into `course/sessions/*.md` with frontmatter. Scripted; the text does not change.
2. Move the manifest to `course/readings.tsv`, add the four columns, generate `readings.bib` and the 47 reading guides from what the curriculum already says about sections.
3. Move the tutor rules to `tutor/SYSTEM.md`, thin out `CLAUDE.md`, remove the name, add the harness guard hook.
4. Add `Makefile`, `make init`, `.gitattributes` merge drivers, `.devcontainer/`, both licenses, `CONTRIBUTING.md`.
5. Scaffold `site/` with Astro and Starlight, content collections over `../course`, deploy from upstream.
6. Flip the GitHub template flag. Create your learner copy. Run `make init` there and start S01.

Nothing in this phase touches `harness/agent.py`, `evals/run.py`, or the tasks. Oracle and noop runs stay the regression test.

### Phase 2: the local lab server (about one evening, grows with the curriculum)

A trajectory viewer with a step timeline, tool calls and outputs, input tokens per step, and a diff of two runs; plus the scoreboard from `history.tsv` and a "run evals" form that streams progress. Plain Python server, plain HTML and JS, no Node for learners.

This is lab infrastructure, so it is fair game for me to write. It also serves three sessions directly: S03 reads trajectories, S13 plots tokens per step, S26 refactors logging into typed events that this viewer will consume. Build the viewer at S03 rather than up front.

### Phase 3: the tutor in the browser (a few evenings; decide at S18, checkpoint 1)

`server/tutor.py` opens a Claude Agent SDK session with `tutor/SYSTEM.md` as the system prompt, the repo as the working directory, the file and bash tools, the harness guard hook, and two custom tools: run evals and read state. The lab page gets a chat pane that streams it. Sessions persist, so "resume today's session" works. The learner still edits code in their own editor; the tutor edits on explicit request, as the rules say.

This gives reading, tutor, and trajectories in one window. It is also a real project, which is why it waits until the first checkpoint. If Claude Code in the browser or the desktop app side by side with the site turns out to be enough, skip it.

### Phase 4: a hosted lab with code execution. Not recommended.

Running learners' agents on a server means sandboxes, API keys for strangers, and abuse handling. Codespaces gives one-click setup with the local server on a forwarded port, and Claude Code on the web can open the repo directly. Both cover "I don't want to set anything up" without hosting execution. Revisit only if there are many learners who cannot use either.

## Decisions for you

| | Decision | Recommendation | Why |
|---|---|---|---|
| A | Site stack | Astro with Starlight | Content collections match one-file-per-session, search and navigation are free, and islands can host the phase 2 and 3 panels later. MkDocs is simpler but has no path to interactive panels. Next.js is heavier than a content site needs. |
| B | One repo or two | One template repo; your learner work in a copy made from it | Keeps the course and the kit together for contributors. Your copy is just another learner's copy, which keeps the template honest. |
| C | Where execution runs | Local clone or Codespaces, never hosted | No sandboxes, no key handling, and the site still shows live panels when a local server answers. |
| D | Publish your own logs and results on the site | Yes, as "author's run" | A worked example is the most useful thing a new learner can see, and it keeps you honest about measuring. Your call. |
| E | When to do phase 3 | Decide at S18 | By then you will know whether the site plus Claude Code side by side is enough. |

## Risks

- **Scope creep.** Phases 2 and 3 are fun to build and are not the course. Phase 1 is bounded; everything after it should be scheduled against the curriculum, not instead of it.
- **Copyright.** Blog posts and some arXiv PDFs cannot be hosted. The license column and link-out behaviour handle it, but someone has to fill the column in.
- **Task contamination.** Public hidden tests will leak into training data over time. S32 and CONTRIBUTING carry the mitigation.
- **Author and learner friction.** Curriculum edits proposed by `/review` in your copy have to be applied upstream by hand. One person, a few times over 42 sessions; acceptable.
