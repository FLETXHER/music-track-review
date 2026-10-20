---
name: music-track-review
description: Research and review individual music tracks from an artist name plus track title, using current web evidence to classify Style and score mainstream appeal and musicality. Use whenever a user submits a song, recording, remix, live version, alternate take, or a short list of tracks and wants concise music classification or scoring.
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
   - Read `references/web-research.md` for evidence selection and the final-output firewall.

3. **Classify Style and run the Primary Style Validation Gate.**
   - Read `references/style-research-policy.md` for the full gate and optional authorized catalog mapping. Use `references/genre-family-guide.md` only for internal orientation.
   - Identify the dominant musical identity from the exact recording and credible evidence before choosing labels. At least one Style must describe a supported dominant musical style; `Instrumental`, `Acoustic`, `Theme`, `Soundtrack`, or `Video Game Music` alone do not complete classification.
   - When a public candidate spelling or style distinction needs checking, consult `references/public-style-reference.md`, then its seed or listening questions as needed. These are heuristic candidates, not track evidence, a whitelist, or the authorized catalog used for out-of-catalog notes.
   - Keep genuine instrumental or soundtrack attributes when relevant, but check every label for musical fit and material importance. Never force three Styles or invent a compound term.
   - If an explicitly authorized catalog is accessible in this session, map accurate terms to it; otherwise use established public vocabulary. Never invent catalog membership or choose a wrong label to satisfy a catalog.
   - If no credible dominant style can be identified, state what needs verification rather than issuing a completed review.

4. **Judge listening era.**
   Choose one:
   - `现代`: modern production and modern overall listening character.
   - `复古`: modern production deliberately foregrounding an older aesthetic.
   - `经典怀旧`: genuinely older-period recording/production whose period character remains audible.
   - Do not infer this field from release year alone.
   - Listening era is NOT a proxy for:
     - release year;
     - recording age alone;
     - artist generation;
     - use of an old sample;
     - a track simply being considered a classic.
   - Choose `经典怀旧` only when the actual recording, performance, mix, instrumentation, or production character audibly carries an older-period identity.
   - An older recording may still be `现代` if its overall production/listening character does not meaningfully read as period-specific under this rubric.
   - A modern track deliberately foregrounding an older aesthetic should be `复古` rather than `经典怀旧`.

5. **Score Mainstream Appeal and Musicality independently.**
   - Read `references/scoring-guide.md`.
   - Find concrete strengths and limitations before choosing the number.
   - Treat 4/5 Musicality as the normal professional pass band; use 3/5 only when a clear pattern of foundational weakness materially prevents a stable professional result. Do not count dimensions mechanically.
   - For either score, award 5/5 only when concrete affirmative evidence supports why the recording reaches the top band, not merely because meaningful defects are absent.
   - Before finalizing, check all five relevant dimensions for each score internally, then use the note-compression gate to merge their evidence into compact wording. Compare the note with the chosen numbers and resolve any contradiction without changing the rubric into arithmetic.
   - A score below 5/5 needs a concrete, supported limit. In particular, Musicality 4/5 cannot rely on vague deductions such as “发展有限” without the specific musical event or section; do not invent a defect when evidence is insufficient.
   - Do not raise Musicality because a work is famous, canonical, critically acclaimed, or commercially successful.
   - Do not lower Musicality merely because Mainstream Appeal is low.

6. **Return the short output.**
   Use exactly this field order:

```text
Style：...
听感年代：现代 / 复古 / 经典怀旧
大众性：X/5
音乐性：X/5

备注：大众性X分：……；音乐性X分：……。
```

When an authorized catalog was actually checked and an important established style is absent from it, use the three-line continuation inside `备注` defined in `references/style-research-policy.md`. Otherwise retain the single-line note above. Never add a separate `Genre` or out-of-catalog field.

### Natural-language pass

Before final output, lightly rewrite the note so it reads like concise human-written analysis rather than generic AI prose.

This pass is stylistic only.

It must NOT:
- change Style, listening era, or either score;
- add or remove scoring reasons;
- introduce new facts, credits, instruments, or evidence;
- weaken the explicit score-deduction requirement;
- add first-person opinions, rhetorical questions, jokes, or conversational filler.

For the note:
- prefer direct, concrete wording;
- remove generic filler such as “整体来看”“值得一提的是”“总体而言”;
- avoid promotional or exaggerated language;
- avoid formulaic “不仅……更……” / “既……又……” constructions when a simpler sentence works;
- avoid vague praise such as “表现出色”“完成度很高” unless followed by the concrete musical reason;
- avoid repetitive AI-style transitions;
- use a neutral, professional, diagnostic work-note tone; avoid emoji, emoticons, memes, slang-heavy phrasing, exaggerated exclamations, and social-post language;
- merge related evidence into concise, selective clauses instead of expanding every dimension into a separate sentence;
- write like a concise QC work note: direct, high-density, and problem-oriented rather than a polished full review;
- for 3/5 and 4/5, use an inline highlight only when it adds a non-redundant, recording-specific value; for every 5/5, state its concrete affirmative evidence inside the relevant score section;
- keep the compact `大众性X分：……；音乐性X分：……。` structure. If an inline `亮点：……` is genuinely useful, keep it inside the same note rather than creating a new field.

The humanization pass may improve wording only. Evidence and scoring logic always take priority.

### Note compression gate

**Check comprehensively → write selectively and compactly.**

1. Check all five relevant dimensions internally, then identify the score-changing evidence: **P0** factors that determine the score, **P1** clear musical issues, and only then a **P2** recording-specific highlight if it adds distinct value.
2. Select the score and retain only the evidence needed to show why it belongs in that band and, where applicable, what blocks the next higher band.
3. Merge related evidence into direct, high-density QC-style short clauses; do not write a dimension-by-dimension audit report or a full music review.
4. Remove repeated, synonymous, score-irrelevant wording, repeated Style labels, and background that does not explain the current sound. Mention a Style only when its audible character directly creates a scoring barrier.
5. Confirm that all five dimensions were considered internally, the concise note supports the selected score, every sub-5 limitation remains explicit, and every 5/5 retains concrete affirmative evidence.

For Mainstream Appeal, normally retain one or two central accessibility strengths and one or two real barriers. For Musicality, retain the stable professional result or foundational-weakness pattern, the largest production/arrangement/performance issue, and what blocks the next band.

Aim for roughly 60–100 Chinese characters for the score explanation and normally stay at or below about 120. This is a soft target: concrete 5/5 affirmative evidence, exact-version reasoning, a special form, or a verified out-of-catalog Style line may need more wording. Correctness wins, but deduplicate first.

## Output rules

- Usually give 1–3 Style labels, with a supported dominant musical style first; broad genre families are internal only.
- Prefer dominant styles; omit trace influences that are not important to the track's identity.
- Before final output, apply the Primary Style Validation Gate from `references/style-research-policy.md`, including genuine instrumental/soundtrack attributes and the fit of every secondary label.
- Keep the default note compact and concrete: it is a concise QC work note, not an audit report.
- For each numeric score, assess all five relevant dimensions as an exhaustive internal check, then write selectively using only score-moving evidence. For instrumental, rap, spoken-word, or similar recordings, assess performance/execution appropriately instead of fabricating conventional vocal evidence.
- This is a coverage requirement, not a five-subscore table, an arithmetic formula, or a reason to count minor limitations as deductions.
- Explain *why points are lost or earned* using audible/researched features: hook strength, flow, rhythmic accessibility, arrangement development, production texture, performance, dynamics, emotional progression, and structure.
- For every score below 5/5, the note must name at least one concrete limitation that prevents the next higher score. A note that only describes the track is invalid.
- For every 5/5, the note must name concrete affirmative evidence that supports the top band; “没有明显问题” alone is invalid.
- For 3/5 and 4/5, a concrete positive highlight is optional; include it only when it adds non-redundant value. Every 5/5 must state concrete affirmative or standout evidence inside the relevant score section. Do not create a standalone highlight field.
- Before output, run a score-to-note consistency check: the documented strengths, barriers, and foundational weaknesses must support the selected number. Each sub-5 deduction must name a specific supported musical reason, especially at Musicality 4/5; do not invent an unheard weakness to fill the note.
- Do not print the research process, source list, or a five-dimension scorecard unless the user asks.
- In the default compact review, do not include artist/creator biography, album or release story, producer/remixer identity, charts, sales, awards, historical context, or style-history discussion. Use research context only to resolve and understand the current recording.
- Never place citations, source markers, reference IDs, or URLs inside Style, 听感年代, 大众性, 音乐性, or 备注.
- If the host requires citations, place them only after the complete compact review.
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
