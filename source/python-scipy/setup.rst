======================================================================
インストール
======================================================================
自分の Python_ 環境 (Windows XP, 7, 10) に SciPy_ をインストールする方法を記す。
単体テストが走るところまで確認できたら、インストール成功とみなす。

.. contents::

* <The SciPy library depends on NumPy, which provides convenient and
  fast N-dimensional array manipulation> (SciPy.org) とあるので、
  本ノートではあらかじめ NumPy_ をインストールしてあることを前提とする。

* 各種計算結果の出力（表示）に Matplotlib_ を多用しているので、
  そちらもインストール済みであるとする。

* SciPy_ は単体テストに Nose_ を利用している。
  NumPy_ インストール時に併せてインストールしてあるハズ。

* Anaconda_ もしくは Miniconda_ 環境ではコマンドラインから
  インストールまたはアップグレードを容易に実施できる。

  .. code-block:: console

     $ conda install scipy
     Fetching package metadata .........
     Solving package specifications: ..........

     Package plan for installation in environment D:\Miniconda3:

     The following packages will be downloaded:

         package                    |            build
         ---------------------------|-----------------
         scipy-0.18.0               |      np111py35_0        11.7 MB

     The following NEW packages will be INSTALLED:

         scipy: 0.18.0-np111py35_0

     Proceed ([y]/n)?

* Windows 環境ではインストーラーからインストールするのが吉。
  :file:`scipy-x.y.z-win32-superpack-python2.6.exe` みたいな名前のインストーラーを
  SciPy_ のサイトから検索して入手しておけばよい。

  Python 3.x 系や 64 ビット環境の場合は公式サイトではなく、
  `Python Extension Packages for Windows - Christoph Gohlke`_ を利用させてもらう。
  :file:`scipy-x.y.z.win-amd64-py3.4` のような名前のインストーラーをダウンロードすることができる。

  * インストーラー形式の場合は素直に実行する。
  * whl 形式の場合はダウンロードして pip install する。例を示す。

    .. code-block:: console

       $ pip install scipy-0.16.0-cp35-none-win_amd64.whl
       $ pip install --upgrade scipy-0.16.0-cp35-none-win_amd64.whl

* インストールを終了したら、何はさておき
  :file:`INSTALL.rst.txt` を一読すること。
  NumPy_ のときと同様、
  Nose_ が環境にあれば単体テストが実行できる。
  例によって実行時間は決して短くない。

  .. code-block:: pycon

     >>> import scipy
     >>> scipy.test()
     Running unit tests for scipy
     NumPy version 1.10.0
     NumPy relaxed strides checking option: True
     NumPy is installed in d:\python35\lib\site-packages\numpy
     SciPy version 0.16.0
     SciPy is installed in d:\python35\lib\site-packages\scipy
     Python version 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)]
     nose version 1.3.7
     d:\python35\lib\site-packages\matplotlib\__init__.py:1318: UserWarning:  This call to matplotlib.use() has no effect
     because the backend has already been chosen;
     matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
     or matplotlib.backends is imported for the first time.

       warnings.warn(_use_error_msg)
     .............
     ... more dots ...
     ----------------------------------------------------------------------
     Ran 5323 tests in 226.199s

     FAILED (KNOWNFAIL=15, SKIP=2, errors=8)

  * (0.16.0) プロットの単体テストがあるらしく、途中でウィンドウがバンバン表示される。
    自動的に閉じてくれないものがいくつかある。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
