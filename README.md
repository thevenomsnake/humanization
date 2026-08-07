<p align="center">
  <img src="./assets/readme-cover.svg" alt="Human Writing General" width="100%">
</p>

<p align="center">
  <a href="https://github.com/thevenomsnake/human-writing-general/releases/tag/v2.0.0"><img alt="Version 2.0.0" src="https://img.shields.io/badge/version-2.0.0-C4473A?style=flat-square"></a>
  <a href="./LICENSE"><img alt="MIT License" src="https://img.shields.io/badge/license-MIT-313131?style=flat-square"></a>
  <a href="https://github.com/thevenomsnake/human-writing-general/releases/latest"><img alt="GitHub Release" src="https://img.shields.io/github/v/release/thevenomsnake/human-writing-general?style=flat-square&color=6B6258"></a>
</p>

<p align="center">
  <a href="#快速安装">快速安装</a> ·
  <a href="#它做什么">写作流程</a> ·
  <a href="#仓库结构">仓库结构</a> ·
  <a href="https://github.com/thevenomsnake/human-writing-general/issues">提交问题</a>
</p>

> Human Writing General 让多语言作品有清楚的事实边界、说话位置和自然节奏，而不是把中文规则翻译到所有语言。

支持 `zh-CN`、`zh-TW`、`en`、`ja`、`ko`、`es` 的创作与改稿，也支持网站标题、导航、按钮、状态、错误、隐私和无障碍短文案。

## 它做什么

写作之前先解决一个前置问题：你手上有没有东西可写。

现实题材，材料不够就去查、追问或缩小题目；虚构题材可以创造人物和情节，但每个场景仍然要有目标、动作和变化。短文案不套用长文材料数量门槛。

材料过关之后管三件事：

| 事实 | 推进 | 语言 |
| :--- | :--- | :--- |
| 现实写作核准事实、数字、引语和亲历。虚构写作检查人物、行动与因果。 | 每段或每个文案单元都增加事实、动作、区别、选择或后果。 | 由目标语言档案处理词序、标点、正式程度、机器翻译痕迹和节奏。 |

初稿写完再做检查。确定性脚本只管明确字段、标点和硬禁令；自然度、语气、地区用词和翻译质量由对应语言档案人工判断。

## 快速安装

把下面这句话发给你的 Agent。

```bash
帮我安装这个skill：https://github.com/thevenomsnake/human-writing-general
```

Agent 会读取仓库、找到 `human-writing-general`，完成安装。装好之后显示名为 `Human Writing General`。

<details>
<summary><strong>Agent 不支持直接安装时</strong></summary>

从 [Releases](https://github.com/thevenomsnake/human-writing-general/releases/latest) 下载，或者把仓库里的 [`human-writing-general`](./human-writing-general) 文件夹完整复制到本机 Skills 目录。文件夹名保留 `human-writing-general`。

```text
~/.agents/skills/human-writing-general/
```

</details>

装好之后这样用：

```text
使用 $human-writing-general，用 `locale=en format=web-microcopy` 把这组产品事实写成网站短文案。
```

## 2.0.0 改了什么

2.0 把通用事实与能力边界和语言档案分开，首批支持六个 locale，并增加 web microcopy 分支。中文动作级规则只在 `zh-CN` 档案生效，英文、日文、韩文、西班牙文和台灣繁中各自维护自然表达。校验器显式接收 `--locale` 与 `--format`，不自动猜混合语言。

完整变更见 [CHANGELOG.md](./CHANGELOG.md)。

## 仓库结构

<details>
<summary><strong>展开查看完整目录</strong></summary>

```text
human-writing-general/
├── SKILL.md
├── VERSION
├── LICENSE
├── agents/
│   └── openai.yaml
├── references/
│   ├── locales/
│   │   ├── zh-CN.md
│   │   ├── zh-TW.md
│   │   ├── en.md
│   │   ├── ja.md
│   │   ├── ko.md
│   │   └── es.md
│   ├── formats/
│   │   └── web-microcopy.md
│   ├── forum-prose.md
│   ├── reality.md
│   ├── fiction.md
│   ├── formats.md
│   └── revision.md
└── scripts/
    ├── check_writing.py
    ├── check_zh_cn.py
    └── check_prose.py
```

| 位置 | 干什么的 |
| :--- | :--- |
| [`SKILL.md`](./human-writing-general/SKILL.md) | 通用事实边界、locale/format 分流和交付检查 |
| [`locales/`](./human-writing-general/references/locales) | 六个语言档案，各自维护自然表达与地区边界 |
| [`web-microcopy.md`](./human-writing-general/references/formats/web-microcopy.md) | 网站短文案的输入契约与可验证字段 |
| [`check_writing.py`](./human-writing-general/scripts/check_writing.py) | 显式 locale/format 的通用确定性校验器 |
| [`check_zh_cn.py`](./human-writing-general/scripts/check_zh_cn.py) | 原中文动作级检查器，限定在 zh-CN prose |

</details>

## 反馈

MIT 协议开源。仓库只有原创规则和工具，没有第三方文章、训练语料或模型权重。

本 fork 基于 [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing)；本地 `upstream` remote 指向上游，保留用于后续同步。

碰到规则冲突、误报或者某个模型上表现不对，欢迎[提 Issue](https://github.com/thevenomsnake/human-writing-general/issues)。附上你的提示词、模型输出片段和你觉得应该是什么样，排查起来快很多。

<p align="center">
  <sub>Human Writing General · 2.0.0</sub>
</p>
