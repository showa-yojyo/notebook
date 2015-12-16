======================================================================
トレンド関連
======================================================================
Twitter REST API のトレンド関連 3 機能について記す。
これらの機能は個人的には積極的に利用したことがこれまでなかったので、
API を操作することで何か発見があれば儲けものだ。

.. contents::

GET trends/available
======================================================================
GET trends/available は他の機能のパラメーターとして指定する WOEID という型の有効な値の一覧を取得するために用いる。
この機能自身はまったく引数を取らないので、サンプルコードは至って質素なものになる。

.. literalinclude:: /_sample/ptt/trends-available.py
   :language: python3

次に実行例を示す。極めて長くなるので大部分をカットした。

.. code-block:: console

   $ ./trends-available.py
   [
       {
           "name": "Worldwide",
           "country": "",
           "url": "http://where.yahooapis.com/v1/place/1",
           "parentid": 0,
           "woeid": 1,
           "placeType": {
               "name": "Supername",
               "code": 19
           },
           "countryCode": null
       },
       {
           "name": "Winnipeg",
           "country": "Canada",
           "url": "http://where.yahooapis.com/v1/place/2972",
           "parentid": 23424775,
           "woeid": 2972,
           "placeType": {
               "name": "Town",
               "code": 7
           },
           "countryCode": "CA"
       },
       {
           "name": "Ottawa",
           "country": "Canada",
           "url": "http://where.yahooapis.com/v1/place/3369",
           "parentid": 23424775,
           "woeid": 3369,
           "placeType": {
               "name": "Town",
               "code": 7
           },
           "countryCode": "CA"
       },
   ... 略 ...
       {
           "name": "Okayama",
           "country": "Japan",
           "url": "http://where.yahooapis.com/v1/place/90036018",
           "parentid": 23424856,
           "woeid": 90036018,
           "placeType": {
               "name": "Town",
               "code": 7
           },
           "countryCode": "JP"
       }
   ]

日本に興味があるのならば ``dump`` する直前に ``country`` が ``Japan`` な項目をフィルターしておくとよい。
インターネットを検索すれば、既に誰かがまとめた表を見られるだろう。

GET trends/closest
======================================================================
GET trends/closest は指定地点を対応できる WOEID を取得する機能なのだろう。
緯度と経度を指定する必要がある。

次にサンプルコードを示す。

.. literalinclude:: /_sample/ptt/trends-closest.py
   :language: python3

* [1] 東京都千代田区某所の緯度・経度を指定して API にアクセスする。
  緯度と経度は ``lat`` と ``long`` のパラメーターでそれぞれ指定する。

* [2] 応答結果を出力する。

次に実行例を示す。

.. code-block:: console

   $ ./trends-closest.py
   [
       {
           "country": "Japan",
           "placeType": {
               "code": 7,
               "name": "Town"
           },
           "url": "http://where.yahooapis.com/v1/place/1118370",
           "parentid": 23424856,
           "name": "Tokyo",
           "woeid": 1118370,
           "countryCode": "JP"
       }
   ]

Twitter はトレンドを管理するときに東京という規模の括りを設けているようだ。
千代田区だとか、それ以下には局所的にならなそうだ。

GET trends/place
======================================================================
GET trends/place は指定する場所でトレンドとなっているものを得る機能だ。
サンプルコードを示す。これは東京でのトレンドを Twitter から取得し、画面に出力する。

.. literalinclude:: /_sample/ptt/trends-place.py
   :language: python3

* [1] PTT では公式のパラメーター名が ``id`` であるものをなぜか ``_id`` として指定する必要がある。
  ここでの実引数は上述の ``Tokyo`` における WOEID 値だ。

  本サンプルでは指定していないが、ハッシュタグを取得しないオプションも提供されている。
  その場合は ``exclude='hashtags'`` をキーワード引数とする。

* [2] 応答結果を出力する。

次に実行例を示す。かなり長いので一部のみ掲載する。

.. code-block:: console

   $ ./trends-place.py
   [
       {
           "trends": [
               {
                   "name": "サイレーン",
                   "url": "http://twitter.com/search?q=%E3%82%B5%E3%82%A4%E3%83%AC%E3%83%BC%E3%83%B3",
                   "promoted_content": null,
                   "tweet_volume": 195007,
                   "query": "%E3%82%B5%E3%82%A4%E3%83%AC%E3%83%BC%E3%83%B3"
               },
               {
                   "name": "コナミ退社",
                   "url": "http://twitter.com/search?q=%E3%82%B3%E3%83%8A%E3%83%9F%E9%80%80%E7%A4%BE",
                   "promoted_content": null,
                   "tweet_volume": null,
                   "query": "%E3%82%B3%E3%83%8A%E3%83%9F%E9%80%80%E7%A4%BE"
               },
               {
                   "name": "俺の股間",
                   "url": "http://twitter.com/search?q=%E4%BF%BA%E3%81%AE%E8%82%A1%E9%96%93",
                   "promoted_content": null,
                   "tweet_volume": 11680,
                   "query": "%E4%BF%BA%E3%81%AE%E8%82%A1%E9%96%93"
               },
   ... 略 ...
           ],
           "as_of": "2015-12-15THH:MM:SSZ",
           "created_at": "2015-12-15THH:MM:SSZ",
           "locations": [
               {
                   "name": "Japan",
                   "woeid": 23424856
               }
           ]
       }
   ]

各項目内 ``query`` の文字列を ``urllib.unquote(query).decode('utf8')`` するのがよいかもしれない。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-twitter.txt
