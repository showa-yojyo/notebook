"""disablesearchindex.py: Disable searchindex.js generation.

See https://groups.google.com/d/topic/sphinx-users/vzSAi8SM3aY
"""

def on_builder_inited(app):
    if app.builder.name == 'html':
        app.builder.search = False

def setup(app):
    app.connect('builder-inited', on_builder_inited)
