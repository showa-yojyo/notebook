======================================================================
第 4 章 微分形式とベクトル場 1/4
======================================================================

アイソトピーの微分、ベクトル場、微分形式の関係について。

.. contents:: ノート目次

4.1 多様体上のフローとベクトル場
======================================================================

4.1.1 リー微分
----------------------------------------------------------------------
以下、多様体 :math:`M` はコンパクトであるとする。本節の冒頭は復習事項が多い。

* フローはベクトル場によって生成される。
* フローは常微分方程式 :math:`\displaystyle \diff{\varphi_t(x)}{t} = \xi(\varphi_t(x))` の解で定義される。
* 関数 :math:`f` のフロー :math:`\varphi_t` に沿う変化は :math:`(\varphi_t^* f)(x) = (f \circ \varphi_t)(x) = f(\varphi_t(x))` でわかる。
  パラメーター :math:`t` による微分が「変化率」であり、それは :math:`\xi(f)` に等しい。

ここまでが復習。

* 接空間の基底と余接空間の基底は双対基底である。次のように書く：

  .. math::

     \dd x_j\left(\dfrac{\partial}{\partial x_i}\right) = \delta_{ij}

.. _tsuboi08.4.1.1:

* 定義 4.1.1: `リー微分 <http://mathworld.wolfram.com/LieDerivative.html>`__

  * 微分 1 形式のフローに沿う変化率を考える。
    :math:`\alpha = \sum f_i\,\dd x_i` とおくと、そのフローによる引き戻しは次のようになる：

    .. math::

       \varphi_t^*\alpha = \sum_{i = 1}^n f_i(\varphi_t(x))\,\dd \varphi_t^{(i)}.

  * ここで各係数の導関数の :math:`t = 0` における式を見る：

    .. math::

       \left(\diff{}{t}\right)_{t = 0} f_i(\varphi_t(x)) = \sum_{j = 1}^n \dfrac{\partial f_i}{\partial x_j}\xi_j.

  * 一方、引き戻しの基底部分？はこうなっている：

    .. math::

       \dd \varphi_t^{(i)} = \sum_{j = 1}^n \dfrac{\partial \varphi_t^{(i)}}{\partial x_j}\,\dd x_j.

  * 以上を組み合わせて、引き戻しの基底部分？の導関数の :math:`t = 0` における式は：

    .. math::

       \left(\diff{}{t}\right)_{t = 0} \dd \varphi_t^{(i)} = \sum_{j = 1}^n \dfrac{\partial \xi_i}{\partial x_j}\,\dd x_j.

  * フローによる引き戻しの変化率は次の 1 形式になる：

    .. math::

       \left(\diff{}{t}\right)_{t = 0} \varphi_t^*\alpha
       = \sum_{i = 1}^n\sum_{j = 1}^n \dfrac{\partial f_i}{\partial x_j}\xi_j\,\dd x_i
       + \sum_{i = 1}^n\sum_{j = 1}^n f_i \dfrac{\partial \xi_i}{\partial x_j}\,\dd x_j.

    上の式の左辺を :math:`L_\xi \alpha` と書いて、
    これを微分形式 :math:`\alpha` のベクトル場 :math:`\xi` によるリー微分という。

  * 以上の手続きを p 形式について考えると、同様の式で定まる p 形式が得られる。

    .. math::

       L_\xi \alpha = \left(\diff{}{t}\right)_{t = 0} \varphi_t^*\alpha.

.. _tsuboi08.4.1.2:

* 注意 4.1.2: フローで不変な部分多様体と包含写像

  * :math:`N \subset M` をフロー :math:`\varphi_t` で不変な部分多様体であるとする。
  * ベクトル場 :math:`\xi` が :math:`\varphi_t` を、
    ベクトル場 :math:`\xi_N` が :math:`\varphi_t|N` を生成するとする。

  このとき、

  1. :math:`N` 上 :math:`\xi = \iota_* \xi_N.`
  2. :math:`\displaystyle \left(\diff{}{t}\right)_{t = 0} (\varphi_t|N)^* \iota^* \alpha = \left(\diff{}{t}\right)_{t = 0} \iota^* (\varphi_t|N)^* \alpha.`

  であるので :math:`L_{\xi_N}(\alpha|N) = (L_\xi\alpha)|N` が成り立つ。

.. _tsuboi08.4.1.3:

* 問題 4.1.3: ライプニッツ則の確認

  * :math:`\alpha \in \Omega^p(M),\ \beta \in \Omega^q(M)`
  * :math:`\xi \in \mathfrak X(M)`

  のときに次の等式が成り立つ：

  .. math::

     L_\xi(\alpha \wedge \beta) = (L_\xi\alpha) \wedge \beta + \alpha \wedge (L_\xi\beta).

  以下を用いて示すことになる：

  1. :math:`\varphi_t^*` の分配則。
  2. 微分 :math:`\displaystyle \left(\diff{}{t}\right)_{t = 0}` のライプニッツ則。
  3. リー微分の定義。

.. _tsuboi08.4.1.4:

* 問題 4.1.4: リー微分と外微分の演算順序交換

  * :math:`\alpha \in \Omega^p(M)`
  * :math:`\xi \in \mathfrak X(M)`

  のときに次の等式が成り立つ：

  .. math::

     \dd(L_xi\alpha) = L_\xi(\dd \alpha).

  以下を用いて示すことになる：

  1. リー微分の定義。
  2. 微分と外微分の順序交換と :ref:`定理 1.8.11 <tsuboi08.1.8.11>` の外微分と引き戻しの順序交換。
  3. 再びリー微分の定義。

4.1.2 内部積
----------------------------------------------------------------------
.. _tsuboi08.4.1.5:

* 定義 4.1.5: `内部積 <http://mathworld.wolfram.com/InteriorProduct.html>`__

  1. :math:`\alpha \in \Omega^1(M)` のベクトル場 :math:`\xi` による
     リー微分 :math:`L_\xi(\alpha)` の書き換えを考えたい。
  2. :math:`M` 上の関数として :math:`\alpha(\xi) = \sum f_i\xi_i` のようなものが考えられる。
  3. ここで :math:`\dd(\alpha(\xi))` を計算してみると、和の一部が 1. の和の一部と一致する。
  4. 1. と 3. の差 :math:`L_\xi\alpha - \dd(\alpha(\xi))` をとると、
     :math:`\dd \alpha` と :math:`\xi` の成分から得られた積のように見える。
  5. 仮にその差を :math:`i_\xi(\dd\alpha)` とおく：
     :math:`L_\xi\alpha = \dd(\alpha(\xi)) + i_\xi(\dd\alpha).`
     これは後ほどあたらめて定義する。

  :math:`\extp^p T_x^*M` の基底と :math:`T_xM` の基底の内部積として
  :math:`\extp^{p - 1} T_x^*M` の値を対応させる。

  .. math::

     \begin{align*}
     i_{\frac{\partial}{\partial x_k}}(\dd x_{i_1} \wedge \dotsb \wedge \dd x_{i_p}) =
     \begin{cases}
     \displaystyle \sum_{j = 1}^p (-1)^{j - 1}\,
        \dd x_{i_1} \wedge \overset{(\text{pop }\dd x_{i_j})}{\dotsb} \wedge \dd x_{i_p}
        & \quad \text{if }k = i_j,\\
     0  & \quad \text{if }k \notin \set{i_1, \dotsc, i_p}.
     \end{cases}
     \end{align*}

  一般のベクトル場による :math:`\alpha \in \Omega^p(M)` の内部積は次のように定義する：

  .. math::

     i_\xi\alpha = \sum_{i_1 < \dotsb < i_p}\sum_{j = 1}^p (-1)^{j - 1}
       f_{i_1 \dots i_p}\xi_{ij}
       \,\dd x_{i_1} \wedge \overset{(\text{pop }\dd i_j)}{\dotsb} \wedge \dd x_{i_p}
       \in \Omega^{p - 1}(M).

  関数 :math:`f \in \Omega^0(M)` の内部積はゼロとする：

  .. math::

     i_\xi f = 0.

.. _tsuboi08.4.1.6:

* 注意 4.1.6:

  多様体の座標近傍に付随する概念を定義するときには、
  それが本当に座標近傍に依存するのかどうかを示す。

.. _tsuboi08.4.1.7:

* 問題 4.1.7: 内部積の定義は座標近傍のとり方に依存しない

  * \(1) :math:`\alpha \in \Omega^p(M),\ \beta \in \Omega^q(M)` に対して次の式が成り立つ：

    .. math::

       i_\xi(\alpha \wedge \beta) = (i_\xi\alpha) \wedge \beta + (-1)^p\alpha \wedge (i_\xi\beta).

    * 次数付きライプニッツ則とでも言えばよいか？
    * 直接計算で示す。

  * \(2) :math:`\fn{F}{U}V` をユークリッド空間の開集合間の微分同相写像、
    :math:`\alpha \in \Omega^1(V)`, :math:`\xi \in \mathfrak{X}(V)` のとき次が成り立つ：

    .. math::

       F^*(i_\xi\alpha) = i_{{{F\inv}_*}\xi}F^*\alpha.

    1. 記号を次のようにおく：

       * :math:`F(y_1, \dotsc, y_n) = (x_1, \dotsc, x_n) \in V`
       * :math:`\alpha = \sum f_i,\dd x_i`
       * :math:`\xi = \sum \xi_i \dfrac{\partial}{\partial x_i}`

    2. 与式左辺の一部を計算：
       :math:`i_\xi\alpha = \sum f_i\xi_i.`

    3. 与式右辺の一部を計算：

       .. math::

          \begin{align*}
          F^*\alpha &= \sum_i^n \sum_j^n (f_i \circ F)\dfrac{\partial x_i}{\partial y_j}\,\dd y_j.\\
          F_*\inv \xi &= \sum_i^n \sum_j^n (\xi_i \circ F)\dfrac{\partial y_j}{\partial x_i}\dfrac{\partial}{\partial y_j}.
          \end{align*}

    4. 与式右辺を 3. を組み合わせて求める：

       .. math::

          \begin{align*}
          \sum_i^n \sum_j^n(f_i \circ F)\dfrac{\partial x_i}{\partial y_j}(\xi_i \circ F)\dfrac{\partial y_j}{\partial x_i}
          &= \sum_i^n(f_i \circ F)(\xi_i \circ F)\\
          &= F^*(i_\xi\alpha).
          \end{align*}

  * \(3) (2) の :math:`\alpha` を :math:`\Omega^p(V)` としても与式が成り立つ。

    1. :math:`p = 0` のときも確かめる必要があることに注意。
       両辺ゼロで成り立つ。

    2. トリッキーな帰納法を用いる。与式が
       :math:`\alpha \in \Omega^p(V),\ \beta \in \Omega^q(V)` に対して成り立つと仮定する。
       このとき、外積に対しても成り立つことを示せれば話が早い：

       .. math::

          F^*(i_\xi(\alpha \wedge \beta)) = i_{{{F\inv}_*}\xi}F^*(\alpha \wedge \beta).

       式変形で直接示す。

    3. (2) より :math:`p = 1` のときには成り立つから、

       * 単項式 :math:`f_{i_1 \dots i_p}\,\dd x_{i_1} \wedge x_{i_p}` に対して成り立ち、
       * その単項式の線形結合に対しても成り立つ

       から、一般の微分形式に対して成り立つと結論できる。

4.1.3 カルタンの公式
----------------------------------------------------------------------
.. _tsuboi08.4.1.8:

* 命題 4.1.8: カルタンの公式

  :math:`\alpha \in \Omega^p(M),\ \xi \in \mathfrak{X}(M)` に対して次の等式が成り立つ：

  .. math::

     L_\xi\alpha = \dd(\alpha(\xi)) + i_\xi(\dd\alpha).

  :ref:`問題 4.1.7 <tsuboi08.4.1.7>` と同じように証明する：

  1. :math:`p = 0, 1` に対しては前節の議論によって示されている。
  2. 一般の :math:`p` に対して示すために、与式が :math:`\alpha \in \Omega^p(M),\ \beta \in \Omega^q(M)`
     のときに成り立つと仮定し、外積に対して同等の等式：

     .. math::

        L_\xi(\alpha \wedge \beta)
        = \dd(i_\xi(\alpha \wedge \beta)) + i_\xi(\dd(\alpha \wedge \beta))

     が示せれば、同じ論理で一般の場合に対して成り立つことになる。

..

* 復習だと思うが括弧積の成分表示：

  .. math::

     [\xi, \eta] = \sum_j^n\sum_i^n\left(
       \xi_i \dfrac{\partial \eta_j}{\partial x_i}
       - \eta_i \dfrac{\partial \xi_j}{\partial x_i}\right)
       \dfrac{\partial}{\partial x_j}.

.. _tsuboi08.4.1.9:

* 問題 4.1.9: リー微分と括弧積に関する等式 1 形式版

  * :math:`\alpha \in \Omega^1(M)`
  * :math:`\xi, \eta \in \in \mathfrak{X}(M)`

  ならば、次が成り立つ：

  .. math::

     L_\xi L_\eta \alpha - L_\eta L_\xi \alpha = L_{[\xi, \eta]}\alpha.

  証明は直接計算になる：

  1. :math:`\alpha = \sum f_i,\dd x_i` とおく。
  2. :math:`L_\xi\alpha` をそれで表す：

     .. math::

        L_\xi\alpha = \sum_i^n\sum_j^n\left(
          \dfrac{\partial f_i}{\partial x_j}\xi_j
          + f_j \dfrac{\partial \xi_j}{\partial x_i}\right)
          \,\dd x_i.

  3. :math:`L_\xi L_\eta \alpha` と :math:`L_\eta L_\xi \alpha` を直接計算する。
  4. 3. の差を計算すると、本書の解答例の式で言うところの奇数項が打ち消し合って
     次のようになる：

     .. math::

        \sum_i \sum_k \sum_j \left(
          \dfrac{\partial f_i}{\partial x_j}\left(
            \dfrac{\partial \eta_j}{\partial x_k}\xi_k
          - \dfrac{\partial \xi_j}{\partial x_k}\eta_k\right)
          + f_j \dfrac{\partial}{\partial x_i}\left(
            \dfrac{\partial \eta_j}{\partial x_k}\xi_k
          - \dfrac{\partial \xi_j}{\partial x_k}\eta_k\right)\right)
          \,\dd x_i.

     これは括弧積によるリー微分である。

.. _tsuboi08.4.1.10:

* 問題 4.1.10: リー微分と括弧積に関する等式 p 形式版

  :ref:`問題 4.1.9 <tsuboi08.4.1.9>` において :math:`\alpha \in \Omega^p(M)` と
  仮定を一般の次数に緩めても同じ等式が成り立つ。

  1. :math:`p = 0` のとき成り立つことを示す。
     つまり関数 :math:`f \in \Omega^0(M)` で確認する：

     .. math::

        \begin{align*}
        L_\xi L_\eta f - L_\eta L_\xi f
        &= \xi(\eta(f)) - \eta(\xi(f))\\
        &= [\xi, \eta](f)\\
        &= L_{[\xi, \eta]}f.
        \end{align*}

  2. :math:`p = 1` のときは既に :ref:`問題 4.1.9 <tsuboi08.4.1.9>` において証明済みである。
  3. 与式が :math:`\alpha \in \Omega^p(M),\ \beta \in \Omega^q(M)`
     のときに成り立つと仮定し、
     :ref:`問題 4.1.7 <tsuboi08.4.1.7>` での証明技法を用いる。
     つまり、次の等式が成り立つことを示す：

     .. math::

        L_\xi L_\eta (\alpha \wedge \beta) - L_\eta L_\xi (\alpha \wedge \beta)
        = L_{[\xi, \eta]}(\alpha \wedge \beta).

.. _tsuboi08.4.1.11:

* 問題 4.1.11: 内部積とリー微分と括弧積

  * :math:`\alpha \in \Omega^p(M)`
  * :math:`\xi, \eta \in \mathfrak{X}(M)`

  ならば、次が成り立つ：

  .. math::

     i_\xi L_\eta \alpha - L_\eta i_\xi \alpha = i_{[\xi, \eta]}\alpha.

  1. :math:`p = 1` のときを示す。
     :math:`\alpha = \sum f_i\,\dd x_i` に対して直接計算で示す。

  2. あとは :ref:`問題 4.1.7 <tsuboi08.4.1.7>` での証明技法を用いる。
     直接計算で次を示せば十分：

     .. math::

        (i_\xi L_\eta - L_\eta i_\xi)(\alpha \wedge \beta) = i_{[\xi, \eta]}(\alpha \wedge \beta).

.. _tsuboi08.4.1.12:

* 問題 4.1.12: カルタンの公式の応用？

  * \(1) :math:`\omega = \dd x_1 \wedge \dd x_2 \wedge \dd x_3 \in \Omega^3(\RR^3)` とする。
    :math:`\displaystyle \xi = \sum_{i, j = 1}^3 a_{ij}x_j \dfrac{\partial}{\partial x_i}` による
    リー微分 :math:`L_\xi\omega` がゼロとなる条件とは何か。

    ポイントは :math:`\dd \omega = 0` であるから、カルタンの公式が簡単になることを利用することだ。

    .. math::

       \begin{align*}
       L_\xi\omega
       &= \dd(i_\xi\omega) + i_\xi(\dd \omega)\\
       &= \dd(i_\xi\omega)\\
       &= \dd(\xi_1\,\dd x_2 \wedge \dd x_3 - \xi_2\,\dd x_1 \wedge \dd x_3 + \xi_3\,\dd x_1 \wedge \dd x_2)\\
       &= \sum_{i = 1}^3 \dfrac{\partial \xi_i}{\partial x_i}\omega\\
       &= \sum_{i = 1}^3 a_{ii}\omega.
       \end{align*}

    ただし :math:`\displaystyle \xi_1 = \sum_{j = 1}^3 a_{1j}x_j` などとした。

    よって求める条件は :math:`\sum a_{ii} = 0` となる。

  * \(2) :math:`\alpha = x_1\,\dd x_2 \wedge \dd x_3 - x_2\,\dd x_1 \wedge \dd x_3 + x_3\,\dd x_1 \wedge \dd x_2 \in \Omega^2(\RR^3)`
    についてはどうか。

    直接計算による方法と :math:`\dd \alpha = 3 \omega` を利用する方法がある。
    :math:`L_\xi\omega = 0 \iff L_\xi\alpha = 0` を示す。

    1. 直接計算により :math:`\dd \alpha = 3 \omega` がわかる。

    2. :math:`L_\xi\alpha = 0 \implies L_\xi\alpha = 0` を示す：

         :math:`\dd(L_\xi\alpha) = 0` に :ref:`問題 4.1.4 <tsuboi08.4.1.4>` の順序交換を適用して
         :math:`L_\xi(\dd\alpha) = 0`

         ここで 1. を利用すると :math:`L_\xi(\dd\alpha) = L_\xi(3\omega) = 3L_\xi\omega.`

         ゆえに :math:`L_\xi\alpha = 0 \implies L_\xi\alpha = 0` が成り立つ。

    3. :math:`L_\xi\omega = 0 \implies L_\xi\alpha = 0` を示す：

         まず :math:`\displaystyle \eps = \sum_{i, j = 1}^3 \delta_{ij}x_j\dfrac{\partial}{\partial x_i}`
         とおくと次の等式が成り立つ：

         * :math:`[\eps, \xi] = 0`
         * :math:`i_\eps\alpha = 0`

         :ref:`問題 4.1.11 <tsuboi08.4.1.11>` により次の等式が成り立つ：

         .. math::

            i_\eps L_\xi \omega - L_\xi i_\eps \omega = i_{[\eps, \xi]}\omega.

         * :math:`[\eps, \xi] = 0` なので、右辺、結局両辺ともにゼロである。
         * 一方 :math:`L_\xi\omega = 0` であることから、
           左辺は :math:`-L_\xi i_\eps \omega = - L_\xi \alpha` に等しい。

       以上より :math:`L_\xi\omega = 0 \implies L_\xi\alpha = 0` が成り立つ。

    4. 主張の同値性が 2. と 3. により示された。
       従って、求める条件とは (1) のそれと同じである。

4.1.4 微分形式のベクトル場における値
----------------------------------------------------------------------
冒頭、外積代数 :math:`\extp^p T^*M` のベクトル束とは何？

.. _tsuboi08.4.1.13:

* 定義 4.1.13: 微分形式のベクトル場における値

  .. math::

     \alpha(\xi_1, \dotsc, \xi_p) = i_{\xi_p} \dots i_{\xi_1}\alpha.

  内部積で定義される値のようだ。

.. _tsuboi08.4.1.14:

* 注意 4.1.14: 上記の右辺を :math:`p!` で割った値を定義とする流儀もあるらしい。

.. _tsuboi08.4.1.15:

* 問題 4.1.15: 外積の微分形式のベクトル場における値

  :math:`\alpha \in \Omega^p(M),\ \beta \in \Omega^q(M)` のとき、
  外積のベクトル場における値は次のとおり：

  .. math::

     (\alpha \wedge \beta)(\xi_1, \dotsc, \xi_{p + q})
     = \sum_{j_1 < \dotsb < j_p\\k_1 < \dotsb < k_q}
     \operatorname{sgn}
     \begin{pmatrix}
     1 & \cdots & p & p + 1 & \cdots & p + q\\
     j_1 & \cdots & j_p & k_1 & \cdots & k_q
     \end{pmatrix}
     \alpha(\xi_{j_1}, \dotsc, \xi_{j_p})
     \beta (\xi_{k_1}, \dotsc, \xi_{k_q})

  1. :ref:`定義 4.1.13 <tsuboi08.4.1.13>` の右辺を
     :ref:`問題 4.1.7 <tsuboi08.4.1.7>` に基いて軽く計算すると、
     おおまかには次の形になる：

     .. math::

        i_{\xi_{p + q}} \dots i_{\xi_1}(\alpha \wedge \beta)
        = \sum (-1)^?
          (i_{\xi_{j_p}} \dots i_{\xi_{j_1}}\alpha)
          (i_{\xi_{k_q}} \dots i_{\xi_{k_1}}\beta).

  2. :math:`i_\xi i_\eta = -i_\eta i_\xi` なので
     :math:`i_{\xi_{k_q}} \dots i_{\xi_{k_1}} i_{\xi_{j_p}} \dots i_{\xi_{j_1}}(\alpha \wedge \beta)`
     における :math:`(i_{\xi_{j_p}} \dots i_{\xi_{j_1}}\alpha)(i_{\xi_{k_q}} \dots i_{\xi_{k_1}}\beta)`
     の :math:`\operatorname{sgn}` はプラス。

  3. よって 1. の左辺における 2. 最終式の符号は主張の置換の符号に等しい。

.. _tsuboi08.4.1.16:

* 問題 4.1.16: 外微分とリー微分の性質（あるいは定義）

  * \(1) :math:`\alpha \in \Omega^1(M)` に対して次の等式が成り立つ：

    .. math::

       (\dd \alpha)(\xi_1, \xi_2)
       = \xi_1(\alpha(\xi_2)) - \xi_2(\alpha(\xi_1)) - \alpha([\xi_1, \xi_2]).

    1. :ref:`問題 4.1.11 <tsuboi08.4.1.11>` の等式に
       カルタンの公式 :ref:`命題 4.1.8 <tsuboi08.4.1.8>` を適用する。

    2. :ref:`定義 4.1.13 <tsuboi08.4.1.13>` を用いて書き換えれば示される。

  * \(2) :math:`\alpha \in \Omega^p(M)` に対して次の等式が成り立つ：

    .. math::

       (\dd \alpha)(\xi_1, \dotsc, \xi_{p + 1})
       = \sum_{i = 1}^{p + 1} (-1)^{i - 1}\xi_i(\alpha(\xi_1, \overset{(\text{pop }i)}{\dotsc}, \xi_{p + 1}))
         + \sum_{i < j}(-1)^{i + j} \alpha([\xi_i, \xi_j], \xi_1,
           \overset{(\text{pop }i, j)}{\dotsc}, \xi_{p + 1}).

    これは難しい。
    :ref:`問題 4.1.11 <tsuboi08.4.1.11>` の拡張版と（ふつうの）帰納法による。

  * \(3) :math:`\alpha \in \Omega^p(M)` に対して次の等式が成り立つ：

    .. math::

       (L_\xi\alpha)(\xi_1, \dotsc, \xi_p)
       = \xi(\alpha(\xi_1, \dotsc, \xi_p))
         - \sum_{i = 1}^p \alpha(\xi_1, \dotsc, [\xi, \xi_i], \dotsc, \xi_p).

    左辺からひたすら計算する。

    .. math::

       \begin{align*}
       i_{\xi_p}\dots i_{\xi_1} L_\xi\alpha
       &= i_{\xi_p}\dots i_{\xi_2}i_{[\xi_1, \xi]}\alpha +
          i_{\xi_p}\dots i_{\xi_2}L_\xi i_{\xi_x}\alpha\\
       &= i_{\xi_p}\dots i_{[\xi_1, \xi]}\alpha +
          i_{\xi_p}\dots i_{\xi_3}i_{[\xi_2, \xi]} i_{\xi_1} \alpha +
          i_{\xi_p}\dots i_{\xi_3} L_\xi i_{\xi_2} i_{\xi_1} \alpha\\
       &= \cdots\\
       &= \sum_{i = 1}^n i_{\xi_p} \dots i_{[\xi_i, \xi]} \dots i_{xi_1} \alpha
         + L_\xi i_{\xi_p} \dots i_{xi_1} \alpha\\
       &= \xi(\alpha(\xi_1, \dotsc, \xi_p))
         - \sum_{i = 1}^p \alpha(\xi_1, \dotsc, [\xi, \xi_i], \dotsc, \xi_p).
       \end{align*}

    * 最後の等号で、直前の二項が入れ替わった。

  本によってはこちらが外微分・リー微分の定義として採用されているらしい。
