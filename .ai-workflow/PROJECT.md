---
schema_version: 2
workflow_version: 0.10.0
status: active
project_name: "human-writing-general"
---

# Human Writing General

## Product Direction

- Intended user: 使用 Codex Skill 写作、改稿和制作网站短文案的多语言用户。
- Problem: 中文长文规则不能直接用于英文、日文、韩文、西班牙文或台湾繁中，短文案也不应被长文材料门槛误伤。
- First value: 明确指定 `locale` 与 `format` 后，Skill 能按通用事实边界和对应语言档案生成或检查 prose / web microcopy。
- Delivery: 可安装的 `human-writing-general/` Skill 目录、语言档案、web microcopy 参考和确定性 CLI 校验器。
- Boundaries: 只修改本 fork；不触碰 Sumimi、Cloudflare、生产环境或自动发布；保留 MIT、上游归属和同步入口。

## Current State

上游 1.1.0 中文 Skill 已完成结构研究。首个六语言入口与 web microcopy 纵向切片已实现并通过定向 smoke；后续可在真实样例上扩充语言专属硬规则。

## Roles

- [project-lead](roles/project-lead.md): 维护产品边界、切片和验收。

## Active Tickets

- [T001 六语言入口与短文案切片](tickets/T001-multilingual-slice.md): completed, approved

## Decisions

- [研究结论](../research/multilingual-skill-research.md)
