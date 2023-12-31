======================================================================
基本技法
======================================================================

本節では PTT を利用して Twitter API を操作するときに共通するコードの書き方の要領
を記す。 Twitter の API には大きく分けて REST と Streaming の二つがあるが、リク
エストの送信手順や受信データの反復処理のように、用いる機能に係わりなく同じ手法を
適用する場合がかなりある。ここではそのような手法を項目別にまとめておく。

.. contents:: ノート目次

概要
======================================================================

PTT を利用するプログラムに共通する手続きを図示するとこのようになる。

#. 認証キー等を用意する
#. ``OAuth`` オブジェクトを生成する
#. ``Twitter`` オブジェクトまたは ``TwitterStream`` オブジェクトを生成する
#. Twitter API を利用する

明らかに API を利用するまでの手続きがワンパターンなので、どこかにカプセル化して
おくべきだろう。次節ではそのパターンの例を示す。

Twitter API の利用法は当然ながらリクエストごとに異なるのが普通だが、取得データの
構造が似通っているため、その処理手順も似通っていくる。カーソル処理等、取得データ
を処理するための技法で頻出するものを本章の後半で述べる。

認証処理およびインターフェイス準備処理
======================================================================

PTT を利用するプログラムに共通して書く必要のあるコードは次のようなものである。認
証と Twitter 本体とのインターフェイスとなるインスタンスのセットアップからなる。

.. code:: python3

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

* [1] Twitter の開発者ページで入手した、実際の API key と API secret の文字列を
  それぞれに定義する。ここでは説明用にハードコードしている。
* [2] 唐突に :file:`$HOME/.my_app_credentials` なるファイルが登場する。このファ
  イルは内容が Access token と Access token secret の実際の文字列二行からなる設
  定ファイルである。

  この設定ファイルは初回のみ PTT が生成してくれる。正確に挙動を言うと、その前に
  関数 ``oauth_dance`` がウェブブラウザーをアクティブにする。ここでアカウント情
  報を入力して OK すると、PIN コードというものをブラウザー画面に表示する。この
  コードをコンソールに戻って入力すると、設定ファイルが生成されるという流れだ。

* [3] 認証オブジェクトを生成する。クラス ``OAuth`` のコンストラクターを直接利用
  する。
* [4] Twitter API のインターフェイスオブジェクトを ``auth`` を指定して生成する。
  REST API を利用する場合はクラス ``Twitter`` を、Streaming API を利用する場合は
  クラス ``TwitterStream`` を用いて、オブジェクトをコンストラクターから生成す
  る。

  Streaming の場合はコンストラクターに引数を渡すことになるはずだ。詳しくは
  Streaming API の演習ノートで説明する。

さて、使い捨てのスクリプトで毎回上のようなコードをコピーアンドペーストするのはプ
ログラマーの美学に反する。そこで、一連の手順をモジュール化して ``PYTHONPATH`` の
パスリストのどこかに安置しておくことを勧める。私の例を示す。

#. まず、下記コードを :file:`secret.py` として :file:`$HOME/my-python-modules`
   保存する。

   .. literalinclude:: /_sample/ptt/secret.py_t
      :language: python3

#. Windows のユーザー環境変数設定で ``PYTHONPATH`` の値に
   ``%%HOME%%\my-python-modules`` を含める。
#. PTT を利用する使い捨てのスクリプトの構造を次のようにする。

   .. code:: python3

      from secret import twitter_instance

      tw = twitter_instance()
      ...

リクエスト結果オブジェクトの出力処理
======================================================================

Twitter にリクエストを送信すると、原則的にその結果を JSON データとして受信する。
Python 的には単に組み込みのコンテナーオブジェクトに変換されている節があるので、
その辺をうまく加工して画面にテキストを出力するようにしたい。

.. code:: python3

   response = tw.statuses.user_timeline(**kwargs)

この ``response`` をいい感じに出力するのに私が使う方法を次に挙げる。

* 組み込みの関数 ``print`` プラス文字列メソッド ``format``
* 関数 ``pprint.pprint``
* 関数 ``json.dump``

これらを状況に応じて使い分ける。取得データのごく一部を抽出したい場合にはメソッド
``format`` で欲しいフィールドのみを出力する。データ構造を保持したままデータを見
たり保存する場合には、後者二つを用いる。

特殊なパラメーター ``id``
======================================================================

Twitter のインターフェイスでパラメーター名が ``id`` であるものがいくつかある。
PTT ではこれを ``_id`` と呼び変えて値を渡すのが無難だ。

特にコロンが機能名に入るものに注意を要する。次にメソッドの呼び出し方法をまとめて
おく。

* GET geo/id/:place_id -> ``tw.geo.id._id(_id=xxxx)``
* POST saved_searches/destroy/:id -> ``tw.saved_searches.destroy(_id=xxxx)``
* GET saved_searches/show/:id -> ``tw.saved_searches.show._id(_id=xxxx)``
* POST statuses/destroy/:id -> ``tw.saved_searches.destroy._id(_id=xxxx)``
* POST statuses/retweet/:id -> ``tw.statuses.retweet._id(_id=xxxx)``
* GET statuses/retweets/:id -> ``tw.statuses.retweets._id(_id=xxxx)``
* GET statuses/show/:id -> ``tw.statuses.show(_id=xxxx)``
* GET users/suggestions/:slug, GET users/suggestions/:slug/members -> :doc:`./rest-users` 参照

ページング処理
======================================================================

ここからは PTT のメソッドを利用して Twitter の自分のアカウントを対象とするの操作
を試していく。本稿のサンプルコードは前述の共通処理をカットしているので、読者は注
意して欲しい。

さっそくタイムラインの取得処理から見ていこう。まずは、コードを書く前に Twitter
本家ドキュメントの `Working with Timelines
<https://dev.twitter.com/rest/public/timelines>`_ を一読して、API がツイートの
データ構造をどのように定義しているのかをおおまかに理解しておこう。

特徴的なのは、``statuses/user_timeline`` や ``lists/statuses`` 等の「大量のツ
イートを返す」ような API を利用する場合には、一度のリクエストでデータを一括取得
するのではなく、リクエストを複数回に分けて行い、その際に ``max_id`` や
``since_id`` 引数を適宜指定して利用するという技法が一般的らしいということが理解
できる。パターンとしては次の二通りしかないので、レスポンスの処理技法を習得するの
は容易い。

ツイート日時の新しいものから、順次古い方向へ取得していくケース
----------------------------------------------------------------------

一般的な Twitter クライアントでは、タイムラインはツイートが上から下に新しい順に
並んでいる。この画面を下方向にスクロールしたときに、より古いツイートを動的にリク
エストするようになっている。実質的には次に説明するようなことを行なっているハズ
だ。

* 初回リクエスト。レスポンス中のツイート群の ``id`` の最小値をプログラム側で記憶
  する。
* 次回リクエスト。このとき引数の ``max_id`` を明示的に指示する。

コードを示す。

.. code:: python3

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

レスポンス中のツイートは ``id`` という値を保持しており、ツイートは ``id`` が降順
になるように配列された状態で戻ってきている。その事実を利用すれば ``id`` の最大・
最小が得られる。配列の先頭ツイートの ``id`` が最大であり、末尾ツイートのそれが最
小であるはずだ。

三回目以降のリクエストも同様に繰り返す。

なお、本当に上のようなループを書くといつ終わるのかがわからない。アプリケーション
側で適宜条件 ``XXX`` を定義することだ。

取得済みのツイートの「上」に、最新のツイートを取得するケース
----------------------------------------------------------------------

一般的な Twitter クライアントでは、ビューにタイマーが仕込んであり、例えば 60 秒
毎に最新のツイートをリクエストしてタイムラインを更新するものが多い。

おそらく、次のようなアルゴリズムを実行している：

* 初回リクエスト。レスポンス中のツイート群の ``id`` の最大値をプログラム側で記憶
  する。
* 次回リクエスト。このとき引数の ``since_id`` を明示的に指示する。

前項コードとの差分だけを示そう。

.. code:: python3

   max_id = response[0]['id']
   kwargs['since_id'] = max_id

なお、実際に Twitter アプリケーションを作成するのであれば、本項と前項の処理を同
時に実装するのが効率的だし自然だ。

カーソル処理
----------------------------------------------------------------------

``cursor`` という名前の optional 引数がある API については、次のような手順でペー
ジング処理と同等のことを実現する。

* 初回取得では ``cursor`` 引数を ``-1`` に指示すること。
* 二回目以降取得では、``cursor`` の値として前回レスポンス中の ``next_cursor``
  または ``previous_cursor`` を指示する。通常は前者を用いる。

  その際、値がゼロでないことを確認する必要がある。ゼロは取得するべきデータは
  Twitter に存在しないということを示唆している。

擬似コードを示す。ここで ``kwargs`` は API に渡す引数を保持する ``dict`` オブ
ジェクトであり、``process_something`` は Twitter からの応答オブジェクトを処理す
る関数か何かを意味する。

.. code:: python3

   next_cursor = -1
   while next_cursor:
       response = tw.friends.ids(
           cursor=next_cursor,
           **kwargs)

       process_response(response)

       next_cursor = response['next_cursor']

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-twitter.txt
