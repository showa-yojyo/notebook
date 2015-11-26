======================================================================
検索関連
======================================================================
ツイートを対象とする検索 REST API はただひとつしかない。

.. contents::

GET search/tweets
======================================================================
単純な検索を行うには ``search/tweets`` を利用する。

.. literalinclude:: /_sample/ptt/search-tweets.py
   :language: python3

* Comment 1: ``ネシカ`` または ``nesica`` という単語を含むツイートを
  33 件検索させようとしている（厳密には不正確なやり方だが）。

  検索したい単語等をメソッド ``search.tweets`` に与える。
  キーワード引数の指定方法にコツがあるようだが、詳しくは
  https://dev.twitter.com/rest/reference/get/search/tweets 参照。

* Comment 2: 検索結果の本体は、関数戻り値からこのように得られる。
  この例ではツイートのタイムスタンプ、ユーザー名、本文だけをコンソールに出力する。

  * 日付は標準時 (``+0000``) で得られる？

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-twitter.txt
