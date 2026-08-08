<p align="center">
  <img src="./assets/readme-cover.svg" alt="Humanization" width="100%">
</p>

<p align="center">
  <strong>English</strong> ·
  <a href="./README.zh-CN.md">简体中文</a> ·
  <a href="./README.zh-TW.md">繁體中文</a> ·
  <a href="./README.ja.md">日本語</a> ·
  <a href="./README.ko.md">한국어</a> ·
  <a href="./README.es.md">Español</a>
</p>

<p align="center">
  <strong>v3.0.0</strong> · MIT · 6 locales · prose / copy / GUI microcopy
</p>

<p align="center">
  <a href="#install">Install</a> ·
  <a href="#how-it-works">How it works</a> ·
  <a href="#before-and-after">Before and after</a> ·
  <a href="#where-the-rules-come-from">Sources</a> ·
  <a href="#locale-profiles">Locale profiles</a> ·
  <a href="#repository-layout">Repository layout</a> ·
  <a href="https://github.com/thevenomsnake/humanization/issues">Issues</a>
</p>

<p align="center"><strong>Decide what belongs in the product, then write it naturally across six locales.</strong></p>

Humanization brings together practical methods from established writing, editing, localization, content-design, and anti-slop projects. It is built for people creating multilingual products: prose, stories, documentation, product content, marketing copy, email, social posts, and GUI text such as navigation, buttons, errors, empty states, confirmations, notifications, privacy notices, and accessible names. Before rewriting, it separates internal capability facts from messages users actually need on the selected surface.

**Locale profiles:** [zh-CN 简体中文](./humanization/references/locales/zh-CN.md) · [zh-TW 繁體中文](./humanization/references/locales/zh-TW.md) · [en English](./humanization/references/locales/en.md) · [ja 日本語](./humanization/references/locales/ja.md) · [ko 한국어](./humanization/references/locales/ko.md) · [es Español](./humanization/references/locales/es.md)

## How it works

Every task loads three modules, each with a narrow job.

- **Common contract:** facts, sources, capabilities, privacy, CTA, brand terms, placeholders, minimal editing, and the content existence gate.
- **Locale profile:** syntax, register or honorifics, punctuation, regional vocabulary, translationese, and natural rhythm.
- **GUI microcopy:** component-specific writing for buttons, errors, empty states, confirmations, and notifications, with protection for keys, ICU messages, variables, markup, and runtime structure.

The common contract first marks each candidate as `keep`, `rewrite`, `move`, or `remove`. If the candidate also exposes a missing action, state, or recovery path, it adds `needs_product_decision` for the underlying journey. Internal facts constrain what the product may claim, but they do not automatically become public copy. The locale profiles then decide how approved messages should sound locally. Translations may use different sentence structures and lengths, but they must preserve the same audience, action, capability boundary, privacy promise, and approved terminology.

When source material is incomplete, the Skill asks a focused question, checks a source, or narrows the claim. When a page has no supported action or recovery path, it returns `needs_product_decision` instead of hiding the product gap behind explanatory copy. Deterministic checks fail when they can prove damage; message relevance, tone, and naturalness remain contextual review decisions.

## Before and after

Humanization does not polish every true sentence into publishable copy. It first asks whether the sentence has a user-facing job on this surface.

| Before | After |
| :--- | :--- |
| “This public site has no processing service, does not provide file uploads, does not connect to external systems, and has no entry point to start a task.” | **No replacement public copy.**<br><br>**Copy disposition:** `remove`<br>**Product flow:** `needs_product_decision`. Is this page reading-only, or should visitors be able to start a task here? If analysis belongs here, implement a real entry point and CTA before writing copy. |

The internal facts stay in the capability ledger. The sentence disappears because it does not help a visitor act or decide. The missing entry point remains a separate product decision; explanatory copy cannot complete that journey.

## Where the rules come from

Humanization exists because other projects published useful writing methods and language-specific guidance. The projects below shaped its common contract, locale profiles, and editing workflow.

| Project | Contribution to Humanization |
| :--- | :--- |
| [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing/tree/cd879d22c8588125c1869d0b443f5d8df74b4192) | Provided the initial `zh-CN` long-form foundation: material sufficiency, source checks, reality and fiction boundaries, revision flow, and natural Chinese rhythm. |
| [yetone/kill-ai-slop](https://github.com/yetone/kill-ai-slop/tree/96d1ca568a1db7e1ef9a381644c744440f816ee4) | Informed the text review practice of preferring concrete information to slogans, removing decoration before rewriting, and using pattern matches to guide further review. |
| [ehmo/slopkit (`slopbeth`)](https://github.com/ehmo/slopkit/blob/b33718bb9283c11b09567dc714f92d90ffb7bd16/skills/slopbeth/SKILL.md) | Informed the evidence ledger for entities, numbers, dates, URLs, quotations, and uncertainty, keeping every claim within the available evidence. |
| [blader/humanizer](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md) and [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop/blob/d30eddb9e04562234f2070b5ee63ca4649d9a05e/skills/no-ai-slop/SKILL.md) | Informed the minimal-editing workflow: preserve the writer's facts and working voice, make the smallest useful edit, and allow `no_change`. |
| [18F/content-guide](https://github.com/18F/content-guide/tree/1b1723d3d5b8f91d92c16487c88b56265dc0ec3a) and [GOV.UK Design System](https://github.com/alphagov/govuk-design-system/tree/efb0d77d38b7ed7f921697564d2c47723d434977) | Informed the user-need gate, positive task instructions, message placement, and the requirement that errors and unavailable states give users a real next step. |
| [Shopify Polaris](https://github.com/Shopify/polaris-react-archive/blob/af6ffb66a5b1d20f6c2c898b334a1ebb53728ba2/polaris.shopify.com/content/content/fundamentals.mdx), [Carbon Design System](https://github.com/carbon-design-system/carbon-website/tree/e14433309b1dd53ec790eaa176139007ea9e9c80), and [PatternFly](https://github.com/patternfly/patternfly-org/tree/3aff87cace31c7d7e94ebae4cb35666f4f2e75d7) | Informed component-level content selection: keep only task-relevant assistance, distinguish interface states, and connect limitations to observable consequences and supported actions. |
| [ya8282/ux-writing-skill](https://github.com/ya8282/ux-writing-skill/tree/711e4162d21367bc62003e428696dc76807d56ec), [OOOOuyang/UX-writing-skill](https://github.com/OOOOuyang/UX-writing-skill/tree/fad02668533dca76d638aaacf6c2e834657df0ab), and [RobTar97/japanese-writing-skills](https://github.com/RobTar97/japanese-writing-skills/tree/e4b1700464219c60da786f005a061bccffbbd4e3) | Informed the explicit content disposition, the rule that every helper string earns its place, and the separation of user-facing recovery copy from developer diagnostics. |

## Locale profiles

Each locale profile defines native syntax, register, punctuation, terminology, translationese review, and rhythm for that language.

| Locale | Projects and guidance | Principles informed by these sources |
| :--- | :--- | :--- |
| `zh-CN` | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing/tree/cd879d22c8588125c1869d0b443f5d8df74b4192) and [GB/T 15834-2011](https://openstd.samr.gov.cn/) | Mainland Chinese syntax and terminology, full-width punctuation, material-led long-form writing, and a dedicated `zh-CN prose` house style. |
| `zh-TW` | [Mozilla zh-TW style guide](https://github.com/mozilla-l10n/styleguides/blob/main/docs/zh-TW/README.md) and [bruce6731/anti-ai-writing-taiwan](https://github.com/bruce6731/anti-ai-writing-taiwan/tree/2c14f6a6015885b0c1cad9b54c861bc7b8a3b27d) | Native `zh-TW` localization across Traditional Chinese terminology, register, punctuation, and cultural ordering. |
| `en` | [Google styleguide](https://github.com/google/styleguide/tree/gh-pages/docguide), [Microsoft Writing Style Guide](https://github.com/MicrosoftDocs/microsoft-style-guide), and [Digital.gov Plain Language](https://digital.gov/guides/plain-language/) | Clear actor and action relationships, concise documentation, contextual brand voice, regional consistency, and ordinary English punctuation. |
| `ja` | [Mozilla Japanese style guide](https://github.com/mozilla-l10n/styleguides/blob/main/docs/ja/l10nguideline.md), [chezou/slop-nuki](https://github.com/chezou/slop-nuki/tree/1bdf627b5991f4f806069619c9bde407960feac7), [iKora128/stop-ai-slop-jp](https://github.com/iKora128/stop-ai-slop-jp/tree/e09d32796f253a62693885757cea484c275d06f2), [RobTar97/japanese-writing-skills](https://github.com/RobTar97/japanese-writing-skills/tree/e4b1700464219c60da786f005a061bccffbbd4e3), and [coji/natural-japanese](https://github.com/coji/natural-japanese/tree/b54954f8deb4f110f0959f4e4fac295708900120) | Natural omission and word order, particles, honorifics and cushioning by context, component-specific noun and verb forms, GUI resource integrity, and review calibrated to density and genre. |
| `ko` | [Mozilla Korean style guide](https://github.com/mozilla-l10n/styleguides/blob/main/docs/ko/README.md), [dotoricode/korean-humanizer](https://github.com/dotoricode/korean-humanizer/tree/7dff5b48cc06fc4252d4766b802ecd61e62c50ad), and [HarryJhin/korean-writing](https://github.com/HarryJhin/korean-writing/tree/e4db3883ed76521b7a0cac30392fa67d182cc8ab) | Natural subject omission, particles and spacing, `합니다`/`해요`/`다` speech levels, honorific preservation, endings, and English and Japanese translationese. |
| `es` | [Mozilla Spanish style guides](https://github.com/mozilla-l10n/styleguides/tree/main/docs/es) | Agreement, clitics, `tú`/`usted`/`ustedes`, sentence-case UI, regional terminology, punctuation, and English calques. |

The linked projects remain under their own licenses. [The multilingual research notes](./research/multilingual-skill-research.md) and [the GUI copy existence-gate report](./research/gui-copy-existence-gate.md) record the source evidence and how each source informs Humanization; consult each linked repository's license before reusing its text or code. The project-specific instructions in Humanization are newly written from the practices summarized above.

## Install

Ask an agent that supports installing Skills from GitHub:

```text
Install the humanization Skill from https://github.com/thevenomsnake/humanization. The Skill is in the humanization/ directory.
```

The installed directory name must remain `humanization`. The correct card is named `Humanization`, uses a dark-green H icon with six language bars, and reads “Natural writing and GUI copy across six locales.” A card labeled `活人感写作` belongs to the legacy `human-writing` Skill; the metadata above identifies Humanization.

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

Audit whether existing copy belongs on its current surface before rewriting:

```text
Use $humanization with locale=zh-CN, format=web-microcopy, and surface=public-page. Decide whether each capability statement should be kept, rewritten, moved, or removed, and flag any underlying product decision.
```

The public format name `web-microcopy` covers GUI text in HTML, JSON, YAML, ARB, PO, source code, and design files across web, desktop, and mobile products.

Run the deterministic checker with the same explicit routing:

```bash
python humanization/scripts/check_writing.py --locale en --format copy draft.md
python humanization/scripts/check_writing.py --locale es --format web-microcopy --source source.json target.json
```

## What changed in 3.0.0

- Finalized `humanization` as the stable Skill and directory name, with `Humanization` as the UI display name.
- Split the runtime guidance into one common contract, six locale profiles, and one GUI microcopy module.
- Added concrete-information, restraint, and review-lead principles informed by `kill-ai-slop`.
- Added a cross-language content existence gate that separates internal capability facts from publishable user messages.
- Made `--locale` and `--format` explicit, with caller-selected routing for mixed text and warning-level review for tone judgments.

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

| Path | Purpose |
| :--- | :--- |
| [`SKILL.md`](./humanization/SKILL.md) | Routes each task through the common, locale, and format modules. |
| [`core.md`](./humanization/references/core.md) | Owns facts, sources, capabilities, privacy, CTA, brand terms, placeholders, minimal editing, and content disposition. |
| [`locales/`](./humanization/references/locales) | Holds the six native writing profiles. |
| [`expressive-text.md`](./humanization/references/formats/expressive-text.md) | Covers non-GUI product, documentation, marketing, email, and social copy. |
| [`gui-microcopy.md`](./humanization/references/formats/gui-microcopy.md) | Defines the GUI content gate, component jobs, and structured-resource protection. |
| [`check_writing.py`](./humanization/scripts/check_writing.py) | Provides the single CLI for common, locale, and GUI checks. |
| [`check_zh_cn.py`](./humanization/scripts/check_zh_cn.py) | Keeps the original action-level checker limited to `zh-CN prose`. |

</details>

## Attribution and feedback

Humanization is released under the MIT License. Its initial `zh-CN` long-form foundation comes from [KKKKhazix/human-writing v1.1.0](https://github.com/KKKKhazix/human-writing/tree/cd879d22c8588125c1869d0b443f5d8df74b4192), also under the MIT License. The source map above credits the projects and guides that informed the current architecture and describes their contribution.

For rule conflicts, false positives, or model-specific failures, [open an issue](https://github.com/thevenomsnake/humanization/issues) with the prompt, the relevant output, and the result you expected.

<p align="center">
  <sub>Humanization · 3.0.0</sub>
</p>
