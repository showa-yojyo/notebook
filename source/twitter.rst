======================================================================
Twitter 利用ノート [obsolete]
======================================================================

棲み家にインターネット回線が引っ張れた記念に Twitter_ について調査。

.. warning::

   本稿は Twitter API のバージョンが 1.0 のときに書いたものであり、
   バージョン 1.1 の API が稼働している 2014 年現在、以降の記述は概ね通用しないものとなった。
   したがって本稿は無価値になり果てたが、何かのためにここに残しておく。

.. contents:: ノート目次

関連ノート
======================================================================
* :doc:`python-twitter-tools`

ユーザー登録
======================================================================
メールアドレスが必要なだけだった。

1. ブラウザーで Twitter_ にアクセスする。
2. 「Twitter に登録する」というボタンを含むフォームがあるので、
   そこを適宜入力し、ボタンを押す。
3. 後は手なりで。

後々わかったことだが、アカウントがなくても利用できる機能が多い。
慌ててユーザー登録する必要は実はなかったのかもしれない。

Twitter 専用アプリ
======================================================================
ショボイ PC を使っているせいか、ウェブブラウザーを使うのでは
Twitter_ のページが重くて使えたものではない。

* Windows 100% 誌に紹介されていた Echofon_ というソフトが軽そうなので、
  これを当面利用してみよう。

* 他にも Twitter 専用アプリが存在するようなので、暇を見て調べよう。

.. warning::

   Echofon_ の Windows 版は提供終了済み。

Getting Started ノート
======================================================================

Twitter for Websites
----------------------------------------------------------------------
* HTML コード片を自分の管理するウェブサイト内の HTML ファイルに記述することで、
  自分の客に見て欲しい Twitter ページへのリンクを貼ることができるようだ。
  コード片は Twitter の提供するページ `Twitter ボタン`_ で生成することができる。

  * そのページで適当に入力すれば、HTML コード片が生成されるので、
    自分で編集できる HTML ファイルに貼りつければよい。
  * ``script`` タグの ``src`` 値の URL 形式にクセがあり、
    ローカルディスクにある HTML ファイルを閲覧してもボタンが描画されないだろう。

Search API
----------------------------------------------------------------------
.. warning::

   以下は API v1.0 で通用した方法であり、v1.1 ではダメだ。
   特に ``http://search.twitter.com/search`` が関係する技法は無効。

API を勉強する前に `search-home`_ をまずは試す。

ここは興味があるので、基本事項にプラスアルファを乗せたいところだ。
`Using the Twitter Search API`_ をまずは一読する。

* Search Operators の節は必読。

  * or 検索は文字列 ``OR`` がそのまま演算子になる。
  * ``from:``, ``to:`` 演算子はユーザー名指定。
  * ``since:``, ``until:`` 演算子の引数は ``yyyy-mm-dd`` 形式で指示する。
    未来の日付を指示するとエラーが返ってくる模様。
  * ``:)``, ``:(`` 演算子はいかにも Twitter らしい機能だが、
    個人的にはおよびでない。

* 基本的な検索性能は期待しているよりも高くない。
  最近の tweet しか対象としない等の機能的制限が相当ある。
  ある程度はオプション引数で調整可能。

* 検索結果をブラウザーで見たい (View) のならば
  ``http://search.twitter.com/search?q=XXXXXX`` で十分。

* 検索結果をデータで欲しい (Model) ならば
  ``http://search.twitter.com/search.format?q=XXXXXX`` で得られる。
  ここで URL 中の文字列 ``format`` は、実際には得たいデータ形式を表現する文字列だ。
  例えば JSON 形式で欲しいのならば ``format`` を ``json`` と置き換えてリクエストする。
  `GET search`_ に詳細の説明あり。

  * 面白い利用法として ``format`` を ``atom`` と置き換えて RSS にするというのが知られている。
    この URL を RSS リーダーに登録しておけば、
    Twitter での XXXXXX に対する検索結果、すなわち
    「最近の Twitter での XXXXXX に関する動向」を監視することができる。

よく使う Optional Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``http://search.twitter.com/search?q=XXXXXX`` の ``?`` 以降のどこかに
``parameter=value`` の形で文字列を追加することで、
検索の振る舞いをある程度制御することができる。

個人的に有用なパラメーターをノートしておこう。

``result_type``
  ``mixed`` (default), ``recent``, ``popular`` のいずれかを指定。
  定期チェック RSS 用途に合わせて ``recent`` を指定したい。

``rpp``
  <The number of tweets to return per page> (Documentation_) だから、
  マイナーフレーズ検索用とメジャーフレーズ検索用で値を細かく設定し分けることができる。

``show_user``
  RSS で検索結果 Tweets を見たいときに、ユーザー名を tweet の先頭に
  ``user_name:`` の形で表示させるか否かを指定する。
  デフォルト値は ``false`` なので、明示的にこのパラメーターを指示しないと、
  仮に知り合いの tweet だったとしても RSS ビューワーで見るだけではそうだと判断できない。

  常に ``show_user=true`` を指定しておきたい。

RSS 用に URL を組み立てる例
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: text

   マイナーゲームのファンの傾向を知る
   http://search.twitter.com/search.atom?q=%E3%82%A4%E3%83%AB%E3%83%99%E3%83%AD&show_user=true

   最近の逮捕を知る
   http://search.twitter.com/search.atom?q=%E9%80%AE%E6%8D%95&rpp=30&result_type=recent&show_user=true

``q`` の引数は URL encoded とするのが妥当とのことなので、
エンコード済み文字列を準備しておくべし。
特に日本語テキストを検索するリクエスト文字列のためには絶対必要。

エンコード文字列がわからない場合、Twitter で手で検索してみるしかない。

1. `search-home`_ にブラウザーでアクセス。
2. 検索したい単語（場合によっては演算子を含むような文字列）をテキストボックスにタイプ。
3. 検索ボタンを押す。
4. 画面がジャンプしたら、ブラウザーのアドレスバーの URL の末尾を適宜クリップボードへコピー。

REST API
----------------------------------------------------------------------
.. warning::

   以下は API v1.0 で通用した方法であり、v1.1 ではダメだ。
   特にブラウザー一丁でリクエストうんぬんという記述は完全に無駄。

`REST APIs`_ を眺めていると、なんとなく応用方法が見えてくるか。

* <If you're building application that leverages core Twitter objects,
  then this is the API for you> (Documentation_) だそうなので、
  これはプログラマー向けのトピックと考えられる。
  しかし、ウェブブラウザー一丁でも動作確認をすることはできるのだ。

* ``http://api.twitter.com/1/COMMAND.FORMAT?param=value&...`` の形がリクエスト基本形。
  例えば ``GET statuses/user_timeline`` の仕様をじっくり読むと、
  ある Twitter ユーザーの最近の 20 tweets を購読するのに利用できる、
  RSS リーダーのための URL の構成方法が理解できる。

使えそうなリクエスト
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
まだ初心者ゆえ、次のものくらいしか理解できない（ので、それらしか使えない）。
しばらくは GET メインでやっていく。POST は慣れてから。

* ``statuses/user_timeline`` - ユーザーを特定してタイムライン表示用。
  ``screen_name`` パラメーターを明示的に指示するやりかたで、要人の情報収集に役立つだろう。

* ``users/profile_image/:screen_name`` - プロフィール画像リダイレクト用。

  * ``format`` は事実上 ``png`` 一択。
  * ``size`` パラメーターで画像サイズを指示するのがよい。引数は
    ``bigger``, ``normal``, ``mini``, ``original`` (default) から選択。

* ``users/show`` - あとで試す。

``user_id`` または ``screen_name`` が指示必須引数になっているリクエストがしばしばあるが、
可読性を考慮に入れれば当然 ``screen_name`` の方を採用したい。

Streaming API
----------------------------------------------------------------------
TBW

Widgets
======================================================================
ブログ等でよく見かける Twitter_ のミニ表示領域みたいなものは、HTML コード片で実現する。

コード片は同社サイト内にある Widgets_ ページで生成することができる。
Twitter API のストレートな応用例と言える。

* まずは「ウィジェットを選んでください」「自分のサイト」をクリック。
  次のものをローカルの HTML ファイルにペーストして試してみるとよい。
  ああなるほどと思うはずだ。

  * プロフィールウィジェット
  * 検索ウィジェット

* ``script`` 要素のうち ``src`` 属性付きのほうは、
  ``head`` ブロックの内側に移したい。

.. _Twitter: https://twitter.com/
.. _Documentation: https://dev.twitter.com/overview/documentation
.. _Getting Started: https://dev.twitter.com/start
.. _Twitter ボタン: https://about.twitter.com/resources/buttons#tweet
.. _search-home: http://twitter.com/#!/search-home
.. _Using the Twitter Search API: https://dev.twitter.com/docs/using-search
.. _GET search: https://dev.twitter.com/docs/api/1/get/search
.. _REST APIs: https://dev.twitter.com/rest/public
.. _Widgets: http://twitter.com/about/resources/widgets
.. _Echofon: http://www.echofon.com/
