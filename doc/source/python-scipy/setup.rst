======================================================================
インストール
======================================================================

自分の Python_ 環境 (Windows XP, 7, 10) に SciPy_ をインストールする方法を記す。
単体テストが走るところまで確認できたら、インストール成功とみなす。

* :ref:`python-pkg-proc` の方針でインストールする。:program:`conda` を使えない
  場合はかなりの確率で Gohlke ページに行くことになる。
* 各種計算結果の出力（表示）に Matplotlib_ を多用しているので、そちらもインス
  トール済みであるとする。
* SciPy_ は単体テストに Nose_ を利用している。NumPy_ インストール時に併せてイン
  ストールしてあるハズ。
* インストールを終了したら、何はさておき :file:`INSTALL.rst.txt` を一読するこ
  と。NumPy_ のときと同様、Nose_ が環境にあれば単体テストが実行できる。例によっ
  て実行時間は決して短くない。

  .. code:: pycon

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

  * (0.16.0) プロットの単体テストがあるらしく、途中でウィンドウがバンバン表示さ
    れる。自動的に閉じてくれないものがいくつかある。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
