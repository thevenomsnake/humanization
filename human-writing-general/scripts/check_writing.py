#!/usr/bin/env python3
"""Check explicit-locale prose or HTML microcopy without guessing language."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

LOCALES = ("zh-CN", "zh-TW", "en", "ja", "ko", "es")
FORMATS = ("prose", "web-microcopy")


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


def check_generic(text: str, locale: str, format_name: str, brand_terms: list[str]) -> list[str]:
    failures = []
    if not text.strip():
        failures.append("input is empty")
    failures.extend(f"missing declared brand term: {term}" for term in terms_missing(text, brand_terms))
    if format_name == "web-microcopy":
        failures.extend(check_web(text, locale))
    elif locale in {"zh-CN", "zh-TW"} and re.search(r"[\u4e00-\u9fff]", text):
        if "\u2014" in text or "\u2013" in text:
            failures.append("Chinese prose contains an em dash or en dash; use the selected Chinese profile's punctuation")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Check writing with an explicit locale and format")
    parser.add_argument("--locale", choices=LOCALES, required=True)
    parser.add_argument("--format", dest="format_name", choices=FORMATS, required=True)
    parser.add_argument("--brand-term", action="append", default=[])
    parser.add_argument("path", help="UTF-8 file path or - for stdin")
    args = parser.parse_args()
    text = read_input(args.path)
    failures = check_generic(text, args.locale, args.format_name, args.brand_term)
    if args.locale == "zh-CN" and args.format_name == "prose" and args.path != "-" and not failures:
        checker = Path(__file__).with_name("check_zh_cn.py")
        result = subprocess.run([sys.executable, str(checker), args.path], text=True)
        if result.returncode:
            return result.returncode
    if failures:
        print("\n".join(f"- {failure}" for failure in failures))
        return 1
    print(f"OK locale={args.locale} format={args.format_name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
