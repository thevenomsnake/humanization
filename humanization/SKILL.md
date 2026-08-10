---
name: humanization
description: Write, revise, and audit whether prose, stories, documentation, product content, marketing copy, email, and GUI microcopy should appear in zh-CN, zh-TW, en, ja, ko, and es, optionally calibrating expression to a user-designated writing sample for the current task. Use an explicit locale, format, and surface to decide each message's user-facing job, preserve facts, sources, capabilities, privacy, CTA, brand terms, placeholders, ICU messages, variables, markup, and runtime structure, and apply native language rules.
---

# Humanization 3.0.0

先用通用契约判断候选信息是否属于当前表面，再读取一个语言档案和一个格式模块完成写作或改稿。不要自动猜测混合文本的 locale，也不要把某种语言的禁令提升为全局规则。

## 1. 确定输入

记录以下字段；缺失内容会改变事实、承诺或 CTA 时只问一个聚焦问题：

- `locale`: `zh-CN`、`zh-TW`、`en`、`ja`、`ko` 或 `es`；
- `format`: `prose`、`copy` 或 `web-microcopy`；
- `surface`: 文章、邮件、按钮、错误、空状态、确认、通知、页面或资源文件等真实表面；
- 受众、目的、渠道、已有材料和交付限制；
- 可选的 `author_sample`：用户明确指定用于当前任务表达校准的样本文字，并记录其 locale、format/surface 和正文边界；
- 公开文字的用户目标、决定点、当前状态和必须披露项；
- 现实、虚构或混合，以及现实内容的来源边界；
- 品牌词、不可翻译词、CTA、隐私/能力承诺；
- GUI 任务的源资源、key、placeholder、ICU、变量、markup 和运行时约束。

`web-microcopy` 是兼容保留的公开 format 名，实际覆盖所有 GUI 文案，不限于 HTML 或网页。

## 2. 按三层路由

### 通用层

始终读取 `references/core.md`。它是事实、来源、能力、隐私、CTA、品牌词、占位符、最小编辑和内容存在性判定的唯一规则来源。事实与能力账本约束公开文案，但不是公开文案目录。

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
- `copy`: 读取 `references/formats/expressive-text.md`，先判断信息是否值得出现在当前表面，再处理非 GUI 的文档、产品、营销、邮件和社交文字。
- `web-microcopy`: 读取 `references/formats/gui-microcopy.md`，按按钮、错误、空状态、确认、通知等组件处理文字并保护资源结构。

一段文字附着在控件或产品状态上时使用 `web-microcopy`，无论它存放在 HTML、JSON、YAML、ARB、PO、源码还是设计稿中。

## 3. 写作或改稿

1. 按 `core.md` 建立事实账本，并为每条候选信息判定 `keep`、`rewrite`、`move` 或 `remove`；候选文案暴露产品流程缺口时同时标记 `needs_product_decision`。
2. 用目标 locale 档案决定自然语序、语体、标点、地区词和节奏；有 `author_sample` 时，再按 `core.md` 的“任务内作者样本校准”匹配可观察的文字习惯。
3. 用选定的 format 模块完成文字表面的任务；组件职责不能替代存在性判定。
4. 只做必要改动；原文合格时返回 `no_change`，无用户职责的信息不要改写成另一段宣传文案。
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

脚本只阻断可证明的空输入、品牌词丢失、资源结构损坏、可访问名称缺失和 locale 专属硬规则。脚本不能判断候选信息是否有用户职责，也不能凭关键词决定文案是否应该存在。词汇、语气、翻译腔、节奏和信息价值只给人工或模型结合上下文判断。旧入口 `scripts/check_prose.py` 继续兼容 `zh-CN prose`。

## 5. 交付

交付作品或资源本身，并简短标出 `remove`、`move` 和相关的 `needs_product_decision` 及其原因、无法确认的事实或未运行的资源检查。`remove` 时明确说明没有公开文案，不强行补一条替代句；删除一句内部盘点不能代替修复它暴露的产品流程缺口。不要把内部能力盘点原样交给读者，也不要把 warning 写成作者身份判断。
