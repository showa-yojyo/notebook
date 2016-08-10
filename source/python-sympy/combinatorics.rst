======================================================================
組合せ論と群論
======================================================================
モジュール ``sympy.combinatorics`` をいくつかのサブモジュールを省略しつつ大雑把に見ていく。
ここにあるのは群論の有限置換群に関係する機能が中心のようだ。

.. contents:: ノート目次

.. note::

   本文中のすべての IPython セッション中のサンプルコードで、
   以下のインポートおよび出力書式設定が済んでいるものとする。

   .. code-block:: python3

      from sympy.combinatorics import *
      from itertools import islice
      init_printing(pretty_print=False)

巡回置換と置換
======================================================================
モジュール ``sympy.combinatorics.permutations`` に群論オブジェクトのための重要な構成要素がある。
クラス Cycle と Permutation がそれで、
後で見る各種有限群オブジェクトの基礎となるデータ型を表現する。
SymPy_ のドキュメントでは先に Permutation を説明しているが、
私は Cycle を先に理解するのがよいと思うので、
ここではそのようにノートを記す。

クラス Cycle
----------------------------------------------------------------------
巡回置換を表現する。基本的な構成要素なので少々細かく見てきたい。

* 要素は自然数で表現する。0 から始まる。

  * したがって、恒等置換を生成するには :code:`Cycle(0)` とする。位数 1 の巡回が生成する。

* 例を挙げる。:code:`Cycle(0, 3, 7)` は次のような巡回置換を表現する。

  * 0 → 3
  * 3 → 7
  * 7 → 0
  * 1, 2, 4, 5, 6 は固定点。

* IPython 等の Python シェルでオブジェクトをダンプする際には

  * :code:`c.list()` のようにして確認できる。
  * または明示的に Python 組み込み関数 :code:`print` を用いる。

* 巡回置換を合成するにはコンストラクター呼び出し直後にさらに括弧を付けて巡回置換を追加する。
  例を示す。

  .. code-block:: ipython

     In [1]: Cycle(0, 3, 7)(1, 2).list()
     Out[1]: [3, 2, 1, 7, 4, 5, 6, 0]

* このクラスは実は Python の dict をスーパークラスに持つだけなので、
  あまり SymPy のオブジェクトという感じがしない。

* 極端に大きい値を巡回させると MemoryError が送出される。
  例えば :code:`Cycle(1000000, 100)(10000, 1, 100000000)` などとしないほうがよい。

クラス Permutation
----------------------------------------------------------------------
置換を表現する。土台となる概念は上述の巡回置換なので、
要素周りの規則はそれに準じる。

ここではこのクラスの主要な機能を記す。

コンストラクター
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
コンストラクターの記法が複数ある。好きなものを使えるようにしておく。

.. code-block:: ipython

   In [1]: Permutation(2, 1)(0, 5, 6)
   Out[1]: Permutation(0, 5, 6)(1, 2)

   In [2]: Permutation([[2, 1], [0, 5, 6]])
   Out[2]: Permutation(0, 5, 6)(1, 2)

   In [3]: Permutation(2, 1) * Permutation(0, 5, 6)
   Out[3]: Permutation(0, 5, 6)(1, 2)

* 上のコンストラクターのみの場合では、与える巡回置換は互いに素である必要がある。

* キーワード引数 :code:`size` が便利。
  要素数は多いが置換部分が少ない置換を生成するときにはこれだ。

  .. code-block:: ipython

     In [1]: Permutation([[44, 88],], size=100)
     Out[1]: Permutation(99)(44, 88)

* 長さ `n` の恒等置換の生成法をひとつマスターしておく。
  一番楽なのは :code:`Permutation(size=n)` だろう。

置換の合成・積
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
置換の合成の記法も複数あるので注意。
次のものはすべて :code:`i` に対して同じ作用を示す。
いずれもまず :code:`p` を作用する。

* :code:`(p * q)(i)`
* :code:`q(p(i))`
* :code:`i^p^q`
* :code:`i^(p * q)`

オブジェクトの出力
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Permutation オブジェクトを出力する方法がいくつかある。

* :code:`array_form`: e.g. :code:`[5, 2, 1, 3, 4, 6, 0]`
* :code:`cyclic_form`: e.g. :code:`[[0, 5, 6], [1, 2]]`

デフォルトの出力パターンは :code:`Permutation.print_cyclic` フラグで設定する。

置換による像を得る
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
オブジェクトの丸括弧演算子を用いる。

.. code-block:: ipython

   In [1]: p = Permutation(2, 1)(0, 5, 6)

   In [2]: p(0), p(1), p(2)
   Out[2]: (5, 2, 1)

同サイズの文字列・コレクションの像も同様に得られる。

.. code-block:: ipython

   In [1]: p('ABCDEFG')
   Out[1]: ['F', 'C', 'B', 'D', 'E', 'G', 'A']

   In [2]: p(symbols('a0:7'))
   Out[2]: [a5, a2, a1, a3, a4, a6, a0]

置換によって動く要素を求める
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
メソッド :code:`support()` を用いる。

.. code-block:: ipython

   In [1]: Permutation(2, 1)(0, 5, 6).support()
   Out[1]: [0, 1, 2, 5, 6]

   In [2]: Permutation(0, 1, 2, 3).support()
   Out[2]: [0, 1, 2, 3]

   In [3]: Permutation(size=4).support()
   Out[3]: []

置換をランダムに生成する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ランダムな置換の生成にはクラスメソッド :code:`random(n)` を用いる。
次数 `n` の対称群にある置換をランダムに一個返すと言えばよい？

.. code-block:: ipython

   In [1]: Permutation.random(10)
   Out[1]: Permutation(0, 5, 3, 4, 8)(1, 2, 9)(6, 7)

   In [2]: Permutation.random(10)
   Out[2]: Permutation(0, 4, 5, 8)(1, 2, 3, 6)(7, 9)

   In [3]: Permutation.random(10)
   Out[3]: Permutation(0, 7, 6, 8, 1, 9, 3, 2, 5, 4)

* どういう種類のランダムなのか Python だけが知っている。
* ちなみに :code:`random(0)` と :code:`random(1)` の結果は異なる。

置換のべき乗を求める
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
べき乗演算子 :code:`**` を置換オブジェクトに適用することができる。
試しに適当な置換オブジェクトをその位数乗すると、恒等置換が得られることを見よう。

.. code-block:: ipython

   In [1]: p = Permutation(2, 1)(0, 5, 6); p
   Out[1]: Permutation(0, 5, 6)(1, 2)

   In [2]: p.order()
   Out[2]: 6

   In [3]: p ** 6
   Out[3]: Permutation(6)

逆置換を求める
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
逆置換オブジェクトを生成するにはべき乗演算子 :code:`**` を援用する。
指数を -1 にすればよい。

.. code-block:: ipython

   In [1]: p = Permutation(2, 1)(0, 5, 6); p
   Out[1]: Permutation(0, 5, 6)(1, 2)

   In [2]: p ** -1
   Out[2]: Permutation(0, 6, 5)(1, 2)

   In [3]: p * (p**-1)
   Out[3]: Permutation(6)

置換の巡回表記を互換の積へ分解する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
メソッド :code:`transpositions()` を用いることで、置換を互換の積として表現できる。
置換と同等のあみだくじの描き方がわかるということだ。

.. code-block:: ipython

   In [1]: p = Permutation(2, 1)(0, 5, 6); p
   Out[1]: Permutation(0, 5, 6)(1, 2)

   In [2]: p.transpositions()
   Out[2]: [(0, 6), (0, 5), (1, 2)]

と思ったら、両端の線を結ぶことになってしまった。

置換の符号、偶置換、奇置換判定
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
置換の符号を得るにはメソッド :code:`signature()` を、
置換の偶置換、奇置換の判定にはプロパティー :code:`is_even`, :code:`is_odd` をそれぞれ用いる。

先ほどの 3 つの互換の積で表せる :code:`p` を再利用して動作を確認する。

.. code-block:: ipython

   In [1]: p.signature()
   Out[1]: -1

   In [2]: p.is_even
   Out[2]: False

   In [3]: p.is_odd
   Out[3]: True

群オブジェクトジェネレーター
======================================================================
モジュール ``sympy.combinatorics.generators`` にあるジェネレーターおよび関数は、
よく使われる群を参照するのに便利だ。下に示す表はこのモジュールが提供する機能だ。

いずれも対応する群の元を Permutation オブジェクトとして生成する。

.. csv-table::
   :delim: @
   :header: ジェネレーターまたは関数, 機能
   :widths: 16, 32

   :code:`alternating(n)`@`n` 次の交代群を列挙する。
   :code:`cyclic(n)`@`n` 次の巡回群を列挙する。
   :code:`dihedral(n)`@:code:`2 * n` 次の二面体群を列挙する。
   :code:`rubik(n)`@:code:`n * n` 次のルービックキューブ群を生成する。
   :code:`rubik_cube_generators()`@普通のルービックキューブ群を生成する。
   :code:`symmetric(n)`@`n` 次の対称群を列挙する。

ジェネレーターの動きを見よう。

.. code-block:: ipython

   In [1]: for i in symmetric(4): print(i.cyclic_form)
   []
   [[2, 3]]
   [[1, 2]]
   [[1, 2, 3]]
   [[1, 3, 2]]
   [[1, 3]]
   [[0, 1]]
   [[0, 1], [2, 3]]
   [[0, 1, 2]]
   [[0, 1, 2, 3]]
   [[0, 1, 3, 2]]
   [[0, 1, 3]]
   [[0, 2, 1]]
   [[0, 2, 3, 1]]
   [[0, 2]]
   [[0, 2, 3]]
   [[0, 2], [1, 3]]
   [[0, 2, 1, 3]]
   [[0, 3, 2, 1]]
   [[0, 3, 1]]
   [[0, 3, 2]]
   [[0, 3]]
   [[0, 3, 1, 2]]
   [[0, 3], [1, 2]]

   In [2]: for i in dihedral(4): print(i.cyclic_form)
   []
   [[0, 3], [1, 2]]
   [[0, 1, 2, 3]]
   [[1, 3]]
   [[0, 2], [1, 3]]
   [[0, 1], [2, 3]]
   [[0, 3, 2, 1]]
   [[0, 2]]

   In [3]: for i in alternating(4): print(i.cyclic_form)
   []
   [[1, 2, 3]]
   [[1, 3, 2]]
   [[0, 1], [2, 3]]
   [[0, 1, 2]]
   [[0, 1, 3]]
   [[0, 2, 1]]
   [[0, 2, 3]]
   [[0, 2], [1, 3]]
   [[0, 3, 1]]
   [[0, 3, 2]]
   [[0, 3], [1, 2]]

   In [4]: for i in cyclic(4): print(i.cyclic_form)
   []
   [[0, 1, 2, 3]]
   [[0, 2], [1, 3]]
   [[0, 3, 2, 1]]

ルービックキューブについては後述する。

置換群
======================================================================
モジュール ``sympy.combinatorics.perm_groups`` に
置換群を表現するクラス PermutationGroup が宣言されている。

コンストラクター
----------------------------------------------------------------------
置換群を表現するクラス PermutationGroup のコンストラクターには、
その群の生成元を表すいくつかの Permutation オブジェクトを渡す。

手作業で一つ一つオブジェクトを用意するのもよいし、
先述のジェネレーターを利用するのもよいだろう。

プロパティー
----------------------------------------------------------------------
理解している範囲で記す。

:code:`base`
  群の基底。整数点の list オブジェクトである。

  * Schreier-Sims アルゴリズムから得られる。
  * この置換群の恒等置換（単位元）以外のどんな置換を適用しても、
    :code:`base` のすべての整数点を固定することがない。

    例。5 次の対称群 :code:`S5 = SymmetricGroup(5)` を下処理
    （後述の :code:`is_group` の記述を参照）したものに対して試す。

    .. code-block:: ipython

       In [1]: all(
       .....:    (not all(
       .....:        (i == g(i) for i in S5.base)) for g in S5 if not g.is_Identity))
       Out[1]: True

:code:`basic_orbits`
  群の基底と強生成元に関する軌道。

  * Schreier-Sims アルゴリズムから得られる。
  * 上述のプロパティー :code:`base` と後述のメソッド :code:`orbit` とを組み合わせたものと考える。
  * 例。テキトーに作った置換群で動作確認をする。
    :code:`basic_orbits` と :code:`base` がすべての軌道とそれらの代表元をそれぞれ表しているのか。

    .. code-block:: ipython

       In [1]: G = PermutationGroup([Permutation(0, 2, 4)(1, 3), Permutation(5, 6)])

       In [2]: G = PermutationGroup(list(G.generate()))

       In [3]: G.base
       Out[3]: [0, 5, 1]

       In [4]: G.basic_orbits
       Out[4]: [[0, 2, 4], [5, 6], [1, 3]]

       In [5]: for i in range(G.degree):
          ....:     print(G.orbit(i))
          ....:
       {0, 2, 4}
       {1, 3}
       {0, 2, 4}
       {1, 3}
       {0, 2, 4}
       {5, 6}
       {5, 6}

:code:`basic_stabilizers`
  群の基底と強生成元に関する固定群鎖。

  * Schreier-Sims アルゴリズムから得られる。
  * このリストは先頭から大きい順に部分群が並んでいる。

    例。8 次の対称群 :code:`S8 = SymmetricGroup(8)` で試す。

    .. code-block:: ipython

       In [1]: L = S8.basic_stabilizers

       In [2]: S8.base
       Out[2]: [0, 1, 6, 5, 4, 3, 2]

       In [3]: [i.order() for i in L]
       Out[3]: [40320, 5040, 720, 120, 24, 6, 2]

       In [4]: all(i.is_subgroup(j) for i, j in zip(islice(L, 1, None), L))
       Out[4]: True

:code:`basic_transversals`
  群の :code:`basic_orbits` の代表系。

  * 型は dict の list である。
    キーと値は :code:`basic_orbits` の要素とそれに対応する代表元をそれぞれ表す。

    .. code-block:: ipython

       In [1]: G.base
       Out[1]: [0, 5, 1]

       In [2]: G.basic_orbits
       Out[2]: [[0, 2, 4], [5, 6], [1, 3]]

       In [3]: G.basic_transversals
       Out[3]:
       [{0: Permutation(6), 2: Permutation(6)(0, 2, 4)(1, 3), 4: Permutation(6)(0, 4, 2)},
        {5: Permutation(6), 6: Permutation(5, 6)},
        {1: Permutation(6), 3: Permut ation(6)(1, 3)}]

:code:`degree`
  群が含む置換のサイズ。置換が対象とする文字数。

:code:`generators`
  群の生成元を保持する list オブジェクトだ。

:code:`is_abelian`
  群がアーベル群かどうかを返す。

:code:`is_nilpotent`
  群がべき零群かどうかを返す。

  * 実装ではこの群の降中心列の末端の部分群が恒等群かどうかを（入念なやり方で）見ている。
  * べき零群は可解群である。

:code:`is_solvable`
  群が可解群かどうかを返す。

  * 実装が上述の :code:`is_nilpotent` と酷似しているので見ておくとよい。
    降中心列ではなく導来列を調べる。

:code:`is_trivial`
  群が自明な群、恒等群かどうかを返す。

  * そのような群を得たければ何か適当な `n` を用いて
    :code:`PermutationGroup(Permutation(size=n))` とでもしよう。

:code:`strong_gens`
  群の強生成元。

  * Schreier-Sims アルゴリズムから得られる。

メソッド
----------------------------------------------------------------------
理解している範囲で記す。
以下、第一引数の :code:`self` を省略する。

:code:`center()`
  群の中心を返す。

:code:`centralizer(other)`
  この置換群と :code:`other` の中心化群を返す。
  ここで :code:`other` は置換の list または置換群をとる。

  * :code:`G.center() == G.centralizer(G)` が成り立つ。

:code:`commutator(G, H)`
  群の部分群 :code:`G` と :code:`H` の交換子を生成する。
  特に引数として両方とも自身を与えると、交換子群が生成する。

  .. code-block:: ipython

     In [1]: S4 = SymmetricGroup(4)

     In [2]: A4 = AlternatingGroup(4)

     In [3]: G = S4.commutator(S4, S4)

     In [4]: G.is_normal(A4) and A4.is_normal(G)
     Out[4]: True

:code:`contains(g, strict=True)`
  置換 :code:`g` が群に含まれているかどうかを返す。

  * キーワード引数を :code:`strict=False` などとした場合は、
    群と引数の置換のサイズ不整合時に適宜考慮してくれる。

:code:`coset_factor(g, factor_index=False)`
  群の元 :code:`g` を「因数分解」する。

  * 戻り値は置換の list であり、
    末端から先頭に向かって掛けると :code:`g` が得られる。

  * さきほどの :code:`G` で試そう。

    .. code-block:: ipython

       In [5]: G.basic_transversals
       Out[5]:
       [{0: Permutation(6), 2: Permutation(6)(0, 2, 4)(1, 3), 4: Permutation(6)(0, 4, 2)},
        {5: Permutation(6), 6: Permutation(5, 6)},
        {1: Permutation(6), 3: Permut ation(6)(1, 3)}]

       In [6]: perm = Permutation(0, 2, 4)(1, 3)(5, 6)

       In [7]: G.coset_factor(perm)
       Out[7]: [Permutation(6)(0, 2, 4)(1, 3), Permutation(5, 6), Permutation(6)]

       In [8]: G.coset_factor(perm, True)
       Out[8]: [2, 6, 1]

       In [9]: perm == Permutation.rmul(*Out[57])
       Out[9]: True

:code:`coset_rank(g)`
  群の元 :code:`g` のインデックスを得る。
  つまり :code:`G[k] == g` を満たす値 `k` を得る。

  * 当然 :code:`G.contains(g)` なる元にしか意味がない。

:code:`coset_unrank(rank, af=False)`
  群の :code:`rank` 番目の元を得る。

  * 普通は :code:`G[rank]` の記法のほうが楽だ。
  * キーワード引数 :code:`af` は戻り値を list オブジェクトにするか
    Permutation オブジェクトで得るかを指定する。

:code:`derived_series()`
  群の導来列を求める。日本語はこれで適切か知らないが。

  * 戻り値は PermutationGroup オブジェクトの list オブジェクト。
  * 列の先頭と末尾はそれぞれこの群自身と恒等群である。
  * 実装はメソッド :code:`derived_subgroup` を反復的に利用している。

:code:`derived_subgroup()`
  群の導来部分群（交換子部分群）を求める。

:code:`generate(method='coset', af=False)`
  群の要素をすべて列挙する。

  * 名前の通りジェネレーターである。
  * キーワード引数 :code:`af=True` とすると
    Permutation オブジェクトではなく list オブジェクトを列挙する。

:code:`is_group()`
  この群が本当に群かどうかを返す。

  * 後述する名前付き群オブジェクトと正多面体群オブジェクトを用いるときは要注意。
    次のように前処理をしないと True を返してくれない場合がある。

    .. code-block:: ipython

       In [1]: S5 = SymmetricGroup(5)

       In [2]: S5.is_group()
       Out[2]: False

       In [3]: S5 = PermutationGroup(list(S5.generate()))

       In [4]: S5.is_group()
       Out[4]: True

  * そしてこの関数はおそらくかなりのコストがかかる。
  * 本稿では上の例の :code:`S5` の作り直しのような処理を「下処理」と呼ぶことにする。
    群としてみなされるための下処理。

:code:`is_normal(gr)`
  この群が群 :code:`gr` の正規部分群かどうかを返す。

:code:`is_primitive(randomized=True)`
  この群が原始的かどうかを返す。

  .. code-block:: ipython

     In [1]: CyclicGroup(3).is_primitive()
     Out[1]: True

     In [2]: CyclicGroup(4).is_primitive()
     Out[2]: False

:code:`is_subgroup(G, strict=True)`
  この群が群 :code:`G` の部分群であるかどうかを返す。

  * キーワード引数 :code:`strict` については別のメソッドのそれと同じ意味だ。

:code:`is_transitive(strict=True)`
  この群が推移的かどうかを返す。

  * 軌道が一個だけかどうかを調べる。
  * :code:`strict=False` の場合は、
    長さが 1 ではない軌道が一個だけあるのかを調べる。

:code:`lower_central_series()`
  群の降中心列を返す。

  * 戻り値は PermutationGroup オブジェクトの list オブジェクト。
  * もちろん列の先頭がこの群自身だ。
  * 実装はメソッド :code:`commutator` を反復的に利用している。

:code:`orbit(alpha, action='tuples')`
  群の置換の作用による整数点 :code:`alpha` の軌道を求める。

  * 整数点を複数指定することも可能。
    そのときは :code:`action='union'` が便利だ。

:code:`orbits(rep=False)`
  群自身の軌道を全て返す。

  * 戻り値の型は各軌道を set オブジェクトで表した list オブジェクトだ。
  * キーワード引数 :code:`rep` の意味は不明。

:code:`order()`
  群の位数を求める。

  * 全部でいくつの置換を生成できるかということ。

:code:`pointwise_stabilizer(points, incremental=True)`
  整数点 :code:`points` を動かさない、この群の置換の部分群を返す。

:code:`random(af=False)`
  ランダムで群の元を返す。
  キーワード引数は戻り値を list と PermutationGroup のどちらを得るかを指定する。

:code:`stabilizer(alpha)`
  整数点 :code:`alpha` を動かさない、この群の置換の部分群を返す。

その他のメンバー
----------------------------------------------------------------------
演算子や特別な関数をここに記す。
ここでは :code:`G` などを PermutationGroup オブジェクトとする。

:code:`G[i]`
  置換群の `i` 番目の生成元を参照する。
  乗法表を書くときや、「下処理」に用いる。

:code:`len(G)`
  置換群の生成元の個数を返す。

:code:`G == H`
  :code:`G` と :code:`H` それぞれのすべての生成元が同じかどうかを返す。

  * オブジェクトの由来次第では両辺の置換群が同型であっても False を返すことがある。
    これは実装では :code:`.generators` を比較していることによる。

:code:`G * H`
  直積群を置換群として生成する。
  次節の関数 :code:`DirectProduct` も参照。

直積群
======================================================================
モジュール ``sympy.combinatorics.group_constructs`` に群オブジェクトのコレクションから
直積群オブジェクトを生成する関数がある。

関数 :code:`DirectProduct(*groups)`
  複数の PermutationGroup オブジェクトの直積をひとつの PermutationGroup として生成する。

  * 単に :code:`G1 * G2 * ...` としても同じ結果が得られる。
    効率の観点からは当関数を利用するほうが有利だそうだ。

  * この関数の恩恵をもっとも受けるのは、おそらく後述する関数 :code:`AbelianGroup` である。

名前付き群
======================================================================
モジュール ``sympy.combinatorics.named_groups`` にある群オブジェクト生成関数を見ていく。
これらの関数は最終的にひとつの PermutationGroup オブジェクトを生成する。

勝手に「名前付き」と訳したが、「名前のある」「名前を持っている」くらいの意味だろう。

.. csv-table::
   :delim: @
   :header: 関数, 機能
   :widths: 16, 24

   :code:`AbelianGroup(*cyclic_orders)`@巡回群の直積群を生成する。
   :code:`AlternatingGroup(n)`@`n` 次交代群を生成する。
   :code:`CyclicGroup(n)`@`n` 次巡回群を生成する。
   :code:`DihedralGroup(n)`@:code:`2 * n` 次の二面体群を生成する。
   :code:`SymmetricGroup(n)`@`n` 次対称群を生成する。
   :code:`RubikGroup(n)`@:code:`PermutationGroup(rubik(n))` を返す。

AbelianGroup
----------------------------------------------------------------------
名前はアーベル群だが、実体は先ほどの DirectProduct の計算の利用による巡回群の直積群である。
引数で与えたものの和が次数、積が位数になると覚えておくとよい。

.. code-block:: ipython

   In [1]: G = AbelianGroup(2, 2, 3); G
   Out[1]:
       PermutationGroup([
       Permutation(6)(0, 1),
       Permutation(6)(2, 3),
       Permutation(4, 5, 6)])

   In [2]: G.order()
   Out[2]: 12

   In [3]: for i in G.generate(): print(i.cyclic_form)
   []
   [[0, 1]]
   [[2, 3]]
   [[0, 1], [2, 3]]
   [[4, 5, 6]]
   [[0, 1], [4, 5, 6]]
   [[2, 3], [4, 5, 6]]
   [[0, 1], [2, 3], [4, 5, 6]]
   [[4, 6, 5]]
   [[0, 1], [4, 6, 5]]
   [[2, 3], [4, 6, 5]]
   [[0, 1], [2, 3], [4, 6, 5]]

   In [4]: AbelianGroup(2, 5, 4, 210).order() == 2 * 5 * 4 * 210
   Out[4]: True

   In [5]: [i.order() for i in AbelianGroup(3, 3).generate()]
   Out[5]: [1, 3, 3, 3, 3, 3, 3, 3, 3]

AlternatingGroup
----------------------------------------------------------------------
交代群。ここでは群の要素がすべて偶置換であることを見ておく。

.. code-block:: ipython

   In [1]: AlternatingGroup(1) == AlternatingGroup(2)
   Out[1]: True

   In [2]: A4 = AlternatingGroup(4)

   In [3]: all(i.is_even for i in A4.generate())
   Out[3]: True

CyclicGroup
----------------------------------------------------------------------
巡回群。

.. code-block:: ipython

   In [1]: CyclicGroup(0) == CyclicGroup(1)
   Out[1]: True

   In [2]: C8 = CyclicGroup(8)

   In [3]: C8.degree
   Out[3]: 8

   In [4]: C8.order()
   Out[4]: 8

   In [5]: list(C8.generate(af=True))
   Out[5]:
   [[0, 1, 2, 3, 4, 5, 6, 7],
    [1, 2, 3, 4, 5, 6, 7, 0],
    [2, 3, 4, 5, 6, 7, 0, 1],
    [3, 4, 5, 6, 7, 0, 1, 2],
    [4, 5, 6, 7, 0, 1, 2, 3],
    [5, 6, 7, 0, 1, 2, 3, 4],
    [6, 7, 0, 1, 2, 3, 4, 5],
    [7, 0, 1, 2, 3, 4, 5, 6]]

   In [6]: C8.is_abelian
   Out[6]: True

DihedralGroup
----------------------------------------------------------------------
二面体群。引数は次数の半分を指定する。
ここでは位数 2, 4, 6, 8 の二面体群の乗法表をそれぞれ出力する。

.. code-block:: ipython

   In [1]: %paste
   def group_multiplication_table(G):
       L = list(G.generate())
       size = len(L)
       return [[L.index(row * col) for col in L] for row in L]

   for i in range(1, 5):
       Di = DihedralGroup(i)
       print("D{}: degree={} order={} abelian={}".format(i, Di.degree,Di.order(), Di.is_abelian))
       print(TableForm(group_multiplication_table(Di), wipe_zeros=False))
       print()
   ## -- End pasted text --
   D1: degree=2 order=2 abelian=True
   0 1
   1 0

   D2: degree=4 order=4 abelian=True
   0 1 2 3
   1 0 3 2
   2 3 0 1
   3 2 1 0

   D3: degree=3 order=6 abelian=False
   0 1 2 3 4 5
   1 5 4 2 3 0
   2 3 0 1 5 4
   3 4 5 0 1 2
   4 2 1 5 0 3
   5 0 3 4 2 1

   D4: degree=4 order=8 abelian=False
   0 1 2 3 4 5 6 7
   1 2 7 6 3 4 5 0
   2 7 0 5 6 3 4 1
   3 4 5 0 1 2 7 6
   4 5 6 7 0 1 2 3
   5 6 3 2 7 0 1 4
   6 3 4 1 2 7 0 5
   7 0 1 4 5 6 3 2

SymmetricGroup
----------------------------------------------------------------------
対称群。

.. code-block:: ipython

   In [1]: A5, C5, S5 = AlternatingGroup(5), CyclicGroup(5), SymmetricGroup(5)

   In [2]: A5.is_subgroup(S5)
   Out[2]: True

   In [3]: A5.is_normal(S5)
   Out[3]: True

   In [4]: S5.generators
   Out[4]: [Permutation(0, 1, 2, 3, 4), Permutation(4)(0, 1)]

   In [5]: C5.is_subgroup(S5)
   Out[5]: True

   In [6]: C5.is_normal(S5)
   Out[6]: False

RubikGroup
----------------------------------------------------------------------
ルービックキューブ群を生成する。通常は 3x3 なので 3 を指定する。
整数点とキューブ小面との対応関係のイラストを用意しないと読み解けない。

.. code-block:: ipython

   In [1]: R3 = RubikGroup(3)

   In [2]: print(R3)
   PermutationGroup([
       Permutation(53)(6, 44, 47, 18)(7, 41, 46, 21)(8, 38, 45, 24)(9, 15, 17, 11)(10, 12, 16, 14),
       Permutation(53)(3, 43, 50, 19)(4, 40, 49, 22)(5, 37, 48, 25),
       Permutation(2, 11, 47, 33)(5, 14, 50, 30)(8, 17, 53, 27)(18, 24, 26, 20)(19, 21, 25, 23),
       Permutation(53)(1, 10, 46, 34)(4, 13, 49, 31)(7, 16, 52, 28),
       Permutation(15, 42, 33, 24)(16, 43, 34, 25)(17, 44, 35, 26)(45, 51, 53, 47)(46, 48, 52, 50),
       Permutation(53)(12, 39, 30, 21)(13, 40, 31, 22)(14, 41, 32, 23)])

   In [3]: R3.order()
   Out[3]: 43252003274489856000

   In [4]: R3.degree
   Out[4]: 54

そこでこの群の軌道を見る。何か違和感がある。

.. code-block:: ipython

   In [5]: for i in R3.orbits(): print(i, len(i))
   {0} 1
   {1, 3, 5, 7, 10, 12, 14, 16, 19, 21, 23, 25, 28, 30, 32, 34, 37, 39, 41, 43, 46, 48, 50, 52} 24
   {33, 2, 35, 6, 38, 8, 9, 42, 11, 44, 45, 15, 47, 17, 18, 51, 20, 53, 24, 26, 27} 21
   {4, 40, 13, 49, 22, 31} 6
   {29} 1
   {36} 1

正多面体
======================================================================
モジュール ``sympy.combinatorics.polyhedron`` に正多面体を表現するクラスが実装されている。
そして、各正多面体に対応するオブジェクトが生成されており、
ユーザーはこれらを参照することができる。

クラス Polyhedron
----------------------------------------------------------------------
正多面体群を表現する。

* 基底クラスが Basic であることをうまく利用できるかもしれない。
* このクラスと PermutationGroup との間に has-a 関係がある。

プロパティー
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
クラス Polyhedron のプロパティーは次のものがある。

:code:`array_form`, :code:`cyclic_form`
  それぞれ頂点のインデックスを先述の形式で得る。

:code:`corners`, :code:`vertices`, :code:`size`
  最初のふたつのプロパティーは同一で、多面体の全頂点を返す。
  最後のプロパティーはこの多面体の頂点数を返す。

  例。生成済み多面体の頂点数を出力する。

  .. code-block:: ipython

     In [1]: solids = (tetrahedron, cube, octahedron, dodecahedron, icosahedron)

     In [2]: [s.size for s in solids]
     Out[2]: [4, 8, 6, 20, 12]

:code:`edges`, :code:`faces`
  それぞれ多面体の全辺、全面を返す。
  どちらも頂点列を表す tuple の set オブジェクト。

  例。正四面体の辺と面を出力する。
  また、各多面体において Euler の多面体公式を確認する。

  .. code-block:: ipython

     In [1]: tetrahedron.edges
     Out[1]: {(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)}

     In [2]: tetrahedron.faces
     Out[2]: {(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)}

     In [3]: [s.size - len(s.edges) + len(s.faces) for s in solids]
     Out[3]: [2, 2, 2, 2, 2]

:code:`pgroup`
  多面体群を返す。PermutationGroup オブジェクト。

  例。正四面体群の位数が 12 であることと 4 次の交代群と同型であることを見る。

  .. code-block:: ipython

     In [1]: T4 = tetrahedron.pgroup

     In [2]: T4.order()
     Out[2]: 12

     In [3]: T4.is_abelian
     Out[3]: False

     In [4]: A4 = AlternatingGroup(4)

     In [5]: A4.is_subgroup(T4) and T4.is_subgroup(A4)
     Out[5]: True

メソッド
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
メソッドはそれほど多くない。

:code:`reset()`
  オブジェクトを「初期状態」に復元する。

:code:`rotate(perm)`
  この多面体に置換 :code:`perm` を作用させる。

  * メソッドは引数の置換が妥当であるか判断しないので、
    呼び出し側で気を遣う必要がある。

テンソルの正規化
======================================================================
モジュール ``sympy.combinatorics.tensor_con`` には
テンソルの正規化に関する関数が何個かある。
どの関数も PermutationGroup を利用しているため、
この階層にこのモジュールがある。
本格的なテンソル代数モジュールが別にあるので、
そちらを見てから再びここに戻ってくる予定。

:doc:`./tensor` を参照。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
