#!/usr/bin/env python3
"""Small self-check for the multilingual expressive-text checker."""

from check_writing import check_generic


SLOP_SAMPLES = {
    "zh-CN": "这不只是工具，而是一次革命性升级。",
    "zh-TW": "這不只是工具，而是一場革命性的升級。",
    "en": "It is not just fast, it is revolutionary.",
    "ja": "単なるツールではなく、次のレベルです。",
    "ko": "단순한 도구가 아니라 차원이 다릅니다.",
    "es": "No solo es rápido, es revolucionario.",
}


def main() -> None:
    for locale, text in SLOP_SAMPLES.items():
        failures, warnings = check_generic(text, locale, "copy", [])
        assert not failures, (locale, failures)
        assert warnings, f"expected a review warning for {locale}"

    html = (
        '<html lang="en"><head><title>Settings</title>'
        '<meta name="description" content="A revolutionary dashboard."></head>'
        '<body><button>Save</button></body></html>'
    )
    failures, warnings = check_generic(html, "en", "web-microcopy", [])
    assert not failures, failures
    assert warnings, "expected metadata copy to be scanned"

    failures, _ = check_generic("中文 — 文案", "zh-CN", "copy", [])
    assert failures, "expected the Chinese punctuation hard rule to fail"
    print("check_writing smoke passed")


if __name__ == "__main__":
    main()
