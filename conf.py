# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# Add project source path if needed (e.g., ../src)
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Set Up My5 TV'
copyright = '2025, My5'
author = 'My5 Support Team'
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx_rtd_theme",   # Theme extension
]

# Allow raw HTML in RST
rst_prolog = """
.. raw:: html

   <style>
      /* Custom Button Hover Effects */
      a:hover {
         opacity: 0.9;
      }
   </style>
"""

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_title = "How to Get Started with My5 TV – Complete Guide"
html_short_title = "My5 TV Setup Guide"
html_favicon = 'favicon.ico'  # Put favicon.ico inside _static

# Hide "View page source"
html_show_sourcelink = False

# Allow unsafe raw HTML
suppress_warnings = ["misc.highlighting_failure"]

# Theme customization
html_theme_options = {
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 3,
    'style_external_links': True,
}

# Static files (CSS/JS/images)
html_static_path = ['_static']

# Custom CSS for branding
def setup(app):
    app.add_css_file('custom.css')
