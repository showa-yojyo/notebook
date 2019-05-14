======================================================================
第 2 章 多様体上の微分形式 (3/3)
======================================================================

.. contents:: ノート目次

2.9 直積のドラーム・コホモロジー（展開）
======================================================================
* :math:`T^2 = S^1 \times S^1` について
  :math:`\H^2(T^2) \cong \RR,\ \H^1(T^2) \cong \RR^2,\ \H^0(T^2) \cong \RR` であった。
  :ref:`例題 2.4.8 <tsuboi08.2.4.8>` 参照。

  * 1 をとる定数関数のコホモロジー類が :math:`\H^0(T^2)` の、
  * :math:`\dd x_1, \dd x_2 \in Z^1(T^2)` のコホモロジー類が :math:`\H^1(T^2)` の、
  * :math:`\dd x_1 \wedge \dd x_2 \in Z^2(T^2)` のコホモロジー類が :math:`\H^2(T^2)` の

  基底になることがわかる。

* 二つの多様体 :math:`M, N` の直積に対する射影 :math:`\pi_M, \pi_N` を考えると、

  * :math:`\alpha \in Z^p(M)`,
  * :math:`\beta \in Z^q(N)`

  に対して :math:`\pi_M^*\alpha \wedge \pi_N^*\beta \in Z^{p + q}(M \times N)` が得られる。

  * これを :math:`T^2` で考えると :math:`S^1` から導かれたこういう閉形式らがコホモロジー類を生成することがわかる。

* 二つの有限次元ベクトル空間 :math:`V, W` の
  `テンソル積 <http://mathworld.wolfram.com/VectorSpaceTensorProduct.html>`__
  :math:`V \otimes W` の定義そして説明。

* :math:`\H^*(M), \H^*(N)` のテンソル積は :math:`\H^*(M) \otimes \H^*(N)` の次数 p の部分を
  次の式で定義することで定まる：

  .. math::

     \bigoplus_{i = 0}^p \H^i(M) \otimes \H^{p - i}(N).

* このとき :math:`[\alpha] \otimes [\beta] \in \H^p(M) \otimes \H^q(N)` が定まって、
  :math:`[\pi_M^*\alpha \wedge \pi_N^*\beta] \in H^{p + q}(M \times N)` も定まる。
  そして準同型 :math:`\H^p(M) \otimes \H^q(N) \longto H^{p + q}(M \times N)` もこの対応で定まる。

.. _tsuboi08.2.9.1:

* 定理 2.9.1: `キネットの公式 <https://en.wikipedia.org/wiki/K%C3%BCnneth_theorem>`__

  * コンパクト多様体 :math:`M, N` について :math:`\H^*(M \times N) \cong \H^*(M) \otimes \H^*(N).`
  * :math:`\alpha \in \Z^p(M),\ \beta \in \Z^q(N)` に対して
    :math:`[\alpha] \otimes [\beta] \in \H^p(M) \otimes \H^q(N)` は
    :math:`[\pi_M^*\alpha \wedge \pi_N^*\beta]` に対応する。

  証明：

  * 多様体が球面 :math:`S^k` のときの証明

    帰納法による。

    * :math:`k = 0` のときの証明

      * :math:`\varOmega^*(S^0 \times N) \cong \varOmega^*(N) \oplus \varOmega^*(N)`: この理由は？
      * :math:`\H^0(S^0) \otimes \H^p(N) \cong \H^p(N) \oplus \H^p(N)`: 前ページ定義より。

      以上より OK となる。

    * :math:`P(k - 1) \implies P(k)` の証明

      * まず主張 `P(k - 1)` が真であると仮定する。
      * いつものように分解する：
        :math:`S^k = M_1 \cup M_2,\ M_{12} = M_1 \cap M_2 \cong S^{k - 1} \times \RR`

      * :math:`M_1, M_2` のマイヤー・ビエトリス完全系列に :math:`\otimes \H^*(N)` した完全系列を考える。

        * これが完全系列となる根拠は後述の :ref:`補題 2.9.3 <tsuboi08.2.9.3>` による。

        * ただし :math:`M_1, M_2` をそれぞれのコホモロジー群が等しい一点にそれぞれ置き換え、
          :math:`M_{12}` を :math:`S^{k - 1}` に置き換える。

      * さらに :math:`S^k \times N = (M_1 \times N) \cup (M_2 \times N)` についての
        マイヤー・ビエトリス完全系列を考える。ただし以下の置き換えをする：

        * :math:`M_1 \times N,\ M_2 \times N` をそれぞれコホモロジー群が等しい :math:`N` に、
        * :math:`M_{12} \times N` を :math:`S^{k - 1} \times N` に。

      * この二つの完全系列を並列させて、準同型の矢印で接続する：

        .. math::

           \require{AMScd}
           \begin{CD}
           @. @. @.\\
           @VVV @VVV\\
           \H^{p-1}(N) \oplus \H^{p-1}(N) @>{(A)}>> \H^{p-1}(N) \oplus \H^{p-1}(N)\\
           @VV{(i_1^* - i_2^*) \otimes \id^*}V @VV{i_1^* - i_2^*}V\\
           \bigoplus_{i = 0}^p\H^i(S^{k - 1}) \otimes \H^{p-1-i}(N) @>{(B)}>> \H^{p-1}(S^{k - 1} \times N)\\
           @VV{\Delta^* \otimes \id^*}V @VV{\Delta^*}V\\
           \bigoplus_{i = 0}^p\H^i(S^k) \otimes \H^{p-i}(N) @>{(C)}>> \H^p(S^{k - 1} \times N)\\
           @VV{(j_1^*, j_2^*) \times \id^*}V @VV{(j_1^*, j_2^*)}V\\
           \H^p(N) \oplus \H^p(N) @>{(A)}>> \H^p(N) \oplus \H^p(N)\\
           @VV{(i_1^* - i_2^*) \otimes \id^*}V @VV{i_1^* - i_2^*}V\\
           \bigoplus_{i = 0}^p\H^i(S^k) \otimes \H^{p-i}(N) @>{(B)}>> \H^p(S^{k - 1} \times N)\\
           @VVV @VVV\\
           \end{CD}

      * 横向きの準同型写像はコホモロジー群のテンソル積から
        直積のコホモロジー群に定義されたもので可換となる。

      * \(A) は帰納法によりどちらも同型写像。
      * \(B) はどちらも恒等写像なので同型写像。
      * \(C) は後述する :ref:`補題 2.9.2 <tsuboi08.2.9.2>` により同型写像。

    以上で球面の場合は終了。

  * 多様体が一般のコンパクト多様体のときの証明

    * 多様体の開被覆に対していつものように分解を構成する

    * :math:`P(k - 1) \implies P(k)` の証明

      先ほどと同様に完全系列を二つ並べて考える：

      * 左列は :math:`M_j = M_{j - 1} \cup B_j` についてのマイヤー・ビエトリス完全系列に :math:`\otimes \H^*(N)` した完全系列。

        * :math:`B_j` をコホモロジー群が等しい 1 点で置き換え。
        * :math:`M_{j - 1} \cap B_j` を :math:`S^{m_j}` に置き換え。

      * 右列は :math:`M_j \times N = (M_{j - 1} \times N) \cup (B_j \times N)` についてのマイヤー・ビエトリス完全系列。

      .. math::

         \begin{CD}
         @. @. @.\\
         @VVV @VVV\\
         \bigoplus_{i = 0}^{p - 1}\H^i(M_{j - 1}) \otimes \H^{p-1-i}(N) \oplus \H^{p-1}@>{(A)}>> \H^{p-1}(M_{j - 1} \times N) \oplus \H^{p-1}(B_j \times N)\\
         @VVV @VVV\\
         \bigoplus_{i = 0}^{p-1}\H^i(S^{m_j}) \otimes \H^{p-1-i}(N) @>{(B)}>> \H^{p-1}((M_{j - 1} \cap B_j) \times N)\\
         @VVV @VVV\\
         \bigoplus_{i = 0}^p\H^i(M_j) \otimes \H^{p-i}(N) @>{(C)}>> \H^p(M_j \times N)\\
         @VVV @VVV\\
         \bigoplus_{i = 0}^p\H^i(M_{j - 1}) \otimes \H^{p-i}(N) \oplus \H^p(N) @>{(A)}>> \H^p(M_{j - 1} \times N) \oplus \H^p(B_j \times N)\\
         @VVV @VVV\\
         \bigoplus_{i = 0}^p\H^i(S^{m_j}) \otimes \H^{p-i}(N) @>{(B)}>> \H^p((M_{j - 1} \cap B_j) \times N)\\
         @VVV @VVV\\
         \end{CD}

      * \(A) は帰納法の仮定によりどちらも同型写像。
      * \(B) は球面の場合によりどちらも同型写像。
      * \(C) は後述する :ref:`補題 2.9.2 <tsuboi08.2.9.2>` により同型写像。

    以上で一般の場合は終了。

  以上により主張の同型は示された。

.. _tsuboi08.2.9.2:

* 補題 2.9.2: `Five Lemma <http://mathworld.wolfram.com/FiveLemma.html>`__

  ベクトル空間と線形写像の二つの完全系列と、その間にある準同型との間にある
  可換図式に関する補題。

  .. math::

     \begin{CD}
     A_1 @>{f_1}>> A_2 @>{f_2}>> A_3 @>{f_3}>> A_4 @>{f_4}>> A_5\\
     @V{F_1}VV @V{F_2}VV @V{F_3}VV @V{F_4}VV @V{F_5}VV\\
     B_1 @>{g_1}>> B_2 @>{g_2}>> B_3 @>{g_3}>> B_4 @>{g_4}>> B_5
     \end{CD}

  この図式で、

  * 上下の行が完全系列であり、
  * :math:`F_1, F_2, F_4, F_5` が同型写像であり、
  * :math:`F_3` が準同型写像（ふつうの線形写像）である

  とする。このとき :math:`F_3` は同型写像である。

  1. :math:`F_3` が単射であることを示す。

     * :math:`x \in \ker{F_3}` を一つとる。
     * :math:`F_4 \circ f_3(x) = g_3 \circ F_3(x) = 0` および
       :math:`F_4` が同型写像であることから :math:`f_3(x) = 0.`
       したがって :math:`\exists x_2 \in A_2 \text{ s.t. } f_2(x_2) = x.`

     * :math:`g_2 \circ F_2(x_2) = F_3 \circ f_2(x_2) = 0` および
       :math:`F_2` が同型写像であることから
       :math:`\exists y_1 \in B_1 \text{ s.t. } g_1(y_1) = F_2(x_2).`

     * :math:`F_1` が同型写像であることから
       :math:`\exists x_1 \in A_1 \text{ s.t. } F_1(x_1) = y_1.`

     * :math:`F_2 \circ f_1(x_1) = g_1 \circ F_1(x_1)` および
       :math:`F_2` が同型写像であることから
       :math:`f_1(x_1) = x_2.`

     * :math:`\im{f_1} = \ker{f_2}` に注意して :math:`x = f_2 \circ f_1(x_1) = 0.`

     :math:`\ker{F_3} = \zeroset` つまり :math:`F_3` は単射である。

  2. :math:`F_3` が全射であることを示す。

     * :math:`y \in B_3` を一つとる。
     * :math:`F_4` が同型写像であることから
       :math:`\exists x_4 \in A_4 \text{ s.t. } F_4(x_4) = g_3(y).`
     * :math:`F_5 \circ f_4(x_4) = g_4 \circ F_4(x_4) = g_4 \circ g_3(y) = 0`
       および `F_5` が同型写像であることから
       :math:`f_4(x_4) = 0.`
     * 一行目が完全系列であることから
       :math:`\exists x_3 \in A_3 \text{ s.t. } f_3(x_3) = x_4.`
     * :math:`g_3 \circ F_3(x_3) = F_4 \circ f_3(x_3) = g_3(y)` だから
       :math:`y - F_3(x_3) \in \ker{g_3}.`

     * :math:`\exists y_2 \in B_2 \text{ s.t. } g_2(y_2) = y - F_3(x_3).`
     * :math:`F_2` が同型写像であることから
       :math:`\exists x_2 \in A_2 \text{ s.t. } F_2(x_2) = y_2.`

     このとき次が成り立つので :math:`F_3` は全射である。

     .. math::

        \begin{align*}
        F_3(f_2(x_2) + x_3)
        &= g_2 \circ F_2(x_2) + F_3(x_3)\\
        &= g_2(y_2) + + F_3(x_3)\\
        &= y.
        \end{align*}

  3. 以上 1. と 2. により :math:`F_3` は同型写像である。

.. _tsuboi08.2.9.3:

* 補題 2.9.3: テンソル積の完全性

  .. math::

     \begin{CD}
     @. \cdots @>>> A_0 @>>> A_1 @>>> A_2 @>>> \cdots
     \end{CD}

  が完全系列であれば、ベクトル空間 :math:`B` に対して引き起こされる写像についての

  .. math::

     \begin{CD}
     @. \cdots @>>> A_0 \otimes B @>>> A_1 \otimes B @>>> A_2 \otimes B @>>> \cdots
     \end{CD}

  もまた完全系列である。

  1. まず与えられた完全系列上の線形写像を :math:`\fn{f_i}{A_i}A_{i + 1}` とおく。
     示すべきは :math:`(f_1 \otimes \id_B) \circ (f_0 \otimes \id_B) = 0` である。

  2. :math:`0 \ne \bm y \in A_1 \otimes B` をとり :math:`f_1(\bm y) = 0`
     すなわち :math:`(f_1 \otimes \id_B)(\bm y) = 0` を仮定する。

     ここで、線形独立な :math:`\bm b_1, \dotsc \bm b_m \in B` および
     :math:`\bm y_1, \dotsc, \bm y_n \in A_1` により次の和で表すものとする：

     .. math::

        \bm y = \sum{i = 1}^n\sum{j = 1}^m \bm y_i \otimes \bm b_j.

  3. 上記の 1. と 2. を合わせると次のように書ける：

     .. math::

        0 = (f_1 \otimes \id_B)(\bm y) = \sum{i = 1}^n\sum{j = 1}^m f_1(\bm y_i) \otimes \bm b_j.

     この式より :math:`\forall i \in \set{0, \dotsc, n}, f_1(\bm y_i) = 0`
     が必要であることがわかる。

  4. さらに与えられた完全系列から
     :math:`\forall i \in \set{0, \dotsc, n}, \exists \bm x_i \in A_0 \text{ s.t. } f_0(\bm x_i) = \bm y_i.`

  5. 以上をまとめて：

     .. math::

        \begin{align*}
        \bm y
        &= \sum{i = 1}^n\sum{j = 1}^m \bm y_i \otimes \bm b_j\\
        &= \sum{i = 1}^n\sum{j = 1}^m f_0(\bm x_i) \otimes \bm b_j\\
        &= (f_0 \otimes \id_)\left(\sum{i = 1}^n\sum{j = 1}^m \bm x_i \otimes \bm b_j \right).
        \end{align*}

     これと 3. を合成すれば所望の結論が示される。

  参考：
  https://math.stackexchange.com/questions/1899546/tensor-product-of-an-exact-sequence-of-vector-spaces-by-a-vector-space

.. _tsuboi08.2.9.4:

* 問題 2.9.4: :math:`\H^*(T^n) = \bigotimes^n \H^*(S^1)`

  * :math:`\H^p(T^n)` の元はすべてが :math:`\sum a_{i_1 \dots i_p} \dd x_{i_1} \wedge \dotsb \wedge \dd x_{i_p}`
    のような形をしている。ここで各 :math:`a_{i_1 \dots i_p} \in \RR.`

  * 証明は帰納法による。

    * :math:`n = 1` ならば :math:`\H^*(T^1) = \bigotimes^n \H^*(S^1) = H^*(S^1) \times H^*(S^1).`
      まともに展開すれば納得できる。

    * :math:`n - 1` のときに主張が正しいと仮定する。
      つまり :math:`\H^*(T^{n - 1}) = \bigotimes^{n - 1}\H^*(S^1)` とする。
      このとき、:ref:`キネットの公式 <tsuboi08.2.9.1>` により

      .. math::

         \H^*(T^n) = \H^*(S^1) \otimes \bigotimes^{n - 1} \H^*(S^1).

      * 各 :math:`\H^*(S^1)` の生成元を :math:`\dd x_k` とすると、
        :math:`\H^p(T^n)` の基底は :math:`\dd x_{i_1} \wedge \dotsb \wedge \dd x_{i_p}` となる。
        つまり :math:`\H^p(T^n)` の元はこれらの線形結合の形をとる。

.. _tsuboi08.2.9.5:

* 定義 2.9.5: `カップ積 <http://mathworld.wolfram.com/CupProduct.html>`__

  :math:`\H^*(M \times M) \cong \H^*(M) \otimes \H^*(M)` について対角写像
  :math:`\fn{\diag}{M}M \times M` に対する :math:`\diag^*` と同型写像を結合した写像
  :math:`\H^*(M) \otimes \H^*(M) \longto \H^*(M)` が定義される。

  この :math:`\diag^*` が各 :math:`p, q` に対して定める双線型写像
  :math:`\fn{\cup}{\H^p(M) \times \H^q(M)}\H^{p + q}(M)` をカップ積という。

.. _tsuboi08.2.9.6:

* 定理 2.9.6: :math:`[\cdot]` のカップ積は :math:`[\cdot] \wedge [\cdot]` と一致する。

  :math:`M` の閉形式 :math:`\alpha, \beta` について :math:`[\alpha] \cup [\beta] = [\alpha \wedge \beta]`

  * 証明。射影をそれぞれ :math:`\pi_1, \pi_2` とする。

    .. math::

       \begin{align*}
       \diag^*(\pi_1^* \alpha \wedge \pi_2^* \beta)
       &= \diag^*\pi_1^* \alpha \wedge \diag^*\pi_2^* \beta\\
       &= (\pi_1 \circ \diag)^* \alpha \wedge (\pi_2 \circ \diag)^* \beta\\
       &= \id^* \alpha \wedge \id^* \beta\\
       &= \alpha \wedge \beta.
       \end{align*}

    :math:`\therefore [\alpha] \cup [\beta] = [\alpha \wedge \beta].`

.. _tsuboi08.2.10:

2.10 チェック・ドラーム複体（展開）
======================================================================
* コンパクト多様体の開被覆を工夫して、ドラーム・コホモロジー群が有限次元であることを示す。
  以下、

  * :math:`M` をコンパクト多様体、
  * :math:`\set{U_i}_{i = 1 \dots N}` をその開被覆、
  * :math:`U_{i_0 \dots i_k} = U_{i_0} \cap \dotsb \cap U_{i_k}\quad(1 \le i_0 < \dotsb < i_k \le N` とおく。
    ここで各 :math:`U_{i_0 \dots i_k}` は :math:`\RR^n` と微分同相であるか、空集合であるとする。

..

.. math::

   \begin{CD}
   @. @. @.\\
   @. @AA{\dd}A @AA{\dd}A @AA{\dd}A @AA{\dd}A\\
   0 @>{r}>> \varOmega^3(M) @>{\delta}>> \bigoplus_i \varOmega^3(U_i) @>{\delta}>> \bigoplus_{i_0 < i_1} \varOmega^3(U_{i_0 i_1}) @>{\delta}>> \bigoplus_{i_0 < i_1 < i_2} \varOmega^3(U_{i_0 i_1 i_2}) @>{\delta}>>\\
   @. @AA{\dd}A @AA{\dd}A @AA{\dd}A @AA{\dd}A\\
   0 @>{r}>> \varOmega^2(M) @>{\delta}>> \bigoplus_i \varOmega^2(U_i) @>{\delta}>> \bigoplus_{i_0 < i_1} \varOmega^2(U_{i_0 i_1}) @>{\delta}>> \bigoplus_{i_0 < i_1 < i_2} \varOmega^2(U_{i_0 i_1 i_2}) @>{\delta}>>\\
   @. @AA{\dd}A @AA{\dd}A @AA{\dd}A @AA{\dd}A\\
   0 @>{r}>> \varOmega^1(M) @>{\delta}>> \bigoplus_i \varOmega^1(U_i) @>{\delta}>> \bigoplus_{i_0 < i_1} \varOmega^1(U_{i_0 i_1}) @>{\delta}>> \bigoplus_{i_0 < i_1 < i_2} \varOmega^1(U_{i_0 i_1 i_2}) @>{\delta}>>\\
   @. @AA{\dd}A @AA{\dd}A @AA{\dd}A @AA{\dd}A\\
   0 @>{r}>> \varOmega^0(M) @>{\delta}>> \bigoplus_i \varOmega^0(U_i) @>{\delta}>> \bigoplus_{i_0 < i_1} \varOmega^0(U_{i_0 i_1}) @>{\delta}>> \bigoplus_{i_0 < i_1 < i_2} \varOmega^0(U_{i_0 i_1 i_2}) @>{\delta}>>\\
   @. @. @AA{\iota}A @AA{\iota}A @AA{\iota}A\\
   @. @. \bigoplus_i \RR(U_i) @>{\delta}>> \bigoplus_{i_0 < i_1} \RR(U_{i_0 i_1}) @>{\delta}>> \bigoplus_{i_0 < i_1 < i_2} \RR(U_{i_0 i_1 i_2}) @>{\delta}>>\\
   @. @. @AAA @AAA @AAA\\
   @. @. 0 @. 0 @. 0
   \end{CD}

* \p. 77 の可換図式の見方。

  * 縦向きの系列

    * 当然 :math:`\dd` は外微分を意味する。
    * 一番下の列 :math:`\displaystyle \bigoplus_{i_0 < \dotsb < i_k}\RR(U_{i_0 \dots i_k})` は
      :math:`\set{U_{i_0 \dots i_k}}_{i_0 < \dotsb < i_k}` を基底とするベクトル空間として見る。
    * 写像 :math:`\fn{\iota}{\RR(U_{i_0 \dots i_k})}\varOmega^0(U_{i_0 \dots i_k})` は定数関数の埋め込みである。

      * :math:`\varOmega^0` の行は各開集合上における関数全体であることに注意したい。
        定数関数はその部分と捉えられる。

    以上のような条件と :ref:`定理 1.7.2 <tsuboi08.1.7.2>` により、これは完全系列である。
    ポアンカレの補題が要。

  * 横向きの系列

    * 写像 :math:`\fn{r_i}{\varOmega^p(M)}\varOmega^p{U_i}` を制限とすることで :math:`r = \bigoplus r_i.`
    * 添字 :math:`i_0 < \dotsb < i_k` とこの中の :math:`i_s` について
      写像 :math:`\varOmega^p(U_{i_0 \dots i_{s-1} i_{s+1} \dots i_k}) \longto \varOmega^p(U_{i_0 \dots i_k})` は制限
      :math:`r_{i_0 \dots i_k}^{i_0 \dots i_{s-1} i_{s+1} \dots i_k}` の :math:`(-1)^s` 倍である。
    * :math:`\displaystyle \delta = \bigoplus \sum (-1)^s r_{i_0 \dots i_k}^{i_0 \dots i_{s-1} i_{s+1} \dots i_k}`
      と定義する。

    もう一つ見るべきことがあり、それが次の補題だ。

.. _tsuboi08.2.10.1:

* 補題 2.10.1: :math:`0 \longto \varOmega^p(M) \longto \cdots` の行は完全系列

  * 関数 :math:`\displaystyle f^{(k)} \in \bigoplus_{i_0 < \dotsb < i_k} \varOmega^p(U_{i_0 \dots i_k}) \cong \varOmega^p\left(\bigsqcup_{i_0 < \dotsb < i_k} U_{i_0 \dots i_k} \right)`
    の :math:`\varOmega^p(U_{i_0 \dots i_k})` の成分を :math:`f^{(k)}|U_{i_0 \dots i_k}` または
    :math:`f^{(k)}_{i_0 \dots i_k}` の使いやすい方で表すことにする。

  * :math:`\delta` の定義により：

    .. math::

       (\delta f^{(k)})|U_{i_0 \dots i_k i_{k + 1}}
       = \sum_{j = 0}^{k + 1} (-1)^j f^{(k)}_{i_0 \dots i_{j-1} i_{j+1} \dots i_k}|U_{i_0 \dots i_k i_{k + 1}}

  * :math:`(\delta(\delta(f^{(k)}))|U_{i_0 \dots i_{k + 2}} = \cdots = 0.`
    つまり :math:`\delta \circ \delta = 0.`

  * :math:`\displaystyle f^{(k + 1)} \in \bigoplus_{i_0 < \dotsb < i_{k + 1}} \varOmega^p(U_{i_0 \dots i_{k + 1}}) \cong \varOmega^p\left(\bigsqcup_{i_0 < \dotsb < i_k} U_{i_0 \dots i_k} \right)`
    に対して

    .. math::

       Sf^{(k + 1)} \in \bigoplus_{i_0 < \dotsb < i_k} \varOmega^p(U_{i_0 \dots i_k}) \cong \varOmega^p\left(\bigsqcup_{i_0 < \dotsb < i_k} U_{i_0 \dots i_k} \right)

    を次の式で定義する：

    .. math::

       (Sf^{(k + 1)})|U_{i_0 \dots i_k} = \sum_m \lambda_m f^{(k + 1)}_{m i_0 \dots i_k}.

    ここで :math:`\lambda_i` は :math:`U_i` に従属する 1 の分割とし、

    .. math::

       f^{(k + 1)}_{m i_0 \dots i_k} =
       \begin{cases}
       0 & \quad \text{if } m \in \set{i_0, \dotsc, i_k},\\
       (-1)^j f^{(k + 1)}_{i_0 \dots i_{j - 1} m i_j \dots i_k} & \quad \text{otherwise}
       \end{cases}

    とし、:math:`\lambda_m f_{m i_0 \dots i_k} \in \varOmega^p(U_{i_0 \dots i_k})` とみなす。

  * :math:`\delta(Sf^{(k)}) + S(\delta f^{(k)}) = f^{(k)}` を示して、
    :math:`\delta f^{(k)} = 0 \implies f^{(k)} = \delta(Sf^{(k)})` となり、
    横向きの系列は完全系列であることがわかる。

    * :math:`\im \delta` が次の :math:`\ker \delta` と一致すると言っている。

..

* \p. 77 の図の一番下の行をチェック複体という。
  そのコホモロジー群を `チェック・コホモロジー群 <http://mathworld.wolfram.com/CechCohomology.html>`__ という。
  記号 :math:`\check{H}^p(M, \set{U_i})` で表す。

  .. math::

     \begin{CD}
     0 @>{\delta}>> \bigoplus_i \RR(U_i)
       @>{\delta}>> \bigoplus_{i_0 < i_1} \RR(U_{i_0 i_1})
       @>{\delta}>> \bigoplus_{i_0 < i_1 < i_2} \RR(U_{i_0 i_1 i_2})
       @>{\delta}>> \cdots
     \end{CD}

.. _tsuboi08.2.10.2:

* 定理 2.10.2: チェック・ドラームの定理 :math:`\H^p(M) \cong \check H^p(M, \set{U_i})`

  証明が長いし、
  `コサイクル <http://mathworld.wolfram.com/Cocycle.html>`__ だの
  `コバウンダリー <http://mathworld.wolfram.com/Coboundary.html>`__ だの見慣れぬ用語があるのが気になる。
  以下、適宜書き直す：

  1. :math:`\forall \alpha \in Z^p(M)` に何らかの :math:`\alpha^{(p, -1)} \in \check{Z}^p(M, \set{U_i})`
     が対応することを示す。

     本書にイラストが添えられているが、併せて p. 77 の図式も参照すること。

     * :math:`\forall \alpha \in Z^p(M), \dd{r\alpha} = r\dd\alpha = 0.`
       したがって :math:`\exists \alpha^{(0, p - 1)} \in \bigoplus_i \varOmega^{p - 1}(U_i) \text{ s.t. } r\alpha = \dd\alpha^{(0, p - 1)}.`

       * :math:`r` は制限写像 :math:`\fn{r_i}{\varOmega^p(M)}\varOmega^p(U_i)` の直和である。
       * そもそも縦列は :ref:`定理 1.7.2 <tsuboi08.1.7.2>` により完全系列である。

     * :math:`\dd{\delta\alpha^{(0, p - 1)}} = \delta\dd\alpha^{(0, p - 1)} = \delta r\alpha = 0.`

     * 帰納的に

       .. math::

          \alpha^{(j - 1, p - j)} \in \bigoplus_{i_0 < \dotsb < i_{j - 1}}\varOmega^{p - j}(U_{i_0\dots i_{j - 1}}),
          \dd{\delta \alpha^{(j - 1, p - j)}} = 0

       を仮定すれば、

       .. math::

          \exists \alpha^{(j, p - j - 1)} \in \bigoplus_{i_0 < \dotsb < i_j}\varOmega^{p - j - 1}(U_{i_0\dots i_j})
          \text{ s.t. }
          \delta \alpha^{(j - 1, p - j)} = \dd{\alpha^{(j, p - j - 1)}}.

       * 境界準同型の性質 :math:`\delta\delta\alpha^{(j - 1, p - j)} = 0` に注意。

     * 帰納法によって

       .. math::

          \exists \alpha^{(p - 1, 0)} \in \bigoplus_{i_0 < \dotsb < i_{p - 1}}\varOmega^0(U_{i_0\dots i_{p - 1}}),
          \exists \alpha^{(p, -1)} \in \bigoplus_{i_0 < \dotsb < i_p} \RR(U_{i_0 \dots i_p})
          \text{ s.t. }
          \delta\alpha^{(p - 1, 0)} = \iota\alpha^{(p - 1, 0)}.

       ここで

       .. math::

          \begin{align*}
          \iota\delta\alpha^{(p - 1, 0)}
          &= \delta\iota\alpha^{(p - 1, 0)}\\
          &= \delta\delta\alpha^{(p - 1, 0)}\\
          &= 0.
          \end{align*}

       :math:`\iota` が単射であることから :math:`\delta\alpha^{(p - 1, 0)} = 0.`

     よって
     :math:`\alpha \in \varOmega^p(M)` に対して、対応する
     :math:`\alpha^{(p, -1)} \in \bigoplus_{i_0 < \dotsb i_p} \RR(U_{i_0 \dots i_p})` が何か存在する。

   2. この対応がコホモロジー群の準同型を導き、well-defined であることを示す。
      これにより準同型 :math:`\H^p(M) \longto \check H^p(M, \set{U_i})` が定まる。

      今度は完全形式 :math:`\alpha \in \varOmega^p(M)` から出発して最下段へ向かう。

      * :math:`\forall \alpha \in B^p(M), \exists \beta \in \varOmega^{p - 1}(M) \text{ s.t. } \alpha = \dd\beta.`
      * この :math:`\alpha` に対して 1. の :math:`\alpha^{(0, p - 1)}` を考える。

        :math:`\dd{\alpha^{(0, p - 1)}} = r\alpha = r\dd\beta = \dd r\beta` ゆえ、

        .. math::

           \exists \beta^{(0, p - 2)} \in \bigoplus_{i} \varOmega^{p - 2}(U_i)
           \text{ s.t. }
           \dd\beta^{(0, p - 2)} = \alpha^{(0, p - 1)} - r\beta.

      * ここで次が成り立つ：

        .. math::

           \dd\delta\beta^{(0, p - 2)} = \delta\dd\beta^{(0, p - 2)}
           = \delta(\alpha^{(0, p - 1)} - r\beta)
           = \delta\alpha^{(0, p - 1)}.

      * 帰納的に

        .. math::

           \beta^{(j - 1, p - j - 1)} \in \bigoplus_{i_0 < \dotsb i_{j - 1}}\varOmega^{p - j - 1}(U_{i_0\dots i_{j - 1}})

        に対して次を仮定する：

        .. math::

           \dd\delta\beta^{(j - 1, p - j - 1)}
           = \delta\alpha^{(j - 1, p - j)}
           = \dd\alpha^{(j, p - j - 1)}.

        このとき：

        .. math::

           \exists \beta^{(j, p - j - 2)} \in \bigoplus_{i_0 < \dotsb i_{j - 2}}\varOmega^{p - j - 2}(U_{i_0\dots i_{j - 2}})
           \text { s.t. }
           \dd\beta^{(j, p - j - 2)} = \alpha^{(j, p - j - 1)} - \delta\beta^{(j - 1, p - j - 1)}.

        * ここで次に注意する：

          .. math::

             \begin{align*}
             \dd\delta\beta^{(j, p - j - 2)}
             &= \delta\dd\beta^{(j, p - j - 2)}\\
             &= \delta(\alpha^{(j, p - j - 1)} - \delta\beta^{(j - 1, p - j - 1)})\\
             &= \delta\alpha^{(j, p - j - 1)}.
             \end{align*}

      * 帰納法によって次が得られる：

        .. math::

           \beta^{(p - 2, 0)} \in \bigoplus_{i_0 < \dotsb i_{p - 2}}\varOmega^0(U_{i_0\dots i_{p - 2}}).

        これに対して次を仮定する：

        .. math::

           \dd\delta\beta^{(p - 2, 0)}
           = \delta\alpha^{(p - 2, 1)}
           = \dd\alpha^{(p - 1, 0)}.

        すると次が得られる：

        .. math::

           \exists \beta^{(p - 1, -1)} \in \bigoplus_{i_0 < \dotsb < i_{p - 1}}\RR(U_{i_0\dots i_{p - 1}})
           \text{ s.t. }
           \iota\beta^{(p - 1, -1)} = \alpha{(p - 1, 0)} - \delta\beta^{(p - 2, 0)}.

        * 次の評価および :math:`\iota` が単射であることから
          :math:`\alpha^{(p, -1)} = \delta\beta^{(p - 1, -1)}:`

          .. math::

             \begin{align*}
             \iota\delta\beta^{(p - 1, -1)}
             &= \delta\iota\beta^{(p - 1, -1)}\\
             &= \delta(\alpha{(p - 1, 0)} - \delta\beta^{(p - 2, 0)}\\
             &= \delta\alpha{(p - 1, 0)}\\
             &= \iota\alpha{(p, -1)}.
             \end{align*}

        * 「完全形式の差の自由度」は途中の :math:`\beta^{(j, p - j - 2)}` に表されている。

     以上で準同型 :math:`\H^p(M) \longto \check H^p(M, \set{U_i})` が得られたことになる。

  3. 縦と横の役割を入れ替えて議論すると、
     準同型 :math:`\check H^p(M, \set{U_i}) \longto \H^p(M)` が構成できて、
     かつ 1. の :math:`\alpha` から :math:`\alpha^{(p, - 1)}` への対応と、
     入れ替え版の :math:`\alpha^{(p, - 1)}` から :math:`\alpha` への対応が
     互いに逆写像である。つまり表題の同型が存在する。

.. _tsuboi08.2.10.3:

* 例 2.10.3: :math:`S^2` に内接する正四面体 :math:`v_1 v_2 v_3 v_4` の面上投影

  * 球面三角形 :math:`v_2 v_3 v_4` の補集合（開集合とする）を :math:`U_1` とする。
    その他の球面三角形についても同様にして開集合を対応させておく。

  * だいたいの :math:`U_{12}, U_{13}`, etc. は開球 :math:`B^2` と微分同相であるが、
    :math:`U_{1234}` のみ空集合となる。

  以上より、チェック・ドラームの定理が適用できることがわかる。

  * :math:`\varOmega^*(S^2)` については :ref:`命題 2.7.3 <tsuboi08.2.7.3>` で見たように次が成り立つ：

    .. math::

       \H^p(S^2) \cong
       \begin{cases}
       \RR & \quad\text{if } p = 0, 2\\
       0   & \quad\text{otherwise}
       \end{cases}

  * チェック複体は :math:`0 \longto \RR^4 \longto \RR^6 \longto \RR^4 \longto 0` となる。

    * 4 や 6 は組み合わせから来ているわけだが、なおのこと両端のゼロに注意。

  * 関数 :math:`\chi_{i_0 \dots i_p}` を :math:`U_{i_0 \dots i_p}` 上で 1 をとるものとする。

    * さらに次の二つを計算する：

      .. math::

         \begin{align*}
         &\delta\left(\sum_{i = 1}^4 a_i\chi_i\right)
         = \sum_{i_0 < i_1} (a_{i_0} - a_{i_1})\chi_{i_0 i_1}\\
         &\delta\left(\sum_{i_0 < i_1} b_{i_0 i_1}\right)
         = \sum_{i_0 < i_1 < i_2}(b_{i_1 i_2} - b_{i_0 i_2} + b_{i_0 i_1})\chi_{i_0 i_1 i_2}
         \end{align*}

      本書では（紙幅の都合で？）行列の形にしてある。
      基底 :math:`\chi_1, \dotsc, \chi_4, \chi_{12}, \dotsc, \chi_{34}, \chi_{123}, \dotsc, \chi_{234}`
      に対して：

      .. math::

         \begin{pmatrix}
         -1 & 1 & 0 & 0\\
         -1 & 0 & 1 & 0\\
         -1 & 0 & 0 & 1\\
         0 & -1 & 1 & 0\\
         0 & -1 & 0 & 1\\
         0 & 0 & -1 & 0
         \end{pmatrix},
         \begin{pmatrix}
         1 & -1 & 0 & 1 & 0 & 0\\
         1 & 0 & -1 & 0 & 1 & 0\\
         0 & 1 & -1 & 0 & 0 & 1\\
         0 & 0 & 0 & 1 & -1 & 1
         \end{pmatrix}.

  * :math:`\ker`, :math:`\im` をそれぞれ計算して次が得られる：

    .. math::

       \check H^p(S^2, \set{U_i}) \cong
       \begin{cases}
       \RR & \quad\text{if } p = 0, 2\\
       0   & \quad\text{otherwise}
       \end{cases}

2.11 第 2 章の問題の解答
======================================================================
すでに書き込んだ。
