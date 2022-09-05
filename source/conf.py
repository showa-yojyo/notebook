# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys
import os
from datetime import date

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

sys.path.append(os.path.abspath('./_extension'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'IPython.sphinxext.ipython_console_highlighting',
    'IPython.sphinxext.ipython_directive',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinxcontrib.mermaid',
    'japanesesupport',
    'disablesearchindex',]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '読書ノート'
author = 'プレハブ小屋'
copyright = f'1999-{date.today().year}, {author} All rights reserved'

# The short X.Y version.
version = '1.5'
# The full version, including alpha/beta/rc tags.
release = '1.5dev'

# A list of warning types to suppress arbitrary warning messages.
suppress_warnings = ['autosectionlabel.*']

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes:
# https://www.sphinx-doc.org/en/master/usage/theming.html
#
# Alabaster and Scrolls themes are mobile-optimated.
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'description': '個人的な読書、学習、研究ノート。',
    'github_user': 'showa-yojyo',
    'github_repo': 'notebook',
    'show_powered_by': False,
    'show_relbars': True,
}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []
#html_theme_path = ["."]

html_js_files = [
    #'mathjax-v3.js', # move to mathjax_path
    'mermaid.js',
]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%Y-%m-%d (%a) %H:%M:%S (%Z)'

# Custom sidebar templates, maps document names to template names.
# Alabaster wants explicit settings for sidebars:
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',
        'searchbox.html',
        'donate.html',
    ]
}

# If false, no index is generated.
html_use_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'h', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'r', 'sv', 'tr'
#html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
#html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#html_search_scorer = 'scorer.js'

# -- Options for MathJax -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/math.html

# Use customized version
mathjax_path = "mathjax-v3.js"

# -- Options for Mermaid -------------------------------------------------
# https://github.com/mgaitan/sphinxcontrib-mermaid

# See html_js_files
mermaid_version = ""
mermaid_init_js = ""
