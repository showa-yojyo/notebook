======================================================================
多項式
======================================================================

本稿ではモジュール ``sympy.polys`` のサブモジュールに点在するクラスや関数を可能
な限り見ていく。 SymPy_ は多項式の取り扱いをかなり重要視しているようで、素人に
とっては手に余るほどの豊富な機能を提供している。

.. contents:: ノート目次

.. note::

   本文中のすべての IPython セッション中のサンプルコードで、以下のインポートおよ
   び出力書式設定が済んでいるものとする。

   .. code:: python3

      from sympy import *
      init_printing(pretty_print=False)

基本
======================================================================

ここで紹介する関数は :code:`from sympy import *` で利用できるが、モジュールとし
ては ``sympy.polys`` にある関数を見ていく。

除算
----------------------------------------------------------------------

多項式同士の除算を行うには関数 ``div`` を用いる。

関数 :code:`div(f, g, *gens, **kwargs)`
  多項式の Euclid 除法を計算する。商と余りを同時に計算する。

  * 戻り値は ``tuple`` オブジェクトで、先頭から順に商、余りだ。

    * キーワード引数 ``polys=True`` を指定すると、商、余りを表現する Poly オブ
      ジェクトそれぞれを要素とする ``tuple`` オブジェクトを得られる。

  * キーワード引数 ``domain`` で中間生成する ``Poly`` オブジェクトがどの整域上の
    ものであるのかを指定する。引数として文字列 ``'ZZ'`` や ``'QQ'`` などを指定す
    る。例を示す：

    .. code:: ipython

       In [1]: from sympy.abc import x

       In [2]: div(x**5 + 4*x**2 + 9, 2*x**3 - 7*x, domain='QQ')
       Out[2]: (x**2/2 + 7/4, 4*x**2 + 49*x/4 + 9)

       In [3]: div(x**5 + 4*x**2 + 9, 2*x**3 - 7*x, domain='ZZ')
       Out[3]: (0, x**5 + 4*x**2 + 9)

       In [4]: div(x**5 + 4*x**2 + 9, 2*x**3 - 7*x, domain='RR')
       Out[4]: (0.5*x**2 + 1.75, 4.0*x**2 + 12.25*x + 9.0)

       In [5]: div(x**5 + 4*x**2 + 9, 2*x**3 - 7*x)
       Out[5]: (x**2/2 + 7/4, 4*x**2 + 49*x/4 + 9)

  * 多変数多項式にも対応している。
    どのシンボルが変数なのかを明示的に指示することもできる：

    .. code:: ipython

       In [6]: from sympy.abc import y

       In [7]: f = x**4 + x**3*y**2 + x**3*y + 6*x**3 - x**2*y - x*y**3 - x*y**2 - 6*x*y + 5*x + 4*y**2 + 3*y + 24

       In [8]: g = y**2 + 6+y + x

       In [9]: div(f, g)
       Out[9]: (x**3 - x*y + 5, -y**2 - 2*y - 6)

       In [10]: div(f, g, x)
       Out[10]: (x**3 - x*y + 5, -y**2 - 2*y - 6)

       In [11]: div(f, g, y)
       Out[11]: (x**3 - x*y + 4, x - y)

  * ``f`` と ``g`` を両方定数にすると、例外 ``ComputationFailed`` を送出すること
    で計算を失敗として処理する。

最大公約式と最小公倍式
----------------------------------------------------------------------

多項式同士の GCD および LCM を計算する関数を利用できる。

関数 :code:`gcd(f, g, *gens, **kwargs)`, :code:`gcd_list(seq, *gens, **args)`
  最大公約式を計算する。

  * 結果の多項式の最高次数係数がどうなるかは引数に依存する。例えば有理数係数同士
    の ``gcd`` はモニックになる。
  * 多変数多項式にも対応している。変数はアルファベット順に並んでいる。

関数 :code:`lcm(f, g, *gens, **kwargs)`, :code:`lcm_list(seq, *gens, **args)`
  最小公倍多項式を計算する。

  * :code:`lcm(f, g) * gcd(f, g) == f * g` が満たされるように結果を決める。

どちらも定数同士を評価できるが、別のモジュールに ``igcd``, ``ilcm`` という関数が
ある。しかも複数個の評価ができる。多項式の場合は整数の場合とは異なり、ペアの評価
か複数個の評価によって関数を使い分ける。例えば複数個の GCD を求める場合には関数
``gcd`` ではなく関数 ``gcd_list`` を用いる。引数 ``seq`` にリストなどを渡せばよ
い。

関数 :code:`resultant(f, g, *gens, **args)`
  多項式同士の集結式を計算する。

  * キーワード引数 :code:`includePRS=True` を指定すれば、主部分終結式係数のリス
    トをも生成する。このとき、戻り値は集結式と主部分終結式係数のリストの
    ``tuple`` オブジェクトとなる。ちなみに後者のみを返す関数 ``subresultants``
    というものがある。

無平方因子分解
----------------------------------------------------------------------

ここでは square-free factorization を無平方因子分解と呼ぶことにする。

関数 :code:`sqf(f, *gens, **args)`, :code:`sqf_list(f, *gens, **args)`
  多項式を無平方因子分解する。

  * 多変数多項式も対応する。
  * ``sqf`` の戻り値は単に多項式である。一方 ``sqf_list`` の戻り値は次の構造の
    ``tuple`` オブジェクトである：

    #. 無平方因子分解の最高次数項の係数
    #. 無平方因数とその指数からなるペアを並べた ``list`` オブジェクト

他にも ``sqf_`` な関数はある。

因数分解
----------------------------------------------------------------------

関数 :code:`factor(f, *gens, **args)`, :code:`factor_list(f, *gens, **args)`
  多項式を（デフォルトでは有理数の範囲で）因数分解する。

  * 一変数多項式だけではなく、多変数多項式も因数分解する。
  * 定数を因数分解させると、引数そのものが戻り値として得られる。特に整数を因数分
    解したい場合は、別に関数 ``factorint`` が用意されている。
  * キーワード引数各種により因数分解の範囲を「拡大」できる。

    .. code:: ipython

       In [1]: factor(x**2 + 1, gaussian=True)
       Out[1]: (x - I)*(x + I)

       In [2]: factor(x**2 + 1, extension=I)
       Out[2]: (x - I)*(x + I)

       In [3]: factor(x**10 -1, modulus=2)
       Out[3]: (x + 1)**2*(x**4 + x**3 + x**2 + x + 1)**2

Gröbner 基底
----------------------------------------------------------------------

多項式の方程式を解くのに用いられる概念である。

関数 :code:`groebner(F, *gens, **args)`
  Gröbner 基底を計算する。

  最初の引数の ``F`` が多項式のコレクションを指定して、次に多項式の変数を引数リ
  ストに並べて呼び出す。

  * キーワード引数 ``order`` で基底の項順序を指定することができる。デフォルトで
    は :code:`order='lex'` とのこと。

多項式の方程式、連立方程式を解く
----------------------------------------------------------------------

以下では「多項式の方程式」という用語は polynomial equation(s) を指す。これらの関
数を用いる際には、多項式変数シンボルを引数リストで明示的に指定する。

関数 :code:`solve(f, *symbols, **flags)`, :code:`solve_poly_system(seq, *gens, **args)`
  汎用の方程式ソルバーが多項式方程式を解く際にも用いられる。

  * ところでキーワード引数 :code:`domain='ZZ'` のようなものはサポートされていな
    いのだろうか。次のようにシンボルを設定し直せば意図通りの動きはするようだが。

    .. code:: ipython

       In [1]: solve([(x**4 - 1) * (x**4 - 4)], x)
       Out[1]: [(-1,), (1,), (-sqrt(2),), (sqrt(2),), (-I,), (I,), (-sqrt(2)*I,), (sqrt(2)*I,)]

       In [2]: x, y = symbols('x y', real=True)

       In [3]: solve([(x**4 - 1) * (x**4 - 4)], x)
       Out[3]: [(-1,), (1,), (-sqrt(2),), (sqrt(2),)]

       In [4]: x, y = symbols('x y', rational=True)

       In [5]: solve([(x**4 - 1) * (x**4 - 4)], x)
       Out[5]: [(-1,), (1,)]

  * 方程式が重根を持つ場合、戻り値を見ただけではすぐにはそれとわからないので注
    意。
  * Mathematica のドキュメントを参考にした例が解けない。先述の動作環境では 1 分
    経っても呼び出しから返ってこない。

    .. code:: ipython

       In [1]: x = symbols('x', real=True)

       In [2]: solve(x ** 1000000 - 2*x**777777 + 3*x**12345 + 9*x*67 - 10)

モジュール別
======================================================================

モジュール ``sympy.polys.polytools``
----------------------------------------------------------------------

.. todo::

   調査中。関数名を見れば何とかなりそうだ。

* 関数 :code:`degree(f, *gens, **args)`, :code:`degree_list(f, *gens, **args)`
* 関数 :code:`LC(f, *gens, **args)`
* 関数 :code:`LM(f, *gens, **args)`
* 関数 :code:`LT(f, *gens, **args)`
* 関数 :code:`rem(f, g, *gens, **args)`
* 関数 :code:`quo(f, g, *gens, **args)`
* 関数 :code:`discriminant(f, *gens, **args)`
* 関数 :code:`monic(f, *gens, **args)`
* 関数 :code:`compose(f, g, *gens, **args)`
* 関数 :code:`decompose(f, *gens, **args)`
* 関数 :code:`count_roots(f, inf=None, sup=None)`
* 関数 :code:`real_roots(f, multiple=True)`
* 関数 :code:`cancel(f, *gens, **args)`

モジュール ``sympy.polys.polyfuncs``
----------------------------------------------------------------------

関数 :code:`symmetrize(F, *gens, **args)`
  与えられた対称多項式をいくつかの基本対称式の和として書き換える。戻り値は対称式
  の ``tuple`` オブジェクトなので、受け取る側でこれを ``sum`` すれば全体になる。

  * 引数が対称でない多項式でもエラーなしで呼び出せる。
    戻り値内の多項式に、元の多項式に含まれていた文字が残ってしまうだけ。
  * キーワード引数 :code:`formal=True` を指定すること、基本対称式を名前で出して
    くれる。

    .. code:: ipython

       In [1]: symmetrize(x**3 + y**3 + z**3, formal=True)
       Out[1]: (s1**3 - 3*s1*s2 + 3*s3, 0, [(s1, x + y + z), (s2, x*y + x*z + y*z), (s3, x*y*z)])

関数 :code:`interpolate(data, x)`
  引数の点列データを通過するような多項式を生成する。補間。データ ``data`` の型は
  ``list`` か ``dict`` で通じる。次のものはどれも同じ多項式を生成する。

  * :code:`[(1, 1), (2, 4), (3, 9), (4, 16)]`
  * :code:`{1:1, 2:4, 3:9, 4:16}`
  * :code:`[1, 4, 9, 16]`

  .. code:: ipython

     In [1]: x0, x1, x2 = symbols('x0:3')

     In [2]: P = interpolate([x0, x1, x2], x)

     In [3]: P
     Out[3]: x**2*x0/2 - x**2*x1 + x**2*x2/2 - 5*x*x0/2 + 4*x*x1 - 3*x*x2/2 + 3*x0 - 3*x1 + x2

     In [4]: [P.subs({x:t}) for t in range(1, 4)]
     Out[4]: [x0, x1, x2]

モジュール ``sympy.polys.numberfields``
----------------------------------------------------------------------

代数的数、代数体、その辺り。多項式の話題から離れる可能性がある。

関数 :code:`minimal_polynomial(ex, x=None, **args)`, ``minpoly``
  代数的数の最小多項式を求める。

  * ``minpoly`` は単なる別名。
  * キーワード引数 ``domain`` で最小多項式をどの体上で求めるかを指定できる。

モジュール ``sympy.polys.monomials``
----------------------------------------------------------------------

単項式関連のモジュールだ。関数だけ見ていく。

ジェネレーター :code:`itermonomials(variables, degree)`
  指定次数の単項式に含まれるすべての単項式を返す。

  * 次数ゼロの項、すなわち ``1`` をも返す。
  * 返ってくる単項式の順序は不定。受け取り側で適宜ソートすればよい。

    * ソートのキーには別モジュールにある関数 ``monomial_key`` という（ドキュメン
      トがないようだ）ものを用いる。

関数 :code:`monomial_count(V, N)`
  相異なる ``V`` 個の文字からなる ``N`` 次多項式が含む単項式の個数を返す。

モジュール ``sympy.polys.polyroots``
----------------------------------------------------------------------

関数 :code:`roots(f, *gens, **flags)`
  一変数多項式の根を計算する。

  色々とキーワード引数があるが、利用する可能性のあるのはこれぐらいか。

  * :code:`filter=R` などのようにして、根を求める範囲を限定できる。

    * デフォルトでは複素数の範囲になっている。すなわち :code:`filter=C` だ。
    * 別の関数では ``domain`` と言っていた。

  * :code:`multiple=True` とすると、重根を丁寧に出力するようだ。

    .. code:: ipython

       In [1]: roots(x**2 - 2*x + 1, multiple=True)
       Out[1]: [1, 1]

       In [2]: roots(x**2 - 2*x + 1, multiple=False)
       Out[2]: {1: 2}

  * 根基で表現できる解だけを計算する。

    .. code:: ipython

       In [1]: roots(x**5 - 22*x + 19)
       Out[1]: {}

モジュール ``sympy.polys.specialpolys``
----------------------------------------------------------------------

わかる範囲で。

関数 :code:`interpolating_poly(n, x, X='x', Y='y')`
  Lagrange の補間多項式を生成する。

  * 第一引数は補間点列の点数。
  * 第二引数は多項式の変数文字を指定する。
  * 通過点列はデフォルトで :code:`(x0, y0)`, :code:`(x1, y1)`, ... となる。

関数 :code:`cyclotomic_poly(n, x=None, **args)`
  位数 ``n`` の円分多項式を生成する。

  * デフォルトだと生成する多項式の変数文字が ``_x`` とかいう汚いものになる？

関数 :code:`symmetric_poly(n, *gens, **args)`
  与えた複数の文字における ``n`` 番目の基本対称多項式を生成する。

  .. code:: ipython

     In [1]: symmetric_poly(4, symbols('x0:5'))
     Out[1]: x0*x1*x2*x3 + x0*x1*x2*x4 + x0*x1*x3*x4 + x0*x2*x3*x4 + x1*x2*x3*x4

関数 :code:`random_poly(x, n, inf, sup, domain=ZZ, polys=False)`
  各項の係数がランダムかつ指定範囲に収まるような多項式を生成する。

  .. code:: ipython

     In [1]: random_poly(x, 3, -10, 10)
     Out[1]: x**3 + 2*x**2 + 4*x + 9

     In [2]: random_poly(x, 3, -10, 10)
     Out[2]: 7*x**3 + 9*x**2 - 4*x + 9

     In [3]: random_poly(x, 3, -10, 10)
     Out[3]: -10*x**3 - 5*x + 7

     In [4]: random_poly(x, 3, -10, 10)
     Out[4]: 5*x**3 + 8*x**2 - 8*x - 4

モジュール ``sympy.polys.orthopolys``
----------------------------------------------------------------------

このモジュールには多項式の直交系に関係する関数が置いてある。

関数 :code:`chebyshevt_poly(n, x=None, **args)`, :code:`chebyshevu_poly(n, x=None, **args)`
  それぞれ第一種 Chebyshev 多項式、第二種 Chebyshev 多項式を求める。

  .. code:: ipython

     In [1]: simplify(chebyshevt_poly(3, cos(x)))
     Out[1]: cos(3*x)

     In [2]: simplify(chebyshevu_poly(3, cos(x)))
     Out[2]: 4*cos(x)*cos(2*x)

     In [3]: %paste
     Tm = chebyshevt_poly(2, x)
     Tn = chebyshevt_poly(3, x)
     integrate(Tm * Tn * 1/sqrt(1 - x**2), (x, -1, 1))

     ## -- End pasted text --
     Out[3]: 0

     In [4]: %paste
     Um = chebyshevu_poly(2, x)
     Un = chebyshevu_poly(3, x)
     integrate(Um * Un * 1/sqrt(1 - x**2), (x, -1, 1))

     ## -- End pasted text --
     Out[4]: 0

  この定積分の計算時間が若干長い。

関数 :code:`gegenbauer_poly(n, a, x=None, **args)`
  Gegenbauer 多項式 a.k.a. 超球関数を求める。
関数 :code:`hermite_poly(n, x=None, **args)`
  Hermite の多項式を求める。

  * 積分したら返ってこない。

関数 :code:`jacobi_poly(n, a, b, x=None, **args)`
  Jacobi の多項式を求める。

  .. code:: ipython

     In [1]: P = jacobi(2, 10, 20, x)

     In [2]: Q = jacobi(3, 10, 20, x)

     In [3]: integrate(P * Q * (1 - x)**10 * (1 + x)**20, (x, -1, 1))
     Out[3]: 0

関数 :code:`legendre_poly(n, x=None, **args)`
  Legendre の多項式を求める。

  .. code:: ipython

     In [1]: P3 = legendre_poly(3, x)

     In [2]: P7 = legendre_poly(7, x)

     In [3]: integrate(P3 * P7, (x, -1, 1))
     Out[3]: 0

関数 :code:`laguerre_poly(n, x=None, alpha=None, **args)`
  Laguerre の多項式を求める。スペリングが紛らわしいので、コンソールでテキスト補
  完のときは注意。

  * 積分したら返ってこない。

モジュール ``sympy.polys.rationaltools``
----------------------------------------------------------------------

このモジュールの代表的な機能は次の関数だ。

関数 :code:`together(expr, deep=False)`
  有理式 ``expr`` の通分を実行する。正確に言うと、有理式の和の形になっているもの
  を単一の有理式にする。

  * キーワード引数で :code:`deep=True` とすると、通分の適用を与式の「内側」まで
    有効にする。
  * 関数 ``apart`` と逆の働きをする。

モジュール ``sympy.polys.partfrac``
----------------------------------------------------------------------

部分分数分解に関係する機能を含むモジュール。

関数 :code:`apart(f, x=None, full=False, **options)`, :code:`apart_list(f, x=None, dummies=None, **options)`
  有理関数を部分分数分解する。

  .. code:: ipython

     In [1]: together((x**2 - 4*x)/(x**2 - x) + (x**2 + 3*x - 4)/(x**2- 1))
     Out[1]: ((x - 4)*(x**2 - 1) + (x - 1)*(x**2 + 3*x - 4))/((x - 1)*(x**2 - 1))

     In [2]: apart(_)
     Out[2]: 2 + 3/(x + 1) - 3/(x - 1)

  * キーワード引数 :code:`full=True` がわからない。

関数 :code:`assemble_partfrac_list(partial_list)`
  上述の ``apart_list`` の戻り値から有理関数の部分分数分解を復元する。

モジュール ``sympy.polys.dispersion``
----------------------------------------------------------------------

.. todo::

   調査中。

----

モジュールにしろ関数にしろクラスにしろ、かなりの量がある。整理して理解するのは困
難。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
