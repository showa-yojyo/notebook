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
    :math:`\psi \circ c_i = (\psi \circ (\varphi)^{-1}) \circ (\varphi \circ c_i)` であるので、
    chain rule によって適当な近傍において次のようになるから。
    最後の変形は :math:`i = j` でも同じであることによる。

    .. math::
       :nowrap:

       \begin{equation*}
       \begin{split}
       \frac{d (\psi \circ c_i)}{dt}(t_i) 
       & = D(\psi \circ (\varphi)^{-1})_{\varphi(x_0)} \frac{d (\varphi \circ c_i)}{dt}(t_i) \\
       & = \cdots \\
       & = \frac{d (\varphi \circ c_j)}{dt}(t_j)
       \end{split}
       \end{equation*}

  * 人のことは言えないが p. 74 の式変形は誤植か？

4.2 接ベクトル空間
----------------------------------------------------------------------
TBW

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
