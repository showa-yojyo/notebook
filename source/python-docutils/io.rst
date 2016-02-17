======================================================================
モジュール ``docutils.io``
======================================================================
Docutils_ の入出力インターフェイスを扱うモジュール ``docutils.io`` を見ていく。
ここは難しいところはないはずだ。

例によってエラー処理やら低水準処理のラッパーやらは省略する。

.. contents:: ノート目次

クラス図
======================================================================
モジュール ``docutils.io`` の全クラスを一枚の図に収めて示したいが、
紙幅とレイアウトの都合上、二つのスーパークラスそれぞれに分割して図示する。
また、両図ともに本節の解説の主眼にない機能の記載はグレーアウトしたり、
記載そのものを省略している。

まずはクラス ``Input`` の継承グラフを表現するクラス図だ。次に示す。

.. figure:: /_static/docutils-input.png
   :align: center
   :alt: (class diagram)
   :scale: 100%

次の図はクラス ``Output`` の継承グラフを表現するクラス図だ。

.. figure:: /_static/docutils-output.png
   :align: center
   :alt: (class diagram)
   :scale: 100%

* スーパークラスについては :doc:`./base` を参照。
* それぞれ対称的なインターフェイスを備えていることが明白。
  機能も対称的だ。

クラス ``Input``
======================================================================
補助的な機能は無視して、興味のあるインターフェイスのみ記す。

データ
----------------------------------------------------------------------
``component_type``
  一応文字列 ``input`` が定義されているが、
  このクラスは ``Component`` を継承しているわけではない。

``default_source_path``
  サブクラスでの上書き専用。
  入力の対象がファイルでないときに、何らかのダミー文字列を入れておく。

``self.encoding``
  入力データのエンコーディング名。普通は ``"utf-8"`` でよいだろう。

``self.source``
  入力そのもの。

``self.source_path``
  入力の対象がファイルであるときの、ファイルパス文字列。

メソッド
----------------------------------------------------------------------
``read(self)``
  サブクラスで定義。

  * ``NullInput`` ならば空の文字列を返す。
  * ``FileInput`` ならばファイルを ``open`` して ``read`` して ``decode`` して返す。
  * ``StringInput`` ならば ``self.source`` を ``decode`` して返す。
  * ``DocTreeInput`` ならば ``self.source`` を単に返す。

``decode(self, data)``
  引数のデータを文字列に復号する。

  * ``self.encoding`` が与えられている場合は、それを利用する。
    ない場合は発見的方法で頑張る。

サブクラス
----------------------------------------------------------------------
サブクラスでは必要に応じてメソッドを追加する。
例えば ``FileInput`` ならば ``open``, ``readlines``, ``close`` 等々。
それほど興味を引くものはないので省略。

クラス ``Output``
======================================================================
こちらも補助的な機能は無視する。

データ
----------------------------------------------------------------------
``component_type``
  一応文字列 ``output`` が定義されているが、
  このクラスは ``Component`` を継承しているわけではない。

``default_destination_path``
  サブクラスでの上書き専用。
  出力の対象がファイルでないときに、何らかのダミー文字列を入れておく。

``self.encoding``
  出力データのエンコーディング名。

``self.destination``
  出力先。

``self.destination_path``
  出力の対象がファイルであるときの、ファイルパス文字列。

メソッド
----------------------------------------------------------------------
``write(self, data)``
  サブクラスで定義。

  * ``NullOutput`` ならば何もしない。
  * ``FileOutput``, ``BinaryFileOutput`` ならばファイル
    ``self.destination`` に ``decode`` したデータを ``write`` する。
  * ``StringOutput`` ならば ``self.destination`` を文字列扱いして ``encode`` して返す。

``encode(self, data)``
  データを ``encode`` して、それを返す。

クライアント
======================================================================
何が ``Input`` と ``Output`` のサブクラスのオブジェクトを生成するのか、
それらをどう用いるのかを記す。

* ``FileInput``

  * ``parsers.rst.directives.Include.run``
    ``include_file`` として
    状況に応じて ``readlines()`` または ``read()``

  * ``parsers.rst.directives.Raw.run``
    ``raw_file`` としてオブジェクトを生成、``read()`` する

  * ``parser.rst.directives.CSVTable.get_csv_data``
    ``csv_file`` として生成、``read()`` する

  * and more

* ``StringInput``

  * ``urllib.request.urlopen(source).read()`` の戻り値を利用する状況。

* ``DocTreeInput``

  * ``core.publish_from_doctree`` にて利用。
    ``document`` が既にあることが決定的。

* ``FileOutput``

  * ``Publisher`` のデフォルトの ``destination_class``
  * ``publish_file`` 系関数のデフォルトの ``destination_class``
  * ``utils.DependencyList.set_output`` で利用

* ``StringOutput``

  * ``core.publish_programmatically`` 系関数のデフォルトの ``destination_class``

* ``NullOutput`` も出番がある。
* ``BinaryFileOutput`` は ``publish_cmdline_to_binary`` のデフォルトの ``destination_class``

感想
======================================================================
* ここに記さなかった補助関数 ``check_encoding`` の実装では
  Python 標準のモジュール ``codecs`` を利用している。

* ``Output`` のメソッド ``encode`` では
  結局 ``str`` のメソッド ``encode`` を用いるが、
  ``Input`` のメソッド ``decode`` では ``str`` のコンストラクターを用いる。

.. include:: /_include/python-refs-core.txt
