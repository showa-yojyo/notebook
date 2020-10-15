#!/bin/bash
# gh-pages.sh - This script is invoked from the Makefile's gh-pages rule.

TARGET_DIR=./gh-pages

function main
{
    function _ensure_local_repository
    {
        local remote_repository=https://github.com/showa-yojyo/notebook.git

        if [ ! -d "$TARGET_DIR" ]; then
            git clone -b gh-pages --single-branch $remote_repository "$TARGET_DIR"
        fi
    }

    function _execute_rsync
    {
        local source_dir=./build/html/
        local rsync_include_from=./rsync-include.txt
        local rsync_exclude_from=./rsync-exclude.txt

        rsync -av --delete \
          --include-from "$rsync_include_from" \
          --exclude-from "$rsync_exclude_from" \
          "$source_dir" "$TARGET_DIR"
    }

    function _commit_worktree
    {
        # tr -d drops trailing CR and/or LF
        local sphinx_version="$(sphinx-build --version | cut -d" " -f2 | tr -d [:space:])"
        local log_format="%C(auto)%h %ad%d %s %C(bold blue)[%cn]%C(reset)"

        git -C "$TARGET_DIR" add -A
        git -C "$TARGET_DIR" commit \
          -m "Build 1.5dev (Sphinx: v${sphinx_version})"
        git -C "$TARGET_DIR" --no-pager log --pretty=tformat:"$log_format" \
          --decorate --date=iso HEAD~..
    }

    _ensure_local_repository
    _execute_rsync
    _commit_worktree
}

main
