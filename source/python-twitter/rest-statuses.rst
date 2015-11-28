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

POST statuses/update
======================================================================
POST statuses/update はツイートを投稿する API だ。

.. literalinclude:: /_sample/ptt/statuses-update.py
   :language: python3

* [1] tweet 内容を文字列として定義してみる。
* [2] 関数 ``statuses.update`` をキーワード引数 ``status`` を指示して呼び出す。

POST statuses/update_with_media
======================================================================
稼働実績なし。

.. literalinclude:: /_sample/ptt/statuses-update_with_media.py
   :language: python3
