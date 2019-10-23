======================================================================
第 3 章 微分形式の積分 3/3
======================================================================

.. contents:: ノート目次

3.5 境界を持つ多様体とストークスの定理
======================================================================
* 多様体の定義を次のように修正することで「境界を持つ」多様体を定義する：

  * 座標関数の値域を :math:`\RR^n` ではなく :math:`\RR_{\le 0} \times \RR^{n - 1}` に変更する。
  * 座標変換、多様体上の :math:`C^\infty` 級関数、多様体の間の
    :math:`C^\infty` 級写像の定義を、各関数・写像の適当な制限に変更する。

* 境界

  * 境界 :math:`\partial M \coloneqq \bigcup \varphi\inv(\zeroset \times \RR^{n - 1}) \subset M` は
    :math:`n - 1` 次元部分多様体である。

  * 境界を持つ多様体の座標近傍系 :math:`\set{(U_i, \varphi_i)}` が向き付けられているとき、
    制限写像 :math:`\varphi_i|(U_i \cap \partial M)` を :math:`\partial M` の向き付けという。

  * 座標近傍 :math:`(U_i, \varphi_i = (x_1, \dotsc, x_n))` が向き付けられているならば、
    座標近傍 :math:`(\varphi_i\inv|U(\zeroset \times \RR^{n - 1}), (x_2, \dotsc, x_n))` が
    向き付けられている。

.. _tsuboi08.3.5.1:

* 定理 3.5.1: ストークスの定理

  * :math:`M` を境界あり・コンパクト・向き付けられている多様体とする。
  * :math:`\alpha \in \varOmega^{n - 1}(M)`
  * :math:`\partial M` には :math:`M` の境界としての向き付けを与えられているとする。

  次の等式が成り立つ：

  .. math::

     \int_M\!\dd \alpha = \int_{\partial M}\!\alpha.

  証明のポイント：有限開被覆、1 の分割、直方体、
  :ref:`例題 1.6.9: 直方体版ストークスの定理 <tsuboi08.1.6.9>` を使う。
  以下、

  * 有限開被覆を :math:`\set{(U_i, \varphi_i)}_{\text{i: finite}}`,
  * それに従属する 1 の分割を :math:`\lambda_i`

  とする。

  * 各 :math:`U_i` に台を持つ :math:`\alpha_i \coloneqq \lambda_i \alpha` に対して
    :math:`\displaystyle \int_M\!\dd \alpha_i = \int_{\partial M}\!\alpha_i` を示せばよい。

  * :math:`\supp{{\varphi\inv}^*\alpha_i} \subset [a_1, b_1] \times \dotsb \times [a_n, b_n] \subset \varphi_i(U_i)`
    としてよい。この直方体は :math:`i` ごとにとる。

  * :math:`\varphi_i(U_i) \cap (\zeroset \times \RR^{n - 1})` が空集合か否かで場合分けをする。

    * 空集合の場合は両辺ともにゼロとなり等しくなる。

      * 右辺は境界上で微分形式がゼロであることから、積分もゼロ。
      * 左辺。

        .. math::

           {\varphi\inv}^*\alpha_i|[a_1, b_1] \times \dotsb \times \set{a_k, b_k} \times \dotsb \times [a_n, b_n] = 0

        であるので：

        .. math::

           \begin{align*}
           \int_M\!\dd \alpha_i
           &= \int_{\varphi\inv|([a_1, b_1] \times \dotsb \times [a_n, b_n])}\!\dd \alpha_i\\
           &= \int_{[a_1, b_1] \times \dotsb \times [a_n, b_n]}\! {\varphi\inv}^* \dd \alpha_i\\
           &= \int_{\partial([a_1, b_1] \times \dotsb \times [a_n, b_n])}\! {\varphi\inv}^* \alpha_i\\
           &= 0
           \end{align*}

        となる。
        最後から二番目の等号に :ref:`例題 1.6.9 <tsuboi08.1.6.9>` を使う。

    * 空集合でない場合は :math:`a_1 < 0,\ b_1 = 0` が成り立っている。
      :math:`k > 1` ならば、やはり

      .. math::

         {\varphi\inv}^*\alpha_i|[a_1, b_1] \times \dotsb \times \set{a_k, b_k} \times \dotsb \times [a_n, b_n] = 0

      であるので、再び :ref:`例題 1.6.9 <tsuboi08.1.6.9>` により積分の値は次のようになる：

      .. math::

         \begin{align*}
         \int_M\!\dd \alpha_i
         &= \int_{\varphi\inv|([a_1, b_1] \times \dotsb \times [a_n, b_n])}\!\dd a_i\\
         &= \int_{\varphi\inv|\zeroset \times [a_2, b_2] \times \dotsb \times [a_n, b_n]}\!\alpha_i\\
         &= \int_{\partial M}\!\alpha.
         \end{align*}

.. _tsuboi08.3.5.2:

* 問題 3.5.2: :math:`\omega = x_1 \dd x_2 \wedge \dd x_3 - x_2 \dd x_1 \wedge \dd x_3 + x_3 \dd x_1 \wedge \dd x_2`

  埋め込み :math:`\fn{\iota}{S^2}\RR^3` について、
  球面 :math:`S^2` に閉球 :math:`B^3` の境界としての向きを定義する。

  * \(1) :math:`\displaystyle \int_{S^2}\!\iota^*\omega` の値は何か。

    .. math::

       \begin{align*}
       \int_{S^2}\!\iota^*\omega
       &= \int_{S^2}\!\omega\\
       &= \int_{\partial B^3}\!\omega\\
       &= \int_{B^3}\!\dd\omega\\
       &= \int_{B^3}\! 3 \dd x_1 \wedge \dd x_2 \wedge \dd x_3\\
       &= 3 \cdot \frac{4}{3}\pi\\
       &= 4\pi.
       \end{align*}

    * 最初の等号は包含写像の引き戻しであることによる。
    * 二番目の等号は本問の仮定による。
    * 三番目の等号は :ref:`定理 3.5.1 ストークスの定理 <tsuboi08.3.5.1>` による。
    * 四番目の等号が暗算で出てくるのが望ましい。
      この積分は球の体積 3 倍を意味する。

  * \(2) :ref:`問題 2.7.4 <tsuboi08.2.7.4>` の :math:`(\pi_S\inv)^*(\omega|S^2)` について
    :math:`\displaystyle \int_{\RR^2}\!(\pi_S\inv)^*(\omega|S^2)` の値は何か。

    素直に計算して構わない：

    .. math::

       \begin{align*}
       \int_{\RR^2}\!(\pi_S\inv)^*(\omega|S^2)
       &= \int_{\RR^2}\! \frac{4}{(1 + u_1^2 + u_2^2)^2}\,\dd u_1 \wedge \dd u_2\\
       &= \int_{-\infty}^{\infty}\!\int_{-\infty}^{\infty}\!
           \frac{4}{(1 + (r\cos\theta)^2 + (r\sin\theta)^2)^2}
           r(\cos^2\theta - (-\sin^2\theta))\,\dd r \dd \theta\\
       &= \int_0^{2\pi}\!\int_0^\infty\!\frac{4r}{(1 + r^2)^2}\,\dd r \dd \theta\\
       &= 2\pi \left[-\frac{2}{1 + r^2}\right]_0^\infty\\
       &= 4\pi.
       \end{align*}

.. _tsuboi08.3.5.3:

* 問題 3.5.3: :math:`T^2 = \set{(x_1, x_2, x_3) \in \RR^3 \sth (\sqrt{x_1^2 + x_2^2} - 2)^2 + x_3^2 = 1}`

  :math:`H = \set{(x_1, x_2, x_3) \in \RR^3 \sth (\sqrt{x_1^2 + x_2^2} - 2)^2 + x_3^2 \le 1}`
  の境界としての向きをトーラスに定義する。

  * \(1) 次の積分を示せ：

    .. math::

       \int_{T^2}\!x_1\,\dd x_2 \wedge \dd x_3 = 4\pi^2.

    ストークスの定理を利用すると左辺は次のように変形できる：

    .. math::

       \begin{align*}
       \int_{T^2}\! x_1\,\dd x_2 \wedge \dd x_3
       &= \int_{\partial H}\! x_1 \,\dd x_2 \wedge \dd x_3\\
       &= \int_H\! \dd(x_1 \,\dd x_2 \wedge \dd x_3)\\
       &= \int_H\! \dd x_1 \wedge \dd x_2 \wedge \dd x_3.
       \end{align*}

    ここから重積分に展開して計算を続けてもよいが、
    これは取りも直さずこのトーラス内部の体積を意味するので
    積分の値は :math:`2\pi^2 \cdot 1 \cdot \sqrt{2}^2 = 4\pi^2` であると言ってよい。

  * \(2) 次の積分を示せ：

    .. math::

       \int_{T^2}\!\dfrac{\sqrt{x_1^2 + x_2^2} - 2}{x_1^2 + x_2^2}
       (x_1\dd x_2 - x_2\dd x_1) \wedge \dd x_3
       + x_3\dd x_1 \wedge \dd x_2 = 8 \pi^2.

    .. todo::

       まず被積分微分形式を外微分することになる：

       .. math::

          3 - \dfrac{2}{\sqrt{x_1^2 + x_2^2}}\,\dd x_1 \wedge \dd x_2 \wedge \dd x_3.

       これにより変数変換を施した上で次のようになる：

       .. math::

          \begin{align*}
          \cdots &= \int_H\!\left(3 - \frac{2}{r}\right)r\,\dd r \dd \theta \dd x_3\\
          &= \int_{-1}^1\!\int_0^{2\pi}
             \left[\frac{3}{2}r^2 - 2\right]_{2 - \sqrt{1 - x_3^2}}^{2 - \sqrt{1 + x_3^2}}
             \,\dd \theta \dd x_3\\
          &= \cdots\\
          &= 8 \pi^2.
          \end{align*}

  * 別解の三角関数バージョン引き戻しも面白い。
    埋め込み（はめ込み）の :math:`\iota` を後述の :ref:`問題 3.7.1 <tsuboi08.3.7.1>`
    にあるトーラスの式で定義して、

    .. math::

       \iota^* \omega = (2 + \cos v)\,\dd u \wedge \dd v

    であることを利用するものだ。

.. _tsuboi08.3.5.4:

* 問題 3.5.4: 商空間の多様体 1-form

  * :math:`A = \RR^3 \minuszero`
  * :math:`r > 1` に対して :math:`A` の同値関係を次で定義する：
    :math:`\bm x \sim \bm y \iff \exists n \in \ZZ \quad\text{s.t. }\bm x = r^n\bm y.`
  * :math:`X = A/\sim`, 射影を :math:`\fn{\pi}{A}X` とする。

  商空間のために記号を定義すると、どちらがどちらかわかりにくいのでやめておけばよかった。

  * \(1) :math:`0 \ne (a_1, a_2, a_3) \in \RR^3` のときに次の微分形式 :math:`\widetilde \alpha \in \varOmega^1(A)`
    について :math:`\widetilde \alpha = \pi^* \alpha` を満たす :math:`\alpha \in \varOmega^1(X)` が存在する：

    .. math::

       \dfrac{a_1 x_1 \dd x_1 + a_2 x_2 \dd x_2 + a_3 x_3 \dd x_3}{x_1^2 + x_2^2 + x_3^2} \in \varOmega^1(A).

    * 写像 :math:`\fnm{F^n}{A}{A}{\bm y}r^n\bm y` で :math:`\widetilde \alpha` を引き戻すと
      :math:`{F^n}^*\widetilde\alpha = \widetilde \alpha` が成り立つことを示す。

    * :math:`X` の座標近傍系をなす開集合間の座標変換が局所的に :math:`F^n` に一致することを利用して、
      1 形式の定義 :ref:`定義 2.1.7 <tsuboi08.2.1.7>` より、
      :math:`X` 上の :math:`\alpha` を定めている。
      これが引き戻し :math:`\widetilde \alpha` なのだ。

  * \(2) :math:`0 \ne \bm v = (v_1, v_2, v_3) \in \RR^3` に対して閉曲線
    :math:`\fnm{\gamma_v}{[0, 1]}{X}{t}{\pi \circ r^t(v_1, v_2, v_3)}` とする。
    積分 :math:`\displaystyle \int_{\gamma_v}\!\alpha` は何か。

    * 元の空間上への曲線 :math:`\fnm{\widetilde \gamma_v}{A}{t}r^t(v_1, v_2, v_3)` を考える。
      これは :math:`\gamma_v = \pi\circ \widetilde \gamma_v` となるように定義したものだ。

    * あとは積分をひたすら計算する：

      .. math::

         \begin{align*}
         \int_{\gamma_v}\!\alpha
         &= \int_{[0, 1]}\!\gamma_v^*\alpha\\
         &= \int_{[0, 1]}\!\widetilde \gamma_v^* \pi^*\alpha\\
         &= \int_{[0, 1]}\!\widetilde \gamma_v^*\widetilde\alpha\\
         &= \int_0^1\! \text{ TODO }\\
         &= \frac{a_1 v_1^2 + a_2 v_2^2 + a_3 v_3^2}{v_1^2 + v_2^2 + v_3^2} \log r.
         \end{align*}

      * 最初の等号は線積分の定義による。
      * 二番目の等号は前小問の結果と引き戻しの反変性による。
      * 三番目の等号は射影（の引き戻し）の性質による。
      * 残りの等号は直接計算による。

  * \(3) :math:`\alpha \in Z^1(X)` だろうか。
    そしてもしそうであれば、もっと強く :math:`\alpha \in B^1(X)` だろうか。
    さらに :math:`\widetilde \alpha \in Z^1(A)` に対してはどうか。

    * :math:`\alpha \in Z^1(X)` というのは局所的な条件。
      座標近傍上の表示とみられる :math:`\widetilde \alpha \in Z^1(A)` と同値である。

    * よって :math:`\dd \widetilde \alpha` を計算すればわかる：
      :math:`\dd \widetilde \alpha = 0 \iff a_1 = a_2 = a_3 = 0.`

    * :math:`a_1 = a_2 = a_3 = a \ne 0` と仮定すると、小問 (2) の積分はゼロではない。
      だから完全形式であるとは限らない。

    * :math:`\widetilde \alpha \in Z^1(A)` ならば、
      実は :math:`\widetilde \alpha \in B^1(A)` である：

      .. math::

         \widetilde \alpha = \frac{a(x_1\dd x_1 + x_2\dd x_2 + x_3\dd x_3)}{x_1^2 + x_2^2 + x_3^2}
         = \dd{(a \log(x_1^2 + x_2^2 + x_3^2))}.

      解答の注によると :math:`\H^1(A) \cong 0` であるとのこと。

.. _tsuboi08.3.5.5:

* 問題 3.5.5: 商空間の多様体 2-form

  前問の設定をそのまま引き継ぐ。

  * :math:`b_1, b_2, b_3 \in \RR`

  ..

  * \(1) :math:`\widetilde \beta \in \varOmega^2(A)` を次のように定義する：

    .. math::

       \widetilde \beta =
         \frac{b_1 x_2 x_3 \dd x_2 \wedge \dd x_3
              -b_2 x_1 x_3 \dd x_1 \wedge \dd x_3
              +b_3 x_1 x_2 \dd x_1 \wedge \dd x_2}
              {x_1^2 + x_2^2 + x_3^2}

    このとき :math:`\widetilde \beta = \pi^* \beta` を満たす
    :math:`\beta \in \varOmega^2(X)` が存在する。

    * :ref:`前問 <tsuboi08.3.5.4>` 参照。

  * \(2) :math:`\pi(S^2) \subset X` に向きを与えて積分 :math:`\displaystyle \int_{\pi S^2}\!\beta` を求める。

    * :math:`\displaystyle \int_{\pi S^2}\!\beta = \int_{S^2}\!\widetilde\beta.`
    * :math:`\beta` の分子を :math:`\beta_1` とおくと、
      :math:`\widetilde\beta|S^2 = \beta_1|S^2` が成り立つというのが本問の急所だと思われる。
    * :math:`\dd \beta_1 = 0` である。ストークスの定理により次の計算が成り立つ：

      .. math::

         \begin{align*}
         \int_{S^2}\!\beta_1
         &= \int_{B^3}\!\dd \beta_1\\
         &= 0.
         \end{align*}

      ここで :math:`B^3` は閉球とする。

  * \(3) :math:`\beta \in Z^2(X)` か。
    もしそうならば、より強く :math:`\beta \in B^2(X)` と言えるか。

    * まず :math:`\beta \in Z^2(X) \iff \widetilde \beta \in Z^2(A)` に注意する。
    * :math:`\dd \widetilde \beta` を計算して、:math:`b_1 = b_2 = b_3 = 0` が条件であることがわかる。
    * :math:`\beta \in Z^2(X)` のとき :math:`0 = [\beta] \in \H^2(X).`

3.6 写像度
======================================================================
.. _tsuboi08.3.6.1:

* 定理 3.6.1: 写像度

  * :math:`M_1, M_2` を向き付けを持つコンパクト n 次元多様体とする。
  * :math:`\fn{F}{M_1}M_2` を写像とする。

  このときある整数 :math:`m \in \ZZ` が存在して、
  任意の :math:`\alpha \in \varOmega^n(M_2)` に対して次の等式が成り立つ：

  .. math::

     \int_{M_1}\!F^*\alpha = m \int_{M_2}\!\alpha.

  本書の図 3.9 がわかりやすい。こういうイラストを自分で描けるようにしたいものだ。

  1. :math:`\fn{F}{M_1}M_2` の臨界値の集合を :math:`C \subset M_2` とおく。
     :ref:`幾何学 I 定理 5.4.1 サードの定理 <tsuboi05.5.4.1>` によると、
     :math:`C` の測度はゼロである。

  2. :math:`M_1` のコンパクト性により、:math:`M_1` の臨界点の集合もコンパクトである。
     ゆえに :math:`C` もコンパクトである。

  3. 補集合 :math:`M_2 \setminus C` は空集合ではない開集合である。

  4. 点 :math:`y \in M_2 \setminus C` をとる。さらにその逆像を
     :math:`F\inv(y) = \set{x_1, \dotsc, x_k}` とおく。

     * 有限個で済む理由を考えないといけない。

     このとき、各点 :math:`x_1, \dotsc, x_k` の座標近傍をそれぞれ
     :math:`U_1, \dotsc, U_k` とおく。
     これらはいずれも :math:`y` の座標近傍 :math:`V` と微分同相である。

  5. 点 :math:`y` を含んでいない集合 :math:`\displaystyle F(M_1\setminus \bigcup_{i=1}^k U_i)`
     はコンパクトである。

  6. よって、その補集合 :math:`\displaystyle M_2 \setminus F(M_1\setminus \bigcup_{i=1}^k U_i)` は開集合であり、
     :math:`y \in W \subset V` なる開集合 :math:`W` がとれる。

  7. 以上により

     * :math:`\displaystyle F\inv(W) = \bigcup_{i=1}^k (F\inv(W) \cap U_i)`
     * :math:`F|(F\inv(W) \cap U_i)` は微分同相

     である。

  8. :math:`\alpha \in \varOmega^n(M_2)` で

     * :math:`\displaystyle \int_{M_2}\!\alpha > 0` かつ
     * :math:`\supp{F^*\alpha} = W`

     なるものをとる。

  9. :math:`F^*\alpha \in \varOmega^n(M_1)` は :math:`\supp{\alpha} = W` を満たす。

  10. 次の等式が 7. により成り立つ：

      .. math::

         \int_{F\inv(W) \cap U_i}\!(F^*\alpha)|(F\inv(W) \cap U_i) = \pm\int_W\!\alpha|W.

  11. この等式が成り立つということは、ある整数が存在してうんぬんという主張が成り立つということだ。

  12. :math:`[\alpha] \in \H^n(M_2)` は生成元である。
      :math:`\fn{F^*}{\H^n(M_2)}\H^n(M_1)` は :math:`\RR \longto \RR` の準同型であるから、
      8. の :math:`\alpha` は任意でよい。

      * :ref:`定理 2.4.11 <tsuboi08.2.4.11>` による？

.. _tsuboi08.3.6.2:

* 定義 3.6.2: `写像度 <http://mathworld.wolfram.com/BrouwerDegree.html>`__

  上述の整数 :math:`m` を :math:`F` の写像度という。

.. _tsuboi08.3.6.3:

* 注意 3.6.3: ホモトピックな関数について

  * :math:`C^\infty` ホモトピックな写像同士の写像度は等しい。
    これは :ref:`定理 2.4.18 <tsuboi08.2.4.18>` による。
  * 写像度はホモトピー不変量であるということだが、
    逆に写像度が等しい :math:`F_0, F_1` 同士はホモトピックだろうか。
    考えてみよう。

.. _tsuboi08.3.6.4:

* 問題 3.6.4: 複素射影直線と `代数学の基本定理 <http://mathworld.wolfram.com/FundamentalTheoremofAlgebra.html>`__

  * :math:`z \in \CC` と :math:`n \in \NN` に対して

    * :math:`P_0(z) = z^n`,
    * :math:`P(z)` を n 次多項式とする。

  * :math:`\fn{f}{\CC P^1}\CC P^1` を次の条件を満たす写像とする：

    * :math:`[z : 1] \longmapsto [P(z) : 1]`
    * :math:`[1 : 0] \longmapsto [1 : 0]`

  * :math:`\fn{f_0}{\CC P^1}\CC P^1` を次の条件を満たす写像とする：

    * :math:`[z : 1] \longmapsto [P_0(z) : 1]`
    * :math:`[1 : 0] \longmapsto [1 : 0]`

  * \(1) :math:`f` は :math:`C^\infty` 級である。

    :math:`\CC P^1` の座標近傍系を次のようにとれる：
    :math:`\set{(U_1, \varphi_1), (U_2, \varphi_2)}`

    ここで各記号は次を意味するものとする：

    * :math:`U_1 = \CC P^1\setminus\set{[1 : 0]}`
    * :math:`U_2 = \CC P^1\setminus\set{[0 : 1]}`
    * :math:`\fnm{\varphi_1}{U}{\CC P^1}{[z : w]}\dfrac{z}{w}`
    * :math:`\fnm{\varphi_2}{V}{\CC P^1}{[z : w]}\dfrac{w}{z}`

    1. :math:`\varphi_1 \circ f|U_1 \circ \varphi_1\inv(z) = P(z)` となるので、
       :math:`f` は :math:`U_1` 上に制限すれば :math:`C^\infty` 級である：

       .. math::

          \begin{align*}
          \varphi_1 \circ f|U_1 \circ \varphi_1\inv(z)
          &= \varphi_1 \circ f|U_1([z : 1])\\
          &= \varphi_1([P(z) : 1])\\
          &= \frac{P(z)}{1}\\
          &= P(z).
          \end{align*}

    2. :math:`\displaystyle \sum_{k = 0}^n a_{n - k}z^k\ (a_0 \ne 0)` とおくと、
       :math:`[0 : 1]` の近傍では

       .. math::

          \begin{align*}
          \varphi_2 \circ f \circ \varphi_2\inv(w)
          &= \dfrac{1}{P(\dfrac{1}{w})}\\
          &= \dfrac{1}{\sum_{k = 0}^n a_{n - k} \dfrac{1}{w^k}}\\
          &= \dfrac{w^n}{\sum_{k = 0}^n a_k w^k}.
          \end{align*}

       ここで :math:`\abs{w} < 1` ならば分母の絶対値は次の値以上である：

       .. math::

          \abs{a_0} - \left(\sum_{k = 0}^n \abs{a_k} \right)\abs{w}.

       よって :math:`\abs{w}` は 1 と :math:`\dfrac{\abs{a_0}}{\sum\abs{a_i}}` の
       小さいほうよりも小さいならば、分母の絶対値はゼロとはならない。

       それゆえ、:math:`[0 : 1]` の近傍で :math:`f` は
       :math:`C^\infty` 級である。

    以上の 1. と 2. により、:math:`f` は :math:`C^\infty` 級である。

  * \(2) 次の条件を満たす :math:`C^\infty` 級写像 :math:`\fn{F}{\CC P^1 \times [0, 1]}\CC P^1` が
    存在する：

    .. math::

       \begin{align*}
       F|\CC P^1 \times \zeroset &= f_0,\\
       F|\CC P^1 \times \set{1} &= f.\\
       \end{align*}

    1. :math:`P_z(t) = r_0\mathrm{e}^{i t \theta_0}z^n + t(a_1 z^{n - 1} + \dotsb + a_n)` とおく。

       :math:`a_0 = r_0\mathrm{e}^{i\theta_0}` としてある。

    2. :math:`F|(U \times [0, 1])` を :math:`F([z : 1], t) = [P_z(t) : 1]` で定義する。
       そうすることで、この制限定義域上では :math:`C^\infty` 級である。

       :math:`\set{[0 : 1]} \times [0 : 1]` の近傍で :math:`\varphi_2 \circ F_t \circ \varphi_2\inv` が
       原点付近で :math:`C^\infty` 級であることを見ればよい：

       .. math::

          \begin{align*}
          \varphi_2 \circ F_t \circ \varphi_2\inv(w)
          &= \cfrac{1}{P_t\left(\dfrac{1}{w}\right)}\\
          &= \frac{w^n}{r_0 \mathrm{e}^{i t \theta_0} + t(a_1 w + \dotsb + a_n w^n}).
          \end{align*}

       先ほどと同様の評価をすることで、分母は原点付近ではゼロにはならないことを示す。
       :math:`R = \min\set{r_0, 1}` とおく。

       * :math:`\abs{w} < 1` ならば分母の絶対値は :math:`R - (\sum\abs{a_k})\abs{w_k}`
         を下回らない。
       * :math:`\abs{w} < \min\Set{\dfrac{R}{\sum\abs{a_k}}, 1}` ならば
         分母の絶対値はゼロとはならない。

  * \(3) :math:`f^* = \fn{f_0^*}{\H^2(\CC P^1)}\H^2(\CC P^1)`

    * :ref:`定理 2.4.18 <tsuboi08.2.4.18>` と (2) の結果からわかる
      :math:`f` と :math:`f_0` のホモトピック関係による。

  * \(4) :math:`\displaystyle \alpha \in \varOmega^2(\CC P^1) \longmapsto \int\!\alpha` は
    写像 :math:`\fn{I}{\H^2(\CC P^1)}\RR` を導く。
    :math:`f_0^*` は何か。

    * :math:`f_0\inv([1 : 1])` の各点が正則点であるので、
      :math:`[1 : 1]` は正則値である。

      * 各点とは :math:`\set{\exp(2\pi\sqrt{-1}k/n) \sth k = 0, \dotsc, n - 1}` である。
      * 正則点であるイコール :math:`\varphi_1 \circ f \circ \varphi_1\inv(z) = z^n` における
        :math:`Dz^n = nz^{n - 1} \ne 0` を意味する。

    * :math:`D` を :math:`\RR^2` で考えると
      :math:`D(\varphi_1 \circ f \circ \varphi_1\inv) = \abs{nz^{n - 1}}^2 \ne 0.`

    このあとの証明は :ref:`定理 3.6.1 <tsuboi08.3.6.1>` の証明を含む。
    :math:`\alpha \in \varOmega^n(\CC P^1)` とある :math:`[1 : 1]` の近傍
    :math:`W` に対して：

    .. math::

       \int_{\CC P^1}\!f_0^*\alpha = n\int_{\CC P^1}\!\alpha.

  * \(5) :math:`P(z) = 0` なる :math:`z` が存在しなければ、
    写像 :math:`f` は定数写像 :math:`[1 : 0]` とホモトピックであり、
    :math:`f^* = 0.`

    * :math:`P(z) = 0` を満たす :math:`z` が存在しないならば、
      次のようなホモトピー :math:`\fn{G_t}{\CC P^1}\CC P^1` が存在することになる：

      .. math::

         G_t([z : w]) = \varphi_2\inv(t \varphi_2 f([z : w])).

    * :math:`G_1 = f.`
    * :math:`G_0` は定数関数 :math:`[1 : 0]` である。
    * :math:`G_t` は写像度ゼロの :math:`G_0` と :math:`C^\infty` 級
      ホモトピーであることになるので、:math:`f^* = 0.`

    以上は (4) と矛盾するので、零点は存在する。
    つまり、代数学の基本定理に沿う。

3.7 ガウス写像
======================================================================
* `ガウス写像 <http://mathworld.wolfram.com/GaussMap.html>`__

  * :math:`M` を向き付け可能な 2 次元多様体とする。
  * 写像 :math:`\fn{\iota}{M}\RR^3` を埋め込み（はめ込み）とする。
  * ベクトル :math:`\bm n(p)` を :math:`\iota(M)` の単位法ベクトルとする。
    次の性質がある：

    * :math:`\bm n(p) \in T_{\iota(p)}\RR^3`
    * :math:`\norm{\bm n(p)} = 1`
    * :math:`\bm n(p) \perp \iota_*(T_pM)`

  写像 :math:`\fn{\bm n}{M}S^2` を、
  :math:`T_{\iota(p)}\RR^3` と :math:`\RR^3` を同一視して、ガウス写像という。

  これは、曲面 :math:`M` の一点上における長さが 1 の法線ベクトルを
  全部まとめて考えたいと言っている。
  法線ベクトルの先端が球面をどれだけ被覆するのかに興味があるのだろう。

.. _tsuboi08.3.7.1:

* 問題 3.7.1: トーラス

  :math:`T^2 = \set{(\cos u)(2 + \cos v), (\sin u)(2 + \cos v), \sin v) \in \RR^3 \sth u, v \in \RR}`

  * \(1) :math:`\bm n(u, v)` はどういうものか。

    これは単純にベクトル :math:`\dfrac{\partial \iota}{\partial u} \times \dfrac{\partial \iota}{\partial v}`
    を計算して、長さを 1 に直せばよい。

    .. math::

       \bm n(u, v)
       = \cos u \cos v \dfrac{\partial}{\partial x_1}
       + \sin u \cos v \dfrac{\partial}{\partial x_2}
       + \sin v \dfrac{\partial}{\partial x_3}.

    クロス積の計算時点で長さは :math:`\cos(v) + 2` になっているので、
    これで割ればそのままガウス写像が得られたことになる。

  * \(2) 次の微分形式に対して積分 :math:`\displaystyle \int_{T^2}\!\bm{n}^*\omega` はいくらか。

    .. math::

       \omega = x_1\,\dd x_2 \wedge \dd x_3
              - x_2\,\dd x_1 \wedge \dd x_3
              + x_3\,\dd x_1 \wedge \dd x_2.

    1. :math:`\bm{n}^*\omega` を計算する：

       .. math::

          \begin{align*}
          \bm{n}^*\omega
          &= \omega \circ \bm n\\
          &= \cos u \cos v\,\dd{(\sin u \cos v)} \wedge \dd{\sin v}\\
          &\qquad - \sin u \cos v\,\dd{(\cos u \cos v)} \wedge \dd{\sin v}\\
          &\qquad + \sin v\,\dd{(\cos u \cos v)} \wedge \dd{(\sin u \cos v)}\\
          &= \cos u \cos v\,(\cos u \cos v\,\dd u - \sin u \sin v\,\dd v) \wedge \cos v\,\dd v\\
          &\qquad- \sin u \cos v\,(-\sin u \cos v\,\dd u - \cos u \sin v\,\dd v) \wedge \cos v\,\dd v\\
          &\qquad+ \sin v\,(-\sin u \cos v\,\dd u - \cos u \sin v\,\dd v) \wedge (\cos u \cos v\,\dd u - \sin u \sin v\,\dd v)\\
          &= \cos u \cos v\,(\cos u \cos v\,\dd u) \wedge \cos v\,\dd v - \sin u \cos v\,(-\sin u \cos v\,\dd u) \wedge \cos v\,\dd v\\
          &\qquad + \sin^2 u \cos v \sin^2 v\,\dd u \wedge \dd v\\
          &\qquad - \cos^2 u \cos v \sin^2 v\,\dd v \wedge \dd u\\
          &= \cos^2 u \cos^3 v\,\dd u \wedge \dd v + \sin^2 u \cos^3 v\,\dd u \wedge \dd v\\
          &\qquad + \sin^2 u \cos v \sin^2 v\,\dd u \wedge \dd v\\
          &\qquad - \cos^2 u \cos v \sin^2 v\,\dd v \wedge \dd u\\
          &= (\cos^2 u \cos^3 v + \sin^2 u \cos^3 v + \sin^2 u \cos v \sin^2 v + \cos^2 u \cos v \sin^2 v)\,\dd u \wedge \dd v\\
          &= \cos v (\cos^2 u \cos^2 v + \sin^2 u \cos^2 v + \sin^2 u \sin^2 v + \cos^2 u \sin^2 v)\,\dd u \wedge \dd v\\
          &= \cos v (\cos^2 u \cos^2 v + \cos^2 u \sin^2 v + \sin^2 u \sin^2 v + \sin^2 u \cos^2 v)\,\dd u \wedge \dd v\\
          &= \cos v (\cos^2 u + \sin^2 u)\,\dd u \wedge \dd v\\
          &= \cos v\,\dd u \wedge \dd v.
          \end{align*}

       SymPy にやらせようとしたが上手くいかず、結局自力で計算することになった。
       検算が面倒過ぎる。

    2. 定義に従って重積分に置き換える：

       .. math::

          \begin{align*}
          \int_{T^2}\!\bm{n}^*\omega
          &= \int_0^{2\pi}\!\int_0^{2\pi}\!\cos u\,\dd u\dd v\\
          &= 0.
          \end{align*}

.. _tsuboi08.3.7.2:

* 問題 3.7.2: ガウス・ボンネの定理の証明

  連結性が要る。

  * \(1) 本節冒頭の滑らかな埋め込み（はめ込み）の族 :math:`\iota_t` に対して、
    :math:`\fn{\bm n_t}{M}S^2` を各埋め込み（はめ込み）に対応するガウス写像とする。
    このとき、:ref:`問題 3.5.2 <tsuboi08.3.5.2>` の :math:`\omega|S^2` に対して積分
    :math:`\displaystyle \int_{M}\!\bm n_t^*(\omega|S^2)` は :math:`4 \pi` の倍数である。

    1. :math:`\bm n_t` のホモトピー性（:ref:`注意 3.6.3 <tsuboi08.3.6.3>` 参照）により、
       :math:`\bm n_t` の写像度を表す値 :math:`m \in \ZZ` が一意的に存在する。
       ゆえに任意の :math:`t` に対して：

       .. math::

          \int_M\!\bm n_t^*(\omega|S^2) = m\int_{S^2}\!\omega.

    2. 再び :ref:`問題 3.5.2 <tsuboi08.3.5.2>` により、
       :math:`\displaystyle \int_{S^2}\!\omega = 4\pi` であるから、1. に代入して

       .. math::

          \int_M\!\bm n_t^*(\omega|S^2) = 4\pi m.

  * \(2) :math:`\iota` に対して定義されるガウス写像を :math:`\bm n` とする。
    :math:`(0, 0, \pm 1)` が正則値であるとする。
    このとき、座標 :math:`x_3` は :math:`M` 上のモース関数である。

    ポイント：逆像 :math:`\bm n\inv(0, 0, \pm 1)` の各点において、
    :math:`x_3(x_1, x_2)` のヘッセ行列が非退化であることを直接示す。

    1. ヒントに従って :math:`\bm n\inv(0, 0, \pm 1)` の近傍の点を :math:`(x_1, x_2, x_3(x_1, x_2))`
       と表すことにする。

    2. :math:`x_3` の臨界点の集合は、

       * :math:`\dfrac{\partial x_3}{\partial x_1} = \dfrac{\partial x_3}{\partial x_2} = 0` を満たす点の集合と、
       * :math:`\bm n = (0, 0, \pm 1)` を満たす点の集合の

       共通部分である。

    3. :math:`\bm n(x_1, x_2)` を求めると、次のベクトルの長さを 1 に正規化したものである：

       .. math::

          \left(-\dfrac{\partial x_3}{\partial x_1},
                -\dfrac{\partial x_3}{\partial x_2},
                \pm1\right).

    4. ここがポイント。
       :math:`(0, 0, \pm 1)` の近傍における :math:`S^2` の座標関数をヒントに従って

       .. math::

          (x_1, x_2, x_3) \longmapsto \left(\dfrac{\partial x_1}{\partial x_3}, \dfrac{\partial x_2}{\partial x_3}\right)

       とすると、:math:`\bm n(x_1, x_2) = \left(\dfrac{\partial x_3}{\partial x_1}, \dfrac{\partial x_3}{\partial x_2}\right)` より、

       .. math::

          D\bm n =
          \begin{pmatrix}
          \dfrac{\partial^2 x_3}{\partial x_1^2} && \dfrac{\partial^2 x_3}{\partial x_1 \partial x_2}\\
          \dfrac{\partial^2 x_3}{\partial x_1 \partial x_2} && \dfrac{\partial^2 x_3}{\partial x_2^2}
          \end{pmatrix}.

    5. :math:`(0, 0, \pm 1)` が正則値であるならば、
       :math:`\bm n\inv(0, 0, \pm 1)` の点において :math:`x_3(x_1, x_2)` のヘッセ行列は非退化である。

  * \(3) :math:`x_3` についての極大値、極小値、鞍点のそれぞれの個数を :math:`a, b, c` とすると
    :math:`\bm n` の写像度は :math:`\dfrac{1}{2}(a + b + c)` で与えられる。

    * ポイント：逆像 :math:`\bm n\inv(0, 0, 1)` と :math:`\bm n\inv(0, 0, -1)` を分けて考える。
    * 各点でヤコビアンの行列式が正であることと、:math:`x_3` の極大・極小をそこでとることが同値である。
    * 各点でヤコビアンの行列式が負であることと、:math:`x_3` の鞍点をそこでとることが同値である。

    1. :math:`\bm n\inv(0, 0, 1) = \set{p_1, \dotsc, p_k}` とし、
       開集合 :math:`U_i \in M` を

       * 点 :math:`p_i` の近傍であり、
       * :math:`\fn{\bm n}{U_i}S^2` について :math:`\bm n(U_i)` と微分同相である

       ようにとる。

    2. :math:`(0, 0, 1)` の近傍 :math:`V_+` を次のようにとる：

       .. math::

          V_+ \cap \bm n\left(M \setminus \bigcap_{i = 1}^k \closure{U_i}\right) = \varnothing.

    3. :math:`\alpha \in \varOmega^2(S^2)` を :math:`\supp\alpha = V_+` となるようにとる。

    4. 上述 (2) より

       * \(A+): :math:`\det{D\bm n} > 0 \iff` :math:`x_3` の極大点・極小点
       * \(B+): :math:`\det{D\bm n} < 0 \iff` :math:`x_3` の鞍点

    5. 以上より次の式が成り立つ：

       .. math::

          \int_M\!\bm n^*\alpha = \sum_{\text{(A+)}}\int_{S^2}\!\alpha - \sum_{\text{(B+)}}\int_{S^2}\!\alpha.

    6. :math:`\bm n\inv(0, 0, -1)` に対しても 1. から 5. までと同様に考える：

       .. math::

          \int_M\!\bm n^*\beta = \sum_{\text{(A-)}}\int_{S^2}\!\beta - \sum_{\text{(B-)}}\int_{S^2}\!\beta.

    7. 写像度を求めることができる。

       :math:`\displaystyle \int_{S^2}\!\alpha = \int_{S^2}\!\beta` ととれれば（？）、
       :math:`\displaystyle \int_M\!\bm n^*\alpha = \int_M\!\bm n^*\beta` となる。
       これらを割り、5. と 6. を適用すれば題意の和を得る。

.. _tsuboi08.3.7.3:

* 問題 3.7.3: `ガウス・ボンネの定理 <http://mathworld.wolfram.com/Gauss-BonnetFormula.html>`__

  :math:`M` を向き付けられた 2 次元連結多様体であるとし、
  :math:`\fn{\bm n}{M}S^2` を埋め込み（はめ込み）に対するガウス写像である

  とする。

  * :ref:`問題 3.7.2 <tsuboi08.3.7.2>` の (3) の :math:`\dfrac{1}{2}(a + b + c)` は
    :math:`\chi(M)` そのものである。
    だから、この値は :math:`\iota` のとり方によらないはずだ。

  * :ref:`問題 3.7.2 <tsuboi08.3.7.2>` の (1) より、埋め込み（はめ込み）を変形すれば
    :math:`(0, 0, \pm 1)` を正則値としてもよい。それゆえ :math:`\bm n` の写像度は
    :math:`\dfrac{1}{2}\chi(M)` と等しい。

  * :ref:`問題 3.5.2 <tsuboi08.3.5.2>` の :math:`\omega|S^2` は「面積要素」であり、
    :math:`\displaystyle \int_{S^2}\!\omega|S^2 = 4\pi.`

  以上を組み合わせて次の等式を得る：

  .. math::

     \int_M\!\bm n^*(\omega|S^2) = 2\pi \chi(M).

  この被積分部をガウスの曲率形式という。

ガウス・ボンネの定理の対象を偶数次元のコンパクト多様体に一般化できることが
後ほど第 5 章の冒頭でごく簡単に紹介される。

3.8 第 3 章の問題の解答
======================================================================
.. todo:: 吟味中。
