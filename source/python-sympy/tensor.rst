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

* モジュール ``sympy.tensor.tensor`` の docstring および対応するテストコード
* `Four-momentum <https://en.wikipedia.org/wiki/Four-momentum>`_: 英語版のほうが都合が良い符号の取り方をしている。
* `電磁テンソル <https://ja.wikipedia.org/wiki/%E9%9B%BB%E7%A3%81%E3%83%86%E3%83%B3%E3%82%BD%E3%83%AB>`_
* `Levi-Civita symbol <https://en.wikipedia.org/wiki/Levi-Civita_symbol>`_: モデルの視覚的表現物が豊富な英語版の記事のほうを勧める。

四元運動量
----------------------------------------------------------------------
四元運動量は 1 階テンソルとして表現できる。
以下の例ではテンソルオブジェクトの生成、上付き下付き添字の使い分け方、
内積・ノルムの評価をする。

.. code-block:: ipython

   In [1]: Lorentz = TensorIndexType('Lorentz', dummy_fmt='L')

   In [2]: Lorentz.data = [-1, 1, 1, 1]

   In [3]: E, c = symbols('E c', positive=True)

   In [4]: px, py, pz = symbols('p_x p_y p_z')

   In [5]: P = tensorhead('P', [Lorentz], [[1]])

   In [6]: P.data = [E/c, px, py, pz]

   In [7]: i = tensor_indices('i', Lorentz)

   In [8]: P(i).data, P(-i).data
   Out[8]:
   (array([E/c, p_x, p_y, p_z], dtype=object),
    array([-E/c, p_x, p_y, p_z], dtype=object))

   In [9]: (P(i) * P(-i)).data
   Out[9]: -E**2/c**2 + p_x**2 + p_y**2 + p_z**2

   In [10]: P**2
   Out[10]: -E**2/c**2 + p_x**2 + p_y**2 + p_z**2

* [1][2] オブジェクト ``Lorentz`` を生成する。
  この例題では Minkowski 内積を (-, +, +, +) となるように設定する。

* [3][4] 例題で利用する次の各シンボルを定義する。

  * 粒子のエネルギーを表すシンボル ``E``
  * 光速 ``c``
  * 粒子の運動量ベクトル :math:`\mathbf{P} = (p_x, p_y, p_z)` の各成分を表すシンボル ``px``, ``py``, ``pz``

* [5][6] 1 階のテンソルである四元運動量 :math:`P` を ``P`` として定義する。

* [7] テンソルの添字を表すシンボル ``i`` を定義する。
  一つあれば十分。

* [8] :math:`P^i` と :math:`P_i` の成分を表示する。
* [9][10] Minkowski ノルム :math:`P^i P_i` を計算するにはこのようにする。
  添字にマイナスの符号をつけることで subscript/covariant を指示する。
  念のため言及すると、反変と共変を入れ替えても同じ値が得られる。

電磁テンソル
----------------------------------------------------------------------
電磁場の強度は 2 階のテンソルで表現することがある。
以下の例では、テンソルの行列形式の成分を直接設定して、各種メソッドや関数を試す。

.. code-block:: ipython

   In [1]: Lorentz = TensorIndexType('Lorentz', dummy_fmt='L')

   In [2]: Lorentz.data = [1, -1, -1, -1]

   In [3]: Ex, Ey, Ez, Bx, By, Bz = symbols('E_x E_y E_z B_x B_y B_z')

   In [4]: c = symbols('c', positive=True)

   In [5]: m, n = tensor_indices('m n', Lorentz)

   In [6]: F = tensorhead('F', [Lorentz, Lorentz], [[2]])

   In [7]: F(-m, -n).data = [
       .....: [0, Ex/c, Ey/c, Ez/c],
       .....: [-Ex/c, 0, -Bz, By],
       .....: [-Ey/c, Bz, 0, -Bx],
       .....: [-Ez/c, -By, Bx, 0]]

   In [8]: F(m, n).get_matrix()
   Out[8]:
   Matrix([
   [    0, -E_x/c, -E_y/c, -E_z/c],
   [E_x/c,      0,   -B_z,    B_y],
   [E_y/c,    B_z,      0,   -B_x],
   [E_z/c,   -B_y,    B_x,      0]])

   In [9]: F(m, -n).get_matrix()
   Out[9]:
   Matrix([
   [    0, E_x/c, E_y/c, E_z/c],
   [E_x/c,     0,   B_z,  -B_y],
   [E_y/c,  -B_z,     0,   B_x],
   [E_z/c,   B_y,  -B_x,     0]])

   In [10]: F(-m, -n).get_matrix()
   Out[10]:
   Matrix([
   [     0, E_x/c, E_y/c, E_z/c],
   [-E_x/c,     0,  -B_z,   B_y],
   [-E_y/c,   B_z,     0,  -B_x],
   [-E_z/c,  -B_y,   B_x,     0]])

   In [11]: F(-m, -n)[0, 1:4]
   Out[11]: array([E_x/c, E_y/c, E_z/c], dtype=object)

   In [12]: F(-m, -n)[2, 3], F(-m, -n)[3, 1], F(-m, -n)[1, 2]
   Out[12]: (-B_x, -B_y, -B_z)

   In [13]: F(m, n)[0, 1:4]
   Out[13]: array([-E_x/c, -E_y/c, -E_z/c], dtype=object)

   In [14]: F(m, n)[2, 3], F(m, n)[3, 1], F(m, n)[1, 2]
   Out[14]: (-B_x, -B_y, -B_z)

* [1][2] オブジェクト ``Lorentz`` を生成する。
  計量は (+, -, -, -) とする。

* [3][4] 例題で利用する次の各シンボルを定義する。

  * 電場 :math:`\mathbf{E} = (E_x, E_y, E_z)` の各成分を表すシンボル ``Ex``, ``Ey``, ``Ez``
  * 磁束密度 :math:`\mathbf{B} = (B_x, B_y, B_z)` の各成分を表すシンボル ``Bx``, ``By``, ``Bz``
  * 光速（スカラー量）を表すシンボル ``c``

* [5] テンソルの添字を表すふたつのシンボル ``m`` と ``n`` を定義する。
  この後生成する 2 階のテンソルシンボルとともに用いることになる。

* [6] 電磁テンソル :math:`F` を ``F`` として定義する。これは 2 階テンソルとなる。
* [7] :math:`F_{m n}` の行列表現の成分を直接設定する。
  負の符号付き添字オブジェクトは subscript/covariant を意味する。

* [8]-[10] :math:`F^{m n}`, :math:`F^m_n`, :math:`F_{m n}` を見る。

* [11]-[14] 電場の強度と磁束密度をテンソルから取る。

  .. math::
     :nowrap:

     \begin{eqnarray*}
     (F_{01}, F_{02}, F_{03}) &=& \left(\frac{E_x}{c}, \frac{E_y}{c}, \frac{E_z}{c}\right)\\
     (F^{01}, F^{02}, F^{03}) &=& \left(-\frac{E_x}{c}, -\frac{E_y}{c}, -\frac{E_z}{c}\right)\\
     (F_{23}, F_{31}, F_{12}) &=& (-B_x, -B_y, -B_z)\\
     (F^{23}, F^{31}, F^{12}) &=& (-B_x, -B_y, -B_z)
     \end{eqnarray*}

もっと確かめる。

.. code-block:: ipython

   In [15]: Fmat = F(m, n).get_matrix()

   In [16]: Fmat.is_anti_symmetric()
   Out[16]: True

   In [17]: B = Matrix([Bx, By, Bz]); E = Matrix([Ex, Ey, Ez])

   In [18]: simplify((F(-m, -n) * F(m, n)).data)
   Out[18]: 2*(-E_x**2 - E_y**2 - E_z**2 + c**2*(B_x**2 + B_y**2 + B_z**2))/c**2

   In [19]: simplify(2*(B.dot(B) - E.dot(E)/c**2))
   Out[19]: 2*(-E_x**2 - E_y**2 - E_z**2 + c**2*(B_x**2 + B_y**2 + B_z**2))/c**2

   In [20]: simplify(B.dot(E) **2 / Fmat.det())
   Out[20]: c**2

* [15][16] 電磁テンソルの行列形式は交代行列である。
* [17] もっと早く定義しておくべきだったが、
  電場ベクトル ``E`` と磁束密度ベクトル ``B`` を生成する。
* [18][19] 電磁テンソルの内積 :math:`F_{m n} F^{m n}` は電場と磁束密度の大きさと光速の自乗とで表現できる。
* [20] 行列式 :math:`\det F` は電場と磁束密度のスカラー積と光速の自乗とで表現できる。

.. todo::

   この後 4 階の Levi-Civita epsilon をなんとか利用可能な状態にして、
   双対テンソルの生成をしたい。

Levi-Civita 記号
----------------------------------------------------------------------
``TensorIndexType`` 型オブジェクトのプロパティー ``epsilon`` は Levi-Civita 記号を表現する。
以下の例では、3 階の Levi-Civita 記号の添字の重複のない 6 個の値を見る。

.. code-block:: ipython

   In [1]: Lorentz = TensorIndexType('Lorentz', dim=3, dummy_fmt='L')

   In [2]: eps = Lorentz.epsilon

   In [3]: eps.rank
   Out[3]: 3

   In [4]: for i in permutations(tensor_indices('i:{}'.format(eps.rank), Lorentz)):
          .....:     e = eps(*i)
          .....:     print('{} == {}'.format(e, e.canon_bp()))
          .....:
   Eps(i0, i1, i2) == Eps(i0, i1, i2)
   Eps(i0, i2, i1) == -Eps(i0, i1, i2)
   Eps(i1, i0, i2) == -Eps(i0, i1, i2)
   Eps(i1, i2, i0) == Eps(i0, i1, i2)
   Eps(i2, i0, i1) == Eps(i0, i1, i2)
   Eps(i2, i1, i0) == -Eps(i0, i1, i2)

   In [5]: from sympy.combinatorics import AlternatingGroup

   In [6]: A3 = AlternatingGroup(3)

   In [7]: for i in A3.generate(): print(i.array_form)
   [0, 1, 2]
   [1, 2, 0]
   [2, 0, 1]

* [1] いつものようにオブジェクト ``Lorentz`` を生成する。3 次元とする。
* [2][3] プロパティー ``Lorentz.epsilon`` に別名を付ける。
  ついでにその階数が 3 であることを確認する。

* [4] 重複のないすべての添字の順列における ``epsilon`` の値と、
  その canonnical form とのそれの値とを出力する。
  これによると、次のことが正しく表現できていることが確認できる。

  * 添字順がサイクル ``(i0, i1, i2)`` の偶置換ならば ``epsilon(i0, i1, i2)`` に等しい
  * 添字順がサイクル ``(i0, i1, i2)`` の奇置換ならば ``-epsilon(i0, i1, i2)`` に等しい

* [5]-[7] 参考までに 3 次交代群の要素をすべて記す。

ここでは 3 階の例を試したが、テストコードは 4 階で動作確認をしている。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
