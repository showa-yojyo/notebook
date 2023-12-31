======================================================================
Firebird 利用ノート
======================================================================

:Since: 2000
:Official site: `Firebird <https://firebirdsql.org/en/start/>`__
:License: IPL, IDPL
:Version: 5.0 rc1
:CLI: :program:`isql`

まずは `Firebird 5 Quick Start Guide
<https://firebirdsql.org/file/documentation/html/en/firebirddocs/qsg5/firebird-5-quickstartguide.html>`__
に従って、Firebird を設置したい。

インストール手順は、適当な圧縮ファイルをダウンロードして解凍し、同梱されているス
クリプトを実行する、だ。圧縮ファイルの URL は公式サイトの :guilabel:`DOWNLOADS`
からたどれる。今回試すのは
:file:`Firebird-5.0.0.1227-ReleaseCandidate1-linux-x64.tar.gz` とする。

   Please install required library 'tommath' before firebird, after it repeat
   firebird install

このメッセージが出たら :command:`apt` でかまわないので当該パッケージをインストー
ルしろ。私の場合は ``sudo apt install libtommath1`` で次へ進めた。

   Please enter new password for SYSDBA user:

このプロンプトがあるので、パスワードをあらかじめ決めておけ。

以上でインストールが完了すると共にサーバーが稼働する。マニュアルでは稼働状態を
:command:`top` で確認している。

サーバーと同時に、クライアントプログラムもインストールされる。コンソールで
:file:`/opt/firebird/bin/isql` を実行すると対話シェルが起動する。

SYSDBA で初回はログインして、マニュアルの勧めに従って作業用のユーザーを作成す
る。二つ作っておくと良い。また、一方にはテーブル操作権限を付与しておくとなお良
い。SQL を試すときには :program:`isql` セッションに作業ユーザーでログインし直す。

.. code:: console

   $ isql localhost:employee -u SYSDBA -p masterkey;
   SQL> grant create table to user USERNAME;
   SQL> grant create view to user USERNAME;
   SQL> grant create sequence to user USERNAME;
   SQL> quit;

   $ isql localhost:employee -u USERNAME -p PASSWORD
   SQL> show tables;
   COUNTRY
   CUSTOMER
   DEPARTMENT
   EMPLOYEE
   EMPLOYEE_PROJECT
   JOB
   PROJECT
   PROJ_DEPT_BUDGET
   SALARY_HISTORY
   SALES
   SQL> help;
   SQL> set;
   SQL> set count;

ユーザー名とパスワードを毎回入力するのは煩雑なので、環境変数二つに設定しておく：

.. code:: bash

   export ISC_USER=USERNAME
   export ISC_PASSWORD=PASSWORD

こうしておけば、:command:`isql` の引数はデータベースだけで済む。ロック機能を試す
ためにアカウントを複数作成するときが手こずるかもしれない。コツ：

:program:`isql` マニュアルについては次を参照：
`Firebird Interactive SQL Utility
<https://firebirdsql.org/file/documentation/html/en/firebirddocs/isql/firebird-isql.html>`__.

初心者のうちはコマンド実行後に何も出力されないと不安なので ``SET COUNT`` を実行
しておくといい。

Firebird サーバーを停止するには：

.. code:: console

   $ sudo service firebird stop

アンインストールするには、おそらく次の項目をこなす：

* サーバーを休止状態にする
* データベースをバックアップする
* インストールディレクトリーを削除する

以上を行うスクリプトがインストールされているので、それを実行する：

.. code:: console

   $ sudo bash /opt/firebird/bin/FirebirdUninstall.sh

   Firebird 5.0.0.1227-ReleaseCandidate1.x64 Uninstall program

   Are you sure you want to proceed?

   Press Enter to start uninstall or ^C to abort^C
   Uninstalling...
   Stopping Guardian server: Stopping Firebird server: Saved a copy of SecurityDatabase (security5.fdb) in /tmp
   Uninstall completed
