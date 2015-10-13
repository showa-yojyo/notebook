======================================================================
Getting Started
======================================================================
初心者をなるべく速く SciPy_ を理解させ、かつ生産的にさせることを目的とするページ。

.. contents::

What are NumPy, SciPy, matplotlib, ...?
======================================================================
* NumPy_ の配列型は数値に関する作業に対して便利。
* SciPy_ は科学的な作業に必要な routines を含む。
  例を挙げると次のようなものがある。

  * 数値積分
  * 微分方程式のソルバー
  * 最適化
  * 疎行列

* Matplotlib_ は高品質はプロットを生産する。数値モデルを図示するのに便利。
* IPython_ はインタラクティブな作業を容易にする。

How to work with SciPy
======================================================================
* 一番普通のやり方は、IPython_ を利用すること。
  これでコマンドを入力し、スクリプトを走らせる。
* スクリプトを書くには、はどんなテキストエディターを用いてもよい。
* <Some of the packages such as Python(x,y) mentioned in *Installing the SciPy Stack*
  also offer an integrated scientific development environment>
  読み違えていなければ、他のページで列挙されている SciPy Stack の構成要素は次のパッケージ群を指す。

  * Python_: 言語自身も構成要素である。
  * NumPy_: 数値計算の土台をなすパッケージ。:doc:`/python-numpy/index`
  * SciPy_: 当パッケージ。
  * Matplotlib_: プロットパッケージ。
  * IPython_: インターフェイス。環境と言ったほうが伝わる。:doc:`/python-ipython`
  * Pandas_: データ構造パッケージ。
  * SymPy_: 計算機数学・計算機代数パッケージ。:doc:`/python-sympy/index`
  * Nose_: 単体テストに便利なパッケージ。:doc:`/python-nose`

* NumPy_ も SciPy_ もプロット機能を提供しない。
  プロットパッケージとしては Matplotlib_ が最も普通に利用されている。

.. todo::

   * Pandas_ とやらを試す。

Learning to work with SciPy
======================================================================
* Python の全般に関するの学習は、公式サイトの Python チュートリアルが素晴らしい。
* Python での数値計算に関して

  * 各種ツールに関する理解を得る方法のひとつは、次に挙げるオンラインリソースを当たることだ。

    * http://scipy-lectures.github.io/index.html
    * http://docs.scipy.org/doc/scipy/reference/tutorial/index.html

  * それに加えて、書籍が多数あるので活用すること。
    Google で ``SciPy scientific python`` 等のキーワードで検索するとよい。

An example session
----------------------------------------------------------------------
* IPython_ 環境上での操作例を記した文章。
  Bessel 関数の最大値の計算とプロット出力を行う例にいつの間にか書き換えられている？
* **SciPy Stack** をインストール済みであることを事前条件としている。

An example script
----------------------------------------------------------------------
前述の操作をスクリプトでやったらどうなるかを記した文章。

* モジュール ``argparse`` を利用してコマンドライン引数を実装している。
* 関数 ``np.linspace`` が等間隔に値を並べる配列を生成するものであることが読み取れる。
  明らかに使い勝手が良い。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
