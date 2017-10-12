======================================================================
幾何学 I 多様体入門 読書ノート 7/8
======================================================================

:doc:`note6` からの続き。

.. contents:: ノート目次

第 7 章 多様体上の曲線の長さ
======================================================================
多様体上の曲線の長さを定義できる多様体を
`リーマン計量 <http://mathworld.wolfram.com/RiemannianMetric.html>`__ を持つ
`リーマン多様体 <http://mathworld.wolfram.com/RiemannianManifold.html>`__ という。

7.1 ユークリッド空間内の多様体上の曲線（基礎）
----------------------------------------------------------------------
:math:`\displaystyle L(c) = \int_{t_0}^{t_1}\!\left\lVert \diff{c(t)}{t} \right\rVert\,dt`

* 例題 7.1.1: 最小問題

  曲線 :math:`c` は :math:`c(0) = x^0,\ c(1) = x^1` とする。

  #. この二点を結ぶ曲線の中で長さが最小のものは線分である。

     * 別解が面白い。
       :math:`\displaystyle \bm v = \frac{x^1 - x^0}{\lVert x^1 - x^0 \rVert}` として
       :math:`\displaystyle \left\lVert \diff{c(t)}{t} \right\rVert \le \left\lvert \diff{c(t)}{t} \cdot \bm v \right\rvert`
       を利用する。

  #. :math:`\displaystyle A(c) = \int_0^1\!\left\lVert \diff{c(t)}{t} \right\rVert ^2\,dt`
     を最小とする曲線は :math:`c(t) = x^0 + t(x^1 - x^0)` である。

     * :math:`A(c + s\eps)` なる量を考える。展開すると :math:`s` の二次式が得られる。
       これが最小値（極小値）を :math:`s = c` で持つには
       :math:`\displaystyle \diff{c}{t} = 0` であることが必要だ。
       仮定を満たすものは :math:`c(t) = x^0 + t(x^1 - x^0)` しかない。

     * なお :math:`A(c)` と :math:`L(c)` の最小値を与える :math:`c(t)` は同じものである。

* 問題 7.1.2: :math:`C^1` 級曲線の長さ

  * :math:`\Delta = \{ 0 = t_0 \le \dots \le t_m = 1\}` を区間 :math:`[0, 1]` の細分とすると
    :math:`\displaystyle \int_{0}^{1}\!\left\lVert \diff{c(t)}{t} \right\rVert\,dt = \sup_{\Delta}\sum_{k = 1}^m \left\lVert c(t_k) - c(t_{k - 1})\right\rVert`

  * 証明全体は微積分の教科書を参照。

* 問題 7.1.3: 双曲面上の長さの最小値

  曲面 :math:`x^2 + y^2 - z^2 = 1` 上で点 :math:`(1, 0, 0)` から点 :math:`(-1, 0, 0)` を結ぶ曲線の長さの最小値を調べる。

  * `絵 <http://mathworld.wolfram.com/One-SheetedHyperboloid.html>`__ を描けば半円弧の長さが最小値と一致することは直感でわかる。
  * なぜか平面上への写像 :math:`\displaystyle p(x, y, z) = \left(\frac{x}{\sqrt{x^2 + y^2}}, \frac{y}{\sqrt{x^2 + y^2}}, 0\right)` を定義し、
    :math:`p \circ c(t)` を考えることになる。
    この写像は双曲面上の点を円筒 :math:`x^2 + y^2 = 1` に投影してから座標平面 :math:`z = 0` に投影するものだ。

    * 合成写像の曲線の長さのほうがオリジナルよりも小さくなることをどう説明するか。

  .. math::
     :nowrap:

     \begin{align*}
     \int_{0}^{1}\!\left\lVert \diff{p \circ c(t)}{t} \right\rVert\,dt
     =   \int_{0}^{1}\!\left\lVert (Dp)_{c(t)} c'(t) \right\rVert\,dt
     \le \int_{0}^{1}\!\left\lVert c'(t) \right\rVert\,dt
     \end{align*}

連結多様体 :math:`M` には次のようにすると距離が入る。
これは後で正式に確かめる：

.. math::
   :nowrap:

   \begin{align*}
   \forall x, y \in M, d(x, y) = \inf\{L(c) \mid c: [0, 1] \longto M,\ c(0) = x,\ c(1) = y\}
   \end{align*}

* 例題 7.1.4: 曲線の合成？

  * 本題である長さの計算というより計算途中で
    :math:`\displaystyle {}^t\!D\Phi D\Phi` という量が出てくることのほうが気になる。
    これは次のようにして得られる：

    .. math::
       :nowrap:

       \begin{gather*}
       \begin{split}
       \left\lVert \diff{(\Phi \circ c)(t)}{t} \right\rVert
       &= \left\lVert (D\Phi)_{c(t)} \diff{c(t)}{t} \right\rVert\\
       &= \left({}^t\!\left((D\Phi)_{c(t)} \diff{c(t)}{t}\right) \cdot \left((D\Phi)_{c(t)} \diff{c(t)}{t}\right)\right)^\frac{1}{2}\\
       &= \left({}^t\!\left(\diff{c}{t}\right) {}^t\!D\Phi \cdot D\Phi \diff{c}{t}\right)^\frac{1}{2}
       \end{split}
       \end{gather*}

* 問題 7.1.5: 球面に投影した曲線の長さ

  * :math:`S_r` を曲面 :math:`x^2 + y^2 + (z + R)^2 = R^2` とする。
  * 平面曲線を :math:`c(t) = (\xi(t), \eta(t)),\quad t \in [0, 1]` とする。
  * 球面上の点を平面に投影する写像を :math:`p: S_r \setminus (0, 0, -2R) \longto \RR^2` とする。
  * 考え方は問題 7.1.3 や例題 7.1.4 と同じ。次の手順で計算する：

    #. :math:`p^{-1}` を計算する（球面上への投影写像）
    #. :math:`Dp^{-1}` を計算する
    #. :math:`{}^t\!(Dp^{-1})(Dp^{-1})` を計算する（積分の途中で使うため）
    #. 積分 :math:`L(p^{-1} \circ c)` を計算する

----

:doc:`note8` へ。
