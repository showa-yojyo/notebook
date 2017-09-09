#!/usr/bin/env python
"""Generate note templates.

Examples:
  $ scratch.py milestone09
  $ scratch.py gamma95 --pages=3
"""
import sys
from argparse import ArgumentParser
from pathlib import Path
from jinja2 import (Environment, FileSystemLoader)

def run(args):
    """The main function.

    Args:
      args: An instance of argparse.ArgumentParser after
        parse_args() called.
    """

    env = Environment(loader=FileSystemLoader(
        str(Path(__file__).parent)))
    note_name = args.note_name[0]
    num_page = args.pages

    params = dict(title=args.title,
                  note_name=note_name)

    # Case of a single page is specified.
    if num_page == 1:
        template = env.get_template(args.page_template)
        params['page'] = 0
        params['totalpages'] = 0

        with open('{}.rst'.format(note_name), mode='w', encoding='utf-8') as fout:
            print(template.render(params), file=fout)

        return

    # Case of an exclusive directory, index.rst, and note[1-9].rst.

    # Execute `mkdir -p note_name`.
    dest = Path.cwd() / note_name
    dest.mkdir(exist_ok=True)

    # Generate index.rst.
    template = env.get_template(args.index_template)
    with open(dest / 'index.rst', mode='w', encoding='utf-8') as fout:
        print(template.render(params), file=fout)

    # Generate note[1-9].rst.
    template = env.get_template(args.page_template)
    for i in range(1, num_page + 1):
        with open(dest / 'note{:d}.rst'.format(i),
                  mode='w', encoding='utf8') as fout:
            print(template.render(params, page=i, totalpages=num_page),
                  file=fout)

def parse_args(args):
    parser = ArgumentParser(description='Generate note templates.')
    parser.add_argument(
        'note_name',
        nargs=1,
        help='specify the output file or directory to be generated')
    parser.add_argument(
        '--title',
        default='TODO: Insert title here',
        help='specify the title of your note')
    parser.add_argument(
        '--pages',
        type=int,
        default='1',
        help='specify the number of pages (default to 1)')
    parser.add_argument(
        '--index_template',
        default='toc.rst_t',
        help='specify the template file name for TOC page (default to toc.rst_t)')
    parser.add_argument(
        '--page_template',
        default='note.rst_t',
        help='specify the template file name for all pages (default to note.rst_t)')
    return parser.parse_args(args or ["--help"])

def main(args=sys.argv[1:]):
    sys.exit(run(parse_args(args)))

if __name__ == '__main__':
    main()
