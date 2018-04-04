======================================================================
環境変数
======================================================================
本節では Git_ の環境変数について記す。

.. contents::

概要
======================================================================
環境変数は、コマンドライン引数や ``.gitconfig`` での構成のように、
Git コマンドの振る舞いを制御する方法の一つだ。

普通はコマンドラインオプションか ``.gitconfig`` でできるならばそれらで済ませる。
しかし、それらで実現できそうにないことをする必要が生じた場合には、
環境変数で何とかできないかを模索したい。

リポジトリー関連
----------------------------------------------------------------------
ヘルプドキュメントでは、Git はリポジトリー関連の環境変数として次のものを参照するとしている。
これらの変数がすべてのコアコマンド群に影響する。
また、サードパーティー製の Git フロントエンドツールがこれらの環境変数を当てにしている。

GIT_INDEX_FILE,
GIT_INDEX_VERSION,
GIT_OBJECT_DIRECTORY,
GIT_ALTERNATE_OBJECT_DIRECTORIES,
GIT_DIR,
GIT_WORK_TREE,
GIT_NAMESPACE,
GIT_CEILING_DIRECTORIES,
GIT_DISCOVERY_ACROSS_FILESYSTEM,
GIT_COMMON_DIR.

以下、興味のあるものだけ記す。

GIT_INDEX_FILE
  リポジトリーのインデックスのパスを示す。

  * 通常はこの値をセットしないことによって、
    パス ``$GIT_DIR/index`` をインデックスとして採用する。

GIT_OBJECT_DIRECTORY
  リポジトリーのオブジェクト格納ディレクトリーのパスを示す。
  この直下に 16 進数 2 ケタのディレクトリーがズラッと並ぶようなディレクトリーのことだ。

  * 通常はこの値をセットしないことによって、
    パス ``$GIT_DIR/objects`` をオブジェクト格納ディレクトリーとして採用する。

GIT_DIR
  リポジトリーのベースディレクトリーを示す。

  * 通常はこの値をセットしないことによって、
    ディレクトリー ``.git`` をリポジトリーベースとして採用する。

  * この環境変数と同じ働きをするコマンドラインオプションが ``--git-dir=<directory>`` だ。

GIT_WORK_TREE
  作業コピーのルートのパスを示す。

  * 対応するコマンドラインオプションは ``--work-tree=<directory>`` だ。
  * 対応する ``.gitconfig`` の構成項目は ``core.worktree`` だ。

コミット関連
----------------------------------------------------------------------
次の環境変数はコミット履歴改竄の主役となるべきもので、たいへん有用だ。

GIT_AUTHOR_NAME,
GIT_AUTHOR_EMAIL,
GIT_AUTHOR_DATE,
GIT_COMMITTER_NAME,
GIT_COMMITTER_EMAIL,
GIT_COMMITTER_DATE,
EMAIL.

まとめて説明すると、コミットログにこれらの変数の名前が表現する情報がそれぞれ記録される。

例えば自分だけがコミットする個人用のリポジトリーがここにあるとする。
これはたった今よそのバージョン管理システムからコンバートしたばかりなので、
すべてのコミットにおいて、ログメッセージ中の上述の情報を適切にリセットしたい。

それにはコマンド filter-branch を用いる。
環境変数の渡し方が特殊で、一般には ``git`` の直前でセットするのだが、
このコマンドはオプション ``--env-filter=<command>`` でそれを行う。
[SO750172]_ で紹介されていた例を次に引用する。

.. code:: console

   $ git filter-branch -f --env-filter "
   > GIT_AUTHOR_NAME='Newname'
   > GIT_AUTHOR_EMAIL='new@email'
   > GIT_COMMITTER_NAME='Newname'
   > GIT_COMMITTER_EMAIL='new@email'
   > " HEAD

差分関連
----------------------------------------------------------------------
次の環境変数が差分コマンドに関連する。

GIT_DIFF_OPTS,
GIT_EXTERNAL_DIFF,
GIT_DIFF_PATH_COUNTER,
GIT_DIFF_PATH_TOTAL.

以下、興味のあるものだけ記す。

GIT_DIFF_OPTS
  差分コマンドにおける ``--unified=<n>`` や ``-U<n>`` オプションと同等。
  変更行の前後 `n` 行をついでに出力するかを指定する。
  こちらでの定義のほうが、コマンドライン引数での指定よりも優先度が高い。

GIT_EXTERNAL_DIFF
  差分コマンドに既定の差分プログラムではなく、外部プログラムを実行させるように設定できる。
  「外部プログラム」と書いたが、
  下の形式で呼び出すようなので実際にはラッパースクリプトを指定することになりそうだ。

  .. code:: console

     $ "$GIT_EXTERNAL_DIFF" old-file old-hex old-mode new-file new-hex new-mode

残りの変数は GIT_EXTERNAL_DIFF での処理中に自動的に設定される。

その他
----------------------------------------------------------------------
どの括りにも当てはまらない環境変数を次に列挙する。

GIT_MERGE_VERBOSITY,
GIT_PAGER,
GIT_EDITOR,
GIT_SSH,
GIT_SSH_COMMAND,
GIT_ASKPASS,
GIT_TERMINAL_PROMPT,
GIT_CONFIG_NOSYSTEM,
GIT_FLUSH,
GIT_TRACE,
GIT_TRACE_PACK_ACCESS,
GIT_TRACE_PACKET,
GIT_TRACE_PACKFILE,
GIT_TRACE_PERFORMANCE,
GIT_TRACE_SETUP,
GIT_TRACE_SHALLOW,
GIT_LITERAL_PATHSPECS,
GIT_GLOB_PATHSPECS,
GIT_NOGLOB_PATHSPECS,
GIT_ICASE_PATHSPECS,
GIT_REFLOG_ACTION,
GIT_REF_PARANOIA.

以下、興味のあるものだけ記す。

GIT_EDITOR
  Git のコマンドでテキストエディターを開く状況すべてにおいて、
  ここでエディターのパスが設定されていれば、それを開く。

  * EDITOR も VISUAL もどちらも未定義の場合に GIT_EDITOR が効いてくる。

  * 対応する ``.gitconfig`` の構成項目は ``core.editor`` だ。
    こちらで十分。

出典
======================================================================
.. [SO750172] `Change the author of a commit in Git <http://stackoverflow.com/questions/750172/change-the-author-of-a-commit-in-git>`_

.. include:: /_include/git-refs.txt
