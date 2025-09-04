# conf.py — My5 TV Guide Center (USA)

import os
import sys
from datetime import datetime

# -- Project information -----------------------------------------------------
project = "My5 TV Guide Center (USA)"
author = "My5 Support Team"
copyright = ""   # Blank footer
release = "1.0.0"

# -- General configuration ---------------------------------------------------
extensions = ["sphinx_rtd_theme"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "en"

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_title = "Activate My5 TV – my5.tv/activate (USA Guide)"
html_short_title = "My5 TV – Activate"
html_favicon = "favicon.ico"
html_static_path = ["_static"]

# Hide defaults
html_show_sourcelink = False
html_show_sphinx = False   # removes "Built with Sphinx"

html_theme_options = {
    "collapse_navigation": False,
    "sticky_navigation": True,
    "navigation_depth": 3,
    "style_external_links": True,
}

# Add custom CSS
def setup(app):
    app.add_css_file("custom.css")
