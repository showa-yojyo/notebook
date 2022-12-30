======================================================================
幾何学と不変量 読書ノート 2/10
======================================================================

.. contents:: ノート目次

第 2 章 正多面体群と方程式
======================================================================

方程式、群の準同型定理。

2.1 3 次方程式
----------------------------------------------------------------------

3 次の二面体群を利用して 3 次方程式 :math:`{x^3 + Ax^2 + Bx + C = 0}` の解の公式
を導く（係数の符号が本と異なるかも）。

* 用語：対称式、基本対称式。
* 定理 2.1: `対称式の基本定理
  <http://mathworld.wolfram.com/FundamentalTheoremofSymmetricFunctions.html>`__
* 演習 2.2: これは高校数学の教科書を参照という感じだ。

`カルダーノの公式 <http://mathworld.wolfram.com/CubicFormula.html>`__ を得る手順
の概略は次のようになる：

#. 1 の原始 3 乗根 :math:`\omega` をとる。
#. :math:`{r = \alpha + \beta + \gamma,\ s = \alpha + \omega\beta +
   \omega^2\gamma,\ \alpha + \omega^2 \beta + \omega \gamma}` とする。

   * この時点で :math:`r` はわかる。

#. 3 次の二面体群 :math:`D_3` を考察することで :math:`{p = s^3 + t^3}` と
   :math:`{q = s^3 t^3}` が回転と鏡映のどちらの変換に対しても不変であることがわ
   かる。実は :math:`p,\ q` は任意の変換について不変である。
#. ゆえに :math:`s^3, t^3` は :math:`\alpha, \beta, \gamma` の基本対称式として書
   かれる。
#. :math:`{A = 0}` ならば :math:`{r = 0}` であるので :math:`s^3, t^3` は方程式
   :math:`{x^2 + 27 Cx - 27B^3 = 0}` の根である。

2.2 群の同型と準同型
----------------------------------------------------------------------

群論の教科書を参照すればよさそうだ。

* 定義 2.7: `準同型写像 <http://mathworld.wolfram.com/GroupHomomorphism.html>`__
* 定義 2.9: 同型、同型写像。記号としては :math:`G_1 \cong G_2` を用いる。
* 定理 2.10: :math:`\ker f` と :math:`\operatorname{im} f` はそれぞれ定義域およ
  び値域の部分群となる。
* 定義 2.11: `正規部分群 <http://mathworld.wolfram.com/NormalSubgroup.html>`__
* 定理 2.12: :math:`{\ker f = \set{e}}` であることと :math:`f` が同型写像である
  ことは同値。
* 定理 2.13: :math:`{Aut(T_4) \cong \mathfrak{S}_4}`

2.3 4 次方程式
----------------------------------------------------------------------

今度は群 :math:`{Aut(T_4) \cong \mathfrak{S}_4}` を利用する。解の公式を得る手順
の概略は次のようになる：

#. 準同型 :math:`{\fn{\varphi}{\mathfrak{S}_4}\mathfrak{S}_3}` の核をどうにかして
   求める。
#. :math:`\ker \varphi` の元に従って p. 41 のように :math:`s, t, u, v` を根の結
   合とする。
#. :math:`t^2, u^2, v^2` の基本対称式が根の対称式で書かれることがわかる。
#. :math:`tuv, {t^2 + u^2 + v^2}, {t^2 u^2 + u^2 v^2 + v^2 t ^2}` も基本対称式と
   して書かれる。
#. 例によって :math:`{A = 0}` ならば :math:`{s = 0}` となって話が早い。
   :math:`t^2, u^2, v^2` は次の方程式の根となる：

   .. math:: x^3 + 8 Bx^2 + (16 B^2 - 64 D)x - 64 C^2 = 0.

* 演習 2.20: 正六面体群 :math:`C_6` の自己同型群 :math:`Aut(C_6)` から
  :math:`\mathfrak{S}_8, \mathfrak{S}_6, \mathfrak{S}_4` それぞれへの準同型を考
  える。

2.4 準同型定理
----------------------------------------------------------------------

この節では別に断らない限り :math:`{\fn{\varphi}{G_1}G_2}` を全射としている。

* 用語：逆像 or `ファイバー <http://mathworld.wolfram.com/Fiber.html>`__。ある一
  点の写像前の元全て。

一つの元 :math:`{\tau_1 \in \varphi\inv(\sigma)}` と :math:`\ker \varphi` が既に
わかっていれば、ファイバーは容易に求まる。すなわち :math:`{\varphi\inv(\sigma) =
\tau_1 \ker \varphi}` がそれだ。

そこで :math:`{N = \ker \varphi}` とおくと、:math:`\tau N` の形の集合の間に演算が
定義できる。

* 演習 2.22: :math:`{[\tau] \coloneqq \tau N}` と書く。これは群をなす。
* 定義 2.23: 商群 :math:`{G/N \coloneqq \set{[\tau] \sth \tau \in G}}`
* 定理 2.24: 準同型定理。

  .. math::
     :nowrap:

     \begin{align*}
     \forall \sigma \in G_2 = \operatorname{im}\varphi,
     \ \exists \tau \in G_1:\ \tau \ker \varphi = \varphi\inv \ker \varphi
     \end{align*}

  ということ。

任意の準同型写像の任意のファイバーの任意のニ元について、一方ともう一方の逆元を乗
じれば、それは準同型写像の核に属する。
