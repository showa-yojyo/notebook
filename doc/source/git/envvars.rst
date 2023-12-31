======================================================================
環境変数
======================================================================

本節では Git_ の環境変数について記す。コマンド ``git help git`` の出力中に環境変
数に関するまとまった記述がある。

.. contents::

概要
======================================================================

環境変数は、コマンドライン引数や :file:`.gitconfig` での構成のように、Git コマン
ドの振る舞いを制御する方法の一つだ。

普通はコマンドラインオプションか構成ファイルでできるならばそれらで済ませる。しか
し、それらで実現できそうにないことをする必要が生じた場合には、環境変数で何とかで
きないかを模索したい。

リポジトリー関連
----------------------------------------------------------------------

ヘルプドキュメントでは、Git はリポジトリー関連の環境変数として次のものを参照する
としている。これらの変数がすべてのコアコマンド群に影響する。また、サードパー
ティー製の Git フロントエンドツールがこれらの環境変数を当てにしている。

.. code:: text

   GIT_INDEX_FILE
   GIT_INDEX_VERSION
   GIT_OBJECT_DIRECTORY
   GIT_ALTERNATE_OBJECT_DIRECTORIES
   GIT_DIR
   GIT_WORK_TREE
   GIT_NAMESPACE
   GIT_CEILING_DIRECTORIES
   GIT_DISCOVERY_ACROSS_FILESYSTEM
   GIT_COMMON_DIR
   GIT_DEFAULT_HASH

以下、興味のあるものだけ記す。

``GIT_INDEX_FILE``
  リポジトリーのインデックスのパスを示す。通常はこの値をセットしないことによっ
  て、パス :file:`$GIT_DIR/index` をインデックスとして採用する。

``GIT_OBJECT_DIRECTORY``
  リポジトリーのオブジェクト格納ディレクトリーのパスを示す。この直下に 16 進数二
  ケタのディレクトリーがズラッと並ぶようなディレクトリーのことだ。通常はこの値を
  セットしないことによって、パス :file:`$GIT_DIR/objects` をオブジェクト格納ディ
  レクトリーとして採用する。

``GIT_DIR``
  リポジトリーのベースディレクトリーを示す。通常はこの値をセットしないことによっ
  て、ディレクトリー :file:`.git` をリポジトリーベースとして採用する。この環境変
  数と同じ働きをするコマンドラインオプションが :option:`--git-dir` だ。

``GIT_WORK_TREE``
  作業コピーのルートのパスを示す。対応するコマンドラインオプションは
  :option:`--work-tree` だ。対応する :file:`.gitconfig` の構成項目は
  ``core.worktree`` だ。

コミット関連
----------------------------------------------------------------------

次の環境変数はコミット履歴改竄の主役となるべきもので、たいへん有用だ：

.. code:: text

   GIT_AUTHOR_NAME
   GIT_AUTHOR_EMAIL
   GIT_AUTHOR_DATE
   GIT_COMMITTER_NAME
   GIT_COMMITTER_EMAIL
   GIT_COMMITTER_DATE
   EMAIL

まとめて説明すると、コミットログにこれらの変数の名前が表現する情報がそれぞれ記録
される。

例えば自分だけがコミットする個人用のリポジトリーがここにあるとする。これはたった
今よそのバージョン管理システムからコンバートしたばかりなので、すべてのコミットに
おいて、ログメッセージ中の上述の情報を適切にリセットしたい。

それにはコマンド ``filter-branch`` を用いる。環境変数の渡し方が特殊で、一
般には ``git`` の直前でセットするのだが、このコマンドはオプション
``--env-filter=<command>`` でそれを行う。[SO750172]_ で紹介されていた例を
次に引用する：

.. code:: console

   bash$ git filter-branch -f --env-filter "
     GIT_AUTHOR_NAME='Newname'
     GIT_AUTHOR_EMAIL='new@email'
     GIT_COMMITTER_NAME='Newname'
     GIT_COMMITTER_EMAIL='new@email'" HEAD

差分関連
----------------------------------------------------------------------

次の環境変数が差分コマンドに関連する：

.. code:: text

   GIT_DIFF_OPTS
   GIT_EXTERNAL_DIFF
   GIT_DIFF_PATH_COUNTER
   GIT_DIFF_PATH_TOTAL

以下、興味のあるものだけ記す。

``GIT_DIFF_OPTS``
  差分コマンドにおける ``--unified=<n>`` や ``-U<n>`` オプションと同等。変更行の
  前後 ``n`` 行をついでに出力するかを指定する。こちらでの定義のほうが、コマンドラ
  イン引数での指定よりも優先度が高い。

``GIT_EXTERNAL_DIFF``
  差分コマンドに既定の差分プログラムではなく、外部プログラムを実行させるように設
  定できる。「外部プログラム」と書いたが、下の形式で呼び出すようなので実際には
  ラッパースクリプトを指定することになりそうだ。

  .. code:: console

     bash$ "$GIT_EXTERNAL_DIFF" old-file old-hex old-mode new-file new-hex new-mode

残りの変数は ``GIT_EXTERNAL_DIFF`` での処理中に自動的に設定される。

その他
----------------------------------------------------------------------

どの括りにも当てはまらない環境変数を次に列挙する：

.. code:: text

   GIT_MERGE_VERBOSITY
   GIT_PAGER
   GIT_PROGRESS_DELAY
   GIT_EDITOR
   GIT_SEQUENCE_EDITOR
   GIT_SSH
   GIT_SSH_COMMAND
   GIT_SSH_VARIANT
   GIT_ASKPASS
   GIT_TERMINAL_PROMPT
   GIT_CONFIG_GLOBAL
   GIT_CONFIG_SYSTEM
   GIT_CONFIG_NOSYSTEM
   GIT_FLUSH
   GIT_TRACE
   GIT_TRACE_FSMONITOR
   GIT_TRACE_PACK_ACCESS
   GIT_TRACE_PACKET
   GIT_TRACE_PACKFILE
   GIT_TRACE_PERFORMANCE
   GIT_TRACE_REFS
   GIT_TRACE_SETUP
   GIT_TRACE_SHALLOW
   GIT_TRACE_CURL
   GIT_TRACE_CURL_NO_DATA
   GIT_TRACE2
   GIT_TRACE2_EVENT
   GIT_TRACE2_PERF
   GIT_TRACE2_REDACT
   GIT_LITERAL_PATHSPECS
   GIT_GLOB_PATHSPECS
   GIT_NOGLOB_PATHSPECS
   GIT_ICASE_PATHSPECS
   GIT_REFLOG_ACTION
   GIT_REF_PARANOIA
   GIT_ALLOW_PROTOCOL
   GIT_PROTOCOL_FROM_USER
   GIT_PROTOCOL
   GIT_OPTIONAL_LOCKS
   GIT_REDIRECT_STDIN
   GIT_REDIRECT_STDOUT
   GIT_REDIRECT_STDERR
   GIT_PRINT_SHA1_ELLIPSIS (deprecated)

以下、興味のあるものだけ記す。

``GIT_PAGER``
  ページャーを指定したい場合にこれを設定する。値が空であるか、もしくは文字列
  ``cat`` であれば、Git はページャーを起動しなくなる。

  他にもページャーを指定する方法はあり、優先順位は次のようになっている：

  1. 環境変数 ``GIT_PAGER``
  2. 設定項目 ``core.pager``
  3. 環境変数 ``PAGER``

  これは差分表示などでページャーが出てくるのを防ぐのに使える。ページャーを一時的
  に無効にしたいならば次のようにすればいい：

  .. code:: console

     bash$ GIT_PAGER= git diff

``GIT_EDITOR``
  Git のコマンドでテキストエディターを開く状況すべてにおいて、ここでエディターの
  パスが設定されていれば、それを開く。``EDITOR`` も ``VISUAL`` もどちらも未定義
  の場合に ``GIT_EDITOR`` が効いてくる。対応する :file:`.gitconfig` の構成項目は
  ``core.editor`` だ。こちらで十分。

出典
======================================================================

.. [SO750172] `Change the author of a commit in Git <http://stackoverflow.com/questions/750172/change-the-author-of-a-commit-in-git>`_

.. include:: /_include/git-refs.txt
