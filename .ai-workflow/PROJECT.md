---
schema_version: 2
workflow_version: 0.10.0
status: active
project_name: "humanization"
---

# Humanization

## Product Direction

- Intended user: 使用 Codex Skill 写作、改稿和制作网站短文案的多语言用户。
- Problem: 简体中文长文规则不能直接用于繁体中文、英文、日文、韩文或西班牙文，短文案也不应被长文材料门槛误伤。
- First value: 明确指定 `locale`、`format` 与 `surface` 后，Skill 按通用契约、一个语言档案和一个格式模块生成或检查文章、产品内容和 GUI microcopy。
- Delivery: 可安装的 `humanization/` Skill 目录、通用契约、六个语言档案、GUI microcopy 参考和确定性 CLI 校验器。
- Boundaries: 只修改本独立项目；不触碰 Sumimi、Cloudflare、生产环境或自动发布；保留 MIT 许可证与所有来源项目的逐项归属。

## Current State

Humanization 3.0.0 已完成稳定标识定稿，并已从 GitHub fork network 脱离为独立项目。运行时按通用契约、六个 locale 档案和 GUI microcopy 模块分层；确定性校验只阻断可证明的结构损坏，语言自然度信号保持 warning-only，视觉反 slop 规则明确排除。

## Roles

- [project-lead](roles/project-lead.md): 维护产品边界、切片和验收。

## Active Tickets

- [T001 六语言入口与短文案切片](tickets/T001-multilingual-slice.md): completed, approved
- [T002 全表达性文字与文本反 slop](tickets/T002-expressive-text-antislop.md): completed, approved
- [T003 Humanization 稳定标识与仓库重命名](tickets/T003-humanization-rename.md): completed, approved

## Decisions

- [研究结论](../research/multilingual-skill-research.md)
