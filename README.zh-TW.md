<p align="center">
  <img src="./assets/readme-cover.svg" alt="Humanization" width="100%">
</p>

<p align="center">
  <a href="./README.md">English</a> ·
  <a href="./README.zh-CN.md">简体中文</a> ·
  <strong>繁體中文</strong> ·
  <a href="./README.ja.md">日本語</a> ·
  <a href="./README.ko.md">한국어</a> ·
  <a href="./README.es.md">Español</a>
</p>

<p align="center">
  <strong>v3.0.0</strong> · MIT · 6 locales · prose / copy / GUI microcopy
</p>

<p align="center">
  <a href="#安裝">安裝</a> ·
  <a href="#運作方式">運作方式</a> ·
  <a href="#規則來源">規則來源</a> ·
  <a href="#語言檔案">語言檔案</a> ·
  <a href="#儲存庫結構">儲存庫結構</a> ·
  <a href="https://github.com/thevenomsnake/humanization/issues">問題回報</a>
</p>

<p align="center"><strong>以六種 locale 撰寫與修改文字，不把某種語言的規則帶進另一種語言。</strong></p>

Humanization 是獨立維護的 Codex Skill，適用於文章、故事、文件、產品內容、行銷文案、電子郵件和社群貼文。它也能處理導覽、按鈕、錯誤、空白狀態、確認、通知、隱私權說明和無障礙名稱等 GUI 文字。

**語言檔案：** [zh-CN 简体中文](./humanization/references/locales/zh-CN.md) · [zh-TW 繁體中文](./humanization/references/locales/zh-TW.md) · [en English](./humanization/references/locales/en.md) · [ja 日本語](./humanization/references/locales/ja.md) · [ko 한국어](./humanization/references/locales/ko.md) · [es Español](./humanization/references/locales/es.md)

## 運作方式

每項任務都會載入三個模組，每個模組只負責一類問題。

- **通用契約：** 事實、來源、能力、隱私權、CTA、品牌詞、placeholder 和最小幅度修改。
- **語言檔案：** 語序、語體或敬語、標點、地區用詞、翻譯腔和自然節奏。
- **GUI 微文案：** 依按鈕、錯誤、空白狀態、確認和通知等元件分別處理文字，並保護 key、ICU 訊息、變數、markup 和執行階段結構。

通用契約確保不同語言中的事實主張和產品承諾保持一致。語言檔案決定這些限制在當地語言中如何自然表達。譯文可以使用不同的句型和長度，但必須保留相同的受眾、動作、能力邊界、隱私權承諾和核准術語。

來源材料不完整時，Skill 會提出一個聚焦問題、查核來源或縮小主張。原文已經合用時，它會維持原文。確定性檢查只會阻擋可以證明的損壞；語氣和自然度仍由所選的語言檔案負責審閱。

## 規則來源

Humanization 借鑑其他專案的編輯機制，再依照本專案的架構重新表述。它不會複製這些專案的內文、範例、指令碼或詞表。

| 專案 | Humanization 採用的內容 | 未採用的內容 |
| :--- | :--- | :--- |
| [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing/tree/cd879d22c8588125c1869d0b443f5d8df74b4192) | `zh-CN` 長文基礎，包括材料是否充足、來源查核、現實與虛構邊界、修改流程和自然中文節奏。 | 中文標點和對比句型的 house rules 只保留在 `zh-CN prose`，不會成為全域規則。 |
| [yetone/kill-ai-slop](https://github.com/yetone/kill-ai-slop) | 只採用文字原則，包括以具體資訊取代口號、先移除裝飾再改寫，以及把模式命中視為審閱線索而不是結論。 | 顏色、字體、卡片、圓角、圖示、動態效果、按鈕樣式和視覺掃描器。 |
| [ehmo/slopkit (`slopbeth`)](https://github.com/ehmo/slopkit/blob/b33718bb9283c11b09567dc714f92d90ffb7bd16/skills/slopbeth/SKILL.md) | 為實體、數字、日期、URL、引文和不確定性建立證據約束帳本；缺少證據時不得以虛構主張填補。 | 英文禁用詞、長破折號規則、專案自報分數和規避偵測器的承諾。 |
| [blader/humanizer](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md) 和 [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop/blob/d30eddb9e04562234f2070b5ee63ca4649d9a05e/skills/no-ai-slop/SKILL.md) | 保留作者的事實和有效語氣，優先採用最小有效修改，允許 `no_change`，也不根據模式清單推斷作者是否使用 AI。 | 通用語氣公式和自動判斷作者身分。 |

## 語言檔案

這些檔案是各語言的原生寫作契約，不是中文規則的翻譯版。

| Locale | 採用的原生專案和指南 | 採用的語言專屬原則 |
| :--- | :--- | :--- |
| `zh-CN` | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing/tree/cd879d22c8588125c1869d0b443f5d8df74b4192) 和 [GB/T 15834-2011](https://openstd.samr.gov.cn/) | 中國大陸中文語序和術語、全形標點、由材料推進的長文寫作，以及僅限 `zh-CN prose` 的中文 house rules。 |
| `zh-TW` | [Mozilla zh-TW style guide](https://github.com/mozilla-l10n/styleguides/blob/main/docs/zh-TW/README.md) 和 [bruce6731/anti-ai-writing-taiwan](https://github.com/bruce6731/anti-ai-writing-taiwan/tree/2c14f6a6015885b0c1cad9b54c861bc7b8a3b27d) | 採用台灣常用詞、語體、標點和文化脈絡下的重組方式，並明確規定 `zh-TW` 不是簡體轉繁體。未引入 Mozilla 的產品專屬術語。 |
| `en` | [Google styleguide](https://github.com/google/styleguide/tree/gh-pages/docguide)、[Microsoft Writing Style Guide](https://github.com/MicrosoftDocs/microsoft-style-guide) 和 [Digital.gov Plain Language](https://digital.gov/guides/plain-language/) | 清楚的行動者與動作關係、簡潔文件、依情境調整的品牌語氣、地區一致性，以及英語標點的一般用法。未引入 Microsoft 專屬術語。 |
| `ja` | [Mozilla Japanese style guide](https://github.com/mozilla-l10n/styleguides/blob/main/docs/ja/l10nguideline.md)、[chezou/slop-nuki](https://github.com/chezou/slop-nuki/tree/1bdf627b5991f4f806069619c9bde407960feac7)、[iKora128/stop-ai-slop-jp](https://github.com/iKora128/stop-ai-slop-jp/tree/e09d32796f253a62693885757cea484c275d06f2)、[RobTar97/japanese-writing-skills](https://github.com/RobTar97/japanese-writing-skills/tree/e4b1700464219c60da786f005a061bccffbbd4e3) 和 [coji/natural-japanese](https://github.com/coji/natural-japanese/tree/b54954f8deb4f110f0959f4e4fac295708900120) | 自然省略和語序、助詞、依情境使用的敬語與緩衝表達、依元件選擇名詞或動詞形式、GUI 資源完整性，以及依密度與文體審閱，而不是絕對禁止某種模式。 |
| `ko` | [Mozilla Korean style guide](https://github.com/mozilla-l10n/styleguides/blob/main/docs/ko/README.md)、[dotoricode/korean-humanizer](https://github.com/dotoricode/korean-humanizer/tree/7dff5b48cc06fc4252d4766b802ecd61e62c50ad) 和 [HarryJhin/korean-writing](https://github.com/HarryJhin/korean-writing/tree/e4db3883ed76521b7a0cac30392fa67d182cc8ab) | 自然省略主詞、助詞和分寫、`합니다`/`해요`/`다` 語體層級、保留敬語、句尾形式，以及英語和日語翻譯腔。未採用任意修改配額。 |
| `es` | [Mozilla Spanish style guides](https://github.com/mozilla-l10n/styleguides/tree/main/docs/es) | 性數一致、附著代名詞、`tú`/`usted`/`ustedes`、句首大寫式 UI、地區術語、標點和英語仿譯。未引入 Firefox 專屬標籤，也沒有規定一種通用於所有西語的語體。 |

連結的專案仍分別適用各自的授權條款。[研究筆記](./research/multilingual-skill-research.md) 記錄了來源證據和採用邊界；重複使用這些專案的文字或程式碼前，請先查閱相應儲存庫的授權條款。Humanization 中的規則是重新撰寫的上述機制摘要。

## 安裝

請讓支援從 GitHub 安裝 Skill 的 Agent 執行：

```text
Install the humanization Skill from https://github.com/thevenomsnake/humanization. The Skill is in the humanization/ directory.
```

安裝後的目錄名稱必須維持為 `humanization`。正確的卡片名稱是 `Humanization`，使用帶有六條語言色帶的深綠色 H 圖示，說明文字為 “Natural writing and GUI copy across six locales.”。如果 Codex 顯示 `活人感写作`，它展示的是舊版 `human-writing` Skill，而不是 Humanization。

<details>
<summary><strong>手動安裝</strong></summary>

將儲存庫中的 [`humanization`](./humanization) 目錄複製到 Codex Skills 目錄：

```text
$CODEX_HOME/skills/humanization/
```

</details>

使用時請明確指定 locale、format 和 surface：

```text
Use $humanization with locale=ja, format=web-microcopy, and surface=error. Rewrite these error messages while preserving the CTA, brand terms, placeholders, and source resource structure.
```

公開 format 名稱 `web-microcopy` 涵蓋 HTML、JSON、YAML、ARB、PO、原始碼和設計檔案中的 GUI 文字，不僅限於網站。

執行確定性檢查器時使用相同的明確路由：

```bash
python humanization/scripts/check_writing.py --locale en --format copy draft.md
python humanization/scripts/check_writing.py --locale es --format web-microcopy --source source.json target.json
```

## 3.0.0 的變更

- 將 `humanization` 定為穩定的 Skill 名稱和目錄名稱，UI 顯示名稱為 `Humanization`。
- 將執行階段指南拆成一份通用契約、六個語言檔案和一個 GUI 微文案模組。
- 只採用 `kill-ai-slop` 的文字原則；顏色、卡片、圓角、圖示和動態效果等視覺規則不在範圍內。
- `--locale` 和 `--format` 改為明確參數。檢查器不會猜測混合文字的語言，也不會把語氣判斷變成硬失敗。

完整歷史記錄請見 [CHANGELOG.md](./CHANGELOG.md)。

## 儲存庫結構

<details>
<summary><strong>展開完整目錄</strong></summary>

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

| 路徑 | 用途 |
| :--- | :--- |
| [`SKILL.md`](./humanization/SKILL.md) | 讓每項任務依序經過通用、語言和格式模組。 |
| [`core.md`](./humanization/references/core.md) | 負責事實、來源、能力、隱私權、CTA、品牌詞、placeholder 和最小幅度修改。 |
| [`locales/`](./humanization/references/locales) | 保存六個語言的原生寫作檔案。 |
| [`expressive-text.md`](./humanization/references/formats/expressive-text.md) | 處理非 GUI 的產品、文件、行銷、電子郵件和社群文字。 |
| [`gui-microcopy.md`](./humanization/references/formats/gui-microcopy.md) | 定義 GUI 元件職責和結構化資源保護。 |
| [`check_writing.py`](./humanization/scripts/check_writing.py) | 提供執行通用、語言和 GUI 檢查的單一 CLI。 |
| [`check_zh_cn.py`](./humanization/scripts/check_zh_cn.py) | 將原有的動作層級檢查器限定在 `zh-CN prose`。 |

</details>

## 來源聲明與意見回饋

Humanization 依 MIT License 發布。儲存庫不包含第三方文章、訓練語料或模型權重。

Humanization 是獨立專案。它最初的 `zh-CN` 長文基礎依 MIT License 衍生自 [KKKKhazix/human-writing v1.1.0](https://github.com/KKKKhazix/human-writing/tree/cd879d22c8588125c1869d0b443f5d8df74b4192)。上方的來源對照表記錄了所有影響目前架構的專案或指南、從中採用的原則，以及明確排除的專案專屬規則。

若遇到規則衝突、誤判或特定模型上的問題，請[建立 issue](https://github.com/thevenomsnake/humanization/issues)，並附上提示詞、相關輸出和你預期的結果。

<p align="center">
  <sub>Humanization · 3.0.0</sub>
</p>
