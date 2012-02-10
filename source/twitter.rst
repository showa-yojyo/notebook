======================================================================
Twitter 利用ノート
======================================================================
棲み家にインターネット回線が引っ張れた記念に Twitter_ について調査。

.. contents:: ノート目次

ユーザー登録
======================================================================
メールアドレスが必要なだけだった。

1. ブラウザーで Twitter_ にアクセスする。
2. 「Twitter に登録する」というボタンを含むフォームがあるので、
   そこを適宜入力し、ボタンを押す。
3. 後は手なりで。

Getting Started ノート
======================================================================
まずは `Getting Started`_ から見ていく。

Twitter for Websites
----------------------------------------------------------------------
個人的にはあまり興味のない機能。

* <Easily embed Twitter functionality,
  encourage your users to share content on Twitter,
  and increase your audience reach with Twitter for Websites> (Documentation_) だそうだ。

* HTML コード片を自分の管理するウェブサイト内の HTML ファイルに記述することで、
  自分の客に見て欲しい Twitter ページへのリンクを貼ることができるようだ。
  コード片は Twitter の提供するページ `Twitter ボタン`_ で生成することができる。

  * そのページで適当に入力すれば、HTML コード片が生成されるので、
    自分で編集できる HTML ファイルに貼りつければよい。
  * ``script`` タグの ``src`` 値の URL 形式にクセがあり、
    ローカルディスクにある HTML ファイルを閲覧してもボタンが描画されないだろう。

Search API
----------------------------------------------------------------------
ここは興味があるので、基本事項にプラスアルファを乗せたいところだ。
`Using the Twitter Search API`_ をまずは一読する。

* Search Operators の節は必読。

* 基本的な検索性能は期待しているよりも高くない。
  最近の tweet しか対象としない等の機能的制限が相当ある。

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

REST API
----------------------------------------------------------------------
`REST API Resources`_ を眺めていると、なんとなく応用方法が見えてくるか。

* <If you're building application that leverages core Twitter objects,
  then this is the API for you> (Documentation_) だそうなので、
  これはプログラマー向けのトピックと考えられる。
  しかし、ウェブブラウザー一丁でも動作確認をすることはできるのだ。

  * 例えば ``GET statuses/user_timeline`` の仕様をじっくり読むと、
    ある Twitter ユーザーの最近の 20 tweets を購読するのに利用できる、
    RSS リーダーのための URL の構成方法が理解できる。

Streaming API
----------------------------------------------------------------------
TBW



Widgets
======================================================================
ブログ等でよく見かける
Twitter_ のミニ表示領域みたいなものは、HTML コード片で実現する。

コード片は同社サイト内にある Widgets_ ページで生成することができる。
Twitter API のストレートな応用例と言える。

* まずは「ウィジェットを選んでください」「自分のサイト」をクリック。
  次のものをローカルの HTML ファイルにペーストして試してみるとよい。
  ああなるほどと思うはずだ。

  * プロフィールウィジェット
  * 検索ウィジェット

* ``script`` 要素のうち ``src`` 属性付きのほうは、
  ``head`` ブロックの内側に移したい。

.. _Twitter: http://twitter.com/
.. _Documentation: https://dev.twitter.com/docs
.. _Getting Started: https://dev.twitter.com/start
.. _Twitter ボタン: https://twitter.com/about/resources/buttons?tw_p=twt#follow
.. _Using the Twitter Search API: https://dev.twitter.com/docs/using-search
.. _GET search: https://dev.twitter.com/docs/api/1/get/search
.. _REST API Resources: https://dev.twitter.com/docs/api
.. _Widgets: http://twitter.com/about/resources/widgets
