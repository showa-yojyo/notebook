======================================================================
第 4 章 微分形式とベクトル場 3/4
======================================================================

.. contents:: ノート目次

4.3 接平面場（展開）
======================================================================

4.3.1 フロベニウスの定理
----------------------------------------------------------------------
* `接平面場 or 接分布 <https://en.wikipedia.org/wiki/Distribution_(differential_geometry)>`__ を余接空間と接空間の関係で定義する。

  1. :math:`\alpha \in \Omega^1(M)` と :math:`x \in M` に対して
     :math:`\ker\alpha = \set{v \in T_xM \sth \alpha(v) = 0}` は
     接空間 :math:`T_xM` の :math:`\dim M - 1` 次元部分多様体である。

  2. この :math:`\ker\alpha` の部分空間（接束 :math:`TM` の部分ベクトル束）を
     接平面場 or 接分布と呼ぶ。

* 関数 :math:`f \in \Omega^0(M)` が点 :math:`x_0 \in M` において
  :math:`\dd f \ne 0` であるとする。

  * このとき部分集合 :math:`\set{x \in M \sth f(x) = f(x_0)} \subset M` は
    点 :math:`x_0 \in M` の近傍で :math:`\dim M - 1` 次元部分多様体である。

  * この近傍は :math:`\dim M - 1` 次元の等位面で埋め尽くされていて、
  * :math:`\ker\dd f` は各点で等位面の接空間と一致する。

* 1 形式 :math:`g \dd f \in \Omega^1(M)` が点 :math:`x_0 \in M` で
  :math:`g(x) \ne 0` であるとする。
  このとき、状況は上記と同様になる。

* 1 形式 :math:`\alpha = g\dd f \in \Omega^1(M)` が点 :math:`x_0 \in M` の近傍で
  :math:`\alpha \ne 0` であるとするならば、
  :math:`\alpha \wedge \dd \alpha = 0` が成り立つ。

  * :math:`\alpha \wedge \dd \alpha = g\,\dd f \wedge (\dd f \wedge \dd f) = 0` による。

.. _tsuboi08.4.3.1:

* 定理 4.3.1: 上の逆が成立する

  * :math:`\alpha \in \Omega^1(M)` が点 :math:`x_0 \in M` の近傍で
    :math:`\alpha \ne 0` であり、
  * :math:`\alpha \wedge \dd \alpha = 0`

  ならば、点 :math:`x_0 \in M` の近傍の関数 :math:`f, g` が存在して、
  :math:`\alpha = g\,\dd f` が成り立つ。

  1. 証明をするための多様体上の点と座標近傍、微分形式、枠場を設定する：

     * :math:`x_0 \in (U, \varphi = (x_1, \dotsc, x_n))`
     * :math:`\displaystyle \alpha = \sum_{i = 1}^n f_i\,\dd x_i \in \Omega^1(M)`,
       ただし :math:`f_n = 1`
     * :math:`\xi_i = \dfrac{\partial}{\partial x_i} - f_i{\partial}{\partial x_n}\quad(i = 1, \dotsc, n - 1)`

  2. :math:`\alpha \wedge \dd\alpha = 0` であるので、次のようになっている：
  
     .. math::
     
        0 = \sum_i\sum_k\sum_j f_i \dfrac{\partial f_k}{\partial x_j}\,\dd x_i \wedge \dd x_j \wedge \dd x_k.`

  3. 括弧積を定義に従って計算すると次のようになる：
  
     .. math::
     
        [\xi_i, \xi_j] = \left(
            \dfrac{\partial f_j}{\partial x_i}
           +\dfrac{\partial f_i}{\partial x_j}
           + f_i \dfrac{\partial f_j}{\partial x_n}
           - f_j \dfrac{\partial f_i}{\partial x_n}
           \right)
           \dfrac{\partial}{\partial x_n}.

  4. ここで 2. の和のうち :math:`\dd x_i \wedge \dd x_j \wedge \dd x_n` の係数は
     3. の括弧内のものと等しい。したがって 3. の値はゼロである。

  5. 以上より、:math:`\xi_1, \dotsc, \xi_{n - 1}` は、

     * 生成するフローが可換であり、
     * :math:`\RR^{n - 1}` の局所的な作用を生成し、
     * :math:`\ker\dd f` を張る
     
       * :math:`\varphi\inv(0, \dotsc, 0, f(x))` がどうのと言っている。

     ベクトル場である。:ref:`幾何学 I 8.4 節 <tsuboi05.8.4>` を参照。

  6. 各点 :math:`x \in M` で、:math:`\alpha` は :math:`\dd f` のゼロでない関数倍である。
     つまり :math:`\alpha = g\,\dd f` なる :math:`g \ne 0` が存在する。

..

* :ref:`定理 4.3.1 <tsuboi08.4.3.1>` の条件を満たす接平面場と
  定理 4.3.1 の関数 :math:`f` の等位面の接平面場は同じもの（局所的）。
  これを「多様体 :math:`M` に余次元 1 `葉層構造 <http://mathworld.wolfram.com/Foliation.html>`__
  が与えられている」という。

  * 関数の等位面をつなぎ合わせると :math:`\dim M - 1` 次元部分多様体が定義される（局所的）。
  * この部分多様体の極大なものを葉という。

  * 例えば任意の接ベクトル :math:`v \in T_xM` に対して
    :math:`\alpha(v) \ne 0` なる :math:`\alpha \in Z^1(M)` は定理 4.3.1 の仮定を満たすので、
    余次元 1 葉層構造がある。

    * 微分形式が完全形式であるというのがありがたい。

* :math:`\alpha = g\,\dd f` が点 :math:`x_0 \in M` の近傍でゼロでなければ、
  :math:`\dd\alpha = \dd f \wedge \dd f = \dfrac{1}{g} \wedge \alpha` と書ける。
  よって、:math:`\alpha \wedge \dd\alpha = 0` ならば、
  :math:`\beta \in \Omega^1(M)` が存在して :math:`\dd\alpha = \beta \wedge \alpha` が
  成り立つと言い変えてもよい。

.. _tsuboi08.4.3.2:

* 定理 4.3.2: 1 形式と p 形式の外積に対する :math:`p - 1` 形式の存在

.. _tsuboi08.4.3.3:
.. _tsuboi08.4.3.4:
.. _tsuboi08.4.3.6:
.. _tsuboi08.4.3.7:
.. _tsuboi08.4.3.8:

4.3.2 微分形式の核
----------------------------------------------------------------------
TBW

4.3.3 体積形式とダイバージェンス
----------------------------------------------------------------------
TBW

4.3.4 シンプレクティク形式とハミルトン・ベクトル場
----------------------------------------------------------------------
TBW

4.3.5 接触形式とレーブ・ベクトル場
----------------------------------------------------------------------
TBW
