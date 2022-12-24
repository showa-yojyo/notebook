======================================================================
ダイレクトメッセージ関連
======================================================================

ダイレクトメッセージを操作する各機能について記す。これもまた個人的にまったく活用
しない機能の一つだ。

.. contents::

POST direct_messages/new
======================================================================

POST direct_messages/new はダイレクトメッセージを作成・送信する機能だ。パラメー
ターは送信先のユーザーとテキストしかない。

次に利用例を示す。

.. literalinclude:: /_sample/ptt/direct_messages-new.py
   :language: python3

* [1] 自分宛てにダイレクトメッセージを送信する。
* [2] 実行結果を出力する。

次に実行例を示す。

.. code:: console

   bash$ ./direct_messages-new.py
   {
       "created_at": "Fri Dec 18 13:41:06 +0000 2015",
       "entities": {
           "hashtags": [],
           "symbols": [],
           "urls": [],
           "user_mentions": []
       },
       "id": 677846047566114819,
       "id_str": "677846047566114819",
       "recipient": {
           "contributors_enabled": false,
           "created_at": "Wed Jan 11 12:01:03 +0000 2012",
           "default_profile": false,
           "default_profile_image": false,
           "description": "実は電子の世界の人で現実には存在しない。",
           "entities": {
               "description": {
                   "urls": []
               },
               "url": {
                   "urls": [
                       {
                           "display_url": "github.com/showa-yojyo",
                           "expanded_url": "https://github.com/showa-yojyo",
                           "indices": [
                               0,
                               23
                           ],
                           "url": "https://t.co/YxrYqoZQ1r"
                       }
                   ]
               }
           },
           "favourites_count": 701,
           "follow_request_sent": false,
           "followers_count": 24,
           "following": false,
           "friends_count": 0,
           "geo_enabled": false,
           "has_extended_profile": false,
           "id": 461058152,
           "id_str": "461058152",
           "is_translation_enabled": true,
           "is_translator": false,
           "lang": "ja",
           "listed_count": 2,
           "location": "東京都区内",
           "name": "プレハブ小屋",
           "notifications": false,
           "profile_background_color": "FFFFFF",
           "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/678214720462020608/70eusxt6.png",
           "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/678214720462020608/70eusxt6.png",
           "profile_background_tile": true,
           "profile_banner_url": "https://pbs.twimg.com/profile_banners/461058152/1450531542",
           "profile_image_url": "http://pbs.twimg.com/profile_images/678206878820642816/7o08Gvb9_normal.png",
           "profile_image_url_https": "https://pbs.twimg.com/profile_images/678206878820642816/7o08Gvb9_normal.png",
           "profile_link_color": "FF1493",
           "profile_sidebar_border_color": "FFFFFF",
           "profile_sidebar_fill_color": "DDEEF6",
           "profile_text_color": "333333",
           "profile_use_background_image": true,
           "protected": false,
           "screen_name": "showa_yojyo",
           "statuses_count": 7407,
           "time_zone": "Tokyo",
           "url": "https://t.co/YxrYqoZQ1r",
           "utc_offset": 32400,
           "verified": false
       },
       "recipient_id": 461058152,
       "recipient_id_str": "461058152",
       "recipient_screen_name": "showa_yojyo",
       "sender": {
           ...
       },
       "sender_id": 461058152,
       "sender_id_str": "461058152",
       "sender_screen_name": "showa_yojyo",
       "text": "いい感じでモジャってますね。"
   }

GET direct_messages/show
======================================================================

GET direct_messages/show は既存のダイレクトメッセージの情報を取得する機能だ。先
述のように ID を指定してメッセージを取り扱う。

次に利用例を示す。先ほどのメッセージの情報を得る。

.. literalinclude:: /_sample/ptt/direct_messages-show.py
   :language: python3

* [1] PTT ルールにより、公式のパラメーター名が ``id`` の場合は ``_id`` と書き換
  えて指定する必要がある。
* [2] 実行結果を出力する。

実行結果例は上述の POST direct_messages/new の例と同様なので省略する。

GET direct_messages
======================================================================

GET direct_messages は自分へ送られたダイレクトメッセージを取得する機能だ。基本的
にはツイート取得系のインターフェイスと同じパラメーターを受け付ける。ただし、取得
可能なメッセージ数の上限が 200 件と決まっている（本当なのか）。

次に利用例を示す。

.. literalinclude:: /_sample/ptt/direct_messages.py
   :language: python3

* [1] 通信データ量をなるべく小さくするようなパラメーターを与えてリクエストを送信
  する。
* [2] 実行結果を出力する。

実行結果例は上述の GET direct_messages/sent の例と同様なので省略する。

GET direct_messages/sent
======================================================================

GET direct_messages/sent は自分が送ったダイレクトメッセージを取得する機能だ。最
大 800 件。

次に利用例を示す。

.. literalinclude:: /_sample/ptt/direct_messages-sent.py
   :language: python3

* [1] これがダイレクトメッセージのヘビーユーザーならば、オプション
  ``since_id``, ``max_id``,  ``page`` 等を駆使してページング処理をする。
  しかし私はダイレクトメッセージ箱が空なので、これでよい。

* [2] 実行結果を出力する。

POST direct_messages/destroy
======================================================================

POST direct_messages/destroy はダイレクトメッセージを削除する機能だ。ダイレクト
メッセージオブジェクトには一意な ID が与えられているので、この ID を指定してメッ
セージを取り扱う。

次に利用例を示す。

.. literalinclude:: /_sample/ptt/direct_messages-destroy.py
   :language: python3

* [1] PTT ルールにより、公式のパラメーター名が ``id`` の場合は ``_id`` と書き換
  えて指定する必要がある。
* [2] 実行結果を出力する。

実行結果例は上述の POST direct_messages/new の例と同様なので省略する。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-twitter.txt
