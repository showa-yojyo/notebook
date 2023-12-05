======================================================================
OrientDB 利用ノート
======================================================================

:Since: 2010
:Official site: `Home | OrientDB Community Edition <https://www.orientdb.org/>`__
:CLI: OrientDB console 3.2.24

インストール手順は、ホームページのリンク先から圧縮ファイルをダウンロードして解凍
し、中にあるスクリプト :file:`bin/server.sh` を実行するというものだ。もう一つ、
Homebrew を用いる方法もあるようだ。

以下、ローカルホストで閉じた環境で実施する。

3.2. Create a DB の記述にしたがって URL をブラウザーで閲覧すると OrientDB Studio
画面が開く。

* ボタン :guilabel:`CREATE TABLE` を押す前に :guilabel:`Create Admin user` を ON
  にする必要がある。
* 他にも、インターネットからデータベースをインポート可能。

SQL 文 ``SELECT * FROM OUser`` を実行して成功すれば OK とする。画面上部の各種メ
ニュー項目も見ておく。

* 3.3. Create the Java Application 以降は私の Java 技術が欠落しているので実施しな
  い。
* 4.4. Run the Studio 以降をブラウザーで試す。コマンドの一部が微妙に失敗するが、
  その場合は当該クラスにレコードがあることを確認する。それでも失敗する場合はあ
  る。
* OrientDB Studio の :guilabel:`Schema Manager` の検索結果はカルーセルがあるのを
  見落とすな。
* 4.7.3 Queries をすべて試す。ブラウザーでは :guilabel:`BROWSE` と
  :guilabel:`GRAPH` タブを往復することになる。
* :guilabel:`Graph Editor` で問い合わせを実行してグラフを描画し終わったら、ゴミ
  箱ボタン :guilabel:`Clear Canvas` を押してクリアしておくこと。:guilabel:`MORE`
  も色々と試せ。
* ここでようやく 4.11. Tutorials を試す。ここまでを読み飛ばして最初に手を付けて
  はいけない。

  * 4.11.3. Setup a Distributed Database 辺りからやることが明らかでなくなる。
  * 4.11.9.1. Importing the Open Beer Database into OrientDB の元データのアドレ
    スが微妙に異なる。:file:`https://openbeerdb.com/files/openbeerdb_csv.zip` が
    良い。

    * 作成する JSON ファイル各種のパスを動作環境に合わせろ。

* 6.2. Basic Concepts をしっかりと読め。
* 8.1.3. Install as Service on Unix を読め。
* 9.1. Studio
* 10.1. Introduction

  * OrientDB の SQL には ``JOIN`` がない。

.. todo::

   * Neo4j を済ませたら 4.11.9.2 に戻る。
   * アンインストール手順を記す。
