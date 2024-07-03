======================================================================
論理代数
======================================================================

本稿では SymPy_ が論理代数演算を実現するために用意しているモジュール
``sympy.logic`` 配下を見ていく。 Python が組み込みで持っている論理演算を表現しな
おした一連のクラス群などがある。

.. contents:: ノート目次

ブール論理クラス図
======================================================================

モジュール ``sympy.logic.boolalg`` に定義されているクラスの継承関係だけを図示す
るとこうなる。

.. mermaid::
   :align: center

   classDiagram
       Boolean <|-- BooleanAtom
           BooleanAtom <|-- BooleanTrue
           BooleanAtom <|-- BooleanFalse
       Boolean <|-- BooleanFunction
           BooleanFunction <|-- And
           BooleanFunction <|-- Or
           BooleanFunction <|-- Not
           BooleanFunction <|-- Xor
           BooleanFunction <|-- Nand
           BooleanFunction <|-- Nor
           BooleanFunction <|-- Implies
           BooleanFunction <|-- Equivalent
           BooleanFunction <|-- ITE

* クラス ``Boolean`` のスーパークラスはクラス ``Basic`` である。このクラスが論理
  演算子 ``&``, ``|``, ``~``, etc. をオーバーロードしているので、オブジェクト
  ``A``, ``B`` がある要件を満たしていれば、例えば :code:`A & B` のような記法で論
  理式オブジェクトを生成できる。
* クラス ``BooleanTrue`` と ``BooleanFalse`` は ``Singleton`` のサブクラスでもあ
  る。いつものようにオブジェクト ``S`` を用いて、それぞれのオブジェクトにアクセ
  スできる。

.. csv-table::
   :delim: |
   :header-rows: 1
   :widths: auto

   クラス | 値
   ``BooleanTrue`` | :code:`S.true`
   ``BooleanFalse`` | :code:`S.false`

* ブール関数オブジェクトはクラス ``Boolean`` のサブクラスオブジェクトを木構造コ
  ンポジットで表現することになる。

ブール関数クラス
----------------------------------------------------------------------
クラス BooleanFunction のサブクラスを表にまとめておく。
いきなり直感的な操作ができると思う。

.. csv-table::
   :delim: @
   :header-rows: 1
   :widths: auto

   クラス @ 演算子 @ 演算の意味
   And@``&``@論理積、かつ、conjunction
   Or@``|``@論理和、または、[inclusive] disjunction
   Not@``~``@否定、でない、negation
   Xor@``^``@排他的論理和、exclusive disjunction
   Nand@n/a@:code:`Not(And(...))`
   Nor@n/a@:code:`Not(Or(...))`
   Implies@:code:`>>`@ならば
   Equivalent@n/a@等値、equality?
   ITE@n/a@三項演算子のようなもの、conditioned disjunction

論理演算の基本は ``&``, ``|``, ``~`` である。それぞれに対応するクラスが存在し、
名前は ``And``, ``Or``, ``Not`` である。SymPy ではシンボルや論理式オブジェクトを
これらの組み合わせで組み立てることで表現する。

* メソッド ``as_set`` で具体的な集合オブジェクトを生成する。例えば :code:`And(-2
  < x, x < 2).as_set()` は :code:`Interval(-2, 2)` を生成する。

  * ここで :code:`-2 < x` 等はまた別の型だが、今は気にしない。

* 論理式オブジェクトでもメソッド ``subs`` を利用できる。オブジェクトを構成するシ
  ンボルに Python 組み込みのブーリアン値を代入するような使い方をする。

  * :code:`S.true` と :code:`S.false` でも通じるはず。

関数
======================================================================

クラスのメソッドでないブール代数用関数を見ていく。

関数 ``SOPform``, ``POSform``
----------------------------------------------------------------------

これらの関数は真理値表からブール関数オブジェクトを生成する。生成するブール関数オ
ブジェクトは「最も単純化された表現」になっている。

SymPy では Sum of Products form と Product of Sums form を扱っている。

関数 :code:`SOPform(variables, minterms, dontcares=None)`
  戻り値は ``Or`` オブジェクトである。
関数 :code:`POSform(variables, minterms, dontcares=None)`
  戻り値は ``And`` オブジェクトである。

まずはテストコードを真似て動きを試してみる。

.. code:: ipython

   In [1]: SOPform('xyz', [[0, 0, 1], [0, 1, 1], [1, 0, 0], [1, 1, 0]])
   Out[1]: Or(And(x, Not(z)), And(z, Not(x)))

   In [2]: POSform('xyz', [[0, 0, 1], [0, 1, 1], [1, 0, 0], [1, 1, 0]])
   Out[2]: And(Or(x, z), Or(Not(x), Not(z)))

真理値表 ``minterms`` はこのように入れ子の ``list`` で表現する。例えば
:code:`[0, 0, 1]` の意図は「命題 :code:`~x & ~y & z` が真である」だ。

次に `Wikipedia の例
<https://en.wikipedia.org/wiki/Quine%E2%80%93McCluskey_algorithm>`_ を再現してみ
よう。ここでは引数 ``dontcare`` も指定する。

.. code:: ipython

   In [1]: %paste
   minterms = [[0, 1, 0, 0],
               [1, 0, 0, 0],
               [1, 0, 0, 1],
               [1, 0, 1, 0],
               [1, 1, 0, 0],
               [1, 1, 1, 1],]

   dontcare = [[1, 0, 1, 1],
               [1, 1, 1, 0],]

   ## -- End pasted text --
   In [2]: SOPform('ABCD', minterms, dontcare)
   Out[2]: Or(And(A, C), And(A, Not(B)), And(B, Not(C), Not(D)))

   In [3]: POSform('ABCD', minterms, dontcare)
   Out[3]: And(Or(A, B), Or(A, Not(C)), Or(C, Not(B), Not(D)))

当該記事の真理値表からこれらの関数の実引数を構成する方法を記す。

* まず、当該記事の真理値表から ``f`` が 0 の行はカットする。
* さらに ``f`` が Don't care な行は ``minterms`` では含めない。むしろ
  ``dontcare`` の入れ子要素にする。

``Out[2]`` が当該記事の最終結果と一致している。そして ``Out[2]`` と ``Out[3]``
は等値だ。どうすればこのことが確認できるのか、わからないようなら考えて理解するこ
と。

論理式を正規化する関数
----------------------------------------------------------------------

忘れそうなので用語と関連する概念をまとめておく。

* 連言標準形 POS, CNF, Conjunctive Normal Form, ``AND(...)``
* 選言標準形 SOP, DNF, Disjunctive Normal Form, ``OR(...)``

関数 :code:`to_cnf(expr, simplify=False)`, :code:`is_cnf(expr)`
  論理式オブジェクト ``expr`` から、等値性を保ったまま「複数の論理和オブジェクト
  をオペランドとする一つの論理積オブジェクト」を生成する。

  .. code:: ipython

     In [1]: is_cnf(A & (B | (C & D)))
     Out[1]: False

     In [2]: to_cnf(A & (B | (C & D)))
     Out[2]: And(A, Or(B, C), Or(B, D))

関数 :code:`to_dnf(expr, simplify=False)`, :code:`is_dnf(expr)`
  論理式オブジェクト ``expr`` から、等値性を保ったまま「複数の論理積オブジェクト
  をオペランドとする一つの論理和オブジェクト」を生成する。

  .. code:: ipython

     In [1]: is_dnf(A & (B | (C & D)))
     Out[1]: False

     In [2]: to_dnf(A & (B | (C & D)))
     Out[2]: Or(And(A, B), And(A, C, D))

関数 :code:`to_nnf(expr, simplify=False)`, :code:`is_nnf(expr)`
  論理式オブジェクト ``expr`` から、等価性を保ったまま次の条件を満たす論理式オブ
  ジェクトを生成する。

  * ``Not`` がかかるのが最も内側の論理式（おそらくシンボルだろう）だけである
  * それを除けば、式を構成する演算子は ``And`` と ``Or`` だけである。

  .. code:: ipython

     In [1]: is_nnf(A >> B)
     Out[1]: False

     In [2]: to_nnf(A >> B)
     Out[2]: Or(B, Not(A))

.. warning::

   上記サンプルではあらかじめ下記のインポートが必要である。

   >>> from sympy.logic.boolalg import (is_nnf, is_cnf, is_dnf)

単純化
----------------------------------------------------------------------

関数 :code:`simplify_logic(expr, form=None, deep=True)`
  この関数は論理式 ``expr`` を単純化したオブジェクトを生成する。

  * キーワード引数 ``form`` に値を指定するならば、文字列 ``cnf`` または ``dnf``
    を与えること。その値に対応する形式の論理式オブジェクトが得られる。
  * キーワード引数 ``deep`` は単純化の再帰をするかどうかを示すフラグ。

汎用の単純化関数 ``simplify`` も論理式オブジェクトを単純化するのに使える。

充足性テスト
----------------------------------------------------------------------

モジュール ``sympy.logic.inference`` にはブール関数の充足性をテストする関数があ
る。

関数 :code:`satisfiable(expr, algorithm='dpll2', all_models=False)`
  論理式 ``expr`` の充足性をテストする。

  * 論理式 ``expr`` が真になる可能性が全くなければ ``False`` を返す。
  * 論理式 ``expr`` が真になる可能性があれば、そのときのシンボルの組み合わせを一
    つ返す。

    .. code:: ipython

       In [1]: satisfiable((A | B) & (~A | ~B))
       Out[1]: {B: False, A: True}

       In [2]: satisfiable((A & B) & (~A | ~B))
       Out[2]: False

  * キーワード引数 :code:`all_models=True` を指定すると、充足性可能のときのシン
    ボルの組み合わせを全部返そうとする。さらに、この関数はジェネレーター化する。

    .. code:: ipython

       In [1]: list(satisfiable((A | B) & (~A | ~B), all_models=True))
       Out[1]: [{B: False, A: True}, {B: True, A: False}]

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
