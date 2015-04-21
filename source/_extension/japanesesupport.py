# -*- coding: utf-8 -*-
"""japanesesupport.py: A custom Sphinx extension module.

This extension removes the unwanted white spaces among Japanese characters
that Sphinx (Docutils) appends.

References:
  * Sphinx-Users.jp <http://sphinx-users.jp/reverse-dict/html/japanese.html>
  * Sphinx-Users 304 <http://www.python.jp/pipermail/sphinx-users/2012-July/000303.html>
"""

import re
UNWANTED_SPACES_PATTERN = re.compile(r'([^!-~])[\n\r\t]+([^!-~])')

def trunc_whitespace(app, doctree, docname):
    from docutils.nodes import Text, paragraph
    if not app.config.japanesesupport_trunc_whitespace:
        return

    for node in doctree.traverse(Text):
        parent = node.parent
        if isinstance(parent, paragraph):
            newtext = UNWANTED_SPACES_PATTERN.sub(r"\1\2", node.astext())
            parent.replace(node, Text(newtext))

def setup(app):
    app.add_config_value('japanesesupport_trunc_whitespace', True, True)
    app.connect("doctree-resolved", trunc_whitespace)
