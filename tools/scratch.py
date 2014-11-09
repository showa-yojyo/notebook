#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Generate note templates.

Examples:
  $ scratch.py milestone09
  $ scratch.py gamma95 --separate=3
"""
from argparse import ArgumentParser
from jinja2 import Environment
from jinja2 import FileSystemLoader

def main(args):
    """The main function.

    Args:
      args: An instance of argparse.ArgumentParser after
        parse_args() called.

    Returns:
        None.
    """

    env = Environment(loader=FileSystemLoader('.'))
    filename = args.file_name[0]
    num_page = args.separate

    params = dict(title=args.title,
                  author=args.author,
                  interpreter=args.interpreter,
                  publisher=args.publisher,
                  isbn=args.isbn,
                  notename=filename)

    if num_page == 1:
        template = env.get_template(args.page_template)
        params['page'] = 0
        params['totalpages'] = 0
    else:
        template = env.get_template(args.cover_template)

    with open('{}.rst'.format(filename), mode='w', encoding='utf-8') as fout:
        print(template.render(params), file=fout)

    if num_page == 1:
        return

    template = env.get_template(args.page_template)
    for i in range(1, num_page + 1):
        with open('{}-note{:d}.rst'.format(filename, i),
                  mode='w', encoding='utf8') as fout:
            print(template.render(params, page=i, totalpages=num_page),
                  file=fout)

if __name__ == '__main__':
    parser = ArgumentParser(description='Generate note templates.')
    parser.add_argument(
        'file_name',
        nargs=1,
        help='TBW')
    parser.add_argument(
        '--title',
        default='タイトル',
        help='TBW')
    parser.add_argument(
        '--author',
        default='著者',
        help='TBW')
    parser.add_argument(
        '--interpreter',
        default='訳者',
        help='TBW')
    parser.add_argument(
        '--publisher',
        default='出版社',
        help='TBW')
    parser.add_argument(
        '--isbn',
        default='ISBN-XXXXX',
        help='TBW')
    parser.add_argument(
        '--separate',
        type=int,
        default='1',
        help='TBW')
    parser.add_argument(
        '--cover_template',
        default='toc.rst_t',
        help='TBW')
    parser.add_argument(
        '--page_template',
        default='note.rst_t',
        help='TBW')

    main(parser.parse_args())
