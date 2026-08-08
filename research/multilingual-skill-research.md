# Humanization 研究结论

研究日期：2026-08-07；GitHub 横向比较补充于 2026-08-08

范围：研究 `thevenomsnake/humanization`、其上游、`kill-ai-slop` 文本子集、GitHub 上的多语言 humanizer/plain-language/l10n 项目、Skill 格式、语言标签和 Web microcopy 约束。未访问或修改 Sumimi、Cloudflare 或任何生产环境。

## 结论摘要

- 2026-08-07 的改造前基线只是上游中文 Skill 的 fork。当前 `3.0.0` 已完成一个安装单元、六个 locale、`prose/copy/web-microcopy` 分流和显式 `locale/format` CLI；这只是架构纵向切片，六份语言档案仍需要本地规则与样例校准。
- 事实、能力边界、来源、虚构与现实分流、段落推进和品牌词一致性可作为跨语言核心。词序、标点、正式程度、机器翻译痕迹、套话与自然节奏不能用中文规则翻译后复用。
- 硬规则可以确定性检查；自然度、语气和文化适配必须留在语言档案，靠人工或模型审阅。脚本不应把“看起来像真人”伪装成通过/失败。

## 一手来源与当前仓库事实

### 上游结构、版本和许可证

GitHub API 将 `KKKKhazix/human-writing` 标记为公开、非 fork，描述为中文写作 Skill：[仓库 API](https://api.github.com/repos/KKKKhazix/human-writing)。上游 `v1.1.0` 的可复现提交是 `cd879d22c8588125c1869d0b443f5d8df74b4192`；固定引用应同时记录 tag 和 SHA：[不可变树](https://github.com/KKKKhazix/human-writing/tree/cd879d22c8588125c1869d0b443f5d8df74b4192)。

`human-writing/` 安装树包含 `SKILL.md`、`VERSION`、`agents/openai.yaml`、`references/`、`scripts/check_prose.py`、`dist/` 和 Skill 内许可证：[v1.1.0 目录](https://github.com/KKKKhazix/human-writing/tree/v1.1.0/human-writing)。入口仍声明 `name: human-writing`，description 和正文明确面向中文长文：[SKILL.md](https://github.com/KKKKhazix/human-writing/blob/cd879d22c8588125c1869d0b443f5d8df74b4192/human-writing/SKILL.md)。

根目录和 Skill 内的 `LICENSE` 都是 MIT；MIT 要求复制或 substantial portions 时保留版权声明和许可文本：[根许可证](https://github.com/KKKKhazix/human-writing/blob/cd879d22c8588125c1869d0b443f5d8df74b4192/LICENSE) 和 [Skill 许可证](https://github.com/KKKKhazix/human-writing/blob/cd879d22c8588125c1869d0b443f5d8df74b4192/human-writing/LICENSE)。因此 fork 应保留许可证、上游归属和可追踪同步记录，不要把规则重写成无来源的新作品。

改造前本地检查确认：仓库为独立目录，`main` 跟踪 fork 的 `origin/main`，当时没有 `upstream` remote；上游检查器只接收一个 `path`/标准输入，描述为中文成稿检查，不能接收 `locale` 或 `format`：[上游脚本](https://github.com/KKKKhazix/human-writing/blob/cd879d22c8588125c1869d0b443f5d8df74b4192/human-writing/scripts/check_prose.py)。截至 2026-08-08，本地仓库已配置 `upstream`，当前版本为 `3.0.0`，上述 1.1.0 状态只保留为历史基线。

### Codex Skill 元数据和目录

OpenAI 官方文档规定 Skill 是一个目录，必须有 `SKILL.md`，其 front matter 必须含 `name` 和 `description`；`scripts/`、`references/`、`assets/` 和 `agents/openai.yaml` 均为可选：[Build skills](https://learn.chatgpt.com/docs/build-skills)。宿主先加载 name/description，再在命中后读完整 `SKILL.md`，所以 description 要简洁写清触发范围与边界。

官方文档列出的 `agents/openai.yaml` 可选字段包括 `interface.display_name`、`short_description`、图标、`brand_color`、`default_prompt`，以及 `policy.allow_implicit_invocation` 和工具依赖。稳定标识、目录名、front matter `name`、调用名和 default prompt 应统一为 `humanization`；UI 显示名统一为 `Humanization`。仓库发布前应检查这些值没有残留 `$human-writing-general`。

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

## 最小纵向切片建议（已由 3.0.0 实现的历史方案）

以下四项记录 2026-08-07 的实现决策，不再代表待办：

1. 将 `human-writing/SKILL.md` 入口改为通用核心，保留现实/虚构/来源/能力边界；新增 `references/locales/{zh-CN,zh-TW,en,ja,ko,es}.md`，先完成 `zh-CN` 与 `en` 的正向规则，其余四个档案先写清规范来源、地区边界和待人工校准项。
2. 新增 `references/formats/web-microcopy.md`，定义输入契约：受众、页面/组件、事实、CTA、品牌词与不可翻译词、隐私/能力承诺、目标 locale；短格式绕过长文材料数量和篇幅门槛。
3. 把 `check_prose.py` 拆成最小 CLI：`python check_writing.py --locale zh-CN --format prose PATH`。第一步只保留通用事实/字段检查和 `zh-CN` 硬规则；`en` 先检查可验证的 Web 字段与明显结构问题。无 locale/format 时失败，不自动猜混合语言。
4. 保留原 MIT 文件与上游归属；配置 `upstream` remote 只用于同步，不改上游。发布时记录不可变 tag 对应 SHA，并让 `VERSION`、front matter `name`、目录名、UI display name 和 default prompt 全部一致。

### 不在首片实现的内容

不做五套中文规则翻译、不做自动“自然度评分”、不做逐句跨语言对齐、不接 Sumimi/Cloudflare/生产安装器。等六档案有真实样例和人工校准后，再扩大语言专属检测；等发布流程需要时，再增加固定 tag 安装与阻断逻辑。

## `kill-ai-slop` 文本融合研究

本地已读取已安装的 `kill-ai-slop` Skill 及其 `taxonomy.md`、`detection.md`、`fixes.md`。原 Skill 将“具体胜过口号”、先删减、确认语境再判断，以及复制层的三类信号列为核心，尤其是 AI copywriting voice、装饰性关键词强调和 emoji 泛滥。它还明确把扫描命中视为线索，不是自动判决，并允许按语言加载额外规则。

本次只吸收文本原则，排除颜色、字体、布局、卡片、圆角、动效、图标、按钮样式和视觉扫描器。文本原则已改写为适用于文章、文档、产品内容、营销文案、邮件、社交内容和 GUI 文案的通用参考，再由六个 locale 档案处理本语言的模板句、语气和机器翻译痕迹。

来源仓库：[yetone/kill-ai-slop](https://github.com/yetone/kill-ai-slop)，其 API 元数据标注为 Apache License 2.0：[仓库 API](https://api.github.com/repos/yetone/kill-ai-slop)，许可证原文：[LICENSE](https://github.com/yetone/kill-ai-slop/blob/main/LICENSE)。本 fork 不复制其脚本或视觉规则，新增参考文件会注明这是经过范围缩减和多语言改写的文本适配。

## GitHub 多语言写作实践比较

本节只比较公开仓库中的原始规则文件，不把仓库的自我宣传或检测分数当作语言质量证据。活跃度只记录能从 GitHub 提交记录直接看到的最近提交日期，未把 star 数当作质量指标。

### 英文 plain-language 与 technical-writing

#### Google `styleguide`

- 仓库/维护者/许可：Google 维护的开源项目风格指南，默认分支为 `gh-pages`；文档指南入口是 [`docguide/README.md`](https://github.com/google/styleguide/blob/gh-pages/docguide/README.md)，仓库许可证文件标为 Creative Commons Attribution 3.0：[LICENSE](https://github.com/google/styleguide/blob/gh-pages/LICENSE)。提交流显示最近一次更新为 2026-06-03 的 C++ 指南修改：[commit](https://github.com/google/styleguide/commit/1809c769de31ba388c755ad15dd057a9ba8531fd)。
- 可借鉴机制：[`best_practices.md`](https://github.com/google/styleguide/blob/gh-pages/docguide/best_practices.md) 要求最小而准确的文档、文档和代码同一变更更新、删除过时/重复文档；[`style.md`](https://github.com/google/styleguide/blob/gh-pages/docguide/style.md) 把标题、段落、列表、链接、代码块和可移植纯文本写成可执行规则。
- 不可直接搬用：这是英文工程文档/Markdown 规范，不能把英文标题大小写、80 列、Markdown 排版或英文句法变成六种语言的散文禁令。CC BY-3.0 的原文或示例也不能脱离归属要求直接复制。

#### Microsoft `microsoft-style-guide`

- 仓库/维护者/许可：MicrosoftDocs 维护，许可证为 CC BY 4.0：[README](https://github.com/MicrosoftDocs/microsoft-style-guide/blob/main/README.md)、[LICENSE](https://github.com/MicrosoftDocs/microsoft-style-guide/blob/main/LICENSE)。提交流最后更新时间为 2024-11-13：[commit](https://github.com/MicrosoftDocs/microsoft-style-guide/commit/c6945c32294e845a84b192a094fb1b7c2c452a6a)，仓库页面已标记为 archived，后续采用前应核对是否有替代文档。
- 可借鉴机制：[`brand-voice-above-all-simple-human.md`](https://github.com/MicrosoftDocs/microsoft-style-guide/blob/main/styleguide/brand-voice-above-all-simple-human.md) 将 voice 拆成语气和上下文，强调 warm、crisp、helpful；[`top-10-tips-style-voice.md`](https://github.com/MicrosoftDocs/microsoft-style-guide/blob/main/styleguide/top-10-tips-style-voice.md) 给出“先说重点、像人说话、少词、便于扫描、术语和大小写一致”的前后对照。
- 不可直接搬用：这些是 Microsoft 产品语境的英文品牌声音和术语库，不是通用英语，也不能把 contractions、Oxford comma、英文句末标点或其品牌承诺推到 `ja`/`ko`/`zh-TW`/`es`。

### 本地化规则如何处理语言差异

Mozilla 的 [`mozilla-l10n/styleguides`](https://github.com/mozilla-l10n/styleguides) 是一个由 Mozilla 本地化社区维护的规则库。仓库 README 说明默认按文件头以 CC BY-SA 4.0 发布，[LICENSE.md](https://github.com/mozilla-l10n/styleguides/blob/main/LICENSE.md) 要求复用前核对具体文件；最近一次可见主分支提交是 2025-12-19 的 mdBook/Actions 更新：[commit](https://github.com/mozilla-l10n/styleguides/commit/50ad513b1fe0c67d10cc9ade5a5ef8078153889b)。以下结论都来自该仓库的 locale 文件。

#### `ja` 日文

- [`docs/ja/l10nguideline.md`](https://github.com/mozilla-l10n/styleguides/blob/main/docs/ja/l10nguideline.md) 明确反对逐词翻译，要求按日语语序重排、删除英语中必须但日语可省略的主语，并按菜单、按钮、tooltip、checkbox 等组件分别决定体言止め、动词和句点。默认使用 `ですます`，术语、片假名长音、全角日文标点、日英之间空格都有独立规则。
- [`docs/ja/editorialguideline.md`](https://github.com/mozilla-l10n/styleguides/blob/main/docs/ja/editorialguideline.md) 还把 `Web`、数字、单位、引号、三点リーダー、ダッシュ和正式度拆成可查表的编辑规则。
- 可借鉴：按组件定义短文案形态，并把“直译痕迹”写成源语言到目标语言的动作规则；不可搬用：`ですます`、全角标点、日英空格、日文长音和允许使用 U+2014 的规定只对日语 profile 成立，不能覆盖中文的全局规则。

#### `ko` 韩文

- [`docs/ko/README.md`](https://github.com/mozilla-l10n/styleguides/blob/main/docs/ko/README.md) 要求合쇼체敬语，句末有句点时写完整句、没有句点时使用名词短语；品牌、变量和占位符不翻译；术语变更要考虑多产品影响；明确提醒不要直接复制机器翻译，也要避免日式翻译腔。
- 可借鉴：为组件和句末形态建立 profile 级规则，保留品牌/变量/占位符保护和术语变更影响检查；不可搬用：韩语敬语、助词和句末规则不适用于其他语言，也不能当成一般散文的硬规则。

#### `zh-TW` 繁体中文（台湾）

- [`docs/zh-TW/README.md`](https://github.com/mozilla-l10n/styleguides/blob/main/docs/zh-TW/README.md) 说明该指南由 MozTW 维护，要求使用台湾常用词（例如「網路」而非「互聯網」）、避免机器翻译、允许为文化和语境调整顺序或删减；它还规定品牌/硬编码字符串保护、中英半角空格、句尾半角冒号、参数顺序、字符串截断和日期时间 QA。
- 可借鉴：把地区词、品牌词、占位符、长度/截断和格式化检查放进 `zh-TW` 档案，并让“译文不自然”触发人工校阅而不是自动替换；不可搬用：`您`、半角冒号、Mozilla/SUMO slug 和产品术语属于该产品语境，不应成为所有繁中文案的全局禁令。

#### `es` 西班牙语

- [`docs/es/README.md`](https://github.com/mozilla-l10n/styleguides/blob/main/docs/es/README.md) 将国际西语拆成 Firefox 与 SUMO 两份指南；[`docs/es/ff.md`](https://github.com/mozilla-l10n/styleguides/blob/main/docs/es/ff.md) 规定对用户使用 `tú`、UI 和标题只大写首词、避免不必要 anglicism、产品标签保持统一。
- 可借鉴：locale 档案应明确读者称呼、标题大小写、术语表和地区变体；不可搬用：`tú`、Firefox 标签和特定产品的标点替换不能推成所有西语（例如 `es-ES`/`es-AR`）的唯一答案。

### 可复用的 AI-copy / anti-slop Skill

#### ehmo `slopkit` / `slopbeth`

- 仓库/维护者/许可/活跃度：`ehmo/slopkit` 由 ehmo 维护，许可证文件为 MIT：[仓库](https://github.com/ehmo/slopkit)、[LICENSE](https://github.com/ehmo/slopkit/blob/main/LICENSE)；主分支最近可见提交为 2026-07-22 的 `slopkit 1.4.1`：[commit](https://github.com/ehmo/slopkit/commit/b33718bb9283c11b09567dc714f92d90ffb7bd16)。可复用 Skill 原文在 [`skills/slopbeth/SKILL.md`](https://github.com/ehmo/slopkit/blob/main/skills/slopbeth/SKILL.md)。
- 可借鉴机制：先锁定实体、数字、日期、URL、引语和不确定性；材料不足时进入 evidence-bound mode，不填充功能、指标或经历；按模式簇诊断而不是逐个禁词；执行“先删模式、再检查是否变成无声公式文”的两遍流程；脚本结果只作信号，不能声称 detector-proof 或永久像人。
- 不可搬用：其规则和示例几乎全是英语，em dash、`delve`、Orwell 规则及英文节奏不应复制到六语言全局层；项目自带 benchmark/分数是其自身证据，不能当作跨语言质量证明。MIT 允许复用代码/规则，但仍需保留归属和许可证。

#### gabelul `slopbuster`（备选规则库）

- 仓库/维护者/许可/活跃度：`gabelul/slopbuster` 由 gabelul 维护，仓库和 Skill 声明 MIT：[README](https://github.com/gabelul/slopbuster/blob/main/README.md)、[`SKILL.md`](https://github.com/gabelul/slopbuster/blob/main/SKILL.md)；主分支最近可见提交为 2026-07-21：[commit](https://github.com/gabelul/slopbuster/commit/8215cbfc9723a52696fb493bd66059663b43c750)。
- 可借鉴机制：把 text、code、academic 分成显式模式；规则按 Tier 1/2/3 加权；先扫描再二次改写；支持 `--score-only`；README 明确说补具体内容不能编造事实，要把缺证据处列为人工复核。
- 不可搬用：152 条模式主要针对英语词汇/标点，目标分数和“human-ness”量表是项目自报；不要把英文词表、em dash 集群或 8+ 阈值变成 `zh-CN`、`ja`、`ko`、`es` 的硬验收。

## 对 Humanization 的最小改进建议

### 证据支持的改进

1. 保留一个跨语言 evidence-bound 核心：锁定事实、实体、数字、URL、引用和不确定性；缺材料输出 proof gap/追问，不用重写填空。依据 `slopbeth` 的 [Workflow/Hard rules](https://github.com/ehmo/slopkit/blob/main/skills/slopbeth/SKILL.md)、Google 的 [minimum viable documentation](https://github.com/google/styleguide/blob/gh-pages/docguide/best_practices.md) 和现有 `reality.md`。
2. 每个 locale 档案增加“组件形态 + 术语/品牌/占位符 + QA”小节。Mozilla 的 `ja`、`ko`、`zh-TW`、`es` 文件都按组件或地区明确规则，这比翻译一份中文禁词表可复用。
3. 让 `locale` 与 `format` 成为显式输入，并把硬检查限定为占位符/实体/字段/标点/长度和未声明术语；slopbeth 与 slopbuster 都把脚本当信号、把自然度留给人工复核。
4. 保留第三方许可证和归属，先提炼机制再改写示例。Google 的 CC BY-3.0、Microsoft 的 CC BY-4.0、Mozilla 的文件级 CC BY-SA 4.0/例外、slopkit/slopbuster 的 MIT 条款都要求按各自许可处理，不能整段复制后混入 MIT。

### 推断性建议（需后续样例验证）

- 先为六个 locale 各写一组同事实的 Web microcopy fixture（标题、按钮、错误、空状态、隐私说明），再用本地规则做人工双语审阅；这是从 Mozilla 的组件规则推断出的最低验证成本，不是任何仓库声明的标准。
- 把“反直译”“不加证据”“不换同义词掩盖重复”“两遍审稿”作为通用动作，把禁词、标点和敬语留在 locale profile；这是综合 Google/Mozilla/slopbeth 后的架构推断，不能替代目标语言母语审校。
- 当前不应引入统一的 AI-slop 分数或跨语言阈值。不同语言的句法、标点和自然重复差异太大；先记录规则命中、保留/删除事实和人工结论，等每个 locale 有真实样本后再决定是否需要统计指标。

## 补充搜索：语言原生 Humanizer 与多语言方案

2026-08-08 又以 GitHub repository search、code tree 和原始 `SKILL.md` 扩大搜索。筛选标准不是 star 数，而是仓库是否公开语言规则、编辑边界、检查脚本或评估材料。以下链接固定到本次读取的提交，避免以后 `main` 漂移。

| 语言/类型 | 代表仓库 | 本次读取重点 |
| --- | --- | --- |
| 英语通用 humanizer | [`blader/humanizer`](https://github.com/blader/humanizer/tree/523374dee72d67c7b2b5f858ea0094ffda49c3ac) | 信息保留、voice calibration、模式目录和硬禁令。 |
| 英语编辑/诊断 | [`petergyang/no-ai-slop`](https://github.com/petergyang/no-ai-slop/tree/d30eddb9e04562234f2070b5ee63ca4649d9a05e) | 最小有效改动、编辑与诊断分流、拒绝猜测作者是否用了 AI。 |
| 日语写作系统 | [`coji/natural-japanese`](https://github.com/coji/natural-japanese/tree/b54954f8deb4f110f0959f4e4fac295708900120) | 文档类型、日语 lint、语料误报校正、生成前约束。 |
| 日语 anti-slop | [`iKora128/stop-ai-slop-jp`](https://github.com/iKora128/stop-ai-slop-jp/tree/e09d32796f253a62693885757cea484c275d06f2)、[`chezou/slop-nuki`](https://github.com/chezou/slop-nuki/tree/1bdf627b5991f4f806069619c9bde407960feac7) | 书写者立场、敬语、业务场景与 register 保护。 |
| 日语产品本地化 | [`RobTar97/japanese-writing-skills`](https://github.com/RobTar97/japanese-writing-skills/tree/e4b1700464219c60da786f005a061bccffbbd4e3) | UI 组件职责、占位符/ICU/资源结构保护和渲染 QA。 |
| 韩语 humanizer | [`dotoricode/korean-humanizer`](https://github.com/dotoricode/korean-humanizer/tree/7dff5b48cc06fc4252d4766b802ecd61e62c50ad)、[`HarryJhin/korean-writing`](https://github.com/HarryJhin/korean-writing/tree/e4db3883ed76521b7a0cac30392fa67d182cc8ab) | 终结语尾、敬语等级、主语省略、英日翻译腔与确定性检查边界。 |
| 越南语 | [`longhang2004/vietnamese-humanizer`](https://github.com/longhang2004/vietnamese-humanizer/tree/611c6e9ed911897c8febffc056d62543d76ea411) | pattern 数据、register、保留契约、人工 benchmark 和不判作者来源。 |
| 俄语 | [`smixs/humanizer-ru`](https://github.com/smixs/humanizer-ru/tree/91f70df11f7fb30722e6fcf18803d402e2d86a53) | 俄语官样文、格链、动词化、聊天机器人复制残留与 ERROR/WARN 分级。 |
| 捷克语 | [`nowork-ai/anti-ai-slop-cz`](https://github.com/nowork-ai/anti-ai-slop-cz/tree/5efb11a03a064e8e31e46f29c46e6c1a8ce94b1a) | 捷克语公开文案、LinkedIn 套路、具体性与准确性。 |
| 七语言并列包 | [`White-Wolf-dv/Natural-Writing-Skills-Claude`](https://github.com/White-Wolf-dv/Natural-Writing-Skills-Claude/tree/d6d55b7cb60fccee67c08cce225ca9d8a3406663) | `fa/en/ar/es/he/it/fr` 独立安装包，但共享同一组九类模式。 |
| 四语言统一系统 | [`devswha/patina`](https://github.com/devswha/patina/tree/9cbfc7873b71efca7cf117f10412b4c481810d34) | `ko/en/zh/ja` pattern pack、document type/persona/register 三轴和意义保留门。 |
| 台灣繁中 | [`bruce6731/anti-ai-writing-taiwan`](https://github.com/bruce6731/anti-ai-writing-taiwan/tree/2c14f6a6015885b0c1cad9b54c861bc7b8a3b27d) | 台灣读者语感、最小编辑和繁中独立边界。 |

### 真正可跨语言的是编辑契约，不是禁词表

`blader/humanizer` 的 [`SKILL.md`](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md) 要求保留每项原始信息、不创造事实，并在用户给出样本时让样本优先于内置风格规则。`petergyang/no-ai-slop` 的 [`SKILL.md`](https://github.com/petergyang/no-ai-slop/blob/d30eddb9e04562234f2070b5ee63ca4649d9a05e/skills/no-ai-slop/SKILL.md) 把编辑和只诊断分开，强调最小有效改动，并明确不猜作者是否使用 AI。越南语 [`humanizer-vi`](https://github.com/longhang2004/vietnamese-humanizer/blob/611c6e9ed911897c8febffc056d62543d76ea411/skills/humanizer-vi/SKILL.md) 同样锁定数字、名称、引用、条件、例外、立场、术语和确定程度，禁止把“可能”改成“必然”。

这三种语言得到的共同核心很窄，也很稳定：先识别受众、目的和 register；锁定事实与行动；只改真正影响理解或语气的部分；原文自然时允许 `no_change`；规则命中不能变成作者归因。Humanization 现有的事实、能力、隐私、CTA 与品牌词核心符合这个方向。

越南语项目还把交付结果分成 `clean_rewrite`、`review_comment`、`needs_author_decision` 和 `no_change`；见其 [`evaluation-methodology.md`](https://github.com/longhang2004/vietnamese-humanizer/blob/611c6e9ed911897c8febffc056d62543d76ea411/docs/evaluation-methodology.md)。这比“每次都必须重写”可靠：歧义会改变事实或行动时应询问作者，原文合格时应停手。

### 日语与韩语证明“更直接”不是通用答案

[`slop-nuki`](https://github.com/chezou/slop-nuki/blob/1bdf627b5991f4f806069619c9bde407960feac7/skills/slop-nuki/SKILL.md) 直接指出，把英语 stop-slop 的“越直接越简洁”照搬到日语，会一起删掉敬语、缓冲语和必要配虑，使商务文字失礼。它按外部邮件、道歉、催促、拒绝、内部 Slack、会议记录等场景分别保留不同程度的敬语。`stop-ai-slop-jp` 的 [`SKILL.md`](https://github.com/iKora128/stop-ai-slop-jp/blob/e09d32796f253a62693885757cea484c275d06f2/SKILL.md) 则把书写者立场、反证可能性和主体缺失放在标点、偏爱词之前。

韩语方案也不是把英语主动语态规则翻译一次。`dotoricode/korean-humanizer` 的 [`SKILL.md`](https://github.com/dotoricode/korean-humanizer/blob/7dff5b48cc06fc4252d4766b802ecd61e62c50ad/SKILL.md) 把 `합니다`、`해요`、`다` 和口语终结语尾按领域保护；其可取之处是先保留原有敬语等级和品牌声口。它同时规定“最多改 20% 句子”“输出不得短于 90%”等任意配额，这些没有跨语言证据，不应吸收。`HarryJhin/korean-writing` 的 [`SKILL.md`](https://github.com/HarryJhin/korean-writing/blob/e4db3883ed76521b7a0cac30392fa67d182cc8ab/skills/writing-korean/SKILL.md) 区分了可由 hook 检查的双重被动/残留符号与需要上下文判断的主语省略、翻译腔和句尾分布；其 [`theory-korean.md`](https://github.com/HarryJhin/korean-writing/blob/e4db3883ed76521b7a0cac30392fa67d182cc8ab/skills/writing-korean/references/theory-korean.md) 也承认部分二手数值未在该文件中直接核对，因此这些数字不能直接成为 Humanization 的规则依据。

### GUI 文案需要资源契约，不只是“按钮写短一点”

`japanese-product-localization` 的 [`SKILL.md`](https://github.com/RobTar97/japanese-writing-skills/blob/e4b1700464219c60da786f005a061bccffbbd4e3/skills/japanese-product-localization/SKILL.md) 先锁定 surface、component、user goal、action、consequence 和现有术语，再写日语。其 [`interface-copy-patterns.md`](https://github.com/RobTar97/japanese-writing-skills/blob/e4b1700464219c60da786f005a061bccffbbd4e3/skills/japanese-product-localization/references/interface-copy-patterns.md) 按按钮、校验、错误、破坏性确认、空状态和通知分别定义任务；[`resource-integrity-and-qa.md`](https://github.com/RobTar97/japanese-writing-skills/blob/e4b1700464219c60da786f005a061bccffbbd4e3/skills/japanese-product-localization/references/resource-integrity-and-qa.md) 保护 key、placeholder、ICU branch、markup、link、escape、权限、金额和不可逆后果。

这比统一规定“按钮必须是短动词”可靠。Mozilla 日语指南甚至按组件给出不同形态：窗口标题和菜单通常用体言，按钮可用简洁体言，checkbox 多用动词；见 [`docs/ja/l10nguideline.md`](https://github.com/mozilla-l10n/styleguides/blob/main/docs/ja/l10nguideline.md)。因此 GUI 模式应先定义组件职责和运行时不变量，再由 locale 档案选词与句形。

### 确定性检测最容易在“像人”这件事上过度自信

`coji/natural-japanese` 的价值不只在规则数量，而在它公开记录误报。其 [`antithesis-recalibration.md`](https://github.com/coji/natural-japanese/blob/b54954f8deb4f110f0959f4e4fac295708900120/corpus/reports/antithesis-recalibration.md) 显示，仅按“否定后转肯定”绝对出现次数判断时，quality-high 人类文本命中率为 23.5%，AI 文本反而只有 11.8%；改用文档内密度和 genre 后才减少误报。其 [`business-fp-check.md`](https://github.com/coji/natural-japanese/blob/b54954f8deb4f110f0959f4e4fac295708900120/corpus/reports/business-fp-check.md) 也记录政府/白皮书中重复句首、低词汇多样性和翻译腔检测会大量误报。

俄语 [`scripts/lint.py`](https://github.com/smixs/humanizer-ru/blob/91f70df11f7fb30722e6fcf18803d402e2d86a53/scripts/lint.py) 值得借鉴的是把聊天机器人复制残留、占位符和少数硬错误列为 `ERROR`，把词汇、节奏、emoji 和抽象表达列为 `WARN`。其 [`SKILL.md`](https://github.com/smixs/humanizer-ru/blob/91f70df11f7fb30722e6fcf18803d402e2d86a53/SKILL.md) 还要求改稿后保留 CTA、offer、deadline、link 和 contact，这正是短文案不能被“删水分”一起删掉的功能契约。不过该 linter 又把长破折号、数学符号和部分否定对比列为全局 `ERROR`，也没有完整屏蔽引语，与 Skill 要求保留引语的规则存在冲突，不能照搬。

越南语项目的 [`architecture.md`](https://github.com/longhang2004/vietnamese-humanizer/blob/611c6e9ed911897c8febffc056d62543d76ea411/docs/architecture.md) 更保守：YAML 记录 `finding_type`、`scope`、`aggregation` 和 false-positive risk，regex 只指出位置，不自动重写，也不生成 AI score。

因此以下内容不能作为跨语言硬失败：破折号、冒号、主动/被动、无生物主语、三项列表、否定对比、句长均匀、词汇多样性或某个所谓 AI 偏爱词。可以硬失败的范围应接近 placeholder/markup 损坏、非法 locale/format、明确未填槽位、复制残留、品牌词破坏和项目自己声明的资源不变量。

### 多语言项目的两种架构，只有一种真正完成分层

`Natural-Writing-Skills-Claude` 的 [README](https://github.com/White-Wolf-dv/Natural-Writing-Skills-Claude/blob/d6d55b7cb60fccee67c08cce225ca9d8a3406663/README.md) 为波斯语、英语、阿拉伯语、西班牙语、希伯来语、意大利语和法语分别打包，但明确说明七包共享同一组九类 pattern。西班牙语包把同样的 generic descriptors、summary phrases、rigid structure、vague attribution 和 `no X, sino Y` 翻成西语，并要求固定混合“culto/literario”与口语 register。它证明独立目录不等于语言原生设计；没有地区、体裁和受众证据时，强制混合 register 仍会制造新的模板。

`patina` 的 [`SKILL.md`](https://github.com/devswha/patina/blob/9cbfc7873b71efca7cf117f10412b4c481810d34/SKILL.md) 则显式选择 `ko/en/zh/ja` pattern pack，并把 Document Type、Persona、Register 设为互不推断的三轴；其 [`ARCHITECTURE.md`](https://github.com/devswha/patina/blob/9cbfc7873b71efca7cf117f10412b4c481810d34/docs/ARCHITECTURE.md) 区分确定性测量与模型改写，并用 claim、number、polarity、causation 的意义保留门约束改写。这套思路与 Humanization 的 `locale + format + input contract` 相容，但 184 patterns、stylometry、persona 系统、CLI/Web 双引擎和分数门远超当前需要。它还会对两句以内文本跳过语义 anchor/MPS，HTML 模式不改按钮和导航，不能直接承担 GUI microcopy。应吸收字段所有权和意义保留，不复制整套平台。

### 对当前六个 locale 档案的研究审计

以下只是研究结论，本轮不改产品文件：

- `en.md` 的 plain-language、事实和具体动词方向成立，但禁词与主动语态只能是语境提示；英文人类写作会正常使用 em dash、被动和无生物主语。
- `ja.md` 目前写“按钮或标签用短动词”过于单一。Mozilla 和日语产品本地化 Skill 都按组件决定体言、动词、句点、敬语和目的语，下一轮应改为组件矩阵。
- `ko.md` 目前写“主语和行动放前面”会误伤自然省略。应改为先识别行文者、受事和结果，只有责任或恢复动作不清时才显式补主体；终结语尾、敬语等级和助词/占位符才是韩语档案的核心。
- `es.md` 的“中性西语”只能是未指定地区时的保守回退。西语产品必须显式决定 `tú/usted/ustedes`、地区词和品牌术语；`no solo... sino...`、冒号和破折号不能成为硬禁令。
- `zh-TW.md` 已经独立处理台灣用词，这是正确方向；但“避免破折号和提示性冒号”仍带有上游中文硬禁令痕迹。MozTW 自己要求某些 UI 句尾使用半角冒号，说明标点必须按组件和产品约定处理，不能在整个 locale 禁止。
- `anti-slop.md` 当前把各语言的否定对比、企业词和三连节奏定义为人工复核线索，而不是硬失败，这一层级应保留。下一轮重点应是减少跨语言示例的“机械对译感”，把实际句法交回 locale 文件。

## 本轮研究后的取舍

1. 不引入统一“人味分数”、跨语言 stylometry、作者归因或 detector-bypass 承诺。
2. 通用核心只保留事实、来源、能力、隐私、CTA、品牌/术语、placeholder/markup 和最小编辑契约。
3. `web-microcopy` 增加组件职责与资源不变量；具体语气、词形、标点、敬语和地区词留给 locale。
4. 硬检查只覆盖可证明的破坏，风格 pattern 默认 warning，并允许引用、品牌、体裁和自然人样本覆盖。
5. 下一次实现前先做六语言同事实 fixture 与母语/高质量本地规则审阅；当前研究不能替代这种验证。
