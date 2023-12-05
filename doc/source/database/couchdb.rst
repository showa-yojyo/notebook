======================================================================
Apache CouchDB 利用ノート
======================================================================

:Since: 2005
:Official site: <https://couchdb.apache.org/>
:Version: 3.3.2
:CLI: 専用ツールなし

Sphinx で記述された公式文書 `Apache CouchDB® 3.3 Documentation
<https://docs.couchdb.org/en/stable/>`__ の品質が良く、インストール手順で詰まるこ
とはないはずだ。

.. code:: console

   $ curl https://couchdb.apache.org/repo/keys.asc |
     gpg --dearmor |
     sudo tee /usr/share/keyrings/couchdb-archive-keyring.gpg >/dev/null 2>&1
   $ . /etc/os-release  # $VERSION_CODENAME が欲しい
   $ echo "deb [signed-by=/usr/share/keyrings/couchdb-archive-keyring.gpg] https://apache.jfrog.io/artifactory/couchdb-deb/ ${VERSION_CODENAME} main" |
     sudo tee /etc/apt/sources.list.d/couchdb.list >/dev/null
   $ sudo apt update
   $ sudo apt install -y couchdb

インストール中、対話形式での手順は次の記事を参照： `How to Install Apache
CouchDB in Ubuntu 22.04
<https://www.geekbits.io/how-to-install-apache-couchdb-in-ubuntu-22-04/>`__

サービスを手動で稼働する。別のコンソールウィンドウで実施するか、バックグラウンド
実行すると何かの時に小回りが利く：

.. code:: console

   $ service couchdb status
   $ sudo -i -u couchdb /opt/couchdb/bin/couchdb

.. admonition:: 読者ノート

   まともなサービス停止方法が判明していない。現状 :command:`kill` コマンドで強引
   に殺している。

   .. code:: console

      $ su couchdb service couchdb stop
      Password:
       * Stopping Apache CouchDB couchdb
      start-stop-daemon: pid value must be a number greater than 0
      Try 'start-stop-daemon --help' for more information.
      $ sudo start-stop-daemon --stop --user couchdb

サービス稼働中に管理者権限を有するアカウントを作成する：

.. code:: console

   $ COUCHDB_HOST=http://admin:${ADMIN_PASSWORD}@localhost:5984
   $ curl -X PUT ${COUCHDB_HOST}/_node/couchdb@127.0.0.1/_config/admins/${NEW_USER} -d '"${NEW_PASSWORD}"'

ここまで準備が整ったらチュートリアルを実施する。アカウントは今作成したものに変え
て、変数の値もそれに合わせる。

.. code:: console

   $ curl http://localhost:5984/
   $ COUCHDB_HOST=http://${NEW_USER}:${NEW_PASSWORD}@localhost:5984
   $ curl -X GET ${COUCHDB_HOST}/_all_dbs
   $ curl -X PUT ${COUCHDB_HOST}/my_database
   $ curl -s -X GET ${COUCHDB_HOST}/test | jq .

この辺で Fauxton と呼ばれているブラウザーインターフェイス
<http://127.0.0.1:5984/_utils/> にアクセス可能となる。コンソールからブラウザーへ
移動しろ。

`Getting Started - CouchDB: The Definitive Guide <https://guide.couchdb.org/draft/tour.html>`__
  ブラウザー画面が少々異なるが、学習可能。
`CouchDB Tutorial <https://www.tutorialspoint.com/couchdb/>`__
  バージョンが古いが学習可能。:program:`curl` とブラウザーの両方について方法が述
  べられている。``rev`` の意味、更新、ローカルファイル添付（アップロード）を習得
  可能。
`CouchDB tutorial - W3schools <https://www.w3schools.blog/couchdb-tutorial>`__
  Fauxton 対応。Python や JavaScript (Node.js) などから CouchDB にアクセスする方
  法に関する記述もある。
