======================================================================
Python Twitter Tools 利用ノート
======================================================================

.. note::

   本稿において、利用した各パッケージのバージョンは次のとおり。

   * Python_: 2.6.6
   * `Python Twitter Tools`_: 1.7.2

.. contents:: ノート目次

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

GET statuses/public_timeline
----------------------------------------------------------------------

.. code-block:: python

   import twitter

   api = twitter.Twitter()
   stats = api.statuses.public_timeline(count=22)

   for stat in stats:
       user = stat['user']
       try:
           print('[%s] %s' % (user['screen_name'], stat['text']))
       except UnicodeEncodeError:
           pass

* パブリックタイムラインを Twitter から 22 件取得し、
  アカウント名と投稿内容をコンソールに出力するコードである。

* 引数仕様は https://dev.twitter.com/docs/api/1/get/statuses/public_timeline を参照。
  上記コードの ``user`` の構造は、その仕様書の JSON コードを眺めていればわかる。

* コンストラクターで引数を与えずに生成した ``Twitter`` インスタンスは、
  認証が必要ない API を利用する場合に動作する。
  このルールは全 API 共通だろう。

GET statuses/user_timeline
----------------------------------------------------------------------

.. code-block:: python

   import twitter
   
   api = twitter.Twitter()
   stats = api.statuses.user_timeline(screen_name='showa_yojyo', count=40)

   for item in stats:
       print(u'%(created_at)s: %(text)s' % item)

* ユーザー名 ``showa_yojyo`` のタイムラインを 40 件取得し、
  ツイート時刻と投稿内容をコンソールに出力するコードである。

* 引数仕様は https://dev.twitter.com/docs/api/1/get/statuses/user_timeline を参照。

* ちなみに、ドキュメント上は ``screen_name`` か ``user_id`` が
  optional パラメーターとなっている API について注意が必要だ。
  むしろ「そのうちのどちらかが required パラメーターである」という意味だろう。

認証関係
----------------------------------------------------------------------
TBW; 説明が面倒。

GET saved_searches
----------------------------------------------------------------------
TBW

GET lists/all
----------------------------------------------------------------------
TBW

POST lists/create
----------------------------------------------------------------------
TBW

.. _Python: http://www.python.org/
.. _Python Twitter Tools: http://mike.verdone.ca/twitter/
.. _easy_install: http://peak.telecommunity.com/DevCenter/EasyInstall
.. _REST API Resources: https://dev.twitter.com/docs/api
