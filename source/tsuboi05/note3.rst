======================================================================
幾何学 I 多様体入門 読書ノート 3/8
======================================================================
:math:`\require{AMScd}`
:doc:`note2` からの続き。

.. contents:: ノート目次

第 3 章 多様体の定義
======================================================================
多様体はユークリッド空間内になくてもよさそうだという考えが
微分可能多様体の概念が生まれるきっかけとなった。

3.1 微分可能多様体の定義
----------------------------------------------------------------------

.. _tsuboi05.3.1.1:

* 定義 3.1.1: n 次元 `（微分可能）多様体 <http://mathworld.wolfram.com/SmoothManifold.html>`__

  * 以降、単に「多様体」と書くときは「微分可能多様体」を意味するものとする。

  * :math:`C^\infty` 級多様体の定義は、前章までに見てきた位相多様体や
    :math:`C^r` 級多様体の上位？概念のように捉えられる。

  * `局所座標 or 座標近傍 <http://mathworld.wolfram.com/CoordinateChart.html>`__
  * `局所座標系 or 座標近傍系 <http://mathworld.wolfram.com/Atlas.html>`__
  * `座標変換 <http://mathworld.wolfram.com/TransitionFunction.html>`__

.. _tsuboi05.3.1.3:

* 注意 3.1.3: `パラコンパクト <http://mathworld.wolfram.com/ParacompactSpace.html>`__

  * 本書でこれ以降扱う多様体はパラコンパクト性（と同値な性質）があるものとする。
  * 特に `第 2 可算 <http://mathworld.wolfram.com/SecondCountableTopology.html>`__ 公理を満たす。

* 例 3.1.5: 2 次曲面

  .. math::

     Q = \Set{(X_1, \dotsc, X_n) \in \RR^n \Sth \sum_{i = 1}^n \lambda_i X_i^2 = b\quad(\ne 0)}

  * 座標近傍系を定義することで、曲面が多様体であることを示す。
  * :math:`U_i^+ := Q \cap \set{X_i > 0}, \varphi_i^+(X_1, \dotsc, X_n) = (X_1, \dotsc, \widehat{(i)}, \dotsc, X_n)` などと置く
    （ハットの部分は除去を意味する）。

  * 開集合 :math:`U_i^\pm` をすべて合併させると曲面全体を覆う。
  * 写像 :math:`\fn{\varphi_i^\pm}{Q}\RR^{n - 1}` はちょっとした計算により同相写像であることを示せる。
  * 座標変換 :math:`\varphi_i^\sigma \circ (\varphi_j^\tau)\inv` が :math:`C^\infty` 級であることも同様にして示せる。

* 例 3.1.6: 多様体の直積、直和はどちらも多様体

  次のようにして位相が定まる：

  * 直積の位相: :math:`U_1 \times U_2` の任意個の和集合を開集合とする。
  * 直和の位相: :math:`U_1 \sqcup U_2` を開集合とする。

3.2 商空間（基礎）
----------------------------------------------------------------------
* 確認: 商空間 :math:`X/\sim` の位相の入れ方、誘導される写像。

* 例 3.2.1: n + 1 次元空間内の「球面」

  :math:`S^n` の `対蹠点 <http://mathworld.wolfram.com/AntipodalPoints.html>`__
  を同一視することで構成される射影空間 :math:`\RR P^n` は多様体となる。

  * 前半は「球面」が多様体であることを示す。

    * 局所座標系 :math:`\set{(U_i^\pm, \varphi_i^\pm)}` を次のように定義する。

      .. math::
         :nowrap:

         \begin{align*}
         U_i^\pm & = \set{(x_0, \dotsc, x_n) \in S^n \sth \pm x_i > 0},\\
         \varphi_i^\pm (x_0, \dotsc, x_n) & =
         \left(
         \frac{x_0}{x_i}, \dotsc, \widehat{(i)}, \dotsc, \frac{x_n}{x_i}
         \right)
         \end{align*}

    * 各 :math:`\varphi_i^\pm` は対応する :math:`U_i^\pm` 上で連続となり、
      逆写像もまた連続となる。これで同相写像であることは言える。

    * 次に座標変換 :math:`\varphi_j^+(U_i^- \cap U_j^+) \longto \varphi_i^-(U_i^- \cap U_j^+)` などを計算して、
      これらがすべて滑らかであることを示す。

  * 後半は射影空間が多様体であることを示す。

    * 射影 :math:`\fnm{p}{S^n}{\RR P^n}{[x]}\set{x, -x}` は同値類への写像となる。
    * 局所座標系 :math:`\set{(V_i, \varphi_i)}` を次のように定義する。

      .. math::
         :nowrap:

         \begin{align*}
         V_i & = \set{[\bm{x}] \in \RR P^n \sth x_i \ne 0},\\
         \varphi_i([\bm{x}]) &= \varphi_i^\pm(\bm{x})
         \end{align*}

    * このとき、写像 :math:`\varphi_i` は well-defined かつ連続写像かつ逆写像が存在する。
    * 逆写像 :math:`\varphi_i\inv` は :math:`p \circ (\varphi_i^+)\inv = p \circ (\varphi_i^-)\inv` となって連続である。
      図を入れたい。

    * 次に座標変換が滑らかであることを示す。
      これは :math:`\varphi_i \circ \varphi_j\inv` が「球面」のときと同じ式で定義されることから言える。

    * 射影空間がハウスドルフであることを示す。
      「球面」がハウスドルフであることと :math:`[\bm{x^1}] \ne [\bm{x^2}] \implies \bm{x^1} \ne \pm \bm{x^2}` であることから地道に示す。

3.3 変換群
----------------------------------------------------------------------
* 用語確認

  * 位相空間の変換群：
    同相写像の場合、写像の合成と逆写像をとる操作で閉じている。
  * `作用 <http://mathworld.wolfram.com/Action.html>`__ する

* 定理 3.3.1: 位相空間の有限変換群による商空間はハウスドルフ空間となる。

  * 元の位相空間自身はハウスドルフ空間である必要はない。

  :math:`[x] \ne [y]` となる :math:`x, y \in X` をとる。
  変換群を :math:`F = \set{f_i}_{i = 1, \dots, n},\ f_1 = \id` とおく。

  #. まず各 :math:`i` に対して次が成り立つ開集合 :math:`U_i, V_i \subset X` があることに注意：

     .. math::

        x \in U_i, f_i(y) \in V_i, U_i \cap V_i = \varnothing.

     これは背理法で示せるのだが、簡単なためか紙幅の都合上か本書では触れていない。

  #. 次に :math:`\displaystyle U = \bigcap_{i = 1}^n U_i,\ V = \bigcap_{i = 1}^n f_i\inv(V_i)` とおく。
     このとき次が成り立つ：

     * :math:`x \in U,\ y \in V.`
     * :math:`f_i(U) \cap f_j(V) = \varnothing \text{ for } i, j = 1, \dots, n.`

     二番目の等式は :math:`f_i\inv \circ = f_j = f_k` と表すと、次のようにしてわかる：

     .. math::

        \begin{align*}
        f_i\inv(f_i(U) \cap f_j(V))
        &= U \cap (f_i\inv \circ f_j)(V)\\
        &= U \cap f_k(V)\\
        &\subset U_k \cap U_k
        = \varnothing.
        \end{align*}

  #. このとき射影 :math:`\fn{p}{X}X/F` に対して :math:`[x] \in p(U),\ [y] \in p(V)` である。

     * 例えば :math:`\displaystyle p\inv(p(U)) = \bigcup_{i = 1}^n f_i(U)` であるから
       （もっと丁寧に説明したい）
       :math:`[x] \in p(U)` と言える。
       :math:`[y] \in p(V)` についても同じ。

  #. 最後に :math:`p\inv(p(U) \cap p(V)) = \varnothing` を示して、
     :math:`P(U)` と :math:`P(V)` が先の同値類を分離する開集合であることを示す。
     射影が連続写像なのでこういう等式変形となる：

     .. math::

        \begin{align*}
        p\inv(p(U) \cap p(V)) &= p\inv(p(U)) \cap p\inv(p(V))\\
        &= \left(\bigcup_{i = 1}^n f_i(U)\right) \cap \left(\bigcup_{i = 1}^n f_i(V)\right)\\
        &= \varnothing \quad(\because f_i(U) \cap f_j(V).)
        \end{align*}

この節は例題と問題が多い。どれも大切。
ハウスドルフ空間であることを示すために、二点が「関数で分離される」ことを示す必要がある場合のコツなど。

* 例題 3.3.2: 平面から原点を取り除いた空間において、
  水平な（半）直線に属する点同士を同値類とする商空間は多様体とはならない。

  * 考察対象の空間

    * :math:`Z = \RR^2 \minuszero`,
    * :math:`Y = Z / \sim`

  * 考察する写像

    * :math:`\fnm{p}{Z}{\RR}{(x, y)}y`
    * :math:`\fnm{\underline{p}}{Y}{\RR}{[x, y]}y`
    * :math:`\fnm{f^\pm}{\RR}{Z}{y}(\pm 1, y)`
    * :math:`\fn{p_Y}{Z}Y` （射影）

  * 合成写像 :math:`p_Y \circ f_\pm` を考える。
    :math:`Y_\pm := (p_Y \circ f_\pm)(\RR)` とおくと、
    :math:`\underline{p}` との絡みで :math:`Y_\pm` と実数全体が同相であることを示せる。
    商空間の任意の点について、それを含む開近傍が
    :math:`Y_+` か :math:`Y_-` にあると結論できる。

    .. math::
       :nowrap:

       \begin{align*}
       \begin{CD}
       \RR @>{f^\pm}>> Z @>{p_Y}>> Y_\pm \subset Y\\
       @.        @V{p}VV   @V{\underline{p}}VV\\
       @.             \RR @. \RR
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
     \RR @>{g_\pm,\ h_\pm}>> Z @>{p_X}>> X_\pm^g, X_\pm^h = X\\
     @.        @V{p}VV   @V{\underline{p}}VV\\
     @.             \RR @. \RR
     \end{CD}

  * 商空間の任意の点に対して、それを含む開近傍が存在して、ある開区間と同相とはなるものの、
  * 商空間はハウスドルフではない。
  * この問題は、考える写像がけっこうあるので図式をスケッチしながら解く。

* 問題 3.3.4: 平面から原点を除いた部分を図形で埋め尽くして
  同値類のなす商空間が多様体にならないパターンの問題。

  * 行列 :math:`A = \displaystyle \begin{pmatrix} a & 0 \\ 0 & \dfrac{1}{a} \end{pmatrix}\ (a > 1)` をとり、
    元の空間における同値関係を :math:`z_1 \sim z_2 \iff \exists n \in \ZZ: A^n z_1 = z_2` で定義する。

    * 同値関係であることを確認するのは簡単なので紙幅を割いていない。

  * 対象となる空間は :math:`Z = \RR^2 \minuszero,\ S = Z / \sim`
  * 前半は、:math:`S` の各点に :math:`\RR^2` と同相な近傍があることを示す。

    * 点 :math:`(x, y) \in Z` に対して

      * :math:`x \ne 0` ならば開区間 :math:`\displaystyle I = \left(\frac{1}{\sqrt{a}}x, \sqrt{a}x \right)` を導入して :math:`I \times \RR` を、
      * :math:`y \ne 0` ならば開区間 :math:`\displaystyle I = \left(\frac{1}{\sqrt{a}}y, \sqrt{a}y \right)` を導入して :math:`\RR \times I` をそれぞれ考える。

      このような直積を対応する点を含む :math:`Z` の開集合とする。
      以下、しばらくは :math:`x \ne 0` で話をすすめる。

    * 写像 :math:`\fn{p_s}{Z}S` を射影とする。
    * 写像 :math:`\fn{i}{I \times \RR}Z` を包含写像とする。
    * 写像 :math:`\fn{s: W }{= (p_s \circ i)(I \times \RR) } I \times \RR` を代表元を取る写像とする。

      .. math::
         :nowrap:

         \begin{CD}
         I \times \RR @>{i}>> Z @>{p_s}>> W \subset S @>{s}>> I \times \RR
         \end{CD}

      次の点を確認する必要がある：

      #. :math:`s` は well-defined である

         これは :math:`I \times \RR` と各同値類の交点が高々一点であることから成り立つ。
         どう確かめるのがいいのか。

      #. :math:`s` は連続写像である

         開集合 :math:`U \subset I \times RR` をとると :math:`s\inv(U)` が開集合であればよい。
         :math:`p\inv\circ s\inv(U)` が開集合であることを示すのがよい。
         :math:`\displaystyle \bigcup_{n \in \ZZ}A^n(U)` の代表元がどうなるかを考える。

      #. :math:`s` は同相写像である

         すなわち :math:`W \cong I \times \RR` を示す。
         :math:`s \circ (p_s \circ i) = \id_{I \times \RR}` と
         :math:`(p_s \circ i) \circ s = \id_W` であると言う。

      :math:`W \cong I \times \RR \implies I \times \RR \cong \RR^2\ ([x] \in W)` を示す。

  * 後半のハウスドルフではないことの証明は、
    :math:`[1, 0]` の近傍と :math:`[0, 1]` の近傍がどうしても共通部分があることを示すことにする。

* 例題 3.3.5: :math:`\RR/\ZZ \cong S^1` は多様体になる。

  * 同値関係 :math:`x_1 \sim x_2 \iff x_1 - x_2 \in \ZZ` で商空間 :math:`\RR/\sim` を定義する。
  * 射影を :math:`p` とする。

    * ある閉集合の像 :math:`p(\set{0 \le x \le 1})` が空間全体となるゆえ、商空間はコンパクトであるといえる。

  * 座標近傍系を次のように構成する。

    * 同値類 :math:`[x]` に対して開区間 :math:`I_x := (x - 1/4, x + 1/4) \subset \RR` を定義する。
    * 同値類からその代表元を :math:`I_x` の中にあるように取る（？）写像を :math:`s_x` を定義する。

      * :math:`s_x` は連続となる。なぜなら開集合 :math:`U \subset I_x` に対して
        :math:`{ \displaystyle p\inv(s_x\inv(U)) = \bigcup_{n \in \ZZ}\set{x + n \sth x \in U} }` は開集合だから。

      * :math:`s_x` は同相となる。なぜなら
        :math:`(p|I_x) \circ s_x = \id,\quad s_x \circ (p|I_x) = \id` であるから。

    * :math:`\set{(p(I_x), s_x)}_{x \in \RR}` が構成できた。

  * これがハウスドルフであることを直接示すのは面倒。

  * 円周 :math:`S^1` と同相となることを示せる。

    * 実数から円周への写像 :math:`h: x \longmapsto (\cos 2\pi x, \sin 2 \pi x)` を定義する。
    * 誘導される写像 :math:`\underline{h} = h \circ p\inv` が定義でき、
      これが全射であるだけでなく、単射であることを示せば、同相であると結論できる。

* 例題 3.3.6: :math:`\RR P^n = S^n / \set{\pm 1} = (\RR^{n + 1} \minuszero) / \RR^\times`

  * 次のような写像 :math:`\fn{f}{\RR^{n + 1} \minuszero}\RR` をまず定義し、
    これが well-defined であることを確認する。

    .. math::
       :nowrap:

       \begin{align*}
       f(\bm{x_2}) = \frac{\abs{\bm{x_1} \cdot \bm{x_2}}}{\norm{\bm{x_1}} \norm{\bm{x_2}}}.
       \end{align*}

  * 次に誘導される写像 :math:`\underline{f}` が連続であることを示し、
    コーシー・シュワルツの不等式の等式成立条件などからハウスドルフであることを示す。

  * 多様体であることを示すために、局所座標系 :math:`\set{(V_i, \varphi_i)}` を定義する。

    .. math::
       :nowrap:

       \begin{align*}
       V_i & = \set{[\bm{x}] \in \RR^{n + 1} \zeroset \sth x_i \ne 0},\\
       \varphi_i([\bm{x}]) &= \left( \frac{x_0}{x_i}, \dotsc, \widehat{(i)}, \dotsc, \frac{x_n}{x_i} \right)
       \end{align*}

    * TODO: ここに包含写像を説明する可換図式みたいなものを挿れたい。

  * 座標変換が滑らかであることを示す。
  * 射影空間では超平面とそれに含まれない直線とは必ず一点で交わる。

* 問題 3.3.7: :math:`\CC P^n`

  #. :math:`\CC P^n` はハウスドルフである

     * 例題 3.3.6 と同様の実数値関数 :math:`\fn{f}{(\CC^{n + 1})^\times}\RR` を定義する。
     * 同様の理由により、:math:`f` は :math:`\bm z_1` の取り方によらず値が確定する。
       また、誘導される関数 :math:`\fn{\underline f}{(\CC^{n + 1})^\times/\sim = \CC P^n} \RR` も
       同様の理由により連続関数として確定する。
     * 再びコーシー・シュワルツの不等式より :math:`\underline f \le 1.`
       等号成立条件は :math:`\exists \lambda \in \CC^\times \text{ s.t. } \bm z_1 = \lambda \bm z_2.`
       これは :math:`[\bm z_1] = [\bm z_2]` を意味する。
       ゆえに :math:`[\bm z_1] \ne [\bm z_2] \iff \underline f([\bm z_1]) \ne \underline f([\bm z_2]).`
     * 相異なる二点を連続関数で分離されることを示せたので、
       この空間はハウスドルフである。

  #. :math:`\CC P^n` は実 :math:`2n` 次元多様体である

     * 座標近傍系を次のように定義する：

       .. math::

          \begin{align*}
          V_i &= \set{[\bm z] \in (\CC^{n + 1})^\times/\sim \sth z_i \ne 0},\\
          \varphi_i([\bm z]) &= \left(\frac{x_0}{x_i}, \dotsc, \widehat{(i)}, \dotsc, \frac{x_n}{x_i}\right).
          \end{align*}

       次の性質がある：

       * 各座標 :math:`\varphi_i` は :math:`V_i` 上の連続関数である（分母はゼロでないから）。
       * 各座標 :math:`\varphi_i` は同相写像である。

         これを示すには :math:`\fn{\iota_i}{\CC^n}\CC^{n + 1}` を次のように定め、
         これまでの問題にあるように射影 :math:`p` と合成して
         :math:`\varphi_i \circ (p \circ \iota_i) = \id_{\CC^n}` かつ
         :math:`(p \circ \iota_i) \circ \varphi_i = \id_{V_i}` であるから同相となると言う：

         .. math::

            \iota_i: (z_0, \dotsc, z_{i - 1}, z_{i + 1}, \dotsc, z_n) \longmapsto
            (z_0, \dotsc, z_{i - 1}, 1, z_{i + 1}, \dotsc, z_n)

     * 座標変換 :math:`\varphi_i \circ \varphi_j\inv` を確かめる。
       :math:`i > j` とすると、この変換は次のようなものとなり、
       複素数では :math:`n` 個の、実数では :math:`2n` 個の座標成分があるとみなせる。

       .. math::

          (z_0, \dotsc, z_{j - 1}, z_{j + 1}, \dotsc, z_n) \longmapsto
          \left(\frac{z_0}{z_i},
          \dotsc, \frac{z_{i - 1}}{z_i}, \frac{z_{i + 1}}{z_i},
          \dotsc, \frac{z_{j - 1}}{z_i}, \frac{1}{z_i}, \frac{z_{j + 1}}{z_i},
          \dotsc, \frac{z_n}{z_i}
          \right).

     * 座標変換が :math:`C^\infty` 級であり、
       :math:`\CC P^n` はハウスドルフであるので、多様体である。

3.4 :math:`C^r` 級多様体の間の :math:`C^s` 級写像、微分同相写像
----------------------------------------------------------------------
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

    * 問題 3.3.7 の記号で言うと :math:`\fn{\varphi_i}{V_i}\CC,\ z \in \CC^\times, \varphi_1 \circ \varphi_0\inv(z) = \dfrac{1}{z}.`
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

* 定理 3.4.8: 滑らかな多様体の滑らかな有限変換群に対する商空間は、滑らかな多様体となる。

  * これは定理 3.3.1 の上位互換版のような定理だ。実際、証明にそれを利用している。

* 例題 3.4.9: `レンズ空間 <http://mathworld.wolfram.com/LensSpace.html>`__

  :math:`S^3 := \set{(z_1, z_2) \in \CC^2 \sth \abs{z_1} ^2 + \abs{z_2} ^2 = 1}`

  * 有限変換群 :math:`F` の元は互いに素な自然数の組 :math:`p, q` を用いて構成できる。
    LaTeX を書くと字が潰れるので省略。

  * この有限群は位数 :math:`p` の巡回群 :math:`\ZZ/p\ZZ` になり、
    :math:`S^3` へ作用する。定理 3.4.8 により :math:`S^3/F` は多様体となる。

    * これを :math:`L_{p, q}` と表す。ちなみに :math:`L_{2, 1}` は
      :math:`\RR P^3` と微分同相となる。

3.5 座標変換
----------------------------------------------------------------------
* <多様体の定義において最も重要なものは、座標近傍系である> (p. 61)
* 座標変換から多様体を構成する手法がファイバー束、ベクトル束の全空間を
  多様体と考えるときに必要となる。

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

* 例題 3.5.2: 例題 3.5.1 の記号の一部を流用し、開集合の直和に同値関係を入れて商空間を定義する。

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
     例題 3.5.1 の記号を流用すると、

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

* 問題 3.5.3: ファイバー束

  * :math:`E, B` は位相空間であり、
  * 写像 :math:`\fn{p}{E}B` は連続であり、
  * 次を満たす位相空間 :math:`F` が存在するとする：

    .. math::

       \forall b \in B, \exists U_b \owns b
       \text{ s.t. }
       \exists \fn{h}{p\inv(U_b)}U_b \times F,\ \operatorname{pr}_1 \circ h = p.

    ただし :math:`h` は同相写像であり、
    :math:`\operatorname{pr}_1` は直積 :math:`U_b \times F` の第一成分への射影とする。

  このとき :math:`B, F` がハウスドルフならば :math:`E` もそうである。

  .. math::
     :nowrap:

     \begin{CD}
     E @>{p}>> B\\
     @A{\subset}AA @A{\subset}AA\\
     p\inv(U_b) @>{p}>> U_b\\
     @V{h}VV @A{\operatorname{pr}_1}AA\\
     U_b \times F
     \end{CD}

  * この状況における位相空間 :math:`E` をファイバー束といい、
    位相空間 :math:`F` を :math:`B` 上のファイバーという。

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

  後ほど例題 8.6.1 で同じ状況が現れる。

3.6 向き付け（展開）
----------------------------------------------------------------------
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
----------------------------------------------------------------------
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
          \diff{\rho(x)}{x} &= \frac{\mathrm e^{- \frac{1}{x}}}{x^{2}} & \quad \to 0 \quad(x \to +0)\\
          \mdiff{\rho(x)}{2}{x} &= \frac{\mathrm e^{- \frac{1}{x}}}{x^{3}} \left(-2 + \frac{1}{x}\right) & \quad \to 0 \quad(x \to +0)\\
          \mdiff{\rho(x)}{3}{x} &= \frac{\mathrm e^{- \frac{1}{x}}}{x^{4}} \left(6 - \frac{6}{x} + \frac{1}{x^{2}}\right) & \quad \to 0 \quad(x \to +0)\\
          \mdiff{\rho(x)}{4}{x} &= \frac{\mathrm e^{- \frac{1}{x}}}{x^{5}} \left(-24 + \frac{36}{x} - \frac{12}{x^{2}} + \frac{1}{x^{3}}\right) & \quad \to 0 \quad(x \to +0)\\
          \mdiff{\rho(x)}{5}{x} &= \frac{\mathrm e^{- \frac{1}{x}}}{x^{6}} \left(120 - \frac{240}{x} + \frac{120}{x^{2}} - \frac{20}{x^{3}} + \frac{1}{x^{4}}\right) & \quad \to 0 \quad(x \to +0)
          \end{align*}

       上の展開から
       :math:`x^{2m}\rho^{(m)}(x) = \rho(x)P(x)` の形に書けて、
       :math:`x \to +0` のときに :math:`\rho^{(m)}(x) \to 0` であると言えばよいであろうことがわかる。

  #. :math:`\RR^n` の連結な折れ線は、実数全体を定義域とする
     :math:`C^\infty` 級写像の像とできるという事実は大事。

3.8 第 3 章の解答
----------------------------------------------------------------------
解答まとめ。

----

:doc:`note4` へ。
