======================================================================
フォロー自身とフォローに付随する機能 (friendships)
======================================================================
本節では friendships 系 REST API について記す。
私自身はフォロー機能を全く利用しないので、この括りの機能には基本的には縁がない。
試すとしたら、任意のユーザー同士の関係性を知る機能ということになる。

.. contents::

POST friendships/create
======================================================================
POST friendships/create は他人をフォローする機能だ。
オプションとして彼に関するイベント通知の有無を設定できる。

次にサンプルコードを示す。

.. literalinclude:: /_sample/ptt/friendships-create.py
   :language: python3

* [1] フォローするユーザーの ``user_id`` または ``screen_name`` を指定する。
  どちらか一方でよい。

  また、オプションとして ``follow=True`` という解りにくいパラメーターがある。
  これは相手からのイベント通知を有効にするかどうかのフラグである。

* [2] 応答データを出力する。

次に実行例を示す。自分自身をフォローすることはできないようだ。

.. code-block:: console

   $ ./friendships-create.py
   Traceback (most recent call last):
     File "D:\Python35\lib\site-packages\twitter\api.py", line 319, in _handle_response
       handle = urllib_request.urlopen(req, **kwargs)
     File "D:\Python35\lib\urllib\request.py", line 162, in urlopen
       return opener.open(url, data, timeout)
     File "D:\Python35\lib\urllib\request.py", line 471, in open
       response = meth(req, response)
     File "D:\Python35\lib\urllib\request.py", line 581, in http_response
       'http', request, response, code, msg, hdrs)
     File "D:\Python35\lib\urllib\request.py", line 509, in error
       return self._call_chain(*args)
     File "D:\Python35\lib\urllib\request.py", line 443, in _call_chain
       result = func(*args)
     File "D:\Python35\lib\urllib\request.py", line 589, in http_error_default
       raise HTTPError(req.full_url, code, msg, hdrs, fp)
   urllib.error.HTTPError: HTTP Error 403: Forbidden

   During handling of the above exception, another exception occurred:

   Traceback (most recent call last):
     File "./friendships-create.py", line 14, in <module>
       response = tw.friendships.create(screen_name='showa_yojyo')
     File "D:\Python35\lib\site-packages\twitter\api.py", line 312, in __call__
       return self._handle_response(req, uri, arg_data, _timeout)
     File "D:\Python35\lib\site-packages\twitter\api.py", line 345, in _handle_response
       raise TwitterHTTPError(e, uri, self.format, arg_data)
   twitter.api.TwitterHTTPError: Twitter sent status 403 for URL: 1.1/friendships/create.json using parameters: (oauth_consumer_key=...&screen_name=showa_yojyo)
   details: {'errors': [{'code': 158, 'message': "You can't follow yourself."}]}

POST friendships/destroy
======================================================================
POST friendships/destroy は他人をフォローするのをやめる機能だ。

次にサンプルコードを示す。

.. literalinclude:: /_sample/ptt/friendships-destroy.py
   :language: python3

* [1] フォローを解除するユーザーの ``user_id`` または ``screen_name`` を指定する。
  どちらか一方でよい。

* [2] 応答データを出力する。

次に実行例を示す。
フォローに失敗したはずのユーザーでも相手のユーザーオブジェクトが得られる。

.. code-block:: console

   $ ./friendships-destroy.py
   {
       ...
       "following": false,
       ...
       "screen_name": "showa_yojyo",
       ...
   }

GET friendships/incoming
======================================================================
GET friendships/incoming は自分が保護ユーザー、
つまりツイート非公開アカウントとして運用している場合に利用価値がある。
これは自分に対してのフォローリクエストで未承認のものがどれだけあるかを知る機能だ。

次にサンプルコードを示す。

.. literalinclude:: /_sample/ptt/friendships-incoming.py
   :language: python3

* [1] :doc:`./rest` で説明したカーソル処理。

次に実行例を示す。
空のデータが得られる。
私が公開アカウントであることか、誰からも相手にされていないことかのいずれかが成り立っている。

.. code-block:: console

   $ ./friendships-incoming.py
   []

GET friendships/outgoing
======================================================================
GET friendships/outgoing は自分がフォローしたい非公開アカウントの ID を得る機能だ。
言い換えると、フォローリクエストがお預けを食らっている相手がどれだけいるかを知る機能だ。

次にサンプルコードを示す。

.. literalinclude:: /_sample/ptt/friendships-outgoing.py
   :language: python3

* [1] :doc:`./rest` で説明したカーソル処理。

次に実行例を示す。
どんな非公開アカウントをもフォローしようとしていないからこうなる。

.. code-block:: console

   $ ./friendships-outgoing.py
   []

GET friendships/lookup
======================================================================
GET friendships/lookup は自分と任意の他人との関係性を知る機能だ。
関係性とは、フォロー関係、当方から先方へのブロック・ミュート状況といったものだ。
一度のリクエストで複数のユーザーに対して情報を得ることができる。

次にサンプルコードを示す。

.. literalinclude:: /_sample/ptt/friendships-lookup.py
   :language: python3

* [1] 調査対象ユーザーをパラメーター ``user_id`` か ``screen_name`` の（どちらか一方でだろうか？）指定する。
  どちらも CSV 文字列とする。

* [2] 結果を出力する。

次に実行例を示す。一部省略する。

.. code-block:: console

   $ ./friendships-lookup.py
   [
       {
           "id_str": "577367985",
           "screen_name": ...
           "name": ...
           "id": 577367985,
           "connections": [
               "followed_by"
           ]
       },
       {
           "id_str": "1220723053",
           "screen_name": ...
           "name": ...
           "id": 1220723053,
           "connections": [
               "followed_by"
           ]
       },
       {
           "id_str": "1288619659",
           "screen_name": ...
           "name": ...
           "id": 1288619659,
           "connections": [
               "followed_by"
           ]
       }
   ]

注目したいのは connections の値だ。
ここには ``none``, ``blocking``, ``muting``, ``following``,
``following_requested``, ``followed_by`` がその条件を満たすもの全部が含まれる。

GET friendships/show
======================================================================
GET friendships/show は任意の二人のユーザー間の関係を得る機能だ。

サンプルコードを次に示す。
選択するユーザー同士によってはかなり興味深い情報が得られることがあるが、
ここではおとなしい結果が得られるようにした。

.. literalinclude:: /_sample/ptt/friendships-show.py
   :language: python3

* [1] この二人の関係性を調べてみよう。
  Twitter ではユーザー同士の関係性には対称律は一般に成り立たないので、
  引数を左右入れ替えてもう一度リクエストする。

次に実行例を示す。

.. code-block:: console

   $ ./friendships-show.py
   {
       "relationship": {
           "source": {
               "following_requested": null,
               "muting": null,
               "want_retweets": null,
               "can_dm": false,
               "screen_name": "asahi",
               "id_str": "42816371",
               "notifications_enabled": null,
               "marked_spam": null,
               "blocked_by": null,
               "all_replies": null,
               "following": false,
               "blocking": null,
               "following_received": null,
               "id": 42816371,
               "followed_by": false
           },
           "target": {
               "following_requested": null,
               "following": false,
               "id": 562773398,
               "id_str": "562773398",
               "screen_name": "Sankei_news",
               "followed_by": false,
               "following_received": null
           }
       }
   }
   {
       "relationship": {
           "source": {
               "following_requested": null,
               "muting": null,
               "want_retweets": null,
               "can_dm": false,
               "screen_name": "Sankei_news",
               "id_str": "562773398",
               "notifications_enabled": null,
               "marked_spam": null,
               "blocked_by": null,
               "all_replies": null,
               "following": false,
               "blocking": null,
               "following_received": null,
               "id": 562773398,
               "followed_by": false
           },
           "target": {
               "following_requested": null,
               "following": false,
               "id": 42816371,
               "id_str": "42816371",
               "screen_name": "asahi",
               "followed_by": false,
               "following_received": null
           }
       }
   }


GET friendships/no_retweets/ids
======================================================================
GET friendships/no_retweets/ids はリツイートを受信したくないユーザーを得る機能だ。
Twitter ではユーザーごとにリツイートを受信するか否かを選択することが可能で、
例えば POST friendships/update を用いて受信設定を更新する。

次にサンプルコードを示す。

.. literalinclude:: /_sample/ptt/friendships-no_retweets-ids.py
   :language: python3

* [1] これは引数を一切取らない。

次に実行例を示す。
当方誰でもウェルカムなので空のデータが返ってくる。

.. code-block:: console

   $ ./friendships-no_retweets-ids.py
   []

POST friendships/update
======================================================================
POST friendships/update は指定ユーザーに対して、
リツイート受信または彼に対する何らかのイベント通知の有無設定を更新する機能だ。

次にサンプルコードを示す。

.. literalinclude:: /_sample/ptt/friendships-update.py
   :language: python3

* [1] 対象ユーザーをいつものようにパラメーター ``user_id`` または ``screen_name`` のどちらか一方で指定する。
  リツイート通知もプッシュ通知も有効にしたい。

次に実行例を示す。自分で自分の通知をオンにする。

.. code-block:: console

   $ ./friendships-update.py
   {
       "relationship": {
           "target": {
               "screen_name": "showa_yojyo",
               "followed_by": false,
               "id_str": "461058152",
               "id": 461058152,
               "following_received": false,
               "following_requested": null,
               "following": false
           },
           "source": {
               "screen_name": "showa_yojyo",
               "want_retweets": false,
               "blocking": false,
               "id_str": "461058152",
               "id": 461058152,
               "following_received": null,
               "following_requested": false,
               "followed_by": false,
               "all_replies": false,
               "muting": false,
               "notifications_enabled": false,
               "can_dm": false,
               "marked_spam": false,
               "blocked_by": false,
               "following": false
           }
       }
   }

機能しなかったようだ。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-twitter.txt
