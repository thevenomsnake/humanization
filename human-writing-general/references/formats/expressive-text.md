# Expressive text

Use `format=copy` when the output is bounded text rather than a long article. This includes product pages, documentation, help content, release notes, email, social posts, campaign copy, captions, form guidance, labels, statuses, errors, empty states, privacy notices, metadata, and accessible names.

## Input contract

Record the target locale, surface, audience, purpose, source facts, call to action, length or space limit, brand terms, non-translatable terms, and any capability or privacy claim. A surface can be a button, page section, tooltip, notification, email, or paragraph in a document.

## Output rules

- Keep one primary job per string or paragraph. Do not force every surface into a headline plus slogan plus CTA.
- Preserve facts, scope, uncertainty, brand terms, and user action across locales; let wording and length change naturally.
- Use the target locale profile and `references/text/anti-slop.md`. Treat template hits as review prompts, not automatic failures.
- Short text does not need the long-form material count, but every claim still needs a source or an explicit product contract.
- For HTML fields, also read `web-microcopy.md` for `lang`, metadata, control names, status messages, and error recovery.
