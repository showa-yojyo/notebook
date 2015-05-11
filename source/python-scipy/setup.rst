======================================================================
インストール
======================================================================

自分の Python_ 環境 (Windows XP) に SciPy_ をインストールする方法を記す。
単体テストが走るところまで確認できたら、インストール成功とみなす。

.. contents::

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

.. include:: /_include/python-refs.txt
