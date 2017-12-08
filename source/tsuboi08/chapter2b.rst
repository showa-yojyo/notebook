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
----------------------------------------------------------------------
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

TBW

----

:doc:`chapter3` へ。
