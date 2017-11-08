======================================================================
幾何学 I 多様体入門 読書ノート 8/8
======================================================================

:doc:`note7` からの続き。最終章。

.. contents:: ノート目次

第 8 章 多様体上のベクトル場
======================================================================
* 微分法を多様体上で考える。
* 多様体上の変化の対象はフローとするのが自然だ。

8.1 フローと関数
----------------------------------------------------------------------
* フロー :math:`F_t` と :math:`C^\infty` 級関数 :math:`f` について、フローの軌道に沿う変化が考えられる。
  すなわちフローを生成するベクトル場を :math:`\displaystyle X = \diff{F_t}{t} \circ F_t\inv` とすると

  .. math::

     \diff{(f \circ F_t)(x)}{t} = (Xf)(F_t(x)).

  ベクトル場による関数の微分とは、ベクトル場が生成するフローの軌道に沿った変化率ということか。

* :math:`Xf: M \longto \RR` は :math:`C^\infty` 級である。
* :math:`X: C^\infty(M) \longto C^\infty(M)` は線形写像かつライプニッツ則を満たす (cf. 問題 5.1.6)。
* :math:`Xf = 0 \implies f(F_t(x)) = f(x).`

* 問題 8.1.1: :math:`X = \dfrac{\partial}{\partial x} + \alpha \dfrac{\partial}{\partial y},\ \alpha \in \RR \setminus \QQ`
  は :math:`\RR^2/\ZZ^2` 上のベクトル場を与える。
  このとき :math:`f \in C^\infty(M)` が :math:`Xf = 0` であるならば :math:`f` は定数関数である。

  * まず :math:`X` のフロー :math:`\varphi_t` を :math:`\RR^2` で計算する。

    * :math:`x, y` ごとに単純に微分方程式を解くと :math:`x = t + x_0,\ y = \alpha t + y_0` のようになる。
    * :math:`\varphi_t(x0, y0) = (x_0, y_0) + (t, \alpha t)` で初期値をそのまま変数の文字に置き換えて
      :math:`\varphi_t(x, y) = (x + t, y + \alpha t)` となる。
      これは :math:`\varphi_t \circ \varphi_s = \varphi_{t + s}` を満たすのでフローになっている。

  * 次に :math:`\varphi_t(x, y) = (x + t, y + \alpha t) \pmod{\ZZ^2}` は
    :math:`\RR^2/\ZZ^2` 上のフローとなっていることを確認する。

  * 軌道は :math:`G(x, y) = \set{(x + t, y + \alpha t) \in \RR^2/\ZZ^2 \sth t \in \RR}` と書ける。
    この集合は稠密なので、ベクトル場によりゼロになる関数は定数関数となる。

    * だから本題はこの軌道の稠密性の証明だ。
      この軌道は :math:`\RR^2/\ZZ^2` の上下左右の縁で無限ループする傾きが :math:`\alpha` の直線だ。
      図に描くといい。

    * 稠密でないと仮定して矛盾を導く。
      適当な :math:`\eps > 0` が存在して開円板 :math:`D_\eps` が :math:`\subset \RR^2/\ZZ^2 \setminus G(x, y).`
      となるようなものがある。
    * そのような正の数で最大のものを改めて :math:`\eps` とする。
    * (?) :math:`\closure{D_\eps} \supset \closure{G(x, y)}.` 
    * このとき各 :math:`\varphi_{2n\eps}(D_\eps)\quad(n \in \ZZ)` は互いに交わらない。
    * :math:`\varphi_{2n\eps}(D_\eps)` の面積の和を :math:`n \in \ZZ` についてとると、
      これは :math:`\infty` に発散する。
      しかし、これは :math:`\RR^2/\ZZ^2` の面積 1 を超えるので矛盾となる。

* 問題 8.1.2: コンパクト多様体上のベクトル場 :math:`X` と多様体上の :math:`C^\infty` 級関数
  :math:`f` について :math:`Xf = 0 \implies f = 0`

  .. math::

     \diff{(f \circ \varphi_t(x))}{t} = (Xf)(\varphi_t(x)) = f(\varphi_t(x)).

  これを解くと :math:`\varphi_t(x) = \mathrm{e}^t f(x).`

  * :math:`f(x) \ne 0` とすると :math:`f \to \infty\ (t \to \infty)` となるが、
    これは多様体がコンパクトであることに矛盾する（本書ではわざわざこれに言及していない）。
    したがって :math:`f(x) = 0.`

* フローに沿う微分は偏微分であると考える。

  * :math:`\RR^2` で定義された :math:`C^\infty` 級関数のような
    :math:`\displaystyle \frac{\partial^2 f}{\partial x \partial y} = \frac{\partial^2 f}{\partial y \partial x}` が成り立つこととは事情が違って、
    ベクトル場二つを順に作用させる結果は、その作用の順序に依存する。

8.2 フローとベクトル場
----------------------------------------------------------------------
* 定義 8.2.1: `ブラケット積 or 括弧積 <http://mathworld.wolfram.com/Commutator.html>`__

  :math:`X, Y` をベクトル場、
  :math:`X` の生成するフロー :math:`F_t` について次の値を定義する：

  .. math::

     [X, Y] = \left.\diff{}{t}\right|_{t = 0}(F_{-t})_*Y

  * :math:`[X, Y]` もベクトル場となる。
  * :math:`X, Y` どちらについても線形である :math:`\because [Y, X] = -[X, Y]`
  * `ヤコビ恒等式 <http://mathworld.wolfram.com/JacobiIdentities.html>`__ が成り立つ。
    すなわち :math:`Z` もベクトル場とすると
    :math:`[[X, Y], Z] + [[Y, Z], X] + [[Z, X], Y] = 0.`
  * ベクトル場は関数空間から関数空間への微分作用素でもある。
  * :math:`[X, Y]f = X(Yf) - Y(Xf)` 計算しやすい。
  * 式で書き下してみる：

    .. math::

       [X, Y] = \sum_{i, j}\left(
           X_i \frac{\partial}{\partial x_i} Y_j \frac{\partial}{\partial x_j}
          -Y_j \frac{\partial}{\partial x_j} X_i \frac{\partial}{\partial x_i}
       \right),\\
       \text{ where }
       X = \sum_{i}X_i \frac{\partial}{\partial x_i},\ 
       Y = \sum_{i}Y_i \frac{\partial}{\partial x_i}.

  * 幾何的解釈は「ベクトル場 :math:`Y` を :math:`F_{-t}` で動かしたときの変化率」である。

* 例題 8.2.2: :math:`n` 次元ユークリッド空間上の線形ベクトル場の括弧積

  #. 式で書き下す。

     :math:`\displaystyle X = \sum_{i, j}^n a_{ij} x_j \frac{\partial}{\partial x_i}`,
     :math:`\displaystyle Y = \sum_{i, j}^n b_{ij} x_j \frac{\partial}{\partial x_i}`
     と置いてひたすら式を展開する。
     最終的に :math:`\sum` 記号が三つ並ぶ。

  #. :math:`X` が :math:`\varphi_t` を生成するとして :math:`(\varphi_{-t}Y)` を書いて、
     それに基いて :math:`[X, Y] = \left.\diff{}{t}\right|_{t = 0}((\varphi_{-t})_*Y)` を求める。

     * :math:`A = (a_{ij}), B = (b_{ij})` とする。
       :math:`X` のフローは微分方程式を解いて :math:`\varphi_t(\bm x) = \mathrm e^{tA} \bm x` であるから、
       :math:`((\varphi_{-t})_*Y)(\bm x) = \mathrm e^{-tA}B \mathrm e^{tA} \bm x`

       .. math::

          \begin{align*}
          \diff{}{t}((\varphi_{-t})_*Y)(\bm x)
          &= \diff{}{t}(\mathrm e^{-tA}B \mathrm e^{tA} \bm x)\\
          &= -A \mathrm e^{-tA}B \mathrm e^{tA} \bm x + \mathrm e^{-tA}BA \mathrm e^{tA} \bm x\\
          &= -\mathrm e^{-tA}(AB - BA)\mathrm e^{tA} \bm x
          \\
          \therefore \left.\diff{}{t}\right|_{t = 0}((\varphi_{-t})_*Y) &= -(AB - BA).
          \end{align*}

  なお、微分同相写像 :math:`\varphi_t` とベクトル場 :math:`Y` に対して
  ベクトル場 :math:`{\varphi_t}_*Y` を次の式で定義する：

  .. math::

     \begin{align*}
     ({\varphi_t}_*Y)(\varphi_t(x)) &= {\varphi_t}_*(Y(x)), \quad\text{or }\\
     ({\varphi_t}_*Y)(x) &= {\varphi_t}_*(Y(\varphi_{-t}(x))).
     \end{align*}

* 例題 8.2.3

  仮定：

  * :math:`M, N` をコンパクト多様体、
  * :math:`F: M \longto N` を :math:`C^\infty` 級写像、
  * :math:`X, Y` を :math:`N` 上のベクトル場とし、
  * :math:`\overset{\sim}{X}, \overset{\sim}{Y}` を :math:`M` 上のベクトル場で次のようになっている：
    :math:`F_*\overset{\sim}{X} = X,\ F_*\overset{\sim}{Y} = Y.`

  結論：

  * :math:`F_*([\overset{\sim}{X}, \overset{\sim}{Y}]) = [X, Y].`
  * 特に :math:`F: N \longto N` が微分同相ならば :math:`F_*([X, Y]) = [F_*X, F_*Y].`

  証明：

  * 方針：例題 6.5.5 の恒等式 :math:`F \circ \overset{\sim}{\varphi_t} = \varphi_t \circ F`
    を利用する。
  * あとなぜか :math:`\displaystyle [\overset{\sim}{X}, \overset{\sim}{Y}] = \lim_{t \to 0}\frac{1}{t}(\overset{\sim}{\varphi_{-t}}_* \overset{\sim}{Y} - \overset{\sim}{Y})`
    を利用する。

  .. math::

     \begin{align*}
     F_*([\overset{\sim}{X}, \overset{\sim}{Y}])
     &= F_*\left(\lim_{t \to 0}\frac{\overset{\sim}{\varphi_{-t}}_* \overset{\sim}{Y} - \overset{\sim}{Y}}{t}\right)\\
     &= \lim_{t \to 0}\frac{\overset{\sim}{\varphi_{-t}}_* F_* \overset{\sim}{Y} - F_* \overset{\sim}{Y}}{t}\\
     &= \lim_{t \to 0}\frac{{\varphi_{-t}}_* Y - Y}{t}\\
     &= [X, Y].
     \end{align*}

  * 最初の等号は括弧積の定義による。
  * 次の等号は例題 6.5.5 の恒等式による。
  * その次の等号は本問の仮定を使った。
  * 最後の等号は再び括弧積の定義による。

* 例題 8.2.4

  仮定：

  * :math:`M` はコンパクト多様体で、
  * :math:`\xi, \eta` はその上のベクトル場であって、
  * :math:`[\xi, \eta] = 0` であり、
  * それぞれのベクトル場はフロー :math:`\varphi_s, \psi_t` を生成する。

  結論：

  * :math:`\varphi_s \circ \psi_t = \psi_t \circ \varphi_s.`

  証明：

  * :math:`(\varphi_s)_*\eta = \eta` を示したい。
  * :math:`\displaystyle \left.\diff{}{s}((\varphi_{-s})_*\eta)(x)\right|_{s = 0} = 0` を示して
    :math:`s = 0` で :math:`(\varphi_s)_*\eta = \eta` を示して結論する。

  .. math::

     \begin{align*}
     \diff{({\varphi_{-s}}_*\eta)(x)}{s}
     &= {\varphi_{-s}}_* \left( \left.\diff{({\varphi_{-u}}_*\eta)(\varphi_s(x))}{u}\right|_{s = 0}\right)\\
     &= {\varphi_{-s}}_* ([\xi, \eta]\varphi_s(x))\\
     &= {\varphi_{-s}}_* (0)\\
     &= 0.
     \end{align*}

  したがって :math:`{\varphi_{-s}}_*\eta(x) = \id_*\eta(x) = \eta(x).`
  すなわち :math:`{\varphi_{-s}}_*\eta = \eta.`

* 問題 8.2.5

  仮定：

  * :math:`M` はコンパクト多様体で、
  * :math:`\xi, \eta` はその上のベクトル場であって、
  * :math:`[\xi, \eta] = \eta` であり、
  * それぞれのベクトル場はフロー :math:`\varphi_s, \psi_t` を生成する。

  結論：

  * (A): :math:`{\varphi_s}_*\eta = \mathrm e^s\eta,`
  * (B): :math:`\varphi_s \circ \psi_t \circ \varphi_{-s} = \psi_{\mathrm e^s t}.`

  証明：

  * (A) ならば :math:`\mathrm e^s\eta` が :math:`\psi_{\mathrm e^s t}`
    を生成するということであるので (B) であると言える。

    .. math::

       \begin{align*}
       \diff{({\varphi_{-s}}_*\eta)(x)}{s}
       &= \dots\\
       &= {\varphi_{-s}}_* ([\xi, \eta]\varphi_s(x))\\
       &= {\varphi_{-s}}_* \eta(\varphi_s(x))\\
       &= {\varphi_{-s}}_* \eta(x).
       \end{align*}

  * 次に :math:`\displaystyle \left.\diff{(\mathrm e^s\eta)(x)}{s}\right|_s = \mathrm e^s \eta(x)` を利用して
    :math:`s = 0` のときを確かめる。

    .. math::

       \left.{\varphi_{-s}}_* \eta\right|_{s=0} = \eta = \left.\mathrm e^s \eta\right|_{s=0}.

    したがって :math:`{\varphi_{-s}}_* \eta = \mathrm e^s \eta.`

* リー群（多様体でもある）の構造の解析にはそれに即したベクトル場を用いる。

* 問題 8.2.6: リー群

  #. 左不変ベクトル場全体 :math:`\mathfrak g` は :math:`\dim G` 次元のベクトル空間である
     （`リー環 or リー代数 <http://mathworld.wolfram.com/LieAlgebra.html>`__）。

     * :math:`X` が左不変ベクトル場であるとは :math:`\forall g \in G, (L_g)_*X = X` であることをいう。
     * :math:`L_g` の定義は 4.3.3 でやった。
     * :math:`\mathfrak g = \set{X \in \mathcal X(G) \sth (L_g)_*X = X}.`

     証明は :math:`\mathfrak g` と :math:`T_1G` が同型であることを示す。

     * 写像 :math:`E(\xi) = xi(1)` を考える。これはベクトル空間の準同型写像であるので、
       あとは全単射性を示せばよい。

     * :math:`E` が単射であること：

       * :math:`E(\xi) = 0 \implies \xi = 0` を示す。
       * :math:`g, h \in G` と :math:`\xi \in \mathfrak g` に対してこうなっている：

         .. math::

            \xi(h) = (L_g)_*\xi(h) = \xi(L_g(h)) = \xi(gh).\\

       * 特に :math:`h = 1` とすると :math:`\xi(g) = {L_g}_*\xi(1) = {L_g}_*E(1)` なので
         :math:`E(\xi) = 0 \implies \xi = 0` が成り立つ。

     * :math:`E` が全射であること：

       * :math:`v \in T_1G` に対して :math:`\xi(h) = {L_h}_*\xi(1)` となる
         :math:`\xi \in \mathcal X(G)` および :math:`h \in G` をとる。
         このとき：

         .. math::

            L_g(\xi(h)) = {L_g}_*({L_h}_* v) = {L_{gh}}v = \xi(gh).

       * したがって :math:`\xi \in \mathfrak g` かつ :math:`E(\xi) = v` である。

  #. :math:`\xi, \eta` を左不変ベクトル場とすると :math:`[\xi, \eta]` もそうである。

     .. math::

        \begin{align*}
        &{L_g}_*[\xi, \eta] = [{L_g}_*\xi, {L_g}_*\eta] = [\xi, \eta].\\
        &\therefore [\xi, \eta] \in \mathfrak g.
        \end{align*}

     ここで例題 8.2.3 の結果を利用している。

  #. :math:`\xi` が生成するフローを :math:`\varphi_t` とする。このとき
     :math:`\forall g \in G, \varphi_t(g) = g\varphi_t(1).`

     * この :math:`\varphi_t(1)` を :math:`\exp(t\xi)` と書く。
     * :math:`{L_g}_* \xi = \xi` より :math:`{L_g}_* \varphi_t = \varphi_t L_g.`
     * したがって :math:`\varphi_t(g) = \varphi_t(L_g(1)) = L_g \varphi_t(1) = g\varphi_t(1).`

  #. :math:`\xi \longmapsto \exp(\xi)` は :math:`\mathfrak g` のゼロ近傍から
     :math:`G` の単位元 1 の近傍への微分同相写像である。

     * 接写像 :math:`\exp_*: T_0\mathfrak g \longmapsto T_1G` が同型写像であることを示す。
     * :math:`t = 0` における曲線 :math:`t\xi\quad(t \in \RR)` の接ベクトルは
       :math:`\xi \in \mathfrak g \cong T_0\mathfrak g` である。
     * :math:`G` 上の曲線 :math:`\exp(t\xi) = \varphi_t(1)` の
       :math:`t = 0` における接ベクトルを計算して :math:`= \xi(1) \in T_1(G)` とする。

       .. math::

          \begin{align*}
          \left.\diff{\exp(t\xi)}{t}\right|_{t = 0}
          &= \left.\diff{\varphi_t(1)}{t}\right|_{t = 0}\\
          &= \left.\xi(\varphi_t(1))\right|_{t = 0}\\
          &= \xi(1) \in T_1(G).
          \end{align*}

       * 最初の等号は :math:`\exp(t\xi)` の定義による。
       * 次の等号はベクトル場とフローの関係による。
       * 最後の等号は :math:`t = 0` による。

     * あとは逆写像定理による。

* 注意 8.2.7

  * :math:`G \subset GL_n(\RR)` を部分群とすると、
    :math:`A \in G` における接ベクトルが :math:`AX` の形（ベクトルとは言っているが行列である）をしていることが
    :math:`X` が左不変であることの条件である。

    * :math:`X` が生成するフローを :math:`F_t` とする。このとき
      :math:`\displaystyle \diff{F_t(A)}{t} = F_t(A)X` を満たすので
      :math:`F_t(A) = \mathrm e^{tX}.`

  * 問題 8.2.6 の :math:`\exp` はリー群版の指数写像である。

8.3 行列群上の計量（展開）
----------------------------------------------------------------------
:math:`G = GL_n(\RR)` 上の曲線 :math:`c(t)` の「接ベクトルの長さの自乗」を二通り与えて、
それぞれの測地線の方程式を調べる。ただしどちらの与え方も
:math:`G` の左作用が接ベクトルの長さを不変にするように定義する。

#. :math:`\trace {}^t\!(c'){}^t\!(c\inv)c\invc'`
#. :math:`\trace c\invc'c\invc'`

* 単位行列 :math:`I_n` においては :math:`n^2` 次元ユークリッド空間の計量と一致する。
* この前と同じく変分法を適用して、値がゼロになる必要条件をそれぞれ調べる。

それぞれの測地線の方程式は次のようになる：

#. :math:`-c\invc'' + {}^t\!(c\invc')(c\invc') + (c\invc')^2 - (c\invc')\ {}^t\!(c\invc') = 0`
#. :math:`-(c\invc')' = 0`

* 例題 8.3.1: 最初の :math:`c(t) = \mathrm e^{tA}` が測地線である条件

  * 測地線の式の左辺を展開すると :math:`{}^t\!AA - A\,^t\!A` となるが、
    これがゼロであるということは :math:`A \in O(n)` を意味する。

* 行列群上の計量は非リーマンであるのがよい。
  そうすると曲線の長さが正にも負にもなるかもしれず、そうなると局所性最短性はどこかへ行ってしまう。
  ただし、長さは「臨界的である」ことで定義される。

* 指数写像とは、リーマン多様体上の測地線の方程式により定義される写像だ。

8.4 k-枠場（展開）
----------------------------------------------------------------------
k-枠場
  多様体 :math:`M` 上の一次独立なベクトル場 k 個の組を意味する。
  :math:`0 \le k \le \dim M`

  * 例：二次元曲面 :math:`\Sigma_g\ (g \le 2)` 上には 1-枠場と 2-枠場のどちらも存在しない。
    一方、トーラス :math:`T^2` 上にはどちらも存在する。

  * n-枠場を持つ n 次元多様体を `平行可能化多様体 <http://mathworld.wolfram.com/Parallelizable.html>`__ と呼ぶ。

2-枠場のある多様体 :math:`M` 上で :math:`[\xi_1, \xi_2] = 0` であれば
:math:`\RR^2` の :math:`M` への作用 :math:`(\varphi_1^{t_1} \circ \varphi_2^{t_2})(x)` を定義することで
:math:`\RR^2` 作用の軌道の族で :math:`M` を分割することができる。
このとき、軌道は :math:`M` の各点の近傍に対して二次元の共通部分を持つ。

* :math:`x \in M` を固定すると作用の接写像のランクが 2 である。
* 共通部分は高々可算個である。

これを 2 から k に拡張する。
一般に k 枠場 :math:`(\xi_1, \dotsc, \xi_k)` が :math:`[\xi_i, \xi_j] = 0` であるならば、
加法群 :math:`\RR^k` の :math:`M` への作用を次のように定義できて、
:math:`M` は k 次元の :math:`\RR^k` 作用の軌道に分割される。

.. math::

   \varphi_1^{t_1} \circ \dotsb \circ \varphi_k^{t_k} (x)

:math:`M` の各点の近傍 :math:`U` においてランク :math:`n - k` の写像
:math:`F: U \longto \RR^{n - k}` が存在して、軌道と近傍の共通部分が
:math:`F` で決まる近傍の k 次元部分多様体の和集合となる。

* 例 8.4.1: :math:`\RR^3` 上のベクトル場

  * :math:`f \in C^\infty(\RR^2).`
  * :math:`\displaystyle \xi_1 = \frac{\partial}{\partial x_1} + \frac{\partial f}{\partial x_1}\frac{\partial}{\partial x_3},`
    :math:`\displaystyle \xi_2 = \frac{\partial}{\partial x_2} + \frac{\partial f}{\partial x_2}\frac{\partial}{\partial x_3}.`
  * :math:`[\xi_1, \xi_2] = 0.`
  * :math:`h = x_3 - f(x_1, f_2)` が一定である点からなる曲面が :math:`\RR^2` 作用の軌道となる。

* 例 8.4.2: ダメな例

  * :math:`\displaystyle \xi_1 = \frac{\partial}{\partial x_1} - x_2 \frac{\partial}{\partial x_3},`
    :math:`\displaystyle \xi_2 = \frac{\partial}{\partial x_2}.`

  * :math:`\because [\xi_1, \xi_2] = \frac{\partial}{\partial x_3}.`

k 次元接平面場 or k 次元分布
  多様体 :math:`M` 上の k 次元接平面場に対して、各点の近傍ではその
  k 次元接平面場を張る k 枠場に取り替えられる。

* 定理 8.4.3:
  :math:`\RR^n` の開集合 :math:`U` 上の k-枠場が :math:`U` の各点の近傍に対して
  :math:`[\xi_i, \xi_j]` が 0 となる k-枠場に取り替えられることは、
  :math:`[\xi_i, \xi_j]` が :math:`\xi_1, \dotsc, \xi_k` の張る k-枠場に値を持つことと同値である。

  * 証明がよくわからない。

  * :math:`(\xi_1, \dotsc, \xi_k)` と :math:`(\eta_1, \dotsc, \eta_k)` が同じ接平面場を与えるならば
    :math:`\exists a_{ij}: U \longto GL_k(\RR)\quad\text{s.t. } \eta_i = \sum_{j = 1}^k a_{ij}\xi_j`
    を示す。

    * 一方の括弧積を計算することで、他方の括弧積と同時に接平面場に値を持つことがわかる：

      .. math::

         \begin{align*}
         [\eta_l, \eta_m]
         &= \left[\sum_{i = 1}^k a_{li}\xi_i, \sum_{k = 1}^k a_{mi}\xi_i\right]\\
         &= \sum_{i, j} a_{li}\xi_j(a_{mj})\xi_j - \sum_{i,j} a_{mj}(\xi_j a_{li})\xi_i + \sum_{i,j}a_{li}a_{mj}[\xi_i, \xi_j].
         \end{align*}

  * 十分：適当に座標を取り替えて写像 :math:`p: \RR^n \longto \RR^k` を
    :math:`p(\bm x) = (x_1, \dotsc, x_k)` で定義する。

    * 点の近傍上 :math:`p_*` を接平面場に制限した接写像は何かとの同型を与える。
    * その次の「
      :math:`V` 上の k 枠場 :math:`(\eta_1, \dotsc, \eta_k)` を
      :math:`p_* \eta_i = \dfrac{\partial}{\partial x_i}` となるようにとれる」
      がわかりにくい。
    * :math:`[\eta_l, \eta_m]` が値を持てば
      :math:`p_*[\eta_l, \eta_m] = \left[\dfrac{\partial}{\partial x_i}, \dfrac{\partial}{\partial x_j}\right] = 0`
      より 0 が値である。

* フローの可換性の成立だけで :math:`U` 内の「軌道」が :math:`F` によって定まる
  :math:`U` の k 次元部分多様体となるといえる。

  * 「軌道」と書いたが、
    :math:`x` において k 次元接平面場は :math:`T_x(F\inv(F(x)))` と一致する。

* 定理 8.4.4: `フロベニウス <https://en.wikipedia.org/wiki/Frobenius_theorem_(differential_topology)>`__

  * :math:`[\xi_i, \xi_j]` が k 次元接平面場に値を持つということを
    `（完全）積分可能条件 <https://en.wikipedia.org/wiki/Integrability_conditions_for_differential_systems>`__ という。

  * :math:`F_V\inv(F_V(x)),\ T_x(F_V\inv(F_V(x))) \subset T_xM` と
    :math:`x` における k 次元接平面場が一致する。

  * （極大）積分多様体
    or `葉 <http://mathworld.wolfram.com/FoliationLeaf.html>`__

  * 共通部分できれいに貼り合わさる。
  * 「正則とは限らない」部分多様体とは？
  * `葉層 <http://mathworld.wolfram.com/Foliation.html>`__ 構造（本書図 8.2 参照）

8.5 勾配ベクトル場
----------------------------------------------------------------------
多様体上の微分可能関数 :math:`f \in C^1(M)` とベクトル場 :math:`X` と
リーマン計量 :math:`g` に対して、ベクトル場 :math:`\grad f` を次で定義する：

.. math::

   \begin{align*}
   Xf &= g(X, \grad f),\text{ or }\\
   \grad f &= \sum_{i = 1}^n \sum_{j = 1}^n g^{ij} \frac{\partial f}{\partial x_j}\frac{\partial}{\partial x_i}.
   \end{align*}

* :math:`f` の等位面が部分多様体であるとき、
  :math:`f\inv(a)` と :math:`\grad f` は直交する。
  なぜならば :math:`f\inv(a)` の接ベクトル :math:`v` を取ると
  :math:`f_*v = 0` であって :math:`g(v, \grad f) = 0` が成り立つ。

  .. math::

     f_*v = 0 \implies g(v, \grad f) = \sum \frac{\partial}{\partial x_i} v_i = 0

* :math:`\grad f` が生成するフローを gradient flow と呼ぶ。

* 例 8.5.1: 球面上の微分可能関数に対する勾配ベクトル場

  * :math:`S^2` のパラメーター表示を
    :math:`(x, y, z) = (\cos\theta\cos\cos\varphi, \sin\theta\cos\varphi, \sin\varphi)` とおく。

  * ベクトル場の基底を :math:`\dfrac{\partial}{\partial \theta}, \dfrac{\partial}{\partial \varphi}` ととる。
  * リーマン計量は :math:`\displaystyle g = \begin{pmatrix}\cos^2\varphi & 0\\0 & 1\end{pmatrix}` と書ける。
  * 次のようにおいて :math:`g(\grad f, X)` と :math:`X(f)` をそれぞれ計算する：

    .. math::

       \begin{align*}
       \grad f &= a\frac{\partial}{\partial \theta} + b\frac{\partial}{\partial \varphi},\\
       X &= u\frac{\partial}{\partial \theta} + v\frac{\partial}{\partial \varphi}.
       \end{align*}

    計算の結果 :math:`\grad f = \cos\varphi \dfrac{\partial}{\partial \varphi}` となる。
    直交座標系で書くと :math:`-xz\dfrac{\partial}{\partial x} - yz\dfrac{\partial}{\partial y} + (1 - z^2)\dfrac{\partial}{\partial z}.`

* 例題 8.5.2

  #. :math:`f(x, y) = x^3 - x + y^2` のグラフを描け。

     * フローが等位線と直交するように描くのが鉄則。
     * :math:`X = \dfrac{\partial f}{\partial x}\dfrac{\partial}{\partial x} + \dfrac{\partial f}{\partial y}\dfrac{\partial}{\partial y}` は
       ユークリッド計量についての :math:`f` の勾配ベクトル場である。
     * :math:`Xf = \left(\dfrac{\partial f}{\partial x}\right)^2 + \left(\dfrac{\partial f}{\partial y}\right)^2 \le 0` より
       非減少である。

  #. :math:`\displaystyle \diff{x}{t} = \frac{\partial}{\partial x},\ \diff{y}{t} = \frac{\partial}{\partial y}` の解曲線を求めろ。

* 問題 8.5.3

  :math:`\grad f \ne 0` なる点で定義されるベクトル場
  :math:`\displaystyle Y = \frac{\grad f}{g(\grad f, \grad f)}` およびその解曲線
  :math:`c(t)` について。

  定義域では :math:`f(c(t_0 + t)) - f(c(t_0)) = t.`
  :math:`Yf = 1` より :math:`\displaystyle \diff{(f \circ \varphi_t)(x)}{t} = (Yf)(\varphi_t(x)) = 1.`
  :math:`\therefore\ f(\varphi_t(x)) - f(x) = t.`

* モース関数について

  * 臨界点近傍で :math:`\displaystyle f = \sum_{i = 1}^\lambda x_i^2 + \sum_{i = \lambda + 1}^n x_i^2.`
  * 1 の分割の技法を使ってリーマン計量 :math:`g` を :math:`g_{ij} = \delta_{ij}` となるように定める。
    このとき勾配ベクトルは次のようになる：

    .. math::

       \grad f = -2 \sum_{i = 1}^\lambda x_i \frac{\partial}{\partial x_i}  + 2 \sum_{i = \lambda + 1}^n x_i\frac{\partial}{\partial x_i}.

  * 解曲線は :math:`(\mathrm e^{-2t}x_1, \dotsc, \mathrm e^{-2t}x_{\lambda}, \mathrm e^{2t}x_{\lambda + 1}, \dotsc, \mathrm e^{2t}x_n).`
  * :math:`f\inv(x^0 - \eps)` と :math:`f\inv(x^0 + \eps)` の間には二枚の平面を除いて対応が付いている。

* 例 8.5.4: トーラス :math:`f(x, y) = a(2 + \cos y)\cos x + c \sin y`

  * :math:`\RR^3` 内のトーラス (p. 24) として考える。
  * :math:`\displaystyle Df = \begin{pmatrix}-a(2 + \cos y)\sin x & -a \sin y\cos x + a \cos y\end{pmatrix}.`
  * :math:`\displaystyle g = \begin{pmatrix}(2 + \cos y)^2 & 0\\0 & 1\end{pmatrix}.` (cf. 例題 7.1.4)
  * :math:`\displaystyle g\inv = \begin{pmatrix}\dfrac{1}{(2 + \cos y)^2} & 0\\0 & 1\end{pmatrix}.`

  定義に従って勾配ベクトル場を計算するのは容易い：

  .. math::

     \grad f = -\frac{a\sin x}{2 + \cos y}\frac{\partial}{\partial x} + (-a \sin y\cos x + c\cos y)\frac{\partial}{\partial y}.

8.6 ファイバー束（展開）
----------------------------------------------------------------------
* 例題 8.6.1: ファイブレーション定理

  * :math:`M, N` をコンパクト連結多様体で :math:`\dim M > \dim N` であり、
  * :math:`F \in C^\infty(M, N)` が
  * :math:`\forall x \in M, F_*: T_xM \longto T_{F(x)}N` が全射である

  とする。このとき :math:`\forall y \in N` に次のような近傍 :math:`V_y \owns y` と
  同相写像 :math:`h` が存在する：

  * :math:`h: F\inv(V_y) \longto V_y \times F\inv(y),`
  * :math:`F = \operatorname{pr}_1 \circ h,`
  * :math:`\operatorname{pr_1}` は第一成分への射影。

  証明：

  * リーマン計量を :math:`g` とする。
  * 接空間の部分集合 :math:`\nu_x = \set{v \in T_x(M) \sth \forall w \in T_x(F\inv(F(x))), g(v, w) = 0}` を定義する。

    * :math:`F_*|\nu_x` が同型写像になるという性質がある。

  * ある一点 :math:`y^0 \in N` の開被覆として :math:`(V, \psi = (y_1, \dotsc, y_n)),\ \psi(y^0) = (0, \dotsc, 0)` をとる。
  * 近傍 :math:`W \owns y^0` を :math:`\closure{W} \subset V` となるようにとる。
  * :math:`C^\infty` 級関数 :math:`\mu: N \longto \RR` を次のように定義する：

    * :math:`\supp \mu = V,`
    * :math:`y \in \closure{W} \implies \mu(y) = 1.`

  * :math:`N` 上の :math:`C^\infty` 級ベクトル場 :math:`\xi_i = \mu\dfrac{\partial}{\partial y_i}` を考える。
  * また :math:`\bm a \in \RR^n` として
    :math:`\xi_{\bm a} = \sum_{i = 1}^n a_i\xi_i` およびそれが生成するフロー
    :math:`\Psi_{\bm a}^t` を考える。

    これはある :math:`\eps > 0` について次のような性質がある：

    .. math::

       t\norm{\bm a} < \eps \implies \Psi_{\bm a}^t(y^0) = \psi\inv(t\bm a).

  * :math:`F_*|\nu_x` は同型なので :math:`\xi_i` に対して
    :math:`M` 上のベクトル場 :math:`\overset{\sim}{\xi_i}` を次が成り立つように一意的に取れる：

    .. math::

       F_* \overset{\sim}{\xi_i} = \xi_i,
       \
       \overset{\sim}{\xi_i}(x) \in \nu_x.

    * この状況をファイバー束の接続という。
    * :math:`\overset{\sim}{\xi_i}` を :math:`\xi_i` の
      `持ち上げ <http://mathworld.wolfram.com/Lift.html>`__ という。

  * :math:`\displaystyle \overset{\sim}{\xi}_{\bm a} = \sum_{i = 1}^n a_i \overset{\sim}{\xi_i}` とおくと
    :math:`F_* \overset{\sim}{\xi}_{\bm a} = \overset{\sim}{\xi}_{\bm a}.`

    ゆえに 6.6.5 のベクトル場の射影の性質により、
    :math:`\overset{\sim}{\xi}_{\bm a}` のフロー :math:`\Phi_{\bm a}^t` について次が成り立つ：

    .. math::

       F \circ \Phi_{\bm a}^t = \Psi_{\bm a}^t \circ F.

  * 写像 :math:`H: \set{\bm a \in \RR^n \sth \norm{\bm a} < \eps} \times F\inv(y^0) \longto M` を
    :math:`H(\bm a, x) = \Phi_{\bm a}^1(x)` で定義する。

    * 注意 6.3.6 より :math:`H` は :math:`C^\infty` 級である。
    * :math:`F(H(\bm a, x)) = \Psi_{\bm a}^1(F(x)) = \Psi_{\bm a}^1(y^0) = \psi\inv(a).`
    * :math:`H` の逆写像は :math:`x \longmapsto (\psi(F(x)), \Phi_{\psi(F(x))}(x))` で与えられる。

    よって写像 :math:`H` は微分同相写像である。

`ファイバー束 <http://mathworld.wolfram.com/FiberBundle.html>`__
  位相空間 :math:`E, B` と連続写像 :math:`p: E \longto B` について
  次が成り立つ位相空間 :math:`F` が存在すれば、これを `ファイバー <http://mathworld.wolfram.com/Fiber.html>`__ といい、
  :math:`p` をファイバー束という：

  .. math::

     \forall b \in B, \exists U_b \owns b \quad \text{ s.t. }
     \exists h: p\inv(U_b) \longto U_b \times F,\
     \operatorname{pr}_1 \circ h = p.

平坦な接続
  例題 8.6.1 における :math:`[\overset{\sim}{\xi}, \overset{\sim}{\eta}]` を考える。

  * 持ち上げによってベクトル場 :math:`[\overset{\sim}{\xi}, \overset{\sim}{\eta}]` は
    :math:`F_*[\overset{\sim}{\xi}, \overset{\sim}{\eta}] = [F_*\overset{\sim}{\xi}, F_*\overset{\sim}{\eta}] = [\xi, \eta].`

    * 最初と最後の等号はそれぞれ例題 8.2.3 と持ち上げによる。

  * 特に座標近傍上で :math:`\displaystyle \xi = \zeta_i = \frac{\partial}{\partial x_i}` をとれば、
    :math:`[\zeta_i, \zeta_j] = 0` なので
    :math:`[\overset{\sim}{\zeta_i}, \overset{\sim}{\zeta_j}]` は
    ファイバーの方向のベクトル場である。

  * さらに :math:`\forall \zeta_i, \zeta_j,\ [\overset{\sim}{\zeta_i}, \overset{\sim}{\zeta_j}] = 0`
    のときには接続が平坦な接続であるという。

    * 各 :math:`\zeta_i` が生成するフローを :math:`\varphi_i^{t_i}` とすると、各フローは局所的には可換である。
    * :math:`x \in M` と 0 近傍の点 :math:`(t_1, \dotsc, t_n)` に対し、
      :math:`\Phi(t_1, \dotsc, t_n)(x) = \varphi_1^{t_1} \circ \dotsb \circ \varphi_n^{t_n}(x)` とおく。

      #. :math:`\psi(F(\Phi(t_1, \dotsc, t_n)))(x) = \psi(F(x)) + (t_1, \dotsc, t_n),`
      #. :math:`\Phi(s_1, \dotsc, s_n) \circ \Phi(t_1, \dotsc, t_n)(x) = \Phi(s_1 + t_1, \dotsc, s_n + t_n)(x).`

    * 微分同相写像 :math:`x \longmapsto (F(x), \Phi(\psi(y) - \psi(F(x)))(x))` に関する
      :math:`U_y \times \set{z}` の逆像は部分多様体のように貼り合わされる。

* ファイバーがリー群であるようなファイバー束を考えることができる。

  * :math:`G` がファイバーを左または右から :math:`M` に作用している。
  * この作用について不変なファイバーに対して横断的な接平面場を考えると、
    持ち上げが :math:`G` の作用で不変となるような接続がある。
    このとき :math:`[\overset{\sim}{\xi}, \overset{\sim}{\eta}]` も不変ベクトル場であり、
    :math:`G` のリー代数 :math:`\mathfrak g` の元である。

* n 次元リーマン多様体の :math:`\operatorname{Fr}M` はファイバーが :math:`O(n)` であるような
  :math:`M` 上のファイバー束となっている。
* `レビチビタ接続 <http://mathworld.wolfram.com/Levi-CivitaConnection.html>`__ とはこのファイバー束の接続である。

8.7 第 8 章の問題の回答
----------------------------------------------------------------------
ノートは以上に記した。
