======================================================================
アプリケーション関連
======================================================================

本節では Twitter REST API の application 系機能について記す。と言ってはみたもの
の、実のところ利用するものは一つだけだ。

.. contents::

GET application/rate_limit_status
======================================================================

GET application/rate_limit_status は現在の API 利用制限状況を知る機能だ。例えば
ツイートを短時間に連続投稿するには限度があるわけだが、今からどのくらいの時間帯に
どれだけツイートすることが可能かを具体的に知ることができる。

.. literalinclude:: /_sample/ptt/application-rate_limit_status.py
   :language: python3

* [1] 状況を知りたい機能の一つ上位の単位の名前をいくつかまとめる CSV 文字列を組
  む。欲張って全部のインターフェイスを指定するとおそらく良くないことが起こる。
* [2] パラメーター ``resources`` として CSV 文字列を与え、リクエストを送信する。
* [3] 受信内容を出力する。

次に実行例を示す。長くなるので一部を省略する。

.. code:: console

   bash$ ./application-rate_limit_status.py
   {
       "rate_limit_context": {
           "access_token": "..."
       },
       "resources": {
           "lists": {
               "/lists/list": {
                   "limit": 15,
                   "remaining": 15,
                   "reset": 1450622609
               },
               ...
           },
           "search": {
               "/search/tweets": {
                   "limit": 180,
                   "remaining": 180,
                   "reset": 1450622609
               }
           },
           "statuses": {
               "/statuses/friends": {
                   "limit": 15,
                   "remaining": 15,
                   "reset": 1450622609
               },
               ...
           },
           "users": {
               "/users/derived_info": {
                   "limit": 15,
                   "remaining": 15,
                   "reset": 1450622609
               },
               ...
           }
       }
   }

ここで ``reset`` だけがわかりにくいので説明を加える。これは利用制限の再設定がか
かる時刻を POSIX 時刻表現で表した数値だ。見慣れた時刻表現にするならば、Python 標
準のメソッド ``datetime.datetime.fromtimestamp`` を利用する等の方法がある。

.. code:: pycon

   >>> import datetime
   >>> datetime.datetime.fromtimestamp(1450622609).strftime('%c')
   'Sun Dec 20 23:43:29 2015'

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-twitter.txt
