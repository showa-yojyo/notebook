#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""note-book.py: Convert tab-separeted values to a Sphinx document.

Requirements
------------
* jinja2 (pip install)
* isbn_hyphenate (pip install)
"""

import sys
from argparse import ArgumentParser
from argparse import FileType
import csv
from jinja2 import Environment
from isbn_hyphenate import hyphenate

TEMPLATE = '''\
======================================================================
THE TITLE
======================================================================

..contents::

{%- for book in books %}
{{ book["title"] }}
======================================================================

:著者: {{ book["authors"] }}
{%- if "reinterpreters" in book %}
:訳者: {{ book["reinterpreters"] }}
{%- endif %}
:出版社: {{ book["publisher"] }}
:ISBN: {{ book["isbn"] }}

.. todo::

   寸評を記す。

{% endfor -%}
'''

def configure():
    """Parse the command line parameters.

    Returns:
        The arguments for this program.
    """

    parser = ArgumentParser(description='Note Template Generator')
    parser.add_argument('--version', action='version', version='0.0.0')

    parser.add_argument(
        'infile', nargs='?',
        type=FileType(mode='r', encoding='utf-8'),
        default=sys.stdin)

    return parser.parse_args()

def read(source):
    """Read TSV from the source."""

    books = []
    reader = csv.DictReader(source, delimiter='\t', quoting=csv.QUOTE_NONE)
    header = reader.fieldnames
    books = [book for book in reader]

    return header, books

def parse(input):
    """Parse the input data."""

    for i in input:
        if i["reinterpreters"] == "n/a":
            del i["reinterpreters"]

        i.update(isbn=hyphenate(i["isbn"]))

    env = Environment(autoescape=False)
    templ = env.from_string(TEMPLATE)

    return templ.render(books=input)

def write(output, destination):
    """Write the output to the destination."""

    print(output, file=destination)

def main(args):
    """The main function."""

    header, books = read(args.infile)
    output = parse(books)
    write(output, sys.stdout)

if __name__ == '__main__':
    main(configure())
