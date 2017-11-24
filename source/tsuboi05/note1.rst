======================================================================
幾何学 I 多様体入門 読書ノート 1/8
======================================================================

.. contents:: ノート目次

第 1 章 多様体論について
======================================================================

1.1 なぜ多様体論を学ぶのか
----------------------------------------------------------------------
#. 多様体は幾何学の対象としてさまざまな場面で現れる。

   * 曲面論（図形を吟味する）
   * 複素関数論（線積分の振る舞い）
   * ベクトル解析（ベクトル場、微分形式）

#. 現代幾何学の問題設定の枠組を与える。

   * 位相多様体から微分可能多様体へ。
   * 「位相多様体には微分可能構造を入れられるか」という問題。
   * 多様体が定義されると、その上での常微分方程式、偏微分方程式、
     多様体間の写像、多様体上の構造についてのさまざまな問題が定式化される (p. 5)。

#. 多様体の定義から派生する各種概念、代数的構造の抽出、上部構造の定式化という理論構成が
   現代数学の理論構成の典型となっている。

   * 近傍＆分離公理からベクトル場＆微分形式が出てくる。

     * ベクトル場からリー代数、リー群の作用が出てくる。
     * 微分形式から次数付き微分加群、ドラームコホモロジー不変量が出てくる。

   * 上部構造とはリーマン構造（計量）、複素構造など。

   こういう視点が欲しい。

* 用語

  * `位相空間 <http://mathworld.wolfram.com/TopologicalSpace.html>`__
  * 局所 `ユークリッド的 <http://mathworld.wolfram.com/EuclideanSpace.html>`__
  * `ハウスドルフ <http://mathworld.wolfram.com/HausdorffAxioms.html>`__
  * n 次元 `位相多様体 <http://mathworld.wolfram.com/TopologicalManifold.html>`__

* 例 1.1.2: `コッホ曲線 <http://mathworld.wolfram.com/KochSnowflake.html>`__

  * 「収束先」は円周と同相な図形だが、至るところ微分不可能な閉曲線。
  * 任意の二点間の自然に定義される距離が無限大になる。

* 問題 1.1.3: 線分集合が位相多様体となる条件

  * 3 次元空間内の線分群が多様体になる条件。
  * 各線分を構成する各点の近傍がどのようになるのかが重要。

    * 線分の内点については :math:`\RR` と同相になるような近傍が存在する。

    * 線分の端点については、もしそれが他の線分と接続されていなければ、
      :math:`\RR` と同相になるような近傍が存在しないので候補から外す。

    * 線分と線分との「折れ目」に相当する点は詳しく調べる。

      * その点から線分が二つしか接続していない場合は、
        やはり十分小さな「半径」を考えれば :math:`\RR` と同相になるような近傍が存在する。

      * 線分が三つ以上接続している場合はそのような近傍は存在しない。

    * 解説を見ると孤立点の場合も考慮しているが、
      それは問題の仮定の時点で除外されている。

  * 折れ線がループになって、それがいくつか空間内にあるようなイメージで良さそうだ。

    * ただし、直積位相を考えることになる？
      :math:`S^1 \times S^1 \times \dots S^1` と同相なのか。

1.2 逆写像定理、陰関数定理（基本）
----------------------------------------------------------------------
リプシッツ連続性 ⇒ chain rule ⇒ 合成写像 ⇒ 逆写像定理 ⇒ 陰関数定理という構造か。

* 定理 1.2.1: `逆写像定理 <http://mathworld.wolfram.com/InverseFunctionTheorem.html>`__

  * 定義確認：逆写像定理の仮定の陳述で `ヤコビアン <http://mathworld.wolfram.com/Jacobian.html>`__
    が現れる。
  * 逆写像定理の結論は「ある近傍と写像が存在して、その近傍で局所的に逆写像が存在する」だ。

* 定義確認

  * ユークリッド空間の `開近傍 <http://mathworld.wolfram.com/OpenNeighborhood.html>`__
    （位相空間論の本を参照）

  * `ノルム <http://mathworld.wolfram.com/Norm.html>`__
    （普通の感覚での距離）

  * :math:`C^r` 級である
  * :math:`C^\infty` 級 or 無限回微分可能 or `滑らかである <http://mathworld.wolfram.com/SmoothFunction.html>`__
  * :math:`C^0` 級である（連続関数と同義）

* 定理 1.2.3: `陰関数定理 <http://mathworld.wolfram.com/ImplicitFunctionTheorem.html>`__

  * :math:`C^r` 級写像 :math:`F` が :math:`\RR^n` の開集合から
    :math:`\RR^m` (:math:`m \le n`) へのものとなっている。
    憶え方として「k + m 次元から m 次元」というのもアリ。
    タイプ量の都合上、以下 :math:`k = n - m` を導入する。

  * :math:`\rank DF_{(x^0)} = m` ならば、
    :math:`F` と同級の写像 :math:`g` と近傍
    :math:`W \subset \RR^k` が何か存在して、そこで次を満たす。

    .. math::
       :nowrap:

       \begin{align*}
       \begin{array}{rll}
                            & g(x_1^0, \dotsc, x_k^0)  &= (x_{k + 1}^0, \dotsc, x_n^0)\\
       F(x_1, \dotsc, x_k,\ & g(x_1^0, \dotsc, x_k^0)) &= F(x^0)
       \end{array}
       \end{align*}

* 例題 1.2.4: chain rule を書くために行ベクトルで書くほうがよい。

  * 解説中に臨界点という用語が出ている。
    これは正則点でないという意味であり、その点におけるヤコビアンが正則でないの意味にとる。
    詳しくは第 5 章で扱う。

* 問題 1.2.5: 計算が面倒。
* 問題 1.2.6: もっと面倒。

本書では陰関数定理を証明するのに逆写像定理を利用する。

.. _tsuboi05.1.2.7:

* 例題 1.2.7: リプシッツ連続性

  * 開集合 :math:`U \subset \RR^n` で定義された
  * 関数 :math:`G \in C^1(U, \RR^m)` が、
  * :math:`G(\bm x) = (g_1(x_1, \dotsc, x_n), \dotsc, g_m(x_1, \dotsc, x_n))` とおくと
  * 凸な閉集合 :math:`A \subset U` において :math:`\displaystyle \abs{\frac{\partial g_i}{\partial x_j}} \le K`
    なる定数 :math:`K > 0` があるとする。

  このとき次が成り立つ：

  .. math::

     \forall \bm x, \bm x + \bm v \in A,\ 
     \norm{G(\bm x + \bm v) - G(\bm x)} \le \sqrt{mn}K\norm{\bm v}.

  * 証明方針

    #. 全微分可能性より各 :math:`i = 1, \dotsc, n` について次のように書ける
       :math:`\eps_i(\bm x, \bm v)` が :math:`A` には存在する：

       .. math::

          g_i(\bm x + \bm v) - g_i(\bm x) = \sum_{j = 1}^n\frac{\partial g_i}{\partial x_j}v_j + \eps_i(\bm x, \bm v)\norm{\bm v},\\
          \eps_i(\bm x, \bm v) \to 0 \text{ as } \bm v \to 0.

    #. この関係式を :math:`\bm x + (t + s)\bm v` と :math:`\bm x + t\bm v` に対して適用すると
       次の等式が得られるとあるが、ここがよくわかっていない。
       極限が微分になるのはわかるが、何を何に代入するとこうなる？
       :math:`s` はどこへ消えた？

       .. math::

          \diff{g_i(\bm x + t\bm v)}{t} = \sum_{j = 1}^n\frac{\partial g_i(\bm x + t\bm v)}{\partial x_j}v_j.

    #. 定積分を利用する後半の評価式は大丈夫。気をつけるのは
       :math:`\displaystyle \sum_{j = 1}^n\abs{v_j} \le \sqrt{n}\norm{\bm v}` くらいか。

       * 両辺とも正の値であるから :math:`\displaystyle \left(\sum_{j = 1}^n \abs{v_i}\right)^2 \le \sum_{j = 1}^n nv_i^2` を示せばいい。
         不等式の右辺マイナス左辺を展開すると :math:`\displaystyle \sum_{i \ne j}^n(\abs{v_i} - \abs{v_j})^2` の形になる。
         確かにこの値は負にならない。

       * 今得られた :math:`\abs{g_i(\bm x + \bm v) - g_i(\bm x)} \le \sqrt{n}K\norm{\bm v}`
         を利用して最後の評価を次のようにする：

         .. math::

            \begin{align*}
            \norm{G(\bm x + \bm v) - G(\bm x)}
              &\le \sqrt{m}\norm{\bm v}
              = \sqrt{m} \sum_{i = 1}^m \abs{g_i(\bm x + \bm v) - g_i(\bm x)}^2\\
              &\le \sqrt{m} \sqrt{n}K\norm{\bm v}\\
              &\le \sqrt{mn}K \norm{\bm v}.
            \end{align*}

.. _tsuboi05.1.2.8:

* 例題 1.2.8: `chain rule <http://mathworld.wolfram.com/ChainRule.html>`__

  * 合成写像のヤコビアン :math:`D(F \circ G) =  DF_{(G)} DG` の証明するのに、
    さっそくリプシッツ連続性を利用する。
    具体的には :math:`f_i(G(\bm x + \bm u)) - f_i(G(\bm x))` を展開、評価する。

  * 式の展開はシグマ記号が複数出てきて頭に馴染みにくいかもしれない。

    .. math::

       \sum_{k = 1}^l\left(\sum_{j = 1}^m \frac{\partial f_i}{\partial y_j}\frac{\partial g_j}{\partial x_k}\right)u_k + (\dots)\norm{\bm u}

    ただ、証明の骨格は一変数関数についての合成関数の微分法の公式の証明と同じに見える。

    .. math::

       f(g(x + \Delta x)) - f(g(x)) = 
         f'(g(x))g'(x) + \eps_g(x, \Delta x)f'(g(x))\Delta x 
          + \eps_f(g(x), g(x + \Delta x) - g(x))(g(x + \Delta x) - g(x)).

    :math:`\Delta x \to 0` のときに :math:`\eps_g(\dots)\Delta x \to 0,\ \eps_f(\dots)(g(x + \Delta x) - g(x)) \to 0.`
    一変数版の :math:`\Delta x` が多変数版のヤコビアンの行列式に相当する。

* 例題 1.2.9: :math:`C^r` 級写像の合成

  * :ref:`chain rule <tsuboi05.1.2.8>` および帰納法で示す。
  * 行列の積が :math:`C^\infty` 写像とみなせることに注意。
  * ヤコビアンをとる演算が :math:`C^{r-1}` 級であるならば、
    ヤコビアンの対象となる写像は :math:`C^r` 級である。

1.3 逆写像定理の証明
----------------------------------------------------------------------
次の二段階に分けて証明する。

1.3.1 特別な場合の逆写像定理
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ヤコビアンが原点において単位行列であり、かつ開集合が原点を含む場合を示す：

  :math:`\RR^n` の原点を含む開集合 :math:`U` で定義された :math:`C^r` 級写像
  :math:`\fn{F}{U}\RR^n` に対して、次のような開集合 :math:`V` と
  :math:`C^r` 級写像 :math:`\fn{G}{V}U` が存在する：

  .. math::

     G \circ F = \id_{G(V)},\ F \circ G = id_V.

* まず :math:`F(\bm x) = \bm y` に収束するコーシー列 :math:`\set{\bm x_i}` を構成したい。

  .. math::

     \begin{align*}
     &\bm x_0 = 0,\\
     &\bm x_1 = \bm y,\\
     &\bm x_2 = \bm x_1 - (F(\bm x_1) - y),\\
     &\bm x_3 = \bm x_2 - (F(\bm x_2) - y),\\
     &\dots,
     \end{align*}

  * :math:`H(\bm x) = \bm y - F(\bm x)` とおく。

    * 当然 :math:`DH_{(0)} = 0.`

  * :math:`\displaystyle \frac{\partial f_i}{\partial x_j}` が 0 に近いので、
    :math:`\displaystyle \eps \le \frac{1}{2n}` に対して次を満たす :math:`\delta > 0` が存在する：

    .. math::

       \norm{\bm x} < \delta \implies \abs{\frac{\partial h_i}{\partial x_j}} \le \eps.

  * :ref:`例題 1.2.7 <tsuboi05.1.2.7>` のリプシッツ評価式を利用して
    :math:`\norm{H(\bm x + \bm v) - H(\bm x)} \le \eps n \norm{\bm v}.`
  * :math:`\displaystyle \norm{\bm y} \le \frac{\delta}{2}` とすると
    :math:`\displaystyle \norm{\bm x_{k + 1} - \bm x_k} = \norm{H(\bm x_k) - H(\bm x_{k - 1})} \le \frac{1}{2^k}\lVert \bm x_1 - \bm x_0 \rVert` より
    :math:`\norm{\bm x_{k + 1}} < \delta` が成り立つ。
    各点に対して上述のリプシッツ評価式が成り立つから
    :math:`\set{\bm x_i}` はコーシー列であり、極限が :math:`\bm x` であることが示せた。

* 逆写像 :math:`G(\bm y) = \bm x` のひねり出し方がよくわからない。
  コーシー列の対応関係だけで決めて良い？

  * まず :math:`G` が :math:`C^1` 級であることを示す。
    以下 :math:`\bm y_i = F(\bm x_i), G(\bm y_i) = \bm x_i` とおく。

    .. math::

       \begin{align*}
       F(\bm x_2) - F(\bm x_1) = DF_{(\bm x_1)}(\bm x_2 - \bm x_1) + r(\bm x_1, \bm x_2)\norm{\bm x_2 - \bm x_1},\\
       r(\bm x_1, \bm x_2) \to 0 \text{ as } \bm x_2 \to \bm x_1
       \end{align*}

    とおくと、次を意味する：

    .. math::

       \begin{align*}
       \bm y_2 - \bm y_1 &= DF_{(G(\bm y_1))}(G(\bm y_2) - G(\bm y_1))
                + r(G(\bm y_1), G(\bm y_2))
                \frac{\norm{G(\bm y_2) - G(\bm y_1)}}{\norm{\bm y_2 - \bm y_1}}
                \norm{\bm y_2 - \bm y_1}
       \\
       G(\bm y_2) - G(\bm y_1) &= {DF_{(G(\bm y_1))}}\inv(\bm y_2 - \bm y_1)
                - r(G(\bm y_1), G(\bm y_2))
                \frac{\norm{G(\bm y_2) - G(\bm y_1)}}{\norm{\bm y_2 - \bm y_1}}
                \norm{\bm y_2 - \bm y_1}
       \end{align*}

  * ここで :math:`(DH)^k` の各成分の絶対値が :math:`\displaystyle \frac{1}{2^kn}` を超えないので、
    :math:`\displaystyle DF\inv = \sum_{k = 0}^\infty(1 - DF)^k = \sum_{k = 0}^\infty (DH)^k` であることを利用すると、
    :math:`DF` は :math:`G(V)` で正則である。

    * 無限級数に気づかないといけない。

  * :math:`G(\bm y)` は全微分可能であるので、上の式の :math:`r(G(\bm y_1), G(\bm y_2))\dots` の項は
    :math:`\bm y_2 \to \bm y_1` のときにゼロに収束する。

  * :math:`\bm y_1` に対して連続であるから :math:`G` は :math:`C^1` 級である。

* 最後に :math:`G` が :math:`F` の微分可能回数 :math:`r` と一致することを示す。
  これは :math:`DF` が :math:`C^{r - 1}` 級であること、
  逆行列をとる演算が :math:`C^\infty` 級であること、
  および帰納法を利用して示せる。

本書後半で類似証明が表れるので、確実に習得したい。

1.3.2 一般の場合の逆写像定理
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
一般の場合は次のようにして上の場合に帰着させる。

* :math:`L(\bm x) = DF_{(\bm x^0)}(\bm x - \bm x^0) + F(\bm x^0)` とすると :math:`L\inv` が存在して
  :math:`L\inv(\bm y) = {DF_{(\bm x^0)}}\inv(\bm y - F(\bm x^0)) + \bm x^0` が成り立つ。

* :math:`F_0(\bm x) = L\inv(F(\bm x + \bm x^0))` とおくと、
  原点の近傍上定義された局所的逆写像 :math:`G_0` がある。
  あとは :math:`G(\bm y) = G_0(L\inv(\bm y)) + \bm x^0` とおく。

1.4 本書の概要
----------------------------------------------------------------------
* ユークリッド空間内の多様体。
* 多様体から多様体への写像、微分、接空間、接束。
  多用体間の写像は接束から接束への線形写像である。
* 多様体はユークリッド空間に埋め込まれる。
* 一点の逆像が多様体となることが多い（サードの定理）。
  また、方程式（系）で与えられる部分集合も多様体となることが多い。
* 多様体の部分集合同士の比較。微分同相写像、常微分方程式論、ベクトル場の理論。
* リーマン計量（曲線の長さを、つまり多様体の大きさを定義）。
  等距離変換群はリー群となる。
* ベクトル場全体のなす線形空間には括弧積についてリー代数の構造が入る。

1.5 第 1 章の問題の回答
----------------------------------------------------------------------
線分の問題は後で見直すかもしれない。

----

:doc:`note2` へ。
