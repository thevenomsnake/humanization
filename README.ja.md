<p align="center">
  <img src="./assets/readme-cover.svg" alt="Humanization" width="100%">
</p>

<p align="center">
  <a href="./README.md">English</a> ·
  <a href="./README.zh-CN.md">简体中文</a> ·
  <a href="./README.zh-TW.md">繁體中文</a> ·
  <strong>日本語</strong> ·
  <a href="./README.ko.md">한국어</a> ·
  <a href="./README.es.md">Español</a>
</p>

<p align="center">
  <strong>v3.0.0</strong> · MIT · 6ロケール · prose / copy / GUI microcopy
</p>

<p align="center">
  <a href="#インストール">インストール</a> ·
  <a href="#仕組み">仕組み</a> ·
  <a href="#ルールの出典">出典</a> ·
  <a href="#ロケールプロファイル">ロケールプロファイル</a> ·
  <a href="#リポジトリ構成">リポジトリ構成</a> ·
  <a href="https://github.com/thevenomsnake/humanization/issues">Issues</a>
</p>

<p align="center"><strong>ある言語のルールを別の言語へ持ち込まず、6つのロケールで文章を作成・推敲します。</strong></p>

Humanizationは、文章、物語、ドキュメント、製品コンテンツ、マーケティングコピー、メール、ソーシャル投稿に対応する、独立して保守されているCodex Skillです。ナビゲーション、ボタン、エラー、空状態、確認、通知、プライバシー通知、アクセシブルネームなどのGUIテキストも扱います。

**ロケールプロファイル:** [zh-CN 简体中文](./humanization/references/locales/zh-CN.md) · [zh-TW 繁體中文](./humanization/references/locales/zh-TW.md) · [en English](./humanization/references/locales/en.md) · [ja 日本語](./humanization/references/locales/ja.md) · [ko 한국어](./humanization/references/locales/ko.md) · [es Español](./humanization/references/locales/es.md)

## 仕組み

すべてのタスクで、役割を限定した3つのモジュールを読み込みます。

- **共通契約:** 事実、出典、機能、プライバシー、CTA、ブランド用語、プレースホルダー、最小限の編集。
- **ロケールプロファイル:** 構文、文体または敬語、句読点、地域語彙、翻訳調、自然なリズム。
- **GUIマイクロコピー:** ボタン、エラー、空状態、確認、通知に応じた文言と、key、ICUメッセージ、変数、markup、ランタイム構造の保護。

共通契約は、事実に関する主張と製品の約束を言語間で変えません。各ロケールプロファイルは、その制約を現地でどう自然に表現するかを決めます。翻訳では文の構造や長さを変えられますが、対象読者、アクション、機能の境界、プライバシー上の約束、承認済み用語は同じままにします。

元資料が不十分な場合、Skillは要点を絞って質問するか、出典を確認するか、主張の範囲を狭めます。原文に問題がなければ変更しません。自動チェックでエラーにするのは、破損を証明できる場合だけです。トーンと自然さは、選択したロケールプロファイルに基づくレビュー判断として残します。

## ルールの出典

Humanizationは、他のプロジェクトから編集の仕組みを取り入れ、このアーキテクチャ向けに書き直しています。各プロジェクトの文章、例、スクリプト、単語リストを転載しているわけではありません。

| プロジェクト | Humanizationが採用したもの | 採用しなかったもの |
| :--- | :--- | :--- |
| [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing/tree/cd879d22c8588125c1869d0b443f5d8df74b4192) | `zh-CN`長文の基礎。資料の充足度、出典チェック、現実とフィクションの境界、推敲フロー、自然な中国語のリズム。 | 中国語の句読点と対比表現に関するハウスルールは`zh-CN prose`の内部に限定し、グローバルルールにはしていません。 |
| [yetone/kill-ai-slop](https://github.com/yetone/kill-ai-slop) | テキストに関する原則のみ。スローガンより具体的な情報を優先し、書き直す前に装飾を取り除き、パターン一致を断定ではなくレビューの手掛かりとして扱うこと。 | 色、タイポグラフィ、カード、角丸、アイコン、モーション、ボタンのスタイル、視覚スキャナー。 |
| [ehmo/slopkit (`slopbeth`)](https://github.com/ehmo/slopkit/blob/b33718bb9283c11b09567dc714f92d90ffb7bd16/skills/slopbeth/SKILL.md) | エンティティ、数値、日付、URL、引用、不確実性を証拠に結び付ける台帳。証拠がない箇所を架空の主張で埋めてはいけないこと。 | 英語の禁止語、em dashのルール、自己申告スコア、検出器を回避できるという主張。 |
| [blader/humanizer](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md)と[petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop/blob/d30eddb9e04562234f2070b5ee63ca4649d9a05e/skills/no-ai-slop/SKILL.md) | 書き手の事実と機能している声を保ち、有用な最小限の編集を優先し、`no_change`を認め、パターンリストからAIによる執筆だと推測しないこと。 | 普遍的な声の公式と、自動的な著者判定。 |

## ロケールプロファイル

各プロファイルは中国語ルールの翻訳ではなく、その言語固有の執筆契約です。

| ロケール | 参照したネイティブプロジェクトとガイダンス | 採用した言語固有の原則 |
| :--- | :--- | :--- |
| `zh-CN` | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing/tree/cd879d22c8588125c1869d0b443f5d8df74b4192)、[GB/T 15834-2011](https://openstd.samr.gov.cn/) | 中国大陸の中国語に合う構文と用語、全角句読点、資料を軸にした長文、中国語のハウスルールを`zh-CN prose`に限定すること。 |
| `zh-TW` | [Mozilla zh-TW style guide](https://github.com/mozilla-l10n/styleguides/blob/main/docs/zh-TW/README.md)、[bruce6731/anti-ai-writing-taiwan](https://github.com/bruce6731/anti-ai-writing-taiwan/tree/2c14f6a6015885b0c1cad9b54c861bc7b8a3b27d) | 台湾の語彙、文体、句読点、文化に合わせた並べ替え、そして`zh-TW`を簡体字から繁体字への単なる文字変換として扱わないこと。Mozilla製品固有の用語は取り込んでいません。 |
| `en` | [Google styleguide](https://github.com/google/styleguide/tree/gh-pages/docguide)、[Microsoft Writing Style Guide](https://github.com/MicrosoftDocs/microsoft-style-guide)、[Digital.gov Plain Language](https://digital.gov/guides/plain-language/) | 明確な主体と動作の関係、簡潔なドキュメント、文脈に合うブランドボイス、地域内の一貫性、英語の句読点を通常どおり使うこと。Microsoft固有の用語は取り込んでいません。 |
| `ja` | [Mozilla Japanese style guide](https://github.com/mozilla-l10n/styleguides/blob/main/docs/ja/l10nguideline.md)、[chezou/slop-nuki](https://github.com/chezou/slop-nuki/tree/1bdf627b5991f4f806069619c9bde407960feac7)、[iKora128/stop-ai-slop-jp](https://github.com/iKora128/stop-ai-slop-jp/tree/e09d32796f253a62693885757cea484c275d06f2)、[RobTar97/japanese-writing-skills](https://github.com/RobTar97/japanese-writing-skills/tree/e4b1700464219c60da786f005a061bccffbbd4e3)、[coji/natural-japanese](https://github.com/coji/natural-japanese/tree/b54954f8deb4f110f0959f4e4fac295708900120) | 自然な省略と語順、助詞、文脈に応じた敬語とクッション表現、コンポーネントごとの名詞形・動詞形、GUIリソースの完全性、絶対的なパターン禁止ではなく密度とジャンルを考慮したレビュー。 |
| `ko` | [Mozilla Korean style guide](https://github.com/mozilla-l10n/styleguides/blob/main/docs/ko/README.md)、[dotoricode/korean-humanizer](https://github.com/dotoricode/korean-humanizer/tree/7dff5b48cc06fc4252d4766b802ecd61e62c50ad)、[HarryJhin/korean-writing](https://github.com/HarryJhin/korean-writing/tree/e4db3883ed76521b7a0cac30392fa67d182cc8ab) | 自然な主語の省略、助詞と分かち書き、`합니다`/`해요`/`다`の文体レベル、敬語の保持、文末表現、英語・日本語の翻訳調。恣意的な書き換えノルマは採用していません。 |
| `es` | [Mozilla Spanish style guides](https://github.com/mozilla-l10n/styleguides/tree/main/docs/es) | 性数一致、接語、`tú`/`usted`/`ustedes`、sentence caseのUI、地域用語、句読点、英語の直訳表現。Firefox固有のラベルと、スペイン語全体に一律適用する文体は取り込んでいません。 |

リンク先のプロジェクトには、それぞれ固有のライセンスが適用されます。[調査ノート](./research/multilingual-skill-research.md)には、出典の根拠と採用範囲が記録されています。文章やコードを再利用する前に、各リポジトリのライセンスを確認してください。Humanizationのルールは、上記の仕組みを新たに要約して書いたものです。

## インストール

GitHubからSkillをインストールできるエージェントに、次のように依頼します。

```text
https://github.com/thevenomsnake/humanization から humanization Skill をインストールしてください。Skill は humanization/ ディレクトリにあります。
```

インストール先のディレクトリ名は`humanization`のままにしてください。正しいカードの名前は`Humanization`で、6本の言語バーが付いた濃緑色のHアイコンを使用し、「Natural writing and GUI copy across six locales.」と表示されます。Codexに`活人感写作`と表示される場合、それはHumanizationではなく、従来の`human-writing` Skillです。

<details>
<summary><strong>手動インストール</strong></summary>

リポジトリの[`humanization`](./humanization)ディレクトリをCodexのSkillsディレクトリへコピーします。

```text
$CODEX_HOME/skills/humanization/
```

</details>

使用時には、ロケール、フォーマット、対象を明示します。

```text
locale=ja、format=web-microcopy、surface=error を指定して $humanization を使用してください。CTA、ブランド用語、プレースホルダー、元リソースの構造を保ったまま、これらのエラーメッセージを書き直してください。
```

公開フォーマット名`web-microcopy`は、HTML、JSON、YAML、ARB、PO、ソースコード、デザインファイル内のGUIテキストを対象とします。ウェブサイトだけに限定されません。

同じ明示的なルーティングで自動チェッカーを実行します。

```bash
python humanization/scripts/check_writing.py --locale en --format copy draft.md
python humanization/scripts/check_writing.py --locale es --format web-microcopy --source source.json target.json
```

## 3.0.0での変更点

- 安定したSkill名およびディレクトリ名を`humanization`、UI表示名を`Humanization`に確定しました。
- ランタイムガイダンスを、1つの共通契約、6つのロケールプロファイル、1つのGUIマイクロコピーモジュールに分割しました。
- `kill-ai-slop`からテキストの原則だけを採用しました。色、カード、角丸、アイコン、モーションに関する視覚ルールは対象外です。
- `--locale`と`--format`を必須にしました。チェッカーは混在するテキストの言語を推測せず、トーンの判断をハードエラーにしません。

完全な履歴は[CHANGELOG.md](./CHANGELOG.md)を参照してください。

## リポジトリ構成

<details>
<summary><strong>ディレクトリ全体を表示</strong></summary>

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

| パス | 役割 |
| :--- | :--- |
| [`SKILL.md`](./humanization/SKILL.md) | 各タスクを共通、ロケール、フォーマットの各モジュールへ振り分けます。 |
| [`core.md`](./humanization/references/core.md) | 事実、出典、機能、プライバシー、CTA、ブランド用語、プレースホルダー、最小限の編集を管理します。 |
| [`locales/`](./humanization/references/locales) | 各言語向けの6つの執筆プロファイルを収録します。 |
| [`expressive-text.md`](./humanization/references/formats/expressive-text.md) | GUI以外の製品、ドキュメント、マーケティング、メール、ソーシャルコピーを扱います。 |
| [`gui-microcopy.md`](./humanization/references/formats/gui-microcopy.md) | GUIコンポーネントの役割と、構造化リソースの保護を定義します。 |
| [`check_writing.py`](./humanization/scripts/check_writing.py) | 共通、ロケール、GUIチェック用の単一CLIを提供します。 |
| [`check_zh_cn.py`](./humanization/scripts/check_zh_cn.py) | 従来のアクションレベルのチェッカーを`zh-CN prose`に限定します。 |

</details>

## 帰属とフィードバック

HumanizationはMIT Licenseで公開されています。このリポジトリには、第三者の記事、学習コーパス、モデルウェイトは含まれていません。

Humanizationは独立したプロジェクトです。最初の`zh-CN`長文基盤は、MIT Licenseの下で[KKKKhazix/human-writing v1.1.0](https://github.com/KKKKhazix/human-writing/tree/cd879d22c8588125c1869d0b443f5d8df74b4192)から派生しました。上記の出典一覧には、現在のアーキテクチャに影響を与えたすべてのプロジェクトやガイド、各出典から採用した原則、意図的に除外したプロジェクト固有のルールを記録しています。

ルールの衝突、誤検出、モデル固有の不具合については、プロンプト、該当する出力、期待した結果を添えて[issueを作成してください](https://github.com/thevenomsnake/humanization/issues)。

<p align="center">
  <sub>Humanization · 3.0.0</sub>
</p>
