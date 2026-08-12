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
5. citation / reference marker 是否允许出现在“备注”字段内部？

如果读取正确，之后等待我发送 Artist - Track。

之后每收到一首歌：
- 必须重新联网研究 exact track / recording / version；
- 严格按照 WEB-CHAT.md 的 Genre、Style、听感年代、大众性、音乐性和备注规则执行；
- 默认只输出规则规定的短格式。
```

校验正确结果应为：

`0.5 / 2/5 / 3/5 / 5/5 / 不允许`

如果回答与上述结果不一致，请让模型重新读取 `WEB-CHAT.md` 后再开始分析歌曲。

之后只需输入：
`Artist - Track`

## Web Chat Compatibility

Tested with the current WEB-CHAT ruleset.

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
5. citation / reference marker 是否允许出现在“备注”字段内部？

读取正确后等待我发送 Artist - Track。
```

> Gemini keeps the repository state from the time it was imported. If this repository is updated, start a new chat and import the repository again to use the latest rules.

A web-first music research and review workflow for repeated **Artist + Track** inputs.

It is designed to work in two ways:

1. **Web chat:** enable the host's web-search/browsing capability, use the Quick Start prompt so the model reads `WEB-CHAT.md`, then submit tracks as `Artist - Track`.
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
- `WEB-CHAT.md` — standalone ruleset for web-chat models that can retrieve external URLs
- `references/scoring-guide.md` — scoring dimensions and calibration
- `references/web-research.md` — evidence and source-selection policy
- `references/style-research-policy.md` — how to classify style without overfitting to one database
- `references/genre-family-guide.md` — broad genre-family orientation
- `references/examples.md` — calibration examples
- `evals/evals.json` — behavioral eval cases
- `scripts/validate_repo.py` — lightweight structure and disclosure check


## Status

Current web-chat ruleset: **v0.5**

The project remains calibration-oriented. Examples and evals are intended to improve consistency across models, not to claim that every genre/style label or score is objectively unique or immutable.

Natural-language cleanup principles are inspired by [Humanizer-zh](https://github.com/op7418/Humanizer-zh), licensed under MIT.
