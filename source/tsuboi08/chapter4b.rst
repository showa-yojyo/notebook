======================================================================
第 4 章 微分形式とベクトル場 2/4
======================================================================

.. contents:: ノート目次

4.2 リー群
======================================================================
:ref:`幾何学 I 問題 4.4.3 <tsuboi05.4.4.3>` も参照。

4.2.1 不変微分形式
----------------------------------------------------------------------
当分の間 :math:`G` を多様体次元が :math:`n` であるリー群とする。

* 自身への微分同相写像 :math:`\fnm{L_g}{G}{G}{h}gh` は :math:`g \in G` による左移動であるいう。
* 同様に :math:`\fnm{L_g}{G}{G}{h}hg` を右移動という。
* 左不変ベクトル場

  :ref:`幾何学 I 問題 8.2.6 <tsuboi05.8.2.6>` の復習。

  1. :math:`h \in G` に対して、
     ベクトル場 :math:`\fn{\xi}{T_1G}{T_hG}{v}{(L_h)}_*v` を考える。

  2. :math:`\forall g \in G,\ {(L_g)}_*\xi = \xi` という性質を左不変であるという。
  3. 左不変ベクトル場の全体を :math:`\mathfrak{g}` と書く。

     * これを :math:`G` の `リー環 or リー代数 <http://mathworld.wolfram.com/LieAlgebra.html>`__ という。
     * ベクトル空間として :math:`\mathfrak{g} \cong T_1G.`

  4. :math:`\forall \xi, \eta \in \mathfrak{g},\ [\xi, \eta] \in \mathfrak{g}.`

* 左不変微分形式

  1. :math:`a \in \extp^p T_1^*G` に対して、微分形式
     :math:`\fn{\alpha}{G}{\extp^p T_{h\inv}^* G}{h\inv}(L_h)^*a` を考える。
  2. この対応は左不変である：
     :math:`\forall g \in G,\ (L_g)^*\alpha = \alpha.`

  左不変微分形式については記号を用意しない？

.. _tsuboi08.4.2.1:

* 問題 4.2.1: 左不変形式と左不変ベクトル場の内部積

  * :math:`\alpha \in \Omega^p(G)` を左不変形式とする。
  * :math:`\xi \in \mathfrak{g}` とする。

  このとき、内部積 :math:`i_\xi\alpha` は左不変形式である：

  .. math::

     \begin{align*}
     (L_g)^*(i_\xi\alpha)
     &= i_{{L_g\inv}_*\xi}(L_g)^*\alpha\\
     &= i_\xi\alpha.
     \end{align*}

  * 最初の等号は :ref:`問題 4.1.7 <tsuboi08.4.1.7>` (3) による。
  * 次の等号は左不変ベクトル場と左不変形式の性質を同時に適用することによる。

..

* 左不変形式の外微分もまた左不変形式である：
  :math:`(L_g)^*\dd\alpha = \dd\alpha.`

  1. :math:`\mathfrak{g} \cong T_1G` の基底を何かとって :math:`e_1, \dotsc, e_n` とする。
  2. :math:`T_1^*G` における双対基底を :math:`e_1^*, \dotsc, e_n^*` とする。
  3. :math:`\displaystyle [e_i, e_j] = \sum_{k = 1}^n c_{ij}^k e_k` とおく。
  4. :math:`\dd(e_k^*)(e_i, e_j) = -c_{ij}^k` を示す：

     .. math::

        \begin{align*}
        (\dd(e_k^*)(e_i, e_j)
        &= e_i(e_k^*(e_j))) - e_j(e_k^*(e_i))) - e_k^*([e_i, e_j])\\
        &= e_i(\delta_{kj}) - e_j(\delta_{ki}) - e_k^*([e_i, e_j])\\
        &= 0 - 0 - e_k^*([e_i, e_j])\\
        &= - c_{ij}^k.
        \end{align*}

     * 最初の等号は :ref:`問題 4.1.16 <tsuboi08.4.1.16>` による。
     * 二番目の等号は双対基底の性質による。
     * 三番目の等号は、定数の方向微分がゼロとなることによる。
     * 最後の等号は 3. および双対基底の性質による。

..

* 一般線形群の部分群の左不変ベクトル場の括弧積

  :math:`G \subset GL_N(\RR)` をリー群とする。
  このとき行列 :math:`A \in T_1G \subset T_1(GL_N(\RR)) \cong \RR^{N^2}` で
  表される左不変ベクトル場 :math:`A \in \mathfrak{g}` が :math:`G` 上に
  生成するフローは :math:`\varphi_t^A(B) = B\mathrm{e}^tA` と書かれる。

  1. そこで、ベクトル場 :math:`A` の行列 `B` における値を書き下すと次のようになる：

     .. math::

        \begin{align*}
        A|_B
        &= \left(\diff{}{t}\right)_0 B\mathrm{e}^tA\\
        &= BA \in T_BG \subset T_B(GL_N(\RR)) \cong \RR^{N^2}.
        \end{align*}

  2. 括弧積 :math:`[A_1, A_2]` の行列 `B` における値を計算する：

     .. math::

        \begin{align*}
        [A_1, A_2]|_B
        &= \left(\diff{}{t}\right)_0 (\varphi_t^{A_1})_* A_2|_{\varphi_t^{A_1}(B)}\\
        &= \left(\diff{}{t}\right)_0 (\varphi_t^{A_1})_* A_2|_{B\mathrm{e}^{tA_1}}\\
        &= \left(\diff{}{t}\right)_0 (A_2 \mathrm{e}^{-tA_1})|_{B\mathrm{e}^{tA_1}}\\
        &= \left(\diff{}{t}\right)_0 (B\mathrm{e}^{tA_1} A_2\mathrm{e}^{-tA_1}\\
        &= (BA_1 \mathrm{e}^{tA_1} A_2 \mathrm{e}^{-tA_1}
           - B\mathrm{e}^{tA_1}A_2 A_1 \mathrm{e}^{-tA_1})|_{t=0}\\
        &= BA_1 A_2 - BA_2 A_1\\
        &= B(A_1 A_2 - A_2 A_1).
        \end{align*}

     * 最初と三番目の等号は :ref:`幾何学 I 定義 8.2.1 <tsuboi05.8.2.1>` などによる。
     * 二番目の等号は先述の :math:`A` と :math:`\varphi_t^A` の関係による。
     * 四番目の等号は 1. による。
     * 以降の等号は直接計算による。

  つまり :math:`[A_1, A_2] = A_1 A_2 - A_2 A_1` が成り立っている。

.. _tsuboi08.4.2.2:

.. from sympy import Matrix
.. e_1 = Matrix([[0, 0, 0], [0, 0, 1], [0, -1, 0]])
.. e_2 = Matrix([[0, 0, -1], [0, 0, 0], [1, 0, 0]])
.. e_3 = Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]])
.. H = Matrix([[1, 0], [0, -1]])
.. S = Matrix([[0, 0], [1, 0]])
.. U = Matrix([0, 1], [0, 0]])

* 問題 4.2.2: 一般線形群の部分リー群各種

  * \(1) :math:`SO(3)` のリー代数 :math:`\mathfrak{so}(3) \cong T_1(SO(3))` は
    :math:`{}^t\!A + A = O` なる 3 次正方行列 :math:`A` の全体である。

    * 次のように基底をとるときの、各括弧積 :math:`[e_i, e_j]` は何か：

      .. math::

         e_1 =
         \begin{pmatrix}
         0 & 0 & 0\\
         0 & 0 & 1\\
         0 & -1 & 0
         \end{pmatrix},\quad
         e_2 =
         \begin{pmatrix}
         0 & 0 & -1\\
         0 & 0 & 0\\
         1 & 0 & 0
         \end{pmatrix},\quad
         e_3 =
         \begin{pmatrix}
         0 & -1 & 0\\
         1 & 0 & 0\\
         0 & 0 & 0
         \end{pmatrix}.

      * 素直に計算するしかない。TeX を書くのもキツかったので SymPy を使った：

        .. math::

           \begin{align*}
           [e_1, e_2] &= e_1 e_2 - e_2 e_1\\
           &=  \begin{pmatrix}0 & 0 & 0\\1 & 0 & 0\\0 & 0 & 0\end{pmatrix}
             - \begin{pmatrix}0 & 1 & 0\\0 & 0 & 0\\0 & 0 & 0\end{pmatrix}\\
           &= \begin{pmatrix}0 & -1 & 0\\1 & 0 & 0\\0 & 0 & 0\end{pmatrix}\\
           &= e_3,
           \\
           [e_1, e_3] &= e_1 e_3 - e_3 e_1\\
           &= \begin{pmatrix}0 & 0 & 0\\0 & 0 & 0\\-1 & 0 & 0\end{pmatrix}
             -\begin{pmatrix}0 & 0 & -1\\0 & 0 & 0\\0 & 0 & 0\end{pmatrix}\\
           &= \begin{pmatrix}0 & 0 & 1\\0 & 0 & 0\\-1 & 0 & 0\end{pmatrix}\\
           &= -e_2,
           \\
           [e_2, e_3] &= e_2 e_3 - e_3 e_2\\
           &= \begin{pmatrix}0 & 0 & 0\\0 & 0 & 0\\0 & -1 & 0\end{pmatrix}
             -\begin{pmatrix}0 & 0 & 0\\0 & 0 & -1\\0 & 0 & 0\end{pmatrix}\\
           &= \begin{pmatrix}0 & 0 & 0\\0 & 0 & 1\\0 & -1 & 0\end{pmatrix}\\
           &= e_1.
           \end{align*}

    * 左不変 1 形式の基底を上の双対基底を :math:`e_1^*, e_2^*, e_3^*` とするとき、
      各 :math:`\dd e_i^*` は何か。

      * この問題の少し前に述べられている議論をそのまま使う。
        :math:`(\dd e_k^*)(e_i, e_j)` の値をすべてチェックし、
        :math:`e_k` の係数がゼロでない括弧積をそのまま外積に置き換えるような作業で構わない。

        .. math::

           \begin{align*}
           \dd e_1^* &= -e_2^* \wedge e_3^*\\
           \dd e_2^* &=  e_1^* \wedge e_3^*\\
           \dd e_3^* &= -e_1^* \wedge e_2^*
           \end{align*}

  * \(2) :math:`SL_2(\RR)` のリー代数 :math:`\mathfrak{sl}(2) \cong T_1(SL_2(\RR))` は
    :math:`\trace{A} = 0` なる 2 次正方行列 :math:`A` の全体である。
    次のように基底をとるときの括弧積と双対基底の外微分とは何か：

    .. math::

       H = \begin{pmatrix}1 & 0\\0 & -1\end{pmatrix},\quad
       S = \begin{pmatrix}0 & 0\\1 & 0\end{pmatrix},\quad
       U = \begin{pmatrix}0 & 1\\0 & 0\end{pmatrix}.

    やり方は同じだが、本書の回答例と計算結果が食い違う。
    普通に計算すると次のようになる：

    .. math::

       \begin{align*}
       [H, S] &= HS - SH = -2S,\\
       [H, U] &= HU - UH = 2U,\\
       [S, U] &= SU - US = -H.
       \end{align*}

    だから：

    .. math::

       \begin{align*}
       \dd H^* &= S^* \wedge U^*,\\
       \dd S^* &= 2 H^* \wedge U^*,\\
       \dd U^* &= -2 H^* \wedge U^*.
       \end{align*}

    となるはずだ。

4.2.2 リー群の作用
----------------------------------------------------------------------
.. todo::

   冒頭の微分形式の平均の議論のノートを見返したら、
   リー微分の記号と左移動の記号が紛らわしくて使い物になっていない。
   もう一度読み直し。

.. _tsuboi08.4.2.3:

* 定理 4.2.3: コンパクト多様体にコンパクト連結リー群が作用していると

  * :math:`M` と :math:`G` をそれぞれコンパクト多様体とコンパクト連結リー群であるとする。
  * :math:`G` は :math:`M` に作用しているとする。

  このとき、:math:`M` のドラーム・コホモロジー群は、
  :math:`M` の :math:`G` 不変微分形式のなすコチェイン複体のドラーム・コホモロジー群である。

..

* :math:`G` の自身への作用を考えると、

  * 左不変微分形式は有限次元であり、
  * :math:`G` 不変微分形式のドラーム・コホモロジー群が有限ベクトル空間のコチェイン複体上の
    外微分の計算で求まる

  ことになる。

.. _tsuboi08.4.2.4:

* 例 4.2.4: 特殊線形群のコチェイン複体

  :ref:`問題 4.2.2 <tsuboi08.4.2.2>` (1) のコチェイン複体は次のようになる：

  .. math::

     \require{AMScd}
     \begin{CD}
     0 @>{\dd}>> \RR[1]
       @>{\dd}>> \RR[e_1^*] \oplus \RR[e_2^*] \oplus \RR[e_3^*]
       @>{\dd}>> \RR[e_2^* \wedge e_3^*] \oplus \RR[e_1^* \wedge e_3^*] \oplus \RR[e_1^* \wedge e_2^*]
       @>{\dd}>> \RR[e_1^* \wedge e_2^* \wedge e_3^*]
       @>{\dd}>> 0.
     \end{CD}

  これよりドラーム・コホモロジー群は次のようになる：

  .. math::

     \H^k(SO(3)) \cong
     \begin{cases}
     \RR &\quad\text{if }k = 0, 3\\
     0   &\quad\text{otherwise}
     \end{cases}

.. _tsuboi08.4.2.5:

* 問題 4.2.5: :math:`U(2)` の左不変微分形式のなすコチェイン複体およびドラーム・コホモロジー群

  :math:`U(2) = \set{A \in M_2(\CC) \sth AA^* = I_2}.`

  1. :math:`U(2)` のリー代数は次である：

     .. math::

        \mathfrak{u}(2) = \set{A \in M_2(\CC) \sth A + A^* = O}.`

  2. :math:`\mathfrak{u}(2)` の基底をとる。
     記号はなぜか :math:`e_1, e_2, t, e_3` とする。
     定義は本書参照。

  3. 基底の各括弧積を計算する。次のようになる：

     .. math::

        \begin{align*}
        &[t, e_1] = 0,\ [t, e_2] = 0,\ [t, e_3] = 0,\\
        &[e_1, e_2] = e_3,\ [e_1, e_3] = -e_2,\\
        &[e_2, e_3] = e_1.
        \end{align*}

  4. 左不変 1 形式の基底として、3. の双対基底 :math:`e_1^*, e_2^*, t^*, e_3^*` をとる。
  5. 左不変 1 形式の基底の外微分を求める。
     方法は :ref:`問題 4.2.2 <tsuboi08.4.2.2>` などで見たとおり：

     .. math::

        \begin{align*}
        \dd e_1^* &= -e_2^* \wedge e_3^*,\\
        \dd e_2^* &= e_1^* \wedge e_3^*,\\
        \dd e_3^* &= -e_1^* \wedge e_2^*,\\
        \dd t^* &= 0,
        \end{align*}

  6. コチェイン複体を 5. より書き下す。面倒なので書かないが 1-4-6-4-1 型。
  7. ドラーム・コホモロジー群は次のようになる：

     .. math::

        \H^k(SO(3)) \cong
        \begin{cases}
        \RR &\quad\text{if }k = 0, 1, 3, 4\\
        0   &\quad\text{otherwise}
        \end{cases}

     :math:`\dd(e_1^* \wedge t^*) = (\dd e_1^*) \wedge \dd t^*` に注意が要る。

  別解としてリー群の同型 :math:`U(2) \cong SU(2) \times U(1)` と
  :math:`S^3 \times S^1` に :ref:`定理 2.9.1 キネットの公式 <tsuboi08.2.9.1>`
  を用いる方法もあるとのこと。
  上述の :math:`e_1, e_2, e_3` と :math:`t` という名前は
  :math:`SU(2)` と :math:`U(1)` への同型を意識していたのだ。

4.2.3 :math:`U(1)` の自由作用
----------------------------------------------------------------------
* 最も簡単なコンパクトリー群は

  .. math::

     U(1) = \set{\mathrm{e}^{\sqrt{-1}\theta} \sth \theta \in \RR}

  である。

* 多様体 :math:`M` に :math:`U(1)` が作用していて、つまり：

  * :math:`R_{\theta_1} R_{\theta_2} x = R_{\theta_1 + \theta_2}x`
  * :math:`R_0 x = x`

  であって、かつそれが `自由に作用 <http://mathworld.wolfram.com/FreeAction.html>`__、
  つまり：

  * :math:`R_\theta x = x` なる :math:`x \in M` に対して、
    :math:`\mathrm{e}^{\sqrt{-1}\theta} = 1` であることが同値である

  とする。

* :math:`M` 上の同値関係を次のように導入する：

  .. math::

     x \sim y \iff \exists \theta \in \RR \quad\text{s.t. }R_\theta x = y.

* :math:`M/U(1) = M/\sim` と書くことにすると、
  この空間は :math:`\dim M  - 1` 次元多様体であり、射影 :math:`\fn{p}{M}{M/U(1)}` は
  `沈み込み <http://mathworld.wolfram.com/Submersion.html>`__ となる。

* :math:`U(1)` 作用はベクトル場 :math:`\displaystyle X_x = \left(\diff{}{\theta}\right)_{\theta = 0} R_\theta x`
  で生成されていて、作用が自由であればこのベクトル場はゼロではない。

.. _tsuboi08.4.2.6:

* 問題 4.2.6: :math:`U(1)` の自由作用

  * ベクトル場 :math:`X` が :math:`M` 上の :math:`U(1)` の自由作用を生成していて、
  * :math:`\beta \in \Omega^k(M)` が :math:`i_X\beta = L_X\beta = 0` を満たして

  いるとする。このとき次が成り立つ：

  * :math:`\exists \underline\beta \in \Omega^k(M/U(1)) \quad\text{s.t. } p^*\underline\beta = \beta.`
  * :math:`\beta \in Z^k(M) \implies \underline\beta \in Z^k(M/U(1)).`

  沈み込みの活用がわからない。:math:`\ker p^*` が :math:`X` のスカラー倍とは？

  1. 点 :math:`y \in M/U(1)` をとる。
     それに対応する :math:`p(x) = y` を満たす :math:`x \in M` をとる。

     * 射影 :math:`p` は全射である。

  2. 接ベクトルの対応を一つ決める。
     ここでは :math:`i = 1, \dotsc, k = \dim M` に対して、
     :math:`Y_i \in T_y(M/U(1))` と
     :math:`p_* \widetilde Y_i = Y_i` を満たす :math:`\widetilde Y_i \in T_xM` が対応するとする。

  3. ここで別の :math:`\widetilde Y'_i \in T_xM` が存在して :math:`p_* \widetilde Y'_i = Y_i`
     が成り立つと仮定する。すると：

     .. math::

        \begin{align*}
        p_* \widetilde Y'_i = p_* \widetilde Y_i
        & \iff p_*(\widetilde Y'_i - \widetilde Y_i)\\
        & \iff \widetilde Y'_i - \widetilde Y_i \in \ker p_*.
        \end{align*}

     すなわち :math:`\widetilde Y'_i - \widetilde Y_i = aX \in T_xM`
     が成り立つようなスカラー :math:`a \in \RR` が存在する。

  4. :math:`i_X\beta = 0` より
     :math:`\beta(\widetilde Y_1, \dotsc, \widetilde Y_k) = \beta(\widetilde Y'_1, \dotsc, \widetilde Y'_k)` が言える。

  5. :math:`\forall \theta \in \RR,\quad p \circ R_\theta = p` であるから
     :math:`p_* \circ {R_\theta}_* = p_*.`

  6. :math:`L_X\beta = 0` より
     :math:`\forall \theta \in \RR,\quad R_\theta^*\beta = \beta.`

  7. :math:`x \sim x'` なる :math:`x' \in M` をとり、
     :math:`\theta \in \RR` を :math:`x = R_\theta x'` を満たすものに固定する。

  8. :math:`p_*\widetilde Y'_i = Y_i` を満たす :math:`\widetilde Y'_i \in T_{x'}M` がとれれば
     次が成り立つ：

     .. math::

        \begin{align*}
        \beta(\widetilde Y'_1, \dotsc, \widetilde Y'_k)
        &= R_\theta^*\beta(\widetilde Y'_1, \dotsc, \widetilde Y'_k)\\
        &= \beta({R_\theta}_*\widetilde Y'_1, \dotsc, \widetilde {R_\theta}_*Y'_k)\\
        &= \beta(\widetilde Y_1, \dotsc, \widetilde Y_k).
        \end{align*}

     * 最初の等号は 6. による。
     * 次の等号は？
     * 最後の等号は 3. と 5. より :math:`p_* \widetilde Y'_i = p_* \circ {R_\theta}_* \widetilde Y'_i = Y_i`
       であることによる。

  9. よって :math:`\underline\beta(Y_1, \dotsc, Y_k) = \beta(\widetilde Y_1, \dotsc, \widetilde Y_k)`
     は一意的な定義になっている。

  10. 一意的であることが言えたので、:math:`\beta \in Z^k(M)` であれば
      :math:`0 = \dd \beta = p^*\dd \underline\beta` から :math:`\dd \underline\beta = 0`
      と結論できる。
