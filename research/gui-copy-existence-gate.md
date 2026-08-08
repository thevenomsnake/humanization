# GUI 文案存在性门：研究报告

- 研究日期：2026-08-08
- 研究范围：网站、产品和 GUI 文案在写作前如何判断“这条信息是否应该出现”；重点是把内部能力清单误写成公开宣传文案的情况。
- 资料范围：官方内容设计指南、成熟设计系统的公开源文件，以及 `kill-ai-slop` 的原始 Skill。链接均固定到本次读取的提交或官方页面。
- 与多语言无关：本报告讨论通用的内容决策层；语言档案只在存在性决定后负责自然表达。

## 结论

用户给出的句子：

> 这个公开网站没有处理服务，不提供文件上传，不连接外部系统，也没有开始任务的入口。

它是内部 QA/能力盘点，不是对外宣传文案。句子虽然可能事实正确，却没有说明受众要完成什么任务、需要作什么决定、下一步是什么，列出的“没有”也没有带来可见的用户收益。默认动作应是从公开页面删除，或回到内部产品说明；只有当某项限制会改变用户预期、隐私判断、权限判断、恢复路径或法律/安全选择时，才把它转成用户能理解并能据此行动的说明。

这不是简单的“负面词过滤”。`不存在`、`不能`、`不支持` 有时是必要信息，例如不可逆后果、权限不足、数据处理边界、服务故障或明确的方案差异。应先通过存在性门决定信息的职责和位置，再由 GUI 组件与 locale 规则决定句式。

## 一手来源与可转化原则

### GOV.UK 内容发布指南

GOV.UK 的“Identify user needs”要求每一项已发布内容满足有效用户需要，并把用户需要写成“谁、要做什么、为了什么”。它明确说，若用户知道某事后不需要采取行动，那就不是有效的用户需要；也警告不要为了给已有内容找理由而制造需要。[原文：`Every piece of published content should meet a valid user need`](https://github.com/alphagov/govuk-content-publishing-guidance/blob/6688ebb88227991b8987bd65df05bfcc3c39b7e4/app/writing-to-gov-uk-standards/plan-manage-content/identify-user-needs.md#L13-L14)、[动作/任务与无后续动作的边界](https://github.com/alphagov/govuk-content-publishing-guidance/blob/6688ebb88227991b8987bd65df05bfcc3c39b7e4/app/writing-to-gov-uk-standards/plan-manage-content/identify-user-needs.md#L72-L94)、[不要反过来制造需要](https://github.com/alphagov/govuk-content-publishing-guidance/blob/6688ebb88227991b8987bd65df05bfcc3c39b7e4/app/writing-to-gov-uk-standards/plan-manage-content/identify-user-needs.md#L103-L114)。

“Write content to meet user needs”进一步要求只发布满足该需要所必需的内容，不多写，并让用户快速找到信息、完成任务、离开页面。[原文](https://github.com/alphagov/govuk-content-publishing-guidance/blob/6688ebb88227991b8987bd65df05bfcc3c39b7e4/app/writing-to-gov-uk-standards/writing-guidelines/meet-user-needs.md#L13-L24)。

可转化为 Humanization 的通用规则：

- 写作前先建立 `As a… / I need to… / So that…` 的用户需要，不以“团队想介绍什么功能”作为存在理由。
- 把“知道”继续追问到动作、决定或结果；没有后续动作的说明默认删除或移动到合适的文档。
- 用最小信息满足任务。内部架构、团队流程和功能盘点不能自动成为公开正文。

### 18F Content Guide

18F 的技术与界面写作指南要求直接引导读者，以清晰动词或目标开头，并明确写道“聚焦读者能做什么，而不是他们不能做什么”。它给出成对例子：`You cannot continue without signing in.` 改为 `Sign in to continue.`。[固定源文件与原文示例](https://github.com/18F/content-guide/blob/1b1723d3d5b8f91d92c16487c88b56265dc0ec3a/_pages/our-style/technical-and-interface-writing.md#L30-L55)。

可转化规则：

- 内部能力事实先转为用户可观察的结果和下一步，不直接把“后端/API/数据库没有什么”抛给读者。
- 能力限制若确实影响任务，应写成“现在能做什么、用户接下来怎么做”；若不改变行动或预期，不出现在该表面。
- 这是一条表达和信息架构规则，不是禁止所有否定句。隐私、权限、费用和不可逆后果仍可用否定表达，只要它改变用户决定。

### GOV.UK Design System：错误、通知、警告和 Details

这些组件把“信息该不该出现”与“该放在哪里”分开处理：

- 错误消息要说明发生了什么以及如何修复；对于用户无法修复的服务容量或服务问题，不应伪装成字段错误，而应使用说明问题并给出下一步的页面。[错误消息职责](https://github.com/alphagov/govuk-design-system/blob/efb0d77d38b7ed7f921697564d2c47723d434977/src/components/error-message/index.md#L14-L28)。
- 错误文案应具体，泛化的 `An error occurred` 没有帮助；具体情形和真实恢复动作才值得占据界面空间。[具体与可恢复](https://github.com/alphagov/govuk-design-system/blob/efb0d77d38b7ed7f921697564d2c47723d434977/src/components/error-message/index.md#L88-L92)、[避免泛化错误](https://github.com/alphagov/govuk-design-system/blob/efb0d77d38b7ed7f921697564d2c47723d434977/src/components/error-message/index.md#L116-L131)。
- 通知横幅只用于用户需要知道、但与当前页面主体不直接相关的事项，并且应少用；与当前任务直接相关的信息应放在主体内容中。示例包括影响全站的延迟、用户个人的截止日期和刚完成动作的结果。[通知职责与位置](https://github.com/alphagov/govuk-design-system/blob/efb0d77d38b7ed7f921697564d2c47723d434977/src/components/notification-banner/index.md#L12-L28)。
- 警告文字用于重要后果，例如采取或不采取行动带来的法律后果。[警告使用条件](https://github.com/alphagov/govuk-design-system/blob/efb0d77d38b7ed7f921697564d2c47723d434977/src/components/warning-text/index.md#L14-L16)。
- Details 适合只需少数用户展开的次要信息，不应把大多数用户需要的信息藏起来。[Details 的使用边界](https://github.com/alphagov/govuk-design-system/blob/efb0d77d38b7ed7f921697564d2c47723d434977/src/components/details/index.md#L12-L27)。

可转化规则：同一事实在不同 surface 的存在理由不同。错误要恢复，通知要及时告知，警告要帮助权衡重要后果，Details 只承载低频补充。不要把一条内部限制复制到首页、错误、空状态和通知四处。

### PatternFly：Empty State 的公开 GitHub 示例

PatternFly 的 Empty State 源文件把状态分成首次使用、无结果、必需配置、无权限、后端失败、成功和创建等情形。其共同要求是解释当前为何为空、用户如何继续，以及下一步能获得什么；必需配置和无权限示例都要求写“需要做什么”，而不是“还没做什么”或“被拒绝”。[组件元素与下一步](https://github.com/patternfly/patternfly-org/blob/3aff87cace31c7d7e94ebae4cb35666f4f2e75d7/packages/documentation-site/patternfly-docs/content/components/empty-state/empty-state.md#L16-L18)、[配置状态 Do/Don't](https://github.com/patternfly/patternfly-org/blob/3aff87cace31c7d7e94ebae4cb35666f4f2e75d7/packages/documentation-site/patternfly-docs/content/components/empty-state/empty-state.md#L101-L121)、[无权限与后端失败](https://github.com/patternfly/patternfly-org/blob/3aff87cace31c7d7e94ebae4cb35666f4f2e75d7/packages/documentation-site/patternfly-docs/content/components/empty-state/empty-state.md#L134-L176)。它还要求空状态说明当前缺少什么后给下一步，并避免用大段文字解释页面本身。[信息量边界](https://github.com/patternfly/patternfly-org/blob/3aff87cace31c7d7e94ebae4cb35666f4f2e75d7/packages/documentation-site/patternfly-docs/content/components/empty-state/empty-state.md#L336-L337)。

可转化规则：空状态不是“把所有没有的功能列出来”，而是当前状态的任务引导。只有当前状态阻断或改变用户目标时才写限制，并附带真实动作、恢复路径或离开路径。

### USWDS：404/死路场景

U.S. Web Design System 的 404 指南要求简洁、非技术化，不为了填空间增加内容；同时必须告诉用户下一步，并给错误死路提供首页、搜索、反馈等出口。[固定源文件](https://github.com/uswds/uswds-site/blob/284e0976332d4e958ac1baf986180276dd4cbbcb/_templates/page-templates/404/guidance/usability.md#L1-L7)。

可转化规则：没有下一步的状态文案应被视为死路信号。不能提供真实出口时，优先修正产品流程或移除该表面，而不是再加一段解释。

## 为什么融合 `kill-ai-slop` 后不会自动解决

`kill-ai-slop` 的公开 Skill 把重点放在视觉和文案的“默认套路”，提出 `Subtract first` 与 `Specific beats punchy`，并要求扫描结果只作起点、逐项人工 triage，保留作者有意选择和文案含义。[原则](https://github.com/yetone/kill-ai-slop/blob/96d1ca568a1db7e1ef9a381644c744440f816ee4/skill/SKILL.md#L35-L38)、[扫描只是起点](https://github.com/yetone/kill-ai-slop/blob/96d1ca568a1db7e1ef9a381644c744440f816ee4/skill/SKILL.md#L58-L71)、[保持含义](https://github.com/yetone/kill-ai-slop/blob/96d1ca568a1db7e1ef9a381644c744440f816ee4/skill/SKILL.md#L100-L102)。这套边界很适合清理模板腔，但它没有输入“用户任务、表面职责、披露依据、可执行下一步”这些字段，也没有声明“事实正确但没有用户价值的句子应删除”。

因此此前融合能阻止空泛、夸张或模板化表达，却不会自动知道“没有处理服务”是内部验收信息还是访客必须知道的限制。这个缺口属于内容决策层，和语言特化无关；补法是增加存在性门，不是继续扩充 anti-slop 词表。

## 建议的存在性门

### 输入账本

在语言改写和组件措辞之前，为每个候选字符串记录：

| 字段 | 要回答的问题 |
| --- | --- |
| `surface` | 它附着在页面、按钮、错误、空状态、确认、通知、隐私说明、无障碍名称还是内部日志？ |
| `audience` | 谁在此刻读它？访客、已登录用户、管理员、支持人员还是开发者？ |
| `user_need` | 这个人要完成什么动作、决定什么选择或确认什么结果？ |
| `candidate_role` | 它是动作、状态、恢复、后果、信任/合规、导航/识别，还是内部说明？ |
| `observable_effect` | 省略它会改变用户的行动、预期、权限判断、隐私判断或恢复路径吗？ |
| `disclosure_basis` | 若不是任务信息，是否有法律、隐私、安全、无障碍或明确产品契约要求？ |
| `next_step` | 用户读完后能做什么，或能准确预期什么？动作必须真实存在。 |
| `source_of_truth` | 能力、数据行为和后果由哪个产品事实或政策证明？ |

### 判定流程

1. **先写用户需要，不先写句子。** 用“作为某类用户，我需要完成某动作/决定，以便得到某结果”。如果只能写成“让用户了解我们内部如何实现”，先暂停。
2. **判定职责。** 候选必须属于当前 surface 的任务。按钮命名动作结果，错误帮助恢复，空状态解释当前状态并导向下一步，通知传达及时且需要知道的变化，隐私/权限说明真实的数据或访问边界。
3. **做省略测试。** 暂时拿掉它，问“用户会因此无法行动、无法作出重要选择、误解结果、无法恢复，或错过必须知道的法律/隐私/安全事实吗？”全为“不会”时，默认 `drop` 或 `move`。
4. **做内部事实转译。** 把内部事实映射为“用户可观察的结果 → 受影响的选择/预期 → 真实下一步”。映射不出结果或下一步，就不要把内部事实写成公开文案。
5. **按时机放置。** 会改变当前任务的信息放在任务现场；跨页面的服务状态才用通知；低频补充才放 Details；错误和空状态不要在首页预先罗列。
6. **最后才做语言和结构检查。** 存在性结论先固定为 `keep`、`reframe`、`move`、`drop` 或 `needs_author_decision`，再交给 locale 与组件模块表达。

### 四类应保留的信息

1. **行动/恢复：** 用户需要知道如何提交、继续、重试、返回或联系支持。
2. **决定/预期：** 信息会改变用户是否使用、付费、授权、上传、等待或执行不可逆动作的决定。
3. **状态/结果：** 当前结果、权限、资格、截止日期、服务中断或处理完成情况会改变下一步。
4. **信任/义务：** 已确认的数据收集/使用/分享、法律后果、安全警示和无障碍名称等必须信息。它们不一定有 CTA，但必须放在用户能取得且与行为相称的位置。

## 负面能力清单怎么处理

### 默认不公开

以下句式通常是内部材料，不是首页宣传：

- “没有处理服务。”
- “不提供文件上传。”
- “不连接外部系统。”
- “没有开始任务的入口。”

它们描述的是实现盘点，既没有用户目标，也没有说明访客因此应做什么。把四条拼在一起只会让读者寻找一个并不存在的功能，甚至暗示产品原本应该有这些功能。

### 只有在改变用户选择时才公开

可以保留负面或限制信息，但要满足以下至少一项：

- 访客很可能有相反预期，省略会造成错误行动或错误购买决定；
- 数据是否上传、保存、分享会影响隐私选择；
- 权限、资格、地区、费用、期限或不可逆后果会影响是否继续；
- 当前故障或空状态阻断任务，并且文案能给出真实恢复/离开路径；
- 无障碍、法律或安全要求必须告知。

### 由内部事实转为外部表达

下面只是结构示例，不是对任何具体产品能力的事实断言：

| 内部笔记 | 存在性判断 | 可能的外部表达 |
| --- | --- | --- |
| 没有处理服务 | 若页面只是介绍/指南，删掉；若用户会期待上传分析，在入口附近澄清 | “这是阅读与参考页面，不会处理你提交的文件。” |
| 不提供文件上传 | 若原因是隐私或用户会寻找上传入口，保留可验证的数据行为 | “文本留在此浏览器中，不会上传。”（只有产品事实已核实才可写） |
| 不连接外部系统 | 若没有外部系统连接并不改变访客任务，删掉；若用户会误以为会自动投递，改写为实际能做的准备/导出动作 | “整理好材料后，你可以在目标网站自行提交。”（需确认确有该动作/链接） |
| 没有开始任务入口 | 不把“没有入口”写出来；调整页面结构或提供真实 CTA。若当前状态确实无内容，用空状态说明下一步 | “先选择一份材料，再开始。”（只有选择与开始动作真实存在才可写） |

核心原则是：内部清单可以约束不能说什么，但不是公开文案的内容目录。公开文案应描述用户能获得的结果、当前状态和真实选择。

## 什么可以自动化，什么不能

### 可确定性检查的窄范围

检查器可以在有产品上下文或能力账本时硬性阻断：

- 候选缺少 `surface`、`user_need` 或 `candidate_role`；
- 文案声称一个能力，但能力账本明确标记为不存在；
- CTA、权限、费用、期限、数据行为或不可逆后果被改写后不一致；
- GUI key、变量、ICU 分支、markup 或可访问名称被破坏；
- 已声明的隐私/法律/安全披露被遗漏。

它可以把“没有/不能/不支持 + 后端/API/上传/集成”等组合标为 `existence_review` 警告，提示人工判断，但不能仅凭关键词删除。

### 必须交给人工或模型结合上下文判断

- 用户是否真的有该误解，限制是否影响转化或信任；
- 一句“无需上传”是隐私价值、功能缺失，还是两者都有；
- 当前 surface 是公开宣传、操作中状态、帮助文档还是内部诊断；
- 法律、行业政策、合同或无障碍义务是否适用；
- 页面没有 CTA 是有意的阅读路径，还是产品遗漏；
- 删除后是否会造成沉默的错误预期。

这些问题无法由跨产品通用词表稳定回答。缺上下文且会改变承诺或行动时，返回 `needs_author_decision`，只问一个聚焦问题；不要用漂亮改写替作者决定。

## 给 Humanization 的最小落点

把“存在性门”放在现有 `core` 账本和 `gui-microcopy` 组件职责之间：

1. 通用层新增“用户需要/候选职责/省略后果/披露依据/真实下一步”五项决策字段。
2. GUI 模式先判 `keep | reframe | move | drop | needs_author_decision`，再保护 key、ICU、变量和 markup；不要让结构保护等同于内容必须保留。
3. 对外宣传默认写产品结果和受众收益；内部能力边界仅用于防止虚假承诺，只有在影响用户决定时才在相应位置说明。
4. 确定性脚本只报告缺失账本、明确矛盾和资源破坏；自然度、信息价值和“是否该存在”保留为带上下文的人工/模型审阅。

### 本次实现采用的结果

运行时使用 `keep | rewrite | move | remove` 处置候选文案，并用 `needs_product_decision` 单独标记候选文案暴露的产品流程缺口。两种结论可以同时成立：示例句本身可以 `remove`，缺少真实分析入口的问题仍需要产品团队决定。`no_change` 表示 `keep` 且文字无需修改，结构化资源中的 `remove` 只报告处置建议，不清空 value、不删除 key，也不改变运行时结构。

## 资料与证据边界

本报告提炼的是各项目明确写出的用户需要、行动、恢复和信息放置原则；“存在性门”的字段与五种结果是对这些原则的工程化综合，不是任何单一项目宣称的标准。来源项目的例子只用于说明其公开规则和设计决策，不把某一语言或某一产品的词形、标点和视觉规则提升为全局规则。
