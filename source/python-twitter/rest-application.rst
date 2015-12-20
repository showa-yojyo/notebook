======================================================================
アプリケーション関連
======================================================================
本節では Twitter REST API の application 系機能について記す。
と言ってはみたものの、実のところ利用するものは一つだけだ。

.. contents::

GET application/rate_limit_status
======================================================================
GET application/rate_limit_status は現在の API 利用制限状況を知る機能だ。
例えばツイートを短時間に連続投稿するには限度があるわけだが、
今からどのくらいの時間帯にどれだけツイートすることが可能かを具体的に知ることができる。

.. literalinclude:: /_sample/ptt/application-rate_limit_status.py
   :language: python3

* [1] 状況を知りたい機能の一つ上位の単位の名前をいくつかまとめる CSV 文字列を組む。
  欲張って全部のインターフェイスを指定するとおそらく良くないことが起こる。

* [2] パラメーター ``resources`` として CSV 文字列を与え、リクエストを送信する。

* [3] 受信内容を出力する。

次に実行例を示す。長くなるので一部を省略する。

.. code-block:: console

   $ ./application-rate_limit_status.py
   {
       "resources": {
           "users": {
               "/users/show/:id": {
                   "reset": 1450622609,
                   "remaining": 181,
                   "limit": 181
               },
               ...
           },
           "statuses": {
               "/statuses/user_timeline": {
                   "reset": 1450622609,
                   "remaining": 180,
                   "limit": 180
               },
               ...
           },
           "lists": {
               "/lists/subscribers/show": {
                   "reset": 1450622609,
                   "remaining": 15,
                   "limit": 15
               },
               ...
           },
           "search": {
               "/search/tweets": {
                   "reset": 1450622609,
                   "remaining": 180,
                   "limit": 180
               }
           }
       },
       "rate_limit_context": {
           "access_token": "..."
       }
   }

ここで ``reset`` だけがわかりにくいので説明を加える。
これは利用制限の再設定がかかる時刻を POSIX 時刻表現で表した数値だ。
見慣れた時刻表現にするならば、
Python 標準のメソッド ``datetime.datetime.fromtimestamp`` を利用する等の方法がある。

.. code-block:: pycon

   >>> import datetime
   >>> datetime.datetime.fromtimestamp(1450622609).strftime('%c')
   'Sun Dec 20 23:43:29 2015'

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-twitter.txt
