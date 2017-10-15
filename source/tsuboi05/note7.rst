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

7.2 リーマン計量
----------------------------------------------------------------------
冒頭の議論が少々雑然としている感がある。

* 定義 7.2.1: リーマン計量

  #. :math:`T_xM` の元の長さの自乗を与える関数 :math:`q: T_xM \longto \RR` は存在するだろうか？
  #. それは次のような :math:`C^\infty` 級関数 :math:`q: TM \longto \RR` が存在すれば定まる：
     「:math:`q|T_xM` が `正値二次形式 <http://mathworld.wolfram.com/PositiveDefiniteQuadraticForm.html>`__ となる」
  #. このとき同時に正値 `対称双一次形式 <http://mathworld.wolfram.com/SymmetricBilinearForm.html>`__
     :math:`g: T_xM \times T_xM \longto \RR` が定まる。

  この上記の :math:`q: TM \longto \RR` をリーマン計量というのだが、
  :math:`g: T_xM \times T_xM \longto \RR` のほうをそう呼ぶことが多い。

  * :math:`\displaystyle v = \sum_i v_i\frac{\partial}{\partial x_i} \in T_xM` とすると
    :math:`\displaystyle q(v) = g(v, v) = \sum_{i, j} g_{ij}(x) v_i v_j` と書ける。

    * 行列 :math:`(g_{ij}(x))` は正値対称行列。
    * :math:`i, j` を固定すると :math:`g_{ij}: U \longto \RR` は :math:`C^\infty` 級関数。

  * リーマン多様体上では曲線の長さを測ることができる：

    .. math::
       :nowrap:

       \begin{gather*}
       L(c) = \int_0^1 \sqrt{q\left(\diff{c}{t}\right)}\,dt
            = \int_0^1 \sqrt{g\left(\diff{c}{t}, \diff{c}{t}\right)}\,dt.
       \end{gather*}

* 例 7.2.2: :math:`\RR^n` の原点近傍における :math:`\displaystyle\left. q(v) = \sum_{i = 1}^n v_i^2 \middle/ \left(1 + a \sum_{i = 1}^n x_i^2 \right)^2\right.\quad (a \in \RR)`

  * :math:`q` がリーマン計量を与えるような近傍が :math:`a` の符号によって異なる。
  * 点 :math:`(0, \dots, 0)` と点 :math:`(r, 0, \dots, 0)` を結ぶ線分の長さを計算する。
  * 円周 :math:`(r\cos\theta, r\sin\theta, 0, \dots, 0)` の長さを計算する。

    * 計算結果によると「円周率」が半径に依存することが見られる。

* 先ほどの距離がリーマン多様体上で距離の公理を満たすことを確認する。

  * 距離の公理のうち :math:`d(x, y) = 0 \implies x = y` だけが不明なので確認：

    * :math:`x \in M` の座標近傍 :math:`(U, \varphi)` 上のリーマン計量 :math:`g_{ij}` を考える。

    * まず :math:`\delta > 0` を :math:`g_{ij}(x)` の固有値の最小値を超えないように取る。
      このとき、:math:`\displaystyle \sum_{i, j} g_{ij}v_i v_j \le \delta \sum_{i} v_i^2` が
      開球 :math:`V = B_\eps(\varphi(x))` で成り立つような :math:`\eps > 0` が存在する。

      * :math:`y \in \varphi^{-1}(V)` であれば :math:`d(x, y) \le \sqrt{\delta}\lVert \varphi(x) - \varphi(y)\rVert`
        :math:`\therefore\ d(x, y) = 0 \implies \varphi(x) = \varphi(y) \implies x = y.`

      * :math:`y \notin \varphi^{-1}(V)` のときは面倒で、次のような関数を説明することになる：

        .. math::
           :nowrap:

           \begin{align*}
           F(z) = \left\{
           \begin{array}{lr}
           \lVert \varphi(x) - \varphi(z)\rVert^2 & : z \in \varphi^{-1}(V)\\
           \eps^2 + 1                             & : z \notin \varphi^{-1}(V)
           \end{array}
           \right.
           \end{align*}

        このとき、

        * :math:`x` と :math:`y` を結ぶ曲線は :math:`\varphi^{-1}(\partial V)` と交わって（∵中間値の定理）、
        * 境界 :math:`\partial V` 上では :math:`\lVert z - \varphi(x)\rVert = \eps`

        なので、
        :math:`d(x, y) \le \min\{d(z, x) \mid \varphi(z) \in \partial V\} \le \sqrt{\delta}\eps.`
        以下略。

    以上で :math:`d(x, y) = 0 \implies x = y` が示せた。

* 定義 7.2.3: リーマン計量により定まる距離

  :math:`d(x, y) = d_g(x, y) = \inf\{L(c) \mid c: [0, 1] \longto M,\ c(0) = x,\ c(1) = y\}.`

7.3 測地線
----------------------------------------------------------------------

`測地線 <http://mathworld.wolfram.com/Geodesic.html>`__
  :math:`C^1` 級曲線 :math:`c: [0, 1] \longto M` の次の積分の最小値問題を考える：
  
  .. math::
     :nowrap:
  
     \begin{align*}
     L(c) = \int_0^1\!\sqrt{\sum_{i, j}g_{ij}\left(\diff{c_i}{t}, \diff{c_j}{t}\right)}\,dt
     \end{align*}
  
  * ちなみに曲線のパラメーターの取り方は積分の値に影響しない。
  * 作用 :math:`\displaystyle A(c) = \int_0^1\!\sum_{i, j}g_{ij} \circ \diff{c_i}{t} \diff{c_j}{t}\,dt`
    について、本章の冒頭で述べたように :math:`L(c)^2 \le A(c)` が成りたつ。
  
    * 関数の内積、コーシー・シュワルツの不等式の等号成立条件などの検討をする。
  
  * 問題をすり替えて :math:`A(c)` の最小値問題とする。
    これを最小とするための必要条件を求めるのに、変分法という技法を適用する。
  
    * :math:`C^\infty` 級曲線 :math:`\eps: [0, 1] \longto \RR^n` で :math:`\eps(0) = \eps(1) = \bm 0` かつ
      ある十分小さい :math:`s \in \RR` に対して :math:`c(t) + s \eps(t)` は多様体に含まれるようなものを考える。
  
    * このとき :math:`A(c + s\eps)` は定まる。
      意味は :math:`s` の関数として :math:`s = 0` のときに :math:`A(c)` は最小であると仮定している。
  
  * :math:`\displaystyle \left.\diff{}{s}\right|_{s = 0} A(c + s\eps) = 0` が必要だ。
  
  * 各 :math:`k` に対して :math:`\displaystyle \sum_i g_{ik}\mdiff{c_i}{2}{t} = \sum_{i, j}\left(\frac{1}{2} \frac{\partial g_{ij}}{\partial x_k} - \frac{\partial g_{ik}}{\partial x_j}\right) \diff{c_j}{t} \diff{c_i}{t}`
    が必要。
  
  * 整形すると次のようになる。ただし :math:`g^{ij} = g_{ij}^{-1}` とする。
    :math:`\sum_k g^{lk}g_{kj} = \delta_{ij}` や :math:`g_{ij},\ g^{ij}` が対称行列であることに注意。
    
    .. math::
       :nowrap:
       
       \begin{align*}
       \mdiff{c_l}{2}{t} & = \sum_{i, k}g^{kl}g_{ik}\mdiff{c_i}{2}{t}\\
                         & = \sum_k g^{kl} \left(\frac{1}{2} \frac{\partial g_{ij}}{\partial x_k} - \frac{\partial g_{ik}}{\partial x_j}\right) \diff{c_j}{t} \diff{c_i}{t}.
       \end{align*}
  
  * この常微分方程式を満たす曲線 :math:`c` を測地線と呼ぶ。
  * 常微分方程式のかっこ内部分と :math:`\displaystyle \diff{c_j}{t}\diff{c_i}{t}` をかけて
    足し合わせたものの「対象成分」が測地線を決める：
    
    .. math::
       :nowrap:
       
       \begin{align*}
       \frac{1}{2}\left(\frac{\partial g_{ij}}{\partial x_k}
                       -\frac{\partial g_{jk}}{\partial x_i}
                       -\frac{\partial g_{ik}}{\partial x_j}\right).
       \end{align*}

`クリストッフェルの記号 <http://mathworld.wolfram.com/ChristoffelSymbol.html>`__
  クリストッフェルの記号とは、上記微分方程式を次の形式で書いたときの :math:`\Gamma_{ij}^l` 部分のことを言う：
  
  .. math::
     :nowrap:

     \begin{align*}
     \mdiff{c_l}{2}{t} + \sum_{i, j}\Gamma_{ij}^l\diff{c_j}{t} \diff{c_i}{t} = 0.
     \end{align*}

  :math:`\displaystyle \Gamma_{ij}^l = -\frac{1}{2}\sum_k g^{kl} \left( \frac{\partial g_{ij}}{\partial x_k} -\frac{\partial g_{jk}}{\partial x_i} -\frac{\partial g_{ik}}{\partial x_j}\right)`
  とすれば :math:`\Gamma_{ij}^l = \Gamma_{ji}^l` となる。

* :math:`\displaystyle v_l = \diff{c_l}{t}` とおいて、常微分方程式の階数を一つ落とす。
  :math:`v(t) \in T_{c(t)}M` に対しての常微分方程式
  :math:`\displaystyle \diff{v_l}{t} + \sum_{i,j}\Gamma_{ij}^l \diff{c_i}{t}v_j = 0` という見方もできる。

  * :math:`v(t)` は一意的に定まる。
  * `ユークリッド計量 <http://mathworld.wolfram.com/EuclideanMetric.html>`__
    :math:`g_{ij} = \delta_{ij}` に対しては :math:`\Gamma_{ij}^l = 0,\ v(t) = const` であり、
    :math:`v^0 \in T_{c(0)}\RR^n` を :math:`v^0 \in T_{c(t)}\RR^n` に平行移動したものになる。

* 問題 7.3.1: 上述の一階常微分方程式の解 :math:`v(t)` について :math:`q(v(t))` は一定である

  * 直接計算による。

* 先の一階常微分方程式の解二つ :math:`v(t), w(t)` について、さらに次のことが言える：
  :math:`q(v(t) + w(t))` も :math:`g(v(t), w(t))` も一定値を取る。

  * 正規直交基底をなすベクトルの組 :math:`v^{1}(0), \dotsc, v^{(n)}(0)` を初期値とする常微分方程式の解
    :math:`v^{1}(t), \dotsc, v^{(n)}(t)` も正規直交基底をなす。

  * 先の一階常微分方程式の解を用いて :math:`T_{c(0)}M` の一つの基底を :math:`c(t)` に沿って動かすことで
    :math:`T_{c(t)}M` に基底を定めることができる。
    このことを :math:`\Gamma_{ij}^l` により接続が与えられているという。

    * 特に :math:`\Gamma_{ij}^l` がリーマン計量から定まる接続を
      `レビチビタ接続 <http://mathworld.wolfram.com/Levi-CivitaConnection.html>`__
      という（正規直交系を正規直交系に平行移動）。

* 注意 7.3.2: 平行移動は曲線 :math:`c(t)` に依存して決まる。

----

:doc:`note8` へ。
