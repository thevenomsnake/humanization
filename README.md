<p align="center">
  <img src="./assets/readme-cover.svg" alt="Humanization" width="100%">
</p>

<p align="center">
  <strong>v3.0.0</strong> · MIT · 6 locales · prose / copy / GUI microcopy
</p>

<p align="center">
  <a href="#install">Install</a> ·
  <a href="#how-it-works">How it works</a> ·
  <a href="#where-the-rules-come-from">Sources</a> ·
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

## Where the rules come from

Humanization adapts editing mechanisms from other projects and rewrites them for this architecture. It does not paste their prose, examples, scripts, or word lists.

| Project | What Humanization adopted | What stayed out |
| :--- | :--- | :--- |
| [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing/tree/cd879d22c8588125c1869d0b443f5d8df74b4192) | The `zh-CN` long-form foundation: material sufficiency, source checks, reality/fiction boundaries, revision flow, and natural Chinese rhythm. | Chinese punctuation and contrast-sentence house rules remain inside `zh-CN prose`; they are not global rules. |
| [yetone/kill-ai-slop](https://github.com/yetone/kill-ai-slop) | Text-only principles: prefer concrete information to slogans, remove decoration before rewriting, and treat pattern matches as review leads rather than verdicts. | Colors, typography, cards, corners, icons, motion, button styling, and visual scanners. |
| [ehmo/slopkit (`slopbeth`)](https://github.com/ehmo/slopkit/blob/b33718bb9283c11b09567dc714f92d90ffb7bd16/skills/slopbeth/SKILL.md) | The evidence-bound ledger for entities, numbers, dates, URLs, quotations, and uncertainty; missing evidence must not be filled with invented claims. | English word bans, em-dash rules, self-reported scores, and detector-proof claims. |
| [blader/humanizer](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md) and [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop/blob/d30eddb9e04562234f2070b5ee63ca4649d9a05e/skills/no-ai-slop/SKILL.md) | Preserve the writer's facts and working voice, prefer the smallest useful edit, allow `no_change`, and never infer AI authorship from a pattern list. | Universal voice formulas and automatic authorship judgments. |

## Locale profiles

The profiles are native writing contracts, not translations of the Chinese rules.

| Locale | Native projects and guidance used | Language-specific principles adopted |
| :--- | :--- | :--- |
| `zh-CN` | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing/tree/cd879d22c8588125c1869d0b443f5d8df74b4192) and [GB/T 15834-2011](https://openstd.samr.gov.cn/) | Mainland Chinese syntax and terminology, full-width punctuation, material-led long-form writing, and Chinese house rules confined to `zh-CN prose`. |
| `zh-TW` | [Mozilla zh-TW style guide](https://github.com/mozilla-l10n/styleguides/blob/main/docs/zh-TW/README.md) and [bruce6731/anti-ai-writing-taiwan](https://github.com/bruce6731/anti-ai-writing-taiwan/tree/2c14f6a6015885b0c1cad9b54c861bc7b8a3b27d) | Taiwan vocabulary, register, punctuation, cultural reordering, and the rule that `zh-TW` is not a Simplified-to-Traditional character conversion. Product-specific Mozilla terms were not imported. |
| `en` | [Google styleguide](https://github.com/google/styleguide/tree/gh-pages/docguide), [Microsoft Writing Style Guide](https://github.com/MicrosoftDocs/microsoft-style-guide), and [Digital.gov Plain Language](https://digital.gov/guides/plain-language/) | Clear actor/action relationships, concise documentation, contextual brand voice, regional consistency, and ordinary use of English punctuation. Microsoft-specific terminology was not imported. |
| `ja` | [Mozilla Japanese style guide](https://github.com/mozilla-l10n/styleguides/blob/main/docs/ja/l10nguideline.md), [chezou/slop-nuki](https://github.com/chezou/slop-nuki/tree/1bdf627b5991f4f806069619c9bde407960feac7), [iKora128/stop-ai-slop-jp](https://github.com/iKora128/stop-ai-slop-jp/tree/e09d32796f253a62693885757cea484c275d06f2), [RobTar97/japanese-writing-skills](https://github.com/RobTar97/japanese-writing-skills/tree/e4b1700464219c60da786f005a061bccffbbd4e3), and [coji/natural-japanese](https://github.com/coji/natural-japanese/tree/b54954f8deb4f110f0959f4e4fac295708900120) | Natural omission and word order, particles, honorifics and cushioning by context, component-specific noun/verb forms, GUI resource integrity, and density/genre-aware review instead of absolute pattern bans. |
| `ko` | [Mozilla Korean style guide](https://github.com/mozilla-l10n/styleguides/blob/main/docs/ko/README.md), [dotoricode/korean-humanizer](https://github.com/dotoricode/korean-humanizer/tree/7dff5b48cc06fc4252d4766b802ecd61e62c50ad), and [HarryJhin/korean-writing](https://github.com/HarryJhin/korean-writing/tree/e4db3883ed76521b7a0cac30392fa67d182cc8ab) | Natural subject omission, particles and spacing, `합니다`/`해요`/`다` speech levels, honorific preservation, endings, and English/Japanese translationese. Arbitrary rewrite quotas were rejected. |
| `es` | [Mozilla Spanish style guides](https://github.com/mozilla-l10n/styleguides/tree/main/docs/es) | Agreement, clitics, `tú`/`usted`/`ustedes`, sentence-case UI, regional terminology, punctuation, and English calques. Firefox-specific labels and one universal Spanish register were not imported. |

The linked projects remain under their own licenses. [The research notes](./research/multilingual-skill-research.md) record the source evidence and adoption boundaries; consult each linked repository's license before reusing its text or code. The rules in Humanization are newly written summaries of the mechanisms above.

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

This fork is based on [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) and retains an `upstream` remote for synchronization. The source map above distinguishes the rules that informed Humanization from the project-specific rules that were deliberately excluded.

For rule conflicts, false positives, or model-specific failures, [open an issue](https://github.com/thevenomsnake/humanization/issues) with the prompt, the relevant output, and the result you expected.

<p align="center">
  <sub>Humanization · 3.0.0</sub>
</p>
