======================================================================
検索履歴関連
======================================================================
本節では saved_searches 系 API の応用について記す。
私が愛用している Twitter クライアントに頻用検索用語集を埋め込んだことにより、
現在ではまったく用いなくなったものである。

.. contents::

GET saved_searches/list
======================================================================
Twitter ログイン時に当該アカウントで検索したクエリーの一覧を取得する。
実行してみれば理解できる。

.. literalinclude:: /_sample/ptt/saved_searches-list.py
   :language: python3

GET saved_searches/create
======================================================================
わかりにくい言い方をすると「保存した検索」項目を一つ新しく作成するための API だ。
個人的には今となっては使い途がなくなってしまった API のひとつ。

.. literalinclude:: /_sample/ptt/saved_searches-create.py
   :language: python3

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-twitter.txt
