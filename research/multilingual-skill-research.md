# human-writing-general 研究结论

研究日期：2026-08-07

范围：只研究 `thevenomsnake/human-writing-general`、其上游、Skill 格式、语言标签和 Web microcopy 约束。未访问或修改 Sumimi、Cloudflare 或任何生产环境。

## 结论摘要

- 这个项目现在是上游中文 Skill 的 fork，不是已经完成的多语言 Skill。最小可用切片应先保住一个安装单元 `human-writing-general/`，把中文专属规则从全局规则移入 `zh-CN` 档案，再增加 `en` 档案和 Web microcopy 格式，最后用同一 CLI 入口显式接收 `locale` 与 `format`。
- 事实、能力边界、来源、虚构与现实分流、段落推进和品牌词一致性可作为跨语言核心。词序、标点、正式程度、机器翻译痕迹、套话与自然节奏不能用中文规则翻译后复用。
- 硬规则可以确定性检查；自然度、语气和文化适配必须留在语言档案，靠人工或模型审阅。脚本不应把“看起来像真人”伪装成通过/失败。

## 一手来源与当前仓库事实

### 上游结构、版本和许可证

GitHub API 将 `KKKKhazix/human-writing` 标记为公开、非 fork，描述为中文写作 Skill：[仓库 API](https://api.github.com/repos/KKKKhazix/human-writing)。上游 `v1.1.0` 的可复现提交是 `cd879d22c8588125c1869d0b443f5d8df74b4192`；固定引用应同时记录 tag 和 SHA：[不可变树](https://github.com/KKKKhazix/human-writing/tree/cd879d22c8588125c1869d0b443f5d8df74b4192)。

`human-writing/` 安装树包含 `SKILL.md`、`VERSION`、`agents/openai.yaml`、`references/`、`scripts/check_prose.py`、`dist/` 和 Skill 内许可证：[v1.1.0 目录](https://github.com/KKKKhazix/human-writing/tree/v1.1.0/human-writing)。入口仍声明 `name: human-writing`，description 和正文明确面向中文长文：[SKILL.md](https://github.com/KKKKhazix/human-writing/blob/cd879d22c8588125c1869d0b443f5d8df74b4192/human-writing/SKILL.md)。

根目录和 Skill 内的 `LICENSE` 都是 MIT；MIT 要求复制或 substantial portions 时保留版权声明和许可文本：[根许可证](https://github.com/KKKKhazix/human-writing/blob/cd879d22c8588125c1869d0b443f5d8df74b4192/LICENSE) 和 [Skill 许可证](https://github.com/KKKKhazix/human-writing/blob/cd879d22c8588125c1869d0b443f5d8df74b4192/human-writing/LICENSE)。因此 fork 应保留许可证、上游归属和可追踪同步记录，不要把规则重写成无来源的新作品。

本地检查确认：仓库为独立目录，`main` 跟踪 fork 的 `origin/main` 且工作树干净；没有 `upstream` remote。当前检查器只接收一个 `path`/标准输入，描述为中文成稿检查，不能接收 `locale` 或 `format`：[上游脚本](https://github.com/KKKKhazix/human-writing/blob/cd879d22c8588125c1869d0b443f5d8df74b4192/human-writing/scripts/check_prose.py)。fork 目前仍以 1.1.0 中文内容为基线，先改稳定标识并不等于完成国际化。

### Codex Skill 元数据和目录

OpenAI 官方文档规定 Skill 是一个目录，必须有 `SKILL.md`，其 front matter 必须含 `name` 和 `description`；`scripts/`、`references/`、`assets/` 和 `agents/openai.yaml` 均为可选：[Build skills](https://learn.chatgpt.com/docs/build-skills)。宿主先加载 name/description，再在命中后读完整 `SKILL.md`，所以 description 要简洁写清触发范围与边界。

官方文档列出的 `agents/openai.yaml` 可选字段包括 `interface.display_name`、`short_description`、图标、`brand_color`、`default_prompt`，以及 `policy.allow_implicit_invocation` 和工具依赖。稳定标识、目录名、front matter `name`、调用名和 default prompt 应统一为 `human-writing-general`；UI 显示名统一为 `Human Writing General`。仓库发布前应检查这些值没有残留 `$human-writing`。

Codex 的 repo 技能发现路径是当前目录到仓库根目录的 `.agents/skills`，用户级路径为 `$HOME/.agents/skills`。上游 README 的 `~/.agents/skills/human-writing/` 属于用户级安装约定；发行时仍应把完整 Skill 目录作为安装单元，而不是只复制一个 Markdown 文件。

## Locale 设计证据

### 标签和数据层

IETF BCP 47（RFC 5646）定义语言标签的结构、子标签和区域语义，并要求按需要选择足够精确的标签：[RFC 5646](https://www.rfc-editor.org/rfc/rfc5646.html)。因此首批键可以使用：

| 语言档案 | BCP 47 标签 | 实现含义 |
| --- | --- | --- |
| 简体中文 | `zh-CN` | 中国大陆简体中文规则；不能只由 `zh` 推断地区。 |
| 繁体中文 | `zh-TW` | 台湾繁体中文规则；用词、语气和标点单独维护，不能当作简繁转换。 |
| English | `en` | 语言中立英语；产品需要地区差异时再明确 `en-US`、`en-GB` 等。 |
| 日本語 | `ja` | 日语规则。 |
| 한국어 | `ko` | 韩语规则。 |
| Español | `es` | 西班牙语规则；地区差异另用显式区域标签。 |

Unicode CLDR 是 locale 数据的权威来源，提供语言/地区命名、格式、排序等机器可用数据：[CLDR 规范](https://cldr.unicode.org/index/cldr-spec) 和 [Unicode TR35](https://unicode.org/reports/tr35/)。CLDR 不是完整的散文风格指南；它能支撑 locale 选择和格式化，不能证明一段文案“自然”。

语言档案的规范入口应保持可替换，并以本地权威资料做人工校准：

- `zh-CN`：以中国国家标准《标点符号用法》GB/T 15834-2011 为标点基线；规则来源入口为国家标准全文公开系统 [openstd.samr.gov.cn](https://openstd.samr.gov.cn/)。
- `zh-TW`：台湾教育部《重訂標點符號手冊》提供繁中文稿的标点与用法基线：[教育部語文成果](https://language.moe.gov.tw/001/Upload/Files/site_content/M0001/hau/c2.htm)。
- `en`：美国政府 Digital.gov 的 Plain Language 指南可作为英语 Web/公共说明文字的清晰度基线：[Plain language](https://digital.gov/guides/plain-language/)。
- `ja`：日本文化庁国語課的《公用文作成の考え方》是官方日语公文写作参考；实现时应从文化庁国語施策页面固定具体版本，不把日语规则翻译成中文禁令。[文化庁国語施策](https://www.bunka.go.jp/seisaku/kokugo_nihongo/)。
- `ko`：韩国国立国語院的《한국어 어문 규범》是韩语拼写、分写和标点规范入口：[국립국어원 어문 규범](https://korean.go.kr/kornorms/main/main.do)。
- `es`：西班牙皇家学院（RAE）《Ortografía de la lengua española》是西班牙语正字法参考；地区用法需在档案中标明范围：[RAE Ortografía](https://www.rae.es/ortografia)。

这些资料适合定义“允许/不允许的标点、大小写、拼写、地区词和正式度边界”。机器翻译痕迹、套话密度和自然节奏不是这些标准的确定性结论，应由各语言档案给出正向例子和人工判断清单。

## Web microcopy 的可验证边界

短文案模式应与长文材料门槛分开：标题、导航、按钮、标签、状态、错误/空状态、隐私说明、`title`/`description`、Open Graph 和无障碍名称仍需事实与能力边界，但不需要“非虚构长文至少五件材料”或固定篇幅。

可落成确定性检查的规范事实：

| 内容 | 最小检查 | 一手规范 |
| --- | --- | --- |
| 页面语言 | HTML 根或片段有合法 `lang`，值与输入 locale 一致；混合片段可在局部覆盖。 | [WHATWG `lang`](https://html.spec.whatwg.org/multipage/dom.html#the-lang-and-xml:lang-attributes)，[RFC 5646](https://www.rfc-editor.org/rfc/rfc5646.html) |
| 页面标题/说明 | `<title>` 非空；`meta[name=description]` 有与页面事实相符的文本。长度只作为项目告警，不宣称标准硬阈值。 | [WHATWG `title`](https://html.spec.whatwg.org/multipage/semantics.html#the-title-element)，[WHATWG `meta`](https://html.spec.whatwg.org/multipage/semantics.html#the-meta-element) |
| Open Graph | 项目需要社交预览时检查 `og:title`、`og:type`、`og:image`、`og:url`，并在需要时检查 `og:description`；值必须来自同一事实/品牌词输入。 | [Open Graph protocol](https://ogp.me/) |
| 错误与表单 | 错误用文字识别；控件有可见标签/说明；可预见错误提供修正建议。 | [WCAG 2.2 3.3.1](https://www.w3.org/TR/WCAG22/#error-identification)、[3.3.2](https://www.w3.org/TR/WCAG22/#labels-or-instructions)、[3.3.3](https://www.w3.org/TR/WCAG22/#error-suggestion) |
| 按钮、标签、状态 | 每个交互控件的名称/角色/值可由辅助技术确定；动态状态消息不应只依赖视觉变化。 | [WCAG 2.2 4.1.2](https://www.w3.org/TR/WCAG22/#name-role-value)、[4.1.3](https://www.w3.org/TR/WCAG22/#status-messages) |
| 隐私承诺 | 只写产品实际能证明的收集、用途、保存和分享行为；说明要清晰、易取得，不能用“绝不”“完全安全”等无证据承诺。 | [GDPR 第 12 条](https://eur-lex.europa.eu/eli/reg/2016/679/oj#d1e2014-1-1)、[第 13 条](https://eur-lex.europa.eu/eli/reg/2016/679/oj#d1e2202-1-1) |

长度、按钮动词是否自然、错误语气是否合适、隐私文本是否让目标用户真正理解，不能仅靠正则判定。脚本最多报告空值、缺字段、非法 locale、未声明品牌词和超出能力声明的候选句。

## 最小纵向切片建议

1. 将 `human-writing/SKILL.md` 入口改为通用核心，保留现实/虚构/来源/能力边界；新增 `references/locales/{zh-CN,zh-TW,en,ja,ko,es}.md`，先完成 `zh-CN` 与 `en` 的正向规则，其余四个档案先写清规范来源、地区边界和待人工校准项。
2. 新增 `references/formats/web-microcopy.md`，定义输入契约：受众、页面/组件、事实、CTA、品牌词与不可翻译词、隐私/能力承诺、目标 locale；短格式绕过长文材料数量和篇幅门槛。
3. 把 `check_prose.py` 拆成最小 CLI：`python check_prose.py --locale zh-CN --format prose PATH`。第一步只保留通用事实/字段检查和 `zh-CN` 硬规则；`en` 先检查可验证的 Web 字段与明显结构问题。无 locale/format 时失败，不自动猜混合语言。
4. 保留原 MIT 文件与上游归属；配置 `upstream` remote 只用于同步，不改上游。发布 v2.0.0 时记录不可变 tag 对应 SHA，并让 `VERSION`、front matter `name`、目录名、UI display name 和 default prompt 全部一致。

### 不在首片实现的内容

不做五套中文规则翻译、不做自动“自然度评分”、不做逐句跨语言对齐、不接 Sumimi/Cloudflare/生产安装器。等六档案有真实样例和人工校准后，再扩大语言专属检测；等发布流程需要时，再增加固定 tag 安装与阻断逻辑。
