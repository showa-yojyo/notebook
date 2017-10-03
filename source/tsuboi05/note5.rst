======================================================================
幾何学 I 多様体入門 読書ノート 5/8
======================================================================

:doc:`note4` からの続き。

.. contents:: ノート目次

第 5 章 多様体上の関数
======================================================================

5.1 関数の台
----------------------------------------------------------------------
関数の台
  多様体 :math:`M` で定義された関数 :math:`f` に対する次の部分集合のことを関数の台という。

  .. math::
     :nowrap:

     \begin{align*}
     \operatorname{supp}f = \overline{\{x \in M \mid f(x) \ne 0\}}
     \end{align*}

  補集合について次のことが成り立つことに注意する：

  .. math::
     :nowrap:

     \begin{align*}
     x \in M \setminus \operatorname{supp}F \Leftrightarrow \exists U \owns x: f(U) = \{0\}
     \end{align*}

  * 定義上、多様体という条件を位相空間まで緩められる。

* 定理 5.1.1: 任意の :math:`x_0 \in M` とその任意の近傍 :math:`V \in M` に対して、
  次のような :math:`M` を定義域とする :math:`C^\infty` 級関数 :math:`\mu` が存在する：

  #. :math:`\mu(x) \ge 0`
  #. :math:`\mu(x_0) > 0, \operatorname{supp} \mu \in V`
  #. :math:`\operatorname{supp} \mu` がコンパクトである。

  証明方針：問題 3.7.1 の関数 :math:`\rho(x)` を加工してなんとか関数 :math:`\mu(x)` を構成する。

* 定理 5.1.2: :math:`M` のコンパクト集合 :math:`K` とそれを含む開集合 :math:`U` があるとき、
  次のような :math:`M` を定義域とする :math:`C^\infty` 級関数 :math:`\nu` が存在する：

  #. :math:`\nu(x) \ge 0`
  #. :math:`\nu|K(x) > 0`
  #. :math:`\operatorname{supp} \nu` が :math:`U` のコンパクト集合である。

  証明方針：定理 5.1.1 の関数 :math:`\mu(x)` をいくつか足して関数 :math:`\nu(x)` を構成する。

* 定理 5.1.3: 定理 5.1.2 と同じ仮定の下で
  次のような :math:`M` を定義域とする :math:`C^\infty` 級関数 :math:`\nu` が存在する：

  #. :math:`0 \le \nu(x) \le 1`
  #. :math:`\nu|K(x) = 1`
  #. :math:`\operatorname{supp} \nu` が :math:`U` のコンパクト集合である。

* 注意 5.1.4 の :math:`\nu f: M \to \mathbb R,\ \nu|K = f|K` の意味とは？

ここまでの議論で、多様体上には多くの :math:`C^\infty` 級関数が存在することがわかった。

* 補題 5.1.5: アダマール。

  :math:`\mathbb R^n` 内の原点の開近傍で定義されている :math:`C^\infty` 級関数 :math:`f` に対して、
  次のように書けるような :math:`C^\infty` 関数 :math:`g_k (k = 0, \dotsc, n)` が存在する：

  .. math::
     :nowrap:

     \begin{align*}
     f(x_1, \dotsc, x_n) & = f(0, \dotsc, 0) + \sum_{k = i}^{n}x_k g_k(x_1, \dotsc, x_n)\\
     \frac{\partial f}{\partial x_k}(0, \dotsc, 0) & = g_k(0, \dotsc, 0)
     \end{align*}

  初等的な方法で示せる。
  :math:`{ \displaystyle g_k(x_1, \dotsc, x_n) = \int_0^1 \frac{\partial f}{\partial x_k} (tx_1, \dotsc, tx_n) dt}`

* 問題 5.1.6: 方向微分。
  多様体 :math:`M` 上で定義されている :math:`C^\infty` 級関数 :math:`f, g` と点 :math:`p \in M` に対して、
  線形な演算 :math:`D` が定義できて :math:`D(f \cdot g) = Df g(p) + f(p) Dg` が成り立つとする（これを方向微分と呼ぶ）。

  #. 点 :math:`p \in M` における方向微分全てからなる空間 :math:`\mathcal{D}_p` は実ベクトル空間である。
  #. 多様体 :math:`M` 上の曲線 :math:`c(t)\ (c(0) = p)` について
     :math:`{ \displaystyle D_c: f \mapsto \frac{d(f \circ c)}{dt}(0)}` は点 :math:`p` における方向微分である。
  #. :math:`\mathcal{D}_p` の基底は :math:`{ \displaystyle
     \left\{
     \left(\frac{\partial}{\partial x_1} \right)_p,
     \dotsc,
     \left(\frac{\partial}{\partial x_n} \right)_p
     \right\}}` である。

     * :math:`{ \displaystyle \left(\frac{\partial}{\partial x_k} \right)_p}` は関数
       :math:`{ \displaystyle t \mapsto \varphi^{-1}(0, \dotsc, \overset{(k)}t, \dotsc, 0)}` における方向微分とする (cf. p. 76)。
     * これを証明するのに補題 5.1.5 を利用する。

5.2 コンパクト多様体のユークリッド空間への埋め込み
----------------------------------------------------------------------
* 例題 5.2.1: コンパクトハウスドルフ空間は `正規空間 <http://mathworld.wolfram.com/NormalSpace.html>`__ である。

  * 位相空間論の教科書を参照する。
  * まず一点 vs 閉集合について証明する。それから普通の閉集合 vs 閉集合について証明する。

* 例題 5.2.2: コンパクトハウスドルフ空間 :math:`X` の開被覆 :math:`\{U_i\}` に対し、
  次のような開被覆 :math:`\{V_i\}` が存在する：
  :math:`\overline{V_i} \subset U_i`

  * 位相空間論の教科書を参照する。証明方針は次のような感じだ：
  * コンパクト性により、有限開被覆 :math:`\{U_1, \dotsc, U_k\}` が :math:`\{U_i\}` から選べる。
    証明のポイントは元の開被覆を有限開被覆とそれ以外のものとに分けて扱うことにある。

  * 開集合 :math:`V_i` を次のようにとる：

    .. math::
       :nowrap:

       \begin{align*}
       V_i = \left\{
       \begin{array}{ll}
       U_i & (i = 1, \dotsc, k),\\
       \varnothing & (otherwise)
       \end{array}
       \right.
       \end{align*}

  * 閉集合 :math:`{ \displaystyle K_j = X \setminus \left(\bigcup_{i = 1}^j V_i \cup \bigcup_{i = j + 1}^k U_i\right)}`
    を考える（何か :math:`V_i` 周りの記号が帰納法の提示の関係でわかりにくい。ノートをミスったか）。
    例題 5.2.1 により次のような開集合 :math:`V_j, W_j` が（帰納法により）存在する：
    :math:`K_j \subset V_j, X \setminus U_j \subset W_j, V_j \cap W_j = \varnothing`

  * このとき :math:`\overline{V_i} \subset U_i` かつ :math:`\bigcup V_i = X` となっている。

* 定理 5.2.3: コンパクト多様体はユークリッド空間に埋め込める。

  * ポイント：例題 5.2.2 の開被覆の構成手順を二重に行う。
    つまり :math:`\overline{V_i} \subset U_i,\ \overline{W_i} \subset V_i` のようなものを取る。
    これらの有限開被覆の個数を :math:`k` としておく。

  * 閉集合 :math:`\overline{V_i}` に関して定理 5.1.3 の条件を満たす :math:`C^\infty` 級関数 :math:`\nu_i` を取る。
  * 閉集合 :math:`\overline{W_i}` に関して定理 5.1.2 の条件を満たす :math:`C^\infty` 級関数 :math:`\mu_i` を取る。
  * 座標近傍 :math:`(U_i, \varphi_i)` の局所座標 :math:`\varphi_i = (x_1^{(i)}, \dotsc, x_n^{(i)})` に対して
    関数 :math:`\nu_i \varphi_i := (\nu_i x_1^{(i)}, \dotsc, \nu_i x_n^{(i)})` を取ると、これは :math:`C^\infty` 級となる。

  * ここで :math:`\Phi = (\mu_1, \nu_1 \varphi_1, \dotsc, \mu_k, \nu_k \varphi_k)` とおくと、
    これが多様体から :math:`\mathbb R^{k(n + 1)}` への埋め込みとなる：

    * 定理 4.4.2 の上にある説明により :math:`\Phi_*: T_xM \to \mathbb R^{k(n + 1)}` のランクが
      :math:`n` で :math:`\Phi` が単射であるから。

      * ランクが :math:`n` であることは :math:`(\nu_i \varphi_i | V_i) \circ \varphi_i^{-1} = id_{\varphi_i(V_i)}` から示せる。
      * 単射であることは :math:`\Phi(x) = \Phi(y) \implies x = y` を示すのに
        :math:`\mu_i` の成分と :math:`\nu_i` の成分の単射性を別々に示す。
        関数の非ゼロ性と局所座標の微分同相性が使えるので容易に示せる。

ユークリッド空間が利用できるようになったので、内積の話題が出て来るようになる。

法束
  :math:`\nu M = \{(x, v) \in \mathbb R^N \times \mathbb R^N \mid v \perp T_xM \}`

  これはユークリッド空間内の :math:`N` 次元多様体になっている。

法空間
  :math:`\nu_x M = \{v \in \mathbb R^N \mid v \perp T_xM \}`

* TODO: (pp. 96-97) の可換図式を何とかここに描きたい。
* 接束 :math:`TM` が :math:`(V_i \times \mathbb R^n, \gamma_{ij} \times D\gamma_{ij})` から構成されたのと似て、
  法束 :math:`\nu M` は :math:`(V_i \times \mathbb R^{N - n}, \gamma_{ij} \times A_{ij})` から構成される。
  ここで :math:`A_{ij_{(x_j)}} \in GL_{N - n}(\mathbb R)` である。

* 注意 5.2.4: ユークリッド空間 :math:`\mathbb R^{n + 1}` 内の
  :math:`n` 次元コンパクト多様体は向き付け可能とある。理屈が飲み込めない。

* 問題 5.2.5: ユークリッド空間に埋め込まれるコンパクト多様体の性質。
  後回しにしたい。

  #. 法束は :math:`N` 次元多様体になっている。
  #. 写像 :math:`(x, y) \mapsto x + y` は :math:`X \cap (\mathbb R^N \times \{0\})` 近傍で微分同相である。

5.3 :math:`C^\infty` 級写像と多様体の埋め込み、はめ込み
----------------------------------------------------------------------
<どのような次元のユークリッド空間に埋め込まれるかというのは多様体の複雑さをはかる量になる> (p. 98)

* 例 5.3.1: 色々なコンパクト多様体

  * 円周、球面は当然ユークリッド空間 :math:`\mathbb R^2` と :math:`\mathbb R^3` にそれぞれ埋め込まれる。
  * :math:`\mathbb RP^2` は :math:`\mathbb R^3` に埋め込めない。メビウス帯を部分空間として含むことによる。

<埋め込みやはめ込みの空間は、数学的に非常に興味深い> (p. 99)

* 例 5.3.2: 円周 :math:`S^1` の埋め込み

  * 円周の :math:`\mathbb R^2` への埋め込みは円板 :math:`D^2` を囲む。
    :math:`D^2` の :math:`\mathbb R^2` への埋め込みの境界への制限（ジョルダンの閉曲線定理）。

  * 円周の :math:`\mathbb R^3` への埋め込みは制限とはならない。分類＝結び目理論。
  * 円周の :math:`\mathbb R^n\ (n \le 4)` への埋め込みは
    円板 :math:`D^2` の :math:`\mathbb R^n` への埋め込みの境界への制限。

* 多様体の形を理解するには、超球面 :math:`S^n` などのよくわかる多様体から構成的に理解するのがよい。

  * コンパクト連結一次元多様体は :math:`S^1` と微分同相。
  * コンパクトではない可分な連結一次元多様体は :math:`\mathbb R` と微分同相。
  * コンパクト連結二次元多様体

    * 向き付け可能： :math:`S^2, T^2, \Sigma_2, \Sigma_3, \Sigma_4, \dots`; 有向閉曲面は可算個。

      * 有向閉曲面 :math:`\Sigma_k \subset \mathbb R^3` の定義は p. 100 を参照。

    * 向き付け不可能： :math:`\mathbb RP^2, K, N_3, N_4, \dots`; 非有向閉曲面は可算個。
    
      * :math:`\forall x \in \Sigma_k, -x \in \Sigma_k` なので同値関係を定義して :math:`\Sigma_k/\sim` を定義できる。
        このとき、これは多様体となり非有向閉曲面 :math:`N_{k + 1}` となる。

* 例 5.3.3: メビウス帯の像、ホイットニーの傘、クロスキャップ

* <写像 :math:`F: M \to N` が与えられ、:math:`N` の形と :math:`F^{-1}(y)\ (y \in N)` の形が理解できれば、
  :math:`M` の形がわかることが期待できる> (p. 101)

  * 写像 :math:`F` については :math:`F_*|T_xM \to T_{F(x)}N` のランクが :math:`\dim N` であるようなものがよいと思われる。
    こういう :math:`x` とそれに対応する :math:`y` はそれぞれ正則点、正則値であるという。

    * 言葉に引っ張られないように。正則「値」と言っても多様体上の点を指している。

  * 正則値の逆像 :math:`F^{-1}(y)` は :math:`\dim M - \dim N` 次元部分多様体である。
  * 臨界点とは、正則点でない点である。
  * 臨界値とは、臨界点全ての集合の像である。
  * :math:`\dim M < \dim N` のときは、:math:`F(M),\ N \setminus F(M)` がそれぞれ臨界値、正則値である。
    正則値の逆像は空集合になる。

* 例 5.3.4: 例題 2.4.1 の関数の検討
* 例 5.3.5

  * ポーイ・アペリ曲面の平面への射影（写像）など。
  * 問題 2.5.1 では図のソリッドな曲線が臨界値となっている。
  * これらによると、アウトラインが大体臨界値であるということが推測される。

* 例題 5.3.6: 1 の分割

  * :math:`M, \{(U_i, \varphi_i)\}` をそれぞれコンパクト多様体とその座標近傍系とする。
  * :math:`\exists \lambda_i: M \to \mathbb R\ s.t. \lambda_i \in C^\infty(M),\ 0 \le \lambda_i(x) \le 1,\ \operatorname{supp} \lambda_i \subset U_i.`
    有限個の添字を除いて :math:`\lambda_i = 0,\ \sum \lambda_i = 1.`

  * 証明では例題 5.2.2 およびその元となる各種命題を利用している。
    :math:`U_i` 上にある性質の関数 :math:`\mu_{i_j}` を構成して、次のような開被覆および関数を構成する：

    .. math::
       :nowrap:

       \begin{gather*}
       \lambda_{i_{i_j}} = \dfrac{\mu_{i_j}} {\sum_{l = 1}^k \mu_{i_l}},\
       \{U_{i_j}\},\
       \overline{V_{i_j}} \subset U_{i_j},\
       \mu_{i_j}|\overline{V_{i_j}} > 0,\
       \operatorname{supp} \mu_{i_j} \subset U_{i_j}.
       \end{gather*}

5.4 サードの定理とモース関数
----------------------------------------------------------------------
TBW

5.5 サードの定理の証明の概略（展開）
----------------------------------------------------------------------
TBW

5.6 モース関数の存在の証明の概略（展開）
----------------------------------------------------------------------
TBW

5.7 関数の空間、写像の空間（展開）
----------------------------------------------------------------------
TBW

5.8 第 5 章の問題の解答
----------------------------------------------------------------------
TBW

----

:doc:`note6` へ。
