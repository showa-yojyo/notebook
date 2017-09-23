======================================================================
幾何学と不変量 読書ノート 8/10
======================================================================

:doc:`note07` からの続き。

.. contents:: ノート目次

第 8 章 軌道空間の幾何的構造
======================================================================
ノートが上手くとれていない。

8.1 等質空間
----------------------------------------------------------------------
等質空間
  位相群 G の閉部分群 H による商空間 G/H のこと。

推移的
  群 G が空間 X への推移的作用であるとは、
  :math:`\forall x, y \in X, \exists g \in G such that gx = y` であることを言う。

  * X 自身が一つの G 軌道である。
  * :math:`\Omega_{G}(X)` と :math:`X/G` は一点からなる。

固定部分群
  :math:`G_x = \lbrace g \in G \mid gx = x \rbrace` を x の固定部分群という。

  :math:`G = \bigsqcup aG_x (a \in G/G_x)` を右剰余類を用いた軌道分解という。

* 定理 8.3: G が位相空間 X に連続かつ推移的に作用しているならば、X の任意の元 x に対して
  写像 :math:`G/G_x \longrightarrow X` が存在して、それは連続かつ全単射である。

* 定理 8.6: :math:`G/G_x \cong X` を紹介するだけか。詳細がわからない。
* 例 8.7: :math:`G = \mathit{SO}_3(\mathbb{R})` の :math:`S^2 \subset \mathbb{R}^3` への作用。
  球面の「北極」の固定部分群を求めると、これが :math:`G = \mathit{SO}_2(\mathbb{R})` と同型であることがわかるので、
  先の定理より :math:`\mathit{SO}_3(\mathbb{R}) / \mathit{SO}_2(\mathbb{R}) \cong S^2` が結論できる。

* 例 8.8: 複素平面上の単位円について

  * 実数を加法群とみなして :math:`e^{2 \pi i \xi} (\xi \in \mathbb{R})` の乗算によって作用している。
  * 1 の固定部分群が整数である。
  * よって :math:`G/\mathbb{Z} \cong S^1`

トーラスも固定部分群を :math:`\lbrace (2 \pi n, 2 \pi m) \mid n, m \in \mathbb{Z} \rbrace` とすれば
:math:`\mathbb{R}^2/\mathbb{Z}^2 \cong S^1 \times S^1`

* 例 8.9: 曲面 :math:`x^2 + y^2 - z^2 = k` ただし k は実数。

  * k が正ならば一葉双曲面（連結）
  * k が負ならばニ葉双曲面
  * :math:`G = O_{21}(\mathbb{R})` が自然に作用している。
  * :math:`Q = {}^t\xi \operatorname{diag}(1, 1, -1) \xi` とすると :math:`Q(g \xi) = Q(\xi)` なので、
    この二次形式は G の作用による不変式。つまり双曲面上の点は双曲面上の点に移る。

  * k が 1 のとき（以下、曲面を :math:`X_1` とする）

    * :math:`O_{21}(\mathbb{R})` は :math:`X_1` に推移的に作用する。
    * スペースの都合でここには成分を記せないが、
      :math:`u_{\theta} \in O_{21}(\mathbb{R})` と :math:`a_t \in O_{2}(\mathbb{R})` で移る。

      * 後者のようなものを双極回転という。
        断面の双曲線に沿った動き。

    * :math:`X_1` のパラメーター表示が得られた。
    * この後、点 (1, 0, 0) に関する固定部分群を求めて、定理 8.6 を用いて
      :math:`X_1 \cong O_{21}(\mathbb{R}) / O_{11}(\mathbb{R})` を導く。
      :math:`I_{11} = \operatorname{diag}(1, -1)`

    * 結論: 一葉双曲面は連結であり、唯一の軌道からなる。

  * k が -1 のときは :math:`X_{-1} \cong O_{21}(\mathbb{R}) / O_2(\mathbb{R})` が成り立つ。
    連結ではなく、唯一の軌道からなる。

  * k が 0 のときは見てくれどおり
    :math:`\lbrace 0 \rbrace \sqcup X_0 \setminus \lbrace 0 \rbrace` だとしか言えない。

TODO: 8.1 最後の鏡映の話がノートから漏れた。

8.2 同伴ファイバー束
----------------------------------------------------------------------
同伴するファイバー束
  G, H, W をそれぞれ群、G の部分群、H が作用する空間とする。
  :math:`G \times_{H} W` を :math:`(G \times W) / H` で定義し、
  それを同伴するファイバー束と呼ぶ。

  * 集合としては軌道空間と同じ。:math:`G \times_{H} W = \Omega_{H}(G \times W)`
  * 右辺の直積には同値関係 :math:`(g, w) \sim (gh^{-1}, hw)` が入る。
    :math:`G \times_{H} W = \lbrace [g, w] \mid (g, w) \in G \times W \rbrace = G \times W / \sim`

ファイバー束から底空間への射影
  写像 :math:`[g, w] \mapsto gH \in G/H` とすると、この逆像は部分群が作用する空間と同型になる。

底空間
  商群 :math:`G/H` のことをそう呼ぶ。

ファイバー
  空間 W のことをそう呼ぶ。

* 例 8.13

  * :math:`S^2` は :math:`\mathit{SO}_3(\mathbb{R})` の等質空間だ。
  * :math:`S^2 \cong \mathit{SO}_3(\mathbb{R})/\mathit{SO}_2(\mathbb{R})` であった（復習）。
  * :math:`H = \mathit{SO}_2(\mathbb{R})` は :math:`W = \mathbb{R}^2` に回転として作用するので、
    同伴ファイバー束 :math:`G \times_{H} W` を考える。

    * 底空間は :math:`S^2` だ。
    * ファイバーは :math:`\mathbb{R}^2` のファイバー束（接束という）。

* 例 8.14: :math:`W = \mathbb{R}^2 \subset \mathbb{R}^3` を xy 平面とし、
  :math:`H = \mathit{SO}_2(\mathbb{R})` を z 軸周りの回転で :math:`G = \mathit{SO}_3(\mathbb{R})` の部分群とする。

  * このとき同伴ファイバー束から 3 次元空間への射影を
    :math:`[g, w] \mapsto g(\mathbf{e}_3 + w)` で定めると、

    * well-defined かつ
    * 値は :math:`g\mathbf{e}_3` における接平面であり、
    * 同型写像を与える。

  * 同伴ファイバー束と球面の接束 :math:`TS^2` は同一視できる。

.. todo:: 8.3 and 8.4

----

:doc:`note09` へ。
