#!/bin/bash

REPOSITORY_URL=https://github.com/showa-yojyo/notebook.git
SOURCE_DIR=./build/html/
TARGET_DIR=./gh-pages
RSYNC_INCLUDE_FROM=./rsync-include.txt
RSYNC_EXCLUDE_FROM=./rsync-exclude.txt

if [ ! -d "$TARGET_DIR" ]; then
    git clone -b gh-pages --single-branch $REPOSITORY_URL "$TARGET_DIR"
fi

rsync -av --delete \
  --include-from "$RSYNC_INCLUDE_FROM" \
  --exclude-from "$RSYNC_EXCLUDE_FROM" \
  "$SOURCE_DIR" "$TARGET_DIR"

cd "$TARGET_DIR"

SPHINX_VERSION="$(sphinx-build --version | cut -d" " -f2 | tr -d "\r")"
COMMIT_MESSAGE="${1:+ ($1)}"
git add -A
git commit -m "Build 1.5dev (Sphinx: v${SPHINX_VERSION}) $COMMIT_MESSAGE"

NUM=5
echo Most recent $NUM commits:
git --no-pager log --pretty=tformat:'%C(auto)%h %ad%d %s %C(bold blue)[%cn]%C(reset)' --decorate --date=iso HEAD~$NUM..

cd -
