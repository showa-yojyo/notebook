======================================================================
幾何学 I 多様体入門 読書ノート 6/8
======================================================================

:doc:`note5` からの続き。

.. contents:: ノート目次

第 6 章 多様体上のフロー
======================================================================
値が十分近い二つの正則値同士の逆像もまた十分近い形をしているだろうか。

6.1 多様体の部分集合の比較、アイソトピー
----------------------------------------------------------------------
* 微分同相写像で互いに写り合う多様体同士を同じものと考える (p. 123)。

アイソトピー
  :math:`t \in [0, 1]` に対して連続的に変化する微分同相写像 :math:`F_t: M \to M` で、
  :math:`F_0 = \operatorname{id}_M` を満たすものを `アイソトピー <http://mathworld.wolfram.com/Isotopy.html>`__ という。

  * :math:`\mathbb R \times M` の :math:`[0, 1] \times M` への制限。
  * :math:`A_0, A_1 \subset M` は多様体の部分集合であるとすると、
    :math:`F_0(A_0) = A_0,\ F_1(A_0) = A_1.`

  * 制限なしの :math:`F` について

    #. :math:`(t_0, x_0)` を固定すると :math:`T_{F_{t_0}(x_0)}M` の接ベクトルが定まる。
       なぜなら :math:`F_t(x_0)` が :math:`F_{t_0}(x_0)` を通過するから。

    #. :math:`\forall y_0 \in M, x_0 = F_{t_0}^{-1}(y_0)` とすると :math:`T_{y_0}M` の接ベクトルが定まる。
       なぜなら  :math:`F_{t_0}` が微分同相だから。

  * :math:`\displaystyle X_t := \frac{\partial F_t}{\partial t} \circ F_t^{-1}: M \longrightarrow T_{y_0}M` なる量を考える。

    * :math:`y_0 \in M` 周りの座標近傍を :math:`(U, \varphi)` とし、
    * :math:`(\varphi \circ (F_t \circ F_{t_0}^{-1})\circ\varphi^{-1}(x_1, \dotsc, x_n)` を
      :math:`(f_1(t, t_0, x_1, \dotsc, x_n), \dotsc, f_n(t, t_0, x_1, \dotsc, x_n),)` と書く。

    * :math:`\displaystyle X_i = \sum_{i = 1}^n \frac{df_i}{dt}(t, t_0, x_1, \dotsc, x_n) \frac{\partial}{\partial x_i}.`

    * :math:`(t_0, \varphi(y_0))` の近傍で定義されている :math:`\mathbb R^n` に値を持つ :math:`C^\infty` 級写像である。
    * :math:`(t_0, \varphi(y_0))` の近傍において :math:`X(t, y) = X_t(y)` による写像
      :math:`X: \mathbb R \times R \longrightarrow TM` は :math:`C^\infty` 級写像である。

ベクトル場
  各 :math:`t` について :math:`X_t: M \longrightarrow TM` は
  :math:`p \circ X_t = \operatorname{id}_M` となる :math:`C^\infty` 級写像である。

  そこで、こういう性質を持つ :math:`C^\infty` 級写像 :math:`X: M \longrightarrow TM` を
  :math:`M` 上の :math:`C^\infty` 級ベクトル場と言う。

  * :math:`\displaystyle \frac{dF_t}{dt} = X_t \circ F_t,\ F_{t_0} = \operatorname{id}_M`
  * :math:`F_{t_0} = \operatorname{id}_M` となる :math:`F_t` により :math:`F_{t_1}(A_0) = A_1` となることは、
    ベクトル場の定める常微分方程式の解により :math:`A_0` を :math:`A_1` に写すことと同じである。

  * :math:`t \sim t_0` のとき :math:`F_t \circ F_{t_0}^{-1}` を局所座標表示するとわかる。

* 例 6.1.1: 線形常微分方程式を :math:`\mathbb R^n` 上の接ベクトルとして書く。

  * 以下 :math:`A(t) \in M_n(\mathbb R)` を :math:`t` について連続な行列、
    成分を :math:`A(t) = (a_{ij}(t))` と表し、ベクトル :math:`\boldsymbol{x} = (x_j)` と表す。

  * :math:`\displaystyle \frac{d}{dt}\boldsymbol{x} = A(t)\boldsymbol{x}` について、
    これは接ベクトル場 :math:`\displaystyle \sum_{i = 1}^n\left(\sum_{j = 1}^n a_{ij}(t)x_j\right)\frac{\partial}{\partial x_i}` である。

  * :math:`A(t)` が :math:`t` に非依存ならば
    :math:`F_t \circ F_{t_0}^{-1}(\boldsymbol{x}) = e^{(t - t_0)A}\boldsymbol{x}` である。

* 例題 6.1.2: 微分同相からアイソトピーを構成する？

  * 仮定

    * :math:`F: \mathbb R^n \longrightarrow \mathbb R^n` は微分同相であり、
    * :math:`DF_{(\boldsymbol{x})} - E` の成分の絶対値が :math:`\displaystyle \varepsilon\quad (< \frac{1}{2n})` より小さいとする。

  * 結論

    * :math:`F_t(\boldsymbol{x}) = (1 - t) \boldsymbol{x} + F(\boldsymbol{x})` は微分同相であり、
    * :math:`F_0 = \operatorname{id}_{\mathbb R^n},\ F_1 = F` である。

  * 証明

    #. :math:`DF_{(\boldsymbol{x})}` は正則である。

       これがよくわからない。仮定の評価式から次の式の級数が絶対収束することからすぐにわかるようだ。
       :math:`\displaystyle (E + t(DF_{(\boldsymbol{x})} - E))\sum_{k = 0}^\infty (-t)^k (DF_{(\boldsymbol{x})} - E)^k = E` 

    #. :math:`F_t` は単射である。

       :math:`H_t(\boldsymbol{x}) = \boldsymbol{x} - F_t(\boldsymbol{x})`, :math:`\boldsymbol{y} \in \mathbb R^b` とおくと
       次のように評価できる：

       .. math::
          :nowrap:

          \begin{gather*}
          \lVert H_t(\boldsymbol{x}) - H_t(\boldsymbol{y}) \rVert & \le nt\varepsilon \lVert \boldsymbol{x} - \boldsymbol{y} \rVert\\
          & \le \frac{1}{2}\lVert \boldsymbol{x} - \boldsymbol{y} \rVert\\
          \therefore \lVert F_t(\boldsymbol{x}) - F_t(\boldsymbol{y}) \rVert & \ge \frac{1}{2}\lVert \boldsymbol{x} - \boldsymbol{y} \rVert
          \end{gather*}

    #. :math:`F_t` は全射である。

       :math:`\boldsymbol{x_1} = \boldsymbol{y},\ \boldsymbol{x}_{k + 1} = \boldsymbol{x}_k - (F_t(\boldsymbol{x}_k) - \boldsymbol{y}) = \boldsymbol{y} + H_t(\boldsymbol{x}_k)` とおく。
       次のように評価できる：

       .. math::
          :nowrap:

          \begin{gather*}
          \lVert \boldsymbol{x}_{k+1} - \boldsymbol{x}\rVert & \le \frac{1}{2^{k-1}}\lVert \boldsymbol{x}_2 - \boldsymbol{x}_1 \rVert\\
          & = \frac{1}{2^{k-1}}\lVert \boldsymbol{y} - F_t(\boldsymbol{y}) \rVert\\
          &\therefore \boldsymbol{x}_k \to \boldsymbol{y}\ s.t.\ \boldsymbol{y} = F_t(\boldsymbol{y}). 
          \end{gather*}

----

:doc:`note7` へ。
