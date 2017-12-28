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
  4. :math:`(\dd(e_k^*)(e_i, e_j) = -c_{ij}^k` を示す：

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

.. _tsuboi08.4.2.3:

* 定理 4.2.3: コンパクト多様体にコンパクト連結リー群が作用していると

.. _tsuboi08.4.2.4:

* 例 4.2.4: 正則行列群各種のコチェイン複体

.. _tsuboi08.4.2.5:

* 問題 4.2.5: :math:`U(2)` の左不変微分形式のなすコチェイン複体およびドラーム・コホモロジー群

4.2.3 :math:`U(1)` の自由作用
----------------------------------------------------------------------

.. _tsuboi08.4.2.6:

* 問題 4.2.6: :math:`U(1)` の自由作用


