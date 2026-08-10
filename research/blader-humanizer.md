# `blader/humanizer` 深度研究

- 研究日期：2026-08-10
- 上游仓库：[`blader/humanizer`](https://github.com/blader/humanizer)
- 不可变上游快照：[`523374dee72d67c7b2b5f858ea0094ffda49c3ac`](https://github.com/blader/humanizer/tree/523374dee72d67c7b2b5f858ea0094ffda49c3ac)，同时对应 `v2.9.1`
- 本地对照快照：[`thevenomsnake/humanization@d3b8f3791fee58c030aa52539296ad361654f1c7`](https://github.com/thevenomsnake/humanization/tree/d3b8f3791fee58c030aa52539296ad361654f1c7)
- 资料范围：仓库文件、完整 Git 历史、GitHub API、Actions、releases、issues 和 pull requests。统计值属于 2026-08-10 的可变快照；规则与代码引用尽量固定到提交。

## 结论摘要

`blader/humanizer` 最有价值的部分并非 33 条英文禁忌本身，而是后来逐步补上的编辑契约：保留原始信息、不得造事实、根据作者样本校准 voice、按调用场景决定交付形态，并用 false-positive guidance 抑制过度编辑。这些内容集中在当前 [`SKILL.md` 的任务、voice 和检测边界](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L19-L46) 以及 [`Invocation Modes` / `Process and Output`](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L391-L406)。

它不是一个经过语料评测的“AI 检测器”。运行时只是 412 行 Markdown 指令，仓库没有行为测试集、benchmark、golden outputs 或 precision/recall 评测；唯一脚本只校验包结构、版本同步、编号和行数，CI 再检查 Skills CLI 与 Claude Code 插件能否识别该包。[运行时说明](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/AGENTS.md#L5-L17)、[校验脚本](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/scripts/validate-package.py)、[CI](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/.github/workflows/validate.yml)

当前版本仍有两类实质性矛盾。第一类是规则冲突，例如英文破折号被设为硬禁令，但检测指导又说单独出现破折号不是可靠信号；弯引号也同时被要求替换和列为单独不足以判断的 false positive。[破折号硬规则](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L171-L183)、[false-positive guidance](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L357-L375) 第二类是示例违背“不得造事实”和“每项 claim 都保留”的总规则，当前示例仍会新增 `delicacy`、`especially in the south`、`user research`、Next.js 缓存层等原文没有的信息，也会删除媒体引用、排名、同时成立关系和其他主张。[总规则](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L21-L28)、[仍有新增事实的示例](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L112-L119)、[开放问题 #212](https://github.com/blader/humanizer/issues/212)

对本地 Humanization，结论是保留现有六 locale、三层路由、内容存在性门和结构保护，不移植整套 33 项英文规则。值得吸收的增量只有几项：更具体的 voice calibration 清单、双向语义审计、引用/标题/专名/示例的 pattern-scan 保护，以及文档场景下的 diff-anchored writing 检查。完整的调用模式和包同步校验也可参考，但优先级低于语义保真。[本地通用契约](https://github.com/thevenomsnake/humanization/blob/d3b8f3791fee58c030aa52539296ad361654f1c7/humanization/references/core.md)、[本地英文档案](https://github.com/thevenomsnake/humanization/blob/d3b8f3791fee58c030aa52539296ad361654f1c7/humanization/references/locales/en.md)

## 1. 仓库身份与当前快照

### 观察

| 项目 | 2026-08-10 快照 | 一手来源 |
| --- | --- | --- |
| 仓库身份 | 公开、非 fork、未归档；描述为“Agent skill that removes signs of AI-generated writing from text” | [GitHub repository API](https://api.github.com/repos/blader/humanizer) |
| 创建与最近推送 | 创建于 2026-01-18；最近一次 `main` 推送为 2026-07-22 | [GitHub repository API](https://api.github.com/repos/blader/humanizer) |
| 默认分支与 HEAD | `main`，HEAD 为 `523374dee72d67c7b2b5f858ea0094ffda49c3ac` | [不可变提交](https://github.com/blader/humanizer/commit/523374dee72d67c7b2b5f858ea0094ffda49c3ac) |
| 当前版本 | `2.9.1`；`SKILL.md`、插件清单和 README 版本记录一致 | [`SKILL.md` front matter](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L1-L13)、[`plugin.json`](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/.claude-plugin/plugin.json)、[README version history](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/README.md#L208-L226) |
| tags / releases | 只有 `v2.9.0` 和 `v2.9.1` 两个 tag，也只有这两个 GitHub Release；早期版本只存在于 README 历史和提交记录 | [tags API](https://api.github.com/repos/blader/humanizer/tags?per_page=100)、[releases API](https://api.github.com/repos/blader/humanizer/releases?per_page=100) |
| 社区规模 | 34,634 stars、3,112 forks、202 subscribers；这些值会继续变化 | [GitHub repository API](https://api.github.com/repos/blader/humanizer) |
| 提交规模 | 当前 DAG 共 43 个提交；首个提交为 `63def2e4...`，当前 HEAD 为 `523374de...` | [首个提交](https://github.com/blader/humanizer/commit/63def2e4c5bb004ec6c8395e619b069e2f0c4af7)、[首尾比较](https://github.com/blader/humanizer/compare/63def2e4c5bb004ec6c8395e619b069e2f0c4af7...523374dee72d67c7b2b5f858ea0094ffda49c3ac) |

仓库的产品定位在 2026-07-22 已被维护者明确收窄为“改善给人阅读的文字”，不承诺绕过 GPTZero 等检测器。[issue #2 的维护者结论](https://github.com/blader/humanizer/issues/2#issuecomment-5042167295) 因此 README 和 Skill 中的 `Detects`、`AI tell` 更适合理解成编辑启发，不应解释为来源判定或检测规避能力。

## 2. 文件结构、安装与触发设计

### 完整文件树

快照只有 9 个受 Git 跟踪的文件，没有 `references/`、`tests/`、`evals/`、语料或构建产物。[不可变仓库树](https://github.com/blader/humanizer/tree/523374dee72d67c7b2b5f858ea0094ffda49c3ac)

| 文件 | 实际职责 |
| --- | --- |
| [`SKILL.md`](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md) | 唯一运行时指令，含 front matter、33 个 pattern、示例、检测边界、调用模式和输出流程。 |
| [`README.md`](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/README.md) | 安装、用法、33 项摘要表、Lisbon 完整示例、引用和版本历史。 |
| [`.claude-plugin/plugin.json`](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/.claude-plugin/plugin.json) | Claude Code 插件名、版本、作者、许可证和关键词。 |
| [`.claude-plugin/marketplace.json`](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/.claude-plugin/marketplace.json) | 单仓库 Claude Code marketplace 入口。 |
| [`agents/openai.yaml`](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/agents/openai.yaml) | Codex/Agent Skills 的显示名、短描述和 `$humanizer` 默认提示。 |
| [`scripts/validate-package.py`](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/scripts/validate-package.py) | 无第三方依赖的包结构同步检查。 |
| [`.github/workflows/validate.yml`](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/.github/workflows/validate.yml) | 在 `main` push 和 PR 上执行包校验、Skills CLI discovery 和 Claude 插件校验。 |
| [`AGENTS.md`](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/AGENTS.md) | 维护合同，规定编号、版本、README 和插件元数据同步。 |
| [`LICENSE`](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/LICENSE) | `Copyright (c) 2025 Siqi Chen` 的 MIT 许可证。 |

### 安装表面

README 提供三条安装路径：`npx skills add blader/humanizer --global` 的跨 agent CLI、Claude Code marketplace/plugin 命令，以及复制或克隆 `SKILL.md` 的手动安装。它还说明项目安装可去掉 `--global`，安装后需新开 session 或 reload skills。[安装说明](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/README.md#L7-L63)

触发本身没有代码 hook。自动发现依赖宿主读取 `SKILL.md` front matter 的 `name: humanizer` 和宽泛 description；显式调用可以是 `/humanizer`、自然语言请求，或 Claude Code 的 `/humanizer:humanizer`。[front matter](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L1-L13)、[显式用法](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/README.md#L65-L83)、[Claude Code 调用名](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/README.md#L37-L46)

运行时又区分三种交付形态。粘贴文本返回 draft、简短 audit 和 final；文件模式在原文件中只留下 final，聊天里给摘要；嵌入模式只返回 final，不输出过程。[Invocation Modes](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L391-L406) 这项区分值得借鉴，但“文件原地覆盖”没有事务、备份或 parser 保障，只靠模型遵守“保留 code blocks、front matter、data 和 link targets”。

一个仍未解决的兼容性报告指出，根目录 `SKILL.md` 在 Claude Code 和 Cowork web 可用，却未被 Claude Desktop 的插件 loader 识别；报告者推测 Desktop 只扫描 `skills/<name>/SKILL.md`。这是可复现报告中的假设，不是维护者确认的根因。[issue #202](https://github.com/blader/humanizer/issues/202)

## 3. 运行时编辑契约

### 观察

33 个 pattern 之前有四条总规则：扫描模式、保留信息而不拘泥原形、不得新增来源中没有的事实、匹配目标 voice。非虚构中不得新增事实、姓名、数字、日期、引语或引用；虚构创作例外；意见和反应被归入 voice，可以在 `PERSONALITY AND SOUL` 适用时加入。[`Your Task`](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L19-L28)

有作者样本时，Skill 要求先观察句长、词汇、段落开头、标点、重复短语和转场，再匹配这些习惯；样本甚至高于第 14 条破折号禁令。[Voice Calibration](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L30-L38)

“人格与灵魂”只应作用于博客、随笔、观点和个人写作；百科、技术、法律和参考文本应保持中性。该节允许不整齐的句式、意见、不确定、矛盾感、幽默和插话，但不允许为此新增事实。[`PERSONALITY AND SOUL`](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L40-L46)

最终流程固定为 draft、两问 audit、final。audit 会问“哪里仍明显像 AI”和“是否新增事实”，却没有反向逐项问“原文的每个 claim 是否还在”。[Process and Output](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L399-L406) 开放的 [issue #212](https://github.com/blader/humanizer/issues/212) 正是这个缺口的实例：数字和标识符都保留了，排名和“同时成立”关系却被当作形状删掉。

### 判断

“作者样本高于通用偏好”和“neutral plain 也可能是正确的人类 voice”很可靠。风险在于把“意见不是事实”推导成编辑器可以添加立场。立场、情绪和评价仍属于作者信息；本地 Humanization 目前要求保留作者立场，这比上游允许凭 `PERSONALITY AND SOUL` 添加 stance 更稳妥。[本地最小编辑规则](https://github.com/thevenomsnake/humanization/blob/d3b8f3791fee58c030aa52539296ad361654f1c7/humanization/references/core.md#L81-L87)

## 4. 完整的 33 项规则分类

以下名称与编号来自当前 `SKILL.md`。上游文件自身把 23 至 33 全放在 `FILLER AND HEDGING` 标题下，README 却把 26 至 33 列入 Style；校验脚本只检查编号集合，不检查分类或规则文本同步，因此不会发现这类 taxonomy 漂移。[Skill 第 23 至 33 项](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L255-L355)、[README 分类](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/README.md#L138-L171)、[validator 的检查范围](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/scripts/validate-package.py#L37-L59)

| # | 上游名称 | 它试图修正的动作 | 采用边界 |
| --- | --- | --- | --- |
| 1 | Significance, legacy, broader trends | 删掉给普通事实强行抬高历史意义的句子 | 先确认“意义”是否为原始 claim，不能因语气浮夸直接删事实 |
| 2 | Notability and media coverage | 减少无上下文的媒体名单和显著性背书 | 来源清单可能本身就是证据，不能机械裁掉 |
| 3 | Superficial `-ing` analyses | 删除句尾 `highlighting`、`reflecting` 等伪分析 | `-ing` 是正常英语结构，只看分析是否有来源和内容 |
| 4 | Promotional language | 把旅游宣传式形容词改为中性事实 | 营销文案可能有意需要说服力，必须由 surface 决定 |
| 5 | Vague attribution and weasel words | 指明来源，或删除无来源的“experts say” | 不应把来源不明改写成另一条未经证明的事实 |
| 6 | Formulaic challenges/future sections | 删掉模板化“挑战与展望”和乐观收尾 | 真正的风险、计划与前景必须保留 |
| 7 | Overused “AI vocabulary” | 审查 `delve`、`pivotal`、`landscape` 等高频词簇 | 单词不是证据，技术词、引语和作者习惯应保留 |
| 8 | Copula avoidance | 用 `is/are/has` 代替 `serves as/boasts` 等绕写 | 只在更直接且含义不变时改 |
| 9 | Negative parallelisms / tailing negations | 改写 `not just X but Y` 和句尾 `no guessing` | 真实对比、否定和修辞节奏不可按词形删除 |
| 10 | Rule of three | 取消为了完整感硬凑的三项列举 | 三项都承载独立事实时必须全部保留；#212 已验证误删风险 |
| 11 | Elegant variation | 停止为避重复而轮换同义词 | 专名和清楚指代可重复，文学性变化仍由文体决定 |
| 12 | False ranges | 拆掉没有共同尺度的 `from X to Y` | 真正时间、数量或程度范围应保留 |
| 13 | Passive voice / subjectless fragments | actor 重要时改主动、补主语 | 英语 passive、UI 短句和中日韩主语省略都可能自然 |
| 14 | Em/en dashes | 当前规则要求最终稿清零，作者样本是例外 | 与 false-positive guidance 冲突，也不能跨 locale 推广 |
| 15 | Boldface overuse | 减少机械强调 | Markdown 结构、术语定义和无障碍扫描可能需要强调 |
| 16 | Inline-header vertical lists | 把“粗体标签 + 冒号”列表改成段落 | 扫描型说明、参数表和 GUI 内容不应机械合并 |
| 17 | Title Case headings | 默认改 sentence case | 服从品牌、出版物、语言和产品约定 |
| 18 | Emojis | 删除装饰性 emoji | 社交语气、品牌和状态图标需结合 surface |
| 19 | Curly quotation marks | 英文示例统一换直引号 | 与英语排版工具和中文引号规范冲突 |
| 20 | Collaborative communication artifacts | 从正文移除 `I hope this helps`、`Want me to...` | 对文章正文有效，对真实邮件或对话不成立 |
| 21 | Cutoff disclaimers / speculative gap-filling | 删知识截止声明，不用“低调”之类填资料空缺 | 应保留真正重要且已说明来源范围的不确定性 |
| 22 | Sycophantic/servile tone | 删除空洞恭维，直接回应内容 | 礼貌和关系维护不是一概多余 |
| 23 | Filler phrases | 把 `in order to` 等缩成直接表达 | 语气、法律含义或节奏需要时可保留 |
| 24 | Excessive hedging | 合并重复模态词 | 不能削弱概率、条件、范围和责任边界 |
| 25 | Generic positive conclusions | 删除无事实的光明前景式结尾 | 有来源的计划、承诺和预测不是 filler |
| 26 | Hyphenated word pairs | 只在 predicate position 去掉不必要连字符 | 上游已因原规则会破坏英语语法而在 PR #121 收窄 |
| 27 | Persuasive authority tropes | 去掉 `the real question is` 等抬高句 | 真正的层级区分或论证转折可保留 |
| 28 | Signposting and announcements | 删除 `let's dive in`，直接进入内容 | 教学、演讲和导航表面可能确实需要路标 |
| 29 | Fragmented headers | 删除标题后的同义暖场句 | 若该句提供 scope 或条件，则不能只因短而删 |
| 30 | Diff-anchored writing | 普通文档描述当前行为，不叙述本次 diff | changelog、release note、migration guide 和 ADR 例外 |
| 31 | Manufactured punchlines / staccato drama | 合并成串的短句和刻意落点 | 单个短句或作者真实节奏不是问题 |
| 32 | Aphorism formulas | 把“X is the language/currency of Y”还原成具体 claim | 真实引语、品牌语和文学表达需要保护 |
| 33 | Conversational rhetorical openers | 删除 `Honestly?`、`Here's the thing` 等假亲密开场 | 真实口语或作者惯用语不应按关键词删除 |

第 1 至 6 项的原文与例子见 [`CONTENT PATTERNS`](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L48-L108)，第 7 至 13 项见 [`LANGUAGE AND GRAMMAR PATTERNS`](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L110-L167)，第 14 至 19 项见 [`STYLE PATTERNS`](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L169-L222)，第 20 至 22 项见 [`COMMUNICATION PATTERNS`](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L224-L253)，第 23 至 33 项见 [`FILLER AND HEDGING`](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L255-L353)。

## 5. 示例审计：规则承诺与实际示范不一致

### 仍会新增原文没有的事实

`v2.9.0` 的提交说明说“Every example that modeled invented specifics is re-cut”，PR #189 也列出五组已修示例。[v2.9.0 commit](https://github.com/blader/humanizer/commit/a25db2d96e95cfd1e6c1831296fe12ba52960ff9)、[PR #189](https://github.com/blader/humanizer/pull/189) 当前快照仍有以下反例：

| Pattern | Before 实际提供的信息 | After 新增的内容 | 固定证据 |
| --- | --- | --- | --- |
| 7 | Somali cuisine 使用 camel meat；pasta 受意大利殖民影响并被广泛采用 | camel meat “is considered a delicacy”；pasta “especially in the south” | [`SKILL.md` 112-119](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L112-L119) |
| 10 | 活动有 keynote、panel 和 networking opportunities | networking 是 `informal`，并且发生在 `between sessions` | [`SKILL.md` 141-146](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L141-L146) |
| 16 | Performance 通过 optimized algorithms 改善 | 具体结果变成 `speeds up load times` | [`SKILL.md` 192-199](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L192-L199) |
| 18 | `Key Insight: Users prefer simplicity` | 该结论被写成 `User research showed...`，新增来源类型 | [`SKILL.md` 208-215](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L208-L215) |
| 20 | 只说“这里是一篇法国大革命 overview” | 新增 1789、financial crisis、food shortages 和 widespread unrest | [`SKILL.md` 226-233](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L226-L233) |
| 28 | 只宣布要解释 Next.js caching | 新增 request memoization、data cache、router cache 三层 | [`SKILL.md` 299-306](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L299-L306) |
| 30 | 只说新函数替代遍历并避免 `O(n²)` | 新增实现为 hash map，lookup 为 `O(1)` | [`SKILL.md` 323-328](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L323-L328) |

### 仍会删除原文 claim

Pattern 2 的 After 删除 Financial Times、The Hindu 和 500,000 followers；Pattern 3 删除 `diverse Texan landscapes` 与 community connection；Pattern 5 删除“plays a crucial role in the regional ecosystem”；Pattern 6 只留下交通和缺水，删掉工业繁荣、战略位置、ongoing initiatives 和 Chennai growth。[Patterns 2-6](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L59-L108)

这些内容有些确实像未经支持的抬高句，但上游总规则说的是“Every claim in the original survives”。只有在任务明确允许事实核查后删除无来源 claim，或作者确认这些是可删修辞时，才能同时满足准确性和编辑目标。当前 prompt 没有把这种处置分支说清。[总规则](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L21-L28)

README 的 Lisbon 完整示例另有明确注记，说明 October、Alfama、neighborhoods 等细节只是作者将来会提供的占位示范，不应在真实会话中自行生成。[README full example](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/README.md#L173-L201) 这降低了误导，但它也说明完整示例不能作为“无事实漂移”的行为证据。

## 6. 检测指导、限制与常见失败模式

### 上游自己承认的 false positives

当前 Skill 明确说，完美语法、正式词汇、混合语体、单个连接词、弯引号、破折号、单个短句、普通 `Honestly`、无引用和复杂格式都不能单独证明 AI；引语、标题、专名和讨论中的示例也不应被 pattern 改写。它主张看 pattern cluster，并保护具体细节、矛盾感、年代语汇、作者可解释的选择、句长变化和自我修正。[Detection Guidance](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L355-L387)

这段 guidance 是上游最值得保留的安全阀，但它没有改变后面的固定流程。即使没有可靠 cluster，流程仍要求写 draft 和 final，也没有正式的 `no_change` 结果。[Process and Output](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L399-L406) 社区分别提出 density pre-check 和 light-edit mode；维护者认为分层计分、硬改动数会增加 ceremony，选择以 voice calibration、personality gating 和 detection guidance 承担克制原则。[issue #93 的关闭理由](https://github.com/blader/humanizer/issues/93#issuecomment-5042167963)、[issue #172 的关闭理由](https://github.com/blader/humanizer/issues/172#issuecomment-5042168685)

### 主要失败模式

1. **事实新增仍会被示例诱导。** 第 5 节已经列出多个当前反例，说明 v2.9.0 的修复并不完整。[PR #189](https://github.com/blader/humanizer/pull/189)
2. **事实删除缺少逆向 audit。** #212 展示了排名和 simultaneity 的丢失；早期 #78 还报告过整段截断和凭空加入第一人称经历，后来 #84 增加了内容保留规则。[issue #212](https://github.com/blader/humanizer/issues/212)、[issue #78](https://github.com/blader/humanizer/issues/78)、[PR #84](https://github.com/blader/humanizer/pull/84)
3. **硬规则与 false-positive guidance 冲突。** 破折号和弯引号既被列为单独不足以判断的正常现象，又在 pattern 中被要求替换。[Pattern 14-19](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L171-L222)、[false positives](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L357-L375)
4. **英文规则不能直接跨语言。** 维护者选择让各语言在独立社区仓库演化；zh-CN 与 zh-TW issue 都说明引号、破折号、无主语句和连字符规则会在中文中反转或失效。[维护者的 locale policy](https://github.com/blader/humanizer/issues/163#issuecomment-5042168700)、[zh-CN #203](https://github.com/blader/humanizer/issues/203)、[zh-TW #194](https://github.com/blader/humanizer/issues/194)
5. **格式和 surface 缺席。** 同一条“删 emoji、改列表、补主语”会在文章、邮件、UI、法律文本和社交内容中产生不同后果；当前输入没有 `locale`、`format`、`surface` 或结构契约。[front matter 与任务输入](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L1-L28)
6. **运行时上下文偏重。** 每次调用都加载 33 组 Before/After；开放的 PR #191 计划把示例移到按需读取的 `PATTERNS.md`，把 `SKILL.md` 从 412 行降到 247 行，但尚未合并。[PR #191](https://github.com/blader/humanizer/pull/191)
7. **“人类迹象”有时效性和归因风险。** “模型落后一到多年”和“2022-11-30 以前几乎不是 AI”可作调查线索，不能作为作者身份判定；仓库没有对此做行为评测。[相关原文](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L377-L387)
8. **文件模式只靠提示保护结构。** 没有 parser 比较 key、markup、placeholder、ICU 或链接结构，也没有回滚机制。[File mode](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L393-L397)
9. **安装兼容仍有缺口。** Claude Desktop 的 root-level `SKILL.md` 识别问题尚未关闭。[issue #202](https://github.com/blader/humanizer/issues/202)
10. **外部“security”报告不足以证实漏洞。** #210 只给出 skills.sh/Snyk 链接，没有复现步骤或受影响代码；当前仓库唯一 Python 脚本只读本地文件和 JSON。它应继续 triage，但不能据此宣称存在已确认的 credential vulnerability。[issue #210](https://github.com/blader/humanizer/issues/210)、[validator 源码](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/scripts/validate-package.py)

## 7. 脚本、CI、测试与本次小探针

### 仓库自带校验

`validate-package.py` 做五件事：确认 `SKILL.md` 从 YAML front matter 开始；拒绝 `compatibility` 和 `allowed-tools` 两个非便携 key；同步 `SKILL.md`、README、plugin 的版本；确认 Skill 编号严格为 1 至 33 且 README 集合相同；限制 Skill 不超过 500 行。[完整脚本](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/scripts/validate-package.py)

CI 在 Ubuntu、Python 3.12、Node 22 上运行该脚本、`npx --yes skills@1.5.20 add . --list` 和 `claude plugin validate .`；HEAD 对应的主分支 run 成功。[workflow](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/.github/workflows/validate.yml)、[成功 run](https://github.com/blader/humanizer/actions/runs/29896748584)

本次在 Windows 默认 GBK 环境运行 `python scripts/validate-package.py` 时，`Path.read_text()` 因未指定 UTF-8 而抛出 `UnicodeDecodeError`；设置 `PYTHONUTF8=1` 后输出 `Humanizer package v2.9.1 is valid`。问题来自脚本三处未传 `encoding` 的 `read_text()`，不会在当前 Ubuntu CI 暴露。[源码位置](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/scripts/validate-package.py#L10-L13)

### 不存在的行为评测

当前树没有自动调用 agent 的测试、前后文语义 diff、事实保留检查、pattern precision/recall、作者 voice 相似度、locale corpus 或基准分数；CI 通过只能证明包面和发现机制通过，不能证明改写质量。[不可变仓库树](https://github.com/blader/humanizer/tree/523374dee72d67c7b2b5f858ea0094ffda49c3ac)、[CI 内容](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/.github/workflows/validate.yml)

### 一个有界 prompt probe，不是评测

2026-08-10 的一个全新 Codex 子任务只读取快照 `SKILL.md`，未固定模型，也没有重复采样。第一段输入同时含排名、三个并列作用、`simultaneously` 和 `not just`；最终稿保留“最重要”、三个作用和 launch gate，却删除了显式 `simultaneously`。第二段是带时间、姓名、失败细节和作者自我评价的个人文字；最终稿只把破折号改成冒号，其余内容保留。这个结果与 #212 的风险方向一致，但一次、未固定模型的样本不能证明总体成功率，也不能当作 benchmark。[对应的上游问题 #212](https://github.com/blader/humanizer/issues/212)

## 8. 提交历史与版本演进

完整历史从 2026-01-17 的初始 Skill 到 2026-07-21/22 的 `v2.9.1`，共 43 个提交。[首尾 compare](https://github.com/blader/humanizer/compare/63def2e4c5bb004ec6c8395e619b069e2f0c4af7...523374dee72d67c7b2b5f858ea0094ffda49c3ac) 关键节点如下：

| 时间 | 提交 / PR | 变化 |
| --- | --- | --- |
| 2026-01-17 | [`63def2e4`](https://github.com/blader/humanizer/commit/63def2e4c5bb004ec6c8395e619b069e2f0c4af7) | 初始 Claude Code Skill。 |
| 2026-01-17 | [`b2564d30`](https://github.com/blader/humanizer/commit/b2564d305b77e33ee51ebdc0f26b033a6de997cf) | `v2.0.0`，提交说明称直接抓取 Wikipedia 原始文章并据此重写为 24 类 pattern。 |
| 2026-01-17 | [`47a64322`](https://github.com/blader/humanizer/commit/47a64322abe0c65704eb8f711d59de28b79c835e) | 为当时全部 pattern 加 Before/After 示例。 |
| 2026-01-18 | [PR #1](https://github.com/blader/humanizer/pull/1) | 增加 `Personality and Soul`。 |
| 2026-03-31 | [PR #64](https://github.com/blader/humanizer/pull/64) | 增加作者样本 voice calibration。 |
| 2026-04-01 | [PR #79](https://github.com/blader/humanizer/pull/79) / [PR #80](https://github.com/blader/humanizer/pull/80) | 整合新 pattern，并加入 passive voice / subjectless fragments。 |
| 2026-05-26 | [PR #113](https://github.com/blader/humanizer/pull/113)、[PR #121](https://github.com/blader/humanizer/pull/121)、[PR #84](https://github.com/blader/humanizer/pull/84) | 加 false-positive guidance，收窄连字符规则，补内容保留与破折号变体。 |
| 2026-05-26 至 06-07 | [`9c448c84`](https://github.com/blader/humanizer/commit/9c448c8430967d122e0e40d696f7e196f18bdc7f)、[`a2ace14a`](https://github.com/blader/humanizer/commit/a2ace14a88a6746f64f1f53ed8272d6788828038)、[`9600f2b7`](https://github.com/blader/humanizer/commit/9600f2b7241cb4eed6ad803abee5ea01d67fe8e4) | `v2.6` 精简、`v2.7` 硬化破折号并加 gap-filling/diff-anchored、`v2.8` 加 cadence pattern。 |
| 2026-07-21 | [PR #189 / `a25db2d9`](https://github.com/blader/humanizer/commit/a25db2d96e95cfd1e6c1831296fe12ba52960ff9) | `v2.9.0`：no-fabrication、information over shape、voice 样本优先、三种调用模式。 |
| 2026-07-21 | [`523374de`](https://github.com/blader/humanizer/commit/523374dee72d67c7b2b5f858ea0094ffda49c3ac) | `v2.9.1`：跨 agent 包装、OpenAI 元数据、校验脚本和 CI；当前 HEAD。 |

README 记录了 `1.0.0` 至 `2.9.1` 的版本叙述，但只有最后两个版本建立了 tag 和 Release；Release 没有附加 binary/assets，只提供 GitHub 自动生成的源码压缩包。[README history](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/README.md#L208-L226)、[releases API](https://api.github.com/repos/blader/humanizer/releases?per_page=100)

## 9. Issues、PRs 与维护信号

### 统计快照

截至 2026-08-10，GitHub 搜索返回 87 个 issue，其中 13 个 open、74 个 closed；122 个 PR，其中 13 个 open、16 个 merged、93 个 closed-unmerged。[issues 查询](https://api.github.com/search/issues?q=repo%3Ablader%2Fhumanizer%20is%3Aissue)、[PR 查询](https://api.github.com/search/issues?q=repo%3Ablader%2Fhumanizer%20is%3Apr)、[merged PR 查询](https://api.github.com/search/issues?q=repo%3Ablader%2Fhumanizer%20is%3Apr%20is%3Amerged)

16 个已合并 PR 的主题集中在 prompt 规则、文档和包装：voice calibration、内容保留、false-positive guidance、连字符收窄、OpenCode、许可证、版本和 `v2.9.0` no-fabrication。[closed PR API](https://api.github.com/repos/blader/humanizer/pulls?state=closed&per_page=100) 这说明维护者愿意吸收窄而明确的修复，但合并率不高，许多更大架构或模式扩展被关闭或长期开放。

### 当前 backlog 的含义

- 正确性问题仍在继续。#212 是语义删除；#190 请求给 annotated link / definition 的破折号加例外；#209 请求处理重复句首。[#212](https://github.com/blader/humanizer/issues/212)、[#190](https://github.com/blader/humanizer/pull/190)、[#209](https://github.com/blader/humanizer/pull/209)
- 多个开放 PR 同时争用 pattern 34 和 `v2.10.0`，包括 abrupt shifts、invisible-context defenses、vague `This` back-reference、shadowboxing 和 sentence-length patterns，合并时会发生编号和版本协调问题。[#196](https://github.com/blader/humanizer/pull/196)、[#201](https://github.com/blader/humanizer/pull/201)、[#208](https://github.com/blader/humanizer/pull/208)、[#207](https://github.com/blader/humanizer/pull/207)、[#211](https://github.com/blader/humanizer/pull/211)
- locale 政策当前仍是独立社区仓库。维护者在 French #163 和 Spanish #138 明确关闭了 core 内多语言请求；与此同时，文档 PR #204 和 Arabic language-pack PR #205 仍开放，尚不能当作 roadmap 承诺。[#163](https://github.com/blader/humanizer/issues/163#issuecomment-5042168700)、[#138](https://github.com/blader/humanizer/issues/138#issuecomment-5042168199)、[#204](https://github.com/blader/humanizer/pull/204)、[#205](https://github.com/blader/humanizer/pull/205)
- 维护者拒绝把 detector score 作为成功标准，也拒绝 density 分层和固定改动上限带来的额外 ceremony。[#2](https://github.com/blader/humanizer/issues/2#issuecomment-5042167295)、[#93](https://github.com/blader/humanizer/issues/93#issuecomment-5042167963)、[#172](https://github.com/blader/humanizer/issues/172#issuecomment-5042168685)

### 工程维护信号

正向信号包括：HEAD 与最新 tag/release 对齐；主分支 HEAD 的 CI 成功；有 `AGENTS.md` 维护合同；版本和 pattern 编号有自动同步检查；至少 10 个 GitHub contributor identity 被 contributors API 识别。[HEAD commit](https://github.com/blader/humanizer/commit/523374dee72d67c7b2b5f858ea0094ffda49c3ac)、[成功 CI](https://github.com/blader/humanizer/actions/runs/29896748584)、[contributors API](https://api.github.com/repos/blader/humanizer/contributors?per_page=100)

风险信号包括：`main` 在 API 中显示未保护；仓库没有 `CONTRIBUTING`、issue template、PR template、CODE_OF_CONDUCT 或公开 `SECURITY.md`；当前 13 个开放 PR 的 workflow run 多为 `action_required`，并非已执行后失败；多个 PR 争用同一版本和编号。[branches API](https://api.github.com/repos/blader/humanizer/branches?per_page=100)、[community profile API](https://api.github.com/repos/blader/humanizer/community/profile)、[Actions runs API](https://api.github.com/repos/blader/humanizer/actions/runs?per_page=20)

综合判断：这是高关注、低代码量、维护者主导的 prompt 项目，有可用的包面纪律，但行为质量仍主要靠规则文字、issue 反馈和人工判断，没有形成可复现的 eval 体系。

## 10. 来源、许可证与归属义务

### 上游 MIT

上游 `LICENSE` 是 MIT，版权行为 `Copyright (c) 2025 Siqi Chen`。复制或发布该软件及 substantial portions 时，许可证要求把该版权声明和完整 permission notice 一并保留。[固定许可证](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/LICENSE)

因此，如果 Humanization 未来逐段复制 `SKILL.md`、示例、validator 或 manifests，README 中的一条来源链接不能替代 MIT 文本要求，应把 Siqi Chen 的 MIT notice 放入第三方 notices 或随复制部分分发。若只是研究方法、独立重写原则，没有复制受保护表达，是否构成 substantial portion 需要按实际差异判断；本报告不作法律结论。

### Wikipedia 内容链路

上游反复声明其规则基于 Wikipedia 的 `Signs of AI writing`，`v2.0.0` 提交说明更明确写着“fetched directly”且“examples from Wikipedia”。当前 README 把 Wikipedia 称作 primary source，却没有固定 revision ID，也没有在 MIT `LICENSE` 中说明 Wikipedia 文本的 CC BY-SA 链路。[`v2.0.0` commit](https://github.com/blader/humanizer/commit/b2564d305b77e33ee51ebdc0f26b033a6de997cf)、[当前引用](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/README.md#L101-L111)、[References](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/README.md#L203-L206)

Wikipedia 文字一般按 CC BY-SA 4.0 提供，复用时需要按 Wikimedia 的许可条款处理归属、许可和修改说明；上游的 MIT 声明不能自动消除第三方内容义务。[Wikipedia copyrights](https://en.wikipedia.org/wiki/Wikipedia:Copyrights)、[Wikimedia Terms of Use §7](https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use/en#7._Licensing_of_Content) 对本地最稳妥的做法是继续提炼机制并重写示例，不直接搬运上游的 Wikipedia 衍生示例；若必须搬运，先追溯具体 Wikipedia revision 和原始许可。

### 本地当前状态

本地 README 已用固定 SHA 说明 `blader/humanizer` 对“事实与 working voice 保留、最小编辑、`no_change`”的启发，并明确各链接项目保留各自许可证、当前指令是重新写成的项目规则。[本地 source map](https://github.com/thevenomsnake/humanization/blob/d3b8f3791fee58c030aa52539296ad361654f1c7/README.md#L60-L87) 本地两个 MIT 文件当前只有 `Human Writing Skill contributors` 的版权行。[根许可证](https://github.com/thevenomsnake/humanization/blob/d3b8f3791fee58c030aa52539296ad361654f1c7/LICENSE)、[Skill 许可证](https://github.com/thevenomsnake/humanization/blob/d3b8f3791fee58c030aa52539296ad361654f1c7/humanization/LICENSE)

观察结论是：现有 provenance 记录适合“受启发、独立实现”的状态。后续若复制上游原文或脚本，应新增准确的 MIT notice；若复制 Wikipedia 衍生文字，还需单独处理 CC BY-SA，不要只沿用上游 MIT 标签。

## 11. 与本地 Humanization 的实际对照

### 架构差异

| 维度 | `blader/humanizer@523374d` | 本地 `Humanization@d3b8f37` |
| --- | --- | --- |
| 语言 | 英文规则和英文示例；locale 由独立社区仓库维护 | `zh-CN`、`zh-TW`、`en`、`ja`、`ko`、`es` 六个独立档案 |
| 路由 | 单一 `SKILL.md`，所有 pattern 每次加载 | 通用契约 + 一个 locale + 一个 format，按需加载 |
| 输入 | 给定 text；voice sample 可选 | 显式 `locale`、`format`、`surface`、受众、事实、能力、隐私、CTA 和结构 token |
| 内容决策 | 先扫描 pattern，再重写 | 先做 `keep/rewrite/move/remove` 与 `needs_product_decision` 存在性判断 |
| 保真 | prompt 约束事实与信息，当前只有新增事实 audit | 事实、数字、日期、引语、否定、条件、确定程度、品牌词和 CTA 的账本 |
| 原文合格 | guidance 建议少改，但流程没有正式 `no_change` | 明确允许 `no_change` 和 `needs_author_decision` |
| GUI / 结构 | 文件模式只靠 prompt 保留 code/front matter/data/link | JSON/ARB、HTML、placeholder、ICU、变量、URL、markup 有确定性检查 |
| 自动化 | 包版本、pattern 编号、行数和 discovery CI | 六 locale warning、中文硬规则、GUI 结构与 protected token smoke；当前无 GitHub workflow |

上表的上游事实来自 [`SKILL.md`](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md)、[`validate-package.py`](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/scripts/validate-package.py) 和 [locale policy](https://github.com/blader/humanizer/issues/163#issuecomment-5042168700)；本地事实来自 [不可变仓库树](https://github.com/thevenomsnake/humanization/tree/d3b8f3791fee58c030aa52539296ad361654f1c7)、[`SKILL.md`](https://github.com/thevenomsnake/humanization/blob/d3b8f3791fee58c030aa52539296ad361654f1c7/humanization/SKILL.md)、[`core.md`](https://github.com/thevenomsnake/humanization/blob/d3b8f3791fee58c030aa52539296ad361654f1c7/humanization/references/core.md) 和 [`check_writing_smoke.py`](https://github.com/thevenomsnake/humanization/blob/d3b8f3791fee58c030aa52539296ad361654f1c7/humanization/scripts/check_writing_smoke.py)。

### 已经吸收，而且本地实现更完整的原则

1. **事实与来源保护。** 本地不仅禁止虚构，还记录每项现实 claim 的来源，保护否定、条件、确定程度、能力、隐私和 CTA。[本地事实契约](https://github.com/thevenomsnake/humanization/blob/d3b8f3791fee58c030aa52539296ad361654f1c7/humanization/references/core.md#L9-L30)
2. **最小编辑与停手。** 本地要求只改准确性、理解、任务完成或 locale 自然度真正需要的部分，并提供 `no_change`。[本地最小编辑](https://github.com/thevenomsnake/humanization/blob/d3b8f3791fee58c030aa52539296ad361654f1c7/humanization/references/core.md#L81-L87)
3. **voice 与 register。** 本地英文档案已经规定用户样本和批准的产品 voice 高于通用 anti-slop 偏好，并按受众、渠道、地区和品牌决定语体。[本地英文档案](https://github.com/thevenomsnake/humanization/blob/d3b8f3791fee58c030aa52539296ad361654f1c7/humanization/references/locales/en.md#L10-L17)
4. **pattern cluster，而非单词定罪。** 本地只把 inflated significance、vague attribution、`-ing`、synonym cycling、forced triples、`not just` 和 chatbot opening/closing 当作密度与语境信号。[本地英文档案](https://github.com/thevenomsnake/humanization/blob/d3b8f3791fee58c030aa52539296ad361654f1c7/humanization/references/locales/en.md#L23-L31)
5. **不做 AI 作者判定。** 本地明确不根据词表或分数声称作者使用 AI，也不承诺规避检测器。[本地 core](https://github.com/thevenomsnake/humanization/blob/d3b8f3791fee58c030aa52539296ad361654f1c7/humanization/references/core.md#L81-L87)
6. **英文规则不跨 locale。** 本地把标点、敬语、主语省略、翻译腔和节奏留给六个 locale；这已经解决 #194/#203 所指出的中文反转问题。[本地 locale 路由](https://github.com/thevenomsnake/humanization/blob/d3b8f3791fee58c030aa52539296ad361654f1c7/humanization/SKILL.md#L25-L46)

### 真正值得增加的内容

以下均为建议，不表示已经实现。

1. **最高优先级：双向语义 audit。** 在 `core.md` 的确定程度之外，再明确保护排名、最高级、数量词、同时成立关系、因果、例外、范围和比较关系。最终检查同时问“目标新增了什么”和“来源丢了什么”。#212 已给出可复现失败；本地现有条款虽覆盖否定、条件和确定程度，尚未逐项点名 ranking / simultaneity。[#212](https://github.com/blader/humanizer/issues/212)、[本地现有范围](https://github.com/thevenomsnake/humanization/blob/d3b8f3791fee58c030aa52539296ad361654f1c7/humanization/references/core.md#L23-L30)
2. **中优先级：具体的 voice calibration 清单。** 作者明确提供样本时，观察句长、词汇、段落开头、标点、重复短语和转场，并把结论限制为当前任务的临时约束。上游这六项比本地一句“样本优先”更可执行。[上游 Voice Calibration](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L30-L38)
3. **中优先级：pattern scan 的保护区。** 明确跳过逐字引语、标题、专名、示例、代码和讨论中的被观察词，除非用户要求编辑这些区域。上游 detection guidance 已指出 secondhand text 误伤；本地确定性检查会 mask 部分非 prose，但模型级通用契约还可写得更直接。[上游保护边界](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L371-L375)、[本地 protected tokens](https://github.com/thevenomsnake/humanization/blob/d3b8f3791fee58c030aa52539296ad361654f1c7/humanization/scripts/check_common.py)
4. **中低优先级：文档专用 diff-anchored rule。** 普通 API/doc/comment 描述当前行为，只有 changelog、release note、migration guide 和 ADR 才把“这次新增/替代了什么”作为主体。该规则应放在文档 surface，而不是六语言通用禁令。[上游 Pattern 30](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L323-L328)
5. **低优先级：调用交付模式。** 若独立安装的 Skill 经常同时用于聊天、文件和其他 agent，可加入 `pasted/file/embedded` 的交付差异；本地自动 Humanization wrapper 已有类似行为时，不必重复。[上游 Invocation Modes](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L391-L397)
6. **低优先级：包面同步校验。** 可借鉴版本、README、`agents/openai.yaml`、目录和入口的一致性检查，但必须显式用 `encoding="utf-8"`，并保持与本地现有 smoke 分工清楚。[上游 validator](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/scripts/validate-package.py)

### 明确冲突，不应复制

1. 不复制英文 em/en dash 全局清零。上游自己承认单独破折号不是证据，本地英文档案也把它视为普通标点。[上游冲突](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L171-L183)、[本地规则](https://github.com/thevenomsnake/humanization/blob/d3b8f3791fee58c030aa52539296ad361654f1c7/humanization/references/locales/en.md#L19-L20)
2. 不复制 curly quotes 转 straight quotes。英语排版工具会自动弯引号，zh-CN 与 zh-TW 又有自己的标准形式。[上游 false positive](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L361-L373)、[zh-CN #203](https://github.com/blader/humanizer/issues/203)、[zh-TW #194](https://github.com/blader/humanizer/issues/194)
3. 不复制 blanket active voice、补主语、去 emoji、去 bold、列表转段落、heading sentence case。它们都依赖语言、品牌、内容类型、无障碍和组件职责。[上游 Patterns 13-19](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L162-L222)、[本地 GUI 契约](https://github.com/thevenomsnake/humanization/blob/d3b8f3791fee58c030aa52539296ad361654f1c7/humanization/references/formats/gui-microcopy.md)
4. 不复制词表即作者信号、固定三项拆分、hedging 压缩和 generic conclusion 整段删除。它们会损伤范围、概率、排名、计划和承诺；本地 warning-only 与事实账本更可靠。[上游 Patterns 7/10/24/25](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L112-L146)、[上游 24/25](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L267-L279)、[本地 checker 边界](https://github.com/thevenomsnake/humanization/blob/d3b8f3791fee58c030aa52539296ad361654f1c7/humanization/SKILL.md#L62-L72)
5. 不复制“为人格加入 stance”的授权。作者立场不是可随意生成的装饰，本地应继续把它当作必须保留的信息。[上游授权](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md#L23-L26)、[本地立场保护](https://github.com/thevenomsnake/humanization/blob/d3b8f3791fee58c030aa52539296ad361654f1c7/humanization/references/core.md#L81-L87)
6. 不复制 33 组示例进入全局运行时。现有本地按 `core + locale + format` 逐层加载，更适合六语言，也降低互相冲突和上下文成本。[本地路由](https://github.com/thevenomsnake/humanization/blob/d3b8f3791fee58c030aa52539296ad361654f1c7/humanization/SKILL.md#L18-L51)、[上游 progressive-disclosure PR](https://github.com/blader/humanizer/pull/191)

## 12. 最终建议

观察和建议应分开处理。上游已经证明“保留信息、不得造事实、样本优先、识别 false positive”能显著提高 prompt 的安全边界；issues 又证明仅写这些原则仍不够，示例和审计流程会把模型带回信息增删。最值得本地吸收的是一个很小的逆向补丁：把语义保真从名词清单扩展到关系清单，并在最终稿同时检查新增与遗漏。

不建议把这次研究变成一次 33 条规则迁移。Humanization 已经拥有更合适的多语言架构、内容存在性门、`no_change`、能力与 CTA 约束，以及 GUI 资源保护。[本地 `Humanization 3.0.0`](https://github.com/thevenomsnake/humanization/blob/d3b8f3791fee58c030aa52539296ad361654f1c7/humanization/SKILL.md) 上游可作为英语 pattern catalog 和失败案例库，不能作为跨语言真值表，也不能作为“通过 AI 检测”的证据。
