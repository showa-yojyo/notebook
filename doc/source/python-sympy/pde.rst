======================================================================
偏微分方程式
======================================================================

モジュール ``sympy.solvers.pde`` が提供する、偏微分方程式を解くための機能に関す
る覚え書きを記す。

.. contents:: ノート目次

.. note::

   紙幅の都合上、出力を一部手で改行した。

   本文中のすべての IPython セッション中のサンプルコードで、以下のインポートおよ
   び出力書式設定が済んでいるものとする。

   .. code:: python3

      init_printing(pretty_print=False)

基本機能
======================================================================

ここに記す関数は :program:`isympy` シェルがデフォルトで実行するインポート
:code:`from sympy import *` だけで利用可能だ。

関数 :code:`pde_separate(eq, fun, sep, strategy='mul')`
  偏微分方程式に含まれる従属変数的関数を加法的または乗法的に変数分離する。

  * 引数 ``eq`` は偏微分方程式を表す ``Eq`` オブジェクト。

    * 常微分方程式のときのような単なる数式ではダメ。

  * 引数 ``fun`` は ``eq`` を構成する従属変数的関数を表すオブジェクト。
  * 引数 ``sep`` は「分離先の関数」を表すオブジェクト。独立変数の個数に見合う？
    だけのオブジェクトをコレクションで渡す。

  * キーワード引数 ``strategy`` は分離の戦略（大げさ）を指定する。次のどちらかを
    選択する。

    * :code:`'add'`: 次に記す ``pde_separate_add`` を適用する。
    * :code:`'mul'`: 次に記す ``pde_separate_mul`` を適用する。
      こちらがデフォルト。

  * 戻り値の情報については下記の各関数の説明を参照。

関数 :code:`pde_separate_add(eq, fun, sep)`
  偏微分方程式に含まれる従属変数的関数を加法的に変数分離する。

  .. code:: ipython

     In [1]: x, t = symbols('x t')

     In [2]: u = symbols('u', function=True)

     In [3]: X, T = symbols('X T', function=True)

     In [4]: pde_separate_add(Eq(u(x, t).diff(x), E**(u(x, t).diff(t))), u(x, t), [X(x), T(t)])
     Out[4]: [Derivative(X(x), x), exp(Derivative(T(t), t))]

  * [4] 仮に :code:`u(x, t) == X(x) + T(t)` の形に書き直せると考える。このとき何
    かある定数が存在して、出力結果のリストの各項目に等しい。独立変数の個数分だけ
    の常微分方程式を解いて、それらの和をとれば :code:`u(x, t)` が求められる。

    ちなみにおそらく :math:`{C_1 x + t \log C_1 + C_2}` のようなものが一般解であ
    る。

関数 :code:`pde_separate_mul(eq, fun, sep)`
  偏微分方程式に含まれる従属変数的関数を乗法的に変数分離する。

  .. code:: ipython

     In [1]: x, y = symbols('x y')

     In [2]: u = symbols('u', function=True)

     In [3]: X, Y = symbols('X Y', function=True)

     In [4]: pde_separate_mul(Eq(u(x, y).diff(x, x), u(x, y).diff(y, y)), u(x, y), [X(x), Y(y)])
     Out[4]: [Derivative(X(x), x, x)/X(x), Derivative(Y(y), y, y)/Y(y)]

  * [4] 仮に :code:`u(x, y) == X(x) * Y(y)` の形に書き直せると考える。このとき何
    かある定数が存在して、出力結果のリストの各項目に等しい。常微分方程式を項目数
    分解いて、それらの積をとれば :code:`u(x, y)` が得られる。

    ちなみに :math:`{(C_1 e^{-C_0 x} + C_2 e^{C_0 x})(C_3 e^{-C_0 y} + C_4
    e^{C_0y})}` のようなものが一般解だ。

関数 :code:`pdsolve(eq, ...)`
  二変数関数に関する偏微分方程式を解く。

  * 引数 ``eq`` は対象となる偏微分方程式。いちおう ``Eq`` オブジェクトで渡しても
    よいし、ゼロに等しいとみなす数式オブジェクトでもよいことになっている。
  * キーワード引数 :code:`func=None` は偏微分方程式を構成する二変数関数を指定す
    る。ふつうは明示的に指定する必要はない。ソルバーが自動検出する。
  * キーワード引数 :code:`hint='default'` ではソルバーに微分方程式のタイプについ
    てヒントを教える。このヒントによって方程式の解法を調整することになる。

    以下、対応する ``dsolve`` のそれと同様。

    * ``default``
    * ``all``
    * ``all_Integral``
    * :code:`classify_pde(eq, ...)` が返すタイプ名

  * キーワード引数 :code:`dict=False` はソルバー関数が内々に利用するもの。このパ
    ラメーターはドキュメント化されていない。
  * キーワード引数 :code:`solvefun=None` はソルバーが返す任意関数に用いられる記
    号を指定する。特に指示のない場合は ``F`` が採用される。

関数 :code:`classify_pde(eq, ...)`
  偏微分方程式 ``eq`` のタイプを返す。関数 ``classify_ode`` の偏微分方程式バー
  ジョン。

  * キーワード引数 :code:`func=None` はソルバー関数と同じ。
  * キーワード引数 :code:`dict=False` はソルバー関数が内々に利用するもの。
  * 戻り値は文字列からなる ``tuple`` オブジェクトである。内容の順序についても
    「先頭ほど良く速く」である。
  * 全サポート分類を保持する ``allhints`` オブジェクト。偏微分方程式バージョンは
    四個しかない。実質三個だ。

    .. code:: ipython

       In [1]: from sympy.solvers.pde import allhints

       In [t2]: allhints
       Out[t2]:
       ('1st_linear_constant_coeff_homogeneous',
        '1st_linear_constant_coeff',
        '1st_linear_constant_coeff_Integral',
        '1st_linear_variable_coeff')

関数 :code:`checkpdesol(pde, sol, ...)`
  これは微分方程式の解を求めた後に、それを検算するのに用いる。関数
  ``checkodesol`` の偏微分方程式バージョン。

  * もし解が既知の微分方程式を評価して ``False`` が戻ってくるようならば、それは
    おそらく :code:`doit()` が式をゼロに簡単化することが不能なためと思われる。

特化型ソルバー
======================================================================

ここからはモジュール ``sympy.solvers.pde`` からの明示的なインポートを必要とする
機能を記す。

次の表はすべてのソルバー名と対応する偏微分方程式の形式だ。サポートしている偏微分
方程式は一階線形タイプのみのようだ。

.. csv-table::
   :delim: @
   :header: ソルバー, 偏微分方程式
   :widths: auto

   ``pde_1st_linear_constant_coeff`` @ :math:`{a \frac{\partial f(x, y)}{\partial x} + b \frac{\partial f(x, y)}{\partial y} + c f(x, y) = G(x, y)}`
   ``pde_1st_linear_constant_coeff_homogeneous``@:math:`{a \frac{\partial f(x, y)}{\partial x} + b \frac{\partial f(x, y)}{\partial y} + c f(x, y) = 0}`
   ``pde_1st_linear_variable_coeff`` @ :math:`{a(x, y) \frac{\partial f(x, y)}{\partial x} + b(x, y) \frac{\partial f(x, y)}{\partial y} + c(x, y) f(x, y) = G(x, y)}`

演習
======================================================================

ここに出てくる微分方程式は次の文書から拝借した。

* `DSolveで解く微分方程式 <http://reference.wolfram.com/language/tutorial/DSolveOverview.html>`_

以降のコードでは次の前処理を済ませている。

.. code:: python3

   a, b, c, x, y = symbols('a b c x y')
   u = symbols('u', function=True)
   z, p, q = u(x, y), u(x, y).diff(x), u(x, y).diff(y)

線形偏微分方程式
----------------------------------------------------------------------

ここでは線形偏微分方程式を解く様子をひたすら例示する。

定数係数同次一階線形偏微分方程式の例を示す。指数が汚いようだ。

.. code:: ipython

   In [1]: eq = Eq(2 * p + 3 * q + z, 0)

   In [2]: classify_pde(eq)
   Out[2]: ('1st_linear_constant_coeff_homogeneous',)

   In [3]: pdsolve(eq)
   Out[3]: Eq(u(x, y), F(3*x - 2*y)*exp(-2*x/13 - 3*y/13))

輸送方程式の例を示す。一般解に指数関数が出てこない。

.. code:: ipython

   In [1]: eq = Eq(p + q, 0)

   In [2]: classify_pde(eq)
   Out[2]: ('1st_linear_constant_coeff_homogeneous',)

   In [3]: pdsolve(eq)
   Out[3]: Eq(u(x, y), F(x - y))

非同次一階線形偏微分方程式の例を示す。指数が汚いのはソルバーのクセのようなもの
か。

.. code:: ipython

   In [1]: eq = Eq(7 * p + 3 * q + z, x + y)

   In [2]: classify_pde(eq)
   Out[2]: ('1st_linear_constant_coeff', '1st_linear_constant_coeff_Integral')

   In [3]: pdsolve(eq)
   Out[3]: Eq(u(x, y), x + y + F(3*x - 7*y)*exp(-7*x/58 - 3*y/58) - 10)

変数係数同次線形偏微分方程式の例を示す。これは残念ながら解けない。

.. code:: ipython

   In [1]: eq = Eq(sin(x) * p + E**q * p, 0)

   In [2]: classify_pde(eq)
   Out[2]: ()

変数係数非同次線形偏微分方程式の例を示す。

.. code:: ipython

   In [1]: eq = Eq(p + x * q, cos(x))

   In [2]: classify_pde(eq)
   Out[2]: ('1st_linear_variable_coeff',)

   In [3]: pdsolve(eq)
   Out[3]: Eq(u(x, y), F(-x**2/2 + y) + sin(x))

一階準線形偏微分方程式の例を示す。これは残念ながら解けない。

.. code:: ipython

   In [1]: eq = Eq(p + x * q, z**2 + 5)

   In [2]: classify_pde(eq)
   Out[2]: ()

非粘性 Burgers 方程式の例を示す。これは残念ながら解けない。

.. code:: ipython

   In [1]: eq = Eq(p + z * q, 0)

   In [2]: classify_pde(eq)
   Out[2]: ()

一階非線形偏微分方程式
----------------------------------------------------------------------

現在、SymPy のソルバーは一階非線形偏微分方程式に対応していない。

.. code:: ipython

   In [1]: classify_pde(Eq(p * q, 1)) # simple (envelop 1)
   Out[1]: ()

   In [2]: classify_pde(Eq(4*z + p**2 + q**2, 4)) # simple (envelop 2)
   Out[2]: ()

   In [3]: classify_pde(Eq(p**2 + q**2, 1)) # Eikonal
   Out[3]: ()

   In [4]: classify_pde(Eq(z, x*p + y*q + 2*p*q*sqrt(1 - p**2))) # Clairaut
   Out[4]: ()

   In [5]: classify_pde(Eq(p**2 + a*q, x + 3*y)) # separable
   Out[5]: ()

   In [6]: classify_pde(Eq(a * p **2 + b*p*q, c * z**2)) # missing independent variables
   Out[6]: ()

   In [7]: classify_pde(Eq(x*y*p*q, 1)) # reducible to f(x, y) == 0 by X = log(x), Y = log(y)
   Out[7]: ()

   In [8]: classify_pde(Eq((y*p - x*q)**2 + a*(x*p + y*q), b)) # solvable by polar coordinates transform
   Out[8]: ()

   In [9]: classify_pde(Eq(y*p*q - z*p + a*q, 0)) # solvable by Legendre transform
   Out[9]: ()

   In [10]: classify_pde(Eq((1 + q**2)*z, p*x)) # implicit form
   Out[10]: ()

二階偏微分方程式
----------------------------------------------------------------------

先ほど記したように、SymPy のソルバーは二階偏微分方程式には対応していない。
Laplace 方程式のもっとも簡単な形のものを試してみよう。

.. code:: ipython

   In [1]: classify_pde(Eq(u.diff(x, x) + u.diff(y, y), 0))
   ---------------------------------------------------------------------------
   ValueError                                Traceback (most recent call last)
   <ipython-input-13-d4ae5395f9e0> in <module>()
   ----> 1 classify_pde(Eq(u.diff(x, x) + u.diff(y, y), 0))

   D:\home\yojyo\devel\sympy\sympy\solvers\pde.py in classify_pde(eq, func, dict, **kwargs)
       277
       278     if prep or func is None:
   --> 279         prep, func_ = _preprocess(eq, func)
       280         if func is None:
       281             func = func_

   D:\home\yojyo\devel\sympy\sympy\solvers\deutils.py in _preprocess(expr, func, hint)
        75         if len(funcs) != 1:
        76             raise ValueError('The function cannot be '
   ---> 77                 'automatically detected for %s.' % expr)
        78         func = funcs.pop()
        79     fvars = set(func.args)

   ValueError: The function cannot be automatically detected for True.

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
