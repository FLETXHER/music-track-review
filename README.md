# Music Track Review

A web-first music research and review workflow for repeated **Artist + Track** inputs.

It is designed to work in two ways:

1. **Web chat:** enable the host's web-search/browsing capability, give the model this repository, ask it to read `README.md` and `SKILL.md`, then submit tracks as `Artist - Track`.
2. **Agent Skills-compatible host:** install this folder as a skill. The required entry point is `SKILL.md`.

## What it returns

```text
Genre：...
Style：...
听感年代：现代 / 复古 / 经典怀旧
大众性：X/5
音乐性：X/5

备注：大众性X分：……；音乐性X分：……。
```

The default answer stays short. Long-form research, source-by-source discussion, and dimension tables are only shown when the user asks.

## Core behavior

- Always research the **exact track/recording/version** on the web before classifying or scoring it.
- Use public music sources as evidence. Do not answer from model memory alone.
- Treat genre/style labels as an **open vocabulary**. Prefer established terms supported by evidence; do not invent labels.
- Use broad genre families as orientation, not as a restrictive whitelist.
- Score **Mainstream Appeal** and **Musicality** independently.
- Separate recording/release year from **listening era**. A modern release can sound retro; an older recording can still have a modern listening character.
- If reliable web access is unavailable, say so instead of pretending research was performed.

## Scope

Included:
- Genre
- Style
- Listening era
- Mainstream Appeal /5
- Musicality /5
- Compact reasoning note

Not included by default:
- Lyrics grading
- Recording-quality label
- Discard/keep decision
- Highlight flags
- Duration checks

## Repository map

- `SKILL.md` — core workflow and output contract
- `references/scoring-guide.md` — scoring dimensions and calibration
- `references/web-research.md` — evidence and source-selection policy
- `references/style-research-policy.md` — how to classify style without overfitting to one database
- `references/genre-family-guide.md` — broad genre-family orientation
- `references/examples.md` — calibration examples
- `evals/evals.json` — behavioral eval cases
- `scripts/validate_repo.py` — lightweight structure and disclosure check

## Web chat starter

After opening web search, a minimal setup message is:

```text
Read this repository's README.md and SKILL.md. Follow the workflow for every track I send.
Use web research first, then return only the required short format unless I ask for detail.
```

Then send:

```text
Joji - Die For You
```

or:

```text
Bob Dylan - Tryin' to Get to Heaven (Version 2)
```

## Status

v0.1 is a calibration-oriented first release. The included examples and evals are intended to keep behavior consistent across different models, not to claim that every genre label is objectively unique or immutable.
