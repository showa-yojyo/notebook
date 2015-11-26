======================================================================
ユーザーアカウント関連
======================================================================
本節では users 系 API の応用方法について述べる。

.. contents::

GET users/show
======================================================================
特定のユーザーの詳細情報を得るのに ``users/show`` を利用する。

.. literalinclude:: /_sample/ptt/users-show.py
   :language: python3

* Comment 1: 基本的に指定する引数はこれだけで構わない。
* Comment 2: ユーザーの Twitter 情報を出力してみる。
* https://dev.twitter.com/rest/reference/get/users/show 参照。

GET users/search
======================================================================
``users/search`` はキーワードから何か関係のありそうなユーザーを探すのにたいへん便利だ。
応用例としては、例えば bot に関係しそうなユーザーを可能な限りかき集めて、
ひとつのリストにまとめるといったものが考えられる（私はそれを実践している）。

これはごく単純な呼び出し例なので、キーワード引数
``count`` の上限である 20 ユーザーしか取得できない。
さらに取得するには、この API の呼び出しをループの中に入れて、
キーワード引数 ``page`` をループカウンターで指定するとよいだろう。
その際には関数 ``time.sleep`` 等でリクエストに時間的間隔を設けると申し分ない。

.. literalinclude:: /_sample/ptt/users-search.py
   :language: python3

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-twitter.txt
