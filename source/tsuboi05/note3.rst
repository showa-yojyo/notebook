======================================================================
幾何学 I 多様体入門 読書ノート 3/8
======================================================================
:math:`\require{AMScd}`
:doc:`note2` からの続き。

.. contents:: ノート目次

第 3 章 多様体の定義
======================================================================

3.1 微分可能多様体の定義
----------------------------------------------------------------------
* 用語確認

  * n 次元（微分可能）多様体

    * :math:`C^{\infty}` 級多様体の定義は、前章までに見てきた位相多様体や
      :math:`C^{r}` 級多様体の上位？概念のように捉えられる。

  * 局所座標 or 座標近傍
  * 局所座標系 or 座標近傍系
  * 座標変換
  * パラコンパクト

    * 知らないか、またはど忘れしている。調べておく。

  * 第 2 可算公理

* 例 3.1.5: 2 次曲面 :math:`{ \displaystyle Q = \lbrace (X_1, \dotsc, X_n) \in \mathbb{R}^n \mid \sum_{i = 1}^{n} \lambda_i X_i^2 = b \rbrace \quad (b \ne 0) }`

  * 座標近傍系を定義することで、曲面が多様体であることを示す。
  * :math:`U_i^+ := Q \cap \lbrace X_i > 0 \rbrace, \varphi_i^+(X_1, \dotsc, X_n) = (X_1, \dotsc, \widehat{X_i}, \dotsc, X_n)` などと置く
    （ハットの部分は除去を意味する記法）。

  * 開集合 :math:`U_i^\pm` をすべて合併させると曲面全体を覆う。
  * 写像 :math:`\varphi_i^\pm: Q \longrightarrow \mathbb{R}^{n - 1}` はちょっとした計算により同相写像であることを示せる。
  * 座標変換 :math:`\varphi_i^\sigma \circ (\varphi_j^\tau)^{-1}` が :math:`C^{\infty}` 級であることも同様にして示せる。

* 例 3.1.6: 多様体の直積、直和はどちらも多様体となる。次のようにして位相が定まる：

  * 直積の位相: :math:`U_1 \times U_2` の任意個の和集合を開集合とする。
  * 直和の位相: :math:`U_1 \sqcup U_2` を開集合とする。

3.2 商空間（基礎）
----------------------------------------------------------------------
* 確認: 商空間 :math:`X/\sim` の位相の入れ方、誘導される写像。

* 例 3.2.1: n + 1 次元空間内の「球面」
  :math:`S^n` の対蹠点を同一視することで構成される射影空間 :math:`\mathbb{R}P^n` は多様体となる。

  * 前半は「球面」が多様体であることを示す。

    * 局所座標系 :math:`\lbrace (U_i^\pm, \varphi_i^\pm)\rbrace` を次のように定義する。

      .. math::
         :nowrap:

         \begin{align*}
         U_i^\pm & = \lbrace (x_0, \dotsc, x_n) \in S^n \mid \pm x_i > 0 \rbrace,\\
         \varphi_i^\pm (x_0, \dotsc, x_n) & =
         \left(
         \frac{x_0}{x_i}, \dotsc, \widehat{(i)}, \dotsc, \frac{x_n}{x_i}
         \right)
         \end{align*}

    * 各 :math:`\varphi_i^\pm` は対応する :math:`U_i^\pm` 上で連続となり、
      逆写像もまた連続となる。これで同相写像であることは言える。

    * 次に座標変換 :math:`\varphi_j^+(U_i^- \cap U_j^+) \longrightarrow \varphi_i^-(U_i^- \cap U_j^+)` などを計算して、
      これらがすべて滑らかであることを示す。

  * 後半は射影空間が多様体であることを示す。

    * 射影 :math:`p: S^n \longrightarrow \mathbb{R}P^n;\quad [x] \mapsto \lbrace x, -x \rbrace` は同値類への写像となる。
    * 局所座標系 :math:`\lbrace (V_i, \varphi_i) \rbrace` を次のように定義する。

      .. math::
         :nowrap:

         \begin{align*}
         V_i & = \lbrace [\boldsymbol{x}] \in \mathbb{R}P^n \mid x_i \ne 0 \rbrace,\\
         \varphi_i([\boldsymbol{x}]) &= \varphi_i^\pm(\boldsymbol{x})
         \end{align*}

    * このとき、写像 :math:`\varphi_i` は well-defined かつ連続写像かつ逆写像が存在する。
    * 逆写像 :math:`\varphi_i^{-1}` は :math:`p \circ (\varphi_i^+)^{-1} = p \circ (\varphi_i^-)^{-1}` となって連続である。
      図を入れたい。

    * 次に座標変換が滑らかであることを示す。
      これは :math:`\varphi_i \circ \varphi_j^{-1}` が「球面」のときと同じ式で定義されることから言える。

    * 射影空間がハウスドルフであることを示す。
      「球面」がハウスドルフであることと :math:`[\boldsymbol{x^1}] \ne [\boldsymbol{x^2}] \implies \boldsymbol{x^1} \ne \pm \boldsymbol{x^2}` であることから地道に示す。

3.3 変換群
----------------------------------------------------------------------
* 用語確認

  * 位相空間の変換群

    * 同相写像の場合、写像の合成と逆写像をとる操作で閉じている。

  * 作用する

* 定理 3.3.1: 位相空間の有限変換群による商空間はハウスドルフ空間となる。

  * 元の位相空間自身はハウスドルフ空間である必要はないことがポイントか。

この節は例題と問題が多い。どれも大切。
ハウスドルフ空間であることを示すために、二点が「関数で分離される」ことを示す必要がある場合のコツなど。

* 例題 3.3.2: 平面から原点を取り除いた空間において、
  水平な（半）直線に属する点同士を同値類とする商空間は多様体とはならない。

  * 考察対象の空間

    * :math:`Z = \mathbb{R}^2 \setminus \lbrace 0 \rbrace`,
    * :math:`Y = Z / \sim`

  * 考察する写像

    * :math:`p: Z \longrightarrow \mathbb{R}; \quad (x, y) \mapsto y`
    * :math:`\underline{p}: Y \longrightarrow \mathbb{R}; \quad [x, y] \mapsto y`
    * :math:`f^\pm: \mathbb{R} \longrightarrow Z; \quad y \mapsto (\pm 1, y)`
    * :math:`p_Y: Z \longrightarrow Y;` （射影）

  * 合成写像 :math:`p_Y \circ f_\pm` を考える。
    :math:`Y_\pm := (p_Y \circ f_\pm)(\mathbb{R})` とおくと、
    :math:`\underline{p}` との絡みで :math:`Y_\pm` と実数全体が同相であることを示せる。
    商空間の任意の点について、それを含む開近傍が
    :math:`Y_+` か :math:`Y_-` にあると結論できる。

    .. math::
       :nowrap:

       \begin{align*}
       \begin{CD}
       \mathbb R @>{f^\pm}>> Z @>{p_Y}>> Y_\pm \subset Y\\
       @.        @V{p}VV   @V{\underline{p}}VV\\
       @.             \mathbb R @. \mathbb R
       \end{CD}
       \end{align*}

  * 商空間はハウスドルフではない。
    数直線の正の部分と負の部分が（見てくれに反して）分離できない。

* 問題 3.3.3: 平面から原点を取り除いた空間において、
  直角双曲線と座標軸に沿う半直線 4 本で埋め尽くされる商空間
  （双曲線や座標軸の部品を点とみなす）は多様体とはならない。

  .. math::
     :nowrap:

     \begin{CD}
     \mathbb R @>{g_\pm,\ h_\pm}>> Z @>{p_X}>> X_\pm^g, X_\pm^h = X\\
     @.        @V{p}VV   @V{\underline{p}}VV\\
     @.             \mathbb R @. \mathbb R
     \end{CD}

  * 商空間の任意の点に対して、それを含む開近傍が存在して、ある開区間と同相とはなるものの、
  * 商空間はハウスドルフではない。
  * この問題は、考える写像がけっこうあるので図式をスケッチしながら解く。

* 問題 3.3.4: 平面から原点を除いた部分を図形で埋め尽くして同値類のなす商空間が多様体にならないパターンの問題。

  * 行列 :math:`A = { \displaystyle \left( \begin{array}{ c c } a & 0 \\ 0 & \cfrac{1}{a} \end{array} \right) \ (a > 1) }` をとり、
    元の空間における同値関係を :math:`z_1 \sim z_2 \Leftrightarrow \exists n \in \mathbb{Z}: A^n z_1 = z_2` で定義する。

  * 対象となる空間は :math:`Z = \mathbb{R}^2 \setminus \lbrace (0, 0) \rbrace,\ S = Z / \sim`
  * これはまだ理解していないが、
    :math:`(x, y) \in Z` に対して開区間 :math:`{ \displaystyle I =  \left( \cfrac{1}{\sqrt{a}}x, \sqrt{a}x \right)}` を導入する。
  * 写像 :math:`p_s: Z \longrightarrow S` を射影とする。
  * 写像 :math:`i: I \times \mathbb{R} \subset Z \longrightarrow Z` を包含写像とする。
  * 写像 :math:`s: W := (p_s \circ i)(I \times \mathbb{R}) \longrightarrow I \times \mathbb{R}` を代表元を取る写像として構成したい。

    .. math::
       :nowrap:

       \begin{CD}
       I \times \mathbb{R} @>{\iota}>> Z @>{p_s}>> W \subset S @>{s}>> I \times \mathbb{R}
       \end{CD}

    * 連続であることをも示す。ここが理解できていない。

  * :math:`s \circ (p_s \circ i)` と :math:`(p_s \circ i) \circ s` がそれぞれ恒等写像であることを示す。
    :math:`W \cong I \times \mathbb{R} \implies I \times \mathbb{R} \cong \mathbb{R}^2\ ([x] \in W)` を示す。

* 例題 3.3.5: :math:`\mathbb{R}/\mathbb{Z} \cong S^1` は多様体になる。

  * 同値関係 :math:`x_1 \sim x_2 \Leftrightarrow x_1 - x_2 \in \mathbb{Z}` で商空間 :math:`\mathbb{R}/\sim` を定義する。
  * 射影を :math:`p` とする。

    * ある閉集合の像 :math:`p(\lbrace 0 \le x \le 1 \rbrace)` が空間全体となるゆえ、商空間はコンパクトであるといえる。

  * 座標近傍系を次のように構成する。

    * 同値類 :math:`[x]` に対して開区間 :math:`I_x := (x - 1/4, x + 1/4) \subset \mathbb{R}` を定義する。
    * 同値類からその代表元を :math:`I_x` の中にあるように取る（？）写像を :math:`s_x` を定義する。

      * :math:`s_x` は連続となる。なぜなら開集合 :math:`U \subset I_x` に対して
        :math:`{ \displaystyle p^{-1}(s_x^{-1}(U)) = \bigcup_{n \in \mathbb{Z}}\lbrace x + n \mid x \in U \rbrace }` は開集合だから。

      * :math:`s_x` は同相となる。なぜなら
        :math:`(p|I_x) \circ s_x = \operatorname{id},\quad s_x \circ (p|I_x) = \operatorname{id}` であるから。

    * :math:`\lbrace (p(I_x), s_x) \rbrace_{x \in \mathbb{R}}` が構成できた。

  * これがハウスドルフであることを直接示すのは面倒。

  * 円周 :math:`S^1` と同相となることを示せる。

    * 実数から円周への写像 :math:`h: x \mapsto (\cos 2\pi x, \sin 2 \pi x)` を定義する。
    * 誘導される写像 :math:`\underline{h} = h \circ p^{-1}` が定義でき、
      これが全射であるだけでなく、単射であることを示せば、同相であると結論できる。

* 例題 3.3.6: :math:`\mathbb{R}P^n = S^n / \lbrace \pm 1 \rbrace = (\mathbb{R}^{n + 1} \setminus \lbrace 0 \rbrace) / \mathbb{R}^\times`

  * 次のような写像 :math:`f: \mathbb{R}^{n + 1} \setminus \lbrace 0 \rbrace \longrightarrow \mathbb{R}` をまず定義し、
    これが well-defined であることを確認する。

    .. math::
       :nowrap:

       \begin{align*}
       f(\boldsymbol{x_2}) = \cfrac{\lvert \boldsymbol{x_1} \cdot \boldsymbol{x_2} \rvert }{\lVert \boldsymbol{x_1} \rVert \cdot \lVert \boldsymbol{x_2} \rVert}
       \end{align*}

  * 次に誘導される写像 :math:`\underline{f}` が連続であることを示し、
    コーシー・シュワルツの不等式の等式成立条件などからハウスドルフであることを示す。

  * 多様体であることを示すために、局所座標系 :math:`\lbrace (V_i, \varphi_i) \rbrace` を定義する。

    .. math::
       :nowrap:

       \begin{align*}
       V_i & = \lbrace [\boldsymbol{x}] \in \mathbb{R}^{n + 1} \setminus \lbrace 0 \rbrace \mid x_i \ne 0 \rbrace,\\
       \varphi_i([\boldsymbol{x}]) &= \left( \frac{x_0}{x_i}, \dotsc, \widehat{(i)}, \dotsc, \frac{x_n}{x_i} \right)
       \end{align*}

    * TODO: ここに包含写像を説明する可換図式みたいなものを挿れたい。

  * 座標変換が滑らかであることを示す。
  * 射影空間では超平面とそれに含まれない直線とは必ず一点で交わる。

* 問題 3.3.7: :math:`\mathbb{C}P^n := (\mathbb{C}^{n + 1} \setminus \lbrace 0 \rbrace) / \mathbb{C} ^ \times` は多様体になる。

3.4 :math:`C^r` 級多様体の間の :math:`C^s` 級写像、微分同相写像
----------------------------------------------------------------------
ここでは :math:`s \le r` とする。

:math:`C^s` 級
  写像 :math:`F: M_1 \longrightarrow m_2` が :math:`C^s` 級 であるとは、
  写像 :math:`\psi \circ F \circ \varphi^{-1}: \varphi(U) \longrightarrow \psi(V)` が :math:`C^s` 級 であることとする。

微分同相写像
  写像 :math:`F_1 \text{or} F_2` が微分同相写像であるとは、
  :math:`F_1 \circ F_2 = \operatorname{id}_{M_2}` かつ
  :math:`F_2 \circ F_1 = \operatorname{id}_{M_1}` であることとする。

* 例 3.4.3

  #. :math:`\mathbb{R}/\mathbb{Z} \cong S^1`
  #. :math:`\mathbb{R}^2/(2 \pi \mathbb{Z})^2 \cong T^1`

* 問題 3.4.4: 複素射影直線と球面は微分同相である。
  :math:`\mathbb{C}P^1 = (\mathbb{C}^2 \setminus \lbrace 0 \rbrace) / \mathbb{C} ^ \times \cong S^2`

  #. ヒントに従うと、次のふたつの射影による座標近傍系を定義できる。
  #. :math:`\mathbb{C}P^1` に開集合 :math:`V_i = \lbrace [x] \in (\mathbb{C}^2 \setminus \lbrace 0 \rbrace) / \sim\ \mid x_i \ne 0 \rbrace,\ (i = 0, 1)` を入れる。

     * TODO: 可換図式みたいなのを挿れたい。

* 問題 3.4.5: 四元数を意識したクイズ。

  * これは線形代数が相当得意でないと解けないと見た。
    例えば :math:`SO_3` の行列の固有値が :math:`\lambda, \bar{\lambda}, 1` であることを知らない程度では歯が立たない。

* 例題 3.4.7: 自身への微分同相の例として対蹠点、平行移動、行列式が非ゼロである線型写像を挙げている。

* 用語確認

  * :math:`C^\infty` 級変換群
  * :math:`C^\infty` 級に作用する or 滑らかに作用する
  * 効果的

    * :math:`K = \lbrace g \in G \mid gx = x \rbrace` のとき。
    * :math:`K` は正規部分群となる。

* <群の構造だけを取り出した群> とは？

* 定理 3.4.8: 滑らかな多様体の滑らかな有限変換群に対する商空間は、滑らかな多様体となる。
* 例題 3.4.9: レンズ空間 :math:`S^3 := \lbrace (z_1, z_2) \in \mathbb{C}^2 \mid \lvert z_1 \rvert ^2 + \lvert z_2 \rvert ^2 = 1 \rbrace`

  * 有限変換群 :math:`F` の元は互いに素な自然数の組 :math:`p, q` を用いて構成できる。
    LaTeX を書くと字が潰れるので省略。

  * この有限群は位数 :math:`p` の巡回群 :math:`\mathbb{Z}/p\mathbb{Z}` になり、
    :math:`S^3` へ作用する。定理 3.4.8 により :math:`S^3/F` は多様体となる。

    * これを :math:`L_{p, q}` と表す。ちなみに :math:`L_{2, 1}` は
      :math:`\mathbb{R}P^3` と微分同相となる。

3.5 座標変換
----------------------------------------------------------------------
* <多様体の定義において最も重要なものは、座標近傍系である> (p. 61)
* 座標変換から多様体を構成する手法がファイバー束、ベクトル束の全空間を
  多様体と考えるときに必要となる。

* 例題 3.5.1: 座標近傍の同相写像がまた同相写像となる。

  * :math:`\gamma_{ij}: \varphi_j(U_i \cap U_j) \longrightarrow \varphi_i(...)` を
    :math:`\gamma_{ij} = \varphi_i \circ (\varphi_j|U_i \cap U_j)^{-1}` で定義する。
    このとき :math:`\varphi_k(U_i \cap U_j \cap U_k)` 上は
    :math:`\gamma_{ij} \circ \gamma_{jk} = \gamma_{ik}` となる。

    * 図を描いて確認しよう。定義域が怪しくないことも確認する。

  * 以下紙幅の都合上 :math:`V_i = \varphi_i(U_i),\ V_{ij} = \varphi_j(V_i \cap V_j)` とおく。
  * 写像 :math:`\gamma_{ij}` は :math:`\mathbb R^n` の開集合の間の同相写像となる。

    .. math::
       :nowrap:

       \begin{CD}
       V_{ik} \cap V_{jk} @>{\gamma_{jk}}>> V_{ij} \cap V_{kj} @>{\gamma_{ij}}>> V_{jk} \cap V_{ki}
       \end{CD}

* 一般の開集合 :math:`V_i \subset \mathbb R^n` の直和について。

  * :math:`{ \displaystyle \bigsqcup_{i \in I} V_i = \bigsqcup_{i \in I} V_i \times \{i\} \subset \mathbb R^n \times I}`

  * 左辺は :math:`\mathbb R^n \times I` の直積位相から誘導される位相を入れる。
  * :math:`\mathbb R^n` の位相はいつものユークリッド空間位相を入れる。
  * 添字集合 :math:`I` には離散位相を入れる。
  * c.f. この直和位相（仮称）を一般の位相空間に対する直和位相

* 例題 3.5.2: 例題 3.5.1 の記号の一部を流用し、開集合の直和に同値関係を入れて商空間を定義する。

  #. まず :math:`x_i \sim x_j \Leftrightarrow x_j \in V_{ij} \subset V_j,
     x_i = \gamma_{ij}(x_j)` とする。これは同値関係になることを確認する。

  #. ここで :math:`X = (\bigsqcup V_i / \sim)` がハウスドルフであれば、多様体となるといえる。

     * 射影 :math:`p: \bigsqcup V_i \longrightarrow X` を考える。
       :math:`V_i` と :math:`p(V_i)` が同相である。
       代表元を取る写像を :math:`s_i` とすると、次のようにして連続であることがわかる：

       :math:`V_i` の開集合 :math:`W` に対して
       :math:`s_i^{-1}(W)` が開集合であり、
       :math:`p^{-1}(s_i^{-1}(W)) \subset \bigcup V_i` が開集合であることによる。

     * 写像 :math:`s_i` は同相である。なぜなら :math:`p \circ s_i = \operatorname{id}_{p(V_i)}` かつ
       :math:`s_i \circ p = \operatorname{id}_{V_i}` だから。

     * 最後に、商空間の近傍系 :math:`\{(p(V_i), s_i)\}_{i \in I}` の座標変換が滑らかであることを
       示して（最初から商空間はハウスドルフと言っているから）多様体であることが示せる。

  #. n 次元 :math:`C^\infty` 多様体 :math:`M` と上述の商空間 :math:`X` とが微分同相となる。
     例題 3.5.1 の記号を流用すると、

     * 写像 :math:`\iota: x_i \in V_i \mapsto \varphi_i^{-1}(x_i)` を考える。
       このとき、誘導される写像 :math:`\underline{\iota}: X \longrightarrow M` は連続となる。

       なぜなら :math:`x_i \in V_{ij}, \iota(\gamma_{ji}(x_i)) = \iota(x_i)` だから。

     * 写像 :math:`p \circ \varphi_i: U_i \longrightarrow p(V_i)` は同相の合成で同相。

     * :math:`\underline{\iota} \circ (p \circ \varphi_i) = \operatorname{id}_{U_i}` かつ
       :math:`(p \circ \varphi_i) \circ (\underline{\iota} \mid p(V_i)) = \operatorname{id}_{p(V_i)}` となるので、
       :math:`\underline{\iota} ^{-1} = (p \circ \varphi_i)` は連続。
       したがって :math:`M` と :math:`X` は同相であり、
       :math:`X` はハウスドルフだ。

     * あとは座標近傍系
       :math:`\{(U_i), \varphi_i)\}`,
       :math:`\{(p(V_i), s_i)\}`
       同士を比較することで :math:`\underline{\iota}` が微分同相であると結論する。

* 問題 3.5.3: ファイバー束

  * :math:`E, B, F` を位相空間とする。
  * 写像 :math:`p: E \longrightarrow B` は連続とする。
  * :math:`\forall b \in B` に対する開近傍を :math:`U_b` とする。
  * 直積 :math:`U_b \times F` の第一成分への射影を :math:`\operatorname{pr}_1` とする。

  このとき :math:`B, F` がハウスドルフならば :math:`E` もまたしかり。

  .. math::
     :nowrap:

     \begin{CD}
     E @>{p}>> B\\
     @A{\subset}AA @A{\subset}AA\\
     p^{-1}(U_b) @>{p}>> U_b\\
     @V{h}VV @A{\operatorname{pr}_1}AA\\
     U_b \times F
     \end{CD}

  * この状況における位相空間 :math:`E` をファイバー束といい、
    位相空間 :math:`F` を :math:`B` 上のファイバーという。

  * 証明には :math:`\operatorname{pr}_2` も考える必要がある。

3.6 向き付け（展開）
----------------------------------------------------------------------
ある多様体が向き付けを持つとは、各座標変換のヤコビアンがすべて正であるような
座標近傍系が存在することを意味する。

* 連結多様体 :math:`M` から常に「向き付けを持つ」多様体 :math:`\widehat{M}` を構成できる。

  * :math:`\widehat{M} \cong M \times \{\pm 1\} \Leftrightarrow \forall \gamma_{ij}, \det (D\gamma_{ij}) > 0`

    このとき :math:`M` 自身がすでに向き付け可能。

  * :math:`M` が向き付け不可能で連結であっても :math:`\widehat{M}` は向き付け可能。
  * :math:`P: \widehat{M} \longrightarrow M` において :math:`P^{-1}(y)` の二点を入れ替える写像
    :math:`F: \widehat{M} \longrightarrow \widehat{M}` は、向き付けを反対にする微分同相写像だ。

* 例 3.6.2: 実射影空間は多様体次元の偶数奇数によって向き付け可能性が決まる。
  偶数次元は向きが付けられない。

* 例 3.6.3

  * メビウスバンドのパラメーター表示が紹介されているので有用。
  * 実射影平面から一点を除くとこれと微分同相となる。

3.7 :math:`C^\infty` 級写像の存在について
----------------------------------------------------------------------
* :math:`C^\infty (M, N)` は十分たくさんの元を有し、トポロジーも何か入る。
* :math:`C^\infty (M, \mathbb{R})` を :math:`C^\infty (M)` と略記する。

* 問題 3.7.1: 微分積分の教科書を参照。

  #. :math:`e^x` のマクローリン展開から得られる評価や変数変換（逆数）を駆使する。

  #. 平均値の定理から明らか。

  #. この関数 :math:`\displaystyle
     \rho(x) = 0\ (x \le 0),\ \exp\left(-\frac{1}{x}\right)\ (0 < x)`
     を利用すれば、多様体上の :math:`C^\infty` 級関数を構成できる。

  #. :math:`\mathbb R^n` の連結な折れ線は、実数全体を定義域とする
     :math:`C^\infty` 級写像の像とできるという事実は大事。

3.8 第 3 章の解答
----------------------------------------------------------------------
解答まとめ。

----

:doc:`note4` へ。
