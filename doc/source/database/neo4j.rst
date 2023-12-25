======================================================================
Neo4j 利用ノート
======================================================================

:Since: 2010
:Official site: <https://neo4j.com/>
:CLI: :program:`cypher-shell`
:Server Version: 5.14.0
:Browser Version: 5.12.0

Neo4j Community Edition インストール手順を記す。場合によっては Java の調整を行う
ことがある（説明割愛）。

.. code:: console

   $ sudo apt update && suto apt upgrade -y
   $ curl -fsSL https://debian.neo4j.com/neotechnology.gpg.key | sudo gpg --dearmor -o /usr/share/keyrings/neo4j.gpg
   $ echo 'deb https://debian.neo4j.com stable latest' | sudo tee -a /etc/apt/sources.list.d/neo4j.list
   $ sudo apt-get update
   $ apt list -a neo4j
   $ sudo apt install neo4j=1:5.14.0

管理者アカウントの初期パスワードを明示的に設定変更する必要があるようで、次のコマ
ンドによる。:samp:`{XXXXXX}` 部分を適宜指定する：

.. code:: console

   $ sudo neo4j-admin dbms set-initial-password XXXXXX
   [sudo] password for work:
   Changed password for user 'neo4j'. IMPORTANT: this change will only take effect if performed before the database is started for the first time.

Neo4j サービスを稼動する方法は複数ある：

* Ubuntu につき :program:`service` から起動する
* ``sudo neo4j start`` を実行する

.. code:: console

   $ sudo service neo4j start
   Directories in use:
   home:         /var/lib/neo4j
   config:       /etc/neo4j
   logs:         /var/log/neo4j
   plugins:      /var/lib/neo4j/plugins
   import:       /var/lib/neo4j/import
   data:         /var/lib/neo4j/data
   certificates: /var/lib/neo4j/certificates
   licenses:     /var/lib/neo4j/licenses
   run:          /var/lib/neo4j/run
   Starting Neo4j.
   Started neo4j (pid:xxxxx). It is available at http://localhost:7474

停止する方法はそれぞれに対応する ``stop`` コマンドを用いる。

.. admonition:: 読者ノート

   この URL をブラウザーで開くと empty response だの connection refused だのエ
   ラーが出る。一方、コンソールから :program:`curl` などで応答を受信すると、サー
   バーは稼働していることがわかる。

   サーバーをいったん停止して、構成ファイル :file:`/etc/neo4j/neo4j.conf` を管理
   者権限で編集することで解決する。次の行のコメントアウトを外せ：

   .. code:: shell

      # With default configuration Neo4j only accepts local connections.
      # To accept non-local connections, uncomment this line:
      #server.default_listen_address=0.0.0.0

   次にサービスを稼動すると、<http://localhost:7474/browser/> をブラウザーで開くこ
   とで Neo4j 画面が出るはずだ。

とりあえず作業ユーザーを作成する：

.. code:: console

   $ cypher-shell
   username: neo4j
   password:
   Connected to Neo4j using Bolt protocol version 5.4 at neo4j://localhost:7687 as user neo4j.
   Type :help for a list of available commands or :exit to exit the shell.
   Note that Cypher queries must end with a semicolon.
   neo4j@neo4j> create user XXXXXXXX set password YYYYYYY change not required;
   0 rows
   neo4j@neo4j> :exit

   Bye!

作業ユーザーが用意できたらブラウザーで作業する。上述の URL を開いて Neo4j の画面
が出たら作業ユーザーでログインしろ。:guilabel:`User database` を
:guilabel:`neo4j` に合わせろ。Neo4j Browser Guides を素直に全部読め。構文の詳細
を理解するのは後回しにして、ツールの使い方に慣れろ。

.. tip::

   Neo4j Browser でよく実行するコマンドを :guilabel:`Save as Faivorite` しておく
   のがよい。

   * ``MATCH (n) RETURN n``
   * ``MATCH (n) DETACH DELETE n``

ガイドを追えたら接続を解除してブラウザーを閉じてよい。

次に `Neo4j Tutorial <https://www.tutorialspoint.com/neo4j/>`__ もこなしてみる。
若干古いバージョン向けの教材らしく、コマンドの一部は書き改めないと動作しない。こ
れを調べながら動作させつつ進め。

アンインストール手順は ``sudo apt uninstall neo4j`` 実行とファイルシステムの整頓
でいいか。
