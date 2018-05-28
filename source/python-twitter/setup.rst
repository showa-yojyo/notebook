======================================================================
インストール
======================================================================
自分の Python_ 環境に `Python Twitter Tools`_ をインストールする方法を記す。

.. contents:: ノート目次

前準備
======================================================================
PTT のインストールだけではモノが動かない。Twitter 側の設定作業も必要だ。

インストール
----------------------------------------------------------------------
PTT のインストールはいつものように pip で構わない。

.. code:: console

   $ pip install twitter

本パッケージ配布版には単体テストコードのようなものはない。
インストールが無事に終わったことを知りたいのならば、
``import twitter`` の確認で我慢する。

.. code:: console

   $ python -c 'import twitter; help(twitter)'
   Help on package twitter:

   NAME
       twitter - The minimalist yet fully featured Twitter API and Python toolset.

   DESCRIPTION
       The Twitter and TwitterStream classes are the key to building your own
       Twitter-enabled applications.
   以下略

ドキュメント
----------------------------------------------------------------------
PTT のドキュメントよりも重要なのは Twitter API 自身のドキュメントであるので、
Documentation_ 等のウェブページを見ながら Python コードを書くことになる。

認証トークン入手
----------------------------------------------------------------------
* Twitter API は OAuth という認証を利用している。
  このため、API key および API secret と呼ばれる文字列が必要となる。
  API v1.0 では一部 GET 系は認証なしで利用できる API もあったが、
  v1.1 からはすべての API で要認証となった。

  * これらの文字列を入手するには、
    https://dev.twitter.com/apps 以降のページ群であらかじめ手続きを済ませる。

    * ウェブブラウザーと Twitter アカウントを持っていることが必要である。
    * Create an application というページに入力フォームがある。
      入力後、画面下部のボタンを押せば多分出てくるだろう。

* 次に Access token および Access token secret という、別の一対の文字列が必要だ。

  * これらの文字列を得るために、先ほどの文字列が必要となる。

  * Google で ``get_access_token`` 等検索してヒットする、
    ネットに落ちているスクリプトを一部改変して実行する。
    コードを見れば手を入れる箇所は理解できるハズ。

* 上記 4 つの文字列を入手できて初めて Twitter API v1.1 が利用可能となる。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-twitter.txt
