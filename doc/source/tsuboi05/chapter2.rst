======================================================================
第 2 章 ユークリッド空間内の多様体
======================================================================

主題は陰関数表示、グラフ表示、パラメーター表示の同値性。

.. contents:: ノート目次

2.1 簡単な例（基礎）
======================================================================

.. _tsuboi05.2.1.1:

* 例 2.1.1: `トーラス <http://mathworld.wolfram.com/Torus.html>`__

  * これは問題ない。
  * 陰関数表示とパラメーター表示が両方示されている。

.. _tsuboi05.2.1.2:

* 例 2.1.2: 曲線 :math:`x^3 - y^2 = 0`

  * 原点において `カスプ <http://mathworld.wolfram.com/Cusp.html>`__ となるの
    は、ここでヤコビアンの行列式がゼロになるから。こういう現象は逆写像・陰関数定
    理によって互いに関係がある。

2.1.1 曲線
----------------------------------------------------------------------

* 曲線の定義。微分係数がゼロになることを認めるとカスプを生じるかもしれない。そこ
  で後述の :ref:`定理 2.1.3<tsuboi05.2.1.3>` で述べられる性質を導入する。

.. _tsuboi05.2.1.3:

* 定理 2.1.3: 一次元多様体

  陰関数表示、グラフ表示、パラメーター表示の同値性を主張する。

  * この命題は <折れ曲がりや交差がない滑らかな曲線であるという性質を
    :math:`\RR^n` の部分集合に対して表す> ものだ。
  * この意味での曲線を一次元多様体と呼ぶ。

    * 接線が自然に定義されて、パラメーター表示でも陰関数表示でも書かれる。

      .. math::

         \set{\bm x_0 + t D\varPhi_{(t^0)} \sth t \in \RR}
         = \set{\bm x_0 + \bm v \sth DF_{(\bm x_0)}\bm v = 0, \bm v \in \RR^n}.

  * 陰関数とグラフ表示は「ある近傍」だが、パラメーター表示だけ「任意の近傍」。パ
    ラメーターの主張は曲線とパラメーターの位相が同じになると述べている。

2.1.2 （超）曲面
----------------------------------------------------------------------

.. _tsuboi05.2.1.6:

* 定理 2.1.6: 超曲面

  定理 2.1.3 の超曲面版。各表示の表現が曲線のときのものと少し違うので注意。

  * 初期版と同じく、パラメーターでの主張は開球の位相とその像との位相が同じだと述
    べている。
  * (p. 30) :math:`C \cap U` はおそらく :math:`S \cap U` の誤植。

.. _tsuboi05.2.1.7:

* 例 2.1.7: 二次曲面

  * :math:`{\bm{x^0} \in Q}` における接超平面
  * 曲面の形状分類（一葉双曲面かニ葉双曲面か）で符号数という概念が出てくる。
    行列の固有値のプラスマイナスの個数の組のことだ。
  * 線形代数の教科書の後ろの方に二次形式の説明があるので、それを参考にする。

* (p. 31) 超曲面上の曲線の一点における接ベクトルを集めたものを接超平面と呼ぶ。

  * 接ベクトルはパラメーター表示関数のヤコビアンで表現する。
  * 確認：接線、接平面を点、ヤコビアンとで集合として表現できるようにしておく。接
    平面の集合は次のようになる：

    .. math::

       \set{\bm x_0 + D\varPhi_{(t^0)} \bm v \sth \bm v \in \RR^{n - 1}}
       = \set{\bm x_0 + \bm v \sth DF_{(\bm x_0)}\bm v = 0, \bm v \in \RR^n}.

2.2 ユークリッド空間内の多様体
======================================================================

.. _tsuboi05.2.2.1:

* 定理 2.2.1: :math:`p` 次元部分多様体

  以下 :math:`{p + q = n}` とする。

  * この :math:`q` を `余次元 <http://mathworld.wolfram.com/Codimension.html>`__ という。
  * 書き切れなかったが、下に出てくる :math:`W` は何らかの `開球
    <http://mathworld.wolfram.com/OpenBall.html>`__ を意味する。

  陰関数表示

    .. math::

       \begin{align*}
       &\forall \bm x_0 \in M,\ \exists U \owns \bm x_0, \exists F \in C^\infty(U, \RR^q)\\
       \text{ s.t. }\\
       &\rank DF = q, M \cap U = \set{\bm x \in U \sth F(\bm x) = F(\bm x_0)}.
       \end{align*}

  グラフ表示

    .. math::

       \begin{align*}
       &\forall \bm x_0 \in M,\ \exists W \owns (x_{i_1}^0, \dotsc, x_{i_p}^0), \exists G \in C^\infty(W, \RR^q)\\
       \text{ s.t. }\\
       &M \cap U = \set{(x_{i_1}^0, \dotsc, x_{i_p}^0, G(x_{i_1}^0, \dotsc, x_{i_p}^0)) \sth (x_{i_1}^0, \dotsc, x_{i_p}^0) \in W}.
       \end{align*}

  パラメーター表示

    .. math::

       \begin{align*}
       &\forall \bm x_0 \in M, \forall U \owns \bm x_0,\ \exists V \subset U, \exists \varPhi \in C^\infty(W, V)\\
       \text{ s.t. }\\
       &\forall \bm u \in W, \rank D\varPhi_{(\bm u)} = p,\\
       &M \cap V = \set{\varPhi(\bm u) \sth \bm u \in W},\\
       &\varPhi \text{ is injection.}
       \end{align*}

  * グラフ表示可能ならば陰関数表示可能：

    :math:`{F: (x_1, \dotsc, x_n) \longmapsto (x_{j_1}, \dotsc, x_{j_q}) -
    G(x_{i_1}, \dotsc, x_{i_p}) \in \RR^q.}`

  * グラフ表示可能ならばパラメーター表示可能：

    :math:`{\varPhi(x_{i_1}, \dotsc, x_{i_p}) = (x_{i_1}, \dotsc, x_{i_p},
    G(x_{i_1}, \dotsc, x_{i_p})).}`

  * 陰関数表示可能ならばグラフ表示可能：

    * 陰関数定理による。

  * パラメーター表示可能ならばグラフ表示可能：

    * 逆写像定理による。
    * :math:`D\varPhi` はランクが :math:`p` である :math:`{n \times p}` 行列であ
      るが、適宜列を並び替えて :math:`{p \times p}` 行列 :math:`{\displaystyle
      \left(\frac{\partial \varphi_j}{\partial x_i}\right)}` が正則であるとす
      る。
    * :math:`{\varPhi_1(\bm u) = (\varphi_1(\bm u), \dotsc, \varphi_p(\bm u))}`
      とおくと、開球 :math:`{W_1 \subset \RR^p}` と写像 :math:`{H \in
      C^\infty(W_1, W)}` が存在して次のようになる：

        :math:`{H \circ \varPhi_1 = \id_{H(W_1)},\ \varPhi_1 \circ H =
        \id_{W_1}.}`

    * :math:`{\varPhi(H(\bm x_1)) = (\varPhi_1(H(x_1, \dotsc, x_p)),
      \varPhi_2(H(x_1, \dotsc, x_p))) = (x_1, \dotsc, x_p, (\varPhi_2 \circ
      H)(x_1, \dotsc, x_p))}`という :math:`{(W_1 \times \RR^q) \times V}` 上のグ
      ラフ表示が得られる。

* `接空間 <http://mathworld.wolfram.com/TangentSpace.html>`__ とは、ある点を通過
  する多様体上の曲線の接線の集まりだ。

  * パラメーター表示ならば :math:`{\set{\bm{x^0} + DF_{\varPhi(u^0)}\bm{v} \sth
    \bm{v} \in \RR^p}}`
  * 陰関数表示ならば :math:`{\set{\bm{x^0} + \bm{v} \sth DF_{(x^0)} \bm{v} =
    0}}`

.. _tsuboi05.2.2.2:

* 問題 2.2.2: 即答できないとダメ。線形代数の復習をしないといけない。

  * なぜ :math:`{\text{im} D\varPhi_{(u^0)} \subset \ker DF_{(x^0)}}` なのか？

    .. math::

       F(\varPhi(\bm u)) = F(\bm x_0) \implies DF_{(\varPhi_{(\bm u_0)})} D\varPhi_{(\bm u_0)} = 0

  * なぜ :math:`{\ker DF_{(x^0)}}` は :math:`p` 次元なのか？

    .. math::

       \rank D\varPhi = p,\ DF_{(\varPhi_{(\bm u_0)})} = DF_{(\bm x_0)}.

  * そしてなぜ :math:`{\text{im} D\varPhi_{(u^0)} = \ker DF_{\varPhi(x^0)}}` と
    結論できるのか？

    .. math::

       n - q = p = \dim D\varPhi.

2.3 逆写像定理、陰関数定理の意味
======================================================================

微分同相という考え方が本質的だ。

* :math:`C^r` 級微分同相写像の定義。
* 逆写像定理は微分同相となる近傍のペアがあると言っている。
* ユークリッド空間内の多様体は微分同相写像で定義される。

2.4 多様体上の関数、多様体からの写像
======================================================================

.. _tsuboi05.2.4.1:

* 例題 2.4.1: 楕円体？上のある関数を調べる。

  * <多様体上の関数の極大、極小の判定のためには、局所座標を使うのが適当である>

2.5 直線、超平面との関係
======================================================================

平行な直線の族または超平面の族を考えるのが自然である。

* （用語）横断的、接超平面 or 接空間

  * 直線は :math:`\set{\bm{x^0} + t\bm{v^0} \sth t \in \RR}` またはランクが
    :math:`n - 1` の何らかの線形写像 :math:`\fn{A}{\RR^n}\RR^{n - 1}` と何らかの
    定点 :math:`{\bm{y} \in \RR^{n - 1}}` を用いて :math:`\set{\bm{x} \in \RR^n
    \sth A\bm{x} = \bm{y}}` として書かれる。

    * 定点を変化させると平行な直線族が得られる。

  * 超平面は :math:`\set{\bm{x} \in \RR^n \sth L\bm{x} = a}` と書かれる。ただし
    :math:`\fn{L}{\RR^n}\RR` と :math:`{a \in \RR}` は何らかのゼロでない線形写像
    と、何らかの実数であるとする。

  ここまでが用語を定義するための舞台設定。

  * 超曲面 :math:`S` の局所的パラメーター表示 :math:`\fn{\varPhi}{W}\RR^n` と上
    記 :math:`A` と近傍内の点 :math:`{u^0 \in W}` とを取る。

    * :math:`{A D\varPhi_{(u^0)}}` が正則である場合、上記直線族は
      :math:`{\bm{x^0} = \varPhi(u^0)}` の近傍で超曲面 :math:`S` に突き刺さる。
      この状況を「直線族が超曲面と横断的である」という。
    * 正則でない場合は :math:`\operatorname{im}D\varPhi_{(u^0)}` のことを超曲面
      の点 :math:`\bm{x^0}` における接超平面 or 接空間と呼ぶ。

  * 一般の部分多様体の場合。上記の超曲面を :math:`p` 次元部分多様体 :math:`M` に
    置き換えて読み替える。:math:`\rank(A D\varPhi_{(u^0)})` の値が

    * :math:`p` ならば :math:`{\operatorname{im} A\varPhi}` は :math:`\RR^{n -
      1}` の多様体（の条件を一部満たす）。
    * :math:`p - 1` 以下ならば :math:`{\operatorname{im} D\varPhi_{(u^0)}}` を点
      :math:`{x^0 \in M}` における接空間と呼ぶ。直線 :math:`{A
      \inv(A(\bm{x^0}))}` が :math:`\bm{x^0}` において接する。

    あるいは、:math:`{\rank(L D\varPhi_{(u^0)})}` の値が

    * 1 ならば :math:`p - 1` 次元多様体。
    * 0 ならば :math:`L\inv(L(\bm{x^0}))` を点 :math:`{\bm{x^0} \in M}` における
      接空間と呼ぶ。

.. _tsuboi05.2.5.1:

* 問題 2.5.1: 曲面が陰関数表示で与えられているから、ヤコビアンを素直に計算する。

  * (p. 41) の 2 式より接平面の方程式はすぐに書き下せる。
  * 接平面が座標軸と平行になる条件は、その座標成分の係数イコールゼロとなる点だ。
  * 曲線の各座標平面への正射影曲線は、その座標成分をゼロと置く。

2.6 第 2 章の問題の解答
======================================================================

ノーコメント。
