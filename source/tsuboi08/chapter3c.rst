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

  * 境界 :math:`\partial M := \bigcup \varphi\inv(\zeroset \times \RR^{n - 1}) \subset M` は
    :math:`n - 1` 次元部分多様体である。

  * 境界を持つ多様体の座標近傍系 :math:`\set{(U_i, \varphi_i)}` が向き付けられているとき、
    制限写像 :math:`\varphi_i|(U_i \cap \partial M)` を :math:`\partial M` の向き付けという。

  * 座標近傍 :math:`(U_i, \varphi_i = (x_1, \dotsc, x_n))` が向き付けられているならば、
    座標近傍 :math:`(\varphi_i\inv|U(\zeroset \times \RR^{n - 1}), (x_2, \dotsc, x_n))` が
    向き付けられている。

.. _tsuboi08.3.5.1:

* 定理 3.5.1: ストークスの定理

  * :math:`M` を境界あり・コンパクト・向き付けられている多様体とする。
  * :math:`\alpha \in \Omega^{n - 1}(M)`
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

  * 各 :math:`U_i` に台を持つ :math:`\alpha_i := \lambda_i \alpha` に対して
    :math:`\displaystyle \int_M\!\dd \alpha_i = \int_{\partial M}\!\alpha_i` を示せばよい。

  * :math:`\supp{{\varphi\inv}^*\alpha_i} \subset [a_1, b_1] \times \dotsb \times [a_n, b_n] \subset \varphi_i(U_i)`
    としてよい。この直方体は :math:`i` ごとにとる。

  * :math:`\varphi_i(U_i) \cap (\zeroset \times \RR^{n - 1})` が空集合か否かで場合分けをする。

    * 空集合の場合は両辺ともにゼロとなり等しくなる。

      * 右辺は境界上で微分形式がゼロであることから、積分もゼロ。
      * 左辺：

        .. math::

           \begin{align*}
           \int_M\!\dd \alpha_i
           &= \int_{\varphi\inv|\varphi(U_i)}\!\dd \alpha_i\\
           &= \int_{\varphi\inv|([a_1, b_1] \times \dotsb \times [a_n, b_n])}\!\dd \alpha_i\\
           &= \text{TODO}\\
           &= 0.
           \end{align*}

        最後から二番目の等号に :ref:`例題 1.6.9 <tsuboi08.1.6.9>` を使う。

    * 空集合でない場合は :math:`a_1 < 0,\ b_1 = 0` が成り立っている。
      :math:`k > 1` ならば

      .. math::

         {\varphi\inv}^*\alpha_i|[a_1, b_1] \times \dotsb \times \set{a_k, b_k} \times \dotsb \times [a_n, b_n] = 0

      であるので、再び :ref:`例題 1.6.9 <tsuboi08.1.6.9>` により積分の値は次のようになる：

      .. math::

         \begin{align*}
         \int_M\!\dd \alpha_i
         &= \int_{\varphi\inv|\varphi(U_i)}\!\dd a_i\\
         &= \int_{\varphi\inv|\zeroset \times \dots}\!\alpha_i\\
         &= \int_{\partial M}\!\alpha.
         \end{align*}

.. _tsuboi08.3.5.2:

* 問題 3.5.2: :math:`\omega = x_1 \dd x_2 \wedge \dd x_3 - x_2 \dd x_1 \wedge \dd x_3 + x_3 \dd x_1 \wedge \dd x_2`

  埋め込み :math:`\fn{\iota}{\S^2}\RR^3` について、
  球面 :math:`S^2` に閉球 :math:`B^3` の境界としての向きを定義する。

  * \(1) :math:`\displaystyle \int_{S^2}\!\iota^*\omega` の値は何か。

    * 解は :math:`\displaystyle \int_{B^3}\!\dd \omega = 4 \pi` であることを示したい。

  * \(2) :ref:`問題 2.7.4 <tsuboi08.2.7.4>` の :math:`(\pi_S\inv)^*(\omega|S^2)` について
    :math:`\displaystyle \int_{\RR^2}\!(\pi_S\inv)^*(\omega|S^2)` の値は何か。

    * 広義積分 :math:`\displaystyle \int_0^{2\pi}\!\int_0^\infty\!\frac{4r}{(1 + r^2)^2}\,\dd r \dd \theta = 4 \pi`
      に帰着することを示したい。

  .. todo:: 外微分の展開を計算する。

  この問題は向きの考え方がわかっていないと、例えば
  :math:`\dd u_1 \wedge \dd u_2` を :math:`\dd u_1 \dd u_2` と
  してよいかがわからないことに注意。

.. _tsuboi08.3.5.3:

* 問題 3.5.3: :math:`T^2 = \set{(x_1, x_2, x_3) \in \RR^3 \sth (\sqrt{x_1^2 + x_2^2} - 2)^2 + x_3^2 = 1}`

  :math:`H = \set{(x_1, x_2, x_3) \in \RR^3 \sth (\sqrt{x_1^2 + x_2^2} - 2)^2 + x_3^2 \le 1}`
  の境界としての向きをトーラスに定義する。

  * \(1) 次の積分を示せ：

    .. math::

       \int_{T^2}\!x_1\,\dd x_2 \wedge \dd x_3 = 4\pi^2.

    .. todo::

       残りを計算する：

       .. math::

          \begin{align*}
          \int_{T^2}\! x_1\,\dd x_2 \wedge \dd x_3
          &= \int_{\partial H}\! x_1 \,\dd x_2 \wedge \dd x_3\\
          &= \int_H\! \dd(x_1 \,\dd x_2 \wedge \dd x_3)\\
          &= \cdots
          \end{align*}

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

.. _tsuboi08.3.5.4:

* 問題 3.5.4: 商空間の多様体 1-form

  * :math:`A = \RR^3 \minuszero`
  * :math:`r > 1` に対して :math:`A` の同値関係を次で定義する：
    :math:`\bm x \sim \bm y \iff \exists n \in \ZZ \quad\text{s.t. }\bm x = r^n\bm y.`
  * :math:`X = A/\sim`, 射影を :math:`\fn{\pi}{A}X` とする。

  商空間のために記号を定義すると、どちらがどちらかわかりにくいのでやめておけばよかった。

  * \(1) :math:`0 \ne (a_1, a_2, a_3) \in \RR^3` のときに次の微分形式 :math:`\widetilde \alpha \in \Omega^1(A)`
    について :math:`\widetilde \alpha = \pi^* \alpha` を満たす :math:`\alpha \in \Omega^1(X)` が存在する：

    .. math::

       \dfrac{a_1 x_1 \dd x_1 + a_2 x_2 \dd x_2 + a_3 x_3 \dd x_3}{x_1^2 + x_2^2 + x_3^2} \in \Omega^1(A).

    * 写像 :math:`\fnm{F^n}{A}{A}{\bm y}r^n\bm y` で :math:`\widetilde \alpha` を引き戻すと
      :math:`{F^n}^*\widetilde\alpha = \widetilde \alpha` が成り立つことを示す。

    * :math:`X` の座標近傍系をなす開集合間の座標変換が局所的に :math:`F^n` に一致することを利用して、
      1 形式の定義 :ref:`定義 2.1.7 <tsuboi08.2.1.7>` より、
      :math:`X` 上の :math:`\alpha` を定めている。
      これが引き戻し :math:`\widetilde \alpha` なのだ。

  * \(2) :math:`0 \ne \bm v = (v_1, v_2, v_3) \in \RR^3` に対して閉曲線
    :math:`\fnm{\gamma_v}{[0, 1]}{X}{t}{\pi\circ r^t(v_1, v_2, v_3)}` とする。
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

  * \(3) :math:`\alpha` は閉形式であるだろうか。
    そして :math:`\alpha` が閉形式であるとすれば、それは完全形式でもあるだろうか。
    さらに、:math:`\widetilde \alpha` が閉形式であるならば、それは完全形式でもあるだろうか。

    * :math:`\alpha` が閉形式であるというのは局所的な条件。
      座標近傍上の表示とみられる :math:`\widetilde \alpha` が閉形式であることと同値である。

    * よって :math:`\dd \widetilde \alpha` を計算すればわかる：
      :math:`\dd \widetilde \alpha = 0 \iff a_1 = a_2 = a_3 = 0.`

    * :math:`a_1 = a_2 = a_3 = a \ne 0` と仮定すると、小問 (2) の積分はゼロではない。
      だから完全形式であるとは限らない。

    * :math:`\widetilde \alpha` が閉形式であるならば、実は完全形式になっている：

      .. math::

         \widetilde \alpha = \frac{a(x_1\dd x_1 + x_2\dd x_2 + x_3\dd x_3)}{x_1^2 + x_2^2 + x_3^2}
         = \dd{(a \log(x_1^2 + x_2^2 + x_3^2))}.

      解答の注によると :math:`\H^1(A) \cong 0` であるとのこと。

.. _tsuboi08.3.5.5:

* 問題 3.5.5: 商空間の多様体 2-form

  全問の設定をそのまま引き継ぐ。

  * :math:`b_1, b_2, b_3 \in \RR`

  ..

  * \(1) :math:`\widetilde \beta \in \Omega^2(A)` を次のように定義する：

    .. math::

       \widetilde \beta =
         \frac{b_1 x_2 x_3 \dd x_2 \wedge \dd x_3
              -b_2 x_1 x_3 \dd x_1 \wedge \dd x_3
              +b_3 x_1 x_2 \dd x_1 \wedge \dd x_2}
              {x_1^2 + x_2^2 + x_3^2}

    このとき :math:`\widetilde \beta = \pi^* \beta` を満たす
    :math:`\alpha \in \Omega^2(X)` が存在する。

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

  * \(3) :math:`\beta` は閉形式であるだろうか。
    そして :math:`\beta` が閉形式であるとすれば、それは完全形式でもあるだろうか。

    * まず :math:`\beta \in Z^2(X) \iff \widetilde \beta \in Z^2(A)` に注意する。
    * :math:`\dd \widetilde \beta` を計算して、:math:`b_1 = b_2 = b_3 = 0` が条件であることがわかる。
    * :math:`\beta \in Z^2(X)` のとき :math:`0 = [\beta] \in \H^2(X).`

3.6 写像度
======================================================================
TBW
