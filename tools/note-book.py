#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""note-book.py: Convert tab-separeted values to a Sphinx document.

Requirements
------------
* jinja2 (pip install)
* isbn_hyphenate (pip install)
"""

import sys
from argparse import (ArgumentParser, FileType)
import csv
from jinja2 import Environment
from isbn_hyphenate import hyphenate

__version__ = '1.1.1'

TEMPLATE = '''\
======================================================================
ノート準備中書籍群
======================================================================

.. contents::
{% for book in books %}
{{ book["title"] }}
======================================================================

:著者: {{ book["authors"] }}
{%- if "reinterpreters" in book %}
:訳者: {{ book["reinterpreters"] }}
{%- endif %}
:出版社: {{ book["publisher"] }}
:発行年: {{ book["pubyear"] }} 年
:ISBN: {{ book["isbn"] }}
{%- if "url" in book %}
:関連 URL: `あり <{{ book["url"] }}>`__
{% else %}
:関連 URL: なし
{%- endif %}
.. todo::

   寸評を記す。
{% endfor -%}
'''

def configure():
    """Return the command line parameter."""

    parser = ArgumentParser()
    parser.add_argument(
        '--version', action='version', version=__version__)

    parser.add_argument(
        'file',
        metavar='FILE',
        nargs='?',
        type=FileType(mode='r', encoding='utf-8'),
        default=sys.stdin)

    return parser

def read(source):
    """Read TSV from the source."""

    reader = csv.DictReader(source, delimiter='\t', quoting=csv.QUOTE_NONE)
    header = reader.fieldnames
    books = [book for book in reader]

    return header, books

def parse(input):
    """Parse the input data."""

    for i in input:
        if i["reinterpreters"] == "n/a":
            del i["reinterpreters"]
        if i["url"] == 'unknown':
            del i["url"]

        i.update(isbn=hyphenate(i["isbn"]))

    env = Environment(autoescape=False)
    templ = env.from_string(TEMPLATE)

    return templ.render(books=input)

def write(output, destination):
    """Write the output to the destination."""

    print(output, file=destination)

def main():
    """The main function."""

    args = configure().parse_args()

    header, books = read(args.file)
    write(parse(books), sys.stdout)

if __name__ == '__main__':
    main()
