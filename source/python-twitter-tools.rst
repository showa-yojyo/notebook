======================================================================
Python Twitter Tools 利用ノート
======================================================================

.. contents:: ノート目次

.. note::

   * OS: Windows XP Home Edition SP 3
   * 本稿において、利用した各パッケージのバージョンは次のとおり。

     * Python_: 2.6.6, 2.7.3
     * `Python Twitter Tools`_: 1.7.2, 1.8.0, 1.9.0

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
* `easy_install`_ （可能ならば `pip`_ のほうがよい）を利用してインストールするのが最もシンプルだ。

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


ページング処理
----------------------------------------------------------------------
`Working with Timelines`_ をまずは一読あれ。

``statuses/user_timeline`` や ``lists/statuses`` 等の「大量のツイートを返す」 API を利用する場合には、
一度のリクエストでデータを一括取得するのではなく、
リクエストを複数回に分けて行い、その際に
``max_id`` や ``since_id`` 引数を適宜指定して利用するという技法が一般的だ。

パターンとしては次の二通りしかないので、レスポンスの処理技法を習得しておこう。

ツイート日時の新しいものから、順次古い方向へ取得していくケース
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
一般的な Twitter クライアントでは、タイムラインはツイートが上から下に新しい順に並んでいる。
この画面を下方向にスクロールしたときに、より古いツイートを動的にリクエストするようになっている。
実質的には次に説明するようなことを行なっているハズだ。

* 初回リクエスト。レスポンス中のツイート群の ``id`` の最小値をプログラム側で記憶する。
* 次回リクエスト。このとき引数の ``max_id`` を明示的に指示する。

コードを示す。

.. code-block:: python

   kwargs = dict(
       screen_name='showa_yojyo',
       count=20,
       page=1,
       include_entities=1,
       include_rts=1,
       exclude_replies=0)

   response = api.statuses.user_timeline(**kwargs)

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

.. code-block:: python

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
       print(u'{created_at} {text}'.format(**stat))

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
           print(u'{created_at} {text}'.format(**stat))
       except UnicodeEncodeError:
           print(u'{created_at} (UnicodeEncodeError)'.format(**stat)

* Comment 1: 認証ユーザーに関する mentions を最新のものから 50 件取得する。

  https://dev.twitter.com/docs/api/1/get/statuses/mentions 参照。

* Comment 2: ここでは mention の日時とツイート本文を新しい順にコンソールに出力している。

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
       print(u'{created_at} {text}'.format(**item))

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
       print(u'{created_at} {from_user} {text}'.format(**result))

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

GET followers/ids, GET friends/ids, GET users/lookup
----------------------------------------------------------------------
これらの API をまとめて理解するのが効率的だ。
特定のユーザーのフォロー・被フォローユーザーの集合を得るときに利用するのだが、
実用上の観点から 2 パスでデータを処理することになる。

#. 前者の API でユーザーの ID だけを得る。
#. 後者の API で詳細情報を得る。

次のようなコードを書けばよいだろう。フォロワーを調べる例を示す。

.. code-block:: python

   # ... import 文、Twitter インスタンス作成、例外処理等省略。
   
   # Comment 1
   res1 = api.followers.ids(screen_name='showa_yojyo', cursor=-1)
   if 0 < len(res1['ids']) and len(res1['ids']) < 100:
       # Comment 2
       ids = ','.join([str(id) for id in res1['ids'])
       res2 = api.users.lookup(user_id=ids, include_entities=0)

* Comment 1: ``cursor=-1`` は最初のチャンクをリクエストすることを意味する。
  仮にこのユーザーのフォロワー数が異様に多い (5000) 場合、戻り値の
  ``res1.next_cursor`` に非ゼロの値が含まれるので、さらなる
  ``api.followers.ids`` の呼び出し時に ``cursor`` キーワード引数にこの値を指示するのだ。

* Comment 2: user_id の配列を CSV 化する。
  詳しくは ``users/lookup`` の仕様説明を当たって欲しい。

  * リクエストする id は 100 個を超えないようにすること。
  * ``res2`` には詳細情報が格納されるが、順序はデタラメになっていると思ったほうがよい。
    こんな感じにソートするしかなさそうだ。

    .. code-block:: python

       res3 = [None] * len(res1['ids'])
       for user in res2:
           user_id = user[u'id']
           i = res1['ids'].index(user_id)
           res3[i] = user

* 参考

  * https://dev.twitter.com/docs/api/1/get/followers/ids
  * https://dev.twitter.com/docs/api/1/get/friends/ids
  * https://dev.twitter.com/docs/api/1/get/users/lookup

GET users/show
----------------------------------------------------------------------
特定のユーザーの詳細情報を得るのに ``users/show`` を利用する。

.. code-block:: python

   # ... import 文、Twitter インスタンス作成、例外処理等省略。

   # Comment 1
   response = api.users.show(screen_name='showa_yojyo', entities=1)

   # Comment 2
   print u'''
   {screen_name} | {name}
   {location}
   {url}
   {description}

   ツイート数 {statuses_count}
   フォロー {friends_count} 人
   フォロワー {followers_count} 人
   '''.format(**response)

* Comment 1: 基本的に指定する引数はこれだけで構わない。
* Comment 2: ユーザーの Twitter 情報を出力してみる。
* https://dev.twitter.com/docs/api/1/get/users/show 参照。

GET favorites
----------------------------------------------------------------------
特定のユーザー星マークを付けたツイート群を取得する。

.. code-block:: python

   # ...NoAuth で api 作成。

   kwargs = dict(
       screen_name='showa_yojyo',
       count=10,
       page=1,
       include_entities=1)

   response = api.favorites(**kwargs)
   for status in response:
       print u'@{user[screen_name]}'.format(**status),
       print u'{text}\n{created_at} %{source}'.format(**status)
       print u'-' * 70

だんだん解説をするのが面倒になってきた。他の項目を見てくれ。

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
       print(u'{mode} following={following} {full_name} {description}'.format(**item))

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
           print u'{text}\n{created_at} {source}'.format(**item)
           print '-' * 70

* Comment 1

  * ``lists.statuses`` 関数に与える引数を準備する。
    リストを特定する手段は一つではないのだが、
    分かりやすさを優先して ``slug`` および ``owner_screen_name`` を同時に指示する。

  * その他は https://dev.twitter.com/docs/api/1/get/lists/statuses 参照。

* Comment 2

  * 文字列をコンソールに出力する。
    ツイート内容、改行、ツイート時刻、ツイートに利用したアプリ名が確認できる。

GET lists/memberships
----------------------------------------------------------------------
``lists/memberships`` リクエストは、
あるユーザーが他のユーザーが管理しているリストに含まれているとき、
そのようなリストを列挙するのに利用する。

.. code-block:: python

   # ...NoAuth で api 作成。

   # Comment 1
   response = api.lists.memberships(screen_name='showa_yojyo', cursor=-1)

   # Comment 2
   for item in response[u'lists']:
       print u'{full_name} {description}'.format(**item)

* Comment 1: ユーザー ``showa_yojyo`` を含むリストをリクエストする。
  ``cursor`` については別項で詳しく解説する。

* Comment 2: 各リストの名前と説明文をコンソールに出力する。
  ``full_name`` の先頭にはリストの作者の ``screen_name`` が見えると思う。

* https://dev.twitter.com/docs/api/1/get/lists/memberships 参照。

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
           print(u'{name}...'.format(**item))
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

GET lists
----------------------------------------------------------------------
``lists`` はあるユーザーが管理しているリストを列挙するのに利用する。
ツイートというよりは、リストのプロパティーを得るのに利用する。

.. code-block:: python

   # ...NoAuth で api 作成。

   response = api.lists(screen_name='showa_yojyo', cursor=-1)
   for item in response[u'lists']:
       print u'{full_name} {description}'.format(**item)

* コードについては GET lists/memberships の項を参照。
* https://dev.twitter.com/docs/api/1/get/lists 参照。

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
.. _pip: http://pypi.python.org/pypi/pip
.. _REST API Resources: https://dev.twitter.com/docs/api
.. _Working with Timelines: https://dev.twitter.com/docs/working-with-timelines
