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

# -- Project information -----------------------------------------------------

# The documented project’s name.
project = '読書ノート'

# The author name(s) of the document.
author = 'プレハブ小屋'

# A copyright statement in the style '2008, Author Name'.
copyright = f'1999-{date.today().year}, {author} All rights reserved'

# The short X.Y version.
# The major project version, used as the replacement for |version|.
version = '1.5'

# The full project version, used as the replacement for |release| and e.g. in
# the HTML templates.
release = '1.5'

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'disablesearchindex',
    'IPython.sphinxext.ipython_console_highlighting',
    'IPython.sphinxext.ipython_directive',
    'japanesesupport',
    'sphinx.ext.githubpages',
    'sphinx.ext.mathjax',
    'sphinx.ext.todo',
    'sphinxcontrib.mermaid',]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
root_doc = 'index'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# A list of warning types to suppress arbitrary warning messages.
suppress_warnings = ['autosectionlabel.*']

# -- Options for HTML output -------------------------------------------------

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
    'body_text': 'black',
    'caption_font_family': 'initial',
    'description': '個人的な読書、学習、研究ノート。',
    'description_font_style': 'initial',
    'font_family': 'initial',
    'font_size': 'initial',
    'footer_text': 'black',
    'head_font_family': 'initial',
    'github_button': False,
    'github_repo': 'notebook',
    'github_user': 'showa-yojyo',
    'link': 'deeppink',
    'link_hover': 'deeppink',
    'narrow_sidebar_link': 'deeppink',
    'nosidebar': True,
    'page_width': '1200px',
    'show_powered_by': False,
    'show_relbars': True,
    'sidebar_link': 'deeppink',
    'sidebar_link_underscore': 'deeppink',
    'sidebar_text': 'initial',
}

# A list of JavaScript filename.
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
        #'searchbox.html',
        'donate.html',
    ]
}

# If false, no index is generated.
html_use_index = False

# If true, the reST sources are included in the HTML build as _sources/name. The
# default is True.
html_copy_source = False

# If true (and html_copy_source is true as well), links to the reST sources will
# be added to the sidebar.
html_show_sourcelink = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, the text around the keyword is shown as summary of each search
# result. Default is True.
html_show_search_summary = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#html_search_scorer = 'scorer.js'

# -- Options for MathJax -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/math.html

# Use customized version
mathjax_path = "mathjax-v3.js"

# -- Options for sphinx.ext.todo
# https://www.sphinx-doc.org/en/master/usage/extensions/todo.html

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Options for Mermaid -------------------------------------------------
# https://github.com/mgaitan/sphinxcontrib-mermaid

# See html_js_files
mermaid_version = ""
mermaid_init_js = ""
