======================================================================
Python SciPy 利用ノート
======================================================================

.. note::

   本稿において、利用した各パッケージのバージョンは次のとおり。

   * Python_: 2.6.6
   * SciPy_: 0.10.1
   * NumPy_: 1.6.1
   * Nose_: 1.1.2

.. contents:: ノート目次

関連リンク
======================================================================
SciPy_
  SciPy 総本山ウェブサイト。
  ドキュメント、ダウンロード、コードレシピ等。

インストール
======================================================================
自分の Python_ 環境 (Windows XP) に SciPy_ をインストールする方法を記す。
単体テストが走るところまで確認できたら、インストール成功とみなす。

* <The SciPy library depends on NumPy, which provides convenient and
  fast N-dimensional array manipulation> (SciPy.org) とあるので、
  本ノートではあらかじめ NumPy_ をインストールしてあることを前提とする。

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

ドキュメントを読む
======================================================================
SciPy_ サイト内のリンクを辿っていき、次のように攻略する予定。
ドキュメントを読みながら、コードを書いてその都度走らせる、
というやり方で何となく学習した気になる。

Getting Started
----------------------------------------------------------------------
TBW

Cookbook
----------------------------------------------------------------------
TBW

SciPy Reference Guide
----------------------------------------------------------------------
TBW

コードを書く
======================================================================

.. warning::

   以下のテキストは全てがスタブだ。

SciPy Reference Guide に倣い、以降のコード片においては、
あらかじめ各種 ``import`` を次のようにしたものとする。

.. code-block:: python

   import numpy as np
   import scipy as sp
   import matplotlib as mpl
   import matplotlib.pyplot as plt

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
.. _Nose: http://somethingaboutorange.com/mrl/projects/nose/

