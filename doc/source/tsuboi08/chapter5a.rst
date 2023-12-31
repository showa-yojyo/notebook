======================================================================
第 5 章 多様体の位相と微分形式 1/2
======================================================================

ホモロジーの話が多いが、不慣れなので別の本で補わないと苦しい。

.. contents:: ノート目次

* 曲率形式
* パフ形式、:math:`{2n \times 2n}` 行列を値とする。
* ガウス・ボンネの定理→偶数次元リーマン多様体に拡張。
* オイラー標数の定数倍
* 特性形式、ホモロジー類上での積分、次元＝次数、不変量。
* :ref:`命題 3.4.10<tsuboi08.3.4.10>` の考察：向き付けの有無と :math:`\H^n(M)`
  が :math:`\RR` と同型になるのか、ゼロと同型になるのかの対応関係。ポアンカレ双
  対定理はこれの拡張とみなせる。

5.1 多様体の三角形分割
======================================================================

5.1.1 組合せ多様体
----------------------------------------------------------------------

まず :ref:`定義 3.3.1<tsuboi08.3.3.1>` 前後を復習しておいたほうがいい。特に
:math:`k` 単体、単体複体、重心座標、幾何的表現、面、境界準同型などの用語の定義と
性質を思い出す必要がある。

* リンク

  * :math:`K` を単体複体とする。
  * 単体 :math:`{\tau \in K}` に対し、次の性質を満たす単体 :math:`{\sigma \in
    K}` の全体を :math:`\operatorname{Link}(\tau)` と書く：

    * :math:`{\tau \cap \sigma = \varnothing}`
    * :math:`\tau, \sigma` が共通のある一つの :math:`K` の単体の面となる。

.. _tsuboi08.5.1.1:

* 定義 5.1.1: 組合せ多様体 or PL 多様体

  * :math:`n` 次元単体複体 :math:`K` が :dfn:`組合せ多様体` or :dfn:`PL 多様体`
    であるとは、各 :math:`\tau \in K` に対し
    :math:`\abs{\operatorname{Link}(\tau)}` が球面 :math:`S^{n - p - 1}` と同相
    な :math:`{n - 1}` 次元組合せ多様体 or PL 多様体であることを言う。

  * この :math:`p` とは何だ？
  * 定義が再帰的に与えられている。

.. _tsuboi08.5.1.2:

* 注意 5.1.2: 単体複体 :math:`K` の頂点 :math:`v` について
  :math:`\abs{\operatorname{Link}(v)}` が :math:`S^{n - 1}` と同相であると言って
  いるのと同値である。
* 開星状体

  * この概念は 3.3.2 節で定義していた。
  * 単体複体の頂点 :math:`{v \in K}` に対して開集合 :math:`O(v)` を :math:`v` を
    頂点とする単体の内部全体の和集合として定義する。
  * :math:`K` が組合せ多様体であるときは :math:`O(v)` は開球 :math:`B^n` と同相で
    ある。

5.1.2 三角形分割
----------------------------------------------------------------------

:math:`C^\infty` 級多様体は三角形分割可能である。

.. _tsuboi08.5.1.3:

* 定義 5.1.3: :math:`C^\infty` `三角形分割 <https://en.wikipedia.org/wiki/Triangulation_(topology)>`__

  コンパクト :math:`n` 次元多様体 :math:`M` に対して、次の性質がある :math:`n`
  次元組合せ多様体 :math:`K` および同相写像 :math:`{\abs{K} \longto M}` が存在す
  る：

    各単体上で :math:`C^\infty` 級写像である。

  * 先の同相写像のほうを :math:`C^\infty` 三角形分割という。
  * 証明は付録で与えられる。

5.2 ポアンカレ双対原理
======================================================================

この節ではポアンカレ双対原理の主張を最初に述べて、その証明に必要な準備をして、最
後に証明を与えるという構成になっている。

.. _tsuboi08.5.2.1:

* 定理 5.2.1: ポアンカレ双対原理

  :math:`M` をコンパクトな向き付け可能 :math:`n` 次元多様体とする。このとき、
  チェイン複体のホモロジー群とコチェイン複体のコホモロジー群が同型である：

  .. math::

     H_{n - k}(M) \cong H^k(M).

  * 整数係数のホモロジー、コホモロジーに対して成り立つ（ので実数係数でも成り立
    つ）。
  * 証明は 5.2.7 節で与える。

5.2.1 基本類
----------------------------------------------------------------------

* `基本類 <http://mathworld.wolfram.com/FundamentalClass.html>`__

  * コンパクトで向き付け可能な連結 :math:`n` 次元多様体 :math:`M` のホモロジー群
    は :math:`\RR` と同型である。:ref:`定理 3.4.8<tsuboi08.3.4.8>` 参照。
  * :math:`K` を :math:`M` の三角形分割とし、:math:`\set{\sigma_i}` を :math:`n`
    次元単体全体とする。
  * :math:`n` チェイン :math:`\sum \sgn(\sigma_i)\sigma_i` に対して
    :math:`{\partial c = 0.}`

    * ただし :math:`\sgn` は向き付けられた :math:`M` と :math:`\sigma_i` との向
      きの一致を示す符号とする（もちろん一致していればプラスとする）。
    * この :math:`c` 上での積分は :math:`M` 上でのそれと一致する：

      .. math::

         \fn{\int_c = \int_M}{\H^n(M)}\RR`

    * この :math:`c` は :math:`M` の :math:`\ZZ` 係数ホモロジー群の元を代表して
      いる。その元を :math:`[M]` で表し、これを基本類と呼ぶ。

5.2.2 重心細分
----------------------------------------------------------------------

:math:`K` を単体複体とする。

.. _tsuboi08.5.2.2:

* 定義 5.2.2: `重心細分
  <https://en.wikipedia.org/wiki/Barycentric_subdivision>`__

  * 以下、単体 :math:`{\tau \in K}` の重心を :math:`b_\tau` のように表す。
  * 重心細分 :math:`\bsd(K)` とは、次の性質がある :math:`k` 単体全体であるとす
    る：

    .. math::

       \langle b_{\tau^{m_0}} \dots b_{\tau^{m_k}} \rangle

    ただし :math:`\tau^{m_0}, \dotsc, \tau^{m_k}` とは :math:`K` の相異なる次元
    の単体であり、:math:`\tau^{m_{i - 1}}` が :math:`\tau^{m_i}` の面となる。

    * この単体列における単体同士の包含関係のようなものを :math:`{\tau^{m_{i -
      1}} \prec \tau^{m_i}}` と書く。本書で明示的には言っていないが、これは半順
      序になるようだ。

* 重心細分 :math:`\bsd(K)` は単体複体である。
* 両者の幾何的表現は同じものである：

  .. math::

     \abs{\bsd(K)} = \abs{K}.

* 単体の符号

  次のように取り決める。この規約がチェインの記述に必要となる：

  .. math::

     \langle e_{j_0} \dots e_{j_k} \rangle = \sgn
     \begin{pmatrix}
     i_0 & \cdots & i_k\\
     j_0 & \cdots & j_k
     \end{pmatrix}
     \langle e_{i_0} \dots e_{i_k} \rangle

* :math:`\fn{\bsd}{C_*(K)}C_*(\bsd(K))` からホモロジー群の同型
  :math:`\fn{\bsd_*}{H_*(K)}H_*(\bsd(K))` が得られる。

  * :math:`\bsd(K)` の :math:`k` 単体のうち、:math:`{\langle e_{i_0} \dots
    e_{i_k}\rangle \in K}` を重心細分して得られるものを記述したい。

  1. 添字の置換を :math:`{J = j_0 \dots j_k}` とおく。
  2. :math:`m\quad{(m = 0, 1, \dotsc, k)}` 単体を :math:`\tau^m = \tau^m(J) =
     {\langle e_{j_0} \dots e_{j_k}\rangle}` で定義する。
  3. \2. から単体の列が得られる。この各列が :math:`J` と一対一対応する：

     .. math::

        \tau^0 \prec \dotsb \prec \tau^k.

  4. このとき :math:`{\langle b_{\tau^0}\dots b_{\tau^k}\rangle} \in \bsd(K).`
  5. 単体の列に符号を定義する：

     .. math::

        \sgn(\tau^0 \prec \dotsb \prec \tau^k) = \sgn
        \begin{pmatrix}
        0 & \cdots & k\\
        j_0 & \cdots & j_k
        \end{pmatrix}.

     右辺 2 行目の並びは置換 :math:`J` だ。

  6. 次の和は符号を込めて単体 :math:`{\langle e_{i_0} \dots e_{i_k}\rangle}` を
     表現している：

     .. math::

        \sum_{\tau^0 \prec \dotsb \prec \tau^k = \langle e_{i_0} \dots e_{i_k}\rangle}
        \sgn(\tau^0 \prec \dotsb \prec \tau^k) \langle b_{\tau^0}\dots b_{\tau^k}\rangle.

     * シグマ記号の下、メモミス？
     * 各項 :math:`{\langle e_{i_0} \dots e_{i_k}\rangle}` の向きと一致する。

5.2.3 双対胞体
----------------------------------------------------------------------

* :math:`n` 次元組合せ多様体 :math:`M` の三角形分割を :math:`K` とする。重心細分
  :math:`\bsd(K)` の各頂点 :math:`b_\tau` に対して :math:`O(b_\tau) \cong B^n` が
  成り立つ。

以下、重心細分 :math:`\bsd(K)` と三角形分割 :math:`K` との関係を考える。

.. _tsuboi08.5.2.3:

* 定義 5.2.3: `双対胞体
  <https://en.wikipedia.org/wiki/Dual_polyhedron#Dual_polytopes_and_tessellations>`__

  :math:`k` 単体 :math:`{\tau^k \in K}` に対して、次元が 1 ずつ増加する単体列：

  .. math::

     \tau^k \prec \tau^{k + 1} \prec \dotsb \prec \tau^n

  の全体を考える。この列それぞれに対して、:math:`{n - k}` 単体 :math:`{\langle
  b_{\tau^k} \dots b_{\tau^n}\rangle}` をとり、その和集合を :math:`\tau^{k*}` と
  する。

  * 一般的な状況を記述しているため、直観的にわかりづらい。

* :math:`\tau^{k*}` は :math:`\operatorname{Link}(\tau^k)` の :math:`b_{\tau^k}`
  を頂点とする錐体の単体と同型である。
* :math:`\tau^{k*}` は閉球 :math:`B^{n - k}` と同相である。
* 組合せ多様体はその単体分割の双対胞体を持つ。
* :math:`M` が向き付けられていれば、:math:`M` の :math:`b_{\tau^k}` における向き
  が定まるように双対胞体の向きとれる。

5.2.4 単体の向き
----------------------------------------------------------------------

:math:`k` 単体の向きは、それに接する :math:`k` 個の一次独立なベクトル、:math:`k`
枠、で表される。

* 単体の各頂点が一直線上に並んでいないのでこのようなものを考えられる。

.. _tsuboi08.5.2.4:

* 定義 5.2.4: :math:`{\langle v_0 \dots v_k\rangle}` の向き

  * :math:`v_0, \dotsc, v_k \in \RR^N` を頂点とする :math:`k` 単体に対
    し、:math:`k` 枠 :math:`{(v_1 - v_0, v_2 - v_1, \dotsc, v_k - v_{k - 1})}`
    がその向きを定めるとする。
  * この向きは :math:`k` 枠 :math:`{(v_1 - v_0, v_2 - v_0, \dotsc, v_k - v_{k -
    0})}` が定める向きと同じである。:math:`n` 単体 :math:`{\langle v_0 \dots
    v_n\rangle}` の部分 :math:`k` 単体とみなせることに注意。
  * :math:`{\langle b_{\tau^0} \dots b_{\tau^n}\rangle} \in \bsd(\tau^n)` の向きと
    :math:`{\langle v_0 \dots v_k\rangle}` の向きは同じ。

* 境界準同型メモ

  * :math:`{\partial \tau^k}` を展開したときの :math:`\tau^{k - 1}` の係数は
    :math:`(-1)^k` である。
  * :math:`{\partial\langle b_{\tau^{k - 1}}b_{\tau^k}\dots b_{\tau^n}\rangle}`
    を展開したときの :math:`{\langle b_{\tau^k}\dots b_{\tau^n}\rangle}` の係数
    は 1である。

5.2.5 多様体の向きと単体の向き
----------------------------------------------------------------------

* 基本類 :math:`[M]` は次の和で代表される：

  .. math::

     \sum_\sigma \sgn_M(\sigma)\sigma.

  * ただし :math:`{\sigma = \langle e_{j_0}\dots e_{j_n}\rangle.}`
  * ただし :math:`\sgn_M(\sigma)` とは、:math:`M` と :math:`{\sigma \in K}` の向
    きが一致するか否かで 1 または -1 をとるものとする。

* 双対胞体 :math:`\tau^{k*}` の向き

  * :math:`{\tau^k = \langle v_0 \dots v_k\rangle}` とおく。
  * :math:`{\tau^k \prec \tau^n = \langle v_0 \dots v_n\rangle}` に対して
    :math:`{\tau^l = \langle v_0 \dots v_l\rangle}` とおく（意味不明）。

    * :math:`\tau^k` が向きが正の単体のときは :math:`{\langle b_{\tau^k}\dots
      b_{\tau^n}\rangle}` と向きが同じ単体を、
    * :math:`\tau^k` が向きが負の単体のときは :math:`{\langle b_{\tau^k}\dots
      b_{\tau^n}\rangle}` と逆向きの単体を

    考えた和をとる。

  * 本書図 5.5 の解釈に注意したい。一単体 :math:`{\langle v_0 v_1\rangle}` から
    三単体 :math:`{\langle v_0 v_1 v_2 v_3\rangle}` に至る列（というか経路）が複
    数ありそうだ。例えば：

    .. math::

       \begin{align*}
       \langle v_0 v_1\rangle \prec \langle v_0 v_1 v_2\rangle \prec \langle v_0 v_1 v_2 v_3\rangle\\
       \langle v_0 v_1\rangle \prec \langle v_0 v_2 v_3\rangle \prec \langle v_0 v_1 v_2 v_3\rangle
       \end{align*}

.. _tsuboi08.5.2.5:

* 定義 5.2.5: 双対胞体

  チェインバージョン。

  * :math:`M` を向き付けられた :math:`n` 次元多様体、
  * :math:`K` を :math:`M` の三角形分割、
  * :math:`{\tau^k = \langle v_0 \dots v_k \rangle \in K}` に対して、
    :math:`{\tau^k \prec \tau^n = \langle v_0 \dots v_n \rangle \in K}` を考え、
    さらに

    .. math::

       \tau^l = \langle v_0 \dots v_l \rangle\quad(l = k, \dotsc, n)

  とする。このとき :math:`\tau^{k*}` を次で定義する：

  .. math::

     \begin{align*}
     \langle v_0 \dots v_k \rangle^* =
     \sum_{\langle v_0 \dots v_k \rangle \prec \langle v_0 \dots v_n \rangle}
     \sgn_M(\langle v_0 \dots v_n \rangle)
     \langle b_{\tau^k}\dots b_{\tau^n}\rangle
     \in C_{n - k}(K).
     \end{align*}

  .. todo::

     記号が間違っている可能性が大。なぜなら :math:`l` が出て来ないから。

.. _tsuboi08.5.2.6:

* 補題 5.2.6: 双対胞体の境界は双対胞体の和で表せる

  .. math::

     \partial\langle v_0 \dots v_{k - 1} \rangle^* =
     \sum_{\langle v_0 \dots v_{k - 1} \rangle \prec \langle v_0 \dots v_n \rangle}
     \langle v_0 \dots v_k \rangle^*

  記号の使い方を何か工夫したいところだ。

  .. math::

     \begin{align*}
     \text{LHS}
     &= \sum_{(1)} \sgn_M(\langle v_0 \dots v_n\rangle) \partial\langle b_{\tau^{k - 1}}\dots b_{\tau^n}\rangle\\
     &= \sum_{(1)}\sum_{(2)} \sgn_M(\langle v_0 \dots v_n\rangle) \partial\langle b_{\tau^{k - 1}}\dots b_{\tau^n}\rangle\\
     &= \sum_{(1)}\sum_{(2)} \sgn_M(\langle v_0 \dots v_n\rangle) \partial\langle b_{\tau^k}\dots b_{\tau^n}\rangle\\
     &= \text{RHS}.
     \end{align*}

  和の (1), (2) はそれぞれ次のとおり：

  * \(1) :math:`{\langle v_0 \dots v_{k - 1} \rangle \prec \langle v_0 \dots v_n
    \rangle}`
  * \(2) :math:`{\langle v_0 \dots v_k \rangle \prec \langle v_0 \dots v_n
    \rangle}`

  1. 最初の等号は :ref:`定義 5.2.5<tsuboi08.5.2.5>` をそのまま適用した？
     :math:`\sgn` は :math:`\partial` の影響を受けないのでシグマの中に入れたの
     か？
  2. 二番目の等号でシグマが増えている。これは何だ？
  3. 本書によると三番目の等号は次の場合分けの考察による：

     * :math:`{k \lt l \lt n}` のとき

       :math:`{\sgn_M(\langle v_0 \dots v_{l - 1} v_l \dots v_n
       \rangle)\partial\langle\dots\rangle}` の展開式中の項

       .. math::

          \sgn_M(\langle v_0 \dots v_{l - 1} v_l \dots v_n \rangle)
          (-1)^{l - k - 1}\langle\dots b_{\tau^{l - 2}} b_{\tau^l} \dots\rangle

       と :math:`{\sgn_M(\langle v_0 \dots v_l v_{l - 1} \dots v_n
       \rangle)\partial\langle\dots\rangle}` の展開式中の項

       .. math::

          \sgn_M(\langle v_0 \dots v_l v_{l - 1} \dots v_n \rangle)
          (-1)^{l - k - 1}\langle\dots b_{\tau^{l - 2}} b_{\tau^l} \dots\rangle

       のペアがキャンセルし合う。

     * :math:`{l = n}` のとき

       :math:`{\langle v_0 \dots v_{n - 1} v_n\rangle}` に対して
       :math:`{\operatorname{Link}(\langle v_0 \dots v_{n - 1} v_n\rangle)}` が
       :math:`S^0` と同相であることより、これは二点からなる。

       ある :math:`{v_n' \in K}` が存在して :math:`{\langle v_0 \dots v_{n - 1}
       v_n'\rangle}` が単体として存在して、:math:`{\langle v_0 \dots v_{n - 1}
       v_n\rangle}` と :math:`{\langle v_0 \dots v_{n - 1}\rangle}` を共有する。

       .. math::

          \sgn_M(\langle v_0 \dots v_{n - 1} v_n\rangle)
          \sgn_M(\langle v_0 \dots v_{n - 1} v_n'\rangle)
          = -1.

       ゆえに

       .. math::

          \sgn_M(\langle v_0 \dots v_{n - 1} v_n\rangle)
          (-1)^{n - k - 1}
          \langle b_{\tau^{k - 1}} \dots b_{\tau^{n - 1}}\rangle
          +
          \sgn_M(\langle v_0 \dots v_{n - 1} v_n'\rangle)
          (-1)^{n - k - 1}
          \langle b_{\tau^{k - 1}} \dots b_{\tau^{n - 1}}\rangle
          = 0.

     全然わからない。添字がわからない。

5.2.6 双対胞体のなす複体のホモロジー
----------------------------------------------------------------------

* :math:`C_l(K^*)` を :math:`{n - l}` 単体の双対胞体を基底とする加群（自由
  :math:`\ZZ` または :math:`\RR` ベクトル）とする。
* 境界準同型 :math:`\fn{\partial}{C_l(K^*)}C_{l - 1}(K^*)` を p. 101 の要領で定
  義する。

.. _tsuboi08.5.2.7:

* 問題 5.2.7: :math:`{\partial \circ \partial = 0}`

  1. :math:`\displaystyle {\partial(\partial(\langle v_0 \dots v_n\rangle^*) =
     \sum_{\langle v_0 \dots v_{k - 1}\rangle \prec \langle v_0 \dots
     v_n\rangle}\partial\langle v_0 \dots v_n\rangle^*.}`
  2. :math:`\displaystyle {\partial\langle v_0 \dots v_k\rangle^* =
     \sum_{\langle v_0 \dots v_k\rangle \prec \langle v_0 \dots v_{k +
     1}\rangle} \langle v_0 \dots v_{k + 1}\rangle^*.}`
  3. :math:`{\langle v_0 \dots v_{k - 1}\rangle \prec \langle v_0 \dots v_{k +
     1}\rangle}` ならば次の半順序関係が成り立つ：

     .. math::

        \begin{align*}
        \langle v_0 \dots v_{k - 1}\rangle &\prec \langle v_0 \dots v_{k - 1} v_k\rangle       &\prec \langle v_0 \dots v_{k - 1} v_k v_{k + 1}\rangle\\
        \langle v_0 \dots v_{k - 1}\rangle &\prec \langle v_0 \dots v_{k - 1} v_{k + 1}\rangle &\prec \langle v_0 \dots v_{k - 1} v_k v_{k + 1}\rangle
        \end{align*}

  4. \3. の最初の半順序関係から得られる 1. の展開式中の :math:`{\langle v_0
     \dots v_{k + 1}\rangle}^*` の係数はプラスである。一方、3. の二番目の半順序
     関係から偉えるそれはマイナスであるから、それは :math:`{\partial \circ
     \partial = 0}` を意味する。

  この証明もよくわからない。

* :ref:`補題 5.2.6<tsuboi08.5.2.6>` は包含写像 :math:`{C_l(K^*) \longto
  C_l(\bsd(K))}` がチェイン写像であると言っている。
* :math:`K^*` と :math:`\bsd(K)` を有限胞体複体であると考えると、ホモロジー群は
  :math:`M` の特異ホモロジー群と同型であることが、ホモロジー群の教科書に書いてあ
  るらしい。

  * 特異ホモロジー群は p. 99 でやった。

* この包含写像がホモロジー群の同型を導くらしい。

5.2.7 ポアンカレの双対定理の証明
----------------------------------------------------------------------

準備が整ったので :ref:`定理 5.2.1<tsuboi08.5.2.1>` の証明を与える。

1. :math:`\fn{C_k(K)}C_{k - 1}(K)` を表す :math:`{k - 1 \times k}` 行列を
   :math:`{A = (a_{ij})}` とする：

   .. math::

      \partial\sigma_j^k = \sum_{i = 1}^{n_{k - 1}} a_{ij}\sigma_i^{k - 1}
      \quad(j = 1, \dotsc, n_k).

2. すると :math:`\fn{\partial}{C_{n - k + 1}(K^*)}C_{n - k}(K^*)` を表す行列は
   :math:`{(-1)^k {}\!^tA = ((-1)^k a_{ji})}` となる。
3. 行列は :math:`{(-1)^k {}\!^tA}` は写像 :math:`\fn{(-1)^k\delta}{C^{k -
   1}(K)}C^k(K)`を表すものである（これを示すのに :ref:`補題 5.2.6
   <tsuboi08.5.2.6>` を用いる）：

   .. math::

      \require{amscd}
      \begin{CD}
      @>{\partial}>> C_{n - k + 1}(K^*) @>{\partial}>> C_{n - k}(K^*) @>{\partial}>> C_{n - k - 1}(K^*) @>{\partial}>>\\
      @. @VVV @VVV @VVV\\
      @>{(-1)^{k - 1}\delta}>> C^{k - 1}(K) @>{(-1)^k\delta}>> C^k(K) @>{(-1)^{k + 1}\delta}>> C^{k + 1}(K) @>{(-1)^{k + 2}\delta}>>
      \end{CD}

したがって :math:`{H_{n - k}(K^*) \cong H^k(K)}` が成り立つ。

.. _tsuboi08.5.2.8:

* 注意 5.2.8: この証明は向き付けを持たない閉多様体に対して、:math:`{\ZZ/2\ZZ}`
  係数のポアンカレ双対定理が成立する。

.. _tsuboi08.5.2.9:

* 問題 5.2.9: 奇数次元コンパクト向き付け可能多様体はオイラー標数がゼロ

  1. コンパクト向き付け可能多様体を :math:`M` とし、:math:`{\dim M = 2n + 1}` と
     おく。
  2. オイラー標数を計算する：

     .. math::

        \begin{align*}
        \chi(M)
        &= \sum_{k = 0}^{2n + 1} (-1)^k \dim H^k(M)\\
        &= \left(\sum_{k = 0}^n + \sum_{k = n + 1}^{2n + 1}\right)(-1)^k \dim H^k(M)\\
        &= \sum_{k = 0}^n(-1)^k \dim H^k(M) + \sum_{k = n + 1}^{2n + 1}(-1)^k \dim H^{2n + 1 - k}(M)\\
        &= \sum_{k = 0}^n(-1)^k \dim H^k(M) + \sum_{k = 0}^n (-1)^{2n + 1 - k} \dim H_k(M)
        \end{align*}

     * 最初の等号は :ref:`問題 3.3.3<tsuboi08.3.3.3>` による。
     * 二番目の等号はシグマを前半と後半とに分割した。
     * 三番目の等号にポアンカレ双対定理を間接的に使用してあるようだ。
     * 最後の等号にポアンカレ双対定理、添字調整、:ref:`命題
       3.3.4<tsuboi08.3.3.4>` を使用してあるようだ。
