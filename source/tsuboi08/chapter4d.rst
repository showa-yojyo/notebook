======================================================================
第 4 章 微分形式とベクトル場 4/4
======================================================================

.. contents:: ノート目次

4.4 TBW
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

  を見ると、リーマン計量 :math:`g` は
  射影 :math:`\fn{p}{T^*M \times T^*M}M` に対し :math:`p \circ g` になるような
  対称なテンソル積のなす :math:`\dfrac{n(n + 1)}{2}` 次元ベクトル空間をファイバーとする
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

  をとる。これに対応する余接空間の基底

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
     \xi^{(k + 1)} &= \frac{v_{k + 1}}{\sqrt{g(v_{k + 1}, g(v_{k + 1})}}
     \end{align*}

  と正規化する。

..

* `リーマン多様体の体積形式 <https://en.wikipedia.org/wiki/Volume_form#Riemannian_volume_form>`__ 

  * 余接空間 :math:`T_x^*M` の正規直交基底 :math:`\set{\alpha^{(k)}}` に対して、
    n 形式 :math:`\alpha^{(1)} \wedge \dotsb \wedge ^{(n)}` は（符号を除いて）リーマン計量で定まる。

  * 多様体が向き付け可能であれば、各座標近傍上で正の正規直交基底がとれる。
    そのとき、上述の n 形式の外微分をとると、二つの座標近傍の共通部では
    座標変換のよる引き戻しとなる。このような非ゼロ微分形式をリーマン多様体の
    体積形式という。

.. _tsuboi08.4.4.1:

* 問題 4.4.1: 向き付けられたリーマン多様体の向き付けられた座標近傍における体積形式

.. _tsuboi08.4.4.2:

* 定理 4.4.2: ガウス・グリーンの公式

.. _tsuboi08.4.4.3:

* 例 4.4.3: ガウス・グリーンの公式の特殊化

.. _tsuboi08.4.4.4:

* 問題 4.4.4: 行列式の計算

.. _tsuboi08.4.4.5:

* 問題 4.4.5: ホッジスターの定義は正規直交基底のとり方に依存しない

.. _tsuboi08.4.4.6:

* 定理 4.4.6: ホッジ・ドラーム・小平の定理
