======================================================================
第 3 章 微分形式の積分 1/3
======================================================================

.. contents:: ノート目次

* コンパクト多様体 :math:`M` の :math:`\H^p(M)` が有限次元であるならば：

  .. math::

     \dd \alpha = 0 \quad\text{and } \H^p(M) \owns [\alpha] = 0
     \iff
     \exists \beta \in \Omega^{p - 1}(M) \quad\text{s.t. } \dd \beta = \alpha.

* :math:`\H^p(M)` が自明でないときには、今のところは自力で判定するしかない。
  マイヤー・ビエトリス完全系列やチェック・ドラーム完全系列を調べることになる。

* :math:`[\alpha] = 0` であるかどうかは、有限個の積分により判定が可能となる。

3.1 閉微分 1 形式の積分
======================================================================
連結多様体 :math:`M` 上の曲線 :math:`\fn{\gamma_x}{[0, 1]}\RR` 上で積分を定義する。

* これは :math:`x_0, x \in M` を結ぶ曲線であり、
  :math:`\gamma_x(0) = x_0,\ \gamma_x(1) = x` を満たすものとしておく。

* 関数 :math:`\fn{f}{M}\RR` について閉 1 形式 :math:`\alpha` を
  :math:`\alpha = \dd f` で定義する。

* 下の左のふたつの意味が同じ積分を、右のふたつの意味が同じ積分で定義する：

  .. math::

     \int_{\gamma_x}\!\alpha = \int_{\gamma_x}\!\dd f =
     \int_0^1\!\gamma_x^* \alpha = \int_0^1\!\gamma_x^*\,\dd f.

  これの根拠は次の式が成り立つことによる：

  .. math::

     f(x) - f(x_0) = f(\gamma_x(1)) - f(\gamma_x(0))
     = \int_0^1\!\diff{f\circ \gamma_x}{t}\,\dd t.

  積分記号の中身全部は :math:`\gamma_x \dd f` である。
  これは :ref:`定義 2.1.7 <tsuboi08.2.1.7>` と :ref:`命題 2.3.6 <tsuboi08.2.3.6>` による。

* この閉 1 形式に対して積分の値が経路のとり方に依らなければ、
  :math:`\displaystyle f(x) = \int_{\gamma_x}\!\alpha` と定義すれば
  :math:`\alpha = \dd f` となる。

* :math:`\alpha = \dd f` なる :math:`f` が存在することと、
  すべての閉曲線 :math:`\gamma` について :math:`\displaystyle \int_\gamma\!\alpha = 0` であることは
  同値である。

* :math:`\H^p(M) \owns [\alpha] \ne 0` ならば、
  :math:`\displaystyle \int_\gamma\!\alpha \ne 0` なる :math:`f` が存在する。

.. _tsuboi08.3.1.1:

* 例題 3.3.1: 全微分すると与えられた微分形式に一致する関数の存在する十分条件

  * :math:`M` をコンパクト多様体、
  * :math:`\H^1(M) \cong \RR^k,`
  * 次の条件を満たす多様体上の閉曲線 :math:`\gamma_1, \dotsc, \gamma_k` が存在する：

    .. math::

       \int_{\gamma_i}\!\alpha = 0\quad\text{for }i = 1, \dotsc, k.

  このとき :math:`\alpha = \dd f` を満たす多様体上の関数 :math:`f` が存在する。

  * :math:`\H^1(M)` の基底を :math:`[\alpha_1], \dotsc, [\alpha_k]` とおく。
  * 線形代数の各種命題の証明にありがちなアルゴリズムにより、
    次の正方行列が正則であるように閉曲線 :math:`\gamma_1, \dotsc, \gamma_k` がとれる：

    .. math::

       \left(\int_{\gamma_j}\!\alpha_i\right)_{i, j = 1, \dotsc, k}.

  * 閉 1 形式 :math:`\displaystyle [\alpha] = \sum_{i = 1}^k b_i [\alpha_i]`
    となるように各 :math:`b_i \in \RR` をとる。

    * :math:`\displaystyle \int_{\gamma_j}\!\alpha = \sum_{i = 1}^k b_i \int_{\gamma_j}\!\alpha_i = 0,`
    * :math:`\det\left(\int_{\gamma_j}\!\alpha_i\right) \ne 0`

    より、すべての :math:`b_j = 0`

  * ゆえに :math:`\int_{\gamma_i}\!\alpha = 0 \implies \H^1(M) \owns [\alpha] = 0.`
  * 前ページの黒丸より :math:`\alpha = \dd f.`

.. _tsuboi08.3.1.2:

* 例 3.1.2: トーラス :math:`T^n = \RR^n/\ZZ^n` での事情

  * :math:`\H^1(T^n) \cong \RR^n` であるので（前章で何度か言及された）
    基底として :math:`[\dd x_1], \dotsc, [\dd x_n]` がとれる。
  * 曲線 :math:`\fnm{\gamma_j}{[0, 1]}{\RR^n}{t}t\bm e_j` に対して
    :math:`\displaystyle \int_{\gamma_j}\!\dd x_i = \delta_{ji}` が成り立つ。
    右辺はクロネッカーの記号。

  * 閉形式 :math:`\alpha \in \Omega^1(T^n)` に対して、
    各曲線に沿う積分がゼロであるならば、:math:`\alpha = \dd f` を満たす
    トーラス上の関数 :math:`f` が存在する。

  * 一般には次を満たす関数 :math:`f` が存在する：

    .. math::

       \alpha - \sum_{i = 1}^n \int_{\gamma_i}\!\alpha \,\dd x_i = \dd f.

.. _tsuboi08.3.1.3:

* 問題 3.1.3: :math:`C^\infty` ホモトピックならば積分値は経路の取り方に依らない

  * :math:`C^\infty` 級関数 :math:`\fn{F}{[0, 1]\times[0, 1]}M` が

    .. math::

       \begin{align*}
       F(0, t) &= \gamma_0(t),\quad F(s, 0) = x_0,\\
       F(1, t) &= \gamma_1(t),\quad F(s, 1) = x_1
       \end{align*}

    を満たすとすると、すべての閉 1 形式 :math:`\alpha` の経路積分は同じである：

    .. math::

       \begin{align*}
       \int_{\gamma_1}\!\alpha - \int_{\gamma_0}\!\alpha
       &= \int_0^1\!\gamma_1^*\alpha - \int_0^1\!\gamma_0^*\alpha\\
       &= \int_{[0, 1]\times\set{0}}\!F^*\alpha
        + \int_{\set{1}\times[0, 1]}\!F^*\alpha
        - \int_{[0, 1]\times\set{1}}\!F^*\alpha
        - \int_{\set{0}\times[0, 1]}\!F^*\alpha\\
       &= \int_{[0, 1]\times[0, 1]}\!F^*\,\dd \alpha\\
       &= 0.
       \end{align*}

    * 最初の等号は 1 形式の積分の定義による。本節冒頭参照。
    * 二番目の等号はホモトピックであるという仮定による。
    * 三番目の等号は長方形上の 1 形式に対する積分であることによる。
      :ref:`命題 1.3.1 <tsuboi08.1.3.1>` 参照。
    * 最後の等号は与えられた微分形式が閉形式であることによる。

3.2 単体からの写像に沿う積分
======================================================================
まずは直方体。p 形式を p 次元直方体上で積分する。

* :math:`\fn{\kappa}{[a_1, b_1] \times \dotsb \times [a_p, b_p]}M`
* :math:`\alpha \in \Omega^p(M)`

このとき :math:`\kappa^*\alpha \in \Omega^p([a_1, b_1] \times \dotsb \times [a_p, b_p]).`
:math:`\kappa^*\alpha = f(t_1, \dotsc, t_p)\,\dd t_1 \wedge \dotsb \wedge \dd t_p` となる
関数 :math:`f` が存在するので、直方体上の p 形式の積分を次で定義する：

.. math::

   \int_\kappa\!\alpha = \int_\id\!\kappa^*\alpha
   = \int_{a_1}^{b_1}\dotsi\int_{a_p}^{b_p}\!f(t_1, \dotsc, t_p)\,\dd t_1 \dots \dd t_p.

次に単体に沿う積分を定義する。

* p 次元標準 `単体 <http://mathworld.wolfram.com/Simplex.html>`__ を定義する：

  .. math::

     \Delta^p = \set{(x_1, \dotsc, x_p) \in \RR^p \sth 1 \ge x_1 \ge \dotsb \ge x_p \ge 0}.

* 単体からの写像に沿う積分を次で定義する：

  .. math::

     \int_{\Delta^p}\!f(x_1, \dotsc, x_p)\,\dd t_1 \wedge \dotsb \wedge \dd t_p
     = \int_{x_1 = 0}^1\dotsi \int_{x_i = 0}^{x_{i - 1}}\dotsi \int_{x_p = 0}^{x_{p - 1}}\!
     f(x_1, \dotsc, x_p)\,\dd x_p \dots \dd x_i \dots \dd x_1.

* :math:`C^\infty` 級写像 :math:`\fn{\sigma}{\Delta^p}M` に沿う積分を次で定義する：

  .. math::

     \int_\sigma\!\alpha = \int_{\Delta^p}\!\sigma^*\alpha.

  * 写像 :math:`\sigma` を :math:`C^\infty` 級特異 p 単体
    or p 次元 :math:`C^\infty` 級特異単体という。

  * 特異 p 単体有限個の形式的な線形結合を :math:`C^\infty` 級特異 p チェイン
    or p 次元 :math:`C^\infty` 級特異チェインという。

    .. math::

       \sum_{i = 1}^j a_i \sigma_i, \quad a_i \in \RR.

* :math:`C^\infty` 級特異 p チェイン上の積分を次で定義する：

  .. math::

     \int_{\sum a_i \sigma_i}\!\alpha = \sum a_i \int_{\sigma_i}\!\alpha = \sum a_i\int_{\Delta^p}\!\sigma_i^*\alpha.

以下、:ref:`例題 1.6.9 <tsuboi08.1.6.9>` で見たストークスの定理の単体バージョンを考えたい。

* 写像 :math:`\fn{\eps_k}{\Delta^{p - 1}}\Delta^p` を次で定義する：

  .. math::

     \eps_k\colon (x_1, \dotsc, x_{p - 1}) \longmapsto
     \begin{cases}
     (1, x_1, \dotsc, x_{p - 1}) & \quad \text{if } k = 0\\
     (x_1, \dotsc, x_k, x_k, \dotsc, x_{p - 1}) & \quad \text{if } 0 < k < p\\
     (x_1, \dotsc, x_{p - 1}, 0) & \quad \text{if } k = p
     \end{cases}

  * 試しに 2 次元から 3 次元の :math:`\eps_k` を書き出してみる。
    三角形から四面体各面への 4 つの写像を意味する：

    .. math::

       \begin{align*}
       \eps_0(x_1, x_2) &= (1, x_1, x_2)\\
       \eps_1(x_1, x_2) &= (x_1, x_1, x_2)\\
       \eps_2(x_1, x_2) &= (x_1, x_2, x_2)\\
       \eps_3(x_1, x_2) &= (x_1, x_2, 0)
       \end{align*}

    * :math:`\eps_0, \eps_p` は幾何的には合同変換。埋め込みのようなものか。
    * それ以外でも微分同相写像のように思える。

* 境界 :math:`\partial \sigma` を次で定義する：

  .. math::

     \partial \sigma = \sum_{k = 0}^p (-1)^k \sigma \circ \eps_k.

.. _tsuboi08.3.2.1:

* 定理 3.2.1: ストークスの定理単体バージョン

  :math:`\sigma` を特異 p 単体、
  :math:`\alpha \in \Omega^{p - 1}(M)` とすると：

  .. math::

     \int_\sigma\!\dd\alpha = \int_{\partial \sigma}\!\alpha.

  証明の方針は、まず :math:`\sigma^*\alpha` を次のように表したときに：

  .. math::

     \begin{align*}
     \sigma^*\alpha &= \sum_{k = 1}^{p - 1}\alpha_k
     = \sum_{k = 1}^{p - 1}(-1)^k f_k \dd x_1 \wedge \dotsb
       \wedge \dd x_{k - 1} \wedge \dd x_{k + 1} \dotsb
       \wedge \dd x_p,
     \\
     \sigma^* \dd\alpha &= \dd \sigma^*\alpha =
     \sum_{k = 1}^p \frac{\partial f_k}{\partial x_k}\dd x_1 \wedge \dd x_p
     \end{align*}

  和の各項における、次の等式を示されれば、主張も示されることになる：

  .. math::

     \int_{\Delta^p}\!\frac{\partial f_k}{\partial x_k}\dd x_1 \wedge \dotsb \wedge \dd x_p
     = \int_{\sum_{i = 0}^p(-1)^i\eps_i}\!\alpha_k.

  以下、:math:`k = p` のときとそれ以外とで場合分けして示す。

  * :math:`k = p` のとき：

    .. math::

       \begin{align*}
       \int_{\Delta^p}\!\frac{\partial f_p}{\partial x_p}\,\dd x_1 \wedge \dotsb \wedge \dd x_p
       &= \int_{x_1 = 0}^1\dotsi\int_{x_p = 0}^{x_{p - 1}}\!\frac{\partial f_p}{\partial x_p}\,\dd x_p \dots \dd x_1\\
       &= \int_{x_1 = 0}^1\dotsi\int_{x_{p - 1} = 0}^{x_{p - 2}}\!f_p(x_1, \dotsc, x_{p - 1}, x_{p - 1}) - f_p(x_1, \dotsc, x_{p - 1}, 0)\,\dd x_{p - 1} \dots \dd x_1\\
       &= \int_{\eps_{p - 1} - \eps_p}\!(-1)^{p - 1}\alpha_p\\
       &= \int_{(-1)^{p - 1}\eps_{p - 1} + (-1)^p\eps_p}\!\alpha_p\\
       &= \int_{\sum_{i = 0}^p (-1)^i\eps_i}\!\alpha_p.
       \end{align*}

    * 最初の等号は単体に沿う積分の定義そのもの。
    * 二番目の等号は中央の定積分を展開しただけ。
    * 三番目の等号。ここがわからない。かなりギャップがあるような。
    * 四番目の等号は :math:`i \ne p - 1, p` ならば
      :math:`\displaystyle \int_{\eps_i}\!(-1)^p\alpha_p = 0` から導かれる。
    * 最後の等号は和をシグマ記号にまとめただけ。

    となって OK となる。

  * :math:`k < p` のとき：細かい技巧があるようだ。

    * :math:`\displaystyle F(x_1, \dotsc, x_k) = \int_{x_{k + 2} = 0}^{x_{k + 1}}\dotsi\int_{x_p = 0}^{x_{p - 1}}\!\frac{\partial f_k}{\partial x_k}\,\dd x_p \dots \dd x_{k + 2}`
      とおく。
    * ふつうのニ変数の積分の順序交換により、次のように書き換えられる：

      .. math::

         \int_{x_k = 0}^{x_{k - 1}}\int_{x_{k + 1} = 0}^{x_k}\!F(\cdot)\,\dd x_{k + 1}\dd x_k
         = \int_{x_{k + 1} = 0}^{x_{k - 1}}\int_{x_k = x_{k + 1}}^{x_{k - 1}}\!F(\cdot)\,\dd x_k\dd x_{k + 1}.

      この右辺の内側の定積分を展開すると次のようになる：

      .. math::

         \int_{x_{k + 2} = 0}^{x_{k + 1}}\dotsi\int_{x_p = 0}^{x_{p - 1}}\!
         f_k(x_1, \dotsc, x_{k - 1}, x_{k - 1}, x_{k + 1}, \dotsc, x_p) -
         f_k(x_1, \dotsc, x_{k - 1}, x_{k + 1}, x_{k + 1}, \dotsc, x_p)\,
         \dd x_p \dots \dd x_{k + 2}.

    以上を利用して：

    .. math::

       \begin{align*}
       \int_{\Delta^p}\!\frac{\partial f_k}{\partial x_k}\,\dd x_1 \wedge \dotsb \wedge \dd x_p
       &= \int_{x_1 = 0}^1\dotsi\int_{x_{k - 1} = 0}^{x_{k - 2}}\int_{x_{k + 1} = 0}^{x_{k - 1}}\int_{x_{k + 2} = 0}^{x_{k + 1}}\dotsi\int_0^{x_{p - 1}}
          \!f_k(\cdot) - f_k(\cdot)\,
          \dd x_p \dots \dd x_{k + 2} \dd x_{k + 1} \dd x_{k - 1} \dots \dd x_1\\
       &= \int_{\eps_{k - 1} - \eps_k}\!(-1)^{k - 1}\alpha_k\\
       &= \int_{(-1)^{k - 1}\eps_{k - 1} + (-1)^k\eps_k}\!\alpha_k\\
       &= \int_{\sum_{i = 0}^k (-1)^i\eps_i}\!\alpha_k.
       \end{align*}

    * 最初の等号：単体に沿う積分の定義に上記を加味した変形による。
    * 二番目の等号：:math:`k + 1` 以降を :math:`k` に置き換えることで得られるらしい。
    * 三番目の等号：:math:`j \ne k - 1, k` ならば
      :math:`\displaystyle \int_{\eps_i}\!(-1)^k\alpha_k = 0` から導かれる。
    * 以降の等号成立の理由については先ほどの場合を参照。

    となって OK となる。

  以上でストークスの定理単体バージョンが示された。

..

* 上記定理の検討？

  特異 p チェインの次の集合を定義する：

  .. math::

     S_p^\infty(M) = \Set{\sum_i^{\text{finite}}a_i \sigma_i
       \Sth a_i \in \RR,\ \sigma_i \in C^\infty(\Delta^p, M)}

  このとき、次の双線型写像が考えられる（ストークスの定理が成り立つ）：

  .. math::

     S_p^\infty(M) \times \Omega^p(M) \longto \RR,
     \quad
     (c, \alpha) \longmapsto
     \int_c\!\alpha = \sum a_i \int_{\sigma_i}\!\alpha

  * 境界準同型 :math:`\partial` が特異 p チェイン全体 :math:`S_*^\infty(M)` に
    対して定義されていて :math:`\partial \circ \partial = 0.`
    そこで次の系列は複体となり、これを :math:`C^\infty` 級特異単体複体という：

    .. math::

       \require{AMScd}
       \begin{CD}
       0 @<{\partial}<< S_0^\infty(M) @<{\partial}<< S_1^\infty(M) @<{\partial}<< \cdots
       \end{CD}

  * :math:`Z_p^\infty(M) = \ker(\fn{\partial}{S_p^\infty}S_{p - 1}^\infty)` の元を
    p 次元 :math:`C^\infty` 級特異サイクルという。

  * :math:`B_p^\infty(M) = \im(\fn{\partial}{S_{p + 1}^\infty}S_p^\infty)` の元を
    p 次元 :math:`C^\infty` 級特異バウンダリーという。

  * :math:`H_p^\infty(M) = Z_p^\infty(M) / B_p^\infty(M)` を
    p 次元 :math:`C^\infty` 級特異ホモロジー群という。

* :math:`\alpha \in Z^p(M)` と :math:`\beta \in B^{p - 1}(M)` とが
  :math:`\alpha = \dd \beta` を満たすならば、
  積分 :math:`\displaystyle \int_c\!\alpha = \int_c\!\dd \beta = \int_{\partial c}\!\beta` は
  :math:`\partial c = 0` なる :math:`c` に対しては常にゼロである。

* :math:`\alpha \in Z^p(M)` と :math:`c \in S_p^\infty(M)` について
  :math:`\int_c\!\alpha = 0 \implies \exists \beta \in B^{p - 1}(M)\text{ s.t. }\alpha = \dd \beta.`

  * :math:`c \in S_p^\infty(M) \iff \partial c = 0.`

* :math:`c \in B_p(M)` であって :math:`c = \partial b` であるとするならば、
  :math:`\forall \alpha \in Z^p(M),\ \displaystyle \int_c\!\alpha = \int_{\partial b}\!\alpha = \int_b\!\dd \alpha = 0.`

* :math:`H_p^\infty(M)` の基底の各代表 :math:`c_i \in S_p^\infty(M)` に対して
  :math:`\displaystyle \int_{c_i}\!\alpha = 0 \implies \alpha = \dd \beta.`

* :math:`k = \dim H_p^\infty(M) = \dim \H^p(M)` とし、
  基底 :math:`[c_1], \dotsc, [c_k] \in H_p^\infty(M)` と :math:`\alpha \in Z^p(M)` が
  :math:`\displaystyle \int_{c_i}\!\alpha = 0` を満たすならば
  :math:`\exists \beta \in B^{p - 1}(M)\text{ s.t. }\alpha = \dd \beta.`

  * cf. :ref:`例題 3.3.1 <tsuboi08.3.1.1>`

.. figure:: /_static/cd-topology-singular-homology.png
   :align: center
   :alt: math.topology.algebraic.singular.homology
   :width: 756px
   :height: 370px
   :scale: 100%

.. _tsuboi08.3.2.2:

* 注意 3.2.2: :math:`C^\infty` 級特異単体複体のチェインを定義する係数を
  整数にするとどうなるかを説明している。

.. _tsuboi08.3.2.3:

* 問題 3.2.3: ホモトピックサイクルについては積分が一致する

  * :math:`c_0, c_1 \in S_p^\infty(M)` がホモトピックサイクルであるとは、
    :math:`\displaystyle c_t = \sum_i a_i \sigma_i^{(t)}\quad(t \in [0, 1])` が
    写像 :math:`(t, x) \longmapsto \sigma_i^{(t)}(x)` が滑らかであるように与えられていることをいう。

  * :math:`\alpha \in Z^p(M)` に対して :math:`\displaystyle \int_{c_0}\!\alpha = \int_{c_1}\!\alpha.`

  * 写像 :math:`\fn{F_i}{[0, 1]\times \Delta^p}{M}{(x, t)}\sigma_i^{(t)}(x)` を定義する。

    .. math::

       \partial F_i = \sigma_0^{(1)} - \sigma_0^{(0)} - \sum_{k = 0}^p (-1)^k F_i \circ (\id, \eps_k).

  * :math:`c_i \in S_p^\infty(M)` の性質によって：

    .. math::

       \begin{align*}
       &\partial c_t = \sum_i a_i \sum_{k = 0}^p \sigma_i^{(t)}\circ \eps_k = 0,\\
       &\text{i.e. } \sum_i a_i \sum_{k = 0}^p (-1)^k F_i \circ (\id, \eps_k) = 0.\\
       &\therefore
       \partial \sum_i a_i F_i = \sum_i a_i \sigma_i^{(1)} - \sum_i a_i \sigma_i^{(0)} = c_1 - c_0.
       \end{align*}

  * :ref:`定理 3.2.1 <tsuboi08.3.2.1>` および :ref:`例題 1.6.9 <tsuboi08.1.6.9>` のどちらかを利用できる。
    ストークスの定理を :math:`[0, 1] \times \Delta^p` からの写像に沿って考えるか、
    :math:`[0, 1] \times \Delta^p` を単体に分割して考えることで次を得る：

    .. math::

       \begin{align*}
       0 = \int_F\!\dd\alpha
       &= \int_{\partial F}\!\alpha\\
       &= \int_{c_1}\!\alpha - \int_{c_0}\!\alpha.
       \end{align*}
