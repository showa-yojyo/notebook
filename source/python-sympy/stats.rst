======================================================================
確率統計
======================================================================
確率統計機能のモジュールである ``sympy.stats`` を調べてみよう。

.. contents:: ノート目次

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

.. todo:: ひたすら確率計算をする。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
