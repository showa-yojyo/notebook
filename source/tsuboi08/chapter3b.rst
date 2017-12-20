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
