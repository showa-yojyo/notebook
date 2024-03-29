======================================================================
SciPy 利用ノート
======================================================================

特に目的も定めずに SciPy_ を利用してみよう。何か便利なものが見つかるかもしれな
い。

.. toctree::
   :maxdepth: 3

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

     * Windows XP Home Edition SP3
     * Windows 7 Home Premium x64 SP1
     * Windows 10 Home x64

   * 本稿において、利用した各パッケージのバージョンは次のとおり。

     * Python_: 2.6.6, 2.7.3, 3.4.1, 3.5.0, 3.5.2, 3.6.5
     * SciPy_: 0.10.1, 0.14.0, 0.16.0, 0.18.0, 1.1.0
     * NumPy_: 1.6.1, 1.6.2, 1.8.2, 1.10.0, 1.11.1, 1.13.3
     * Matplotlib_: 1.1.0, 1.1.1, 1.3.1, 1.4.3, 1.5.1, 2.2.2
     * Nose_: 1.1.2, 1.3.3, 1.3.7

.. note::

   SciPy Reference Guide に倣い、以降のコード片においては、あらかじめ各種
   ``import`` を次のようにしたものとする。

   .. code:: python3

      import numpy as np
      import scipy as sp
      import matplotlib as mpl
      import matplotlib.pyplot as plt

関連リンク
======================================================================

SciPy_
  SciPy 総本山ウェブサイト。ドキュメント、ダウンロード、コードレシピ等。

関連ノート
======================================================================

* :doc:`/python-numpy/index`
* :doc:`/python-matplotlib/index`
* :doc:`/python-nose`

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
