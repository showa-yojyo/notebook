======================================================================
フォロワー関連
======================================================================
本節では followers 系 REST API について記す。
他人から自分に向かう関係の機能に followers の名前が含まれる。
インターフェイスは friends 系の対応する機能と一致している。

.. contents::

GET followers/ids
======================================================================
GET followers/ids は GET friends/ids のフォロワー版だ。
解説は :doc:`./rest-friends` を参照。

.. literalinclude:: /_sample/ptt/followers-ids.py
   :language: python3

GET followers/list
======================================================================
特定のユーザーをフォローしている全ユーザーの情報を得るのには GET followers/list を利用できる。
解説は :doc:`./rest-friends` を参照。

.. literalinclude:: /_sample/ptt/followers-list.py
   :language: python3

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-twitter.txt
