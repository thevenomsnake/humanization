<p align="center">
  <img src="./assets/readme-cover.svg" alt="Humanization" width="100%">
</p>

<p align="center">
  <a href="./README.md">English</a> ·
  <a href="./README.zh-CN.md">简体中文</a> ·
  <a href="./README.zh-TW.md">繁體中文</a> ·
  <a href="./README.ja.md">日本語</a> ·
  <strong>한국어</strong> ·
  <a href="./README.es.md">Español</a>
</p>

<p align="center">
  <strong>v3.0.0</strong> · MIT · 6개 로캘 · prose / copy / GUI microcopy
</p>

<p align="center">
  <a href="#설치">설치</a> ·
  <a href="#작동-방식">작동 방식</a> ·
  <a href="#규칙의-출처">출처</a> ·
  <a href="#로캘-프로필">로캘 프로필</a> ·
  <a href="#저장소-구조">저장소 구조</a> ·
  <a href="https://github.com/thevenomsnake/humanization/issues">Issues</a>
</p>

<p align="center"><strong>여섯 로캘에서 자연스럽게 읽히는 제품 문구와 GUI 카피.</strong></p>

Humanization은 글쓰기, 편집, 현지화, anti-slop 분야에서 꾸준히 발전해 온 여러 프로젝트의 실무 방식을 한데 모은 Codex Skill입니다. 다국어 제품을 만드는 사람을 위해 산문, 이야기, 문서, 제품 콘텐츠, 마케팅 카피, 이메일, 소셜 게시물을 지원합니다. 내비게이션, 버튼, 오류, 빈 상태, 확인, 알림, 개인정보 안내, 접근 가능한 이름 같은 GUI 텍스트도 다룹니다.

**로캘 프로필:** [zh-CN 简体中文](./humanization/references/locales/zh-CN.md) · [zh-TW 繁體中文](./humanization/references/locales/zh-TW.md) · [en English](./humanization/references/locales/en.md) · [ja 日本語](./humanization/references/locales/ja.md) · [ko 한국어](./humanization/references/locales/ko.md) · [es Español](./humanization/references/locales/es.md)

## 작동 방식

모든 작업은 역할이 분명한 세 모듈을 불러옵니다.

- **공통 계약:** 사실, 출처, 기능, 개인정보, CTA, 브랜드 용어, 플레이스홀더, 최소 편집을 담당합니다.
- **로캘 프로필:** 구문, 문체 또는 높임말, 문장부호, 지역 어휘, 번역투, 자연스러운 리듬을 담당합니다.
- **GUI 마이크로카피:** 버튼, 오류, 빈 상태, 확인, 알림에 맞는 문구를 작성하고 key, ICU 메시지, 변수, markup, 런타임 구조를 보호합니다.

공통 계약은 사실에 관한 주장과 제품의 약속을 언어마다 일관되게 유지합니다. 로캘 프로필은 이 제약을 각 언어에서 자연스럽게 표현하는 방식을 정합니다. 번역문의 문장 구조와 길이는 달라도 대상 독자, 행동, 기능 범위, 개인정보 약속, 승인된 용어는 같아야 합니다.

원자료가 부족하면 Skill은 한 가지에 초점을 맞춰 질문하거나, 출처를 확인하거나, 주장의 범위를 좁힙니다. 원문이 이미 자연스러우면 그대로 둡니다. 자동 검사는 명확히 입증된 훼손을 실패로 처리합니다. 어조와 자연스러움은 선택한 로캘 프로필에 따라 사람이 검토합니다.

## 규칙의 출처

Humanization은 여러 프로젝트가 유용한 글쓰기 방법과 언어별 지침을 공개해 준 덕분에 만들어질 수 있었습니다. 아래 프로젝트는 공통 계약, 로캘 프로필, 편집 흐름을 설계하는 데 도움을 주었습니다.

| 프로젝트 | Humanization에 기여한 내용 |
| :--- | :--- |
| [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing/tree/cd879d22c8588125c1869d0b443f5d8df74b4192) | 자료의 충분성, 출처 확인, 현실과 허구의 경계, 수정 흐름, 자연스러운 중국어 리듬을 포함한 최초의 `zh-CN` 장문 기반을 제공했습니다. |
| [yetone/kill-ai-slop](https://github.com/yetone/kill-ai-slop) | 구체적인 정보를 중심에 두고, 다시 쓰기 전에 장식을 걷어 내며, 패턴 일치를 다음 검토로 이어 가는 텍스트 검토 방식에 영향을 주었습니다. |
| [ehmo/slopkit (`slopbeth`)](https://github.com/ehmo/slopkit/blob/b33718bb9283c11b09567dc714f92d90ffb7bd16/skills/slopbeth/SKILL.md) | 개체, 숫자, 날짜, URL, 인용, 불확실성을 관리하고 모든 주장을 현재 증거의 범위 안에 두는 증거 원장에 영향을 주었습니다. |
| [blader/humanizer](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md) 및 [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop/blob/d30eddb9e04562234f2070b5ee63ca4649d9a05e/skills/no-ai-slop/SKILL.md) | 작성자의 사실과 자연스러운 문체를 보존하고, 필요한 만큼만 다듬으며, `no_change`를 허용하는 최소 편집 흐름에 영향을 주었습니다. |

## 로캘 프로필

각 로캘 프로필은 해당 언어의 고유한 구문, 문체, 문장부호, 용어, 번역투 검토 방식, 리듬을 정의합니다.

| 로캘 | 참고한 현지 프로젝트와 지침 | 이들 출처에서 얻은 원칙 |
| :--- | :--- | :--- |
| `zh-CN` | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing/tree/cd879d22c8588125c1869d0b443f5d8df74b4192) 및 [GB/T 15834-2011](https://openstd.samr.gov.cn/) | 중국 대륙에서 자연스러운 구문과 용어, 전각 문장부호, 자료 중심의 장문 작성, 전용 `zh-CN prose` 문체. |
| `zh-TW` | [Mozilla zh-TW style guide](https://github.com/mozilla-l10n/styleguides/blob/main/docs/zh-TW/README.md) 및 [bruce6731/anti-ai-writing-taiwan](https://github.com/bruce6731/anti-ai-writing-taiwan/tree/2c14f6a6015885b0c1cad9b54c861bc7b8a3b27d) | 대만에서 자연스러운 용어, 문체, 문장부호, 문화에 맞는 정보 배열. |
| `en` | [Google styleguide](https://github.com/google/styleguide/tree/gh-pages/docguide), [Microsoft Writing Style Guide](https://github.com/MicrosoftDocs/microsoft-style-guide) 및 [Digital.gov Plain Language](https://digital.gov/guides/plain-language/) | 행위자와 행동의 명확한 관계, 간결한 문서, 문맥에 맞는 브랜드 목소리, 지역별 일관성, 자연스러운 영어 문장부호. |
| `ja` | [Mozilla Japanese style guide](https://github.com/mozilla-l10n/styleguides/blob/main/docs/ja/l10nguideline.md), [chezou/slop-nuki](https://github.com/chezou/slop-nuki/tree/1bdf627b5991f4f806069619c9bde407960feac7), [iKora128/stop-ai-slop-jp](https://github.com/iKora128/stop-ai-slop-jp/tree/e09d32796f253a62693885757cea484c275d06f2), [RobTar97/japanese-writing-skills](https://github.com/RobTar97/japanese-writing-skills/tree/e4b1700464219c60da786f005a061bccffbbd4e3) 및 [coji/natural-japanese](https://github.com/coji/natural-japanese/tree/b54954f8deb4f110f0959f4e4fac295708900120) | 자연스러운 생략과 어순, 조사, 문맥에 맞는 높임말과 완충 표현, 컴포넌트별 명사형과 동사형, GUI 리소스 무결성, 밀도와 장르에 맞춘 검토. |
| `ko` | [Mozilla Korean style guide](https://github.com/mozilla-l10n/styleguides/blob/main/docs/ko/README.md), [dotoricode/korean-humanizer](https://github.com/dotoricode/korean-humanizer/tree/7dff5b48cc06fc4252d4766b802ecd61e62c50ad) 및 [HarryJhin/korean-writing](https://github.com/HarryJhin/korean-writing/tree/e4db3883ed76521b7a0cac30392fa67d182cc8ab) | 자연스러운 주어 생략, 조사와 띄어쓰기, `합니다`/`해요`/`다` 문체, 높임말 보존, 종결어미, 영어와 일본어 번역투 검토. |
| `es` | [Mozilla Spanish style guides](https://github.com/mozilla-l10n/styleguides/tree/main/docs/es) | 성과 수의 일치, 접어, `tú`/`usted`/`ustedes`, 문장형 대소문자를 쓰는 UI, 지역 용어, 문장부호, 영어 직역 표현. |

링크된 프로젝트에는 각각의 라이선스가 적용됩니다. [연구 기록](./research/multilingual-skill-research.md)에는 출처의 근거와 각 출처가 Humanization에 기여한 방식이 정리되어 있습니다. 해당 텍스트나 코드를 재사용하기 전에 각 저장소의 라이선스를 확인하세요. Humanization의 프로젝트별 지침은 위에서 정리한 실무 방식을 바탕으로 새로 작성했습니다.

## 설치

GitHub에서 Skill을 설치할 수 있는 에이전트에게 다음과 같이 요청합니다.

```text
https://github.com/thevenomsnake/humanization 에서 humanization Skill을 설치해 주세요. Skill은 humanization/ 디렉터리에 있습니다.
```

설치된 디렉터리 이름은 `humanization`으로 유지해야 합니다. 올바른 카드 이름은 `Humanization`이고, 여섯 개 언어 막대가 있는 짙은 초록색 H 아이콘을 사용하며, “Natural writing and GUI copy across six locales.”라고 표시됩니다. `活人感写作` 카드는 기존 `human-writing` Skill에 속하며, 위 메타데이터로 Humanization을 확인할 수 있습니다.

<details>
<summary><strong>수동 설치</strong></summary>

저장소의 [`humanization`](./humanization) 디렉터리를 Codex Skills 디렉터리로 복사합니다.

```text
$CODEX_HOME/skills/humanization/
```

</details>

사용할 때는 로캘, 형식, 적용 대상을 명시합니다.

```text
locale=ja, format=web-microcopy, surface=error로 $humanization을 사용하세요. CTA, 브랜드 용어, 플레이스홀더, 원본 리소스 구조를 보존하면서 이 오류 메시지를 다듬으세요.
```

공개 형식 이름 `web-microcopy`는 웹, 데스크톱, 모바일 제품의 HTML, JSON, YAML, ARB, PO, 소스 코드, 디자인 파일에 있는 GUI 텍스트를 모두 포함합니다.

같은 명시적 경로 지정으로 자동 검사기를 실행합니다.

```bash
python humanization/scripts/check_writing.py --locale en --format copy draft.md
python humanization/scripts/check_writing.py --locale es --format web-microcopy --source source.json target.json
```

## 3.0.0에서 달라진 점

- 안정적인 Skill 및 디렉터리 이름을 `humanization`으로, UI 표시 이름을 `Humanization`으로 확정했습니다.
- 런타임 지침을 하나의 공통 계약, 여섯 개 로캘 프로필, 하나의 GUI 마이크로카피 모듈로 나눴습니다.
- `kill-ai-slop`을 참고해 구체적인 정보, 절제된 표현, 패턴 일치를 검토 단서로 다루는 원칙을 추가했습니다.
- `--locale`과 `--format`을 명시하고, 여러 언어가 섞인 텍스트의 경로는 호출자가 선택하며, 어조 판단은 warning 수준에서 검토하도록 했습니다.

전체 변경 이력은 [CHANGELOG.md](./CHANGELOG.md)에서 확인할 수 있습니다.

## 저장소 구조

<details>
<summary><strong>전체 디렉터리 보기</strong></summary>

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

| 경로 | 용도 |
| :--- | :--- |
| [`SKILL.md`](./humanization/SKILL.md) | 각 작업을 공통, 로캘, 형식 모듈로 연결합니다. |
| [`core.md`](./humanization/references/core.md) | 사실, 출처, 기능, 개인정보, CTA, 브랜드 용어, 플레이스홀더, 최소 편집을 담당합니다. |
| [`locales/`](./humanization/references/locales) | 여섯 개 언어의 고유한 작성 프로필을 담습니다. |
| [`expressive-text.md`](./humanization/references/formats/expressive-text.md) | GUI가 아닌 제품, 문서, 마케팅, 이메일, 소셜 카피를 다룹니다. |
| [`gui-microcopy.md`](./humanization/references/formats/gui-microcopy.md) | GUI 컴포넌트의 역할과 구조화된 리소스 보호 규칙을 정의합니다. |
| [`check_writing.py`](./humanization/scripts/check_writing.py) | 공통, 로캘, GUI 검사를 위한 단일 CLI를 제공합니다. |
| [`check_zh_cn.py`](./humanization/scripts/check_zh_cn.py) | 기존 동작 수준 검사기의 범위를 `zh-CN prose`로 제한합니다. |

</details>

## 출처 표기와 피드백

Humanization은 MIT License로 배포됩니다. 최초의 `zh-CN` 장문 기반은 같은 MIT License로 배포된 [KKKKhazix/human-writing v1.1.0](https://github.com/KKKKhazix/human-writing/tree/cd879d22c8588125c1869d0b443f5d8df74b4192)을 바탕으로 합니다. 위 출처 목록은 현재 구조에 영향을 준 프로젝트와 지침에 감사를 표하고, 각각의 기여를 설명합니다.

규칙 충돌, 오탐, 모델별 문제를 발견하면 프롬프트, 관련 출력, 예상한 결과와 함께 [이슈를 등록해 주세요](https://github.com/thevenomsnake/humanization/issues).

<p align="center">
  <sub>Humanization · 3.0.0</sub>
</p>
