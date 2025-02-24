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
    "sphinxext.opengraph",
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

# -- Opengraph setup -------------------------------------------------
ogp_site_url = "https://bokeh-a11y-audit.readthedocs.io/"
ogp_image = "https://static.bokeh.org/branding/icons/bokeh-icon.png"
ogp_site_name = False # So we can customise the name with tags
ogp_custom_meta_tags = [
    '<meta property="og:site_name" content="Bokeh Accessibility Audit">',
    '<meta name="twitter:card" content="summary">'
    '<meta property="twitter:title" content="Bokeh Accessibility Audit">',
]
ogp_social_media_cards ={
  "image": "./images/bokeh-icon.png",
}
# generates description from the page content
ogp_enable_meta_description = True
