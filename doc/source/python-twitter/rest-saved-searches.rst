======================================================================
検索履歴関連
======================================================================

本節では saved_searches 系の応用について記す。私が愛用している Twitter クライア
ントに頻用検索用語集を埋め込んだことにより、現在ではまったく用いなくなったもので
ある。

.. contents::

GET saved_searches/list
======================================================================

リクエスト時の認証と Twitter ログインとで共通するアカウントでかつて検索したクエ
リーの一覧を取得する。実行してみれば理解できる。

.. literalinclude:: /_sample/ptt/saved_searches-list.py
   :language: python3

上の例では、何も検索していなかった場合には、空のリストが出力される。

GET saved_searches/show:id
======================================================================

GET saved_searches/show:id は保存済みの検索クエリーの詳細を得るのに用いる機能だ
が、これを利用する機会はないだろう。なぜなら実際に目的のクエリーの ID を知ってい
る必要があるはずだが、それならば先述の GET saved_searches/list のほうがパラメー
ターを指示することなく、より強い情報を得られる。

.. literalinclude:: /_sample/ptt/saved_searches-show-id.py
   :language: python3

* [1] パラメーター名は本来 ``id`` だが、PTT ルールでは ``_id`` と書く。

実行結果を示す。

.. code:: console

   bash$ ./saved_searches-show-id.py
   [{'created_at': 'Fri Nov 27 14:14:19 +0000 2015',
     'id': 4378204334,
     'id_str': '4378204334',
     'name': 'イルベロ OR イルマティックエンベロープ',
     'position': None,
     'query': 'イルベロ OR イルマティックエンベロープ'}]

POST saved_searches/create
======================================================================

わかりにくい言い方をすると「保存した検索」項目を一つ新しく作成するための機能だ。
個人的には今となっては使い途がなくなってしまった。

.. literalinclude:: /_sample/ptt/saved_searches-create.py
   :language: python3

実行結果を示す。

.. code:: console

   bash$ ./saved_searches-list.py
   [{'created_at': 'Fri Nov 27 14:14:19 +0000 2015',
     'id': 4378204334,
     'id_str': '4378204334',
     'name': 'イルベロ OR イルマティックエンベロープ',
     'position': None,
     'query': 'イルベロ OR イルマティックエンベロープ'}]

POST saved_searches/destroy/:id
======================================================================

POST saved_searches/destroy/:id は保存済みの検索クエリーをひと削除する機能だ。た
だしクエリーを指定する方法は ID の指定による。

.. literalinclude:: /_sample/ptt/saved_searches-destroy.py
   :language: python3

成功時の実行レスポンスは上述の POST saved_searches/create と同じように見える。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-twitter.txt
