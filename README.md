<p align="center">
  <img src="./assets/readme-cover.svg" alt="Humanization" width="100%">
</p>

<p align="center">
  <strong>v3.0.0</strong> · MIT · 6 locales · prose / copy / web GUI
</p>

<p align="center">
  <a href="#快速安装">快速安装</a> ·
  <a href="#它做什么">工作方式</a> ·
  <a href="#仓库结构">仓库结构</a> ·
  <a href="https://github.com/thevenomsnake/humanization/issues">提交问题</a>
</p>

<p align="center"><strong>Humanization 把同一组事实写成六种语言里各自自然的文字。</strong></p>

面向 `zh-CN`、`zh-TW`、`en`、`ja`、`ko`、`es` 的文章、故事、文档、产品说明、营销文案、邮件和社交内容，也处理导航、按钮、错误、空状态、通知、隐私说明与无障碍名称等 GUI 文案。

## 它做什么

写作和改稿分成三层，每层只管一件事。

- **通用契约** 只管事实、来源、能力、隐私、CTA、品牌词、占位符和最小编辑。
- **语言档案** 分别处理语序、敬语或语体、标点、地区词、翻译腔和自然节奏。
- **GUI 文案** 按按钮、错误、空状态、确认、通知等组件处理，并保护 key、ICU、变量、markup 和运行时结构。

这里没有把中文规则翻译五遍。英文中的冒号和 em dash 是正常工具；日语和韩语需要处理省略、敬语与句尾；西班牙语要区分地区词和称呼；`zh-TW` 也按台湾用词与标点独立处理。

现实材料不够时，先补查来源、追问或缩小主张。原文已经成立就停手。确定性脚本只阻断能够证明的输入或资源损坏，词汇、语气、地区用词和自然度仍由对应语言档案判断。

## 快速安装

在支持从 GitHub 安装 Skill 的 Agent 中，直接发：

```text
请从 https://github.com/thevenomsnake/humanization 安装 humanization Skill。
```

安装后的技能目录名应为 `humanization`，界面显示名为 `Humanization`。

<details>
<summary><strong>Agent 不支持直接安装时</strong></summary>

把仓库里的 [`humanization`](./humanization) 文件夹完整复制到 Codex Skills 目录。文件夹名保留 `humanization`。

```text
$CODEX_HOME/skills/humanization/
```

</details>

装好之后这样用：

```text
使用 $humanization，locale=en，format=web-microcopy，surface=error。改写这组错误文案，保留 CTA、品牌词、placeholder 和源资源结构。
```

## 3.0.0 改了什么

- 稳定标识定为 `humanization`，界面显示名为 `Humanization`。
- 规则拆成通用契约、六个语言档案和 GUI 文案模块。
- 只吸收 `kill-ai-slop` 的文本原则，不引入颜色、卡片、圆角或动效等视觉规则。
- 校验器显式接收 `--locale` 与 `--format`，不猜测混合文本的语言，也不把语气判断当成硬错误。

完整变更见 [CHANGELOG.md](./CHANGELOG.md)。

## 仓库结构

<details>
<summary><strong>展开查看完整目录</strong></summary>

```text
humanization/
├── SKILL.md
├── VERSION
├── LICENSE
├── agents/
│   └── openai.yaml
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

| 位置 | 干什么的 |
| :--- | :--- |
| [`SKILL.md`](./humanization/SKILL.md) | 只负责 core、locale 和 format 路由 |
| [`core.md`](./humanization/references/core.md) | 事实、来源、能力、隐私、CTA、品牌词、占位符和最小编辑 |
| [`locales/`](./humanization/references/locales) | 六个语言档案，各自维护自然表达与地区边界 |
| [`expressive-text.md`](./humanization/references/formats/expressive-text.md) | 非 GUI 的产品、文档、营销、邮件和社交文字 |
| [`gui-microcopy.md`](./humanization/references/formats/gui-microcopy.md) | GUI 组件职责和结构化资源保护 |
| [`check_writing.py`](./humanization/scripts/check_writing.py) | 汇总 common、locale 和 GUI 检查的唯一 CLI |
| [`check_zh_cn.py`](./humanization/scripts/check_zh_cn.py) | 原中文动作级检查器，限定在 zh-CN prose |

</details>

## 反馈

本项目使用 MIT 许可证，仓库不包含第三方文章、训练语料或模型权重。

本 fork 基于 [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing)，维护时通过 `upstream` remote 同步原项目。文本原则参考 [yetone/kill-ai-slop](https://github.com/yetone/kill-ai-slop)，该项目使用 Apache-2.0 许可证；这里只吸收文字部分。

碰到规则冲突、误报或者某个模型上表现不对，欢迎[提 Issue](https://github.com/thevenomsnake/humanization/issues)。附上你的提示词、模型输出片段和你觉得应该是什么样，排查起来快很多。

<p align="center">
  <sub>Humanization · 3.0.0</sub>
</p>
