======================================================================
MariaDB 利用ノート
======================================================================

:Since: 2013
:Official site: <https://mariadb.org/>
:CLI: :program:`mariadb`, :program:`mysql`
:Server Version: 11.4.2-MariaDB-ubu2404 mariadb.org binary distribution

MariaDB をとりあえず利用するまでの手順を記す。ただし、Docker を利用するものとす
る。

`Installing and Using MariaDB via Docker - MariaDB Knowledge Base
<https://mariadb.com/kb/en/installing-and-using-mariadb-via-docker/>`__ の記述に
従えばデータベースシェル起動まではすんなり実現するはずだ。以下に要点をまとめてお
く。

.. rubric:: イメージを入手してコンテナーを稼働する

最初に Docker Hub から公式イメージを検索して、それをローカルに持ってくる：

.. sourcecode:: console
   :caption: MariaDB イメージ取得例

   $ docker search mariadb --filter=stars=5000
   $ docker pull mariadb
   $ docker images --filter reference=mariadb

コンテナーに例えば ``mariadbtest`` などの名前を付けて稼働する。このときに
MariaDB に対して必要な情報、環境変数を指定する：

.. sourcecode:: console
   :caption: MariaDB コンテナー稼働コマンド例

   $ docker run --name mariadbtest -e MARIADB_ROOT_PASSWORD=mypass -p 3306:3306 -d mariadb

あくまでも練習用の手順なので、パスワードの扱いはここではぞんざいだ。

.. rubric:: データベースクライアントを実行する

コンテナー内で稼働している MariaDB サーバーに CLI でアクセスしたい。このコンテ
ナー内でアクセスする方法と、ホスト側で CLI を使ってアクセスする方法があり得る。
前者は：

.. sourcecode:: console
   :caption: 稼働中の MariaDB コンテナーで CLI を対話的に起動する例

   $ docker exec -it mariadbtest mariadb -p
   Enter password:
   Welcome to the MariaDB monitor.  Commands end with ; or \g.
   Your MariaDB connection id is 4
   Server version: 11.4.2-MariaDB-ubu2404 mariadb.org binary distribution

   Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

   Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

   MariaDB [(none)]>

後者を行うにはコンテナーの IP アドレスが必要だ。次の例ではホスト側にある
:program:`mysql` を使って接続するが、ホストにおいても :program:`mariadb` が実行
可能であればもちろんそれが使える：

.. sourcecode:: console
   :caption: ホスト側 CLI からコンテナーの MariaDB サーバーに接続する例

   $ docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mariadbtest
   172.17.0.2
   $ mysql -h 172.17.0.2 -u root -p
   Enter password:
   Welcome to the MySQL monitor.  Commands end with ; or \g.
   Your MySQL connection id is 5
   Server version: 11.4.2-MariaDB-ubu2404 mariadb.org binary distribution

   Copyright (c) 2000, 2018, Oracle and/or its affiliates. All rights reserved.

   Oracle is a registered trademark of Oracle Corporation and/or its
   affiliates. Other names may be trademarks of their respective
   owners.

   Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

   mysql>

.. admonition:: 利用者ノート

   IP アドレスを適当な変数を定義してそれに代入しておくのが行儀が良いかもしれな
   い。

.. rubric:: コンテナーを一時停止する

MaridDB コンテナーを一時停止、再開するには次のどちらかの組み合わせを実行する：

.. sourcecode:: console
   :caption: コンテナー一時停止＆再開例

   $ docker stop mariadbtest
   $ docker start mariadbtest

   $ docker pause mariadbtest
   $ docker unpause mariadbtest

後者の方法はシステム資源を一時的に解放する必要がある場合に便利であることを覚えて
おく。

.. rubric:: SQL などの練習をする

`Beginner MariaDB Articles - MariaDB Knowledge Base
<https://mariadb.com/kb/en/beginner-mariadb-articles/>`__ のいくつかの SQL 文や
コマンドはそのまま実行可能。

別のページにチュートリアルリンク一覧がある。

.. rubric:: ドットファイル

構成ファイルのパスはヘルプコマンドで確認可能：

.. sourcecode:: console
   :caption: ロードされるドットファイルパスを得る例

   $ mariadb --help --verbose | head -n 10
   mariadb from 11.4.2-MariaDB, client 15.2 for debian-linux-gnu (x86_64) using  EditLine wrapper
   Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

   Usage: mariadb [OPTIONS] [database]

   Default options are read from the following files in the given order:
   /etc/my.cnf /etc/mysql/my.cnf ~/.my.cnf
   ...

次に述べるバインドマウントの手法を用いて、前項の構成ファイルをホスト側に用意する
ことも可能。

.. rubric:: データ格納場所

データをホスト側のどこに格納するかを指定する方法はいくつかあるようだ。いずれにせ
よコンテナー稼働時に指定する。

.. sourcecode:: console
   :caption: Docker Hub の記事にあるコマンド例（改変）

   $ mkdir datadir
   $ docker run --name mariadb \
       --mount type=bind,source=$(pwd)/datadir,target=/var/lib/mysql \
       -e MARIADB_ROOT_PASSWORD=mypass -d mariadb

これで :command:`mariadb` で実行したデータベース操作がホスト側ディレクトリー
:file:`$(pwd)/datadir` 以下に作用する。きちんとした内容は `mariadb - Official
Image <https://hub.docker.com/_/mariadb>`__ を参照しろ。

.. rubric:: コンテナーを廃棄する

MariaDB コンテナーが用済みになったらそれを削除することでデータベースも消去され
る。失いたくない場合には ``docker run`` の段階でマウントなどを指定するか、コンテ
ナーにあるデータベースをホスト側に退避させるのだろう。

.. sourcecode:: console
   :caption: コンテナーを捨てるコマンド例

   $ docker stop mariadbtest
   $ docker rm mariadbtest

ディスクに余裕がなければ MariaDB イメージも削除する。

----

ネットワークや Dockerfile など、未実施の項目が残っているが、ひとまず終わる。
