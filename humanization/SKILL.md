---
name: humanization
description: Write and revise prose, stories, documentation, product content, marketing copy, email, and GUI microcopy in zh-CN, zh-TW, en, ja, ko, and es. Use an explicit locale, format, and surface to preserve facts, sources, capabilities, privacy, CTA, brand terms, placeholders, ICU messages, variables, markup, and runtime structure while applying native language rules.
---

# Humanization 3.0.0

用一个通用契约、一个语言档案和一个格式模块完成写作或改稿。不要自动猜测混合文本的 locale，也不要把某种语言的禁令提升为全局规则。

## 1. 确定输入

记录以下字段；缺失内容会改变事实、承诺或 CTA 时只问一个聚焦问题：

- `locale`: `zh-CN`、`zh-TW`、`en`、`ja`、`ko` 或 `es`；
- `format`: `prose`、`copy` 或 `web-microcopy`；
- `surface`: 文章、邮件、按钮、错误、空状态、确认、通知、页面或资源文件等真实表面；
- 受众、目的、渠道、已有材料和交付限制；
- 现实、虚构或混合，以及现实内容的来源边界；
- 品牌词、不可翻译词、CTA、隐私/能力承诺；
- GUI 任务的源资源、key、placeholder、ICU、变量、markup 和运行时约束。

`web-microcopy` 是兼容保留的公开 format 名，实际覆盖所有 GUI 文案，不限于 HTML 或网页。

## 2. 按三层路由

### 通用层

始终读取 `references/core.md`。它是事实、来源、能力、隐私、CTA、品牌词、占位符和最小编辑的唯一规则来源。

### 语言层

只读取目标 locale 对应的一个档案；多语言交付才分别读取多个档案。语言档案只负责语序、敬语或语体、标点、地区词、翻译腔、模板信号和自然节奏：

- `references/locales/zh-CN.md`
- `references/locales/zh-TW.md`
- `references/locales/en.md`
- `references/locales/ja.md`
- `references/locales/ko.md`
- `references/locales/es.md`

中文长文需要细分文体时，由 `zh-CN.md` 继续路由到根目录的中文专属资料。其他 locale 不读取这些文件。

### 格式层

- `prose`: 按材料和文体组织长文，不套用 GUI 组件规则。
- `copy`: 读取 `references/formats/expressive-text.md`，处理非 GUI 的文档、产品、营销、邮件和社交文字。
- `web-microcopy`: 读取 `references/formats/gui-microcopy.md`，按按钮、错误、空状态、确认、通知等组件处理文字并保护资源结构。

一段文字附着在控件或产品状态上时使用 `web-microcopy`，无论它存放在 HTML、JSON、YAML、ARB、PO、源码还是设计稿中。

## 3. 写作或改稿

1. 按 `core.md` 建立不可变账本。
2. 用目标 locale 档案决定自然语序、语体、标点、地区词和节奏。
3. 用选定的 format 模块完成文字表面的任务。
4. 只做必要改动；原文合格时停手，歧义影响事实或行动时交还作者决定。
5. 跨语言只对齐事实、能力、隐私、CTA、品牌词和保护 token，不要求逐句直译或句数相同。

## 4. 做确定性校验

显式传入 locale 和 format：

```bash
python scripts/check_writing.py --locale zh-CN --format prose draft.md
python scripts/check_writing.py --locale es --format copy campaign.txt
python scripts/check_writing.py --locale en --format web-microcopy page.html
python scripts/check_writing.py --locale ja --format web-microcopy --source source.json target.json
```

可重复使用 `--brand-term TERM` 声明必须保留的品牌词。`--source` 提供 GUI 源资源后，检查器会比较 JSON/ARB key 与结构、HTML markup，以及常见 placeholder、ICU 参数、变量、URL 和转义；其他资源格式仍应运行项目自己的 parser 或 linter。

脚本只阻断可证明的空输入、品牌词丢失、资源结构损坏、可访问名称缺失和 locale 专属硬规则。词汇、语气、翻译腔和节奏只给人工判断 warning。旧入口 `scripts/check_prose.py` 继续兼容 `zh-CN prose`。

## 5. 交付

交付作品或资源本身，并简短标出无法确认的事实或未运行的资源检查。不要展示内部清单，也不要把 warning 写成作者身份判断。
