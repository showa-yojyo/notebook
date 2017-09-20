======================================================================
幾何学と不変量 読書ノート 2/4
======================================================================

:doc:`note1` からの続き。

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
     F(x, y) = {}^tvAv,\quad
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

* 定理 4.14: 作用 :math:`E_2^\curvearrowright \operatorname{Sym}_3(\mathbb R): A \mapsto {}^tg^{-1}Ag^{-1}` の不変式環
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

第 5 章 平面上のアフィン変換とアフィン幾何
======================================================================

5.1 アフィン変換群とその応用
----------------------------------------------------------------------
前章の直交行列を一般の正則行列にしたものがアフィン変換。線形変換と平行移動の合成。

.. math::
   :nowrap:

   \begin{align*}
   A_2 = \lbrace
   \left(
     \begin{array}{ c c }
       \operatorname{GL}_2(\mathbb R) & \mathbb{R}^2\\
       0 & 1
     \end{array} \right)
   \rbrace
   \end{align*}

* 演習 5.1: アフィン変換を :math:`g \in A_2` による行列の積としてみなすと、
  平面上の三角形の像で変換が決まる。

* 定理 5.2: 作用 :math:`A_2^\curvearrowright (\mathbb R^2)^m: p \mapsto gp` の不変式環
  :math:`\mathbb C[(\mathbb R^2)^m]^{A_2}` は定数関数しかない。

* 補題 5.3, 定理 5.4: アフィン変換は平行な直線を平行な直線へ写す。

5.2 相対不変式
----------------------------------------------------------------------
* 定義 5.5: 相対不変式、指標。

  * 作用 :math:`G^\curvearrowright X` においてゼロでない :math:`f \in X` が相対不変式であるとは、
    群の任意の要素に対して、次の性質がある定数 :math:`\chi_f(g) \in \mathbb C` が存在することをいう。

    .. math::
       :nowrap:

       \begin{align*}
       f(gx) = \chi_f(g) f(x)\quad(x \in X)
       \end{align*}

    * このとき :math:`\chi_f: G \to \mathbb C` を指標という。

      * 指標は一次元表現である。
      * 例えば行列式の性質 :math:`\det(AB) = \det A \det B` は指標の性質であるといえる。

* 演習 5.6: ベクトル :math:`a, b, c \in \mathbb R^2` に対して関数
  :math:`f(a, b, c) = \det(a - c\quad b - c)` を定める。
  この関数は :math:`A_2` の不変式であり、指標 :math:`\chi_f` はアフィン変換行列の
  線形変換部分の行列式と一致する。

いちおう断ってあるが、相対不変式全体は環ではない。

* 命題 5.7: 相対不変式 :math:`\varphi(x), \psi(x)` とそれぞれに付随する指標
  :math:`\chi_\varphi, \chi_\psi` について次のことが言える：

  #. 積 :math:`\chi_\varphi \chi_\psi` も相対不変式となり、
     その指標は :math:`\chi_{\varphi \psi} = \chi_\varphi \chi_\psi`

  #. 和 :math:`\chi_\varphi + \chi_\psi` は :math:`\chi_\varphi = \chi_\psi` でなければ相対不変式ではない。

* 定理 5.8: 作用 :math:`A_2^\curvearrowright (\mathbb R^2)^m` について。

  * 相対不変式は行列式の同次積とその一次結合を取ることで全て得られる。
  * 相対不変有利式とは、商 :math:`{ \displaystyle \frac{\varphi(x)}{\psi(x)} }` のことであり、
    指標は :math:`{ \displaystyle \frac{\chi_\varphi}{\chi_\psi} }` で得られる。
    ただし :math:`\psi(x) \ne 0` のときに定義する量である。
  * 不変有利式とは :math:`\varphi(x), \psi(x)` の指標が一致している場合の相対不変有利式のことをいう。

* 例 5.9: 線分を :math:`s : t` に内分する点 :math:`x` について、
  直線外の任意の一点 :math:`z` を取ることで、不変有利式で :math:`s, t` を表せる。

  * 同一直線上の線分比はアフィン変換によって変わらない。これは大事だ。

* 例 5.10: 三角形の符号付き面積 :math:`{ \displaystyle S = \frac{1}{2} \det(p - r \quad q -r)}`

  * 二つの三角形の面積比は不変有利式になる。
  * c.f. チェバの定理、メネラウスの定理。

.. todo:: section 5.3 onwards

* アフィン合同

  * 任意の三角形はアフィン合同である。
  * 三角形の各頂点をまったく移動させないような変換は恒等写像しかない。
  * 四角形がアフィン合同⇔対角線の交点による二組の対角線の内分 or 外分比がそれぞれ一致する。

* 二次曲線のアフィン合同類

  * 楕円と単位円が合同。
    双曲線は :math:`x^2 - y^2 = 1` と合同。放物線は :math:`y = x^2` と合同。

* アフィン幾何の定理について。冒頭のチェックリストが便利。

  * アフィン幾何の定理を証明するために、対象となる図形を単純なアフィン合同図形に置き換えて、
    使い慣れた初等幾何なり解析なりの技法を採用することができると言っている。

第 6 章 実射影平面
======================================================================
無限遠点および無限遠直線の導入。

* H, H' をそれぞれ xy 平面と yz 平面を 1 ずらしたものとおく。
  写像 :math:`\pi_p(x, y) = (y/x, 1 - 1/x)` を考える。

  * 視点を原点に置くと H 上の直線は H' 上の直線に写されるが、
    H 上の直線の「極限」は H' 上の直線
    :math:`\eta = 1` 上のどこかの点となる（直線の方向が y 軸に平行でない限り）。

  * H 上で平行な二直線の「極限」は H' 上の同一点に写される。

* 射影平面 :math:`\mathbb{P}^2 (\mathbb{R})` とは、空間から原点を除いた集合上の点を、
  定数倍の同値関係で同一して得られる（無限遠点を含む）点全体のなす平面。

  * 代表元を同次座標と呼んで、射影平面の元を :math:`[x : y : z]` と記す。
  * 対応する平面上の点 :math:`(\xi, \eta)` を非同次座標と呼ぶ。

* :math:`\mathbb{P}^1 (\mathbb{R})` は :math:`S^1` の半分と同型。無限遠点一つのみ。
* :math:`\mathbb{P}^2 (\mathbb{R})` は :math:`S^2` の半分と同型。縁の円周が無限遠点。

* 平面射影幾何では、実は点と直線に関する全ての定理が、
  直線と点を入れ替えても成り立つ。

* 2 次曲線は射影平面上では円周と同じ形状になっている。

* 射影平面同士の点の写像は、単に座標成分の入れ替えとなる。
  元々は割り算なので、同次座標成分がゼロでないという縛りがあったが、
  これを気にしなくて済むようになった。

* 一般の平面から :math:`{H_3}` への射影 :math:`\pi_H` について。

  * 正則行列 A を用いて写像 :math:`\pi_A: [v] \mapsto [Av]` を定義し、
    これを射影変換と呼ぶ。
  * この写像全体のなす群を :math:`\mathit{PGL}_3(\mathbb{R})` と表す。

    * A がスカラー行列のときには :math:`\pi_A = \mathrm{id}` となって、
      :math:`\pi_A^*: \mathit{GL}_3(\mathbb{R}) \to \mathit{PGL}_3(\mathbb{R})` は同型とはならない。

* 射影平面上の任意の 2 本の直線を互いに写し合う変換が存在する。
* 二次曲線は同次式で定義式を与えておくと具合が良い。
  対称行列を用いて :math:`f(v) = {}^t\!vQv` とする。

* 実射影平面上の非退化二次曲線は単位円に写せる。
  ある行列 A があって、:math:`{}^t\!AQA` が対角行列で、
  かつ対角成分の絶対値が 1 となるようにできると言っている。

----

:doc:`note3` へ。
