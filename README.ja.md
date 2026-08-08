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
  <a href="#修正前と修正後">修正前と修正後</a> ·
  <a href="#ルールの出典">出典</a> ·
  <a href="#ロケールプロファイル">ロケールプロファイル</a> ·
  <a href="#リポジトリ構成">リポジトリ構成</a> ·
  <a href="https://github.com/thevenomsnake/humanization/issues">Issues</a>
</p>

<p align="center"><strong>プロダクトに何を載せるかを決め、6つのロケールで自然に伝えます。</strong></p>

Humanizationは、実績のあるライティング、編集、ローカライゼーション、コンテンツデザイン、anti-slopプロジェクトの実践知を集約したCodex Skillです。多言語プロダクトを作る人に向けて、文章、物語、ドキュメント、製品コンテンツ、マーケティングコピー、メール、ソーシャル投稿を支援します。ナビゲーション、ボタン、エラー、空状態、確認、通知、プライバシー通知、アクセシブルネームなどのGUIテキストにも対応します。書き直す前に、内部の機能情報と、対象の画面でユーザーに本当に必要なメッセージを切り分けます。

**ロケールプロファイル:** [zh-CN 简体中文](./humanization/references/locales/zh-CN.md) · [zh-TW 繁體中文](./humanization/references/locales/zh-TW.md) · [en English](./humanization/references/locales/en.md) · [ja 日本語](./humanization/references/locales/ja.md) · [ko 한국어](./humanization/references/locales/ko.md) · [es Español](./humanization/references/locales/es.md)

## 仕組み

すべてのタスクで、役割の異なる3つのモジュールを読み込みます。

- **共通契約:** 事実、出典、機能、プライバシー、CTA、ブランド用語、プレースホルダー、最小限の編集、コンテンツ掲載判定。
- **ロケールプロファイル:** 構文、文体または敬語、句読点、地域語彙、翻訳調、自然なリズム。
- **GUIマイクロコピー:** ボタン、エラー、空状態、確認、通知に応じた文言と、key、ICUメッセージ、変数、markup、ランタイム構造の保護。

共通契約では、候補ごとに`keep`、`rewrite`、`move`、`remove`のいずれかを最初に付けます。その候補から未実装の操作、状態、復旧手段が見つかった場合は、根本の導線に`needs_product_decision`も付けます。内部情報はプロダクトが主張できる範囲を定め、掲載判定が公開文にする内容を選びます。各ロケールプロファイルは、掲載が決まったメッセージを対象言語で自然に表現する方法を決めます。翻訳ごとに文の構造や長さが変わっても、対象読者、アクション、機能の範囲、プライバシー上の約束、承認済み用語は共通です。

元資料が不十分な場合、Skillは要点を絞って質問するか、出典を確認するか、主張の範囲を狭めます。ページに実装済みの操作や復旧手段がなければ、製品側で判断できるよう`needs_product_decision`を返します。自動チェックは、破損を証明できた場合にエラーを返します。メッセージの必要性、トーン、自然さは文脈に沿って人が確認します。

## 修正前と修正後

Humanizationは、事実であれば何でも公開文に整えるわけではありません。まず、その画面でユーザーに伝える役割があるかを判断します。

| 修正前 | 修正後 |
| :--- | :--- |
| 「この公開サイトには処理サービスがなく、ファイルのアップロードにも外部システムとの連携にも対応していません。タスクを開始する入口もありません。」 | **公開向けの代替文は追加しません。**<br><br>**文言の扱い:** `remove`<br>**プロダクト導線:** `needs_product_decision`。このページは閲覧専用ですか。それとも、ここから分析を始められるようにしますか。分析を提供するページなら、文言を用意する前に、実際に使える入口とCTAを実装します。 |

内部の事実は機能台帳に残します。元の文はユーザーの行動や判断に役立たないため削除します。入口がない問題は別のプロダクト判断として扱い、説明文で導線を代用しません。

## ルールの出典

Humanizationが成り立っているのは、他のプロジェクトが有用な執筆手法と言語別ガイダンスを公開してきたおかげです。以下のプロジェクトは、共通契約、ロケールプロファイル、編集フローの設計に貢献しています。

| プロジェクト | Humanizationへの貢献 |
| :--- | :--- |
| [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing/tree/cd879d22c8588125c1869d0b443f5d8df74b4192) | 資料の充足度、出典チェック、現実とフィクションの境界、推敲フロー、自然な中国語のリズムを含む、最初の`zh-CN`長文基盤を提供しました。 |
| [yetone/kill-ai-slop](https://github.com/yetone/kill-ai-slop/tree/96d1ca568a1db7e1ef9a381644c744440f816ee4) | 具体的な情報を中心に据え、書き直す前に装飾を取り除き、パターン一致を次のレビューへつなげるテキストレビューの実践に影響を与えました。 |
| [ehmo/slopkit (`slopbeth`)](https://github.com/ehmo/slopkit/blob/b33718bb9283c11b09567dc714f92d90ffb7bd16/skills/slopbeth/SKILL.md) | エンティティ、数値、日付、URL、引用、不確実性を扱い、すべての主張を手元の証拠の範囲に収める証拠台帳の設計に影響を与えました。 |
| [blader/humanizer](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md)と[petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop/blob/d30eddb9e04562234f2070b5ee63ca4649d9a05e/skills/no-ai-slop/SKILL.md) | 書き手の事実と自然な文体を保ち、有用な最小限の修正を加え、`no_change`を認める編集フローに影響を与えました。 |
| [18F/content-guide](https://github.com/18F/content-guide/tree/1b1723d3d5b8f91d92c16487c88b56265dc0ec3a)と[GOV.UK Design System](https://github.com/alphagov/govuk-design-system/tree/efb0d77d38b7ed7f921697564d2c47723d434977) | ユーザーニーズに基づく掲載判定、前向きで実行可能な手順、適切なメッセージ配置、エラーや利用不可状態で実際の次の手順を示す要件に影響を与えました。 |
| [Shopify Polaris](https://github.com/Shopify/polaris-react-archive/blob/af6ffb66a5b1d20f6c2c898b334a1ebb53728ba2/polaris.shopify.com/content/content/fundamentals.mdx)、[Carbon Design System](https://github.com/carbon-design-system/carbon-website/tree/e14433309b1dd53ec790eaa176139007ea9e9c80)、[PatternFly](https://github.com/patternfly/patternfly-org/tree/3aff87cace31c7d7e94ebae4cb35666f4f2e75d7) | コンポーネント単位のコンテンツ選択に影響を与えました。タスクに必要な支援を残し、インターフェースの状態を区別し、制約を確認可能な結果と実装済みの操作へ結び付けます。 |
| [ya8282/ux-writing-skill](https://github.com/ya8282/ux-writing-skill/tree/711e4162d21367bc62003e428696dc76807d56ec)、[OOOOuyang/UX-writing-skill](https://github.com/OOOOuyang/UX-writing-skill/tree/fad02668533dca76d638aaacf6c2e834657df0ab)、[RobTar97/japanese-writing-skills](https://github.com/RobTar97/japanese-writing-skills/tree/e4b1700464219c60da786f005a061bccffbbd4e3) | コンテンツの扱いを明示し、すべての補助文に役割を持たせ、ユーザー向けの復旧案内と開発者向け診断情報を分ける設計に影響を与えました。 |

## ロケールプロファイル

各ロケールプロファイルは、その言語に固有の構文、文体、句読点、用語、翻訳調の見直し方、リズムを定めています。

| ロケール | 参照したプロジェクトとガイド | これらの情報源から得た原則 |
| :--- | :--- | :--- |
| `zh-CN` | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing/tree/cd879d22c8588125c1869d0b443f5d8df74b4192)、[GB/T 15834-2011](https://openstd.samr.gov.cn/) | 中国大陸で自然な構文と用語、全角句読点、資料を軸にした長文、専用の`zh-CN prose`ハウススタイル。 |
| `zh-TW` | [Mozilla zh-TW style guide](https://github.com/mozilla-l10n/styleguides/blob/main/docs/zh-TW/README.md)、[bruce6731/anti-ai-writing-taiwan](https://github.com/bruce6731/anti-ai-writing-taiwan/tree/2c14f6a6015885b0c1cad9b54c861bc7b8a3b27d) | 台湾で自然な用語、文体、句読点、文化に沿った情報の並べ方。 |
| `en` | [Google styleguide](https://github.com/google/styleguide/tree/gh-pages/docguide)、[Microsoft Writing Style Guide](https://github.com/MicrosoftDocs/microsoft-style-guide)、[Digital.gov Plain Language](https://digital.gov/guides/plain-language/) | 明確な主体と動作の関係、簡潔なドキュメント、文脈に合うブランドボイス、地域内の一貫性、英語本来の句読点。 |
| `ja` | [Mozilla Japanese style guide](https://github.com/mozilla-l10n/styleguides/blob/main/docs/ja/l10nguideline.md)、[chezou/slop-nuki](https://github.com/chezou/slop-nuki/tree/1bdf627b5991f4f806069619c9bde407960feac7)、[iKora128/stop-ai-slop-jp](https://github.com/iKora128/stop-ai-slop-jp/tree/e09d32796f253a62693885757cea484c275d06f2)、[RobTar97/japanese-writing-skills](https://github.com/RobTar97/japanese-writing-skills/tree/e4b1700464219c60da786f005a061bccffbbd4e3)、[coji/natural-japanese](https://github.com/coji/natural-japanese/tree/b54954f8deb4f110f0959f4e4fac295708900120) | 自然な省略と語順、助詞、文脈に応じた敬語とクッション表現、コンポーネントごとの名詞形・動詞形、GUIリソースの完全性、密度とジャンルに応じたレビュー。 |
| `ko` | [Mozilla Korean style guide](https://github.com/mozilla-l10n/styleguides/blob/main/docs/ko/README.md)、[dotoricode/korean-humanizer](https://github.com/dotoricode/korean-humanizer/tree/7dff5b48cc06fc4252d4766b802ecd61e62c50ad)、[HarryJhin/korean-writing](https://github.com/HarryJhin/korean-writing/tree/e4db3883ed76521b7a0cac30392fa67d182cc8ab) | 自然な主語の省略、助詞と分かち書き、`합니다`/`해요`/`다`の文体レベル、敬語の保持、文末表現、英語・日本語由来の翻訳調の見直し。 |
| `es` | [Mozilla Spanish style guides](https://github.com/mozilla-l10n/styleguides/tree/main/docs/es) | 性数一致、接語、`tú`/`usted`/`ustedes`、sentence caseのUI、地域用語、句読点、英語の直訳表現。 |

リンク先のプロジェクトには、それぞれ固有のライセンスが適用されます。[多言語調査ノート](./research/multilingual-skill-research.md)と[GUIコピー掲載判定レポート](./research/gui-copy-existence-gate.md)には、出典となる根拠と、各情報源がHumanizationにどう生かされているかを記録しています。文章やコードを再利用する前に、各リポジトリのライセンスを確認してください。Humanizationのプロジェクト固有の指示は、上記の実践をもとに新しく書かれています。

## インストール

GitHubからSkillをインストールできるエージェントに、次のように依頼します。

```text
https://github.com/thevenomsnake/humanization から humanization Skill をインストールしてください。Skill は humanization/ ディレクトリにあります。
```

インストール先のディレクトリ名は`humanization`のままにしてください。正しいカードの名前は`Humanization`で、6本の言語バーが付いた濃緑色のHアイコンを使用し、「Natural writing and GUI copy across six locales.」と表示されます。`活人感写作`というカードは従来の`human-writing` Skillに属し、上記のメタデータがHumanizationを識別します。

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

既存の文言を直す前に、現在の表示面に置くべきかを監査できます。

```text
locale=zh-CN、format=web-microcopy、surface=public-page を指定して $humanization を使用してください。各機能説明を `keep`、`rewrite`、`move`、`remove` のどれにするかを判断し、根本に製品判断が必要な点も示してください。
```

公開フォーマット名`web-microcopy`は、Web、デスクトップ、モバイル製品のHTML、JSON、YAML、ARB、PO、ソースコード、デザインファイルに含まれるGUIテキストを対象とします。

同じ明示的なルーティングで自動チェッカーを実行します。

```bash
python humanization/scripts/check_writing.py --locale en --format copy draft.md
python humanization/scripts/check_writing.py --locale es --format web-microcopy --source source.json target.json
```

## 3.0.0での変更点

- 安定したSkill名およびディレクトリ名を`humanization`、UI表示名を`Humanization`に確定しました。
- ランタイムガイダンスを、1つの共通契約、6つのロケールプロファイル、1つのGUIマイクロコピーモジュールに分割しました。
- `kill-ai-slop`を参考に、具体的な情報、抑制の利いた表現、パターン一致をレビューの手掛かりとして扱う原則を追加しました。
- 内部の機能情報と公開可能なユーザーメッセージを分ける、言語横断のコンテンツ掲載ゲートを追加しました。
- `--locale`と`--format`を明示し、混在テキストのルーティングを呼び出し側で選び、トーンの判断をwarningとしてレビューできるようにしました。

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
| [`core.md`](./humanization/references/core.md) | 事実、出典、機能、プライバシー、CTA、ブランド用語、プレースホルダー、最小限の編集、コンテンツの扱いを管理します。 |
| [`locales/`](./humanization/references/locales) | 各言語向けの6つの執筆プロファイルを収録します。 |
| [`expressive-text.md`](./humanization/references/formats/expressive-text.md) | GUI以外の製品、ドキュメント、マーケティング、メール、ソーシャルコピーを扱います。 |
| [`gui-microcopy.md`](./humanization/references/formats/gui-microcopy.md) | GUIコンテンツゲート、コンポーネントの役割、構造化リソースの保護を定義します。 |
| [`check_writing.py`](./humanization/scripts/check_writing.py) | 共通、ロケール、GUIチェック用の単一CLIを提供します。 |
| [`check_zh_cn.py`](./humanization/scripts/check_zh_cn.py) | 従来のアクションレベルのチェッカーを`zh-CN prose`に限定します。 |

</details>

## クレジットとフィードバック

HumanizationはMIT Licenseで公開されています。最初の`zh-CN`長文基盤は、同じくMIT Licenseで公開されている[KKKKhazix/human-writing v1.1.0](https://github.com/KKKKhazix/human-writing/tree/cd879d22c8588125c1869d0b443f5d8df74b4192)に由来します。上記の出典一覧では、現在のアーキテクチャに影響を与えたプロジェクトとガイドにクレジットを記し、それぞれの貢献を説明しています。

ルールの衝突、誤検出、モデル固有の不具合については、プロンプト、該当する出力、期待した結果を添えて[issueを作成してください](https://github.com/thevenomsnake/humanization/issues)。

<p align="center">
  <sub>Humanization · 3.0.0</sub>
</p>
