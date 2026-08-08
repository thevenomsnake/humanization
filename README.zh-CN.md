<p align="center">
  <img src="./assets/readme-cover.svg" alt="Humanization" width="100%">
</p>

<p align="center">
  <a href="./README.md">English</a> ·
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
  <a href="#规则来源">规则来源</a> ·
  <a href="#语言档案">语言档案</a> ·
  <a href="#仓库结构">仓库结构</a> ·
  <a href="https://github.com/thevenomsnake/humanization/issues">问题反馈</a>
</p>

<p align="center"><strong>用六种 locale 写作与改稿，不把一种语言的规则带进另一种语言。</strong></p>

Humanization 是一个独立维护的 Codex Skill，用于文章、故事、文档、产品内容、营销文案、邮件和社交内容。它也处理导航、按钮、错误、空状态、确认、通知、隐私说明和无障碍名称等 GUI 文字。

**语言档案：** [zh-CN 简体中文](./humanization/references/locales/zh-CN.md) · [zh-TW 繁體中文](./humanization/references/locales/zh-TW.md) · [en English](./humanization/references/locales/en.md) · [ja 日本語](./humanization/references/locales/ja.md) · [ko 한국어](./humanization/references/locales/ko.md) · [es Español](./humanization/references/locales/es.md)

## 工作方式

每项任务都会加载三个模块，每个模块只负责一类问题。

- **通用契约：** 事实、来源、能力、隐私、CTA、品牌词、占位符和最小编辑。
- **语言档案：** 语序、语体或敬语、标点、地区词、翻译腔和自然节奏。
- **GUI 微文案：** 分别处理按钮、错误、空状态、确认和通知，并保护 key、ICU 消息、变量、markup 和运行时结构。

通用契约让各语言版本的事实主张和产品承诺保持稳定。语言档案决定这些约束在当地语言中应该怎样自然表达。译文的句式和长度可以不同，但受众、动作、能力边界、隐私承诺和已批准术语必须一致。

源材料不完整时，Skill 会提出一个聚焦问题、核查来源或缩小主张。原文已经成立时，它不会强行改写。确定性检查只阻断可以证明的损坏；语气和自然度仍由所选语言档案负责审阅。

## 规则来源

Humanization 借鉴其他项目的编辑机制，再按照本项目的架构重新表述。它不会复制这些项目的正文、示例、脚本或词表。

| 项目 | Humanization 采用的内容 | 未采用的内容 |
| :--- | :--- | :--- |
| [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing/tree/cd879d22c8588125c1869d0b443f5d8df74b4192) | `zh-CN` 长文基础，包括材料是否充足、来源核查、现实与虚构边界、改稿流程和自然中文节奏。 | 中文标点和对比句式的 house rules 只留在 `zh-CN prose`，不会成为全局规则。 |
| [yetone/kill-ai-slop](https://github.com/yetone/kill-ai-slop) | 只采用文本原则，包括用具体信息替代口号、先删除装饰再改写，以及把模式命中当作审阅线索而不是结论。 | 颜色、字体、卡片、圆角、图标、动效、按钮样式和视觉扫描器。 |
| [ehmo/slopkit (`slopbeth`)](https://github.com/ehmo/slopkit/blob/b33718bb9283c11b09567dc714f92d90ffb7bd16/skills/slopbeth/SKILL.md) | 为实体、数字、日期、URL、引语和不确定性建立证据约束账本；缺少证据时不得用虚构主张填补。 | 英文禁词、长破折号规则、项目自报评分和规避检测器的承诺。 |
| [blader/humanizer](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md) 和 [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop/blob/d30eddb9e04562234f2070b5ee63ca4649d9a05e/skills/no-ai-slop/SKILL.md) | 保留作者的事实和有效声口，优先做最小有效改动，允许 `no_change`，也不根据模式清单推断作者是否使用 AI。 | 通用声口公式和自动作者身份判断。 |

## 语言档案

这些档案是各语言的原生写作契约，不是中文规则的翻译版。

| Locale | 采用的原生项目和指南 | 采用的语言专属原则 |
| :--- | :--- | :--- |
| `zh-CN` | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing/tree/cd879d22c8588125c1869d0b443f5d8df74b4192) 和 [GB/T 15834-2011](https://openstd.samr.gov.cn/) | 中国大陆中文语序和术语、全角标点、材料驱动的长文写作，以及仅限 `zh-CN prose` 的中文 house rules。 |
| `zh-TW` | [Mozilla zh-TW style guide](https://github.com/mozilla-l10n/styleguides/blob/main/docs/zh-TW/README.md) 和 [bruce6731/anti-ai-writing-taiwan](https://github.com/bruce6731/anti-ai-writing-taiwan/tree/2c14f6a6015885b0c1cad9b54c861bc7b8a3b27d) | 采用台湾常用词、语体、标点和文化语境下的重组，并明确 `zh-TW` 不是简体转繁体。未引入 Mozilla 的产品专属术语。 |
| `en` | [Google styleguide](https://github.com/google/styleguide/tree/gh-pages/docguide)、[Microsoft Writing Style Guide](https://github.com/MicrosoftDocs/microsoft-style-guide) 和 [Digital.gov Plain Language](https://digital.gov/guides/plain-language/) | 清楚的行动者与动作关系、简洁文档、结合语境的品牌声口、地区一致性，以及英语标点的正常用法。未引入 Microsoft 专属术语。 |
| `ja` | [Mozilla Japanese style guide](https://github.com/mozilla-l10n/styleguides/blob/main/docs/ja/l10nguideline.md)、[chezou/slop-nuki](https://github.com/chezou/slop-nuki/tree/1bdf627b5991f4f806069619c9bde407960feac7)、[iKora128/stop-ai-slop-jp](https://github.com/iKora128/stop-ai-slop-jp/tree/e09d32796f253a62693885757cea484c275d06f2)、[RobTar97/japanese-writing-skills](https://github.com/RobTar97/japanese-writing-skills/tree/e4b1700464219c60da786f005a061bccffbbd4e3) 和 [coji/natural-japanese](https://github.com/coji/natural-japanese/tree/b54954f8deb4f110f0959f4e4fac295708900120) | 自然省略和语序、助词、结合语境的敬语与缓冲表达、按组件选择名词或动词形式、GUI 资源完整性，以及结合密度和体裁审阅，而不是绝对禁止某种模式。 |
| `ko` | [Mozilla Korean style guide](https://github.com/mozilla-l10n/styleguides/blob/main/docs/ko/README.md)、[dotoricode/korean-humanizer](https://github.com/dotoricode/korean-humanizer/tree/7dff5b48cc06fc4252d4766b802ecd61e62c50ad) 和 [HarryJhin/korean-writing](https://github.com/HarryJhin/korean-writing/tree/e4db3883ed76521b7a0cac30392fa67d182cc8ab) | 自然省略主语、助词和分写、`합니다`/`해요`/`다` 语体等级、保留敬语、句末形式，以及英语和日语翻译腔。未采用任意改写配额。 |
| `es` | [Mozilla Spanish style guides](https://github.com/mozilla-l10n/styleguides/tree/main/docs/es) | 性数一致、附着代词、`tú`/`usted`/`ustedes`、句首大写式 UI、地区术语、标点和英语仿译。未引入 Firefox 专属标签，也没有规定一种通用于所有西语的语体。 |

所链接的项目仍分别适用各自的许可证。[研究笔记](./research/multilingual-skill-research.md) 记录了来源证据和采用边界；复用这些项目的文字或代码前，请查阅相应仓库的许可证。Humanization 中的规则是对上述机制重新撰写的摘要。

## 安装

请让支持从 GitHub 安装 Skill 的 Agent 执行：

```text
Install the humanization Skill from https://github.com/thevenomsnake/humanization. The Skill is in the humanization/ directory.
```

安装后的目录名必须保持为 `humanization`。正确的卡片名称是 `Humanization`，使用带六条语言色带的深绿色 H 图标，说明文字为 “Natural writing and GUI copy across six locales.”。如果 Codex 显示 `活人感写作`，它展示的是旧版 `human-writing` Skill，而不是 Humanization。

<details>
<summary><strong>手动安装</strong></summary>

把仓库中的 [`humanization`](./humanization) 目录复制到 Codex Skills 目录：

```text
$CODEX_HOME/skills/humanization/
```

</details>

调用时请明确指定 locale、format 和 surface：

```text
Use $humanization with locale=ja, format=web-microcopy, and surface=error. Rewrite these error messages while preserving the CTA, brand terms, placeholders, and source resource structure.
```

公开 format 名 `web-microcopy` 覆盖 HTML、JSON、YAML、ARB、PO、源代码和设计文件中的 GUI 文字，并不只适用于网站。

运行确定性检查器时使用同样的显式路由：

```bash
python humanization/scripts/check_writing.py --locale en --format copy draft.md
python humanization/scripts/check_writing.py --locale es --format web-microcopy --source source.json target.json
```

## 3.0.0 的变化

- 将 `humanization` 定为稳定的 Skill 名和目录名，UI 显示名为 `Humanization`。
- 把运行时指南拆成一个通用契约、六个语言档案和一个 GUI 微文案模块。
- 只采用 `kill-ai-slop` 的文本原则；颜色、卡片、圆角、图标和动效等视觉规则不在范围内。
- `--locale` 和 `--format` 改为显式参数。检查器不会猜测混合文本的语言，也不会把语气判断变成硬失败。

完整历史记录见 [CHANGELOG.md](./CHANGELOG.md)。

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
| [`SKILL.md`](./humanization/SKILL.md) | 让每项任务依次经过通用、语言和格式模块。 |
| [`core.md`](./humanization/references/core.md) | 负责事实、来源、能力、隐私、CTA、品牌词、占位符和最小编辑。 |
| [`locales/`](./humanization/references/locales) | 保存六个语言的原生写作档案。 |
| [`expressive-text.md`](./humanization/references/formats/expressive-text.md) | 处理非 GUI 的产品、文档、营销、邮件和社交文字。 |
| [`gui-microcopy.md`](./humanization/references/formats/gui-microcopy.md) | 定义 GUI 组件职责和结构化资源保护。 |
| [`check_writing.py`](./humanization/scripts/check_writing.py) | 提供执行通用、语言和 GUI 检查的统一 CLI。 |
| [`check_zh_cn.py`](./humanization/scripts/check_zh_cn.py) | 将原有动作级检查器限定在 `zh-CN prose`。 |

</details>

## 归属与反馈

Humanization 以 MIT License 发布。仓库不包含第三方文章、训练语料或模型权重。

Humanization 是一个独立项目。它最初的 `zh-CN` 长文基础依据 MIT License 派生自 [KKKKhazix/human-writing v1.1.0](https://github.com/KKKKhazix/human-writing/tree/cd879d22c8588125c1869d0b443f5d8df74b4192)。上面的来源表记录了所有影响当前架构的项目或指南、从中采用的原则，以及明确排除的项目专属规则。

遇到规则冲突、误报或特定模型上的问题时，请[提交 issue](https://github.com/thevenomsnake/humanization/issues)，并附上提示词、相关输出和你预期的结果。

<p align="center">
  <sub>Humanization · 3.0.0</sub>
</p>
