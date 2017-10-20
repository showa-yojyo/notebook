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
