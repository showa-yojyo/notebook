======================================================================
第 8 章 多様体上のベクトル場（前編）
======================================================================

* 微分法を多様体上で考える。
* 多様体上の変化の対象はフローとするのが自然だ。

.. contents:: ノート目次

8.1 フローと関数
======================================================================
* フロー :math:`F_t` と :math:`C^\infty` 級関数 :math:`f` について、フローの軌道に沿う変化が考えられる。
  すなわちフローを生成するベクトル場を :math:`\displaystyle X = \diff{F_t}{t} \circ F_t\inv` とすると

  .. math::

     \diff{(f \circ F_t)(x)}{t} = (Xf)(F_t(x)).

  ベクトル場による関数の微分とは、ベクトル場が生成するフローの軌道に沿った変化率ということか。

* :math:`\fn{Xf}{M}\RR` は :math:`C^\infty` 級である。
* :math:`\fn{X}{C^\infty(M)}C^\infty(M)` は線形写像かつライプニッツ則を満たす
  (cf. :ref:`問題 5.1.6 <tsuboi05.5.1.6>`)。
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
======================================================================
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

.. _tsuboi05.8.2.3:

* 例題 8.2.3

  仮定：

  * :math:`M, N` をコンパクト多様体、
  * :math:`\fn{F}{M}N` を :math:`C^\infty` 級写像、
  * :math:`X, Y` を :math:`N` 上のベクトル場とし、
  * :math:`\overset{\sim}{X}, \overset{\sim}{Y}` を :math:`M` 上のベクトル場で次のようになっている：
    :math:`F_*\overset{\sim}{X} = X,\ F_*\overset{\sim}{Y} = Y.`

  結論：

  * :math:`F_*([\overset{\sim}{X}, \overset{\sim}{Y}]) = [X, Y].`
  * 特に :math:`\fn{F}{N}N` が微分同相ならば :math:`F_*([X, Y]) = [F_*X, F_*Y].`

  証明：

  * :ref:`例題 6.5.5 <tsuboi05.6.5.5>` の恒等式
    :math:`F \circ \overset{\sim}{\varphi_t} = \varphi_t \circ F`
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
  * 次の等号は :ref:`例題 6.5.5 <tsuboi05.6.5.5>` の恒等式による。
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

.. _tsuboi05.8.2.6:

* 問題 8.2.6: リー群

  #. 左不変ベクトル場全体 :math:`\mathfrak g` は :math:`\dim G` 次元のベクトル空間である
     （`リー環 or リー代数 <http://mathworld.wolfram.com/LieAlgebra.html>`__）。

     * :math:`X` が左不変ベクトル場であるとは :math:`\forall g \in G, (L_g)_*X = X` であることをいう。
     * :math:`L_g` の定義は :ref:`4.3.3 <tsuboi05.4.3.3>` でやった。
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

     ここで :ref:`例題 8.2.3 <tsuboi05.8.2.3>` の結果を利用している。

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

  * :ref:`問題 8.2.6 <tsuboi05.8.2.6>` の :math:`\exp` はリー群版の指数写像である。

8.3 行列群上の計量（展開）
======================================================================
:math:`G = GL_n(\RR)` 上の曲線 :math:`c(t)` の「接ベクトルの長さの自乗」を二通り与えて、
それぞれの測地線の方程式を調べる。ただしどちらの与え方も
:math:`G` の左作用が接ベクトルの長さを不変にするように定義する。

#. :math:`\trace {}^t\!(c'){}^t\!(c\inv)c\inv c'`
#. :math:`\trace c\inv c'c\inv c'`

* 単位行列 :math:`I_n` においては :math:`n^2` 次元ユークリッド空間の計量と一致する。
* この前と同じく変分法を適用して、値がゼロになる必要条件をそれぞれ調べる。

それぞれの測地線の方程式は次のようになる：

#. :math:`-c\inv c'' + {}^t\!(c\inv c')(c\inv c') + (c\inv c')^2 - (c\inv c')\ {}^t\!(c\inv c') = 0`
#. :math:`-(c\inv c')' = 0`

* 例題 8.3.1: 最初の :math:`c(t) = \mathrm e^{tA}` が測地線である条件

  * 測地線の式の左辺を展開すると :math:`{}^t\!AA - A\,^t\!A` となるが、
    これがゼロであるということは :math:`A \in O(n)` を意味する。

* 行列群上の計量は非リーマンであるのがよい。
  そうすると曲線の長さが正にも負にもなるかもしれず、そうなると局所性最短性はどこかへ行ってしまう。
  ただし、長さは「臨界的である」ことで定義される。

* 指数写像とは、リーマン多様体上の測地線の方程式により定義される写像だ。
