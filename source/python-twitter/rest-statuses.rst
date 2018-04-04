======================================================================
タイムラインおよびツイート関連
======================================================================
本節では statuses 系 API について述べる。

.. contents::

GET statuses/mentions_timeline
======================================================================
GET statuses/mentions_timeline はいわゆるリプを取得する機能だ。
次に利用例を挙げる。

.. literalinclude:: /_sample/ptt/statuses-mentions_timeline.py
   :language: python3

* [1] 認証ユーザーに関する mentions を最新のものから 50 件取得する。
  取得データをなるべく軽量化したいので、色々とオプションを設定している。

* [2] ここでは mention の日時とツイート本文を新しい順に標準出力に出力している。

実行例を示す。自分で自分に話しかけているツイートが多いので後半をカットした。

.. code:: console

   $ ./statuses-mentions_timeline.py
   Sun Feb 22 15:52:49 +0000 2015|@showa_yojyo 今さっき復旧したもよう。
   Sun Feb 22 15:44:10 +0000 2015|@showa_yojyo やっぱり固い。この私がレベル 300 いかないというのはおかしい。
   Sat Nov 29 15:57:40 +0000 2014|すいません。右クリックメニューが出ない。 RT @showa_yojyo: 今になって Python (command line) を ConEmu タブ化できるようにした。気付くのが遅い。
   Sun Oct 12 01:01:40 +0000 2014|@showa_yojyo しゅわっ
   Fri Jun 20 15:13:53 +0000 2014|@showa_yojyo 画面が死に掛けてるのはなぁお手上げですね、とりあえず分解するときはコンセントはもちろんバッテリーもぬいたほうが無難ですね、がんばってください
   Fri Jun 20 15:06:10 +0000 2014|@showa_yojyo たまにやりますが、割りに簡単ですわ、もっともそこそこのスペックならてきとうなフリーのOSでもぶち込んでつかいたいですけどねｗ大抵手元にくるのがぼろいやつなんでｗｗｗ
   Fri Jun 20 15:02:38 +0000 2014|@showa_yojyo はじめまして、ノーパソでしたら最悪分解して萌えないゴミでもまぁもんだいないですな、もしくはだれかに押し付けるというても参考までに
   Sat May 03 14:50:48 +0000 2014|@showa_yojyo Cygwin の git はバージョンが 1.7 くらいで、0.2 も違うからダメ。
   Fri Apr 25 17:54:29 +0000 2014|@showa_yojyo またボケた。単なる 79 待ちではないか。
   ...

GET statuses/user_timeline
======================================================================
GET statuses/user_timeline は指定ユーザーによるツイートを得られる機能だ。

次にユーザー名を指定してタイムラインを取得し、
ツイート時刻と投稿内容をコンソールに出力する例を示す。

.. literalinclude:: /_sample/ptt/statuses-user_timeline.py
   :language: python3

* [1] ユーザー名の指定には ``screen_name`` か ``user_id`` のどちらか一方を用いる。
* [2] 新しい順にツイートを標準出力に出力する。

GET statuses/home_timeline
======================================================================
自分のタイムラインを取得する例を示す。

.. literalinclude:: /_sample/ptt/statuses-home_timeline.py
   :language: python3

* [1] 認証ユーザー、自分のタイムラインを最新のものから 50 件取得する。
  主に自分のツイート、フォローしているユーザーのツイート、返信各種からなるものと思われる。

* [2] 新しい順にツイートを標準出力に出力する。

実行例を示す。途中は長いので省略。

.. code:: console

   $ ./statuses-home_timeline.py
   Fri Nov 27 16:58:39 +0000 2015|体が冷えまくり。
   Fri Nov 27 16:44:39 +0000 2015|[notebook] https://t.co/PUasyXX9lC showa_yojyo -(rest-saved-searches.rst) Complete saved_searches APIs.
   Fri Nov 27 16:44:39 +0000 2015|[notebook] https://t.co/Te1fC2FqxM showa_yojyo -(rest-lists.rst) Complete lists APIs.
   Fri Nov 27 16:44:20 +0000 2015|[bin] https://t.co/lpcHyV0WJT showa_yojyo - Implement friendships-(show|update) subcommands.
   Fri Nov 27 16:12:25 +0000 2015|今日の倍満。メンチンツモドライチ。 https://t.co/z7P4RLrN8w
   Fri Nov 27 15:55:20 +0000 2015|麻雀の練習しよう。
   ...
   Fri Nov 20 15:30:35 +0000 2015|ステパップ

GET statuses/retweets_of_me
======================================================================
GET statuses/retweets_of_me は他の人がリツイートした自分のツイートを新しい順に得る機能だ。

.. literalinclude:: /_sample/ptt/statuses-retweets_of_me.py
   :language: python3

GET statuses/retweets/:id
======================================================================
GET statuses/retweets/:id は指定ツイートの直近 100 リツイートまでを得る機能だ。
ツイートを指定するにはツイートの ID があらかじめ必要となる。

.. literalinclude:: /_sample/ptt/statuses-retweets-id.py
   :language: python3

* [1] パラメーター名が ``id`` のときは ``_id`` に書き換えるのが PTT ルール。

誰もリツイートしていないツイートを調べると次のようになる。

.. code:: console

   $ ./statuses-retweets-id.py
   []

GET statuses/show/:id
======================================================================
GET statuses/show/:id は指定ツイートの詳細を得る機能だ。
このように利用する。

.. literalinclude:: /_sample/ptt/statuses-show-id.py
   :language: python3

* [1] いつものようにパラメーター名が ``id`` のときは ``_id`` に書き換えるのが無難。

実行結果を次に示す。

.. code:: console

   $ ./statuses-show-id.py
   {'contributors': None,
    'coordinates': None,
    'created_at': 'Sun Oct 11 17:11:36 +0000 2015',
    'favorite_count': 0,
    'favorited': False,
    'geo': None,
    'id': 653256646810955776,
    'id_str': '653256646810955776',
    'in_reply_to_screen_name': None,
    'in_reply_to_status_id': None,
    'in_reply_to_status_id_str': None,
    'in_reply_to_user_id': None,
    'in_reply_to_user_id_str': None,
    'is_quote_status': False,
    'lang': 'ja',
    'place': None,
    'retweet_count': 0,
    'retweeted': False,
    'source': '<a href="https://github.com/showa_yojyo/iustus-iudex/" '
              'rel="nofollow">Iustus Iudex</a>',
    'text': 'ああ眠い。',
    'truncated': False,
    'user': {'id': 461058152, 'id_str': '461058152'}}

POST statuses/destroy/:id
======================================================================
POST statuses/destroy/:id は自分のツイートに限るが、指定ツイートを削除する機能だ。
一度に一ツイートだけを削除するに過ぎないので、使い勝手は悪いと思われる。

.. literalinclude:: /_sample/ptt/statuses-destroy-id.py
   :language: python3

* [1] いつものようにパラメーター名が ``id`` のときは ``_id`` に書き換えるのが無難。

実行結果を次に示す。

.. code:: console

   $ ./statuses-destroy-id.py
   {
       "contributors": null,
       "coordinates": null,
       "created_at": "Tue Dec 22 14:23:33 +0000 2015",
       "entities": {
           "hashtags": [],
           "symbols": [],
           "urls": [],
           "user_mentions": []
       },
       "favorite_count": 0,
       "favorited": false,
       "geo": null,
       "id": 679306282629619712,
       "id_str": "679306282629619712",
       "in_reply_to_screen_name": null,
       "in_reply_to_status_id": null,
       "in_reply_to_status_id_str": null,
       "in_reply_to_user_id": null,
       "in_reply_to_user_id_str": null,
       "is_quote_status": false,
       "lang": "en",
       "place": null,
       "retweet_count": 0,
       "retweeted": false,
       "source": "<a href=\"http://www.geocities.jp/showa_yojyo/\" rel=\"nofollow\">ホーリー・エンタープライズ</a>",
       "text": "Test",
       "truncated": false,
       "user": {
           "id": 461058152,
           "id_str": "461058152"
       }
   }

POST statuses/update
======================================================================
POST statuses/update はツイートを投稿する機能だ。

テキストだけをツイートする
----------------------------------------------------------------------

.. literalinclude:: /_sample/ptt/statuses-update.py
   :language: python3
   :lines: 1-18

* [1] ツイート内容を文字列として定義してみる。
* [2] 関数 ``statuses.update`` をキーワード引数 ``status`` を指示して呼び出す。

画像をツイートする
----------------------------------------------------------------------
画像ファイルのアップロード方法については :doc:`./rest-media` を参照。

.. literalinclude:: /_sample/ptt/statuses-update.py
   :language: python3
   :lines: 1-10,20-

* [3] あらかじめ POST media/upload で得られた ID を用いて、
  関数 ``statuses.update`` をキーワード引数 ``media_ids`` に指示して呼び出す。

  なお、複数の画像を同一ツイートに含めるには ``media_ids`` に ID を ``,`` で連結した文字列を与える。

POST statuses/retweet/:id
======================================================================
POST statuses/retweet/:id は指定ツイートを自分のアカウントからリツイートする機能だ。
ツイートを指定するにはツイートの ID があらかじめ必要となる。

.. literalinclude:: /_sample/ptt/statuses-retweet-id.py
   :language: python3

実行結果を次に示す。なぜか失敗した。

.. code:: console

   $ ./statuses-retweet-id.py
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
     File "./statuses-retweet-id.py", line 16, in <module>
       trim_user=True,)
     File "D:\Python35\lib\site-packages\twitter\api.py", line 312, in __call__
       return self._handle_response(req, uri, arg_data, _timeout)
     File "D:\Python35\lib\site-packages\twitter\api.py", line 345, in _handle_response
       raise TwitterHTTPError(e, uri, self.format, arg_data)
   twitter.api.TwitterHTTPError: Twitter sent status 403 for URL: 1.1/statuses/retweet/678987432331632643.json using parameters: (oauth_consumer_key=...)
   details: {'errors': [{'message': 'Retweet is not permissible for this status.','code': 328}]}

POST statuses/unretweet/:id
======================================================================
POST statuses/unretweet/:id は指定の retweet を解除するような機能だ。
先程と同様に ID で retweet を指定する。
ちょっとした注意をしておくと、仕様には
<When passing a source status ID instead of the retweet status ID
a HTTP 200 response will be returned with the same Tweet object but no action>
とあるので、元ツイートのそれを誤って指定しないようにする。

.. literalinclude:: /_sample/ptt/statuses-unretweet-id.py
   :language: python3

* [1] 自分側の ID をキーワード引数 ``_id`` に指定する。

実行結果を次に示す。
某ボットアカウントの ID が 708316560780185601 のツイートを私がリツイートして、
新たに ID が 708317138675630082 のツイートが生成されている。
ここでは後者の ID を指定する。

.. code:: console

   $ ./statuses-unretweet-id.py
   {
       "contributors": null,
       "coordinates": null,
       "created_at": "Fri Mar 11 15:42:20 +0000 2016",
       "entities": {
           "hashtags": [],
           "symbols": [],
           "urls": [
               {
                   "display_url": "twitter.com/eiken_1/status…",
                   "expanded_url": "https://twitter.com/eiken_1/status/708316560780185601",
                   "indices": [
                       30,
                       53
                   ],
                   "url": "https://t.co/xOBVFOcEyA"
               }
           ],
           "user_mentions": []
       },
       "favorite_count": 0,
       "favorited": false,
       "geo": null,
       "id": 708317138675630082,
       "id_str": "708317138675630082",
       "in_reply_to_screen_name": null,
       "in_reply_to_status_id": null,
       "in_reply_to_status_id_str": null,
       "in_reply_to_user_id": null,
       "in_reply_to_user_id_str": null,
       "is_quote_status": true,
       "lang": "ja",
       "place": null,
       "possibly_sensitive": false,
       "quoted_status": {
           "contributors": null,
           "coordinates": null,
           "created_at": "Fri Mar 11 15:40:02 +0000 2016",
           "entities": {
               "hashtags": [],
               "symbols": [],
               "urls": [
                   {
                       "display_url": "eiken-01.blogspot.jp/search/label/%…",
                       "expanded_url": "http://eiken-01.blogspot.jp/search/label/%E8%8B%B1%E6%A4%9C1%E7%B4%9A%E8%8B%B1%E5%8D%98%E8%AA%9E%20C?&max-results=1",
                       "indices": [
                           88,
                           111
                       ],
                       "url": "https://t.co/oC6grVE4di"
                   }
               ],
               "user_mentions": []
           },
           "favorite_count": 4,
           "favorited": false,
           "geo": null,
           "id": 708316560780185601,
           "id_str": "708316560780185601",
           "in_reply_to_screen_name": null,
           "in_reply_to_status_id": null,
           "in_reply_to_status_id_str": null,
           "in_reply_to_user_id": null,
           "in_reply_to_user_id_str": null,
           "is_quote_status": false,
           "lang": "ja",
           "place": null,
           "possibly_sensitive": false,
           "retweet_count": 0,
           "retweeted": false,
           "source": "<a href=\"http://eiken-001.seesaa.net/\" rel=\"nofollow\">英単語リスト＠英検１級英単語</a>",
           "text": "counterclockwise /kàuntəklɑ'kwaiz/　〔形〕〔副〕（米）反時計回り［左回り］の［に］（⇔clockwise，英ではanticlockwise） https://t.co/oC6grVE4di",
           "truncated": false,
           "user": {
               "id": 125180877,
               "id_str": "125180877"
           }
       },
       "quoted_status_id": 708316560780185601,
       "quoted_status_id_str": "708316560780185601",
       "retweet_count": 0,
       "retweeted": false,
       "source": "<a href=\"http://twitter.com\" rel=\"nofollow\">Twitter Web Client</a>",
       "text": "リツイートテスト。あとでリツイートを取り消すテストをする。 https://t.co/xOBVFOcEyA",
       "truncated": false,
       "user": {
           "id": 461058152,
           "id_str": "461058152"
       }
   }

ブラウザーで当該 retweet と元 tweet を見ると、
どのように処理されているのかが理解できるだろう。
以下にリンクを示す。

* https://twitter.com/showa_yojyo/status/708317138675630082
* https://twitter.com/eiken_1/status/708316560780185601

POST statuses/update_with_media
======================================================================
ドキュメントによると
<This endpoint has been DEPRECATED.
Please use POST statuses/update for uploading one or more media entities>
とのことなので、これは忘れ去ってしまったようがよい。

GET statuses/oembed
======================================================================
GET statuses/oembed は特定のツイートを oEmbed 互換な書式で得る機能だ。
これは HTML 文書の中に埋め込むコード片としてツイートを表現するためのものだろう。

最低限のパラメーターでリクエストを送信しよう。

.. literalinclude:: /_sample/ptt/statuses-oembed.py
   :language: python3

キーワード引数 ``url`` で対象ツイートの URL を指定した。
Twitter のドキュメントによると URL を指定する代わりに ``id`` としてツイート ID を指定することもできるとある。
しかし、私が試したところではエラー 34 すなわち Sorry, that page does not exist メッセージが返ってきた。
PTT のドキュメントによると Python 側のキーワード引数名を ``_id`` にする必要があるとのことだ。

.. code:: python3

   response = tw.statuses.oembed(_id=674636677982257152)

そういうわけで実行例を示す。
JSON データの ``html`` の値が確かに HTML コード片になっている。

.. code:: console

   $ ./statuses-oembed.py
   {'author_name': 'プレハブ小屋',
    'author_url': 'https://twitter.com/showa_yojyo',
    'cache_age': '3153600000',
    'height': None,
    'html': '<blockquote class="twitter-tweet"><p lang="ja" '
            'dir="ltr">ボワ～</p>&mdash; プレハブ小屋 (@showa_yojyo) <a '
            'href="https://twitter.com/showa_yojyo/status/674636677982257152">December '
            '9, 2015</a></blockquote>\n'
            '<script async src="//platform.twitter.com/widgets.js" '
            'charset="utf-8"></script>',
    'provider_name': 'Twitter',
    'provider_url': 'https://twitter.com',
    'type': 'rich',
    'url': 'https://twitter.com/showa_yojyo/statuses/674636677982257152',
    'version': '1.0',
    'width': 550}

GET statuses/retweeters/ids
======================================================================
GET statuses/retweeters/ids は指定ツイートの直近 100 リツイートまでに限定して、
リツイートしたユーザーの ID を得る機能だ。
サンプルコード省略。

GET statuses/lookup
======================================================================
GET statuses/lookup はツイートの詳細を得る機能で、一度に 100 件まで処理できる。
使いどころが難しい？

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-twitter.txt
