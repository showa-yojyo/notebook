======================================================================
第 6 章 多様体上のフロー（前編）
======================================================================

値が十分近い二つの正則値同士の逆像もまた十分近い形をしているだろうか。

.. contents:: ノート目次

6.1 多様体の部分集合の比較、アイソトピー
======================================================================
* 微分同相写像で互いに写り合う多様体同士を同じものと考える (p. 123)。

`アイソトピー <http://mathworld.wolfram.com/Isotopy.html>`__
  :math:`t \in [0, 1]` に対して連続的に変化する微分同相写像 :math:`\fn{F_t}{M}M` で、
  :math:`F_0 = \id_M` を満たすものをアイソトピーという。

  * :math:`\RR \times M` の :math:`[0, 1] \times M` への制限。
  * :math:`A_0, A_1 \subset M` は多様体の部分集合であるとすると、
    :math:`F_0(A_0) = A_0,\ F_1(A_0) = A_1.`

  * 制限なしの :math:`F` について

    #. :math:`(t_0, x_0)` を固定すると :math:`T_{F_{t_0}(x_0)}M` の接ベクトルが定まる。
       なぜなら :math:`F_t(x_0)` が :math:`F_{t_0}(x_0)` を通過するから。

    #. :math:`\forall y_0 \in M, x_0 = F_{t_0}\inv(y_0)` とすると :math:`T_{y_0}M` の接ベクトルが定まる。
       なぜなら  :math:`F_{t_0}` が微分同相だから。

  * :math:`X_t := \fn{\dfrac{\partial F_t}{\partial t} \circ F_t\inv}{M}T_{y_0}M` なる量を考える。

    * :math:`y_0 \in M` 周りの座標近傍を :math:`(U, \varphi)` とし、
    * :math:`\varphi \circ (F_t \circ F_{t_0}\inv)\circ\varphi\inv(x_1, \dotsc, x_n)` を
      :math:`(f_1(t, t_0, x_1, \dotsc, x_n), \dotsc, f_n(t, t_0, x_1, \dotsc, x_n))` と書く。

    * :math:`\displaystyle X_i = \sum_{i = 1}^n \diff{f_i}{t}(t, t_0, x_1, \dotsc, x_n) \frac{\partial}{\partial x_i}.`

    * :math:`(t_0, \varphi(y_0))` の近傍で定義されている :math:`\RR^n` に値を持つ :math:`C^\infty` 級写像である。
    * :math:`(t_0, \varphi(y_0))` の近傍において :math:`X(t, y) = X_t(y)` による写像
      :math:`\fn{X}{\RR \times M}TM` は :math:`C^\infty` 級写像である。

`ベクトル場 <http://mathworld.wolfram.com/VectorField.html>`__
  各 :math:`t` について :math:`\fn{X_t}{M}TM` は
  :math:`p \circ X_t = \id_M` となる :math:`C^\infty` 級写像である。

  そこで、こういう性質を持つ :math:`C^\infty` 級写像 :math:`\fn{X}{M}TM` を
  :math:`M` 上の :math:`C^\infty` 級ベクトル場と言う。

  * :math:`\displaystyle \diff{F_t}{t} = X_t \circ F_t,\ F_{t_0} = \id_M`
  * :math:`F_{t_0} = \id_M` となる :math:`F_t` により :math:`F_{t_1}(A_0) = A_1` となることは、
    ベクトル場の定める常微分方程式の解により :math:`A_0` を :math:`A_1` に写すことと同じである。

  * :math:`t = t_0` のとき :math:`F_t \circ F_{t_0}\inv` を局所座標表示するとわかる。

* 例 6.1.1: 線形常微分方程式を :math:`\RR^n` 上の接ベクトルとして書く。

  * 以下 :math:`A(t) \in M_n(\RR)` を :math:`t` について連続な行列、
    成分を :math:`A(t) = (a_{ij}(t))` と表し、ベクトル :math:`\bm{x} = (x_j)` と表す。

  * :math:`\displaystyle \diff{}{t}\bm{x} = A(t)\bm{x}` について、
    これは接ベクトル場 :math:`\displaystyle \sum_{i = 1}^n\left(\sum_{j = 1}^n a_{ij}(t)x_j\right)\frac{\partial}{\partial x_i}` である。

  * :math:`A(t)` が :math:`t` に非依存ならば
    :math:`F_t \circ F_{t_0}\inv(\bm{x}) = e^{(t - t_0)A}\bm{x}` である。

* 例題 6.1.2: 微分同相からアイソトピーを構成する？

  * 仮定

    * :math:`\fn{F}{\RR^n}\RR^n` は微分同相であり、
    * :math:`DF_{(\bm{x})} - I_n` の成分の絶対値が :math:`\displaystyle \eps\quad (< \frac{1}{2n})` より小さいとする。

  * 結論（ただし本書の関数定義には誤植があると思われるので勝手に修正する）

    * :math:`F_t(\bm{x}) = (1 - t) \bm{x} + t F(\bm{x})` は微分同相であり、
    * :math:`F_0 = \id_{\RR^n},\ F_1 = F` である。

  * 証明

    #. :math:`DF_{(\bm{x})}` は正則である。

       * 単純計算により :math:`DF_{(\bm x)} = (I_n + t(DF_{(\bm{x})} - I_n)).`
       * 高校数学の :math:`\displaystyle \frac{1}{1 + x}` の級数展開を参考に次の式が浮かぶ：

         .. math::
            :nowrap:

            \begin{gather*}
            (I_n + t(DF_{(\bm{x})} - I_n))\sum_{k = 0}^\infty (-t)^k (DF_{(\bm{x})} - I_n)^k = I_n
            \end{gather*}

         問題は級数の収束性だが（行列式の評価には注意したい）、
         これは仮定の評価から絶対収束であることがわかる：

         .. math::
            :nowrap:

            \begin{split}
            \abs{(-t)^k (DF_{(\bm{x})} - I_n)^k}
                &<& \abs{t^k n^{k - 1} \eps^k}\\
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
          \norm{H_t(\bm{x}) - H_t(\bm{y})} & \le nt\eps \norm{\bm{x} - \bm{y}}\\
          & \le \frac{1}{2}\norm{\bm{x} - \bm{y}}\\
          \therefore \norm{F_t(\bm{x}) - F_t(\bm{y})} & \ge \frac{1}{2}\norm{\bm{x} - \bm{y}}
          \end{split}

    #. :math:`F_t` は全射である。

       :math:`\bm{x_1} = \bm{y},\ \bm{x}_{k + 1} = \bm{x}_k - (F_t(\bm{x}_k) - \bm{y}) = \bm{y} + H_t(\bm{x}_k)` とおく。
       次のように評価できる：

       .. math::
          :nowrap:

          \begin{split}
          \norm{\bm{x}_{k+1} - \bm{x}} & \le& \frac{1}{2^{k-1}}\norm{\bm{x}_2 - \bm{x}_1}\\
          & =& \frac{1}{2^{k-1}}\norm{\bm{y} - F_t(\bm{y})}\\
          &\therefore& \bm{x}_k \to \bm{y}\ \text{s.t. } \bm{y} = F_t(\bm{y}). 
          \end{split}

6.2 フロー
======================================================================
序盤から難しい。

`フロー <http://mathworld.wolfram.com/Flow.html>`__
  フローとは次の性質を満たすアイソトピーである：
  :math:`F_s \circ F_t = F_{s + t}.`

  * フローは加法群 :math:`\RR` の多様体への群作用である。
  * ベクトル場 :math:`X_t` は、あるいは局所座標系で書かれた常微分方程式は :math:`t` に依存しない。

    * :math:`F_t` がフローの場合は :math:`\displaystyle X_{t_0}(y_0) = \frac{\partial F}{\partial t}(t_0, F_{t_0}\inv(y_0)) = \frac{\partial F}{\partial t}(0, y_0) = X_0(y_0)` とあるが、
      二番目の等号が成立する根拠がわからない。
      :math:`F_t = F_{t - t_0} \circ F_{t_0}` であることがどう関わっているのか。

  * ベクトル場 :math:`X = X_t` はフローを :math:`F_t` を生成するベクトル場であるという。
    生成の主従を逆に見ることもある。

* 例 6.2.1: 軌道

  :math:`\RR^n` のベクトル :math:`\bm x = (x_i)` と行列 :math:`A = (a_{ij})` を考える。

  * :math:`F_t(\bm x) = \mathrm{e}^{tA} \bm x` は :math:`\RR^n` 上のベクトル場
    :math:`\displaystyle \sum_{i = 1}^n \left( \sum_{j = 1}^n a_{ij} x_j \right)\frac{\partial}{\partial x_j}` が生成するフローである。

    * :math:`\displaystyle \diff{F_t}{t}\circ F_{-t} = A \mathrm e^{At\bm x} \mathrm e^{-At\bm x} = A\bm x = \sum\sum a_{ij}x_j.`

  * フロー :math:`\set{ F_t(\bm x) \sth t \in \RR}` を :math:`\bm x` を通る軌道という。
    この軌道は :math:`M` 上の同値関係を定義する。

  * 軌道は一点、円周、実数全体のいずれかでパラメーター付けられる。

    * 円周ならば一次元部分多様体である。

* 例 6.2.2: 平面上の線形ベクトル場の生成するフローの軌道カタログ

  * 式にすれば :math:`\displaystyle \sum_{i, j = 1}^2 a_{ij} x_j \frac{\partial}{\partial x_j}` だが、
    本書の図によると三種類に分類できるようだ。

* 問題 6.2.3: コンパクト多様体上のフローについて

  #. :math:`\varphi_{t_1}(x_0) = \varphi_{t_2}(x_0)` ならば
     :math:`\exists T \le 0,\ \exists n \in \ZZ \ \text{s.t. } t_2 - t_1 = nT.`

     * まとめて考えるために :math:`A = \set{t \in \RR \sth \varphi_t(x_0) (= \varphi_0(x_0)) = x_0} \subset \RR` とおく。
       :math:`A` が群であることと、閉集合であることを示す：

       * :math:`0 \in A`
       * :math:`a_1, a_2 \in A` について
         :math:`\varphi_{a_1 + a_2}(x_0) = \varphi_{a_1} \circ \varphi_{a_2}(x_0) = \varphi_{a_1}(x_0) = x_0` だから
         :math:`a_1 + a_2 \in A.`

       よって :math:`A` は :math:`\RR` の部分群となっている。

     * 閉集合であることを示すために :math:`A` の収束点列の極限が :math:`A` にあることを示す。

       * :math:`\varphi_t(x_0)` は :math:`t` について連続であるので、
         点列 :math:`\set{a_i}` が :math:`\displaystyle \lim_{i \to \infty} a_i = a` とおくと、
         次のようになる：

         .. math::

            \varphi_a(x_0) = \lim_{i \to \infty}\varphi_{a_i}(x_0)
              = \lim_{i \to \infty}x_0 = x_0.

       したがって :math:`A` は :math:`\RR` の閉集合となっている。

     * :math:`A = \zeroset` と仮定すると :math:`T = 0` が求める値となる。
     * :math:`A \ne \zeroset` と仮定すると :math:`T = \inf\set{a \in A \sth a > 0}` が求める値である。
       要するに :math:`A` の中でゼロの次に小さい値である。

       * :math:`T > 0` のときは :math:`A = \ZZ T`

         * :math:`A \in \ZZ T, \exists n\ \text{s.t. } \abs{a - nT} < T`
           しかし :math:`a - nT \in A \implies a = nT.`

       * :math:`T = 0` のときは :math:`A = \RR`

         * さっきと同じように :math:`\set{a_i} \in A, a_i > 0, \lim a_i = 0 \implies \bigcup\set{n a_i \sth n \in \ZZ} \subset \RR` は
           稠密であるが、:math:`A` が閉集合であるために :math:`A = \RR.`
           :math:`\therefore t \in \RR,\ \varphi_t(x_0) = x_0.`
           これは仮定の「定数関数ではない」に反する。

     となる。

  #. :math:`\exists y \in M,\ \text{s.t. } \forall U_y \owns y, \sup\set{t \in \RR \sth \varphi_t(x_0) \in U_y} = \infty.`

     * :math:`\varphi_t(x_0) = x_0, t \ne 0` ならば :math:`y = x_0` である。
     * そうでなければ :math:`\set{\varphi_t(x_0) \sth t \in \NN}` の集積点を :math:`y` とする。

  この問題が言いたいことは図を描いて理解するのがいい？

