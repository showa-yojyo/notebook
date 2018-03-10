======================================================================
第 8 章 多様体上のベクトル場（後編）
======================================================================

.. contents:: ノート目次

.. _tsuboi05.8.4:

8.4 k-枠場（展開）
======================================================================
k-枠場
  多様体 :math:`M` 上の一次独立なベクトル場 k 個の組を意味する。
  :math:`0 \le k \le \dim M`

  * 例：二次元曲面 :math:`\Sigma_g\ (g \le 2)` 上には 1-枠場と 2-枠場のどちらも存在しない。
    一方、トーラス :math:`T^2` 上にはどちらも存在する。

  * n-枠場を持つ n 次元多様体を `平行可能化多様体 <http://mathworld.wolfram.com/Parallelizable.html>`__ と呼ぶ。

.. figure:: /_static/cd-topology-framebundle.png
   :align: center
   :alt: math.topology.framebundle
   :width: 524px
   :height: 341px
   :scale: 100%

2-枠場のある多様体 :math:`M` 上で :math:`[\xi_1, \xi_2] = 0` であれば
:math:`\RR^2` の :math:`M` への作用 :math:`(\varphi_1^{t_1} \circ \varphi_2^{t_2})(x)` を定義することで
:math:`\RR^2` 作用の軌道の族で :math:`M` を分割することができる。
このとき、軌道は :math:`M` の各点の近傍に対して二次元の共通部分を持つ。

* :math:`x \in M` を固定すると作用の接写像のランクが 2 である。
* 共通部分は高々可算個である。

これを 2 から k に拡張する。
一般に k 枠場 :math:`(\xi_1, \dotsc, \xi_k)` が :math:`[\xi_i, \xi_j] = 0` であるならば、
加法群 :math:`\RR^k` の :math:`M` への作用を次のように定義できて、
:math:`M` は k 次元の :math:`\RR^k` 作用の軌道に分割される。

.. math::

   \varphi_1^{t_1} \circ \dotsb \circ \varphi_k^{t_k} (x)

:math:`M` の各点の近傍 :math:`U` においてランク :math:`n - k` の写像
:math:`\fn{F}{U}\RR^{n - k}` が存在して、軌道と近傍の共通部分が
:math:`F` で決まる近傍の k 次元部分多様体の和集合となる。

.. _tsuboi05.8.4.1:

* 例 8.4.1: :math:`\RR^3` 上のベクトル場

  * :math:`f \in C^\infty(\RR^2).`
  * :math:`\displaystyle \xi_1 = \frac{\partial}{\partial x_1} + \frac{\partial f}{\partial x_1}\frac{\partial}{\partial x_3},`
    :math:`\displaystyle \xi_2 = \frac{\partial}{\partial x_2} + \frac{\partial f}{\partial x_2}\frac{\partial}{\partial x_3}.`
  * :math:`[\xi_1, \xi_2] = 0.`
  * :math:`h = x_3 - f(x_1, f_2)` が一定である点からなる曲面が :math:`\RR^2` 作用の軌道となる。

.. _tsuboi05.8.4.2:

* 例 8.4.2: ダメな例

  * :math:`\displaystyle \xi_1 = \frac{\partial}{\partial x_1} - x_2 \frac{\partial}{\partial x_3},`
    :math:`\displaystyle \xi_2 = \frac{\partial}{\partial x_2}.`

  * :math:`\because [\xi_1, \xi_2] = \dfrac{\partial}{\partial x_3}.`

`k 次元接平面場 or k 次元分布 <https://en.wikipedia.org/wiki/Distribution_(differential_geometry)>`__
  多様体 :math:`M` 上の k 次元接平面場に対して、各点の近傍ではその
  k 次元接平面場を張る k 枠場に取り替えられる。

.. _tsuboi05.8.4.3:

* 定理 8.4.3:
  :math:`\RR^n` の開集合 :math:`U` 上の k-枠場が :math:`U` の各点の近傍に対して
  :math:`[\xi_i, \xi_j]` が 0 となる k-枠場に取り替えられることは、
  :math:`[\xi_i, \xi_j]` が :math:`\xi_1, \dotsc, \xi_k` の張る k-枠場に値を持つことと同値である。

  * 証明がよくわからない。

  * :math:`(\xi_1, \dotsc, \xi_k)` と :math:`(\eta_1, \dotsc, \eta_k)` が同じ接平面場を与えるならば
    :math:`\exists \fn{a_{ij}}{U}GL_k(\RR)\quad\text{s.t. } \eta_i = \sum_{j = 1}^k a_{ij}\xi_j`
    を示す。

    * 一方の括弧積を計算することで、他方の括弧積と同時に接平面場に値を持つことがわかる：

      .. math::

         \begin{align*}
         [\eta_l, \eta_m]
         &= \left[\sum_{i = 1}^k a_{li}\xi_i, \sum_{k = 1}^k a_{mi}\xi_i\right]\\
         &= \sum_{i, j} a_{li}\xi_j(a_{mj})\xi_j - \sum_{i,j} a_{mj}(\xi_j a_{li})\xi_i + \sum_{i,j}a_{li}a_{mj}[\xi_i, \xi_j].
         \end{align*}

  * 十分：適当に座標を取り替えて写像 :math:`\fn{p}{\RR^n}\RR^k` を
    :math:`p(\bm x) = (x_1, \dotsc, x_k)` で定義する。

    * 点の近傍上 :math:`p_*` を接平面場に制限した接写像は何かとの同型を与える。
    * その次の「
      :math:`V` 上の k 枠場 :math:`(\eta_1, \dotsc, \eta_k)` を
      :math:`p_* \eta_i = \dfrac{\partial}{\partial x_i}` となるようにとれる」
      がわかりにくい。
    * :math:`[\eta_l, \eta_m]` が値を持てば
      :math:`p_*[\eta_l, \eta_m] = \left[\dfrac{\partial}{\partial x_i}, \dfrac{\partial}{\partial x_j}\right] = 0`
      より 0 が値である。

* フローの可換性の成立だけで :math:`U` 内の「軌道」が :math:`F` によって定まる
  :math:`U` の k 次元部分多様体となるといえる。

  * 「軌道」と書いたが、
    :math:`x` において k 次元接平面場は :math:`T_x(F\inv(F(x)))` と一致する。

.. _tsuboi05.8.4.4:

* 定理 8.4.4: `フロベニウス <https://en.wikipedia.org/wiki/Frobenius_theorem_(differential_topology)>`__

  * :math:`[\xi_i, \xi_j]` が k 次元接平面場に値を持つということを
    `（完全）積分可能条件 <https://en.wikipedia.org/wiki/Integrability_conditions_for_differential_systems>`__ という。

  * :math:`F_V\inv(F_V(x)),\ T_x(F_V\inv(F_V(x))) \subset T_xM` と
    :math:`x` における k 次元接平面場が一致する。

  * （極大）積分多様体
    or `葉 <http://mathworld.wolfram.com/FoliationLeaf.html>`__

  * 共通部分できれいに貼り合わさる。
  * 「正則とは限らない」部分多様体とは？
  * `葉層 <http://mathworld.wolfram.com/Foliation.html>`__ 構造（本書図 8.2 参照）

8.5 勾配ベクトル場
======================================================================
多様体上の微分可能関数 :math:`f \in C^1(M)` とベクトル場 :math:`X` と
リーマン計量 :math:`g` に対して、ベクトル場 :math:`\grad f` を次で定義する：

.. math::

   \begin{align*}
   Xf &= g(X, \grad f),\text{ or }\\
   \grad f &= \sum_{i = 1}^n \sum_{j = 1}^n g^{ij} \frac{\partial f}{\partial x_j}\frac{\partial}{\partial x_i}.
   \end{align*}

* :math:`f` の等位面が部分多様体であるとき、
  :math:`f\inv(a)` と :math:`\grad f` は直交する。
  なぜならば :math:`f\inv(a)` の接ベクトル :math:`v` を取ると
  :math:`f_*v = 0` であって :math:`g(v, \grad f) = 0` が成り立つ。

  .. math::

     f_*v = 0 \implies g(v, \grad f) = \sum \frac{\partial}{\partial x_i} v_i = 0

* :math:`\grad f` が生成するフローを gradient flow と呼ぶ。

.. _tsuboi05.8.5.1:

* 例 8.5.1: 球面上の微分可能関数に対する勾配ベクトル場

  * :math:`S^2` のパラメーター表示を
    :math:`(x, y, z) = (\cos\theta\cos\cos\varphi, \sin\theta\cos\varphi, \sin\varphi)` とおく。

  * ベクトル場の基底を :math:`\dfrac{\partial}{\partial \theta}, \dfrac{\partial}{\partial \varphi}` ととる。
  * リーマン計量は :math:`\displaystyle g = \begin{pmatrix}\cos^2\varphi & 0\\0 & 1\end{pmatrix}` と書ける。
  * 次のようにおいて :math:`g(\grad f, X)` と :math:`X(f)` をそれぞれ計算する：

    .. math::

       \begin{align*}
       \grad f &= a\frac{\partial}{\partial \theta} + b\frac{\partial}{\partial \varphi},\\
       X &= u\frac{\partial}{\partial \theta} + v\frac{\partial}{\partial \varphi}.
       \end{align*}

    計算の結果 :math:`\grad f = \cos\varphi \dfrac{\partial}{\partial \varphi}` となる。
    直交座標系で書くと :math:`-xz\dfrac{\partial}{\partial x} - yz\dfrac{\partial}{\partial y} + (1 - z^2)\dfrac{\partial}{\partial z}.`

.. _tsuboi05.8.5.2:

* 例題 8.5.2

  #. :math:`f(x, y) = x^3 - x + y^2` のグラフを描け。

     * フローが等位線と直交するように描くのが鉄則。
     * :math:`X = \dfrac{\partial f}{\partial x}\dfrac{\partial}{\partial x} + \dfrac{\partial f}{\partial y}\dfrac{\partial}{\partial y}` は
       ユークリッド計量についての :math:`f` の勾配ベクトル場である。
     * :math:`Xf = \left(\dfrac{\partial f}{\partial x}\right)^2 + \left(\dfrac{\partial f}{\partial y}\right)^2 \le 0` より
       非減少である。

  #. :math:`\displaystyle \diff{x}{t} = \frac{\partial}{\partial x},\ \diff{y}{t} = \frac{\partial}{\partial y}` の解曲線を求めろ。

.. _tsuboi05.8.5.3:

* 問題 8.5.3

  :math:`\grad f \ne 0` なる点で定義されるベクトル場
  :math:`\displaystyle Y = \frac{\grad f}{g(\grad f, \grad f)}` およびその解曲線
  :math:`c(t)` について。

  定義域では :math:`f(c(t_0 + t)) - f(c(t_0)) = t.`
  :math:`Yf = 1` より :math:`\displaystyle \diff{(f \circ \varphi_t)(x)}{t} = (Yf)(\varphi_t(x)) = 1.`
  :math:`\therefore\ f(\varphi_t(x)) - f(x) = t.`

* モース関数について

  * 臨界点近傍で :math:`\displaystyle f = \sum_{i = 1}^\lambda x_i^2 + \sum_{i = \lambda + 1}^n x_i^2.`
  * 1 の分割の技法を使ってリーマン計量 :math:`g` を :math:`g_{ij} = \delta_{ij}` となるように定める。
    このとき勾配ベクトルは次のようになる：

    .. math::

       \grad f = -2 \sum_{i = 1}^\lambda x_i \frac{\partial}{\partial x_i}  + 2 \sum_{i = \lambda + 1}^n x_i\frac{\partial}{\partial x_i}.

  * 解曲線は :math:`(\mathrm e^{-2t}x_1, \dotsc, \mathrm e^{-2t}x_{\lambda}, \mathrm e^{2t}x_{\lambda + 1}, \dotsc, \mathrm e^{2t}x_n).`
  * :math:`f\inv(x^0 - \eps)` と :math:`f\inv(x^0 + \eps)` の間には二枚の平面を除いて対応が付いている。

.. _tsuboi05.8.5.4:

* 例 8.5.4: トーラス :math:`f(x, y) = a(2 + \cos y)\cos x + c \sin y`

  * :math:`\RR^3` 内のトーラス (p. 24) として考える。
  * :math:`\displaystyle Df = \begin{pmatrix}-a(2 + \cos y)\sin x & -a \sin y\cos x + a \cos y\end{pmatrix}.`
  * :math:`\displaystyle g = \begin{pmatrix}(2 + \cos y)^2 & 0\\0 & 1\end{pmatrix}.`
    (cf. :ref:`例題 7.1.4 <tsuboi05.7.1.4>`)
  * :math:`\displaystyle g\inv = \begin{pmatrix}\dfrac{1}{(2 + \cos y)^2} & 0\\0 & 1\end{pmatrix}.`

  定義に従って勾配ベクトル場を計算するのは容易い：

  .. math::

     \grad f = -\frac{a\sin x}{2 + \cos y}\frac{\partial}{\partial x} + (-a \sin y\cos x + c\cos y)\frac{\partial}{\partial y}.

8.6 ファイバー束（展開）
======================================================================

ここでファイバー束およびそれに関係する簡単な概念のいくつかを図式化したものを次に示す。

.. figure:: /_static/cd-topology-bundles.png
   :align: center
   :alt: math.topology.bundles
   :width: 657px
   :height: 425px
   :scale: 100%

.. _tsuboi05.8.6.1:

* 例題 8.6.1: ファイブレーション定理

  * :math:`M, N` をコンパクト連結多様体で :math:`\dim M > \dim N` であり、
  * :math:`F \in C^\infty(M, N)` が
  * :math:`\forall x \in M, \fn{F_*}{T_xM}T_{F(x)}N` が全射である

  とする。このとき :math:`\forall y \in N` に次のような近傍 :math:`V_y \owns y` と
  同相写像 :math:`h` が存在する：

  * :math:`\fn{h}{F\inv(V_y)}V_y \times F\inv(y),`
  * :math:`F = \operatorname{pr}_1 \circ h,`
  * :math:`\operatorname{pr_1}` は第一成分への射影。

  証明：

  * リーマン計量を :math:`g` とする。
  * 接空間の部分集合 :math:`\nu_x = \set{v \in T_x(M) \sth \forall w \in T_x(F\inv(F(x))), g(v, w) = 0}` を定義する。

    * :math:`F_*|\nu_x` が同型写像になるという性質がある。

  * ある一点 :math:`y^0 \in N` の開被覆として :math:`(V, \psi = (y_1, \dotsc, y_n)),\ \psi(y^0) = (0, \dotsc, 0)` をとる。
  * 近傍 :math:`W \owns y^0` を :math:`\closure{W} \subset V` となるようにとる。
  * :math:`C^\infty` 級関数 :math:`\fn{\mu}{N}\RR` を次のように定義する：

    * :math:`\supp \mu = V,`
    * :math:`y \in \closure{W} \implies \mu(y) = 1.`

  * :math:`N` 上の :math:`C^\infty` 級ベクトル場 :math:`\xi_i = \mu\dfrac{\partial}{\partial y_i}` を考える。
  * また :math:`\bm a \in \RR^n` として
    :math:`\xi_{\bm a} = \sum_{i = 1}^n a_i\xi_i` およびそれが生成するフロー
    :math:`\Psi_{\bm a}^t` を考える。

    これはある :math:`\eps > 0` について次のような性質がある：

    .. math::

       t\norm{\bm a} < \eps \implies \Psi_{\bm a}^t(y^0) = \psi\inv(t\bm a).

  * :math:`F_*|\nu_x` は同型なので :math:`\xi_i` に対して
    :math:`M` 上のベクトル場 :math:`\overset{\sim}{\xi_i}` を次が成り立つように一意的に取れる：

    .. math::

       F_* \overset{\sim}{\xi_i} = \xi_i,
       \
       \overset{\sim}{\xi_i}(x) \in \nu_x.

    * この状況をファイバー束の接続という。
    * :math:`\overset{\sim}{\xi_i}` を :math:`\xi_i` の
      `持ち上げ <http://mathworld.wolfram.com/Lift.html>`__ という。

  * :math:`\displaystyle \overset{\sim}{\xi}_{\bm a} = \sum_{i = 1}^n a_i \overset{\sim}{\xi_i}` とおくと
    :math:`F_* \overset{\sim}{\xi}_{\bm a} = \overset{\sim}{\xi}_{\bm a}.`

    ゆえに :ref:`例題 6.5.5 <tsuboi05.6.5.5>` のベクトル場の射影の性質により、
    :math:`\overset{\sim}{\xi}_{\bm a}` のフロー :math:`\Phi_{\bm a}^t` について次が成り立つ：

    .. math::

       F \circ \Phi_{\bm a}^t = \Psi_{\bm a}^t \circ F.

  * 写像 :math:`\fn{H}{\set{\bm a \in \RR^n \sth \norm{\bm a} < \eps} \times F\inv(y^0)}M` を
    :math:`H(\bm a, x) = \Phi_{\bm a}^1(x)` で定義する。

    * :ref:`注意 6.3.6 <tsuboi05.6.3.6>` より :math:`H` は :math:`C^\infty` 級である。
    * :math:`F(H(\bm a, x)) = \Psi_{\bm a}^1(F(x)) = \Psi_{\bm a}^1(y^0) = \psi\inv(a).`
    * :math:`H` の逆写像は :math:`x \longmapsto (\psi(F(x)), \Phi_{\psi(F(x))}(x))` で与えられる。

    よって写像 :math:`H` は微分同相写像である。

`ファイバー束 <http://mathworld.wolfram.com/FiberBundle.html>`__
  位相空間 :math:`E, B` と連続写像 :math:`\fn{p}{E}B` について
  次が成り立つ位相空間 :math:`F` が存在すれば、これを `ファイバー <http://mathworld.wolfram.com/Fiber.html>`__ といい、
  :math:`p` をファイバー束という：

  .. math::

     \forall b \in B, \exists U_b \owns b \quad \text{ s.t. }
     \exists \fn{h}{p\inv(U_b)}U_b \times F,\
     \operatorname{pr}_1 \circ h = p.

平坦な接続
  :ref:`例題 8.6.1 <tsuboi05.8.6.1>` における :math:`[\overset{\sim}{\xi}, \overset{\sim}{\eta}]` を考える。

  * 持ち上げによってベクトル場 :math:`[\overset{\sim}{\xi}, \overset{\sim}{\eta}]` は
    :math:`F_*[\overset{\sim}{\xi}, \overset{\sim}{\eta}] = [F_*\overset{\sim}{\xi}, F_*\overset{\sim}{\eta}] = [\xi, \eta].`

    * 最初と最後の等号はそれぞれ :ref:`例題 8.2.3 <tsuboi05.8.2.3>` と持ち上げによる。

  * 特に座標近傍上で :math:`\displaystyle \xi = \zeta_i = \frac{\partial}{\partial x_i}` をとれば、
    :math:`[\zeta_i, \zeta_j] = 0` なので
    :math:`[\overset{\sim}{\zeta_i}, \overset{\sim}{\zeta_j}]` は
    ファイバーの方向のベクトル場である。

  * さらに :math:`\forall \zeta_i, \zeta_j,\ [\overset{\sim}{\zeta_i}, \overset{\sim}{\zeta_j}] = 0`
    のときには接続が平坦な接続であるという。

    * 各 :math:`\zeta_i` が生成するフローを :math:`\varphi_i^{t_i}` とすると、各フローは局所的には可換である。
    * :math:`x \in M` と 0 近傍の点 :math:`(t_1, \dotsc, t_n)` に対し、
      :math:`\Phi(t_1, \dotsc, t_n)(x) = \varphi_1^{t_1} \circ \dotsb \circ \varphi_n^{t_n}(x)` とおく。

      #. :math:`\psi(F(\Phi(t_1, \dotsc, t_n)))(x) = \psi(F(x)) + (t_1, \dotsc, t_n),`
      #. :math:`\Phi(s_1, \dotsc, s_n) \circ \Phi(t_1, \dotsc, t_n)(x) = \Phi(s_1 + t_1, \dotsc, s_n + t_n)(x).`

    * 微分同相写像 :math:`x \longmapsto (F(x), \Phi(\psi(y) - \psi(F(x)))(x))` に関する
      :math:`U_y \times \set{z}` の逆像は部分多様体のように貼り合わされる。

* ファイバーがリー群であるようなファイバー束を考えることができる。

  * :math:`G` がファイバーを左または右から :math:`M` に作用している。
  * この作用について不変なファイバーに対して横断的な接平面場を考えると、
    持ち上げが :math:`G` の作用で不変となるような接続がある。
    このとき :math:`[\overset{\sim}{\xi}, \overset{\sim}{\eta}]` も不変ベクトル場であり、
    :math:`G` のリー代数 :math:`\mathfrak g` の元である。

* n 次元リーマン多様体の :math:`\operatorname{Fr}M` はファイバーが :math:`O(n)` であるような
  :math:`M` 上のファイバー束となっている。
* `レビチビタ接続 <http://mathworld.wolfram.com/Levi-CivitaConnection.html>`__ とはこのファイバー束の接続である。

8.7 第 8 章の問題の回答
======================================================================
ノートは以上に記した。
