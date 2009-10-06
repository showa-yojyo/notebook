#!/bin/bash
# $Id$

RST2HTML=./rst2html.py

for SOURCE in *.txt ; do
  TARGET="${SOURCE%%.txt}.html"
  if [ "$SOURCE" -nt "$TARGET" ] ; then
    echo Processing $SOURCE...
    "$RST2HTML" "$SOURCE" "$TARGET"
  fi
done
