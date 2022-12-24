======================================================================
ディオファントス方程式
======================================================================

ここではディオファントス方程式モジュールについて記す。整数係数方程式の検算などに
応用できるかもしれない。

.. contents:: ノート目次

基本事項
======================================================================

SymPy のドキュメントの出来が良いので、特に付け足すことはない。

* 関連機能のインポートは :code:`from sympy.solvers.diophantine import ...` の形
  になる。
* 方程式の構成方法にコツがある。未知数文字を明示的に整数型にする。次のパターンを
  覚えておけば間に合う。

  .. code:: python3

     x, y, z = symbols('x y z', integer=True)
     u, v, w = symbols('u v w', integer=True, positive=True)

* 関数 ``diophantine`` が基本的。引数にディオファントス方程式の左辺を指定する。

関数 ``diophantine``
======================================================================

関数 ``diophantine`` は既定の 5 パターンのディオファントス方程式を解くことができ
る。本稿では各パターンの名前を、それらを解くための専用関数のそれと同じに呼ぶこと
にする。

ソルバー関数と方程式のタイプの対応を記しておく。

.. csv-table::
   :delim: @
   :header: タイプ, 方程式の形式
   :widths: auto

   ``diop_linear``@ :math:`{a_1x_1 + a_2x_2 + \ldots + a_nx_n = b}`
   ``diop_quadratic``@ :math:`{ax^2 + bxy + cy^2 + dx + ey + f = 0}`
   ``diop_ternary_quadratic``@ :math:`{ax^2 + by^2 + cz^2 + dxy + eyz + fzx = 0}`
   ``diop_general_pythagorean``@ :math:`{a_{1}x_{1}^2 + a_{2}x_{2}^2 + \ldots + a_{n}x_{n}^2 = a_{n+1}x_{n+1}^2}`
   ``diop_general_sum_of_squares``@ :math:`{x_{1}^2 + x_{2}^2 + \ldots + x_{n}^2 = k}`

* 関数 ``diophantine`` は引数の方程式に相応しい下回りの関数を特定して呼び出すと
  いう、窓口のような役割がある。
* 関数 ``diophantine`` の戻り値の型は ``set`` である。一方、下回りの関数はいずれ
  も ``tuple`` である。
* 解が存在しない場合は ``None`` を含むコンテナーを返す。
* キーワード引数 :code:`param=t` を明示的に指定すれば、方程式の解の変数のための
  文字を決めることができる。

関数 ``classify_diop``
======================================================================

これも関数 ``diophantine`` の下回りの関数だが、与えられた方程式を解く前に、それ
がどのタイプの方程式であるかを鑑定するものである。

もし ``diophantine`` が（存在するにもかかわらず）解を見つけなかった場合に、関数
``classify_diop`` を単独で用いると良い。

.. code:: ipython

   In [1]: eq = 7*x + 7*y + 7*z - 2*x*y - 2*y*z - 2*z*x

   In [2]: diophantine(eq)
   ---------------------------------------------------------------------------
   NotImplementedError                       Traceback (most recent call last)
   <ipython-input-5-b6fe808b8a42> in <module>()
   ----> 1 diophantine(eq)

   D:\home\yojyo\devel\sympy\sympy\solvers\diophantine.py in diophantine(eq, param, syms)
       197         var_t, _, eq_type = classify_diop(base, _dict=False)
       198         _, base = signsimp(base, evaluate=False).as_coeff_Mul()
   --> 199         solution = diop_solve(base, param)
       200
       201         if eq_type in [

   D:\home\yojyo\devel\sympy\sympy\solvers\diophantine.py in diop_solve(eq, param)
       341     else:
       342         raise NotImplementedError(
   --> 343             'No solver has been written for %s.' % eq_type)
       344
       345

   NotImplementedError: No solver has been written for inhomogeneous_ternary_quadratic.

   In [3]: eq.subs({x:1, y:3, z:22})
   Out[3]: 0

   In [4]: from sympy.solvers.diophantine import classify_diop
   In [5]: classify_diop(eq)
   Out[5]:
   ([x, y, z],
    {x: 7, y: 7, y*z: -2, x*y: -2, z: 7, x*z: -2},
    'inhomogeneous_ternary_quadratic')

関数 ``diophantine`` は ``inhomogeneous_ternary_quadratic`` タイプの方程式をサ
ポートしていないので、解が求まらなかったのだとユーザーが判断できる。

もう一個見てみよう。

.. code:: ipython

   In [1]: x, y, z = symbols('x y z', integer=True, positive=True)

   In [2]: eq =  x**2 + 2*y**2 + 2*z**2 - 2*x*y + 2*y*z - 2*x*z - 5

   In [3]: diophantine(x**2 + 2*y**2 + 2*z**2 - 2*x*y + 2*y*z - 2*z*x - 5)
   ---------------------------------------------------------------------------
   NotImplementedError                       Traceback (most recent call last)
   <ipython-input-9-b6fe808b8a42> in <module>()
   ----> 1 diophantine(eq)

   D:\home\yojyo\devel\sympy\sympy\solvers\diophantine.py in diophantine(eq, param, syms)
       197         var_t, _, eq_type = classify_diop(base, _dict=False)
       198         _, base = signsimp(base, evaluate=False).as_coeff_Mul()
   --> 199         solution = diop_solve(base, param)
       200
       201         if eq_type in [

   D:\home\yojyo\devel\sympy\sympy\solvers\diophantine.py in diop_solve(eq, param)
       341     else:
       342         raise NotImplementedError(
   --> 343             'No solver has been written for %s.' % eq_type)
       344
       345

   NotImplementedError: No solver has been written for inhomogeneous_general_quadratic.

   In [4]: eq.subs({x:3, y:1, z:2})
   Out[4]: 0

   In [5]: classify_diop(eq)
   Out[5]:
   ([x, y, z],
    {1: -5, y*z: 2, z**2: 2, x*y: -2, y**2: 2, x**2: 1, x*z: -2},
    'inhomogeneous_general_quadratic')

こちらも例も解が存在するが、ソルバーが対応していないであろうことがわかる。

.. include:: /_include/python-refs-sci.txt
