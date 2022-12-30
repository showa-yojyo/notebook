======================================================================
トレンド関連
======================================================================

Twitter REST API のトレンド関連三機能について記す。これらの機能は個人的には積極
的に利用したことがこれまでなかったので、 API を操作することで何か発見があれば儲
けものだ。

.. contents::

GET trends/available
======================================================================

GET trends/available は他の機能のパラメーターとして指定する WOEID という型の有効
な値の一覧を取得するために用いる。この機能自身はまったく引数を取らないので、サン
プルコードは至って質素なものになる。

.. literalinclude:: /_sample/ptt/trends-available.py
   :language: python3

次に実行例を示す。極めて長くなるので大部分をカットした。

.. code:: console

   bash$ ./trends-available.py
   [
       {
           "country": "",
           "countryCode": null
           "name": "Worldwide",
           "parentid": 0,
           "placeType": {
               "code": 19,
               "name": "Supername"
           },
           "url": "http://where.yahooapis.com/v1/place/1",
           "woeid": 1
       },
       {
           "country": "Canada",
           "countryCode": "CA",
           "name": "Winnipeg",
           "parentid": 23424775,
           "placeType": {
               "code": 7,
               "name": "Town"
           },
           "url": "http://where.yahooapis.com/v1/place/2972",
           "woeid": 2972
       },
       ...
       {

           "country": "Japan",
           "countryCode": "JP",
           "name": "Okayama",
           "parentid": 23424856,
           "placeType": {
               "code": 7,
               "name": "Town"
           },
           "url": "http://where.yahooapis.com/v1/place/90036018",
           "woeid": 90036018
       }
   ]

日本に興味があるのならば ``dump`` する直前に ``country`` が ``Japan`` な項目を
フィルターしておくとよい。インターネットを検索すれば、既に誰かがまとめた表を見ら
れるだろう。

GET trends/closest
======================================================================

GET trends/closest は指定地点を対応できる WOEID を取得する機能なのだろう。緯度と
経度を指定する必要がある。

次にサンプルコードを示す。

.. literalinclude:: /_sample/ptt/trends-closest.py
   :language: python3

* [1] 東京都千代田区某所の緯度・経度を指定して API にアクセスする。緯度と経度は
  ``lat`` と ``long`` のパラメーターでそれぞれ指定する。
* [2] 応答結果を出力する。

次に実行例を示す。

.. code:: console

   bash$ ./trends-closest.py
   [
       {
           "country": "Japan",
           "countryCode": "JP",
           "name": "Tokyo",
           "parentid": 23424856,
           "placeType": {
               "code": 7,
               "name": "Town"
           },
           "url": "http://where.yahooapis.com/v1/place/1118370",
           "woeid": 1118370
       }
   ]

Twitter はトレンドを管理するときに東京という規模の括りを設けているようだ。千代田
区だとか、それ以下には局所的にならなそうだ。

GET trends/place
======================================================================

GET trends/place は指定する場所でトレンドとなっているものを得る機能だ。サンプル
コードを示す。これは東京でのトレンドを Twitter から取得し、画面に出力する。

.. literalinclude:: /_sample/ptt/trends-place.py
   :language: python3

* [1] PTT では公式のパラメーター名が ``id`` であるものをなぜか ``_id`` として指
  定する必要がある。ここでの実引数は上述の ``Tokyo`` における WOEID 値だ。

  本サンプルでは指定していないが、ハッシュタグを取得しないオプションも提供されて
  いる。その場合は ``exclude='hashtags'`` をキーワード引数とする。
* [2] 応答結果を出力する。

次に実行例を示す。かなり長いので一部のみ掲載する。

.. code:: console

   bash$ ./trends-place.py
   [
       {
           "as_of": "2015-12-15THH:MM:SSZ",
           "created_at": "2015-12-15THH:MM:SSZ",
           "locations": [
               {
                   "name": "Japan",
                   "woeid": 23424856
               }
           ],
           "trends": [
               {
                   "name": "サイレーン",
                   "promoted_content": null,
                   "query": "%E3%82%B5%E3%82%A4%E3%83%AC%E3%83%BC%E3%83%B3",
                   "tweet_volume": 195007,
                   "url": "http://twitter.com/search?q=%E3%82%B5%E3%82%A4%E3%83%AC%E3%83%BC%E3%83%B3"
               },
               {
                   "name": "コナミ退社",
                   "promoted_content": null,
                   "tweet_volume": null,
                   "query": "%E3%82%B3%E3%83%8A%E3%83%9F%E9%80%80%E7%A4%BE",
                   "url": "http://twitter.com/search?q=%E3%82%B3%E3%83%8A%E3%83%9F%E9%80%80%E7%A4%BE"
               },
               {
                   "name": "俺の股間",
                   "promoted_content": null,
                   "query": "%E4%BF%BA%E3%81%AE%E8%82%A1%E9%96%93",
                   "tweet_volume": 11680,
                   "url": "http://twitter.com/search?q=%E4%BF%BA%E3%81%AE%E8%82%A1%E9%96%93"
               },
               ...
           ]
       }
   ]

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-twitter.txt
