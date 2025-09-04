# conf.py — My5 TV (USA) Guide Center

import os
import sys
from datetime import datetime

# -- Path setup --------------------------------------------------------------
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------
project = "My5 TV Guide Center (USA)"
author = "My5 Support Team"
copyright = f"{datetime.now():%Y}, My5"
release = "1.0.0"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx_rtd_theme",   # Read the Docs theme
    # "sphinx_sitemap",   # <-- Optional: enable after setting html_baseurl below
]

# Keep warnings cleaner when using raw HTML in .rst
suppress_warnings = ["misc.highlighting_failure"]

# If you ever want Markdown, add "myst_parser" and allow .md in source_suffix.
# source_suffix = {".rst": "restructuredtext"}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Language/locale
language = "en"

# -- HTML output -------------------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_title = "Activate My5 TV – my5.tv/activate (USA Guide)"
html_short_title = "My5 TV – Activate"
html_favicon = "favicon.ico"  # place inside _static/
html_static_path = ["_static"]

# Optional: if you add a logo, put it in _static and uncomment:
# html_logo = "_static/my5-logo.png"

# Hide “View page source”
html_show_sourcelink = False

# Theme options (tidy, sticky nav, deeper TOC)
html_theme_options = {
    "collapse_navigation": False,
    "sticky_navigation": True,
    "navigation_depth": 3,
    "style_external_links": True,
    # "logo_only": True,  # if you want only logo in header
}

# ---- SEO (optional) --------------------------------------------------------
# If you enable sphinx_sitemap, set your canonical base URL:
# html_baseurl = "https://www.yoursite.com/my5tv-activate/"  # <-- update this

# -- Custom assets -----------------------------------------------------------
def setup(app):
    # Custom CSS for My5 branding (red/black/white)
    app.add_css_file("custom.css")
    # If you have custom JS, add it similarly:
    # app.add_js_file("custom.js")

# -- HTML context / extra ----------------------------------------------------
# Ensure Sphinx finds your custom layout at _templates/custom_layout.html
# (Your template extends "!layout.html" and injects SEO meta tags.)
