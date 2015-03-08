======================================================================
Cookbook
======================================================================
よくあるタスクのレシピ集のページのようだ。導入レベルのものからまったく高度なものまで幅広く取り揃っている。

.. contents::

Scipy Central
======================================================================
レシピの検索および投稿は http://scipy-central.org/ でできるようだ。

NumPy / SciPy
======================================================================
* NumPy arrays: tips and tricks:

  * BuildingArrays は NumPy の基本中の基本である array インスタンスの
    作り方について説明している。コードを一通り手で打って実行して結果を見るべし。

    * ``dtype`` の結果が異なるかもしれない。
    * bool-array で array の要素群にアクセスできるのは初耳。
    * 多次元スライスに早く慣れること。
    * ``linspace``, ``mgrid``, ``ogrid``, ``zeros``, ``ones`` が便利なことがある。

  * Indexing: 必読。内容が一部後述の ViewsVsCopies とかぶる。
  * Multiplying multiple arguments: 組み込み関数 ``reduce`` を利用した ``mdot`` の実装例等。

* Linear Algebra:

  * Rank and nullspace: 行列の階数を二種類のトレランスを指定して計算する例。

* Interpolation:

  * Interpolation: 指定点列を通過するスプライン曲線を得る例を説明。

    * モジュール ``scipy.signal`` にあるスプライン補間曲線 ``cspline1d`` を用いる。入力点列は等間隔である必要がある。
    * モジュール ``scipy.ndimage`` にある ``spline_filter``, ``map_coordinates`` を用いる。入力点列は等間隔である必要がある。

      * サンプルコードの ``np.ogrid`` と ``np.mgrid`` の用例に注目したい。手際よく *(x, y)* を生成している。

    * モジュール ``scipy.interpolate`` にある ``splprep``, ``splev`` を用いる。
      別ページ :doc:`/python-scipy/interpolate` を参照。

  * Radial Basis Functions: *n* 次元の散布データから放射基底関数を用いての補間。

* Optimization and fitting techniques: 専門外なのでわからない。

  * Optimization: 前から思っていることだが、この英単語、日本語で何と表現すれば適切になるのだろうか。

    * ``scipy.optimize.fmin(func, x0)``: 関数 ``func`` の最小値を変数 ``x0`` から求める。
    * ``scipy.optimize.fsolve(func, x0)``: 関数 ``func`` の根を変数 ``x0`` から求める。
    * ``scipy.optimize.fminbound(func, x1, x2)``: 関数 ``func`` の最小値を区間内から求める。
    * 最大値が欲しい場合は ``-func`` を与えればよい。

  * Optimization with fit: 謎のモジュール ``enthought.chaco.wx`` を用いる例。
  * Fitting Data: パッと見、読んだほうがよさそうだ。
  * Linear Regression: ``scipy.polyval``, ``scipy.polyfit`` を用いた回帰直線の作成及びプロットの例。

* Ordinary differential equations: 微分方程式のレシピなのだが、私の数学知識を遥かに超えているので飛ばす。

  * Zombie Apocalypse ODE Modeling: ゾンビって言われても困る。
  * A coupled spring-mass system: 微分方程式を解く例に、
    ばねと重りのペア 2 つを摩擦のある床の上に置いて引っ張る状況を出している。

* Root finding

  * Spherical Bessel Zeros: ``scipy.optimize.brentq`` で「明らかに効率的でない」何かを行うサンプル。
  * Intersection of functions: ``scipy.optimize.fsolve`` で 2 曲線の交点が求められる。

* Data rebinning: 日本語で rebin はどう表現すればよいのかわからない。ヒストグラムのビンの取り方を変えるような。
* Histograms: 2 次元ヒストグラム作図デモ。関数 ``np.histogram2d`` が決定的。
* Convex Hull: 2 次元点列の凸包を自力で計算、プロットするレシピ。

  * 関数 ``area_of_triangle`` を見て気づいた。ベクトルの長さを ``numpy.linalg.norm`` で得られる。

* Minimum Point of a Convex Hull: 凸包の最小点を無限ループに陥ることなく求めるレシピ。
* Smoothing a signal: デジタル信号データの平滑化のレシピか。

  * 関数 ``numpy.convolve`` を利用する。
  * 図の Smoothing a noisy signal のグラフで効果が一目瞭然。

* Butterworth Bandpass Filter: ``scipy.signal.butter``, ``scipy.signal.lfilter`` 用例あり。
* Multithreading: <numpy code often releases the GIL while it is calculating> だと。
* KDTree: 別ページ :doc:`/python-scipy/spatial` を参照。
* Brownian Motion: 2 次元ブラウン運動のプロットのデモ。
* Correlated Random Samples:

  * メソッド ``scipy.stats.norm.rvs`` で乱数を生成するサンプル。
  * 冒頭の注記によると関数 ``numpy.random.multivariate_normal`` が同じタスクをこなせる。

* Large Markov Chains: マルコフ連鎖の定常分布を計算するデモ。べき乗法という iterative method を用いる。
* Watershed algorithm: 画像処理ネタ。
* Linear Classification: Fisher の線形判別法。パターン認識とか機械学習の専門家向け。

Advanced topics
======================================================================
* ViewsVsCopies: NumPy 配列の view と copy に関する考察。

  * ビューには slice view と dtype view の 2 種類がある。

    * 普通、ビューと言えば slice のほうを指す。既存の配列オブジェクトの部分を操作する。そしてオリジナルを更新することもできる。
    * メソッド ``view`` を用いるビューのほうが dtype view である。こちらは slice view ほど便利でない。

  * fancy indexing がビューを返さない理由は、一般にはそれが slice で表せないから。従って（元の配列の部分の）コピーを返す。
  * fancy indexing が左辺値である場合、ビューでもコピーでもなく ``__setitem__`` の呼び出しである。

Compiling Extensions
======================================================================
* Compiling Extensions on Windows:

  * MinGW 環境で拡張モジュールをコンパイルする手順を説明するレシピだ。私は読まない。

Scientific Scripts
======================================================================
* Theoretical Ecology: 専門家ではないので理解していない。食物連鎖のシミュレーションか？
* Schrödinger's equation: 一次元の波動方程式を FDTD 法で解くサンプル。SciPy というより NumPy で実現している。

Input Output
======================================================================
ここにあるレシピがほとんど使わなそうだ。あるとすれば下に挙げるものか。

* input/output: NumPy 配列オブジェクトをファイルに入出力する方法のレシピ。

  * アスキー形式

    * NumPy/SciPy: ``numpy.savetxt``, ``numpy.genfromtext``
    * Matplotlib: ``pylab.save``, ``pylab.load``

  * バイナリー形式

    * NumPy: ``numpy.save``, ``numpy.savez``, ``numpy.load``
    * SciPy: ``scipy.io.numpyio.fwrite``, ``scipy.io.numpyio.fread``

      * ``scipy.io.npfile`` は使い勝手が良さそうにも関わらず、どういうわけか deprecated だそうだ。

Graphics
======================================================================
* Matplotlib cookbook: 当然要チェック。中を見るとさらにレシピがある。
* Python Imaging Library: NumPy 配列を PIL_ でイメージ化するコードが掲載。多分使わない。
* Mat3d: OpenGL バックエンドを使った立体プロットとあるので、個人的には触ってみたい。
* Line Integral Convolution: 2 次元ベクトル場をイメージ化する技法があるらしい。その説明とイメージ例。ゴッホの絵みたい。
* VTK volume rendering: 3 次元配列のボリュームレンダリングについて。気になる。
* Old Matplotlib recipes: これは :doc:`/python-matplotlib` で改めて採り上げてみたい。

Using NumPy With Other Languages (Advanced)
======================================================================
個人的には Python 内で実現可能なことにだけ興味があるので、このノートでは深く立ち入らない。

Scientific GUIs
======================================================================
wxPython と TraitsUI の例を挙げている。個人的には PyQt の例が作成できるのならば読んでみたい。

.. include:: /_include/scipy-refs.txt
