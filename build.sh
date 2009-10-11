#!/bin/bash
# $Id$

RST2HTML=./rst2html.py
CSSFILE=./note.css
DEST=./build

# build 先のディレクトリを確保
mkdir -p ${DEST}

# rst2html コンバート
for SOURCE in *.txt ; do
  TARGET="${SOURCE%%.txt}.html"
  if [ "$SOURCE" -nt "$DEST/$TARGET" ] ; then
    echo Processing $SOURCE...
    "$RST2HTML" "$SOURCE" "$DEST/$TARGET"
  fi
done

# css ファイルを build 先ディレクトリへコピー
if [ -f "$CSSFILE" ]; then
  cp -u note.css ${DEST}
fi
