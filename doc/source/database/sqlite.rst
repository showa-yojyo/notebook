======================================================================
SQLite 利用ノート
======================================================================

:Since: 2000
:Official site: `SQLite Home Page <https://www.sqlite.org/index.html>`__
:CLI: :program:`sqlite3` 3.41.2

教材としては `SQLite Tutorial <https://www.sqlitetutorial.net/>`__ がいいと思わ
れる。SQL の基本を確認することも可能。

インストール
======================================================================

業務目的ではない場合、インストール手順は Python 環境に手を入れる手っ取り早い：

.. code:: console

   $ conda install sqlite

バージョン確認コマンドは ``sqlite3 -version``.

対話的セッションに入るにはコマンドラインから引数なしで ``sqlite3`` を実行する。
まず ``.help`` を実行してセッション終了方法を習得しろ。

構成
======================================================================

CLI のドットファイルのパスは :file:`$XDG_HOME_CONFIG/sqlite3/sqliterc` にした
い。:doc:`/xdg` 参照。

.. code:: bash

   # .bashrc
   export SQLITE_HISTORY="$XDG_STATE_HOME/sqlite_history"

内容は適当：

.. code:: console

   $ cat $XDG_CONFIG_HOME/sqlite3/sqliterc
   .headers ON
   .mode columns

アンインストール
======================================================================

SQLite をアンインストールする場合はこうするだろう：

* 本体をファイルシステムから削除する - ``conda uninstall sqlite``
* 構成ファイルを削除する
* データベースファイルを削除する
