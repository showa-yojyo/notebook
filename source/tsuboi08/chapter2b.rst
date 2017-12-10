======================================================================
第 2 章 多様体上の微分形式（後半）
======================================================================

:doc:`chapter2a` からの続き。

.. contents:: ノート目次

2.5 関手という見方
======================================================================
* 本書では `関手 <http://mathworld.wolfram.com/Functor.html>`__ の正式な定義は与えていない。

* 下に挙げるような、

  #. `対象 <http://mathworld.wolfram.com/Object.html>`__ と
  #. 合成写像と恒等写像があるような `射 <http://mathworld.wolfram.com/Morphism.html>`__

  の組を抽象化する理論があるらしい。以下その例：

  * :math:`C^\infty` 級多様体全部とそれらの間の :math:`C^\infty` 級写像の全体
  * ベクトル空間全部と線型写像全部
  * コチェイン複体全部とコチェイン写像全部

* 多様体に微分形式を与える対応は（多様体、写像）から
  （コチェイン複体、コチェイン写像）への `反変関手 <http://mathworld.wolfram.com/ContravariantFunctor.html>`__
  であるといえる。

  * :math:`\fn{F}{M}N` から
    :math:`\fn{F^*}{\Omega^*(N)}\Omega^*(M)` への対応をいう。

  * :math:`(F_2 \circ F_1)^* = F_1^* \circ F_2^*` という性質がある。

* コホモロジー群をとる対応は（コチェイン複体、コチェイン写像）から
  （ベクトル空間、線型写像）への `共変関手 <http://mathworld.wolfram.com/CovariantFunctor.html>`__
  である。

  * :math:`\fn{F^*}{\Omega^*(N)}\Omega^*(M)` から
    :math:`\fn{F^*}{\H^p(N)}{\H^p(M)}` への対応をいう。

* この二つの結合（反変関手となる）のことが
  :ref:`定理 2.4.11 <tsuboi08.2.4.11>` である。

* やはり同定理より :math:`M` と :math:`N` が微分同相であれば :math:`\H^p(M) \cong \H^p(N)` である。

  * 微分同相でなくとも、

    * :math:`\fn{f}{M}N,\ \fn{g}{N}M` が存在して、
    * 合成写像 :math:`f \circ g` と
      恒等写像 :math:`\id_N` が :math:`C^\infty` ホモトピックであり、
    * 合成写像 :math:`g \circ f` と
      恒等写像 :math:`\id_M` が :math:`C^\infty` ホモトピックである

    ならば :math:`\H^p(M) \cong \H^p(N)` といえる。

* 注意 2.5.1: 上記 :math:`f, g` は実は連続写像にまで緩められる。
  :math:`M` と :math:`N` がホモトピー同値であれば、ドラーム・コホモロジー群は同型となる。

2.6 マイヤー・ビエトリス完全系列
======================================================================
* ドラーム・コホモロジー群の計算ができれば、二つの多様体が異なることを示せる。

.. _tsuboi08.2.6.1:

* 命題 2.6.1

  * :math:`M` をコンパクト多様体の開集合、
  * :math:`M_1 \subset M,\ M_2 \subset M` を :math:`M_1 \cup M_2 = M` なる開集合、
  * :math:`M_{12} = M_1 \cap M_2` とし、
  * :math:`\fn{i_1}{M_{12}}M_1`, :math:`\fn{i_2}{M_{12}}M_2`,
    :math:`\fn{j_1}{M_1}M`, :math:`\fn{j_2}{M_2}M` を包含写像とする。

  このとき、次の写像の列は完全系列である：

  .. math::

     \require{AMScd}
     \begin{CD}
     0 @>>> \Omega^p(M)
       @>{(j_1^*,\ j_2^*)}>> \Omega^p(M_1) \oplus \Omega^p(M_2)
       @>{i_1^* - i_2^*}>> \Omega^p(M_{12})
       @>>> 0
     \end{CD}

  #. :math:`(j_1^*, j_2^*)` が単射であることを示す：

     * :math:`j_1, j_2` はそれぞれ :math:`M_1, M_2` 上で単射であるので、
       その引き戻しも単射である。
     * 単射の直積もまた単射である。

     ゆえに :math:`(j_1^*, j_2^*)` は単射である。

  #. :math:`\im(j_1^*, j_2^*) = \ker(i_1^* - i_2^*)` を示す：

     :math:`\alpha \in \Omega^p(M)` をとる。このとき次のようになる：

     .. math::

        \begin{align*}
        (i_1^* - i_2^*)\circ(j_1^*, j_2^*)\alpha
        &= (i_1^* - i_2^*)(j_1^*\alpha \oplus j_2^*\alpha)\\
        &= i_1^*j_1^*\alpha - i_2^*j_2^*\alpha\\
        &= \alpha \circ j_1 \circ i_1 - \alpha \circ j_2 \circ i_2\\
        &= \alpha - \alpha = 0.
        \end{align*}

  #. :math:`i_1^* - i_2^*` が全射であることを示す：

     これの証明が複雑だ。まず次のように 1 の分割を構成する：

     * :math:`V_1 \subset \closure{V_1} \subset M_1` であり
       :math:`V_1` は開集合であり :math:`\closure{V_1}` はコンパクトであるようにとる。
     * :math:`V_2` も同様に定義する。
     * :math:`C^\infty` 級関数 :math:`\fn{\lambda_1}{M}\RR` を次のようにとる：

       * :math:`0 \le \lambda_1 \le 1`
       * :math:`\lambda_1|(M \setminus V_2) = 1`
       * :math:`\supp \lambda_1 \subset V_1`

     * :math:`C^\infty` 級関数 :math:`\lambda_2` を :math:`1 - \lambda_1` と定義することで
       :math:`\set{\lambda_1, \lambda_2}` は :math:`\set{M_1, M_2}` に従属する
       1 の分割となる。

       * :math:`M \setminus M_2` の近傍上 :math:`\lambda_2 = 0` である。
         なぜならば :math:`\supp \lambda_2 \subset M_2` がコンパクト部分集合として成り立つから。

     * すべての :math:`\alpha \in \Omega^p(M_{12})` に対して
       :math:`\lambda_2\alpha` を :math:`M \setminus M_2` 上ゼロと定義することで
       :math:`M_{12} \cup (M \setminus M_2) = M_1` 上の p 形式であるように拡張できる。

       ゆえに :math:`\lambda_2\alpha \in \Omega^p(M_1).`

     * 同様にして :math:`-\lambda_1\alpha \in \Omega^p(M_2).`

     .. math::

        \begin{align*}
        (i_1^* - i_2^*)(\lambda_2\alpha - \lambda_1\alpha)
        &= \lambda_2\alpha + \lambda_1\alpha\\
        &= \alpha.
        \end{align*}

.. _tsuboi08.p.62:

* :ref:`命題 2.4.10: コチェイン写像 <tsuboi08.2.4.10>` により
  :ref:`命題 2.6.1 <tsuboi08.2.6.1>` の完全系列を縦に :math:`\dd` でつないだ
  写像のグラフは可換となる。

  .. math::

     \begin{CD}
       @. @A{\dd}AA @A{\dd}AA @A{\dd}AA\\
     0 @>>> \Omega^{p + 1}(M)
       @>{(j_1^*,\ j_2^*)}>> \Omega^{p + 1}(M_1) \oplus \Omega^{p + 1}(M_2)
       @>{i_1^* - i_2^*}>> \Omega^{p + 1}(M_{12})
       @>>> 0\\
       @. @A{\dd}AA @A{\dd}AA @A{\dd}AA\\
     0 @>>> \Omega^p(M)
       @>{(j_1^*,\ j_2^*)}>> \Omega^p(M_1) \oplus \Omega^p(M_2)
       @>{i_1^* - i_2^*}>> \Omega^p(M_{12})
       @>>> 0\\
       @. @A{\dd}AA @A{\dd}AA @A{\dd}AA\\
     0 @>>> \Omega^{p - 1}(M)
       @>{(j_1^*,\ j_2^*)}>> \Omega^{p - 1}(M_1) \oplus \Omega^{p - 1}(M_2)
       @>{i_1^* - i_2^*}>> \Omega^{p - 1}(M_{12})
       @>>> 0\\
       @. @A{\dd}AA @A{\dd}AA @A{\dd}AA
     \end{CD}

* :math:`\alpha \in \Omega^p(M_{12}), \alpha_1 \in \Omega^p(M_1), \alpha_2 \in \Omega^p(M_2)`,
  :math:`i_1^*a_1 - i_2^*a_2 = \alpha.`
* :math:`\dd \alpha_1 \in \Omega^{p + 1}(M_1), \dd \alpha_2 \in \Omega^{p + 1}(M_2)`
  これらは :math:`M_{12}` 上一致し、どちらもある :math:`\beta \in \Omega^{p + 1}(M_{12})`
  を定める。

.. _tsuboi08.2.6.2:

* 命題 2.6.2

  #. 閉形式 :math:`\beta \in \Omega^{p + 1}(M)` について
     :math:`[\beta]` は :math:`\alpha` に対する :math:`\alpha_1, \alpha_2` の取り方によらない。

     * :math:`\alpha = i_1^*\alpha - i_2^*\alpha = i_1^*\alpha' - i_2^*\alpha'` とおく。
       すなわち :math:`i_1^*(\alpha - \alpha') - i_2^*(\alpha_2 = \alpha_2') = 0` である。
     * :ref:`命題 2.6.1 <tsuboi08.2.6.1>` により、
       :math:`\exists \gamma \in \Omega^p(M)\quad\text{s.t.}\quad (j_1^*, j_2^*)\gamma = (\alpha_1 - \alpha_1', \alpha_2 - \alpha_2').`
     * このとき閉形式 :math:`\beta' \in \Omega^{p + 1}(M)` が、
       :math:`\dd \alpha_1' \in \Omega^{p + 1}(M_1), \dd \alpha_2' \in \Omega^{p + 1}(M_2)` が
       :math:`M_{12}` 上で一致することで定まる。
     * したがって :math:`\beta' - \beta = \dd \gamma` となる。
     * ゆえに :math:`[\beta] = [\beta'] \in \H^{p + 1}(M).`

  #. :math:`\alpha` が完全形式であるならば :math:`\beta` もまた完全形式である。

     * :math:`\alpha = \dd \eta` とする。
     * :math:`\exists \eta_1 \in \Omega^{p - 1}(M_1), \exists \eta_2 \in \Omega^{p - 1}(M_2) \quad\text{s.t.}\quad i_1^*\eta_1 - i_2^*\eta_2 = \eta.`
     * :math:`\alpha_1 = \dd \eta_1, \alpha_2 = \dd \eta_2` ととれる。
     * :math:`\dd \alpha_1 = 0, \dd \alpha_2 = 0.`
     * ゆえに :math:`\beta = 0` ととれる。
     * 先ほどの結果を用いると :math:`\alpha_1, \alpha_2` の取り方によらず
       :math:`\beta` は完全形式である。

.. _tsuboi08.2.6.3:

* 定義 2.6.3: 連結準同型 :math:`\fn{\Delta^*}{\H^p(M_{12})}\H^{p + 1}(M)`

  * :ref:`命題 2.6.2 <tsuboi08.2.6.2>` の定め方に従う。

.. _tsuboi08.2.6.4:

* 定理 2.6.4: `マイヤー・ビエトリス完全系列 <https://en.wikipedia.org/wiki/Mayer%E2%80%93Vietoris_sequence>`__

  .. math::

     \begin{CD}
     @. @. \cdots @>{i_1^* - i_2^*}>> \H^{p - 1}(M_{12})\\
     @.\\
     @>{\Delta^*}>> \H^p(M)
     @>{(j_1^*,\ j_2^*)}>> \H^p(M_1) \oplus \H^p(M_2)
     @>{i_1^* - i_2^*}>> \H^p(M_{12})\\
     @.\\
     @>{\Delta^*}>> \H^{p + 1}(M)
     @>{(j_1^*,\ j_2^*)}>> \cdots
     \end{CD}

  * コチェイン複体の完全系列が与えられると、コホモロジー群の完全系列が得られる。
  * 本書 pp. 63-65 が証明であるが、明らかに手間がかかる。
    次のことを全て（任意の順序で）示せばよいようだ：

    #. :math:`\Delta^*(i_1^* - i_2^*) = 0`
    #. :math:`(j_1^*,\ j_2^*)\Delta^* = 0`
    #. :math:`(i_1^* - i_2^*)(j_1^*,\ j_2^*) = 0`
    #. :math:`\ker\Delta^* \subset \im(i_1^* - i_2^*)`
    #. :math:`\ker(j_1^*,\ j_2^*) \subset \im\Delta^*`
    #. :math:`\ker(i_1^* - i_2^*) \subset \im(j_1^*,\ j_2^*)`

  * 核にあるのが閉形式、像にあるのが完全形式。
  * 全般的に閉形式の性質と :ref:`p. 62 <tsuboi08.p.62>` の図を駆使する。

2.7 球面のドラーム・コホモロジー
======================================================================
以下で使う記号：

* :math:`S^1 = \RR/\ZZ` を円とする。
* :math:`\fn{\pi}{\RR}\RR/\ZZ` をその射影とする。
* :math:`M_1 = \pi((0, 1)),\ M_2 = \pi((-1/2, 1/2))` とおくと :math:`S^1` の開被覆となる。

  * 前者は円周を 0 度から 360 度までを、後者は -180 度から 180 度までを表現している。

* :math:`M_{12} = M_1 \cap M_2` とおく。

このマイヤー・ビエトリス完全系列を書くと次のようになる：

.. math::

   \begin{CD}
   0 @>>> \H^0(S^1)
   @>>> \H^0(M_1) \oplus \H^0(M_2)
   @>>> \H^0(M_{12})\\
   @.\\
   @>>> \H^1(S^1)
   @>>> 0
   \end{CD}

上の完全系列は次のものと同型である：

.. math::

   \begin{CD}
   0 @>>> \RR
   @>>> \RR \oplus \RR
   @>>> \RR \oplus \RR\\
   @.\\
   @>>> \H^1(S^1)
   @>>> 0
   \end{CD}

* この例に限らず、:math:`\H^0(\cdot)` は「連結成分上の定数関数」と同一視する。
* 意味のあるコホモロジー群の最初と最後を見ると :math:`\H^1(S^1) \cong \RR` と言える。

.. _tsuboi08.2.7.1:

* 例題 2.7.1: 円の連結準同型

  円周上の :math:`C^\infty` 関数 :math:`\fn{\nu_1}{[0, 1/2]}[0, 1]`,
  :math:`\fn{\nu_2}{[1/2, 1]}[0, 1]` が次のように定義されているときの
  :math:`\fn{\Delta^*}{\H^0(M_{12})}{H^1(S^1)}` の記述はどのようなものか：

  .. math::

     \begin{align*}
     \nu_1(t) &= \begin{cases}
     0 & \quad\text{if } t \in \left[0, \dfrac{1}{6}\right],\\
     \text{(unknown)} & \quad\text{if } t \in \left[\dfrac{1}{6}, \dfrac{1}{3}\right],\\
     1 & \quad\text{if } t \in \left[\dfrac{1}{3}, \dfrac{1}{2}\right],\\
     \end{cases}
     \\
     \nu_2(t) &= \nu_1\left(t - \frac{1}{2}\right).
     \end{align*}

  * まず :math:`M_1, M_2` に従属する 1 の分割 :math:`\lambda_1, \lambda_2` を適宜構成する：

    .. math::

       \begin{align*}
       \lambda_1(t) &=
       \begin{cases}
       \nu_1(t)     & \quad\text{if } t \in \left[0, \dfrac{1}{2}\right],\\
       1 - \nu_2(t) & \quad\text{if } t \in \left[\dfrac{1}{2}, 1\right],
       \end{cases}
       \\
       \lambda_2(t) &= 1 - \lambda_1(t).
       \end{align*}

    これが 1 の分割になっていることは、本書の図を見れば納得できる。

  * 次に :math:`a, b \in \RR` を何かとって、関数 :math:`\fn{M_{12}}\RR` を次のように定義する：

    .. math::

       f(x) =
       \begin{cases}
       a & \quad\text{if } t \in \pi\left(\!\left(0, \dfrac{1}{2}\right)\!\right),\\
       b & \quad\text{if } t \in \pi\left(\!\left(\dfrac{1}{2}, 1\right)\!\right).
       \end{cases}

  * 次のように :math:`M_1, M_2` 上の :math:`C^\infty` 級関数を構成すると、
    :math:`i_1^* f_1 - i_2^* f_2 = f` をみたす（暗算で確認できる）：

    .. math::

       \begin{align*}
       f_1(x) &= \lambda_2(t) f(x) =
       \begin{cases}
       a(1 - \nu_1(t)) & \quad\text{if } t \in \left[0, \dfrac{1}{2}\right],\\
       b \nu_2(t)      & \quad\text{if } t \in \left[\dfrac{1}{2}, 1\right],
       \end{cases}
       \\
       f_2(x) &= -\lambda_1(t) f(x) =
       \begin{cases}
       -a\nu_1(t)       & \quad\text{if } t \in \left[0, \dfrac{1}{2}\right],\\
       -b(1 - \nu_2(t)) & \quad\text{if } t \in \left[\dfrac{1}{2}, 1\right].
       \end{cases}
       \end{align*}

    :math:`f_1` が :math:`M_1` 上滑らかであることは :math:`t = 1/2` における微分可能性を確認すればよい。
    同様に :math:`f_2` が :math:`M_2` 上滑らかであることは :math:`t = 0` を確認すればよい。

  * :math:`M_{12}` 上において :math:`\dd f_1 = \dd f_2 = -a\dd \nu_1 + b\dd v_2` となる。
    この値を :math:`\alpha` とすると次がわかる：

    .. math::

       \alpha = -a\dd \nu_1 + b\dd v_2
       = \left(-a\diff{\nu_1}{t} + b\diff{\nu_2}{t}\right)\dd t
       \in \Omega^1(S^1).

  * したがって :math:`\Delta^*(a, b) = [\alpha]` である。

.. _tsuboi08.2.7.2:

* 注意 2.7.2: 補足

  * :math:`a = b` ならば :math:`f = (i_1^* - i_2^*)(a, 0)`, :math:`\Delta^*(a, a) = 0`
    (:math:`\alpha = \dd(a\lambda_2)`).

  * :math:`a \ne b` ならば :math:`\Delta^*(a, b)` が :math:`\H^1(S^1)` の基底となる。
    :math:`\displaystyle \int_0^1\!\left(-a\diff{\nu_1}{t} + b\diff{\nu_2}{t}\right)\dd t = b - a`
    となって :math:`\nu_1, \nu_2` が消去する。

    * :math:`[\alpha] = [(b - a)\dd t]`

  * :ref:`2.4.6 <tsuboi08.2.4.6>` も参照。

.. _tsuboi08.2.7.3:

* 命題 2.7.3: 一般の多様体次元の :math:`\H^*(S^k)`

  .. math::

     \H^p(S^k) \cong
     \begin{cases}
     \RR & \quad\text{if } p = 0, k\\
     0   & \quad\text{if } 0 < p < k
     \end{cases}

  * まず :math:`H^0(S^k) \cong \RR` であることは言える。
    0 次元のドラームコホモロジー群が球面上の定数関数全体と同一視できるからだ。

  * それ以外の場合については多様体次元 :math:`k` についての帰納法で示す。
    そのために :math:`M_1 = S^k \setminus \set{p_S}`, :math:`M_2 = S^k \setminus \set{p_N}`
    とおく。ここで :math:`p_S, p_N` はそれぞれ南極、北極に相当する点とする。

    * :math:`M_{12} = M_1 \cap M_2` は :math:`(-1, 1) \times S^{k - 1}` と微分同相だ。

  * :ref:`問題 2.4.19 <tsuboi08.2.4.19>` によると :math:`\H^p(M_{12}) \cong H^p(S^{k - 1})` だ。

  * マイヤー・ビエトリス完全系列：

    .. math::

       \begin{CD}
       \cdots @>>> \H^{k - 1}(M_1) \oplus \H^{k - 1}(M_2)
              @>>> \H^{k - 1}(M_{12})
              @>>> \H^k(S^k)
              @>>> 0
       \end{CD}

    においては、帰納法の仮定：

    .. math::

       \H^p(S^{k - 1}) \cong
       \begin{cases}
       \RR & \quad\text{if } p = 0, k - 1\\
       0   & \quad\text{if } 0 < p < k - 1
       \end{cases}

    より、次の系列と同型と言える：

    .. math::

       \begin{CD}
       \cdots @>>> 0 \oplus 0
              @>>> \RR
              @>>> \H^k(S^k)
              @>>> 0
       \end{CD}

    したがって主張が成り立つ。

  * 証明は終わったが次のようなコメントがある。

    * :math:`\lambda_1, \lambda_2` を :math:`M_1, M_2` に従属する 1 の分割とし、
    * :math:`[\omega^{k - 1}]` を :math:`\H^{k - 1}(S^{k - 1})` の基底である

    とすると、次式が成り立つように :math:`\H^k(S^k)` の基底 :math:`[\omega^k]` をとれる：

    .. math::

       [\omega^k] = \Delta^*[\omega^{k - 1}] = [\dd(\lambda_2 \pi^* \omega^{k - 1})].

.. _tsuboi08.2.7.4:

* 問題 2.7.4: :ref:`問題 2.2.6 <tsuboi08.2.2.6>` の状況で

  #. :math:`\RR^3` 上の次の微分形式に対する :math:`(\pi_S\inv)^*(\omega|S^2)` とは：

     .. math::

        \omega = x_1 \dd x_2 \wedge \dd x_3
                -x_2 \dd x_1 \wedge \dd x_3
                +x_3 \dd x_1 \wedge \dd x_2

     まず :math:`\dd x_1, \dd x_2, \dd x_3` を計算する。
     各座標を :math:`u_1, u_2` で表す必要があることに注意。

     .. todo:: SymPy で計算してみる。
     .. 結果だけ書くと :math:`\frac{4 \dd u_1 \wedge \dd u_2}{(1 + u_1^2 + u_2^2)^2}`

  #. :math:`\RR^3\minuszero \times \RR` 上の次の微分形式 :math:`\alpha` に対して、
     全微分がゼロとなる。また、:math:`\RR^2\minuszero` 上の微分形式
     :math:`(\pi_S\inv)^*(\alpha|S^2\setminus\set{p_N, p_S})` は何か。

     .. math::

        \alpha = \dfrac{x_1 \dd x_2 - x_2 \dd x_1}{x_1^2 + x_2^2}.

     前半は直接計算により示せる。後半も直接計算か。

     .. todo:: SymPy で計算してみる。
     .. 結果だけ書くと :math:`\frac{u_1 \dd u_2 - u_2 \dd u_1}{u_1^2 + u_2^2}`

  #. :math:`\fnm{\gamma}{[0, 1]}{\RR^3}{t}(\cos 2\pi t, \sin 2\pi t, 0)` に沿った :math:`\alpha` の線積分。

     解答で省略されている部分を記す：

     .. math::

        \begin{align*}
        \int_\gamma\!\alpha &= \int_\id\!\gamma^*\alpha\\
        &=\int_0^1\!\sum_{i = 1}^2 \alpha_i(\gamma_i(t))\diff{\gamma_i}{t}\,\dd t\\
        &=\int_0^1\! (-\sin 2\pi t)(-2\pi \sin 2\pi t) + \cos 2\pi t (2\pi \cos 2\pi t))\,\dd t\\
        &= \cdots\\
        &= 2\pi.
        \end{align*}

  #. :math:`\alpha_1 = \dfrac{1 - x_3}{2}\alpha` は :math:`S^2\setminus\set{p_S}` 上の
     微分形式である。

     * これも直接計算するといい。

     .. todo:: SymPy で計算してみる。
     .. 結果だけ書くと :math:`\alpha_1 = \frac{u_1 \dd u_2 - u_2 \dd u_1}{1 + u_1^2 + u_2^2}`

     * また、同様にして :math:`\alpha_2 = \dfrac{1 + x_3}{2}\alpha` は
       :math:`S^2\setminus\set{p_N}` 上の微分形式であることもわかる。
       そして :math:`\alpha = \alpha_1 - \alpha_2` に注意するとよい。

.. _tsuboi08.2.7.5:

* 問題 2.7.5: :ref:`前問 <tsuboi08.2.7.4>` の続き

  * :math:`M_1 = S^2 \setminus \set{p_S}`, :math:`M_2 = S^2 \setminus \set{p_N}`
  * :math:`M_{12} = M_1 \cap M_2`

  とする。このとき次の二つのマイヤー・ビエトリス完全系列は同型である：

  .. math::

     \begin{CD}
     \cdots @>>> \H^1(M_1) \oplus \H^1(M_2)
            @>>> \H^1(M_{12})
            @>>> \H^2(S^2)
            @>>> 0,\\
     @.\\
     \cdots @>>> 0 \oplus 0
            @>>> \RR
            @>>> \H^2(S^2)
            @>>> 0.
     \end{CD}

  * :ref:`前問 <tsuboi08.2.7.4>` の :math:`\alpha` は完全形式であり、
    かつ :math:`\H^1(M_{12})` の生成元である。

    * それぞれ :ref:`前問 <tsuboi08.2.7.4>` の小問 2 と 3 による。
      （生成元の辺りはきちんと説明できるか？）

  :math:`\Delta^* [\alpha|M_{12}]` を代表する 2 形式とは何か。

  * :math:`\dd \alpha` を計算していくと、
    :ref:`前問 <tsuboi08.2.7.4>` の小問 1 の値が出てくる。
    このことから次式が成り立つ：

    .. math::

       \Delta^* [\alpha|M_{12}] = \frac{1}{2}[\omega|S^2].

    なぜなのか、よく考えてみること。

2.8 コンパクト多様体のドラーム・コホモロジー
======================================================================
* 臨界点、ヘッセ行列、非退化、モース関数、モースの補題などのおさらい。

  * :ref:`幾何学 I 問題 5.4.8 <tsuboi05.5.4.8>`
  * :ref:`幾何学 I 補題 5.4.3 <tsuboi05.5.4.3>`

  などを参照する。ノートを見返したら難しかったのでまともにやっていなかった。

* モース関数の gradient flow を用いることで次がわかる：

  :math:`M` の開集合 :math:`N_1, \dotsc, N_k` で

  * :math:`\varnothing = N_0 \subset N_1 \subset \dotsb N_k = M`,
  * :math:`N_j = N_{j - 1} \cup B_j \quad(0 < j \le k)`

  なるものがある。
  ここで各 :math:`B_j` は n 次元開球 :math:`B^n` と微分同相であり、

  * :math:`N_{j - 1} \cap B_j = \varnothing`
  * またはある :math:`m_j` が存在して :math:`0 \le m_j \le n - 1` のときに
    :math:`N_{j - 1} \cap B_j` と :math:`B^{n - m_j} \times S^{m_j}` が微分同相である。

.. _tsuboi08.2.8.1:

* 定理 2.8.1: コンパクト多様体のドラーム・コホモロジー群は有限次元ベクトル空間である

  証明は :math:`N_j = N_{j - 1} \cup B_j` についてのマイヤー・ビエトリス完全系列に対する帰納法による。

  .. math::

     \begin{CD}
     @. \cdots
     @>{(j_1^*,\ j_2^*)}>> \H^{p - 1}(N_{j - 1}) \oplus \H^{p - 1}(B_j)
     @>{i_1^* - i_2^*}>> \H^{p - 1}(N_{j - 1} \cap B_j)\\
     @.\\
     @>{\Delta^*}>> \H^p(N_j)
     @>{(j_1^*,\ j_2^*)}>> \H^p(N_{j - 1}) \oplus \H^p(B_j)
     @>{i_1^* - i_2^*}>> \H^p(N_{j - 1} \cap B_j)\\
     @.\\
     @>{\Delta^*}>> \cdots
     \end{CD}

  * まず完全系列であることにより :math:`\H^p(N_j) \cong \im \Delta^* \oplus \H^p(N_j)/\ker (j_1^*,\ j_2^*).`
    ベクトル空間として同型。

    * :math:`\im \Delta^* \cong \H^{p - 1}(N_{j - 1} \cap B_j)/\ker \Delta^*` が成り立つ（同様）。

      * :math:`\H^{p - 1}(N_{j - 1} \cap B_j) \cong H^{p - 1}(S^{m_j})`.
        商空間として有限次元ベクトル空間と同型（本節冒頭を参照）。

    * :math:`\H^p(N_j)/\ker (j_1^*,\ j_2^*) \cong \im (j_1^*,\ j_2^*) \subset H^p(N_{j - 1}) \oplus H^p(B_j).`
      包含写像の像が有限次元ベクトル空間の部分ベクトル空間であると言っている。
      最右辺の直和が有限次元であることは、帰納法でわかる。

    以上の二点により :math:`\H^p(N_j)` は有限次元である。

.. _tsuboi08.2.8.2:

* 注意 2.8.2: モース理論による :math:`N_j` への分解はいろいろと有用である。

.. _tsuboi08.2.8.3:

* 問題 2.8.3: :ref:`幾何学 I 問題 5.4.6 の複素射影空間ファイブレーション <tsuboi05.5.4.6>` 参照

  * 特に参照先の関数 :math:`f, F` および臨界点、指数、臨界値についての知識を本問では用いる。

  :math:`\CC P^n` のドラーム・コホモロジー群はどのようなものか。
  
  * まずは誘導された関数 :math:`F` により次のような開集合が確定する：
  
    * :math:`\varnothing = N_0 \subset N_1 \subset \dotsb N_{n + 1} = \CC P^n`
    * :math:`N_j = N_{j - 1} \cup B_j\quad(0 < j \le n + 1)`
    * :math:`B_j \cong B^n`
    * :math:`N_{j - 1} \cap B_j \cong B^{2n - 2(j - 1) + 1} \times S^{2(j - 1) - 1}\quad(j \ge 2)`

  * 次に :math:`N_j = N_{j - 1} \cup B_j` に関するマイヤー・ビエトリス完全系列を考える。
  
    .. math::
    
       \begin{CD}
       @. \cdots
       @>>> \H^{p - 1}(N_{j - 1}) \oplus \H^{p - 1}(B_j)
       @>>> \H^{p - 1}(S^{2(j - 1)-1})\\
       @.\\
       @>>> \H^p(N_j)
       @>>> \H^p(N_{j - 1}) \oplus \H^p(B_j)
       @>>> \H^p(S^{2(j - 1)-1})\\
       \end{CD}
       
    これにより :math:`\H^p(N_{j - 1})` が :math:`\H^p(N_j)` を定める。
    なぜならば
    
    .. math::
    
       \H^p(N_{j - 1}) \cong
       \begin{cases}
       \RR & \quad\text{if } p = 0, 2, \dotsc, 2(j - 1)\\
       0   & \quad\text{otherwise}
       \end{cases}

    が示されると、

    .. math::
    
       \H^p(N_j) \cong
       \begin{cases}
       \RR & \quad\text{if } p = 0, 2, \dotsc, 2j\\
       0   & \quad\text{otherwise}
       \end{cases}

    が示される。ゆえに：
    
    .. math::
    
       \H^p(\CC P^n) \cong
       \begin{cases}
       \RR & \quad\text{if } p = 0, 2, \dotsc, 2n\\
       0   & \quad\text{otherwise}
       \end{cases}

.. _tsuboi08.2.8.4:

* 問題 2.8.4: コンパクト連結多様体 :math:`M^2`

  この多様体上にモース関数 :math:`f` が存在して、その
  
  * 極小点が 1 個、
  * 極大点が 1 個、
  * 指数 1 の臨界点が k 個
  
  あるとする。このときドラーム・コホモロジー群は次のようになる：
  
  .. math::
    
     \H^p(M^2) \cong
     \begin{cases}
     \RR   & \quad\text{if } p = 0\\
     \RR^k & \quad\text{if } p = 1\\
     \RR   & \quad\text{if } p = 2
     \end{cases}
     \quad\text{or }
     \H^p(M^2) \cong
     \begin{cases}
     \RR        & \quad\text{if } p = 0\\
     \RR^{k - 1}& \quad\text{if } p = 1\\
     0          & \quad\text{if } p = 2
     \end{cases}

  以下証明。例によって開集合列を構成して、
  完全系列を :math:`N_j` と :math:`M^2` それぞれについて見ていく。

  * 開集合を構成する：

    * :math:`\varnothing = N_0 \subset N_1 \subset \dotsb N_{k + 2} = M^2`
    * :math:`N_j = N_{j - 1} \cup B_j\quad(0 < j \le k + 2)`
    * :math:`B_j \cong B^2`
    * :math:`N_{j - 1} \cap B_j \cong B^2 \times S^0\quad(2 \le j \le k + 1)`
    * :math:`N_{k + 1} \cap B_{k + 2} \cong B^1 \times S^1`

  * :math:`N_j = N_{j - 1} \cup B_j` のマイヤー・ビエトリス完全系列を検討する。
    完全系列はいつものように描くと 3 行からなるが、省略。
    
    * いつものように :math:`\H^0(\cdot)` は（局所的）定数関数で代表されるので、
      1 行目の :math:`i_1^* - i_2^*` を行列 :math:`\begin{pmatrix}1 & -1\\1 & -1\end{pmatrix}` で表現できる。

    * :math:`\H^1(B_j) = 0,\ H^1(B^2 S^0) = 0` ゆえ :math:`\H^1(N_j) \cong \H^1(N_{j - 1}) \oplus \RR` ← 2 行目
    * :math:`\H^1(N_1) = 0` ゆえ :math:`\H^1(N_j) \cong \RR^{j - 1}`
    * :math:`\H^2(N_j) = 0\quad(j \le k + 1)` は容易い。

  * :math:`M^2 = N_{k + 1} = N_{k + 1} \cup B_{k + 2}` のマイヤー・ビエトリス完全系列を検討する。

    * 1 行目の :math:`i_1^* - i_2^*` は全射。
    * 2 行目の :math:`i_1^* - i_2^*` は断定できないので場合分け。
    
      * 全射であれば :math:`\H^1(N_{k + 2}) \cong \RR^k/\RR \cong \RR^{k - 1}`, :math:`\H^2(N_{k + 2}) = 0`.
      * ゼロ写像であれば :math:`\H^1(N_{k + 2}) \cong \RR^k`,  :math:`\H^2(N_{k + 2}) = \RR`.

.. _tsuboi08.2.8.5:

* 注意 2.8.5:

  * :ref:`問題 2.8.4 <tsuboi08.2.8.4>` の「または～」の側は種数 k の向き付け不能閉曲面に相当する。
  * :math:`k = 2g` のときの :math:`\H^p(M) \cong \RR \text{ or } \RR^{2g} \text{ or } \RR` に対して、
    種数 g の向き付け不能閉曲面。
  * 向き付け可能のとき :math:`\H^1(M)` が偶数次元である必要があることは、
    ポアンカレ双対原理による。

2.9 直積のドラーム・コホモロジー（展開）
======================================================================
TBW

2.10 チェック・ドラーム複体（展開）
======================================================================
TBW

2.11 第 2 章の問題の解答
======================================================================
TBW

----

:doc:`chapter3` へ。
