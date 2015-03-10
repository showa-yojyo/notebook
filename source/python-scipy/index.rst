======================================================================
SciPy 利用ノート
======================================================================

特に目的も定めずに SciPy_ を利用してみよう。
何か便利なものが見つかるかもしれない。

.. toctree::
   :maxdepth: 5

   setup
   practice
   nonlinear-equations
   linear-equations
   eigenvalues
   interpolate
   integrate
   ode
   statistics
   least-squares
   spatial

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
* :doc:`/python-numpy/index`
* :doc:`/python-matplotlib`
* :doc:`/python-nose`

.. include:: /_include/scipy-refs.txt
