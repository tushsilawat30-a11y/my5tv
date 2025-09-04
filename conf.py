# conf.py — My5 TV Guide Center (No footer at all)

import os
import sys
from datetime import datetime

# -- Project information -----------------------------------------------------
project = "My5 TV Guide Center (USA)"
author = "My5 Support Team"
release = "1.0.0"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx_rtd_theme",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "en"

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_title = "Activate My5 TV – my5.tv/activate (USA Guide)"
html_short_title = "My5 TV – Activate"
html_favicon = "favicon.ico"
html_static_path = ["_static"]

# Remove default footer & source links
html_show_sourcelink = False
html_show_sphinx = False   # “Built with Sphinx…” hata dega

html_theme_options = {
    "collapse_navigation": False,
    "sticky_navigation": True,
    "navigation_depth": 3,
    "style_external_links": True,
}

# Custom CSS for branding
def setup(app):
    app.add_css_file("custom.css")
