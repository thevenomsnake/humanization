#!/usr/bin/env python3
"""Check explicit-locale expressive text or HTML microcopy without guessing."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

LOCALES = ("zh-CN", "zh-TW", "en", "ja", "ko", "es")
FORMATS = ("prose", "copy", "web-microcopy")

# ponytail: regexes are review leads; add locale-aware parsing only if warning precision becomes a real problem.
TEXT_SLOP_PATTERNS: dict[str, tuple[tuple[str, re.Pattern[str]], ...]] = {
    "en": (
        ("contrast slogan", re.compile(r"\bnot just\b.{1,80}\b(?:it(?:'s| is)|but)\b|\bsay goodbye to\b", re.I | re.S)),
        ("empty promise", re.compile(r"\b(?:revolutionary|seamless(?:ly)?|effortless(?:ly)?|next[- ]level|unlock the power|supercharge)\b", re.I)),
        ("invented social proof", re.compile(r"\b(?:\d+[km]\+\s+(?:users|teams|customers)|99\.9+%|24/7)\b", re.I)),
    ),
    "zh-CN": (
        ("模板化翻案", re.compile(r"(?:不是|并非|不在于|不只是)[^。！？\n]{0,80}(?:而是|而在于)|说到底|真正的?问题是")),
        ("空泛承诺", re.compile(r"赋能|抓手|降本增效|革命性|无缝|颠覆性")),
    ),
    "zh-TW": (
        ("模板化翻案", re.compile(r"(?:不是|並非|不在於|不只是)[^。！？\n]{0,80}(?:而是|而在於)|說到底|真正的?問題是")),
        ("空泛承諾", re.compile(r"賦能|抓手|降本增效|革命性|無縫|顛覆性")),
    ),
    "ja": (
        ("対比スローガン", re.compile(r"単なる.{0,60}(?:ではなく|ではありません)|さようなら.{0,30}(?:課題|悩み)")),
        ("空疎な約束", re.compile(r"革命的|シームレス|次のレベル|可能性を解き放|簡単に実現")),
    ),
    "ko": (
        ("대조형 슬로건", re.compile(r"단순한.{0,60}(?:아니|넘어|것이 아니라)|이제.{0,20}(?:작별|안녕)")),
        ("공허한 약속", re.compile(r"혁신적|끊김 없이|차원이 다른|잠재력을 깨우|손쉽게")),
    ),
    "es": (
        ("eslogan de contraste", re.compile(r"\bno solo\b.{1,80}\b(?:sino|es)\b|\bdile adiós a\b", re.I | re.S)),
        ("promesa vacía", re.compile(r"\b(?:revolucionari[oa]|sin fisuras|de siguiente nivel|libera el potencial|sin esfuerzo)\b", re.I)),
    ),
}


def read_input(path: str) -> str:
    return sys.stdin.read() if path == "-" else Path(path).read_text(encoding="utf-8")


def terms_missing(text: str, terms: list[str]) -> list[str]:
    return [term for term in terms if term not in text]


def check_web(text: str, locale: str) -> list[str]:
    failures: list[str] = []
    lang = re.search(r"\blang\s*=\s*['\"]([^'\"]+)['\"]", text, re.I)
    if not lang or lang.group(1) != locale:
        failures.append(f"lang must be declared as {locale}")
    title = re.search(r"<title(?:\s[^>]*)?>(.*?)</title>", text, re.I | re.S)
    if not title or not re.sub(r"<[^>]+>", "", title.group(1)).strip():
        failures.append("<title> must be non-empty")
    description = re.search(
        r"<meta\b(?=[^>]*\bname\s*=\s*['\"]description['\"])(?=[^>]*\bcontent\s*=\s*['\"][^'\"]+['\"])[^>]*>",
        text,
        re.I,
    )
    if not description:
        failures.append("meta[name=description] must have non-empty content")

    controls = list(re.finditer(r"<(button|select|textarea)\b([^>]*)>(.*?)</\1>", text, re.I | re.S))
    controls.extend(re.finditer(r"<input\b([^>]*)/?>", text, re.I | re.S))
    for match in controls:
        tag = match.group(1) if match.lastindex == 3 else "input"
        attrs = match.group(2) if match.lastindex == 3 else match.group(1)
        body = match.group(3) if match.lastindex == 3 else ""
        has_name = re.search(r"\baria-label\s*=\s*['\"][^'\"]+['\"]", attrs, re.I)
        labelled = re.search(r"\bid\s*=\s*['\"]([^'\"]+)['\"]", attrs, re.I)
        has_for = labelled and re.search(rf"<label\b[^>]*\bfor\s*=\s*['\"]{re.escape(labelled.group(1))}['\"]", text, re.I)
        if not has_name and not body.strip() and not has_for:
            failures.append(f"<{tag.lower()}> needs visible text, label, or aria-label")

    for role in ("status", "alert"):
        for match in re.finditer(rf"<[^>]*\brole\s*=\s*['\"]{role}['\"][^>]*>(.*?)</[^>]+>", text, re.I | re.S):
            if not re.sub(r"<[^>]+>", "", match.group(1)).strip():
                failures.append(f"role={role} must contain text")

    og_fields = set(re.findall(r"\bproperty\s*=\s*['\"](og:[^'\"]+)['\"]", text, re.I))
    if og_fields:
        failures.extend(f"missing Open Graph field {field}" for field in ("og:title", "og:type", "og:url", "og:image") if field not in og_fields)
    return failures


def check_text_slop(text: str, locale: str, format_name: str) -> list[str]:
    if format_name == "web-microcopy":
        attributes = re.findall(
            r"\b(?:content|aria-label|alt|placeholder|title|value)\s*=\s*['\"]([^'\"]+)['\"]",
            text,
            re.I,
        )
        text = " ".join(attributes) + " " + re.sub(r"<[^>]+>", " ", text)
    warnings: list[str] = []
    for label, pattern in TEXT_SLOP_PATTERNS.get(locale, ()):
        matches = list(pattern.finditer(text))
        if matches:
            warnings.append(
                f"文本反模板信号 {label} {len(matches)} 处；确认它是否有事实、引用或真实语境，没有就改成直接陈述。"
            )
    return warnings


def check_generic(
    text: str, locale: str, format_name: str, brand_terms: list[str]
) -> tuple[list[str], list[str]]:
    failures: list[str] = []
    warnings = check_text_slop(text, locale, format_name)
    if not text.strip():
        failures.append("input is empty")
    failures.extend(f"missing declared brand term: {term}" for term in terms_missing(text, brand_terms))
    if format_name == "web-microcopy":
        failures.extend(check_web(text, locale))
    if locale in {"zh-CN", "zh-TW"} and re.search(r"[\u4e00-\u9fff]", text):
        if "\u2014" in text or "\u2013" in text:
            failures.append("Chinese prose contains an em dash or en dash; use the selected Chinese profile's punctuation")
    return failures, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Check expressive text with an explicit locale and format")
    parser.add_argument("--locale", choices=LOCALES, required=True)
    parser.add_argument("--format", dest="format_name", choices=FORMATS, required=True)
    parser.add_argument("--brand-term", action="append", default=[])
    parser.add_argument("path", help="UTF-8 file path or - for stdin")
    args = parser.parse_args()
    text = read_input(args.path)
    failures, warnings = check_generic(text, args.locale, args.format_name, args.brand_term)
    if args.locale == "zh-CN" and args.format_name == "prose" and args.path != "-" and not failures:
        checker = Path(__file__).with_name("check_zh_cn.py")
        result = subprocess.run([sys.executable, str(checker), args.path], text=True)
        if result.returncode:
            return result.returncode
    if failures:
        print("\n".join(f"- {failure}" for failure in failures))
        return 1
    if warnings:
        print("\n需要人工判断")
        print("\n".join(f"- {warning}" for warning in warnings))
    print(f"OK locale={args.locale} format={args.format_name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
