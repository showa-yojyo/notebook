======================================================================
第 4 章 微分形式とベクトル場
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

* 定義 4.1.5: 内部積

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
        (\dd x_{i_1} \wedge \overset{(\text{pop }\dd x_{i_j})}{\dotsb} \wedge \dd x_{i_p})
        & \quad \text{if }k = i_j,\\
     0  & \quad \text{if }k \notin \set{i_1, \dotsc, i_p}.
     \end{cases}
     \end{align*}

  一般のベクトル場による :math:`\alpha \in \Omega^p(M)` の内部積は次のように定義する：

  .. math::

     i_\xi\alpha = \sum_{i_1 < \dotsb < i_p}\sum_{j = 1}^p (-1)^{j - 1}
       f_{i_1 \dots i_p}\xi_{ij}
       \,\dd x_{i_1} \wedge \overset{(\text{pop }\dd i_j)}{\dotsb} \wedge \dd x_{i_p}.

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
          F^*\alpha &= \sum\sum(f_i \circ F)\dfrac{\partial x_i}{\partial y_j}\,\dd y_j.\\
          F_*\inv \xi &= \sum\sum(\xi_i \circ F)\dfrac{\partial y_j}{\partial x_i}\dfrac{\partial}{\partial y_j}.
          \end{align*}

    4. 与式右辺を 3. を組み合わせて求める：

       .. math::

          \begin{align*}
          \sum\sum(f_i \circ F)\dfrac{\partial x_i}{\partial y_j}(\xi_i \circ F)\dfrac{\partial y_j}{\partial x_i}
          &= \sum(f_i \circ F)(\xi_i \circ F)\\
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
TBW

.. _tsuboi08.4.1.8:

* 命題 4.1.8: カルタンの公式

.. _tsuboi08.4.1.9:

* 問題 4.1.9: リー微分と括弧積に関する等式 1 形式版

.. _tsuboi08.4.1.10:

* 問題 4.1.10: リー微分と括弧積に関する等式 p 形式版

.. _tsuboi08.4.1.11:

* 問題 4.1.11: 内部積とリー微分と括弧積

.. _tsuboi08.4.1.12:

* 問題 4.1.12: カルタンの公式の応用？

4.1.4 微分形式のベクトル場における値
----------------------------------------------------------------------
TBW

.. _tsuboi08.4.1.13:

* 定義 4.1.13: 微分形式のベクトル場における値

.. _tsuboi08.4.1.14:

* 注意 4.1.14:

.. _tsuboi08.4.1.15:

* 問題 4.1.15: 外積と微分形式のベクトル場における値

.. _tsuboi08.4.1.16:

* 問題 4.1.16: 外微分とリー微分の性質（あるいは定義）

4.2 リー群
======================================================================
TBW
