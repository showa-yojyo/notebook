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
  :math:`t \in [0, 1]` に対して連続的に変化する微分同相写像 :math:`F_t: M \longto M` で、
  :math:`F_0 = \id_M` を満たすものを `アイソトピー <http://mathworld.wolfram.com/Isotopy.html>`__ という。

  * :math:`\RR \times M` の :math:`[0, 1] \times M` への制限。
  * :math:`A_0, A_1 \subset M` は多様体の部分集合であるとすると、
    :math:`F_0(A_0) = A_0,\ F_1(A_0) = A_1.`

  * 制限なしの :math:`F` について

    #. :math:`(t_0, x_0)` を固定すると :math:`T_{F_{t_0}(x_0)}M` の接ベクトルが定まる。
       なぜなら :math:`F_t(x_0)` が :math:`F_{t_0}(x_0)` を通過するから。

    #. :math:`\forall y_0 \in M, x_0 = F_{t_0}^{-1}(y_0)` とすると :math:`T_{y_0}M` の接ベクトルが定まる。
       なぜなら  :math:`F_{t_0}` が微分同相だから。

  * :math:`\displaystyle X_t := \frac{\partial F_t}{\partial t} \circ F_t^{-1}: M \longto T_{y_0}M` なる量を考える。

    * :math:`y_0 \in M` 周りの座標近傍を :math:`(U, \varphi)` とし、
    * :math:`(\varphi \circ (F_t \circ F_{t_0}^{-1})\circ\varphi^{-1}(x_1, \dotsc, x_n)` を
      :math:`(f_1(t, t_0, x_1, \dotsc, x_n), \dotsc, f_n(t, t_0, x_1, \dotsc, x_n),)` と書く。

    * :math:`\displaystyle X_i = \sum_{i = 1}^n \frac{df_i}{dt}(t, t_0, x_1, \dotsc, x_n) \frac{\partial}{\partial x_i}.`

    * :math:`(t_0, \varphi(y_0))` の近傍で定義されている :math:`\RR^n` に値を持つ :math:`C^\infty` 級写像である。
    * :math:`(t_0, \varphi(y_0))` の近傍において :math:`X(t, y) = X_t(y)` による写像
      :math:`X: \RR \times R \longto TM` は :math:`C^\infty` 級写像である。

ベクトル場
  各 :math:`t` について :math:`X_t: M \longto TM` は
  :math:`p \circ X_t = \id_M` となる :math:`C^\infty` 級写像である。

  そこで、こういう性質を持つ :math:`C^\infty` 級写像 :math:`X: M \longto TM` を
  :math:`M` 上の :math:`C^\infty` 級ベクトル場と言う。

  * :math:`\displaystyle \frac{dF_t}{dt} = X_t \circ F_t,\ F_{t_0} = \id_M`
  * :math:`F_{t_0} = \id_M` となる :math:`F_t` により :math:`F_{t_1}(A_0) = A_1` となることは、
    ベクトル場の定める常微分方程式の解により :math:`A_0` を :math:`A_1` に写すことと同じである。

  * :math:`t \sim t_0` のとき :math:`F_t \circ F_{t_0}^{-1}` を局所座標表示するとわかる。

* 例 6.1.1: 線形常微分方程式を :math:`\RR^n` 上の接ベクトルとして書く。

  * 以下 :math:`A(t) \in M_n(\RR)` を :math:`t` について連続な行列、
    成分を :math:`A(t) = (a_{ij}(t))` と表し、ベクトル :math:`\bm{x} = (x_j)` と表す。

  * :math:`\displaystyle \frac{d}{dt}\bm{x} = A(t)\bm{x}` について、
    これは接ベクトル場 :math:`\displaystyle \sum_{i = 1}^n\left(\sum_{j = 1}^n a_{ij}(t)x_j\right)\frac{\partial}{\partial x_i}` である。

  * :math:`A(t)` が :math:`t` に非依存ならば
    :math:`F_t \circ F_{t_0}^{-1}(\bm{x}) = e^{(t - t_0)A}\bm{x}` である。

* 例題 6.1.2: 微分同相からアイソトピーを構成する？

  * 仮定

    * :math:`F: \RR^n \longto \RR^n` は微分同相であり、
    * :math:`DF_{(\bm{x})} - E` の成分の絶対値が :math:`\displaystyle \eps\quad (< \frac{1}{2n})` より小さいとする。

  * 結論（ただし本書の関数定義には誤植があると思われるので勝手に修正する）

    * :math:`F_t(\bm{x}) = (1 - t) \bm{x} + t F(\bm{x})` は微分同相であり、
    * :math:`F_0 = \id_{\RR^n},\ F_1 = F` である。

  * 証明

    #. :math:`DF_{(\bm{x})}` は正則である。

       * 単純計算により :math:`DF_{(\bm x)} = (E + t(DF_{(\bm{x})} - E)).`
       * 高校数学の :math:`\displaystyle \frac{1}{1 + x}` の級数展開を参考に次の式が浮かぶ：

         .. math::
            :nowrap:

            \begin{gather*}
            (E + t(DF_{(\bm{x})} - E))\sum_{k = 0}^\infty (-t)^k (DF_{(\bm{x})} - E)^k = E
            \end{gather*}

         問題は級数の収束性だが（行列式の評価には注意したい）、
         これは仮定の評価から絶対収束であることがわかる：

         .. math::
            :nowrap:

            \begin{split}
            \lvert (-t)^k (DF_{(\bm{x})} - E)^k \rvert
                &<& \lvert t^k n^{k - 1} \eps^k \rvert\\
                &<& n^{k - 1} \eps^k\\
                &<& \frac{1}{2^{k - 1}}\eps.
            \end{split}

         以上で :math:`DF_{(\bm x)}` の逆行列が存在して、それが上記の級数で与えられることがわかった。

    #. :math:`F_t` は単射である。

       :math:`H_t(\bm{x}) = \bm{x} - F_t(\bm{x})`, :math:`\bm{y} \in \RR^n` とおくと
       次のように評価できる：

       .. math::
          :nowrap:

          \begin{split}
          \lVert H_t(\bm{x}) - H_t(\bm{y}) \rVert & \le nt\eps \lVert \bm{x} - \bm{y} \rVert\\
          & \le \frac{1}{2}\lVert \bm{x} - \bm{y} \rVert\\
          \therefore \lVert F_t(\bm{x}) - F_t(\bm{y}) \rVert & \ge \frac{1}{2}\lVert \bm{x} - \bm{y} \rVert
          \end{split}

    #. :math:`F_t` は全射である。

       :math:`\bm{x_1} = \bm{y},\ \bm{x}_{k + 1} = \bm{x}_k - (F_t(\bm{x}_k) - \bm{y}) = \bm{y} + H_t(\bm{x}_k)` とおく。
       次のように評価できる：

       .. math::
          :nowrap:

          \begin{split}
          \lVert \bm{x}_{k+1} - \bm{x}\rVert & \le& \frac{1}{2^{k-1}}\lVert \bm{x}_2 - \bm{x}_1 \rVert\\
          & =& \frac{1}{2^{k-1}}\lVert \bm{y} - F_t(\bm{y}) \rVert\\
          &\therefore& \bm{x}_k \to \bm{y}\ s.t.\ \bm{y} = F_t(\bm{y}). 
          \end{split}

6.2 フロー
----------------------------------------------------------------------
`フロー <http://mathworld.wolfram.com/Flow.html>`__
  フローとは次の性質を満たすアイソトピーである：
  :math:`F_s \circ F_t = F_{s + t}.`

  * フローは加法群 :math:`\RR` の多様体への群作用である。
  * ベクトル場 :math:`X_t` は、あるいは局所座標系で書かれた常微分方程式は :math:`t` に依存しない。
  * ベクトル場 :math:`X = X_t` はフローを :math:`F_t` を生成するベクトル場であるという。
    生成の主従を逆に見ることもある。

* 例 6.2.1: 軌道

  :math:`\RR^n` のベクトル :math:`\bm x = (x_i)` と行列 :math:`A = (a_{ij})` を考える。

  * :math:`F_t(\bm x) = \mathrm{e}^{tA} \bm x` は :math:`\RR^n` 上のベクトル場
    :math:`\displaystyle \sum_{i = 1}^n \left( \sum_{j = 1}^n a_{ij} x_j \right)\frac{\partial}{\partial x_j}` が生成するフローである。

  * フロー :math:`\{ F_t(\bm x) \mid t \in \RR\}` を :math:`\bm x` を通る軌道という。
    この軌道は :math:`M` 上の同値関係を定義する。

  * 軌道は一点、円周、実数全体のいずれかでパラメーター付けられる。

    * 円周ならば一次元部分多様体である。

* 例 6.2.2: 平面上の線形ベクトル場の生成するフローの軌道カタログ

  * 式にすれば :math:`\displaystyle \sum_{i, j = 1}^2 a_{ij} x_j \frac{\partial}{\partial x_j}` だが、
    本書の図によると三種類に分類できるようだ。

* 問題 6.2.3: コンパクト多様体上のフローについて（後回し）

  * TBW

----

:doc:`note7` へ。
