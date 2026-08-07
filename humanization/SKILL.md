---
name: humanization
description: 用于 zh-CN、zh-TW、en、ja、ko、es 的所有表达性文字，包括文章、故事、文档、产品内容、营销文案、邮件和网页 GUI 文案；按明确的 locale 与 format 处理事实边界、语言自然度、文本反模板规则、品牌词、隐私和无障碍文本，不吸收视觉样式规则。
---

# Humanization 3.0.0

把作品写成有具体说话位置、事实边界和自然语言节奏的文字。先确定 `locale` 和 `format`，再读取对应档案；不自动把混合语言猜成一种规则。

## 1. 建立输入契约

在内部记下以下字段，缺少会改变事实或 CTA 的字段时只问一个聚焦问题：

- `locale`: `zh-CN`、`zh-TW`、`en`、`ja`、`ko` 或 `es`。
- `format`: `prose`、`copy` 或 `web-microcopy`。`copy` 是所有非长文表达性文字的通用模式，`web-microcopy` 专门校验 HTML/GUI 字段。
- `surface`: 文章、文档、产品页、按钮、错误、邮件等具体文字表面；没有特殊表面时写 `general`。
- 受众、目的、渠道、已有材料和交付长度。
- 现实、虚构或混合；现实内容的来源与用户亲历边界。
- 品牌词、不可翻译词、产品名称、CTA 和隐私/能力承诺。

## 2. 先守住通用核心

### 事实与能力

- 现实作品只使用用户提供或可核验的事实、数字、引语、过程和经历；不能把推测写成现场或亲历。
- 虚构作品可以创造人物、动作、对白和心理，但每个场景都要有目标、选择、关系、信息或后果的变化。
- 不虚构检索、工具调用、客户、用户反馈、指标、权限或交付能力。无法证明的承诺改成条件、范围或待确认事项。
- 材料不足时研究、提问或缩小题目。长篇的材料门槛只适用于 `prose`，不阻挡短文案。

### 推进与说话位置

- 先让读者知道谁在什么条件下说什么；把判断放在它的依据附近。
- 每段或每个文案单元增加事实、动作、区别、选择或后果；删掉只换说法的重复。
- 让语气服务于受众和渠道。用具体动词、名词和可核验的细节，少用空泛的营销承诺与模板化路标。
- 不要求逐句直译或句子数量一致。跨语言只保持受众、事实、能力边界、CTA、隐私承诺和品牌词一致。

### 文字反模板检查

所有格式都读取 `references/text/anti-slop.md`。它吸收 `kill-ai-slop` 中与文字有关的原则，检查口号式翻案、空泛的最高级形容词、三连节奏、装饰性强调、无来源数字、重复标题和抽象名词堆叠。命中只是复核线索，引用、用户内容、真实状态和有来源的数字保留；颜色、字体、布局、卡片、动效、图标和按钮样式不属于本 Skill。

## 3. 选择语言档案

只读取与目标 locale 对应的一个档案；混合交付才读取多个档案并分别检查。档案里包含本语言的标点、正式度、机器翻译痕迹、套话和节奏边界：

- `references/locales/zh-CN.md`
- `references/locales/zh-TW.md`
- `references/locales/en.md`
- `references/locales/ja.md`
- `references/locales/ko.md`
- `references/locales/es.md`
- `references/text/anti-slop.md`
- `references/formats/expressive-text.md`

中文长文的细分现实/虚构/改稿资料仍在 `references/` 根目录，仅在 `locale` 为 `zh-CN` 且任务命中相应文体时读取。它们不是通用规则。

## 4. 按格式分流

### `prose`

先确认现实材料或虚构许可，再按语言档案写初稿。长文初稿完成后再读取 `references/revision.md`（仅中文档案使用）并运行对应检查器。交稿只交作品和必要的事实来源，不展示内部清单。

### `copy`

读取 `references/formats/expressive-text.md`。用它处理文章之外的完整表达性文字，包括文档段落、产品说明、营销内容、邮件、社交内容和 GUI 字符串。长度和载体可以不同，事实、能力、品牌词和目标动作不能漂移。

### `web-microcopy`

先读取 `references/formats/web-microcopy.md`。标题、导航、按钮、标签、状态、错误/空状态、隐私说明、`title`、description、Open Graph 和无障碍名称各自承担一个动作。短文案不套用长文的字数或材料数量规则，但仍需事实、能力、品牌词和隐私边界。按钮和标签使用目标语言自然的短动词，不把英文逐词翻译成其他语言。

## 5. 做确定性校验

显式传入 locale 和 format；不要让脚本猜语言或格式：

```bash
python scripts/check_writing.py --locale zh-CN --format prose draft.md
python scripts/check_writing.py --locale es --format copy campaign.txt
python scripts/check_writing.py --locale en --format web-microcopy page.html
```

可以重复使用 `--brand-term TERM` 声明不可改写的品牌词；脚本只检查字段、标点和明确硬禁句，并对文本反模板信号给出人工判断警告，不自动判断自然度、能力或隐私承诺。自然度、幽默、地区语感和翻译质量留给对应语言档案的人工或模型判断。旧入口 `scripts/check_prose.py` 仍保留，用于旧中文调用。

## 6. 交付与一致性

交付前核对：目标 locale 明确，所有现实事实有来路，品牌词未被翻译，CTA 的动作和能力边界没有漂移，隐私文字没有超出实际行为，web 控件具备可识别名称。发现任一项不一致就先修正或标成待确认，不用另一种漂亮句式掩盖缺口。
