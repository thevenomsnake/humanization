---
key: T001
status: completed
authorization: approved
role: project-lead
workspace: delivery
---

# 六语言入口与短文案切片

## Outcome

安装 `human-writing-general` 后，用户可以显式指定 `zh-CN`、`zh-TW`、`en`、`ja`、`ko` 或 `es`，选择 `prose` 或 `web-microcopy`，并得到通用事实边界、对应语言规则和确定性硬规则检查。

## Acceptance

- Skill 目录名、front matter `name`、UI display name 和调用提示统一为 `human-writing-general` / `Human Writing General`。
- 六个 locale 档案独立表达本语言的标点、正式度、机器翻译痕迹和自然节奏；中文专属硬禁令不进入通用核心。
- web microcopy 绕过长文材料数量门槛，覆盖页面标题、按钮、状态、错误、隐私和无障碍名称的事实边界。
- 校验 CLI 显式要求 `--locale` 与 `--format`，不自动猜混合语言；保留 `check_prose.py` 兼容入口。

## Boundaries

- 不修改 Sumimi、Cloudflare、生产环境或上游仓库。
- 不做自动自然度评分、逐句对齐或固定 tag 安装器。
- 保留 MIT 许可证、上游归属和 upstream remote。

## Blocked By

- None

## Reads First

- `research/multilingual-skill-research.md`
- `human-writing-general/SKILL.md`
- `human-writing-general/scripts/check_prose.py`

## Completion Check

在仓库目录运行一次定向 smoke：Skill 元数据验证、六个 locale/format CLI 通过样例与一个应失败的中文硬规则样例。

## Execution

- Task opening: not-needed
- Task title: current project lead task
- Attempt: 1

## Completion

- Behavior: 完成 `human-writing-general` 入口、六个 locale 档案、web microcopy 规则和显式校验 CLI；保留中文兼容检查入口。
- Validation: `PYTHONUTF8=1` 下运行 quick_validate、三份脚本 py_compile、六 locale prose、英文 web microcopy 和中文破折号失败样例，定向 smoke 通过。
- Evidence: `Skill is valid!`、六次 `OK locale=... format=prose`、一次 `OK locale=en format=web-microcopy`，负例返回中文破折号错误。
- Commit or artifact: `b1257ba` (implementation commit)
- Blocker: none
