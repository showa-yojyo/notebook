======================================================================
MongoDB 利用ノート
======================================================================

:Since: 2007
:Official site: `MongoDB <https://www.mongodb.com/>`__
:Service: :program:`mongod` 7.0.3
:CLI: :program:`mongosh` 2.0.2

何かのチュートリアルでインストールされた旧版 MongoDB をファイルシステムから撤去
するのに手間取る。旧版を完全に払拭しないと :program:`apt` によるバージョン 7.0
のインストールが歪む。その作業を含めたインストール手順は次の文書に記されている：
`Install MongoDB Community Edition on Ubuntu
<https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/>`__

インストール後、サービスを手動で稼動させる。Ubuntu の場合には :program:`service`
を用いる：

.. code:: console

   $ sudo service mongodb start
    * Starting database mongod                           [ OK ]
   $ sudo service mongodb status
    * Checking status of database mongod
   /etc/init.d/mongodb: 251: log_successs_msg: not found

サービスを停止するには：

.. code:: console

   $ sudo service mongodb stop
    * Stopping database mongod                           [ OK ]

サービス稼働中ならば :command:`mongosh` を実行して対話シェルを稼動可能。以下、
ローカルホストでの稼動を仮定する。

エディターなどの MongoDB Shell 設定をカスタマイズするといい。構成内容は JSON 形
式でファイル :file:`$HOME/.mongodb/mongosh/config` に保存される。現在のところ
XDG 未対応で、Git などによるバージョン管理が面倒だ。

入門として W3Schools の次のチュートリアルの前半をまず行う：
`MongoDB Tutorial <https://www.w3schools.com/mongodb/index.php>`__

中盤から出来合いのデータベースを用いる。そのため避けていた Atlas に触れざるを得
ない。アカウントを作成するときに氏名を求められるのが怖いので、ここで学習を中止す
る。

次のリポジトリーを ``git clone`` してスクリプトを実行すると、チュートリアルの続
きを少しは実施可能になる： `neelabalan/mongodb-sample-dataset: sample dataset
used in mongodb atlas cluster for local testing purpose
<https://github.com/neelabalan/mongodb-sample-dataset>`__

インデックス作成法辺りから迷子になる。
