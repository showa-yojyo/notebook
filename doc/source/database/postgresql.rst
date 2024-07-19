======================================================================
PostgreSQL 利用ノート
======================================================================

:Since: 1996
:Official site: <https://www.postgresql.org/>
:Version: :program:`psql` 16.3 (Debian 16.3-1.pgdg120+1)

PostgreSQL をとりあえず利用するまでの手順を記す。SQL 学習環境が得られれば十分
だ。本稿では :doc:`Docker</docker/index>` を利用するものとする。

.. rubric:: 以前の PostgreSQL 環境の残滓を一掃する

環境が完全にクリーンである場合にはここを飛ばしてイメージ入手工程を読め。以前、何
かの PostgreSQL チュートリアルをやって上手くいかなかった場合にはこの工程が外せな
い。

おそらく :program:`apt` を利用して環境構築したはずなので、次の手順に従えばひじょ
うに上手くいく：

`How to Uninstall PostgreSQL from Ubuntu
<https://www.postgresqltutorial.com/postgresql-administration/uninstall-postgresql-ubuntu/>`__

.. sourcecode::
   :caption: アンインストール手順例

   $ sudo apt remove --purge postgresql
   $ dpkg -l | grep postgres
   $ sudo apt remove --purge postgresql-{{,client-}{14,common},contrib}
   $ sudo rm -rf {/var/lib/,/var/log/,/etc/}postgresql/
   $ sudo deluser postgres

さらにユーザー設定ファイルも削除するべきだと考えられる。後ほど XDG Base
Directory 対応と同時に設定ファイルを作り直す想定だ。

.. rubric:: イメージを入手してコンテナーを稼働する

最初に Docker Hub から公式イメージを検索して、それをローカルに持ってくる：

.. sourcecode:: console
   :caption: PostgreSQL イメージ取得例

   $ docker search postgresql --filter=is-official=true
   $ docker pull postgres
   $ docker images --filter reference=postgres

コンテナーに例えば ``some-postgres`` などの名前を付けて稼働する。このときに
PostgreSQL に対して必要な情報、環境変数を指定する：

.. sourcecode:: console
   :caption: PostgreSQL コンテナー稼働コマンド例

   $ docker run --name some-postgres -e POSTGRES_PASSWORD=secret -d postgres

これで PostgreSQL サーバーが稼働する。あくまでも練習用の手順なので、パスワードの
扱いはここではぞんざいだ。

.. rubric:: データベースクライアントを実行する

PostgreSQL が稼働しているコンテナーに「入って」クライアント :program:`psql` を実
行したい。

.. sourcecode:: console
   :caption: 稼働中の PostgreSQL コンテナーで CLI を対話的に起動する例

   $ docker exec -it -u postgres some-postgres createdb mydb
   $ docker exec -it -u postgres some-postgres psql -s mydb
   psql (16.3 (Debian 16.3-1.pgdg120+1))
   Type "help" for help.

   mydb=#

.. rubric:: コンテナーを一時停止する

PostgreSQL コンテナーを一時停止、再開するには次のどちらかの組み合わせを実行す
る：

.. sourcecode:: console
   :caption: コンテナー一時停止＆再開例

   $ docker stop some-postgres
   $ docker start some-postgres

   $ docker pause some-postgres
   $ docker unpause some-postgres

システム資源を一時的に解放する必要がある場合に停止するといい。

.. rubric:: SQL などの練習をする

PostgreSQL 公式文書のチュートリアルも有用であるし、キーワード "PostgreSQL
Tutorial" などで Google 検索するとそれらしい教材がたくさん見つかる。

* `公式チュートリアル <https://www.postgresql.org/docs/current/tutorial.html>`__
* `PostgreSQL Tutorial <https://www.postgresqltutorial.com/>`__

.. rubric:: ドットファイル

ここで言うドットファイルとは :file:`.psqlrc` とする。PostgreSQL 環境を Docker コ
ンテナーではなくホストに構築したとするならば、次のようにこのファイルを管理した
い。まず、Bash ドットファイル :file:`.bashrc` で :envvar:`PSQLRC` と
:envvar:`PSQL_HISTORY` を設定する：

.. sourcecode:: bash
   :caption: PSQLRC と PSQL_HISTORY の設定例

   export PSQLRC="$XDG_CONFIG_HOME/postgresql/psqlrc"
   export PSQL_HISTORY="$XDG_STATE_HOME/postgresql/psql_history"

上記パスのディレクトリー部分に当たるものは :command:`mkdir` しておく必要がある。
ここまで述べた方式はクライアントプログラム :program:`psql` をホスト環境にインス
トールしている場合にはそのまま使える。

コンテナー環境の :program:`psql` を利用する場合。ユーザーは postgres であるとす
ると、その :envvar:`HOME` は :file:`/var/lib/postgresql` だ。この直下にドット
ファイルが置かれる。コンテナー稼働開始時にホストファイルを bind-mount すれば行け
る。履歴はコンテナーに置いてかまわないと考えるので指定しない。

.. sourcecode:: console

   $ docker run -d \
       --name some-postgres \
       -e POSTGRES_PASSWORD=secret \
       --mount type=bind,source=$PSQLRC,target=/var/lib/postgresql/.psqlrc,readonly \
       postgres

サーバードットファイルに関しても同様に、ホストにカスタム版を置いて bind-mount す
ることが可能だ。ログが欲しい場合などに設定項目を編集することになる。

.. sourcecode:: console

   $ docker run -d \
       --name some-postgres \
       -e POSTGRES_PASSWORD=secret \
       --mount type=bind,source=/path/to/my-postgres.conf,/etc/postgresql/postgresql.conf,readonly \
       postgres -c config_file=/etc/postgresql/postgresql.conf

.. rubric:: データ格納場所

コンテナー内 :file:`/var/lib/postgresql` が既定のデータベース格納場所であり、こ
れをホスト側で管理したい場合には bind-mount を適宜指定する。ホスト側のディレクト
リーは前もって手動で作成しておく。

Docker Hub 公式イメージ README によると :file:`/var/lib/postgresql` にマウントす
る場合、:file:`/var/lib/postgresql/data` はコンテナーランタイムからのローカルボ
リュームであるため、マウントされたボリューム上にデータは永続化されないと文書にあ
る。

.. sourcecode:: console
   :caption: :file:`/path/to` は差し当たり ``$(pwd)`` にしておけ

   $ docker run -d \
       --name some-postgres \
       -e POSTGRES_PASSWORD=secret \
       -e PGDATA=/var/lib/postgresql/data/pgdata \
       --mount type=bind,source=/path/to/datadir,target=/var/lib/postgresql/data \
       postgres

この結果、ホスト側ファイルシステム部分である :file:`./data/pgdata` にデータベー
ス実体が保存される。コンテナーをいったん廃棄して再度この ``docker run`` コマンド
を実行すると、データベースが維持できていることが確認できる。

.. admonition:: 利用者ノート

   :file:`./data/pgdata` の所有権表記が ``999 root`` になる。コンテナーの
   :file:`/etc/passwd` を確認するとユーザー ``postgres`` に相当する。

.. rubric:: まとめ

.. sourcecode:: console
   :caption: ここまでの諸々をまとめたコンテナー稼働コマンド

   $ docker run -d \
       --name some-postgres \
       -e POSTGRES_PASSWORD=secret \
       -e PGDATA=/var/lib/postgresql/data/pgdata \
       --mount type=bind,source=$PWD/datadir,target=/var/lib/postgresql/data \
       --mount type=bind,source=$PSQLRC,target=/var/lib/postgresql/.psqlrc,readonly \
       postgres

こんなコマンドを毎回書いていられないので Docker Compose を利用する。ファイル
:file:`compose.yaml` を次のような内容で用意：

.. sourcecode:: yaml
   :caption: Example of :file:`compose.yaml`

   services:
     postgres:
       container_name: some-postgres
       image: postgres
       environment:
         PGDATA: /var/lib/postgresql/data/pgdata
         POSTGRES_USER: postgres
         POSTGRES_PASSWORD: secret
       volumes:
         - type: bind
           source: ${PWD}/datadir
           target: /var/lib/postgresql/data
         - type: bind
           source: ${PSQLRC}
           target: /var/lib/postgresql/.psqlrc
           read_only: true

これで ``docker compose up -d`` や ``docker compose down`` が利用可能になる。

.. rubric:: コンテナーを廃棄する

PostgreSQL コンテナーが用済みになったらそれを削除することでデータベースも消去さ
れる。失いたくない場合には ``docker run`` の段階でマウントなどを指定するか、コン
テナーにあるデータベースをホスト側に退避させるのだろう。

.. sourcecode:: console
   :caption: コンテナーを処分するコマンド例

   $ docker stop some-postgres
   $ docker rm some-postgres

ディスクに余裕がなければイメージも削除する。

----

ネットワークや Dockerfile など、未実施の項目が残っているが、ひとまず終わる。
