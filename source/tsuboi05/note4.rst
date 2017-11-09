======================================================================
幾何学 I 多様体入門 読書ノート 4/8
======================================================================
:math:`\require{AMScd}`
:doc:`note3` からの続き。

.. contents:: ノート目次

第 4 章 接空間
======================================================================
本章の目的は次のとおり：

* 接ベクトル、接空間を考察する。
* 接写像を定義する。
* 多様体間の写像についても逆写像・陰関数定理が応用可能であることを見る。

4.1 曲線の接ベクトル
----------------------------------------------------------------------
`接ベクトル <http://mathworld.wolfram.com/ManifoldTangentVector.html>`__
  次のように同値類を構成するときに現れる曲線に関する微分のことを接ベクトルと呼ぶ。

  #. 多様体 :math:`M` とその一点 :math:`x_0 \in M` につき、
     次のような曲線族 :math:`\mathcal{C}_{x_0}` を考える。

     .. math::
        :nowrap:

        \begin{align*}
        \mathcal{C}_{x_0} := \set{\fn{c_i}{(a_i,\ b_i)}M \sth c_i(t_i) = x_0}_{i \in I}
        \end{align*}

  #. 次にこの一点を含む座標近傍 :math:`(U, \varphi)` をとって、
     曲線族の曲線に次のような同値関係を入れる。

     .. math::
        :nowrap:

        \begin{align*}
        c_1 \sim c_2 \iff 
        \exists t_1 \in I_{c_1},\ t_2 \in I_{c_2}: \diff{(\varphi \circ c_1)}{t}(t_1) = \diff{(\varphi \circ c_2)}{t}(t_2)
        \end{align*}

* :math:`{\displaystyle \diff{d (\varphi \circ c_1)}{t}(t_1)}` 等は :math:`\RR^n` のベクトルであって
  点 :math:`\varphi(x_0) \in \varphi(U)` から「生えている」ようなイメージか？

* 別の近傍 :math:`(V, \psi)` をとって
  :math:`{\displaystyle \diff{(\psi \circ c_i)}{t}(t_i)}` を考えると
  「:math:`{\displaystyle \diff{(\varphi \circ c_i)}{t}(t_i)}` が同じであることと
  :math:`{\displaystyle \diff{(\psi \circ c_i)}{t}(t_i)}` が同じであること」となる。

  * それはなぜか。
    :math:`\psi \circ c_i = (\psi \circ \varphi\inv) \circ (\varphi \circ c_i)` であるので、
    chain rule によって適当な近傍において次のようになるから。

    .. math::
       :nowrap:

       \begin{equation*}
       \begin{split}
       \diff{(\psi \circ c_i)}{t}(t_i)
       & = D(\psi \circ \varphi\inv)_{\varphi(x_0)} \diff{(\varphi \circ c_i)}{t}(t_i) \quad \because \text{chain rule}\\
       & = D(\psi \circ \varphi\inv)_{\varphi(x_0)} \diff{d (\varphi \circ c_j)}{t}(t_j) \quad \because c_i \sim c_j \text{ for } (U, \varphi)\\
       & = \diff{(\psi \circ c_j)}{t}(t_j) \quad \because \text{chain rule}
       \end{split}
       \end{equation*}

  * 人のことは言えないが p. 74 の式変形は誤植か？

4.2 接ベクトル空間
----------------------------------------------------------------------
`接空間 or 接ベクトル空間 <http://mathworld.wolfram.com/TangentSpace.html>`__
  :math:`T_{x_0}M := \mathcal{C}_{x_0} / \sim` を接空間 or 接ベクトル空間と呼ぶ。

* 接ベクトル空間は実ベクトル空間である。
* 曲線族の曲線に :math:`\RR^n` の接ベクトルを対応させる写像は
  全単射 :math:`\fn{\varphi_{*}}{\mathcal{C}_{x_0}/\sim}\RR^n` を誘導する。
* 単射であることは同値類の定義から従う。
* 全射であることについて。これを示すのに面白い技法を使う。

  接ベクトル :math:`\bm{v} \in \RR^n` に対し
  :math:`c_\varphi ^\bm{v} (t) := \varphi \inv(t \bm{v} + \varphi (x_0))` というのを考える。
  ただし :math:`t \in (-\eps_{\varphi}^\bm{v},\ \eps_{\varphi}^\bm{v})` の範囲で
  :math:`t \bm{v} + \varphi (x_0) \in \varphi(U)` が成り立つように取る。
  こうすると次のようになるので全射であることが示せる（任意のベクトルについて曲線が作れるから）。

  .. math::
     :nowrap:

     \begin{equation*}
     \begin{split}
     \varphi_*(c_\varphi ^\bm{v})
         & = \diff{(\varphi \circ (\varphi \inv (t \bm{v} + \varphi (x_0))))}{t}(0) \\
         & = \diff{(t \bm{v} + \varphi (x_0))}{t}(0) \\
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
     \diff{(\psi \circ c_\varphi^{a_1 \bm{v_1} + a_2 \bm{v_2}})}{t}(0)
     &= D(\psi \circ \varphi\inv)_{\varphi(x_0)} \diff{(t(a_1 \bm{v_1} + a_2 \bm{v_2}) + \varphi(x_0))}{t}(0)\\
     &= D(\psi \circ \varphi\inv)_{\varphi(x_0)}(a_1 \bm{v_1} + a_2 \bm{v_2})\\
     &= a_1 D(\psi \circ \varphi\inv)_{\varphi(x_0)} \bm{v_1} + a_2 D(\psi \circ \varphi\inv)_{\varphi(x_0)} \bm{v_2}\\
     &= a_1 \diff{(\psi \circ c_\varphi^{\bm{v_1}})}{t}(0) + a_2 \diff{(\psi \circ c_\varphi^{\bm{v_2}})}{t}(0)
     \end{split}
     \end{equation*}

* 接ベクトル空間の基底は :math:`(c_{\varphi}^{\bm{e}_1}, \dotsc, c_{\varphi}^{\bm{e}_n})` である。

  * :math:`\varphi` に依存して決まることに気をつける。

* :math:`{ \displaystyle [c_{\varphi}^{\bm{e}_i}] := \frac{\partial}{\partial x_i}}` と記す。

  * 理由 1: 曲線は（偏）微分 or 方向微分を表しているとみなせるから。
  * 理由 2: 座標近傍を換えたときの基底変換が形式的にできるから。

    * 接ベクトルは :math:`{ \displaystyle \sum \diff{(x_i \circ c)}{t}(t_0) \frac{\partial}{\partial x_i} = \sum \diff{(y_i \circ c)}{t}(t_0) \frac{\partial}{\partial y_i} }`
    * 座標変換は :math:`\psi \circ \varphi\inv = (y_1(x_1, \dotsc, x_n), \dotsc, y_n(x_1, \dotsc, x_n))`
    * ヤコビ行列は :math:`{ \displaystyle \left( \frac{\partial y_i}{\partial x_j} \right) }`
    * 接ベクトルの変換は :math:`{ \displaystyle \frac{\partial}{\partial x_j}}` を
      :math:`{ \displaystyle \sum_{i = 1}^n \frac{\partial y_i}{\partial x_j} (\varphi(x_0)) \frac{\partial}{\partial y_i} }`
      で置き換える。

4.3 接写像
----------------------------------------------------------------------
`接写像 <http://mathworld.wolfram.com/TangentMap.html>`__
  :math:`F \in C^\infty(M, N),\ x \in M,\ \fnm{c}{(a, b)}{M}{t_0}x` を仮定する。
  点 :math:`F(x) \in N` を通る曲線 :math:`\fnm{F \circ c}{(a, b)}{N}{t_0}F(x)` という具合になる。
  接ベクトルを接ベクトルに対応させられる。
  このことから線形写像 :math:`\fn{F_*}{T_x}T_{f(x)}N` が定義できる。
  この写像 :math:`F_*` を接写像という。

  色々な性質をまとめておく：

  * :math:`F_*` は線形写像である。
    <多様体の間の写像の微分を接空間から接空間への線形写像として定義したもの> だ。
  * 実体は :math:`F_* = D(\psi \circ F \circ \varphi\inv)` である。
    ここで :math:`\varphi, \psi` は局所座標である。
  * 記号は他にも :math:`T_x F,\ D_x F,\ (dF)_x` などがある。
  * 接写像の記号の下付き米印は共変性 :math:`(f \circ g)_* = f_* \circ g_*` が成り立つことを示唆している。
  * :math:`\rank F_* = \rank D(\psi \circ F \circ \varphi \inv)_{(\varphi(x_0))}.`
  * :math:`\rank F_* = \dim N` ならば :math:`F_*` は
    :math:`x_0` の近傍で微分同相である（逆写像定理による）。

    * :math:`F_*` のランクが :math:`n = \dim M = \dim N` であったとしても
      :math:`M` と :math:`F(M)` が微分同相であるとは限らない。

* 例題 4.3.1: ただし :math:`M` のコンパクト集合 :math:`K` 上で :math:`F|K` が単射ならば、
  近傍 :math:`V` から :math:`F(V)` への微分同相となる。

  * :math:`\fn{F|U_x}{U_x}V_{F(x)}` が微分同相となるような近傍
    :math:`U_x \subset U_i` は存在する（∵逆写像定理）。
  * この近傍 :math:`U_x` はその閉包がコンパクトになるように取れる（らしい）。
  * :math:`K` の開被覆 :math:`\set{U_x}_{x \in K}` は
    有限開被覆 :math:`\set{U_{x_k}}_{k = 0,\dots\,k_0}` を持つ（∵コンパクト）。

  ここから先の減少列に関する議論がわからない。
  次のような :math:`\set{U_x^m}` があると言えるらしい。

  .. math::

     \begin{gather*}
     U_x \supset \closure{U_x^1} \supset U_x^1 \supset \closure{U_x^2} \supset U_x^2 \supset \dots,\\
     \bigcap_{m = 1}^\infty U_x^m = \set{ x }
     \end{gather*}

  * 各 :math:`\set{U_x^m}_{x \in K}` の有限部分？被覆
    :math:`\set{U_{x_k}^m}_{k = 1, \dots, k_0^m}` が得られる（∵コンパクト）。

  * :math:`W = \bigcup_k U_{x_k}^m` とおくと
    :math:`W_1 \supset \closure{W_2} \supset W_2 \supset \dots,\ \bigcap\closure{Q_m} = K` とできる。

  * するとある番号があって :math:`\fn{F}{W_m}F(W_m)` が単射となる（背理法と完備性を利用する）。

* 問題 4.3.2: 商空間 :math:`\RR^2/\ZZ^2`

  #. ハウスドルフであること

     * 次の性質を満たす連続関数をうまく見つける。
       理屈は前章で見たように「任意の二点を関数で分離したい」だ。
       :math:`\alpha, \beta\ (\alpha \ne \beta) \implies f(\alpha) \ne f(\beta).`

     * 解答例では :math:`f^{[x_0, y_0]}(x, y) = \cos 2\pi(x - x_0) + \cos 2\pi(y - y_0)` を採用している。

       * この関数 :math:`\fn{f}{\RR^2}\RR` は余弦関数の性質より :math:`[x_0, y_0]` の
         同値類のとり方によらず、また :math:`[x, y]` の同値類上で同じ値となるので、
         誘導される関数 :math:`\fn{\underline f}{\RR^2/\ZZ^2}\RR` も確定する。

       * よって :math:`[x_0, y_0] \ne [x, y]` ならば :math:`\underline f(x, y) \ne 2` であり、
         :math:`[x_0, y_0] = [x, y]` ならば :math:`\underline f(x, y) = 2` であるので、
         相異なる同値類を連続関数で分離できた。
         よってこの商空間はハウスドルフである。

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
     座標近傍系を :math:`\set{(p_x(B_x), s_x)}_{x \in \RR^2}` で定義する。

     * :math:`s_x` は連続である。
       なぜならば開集合 :math:`U \subset B_x` に対して
       :math:`\displaystyle p\inv(s_x\inv(U)) = \bigcup_{m, n \in \ZZ} (U + (m, n))` が開集合であるから。

     * :math:`s_x` は同相写像である。
       なぜならば :math:`s_x \circ (p_x|B_x) = \id_{B_x},\ (p_x|B_x) \circ s_x = \id_{p(B_x)}` だから。

     * 座標変換は :math:`C^\infty` 級である。
       なぜならば点 :math:`z \in p_x(B_x) \cap p_y(B_y)` に対して次を満たす整数の組が何かあるから：
       :math:`s_x(z) = s_y(z) + (m, n)`

     以上とハウスドルフ性により商空間は多様体であると結論できる。

  #. 行列 :math:`A \in M_2(\ZZ)` の定める :math:`\RR^2` 上の線形変換は
     :math:`\RR^2/\ZZ^2` 上の微分可能な変換 :math:`F_A` を定義する。

     * 同値な点が同値な点に写ることはすぐに示せる：
       :math:`A(\bm x + \bm n) = A\bm x + A\bm n \sim A\bm x.`

       よって写像 :math:`F_A` は well-defined である。

     * :math:`F_A` が :math:`C^\infty` 級であるといえる。
       なぜなら、商空間の座標近傍系を前項と同様に定義すると、写像
       :math:`s_{A(x)} \circ F_A \circ p_x` は点 :math:`x` の近傍で元の線形変換 :math:`A` と一致するので、

  #. :math:`\rank F_{A*} = \rank DF_A = \rank A`

     場合分けをするとこうなる：

     * :math:`\det A \ne 0` のときは :math:`\rank F_{A*} = \rank A = 2,`
     * :math:`\det A = 0` で

       * :math:`A \ne O` のときは :math:`\rank F_{A*} = \rank A = 1,`
       * :math:`A = O` のときは :math:`\rank F_{A*} = \rank A = 0.`

* 問題 4.3.3: `リー群 <http://mathworld.wolfram.com/LieGroup.html>`__

  #. :math:`L_g: h \longmapsto gh` は :math:`C^\infty` 級微分同相である。

     * これは微分同相の定義を確認するだけで済む。
       :math:`L_g \circ L_{g\inv} = L_{g\inv} \circ L_g = \id_G`

  #. 接写像 :math:`T_{(g, h)}(G \times G) \longto T_{gh}G` のランク。

     * 群の多様体次元と一致することを示すわけだが、ヒントから何をしていいかわからない。
     * 定数関数 :math:`G \owns c_g: g \longmapsto a \in \RR` を取る。
     * 次のような演算の列を考える。

       .. math::
          :nowrap:

          \begin{CD}
          G @>{c_g,\ L_h}>> G \times G @>{(op)}>> G @>{L_{(gh)\inv}}>> G\\
          @.     @.         @.     @.\\
          T_1 G @>{c_g,\ L_h}_{\ *}>> T_{(g, h)}(G \times G) @>{(op)_*}>> T_{gh}G @>{L_{(gh)\inv}}_{\ *}>> T_1 G
          \end{CD}

       左から右まででで恒等写像となり、接写像 :math:`L_{(gh)\inv*}` が全単射で、
       中央の写像が全射であることから、ランクが :math:`\dim G` と一致すると結論できる（らしい）。

  #. 逆元を取る演算は :math:`C^\infty` 級である。

     * 陰関数定理、逆元写像の接写像 :math:`T_(g, g\inv)(G \times G) \longto T_1 G` グラフ？

4.4 部分多様体
----------------------------------------------------------------------

* 定義 4.4.1: 部分多様体

  * 多様体 :math:`N` に対して :math:`M \subset N` に次の性質があるとき、
    それを p 次元部分多様体であるという。

    .. math::
       :nowrap:

       \begin{align*}
       \forall x_0 \in M, \exists(U, \varphi): M \cap U = \set{x \in U \sth x_{p + 1} = \dots = x_n = 0}
       \end{align*}

`微分可能構造 <http://mathworld.wolfram.com/SmoothStructure.html>`__
  座標近傍系の同値類について注意しておく。
  座標近傍系の両立という概念の上位互換な概念が微分可能構造だ。

:math:`\fn{F}{M}N,\ \rank F_* = \min{m = \dim M, n = \dim N}` とすると、

.. math::

   (y_i \circ F \circ \varphi\inv) =
   \begin{cases}
   x_i & \quad \text{if } m \le n \text{ and } i = 1, \dotsc, m\\
     0 & \quad \text{if } m \le n \text{ and } i = m + 1, \dotsc, n\\
   x_i & \quad \text{if } m \ge n \text{ and } i = 1, \dotsc, n.
   \end{cases}

最後のケースでは特に :math:`F\inv(F(x_0)) \cap U = \set{x \in U \sth x_{m + 1} = \dots = x_n = 0}` は
:math:`m - n` 次元部分多様体である。

`はめ込み <http://mathworld.wolfram.com/Immersion.html>`__
  :math:`m < n` のときに、
  写像 :math:`\fn{F}{M}N` に対し、:math:`\rank F_* = m` であればはめ込みであるという。

`埋め込み <http://mathworld.wolfram.com/Embedding.html>`__
  はめ込み :math:`F` によって :math:`N` の位相から誘導される位相が
  :math:`M` の位相そのものと一致するような
  :math:`F` は埋め込みであるという。

  * :math:`F(M)` は :math:`N` の正則な部分多様体となる。

* 定理 4.4.2: はめ込みが単射であれば、コンパクトな多様体の像は部分多様体となる。

`沈み込み <http://mathworld.wolfram.com/Submersion.html>`__
  :math:`m \ge n` の場合に
  任意の :math:`x \in M` に対して :math:`\rank F_* = n` となるとき、
  この写像は沈み込みであるという。

  * :math:`F\inv(y)` は :math:`m - n` 次元部分多様体となる。
  * この特殊な状況を例題 8.6.1 ファイブレーション定理で取り扱う。

* 例題 4.4.3: 部分多様体間の :math:`C^\infty` 級写像が誘導する写像も :math:`C^\infty` 級となる。

  * 仮定をまとめる：

    * :math:`N_1, N_2` をそれぞれ :math:`n_1, n_2` 次元多様体とし、
    * :math:`C^\infty` 級写像 :math:`\fn{F}{N_1}N_2` があり、
    * :math:`M_1 \subset N_1,\ M_2 \subset N_2` はそれぞれ部分多様体であり、
    * さらに :math:`F(M_1) \subset M_2` が成り立つとする。

  * :math:`M_2 \subset N_2` が部分多様体であるので、
    次のような :math:`F(x_0) \in M_2 \subset N_2` の座標近傍 :math:`(V, \varphi),\ \varphi = (y_1, \dotsc, y_{n_2})` がある：
    :math:`M_2 \cap V = \set{y_{{m_2} + 1}, \dotsc, y_{n_2} = 0}.`

  * 残りの座標成分のほうを考えと
    :math:`(y_1, \dotsc, y_{m_2}) \circ F \circ \varphi\inv` が :math:`C^\infty` 級となる。
    したがって 誘導される写像 :math:`\fn{G}{M_1}M_2` も :math:`C^\infty` 級となる。

* 問題 4.4.4: :math:`GL_2(\RR)` と :math:`SL_n(\RR)`

  * 前者は :math:`n^2` 次元多様体、後者は :math:`n^2 - 1` 次元部分多様体である。

    * 大前提として :math:`M_n(\RR)` は座標近傍系を空間全体を近傍とし、
      各成分の値をそのまま座標とする座標近傍一つからなるものを考えれば、
      これは :math:`n^2` 次元多様体である。

    * GL については :math:`GL_n(\RR) = \set{A \in M_n(\RR) \sth \det A \ne 0}` である。
      連続写像 :math:`\fn{\det}{M_n(\RR)}\RR` の開集合 :math:`\set{x \in \RR \sth x \ne 0}` の
      逆像とみなすことで開集合となり、先ほどと同じ要領で座標近傍系を構成すれば
      :math:`n^2` 次元多様体である。

    * SL について。まず定義を書き下してみると :math:`SL_n(\RR) = \set{A \in GL_n(\RR) \sth \det A = 1}` だ。
      今度は :math:`\det\inv(1)` である。

      * :math:`\det` のヤコビ行列なるものを考える。余因子展開を意識することで
        :math:`\det(x_{ij}) = \sum x_{ij} A_{ij}` のように書かれるから、
        :math:`\displaystyle \frac{\partial \det}{\partial x_{ij}} = A_{ij}` で、
        右辺は :math:`(n - 1)^2` 次正方行列の行列式になっている。

      * SL では :math:`D\det \ne 0` であることに注意。
        :math:`\det` は :math:`n^2` 次元から :math:`1` 次元への関数であり、
        陰関数定理により、ある近傍 :math:`W` と :math:`C^\infty` 級写像（座標になる）
        :math:`\fn{\varphi}{W}\RR^{n^2 - 1}` が存在する。

  * 行列の積、逆行列を取る演算はどちらも :math:`C^\infty` 級の写像である。

    * 両者ともリー群なので問題 4.3.3 を利用できる。
    * 積も逆行列も多項式の演算に、せいぜい非ゼロの値の除算が加わるものなので
      :math:`C^\infty` 級の写像だという主張には問題あるまい。

* 問題 4.4.5: 直交群 :math:`O(n)` は多様体である。

  * 写像 :math:`C: A \longmapsto {}^t\!AA` を考える。

    * 直交群は :math:`C\inv(I_n)` となる。
    * :math:`C` は :math:`C^\infty` 級である。

  * 微分を考える。ここが少し思いつかない。

    * まずは :math:`C(A + X) - C(A) = {}^t\!XA + {}^t\!AX + {}^t\!XX.`
      これの極限 :math:`X \to O` が :math:`DC_{(A)}X` である。

    * :math:`DC_{(A)}X = {}^t\!XA + {}^t\!AX` という形をよく見ると二つの写像
      :math:`X \longmapsto {}^AX` と :math:`X \longmapsto {}^t\!X + X` の合成であることに気付く。

      * :math:`\rank(X \longmapsto {}^AX) = n^2` である。
      * :math:`\displaystyle \rank({}^t\!X + X) = \frac{n(n + 1)}{2})` である。

      以上より合成写像のランクは :math:`\displaystyle \frac{n(n + 1)}{2}` である。

  * よって陰関数定理により、:math:`C\inv(I_n) = O(n)` の
    近傍 :math:`W` と :math:`C^\infty` 級写像 :math:`W \longto \RR^\frac{n(n - 1)}{2}` が存在する。

    * 写像 :math:`\fn{C}{M_n(\RR)}M_n(\RR)` は :math:`n^2` 次元空間から
      :math:`\displaystyle \frac{n(n + 1)}{2}` 次元空間へのものだとわかったことによる。

* 例題 4.4.7: 横断的に交わる二つの部分多様体の共通部もまた部分多様体である。

  * :math:`\forall x \in X \cap Z, T_x Y + T_x Z = T_x X` が仮定、
    :math:`Y \cap Z \subset X` が部分多様体であることが結論。

  以下、ノートの都合上 :math:`a = \dim X - \dim Y,\ b = \dim X - \dim Z` と書く。

  * :math:`x_0 \in Y \cap Z` の座標近傍を :math:`(U, \varphi)` とする。
  * まず次のような写像 :math:`\fn{F_Y}{U}\RR^a` が存在する：
    :math:`U \cap Y = F_Y\inv(F_Y(x_0)).`
  * さらに :math:`\forall x \in U, \rank F_{Y*} = a\quad(\fn{F_{Y*}}{T_xX}\RR^a.)`
  * 同様な性質の :math:`F_Z` も存在する。

  * 写像の直積を構成することで :math:`F_{Y*}, F_{Z*}` を適当に制限すると同型写像が得られることを示す：

    .. math::

       \fn{(F_{Y*}, F_{Z*})}{U}\RR^a \times \RR^b.

    * 接空間を :math:`T_xY = (T_xY \cap T_xZ) \oplus V_Y` のように部分空間の直和に分解する。
      このとき :math:`F_{Y*}|V_Y \cong \RR^a` となる。
      :math:`T_xZ` についても同様に :math:`V_Z` を定義する。

    * :math:`(F_{Y*}, F_{Z*})|(V_Y \oplus V_Z) \cong \RR^a \oplus \RR^b.`
      :math:`\rank(F_{Y*}, F_{Z*}) = a + b = 2\dim X - \dim Y - \dim Z.` が得られた。

  * :math:`U \cap (Y \cup Z) = (F_Y, F_Z)\inv(F_Y(x_0), F_Z(x_0))` において、
    :math:`X` 内で :math:`U` を動かすことによって
    :math:`Y \cap Z` が :math:`\dim X - (2\dim X - \dim Y - \dim Z) = \dim Y + \dim Z - \dim X` 次元の部分多様体であることがわかる。

4.5 接束（展開）
----------------------------------------------------------------------
冒頭のユークリッド空間内の多様体から多様体と接空間のペアの空間を構成する部分は前座。

`接束 <http://mathworld.wolfram.com/TangentBundle.html>`__
  前章の記号 :math:`V_i, V_{ij}, \gamma_{ij}` 等を流用する。
  次のようにして構成する商空間を多様体の接束という：

  #. 直和 :math:`\bigsqcup V_i` に同値関係 :math:`x_i \sim x_j \iff x_i = \gamma_{ij}(x_j)` を導入する。
     このとき、商空間 :math:`X = (\bigsqcup V_i / \sim)` は :math:`M` と微分同相になる（例題 3.5.2 などを参照）。

  #. 直積の直和 :math:`\bigsqcup (V_i \times \RR^n)` に次の同値関係を導入する。

     .. math::
        :nowrap:

        \begin{align*}
        (x_i, v_i) \sim (x_j, v_j) \iff \exists \gamma_{ij}:
        x_i = \gamma_{ij}(x_j),\ v_i = (D\gamma_{ij})_{(x_j)} v_j
        \end{align*}

     同値関係となる理由：

     * 写像 :math:`G_{ij}: (x_i, v_i) \longmapsto (\gamma_{ij}(xj), (D\gamma_{ij})_{(x_j)} v_j)` を考える。
       これは微分同相となる。
     * そして :math:`G_{ij} \circ G_{jk} = G_{ik}` （ただし :math:`G_{ii} = \id` と約束する）が成り立つ。

     このとき、商空間 :math:`Y = (\bigsqcup (V_i \times \RR^n))/\sim` はハウスドルフとなり、
     :math:`2n` 次元多様体となる。

     ハウスドルフとなる理由（面倒）：

     * 射影をいくつか定義して、その合成写像による商空間の開集合の逆像もまた開集合であることを示し、
       :math:`Y \longto X` に連続写像が存在することを示せる。
     * 次に、直和から商空間への射影二種 :math:`p_x, p_y` を適宜制限して同相写像を得る。
     * 写像 :math:`\fn{P\inv}{p_x(V_i)}p_x(V_i) \times \RR^n` が同相であることを示す。
     * 最後に問題 3.5.3 を利用する。

  接束は `ベクトル束 <http://mathworld.wolfram.com/VectorBundle.html>`__ の一種である (pp. 85-86)。

* 問題 4.5.2: :math:`F \in C^\infty(M, N)` の引き起こす接束の間の写像
  :math:`\fn{F_*}{TM}TN` は :math:`C^\infty` 級である。

  * :math:`TM` は :math:`\bigcup \varphi_i(U_i) \times \RR^m` の商空間である。
  * :math:`TM` の座標近傍系は :math:`\varphi_i(U_i) \times \RR^m` の像および
    そこからの逆写像として定義される。
  * 以上、:math:`TN` も同様。
  * それゆえ、次の写像は :math:`F` が :math:`C^\infty` 級であれば
    :math:`C^\infty` 級となる：

    .. math::

       (\bm u_i, \bm v_i) \longmapsto ((\psi \circ F \circ \varphi_i\inv)(\bm u_i),
                                      D(\psi \circ F \circ \varphi_i\inv)_{(\bm u_i)}(\bm v_i)).

* 問題 4.5.3: ユークリッド空間内の多様体 :math:`M \subset \RR^N` に対して
  :math:`TM` と :math:`X = \set{(x, v) \sth x \in M, v \in T_x M}` は微分同相である。

  * 点 :math:`\bm x^0 \in M` の近傍におけるグラフ表示から :math:`X` のグラフ表示を構成する。

    .. math::

       \bm x^0 = (\bm x_1^0, \bm x_2^0) \in \RR^p \times \RR^{N - p},

    :math:`\bm x_1^0 \in W` 上のグラフ表示 :math:`\fn{g}{W}\RR^{N - p},\ M \cap U = \set{(\bm x_1, g(\bm x_1)) \sth \bm x_1 \in W}`
    とすると :math:`\bm v \in T_{(\bm x_1, g(\bm x_1))}M \iff \bm v = (\bm v_1, Dg_{(\bm x_1)}\bm v_1)).`

    :math:`X \cap (U \times \RR^N) = \set{(\bm x_1, g(\bm x_1)), (\bm v_1, Dg_{(\bm x_1)}\bm v_1)) \sth (\bm u_1, \bm v_1) \in W \times \RR^p}.`

  * :math:`TM` は :math:`M` のパラメーター表示による被覆 :math:`\set{\Phi_i(W_i)}` について
    商空間 :math:`\bigcup W_i \times \RR^p` として定義されている。

  * 写像 :math:`(\bm u, \bm v) \longmapsto (\Phi_i(\bm u), {D\Phi_i}_{(\bm u)}(\bm v))` は連続であり、
    :math:`TM` の定義から逆写像もまた連続、:math:`C^\infty` 級である。

----

:doc:`note5` へ。
