======================================================================
第 7 章 多様体上の曲線の長さ（後編）
======================================================================

.. contents:: ノート目次

7.5 測地流（展開）
======================================================================
`測地流 <http://mathworld.wolfram.com/GeodesicFlow.html>`__
  測地線の方程式は接束上のベクトル場として表わされる。

  * 測地線 :math:`c(t)` は次を満たす：
    :math:`\displaystyle q\left(\diff{c}{t}\right) = const.`
  * :math:`a > 0` に対して :math:`q\inv(a)` はコンパクトであり、
    さっきのベクトル場はフローを生成するので、次のフローを定義できる：
    :math:`\fn{F_t}{q\inv(a)}q\inv(a);\quad \fn{F_t}{TM}TM.`

* 定理 7.5.1: `ホップ・リノウの定理 <http://mathworld.wolfram.com/Hopf-RinowTheorem.html>`__

  コンパクト連結多様体の任意の二点について、測地線が存在するという主張か。
  ここで示すのは :math:`\forall x, y \in M, \exists \fn{c}{[0, 1]}M \quad \text{s.t. } c(0) = x, c(1) = y, d(x, y) = L(c).`

  * 任意の二点が一致するときはどうだ。点（定値写像）も測地線の一種ということでよい？

  * 証明では :math:`M` の任意の点が指数写像 :math:`\fn{E_x}{T_xM}M` の像となることを示す。
  * そのために :math:`\forall k \in NN` に対して :math:`\fn{E_x}{T_xM}M` が
    :math:`\set{y \in M \sth d(x, y) < k\eps}` 上への全射となることを示す。

  * 帰納法で :math:`k = 2` のときと、
    :math:`k` のときに成り立てば :math:`k + 1` のときに成り立つことを示す。

    #. :math:`T_xM` の半径 :math:`2\eps` の閉球体が
       :math:`E_x` により :math:`M` に単射されるように :math:`\eps > 0` をとる。

       * :math:`E_x|\set{v \in T_xM \sth g(v, v) \le 4\eps^2} \longto M` が単射？

    #. :math:`k` のときに成り立つと仮定する。

       * 指数写像 :math:`\fn{E_y}{T_yM}M` によるボール :math:`S_\eps = \set{v \in T_yM \sth g(v, v) = \eps^2}` および
         像 :math:`E_y(S_\eps)` を考える。

       * コンパクト性により、:math:`\exists z \in S_y(v) \in E_y(S_\eps) \quad \text{s.t. }`
         次のような写像 :math:`M \longto \RR` がある：

           :math:`z \longmapsto d(x, y)` の制限 :math:`|E_y(S_\eps)` が最小値 :math:`m` をとる。

       * :math:`x, y` を結ぶ曲線は :math:`E_y(S_\eps)` の点を通過するから :math:`m < k\eps.`
       * :math:`\exists w \in M\quad\text{s.t. } z = E_y(v) = E_x(w), g(w, w)^2 = d(x, z)^2, d(z, y) = \eps.`
       * ここで次の二つのベクトルが線形独立であるとすると、
         :math:`\exists z' \in E_y(S_\eps)\quad\text{s.t. } z' \ne z, d(x, z') < d(x, z).`
         これは :math:`z` のとり方に矛盾する。
         したがってこの二つの測地線は互いに反対を向いている。

         .. math::

            \left.\diff{E_x(tw)}{t}\right|_{t = 1} \in T_zM,\ 
            \left.\diff{E_y(tv)}{t}\right|_{t = 1} \in T_zM.

       * ゆえに :math:`E_x(\dfrac{m + \eps}{m}) = y.`
         これで :math:`k + 1` のときも成り立っていることが示された。

* （最短測地線）コンパクト連結リーマン多様体の任意の二点に対して、

  #. それらを結ぶ最小の長さの曲線が存在して、
  #. それは測地線で表される。

* リーマン多様体が距離空間的に完備であれば、

  #. それらを結ぶ最小の長さの曲線が存在し、
  #. :math:`E_x` が全射となる。

* 例 7.5.2: 球面にユークリッド計量から決まるリーマン計量

  * :math:`T_1 S^2` を :math:`TS^2` のうち長さが 1 のベクトルの全体とする。
    これは :math:`SO(3)` と同一視できる。前にも書かれている。
  * 軌道は大円の接ベクトルとなる。
  * すべての軌道は閉である。
  * 測地流は :math:`T_1 S^2` 上のフローとなっている。
  * :math:`(\bm v_1, \bm v_2, \bm v_3) \in SO(3)` に対して :math:`\bm v_1 \in S^2` における
    接ベクトル :math:`\bm v_2` を対応させるとフロー :math:`\fn{F_t}{T_1 S^2}T_1 S^2` は計算できて
    次のようになる：

    .. math::
       :nowrap:

       \begin{align*}
       F_t((\bm v_1, \bm v_2, \bm v_3)) 
       &=
       \begin{pmatrix}
       \bm v_1 \cos t + \bm v_2 \sin t & - \bm v_1 \sin t + \bm v_2 \cos t & \bm v3
       \end{pmatrix}
       \\
       &= (\bm v_1, \bm v_2, \bm v_3)
       \begin{pmatrix}
       \cos t & -\sin t & 0\\
       \sin t &  \cos t & 0\\
       0 & 0 & 0
       \end{pmatrix}
       \end{align*}

* 例 7.5.3: :math:`T^2 = \RR^2/\ZZ^2` に :math:`\RR^2` のユークリッド計量から誘導されるリーマン計量

  * :math:`T_1T^2` を :math:`TT^2` のうち長さが 1 のベクトルの全体とする。
  * 測地流は :math:`T_1T^2` 上のフローであり次のように書ける：
    :math:`F_t((x_1, x_2), (v_1, v_2)) = ((x_1 + tv_1, x_2 + tv_2), (v_1, v_2))`
  * 測地流の軌道は

    * 閉軌道 if :math:`v_2/v_1 \in \QQ \cup \set{\infty}`
    * :math:`(\RR/\ZZ)^2 \times \set{(v_1, v_2)}` において稠密な軌道
      if :math:`v_2/v_1 \in \RR\setminus\QQ`

* 例 7.5.4: トーラスの測地流の振る舞い

  * フロー上では :math:`q(x)^2 = v_1^2(2 + \cos x_2)^2 + v_2^2` が不変量であるので、
    この値が 1 である軌道の全体を考える。

  * :math:`\cos \theta = v_1^2(2 + \cos x_2)^2,\quad \sin\theta = v_2` と変数変換すると
    次の常微分方程式を得る：

    .. math::

       \begin{align*}
       \diff{\theta}{t} &= \frac{\sin x_2}{2 + \cos x_2},\\
       \diff{x_2}{t} &= \sin\theta
       \end{align*}

  * さらに :math:`f(x_2, \theta) = (2 + \cos x_2)\cos\theta` とおくと
    常微分方程式 :math:`\displaystyle \diff{f}{t} = 0` が得られる。
    軌道は :math:`f` の等位線上にある（本書図 7.5 参照）。

7.6 等長変換群（展開）
======================================================================
リーマン計量を持つ多様体上で距離を不変に保つ等長変換を考えると、
多様体の性質がよくわかることがある。

* 定義 7.6.1: `等長変換 <http://mathworld.wolfram.com/Isometry.html>`__

  二つのリーマン多様体 :math:`(M, g_M),\ (N, g_N)` に対して次のような微分同相写像
  :math:`\fn{F}{M}N` が存在する：
  :math:`F^* g_N = g_M.`

  * ここで :math:`(F^* g_N)(v_1, v_2) := g_N(F_* v_1, F_* v_2)` とする。
  * これは :math:`M` 上のリーマン計量となる。

* :math:`(M, g)` から自身への等長写像の全体 :math:`\operatorname{Isom}(M)` は群となる。

  * これは高々 :math:`\displaystyle \frac{n(n + 1)}{2}` 次元多様体である。

  * :math:`T_xM` に正規直交基底を定義する。二つ定義すると、それらは :math:`O(n)` で写り合う。
  * 点 :math:`x` のある座標近傍 :math:`(U, \varphi)` で :math:`T_yM\ (y \in U)` の
    正規直交基底の全体は多様体 :math:`U \times O(n)` でパラメーター付けられる。

  * 以上を各点 :math:`x \in M` で考える。
    すると :math:`T_xM` の正規直交基底全体は :math:`U \times O(n)` の座標近傍により
    :math:`\displaystyle \frac{n(n + 1)}{2}` 次元多様体となる。

  * これを記号 :math:`\operatorname{Fr}(M)` で :math:`T_xM\ (x \in M)` で表す。
    接正規直交 `n 枠束 <http://mathworld.wolfram.com/FrameBundle.html>`__ という。

  * :math:`\operatorname{Isom}(M)` は :math:`\operatorname{Fr}(M)` の閉部分集合である。

  * 自然な射影 :math:`\fn{p}{\operatorname{Fr}M}M` について
    :math:`p\inv(U)` は :math:`U \times O(n)` と微分同相となる。
    ファイバー束を構造として持つとみなせる。

`マイヤーズ・スティンロッドの定理 <https://en.wikipedia.org/wiki/Myers%E2%80%93Steenrod_theorem>`__
  ここよくわからない。

  #. 点 :math:`x_0 \in M` とその :math:`T_{x_0}M` 上の正規直交基底 :math:`E_0 = (e_1, \dotsc, e_n)` を固定する。
  #. 等長変換 :math:`\fn{F}{M}M,\ F_*E_0 = (F_*e_0, \dotsc, F_*e_n) \in \operatorname{Fr}M.`
  #. 点 :math:`y \in M,` 二点を結ぶ測地線 :math:`E_{x_0}(tv)\ (v \in T_{x_0}M, E_{x_0}(v) = y` をとる。

     :math:`F(E_{x_0}(tv)) = E_{F(x_0)}(tF_*v)` より
     :math:`F(y) = E_{F(x_0)}(F_*v)` となり、
     :math:`F` は :math:`F_*E_0` で定まる。

  #. したがって :math:`\operatorname{Isom}(M)` は :math:`\operatorname{Fr}M` に埋め込まれる。

* 例 7.6.2: 単位球面の等長変換群

  * :math:`O(n + 1)`
  * :math:`\displaystyle \frac{n(n + 1)}{2}` 次元多様体である。

* :math:`n` 次元ユークリッド空間の等長変換群は
  直交群と平行移動群との `半直積 <http://mathworld.wolfram.com/SemidirectProduct.html>`__
  :math:`O(n) \ltimes \RR^n` として表され、
  :math:`\displaystyle \frac{n(n + 1)}{2}` 次元多様体である。

* 球面の直積 :math:`S^m \times S^n\ (m \ne n)` のリーマン計量をそれぞれの計量の直積とする。
  このとき :math:`\operatorname{Isom}(S^m \times S^n) = O(m + 1) \times O(n + 1).`

* コンパクト 2 次元連結多様体 :math:`M` とそのリーマン計量 :math:`g` について

  * 各 :math:`x \in M` に対して長さが 1 の接ベクトル :math:`v \in T_xM` をとると、
    次のような近傍 :math:`U_v \subset M` が存在する：

      :math:`v_1 \in T_{x_1}M,\ v_2 \in T_{x_2}M` に対して
      等長変換 :math:`\fn{F_{v_1 v_2}}{U_{v_2}}U_{v_1}` が存在して
      :math:`(F_{v_1 v_2})_* v_2 = v_1` となる。

  * :math:`g` から来るガウス曲率が一定になるだとか、
    :math:`g` は局所的に対称性が高いだとかに触れている。

* コンパクト 2 次元連結多様体は次の三つしかない：

  #. :math:`S^2,\ \RR P^2`
  #. :math:`\RR^2/\ZZ^2,\ \RR^2/G\ (G \cong \ZZ/2\ZZ \ltimes \ZZ^2):` クラインボトル
  #. :math:`D^2/GP,` ここで :math:`G` は
     `ポアンカレ円板 <http://mathworld.wolfram.com/PoincareHyperbolicDisk.html>`__
     の等長変換群の部分群とする

* 与えられたリーマン計量を変形して、もっとよいリーマン計量を得るという問題がある。

7.7 リーマン計量の存在
======================================================================
* 定理 7.7.1: :math:`n` 次元コンパクト多様体 :math:`M` 上にはリーマン計量が存在する

  証明方針は、とにかく正値二次形式 :math:`q(v)` を構成する。

  #. 有限開被覆 :math:`\set{(U_i, \varphi_i)}_{i = 1, \dotsc, k}` をとり、さらに
     いつものように次の包含関係を満たす開被覆 :math:`\set{(V_i, \varphi_i)}_{i = 1, \dotsc, k}` をとる：
     :math:`U_i \supset \closure{V_i} \supset V_i.`

  #. 非負関数 :math:`\mu_i: M \to \RR` を次のようにとる：
     :math:`\supp \mu_i = U_i,\ \mu_i(x) > 0 \text{ if } x \in \closure{V_i}.`

  #. 次のように :math:`\mu_i q_i(v)` をとると、
     :math:`TM` 上 :math:`C^\infty` 級かつ :math:`T_xM` 上二次形式となる：

     .. math::

        \mu_i q_i(v) =
        \begin{cases}
        \displaystyle \mu_i(x)\sum_{i=1}^n(v_i^{(i)})^2 & \quad \text{if } v \notin T_xM\\
        0 & \quad \text{if } v \in T_xM
        \end{cases}

  #. :math:`\displaystyle q(v) = \sum_{i = 1}^k \mu_i q_i(v)` とすると、
     これが :math:`TM` 上 :math:`C^\infty` 級かつ :math:`T_xM` 上正値二次形式となる。

     * :math:`\forall a \in \RR, q(av) = a^2 q(v)` はすぐにわかる。
     * :math:`q(u + v) - q(u) - q(v) = \sum \mu_i(q_i(u + v) - q_i(u) - q_i(v))` であるが、
       カッコの中身が bilinear なので和をとっても bilinear だ。

  #. :math:`q(v) = 0, v \in T_xM \implies \forall i, x \in V_i,`

     .. math::

        v = \sum_j v_i^{(i)}\frac{\partial}{\partial x_j^{(i)}},\quad
        q_i(v) = \sum (v_i^{(i)})^2 = 0.\quad
        \therefore v = 0.

* 問題 7.7.2: コンパクト多様体の微分同相写像からなる有限群 :math:`F` に対して、
  次を満たすリーマン計量 :math:`g` が存在する：
  :math:`\forall f \in F, f^*g = g.`

  * 記号を導入する：

    * :math:`F = \set{f_1 = \id_M, f_2, \dotsc, f_k}` と書く。
    * 写像 :math:`\fn{q}{TM}M` を「各接空間でリーマン計量を与える二次形式を与える」ようにとる。
    * ヒントにあるように写像 :math:`\hat{q}(v) = \dfrac{1}{k}\sum(q((f_i)_*v)` を定義する。

  * :math:`\fn{(f_i)_*}{T_xM}T_{f_i(x)}M` は線形写像である。
  * :math:`q((f_i)_*v)` は :math:`T_xM` 上は正定値二次形式である。
    これを :math:`k` で割っても正定値二次形式である。

  * ゆえに :math:`\hat{q}` は :math:`M` 上でリーマン計量を与える。

  .. math::

     \begin{align*}
     (f^*\hat{q})(v) & = \hat{q}(f_*v) \quad(\because \text{pull-back})\\
     &= \frac{1}{k}\sum_{i = 1}^k q((f_i)_*(f_*v))\\
     &= \frac{1}{k}\sum_{i = 1}^k q((f_if)_*v) \quad(\because \text{covariant})\\
     &= \frac{1}{k}\sum_{i = 1}^k q((f_i)_*v) \quad(\because \text{property of }F)\\
     &= \hat{q}(v).\\
     \therefore f^*g &= g.
     \end{align*}

* 問題 7.7.3: リーマン多様体間の等長変換はリーマン計量をリーマン計量に写す微分同相写像である。
  すなわち :math:`d_{g_N}(f(x), f(y)) = d_{g_M}(x, y) \implies g_N(f_* v_1, f_* v_2) = g_M(v_1, v_2).`

  * 解答の :math:`\fn{F}{TM}TN` をどのように捻出したのかがわからない。
    問題文の :math:`f` について :math:`f_* = F` となる :math:`F` を最初に定義するわけだが。

  * 指数写像 :math:`\fn{E_x}{T_xM}M` と測地線 :math:`\gamma(t)` の接ベクトル
    :math:`s\bm v_1` と :math:`s\bm v_2` に対する像を考える。
    これらの :math:`M` 上の :math:`t : 1 - t` の内分点の逆像ベクトルの
    :math:`s \to 0` の極限が :math:`t\bm v_1 + (1 - t)\bm v_2` になることを確認して、
    指数写像に関係する :math:`F` が線形であることを示す。

* 最後に `ナッシュの埋め込み定理 <https://en.wikipedia.org/wiki/Nash_embedding_theorem>`__ について触れている。

7.8 ユークリッド空間の超曲面の測地線
======================================================================
* :math:`f(\bm x) = 0` で表される曲面の測地線を求める。

  #. :math:`f(\bm x) = 0` を二度微分する。
  #. ある関数 :math:`a(\bm x, \bm v)` に対して、測地線の方程式を次のように立てる：

     .. math::
        :nowrap:

        \begin{gather*}
        \diff{x_i}{t} = v_i,\ \diff{v_i}{t} = a(\bm x, \bm v)\frac{\partial}{\partial x_i}(\bm x).
        \end{gather*}

  #. この式を二度微分した式に代入して :math:`a(\bm x, \bm v)` について表す：

     .. math::
        :nowrap:

        \begin{gather*}
        a(\bm x, \bm v) = - \frac
            {\displaystyle \sum_{i, j = 1}^n \frac{\partial^2 f}{\partial x_i \partial x_j}(\bm x) v_i v_j}
            {\displaystyle \sum_{i, j = 1}^n \left(\frac{\partial f}{\partial x_i}(\bm x)\right)^2}
        \end{gather*}

  #. 最後にこの式を測地線の方程式に代入して :math:`a(\bm x, \bm v)` を消去する。

* :math:`z = h(x_1, x_2)` とグラフ表示される曲面では :math:`f = -h(x_1, x_2) + z` ととることで
  次の式で測地線を表せる：

  .. math::
     :nowrap:

     \begin{gather*}
     \diff{v_i}{t} = -\frac
       {\displaystyle \frac{\partial h}{\partial x_i}}
       {\displaystyle 1 
         + \left(\frac{\partial h}{\partial x_1}\right)^2 
         + \left(\frac{\partial h}{\partial x_2}\right)^2}
     \left(
       \frac{\partial^2 h }{\partial x_1^2}v_1^2 
         + 2 \frac{\partial^2 h}{\partial x_1 \partial x_2}v_1 v_2
         + \frac{\partial^2 h}{\partial x_2^2} v_2^2
       \right)
     \ \text{ for } i = 1, 2.
     \end{gather*}

* 例 7.8.1: `双曲放物面 <http://mathworld.wolfram.com/HyperbolicParaboloid.html>`__  :math:`z = x_1 x_2 = h`

  * :math:`Dh = \begin{pmatrix}x_2 & x_1\end{pmatrix}`
  * :math:`H_h = \begin{pmatrix}0 & 1\\1 & 0\end{pmatrix}`

  .. math::

     \mdiff{}{2}{t}\begin{pmatrix}x_1\\x_2\end{pmatrix} =
     - \frac{2}{1 + x_1^2 + x_2^2}
     \diff{x_1}{t}\diff{x_2}{t}
     \begin{pmatrix}x_2\\x_1\end{pmatrix}.

* 例 7.8.2: `放物面 <http://mathworld.wolfram.com/EllipticParaboloid.html>`__ :math:`z = -x_1^2 - x_2^2 = h`

  * :math:`Dh = \begin{pmatrix}-2x_1\quad -2x_2\end{pmatrix}`
  * :math:`H_h = \begin{pmatrix}-2 & 0\\0 & -2\end{pmatrix}`

  .. math::

     \mdiff{}{2}{t}\begin{pmatrix}x_1\\x_2\end{pmatrix} =
     -\frac{4}{1 + 4x_1^2 + 4x_2^2}
     \left(
       \left(\mdiff{x_1}{2}{t}\right)^2 +
       \left(\mdiff{x_2}{2}{t}\right)^2
     \right)
     \begin{pmatrix}x_1\\x_2\end{pmatrix}.

7.9 第 7 章の問題の解答
======================================================================
本文中に埋めた。
