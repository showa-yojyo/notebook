======================================================================
第 4 章 微分形式とベクトル場 3/4
======================================================================

.. contents:: ノート目次

4.3 接平面場（展開）
======================================================================

4.3.1 フロベニウスの定理
----------------------------------------------------------------------
* `接平面場 or 接分布 <https://en.wikipedia.org/wiki/Distribution_(differential_geometry)>`__ を余接空間と接空間の関係で定義する。

  1. :math:`\alpha \in \Omega^1(M)` と :math:`x \in M` に対して
     :math:`\ker\alpha = \set{v \in T_xM \sth \alpha(v) = 0}` は
     接空間 :math:`T_xM` の :math:`\dim M - 1` 次元部分多様体である。

  2. この :math:`\ker\alpha` の部分空間（接束 :math:`TM` の部分ベクトル束）を
     接平面場 or 接分布と呼ぶ。

* 関数 :math:`f \in \Omega^0(M)` が点 :math:`x_0 \in M` において
  :math:`\dd f \ne 0` であるとする。

  * このとき部分集合 :math:`\set{x \in M \sth f(x) = f(x_0)} \subset M` は
    点 :math:`x_0 \in M` の近傍で :math:`\dim M - 1` 次元部分多様体である。

  * この近傍は :math:`\dim M - 1` 次元の等位面で埋め尽くされていて、
  * :math:`\ker\dd f` は各点で等位面の接空間と一致する。

* 1 形式 :math:`g \dd f \in \Omega^1(M)` が点 :math:`x_0 \in M` で
  :math:`g(x) \ne 0` であるとする。
  このとき、状況は上記と同様になる。

* 1 形式 :math:`\alpha = g\dd f \in \Omega^1(M)` が点 :math:`x_0 \in M` の近傍で
  :math:`\alpha \ne 0` であるとするならば、
  :math:`\alpha \wedge \dd \alpha = 0` が成り立つ。

  * :math:`\alpha \wedge \dd \alpha = g\,\dd f \wedge (\dd f \wedge \dd f) = 0` による。

.. _tsuboi08.4.3.1:

* 定理 4.3.1: 上の逆が成立する

  * :math:`\alpha \in \Omega^1(M)` が点 :math:`x_0 \in M` の近傍で
    :math:`\alpha \ne 0` であり、
  * :math:`\alpha \wedge \dd \alpha = 0`

  ならば、点 :math:`x_0 \in M` の近傍の関数 :math:`f, g` が存在して、
  :math:`\alpha = g\,\dd f` が成り立つ。

  1. 証明をするための多様体上の点と座標近傍、微分形式、枠場を設定する：

     * :math:`x_0 \in (U, \varphi = (x_1, \dotsc, x_n))`
     * :math:`\displaystyle \alpha = \sum_{i = 1}^n f_i\,\dd x_i \in \Omega^1(M)`,
       ただし :math:`f_n = 1`
     * :math:`\xi_i = \dfrac{\partial}{\partial x_i} - f_i{\partial}{\partial x_n}\quad(i = 1, \dotsc, n - 1)`

  2. :math:`\alpha \wedge \dd\alpha = 0` であるので、次のようになっている：

     .. math::

        0 = \sum_i\sum_k\sum_j f_i \dfrac{\partial f_k}{\partial x_j}\,\dd x_i \wedge \dd x_j \wedge \dd x_k.

  3. 括弧積を定義に従って計算すると次のようになる：

     .. math::

        [\xi_i, \xi_j] = \left(
            \dfrac{\partial f_j}{\partial x_i}
           +\dfrac{\partial f_i}{\partial x_j}
           + f_i \dfrac{\partial f_j}{\partial x_n}
           - f_j \dfrac{\partial f_i}{\partial x_n}
           \right)
           \dfrac{\partial}{\partial x_n}.

  4. ここで 2. の和のうち :math:`\dd x_i \wedge \dd x_j \wedge \dd x_n` の係数は
     3. の括弧内のものと等しい。したがって 3. の値はゼロである。

  5. 以上より、:math:`\xi_1, \dotsc, \xi_{n - 1}` は、

     * 生成するフローが可換であり、
     * :math:`\RR^{n - 1}` の局所的な作用を生成し、
     * :math:`\ker\dd f` を張る

       * :math:`\varphi\inv(0, \dotsc, 0, f(x))` がどうのと言っている。

     ベクトル場である。:ref:`幾何学 I 8.4 節 <tsuboi05.8.4>` を参照。

  6. 各点 :math:`x \in M` で、:math:`\alpha` は :math:`\dd f` のゼロでない関数倍である。
     つまり :math:`\alpha = g\,\dd f` なる :math:`g \ne 0` が存在する。

..

* :ref:`定理 4.3.1 <tsuboi08.4.3.1>` の条件を満たす接平面場と
  定理 4.3.1 の関数 :math:`f` の等位面の接平面場は同じもの（局所的）。
  これを「多様体 :math:`M` に余次元 1 `葉層構造 <http://mathworld.wolfram.com/Foliation.html>`__
  が与えられている」という。

  * 関数の等位面をつなぎ合わせると :math:`\dim M - 1` 次元部分多様体が定義される（局所的）。
  * この部分多様体の極大なものを葉という。

  * 例えば任意の接ベクトル :math:`v \in T_xM` に対して
    :math:`\alpha(v) \ne 0` なる :math:`\alpha \in Z^1(M)` は定理 4.3.1 の仮定を満たすので、
    余次元 1 葉層構造がある。

    * 微分形式が閉形式であるというのがありがたい。

* :math:`\alpha = g\,\dd f` が点 :math:`x_0 \in M` の近傍でゼロでなければ、
  :math:`\dd\alpha = \dd f \wedge \dd f = \dfrac{1}{g} \wedge \alpha` と書ける。
  よって、:math:`\alpha \wedge \dd\alpha = 0` ならば、
  :math:`\beta \in \Omega^1(M)` が存在して :math:`\dd\alpha = \beta \wedge \alpha` が
  成り立つと言い変えてもよい。

.. _tsuboi08.4.3.2:

* 命題 4.3.2: 1 形式と p 形式の外積に対する :math:`p - 1` 形式の存在

  * :math:`\alpha \in \Omega^1(M),\ \alpha \ne 0`
  * :math:`\beta \in \Omega^p(M)`
  * :math:`\alpha \wedge \beta = 0`

  ならば、:math:`\exists \gamma\quad\text{s.t. }\beta = \gamma \wedge \alpha.`

  1. 余接空間 :math:`T_x^*M` の基底を :math:`\dd x_1, \dotsc, \dd x_n` から
     :math:`e_1, \dotsc, e_n` に取り替えることを考える。
     ここで :math:`\alpha(x) = e_1` とする。

     同時に :math:`\extp^p T_x^*M` の基底も :math:`\dd x_{i_1} \wedge \dd x_{i_p}` から
     :math:`e_{i_1} \wedge e_{i_p}` に置き換わる。

  2. この取り替えは点 :math:`x \in M` の座標近傍 :math:`(U, \varphi)` で
     各 :math:`e_i` が :math:`C^\infty` 級写像となるようにとれる。

  3. :math:`\displaystyle \alpha = e_1, \beta = \sum_{j_1 < \dotsb j_p}g_{j_1 \dots j_p}e_{j_1} \wedge \dotsb \wedge e_{j_p}` と書ける：
  4. :math:`\alpha \wedge \beta = 0` より :math:`1 < j_1` ならば
     :math:`g_{i_1 \dots i_p} = 0` である。
     したがって次が成り立つ：

     .. math::

        \beta = \sum_{j_2 < \dotsb j_p}g_{1 j_2 \dots j_p}e_{j_2} \wedge \dotsb \wedge e_{j_p}.

  5. :math:`M` の開被覆 :math:`U_i` を 2. のようにとり、
     これに従属する 1 の分割 :math:`\lambda_i` をとる。

  6. :math:`\exists \gamma_i \in \Omega^{p - 1}(U_i)\quad\text{s.t. }\beta = \alpha \wedge \gamma_i.`
  7. :math:`\gamma = \sum\lambda_i\gamma_i` に対して：

     .. math::

        \begin{align*}
        \alpha \wedge \gamma
        &= \alpha \wedge \sum_i \lambda_i\gamma_i\\
        &= \sum_i \lambda_i\alpha_i \wedge \gamma_i\\
        &= \sum_i \lambda_i\beta\\
        &= \beta.
        \end{align*}

  これは :ref:`定理 4.3.1 <tsuboi08.4.3.1>` の言い換えである。

..

次のテーマは写像 :math:`\fn{F}{U}\RR^q` で定まる多様体の族である。

* :math:`\rank F = q` とする。
  このとき座標 :math:`\fn{\varphi}{U}\RR^n` で :math:`F` が射影
  :math:`\RR^n \longto \RR^q` に一致するものがうまくとれる。

  * 射影でない方の座標を :math:`(x_1, \dotsc, x_p)`
  * 射影のほうを :math:`(y_1, \dotsc, y_q)`

  とすると、部分多様体の接空間は次で与えられる：

  .. math::

     \ker\dd y_1 \cap \dotsb \cap \ker\dd y_q.

* 行列による線形写像 :math:`\displaystyle \fn{A = (a_{ij})}{U}GL_q(\RR)` と
  1 形式 :math:`\alpha_i = \sum_{i = 1}^q a_{ij}\,\dd y_j\quad(i = 1, \dotsc, q)` を考えると、
  部分多様体の族の接空間は次で与えられる：

  .. math::

     \ker\alpha_1 \cap \dotsb \cap \ker\alpha_q.

* この 1 形式に対する外微分を計算する：

  .. math::

     \begin{align*}
     \dd\alpha_i
     &= \sum_{i = 1}^q \dd a_{ij} \wedge \dd y_j\\
     &= \sum_{i = 1}^q \dd a_{ij} \wedge \left(\sum_{k = 1}^q(A\inv)_{jk}\alpha_k\right)\\
     &= \sum_k\left(\sum_j (A\inv)_{jk}\,\dd a_{ij}\right) \wedge \alpha_k
     \end{align*}

  つまり :math:`\beta_{ik} \in \Omega^1(U)` が存在して
  :math:`\dd \alpha_i = \sum \beta_{ik} \wedge \alpha_k` と書けることを意味する。
  これを完全積分可能条件という。

.. _tsuboi08.4.3.3:

* 問題 4.3.3: 上記の存在条件は :math:`\alpha_i` のとり方に依存しない

  示すべきは :math:`\ker\alpha_1 \cap \dotsb \cap \ker\alpha_q = \ker\alpha'_1 \cap \dotsb \cap \ker\alpha'_q`
  と書けるときに、
  :math:`\displaystyle \alpha'_i = \sum_{j = 1}^q a'_{ij}\alpha_j` となるような
  :math:`\fn{A' = (a'_{ij})}{U}GL_q(\RR)` が存在することを使って
  :math:`\displaystyle \dd \alpha'_i = \sum_{i = 1}^q \beta'_{ik} \wedge \alpha'_k`
  なる :math:`\beta'_{ik} \in \Omega^1(U)` があることだ。

.. _tsuboi08.4.3.4:

* 定理 4.3.4: `フロベニウスの定理 <https://en.wikipedia.org/wiki/Frobenius_theorem_(differential_topology)#Differential_forms_formulation>`__

  多様体 :math:`M^{p + q}` の各点において近傍 :math:`U \subset M` が存在して、

  * :math:`\alpha_1, \dotsc, \alpha_q \in \Omega^1(U)` が一次独立で、
  * :math:`\ker\alpha_1 \cap \dotsb \cap \ker\alpha_q` で p 次元接平面場が表される

  とする。この接平面場が点の近傍 :math:`V \subset` からユークリッド空間への
  ランク q の写像 :math:`\fn{F}{V}\RR^q` で定まる p 次元部分多様体の
  族の接平面場となることと、次が同値となる：

  .. math::

     \exists \beta_{ik} \in \Omega^1(V)\quad\text{s.t. }
     \dd\alpha_i = \sum_{k = 1}^q \beta_{ik}\wedge\alpha_k.

  :math:`\Longleftarrow` 側の証明が残っている。

  1. 座標近傍 :math:`(U, \varphi = (x_1, \dotsc, x_p, y_1, \dotsc, y_q)` において
     p 次元接平面場は射影に対して横断的であるとする。

  2. 接平面場は次の p 個のベクトル場が張る：

     .. math::

        \xi_i = \dfrac{\partial}{\partial x_i} + \sum_{l = 1}^q b_{li}\dfrac{\partial}{\partial y_l}.

  3. 必要なら各 :math:`\alpha_l` を並び替えて次が成り立つようにする：

     .. math::

        \alpha_l = \dd y_l = \sum_{i = 1}^p b_{li}\,\dd x_i.

     このとき各微分形式の核の共通部分は保たれる。

  4. :math:`F` で定まる p 次元部分多様体の族の接平面場となるとき、2. のベクトル場
     が局所的に生成するフローは可換である。

     ベクトル場が p 次元部分多様体の接空間に接しているので、
     :math:`[\xi_i, \xi_j]` はそこに値を持つ。
     それゆえ :math:`\displaystyle [\xi_i, \xi_j] = \sum_{i = 1}^p c_i\xi_i` のように
     線形結合の形で書けるはずだが、左辺の :math:`\dfrac{\partial}{\partial x_i}` の
     各成分はゼロであり、したがって全体としてゼロである。

  5. ベクトル場 :math:`\xi` が可換である条件を計算で求める。

     * :math:`\alpha_l`
     * :math:`\displaystyle \dd\alpha_l = \sum_{k = 1}^q\beta_{ik}\wedge \alpha_k`
     * :math:`\displaystyle \beta_{li} = \sum_{j = 1}^p f_{lij}\,\dd x_j + \sum_{j = 1}^q g_{lij}\,\dd y_j`

     を利用して条件を詰めていく。難しい。

     :math:`\displaystyle [\xi_i, \xi_j] = \sum_{m = 1}^q(\cdots)\dfrac{\partial}{\partial y_m}`
     の形に書き換えれば、括弧内がゼロになる。

  6. これで :math:`\xi_1, \dotsc, \xi_p` が生成するフローが可換であり、
     :math:`\RR^p` の局所的な作用を生成することが言えた。

  :math:`\xi_1, \dotsc, \xi_{n - 1}` は :math:`F` により定まる
  p 次元部分多様体の族の接平面場を張る。

.. _tsuboi08.4.3.6:

* 問題 4.3.6: :math:`SL_2(\RR)` の左不変完全積分可能 2 次元平面場

  本問は :ref:`問題 4.2.2 <tsuboi08.4.2.2>` (2) で途中まで計算済み。
  :math:`aH^* + bS^* + cU^*` とおいて :math:`\dd\alpha \wedge \alpha = 0` となる条件を示せばよい。

.. _tsuboi08.4.3.7:

* 問題 4.3.7: :math:`M` 上の余次元 1 の接平面場が :math:`\alpha \in \Omega^1(M)` で与えられるとする

  1. 完全積分可能条件より :math:`\beta \in \Omega^1(M)` に対して :math:`\dd\alpha = \beta \wedge \alpha` となるものが存在する。
  2. :math:`\beta \wedge \dd \beta \in Z^3(M)`
  3. \2. のドラーム・コホモロジー群は :math:`\beta` のとり方に依存しない。

  :math:`\dd\alpha = \beta \wedge \alpha` の両辺を外微分することで :math:`\dd\beta \wedge \alpha = 0` がわかる：

  .. math::

     \begin{align*}
     0 = \dd(\dd\alpha)
     &= \dd\beta + \alpha + \beta \wedge \dd\alpha\\
     &= \dd\beta + \alpha + \beta \wedge \beta \wedge \alpha\\
     &= \dd\beta + \alpha.
     \end{align*}

  :ref:`命題 4.3.2 <tsuboi08.4.3.2>` より :math:`\dd\beta = \gamma \wedge \alpha` を
  みたす :math:`\gamma \in \Omega^1(M)` があるので：

  .. math::

     \begin{align*}
     \dd(\beta \wedge \dd\beta)
     &= \dd\beta \wedge \dd\beta + \dd(\dd\beta)\\
     &= (\gamma \wedge \alpha) \wedge (\gamma \wedge \alpha) + 0\\
     &= 0.
     \end{align*}

  :math:`\dd\alpha = \beta \wedge \alpha = \beta' \wedge \alpha` なる :math:`\beta'` をとる。
  このとき :math:`(\beta' - \beta) \wedge \alpha = 0` だから
  :ref:`命題 4.3.2 <tsuboi08.4.3.2>` より :math:`\beta' - \beta = h\alpha` を満たす
  :math:`h \in \Omega^0(M)` が存在する。

  :math:`\beta' \wedge \dd\beta' = \beta \wedge \dd\beta - \dd(\beta \wedge (h \wedge \alpha))`
  なので、確かに :math:`\beta'` のとり方に依存しない。

  :math:`\alpha'` を :math:`\alpha` が定まる余次元 1 接平面場と同じものを定めるものとする。
  このとき :ref:`命題 4.3.2 <tsuboi08.4.3.2>` の前座部分より、
  局所的に :math:`\alpha' = g\alpha\quad(g \ne 0)`
  を満たす関数 :math:`g \in \Omega^0(M)` が存在する。

  .. math::

     \begin{align*}
     \dd\alpha'
     &= \dd g \wedge \alpha + g \dd\alpha\\
     &= \dd g \wedge \alpha + g\beta \wedge \alpha\\
     &= \left(\frac{\dd g}{g} + \beta\right) \wedge (g\alpha)\\
     &= (\dd\log\abs{g} + \beta) \wedge (g\alpha).
     \end{align*}

  * 最初の等号に :math:`\alpha' = g\alpha` を使用した。
  * 二番目の等号に 1. を使用した。
  * 三番目の等号は左から :math:`\dfrac{1}{g}` を、右から :math:`g` を乗じてある。
  * 最後の等号に対数が出てくるのは逆数の不定積分のように見える。

  .. math::

     (\dd\log\abs{g} + \beta) \wedge (\dd\log\abs{g} + \beta)
     = \beta \wedge \dd\beta + \dd(\log\abs{g} \wedge \beta)

  となり、:math:`\alpha` のとり方に依存しない。

.. _tsuboi08.4.3.8:

* 注意 4.3.8: `ゴドビヨンベイ類 <https://de.wikipedia.org/wiki/Godbillon-Vey-Invariante>`__

4.3.2 微分形式の核
----------------------------------------------------------------------
前節の :math:`\ker\alpha` の定義を一般の p 形式に拡張する：

.. math::

   \ker\alpha = \set{v \in T_xM \sth i_v\alpha = 0 \in \extp^{p - 1}T_x^*M}

これは内部積の性質のおかげで線形空間になっている：

.. math::

   \xi, \eta \in T_xM,\ i_\xi\alpha = i_\eta\alpha = 0
   \implies \forall a, b \in \RR,\ i_{a\xi + b\eta}\alpha = 0.

.. _tsuboi08.4.3.9:

* 例 4.3.9:

  * \(1) :math:`0 \ne \Omega \in \Omega^n(M^n)` に対しては :math:`\ker\alpha = 0.`
  * \(2) ユークリッド空間の例。

    * :math:`T_0\RR^4` で :math:`\ker(\dd x_1 \wedge \dd x_2 + \dd x_3 \wedge \dd x_4) = 0.`
    * :math:`T_0\RR^6` で :math:`\ker(\dd x_1 \wedge \dd x_2 \wedge \dd x_3 + \dd x_4 \wedge \dd x_5 \wedge \dd x_6) = 0.`

.. _tsuboi08.4.3.10:

* 問題 4.3.10: :math:`\alpha \in \Omega^p(M), \beta \in \Omega^q(M) \implies \ker(\alpha \wedge \beta) \supset \ker\alpha \cap \ker\beta`

  * 証明には :math:`i_v\alpha = i_v\beta = 0` から出発して :math:`i_v(\alpha \wedge \beta) = 0` を示す。
    次数付き可換性を用いて式変形する。

4.3.3 体積形式とダイバージェンス
----------------------------------------------------------------------
* ベクトル場 :math:`\xi` の n 形式 :math:`\Omega` に対する発散、
  :math:`\div\xi` とは次の式を満たす関数である：

  .. math::

     L_\xi\Omega = (\div\xi)\Omega.

  * :math:`\Omega \in \Omega^n(M^n)` は各点で :math:`\ne 0` とする（多様体が向き付け可能であることと同値）。
  * :math:`\displaystyle \xi = \sum_i^n\xi\dfrac{\partial}{\partial x_i}` の
    :math:`\dd x_1 \wedge \dotsb \dd x_n` に対する発散は次のようになる：

    .. math::

       \div\xi = \sum_i^n\dfrac{\partial \xi}{\partial x_i}.

..

* `ガウス・グリーンの公式 <http://mathworld.wolfram.com/DivergenceTheorem.html>`__

  向き付けられた多様体 :math:`M` で使える公式である：

  .. math::

     \int_M\!\div\xi\Omega = \int_{\partial M}\!i_\xi\Omega.

  なぜこれが成り立つのか：

  .. math::

     \begin{align*}
     \int_M\!\div\xi\Omega
     &= \int_M\!L_\xi\Omega\\
     &= \int_M\!\dd(i_\xi\Omega)\\
     &= \int_{\partial M}\!i_\xi\Omega.
     \end{align*}

  * 最初の等号は発散の定義による。
  * 次の等号は :ref:`命題 4.1.8 <tsuboi08.4.1.8>` カルタンの公式による。
    微分形式の次数が n であることも効いている。
  * 最後の等号は :ref:`定理 3.5.1 <tsuboi08.3.5.1>` ストークスの定理による。

  特に :math:`M` がコンパクト閉多様体であれば、積分の値はゼロである。

.. _tsuboi08.4.3.11:

* 注意 4.3.11: モーザーのアイソトピー

  コンパクトで向き付け可能な多様体 :math:`M` と、その上の
  微分形式 :math:`\Omega_1 \ne 0, \Omega_2 \ne 0` に対して、

  .. math::

     \int_M\!\Omega_0 = \int_M\!\Omega_1

  が成り立つのであれば、次の条件を満たすアイソトピー :math:`\fn{F_t}{M}M` が存在する：

  .. math::

     F_0 = \id_M,\ F_1^*\Omega_0 = \Omega_1.

4.3.4 シンプレクティク形式とハミルトン・ベクトル場
----------------------------------------------------------------------
.. _tsuboi08.4.3.12:

* 問題 4.3.12: ユークリッド空間原点近傍の 2 形式の核がゼロしかないとき

  * :math:`\omega` を n 次元ユークリッド空間の 2 形式とし、
  * :math:`\ker\omega = 0` であるとする。

  このとき次のすべてが成り立つ：

  * ユークリッド空間の次元 n は偶数 :math:`n = 2m` である。
  * 原点における接空間 :math:`T_0\RR^n` の基底 :math:`e_1, \dotsc, e_{2m}` に対する
    双対基底 :math:`e_1^*, \dotsc, e_{2m}^*` を使って次のように書ける：

    .. math::

       \omega(0) = e_1^* \wedge e_2^* + \dotsb + e_{2m - 1}^* \wedge e_{2m}^*.

  * :math:`\omega^m \ne 0` である。

  逆に

  * 偶数次元ユークリッド空間の原点近傍で定義されている 2 形式
    :math:`\omega` が :math:`\omega^m \ne 0` であるならば、
    :math:`\omega(0)` は上の形に書ける。

  まずベクトル場 :math:`\xi, \eta \in \mathfrak{X}(\RR^n)` に対する
  値 :math:`\omega(\xi, \eta)` を考える。

  1. :math:`\omega(\xi, \eta) = -\omega(\eta, \xi)` が成り立つ（交代形式）。
  2. :math:`\ker\omega = 0` より、これは非退化である。すなわち
     :math:`\xi \ne 0 \text{or } \eta \ne 0 \implies \omega(\xi, \eta) \ne 0.`

  3. 原点における接空間 :math:`T_0\RR^n` の基底 :math:`\dfrac{\partial}{\partial x_i}` をとって、
     各ベクトル場に成分表示を与えておく：

     .. math::

        \begin{align*}
        \xi &= \sum_{i = 1}^n \xi_i \dfrac{\partial}{\partial x_i}\\
        \eta &= \sum_{i = 1}^n \eta_i \dfrac{\partial}{\partial x_i}
        \end{align*}

  4. まず 3. により :math:`\displaystyle \omega(\xi, \eta) = \sum a_{ij}\xi_i\eta_j` の形に表せる。
     さらに 1. により :math:`a_{ij} = -a_{ji}` が成り立つ。

  5. 行列 :math:`A = (a_{ij})` とおく。
     これは実交代行列であるので線形代数論により、
     ある直交行列が存在して次の形の行列に対して共役となる：

     .. math::

        \bigcup_k
        \begin{pmatrix}
        0 & \lambda_k\\
        -\lambda_k & 0
        \end{pmatrix}
        \cup
        \begin{pmatrix}
        0 & 0\\
        0 & 0
        \end{pmatrix}

  6. したがって対応する :math:`T_0\RR^n` の基底 :math:`e'_1, \dotsc, e'_n` およびその双対基底
     :math:`{e_1^*}', \dotsc, {e_n^*}'` がとれて次の形に書ける：

     .. math::

        \omega = \lambda_1 {e_1^*}' \wedge {e_2^*}'
          + \dotsb + \lambda_m {e_{2m - 1}^*}' \wedge {e_{2m}^*}'
        \quad(2m \le n).

     * 本書では接空間の基底の外積の線形結合で書かれていたが、
       余接空間の基底に勝手に直しておく。
     * 不等式は固有値の重複度を考慮したからか？

  7. :math:`\ker\omega = 0` ゆえ 6. の式は :math:`2m = n` で成り立つ。
  8. 基底を調節して :math:`e_{2k - 1} = \dfrac{e'_{2k - 1}}{\lambda_{2k - 1}},\ e_{2k} = e'_{2k}`
     と置き換え、:math:`e_i` の双対基底を :math:`e_i^*` と書けば、
     本問の冒頭の :math:`\omega(0)` に関する等式が成り立つことになる。

.. _tsuboi08.4.3.13:

* 注意 4.3.13: 閉形式の場合

  さらに :math:`\omega` が閉形式であれば、後述する :ref:`問題 4.3.17 <tsuboi08.4.3.17>`
  により空間各点の座標近傍で次の形のものがあることがわかる：

  .. math::

     \omega = \dd x_1 \wedge \dd x_2 + \dotsb + \dd x_{2m - 1} \wedge \dd x_{2m}.

.. _tsuboi08.4.3.14:

* 定義 4.3.14: `シンプレクティク形式 <http://mathworld.wolfram.com/SymplecticForm.html>`__

  * :math:`\omega \in Z^2(M), \ker\omega = 0` をみたす :math:`\omega` をシンプレクティク形式という。
  * シンプレクティク多様体とは、シンプレクティク形式を備えた多様体のことをいう。

..

* ハミルトン関数

  * :math:`\RR^{2m}` 上のシンプレクティク形式 :math:`\omega` に対し、
    ベクトル場 :math:`\xi` がそれを保つならば、
    :ref:`命題 4.1.8 <tsuboi08.4.1.8>` カルタンの公式と
    :ref:`定理 1.7.2 <tsuboi08.1.7.2>` ポアンカレの補題により
    :math:`i_\xi\omega = \dd f` をみたす関数 :math:`f` が存在する。

  * ベクトル場 :math:`\xi` が生成するフローによって :math:`f` は一定である。

    * なぜならば :math:`\xi(f) = (\dd f)(\xi) = i_\xi i_\xi \omega = 0`

  * 逆に :math:`\alpha \in Z^1(\RR^{2m}),\ i_\xi\alpha = 0` なるベクトル場 :math:`\xi` は
    一意的に定まる。この :math:`\xi` が生成するフローは :math:`\omega` を保つ。
    フローの軌道は葉層構造の葉の上にある。

    * ここで :ref:`定理 4.3.1 <tsuboi08.4.3.1>` により :math:`\alpha \ne 0.`

* `ハミルトン・ベクトル場 <https://en.wikipedia.org/wiki/Hamiltonian_vector_field>`__

  シンプレクティク多様体 :math:`M` 上の関数 :math:`f` に対して、
  ベクトル場 :math:`X_f` が次の式で定まる。これをハミルトン・ベクトル場と呼ぶ：

  .. math::

     i_{X_f}\omega = \dd f.

  * 例えば :ref:`注意 4.3.13 <tsuboi08.4.3.13>` のシンプレクティク形式に対する
    関数 :math:`f(x_1, \dotsc, x_{2m})` のハミルトン・ベクトル場はこうである：

    .. math::

       \dfrac{\partial f}{\partial x_2}\dfrac{\partial}{\partial x_1}
       - \dfrac{\partial f}{\partial x_1}\dfrac{\partial}{\partial x_2}
       + \dotsb +
       \dfrac{\partial f}{\partial x_{2m}}\dfrac{\partial}{\partial x_{2m - 1}}
       - \dfrac{\partial f}{\partial x_{2m - 1}}\dfrac{\partial}{\partial x_{2m}}.

* `余接束 <http://mathworld.wolfram.com/CotangentBundle.html>`__ には
  標準的シンプレクティク形式が定まる。

  1. 状況

     * 多様体 :math:`M` の次元を n とする。
     * ある点の座標近傍を :math:`(U, \varphi = (x_1, \dotsc, x_n))` とおく。
     * 射影を :math:`\fn{p}{T^*M}M` とおく。
     * 写像 :math:`\fn{\widehat{\varphi}}{p\inv(U)}\varphi(U) \times \RR^n` を定義する。
       ここで像の点 :math:`(x_1, \dotsc, x_n, y_1, \dotsc, y_n)` の後半部分は
       前半部分が表す点に対する接空間の双対ベクトルか。

  2. ここで :math:`\theta = \sum_{i = 1}^n y_i\,\dd x_i \in \Omega^1(T^*M)` とおく。

     * これは座標近傍の取り方に依存しない。

  3. :math:`\displaystyle \omega = -\dd \theta = \sum_{i = 1}^n \dd x_i \wedge \dd y_i` は
     余接束上のシンプレクティク形式になる。

* リーマン多様体の余接束上には二次形式が定まる。

  .. math::

     q^*\colon \sum_{i = 1}^n y_i\,\dd x_i \longmapsto \sum_{i,j = 1}^n g^{ij}y_i y_j.

  ここでリーマン計量を :math:`g_{ij}` とし、その逆行列を :math:`g^{ij}` とする。

.. _tsuboi08.4.3.15:

* 問題 4.3.15: リーマン計量の二次形式が余接束に定めるハミルトン・ベクトル場

  :ref:`幾何学 I 7.2 <tsuboi05.7.2>` や後述の節を参照。

  .. todo:: これは後ほど取り組む。

.. _tsuboi08.4.3.16:

* 問題 4.3.16: 全微分と余接束のシンプレクティク形式

  :math:`M` 上の関数 :math:`f` の全微分は写像 :math:`\fn{\dd f}{M}T^*M` とみなせる。

  :math:`T^*M` のシンプレクティク形式 :math:`\omega` に対して
  :math:`(\dd f)^*\omega = 0` が成り立つ。

  1. 全微分はこのような和である：

     .. math::

        \dd f = \sum_{i = 1}^n \dfrac{\partial f}{\partial x_i}\,\dd x_i.

     先ほどの座標表記を用いると：

     .. math::

        \dd f\colon (x_1, \dotsc, x_n) \longmapsto
        \left(x_1, \dotsc, x_n,
              \dfrac{\partial f}{\partial x_1},
              \dotsc,
              \dfrac{\partial f}{\partial x_n}\right).

  2. 引き戻しを計算する：

     .. math::

        \begin{align*}
        (\dd f)^*\omega
        &= (\dd f)^*\left(\sum_{i = 1}^n \dd x_i \wedge \dd y_i\right)\\
        &= \sum_{i = 1}^n \dd x_i \wedge \dd\left(\dfrac{\partial f}{\partial x_i}\right)\\
        &= \sum_{i = 1}^n \dd x_i \wedge \sum_{j = 1}^n \dfrac{\partial^2 f}{\partial x_i}{\partial x_j}\,\dd x_j\\
        &= \sum{1 \le i < j \le n}\dfrac{\partial^2 f}{\partial x_i}{\partial x_j}(
            \dd x_i \wedge \dd x_j + \dd x_j \wedge \dd x_i)\\
        &= 0.
        \end{align*}

     * 最初の等号は余接束の標準的シンプレクティク形式。
     * 二番目の等号は 1. による。
     * 三番目の等号は関数の全微分である。
     * 四番目の等号は直接計算。ここは本書の解答例とみてくれが異なるが、意味は同じ。
     * 最後の等号は外積の反対称性による。

.. _tsuboi08.4.3.17:

* 定理 4.3.17: ダルブーの定理（シンプレクティク版）

  :math:`2m` 次元シンプレクティク多様体 :math:`M` のシンプレクティク形式 :math:`\omega`
  に対し、点 :math:`x_0 \in M` の座標近傍 :math:`(U, \varphi = (y_1, \dotsc, y_{2m}))` で
  次のように書けるものがある：

  .. math::

     \omega = \dd y_1 \wedge \dd y_2 + \dotsb + \dd y_{2m - 1} \wedge \dd y_{2m}.

  .. todo:: 難しい。

4.3.5 接触形式とレーブ・ベクトル場
----------------------------------------------------------------------
* 奇数次元多様体 :math:`M^{2m + 1}` 上の

  * 値がゼロにならない :math:`\alpha \in \Omega^1(M^{2m + 1})` は
    :math:`2m` 次元の核を持つ。

  * :math:`\dd\alpha \in \Omega^2(M^{2m + 1})` は
    次元が 1 以上の核を持つ。
    :ref:`定理 4.3.12 <tsuboi08.4.3.12>` 参照。

.. _tsuboi08.4.3.18:

* 問題 4.3.18: 奇数次元空間で :math:`\ker(\dd\alpha)` :math:`\ker\alpha` が横断的に交わる状況

  :math:`\alpha \in \Omega^1(\RR^{2m + 1})` が :math:`\ker(\dd\alpha) \cap \ker\alpha = 0`
  を満たすならば、原点における接空間の基底 :math:`e_0, e_1, \dotsc, e_{2m}` で次を満たす
  ものが存在する：

  .. math::

     \alpha(0) = e_0,\quad
     \dd\alpha(0) = e_1 \wedge e_2 + \dotsb + \wedge e_{2m - 1} \wedge e_{2m}.

  また、:math:`\alpha \in \Omega^1(\RR^{2m + 1})` が
  :math:`\alpha \wedge (\dd\alpha)^m \ne 0` であれば、
  :math:`\alpha(0)` は上の形になる。

  証明手順は :ref:`問題 4.3.12 <tsuboi08.4.3.12>` と似ている。

  1. 横断的であることから :math:`\ker((\dd\alpha)|\ker\alpha) = 0.`
  2. :math:`\ker\alpha(0)` の基底 :math:`e'_1, \dotsc, e'_{2m}` をとり、
     次のように表せる：

     .. math::

        (\dd\alpha)|\ker\alpha = {e_1^*}' \wedge {e_2^*}' + \dotsb + {e_{2m - 1}^*}' \wedge {e_{2m}^*}'.

     :math:`\ker\alpha(0)` 上の交代形式に対する基底とする。

  3. :math:`\alpha(0)(e'_0) = 1` となるように :math:`e'_0` を定め、
     接空間 :math:`T_0\RR^{2m + 1}` の基底 :math:`e'_0, e'_1, \dotsc, e'_{2m}` を得る。

  4. \3. の双対基底に対して次が成り立つような :math:`\set{a_i}` が存在する：

     .. math::

        \begin{align*}
        \alpha(0) &= {e_0^*}',\\
        (\dd\alpha)(0) &= \sum_{i = 1}^{2m}
          a_i {e_0^*}' \wedge {e_i^*}'
          + {e_1^*}' \wedge {e_2^*}' + \dotsb + {e_{2m - 1}^*}' \wedge {e_{2m}^*}'.
        \end{align*}

  5. 接空間 :math:`T_0\RR^{2m + 1}` の基底 :math:`e_0, e_1, \dotsc, e_{2m}` を
     4. を用いて次のようにして得る：

     .. math::

        e_i =
        \begin{cases}
        \displaystyle \sum_{j = 1}^m(a_{2j}e_{2j - 1} - a_{2j - 1}e_{2j}) &\quad\text{if }i = 0,\\
        e_i' & \quad\text{otherwise}.
        \end{cases}

  6. そして 5. の双対基底を次のようにする：

     .. math::

        \begin{align*}
        e_0^* &= {e_0^*}',\\
        e_{2j - 1}^* &= {e_{2j - 1}^*}' + a_{2j}{e_0^*}',\\
        e_{2j}^* &= {e_{2j}^*}' - a_{2j - 1}{e_0^*}'.
        \end{align*}

  7. 奇数項の外積を計算すると：

     .. math::

        \begin{align*}
        e_{2j - 1}^* \wedge e_{2j}^*
        &= ({e_{2j - 1}^*}' + a_{2j}{e_0^*}') \wedge ({e_{2j}^*}' - a_{2j - 1}{e_0^*}')\\
        &= {e_{2j - 1}^*}' \wedge {e_{2j}^*}' + a_{2j - 1}{e_0^*}' \wedge {e_{2j - 1}^*}'
          + a_{2j}{e_0^*}' \wedge {e_{2j}^*}'.
        \end{align*}

     よって主張の等式の両方を得る。

  ここから後半を証明する。

  8. :math:`\alpha \wedge (\dd\alpha)^m \ne 0` であれば、
     :math:`\alpha \ne 0` かつ :math:`\ker((\dd\alpha)^m|\ker\alpha) = 0.`

  9. :math:`\ker((\dd\alpha)|\ker\alpha) \subset \ker((\dd\alpha)^m|\ker\alpha)`
     であるから :math:`\ker((\dd\alpha)|\ker\alpha) = 0.`
     あとは 1. 以降の議論に合流する。

.. _tsuboi08.4.3.19:

* 注意 4.3.19: 実は :ref:`定理 4.3.24 <tsuboi08.4.3.24>` ダルブーの定理によると
  より強いことが言える。

.. _tsuboi08.4.3.20:

* 定義 4.3.20: 接触形式

  :math:`\alpha \in \Omega^1(M)` が接触形式であるとは、
  :math:`\alpha \wedge (\dd\alpha)^m \ne 0` であって、
  値がゼロとならないものをいう。

.. _tsuboi08.4.3.21:

* 定義 4.3.21: `接触構造・接触多様体 <https://en.wikipedia.org/wiki/Contact_geometry#Contact_forms_and_structures>`__

  * 接触構造とは、多様体 :math:`M` 上の余次元 1 の平面場 :math:`E` であって、
    各点の周りで :math:`E = \ker\alpha` が成り立つ :math:`\alpha \in \Omega^1(M)` が
    接触形式であるものをいう。

  * 多様体が接触多様体であるとは、それが接触構造を有することを意味する。

.. _tsuboi08.4.3.22:

* 問題 4.3.22: :math:`4m - 1` 次元接触多様体は向き付け可能

  1. 接触形式と非ゼロ関数をそれぞれ :math:`\alpha` と :math:`g` とおく。
  2. 体積形式 :math:`\alpha \wedge (\dd\alpha)^{2m - 1}` を意識して、
     :math:`g\alpha` の定める体積形式を計算する：

     .. math::

        (g\alpha) \wedge (\dd(g\alpha))^{2m - 1}
        = g^{2m}\alpha \wedge (\dd\alpha)^{2m - 1}

     * 式変形において :math:`\dd(g\alpha) = \dd{g}\alpha + g\,\dd\alpha` を用いる。

  3. \1. により :math:`g^{2m} > 0` であるから多様体に対する向き付けは
     :math:`\alpha` のとり方に依存しない。すなわち多様体が向き付け可能であることを意味する。

..

* `レーブ・ベクトル場 <https://en.wikipedia.org/wiki/Contact_geometry#Reeb_vector_field>`__

  ベクトル場 :math:`\xi` がレーブ・ベクトル場であるとは、
  奇数次元多様体上の接触形式 :math:`\alpha` に対するベクトル場であって、

  * :math:`\alpha(\xi) = 1`
  * :math:`i_\xi\dd\alpha = 0`

  を満たすものをいう。

* 接触多様体の接触構造を保つ群は、多様体に推移的に作用する。

.. _tsuboi08.4.3.23:

* 問題 4.3.23: :math:`\CC^{n + 1}` 上のシンプレクティク形式

  * TBW

.. _tsuboi08.4.3.24:

* 定理 4.3.24: ダルブーの定理

  * TBW
