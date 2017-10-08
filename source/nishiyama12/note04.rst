======================================================================
幾何学と不変量 読書ノート 4/10
======================================================================

:doc:`note03` からの続き。

.. contents:: ノート目次

第 4 章 平面の合同変換と不変式
======================================================================

4.1 等長変換
----------------------------------------------------------------------
* 定義 4.1: 等長変換

  * :math:`\lVert f(\boldsymbol{p}) - f(\boldsymbol{q}) \rVert = \lVert \boldsymbol{p} - \boldsymbol{q} \rVert`
  * 平行移動、回転、鏡映。

* 注意 4.2: 本書で変換と言う場合は全単射であるとする。

* 例 4.3: 平行移動。複素数で表現すると :math:`z \mapsto z + v` という写像だ。
* 例 4.4: 回転。原点中心の場合と任意の点の周りの回転は次のような写像だ。

  .. math::
     :nowrap:

     \begin{align*}
     f(z) &= e^{i\varphi} z\\
     \\
     f(z) &= e^{i\varphi} (z - a) + a\\
          &= e^{i\varphi} z + a(1 - e^{i\varphi})
     \end{align*}

* 演習 4.5: 単に :math:`a = \alpha + i \beta` とすればよさそうだ。

* 例 4.6: 鏡映。実軸に対して対称の場合と任意の直線
  :math:`l = \{ e^{i\theta} + u \mid t \in \mathbb R\}`
  に関して対称の場合。

  .. math::
     :nowrap:

     \begin{align*}
     f(z) &= \overline{z}\\
     f(z) &= g^{-1} (\overline{g(z)}),\text{ where }g(z) = e^{-i\theta}(z - u)
     \end{align*}

* 演習 4.7: 滑り鏡映 :math:`f(z) = \overline{z} + \alpha\quad (\alpha \in \mathbb R)`

* 定理 4.8: :math:`\mathbb C` 上の等長変換は :math:`f(z) = uz + v` の形に限られる。
  ここで、:math:`u` は絶対値が 1 であるとする。

* 補題 4.9: :math:`\mathbb C` 上で三角形を固定する等長変換は恒等写像だ。

4.2 合同変換群の不変式
----------------------------------------------------------------------
* 定義 4.10: 合同変換群 or 運動群

  * こういう変換全体は写像の合成を演算として群をなす。
    これを合同変換群 or 運動群と呼ぶ。

  * 合同変換群は次章で扱うアフィン変換群の部分群である。
  * 合同変換群 :math:`E_2` は直交群 :math:`O_2(\mathbb R)` と平行移動のなす部分群 :math:`\mathbb R^2` によって生成されている。

    * 平行移動のなす部分群 :math:`\mathbb R^2` は合同変換群 :math:`E_2` の正規部分群だ。
    * :math:`E_2 = O_2(\mathbb R) \ltimes \mathbb R^2` は半直積群だ。

* :math:`E_2` の不変式全体は :math:`V = (\mathbb R^2)^m` として
  :math:`\mathfrak{I} = \{F \in \mathbb C[V] \mid F(g(\boldsymbol{p_1}, \dotsc, \boldsymbol{p_m}) = F(\boldsymbol{p_1}, \dotsc, \boldsymbol{p_m})\quad (\forall g \in E_2)\}`
  という不変式環をなす。

* 定理 4.11: :math:`\mathfrak{I}` は :math:`\{(\boldsymbol{p_i} - \boldsymbol{p_j}) \dot (\boldsymbol{p_k} - \boldsymbol{p_l})\}` で生成される。

  * 証明を見ると、まず一つの成分をゼロにする平行移動を利用して直交群の作用の不変式環を求める問題に帰着させる。
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
         \end{array} \right)
       \end{align*}

  * 複素数を導入して :math:`z_j, \overline{z_j}` の多項式で :math:`u_\theta`
    不変なものが :math:`z_j \overline{z_k}` で生成されることを示す。
  * :math:`s` 不変なものは :math:`z_j \overline{z_k} \pm \overline{z_j} z_k` による展開を考える。

  * 不変式環の説明がよくわからない。距離の平方と内積とで生成される？

* 定理 4.12: 4.11 の n 次元版。

4.3 ニ次曲線
----------------------------------------------------------------------
* 二次曲線を :math:`F(x, y) = ax^2 + 2bxy + cy^2 + 2dx + 2ey + f = 0` とする。
* アフィン変換群を次のように記す：

  .. math::
     :nowrap:

     \begin{align*}
     E_2 = \lbrace
     g = \left(
       \begin{array}{ c c }
          h & v \\
          0 & 1
       \end{array} \right)
     \mid
     h \in O_2(\mathbb R), v \in \mathbb{R}^2\rbrace
     = \left(
       \begin{array}{ c c }
         O_2(\mathbb R) & \mathbb{R}^2\\
         0 & 1
       \end{array} \right)
     \end{align*}

  こうすると曲線を次のように記せる：

  .. math::
     :nowrap:

     \begin{align*}
     F(x, y) = {}^t\!vAv,\quad
     A = \left(
     \begin{array}{ c c c }
       a & b & d \\
       b & c & e \\
       d & e & f
     \end{array} \right),\quad
     v = \left(
       \begin{array}{ c }
       x \\
       y \\
       1
     \end{array} \right)
     \end{align*}

  * ここで用いられている技法は、CG プログラミングのそれと同じではないか。なるほど。

* 対称行列全体を :math:`\operatorname{Sym}_3(\mathbb R)` で表す（これを二次曲線全体とみなしてよい）。

* 定理 4.14: 作用 :math:`E_2^\curvearrowright \operatorname{Sym}_3(\mathbb R): A \mapsto {}^t\!g^{-1}Ag^{-1}` の不変式環
  :math:`\mathbb C[\operatorname{Sym}_3(\mathbb R)]^{E_2}` は
  :math:`a + c, ac - b^2, \det A` から生成される。

  * 証明を見ると、これらが不変量であることを示し、これらの多項式もまた不変式であることを示す。
  * 次に逆を示す。線形代数の教科書参照。
  
  :math:`\Delta = \det A` とおき、これを二次曲線の判別式という。

* 演習 4.15: :math:`\Delta = 0` ならば曲線は空集合、一点、二本以下の直線のいずれかである。

以下 :math:`\Delta \ne 0` とする。
判別式がゼロのものは「曲線でなくなる」ので、ひとまず考察の対象から外しておく。

* 射影的不変量 :math:`P_1, P_2` を定義する。

  .. math::
     :nowrap:

     \begin{align*}
     P_1 = \cfrac{\operatorname{trace} X}{\sqrt[3]{\Delta^2}},
     P_2 = \cfrac{\det X}{\sqrt[3]{\Delta^2}},
     \text{ where }
     X = \left(
     \begin{array}{c c}
       a & b\\
       c & d
     \end{array} \right).
     \end{align*}

  * この二つの不変量が一致する曲線同士が合同となる。逆もしかり。
  * これらの符号で曲線の分類ができる。主に :math:`P_2` を用いる。

2 次曲線の囲む面積や、ニ焦点間の距離、曲線長などは不変量を使って表現できる。

* 例 4.17: 楕円の面積や焦点間の距離を :math:`P_1, P_2` で表す。

  * 周長については楕円関数をいうものも現れる。

* 演習 4.18: 双曲線。
* 例 4.19: 放物線。準線と焦点の距離を :math:`P_1` で表す。
* 演習 4.20: パラボラアンテナ。
* 演習 4.21: 離心率を :math:`P_1, P_2` で表す。極表示で考える。

----

:doc:`note05` へ。
