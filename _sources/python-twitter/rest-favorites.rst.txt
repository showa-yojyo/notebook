======================================================================
お気に入り関連
======================================================================

現在ではお気に入りとは呼ばず、当世風にいいねという名前になってしまったが、本稿で
は旧式の用語のままにしておく。以下、星マークとある箇所をハートマークをする等、旧
用語は順次読み替えて欲しい。

.. contents::

POST favorites/create
======================================================================

POST favorites/create はツイートを一つ指定して、それをお気に入りとする機能だ。

次にサンプルコードを示す。

.. literalinclude:: /_sample/ptt/favorites-create.py
   :language: python3

* [1] ツイート ID をパラメーター ``id`` として指定することになっているが、PTT で
  は ``_id`` として値を渡すのが無難だ。

  また、応答データが少しでも軽くなるように ``include_entities=False`` を明示的に
  指定しておく。
* [2] 返信データ、すなわち指定したツイートオブジェクトを出力する。

POST favorites/destroy
======================================================================

POST favorites/destroy は自分のお気に入りツイートを一つ選択して解除する機能だ。

次にサンプルコードを示す。POST favorites/create と同じ形式になる。

.. literalinclude:: /_sample/ptt/favorites-destroy.py
   :language: python3

GET favorites/list
======================================================================

GET favorites/list は特定のユーザーが星マークを付けたツイート群を取得する機能
だ。

次にサンプルコードを示す。

.. literalinclude:: /_sample/ptt/favorites-list.py
   :language: python3

* [1] ここで示すのは、それほど多くはない決まった数量のツイートを取得する方法とな
  る。パラメーター ``count`` に 200 までの値を指定することができる。

  なお 200 を超える量のデータを得たい場合は、パラメーター ``max_id`` をうまく利
  用すること。詳しくは :doc:`./rest` 参照。
* [2] ツイートオブジェクトを含むデータを出力する。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-twitter.txt
