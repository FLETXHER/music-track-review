---
name: music-track-review
description: Research and review individual music tracks from an artist name plus track title, using current web evidence to classify genre/style and score mainstream appeal and musicality. Use whenever a user submits a song, recording, remix, live version, alternate take, or a short list of tracks and wants concise music classification or scoring.
compatibility: Requires a web search, browser, or retrieval capability that can access public music sources. If web access is unavailable, do not present research-dependent classification or scoring as verified.
---

# Music Track Review

## Purpose

Turn a minimal input such as `Artist - Track` into a compact, repeatable music review grounded in current web research.

## Required workflow

1. **Identify the exact recording first.**
   - Resolve title spelling, featured artists, release, remix/live/alternate-take status, and other version ambiguity.
   - If two plausible recordings remain after research, ask one concise clarification question before scoring.

2. **Research before judging.**
   - Use the current host's web-search, browsing, or retrieval tools.
   - Do not rely on model memory alone.
   - Read `references/web-research.md` for evidence selection.

3. **Classify Genre and Style.**
   - Determine the music's dominant characteristics from evidence, not from a single database label.
   - Use `references/style-research-policy.md`.
   - Broad genre families in `references/genre-family-guide.md` are orientation only.
   - Style vocabulary is open: use established public terms when well supported.
   - Never invent a style name to force a fit.

4. **Judge listening era.**
   Choose one:
   - `现代`: modern production and modern overall listening character.
   - `复古`: modern production deliberately foregrounding an older aesthetic.
   - `经典怀旧`: genuinely older-period recording/production whose period character remains audible.
   - Do not infer this field from release year alone.

5. **Score Mainstream Appeal and Musicality independently.**
   - Read `references/scoring-guide.md`.
   - Find concrete strengths and limitations before choosing the number.
   - Do not raise Musicality because a work is famous, canonical, critically acclaimed, or commercially successful.
   - Do not lower Musicality merely because Mainstream Appeal is low.

6. **Return the short output.**
   Use exactly this field order:

```text
Genre：...
Style：...
听感年代：现代 / 复古 / 经典怀旧
大众性：X/5
音乐性：X/5

备注：大众性X分：……；音乐性X分：……。
```

## Output rules

- Usually give 1–2 Genre labels and 1–3 Style labels.
- Prefer dominant styles; omit trace influences that are not important to the track's identity.
- Keep the default note compact and concrete.
- Explain *why points are lost or earned* using audible/researched features: hook strength, flow, rhythmic accessibility, arrangement development, production texture, performance, dynamics, emotional progression, and structure.
- Do not print the research process, source list, or a five-dimension scorecard unless the user asks.
- If evidence is incomplete, prefer a broader defensible label over a falsely precise label.
- If web access is unavailable, explicitly state that web research could not be performed and do not pretend the result is verified.

## Out of scope by default

Do not add these fields unless the user explicitly asks:
- lyrics evaluation
- recording-quality category
- discard/keep decision
- music-highlight flags
- duration compliance

## Calibration

Before handling a batch or when scores begin drifting, read:
- `references/scoring-guide.md`
- `references/examples.md`
