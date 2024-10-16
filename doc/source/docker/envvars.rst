======================================================================
環境変数集
======================================================================

今のところ重要な環境変数が見つからない。

.. include:: ./docker-inc.txt

.. contents:: 本章見出し
   :depth: 3
   :local:

.. envvar:: DOCKER_CONFIG

   :doc:`./config` 参照。要点はそこに全部記したつもりだ。

.. envvar:: DOCKER_CONTEXT

   Docker デーモンが使用するコンテキストの名前。環境変数 :envvar:`DOCKER_HOST`
   およびコマンド ``docker context use`` で設定した既定コンテキストを上書きす
   る。コンテキストが何かわからぬ場合は ``docker build`` や ``docker compose``
   の文書を読むといい。

   コマンド :samp:`docker context use {context-name}` をいちいち呼び出すのが面倒
   だったり、不可能であったりする場合に代わりにこの環境変数を定義することでコン
   テキストを指定するという使い方をするのだろう。

   Docker クライアントの共通オプションである ``-c``, ``--context`` の環境変数
   バージョンと解釈してかまわない。学習時には使わない。

.. envvar:: DOCKER_HIDE_LEGACY_COMMANDS

   これを設定すると、Docker ヘルプの出力は「レガシー」なトップレベルコマンドを省
   き、オブジェクト型ごとの管理コマンドしか示さなくなる。

   これは設定しておきたい。値は空でなければ何でもいいだろう。シェルのスタート
   アップファイルのどこかに設定して ``export`` しておく。

.. envvar:: DOCKER_HOST

   Docker クライアントの共通オプションである ``-H``, ``--host`` と同等。コマンド
   呼び出し時にこのオプションをいちいち指定しなくて済むという利点がある。学習時
   には使わない。
