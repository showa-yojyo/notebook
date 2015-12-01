======================================================================
演習 (REST API)
======================================================================
本節では PTT を利用して Twitter REST API を操作するときのコツのようなものを記す。
Twitter の API には大きく分けて REST と Streaming のふたつがある。
前者がより基本的なインターフェイスのようなので、先に見ていく。

.. contents:: ノート目次

概要
======================================================================
PTT を利用するプログラムに共通する手続きを図示するとこのようになる。

#. 認証キー等を用意する
#. ``OAuth`` オブジェクトを生成する
#. ``Twitter`` オブジェクトまたは ``TwitterStream`` オブジェクトを生成する
#. Twitter API を利用する

明らかに API を利用するまでの手続きがワンパターンなので、どこかにカプセル化しておくべきだろう。
次節ではそのパターンの例を示す。

Twitter API の利用法は当然ながらリクエストごとに異なるのが普通だが、
取得データの構造が似通っているため、その処理手順も似通っていくる。
カーソル処理等、取得データを処理するための技法で頻出するものを本章の後半で述べる。

認証処理およびインターフェイス準備処理
======================================================================
PTT を利用するプログラムに共通して書く必要のあるコードは次のようなものである。
認証と Twitter 本体とのインターフェイスとなるインスタンスのセットアップからなる。

.. code-block:: python3

   from twitter import *

   # [1]
   CONSUMER_KEY = '**********************'  # API key
   CONSUMER_SECRET = '******************************************' # API secret; Keep this value secret.

   # [2]
   MY_TWITTER_CREDS = os.path.expanduser('~/.my_app_credentials')
   if not os.path.exists(MY_TWITTER_CREDS):
       oauth_dance("My App Name", CONSUMER_KEY, CONSUMER_SECRET, MY_TWITTER_CREDS)

   oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)

   # [3]
   auth = OAuth(oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET)

   # [4]
   t = Twitter(auth=auth)

   # Use Twitter APIs via `t`...

* [1] Twitter の開発者ページで入手した、
  実際の API key と API secret の文字列をそれぞれに定義する。
  ここでは説明用にハードコードしている。

* [2] 唐突に :file:`$HOME/.my_app_credentials` なるファイルが登場する。
  このファイルは内容が Access token と Access token secret の実際の文字列 2 行からなる設定ファイルである。

  この設定ファイルは初回のみ PTT が生成してくれる。
  正確に挙動を言うと、その前に関数 ``oauth_dance`` がウェブブラウザーをアクティブにする。
  ここでアカウント情報を入力して OK すると、PIN コードというものをブラウザー画面に表示する。
  このコードをコンソールに戻って入力すると、設定ファイルが生成されるという流れだ。

* [3] 認証オブジェクトを生成する。
  クラス ``OAuth`` のコンストラクターを直接利用する。

* [4] Twitter API のインターフェイスオブジェクトを ``auth`` を指定して生成する。
  REST API を利用する場合はクラス ``Twitter`` を、
  Streaming API を利用する場合はクラス ``TwitterStream`` を用いて、
  オブジェクトをコンストラクターから生成する。

  Streaming の場合はコンストラクターに引数を渡すことになるはずだ。
  詳しくは Streaming API の演習ノートで説明する。

さて、使い捨てのスクリプトで毎回上のようなコードをコピーアンドペーストするのはプログラマーの美学に反する。
そこで、一連の手順をモジュール化して ``PYTHONPATH`` のパスリストのどこかに安置しておくことを勧める。
私の例を示す。

#. まず、下記コードを :file:`secret.py` として :file:`$HOME/my-python-modules` 保存する。

   .. literalinclude:: /_sample/ptt/secret.py
      :language: python3

#. Windows のユーザー環境変数設定で ``PYTHONPATH`` の値に ``%%HOME%%\my-python-modules`` を含める。
#. PTT を利用する使い捨てのスクリプトの構造を次のようにする。

   .. code-block:: python3

      from secret import twitter_instance

      tw = twitter_instance()
      ...

ページング処理
======================================================================
ここからは PTT のメソッドを利用して Twitter の自分のアカウントを対象とするの操作を試していく。
本稿のサンプルコードは前述の共通処理をカットしているので、読者は注意して欲しい。

さっそくタイムラインの取得処理から見ていこう。
まずは、コードを書く前に Twitter 本家ドキュメントの
`Working with Timelines <https://dev.twitter.com/rest/public/timelines>`_ を一読して、
API がツイートのデータ構造をどのように定義しているのかをおおまかに理解しておこう。

特徴的なのは、``statuses/user_timeline`` や ``lists/statuses`` 等の
「大量のツイートを返す」ような API を利用する場合には、
一度のリクエストでデータを一括取得するのではなく、リクエストを複数回に分けて行い、
その際に ``max_id`` や ``since_id`` 引数を適宜指定して利用するという技法が一般的らしいということが理解できる。
パターンとしては次の二通りしかないので、レスポンスの処理技法を習得するのは容易い。

ツイート日時の新しいものから、順次古い方向へ取得していくケース
----------------------------------------------------------------------
一般的な Twitter クライアントでは、タイムラインはツイートが上から下に新しい順に並んでいる。
この画面を下方向にスクロールしたときに、
より古いツイートを動的にリクエストするようになっている。
実質的には次に説明するようなことを行なっているハズだ。

* 初回リクエスト。レスポンス中のツイート群の ``id`` の最小値をプログラム側で記憶する。
* 次回リクエスト。このとき引数の ``max_id`` を明示的に指示する。

コードを示す。

.. code-block:: python3

   kwargs = dict(
       screen_name='showa_yojyo',
       count=20,
       page=1,
       include_entities=1,
       include_rts=1,
       exclude_replies=0)

   while XXX:
       response = tw.statuses.user_timeline(**kwargs)
       if not response:
           break

       process_response(response)

       min_id = response[-1]['id']
       kwargs['max_id'] = min_id - 1

レスポンス中のツイートは ``id`` という値を保持しており、
ツイートは ``id`` が降順になるように配列された状態で戻ってきている。
その事実を利用すれば ``id`` の最大・最小が得られる。
配列の先頭ツイートの ``id`` が最大であり、
末尾ツイートのそれが最小であるはずだ。

3 回目以降のリクエストも同様に繰り返す。

なお、本当に上のようなループを書くといつ終わるのかがわからない。
アプリケーション側で適宜条件 ``XXX`` を定義することだ。

取得済みのツイートの「上」に、最新のツイートを取得するケース
----------------------------------------------------------------------
一般的な Twitter クライアントでは、ビューにタイマーが仕込んであり、
例えば 60 秒毎に最新のツイートをリクエストしてタイムラインを更新するものが多い。

おそらく、次のようなアルゴリズムを実行している。

* 初回リクエスト。レスポンス中のツイート群の ``id`` の最大値をプログラム側で記憶する。
* 次回リクエスト。このとき引数の ``since_id`` を明示的に指示する。

前項コードとの差分だけを示そう。

.. code-block:: python3

   max_id = response[0]['id']
   kwargs['since_id'] = max_id

なお、実際に Twitter アプリケーションを作成するのであれば、
本項と前項の処理を同時に実装するのが効率的だし自然だ。

カーソル処理
----------------------------------------------------------------------
``cursor`` という名前の optional 引数がある API については、
次のような手順でページング処理と同等のことを実現する。

* 初回取得では ``cursor`` 引数を ``-1`` に指示すること。

* 二回目以降取得では、
  ``cursor`` の値として前回レスポンス中の ``next_cursor`` または
  ``previous_cursor`` を指示する。
  通常は前者を用いる。

  その際、値がゼロでないことを確認する必要がある。
  ゼロは取得するべきデータは Twitter に存在しないということを示唆している。

擬似コードを示す。
ここで ``kwargs`` は API に渡す引数を保持する ``dict`` オブジェクトであり、
``process_something`` は Twitter からの応答オブジェクトを処理する関数か何かを意味する。

.. code-block:: python3

   next_cursor = -1
   while next_cursor != 0:
       response = tw.friends.ids(
           cursor=next_cursor,
           **kwargs)

       process_response(response)

       next_cursor = response['next_cursor']

API 別コード例
======================================================================
以下、PTT をツールとして Twitter の REST API を操作するためのコード例を記す。

.. toctree::
   :glob:
   :maxdepth: 2

   rest-*

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-twitter.txt
