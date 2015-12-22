======================================================================
場所関連
======================================================================
ユーザー設定にもよるが、これから投稿するツイートに地球上のどこかの場所を関連付けることができる。
その機能に関係する利用可能なリクエストは名前が geo/xxx の形をしており、今のところ 3 個ほどある。
本節では PTT を用いてこれらを実行するには、どのようにコードを書くのか、
どういう注意点があるのか等について記す。

.. contents::

GET geo/id/:place_id
======================================================================
GET geo/id/:place_id は場所 ID というものを指定して、その詳細情報を得るのに用いる。
場所 ID の具体的な値は別にある GET geo/reverse_geocode 等の応答データから知ることになる。

次に PTT によるサンプルコードを示す。
コロンが付くインターフェイスの呼び出しはいつもとやり方が異なるので覚えておきたい。

.. literalinclude:: /_sample/ptt/geo-id-place_id.py
   :language: python3

* [1] ``Twitter`` オブジェクトのメソッド名とキーワード引数の付け方がこのようになる。
  ``place_id`` という文字列がコードのどこにも出てこないが、このようにしなければ動作しない。

  ここで指定している場所 ID の値は、
  後述する GET geo/reverse_geocode のサンプルコードにて得られたものの一つを流用している。

* [2] GET geo/id/:place_id から受信した JSON データをほぼ忠実にコンソールに出力する。

次に実行例を示す。

.. code-block:: console

   $ geo-id-place_id.py
   {
       "attributes": {
           "190533:id": "city_13_101"
       },
       "bounding_box": {
           "coordinates": [
               [
                   [
                       139.730511000003,
                       35.6663720001634
                   ],
                   [
                       139.730511000003,
                       35.7017300013607
                   ],
                   [
                       139.779853999959,
                       35.7017300013607
                   ],
                   [
                       139.779853999959,
                       35.6663720001634
                   ],
                   [
                       139.730511000003,
                       35.6663720001634
                   ]
               ]
           ],
           "type": "Polygon"
       },
       "centroid": [
           139.748980818553,
           35.6839603639963
       ],
       "contained_within": [
           {
               "attributes": {},
               "bounding_box": {
                   "coordinates": [
                       [
                           [
                               138.946976001637,
                               24.2247179989435
                           ],
                           [
                               138.946976001637,
                               35.8941379990039
                           ],
                           [
                               142.239272999512,
                               35.8941379990039
                           ],
                           [
                               142.239272999512,
                               24.2247179989435
                           ],
                           [
                               138.946976001637,
                               24.2247179989435
                           ]
                       ]
                   ],
                   "type": "Polygon"
               },
               "centroid": [
                   139.460189420286,
                   35.6976500888796
               ],
               "country": "日本",
               "country_code": "JP",
               "full_name": "日本 東京都",
               "id": "a56612250c754f23",
               "name": "東京都",
               "place_type": "admin",
               "url": "https://api.twitter.com/1.1/geo/id/a56612250c754f23.json"
           }
       ],
       "country": "日本",
       "country_code": "JP",
       "full_name": "東京都 千代田区",
       "geometry": null,
       "id": "28b9063fdce43645",
       "name": "千代田区",
       "place_type": "city",
       "polylines": [],
       "url": "https://api.twitter.com/1.1/geo/id/28b9063fdce43645.json"
   }

とにかく東京都千代田区のどこかだという情報が得られた。

POST geo/place
======================================================================
POST geo/place はドキュメントによると
<As of December 2nd, 2013, this endpoint is deprecated and retired and no longer functions>
とのことなので、この API は忘れてよい。

どうやら緯度経度の値を指定して場所オブジェクトなるものを生成する機能だったらしい。

GET geo/reverse_geocode
======================================================================
GET geo/reverse_geocode は基本的には緯度経度を与えて、
Twitter API が取り扱える値としての場所 ID を得ることができる。

次に PTT によるサンプルコードを示す。

.. literalinclude:: /_sample/ptt/geo-reverse_geocode.py
   :language: python3

* [1] この例では入力必須引数のみを指示して呼び出す。
  所望の緯度と経度を ``lat`` と ``long`` としてそれぞれ指示すればよい。

* [2] Twitter からの JSON データをほぼ忠実にコンソールに出力する。

次に実行例を示す（一部加工済み）。

.. code-block:: console

   $ geo-reverse_geocode.py
   {
       "query": {
           "params": {
               "accuracy": 0.0,
               "coordinates": {
                   "coordinates": [
                       139.773828,
                       35.696805
                   ],
                   "type": "Point"
               },
               "granularity": "neighborhood"
           },
           "type": "reverse_geocode",
           "url": "https://api.twitter.com/1.1/geo/reverse_geocode.json?lat=35.696805&long=139.773828&oauth_consumer_key=pBXKrfuhVW14XWnE4Mvm9Tfs6&oauth_nonce=14150764466553511811&oauth_signature_method=HMAC-SHA1&oauth_timestamp=1450728413&oauth_token=461058152-4G46kPHscjTXfl0skuoPdmwJfHd2QJSTSgtzvfTb&oauth_version=1.0&oauth_signature=9C1Fy%2FfWtHPNJl%2BwK%2Fw8gzGaF70%3D"
       },
       "result": {
           "places": [
               {
                   "attributes": {},
                   "bounding_box": {
                       "coordinates": [
                           [
                               [
                                   139.730511000003,
                                   35.6663720001634
                               ],
                               [
                                   139.730511000003,
                                   35.7017300013607
                               ],
                               [
                                   139.779853999959,
                                   35.7017300013607
                               ],
                               [
                                   139.779853999959,
                                   35.6663720001634
                               ],
                               [
                                   139.730511000003,
                                   35.6663720001634
                               ]
                           ]
                       ],
                       "type": "Polygon"
                   },
                   "centroid": [
                       139.748980818553,
                       35.6839603639963
                   ],
                   "contained_within": [
                       {
                           "attributes": {},
                           "bounding_box": {
                               "coordinates": [
                                   [
                                       [
                                           138.946976001637,
                                           24.2247179989435
                                       ],
                                       [
                                           138.946976001637,
                                           35.8941379990039
                                       ],
                                       [
                                           142.239272999512,
                                           35.8941379990039
                                       ],
                                       [
                                           142.239272999512,
                                           24.2247179989435
                                       ],
                                       [
                                           138.946976001637,
                                           24.2247179989435
                                       ]
                                   ]
                               ],
                               "type": "Polygon"
                           },
                           "centroid": [
                               139.460189420286,
                               35.6976500888796
                           ],
                           "country": "日本",
                           "country_code": "JP",
                           "full_name": "日本 東京都",
                           "id": "a56612250c754f23",
                           "name": "東京都",
                           "place_type": "admin",
                           "url": "https://api.twitter.com/1.1/geo/id/a56612250c754f23.json"
                       }
                   ],
                   "country": "日本",
                   "country_code": "JP",
                   "full_name": "東京都 千代田区",
                   "id": "28b9063fdce43645",
                   "name": "千代田区",
                   "place_type": "city",
                   "url": "https://api.twitter.com/1.1/geo/id/28b9063fdce43645.json"
               },
               {
                   "attributes": {},
                   "bounding_box": {
                       "coordinates": [
                           [
                               [
                                   138.400956002244,
                                   24.2247179989435
                               ],
                               [
                                   138.400956002244,
                                   37.1512180002819
                               ],
                               [
                                   142.239272999512,
                                   37.1512180002819
                               ],
                               [
                                   142.239272999512,
                                   24.2247179989435
                               ],
                               [
                                   138.400956002244,
                                   24.2247179989435
                               ]
                           ]
                       ],
                       "type": "Polygon"
                   },
                   "centroid": [
                       139.644023323251,
                       36.0251385011289
                   ],
                   "contained_within": [
                       {
                           "attributes": {},
                           "bounding_box": {
                               "coordinates": [
                                   [
                                       [
                                           122.933197001144,
                                           24.0456418391239
                                       ],
                                       [
                                           122.933197001144,
                                           45.5227849999761
                                       ],
                                       [
                                           145.817458998856,
                                           45.5227849999761
                                       ],
                                       [
                                           145.817458998856,
                                           24.0456418391239
                                       ],
                                       [
                                           122.933197001144,
                                           24.0456418391239
                                       ]
                                   ]
                               ],
                               "type": "Polygon"
                           },
                           "centroid": [
                               143.330213688502,
                               43.4604070037548
                           ],
                           "country": "日本",
                           "country_code": "JP",
                           "full_name": "日本",
                           "id": "06ef846bfc783874",
                           "name": "日本",
                           "place_type": "country",
                           "url": "https://api.twitter.com/1.1/geo/id/06ef846bfc783874.json"
                       }
                   ],
                   "country": "日本",
                   "country_code": "JP",
                   "full_name": "日本 関東地方",
                   "id": "d473ed704dbcd4a5",
                   "name": "関東地方",
                   "place_type": "admin",
                   "url": "https://api.twitter.com/1.1/geo/id/d473ed704dbcd4a5.json"
               },
               {
                   "attributes": {},
                   "bounding_box": {
                       "coordinates": [
                           [
                               [
                                   138.946976001637,
                                   24.2247179989435
                               ],
                               [
                                   138.946976001637,
                                   35.8941379990039
                               ],
                               [
                                   142.239272999512,
                                   35.8941379990039
                               ],
                               [
                                   142.239272999512,
                                   24.2247179989435
                               ],
                               [
                                   138.946976001637,
                                   24.2247179989435
                               ]
                           ]
                       ],
                       "type": "Polygon"
                   },
                   "centroid": [
                       139.460189420286,
                       35.6976500888796
                   ],
                   "contained_within": [
                       {
                           "attributes": {},
                           "bounding_box": {
                               "coordinates": [
                                   [
                                       [
                                           122.933197001144,
                                           24.0456418391239
                                       ],
                                       [
                                           122.933197001144,
                                           45.5227849999761
                                       ],
                                       [
                                           145.817458998856,
                                           45.5227849999761
                                       ],
                                       [
                                           145.817458998856,
                                           24.0456418391239
                                       ],
                                       [
                                           122.933197001144,
                                           24.0456418391239
                                       ]
                                   ]
                               ],
                               "type": "Polygon"
                           },
                           "centroid": [
                               143.330213688502,
                               43.4604070037548
                           ],
                           "country": "日本",
                           "country_code": "JP",
                           "full_name": "日本",
                           "id": "06ef846bfc783874",
                           "name": "日本",
                           "place_type": "country",
                           "url": "https://api.twitter.com/1.1/geo/id/06ef846bfc783874.json"
                       }
                   ],
                   "country": "日本",
                   "country_code": "JP",
                   "full_name": "日本 東京都",
                   "id": "a56612250c754f23",
                   "name": "東京都",
                   "place_type": "admin",
                   "url": "https://api.twitter.com/1.1/geo/id/a56612250c754f23.json"
               },
               {
                   "attributes": {},
                   "bounding_box": {
                       "coordinates": [
                           [
                               [
                                   122.933197001144,
                                   24.0456418391239
                               ],
                               [
                                   122.933197001144,
                                   45.5227849999761
                               ],
                               [
                                   145.817458998856,
                                   45.5227849999761
                               ],
                               [
                                   145.817458998856,
                                   24.0456418391239
                               ],
                               [
                                   122.933197001144,
                                   24.0456418391239
                               ]
                           ]
                       ],
                       "type": "Polygon"
                   },
                   "centroid": [
                       143.330213688502,
                       43.4604070037548
                   ],
                   "contained_within": [],
                   "country": "日本",
                   "country_code": "JP",
                   "full_name": "日本",
                   "id": "06ef846bfc783874",
                   "name": "日本",
                   "place_type": "country",
                   "url": "https://api.twitter.com/1.1/geo/id/06ef846bfc783874.json"
               }
           ]
       }
   }

JSON データの ``result`` -> ``places`` 以下に色々と興味深いデータがある。
指定した場所は実は秋葉原の柳森神社なのだが、
``places`` として 4 項目が得られており、それぞれ領域の規模が異なっている。
Twitter は場所を点というより（地球面上の）矩形領域として扱うようだ。

GET geo/search
======================================================================
GET geo/search は緯度経度は言うに及ばず、地名、IP アドレス、地所等から、
もしそこからツイートを投稿したらどんな場所 ID が付随するのかを返すものと思われる。

次に PTT によるサンプルコードを示す。

.. literalinclude:: /_sample/ptt/geo-search.py
   :language: python3

* [1] パラメーター ``query`` のみを指定して GET geo/search を呼び出したい。
  しかもクエリー文言は単に「千代田区」とする。

* [2] Twitter からの JSON データをほぼ忠実にコンソールに出力する。

実行例の一部を示す。全部ここに載せたいのだが、
興味深いことに千葉県八千代市、群馬県千代田町、名古屋市千種区、茨城県八千代町、
兵庫県神戸市長田区、北海道札幌市清田区、長野県御代田町等も候補として返っており、
紙幅の都合上ほとんどを省略する。

.. code-block:: console

   $ geo-search.py
   {
       "query": {
           "params": {
               "accuracy": 0.0,
               "autocomplete": false,
               "granularity": "neighborhood",
               "query": "千代田区",
               "trim_place": false
           },
           "type": "search",
           "url": "https://api.twitter.com/1.1/geo/search.json?oauth_consumer_key=pBXKrfuhVW14XWnE4Mvm9Tfs6&oauth_nonce=11546684270722490170&oauth_signature_method=HMAC-SHA1&oauth_timestamp=1450728486&oauth_token=461058152-4G46kPHscjTXfl0skuoPdmwJfHd2QJSTSgtzvfTb&oauth_version=1.0&query=%E5%8D%83%E4%BB%A3%E7%94%B0%E5%8C%BA&oauth_signature=HH4avR8cHYW8fs198a9vAWfAH74%3D"
       },
       "result": {
           "places": [
               {
                   "attributes": {},
                   "bounding_box": {
                       "coordinates": [
                           [
                               [
                                   139.730511000003,
                                   35.6663720001634
                               ],
                               [
                                   139.730511000003,
                                   35.7017300013607
                               ],
                               [
                                   139.779853999959,
                                   35.7017300013607
                               ],
                               [
                                   139.779853999959,
                                   35.6663720001634
                               ],
                               [
                                   139.730511000003,
                                   35.6663720001634
                               ]
                           ]
                       ],
                       "type": "Polygon"
                   },
                   "centroid": [
                       139.748980818553,
                       35.6839603639963
                   ],
                   "contained_within": [
                       {
                           "attributes": {},
                           "bounding_box": {
                               "coordinates": [
                                   [
                                       [
                                           138.946976001637,
                                           24.2247179989435
                                       ],
                                       [
                                           138.946976001637,
                                           35.8941379990039
                                       ],
                                       [
                                           142.239272999512,
                                           35.8941379990039
                                       ],
                                       [
                                           142.239272999512,
                                           24.2247179989435
                                       ],
                                       [
                                           138.946976001637,
                                           24.2247179989435
                                       ]
                                   ]
                               ],
                               "type": "Polygon"
                           },
                           "centroid": [
                               139.460189420286,
                               35.6976500888796
                           ],
                           "country": "日本",
                           "country_code": "JP",
                           "full_name": "日本 東京都",
                           "id": "a56612250c754f23",
                           "name": "東京都",
                           "place_type": "admin",
                           "url": "https://api.twitter.com/1.1/geo/id/a56612250c754f23.json"
                       }
                   ],
                   "country": "日本",
                   "country_code": "JP",
                   "full_name": "東京都 千代田区",
                   "id": "28b9063fdce43645",
                   "name": "千代田区",
                   "place_type": "city",
                   "url": "https://api.twitter.com/1.1/geo/id/28b9063fdce43645.json"
               },
               ...
           ]
       }
   }

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-twitter.txt
