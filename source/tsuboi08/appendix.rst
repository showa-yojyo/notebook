======================================================================
付録 多様体の三角形分割の構成（展開）
======================================================================

* :ref:`定理 5.1.3 <tsuboi08.5.1.3>` の証明の概略。Whitney の
  `Geometric Integration Theory <https://press.princeton.edu/titles/3151.html>`__
  の内容を基にしているとのこと。

* 最初は :ref:`幾何学 I 定理 5.2.3 <tsuboi05.5.2.3>` にある、
  コンパクト多様体がユークリッド空間に埋め込み可能であることから出発する。

.. contents:: ノート目次

* \1. 証明の土台を準備する。

  * :math:`C^\infty` 級多様体を :math:`M` とし、コンパクトかつ n 次元であるとする。
  * :math:`M` はユークリッド空間 :math:`\RR^N` に埋め込まれるとする。
  * そのノルムを :math:`\norm{\cdot}` とする。
  * 点 :math:`p` の :math:`\delta` 近傍を :math:`B_\delta(p)` とする（開球と思ってよさそうだ）。

  本書では :math:`M` と :math:`M^n \in \RR^N` を区別しているらしいが、
  ここでは面倒なので単に :math:`M` で済ませる。

.. _tusboi08.appendix.1.1:

  * 1.1 :math:`\forall \eps > 0, \exists \delta > 0 \text{s.t. }\quad \forall x \in M:`

    * :math:`T_xM \cap B_\delta(x) \subset B_{\eps\delta}(M \cap B_\delta(x))` and
    * :math:`M \cap B_\delta(x) \subset B_{\eps\delta}(T_xM \cap B_\delta(x)).`

    本書図 A.1 はこれの :math:`N = 2` バージョンのイラストだ。
    円の直径が「接空間と開球の共通部分」に、内側の実線の円弧が「多様体と開球の共通部分」に
    それぞれ対応する。

    :math:`\fn{\pi_{T_xM}}{\RR^N}T_xM` を直交射影とする。

    * ノートでは以下字が潰れるので単に :math:`\pi` と書く。
    * この写像は像への微分同相写像である。
    * :math:`\pi(T_xM \cap B_\delta(x)) \supset T_xM \cap B_{\delta - \eps\delta}(x).`
      すなわち「図 A.1 の大円より小さい円を含む」か。

    :math:`\delta > 0` をもっと小さくとって次のようにできる：

    * :math:`y \in M \cap B_\delta(x)` における :math:`\bm v \in T_yM` に対して
      :math:`\norm{\bm v - \pi(\bm v)} \le \eps\norm\pi(\bm v) \le \eps\norm{\bm v}.`

    * :math:`y, z \in M \cap B_\delta(x)` に対して
      :math:`\norm{(y - \pi(y)) - (z - \pi(z))} \le \eps{\pi(y) - \pi(z)}.`

.. _tusboi08.appendix.1.2:

  * 1.2 :math:`M` のある近傍 :math:`U` をとれば、法束のゼロ切断の近傍と、
    法束からの指数写像で微分同相である。
    それゆえ :math:`U` で法束の射影 :math:`\fn{p_M}{U}M` が定義される。

    * :ref:`幾何学 I 問題 5.2.5 <tsuboi05.5.2.5>` による。

    :math:`x \in M` について :math:`B_\delta(x) \cap U` において、
    :math:`p_M|(B_\delta(x) \cap U)` のファイバーの方向と :math:`\pi` のそれは
    ほとんど等しい（それは納得できる）。

    特に :math:`\bm v` を :math:`U` の点における接ベクトルとし、
    :math:`\norm{\bm v - \pi(\bm v)} \le \dfrac{1}{2}` が成り立つならば、
    :math:`(p_M)_*\bm v \ne 0.`

.. _tusboi08.appendix.1.3:

  * 1.3 立方体の正則分割を定義する（本書図 A.2 の左側）。

    * 超立方体を単に立方体と書くことにしている。
    * 各次元版立方体の包含関係による列 :math:`I^0 \subset I^1 \subset \dotsb \subset I^N`
      に対応して、各重心 :math:`b_{I^0}, \dotsc, b_{I^k}` で構成される単体
      :math:`\langle b_{I^0} \dots b_{I^k}\rangle` が考えられる。

    空間 :math:`\RR^n` を辺長 :math:`\dfrac{2 \delta_0}{\sqrt{N}}` の立方体で細分し、
    すべての立方体の正則分割として得られる空間の単体分割を :math:`L` とする。

    * :math:`L` の N 単体の直径は :math:`\delta_0` である。

.. _tusboi08.appendix.1.4:

  * 1.4 標準単体 :math:`\Delta^n` について、
    次を満たす :math:`0 < \rho_0 < \dfrac{1}{2\sqrt{2}}` が何か存在する：

      :math:`\Delta^n` の各頂点をそれぞれから距離 :math:`\rho_0` 以内の
      点に移して得られる単体が、:math:`\Delta^n` と同相である。

    このような単体の直径は :math:`1 + 2\rho_0` 以下である。

    .. todo:: 

       ここでいったん保留。
       :math:`\rho_0` をある定数 :math:`H` 以上の値であるとする。

.. _tusboi08.appendix.1.5:

  * 1.5 空間内の半径 1 の球 :math:`B^N \subset \RR^N` に対して次が成り立つ：

    .. math::

       \forall \eps > 0 \exists \delta > 0 \quad\text{s.t. }
       \operatorname{vol}_N(B_\delta(A) \cap B^N) \le \eps\operatorname{vol}_N(B^N).

    ここで :math:`A` は次元が :math:`N - 1` 以下の affine 空間であり、
    :math:`\operatorname{vol}_N` は :math:`\RR^N` での「体積」とする。

    * 立方体分割の正則分割 1.3 の頂点に集まる単体の個数は、
      :math:`b_{I^N}` に交わる単体の個数を超えない。
      その個数を :math:`k_N` としておく。

    * :math:`\eps < \dfrac{1}{k_N}` に対して先ほどの体積不等式を満たす
      :math:`\delta_N` をとると、次の条件を満たす :math:`B^N` の点が何か存在する：

        点が affine 部分空間の和集合 :math:`\displaystyle \bigcup_{i = 1}^{k_N}\delta_N(A_i)`
        に含まれない。

.. _tusboi08.appendix.1.6:

  * 1.6 :math:`A_0 \subset A_1 \subset \RR^N` を affine 部分空間とし、
    :math:`\sigma \in A_1` を affine 単体とする。

    補集合の点 :math:`p \in \RR^N\setminus{A_1}` に対して次の集合を考える：

    .. math::

       p * \sigma = \set{(1 - t)p + ty \sth y \in \sigma,\ 0 \le t \le 1}

    * これを join と呼ぶ。
    * :math:`p * \sigma` は :math:`\dim\sigma + 1` 単体である。
    * 平面幾何的な理由によって（本書の図 A.3 に関する説明に相当）次の不等式が成り立つ：

      .. math::

         \dist(p * \sigma) \ge \frac{\dist(\sigma, A_0)\dist(p, A_1)}{\diam(p * \sigma)}.

.. _tusboi08.appendix.1.7:

  * 1.7 立方体分割の大きさ :math:`c` を次のように定める：

    .. math::

       c = \frac{\delta_N^{N - n}\rho_0^{N ^ n}}{2^{2(N - n)}(1 + 2\rho_0)^{N - n}}.

    ここで十分小さい :math:`a < 1` をとり（具体的な値は後で決める）

    .. math::

       \eps = \frac{ac^2}{4}

    とする。

    * 1.1 で得られる :math:`\delta` をこの :math:`\eps` による値とする。
    * 1.3 の直径 :math:`\delta_0` に対して :math:`\delta_0 = \dfrac{\delta}{2^3}` とする。

    * :math:`M` に交わる立方体分割の立体の 4 倍のスケールの立体は交点の :math:`\delta`
      近傍に含まれる。

    * :math:`T_xM \cap B_{8\delta_0}(x)` と :math:`M \cap B_{8\delta_0}(x)` は
      互いの :math:`8\eps\delta_0 = \dfrac{1}{2}ac^2\delta_0` 近傍にある。
      両者は実は数値的にはほとんど一致している。

* \2. 立方体分割の正則分割 :math:`L` を変形して、
  多様体に対して一般の位置にある三角形分割 :math:`\widehat{L}` を構成する。

* \3. 多様体と :math:`\widehat{L}` の位置関係を記述するための準備する。
* \4. 多様体と :math:`\widehat{L}` の交わり方と記述する。
* \5. 多様体の近くに単体複体 :math:`K` を構成する。
* \6. 法束の射影の制限が求める三角形分割であることを示す。
