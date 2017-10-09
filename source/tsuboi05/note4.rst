======================================================================
幾何学 I 多様体入門 読書ノート 4/8
======================================================================
:math:`\require{AMScd}`
:doc:`note3` からの続き。

.. contents:: ノート目次

第 4 章 接空間
======================================================================

4.1 曲線の接ベクトル
----------------------------------------------------------------------
接ベクトル
  次のように同値類を構成するときに現れる曲線に関する微分のことを接ベクトルと呼ぶ。

  #. 多様体 :math:`M` とその一点 :math:`x_0 \in M` につき、
     次のような曲線族 :math:`\mathcal{C}_{x_0}` を考える。

     .. math::
        :nowrap:

        \begin{align*}
        \mathcal{C}_{x_0} := \lbrace c_i: (a_i,\ b_i) \longto M \mid c_i(t_i) = x_0 \rbrace _{i \in I}
        \end{align*}

  #. 次にこの一点を含む座標近傍 :math:`(U, \varphi)` をとって、
     曲線族の曲線に次のような同値関係を入れる。

     .. math::
        :nowrap:

        \begin{align*}
        c_1 \sim c_2 \Longleftrightarrow 
        \exists t_1 \in I_{c_1},\ t_2 \in I_{c_2}: \frac{d (\varphi \circ c_1)}{dt}(t_1) = \frac{d (\varphi \circ c_2)}{dt}(t_2)
        \end{align*}

* :math:`{\displaystyle \frac{d (\varphi \circ c_1)}{dt}(t_1)}` 等は :math:`\RR^n` のベクトルであって
  点 :math:`\varphi(x_0) \in \varphi(U)` から「生えている」ようなイメージか？

* 別の近傍 :math:`(V, \psi)` をとって
  :math:`{\displaystyle \frac{d (\psi \circ c_i)}{dt}(t_i)}` を考えると
  「:math:`{\displaystyle \frac{d (\varphi \circ c_i)}{dt}(t_i)}` が同じであることと
  :math:`{\displaystyle\frac{d (\psi \circ c_i)}{dt}(t_i)}` が同じであること」となる。

  * それはなぜか。
    :math:`\psi \circ c_i = (\psi \circ \varphi^{-1}) \circ (\varphi \circ c_i)` であるので、
    chain rule によって適当な近傍において次のようになるから。

    .. math::
       :nowrap:

       \begin{equation*}
       \begin{split}
       \frac{d (\psi \circ c_i)}{dt}(t_i)
       & = D(\psi \circ \varphi^{-1})_{\varphi(x_0)} \frac{d (\varphi \circ c_i)}{dt}(t_i) \quad \because \text{chain rule}\\
       & = D(\psi \circ \varphi^{-1})_{\varphi(x_0)} \frac{d (\varphi \circ c_j)}{dt}(t_j) \quad \because c_i \sim c_j \text{ for } (U, \varphi)\\
       & = \frac{d (\psi \circ c_j)}{dt}(t_j) \quad \because \text{chain rule}
       \end{split}
       \end{equation*}

  * 人のことは言えないが p. 74 の式変形は誤植か？

4.2 接ベクトル空間
----------------------------------------------------------------------
接空間 or 接ベクトル空間
  :math:`T_{x_0}M := \mathcal{C}_{x_0} / \sim` を接空間 or 接ベクトル空間と呼ぶ。

* 接ベクトル空間は実ベクトル空間である。
* 曲線族の曲線に :math:`\RR^n` の接ベクトルを対応させる写像は
  全単射 :math:`\varphi_{*}: \mathcal{C}_{x_0} / \sim \longto \RR^n` を誘導する。
* 単射であることは同値類の定義から従う。
* 全射であることについて。これを示すのに面白い技法を使う。

  接ベクトル :math:`\bm{v} \in \RR^n` に対し
  :math:`c_\varphi ^\bm{v} (t) := \varphi ^{-1}(t \bm{v} + \varphi (x_0))` というのを考える。
  ただし :math:`t \in (-\eps_{\varphi}^\bm{v},\ \eps_{\varphi}^\bm{v})` の範囲で
  :math:`t \bm{v} + \varphi (x_0) \in \varphi(U)` が成り立つように取る。
  こうすると次のようになるので全射であることが示せる（任意のベクトルについて曲線が作れるから）。

  .. math::
     :nowrap:

     \begin{equation*}
     \begin{split}
     \varphi_*(c_\varphi ^\bm{v})
         & = \frac{d(\varphi \circ (\varphi ^{-1} (t \bm{v} + \varphi (x_0))))}{dt}(0) \\
         & = \frac{d(t \bm{v} + \varphi (x_0))}{dt}(0) \\
         & = \bm{v}
     \end{split}
     \end{equation*}

  * この技法はまた出て来る。
  * ところで :math:`\bm{v} = 0` のときも上の議論が通じるだろうか。
    曲線を定数関数とすればいいか。

* 接ベクトル空間のベクトル空間としての構造は、点 :math:`x_0` の別の座標近傍を用いて定義しても変わらない。
  :math:`\bm{v_1}, \bm{v_2} \in \RR^n,\ a_1, a_2 \in \RR` とすると：

  .. math::
     :nowrap:

     \begin{equation*}
     \begin{split}
     \frac{d(\psi \circ c_\varphi^{a_1 \bm{v_1} + a_2 \bm{v_2}})}{dt}(0)
     &= D(\psi \circ \varphi^{-1})_{\varphi(x_0)} \frac{d(t(a_1 \bm{v_1} + a_2 \bm{v_2}) + \varphi(x_0))}{dt}(0)\\
     &= D(\psi \circ \varphi^{-1})_{\varphi(x_0)}(a_1 \bm{v_1} + a_2 \bm{v_2})\\
     &= a_1 D(\psi \circ \varphi^{-1})_{\varphi(x_0)} \bm{v_1} + a_2 D(\psi \circ \varphi^{-1})_{\varphi(x_0)} \bm{v_2}\\
     &= a_1 \frac{d(\psi \circ c_\varphi^{\bm{v_1}})}{dt}(0) + a_2 \frac{d(\psi \circ c_\varphi^{\bm{v_2}})}{dt}(0)
     \end{split}
     \end{equation*}

* 接ベクトル空間の基底は :math:`(c_{\varphi}^{\bm{e}_1}, \dotsc, c_{\varphi}^{\bm{e}_n})` である。

  * :math:`\varphi` に依存して決まることに気をつける。

* :math:`{ \displaystyle [c_{\varphi}^{\bm{e}_i}] := \frac{\partial}{\partial x_i}}` と記す。

  * 理由 1: 曲線は（偏）微分 or 方向微分を表しているとみなせるから。
  * 理由 2: 座標近傍を換えたときの基底変換が形式的にできるから。

    * 接ベクトルは :math:`{ \displaystyle \sum \frac{d(x_i \circ c)}{dt}(t_0) \frac{\partial}{\partial x_i} = \sum \frac{d(y_i \circ c)}{dt}(t_0) \frac{\partial}{\partial y_i} }`
    * 座標変換は :math:`\psi \circ \varphi^{-1} = (y_1(x_1, \dotsc, x_n), \dotsc, y_n(x_1, \dotsc, x_n))`
    * ヤコビ行列は :math:`{ \displaystyle \left( \frac{\partial y_i}{\partial x_j} \right) }`
    * 接ベクトルの変換は :math:`{ \displaystyle \frac{\partial}{\partial x_j}}` を
      :math:`{ \displaystyle \sum_{i = 1}^n \frac{\partial y_i}{\partial x_j} (\varphi(x_0)) \frac{\partial}{\partial y_i} }`
      で置き換える。

4.3 接写像
----------------------------------------------------------------------
接写像
  :math:`F \in C^\infty(M, N),\ x \in M,\ c: (a, b) \longto M,\ c(t_0) = x` を仮定する。
  点 :math:`F(x) \in N` を通る曲線 :math:`F \circ c: (a, b) \longto N,\ (F \circ c)(t_0) = F(x)` という具合になる。
  接ベクトルを接ベクトルに対応させられる。
  このことから線形写像 :math:`F_*: T_x \longto T_{f(x)} N` が定義できる。
  この写像 :math:`F_*` を接写像という。

  * <多様体の間の写像の微分を接空間から接空間への線形写像として定義したもの> だ。
  * 記号は他にも :math:`T_x F,\ D_x F,\ (dF)_x` などがある。
  * 接写像は共変性 :math:`(f \circ g)_* = f_* \circ g_*` が成り立つ。
  * 接写像のランクは :math:`\rank D(\psi \circ F \circ \varphi ^{-1})_{(\varphi(x_0))}` だ。

:math:`F_*` のランクが :math:`n = \dim M = \dim N` であったとしても
:math:`M` と :math:`F(M)` が微分同相であるとは限らない。

* 例題 4.3.1: ただし :math:`M` のコンパクト集合 :math:`K` 上で :math:`F|K` が単射ならば、
  近傍 :math:`V` から :math:`F(V)` への微分同相となる。

  * :math:`F|U_x: U_x \longto V_{F(x)}` が微分同相となるような近傍 :math:`U_x \subset U_i` は存在する（∵逆写像定理）。
  * この近傍 :math:`U_x` はその閉包がコンパクトになるように取れる（らしい）。
  * :math:`K` の開被覆 :math:`\{U_x\}_{x \in K}` は有限開被覆 :math:`\{U_{x_k}\}_{k = 0,\dots\,k_0}` を持つ（∵コンパクト）。

  ここから先の減少列に関する議論がわからない。
  次のような :math:`\{U_x^m\}` があると言えるらしい。

  .. math::
     :nowrap:

     \begin{gather*}
     U_x \supset \overline{U_x^1} \supset U_x^1 \supset U_x^1 \supset \overline{U_x^2} \supset U_x^2 \supset \dots,\\
     \bigcap_{m = 1}^\infty U_x^m = \{ x \}
     \end{gather*}

  * 各 :math:`\{U_x^m\}_{x \in K}` の有限部分？被覆 :math:`\{U_{x_k}^m\}_{k = 1, \dots, k_0^m}` が得られる（∵コンパクト）。
  * :math:`W = \bigcup_k U_{x_k}^m` とおくと
    :math:`W_1 \supset \overline{W_2} \supset W_2 \supset \dots,\ \bigcap\overline{Q_m} = K` とできる。

  * するとある番号があって :math:`F: W_m \longto F(W_m)` が単射となる（背理法と完備性を利用する）。

* 問題 4.3.2: 商空間 :math:`\RR^2/\ZZ^2`

  #. ハウスドルフであること

     * 次の性質を満たす連続関数をうまく見つける。理屈は「任意の二点を関数で分離したい」だ。
       :math:`\alpha, \beta\ (\alpha \ne \beta) \implies f(\alpha) \ne f(\beta).`

     * 解答例では :math:`f_{[x_0, y_0]}(x, y) = \cos 2\pi(x - x_0) + cos 2 \pi(y - y_0)` を採用している。

  #. 商空間が 2 次元の多様体であること

     .. math::
        :nowrap:

        \begin{CD}
        \RR^2 @>{p_x}>> \RR^2/\ZZ^2\\
        @A{\subset}AA @A{\subset}AA\\
        B_x @>{p_x|B_x}>> p_x(B_x)
        \end{CD}

     前章の例題や問題で頻出した技法を適用する。上の図式で、

     * :math:`B_x` は点 :math:`x` を中心とする平面上の半径 1/4 の開円盤。
     * :math:`p_x` は射影とする。

     商空間の点から平面の代表元を取る操作を :math:`s_x` とし、
     座標近傍系を :math:`\{(p_x(B_x), s_x)\}_{x \in \RR^2}` で定義する。

     * :math:`s_x` は連続である。
       なぜならば開集合 :math:`U \subset B_x` に対して
       :math:`p^{-1}(s_x^{-1}(U)) = \bigcup_{m, n \in \ZZ} (U + (m, n))` が開集合であるから。

     * :math:`s_x` は同相写像である。
       なぜならば :math:`s_x \circ (p_x|B_x) = \id_{B_x},\ (p_x|B_x) \circ s_x = \id_{p(B_x)}` だから。

     * 座標変換は :math:`C^\infty` 級である。
       なぜならば点 :math:`z \in p_x(B_x) \cap p_y(B_y)` に対して次を満たす整数の組が何かあるから：
       :math:`s_x(z) = s_y(z) + (m, n)`

     以上とハウスドルフ性により商空間は多様体であると結論できる。

  #. 行列 :math:`A \in M_2(\ZZ)` の定める :math:`\RR^2` 上の線形変換は
     :math:`\RR^2/\ZZ^2` 上の微分可能な変換 :math:`F_A` を定義する。

     * 同値な点が同値な点に写ることはすぐに示せる。写像 :math:`F_A` が well-defined である。
     * 商空間の座標近傍系を前項と同様に定義すると、写像
       :math:`s_{A(x)} \circ F_A \circ p_x` は点 :math:`x` の近傍で元の線形変換と一致するので、
       :math:`F_A` が :math:`C^\infty` 級であるといえる。

  #. :math:`\rank F_A = \rank DF_A = \rank A`

* 問題 4.4.3: リー群。

  #. :math:`L_g: h \mapsto gh` は :math:`C^\infty` 級微分同相である。

     * これは微分同相の定義を確認するだけで済む。
       :math:`L_g \circ L_{g^{-1}} = L_{g^{-1}} \circ L_g = \id_G`

  #. 接写像 :math:`T_{(g, h)}(G \times G) \longto T_{gh}G` のランク。

     * 群の多様体次元と一致することを示すわけだが、ヒントから何をしていいかわからない。
     * 定数関数 :math:`G \owns c_g: g \mapsto a \in \RR` を取る。
     * 次のような演算の列を考える。

       .. math::
          :nowrap:

          \begin{CD}
          G @>{c_g,\ L_h}>> G \times G @>{(op)}>> G @>{L_{(gh)^{-1}}}>> G\\
          @.     @.         @.     @.\\
          T_1 G @>{c_g,\ L_h}_{\ *}>> T_{(g, h)}(G \times G) @>{(op)_*}>> T_{gh}G @>{L_{(gh)^{-1}}}_{\ *}>> T_1 G
          \end{CD}

       左から右まででで恒等写像となり、接写像 :math:`L_{(gh)^{-1}*}` が全単射で、
       中央の写像が全射であることから、ランクが :math:`\dim G` と一致すると結論できる（らしい）。

  #. 逆元を取る演算は :math:`C^\infty` 級である。
  
     * 陰関数定理、逆元写像の接写像 :math:`T_(g, g^{-1})(G \times G) \longto T_1 G` グラフ？

4.4 部分多様体
----------------------------------------------------------------------

* 定義 4.4.1: 部分多様体

  * 多様体 :math:`N` に対して :math:`M \subset N` に次の性質があるとき、
    それを p 次元部分多様体であるという。

    .. math::
       :nowrap:

       \begin{align*}
       \forall x_0 \in M, \exists(U, \varphi): M \cap U = \{x \in U \mid x_{p + 1} = \dots = x_n = 0\}
       \end{align*}

微分可能構造
  座標近傍系の同値類について注意しておく。

はめ込み
  写像 :math:`F: M \longto N` に対し、接写像 :math:`F_*` のランクが
  任意の :math:`x \in M` に対して :math:`\dim M\ (\dim M < \dim N)` となるとき、
  この写像ははめ込みであるという。

埋め込み
  はめ込み :math:`F` によって :math:`N` の位相から誘導される位相が :math:`M` の位相そのものと一致するような
  :math:`F` は埋め込みであるという。

  * :math:`F(M)` は部分多様体となる。

* 定理 4.4.2: はめ込みが単射であれば、コンパクトな多様体の像は部分多様体となる。

沈み込み
  接写像のランクが任意の :math:`x \in M` に対して :math:`\dim N\ (\dim M \ge \dim N)` となるとき、
  この写像は沈み込みであるという。

  * :math:`F^{-1}(y)` は :math:`m - n` 次元部分多様体となる。

* 例題 4.4.3: 部分多様体間の :math:`C^\infty` 級写像が誘導する写像も :math:`C^\infty` 級となる。

  * TODO: ここはノートが特にダメ。やり直し。

  * 多様体が :math:`N_1, N_2`, それらの部分多様体が :math:`M_1, M_2`,
    写像が :math:`F: N_1 \longto N_2` で、誘導される写像が :math:`G: M_1 \longto M_2` であるような図を入れたい。

  * :math:`F(M_1) \subset F(M_2)` とする（？）

  * :math:`M_2 \subset N_2` のある座標近傍 :math:`(V, \varphi)` を次のようにとれる：
    :math:`(x_1, \dotsc, x_p, 0, \dots, 0)` in :math:`M_2 \cap V`

  * 残りの座標成分のほうを考える。
    :math:`(x_1, \dotsc, x_p) \circ F \circ \varphi^{-1}` が :math:`C^\infty` 級となる。
    したがって :math:`G: M_1 \longto M_2` も :math:`C^\infty` 級となる。

* 問題 4.4.4: :math:`GL_2(\RR)` と :math:`SL_n(\RR)`

  * 前者は :math:`n^2` 次元多様体、後者は :math:`n^2 - 1` 次元部分多様体である。

    * GL については :math:`GL_n(\RR) \cong \RR^{n^2}` ゆえ、前者の主張は当然だ。
      解答例によると :math:`\{A \in M_n(\RR) \mid \det A \ne 0\}` が
      :math:`M_n(\RR)` の開集合であることを注意している。

    * SL について。まず定義を書き下してみると :math:`SL_n(\RR) = \{A \in GL_n(\RR) \mid \det A = 1\}` だ。
      そこでこの空間を「写像」 :math:`\det: GL_n(\RR) \longto \RR` における「単位元の逆像」とみなす。

    * :math:`\det` のヤコビ行列なるものを考える。余因子展開を意識することで
      :math:`\det(x_{ij}) = \sum x_{ij} A_{ij}` のように書かれるから、
      :math:`{ \displaystyle \frac{\partial \det}{\partial x_{ij}} = A_{ij}}` で、
      右辺は :math:`(n - 1)^2` 次正方行列の行列式になっている。

    * SL では :math:`D(\det) \ne 0` であることに注意。

  * 行列の積、逆行列を取る演算はどちらも :math:`C^\infty` 級の写像である。

    * 両者ともリー群なので問題 4.4.3 を利用できる。

* 問題 4.4.5: 直交群 :math:`O(n)` は多様体である。

  * 写像 :math:`C: A \mapsto {}^t\!AA` を考える。直交群は「単位元の逆像」となる。
  * 微分を考える。
    :math:`DC_{(A)}X = {}^t\!XA + {}^t\!AX` という形をよく見ると二つの写像
    :math:`X \mapsto {}^AX` と :math:`X \mapsto {}^t\!X + X` の合成であることに気付く。

    * 前者の写像のランクは :math:`n^2` である。
    * 後者の写像のランクは :math:`{ \displaystyle \frac{n(n + 1)}{2}}` である。
    * 合成写像のランクは :math:`{ \displaystyle \frac{n(n + 1)}{2}}` である。

  * よって :math:`{ \displaystyle \dim O(n) = \dim \RR^{n^2} - \rank C = \frac{n(n - 1)}{2} }`

* 例題 4.4.7: 横断的に交わる二つの部分多様体の共通部もまた部分多様体である。

  * :math:`\forall x \in X \cap Z, T_x Y + T_x Z = T_x X`
  * これはあとでやる。部分ベクトル空間の取り扱い方に自信がない。

4.5 接束（展開）
----------------------------------------------------------------------
冒頭のユークリッド空間内の多様体から多様体と接空間のペアの空間を構成する部分は前座。

接束
  前章の記号 :math:`V_i, V_{ij}, \gamma_{ij}` 等を流用する。
  次のようにして構成する商空間を多様体の接束という：

  #. 直和 :math:`\bigsqcup V_i` に同値関係 :math:`x_i \sim x_j \Leftrightarrow x_i = \gamma_{ij}(x_j)` を導入する。
     このとき、商空間 :math:`X = (\bigsqcup V_i / \sim)` は :math:`M` と微分同相になる（例題 3.5.2 などを参照）。

  #. 直積の直和 :math:`\bigsqcup (V_i \times \RR^n)` に次の同値関係を導入する。

     .. math::
        :nowrap:

        \begin{align*}
        (x_i, v_i) \sim (x_j, v_j) \Leftrightarrow \exists \gamma_{ij}:
        x_i = \gamma_{ij}(x_j),\ v_i = (D\gamma_{ij})_{(x_j)} v_j
        \end{align*}

     同値関係となる理由：

     * 写像 :math:`G_{ij}: (x_i, v_i) \mapsto (\gamma_{ij}(xj), (D\gamma_{ij})_{(x_j)} v_j)` を考える。
       これは微分同相となる。
     * そして :math:`G_{ij} \circ G_{jk} = G_{ik}` （ただし :math:`G_{ii} = \id` と約束する）が成り立つ。

     このとき、商空間 :math:`Y = (\bigsqcup (V_i \times \RR^n))/\sim` はハウスドルフとなり、
     :math:`2n` 次元多様体となる。

     ハウスドルフとなる理由（面倒）：

     * 射影をいくつか定義して、その合成写像による商空間の開集合の逆像もまた開集合であることを示し、
       :math:`Y \longto X` に連続写像が存在することを示せる。
     * 次に、直和から商空間への射影二種 :math:`p_x, p_y` を適宜制限して同相写像を得る。
     * 写像 :math:`P^{-1}: (p_x(V_i)) \longto p_x(V_i) \times \RR^n` が同相であることを示す。
     * 最後に問題 3.5.3 を利用する。

  接束はベクトル束の一種である (pp. 85-86)。

* 問題 4.5.2: :math:`F \in C^\infty(M, N)` の引き起こす接束の間の写像
  :math:`F_*: TM \longto TN` は :math:`C^\infty` 級である。

* 問題 4.5.3: ユークリッド空間内の多様体 :math:`M \subset \RR^N` に対して
  :math:`TM` と :math:`X = \{(x, v) \mid x \in M, v \in T_x M\}` は微分同相である。
  
  * 点 :math:`x_0 \in M` の近傍におけるグラフ表示から :math:`X` のグラフ表示を構成する。
  * :math:`TM` の商空間座標近傍系の近傍？から :math:`\RR^N \times \RR^N` への連続写像を定義する。
    これの逆写像を検討する（連続であることと :math:`C^\infty` 級であること）。

----

:doc:`note5` へ。
