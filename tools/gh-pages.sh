#!/bin/bash

SOURCE_DIR=./build/html/
TARGET_DIR=../notebook-gh-pages

rsync -av \
  --delete \
  --exclude='.git/' \
  --exclude='.nojekyll' \
  --exclude='.buildinfo' \
  --exclude='_sources/*' \
  --exclude='_static/*' \
  --exclude='search.html' \
  --exclude='objects.inv' \
  --exclude='searchindex.js' \
  --include='_static/*.css' \
  --include='_static/twitter-button.js' \
  --include='_static/logos.png' \
  ${SOURCE_DIR}/ ${TARGET_DIR}
