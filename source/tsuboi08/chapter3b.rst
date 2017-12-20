======================================================================
第 3 章 微分形式の積分 2/3
======================================================================

.. contents:: ノート目次

3.3 単体的ドラーム理論（展開）
======================================================================
目標は次のとおり：

* :math:`\Omega^*(M)` の p 次元コホモロジー群と単体複体のコホモロジー群は一致する。
* 単体複体のコホモロジー群とホモロジー群は同次元の双対空間である。

これらが言えれば :math:`\H^p(M) \cong \RR^d` のときに
次の条件を満たす :math:`c_1, \dotsc, c_d \in Z_p^\infty(M)` が存在することになる：

.. math::

   \alpha \in Z^p(M), \alpha = \dd \beta \iff \int_{c_i}\!\alpha = 0.

3.3.1 単体複体
----------------------------------------------------------------------
有限単体複体を定義するために、記号と用語をいくつか導入する。

* :math:`\RR^N` の基底を :math:`e_1, \dotsc, e_N` とする。
  ここでは太字にしない。

* k 次元単体 :math:`\langle e_{i_0} \dots e_{i_k}\rangle`

  ここに書いた点を頂点とする凸包であり、添字を昇順に配列するものとする。

* `重心座標 <http://mathworld.wolfram.com/BarycentricCoordinates.html>`__
  :math:`(t_{i_0}, \dotsc, t_{i_k})`

  k 次元単体の点を :math:`\displaystyle \sum_{l = 0}^k t_{i_l} e_{i_l}` で表したときの
  基底に対する係数を組にしたものを重心座標と呼ぶ。

  * 各座標成分が非負であることと、座標成分の和が 1 であることに注意。

* k 次元単体の内部とは、重心座標のどの成分も正となるような点のなす部分と解釈する。
  特に境界は内部に含まれない。

.. _tsuboi08.3.3.1:

* 定義 3.3.1: `有限単体複体 <http://mathworld.wolfram.com/SimplicialComplex.html>`__

  * 上記の k 次元単体からなる有限集合で、さらに次の条件を満たすものを有限単体複体という：

      :math:`\langle e_{i_0} \dots e_{i_k}\rangle \in K` ならば、
      :math:`\langle e_{i_0} \dots e_{i_{l - 1}} e_{i_{l + 1}} \dots e_{i_k}\rangle \in K` である。

    つまり、各面も :math:`K` にいなければならない。

  * :math:`\displaystyle \abs{K} = \bigcup_{\sigma \in K}\sigma` を
    `幾何的実現 <http://mathworld.wolfram.com/GeometricRealization.html>`__ という。

    * 元は重心座標で表される。
    * この概念はよくわからない。

..

* k チェイン

  * k チェインとは有限単体複体 :math:`K` の k 単体の実係数有限線形結合である。
  * k チェインの集合を次で記す：

    .. math::

       C_k(K) = \Set{\sum_i^{\text{finite}}a_i \sigma_i \Sth a_i \in \RR, \sigma_i \in \abs{K}}.

  * :math:`C_k(K)` は k 単体の個数と同じ次元のベクトル空間である。

..

* 境界 :math:`\displaystyle \partial \sigma = \sum_{j = 0}^k(-1)^j \langle e_{i_0} \dots e_{i_{j - 1}} e_{i_{j + 1}} \dots e_{i_k}\rangle`

  * `境界準同型 <http://mathworld.wolfram.com/BoundaryOperator.html>`__
    :math:`\fn{\partial}{C_k(K)}C_{k - 1}(K)` が定義される。

  * :math:`\partial \circ \partial = 0.`

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
      / \im(\fn{\partial}{C_{k + 1}(K)}{C_k(K)})

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

.. _tsuboi08.3.3.5:

* 注意 3.3.5: :math:`C^k(K)` と :math:`C_k(K)` との間の積は
  :math:`H^k(K)` と :math:`H_k(K)` との間の積を引き起こす。

3.3.2 単体複体上の微分形式
----------------------------------------------------------------------
* 定義 3.3.6: :math:`\Omega^k(K),\ \H^*(K)`

  * :math:`\omega \in \Omega^k(K)` を次の二点で定義する：

    * :math:`K` のすべての単体から、その上の k 形式への対応である：
      :math:`\sigma \longmapsto \omega_\sigma`

    * m 単体 :math:`\sigma` とその面である m - 1 単体 :math:`\tau` に対して
      :math:`\omega_\sigma|\tau = \omega_\tau` となる。

  * 外微分 :math:`\fn{\dd{}}{\Omega^k(K)}\Omega^{k+1}(K)` について

    * :math:`\dd{} \circ \dd{} = 0`
    * :math:`\H^*(K) = \ker{\dd{}}/\im{\dd{}}`

    が定義される。

..

* 2.10 節の理論を :math:`K` のドラーム複体 :math:`\Omega^*(K)` に適用することができる。
  その結果 :math:`\H^*(K) \cong H^*(K)` と結論できる。

..

* 開星状体 :math:`O(e_i)` の定義中にある「単体の内部の和集合」がわからない。
  これは :math:`e_i \notin O(e_i)` を意味する？

3.3.3 単体的ドラームの定理
----------------------------------------------------------------------
* 単体上の積分が :math:`K` の :math:`\Omega^*(K)` と :math:`C^*(K)` の関係を与える。
* :math:`\Delta^k` から :math:`\sigma = \langle e_{i_0} \dots e_{i_k}\rangle` への写像をやはり同じ記号で記す：

  .. math::

     \sigma(x_1, \dotsc, x_k)
     = (1 - x_1)e_{i_0} + (x_1 - x_2)e_{i_1}
     + \dotsb
     + (x_{k - 1} - x_k)e_{i_{k - 1}}
     + x_k e_{i_k}.

* 写像 :math:`\fnm{I}{\Omega^*(K)}{C^*(K)}{(\omega, \sigma)}\int_\sigma\!\omega \in \RR` は
  :math:`K` の k コチェインを与える。

  * :math:`I` は :ref:`定理 3.2.1 <tsuboi08.3.2.1>` により、
    :math:`I \circ \dd{} = \delta \circ I` が成り立つコチェイン写像である。

.. _tsuboi08.3.3.7:

* 定理 3.3.7: 単体ドラームの定理

  :math:`I` は :math:`\H^*(K)` と :math:`H^*(K)` の間の同型写像を誘導する。

  * ここの証明と準備がわからない。

    * :math:`s`,
    * :math:`I_*`,
    * 標準 k 形式 :math:`\omega_{i_0 \dots i_k}`,
    * 複雑な和のとり方

3.3.4 多様体の三角形分割と単体的ドラーム理論
----------------------------------------------------------------------
* 同相写像 :math:`\fn{\varphi}{\abs{K}}M` が各単体上で :math:`C^\infty` 級となるものを
  :math:`M` の :math:`C^\infty` 級 `三角形分割 <http://mathworld.wolfram.com/Triangulation.html>`__
  という。

* 次の三点により :math:`\varphi^*` が :math:`\H^*(M)` と :math:`\H^*(K)` の同型を与えている：

  * :math:`\H^*(M) \cong H^*(K).`
  * :math:`\H^*(K) \cong H^*(K),` 3.3.2 節参照。
  * :math:`\fn{\varphi^*}{\Omega^*(M)}\Omega^*(K)` の存在。

* :math:`\Omega^*(K)` と :math:`C^*(K)` のコホモロジー群の同型も単体に沿う積分から誘導される。
* :math:`H_p(K)` の生成元 :math:`[c_1], \dotsc, [c_k]` に対し、
  :math:`\displaystyle \int_{c_i}\!\alpha = 0` となる :math:`\alpha \in Z^p(M)` は
  :math:`\alpha \in B^p(M)` を満たす。

* 三角形分割のとり方に依らないので :math:`\Omega^*` と :math:`C^*` が等しい？
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

:math:`\alpha \in \Omega^n(M)` ということは :math:`\alpha = f(\bm x)\,\dd x_1 \wedge \dotsb \wedge \dd x_n`
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
  * 写像 :math:`\displaystyle \Omega^n(M) \owns \alpha \longmapsto \int_M\!\alpha \in \RR` は
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

  ここで :math:`\alpha \in \Omega^n(M)` をとり、
  射影を :math:`\fn{\pi}{\widehat M}M` とおく。

  * :math:`\pi = \pi \circ \varphi` ゆえ :math:`\varphi^*\pi^*\alpha = \pi^*\alpha.`
    したがって：

    .. math::

       \int_{\widehat M}\!\varphi^*\pi^*\alpha
       = \int_{\widehat M}\!\pi^*\alpha.

  * 写像 :math:`\varphi` の反転性により：

    .. math::

       \int_{\widehat M}\!\varphi^*\pi^*\alpha
       = -\int_{\widehat M}\!\pi^*\alpha.

  * この二つの等式より：

    .. math::

       \int_{\widehat M}\!\pi^*\alpha = 0.

  * ここで :ref:`定理 3.4.8 <tsuboi08.3.4.8>` により、
    :math:`\pi^*\alpha = \dd \beta \in \Omega^n(M)`
    （外微分をオメガの元と見るのが新鮮）

  * :math:`\displaystyle \beta_1 = \frac{1}{2}(\beta + \varphi^*\beta) \in \Omega^{n - 1}(\widehat M)` に対して、
    :math:`\varphi^*\beta_1 = \beta_1` より :math:`\beta_1 = \pi^*\beta_2 \in \Omega^{n - 1}(\widehat M).`

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
