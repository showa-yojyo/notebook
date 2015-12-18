======================================================================
ダイレクトメッセージ関連
======================================================================
ダイレクトメッセージを操作する各機能について記す。
これもまた個人的にまったく活用しない機能の一つだ。

.. contents::

POST direct_messages/new
======================================================================
POST direct_messages/new はダイレクトメッセージを作成・送信する機能だ。
パラメーターは送信先のユーザーとテキストしかない。

次に利用例を示す。

.. literalinclude:: /_sample/ptt/direct_messages-new.py
   :language: python3

* [1] 自分宛てにダイレクトメッセージを送信する。
* [2] 実行結果を出力する。

次に実行例を示す。

.. code-block:: console

   $ ./direct_messages-new.py
   {
       "sender_id": 461058152,
       "created_at": "Fri Dec 18 13:41:06 +0000 2015",
       "recipient_id": 461058152,
       "recipient_screen_name": "showa_yojyo",
       "sender_id_str": "461058152",
       "text": "いい感じでモジャってますね。"
       "entities": {
           "urls": [],
           "symbols": [],
           "user_mentions": [],
           "hashtags": []
       },
       "id_str": "677846047566114819",
       "id": 677846047566114819,
       "sender": {
           "profile_sidebar_border_color": "FFFFFF",
           "created_at": "Wed Jan 11 12:01:03 +0000 2012",
           "profile_banner_url": "https://pbs.twimg.com/profile_banners/461058152/1447250161",
           "screen_name": "showa_yojyo",
           "id_str": "461058152",
           "contributors_enabled": false,
           "default_profile": false,
           "is_translation_enabled": true,
           "profile_image_url": "http://pbs.twimg.com/profile_images/518444238069968896/9swnzcfK_normal.png",
           "is_translator": false,
           "profile_sidebar_fill_color": "DDEEF6",
           "description": "実は電子の世界の人で現実には存在しない。",
           "followers_count": 24,
           "time_zone": "Tokyo",
           "id": 461058152,
           "name": "プレハブ小屋",
           "location": "東京都区内",
           "listed_count": 2,
           "favourites_count": 700,
           "friends_count": 0,
           "profile_link_color": "FF1493",
           "statuses_count": 7375,
           "profile_image_url_https": "https://pbs.twimg.com/profile_images/518444238069968896/9swnzcfK_normal.png",
           "profile_use_background_image": true,
           "profile_text_color": "333333",
           "default_profile_image": false,
           "lang": "ja",
           "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/557620683388108800/RoH3aAq8.png",
           "geo_enabled": false,
           "verified": false,
           "notifications": false,
           "following": false,
           "protected": false,
           "utc_offset": 32400,
           "profile_background_tile": true,
           "entities": {
               "url": {
                   "urls": [
                       {
                           "indices": [
                               0,
                               23
                           ],
                           "expanded_url": "https://showa-yojyo.github.io/",
                           "url": "https://t.co/HiE41wLa5W",
                           "display_url": "showa-yojyo.github.io"
                       }
                   ]
               },
               "description": {
                   "urls": []
               }
           },
           "has_extended_profile": false,
           "url": "https://t.co/HiE41wLa5W",
           "follow_request_sent": false,
           "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/557620683388108800/RoH3aAq8.png",
           "profile_background_color": "FFFFFF"
       },
       "recipient": {
           ... 略 ...
       },
       "recipient_id_str": "461058152",
       "sender_screen_name": "showa_yojyo"
   }

GET direct_messages/show
======================================================================
GET direct_messages/show は既存のダイレクトメッセージの情報を取得する機能だ。
先述のように ID を指定してメッセージを取り扱う。

次に利用例を示す。先ほどのメッセージの情報を得る。

.. literalinclude:: /_sample/ptt/direct_messages-show.py
   :language: python3

* [1] PTT ルールにより、公式のパラメーター名が ``id`` の場合は
  ``_id`` と書き換えて指定する必要がある。

* [2] 実行結果を出力する。

実行結果例は上述の POST direct_messages/new の例と同様なので省略する。

GET direct_messages
======================================================================
GET direct_messages は自分へ送られたダイレクトメッセージを取得する機能だ。
基本的にはツイート取得系のインターフェイスと同じパラメーターを受け付ける。
ただし、取得可能なメッセージ数の上限が 200 件と決まっている（本当なのか）。

次に利用例を示す。

.. literalinclude:: /_sample/ptt/direct_messages.py
   :language: python3

* [1] 通信データ量をなるべく小さくするようなパラメーターを与えてリクエストを送信する。

* [2] 実行結果を出力する。

次に実行例を示す。

.. code-block:: console

   $ ./direct_messages.py
   [
       {
           "recipient": {
               ... 略 ...
           },
           "id_str": "677846047566114819",
           "sender": {
               ... 略 ...
           },
           "recipient_id": 461058152,
           "text": "いい感じでモジャってますね。",
           "created_at": "Fri Dec 18 13:41:06 +0000 2015",
           "recipient_id_str": "461058152",
           "id": 677846047566114819,
           "sender_id_str": "461058152",
           "sender_id": 461058152,
           "sender_screen_name": "showa_yojyo",
           "recipient_screen_name": "showa_yojyo"
       },
       {
          ... 略 ...
       },
       ... 略 ...
   ]

実行結果例は上述の GET direct_messages/sent の例と同様なので省略する。

GET direct_messages/sent
======================================================================
GET direct_messages/sent は自分が送ったダイレクトメッセージを取得する機能だ。
最大 800 件。

次に利用例を示す。

.. literalinclude:: /_sample/ptt/direct_messages-sent.py
   :language: python3

* [1] これがダイレクトメッセージのヘビーユーザーならば、オプション
  ``since_id``, ``max_id``,  ``page`` 等を駆使してページング処理をする。
  しかし私はダイレクトメッセージ箱が空なので、これでよい。

* [2] 実行結果を出力する。

POST direct_messages/destroy
======================================================================
POST direct_messages/destroy はダイレクトメッセージを削除する機能だ。
ダイレクトメッセージオブジェクトには一意な ID が与えられているので、
この ID を指定してメッセージを取り扱う。

次に利用例を示す。

.. literalinclude:: /_sample/ptt/direct_messages-destroy.py
   :language: python3

* [1] PTT ルールにより、公式のパラメーター名が ``id`` の場合は
  ``_id`` と書き換えて指定する必要がある。

* [2] 実行結果を出力する。

実行結果例は上述の POST direct_messages/new の例と同様なので省略する。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-twitter.txt
