# Translations

Translations for both the Python/Jinja backend and the React (i18next) UI are
managed by `./run.sh translations` (oarepo-tools `make-translations`).

**Edit only `translations/<lang>/LC_MESSAGES/messages.po`** (in the repository
root). It is the single source of truth: strings from Python, Jinja templates
and JS/JSX under `ui/` are extracted into it, and the translations are compiled
from it.

The files in this directory are generated – do not edit them by hand:

- `semantic-ui/translations/messages/<lang>/LC_MESSAGES/translations.json` –
  i18next catalogues compiled from the `.po` files
- `semantic-ui/translations/messages/index.js` – regenerated on every run
- `semantic-ui/translations/i18next.js` – overwritten by oarepo-tools on every run

In JS, import the repository translations with
`import { i18next } from "@translations/i18next";`.

See [https://nrp-cz.github.io/docs/customize/repository_ui/i18n](https://nrp-cz.github.io/docs/customize/repository_ui/i18n) for more details.
