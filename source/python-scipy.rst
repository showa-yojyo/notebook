======================================================================
SciPy 利用ノート
======================================================================

特に目的も定めずに SciPy_ を利用してみよう。
何か便利なものが見つかるかもしれない。

.. contents:: ノート目次

.. note::

   * OS

     * Windows XP Home Edition SP 3
     * Windows 7 Home Premium SP 1

   * 本稿において、利用した各パッケージのバージョンは次のとおり。

     * Python_: 2.6.6, 2.7.3, 3.4.1
     * SciPy_: 0.10.1, 0.14.0
     * NumPy_: 1.6.1, 1.6.2, 1.8.2
     * Matplotlib_: 1.1.0, 1.1.1, 1.3.1
     * Nose_: 1.1.2, 1.3.3

.. note::

   SciPy Reference Guide に倣い、以降のコード片においては、
   あらかじめ各種 ``import`` を次のようにしたものとする。

   .. code-block:: python3

      import numpy as np
      import scipy as sp
      import matplotlib as mpl
      import matplotlib.pyplot as plt

関連リンク
======================================================================
SciPy_
  SciPy 総本山ウェブサイト。
  ドキュメント、ダウンロード、コードレシピ等。

関連ノート
======================================================================
* :doc:`python-numpy`
* :doc:`python-matplotlib`
* :doc:`python-nose`

インストール
======================================================================
自分の Python_ 環境 (Windows XP) に SciPy_ をインストールする方法を記す。
単体テストが走るところまで確認できたら、インストール成功とみなす。

* <The SciPy library depends on NumPy, which provides convenient and
  fast N-dimensional array manipulation> (SciPy.org) とあるので、
  本ノートではあらかじめ NumPy_ をインストールしてあることを前提とする。

* 各種計算結果の出力（表示）に Matplotlib_ を多用しているので、
  そちらもインストール済みであるとする。

* SciPy_ は単体テストに Nose_ を利用している。
  NumPy_ インストール時に併せてインストールしてあるハズ。

* Windows 環境ではインストーラーからインストールするのが吉。
  :file:`scipy-x.y.z-win32-superpack-python2.6.exe` みたいな名前のインストーラーを
  SciPy_ のサイトから検索して入手しておけばよい。

  Python 3.x 系や 64 ビット環境の場合は公式サイトではなく、
  `Python Extension Packages for Windows - Christoph Gohlke`_ を利用させてもらう。
  :file:`scipy-x.y.z.win-amd64-py3.4` のような名前のインストーラーをダウンロードすることができる。

* インストールを終了したら、何はさておき
  :file:`README.txt` と :file:`INSTALL.txt` を一読すること。
  NumPy_ のときと同様、
  Nose_ が環境にあれば単体テストが実行できる。
  例によって実行時間は決して短くない。

  .. code-block:: pycon

     >>> import scipy
     >>> scipy.test()
     Running unit tests for scipy
     NumPy version 1.8.2
     NumPy is installed in D:\Python34\lib\site-packages\numpy
     SciPy version 0.14.0
     SciPy is installed in D:\Python34\lib\site-packages\scipy
     Python version 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 10:45:13) [MSC v.1600 64 bit (AMD64)]
     nose version 1.3.3
     ... ドットの列 ...
     ----------------------------------------------------------------------
     Ran 16418 tests in 770.217s

     OK (KNOWNFAIL=277, SKIP=1171)
     <nose.result.TextTestResult run=16418 errors=0 failures=0>
     >>>

.. warning::

   SciPy のインストールだけが目的ならば、ここから先はもう読まなくてよい。

ドキュメントを読む
======================================================================
SciPy_ サイト内のリンクを辿っていき、次のように攻略する予定。
ドキュメントを読みながら、コードを書いてその都度走らせる、
というやり方で何となく学習した気になる。

Getting Started
----------------------------------------------------------------------
.. http://www.scipy.org/Getting_Started

* <accessing numpy arrays is faster than accessing Python lists>
* ``range`` と ``np.arange`` ならば、後者のほうが圧倒的に速い。
* <Using ipython makes interactive work easy>
* <Neither scipy nor numpy provide, by default, plotting functions.
  They are just numerical tools. The recommended plotting package is matplotlib>

* 次のドキュメントがおすすめらしい。

  * http://www.scipy.org/Additional_Documentation/Astronomy_Tutorial

    リンクの PDF ファイル "Using Python for Interactive Data Analysis"
    (by Perry Greenfield and Robert Jedrzejewski)
    が言わば教科書になっている。SciPy の使い方を説明することが目的の文書ではない。
    もっと包括的な内容の本だ。

  * http://www.rexx.com/~dkuhlman/scipy_course_01.html:
    "SciPy Course Outline" (by Dave Kuhlman)

    これは NumPy, SciPy の利用法の概要を説明したテキストだ。
    PyTables と Matplotlib_ についても説明がある。
    概略なので、紹介する内容を array の取り扱い程度にとどめている。

* An Example Session 以降、IPython を使いながらの説明となる。
  フーリエ変換のグラフをプロットする例だ。
  IPython が環境になくても、コードの動作確認は工夫次第で可能だ。
  例えば次のように IDLE 上で入力していけばよい。

  .. code-block:: pycon

     >> a = np.zeros(1000)
     >> a[:100] = 1
     >> b = sp.fft(a)
     >> plt.plot(np.abs(b))
     [<matplotlib.lines.Line2D instance at 0xb7b9144c>]
     >> plt.show()

  ウィンドウが表示される。

  x 軸が [0, 1000] まで表示されていて、山がちょうど両端に位置している。
  x = 500 で切って左右の曲線を入れ替えて、x = 0 まで平行移動させれば、
  美しい絵が得られる。

  以下、plot の引数を微調整することを試みる。

  .. code-block:: pycon

     >> help(np.concatenate)

  説明文がダラダラ出力される

  .. code-block:: pycon

     >> f = np.arange(-500, 500, 1)
     >> plt.grid(True)
     >> plt.plot(f,abs(concatenate((b[500:],b[:500]))))
     [<matplotlib.lines.Line2D instance at 0xb360ca4c>]
     >> plt.show()

  ウィンドウが表示される

  タイプ量を削減できる IPython を導入したほうが便利であることは想像に難くない。

* 最後に ``import`` 文のコツについて説明している。
  内容は SciPy に限らず、他の Python パッケージ利用時についても言えることだ。

Cookbook
----------------------------------------------------------------------
.. http://www.scipy.org/Cookbook

まずは "NumPy / SciPy" を見ていく。

* BuildingArrays は NumPy の基本中の基本である array インスタンスの
  作り方について説明している。コードを一通り手で打って実行して結果を見るべし。

  * ``dtype`` の結果が異なるかもしれない。
  * bool-array で array の要素群にアクセスできるのは初耳。
  * 多次元スライスに早く慣れること。
  * ``linspace``, ``mgrid``, ``ogrid``, ``zeros``, ``ones`` が便利なことがある。
  * 組み込み関数 ``reduce`` を利用した ``mdot`` の実装例。

* Rank and nullspace: 行列の階数を二種類のトレランスを指定して計算する例。
* Interpolation: 指定点列を通過するスプライン曲線を得る例と、
  フィッティングの例を説明。

* Optimization は専門外なのでわからない。
* Linear Regression: ``scipy.stats.linregress``
* A coupled spring-mass system: 微分方程式を解く例に、
  ばねと重りのペア 2 つを摩擦のある床の上に置いて引っ張る状況を出している。

* Intersection of functions: ``scipy.optimize.fsolve`` で 2 曲線の交点が求められる。
* KDTree: ``scipy.spatial.kdtree.KDTree`` 本稿の後半を参照。

Graphics は何か色々あるが、
Matplotlib_ と PIL の ``Image`` データ作成方法しか用がない。

あとは SWIG 関連か。

SciPy Reference Guide
----------------------------------------------------------------------

http://docs.scipy.org/doc/scipy/reference/

このガイドブックのチュートリアル "SciPy Tutorial" こそが言わば公式チュートリアル。
SciPy の機能を厳選して構成されたと思われるので、一通り読んでみたくなる。
しかし、各章かなりの分量がある。
テキストおよび画像がふんだんにあり、重い。
自分の興味のあるトピックに絞ってまずは学習を進めたい。

正直な所、わからないところの方がずっと多い。

Introduction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ``help``, ``sp.info``, ``sp.source`` がヘルプ三種の神器。

  * ``info`` はキーワード引数でテキストの書式を細かくコントロールできる。

  * ``source`` はちょっと珍しい機能なので、
    初めて使う ``scipy`` 配下の関数に対して、一度は試してみる価値あり。

Basic functions in Numpy (and top-level scipy)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ``sp.isnan``, ``sp.isfinite``, ``sp.isinf`` を浮動小数点数のエラー検知に利用できる。
* array インスタンスを素早く作成するために、
  ``sp.mgrid``, ``sp.ogrid``, ``sp.r_``, ``sp.c_`` の使い方を習得する。

  * これらは相当な修練が必要そうに思える。

* ``poly1d`` で一変数多項式を定義することができる。

  * ``p.integ`` で原始関数取得。キーワード引数 ``k`` が定数項。
  * ``p.derive`` で導関数取得。
  * ``p(arraylike)`` で評価。

* ``vectorize`` 関数を使うと、スカラー引数を取りスカラー値を戻す関数 ``func`` から、
  array-like 版 ``func`` を新たに定義することができる。

* ``mod(x, y)`` vs ``x % y``
* ``fix`` は「ゼロに近い方の整数」を返す（型は float のままのようだが）。
* 角度モノを取り扱うときは ``angle``, ``unwrap`` を当たってみる。
* ``linspace`` だけでなく ``logspace`` もある。
* 関数 ``select`` は「複数版 if 文」みたいなもの。

* n の階乗は ``scipy.misc.factorial(n)`` で求まる。
  ちなみにガンマ関数で実装されている。
* n 個から k 個を選ぶ組み合わせ :math:`_n \mathrm{C} _r` は ``scipy.misc.comb(n, k)`` で求まる。

Special functions (scipy.special)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TBW

Integration (scipy.integrate)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TBW

Optimization (scipy.optimize)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TBW

Interpolation (scipy.interpolate)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TBW

Fourier Transforms (scipy.fftpack)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
まだ書きかけのようだ。

Signal Processing (scipy.signal)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
画像処理か。

Linear Algebra (scipy.linalg)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ``sci.mat`` を利用すると MATLAB 風表記で行列インスタンスを定義できる。
* 行列 ``A`` に対して、もし存在すれば逆行列は ``linalg.inv(A)`` または ``A.I`` で得られる。
* 1 次方程式 :math:`Ax = b` を ``linalg.solve(A, b)`` で解くことができる（解が存在すれば）。
* ``A`` の行列式は ``linalg.det`` で求める。
* ノルムには関数 ``linalg.norm`` を用いる。ノルムの種類を引数で指示する。
* 最小二乗法には ``linalg.lstsq`` を用いる。
* 固有値・固有ベクトル、各種分解も可能。
* 行列のテイラー展開による各種関数もサポート。

* その他いろいろ。

Sparse Eigenvalue Problems with ARPACK
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TBW

Statistics (scipy.stats)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TBW

Multi-dimensional image processing (scipy.ndimage)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ここも画像処理か。

File IO (scipy.io)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
SciPy はある種のファイルフォーマットを操作できるということがわかる。
MATLAB ファイルやら WAV ファイルやら。

Weave (scipy.weave)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Python コードの内部に C/C++ のコードを含めるためのパッケージだそうだ。
今は読む必要はない。

コードを書く
======================================================================

ヘルプ
----------------------------------------------------------------------

SciPy のバージョンを知る
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
:file:`version.py` の変数 ``version`` を参照する。

 >>> sp.version.version
 '0.14.0'

関数のヘルプを見る
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Python 組み込みの関数 ``help`` よりも、
キーワード引数 ``maxwidth`` で一行の文字数を制限することができる
``scipy.info`` のほうが見やすい可能性がある。

定義済み定数を利用する
----------------------------------------------------------------------
Python なので「定数」ではないのだが、
色々便利なものが ``scipy.constances`` にある。

* 円周率、黄金比、真空中の光速、プランク定数、地球の重力加速度、等々。
* SI 基本単位
* SI 接頭辞（キロ、メガ等）

便利なのでリンクをはっておく。
http://docs.scipy.org/doc/scipy/reference/constants.html

KDTree を使う
----------------------------------------------------------------------
空間上のある点とある点群に対して、最も近い距離にあるものを探索するには
``scipy.spatial.KDTree`` を利用するのがよい。

Reference Guide の例を一部改変したものを記す。
ある点とある点群をそれぞれ ``target``, ``points`` としてある。

.. literalinclude:: ../sample/scipy/kdtree.py
   :language: python3

実行結果。乱数を使っているので、結果は毎回異なる。

.. code-block:: text

   Target:  [ 43.83186046  54.76244808  83.13057483]
   Closest:  [40 50 80]
   Distance:  6.8676462584

.. _Python: http://www.python.org/
.. _Numpy: http://scipy.org/NumPy/
.. _SciPy: http://www.scipy.org/
.. _Matplotlib: http://matplotlib.sourceforge.net/
.. _Nose: http://somethingaboutorange.com/mrl/projects/nose/
.. _Python Extension Packages for Windows - Christoph Gohlke: http://www.lfd.uci.edu/~gohlke/pythonlibs/
