---
key: T002
status: completed
authorization: approved
role: project-lead
workspace: delivery
---

# 全表达性文字与文本反 slop

## Outcome

`human-writing-general` 覆盖文章之外的所有表达性文字，包括文档、产品说明、营销文案、邮件、社交内容和网页 GUI 文案；它吸收 `kill-ai-slop` 的文本识别与改写原则，不处理视觉样式或组件实现。

## Acceptance

- Skill 的输入契约有通用 `copy` 格式，`web-microcopy` 作为 HTML/GUI 专用分支保留。
- 新的文本反 slop 参考明确区分模板化口号、空泛承诺、无来源数字、装饰性强调、三连节奏和名词堆叠，并要求先确认语境再改写。
- 六个 locale 都能读取同一通用原则，同时保留各自的自然表达与机器翻译边界。
- 确定性 CLI 对明显模板句只给人工判断警告，不把自然度伪装成硬性通过/失败；显式 locale/format 仍然必填。
- 文档记录 `kill-ai-slop` 来源、Apache-2.0 链接、适配范围和排除的视觉规则。

## Boundaries

- 不吸收颜色、字体、布局、卡片、圆角、动效、图标、按钮样式或视觉扫描器。
- 不修改 `kill-ai-slop`、Sumimi、Cloudflare、生产环境或上游仓库。
- 不做自动自然度评分、逐句对齐或自动发布。

## Blocked By

- None

## Reads First

- `research/multilingual-skill-research.md`
- `human-writing-general/SKILL.md`
- `human-writing-general/references/locales/`

## Completion Check

在仓库目录运行一次定向 smoke，验证 Skill 元数据、`copy` 和 `web-microcopy` 入口、六语言文本模板警告，以及一个明确硬规则负例。

## Execution

- Task opening: not-needed
- Task title: current project lead task
- Attempt: 1

## Completion

- Behavior: 新增 `copy` 全表述文字模式、文本 anti-slop 参考、六语言 warning 规则和 GUI 文本属性扫描；明确排除视觉规则。
- Validation: `PYTHONUTF8=1` 下运行 quick_validate、四份脚本 py_compile、`check_writing_smoke.py`、六 locale clean copy、英文 web microcopy 和中文破折号负例，最终 smoke 通过。
- Evidence: `Skill is valid!`、`check_writing smoke passed`、六次 `OK locale=... format=copy`、一次 `OK locale=en format=web-microcopy`，负例返回中文破折号错误。
- Commit or artifact: pending
- Blocker: none
