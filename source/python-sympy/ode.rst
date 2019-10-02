======================================================================
常微分方程式
======================================================================
モジュール ``sympy.solvers.ode`` が提供する、
常微分方程式を解くための機能に関する覚え書きを記す。

.. contents:: ノート目次

.. note::

   紙幅の都合上、出力を一部手で改行した。

   本文中のすべての IPython セッション中のサンプルコードで、
   以下のインポートおよび出力書式設定が済んでいるものとする。

   .. code:: pycon

      >>> from sympy import *
      >>> init_printing(pretty_print=False)
      >>> x = symbols('x')
      >>> f = Function('f')

基本機能
======================================================================
ここに記す関数は isympy シェルがデフォルトで実行するインポート :code:`from sympy import *` だけで利用可能だ。

SymPy で常微分方程式を解くには、関数 :code:`dsolve` を用いる。
簡単なケースではこれ一本で事足りる。
何か凝ったことをする場合に、その他の関数やデータを併用するという方針でよさそうだ。

関数 :code:`dsolve(eq, ...)`
  常微分方程式系を解く。

  方程式を一個解くときには、引数 :code:`eq` には何か導関数を含むような数式オブジェクトを指定する。
  方程式を複数個解くときには、同様に数式オブジェクトの list オブジェクトを指定する。
  ソルバーは各方程式が 0 と等しい条件を求める。

  * キーワード引数 :code:`func=None` は :code:`eq` がどの一変数関数に関する微分方程式なのかを指示する。
    方程式を複数個解くときには、やはり list の形式をとる。
    普通はソルバーが自動検出するため、指定しない。

  * キーワード引数 :code:`hint='default'` ではソルバーに微分方程式のタイプについてヒントを教える。
    このヒントによって方程式の解法を調整することになる。

    方程式を一個解くときには、与え得るパラメーターは次のとおり（すべて文字列だが、引用符を省略する）。

    * :code:`default`: 後述の関数 :code:`classify_ode(eq, ...)` にて記す。

    * :code:`all`: 全部の解法候補を適用する。
      この場合はソルバーの戻り値がキーと値をタイプ名と解からなる dict オブジェクトになる。
      タイプ名は文字列で、解は Equality オブジェクトだと思われる。
      それに加えて、ベスト解や階数等の副次的な情報も併せて含む。

    * :code:`all_Integral`: :code:`all` と同様に振る舞うが、
      もしタイプ xxx とタイプ xxx_Integral が候補にある場合、
      前者を省略するという点が異なる。
      後者の解法は結果オブジェクト内に Integral オブジェクトが未評価のまま残るが、
      計算処理が速いという特徴がある。

    * :code:`best`: 全部の候補を試して、もっとも解が単純なものを返す。

    * あるいはユーザーが別途関数 :code:`classify_ode(eq, ...)` を呼び出して得たタイプのうちの一つ。

  * キーワード引数 :code:`simplify=True` はソルバー内部が関数 :code:`odesimp` を呼び出すかどうかを指定する。

  * キーワード引数 :code:`ics=None` は境界条件を dict オブジェクトで指定できる。

    * キーの例 :code:`func(x0)`, :code:`func(x).diff(x).subs(x, x2)`
    * 利用可能になる条件は一階常微分方程式のべき級数？

  * キーワード引数 :code:`xi=None` および :code:`eta=None` は無限小関数。
    後述する関数 :code:`infinitesimals` の項で解説する。

  * キーワード引数 :code:`x0=0` は微分方程式のべき級数解をどの点周りに評価するかを指定する。
  * キーワード引数 :code:`n=6` はべき級数の指数をどこまで上げてよいかを指定する。

関数 :code:`classify_ode(eq, ...)`
  常微分方程式 :code:`eq == 0` のタイプを返す。
  微分方程式の教科書と考え方は同じで、
  ソルバーは微分方程式を解く手法を何種類かに名前をつけて分類している。
  この関数は与えられた微分方程式を解くのに相応しいであろう手法の名前を列挙するものだ。

  * キーワード引数 :code:`func=None` および :code:`ics=None` はソルバー関数と同じ。
  * キーワード引数 :code:`dict=False` はソルバー関数が内々に利用するもの。

  * 戻り値は文字列からなる tuple オブジェクトである。

    * ソルバーが方程式を解くのにデフォルトで採用するのは、この最初のタイプである。
      特定の方法で解かせたいならば、関数 :code:`dsolve` の :code:`hint` として、
      この候補のいずれかのタイプを指定する。

    * タイプは基本的には「このタイプとみなせば、方程式を解きやすいだろう」という順序で列挙されている。

  * サポートするタイプは :code:`allhints` という tuple オブジェクトが知っている。
    手許の環境では 34 個ある。

関数 :code:`checkodesol(ode, sol, ...)`
  これは微分方程式の解を求めた後に、それを検算するのに用いる。
  オブジェクト :code:`sol` をソルバーに渡したものと同じ :code:`ode` に代入して、
  ゼロになることを見たい。

  * 戻り値は 2 要素の tuple である。

    * [0]: 代入結果がゼロならば True であり、そうでなければ False である。
    * [1]: [0] が True ならば ``0`` である（逆は必ずしも成り立たない）。
      それ以外は代入結果が何になったのかを表現する値が入る。

  * この関数の呼び出しがなかなか返って来ないときは、
    間違いなく :code:`simplify` がキツイためだろう。

関数 :code:`homogeneous_order(eq, *symbols)`
  同次方程式 :code:`eq == 0` の次数を返す。

  * 非同次であれば None を返す。
  * シンボル関数も :code:`eq` になれるが、関数のすべての変数がシンボルである必要がある。
    なおかつ、数式中のその関数の変数が :code:`*symbols` にマッチしている必要がある。

下回りの機能
======================================================================
ここからはモジュール ``sympy.solvers.ode`` からの明示的なインポートを必要とする機能を記す。

関数 :code:`infinitesimals(eq, ...)`
  一階常微分方程式 :math:`y^\prime = f(x, y)` に対して、
  次の条件をみたすような点変換 :math:`\xi(x, y)` と :math:`\eta(x, y)` を返す：

  これらの点変換が次のリー群について、
  元の :math:`f` を用いて変換先の各変数に関する微分方程式 :math:`(y^*)^\prime=f(x^*, y^*)` が成り立つ。

  .. math::
     :nowrap:

     \begin{aligned}
     x^* &= X(x, y;\eps) = x + \eps \xi(x, y),\\
     y^* &= Y(x, y;\eps) = y + \eps \eta(x, y)
     \end{aligned}

  * 戻り値は dict の list の型をとる。
    内側の dict は、キーが点変換関数オブジェクトで、
    値が Function 系オブジェクトまたは定数である。

  * キーワード引数 :code:`hint` を用いて、
    点変換関数の計算方法のヒューリスティックを調整できるもよう。

関数 :code:`checkinfsol(eq, infinitesimals, ...)`
  この関数は上述の関数 :code:`infinitesimals` の結果を検証するのに用いられる。

  * 引数 :code:`infinitesimals` の型は（というか値は）先ほどの関数の戻り値と同じようにする。
  * 戻り値は list オブジェクトである。
    この要素は各点変換のペアに対応するブーリアン値と検算結果の値とのペアである。
    検算結果とは、次の偏微分に点変換関数を代入して評価した値である。

    .. math::
       :nowrap:

       \begin{align*}
       \frac{\partial \eta}{\partial x} + \left(\frac{\partial \eta}{\partial y}
        - \frac{\partial \xi}{\partial x}\right)\diff{y}{x}
        - \frac{\partial \xi}{\partial y} \left(\diff{y}{x}\right)^{2}
        - \xi\frac{\partial h}{\partial x} - \eta\frac{\partial h}{\partial y}
       \end{align*}

    すなわち、妥当な関数を与えればリストが含む要素はすべて :code:`(True, 0)` となる。

関数 :code:`odesimp(eq, func, order, constants, hint)`
  常微分方程式の単純化処理のための関数。

  * 関数 :code:`dsolve` が本関数を呼び出すので、
    これを単体で利用するケースというのは一般ユーザーにはまれだということだ。

関数 :code:`constant_renumber(expr, symbolname, startnumber, endnumber)`
  式に含まれる任意定数の番号付けを変更する関数。

  式 :code:`expr` 中にはいくつかの Symbol オブジェクトがあるという前提。
  そのオブジェクト名が :code:`symbolname` に末尾から数字のくっついたもので、
  さらにその数字が範囲 `[startnumber, endnumber)` にあれば、リネームの対象になる。
  新たに 1 から範囲の長さまでの連番が振られる。

関数 :code:`constantsimp(expr, constants)`
  式に含まれる任意定数に対する単純化処理のための関数。

  * :code:`C1 + C2` → :code:`C1`
  * :code:`C1 * C2` → :code:`C1`
  * :code:`exp(C1)` → :code:`C1`
  * etc.

関数 :code:`ode_sol_simplicity(sol, func, trysolving=True)`
  解の簡単さを示す数値を返す関数。
  例えば :code:`ode_sol_simplicity(A, f) < ode_sol_simplicity(B, f)` なる :code:`A` と :code:`B` については、
  :code:`A` のほうが :code:`B` よりも解が簡単であると解釈する。

  * ``-2`` や ``-1`` が戻ってくる場合は「解けている」または「解けていないが、解ける」を意味する。
  * 何か正の整数が戻ってくる場合は「解けない」か「与えられた :code:`func` について解けない」を意味する。
    この値は解の文字列的な長さである。長い方程式のほうが難しそうだからこうしたのか。
  * :code:`oo` が戻ってくる場合、解が未評価の Integral オブジェクトを含むことを意味する。

  * キーワード引数 :code:`trysolving` は、
    ユーザーが既に解が解けないことを知っているときに利用できる。
    値 False を指示することで、計算を省略する。

    * :code:`dsolve` の :code:`simplify=False` と連動している。

特化型ソルバー
======================================================================
SymPy のドキュメントが関数名と微分方程式の数式 (LaTeX) を併記していて素晴らしいので、
カタログのように参照すると目当てのタイプのソルバーが提供されているかどうかはすぐにわかるだろう。

ここでは関数名だけを列挙するに留める。
対応するヒント名を併記するとメモ代わりになるか。

* :code:`ode_1st_exact`
* :code:`ode_1st_homogeneous_coeff_subs_dep_div_indep`
* :code:`ode_1st_homogeneous_coeff_subs_indep_div_dep`
* :code:`ode_1st_linear`
* :code:`ode_almost_linear`
* :code:`ode_Bernoulli`
* :code:`ode_linear_coefficients`
* :code:`ode_Liouville`
* :code:`ode_nth_linear_constant_coeff_homogeneous`
* :code:`ode_nth_linear_constant_coeff_undetermined_coefficients`
* :code:`ode_nth_linear_constant_coeff_variation_of_parameters`
* :code:`ode_Riccati_special_minus2`
* :code:`ode_separable`
* :code:`ode_separable_reduced`

連立常微分方程式
======================================================================
連立常微分方程式を :code:`dsolve` に評価させると、
最初に関数 :code:`classify_sysode` を呼ぶ。
これで方程式のタイプを判定して、特化型のソルバーに処理を委ねる。

このタイプ判定が下の図のように入れ子になっていて、
末端のソルバーでは結局 :code:`dsolve` を単一の方程式に対して適用することを繰り返す。

.. code:: text

   sysode_linear_neq_order<M>
       sysode_linear_neq_order1
           _linear_neq_order1_type1
   sysode_linear_<N>eq_order<M>
       sysode_linear_2eq_order1
           _linear_2eq_order1_type<i> i: 1-7
       sysode_linear_2eq_order2
           _linear_2eq_order2_type<i> i: 1-11
       sysode_linear_3eq_order1
           _linear_3eq_order1_type<i> i: 1-4
           _linear_neq_order1_type1 も流用。
   sysode_nonlinear_<N>seq_order<M>
       sysode_nonlinear_2eq_order1
           _nonlinear_2eq_order1_type<i> i: 1-4
       sysode_nonlinear_3eq_order1
           _nonlinear_3eq_order1_type<i> i: 1-5

演習
======================================================================
ここに出てくる微分方程式は次の文書から拝借した。

* `DSolveで解く微分方程式 <http://reference.wolfram.com/language/tutorial/DSolveOverview.html>`_
* `Non-homogeneous 2nd order Euler-Cauchy differential equation <http://math.stackexchange.com/questions/650774/non-homogeneous-2nd-order-euler-cauchy-differential-equation>`_

演習で得た自分なりのコツを次にまとめる。

* 長い数式で表現される常微分方程式は SymPy のオブジェクトとしても長い表現になる。
  何度もタイプするハメにならぬように、素直にローカル変数を宣言してバインドしておく。

* ソルバーに渡す前に関数 :code:`classify_ode` で常微分方程式のタイプを判定しておく。
  その結果が次の :code:`dsolve` 呼び出しの :code:`hint` パラメーターを
  :code:`all` にするか :code:`all_Integral` にするかの判断材料になる。

  * 空の tuple オブジェクトが戻ってくるようならば、
    残念だがその常微分方程式を SymPy で解くのを諦める。

* 関数 :code:`dsolve` を呼び出すときは許される限り :code:`all_Integral` を指定する。
  この戻り値をザッと見ると、未評価の積分オブジェクトが一般解に含まれているだろう。
  必要ならばこれを :code:`doit()` にて手動で遅延評価する。

常微分方程式
----------------------------------------------------------------------
連立しないほうのパターン。

使い方
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

例えば微分方程式 :math:`y^\prime = y` を解くには次のようにするのがいちばん早い：

.. code:: pycon

   >>> y = f(x)
   >>> dsolve(y.diff(x) - y, y)
   Eq(f(x), C1*exp(x))

求積法だけで解が求まる常微分方程式
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
次のデモは単に :code:`integrate` するだけで解が得られる常微分方程式を与えるものだ。
SymPy のソルバーは一階線形常微分方程式の特別に単純な場合として処理する。

.. code:: pycon

   >>> eq = f(x).diff(x) - x**2 * sin(x) + sqrt(1 + x**2)
   >>> dsolve(eq, hint='all_Integral')
   {'nth_linear_constant_coeff_variation_of_parameters_Integral': Eq(f(x), C1 - Integral(-x**2*sin(x) + sqrt(x**2 + 1), x)),
    'Bernoulli_Integral': Eq(f(x), C1 - Integral(-x**2*sin(x) + sqrt(x**2 + 1), x)),
    '1st_linear_Integral': Eq(f(x), C1 + Integral(x**2*sin(x) - sqrt(x**2 + 1), x)),
    'nth_algebraic_Integral': Eq(f(x), C1 + Integral(x**2*sin(x) - sqrt(x**2 + 1), x)),
    '1st_exact_Integral': Eq(Subs(Integral(1, _y) + Integral(-x**2*sin(x) + sqrt(x**2 + 1), x), _y, f(x)), C1),
    'separable_Integral': Eq(Integral(1, (_y, f(x))), C1 + Integral(x**2*sin(x) - sqrt(x**2 + 1), x)),
    'nth_linear_euler_eq_nonhomogeneous_variation_of_parameters_Integral': Eq(f(x), C1 - Integral(-x**2*sin(x) + sqrt(x**2 + 1), x)),
    'best': Eq(f(x), C1 - Integral(-x**2*sin(x) + sqrt(x**2 + 1), x)),
    'best_hint': 'Bernoulli_Integral',
    'default': 'nth_algebraic',
    'order': 1}
   >>> _['best'].doit()
   Eq(f(x), C1 - x**2*cos(x) - x*sqrt(x**2 + 1)/2 + 2*x*sin(x) + 2*cos(x) - asinh(x)/2)

変数分離形常微分方程式
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
変数分離系は微分方程式入門の最初の方に乗っている基本形だ。

.. code:: pycon

   >>> eq = y.diff(x) - (x**2 * y**2)/sqrt(3 - x**2)
   >>> classify_ode(eq)
   ('separable',
    '1st_exact',
    'Bernoulli',
    '1st_power_series',
    'lie_group',
    'separable_Integral',
    '1st_exact_Integral',
    'Bernoulli_Integral')
   >>> dsolve(eq, hint='all')
   {'Bernoulli_Integral': Eq(f(x), 1/(C1 + Integral(-x**2/sqrt(3 - x**2), x))),
    '1st_exact': Eq(f(x), 2/(C1 + x*sqrt(3 - x**2) - 3*asin(sqrt(3)*x/3))),
    '1st_power_series': Eq(f(x), C1 + sqrt(3)*C1**2*x**3/9 + sqrt(3)*C1**2*x**5/90 + O(x**6)),
    'lie_group': Eq(f(x), 2/(C1 + x*sqrt(3 - x**2) - 3*asin(sqrt(3)*x/3))),
    'Bernoulli': Eq(f(x), 1/(C1 + x*sqrt(3 - x**2)/2 - 3*asin(sqrt(3)*x/3)/2)),
    '1st_exact_Integral': Eq(Subs(Integral(_y**(-2), _y) + Integral(-x**2/sqrt(3 - x**2), x), _y, f(x)), C1),
    'separable': Eq(f(x), 2/(C1 + x*sqrt(3 - x**2) - 3*asin(sqrt(3)*x/3))),
    'separable_Integral': Eq(Integral(_y**(-2), (_y, f(x))), C1 + Integral(x**2/sqrt(3 - x**2), x)),
    'best': Eq(f(x), 2/(C1 + x*sqrt(3 - x**2) - 3*asin(sqrt(3)*x/3))),
    'best_hint': 'separable',
    'default': 'separable',
    'order': 1}
   >>> _['best'].doit()
   Eq(f(x), 2/(C1 + x*sqrt(3 - x**2) - 3*asin(sqrt(3)*x/3)))

.. code:: pycon

   >>> eq = y.diff(x) - (x**2 * exp(y))/sqrt(3 - x**2)
   >>> dsolve(eq, hint='all')
   {'separable': Eq(f(x), log(1/(C1 + x*sqrt(3 - x**2) - 3*asin(sqrt(3)*x/3))) + log(2)),
    '1st_power_series': Eq(f(x), sqrt(3)*x**3*exp(C1)/9 + sqrt(3)*x**5*exp(C1)/90 + C1 + O(x**6)),
    'separable_Integral': Eq(Integral(exp(-_y), (_y, f(x))), C1 + Integral(x**2/sqrt(3 - x**2), x)),
    'lie_group': Eq(f(x), log(2/(C1 + x*sqrt(3 - x**2) - 3*asin(sqrt(3)*x/3)))),
    'best': Eq(f(x), log(1/(C1 + x*sqrt(3 - x**2) - 3*asin(sqrt(3)*x/3))) + log(2)),
    'best_hint': 'separable',
    'default': 'separable',
    'order': 1}
   >>> _['best'].doit()
   Eq(f(x), log(1/(C1 + x*sqrt(3 - x**2) - 3*asin(sqrt(3)*x/3))) + log(2))

一階同次常微分方程式
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
変数変換 :math:`z = y/x` で変数分離形常微分方程式になるものを一つ示す。

.. code:: pycon

   >>> eq = y.diff(x) + (x**2 - 3*y**2)/(x*y)
   >>> dsolve(eq, y, hint='all')
   Eq(f(x), x*sqrt(C1*x**4 + 2)/2)],
    'best': Eq(f(x), sqrt(x**6*(C1 + 1/(2*x**4)))),
    'best_hint': 'Bernoulli',
    'default': 'Bernoulli',
    'order': 1}
   >>> _['best'].doit()
   Eq(f(x), sqrt(x**6*(C1 + 1/(2*x**4))))

一階線形常微分方程式
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
一階線形方程式の例だ。非同次項があるものを試す。
``exp`` と ``Integral`` が目につくのがいかにもそれらしい。

.. code:: pycon

   >>> eq = y.diff(x) + x*y - exp(3*x)
   >>> dsolve(eq, y, hint='all')
   {'almost_linear': Eq(f(x), (C1 + Integral(exp(3*x)*exp(x**2/2), x))*exp(-x**2/2)),
    'Bernoulli_Integral': Eq(f(x), (C1 - Integral(-exp(3*x)*exp(Integral(x, x)), x))*exp(-Integral(x, x))),
    '1st_linear_Integral': Eq(f(x), (C1 + Integral(exp(3*x)*exp(Integral(x, x)), x))*exp(-Integral(x, x))),
    '1st_exact': Eq(Integral((x*f(x) - exp(3*x))*exp(x**2/2), x), C1),
    '1st_power_series': Eq(f(x), x + x**2*(3 - C1)/2 + 7*x**3/6 + x**4*(C1 + 6)/8 + 53*x**5/120 + C1 + O(x**6)),
    '1st_linear': Eq(f(x), (C1 + Integral(exp(3*x)*exp(x**2/2), x))*exp(-x**2/2)),
    'lie_group': Eq(f(x), (C1 + Integral(exp(3*x)*sqrt(exp(x**2)), x))/sqrt(exp(x**2))),
    'Bernoulli': Eq(f(x), (C1 + Integral(exp(3*x)*exp(x**2/2), x))*exp(-x**2/2)),
    '1st_exact_Integral': Eq(Subs(Integral((_y*x - exp(3*x))*exp(x**2/2), x) + Integral(exp(x**2/2) - Integral(x*exp(x**2/2), x), _y), _y, f(x)), C1),
    'almost_linear_Integral': Eq(f(x), (C1 + Integral(exp(3*x)*exp(Integral(x, x)), x))*exp(-Integral(x, x))),
    'best': Eq(f(x), x + x**2*(3 - C1)/2 + 7*x**3/6 + x**4*(C1 + 6)/8 + 53*x**5/120 + C1 + O(x**6)),
    'best_hint': '1st_power_series',
    'default': '1st_exact',
    'order': 1}
   >>> _['best'].doit()
   Eq(f(x), x + x**2*(3 - C1)/2 + 7*x**3/6 + x**4*(C1 + 6)/8 + 53*x**5/120 + C1 + O(x**6))

Bernoulli 常微分方程式
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Bernoulli 常微分方程式を解く。

.. code:: ipython

   In [1]: eq = f(x).diff(x) + 11*x*f(x) - x**3 * f(x)**3

   In [2]: dsolve(eq, hint='all_Integral')
   Out[2]:
   {'Bernoulli_Integral': Eq(f(x), 1/sqrt((C1 + 2*Integral(-x**3*exp(-2*Integral(11*x, x)), x))*exp(2*Integral(11*x, x)))),
    'best': Eq(f(x), 1/sqrt((C1 + 2*Integral(-x**3*exp(-2*Integral(11*x, x)), x))*exp(2*Integral(11*x, x)))),
    'best_hint': 'Bernoulli_Integral',
    'default': 'Bernoulli',
    'order': 1}

   In [3]: _['best'].doit()
   Out[3]: Eq(f(x), 1/sqrt((C1 + (11*x**2 + 1)*exp(-11*x**2)/121)*exp(11*x**2)))

   In [4]: eq = 3*x*f(x).diff(x) - 7*x*log(x)*f(x)**5 - f(x)

   In [5]: classify_ode(eq)
   Out[5]: ('Bernoulli', 'lie_group', 'Bernoulli_Integral')

   In [6]: dsolve(eq, hint='all_Integral')
   Out[6]:
   {'Bernoulli_Integral': Eq(f(x), ((C1 + 4*Integral(-7*exp(-4*Integral(-1/(3*x), x))*log(x)/3, x))*exp(4*Integral(-1/(3*x), x)))**(-1/4)),
    'best': Eq(f(x), ((C1 + 4*Integral(-7*exp(-4*Integral(-1/(3*x), x))*log(x)/3, x))*exp(4*Integral(-1/(3*x), x)))**(-1/4)),
    'best_hint': 'Bernoulli_Integral',
    'default': 'Bernoulli',
    'order': 1}

Riccati 常微分方程式
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Riccati 型 :math:`y^\prime = P(x)y + Q(x)y + R(x)y^2,\;P(x) \ne 0,\;R(x) \ne 0` を試す。

.. code:: pycon

   >>> dsolve(y.diff(x) - 3 * y**2 + 2/x**2, y, hint='all')
   {'separable_reduced_Integral': Eq(Integral(1/(_y*(3*_y + 1 - 2/_y)), (_y, x*f(x))), C1 + Integral(1/x, x)),
    'lie_group': Eq(f(x), -(2*C1/3 + x**5)/(x*(-C1 + x**5))),
    'Riccati_special_minus2': Eq(f(x), -(-5*I*tan(C1 + 5*I*log(x)/2) + 1)/(6*x)),
    'separable_reduced': Eq(f(x), (-C1*x**4 - 2/(3*x))/(C1*x**5 - 1)),
    'best': Eq(f(x), -(2*C1/3 + x**5)/(x*(-C1 + x**5))),
    'best_hint': 'lie_group',
    'default': 'Riccati_special_minus2',
    'order': 1}

デフォルトとして認識されていることがわかる。

.. In [30]: dsolve(f(x).diff(x) - (5*x**2 - 2*f(x)**2 + 11)/(sin(f(x)) + 4*x*f(x) + 3), f(x))
.. In [271]: classify_ode(eq)
.. Out[271]: ('1st_power_series', 'lie_group')
.. 返って来ない

.. # 解けない Clairaut; nonlinear
.. In [33]: dsolve(f(x) - x * f(x).diff(x) - f(x).diff(x)**2 - exp(f(x).diff(x)), f(x))
.. In [275]: classify_ode(eq)
.. Out[275]: ('lie_group',)

.. ----------------------------------------------------------------------
.. # アーベル方程式
.. In [34]: dsolve(f(x).diff(x) - f(x)**3 + x*f(x)**2/(x - 1), f(x))
.. In [277]: classify_ode(eq)
.. Out[277]: ('1st_power_series', 'lie_group')
.. Out[34]: Eq(f(x), C1 + C1*x + 2*C1*x**2 + C1*x**3*(16*C1 + 7)/6 + C1*x**4*(21*C1 + 10)/12 + C1*x**5*(C1*(104*C1 + 35) + C1*(48*C1**2 + 6*C1*(30*C1 + 1) + 227*C1 + 37) + 73*C1 + 39)/60 + O(x**6))

.. ----------------------------------------------------------------------
.. # キーニ
.. In [36]: diff(f(x).diff(x) - 5*f(x)**4 - 3*x**(-Rational(4, 3)), f(x))
.. In [279]: classify_ode(eq)
.. Out[279]: ('lie_group',)
.. Out[36]: -20*f(x)**3

定数係数二階線形常微分方程式
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
この型のものは同次形ならば ``dsolve()`` に頼らなくでもなんとかなる。

特性方程式の解のパターン別に試す。
ソルバーが適切なタイプ判定をしていることがわかる。

.. code:: ipython

   In [1]: eq = f(x).diff(x, 2) + 5 * f(x).diff(x) - 6 * f(x)

   In [2]: dsolve(eq, hint='all_Integral')
   Out[2]:
   {'best': Eq(f(x), C1*exp(-6*x) + C2*exp(x)),
    'best_hint': 'nth_linear_constant_coeff_homogeneous',
    'default': 'nth_linear_constant_coeff_homogeneous',
    'nth_linear_constant_coeff_homogeneous': Eq(f(x), C1*exp(-6*x) + C2*exp(x)),
    'order': 2}

   In [3]: eq = f(x).diff(x, 2) - 6 * f(x).diff(x) + 9 * f(x)

   In [4]: dsolve(eq, hint='all_Integral')
   Out[4]:
   {'best': Eq(f(x), (C1 + C2*x)*exp(3*x)),
    'best_hint': 'nth_linear_constant_coeff_homogeneous',
    'default': 'nth_linear_constant_coeff_homogeneous',
    'nth_linear_constant_coeff_homogeneous': Eq(f(x), (C1 + C2*x)*exp(3*x)),
    'order': 2}

   In [5]: eq = f(x).diff(x, 2) - f(x).diff(x) + f(x)

   In [5]: dsolve(eq, hint='all_Integral')
   Out[5]:
   {'best': Eq(f(x), (C1*sin(sqrt(3)*x/2) + C2*cos(sqrt(3)*x/2))*sqrt(exp(x))),
    'best_hint': 'nth_linear_constant_coeff_homogeneous',
    'default': 'nth_linear_constant_coeff_homogeneous',
    'nth_linear_constant_coeff_homogeneous': Eq(f(x), (C1*sin(sqrt(3)*x/2) + C2*cos(sqrt(3)*x/2))*sqrt(exp(x))),
    'order': 2}

Euler 常微分方程式
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Euler 常微分方程式のデモを示す。

.. code:: ipython

   In [1]: eq = x**2 * f(x).diff(x, 2) + 5 * x * f(x).diff(x) + 6 * f(x)

   In [2]: dsolve(eq, hint='all_Integral')
   Out[2]:
   {'best': Eq(f(x), (C1*sin(sqrt(2)*log(x)) + C2*cos(sqrt(2)*log(x)))/x**2),
    'best_hint': 'nth_linear_euler_eq_homogeneous',
    'default': 'nth_linear_euler_eq_homogeneous',
    'nth_linear_euler_eq_homogeneous': Eq(f(x), (C1*sin(sqrt(2)*log(x)) + C2*cos(sqrt(2)*log(x)))/x**2),
    'order': 2}

次のものは非同次？

.. code:: ipython

   In [1]: eq = x**2 * f(x).diff(x, 2) - 2 * f(x) - x**3 * exp(x)

   In [2]: classify_ode(eq)
   Out[2]:
   ('nth_linear_euler_eq_nonhomogeneous_variation_of_parameters',
    'nth_linear_euler_eq_nonhomogeneous_variation_of_parameters_Integral')

   In [3]: dsolve(eq)
   Out[3]: Eq(f(x), C1/x + C2*x**2 + x*exp(x) - 2*exp(x) + 2*exp(x)/x)

.. Legendre type...
.. In [107]: eq = (3*x + 1)**2 * f(x).diff(x, 2) + 5 * (3*x + 1) * f(x).diff(x) + 6 * f(x)
.. NotImplementedError: solve: Cannot solve (3*x + 1)**2*Derivative(f(x), x, x) + (15*x + 5)*Derivative(f(x), x) + 6*f(x)

.. eq = f(x).diff(x, 2) + log(x) * f(x).diff(x) + f(x)/x
.. NotImplementedError: solve: Cannot solve log(x)*Derivative(f(x), x) + Derivative(f(x), x, x) + f(x)/x

特殊な二階常微分方程式
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Airy 微分方程式を解く。
ここではべき級数の形で一般解を得たが、よそではある広義積分で与えられる。

.. code:: ipython

   In [1]: eq = f(x).diff(x, 2) - x * f(x)

   In [2]: classify_ode(eq)
   Out[2]: ('2nd_power_series_ordinary',)

   In [3]: dsolve(eq, hint='all')
   Out[3]:
   {'2nd_power_series_ordinary': Eq(f(x), C2*(x**3/6 + 1) + C1*x*(x**3/12 + 1) + O(x**6)),
    'best': Eq(f(x), C2*(x**3/6 + 1) + C1*x*(x**3/12 + 1) + O(x**6)),
    'best_hint': '2nd_power_series_ordinary',
    'default': '2nd_power_series_ordinary',
    'order': 2}

Bessel 微分方程式を解く。
またしてもべき級数の形で一般解が得られる。
SymPy は Airy 関数も Bessel 関数も持っているのに、
微分方程式のモジュールには関与していないということだろうか。

.. code:: ipython

   In [1]: eq = x**2 * f(x).diff(x, 2) + x * f(x).diff(x) + (x**2 - 16)*f(x)

   In [2]: classify_ode(eq)
   Out[2]: ('2nd_power_series_regular',)

   In [3]: dsolve(eq, hint='all')
   Out[3]:
   {'2nd_power_series_regular': Eq(f(x), C1*x**4 + O(x**6)),
    'best': Eq(f(x), C1*x**4 + O(x**6)),
    'best_hint': '2nd_power_series_regular',
    'default': '2nd_power_series_regular',
    'order': 2}

.. ----------------------------------------------------------------------

.. # Hermite
.. In [287]: eq = f(x).diff(x, 2) - 2 * x * f(x).diff(x) + 2 * n * f(x)
..
.. In [288]: classify_ode(eq)
.. Out[288]: ('2nd_power_series_ordinary',)
..
.. In [289]: dsolve(eq)
.. Out[289]: Eq(f(x), C2*(n**2*x**4/6 - n*x**4/3 - n*x**2 + 1) + C1*x*(-n*x**2/3 +x**2/3 + 1) + O(x**6))

.. In [291]: a, b, c = symbols('a b c')
..
.. In [292]: eq = (x**2 - x)*f(x).diff(x, 2) + ((a + b + 1)*x - c)*f(x).diff(x) + b * a* f(x)
..
.. In [293]: classify_ode(eq)
.. Out[293]: ()

.. In [294]: 64 * x**2 *(x - 1)**2 * f(x).diff(x, 2) + 32 * x *(x - 1)*(3*x - 1)*f(x).diff(x) + (5*x - 21)*f(x)
.. Out[294]: 64*x**2*(x - 1)**2*Derivative(f(x), x, x) + 32*x*(x - 1)*(3*x - 1)*Derivative(f(x), x) + (5*x - 21)*f(x)
..
.. In [295]: eq = _
..
.. In [296]: classify_ode(eq)
.. Out[296]: ()

.. In [297]: eq = x * f(x).diff(x, 2) + (10 * x**3 - 1)*f(x).diff(x, 1) + 5*x**2 *(5*x**3 + 1)*f(x)
..
.. In [298]: classify_ode(eq)
.. Out[298]: ()

.. In [299]: eq = 4*x * f(x).diff(x, 2) + (7*x + 12) * f(x).diff(x) + 21 * f(x)
..
.. In [300]: classify_ode(eq)
.. Out[300]: ('2nd_power_series_regular',)
..
.. In [301]: dsolve(eq)
.. Out[301]: Eq(f(x), C1*(-16807*x**5/122880 + 2401*x**4/6144 - 343*x**3/384 + 49*x**2/32 - 7*x/4 + 1) + O(x**6))

.. In [302]: eq = f(x).diff(x, 2) - x**2 * f(x).diff(x) - f(x) - 1
..
.. In [303]: classify_ode(eq)
.. Out[303]: ()

.. In [124]: eq = f(x).diff(x, 2) - exp(5*x)*f(x)
..
.. In [125]: classify_ode(eq)
.. Out[125]: ()

.. In [304]: eq = f(x).diff(x, 2)*sin(x)*cos(x)**2 - f(x).diff(x)*(3*sin(x)**2 + 1)*cos(x) - f(x)*sin(x)**3
..
.. In [305]: classify_ode(eq)
.. Out[305]: ()
..
.. In [308]: eq = f(x).diff(x, 2) + (k**2 + 2*sech(x)**2)*f(x)
..
.. In [309]: classify_ode(eq)
.. Out[309]: ()
..
.. In [311]: d, l = symbols('d l')
..
.. In [312]: eq = f(x).diff(x, 2) + (-d + d*(1 - exp(-b*x))**2)*f(x) - l * f(x)
..
.. In [313]: classify_ode(eq)
.. Out[313]: ()

二階線形非同次常微分方程式
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
解けているように見えるが、ヒントを :code:`all` にすると返って来ない？
後半で同次版も解いてみる。

.. code:: ipython

   In [1]: eq = x**2 * f(x).diff(x, 2) + f(x) - x**2

   In [2]: classify_ode(eq)
   Out[2]:
   ('nth_linear_euler_eq_nonhomogeneous_undetermined_coefficients',
    'nth_linear_euler_eq_nonhomogeneous_variation_of_parameters',
    'nth_linear_euler_eq_nonhomogeneous_variation_of_parameters_Integral')

   In [3]: dsolve(eq)
   Out[3]: Eq(f(x), C1*sqrt(x)*sin(sqrt(3)*log(x)/2) + C2*sqrt(x)*cos(sqrt(3)*log(x)/2) + x**2/3)

   In [4]: eq = x**2 * f(x).diff(x, 2) + f(x)

   In [5]: classify_ode(eq)
   Out[5]: ('nth_linear_euler_eq_homogeneous', '2nd_power_series_regular')

   In [6]: dsolve(eq)
   Out[6]: Eq(f(x), sqrt(x)*(C1*sin(sqrt(3)*log(x)/2) + C2*cos(sqrt(3)*log(x)/2)))

二階非線形常微分方程式
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Liouville 型は解ける。それ以外が解けない。

.. code:: ipython

   In [1]: eq = f(x).diff(x, 2) - 5 * x * f(x).diff(x) - f(x).diff(x)**2

   In [2]: classify_ode(eq)
   Out[2]: ('Liouville', 'Liouville_Integral')

   In [3]: dsolve(eq, hint='all_Integral')
   Out[3]:
   {'Liouville_Integral': Eq(C1 + C2*Integral(exp(-Integral(-5*x, x)), x) + Integral(exp(Integral(-1, _y)), (_y, f(x))), 0),
    'best': Eq(C1 + C2*Integral(exp(-Integral(-5*x, x)), x) + Integral(exp(Integral(-1, _y)), (_y, f(x))), 0),
    'best_hint': 'Liouville_Integral',
    'default': 'Liouville',
    'order': 2}

   In [4]: _['best'].doit()
   Out[4]: Eq(C1 + sqrt(10)*sqrt(pi)*C2*erfi(sqrt(10)*x/2)/10 - exp(-f(x)), 0)

   In [5]: eq = f(x).diff(x, 2) - exp(3 * f(x))

   In [6]: classify_ode(eq)
   Out[6]: ()

   In [11]: eq = f(x).diff(x, 2) + f(x) * f(x).diff(x)**2 - x**2 * f(x).diff(x)

   In [12]: classify_ode(eq)
   Out[12]: ('Liouville', 'Liouville_Integral')

   In [13]: dsolve(eq, hint='all_Integral')
   Out[13]:
   {'Liouville_Integral': Eq(C1 + C2*Integral(exp(-Integral(-x**2, x)), x) + Integral(exp(Integral(_y, _y)), (_y, f(x))), 0),
    'best': Eq(C1 + C2*Integral(exp(-Integral(-x**2, x)), x) + Integral(exp(Integral(_y, _y)), (_y, f(x))), 0),
    'best_hint': 'Liouville_Integral',
    'default': 'Liouville',
    'order': 2}

   In [14]: _['best'].doit()
   Out[14]: Eq(C1 + 3**(1/3)*C2*exp(-I*pi/3)*gamma(1/3)*lowergamma(1/3, x**3*exp_polar(I*pi)/3)/(9*gamma(4/3)) + sqrt(2)*sqrt(pi)*erfi(sqrt(2)*f(x)/2)/2, 0)

定数係数高階線形常微分方程式
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
SymPy のソルバーは 2 階以上は全部高階扱い。

.. code:: ipython

   In [1]: eq = f(x).diff(x, 5) - 17 * f(x).diff(x, 4) + 108 * f(x).diff(x, 3) -330 * f(x).diff(x, 2) + 488 * f(x).diff(x) - 280 * f(x)

   In [2]: classify_ode(eq)
   Out[2]: ('nth_linear_constant_coeff_homogeneous',)

   In [3]: dsolve(eq, hint='all_Integral')
   Out[3]:
   {'best': Eq(f(x), (C1 + C2*x + C5*exp(5*x) + (C3*sin(x) + C4*cos(x))*exp(x))*exp(2*x)),
    'best_hint': 'nth_linear_constant_coeff_homogeneous',
    'default': 'nth_linear_constant_coeff_homogeneous',
    'nth_linear_constant_coeff_homogeneous': Eq(f(x), (C1 + C2*x + C5*exp(5*x) + (C3*sin(x) + C4*cos(x))*exp(x))*exp(2*x)),
    'order': 5}

高階 Euler 常微分方程式
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
SymPy のソルバーは 2 階以上は全部高階扱い。

.. code:: ipython

   In [1]: eq = x**4 * f(x).diff(x, 4) - 2*x**3 * f(x).diff(x, 3) - x**2 * f(x).diff(x, 2) + 5 * x * f(x).diff(x) + f(x)

   In [2]: classify_ode(eq)
   Out[2]: ('nth_linear_euler_eq_homogeneous',)

   In [3]: dsolve(eq, hint='all_Integral')
   Out[3]:
   {'best': Eq(f(x), C1*x**RootOf(_x**4 - 8*_x**3 + 16*_x**2 - 4*_x + 1, 0) + C2*x**RootOf(_x**4 - 8*_x**3 + 16*_x**2 - 4*_x + 1, 1) + C3*x**RootOf(_x**4 - 8*_x**3 + 16*_x**2 - 4*_x + 1, 2) + C4*x**RootOf(_x**4 - 8*_x**3 + 16*_x**2 - 4*_x + 1, 3)),
    'best_hint': 'nth_linear_euler_eq_homogeneous',
    'default': 'nth_linear_euler_eq_homogeneous',
    'nth_linear_euler_eq_homogeneous': Eq(f(x), C1*x**RootOf(_x**4 - 8*_x**3 + 16*_x**2 - 4*_x + 1, 0) + C2*x**RootOf(_x**4 - 8*_x**3 + 16*_x**2 - 4*_x + 1, 1) + C3*x**RootOf(_x**4 - 8*_x**3 + 16*_x**2 - 4*_x + 1, 2) + C4*x**RootOf(_x**4 - 8*_x**3 + 16*_x**2 - 4*_x + 1, 3)),
    'order': 4}

.. In [151]: eq = (3*x + 5)**4 * f(x).diff(x, 4) - 2*(3*x + 5)**3 * f(x).diff(x, 3) - (3*x + 5)**2 * f(x).diff(x, 2) + 5 * (3*x + 5) * f(x).diff(x) + f(x)
..
.. In [152]: classify_ode(eq)
.. Out[152]: ()

.. 高階 exact
.. In [153]: eq = f(x).diff(x, 3) -f(x).diff(x, 2) + 5 * x * f(x).diff(x) + 5 * f(x)
..
.. In [154]: classify_ode(eq)
.. Out[154]: ()

.. In [155]: eq = f(x).diff(x, 3) - 4*(x + 2)*f(x).diff(x) - 2*f(x)
..
.. In [156]: classify_ode(eq)
.. Out[156]: ()
.. In [157]: eq = x**3 * f(x).diff(x, 3) + 3 * x**2 * f(x).diff(x, 2) + (4*x**3 - 11*x)*f(x).diff(x) + 4*x**2*f(x)
..
.. In [158]: classify_ode(eq)
.. Out[158]: ()

特殊な高階常微分方程式
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
二階で望みの形が得られないようならば、高階でもそうだ。
次の例題は Airy 関数と Bessel 関数で一般解を返して欲しいもの。
これはアウトのようだ。

.. code:: ipython

   In [1]: eq = f(x).diff(x, 3) - 4*(x + 2)*f(x).diff(x) - 2 * f(x)

   In [2]: classify_ode(eq)
   Out[2]: ()

   In [3]: eq = x**3 * f(x).diff(x, 3) + 3 * x**2 * f(x).diff(x, 2) + (4 * x**3 - 11 * x) * f(x).diff(x) + 4 * x**2 * f(x)

   In [4]: classify_ode(eq)
   Out[4]: ()

次の例題はある高次整方程式の解で一般解が表現できる。

.. code:: ipython

   In [1]: eq = f(x).diff(x, 4) - 13 * f(x).diff(x, 2) + 19 * f(x).diff(x) + 33 * f(x) - cos(2*x)

   In [2]: classify_ode(eq)
   Out[2]:
   ('nth_linear_constant_coeff_undetermined_coefficients',
    'nth_linear_constant_coeff_variation_of_parameters',
    'nth_linear_constant_coeff_variation_of_parameters_Integral')

   In [3]: dsolve(eq)
   Out[3]: Eq(f(x), C1*exp(x*RootOf(_x**4 - 13*_x**2 + 19*_x + 33, 0)) + C2*exp(x*RootOf(_x**4 - 13*_x**2 + 19*_x + 33, 1)) + C3*exp(x*RootOf(_x**4 - 13*_x**2 +19*_x + 33, 2)) + C4*exp(x*RootOf(_x**4 - 13*_x**2 + 19*_x + 33, 3)) + 38*sin(2*x)/11645 + 101*cos(2*x)/11645)

こちらは完全にダメだ。

.. code:: ipython

   In [1]: eq = 7 * f(x).diff(x) * f(x).diff(x, 3) - 11 * f(x).diff(x, 2)**2
   In [1]: classify_ode(eq)

   Out[2]: ()

連立常微分方程式
----------------------------------------------------------------------
何となく動作が不安定であるように見受けられる。
場合によってはバグレポートを開発陣に提出するかもしれない。

線形
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
以下の例では、次の前処理を実施済みであることを事前条件としている。

.. code:: python3

   from sympy.solvers.ode import classify_sysode
   x, y, z = symbols('x y z', function=True)

まずは定数係数の例を示す。

.. code:: ipython

   In [1]: A = Matrix([[4, -6], [1, -1]])

   In [2]: A.eigenvals()
   Out[2]: {1: 1, 2: 1}

   In [3]: X = Matrix([x(t), y(t)])

   In [4]: sys = [i for i in X.diff(t) - A*X]

   In [5]: classify_sysode(sys)
   Out[5]:
   {'eq': [-4*x(t) + 6*y(t) + Derivative(x(t), t),
     -x(t) + y(t) + Derivative(y(t), t)],
    'func': [x(t), y(t)],
    'func_coeff': {(0, y(t), 0): 6,
     (0, x(t), 0): -4,
     (1, y(t), 0): 1,
     (1, y(t), 1): 1,
     (1, x(t), 0): -1,
     (0, x(t), 1): 1,
     (0, y(t), 1): 0,
     (1, x(t), 1): 0},
    'is_linear': True,
    'no_of_equation': 2,
    'order': {x(t): 1, y(t): 1},
    'type_of_equation': 'type1'}

   In [6]: dsolve(sys)
   Out[6]: [Eq(x(t), -6*C1*exp(t) - 6*C2*exp(2*t)),
            Eq(y(t), -3*C1*exp(t) - 2*C2*exp(2*t))]

次の常微分方程式系は :code:`type_of_equation` が None とされている。
つまりタイプ不明ゆえ解けない。
こういう場合は :code:`dsolve` の呼び出しを諦めてしまってよい。

.. code:: ipython

   In [1]: sys = [x(t).diff(t, 3) + y(t), y(t).diff(t, 3) - 64 * x(t)]

   In [2]: classify_sysode(sys)
   Out[2]:
   {'eq': [y(t) + Derivative(x(t), t, t, t),
     -64*x(t) + Derivative(y(t), t, t, t)],
    'func': [x(t), y(t)],
    'func_coeff': {(0, x(t), 2): 0,
     (0, y(t), 0): 1,
     (1, y(t), 0): 0,
     (1, y(t), 1): 0,
     (1, x(t), 2): 0,
     (1, x(t), 3): 0,
     (0, x(t), 3): 1,
     (1, x(t), 1): 0,
     (1, x(t), 0): -64,
     (0, y(t), 2): 0,
     (0, x(t), 0): 0,
     (1, y(t), 3): 1,
     (0, x(t), 1): 0,
     (0, y(t), 3): 0,
     (0, y(t), 1): 0,
     (1, y(t), 2): 0},
    'is_linear': True,
    'no_of_equation': 2,
    'order': {x(t): 3, y(t): 3},
    'type_of_equation': None}

次は非定数係数の線形常微分方程式系の一例だが、解きたそうなのに解けないようだ。

.. code:: ipython

   In [1]: sys = [x(t).diff(t) - sin(t)*x(t), y(t).diff(t) - t**2 * y(t)]

   In [2]: classify_sysode(sys)
   Out[2]:
   {'eq': [-x(t)*sin(t) + Derivative(x(t), t), -t**2*y(t) + Derivative(y(t), t)],  'func': [x(t), y(t)],
    'func_coeff': {(0, y(t), 0): 0,
     (0, x(t), 0): -sin(t),
     (1, y(t), 0): -t**2,
     (1, y(t), 1): 1,
     (1, x(t), 0): 0,
     (0, x(t), 1): 1,
     (0, y(t), 1): 0,
     (1, x(t), 1): 0},
    'is_linear': True,
    'no_of_equation': 2,
    'order': {x(t): 1, y(t): 1},
    'type_of_equation': 'type6'}

   In [3]: dsolve(sys)
   ---------------------------------------------------------------------------
   ValueError                                Traceback (most recent call last)
   <ipython-input-223-094226d3d973> in <module>()
   ----> 1 dsolve(sys)

   D:\home\yojyo\devel\sympy\sympy\solvers\ode.py in dsolve(eq, func, hint, simplify, ics, xi, eta, x0, n, **kwargs)
       614             else:
       615                 solvefunc = globals()['sysode_nonlinear_%(no_of_equation)seq_order%(order)s' % match]
   --> 616             sols = solvefunc(match)
       617             return sols
       618     else:

   D:\home\yojyo\devel\sympy\sympy\solvers\ode.py in sysode_linear_2eq_order1(match_)
      6418         sol = _linear_2eq_order1_type5(x, y, t, r)
      6419     if match_['type_of_equation'] == 'type6':
   -> 6420         sol = _linear_2eq_order1_type6(x, y, t, r)
      6421     if match_['type_of_equation'] == 'type7':
      6422         sol = _linear_2eq_order1_type7(x, y, t, r)

   D:\home\yojyo\devel\sympy\sympy\solvers\ode.py in _linear_2eq_order1_type6(x, y, t, r)
      6725     if p == 1:
      6726         equ = diff(x(t),t) - r['a']*x(t) - r['b']*(s*x(t) + C1*exp(-s*Integral(r['b'] - r['d']/s, t)))
   -> 6727         hint1 = classify_ode(equ)[1]
      6728         sol1 = dsolve(equ, hint=hint1+'_Integral').rhs
      6729         sol2 = s*sol1 + C1*exp(-s*Integral(r['b'] - r['d']/s, t))

   D:\home\yojyo\devel\sympy\sympy\solvers\ode.py in classify_ode(eq, func, dict, ics, **kwargs)
       817         "work with functions of one variable, not %s" % func)
       818     if prep or func is None:
   --> 819         eq, func_ = _preprocess(eq, func)
       820         if func is None:
       821             func = func_

   D:\home\yojyo\devel\sympy\sympy\solvers\deutils.py in _preprocess(expr, func, hint)
        75         if len(funcs) != 1:
        76             raise ValueError('The function cannot be '
   ---> 77                 'automatically detected for %s.' % expr)
        78         func = funcs.pop()
        79     fvars = set(func.args)

   ValueError: The function cannot be automatically detected for nan.

次は成功例。積分もおそらく評価し切れる。

.. code:: ipython

   In [1]: A = Matrix([[exp(t), tan(t)], [-tan(t), exp(t)]]; X = Matrix([x(t), y(t)])

   In [2]: sys = [i for i in X.diff(t) - A*X]

   In [3]: classify_sysode(sys)
   Out[3]:
   {'eq': [-x(t)*exp(t) - y(t)*tan(t) + Derivative(x(t), t),
     x(t)*tan(t) - y(t)*exp(t) + Derivative(y(t), t)],
    'func': [x(t), y(t)],
    'func_coeff': {(0, y(t), 0): -tan(t),
     (0, x(t), 0): -exp(t),
     (1, y(t), 0): -exp(t),
     (1, y(t), 1): 1,
     (1, x(t), 0): tan(t),
     (0, x(t), 1): 1,
     (0, y(t), 1): 0,
     (1, x(t), 1): 0},
    'is_linear': True,
    'no_of_equation': 2,
    'order': {x(t): 1, y(t): 1},
    'type_of_equation': 'type4'}

   In [4]: dsolve(sys)
   Out[4]: [Eq(x(t), (C1*cos(Integral(tan(t), t)) + C2*sin(Integral(tan(t), t)))*exp(Integral(exp(t), t))), Eq(y(t), (-C1*sin(Integral(tan(t), t)) + C2*cos(Integral(tan(t), t)))*exp(Integral(exp(t), t)))]

次のものは解けないと言われる。
本筋とは外れるが、関数 :code:`classify_sysode` の出力にある dict オブジェクトのアイテム順はなんとかならないか。

.. code:: ipython

   In [1]: A = Matrix([[exp(t), 2, 3], [0, 2, -1], [0, 0, 1]]); X = Matrix([x(t), y(t), z(t)])

   In [2]: sys = [i for i in X.diff(t) - A*X]

   In [3]: classify_sysode(sys)
   Out[3]:
   {'eq': [-x(t)*exp(t) - 2*y(t) - 3*z(t) + Derivative(x(t), t),
     -2*y(t) + z(t) + Derivative(y(t), t),
     -z(t) + Derivative(z(t), t)],
    'func': [x(t), y(t), z(t)],
    'func_coeff': {(0, y(t), 0): -2,
     (0, z(t), 1): 0,
     (1, y(t), 0): -2,
     (1, y(t), 1): 1,
     (2, z(t), 1): 1,
     (1, z(t), 0): 1,
     (2, z(t), 0): -1,
     (0, y(t), 1): 0,
     (1, x(t), 1): 0,
     (2, y(t), 0): 0,
     (0, x(t), 0): -exp(t),
     (2, x(t), 1): 0,
     (2, y(t), 1): 0,
     (1, x(t), 0): 0,
     (0, x(t), 1): 1,
     (0, z(t), 0): -3,
     (2, x(t), 0): 0,
     (1, z(t), 1): 0},
    'is_linear': True,
    'no_of_equation': 3,
    'order': {x(t): 1, y(t): 1, z(t): 1},
    'type_of_equation': None}

非線形
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
謎のエラーが出てソルバーにたどり着けない。

.. code:: ipython

   In [1]: p, q, r, s = symbols('p q r s', function=True)

   In [2]: sys = [p(t).diff(t) - 1, q(t).diff(t) - t, r(r).diff(t), s(t).diff(t)- r(t)/(p(t) + 4*q(t)*r(t))]

   In [3]: classify_sysode(sys, funcs=[p(t), q(t), r(t), s(t)])
   ---------------------------------------------------------------------------
   KeyError                                  Traceback (most recent call last)
   <ipython-input-25-65d1e646ce2f> in <module>()
   ----> 1 classify_sysode(sys, funcs=[p(t), q(t), r(t), s(t)])

   D:\home\yojyo\devel\sympy\sympy\solvers\ode.py in classify_sysode(eq, funcs, **kwargs)
      1389                 func_dict[eq_no] = func
      1390             order[func] = max_order
   -> 1391     funcs = [func_dict[i] for i in range(len(func_dict))]
      1392     matching_hints['func'] = funcs
      1393     for func in funcs:

   D:\home\yojyo\devel\sympy\sympy\solvers\ode.py in <listcomp>(.0)
      1389                 func_dict[eq_no] = func
      1390             order[func] = max_order
   -> 1391     funcs = [func_dict[i] for i in range(len(func_dict))]
      1392     matching_hints['func'] = funcs
      1393     for func in funcs:

   KeyError: 2

次の例ではソルバーの処理中に謎のエラーが出る。

.. code:: ipython

   In [1]: u, v = symbols('u v', function=True)

   In [2]: sys = [u(t).diff(t) - 1/sqrt(v(t)), v(t).diff(t) - u(t)]

   In [3]: classify_sysode(sys)
   Out[3]:
   {'eq': [Derivative(u(t), t) - 1/sqrt(v(t)), -u(t) + Derivative(v(t), t)],
    'func': [u(t), v(t)],
    'func_coeff': {(1, v(t), 1): 1,
     (0, u(t), 1): 1,
     (0, v(t), 1): 0,
     (1, u(t), 1): 0,
     (0, u(t), 0): 0,
     (1, v(t), 0): 0,
     (0, v(t), 0): 0,
     (1, u(t), 0): -1},
    'is_linear': False,
    'no_of_equation': 2,
    'order': {u(t): 1, v(t): 1},
    'type_of_equation': 'type3'}

   In [4]: dsolve(sys)
   ---------------------------------------------------------------------------
   TypeError                                 Traceback (most recent call last)
   <ipython-input-30-094226d3d973> in <module>()
   ----> 1 dsolve(sys)

   D:\home\yojyo\devel\sympy\sympy\solvers\ode.py in dsolve(eq, func, hint, simplify, ics, xi, eta, x0, n, **kwargs)
       615             else:
       616                 solvefunc = globals()['sysode_nonlinear_%(no_of_equation)seq_order%(order)s' % match]
   --> 617             sols = solvefunc(match)
       618             return sols
       619     else:

   D:\home\yojyo\devel\sympy\sympy\solvers\ode.py in sysode_nonlinear_2eq_order1(match_)
      7772         sol = _nonlinear_2eq_order1_type2(x, y, t, eq)
      7773     elif match_['type_of_equation'] == 'type3':
   -> 7774         sol = _nonlinear_2eq_order1_type3(x, y, t, eq)
      7775     elif match_['type_of_equation'] == 'type4':
      7776         sol = _nonlinear_2eq_order1_type4(x, y, t, eq)

   D:\home\yojyo\devel\sympy\sympy\solvers\ode.py in _nonlinear_2eq_order1_type3(x, y, t, eq)
      7894     G = r2[g].subs(x(t),u).subs(y(t),v)
      7895     sol2r = dsolve(Eq(diff(v(u),u), G.subs(v,v(u))/F.subs(v,v(u))))
   -> 7896     for sol2s in sol2r:
      7897         sol1 = solve(Integral(1/F.subs(v, sol2s.rhs), u).doit() - t - C2, u)
      7898     sol = []

   TypeError: 'Equality' object is not iterable

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
