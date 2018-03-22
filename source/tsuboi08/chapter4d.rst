======================================================================
第 4 章 微分形式とベクトル場 4/4
======================================================================

.. contents:: ノート目次

4.4 リーマン多様体上の微分形式とベクトル場
======================================================================
* リーマン計量 :math:`\fn{g_x}{T_xM \times T_xM}\RR` は余接空間のテンソル積の元である：

  .. math::

     g_x \in T_x^*M \otimes T_x^*M.

* 座標近傍の変換：

  .. math::

     g = \sum_{i, j}^n g_{ij}(\bm x)\dd x_i \otimes \dd x_j
       = \sum_{k, l}^n \sum_{i, j}^n g_{ij}(\bm x(\bm y))
           \frac{\partial x_i}{\partial y_k}
           \frac{\partial x_j}{\partial y_l}
           \dd y_k \otimes \dd y_l

  を見ると、リーマン計量 :math:`g` はベクトル束 :math:`(T^*M \otimes T^*M, M, p)` における
  射影 :math:`\fn{p}{T^*M \times T^*M}M` に対し :math:`p \circ g = id_M` になるような
  切断である。
  細かく言うと、対称なテンソル積のなす :math:`\dfrac{n(n + 1)}{2}` 次元ベクトル空間をファイバーとする
  部分ベクトル束の切断である。

* リーマン計量があると、ベクトル場と 1 形式の間に全単射が存在する：

  .. math::

     \alpha(v) = g_x(v, \xi(x))\quad\forall v \in T_xM.

  * :math:`g_x` が双線型かつ非退化であることに注意。

* 逆に 1 形式 :math:`\alpha` に対して上の式を満たすベクトル場 `\xi` が一意的に定まる。

  * :math:`\displaystyle \alpha_i = \sum_{j = 1}^n g_{ij} \xi_j` から
    :math:`\displaystyle \xi_j = \sum_{i = 1}^n g^{ij}\alpha_i` とすればよい。

  * 座標近傍上では常に :math:`\displaystyle \sum_i^n\alpha_i v_i = \sum_{i, j}^n g_{ij}v_i\xi_j` である。

* 逆行列 :math:`g^{ij}` に関しては双線型 :math:`\fn{\overline g_x}{T_x^*M \times T_x^M}\RR` が
  次で定まる：

  .. math::

     \overline g_x(\sum_{i = 1}^n \alpha_i\,\dd x_i, \sum{j = 1}^n\beta_j\,\dd x_j)
     = \sum_{i, j = 1}^n g^{ij}\alpha_i\beta_j.

  さらに :math:`\alpha, \beta` がベクトル場 :math:`\xi, \eta` にそれぞれ対応するときは：

  .. math::

     \begin{align*}
     \overline g_x(\alpha, \beta)
     &= \sum_{i, j = 1}^n g^{ij}\alpha_i\beta_j\\
     &= \sum_{i, j = 1}^n g^{ij} \sum_{k = 1}^n g_{ik}\xi_k \sum_{l = 1}^n g_{il}\eta_l\\
     &= \sum_{k, l = 1}^n g_{kl}\xi_k\eta_l.
     \end{align*}

* 接空間 :math:`T_xM` の正規直交基底

  .. math::

     \Set{\xi^{(k)} = \sum_{i = 1}^n \xi_i^{(k)}\frac{\partial}{\partial x_i}}

  をとる。正規直交基底なので :math:`g_x(\xi^{(k)}, \xi^{(l)}) = \delta_{kl}` となる。

  これに対応する余接空間 :math:`T_x^*M` の基底

  .. math::

     \Set{\alpha^{(n)} = \sum_{i, j = 1}^n g_{ij}\xi_j^{(k)}\,\dd x_i}

  もまた正規直交基底となる。これは先述の座標近傍上における等式による。

* 正規直交基底が存在することは、グラム・シュミットの直交化法により言える。
  「ベクトル」の大きさの調整にリーマン計量を用いる：

  .. math::

     \begin{align*}
     v_1 &= \frac{\partial}{\partial x_1},\\
     \xi^{(1)} &= \frac{v_1}{\sqrt{g(v_1, v_1)}}
     \end{align*}

  から開始して、:math:`\xi^{(1)}, \dotsc, \xi^{(k)}` が定まる。それから：

  .. math::

     \begin{align*}
     v_{k + 1} &= \frac{\partial}{\partial x_{k + 1}} - \sum_{i = 1}^k
       g\left(\xi^{(i)}, \frac{\partial}{\partial x_{k + 1}}\right)\xi^{(i)},\\
     \xi^{(k + 1)} &= \frac{v_{k + 1}}{\sqrt{g(v_{k + 1}, v_{k + 1})}}
     \end{align*}

  と正規化する。

..

* `リーマン多様体の体積形式 <https://en.wikipedia.org/wiki/Volume_form#Riemannian_volume_form>`__ 

  * 余接空間 :math:`T_x^*M` の正規直交基底 :math:`\set{\alpha^{(k)}}` に対して、
    n 形式 :math:`\alpha^{(1)} \wedge \dotsb \wedge \alpha^{(n)}` は（符号を除いて）リーマン計量で定まる。

  * 多様体が向き付け可能であれば、各座標近傍上で正の正規直交基底がとれる。
    そのとき、上述の n 形式の外微分をとると、二つの座標近傍の共通部では
    座標変換のよる引き戻しとなる。このような非ゼロ微分形式をリーマン多様体の
    体積形式という。

.. _tsuboi08.4.4.1:

* 問題 4.4.1: 向き付けられたリーマン多様体の向き付けられた座標近傍における体積形式

  この問題でリーマン多様体の体積形式を具体的に求める。

  1. リーマン計量を :math:`g_{ij}` とする：

     .. math::

        g = \sum g_{ij} \dd x_i \otimes \dd x_j.

  2. 余接空間 :math:`T_x^*M` の正規直交基底を :math:`\alpha^{(k)}` とする：

     .. math::

        \alpha^{(k)} = \Set{\sum_{i = 1}^n \alpha^{(k)}\,\dd x_i}.

  3. 本節冒頭で述べた双線型写像を適用すると
     :math:`\displaystyle \sum_{i, j = 1}^n g^{ij}\alpha_i^{(k)}\alpha_i^{(l)} = \delta_{kl}`
     すなわち :math:`{}^t\!AG\inv A = I_n` の形に書ける。
     ここで :math:`G = (g_{ij}),\ A = (\alpha_i^{(k)})` とした。

  4. :ref:`問題 1.8.5 <tsuboi08.1.8.5>` の結果より

     .. math::

        \alpha^{(1)} \wedge \dotsb \wedge \alpha^{(n)}
        = \det A \,\dd x_1 \wedge \dotsb \wedge \dd x_n.

  5. \3. より :math:`(\det A)^2 = \det G` である。

  6. \4. と 5. より求める体積形式は次のように表せる：

     .. math::

        \alpha^{(1)} \wedge \dotsb \wedge \alpha^{(n)}
        = \sqrt{\det G}\,\dd x_1 \wedge \dotsb \wedge \dd x_n.

  この右辺が向き付けられたリーマン多様体 :math:`(M, g)` の体積形式である。
  以下で :math:`\Omega_{(M, g)}` とあるのは、これである。

.. _tsuboi08.4.4.2:

* 定理 4.4.2: ガウス・グリーンの公式

  向き付けられたコンパクトリーマン多様体の体積形式に関するベクトル場の発散に関する公式だ。

  * :math:`\Omega_{(M, g)}` をリーマン多様体の体積形式とし、
  * :math:`\xi` を :math:`L_\xi\Omega_{(M, g)} = \div(\xi) \Omega_{(M, g)}`
    を満たすベクトル場であるとし、
  * :math:`n` は単位ベクトル場であり、多様体の境界 :math:`\partial M` において
    それに直交かつ外向きであるとする。

  とする。このとき、次の積分に関する等式が成り立つ：

  .. math::

     \int_M\!\div(\xi)\Omega_{(M, g)}
     = \int_{\partial M}\!g(n, \xi)\Omega_{(\partial M, g|\partial M)}.

  この積分は、境界がない多様体についてはゼロであると解釈する。

  1. ベクトル場 :math:`\xi` についての仮定および :ref:`命題 4.1.8 <tsuboi08.4.1.8>`
     カルタンの公式より左辺を次のように変形できる：

     .. math::

        \begin{align*}
        \int_M\!\div(\xi)\Omega_{(M, g)}
        &= \int_M\!L_\xi\Omega_{(M, g)}\\
        &= \int_M\!\dd i_\xi\Omega_{(M, g)}\\
        &= \int_{\partial M}\!i_\xi \Omega_{(M, g)}.
        \end{align*}

     * 最後の等式はストークスの定理による。

  2. ベクトル場 :math:`n` は定義域を多様体全体に拡張してよい。
     次のように決めて構わない：

     .. math::

        i_n\Omega_{(M, g)}|\partial M = \Omega_{(\partial M, g|\partial M)}.

  3. 正規直交基底 :math:`\set{e_i}\ (i = 1, \dotsc, n)` をとる。
     ただし、境界に沿って局所的に :math:`n = e_1` となるようなものとする。
     このとき :math:`\xi = \sum a_i e_i` について：

     .. math::

        \begin{align*}
        i_\xi\Omega_{(M, g)}|\partial M
        &= a_1 e_2^* \wedge \dotsb \wedge e_n^*\\
        &= g(n, \xi)\Omega_{(\partial M, g|\partial M)}.
        \end{align*}

     これを 1. の右辺に適用すればガウス・グリーンの公式を得る。

.. _tsuboi08.4.4.3:

* 例 4.4.3: ガウス・グリーンの公式の特殊化

  * 領域 :math:`B \subset \RR^2` に対して次が成り立つ：

    .. math::

       \int_B\!\left(\frac{\partial \xi_1}{\partial x_1} + \frac{\partial \xi_2}{\partial x_2}\right)\,\dd x_1\dd x_2
       = \int_{\partial B}\!n \cdot \xi\,\dd s.

    ただし :math:`s` は領域の境界 :math:`\partial B` の向きに沿ったパラメーターとする。

  * 領域 :math:`B \subset \RR^3` に対して次が成り立つ：

    .. math::

       \int_B\!\left(\frac{\partial \xi_1}{\partial x_1} + \frac{\partial \xi_2}{\partial x_2} + \frac{\partial \xi_3}{\partial x_3}\right)\,\dd x_1\dd x_2\dd x_3
       = \int_{\partial B}\!n \cdot \xi\,\dd S.

    ただし :math:`\dd S` は領域の境界 :math:`\partial B` の「面積要素」である。

..

* 一般の k 形式に対しても :math:`\displaystyle \sum_{i_1 < \dotsb < i_k} f_{i_1 \dots i_k} \alpha^{(i_1)} \wedge \dotsb \wedge \alpha^{(i_k)}`
  と書いたときの :math:`\displaystyle \sum_{i_1 < \dotsb < i_k} f_{i_1 \dots i_k}^2`
  の値は正規直交基底のとり方に依存しないで定まる。

  * したがって「長さ」も定まると言いたい？

.. _tsuboi08.4.4.4:

* 問題 4.4.4: 行列式の計算

  * 行列 :math:`A` を :math:`m \times n` サイズ、
  * 行列 :math:`B` を :math:`n \times m` サイズで

  あるとする。このとき :math:`\det(AB)` はどう書けるかという問題。

  * :math:`A = (a_{ij}),`
  * :math:`B = (b_{jk}),`
  * :math:`i, k = 1, \dotsc, m,`
  * :math:`j = 1, \dotsc, n`

  とおく。

  * \(1) :math:`m \ge n` ならば :math:`\det(AB) = 0.`

    :math:`AB` のランクのことを考えれば明らか。

  * \(2) :math:`m \le n` ならば：

    .. math::

       \det(AB) = \sum_{j_1 < \dotsb < j_m}
           \det((a_{ik})_{\substack{i = 1, \dots, m\\k = j_1, \dotsc, j_m}})
           \det((b_{ki})_{\substack{i = 1, \dots, m\\k = j_1, \dotsc, j_m}})

    1. 行列の積を考える：

       .. math::

          AB = \left(\sum_{j = 1} a_{ij}b_{jk}\right)_{i, k = 1, \dotsc, m}.

    2. 行列式をひたすら考える：

       .. math::

          \begin{align*}
          \det(AB)
          &= \sum_\sigma \sgn(\sigma)
              \left(\sum_{j_1 = 1} a_{1 j_1} b_{j_1 \sigma(1)}\right)
              \dotsm
              \left(\sum_{j_m = 1} a_{m j_m} b_{j_m \sigma(m)}\right)\\
          &= \sum_\sigma
             \sum_{J \subset \set{1, \dotsc, n}}
             \sum_{\set{j_1, \dotsc, j_m} = J}
              \sgn(\sigma) a_{1 j_1} b_{j_1 \sigma(1)}
              \dotsm a_{m j_m} b_{j_m \sigma(m)}\\
          &= \sum_\sigma \sum_{j_1 < \dotsb < j_m} \sum_\tau
              \sgn(\sigma) a_{1 j_{\tau(1)}} b_{j_{\tau(1)} \sigma(1)}
              \dotsm a_{m j_{\tau(m)}} b_{j_{\tau(m)} \sigma(m)}.
          \end{align*}

    3. シグマを一個取った部分を計算すると：

       .. math::

          \begin{align*}
          \sum_\sigma \sum_\tau
              \sgn(\sigma) a_{1 j_{\tau(1)}} b_{j_{\tau(1)} \sigma(1)}
              \dotsm a_{m j_{\tau(m)}} b_{j_{\tau(m)} \sigma(m)}
          &= \sum_\tau \sgn(\tau)
              a_{1 j_{\tau(1)}} \dotsm a_{m j_{\tau(m)}}
              \sum_\sigma \sgn(\sigma)\sgn(\tau)
              b_{j_{\tau(1)} \sigma(1)}
              \dotsm b_{j_{\tau(m)} \sigma(m)}\\
          &= \sum_\tau \sgn(\tau)
              a_{1 j_{\tau(1)}} \dotsm a_{m j_{\tau(m)}}
              \sum_\sigma \sgn(\sigma\tau\inv)
              b_{j_1 \sigma(\tau\inv(1))}
              \dotsm b_{j_m \sigma(\tau\inv(m))}.
          \end{align*}

    4. 再び :math:`\displaystyle \sum_{j_1 < \dotsb < j_m}` を適用すると
       所望の結論を得る。

..

* 正規直交基底 :math:`\set{\alpha^{(1)}, \dotsc, \alpha^{(n)}}` に対して、
  :math:`\alpha^{(i_1)} \wedge \dotsb \wedge \alpha^{(i_k)}` が k 次外積の
  空間における自然な内積についての正規直交基底になっていることが今のでわかる。
  自然な内積とは次のものだ：

  .. math::

     \sum_{i_1 < \dotsb < i_k} f_{i_1 \dots i_k} \alpha^{(i_1)} \wedge \dotsb \wedge \alpha^{(i_k)},
     \sum_{i_1 < \dotsb < i_k} g_{i_1 \dots i_k} \alpha^{(i_1)} \wedge \dotsb \wedge \alpha^{(i_k)}
     \longmapsto
     \sum_{i_1 < \dotsb < i_k} f_{i_1 \dots i_k} g_{i_1 \dots i_k}.

* 微分形式同士の内積を定義する。

  * 多様体 :math:`M` は向き付けられたコンパクト閉多様体であり、
  * :math:`\alpha, \beta \in \Omega^k(M)` であり、
  * :math:`(\alpha, \beta)_x` を :math:`\extp^k T_x^*M` の内積である

  とすると、次で定義される：

  .. math::

     (\alpha, \beta) = \int_M\!(\alpha, \beta)_x\Omega_{(M, g)}.

..

* `ホッジのスター作用素 <http://mathworld.wolfram.com/HodgeStar.html>`__

  :math:`\fn{*}{\extp^k T^*M}\extp^{n - k}T^*M` を次のように定義する：

  .. math::

     *(\alpha^{(i_1)} \wedge \dotsb \wedge \alpha^{(i_k)})
     = \sgn
     \begin{pmatrix}
     1   & \cdots & \cdots & \cdots & \cdots & n\\
     i_1 & \cdots & i_k & j_1 & \cdots & j_{n - k}
     \end{pmatrix}
     \alpha^{(j_1)} \wedge \dotsb \wedge \alpha^{(j_{n - k})}

  * ここで各 :math:`\alpha^{(\cdot)}` は正の向きの正規直交基底であり、
  * :math:`i_1 < \dotsb < i_k,\ j_1 < \dotsb < j_{n - k}` であり、
  * :math:`\sgn` ホニャララは n 個の添字の置換の符号を意味するものとする。

.. _tsuboi08.4.4.5:

* 問題 4.4.5: スター作用素の定義は正規直交基底のとり方に依存しない

  1. 正の向きの正規直交基底 :math:`\set{\alpha^{(\cdot)}}, \set{\beta^{(\cdot)}}` に対して
     次の等式を満たす行列 :math:`A = (a_{ij}) \in SO(n)` が存在する：

     .. math::

        \beta^{(i)} = \sum_{j = 1}^n a_{ij}\alpha^{(j)}.

  2. :math:`*(\beta^{(i_1)} \wedge \dotsb \wedge \beta^{(i_k)}) = P \alpha^{(l_1)} \wedge \dotsb \wedge \alpha^{(l_{n - k})}`
     の形に書き表す。:math:`P` の部分は本書にあるようにゴチャゴチャしている。

  3. :math:`\displaystyle \alpha^{(l)} = \sum_{m = 1}^n a_{ml}\beta^{(m)}` を用いて
     2. の :math:`\alpha^{(l_1)} \wedge \dotsb \wedge \alpha^{(l_{n - k})}` を
     :math:`Q \beta^{(m_1)} \wedge \dotsb \wedge \beta^{(m_{n - k})}` の形に書き表す。
     :math:`Q` の部分はやはりゴチャゴチャしている。

  4. \3. を 2. に代入して次のように変形したい：

     .. math::

        \sgn\begin{pmatrix}
        1   & \cdots & \cdots & \cdots & \cdots & n\\
        i_1 & \cdots & i_k & m_1 & \cdots & m_{n - k}
        \end{pmatrix}
        \beta^{(m_1)} \wedge \dotsb \wedge \beta^{(m_{n - k})}

     それには :math:`P` と :math:`Q` が上記の置換の符号と一致することを、
     大量のシグマ記号と置換をうまく捌いて示せば十分。

..

* ホッジのスター作用素の性質いろいろ

  * :math:`*1 = \Omega_{(M, g)}.`
  * :math:`*` は内積を保つ線形同型写像である。
  * :math:`* \circ * = (-1)^{k(n - k)}.`
  * :math:`*` は写像 :math:`\fn{*}{\Omega^k(M)}\Omega^{n - k}(M)` を引き起こす。
    :math:`\Omega^k(M)` の内積を次のように書ける：

    .. math::

       \begin{align*}
       (\alpha, \beta)
       &= \int_M\!(\alpha, \beta)_x \Omega_{(M, g)}\\
       &= \int_M\!\alpha \wedge *\beta\\
       &= \int_M\!*\alpha \wedge \beta.
       \end{align*}

    * :math:`\alpha \in \Omega^{k - 1}(M),\ \beta \in \Omega^k(M)` とする。

      * 写像 :math:`\fn{\delta}{\Omega^k(M)}\Omega^{k - 1}(M)` を次のように定義する：

        .. math::

           \delta = (-1)^{n(k + 1) + 1}(* \circ \dd{} \circ *).

      このとき :math:`(\dd\alpha, \beta) = (\alpha, \delta\beta)` が成り立つ：

      .. math::

         \begin{align*}
         (\dd\alpha, \beta)
         &= \int_M\!(\dd\alpha) \wedge *\beta\\
         &= \int_M\!\dd(\alpha \wedge *\beta) - (-1)^{k - 1}\alpha \wedge \dd(*\beta)\\
         &= -\int_M\!(-1)^{k - 1}\alpha \wedge (-1)^{(n - k + 1)(k - 1)}(* \circ *)\dd(*\beta)\\
         &= -(-1)^{(n - k)(k - 1)}(-1)^{n(k + 1) + 1} \int_M\!\alpha \wedge *\delta\beta\\
         &= \int_M\!\alpha \wedge *\delta\beta\\
         &= (\alpha, \delta\beta).
         \end{align*}

      * 式変形の途中でムリヤリ :math:`\delta` を出現させるところが急所。

..

* :math:`\delta` の性質いろいろ

  * :math:`\delta \circ \delta = 0` であることから :math:`(\Omega^*(M), \delta)` は複体である。
  * :math:`(\dd\alpha, \beta) = (\alpha, \delta\beta)` などが成り立つことから、
    部分空間の直交性 :math:`\ker\dd \perp \im\delta,\ \im\delta \perp \ker\delta` がある。

    * 直交するとは、内積がゼロとなることである。

  * :math:`\Omega^k(M)` には互いに直交する部分空間 :math:`\ker\dd \cap \ker\delta,\ \im\dd,\ \im\delta`
    が存在する。
  * :math:`\boldsymbol{H}^k = \set{\alpha \in \Omega^k(M) \sth (\dd\delta + \delta\dd)\alpha = 0}` とおくと、
    :math:`\boldsymbol{H}^k = \ker\dd{} \cap \ker\delta` が成り立つ。

    * :math:`\alpha \in \boldsymbol{H}^k` ならば :math:`0 = (\dd\delta + \delta\dd)\alpha, \alpha) = (\delta\alpha, \delta\alpha) + (\dd\alpha, \dd\alpha)`
      であるので :math:`\alpha \in \ker\dd{} \cap \ker\delta` と言える。
    * :math:`\alpha \in \ker\dd{} \cap \ker\delta` ならば当然 :math:`\alpha \in \boldsymbol{H}^k` である。

  * :math:`\Laplace = \dd\delta + \delta\dd` と書き、
    `ラプラシアン <http://mathworld.wolfram.com/Laplace-BeltramiOperator.html>`__ と呼ぶ。

    * :math:`\Laplace\alpha = 0` を満たす :math:`\alpha` を
      調和形式という。

      * :math:`\Laplace\alpha = 0 \iff (\dd\alpha = 0) \land (\delta\alpha = 0) \iff \alpha \in \ker\dd \cap \ker\delta.`
      * :math:`\boldsymbol{H}^k = \ker\Delta.`

.. _tsuboi08.4.4.6:

* 定理 4.4.6: ホッジ・ドラーム・小平の定理

  :math:`\Omega^k(M) = \boldsymbol{H}^k \oplus \im\dd{} \oplus \im\delta` は
  直交する部分空間への直和分解である。

  * 証明は参考文献にあるようだ。

4.5 第 4 章の問題
======================================================================
吟味中。
