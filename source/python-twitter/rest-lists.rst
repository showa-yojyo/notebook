======================================================================
リスト関連
======================================================================
本節では lists 系 API の応用について記す。
私が Twitter の機能で最も利用するのがリストである。
特にリストへのユーザー登録処理を重視している。

.. contents::

GET lists/list
----------------------------------------------------------------------
全リスト取得に用いる API だ。

.. literalinclude:: /_sample/ptt/lists-list.py
   :language: python3

* Comment 1: メソッド ``lists.list`` に ``screen_name`` キーワード引数を与えて、
  そのユーザーの持っているリストを全部取得する。
  ユーザーが作成したリストに加え、もしあれば、購読している他ユーザーが作成したリストを含む。

  https://dev.twitter.com/rest/reference/get/lists/list 参照。

* Comment 2: 各リストの mode, full_name, description 各属性をコンソールに出力する。

GET lists/statuses
----------------------------------------------------------------------
既存のリストのタイムラインを閲覧するための API だ。
例えば ``screen_name`` が ``showa_yojyo`` のユーザーの、
``news`` という公開リストがあるという前提で、そのタイムラインを見てみよう。

.. literalinclude:: /_sample/ptt/lists-statuses.py
   :language: python3

* Comment 1

  * メソッド ``lists.statuses`` に与える引数を準備する。
    リストを特定する手段は一つではないのだが、
    分かりやすさを優先して ``slug`` および ``owner_screen_name`` を同時に指示する。

  * その他は https://dev.twitter.com/rest/reference/get/lists/statuses 参照。

* Comment 2

  * 文字列をコンソールに出力する。
    ツイート内容、改行、ツイート時刻、ツイートに利用したアプリ名が確認できる。

POST lists/members/destroy
----------------------------------------------------------------------
リストから指定したユーザーを削除するための API だ。
しかし、これを利用するくらいならばブラウザーで Twitter を利用するほうが早いやもしれない。

.. literalinclude:: /_sample/ptt/lists-members-destroy.py
   :language: python3

GET lists/memberships
----------------------------------------------------------------------
``lists/memberships`` リクエストは、
あるユーザーが他のユーザーが管理しているリストに含まれているとき、
そのようなリストを列挙するのに利用する。

.. literalinclude:: /_sample/ptt/lists-memberships.py
   :language: python3

* Comment 1: ユーザー ``showa_yojyo`` を含むリストをリクエストする。
  ``cursor`` については別項で詳しく解説する。

* Comment 2: 各リストの名前と説明文をコンソールに出力する。
  ``full_name`` の先頭にはリストの作者の ``screen_name`` が見えると思う。

* https://dev.twitter.com/rest/reference/get/lists/memberships 参照。

GET lists/subscribers
----------------------------------------------------------------------
指定リストの購読者をリストするのに利用する。
どうも非公開ユーザーが購読していてもリストされないらしい。

.. literalinclude:: /_sample/ptt/lists-subscribers.py
   :language: python3

POST lists/members/create_all
----------------------------------------------------------------------
ブラウザー上の操作ではできないと思われる、
一括でユーザーを複数指定して指定のリストに登録する処理を実現するための API だ。
次のサンプルコードの ``screen_names`` はスクリーンネームの tuple インスタンスを意味する。
この API はリストを多用する筆者が利用する頻度がもっとも高い。

.. literalinclude:: /_sample/ptt/lists-members-create_all.py
   :language: python3

GET lists/members/show
----------------------------------------------------------------------
指定ユーザーが指定リストに登録されているかを調べる API だ。
使い途が少々思いつかない。

.. literalinclude:: /_sample/ptt/lists-members-show.py
   :language: python3

GET lists/members
----------------------------------------------------------------------
指定リストに登録されているユーザーをすべて得ることができる API だ。
登録ユーザー数が多いリストに対しては、次のように
「カーソル処理」で複数回のリクエストをすることになるだろう。

.. literalinclude:: /_sample/ptt/lists-members.py
   :language: python3

POST lists/members/create
----------------------------------------------------------------------
自分の所有するリストに指定ユーザーを一人分登録する API だ。
今では上述の lists/members/create_all で完全に置き換えてしまって構わなそうだ。

.. literalinclude:: /_sample/ptt/lists-members-create.py
   :language: python3

POST lists/destroy
----------------------------------------------------------------------
自分の所有するリストを一つ指定して、それを削除する API だ。
使用頻度はテスト用に作成したダミーリストをまた削除するときに使うくらいだ。

.. literalinclude:: /_sample/ptt/lists-destroy.py
   :language: python3

POST lists/create
----------------------------------------------------------------------
リストを新しく作成するための API だ。Twitter Web Client で作業するほうが早い。
https://dev.twitter.com/rest/reference/post/lists/create 参照。

.. literalinclude:: /_sample/ptt/lists-create.py
   :language: python3

GET lists/subscriptions
----------------------------------------------------------------------
あるユーザーが購読している（他ユーザーの管理下にある）リストを得るために利用する。

.. literalinclude:: /_sample/ptt/lists-subscriptions.py
   :language: python3

GET lists/ownerships
----------------------------------------------------------------------
``lists/ownerships`` は特定のユーザーが管理しているリストを列挙するのに利用する。
ツイートというよりは、リストのプロパティーを得るのに利用する。

.. literalinclude:: /_sample/ptt/lists-ownerships.py
   :language: python3

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-twitter.txt
