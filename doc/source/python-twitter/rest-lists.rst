======================================================================
リスト関連
======================================================================
本節では lists 系 API の応用について記す。
私が Twitter の機能で最も利用するのがリストである。
特にリストへのユーザー登録処理を重視している。

.. contents::

POST lists/create
======================================================================
リストを新しく作成するための API だ。Twitter Web Client で作業するほうが早い。

.. literalinclude:: /_sample/ptt/lists-create.py
   :language: python3

POST lists/destroy
======================================================================
自分の所有するリストを一つ指定して、それを削除する API だ。
使用頻度はテスト用に作成したダミーリストをまた削除するときに使うくらいだ。

.. literalinclude:: /_sample/ptt/lists-destroy.py
   :language: python3

GET lists/list
======================================================================
GET lists/list は指定ユーザーの所有する全てのリストと購読しているリストを取得する機能だ。

次にサンプルコードを示す。

.. literalinclude:: /_sample/ptt/lists-list.py
   :language: python3

* [1] メソッド ``lists.list`` に ``user_id`` または ``screen_name`` キーワード引数を与えて、
  そのユーザーの持っているリストを全部取得する。
  ユーザーが作成したリストに加え、もしあれば、購読している他ユーザーが作成したリストを含む。

* [2] 各リストの ``mode``, ``full_name``, ``description`` 各属性をコンソールに出力する。

実行例を示す。自分のものについては隠しリストも得られる。

.. code:: console

   $ ./lists-list.py
   public @mj_sega_ad/【mj5】twitter連動
   public @OReillyMedia/everything-o-reilly
   public @fenrir_official/fenrir-inc フェンリルの公式アカウントなど。
   public @nikkei/日経グループ 日経グループ内の公式アカウントのリストです。\n#WelcomeToTwitter
   public @showa_yojyo/followed-by People who follow(ed) me for a fixed period. For some reason some followers are not included.
   private @showa_yojyo/...
   public @showa_yojyo/videogame Accounts related to videogame productions, amusement facilities, etc.
   public @showa_yojyo/informative Accounts of people or organizations that supplyeveryone helpful information and knowledge.
   public @showa_yojyo/tools Accounts that inform of software, hardware, events, bug-fixes, release schedules, etc.
   public @showa_yojyo/bot A list of amusing bot accounts.

GET lists/statuses
======================================================================
GET lists/statuses はリストを指定して、そのタイムラインを閲覧する機能だ。

次にサンプルコードを示す。

.. literalinclude:: /_sample/ptt/lists-statuses.py
   :language: python3

* [1] メソッド ``lists.statuses`` に与える引数を準備する。
  リストを特定する手段は一つではないのだが、
  分かりやすさを優先して ``slug`` および ``owner_screen_name`` を同時に指示する。

  ここでは ``screen_name`` が ``showa_yojyo`` のユーザーの、
  ``informative`` という公開リストがあるという前提で、
  そのタイムラインを見るという例だ。

* [2] 文字列をコンソールに出力する。
  ツイート内容、改行、ツイート時刻、ツイートに利用したアプリ名が確認できる。

GET lists/show
======================================================================
GET lists/show は指定のリストの詳細を知るための API だ。
次の例は私の所有するリスト ``bot`` の全属性を標準出力に出力する。

.. literalinclude:: /_sample/ptt/lists-show.py
   :language: python3

コンソールからの実行例を示す。ユーザー自身の情報は一部カットした。

.. code:: console

   $ lists-show.py
   {'created_at': 'Sun Feb 12 13:21:16 +0000 2012',
    'description': 'A list of amusing bot accounts.',
    'following': True,
    'full_name': '@showa_yojyo/bot',
    'id': 65280663,
    'id_str': '65280663',
    'member_count': 4873,
    'mode': 'public',
    'name': 'bot',
    'slug': 'bot',
    'subscriber_count': 4,
    'uri': '/showa_yojyo/lists/bot',
    'user': {'contributors_enabled': False,
             'created_at': 'Wed Jan 11 12:01:03 +0000 2012',
             'default_profile': False,
             'default_profile_image': False,
             'description': '実は電子の世界の人で現実には存在しない。',
             ...
             'verified': False}}

POST lists/update
======================================================================
POST lists/update は自分の所有するリストの属性を変更するための API だ。
あまり利用しないのでコード省略。

POST lists/members/create
======================================================================
POST lists/members/create は自分の所有するリストに指定ユーザーを一人分登録する機能だ。
今では POST lists/members/create_all で完全に置き換えてしまって構わなそうだ。

一応サンプルコードを示す。

.. literalinclude:: /_sample/ptt/lists-members-create.py
   :language: python3

POST lists/members/create_all
======================================================================
POST lists/members/create_all はブラウザー上の操作ではできないと思われる、
一括でユーザーを複数指定して指定のリストに登録する処理を実現する機能だ。

次のサンプルコードの ``screen_names`` はスクリーンネームの tuple インスタンスを意味する。
この API はリストを多用する筆者が利用する頻度がもっとも高い。

.. literalinclude:: /_sample/ptt/lists-members-create_all.py
   :language: python3

.. hint::

   上のサンプルコードはあくまで簡易版だ。
   ウン千というアカウントをリストに登録する状況が私の場合はあるので、
   CSV 文字列を組む手順に工夫が要る。

   手許のスクリプトを見たら、大体こういうことをしている。

   * ユーザー ID をテキストファイルから入力する
   * リクエストをプログラムでループにする
   * 15 アカウントずつリクエストする
   * リクエスト間に何秒間かのウェイトを入れる

POST lists/members/destroy
======================================================================
POST lists/members/destroy はリストから指定したユーザーを削除する機能だ。
しかし、これを利用するくらいならばブラウザーで Twitter を利用するほうが早いやもしれない。
複数ユーザーを処理するための POST lists/members/destroy_all も参照。

一応サンプルコードを示す。

.. literalinclude:: /_sample/ptt/lists-members-destroy.py
   :language: python3

POST lists/members/destroy_all
======================================================================
POST lists/members/destroy_all は自分の所有するリストから複数のユーザーを一度に削除する機能だ。
コードとしては POST lists/members/create_all と同じ構造になる。

.. literalinclude:: /_sample/ptt/lists-members-destroy_all.py
   :language: python3

GET lists/members
======================================================================
GET lists/members は指定リストに登録されているユーザーをすべて得ることができる機能だ。
登録ユーザー数が多いリストに対しては、次のように
「カーソル処理」で複数回のリクエストをすることになるだろう。

.. literalinclude:: /_sample/ptt/lists-members.py
   :language: python3

.. hint::

   GET lists/ownerships と GET lists/subscriptions を合わせたようなデータが得られる。

GET lists/members/show
======================================================================
GET lists/members/show は指定ユーザーが指定リストに登録されているかを調べる機能だ。
使い途が少々思いつかない。

.. literalinclude:: /_sample/ptt/lists-members-show.py
   :language: python3

GET lists/memberships
======================================================================
GET lists/memberships は、
あるユーザーが他のユーザーが管理しているリストに含まれているとき、
そのようなリストを列挙するのに利用する機能だ。

.. literalinclude:: /_sample/ptt/lists-memberships.py
   :language: python3

* [1] ユーザー ``showa_yojyo`` を含むリストをリクエストする。
  ``cursor`` については別項で詳しく解説する。

* [2] 各リストの名前と説明文をコンソールに出力する。
  ``full_name`` の先頭にはリストの作者の ``screen_name`` が見えると思う。

POST lists/subscribers/create
======================================================================
POST lists/subscribers/create は他人のリストを購読する機能だ。
利用しないこともないが、説明を省略する。

POST lists/subscribers/destroy
======================================================================
POST lists/subscribers/destroy は他人のリストの購読をやめる機能だ。
利用しないので説明略。

GET lists/subscribers
======================================================================
GET lists/subscribers は指定リストの購読者をリストする機能だ。
どうも非公開ユーザーが購読していてもリストされないらしい。

.. literalinclude:: /_sample/ptt/lists-subscribers.py
   :language: python3

余談だが、ユーザー属性の description は改行文字が含まれる場合がある。
CSV 形式で出力する場合は注意したい。

POST lists/subscribers/show
======================================================================
POST lists/subscribers/show は任意のユーザーが任意のリストを購読しているかどうかを知る機能だ。
使いどころが思い浮かばないので、説明を省く。

GET lists/subscriptions
======================================================================
GET lists/subscriptions はあるユーザーが購読している（他ユーザーの管理下にある）リストを得るために利用する機能だ。

.. literalinclude:: /_sample/ptt/lists-subscriptions.py
   :language: python3

GET lists/ownerships
======================================================================
GET lists/ownerships は特定のユーザーが管理しているリストを列挙するのに利用する機能だ。

.. literalinclude:: /_sample/ptt/lists-ownerships.py
   :language: python3

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-twitter.txt
