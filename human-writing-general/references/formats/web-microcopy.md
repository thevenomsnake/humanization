# Web microcopy

Use this branch for short text attached to a page or component. It covers page titles, navigation, buttons, labels, statuses, errors, empty states, privacy notices, `title`, `meta[name=description]`, Open Graph fields, and accessible names.

## Input contract

Require `locale`, audience, surface/component, supported facts, desired action, brand terms, non-translatable terms, and any privacy or capability claim. Record the same contract for each locale in a multilingual set; wording and length may differ.

## Rules

- Give each string one job. A button names an action, a label names its control, and a status describes a current state.
- State only supported product behavior. Do not promise collection, deletion, encryption, availability, integrations, or results that the product cannot demonstrate.
- Make errors identifiable in text and add a recovery step. Make empty states say what is missing and how to begin.
- Keep `title`, description, Open Graph copy, visible CTA, and accessible names aligned to the same facts and brand terms.
- Use the selected locale's profile for punctuation, register, spelling, and translation choices. Never use long-form material counts or paragraph-length rules to reject a short string.

## Deterministic HTML checks

For an HTML input, `scripts/check_writing.py` checks a non-empty `lang` matching the requested locale, a non-empty `<title>`, a description meta tag, accessible names for buttons and form controls, and text for status/error roles. It reports missing Open Graph fields when any `og:*` field is present. It cannot judge naturalness, tone, or whether a privacy statement is legally sufficient.
