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
  <a href="#修改前與修改後">前後對照</a> ·
  <a href="#規則來源">規則來源</a> ·
  <a href="#語言檔案">語言檔案</a> ·
  <a href="#儲存庫結構">儲存庫結構</a> ·
  <a href="https://github.com/thevenomsnake/humanization/issues">問題回報</a>
</p>

<p align="center"><strong>先判斷這段文字是否該出現，再用六種 locale 寫得自然。</strong></p>

Humanization 整合多個成熟寫作、編輯、在地化、內容設計與 anti-slop 專案的實務，服務多語言產品創作者。使用情境涵蓋文章、故事、文件、產品內容、行銷文案、電子郵件和社群貼文，也包括導覽、按鈕、錯誤、空白狀態、確認、通知、隱私權說明和無障礙名稱等 GUI 文字。開始改寫前，它會先分清內部能力事實，以及使用者在目前呈現位置真正需要看到的訊息。

**語言檔案：** [zh-CN 简体中文](./humanization/references/locales/zh-CN.md) · [zh-TW 繁體中文](./humanization/references/locales/zh-TW.md) · [en English](./humanization/references/locales/en.md) · [ja 日本語](./humanization/references/locales/ja.md) · [ko 한국어](./humanization/references/locales/ko.md) · [es Español](./humanization/references/locales/es.md)

## 運作方式

每項任務由三個職責清楚的模組共同處理。

- **通用契約：** 事實、來源、能力、隱私權、CTA、品牌詞、placeholder、最小幅度修改和內容存在性門。
- **語言檔案：** 分別定義該語言的語序、語體或敬語、標點、術語、翻譯腔審查和自然節奏。
- **GUI 微文案：** 依按鈕、錯誤、空白狀態、確認和通知等元件分別處理文字，並保護 key、ICU 訊息、變數、markup 和執行階段結構。

通用契約先將每一則候選訊息標為 `keep`、`rewrite`、`move` 或 `remove`。如果候選訊息也暴露出缺少動作、狀態或復原路徑，再為底層流程同時標記 `needs_product_decision`。內部事實用來約束產品主張，只有確實協助使用者完成任務的訊息才會成為公開文案。語言檔案接著決定這些訊息在目標語言中如何自然表達。不同版本可以採用各自的句型和長度，同時保留相同的受眾、動作、能力邊界、隱私權承諾和核准術語。

原始資料有缺口時，Skill 會提出一個明確問題、查核來源或縮小主張。頁面缺少可用的 CTA 或復原路徑時，Skill 會回傳 `needs_product_decision`，由產品團隊決定如何補齊流程。確定性檢查會攔下可證實的損壞；訊息是否相關、語氣是否合適、文字是否自然，都要依情境審閱。

## 修改前與修改後

Humanization 不會把每一句真實資訊潤飾後直接公開。它會先判斷這段文字在目前頁面負責什麼，再決定改寫、移動或不提供公開文案。

| 修改前 | 修改後 |
| :--- | :--- |
| **內部能力盤點**<br><br>「這個公開網站沒有處理服務，不提供檔案上傳，不連接求職網站，也沒有開始任務的入口。」 | **不補任何公開文案。**<br><br>**文案處置：** `remove`<br>**產品流程：** `needs_product_decision`。這個頁面只提供閱讀資訊，還是應該讓訪客在這裡開始任務？如果分析功能屬於這個頁面，請先實作可用的入口與 CTA，再撰寫文案。 |
| **已確認的能力被套話蓋過**<br><br>「面對快速變動的招募環境，我們以創新的 AI 洞察協助團隊，讓每份文件都能依同一套職缺條件比較。」 | **依同一套職缺條件比較每份文件。**<br><br>**文案處置：** `rewrite` |
| **確實支援重試的錯誤**<br><br>「錯誤 500：worker 逾時，POST /profile 請求失敗。」 | **無法儲存變更，請再試一次。**<br><br>**公開訊息：** `rewrite`<br>**開發診斷：** `move` 到紀錄 |
| **含變數的通知**<br><br>「檔案 {fileName} 已被成功上傳。」 | **{fileName} 已上傳。**<br><br>**文案處置：** `rewrite`<br>**受保護變數：** `{fileName}` |

這些例子不會虛構功能或復原路徑。沒有使用者職責的文字直接移除，已確認的內容繼續保留，開發診斷移到合適位置，執行階段變數維持原樣。

## 規則來源

Humanization 的形成，仰賴其他專案公開實用的寫作方法和語言專屬指南。以下專案共同塑造了它的通用契約、語言檔案和編輯流程。

| 專案 | 對 Humanization 的貢獻 |
| :--- | :--- |
| [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing/tree/cd879d22c8588125c1869d0b443f5d8df74b4192) | 奠定最初的 `zh-CN` 長文基礎，包括材料是否充足、來源查核、現實與虛構邊界、修改流程和自然中文節奏。 |
| [yetone/kill-ai-slop](https://github.com/yetone/kill-ai-slop/tree/96d1ca568a1db7e1ef9a381644c744440f816ee4) | 啟發文字審閱流程，以具體資訊取代口號，先清理裝飾再改寫，並把模式命中視為進一步審閱的線索。 |
| [ehmo/slopkit (`slopbeth`)](https://github.com/ehmo/slopkit/blob/b33718bb9283c11b09567dc714f92d90ffb7bd16/skills/slopbeth/SKILL.md) | 啟發證據帳本的設計，用來記錄實體、數字、日期、URL、引文和不確定性，讓每項主張都能對應現有證據。 |
| [blader/humanizer](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md) 和 [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop/blob/d30eddb9e04562234f2070b5ee63ca4649d9a05e/skills/no-ai-slop/SKILL.md) | 啟發最小編輯流程，保留作者的事實和有效語氣，只做足以解決問題的修改，並允許 `no_change`。 |
| [18F/content-guide](https://github.com/18F/content-guide/tree/1b1723d3d5b8f91d92c16487c88b56265dc0ec3a) 和 [GOV.UK Design System](https://github.com/alphagov/govuk-design-system/tree/efb0d77d38b7ed7f921697564d2c47723d434977) | 啟發以使用者需求為準的內容取捨、正向任務指示和訊息放置原則，並要求錯誤與無法使用的狀態為使用者提供實際的下一步。 |
| [Shopify Polaris](https://github.com/Shopify/polaris-react-archive/blob/af6ffb66a5b1d20f6c2c898b334a1ebb53728ba2/polaris.shopify.com/content/content/fundamentals.mdx)、[Carbon Design System](https://github.com/carbon-design-system/carbon-website/tree/e14433309b1dd53ec790eaa176139007ea9e9c80) 和 [PatternFly](https://github.com/patternfly/patternfly-org/tree/3aff87cace31c7d7e94ebae4cb35666f4f2e75d7) | 啟發元件層級的內容取捨，保留與任務相關的協助、區分介面狀態，並將限制連結到使用者可觀察的後果與產品支援的動作。 |
| [ya8282/ux-writing-skill](https://github.com/ya8282/ux-writing-skill/tree/711e4162d21367bc62003e428696dc76807d56ec)、[OOOOuyang/UX-writing-skill](https://github.com/OOOOuyang/UX-writing-skill/tree/fad02668533dca76d638aaacf6c2e834657df0ab) 和 [RobTar97/japanese-writing-skills](https://github.com/RobTar97/japanese-writing-skills/tree/e4b1700464219c60da786f005a061bccffbbd4e3) | 啟發明確的內容處置，讓每一段輔助文字都有清楚職責，並將面向使用者的復原文案與開發診斷分開。 |

## 語言檔案

每個語言檔案分別定義該語言的語序、語體、標點、術語、翻譯腔審查和節奏。

| Locale | 參考專案與指南 | 由這些來源啟發的語言原則 |
| :--- | :--- | :--- |
| `zh-CN` | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing/tree/cd879d22c8588125c1869d0b443f5d8df74b4192) 和 [GB/T 15834-2011](https://openstd.samr.gov.cn/) | 中國大陸中文語序和術語、全形標點、由材料推進的長文寫作，以及專屬的 `zh-CN prose` house style。 |
| `zh-TW` | [Mozilla zh-TW style guide](https://github.com/mozilla-l10n/styleguides/blob/main/docs/zh-TW/README.md) 和 [bruce6731/anti-ai-writing-taiwan](https://github.com/bruce6731/anti-ai-writing-taiwan/tree/2c14f6a6015885b0c1cad9b54c861bc7b8a3b27d) | 針對 `zh-TW` locale 的原生在地化，涵蓋台灣常用的繁體中文術語、語體、標點和符合文化脈絡的語序。 |
| `en` | [Google styleguide](https://github.com/google/styleguide/tree/gh-pages/docguide)、[Microsoft Writing Style Guide](https://github.com/MicrosoftDocs/microsoft-style-guide) 和 [Digital.gov Plain Language](https://digital.gov/guides/plain-language/) | 清楚的行動者與動作關係、簡潔文件、依情境調整的品牌語氣、地區一致性和英語標點。 |
| `ja` | [Mozilla Japanese style guide](https://github.com/mozilla-l10n/styleguides/blob/main/docs/ja/l10nguideline.md)、[chezou/slop-nuki](https://github.com/chezou/slop-nuki/tree/1bdf627b5991f4f806069619c9bde407960feac7)、[iKora128/stop-ai-slop-jp](https://github.com/iKora128/stop-ai-slop-jp/tree/e09d32796f253a62693885757cea484c275d06f2)、[RobTar97/japanese-writing-skills](https://github.com/RobTar97/japanese-writing-skills/tree/e4b1700464219c60da786f005a061bccffbbd4e3) 和 [coji/natural-japanese](https://github.com/coji/natural-japanese/tree/b54954f8deb4f110f0959f4e4fac295708900120) | 自然省略和語序、助詞、依情境使用的敬語與緩衝表達、依元件選擇名詞或動詞形式、GUI 資源完整性，以及依密度和文體調整的審閱方式。 |
| `ko` | [Mozilla Korean style guide](https://github.com/mozilla-l10n/styleguides/blob/main/docs/ko/README.md)、[dotoricode/korean-humanizer](https://github.com/dotoricode/korean-humanizer/tree/7dff5b48cc06fc4252d4766b802ecd61e62c50ad) 和 [HarryJhin/korean-writing](https://github.com/HarryJhin/korean-writing/tree/e4db3883ed76521b7a0cac30392fa67d182cc8ab) | 自然省略主詞、助詞和分寫、`합니다`/`해요`/`다` 語體層級、敬語、句尾形式，以及英語和日語翻譯腔審查。 |
| `es` | [Mozilla Spanish style guides](https://github.com/mozilla-l10n/styleguides/tree/main/docs/es) | 性數一致、附著代名詞、`tú`/`usted`/`ustedes`、句首大寫式 UI、地區術語、標點和英語仿譯審查。 |

連結的專案分別適用各自的授權條款。[多語言研究筆記](./research/multilingual-skill-research.md) 和 [GUI 文案存在性門研究報告](./research/gui-copy-existence-gate.md) 記錄了來源證據，以及這些來源如何影響 Humanization；使用相關文字或程式碼前，請先查閱相應儲存庫的授權條款。Humanization 的專案規則依據上述實務重新撰寫。

## 安裝

請讓支援從 GitHub 安裝 Skill 的 Agent 執行：

```text
Install the humanization Skill from https://github.com/thevenomsnake/humanization. The Skill is in the humanization/ directory.
```

安裝後的目錄名稱必須維持為 `humanization`。正確的卡片名稱是 `Humanization`，使用帶有六條語言色帶的深綠色 H 圖示，說明文字為 “Natural writing and GUI copy across six locales.”。Codex 顯示 `活人感写作` 時，目前的卡片對應舊版 `human-writing` Skill；Humanization 可依照上述名稱、圖示和說明文字辨識。

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

改寫之前，先檢查現有文案是否適合留在目前的呈現位置：

```text
Use $humanization with locale=zh-CN, format=web-microcopy, and surface=public-page. Decide whether each capability statement should be kept, rewritten, moved, or removed, and flag any underlying product decision.
```

公開 format 名稱 `web-microcopy` 涵蓋 HTML、JSON、YAML、ARB、PO、原始碼和設計檔案中的 GUI 文字，適用於網站、桌面和行動產品。

執行確定性檢查器時使用相同的明確路由：

```bash
python humanization/scripts/check_writing.py --locale en --format copy draft.md
python humanization/scripts/check_writing.py --locale es --format web-microcopy --source source.json target.json
```

## 3.0.0 的變更

- 將 `humanization` 定為穩定的 Skill 名稱和目錄名稱，UI 顯示名稱為 `Humanization`。
- 將執行階段指南拆成一份通用契約、六個語言檔案和一個 GUI 微文案模組。
- 加入由 `kill-ai-slop` 啟發的具體資訊、克制表達和審閱線索原則。
- 新增跨語言內容存在性門，用來區分內部能力事實與適合公開的使用者訊息。
- `--locale` 和 `--format` 改為明確參數，由使用者為混合文字指定路由，語氣繼續作為人工審閱項目。

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
| [`core.md`](./humanization/references/core.md) | 負責事實、來源、能力、隱私權、CTA、品牌詞、placeholder、最小幅度修改和內容處置。 |
| [`locales/`](./humanization/references/locales) | 保存六個語言的原生寫作檔案。 |
| [`expressive-text.md`](./humanization/references/formats/expressive-text.md) | 處理非 GUI 的產品、文件、行銷、電子郵件和社群文字。 |
| [`gui-microcopy.md`](./humanization/references/formats/gui-microcopy.md) | 定義 GUI 內容存在性門、元件職責和結構化資源保護。 |
| [`check_writing.py`](./humanization/scripts/check_writing.py) | 提供執行通用、語言和 GUI 檢查的單一 CLI。 |
| [`check_zh_cn.py`](./humanization/scripts/check_zh_cn.py) | 將原有的動作層級檢查器限定在 `zh-CN prose`。 |

</details>

## 來源聲明與意見回饋

Humanization 依 MIT License 發布。最初的 `zh-CN` 長文基礎來自同樣採用 MIT License 的 [KKKKhazix/human-writing v1.1.0](https://github.com/KKKKhazix/human-writing/tree/cd879d22c8588125c1869d0b443f5d8df74b4192)。上方的來源表向影響目前架構的專案和指南致謝，並說明它們的具體貢獻。

若遇到規則衝突、誤判或特定模型上的問題，請[建立 issue](https://github.com/thevenomsnake/humanization/issues)，並附上提示詞、相關輸出和你預期的結果。

<p align="center">
  <sub>Humanization · 3.0.0</sub>
</p>
