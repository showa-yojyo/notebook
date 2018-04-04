======================================================================
アカウント設定関連
======================================================================
本節では PTT による、Twitter アカウント設定関連のインターフェイスの利用方法を記す。

.. contents::

GET account/verify_credentials
======================================================================
GET account/verify_credentials は自分の credentials が効力があるのかを試すのに用いる機能らしい。
正当な場合は自分を表現するユーザーオブジェクトが得られる。

サンプルコードを示す。

.. literalinclude:: /_sample/ptt/account-verify_credentials.py
   :language: python3

* [1] 適当にオプションを指定して Twitter にリクエストを送信する。
* [2] 自分を表現するオブジェクトを受信したはずなので、それを画面に出力する。

次に実行例を示す。

.. code:: console

   $ ./account-verify_credentials.py
   {
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
   }

見慣れたデータが得られた。

POST account/remove_profile_banner
======================================================================
POST account/remove_profile_banner は自分の Twitter のページのバナー画像を削除する機能だ。

次にサンプルコードを示す。

.. literalinclude:: /_sample/ptt/account-remove_profile_banner.py
   :language: python3

* [1] まったくオプションがない。
* [2] ドキュメントによると単に HTTP 200 が返るらしい。

次に実行例を示す。

.. code:: console

   $ ./account-remove_profile_banner.py
   {
       "code": 200
   }

実行後に Twitter の自分のページを目視で確認したところ、確かにバナー画像が消滅していた。

GET account/settings
======================================================================
GET account/settings は自分のアカウント設定情報を得る機能だ。
次にサンプルコードを示す。

.. literalinclude:: /_sample/ptt/account-settings-g.py
   :language: python3

* [1] 実は account/settings には POST 版もあるため、
  PTT に間違わせないように ``_method=GET`` と指示する。
  Twitter のインターフェイスとしては、このリクエストは引数を取らない。

* [2] 受信データを画面に出力する。

次に実行例を示す。

.. code:: console

   $ ./account-settings.py
   {
       "allow_contributor_request": "all",
       "allow_dm_groups_from": "following",
       "allow_dms_from": "all",
       "always_use_https": true,
       "discoverable_by_email": true,
       "discoverable_by_mobile_phone": false,
       "display_sensitive_media": false,
       "geo_enabled": false,
       "language": "ja",
       "protected": false,
       "screen_name": "showa_yojyo",
       "sleep_time": {
           "enabled": true,
           "end_time": 0,
           "start_time": 3
       },
       "smart_mute": false,
       "time_zone": {
           "name": "Tokyo",
           "tzinfo_name": "Asia/Tokyo",
           "utc_offset": 32400
       },
       "trend_location": [
           {
               "country": "Japan",
               "countryCode": "JP",
               "name": "東京",
               "parentid": 23424856,
               "placeType": {
                   "code": 7,
                   "name": "Town"
               },
               "url": "http://where.yahooapis.com/v1/place/1118370",
               "woeid": 1118370
           }
       ],
       "use_cookie_personalization": true
   }

見慣れたプロパティーもあれば、そうでないのもある。

POST account/settings
======================================================================
POST account/settings は自分のアカウント設定情報を更新する機能だ。

.. literalinclude:: /_sample/ptt/account-settings-p.py
   :language: python3

* [1] 先ほど述べた理由により ``_method=POST`` も併せて指示する。

  * スリープタイム系のパラメーターのタイムゾーンは、現時点での設定値が基準になる？
    それとも同時に設定しているタイムゾーンの値になる？

* [2] 処理結果を画面に出力する。

次に実行例を示す。

.. code:: console

   $ ./account-settings-p.py
   {
       "allow_contributor_request": "all",
       "allow_dm_groups_from": "following",
       "allow_dms_from": "all",
       "always_use_https": true,
       "discoverable_by_email": true,
       "discoverable_by_mobile_phone": false,
       "display_sensitive_media": false,
       "geo_enabled": false,
       "language": "ja",
       "protected": false,
       "screen_name": "showa_yojyo",
       "sleep_time": {
           "enabled": true,
           "end_time": 0,
           "start_time": 3
       },
       "smart_mute": false,
       "time_zone": {
           "name": "Tokyo",
           "tzinfo_name": "Asia/Tokyo",
           "utc_offset": 32400
       },
       "trend_location": [
           {
               "country": "Japan",
               "countryCode": "JP",
               "name": "東京",
               "parentid": 23424856,
               "placeType": {
                   "code": 7,
                   "name": "Town"
               },
               "url": "http://where.yahooapis.com/v1/place/1118370",
               "woeid": 1118370
           }
       ],
       "use_cookie_personalization": true
   }

問題なさそうだ。

POST account/update_delivery_device
======================================================================
これは動かない。

.. POST account/update_delivery_device は自分のアカウントに対するリツイートや返信等の通知を設定する機能だ。
.. 
.. .. literalinclude:: /_sample/ptt/account-update_delivery_device.py
..    :language: python3
.. 
.. * [1] パラメーターは ``device`` しかない。
..   しかも有効な選択肢は ``none`` または ``sms`` しかない。
.. 
.. * [2] 処理結果を画面に出力する。
.. 
.. 次に実行例を示す。
.. 
.. .. code:: console
.. 
..    $ ./account-update_delivery_device.py

POST account/update_profile
======================================================================
POST account/update_profile は自分のプロフィール部分の更新をする機能だ。
次にサンプルコードを示す。

.. literalinclude:: /_sample/ptt/account-update_profile.py
   :language: python3

* [1] 指定可能なすべてのパラメーターを全部使う。
* [2] 処理結果を画面に出力する。

次に実行例を示す。

.. code:: console

   $ ./account-update_profile.py
   {
       "contributors_enabled": false,
       "created_at": "Wed Jan 11 12:01:03 +0000 2012",
       "default_profile": false,
       "default_profile_image": false,
       "description": "実は電子の世界の人で現実には存在しない。",
       "entities": {
           "description": {
               "urls": []
           }
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
           },
       },
       "favourites_count": 700,
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
       "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/557620683388108800/RoH3aAq8.png",
       "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/557620683388108800/RoH3aAq8.png",
       "profile_background_tile": true,
       "profile_image_url": "http://pbs.twimg.com/profile_images/518444238069968896/9swnzcfK_normal.png",
       "profile_image_url_https": "https://pbs.twimg.com/profile_images/518444238069968896/9swnzcfK_normal.png"
       "profile_link_color": "FF1493",
       "profile_location": null,
       "profile_sidebar_border_color": "FFFFFF",
       "profile_sidebar_fill_color": "DDEEF6",
       "profile_text_color": "333333",
       "profile_use_background_image": true,
       "protected": false,
       "screen_name": "showa_yojyo",
       "statuses_count": 7382,
       "time_zone": "Tokyo",
       "url": "https://t.co/YxrYqoZQ1r",
       "utc_offset": 32400,
       "verified": false,
   }

どうも ``include_entities`` が効いていない？

POST account/update_profile_banner
======================================================================
POST account/update_profile_banner は自分の Twitter のページのバナー画像を更新する機能だ。
実際にはローカルにある画像ファイルのバイナリーデータをアップロードすることになる。
Twitter API としては、引数 ``banner`` に base64 エンコードされたバイナリーデータを与えるが、
PTT としてはバイナリーモードで開いた画像ファイルを渡すだけでもよい。
メソッド内部でその辺の面倒な処理を代行してくれる。
自力でエンコードする場合は、別途 PTT 用のパラメーター指定 ``_base64=True`` が必要となる。

これらを踏まえたサンプルコードを次に示す。

.. literalinclude:: /_sample/ptt/account-update_profile_banner.py
   :language: python3

* [1] あらかじめバナー画像を用意しておく。
  Python での通常の方法により、ファイルデータをバイナリーとして持っておく。

* [2] パラメーター ``banner`` のみを指示してリクエストを送信する。
  スクリプトからの相対パス ``profile-banner.png`` がバナー用画像ファイルである。

  .. hint::

     実は寸法とオフセットのパラメーターを指定して試したら、
     期待通りの結果が得られなかったのでサンプルコードを没とした。

* [3] 処理結果を画面に出力する。

次に実行例を示す。

.. code:: console

   $ ./account-update_profile_banner.py
   {}

ドキュメントの仕様に反して空のデータが戻ってきた。
しかし Twitter クライアントを用いて自分のページを開いたところ、
期待通りの画像を表示するようになったことを確認できた。

POST account/update_profile_image
======================================================================
POST account/update_profile_image はたぶんユーザーのアイコンの画像の更新をする機能だ。
やり方は上述のものと同様になる。

サンプルコードを次に示す。

.. literalinclude:: /_sample/ptt/account-update_profile_image.py
   :language: python3

* [1] あらかじめ画像を用意しておく。

* [2] アイコン画像ファイルを開いて、ファイルオブジェクトを得ておき、
  これをメソッドにキーワード引数 ``image`` として渡す。

* [3] 処理結果を画面に出力する。

次に実行例を示す。
出力はいつもの自分のユーザーオブジェクトなので興味のある所だけを示す。

.. code:: console

   $ ./account-update_profile_image.py
   {
       "default_profile_image": false,
       ...
       "profile_image_url": "http://pbs.twimg.com/profile_images/518444238069968896/9swnzcfK_normal.png",
       "profile_image_url_https": "https://pbs.twimg.com/profile_images/518444238069968896/9swnzcfK_normal.png",
       ...
   }

Twitter クライアント等を用いて画像が本当に更新されたかどうかを確認するためには、
このアップロード処理終了後に数秒間をおくとよい。

POST account/update_profile_background_image
======================================================================
POST account/update_profile_background_image は自分の Twitter のページの背景画像を更新する機能だ。
背景画像はあまりお目にかからない気がするが、例えばリスト画面で描画される画像だ。

画像を指定する方法はこれだけは二つある。

#. 画像データを base64 エンコードしたバイナリーデータをアップロードする
#. POST media/upload 済みの画像を ID で指定する

ここでは後者の方法を記す。サンプルコードは次のようになる。

.. literalinclude:: /_sample/ptt/account-update_profile_background_image.py
   :language: python3

* [1] あらかじめ画像を用意しておく。
  画像ファイルを開いて、ファイルオブジェクトを経て生バイナリーを抱えておく。

* [2] これをメソッドにキーワード引数 ``image`` として渡す。
  また、画像を反復させて描画したいので ``tile=True`` も指定する。

* [3] 処理結果を画面に出力する。

次に実行例を示す。
出力はいつもの自分のユーザーオブジェクトなので興味のある所だけを示す。

.. code:: console

   $ ./account-update_profile_background_image.py
   {
       ...
       "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/557620683388108800/RoH3aAq8.png",
       "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/557620683388108800/RoH3aAq8.png",
       "profile_background_tile": true,
       "profile_use_background_image": true
   }

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-twitter.txt
