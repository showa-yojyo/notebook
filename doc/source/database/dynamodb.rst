======================================================================
Amazon DynamoDB 利用ノート
======================================================================

:Since: 2012
:Official site: <https://aws.amazon.com/dynamodb/>
:CLI: AWS Command Line Interface (AWS CLI); :command:`aws`

まずは `開発者向け文書
<https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/>`__ にざっと
目を通しておけ。

インストール手順は次のようなものだ。あらかじめ適当なディレクトリーに移動しておく
こと：

.. code:: console

   $ curl -O https://d1ni2b6xgvw0s0.cloudfront.net/v2.x/dynamodb_local_latest.tar.gz
   $ tar xvzf dynamodb_local_latest.tar.gz --one-top-level dynamodb

サービス稼動方法はこう：

.. code:: console

   $ cd dynamodb
   $ java -D"java.library.path=./DynamoDBLocal_lib" -jar DynamoDBLocal.jar -sharedDb
   Initializing DynamoDB Local with the following configuration:
   Port:   8000
   InMemory:       false
   DbPath: null
   SharedDb:       true
   shouldDelayTransientStatuses:   false
   CorsParams:     null

こうして起動した場合は停止手順は :kbd:`Ctrl` + :kbd:`C` で良い。

実はまだサービスを稼動する条件が整っていない。並行して AWS Command Line
Interface (AWS CLI) をインストールする：

.. code:: console

   $ curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
   $ unzip awscliv2.zip
   $ sudo ./aws/install
   $ aws --version
   aws-cli/2.14.5 Python/3.11.6 Linux/5.15.133.1-microsoft-standard-WSL2 exe/x86_64.ubuntu.22 prompt/off
   $ aws configure
   AWS Access Key ID [None]: fakeMyKeyId
   AWS Secret Access Key [None]: fakeSecretAccessKey
   Default region name [None]: ap-northeast-1
   Default output format [None]: json
   $ aws dynamodb list-tables --endpoint-url http://localhost:8000
   {
       "TableNames": []
   }

ここまで上手く行ったら Developer Guide Getting started with DynamoDB に記載され
ている ``aws dynamodb`` から始まるコマンドを試す。ダウンロード版 DynamoDB を利用
するため、掲載されているコマンドのすべてに対してオプション ``--endpoint-url
http://localhost:8000`` を追加的に指定する必要が本来ある。ここで、その代わりとな
る環境変数を設定する：

.. code:: console

   $ export AWS_ENDPOINT_URL=http://localhost:8000

Get started の章で試せるコマンド群を列挙しておく。`先頭の `aws dynamodb`` は省略
する：

* ``create-table``
* ``describe-table``
* ``update-continuous-backups``: UnknownOperationException
* ``put-item``
* ``get-item``
* ``update-item``
* ``update-table``
* ``query``
* ``delete-table``

操作によっては ``execute-statement`` コマンドを実行する別解もある。例えば

.. code:: console

   $ aws dynamodb query \
     --table-name Music \
     --key-condition-expression "Artist = :name" \
     --expression-attribute-values '{":name":{"S":"Acme Band"}}'

は次のコマンド実行でも同じ出力を得る：

.. code:: console

   $ aws dynamodb execute-statement --statement "SELECT * FROM Music
     WHERE Artist='Acme Band'"

.. admonition:: 読者ノート

   チュートリアルの最後がテーブル削除であるのが素晴らしい。データベースがチュー
   トリアル開始直前と同じ状態に戻して終了することを意味するのだから。

Getting started with DynamoDB and the AWS SDKs の実習は Python からやりたい。文
書にあるように GitHub リポジトリーを丸ごと clone してもよいが、要所を示すために
必要最低限のファイルを手作業でダウンロード、環境構築、デモ実施をする手順の概略を
次に示す：

.. code:: console

   $ mkdir -p sandbox-dynamodb/python/GettingStarted
   $ cd sandbox-dynamodb/python
   $ AWSDOCS_URL=https://raw.githubusercontent.com/awsdocs/aws-doc-sdk-examples/main/python/example_code/dynamodb
   $ curl -O ${AWSDOCS_URL}/README.md
   $ curl -O ${AWSDOCS_URL}/requirements.txt
   $ cd GettingStarted
   $ curl -O ${AWSDOCS_URL}/GettingStarted/scenario_getting_started_movies.py
   $ curl -O ${AWSDOCS_URL}/GettingStarted/question.py
   $ cd ..
   $ python -m venv .venv
   $ source .venv/bin/activate
   $ pip install -r requirements.txt
   $ python GettingStarted/scenario_getting_started_movies.py
   $ deactivate

これで対話的なアプリケーションが開始する。README をよく読まなくても、Python コー
ドで DynamoDB にアクセスできていることが納得できる。
