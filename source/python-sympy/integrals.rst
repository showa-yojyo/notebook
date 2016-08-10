======================================================================
積分
======================================================================
本節ではモジュール ``sympy.integrals`` にある積分機能を見ていく。

SymPy_ は積分変数を含む数式の定積分および不定積分（原始関数）を評価することができる。
また、各種 Laplace 変換および各種 Fourier 変換のための機能を提供している。
例えば学生は数学の宿題を片付けるのにこの機能を利用してもよい。

計算機を利用する限り、積分といえば普通は数値計算を想定するものだ。
SymPy においても、得意とする代数的な設計・実装による積分法のほかに、
数値積分法もサポートしている。本節の最後にこれらを見ていくことにする。

.. contents:: ノート目次

.. note::

   本文中のすべての IPython セッション中のサンプルコードで、
   以下のインポートおよび出力書式設定が済んでいるものとする。

   .. code-block:: python3

      init_printing(pretty_print=False)

基本事項
======================================================================
SymPy では、ある計算を実現するために、
それの即時評価版と遅延評価版の両方を提供し、
前者を後者で実装するという方式を多用している。
積分の場合、前者と後者がそれぞれ関数 :code:`integrate` とクラス Integral になる。
本節ではこれらを簡単に記す。

関数 :code:`integrate`
----------------------------------------------------------------------
積分を計算するには、関数 :code:`integrate(f, var, ...)` をもっとも採用することになる。

* :code:`integrate(f, x)` の形式で用いれば、
  被積分関数 :code:`f` の変数 :code:`x` に関する不定積分（原始関数が一つ）が得られる。

* :code:`integrate(f, (x, a, b))` の形式で用いれば、
  被積分関数 :code:`f` の指定区間における定積分が得られる。

* 引数に積分変数あるいは積分区間を列挙することにより、
  多変数関数の重積分を計算できる。

  * 積分変数も区間もどちらも指定しない場合は、
    被積分関数 :code:`f` の適当な変数に関する原始関数を返すようだ。

* ユーザーは数学公式集に掲載されている基本的な積分公式を本関数が承知していると期待してよい。

比較的わかりやすい例を示す。

.. code-block:: ipython

   In [1]: integrate(1/(x**3 + 1), x)
   Out[1]: log(x + 1)/3 - log(x**2 - x + 1)/6 + sqrt(3)*atan(2*sqrt(3)*x/3 - sqrt(3)/3)/3

   In [2]: integrate(1/(x**3 + 1), (x, 0, 1))
   Out[2]: log(2)/3 + sqrt(3)*pi/9

   In [3]: integrate(log(x) * exp(-x**2), (x, 0, oo))
   Out[3]: -sqrt(pi)*log(2)/2 - EulerGamma*sqrt(pi)/4

   In [4]: integrate(sin(x*y), (x, 0, 1), (y, 0, x))
   Out[4]: Piecewise((0, Eq(x, 0)), (2*log(x) - log(x**2)/2 - Ci(x) + EulerGamma, True))

   In [5]: integrate(sin(x*y), (y, 0, x), (x, 0, 1))
   Out[5]: -Ci(1)/2 + EulerGamma/2

* [1] 不定積分を求める。
  ちなみに検算には :code:`diff` や :code:`subs` を駆使することになる。

* [2] 同じ関数のある定積分を求める。

* [3] 定義域が無限区間になるようなある関数の定積分を求める。
  区間の端点にシンボル :code:`oo` を用いるのがコツだ。

* [4][5] 重積分を求める。

  * 積分区間を表す引数の順序を丁寧に指定する必要があることがわかる。
  * :code:`Ci` は余弦積分。

クラス Integral
----------------------------------------------------------------------
積分計算をオブジェクトにカプセル化するためのクラスに違いない。
前述の関数 :code:`integrate` が本クラスの機能をラップしているはずだ。

メソッド :code:`doit(**hints)`
  実際に積分を計算する。

メソッド :code:`as_sum(n, method='midpoint')`
  キーワード引数 :code:`method` の取りうる値が次のものなので、
  これは積分領域を矩形または台形の `n` 本の短冊の寄せ集めに近似して、
  その面積を計算するメソッドだろう。

  * :code:`left`
  * :code:`right`
  * :code:`midpoint`
  * :code:`trapezoid`

メソッド :code:`transform(x, u)`
  置換積分を行う。
  第一引数を :code:`x` と書いたが、実際は元の積分変数で表現された数式に相当する。
  これを第二引数のシンボル :code:`u` に置換する。

  高校数学のテキストから拝借したある積分を評価してみるとこうなる。

  .. code-block:: ipython

     In [1]: J = Integral(sqrt(x + 1)*(x + 2))

     In [2]: J.doit()
     Out[2]: Piecewise((2*sqrt(x + 1)*(x + 2)**2/5 - 2*sqrt(x + 1)*(x + 2)/15 - 4*sqrt(x + 1)/15, Abs(x + 2) > 1), (2*I*sqrt(-x - 1)*(x + 2)**2/5 - 2*I*sqrt(-x - 1)*(x + 2)/15 - 4*I*sqrt(-x - 1)/15, True))

     In [3]: J.transform(sqrt(x + 1), t)
     Out[3]: Integral(2*t*(t**2 + 1)*sqrt(t**2), t)

     In [4]: _.doit()
     Out[4]: 2*(t**2)**(5/2)/5 + 2*(t**2)**(3/2)/3

線積分
======================================================================
線積分を求めるには、先述のものとは異なる関数を用いる。

関数 :code:`line_integrate(field, Curve, variables)`
  線積分を求める。

  * 引数 :code:`field` が被積分関数である。ベクトル場ということだろう。
  * 引数 :code:`Curve` で積分区間となる曲線オブジェクトを指定する。
    これは平面曲線でなければならないようだ。
    このクラスについては :doc:`./geometry` で見た。

  .. code-block:: ipython

     In [1]: C = Curve([cos(t), sin(t)], (t, 0, 2 * pi))

     In [2]: line_integrate((x**2 * y + y ** 2)/2, C, [x, y])
     Out[3]: pi/2

関数変換
======================================================================
モジュール ``sympy.integrals.transforms`` には、
ある積分を用いることにより、与えられた関数から別の関数を生成するための一連の機能がある。
ここではそのうち Laplace 変換と Fourier 変換だけを見ていく。

Laplace 変換
----------------------------------------------------------------------
Laplace 変換およびその逆変換を計算する機能は、関数として提供されている。

関数 :code:`laplace_transform(f, t, s, **hints)`
  関数 :code:`f(t)` の Laplace 変換を計算して、結果を返す。

  * 引数 :code:`f` と :code:`t` は変換したい関数とその変数シンボルをそれぞれ指定する。
  * 引数 :code:`s` で得られる変換関数の変数シンボルを指定する。
  * 戻り値は :code:`(F, a, cond)` の形の tuple オブジェクト。

    * :code:`F` は変換関数そのもの。
    * :code:`a` はこの変換の収束域の境界値。
      「変数 :code:`s` の実部が値 :code:`a` を超えていれば、積分が収束する」と読み換えてかまわない。
    * :code:`cond` はさらなる収束条件。形式不明。

  * さらに :code:`noconds=True` を加えれば、戻り値は :code:`F` のみになる。

  いくつか実行例を示す。変換したい関数はよそのドキュメントから拝借した。

  .. code-block:: ipython

     In [1]: t, s = symbols('t s')

     In [2]: laplace_transform(t**4 * sin(t), t, s)
     Out[2]:
     (24*(5*s**4 - 10*s**2 + 1)/(s**10 + 5*s**8 + 10*s**6 + 10*s**4 + 5*s**2 + 1),
      0,
      True)

     In [3]: factor(_)
     Out[3]: 24*(5*s**4 - 10*s**2 + 1)/(s**2 + 1)**5

     In [4]: laplace_transform(exp(-t), t, s)
     Out[4]: (1/(s + 1), 0, True)

     In [5]: laplace_transform(t / (1 + t), t, s)
     Out[5]: (exp(s)*expint(2, s)/s, 0, True)

     In [6]: laplace_transform(log(t)**2, t, s)
     Out[6]: ((log(s)**2 + 2*EulerGamma*log(s) + EulerGamma**2 + pi**2/6)/s, 0, True)

     In [7]: laplace_transform(Heaviside(t - 1) * t, t, s)
     Out[7]: ((s + 1)*exp(-s)/s**2, 0, True)

  * [1] Laplace 変換で標準的に用いられる変数名 :code:`t` 等を有効にする。
  * [2][3][4] 小手試し。
    以降、収束条件が全部同じの例ばかりになってしまうので、
    呼び出し時に :code:`noconds=True` を与えたほうがよかった。
  * [5] :code:`expint` を含む関数が得られる。
  * [6] EulerGamma を含む関数が得られる。
  * [7] Heaviside 関数を Laplace 変換する。

関数 :code:`inverse_laplace_transform(F, s, t, plane=None, **hints)`
  関数 :code:`F(s)` の逆 Laplace 変換を計算して、結果を返す。

  * 引数 :code:`F`, :code:`s`, :code:`t` の意味は前述の関数に準ずる。
  * 引数 :code:`plane` を利用する場合は、
    呼び出し側で変換関数 :code:`F` が極を持たないような半平面を知っているときにそうする。

  いくつか実行例を示す。逆変換の対象となる関数はよそのドキュメントから拝借した。

  .. code-block:: ipython

     In [8]: inverse_laplace_transform(1 / (1 + s), s, t)
     Out[8]: exp(-t)*Heaviside(t)

     In [9]: inverse_laplace_transform(log(s)**2 / s, s, t)
     Out[9]: (6*log(t)**2 + 12*EulerGamma*log(t) - pi**2 + 6*EulerGamma**2)*Heaviside(t)/6

     In [10]: inverse_laplace_transform(s/(s**2 + 1), s, t)
     Out[10]: cos(t)*Heaviside(t)

  いちいち Heaviside 関数が現れるのが特徴だ。

Fourier 変換
----------------------------------------------------------------------
こちらも関数として提供されている。
ユニタリー周波に関する変換方式を採用している。

関数 :code:`fourier_transform(f, x, k, **hints)`
  関数 :code:`f(x)` の Fourier 変換を計算して、結果を返す。

  * 引数 :code:`f` は変換したい実変数関数。
  * 引数 :code:`x` は関数 :code:`f` の変数シンボル。
  * 引数 :code:`k` は周波数。角周波数ではない（そうだったら :code:`omega` みたいなパラメーター名になっただろう）。
  * 戻り値は計算状況によって異なる。

    * 評価が成功すれば、いつものように関数を表現する数式 :code:`F(k)` が得られる。
    * 微妙な場合、クラス FourierTransform のオブジェクトが返る。
      これは変換が未評価であることを意味する。

  * さらに :code:`noconds=False` を加えれば、
    戻り値は :code:`F` とブール値からなる tuple オブジェクトに変わる。

    ブール値の意味が文書化されていないので、後で調べたい。

  実行例を示す。

  .. code-block:: ipython

     In [1]: fourier_transform(1, x, k)
     Out[1]: 0

     In [2]: fourier_transform(x**2, x, k)
     Out[2]: 0

     In [3]: fourier_transform(exp(-3*t)*Heaviside(t), t, k)
     Out[3]: 1/(2*I*pi*k + 3)

     In [4]: fourier_transform(exp(-x**2), x, k)
     Out[4]: sqrt(pi)*exp(-pi**2*k**2)

     In [5]: fourier_transform(DiracDelta(t), t, k)
     Out[5]: 1

  * [1][2] 入力が異なるのに変換結果が同じになるのは解せない。
    おそらく DiracDelta を結果に含むはずの変換が正しく求まらない。
  * [3]-[5] こちらはよさそうだ。

関数 :code:`inverse_fourier_transform(F, k, x, **hints)`
  関数 :code:`F(k)` の逆 Fourier 変換を計算して、結果を返す。
  各引数の意味は前述の関数に準ずる。

  実行例を示す。

  .. code-block:: ipython

     In [6]: inverse_fourier_transform(1, k, x)
     Out[6]: 0

     In [7]: inverse_fourier_transform(DiracDelta(k), k, x)
     Out[7]: 1

     In [8]: inverse_fourier_transform(DiracDelta(k - a/(2*pi)), k, x)
     Out[8]: exp(I*a*x)

     In [9]: inverse_fourier_transform(1/k, k, x)
     Out[9]: InverseFourierTransform(1/k, k, x)

     In [10]: inverse_fourier_transform(exp(-k**2), k, x)
     Out[10]: sqrt(pi)*exp(-pi**2*x**2)

  * [6] 逆変換で DiracDelta が欲しい例。
  * [7][8] DiracDelta の逆変換は正しく求まる。
  * [9] このように評価し切れない場合は遅延評価版オブジェクトが返る。
  * [10] おそらく正しい。

数値積分
======================================================================
その名もモジュール ``sympy.integrals.quadrature`` に、数値積分系の関数が定義されている。
すべてが Gauss 求積法の派生アルゴリズムということになる。
まず各関数に共通する引数と戻り値の性質を説明する。

* 引数 :code:`n` は各求積法の order である。
* 引数 :code:`n_digits` は求積の精度、有効桁数を指定する。
* 戻り値は長さ 2 の tuple オブジェクトであり、
  どちらの要素も長さ :code:`n` の list オブジェクトだ。
  その中身も共通して小数点以下が :code:`n_digits` 桁の float 値だ。

  * ガウス点。各短冊の位置のようなものを想像するとよい。
  * 重み。各短冊の太さのようなもの。

次に各関数について固有の事情を記す。

関数 :code:`gauss_legendre(n, n_digits)`
  Gauss-Legendre 求積法を評価する。
  単に Gauss 求積といえばこれを指す。

関数 :code:`gauss_laguerre(n, n_digits)`
  Gauss-Laguerre 求積法を評価する。

関数 :code:`gauss_gen_laguerre(n, alpha, n_digits)`
  Gauss-Laguerre 求積法の一般化版を評価する。

  * 引数 :code:`alpha` は一般化されていないほうの求積法の重み関数に対して乗じる :code:`x ** alpha` の指数を指定する。

関数 :code:`gauss_hermite(n, n_digits)`
  Gauss-Hermite 求積法を評価する。

関数 :code:`gauss_chebyshev_t(n, n_digits)`
  Gauss-Chebyshev 求積法を、第一種多項式について評価する。

関数 :code:`gauss_chebyshev_u(n, n_digits)`
  Gauss-Chebyshev 求積法を、第二種多項式について評価する。

関数 :code:`gauss_jacobi(n, alpha, beta, n_digits)`
  Gauss-Jacobi 求積法を評価する。

  * 引数 :code:`alpha` は Jacobi 多項式第 1 項 :code:`(1 - x)` の指数。
  * 引数 :code:`beta` は Jacobi 多項式第 2 項 :code:`(1 + x)` の指数。
  * これらの指数は -1 より大きい必要がある。

最後に、関数 :code:`gauss_legendre` だけデモを示す。

.. code-block:: ipython

   In [1]: integrate(exp(-x**2/2), (x, -1, 1))
   Out[1]: sqrt(2)*sqrt(pi)*erf(sqrt(2)/2)

   In [2]: _.evalf()
   Out[2]: 1.71124878378430

   In [3]: from sympy.integrals.quadrature import gauss_legendre

   In [4]: nodes, weights = gauss_legendre(5, 8)

   In [5]: nodes
   Out[5]: [-0.90617985, -0.53846931, 0, 0.53846931, 0.90617985]

   In [6]: weights
   Out[6]: [0.23692689, 0.47862867, 0.56888889, 0.47862867, 0.23692689]

   In [7]: sum((exp(-node**2/2) * weight for node, weight in zip(nodes, weights)))
   Out[7]: 1.7112494

* [1][2] まずは汎用の :code:`integrate` による定積分を計算し、近似値を見ておく。
  これをガウス求積による数値計算で得るのがこのデモの目的だ。

* [4] オーダー 5 でガウス点と重みを計算する。
* [5][6] それぞれ有効精度が 8 桁であることがわかる。
* [7] これらと Python の組み込み関数を用いて、
  簡単な算術計算で定積分の数値計算を実現できた。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
