================================================================================
SQLite 利用ノート
================================================================================

.. |sqlite3| replace:: :program:`sqlite3`

:Since: 2000
:Official site: `SQLite Home Page <https://www.sqlite.org/>`__
:CLI: |sqlite3| 3.41.2

教材としては `SQLite Tutorial <https://www.sqlitetutorial.net/>`__ がいいと思わ
れる。SQL の基本を確認することも可能。

インストール
================================================================================

Homebrew を使えば SQLite の管理が容易になる。

.. sourcecode:: bash
   :caption: Homebrew に SQLite をインストールする命令例

   brew install sqlite

バージョン確認コマンドは ``sqlite3 -version``.

対話的セッションに入るにはコマンドラインから引数なしで |sqlite3| を実行する。ま
ず ``.help`` を実行してセッション終了方法を習得しろ。

構成
================================================================================

CLI のドットファイルのパスは :file:`$XDG_HOME_CONFIG/sqlite3/sqliterc` にした
い。:doc:`/xdg` 参照。

.. sourcecode:: bash
   :caption: 環境関数 `SQLITE_HISTORY` を定義する

   # .bashrc
   export SQLITE_HISTORY="$XDG_STATE_HOME/sqlite_history"

プロファイル内容は適当：

.. sourcecode:: console

   $ cat $XDG_CONFIG_HOME/sqlite3/sqliterc
   .headers ON
   .mode columns

アンインストール
================================================================================

SQLite をアンインストールする場合はこうするだろう：

* 本体をファイルシステムから削除する e.g. ``brew uninstall sqlite``
* 構成ファイルを削除する
* データベースファイルを削除する
