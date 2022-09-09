======================================================================
クラス ``docutils.nodes.NodeVisitor``
======================================================================
本節ではクラス ``NodeVisitor`` の実装を調べていく。
設計としては当然 GoF デザインパターンの Visitor パターンであり、
作用する対象はクラス名が示すように ``Node`` オブジェクトだ。

.. contents:: ノート目次

クラス図
======================================================================
まずは抽象クラス ``NodeVisitor`` および ``Node`` を主に見るべく、
簡単なクラス図を示す。

.. mermaid:: ./docutils-visitor.mmd
   :align: center
   :alt: (class diagram)

抽象クラス ``NodeVisitor`` および ``Node`` をメインに見たいので、
特に継承グラフの末端ノード付近のクラスは大胆に省略した。
特にクラス ``Node`` については、大量のサブクラスが存在することに注意が要る。
下に ``NodeVisitor`` のサブクラスをテキストで列挙しておく。

.. code:: text

   NodeVisitor
       writers.html4css1.HTMLTranslator
       writers.latex2e.LaTeXTranslator
       writers.manpage.Translator
       GenericNodeVisitor
           writers.docutils_xml.XMLTranslator
           writers.html4css1.SimpleListChecker
           writers.odf_odt.ODFTranslator
           TreeCopyVisitor
               transforms.parts.ContentsFilter
       SparseNodeVisitor
           transforms.peps.PEPZeroSpecial
           transforms.references.DanglingReferencesVisitor

メソッド ``Node.walk``
======================================================================
メソッド ``Node.walk`` の簡略版コードを次に示す。
ログ出力と、こちらは重要なので載せたいところだが、例外処理コードを省いている。

.. code:: python3

   def walk(self, visitor):
       stop = False
       visitor.dispatch_visit(self)
       for child in self.children[:]:
           if child.walk(visitor):
               stop = True
               break
       return stop

* 問題は冒頭の ``visitor.dispatch_visit(self)`` が何を行うかだが、
  これは後述する。

* 例外処理についてまとめるとこうなる。

  * メソッド ``walk`` のスコープほぼ全域において、
    例外 ``StopTraversal`` が送出された場合、
    これを捕捉して ``stop = True`` を戻り値として当メソッドの呼び出し元に戻る。

  * 呼び出し ``visitor.dispatch_visit`` が例外 ``SkipChildren`` または ``SkipNode`` を送出した場合も、
    同様に当メソッドが終了し、後続の子ノードの ``walk`` は呼び出されない。

* どこかの子ノードの ``walk`` が ``True`` を返すと基点ノードの ``walk`` としても処理終了。

メソッド ``Node.walkabout``
======================================================================
メソッド ``Node.walkabout`` の簡略版コードを次に示す。

.. code:: python3

   def walkabout(self, visitor):
       call_depart = True
       stop = False
       visitor.dispatch_visit(self)
       for child in self.children[:]:
           if child.walkabout(visitor):
               stop = True
               break

       if call_depart:
           visitor.dispatch_departure(self)
       return stop

* 問題は冒頭の ``visitor.dispatch_visit(self)`` および末端の
  ``visitor.dispatch_departure(self)`` が何を行うかだが、
  これは後述する。

* 例外処理についてまとめるとこうなる。

  * 例外 ``SkipNode`` 送出時は ``False`` を戻り値として終了。
  * 例外 ``StopTraversal`` 送出時は ``True`` を戻り値とする。
  * 例外 ``SkipDeparture`` 送出時は末端の ``dispatch_departure`` 呼び出しを省略する。
  * 例外 ``SkipChildren`` 送出時は子ノードに対する ``walkabout`` 呼び出しを省略して末端の処理に進む。
  * 例外 ``SkipSiblings`` 送出時はおそらく各子ノードに対する ``walkabout`` 呼び出しのループの途中のはずで、
    このループを途中で抜ける。

* どこかの子ノードの ``walkabout`` が ``True`` を返すと基点ノードの ``walkabout`` としても処理終了。

メソッド ``NodeVisitor.dispatch_visit``
======================================================================
このメソッドはメソッド ``Node.walk`` がその木構造データの各オブジェクトについて呼び出す。

メソッド ``NodeVisitor.dispatch_visit`` の処理は本質的には引数ノードに対して、
メソッド ``visit_XXXX`` を呼び出し、その戻り値を本メソッドの戻り値として終了するというものだ。

ログ出力等、本質的でない処理を取り除いた簡易コードを示す。

.. code:: python3

   def dispatch_visit(self, node):
       node_name = node.__class__.__name__
       method = getattr(self, 'visit_' + node_name, self.unknown_visit)
       return method(node)

* 変数 ``node_name`` は実行時のオブジェクト ``node`` のクラス名を表す文字列となる。
  例えばオブジェクトが ``Text`` 型ならば文字列 ``'Text'`` となる。

* 変数 ``method`` には Visitor オブジェクトのメソッドが何か入る。
  上の例の続きで、もしこの Visitor にメソッド ``visit_Text`` が存在していれば
  それを取るが、存在しない場合は ``unknown_visit`` を取るように働く。

  * ``visit_XXXX`` タイプのメソッドは ``NodeVisitor`` のサブクラスが個別に定義できる。
    スーパークラスの側ではサブクラス側について何も知る必要がないのに、
    個別メソッドを呼び出せるというのがミソ。

  * ノード型に対応する ``visit_XXXX`` がサブクラスに存在しない場合、
    既定のメソッドとして ``unknown_visit`` を呼び出すという工夫も素晴らしい。
    その上既定の実装が例外 ``NotImplementedError`` を送出するだけというのも気が利いている。

メソッド ``NodeVisitor.dispatch_departure``
======================================================================
このメソッドはメソッド ``Node.walkabout`` がその木構造データの各オブジェクトについて呼び出す。

メソッド ``NodeVisitor.dispatch_departure`` の仕組みも前述の ``dispatch_visit`` と同様。
違いは ``visit_`` または ``_visit`` を ``depart_`` または ``_departure`` にそれぞれ置き換えるだけだ。

クラス ``GenericNodeVisitor``
======================================================================
クラス ``GenericNodeVisitor`` はノードツリーの全ノードを処理の対象にしたいような
Visitor のスーパークラスとして利用する。
具体的に言うと、任意のノードクラス ``NODETYPE`` に対してメソッド ``visit_NODETYPE`` が定義されている。
その実装は ``self.default_visit`` というものを呼び出すものというものになっている。
サブクラスの Visitor 側で適切にメソッド ``visit_NODETYPE`` を定義しなければ、
例外 ``NotImplementedError`` が送出される。
これはメソッド ``default_departure`` についても同様だ。

ノードクラスは 98 個あり、モジュール ``nodes`` 内にリスト ``node_class_names`` として定義されている。
なので、メソッドの宣言も 98 個分書くかといえばそうなってはいない。
Python 組み込み関数の ``setattr`` を用いてテキスト処理感覚で「実装」している。

クラス ``SparseNodeVisitor``
======================================================================
クラス ``SparseNodeVisitor`` はノードツリーの一部のノードだけを処理の対象にしたいような
Visitor のスーパークラスとして利用する。
具体的に言うと、任意のノードクラス ``NODETYPE`` に対してメソッド ``visit_NODETYPE``
および ``depart_NODETYPE`` をオーバーライドし「何もしないで何も返さない」ものとする。

サブクラスの例
======================================================================
クラス ``HTMLTranslator`` を見るとこういうコードがある。
これの直接スーパークラスは ``NodeVisitor`` だ。

.. code:: python3

   # From class docutils.writers.html4css1.HTMLTranslator

   def visit_block_quote(self, node):
        self.body.append(self.starttag(node, 'blockquote'))

   def depart_block_quote(self, node):
        self.body.append('</blockquote>\n')

どのように呼び出されるかというと、このようなものだ。

.. code:: python3

   # From class docutils.writers.html4css1.Writer:

   def translate(self):
        self.visitor = visitor = self.translator_class(self.document)
        self.document.walkabout(visitor)
        for attr in self.visitor_attributes:
            setattr(self, attr, getattr(visitor, attr))
        self.output = self.apply_template()

感想
======================================================================
* ここで見てきた Visitor パターンの実装は Python の特徴を上手に利用している感がある。
  組み込み関数 ``getattr`` で目的のメソッドを動的に検出するところがポイント。

* Docutils には ``run`` もあるが ``walk`` もある。

.. include:: /_include/python-refs-core.txt
