======================================================================
第 7 章 多様体上の曲線の長さ（前編）
======================================================================

多様体上の曲線の長さを定義できる多様体を
`リーマン計量 <http://mathworld.wolfram.com/RiemannianMetric.html>`__ を持つ
`リーマン多様体 <http://mathworld.wolfram.com/RiemannianManifold.html>`__ という。

.. contents:: ノート目次

7.1 ユークリッド空間内の多様体上の曲線（基礎）
======================================================================
:math:`\displaystyle L(c) = \int_{t_0}^{t_1}\!\Norm{\diff{c(t)}{t}}\,\dd{t}`

.. _tsuboi05.7.1.1:

* 例題 7.1.1: 最小問題

  曲線 :math:`c` は :math:`c(0) = x^0,\ c(1) = x^1` とする。

  #. この二点を結ぶ曲線の中で長さが最小のものは線分である。

     * 別解が面白い。
       :math:`\displaystyle \bm v = \frac{x^1 - x^0}{\norm{x^1 - x^0}}` として
       :math:`\displaystyle \Norm{\diff{c(t)}{t}} \le \Abs{\diff{c(t)}{t} \cdot \bm v}`
       を利用する。

  #. :math:`\displaystyle A(c) = \int_0^1\!\Norm{\diff{c(t)}{t}} ^2\,\dd{t}`
     を最小とする曲線は :math:`c(t) = x^0 + t(x^1 - x^0)` である。

     * :math:`A(c + s\eps)` なる量を考える。展開すると :math:`s` の二次式が得られる。
       これが最小値（極小値）を :math:`s = c` で持つには
       :math:`\displaystyle \diff{c}{t} = 0` であることが必要だ。
       仮定を満たすものは :math:`c(t) = x^0 + t(x^1 - x^0)` しかない。

     * なお :math:`A(c)` と :math:`L(c)` の最小値を与える :math:`c(t)` は同じものである。

.. _tsuboi05.7.1.2:

* 問題 7.1.2: :math:`C^1` 級曲線の長さ

  * :math:`\Delta = \set{ 0 = t_0 \le \dots \le t_m = 1}` を区間 :math:`[0, 1]` の細分とすると
    :math:`\displaystyle \int_{0}^{1}\!\Norm{\diff{c(t)}{t}}\,\dd{t} = \sup_{\Delta}\sum_{k = 1}^m \norm{c(t_k) - c(t_{k - 1})}`

  * 証明全体は微積分の教科書を参照。

.. _tsuboi05.7.1.3:

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
     \int_{0}^{1}\!\Norm{\diff{p \circ c(t)}{t}}\,\dd{t}
     =   \int_{0}^{1}\!\Norm{(Dp)_{c(t)} c'(t)}\,\dd{t}
     \le \int_{0}^{1}\!\Norm{c'(t)}\,\dd{t}
     \end{align*}

連結多様体 :math:`M` には次のようにすると距離が入る。
これは後で正式に確かめる：

.. math::
   :nowrap:

   \begin{align*}
   \forall x, y \in M, d(x, y) = \inf\set{L(c) \sth \fn{c}{[0, 1]}M,\ c(0) = x,\ c(1) = y}
   \end{align*}

.. _tsuboi05.7.1.4:

* 例題 7.1.4: トーラスに投影した曲線の長さ

  * :math:`\Phi(x_1, x_2) = ((2 + \cos x_2)\cos x_1,\ (2 + \cos x_2)\sin x_1,\ \sin x_2)` はトーラスだ。
  * :math:`c(t) = (\xi(t), \eta(t)) \subset \RR^2` に関する
    :math:`\fn{\Phi \circ c}{[0, 1]}M` の長さを求めるのが本題だ。

  * 本題である長さの計算というより計算途中で
    :math:`{}^t\!(D\Phi) D\Phi` という量が出てくることのほうが気になる。
    これは次のようにして得られる：

    .. math::
       :nowrap:

       \begin{gather*}
       \begin{split}
       \Norm{\diff{(\Phi \circ c)(t)}{t}}
       &= \Norm{(D\Phi)_{c(t)} \diff{c(t)}{t}}\\
       &= \left({}^t\!\left((D\Phi)_{c(t)} \diff{c(t)}{t}\right) \cdot \left((D\Phi)_{c(t)} \diff{c(t)}{t}\right)\right)^\frac{1}{2}\\
       &= \left({}^t\!\left(\diff{c}{t}\right) {}^t\!D\Phi \cdot D\Phi \diff{c}{t}\right)^\frac{1}{2}
       \end{split}
       \end{gather*}

.. _tsuboi05.7.1.5:

* 問題 7.1.5: 球面に投影した曲線の長さ

  * :math:`c(t) = (\xi(t), \eta(t)) \subset \RR^2` に関する
    :math:`\fn{p\inv \circ c}{[0, 1]}M` の長さを求めるのが本題だ。

  * :math:`S_r` を曲面 :math:`x^2 + y^2 + (z + R)^2 = R^2` とする。
  * 球面上の点を平面に投影する写像を :math:`\fn{p}{S_r \setminus \set{(0, 0, -2R)}}\RR^2` とする。
  * 考え方は :ref:`問題 7.1.3 <tsuboi05.7.1.3>` や
    :ref:`例題 7.1.4 <tsuboi05.7.1.4>` と同じ。次の手順で計算する：

    #. :math:`p(x, y, z)` を求める：

       .. math::

          \left(\frac{2Rx}{2R + z}, \frac{2Ry}{2R + z}\right).

    #. :math:`p\inv(u, v)` を計算する（球面上への投影写像）：

       .. math::

          \left(\frac{4R^2u}{u^2 + v^2 + 4R^2}, \frac{4R^2v}{u^2 + v^2 + 4R^2}, -\frac{2R(u^2 + v^2)}{u^2 + v^2 + 4R^2}\right).

    #. :math:`Dp\inv` を計算する

       .. math::

          \begin{pmatrix}
            \dfrac{4 R^2 (4 R^2 - u^2 + v^2)}{(4 R^2 + u^2 + v^2)^2} & - \dfrac{8 R^2 u v}{(4 R^2 + u^2 + v^2)^2}\\
          - \dfrac{8 R^2 u v}{(4 R^2 + u^2 + v^2)^2} & \dfrac{4 R^2 (4 R^2 + u^2 - v^2)}{(4 R^2 + u^2 + v^2)^2}\\
          - \dfrac{16 R^3 u}{(4 R^2 + u^2 + v^2)^2} & - \dfrac{16 R^3 v}{(4 R^2 + u^2 + v^2)^2}
          \end{pmatrix}

    #. :math:`{}^t\!(Dp\inv)(Dp\inv)` を計算する（積分の途中で使うため）

       .. math::

          \begin{pmatrix}
          \left(\dfrac{4R^2}{u^2 + v^2 + 4R^2}\right)^2 & 0\\
          0 & \left(\dfrac{4R^2}{u^2 + v^2 + 4R^2}\right)^2
          \end{pmatrix}

    #. 積分 :math:`\displaystyle L(p\inv \circ c) = \int_0^1\!\Norm{\diff{(p\inv\circ c)}{t}}\,\dd{t}` を書き下す

       .. math::

          \int_0^1\! \dfrac{4R^2 \sqrt{\xi'(t)^2 + \eta'(t)^2}}{\xi(t)^2 + \eta(t)^2 + 4R^2} \,\dd{t}.

.. _tsuboi05.7.2:

7.2 リーマン計量
======================================================================
冒頭の議論が少々雑然としている感がある。

.. _tsuboi05.7.2.1:

* 定義 7.2.1: リーマン計量

  #. :math:`T_xM` の元の長さの自乗を与える関数 :math:`\fn{q}{T_xM}\RR` は存在するだろうか？
  #. それは次のような :math:`C^\infty` 級関数 :math:`\fn{q}{TM}\RR` が存在すれば定まる：
     「:math:`q|T_xM` が `正値二次形式 <http://mathworld.wolfram.com/PositiveDefiniteQuadraticForm.html>`__ となる」
  #. このとき同時に正値 `対称双一次形式 <http://mathworld.wolfram.com/SymmetricBilinearForm.html>`__
     :math:`\fn{g}{T_xM \times T_xM}\RR` が定まる。

  この上記の :math:`\fn{q}{TM}\RR` をリーマン計量というのだが、
  :math:`\fn{g}{T_xM \times T_xM}\RR` のほうをそう呼ぶことが多い。

  * :math:`\displaystyle v = \sum_i v_i\frac{\partial}{\partial x_i} \in T_xM` とすると
    :math:`\displaystyle q(v) = g(v, v) = \sum_{i, j} g_{ij}(x) v_i v_j` と書ける。

    * 行列 :math:`(g_{ij}(x))` は正値対称行列。
    * :math:`i, j` を固定すると :math:`\fn{g_{ij}}{U}\RR` は :math:`C^\infty` 級関数。

  * リーマン多様体上では曲線の長さを測ることができる：

    .. math::
       :nowrap:

       \begin{gather*}
       L(c) = \int_0^1 \sqrt{q\left(\diff{c}{t}\right)}\,\dd{t}
            = \int_0^1 \sqrt{g\left(\diff{c}{t}, \diff{c}{t}\right)}\,\dd{t}.
       \end{gather*}

.. _tsuboi05.7.2.2:

* 例 7.2.2: :math:`\RR^n` の原点近傍における :math:`\displaystyle\left. q(v) = \sum_{i = 1}^n v_i^2 \middle/ \left(1 + a \sum_{i = 1}^n x_i^2 \right)^2\right.\quad (a \in \RR)`

  * :math:`q` がリーマン計量を与えるような近傍が :math:`a` の符号によって異なる。
  * 点 :math:`(0, \dots, 0)` と点 :math:`(r, 0, \dots, 0)` を結ぶ線分の長さを計算する。

    .. math::

       L = \int_0^r\!\frac{\dd{t}}{1 + a^2}

    * :math:`a > 0` ならば :math:`L = \dfrac{1}{\sqrt{a}}\left[\tan\inv\sqrt{a}t\right]_0^r = \dfrac{1}{\sqrt{a}}\tan\inv\sqrt{a}r.`
    * :math:`a < 0` ならば :math:`L = \dfrac{1}{2\sqrt{-a}}\left[\log\dfrac{1 + \sqrt{-a}t}{1 - \sqrt{-a}t}\right]_0^r = \dfrac{1}{2\sqrt{-a}}\log\dfrac{1 + \sqrt{-a}r}{1 - \sqrt{-a}r}.`

  * 円周 :math:`(r\cos\theta, r\sin\theta, 0, \dots, 0)` の長さを計算する。

    .. math::

       L = \int_0^{2\pi}\!\dfrac{\dd{\theta}}{1 + ar^2} = \dfrac{2\pi}{1 + ar^2}.

    * 計算結果によると「円周率」が半径に依存することが見られる。

* 先ほどの距離がリーマン多様体上で距離の公理を満たすことを確認する。

  * 距離の公理のうち :math:`d(x, y) = 0 \implies x = y` だけが不明なので確認：

    * :math:`x \in M` の座標近傍 :math:`(U, \varphi)` 上のリーマン計量 :math:`g_{ij}` を考える。

    * まず :math:`\delta > 0` を :math:`g_{ij}(x)` の固有値の最小値を超えないように取る。
      このとき、:math:`\displaystyle \sum_{i, j} g_{ij}v_i v_j \le \delta \sum_{i} v_i^2` が
      開球 :math:`V = B_\eps(\varphi(x))` で成り立つような :math:`\eps > 0` が存在する。

      * :math:`y \in \varphi\inv(V)` であれば :math:`d(x, y) \le \sqrt{\delta}\norm{\varphi(x) - \varphi(y)}`
        :math:`\therefore\ d(x, y) = 0 \implies \varphi(x) = \varphi(y) \implies x = y.`

      * :math:`y \notin \varphi\inv(V)` のときは面倒で、次のような関数を説明することになる：

        .. math::

           F(z) = 
           \begin{cases}
           \norm{\varphi(x) - \varphi(z)}^2 & \quad \text{if } z \in \varphi\inv(V)\\
           \eps^2 + 1 & \quad \text{if } z \notin \varphi\inv(V)
           \end{cases}

        このとき、

        * :math:`x` と :math:`y` を結ぶ曲線は :math:`\varphi\inv(\partial V)` と交わって（∵中間値の定理）、
        * 境界 :math:`\partial V` 上では :math:`\norm{z - \varphi(x)} = \eps`

        なので、
        :math:`d(x, y) \le \min\set{d(z, x) \sth \varphi(z) \in \partial V} \le \sqrt{\delta}\eps.`
        以下略。

    以上で :math:`d(x, y) = 0 \implies x = y` が示せた。

.. _tsuboi05.7.2.3:

* 定義 7.2.3: リーマン計量により定まる距離

  :math:`d(x, y) = d_g(x, y) = \inf\set{L(c) \sth \fn{c}{[0, 1]}M,\ c(0) = x,\ c(1) = y}.`

7.3 測地線
======================================================================

`測地線 <http://mathworld.wolfram.com/Geodesic.html>`__
  :math:`C^1` 級曲線 :math:`\fn{c}{[0, 1]}M` の次の積分の最小値問題を考える：

  .. math::
     :nowrap:

     \begin{align*}
     L(c) = \int_0^1\!\sqrt{\sum_{i, j}g_{ij}\left(\diff{c_i}{t}, \diff{c_j}{t}\right)}\,\dd{t}
     \end{align*}

  * ちなみに曲線のパラメーターの取り方は積分の値に影響しない。
  * 作用 :math:`\displaystyle A(c) = \int_0^1\!\sum_{i, j}g_{ij} \circ \diff{c_i}{t} \diff{c_j}{t}\,dd{t}`
    について、本章の冒頭で述べたように :math:`L(c)^2 \le A(c)` が成りたつ。

    * 関数の内積、コーシー・シュワルツの不等式の等号成立条件などの検討をする。

  * 問題をすり替えて :math:`A(c)` の最小値問題とする。
    これを最小とするための必要条件を求めるのに、変分法という技法を適用する。

    * :math:`C^\infty` 級曲線 :math:`\fn{\eps}{[0, 1]}\RR^n` で :math:`\eps(0) = \eps(1) = \bm 0` かつ
      ある十分小さい :math:`s \in \RR` に対して :math:`c(t) + s \eps(t)` は多様体に含まれるようなものを考える。

    * このとき :math:`A(c + s\eps)` は定まる。
      意味は :math:`s` の関数として :math:`s = 0` のときに :math:`A(c)` は最小であると仮定している。

  * :math:`\displaystyle \left.\diff{}{s}\right|_{s = 0} A(c + s\eps) = 0` が必要だ。

  * 各 :math:`k` に対して :math:`\displaystyle \sum_i g_{ik}\mdiff{c_i}{2}{t} = \sum_{i, j}\left(\frac{1}{2} \frac{\partial g_{ij}}{\partial x_k} - \frac{\partial g_{ik}}{\partial x_j}\right) \diff{c_j}{t} \diff{c_i}{t}`
    が必要。

  * 整形すると次のようになる。ただし :math:`g^{ij} = g_{ij}\inv` とする。
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
    :math:`g_{ij} = \delta_{ij}` に対しては :math:`\Gamma_{ij}^l = 0,\ v(t) = const.` であり、
    :math:`v^0 \in T_{c(0)}\RR^n` を :math:`v^0 \in T_{c(t)}\RR^n` に平行移動したものになる。

.. _tsuboi05.7.3.1:

* 問題 7.3.1: 上述の一階常微分方程式の解 :math:`v(t)` について :math:`q(v(t))` は一定である

  * 直接 :math:`\displaystyle \diff{q(v(t))}{t} = 0` を計算によって示す：

    .. math::
       :nowrap:

       \begin{align*}
       \diff{q(v(t))}{t}
       & = \diff{}{t}g(v(t), v(t)) = \diff{}{t}\sum_{i, j} g_{ik}v_i v_k\\

       &= \sum_{i, j, k}\frac{\partial g_{ik}}{\partial x_j} \diff{c_j}{t} v_i v_k
        + \frac{1}{2}\sum_{i, k}\diff{v_i}{t}v_k\\

       &= \sum_{i, j, k}\frac{\partial g_{ik}}{\partial x_j} \diff{c_j}{t} v_i v_k 
        + \sum_{i, j, k}\left(
          \frac{\partial g_{ij}}{\partial x_k}
         -\frac{\partial g_{jk}}{\partial x_i}
         -\frac{\partial g_{ik}}{\partial x_j}
       \right)\diff{c_i}{t}v_j v_k\\

       &= \sum_{i, j, k}\left(\frac{\partial g_{ik}}{\partial x_j} \diff{c_j}{t} v_i v_k -\frac{\partial g_{jk}}{\partial x_i} \diff{c_i}{t}v_j v_k \right)
        + \sum_{i, j, k}\left(\frac{\partial g_{ij}}{\partial x_k} -\frac{\partial g_{ik}}{\partial x_j} \right) \diff{c_i}{t}v_j v_k \\

       &= 0.
       \end{align*}

  * クリストッフェル記号の定義式を逆に見ることと、
    最後の和でうまく組み合わせるとゼロであることがわかるのが難しい。

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

.. _tsuboi05.7.3.2:

* 注意 7.3.2: 平行移動は曲線 :math:`c(t)` に依存して決まる。

7.4 局所的最短性
======================================================================
先の議論は :math:`\displaystyle \diff{c}{t} = 0` となる点を含む曲線は除外していた。それを見直す。

:math:`V \subset \RR^n` 上で定義された正規形二階常微分方程式を
:math:`V \subset \RR^n` 上の正規形一階常微分方程式に書き直す。

#. 初期値を :math:`\displaystyle c(0) = \bm x \in V,\quad \diff{c}{t}(0) = \bm v \in \RR^n` とする。
#. 本書 p. 149 の測地線方程式において :math:`c(t)` が解であれば :math:`c(at)\quad (a \in \RR)` も解である。

   * :math:`(0, 0)` で :math:`(\bm x, \bm v)` をとる。
   * :math:`c(at)` の定義域は元のそれの :math:`a\inv` 倍であるが、問題ない。

#. :math:`V \times \RR^n` 上の初期値を :math:`(\bm x, \bm X)` とする解は次の形をしている：
   :math:`\displaystyle \left(c(t, \bm x, \bm X), \diff{c}{t}(t, \bm x, \bm X)\right).`

#. 一階常微分方程式を :math:`V \times \RR^n` 上のベクトル場として書く。
#. そのベクトル場が生成するフロー :math:`F` は次を満たす：
   :math:`F(at, \bm x, \bm v) = F(t, \bm x, a\bm v).`
   したがって原点の近傍の :math:`\bm v` について次の写像を定義することができる：
   :math:`E_{\bm x}(\bm v) = F(1, \bm x, \bm v).`

#. :math:`E_{\bm x}: \bm v \longmapsto F(1, \bm x, \bm v)` は原点の近傍から
   :math:`\bm x` の近傍への微分同相写像である。
   この写像を `指数写像 <http://mathworld.wolfram.com/ExponentialMap.html>`__ という。

.. _tsuboi05.7.4.1:

* 問題 7.4.1: 球面上の二点の「距離」を定義する曲線は大円に含まれる

  * :math:`S^2` のパラメーター表示を例えば
    :math:`\Phi(\theta, \psi) = (\cos\psi\cos\theta, \cos\psi\sin\theta, \sin\psi)`
    とする。

    * この表示では :math:`\psi` 一定が赤道に平行な面の大円となっている。

  * 一点を北極に固定して証明してよい。
    点 :math:`(0, 0, 1)` と点 :math:`\Phi(\theta_0, \psi_0)` を結ぶ曲線を調べることにする。

  * :math:`D\Phi` を求め、:math:`{}^t\!(D\Phi)(D\Phi) = \cos^2\psi \theta'^2 + \psi'^2` を得る。
  * 本問では長さを不等式で評価すれば十分だ：

    .. math::

       \begin{align*}
       L &= \int_0^1\!\sqrt{\cos^2\psi \theta'^2 + \psi'^2}\,\dd{t}
       \ge \int_0^1\! \sqrt{\psi'^2}\,\dd{t}
       = \int_0^1\! \abs{\psi'}\,\dd{t}\\
       &\ge \abs{\psi(1) - \psi(0)} = \frac{\pi}{2} - \psi_0.
       \end{align*}

  * よって :math:`\theta = \theta_0` なる大円の弧が長さが最短となる。

測地線の局所的最短性。これは難しい。

#. 曲線 :math:`\fn{c}{[0, 1]}\RR^n,\ c(0) = \bm x,\ c(1) = \bm y = E_{\bm x}(\bm v)` から始める。
#. :math:`c(s) = E_{\bm x}(t(s)\bm v(s))` で :math:`s` を定義する。

   * :math:`t(s)` は :math:`s` について :math:`C^1` 級であり、
     :math:`t(s) = 0 \iff s = 0` を仮定しても最短性の議論に差し支えない。
   * :math:`\bm v(s)` は :math:`s \ne 0` において :math:`s` について :math:`C^1` 級。

#. 関数 :math:`H(t, s) = E_{\bm x}(t \bm v(s)) = F(1, \bm x, t\bm v(s)) = F(t, \bm x, \bm v(s))` を考える。

   * :math:`q(\bm v(s)) = g(\bm v(s)) = 1` とすると直接計算より
     :math:`\displaystyle \frac{\partial H}{\partial t} \perp \frac{\partial H}{\partial s}` がわかる。

#. :math:`\displaystyle \diff{c}{s} = \frac{\partial H}{\partial t}\diff{t}{s} + \frac{\partial H}{\partial s}.`
   であるから、
   :math:`\displaystyle \frac{\partial H}{\partial t} \perp \frac{\partial H}{\partial s}` ならば
   :math:`\displaystyle g\left(\frac{\partial H}{\partial t}, \frac{\partial H}{\partial s}\right) = 0.`

#. よって :math:`\displaystyle \sqrt{q\left(\diff{c}{s}\right)} \le \sqrt{q\left(\frac{\partial H}{\partial t} \frac{\partial H}{\partial s}\right)} = \sqrt{\left(\diff{t}{s}\right)^2} = \abs{\diff{t}{s}}.`
#. 積分して :math:`\displaystyle \int_0^1\sqrt{q\left(\diff{c}{s}\right)}\,\dd{s} \le \int_0^1 \abs{\diff{t}{s}}\,\dd{s} \le \abs{t(1) - t(0)}.`

以上により測地線は最短であることが示せた（らしい）。

.. _tsuboi05.7.4.2:

* 例 7.4.2: :ref:`例題 7.1.4 <tsuboi05.7.1.4>` のトーラス上のリーマン計量についての測地線の方程式

  * 以前書いた :math:`{}^t\!(D\Phi)D\Phi` はリーマン計量を意味していた。
  * 式変形がわかりにくいので、結局自分で計算することになる。
    ここでは :math:`\Gamma_{ij}^1,\ \Gamma_{ij}^2` をそれぞれ一行にまとめて記している。
    左辺はスカラーに見えるが、実は行列の :math:`(i, j)` 成分がこの式であるような行列であると読者側が了解しないといけない。

  * 各 :math:`\Gamma_{ij}^l\quad(l = 1, 2)` を計算する。
    :math:`g` が対角行列なので逆行列が計算しやすくて助かる。

  * 最終的に二階常微分方程式が得られるが、
    :math:`\displaystyle \mdiff{x_1}{2}{t}` は :math:`\displaystyle \diff{x_1}{t}\diff{x_2}{t}` の、
    :math:`\displaystyle \mdiff{x_2}{2}{t}` は :math:`\displaystyle \left(\diff{x_1}{t}\right)^2` の項からそれぞれなる。

    * 余裕があれば SymPy で計算させてみたい。

.. _tsuboi05.7.4.3:

* 問題 7.4.3: コンパクトリーマン多様体 :math:`M` の接束と :math:`M \times M` の対角集合の近傍は微分同相である

  仮定をまとめる：

  * :math:`\fnm{F}{TM}{M \times M}{T_xM}(x, E_x(X))` である。
    ただし :math:`X \in T_xM` である。

  * :math:`\Delta = \set{(x, x) \sth x \in M}.`

  * 写像 :math:`\fn{s_0}{M}TM` が `零切断 <http://mathworld.wolfram.com/ZeroSection.html>`__ である。
    つまり次の性質がある：
    :math:`s_0(x) = 0 \in T_xM.`

  :math:`F` は :math:`s_0` の像の近傍から対角集合 :math:`\Delta` の近傍への微分同相写像であることを証明する。

  * 接写像 :math:`\fn{F_*}{T_X TM}T(M \times M) = T_xM \times T_xM` を考える。

    * :math:`T_{s_0(x)}(TM) = T_x(s_0(M)) \times T_x(M) = T_xM \times T_xM.`
    * 次の二つの制限を考える：

      .. math::

         \begin{align*}
         (F_*)_{s_0(x)}|(T_x(s_0(M)) \times \zeroset) &= (\id_{T_xM}, 0)\\
         (F_*)_{s_0(x)}|(\zeroset \times T_x(s_0(M))) &= (0, \id_{T_xM}).
         \end{align*}

      ゆえに :math:`\displaystyle (F_*)_{s_0(x)} = \begin{pmatrix}\id_{T_xM} & 0\\0 & \id_{T_xM}\end{pmatrix}` である。

  * 逆写像定理により :math:`F` は :math:`s_0(M)` 上単射であることが言える。
  * そして :ref:`例題 4.3.1 <tsuboi05.4.3.1>` より
    :math:`F` は求める微分同相写像であると言える。

.. _tsuboi05.7.4.4:

* 問題 7.4.4: コンパクト連結リーマン多様体の微分同相 :math:`\fn{\Phi}{M}M` が
  :math:`C^1` 位相で恒等写像と十分近いのであれば、次のようなアイソトピー :math:`\Phi_t` が存在する：
  :math:`\Phi_0 = id_M,\ \Phi_1 = \Phi.`

  * :ref:`問題 7.4.3 <tsuboi05.7.4.3>` の結論を再利用したい。
    :math:`\id_M` のグラフが :math:`\Delta` であるので、部分集合
    :math:`\set{(x, \Phi(x)) \sth x \in M} \subset M \times M` は前問のように構成される
    :math:`F` が微分同相写像となるような :math:`\Delta` の近傍に含まれる。

  * :math:`\xi = F\inv(x, \Phi(x))` は :math:`M` 上のベクトル場である。
  * :math:`F` の局所的微分同相性のため、
    「:math:`F` が :math:`\id_M` に :math:`C^1` 位相で近いこと」と
    「:math:`\fn{\xi}{M}TM` が 0 に :math:`C^1` 位相で近いこと」は同値である。

  以上より :math:`\fn{\Phi_t}{M}M` を
  :math:`(x, \Phi_t(x)) = F(t\xi(x))` と定義すればよい。
