======================================================================
幾何学と不変量 読書ノート 4/10
======================================================================

.. contents:: ノート目次

第 4 章 平面の合同変換と不変式
======================================================================

4.1 等長変換
----------------------------------------------------------------------

* 定義 4.1: `等長変換 <http://mathworld.wolfram.com/Isometry.html>`__

  * :math:`{\norm{f(\bm{p}) - f(\bm{q})} = \norm{\bm{p} - \bm{q}}}`
  * 平行移動、回転、鏡映。

* 注意 4.2: 本書で変換と言う場合は全単射であるとする。
* 例 4.3: 平行移動。複素数で表現すると :math:`{z \longmapsto z + v}` という写像
  だ。
* 例 4.4: 回転。原点中心の場合と任意の点の周りの回転は次のような写像だ。

  .. math::
     :nowrap:

     \begin{align*}
     f(z) &= \mathrm e^{i\varphi} z\\
     \\
     f(z) &= \mathrm e^{i\varphi} (z - a) + a\\
          &= \mathrm e^{i\varphi} z + a(1 - \mathrm e^{i\varphi}).
     \end{align*}

* 演習 4.5: 単に :math:`{a = \alpha + i \beta}` とすればよさそうだ。
* 例 4.6: 鏡映。実軸に対して対称の場合と任意の直線 :math:`{l = \set{\mathrm{
  e}^{i\theta} + u \sth t \in \RR}}` に関して対称の場合。

  .. math::
     :nowrap:

     \begin{align*}
     f(z) &= \overline{z}\\
     f(z) &= g\inv (\overline{g(z)}),\text{ where }g(z) = \mathrm e^{-i\theta}(z - u).
     \end{align*}

* 演習 4.7: 滑り鏡映 :math:`{f(z) = \overline{z} + \alpha\quad (\alpha \in \RR)}`
* 定理 4.8: :math:`\CC` 上の等長変換は :math:`{f(z) = uz + v}` の形に限られる。こ
  こで、:math:`u` は絶対値が 1 であるとする。
* 補題 4.9: :math:`\CC` 上で三角形を固定する等長変換は恒等写像だ。

4.2 合同変換群の不変式
----------------------------------------------------------------------

* 定義 4.10: 合同変換群 or 運動群

  * こういう変換全体は写像の合成を演算として群をなす。これを合同変換群 or 運動群
    と呼ぶ。
  * 合同変換群は次章で扱うアフィン変換群の部分群である。
  * 合同変換群 :math:`E_2` は直交群 :math:`O_2(\RR)` と平行移動のなす部分群
    :math:`\RR^2` によって生成されている。

    * 平行移動のなす部分群 :math:`\RR^2` は合同変換群 :math:`E_2` の正規部分群
      だ。
    * :math:`{E_2 = O_2(\RR) \ltimes \RR^2}` は半直積群だ。

* :math:`E_2` の不変式全体は :math:`{V = (\RR^2)^m}` として :math:`{\mathfrak{I}
  = \set{F \in \CC[V] \sth F(g(\bm{p_1}, \dotsc, \bm{p_m}) = F(\bm{p_1}, \dotsc,
  \bm{p_m})\quad (\forall g \in E_2)}}` という不変式環をなす。

.. _nishiyama12.4.11:

* 定理 4.11: :math:`\mathfrak{I}` は :math:`{\set{(\bm{p_i} - \bm{p_j}) \cdot
  (\bm{p_k} - \bm{p_l})}}` で生成される。

  * 証明を見ると、まず一つの成分をゼロにする平行移動を利用して直交群の作用の不変
    式環を求める問題に帰着させる。
  * 回転行列 :math:`u_\theta` と鏡映行列 :math:`s` による不変な多項式を考える。

    .. math::
       :nowrap:

       \begin{align*}
       u_\theta = \left(
         \begin{array}{ c r }
         \cos \theta & -\sin \theta\\
         \sin \theta &  \cos \theta\\
         \end{array} \right),\quad

       s = \left(
         \begin{array}{ c r }
          1&  0\\
          0& -1
         \end{array} \right).
       \end{align*}

  * 複素数を導入して :math:`z_j, \overline{z_j}` の多項式で :math:`u_\theta` 不
    変なものが :math:`z_j \overline{z_k}` で生成されることを示す。
  * :math:`s` 不変なものは :math:`{z_j \overline{z_k} \pm \overline{z_j} z_k}`
    による展開を考える。
  * 不変式環の説明がよくわからない。距離の平方と内積とで生成される？

* 定理 4.12: :ref:`定理 4.11 <nishiyama12.4.11>` の :math:`n` 次元版。

4.3 ニ次曲線
----------------------------------------------------------------------

* 二次曲線を :math:`{F(x, y) = ax^2 + 2bxy + cy^2 + 2dx + 2ey + f = 0}` とする。
* アフィン変換群を次のように記す：

  .. math::
     :nowrap:

     \begin{align*}
     E_2 = \Set{
     \begin{pmatrix}
          h & v \\
          0 & 1
       \end{pmatrix}
     \Sth
     h \in O_2(\RR), v \in \RR^2
     }
     = \begin{pmatrix}
         O_2(\RR) & \RR^2\\
         0 & 1
       \end{pmatrix}.
     \end{align*}

  こうすると曲線を次のように記せる：

  .. math::
     :nowrap:

     \begin{align*}
     F(x, y) = {}^t\!vAv,\quad
     A = \begin{pmatrix}
       a & b & d \\
       b & c & e \\
       d & e & f
     \end{pmatrix},\quad
     v = \begin{pmatrix}
       x \\
       y \\
       1
     \end{pmatrix}.
     \end{align*}

  * ここで用いられている技法は、CG プログラミングのそれと同じではないか。なるほ
    ど。

* 対称行列全体を :math:`Sym_3(\RR)` で表す（これを二次曲線全体とみなしてよい）。
* 定理 4.14: 作用 :math:`{E_2^\curvearrowright Sym_3(\RR): A \longmapsto
  {}^t\!g\inv Ag\inv}` の不変式環 :math:`{\CC[Sym_3(\RR)]^{E_2}}` は :math:`{a +
  c, ac - b^2, \det A}` から生成される。

  * 証明を見ると、これらが不変量であることを示し、これらの多項式もまた不変式であ
    ることを示す。
  * 次に逆を示す。線形代数の教科書参照。

  :math:`{\Delta = \det A}` とおき、これを二次曲線の判別式という。

* 演習 4.15: :math:`{\Delta = 0}` ならば曲線は空集合、一点、二本以下の直線のいず
  れかである。

以下 :math:`{\Delta \ne 0}` とする。判別式がゼロのものは「曲線でなくなる」ので、
ひとまず考察の対象から外しておく。

* 射影的不変量 :math:`P_1, P_2` を定義する。

  .. math::
     :nowrap:

     \begin{align*}
     P_1 = \frac{\trace X}{\sqrt[3]{\Delta^2}},
     P_2 = \frac{\det X}{\sqrt[3]{\Delta^2}},
     \quad\text{where }
     X = \begin{pmatrix}
       a & b\\
       c & d
     \end{pmatrix}.
     \end{align*}

  * この二つの不変量が一致する曲線同士が合同となる。逆もしかり。
  * これらの符号で曲線の分類ができる。主に :math:`P_2` を用いる。

2 次曲線の囲む面積や、ニ焦点間の距離、曲線長などは不変量を使って表現できる。

* 例 4.17: 楕円の面積や焦点間の距離を :math:`P_1, P_2` で表す。

  * 周長については楕円関数をいうものも現れる。

* 演習 4.18: `双曲線 <http://mathworld.wolfram.com/Hyperbola.html>`__
* 例 4.19: `放物線 <http://mathworld.wolfram.com/Parabola.html>`__。準線と焦点の
  距離を :math:`P_1` で表す。
* 演習 4.20: パラボラアンテナ。
* 演習 4.21: `離心率 <http://mathworld.wolfram.com/Eccentricity.html>`__ を
  :math:`P_1, P_2` で表す。極座標表示で考える。
