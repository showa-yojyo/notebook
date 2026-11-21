======================================================================
付録 多様体の三角形分割の構成（展開） 1/2
======================================================================

* :ref:`定理 5.1.3 <tsuboi08.5.1.3>` の証明の概略。Whitney の
  `Geometric Integration Theory <https://press.princeton.edu/titles/3151.html>`__
  の内容を基にしているとのこと。
* 最初は :ref:`幾何学 I 定理 5.2.3<tsuboi05.5.2.3>` にある、コンパクト多様体が
  ユークリッド空間に埋め込み可能であることから出発する。

* \1. 証明の土台を準備する。

  * :math:`C^\infty` 級多様体を :math:`M` とし、コンパクトかつ :math:`n` 次元で
    あるとする。
  * :math:`M` はユークリッド空間 :math:`\RR^N` に埋め込まれるとする。
  * そのノルムを :math:`\norm{\cdot}` とする。
  * 点 :math:`p` の :math:`\delta` 近傍を :math:`B_\delta(p)` とする（開球と思っ
    てよさそうだ）。

  本書では :math:`M` と :math:`{M^n \in \RR^N}` を区別しているらしいが、
  ここでは面倒なので単に :math:`M` で済ませる。

.. _tsuboi08.appendix.1.1:

  * 1.1 :math:`{\forall \eps \gt 0, \exists \delta \gt 0}\text{ s.t. }\quad{\forall x \in M:}`

    * :math:`{T_xM \cap B_\delta(x) \subset B_{\eps\delta}(M \cap B_\delta(x))}` and
    * :math:`{M \cap B_\delta(x) \subset B_{\eps\delta}(T_xM \cap B_\delta(x)).}`

    本書図 A.1 はこれの :math:`{N = 2}` バージョンのイラストだ。円の直径が「接空
    間と開球の共通部分」に、内側の実線の円弧が「多様体と開球の共通部分」にそれぞ
    れ対応する。

    :math:`\fn{\pi_{T_xM}}{\RR^N}T_xM` を直交射影とする。

    * ノートでは以下字が潰れるので単に :math:`\pi` と書く。
    * この写像は像への微分同相写像である。
    * :math:`{\pi(T_xM \cap B_\delta(x)) \supset T_xM \cap B_{\delta - \eps\delta}(x).}`
      すなわち「図 A.1 の大円より小さい円を含む」か。

    :math:`{\delta \gt 0}` をもっと小さくとって次のようにできる：

    * :math:`{y \in M \cap B_\delta(x)}` における :math:`{\bm v \in T_yM}` に対
      して :math:`{\norm{\bm v - \pi(\bm v)} \le \eps\norm\pi(\bm v) \le
      \eps\norm{\bm v}.}`
    * :math:`{y, z \in M \cap B_\delta(x)}` に対して :math:`{\norm{(y - \pi(y))
      - (z - \pi(z))} \le \eps{\pi(y) - \pi(z)}.}`

.. _tsuboi08.appendix.1.2:

  * 1.2 :math:`M` のある近傍 :math:`U` をとれば、法束のゼロ切断の近傍と、法束か
    らの指数写像で微分同相である。それゆえ :math:`U` で法束の射影
    :math:`\fn{p_M}{U}M` が定義される。

    * :ref:`幾何学 I 問題 5.2.5<tsuboi05.5.2.5>` による。

    :math:`{x \in M}` について :math:`{B_\delta(x) \cap U}` において、
    :math:`{p_M|(B_\delta(x) \cap U)}` のファイバーの方向と :math:`\pi` のそれは
    ほとんど等しい（それは納得できる）。

    特に :math:`\bm v` を :math:`U` の点における接ベクトルとし、
    :math:`{\norm{\bm v - \pi(\bm v)} \le \dfrac{1}{2}}` が成り立つならば、
    :math:`{(p_M)_*\bm v \ne 0.}`

.. _tsuboi08.appendix.1.3:

  * 1.3 立方体の正則分割を定義する（本書図 A.2 の左側）。

    * 超立方体を単に立方体と書くことにしている。
    * 各次元版立方体の包含関係による列 :math:`{I^0 \subset I^1 \subset \dotsb
      \subset I^N}` に対応して、各重心 :math:`b_{I^0}, \dotsc, b_{I^k}` で構成さ
      れる単体 :math:`{\langle b_{I^0} \dots b_{I^k}\rangle}` が考えられる。

    空間 :math:`\RR^n` を辺長 :math:`\dfrac{2 \delta_0}{\sqrt{N}}` の立方体で細
    分し、すべての立方体の正則分割として得られる空間の単体分割を :math:`L` とす
    る。

    * :math:`L` の :math:`N` 単体の直径は :math:`\delta_0` である。

.. _tsuboi08.appendix.1.4:

  * 1.4 標準単体 :math:`\Delta^n` について、次を満たす :math:`{0 \lt \rho_0 \lt
    \dfrac{1}{2\sqrt{2}}}` が何か存在する：

      :math:`\Delta^n` の各頂点をそれぞれから距離 :math:`\rho_0` 以内の点に移し
      て得られる単体が、:math:`\Delta^n` と同相である。

    このような単体の直径は :math:`{1 + 2\rho_0}` 以下である。

    .. todo::

       ここでいったん保留。:math:`\rho_0` をある定数 :math:`H` 以上の値であると
       する。

.. _tsuboi08.appendix.1.5:

  * 1.5 空間内の半径 1 の球 :math:`{B^N \subset \RR^N}` に対して次が成り立つ：

    .. math::

       \forall \eps \gt 0 \exists \delta \gt 0 \quad\text{s.t. }
       \operatorname{vol}_N(B_\delta(A) \cap B^N) \le \eps\operatorname{vol}_N(B^N).

    ここで :math:`A` は次元が :math:`{N - 1}` 以下の affine 空間であり、
    :math:`\operatorname{vol}_N` は :math:`\RR^N` での「体積」とする。

    * 立方体分割の正則分割 :ref:`1.3<tsuboi08.appendix.1.3>` の頂点に集まる単体
      の個数は、:math:`b_{I^N}` に交わる単体の個数を超えない。その個数を
      :math:`k_N` としておく。
    * :math:`{\eps \lt \dfrac{1}{k_N}}` に対して先ほどの体積不等式を満たす
      :math:`\delta_N` をとると、次の条件を満たす :math:`B^N` の点が何か存在す
      る：

        点が affine 部分空間の和集合 :math:`{\displaystyle \bigcup_{i =
        1}^{k_N}\delta_N(A_i)}` に含まれない。

.. _tsuboi08.appendix.1.6:

  * 1.6 :math:`{A_0 \subset A_1 \subset \RR^N}` を affine 部分空間とし、
    :math:`{\sigma \in A_1}` を affine 単体とする。

    補集合の点 :math:`{p \in \RR^N\setminus{A_1}}` に対して次の集合を考える：

    .. math::

       p * \sigma = \set{(1 - t)p + ty \sth y \in \sigma,\ 0 \le t \le 1}

    * これを :dfn:`join` と呼ぶ。
    * :math:`{p * \sigma}` は :math:`{\dim\sigma + 1}` 単体である。
    * 平面幾何的な理由によって（本書の図 A.3 に関する説明に相当）次の不等式が成
      り立つ：

      .. math::

         \dist(p * \sigma) \ge \frac{\dist(\sigma, A_0)\dist(p, A_1)}{\diam(p * \sigma)}.

.. _tsuboi08.appendix.1.7:

  * 1.7 立方体分割の大きさ :math:`c` を次のように定める：

    .. math::

       c = \frac{\delta_N^{N - n}\rho_0^{N ^ n}}{2^{2(N - n)}(1 + 2\rho_0)^{N - n}}.

    ここで十分小さい :math:`{a \lt 1}` をとり（具体的な値は後で決める）

    .. math::

       \eps = \frac{ac^2}{4}

    とする。

    * :ref:`1.1<tsuboi08.appendix.1.1>` で得られる :math:`\delta` をこの
      :math:`\eps` による値とする。
    * :ref:`1.3<tsuboi08.appendix.1.3>` の直径 :math:`\delta_0` に対して
      :math:`{\delta_0 = \dfrac{\delta}{2^3}}` とする。
    * :math:`M` に交わる立方体分割の立体の 4 倍のスケールの立体は交点の
      :math:`\delta` 近傍に含まれる。
    * :math:`{T_xM \cap B_{8\delta_0}(x)}` と :math:`{M \cap B_{8\delta_0}(x)}`
      は互いの :math:`{8\eps\delta_0 = \dfrac{1}{2}ac^2\delta_0}` 近傍にある。両
      者は実は数値的にはほとんど一致している。

* \2. 立方体分割の正則分割 :math:`L` を変形して、多様体に対して一般の位置にある
  三角形分割 :math:`\widehat{L}` を構成する。

  :math:`L` は直径 :math:`2\delta_0` の立方体による立方体分割である。単体では直
  径は :math:`\delta_0` である。

.. _tsuboi08.appendix.2.1:

  * 2.1 立方体分割のすべての頂点 :math:`{I^0 = b_{I^0}}` に対して次を行なう：

    * この点から距離 :math:`{\rho_0 \delta_0}` 以下、
    * :math:`M` から距離 :math:`\frac{\delta_N \rho_0}{2}\delta_0` 以上

    離れた点をとり、それを :math:`\widehat{b_{I^0}}` とする。

.. _tsuboi08.appendix.2.2:

  * 2.2 各 :math:`{k\quad(1 \le k \lt N - n)}` 次元立方体 :math:`I^k` の重心
    :math:`b_{I^k}` に対して次を行なう：

    * この点から距離 :math:`\rho_0 \delta_0` 以下、
    * :math:`M` から距離 :math:`\frac{\delta_N \rho_0}{2}\delta_0` 以上

    離れた点をとり、それを :math:`\widehat{b_{I^k}}` とする。さらに

    * :math:`\langle\widehat{b_{I^0}} \dots \widehat{b_{I^k}}\rangle \cap M = \varnothing.`

    上記左辺の :math:`l` 単体 :math:`{\tau^l\quad(0 \le l \le k)}` を :math:`M`
    から距離

    .. math::

       \frac{\delta_N^{l + 1}\rho_0^{l + 1}\delta_0}{2^{2l + 1}(1 + 2\rho_0)^l}

    以上離しておいて、:math:`{l = 0}` のとき頂点と :math:`M` の距離、および
    :math:`k` 単体と :math:`M` が交わらないことを保証する。

    :math:`{k = 1, 2, \dotsc}` について帰納的に :math:`b_{I^1}, b_{I^2}, \dotsc`
    を順に処理し、:math:`{k - 1}` 次元まで（距離の）不等式が成り立っているとす
    る：

    .. math::

       \tau^l \subset \langle\widehat{b_{I^0}} \dots \widehat{b_{I^{k - 1}}}\rangle
       \implies \dist(\tau^l, M) \ge
       \frac{\delta_N^{l + 1}\rho_0^{l + 1}\delta_0}{2^{2l + 1}(1 + 2\rho_0)^l}.

    :math:`M` の点の位置関係により場合分けをする：

    * 点が :math:`B_{3\delta_0}(b_{I^k})` に含まれない場合。このときは
      :math:`{\widehat{b_{I^k}} = b_{I^k}}` とする。これを頂点とする新しい
      :math:`l` 単体はすぐ上に記した距離に関する不等式を満たす。

    * 点が :math:`B_{3\delta_0}(b_{I^k})` に含まれる場合。

      その点を :math:`{p \in B_{3\delta_0}(b_{I^k})}` とする。

      * :math:`\tau^{l - 1}\quad{(l - 1 \lt N - n - 1)}` を接空間 :math:`T_xM`
        と立方体分割 :math:`L` の :math:`{k - 1}` 骨格（これが何なのかわからな
        い）上の立方体の重心からなる単体であるとする。

      * :math:`\widehat{\tau^{l - 1}}` を単体 :math:`\tau^{l - 1}` を移動した単
        体であるとする。

      これらについて :math:`T_xM` と :math:`\widehat{\tau^{l - 1}}` の両方を含む
      :math:`{n + l}` 次元 affine 部分空間を考える。このような部分空間は高々
      :math:`k_N` 個しかない。なぜならば：

      * 空間の次元が :math:`{n + l \le n + k \lt N}` を満たし、
      * :math:`{b_{I^k} * \widehat{\tau^{l - 1}}}` が立方体分割の単体であるような
        :math:`\widehat{\tau^{l - 1}}` のとり方が高々 :math:`k_N` 個しかない

      ことによる。

      これらの affine 空間の :math:`{\delta_N\rho_0\delta_0}` 近傍の和集合を
      :math:`{B_{\rho_0\delta_0}(b_{I^k})}` で考えると、
      :ref:`1.5<tsuboi08.appendix.1.5>` よりある点 :math:`\widehat{b_{I^k}}` が
      この和集合と近傍の共通部分外に存在して、

      .. math::

         \dist(T_pM, \widehat{b_{I^k}}) \ge \delta_N\rho_0\delta_0

      を満たす。

      一方 :ref:`1.7<tsuboi08.appendix.1.7>` により
      :math:`{\dist(\widehat{b_{I^k}}, M) \ge
      \dfrac{\delta_N\rho_0}{2}\delta_0}` である。したがって :math:`{M \cap
      B_{4\delta_0}(p)}` は :math:`T_xM` の
      :math:`\dfrac{\delta_N\rho_0}{2}\delta_0` 近傍に含まれる。

      新 :math:`l` 単体は :math:`{\widehat{b_{I^k}} * \sigma^{l - 1}}` のように
      書ける。そして :ref:`2.2<tsuboi08.appendix.2.2>` の序盤での評価と
      :ref:`1.7<tsuboi08.appendix.1.7>` により次の評価が成り立つ：

      .. math::

         \dist(T_xM, \sigma^{l - 1}) \ge
         \frac{\delta_N^l\rho_0^l\delta_0}{2^2l(1 + 2\rho_0)^{l - 1}}.

      これに :math:`{\dist(T_xM, \widehat{b_{I^k}}) \ge \delta_N\rho_0\delta_0}`
      と :ref:`1.6<tsuboi08.appendix.1.6>` を用いて次を得る：

      .. math::

         \begin{align*}
         \dist(\widehat{b_{I^k}} * \sigma, TxM)
         &\ge \frac{\delta_N^l\rho_0^l\delta_0}{2^2l(1 + 2\rho_0)^{l - 1}}
         \cdot \delta_N\rho_0\delta_0 \cdot
         \frac{1}{(1 + 2\rho_0)\delta_0}\\
         &= \frac{\delta_N^{l+1}\rho_0^{l+1}\delta_0}{2^2l(1 + 2\rho_0)^l}.
         \end{align*}

      したがって :ref:`1.7<tsuboi08.appendix.1.7>` より：

      .. math::

         \dist(\widehat{b_{I^k}} * \sigma, M) \ge
         \frac{\delta_N^{l+1}\rho_0^{l+1}\delta_0}{2^{2l + 1}(1 + 2\rho_0)^l}.

.. _tsuboi08.appendix.2.3:

  * 2.3 :math:`{k \ge N - n}` に対して :math:`b_{I^k}` を基に新しい点
    :math:`\widehat{b_{I^k}}` を決める：

    * この点から距離 :math:`\rho_0 \delta_0` 以下、
    * :math:`M` から距離 :math:`\frac{\delta_N \rho_0}{2}\delta_0` 以上

    だけ離れた位置にあるとする。

    :ref:`2.2<tsuboi08.appendix.2.2>` における :math:`\widehat{b_{I^k}}` のとり
    方をすでに移された :math:`{l - 1}` 単体 :math:`{(l < k)}` だけを考えて行なう
    ことで、:math:`{\langle\widehat{b_{I^0}} \dots \widehat{b_{I^k}}\rangle}` の
    :math:`l` 単体は :math:`{l < N - n}` ならば：

    .. math::

       \dist(\sigma^l, M) \ge
       \frac{\delta_N^{l+1}\rho_0^{l+1}\delta_0}{2^{2l + 1}(1 + 2\rho_0)^l}

    とできることがわかる。

.. _tsuboi08.appendix.2.4:

  * 2.4 :ref:`1.7<tsuboi08.appendix.1.7>` の :math:`c` を用いて表すと、
    :math:`\widehat{L}` の :math:`{N - n - 1}` 骨格は :math:`M` から :math:`{2(1
    + 2\rho_0)\delta_0 c}` 以上の離れとなる。

    :ref:`1.7<tsuboi08.appendix.1.7>` から :math:`{x \in M}` に対して

    * :math:`{T_xM \cap B_{8\delta_0}(x)}` と
    * :math:`\widehat{L}` の :math:`{N - n - 1}` 骨格

    との距離は :math:`{2^2(1 + 2\rho_0)\delta_0}` 以上離れている。

* \3. 多様体と :math:`\widehat{L}` の位置関係を記述するための準備する。

  * :math:`\widehat{L}` は :math:`\RR^n` の三角形分割であり、
    :math:`M` に対して一般の位置にある。
  * :math:`\widehat{L}` の単体と :math:`M` の交点はほとんど凸包である。

.. _tsuboi08.appendix.3.1:

  * 3.1

    :math:`{\sigma^k \subset \RR^N}` とし、:math:`A` を :math:`n` 次元 affine 空
    間 :math:`A` とする。

    * :math:`{\dist(\partial \sigma^k, A) \gt d}` かつ :math:`{\dist(\sigma, A)
      \lt d}` であれば、:math:`{k + n = N}` かつ :math:`\sigma` と :math:`A` は
      ただ一点で交わる。
    * :math:`{p_1, p_2 \in \sigma}` に対して :math:`\pi_A` を :math:`A` への直交
      射影とすると、次が成り立つ：

      .. math::

         \norm{(p_1 - \pi_A(p_1)) - (p_2 - \pi_A(p_2))} \ge
         \frac{d}{\diam(\sigma)}\norm{p_1 - p_2}.

    以上を背理法とユークリッド幾何を用いて示す。

.. _tsuboi08.appendix.3.2:

  * 3.2

    * :math:`{\sigma^{N - n} \in \widehat{L}}`
    * :math:`{\sigma^{N - n} \subset B_{8\delta_0}(x)\quad\text{for }x \in M}`
    * :math:`{\sigma^{N - n} \cap T_xM = \set{r}}` (?)
    * :math:`\bm v` を :math:`\sigma^{N - n}` の接ベクトルであるとし、
    * :math:`{r + t\bm v \in \partial \sigma}`

    とすると、

    .. math::

       \begin{align*}
       \norm{t\bm v - \pi(t\bm v)}
       &= \norm{r + t\bm v - \pi(r + t\bm v)}\\
       &\ge 2(1 + 2\rho_0)\delta_0 c.\\
       \therefore \norm{\bm v - \pi(\bm v)}
       &\ge \frac{2(1 + 2\rho_0)\delta_0 c}{t\norm{\bm v}}\norm{\bm v}\\
       &\ge \frac{2(1 + 2\rho_0)\delta_0 c}{\diam{\sigma^{N - n}}}\norm{\bm v}\\
       &\ge 2c\norm{\bm v}.
       \end{align*}

.. _tsuboi08.appendix.3.3:

  * 3.3

    * :math:`{P(\sigma^{N - n})}` を affine 空間であり :math:`\sigma^{N - n}` を
      含むものであるとする。
    * :math:`{\RR^N/{P(\sigma^{N - n})}}` を商空間であり、:math:`{P(\sigma^{N -
      n})}` に平行な affine 空間を同一視して扱うものとする。
    * :math:`\fn{\pi'}{\RR^N}T_xM` を射影であり :math:`{P(\sigma^{N - n})}` に沿
      うものとする。

    このとき、次のことが成り立つ：

    * :math:`{\forall y \in M \cap B_{8\delta_0}(x),} {\forall \bm w \in T_yM,}
      {\norm{\pi'(\bm w)} \ge \dfrac{15}{16}\norm{\bm w}.}`
    * :math:`\pi'` は :math:`{M \cap B_{8\delta_0}(x)}` から像への微分同相であ
      り、:math:`{\pi'(M \cap B_{8\delta_0}(x)) \supset T_xM \cap
      B_{7\delta_0}(x).}`

      * これらは :ref:`1.1<tsuboi08.appendix.1.1>` と
        :ref:`3.2<tsuboi08.appendix.3.2>` から得られる。

    この不等式から :math:`{\pi'|(M \cap B_{8\delta_0}(x))}` の接写像が単射である
    ことが言える。

* \4. 多様体と :math:`\widehat{L}` の交わり方と記述する。

.. _tsuboi08.appendix.4.1:

  * 4.1 :math:`{x \in M}` について :math:`\sigma` を :math:`B_{8\delta_0}(x)` に
    含まれる :math:`\widehat{L}` の :math:`k` 単体であるとする。このとき：

    .. math::

       \sigma \cap M \ne \varnothing \implies k \ge N - n,\ T_xM \cap \sigma \ne \varnothing.

    :ref:`1.7<tsuboi08.appendix.1.7>`, :ref:`2.4<tsuboi08.appendix.1.7>`,
    :ref:`3.1<tsuboi08.appendix.1.7>` を用いる。

    :math:`{y \in \sigma \cap M}` を考える。:math:`\sigma` の面 :math:`\tau` で
    :math:`{\dist(\tau, T_xM) \lt 2(1 + 2\rho_0)\delta_0 c}` となり、その中で次
    元が最小のものを考える。

.. _tsuboi08.appendix.4.2:

  * 4.2 再び :math:`{x \in M}` について :math:`\sigma` を
    :math:`B_{8\delta_0}(x)` に含まれる :math:`\widehat{L}` の :math:`k` 単体で
    あるとする。このとき：

    .. math::

       \sigma \cap T_xM \ne \varnothing \implies k \ge N - n,\ M \cap \sigma \ne \varnothing.

    * :ref:`2.4<tsuboi08.appendix.2.4>`, :ref:`3.1<tsuboi08.appendix.3.1>`,
      :ref:`3.3<tsuboi08.appendix.3.3>`, :ref:`1.7<tsuboi08.appendix.1.7>`,
      :ref:`3.2<tsuboi08.appendix.3.2>` を用いる。
    * :ref:`4.1<tsuboi08.appendix.4.1>` の :math:`\sigma` の面 :math:`\tau` と同
      様のものを考える。

.. _tsuboi08.appendix.4.3:

  * 4.3 :math:`\sigma^{N - n}` を :math:`\widehat{L}` の :math:`{N - n}` 単体で
    あるとすると、これは :math:`M` と高々一点で交わる。

    :ref:`1.1<tsuboi08.appendix.1.1>` と :ref:`3.2<tsuboi08.appendix.3.2>` によ
    る。:math:`{y, z \in \sigma^{N - n} \cap M}` に対して：

    .. math::

       \begin{align*}
       \norm{(y - \pi(y)) - (z - \pi(z))}
       &\ge \eps\norm{\pi(y) - \pi(z)}\\
       &\ge \frac{ac^2}{2^4}\norm{\pi(y) - \pi(z)}.
       \end{align*}

    ここで :ref:`3.2<tsuboi08.appendix.3.2>` によると：

    .. math::

       \norm{(y - \pi(y)) - (z - \pi(z))} \ge 2c \norm{\pi(y) - \pi(z)}.

    :math:`\dfrac{ac^2}{2^4} \lt 2c` だから :math:`{y = z}` が必要である。

.. _tsuboi08.appendix.4.4:

  * 4.4 :math:`\sigma` を :math:`\widehat{L}` の :math:`{N - n + k}` 単体である
    とすると、 :math:`{\sigma \cap M \ne \varnothing}` であるならば、次のような
    :math:`{N - n}` 単体が存在する：

      各頂点が :math:`\sigma` の頂点を頂点とする。

    :math:`{x \in \sigma \cap M}` における :math:`T_xM` と交わる :math:`\sigma`
    の :math:`{N - n}` 次元の面 :math:`\tau` を :math:`{\RR^N/{T_xM}}` への射影
    によって :math:`{0 = [T_xM]}` を含む単体に写る（？）

    さらに :math:`{\partial(\tau * \sigma)\setminus\tau}` の単体で :math:`{0 =
    [T_xM]}` を含む単体に写るものがある。それに対して :math:`{? \cap T_xM \ne
    \varnothing}` かつ :math:`{? \subset B_{8\delta_0}(x)}` により :ref:`4.2
    <tsuboi08.appendix.4.2>` を用いて :math:`{? \cap M \ne \varnothing.}`

.. _tsuboi08.appendix.4.5:

  * 4.5 :math:`\sigma^{N - n} = {\langle v_0 \dots v_{N - n}\rangle}` と
    :math:`M` が交わるならば、交点の重心座標は :math:`2c` 以上である。すなわち、
    交点を :math:`{\psi(\sigma^{N - n})}` を書くと、

      :math:`\displaystyle \sum_{i = 0}^{N - n}t_i v_i` と表すときに
      :math:`{t_i \ge 2c\quad(i = 0, \dotsc, N - n)}` である。

    :math:`v_i` の対面 :math:`\tau_i = {\langle v_0 \dots v_{i - 1} v_{i + 1}
    \dots v_{N - n}\rangle}`を含む affine 空間 :math:`{P(\tau_i)}` からの距離を
    考える：

    .. math::

       \dist(v_i, P(\tau_i)) \le \diam(\sigma^{N - n}) \le (1 + 2\rho_0)\delta_0 c.`

    :ref:`2.4<tsuboi08.appendix.2.4>` より

    .. math::

       \dist(\psi(\sigma^{N - n}), P(\tau_i)) \ge 2(1 + 2\rho_0)\delta_0 c.`

.. _tsuboi08.appendix.4.6:

  * 4.6 :math:`\displaystyle {\psi(\sigma^{N - n + k}) = \sum_{i = 0}^{N - n +
    k}t_i v_i\quad(k \ge 1)}`と書くとき、:math:`{t_i \ge \dfrac{2c}{k_N}.}`

    :math:`\sigma^{N - n + k} = {\langle v_0 \dots v_{N - n + k}\rangle} \cap M
    = \varnothing` ならば、:math:`\tau_1, \dotsc, \tau_m \subset \sigma^{N - n +
    k}` を :math:`{N - n}` 単体であり、いずれも :math:`M` と交わるとすると、
    :ref:`4.4<tsuboi08.appendix.4.4>` と :ref:`4.5<tsuboi08.appendix.4.5>` によ
    り：

    .. math::

       \psi(\sigma^{N - n + k}) = \frac{1}{m}\sum_{i = 1}^m \psi(\tau_i).
