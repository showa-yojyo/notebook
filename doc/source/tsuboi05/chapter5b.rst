======================================================================
第 5 章 多様体上の関数（後編）
======================================================================

.. contents:: ノート目次

5.4 サードの定理とモース関数
======================================================================

式で定義されている図形は、多くの場合多様体である。

.. _tsuboi05.5.4.1:

* 定理 5.4.1: `サードの定理 <http://mathworld.wolfram.com/SardsTheorem.html>`__

  * :math:`C^\infty` 級写像 :math:`\fn{F}{M}N` の臨界値は測度が 0 である。

.. _tsuboi05.5.4.2:

* 定義 5.4.2: 非退化、`モース関数
  <http://mathworld.wolfram.com/MorseFunction.html>`__

  * 臨界点 :math:`x` が非退化であるとは、点 :math:`x` における関数のヘッセ行列が
    正則であることをいう。
  * 関数 :math:`{f \in C^\infty(M)}` がモース関数であるとは、多様体上のどの臨界
    点においても非退化であることをいう。

* ヘッセ行列の正則性は座標近傍の取り方によらない：

  臨界点 :math:`x` と座標近傍 :math:`{(U, \varphi = (x_1, \dotsc, x_n))}` につい
  て行列 :math:`{\left(\dfrac{\partial^2 (f \circ \varphi\inv)}{\partial x_i
  \partial x_j}(\varphi(x))\right)_{i, j}}` がヘッセ行列だ。

  * この座標近傍で関数が二次関数 :math:`{\displaystyle \sum_{i, j}^n
    \left(\dfrac{\partial^2 (f \circ \varphi\inv)}{\partial x_i \partial
    x_j}\right)(\varphi(x))x_i x_j}` で近似できることを意味する。
  * ヘッセ行列が正則であるかどうかは座標近傍によらない。なぜなら、別の座標近傍
    :math:`{(U, \psi = (y_1, \dots, y_n))}` について :math:`{P =
    \left(\dfrac{\partial y_k}{\partial x_i}\right)_{i, k}}` とおくと
    :math:`{H(f \circ \varphi\inv) = {}^t\!PH(f \circ \psi\inv)P}` が成り立つか
    らだ。

* 二次曲面の形は行列 :math:`{\displaystyle \sum_{i, j}^n \frac{\partial^2(f
  \circ \varphi\inv)}{\partial x_i \partial x_j}(\varphi(x))}` の重複を込めた正
  と負それぞれの固有値の個数で分類できる。
* 二次曲面を変換して座標系を正則行列に取り替えることで、次の標準形に書き換えられ
  る：

  .. math::

     -\sum_{i = 1}^k x_i^2 + \sum_{i = k + 1}^n x_i^2.

* 二次曲面の行列の符号数も取り方によらない。
* ちなみに負の固有値の個数をモース臨界点の指数という。

.. _tsuboi05.5.4.3:

* 補題 5.4.3: モースの補題

  * 関数 :math:`f` の非退化な臨界点 :math:`{x^0 \in M}` の座標近傍 :math:`{(U_i,
    \varphi_i = (x_1, \dotsc, x_n))}` で次のようなものがある：

    .. math::
       :nowrap:

       \begin{align*}
       (f \circ \varphi_i\inv)(x_1, \dotsc, x_n)
       = f(x^0) - \sum_{i = 1}^k x_i^2 + \sum_{i = k + 1}^n x_i^2.
       \end{align*}

  * 証明方針を挙げていく：

    * 点 :math:`x^0` を原点に移動して考えたい。つまり :math:`{f - f(x^0)}` を最
      初から考える。さらに必要ならば線形変換しておいて :math:`{\dfrac{\partial^2
      f}{\partial x_i \partial x_j}(0, \dotsc, 0)}` が対角化されているとしてよ
      い。このとき、この行列の (1, 1) 成分がゼロでないことが大事だ。
    * 関数 :math:`f` をアダマールの補題（先述）による書き方にしておく：

      .. math::

         f = \sum_{i = 1}^n x_i g_i,\quad
         g_i = x_1 h_{i1} + \dotsb + x_n h_{in}.

      このとき :math:`{g_i(0, \dotsc, 0) = 0}` および :math:`{h_{11} =
      \dfrac{\partial^2 f}{\partial x_1^2} \ne 0}` に注意。

    * :math:`{f = \sum h_{ij} x_i x_j}` だが、これを :math:`{h_{ij} =
      \dfrac{h_{ij} + h_{ji}}{2}}` と置き換えて :math:`{h_{ij} = h_{ji}}` として
      もよい。
    * 平方完成と座標変換を順次適用する。最初はこうする：

      .. math::

         f = h_{11}\left(x_1 + \frac{h_{12}}{2 h_{11}}x_2
           + \dotsb + \frac{h_{1n}}{2 h_{11}}x_n\right)^2
           + \sum_{i, j = 2}^n h'_{ij} x_i x_j.

      この第一項の平方根を :math:`y_1` とすると、座標変換 :math:`{(x_1, \dotsc,
      x_n) \longmapsto (y_1, x_2, \dotsc, x_n)}` は局所的に微分同相となる。これ
      により次のように書ける：

      .. math::

         f = \sgn(h_{11})y_1^2 + \sum_{i, j = 2}^n h'_{ij}(x_2, \dotsc, x_n) x_i x_j.

      ここで :math:`h'` を関数化させた。この平方完成と座標変換をシグマの項に対し
      て順次適用すると、主張の等式が得られる。

.. _tsuboi05.5.4.4:

* 例 5.4.4: 例題 2.4.1 の吟味

  * この関数は実はモース関数なのであった。
  * 球面上には指数 0, 1, 2 の臨界点がそれぞれ 2 個ずつある。

.. _tsuboi05.5.4.5:

* 問題 5.4.5: :math:`{f(x, y) = (2 + \cos y)(a\cos x + b \sin x) + c \sin y,\
  ((a, b, c) \ne (0, 0, 0))}`

  この関数は :math:`\fn{F}{\RR^2/(2\pi\ZZ)^2}\RR` を誘導する。臨界点の個数が有限
  となる条件と退化する条件とを求める。

  * :math:`F` が well-defined であることを確かめる。いつも通り :math:`{[x_1,
    y_1] = [x_2, y_2] \iff f(x_1, y_1) = f(x_2, y_2)}` を示せばよい。これは三角
    関数の性質より明らか。
  * :math:`F` が :math:`C^\infty` 級であることも確認する。
  * まずはヤコビ行列を計算する。

    * :math:`{Df = \begin{pmatrix}0 & 0\end{pmatrix}}` となるには :math:`{-a\sin
      x + b\cos x = 0}` かつ :math:`{-\sin y(a\cos x + b\sin x) + c\cos y = 0}`
      が条件。

      * :math:`{a\cos x + b\sin x = 0}` のときは :math:`{a = 0},\ {b = 0}` であ
        り、:math:`{c \ne 0}` となって :math:`{\cos y = 0.}`

        :math:`{[x, y], \quad y \equiv 0 \pmod \pi}` なる無限個の点が :math:`F`
        の臨界点となる。

      * :math:`{a\cos x + b\sin x \ne 0}` のときは以下の四個の組み合わせを決める
        四個の :math:`x, y` が臨界点を与える：

        .. math::

           \begin{align*}
           (\cos x, \sin x) =& \left(\pm\dfrac{a}{\sqrt{a^2 + b^2}}, \pm\dfrac{b}{\sqrt{a^2 + b^2}}\right),\\
           \tan y =& \pm\dfrac{c}{\sqrt{a^2 + b^2}}.
           \end{align*}

  * それからヘッセ行列を計算する。

    .. math::

       \begin{pmatrix}
       (-a\cos x - b\sin x)(\cos y + 2) & (a\sin x - b\cos x)\sin y\\
       (a\sin x - b\cos x)\sin y & (a\cos x - b\sin x)\cos y - c\sin y
       \end{pmatrix}

  * あとは三角関数の性質を利用する。
  * 臨界点を調べる。対角行列が得られるので、符号数を確かめることになる。最終的に
    :math:`{\cos y}` の符号と一致する？

.. _tsuboi05.5.4.6:

* 問題 5.4.6: ファイブレーション

  複素射影空間 :math:`{\CC P^n = (\CC^{n + 1} \minuszero)/\CC^\times}` の単位球
  面 :math:`S^{2n + 1} = \set{(z_1, \dotsc, z_{n + 1}) \in \CC^{n + 1} \sth
  \abs{z} = 1}` と :math:`U(1) = \set{\mathrm e^{\sqrt{-1}\theta} \sth \theta
  \in \RR}` について

  * :math:`{g \in U(1)}` に対して :math:`{(g, z) \longmapsto (gz_1, \dotsc,
    gz_n)}` とすると、これは群の作用となる。

    #. :math:`C^\infty` 級写像であることは成り立つ。
    #. :math:`{1 \cdot \bm z = \bm z}` であることは、:math:`U(1)` の単位元が 1
       であるので成り立つ。
    #. :math:`{(g_1 g_2)\bm z = g_1(g_2 \bm z)}` であることは次のとおり：

       .. math::

          \begin{align*}
              (\mathrm e^{\sqrt{-1}\theta_1}, (\mathrm e^{\sqrt{-1}(\theta_2)}, \bm z))
          & = \mathrm e^{\sqrt{-1}\theta_1}(\mathrm e^{\sqrt{-1}\theta_2}\bm z)\\
          & = (\dotsc, \mathrm e^{\sqrt{-1}\theta_1} \mathrm e^{\sqrt{-1}\theta_2} z_k, \dots)\\
          & = (\dotsc, \mathrm e^{\sqrt{-1}(\theta_1 + \theta_2)}z_k, \dots)\\
          & = (\mathrm e^{\sqrt{-1}(\theta_1 + \theta_2)}, \bm z)
          \end{align*}

  * :math:`{S^{2n + 1} \overset{i}{\longto} \CC^{n + 1}\minuszero
    \overset{p}{\longto} \CC P^n}` のランクはいくらか。ただし :math:`i,\ p` は包
    含写像と射影である。

    * 解答は :math:`2n` なのだが、接写像 :math:`{(p \circ i)_*}` が全射であるこ
      とを示すことによる。
    * :math:`{\CC P^n}` の座標近傍系は :ref:`問題 3.3.7<tsuboi05.3.3.7>` と同じ
      ものを用いる。添字の記号が包含写像とカブるのは意図的なもの。
    * :math:`{\bm z^0 \in S^{2n + 1}}` に対して :math:`{(p \circ i)(\bm z^0) \in
      V_i.}`

    ここからがよくわからない。

    * 点 :math:`{\varphi_i((p \circ i)(\bm z^0))}` を通る :math:`C^\infty` 級曲
      線を考える。
    * TBW

  * 次に示す関数は :math:`\fn{F}{\CC P^n}\RR` を誘導する：

    .. math::
       :nowrap:

       \begin{align*}
       f(z) = \dfrac{\displaystyle \sum_{k = 1}^{n + 1} k \abs{z_k} ^2}{\displaystyle \sum_{k = 1}^{n + 1} \abs{z_k} ^2}.
       \end{align*}

    * :math:`F` が well-defined であることを確認する： :math:`{\bm z \in \CC^{n
      + 1}}`, :math:`{\bm z' = \lambda \bm z,\quad \lambda \in \CC^\times}` に対
      して :math:`{F(\bm z) = F(\bm z')}` が成り立つ。
    * :math:`C^\infty` 級であることを確認する。これは :math:`{F \circ
      \varphi_i\inv}` を調べる必要がある。 :math:`{(x_1, \dotsc, x_n) \in
      \varphi_i(V_i)}` に対して :math:`{\varphi_i\inv(x_1, \dotsc, x_n)} = {(z_1,
      \dotsc, z_{i - 1}, 1, z_{i + 1}, \dotsc, z_n).}`

      * :math:`{F \circ \varphi_i\inv}` の分子を計算すると :math:`{\displaystyle
        \sum_{k = 1}^{i - 1}k\abs{x_k}^2 + i \cdot 1^2 + \sum_{k = i + 1}^{n +
        1}k\abs{x_k}^2 = i + \sum_{k = 1}^{i - 1}k\abs{x_k}^2 + \sum_{k = i}^n(k
        + 1)\abs{x_k}^2.}`
      * :math:`{F \circ \varphi_i\inv}` の分母を計算すると :math:`{\displaystyle
        \sum_{k = 1}^{i - 1}k\abs{x_k}^2 + 1^2 + \sum_{k = i + 1}^{n +
        1}k\abs{x_k}^2 = 1 + \sum_{k = 1}^{i - 1}k\abs{x_k}^2 + \sum_{k = i +
        1}^n(k + 1)\abs{x_k}^2.}`

      分母がゼロになることはない。

  * :math:`F` の臨界点は :math:`\fn{F_*}{T_x \CC P^n}\RR` がゼロとなる
    :math:`{x \in \CC P^n}` である。

    * ヒントには合成写像 :math:`{T_zS^{2n + 1} \longto T_x\CC P^n \longto \RR}`
      を考えろとある。

    #. :math:`S^{2n + 1}` 上の関数 :math:`f` と座標近傍 :math:`{(U_i^\pm,
       \varphi_i^\pm), (V_i^\pm, \psi_i^\pm)}` を考える。

       .. math::

          \begin{align*}
          U_i^\pm = \set{\bm z \in S^{2n + 1} \sth \Re z_i \gtrless 0}, & \quad \varphi_i^\pm(\bm z) = (z_1, \dotsc, z_{i - 1}, \Im z_i, z_{i + 1}, \dotsc, z_{n + 1}),\\
          V_i^\pm = \set{\bm z \in S^{2n + 1} \sth \Im z_i \gtrless 0}, & \quad \psi_i^\pm(\bm z) = (z_1, \dotsc, z_{i - 1}, \Re z_i, z_{i + 1}, \dotsc, z_{n + 1}).
          \end{align*}

    #. :math:`{f \circ (\varphi_i^\pm)\inv = i + \sum(k - i)\abs{z_k}^2}` および
       :math:`{f \circ (\psi_i^\pm)\inv = i + \sum(k - i)\abs{z_k}^2}` を考え
       る。

       .. math::

          \begin{align*}
          &D f\circ (\varphi_i^\pm)\inv = 0 \iff z_k = 0 (k \ne i)\\
          &D f\circ (\psi_i^\pm)\inv = 0 \iff z_k = 0 (k \ne i)
          \end{align*}

    #. 以上より :math:`{\bm z \in S^{2n + 1}}` が正則点であることは、:math:`\bm
       z` が :math:`{i \ne j \implies z_i \ne z_j}` であることを同値である。
    #. :math:`{F \circ (p \circ i) = f}` が成り立つので :math:`{F_* \circ (p
       \circ i)_* = f_*}` である。ゆえに :math:`f` の正則点 :math:`\bm z` は
       :math:`{F \circ (p \circ i)(\bm z)}` が :math:`F` の正則点となる。
    #. 臨界点は各 :math:`{(p \circ i)(\bm e_i)\quad(n = 1, \dotsc, n + 1)}` であ
       る。

  * 臨界点におけるヘッセ行列を求める。

    * ポイントは :math:`V_i` 上 :math:`{F \circ \varphi_i\inv}` を無限級数の形に
      展開して、:math:`\abs{z_k}^4` 以降の項を捨てる。

      .. math::

         F \circ \varphi_i\inv(\bm w)
         = i + \sum_{k = 1}^{i - 1}(k - i)\abs{w_k}^2
         + \sum_{k = i}^n(k + 1 - i)\abs{w_k}^2 + \dotsb.

    * 上の式からヘッセ行列を求めると次のようになるので、モース臨界点の指数は
      :math:`{2(i - 1)}` である。

      .. math::

         \diag(2(1 - i), 2(1 - i), \dotsc, -2, -2, 2, 2, \dotsc, 2(n + 1 - i), 2(n + 1 - i)).

* ほとんどすべての射影がモース関数である (p. 107)。

.. _tsuboi05.5.4.8:

* 問題 5.4.8: :ref:`問題 5.2.5<tsuboi05.5.2.5>` の続き。

  同じ記号を引き続き用いる上で、次の仮定を追加する：

  * :math:`\fn{i}{M}\RR^N` を包含写像、
  * :math:`\fn{\operatorname{pr}_2}{\RR^N}\RR^N` を第二成分への射影、
  * :math:`\fn{L}{\RR^N}\RR` を線形写像 :math:`{\displaystyle L(\bm x) = \sum_{i
    = 1}^N a_i x_i}` とする。

  このとき :math:`{\bm a \in \RR^N}` が :math:`{\operatorname{pr}_2|X}` の正則値
  であることと、:math:`{L \circ i}` がモース関数であることは同値である。

  #. :ref:`問題 5.2.5<tsuboi05.5.2.5>` のグラフ表示の記号群を再利用する。

     .. math::

        \begin{align*}
        \operatorname{pr}_2|X &= (\bm y_2 Dg_{(\bm x_1)}, \bm y_2)\\
        &= \left(\sum_{k = p + 1}^N y_k \frac{\partial g_k}{\partial x_1}, \dotsc,
           \sum_{k = p + 1}^N y_k \frac{\partial g_k}{\partial x_p},
           y_{p + 1}, \dotsc, y_N\right).
        \end{align*}

  #. ヤコビ行列を計算すると :math:`{\sum y_k g_k}` の二階微分からなる成分が現れ
     るので、このブロックの正則性が条件となる。
  #. 一方、:math:`{(L \circ i)(\bm x_1, g(\bm x_1)) = \sum a_k x_k + \sum a_k
     g_k}` が :math:`{\bm x^0}` の近傍でモース関数であることは、:math:`{\bm
     x^0}` が :math:`{\displaystyle a_l + \sum_{k = p + 1}^N a_k \frac{\partial
     g_k}{\partial x_l} = 0\quad(l = 1, \dotsc, p)}` を満たすときにヘッセ行列
     :math:`{\displaystyle \left(\sum_{p + 1}^N a_k \frac{\partial^2
     g_k}{\partial x_l \partial x_m}\right)_{l, m}}` が正則であることと同値であ
     る。

     これは :math:`{\bm a = (a_j) \in \RR^N}` が :math:`F` のグラフ上で
     :math:`{\operatorname{pr}_2|X}` の正則値である条件と同じだ。
  #. あとはコンパクト性による。有限個の近傍それぞれで上の議論を繰り返すと
     :math:`{(L \circ i)}` がモース関数であることと、:math:`\bm a` が
     :math:`{\operatorname{pr}_2|X}` の正則値であることが同値となる。

5.5 サードの定理の証明の概略（展開）
======================================================================

証明のアウトラインが記されている。どうも測度論、例えばフビニの定理の知識を要するようだ。

5.6 モース関数の存在の証明の概略（展開）
======================================================================

:ref:`定理 5.2.3<tsuboi05.5.2.3>` と :ref:`問題 5.4.8<tsuboi05.5.4.8>` を合わせ
るとモース関数の存在を示すことができる (p. 111)。

5.7 関数の空間、写像の空間（展開）
======================================================================

関数空間 :math:`C^\infty(M)` の位相を何か定義して、コンパクト多様体上のモース関
数の性質を述べたい。

以下で使用する記号として

* :math:`M` を :math:`n` 次元コンパクト多様体、
* :math:`\set{(U_i, \varphi_i = (x_1^{(i)}, \dotsc, x_n^{(i)}))}` を有限座標近傍
  系、
* :math:`{V_i \subset \closure{V_i} \subset U_i,\ \set{V_i}_{i = 1, \dotsc, k}}`
  を開被覆

とする。

目標は :math:`C^r` 位相というものを定めること、つまり関数 :math:`{f \in
C^\infty(M)}` の :math:`{\eps \gt 0}` 近傍 :math:`{N_\eps^r = N_\eps^r(f,
\set{V_i})}` を定めること。

.. math::
   :nowrap:

   \begin{gather*}
   N_\eps^r(f, \set{V_i}) = \Set{
       f + h \in C^\infty(M)
       \Sth s \le r,\
       \norm{D^s((h \circ \varphi_i\inv)|\varphi_i(\closure{V_i}))} < \eps
   }.
   \end{gather*}

「ヤコビ行列の :math:`{s \le r}` 乗のノルムが抑えられる」の意。行列に対するノル
ムが具体的に何であるかを述べていないが、ノルムならば何でもよいようだ。解析で採用
する行列のノルムは次のものが普通であり、次のページでも言及されている：

.. math::

   \norm{A} = \sup_{\bm x \ne 0}\frac{\norm{A\bm x}}{\norm{\bm x}}.

.. _tsuboi05.5.7.1:

* 補題 5.7.1: 有限座標近傍系を別のものにしても :math:`C^r` 位相は等しい。

  証明に使用する記号を定義しておく。

  * 別の座標近傍系を :math:`\set{(U_j', \varphi_j' = (y_1, \dotsc, y_n))}` とお
    く。このとき、先ほどと同じように開集合、コンパクト集合列 :math:`{V_j'
    \subset \closure{V_j'} \subset U_j'}` を取り、次を示すことを目標とする：

    .. math::

       N_\eps^r(f, \set{V_i}) \subset N_{K\eps}^r(f, \set{V_j'})

  * 座標変換をいつものように :math:`{\gamma_{ij} = (\varphi_i \circ
    \varphi_j\inv)|\varphi_j'(U_i \cap U_j')}` で表す。:math:`{h \circ
    \varphi_j'\inv = (h \circ \varphi_i\inv) \circ \gamma_{ij}}` のようになる。

  帰納法で示せば良いようだ。

  * :math:`{r = 0}` のときは :math:`{N_\eps^0(f_i, \set{V_i}) = N_\eps^0(f_i,
    \set{V_j'})}` は成り立つ。

    * ヤコビ行列のゼロ乗のノルムは単位行列のそれとなり、つまり 1 であるからとい
      うことか。ということは、:math:`\eps` の値によっては :math:`C^0` 近傍は空集
      合になったりするのか？

  * :math:`{r = 1}` のとき：

    * :math:`{D(h \circ \varphi_j'\inv)} = {D(h \circ \varphi_i\inv) \circ
      \gamma_{ij} D\gamma_{ij}}` であり、
    * そして :math:`{N_\eps^1(f, \set{V_i}) \subset N_K^1(f, \set{V_j'})}` を満
      たす :math:`\eps` に依存する正の数 :math:`K` が下のようにしてとれるので成
      り立つ：

      .. math::
         :nowrap:

         \begin{gather*}
         K = \max_{i, j}
         \max_{x \in \varphi_j'(\closure{V_i} \cap \closure{V_j}')}
         \norm{D\gamma_{ij(x)}}.
         \end{gather*}

      添字が有限個であることと、各 :math:`{\closure{V_i} \cap \closure{V_j}'}`
      がコンパクトであることによる。

  * :math:`{r = 2}` のときは p. 104 のような（ここにはとても記せられない）計算を
    して :math:`{N_\eps^2(f, \set{V_i}) \subset N_K^2(f, \set{V_j'})}` を満たす
    :math:`\eps` 依存の正数 :math:`K` を取れることを示す。
  * 一般の :math:`{r = s}` のときは :ref:`chain rule<tsuboi05.1.2.8>` を順次実行
    して、上記の場合の成立を根拠に成り立つことを示す。

    * `ファー・ディ・ブルーノの公式
      <http://mathworld.wolfram.com/FaadiBrunosFormula.html>`__ という、合成写像
      の高次の微分を書き下すやり方がある。

.. _tsuboi05.5.7.2:

* 定義 5.7.2: コンパクト多様体に関する関数空間 :math:`{f \in C^\infty(M)}` の
  :math:`C^r` 位相。

.. _tsuboi05.5.7.3:

* 注意 5.7.3: コンパクトでない多様体の場合について。

  * :math:`\closure{V_i}` がコンパクトであるような開被覆を取れれば
    :math:`C^\infty(M)` の位相を定められる。ただし、開被覆の取り方が変わると位相
    も変わる。

.. _tsuboi05.5.7.4:

* 定理 5.7.4: :math:`{f \in C^\infty(M)}` の :math:`C^2` 位相で、モース関数全体
  は開かつ稠密。

コンパクト多様体間の写像全体の空間 :math:`{C^\infty(M, N)}` についても
:math:`C^r` 位相を考えられる。

* 多様体 :math:`N` の有限局所座標系を :math:`\set{(W_j, \psi_j)}` とする。

  * このとき次のような開被覆 :math:`\set{V_{ji}}` が存在するのであった：
    :math:`{V_{ji} \subset \closure{V_{ji}} \subset U_i \cap F\inv(W_j).}`

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

    :math:`{\varphi_i(\closure{V_{ji}})}` はコンパクトゆえ、上の長い関数
    :math:`{\varphi_i(\closure{V_{ji}}) \longto \psi_j(V_j) \subset \RR^n}` に近
    い :math:`C^\infty` 写像の像は :math:`{\psi_j(V_j)}` にあり、微分が定義でき
    る。

  * :math:`C^r` 位相は各有限座標近傍系のとり方によらない。

写像の空間の開かつ稠密な集合は横断性を考えることで与えられる (p. 115)。

.. _tsuboi05.5.7.6:

* 定理 5.7.6: 横断性定理

  難しい。

  :math:`{C^\infty(M, N)}` の :math:`C^1` 位相において、:math:`N` の部分多様体
  :math:`L` を横断的な写像は開かつ稠密である。

  * :math:`{F \in C^\infty(M, N)}` について :math:`{F(x) \in L}` ならば
    :math:`{F_*(T_x(M)) + T_{F(x)}L = T_{F(x)}N}` が成り立つものの性質に関する定
    理。
  * 証明では線形代数の何かをまず利用する。
  * 途中、サードの定理を必要とする。

.. _tsuboi05.5.7.7:

* 注意 5.7.7: :math:`\fn{F}{M}N` が :math:`{L \subset N}` と横断的ならば、
  :math:`{F\inv(L)}` は :math:`M` の余次元が :math:`L` のそれに等しいような部分
  多様体である。

.. _tsuboi05.5.7.8:

* 注意 5.7.8: これは何を言っているのかわからない。包含写像の一方を近似する写像と
  取り替えると横断的となるとは？

5.8 第 5 章の問題の解答
======================================================================

ノートはすでに書いた。
