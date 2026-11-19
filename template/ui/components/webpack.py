from invenio_assets.webpack import WebpackThemeBundle

theme = WebpackThemeBundle(
    __name__,
    ".",
    default="semantic-ui",
    themes={
        "semantic-ui": {
            "entry": {
                "components": "./js/custom-components.js",
            },
            "dependencies": {},
            # less is pinned below 4.6: less 4.6 is published as ES modules only,
            # while less-loader (used by the Invenio webpack build) loads it with require()
            "devDependencies": {"less": "4.5.1"},
            "aliases": {},
        }
    },
)
