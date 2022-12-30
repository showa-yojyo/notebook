======================================================================
テンソル代数
======================================================================

モジュール ``sympy.tensor`` について記す。

.. contents:: ノート目次

.. note::

   本文中のすべての IPython セッション中のサンプルコードで、以下のインポートおよ
   び出力書式設定が済んでいるものとする。

   .. code:: python3

      from sympy.tensor.tensor import *
      init_printing(pretty_print=False)

演習
======================================================================

モジュール ``sympy.tensor.tensor`` の主要機能の演習を行う。

添字操作
----------------------------------------------------------------------

この例では主に添字の上げ下げについて見ていく。具体的に言えば各階のテンソルに対し
て関数 ``contract_metric`` がどのように利用できるのかを示す。

.. code:: ipython

   In [1]: Lorentz = TensorIndexType('Lorentz', dummy_fmt='L')

   In [2]: i, j, k, l, m, n = tensor_indices('i j k l m n', Lorentz)

   In [3]: g = Lorentz.metric

   In [4]: g
   Out[4]: metric(Lorentz,Lorentz)

   In [5]: g(), g(i), g(i, j)
   Out[5]: (metric(auto_left, -auto_right), metric(i, auto_left), metric(i, j))

* [1] オブジェクト ``Lorentz`` を生成する。この例では名前とダミー添字のプレ
  フィックスだけを指定しておく。
* [2] ``Lorentz`` から生成するテンソルオブジェクト用の添字オブジェクトをまとめて
  生成しておく。添字オブジェクトの生成は ``TensorIndexType`` 型のオブジェクトだ
  けで可能である。
* [3] 計量テンソルに別名 ``g`` を付けておく。
* [4][5] ``g`` 単体を色々な方法で表示してみる。

一階
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

引き続き一階のテンソルを定義して、添字の上げ下げを試みる。

プログラミング的には上げ下げしたいテンソルオブジェクトに対して、丸括弧により付随
する各添字オブジェクトにマイナス符号を付けるかどうかで共変反変の階数を自在に設定
できる。ここでは回りくどい方法を採る。

.. code:: ipython

   In [6]: A = tensorhead('A', [Lorentz]*1, [[1]])

   In [7]: contract_metric(g(-i, -j) * A(j), g)
   Out[7]: A(-i)

   In [8]: contract_metric(g(i, j) * A(-j), g)
   Out[8]: A(i)

   In [9]: g(i, j) * g(-j, -k)
   Out[9]: metric(i, L_0)*metric(-L_0, -k)

   In [10]: contract_metric(g(i, j) * g(-j, -k), g)
   Out[10]: metric(i, -k)

   In [11]: contract_metric(g(-k, -j) * g(j, i), g)
   Out[11]: metric(-k, i)

* [6] 一階テンソル ``A`` を生成する。引数の見てくれがいかにも特徴的だ。
* [7][8] 関数またはメソッド版の ``contract_metric`` を用いれば :math:`{A_i =
  g_{ij} A^j}` や :math:`{A^i = g^{ij} A_j}` を確認することができる。

  コード的にはマイナス付き添字は下付き・共変を意味する。

  * :code:`g(-i, -j)`: 共変計量テンソル
  * :code:`g(i, j)`: 反変計量テンソル

* [9] ところで生のままで :code:`g(i, j) * A(-j)` を出力すると、添字が縮約されて
  いないように一瞬見えるので困る。
* [10][11] :math:`g^{ij} g_{jk} = \delta^i_k` 等を検証したい。これはどうも無理な
  ようだ？

二階
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

引き続き二階のテンソルを定義して、添字の上げ下げを試みる。:math:`{B^{ij} =
g^{il} g^{jm} B_{lm}}` などを確かめる。

.. code:: ipython

   In [12]: B = tensorhead('B', [Lorentz]*2, [[1]*2])

   In [13]: contract_metric(g(i, l) * g(j, m) * B(-l, -m), g)
   Out[13]: B(i, j)

   In [14]: contract_metric(g(-i, -l) * g(-j, -m) * B(l, m), g)
   Out[14]: B(-i, -j)

四元運動量
----------------------------------------------------------------------

四元運動量は一階テンソルとして表現できる。以下の例ではテンソルオブジェクトの生
成、上付き下付き添字の使い分け方、内積・ノルムの評価をする。

.. code:: ipython

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

* [1][2] オブジェクト ``Lorentz`` を生成する。この例題では Minkowski 内積を
  ``(-, +, +, +)`` となるように設定する。
* [3][4] 例題で利用する次の各シンボルを定義する：

  * 粒子のエネルギーを表すシンボル ``E``
  * 光速 ``c``
  * 粒子の運動量ベクトル :math:`{\mathbf{P} = (p_x, p_y, p_z)}` の各成分を表すシ
    ンボル ``px``, ``py``, ``pz``

* [5][6] 一階のテンソルである四元運動量 :math:`P` を ``P`` として定義する。
* [7] テンソルの添字を表すシンボル ``i`` を定義する。一つあれば十分。
* [8] :math:`P^i` と :math:`P_i` の成分を表示する。
* [9][10] Minkowski ノルム :math:`P^i P_i` を計算するにはこのようにする。添字に
  マイナスの符号をつけることで subscript/covariant を指示する。念のため言及する
  と、反変と共変を入れ替えても同じ値が得られる。

電磁テンソル
----------------------------------------------------------------------

電磁場の強度は二階のテンソルで表現することがある。以下の例では、テンソルの行列形
式の成分を直接設定して、各種メソッドや関数を試す。

.. code:: ipython

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

* [1][2] オブジェクト ``Lorentz`` を生成する。計量は ``(+, -, -, -)`` とする。
* [3][4] 例題で利用する次の各シンボルを定義する：

  * 電場 :math:`{\mathbf{E} = (E_x, E_y, E_z)}` の各成分を表すシンボル ``Ex``,
    ``Ey``, ``Ez``
  * 磁束密度 :math:`{\mathbf{B} = (B_x, B_y, B_z)}` の各成分を表すシンボル
    ``Bx``, ``By``, ``Bz``
  * 光速（スカラー量）を表すシンボル ``c``

* [5] テンソルの添字を表すふたつのシンボル ``m`` と ``n`` を定義する。この後生成
  する二階のテンソルシンボルとともに用いることになる。
* [6] 電磁テンソル :math:`F` を ``F`` として定義する。これは二階テンソルとなる。
* [7] :math:`F_{m n}` の行列表現の成分を直接設定する。負の符号付き添字オブジェク
  トは subscript/covariant を意味する。
* [8]-[10] :math:`F^{m n}`, :math:`F^m_n`, :math:`F_{m n}` を見る。
* [11]-[14] 電場の強度と磁束密度をテンソルから取る。

  .. math::
     :nowrap:

     \begin{align*}
     (F_{01}, F_{02}, F_{03}) &= \left(\frac{E_x}{c}, \frac{E_y}{c}, \frac{E_z}{c}\right)\\
     (F^{01}, F^{02}, F^{03}) &= \left(-\frac{E_x}{c}, -\frac{E_y}{c}, -\frac{E_z}{c}\right)\\
     (F_{23}, F_{31}, F_{12}) &= (-B_x, -B_y, -B_z)\\
     (F^{23}, F^{31}, F^{12}) &= (-B_x, -B_y, -B_z)
     \end{align*}

もっと確かめる。

.. code:: ipython

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
* [17] もっと早く定義しておくべきだったが、電場ベクトル ``E`` と磁束密度ベクトル
  ``B`` を生成する。
* [18][19] 電磁テンソルの内積 :math:`F_{m n} F^{m n}` は電場と磁束密度の大きさと
  光速の自乗とで表現できる。
* [20] 行列式 :math:`\det F` は電場と磁束密度のスカラー積と光速の自乗とで表現で
  きる。

.. todo::

   この後四階の Levi-Civita epsilon をなんとか利用可能な状態にして、双対テンソル
   の生成をしたい。

Levi-Civita 記号
----------------------------------------------------------------------

``TensorIndexType`` 型オブジェクトのプロパティー ``epsilon`` は Levi-Civita 記号
を表現する。以下の例では、三階の Levi-Civita 記号の添字の重複のない六個の値を見
る。

.. code:: ipython

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

* [1] いつものようにオブジェクト ``Lorentz`` を生成する。三次元とする。
* [2][3] プロパティー :code:`Lorentz.epsilon` に別名を付ける。ついでにその階数が
  3 であることを確認する。
* [4] 重複のないすべての添字の順列における ``eps`` の値と、その canonnical form
  とのそれの値とを出力する。添字 :code:`(l, m, n)` の置換に関して次のことが正し
  く表現できている。

  * :code:`(i0, i1, i2)` の偶置換ならば :code:`eps(l, m, n) == eps(i0, i1, i2)`
  * :code:`(i0, i1, i2)` の奇置換ならば :code:`eps(l, m, n) == -eps(i0, i1, i2)`

* [5]-[7] 参考までに三次交代群の要素をすべて記す。

ここでは三階の例を試したが、テストコードは四階で動作確認をしている。

参考文献
----------------------------------------------------------------------

* モジュール ``sympy.tensor.tensor`` の docstring および対応するテストコード
* `Raising and lowering indices <https://en.wikipedia.org/wiki/Raising_and_lowering_indices>`_
* `Four-momentum <https://en.wikipedia.org/wiki/Four-momentum>`_: 英語版のほうが都合が良い符号の取り方をしている。
* `電磁テンソル <https://ja.wikipedia.org/wiki/%E9%9B%BB%E7%A3%81%E3%83%86%E3%83%B3%E3%82%BD%E3%83%AB>`_
* `Levi-Civita symbol <https://en.wikipedia.org/wiki/Levi-Civita_symbol>`_: モデルの視覚的表現物が豊富な英語版の記事のほうを勧める。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
