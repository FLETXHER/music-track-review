# Music Track Review

## 🚀 Quick Start — Copy & Use

适用于能够直接读取网页 URL 并进行联网搜索的网页模型。
具体平台兼容性见下方 Web Chat Compatibility。

使用步骤：

- 开启 Web Search / 联网搜索
- 复制下面的 Prompt
- 粘贴到一个新对话
- AI 校验规则成功后，只需要继续发送 `Artist - Track`

```text
请实际读取并严格遵守这个规则文件的当前内容：

https://raw.githubusercontent.com/FLETXHER/music-track-review/main/WEB-CHAT.md

不要只根据搜索摘要、缓存或模型记忆判断。
这个 WEB-CHAT.md 是本对话后续歌曲分析的完整工作规则。

读取完成后暂时不要分析歌曲。

请先只回答：

1. Ruleset version 是多少？
2. Boys Noize - Sireneh 的 Mainstream Appeal calibration 是多少？
3. JAY-Z - What More Can I Say 的 Mainstream Appeal calibration 是多少？
4. Joji - Die For You 的 Mainstream Appeal calibration 是多少？
5. 音乐性中的“正常专业合格带”是几分？
6. 音乐性 3/5 的校准短语是什么？
7. 音乐性 5/5 是否必须提供明确的正向证据？
8. 默认短评是否可以加入艺人、专辑或发行背景？
9. citation / reference marker 是否允许出现在 Style、听感年代、大众性、音乐性或“备注”字段内部？
10. 默认输出有哪五个字段，是否包含 Genre？
11. 只有 Instrumental / Soundtrack 等形式或用途标签，能否通过 Primary Style Validation Gate？
12. 没有用户授权的 Style 标签库时，能否声称完成严格库内匹配？
13. 音乐性 4/5 的备注能否只写“发展有限”作为扣分理由？
14. 五维判断如何用于默认约 60–100 字的备注？

如果读取正确，之后等待我发送 Artist - Track。

之后每收到一首歌：
- 必须重新联网研究 exact track / recording / version；
- 严格按照 WEB-CHAT.md 的 Style、听感年代、大众性、音乐性和备注规则执行；
- 默认只输出规则规定的短格式。
```

校验正确结果依次为：

1. `v0.8`
2. `2/5`
3. `3/5`
4. `5/5`
5. `4/5`
6. `borderline / discard tendency but not automatic discard`
7. `是，必须`
8. `不允许`
9. `不允许`
10. `Style、听感年代、大众性、音乐性、备注；不包含 Genre。`
11. `不能；至少需要一个可信的主导音乐风格。`
12. `不能；应使用可信公开风格词汇作为降级方案。`
13. `不能；必须指出具体、经证据支持的音乐限制，不能虚构缺陷。`
14. `内部完整检查五维，最终只写影响分数的证据；约60–100字，通常不超过约120字。`

如果回答与上述结果不一致，请让模型重新读取 `WEB-CHAT.md` 后再开始分析歌曲。

之后只需输入：
`Artist - Track`

## Web Chat Compatibility

Compatibility observations below are based on prior web-chat testing and may change with model or product versions. v0.8 has not been re-benchmarked across every listed platform.

| Platform | Status | Notes |
| --- | --- | --- |
| Kimi | ✅ Recommended | Good rule adherence, web research, and compact output |
| ChatGPT | ✅ Recommended | Good rule adherence, web research, and scoring notes |
| Claude | ✅ Recommended | Good rule adherence and stable compact output |
| Gemini | ⚙️ Requires repository import | Gemini Web requires importing the repository first; direct GitHub URL retrieval is not supported for this workflow. Execution quality has not yet been fully tested. |
| Doubao | ⚠️ Limited | Can retrieve the rules, but may ignore the strict output and scoring-note contract |
| DeepSeek Web | ❌ Not recommended | Can retrieve the rules, but exact-track resolution, formatting, and scoring adherence were unstable in testing |

Compatibility refers only to observed behavior with this repository's web-chat workflow and may change as model or product versions change.

### Gemini setup

Gemini Web currently requires importing the GitHub repository instead of reading the GitHub URL directly from a prompt.

步骤：

1. Open Gemini on desktop.
2. Click Add files.
3. Choose More uploads → Import code.
4. Import:
   https://github.com/FLETXHER/music-track-review
5. After the repository is attached, send:

```text
请读取当前已导入仓库中的 WEB-CHAT.md。

把 WEB-CHAT.md 作为本对话后续歌曲分析的完整工作规则。
不要使用 README.md、SKILL.md 或模型记忆覆盖 WEB-CHAT.md。

读取完成后暂时不要分析歌曲。

请先只回答：

1. Ruleset version 是多少？
2. Boys Noize - Sireneh 的 Mainstream Appeal calibration 是多少？
3. JAY-Z - What More Can I Say 的 Mainstream Appeal calibration 是多少？
4. Joji - Die For You 的 Mainstream Appeal calibration 是多少？
5. 音乐性中的“正常专业合格带”是几分？
6. 音乐性 3/5 的校准短语是什么？
7. 音乐性 5/5 是否必须提供明确的正向证据？
8. 默认短评是否可以加入艺人、专辑或发行背景？
9. citation / reference marker 是否允许出现在 Style、听感年代、大众性、音乐性或“备注”字段内部？
10. 默认输出有哪五个字段，是否包含 Genre？
11. 只有 Instrumental / Soundtrack 等形式或用途标签，能否通过 Primary Style Validation Gate？
12. 没有用户授权的 Style 标签库时，能否声称完成严格库内匹配？
13. 音乐性 4/5 的备注能否只写“发展有限”作为扣分理由？
14. 五维判断如何用于默认约 60–100 字的备注？

读取正确后等待我发送 Artist - Track。
```

> Gemini keeps the repository state from the time it was imported. If this repository is updated, start a new chat and import the repository again to use the latest rules.

A web-first music research and review workflow for repeated **Artist + Track** inputs.

It is designed to work in two ways:

1. **Web chat:** enable the host's web-search/browsing capability, use the Quick Start prompt so the model reads `WEB-CHAT.md`, then submit tracks as `Artist - Track`.
2. **Agent Skills-compatible host:** install this folder as a skill. The required entry point is `SKILL.md`.

## What it returns

```text
Style：...
听感年代：现代 / 复古 / 经典怀旧
大众性：X/5
音乐性：X/5

备注：大众性X分：……；音乐性X分：……。
```

The default answer stays short. Long-form research, source-by-source discussion, and dimension tables are only shown when the user asks.
When an authorized catalog was actually checked and a material established style is absent from it, `备注` may use one style-name line followed by separate short lines for the two scores. It remains the same fifth field; without an authorized catalog, use the compact single-line note.

## Core behavior

- Always research the **exact track/recording/version** on the web before classifying or scoring it.
- Use public music sources as evidence. Do not answer from model memory alone.
- Identify the supported dominant musical style first. Run the **Primary Style Validation Gate** so form or soundtrack labels never stand alone, and do not fill Style slots with weak matches.
- Map accurate terms to a user-authorized catalog when available in the session. This public repository contains no such catalog; without one, use established, publicly checkable terms and do not claim strict catalog matching.
- Do not create temporary compound labels. Use broad genre families only as internal orientation; the output has no Genre field.
- Score **Mainstream Appeal** and **Musicality** independently.
- Check all five relevant dimensions internally for each score, then write only the score-moving evidence; do not turn the final note into a dimension-by-dimension report.
- Keep the default note as a concise QC work note: direct, problem-oriented, and roughly 60–100 Chinese characters (normally at or below about 120). Preserve correctness first, then remove repetition, Style restatement, and nonessential background.
- For 3/5 and 4/5, an inline highlight is optional and must add non-redundant value. Every 5/5 still needs concrete affirmative evidence, which may be integrated into its score explanation rather than added as a fixed `亮点：` clause.
- Every sub-5 score needs a supported, specific limitation; Musicality 4/5 cannot use vague wording alone or invent a defect to justify its score.
- Separate recording/release year from **listening era**. A modern release can sound retro; an older recording can still have a modern listening character.
- If reliable web access is unavailable, say so instead of pretending research was performed.

## Scope

Included:
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
- `WEB-CHAT.md` — standalone ruleset for web-chat models that can retrieve external URLs
- `references/scoring-guide.md` — scoring dimensions and calibration
- `references/web-research.md` — evidence and source-selection policy
- `references/style-research-policy.md` — how to classify style without overfitting to one database
- `references/genre-family-guide.md` — broad genre-family orientation
- `references/examples.md` — calibration examples
- `evals/evals.json` — behavioral eval cases
- `scripts/validate_repo.py` — lightweight structure and disclosure check


## Status

Current web-chat ruleset: **v0.8**

The project remains calibration-oriented. Examples and evals are intended to improve consistency across models, not to claim that every genre/style label or score is objectively unique or immutable.

Natural-language cleanup principles are inspired by [Humanizer-zh](https://github.com/op7418/Humanizer-zh), licensed under MIT.
