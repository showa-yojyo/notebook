======================================================================
タイムラインおよびツイート関連
======================================================================
本節では statuses 系 API について述べる。

.. contents::

GET statuses/mentions_timeline
======================================================================
いわゆるリプを取得する例を挙げる。

.. literalinclude:: /_sample/ptt/statuses-mentions_timeline.py
   :language: python3

* Comment 1: 認証ユーザーに関する mentions を最新のものから 50 件取得する。

  https://dev.twitter.com/rest/reference/get/statuses/mentions_timeline 参照。

* Comment 2: ここでは mention の日時とツイート本文を新しい順にコンソールに出力している。

GET statuses/user_timeline
======================================================================
ユーザー名を指定してタイムラインを 40 件取得し、
ツイート時刻と投稿内容をコンソールに出力するコードである。

.. literalinclude:: /_sample/ptt/statuses-mentions_timeline.py
   :language: python3

引数仕様は https://dev.twitter.com/rest/reference/get/statuses/user_timeline を参照。

ちなみに、ドキュメント上は ``screen_name`` か ``user_id`` が
optional パラメーターとなっている API について注意が必要だ。
むしろ「そのうちのどちらかが required パラメーターである」という意味だろう。

GET statuses/home_timeline
======================================================================
ユーザーのタイムラインを取得する例を示す。

.. literalinclude:: /_sample/ptt/statuses-home_timeline.py
   :language: python3

* Comment 1: 自作モジュールのメソッドを呼び出している。前述のとおり。

* Comment 2: 認証ユーザーのタイムラインを最新のものから 10 件取得する。
  主に自分のツイート、フォローしているユーザーのツイート、返信各種からなるものと思われる。

  キーワード引数の意味や、戻り値のデータ構造については
  https://dev.twitter.com/rest/reference/get/statuses/home_timeline 参照。

* Comment 3: ツイートの日時と本文を新しい順にコンソールに出力している。

  .. caution::

     Python 3.4 に移行した直後に起動したら、コンソール上のテキストが文字化けして読めなかった。
     結局、環境変数 PYTHONIOENCODING を新規設定して、値を utf-8 と定義したら正常に読めるようになった。

POST statuses/update
======================================================================
スクリプト等からツイートするときには本 API を使用することになる。

.. literalinclude:: /_sample/ptt/statuses-update.py
   :language: python3

* Comment 1: tweet 内容を文字列として定義してみる。
* Comment 2: 関数 ``statuses.update`` をキーワード引数 ``status`` を指示して呼び出す。

  https://dev.twitter.com/rest/reference/post/statuses/update 参照。

POST statuses/update_with_media
======================================================================
稼働実績なし。

.. literalinclude:: /_sample/ptt/statuses-update_with_media.py
   :language: python3
