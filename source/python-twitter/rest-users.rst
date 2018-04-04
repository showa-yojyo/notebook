======================================================================
ユーザーアカウント関連
======================================================================
本節では users 系 API の応用方法について述べる。

.. contents::

GET users/lookup
======================================================================
GET users/lookup は一度に 100 件までの Twitter ユーザー詳細情報を得ることができる。
この API を利用するには、ユーザー ID を必要な分だけあらかじめ知っておく必要がある。

.. hint::

   * ドキュメントにあるように ID を収集するには GET friends/ids や GET followers/ids を併用することになりそうだ。
   * 複数のユーザー ID をカンマで連結して CSV テキストする。
     Python では ``','.join(ids)`` でそれを実現できる。

GET users/show
======================================================================
GET users/show は特定のユーザーの詳細情報を得るのに GET users/show を利用する。
いわば GET users/lookup の単数版だ。

.. literalinclude:: /_sample/ptt/users-show.py
   :language: python3

* [1] 基本的に指定する引数はこれだけで構わない。
* [2] ユーザーの Twitter 情報を出力してみる。

GET users/search
======================================================================
GET users/search はキーワードから何か関係のありそうなユーザーを探すのにたいへん便利だ。
応用例としては、例えば bot に関係しそうなユーザーを可能な限りかき集めて、
ひとつのリストにまとめるといったものが考えられる（私はそれを実践している）。

これはごく単純な呼び出し例なので、キーワード引数
``count`` の上限である 20 ユーザーしか取得できない。
さらに取得するには、この API の呼び出しをループの中に入れて、
キーワード引数 ``page`` をループカウンターで指定するとよいだろう。
その際には関数 ``time.sleep`` 等でリクエストに時間的間隔を設けると申し分ない。

.. literalinclude:: /_sample/ptt/users-search.py
   :language: python3

GET users/profile_banner
======================================================================
GET users/profile_banner では指定ユーザーのプロフィール画像の各種 URL が得られる。
Twitter クライアントを自作する者が利用するのだろう。

.. literalinclude:: /_sample/ptt/users-profile_banner.py
   :language: python3

これを実行するとこのようになる。
実際にブラウザーで下記 ``url`` にアクセスすると、現在のプロフィール画像が描画されるはずだ。
なお、私が新しいものに更新しない限り有効だ。

.. code:: console

   $ ./users-profile_banner.py
   {'1500x500': {'h': 500,
                 'url': 'https://pbs.twimg.com/profile_banners/461058152/1447250161/1500x500',
                 'w': 1500},
    '300x100': {'h': 100,
                'url': 'https://pbs.twimg.com/profile_banners/461058152/1447250161/300x100',
                'w': 300},
    '600x200': {'h': 200,
                'url': 'https://pbs.twimg.com/profile_banners/461058152/1447250161/600x200',
                'w': 600},
    'ipad': {'h': 313,
             'url': 'https://pbs.twimg.com/profile_banners/461058152/1447250161/ipad',
             'w': 626},
    'ipad_retina': {'h': 626,
                    'url': 'https://pbs.twimg.com/profile_banners/461058152/1447250161/ipad_retina',
                    'w': 1252},
    'mobile': {'h': 160,
               'url': 'https://pbs.twimg.com/profile_banners/461058152/1447250161/mobile',
               'w': 320},
    'mobile_retina': {'h': 320,
                      'url': 'https://pbs.twimg.com/profile_banners/461058152/1447250161/mobile_retina',
                      'w': 640},
    'web': {'h': 260,
            'url': 'https://pbs.twimg.com/profile_banners/461058152/1447250161/web',
            'w': 520},
    'web_retina': {'h': 520,
                   'url': 'https://pbs.twimg.com/profile_banners/461058152/1447250161/web_retina',
                   'w': 1040}}

GET users/suggestions
======================================================================
GET users/suggestions は Twitter によるおすすめアカウントのカテゴリーのみを得る機能だ。

サンプルコードを次に示す。

.. literalinclude:: /_sample/ptt/users-suggestions.py
   :language: python3

私の実行例を示す。
誰もフォローしていない割にはかなりのカテゴリーが表示される。
リストには山ほどユーザーを収容していることからこういう構成になっているのだろうかと思う。
お笑い系はどこにもいないのだが？

.. code:: console

   $ ./users-suggestions.py
   Twitter|twitter|13
   野球|野球|11
   サッカー|サッカー|15
   スポーツ|スポーツ|15
   お笑い|お笑い|15
   政府|政府|15
   ニュース|ニュース|14
   ジャーナリスト|ジャーナリスト|15
   旅行 / レジャー|旅行-レジャー|15
   声優 / アニメ|声優-アニメ|15
   ファッション|ファッション|14
   音楽|音楽|15
   ライフライン / 公共交通機関|ライフライン-公共交通機関|13
   美術館・博物館|美術館・博物館|15
   テレビタレント|テレビタレント|15

GET users/suggestions/:slug
======================================================================
GET users/suggestions/:slug は上記のあるカテゴリーのユーザー群を取得する機能だ。
これは PTT でどう呼び出すものか試行錯誤したが、最終的には次のコードで動作を確認した。

.. literalinclude:: /_sample/ptt/users-suggestions-slug.py
   :language: python3

* [1] 例えば「政府」が有効なカテゴリー名の一つなので、これでユーザーを得たい。
  PTT では日本語の実引数を自動的にエンコードしてくれるが、ここでは手動で処理する。
  また、ドキュメントのどこにもない ``_id`` の使い方に注意して欲しい。

次に実行結果を示す。大部分を省略する。

.. code:: console

   $ ./users-suggestions-slug.py
   {
       "name": "政府",
       "size": 15,
       "slug": "政府",
       "users": [
           {
               ...
               "name": "厚生労働省",
               ...
           },
           {
               ...
               "name": "総務省消防庁",
               ...
           },
           ...
           {
              ...
              "name": "消費者庁",
              ...
           }
       ]
   }

GET users/suggestions/:slug/members
======================================================================
GET users/suggestions/:slug/members は上記の GET users/suggestions/:slug の返すデータに加え、
各ユーザーの最近のツイートをも返す。

次にサンプルコードを示す。

.. literalinclude:: /_sample/ptt/users-suggestions-slug-members.py
   :language: python3

次に実行結果を示す。大部分を省略する。

.. code:: console

   $ ./users-suggestions-slug-members.py
   [
       {
          ...
          "status": {
             ...
          },
          ...
          "name": "厚生労働省",
          ...
       },
       ...
   ]

POST users/report_spam
======================================================================
POST users/report_spam は指定のユーザーがスパムであることを Twitter に報告する。
誰彼構わずスパム報告していると、報告者のほうが Twitter のブラックリストに載ると聞いたことがある。

次にサンプルコードを示す。

.. literalinclude:: /_sample/ptt/users-report_spam.py
   :language: python3

* [1] スパムを ``user_id`` または ``screen_name`` のどちらか一方で指定する。
* [2] 送信結果を出力する。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-twitter.txt
