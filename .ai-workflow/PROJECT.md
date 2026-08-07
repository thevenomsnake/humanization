---
schema_version: 2
workflow_version: 0.10.0
status: active
project_name: "humanization"
---

# Humanization

## Product Direction

- Intended user: 使用 Codex Skill 写作、改稿和制作网站短文案的多语言用户。
- Problem: 中文长文规则不能直接用于英文、日文、韩文、西班牙文或台湾繁中，短文案也不应被长文材料门槛误伤。
- First value: 明确指定 `locale` 与 `format` 后，Skill 能按通用事实边界、文字反模板规则和对应语言档案生成或检查文章、产品内容和 web microcopy。
- Delivery: 可安装的 `humanization/` Skill 目录、语言档案、web microcopy 参考和确定性 CLI 校验器。
- Boundaries: 只修改本 fork；不触碰 Sumimi、Cloudflare、生产环境或自动发布；保留 MIT、上游归属和同步入口。

## Current State

Humanization 3.0.0 已完成稳定标识定稿。上游 1.1.0 中文 Skill 与 `kill-ai-slop` 文本子集已完成结构研究，全表达性文字入口、六语言文本反模板参考和 warning-only 校验已实现并通过定向 smoke；视觉反 slop 规则明确排除。

## Roles

- [project-lead](roles/project-lead.md): 维护产品边界、切片和验收。

## Active Tickets

- [T001 六语言入口与短文案切片](tickets/T001-multilingual-slice.md): completed, approved
- [T002 全表达性文字与文本反 slop](tickets/T002-expressive-text-antislop.md): completed, approved

## Decisions

- [研究结论](../research/multilingual-skill-research.md)
