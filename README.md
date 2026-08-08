<p align="center">
  <img src="./assets/readme-cover.svg" alt="Humanization" width="100%">
</p>

<p align="center">
  <strong>v3.0.0</strong> · MIT · 6 locales · prose / copy / web GUI
</p>

<p align="center">
  <a href="#快速安装">快速安装</a> ·
  <a href="#它做什么">写作流程</a> ·
  <a href="#仓库结构">仓库结构</a> ·
  <a href="https://github.com/thevenomsnake/humanization/issues">提交问题</a>
</p>

<p align="center"><strong>Humanization 让多语言作品有清楚的事实边界、说话位置和自然节奏。</strong></p>

支持 `zh-CN`、`zh-TW`、`en`、`ja`、`ko`、`es` 的所有表达性文字，包含文章、故事、文档、产品说明、营销文案、邮件、社交内容，以及网站标题、导航、按钮、状态、错误、隐私和无障碍文本。

## 它做什么

Humanization 只有三层所有权。

- **通用契约** 只管事实、来源、能力、隐私、CTA、品牌词、占位符和最小编辑。
- **语言档案** 分别处理语序、敬语或语体、标点、地区词、翻译腔和自然节奏。
- **GUI 文案** 按按钮、错误、空状态、确认、通知等组件处理，并保护 key、ICU、变量、markup 和运行时结构。

现实材料不足时研究、追问或缩小主张；原文已经成立时不强行改写。确定性脚本只阻断可证明的输入或资源损坏，词汇、语气、地区用词和自然度仍由对应语言档案判断。

## 快速安装

把下面这句话发给你的 Agent。

```bash
帮我安装这个skill：https://github.com/thevenomsnake/humanization
```

Agent 会读取仓库、找到 `humanization`，完成安装。装好之后显示名为 `Humanization`。

<details>
<summary><strong>Agent 不支持直接安装时</strong></summary>

从 [Releases](https://github.com/thevenomsnake/humanization/releases/latest) 下载，或者把仓库里的 [`humanization`](./humanization) 文件夹完整复制到本机 Skills 目录。文件夹名保留 `humanization`。

```text
~/.agents/skills/humanization/
```

</details>

装好之后这样用：

```text
使用 $humanization，用 `locale=en format=web-microcopy surface=error` 改写这组错误文案；保留 CTA、品牌词、placeholder 和源资源结构。
```

## 3.0.0 改了什么

3.0 将稳定标识定稿为 `humanization`，UI 显示名为 `Humanization`。2.1 吸收 `kill-ai-slop` 的文本部分，扩展到所有表达性文字，命中模板句只给人工判断，不吸收网页视觉规则。2.0 的通用事实核心、六个 locale 和 web microcopy 分支继续保留。校验器显式接收 `--locale` 与 `--format`，不自动猜混合语言。

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

MIT 协议开源。仓库不包含第三方文章、训练语料或模型权重；通用契约注明了 `kill-ai-slop` 的 Apache-2.0 来源与“只吸收文本、不吸收视觉”的适配范围。

本 fork 基于 [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing)；本地 `upstream` remote 指向上游，保留用于后续同步。

碰到规则冲突、误报或者某个模型上表现不对，欢迎[提 Issue](https://github.com/thevenomsnake/humanization/issues)。附上你的提示词、模型输出片段和你觉得应该是什么样，排查起来快很多。

<p align="center">
  <sub>Humanization · 3.0.0</sub>
</p>
