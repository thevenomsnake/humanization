<p align="center">
  <img src="../assets/readme-cover.svg" alt="Humanization" width="100%">
</p>

<p align="center">
  <a href="../README.md">English</a> ·
  <strong>简体中文</strong> ·
  <a href="./README.zh-TW.md">繁體中文</a> ·
  <a href="./README.ja.md">日本語</a> ·
  <a href="./README.ko.md">한국어</a> ·
  <a href="./README.es.md">Español</a>
</p>

<p align="center">
  <strong>v3.0.0</strong> · MIT · 6 locales · prose / copy / GUI microcopy
</p>

<p align="center">
  <a href="#安装">安装</a> ·
  <a href="#工作方式">工作方式</a> ·
  <a href="#修改前与修改后">前后对照</a> ·
  <a href="#规则来源">规则来源</a> ·
  <a href="#语言档案">语言档案</a> ·
  <a href="#仓库结构">仓库结构</a> ·
  <a href="https://github.com/thevenomsnake/humanization/issues">问题反馈</a>
</p>

<p align="center"><strong>先判断文案该不该出现，再为六种 locale 写得自然。</strong></p>

Humanization 融合多个成熟写作、编辑、本地化、内容设计与 anti-slop 项目的实践，服务多语言产品创造者。它覆盖文章、故事、文档、产品内容、营销文案、邮件和社交内容，也处理导航、按钮、错误、空状态、确认、通知、隐私说明和无障碍名称等 GUI 文字。动笔改写之前，它会先区分内部能力事实与用户在当前载体上真正需要看到的信息。

**语言档案：** [zh-CN 简体中文](../humanization/references/locales/zh-CN.md) · [zh-TW 繁體中文](../humanization/references/locales/zh-TW.md) · [en English](../humanization/references/locales/en.md) · [ja 日本語](../humanization/references/locales/ja.md) · [ko 한국어](../humanization/references/locales/ko.md) · [es Español](../humanization/references/locales/es.md)

## 工作方式

每项任务由三个各司其职的模块共同处理。

- **通用契约：** 事实、来源、能力、隐私、CTA、品牌词、占位符、最小编辑和内容存在性门。
- **语言档案：** 分别定义本语言的语序、语体或敬语、标点、术语、翻译腔审查和自然节奏。
- **GUI 微文案：** 分别处理按钮、错误、空状态、确认和通知，并保护 key、ICU 消息、变量、markup 和运行时结构。

通用契约先把每条候选信息标为 `keep`、`rewrite`、`move` 或 `remove`。如果候选信息还暴露了缺失的动作、状态或恢复路径，再为底层流程同时标记 `needs_product_decision`。内部事实负责约束产品主张，只有承担用户职责的信息才会进入公开文案。语言档案随后决定这些信息在目标语言中如何自然表达。各版本可以采用不同的句式和长度，同时保持相同的受众、动作、能力边界、隐私承诺和已批准术语。

原始材料存在缺口时，Skill 会提出一个聚焦问题、核查来源或缩小主张。页面缺少可用 CTA 或恢复路径时，Skill 返回 `needs_product_decision`，由产品团队决定如何补齐流程。确定性检查会拦截能够证实的损坏；信息是否相关、语气是否合适、语言是否自然，都要结合上下文审阅。

## 修改前与修改后

Humanization 不会把每句真实信息润色后直接发布。它先判断这段文字在当前页面承担什么职责，再决定改写、移动或不提供公开文案。

| 修改前 | 修改后 |
| :--- | :--- |
| **内部能力盘点**<br><br>“这个页面没有处理服务，不接收文件，不连接外部系统，也没有开始任务的入口。” | **不补任何公开文案。**<br><br>**文案处置：** `remove`<br>**产品流程：** `needs_product_decision`。这个页面只提供信息，还是应该让访客在这里完成任务？如果任务应该在这里完成，应先实现真实入口和 CTA，再写文案。 |
| **事实被空话淹没**<br><br>“为了持续提升用户体验，我们对 42 条客服工单进行了全面深入的分析，并发现了一个值得关注的重要现象：其中 31 条都提到绑定账户时遇到了困难。” | **我们查看了 42 条客服工单，其中 31 条提到绑定账户时遇到问题。**<br><br>**文案处置：** `rewrite` |
| **确实支持重试的错误**<br><br>“错误 500：worker 超时，保存请求失败。” | **未能保存你的更改，请重试。**<br><br>**公开消息：** `rewrite`<br>**开发诊断：** `move` 到日志 |
| **确实提供清除筛选的空状态**<br><br>“暂无数据。” | **没有符合当前筛选条件的结果。清除筛选条件，查看全部内容。**<br><br>**文案处置：** `rewrite` |

这些例子不会虚构功能或恢复路径。没有用户职责的文字直接删除，`42/31` 的事实保持不变，开发诊断移到合适位置，空状态只指向真实存在的操作。

## 规则来源

其他项目公开的实用写作方法和语言专属指南共同促成了 Humanization。以下项目塑造了它的通用契约、语言档案和编辑流程。

| 项目 | 对 Humanization 的贡献 |
| :--- | :--- |
| [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing/tree/cd879d22c8588125c1869d0b443f5d8df74b4192) | 奠定最初的 `zh-CN` 长文基础，包括材料是否充足、来源核查、现实与虚构边界、改稿流程和自然中文节奏。 |
| [yetone/kill-ai-slop](https://github.com/yetone/kill-ai-slop/tree/96d1ca568a1db7e1ef9a381644c744440f816ee4) | 启发文本审阅流程，用具体信息代替口号，先清理装饰再改写，并把模式命中作为进一步审阅的线索。 |
| [ehmo/slopkit (`slopbeth`)](https://github.com/ehmo/slopkit/blob/b33718bb9283c11b09567dc714f92d90ffb7bd16/skills/slopbeth/SKILL.md) | 启发证据账本的设计，用于记录实体、数字、日期、URL、引语和不确定性，让每项主张都与现有证据一致。 |
| [blader/humanizer](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md) 和 [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop/blob/d30eddb9e04562234f2070b5ee63ca4649d9a05e/skills/no-ai-slop/SKILL.md) | 启发最小编辑流程，保留作者的事实和有效表达，只做足以解决问题的改动，并允许 `no_change`。 |
| [18F/content-guide](https://github.com/18F/content-guide/tree/1b1723d3d5b8f91d92c16487c88b56265dc0ec3a) 和 [GOV.UK Design System](https://github.com/alphagov/govuk-design-system/tree/efb0d77d38b7ed7f921697564d2c47723d434977) | 启发以用户需求为准的内容取舍、正向任务说明和信息放置原则，并要求错误与不可用状态为用户提供真实的下一步。 |
| [Shopify Polaris](https://github.com/Shopify/polaris-react-archive/blob/af6ffb66a5b1d20f6c2c898b334a1ebb53728ba2/polaris.shopify.com/content/content/fundamentals.mdx)、[Carbon Design System](https://github.com/carbon-design-system/carbon-website/tree/e14433309b1dd53ec790eaa176139007ea9e9c80) 和 [PatternFly](https://github.com/patternfly/patternfly-org/tree/3aff87cace31c7d7e94ebae4cb35666f4f2e75d7) | 启发组件级内容取舍，保留与任务相关的帮助，区分界面状态，并把限制与用户可观察的后果及产品支持的动作相连。 |
| [ya8282/ux-writing-skill](https://github.com/ya8282/ux-writing-skill/tree/711e4162d21367bc62003e428696dc76807d56ec)、[OOOOuyang/UX-writing-skill](https://github.com/OOOOuyang/UX-writing-skill/tree/fad02668533dca76d638aaacf6c2e834657df0ab) 和 [RobTar97/japanese-writing-skills](https://github.com/RobTar97/japanese-writing-skills/tree/e4b1700464219c60da786f005a061bccffbbd4e3) | 启发显式内容处置，要求每条辅助文案都有明确职责，并将面向用户的恢复文案与开发诊断分开。 |

## 语言档案

每个语言档案分别定义本语言的语序、语体、标点、术语、翻译腔审查和节奏。

| Locale | 参考项目与指南 | 由这些来源启发的语言原则 |
| :--- | :--- | :--- |
| `zh-CN` | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing/tree/cd879d22c8588125c1869d0b443f5d8df74b4192) 和 [GB/T 15834-2011](https://openstd.samr.gov.cn/) | 中国大陆中文语序和术语、全角标点、材料驱动的长文写作，以及专门的 `zh-CN prose` house style。 |
| `zh-TW` | [Mozilla zh-TW style guide](https://github.com/mozilla-l10n/styleguides/blob/main/docs/zh-TW/README.md) 和 [bruce6731/anti-ai-writing-taiwan](https://github.com/bruce6731/anti-ai-writing-taiwan/tree/2c14f6a6015885b0c1cad9b54c861bc7b8a3b27d) | 针对 `zh-TW` locale 的原生本地化，涵盖台湾常用的繁体中文术语、语体、标点和文化语序。 |
| `en` | [Google styleguide](https://github.com/google/styleguide/tree/gh-pages/docguide)、[Microsoft Writing Style Guide](https://github.com/MicrosoftDocs/microsoft-style-guide) 和 [Digital.gov Plain Language](https://digital.gov/guides/plain-language/) | 清楚的行动者与动作关系、简洁文档、结合语境的品牌表达、地区一致性和英语标点。 |
| `ja` | [Mozilla Japanese style guide](https://github.com/mozilla-l10n/styleguides/blob/main/docs/ja/l10nguideline.md)、[chezou/slop-nuki](https://github.com/chezou/slop-nuki/tree/1bdf627b5991f4f806069619c9bde407960feac7)、[iKora128/stop-ai-slop-jp](https://github.com/iKora128/stop-ai-slop-jp/tree/e09d32796f253a62693885757cea484c275d06f2)、[RobTar97/japanese-writing-skills](https://github.com/RobTar97/japanese-writing-skills/tree/e4b1700464219c60da786f005a061bccffbbd4e3) 和 [coji/natural-japanese](https://github.com/coji/natural-japanese/tree/b54954f8deb4f110f0959f4e4fac295708900120) | 自然省略和语序、助词、结合语境的敬语与缓冲表达、按组件选择名词或动词形式、GUI 资源完整性，以及结合密度和体裁的审阅方法。 |
| `ko` | [Mozilla Korean style guide](https://github.com/mozilla-l10n/styleguides/blob/main/docs/ko/README.md)、[dotoricode/korean-humanizer](https://github.com/dotoricode/korean-humanizer/tree/7dff5b48cc06fc4252d4766b802ecd61e62c50ad) 和 [HarryJhin/korean-writing](https://github.com/HarryJhin/korean-writing/tree/e4db3883ed76521b7a0cac30392fa67d182cc8ab) | 自然省略主语、助词和分写、`합니다`/`해요`/`다` 语体等级、敬语、句末形式，以及英语和日语翻译腔审查。 |
| `es` | [Mozilla Spanish style guides](https://github.com/mozilla-l10n/styleguides/tree/main/docs/es) | 性数一致、附着代词、`tú`/`usted`/`ustedes`、句首大写式 UI、地区术语、标点和英语仿译审查。 |

所链接的项目分别适用各自的许可证。[多语言研究笔记](../research/multilingual-skill-research.md) 和 [GUI 文案存在性门研究报告](../research/gui-copy-existence-gate.md) 记录了来源证据，以及这些来源如何影响 Humanization；复用相关文字或代码前，请查阅相应仓库的许可证。Humanization 的项目专属规则根据上述实践重新撰写。

## 安装

请让支持从 GitHub 安装 Skill 的 Agent 执行：

```text
Install the humanization Skill from https://github.com/thevenomsnake/humanization. The Skill is in the humanization/ directory.
```

安装后的目录名必须保持为 `humanization`。正确的卡片名称是 `Humanization`，使用带六条语言色带的深绿色 H 图标，说明文字为 “Natural writing and GUI copy across six locales.”。Codex 显示 `活人感写作` 时，当前卡片对应旧版 `human-writing` Skill；Humanization 可按上述名称、图标和说明文字识别。

<details>
<summary><strong>手动安装</strong></summary>

把仓库中的 [`humanization`](../humanization) 目录复制到 Codex Skills 目录：

```text
$CODEX_HOME/skills/humanization/
```

</details>

调用时请明确指定 locale、format 和 surface：

```text
Use $humanization with locale=ja, format=web-microcopy, and surface=error. Rewrite these error messages while preserving the CTA, brand terms, placeholders, and source resource structure.
```

改写之前，先审查现有文案是否适合留在当前载体：

```text
Use $humanization with locale=zh-CN, format=web-microcopy, and surface=public-page. Decide whether each capability statement should be kept, rewritten, moved, or removed, and flag any underlying product decision.
```

公开 format 名 `web-microcopy` 覆盖 HTML、JSON、YAML、ARB、PO、源代码和设计文件中的 GUI 文字，适用于网站、桌面和移动产品。

运行确定性检查器时使用同样的显式路由：

```bash
python humanization/scripts/check_writing.py --locale en --format copy draft.md
python humanization/scripts/check_writing.py --locale es --format web-microcopy --source source.json target.json
```

## 3.0.0 的变化

- 将 `humanization` 定为稳定的 Skill 名和目录名，UI 显示名为 `Humanization`。
- 把运行时指南拆成一个通用契约、六个语言档案和一个 GUI 微文案模块。
- 加入由 `kill-ai-slop` 启发的具体信息、克制表达和审阅线索原则。
- 新增跨语言内容存在性门，用来区分内部能力事实与适合公开的用户信息。
- `--locale` 和 `--format` 改为显式参数，由调用方为混合文本指定路由，语气继续作为人工审阅项。

完整历史记录见 [CHANGELOG.md](../CHANGELOG.md)。

## 仓库结构

<details>
<summary><strong>展开完整目录</strong></summary>

```text
humanization/
├── SKILL.md
├── VERSION
├── LICENSE
├── agents/
│   └── openai.yaml
├── assets/
│   ├── icon-small.png
│   └── icon-large.svg
├── references/
│   ├── core.md
│   ├── locales/
│   │   ├── zh-CN.md
│   │   ├── zh-TW.md
│   │   ├── en.md
│   │   ├── ja.md
│   │   ├── ko.md
│   │   └── es.md
│   ├── formats/
│   │   ├── expressive-text.md
│   │   └── gui-microcopy.md
│   ├── forum-prose.md
│   ├── reality.md
│   ├── fiction.md
│   ├── formats.md
│   └── revision.md
└── scripts/
    ├── check_common.py
    ├── check_gui.py
    ├── check_locale.py
    ├── check_writing.py
    ├── check_writing_smoke.py
    ├── check_zh_cn.py
    └── check_prose.py
```

| 路径 | 用途 |
| :--- | :--- |
| [`SKILL.md`](../humanization/SKILL.md) | 让每项任务依次经过通用、语言和格式模块。 |
| [`core.md`](../humanization/references/core.md) | 负责事实、来源、能力、隐私、CTA、品牌词、占位符、最小编辑和内容处置。 |
| [`locales/`](../humanization/references/locales) | 保存六个语言的原生写作档案。 |
| [`expressive-text.md`](../humanization/references/formats/expressive-text.md) | 处理非 GUI 的产品、文档、营销、邮件和社交文字。 |
| [`gui-microcopy.md`](../humanization/references/formats/gui-microcopy.md) | 定义 GUI 内容存在性门、组件职责和结构化资源保护。 |
| [`check_writing.py`](../humanization/scripts/check_writing.py) | 提供执行通用、语言和 GUI 检查的统一 CLI。 |
| [`check_zh_cn.py`](../humanization/scripts/check_zh_cn.py) | 将原有动作级检查器限定在 `zh-CN prose`。 |

</details>

## 归属与反馈

Humanization 采用 MIT License 发布。最初的 `zh-CN` 长文基础来自同样采用 MIT License 的 [KKKKhazix/human-writing v1.1.0](https://github.com/KKKKhazix/human-writing/tree/cd879d22c8588125c1869d0b443f5d8df74b4192)。上方来源表向影响当前架构的项目和指南致谢，并说明它们的具体贡献。

遇到规则冲突、误报或特定模型上的问题时，请[提交 issue](https://github.com/thevenomsnake/humanization/issues)，并附上提示词、相关输出和你预期的结果。

<p align="center">
  <sub>Humanization · 3.0.0</sub>
</p>
