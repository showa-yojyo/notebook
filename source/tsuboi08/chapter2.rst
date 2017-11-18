======================================================================
幾何学 III 微分形式 読書ノート 2/6
======================================================================

:doc:`chapter1` からの続き。

.. contents:: ノート目次

第 2 章 多様体上の微分形式
======================================================================
本巻ではユークリッド空間内の多様体のパラーメーター表示に対して、
その表示による引き戻しにより微分形式が表示されていると考える。

2.1 多様体（基礎）
----------------------------------------------------------------------
序盤は :doc:`/tsuboi05/index` のおさらいのようになっている。

* 定義 2.1.1: 多様体の定義

  * :ref:`第 1 巻定義 3.1.1 <tsuboi05.3.1.1>` と同じ。

* 注意 2.1.2: パラコンパクト性に関する注意

  * :ref:`第 1 巻注意 3.1.3 <tsuboi05.3.1.3>` と同じ。

* 定義 2.1.3: 多様体の間の写像の定義

  * 第 1 巻で見覚えあり。

.. _tsuboi08.2.1.4:

* 定理 2.1.4: :ref:`第 1 巻定理 5.1.3 <tsuboi05.5.1.3>` と同じ。
* 定理 2.1.5: :ref:`第 1 巻定理 5.1.3 <tsuboi05.5.3.6>` と同じ。

  * 1 の分割は第 1 巻では多様体上に関数がたくさん存在することなどに
    利用されていた。本巻は
    後で出てくるマイヤー・ビエトリス完全系列、チェック・ドラーム複体、
    向き付けられた多様体上の積分の定義に利用される。

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
----------------------------------------------------------------------
* 接ベクトルの定義と似せて、微分形式を関数の同値類として定義する。
* 多様体上の点において微分可能な関数 :math:`f_1, f_2` が同値であることを
  次のように定義する：

  .. math::

     f_1 \sim f_2 \iff \dd{(f_1 \circ \varphi\inv)}_{(\varphi(x)} = \dd{(f_2 \circ \varphi\inv)}_{(\varphi(x))}.

* 座標近傍 :math:`(U, \varphi),\ (V, \psi)` について :math:`f_1 \sim f_2 \implies \dd{(f_1 \circ \psi\inv)}_{(\psi(x)} = \dd{(f_2 \circ \psi\inv)}_{(\psi(x)}`
  である。

  * このことは :math:`\dd{(\varphi^*f)} = \varphi^*\dd f` や
    :math:`f_k \circ \psi\inv = f_k \circ \varphi\inv \circ \varphi \circ \psi\inv` を使って示せる。

* 定義 2.2.1: `余接空間 <https://en.wikipedia.org/wiki/Cotangent_space>`__

  .. math::

     T_x^*M = C^\infty(M)/\sim.

* 例題 2.2.2: 余接空間は :math:`C^\infty(M)` の実ベクトル空間から定まるベクトル空間である。

  * 写像 :math:`[f] \in C^\infty(M) \longmapsto \left(\dfrac{\partial f}{\partial x_1}(\varphi(x)), \dotsc, \dfrac{\partial f}{\partial x_n}(\varphi(x))\right) \in \RR^n`
    が準同型写像（線形写像と言いたい？）となる：

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

* :math:`T_x^*M` の基底を :math:`\dd x_1, \dotsc, \dd x_n` と書く。

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

* 定義 2.2.3: 多様体上の 1 形式

  * :math:`x \in M`
  * :math:`f_i \in C^\infty(M)`

  このとき各座標近傍上での一次結合への対応
  :math:`x \longmapsto \displaystyle \sum_{i = 1}^n f_i\,\dd x_i \in T_x^*M` を表題のように呼ぶ。

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

* 問題 2.2.6: ステレオグラフ

  多様体上では 1 形式と接ベクトルとをはっきり区別して考える必要があることを示すデモのような問題だ。
  単位球面の北極と南極に関して投影写像を次のようにとる：

  .. math::

     \fnm{\pi_N}{S^2\setminus\set{p_N}}{\RR^2}{(x_1, x_2, x_3)}(v_1, v_2) = \left(\frac{x_1}{1 - x_3}, \frac{x_2}{1 - x_3}\right),\\
     \fnm{\pi_S}{S^2\setminus\set{p_S}}{\RR^2}{(x_1, x_2, x_3)}(u_1, u_2) = \left(\frac{x_1}{1 + x_3}, \frac{x_2}{1 + x_3}\right).

  * 各投影写像の逆写像？
  * 座標近傍系 :math:`\set{(S^2\setminus\set{p_N}, \pi_N), (S^2\setminus\set{p_S}, \pi_S)}` の座標変換？

  .. todo:: 上の 2 問の解答に必要な数式を SymPy に生成させる。

  * 下に示す平面上の多項式係数のベクトル場について :math:`(\pi_N\inv)_*\xi` が
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

  * 下に示す平面上の多項式係数の 1 形式について :math:`\pi_N^* \alpha` が
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
----------------------------------------------------------------------
* 定義 2.3.1: p 次外積の空間 :math:`\extp^p T_x^*M`

  余接空間 :math:`T_x^*M` の p 次外積空間とは、
  :math:`1 \le i_1 \le \dotsb \le i_p \le n` なる自然数の添字に対応する
  記号 :math:`\dd x_{i_1} \wedge \dotsb \wedge \dd x_{i_p}` を基底とする
  ベクトル空間のことをいう。

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

       \dd{y_{j_1}} \wedge \dotsb \wedge \dd{y_{j_p}} = \operatorname{sign}
       \begin{pmatrix}j_1 & \dots & j_p\\k_1 & \dots & k_p\end{pmatrix}
       \dd{y_{k_1}} \wedge \dotsb \wedge \dd{y_{k_p}}.

  * cf. :ref:`定義 1.6.8 <tsuboi08.1.6.8>`

* 注意 2.3.3: 外積空間の座標変換は外積と両立するように定義されている。

* 定義 2.3.4: 多様体上の微分形式 (2)

  * 各座標近傍上で、各点における余接空間の外積空間 :math:`\extp^p T_x^*M` の元を、
    :math:`f_{i_1\dots i_p}` が :math:`C^\infty` 級であるように、
    :math:`f_{i_1\dots i_p}\,\dd x_{i_1} \wedge \dotsb \dd x_{i_p}` に対応させるものを
    この多様体上の :math:`C^\infty` 級微分 p 形式という。

  * 記号 :math:`\Omega^p(M)` で p 形式の空間を表す。
    多様体が 1 次元以上であればこれは無限次元のベクトル空間である。

  * cf. :ref:`定義 2.1.7 <tsuboi08.2.1.7>`

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
     F^*((\dd y_{i_1} \wedge \dotsb \wedge y_{i_p})_{F(x)})
     &= F^*(\dd y_{i_1})_{F(x)} \wedge \dotsb \wedge F^*(\dd y_{i_p})_{F(x)}\\
     &= \dd (y_{i_1} \circ F)_x \wedge \dotsb \wedge \dd (y_{i_p} \circ F)_x.
     \end{align*}

  引き戻しが定義できることがわかる。

* 命題 2.3.6: 引き戻し :math:`\fn{F^*}{\Omega^p(N)}\Omega^p(M)`

  * :ref:`定義 1.8.3 <tsuboi08.1.8.4>` と同じ命題？

* 命題 2.3.7: 反変性 :math:`(F \circ G)^* = G^* \circ F^*`

  * :math:`C^\infty` 級写像 :math:`\fn{F}{M}N` および :math:`\fn{G}{L}M` に対して
    定まる引き戻し :math:`\fn{F^*}{\Omega^p(N)}\Omega^p(M)` および
    :math:`\fn{G^*}{\Omega^p(M)}\Omega^p(L)` について表題の等式が成り立つ。

  * cf. :ref:`例題 1.8.9 <tsuboi08.1.8.9>`

* 例 2.3.8: 制限と射影

  * :math:`\RR^n` 内の開集合 :math:`U` と多様体 :math:`M^m` について
    :math:`M^m \subset U` ならば包含写像 :math:`\fn{\iota}{M^m}U` により
    開集合上の微分形式は多様体上の微分形式に引き戻される。

    .. math::

       \alpha \in \Omega^p(U) \longmapsto \iota^*\alpha \in \Omega^p(M^m).

    * 実は任意の微分形式についてある近傍のある微分形式の制限となっている。
      これは :ref:`第 1 巻問題 5.2.5 <tsuboi05.5.2.5>` を利用して示せるらしい。

  * :math:`\alpha \in \Omega^p(T^n)` の引き戻し :math:`\pi^*\alpha \in \Omega^p(\RR^n)` は
    :math:`\alpha` を :math:`\RR^n` 上で表示する p 形式である。

    * 「:math:`\ZZ^n` 周期的」という修飾があるが……。

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

* 同時に外積 :math:`\fn{\wedge}{\Omega^p(M) \times \Omega^q(M)}\Omega^{p + q}(M)` が導かれる。

  * :ref:`定義 2.1.7 <tsuboi08.2.1.7>` と :ref:`例題 1.8.8 <tsuboi08.1.8.8>` を参照。

* 命題 2.3.10: 次数付き可換性

  * ユークリッド空間バージョンの :ref:`例題 1.6.4 <tsuboi08.1.6.4>` を参照。

* 命題 2.3.11: 引き戻しの分配律

  * ユークリッド空間バージョンの :ref:`例題 1.8.8 <tsuboi08.1.8.8>` を参照。

2.4 外微分とドラーム・コホモロジー
----------------------------------------------------------------------
TBW

----

:doc:`chapter3` へ。
