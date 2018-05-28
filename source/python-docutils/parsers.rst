======================================================================
サブパッケージ ``docutils.parsers``
======================================================================
Docutils_ の構文解析サブパッケージ ``docutils.parsers`` について記す。
構成はクラス ``Parser`` およびそのサブクラスの定義と、
サブサブパッケージ ``docutils.parsers.rst`` の二本立てになっている。
本節では少なくても前者はしっかりと読み込んでいきたい。
余力があれば後者も ``RSTStateMachine`` という面白い教材があるので解読したい。

.. contents:: ノート目次

クラス図
======================================================================
クラス ``Parser`` 周辺のクラス図を以下に示す。
ただし、説明済みのクラスは省略したり灰色に塗りつぶしたりしてある。

* クラス ``Parser`` の直接スーパークラスは ``Component`` だが省略してある。
  Docutils の基本クラスについては :doc:`./base` 参照。
* 状態機械系の抽象クラス群については :doc:`statemachine` 参照。

.. figure:: /_images/docutils-parsers.png
   :align: center
   :alt: (class diagram)
   :scale: 100%

クラス ``Parser``
======================================================================
クラス ``Parser`` は構文解析を実行するためにあるわけだが、ろくなものが実装されていない。

データ
----------------------------------------------------------------------
クラスデータは右辺値としてアクセスする。

``component_type = 'parser'``
  スーパークラス ``Component`` からの上書き。

``config_section = 'parsers'``
  スーパークラス ``SettingsSpec`` からの上書き。

メンバーデータは二つだけある。
ただしこれらのデータは ``setup_parse`` を呼び出さないとアクセスできない。

``inputstring``
  文字列データ。
  基本的には入力テキストデータそのもので、
  テキスト解析の直前にこれを加工して状態機械の入力とする。

``document``
  クラス ``document`` のオブジェクト。初期状態でセットする。
  :doc:`./nodes` も参照。

メソッド
----------------------------------------------------------------------
メソッドは次の三つしかないのだが、全てクライアント側が直接呼び出すことになるようだ。

``parse(self, inputstring, document)``
  文字列を受け取って ``document`` オブジェクトを肉付けしていくためのメソッドだろうが、
  これは完全にオーバーライド専用になっている。
  デフォルトでは ``NotImplementedError`` を送出するだけだ。

``setup_parse(self, inputstring, document)``
  オブジェクトのメンバーデータをセットするだけのメソッド。
  これはサブクラスで上書きしないでよい。

``finish_parse(self)``
  テキストの構文解析を終了したときに呼び出すメソッド。
  これはサブクラスで上書きしないでよい。

* ``setup_parse`` と ``finish_parse`` はサブクラスの ``parse`` から呼び出すか、
  ``Parser`` オブジェクトのクライアントが ``parse`` 呼び出しの前後に呼び出す。

サブクラス
======================================================================
モジュール ``null`` とサブパッケージ ``rst`` にそれぞれ定義されている。
とある理由により、クラス名はすべて同じく ``Parser`` だ。

クラス ``docutils.parsers.null.Parser``
----------------------------------------------------------------------
これはいわゆる Null Object パターンのクラスだ。
メソッド ``parse`` を何もしないように上書きしたものになっている。

* ただしクラスデータ ``supported``, ``config_section``, etc. が
  意味のあるデータが上書きされているのが惜しい。

* このクラスのオブジェクトを生成するには、
  クライアントがモジュール ``docutils.parsers.null`` からこのクラスを直接 import して
  コンストラクターを明示的に呼び出す必要がある。

クラス ``docutils.parsers.rst.Parser``
----------------------------------------------------------------------
これは reStructuredText データを構文解析するクラスだ。
しかし処理を ``RSTStateMachine`` と ``RSTState`` 系に委譲している。
次にメソッド ``parse`` のコードを一部改変引用する。

.. code:: python3

   from docutils.statemachine import string2lines
   from .states import RSTStateMachine

   def parse(self, inputstring, document):
       """Parse `inputstring` and populate `document`, a document tree."""
       self.setup_parse(inputstring, document)
       self.statemachine = RSTStateMachine(...)
       inputlines = string2lines(inputstring, ...)
       self.statemachine.run(inputlines, document, ...)
       self.finish_parse()

利用例
======================================================================
クラス ``Parser`` の何らかのサブクラスのオブジェクトを利用する擬似コードを次に示す。

.. code:: python3

   from docutils.utils import new_document
   from docutils.parsers import get_parser_class

   source_path = '/path/to/source-file'
   settings = ... or None

   with open(source_path, 'r') as source:
       input_string = source.read()

   parser = get_parser_class('parser_name')()
   parser.parse(input_string, new_document(source_path, settings))

   doc = parser.document
   ...

* オブジェクト ``settings`` については現在未調査。
* 基本的にはテキストファイルから全文を読み込んでおく。
* ここでは関数 ``get_parser_class`` を利用して ``Parser`` のサブクラスを実行時に得ている。
  それからコンストラクターを直接呼び出す方法でオブジェクト ``parser`` を生成する。
* 空の ``document`` オブジェクトを関数 ``new_document`` で生成する。
  これを ``parser`` に渡す。

これらの処理は Docutils の設計では ``Reader`` 系が行う想定になっているようだ。

感想
======================================================================
* ``Parser`` のメソッドの設計がやや気に入らない。
  ``setup_parse`` と ``finish_parse`` の呼び出しはスーパークラスの
  ``parse`` に組み込んでおいて、
  中間部分を上書きさせる Template Method パターンがよかった。

* 関数 ``get_parser_class`` で採用している技法は、モジュール
  :doc:`languages` でも見られる。

* Docutils としては構文解析クラスは例えば ``RSTParser`` のようなものだけで十分事足りるはずだが、
  敢えて抽象クラスと具象クラスの二段構えに設計しておくことで、
  別の構文のテキストデータのための構文解析ライブラリーを新しく構築する機会を与えるのだ。
  これは ``RSTStateMachine`` と ``RSTState`` についても当てはまる。

* ``RSTStateMachine`` および ``RSTState`` をどこで議論しようか。

.. include:: /_include/python-refs-core.txt
