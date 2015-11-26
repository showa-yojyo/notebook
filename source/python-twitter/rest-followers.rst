======================================================================
フォロワー関連
======================================================================
本節では followers, friends, friendships 系 REST API について記す。
メインは friendships 系である。

.. contents::

GET friends/list
======================================================================
特定のユーザーがフォローしている全ユーザーの情報を得るのには GET friends/list を利用できる。
一度のリクエストでは返しきれないほどの多数のユーザーをフォローしていることを想定してのカーソル処理となる。
次に示すコード例のように、1 ページずつデータをリクエストすることになる。

.. literalinclude:: /_sample/ptt/friends-list.py
   :language: python3

GET followers/list
======================================================================
特定のユーザーをフォローしている全ユーザーの情報を得るのには GET followers/list を利用できる。
サンプルコードは先のコードをテキストエディターで ``s/friends/followers/`` すれば得られる。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-twitter.txt
