======================================================================
第 2 章 多様体上の微分形式 (1/3)
======================================================================

本巻ではユークリッド空間内の多様体のパラーメーター表示に対して、
その表示による引き戻しにより微分形式が表示されていると考える。

.. contents:: ノート目次

2.1 多様体（基礎）
======================================================================
序盤は :doc:`/tsuboi05/chapter3a` のおさらいのようになっている。

.. _tsuboi08.2.1.1:

* 定義 2.1.1: 多様体の定義

  * :ref:`第 1 巻定義 3.1.1 <tsuboi05.3.1.1>` と同じ。

.. _tsuboi08.2.1.2:

* 注意 2.1.2: パラコンパクト性に関する注意

  * :ref:`第 1 巻注意 3.1.3 <tsuboi05.3.1.3>` と同じ。

.. _tsuboi08.2.1.3:

* 定義 2.1.3: 多様体の間の写像の定義

  * 第 1 巻で見覚えあり。

.. _tsuboi08.2.1.4:

* 定理 2.1.4: :ref:`第 1 巻定理 5.1.3 <tsuboi05.5.1.3>` と同じ。

.. _tsuboi08.2.1.5:

* 定理 2.1.5: :ref:`第 1 巻定理 5.3.6 <tsuboi05.5.3.6>` と同じ。

  * 1 の分割は第 1 巻では多様体上に関数がたくさん存在することなどに
    利用されていた。本巻は
    後で出てくるマイヤー・ビエトリス完全系列、チェック・ドラーム複体、
    向き付けられた多様体上の積分の定義に利用される。

.. _tsuboi08.2.1.6:

* 注意 2.1.6: 多様体における 1 の分割が存在する条件は、
  それがパラコンパクトであることまで緩められる。

以下のノートにおいて、当分の間、多様体の話題が出てくるときには
多様体、座標近傍系、座標、座標変換、座標近傍の像、
多様体間の写像に対していつも使っていた記号を用いる。

.. _tsuboi08.2.1.7:

* 定義 2.1.7: 多様体上の微分形式 (1)

  :math:`\alpha` が多様体上の微分形式であるとは、
  各 :math:`V_i = \varphi(U_i)` 上の :math:`C^\infty` 級 p 形式であって、
  次の条件を満たすものをいう：

  .. math::

     \alpha^{(j)}|V_{ij} = \varphi_{ij}^* \alpha^{(i)}.

* 例題 2.1.8: :math:`(U_0, \varphi_0)` が座標近傍系 :math:`\set{(U_i, \varphi_i)_{i \in I}}`
  と両立するとき、多様体上の微分形式 :math:`\alpha` は :math:`V_0 = \varphi_0(U_0)`
  上の :math:`\alpha^{(0)}` で、
  :math:`\alpha^{(0)}|V_{i0} = \varphi_{i0}^* \alpha^{(i)}` を満たすものを定める。

  * まず :math:`V_0` の開被覆を :math:`\set{(V_{i0})}_{i \in I}` とおく。

    * 座標近傍の像のほうの開被覆をとるのは珍しい気がする。

    示したいことは、
    :math:`\forall V_{i0} \cap V_{j0},\ \varphi_{i0}^*|\alpha^{(i)} = \varphi_{j0}^*|\alpha^{(i)}`
    ならば
    :math:`V_0` 上のすべての点において :math:`\alpha^{(0)}` が well-defined であることだ。

  * 両立しているから :math:`i, j, k \in \zeroset \cup I,\quad \varphi_{ik} = \varphi_{ij} \circ \varphi_{jk}` だが、
    特に :math:`k = 0` として :math:`\varphi_{i0} = \varphi_{ij} \circ \varphi_{j0}` だ。

  * :ref:`定義 2.1.7 <tsuboi08.2.1.7>` の関係が :math:`V_{ij}` 上成り立っているので、
    :math:`V_{i0} \cap V_{j0}` 上次のようになる：

    .. math::

       \begin{align*}
       \varphi_{i0}^* \alpha^{(i)}
       &= (\varphi_{ij} \circ \varphi_{j0})^* \alpha^{(i)}\\
       &= \varphi_{j0}^* \varphi_{ij}^* \alpha^{(i)}\\
       &= \varphi_{j0}^* \alpha^{(j)}.
       \end{align*}

以上より、p 形式 :math:`\alpha` は任意の座標近傍 :math:`U` 上で、
ユークリッド空間の開集合 :math:`\varphi(U)` 上の p 形式として表示されていることがわかった。

.. _tsuboi08.2.2:

2.2 余接空間
======================================================================
* 接ベクトルの定義と似せて、微分形式を関数の同値類として定義する。
* 多様体上の点において微分可能な関数 :math:`f_1, f_2` が同値であることを
  次のように定義する：

  .. math::

     f_1 \sim f_2 \iff \dd{(f_1 \circ \varphi\inv)}_{(\varphi(x))}
     = \dd{(f_2 \circ \varphi\inv)}_{(\varphi(x))}.

* 座標近傍 :math:`(U, \varphi),\ (V, \psi)` について
  :math:`f_1 \sim f_2 \implies \dd{(f_1 \circ \psi\inv)}_{(\psi(x))} = \dd{(f_2 \circ \psi\inv)}_{(\psi(x))}`
  である。

  * このことは :math:`\dd{(\varphi^*f)} = \varphi^*\dd f` や
    :math:`f_k \circ \psi\inv = f_k \circ \varphi\inv \circ \varphi \circ \psi\inv` を使って示せる。

.. _tsuboi08.2.2.1:

* 定義 2.2.1: `余接空間 <https://en.wikipedia.org/wiki/Cotangent_space>`__

  .. math::

     T_x^*M = C^\infty(M)/\sim.

.. _tsuboi08.2.2.2:

* 例題 2.2.2: 余接空間は :math:`C^\infty(M)` の実ベクトル空間から定まるベクトル空間である。

  * 写像 :math:`[f] \in C^\infty(M)/\sim \longmapsto \left(\dfrac{\partial f}{\partial x_1}(\varphi(x)), \dotsc, \dfrac{\partial f}{\partial x_n}(\varphi(x))\right) \in \RR^n`
    が準同型写像（線形写像）となる：

    .. math::

       \frac{\partial(a_1 f_1 + a_2 f_2)}{\partial x_i}(\varphi(x))
       = a_1 \frac{\partial f_1}{\partial x_i}(\varphi(x))
       + a_2 \frac{\partial f_2}{\partial x_i}(\varphi(x)).

  * この写像は同値類の定義により単射である。
  * 全射であることを示すのに 1 の分割の技法を用いる。

    * まず :math:`\bm a \in \RR^n` に対して :math:`U` 上の関数
      :math:`f_{\bm a} = \sum_{i = 1}^n a_i x_i` を対応させる。

    * :ref:`定理 2.1.4 <tsuboi08.2.1.4>` の :math:`\nu` に対して :math:`\nu f_{\bm a}` を考える。
      これは :math:`U` 上の関数 :math:`f_{\bm a}` を
      :math:`M` 上に拡張された :math:`C^\infty` 級関数となっている。

    .. math::

       \dd(\nu f_{\bm a})
       = \dd\left(\nu \sum_{i = 1}^n a_i x_i\right)_{\varphi(x)}
       = \sum_{i = 1}^n a_i (\dd x_i)_{\varphi(x)}.

* 点 :math:`x \in M` の局所座標が :math:`(x_1, \dotsc, x_n)` であるとき、
  :math:`T_x^*M` の基底を :math:`\dd x_1, \dotsc, \dd x_n` と書く。

  * 点を明示する場合もある。
  * 基底の取り方が座標近傍によることに注意。

* 基底の変換は 1 形式の引き戻しの式に一致する：

  .. math::

     \begin{align*}
     \dd y_i &= \sum_{j = 1}^n \left(\dfrac{\partial y_i}{\partial x_j}\right)_{(\varphi(x))}\,\dd x_j\\
     (\varphi \circ \psi\inv)^* (\dd y_i)_{\psi(x)} &=
     \sum_{j = 1}^n \left(\dfrac{\partial y_i}{\partial x_j}\right)_{(\varphi(x))}\,
     (\dd x_j)_{\varphi(x)}.
     \end{align*}

.. _tsuboi08.2.2.3:

* 定義 2.2.3: 多様体上の 1 形式

  * :math:`x \in M`
  * :math:`f_i \in C^\infty(M)`

  このとき各座標近傍上での一次結合への対応
  :math:`x \longmapsto \displaystyle \sum_{i = 1}^n f_i\,\dd x_i \in T_x^*M` を表題のように呼ぶ。

.. _tsuboi08.2.2.4:

* 定義 2.2.4: 多様体上の全微分

  同じ条件で :math:`\displaystyle \dd f = \sum_{i = 1}^n \dfrac{\partial f_i}{\partial x_i}\,\dd x_i`
  のことを表題のように呼ぶ。

.. _tsuboi08.2.2.5:

* 例題 2.2.5: 余接空間の準同型写像（線形写像）

  * :math:`C^\infty` 級写像 :math:`\fn{F}{M}N`
  * :math:`C^\infty` 級関数 :math:`\fn{f}{N}\RR`

  このとき :math:`F^*f = f \circ F` は準同型（線形写像）
  :math:`\fn{F^*}{T_{F(x)}^*N}T_x^*M` を引き起こす。

  * 証明は :ref:`2.2 節 <tsuboi08.2.2>` 冒頭の式変形のようにすることで示せる。
  * :math:`\fn{F^*}{C^\infty(N)}C^\infty(M)` として準同型であるので、
    余接空間の写像として見ても準同型である。

.. _tsuboi08.2.2.6:

* 問題 2.2.6: ステレオグラフ

  多様体上では 1 形式と接ベクトルとをはっきり区別して考える必要があることを示すデモのような問題だ。
  単位球面の北極と南極に関して投影写像を次のようにとる：

  .. math::

     \fnm{\pi_N}{S^2\setminus\set{p_N}}{\RR^2}{(x_1, x_2, x_3)}(v_1, v_2) = \left(\frac{x_1}{1 - x_3}, \frac{x_2}{1 - x_3}\right),\\
     \fnm{\pi_S}{S^2\setminus\set{p_S}}{\RR^2}{(x_1, x_2, x_3)}(u_1, u_2) = \left(\frac{x_1}{1 + x_3}, \frac{x_2}{1 + x_3}\right).

  * \(1) 各投影写像の逆写像

    計算方法は球と直線との交点を求めるだけだ。
    二次方程式を解くことになり、ニ根のうち 1 でないほうを :math:`x_3` とすればよい。
    SymPy で計算した結果を ``print_latex`` で出力し、それを整形したものを記す：

    .. math::

       \begin{align*}
       \pi_N\inv(x_1, x_2, x_3) &= \left(
           \frac{2 v_1}{v_1^2 + v_2^2 + 1},
           \frac{2 v_2}{v_1^2 + v_2^2 + 1},
           \frac{v_1^2 + v_2^2 - 1}{v_1^2 + v_2^2 + 1}\right),\\
       \pi_S\inv(x_1, x_2, x_3) &= \left(
           \frac{2 u_1}{u_1^2 + u_2^2 + 1},
           \frac{2 u_2}{u_1^2 + u_2^2 + 1},
           -\frac{u_1^2 + u_2^2 - 1}{u_1^2 + u_2^2 + 1}\right).
       \end{align*}

  * \(2) 座標近傍系 :math:`\set{(S^2\setminus\set{p_N}, \pi_N), (S^2\setminus\set{p_S}, \pi_S)}` の座標変換

    SymPy の出力を整形したものを記す：

    .. math::

       \begin{align*}
       \pi_N \circ \pi_S\inv(u_1, u_2) &= \left(
           \frac{u_1}{u_1^2 + u_2^2},
           \frac{u_2}{u_1^2 + u_2^2}\right)\\
       \pi_S \circ \pi_N\inv(v_1, v_2) &= \left(
           \frac{v_1}{v_1^2 + v_2^2},
           \frac{v_2}{v_1^2 + v_2^2}\right)
       \end{align*}

  * \(3) 下に示す平面上の多項式係数のベクトル場について :math:`(\pi_N\inv)_*\xi` が
    :math:`S^2` 上でも微分可能である条件とは？

    .. math::

       \xi = P(v_1, v_2) \frac{\partial}{\partial v_1}
           + Q(v_1, v_2) \frac{\partial}{\partial v_2}.

    大まかな解き方：

    #. :math:`{\pi_S}_*(\pi_N\inv)_*\xi` を :math:`P, Q, u_1, u_2, \dfrac{\partial}{\partial u_1}, \dfrac{\partial}{\partial u_2}`
       を使って表す。例えば次を使う：

       .. math::

          \frac{\partial}{\partial v_j} = \sum_{i = 1, 2} \frac{\partial u_i}{\partial v_j}\frac{\partial}{\partial u_i}\quad(j = 1, 2).

    #. :math:`k = \max\set{\deg P, \deg Q}` とし、
       :math:`{\pi_S}_*(\pi_N\inv)_*\xi` の :math:`-k + 2` 次の項を求める。

       * :math:`k > 2` とすると :math:`\dfrac{\partial}{\partial u_1}, \dfrac{\partial}{\partial u_2}`
         の係数の有理式が :math:`u_1 = u_2 = 0` でも有効であるには、
         分子と分母の両方がゼロであることが必要。
         つまり :math:`P, Q` の k 次の項を :math:`P_k, Q_k` とおくと、
         これらが両方ゼロであることが必要となる。

    #. :math:`k = 2` とすると :math:`\dfrac{\partial}{\partial u_1}, \dfrac{\partial}{\partial u_2}`
       の係数の有理式はそれぞれ
       :math:`A(u_1^2 + u_2^2)^2` と :math:`B(u_1^2 + u_2^2)^2` の形をとる。
       すなわち：

       .. math::

          \begin{align*}
          P_2(u_1, u_2) &= (u_2^2 - u_1^2)A - 2 u_1 u_2 B,\\
          Q_2(u_1, u_2) &= -2 u_1 u_2 A - (u_2^2 - u_1^2)B.
          \end{align*}

    #. 1 次同次の項を :math:`P_1(u_1, u_2) = a_1 u_1 + a_2 u_2,`
       :math:`Q_1(u_1, u_2) = b_1 u_1 + b_2 u_2` とすると、
       引き算して :math:`P_1 = a_1 u_1 - b_1 u_2,\ Q_1 = b_1 u_1 + a_1 u_2` ならば
       0 次のベクトル場として球面上に拡張できることがわかる。

    #. 最後に積分定数のようなものを考慮に入れて、
       与えられたベクトル場の形とは次のようなものである：

       .. math::

          ((v_2^2 - v_1^2)A - 2v_1v_2B + a_1v_1 - b_1v_2 + c_1)\frac{\partial}{\partial v_1}
          + (-2v_1v_2A - (v_1^2 - v_2^2)B + b_1v_1 + a_1v_2 + c_2)\dfrac{\partial}{\partial v_2}.

  * \(4) 下に示す平面上の多項式係数の 1 形式について :math:`\pi_N^* \alpha` が
    :math:`S^2` 上でも微分可能である条件とは？

    .. math::

       \alpha = P(v_1, v_2) \dd v_1 + Q(v_1, v_2) \dd v_2.

    大まかな解き方：

    #. :math:`\dd v_1, \dd v_2` を :math:`\dd u_1, \dd u_2` で表す：

       .. math::

          \dd v_j = \sum_{i = 1, 2}\frac{\partial v_j}{\partial x_i}\,\dd x_i\quad(j = 1, 2).

    #. :math:`{\pi_S\inv}^* \pi_N^* \alpha` を :math:`P, Q, u_1, u_2, \dd u_1, \dd u_2` で表す。
    #. 今度は :math:`{\pi_S\inv}^* \pi_N^* \alpha` の :math:`-k - 2` 次の項を求めることになる。

       * :math:`\dd u_1, \dd u_2` の係数の有理式が複雑。
       * :math:`k \ge 0` とすると分母に :math:`(u_1^2 + u_2^2)^{k + 2}` が現れる。
         つまり :math:`P_k = Q_k = 0` が必要。

    #. よって 0 以外の多項式では与えられた微分形式は球面上に拡張できない。

2.3 p 次外積の空間
======================================================================
.. _tsuboi08.2.3.1:

* 定義 2.3.1: p 次外積の空間 :math:`\extp^p T_x^*M`

  余接空間 :math:`T_x^*M` の p 次外積空間とは、
  :math:`1 \le i_1 < \dotsb < i_p \le n` なる自然数の添字に対応する
  記号 :math:`\dd x_{i_1} \wedge \dotsb \wedge \dd x_{i_p}` を基底とする
  ベクトル空間のことをいう。

.. _tsuboi08.2.3.2:

* 例 2.3.2: 4 次元空間の 2 次外積空間は 6 次元ベクトル空間である。

* 余接空間の基底の取り替えにより、外積空間の基底も座標変換される：

  .. math::

     \dd x_{i_1} \wedge \dotsb \wedge \dd x_{i_p}
     = \sum_{j_1, \dotsc, j_p = 1}
       \frac{\partial x_{i_1}}{\partial y_{j_1}}\dots
       \frac{\partial x_{i_p}}{\partial y_{j_p}}\,
       \dd y_{j_1} \wedge \dotsb \wedge y_{j_p}.

  * 同じ添字があれば :math:`\dd y_{j_1} \wedge \dotsb \wedge y_{j_p} = 0.`
  * 添字列が互いに順列ならば、値は符号だけが異なる：

    .. math::

       \dd{y_{j_1}} \wedge \dotsb \wedge \dd{y_{j_p}} = \sgn
       \begin{pmatrix}j_1 & \dots & j_p\\k_1 & \dots & k_p\end{pmatrix}
       \dd{y_{k_1}} \wedge \dotsb \wedge \dd{y_{k_p}}.

  * cf. :ref:`定義 1.6.8 <tsuboi08.1.6.8>`

.. _tsuboi08.2.3.3:

* 注意 2.3.3: 外積空間の座標変換は外積と両立するように定義されている。

.. _tsuboi08.2.3.4:

* 定義 2.3.4: 多様体上の微分形式 (2)

  * 各座標近傍上で、各点における余接空間の外積空間 :math:`\extp^p T_x^*M` の元を、
    :math:`f_{i_1\dots i_p}` が :math:`C^\infty` 級であるように、
    :math:`f_{i_1\dots i_p}\,\dd x_{i_1} \wedge \dotsb \wedge \dd x_{i_p}` に対応させるものを
    この多様体上の :math:`C^\infty` 級微分 p 形式という。

  * 記号 :math:`\varOmega^p(M)` で p 形式の空間を表す。
    多様体が 1 次元以上であればこれは無限次元のベクトル空間である。

  * cf. :ref:`定義 2.1.7 <tsuboi08.2.1.7>`

.. figure:: /_images/cd-differentialform.png
   :align: center
   :alt: math.topology.differentialform
   :width: 388px
   :height: 355px
   :scale: 100%

.. _tsuboi08.2.3.5:

* 例 2.3.5: n 次元トーラス :math:`T^n = \RR^n/\ZZ^n`

  * これは多様体である：

    :math:`\fn{\pi}{\RR^n}T^n` を射影とする。
    また開集合 :math:`U \in \RR^n` において射影が単射であるならば、
    そのような :math:`U` を集めて
    :math:`\set{(\pi(U), (\pi|U)\inv)}` を構成すると、トーラスの座標近傍系となる。

  * トーラス上の微分形式とは：

    #. :math:`\RR^n` の座標を使って書かれる。
    #. 二つの座標近傍の共通部分上において一致する。
    #. ただし :math:`f_{\dots}(\bm x)` はすべての :math:`\bm n \in \ZZ^n` について
       :math:`f_{\dots}(\bm x + \bm n) = f_{\dots}(\bm x)` となる。

       特に :math:`f_{\dots}` が定数関数であれば、トーラス上の p 形式であるといえる。

* 多様体間の :math:`C^\infty` 級写像 :math:`\fn{F}{M}N` は
  :ref:`例題 2.2.5 <tsuboi08.2.2.5>` にあるように
  線形写像 :math:`\fn{F^*}{T_{F(x)}^*N}T_x^*M` を引き起こすが、
  同時に線形写像 :math:`\fn{F^*}{\extp^p T_{F(x)}^*N} \extp^p T_x^*M` を引き起こす。

  .. math::

     \begin{align*}
     F^*((\dd y_{i_1} \wedge \dotsb \wedge \dd y_{i_p})_{F(x)})
     &= F^*(\dd y_{i_1})_{F(x)} \wedge \dotsb \wedge F^*(\dd y_{i_p})_{F(x)}\\
     &= \dd (y_{i_1} \circ F)_x \wedge \dotsb \wedge \dd (y_{i_p} \circ F)_x.
     \end{align*}

  引き戻しが定義できることがわかる。

.. _tsuboi08.2.3.6:

* 命題 2.3.6: 引き戻し :math:`\fn{F^*}{\varOmega^p(N)}\varOmega^p(M)`

  * :ref:`定義 1.8.3 <tsuboi08.1.8.4>` と同じ命題？

.. _tsuboi08.2.3.7:

* 命題 2.3.7: 反変性 :math:`(F \circ G)^* = G^* \circ F^*`

  * :math:`C^\infty` 級写像 :math:`\fn{F}{M}N` および :math:`\fn{G}{L}M` に対して
    定まる引き戻し :math:`\fn{F^*}{\varOmega^p(N)}\varOmega^p(M)` および
    :math:`\fn{G^*}{\varOmega^p(M)}\varOmega^p(L)` について表題の等式が成り立つ。

  * cf. :ref:`例題 1.8.9 <tsuboi08.1.8.9>`

.. _tsuboi08.2.3.8:

* 例 2.3.8: 制限と射影

  * :math:`\RR^n` 内の開集合 :math:`U` と多様体 :math:`M^m` について
    :math:`M^m \subset U` ならば包含写像 :math:`\fn{\iota}{M^m}U` により
    開集合上の微分形式は多様体上の微分形式に引き戻される。

    .. math::

       \alpha \in \varOmega^p(U) \longmapsto \iota^*\alpha \in \varOmega^p(M^m).

    * 実は任意の微分形式についてある近傍のある微分形式の制限となっている。
      これは :ref:`第 1 巻問題 5.2.5 <tsuboi05.5.2.5>` を利用して示せるらしい。

  * :math:`\alpha \in \varOmega^p(T^n)` の引き戻し :math:`\pi^*\alpha \in \varOmega^p(\RR^n)` は
    :math:`\alpha` を :math:`\RR^n` 上で表示する p 形式である。

    * 「:math:`\ZZ^n` 周期的」という修飾があるが……。

.. _tsuboi08.2.3.9:

* 定義 2.3.9 外積

  次の対応は準同型（線形写像）である：

  .. math::

     \fnm{\wedge}{\extp^p T_x^*M \times \extp^q T_x^*M}{\extp^{p + q}T_x^*M}
     {(\dd x_{i_1} \wedge \dotsb \wedge \dd x_{i_p},\ 
       \dd x_{j_1} \wedge \dotsb \wedge \dd x_{j_q})}
       \dd x_{i_1} \wedge \dotsb \wedge \dd x_{i_p}
       \wedge
       \dd x_{j_1} \wedge \dotsb \wedge \dd x_{j_q}.

  演算にはユークリッド空間バージョン :ref:`定義 1.6.2 <tsuboi08.1.6.2>` の規則を適用する。

* 同時に外積 :math:`\fn{\wedge}{\varOmega^p(M) \times \varOmega^q(M)}\varOmega^{p + q}(M)` が導かれる。

  * :ref:`定義 2.1.7 <tsuboi08.2.1.7>` と :ref:`例題 1.8.8 <tsuboi08.1.8.8>` を参照。

.. _tsuboi08.2.3.10:

* 命題 2.3.10: 次数付き可換性

  * ユークリッド空間バージョンの :ref:`例題 1.6.4 <tsuboi08.1.6.4>` を参照。

.. _tsuboi08.2.3.11:

* 命題 2.3.11: 引き戻しの分配律

  * ユークリッド空間バージョンの :ref:`例題 1.8.8 <tsuboi08.1.8.8>` を参照。

2.4 外微分とドラーム・コホモロジー
======================================================================
.. _tsuboi08.2.4.1:

* 定義 2.4.1: 外微分

  * cf. :ref:`定義 1.6.5 <tsuboi08.1.6.5>`
  * :ref:`定義 2.1.7 <tsuboi08.2.1.7>` と :ref:`定理 1.8.11 <tsuboi08.1.8.11>` を参照。

.. _tsuboi08.2.4.2:

* 定理 2.4.2: :math:`\fn{\dd \circ \dd}{\varOmega^p(M)}\varOmega^{p + 2}(M)` は 0 準同型である

  下の図式は準同型の系列である：

  .. math::

     \require{AMScd}
     \begin{CD}
     0 @>{\dd}>> \varOmega^0(M) @>{\dd}>> \varOmega^1(M) @>{\dd}>> \cdots @>{\dd}>> \varOmega^n(M) @>{\dd}>> 0
     \end{CD}

  * 準同型＝ベクトル空間の線形写像と思って読んでいる。
  * cf. :ref:`定理 1.7.1 <tsuboi08.1.7.1>`

.. _tsuboi08.2.4.3:

* 定義 2.4.3: 多様体のドラーム複体

  * 先ほどの図式、正式に言うと
    多様体の微分形式の `コチェイン複体 <http://mathworld.wolfram.com/CochainComplex.html>`__ 
    を多様体 :math:`M` のドラーム複体と呼ぶ。

  * 記号は :math:`\varOmega^*(M)` とする。
  * 複体というのは性質 :math:`\dd \circ \dd = 0` のことだ。
  * :math:`\im(\dd) \subset \ker(\dd)` の「差」をはかるのに
    コホモロジー群という群を使う。

.. _tsuboi08.2.4.4:

* 定義 2.4.4: `ドラーム・コホモロジー <http://mathworld.wolfram.com/deRhamCohomology.html>`__ 群

  .. math::

     \begin{align*}
     \H^p(M) &=
     \ker(\fn{\dd}{\varOmega^p(M)}\varOmega^{p + 1}(M))/
     \im(\fn{\dd}{\varOmega^{p - 1}(M)}\varOmega^p(M))\\
     &= Z^p(M)/B^p(M).
     \end{align*}

  * :math:`\H^p(M)` は商空間である。

    線形写像の :math:`\im` と :math:`\ker` の性質によると
    :math:`B^p(M)` と :math:`Z^p(M)` はどちらも
    :math:`\varOmega^p(M)` の部分ベクトル空間である。
    ここで :math:`B^p(M)` は :math:`Z^p(M)` の部分空間でもあるので、この商空間が成立する。

  * :math:`Z^p(M) = \ker(\fn{\dd}{\varOmega^p(M)}\varOmega^{p + 1}(M))` の元を
    `閉 p 形式 <http://mathworld.wolfram.com/ClosedForm.html>`__ という。
  * :math:`B^p(M) = \im(\fn{\dd}{\varOmega^{p - 1}(M)}\varOmega^p(M))` の元を
    `完全 p 形式 <http://mathworld.wolfram.com/ExactForm.html>`__ という。
  * :math:`[\alpha] \in \H^p(M)` を :math:`\alpha \in \varOmega^p(M)` の
    `コホモロジー <http://mathworld.wolfram.com/Cohomology.html>`__ 類という。
  * :math:`\H^*(M) = \bigoplus_{p = 0}^n \H^p(M)` と書く。

    * このベクトル空間の直和は何を意味するのかが今はわからない。

.. figure:: /_images/cd-derham-cohomology.png
   :align: center
   :alt: math.TODO
   :width: 478px
   :height: 220px
   :scale: 100%

.. _tsuboi08.2.4.5:

* 例 2.4.5:

  * \(1) :math:`\H^0(M)` は :math:`M` の連結成分で定数となる関数全体のなすベクトル空間である。
    これは :math:`\forall f \in Z^0(M)` が局所的定数関数であることによる。

  * \(2) 星型 :math:`U \subset \RR^n` に対して次が成り立つ：

    .. math::

       \H^p(U)
       \begin{cases}
       \cong \RR & \text{if } p = 0,\\
       = 0 & \text{if } p > 0.
       \end{cases}

.. _tsuboi08.2.4.6:

* 例 2.4.6: :math:`S^1 = \RR/\ZZ,\ \H^1(S^1) \cong \RR`

  * :math:`\varOmega^1(S^1) = Z^1(S^1).`
  * :math:`f(t)\,\dd t \in B^1(S^1) \iff \displaystyle \int_0^1\! f(t)\,\dd t = 0.`
    整数周期性による。
  * 次の対応が同型である：

    .. math::

       [\alpha] \longmapsto \int_0^1\!\alpha.

.. _tsuboi08.2.4.7:

* 例 2.4.7: :math:`T^n`

  :math:`\displaystyle \sum_{i_1 < \dotsb < i_p} a_{i_1 \dots i_p}\,\dd x_{i_1} \wedge \dotsb \wedge \dd x_{i_p} \in B^p(T^n).`

.. _tsuboi08.2.4.8:

* 例 2.4.8: :math:`\H^*(T^2)` をフーリエ展開を利用して求める。

  1. :math:`\H^0(T^2) \cong \RR` である。
     :ref:`例 2.4.5 (1) <tsuboi08.2.4.5>` による。

  2. :math:`H^1(T^2)` を求める。

     * :ref:`例 2.3.5 <tsuboi08.2.3.5>` によると
       :math:`T^2` 上の微分形式は :math:`\RR^2` 上の周期関数を係数とする
       微分形式で表される。そこで :math:`\alpha = g_1\,\dd x_1 + g_2\,\dd x_2 \in \varOmega^1(T^2)`
       として、各関数をフーリエ級数の形式で表示する：

       .. math::

          g_1 = \sum a_{n_1 n_2} \exp(2\pi\sqrt{-1}(n_1 x_1 + n_2 x_2))\\
          g_2 = \sum b_{n_1 n_2} \exp(2\pi\sqrt{-1}(n_1 x_1 + n_2 x_2))

     * ここで :math:`g_1, g_2` の性質を確認する。

       * :math:`g_1 \in C^\infty(T^2)` の条件は
         :math:`\forall r > 0, \sum(n_1^2 + n_2^2)^{(r/2)}\abs{a_{n_1 n_2}} < \infty` である。
         :math:`g_2` についても同様の条件である。

       * :math:`g_1 \in \RR` の条件は
         :math:`a_{-n_1 -n_2} = \overline{a_{n_1 n_2}}` である。
         :math:`g_2` についても同様の条件である。

     * :math:`\dd\alpha` を計算することで
       :math:`\alpha \in Z^1(T^2)` の条件が :math:`n_1 b_{n_1 n_2} - n_2 a_{n_1 n_2} = 0`
       であることがわかる。

       このことから :math:`n_1 \ne 0 \implies b_{n_1 0} = 0` と
       :math:`n_2 \ne 0 \implies a_{0 n_2} = 0` がわかる。

     * 関数 :math:`f = \sum c_{n_1 n_2} \exp(2\pi\sqrt{-1}(n_1 x_1 + n_2 x_2))` が
       :math:`\dd f = \alpha` を満たす条件を探る。

       .. math::

          \dd f = 2\pi\sqrt{-1}\left(\sum n_1 c_{n_1 n_2} \exp(\dots)\,\dd x_1
                               + \sum n_2 c_{n_1 n_2} \exp(\dots)\,\dd x_2\right).

       したがって次が条件である：

       * :math:`a_{n_1 n_2} = 2\pi\sqrt{-1} n_1 c_{n_1 n_2}`
       * :math:`b_{n_1 n_2} = 2\pi\sqrt{-1} n_1 c_{n_1 n_2}`

     * 先ほどの :math:`\dd\alpha` の計算結果により、
       :math:`\dd f = \alpha` には :math:`b_{00} = a_{00} = 0` が必要。
       このとき :math:`n_1 \ne 0, n_2 \ne 0` ならば、
       次のように係数をおけば :math:`n_1 b_{n_1 n_2} = n_2 a_{n_1 n_2}` だから
       適切である。

       .. math::

          c_{n_1 n_2} = \frac{a_{n_1 n_2}}{2\pi\sqrt{-1}n_1}
                      = \frac{b_{n_1 n_2}}{2\pi\sqrt{-1}n_1}.

     * 次の場合分けで :math:`c_{n_1 n_2}` が :math:`c_{00}` を除いて定まる：

       .. math::

          n_1 \ne 0 \implies c_{n_1 0} = \frac{a_{n_1 0}}{2\pi\sqrt{-1}n_1}\\
          n_2 \ne 0 \implies c_{0 n_2} = \frac{b_{0 n_2}}{2\pi\sqrt{-1}n_1}.

     * :math:`c_{00} = 0` とすると :math:`f` は :math:`C^\infty` 級であり（収束評価を示す必要がある）、
       :math:`\dd f = \alpha` が成り立つ。

     以上より :math:`\H^1(T^2) \cong \RR^2` であり、
     :math:`\alpha` とフーリエ級数の定数項 :math:`(a_{00}, b_{00})` が対応する。

  3. :math:`\H^2(T^2)` を求める。

     :math:`\beta = h\,\dd x_1 \wedge \dd x_2 \in \varOmega^2(T^2)` などとおいて、
     同様の検討を行なう。ここで :math:`\beta = \dd\alpha` かつ

     .. math::

        h = \sum e_{n_1 n_2}\exp(2\pi\sqrt{-1}(n_1 x_1 + n_2 x_2))

     とおく。

     結果だけ書くと :math:`\H^2(T^2) \cong \RR` であり、
     :math:`\beta` とフーリエ級数の定数項 :math:`e_{00}` が対応する。

.. _tsuboi08.2.4.9:

* 問題 2.4.9

  * 仮定

    * :math:`A = \RR^2\minuszero`
    * :math:`r > 1`
    * :math:`(x_1, x_2) \sim (y_1, y_2) \iff \exists n \in \ZZ \quad\text{s.t. }(y_1, y_2) = (r^n x_1, r^n x_2).`
    * :math:`X = A/\sim`
    * :math:`\fn{\pi}{A}X` を射影とする。

  #. 次が成り立つ：

     .. math::

        \alpha = \frac{a_{11}x_1 + a_{12}x_2}{x_1^2 + x_2^2}\,\dd x_1
                +\frac{a_{21}x_1 + a_{22}x_2}{x_1^2 + x_2^2}\,\dd x_2
        \in \varOmega^1(A),\\
        \exists \beta \in \varOmega^1(X)\quad\text{s.t. }
        \alpha = \pi^* \beta.

     * 解答を読んでも理屈がわからない。
       :math:`\fn{h^n}{A}{A}{(x_1, x_2)}(r^n x_1, r^n x_2)` を考えると
       :math:`(h^n)^* \alpha = \alpha` が成り立つことはわかるのだが。

  #. :math:`\beta \in Z^2(X)` となる条件

     * この条件は :math:`\alpha \in Z^1(X)` となる条件と同値である。
     * :math:`\dd \alpha = 0` を吟味すると :math:`a_{11} = a_{22}, a_{21} = -a_{12}` が条件だとわかる。

     .. todo:: SymPy を利用して数式コードを生成する。

  #. 次の条件における :math:`\gamma_1` に沿った :math:`\beta \in Z^2(X)` の線積分

     * :math:`\rho > 0`
     * :math:`\fnm{\gamma_1}{[0, 1]}{X}{t}\pi(\rho\cos 2\pi t, \rho\sin 2\pi t)`

     円周率の記号と射影の記号がカブっているが、我慢する。

     :math:`\gamma_1 = \pi \circ \gamma` とおくと最初の展開が理解できる。
     最後には上の結果を用いて式を簡略化できる：

     .. math::

        \begin{align*}
        \int_{\gamma_1}\!\beta
        &= \int_{\pi \circ \gamma}\!\beta
        = \int_\gamma\!\pi^*\beta = \int_\gamma\!\alpha\\
        &= \int_0^1\!\alpha \circ \gamma\,\dd t\\
        &= \cdots
        \end{align*}

     .. todo:: SymPy で計算して答え合わせ

  #. 次の条件における :math:`\gamma_2` に沿った :math:`\beta \in Z^2(X)` の線積分

     * :math:`\theta \in \RR`
     * :math:`\fnm{\gamma_2}{[0, 1]}{X}{t}\pi(r^t\cos\theta, r^t\sin\theta)`

     .. todo:: SymPy で計算して答え合わせ

     .. a_1 \log r

.. _tsuboi08.2.4.10:

* 命題 2.4.10: コチェイン写像

  :math:`C^\infty` 写像 :math:`\fn{F}{M}N` に対する引き戻し
  :math:`\fn{F^*}{\varOmega^p(N)}\varOmega^p(M)` はコチェイン写像である：

  .. math::

     F^*\,\dd = \dd\,F^*.

  * :ref:`命題 2.3.6 <tsuboi08.2.3.6>` と :ref:`定理 1.8.11 <tsuboi08.1.8.11>` を参照。

.. _tsuboi08.2.4.11:

* 定理 2.4.11: 上記 :math:`F` は準同型 :math:`\fn{F^*}{\H^p(N)}\H^p(M)` を引き起こす

  * :math:`\alpha \in Z^p(N)` に対して :math:`\dd \alpha = 0` だから
    :math:`0 = F^*\,\dd \alpha = \dd F^*\alpha` であるので、
    :math:`F^* \alpha \in Z^p(M).`

  * :math:`\alpha \in B^p(N)` に対して :math:`\alpha = \dd \beta` なる
    :math:`\beta \in \varOmega^{p - 1}(N)` が存在する。一方、
    :math:`F^* \alpha = F^*\,\dd \beta = \dd F^*\beta` より
    :math:`F^* \alpha \in B^p(M).`

  以上より、次の対応は準同型であると言える：

  .. math::

     \fn{F^*}{\ker(\fn{\dd}{\varOmega^p(N)}\varOmega^{p + 1}(N))}
     \im(\fn{\dd}{\varOmega^{p - 1}(N)}\varOmega^p(N))

  * ベクトル空間としても外積代数としても準同型である。

.. _tsuboi08.2.4.12:

* 命題 2.4.12: :ref:`例題 1.6.7 <tsuboi08.1.6.7>` の多様体バージョン

.. _tsuboi08.2.4.13:

* 命題 2.4.13: ドラーム・コホモロジーにおける外積

  * 外積 :math:`\fn{\wedge}{\varOmega^p(M) \times \varOmega^q(M)}\varOmega^{p + q}(M)` は
    :math:`\H^p(M) \times \H^q(M)` 上に外積
    :math:`\fn{\wedge}{\H^p(M) \times \H^q(M)}\H^{p + q}(M)` を定義する。

  * :math:`[\alpha] \wedge [\beta] = [\alpha \wedge \beta]` という演算規則が成り立つ。
  * :math:`C^\infty` 写像 :math:`\fn{F}{M}N` に対して、
    :math:`F^*([\alpha] \wedge [\beta]) = F^*([\alpha]) \wedge F^*([\beta])` が成り立つ（外積代数の準同型）。

.. _tsuboi08.2.4.14:

* 注意 2.4.14: 2.9.6 予告。

.. _tsuboi08.2.4.15:

* 命題 2.4.15: :ref:`注意 1.9.2 <tsuboi08.1.9.2>` 多様体バージョン

  :math:`\fn{I_a^{(U)}}{\varOmega^p([0, 1] \times M)}\varOmega^{p - 1}([0, 1] \times M)` に対して
  次が成り立つ：

  .. math::

     \dd I_a(\alpha) + I_a(\dd \alpha) = \alpha - \pi^*(\iota_a^*\alpha).

  * これを示すには :math:`(\id \times (\varphi \circ \psi\inv))^* I_a^{(U)}\alpha^{(U)} = I_a^{(U)}\alpha^{(U)}` を示し、
    次に :ref:`定義 2.1.7 <tsuboi08.2.1.7>` により無印の :math:`I_a` が定義される。
    この :math:`I_a` は :ref:`命題 1.9.1 <tsuboi08.1.9.1>` と
    :ref:`注意 1.9.2 <tsuboi08.1.9.2>` により上の式を満たす。

  * 座標近傍 :math:`(U, \varphi)`, :math:`(V, \psi)` および
    :math:`\alpha \in \varOmega^p([0, 1] \times M)` の

    * :math:`[0, 1] \times \varphi(U)` における表示 :math:`\alpha^{(U)}` の :math:`\dd x_0` を含む成分

    を :math:`(\id \times (\varphi \circ \psi\inv))^*` で引き戻すと、:math:`\alpha` の

    *  :math:`[0, 1] \times \psi(V)` における表示 :math:`\alpha^{(V)}` の :math:`\dd x_0` を含む成分

    に :math:`[0, 1] \times \psi(U \cap V)` 上一致する。
    なぜならば :math:`\alpha^{(V)} = (\id \times (\varphi \circ \psi\inv))^*\alpha^{(U)}` だったから。

.. _tsuboi08.2.4.16:

* 定理 2.4.16: :math:`[0, 1] \times M \cong \H^p(M)`

  * :math:`\fn{\pi}{[0, 1] \times M}M`,
    :math:`\fn{\iota_a}{M}[0, 1] \times M` が
    ドラーム・コホモロジー群に誘導する写像
    :math:`\fn{\pi^*}{\H^p(M)}\H^p([0, 1] \times M)`,
    :math:`\fn{\iota_a^*}{\H^p([0, 1] \times M)}M`
    は同型である。

  * さらに

    .. math::

       \begin{align*}
       \iota_a^* \pi^* &= \id_{\H^p(M)}\\
       \pi^* \iota_a^* &= \id_{\H^p([0, 1] \times M)}
       \end{align*}

    である。したがって :math:`\iota_0^* = (\pi^*)\inv = \iota_1.`

  * 証明

    * :math:`\pi \circ \iota_a = \id_M` および :ref:`命題 2.3.7 <tsuboi08.2.3.7>` より
      :math:`\iota_a^* \pi^* = \id_M^*,\ \id_M^* = \id_{\H^p(M)}.`

    * :math:`(\iota_a \circ \pi)^* = \pi^* \circ \iota_a^*` および
      :ref:`命題 2.4.15 <tsuboi08.2.4.15>` より

      * :math:`p > 0` のときは次が成り立つ
        :math:`\dd I_a(\alpha) + I_a(\dd \alpha) = \alpha - \pi^*(\iota_a^*\alpha),\ \alpha`
        が存在する：

        .. math::

           \dd I_a(\alpha) + I_a(\dd \alpha) = \alpha - \pi^*(\iota_a^*\alpha).

        * :math:`\alpha \in Z^p([0, 1] \times M)` とすると、
          :math:`\dd \alpha = 0` につき
          :math:`\dd I_a(\alpha) = \alpha - \pi^*(\iota_a^*\alpha).`

        * これをコホモロジー類で考えると
          :math:`[\alpha] - [\pi^*(\iota_a^*\alpha)] = 0.`

        * ゆえに :math:`\pi^*\iota_a = \id_{\H^p([0, 1] \times M)}.`

      * :math:`p = 0` のときは :math:`\alpha \in Z^0([0, 1] \times M)`
        は局所的定数関数であるので :math:`\pi^*(\iota_a^*\alpha)` と一致する。

.. _tsuboi08.2.4.17:

* 定義 2.4.17: :math:`C^\infty` `ホモトピック <http://mathworld.wolfram.com/Homotopic.html>`__

  二つの :math:`C^\infty` 級写像 :math:`\fn{\varphi_0, \varphi_1}{M}N` が
  :math:`C^\infty` ホモトピックであるとは、
  次の性質を満たす :math:`C^\infty` 級写像 :math:`\fn{\varphi}{[0, 1] \times M}N` が存在することをいう：

  .. math::

     \varphi_0 = \varphi(0, x),\\
     \varphi_1 = \varphi(1, x).

.. _tsuboi08.2.4.18:

* 定理 2.4.18: :math:`\varphi_0, \varphi_1` がホモトピックならば
  :math:`\varphi_0^*, \varphi_1^*` もホモトピックである

  * :math:`\varphi_k = \varphi \circ \iota_k\ (k = 0, 1)` と
  * :ref:`定理 2.4.16 <tsuboi08.2.4.16>` により

  :math:`\fn{\iota_0^* = \iota_1^*}{\H^p([0, 1] \times M)}\H^p(M)` である。
  したがって
  :math:`\varphi_0^* = \iota_0^* \varphi^* = \iota_1^* \varphi^* = \varphi_1^*.`

.. _tsuboi08.2.4.19:

* 問題 2.4.19: :math:`\RR^m \times M` に対し :math:`\H^p(\RR^m \times M) \cong \H^p(M)`

  * :math:`\fnm{\pi}{\RR^m \times M}{M}{(\bm x, y)}y`
  * :math:`\fnm{\iota}{M}{\RR^m \times M}{y}(0, y)`

  とおくと、
  :math:`\pi \circ \iota = \id_M` より :math:`(\pi \circ \iota)^* = \iota^*\pi^* = \id_{\H^p(M)}.`

  * :math:`\fnm{\varphi}{[0, 1]\times \RR^m}{\RR^m \times M}{(t, \bm x, y)}(t\bm x, y)` とおいて、
    ホモトピー

    * :math:`\varphi_0 = \iota\circ\pi`
    * :math:`\varphi_1 = \id_{\RR^m \times M}`

    を与える。

    * :math:`(\iota\circ\pi)^* = \id_{\RR^m \times M}^* = \id_{\H^p(\RR^m \times M)}.`

  * :math:`(\iota\circ\pi)^* = \pi^*\circ\iota^*` だから :math:`\pi^*, \iota^*` は
    同型写像である。
