======================================================================
第 3 章 微分形式の積分 2/3
======================================================================

.. contents:: ノート目次

3.3 単体的ドラーム理論（展開）
======================================================================
目標は次のとおり：

* :math:`\varOmega^*(M)` の p 次元コホモロジー群と単体複体のコホモロジー群は一致する。
* 単体複体のコホモロジー群とホモロジー群は同次元の双対空間である。

これらが言えれば :math:`\H^p(M) \cong \RR^d` のときに
次の条件を満たす :math:`c_1, \dotsc, c_d \in Z_p^\infty(M)` が存在することになる：

.. math::

   \alpha \in Z^p(M), \alpha = \dd \beta \iff \int_{c_i}\!\alpha = 0.

3.3.1 単体複体
----------------------------------------------------------------------
有限単体複体を定義するために、記号と用語をいくつか導入する。

.. note::

   本書では頂点の記号に :math:`e_i` を用いているが、
   これをユークリッド空間の基底である必要がある勝手に勘違いしてしまったので、
   本ノート中は別の記号を割り当てる。

* k 次元単体 :math:`\langle v_{i_0} \dots v_{i_k}\rangle`

  k 次元単体とは :math:`\RR^k` 内の :math:`k + 1` 個の頂点で構成される凸包であり、
  各点は一般の位置にあるものとする。

  * 「各点が一般の位置にある」とは、例えば次のベクトルが一次独立であることを意味する：

    .. math::

       v_1 - v_0, v_2 - v_0, \dotsc, v_{k + 1} - v_0.

* `重心座標 <http://mathworld.wolfram.com/BarycentricCoordinates.html>`__
  :math:`(t_{i_0}, \dotsc, t_{i_k})`

  k 次元単体の点を :math:`\displaystyle \sum_{l = 0}^k t_{i_l} v_{i_l}` で表したときの
  基底に対する係数を組にした :math:`(t_0, \dotsc, t_k)` を重心座標と呼ぶ。

  * 各座標成分が非負であることと、座標成分の和が 1 であることに注意。

* k 次元単体の内部とは、重心座標のどの成分も正となるような点のなす部分と解釈する。
  特に境界は内部に含まれない。

.. _tsuboi08.3.3.1:

* 定義 3.3.1: `有限単体複体 <http://mathworld.wolfram.com/SimplicialComplex.html>`__

  * 単数または複数の k 次元単体からなる有限集合で、
    さらに次の条件を満たすものを有限単体複体という：

    1. 境界を構成するすべての :math:`k - 1` 単体も :math:`K` に含まれる。

       .. math::

          \langle v_{i_0} \dots v_{i_k}\rangle \in K \implies
          \langle v_{i_0} \dots v_{i_{l - 1}} v_{i_{l + 1}} \dots v_{i_k}\rangle \in K.

       この規則が再帰的に適用されるので、自動的に全頂点までも :math:`K` に含まれることになる。

    2. :math:`K` のどの二つの単体についても、それらの共通部分が :math:`K` に含まれる。

  * :math:`\displaystyle \abs{K} = \bigcup_{\sigma \in K}\sigma` を
    `幾何的実現 <http://mathworld.wolfram.com/GeometricRealization.html>`__ という。

    * ユークリッド空間の部分集合、点の集まりとして素朴に解釈すればよい。
    * したがって元は重心座標で表される。

..

* k チェイン

  * k チェインとは有限単体複体 :math:`K` を決めたときの、
    その k 単体の実係数有限線形結合である。
    記号 :math:`C_k(K)` で表す。

  * :math:`C_k(K)` は k 単体の個数と同じ次元のベクトル空間である。
    その個数を n とすると、次のように書ける：

    .. math::

       C_k(K) = \Set{\sum_{i = 1}^n a_i \sigma_i \Sth a_i \in \RR, \sigma_i \in K}.

..

* 境界、境界準同型

  * 単体 :math:`\sigma \in K` の境界 :math:`\partial \sigma` を次で定義する：

    .. math::

       \partial \sigma = \sum_{j = 0}^k(-1)^j \langle v_{i_0} \dots v{i_{j - 1}} v_{i_{j + 1}} \dots v_{i_k}\rangle.

    * 0 単体（頂点、点）の境界はゼロ、
    * 1 単体（辺、線分）の境界は 0 単体（頂点、点）、
    * 2 単体（面）の境界は 1 単体（辺、線分）、

    ……となる。というわけで

  * `境界準同型 or 境界演算子 <http://mathworld.wolfram.com/BoundaryOperator.html>`__
    :math:`\fn{\partial}{C_k(K)}C_{k - 1}(K)` が定義される。

  * :math:`\partial \circ \partial = 0` という性質がある。

..

* このゼロ準同型の性質より、複体 :math:`C_*(K)` が得られる：

  .. math::

     \require{AMScd}
     \begin{CD}
     0 @<{\partial}<< C_0(K) @<{\partial}<< C_1(K) @<{\partial}<< C_2(K) @<{\partial}<< \cdots
     \end{CD}

..

* さらに実係数ホモロジー群が得られる：

  .. math::

     H_k(K) = \ker(\fn{\partial}{C_k(K)}C_{k - 1}(K))
      /{\im(\fn{\partial}{C_{k + 1}(K)}{C_k(K)})}

  例によって :math:`Z_k(K) = \ker(\fn{\partial}{C_k(K)}C_{k - 1}(K))` をサイクル、
  :math:`\im(\fn{\partial}{C_{k + 1}(K)}{C_k(K)})` をバウンダリーと呼ぶ。

  実係数であることは、チェインを実係数で構成したことから来ている。

..

* k コチェイン

  * K の k 単体のなす有限集合上の実数値関数を k コチェインという。
  * k コチェインからなる有限次元ベクトル空間を :math:`C^k(K)` と書く。
  * :math:`C^k(K)` は :math:`C_k(K)` の双対ベクトル空間である。

..

* :math:`\fn{\delta}{C^k(K)}C^{k + 1}(K)` を次で定義する：

  .. math::

     (\delta c)(i_0, \dotsc, i_{k + 1})
     = \sum_{l = 0}^{k + 1}(-1)^l c(i_0, \dotsc, i_{l - 1}, i_{l + 1}, \dotsc, i_{k + 1})

  * :math:`(\delta c)(\sigma) = c(\delta \sigma)`
  * :math:`\delta \circ \delta = 0` が成り立つ。
    これは :math:`\partial \circ \partial = 0` による。

..

* :math:`K` のコホモロジー群は :math:`K` のコチェイン複体 :math:`C^*(K)` の
  コホモロジー群として定義される：

  .. math::

     \begin{CD}
     0 @>{\delta}>> C^0(K) @>{\delta}>> C^1(K) @>{\delta}>> C^2(K) @>{\delta}>> \cdots
     \end{CD}

  .. math::

     H^k(K) = \ker(\fn{\delta}{C^k(K)}C^{k + 1}(K))
      / \im(\fn{\delta}{C^{k - 1}(K)}C^k(K))

.. figure:: /_images/cd-topology-simplicial.png
   :align: center
   :alt: math.topology.algebraic.simplicial
   :width: 793px
   :height: 216px
   :scale: 100%

.. _tsuboi08.3.3.2:

* 定義 3.3.2: `オイラー標数 <http://mathworld.wolfram.com/EulerNumber.html>`__

  * :math:`\dim C_k(K) = \dim C^k(K)` は k 単体の個数 :math:`m_k` である。
  * :math:`K` の単体の次元が高々 n であるとき次の値を :math:`K` のオイラー（・ポアンカレ）標数という：

    .. math::

       \chi(K) = \sum_{k = 0}^n(-1)^k m_k.

.. _tsuboi08.3.3.3:

* 問題 3.3.3: :math:`\displaystyle \chi(K) = \sum_{k = 0}^n(-1)^k \dim H_k(K) = \sum_{k = 0}^n(-1)^k \dim H^k(K)`

  複体 :math:`C_*(K)` においては

  * :math:`\dim H_k(K) = \dim\ker \partial_k - \dim\im \partial_{k + 1}` と
  * 準同型定理 :math:`\dim\im\partial_{k + 1} = \dim C^{k + 1} - \dim\ker \partial_{k + 1}`

  を利用する。複体 :math:`C^*(K)` においても、上の二つに対応する性質を利用する。

.. _tsuboi08.3.3.4:

* 命題 3.3.4: :math:`\dim H_k(K) = \dim H^k(K)`

  こちらの証明は線形代数。内積を利用するようだ。

  1. :math:`C_*(K)` の基底を何かとって :math:`C_k(K)` が列ベクトル表示されるものとする。
  2. 境界準同型 :math:`\partial` を行列 :math:`A, B` を用いて表すものとする。
     このとき :math:`\partial \circ \partial = 0` から :math:`AB = O` を満たす。

     .. math::

        \begin{CD}
        C_{k - 1}(K) @<{\partial}<{A}< C_k(K) @<{\partial}<{B}< C_{k + 1}(K)
        \end{CD}

  3. 同時に :math:`C^*(K)` は行ベクトル表示されるものとする。
     これはコチェインが :math:`C_k(K)` 上の微分形式であることによる。
     準同型 :math:`\delta` は行ベクトルに作用するとみなせば同じ :math:`A, B` で表される：

     .. math::

        \begin{CD}
        C^{k - 1}(K) @>{\delta}>{A}> C^k(K) @>{\delta}>{B}> C^{k + 1}(K)
        \end{CD}

  4. :math:`C^k(K)` と :math:`C_k(K)` の間の「積」をユークリッド空間の内積として定義する。

  5. 直交補空間の性質をこの証明で利用したい。

     * 行列 :math:`A` を行ベクトル :math:`\bm a_i\ (i = 1, \dotsc, l)` を縦に並べたものとすると、
       :math:`\ker\partial = \operatorname{span}({}^t\!\bm a_1, \dotsc, {}^t\!\bm a_l)^\perp.`

     * 行列 :math:`B` を列ベクトル :math:`\bm b_i\ (i = 1, \dotsc, n)` を横に並べたものとすると、
       :math:`\im\partial = \operatorname{span}(\bm b_1, \dotsc, \bm b_n).`

     * :math:`\im\partial \subset \ker\delta`

     以上より次が成り立つ：

     .. math::

        \operatorname{span}(\bm b_1, \dotsc, \bm b_n)
        \subset \operatorname{span}({}^t\!\bm a_1, \dotsc, {}^t\!\bm a_l)^\perp.

  7. 一方、

     * :math:`\ker\delta = \operatorname{span}(\bm b_1, \dotsc, \bm b_n)^\perp,`
     * :math:`\im\delta = \operatorname{span}({}^t\!\bm a_1, \dotsc, {}^t\!\bm a_l),`
     * :math:`\im\delta \subset \ker\delta`

     以上より次が成り立つ：

     .. math::

        \operatorname{span}({}^t\!\bm a_1, \dotsc, {}^t\!\bm a_l)
        \subset \operatorname{span}(\bm b_1, \dotsc, \bm b_n)^\perp.

  8. ここで

     .. math::

        V = \operatorname{span}({}^t\!\bm a_1, \dotsc, {}^t\!\bm a_l)^\perp
          \cap \operatorname{span}(\bm b_1, \dotsc, \bm b_n)^\perp

     とおくと、

     .. math::

        \operatorname{span}({}^t\!\bm a_1, \dotsc, {}^t\!\bm a_l)^\perp
          /\operatorname{span}(\bm b_1, \dotsc, \bm b_n)
        \cong V
        \cong \operatorname{span}(\bm b_1, \dotsc, \bm b_n)^\perp
          /\operatorname{span}({}^t\!\bm a_1, \dotsc, {}^t\!\bm a_l).

     すなわち :math:`\ker\delta/\im\delta \cong V \cong \ker\delta/\im\delta` が成り立つ。
     したがって :math:`\dim H_k(K) = \dim H^k(K)` である。

.. _tsuboi08.3.3.5:

* 注意 3.3.5: :math:`C^k(K)` と :math:`C_k(K)` との間の積は
  :math:`H^k(K)` と :math:`H_k(K)` との間の積を引き起こす。

3.3.2 単体複体上の微分形式
----------------------------------------------------------------------
.. _tsuboi08.3.3.6:

* 定義 3.3.6: :math:`\varOmega^k(K),\ \H^*(K)`

  * :math:`\omega \in \varOmega^k(K)` を次の二点で定義する：

    * :math:`K` のすべての単体から、その上の k 形式への対応である：
      :math:`\sigma \longmapsto \omega_\sigma`

    * m 単体 :math:`\sigma` とその面である m - 1 単体 :math:`\tau` に対して
      :math:`\omega_\sigma|\tau = \omega_\tau` となる。

  * 外微分 :math:`\fn{\dd{}}{\varOmega^k(K)}\varOmega^{k+1}(K)` について

    * :math:`\dd{} \circ \dd{} = 0`
    * :math:`\H^*(K) = \ker{\dd{}}/\im{\dd{}}`

    が定義される。

..

* 2.10 節の理論を :math:`K` のドラーム複体 :math:`\varOmega^*(K)` に適用することができる。
  その結果 :math:`\H^*(K) \cong H^*(K)` と結論できる。

..

* 開星状体 :math:`O(v_i)` の定義中にある「単体の内部の和集合」がわからない。
  これは :math:`v_i \notin O(v_i)` を意味する？

3.3.3 単体的ドラームの定理
----------------------------------------------------------------------
* 単体上の積分が :math:`K` の :math:`\varOmega^*(K)` と :math:`C^*(K)` の関係を与える。
* :math:`\Delta^k` から :math:`\sigma = \langle e_{i_0} \dots e_{i_k}\rangle` への写像をやはり同じ記号で記す：

  .. math::

     \sigma(x_1, \dotsc, x_k)
     = (1 - x_1)e_{i_0} + (x_1 - x_2)e_{i_1}
     + \dotsb
     + (x_{k - 1} - x_k)e_{i_{k - 1}}
     + x_k e_{i_k}.

* 写像 :math:`\fnm{I}{\varOmega^*(K)}{C^*(K)}{(\omega, \sigma)}\int_\sigma\!\omega \in \RR` は
  :math:`K` の k コチェインを与える。

  * :math:`I` は :ref:`定理 3.2.1 <tsuboi08.3.2.1>` により、
    :math:`I \circ \dd{} = \delta \circ I` が成り立つコチェイン写像である。

.. _tsuboi08.3.3.7:

* 定理 3.3.7: 単体ドラームの定理

  :math:`I` は :math:`\H^*(K)` と :math:`H^*(K)` の間の同型写像を誘導する。

  1. コチェイン写像 :math:`\fn{s}{C^*(K)}\varOmega^*(K)` で
     :math:`I \circ s = \id_{C^*(K)}` を満たすものを考える。

     次の事実を利用する：

     * :math:`\fn{I}{\varOmega^*(K)}C^*(K)` は値 :math:`\displaystyle \int_\sigma\!\omega` を対応させる写像であり、
       :math:`I \circ \dd{} = \delta \circ I` である。

     * :math:`I` は準同型写像 :math:`\fn{I_*}{\H^*(?)}H^*(K)` を誘導する。
       さらに :math:`\H^*(?) \cong H^*(K)` および次元が有限であることから同型写像である。

     * :math:`s` は準同型写像 :math:`\fn{s_*}{H^*(K)}\H^*(?)` を誘導し、
       :math:`I_* \circ s_* = \id_{H^*(K)}` を満たす。

     :math:`c \in C^0(K)` に対し :math:`\varOmega^0(K)` の何が対応するのか、
     どのような :math:`\abs{K}` 上の関数であればよいのかを考える。
     それは頂点 :math:`e_i` で値 :math:`c(i)` をとる関数を線形に拡張するのがよい：

       :math:`\sigma = \langle e_{j_0} \dots e_{j_m}\rangle \in K` 上で
       :math:`\displaystyle s(c)_{\sigma} = \sum_{l = 0}^m c(j_l)t_{j_l}` である。

     :math:`\dd{s(c)_\sigma}` の計算をする：

     .. math::

        \begin{align*}
        \dd{s(c)_\sigma}
        &= \sum_{l = 0}^m c(j_l) \dd{t_{j_l}}\\
        &= \sum_{\set{i_0, i_1} \subset \set{j_0, \dotsc, j_m}}
               (c(i_0) - c(i_1))
               \omega_{i_0 i_1}.
        \end{align*}

     * 上の式変形には p. 107 の式やシグマの展開を行なう。

     ここで :math:`i_0 < i_1` としておく。
     上の式が :math:`\delta c` の像であるには
     :math:`\delta c(i_0, i_1) = c(i_0) - c(i_1)` であることから
     :math:`c^1 \in C^1(K)` に対して次のように定義できることが必要である：

     .. math::

        s(c^1)_\sigma = \sum_{\set{i_0, i_1} \subset \set{j_0, \dotsc, j_m}}
            c^1(i_0, i_1)
            \omega_{i_0 i_1}.

     一般の :math:`c \in C^k(K)` に対しては次のように :math:`s` を定義する：

     .. math::

        s(c)_\sigma = \sum_{\set{i_0, \dotsc, i_k} \subset \set{j_0, \dotsc, j_m}}
            c(i_0, \dotsc, i_k)
            \omega_{i_0 \dots i_k}
            \quad
            (m \ge k,\ \sigma = \langle e_{j_0} \dots e_{j_m}\rangle).

  2. :math:`\dd{}\circ s = s \circ \delta` を示す。
     そのために :math:`\dd{s(c)_\sigma} = s(\delta(c))_\sigma` を示す。

     * 最初の等号は上記 :math:`s(c)_\sigma` の定義に外微分を分配することによる。
     * 二番目の等号は標準 k 形式の外微分の定義 (p. 108) による。
     * 三番目の等号はシグマの展開か。
     * 四番目の等号は :math:`\delta` の定義 (p. 102) を当てはめる。
     * 最後の等号は上記 :math:`s(c)_\sigma` の定義で :math:`c` を :math:`\delta c` に
       置き換えると得られる。

  3. :math:`s(c)\ (c \in C^k(K))` を :math:`\sigma = \langle e_{i_0} \dots e_{i_k}\rangle` 上
     で積分するには、:math:`\sigma` を含む任意の単体
     :math:`\langle e_{j_0} \dots e_{j_m}\rangle` で次のようにする：

     .. math::

        \begin{align*}
        (I \circ s)(c)(i_0, \dotsc, i_k)
        &= \int\sigma\!
             \sum_{\set{l_0, \dotsc, l_k} \subset \set{j_0, \dotsc, j_m}}
             c(l_0, \dotsc, l_k)
             \omega_{l_0, \dotsc, l_k}\\
        &= \sum_{\set{l_0, \dotsc, l_k} \subset \set{j_0, \dotsc, j_m}}
             c(l_0, \dotsc, l_k)
             \int\sigma\!
             \omega_{l_0, \dotsc, l_k}\\
        &= c(i_0, \dotsc, i_k).
        \end{align*}

3.3.4 多様体の三角形分割と単体的ドラーム理論
----------------------------------------------------------------------
* 同相写像 :math:`\fn{\varphi}{\abs{K}}M` が各単体上で :math:`C^\infty` 級となるものを
  :math:`M` の :math:`C^\infty` 級 `三角形分割 <http://mathworld.wolfram.com/Triangulation.html>`__
  という。

* 次の三点により :math:`\varphi^*` が :math:`\H^*(M)` と :math:`\H^*(K)` の同型を与えている：

  * :math:`\H^*(M) \cong H^*(K).`
  * :math:`\H^*(K) \cong H^*(K),` 3.3.2 節参照。
  * :math:`\fn{\varphi^*}{\varOmega^*(M)}\varOmega^*(K)` の存在。

* :math:`\varOmega^*(K)` と :math:`C^*(K)` のコホモロジー群の同型も単体に沿う積分から誘導される。
* :math:`H_p(K)` の生成元 :math:`[c_1], \dotsc, [c_k]` に対し、
  :math:`\displaystyle \int_{c_i}\!\alpha = 0` となる :math:`\alpha \in Z^p(M)` は
  :math:`\alpha \in B^p(M)` を満たす。

* 三角形分割のとり方に依らないので :math:`\varOmega^*` と :math:`C^*` が等しい？
* オイラー標数は多様体に対して定まる量になっている。

3.4 向きを持つ多様体上の積分
======================================================================
* 直方体あるいは単体からの写像には自然に向きが定まっている。
* コンパクト n 次元多様体は n 次元単体からの :math:`C^1` 級の写像の像でうまく覆うことができる。
* 多様体に向きが定まっているときは、積分をすることができる。

.. _tsuboi08.3.4.1:

* 定義 3.4.1: `向き付けを持つ or 向き付け可能である多様体 <http://mathworld.wolfram.com/OrientableManifold.html>`__

  * 幾何学 I の :ref:`3.6 節 <tsuboi05.3.6>` を参照。

.. _tsuboi08.3.4.2:

* 定義 3.4.2: 向き付けられている多様体

  * ユークリッド空間には、その座標の順による向きが定まっている。
    例えば直方体の積分の定義にそれが表れている。

  * 向き付けを持つことと、向き付けられていることは別の概念であるらしい。
    上記のリンク先も参照。

.. _tsuboi08.3.4.3:

* 定義 3.4.3: 微分形式の台

  * 関数の台と定義は似ているが、:math:`\alpha(x)` という式が気になる。

..

:math:`\alpha \in \varOmega^n(M)` ということは :math:`\alpha = f(\bm x)\,\dd x_1 \wedge \dotsb \wedge \dd x_n`
となる多様体上の関数 :math:`f` が局所的に存在するということだ。
この局所座標近傍を :math:`(U, \varphi)` とし、コンパクト集合 :math:`K \subset U` をとる。
このときコンパクト集合 :math:`\varphi(K)` を有限個の disjoint な直方体で被覆できる。
この直方体の逆像を :math:`\kappa` とすると、次の式で積分をうまく定義できる：

.. math::

   \int_\kappa\!\alpha = \int_{\text{box}}\!f(\bm x)\,\dd x_1 \dots \dd x_n.

これを :math:`\alpha` の :math:`\varphi\inv` に沿う積分と呼ぶ。

.. _tsuboi08.3.4.4:

* 定義 3.4.4: :math:`U` のコンパクト部分 :math:`K` に台を持つ :math:`\alpha` の :math:`\varphi\inv` に沿う積分

  .. math::

     \int_{\varphi\inv}\!\alpha = \int_{\varphi(U)}\!f(\bm x)\,\dd x_1 \dots \dd x_n.

以下、多様体は向き付けられているものとする。

.. _tsuboi08.3.4.5:

* 命題 3.4.5: 座標近傍の取り方に依らない

  座標近傍 :math:`U, V` の共通部分のコンパクト部分集合 :math:`K` に台を持つ
  :math:`\alpha` の積分の値は等しい：

  .. math::

     \int_{\varphi\inv}\!\alpha = \int_{\psi\inv}\!\alpha.

  * :math:`(V, \psi)` から見て :math:`\alpha = g(\bm y)\,\dd y_1 \wedge \dotsb \wedge \dd y_n` と表す。
  * 座標変換 :math:`\varphi \circ \psi\inv` を考える：
    :math:`(\varphi \circ \psi\inv)(\bm y) = (x_1(\bm y), \dotsc, x_n(\bm y))`

    .. math::

       \begin{align*}
       g(\bm y)\,\dd y_1 \wedge \dotsb \wedge \dd y_n
       &= f(x_1(\bm y), \dotsc, x_n(\bm y))\,\dd x_1 \wedge \dotsb \wedge \dd x_n\\
       &= f(x_1(\bm y), \dotsc, x_n(\bm y)) \det\frac{\partial(x_1, \dotsc, x_n)}{\partial(y_1, \dotsc, y_n)}\,\dd y_1 \wedge \dotsb \wedge \dd y_n.
       \end{align*}

    ここまではよく見かける論証。

  * 積分は次のようになる：

    .. math::

       \begin{align*}
       \int_{\varphi\inv|\varphi(U \cap V)}\!\alpha
       &= \int_{\varphi(U \cap V)}\!f(\bm x)\,\dd x_1 \dots \dd x_n\\
       &= \int_{\psi(U \cap V)}\! f(x_1(\bm y), \dotsc, x_n(\bm y)) \Abs{\det{\frac{\partial(x_1, \dotsc, x_n)}{\partial(y_1, \dotsc, y_n)}}}\,\dd y_1 \dots \dd y_n\\
       &= \int_{\psi(U \cap V)}\! g(\bm y)\,\dd y_1 \dots \dd y_n\\
       &= \int_{\psi\inv|\psi(U \cap V)}\!\alpha.
       \end{align*}

    * 最初と最後の等号は :ref:`定義 3.4.4 <tsuboi08.3.4.4>` による。
    * 二番目の等号は重積分の変数変換か？
    * 三番目の等号は多様体が向き付けられていることにより、
      絶対値を取らなくても行列式の符号が正であることによる。

.. _tsuboi08.3.4.6:

* 命題 3.4.6: 向き付けられた二つの座標近傍系にそれぞれに従属する 1 の分割についての等式

  .. math::

     \sum_i \int_{\varphi\inv}\!\lambda_i\alpha =
     \sum_j \int_{\psi\inv}\!\mu_j\alpha.

  証明は、開被覆 :math:`\set{U_i \cap V_j}` およびそれに従属する
  1 の分割 :math:`\set{\lambda_i \mu_j}` を考えて
  :ref:`命題 3.4.5 <tsuboi08.3.4.5>` を用いる。

.. _tsuboi08.3.4.7:

* 定義 3.4.7: コンパクトで向き付けられた多様体上の微分形式の積分

  .. math::

     \int_M\!\alpha = \sum_i \int_{\varphi\inv}\!\lambda_i \alpha.

  * :math:`\set{(U_i, \varphi_i)}` に従属する 1 の分割を用いている。
  * この定義が well-defined であることは、
    :ref:`命題 3.4.6 <tsuboi08.3.4.6>` による。

.. _tsuboi08.3.4.8:

* 定理 3.4.8: ドラーム・コホモロジー群の性質

  * コンパクト・向き付けを持つ・連結 n 次元多様体 :math:`M` について :math:`\H^n(M) \cong \RR.`
  * 写像 :math:`\displaystyle \varOmega^n(M) \owns \alpha \longmapsto \int_M\!\alpha \in \RR` は
    同型写像 :math:`\H^n(M) \longto \RR` を誘導する。

  これがまともな準同型であることをまず示す。

  * :math:`\alpha` が向き付けを持つ :math:`(U, (x_1, \dotsc, x_n))` 上に台を持ち、
    非負関数を用いて :math:`\alpha = f\,\dd x_1 \wedge \dotsb \wedge \dd x_n` の形に書けるとする。

  * このときに :math:`\displaystyle \int_M\!\alpha > 0` となるから、ゼロ準同型ではない。

  あとは :math:`\H^n(M) \le 1` を示す。

  * 多様体の三角形分割を適用することで、
    :ref:`2.10 節 <tsuboi08.2.10>` の議論におけるコホモロジー群の同型と
    3.3.4 節の複体の同型により次が成り立つ：

    .. math::

       \dim \H^n(M) = \dim H^n(K).

  * また :ref:`命題 3.3.4 <tsuboi08.3.3.4>` により :math:`\dim H^n(K) = \dim H_n(K)` である。
  * ここがわからない。n サイクル :math:`\sum a_i \sigma_i` の図を用いた議論によって、
    この次元が高々 1 であることが観察できる。

.. _tsuboi08.3.4.9:

* 例題 3.4.9: モース関数を利用した :ref:`定理 3.4.8 <tsuboi08.3.4.8>` の証明

  :ref:`2.8 節 <tsuboi08.2.8>` で多用した技法を採用する。

  * :math:`\varnothing = N_0 \subset N_1 \subset \dotsb \subset N_k = M`
  * :math:`j < k` のとき :math:`N_{j - 1}\cap B_j` は空集合であるか、
    :math:`B^{n - m_j} \times S^{m_j}` と微分同相であり、
  * :math:`N_{k - 1} \cap B_k` は :math:`B^1 \times S^{n - 1}` と微分同相である。

  * :ref:`定理 2.8.1 <tsuboi08.2.8.1>` のマイヤー・ビエトリス完全系列を見ると、
    :math:`j < k` のとき :math:`\dim\H^n(N_j) = 0.`

  * よって :math:`\dim\H^n(M) \le 1.`

至るところゼロでない微分形式が存在するならば、多様体は向き付け可能である。

.. _tsuboi08.3.4.10:

* 命題 3.4.10: :math:`M` が境界なし・向き付け不可能・コンパクト・連結ならば
  :math:`\H^n(M) \cong H_n(K) \cong 0`

  :math:`M` は向き付け不可能であるが、
  :ref:`幾何学 I 3.6 節 <tsuboi05.3.6>` にあるように次のような多様体
  :math:`\widehat M` と写像 :math:`\varphi` がとれる：

  * :math:`\widehat M` は向き付け可能・連結であり、
  * 写像 :math:`\fn{\varphi}{\widehat M}\widehat M` は向きを反対にし、不動点がない。

    * :math:`\varphi \circ \varphi = \id_{\widehat M},`
    * :math:`\widehat M/\varphi \cong M.`

  ここで :math:`\alpha \in \varOmega^n(M)` をとり、
  射影を :math:`\fn{\pi}{\widehat M}M` とおく。

  * :math:`\pi = \pi \circ \varphi` ゆえ :math:`\varphi^*\pi^*\alpha = \pi^*\alpha.`
    したがって：

    .. math::

       \int_{\widehat M}\!\varphi^*\pi^*\alpha
       = \int_{\widehat M}\!\pi^*\alpha.

  * 写像 :math:`\varphi` の反変性により：

    .. math::

       \int_{\widehat M}\!\varphi^*\pi^*\alpha
       = -\int_{\widehat M}\!\pi^*\alpha.

  * この二つの等式より：

    .. math::

       \int_{\widehat M}\!\pi^*\alpha = 0.

  * ここで :ref:`定理 3.4.8 <tsuboi08.3.4.8>` により、
    :math:`\pi^*\alpha = \dd \beta \in \varOmega^n(M)`
    （外微分をオメガの元と見るのが新鮮）

  * :math:`\displaystyle \beta_1 = \frac{1}{2}(\beta + \varphi^*\beta) \in \varOmega^{n - 1}(\widehat M)` に対して、
    :math:`\varphi^*\beta_1 = \beta_1` より :math:`\beta_1 = \pi^*\beta_2 \in \varOmega^{n - 1}(\widehat M).`

  .. math::

     \begin{align*}
     \pi^*(\dd \beta_2) &= \dd(\pi^*\beta_2) = \dd \beta_1\\
     &= \frac{1}{2}\dd(\beta + \varphi^*\beta)\\
     &= \frac{1}{2}(\dd \beta + \varphi^* \dd \beta)\\
     &= \frac{1}{2}(\pi^*\alpha + \varphi^*\pi^*\alpha)\\
     &= \pi^*\alpha.
     \end{align*}

  :math:`\pi` が単射だからか :math:`\dd \beta_2 = \alpha` となる。

.. _tsuboi08.3.4.11:

* 命題 3.4.11: まとめ

  * :math:`\H^n(M)` は :math:`\RR` と同型またはゼロである。
  * :math:`M` が向き付け可能であることと、:math:`\H^n(M) \cong \RR` とが同値である。

  これは :ref:`定理 3.4.8 <tsuboi08.3.4.8>` および
  :ref:`命題 3.4.10 <tsuboi08.3.4.10>` をまとめたものだ。
