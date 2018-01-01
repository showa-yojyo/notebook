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
  * 閉形式 :math:`\dd x_1, \dd x_2` のコホモロジー類が :math:`\H^1(T^2)` の、
  * 閉形式 :math:`\dd x_1 \wedge \dd x_2` のコホモロジー類が :math:`\H^0(T^2)` の

  基底になることがわかる。

* 二つの多様体 :math:`M, N` の直積に対する射影 :math:`\pi_M, \pi_N` を考えると、

  * :math:`M` の閉 p 形式 :math:`\alpha`,
  * :math:`N` の閉 q 形式 :math:`\beta`

  に対して :math:`M \times N` の閉 :math:`p + q` 形式 :math:`\pi_M^*\alpha \wedge \pi_N^*\beta` が得られる。

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
  * 閉形式 :math:`\alpha \in \Omega^p(M),\ \beta \in \Omega^q(N)` に対して
    :math:`[\alpha] \otimes [\beta] \in \H^p(M) \otimes \H^q(N)` は
    :math:`[\pi_M^*\alpha \wedge \pi_N^*\beta]` に対応する。

  証明：

  * 多様体が球面 :math:`S^k` のときの証明

    帰納法による。

    * :math:`k = 0` のときの証明

      * :math:`\Omega^*(S^0 \times N) \cong \Omega^*(N) \oplus \Omega^*(N)`: この理由は？
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

  * ベクトル空間と線形写像の二つの完全系列と、その間にある準同型との間にある
    可換図式に関する補題。リンク先参照。

  * 簡単なので証明は載っていない。読者がやる。

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

  * 簡単なので証明は載っていない。読者がやる。

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
   0 @>{r}>> \Omega^3(M) @>{\delta}>> \bigoplus_i \Omega^3(U_i) @>{\delta}>> \bigoplus_{i_0 < i_1} \Omega^3(U_{i_0 i_1}) @>{\delta}>> \bigoplus_{i_0 < i_1 < i_2} \Omega^3(U_{i_0 i_1 i_2}) @>{\delta}>>\\
   @. @AA{\dd}A @AA{\dd}A @AA{\dd}A @AA{\dd}A\\
   0 @>{r}>> \Omega^2(M) @>{\delta}>> \bigoplus_i \Omega^2(U_i) @>{\delta}>> \bigoplus_{i_0 < i_1} \Omega^2(U_{i_0 i_1}) @>{\delta}>> \bigoplus_{i_0 < i_1 < i_2} \Omega^2(U_{i_0 i_1 i_2}) @>{\delta}>>\\
   @. @AA{\dd}A @AA{\dd}A @AA{\dd}A @AA{\dd}A\\
   0 @>{r}>> \Omega^1(M) @>{\delta}>> \bigoplus_i \Omega^1(U_i) @>{\delta}>> \bigoplus_{i_0 < i_1} \Omega^1(U_{i_0 i_1}) @>{\delta}>> \bigoplus_{i_0 < i_1 < i_2} \Omega^1(U_{i_0 i_1 i_2}) @>{\delta}>>\\
   @. @AA{\dd}A @AA{\dd}A @AA{\dd}A @AA{\dd}A\\
   0 @>{r}>> \Omega^0(M) @>{\delta}>> \bigoplus_i \Omega^0(U_i) @>{\delta}>> \bigoplus_{i_0 < i_1} \Omega^0(U_{i_0 i_1}) @>{\delta}>> \bigoplus_{i_0 < i_1 < i_2} \Omega^0(U_{i_0 i_1 i_2}) @>{\delta}>>\\
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
    * 写像 :math:`\fn{\iota}{\RR(U_{i_0 \dots i_k})}\Omega^0(U_{i_0 \dots i_k})` は定数関数の埋め込みである。

      * :math`\Omega^0` の行は各開集合上における関数全体であることに注意したい。
        定数関数はその部分と捉えられる。

    以上のような条件と :ref:`定理 1.7.2 <tsuboi08.1.7.2>` により、これは完全系列である。
    ポアンカレの補題が要。

  * 横向きの系列

    * 写像 :math:`\fn{r_i}{\Omega^p(M)}\Omega^p{U_i}` を制限とすることで :math:`r = \bigoplus r_i.`
    * 添字 :math:`i_0 < \dotsb < i_k` とこの中の :math:`i_s` について
      写像 :math:`\Omega^p(U_{i_0 \dots i_{s-1} i_{s+1} \dots i_k}) \longto \Omega^p(U_{i_0 \dots i_k})` は制限
      :math:`r_{i_0 \dots i_k}^{i_0 \dots i_{s-1} i_{s+1} \dots i_k}` の :math:`(-1)^s` 倍である。
    * :math:`\displaystyle \delta = \bigoplus \sum (-1)^s r_{i_0 \dots i_k}^{i_0 \dots i_{s-1} i_{s+1} \dots i_k}`
      と定義する。

    もう一つ見るべきことがあり、それが次の補題だ。

.. _tsuboi08.2.10.1:

* 補題 2.10.1: :math:`0 \longto \Omega^p(M) \longto \cdots` の行は完全系列

  * 関数 :math:`\displaystyle f^{(k)} \in \bigoplus_{i_0 < \dotsb < i_k} \Omega^p(U_{i_0 \dots i_k}) \cong \Omega^p\left(\bigsqcup_{i_0 < \dotsb < i_k} U_{i_0 \dots i_k} \right)`
    の :math:`\Omega^p(U_{i_0 \dots i_k})` の成分を :math:`f^{(k)}|U_{i_0 \dots i_k}` または
    :math:`f^{(k)}_{i_0 \dots i_k}` の使いやすい方で表すことにする。

  * :math:`\delta` の定義により：

    .. math::

       (\delta f^{(k)})|U_{i_0 \dots i_k i_{k + 1}}
       = \sum_{j = 0}^{k + 1} (-1)^j f^{(k)}_{i_0 \dots i_{j-1} i_{j+1} \dots i_k}|U_{i_0 \dots i_k i_{k + 1}}

  * :math:`(\delta(\delta(f^{(k)}))|U_{i_0 \dots i_{k + 2}} = \cdots = 0.`
    つまり :math:`\delta \circ \delta = 0.`

  * :math:`\displaystyle f^{(k + 1)} \in \bigoplus_{i_0 < \dotsb < i_{k + 1}} \Omega^p(U_{i_0 \dots i_{k + 1}}) \cong \Omega^p\left(\bigsqcup_{i_0 < \dotsb < i_k} U_{i_0 \dots i_k} \right)`
    に対して

    .. math::

       Sf^{(k + 1)} \in \bigoplus_{i_0 < \dotsb < i_k} \Omega^p(U_{i_0 \dots i_k}) \cong \Omega^p\left(\bigsqcup_{i_0 < \dotsb < i_k} U_{i_0 \dots i_k} \right)

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

    とし、:math:`\lambda_m f_{m i_0 \dots i_k} \in \Omega^p(U_{i_0 \dots i_k})` とみなす。

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

  * Stage 1: 閉 p 形式に対して「チェック複体の p コサイクル」が対応する：

    .. math::

       \alpha \longmapsto \alpha^{(p, -1)}.
       
    これは閉形式 :math:`\alpha \in \Omega^p(M)` から出発して図式を下へ下へと辿っていく。
    帰納法で最下段に到達すると :math:`\iota \delta \alpha^{(p, -1)} = \delta\delta\alpha^{(p-1, 0)}`
    なる :math:`\alpha^{(p, -1)}` が存在することがわかる。
    そして :math:`\iota` の単射性により :math:`\delta \alpha^{(p, -1)}.`
    
    以上をまとめると、:math:`\alpha \in \Omega^p(M)` に対して
    :math:`\alpha^{(p, -1)} \in \bigoplus_{i_0 < \dotsb i_p} \RR(U_{i_0 \dots i_p})` が何か存在するということだ。

  * Stage 2: この対応がコホモロジー群の準同型を導き、well-defined である。
    これにより準同型 :math:`\H^p(M) \longto \check H^p(M, \set{U_i})` が定まる。
    
    今度は完全形式 :math:`\alpha \in \Omega^p(M)` から出発して最下段へ向かう。
    :math:`\iota\delta\beta^{(p-1, -1)} = \iota\alpha^{(p, -1)}` なる :math:`\beta^{(p-1, -1)}` が存在し、
    やはり :math:`\iota` の単射性により :math:`\alpha^{(p, -1)} = \delta \beta^{(p - 1, -1)}.`
    
    前の結果とまとめて、準同型 :math:`\H^p(M) \longto \check H^p(M, \set{U_i})` が得られたことになる。

  * Stage 3: 縦と横の役割を入れ替えて議論すると、
    準同型 :math:`\check H^p(M, \set{U_i}) \longto \H^p(M)` も導かれると言える。
    両者は互いに逆写像である。それゆえ表題の同型が結論できる。

.. _tsuboi08.2.10.3:

* 例 2.10.3: :math:`S^2` に内接する正四面体 :math:`v_1 v_2 v_3 v_4` の面上投影

  * 球面三角形 :math:`v_2 v_3 v_4` の補集合（開集合とする）を :math:`U_1` とする。
    その他の球面三角形についても同様にして開集合を対応させておく。

  * だいたいの :math:`U_{12}, U_{13}`, etc. は開球 :math:`B^2` と微分同相であるが、
    :math:`U_{1234}` のみ空集合となる。

  以上より、チェック・ドラームの定理が適用できることがわかる。

  * :math:`\Omega^*(S^2)` については :ref:`命題 2.7.3 <tsuboi08.2.7.3>` で見たように次が成り立つ：

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
