# -*- coding: utf-8 -*-
# $Id$
# Copyright (C) 2011
#
# Permission to copy, use, modify and distribute this software
# is granted provided this copyright notice appears in all copies.
# This software is provided "as is" without express or implied
# warranty, and with no claim as to its suitability for any purpose.
"""%prog [options] name

Example: 
%prog milestone09
%prog --separate=3 gamma95
"""
import sys
import codecs
from optparse import OptionParser
from jinja2 import Template, Environment, FileSystemLoader

def run(options, args):
    env = Environment(
        loader = FileSystemLoader('.'))
    filename = args[0]
    numpage = options.separate

    params = dict(title=options.title,
                  author=options.author,
                  interpreter=options.interpreter,
                  publisher=options.publisher,
                  isbn=options.isbn,
                  notename=filename)
    
    if numpage < 2:
        # Only one page.
        template = env.get_template('toc.rst_t')
        with codecs.open('%s.rst' % filename, 'w', 'utf8', 'ignore') as fout:
            fout.write(template.render(params))
            fout.write('\n')
    else:
        # One cover page and note pages.
        template = env.get_template('toc.rst_t')
        with codecs.open('%s.rst' % filename, 'w', 'utf8', 'ignore') as fout:
            fout.write(template.render(params))
            fout.write('\n')

        template = env.get_template('note.rst_t')
        for i in xrange(1, numpage + 1):
            with codecs.open('%s-note%d.rst' % (filename, i), 'w', 'utf8', 'ignore') as fout:
                fout.write(template.render(params, page=i, totalpages=numpage))
                fout.write('\n')

if __name__ == '__main__':
    parser = OptionParser(__doc__)

    parser.add_option('-t', '--title',
                      default=u'タイトル', 
                      dest='title',)
    parser.add_option('-a', '--author',
                      default=u'著者', 
                      dest='author',)
    parser.add_option('-i', '--interpreter',
                      default=u'訳者', 
                      dest='interpreter',)
    parser.add_option('-p', '--publisher',
                      default=u'出版社', 
                      dest='publisher',)
    parser.add_option('-I', '--isbn',
                      default='ISBN-XXXXX',)
    parser.add_option('-s','--separate',
                      type='int',
                      default=0,
                      dest='separate',)

    options, args = parser.parse_args()
    if len(args) < 1:
        print >>sys.stderr, parser.print_help()
        sys.exit(1)

    run(options, args)
