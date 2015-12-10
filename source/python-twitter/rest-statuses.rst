======================================================================
タイムラインおよびツイート関連
======================================================================
本節では statuses 系 API について述べる。

.. contents::

GET statuses/mentions_timeline
======================================================================
GET statuses/mentions_timeline はいわゆるリプを取得する API である。
次に利用例を挙げる。

.. literalinclude:: /_sample/ptt/statuses-mentions_timeline.py
   :language: python3

* [1] 認証ユーザーに関する mentions を最新のものから 50 件取得する。
  取得データをなるべく軽量化したいので、色々とオプションを設定している。

* [2] ここでは mention の日時とツイート本文を新しい順に標準出力に出力している。

実行例を示す。自分で自分に話しかけているツイートが多いので後半をカットした。

.. code-block:: console

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
GET statuses/user_timeline は指定ユーザーによるツイートを得られる API である。

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

.. code-block:: console

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
GET statuses/retweets_of_me は他の人がリツイートした自分のツイートを新しい順に得る API だ。

.. literalinclude:: /_sample/ptt/statuses-retweets_of_me.py
   :language: python3

GET statuses/retweets/:id
======================================================================
GET statuses/retweets/:id は指定ツイートの直近 100 リツイートまでを得る API だ。
ツイートを指定するにはツイートの ID があらかじめ必要となる。
自由に使えるサンプルツイートがないため、サンプルコードを省略する。

GET statuses/show/:id
======================================================================
GET statuses/show/:id は指定ツイートの詳細を得る API だ。
このように利用する。

.. literalinclude:: /_sample/ptt/statuses-show-id.py
   :language: python3

実行結果省略。

POST statuses/destroy/:id
======================================================================
POST statuses/destroy/:id は自分のツイートに限るが、指定ツイートを削除する API だ。
一度に一ツイートだけを削除するに過ぎないので、使い勝手は悪いと思われる。

POST statuses/update
======================================================================
POST statuses/update はツイートを投稿する API だ。

.. literalinclude:: /_sample/ptt/statuses-update.py
   :language: python3

* [1] ツイート内容を文字列として定義してみる。
* [2] 関数 ``statuses.update`` をキーワード引数 ``status`` を指示して呼び出す。

.. todo:: この例は物足りないので、変わった例を示す。

POST statuses/retweet/:id
======================================================================
POST statuses/retweet/:id は指定ツイートを自分のアカウントからリツイートする API だ。
ツイートを指定するにはツイートの ID があらかじめ必要となる。

POST statuses/update_with_media
======================================================================
ドキュメントによると
<This endpoint has been DEPRECATED.
Please use POST statuses/update for uploading one or more media entities>
とのことなので、この API は忘れ去ってしまったようがよい。

GET statuses/oembed
======================================================================
特定のツイートを oEmbed 互換な書式で得る API だ。
これは HTML 文書の中に埋め込むコード片としてツイートを表現するためのものだろう。

最低限のパラメーターでリクエストを送信しよう。

.. literalinclude:: /_sample/ptt/statuses-oembed.py
   :language: python3

キーワード引数 ``url`` で対象ツイートの URL を指定した。
Twitter のドキュメントによると URL を指定する代わりに ``id`` としてツイート ID を指定することもできるとある。
しかし、私が試したところではエラー 34 すなわち Sorry, that page does not exist メッセージが返ってきた。
PTT のドキュメントによると Python 側のキーワード引数名を ``_id`` にする必要があるとのことだ。

.. code-block:: python3

   response = tw.statuses.oembed(_id=674636677982257152)

そういうわけで実行例を示す。
JSON データの ``html`` の値が確かに HTML コード片になっている。

.. code-block:: console

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
リツイートしたユーザーの ID を得る API だ。
サンプルコード省略。

GET statuses/lookup
======================================================================
GET statuses/lookup はツイートの詳細を得る API で、一度に 100 件まで処理できる。
使いどころが難しい？

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-twitter.txt
