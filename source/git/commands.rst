======================================================================
コマンド
======================================================================
本節では Git_ のコマンドを、よくあるチートシートの形式で記していく。
私にとって利用価値が高いコマンドの用例を優先して掲載する。
Git はコマンドもオプションも数が多くてとにかく憶えにくい。

.. contents::

共通オプション
======================================================================
ここでいう共通オプションとは、次のコマンド呼び出しの形式における
``[common-options]`` の部分に来るコマンドラインオプションのこととする。

.. code-block:: console

   $ git [common-options] <command> [command-options] ...

``--version``
  Git 自身のバージョンを表示する。ほとんど全ての引数とオプションを無視するようだ。

``--help``
  引数がない場合は、共通オプション一覧、いくつかの常用コマンド、特殊なヘルプの表示方法を出力する。

  引数がある場合は、それに関するヘルプをおそらくブラウザーで表示する。
  この場合は ``git help arg`` と同等の動きをする。

``-C <path>``
  作業ディレクトリーがまるで ``<path>`` であるかのように Git を振る舞わせるオプション。

  リポジトリーを操作するスクリプトを書くときに、いちいち ``cd`` 系コマンドを実行しなくて済む。
  このオプションは明らかに有用なので活用したい。

  * オプション ``--git-dir`` や ``--work-tree`` と組み合わせるときに、
    これらが相対パスの形でディレクトリーを指定する場合には ``-C`` からの相対パスとしてみなされる点に注意。

``--no-pager``
  Git がコンソールに長い出力をするときに、ページャーを使わせないようにするオプション。
  利用例としては、まとまった量のコミットログを出力するようなスクリプトを作成するときに適用を考える。

  * ページャーは定義されていれば環境変数 ``PAGER`` が、
    そうでなければ ``less`` が使われる。

``--git-dir=<path>``
  リポジトリーの管理部分本体、つまりディレクトリー ``.git`` のあるパスを指定する。
  尋常でない場所に ``.git`` があるような場合に用いるのだろう。

``--work-tree=<path>``
  作業コピーのパスを指定する。
  リポジトリーに対して普通でない場所に作業コピーを持つときに用いるのだろう。

高水準コマンド
======================================================================
ヘルプドキュメントによる用途別分類をここで利用させてもらう。

主力コマンド
----------------------------------------------------------------------
Git 利用者の必修コマンドのようなものか。
ヘルプドキュメントによる一覧を見てみると、私が利用したことがないコマンドが多数ある。

まずはメインとされているコマンド群の名称を記す。

* add
* am
* archive
* bisect
* branch
* bundle
* checkout
* cherry-pick
* citool
* clean
* clone
* commit
* describe
* diff
* fetch
* format-patch
* gc
* grep
* gui
* init
* log
* merge
* mv
* notes
* pull
* push
* rebase
* reset
* revert
* rm
* shortlog
* show
* stash
* status
* submodule
* tag
* worktree

呪文表
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
そして常用する「呪文表」を次に示す。よくあるチートシートである。

* ``add [file]``
* ``add .``
* ``add -p <file>``
* ``add -i``
* ``add -u``
* ``am <patch file>``
* ``archive master | tar -x -C /somewhere/else``
* ``archive master | bzip2 > source-tree.tar.bz2``
* ``archive --format zip --output /full/path master``
* ``bisect start``
* ``bisect good $id``
* ``bisect bad $id``
* ``bisect bad/good``
* ``bisect visualize``
* ``bisect reset``
* ``branch [branch-name]``
* ``branch new existing``
* ``branch -d [branch-name]``
* ``branch -D branch_to_delete``
* ``branch -av``
* ``branch -dr <remote/branch>``
* ``branch -r``
* ``branch --track <branch> <remote-branch>``
* ``branch --set-upstream <branch> <remote-branch>``
* ``branch -m branchname new_branchname``
* ``branch --merged``
* ``checkout [branch-name]``
* ``checkout -b <branch>``
* ``checkout --track <remote/branch>``
* ``checkout HEAD <file>``
* ``checkout <branch> <path to new file>``
* ``checkout .``
* ``checkout -b <local branch> <remote>/<remote branch>``
* ``checkout -- <file>``
* ``cherry-pick [--edit] [-n] [-m parent-number] [-s] [-x] <commit>``
* ``clean -n``
* ``clean -f``
* ``clone [url]``
* ``clone existing_dir new_dir``
* ``commit -m "[descriptive message]"``
* ``commit -a``
* ``commit -a -m "My Message"``
* ``commit -v``
* ``commit --amend``
* ``commit --amend <file1> <file2> ...``
* ``commit --amend --reset-author [--no-edit]``
* ``commit <tag>``
* ``diff HEAD``
* ``diff --staged``
* ``diff --cached``
* ``diff --no-prefix > patchfile``
* ``fetch [bookmark]``
* ``fetch <remote> <branch>``
* ``fetch --all --prune``
* ``fetch <remote> -p``
* ``format-patch HEAD^``
* ``format-patch <Revision>^..<Revision>``
* ``gc --prune``
* ``grep "foo()"``
* ``gui blame``
* ``init [project-name]``
* ``log -p``
* ``log -p <file>``
* ``log --pretty=short``
* ``log <file>``
* ``log <dir>``
* ``log --stat``
* ``log --color``
* ``log --graph``
* ``log --decorate``
* ``log --author=foo``
* ``log --after="MMM DD YYYY"``
* ``log --before="MMM DD YYYY"``
* ``log --merge``
* ``log <ref>..<ref>``
* ``log --oneline``
* ``log --format=oneline``
* ``log --grep=message``
* ``log --stat --summary``
* ``log --oneline --graph --all --decorate``
* ``merge [branch]``
* ``merge [bookmark]/[branch]``
* ``merge <branch> --no-commit``
* ``merge <branch> -s ours``
* ``merge -ff-only branchname``
* ``merge --no-ff branchname``
* ``merge --abort``
* ``mv [file-original] [file-renamed]``
* ``pull <remote>``
* ``pull <remote> <branch>``
* ``pull --rebase <remote>``
* ``push [alias] [branch]``
* ``push <remote> --force``
* ``push <remote> --all``
* ``push remote :branch``
* ``push --tags``
* ``push origin/upstream --tags``
* ``push <repo> <start-point>:refs/heads/<branch>``
* ``push origin --delete <branchname>``
* ``push --mirror``
* ``rebase <branch>``
* ``rebase master branch``
* ``rebase -i <base>``
* ``rebase --abort``
* ``rebase --continue``
* ``rebase --skip``
* ``reset [file]``
* ``reset <commit>``
* ``reset --hard``
* ``reset --hard HEAD``
* ``reset --hard <commit>``
* ``reset --hard ORIG_HEAD``
* ``reset --keep <commit>``
* ``reset --soft HEAD^``
* ``revert <commit>``
* ``rm [file]``
* ``rm --cached [file]``
* ``rm dir/ -r``
* ``rm $(git ls-files --deleted)``
* ``show <rev>``
* ``show <rev>:<filename>``
* ``show --name-only``
* ``show <branch> -- <path to file>``
* ``stash pop``
* ``stash list``
* ``stash drop``
* ``stash save <optional-name>``
* ``stash apply``
* ``stash show <stash-name> -p``
* ``stash clear``
* ``status -uno``
* ``submodule add <remote_repository> <path/to/submodule>``
* ``submodule update [--init]``
* ``submodule foreach <command>``
* ``tag <tag-name>``
* ``tag -l``

補助コマンド
----------------------------------------------------------------------
* 操作用

  * config
  * fast-export
  * fast-import
  * filter-branch
  * mergetool
  * pack-refs
  * prune
  * reflog
  * relink
  * remote
  * repack
  * replace

* 問い合わせ用

  * annotate
  * blame
  * cherry
  * count-objects
  * difftool
  * fsck
  * get-tar-commit-id
  * help
  * instaweb
  * merge-tree
  * rerere
  * rev-parse
  * show-branch
  * verify-commit
  * verify-tag
  * whatchanged

呪文表
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ``config -e [--global]``
* ``config --global user.name "[name]"``
* ``config --global user.email "[email address]"``
* ``config --global color.ui auto``
* ``config --list``
* ``reflog --relative-date``
* ``reflog --all``
* ``remote -v``
* ``remote -v update``
* ``remote add <shortname> <url>``
* ``remote add -t master -m master origin <url.git>``
* ``remote show <remote>``
* ``remote prune <remote>``
* ``remote set-url origin new_url``

* ``blame <file>``
* ``blame <file> <rev>``
* ``help <command>``
* ``instaweb --httpd=webrick [--start | --stop | --restart]``
* ``whatchanged <file>``

外部連携コマンド
----------------------------------------------------------------------
ヘルプによると、次のコマンド群が外部連携コマンドとして位置づけられている。
他のバージョン管理システムとのデータ変換という意味と、
他の利用者とのリポジトリーデータの交換という意味があるようだ。

* archimport
* cvsexportcommit
* cvsimport
* cvsserver
* imap-send
* p4
* quiltimport
* request-pull
* send-email
* svn

コマンド名には CVS やら Perforce やら、懐かしいバージョン管理システムの名前が見受けられる。
私個人が自由に管理できた Subversion のリポジトリーはすべて Git に変換済みなので、
これらのコマンドが行うであろう機能は私にとってもはや興味がない。

低水準コマンド
======================================================================
ここから先に記すコマンドは、ドキュメントでは低水準コマンドという括りになっている。
一般利用者にとっては実行頻度が低いものということだ。

操作コマンド
----------------------------------------------------------------------
リポジトリーにあるオブジェクトやインデックスを操作するコマンド群である。

* apply
* checkout-index
* commit-tree
* hash-object
* index-pack
* merge-file
* merge-index
* mktag
* mktree
* pack-objects
* prune-packed
* read-tree
* symbolic-ref
* unpack-objects
* update-index
* update-ref
* write-tree

呪文表
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ``hash-object <file-path>``

問い合わせコマンド
----------------------------------------------------------------------
ヘルプによると、次のコマンド群は問い合わせるのに用いるものとして位置づけられている。
原則的にこれらは作業コピーのファイルを touch しないコマンドということになっているので、
安心して実行してよさそうだ。

* cat-file
* diff-files
* diff-index
* diff-tree
* for-each-ref
* ls-files
* ls-remote
* ls-tree
* merge-base
* name-rev
* pack-redundant
* rev-list
* show-index
* show-ref
* unpack-file
* var
* verify-pack

呪文表
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ``ls-files --other --ignored --exclude-standard``
* ``ls-remote <remote> [HEAD]``

同期コマンド
----------------------------------------------------------------------
ヘルプによると、次のコマンド群は同期コマンドとして位置づけられている。
一般ユーザー用のコマンドと、実装用コマンドに分けてリストされている。
ここではどちらも私の興味がないということで、一気に名前のみを挙げる。

* 一般用

  * daemon
  * fetch-pack
  * http-backend
  * send-pack
  * update-server-info

* 実装用 <end users typically do not use them directly>

  * http-fetch
  * http-push
  * parse-remote
  * receive-pack
  * shell
  * upload-archive
  * upload-pack

内部コマンド
----------------------------------------------------------------------
ヘルプによると、次のコマンド群は内部コマンドとして位置づけられている。

* check-attr
* check-ignore
* check-mailmap
* check-ref-format
* column
* credential
* credential-cache
* credential-store
* fmt-merge-msg
* interpret-trailers
* mailinfo
* mailsplit
* merge-one-file
* patch-id
* sh-i18n
* sh-setup
* stripspace

もっとも <end users typically do not use them directly> とのことなので、
私も当然利用しない。

.. include:: /_include/git-refs.txt
