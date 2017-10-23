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
      :math:`(f_1(t, t_0, x_1, \dotsc, x_n), \dotsc, f_n(t, t_0, x_1, \dotsc, x_n))` と書く。

    * :math:`\displaystyle X_i = \sum_{i = 1}^n \diff{f_i}{t}(t, t_0, x_1, \dotsc, x_n) \frac{\partial}{\partial x_i}.`

    * :math:`(t_0, \varphi(y_0))` の近傍で定義されている :math:`\RR^n` に値を持つ :math:`C^\infty` 級写像である。
    * :math:`(t_0, \varphi(y_0))` の近傍において :math:`X(t, y) = X_t(y)` による写像
      :math:`X: \RR \times R \longto TM` は :math:`C^\infty` 級写像である。

ベクトル場
  各 :math:`t` について :math:`X_t: M \longto TM` は
  :math:`p \circ X_t = \id_M` となる :math:`C^\infty` 級写像である。

  そこで、こういう性質を持つ :math:`C^\infty` 級写像 :math:`X: M \longto TM` を
  :math:`M` 上の :math:`C^\infty` 級ベクトル場と言う。

  * :math:`\displaystyle \diff{F_t}{t} = X_t \circ F_t,\ F_{t_0} = \id_M`
  * :math:`F_{t_0} = \id_M` となる :math:`F_t` により :math:`F_{t_1}(A_0) = A_1` となることは、
    ベクトル場の定める常微分方程式の解により :math:`A_0` を :math:`A_1` に写すことと同じである。

  * :math:`t \sim t_0` のとき :math:`F_t \circ F_{t_0}^{-1}` を局所座標表示するとわかる。

* 例 6.1.1: 線形常微分方程式を :math:`\RR^n` 上の接ベクトルとして書く。

  * 以下 :math:`A(t) \in M_n(\RR)` を :math:`t` について連続な行列、
    成分を :math:`A(t) = (a_{ij}(t))` と表し、ベクトル :math:`\bm{x} = (x_j)` と表す。

  * :math:`\displaystyle \diff{}{t}\bm{x} = A(t)\bm{x}` について、
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
序盤から難しい。

`フロー <http://mathworld.wolfram.com/Flow.html>`__
  フローとは次の性質を満たすアイソトピーである：
  :math:`F_s \circ F_t = F_{s + t}.`

  * フローは加法群 :math:`\RR` の多様体への群作用である。
  * ベクトル場 :math:`X_t` は、あるいは局所座標系で書かれた常微分方程式は :math:`t` に依存しない。

    * :math:`F_t` がフローの場合は :math:`\displaystyle X_{t_0}(y_0) = \frac{\partial F}{\partial t}(t_0, F_{t_0}^{-1}(y_0)) = \frac{\partial F}{\partial t}(0, y_0) = X_0(y_0)` とあるが、
      二番目の等号が成立する根拠がわからない。
      :math:`F_t = F_{t - t_0} \circ F_{t_0}` であることがどう関わっているのか。

  * ベクトル場 :math:`X = X_t` はフローを :math:`F_t` を生成するベクトル場であるという。
    生成の主従を逆に見ることもある。

* 例 6.2.1: 軌道

  :math:`\RR^n` のベクトル :math:`\bm x = (x_i)` と行列 :math:`A = (a_{ij})` を考える。

  * :math:`F_t(\bm x) = \mathrm{e}^{tA} \bm x` は :math:`\RR^n` 上のベクトル場
    :math:`\displaystyle \sum_{i = 1}^n \left( \sum_{j = 1}^n a_{ij} x_j \right)\frac{\partial}{\partial x_j}` が生成するフローである。

  * フロー :math:`\set{ F_t(\bm x) \sth t \in \RR}` を :math:`\bm x` を通る軌道という。
    この軌道は :math:`M` 上の同値関係を定義する。

  * 軌道は一点、円周、実数全体のいずれかでパラメーター付けられる。

    * 円周ならば一次元部分多様体である。

* 例 6.2.2: 平面上の線形ベクトル場の生成するフローの軌道カタログ

  * 式にすれば :math:`\displaystyle \sum_{i, j = 1}^2 a_{ij} x_j \frac{\partial}{\partial x_j}` だが、
    本書の図によると三種類に分類できるようだ。

* 問題 6.2.3: コンパクト多様体上のフローについて（後回し）

  * TBW

6.3 常微分方程式の解の存在と一意性（基本）
----------------------------------------------------------------------
* ベクトル場 :math:`X` に対して次のような :math:`F_t` が存在するのかを考える：
  :math:`F_t: M \longto M,\ F_s \circ F_t = F_{s + t}.`
* これは多様体上で常微分方程式を考える問題だ。
* 開集合 :math:`U \subset \RR^n` とコンパクト集合 :math:`K \subset U` があると仮定すれば、
  :math:`\forall \bm x \in K, \exists B_\eps(\bm x) \subset U` が成り立つ。
  コンパクト性から :math:`\eps > 0` の取り方は :math:`\bm x \in K` に依存しないというのがポイントだ。

* 定理 6.3.1 常微分方程式の解の存在、一意性、初期値に対する連続性

  * 仮定

    * リプシッツ条件：
      :math:`\exists L > 0 \text{ s.t. } t \in (a, b),\ \bm x_1, \bm x_2 \in U: \lVert X(t, \bm x_1) - X(t, \bm x_2) \rVert \le L \lVert \bm x_1 - \bm x_2 \rVert.`

    * 有界性：
      :math:`X: (a, b) \times U \longto \RR^n` は有界連続とする：
      :math:`\displaystyle \sup_{t, \bm x \in (a, b) \times U} X(t, \bm x) \le M.`

      * :math:`M` の記号がカブっている。

  * 結論

    :math:`\exists \eps_0 > 0, \exists F: (t_0 - \eps_0, t_0 + \eps_0) \times K \longto U,`

    * :math:`F(t, \bm x)` は :math:`t` について微分可能であり :math:`\bm x` について連続。
    * :math:`\displaystyle F(t_0, \bm x) = \bm x,\ \diff{F}{t} = X(t, F(t, \bm x)).`

  * 証明

    * そのある関数とは
      :math:`\displaystyle F(t, \bm x) = \bm x + \int_{t_0}^t \diff{F(s, \bm x)}{s}\ \dd{s} = \bm x + \int_{t_0}^t\! X(s, F(s, \bm x))\,\dd{s}` となる。

    * アイディア :math:`I_{\eps_0} := (t_0 - \eps_0, t_0 + \eps_0),\quad C = C^0(I_{\eps_0}, U),`

      .. math::
         :nowrap:

         \begin{align*}
         \Gamma[F(t, \bm x)] := \bm x + \int_{t_0}^t X(s, F(s, \bm x))\,\dd{s} \in C^0(I_{\eps_0}, U).
         \end{align*}

    * :math:`F_1, F_2 \in C, \sup \lVert \Gamma[F_1] - \Gamma[F_2]\rVert \le \eps_0 L \sup \lVert F_1 - F_2 \rVert` となる。
    * :math:`F_0(t, \bm x) = \bm x,\ F_1 = \Gamma[F_0]` とすると :math:`\sup \lVert F_1 - F_0 \rVert \le \eps_0 M.`
    * ここで
      :math:`\displaystyle \eps_0 = \min\Set{\frac{1}{2L}, \frac{\eps}{4M}}` とすればよいことわがかる。
    * :math:`\displaystyle \eps_0 \le \frac{1}{2L}` と :math:`\displaystyle \eps_0 \le \frac{\eps}{4M}` から解の一意性と微分可能性をそれぞれ示す。
    * :math:`C^0(I_{\eps_0} \times K, \RR^n)` 上に距離を入れてリプシッツ性を利用する。

* 注意 6.3.2 によると仮定を少し緩められるらしい。
  :math:`(a, b) \times U \times \Lambda,\ \lVert X(t, \bm x_1, \lambda) - X(t, \bm x_2, \lambda) \rVert \le L\lVert \bm x_1 - \bm x_2 \rVert.`

* 問題 6.3.3: :math:`C^1` 級ベクトル場と線形常微分方程式

  * TBW

* 注意 6.3.4: :math:`\displaystyle \frac{\partial F(t, \bm x)}{\partial t} = X(t, F(t, \bm x))` は
  :math:`\bm x` と :math:`t` のどちらについても連続であることが
  :math:`F` が :math:`C^1` 級であることに注意。

* 問題 6.3.5: ベクトル場が :math:`C^\infty` 級ならば解は :math:`C^\infty` 級である

  * 帰納法。

* 注意 6.3.6

  #. :math:`C^\infty` 級ベクトル場が生成するフローはまた :math:`C^\infty` 級である。
  #. パラメーターに対して :math:`C^\infty` 級に依存するベクトル場が生成するフローもまた
     パラメーターに対して :math:`C^\infty` 級に依存する。

6.4 コンパクト多様体上のベクトル場
----------------------------------------------------------------------
コンパクト多様体上の :math:`C^\infty` 級ベクトル場はフロー :math:`F_t` を生成する。

* 定理 6.4.1: :math:`\displaystyle X = \diff{F_t}{t} \circ F_{-t}`

  * いつもの開被覆からさらに次のような :math:`V_i, W_i` をとる：

    * :math:`U_i \supset \closure{V_i} \supset V_i \supset \closure{W_i} \supset W_i`
    * :math:`\bigcup W_i = M`

  * 証明は三段階に分けて理解する。

    #. :math:`C^\infty` 級写像 :math:`\displaystyle F: (-\eps, \eps) \times M \longto \RR^n,\quad \diff{F}{t}(t, x) = X(F(t, x))` が存在することを示す。

       * :math:`\displaystyle X = \sum_{k}\xi_k^{(i)}\frac{\partial}{\partial x_k^{(i)}}` とおく。
         閉包のコンパクト性から :math:`\varphi_i(V_i)` 上で有界連続でリプシッツ条件を満たす。

       * :math:`\varphi_i(\closure{W_i}) \subset \varphi_i(V_i)` において次のような :math:`\eps^{(i)} > 0` が存在する：

         .. math::
            :nowrap:

            \begin{align*}
            & F^{(i)}: (-\eps^{(i)}, \eps^{(i)}) \times \varphi_i(\closure{W_i}) \longto \varphi_i(V_i)\\
            & \diff{F^{(i)}}{t}(t, \bm x) = \xi^{(i)}(F^{(i)}(t, \bm x))\\
            \end{align*}

         ここで :math:`\xi^{(i)} = (\xi_1^{(i)}, \dotsc, \xi_n^{(i)})` とした。

       * :math:`\eps = \min\set{\eps^{(i)}}` とすると全ての :math:`x \in M` に対して次の性質を満たすような近傍 :math:`W^i` が存在する：

         .. math::
            :nowrap:

            \begin{align*}
            & F^i(t, x) = \varphi_i^{-1}(F^{(i)}(t, \varphi_i(x)))\\
            & F_x^i: (-\eps, \eps) \longto M\\
            & \diff{F_x^i}{t}(t) = X(F_x^i(t)).
            \end{align*}

       * 別の :math:`W_j \owns x` について :math:`F_x^j` を上のように定義すると
         :math:`F_x^j = F_x^i` となる（常微分方程式の解の比較）。

    #. 解の接続。上記写像の定義域を :math:`\RR \times M` にまで拡張した写像が存在することを示す。

       * :math:`\displaystyle t \in \left(-\eps,\ \frac{\eps}{2}\eps\right)` のときは
         :math:`\displaystyle t \in \left(\frac{n - 1}{2}\eps,\ \frac{n + 1}{2}\eps\right)` に対して改めて
         :math:`\displaystyle F(t, x) = F\!\left(t - \frac{n - 1}{2}\eps,\ F\!\left(\frac{n - 1}{2}\eps,\ x\right)\!\right)` とする。

       * :math:`\displaystyle t \in \left(-\frac{\eps}{2}\eps,\ \eps\right)` のときは
         上でやった区間の「反対側」に対して改めて
         :math:`\displaystyle F(t, x) = F\!\left( t + \frac{n - 1}{2}\eps,\ F\!\left( -\frac{n - 1}{2}\eps,\ x\right)\!\right)` とする。

       どちらも :math:`\displaystyle \diff{F}{t}(t, x) = X(F(t, x))` が成り立っている。

    #. :math:`F(t + s, x) = F(t, F(s, x))` を示す。

* 例題 6.4.3: 連結コンパクト一次元多様体が向き付け可能であることを使えば、
  多様体上にゼロでないベクトル場が存在することがわかり、
  :math:`M \cong \RR/\ZZ` が成り立つ。

  * 各座標近傍 :math:`U_i` に対し 1 の分割 :math:`\lambda_i` を導入する。
  * :math:`U_i` に台を持つベクトル場 :math:`\displaystyle \lambda_i \frac{\partial}{\partial t^{(i)}}` を考える。
    ここで :math:`t^{(i)}` は座標とする。

  * :math:`\displaystyle X = \sum_i \lambda_i \frac{\partial}{\partial t^{(i)}} \ne 0` を示す。

    * :math:`D\gamma_{ij} > 0` および :math:`\sum_i \lambda_i = 1` を利用する。

  * :math:`X` が生成するフローの軌道は前に述べたように 3 通り。
    このうち連結コンパクトなのは円周しかなかった。

* 注意 6.4.4 は長いが、連結コンパクト一次元多様体が向き付け可能であること自体の証明だ。

* 問題 6.4.5: 次の条件を満たす :math:`\displaystyle \mu\frac{\partial}{\partial x_1}` が生成するフロー
  :math:`\Phi_t` の :math:`\displaystyle \lim_{t \to \infty}\Phi_t(\bm x)` と
  :math:`\displaystyle \lim_{t \to -\infty}\Phi_t(\bm x)` の値

  * :math:`\mu: \RR^n \longto \RR` は :math:`C^\infty` 級で、
  * :math:`\supp \mu = \set{\bm x \in \RR^n \sth \lVert \bm x \rVert \le 1},`
  * :math:`\lVert \bm x \rVert < 1 \implies \mu(\bm x) > 0` と仮定する。

  #. 単位超球面上およびその外側

     :math:`\mu(\bm x) = 0` なので極限値はどちらも :math:`\bm x` となる。

  #. 単位超球面内部の場合

     TBW

6.5 連結多様体上の部分集合の比較
----------------------------------------------------------------------
連結多様体上の点は平等であり、特別な点は存在しない (p. 135)。

* 例題 6.5.1: 連結多様体上の任意の二点について、一方を他方に写す微分同相写像が存在する。

  * 証明には前問 6.4.5 の技法を用いる。
  * 連結多様体上の一点を固定して、微分同相で写り合う点は同値関係となる。
    この同値類が開集合であることを示す必要がある。
  * <同値類が開集合であることを示したから、閉集合でもある> (p. 135) とあるが、ここが理解できない。

* 注意 6.5.2: 例えばアイソトピーもとれることが上のようにわかる。
* 問題 6.5.3: 多様体次元が 2 以上の連結多様体上には、
  相異なる :math:`n` 点と別の相異なる :math:`n` 点とについて、一方を他方に写す微分同相写像が存在する。

  * 証明は帰納法による。

    #. 一点対一点の場合は例題 6.5.1 により成り立つ。
    #. :math:`x_1, \dots, x_{n - 1} \in M` を :math:`y_1, \dots, y_{n - 1} \in M` にそれぞれ写す
       微分同相写像 :math:`F_1: M \longto M` が存在すると仮定する。

       * :math:`M' = M \setminus \set{y_1, \dots, y_{n - 1}}` とおくと、これは連結である（この証明がメインか？）。
       * :math:`F': M' \longto M,\quad F'(F_1(x_n)) = y_n` となる :math:`F'` が例題 6.5.1 により存在する。
       * :math:`F'` の定義域を元の多様体に次のように拡張して :math:`\hat{F'}` とすれば、
         :math:`F = \hat{F'} \circ F_1` が求める微分同相写像だ。

         * 点 :math:`y_i` の近傍の点 :math:`y` に対しては :math:`F' = \id \text{ i.e. } F'(y) = y.`

* 問題 6.5.4: 連結多様体上の任意の二点 :math:`x_0, x_1` に対して次のようなフロー :math:`F_t` が存在する：
  :math:`F_t(x_0) = x_1.`

:math:`F: M \longto N` の二つの正則値 :math:`y_0, y_1` に対する :math:`F^{-1}(y_0), F^{-1}(y_1)` の比較をしたい。

* 例題 6.5.5: TBW

  * :math:`M, N` をコンパクト連結多様体、
  * :math:`F \in C^\infty(M, N),`
  * :math:`\xi, \eta` をベクトル場とする。
  * :math:`\xi, \eta` の生成するフローをそれぞれ :math:`\varphi_t, \psi_t` とする。

  :math:`\forall x \in M, F_*(\xi(x)) = \eta(F(x)) \implies F(\varphi_t(x)) = \psi_t(F(x)).`

  * 証明するには :math:`\displaystyle \diff{F(\varphi_t(x))}{t} = \eta(F(\varphi_t(x)))` を示す。

* 問題 6.5.6: コンパクト連結多様体 :math:`M` 上の :math:`C^\infty` 級関数 :math:`f` について
  :math:`[a, b] \subset \RR` はすべて正則値であるとすると、次が成り立つ：

  :math:`f^{-1}([a, b]) \cong f^{-1}(a) \times [a, b].`

* 問題 6.5.7: フローボックス定理

  * 仮定

    * :math:`M` を :math:`m` 次元コンパクト多様体、
    * :math:`N \subset M` を :math:`m - 1` 次元コンパクト部分多様体、
    * :math:`\xi` をベクトル場、
    * :math:`\varphi_t(x)` を :math:`\xi` が生成するフロー、
    * :math:`\forall x \in N, \xi(x) \notin T_x N` とする。

  * 結論

    * 次を満たす写像と数 :math:`\eps > 0` が存在する：

      写像 :math:`(-\eps, \eps) \times N \longto M` が :math:`M` の開集合への埋め込みである。

  * 証明

    TBW

6.6 第 6 章の解答
----------------------------------------------------------------------
TBW

----

:doc:`note7` へ。
