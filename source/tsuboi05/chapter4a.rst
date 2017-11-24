======================================================================
第 4 章 接空間（前編）
======================================================================
:math:`\require{AMScd}`

本章の目的は次のとおり：

* 接ベクトル、接空間を考察する。
* 接写像を定義する。
* 多様体間の写像についても逆写像・陰関数定理が応用可能であることを見る。

.. contents:: ノート目次

4.1 曲線の接ベクトル
======================================================================
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
    :ref:`chain rule <tsuboi05.1.2.8>` によって適当な近傍において次のようになるから。

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
======================================================================
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
======================================================================
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

.. _tsuboi05.4.3.1:

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

.. _tsuboi05.4.3.3:

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
