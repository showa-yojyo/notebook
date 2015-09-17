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

   .. code-block:: python3

      init_printing(use_unicode=False, pretty_print=False)

基本機能
======================================================================
ここに記す関数は isympy シェルがデフォルトで実行するインポート ``from sympy import *`` だけで利用可能だ。

SymPy で常微分方程式を解くには、関数 ``dsolve`` を用いる。
簡単なケースではこれ一本で事足りる。
何か凝ったことをする場合に、その他の関数やデータを併用するという方針でよさそうだ。

関数 ``dsolve(eq, ...)``
  常微分方程式系を解く。

  方程式を一個解くときには、引数 ``eq`` には何か導関数を含むような数式オブジェクトを指定する。
  方程式を複数個解くときには、同様に数式オブジェクトの ``list`` オブジェクトを指定する。
  ソルバーは各方程式が 0 と等しい条件を求める。

  * キーワード引数 ``func=None`` は ``eq`` がどの一変数関数に関する微分方程式なのかを指示する。
    方程式を複数個解くときには、やはり ``list`` の形式をとる。
    普通はソルバーが自動検出するため、指定しない。

  * キーワード引数 ``hint='default'`` ではソルバーに微分方程式のタイプについてヒントを教える。
    このヒントによって方程式の解法を調整することになる。

    方程式を一個解くときには、与え得るパラメーターは次のとおり（すべて文字列だが、引用符を省略する）。

    * ``default``: 後述の関数 ``classify_ode(eq, ...)`` にて記す。

    * ``all``: 全部の解法候補を適用する。
      この場合はソルバーの戻り値がキーと値をタイプ名と解からなる ``dict`` オブジェクトになる。
      タイプ名は文字列で、解は ``Equality`` オブジェクトだと思われる。
      それに加えて、ベスト解や階数等の副次的な情報も併せて含む。

    * ``all_Integral``: ``all`` と同様に振る舞うが、
      もしタイプ ``xxx`` とタイプ ``xxx_Integral`` が候補にある場合、
      前者を省略するという点が異なる。
      後者の解法は結果オブジェクト内に ``Integral`` オブジェクトが未評価のまま残るが、
      計算処理が速いという特徴がある。

    * ``best``: 全部の候補を試して、もっとも解が単純なものを返す。

    * あるいはユーザーが別途関数 ``classify_ode(eq, ...)`` を呼び出して得たタイプのうちの一つ。

  * キーワード引数 ``simplify=True`` はソルバー内部が関数 ``odesimp`` を呼び出すかどうかを指定する。

  * キーワード引数 ``ics=None`` は境界条件を ``dict`` オブジェクトで指定できる。

    * キーの例 ``func(x0)``, ``func(x).diff(x).subs(x, x2)``
    * 利用可能になる条件は一階常微分方程式のべき級数？

  * キーワード引数 ``xi=None`` および ``eta=None`` は無限小関数。
    後述する関数 ``infinitesimals`` の項で解説する。

  * キーワード引数 ``x0=0`` は微分方程式のべき級数解をどの点周りに評価するかを指定する。
  * キーワード引数 ``n=6`` はべき級数の指数をどこまで上げてよいかを指定する。

関数 ``classify_ode(eq, ...)``
  常微分方程式 ``eq == 0`` のタイプを返す。
  微分方程式の教科書と考え方は同じで、
  ソルバーは微分方程式を解く手法を何種類かに名前をつけて分類している。
  この関数は与えられた微分方程式を解くのに相応しいであろう手法の名前を列挙するものだ。

  * キーワード引数 ``func=None`` および ``ics=None`` はソルバー関数と同じ。
  * キーワード引数 ``dict=False`` はソルバー関数が内々に利用するもの。

  * 戻り値は文字列からなる ``tuple`` オブジェクトである。

    * ソルバーが方程式を解くのにデフォルトで採用するのは、この最初のタイプである。
      特定の方法で解かせたいならば、関数 ``dsolve`` の ``hint`` として、
      この候補のいずれかのタイプを指定する。

    * タイプは基本的には「このタイプとみなせば、方程式を解きやすいだろう」という順序で列挙されている。

  * サポートするタイプは ``allhints`` という ``tuple`` オブジェクトが知っている。
    手許の環境では 34 個ある。

関数 ``checkodesol(ode, sol, ...)``
  これは微分方程式の解を求めた後に、それを検算するのに用いる。
  オブジェクト ``sol`` をソルバーに渡したものと同じ ``ode`` に代入して、
  ゼロになることを見たい。

  * 戻り値は 2 要素の ``tuple`` である。

    * [0]: 代入結果がゼロならば ``True`` であり、そうでなければ ``False`` である。
    * [1]: [0] が ``True`` ならば ``0`` である（逆は必ずしも成り立たない）。
      それ以外は代入結果が何になったのかを表現する値が入る。

  * この関数の呼び出しがなかなか返って来ないときは、
    間違いなく ``simplify`` がキツイためだろう。

関数 ``homogeneous_order(eq, *symbols)``
  同次方程式 ``eq == 0`` の次数を返す。

  * 非同次であれば ``None`` を返す。
  * シンボル関数も ``eq`` になれるが、関数のすべての変数がシンボルである必要がある。
    なおかつ、数式中のその関数の変数が ``*symbols`` にマッチしている必要がある。

下回りの機能
======================================================================
ここからはモジュール ``sympy.solvers.ode`` からの明示的なインポートを必要とする機能を記す。

関数 ``infinitesimals(eq, ...)``
  一階常微分方程式 :math:`y' = f(x, y)` に対して、
  次の条件をみたすような点変換 :math:`\xi(x, y)` と :math:`\eta(x, y)` を返す：

  これらの点変換が次のリー群について、
  元の :math:`f` を用いて変換先の各変数に関する微分方程式 :math:`(y^*)'=f(x^*, y^*)` が成り立つ。

  .. math::
     :nowrap:

     \begin{eqnarray*}
     x^* &=& X(x, y;\varepsilon) = x + \varepsilon \xi(x, y),\\
     y^* &=& Y(x, y;\varepsilon) = y + \varepsilon \eta(x, y)
     \end{eqnarray*}

  * 戻り値は ``dict`` の ``list`` の型をとる。
    内側の ``dict`` は、キーが点変換関数オブジェクトで、
    値が ``Function`` 系オブジェクトまたは定数である。

  * キーワード引数 ``hint`` を用いて、点変換関数の計算方法のヒューリスティックを調整できるもよう。

関数 ``checkinfsol(eq, infinitesimals, ...)``
  この関数は上述の関数 ``infinitesimals`` の結果を検証するのに用いられる。

  * 引数 ``infinitesimals`` の型は（というか値は）先ほどの関数の戻り値と同じようにする。
  * 戻り値は ``list`` オブジェクトである。
    この要素は各点変換のペアに対応するブーリアン値と検算結果の値とのペアである。
    検算結果とは、次の偏微分に点変換関数を代入して評価した値である。

    .. math::
       :nowrap:

       \frac{\partial \eta}{\partial x} + \left(\frac{\partial \eta}{\partial y}
        - \frac{\partial \xi}{\partial x}\right)\frac{dy}{dx}
        - \frac{\partial \xi}{\partial y} \left(\frac{dy}{dx}\right)^{2}
        - \xi\frac{\partial h}{\partial x} - \eta\frac{\partial h}{\partial y}

    すなわち、妥当な関数を与えればリストが含む要素はすべて ``(True, 0)`` となる。

関数 ``odesimp(eq, func, order, constants, hint)``
  常微分方程式の単純化処理のための関数。

  * 関数 ``dsolve`` が本関数を呼び出すので、
    これを単体で利用するケースというのは一般ユーザーにはまれだということだ。

関数 ``constant_renumber(expr, symbolname, startnumber, endnumber)``
  式に含まれる任意定数の番号付けを変更する関数。

  式 ``expr`` 中にはいくつかの ``Symbol`` オブジェクトがあるという前提。
  そのオブジェクト名が ``symbolname`` に末尾から数字のくっついたもので、
  さらにその数字が範囲 `[startnumber, endnumber)` にあれば、リネームの対象になる。
  新たに 1 から範囲の長さまでの連番が振られる。

関数 ``constantsimp(expr, constants)``
  式に含まれる任意定数に対する単純化処理のための関数。

  * ``C1 + C2`` → ``C1``
  * ``C1 * C2`` → ``C1``
  * ``exp(C1)`` → ``C1``
  * etc.

関数 ``ode_sol_simplicity(sol, func, trysolving=True)``
  解の簡単さを示す数値を返す関数。
  例えば ``ode_sol_simplicity(A, f) < ode_sol_simplicity(B, f)`` なる ``A`` と ``B`` については、
  ``A`` のほうが ``B`` よりも解が簡単であると解釈する。

  * ``-2`` や ``-1`` が戻ってくる場合は「解けている」または「解けていないが、解ける」を意味する。
  * 何か正の整数が戻ってくる場合は「解けない」か「与えられた ``func`` について解けない」を意味する。
    この値は解の文字列的な長さである。長い方程式のほうが難しそうだからこうしたのか。
  * ``oo`` が戻ってくる場合、解が未評価の ``Integral`` オブジェクトを含むことを意味する。

  * キーワード引数 ``trysolving`` は、
    ユーザーが既に解が解けないことを知っているときに利用できる。
    値 ``False`` を指示することで、計算を省略する。

    * ``dsolve`` の ``simplify=False`` と連動している。

特化型ソルバー
======================================================================
SymPy のドキュメントが関数名と微分方程式の数式 (LaTeX) を併記していて素晴らしいので、
カタログのように参照すると目当てのタイプのソルバーが提供されているかどうかはすぐにわかるだろう。

ここでは関数名だけを列挙するに留める。
対応するヒント名を併記するとメモ代わりになるか。

* ``ode_1st_exact``
* ``ode_1st_homogeneous_coeff_subs_dep_div_indep``
* ``ode_1st_homogeneous_coeff_subs_indep_div_dep``
* ``ode_1st_linear``
* ``ode_almost_linear``
* ``ode_Bernoulli``
* ``ode_linear_coefficients``
* ``ode_Liouville``
* ``ode_nth_linear_constant_coeff_homogeneous``
* ``ode_nth_linear_constant_coeff_undetermined_coefficients``
* ``ode_nth_linear_constant_coeff_variation_of_parameters``
* ``ode_Riccati_special_minus2``
* ``ode_separable``
* ``ode_separable_reduced``

連立常微分方程式
======================================================================
連立常微分方程式を ``dsolve`` に評価させると、最初に関数 ``classify_sysode`` を呼ぶ。
これで方程式のタイプを判定して、特化型のソルバーに処理を委ねる。

このタイプ判定が下の図のように入れ子になっていて、
末端のソルバーでは結局 ``dsolve`` を単一の方程式に対して適用することを繰り返す。

.. code-block:: text

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

積分だけで解が求まる常微分方程式
----------------------------------------------------------------------
次のデモは単に ``integrate`` するだけで解が得られる常微分方程式を与えるものだ。
SymPy のソルバーは一階線形常微分方程式の特別に単純な場合として処理する。

.. code-block:: ipython

   In [1]: eq = f(x).diff(x) - x**2 * sin(x) + sqrt(1 + x**2)

   In [2]: dsolve(eq, hint='all_Integral')
   Out[2]:
   {'1st_exact_Integral': Eq(Integral(1, (_y, f(x))) + Integral(-x**2*sin(x) + sqrt(x**2 + 1), x), C1),
    '1st_linear_Integral': Eq(f(x), (C1 + Integral((x**2*sin(x) - sqrt(x**2 + 1))*exp(Integral(0, x)), x))*exp(-Integral(0, x))),
    'Bernoulli_Integral': Eq(f(x), (C1 - Integral((-x**2*sin(x) + sqrt(x**2 + 1))*exp(Integral(0, x)), x))*exp(-Integral(0, x))),
    'best': Eq(f(x), (C1 + Integral((x**2*sin(x) - sqrt(x**2 + 1))*exp(Integral(0,x)), x))*exp(-Integral(0, x))),
    'best_hint': '1st_linear_Integral',
    'default': 'separable',
    'nth_linear_constant_coeff_variation_of_parameters_Integral': Eq(f(x), C1 - Integral(-x**2*sin(x) + sqrt(x**2 + 1), x)),
    'order': 1,
    'separable_Integral': Eq(Integral(1, (_y, f(x))), C1 + Integral(x**2*sin(x) - sqrt(x**2 + 1), x))}

   In [3]: _['best'].doit()
   Out[3]: Eq(f(x), C1 - x**2*cos(x) - x*sqrt(x**2 + 1)/2 + 2*x*sin(x) + 2*cos(x)- asinh(x)/2)

変数分離形常微分方程式
----------------------------------------------------------------------
次のデモは、変数分離形のつもりで常微分方程式を解いたところ、
むしろ Bernoulli 型のほうが解きやすい？と言われたものだ。

.. code-block:: ipython

   In [1]: eq = f(x).diff(x) - (x ** 2 * f(x) ** 2)/sqrt(3 - x**2)

   In [2]: classify_ode(eq)
   Out[2]:
   ('separable',
    '1st_exact',
    'Bernoulli',
    '1st_power_series',
    'lie_group',
    'separable_Integral',
    '1st_exact_Integral',
    'Bernoulli_Integral')

   In [3]: dsolve(eq, hint='all_Integral')
   Out[3]:
   {'1st_exact_Integral': Eq(Integral(_y**(-2), (_y, f(x))) + Integral(-x**2/sqrt(-x**2 + 3), x), C1),
    'Bernoulli_Integral': Eq(f(x), exp(-Integral(0, x))/(C1 + Integral(-x**2*exp(-Integral(0, x))/sqrt(-x**2 + 3), x))),
    'best': Eq(f(x), exp(-Integral(0, x))/(C1 + Integral(-x**2*exp(-Integral(0, x))/sqrt(-x**2 + 3), x))),
    'best_hint': 'Bernoulli_Integral',
    'default': 'separable',
    'order': 1,
    'separable_Integral': Eq(Integral(_y**(-2), (_y, f(x))), C1 + Integral(x**2/sqrt(-x**2 + 3), x))}

   In [4]: _['best'].doit()
   Out[4]: Eq(f(x), 1/(C1 + x*sqrt(-x**2 + 3)/2 - 3*asin(sqrt(3)*x/3)/2))

変数分離形としてだけ扱われる常微分方程式を解く。

.. code-block:: ipython

   In [5]: eq = f(x).diff(x) - (x**2 * exp(f(x)))/sqrt(3 - x**2)

   In [5]: dsolve(eq, hint='all_Integral')
   Out[5]:
   {'best': Eq(Integral(exp(-_y), (_y, f(x))), C1 + Integral(x**2/sqrt(-x**2 + 3),x)),
    'best_hint': 'separable_Integral',
    'default': 'separable',
    'order': 1,
    'separable_Integral': Eq(Integral(exp(-_y), (_y, f(x))), C1 + Integral(x**2/sqrt(-x**2 + 3), x))}

   In [6]: _['best'].doit()
   Out[6]: Eq(-exp(-f(x)), C1 - x*sqrt(-x**2 + 3)/2 + 3*asin(sqrt(3)*x/3)/2)

一階同次常微分方程式
----------------------------------------------------------------------
次のデモは同次常微分方程式を解くものだ。

.. code-block:: ipython

   In [1]: eq = f(x).diff(x) + (x**2 - 3 * f(x)**2)/(x * f(x))

   In [2]: dsolve(eq, hint='all_Integral')
   Out[2]:
   {'1st_homogeneous_coeff_subs_dep_div_indep_Integral': Eq(log(x), C1 + Integral(-1/(_u1 + (-3*_u1**2 + 1)/_u1), (_u1, f(x)/x))),
    '1st_homogeneous_coeff_subs_indep_div_dep_Integral': Eq(f(x), C1*exp(Integral(3/(_u2*(_u2**2 - 2)), (_u2, x/f(x))) + Integral(-_u2/(_u2**2 - 2), (_u2, x/f(x))))),
    'Bernoulli_Integral': Eq(f(x), sqrt((C1 - 2*Integral(x*exp(2*Integral(-3/x, x)), x))*exp(-2*Integral(-3/x, x)))),
    'best': Eq(f(x), C1*exp(Integral(3/(_u2*(_u2**2 - 2)), (_u2, x/f(x))) + Integral(-_u2/(_u2**2 - 2), (_u2, x/f(x))))),
    'best_hint': '1st_homogeneous_coeff_subs_indep_div_dep_Integral',
    'default': 'Bernoulli',
    'order': 1}

   In [3]: _['best'].doit()
   Out[3]: Eq(f(x), C1*(x**2/f(x)**2 - 2)**(1/4)/(x/f(x))**(3/2))

一階線形常微分方程式
----------------------------------------------------------------------
一階線形方程式の例だ。
どのような常微分方程式のタイプとして扱っても厳しい積分が現れる。

.. code-block:: ipython

   In [1]: eq = f(x).diff(x) + x * f(x) - exp(3*x)

   In [2]: dsolve(eq, hint='all_Integral')
   Out[2]:
   {'1st_exact_Integral': Eq(Integral((x*f(x) - exp(3*x))*exp(x**2/2), x) + Integral(exp(x**2/2) - Integral(x*exp(x**2/2), x), (_y, f(x))), C1),
    '1st_linear_Integral': Eq(f(x), (C1 + Integral(exp(3*x)*exp(Integral(x, x)), x))*exp(-Integral(x, x))),
    'Bernoulli_Integral': Eq(f(x), (C1 - Integral(-exp(3*x)*exp(Integral(x, x)), x))*exp(-Integral(x, x))),
    'almost_linear_Integral': Eq(f(x), (C1 + Integral(exp(3*x)*exp(Integral(x, x)), x))*exp(-Integral(x, x))),
    'best': Eq(f(x), (C1 + Integral(exp(3*x)*exp(Integral(x, x)), x))*exp(-Integral(x, x))),
    'best_hint': '1st_linear_Integral',
    'default': '1st_exact',
    'order': 1}

Bernoulli 常微分方程式
----------------------------------------------------------------------
Bernoulli 常微分方程式を解く。
二番目のものは積分に時間が掛かるのだろうか、ついに返って来なかったので諦めた。

.. code-block:: ipython

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

   In [7]: _['best'].doit()

Riccati 常微分方程式
---------------------------------------------------------------------
ある Riccati 常微分方程式を試したところ、
ベストは ``separable_reduced`` だと判定された。
それにしては解の有理式の形がやや不自然なようだ。

.. code-block:: ipython

   In [1]: eq = f(x).diff(x) + (2/x**2) - 3 * f(x)**2

   In [2]: dsolve(eq, hint='all')
   Out[2]:
   {'Riccati_special_minus2': Eq(f(x), -(-5*I*tan(C1 + 5*I*log(x)/2) + 1)/(6*x)),  'best': Eq(f(x), (-C1*x**4 - 2/(3*x))/(C1*x**5 - 1)),
    'best_hint': 'separable_reduced',
    'default': 'Riccati_special_minus2',
    'lie_group': Eq(f(x), -(x**5*exp(5*C1) + 2/3)/(x*(x**5*exp(5*C1) - 1))),
    'order': 1,
    'separable_reduced': Eq(f(x), (-C1*x**4 - 2/(3*x))/(C1*x**5 - 1)),
    'separable_reduced_Integral': Eq(Integral(1/(_y*(3*_y + 1 - 2/_y)), (_y, x*f(x))), C1 + Integral(1/x, x))}

.. In [30]: dsolve(f(x).diff(x) - (5*x**2 - 2*f(x)**2 + 11)/(sin(f(x)) + 4*x*f(x) + 3), f(x))
.. 返って来ない

.. # 解けない
.. In [33]: dsolve(f(x) - x * f(x).diff(x) - f(x).diff(x)**2 - exp(f(x).diff(x)), f(x))

.. ----------------------------------------------------------------------
.. # アーベル方程式
.. In [34]: dsolve(f(x).diff(x) - f(x)**3 + x*f(x)**2/(x - 1), f(x))
.. Out[34]: Eq(f(x), C1 + C1*x + 2*C1*x**2 + C1*x**3*(16*C1 + 7)/6 + C1*x**4*(21*C1 + 10)/12 + C1*x**5*(C1*(104*C1 + 35) + C1*(48*C1**2 + 6*C1*(30*C1 + 1) + 227*C1 + 37) + 73*C1 + 39)/60 + O(x**6))

.. ----------------------------------------------------------------------
.. # キーニ
.. In [36]: diff(f(x).diff(x) - 5*f(x)**4 - 3*x**(-Rational(4, 3)), f(x))
.. Out[36]: -20*f(x)**3

定数係数二階線形常微分方程式
----------------------------------------------------------------------
特性方程式の解のパターン別に試す。
ソルバーが適切なタイプ判定をしていることがわかる。

.. code-block:: ipython

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
----------------------------------------------------------------------
Euler 常微分方程式のデモを示す。

.. code-block:: ipython

   In [1]: eq = x**2 * f(x).diff(x, 2) + 5 * x * f(x).diff(x) + 6 * f(x)

   In [2]: dsolve(eq, hint='all_Integral')
   Out[2]:
   {'best': Eq(f(x), (C1*sin(sqrt(2)*log(x)) + C2*cos(sqrt(2)*log(x)))/x**2),
    'best_hint': 'nth_linear_euler_eq_homogeneous',
    'default': 'nth_linear_euler_eq_homogeneous',
    'nth_linear_euler_eq_homogeneous': Eq(f(x), (C1*sin(sqrt(2)*log(x)) + C2*cos(sqrt(2)*log(x)))/x**2),
    'order': 2}

.. Legendre type...
.. In [107]: eq = (3*x + 1)**2 * f(x).diff(x, 2) + 5 * (3*x + 1) * f(x).diff(x) + 6 * f(x)
.. NotImplementedError: solve: Cannot solve (3*x + 1)**2*Derivative(f(x), x, x) + (15*x + 5)*Derivative(f(x), x) + 6*f(x)

.. eq = f(x).diff(x, 2) + log(x) * f(x).diff(x) + f(x)/x
.. NotImplementedError: solve: Cannot solve log(x)*Derivative(f(x), x) + Derivative(f(x), x, x) + f(x)/x

特殊
----------------------------------------------------------------------
ノーコメント？

.. code-block:: ipython

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

.. code-block:: ipython

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

.. In [124]: eq = f(x).diff(x, 2) - exp(5*x)*f(x)
..
.. In [125]: classify_ode(eq)
.. Out[125]: ()

二階線形非同次常微分方程式
----------------------------------------------------------------------
解けているように見えるが、ヒントを ``all`` にすると返って来ない？

.. code-block:: ipython

   In [1]: eq = x**2 * f(x).diff(x, 2) + f(x) - x**2

   In [2]: classify_ode(eq)
   Out[2]:
   ('nth_linear_euler_eq_nonhomogeneous_undetermined_coefficients',
    'nth_linear_euler_eq_nonhomogeneous_variation_of_parameters',
    'nth_linear_euler_eq_nonhomogeneous_variation_of_parameters_Integral')

   In [3]: dsolve(eq)
   Out[3]: Eq(f(x), C1*sqrt(x)*sin(sqrt(3)*log(x)/2) + C2*sqrt(x)*cos(sqrt(3)*log(x)/2) + x**2/3)

二階非線形常微分方程式
----------------------------------------------------------------------
Liouville 型は解ける。それ以外が解けない。

.. code-block:: ipython

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

   In [7]: eq = f(x).diff(x, 2) - 3 * f(x) * f(x).diff(x) - (3*f(x)**2 + 4*f(x) + 1)

   In [8]: classify_ode(eq)
   Out[8]: ()

   In [9]: eq = 7 * f(x)*f(x).diff(x, 2) - 11 * f(x).diff(x)

   In [10]: classify_ode(eq)
   Out[10]: ()

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
----------------------------------------------------------------------
SymPy のソルバーは 2 階以上は全部高階扱い。

.. code-block:: ipython

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
----------------------------------------------------------------------
SymPy のソルバーは 2 階以上は全部高階扱い。

.. code-block:: ipython

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

色々
----------------------------------------------------------------------
ノーコメント。

.. code-block:: ipython

   In [1]: eq = f(x).diff(x, 4) - 13 * f(x).diff(x, 2) + 19 * f(x).diff(x) + 33 * f(x) - cos(2*x)

   In [2]: classify_ode(eq)
   Out[2]:
   ('nth_linear_constant_coeff_undetermined_coefficients',
    'nth_linear_constant_coeff_variation_of_parameters',
    'nth_linear_constant_coeff_variation_of_parameters_Integral')

   In [3]: dsolve(eq)
   Out[3]: Eq(f(x), C1*exp(x*RootOf(_x**4 - 13*_x**2 + 19*_x + 33, 0)) + C2*exp(x*RootOf(_x**4 - 13*_x**2 + 19*_x + 33, 1)) + C3*exp(x*RootOf(_x**4 - 13*_x**2 +19*_x + 33, 2)) + C4*exp(x*RootOf(_x**4 - 13*_x**2 + 19*_x + 33, 3)) + 38*sin(2*x)/11645 + 101*cos(2*x)/11645)

.. In [164]: eq = 7 * f(x).diff(x) * f(x).diff(x, 3) - 11 * f(x).diff(x, 2)**2
.. In [166]: classify_ode(eq)
.. Out[166]: ()

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
