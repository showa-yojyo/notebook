======================================================================
サブパッケージ ``docutils.writers``
======================================================================
本節では Docutils_ のサブパッケージ ``docutils.writers`` を見ていく。
構文木オブジェクトの走査、文字列化、および出力処理をカプセル化した諸クラスを提供する。

.. contents:: ノート目次

クラス図
======================================================================
クラス ``docutils.readers.Writer`` を中心とした簡易クラス図を以下に示す。
これまでに述べたクラスについてはグレーアウトしたり、記載そのものを省いたりしている。

.. mermaid:: ./docutils-writers.mmd
   :align: center
   :alt: (class diagram)

* スーパークラスの ``Writer`` にはさらにその上にスーパークラスとして ``Component`` がある。
  :doc:`./base` を参照。
* クラス ``module`` については :doc:`./languages` を参照。
* クラス ``Output`` については :doc:`./io` を参照。
* 図中で ``(ConcreteWriter)`` となっているクラスとしては、
  次のものが該当する。

  * ``docutils_xml.Writer``
  * ``html4css1.Writer``

    * ``pep_html.Writer``
    * ``s5_html.Writer``

  * ``latex2e.Writer``

    * ``xexex.Writer``

  * ``manpage.Writer``
  * ``odf_odt.Writer``
  * ``pseudoxml.Writer``

クラス ``Writer``
======================================================================
クラス ``Writer`` は構文木オブジェクトを走査して、文字列化し、
それを出力先に書き出すための全てのクラスの共通のスーパークラスだ。

クライアントがこのクラスのオブジェクトを生成するのに必要な物は、
クラス ``document`` および ``Output`` のオブジェクトとなる。

データ
----------------------------------------------------------------------
次の二つはクラスデータだ。

``component_type``
  スーパークラスの同名属性の上書き。
  値は文字列 ``'writer'`` で固定。

``config_section``
  スーパークラスの同名属性の上書き。
  値は文字列 ``'writers'`` で固定。

以下はオブジェクトのメンバーデータだ。

``self.document``
  構文木オブジェクト。

``self.output``
  出力する文字列。
  メモリにあるものとしては最終生成物。

``self.language``
  言語モジュールオブジェクト。

``self.destination``
  データ書き出し先を表現する ``docutils.io.Output`` 型オブジェクト。

``self.parts``
  文書の部品名から出力文字列の「かけら」を照合するための辞書オブジェクト。

  * HTML および LaTeX 書き出しで利用するメンバーデータ
  * キー ``'whole'`` により出力文書文字列丸ごとを得られる。

メソッド
----------------------------------------------------------------------
かなり単純な構成になっている。

``__init__(self)``
  オブジェクトを初期化する。ほとんど何もしない。

``get_transforms(self)``
  スーパークラス ``Component`` からの上書き。
  さらに三種類の変換処理を増やしてある。

``write(self, document, destination)``
  構文木と出力先を指定して、実際に書き出しを行う。

  * クライアントに対する主なインターフェイスとなるメソッド。
  * 設計意図としてはこのメソッドは上書きされない。
    手続きを次の手順で固定したいから。
    その代わりに最終変換処理（と書き出し処理）をサブクラスで上書きする方針だろう。

    #. 文書オブジェクトをセット ``self.document``
    #. 表示用言語モジュールをセット ``self.language`` - :doc:`./languages` 参照。
    #. 出力オブジェクトをセット ``self.destination``
    #. 最終変換処理 ``self.translate``
    #. 書き出し処理 ``self.destination.write`` - :doc:`./io` 参照。

``translate(self)``
  構文木オブジェクトから文字列を構築する。

  * このクラスでは実装されていない。
    当然のように ``NotImplementedError`` を送出する。

  * サブクラスの個性はこのメソッドの上書き内容で決まる。
    文字列 ``self.output`` を確定するように実装する。

``assemble_parts(self)``
  辞書オブジェクト ``self.parts`` を組み立てる。

  * このクラス自身はこのメソッドを呼び出さない。
  * サブクラスでは ``Writer`` のこれを呼び出してから、
    固有の項目操作をする。

サブクラス
======================================================================
最大の見所はサブクラスのメソッド ``translate`` の実装がどのようになっているかということだ。
ほとんどすべてのサブクラスで、次のようなメンバーデータが定義されている。

``self.visitor``
  クラス ``NodeVisitor`` のサブクラスのオブジェクト。
  :doc:`./visitor` 参照。

  ``self.document.walk(self.visitor)`` または
  ``self.document.walkabout(self.visitor)`` の形で構文木を走査する。
  この結果、Visitor オブジェクトに出力するべき情報が溜まるので、
  それを文字列化して ``self.output`` に代入するという処理の流れが多い。

``self.translator_class``
  これはサブクラスにさらなるサブクラスがある場合に現れるメンバーデータ。
  メソッド ``translate`` のコードが同一だが、Visitor のオブジェクトが異なるときに、
  その型だけをクラス間で区別して指定できるようにメンバーデータとして括り出している。

  .. code:: python3

     class SuperWriter(Writer):

         def __init__(self):
             self.translator_class = SuperTranslator
             ...

         def translate(self):
            visitor = self.translator_class(self.document)
            self.document.walkabout(visitor)
            ...

      class SubWriter(SuperTranslator):

         def __init__(self):
             self.translator_class = SubTranslator
             ...

オブジェクト生成
======================================================================
クライアントは所望のモジュールから読み取りクラスそのものではなく、
関数 ``docutils.writers.get_writer_class`` を import する。
この関数に名前を渡すと、クラスが返ってくるので、
呼び出し元がそこからコンストラクターを呼び出す。

* Docutils としては既定の 7 種類の型だけサポートしている。
* 関数 ``get_writer_class`` のコードを読む限り、
  ユーザーが自作の Writer を登録するようなことは基本的にないと思われる。

クライアント
======================================================================
モジュール ``docutils.core`` でオブジェクトの生成処理が確認できる。

.. code:: python3

   def set_writer(self, writer_name):
        """Set `self.writer` by name."""
        writer_class = writers.get_writer_class(writer_name)
        self.writer = writer_class()

感想
======================================================================
* Writer と Visitor は事実上ペア。

.. include:: /_include/python-refs-core.txt
