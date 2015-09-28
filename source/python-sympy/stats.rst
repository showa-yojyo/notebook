======================================================================
確率統計
======================================================================
確率統計機能のモジュールである ``sympy.stats`` を調べてみよう。

.. contents:: ノート目次

.. note::

   本文中のすべての IPython セッション中のサンプルコードで、
   以下のインポートおよび出力書式設定が済んでいるものとする。

   .. code-block:: python3

      init_printing(use_unicode=False, pretty_print=False)

確率変数
======================================================================
``from sympy.stats import *`` を実行すると、クラスというよりは関数がインポートされる。
確率変数生成関数と統計的関数の 2 種類に分類して見ていくと効率が良さそうだ。
ここに記すいくつかの関数については、演習のコーナーにて実際に動作を確かめる。

確率変数生成関数
----------------------------------------------------------------------
まずは確率変数生成関数を表に示す。

.. csv-table::
   :header: 関数, 確率空間, 説明
   :delim: :

   ``Bernoulli``:``SingleFinitePSpace``:
   ``Binomial``:``SingleFinitePSpace``:
   ``Coin``:``SingleFinitePSpace``:コイントスをモデル化した確率変数。
   ``Die``:``SingleFinitePSpace``:偏りのないサイコロをモデル化した確率変数。
   ``DiscreteUniform``:``SingleFinitePSpace``:
   ``FiniteRV``:``SingleFinitePSpace``:有限確率変数を密度を表現する ``dict`` オブジェクトから生成する。
   ``Hypergeometric``:``SingleFinitePSpace``:
   ``Rademacher``:``SingleFinitePSpace``:
   ``Arcsin``:``SingleContinuousPSpace``:
   ``Benini``:``SingleContinuousPSpace``:
   ``Beta``:``SingleContinuousPSpace``:
   ``BetaPrime``:``SingleContinuousPSpace``:
   ``Cauchy``:``SingleContinuousPSpace``:
   ``Chi``:``SingleContinuousPSpace``:
   ``ChiNoncentral``:``SingleContinuousPSpace``:
   ``ChiSquared``:``SingleContinuousPSpace``:
   ``Dagum``:``SingleContinuousPSpace``:
   ``Erlang``:``SingleContinuousPSpace``:
   ``Exponential``:``SingleContinuousPSpace``:
   ``FDistribution``:``SingleContinuousPSpace``:
   ``FisherZ``:``SingleContinuousPSpace``:
   ``Frechet``:``SingleContinuousPSpace``:
   ``Gamma``:``SingleContinuousPSpace``:
   ``GammaInverse``:``SingleContinuousPSpace``:
   ``Kumaraswamy``:``SingleContinuousPSpace``:
   ``Laplace``:``SingleContinuousPSpace``:
   ``Logistic``:``SingleContinuousPSpace``:
   ``LogNormal``:``SingleContinuousPSpace``:
   ``Maxwell``:``SingleContinuousPSpace``:
   ``Nakagami``:``SingleContinuousPSpace``:
   ``Normal``:``SingleContinuousPSpace``:
   ``Pareto``:``SingleContinuousPSpace``:
   ``QuadraticU``:``SingleContinuousPSpace``:
   ``RaisedCosine``:``SingleContinuousPSpace``:
   ``Rayleigh``:``SingleContinuousPSpace``:
   ``StudentT``:``SingleContinuousPSpace``:
   ``Triangular``:``SingleContinuousPSpace``:
   ``Uniform``:``SingleContinuousPSpace``:
   ``UniformSum``:``SingleContinuousPSpace``:
   ``VonMises``:``SingleContinuousPSpace``:
   ``Weibull``:``SingleContinuousPSpace``:
   ``WignerSemicircle``:``SingleContinuousPSpace``:
   ``Geometric``:``SingleDiscretePSpace``:
   ``Poisson``:``SingleDiscretePSpace``:

確率空間クラスについては後述する。

統計的関数
----------------------------------------------------------------------
すべての確率変数生成関数の戻り値は ``RandomSymbol`` というクラスのオブジェクトである。
ここでは ``X``, ``Y`` などを ``RandomSymbol`` オブジェクトまたはそれから構成される式とする。
このオブジェクトの利用法は、そのメソッドを呼び出すというよりは、
次に示す各種確率統計的関数の引数として用いる。

.. csv-table::
   :header: 関数, 説明, 別名
   :delim: :

   ``probability``:``X`` に関するある条件が真となる確率を求める。:``P``
   ``expectation``:``X`` に関するある式の期待値を求める。:``E``
   ``density``:``X`` の確率密度を求める。:
   ``where``:``X`` に関するある条件が真である domain を返す。:
   ``given``:``X`` の条件付き確率空間を生成する。:
   ``pspace``:``X`` の土台となる確率空間を返す。:
   ``cdf``:``X`` の累積分布関数を求める。:
   ``sample``:``sample_iter`` の非 iterator 版。:
   ``sample_iter``:``X`` から標本値をランダムに列挙する。:
   ``sampling_density``:``sample`` の密度版。:
   ``independent``:``dependent`` の否定を返す。:
   ``dependent``:``X`` と ``Y`` が独立かどうかを返す。:
   ``moment``:``X`` の `n` 次モーメントを求める。:
   ``variance``:``X`` の分散を求める。:
   ``standard_deviation``:``X`` の標準偏差を求める。:``std``
   ``covariance``:``X`` と ``Y`` の確率変数の共分散を求める。:
   ``correlation``:``X`` と ``Y`` の確率変数の相関係数を求める。:
   ``cmoment``:``X`` の `n` 次中心モーメントを求める。:
   ``smoment``:``X`` の `n` 次標準化モーメントを求める。:
   ``skewness``:``X`` の歪度を求める。:

クラス
======================================================================
ユーザーがクラスを直にアクセスすることはどうやらまれなようだが、
理解を深めるには、これらの表に出てこないクラス群を調べるのもよいだろう。

確率分布モデルクラス
----------------------------------------------------------------------
確率分布モデルを表現するクラスのごく簡単なクラス図を次に記す。
これらの確率分布クラスは、前述の各種同じ名前からなる確率変数生成関数によってオブジェクト化され、
それから、分布に対応する確率空間クラスのオブジェクトを生成する。

.. code-block:: text

   ContinuousDistribution
       SingleContinuousDistribution
           ArcsinDistribution
           BeniniDistribution
           BetaDistribution
           BetaPrimeDistribution
           CauchyDistribution
           ChiDistribution
           ChiNoncentralDistribution
           ChiSquaredDistribution
           ContinuousDistributionHandmade
           DagumDistribution
           ExponentialDistribution
           FDistributionDistribution
           FisherZDistribution
           FrechetDistribution
           GammaDistribution
           GammaInverseDistribution
           KumaraswamyDistribution
           LaplaceDistribution
           LogisticDistribution
           LogNormalDistribution
           MaxwellDistribution
           NakagamiDistribution
           NormalDistribution
           ParetoDistribution
           QuadraticUDistribution
           RaisedCosineDistribution
           RayleighDistribution
           StudentTDistribution
           TriangularDistribution
           UniformDistribution
           UniformSumDistribution
           VonMisesDistribution
           WeibullDistribution
           WignerSemicircleDistribution

   SingleDiscreteDistribution
       PoissonDistribution
       GeometricDistribution

   SingleFiniteDistribution
       BernoulliDistribution
       BinomialDistribution
       DieDistribution
       DiscreteUniformDistribution
       FiniteDistributionHandmade
       HypergeometricDistribution
       RademacherDistribution

ここにあるほとんどすべてのクラスは、次のクラスを共通基底クラスとしている。

``Basic``
    SymPy の主要クラスに共通する基底クラスであり、いまさら説明はしない。

``NamedArgsMixin``
    当モジュールで定義された補助クラスであり、
    オブジェクトに対して演算子 ``[]`` で属性値にアクセスすることができるようにするものだ。

大量にある分布モデルクラスは、それらの基底クラスによって次の 3 系統に分類できることがわかる。

``SingleContinuousDistribution``
  連続分布。

  * 定義域は ``Interval(-oo, oo)`` すなわち実数である。派生クラスでは事情が異なるかもしれない。
  * オブジェクトに対する丸括弧呼び出しでメソッド ``pdf`` を呼び出す。
  * メソッドとして ``pdf, ``cdf``, ``sample``, ``expectation`` がある。
  * デバッグ用途だと思うが静的メソッド ``check`` がある。

``SingleDiscreteDistribution``
  離散分布。

  * 定義域は ``S.Integers`` すなわち整数である。
  * あとは ``SingleContinuousDistribution`` で記した各項目と同じ。

``SingleFiniteDistribution``
  有限分布。これだけ毛色が異なる。

  * オブジェクトに対する丸括弧呼び出しでメソッド ``pdf`` を呼び出す。
  * メソッドとして ``pdf`` がある。
  * 辞書オブジェクトのような振る舞いをするようだ。

定義域クラス
----------------------------------------------------------------------
ここではある確率密度関数の定義域を domain と呼ぶものと解釈する。

クラス ``RandomDomain`` を基底クラスとする継承関係を図に示したいが、
複雑なダイヤモンド型継承を多用しているので、アスキーアートでは厳しいものがある。
素朴な表でごまかす。

.. csv-table::
   :header: クラス, 直接基底クラス
   :delim: :

   ``RandomDomain``:``Basic``
   ``SingleDomain``:``RandomDomain``
   ``ProductDomain``:``RandomDomain``
   ``ContinuousDomain``:``RandomDomain``
   ``ConditionalDomain``:``RandomDomain``
   ``FiniteDomain``:``RandomDomain``
   ``SingleDiscreteDomain``:``SingleDomain``
   ``SingleContinuousDomain``:``ContinuousDomain``, ``SingleDomain``
   ``SingleFiniteDomain``:``FiniteDomain``
   ``ProductContinuousDomain``:``ProductDomain``, ``ContinuousDomain``
   ``ProductFiniteDomain``:``ProductDomain``, ``FiniteDomain``
   ``ConditionalContinuousDomain``:``ContinuousDomain``, ``ConditionalDomain``
   ``ConditionalFiniteDomain``:``ConditionalDomain``, ``ProductFiniteDomain``

クラス ``RandomDomain``
  ある確率密度関数の定義域を表現するクラスのための基底クラス。

  * プロパティー ``self.symbols``
  * プロパティー ``self.set``
  * 演算子 ``in`` をオブジェクトに対して適用できることになっている。
  * メソッド ``integrate(expr)`` を各派生クラスが実装する。
    この戻り値が何らかの確率密度関数を示すようになる。

確率空間クラス
----------------------------------------------------------------------
クラス ``PSpace`` を基底クラスとする継承関係を図に示したいが、
こちらも少々のダイヤモンド継承関係があるので表でごまかす。

.. csv-table::
   :header: クラス, 直接基底クラス
   :delim: :

   ``PSpace``:``Basic``
   ``SinglePSpace``:``PSpace``
   ``ProductPSpace``:``PSpace``
   ``ContinuousPSpace``:``PSpace``
   ``FinitePSpace``:``PSpace``
   ``SingleDiscretePSpace``:``PSpace``
   ``SingleContinuousPSpace``:``SinglePSpace``, ``ContinuousPSpace``
   ``SingleFinitePSpace``:``SinglePSpace``, ``FinitePSpace``
   ``ProductContinuousPSpace``:``ProductPSpace``, ``ContinuousPSpace``
   ``ProductFinitePSpace``:``ProductPSpace``, ``FinitePSpace``

クラス ``PSpace``
  確率空間を表現するクラス。

  * プロパティーとして ``domain``, ``density``, ``values``, ``symbols`` がある。
  * メソッドとして ``compute_density``, ``integrate``, ``probability``, ``sample``, ``where`` がある。

  ユーザーはこれらには直接触れずに、先述の統計的関数によって間接的に利用する。

クラス ``RandomSymbol``
----------------------------------------------------------------------
クラス ``RandomSymbol`` は確率空間クラスのメソッド ``values`` 系の戻り値の型として利用されている。
このオブジェクトを関数 ``P``, ``E`` の引数として指定する。

このオブジェクトはユーザーが直接生成するというよりは、
前述の確率変数生成関数の戻り値として得られる。

演習
======================================================================
次の文書からいくつか例題を拝借した。

* `Probability and Statistics <http://reference.wolfram.com/language/guide/ProbabilityAndStatistics.html>`_
* `Descriptive Statistics <http://reference.wolfram.com/language/guide/DescriptiveStatistics.html>`_

確率変数生成関数に ``name`` を指定するのが存外面倒なので、
以下、特に問題がなければ ``X`` で通す。

関数 ``probability`` で確率を評価する
----------------------------------------------------------------------
短い別名 ``P`` が付いているので、対話型コードでは主にこちらを採用する。

.. code-block:: ipython

   In [1]: X = Normal('X', mean=0, std=1)

   In [2]: simplify(P(X < 3))
   Out[2]: erf(3*sqrt(2)/2)/2 + 1/2

* [1] ``Normal`` の各引数はデフォルト引数として定義して欲しいという気がする。

.. code-block:: ipython

   In [1]: X = Poisson('X', symbols('m', positive=True))

   In [2]: P(X <= 3)
   ---------------------------------------------------------------------------
   NotImplementedError                       Traceback (most recent call last)
   <ipython-input-44-251995f355a4> in <module>()
   ----> 1 P(X <= 3)

   D:\home\yojyo\devel\sympy\sympy\stats\rv.py in probability(condition, given_condition, numsamples, evaluate, **kwargs)
       619
       620     # Otherwise pass work off to the ProbabilitySpace
   --> 621     result = pspace(condition).probability(condition, **kwargs)
       622     if evaluate and hasattr(result, 'doit'):
       623         return result.doit()

   D:\home\yojyo\devel\sympy\sympy\stats\rv.py in probability(self, condition)
       161
       162     def probability(self, condition):
   --> 163         raise NotImplementedError()
       164
       165     def integrate(self, expr):

   NotImplementedError:

* [1][2] どうも ``Poisson`` は動作しにくい傾向がある。

.. code-block:: ipython

   In [1]: X = Normal('X', 0, 1)

   In [2]: P((X - 1)**2 <= 3*X)
   Out[2]: -erf(sqrt(2)*(-sqrt(21)/2 + 5/2)/2)/2 + erf(sqrt(2)*(sqrt(21)/2 + 5/2)/2)/2

.. code-block:: ipython

   In [1]: X = Die('X', 3)

   In [2]: P(Or(X**2 > 3, abs(X) < 1))
   Out[2]: 2/3

次の例は数値計算になってしまっているが、真の値は :math:`\frac{1}{e}` だ。

.. code-block:: ipython

   In [1]: X = Laplace('X', 0, 1/2)

   In [2]: P(X**2 > 1, X > Rational(1, 2))
   Out[2]: 0.367879441171442

関数 ``expectation`` で期待値または平均値を評価する
----------------------------------------------------------------------
正式な関数名は ``expectation`` であるが、略名 ``E`` が与えられている。
SymPy では自然対数の底にもこの名前が付いているので注意。
冒頭に述べたインポート文でこれが上書きされる。

.. code-block:: ipython

   In [1]: X = Normal('X', 0, 1)

   In [2]: E(2*X + 3)
   Out[2]: 3

.. code-block:: ipython

   In [1]: X = Poisson('X', symbols('m', positive=True))

   In [2]: E(X**2 + 7*X + 8)
   Out[2]: m*(m + 1) + 7*m + 8

.. code-block:: ipython

   In [1]: X = DiscreteUniform('X', symbols('a, b, c, d'))

   In [2]: E(X)
   Out[2]: a/4 + b/4 + c/4 + d/4

確率密度関数を評価する
----------------------------------------------------------------------
確率密度関数は下のように ``pspace`` オブジェクトを経由しないとアクセスできないのか。

.. code-block:: ipython

   In [1]: X = Normal('X', 0, 1)

   In [2]: X.pspace.pdf
   Out[2]: sqrt(2)*exp(-X**2/2)/(2*sqrt(pi))

余裕があればプロットする。

累積分布関数を評価する
----------------------------------------------------------------------
累積分布関数を得るにはフリー関数 ``cdf`` を用いる。

.. code-block:: ipython

   In [1]: cdf(Weibull('X', 2, 5), 4)
   Out[1]: Lambda(_z, Piecewise((1 - exp(-_z**5/32), _z >= 0), (0, True)))

   In [2]: cdf(Normal('X', 0, 1))(0.2).evalf()
   Out[2]: 0.579259709439103

標本点を抽出する
----------------------------------------------------------------------
分布から標本点を抽出すると、毎回結果が異なる。

.. code-block:: ipython

   In [1]: X = Normal('X', 0, 1)

   In [2]: [i for i in sample_iter(X, numsamples=10)]
   Out[2]: [-1.04146627871984, 0.363794003745111, -1.13748652670554, 1.048567943992, -0.479638133723148, 1.29475387658596, -1.15722394615277, 1.57550171698866, -0.545623114068184, -1.52095054404692]

関数 ``moment`` でモーメントを評価する
----------------------------------------------------------------------
ここでは 2 次のモーメントを計算する。

.. code-block:: ipython

   In [1]: moment(DiscreteUniform('X', symbols('x1:4')), 2)
   Out[1]: x1**2/3 + x2**2/3 + x3**2/3

   In [2]: simplify(moment(Normal('X', symbols('mu'), symbols('sigma', positive=True)), 2))
   Out[2]: mu**2 + sigma**2

分散と標準偏差を評価する
----------------------------------------------------------------------
関数 ``variance`` は ``E(X - E(X)**2)`` と同じ値を計算する。
実装が ``cmoment`` を利用していることによる。

関数 ``standard_deviation`` は単に ``variance`` の正の平方根を返す。
短い別名 ``std`` が宣言されている。

数値計算の例を示す。

.. code-block:: ipython

   In [1]: X = DiscreteUniform('X', [1.21, 3.4, 2, 4.66, 1.5, 5.61, 7.22])

   In [2]: variance(X)
   Out[2]: 4.42390612244898

   In [3]: std(X)
   Out[3]: 2.10330837550013

関数 ``covariance`` で共分散を評価する
----------------------------------------------------------------------
あまりやることがない。

.. code-block:: ipython

   In [1]: X, Y = DiscreteUniform('X', symbols('a b')), DiscreteUniform('Y', symbols('x y'))

   In [2]: covariance(X, Y)
   Out[2]: (-a/2 + b/2)*(-x/2 + y/2)/4 + (-a/2 + b/2)*(x/2 - y/2)/4 + (a/2 - b/2)*(-x/2 + y/2)/4 + (a/2 - b/2)*(x/2 - y/2)/4

関数 ``correlation`` で相関を評価する
----------------------------------------------------------------------
これもあまりやることがない。

.. code-block:: ipython

   In [1]: X, Y = DiscreteUniform('X', symbols('a b')), DiscreteUniform('Y', symbols('x y'))

   In [2]: correlation(X, Y)
   Out[2]: ((-a/2 + b/2)*(-x/2 + y/2)/4 + (-a/2 + b/2)*(x/2 - y/2)/4 + (a/2 - b/2)*(-x/2 + y/2)/4 + (a/2 - b/2)*(x/2 - y/2)/4)/(sqrt((-a/2 + b/2)**2/2 + (a/2 - b/2)**2/2)*sqrt((-x/2 + y/2)**2/2 + (x/2 - y/2)**2/2))

関数 ``cmoment`` で中央モーメントを評価する
----------------------------------------------------------------------
色々な確率分布の 2 次の中央モーメントを評価しよう。

.. code-block:: ipython

   In [1]: cmoment(DiscreteUniform('X', symbols('x1:4')), 2)
   Out[1]: (-x1/3 - x2/3 + 2*x3/3)**2/3 + (-x1/3 + 2*x2/3 - x3/3)**2/3 + (2*x1/3- x2/3 - x3/3)**2/3

   In [2]: simplify(cmoment(Gamma('X', symbols('alpha', positive=True), symbols('beta', positive=True)), 2))
   Out[2]: alpha*beta**2

   In [3]: cmoment(Normal('X', symbols('mu'), symbols('sigma', positive=True)), 2)
   Out[3]: sigma**2

関数 ``smoment`` で標準化モーメントを評価する
----------------------------------------------------------------------
関数 ``smoment`` は `n` 次の中央モーメントを標準偏差の `n` 乗で割った値を評価する。
歪度や尖度を評価する関数の実装にはこれを利用する。

この関数を直接利用する例は見当たらない。

関数 ``skewness`` で歪度を評価する
----------------------------------------------------------------------
関数 ``skewness`` は 3 次の ``smoment`` を評価する。
この指標は例えば戻り値の符号でグラフの裾野が広いほうがわかる。

.. code-block:: ipython

   In [1]: skewness(DiscreteUniform('X', symbols('a b c')))
   Out[1]: ((-a/3 - b/3 + 2*c/3)**3/3 + (-a/3 + 2*b/3 - c/3)**3/3 + (2*a/3 - b/3- c/3)**3/3)/((-a/3 - b/3 + 2*c/3)**2/3 + (-a/3 + 2*b/3 - c/3)**2/3 + (2*a/3 - b/3 - c/3)**2/3)**(3/2)

   In [2]: skewness(ChiSquared('X', 10))
   Out[2]: 2*sqrt(5)/5

   In [3]: skewness(Exponential('X', symbols('mu', positive=True)))
   Out[3]: 2

   In [4]: skewness(Normal('X', 0, 1))
   Out[4]: 0

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
