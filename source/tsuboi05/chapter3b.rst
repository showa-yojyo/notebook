======================================================================
第 3 章 多様体の定義（後編）
======================================================================
:math:`\require{AMScd}`

.. contents:: ノート目次

3.4 :math:`C^r` 級多様体の間の :math:`C^s` 級写像、微分同相写像
======================================================================
ここでは :math:`s \le r` とする。

:math:`C^s` 級
  写像 :math:`\fn{F}{M_1}m_2` が :math:`C^s` 級 であるとは、
  写像 :math:`\fn{\psi \circ F \circ \varphi\inv}{\varphi(U)}\psi(V)` が :math:`C^s` 級 であることとする。

* 定義 3.4.2: `微分同相写像 <http://mathworld.wolfram.com/Diffeomorphism.html>`__

  写像 :math:`\fn{F_1}{M_1}M_2` が微分同相写像であるとは、
  :math:`F_1 \circ F_2 = \id_{M_2}` かつ
  :math:`F_2 \circ F_1 = \id_{M_1}` であることとする。

* 例 3.4.3

  #. :math:`\RR/\ZZ \cong S^1`
  #. :math:`\RR^2/(2 \pi \ZZ)^2 \cong T^1`

* 問題 3.4.4: :math:`\CC P^1 = (\CC^2 \minuszero) / \CC ^ \times \cong S^2`

  * ヒントに従うと、次の射影 :math:`\fn{p_\pm}{S^2}\RR^2` による座標近傍系を定義できる。

    .. math::

       \begin{align*}
       p_\pm(x, y, z) &= \left(\frac{x}{1 \mp z}, \frac{y}{1 \mp z}\right),\\
       p_\pm\inv(x, y) &= \left(\frac{2x}{x^2 + y^2 + 1}, \frac{2y}{x^2 + y^2 + 1}, \frac{x^2 + y^2 - 1}{x^2 + y^2 + 1}\right),\\
       p_- \circ p_+\inv(x, y) &= \left(\frac{x}{x^2 + y^2}, \frac{y}{x^2 + y^2}\right).
       \end{align*}

  * :math:`\CC P^1` では座標

    * :ref:`問題 3.3.7 <tsuboi05.3.3.7>` の記号で言うと :math:`\fn{\varphi_i}{V_i}\CC,\ z \in \CC^\times, \varphi_1 \circ \varphi_0\inv(z) = \dfrac{1}{z}.`
    * 写像 :math:`\fnm{\bar\iota}{\RR^2}{\RR^2}{(x, y)}(x, -y)` を定義し、
      :math:`S^2` に新たに座標近傍系 :math:`\set{(U_+, p_+), (U_-, \bar\iota \circ p_-)}` を定義する。

      .. math::

         (\bar\iota \circ p_-) \circ p_+\inv(x, y) = \left(\frac{x}{x^2 + y^2}, -\frac{y}{x^2 + y^2}\right)

      となるが、これは :math:`\displaystyle \varphi_0\inv(z) = \frac{1}{z}` で :math:`z = x + y \sqrt{-1}` としたものと一致している。

* 問題 3.4.5: 四元数を意識したクイズ

  * 相当難しい。
    これは線形代数が相当得意でないと解けないと見た。
    例えば :math:`SO_3` の行列の固有値が :math:`\lambda, \bar{\lambda}, 1`
    であることを知らない程度では歯が立たない。

* 例題 3.4.7: 自身への微分同相の例として対蹠点、平行移動、行列式が非ゼロである線型写像を挙げている。

* 用語確認

  * :math:`C^\infty` 級変換群
  * :math:`C^\infty` 級に作用する or 滑らかに作用する
  * `効果的 <http://mathworld.wolfram.com/EffectiveAction.html>`__

    * :math:`K = \set{g \in G \sth gx = x}` のとき。
    * :math:`K` は正規部分群となる。

* <群の構造だけを取り出した群> とは？

.. _tsuboi05.3.4.8:

* 定理 3.4.8: 滑らかな多様体の滑らかな有限変換群に対する商空間は、滑らかな多様体となる。

  * これは :ref:`定理 3.3.1 <tsuboi05.3.3.1>` の上位互換版のような定理だ。実際、証明にそれを利用している。

* 例題 3.4.9: `レンズ空間 <http://mathworld.wolfram.com/LensSpace.html>`__

  :math:`S^3 := \set{(z_1, z_2) \in \CC^2 \sth \abs{z_1} ^2 + \abs{z_2} ^2 = 1}`

  * 有限変換群 :math:`F` の元は互いに素な自然数の組 :math:`p, q` を用いて構成できる。
    LaTeX を書くと字が潰れるので省略。

  * この有限群は位数 :math:`p` の巡回群 :math:`\ZZ/p\ZZ` になり、
    :math:`S^3` へ作用する。
    :ref:`定理 3.4.8 <tsuboi05.3.4.8>` により :math:`S^3/F` は多様体となる。

    * これを :math:`L_{p, q}` と表す。ちなみに :math:`L_{2, 1}` は
      :math:`\RR P^3` と微分同相となる。

3.5 座標変換
======================================================================
* <多様体の定義において最も重要なものは、座標近傍系である> (p. 61)
* 座標変換から多様体を構成する手法がファイバー束、ベクトル束の全空間を
  多様体と考えるときに必要となる。

.. _tsuboi05.3.5.1:

* 例題 3.5.1: 座標近傍の同相写像がまた同相写像となる。

  * :math:`\fn{\gamma_{ij}}{\varphi_j(U_i \cap U_j)}\varphi_i(...)` を
    :math:`\gamma_{ij} = \varphi_i \circ (\varphi_j|U_i \cap U_j)\inv` で定義する。
    このとき :math:`\varphi_k(U_i \cap U_j \cap U_k)` 上は
    :math:`\gamma_{ij} \circ \gamma_{jk} = \gamma_{ik}` となる。

    * 図を描いて確認しよう。定義域が怪しくないことも確認する。

  * 以下紙幅の都合上 :math:`V_i = \varphi_i(U_i),\ V_{ij} = \varphi_j(V_i \cap V_j)` とおく。
  * 写像 :math:`\gamma_{ij}` は :math:`\RR^n` の開集合の間の同相写像となる。

    .. math::
       :nowrap:

       \begin{CD}
       V_{ik} \cap V_{jk} @>{\gamma_{jk}}>> V_{ij} \cap V_{kj} @>{\gamma_{ij}}>> V_{jk} \cap V_{ki}
       \end{CD}

* 一般の開集合 :math:`V_i \subset \RR^n` の直和について。

  * :math:`{ \displaystyle \bigsqcup_{i \in I} V_i = \bigsqcup_{i \in I} V_i \times \set{i} \subset \RR^n \times I}`

  * 左辺は :math:`\RR^n \times I` の直積位相から誘導される位相を入れる。
  * :math:`\RR^n` の位相はいつものユークリッド空間位相を入れる。
  * 添字集合 :math:`I` には離散位相を入れる。
  * c.f. この直和位相（仮称）を一般の位相空間に対する直和位相

.. _tsuboi05.3.5.2:

* 例題 3.5.2: :ref:`例題 3.5.1 <tsuboi05.3.5.1>` の記号の一部を流用し、開集合の直和に同値関係を入れて商空間を定義する。

  #. まず :math:`x_i \sim x_j \iff x_j \in V_{ij} \subset V_j,
     x_i = \gamma_{ij}(x_j)` とする。これは同値関係になることを確認する。

  #. ここで :math:`X = (\bigsqcup V_i / \sim)` がハウスドルフであれば、多様体となるといえる。

     * 射影 :math:`\fn{p}{\bigsqcup V_i}X` を考える。
       :math:`V_i` と :math:`p(V_i)` が同相である。
       代表元を取る写像を :math:`s_i` とすると、次のようにして連続であることがわかる：

       :math:`V_i` の開集合 :math:`W` に対して
       :math:`s_i\inv(W)` が開集合であり、
       :math:`p\inv(s_i\inv(W)) \subset \bigcup V_i` が開集合であることによる。

     * 写像 :math:`s_i` は同相である。なぜなら :math:`p \circ s_i = \id_{p(V_i)}` かつ
       :math:`s_i \circ p = \id_{V_i}` だから。

     * 最後に、商空間の近傍系 :math:`\set{(p(V_i), s_i)}_{i \in I}` の座標変換が滑らかであることを
       示して（最初から商空間はハウスドルフと言っているから）多様体であることが示せる。

  #. n 次元 :math:`C^\infty` 多様体 :math:`M` と上述の商空間 :math:`X` とが微分同相となる。
     :ref:`例題 3.5.1 <tsuboi05.3.5.1>` の記号を流用すると、

     * 写像 :math:`\fnm{\iota}{V_i}{\RR^n}{x_i}\varphi_i\inv(x_i)` を考える。
       このとき、誘導される写像 :math:`\fn{\underline{\iota}}{X}M` は連続となる。

       なぜなら :math:`x_i \in V_{ij}, \iota(\gamma_{ji}(x_i)) = \iota(x_i)` だから。

     * 写像 :math:`\fn{p \circ \varphi_i}{U_i}p(V_i)` は同相の合成で同相。

     * :math:`\underline{\iota} \circ (p \circ \varphi_i) = \id_{U_i}` かつ
       :math:`(p \circ \varphi_i) \circ (\underline{\iota}|p(V_i)) = \id_{p(V_i)}` となるので、
       :math:`\underline{\iota} \inv = (p \circ \varphi_i)` は連続。
       したがって :math:`M` と :math:`X` は同相であり、
       :math:`X` はハウスドルフだ。

     * あとは座標近傍系
       :math:`\set{(U_i), \varphi_i)}`,
       :math:`\set{(p(V_i), s_i)}`
       同士を比較することで :math:`\underline{\iota}` が微分同相であると結論する。

.. _tsuboi05.3.5.3:

* 問題 3.5.3: `ファイバー束 <http://mathworld.wolfram.com/FiberBundle.html>`__

  * :math:`E, B` は位相空間であり、
  * 写像 :math:`\fn{p}{E}B` は連続であり、
  * 次を満たす位相空間 :math:`F` が存在するとする：

    .. math::

       \forall b \in B, \exists U_b \owns b
       \quad\text{s.t.}\quad
       \exists \fn{h}{p\inv(U_b)}U_b \times F,\ \operatorname{pr}_1 \circ h = p|p\inv(U_b).

    ただし :math:`h` は同相写像であり、
    :math:`\operatorname{pr}_1` は直積 :math:`U_b \times F` の第一成分への射影とする。

  このとき :math:`B, F` がハウスドルフならば :math:`E` もそうである。

  .. math::
     :nowrap:

     \begin{CD}
     E @>{p}>> B\\
     @A{\subset}AA @A{\subset}AA\\
     p\inv(U_b) @>{p|p\inv(U_b)}>> U_b\\
     @V{h}VV @A{\operatorname{pr}_1}AA\\
     U_b \times F
     \end{CD}

  * この状況における位相空間 :math:`E` をファイバー束といい、
    位相空間 :math:`F` を :math:`B` 上のファイバーという。

    * また、:math:`E` と :math:`B` をそれぞれ
      `全空間 <http://mathworld.wolfram.com/TotalSpace.html>`__ および
      `底空間 <http://mathworld.wolfram.com/BaseSpace.html>`__ という。

    * 同相写像 :math:`h` をファイバー :math:`F` に対する局所自明化という。

  * 証明は場合分けをする。

    * :math:`x_1 \ne x_2 \in E,\ p(x_1) \ne p(x_2)` のとき：

      * ハウスドルフ性により、次のような開集合 :math:`U_1, U_2` が存在する：
        :math:`p(x_1) \in U_1, p(x_2) \in U_2, U_1 \cap U_2 = \varnothing.`
      * :math:`p` の連続性により、:math:`p\inv(U_1) \owns x_1,\ p\inv(U_2) \owns x_2` は
        :math:`E` の開集合である。

    * :math:`x_1 \ne x_2 \in E,\ p(x_1) = p(x_2) = b` のとき：

      * ファイバー性により次のような同相写像 :math:`\fn{h}{p\inv(U_b)}U_b \times F` が存在する：
        :math:`\operatorname{pr}_1 \circ h = p.`

      * :math:`x_1 \ne x_2` であるので :math:`\operatorname{pr}_2 \circ h(x_1) \ne \operatorname{pr}_2 \circ h(x_2) \in F.`
      * :math:`F` のハウスドルフ性により、次を満たす開集合 :math:`V_1, V_2 \subset F` が存在する：

        .. math::

           \operatorname{pr}_2 \circ h(x_1) \in V_1,\
           \operatorname{pr}_2 \circ h(x_2) \in V_2,\
           V_1 \cap V_2 = \varnothing.

      * :math:`h\inv(U_b \times V_1) \owns x_1, h\inv(U_b \times V_2) \owns x_2` もまた開集合であるので、
        :math:`h\inv(U_b \times V_1) \cap h\inv(U_b \times V_2) = \varnothing.`

  後ほど :ref:`例題 8.6.1 <tsuboi05.8.6.1>` で同じ状況が現れる。

3.6 向き付け（展開）
======================================================================
* 連結多様体からある商空間を構成すると、ファイバー束の性質が利用できて
  `向き付けを持つ多様体 <http://mathworld.wolfram.com/OrientableManifold.html>`__
  を得られる。

* ある多様体が向き付けを持つとは、各座標変換のヤコビアンの行列式がすべて正であるような
  座標近傍系が存在することを意味する。

* 本文中の記号 :math:`p_M` の定義が与えられていないので、ここを理解できないでいる。

  .. math::

     P\inv(p_M(V_i)) =V_{i+} \sqcup V_{i-} \approx V_i \times \set{\pm 1}.

  * :math:`\set{\pm 1}` がハウスドルフであるというのは意表を突かれた感がある。

* 連結多様体 :math:`M` から常に「向き付けを持つ」多様体 :math:`\widehat{M}` を構成できる。

  * :math:`\widehat{M} \cong M \times \set{\pm 1} \iff \forall \gamma_{ij}, \det (D\gamma_{ij}) > 0`

    このとき :math:`M` 自身がすでに向き付け可能。

  * :math:`M` が向き付け不可能で連結であっても :math:`\widehat{M}` は向き付け可能。
  * :math:`\fn{P}{\widehat{M}}M` において :math:`P\inv(y)` の二点を入れ替える写像
    :math:`\fn{F}{\widehat{M}}\widehat{M}` は、向き付けを反対にする微分同相写像だ。

* 例 3.6.2: 実射影空間は多様体次元の偶数奇数によって向き付け可能性が決まる。

  * 偶数次元は向きが付けられない。

* 例 3.6.3

  * `メビウスバンド <http://mathworld.wolfram.com/MoebiusStrip.html>`__
    のパラメーター表示が紹介されているので有用。
  * `実射影平面 <http://mathworld.wolfram.com/RealProjectivePlane.html>`__
    から一点を除くとこれと微分同相となる。

3.7 :math:`C^\infty` 級写像の存在について
======================================================================
* :math:`C^\infty (M, N)` は十分たくさんの元を有し、トポロジーも何か入る。
* :math:`C^\infty (M, \RR)` を :math:`C^\infty (M)` と略記する。

.. _tsuboi05.3.7.1:

* 問題 3.7.1: 微分積分の教科書を参照。

  #. :math:`\mathrm e^x` のマクローリン展開から得られる評価や変数変換（逆数）を駆使する。

  #. 平均値の定理から明らか。

  #. この関数

     .. math::

        \rho(x) =
        \begin{cases}
        0 & \quad\text{if } x \le 0,\\
        \exp\left(-\dfrac{1}{x}\right) & \quad\text{if } 0 < x.
        \end{cases}

     を利用すれば、多様体上の :math:`C^\infty` 級関数を構成できる。

     * 本題は :math:`\rho^{(m)}(0) = 0` が成り立つことを
       帰納法をメインに示すことだが、敢えて導関数を書き下してみたい。

     * SymPy に計算させたら式の展開結果がいきなりゼロになったので導関数を得られなかった。
       代わりに、最初の数階分だけ導関数と極限を計算させるとこうなる：

       .. math::

          \begin{align*}
          \diff{\rho(x)}{x} &= \frac{\mathrm e^{- \frac{1}{x}}}{x^2},& \quad
          &\lim_{x \to +0} \diff{\rho(x)}{x} = 0\\
          \mdiff{\rho(x)}{2}{x} &= \frac{\mathrm e^{- \frac{1}{x}}}{x^4} (- 2x + 1),& \quad
          &\lim_{x \to +0} \mdiff{\rho(x)}{2}{x} = 0\\
          \mdiff{\rho(x)}{3}{x} &= \frac{\mathrm e^{- \frac{1}{x}}}{x^6} (6x^2 - 6x + 1),& \quad
          &\lim_{x \to +0} \mdiff{\rho(x)}{3}{x} = 0\\
          \mdiff{\rho(x)}{4}{x} &= \frac{\mathrm e^{- \frac{1}{x}}}{x^8} (- 24x^3 + 36 x^2 - 12x + 1),& \quad
          &\lim_{x \to +0} \mdiff{\rho(x)}{4}{x} = 0
          \end{align*}

       上の展開からすべての階数について多項式 :math:`P_m(x)` が存在し、
       :math:`x^{2m}\rho^{(m)}(x) = \rho(x)P_m(x)` の形に書けて、
       :math:`x \to +0` のときに :math:`\rho^{(m)}(x) \to 0` であると言えばよいであろうことがわかる。

  #. :math:`\RR^n` の連結な折れ線は、実数全体を定義域とする
     :math:`C^\infty` 級写像の像とできるという事実は大事。

3.8 第 3 章の解答
======================================================================
解答まとめ。
