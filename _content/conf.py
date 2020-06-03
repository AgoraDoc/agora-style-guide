# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(1, '/usr/local/lib/python3.7/site-packages/')
import recommonmark
from recommonmark.transform import AutoStructify


# -- Project information -----------------------------------------------------

project = 'Agora Developer Document Style Guide'
copyright = '2020, Agora.io'
author = 'Agora Tech Comm'

github_doc_root = 'https://github.com/AgoraDoc/Agora_style_guide/tree/master/_content/'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autosectionlabel',
    'recommonmark',
    'sphinx_markdown_tables'
]

# Prefix document path to section labels, otherwise autogenerated labels would look like 'heading'
# rather than 'path/to/file:heading'
autosectionlabel_prefix_document = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# try different latex engines
latex_engine = 'xelatex'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# If you have your own conf.py file, it overrides Read the Doc's default conf.py. 
# By default, Sphinx expects the master doc to be contents. 
# Read the Docs will set master doc to index instead (or whatever it is you have specified in your settings). Try adding this to your conf.py:
# https://github.com/readthedocs/readthedocs.org/issues/2569

master_doc = 'index'


html_theme_options = {
    'logo_only': True,
    'display_version': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'style_nav_header_background': '#343131',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}
html_logo = 'img/logo.png'
html_favicon = 'img/favicon.ico'

# recommonmark advanced options
def setup(app):
    app.add_config_value('recommonmark_config', {
            'url_resolver': lambda url: github_doc_root + url,
            'auto_toc_tree_section': 'Contents',
            }, True)
    app.add_transform(AutoStructify)