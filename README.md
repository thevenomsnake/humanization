<p align="center">
  <img src="./assets/readme-cover.svg" alt="Humanization" width="100%">
</p>

<p align="center">
  <strong>v3.0.0</strong> · MIT · 6 locales · prose / copy / GUI microcopy
</p>

<p align="center">
  <a href="#install">Install</a> ·
  <a href="#how-it-works">How it works</a> ·
  <a href="#locale-profiles">Locale profiles</a> ·
  <a href="#repository-layout">Repository layout</a> ·
  <a href="https://github.com/thevenomsnake/humanization/issues">Issues</a>
</p>

<p align="center"><strong>Write and revise text in six locales without carrying one language's rules into another.</strong></p>

Humanization is a Codex Skill for prose, stories, documentation, product content, marketing copy, email, and social posts. It also handles GUI text such as navigation, buttons, errors, empty states, confirmations, notifications, privacy notices, and accessible names.

**Locale profiles:** [zh-CN 简体中文](./humanization/references/locales/zh-CN.md) · [zh-TW 台灣繁體中文](./humanization/references/locales/zh-TW.md) · [en English](./humanization/references/locales/en.md) · [ja 日本語](./humanization/references/locales/ja.md) · [ko 한국어](./humanization/references/locales/ko.md) · [es Español](./humanization/references/locales/es.md)

## How it works

Every task loads three modules, each with a narrow job.

- **Common contract:** facts, sources, capabilities, privacy, CTA, brand terms, placeholders, and minimal editing.
- **Locale profile:** syntax, register or honorifics, punctuation, regional vocabulary, translationese, and natural rhythm.
- **GUI microcopy:** component-specific writing for buttons, errors, empty states, confirmations, and notifications, with protection for keys, ICU messages, variables, markup, and runtime structure.

The common contract keeps factual claims and product promises stable across languages. The locale profiles decide how those constraints should sound locally. Translations may use different sentence structures and lengths, but they must preserve the same audience, action, capability boundary, privacy promise, and approved terminology.

When source material is incomplete, the Skill asks a focused question, checks a source, or narrows the claim. When the original already works, it leaves it alone. Deterministic checks only fail on damage they can prove; tone and naturalness remain review decisions owned by the selected locale profile.

## Locale profiles

The profiles are native writing contracts, not translations of the Chinese rules.

| Locale | What its profile owns |
| :--- | :--- |
| `zh-CN` | Mainland Chinese syntax and terms, full-width punctuation, and Chinese long-form rules confined to `zh-CN prose`. |
| `zh-TW` | Taiwan usage, terminology, punctuation, and register. It is not a Simplified-to-Traditional character conversion. |
| `en` | English clause structure, register, regional spelling policy, punctuation, and common translationese. Colons and em dashes remain normal tools. |
| `ja` | Natural omission, particles, modifier order, `です・ます` or plain style, honorifics, and component-appropriate forms. |
| `ko` | Korean word order, particles, spacing, speech level, honorifics, endings, and source-language interference. |
| `es` | Agreement, clitics, forms of address, punctuation, regional vocabulary, and English calques. |

## Install

Ask an agent that supports installing Skills from GitHub:

```text
Install the humanization Skill from https://github.com/thevenomsnake/humanization. The Skill is in the humanization/ directory.
```

The installed directory name must remain `humanization`. Its UI display name is `Humanization`.

<details>
<summary><strong>Manual installation</strong></summary>

Copy the repository's [`humanization`](./humanization) directory into your Codex Skills directory:

```text
$CODEX_HOME/skills/humanization/
```

</details>

Use it with an explicit locale, format, and surface:

```text
Use $humanization with locale=ja, format=web-microcopy, and surface=error. Rewrite these error messages while preserving the CTA, brand terms, placeholders, and source resource structure.
```

The public format name `web-microcopy` covers GUI text in HTML, JSON, YAML, ARB, PO, source code, and design files. It is not limited to websites.

Run the deterministic checker with the same explicit routing:

```bash
python humanization/scripts/check_writing.py --locale en --format copy draft.md
python humanization/scripts/check_writing.py --locale es --format web-microcopy --source source.json target.json
```

## What changed in 3.0.0

- Finalized `humanization` as the stable Skill and directory name, with `Humanization` as the UI display name.
- Split the runtime guidance into one common contract, six locale profiles, and one GUI microcopy module.
- Adopted only the text principles from `kill-ai-slop`; visual rules for colors, cards, corners, icons, and motion are out of scope.
- Made `--locale` and `--format` explicit. The checker does not guess the language of mixed text or turn tone judgments into hard failures.

See [CHANGELOG.md](./CHANGELOG.md) for the complete history.

## Repository layout

<details>
<summary><strong>Show the full directory</strong></summary>

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

| Path | Purpose |
| :--- | :--- |
| [`SKILL.md`](./humanization/SKILL.md) | Routes each task through the common, locale, and format modules. |
| [`core.md`](./humanization/references/core.md) | Owns facts, sources, capabilities, privacy, CTA, brand terms, placeholders, and minimal editing. |
| [`locales/`](./humanization/references/locales) | Holds the six native writing profiles. |
| [`expressive-text.md`](./humanization/references/formats/expressive-text.md) | Covers non-GUI product, documentation, marketing, email, and social copy. |
| [`gui-microcopy.md`](./humanization/references/formats/gui-microcopy.md) | Defines GUI component jobs and structured-resource protection. |
| [`check_writing.py`](./humanization/scripts/check_writing.py) | Provides the single CLI for common, locale, and GUI checks. |
| [`check_zh_cn.py`](./humanization/scripts/check_zh_cn.py) | Keeps the original action-level checker limited to `zh-CN prose`. |

</details>

## Attribution and feedback

Humanization is released under the MIT License. The repository does not include third-party articles, training corpora, or model weights.

This fork is based on [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) and retains an `upstream` remote for synchronization. Its text guidance also draws on [yetone/kill-ai-slop](https://github.com/yetone/kill-ai-slop), which is licensed under Apache-2.0. No visual design rules are copied into this Skill.

For rule conflicts, false positives, or model-specific failures, [open an issue](https://github.com/thevenomsnake/humanization/issues) with the prompt, the relevant output, and the result you expected.

<p align="center">
  <sub>Humanization · 3.0.0</sub>
</p>
