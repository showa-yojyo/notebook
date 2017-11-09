======================================================================
幾何学 I 多様体入門 読書ノート 5/8
======================================================================

:doc:`note4` からの続き。

.. contents:: ノート目次

第 5 章 多様体上の関数
======================================================================

5.1 関数の台
----------------------------------------------------------------------
関数の `台 <http://mathworld.wolfram.com/Support.html>`__
  多様体 :math:`M` で定義された関数 :math:`f` に対する次の部分集合のことを関数の台という。

  .. math::
     :nowrap:

     \begin{align*}
     \supp{f} = \closure{\set{x \in M \sth f(x) \ne 0}}
     \end{align*}

  * ノート上は集合の閉包を上線で表現してあるはず。補集合ではない。
  * ちなみに補集合については次のことが成り立つことに注意する：

    .. math::
       :nowrap:

       \begin{align*}
       x \in M \setminus \supp{F} \iff \exists U \owns x: f(U) = \zeroset
       \end{align*}

  * 定義上、多様体という条件を位相空間にまで緩められる。

* 定理 5.1.1: 任意の :math:`x_0 \in M` とその任意の近傍 :math:`V \in M` に対して、
  次のような :math:`M` を定義域とする :math:`C^\infty` 級関数 :math:`\mu` が存在する：

  * :math:`\mu(x) \ge 0`
  * :math:`\mu(x_0) > 0, \supp{\mu} \in V`
  * :math:`\supp{\mu}` がコンパクトである。

  証明方針：問題 3.7.1 の関数 :math:`\rho(x)` を再利用してなんとか関数 :math:`\mu(x)` を構成する。

  #. プロトタイプとして非負関数 :math:`\mu_0(\bm x) = \rho(1 - \norm{\bm x})` を定義する。

     * これは :math:`\norm{\bm x} \le 1 \implies \mu_0 \ge 0` を満たす。

  #. プロトタイプを若干変形した非負関数
     :math:`\displaystyle \mu1 = \mu0\left(\frac{2}{\eps}(\bm x - \varphi(x_0))\right)`
     を定義する。

     * まず :math:`x_0` を含む座標近傍 :math:`(U, \varphi)` をとり、
       これを :math:`V` との共通部分の座標の像 :math:`\varphi(U \cap V) \subset \RR^n` を思い浮かべるといい。
       点 :math:`\varphi(x_0)` について次を満たす :math:`\eps > 0` が何か存在する：

       .. math::

          B_\eps(\varphi(x_0)) \subset \varphi(U \cap V).

     * このボールのさらに半径が半分の（卵ならば黄身の部分）部分集合を座標とする :math:`V` の点について、
       :math:`0 \le \mu_1 \le 1` が成りたつ。
       卵ならば白身の部分ではゼロとなる。

  #. 最後に :math:`\mu_1` を定義域を全体に拡張すれば所望の関数が得られる：

     .. math::

        \mu(x) =
        \begin{cases}
        \mu_1(\varphi(x)) & \quad \text{if } x \in U \cap V\\
        0 & \quad \text{if } x \in M \setminus (U \cap V).
        \end{cases}

* 定理 5.1.2: :math:`M` のコンパクト集合 :math:`K` とそれを含む開集合 :math:`U` があるとき、
  次のような :math:`M` を定義域とする :math:`C^\infty` 級関数 :math:`\nu` が存在する：

  * :math:`\nu(x) \ge 0`
  * :math:`\nu|K(x) > 0`
  * :math:`\supp{\nu}` が :math:`U` のコンパクト集合である。

  証明方針：定理 5.1.1 の関数 :math:`\mu(x)` をいくつか足して関数 :math:`\nu(x)` を構成する。

  #. 前定理を再利用すると以下の条件が成り立つような各関数が存在する：

     .. math::

        \forall x_0 \in K, \exists \fn{\mu_{x_0}}{M}\RR \quad \text{s.t. }
        \forall x \in M, \mu_{x_0}(x) \le 0, \mu_{x_0}(x_0) > 0, \supp \mu_{x_0} \subset U.

  #. :math:`\set{x \in M \sth \mu_{x_0}(x) > 0} = \int(\supp \mu_{x_0})` であることに注意。
     :math:`K` のコンパクト性により、次が成り立つ：

     .. math::

        \exists x_1, \dotsc x_k \quad \text{s.t } K \subset \bigcup_{i = 1}^k \operatorname{int}(\supp \mu_{x_i}).

  #. 最後に和を取れば所望の関数となる：
     :math:`\displaystyle \sum_{i = 1}^k \mu_{x_i}(x).`

* 定理 5.1.3: 定理 5.1.2 と同じ仮定の下で
  次のような :math:`M` を定義域とする :math:`C^\infty` 級関数 :math:`\nu` が存在する：

  * :math:`0 \le \nu(x) \le 1`
  * :math:`\nu|K(x) = 1`
  * :math:`\supp{\nu}` が :math:`U` のコンパクト集合である。

  証明方針：

  #. 前定理の性質を満たす関数 :math:`\fn{\nu_1}{M}\RR` をとる。
  #. :math:`K = \supp \nu_1 \setminus \operatorname{int}(\supp \nu_1)` は
     開集合 :math:`U \setminus K` のコンパクト部分集合である。
  #. 繰り返し前定理を再利用し、関数 :math:`\fn{\nu_2}{M}\RR` がとれる。
     :math:`(\nu_1 + \nu_2)|\supp \nu_1 > 0` より次の関数を考える：

     .. math::

        \nu(x) =
        \begin{cases}
        \displaystyle \frac{\nu_1}{\nu_1 + \nu_2} & \quad \text{if } x \in \operatorname{int}(\supp(\nu_1 + \nu_2))\\
        0 & \quad \text{if } x \in M \setminus \operatorname{int}(\supp(\nu_1 + \nu_2)).
        \end{cases}

     これは所望の条件をすべて満たす。

* 注意 5.1.4 の :math:`\fn{\nu f}{M}\RR,\ \nu|K = f|K` の意味は、
  このあとの方向微分の問題で効いてくる。

ここまでの議論で、多様体上には多くの :math:`C^\infty` 級関数が存在することがわかった。

* 補題 5.1.5: `アダマールの補題 <https://en.wikipedia.org/wiki/Hadamard%27s_lemma>`__

  :math:`\RR^n` 内の原点の開近傍で定義されている :math:`C^\infty` 級関数 :math:`f` に対して、
  次のように書けるような :math:`C^\infty` 関数 :math:`g_k\ (k = 0, \dotsc, n)` が存在する：

  .. math::
     :nowrap:

     \begin{align*}
     f(x_1, \dotsc, x_n) & = f(0, \dotsc, 0) + \sum_{k = i}^{n}x_i g_i(x_1, \dotsc, x_n)\\
     \frac{\partial f}{\partial x_k}(0, \dotsc, 0) & = g_k(0, \dotsc, 0)
     \end{align*}

  初等的な方法で示せる。
  :math:`{ \displaystyle g_k(x_1, \dotsc, x_n) = \int_0^1 \frac{\partial f}{\partial x_k} (tx_1, \dotsc, tx_n)\,\dd{t}}`

* 問題 5.1.6: `方向微分 <http://mathworld.wolfram.com/DirectionalDerivative.html>`__

  多様体 :math:`M` 上で定義されている :math:`C^\infty` 級関数 :math:`f, g` と点 :math:`p \in M` に対して、
  線形な演算 :math:`D` が定義できて :math:`D(f \cdot g) = Df g(p) + f(p) Dg` が成り立つとする（これを方向微分と呼ぶ）。

  #. 点 :math:`p \in M` における方向微分全てからなる空間 :math:`\mathcal{D}_p` は実ベクトル空間である。

     * 解答にあるように、:math:`D_1, D_2 \in \mathcal D_p,\quad a_1, a_2 \in \RR` に対して
       :math:`(a_1 D_1 + a_2 D_2)(fg) = (a_1 D_1 + a_2 D_2)f g(p) + f(p) (a_1 D_1 + a_2 D_2) g` を示せばよい。

  #. 多様体 :math:`M` 上の曲線 :math:`c(t)\ (c(0) = p)` について
     :math:`\displaystyle D_c: f \longmapsto \diff{(f \circ c)}{t}(0)` は点 :math:`p` における方向微分である。

     * これも計算だけで済む。次の二点を確認すればよい：

       .. math::

          &&D_c(a_1 f_1 + a_2 f_2) = a_1 D_c(f_1) + a_2 D_c(f_2)\\
          &&D_c(fg) = D_c(f)g(0) + D_c f(0)(g)

  #. :math:`\mathcal{D}_p` の基底は :math:`\displaystyle
     \Set{
     \left(\frac{\partial}{\partial x_1} \right)_p,
     \dotsc,
     \left(\frac{\partial}{\partial x_n} \right)_p}` である。

     ここで :math:`\displaystyle \left(\frac{\partial}{\partial x_k} \right)_p` とは曲線
     :math:`\displaystyle t \longmapsto \varphi\inv(0, \dotsc, \overset{(k)}t, \dotsc, 0)` における方向微分とする (cf. p. 76)。

     * :math:`Df` が点 :math:`p` の近傍で定義された :math:`C^\infty` 級関数に対して定義されることを示す。
       この際に定理 5.1.3 の関数 :math:`\nu` および注意 5.1.4 の事実を用いる。

     * :math:`D \in \mathcal D_p` が上述の一次結合で表されることを示す。
       :math:`f \in C^\infty(M)` に対して :math:`\displaystyle \left(\frac{\partial}{\partial x_i} \right)_p f = \frac{\partial(f \circ \varphi\inv)}{\partial x_i}(0, \dotsc, 0).`

       :math:`(\nu f) \circ \varphi\inv` を :math:`\RR^n` 上の関数とみなして、
       アダマールの補題を適用して次のような :math:`g_i` を定義する（これ合っているか？）：

       .. math::

          \begin{align*}
          &(\nu f) \circ \varphi\inv = f(p) + \sum_{i = 1}^n x_i g_i(x_1, \dotsc, x_n),\\
          &g_i(0, \dotsc, 0) = \frac{\partial(f \circ \varphi\inv)}{\partial x_i}(0, \dotsc, 0).
          \end{align*}

     * 点 :math:`p` の近傍では :math:`\displaystyle f = f(p) + \sum_{i = 1}^n (x_i \circ \varphi\inv)(g_i \circ \varphi\inv)`
       となっている。よって次のようにすれば線形結合になっていることが示される：

       .. math::

          \begin{align*}
          Df &= D(f(p)) + \sum_{i = 1}^n (D(x_i)g_i(0) + 0 \cdot D(g_i))\\
             &= \sum_{i = 1}^n D(x_i)\frac{\partial(f \circ \varphi\inv)}{\partial x_i}(0, \dotsc, 0)\\
             &= \sum_{i = 1}^n D(x_i) \left(\frac{\partial}{\partial x_i} \right)_p f.
          \end{align*}

      * 最後に各基底の一次独立性を示しておく。

        .. math::

           \left(\frac{\partial}{\partial x_i} \right)_p x_j
           = \left(\frac{\partial x_j}{\partial x_i} \right)(0, \dotsc, 0)
           = \delta_{ij}.

   ヒントをどこで利用したのかを分かりやすくしておきたい。

   * :math:`D(const) = 0.`
   * :math:`Df` は関数 :math:`f` の点 :math:`p` の近傍の値（だけ）で決まる。
   * 点 :math:`p` の近傍で定義されている任意の関数 :math:`f` に対して、
     :math:`V \subset U` 上 :math:`f` に一致する :math:`C^\infty` 級関数がある。

5.2 コンパクト多様体のユークリッド空間への埋め込み
----------------------------------------------------------------------
* 例題 5.2.1: コンパクトハウスドルフ空間は `正規空間 <http://mathworld.wolfram.com/NormalSpace.html>`__ である。

  * 位相空間論の教科書を参照する。
  * まず `正則空間 <http://mathworld.wolfram.com/RegularSpace.html>`__ であること、すなわち一点 vs 閉集合について証明する。

    * 実はパッと読んだ時点で「？」だったが、有限開被覆 :math:`\set{U_{y_i}}` の各開集合の点 :math:`y_i` に対応して
      被覆 :math:`V_{y_i} \owns x_0` が決まるということが気付かなかっただけだった。

  * それから普通の閉集合 vs 閉集合について証明する。

* 例題 5.2.2: コンパクトハウスドルフ空間 :math:`X` の開被覆 :math:`\set{U_i}` に対し、
  次のような開被覆 :math:`\set{V_i}` が存在する：
  :math:`\closure{V_i} \subset U_i`

  * 位相空間論の教科書を参照する。証明方針は次のような感じだ：
  * コンパクト性により、有限開被覆 :math:`\set{U_1, \dotsc, U_k}` が :math:`\set{U_i}` から選べる。

  * 帰納法の部分のメモ

    * :math:`V_1, \dotsc, V_{j - 1}` が :math:`\closure{V_p} \subset U_p\ (p = 1, \dotsc, j - 1)`,
      :math:`{\displaystyle X = \bigcup_{i = 1}^{j - 1}V_i \cup \bigcup_{i = j}^k U_i}` が成り立っていると仮定する。

    * 閉集合 :math:`{ \displaystyle K_j = X \setminus \left(\bigcup_{i = 1}^{j - 1} V_i \cup \bigcup_{i = j + 1}^k U_i\right) \subset U_j}`
      を考える（部分となることは式を展開すると納得できる）。

    * :math:`K_j \cap (X \setminus U_j) = \varnothing` だから（集合の部分からその集合を差し引くのだから）、
      例題 5.2.1 で見た正規空間の性質によって次のような開集合 :math:`V_j, W_j` が（帰納法により）存在する：
      :math:`K_j \subset V_j, X \setminus U_j \subset W_j, V_j \cap W_j = \varnothing`

  * このとき :math:`\closure{V_i} \subset U_i` かつ
    :math:`{\displaystyle X = \bigcup_{i = 1}^j V_i \cup \bigcup_{i = j + 1}^k U_i}`
    となっている。

* 定理 5.2.3: コンパクト多様体はユークリッド空間に埋め込める。

  * ポイント：例題 5.2.2 の開被覆の構成手順を二重に行う。
    つまり :math:`\closure{V_i} \subset U_i,\ \closure{W_i} \subset V_i` のようなものを取る。
    これらの有限開被覆の個数を :math:`k` としておく。

  * 閉集合 :math:`\closure{V_i}` に関して定理 5.1.3 の条件を満たす :math:`C^\infty` 級関数 :math:`\nu_i` を取る。
  * 閉集合 :math:`\closure{W_i}` に関して定理 5.1.2 の条件を満たす :math:`C^\infty` 級関数 :math:`\mu_i` を取る。
  * 座標近傍 :math:`(U_i, \varphi_i)` の局所座標 :math:`\varphi_i = (x_1^{(i)}, \dotsc, x_n^{(i)})` に対して
    関数 :math:`\nu_i \varphi_i := (\nu_i x_1^{(i)}, \dotsc, \nu_i x_n^{(i)})` を取ると、これは :math:`C^\infty` 級となる。

  * ここで :math:`\Phi = (\mu_1, \nu_1 \varphi_1, \dotsc, \mu_k, \nu_k \varphi_k)` とおくと、
    これが多様体から :math:`\RR^{k(n + 1)}` への埋め込みとなる：

    * 定理 4.4.2 の上にある説明により :math:`\fn{\Phi_*}{T_xM}\RR^{k(n + 1)}` のランクが
      :math:`n` で :math:`\Phi` が単射であるから。

      * ランクが :math:`n` であることは :math:`(\nu_i \varphi_i | V_i) \circ \varphi_i\inv = \id_{\varphi_i(V_i)}` から示せる。
      * 単射であることは :math:`\Phi(x) = \Phi(y) \implies x = y` を示すのに
        :math:`\mu_i` の成分と :math:`\nu_i` の成分の単射性を別々に示す。
        関数の非ゼロ性と局所座標の同相性が使えるので容易に示せる。

ユークリッド空間が利用できるようになったので、内積の話題が出て来るようになる。

法束
  :math:`\nu M = \set{(x, v) \in \RR^N \times \RR^N \sth v \perp T_xM}`

  これはユークリッド空間内の :math:`N` 次元多様体になっている。

法空間
  :math:`\nu_x M = \set{v \in \RR^N \sth v \perp T_xM }`

* TODO: (pp. 96-97) の可換図式を何とかここに描きたい。
* 接束 :math:`TM` が :math:`(V_i \times \RR^n, \gamma_{ij} \times D\gamma_{ij})` から構成されたのと似て、
  法束 :math:`\nu M` は :math:`(V_i \times \RR^{N - n}, \gamma_{ij} \times A_{ij})` から構成される。
  ここで :math:`A_{ij_{(x_j)}} \in GL_{N - n}(\RR)` である。

* 注意 5.2.4

  * ユークリッド空間 :math:`\RR^{n + 1}` 内の n 次元コンパクト多様体の法束は
    1 次元ベクトル空間をファイバーとするベクトル束である。

  * ユークリッド空間 :math:`\RR^{n + 1} \quad(n \le 2)` 内の
    :math:`n` 次元コンパクト多様体は向き付け可能とある。理屈が飲み込めない。

* 問題 5.2.5: ユークリッド空間 :math:`\RR^N` に埋め込まれる p 次元コンパクト多様体 :math:`M` の性質

  #. 法束は :math:`N` 次元多様体になっている。

     :math:`X = \nu M = \set{(\bm x, \bm y) \in \RR^{2N} \sth \bm x \in M, \bm y \perp T_{\bm x}M}.`

     * 問題 4.5.3 でやったように :math:`M` のグラフ表示を考えることから始める。
       同じような記号を使う。

       :math:`(\bm x, \bm y) \in X \iff \bm y = (\bm y_1, \bm y_2)` とは、
       次が成り立つことと同値である：

       .. math::

          \begin{align*}
          &\bm x_2 = g(\bm x_1),\\
          &\begin{pmatrix}\bm y_1 & \bm y_2\end{pmatrix}
           \begin{pmatrix}I_p \\ Dg\end{pmatrix}
          = \bm 0.
          \end{align*}

       :math:`X` は :math:`(\bm x_1, \bm x_2) \longmapsto (g(\bm x_1), -bm y_2 Dg_{(\bm x_1)})` の
       グラフとして表されている。よってこの空間は多様体である。

  #. 写像 :math:`e: (\bm x, \bm y) \longmapsto \bm x + \bm y` は
     :math:`X \cap (\RR^N \times \zeroset)` 近傍で微分同相である。

     * 先ほどのグラフの写像を :math:`F` とすると
       :math:`(e \circ F)(\bm x_1, \bm y_2) = (\bm x_1 - \bm y_2 Dg_{\bm x_1}, g(\bm x_1) + \bm y_2).`

     * :math:`\bm y_2 = 0` すなわち :math:`(\bm x_1^0, \bm 0)` における微分は次のようになる：

       .. math::

          \begin{pmatrix}
          I_p              & -{}^t\!Dg_{(\bm x_0^1)}\\
          Dg_{(\bm x_0^0)} & I_{N - p}
          \end{pmatrix}.

       この行列の右上のブロックと左下のブロック（第 :math:`i` 列と第 :math:`p + j` 列）が直交するので、
       これはランクが :math:`N` である。

     * 写像 :math:`e` を :math:`\bm y_2 = \bm 0` に制限した写像は
       例題 4.3.1 の仮定をみたすので、主張の近傍で微分同相となる。

5.3 :math:`C^\infty` 級写像と多様体の埋め込み、はめ込み
----------------------------------------------------------------------
<どのような次元のユークリッド空間に埋め込まれるかというのは多様体の複雑さをはかる量になる> (p. 98)

* 例 5.3.1: 色々なコンパクト多様体

  * 円周、球面は当然ユークリッド空間 :math:`\RR^2` と :math:`\RR^3` にそれぞれ埋め込まれる。
  * :math:`\RR P^2` は :math:`\RR^3` に埋め込めない。メビウス帯を部分空間として含むことによる。

<埋め込みやはめ込みの空間は、数学的に非常に興味深い> (p. 99)

* 例 5.3.2: 円周 :math:`S^1` の埋め込み

  * 円周の :math:`\RR^2` への埋め込みは円板 :math:`D^2` を囲む。
    :math:`D^2` の :math:`\RR^2` への埋め込みの境界への制限（ジョルダンの閉曲線定理）。

  * 円周の :math:`\RR^3` への埋め込みは制限とはならない。分類＝結び目理論。
  * 円周の :math:`\RR^n\ (n \le 4)` への埋め込みは
    円板 :math:`D^2` の :math:`\RR^n` への埋め込みの境界への制限。

* 多様体の形を理解するには、超球面 :math:`S^n` などのよくわかる多様体から構成的に理解するのがよい。

  * コンパクト連結一次元多様体は :math:`S^1` と微分同相。
  * コンパクトではない可分な連結一次元多様体は :math:`\RR` と微分同相。
  * コンパクト連結二次元多様体

    * 向き付け可能： :math:`S^2, T^2, \Sigma_2, \Sigma_3, \Sigma_4, \dots`; 有向閉曲面は可算個。

      * 有向閉曲面 :math:`\Sigma_k \subset \RR^3` の定義は p. 100 を参照。

    * 向き付け不可能： :math:`\RR P^2, K, N_3, N_4, \dots`; 非有向閉曲面は可算個。

      * :math:`\forall x \in \Sigma_k, -x \in \Sigma_k` なので同値関係を定義して :math:`\Sigma_k/\sim` を定義できる。
        このとき、これは多様体となり非有向閉曲面 :math:`N_{k + 1}` となる。

* 例 5.3.3: メビウス帯の像、
  `ホイットニーの傘 <http://mathworld.wolfram.com/WhitneyUmbrella.html>`__
  `クロスキャップ <http://mathworld.wolfram.com/Cross-Cap.html>`__

* <写像 :math:`\fn{F}{M}N` が与えられ、:math:`N` の形と :math:`F\inv(y)\ (y \in N)` の形が理解できれば、
  :math:`M` の形がわかることが期待できる> (p. 101)

  * 写像 :math:`F` については :math:`\fn{F_*}{T_xM}T_{F(x)}N` のランクが :math:`\dim N` であるようなものがよいと思われる。
    こういう :math:`x` とそれに対応する :math:`y` はそれぞれ正則点、正則値であるという。

    * 言葉に引っ張られないように。正則「値」と言っても多様体上の点を指している。

  * 正則値の逆像 :math:`F\inv(y)` は :math:`\dim M - \dim N` 次元部分多様体である。
  * 臨界点とは、正則点でない点である。
  * 臨界値とは、臨界点全ての集合の像である。
  * :math:`\dim M < \dim N` のときは、:math:`F(M),\ N \setminus F(M)` がそれぞれ臨界値、正則値である。
    正則値の逆像は空集合になる。

* 例 5.3.4: 例題 2.4.1 の関数の検討
* 例 5.3.5

  * `ボーイ・アペリ曲面 <http://mathworld.wolfram.com/BoySurface.html>`__ の平面への射影（写像）など。
  * 問題 2.5.1 では図のソリッドな曲線が臨界値となっている。
  * これらによると、アウトラインが大体臨界値であるということが推測される。

* 例題 5.3.6: `1 の分割 <http://mathworld.wolfram.com/PartitionofUnity.html>`__

  * :math:`M, \set{(U_i, \varphi_i)}` をそれぞれコンパクト多様体とその座標近傍系とする。
  * :math:`\exists \fn{\lambda_i}{M}\RR\quad\text{s.t. }\lambda_i \in C^\infty(M),\ 0 \le \lambda_i(x) \le 1,\ \supp{\lambda_i} \subset U_i.`
    有限個の添字を除いて :math:`\lambda_i = 0,\ \sum \lambda_i = 1.`

  * 証明では例題 5.2.2 およびその元となる各種命題を利用している。
    :math:`U_i` 上にある性質の関数 :math:`\mu_{i_j}` を構成して、次のような開被覆および関数を構成する：

    .. math::
       :nowrap:

       \begin{gather*}
       \lambda_{i_{i_j}} = \frac{\mu_{i_j}}{\displaystyle \sum_{l = 1}^k \mu_{i_l}},\
       \set{U_{i_j}},\
       \closure{V_{i_j}} \subset U_{i_j},\
       \mu_{i_j}|\closure{V_{i_j}} > 0,\
       \supp \mu_{i_j} \subset U_{i_j}.
       \end{gather*}

5.4 サードの定理とモース関数
----------------------------------------------------------------------
式で定義されている図形は、多くの場合多様体である。

* 定理 5.4.1: `サードの定理 <http://mathworld.wolfram.com/SardsTheorem.html>`__

  * :math:`C\infty` 級写像 :math:`\fn{F}{M}N` の臨界値は測度が 0 である。

* 定義 5.4.2: 非退化、`モース関数 <http://mathworld.wolfram.com/MorseFunction.html>`__

  * 臨界点 :math:`x` が非退化であるとは、点 :math:`x` における関数のヘッセ行列が正則であることをいう。
  * 関数 :math:`f \in C^\infty(M)` がモース関数であるとは、
    多様体上のどの臨界点においても非退化であることをいう。

* ヘッセ行列の正則性は座標近傍の取り方によらない：

  臨界点 :math:`x` と座標近傍 :math:`(U, \varphi = (x_1, \dotsc, x_n))` について
  行列 :math:`\left(\dfrac{\partial^2 (f \circ \varphi\inv)}{\partial x_i \partial x_j}(\varphi(x))\right)_{i, j}` が
  ヘッセ行列だ。

  * この座標近傍で関数が二次関数 :math:`\displaystyle \sum_{i, j}^n \left(\dfrac{\partial^2 (f \circ \varphi\inv)}{\partial x_i \partial x_j}\right)(\varphi(x))x_i x_j` で
    近似できることを意味する。

  * ヘッセ行列が正則であるかどうかは座標近傍によらない。なぜなら、
    別の座標近傍 :math:`(U, \psi = (y_1, \dots, y_n))` について
    :math:`P = \left(\dfrac{\partial y_k}{\partial x_i}\right)_{i, k}` とおくと
    :math:`H(f \circ \varphi\inv) = {}^t\!PH(f \circ \psi\inv)P` が成り立つからだ。

* 二次曲面の形は行列 :math:`\displaystyle \sum_{i, j}^n \frac{\partial^2(f \circ \varphi\inv}{\partial x_i \partial x_j}(\varphi(x))`
  の重複を込めた正と負それぞれの固有値の個数で分類できる。

* 二次曲面を変換して座標系を正則行列に取り替えることで、次の標準形に書き換えられる：

  .. math::

     -\sum_{i = 1}^k x_i^2 + \sum_{i = k + 1}^n x_i^2.

* 二次曲面の行列の符号数も取り方によらない。
* ちなみに負の固有値の個数をモース臨界点の指数という。

* 補題 5.4.3: モースの補題

  * 関数 :math:`f` の非退化な臨界点 :math:`x^0 \in M` の座標近傍 :math:`(U_i, \varphi_i = (x_1, \dotsc, x_n))` で
    次のようなものがある：

    .. math::
       :nowrap:

       \begin{align*}
       (f \circ \varphi_i\inv)(x_1, \dotsc, x_n) = f(x^0) - \sum_{i = 1}^k x_i^2 + \sum_{i = k + 1}^n x_i^2.
       \end{align*}

  * 証明方針を挙げていく：

    * 点 :math:`x^0` を原点に移動して考えたい。つまり :math:`f - f(x^0)` を最初から考える。
      さらに必要ならば線形変換しておいて :math:`\dfrac{\partial^2 f}{\partial x_i \partial x_j}(0, \dotsc, 0)` が対角化されているとしてよい。
      このとき、この行列の (1, 1) 成分がゼロでないことが大事だ。

    * 関数 :math:`f` をアダマールの補題（先述）による書き方にしておく：

      .. math::

         f = \sum_{i = 1}^n x_i g_i,\quad
         g_i = x_1 h_{i1} + \dotsb + x_n h_{in}.

      このとき :math:`g_i(0, \dotsc, 0) = 0` および :math:`h_{11} = \dfrac{\partial^2 f}{\partial x_1^2} \ne 0` に注意。

    * :math:`f = \sum h_{ij} x_i x_j` だが、これを :math:`h_{ij} = \dfrac{h_{ij} + h_{ji}}{2}` と置き換えて
      :math:`h_{ij} = h_{ji}` としてもよい。

    * 平方完成と座標変換を順次適用する。最初はこうする：

      .. math::

         f = h_{11}\left(x_1 + \frac{h_{12}}{2 h_{11}}x_2 + \dotsb + \frac{h_{1n}}{2 h_{11}}x_n\right)^2
           + \sum_{i, j = 2}^n h'_{ij} x_i x_j.

      この第一項の平方根を :math:`y_1` とすると、座標変換 :math:`(x_1, \dotsc, x_n) \longmapsto (y_1, x_2, \dotsc, x_n)` は
      局所的に微分同相となる。これにより次のように書ける：

      .. math::

         f = \operatorname{sign}(h_{11})y_1^2 + \sum_{i, j = 2}^n h'_{ij}(x_2, \dotsc, x_n) x_i x_j.

      ここで :math:`h'` を関数化させた。
      この平方完成と座標変換をシグマの項に対して順次適用すると、主張の等式が得られる。

* 例 5.4.4: 例題 2.4.1 の吟味

  * この関数は実はモース関数なのであった。
  * 球面上には指数 0, 1, 2 の臨界点がそれぞれ 2 個ずつある。

* 問題 5.4.5: :math:`f(x, y) = (2 + \cos y)(a\cos x + b \sin x) + c \sin y,\ ((a, b, c) \ne (0, 0, 0))`

  この関数は :math:`\fn{F}{\RR^2/(2\pi\ZZ)^2}\RR` を誘導する。
  臨界点の個数が有限となる条件と退化する条件とを求める。

  * :math:`F` が well-defined であることを確かめる。
    いつも通り :math:`[x_1, y_1] = [x_2, y_2] \iff f(x_1, y_1) = f(x_2, y_2)` を示せばよい。
    これは三角関数の性質より明らか。

  * :math:`F` が :math:`C^\infty` 級であることも確認する。

  * まずはヤコビ行列を計算する。

    * :math:`Df = \begin{pmatrix}0 & 0\end{pmatrix}` となるには
      :math:`-a\sin x + b\cos x = 0` かつ :math:`-\sin y(a\cos x + b\sin x) + c\cos y = 0` が条件。

      * :math:`a\cos x + b\sin x = 0` のときは :math:`a = 0,\ b = 0` であり、
        :math:`c \ne 0` となって :math:`\cos y = 0.`

        :math:`[x, y], \quad y \equiv 0 \pmod \pi` なる無限個の点が :math:`F` の臨界点となる。

      * :math:`a\cos x + b\sin x \ne 0` のときは以下の 4 個の組み合わせを決める
        4 個の :math:`x, y` が臨界点を与える：

        .. math::

           \begin{align*}
           (\cos x, \sin x) =& \left(\pm\dfrac{a}{\sqrt{a^2 + b^2}}, \pm\dfrac{b}{\sqrt{a^2 + b^2}}\right),\\
           \tan y =& \pm\dfrac{c}{\sqrt{a^2 + b^2}}.
           \end{align*}

  * それからヘッセ行列を計算する。

    .. todo:: ヘッセ行列のコードを挿れる。

  * あとは三角関数の性質を利用する。
  * 臨界点を調べる。対角行列が得られるので、符号数を確かめることになる。
    最終的に :math:`\cos y` の符号と一致する？

* 問題 5.4.6: ファイブレーション

  複素射影空間 :math:`\CC P^n = (\CC^{n + 1} \minuszero)/\CC^\times` の
  単位球面 :math:`S^{2n + 1} = \set{(z_1, \dotsc, z_{n + 1}) \in \CC^{n + 1} \sth \abs{z} = 1}` と
  :math:`U(1) = \set{\mathrm e^{\sqrt{-1}\theta} \sth \theta \in \RR}` について

  * :math:`g \in U(1)` に対して :math:`(g, z) \longmapsto (gz_1, \dotsc, gz_n)` とすると、これは群の作用となる。

    #. :math:`C^\infty` 級写像であることは成り立つ。
    #. :math:`1 \cdot \bm z = \bm z` であることは、:math:`U(1)` の単位元が 1 であるので成り立つ。
    #. :math:`(g_1 g_2)\bm z = g_1(g_2 \bm z)` であることは次のとおり：

       .. math::

          \begin{align*}
              (\mathrm e^{\sqrt{-1}\theta_1}, (\mathrm e^{\sqrt{-1}(\theta_2)}, \bm z))
          & = \mathrm e^{\sqrt{-1}\theta_1}(\mathrm e^{\sqrt{-1}\theta_2}\bm z)\\
          & = (\dotsc, \mathrm e^{\sqrt{-1}\theta_1} \mathrm e^{\sqrt{-1}\theta_2} z_k, \dots)\\
          & = (\dotsc, \mathrm e^{\sqrt{-1}(\theta_1 + \theta_2)}z_k, \dots)\\
          & = (\mathrm e^{\sqrt{-1}(\theta_1 + \theta_2)}, \bm z)
          \end{align*}

  * :math:`S^{2n + 1} \overset{i}{\longto} \CC^{n + 1}\minuszero \overset{p}{\longto} \CC P^n` のランクはいくらか。
    ただし :math:`i,\ p` は包含写像と射影である。

    * 解答は :math:`2n` なのだが、接写像 :math:`(p \circ i)_*` が全射であることを示すことによる。
    * :math:`\CC P^n` の座標近傍系は問題 3.3.7 と同じものを用いる。
      添字の記号が包含写像とカブるのは意図的なもの。
    * :math:`\bm z^0 \in S^{2n + 1}` に対して :math:`(p \circ i)(\bm z^0) \in V_i.`

    ここからがよくわからない。

    * 点 :math:`\varphi_i((p \circ i)(\bm z^0))` を通る :math:`C^\infty` 級曲線を考える。
    * TBW

  * 次に示す関数は :math:`\fn{F}{\CC P^n}\RR` を誘導する：

    .. math::
       :nowrap:

       \begin{align*}
       f(z) = \dfrac{\displaystyle \sum_{k = 1}^{n + 1} k \abs{z_k} ^2}{\displaystyle \sum_{k = 1}^{n + 1} \abs{z_k} ^2}.
       \end{align*}

    * :math:`F` が well-defined であることを確認する：
      :math:`\bm z \in \CC^{n + 1}`, :math:`\bm z' = \lambda \bm z,\quad \lambda \in \CC^\times` に対して
      :math:`F(\bm z) = F(\bm z')` が成り立つ。

    * :math:`C^\infty` 級であることを確認する：
      これは :math:`F \circ \varphi_i\inv` を調べる必要がある。
      :math:`(x_1, \dotsc, x_n) \in \varphi_i(V_i)` に対して
      :math:`\varphi_i\inv(x_1, \dotsc, x_n) = (z_1, \dotsc, z_{i - 1}, 1, z_{i + 1}, \dotsc, z_n).`

      * :math:`F \circ \varphi_i\inv` の分子を計算すると
        :math:`\displaystyle \sum_{k = 1}^{i - 1}k\abs{x_k}^2 + i \cdot 1^2 + \sum_{k = i + 1}^{n + 1}k\abs{x_k}^2 = i + \sum_{k = 1}^{i - 1}k\abs{x_k}^2 + \sum_{k = i}^n(k + 1)\abs{x_k}^2.`

      * :math:`F \circ \varphi_i\inv` の分母を計算すると
        :math:`\displaystyle \sum_{k = 1}^{i - 1}k\abs{x_k}^2 + 1^2 + \sum_{k = i + 1}^{n + 1}k\abs{x_k}^2 = 1 + \sum_{k = 1}^{i - 1}k\abs{x_k}^2 + \sum_{k = i + 1}^n(k + 1)\abs{x_k}^2.`

      分母がゼロになることはない。

  * :math:`F` の臨界点は :math:`\fn{F_*}{T_x \CC P^n}\RR` がゼロとなる
    :math:`x \in \CC P^n` である。

    * ヒントには合成写像 :math:`T_zS^{2n + 1} \longto T_x\CC P^n \longto \RR` を考えろとある。

    #. :math:`S^{2n + 1}` 上の関数 :math:`f` と座標近傍 :math:`(U_i^\pm, \varphi_i^\pm), (V_i^\pm, \psi_i^\pm)` を考える。
       
       .. math::

          \begin{align*}
          U_i^\pm = \set{\bm z \in S^{2n + 1} \sth \Re z_i \gtrless 0}, & \quad \varphi_i^\pm(\bm z) = (z_1, \dotsc, z_{i - 1}, \Im z_i, z_{i + 1}, \dotsc, z_{n + 1}),\\
          V_i^\pm = \set{\bm z \in S^{2n + 1} \sth \Im z_i \gtrless 0}, & \quad \psi_i^\pm(\bm z) = (z_1, \dotsc, z_{i - 1}, \Re z_i, z_{i + 1}, \dotsc, z_{n + 1}).
          \end{align*}

    #. :math:`f \circ (\varphi_i^\pm)\inv = i + \sum(k - i)\abs{z_k}^2` および
       :math:`f \circ (\psi_i^\pm)\inv = i + \sum(k - i)\abs{z_k}^2` を考える。

       .. math::

          \begin{align*}
          &D f\circ (\varphi_i^\pm)\inv = 0 \iff z_k = 0 (k \ne i)\\
          &D f\circ (\psi_i^\pm)\inv = 0 \iff z_k = 0 (k \ne i)
          \end{align*}

    #. 以上より :math:`\bm z \in S^{2n + 1}` が正則点であることは、
       :math:`\bm z` が :math:`i \ne j \implies z_i \ne z_j` であることを同値である。

    #. :math:`F \circ (p \circ i) = f` が成り立つので :math:`F_* \circ (p \circ i)_* = f_*` である。
       ゆえに :math:`f` の正則点 :math:`bm z` は :math:`F \circ (p \circ i)(\bm z)` が :math:`F` の正則点となる。

    #. 臨界点は各 :math:`(p \circ i)(\bm e_i)\quad(n = 1, \dotsc, n + 1)` である。

  * 臨界点におけるヘッセ行列を求める。

    * ポイントは :math:`V_i` 上 :math:`F \circ \varphi_i\inv` を無限級数の形に展開して、
      :math:`\abs{z_k}^4` 以降の項を捨てる。

      .. math::

         F \circ \varphi_i\inv(\bm w) = i + \sum_{k = 1}^{i - 1}(k - i)\abs{w_k}^2 + \sum_{k = i}^n(k + 1 - i)\abs{w_k}^2 + \dotsb.

    * 上の式からヘッセ行列を求めると次のようになるので、モース臨界点の指数は :math:`2(i - 1)` である。

      .. math::

         \diag(2(1 - i), 2(1 - i), \dotsc, -2, -2, 2, 2, \dotsc, 2(n + 1 - i), 2(n + 1 - i)).

* ほとんどすべての射影がモース関数である (p. 107)。

* 問題 5.4.8: 問題 5.2.5 の続き。

  同じ記号を引き続き用いる上で、次の仮定を追加する：

  * :math:`\fn{i}{M}\RR^N` を包含写像、
  * :math:`\fn{\operatorname{pr}_2}{\RR^N}\RR^N` を第二成分への射影、
  * :math:`\fn{L}{\RR^N}\RR` を線形写像 :math:`\displaystyle L(\bm x) = \sum_{i = 1}^N a_i x_i` とする。

  このとき :math:`\bm a \in \RR^N` が :math:`\operatorname{pr}_2|X` の正則値であることと、
  :math:`L \circ i` がモース関数であることは同値である。

  #. 問題 5.2.5 のグラフ表示の記号群を再利用する。

     .. math::

        \begin{align*}
        \operatorname{pr}_2|X &= (\bm y_2 Dg_{(\bm x_1)}, \bm y_2)\\
        &= \left(\sum_{k = p + 1}^N y_k \frac{\partial g_k}{\partial x_1}, \dotsc,
           \sum_{k = p + 1}^N y_k \frac{\partial g_k}{\partial x_p},
           y_{p + 1}, \dotsc, y_N\right).
        \end{align*}

  #. ヤコビ行列を計算すると :math:`\sum y_k g_k` の二階微分からなる成分が現れるので、
     このブロックの正則性が条件となる。

  #. 一方、:math:`(L \circ i)(\bm x_1, g(\bm x_1)) = \sum a_k x_k + \sum a_k g_k` が
     :math:`\bm x^0` の近傍でモース関数であることは、
     :math:`\bm x^0` が :math:`\displaystyle a_l + \sum_{k = p + 1}^N a_k \frac{\partial g_k}{\partial x_l} = 0\quad(l = 1, \dotsc, p)`
     を満たすときにヘッセ行列 :math:`\displaystyle \left(\sum_{p + 1}^N a_k \frac{\partial^2 g_k}{\partial x_l \partial x_m}\right)_{l, m}` が
     正則であることと同値である。
     
     これは :math:`\bm a = (a_j) \in \RR^N` が :math:`F` のグラフ上で
     :math:`\operatorname{pr}_2|X` の正則値である条件と同じだ。

  #. あとはコンパクト性による。
     有限個の近傍それぞれで上の議論を繰り返すと
     :math:`(L \circ i)` がモース関数であることと、
     :math:`\bm a` が :math:`\operatorname{pr}_2|X` の正則値であることが同値となる。

5.5 サードの定理の証明の概略（展開）
----------------------------------------------------------------------
証明のアウトラインが記されている。どうも測度論、例えばフビニの定理の知識を要するようだ。

5.6 モース関数の存在の証明の概略（展開）
----------------------------------------------------------------------
定理 5.2.3 と問題 5.4.8 を合わせるとモース関数の存在を示すことができる (p. 111)。

5.7 関数の空間、写像の空間（展開）
----------------------------------------------------------------------
関数空間 :math:`C^\infty(M)` の位相を何か定義して、コンパクト多様体上のモース関数の性質を述べたい。

以下で使用する記号として

* :math:`M` を n 次元コンパクト多様体、
* :math:`\set{(U_i, \varphi_i = (x_1^{(i)}, \dotsc, x_n^{(i)}))}` を有限座標近傍系、
* :math:`V_i \subset \closure{V_i} \subset U_i,\ \set{V_i}_{i = 1, \dotsc, k}` を開被覆

とする。

目標は :math:`C^r` 位相というものを定めること、つまり関数 :math:`f \in C^\infty(M)` の
:math:`\eps > 0` 近傍 :math:`N_\eps^r = N_\eps^r(f, \set{V_i})` を定めること。

.. math::
   :nowrap:

   \begin{gather*}
   N_\eps^r(f, \set{V_i}) = \Set{
       f + h \in C^\infty(M)
       \Sth s \le r,\ 
       \norm{D^s((h \circ \varphi_i\inv)|\varphi_i(\closure{V_i}))} < \eps
   }.
   \end{gather*}

「ヤコビ行列の :math:`s \le r` 乗のノルムが抑えられる」の意。
行列に対するノルムが具体的に何であるかを述べていないが、ノルムならば何でもよいようだ。
解析で採用する行列のノルムは次のものが普通であり、次のページでも言及されている：

.. math::

   \norm{A} = \sup_{\bm x \ne 0}\frac{\norm{A\bm x}}{\norm{\bm x}}.

* 補題 5.7.1: 有限座標近傍系を別のものにしても :math:`C^r` 位相は等しい。

  証明に使用する記号を定義しておく。

  * 別の座標近傍系を :math:`\set{(U_j', \varphi_j' = (y_1, \dotsc, y_n))}` とおく。
    このとき、先ほどと同じように開集合、コンパクト集合列 :math:`V_j' \subset \closure{V_j'} \subset U_j'` を取り、
    次を示すことを目標とする：
    
    .. math::
    
       N_\eps^r(f, \set{V_i}) \subset N_{K\eps}^r(f, \set{V_j'})

  * 座標変換をいつものように :math:`\gamma_{ij} = (\varphi_i \circ \varphi_j\inv)|\varphi_j'(U_i \cap U_j')` で表す。
    :math:`h \circ \varphi_j'\inv = (h \circ \varphi_i\inv) \circ \gamma_{ij}` のようになる。

  帰納法で示せば良いようだ。

  * :math:`r = 0` のときは :math:`N_\eps^0(f_i, \set{V_i}) = N_\eps^0(f_i, \set{V_j'})` は成り立つ。

    * ヤコビ行列のゼロ乗のノルムは単位行列のそれとなり、つまり 1 であるからということか。
      ということは、:math:`\eps` の値によっては :math:`C^0` 近傍は空集合になったりするのか？

  * :math:`r = 1` のとき：

    * :math:`D(h \circ \varphi_j'\inv) = D(h \circ \varphi_i\inv) \circ \gamma_{ij} D\gamma_{ij}` であり、
    * そして :math:`N_\eps^1(f, \set{V_i}) \subset N_K^1(f, \set{V_j'})` を満たす
      :math:`\eps` に依存する正の数 :math:`K` が下のようにしてとれるので成り立つ：

      .. math::
         :nowrap:

         \begin{gather*}
         K = \max_{i, j}
         \max_{x \in \varphi_j'(\closure{V_i} \cap \closure{V_j}')}
         \norm{D\gamma_{ij(x)}}.
         \end{gather*}

      添字が有限個であることと、各 :math:`\closure{V_i} \cap \closure{V_j}'` がコンパクトであることによる。

  * :math:`r = 2` のときは p. 104 のような（ここにはとても記せられない）計算をして
    :math:`N_\eps^2(f, \set{V_i}) \subset N_K^2(f, \set{V_j'})` を満たす
    :math:`\eps` 依存の正数 :math:`K` を取れることを示す。

  * 一般の :math:`r = s` のときは、chain rule を順次実行して、
    上記の場合の成立を根拠に成り立つことを示す。

    * `ファー・ディ・ブルーノの公式 <http://mathworld.wolfram.com/FaadiBrunosFormula.html>`__
      という、合成写像の高次の微分を書き下すやり方がある。

* 定義 5.7.2: コンパクト多様体に関する関数空間 :math:`f \in C^\infty(M)` の :math:`C^r` 位相。
* 注意 5.7.3: コンパクトでない多様体の場合について。

  * :math:`\closure{V_i}` がコンパクトであるような開被覆を取れれば
    :math:`C^\infty(M)` の位相を定められる。ただし、開被覆の取り方が変わると位相も変わる。

* 定理 5.7.4: :math:`f \in C^\infty(M)` の :math:`C^2` 位相で、モース関数全体は開かつ稠密。

コンパクト多様体間の写像全体の空間 :math:`C^\infty(M, N)` についても :math:`C^r` 位相を考えられる。

* 多様体 :math:`N` の有限局所座標系を :math:`\set{(W_j, \psi_j)}` とする。

  * このとき次のような開被覆 :math:`\set{V_{ji}}` が存在するのであった：
    :math:`V_{ji} \subset \closure{V_{ji}} \subset U_i \cap F\inv(W_j).`

  * 開近傍の取り方は次のようになる：

    .. math::
       :nowrap:

       \begin{gather*}
       N_\eps^r(F, \set{V_{ji}}, \set{W_j}) = \Set{
           H \in C^\infty(M, N)
           \Sth s \le r,\ 
           \forall i, j,
           \norm{D^s((\psi_j \circ H \circ \varphi_i\inv - \psi_j \circ F \circ \varphi_i\inv)|\varphi_i(\closure{V_{ji}}))} < \eps
       }.
       \end{gather*}

    :math:`\varphi_i(\closure{V_{ji}})` はコンパクトゆえ、上の長い関数 :math:`\varphi_i(\closure{V_{ji}}) \longto \psi_j(V_j) \subset \RR^n`
    に近い :math:`C^\infty` 写像の像は :math:`\psi_j(V_j)` にあり、微分が定義できる。

  * :math:`C^r` 位相は各有限座標近傍系のとり方によらない。

写像の空間の開かつ稠密な集合は横断性を考えることで与えられる (p. 115)。

* 定理 5.7.6: 横断性定理

  難しい。

  :math:`C^\infty(M, N)` の :math:`C^1` 位相において、
  :math:`N` の部分多様体 :math:`L` を横断的な写像は開かつ稠密である。

  * :math:`F \in C^\infty(M, N)` について :math:`F(x) \in L` ならば
    :math:`F_*(T_x(M)) + T_{F(x)}L = T_{F(x)}N` が成り立つものの性質に関する定理。

  * 証明では線形代数の何かをまず利用する。
  * 途中、サードの定理を必要とする。

* 注意 5.7.7: :math:`\fn{F}{M}N` が :math:`L \subset N` と横断的ならば、
  :math:`F\inv(L)` は :math:`M` の余次元が :math:`L` のそれに等しいような部分多様体である。

* 注意 5.7.8: これは何を言っているのかわからない。
  包含写像の一方を近似する写像と取り替えると横断的となるとは？

5.8 第 5 章の問題の解答
----------------------------------------------------------------------
ノートはすでに書いた。

----

:doc:`note6` へ。
