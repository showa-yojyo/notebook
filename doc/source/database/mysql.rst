======================================================================
MySQL 利用ノート
======================================================================

:Since: 1995
:Official site: <https://www.mysql.com/>
:Version: 9.0.1 for Linux on x86_64
:CLI: :program:`mysql`
:Server: :program:`mysqld`

MySQL をとりあえず利用するまでの手順を記す。ただし、
:doc:`Docker</docker/index>` を利用するものとする。

.. rubric:: 以前の MySQL 環境の残滓を一掃する

環境が完全にクリーンである場合にはここを飛ばしてイメージ入手工程を読め。以前、何
かの MySQL チュートリアルをやって上手くいかなかった場合にはこの工程が外せない。
クライアントくらいは残しておいても良いが、便宜上 Docker ホスト側には MySQL の実
行系は残さないことにする。

Google で "How to uninstall MySQL on Ubuntu" などで検索すれば手順は山ほど見つか
るが、簡単にまとめておく。

おそらく :program:`apt` を利用して環境構築したはずなので、次の手順に従えばひじょ
うに上手くいく：

.. sourcecode:: console
   :caption: アンインストール手順例

   $ sudo systemctl stop mysqld
   $ sudo apt purge mysql-server mysql-common mysql-server-core-* mysql-client-core-*
   $ sudo rm -rf {/var/lib/,/var/log/,/etc/}mysql/
   $ sudo deluser --remove-home mysql
   $ sudo delgroup mysql
   $ sudo apt remove dbconfig-mysql

この手順でも ``apt list mysql*`` などで関連パッケージが出力されるかもしれない。
その場合は出処を確認してなじみのリポジトリーならば納得するしかない：

.. sourcecode:: console

   $ apt search mysql-client-8.0
   Sorting... Done
   Full Text Search... Done
   mysql-client/jammy-updates,jammy-security 8.0.39-0ubuntu0.22.04.1 all
     MySQL database client (metapackage depending on the latest version)

   mysql-client-8.0/jammy-updates,jammy-security 8.0.39-0ubuntu0.22.04.1 amd64
     MySQL database client binaries

.. rubric:: イメージを入手してコンテナーを稼働する

最初に Docker Hub から公式イメージを検索して、それをローカルに持ってくる：

.. sourcecode:: console
   :caption: MySQL イメージ取得例

   $ docker search MySQL --filter=stars=5000
   NAME      DESCRIPTION                                     STARS     OFFICIAL
   mysql     MySQL is a widely used, open-source relation…   15262     [OK]
   mariadb   MariaDB Server is a high performing open sou…   5805      [OK]
   $ docker pull mysql
   Using default tag: latest
   latest: Pulling from library/mysql
   ae34d51c6da2: Download complete
   fe4b01031aab: Download complete
   cc168a9482de: Download complete
   d9a40b27c30f: Download complete
   aa72c34c4347: Download complete
   473ade985fa2: Download complete
   10e5505c3ae4: Download complete
   3e3fac98ea83: Download complete
   a79ade39aab9: Download complete
   3ca3786815dd: Download complete
   Digest: sha256:d8df069848906979fd7511db00dc22efeb0a33a990d87c3c6d3fcdafd6fc6123
   Status: Downloaded newer image for mysql:latest
   docker.io/library/mysql:latest
   $ docker images --filter reference=mysql
   REPOSITORY   TAG       IMAGE ID       CREATED      SIZE
   mysql        latest    d8df06984890   9 days ago   802MB

コマンドライン引数を決めているのならばいきなり ``docker run`` で可。

.. seealso::

   MariaDB については :doc:`./mariadb` で探求する。

コンテナーに例えば ``some-mysql`` などの名前を付けて稼働する。このときに MySQL
に対して必要な情報、環境変数を指定する：

.. sourcecode:: console
   :caption: MySQL コンテナー稼働コマンド例

   $ docker create --name some-mysql \
       -e MYSQL_USER=some-user \
       -e MYSQL_PASSWORD=some-secret-pw \
       -e MYSQL_ROOT_PASSWORD=my-secret-pw mysql
   6460fcdc5e4b7b3b05c51b2ba3b903728cc3f5e97b2f832162d451355259590e
   $ docker start some-mysql

あくまでも練習用の手順なので、パスワードの扱いはここではぞんざいだ。

.. rubric:: データベースクライアントを実行する

コンテナー内で稼働している MySQL サーバーに CLI でアクセスしたい。このコンテナー
内でアクセスする方法と、Docker ホスト側で CLI を使ってアクセスする方法があり得
る。ホストの MySQL 環境は破壊したという前提でノートをとっているので、後者は扱わ
ない。

.. sourcecode:: console
   :caption: 稼働中の MySQL コンテナーで CLI を対話的に起動する例

   $ docker exec -it some-mysql mysql -u some-user -p
   Enter password:
   Welcome to the MySQL monitor.  Commands end with ; or \g.
   Your MySQL connection id is 10
   Server version: 9.0.1 MySQL Community Server - GPL

   Copyright (c) 2000, 2024, Oracle and/or its affiliates.

   Oracle is a registered trademark of Oracle Corporation and/or its
   affiliates. Other names may be trademarks of their respective
   owners.

   Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

   mysql>

.. rubric:: コンテナーを一時停止する

MySQL コンテナーを一時停止、再開するには次のどちらかの組み合わせを実行する：

.. sourcecode:: console
   :caption: コンテナー一時停止＆再開例

   $ docker stop some-mysql
   $ docker start some-mysql

   $ docker pause some-mysql
   $ docker unpause some-mysql

後者の方法はシステム資源を一時的に解放する必要がある場合に便利であることを覚えて
おく。

.. rubric:: SQL などの練習をする

MySQL 公式文書のチュートリアルも有用であるし、キーワード "MySQL Tutorial" などで
Google 検索するとそれらしい教材がたくさん見つかる。

* `MySQL :: MySQL 9.0 Reference Manual :: 5 Tutorial
  <https://dev.mysql.com/doc/refman/9.0/en/tutorial.html>`__
* `MySQL Tutorial - Learn MySQL Fast, Easy and Fun.
  <https://www.mysqltutorial.org/>`__

.. rubric:: ドットファイル

ここで言うドットファイルとは :program:`mysql` に対する :file:`.my.cnf` とする。

.. todo::

   少し調べたら :program:`mysql` の他に :program:`mysqlsh` というクライアントプ
   ログラムが存在するようだ。こちらのほうがカスタマイズしやすい？

構成ファイルのパスを確認するには、ヘルプ出力の ``Default options are read from
the following files in the given order`` の行付近を見る：

.. sourcecode:: console
   :caption: ロードされるドットファイルパスを得る例

   # mysql --help | grep -A1 "Default options"
   Default options are read from the following files in the given order:
   /etc/my.cnf /etc/mysql/my.cnf /usr/etc/my.cnf ~/.my.cnf

残念なことに :file:`~/.my.cnf` はこのパス意外に設定不可能らしい。XDG Base
Directory Specification に適合不能。仕方がないので、コンテナーを稼働するホスト側
ディレクトリーにこのファイルを置いて、bind-mount を適宜指定する方針を採る。

.. sourcecode:: console
   :caption: コンテナー再作成例

   $ docker stop some-mysql; docker rm some-mysql
   $ docker create --name some-mysql \
       -e MYSQL_USER=some-user \
       -e MYSQL_PASSWORD=some-secret-pw \
       -e MYSQL_ROOT_PASSWORD=my-secret-pw \
       --mount type=bind,source=/path/to/.my.cnf,target=/root/.my.cnf,readonly \
       mysql

ドットファイルの中身は暫定的に次のようにしておく：

.. sourcecode:: ini
   :caption: Example of :file:`.my.cnf`

   [client]
   user=some-user
   password=some-secret-pw
   prompt='\\u \\R:\\m:\\s [\\c]>\\_'

なぜか YYYY-mm-dd が表示できない。

.. admonition:: 利用者ノート

   同様の考え方により、履歴ファイルをホスト側に配置したいのだが、MySQL の不具合
   によりホストに用意した :file:`.mysql_history` に bind-mount することができな
   いようだ。

   .. sourcecode:: mysql

      mysql> quit
      mysql: Error on rename of '/root/.mysql_history.TMP' to '/root/.mysql_history' (OS errno 16 - Device or resource busy)
      Bye

   Google で検索すると Docker と関係なく起こり得る現象らしいことがわかる。解法を
   見いだせないので、コンテナー停止後に履歴ファイルをホストへ手動コピーすること
   でしのぐ。

.. rubric:: データ格納場所

コンテナー内 :file:`/var/lib/mysql` が既定のデータベース格納場所であり、これをホ
スト側で管理したい場合には bind-mount を適宜指定する。ホスト側のディレクトリーは
前もって手動で作成しておく。

.. sourcecode:: console
   :caption: :file:`/path/to` は差し当たり ``$PWD`` にしておけ

   $ docker run -d \
       --name some-mysql \
       -e MYSQL_USER=some-user \
       -e MYSQL_PASSWORD=some-secret-pw \
       -e MYSQL_ROOT_PASSWORD=my-secret-pw \
       --mount type=bind,source=/path/to/.my.cnf,target=/root/.my.cnf,readonly \
       --mount type=bind,source=/path/to/datadir,target=/var/lib/mysql \
       postgres

この結果、ホスト側ファイルシステム部分である :file:`./datadir` にデータベース実
体が保存される。コンテナーをいったん廃棄して再度この ``docker run`` コマンドを実
行すると、データベースが維持できていることが確認できる。

.. rubric:: まとめ

Docker Compose を利用する。ファイル :file:`compose.yaml` を次のような内容で
``docker run`` を実行してきたディレクトリー内に用意する：

.. sourcecode:: yaml
   :caption: Example of :file:`compose.yaml`

   services:
     db:
       container_name: mysql
       image: mysql
       environment:
         MYSQL_USER: some-user
         MYSQL_PASSWORD: some-secret-pw
         MYSQL_ROOT_PASSWORD: my-secret-pw
       volumes:
       - type: bind
         source: /path/to/datadir
         target: /var/lib/mysql
       - type: bind
         source: /path/to/.my.cnf
         target: /root/.my.cnf
         read_only: true

これで ``docker compose up -d`` や ``docker compose down`` が利用可能になる。

.. rubric:: サンプルデータベースを構築する

まずコンテナーを停止して破棄する。

先述のチュートリアルサイトからサンプルデータベースの素となるファイルをダウンロー
ドする。圧縮ファイルの中身は :program:`mysql` が処理可能な形式だ。

.. sourcecode:: console
   :caption: サンプルデータベースをダウンロードして解答する

   $ curl -O https://www.mysqltutorial.org/wp-content/uploads/2023/10/mysqlsampledatabase.zip
   $ unzip mysqlsampledatabase.zip

ここでコンテナーを稼働する。

ここからはいろいろな方法があるが、紛れの少ないものを記す。得られたファイル
:file:`mysqlsampledatabase.sql` をコンテナーの適当な一時ディレクトリーにコピー
し、それを MySQL に処理させる。このとき、ユーザーを root としておくのがわかりや
すい。

それからコンテナーに対して :program:`mysql` をユーザー root で実行する：

.. sourcecode:: console
   :caption: ファイルをコンテナーにコピーした後、データベースにログイン

   $ docker cp ./mysqlsampledatabase.sql some-mysql:/tmp
   $ docker exec -it some-mysql mysql -uroot -pmy-secret-pw

.. admonition:: 利用者ノート

   :program:`mysql` のコマンドラインオプションと値の間には空白文字を挟まないのが
   無難だ。特にパスワードを指定する ``-p`` においては。

MySQL セッションでは例のファイルを source する。それから作業用ユーザーにアクセス
権を供与して root での作業は完了する：

.. sourcecode:: mysql
   :caption: サンプルデータベースをインポートする例

   mysql> source /tmp/mysqlsampledatabase.sql
   mysql> GRANT ALL PRIVILEGES ON classicmodels.* TO 'some-user'@'%';
   mysql> quit

最後にコンテナーに対して :program:`mysql` をユーザー some-user で実行し、データ
ベースを classicmodels に切り替えてチュートリアルを実施可能であることを確認す
る：

.. sourcecode:: mysql
   :caption: サンプルデータベースを確認

   mysql> show databases;
   mysql> use classicmodels;
   mysql> show tables;

先ほどの bind-mount が効いているので、コンテナーを再稼働しても、データベース
classicmodels にアクセスできるはずだ。

.. rubric:: コンテナーを廃棄する

MySQL コンテナーが用済みになったらそれを削除することでデータベースも消去される。
失いたくない場合には ``docker run`` の段階でマウントなどを指定するか、コンテナー
にあるデータベースをホスト側に退避させるのだろう。

.. sourcecode:: console
   :caption: コンテナーを捨てるコマンド例

   $ docker stop some-mysql
   $ docker rm some-mysql

ディスクに余裕がなければ MySQL イメージも削除する。

.. rubric:: 参考文献一覧

* `mysql - Official Image <https://hub.docker.com/_/mysql>`__
* `MySQL :: A Quick Guide to Using the MySQL APT Repository
  <https://dev.mysql.com/doc/mysql-apt-repo-quick-guide/en/>`__
* `20.04 - How to completely remove MySQL from my system? - Ask Ubuntu
  <https://askubuntu.com/questions/1270094/how-to-completely-remove-mysql-from-my-system>`__
* `How to Uninstall MySQL on Ubuntu | Linux Tutorials for Beginners
  <https://webhostinggeeks.com/howto/how-to-uninstall-mysql-on-ubuntu/>`__
* `How to properly uninstall MySQL Server in Ubuntu
  <https://www.fosslinux.com/96135/how-to-properly-uninstall-mysql-server-in-ubuntu.htm>`__

----

ネットワークや Dockerfile によるカスタムコンテナー作成など、未実施の項目が残って
いるが、ひとまず終わる。
