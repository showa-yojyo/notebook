======================================================================
Python SciPy 利用ノート
======================================================================

特に目的も定めずに SciPy_ を利用してみよう。
何か便利なものが見つかるかもしれない。

.. contents:: ノート目次

.. note::

   本稿において、利用した各パッケージのバージョンは次のとおり。

   * Python_: 2.6.6
   * SciPy_: 0.10.1
   * NumPy_: 1.6.1
   * Matplotlib_: 1.1.0
   * Nose_: 1.1.2

.. note::

   SciPy Reference Guide に倣い、以降のコード片においては、
   あらかじめ各種 ``import`` を次のようにしたものとする。
   
   .. code-block:: python
   
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

* インストールを終了したら、何はさておき
  :file:`README.txt` と :file:`INSTALL.txt` を一読すること。
  NumPy_ のときと同様、
  Nose_ が環境にあれば単体テストが実行できる。

  .. code-block:: pycon

     >>> import scipy
     >>> scipy.test()  # test('full') というのもある
     Running unit tests for scipy
     NumPy version 1.6.1
     NumPy is installed in D:\Python26\lib\site-packages\numpy
     SciPy version 0.10.1
     SciPy is installed in D:\Python26\lib\site-packages\scipy
     Python version 2.6.6 (r266:84297, Aug 24 2010, 18:46:32) [MSC v.1500 32 bit (Intel)]
     nose version 1.1.2
     略
     ----------------------------------------------------------------------
     Ran 5113 tests in 158.889s
     
     FAILED (KNOWNFAIL=12, SKIP=36, failures=2)
     <nose.result.TextTestResult run=5113 errors=0 failures=2>

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
   
     >> help(np.concatenate)
     説明文がダラダラ出力される
   
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
* KDTree: ``scipy.spatial.kdtree.KDTree`` TODO: あとで試す。

Graphics は何か色々あるが、
Matplotlib_ と PIL の ``Image`` データ作成方法しか用がない。

あとは SWIG 関連か。

SciPy Reference Guide
----------------------------------------------------------------------
.. http://docs.scipy.org/doc/scipy-0.10.1/reference/

このガイドブックのチュートリアルこそが言わば公式チュートリアル。
SciPy の機能を厳選して構成されたと思われるので、一通り読んでみたくなる。
しかし、各章かなりの分量がある。
テキストおよび画像がふんだんにあり、重い。
自分の興味のあるトピックに絞ってまずは学習を進めたい。

コードを書く
======================================================================

.. warning::

   以下のテキストは全てがスタブだ。

ヘルプ
------

SciPy のバージョンを知る
~~~~~~~~~~~~~~~~~~~~~~~~
:file:`version.py` の変数 ``version`` を参照する。

 >>> sp.version.version
 '0.10.1'

.. _Python: http://www.python.org/
.. _Numpy: http://scipy.org/NumPy/
.. _SciPy: http://www.scipy.org/
.. _Matplotlib: http://matplotlib.sourceforge.net/
.. _Nose: http://somethingaboutorange.com/mrl/projects/nose/

