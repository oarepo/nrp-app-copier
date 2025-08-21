from oarepo_ui.resources import TemplatePageUIResource, TemplatePageUIResourceConfig


class TitlePageResourceConfig(TemplatePageUIResourceConfig):
    url_prefix = "/"
    blueprint_name = "titlepage"
    template_folder = "templates"
    pages = {
        "": "TitlePage",
    }


def create_blueprint(app):
    """Register blueprint for this resource."""
    return TemplatePageUIResource(TitlePageResourceConfig()).as_blueprint()
