# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'bokeh-a11y-audit'
copyright = '2024, Bokeh contributors'
author = 'Bokeh contributors'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinxcontrib.video",
    ]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_title = "Bokeh Accessibility Audit"

html_static_path = ['_static']

html_theme_options = {
  "show_toc_level": 2,
  "use_edit_page_button": True,
}

html_show_sourcelink = False

html_context = {
    "github_user": "Quansight-Labs",
    "github_repo": "bokeh-a11y-audit",
    "github_version": "main",
    "doc_path": "source",
}
