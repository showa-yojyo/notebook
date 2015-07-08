======================================================================
論理代数
======================================================================
本稿では SymPy_ が論理代数演算を実現するために用意しているモジュール ``sympy.logic`` 配下を見ていく。
Python が組み込みで持っている論理演算を表現しなおした一連のクラス群などがある。

.. contents:: ノート目次

ブール論理クラス図
======================================================================
モジュール ``sympy.logic.boolalg`` に定義されているクラスの継承関係だけを図示するとこうなる。

.. code-block:: text

   Boolean
       BooleanAtom
           BooleanTrue
           BooleanFalse
       BooleanFunction
           And
           Or
           Not
           Xor
           Nand
           Nor
           Implies
           Equivalent
           ITE

* クラス ``Boolean`` のスーパークラスはクラス ``Basic`` である。
  このクラスが論理演算子 ``&``, ``|``, ``~``, etc. をオーバーロードしているので、
  オブジェクト ``A``, ``B`` がある要件を満たしていれば、
  例えば ``A & B`` のような記法で論理式オブジェクトを生成できる。

* クラス ``BooleanTrue`` と ``BooleanFalse`` は ``Singleton`` のサブクラスでもある。
  いつものようにオブジェクト ``S`` を用いて、それぞれのオブジェクトにアクセスできる。

  ==================== ====================
  クラス               値
  ==================== ====================
  ``BooleanTrue``      ``S.true``
  ``BooleanFalse``     ``S.false``
  ==================== ====================

* ブール関数オブジェクトはクラス ``Boolean`` のサブクラスオブジェクトを木構造コンポジットで表現することになる。

ブール関数クラス
----------------------------------------------------------------------
クラス ``BooleanFunction`` のサブクラスを表にまとめておく。
いきなり直感的な操作ができると思う。

==================== ========== ==================================================
クラス               演算子     演算の意味
==================== ========== ==================================================
``And``              ``&``      論理積、かつ、conjunction
``Or``               ``|``      論理和、または、[inclusive] disjunction
``Not``              ``~``      否定、でない、negation
``Xor``              ``^``      排他的論理和、exclusive disjunction
``Nand``             n/a        ``Not(And(...))``
``Nor``              n/a        ``Not(Or(...))``
``Implies``          ``>>``     ならば
``Equivalent``       n/a        等値、equality?
``ITE``              n/a        三項演算子のようなもの、conditioned disjunction
==================== ========== ==================================================

論理演算の基本は ``&``, ``|``, ``~`` である。
それぞれに対応するクラスが存在し、名前は ``And``, ``Or``, ``Not`` である。
SymPy ではシンボルや論理式オブジェクトをこれらの組み合わせで組み立てることで表現する。

* メソッド ``as_set`` で具体的な集合オブジェクトを生成する。
  例えば ``And(-2 < x, x < 2).as_set()`` は ``Interval(-2, 2)`` を生成する。

  * ここで ``-2 < x`` 等はまた別の型だが、今は気にしない。

* 論理式オブジェクトでもメソッド ``subs`` を利用できる。
  オブジェクトを構成するシンボルに Python 組み込みのブーリアン値を代入するような使い方をする。

  * ``S.true`` と ``S.false`` でも通じるはず。

関数
======================================================================
クラスのメソッドでないブール代数用関数を見ていく。

関数 ``SOPform``, ``POSform``
----------------------------------------------------------------------
これらの関数は真理値表からブール関数オブジェクトを生成する。
生成するブール関数オブジェクトは「最も単純化された表現」になっている。

SymPy では Sum of Products form と Product of Sums form を扱っている。

関数 ``SOPform(variables, minterms, dontcares=None)``
  戻り値は ``Or`` オブジェクトである。

関数 ``POSform(variables, minterms, dontcares=None)``
  戻り値は ``And`` オブジェクトである。

まずはテストコードを真似て動きを試してみる。

.. code-block:: text

   In [119]: SOPform('xyz', [[0, 0, 1], [0, 1, 1], [1, 0, 0], [1, 1, 0]])
   Out[119]: Or(And(x, Not(z)), And(z, Not(x)))

   In [122]: POSform('xyz', [[0, 0, 1], [0, 1, 1], [1, 0, 0], [1, 1, 0]])
   Out[122]: And(Or(x, z), Or(Not(x), Not(z)))

真理値表 ``minterms`` はこのように入れ子の ``list`` で表現する。
例えば ``[0, 0, 1]`` の意図は「命題 ``~x & ~y & z`` が真である」だ。

次に `Wikipedia の例 <https://en.wikipedia.org/wiki/Quine%E2%80%93McCluskey_algorithm>`_ を再現してみよう。
ここでは引数 ``dontcare`` も指定する。

.. code-block:: text

   In [126]: %paste
   minterms = [[0, 1, 0, 0],
               [1, 0, 0, 0],
               [1, 0, 0, 1],
               [1, 0, 1, 0],
               [1, 1, 0, 0],
               [1, 1, 1, 1],]

   dontcare = [[1, 0, 1, 1],
               [1, 1, 1, 0],]

   ## -- End pasted text --
   In [127]: SOPform('ABCD', minterms, dontcare)
   Out[127]: Or(And(A, C), And(A, Not(B)), And(B, Not(C), Not(D)))

   In [128]: POSform('ABCD', minterms, dontcare)
   Out[128]: And(Or(A, B), Or(A, Not(C)), Or(C, Not(B), Not(D)))

当該記事の真理値表からこれらの関数の実引数を構成する方法を記す。

* まず、当該記事の真理値表から f が 0 の行はカットする。
* さらに f が Don't care な行は ``minterms`` では含めない。
  むしろ ``dontcare`` の入れ子要素にする。

``Out[127]`` が当該記事の最終結果と一致している。
そして ``Out[127]`` と ``Out[128]`` は等値だ。
どうすればこのことが確認できるのか、わからないようなら考えて理解すること。

論理式を正規化する関数
----------------------------------------------------------------------
忘れそうなので用語と関連する概念をまとめておく。

* 連言標準形 POS, CNF, Conjunctive Normal Form, AND(...)
* 選言標準形 SOP, DNF, Disjunctive Normal Form, OR(...)

関数 ``to_cnf(expr, simplify=False)``, ``is_cnf(expr)``
  論理式オブジェクト ``expr`` から、等値性を保ったまま
  「複数の論理和オブジェクトをオペランドとする一つの論理積オブジェクト」を生成する。

  .. code-block:: text

     In [113]: is_cnf(A & (B | (C & D)))
     Out[113]: False

     In [114]: to_cnf(A & (B | (C & D)))
     Out[114]: And(A, Or(B, C), Or(B, D))

関数 ``to_dnf(expr, simplify=False)``, ``is_dnf(expr)``
  論理式オブジェクト ``expr`` から、等値性を保ったまま
  「複数の論理積オブジェクトをオペランドとする一つの論理和オブジェクト」を生成する。

  .. code-block:: text

     In [109]: is_dnf(A & (B | (C & D)))
     Out[109]: False

     In [110]: to_dnf(A & (B | (C & D)))
     Out[110]: Or(And(A, B), And(A, C, D))

関数 ``to_nnf(expr, simplify=False)``, ``is_nnf(expr)``
  論理式オブジェクト ``expr`` から、
  等価性を保ったまま次の条件を満たす論理式オブジェクトを生成する。

  * ``Not`` がかかるのが最も内側の論理式（おそらくシンボルだろう）だけである
  * それを除けば、式を構成する演算子は ``And`` と ``Or`` だけである。

  .. code-block:: text

     In [115]: is_nnf(A >> B)
     Out[115]: False

     In [116]: to_nnf(A >> B)
     Out[116]: Or(B, Not(A))

単純化
----------------------------------------------------------------------
関数 ``simplify_logic(expr, form=None, deep=True)``
  この関数は論理式 ``expr`` を単純化したオブジェクトを生成する。

  * キーワード引数 ``form`` に値を指定するならば、
    文字列 ``cnf`` または ``dnf`` を与えること。
    その値に対応する形式の論理式オブジェクトが得られる。

  * キーワード引数 ``deep`` は単純化の再帰をするかどうかを示すフラグ。

汎用の単純化関数 ``simplify`` も論理式オブジェクトを単純化するのに使える。

充足性テスト
----------------------------------------------------------------------
モジュール ``sympy.logic.inference`` にはブール関数の充足性をテストする関数がある。

関数 ``satisfiable(expr, algorithm='dpll2', all_models=False)``
  論理式 ``expr`` の充足性をテストする。

  * 論理式 ``expr`` が真になる可能性が全くなければ ``False`` を返す。
  * 論理式 ``expr`` が真になる可能性があれば、
    そのときのシンボルの組み合わせを一つ返す。

    .. code-block:: text

       In [159]: satisfiable((A | B) & (~A | ~B))
       Out[159]: {B: False, A: True}

       In [160]: satisfiable((A & B) & (~A | ~B))
       Out[160]: False

  * キーワード引数 ``all_models=True`` を指定すると、
    充足性可能のときのシンボルの組み合わせを全部返そうとする。
    さらに、この関数はジェネレーター化する。

    .. code-block:: text

       In [161]: list(satisfiable((A | B) & (~A | ~B), all_models=True))
       Out[161]: [{B: False, A: True}, {B: True, A: False}]

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
