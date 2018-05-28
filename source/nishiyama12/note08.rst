======================================================================
幾何学と不変量 読書ノート 8/10
======================================================================

:doc:`note07` からの続き。

.. contents:: ノート目次

第 8 章 軌道空間の幾何的構造
======================================================================

8.1 等質空間
----------------------------------------------------------------------
* 定義 8.1: `推移的な作用 <http://mathworld.wolfram.com/TransitiveGroupAction.html>`__

  * 群 :math:`G` が空間 :math:`X` への推移的作用であるとは、
    :math:`\forall x, y \in X, \exists g \in G \quad\text{s.t. } gx = y` であることを言う。
  * :math:`X` 自身が一つの :math:`G` 軌道である。
  * :math:`\Omega_{G}(X)` と :math:`X/G` は一点からなる。

* 定義 8.2: `固定部分群 <http://mathworld.wolfram.com/IsotropyGroup.html>`__

  * :math:`G_x = \set{g \in G \sth gx = x}` を :math:`x \in X` の固定部分群という。
  * :math:`G_x` による :math:`G` への右移動による作用では
    :math:`G/G_x = \set{aG_x \sth a \in G}` は右剰余類の空間である。
    :math:`G = \bigsqcup aG_x (a \in G/G_x)` を右剰余類を用いた軌道分解という。

* 定理 8.3: 連続な全単射 :math:`\fn{\mu}{G/G_x}X` の存在

  * ここで :math:`G` は連続群、
    :math:`X` は位相空間、作用は連続かつ推移的であるものと仮定する。

  * 証明としては :math:`\mu(gG_x) = gx` とすればこれが次のことを満たせばよい：

    * :math:`\mu` が well-defined である。
    * :math:`\mu` が全単射である。

      * 全射であることを示すのに作用が推移的であることを必要とする。

    * :math:`\mu` が連続である。

      * 商写像 :math:`\fn{\pi}{G}G/G_x` を考えて :math:`\mu` との合成写像を考える。
        開集合 :math:`U \subset X` の逆像が開集合であることを示すのに、
        作用が連続であることを必要とする。

* 例 8.4: 上記の連続な全単射は一般には微分同相とはならない。

* 定義 8.5: `等質空間 <http://mathworld.wolfram.com/HomogeneousSpace.html>`__

  * 連続群 :math:`G` の閉部分群 :math:`H` による商空間 :math:`G/H` のこと。

.. _nishiyama12.8.6:

* 定理 8.6: ある条件が満たされていれば :math:`G/G_x \cong X`

  * 証明なし。

* 例 8.7: :math:`\mathit{SO}_3(\RR) / \mathit{SO}_2(\RR) \cong S^2`

  * :math:`G = \mathit{SO}_3(\RR)` の :math:`S^2 \subset \RR^3` への作用。
  * 球面の「北極」の固定部分群を求めると、これが :math:`G = \mathit{SO}_2(\RR)` と同型であることがわかるので、
    先の定理より結論できる。

.. _nishiyama12.8.8:

* 例 8.8: :math:`\RR/\ZZ \cong S^1`,
  :math:`\RR^2/\ZZ^2 \cong (\RR/\ZZ) \times (\RR/\ZZ) \cong S^1 \times S^1 \cong T^2`

  * 実数を加法群とみなして :math:`e^{2 \pi i \xi} (\xi \in \RR)` の乗算によって作用している。
  * 1 の固定部分群が整数である。
  * トーラスも固定部分群を :math:`\set{(2 \pi n, 2 \pi m) \sth n, m \in \ZZ}` とすれば
    :math:`\RR^2/\ZZ^2 \cong S^1 \times S^1`

* 例 8.9: 曲面 :math:`x^2 + y^2 - z^2 = k`

  * :math:`k > 0` ならば一葉双曲面（連結）
  * :math:`k < 0` ならばニ葉双曲面
  * :math:`G = O_{21}(\RR)` が自然に作用している。
  * :math:`Q = {}^t\!\xi \diag(1, 1, -1) \xi` とすると :math:`Q(g \xi) = Q(\xi)` なので、
    この二次形式は :math:`G` の作用による不変式。つまり双曲面上の点は双曲面上の点に移る。

  * :math:`k = 1` のとき（以下、曲面を :math:`X_1` とする）

    * :math:`O_{21}(\RR)` は :math:`X_1` に推移的に作用する。
    * スペースの都合でここには成分を記せないが、
      :math:`u_{\theta} \in O_{21}(\RR)` と :math:`a_t \in O_{2}(\RR)` で移る。

      * 後者のようなものを双極回転という。
        断面の双曲線に沿った動き。

    * :math:`X_1` のパラメーター表示が得られた。
    * この後、点 :math:`(1, 0, 0)` に関する固定部分群を求めて、
      :ref:`定理 8.6 <nishiyama12.8.6>` を用いて
      :math:`X_1 \cong O_{21}(\RR) / O_{11}(\RR)` を導く。
      :math:`I_{11} = \diag(1, -1)`

    * 結論: 一葉双曲面は連結であり、唯一の軌道からなる。

  * :math:`k = -1` のときは :math:`X_{-1} \cong O_{21}(\RR) / O_2(\RR)` が成り立つ。
    連結ではなく、唯一の軌道からなる。

  * :math:`k = 0` のときは見てくれどおり
    :math:`\zeroset \sqcup X_0 \minuszero` だとしか言えない。

* 演習 8.10: 実は :math:`a_t \in SO_{2,1}(\RR)` が成り立つ：

  .. math::

     \begin{align*}
     a_t =
     \begin{pmatrix}
     \cosh t & 0 & \sinh t\\
     0 & 1 & 0\\
     \sinh t & 0 & \cosh t
     \end{pmatrix}
     \in O_{2,1}(\RR).
     \end{align*}

* 演習 8.11: :math:`X_1` のパラメーター表示

  :math:`x = \cos \theta \cosh t, y = \sin \theta \cosh t, z = \sinh t,\ 0 \le \theta < 2\pi, t \in \RR`

* 系 8.12: :math:`\mathbb P^2(\RR) \cong O_3(\RR)/(O_2(\RR) \times O_1(\RR))`

8.2 同伴ファイバー束
----------------------------------------------------------------------
`同伴するファイバー束 <http://mathworld.wolfram.com/AssociatedFiberBundle.html>`__
  G, H, W をそれぞれ群、G の部分群、H が作用する空間とする。
  :math:`G \times_{H} W` を :math:`(G \times W) / H` で定義し、
  それを同伴するファイバー束と呼ぶ。

  * 集合としては軌道空間と同じ。:math:`G \times_{H} W = \Omega_{H}(G \times W)`
  * 右辺の直積には同値関係 :math:`(g, w) \sim (gh\inv, hw)` が入る。
    :math:`G \times_{H} W = \set{[g, w] \sth (g, w) \in G \times W} = G \times W / \sim`

ファイバー束から底空間への射影
  写像 :math:`[g, w] \longmapsto gH \in G/H` とすると、この逆像は部分群が作用する空間と同型になる。

底空間
  商群 :math:`G/H` のことをそう呼ぶ。

ファイバー
  空間 W のことをそう呼ぶ。

* 例 8.13

  * :math:`S^2` は :math:`\mathit{SO}_3(\RR)` の等質空間だ。
  * :math:`S^2 \cong \mathit{SO}_3(\RR)/\mathit{SO}_2(\RR)` であった（復習）。
  * :math:`H = \mathit{SO}_2(\RR)` は :math:`W = \RR^2` に回転として作用するので、
    同伴ファイバー束 :math:`G \times_{H} W` を考える。

    * 底空間は :math:`S^2` だ。
    * ファイバーは :math:`\RR^2` のファイバー束（接束という）。

* 例 8.14: :math:`W = \RR^2 \subset \RR^3` を xy 平面とし、
  :math:`H = \mathit{SO}_2(\RR)` を z 軸周りの回転で :math:`G = \mathit{SO}_3(\RR)` の部分群とする。

  * このとき同伴ファイバー束から 3 次元空間への射影を
    :math:`[g, w] \longmapsto g(\bm e_3 + w)` で定めると、

    * well-defined かつ
    * 値は :math:`g\bm e_3` における接平面であり、
    * 同型写像を与える。

  * 同伴ファイバー束と球面の接束 :math:`TS^2` は同一視できる。

8.3 二次曲線と直線の配置問題
----------------------------------------------------------------------
次のものはしばらく使う記号と用語：

* :math:`Sym_3^\circ (\RR)`: 正則な :math:`Sym_3(\RR)` の行列全て。
* :math:`X = Sym_3(\RR) \times (\RR^3 \minuszero)` を考える対象の空間とし、
* :math:`\varphi(g)(Q, w) = (gQ{}^t\!g, gw),\ g \in G, (Q, w) \in X` を作用とする。

  * テーマ別に :math:`G` を変える。

軌道空間 :math:`\Omega_G(X)` を求めるには :math:`G(\diag(\pm 1, \pm 1, \pm 1), w)` 形の軌道を求めれば十分。

* 符号数 :math:`(p, q)` の :math:`Sym_3(\RR)` の部分を :math:`Sym_3^{(p, q)}(\RR)` で表す。

  * :math:`Sym_3^+(\RR) := Sym_3^{(3, 0)}(\RR)` の元を正定値対称行列、
  * :math:`Sym_3^-(\RR) := Sym_3^{(0, 3)}(\RR)` の元を
    `負定値対称行列 <http://mathworld.wolfram.com/NegativeDefiniteMatrix.html>`__ と呼ぶ。

:math:`\displaystyle Sym_3^\circ (\RR) = \bigsqcup_{p + q = 3} Sym_3^{(p,\ q)}(\RR)` である。

8.3.1 直交群の軌道
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* 補題 8.15: 例 7.3 のおさらい

  * :math:`X` は 9 次元の空間で、軌道 :math:`G(E, re_1)` はその中で 8 次元の超曲面の一部となっている。

* 定理 8.16: :math:`G = GL_3(\RR)` の :math:`X` への作用

  * :math:`K = O_3(\RR)` とおく。

  * 点 :math:`(\diag(1, 1, 1), r \bm e_1) \in X` の軌道 :math:`G(\diag(1, 1, 1), r \bm e_1)` について
    同型 :math:`G(\diag(1, 1, 1), r \bm e_1) \cong G \times_K S_r` が成り立つ。

    * 右辺は :math:`G/K \cong Sym_3^+(\RR)` 上の半径 :math:`r` の球面
      :math:`S_r` をファイバーとする同伴ファイバー束を表す。

  * :math:`\dim G(\diag(1, 1, 1), r\bm e_1) = \dim G/K + \dim S_r = 6 + 2 = 8`
  * 証明は写像 :math:`\Psi([g, w]) = (g{}^t\!g, gw)` について次を示す：

    #. :math:`\Psi` が well-defind であること
    #. :math:`\Psi` が全単射であること
    #. :math:`\Psi` が微分同相であること（接空間のチェック）

8.3.2 不定値直交群の場合
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
不定値二次形式 :math:`Q(w) = x^2 + y^2 - z^2 = {}^t\!w \diag(1, 1, -1) w = 0` に関する
軌道が :math:`G(\diag(1, 1, -1), w)` の形のものを考える。

* :math:`H = O_{2, 1}(\RR)` によって :math:`w \in \RR^3 \minuszero` を動かすことによって
  表 (8.7) を得る。

* 定理 8.17: :math:`Hyp_k := \set{[x : y : z] \sth x^2 + y^2 - z^2 = k}` とおくと次が成り立つ。

  .. math::

     \begin{align*}
     G((\diag(1, 1, -1), r \bm e_1)    & \cong G \times_H Hyp_{r^2}\\
     G((\diag(1, 1, -1), r + \bm e_3) & \cong G \times_H Hyp_0\\
     G((\diag(1, 1, -1), r \bm e_3)    & \cong G \times_H Hyp_{-r^2}
     \end{align*}

  上から一葉双曲面、開零錐、ニ葉双曲面。

残る議論は :math:`Q` の代わりに :math:`-Q` を考えればよい。

8.3.3 二次曲線と直線
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
:math:`Q(\xi) = 0` と直線 :math:`w \cdot \xi = 0\ (w \in \RR^3 \minuszero)` を考える。

* 考えるべき作用は :math:`\varphi(g, s, t)(Q, w) = (sgQ{}^t\!g, tgw),\ g \in G, s, t \in \RR^\times` である。
  ここで :math:`G_1 = G \times \RR \times \RR` とおく。

  * 先ほど言ったように正定値か符号数 :math:`(2, 1)` の :math:`Q` だけを考えればよい。
    さらに正定値の場合は二次曲線は（実数上では）空集合になるので除外する。

  * :math:`G_1` の軌道の代表元はやはり
    :math:`G(\diag(1, 1, -1), r \bm e_1),\ G((\diag(1, 1, -1), r + \bm e_3),\ G((\diag(1, 1, -1), r\bm e_3)` しかない。
    それぞれ：

    * 直線と二点で交わる、
    * 直線と接する、
    * 直線と交わらない、

    となる。

8.4 円とトーラス
----------------------------------------------------------------------
* :ref:`例 8.8 <nishiyama12.8.8>` をさらに考える。
* :math:`\ZZ` や :math:`\ZZ^2` のような群を格子群という。

8.4.1 円と三角関数
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
:math:`G = \ZZ,\ X = \RR, \varphi(m)x = x + 2\pi m` とする。
当然ながら :math:`Gx = \set{x + 2\pi m \sth m \in \ZZ}` であり、前に述べたように :math:`\RR/\ZZ \cong S^1` である。

* 商写像 :math:`\fn{p}{\RR}\RR/2\pi \ZZ \cong S^1` を :math:`p(x) = (\cos x, \sin x)` で定める。
* 関数 :math:`\cos x` や :math:`\sin x` は :math:`\RR` 上の :math:`\ZZ` 不変な関数であると言っている。

* 定理 8.18: `フーリエ級数 <http://mathworld.wolfram.com/FourierSeries.html>`__ 定理

  * :math:`f(x)` は :math:`\RR` 上の :math:`\ZZ` 不変な :math:`C^2` 級関数であると仮定しているが、
    級数の絶対収束性を要求しなければ、有界変動の連続関数であればよい。

    * フーリエ級数やルベーグ積分の教科書を参照。

  * 関数 :math:`\cos x` や :math:`\sin x` は :math:`G` 不変式の生成元だと言っている。

:math:`\dfrac{1}{\sin x}` の部分分数分解や
:math:`\sin x` の無限乗積展開に :math:`G` の作用が表れる。

8.4.2 トーラスと楕円関数
----------------------------------------------------------------------
これまでの議論における :math:`\RR^2` と :math:`\ZZ^2` をそれぞれ
:math:`\CC` と :math:`L = L(\omega_1, \omega_2) = \set{m\omega_1 + n\omega_2 \sth m, n \in \ZZ}` に置き換えて考える。

ただし :math:`\displaystyle \frac{\omega_1}{\omega_2} \notin \RR,\ \frac{\omega_1}{\omega_2} \in \mathfrak H` となるように複素数二つを取る。

* :math:`(L, +)` は群であり、加法群 :math:`\ZZ` と同型。
* :math:`(L, +) \subset (\CC, +)` は部分群。
* :math:`T = T(\omega_1, \omega_2) = \CC/L` は

  * 位相空間としてはトーラスであり、
  * 加法群であり、
  * 複素多様体である。

* トーラスは楕円曲線と同型である。これを示すのに複素平面上で :math:`L` 不変な関数を構成したい。
  `次の関数 <http://mathworld.wolfram.com/WeierstrassEllipticFunction.html>`__ について考察する：

  .. math::

     \wp(z) = \frac{1}{z^2} + \sum_{\omega \in L \minuszero}\left(\frac{1}{(z + \omega)^2} - \frac{1}{\omega^2}\right).

  これは :math:`z \notin L` において絶対広義一様収束する。

* 定理 8.19: 関数 :math:`\wp` の性質

  * :math:`\wp` は :math:`\CC` 上の :math:`L` 不変な有理型関数である。
  * 極は :math:`L` にあって、
  * どの極も 2 位である。

  証明としては、単に与式を微分すればよい。絶対収束性から項別微分できて

  .. math::

     \wp'(z) = -2 \sum_{\omega \in L}\frac{1}{(z + \omega)^3}.

  * まずは :math:`z = 0` が 2 位の極であることがわかる。
  * :math:`\wp'(z + \omega) = \wp'(\omega)\quad(\omega \in L)` により
    :math:`\wp(z + \omega) - \wp(z)` が定数であることが言える。

* 補題 8.20: 関数 :math:`\wp` は偶関数

  * :math:`-L = L` が効く。
    :math:`\wp(z + \omega_1) = \wp(z + \omega_2) = \wp(z)` が言える。
    :math:`\omega_1, \omega_2` が :math:`L` の生成元であるので :math:`\forall \omega \in L,\ \wp(z + \omega) = \wp(z).`

  * 先ほど :math:`z = 0` が 2 位の極であることがわかったので、これを :math:`L` で写した
    :math:`\forall \omega \in L` も同様。

  * 導関数 :math:`\wp'(z)` も :math:`L` 不変な有理型関数である。

* 定理 8.21

  .. math::

     \begin{gather*}
     \wp'(z)^2 = 4 \wp(z)^3 - g_2 \wp(z) - g_3,\quad
         g_2 = 60\!\sum_{\omega \in L \minuszero} \omega^{-4},\ 
         g_3 = 140\!\sum_{\omega \in L \minuszero} \omega^{-6}.
     \end{gather*}

  証明はテイラー展開を考える。
  左辺マイナス右辺を評価すると、:math:`L` 不変性と全平面で有界であることからこれが定数となることが言える。
  原点に注目すると左辺マイナス右辺はゼロであることが結論できる。

写像 :math:`\fn{R}{\CC}\CC^2` を :math:`R(z) = (\wp(z), \wp'(z))` で定義すると、
これは :math:`L` 不変ではあるのだが、:math:`\wp` の極が :math:`\infty` となる問題があるのでそのままでは使えない。
代わりに写像 :math:`\fn{E}{\CC \setminus L}\mathbb P^2(\CC)`, :math:`E(z) = [\wp(z), \wp'(z), 1]` を考える。

* :math:`E(z) = [z^3 \wp(z), z^3\wp'(z), z^3] \to [0 : -2 : 0] = [0 : 1 : 0] (z \to 0)` ゆえ（各成分を定数倍した）、
  :math:`E(0) = [0 : 1 : 0]` と定義する。

* これで商写像 :math:`\fn{E}{\CC / L}\overset{\sim}{\mathscr C} (zy^2 = 4x^3 - g_2xz^2 - g_3z^3)` が定義できた。

  * この :math:`z = 1` における曲線を `楕円曲線 <http://mathworld.wolfram.com/EllipticCurve.html>`__ と言う。

* 定理 8.22: :math:`\overset{\sim}{\mathscr C} \cong \CC/L`, 楕円曲線は群である、等々。
* 演習 8.23: 積分

  * :math:`f(z)` を :math:`L` 不変な有理型関数、
  * :math:`\omega_1, \omega_2` が生成する平行四辺形の周を
    :math:`\eps` だけずらした閉曲線を :math:`C_\eps`

  とする。このとき :math:`C_\eps` が :math:`f(z)` の極を含まなければ、
  この閉曲線に沿った関数の積分値はゼロとなる。

* 演習 8.24: 同じ状況で、閉曲線が囲む領域内で :math:`f(z) = c` となる点の個数は位数分の重複を込めて
  領域内の極の個数と等しい。

  * 閉曲線上では :math:`f(z) \ne c` を仮定する。
  * 偏角の原理を用いる。

* 演習 8.25: 分離

  * :math:`(\wp(z), \wp'(z))` は上記閉曲線内部の点をすべて分離する。すなわち商写像は一対一である。

* 演習 8.26: `リーマン球面 <http://mathworld.wolfram.com/RiemannSphere.html>`__

  * :math:`\sqrt{4z^3 - g_2z - g_3}` はリーマン球面上で 4 つの分岐点があり、
    `リーマン面 <http://mathworld.wolfram.com/RiemannSurface.html>`__ はトーラスになる。

* 演習 8.27: 楕円積分

  * 有理関数 :math:`R(x, y)` について積分 :math:`\displaystyle \int R(x, \sqrt{4x^3 - g_2x - g_3})\,\dd{x}` は
    置換積分法により :math:`\displaystyle \int R(\wp(z), \wp'(z))\wp'(z)\,\dz` である。

  * 楕円関数の逆関数 :math:`\displaystyle \wp\inv(z) = \int \frac{\dx}{\sqrt{4x^3 - g_2x - g_3}}` を楕円積分という。

----

:doc:`note09` へ。
