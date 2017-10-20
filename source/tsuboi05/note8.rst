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
  すなわちフローを生成するベクトル場を :math:`\displaystyle X = \diff{F_t}{t} \circ F_t^{-1}` とすると
  :math:`\displaystyle \diff{(f \circ F_t)(x)}{dt} = (Xf)(F_t(x)).`

  * :math:`Xf` は :math:`C^\infty` 級である。

* :math:`X: C^\infty(M) \longto C^\infty(M)` は線形写像かつライプニッツ則を満たす (cf. 問題 5.1.6)。
* :math:`Xf = 0 \implies f(F_t(x)) = f(x).`

* 問題 8.1.1: :math:`\displaystyle X = \frac{\partial}{\partial x} + \alpha \frac{\partial}{\partial y},\ \alpha \in \QQ`
  は :math:`\RR^2/\ZZ^2` 上のベクトル場を与える。
  このとき :math:`f \in C^\infty(M)` が :math:`Xf = 0` であるならば :math:`f` は定数関数である。

  * まず :math:`X` のフロー :math:`\varphi_t` を :math:`\RR^2` で計算する。

    * :math:`x, y` ごとに単純に微分方程式を解くと :math:`x = t + x_0,\ y = \alpha t + y_0` のようになる。
    * :math:`\varphi_t(x0, y0) = (x_0, y_0) + (t, \alpha t)` で初期値をそのまま変数の文字に置き換えて
      :math:`\varphi_t(x, y) = (x + t, y + \alpha t)` となる。
      これは :math:`\varphi_t \circ \varphi_s = \varphi_{t + s}` を満たすのでフローになっている。

  * 次に :math:`\varphi_t(x, y) = (x + t, y + \alpha t) \pmod{\ZZ^2}` は
    :math:`\RR^2/\ZZ^2` 上のフローとなっていることを確認する。

    * :math:`\alpha` が無理数であることが効いてくるのだと思うが。

  * ここからは難しいか？

  * 軌道は :math:`\{(x + t, y + \alpha t) \in \RR^2/\ZZ^2 \mid t \in \RR\}.`

* 問題 8.1.2: コンパクト多様体上のベクトル場 :math:`X` と :math:`C^\infty` 級関数 :math:`f` について
  :math:`Xf = 0 \implies f = 0`

  * :math:`\varphi_t(x) = \mathrm{e}^t f(x).`

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
  * `ヤコビ恒等式 <http://mathworld.wolfram.com/JacobiIdentities.html>`__ が成り立つ。すなわち :math:`Z` もベクトル場とすると
    :math:`[[X, Y], Z] + [[Y, Z], X] + [[Z, X], Y] = 0.`
  * ベクトル場は関数空間から関数空間への微分作用素である。
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

     :math:`X = \sum_{i, j}^n a_{ij} x_j \frac{\partial}{\partial x_i}`,
     :math:`Y = \sum_{i, j}^n b_{ij} x_j \frac{\partial}{\partial x_i}`
     と置いてひたすら式を展開する。
     最終的に :math:`\sum` 記号が三つ並ぶ。

  #. :math:`X` が :math:`\varphi_t` を生成するとして :math:`(\varphi_{-t}Y)` を書いて、
     それに基いて :math:`[X, Y] = `\left.\diff{}{t}\right|_{t = 0}(\varphi_{-t})_*Y)` を求める。

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
  * あとなぜか :math:`\displaystyle [\overset{\sim}{X}, \overset{\sim}{Y}] = \lim_{t \to 0}\frac{1}{x}(\overset{\sim}{\varphi_{-t}}_* \overset{\sim}{Y} - \overset{\sim}{Y})`
    を利用する。

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

* 問題 8.2.5:
  :math:`[\xi, \eta] = \eta \implies (\varphi_s)_*\eta = \mathrm e^s\eta,\ \varphi_s \circ \psi_t \circ \varphi_{-s} = \psi_{\mathrm e^s t}.`

  * 証明の前半は :math:`\displaystyle \left.\diff{}{s}((\varphi_{-s})_*\eta)(x)\right|_{s = 0} = ((\varphi_{-s})_*\eta)(x)` を示す。
  * 次に :math:`\displaystyle \left.\diff{}{s}(\mathrm e^s\eta)(x)\right|_s = \mathrm e^s \eta(x)` を利用して
    :math:`s = 0` のときを確かめる。

* リー群（多様体でもある）の構造の解析にはそれに即したベクトル場を用いる。

* 問題 8.2.6: リー群

  #. 左不変ベクトル場全体 :math:`\mathfrak g` は :math:`\dim G` 次元のベクトル空間である
     （`リー環 or リー代数 <http://mathworld.wolfram.com/LieAlgebra.html>`__）。
  #. :math:`\xi, \eta` を左不変ベクトル場とすると :math:`[\xi, \eta]` もそうである。
  #. :math:`\forall g \in G, \varphi_t(g) = g\varphi_t(I).` ここで :math:`I` は単位元とする。

     * :math:`\varphi_t(I) = \exp(t\xi)` と書く。

  #. :math:`\xi \longmapsto \exp(\xi)` は :math:`\mathfrak g` のゼロ近傍から
     :math:`G` の単位元の近傍への同相写像である。

* 注意 8.2.7

  * :math:`A \in G \subset GL_n(\RR)` における接ベクトルが :math:`AX` の形をしていることが
    :math:`X` が左不変であることの条件である。

  * :math:`F_t` は :math:`\displaystyle \diff{F_t(A)}{t} = F_t(A)X` を満たすので :math:`F_t(A) = \mathrm e^{tX}.`
