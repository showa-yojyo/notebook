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
       x \in M \setminus \supp{F} \Longleftrightarrow \exists U \owns x: f(U) = \zeroset
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

        \forall x_0 \in K, \exists \mu_{x_0}: M \longto \RR \quad \text{s.t. }
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

  #. 前定理の性質を満たす関数 :math:`\nu_1: M \longto \RR` をとる。
  #. :math:`K = \supp \nu_1 \setminus \operatorname{int}(\supp \nu_1)` は
     開集合 :math:`U \setminus K` のコンパクト部分集合である。
  #. 繰り返し前定理を再利用し、関数 :math:`\nu_2: M \longto \RR` がとれる。
     :math:`(\nu_1 + \nu_2)|\supp \nu_1 > 0` より次の関数を考える：

     .. math::

        \nu(x) =
        \begin{cases}
        \displaystyle \frac{\nu_1}{\nu_1 + \nu_2} & \quad \text{if } x \in \operatorname{int}(\supp(\nu_1 + \nu_2))\\
        0 & \quad \text{if } x \in M \setminus \operatorname{int}(\supp(\nu_1 + \nu_2)).
        \end{cases}

     これは所望の条件をすべて満たす。

* 注意 5.1.4 の :math:`\nu f: M \longto \RR,\ \nu|K = f|K` の意味は、
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
     :math:`\displaystyle t \longmapsto \varphi^{-1}(0, \dotsc, \overset{(k)}t, \dotsc, 0)` における方向微分とする (cf. p. 76)。

     * :math:`Df` が点 :math:`p` の近傍で定義された :math:`C^\infty` 級関数に対して定義されることを示す。
       この際に定理 5.1.3 の関数 :math:`\nu` および注意 5.1.4 の事実を用いる。

     * :math:`D \in \mathcal D_p` が上述の一次結合で表されることを示す。
       :math:`f \in C^\infty(M)` に対して :math:`\displaystyle \left(\frac{\partial}{\partial x_i} \right)_p f = \frac{\partial(f \circ \varphi^{-1})}{\partial x_i}(0, \dotsc, 0).`

       :math:`(\nu f) \circ \varphi^{-1}` を :math:`\RR^n` 上の関数とみなして、
       アダマールの補題を適用して次のような :math:`g_i` を定義する（これ合っているか？）：

       .. math::

          \begin{align*}
          &(\nu f) \circ \varphi^{-1} = f(p) + \sum_{i = 1}^n x_i g_i(x_1, \dotsc, x_n),\\
          &g_i(0, \dotsc, 0) = \frac{\partial(f \circ \varphi^{-1})}{\partial x_i}(0, \dotsc, 0).
          \end{align*}

     * 点 :math:`p` の近傍では :math:`\displaystyle f = f(p) + \sum_{i = 1}^n (x_i \circ \varphi^{-1})(g_i \circ \varphi^{-1})`
       となっている。よって次のようにすれば線形結合になっていることが示される：
       
       .. math::
       
          \begin{align*}
          Df &= D(f(p)) + \sum_{i = 1}^n (D(x_i)g_i(0) + 0 \cdot D(g_i))\\
             &= \sum_{i = 1}^n D(x_i)\frac{\partial(f \circ \varphi^{-1})}{\partial x_i}(0, \dotsc, 0)\\
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

    * 定理 4.4.2 の上にある説明により :math:`\Phi_*: T_xM \longto \RR^{k(n + 1)}` のランクが
      :math:`n` で :math:`\Phi` が単射であるから。

      * ランクが :math:`n` であることは :math:`(\nu_i \varphi_i | V_i) \circ \varphi_i^{-1} = id_{\varphi_i(V_i)}` から示せる。
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

       :math:`(\bm x, \bm y) \in X \Longleftrightarrow \bm y = (\bm y_1, \bm y_2)` とは、
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

* <写像 :math:`F: M \longto N` が与えられ、:math:`N` の形と :math:`F^{-1}(y)\ (y \in N)` の形が理解できれば、
  :math:`M` の形がわかることが期待できる> (p. 101)

  * 写像 :math:`F` については :math:`F_*|T_xM \longto T_{F(x)}N` のランクが :math:`\dim N` であるようなものがよいと思われる。
    こういう :math:`x` とそれに対応する :math:`y` はそれぞれ正則点、正則値であるという。

    * 言葉に引っ張られないように。正則「値」と言っても多様体上の点を指している。

  * 正則値の逆像 :math:`F^{-1}(y)` は :math:`\dim M - \dim N` 次元部分多様体である。
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
  * :math:`\exists \lambda_i: M \longto \RR\ s.t. \lambda_i \in C^\infty(M),\ 0 \le \lambda_i(x) \le 1,\ \supp{\lambda_i} \subset U_i.`
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

  * :math:`C\infty` 級写像 :math:`F: M \longto N` の臨界値は測度が 0 である。

* 定義 5.4.2: 非退化、`モース関数 <http://mathworld.wolfram.com/MorseFunction.html>`__

  * 臨界点 :math:`x` が非退化であるとは、点 :math:`x` における関数のヘッセ行列が正則であることをいう。
  * 関数 :math:`f \in C^\infty(M)` がモース関数であるとは、
    多様体上のどの臨界点においても非退化であることをいう。

* ヘッセ行列の正則性は座標近傍の取り方によらない：
  :math:`H(f \circ \varphi^{-1}) = {}^t\!PH(f \circ \psi^{-1})P.`

* 二次曲面の形は行列 :math:`\displaystyle \sum_{i, j}^n \frac{\partial^2(f \circ \varphi^{-1}}{\partial x_i \partial x_j}(\varphi(x))`
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
       (f \circ \varphi_i^{-1})(x_1, \dotsc, x_n) = f(x^0) - \sum_{i = 1}^k x_i^2 + \sum_{i = k + 1}^n x_i^2.
       \end{align*}

  * 証明方針を挙げていく：

    * 点 :math:`x^0` を原点に移動して考えたい。つまり :math:`f - f(x^0)` を最初から考える。
    * 線形変換しておいて :math:`\displaystyle \frac{\partial^2 f}{\partial x_i \partial x_j}(0, \dotsc, 0)` が対角化されているようにする。
    * 関数 :math:`f` をアダマールの補題（先述）による書き方にしておく。
    * 平方完成と座標変換を順次適用する。本書参照。

* 例 5.4.4: 例題 2.4.1 の吟味

  * この関数は実はモース関数なのであった。
  * 球面上には指数 0, 1, 2 の臨界点がそれぞれ 2 個ずつある。

* 問題 5.4.5: :math:`f(x, y) = (2 + \cos y)(a\cos x + b \sin x) + c \sin y,\ ((a, b, c) \ne (0, 0, 0))`

  この関数は :math:`F: \RR^2/(2\pi\ZZ)^2 \longto \RR` を定義する。
  臨界点の個数が有限となる条件と退化する条件とを求める。

  * まずはヤコビ行列を計算する。
  * それからヘッセ行列を計算する。
  * あとは三角関数の性質を利用する。

* 問題 5.4.6: 複素射影空間 :math:`\CC P^n = (\CC^{n + 1} \minuszero)/\CC^\times` の
  単位球面 :math:`S^{2n + 1} = \set{(z_1, \dotsc, z_{n + 1}) \in \CC^{n + 1} \sth \abs{z} = 1}` と
  :math:`U(1) = \set{e^{\sqrt{-1}\theta} \sth \theta \in \RR}` について

  直球のような設問。この問題は理解していないといけない。

  * :math:`g \in U(1)` に対して :math:`(g, z) \mapsto (gz_1, \dotsc, gz_n)` とすると、これは群の作用となる。
  * :math:`S^{2n + 1} \overset{i}{\longto} \CC^{n + 1}\minuszero \overset{p}{\longto} \CC P^n` のランクはいくらか。
    ただし :math:`i,\ p` は包含写像と射影である。
  * 次に示す関数は :math:`F: \CC P^n \longto \RR` を誘導する：

    .. math::
       :nowrap:

       \begin{align*}
       f(z) = \frac{\displaystyle \sum_{k = 1}^{n + 1} k \abs{z_k} ^2}{\displaystyle \sum_{k = 1}^{n + 1} \lvert z_k \rvert ^2}.
       \end{align*}

  * :math:`F` の臨界点は :math:`F_*: T_x \CC P^n \longto \RR` がゼロとなる
    :math:`x \in \CC P^n` である。

  * ヘッセ行列を求める。

* ほとんどすべての射影がモース関数である (p. 107)。

* 問題 5.4.8: 問題 5.2.5 の続き。後回しにしたい。

  * 同じ記号を引き続き用いる上で、次の仮定を追加する：

    * :math:`i: M \longto \RR^N` を包含写像、
    * :math:`\operatorname{pr}_2: \RR^N \longto \RR^N` を第二成分への射影、
    * :math:`L: \RR^N \longto \RR` を線形写像 :math:`{\displaystyle L(\bm x) = \sum_{i = 1}^N a_i x_i}` とする。

  * :math:`\bm a \in \RR^N` が :math:`\operatorname{pr}_2|X` の正則値であることと、
    :math:`L \circ i` がモース関数であることは同値である。

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
       \norm{D^s((h \circ \varphi_i^{-1})|\varphi_i(\closure{V_i}))} < \eps
   }.
   \end{gather*}

「ヤコビ行列の :math:`s \le r` 乗のノルムが抑えられる」の意。
ノルムが具体的に何であるかを述べていない気がする。何か読み落としているか？

* 補題 5.7.1: 有限座標近傍系を別のものにしても :math:`C^r` 位相は等しい。

  証明に使用する記号を定義しておく。

  * 別の座標近傍系をダッシュを付けて表し、座標は :math:`y_i` で表す。
  * 座標変換をいつものように :math:`\gamma_{ij} = (\varphi_i \circ \varphi_j^{-1})|\varphi_j'(U_i \cap U_j')` で表す。
    :math:`h \circ \varphi_j'^{-1} = (h \circ \varphi_i^{-1}) \circ \gamma_{ij}` のようになる。

  帰納法で示せば良いようだ。

  * :math:`r = 0` のときは :math:`N_\eps^0(f_i, \set{V_i}) = N_\eps^0(f_i, \set{V_j'})` は成り立つ（なぜ？）
  * :math:`r = 1` のとき：

    * :math:`D(h \circ \varphi_j'^{-1}) = D(h \circ \varphi_i^{-1}) \circ \gamma_{ij} D\gamma_{ij}` であり、
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

      * 行列のノルムを :math:`\displaystyle \norm{A} = \sup_{x \ne 0}\frac{\lVert A \bm{x} \rVert}{ \lVert \bm{x} \rVert}` とする。

  * :math:`r = 2` のときは p. 104 のような（ここにはとても記せられない）計算をして
    :math:`N_\eps^2(f, \set{V_i}) \subset N_K^2(f, \set{V_j'})` を満たす
    :math:`\eps` 依存の正数 :math:`K` を取れることを示す。

  * 一般の :math:`r = s` のときは、chain rule を順次実行して、
    上記の場合の成立を根拠に成り立つことを示す。

    * `ファー・ディ・ブルーノの公式 <http://mathworld.wolfram.com/FaadiBrunosFormula.html>`__
      という、合成写像の高次の微分を書き下すやり方がある。

* 定義 5.7.2: コンパクト多様体に関する関数空間 :math:`f \in C^\infty(M)` の :math:`C^r` 位相。
* 注意 5.7.3: コンパクトでない多様体の場合について。
* 定理 5.7.4: :math:`f \in C^\infty(M)` の :math:`C^2` 位相で、モース関数全体は開かつ稠密。

コンパクト多様体間の写像全体の空間 :math:`C^\infty(M, N)` についても :math:`C^r` 位相を考えられる。

* 多様体 :math:`N` の有限局所座標系を :math:`\set{(W_j, \psi_j)}` とする。

  * このとき次のような開被覆 :math:`\set{V_{ji}}` が存在するのであった：
    :math:`V_{ji} \subset \closure{V_{ji}} \subset U_i \cap F^{-1}(W_j).`

  * 開近傍の取り方は次のようになる：

    .. math::
       :nowrap:

       \begin{gather*}
       N_\eps^r(F, \set{V_{ji}}, \set{W_j}) = \Set{
           H \in C^\infty(M, N)
           \Sth s \le r,\ 
           \forall i, j,
           \norm{D^s((\psi_j \circ H \circ \varphi_i^{-1} - \psi_j \circ F \circ \varphi_i^{-1})|\varphi_i(\closure{V_{ji}}))} < \eps
       }.
       \end{gather*}

    :math:`\varphi_i(\closure{V_{ji}})` はコンパクトゆえ、上の長い関数 :math:`\varphi_i(\closure{V_{ji}}) \longto \psi_j(V_j) \subset \RR^n`
    に近い :math:`C^\infty` 写像の像は :math:`\psi_j(V_j)` にあり、微分が定義できる。

  * :math:`C^r` 位相は各有限座標近傍系のとり方によらない。

写像の空間の開かつ稠密な集合は横断性を考えることで与えられる (p. 115)。

* 定理 5.7.6: 横断性定理。
  :math:`C^\infty(M, N)` の :math:`C^1` 位相において、
  :math:`N` の部分多様体 :math:`L` を横断的な写像は開かつ稠密である。

  * :math:`F \in C^\infty(M, N)` について :math:`F(x) \in L` ならば
    :math:`F_*(T_x(M)) + T_{F(x)}L = T_{F(x)}N` が成り立つものの性質に関する定理。

  * 証明では線形代数の何かをまず利用する。
  * 途中、サードの定理を必要とする。

* 注意 5.7.7: :math:`F: M \longto N` が :math:`L \subset N` と横断的ならば、
  :math:`F^{-1}(L)` は :math:`M` の余次元が :math:`L` のそれに等しいような部分多様体である。

* 注意 5.7.8: これは何を言っているのかわからない。
  包含写像の一方を近似する写像と取り替えると横断的となるとは？

5.8 第 5 章の問題の解答
----------------------------------------------------------------------
TBW

----

:doc:`note6` へ。
