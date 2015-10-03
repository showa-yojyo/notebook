======================================================================
テンソル代数
======================================================================
モジュール ``sympy.tensor`` について記す。

.. contents:: ノート目次

.. note::

   本文中のすべての IPython セッション中のサンプルコードで、
   以下のインポートおよび出力書式設定が済んでいるものとする。

   .. code-block:: python3

      from sympy.tensor.tensor import *
      init_printing(use_unicode=False, pretty_print=False)

演習
======================================================================
参考文献

* モジュール ``sympy.tensor.tensor`` の docstring
* `電磁テンソル <https://ja.wikipedia.org/wiki/%E9%9B%BB%E7%A3%81%E3%83%86%E3%83%B3%E3%82%BD%E3%83%AB>`_

電磁テンソル
----------------------------------------------------------------------

.. code-block:: ipython

   In [1]: Lorentz = TensorIndexType('Lorentz', dummy_fmt='L')

   In [2]: Ex, Ey, Ez, Bx, By, Bz = symbols('E_x E_y E_z B_x B_y B_z')

   In [3]: c = symbols('c', positive=True)

   In [4]: m, n = tensor_indices('m n', Lorentz)

   In [5]: F = tensorhead('F', [Lorentz, Lorentz], [[2]])

   In [6]: F(-m, -n).data = [
       .....: [0, Ex/c, Ey/c, Ez/c],
       .....: [-Ex/c, 0, -Bz, By],
       .....: [-Ey/c, Bz, 0, -Bx],
       .....: [-Ez/c, -By, Bx, 0]]

   In [7]: F(m, n).get_matrix()
   Out[7]:
   Matrix([
   [    0, -E_x/c, -E_y/c, -E_z/c],
   [E_x/c,      0,   -B_z,    B_y],
   [E_y/c,    B_z,      0,   -B_x],
   [E_z/c,   -B_y,    B_x,      0]])

   In [8]: F(m, -n).get_matrix()
   Out[8]:
   Matrix([
   [    0, E_x/c, E_y/c, E_z/c],
   [E_x/c,     0,   B_z,  -B_y],
   [E_y/c,  -B_z,     0,   B_x],
   [E_z/c,   B_y,  -B_x,     0]])

   In [9]: F(-m, -n).get_matrix()
   Out[9]:
   Matrix([
   [     0, E_x/c, E_y/c, E_z/c],
   [-E_x/c,     0,  -B_z,   B_y],
   [-E_y/c,   B_z,     0,  -B_x],
   [-E_z/c,  -B_y,   B_x,     0]])

   In [10]: F(-m, -n)[0, 1:4]
   Out[10]: array([E_x/c, E_y/c, E_z/c], dtype=object)

   In [11]: F(-m, -n)[2, 3], F(-m, -n)[3, 1], F(-m, -n)[1, 2]
   Out[11]: (-B_x, -B_y, -B_z)

   In [12]: F(m, n)[0, 1:4]
   Out[12]: array([-E_x/c, -E_y/c, -E_z/c], dtype=object)

   In [13]: F(m, n)[2, 3], F(m, n)[3, 1], F(m, n)[1, 2]
   Out[13]: (-B_x, -B_y, -B_z)

* [1] オブジェクト ``Lorentz`` を生成する。
* [2][3] 例題で利用する次の各シンボルを定義する。

  * 電場（ベクトル量）の各成分を表すシンボル ``Ex``, ``Ey``, ``Ez``
  * 磁束密度（ベクトル量）の各成分を表すシンボル ``Bx``, ``By``, ``Bz``
  * 光速（スカラー量）を表すシンボル ``c``

* [4] テンソルの添字を表すふたつのシンボル ``m`` と ``n`` を定義する。
  この後生成する 2 階のテンソルシンボルとともに用いることになる。

* [5] 電磁テンソル :math:`F` を ``F`` として定義する。これは 2 階テンソルとなる。
* [6] :math:`F_{m n}` の行列表現の成分を直接設定する。
  負の符号付き添字オブジェクトは subscript/covariant を意味する。

* [7]-[9] :math:`F^{m n}`, :math:`F^m_n`, :math:`F_{m n}` を見る。

* [10]-[13] 電場の強度と磁束密度をテンソルから取る。

  .. math::
     :nowrap:

     \begin{eqnarray*}
     (F_{01}, F_{02}, F_{03}) &=& \left(\frac{E_x}{c}, \frac{E_y}{c}, \frac{E_z}{c}\right)\\
     (F^{01}, F^{02}, F^{03}) &=& \left(-\frac{E_x}{c}, -\frac{E_y}{c}, -\frac{E_z}{c}\right)\\
     (F_{23}, F_{31}, F_{12}) &=& (-B_x, -B_y, -B_z)\\
     (F^{23}, F^{31}, F^{12}) &=& (-B_x, -B_y, -B_z)
     \end{eqnarray*}

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
