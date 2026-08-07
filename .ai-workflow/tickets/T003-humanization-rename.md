---
key: T003
status: completed
authorization: approved
role: project-lead
workspace: release
---

# Humanization 稳定标识与仓库重命名

## Outcome

Skill、安装目录、UI 显示名、本地仓库目录和 GitHub 仓库统一使用 `humanization`，最终用户调用名为 `$humanization`，显示名为 `Humanization`。

## Acceptance

- `humanization/SKILL.md` 的 front matter `name` 为 `humanization`。
- `humanization/agents/openai.yaml` 的 display name 和 default prompt 使用 `Humanization` / `$humanization`。
- `humanization/VERSION` 为 `3.0.0`，README、资产和安装说明不再把旧 slug 当作活动入口。
- GitHub 仓库为 `thevenomsnake/humanization`，`origin` 已更新；`upstream` 仍指向 `KKKKhazix/human-writing`。

## Boundaries

- 不修改上游仓库、Sumimi、Cloudflare 或生产环境。
- 旧 slug 只在变更历史和迁移说明中保留，不作为稳定调用名。

## Blocked By

- None

## Reads First

- `humanization/SKILL.md`
- `humanization/agents/openai.yaml`
- `README.md`

## Completion Check

在仓库目录运行 quick_validate、自检脚本和元数据/远程仓库查询。

## Execution

- Task opening: not-needed
- Task title: current project lead task
- Attempt: 1

## Completion

- Behavior: 完成本地目录、Skill 标识、UI 元数据、README 资产和 GitHub 仓库的统一重命名。
- Validation: `Skill is valid!`、`check_writing smoke passed`、`Humanization rename smoke passed`；GitHub API 返回 `thevenomsnake/humanization` 且 `isFork: true`。
- Evidence: `origin=https://github.com/thevenomsnake/humanization.git`，`upstream=https://github.com/KKKKhazix/human-writing.git`。
- Commit or artifact: `7b2876e` (local rename implementation)
- Blocker: none
