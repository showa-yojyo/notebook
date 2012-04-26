======================================================================
Python Twitter Tools 利用ノート
======================================================================

.. contents:: ノート目次

.. note::

   * OS: Windows XP Home Edition SP 3
   * 本稿において、利用した各パッケージのバージョンは次のとおり。

     * Python_: 2.6.6
     * `Python Twitter Tools`_: 1.7.2

関連リンク
======================================================================
`Python Twitter Tools`_
  著者ウェブページ。開発ページは別にある。

`REST API Resources`_
  Twitter 本家ドキュメント。

パッケージ概要
======================================================================
* `Python Twitter Tools`_ は Twitter API にアクセスすることのできる Python 製パッケージ。
* API を操作するたけのコードだけでなく、他にも面白いツール群が同梱されている。

  * 本稿ではライブラリー部分の利用法習得を記録する。

前準備
======================================================================
* 最初の目標を「簡単な Python スクリプトを作成し、Twitter からデータを取得する」こととするとよい。
* 次に、特別な認証が必要な API を利用するスクリプトを作成、動作確認することを目標とする。
* 余裕ができたら、さらなる API を叩いてみる。

パッケージインストール
----------------------------------------------------------------------
* `easy_install`_ を利用してインストールするのが最もシンプルだ。

  ``$ easy_install twitter``

  とすればよい。

* 本パッケージには単体テストコードのようなものはない。
  「インストールが無事に終わった」ことを知りたいのならば、
  ``import twitter`` の確認で我慢する。
  
  ``$ python -c 'import twitter; help(twitter)'``

ドキュメント
----------------------------------------------------------------------
* パッケージのドキュメントよりも重要なのは Python API 自身のドキュメントだ。
  `REST API Resources`_ 等のウェブページを見ながら
  Python コードを書くことになるはずなので、ここをブックマークしておくべし。

コード例
======================================================================
以下、個人的に動作確認が取れた状況でのコードのみをノートしておく。
細かい説明を重ねるよりは、動作したコードを淡々と列挙して、
見返したときに直感的に思い出せる方がよい。

認証関係
----------------------------------------------------------------------
事実関係をリストしておく。

* 本家 Twitter API は OAuth という認証を利用している。
  一部の API を利用するために（少なくとも）
  consumer key および
  consumer secret key と呼ばれる文字列が必要となる。

  * これらの文字列を入手するには、
    https://dev.twitter.com/apps 以降のページ群であらかじめ手続きを済ませる。
  
    * ウェブブラウザーと Twitter アカウントを持っていることが必要である。
    * Create an application というページに入力フォームがある。
      入力後、画面下部のボタンを押せば多分出てくるだろう。

* 次に user key および user secret key という、別の一対の文字列が必要だ。

  * これらの文字列を得るために、先ほどの文字列が必要となる。

  * Google で ``get_access_token`` 等検索してヒットする、
    ネットに落ちているスクリプトを一部改変して実行する。
    コードを見れば手を入れる箇所は理解できるハズ。

* 上記 4 つの文字列を入手できたならば、利用できる API が増えるというわけだ。

  * POST 系 API はほぼ OAuth 必須。

GET statuses/home_timeline
----------------------------------------------------------------------
API を利用する認証を得ているユーザー（自分）のタイムラインを取得する例。

.. code-block:: python

   # -*- coding: utf-8 -*-
   import twitter

   # Comment 1
   user_key, user_secret, consumer_key, consumer_secret = get_oauth_keys()

   api = twitter.Twitter(
       auth=twitter.OAuth(user_key, user_secret, 
                          consumer_key, consumer_secret))
   # Comment 2
   statuses = api.statuses.home_timeline(
       count=55,
       include_rts='true',
       include_entities='true',
       exclude_replies='false',)

   # Comment 3
   for stat in statuses:
       print(u'%s %s' % (stat['created_at'], stat['text']))

* Comment 1: ``get_oauth_keys()`` を自作すること。
  前項で説明した文字列を返すだけの関数とする。

* Comment 2: ``auth`` のユーザーのタイムラインを最新のものから 55 件取得する。
  主に自分のツイート、フォローしているユーザーのツイート、返信各種からなるものと思われる。

  キーワード引数の意味や、戻り値のデータ構造については
  https://dev.twitter.com/docs/api/1/get/statuses/home_timeline 参照。

* Comment 3: ツイートの日時と本文を新しい順にコンソールに出力している。

GET statuses/mentions
----------------------------------------------------------------------
いわゆるリプを取得する例を挙げる。

.. code-block:: python

   # 前半省略。
   # api インスタンスを認証つきで前項までの例と同様に作成する。

   # Comment 1
   statuses = api.statuses.mentions(count=50, include_entities='true')

   # Comment 2
   for stat in statuses:
       entities = stat['entities']
       try:
           print(u'%s %s' % (stat['created_at'], stat['text']))
       except UnicodeEncodeError:
           print(u'%s (UnicodeEncodeError)' % stat['created_at'])

* Comment 1: 認証ユーザーに関する mentions を最新のものから 50 件取得する。

  https://dev.twitter.com/docs/api/1/get/statuses/mentions 参照。

* Comment 2: ここでは mention の日時とツイート本文を新しい順にコンソールに出力している。

GET statuses/public_timeline
----------------------------------------------------------------------

.. code-block:: python

   # -*- coding: utf-8 -*-
   import twitter

   # Comment 1
   api = twitter.Twitter()

   # Comment 2
   stats = api.statuses.public_timeline(count=22)

   # Comment 3
   for stat in stats:
       user = stat['user']
       try:
           print('[%s] %s' % (user['screen_name'], stat['text']))
       except UnicodeEncodeError:
           print(u'[%s] (UnicodeEncodeError)' % user['screen_name'])

* Comment 1: コンストラクターで引数を与えずに生成した ``Twitter`` インスタンスは、
  認証が必要ない API を利用する場合に動作する。
  このルールは全 API 共通だろう。

* Comment 2: 引数仕様は https://dev.twitter.com/docs/api/1/get/statuses/public_timeline を参照。
  上記コードの ``user`` の構造は、その仕様書の JSON コードを眺めていればわかる。

* Comment 3: パブリックタイムラインを Twitter から 22 件取得し、
  アカウント名と投稿内容をコンソールに出力するコードである。

GET statuses/user_timeline
----------------------------------------------------------------------
ユーザー名を指定してタイムラインを 40 件取得し、
ツイート時刻と投稿内容をコンソールに出力するコードである。

.. code-block:: python

   # -*- coding: utf-8 -*-
   import twitter
   
   api = twitter.Twitter()

   # Comment 1
   stats = api.statuses.user_timeline(screen_name='showa_yojyo', count=40)

   for item in stats:
       print(u'%(created_at)s: %(text)s' % item)

* Comment 1:
  引数仕様は https://dev.twitter.com/docs/api/1/get/statuses/user_timeline を参照。

  ちなみに、ドキュメント上は ``screen_name`` か ``user_id`` が
  optional パラメーターとなっている API について注意が必要だ。
  むしろ「そのうちのどちらかが required パラメーターである」という意味だろう。

POST statuses/update
----------------------------------------------------------------------
スクリプト等からツイートするときには本 API を使用することになる。

.. code-block:: python

   # 前半省略。
   # api インスタンスを認証つきで前項までの例と同様に作成する。

   # Comment 1
   mytext = u'Python Twitter Tools を利用したツイートのデモ。明示的 URL エンコード処理なし'
   assert len(mytext) < 140

   try:
       # Comment 2
       api.statuses.update(status=mytext)
   except twitter.TwitterHTTPError as e:
       print(e)

* Comment 1: tweet 内容を文字列として定義してみる。
* Comment 2: 関数 ``statuses.update`` をキーワード引数 ``status`` を指示して呼び出す。

  https://dev.twitter.com/docs/api/1/post/statuses/update 参照。

POST statuses/update_with_media
----------------------------------------------------------------------
スクリプト等から画像をツイート（？）するときには本 API を使用することになる。

.. admonition:: TODO

   動作コードをここに書く。

GET search
----------------------------------------------------------------------
単純な検索を行うには ``search`` を利用する。

.. code-block:: python

   import twitter
   
   # Comment 1
   api = twitter.Twitter(domain="search.twitter.com")

   # Comment 2
   response = api.search(
       q=u'ネシカ OR nesica',
       rpp=33)
   
   # Comment 3
   for result in response['results']:
       print(u'%(created_at)s %(from_user)s %(text)s' % result)

* Comment 1: 検索の場合は ``Twitter`` インスタンスの生成時に、
  キーワード引数 ``domain`` を明示的に指示する。

  ここでは ``ネシカ`` または ``nesica`` という単語を含むツイートを
  33 件検索させようとしている（厳密には不正確なやり方だが）。

* Comment 2: 検索したい単語等を関数 ``search`` に与える。
  キーワード引数の指定方法にコツがあるようだが、

  https://dev.twitter.com/docs/api/1/get/search 参照。

* Comment 3: 検索結果の本体は、関数戻り値からこのように得られる。
  この例ではツイートのタイムスタンプ、ユーザー名、本文だけをコンソールに出力する。

  * 日付は標準時 (``+0000``) で得られる？

POST direct_messages/new
----------------------------------------------------------------------
あまり使わないが、ノートに残す。説明省略。

.. code-block:: python

   # 前半省略。
   # api インスタンスを認証つきで前項までの例と同様に作成する。

   try:
       api.direct_messages.new(
           screen_name='@showa_yojyo',
           text=u'ダイレクトメッセ')
   except twitter.TwitterHTTPError as e:
       print(e)

GET lists/all
----------------------------------------------------------------------
全リスト取得に用いる API だ。

.. code-block:: python

   # 前半省略。
   # api インスタンスを認証つきで前項までの例と同様に作成する。

   # Comment 1
   data = api.lists.all(screen_name='showa_yojyo')
   
   # Comment 2
   for item in data:
       print('%(mode)s following=%(following)s %(full_name)s %(description)s' % item)

* Comment 1: ``lists.all`` 関数に ``screen_name`` キーワード引数を与えて、
  対応するユーザーの持っているリストを全部取得する。

  * 当ノートでは ``api`` 作成時の認証と同じユーザーであることを想定している。
    この場合、公開リストも非公開リストも同時に得られる。
    もし、違うユーザーを指定した場合、おそらく公開リストだけが得られるのだろう。

  * https://dev.twitter.com/docs/api/1/get/lists/all 参照。

* Comment 2: リストごとに属性をコンソールに出力する。

GET lists/statuses
----------------------------------------------------------------------
既存のリストのタイムラインを閲覧するための API だ。
例えば ``screen_name`` が ``showa_yojyo`` のユーザーの、
``exam`` という公開リストがあるという前提で、
そのタイムラインを見てみよう。

.. code-block:: python

   # NoAuth パターン

   # Comment 1
   kwargs = dict(
       slug='exam', 
       owner_screen_name='showa_yojyo',
       per_page=10,
       page=1,
       include_entities=1,
       include_rts=1)
   try:
       data = api.lists.statuses(**kwargs)
       for item in data:
           # Comment 2
           print item['user']['screen_name'],
           print '%(text)s\n%(created_at)s %(source)s' % item
           print '-' * 70

* Comment 1

  * ``lists.statuses`` 関数に与える引数を準備する。
    リストを特定する手段は一つではないのだが、
    分かりやすさを優先して ``slug`` および ``owner_screen_name`` を同時に指示する。

  * その他は https://dev.twitter.com/docs/api/1/get/lists/statuses 参照。

* Comment 2

  * 文字列をコンソールに出力する。
    ツイート内容、改行、ツイート時刻、ツイートに利用したアプリ名が確認できる。

POST lists/create
----------------------------------------------------------------------
リストを新しく作成するための API だ。

.. code-block:: python

   # 前半省略。
   # api インスタンスを認証つきで前項までの例と同様に作成する。
   
   # Comment 1
   items = [
       dict(name='friends', description=u'友人たち'),
       dict(name='game', description=u'ゲーム関連'),
       dict(name='rivals', description=u'ライバル連中', mode='private'),
       ]

   try:
       # Comment 2
       for item in items:
           print('%(name)s...' % item)
           data = api.lists.create(**item)
   except twitter.TwitterHTTPError as e:
       print(e)

* Comment 1: Twitter のリストとして追加したい項目をこのように用意しておく。
  例によって上限数に注意。

* Comment 2: ``lists.create`` 関数に先程の項目を指定してループで回す。
  失敗すると例外送出が起こる。
  おそらくリスト項目数の上限数超過が起こっている。

  * https://dev.twitter.com/docs/api/1/post/lists/create 参照。
  * ``try`` ブロックをループの中に入れたほうがよいかも。


GET saved_searches/create
----------------------------------------------------------------------
わかりにくい言い方をすると「保存した検索」項目を一つ新しく作成するための API だ。

.. code-block:: python

   # 前半省略。
   # api インスタンスを認証つきで前項までの例と同様に作成する。

   # Comment 1
   items = [
       u'DQ OR ドラクエ OR ドラゴンクエスト',
       u'@showa_yojyo -from:showa_yojyo',
       ]

   try:
       for item in items:
           # Comment 2
           api.saved_searches.create(query=item)
   except twitter.TwitterHTTPError as e:
       # Comment 3
       print(e)

* Comment 1: Twitter の「保存した検索」の項目ひとつずつと対応する検索パターン。
  上限は Twitter 仕様により 20 個と決まっている。

* Comment 2: https://dev.twitter.com/docs/api/1/post/saved_searches/create 参照。
  ``query`` キーワード引数しかないようだ。

* Comment 3: 検索パターンの登録に失敗すると、例外が発生する。
  大抵の場合、上述の上限値超過だろう。

TwitterStream
----------------------------------------------------------------------
:file:`stream_example.py` はこのままでは実行時エラー
``urllib2.URLError`` (Errno 10060) が発生する。
``TwitterStream`` コンストラクターの呼び出しを次のように修正すると動く。

.. code-block:: python

   stream = TwitterStream(auth=UserPassAuth(args[0], args[1]),
                          secure=True)

.. _Python: http://www.python.org/
.. _Python Twitter Tools: http://mike.verdone.ca/twitter/
.. _easy_install: http://peak.telecommunity.com/DevCenter/EasyInstall
.. _REST API Resources: https://dev.twitter.com/docs/api
