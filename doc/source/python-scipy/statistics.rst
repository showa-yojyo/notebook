======================================================================
確率と統計
======================================================================

本稿では SciPy_ の確率と統計の機能を見ていこう。

.. contents::

基本統計量
======================================================================

以下の説明では ``x`` を何らかの統計データを表現する shape が一次元の
``np.array`` 型インスタンスとする。また、各代表値・散布度を計算するのに十分の個数
の要素を含むものとする。

モジュール ``scipy.stats`` の機能に頼らずとも NumPy_ の機能で計算可能な統計量が
多いようだ。

最大値
----------------------------------------------------------------------

統計データ ``x`` の最大値を得るには以下のいずれかを用いればよい。

* ``x.max()`` の戻り値。
* ``np.max(x)`` の戻り値。
* ``n, (smin, smax), sm, sv, ss, sk = scipy.stats.describe(x)`` として ``smax``
  を採る。

最小値
----------------------------------------------------------------------

統計データ ``x`` の最小値を得るには以下のいずれかを用いればよい。最大値と同様。

* ``x.min()`` の戻り値。
* ``np.min(x)`` の戻り値。
* ``n, (smin, smax), sm, sv, ss, sk = scipy.stats.describe(x)`` として ``smin``
  を採る。

平均値
----------------------------------------------------------------------

統計データ ``x`` の平均値を得るには以下のいずれかを用いればよい。

* ``x.mean()`` の戻り値。
* ``np.mean(x)`` の戻り値。
* ``n, (smin, smax), sm, sv, ss, sk = scipy.stats.describe(x)`` として ``sm`` を
  採る。

中央値
----------------------------------------------------------------------

統計データ ``x`` の中央値を得るには ``np.median(x)`` の戻り値を用いる。

最頻値
----------------------------------------------------------------------

統計データ ``x`` の最頻値を得るには以下のようにする。``vals`` と ``counts`` が
最頻値と出現回数をそれぞれ表す。

>>> from scipy import stats
>>> vals, counts = stats.mode(x)

百分位数
----------------------------------------------------------------------

統計データ ``x`` の百分位数を得るには次のようにする。

* ``np.percentile(x, q)`` の戻り値。ただし ``q`` は 0 から 100 までの数。

  * ``q = 0`` ならば最小値が得られる。
  * ``q = 100`` ならば最大値が得られる。
  * ``q = 50`` ならば中央値が得られる。

SciPy にも同等の機能はあるのだが、NumPy が提供する上述の関数の仕様を推奨してい
る。

分散
----------------------------------------------------------------------

統計データ ``x`` の分散を得るには以下のいずれかを用いればよい。

* ``x.var()`` の戻り値。
* ``np.var(x)`` の戻り値。
* ``n, (smin, smax), sm, sv, ss, sk = scipy.stats.describe(x)`` として ``sv`` を
  採る。

分散といえば ``N`` で割るのか ``N - 1`` で割るのかという問題がつきまとうが、
NumPy の ``var`` はキーワード引数 ``ddof`` を明示的に与えれば biased でも
unbiased でも求まる。デフォルトでは ``ddof=0`` なので biased であり、例えば
``x.var(ddof=1)`` として呼び出せば unbiased な分散が得られる。一方
``scipy.stats.describe`` のほうは unbiased な分散を返す。

標準偏差
----------------------------------------------------------------------

統計データ ``x`` の標準偏差を得るには以下のいずれかを用いればよい。分散と同様。
NumPy のキーワード引数 ``ddof`` に関する事情も同様。

* ``x.std()`` の戻り値。
* ``np.std(x)`` の戻り値。
* ``n, (smin, smax), sm, sv, ss, sk = scipy.stats.describe(x)`` として分散
  ``sv`` から平方根をとって標準偏差を計算する。

範囲幅
----------------------------------------------------------------------

統計データ ``x`` の範囲幅を得るには以下のいずれかを用いればよい。

* ``np.ptp(x)`` の戻り値。
* 以下の手順で得る。

  #. 先述の手法で ``x`` の最大値と最小値を求める。
  #. 両者の差を取り、この値が範囲幅となる。

歪度
----------------------------------------------------------------------

統計データ ``x`` の歪度を得るには以下の手順で得る。

* ``scipy.stats.skew(x)`` の戻り値。
* ``n, (smin, smax), sm, sv, ss, sk = scipy.stats.describe(x)`` として ``ss`` を
  採る。

尖度
----------------------------------------------------------------------

統計データ ``x`` の尖度を得るには以下の手順で得る。歪度と同様。

* ``scipy.stats.kurtosis(x)`` の戻り値。
* ``n, (smin, smax), sm, sv, ss, sk = scipy.stats.describe(x)`` として ``sk`` を
  採る。

確率分布
======================================================================

各種確率分布用の機能はモジュール ``scipy.stats`` 配下に大量に用意されている。ま
ずは `リファレンス <http://docs.scipy.org/doc/scipy/reference/stats.html>`_ から
distribution とかで検索すると色々とわかる。

代表的な確率分布を気の向くままいくつか記す。

.. csv-table::
   :delim: |
   :header-rows: 1
   :widths: auto

   分布型 | 名称 | オブジェクト
   ``rv_discrete``|一様分布|``scipy.stats.randint``
   ``rv_discrete``|Bernoulli 分布|``scipy.stats.bernoulli``
   ``rv_discrete``|二項分布|``scipy.stats.binom``
   ``rv_discrete``|Poisson 分布|``scipy.stats.poisson``
   ``rv_continuous``|一様分布|``scipy.stats.uniform``
   ``rv_continuous``|指数分布|``scipy.stats.expon``
   ``rv_continuous``|正規分布|``scipy.stats.norm``
   ``rv_continuous``| :math:`\chi^2` 分布|``scipy.stats.chi2``
   ``rv_continuous``| :math:`F` 分布|``scipy.stats.f``
   ``rv_continuous``| :math:`t` 分布|``scipy.stats.t``

各種確率分布オブジェクトを利用する場合は次のような手順でコードを組むことになる。

#. 分布の種類に対応するオブジェクトを生成する。以下の説明ではオブジェクトの変数
   名を ``X`` とする。
#. 目的に応じて ``X`` のメソッドを呼び出す。

   * 平均値、分散、歪度、尖度の計算は ``mean, var, skew, kurt =
     X.stats(moments='mvsk')`` でする。
   * 離散型分布の確率質量関数（以下、確率関数と略す）は ``X.pmf(x)`` を利用す
     る。
   * 連続型分布の確率密度関数 （以下、密度関数と略す）は ``X.pdf(x)`` を利用す
     る。これはあまり使わないだろう。
   * 累積分布関数（以下、分布関数と略す）は ``X.cdf(x)`` を利用する。面積が確率
     を表すというアレだ。
   * 逆に cdf の値から対応する確率変数の値を得るには ``X.ppf(p)`` を利用する。引
     数は 0 から 1 までの値とする。
   * ある確率変数から正の無限大までの確率を得るには ``X.sf(x)`` を用いる。
   * 反対に、そのような確率の値から対応する確率変数の値を得るには ``X.isf(p)``
     を用いる。
   * 確率分布の中央付近における確率の値から対応する区間を得るには
     ``X.interval(p)`` を用いる。両側検定のときに有用だ。
   * 乱数を生成するには ``X.rvs()`` を利用する。

暗号のようなメソッド名が多いのだが、コンソールで実際に何度もタイプしていると体が
覚えてくれる。

例：サイコロ
----------------------------------------------------------------------

各面が等しい確率で出るサイコロを ``scipy.stats.randint`` で表現する。最初は
Python 標準の ``range()`` のように引数を指定する。

メソッド ``stats()`` はデフォルトならばこれは期待値（平均値）と分散を返す。バラ
バラにそれらを呼び出すよりも効率が良いのだろう。

メソッド ``pmf()`` は確率関数だ。この例では :math:`{P(X = i)}` を順次計算してい
る。どの目も 1/6 の確率であることが確認できる。

メソッド ``cdf()`` は分布関数だ。この例では意味はないが :math:`{P(X \le i)}` を順次
計算している。

.. code:: ipython

   In [1]: from scipy.stats import randint

   In [2]: X = randint(1, 7)

   In [3]: X.stats()
   Out[3]: (array(3.5), array(2.9166666666666665))

   In [4]: X.expect(), X.dev()
   Out[4]: (3.5, 2.9166666666666665)

   In [5]: [X.pmf(i) for i in range(1, 7)]
   Out[5]:
   [0.16666666666666666,
    0.16666666666666666,
    0.16666666666666666,
    0.16666666666666666,
    0.16666666666666666,
    0.16666666666666666]

   In [6]: [X.cdf(i) for i in range(1, 7)]
   Out[6]:
   [0.16666666666666666,
    0.33333333333333331,
    0.5,
    0.66666666666666663,
    0.83333333333333337,
    1.0]

例：標準正規分布
----------------------------------------------------------------------

``scipy.stats.norm(0, 1)`` で正規分布 :math:`{N(0, 1)}` を表す。なお ``norm()``
はデフォルトで正規分布を返すようなので、引数を明示的に指定しなくてよい。

次の例では最初に標準正規分布に従う確率変数 ``X`` を定義する。次に ``stats()`` メ
ソッドで期待値と分散を出力し、:math:`{E[X] = 1}` および :math:`{V(X) = 1}` であ
ることを確認する。

``pdf()`` メソッドで :math:`x = -4, -3, ..., 3, 4` における密度関数の値（グラフ
の値ということになる）をそれぞれ出力する。少なくともこの範囲では密度関数が偶関数
であることがわかる。

最後に ``cdf()`` 関数で分布関数の値 :math:`{P(X \lt x)}` を出力する。

.. code:: ipython

   In [1]: from scipy.stats import norm

   In [2]: X = norm(0, 1)

   In [3]: X.stats('mv')
   Out[3]: (array(0.0), array(1.0))

   In [4]: [f'{X.pdf(x):.4f}' for x in range(-4, 5)]
   Out[4]:
   ['0.0001',
    '0.0044',
    '0.0540',
    '0.2420',
    '0.3989',
    '0.2420',
    '0.0540',
    '0.0044',
    '0.0001']

   In [5]: [f'{X.cdf(x):.4f}' for x in range(-4, 5)]
   Out[5]:
   ['0.0000',
    '0.0013',
    '0.0228',
    '0.1587',
    '0.5000',
    '0.8413',
    '0.9772',
    '0.9987',
    '1.0000']

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
