======================================================================
コマンド
======================================================================

本節では Git_ のコマンドを、よくあるチートシートの形式で記していく。私にとって利
用価値が高いコマンドの用例を優先して掲載する。Git はコマンドもオプションも数が多
くてとにかく憶えにくい。

.. contents::

記法規約
======================================================================

:doc:`./terminology` を参照。

共通オプション
======================================================================

ここでいう共通オプションとは、次のコマンド呼び出しの形式における
``[common-options]`` の部分に来るコマンドラインオプションのこととする。自分が使
う可能性の高いものを記す。

.. code:: console

   bash$ git [common-options] <command> [command-options] <args>

.. option:: --version

   Git 自身のバージョンを表示する。ほとんど全ての引数とオプションを無視するよう
   だ。

.. option:: --help

   引数がない場合は、共通オプション一覧、いくつかの常用コマンド、特殊なヘルプの
   表示方法を出力する。引数がある場合は、それに関するヘルプをおそらくブラウザー
   で表示する。この場合は ``git help arg`` と同等の動きをする。

.. option:: -C <path>

   作業ディレクトリーがまるで ``<path>`` であるかのように Git を振る舞わせるオプ
   ション。

   リポジトリーを操作するスクリプトを書くときに、いちいち :command:`cd` 系コマン
   ドを実行しなくて済む。このオプションは明らかに有用なので活用したい。

   オプション :option:`--git-dir` や :option:`--work-tree` と組み合わせるとき
   に、これらが相対パスの形でディレクトリーを指定する場合には :option:`-C` か
   らの相対パスとしてみなされる点に注意。

.. option:: --no-pager

   Git がコンソールに長い出力をするときに、ページャーを使わせないようにするオプ
   ション。利用例としては、まとまった量のコミットログを出力するようなスクリプト
   を作成するときに適用を考える。

   ページャーは定義されていれば環境変数 ``PAGER`` が、そうでなければ
   :command:`less` が使われる。

.. option:: --git-dir=<path>

   リポジトリーの管理部分本体、つまりディレクトリー :file:`.git` のあるパスを指
   定する。尋常でない場所に :file:`.git` があるような場合に用いるのだろう。

.. option:: --work-tree=<path>

   作業コピーのパスを指定する。リポジトリーに対して普通でない場所に作業コピーを
   持つときに用いるのだろう。

高水準コマンド
======================================================================

ヘルプドキュメントによる用途別分類をここで利用させてもらう。

主力コマンド
----------------------------------------------------------------------

Git 利用者の必修コマンドのようなものか。ヘルプドキュメントによる一覧を見てみる
と、私が利用したことがないコマンドが多数ある。

まずはメインとされているコマンド群の名称を記す。このテキストはコマンド ``git
help -a`` の出力による：

  .. code:: text

     add                  Add file contents to the index
     am                   Apply a series of patches from a mailbox
     archive              Create an archive of files from a named tree
     bisect               Use binary search to find the commit that introduced a bug
     branch               List, create, or delete branches
     bundle               Move objects and refs by archive
     checkout             Switch branches or restore working tree files
     cherry-pick          Apply the changes introduced by some existing commits
     citool               Graphical alternative to git-commit
     clean                Remove untracked files from the working tree
     clone                Clone a repository into a new directory
     commit               Record changes to the repository
     describe             Give an object a human readable name based on an available ref
     diff                 Show changes between commits, commit and working tree, etc
     fetch                Download objects and refs from another repository
     format-patch         Prepare patches for e-mail submission
     gc                   Cleanup unnecessary files and optimize the local repository
     gitk                 The Git repository browser
     grep                 Print lines matching a pattern
     gui                  A portable graphical interface to Git
     init                 Create an empty Git repository or reinitialize an existing one
     log                  Show commit logs
     maintenance          Run tasks to optimize Git repository data
     merge                Join two or more development histories together
     mv                   Move or rename a file, a directory, or a symlink
     notes                Add or inspect object notes
     pull                 Fetch from and integrate with another repository or a local branch
     push                 Update remote refs along with associated objects
     range-diff           Compare two commit ranges (e.g. two versions of a branch)
     rebase               Reapply commits on top of another base tip
     reset                Reset current HEAD to the specified state
     restore              Restore working tree files
     revert               Revert some existing commits
     rm                   Remove files from the working tree and from the index
     shortlog             Summarize 'git log' output
     show                 Show various types of objects
     sparse-checkout      Initialize and modify the sparse-checkout
     stash                Stash the changes in a dirty working directory away
     status               Show the working tree status
     submodule            Initialize, update or inspect submodules
     switch               Switch branches
     tag                  Create, list, delete or verify a tag object signed with GPG
     worktree             Manage multiple working trees

そして私が常用するものと利用したいもののコマンドライン群、「呪文表」を次に示す。
よくあるチートシートである。

以下、コマンドライン内の ``git [common-options]`` の部分は省略する。Git 特有の符
牒ではなく、実際にありがちな名前を例に使うかもしれない。例えば ``<tree-ish>`` で
はなく ``master`` とか ``HEAD`` とかを敢えて使う。

呪文表 ``add``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド ``add`` はインデックスにファイルおよびその変更を追加するのに用いる。

``add [<pathspec>...]``
  指定したファイルだけをインデックスに追加する。

  引数なしの場合に何が起こるのかは設定によるが、基本的には次の呪文と同じ効果だ。

``add .``
  現在ディレクトリー以下のファイルをインデックスに再帰的に追加する。

``add -p <pathspec>``
  指定したファイルの内部から追加部分を対話的に指示し、インデックスに追加する。

``add -i``
  コンソールで対話的にファイルをインデックス追加処理する。

``add -u [<pathspec>...]``
  作業ディレクトリー配下にあるファイルのうち、既にバージョン管理中のもののみをコ
  マンドの対象とする。

  .. csv-table::
     :delim: @
     :header-rows: 1
     :widths: auto

     状態 @ インデックス
     新規ファイル @ インデックスに影響しない
     変更ファイル @ インデックスに更新対象として追加
     削除ファイル @ インデックスに削除対象として追加

  デフォルトの ``-a`` オプションとの違いに注意。

呪文表 ``archive``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド ``archive`` は作業コピーのファイル全部から圧縮ファイルを作成する
のに利用できる。

``archive --format=tar.gz --prefix=prjname/ master > prjname-master.tar.gz``
  ツリー ``master`` から tar.gz 形式の圧縮ファイルを作る。

``archive master | bzip2 > source-tree.tar.bz2``
  ツリー ``master`` から tar.bz2 形式の圧縮ファイルを作る。

``archive --format=zip --prefix=projname/ master > projname.zip``
  ツリー ``master`` から zip 形式の圧縮ファイルを作る。

呪文表 ``bisect``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド ``bisect`` は異色のコマンドで、コミットを二分探索法によって検索
するものだ。

``bisect help``
  当コマンドの利用法の概要をコンソールに出力する。詳細を見たい場合はやはり
  ``help bisect`` である。

``bisect start HEAD v1.2``
  二分探索セッションを開始する。これは ``HEAD`` で何かマズいことになっているが、
  確か ``v1.2`` 時点では正常だった、の例。

``bisect good [<rev>]``
  このリビジョンは正常だという印をセッション情報に付ける。

``bisect bad [<rev>]``
  このリビジョンは何かマズイという印をセッション情報に付ける。

``bisect visualize``
  現時点で残っている疑わしいものを :command:`gitk` で表示する。最近はこのビュー
  ワーをインストールしていないが。

  ``bisect view`` とタイプしても同じ。短いほうが良い。

``bisect reset``
  セッションを終了して、作業コピーの状態を ``bisect start`` 直前のものに戻す。

呪文表 ``branch``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド ``branch`` はブランチを管理するのに用いる。

``branch <new> [<existing>]``
  新規ブランチ ``<new>`` を既存ブランチ ``<existing>`` から作成する。既存ブラン
  チの指定を省略すると、現在ブランチから作成する。

``branch -r``
  リモート追跡ブランチしかを一覧に示さない。

``branch -a``
  ローカルとリモート追跡の両方のブランチを一覧する。

  オプション ``-v`` でより詳しく。

``branch --merged``
  現在ブランチに対して完全にマージ済みのブランチ全てを一覧に示す。

``branch --track <branchname> [<start-point>]``
  リモート追跡ブランチ ``<branchname>`` を作成する。意味としてはリモートにある
  ``start-point`` からブランチするイメージか。

``branch --set-upstream <branch> <start-point>``
  既存のブランチ ``<branch>`` を ``<start-point>`` のリモート追跡ブランチにす
  る。

``branch -m [<oldbranch>] <newbranch>``
  ブランチ ``<oldbranch>`` の名前を ``<newbranch>`` に変更する。引数
  ``oldbranch`` の指定を省略すると、現在ブランチを改名する。

  オプション ``-M`` は ``-m --force`` と同じ。

``branch -d <branchname>``
  ブランチ ``<branchname>`` を削除する。ただし、別のブランチにマージ済みであると
  失敗してくれる。

  * ``-D`` is ``-d --force``.
  * リモートブランチを削除するのはまったく別のコマンドを用いる。``push`` 参照。

``branch -dr <remote/branchname>``
  リモート追跡ブランチを削除する。マージ済みが条件。

  影響を受けるのはローカルの状態だけ。

呪文表 ``checkout``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド ``checkout`` にはブランチを切り替える用法と、作業コピーのファイルを復元
する用法の両方があることに注意したい。

``checkout <branch>``
  現在ブランチを既存のブランチ ``<branch>`` に切り替える。cf. ``switch
  <branch>``.

``checkout -b <branch> [<start-point>]``
  ブランチ ``<branch>`` を作成して、同時に現在ブランチを切り替える。明示的に
  ``<start-point>`` が指定されていれば、そこからブランチする。cf. ``switch -c
  <branch>``.

``checkout -b <branch> <remote>/<branch>``
  リモートブランチをローカルブランチとして作成する。

``checkout --track <remote>/<branch>``
  リモートブランチからリモート追跡ブランチを作成する。

``checkout HEAD <file>``, ``checkout -- <file>``
  ファイル ``<file>`` のローカルでの変更を破棄する。cf. ``restore``.

``checkout .``
  現在いるディレクトリー以下のローカルでの変更をすべて破棄する。cf. ``restore``.

``checkout <branch> <file>``
  別のブランチ ``<branch>`` にあるファイル ``<file>`` を現在ブランチへ持ってく
  る。

呪文表 ``clean``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド ``clean`` の役割は、バージョン管理されていないファイルを消去する
ことである。

``clean -n``
  仮に ``clean`` を実行すると、何が起こるのかをプレビューする。

  オプション ``-n`` は他のコマンドでも dry run の意味でサポートされている場合が
  ある。まとめたほうがよいかも。

``clean -f``
  Git の構成に依らず、とにかく削除する。

呪文表 ``clone``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド ``clone`` はリポジトリーを新規ディレクトリーに複製する。これによ
り作業コピーができる。

``clone <repository> [<directory>]``
  リポジトリー ``<repository>`` の作業コピーを ``<directory>`` に作成する。

  ``<repository>`` には普通なんちゃら ``.git`` のような文字列が来る。たまにロー
  カルにある作業コピーのパスを指示するような場合もある。

呪文表 ``commit``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド ``commit`` はリポジトリーの変更を確定するために用いる。そしてコミットを
修正することもできる。

``commit -a``
  自動的に変更ファイルと削除ファイルをステージに置いてコミットする。

``commit -m <msg>``
  コミットログメッセージを ``<msg>`` としてコミットする。もっとも普通のコミット
  コマンドの形式。ログメッセージは普通は引用符で囲む。

``commit -v``
  リポジトリーの変更情報を表示しながらコミットする。

``commit --amend``
  直前のコミットを修正する。

``commit --amend <file> ...``
  直前のコミットに変更ファイルを追加してコミットをやり直す。

``commit --amend --reset-author [--no-edit]``
  直前のコミットの作業者情報を上書きする。

  * タイムスタンプを更新することに注意。
  * オプション ``--no-edit`` を併用すれば、ログメッセージを再利用できる。

.. todo::

   * タイムスタンプが 2 種類あることについて言及する。
   * タイムスタンプを任意のタイミングに指定する方法について言及する。

呪文表 ``diff``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド ``diff`` は相異なるコミット間の差分や、特定コミットと作業コピーとの差分
を表示する。ファイル単位で差分を確認することができるが、ここに挙げる例は対象ファ
イル全部になる。

``diff HEAD``
  指定ファイル群について、作業コピーとレポジトリーの最新リビジョン ``HEAD`` との
  差分を表示する。

``diff --cached``
  作業コピーとステージとの差分を表示する。

  別名 ``--staged`` がある。

``diff --no-index <file1> <file2>``
  ファイルの差分をバージョン管理の文脈と無関係に表示する。単に GNU
  :command:`diff` を利用するのが素直だ。

呪文表 ``fetch``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド ``fetch`` はよそにあるリポジトリーからデータをダウンロードする。

``fetch [<bookmark>]``
  リポジトリブックマークからすべての履歴をダウンロードする。

``fetch <repository> [<branch>]``
  リモートリポジトリー ``repository`` からブランチ ``branch`` をダウンロードす
  る。

``fetch <remote> -p``
  リモート ``<remote>`` に関してデータをダウンロードし、削除済みリモートブランチ
  があれば、それに対応するリモート追跡ブランチをローカルにおいて削除する。

``fetch --all --prune``
  すべてのリモートリポジトリーからダウンロードする。なおかつ、削除済みリモートブ
  ランチがあれば、それに対応するリモート追跡ブランチをローカルにおいて削除する。

呪文表 ``gc``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド ``gc`` は不要ファイルを削除してローカルリポジトリーの最適化をする。気分
転換の意味で実行することが多い。

``gc [--prune[=<date>]]``
  リポジトリーのゴミ掃除を行う。

  オプション ``--prune`` は未参照オブジェクトを削除するかどうかのフラグだ。これ
  は既定で on である。

呪文表 ``grep``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

オプションにもよるが、リポジトリー管理対象ファイル限定版 :command:`grep` と表現
できる。それ以外は GNU :command:`grep` と同じように利用できる。

と言うわけで、ここにはコマンドラインを記さない。

呪文表 ``init``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド ``init`` はリポジトリーを（再）作成する。

``init [<directory>]``
  ディレクトリー ``<directory>`` を Git リポジトリーとして初期化する。

``init --bare [<directory>]``
  ディレクトリー ``<directory>`` に生リポジトリーを作成する。管理ディレクトリー
  である :file:`.git` の初期状態を生成するものだ。

呪文表 ``log``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド ``log`` はコミットログを出力する。構文はたいへん単純だが、オプションが
多いので実は憶えにくい。

``log``
  引数オプション一切なしでは全ログを出力することになる。新しい順。

``log --decorate``
  関係するブランチとタグがあれば、そのコミットのログにはそれらの名前を一緒に出力
  する。

``log <ref>..<ref>``
  指定リビジョン範囲におけるコミットに限定してログを出力する。

``log [--] <path>...``
  指定したファイルやディレクトリーに関係するコミットに限定してログを出力する。

``log -<number>``
  指定したコミット数だけログを出力する。

  別名 ``-n <number>`` および ``--max-count <number>`` がある。

``log --after="MMM DD YYYY"``
  指定期日よりも新しいコミットに限定してログを出力する。

  別名 ``--since`` がある。

``log --before="MMM DD YYYY"``
  指定期日よりも古いコミットに限定してログを出力する。

  別名 ``--until`` がある。

``log --author=<pattern>``
  執筆者がパターン ``pattern`` にマッチするコミットに限定してログを出力する。

``log --grep=<pattern>``
  ログメッセージがパターンにマッチするコミットに限定してログを出力する。

``log --merge``
  マージで衝突があったものに限定してログを出力する。

``log --pretty=short``
  短いフォーマットでログを出力する。

``log --format=oneline``
  コミット当たり一行でログを出力する。先頭に SHA-1 付き。

``log --oneline``
  コミット当たり一行でログを出力する。

``log --oneline --graph --all --decorate``
  色んな物をログとして出力する。

``log --graph``
  アスキーアートによるコミットグラフをメッセージの左に添える。

``log -p``
  変更内容を表示する。

``log -p <file>``
  ファイル ``<file>`` が関係するコミットに限定して、変更内容を込めてログを出力す
  る。

``log --stat``
  差分に関する統計を添えてログを出力する。

``log --summary``
  ファイルの作成、移動、削除に関する概要を添えてログを出力する。

``log --color``
  差分に色を付けてログを出力する。オプション単体では意味がないようだ。

呪文表 ``merge``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド ``merge`` は現在ブランチに別のブランチのコミット履歴を取り込む。

``merge <branch>``
  ブランチ ``<branch>`` のコミット履歴を現在ブランチに統合する。

``merge --no-commit <branch>``
  ブランチ ``<branch>`` を現在ブランチにマージするが、新しいコミットを自動的に作
  らない。

``merge -s ours <branch>``
  ブランチ ``<branch>`` を現在ブランチにマージするが、何か衝突がある場合はこちら
  側の変更を採用する。

``merge --no-ff <branch>``
  ブランチ ``<branch>`` を現在ブランチにマージするが、それが fast-forward で解決
  してもマージコミットを生成する。

  当ノートリポジトリーの通常マージ呪文とする。ログメッセージは Git の生成する既
  定値でいいので、さらにオプション ``--no-edit`` を加える。

``merge -ff-only <branch>``
  次のような場合はマージしないで異常終了とする。

  * カレントの ``HEAD`` が既に最新である
  * マージが fast-forward で解決する

``merge --abort``
  現在のマージが衝突したら処理を中止して、状態をマージ直前に復元することを試み
  る。

呪文表 ``mv``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド ``mv`` はファイルを移動する、もしくは名前を変える。ファイルはディレクト
リーとシンボリックリンクを含む。

``mv <source> <destination>``
  ファイル ``<source>`` を ``<destination>`` に移動するか、名前を変える。

  引数 ``<source>`` が複数ファイルの場合は、引数 ``<destination>`` は既存のディ
  レクトリーであるものとする。

呪文表 ``pull``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド ``pull`` は ``fetch`` と ``merge`` を同時に行うようなものだ。

``pull [<repository>]``
  現在ブランチのリモートリポジトリー ``<repository>`` のコピーをダウンロードし
  て、それを直ちにローカルの ``HEAD`` にマージする。

``pull [<repository> [<refspec> ...]]``
  リモートリポジトリー ``<repository>`` のブランチ ``<refspec>`` に対して、その
  コピーをダウンロードしてローカルの ``HEAD`` にマージする。

  ところで ``<repository>`` や ``<refspec>`` の既定値は、現在ブランチの構成に依
  存する。

``pull --rebase <repository>``
  これは ``fetch`` と ``rebase`` を同時に行うようなものだ。上手い人向けのコマン
  ド。

呪文表 ``push``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド ``push`` はローカルのコミットをリモートにアップロードする。

``push [<repository> [<refspec> ...]]``
  ローカルの ``<refspec>`` をリモートリポジトリー ``<repository>`` にアップロー
  ドする。これらの引数の既定値は現在ブランチの構成に従う。

``push --all [<repository>]``
  ローカルのすべてのブランチをリモートリポジトリー ``repository`` にアップロード
  する。言い換えると ``refs/heads/`` 配下の refs をリモートリポジトリーにアップ
  ロードする。

``push --mirror``
  ローカルのすべての状態とリモートリポジトリーの状態が同一となるようにアップロー
  ドする。言い換えると ``refs/`` 配下をリモートリポジトリーにコピーする。

``push --tags``
  ``refs/tags`` 配下にあるすべての refs をアップロードする。

``push -n``
  コマンド実行時のプレビューができる。別名 ``--dry-run`` がある。

``push --force <repository>``
  マージが fast-forward にならない ``push`` であっても、強引にアップロードする。

``push <repository> :<pattern>``
  リモートリポジトリー ``<repository>`` にパターン ``<pattern>`` にマッチする
  ref があれば、それを削除する。

``push -d origin <branch>``
  リモートリポジトリー ``origin`` のブランチ ``<branch>`` を削除する。

``push <repository> <start-point>:refs/heads/<branch>``
  リモートリポジトリー ``<repository>`` にブランチ ``<branch>`` を作成する。ブラ
  ンチの基点はリモートの ``<start-point>`` とする。

呪文表 ``rebase``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド ``rebase`` は私にとってはコミット履歴の修正ツールだ。

``rebase [<upstream> [<branch>]]``
  ブランチ ``<upstream>`` をブランチ ``<branch>`` に ``rebase`` する。

``rebase -i [<upstream> [<branch>]]``
  テキストエディター上でコミット履歴の操作を行う。

  テキストエディター上にはコミット履歴が各行にリストされている。そこで各行の先頭
  にコミット操作命令をタイプしてエディターを終了すると、いい感じにコミット履歴が
  改竄される。

  例えば次のことができる：

  * コミットログを修正する
  * 複数のコミットの順序を交換する
  * 複数のコミットを合併する
  * コミットをキャンセルする

  ``rebase -i HEAD~5``
    直近 5 コミットの履歴の改竄を開始する。

``rebase --continue``
  手動による衝突を解消してインデックスが望み通りの状態になったときに、``rebase``
  処理の対象を次のコミットへ進ませる。

``rebase --abort``
  手動による衝突解消が上手くいかなかったときに、``rebase`` 開始直前の状態に戻
  す。

``rebase --skip``
  衝突したままだが、とにかく次のコミットへ ``rebase`` 処理を進ませる。

呪文表 ``reset``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド ``reset`` は現在の ``HEAD`` を指定した状態へ戻すのに用いる。用法には
ファイルに作用するものと、コミットに作用するものがある。

``reset <paths>...``
  インデックスでファイル ``<paths>`` に関する項目をリセットする。

  ヘルプでは ``add <paths>...`` の逆操作だと表現している。

``reset <commit>``
  現在ブランチの ``HEAD`` をコミット ``<commit>`` にリセットする。インデックスの
  状態もそれに応じてリセットする

``reset --soft HEAD^``
  現在ブランチの状態を直前のコミット直後の状態にリセットする。ローカルでの作業は
  インデックス外に作業コピーに残る。

``reset --hard``
  衝突したパッチを破棄する。

``reset --hard <commit>``
  現在ブランチの ``HEAD`` をコミット ``<commit>`` 直後の時点にリセットする。それ
  以降になされた作業コピーにおけるファイル変更は破棄される。

``reset --hard HEAD``
  現在ブランチの状態を直前のコミット直後の状態にリセットする。コミット以後のロー
  カルでの作業があれば、それは破棄される。

``reset --hard ORIG_HEAD``
  マージが成功したコミットのうち最新のものをアンドゥする。例によってそれ以降の作
  業コピーでのファイル変更は破棄される。

``reset --keep <commit>``
  現在ブランチの ``HEAD`` をコミット ``<commit>`` 直後の時点にリセットする。それ
  以降になされた作業コピーにおいてファイル変更があれば、リセットを中止する。

呪文表 ``restore``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド ``restore`` は作業コピー内の指定ファイルを復元するのに用いる。内容は復
元源のものを使用する。指定ファイルが追跡されている状態で、復元源に対応物が存在し
ない場合、作業コピーから削除される。``git status`` の説明文にチラつくコマンド
だ。

``restore <pathspec>``
  作業コピー内 ``<pathspec>`` をインデックスのそれと同等の内容に復元する。
  ``<pathspec>`` が変更済みファイルだったり、ディレクトリーだったり、作業コピー
  だけで削除したファイルだったりする場合に有効だ。

``restore .``
  上の呪文の系で、現在ディレクトリーの状態をインデックスから復元する。

``restore --staged <pathspec>``
  ``HEAD`` の ``<pathspec>`` 内容と一致するようにインデックス内の ``<pathspec>``
  を復元する。コマンド ``git reset <pathspec>`` と同じことだ。

``restore --source=HEAD --staged --worktree <pathspec>``
  インデックスと作業コピーの両方を復元する。コマンド ``git checkout <pathspec>``
  と同じことだ。

呪文表 ``revert``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド ``revert`` は既存のコミットを無効にするのに用いる。

``revert <commit>``
  コミット ``<comit>`` をなかったことにする。方法はそのコミットの内容を打ち消す
  ような新しいコミットを生み出すことによる。

オプション ``-n`` または ``--no-commit`` は新しいコミットを生じない。

呪文表 ``rm``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド ``rm`` はリポジトリーからファイルを削除する。

``rm [--] <file>...``
  ファイル ``<file>`` を削除する。

``rm -n``
  コマンド実行時のプレビューができる。

  別名 ``--dry-run`` がある。

``rm -r [--] <directory>``
  ディレクトリー ``<directory>`` 以下にあるすべてのファイルを削除する。

``rm --cached [--] <file>``
  ファイル ``<file>`` をインデックスからのみ削除する。

呪文表 ``show``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド ``show`` はあらゆる Git オブジェクトを表示する。

``show <commit>``
  コミット ``<commit>`` との現在の差分を表示する。

``show <commit>:<file>``
  コミット ``<commit>`` でのファイル ``<file>`` の内容を表示する。

``show --name-only``
  変更ファイルの名前だけを表示する。差分は表示しない。

``show <branch> -- <file>``
  ブランチ ``<branch>`` でのファイル ``<file>`` の内容を表示する。

呪文表 ``stash``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド ``stash`` は作業コピーでのファイル変更を一時的に退避するのに用いる。ス
タックのイメージだと思う。

``stash list``
  退避領域の内容を一覧で示す。

``stash show <stash> -p``
  退避領域の内容物を表示する。差分形式で表示できる。

``stash drop``
  直近に一時保存された変更セットを破棄する。

``stash pop``
  直近に一時保存されたファイルを作業コピーへ復元する。

``stash apply``
  直近に一時保存されたファイルを作業コピーへ復元する。ただし保存データはまだ退避
  領域にある。

``stash save <message>``
  現在の作業コピーでの変更ファイルを退避する。この退避には名前が付く。

``stash clear``
  退避領域を完全に消去する。退避内容は失われる。

呪文表 ``status``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド ``status`` は作業コピーの状態を表示するのに用いる。出力結果の読み方を別
途習得する必要がある。

``status``
  引数なしでも色々と情報が得られる。

``status -uno``
  管理外のファイルの情報は要らない。つまり ``Untracked files:`` のセクションを表
  示させない。

呪文表 ``switch``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド ``switch`` は作業ブランチを切り替えるのに用いる。

``switch main``
  作業ブランチを既存ブランチ ``main`` に切り替える。
``switch -``
  作業ブランチをその直前の作業ブランチに切り替える。UNIX コマンド ``cd -`` のア
  ナロジーだ。
``switch -c <new-branch>``
  新規ブランチ ``<new-branch>`` を現在ブランチから開始し、さらに作業ブランチを切
  り替える。

コマンド ``switch`` の切り替え先と衝突するような変更ファイルが作業ブランチに存在
する場合、専用フラグを指定しない限り処理は失敗して、作業ブランチは変わらない。

呪文表 ``tag``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド ``tag`` はタグを管理するのに用いる。

``tag <tagname> [<commit>|<object>]``
  コミットや何かにタグを付ける。

``tag -d <tagname>``
  名前を指定してタグを削除する。

``tag -l [<pattern>]``
  パターンにマッチするタグをリストする。

補助コマンド
----------------------------------------------------------------------

ヘルプドキュメントは補助コマンド群を操作目的のものと問い合わせ目的のものに分けて
紹介している。

次のコマンド群が操作用とされている：

  .. code:: text

     config               Get and set repository or global options
     fast-export          Git data exporter
     fast-import          Backend for fast Git data importers
     filter-branch        Rewrite branches
     mergetool            Run merge conflict resolution tools to resolve merge conflicts
     pack-refs            Pack heads and tags for efficient repository access
     prune                Prune all unreachable objects from the object database
     reflog               Manage reflog information
     remote               Manage set of tracked repositories
     repack               Pack unpacked objects in a repository
     replace              Create, list, delete refs to replace objects

そして次のコマンド群が問い合わせ用とされている：

  .. code:: text

     annotate             Annotate file lines with commit information
     blame                Show what revision and author last modified each line of a file
     bugreport            Collect information for user to file a bug report
     count-objects        Count unpacked number of objects and their disk consumption
     difftool             Show changes using common diff tools
     fsck                 Verifies the connectivity and validity of the objects in the database
     gitweb               Git web interface (web frontend to Git repositories)
     help                 Display help information about Git
     instaweb             Instantly browse your working repository in gitweb
     merge-tree           Show three-way merge without touching index
     rerere               Reuse recorded resolution of conflicted merges
     show-branch          Show branches and their commits
     verify-commit        Check the GPG signature of commits
     verify-tag           Check the GPG signature of tags
     whatchanged          Show logs with difference each commit introduces

呪文表 ``config``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド ``config`` は各種構成オプションを設定するのに用いる。ユーザー固有の設
定、リポジトリー固有の設定、グローバル設定すべてをこれでまかなう。

``config --global user.name <name>``
  コミットログに含まれる著者の名前を設定する。

``config --global user.email <address>``
  コミットログに含まれるメールアドレスを設定する。

``config --global color.ui auto``
  コマンドラインの出力を見やすくする色を設定する。

``config --list``
  すべてのオプションを表示する。何かテキトーな順番で表示されるので、ソートにパイ
  プしたい。

``config -e [--global]``
  テキストエディターでファイル :file:`.git/config` や :file:`~/.gitconfig` を編
  集する。

呪文表 ``reflog``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド ``reflog`` は Git 操作自体の履歴情報を管理するのに用いる。履歴の改竄作
業のヒントになる。

``reflog [show] --relative-date``
  番号の代わりに現在からの時間差を表示する。例えば ``HEAD@{7}`` などではなく
  ``HEAD@{8 days ago}`` などのような表示になる。

``reflog [show] --all``
  すべての refs を表示する。

呪文表 ``remote``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド ``remote`` はリモートリポジトリーおよびそれに関係のあるブランチの管理を
する。

``remote -v``
  饒舌オプション。

``remote add <name> <url>``
  リモートリポジトリー ``<url>`` を追加して、ここでは ``<name>`` と呼ぶ。

``remote add -t master -m master origin <url>``
  URL が ``<url>`` にあるリモートリポジトリーを追加する。ブランチ ``master`` の
  追跡ブランチを ``origin`` という名前で追加する。

``remote get-url origin``
  リモートリポジトリー ``origin`` の URL を得る。

``remote set-url origin <newurl>``
  ``origin`` のリモートリポジトリーの URL が ``<newurl>`` に変更されたので、ロー
  カル側で管理している URL 情報を更新する。

``remote show <repository>``
  リモートリポジトリー ``<repository>`` の情報を表示する。

``remote prune <repository>``
  リモートリポジトリー ``<repository>`` 側では既に存在しないブランチに対応するリ
  モート追跡ブランチを削除する。

``remote -v update``
  リモートリポジトリーから更新データをダウンロードする。

呪文表 ``blame``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド ``blame`` はあるファイルの各行について、リビジョンと著者を表示するとい
うものだ。変なソースコードだなと思ったらこれを使うのもよいだろう。

``blame [<rev>] <file>``
  リビジョン ``<rev>`` 時点でのファイル ``<file>`` の各行の著者を表示する。

呪文表 ``help``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド ``help`` は当然ながらヘルプ機能を供するものだ。

``help [-w] [<command>]``
  コマンド ``<command>`` のヘルプドキュメントをブラウザーで開く。

``help -a``
  一度は試すことを勧める。

``help -g``
  一度は試すことを勧める。

呪文表 ``whatchanged``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド ``whatchanged`` は ``log`` に似ているが、よくわからない。

``whatchanged <file>``
  ファイル ``<file>`` のコミットログと、何かの変更を表示する。

外部連携コマンド
----------------------------------------------------------------------

ヘルプによると、次のコマンド群が外部連携コマンドとして位置づけられている。他の
バージョン管理システムとのデータ変換という意味と、他の利用者とのリポジトリーデー
タの交換という意味があるようだ。

  .. code:: text

     archimport           Import a GNU Arch repository into Git
     cvsexportcommit      Export a single commit to a CVS checkout
     cvsimport            Salvage your data out of another SCM people love to hate
     cvsserver            A CVS server emulator for Git
     imap-send            Send a collection of patches from stdin to an IMAP folder
     p4                   Import from and submit to Perforce repositories
     quiltimport          Applies a quilt patchset onto the current branch
     request-pull         Generates a summary of pending changes
     send-email           Send a collection of patches as emails
     svn                  Bidirectional operation between a Subversion repository and Git

コマンド名には CVS やら Perforce やら、懐かしいバージョン管理システムの名前が見
受けられる。私個人が自由に管理できた Subversion のリポジトリーはすべて Git に変
換済みなので、これらのコマンドが行うであろう機能は私にとってもはや興味がない。

低水準コマンド
======================================================================

ここから先に記すコマンドは、ドキュメントでは低水準コマンドという括りになってい
る。一般利用者にとっては実行頻度が低いものということだ。

操作コマンド
----------------------------------------------------------------------

リポジトリーにあるオブジェクトやインデックスを操作するコマンド群である。

  .. code:: text

     apply                Apply a patch to files and/or to the index
     checkout-index       Copy files from the index to the working tree
     commit-graph         Write and verify Git commit-graph files
     commit-tree          Create a new commit object
     hash-object          Compute object ID and optionally creates a blob from a file
     index-pack           Build pack index file for an existing packed archive
     merge-file           Run a three-way file merge
     merge-index          Run a merge for files needing merging
     mktag                Creates a tag object with extra validation
     mktree               Build a tree-object from ls-tree formatted text
     multi-pack-index     Write and verify multi-pack-indexes
     pack-objects         Create a packed archive of objects
     prune-packed         Remove extra objects that are already in pack files
     read-tree            Reads tree information into the index
     symbolic-ref         Read, modify and delete symbolic refs
     unpack-objects       Unpack objects from a packed archive
     update-index         Register file contents in the working tree to the index
     update-ref           Update the object name stored in a ref safely
     write-tree           Create a tree object from the current index

呪文表 ``hash-object``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド ``hash-object`` はファイルのオブジェクト ID を計算する。

``hash-object <file>``
  ファイル ``<file>`` のオブジェクト ID を計算して SHA1 値として出力する。

問い合わせコマンド
----------------------------------------------------------------------

ヘルプによると、次のコマンド群は問い合わせるのに用いるものとして位置づけられてい
る。原則的にこれらは作業コピーのファイルを :command:`touch` しないコマンドという
ことになっているので、安心して実行してよさそうだ。

  .. code:: text

     cat-file             Provide content or type and size information for repository objects
     cherry               Find commits yet to be applied to upstream
     diff-files           Compares files in the working tree and the index
     diff-index           Compare a tree to the working tree or index
     diff-tree            Compares the content and mode of blobs found via two tree objects
     for-each-ref         Output information on each ref
     for-each-repo        Run a Git command on a list of repositories
     get-tar-commit-id    Extract commit ID from an archive created using git-archive
     ls-files             Show information about files in the index and the working tree
     ls-remote            List references in a remote repository
     ls-tree              List the contents of a tree object
     merge-base           Find as good common ancestors as possible for a merge
     name-rev             Find symbolic names for given revs
     pack-redundant       Find redundant pack files
     rev-list             Lists commit objects in reverse chronological order
     rev-parse            Pick out and massage parameters
     show-index           Show packed archive index
     show-ref             List references in a local repository
     unpack-file          Creates a temporary file with a blob's contents
     var                  Show a Git logical variable
     verify-pack          Validate packed Git archive files

呪文表 ``ls-files``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド ``ls-files`` はインデックスと作業コピーに限定した :command:`ls`
のようなものである。テキスト一括処理の対象ファイルを絞るツールとして活用したい。

``ls-files --other --ignored --exclude-standard``
  作業コピーにあるすべての管理対象外ファイルをリストする。

次のものはシェルでインデックスから削除されたファイルを本当に削除するときのコマン
ド例だ：

.. code:: console

   bash$ rm $(git ls-files --deleted)

作業コピー管理内のファイルに限定して、何らかの文字列挿入・置換・削除をしたい場合
がかなりある。そのときは次のようなワンライナーで一気に片付く。次にファイル内の文
字列 ``OLD_PATTERN`` を ``NEW_PATTERN`` に置換する例を示す。

.. code:: console

   bash$ git ls-files -z | xargs -0 sed -i -e 's/OLD_PATTERN/NEW_PATTERN/g'

呪文表 ``ls-remote``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド ``ls-remote`` はリモートリポジトリーの参照をリストする。

``ls-remote <repositry> [HEAD]``
  リモートリポジトリー ``<repository>`` の ``HEAD`` 時点での参照をリストする。左
  列が ID で右列がブランチとタグ。

同期コマンド
----------------------------------------------------------------------

ヘルプによると、次のコマンド群は同期コマンドとして位置づけられている。一般ユー
ザー用のコマンドと、実装用コマンドに分けてリストされている。ここではどちらも私の
興味がないということで、一気に名前のみを挙げる。

次のコマンド群が操作用とされている：

  .. code:: text

     daemon               A really simple server for Git repositories
     fetch-pack           Receive missing objects from another repository
     http-backend         Server side implementation of Git over HTTP
     send-pack            Push objects over Git protocol to another repository
     update-server-info   Update auxiliary info file to help dumb servers

内部コマンド
----------------------------------------------------------------------

ヘルプによると、次のコマンド群は内部コマンドとして位置づけられている：

  .. code:: text

     check-attr           Display gitattributes information
     check-ignore         Debug gitignore / exclude files
     check-mailmap        Show canonical names and email addresses of contacts
     check-ref-format     Ensures that a reference name is well formed
     column               Display data in columns
     credential           Retrieve and store user credentials
     credential-cache     Helper to temporarily store passwords in memory
     credential-store     Helper to store credentials on disk
     fmt-merge-msg        Produce a merge commit message
     interpret-trailers   Add or parse structured information in commit messages
     mailinfo             Extracts patch and authorship from a single e-mail message
     mailsplit            Simple UNIX mbox splitter program
     merge-one-file       The standard helper program to use with git-merge-index
     patch-id             Compute unique ID for a patch
     sh-i18n              Git's i18n setup code for shell scripts
     sh-setup             Common Git shell script setup code
     stripspace           Remove unnecessary whitespace

もっとも <end users typically do not use them directly> とのことなので、私も当然
利用しない。

.. include:: /_include/git-refs.txt
