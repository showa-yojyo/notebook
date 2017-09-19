======================================================================
幾何学 I 多様体入門 読書ノート 4/8
======================================================================

.. include:: /_include/book-details/tsuboi05.txt

.. contents:: ノート目次

第 4 章 接空間
======================================================================

4.1 曲線の接ベクトル
----------------------------------------------------------------------
接ベクトル
  次のように同値類を構成するときに現れる曲線に関する微分のことを接ベクトルと呼ぶ。

  #. 多様体 :math:`M` とその一点 :math:`x_0 \in M` につき、
     次のような曲線族 :math:`\mathcal{C}_{x_0}` を考える。

     .. math::
        :nowrap:

        \begin{align*}
        \mathcal{C}_{x_0} := \lbrace c_i: (a_i,\ b_i) \to M \mid c_i(t_i) = x_0 \rbrace _{i \in I}
        \end{align*}

  #. 次にこの一点を含む座標近傍 :math:`(U, \varphi)` をとって、
     曲線族の曲線に次のような同値関係を入れる。

     .. math::
        :nowrap:

        \begin{align*}
        c_1 \sim c_2 \Longleftrightarrow 
        \exists t_1 \in I_{c_1},\ t_2 \in I_{c_2}: \frac{d (\varphi \circ c_1)}{dt}(t_1) = \frac{d (\varphi \circ c_2)}{dt}(t_2)
        \end{align*}

* :math:`{\displaystyle \frac{d (\varphi \circ c_1)}{dt}(t_1)}` 等は :math:`\mathbb{R}^n` のベクトルであって
  点 :math:`\varphi(x_0) \in \varphi(U)` から「生えている」ようなイメージか？

* 別の近傍 :math:`(V, \psi)` をとって
  :math:`{\displaystyle \frac{d (\psi \circ c_i)}{dt}(t_i)}` を考えると
  「:math:`{\displaystyle \frac{d (\varphi \circ c_i)}{dt}(t_i)}` が同じであることと
  :math:`{\displaystyle\frac{d (\psi \circ c_i)}{dt}(t_i)}` が同じであること」となる。

  * それはなぜか。
    :math:`\psi \circ c_i = (\psi \circ \varphi^{-1}) \circ (\varphi \circ c_i)` であるので、
    chain rule によって適当な近傍において次のようになるから。

    .. math::
       :nowrap:

       \begin{equation*}
       \begin{split}
       \frac{d (\psi \circ c_i)}{dt}(t_i)
       & = D(\psi \circ \varphi^{-1})_{\varphi(x_0)} \frac{d (\varphi \circ c_i)}{dt}(t_i) \quad \because \text{chain rule}\\
       & = D(\psi \circ \varphi^{-1})_{\varphi(x_0)} \frac{d (\varphi \circ c_j)}{dt}(t_j) \quad \because c_i \sim c_j \text{ for } (U, \varphi)\\
       & = \frac{d (\psi \circ c_j)}{dt}(t_j) \quad \because \text{chain rule}
       \end{split}
       \end{equation*}

  * 人のことは言えないが p. 74 の式変形は誤植か？

4.2 接ベクトル空間
----------------------------------------------------------------------
接空間 or 接ベクトル空間
  :math:`T_{x_0}M := \mathcal{C}_{x_0} / \sim` を接空間 or 接ベクトル空間と呼ぶ。

* 接ベクトル空間は実ベクトル空間である。
* 曲線族の曲線に :math:`\mathbb{R}^n` の接ベクトルを対応させる写像は
  全単射 :math:`\varphi_{*}: \mathcal{C}_{x_0} / \sim \to \mathbb{R}^n` を誘導する。
* 単射であることは同値類の定義から従う。
* 全射であることについて。これを示すのに面白い技法を使う。

  接ベクトル :math:`\boldsymbol{v} \in \mathbb{R}^n` に対し
  :math:`c_\varphi ^\boldsymbol{v} (t) := \varphi ^{-1}(t \boldsymbol{v} + \varphi (x_0))` というのを考える。
  ただし :math:`t \in (-\varepsilon_{\varphi}^\boldsymbol{v},\ \varepsilon_{\varphi}^\boldsymbol{v})` の範囲で
  :math:`t \boldsymbol{v} + \varphi (x_0) \in \varphi(U)` が成り立つように取る。
  こうすると次のようになるので全射であることが示せる（任意のベクトルについて曲線が作れるから）。

  .. math::
     :nowrap:

     \begin{equation*}
     \begin{split}
     \varphi_*(c_\varphi ^\boldsymbol{v})
         & = \frac{d(\varphi \circ (\varphi ^{-1} (t \boldsymbol{v} + \varphi (x_0))))}{dt}(0) \\
         & = \frac{d(t \boldsymbol{v} + \varphi (x_0))}{dt}(0) \\
         & = \boldsymbol{v}
     \end{split}
     \end{equation*}

  * この技法はまた出て来る。
  * ところで :math:`\boldsymbol{v} = 0` のときも上の議論が通じるだろうか。
    曲線を定数関数とすればいいか。

* 接ベクトル空間のベクトル空間としての構造は、点 :math:`x_0` の別の座標近傍を用いて定義しても変わらない。
  :math:`\boldsymbol{v_1}, \boldsymbol{v_2} \in \mathbb R^n,\ a_1, a_2 \in \mathbb R` とすると：

  .. math::
     :nowrap:

     \begin{equation*}
     \begin{split}
     \frac{d(\psi \circ c_\varphi^{a_1 \boldsymbol{v_1} + a_2 \boldsymbol{v_2}})}{dt}(0)
     &= D(\psi \circ \varphi^{-1})_{\varphi(x_0)} \frac{d(t(a_1 \boldsymbol{v_1} + a_2 \boldsymbol{v_2}) + \varphi(x_0))}{dt}(0)\\
     &= D(\psi \circ \varphi^{-1})_{\varphi(x_0)}(a_1 \boldsymbol{v_1} + a_2 \boldsymbol{v_2})\\
     &= a_1 D(\psi \circ \varphi^{-1})_{\varphi(x_0)} \boldsymbol{v_1} + a_2 D(\psi \circ \varphi^{-1})_{\varphi(x_0)} \boldsymbol{v_2}\\
     &= a_1 \frac{d(\psi \circ c_\varphi^{\boldsymbol{v_1}})}{dt}(0) + a_2 \frac{d(\psi \circ c_\varphi^{\boldsymbol{v_2}})}{dt}(0)
     \end{split}
     \end{equation*}

* 接ベクトル空間の基底は :math:`(c_{\varphi}^{\boldsymbol{e}_1}, \dotsc, c_{\varphi}^{\boldsymbol{e}_n})` である。

  * :math:`\varphi` に依存して決まることに気をつける。

* :math:`{ \displaystyle [c_{\varphi}^{\boldsymbol{e}_i}] := \frac{\partial}{\partial x_i}}` と記す。

  * 理由 1: 曲線は（偏）微分 or 方向微分を表しているとみなせるから。
  * 理由 2: 座標近傍を換えたときの基底変換が形式的にできるから。

    * 接ベクトルは :math:`{ \displaystyle \sum \frac{d(x_i \circ c)}{dt}(t_0) \frac{\partial}{\partial x_i} = \sum \frac{d(y_i \circ c)}{dt}(t_0) \frac{\partial}{\partial y_i} }`
    * 座標変換は :math:`\psi \circ \varphi^{-1} = (y_1(x_1, \dotsc, x_n), \dotsc, y_n(x_1, \dotsc, x_n))`
    * ヤコビ行列は :math:`{ \displaystyle \left( \frac{\partial y_i}{\partial x_j} \right) }`
    * 接ベクトルの変換は :math:`{ \displaystyle \frac{\partial}{\partial x_j}}` を
      :math:`{ \displaystyle \sum_{i = 1}^n \frac{\partial y_i}{\partial x_j} (\varphi(x_0)) \frac{\partial}{\partial y_i} }`
      で置き換える。

4.3 接写像
----------------------------------------------------------------------
TBW

4.4 部分多様体
----------------------------------------------------------------------
TBW

4.5 接束（展開）
----------------------------------------------------------------------
TBW

----

:doc:`note5` へ。
