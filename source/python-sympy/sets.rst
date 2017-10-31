======================================================================
集合
======================================================================
SymPy_ が提供するクラス Set およびその諸サブクラスについて記す。
Python も組み込みでクラス set を提供しているが、
記号演算と集合演算に特化させる目的で SymPy としてもこれらを持っているのだろう。

.. contents:: ノート目次

.. note::

   本文中のすべての IPython セッション中のサンプルコードで、
   以下のインポートおよび出力書式設定が済んでいるものとする。

   .. code-block:: python3

      init_printing(pretty_print=False)

主要クラス図
======================================================================
サブパッケージ ``sympy.sets`` が提供する集合を表現するクラスたち。
インデントが派生関係を意味する。一行空けは特に意味はない。

.. code-block:: text

   Set
       EmptySet
       UniversalSet

       Union
       Intersection
       Complement
       SymmetricDifference

       ProductSet

       Interval
           Reals
       FiniteSet

       Naturals
           Naturals0
       Integers

       ComplexRegion
           Complexes

       ImageSet
       Range

* クラス Set のスーパークラスはクラス Basic である。
* クラス Set のサブクラスには、もう一つ別のクラスをスーパークラスに持つことがある。
* 一部のサブクラスは :code:`from sympy.sets.fancysets import ...` しないと利用可能にならない。

集合に関する機能（属性、操作）は、期待しているものがクラス Set のインターフェイスとして提供されている。

クラス Set
======================================================================
ここをしっかり抑えれば SymPy の集合を把握できたも同然。

プロパティー
----------------------------------------------------------------------
クラス単位のものとオブジェクト単位のものがある。
後者に興味があるので、ここでまとめておく。

基本的には各プロパティーの意味はその名前から推測できるとおり。

:code:`inf`, :code:`sup`
  それぞれ集合の下限と上限を返す。

:code:`measure`
  集合のルベーグ測度を返す。

:code:`boundary`
  集合の境界を返す。

:code:`is_open`, :code:`is_closed`
  それぞれ集合が開集合であるか、閉集合であるかを返す。

  * 集合 E が開集合 ⇔ E と E の境界の共通部分が空集合。
  * 集合 E が閉集合 ⇔ E の境界が E に含まれる。

:code:`closure`
  集合の閉包を返す。
  すなわち E と E の境界の和集合を返す。

:code:`interior`
  集合の内部（内点すべての集合）を返す。
  E の境界の補集合として表現する。

位相空間論的プロパティーの核となるものは :code:`boundary` である。

演算子による集合演算
----------------------------------------------------------------------
集合オブジェクト同士の各種演算を演算子で表現できる。
ここで :code:`E` と :code:`T` をオブジェクトとする。

* :code:`E + T`, :code:`E | T` は和集合。
* :code:`E & T` は共通集合。
* :code:`E * T` は直積集合。
* :code:`E ** n` は :code:`E * E * ... * E` の形をとる直積集合。
* :code:`E - T` は :code:`E` に対する :code:`T` の補集合。

メソッド
----------------------------------------------------------------------
ここで :code:`E` と :code:`T` をそれぞれ自身およびメソッド引数となる集合オブジェクトとする。

:code:`union`
  :code:`Union(E, T)` を返す。

:code:`intersect`, :code:`intersection`
  :code:`Intersection(E, T)` を返す。

:code:`complement`
  :code:`Complement(T, E)` を返す。
  これは引数が全体を示す方のオブジェクトなので間違えぬようにする。

:code:`symmetric_difference`
  :code:`SymmetricDifference(E, T)` を返す。

:code:`powerset`
  :code:`E` のべき集合オブジェクトを返す。

:code:`isdisjoint`, :code:`is_disjoint`
  :code:`E` と :code:`T` の共通集合が空であるかを返す。

:code:`issubset`, :code:`is_subset`
  :code:`E` が :code:`T` の部分集合であるかを返す。

:code:`issuperset`, :code:`is_superset`
  :code:`issubset` を逆方向に試す。

:code:`is_proper_subset`
  :code:`E` が :code:`T` の部分集合であり、かつ :code:`E != T` であるかを返す。

:code:`is_proper_superset`
  :code:`is_proper_subset` を逆方向に試す。

:code:`contains`
  これは引数が集合ではなく、何かの値 :code:`x` である。
  つまり :code:`x` が :code:`E` の元であるかを返す。

  :code:`x in E` とも書ける。

サブクラス
======================================================================
クラス Set のサブクラスのうち、面白そうなものを見ていく。

クラス EmptySet
----------------------------------------------------------------------
クラス EmptySet は空集合を表現する。
空集合を表現するためにクラスを定義することで、色々とメリットがあるようだ。

* コンストラクターでオブジェクトを生成することも、
  シングルトン管理オブジェクトから :code:`S.EmptySet` として参照することもできる。
  クラス EmptySet がシングルトンゆえ、両者は同一のオブジェクトだ。

* 関数 :code:`len` を EmptySet オブジェクトに適用すると常に ``0`` を返す。
* ルベーグ測度が常に ``0`` である。
* メソッド :code:`contains` は常に SymPy の :code:`S.false` を返す。
* メソッド :code:`intersection` は常に空集合オブジェクトを返す。
* メソッド :code:`union`, :code:`complement`, :code:`symmetric_difference` は常に引数の集合オブジェクト自身を返す。

クラス UniversalSet
----------------------------------------------------------------------
クラス UniversalSet は全体集合を表現する。
クラス UniversalSet の着想は EmptySet と同じだろう。

* クラス EmptySet 同様、シングルトンである。
  シングルトン管理オブジェクトから :code:`S.UniversalSet` として参照できる。

* 関数 :code:`len` は利用不可。
* ルベーグ測度が常に :code:`S.Inifinity` である。
* メソッド :code:`boundary` は常に :code:`S.EmptySet` を返す。
* メソッド :code:`contains` は常に SymPy の :code:`S.true` を返す。
* その他の集合演算系メソッドはそれぞれ、与えられた引数に対する想像通りの値を返す。

集合演算クラス
----------------------------------------------------------------------
集合演算の結果を表現する一連のクラスを、C++ の標準ライブラリー関数との連想で覚えておく。

.. csv-table::
   :delim: @
   :header: サブクラス, C++ <algorithm>
   :widths: 16, 16

   Union@:code:`std::set_union`
   Complement@:code:`std::set_difference`
   Intersection@:code:`std::set_intersection`
   SymmetricDifference@:code:`std::set_symmetric_difference`

* コンストラクターについて

  * 引数にとる集合オブジェクトの個数は、次のとおり。

    * Union と Intersection は任意の個数。
    * Complement と SymmetricDifference はちょうど 2 個だけ。

  * サポートするキーワード引数は :code:`evaluate` だけとなる。

    * キーワード引数 :code:`evaluate` は Python のブーリアン値をとる。
      これが True のときには要素を簡略化する。
      つまり静的メソッド :code:`reduce` が呼ばれる。

* 静的メソッド :code:`reduce`

  * Union と Intersection のそれの実装を見ると何をしているのか理解できる。
  * 実装に Python の組み込み型 set を利用している。

* イテレーターについて

  * Range の Union に対するイテレーターが動かない？

クラス ProductSet
----------------------------------------------------------------------
クラス ProductSet は集合の直積（デカルト積）を表現する。

* コンストラクターで各集合を指示して直積集合オブジェクトを生成する。
* 集合演算は ProductSet オブジェクト同士でなければならない。
* プロパティー :code:`sets` にて、直積の各集合にアクセスできる。
* オブジェクトが iterable である場合とそうでない場合がある。

  * プロパティー :code:`is_iterable` で判定できる。
  * アクセス順は Python 標準の関数 :code:`product` を各集合に適用したものと同じらしい。

クラス Interval
----------------------------------------------------------------------
クラス Interval は実数区間を表現する。開区間、閉区間、半開区間もサポート。

* コンストラクター

  * 呼び出し形式は :code:`Interval(start, end, left_open=False, right_open=False)` である。
    キーワード引数の意味は、その名前が示す通り。

  * :code:`start < end` となるように引数を指示しないと、
    空集合オブジェクトになってしまう。

  * :code:`start == end` となるように指示すると、
    一点からなる FiniteSet オブジェクトが生成してしまう。

  * 端点として :code:`S.Infinity` 等も指定できる。

  * メソッド :code:`Lopen`, :code:`Ropen` 等により、
    指定端点を開区間にしたオブジェクトを複製できる。

* メソッド :code:`evalf` が利用可能。

クラス FiniteSet
----------------------------------------------------------------------
クラス FiniteSet は有限集合、すなわち元が有限個の集合を表現する。

* コンストラクターには元を列挙しておけばよい。
* オブジェクトは iterable である。
  集合の元は内部的にはソートされた状態なので、その順序に従って値が yield される。
* メソッド :code:`boundary` は自分自身を返す。
* メソッド :code:`measure` は ``0`` を返す。
* メソッド :code:`evalf` が利用可能。

その他のサブクラス
======================================================================
頻出する集合はサブクラスとしてモジュール ``sympy.sets.fancysets`` に定義されている。

クラス Naturals, Naturals0, Integers
----------------------------------------------------------------------
名前が示す通りの整数を元とする集合を表現するクラス。
それぞれのシングルトンオブジェクトが存在しており、
例えば :code:`S.Natural` などとしてアクセスできる。

クラス Reals
----------------------------------------------------------------------
:code:`Interval(-S.Infinity, S.Infinity)` と同じ。
シングルトンオブジェクト :code:`S.Reals` としてアクセス可能。

クラス ComplexRegion, Complexes
----------------------------------------------------------------------
クラス ComplexRegion は複素平面の領域を表現するクラス。

* 例えば Interval の直積で生成すると、複素平面上の矩形領域を表現できる。
* 極座標のような与え方もできる。
  そのときはキーワード引数 :code:`polar=True` を用いる。

一方、クラス Complexes は複素平面全体を表現するクラス。
ユーザーはいつでもシングルトンオブジェクト :code:`S.Complexes` にアクセスできる。

クラス ImageSet
----------------------------------------------------------------------
ある集合とある写像に対する像を表現するクラス。
オブジェクトの生成は :code:`ImageSet(f, E)` のようにすればよい。

* あるいは関数 :code:`imageset` を用いて :code:`imageset(x, expr, E)` のようにする。
* または :code:`imageset(lambda x: f(x), E)` のような。
* 他にもある。

クラス Range
----------------------------------------------------------------------
Python 組み込みの :code:`range` とよく似ている集合。

演習
======================================================================
単体テストのコードを読んでおく。

* 条件を満たせば記号オブジェクトを Interval の端点に指定することができる。

  * あとでメソッド :code:`subs` を利用して値を代入することもできる。

* 単一の集合オブジェクトだけを引数として Union, ProductSet 等の オブジェクトを生成できる。
  ただし、結果は元の集合と同じものになる。
* FiniteSet の元は数に限らない。

* :code:`R2 = S.Reals * S.Reals` または :code:`R2 = S.Reals ** 2` とすれば :math:`\RR^2` を表現できる。

  * :code:`(0, 0) in R2` のようなコードが書ける。

* :code:`Interval(0, 1, True, True) ** 2` に対するメソッド :code:`boundary` の戻り値がおもしろい。

* 座標平面上の原点を中心とする円の定義法の例。テストコード改。

  .. code-block:: ipython

     In [1]: r, th = symbols('r theta', real=True)

     In [2]: L = Lambda((r, th), (r * cos(th), r * sin(th)))

     In [3]: D = ImageSet(L, Interval(0, 1) * Interval(0, 2 * pi, False, True)); D
     Out[3]: ImageSet(Lambda((r, theta), (r*cos(theta), r*sin(theta))), [0, 1] x [0, 2*pi))

     In [4]: D.issubset(S.Reals * S.Reals)
     Out[4]: False

  * [2] 写像 :math:`f: \RR^2 \longto \RR^2` を
    :math:`f: (r, \theta) \longmapsto (r \cos \theta, r \sin \theta)` で定義する。
  * [3] :math:`[0, 1] \times [0, 2 \pi)` の f による像を計算する。
    それらしいオブジェクトが得られる。
  * [4] これはおかしい。:math:`D \subset \RR^2` のつもりなのだが。

.. include:: /_include/python-refs-sci.txt
