======================================================================
Python Twitter Tools 利用ノート
======================================================================

Twitter をたしなむ Python プログラマーならば、Twitter API を Python で操ろうと考えるのは当然なことだ。
ここでは Mike Verdone 氏開発による `Python Twitter Tools`_ (hereafter PTT) パッケージを利用した Twitter 操作を色々と見ていく。

.. contents:: ノート目次

.. note::

   * OS

     * Windows XP Home Edition SP 3
     * Windows 7 Home Premium SP 1

   * 本稿において、利用した各パッケージのバージョンは次のとおり。

     * Python_: 2.6.6, 2.7.3, 3.4.1
     * `Python Twitter Tools`_: 1.7.2, 1.8.0, 1.9.0, 1.14.3

関連リンク
======================================================================
`Python Twitter Tools`_
  著者ウェブページ。開発ページは別にある。

`REST API v1.1 Resources`_
  Twitter 本家ドキュメント。

前準備
======================================================================

インストール
----------------------------------------------------------------------
PTT のインストールはいつものように pip で構わない。

.. code-block:: console

   $ pip install twitter

本パッケージ配布版には単体テストコードのようなものはない。
インストールが無事に終わったことを知りたいのならば、
``import twitter`` の確認で我慢する。

.. code-block:: console

   $ python34 -c 'import twitter; help(twitter)'

ドキュメント
----------------------------------------------------------------------
PTT のドキュメントよりも重要なのは Twitter API 自身のドキュメントであるので、
`REST API v1.1 Resources`_ 等のウェブページを見ながら Python コードを書くことになる。

認証トークン入手
----------------------------------------------------------------------
* Twitter API は OAuth という認証を利用している。
  このため、API key および API secret と呼ばれる文字列が必要となる。
  API v1.0 では一部 GET 系は認証なしで利用できる API もあったが、v1.1 からはすべての API で要認証となった。

  * これらの文字列を入手するには、
    https://dev.twitter.com/apps 以降のページ群であらかじめ手続きを済ませる。
  
    * ウェブブラウザーと Twitter アカウントを持っていることが必要である。
    * Create an application というページに入力フォームがある。
      入力後、画面下部のボタンを押せば多分出てくるだろう。

* 次に Access token および Access token secret という、別の一対の文字列が必要だ。

  * これらの文字列を得るために、先ほどの文字列が必要となる。

  * Google で ``get_access_token`` 等検索してヒットする、
    ネットに落ちているスクリプトを一部改変して実行する。
    コードを見れば手を入れる箇所は理解できるハズ。

* 上記 4 つの文字列を入手できて初めて Twitter API v1.1 が利用可能となる。

コード例
======================================================================
以下、個人的に動作確認が取れた状況でのコードのみをノートしておく。
細かい説明を重ねるよりは、動作したコードを淡々と列挙して、
見返したときにすぐに思い出せるようにする。

共通処理コード
----------------------------------------------------------------------
PTT を利用するプログラムに共通して書く必要のあるコードは次のようなものである。
認証と Twitter 本体とのインターフェイスとなるインスタンスのセットアップからなる。

.. code-block:: python3

   # PTT 利用プログラムに共通して書くことになる処理
   from twitter import *

   # Comment 1
   CONSUMER_KEY = '**********************'  # API key
   CONSUMER_SECRET = '******************************************' # API secret; 人に見せてはいけない。

   # Comment 2
   MY_TWITTER_CREDS = os.path.expanduser('~/.my_app_credentials')
   if not os.path.exists(MY_TWITTER_CREDS):
       oauth_dance("My App Name", CONSUMER_KEY, CONSUMER_SECRET, MY_TWITTER_CREDS)

   oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)

   t = Twitter(auth=OAuth(
       oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET))

   # ... t を介した Twitter 操作コード ...

Comment 1
  Twitter の開発者ページで入手した、実際の API key と API secret の文字列をそれぞれに定義する。
  ここでは説明用にハードコードしている。

Comment 2
  唐突に :file:`$HOME/.my_app_credentials` なるファイルが登場する。
  このファイルは内容が Access token と Access token secret の実際の文字列 2 行からなる設定ファイルである。
  この設定ファイルは一度だけ自分で用意すればよい。

さて、使い捨てのスクリプトで毎回上のようなコードをコピーアンドペーストするのはプログラマーの美学に反する。
そこで、一連の手順をモジュール化して ``PYTHONPATH`` のパスリストのどこかに安置しておくことを勧める。
私の例を示す。

#. まず、下記コードを :file:`secret.py` として :file:`$HOME/my-python-modules` 保存する。

   .. code-block:: python3

      # -*- coding: utf-8 -*-
      from twitter import *
      import os

      CONSUMER_KEY = '**********************'
      CONSUMER_SECRET = '******************************************'
      USER_KEY = '*********-****************************************'
      USER_SECRET = '*****************************************'

      MY_TWITTER_CREDS = os.path.expanduser('~/.my_app_credentials')

      def twitter_instance():
          """Setup an instance of class Twitter."""

          if not os.path.exists(MY_TWITTER_CREDS):
              oauth_dance("My App Name", CONSUMER_KEY, CONSUMER_SECRET, MY_TWITTER_CREDS)

          oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)

          return Twitter(auth=OAuth(
              oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET))

#. Windows のユーザー環境変数設定で ``PYTHONPATH`` の値に ``%%HOME%%\my-python-modules`` を含める。
#. PTT を利用する使い捨てのスクリプトの構造を次のようにする。

   .. code-block:: python3

      from secret import twitter_instance

      tw = twitter_instance()
      ...

ページング処理
----------------------------------------------------------------------
ここからは PTT のメソッドを利用して Twitter の自分のアカウントを対象とするの操作を試していく。
本稿のサンプルコードは前述の共通処理をカットしているので、読者は注意して欲しい。

さっそくタイムラインの取得処理から見ていこう。
まずは、コードを書く前に Twitter 本家ドキュメントの `Working with Timelines`_ を一読して、
API がツイートのデータ構造をどのように定義しているのかをおおまかに理解しておこう。

特徴的なのは、 ``statuses/user_timeline`` や ``lists/statuses`` 等の「大量のツイートを返す」ような API を利用する場合には、
一度のリクエストでデータを一括取得するのではなく、リクエストを複数回に分けて行い、
その際に ``max_id`` や ``since_id`` 引数を適宜指定して利用するという技法が一般的らしいということが理解できる。
パターンとしては次の二通りしかないので、レスポンスの処理技法を習得するのは容易い。

ツイート日時の新しいものから、順次古い方向へ取得していくケース
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
一般的な Twitter クライアントでは、タイムラインはツイートが上から下に新しい順に並んでいる。
この画面を下方向にスクロールしたときに、より古いツイートを動的にリクエストするようになっている。
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

   response = tw.statuses.user_timeline(**kwargs)

   # ... response を処理 ...

   min_id = None
   if len(response):
       min_id = response[-1]['id']

   # 2 回目のリクエスト
   if min_id:
       kwargs['max_id'] = min_id - 1
   response = api.statuses.user_timeline(**kwargs)

   # ... response を処理 ...

レスポンス中のツイートは ``id`` という値を保持しており、
ツイートは ``id`` が降順になるように配列された状態で戻ってきている（と思う）。
その事実を利用すれば ``id`` の最大・最小が得られる。
配列の先頭ツイートの ``id`` が最大であり、
末尾ツイートのそれが最小であるはずだ。

3 回目以降のリクエストも同様に繰り返す。

取得済みのツイートの「上」に、最新のツイートを取得するケース
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
一般的な Twitter クライアントでは、ビューにタイマーが仕込んであり、
例えば 60 秒毎に最新のツイートをリクエストしてタイムラインを更新するものが多い。

おそらく、次のようなアルゴリズムを実行している。

* 初回リクエスト。レスポンス中のツイート群の ``id`` の最大値をプログラム側で記憶する。
* 次回リクエスト。このとき引数の ``since_id`` を明示的に指示する。

前項コードとの差分だけを示そう。

.. code-block:: python3

   # 最大 id の記憶
   max_id = None
   if len(response):
       max_id = response[0]['id']

.. code-block:: python

   # 2 回目のリクエスト
   if max_id:
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

  その際、値がゼロでないことを確認する必要がある。
  ゼロは取得するべきデータは Twitter に存在しないということを示唆している。

タイムライン関連
----------------------------------------------------------------------

GET statuses/mentions_timeline
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
いわゆるリプを取得する例を挙げる。

.. literalinclude:: ../sample/ptt/statuses-mentions_timeline.py
   :language: python3

* Comment 1: 認証ユーザーに関する mentions を最新のものから 50 件取得する。

  https://dev.twitter.com/docs/api/1.1/get/statuses/mentions_timeline 参照。

* Comment 2: ここでは mention の日時とツイート本文を新しい順にコンソールに出力している。

GET statuses/user_timeline
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ユーザー名を指定してタイムラインを 40 件取得し、
ツイート時刻と投稿内容をコンソールに出力するコードである。

.. literalinclude:: ../sample/ptt/statuses-mentions_timeline.py
   :language: python3

引数仕様は https://dev.twitter.com/docs/api/1.1/get/statuses/user_timeline を参照。

ちなみに、ドキュメント上は ``screen_name`` か ``user_id`` が
optional パラメーターとなっている API について注意が必要だ。
むしろ「そのうちのどちらかが required パラメーターである」という意味だろう。

GET statuses/home_timeline
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ユーザーのタイムラインを取得する例を示す。

.. literalinclude:: ../sample/ptt/statuses-home_timeline.py
   :language: python3

* Comment 1: 自作モジュールのメソッドを呼び出している。前述のとおり。

* Comment 2: 認証ユーザーのタイムラインを最新のものから 10 件取得する。
  主に自分のツイート、フォローしているユーザーのツイート、返信各種からなるものと思われる。

  キーワード引数の意味や、戻り値のデータ構造については
  https://dev.twitter.com/docs/api/1.1/get/statuses/home_timeline 参照。

* Comment 3: ツイートの日時と本文を新しい順にコンソールに出力している。

  .. caution::

     Python 3.4 に移行した直後に起動したら、コンソール上のテキストが文字化けして読めなかった。
     結局、環境変数 PYTHONIOENCODING を新規設定して、値を utf-8 と定義したら正常に読めるようになった。

ツイート関連
----------------------------------------------------------------------

POST statuses/update
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
スクリプト等からツイートするときには本 API を使用することになる。

.. literalinclude:: ../sample/ptt/statuses-update.py
   :language: python3

* Comment 1: tweet 内容を文字列として定義してみる。
* Comment 2: 関数 ``statuses.update`` をキーワード引数 ``status`` を指示して呼び出す。

  https://dev.twitter.com/docs/api/1.1/post/statuses/update 参照。

POST statuses/update_with_media
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
稼働実績なし。

.. literalinclude:: ../sample/ptt/statuses-update_with_media.py
   :language: python3

検索関連
----------------------------------------------------------------------
GET search/tweets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
単純な検索を行うには ``search/tweets`` を利用する。

.. literalinclude:: ../sample/ptt/search-tweets.py
   :language: python3

* Comment 1: ``ネシカ`` または ``nesica`` という単語を含むツイートを
  33 件検索させようとしている（厳密には不正確なやり方だが）。

  検索したい単語等をメソッド ``search.tweets`` に与える。
  キーワード引数の指定方法にコツがあるようだが、詳しくは
  https://dev.twitter.com/docs/api/1.1/get/search/tweets 参照。

* Comment 2: 検索結果の本体は、関数戻り値からこのように得られる。
  この例ではツイートのタイムスタンプ、ユーザー名、本文だけをコンソールに出力する。

  * 日付は標準時 (``+0000``) で得られる？

フォロワー関連
----------------------------------------------------------------------
GET friends/list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
特定のユーザーがフォローしている全ユーザーの情報を得るのには GET friends/list を利用できる。
一度のリクエストでは返しきれないほどの多数のユーザーをフォローしていることを想定してのカーソル処理となる。
次に示すコード例のように、1 ページずつデータをリクエストすることになる。

.. literalinclude:: ../sample/ptt/friends-list.py
   :language: python3

GET followers/list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
特定のユーザーをフォローしている全ユーザーの情報を得るのには GET followers/list を利用できる。
サンプルコードは先のコードをテキストエディターで ``s/friends/followers/`` すれば得られる。

ユーザーアカウント関連
----------------------------------------------------------------------
GET users/show
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
特定のユーザーの詳細情報を得るのに ``users/show`` を利用する。

.. literalinclude:: ../sample/ptt/users-show.py
   :language: python3

* Comment 1: 基本的に指定する引数はこれだけで構わない。
* Comment 2: ユーザーの Twitter 情報を出力してみる。
* https://dev.twitter.com/docs/api/1.1/get/users/show 参照。

GET users/search
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``users/search`` はキーワードから何か関係のありそうなユーザーを探すのにたいへん便利だ。
応用例としては、例えば bot に関係しそうなユーザーを可能な限りかき集めて、
ひとつのリストにまとめるといったものが考えられる（私はそれを実践している）。

これはごく単純な呼び出し例なので、キーワード引数 ``count`` の上限である 20 ユーザーしか取得できない。
さらに取得するには、この API の呼び出しをループの中に入れて、
キーワード引数 ``page`` をループカウンターで指定するとよいだろう。
その際には関数 ``time.sleep`` 等でリクエストに時間的間隔を設けると申し分ない。

.. literalinclude:: ../sample/ptt/users-search.py
   :language: python3

お気に入り関連
----------------------------------------------------------------------
GET favorites/list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
特定のユーザーが星マークを付けたツイート群を取得する。

.. literalinclude:: ../sample/ptt/favorites-list.py
   :language: python3

だんだん解説がワンパターン化してきたので、以降は目立つポイントのみ解説をする。

リスト関連
----------------------------------------------------------------------
GET lists/list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
全リスト取得に用いる API だ。

.. literalinclude:: ../sample/ptt/lists-list.py
   :language: python3

* Comment 1: メソッド ``lists.list`` に ``screen_name`` キーワード引数を与えて、
  そのユーザーの持っているリストを全部取得する。
  ユーザーが作成したリストに加え、もしあれば、購読している他ユーザーが作成したリストを含む。

  https://dev.twitter.com/docs/api/1.1/get/lists/list 参照。

* Comment 2: 各リストの mode, full_name, description 各属性をコンソールに出力する。

GET lists/statuses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
既存のリストのタイムラインを閲覧するための API だ。
例えば ``screen_name`` が ``showa_yojyo`` のユーザーの、
``news`` という公開リストがあるという前提で、そのタイムラインを見てみよう。

.. literalinclude:: ../sample/ptt/lists-statuses.py
   :language: python3

* Comment 1

  * メソッド ``lists.statuses`` に与える引数を準備する。
    リストを特定する手段は一つではないのだが、
    分かりやすさを優先して ``slug`` および ``owner_screen_name`` を同時に指示する。

  * その他は https://dev.twitter.com/docs/api/1.1/get/lists/statuses 参照。

* Comment 2

  * 文字列をコンソールに出力する。
    ツイート内容、改行、ツイート時刻、ツイートに利用したアプリ名が確認できる。

POST lists/members/destroy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
リストから指定したユーザーを削除するための API だ。
しかし、これを利用するくらいならばブラウザーで Twitter を利用するほうが早いやもしれない。

.. literalinclude:: ../sample/ptt/lists-members-destroy.py
   :language: python3

GET lists/memberships
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``lists/memberships`` リクエストは、
あるユーザーが他のユーザーが管理しているリストに含まれているとき、
そのようなリストを列挙するのに利用する。

.. literalinclude:: ../sample/ptt/lists-memberships.py
   :language: python3

* Comment 1: ユーザー ``showa_yojyo`` を含むリストをリクエストする。
  ``cursor`` については別項で詳しく解説する。

* Comment 2: 各リストの名前と説明文をコンソールに出力する。
  ``full_name`` の先頭にはリストの作者の ``screen_name`` が見えると思う。

* https://dev.twitter.com/docs/api/1.1/get/lists/memberships 参照。

GET lists/subscribers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
指定リストの購読者をリストするのに利用する。
どうも非公開ユーザーが購読していてもリストされないらしい。

.. literalinclude:: ../sample/ptt/lists-subscribers.py
   :language: python3

POST lists/members/create_all
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ブラウザー上の操作ではできないと思われる、一括でユーザーを複数指定して指定のリストに登録する処理を実現するための API だ。
次のサンプルコードの ``screen_names`` はスクリーンネームの tuple インスタンスを意味する。
この API はリストを多用する筆者が利用する頻度がもっとも高い。

.. literalinclude:: ../sample/ptt/lists-members-create_all.py
   :language: python3

GET lists/members/show
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
指定ユーザーが指定リストに登録されているかを調べる API だ。
使い途が少々思いつかない。

.. literalinclude:: ../sample/ptt/lists-members-show.py
   :language: python3

GET lists/members
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
指定リストに登録されているユーザーをすべて得ることができる API だ。
登録ユーザー数が多いリストに対しては、次のように「カーソル処理」で複数回のリクエストをすることになるだろう。

.. literalinclude:: ../sample/ptt/lists-members.py
   :language: python3

POST lists/members/create
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
自分の所有するリストに指定ユーザーを一人分登録する API だ。
今では上述の lists/members/create_all で完全に置き換えてしまって構わなそうだ。

.. literalinclude:: ../sample/ptt/lists-members-create.py
   :language: python3

POST lists/destroy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
自分の所有するリストを一つ指定して、それを削除する API だ。
使用頻度はテスト用に作成したダミーリストをまた削除するときに使うくらいだ。

.. literalinclude:: ../sample/ptt/lists-destroy.py
   :language: python3

POST lists/create
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
リストを新しく作成するための API だ。Twitter Web Client で作業するほうが早い。
https://dev.twitter.com/docs/api/1.1/post/lists/create 参照。

.. literalinclude:: ../sample/ptt/lists-create.py
   :language: python3

GET lists/subscriptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
あるユーザーが購読している（他ユーザーの管理下にある）リストを得るために利用する。

.. literalinclude:: ../sample/ptt/lists-subscriptions.py
   :language: python3

GET lists/ownerships
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``lists/ownerships`` は特定のユーザーが管理しているリストを列挙するのに利用する。
ツイートというよりは、リストのプロパティーを得るのに利用する。

.. literalinclude:: ../sample/ptt/lists-ownerships.py
   :language: python3

検索履歴関連
----------------------------------------------------------------------
GET saved_searches/list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Twitter ログイン時に当該アカウントで検索したクエリーの一覧を取得する。
実行してみれば理解できる。

.. literalinclude:: ../sample/ptt/saved_searches-list.py
   :language: python3

GET saved_searches/create
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
わかりにくい言い方をすると「保存した検索」項目を一つ新しく作成するための API だ。
個人的には今となっては使い途がなくなってしまった API のひとつ。

.. literalinclude:: ../sample/ptt/saved_searches-create.py
   :language: python3

TwitterStream
----------------------------------------------------------------------
TBW

.. _Python: http://www.python.org/
.. _Python Twitter Tools: http://mike.verdone.ca/twitter/
.. _REST API v1.1 Resources: https://dev.twitter.com/docs/api/1.1
.. _Working with Timelines: https://dev.twitter.com/docs/working-with-timelines
