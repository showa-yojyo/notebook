======================================================================
第 6 章 多様体上のフロー（後編）
======================================================================

.. contents:: ノート目次

6.3 常微分方程式の解の存在と一意性（基本）
======================================================================
* ベクトル場 :math:`X` に対して次のような :math:`F_t` が存在するのかを考える：
  :math:`\fn{F_t}{M}M,\ F_s \circ F_t = F_{s + t}.`
* これは多様体上で常微分方程式を考える問題だ。
* 開集合 :math:`U \subset \RR^n` とコンパクト集合 :math:`K \subset U` があると仮定すれば、
  :math:`\forall \bm x \in K, \exists B_\eps(\bm x) \subset U` が成り立つ。
  コンパクト性から :math:`\eps > 0` の取り方は :math:`\bm x \in K` に依存しないというのがポイントだ。

.. _tsuboi05.6.3.1:

* 定理 6.3.1 常微分方程式の解の存在、一意性、初期値に対する連続性

  * 仮定

    * リプシッツ条件：
      :math:`\exists L > 0 \text{ s.t. } t \in (a, b),\ \bm x_1, \bm x_2 \in U: \norm{X(t, \bm x_1) - X(t, \bm x_2)} \le L \norm{\bm x_1 - \bm x_2}.`

    * 有界性：
      :math:`\fn{X}{(a, b) \times U}\RR^n` は有界連続とする：
      :math:`\displaystyle \sup_{t, \bm x \in (a, b) \times U} X(t, \bm x) \le M.`

      * :math:`M` の記号がカブっている。

  * 結論

    :math:`\exists \eps_0 > 0, \exists \fn{F}{(t_0 - \eps_0, t_0 + \eps_0) \times K}U,`

    * :math:`F(t, \bm x)` は :math:`t` について微分可能であり :math:`\bm x` について連続。
    * :math:`\displaystyle F(t_0, \bm x) = \bm x,\ \diff{F}{t} = X(t, F(t, \bm x)).`

  * 証明

    * そのある関数とは
      :math:`\displaystyle F(t, \bm x) = \bm x + \int_{t_0}^t \diff{F(s, \bm x)}{s}\ \dd{s} = \bm x + \int_{t_0}^t\! X(s, F(s, \bm x))\,\dd{s}` となる。

    * アイディア

      * :math:`I_{\eps_0} := (t_0 - \eps_0, t_0 + \eps_0),\quad \mathcal C = C^0(I_{\eps_0}, U).`

        .. math::
           :nowrap:

           \begin{align*}
           \varGamma[F(t, \bm x)] := \bm x + \int_{t_0}^t X(s, F(s, \bm x))\,\dd{s} \in C^0(I_{\eps_0}, U).
           \end{align*}

        このとき :math:`F \in \mathcal C \implies \varGamma[F] \in C(I_{\eps_0} \times K, \RR^n).`

      * :math:`C^0(I_{\eps_0} \times K, \RR^n)` 上に次の距離を入れてリプシッツ性を利用する。

        .. math::

           \norm{F_1 - F_2} = \sup_{I \times K} \norm{F_1 - F_2}

    以下、上限記号の範囲指定を略記するが、
    だいたい :math:`I_{\eps_0} \times K` とかだ。

    * :math:`F_1, F_2 \in \mathcal C, \sup \norm{\varGamma[F_1] - \varGamma[F_2]} \le \eps_0 L \sup \norm{F_1 - F_2}` となる。

    * :math:`F_0(t, \bm x) = \bm x,\ F_1 = \varGamma[F_0]` とすると :math:`\sup \norm{F_1 - F_0} \le \eps_0 M.`
      ここで :math:`\eps_0 = \min\Set{\dfrac{1}{2L}, \dfrac{\eps}{4M}}` とすればよいことわがかる。

    * :math:`\eps_0 \le \dfrac{1}{2L}` と
      :math:`\eps_0 \le \dfrac{\eps}{4M}` から解の一意性と微分可能性をそれぞれ示す。

    * 微分可能性：

      * :math:`\norm{F_1 - F_0} \le \dfrac{\eps}{4}` より :math:`F_1 \in \mathcal C.`
      * :math:`F_{k + 1} = \varGamma[F_k] (F_k \in \mathcal C)` とすると次のように評価できる：

        .. math::

           \begin{align*}
           \norm{F_{k + 1} - F_k}
           &= \norm{\varGamma[F_k] - \varGamma[F_{k - 1}]}\\
           &\le \frac{1}{2} \norm{F_k - F_{k - 1}}\\
           &\le \frac{1}{2^k} \norm{F_1 - F_0}\\
           &\le \frac{\eps}{2^{k + 2}}\\
           \therefore
           \norm{F_{k + 1} - F_0} &\le \sum_{j = 0}^k \norm{F_{j + 1} - F_j}
           \le \sum{j = 0}^k \frac{\eps}{2^{j + 2}}
           < \frac{\eps}{2}.
           \end{align*}

        ゆえに :math:`\set{F_k}` は一様収束する。

      * 極限を :math:`F_\infty \in C^0(I_{\eps_0} \times K, \RR^n)` とすると
        :math:`F_\infty = \varGamma[F_infty].`

        .. math::

           \therefore F_\infty(t, \bm x) = \bm x + \int_{t_0}^t X(s, F_\infty(s, \bm x))\,\dd{s}.

    * 解の一意性：

      * :math:`F_p = \varGamma[F_p],\ F_q = \varGamma[F_q]` であるとすると、
        :math:`\norm{F_p - F_q} \le \dfrac{1}{2}\norm{F_p - F_q}`
        ゆえに :math:`F_p = F_q.`
      * リプシッツ連続が関係する命題でいつもやっている証明方法だ。

.. _tsuboi05.6.3.2:

* 注意 6.3.2 によると仮定を少し緩められるらしい。
  :math:`(a, b) \times U \times \Lambda,\ \norm{X(t, \bm x_1, \lambda) - X(t, \bm x_2, \lambda)} \le L\norm{\bm x_1 - \bm x_2}.`

.. _tsuboi05.6.3.3:

* 問題 6.3.3: :math:`C^1` 級ベクトル場と線形常微分方程式

  * ベクトル場 :math:`X(t, \bm x)` は :math:`t` について :math:`C^1` 級であり、
  * 解 :math:`F(t, \bm x) = (f_i(t, \bm x))_i` が次を満たすとする：

    * :math:`t = t_0` で初期値が :math:`\bm x` である。
    * :math:`A_{ij}(t, \bm x) = \dfrac{\partial f_i}{\partial x_j}(t, \bm x)`
      （☆）が次を満たす：

      .. math::

         \diff{A_{ij}(t, \bm x)}{t} = \sum_{k = 1}^n \frac{\partial \xi_i}{\partial x_k}(t, F(t, \bm x)) A_{kj}(t, \bm x).

  このとき :math:`F` は :math:`\bm x` についても :math:`C^1` 級である。

  * 証明の前半では :math:`F` が偏微分可能であることを示す。
    つまり、:math:`F(t, \bm x)` の初期値に対する :math:`\bm v` 方向の微分」が存在することを示す。
    そのために次の極限がある常微分方程式の解（で初期値が :math:`\bm v` であるもの）であることを
    アダマールの補題を応用して示す：

    .. math::

       \lim_{s \to 0}\frac{F(t, \bm x + s\bm v) - F(t, \bm x)}{s}.

  * アダマールの補題より、次のように書ける：

    .. math::

       \begin{align*}
       &X(t + \bm x + \bm v) - X(t + \bm x) = \sum_{i = 1}^n v_i Y_i(t, \bm x, \bm v),\\
       &Y_i(t, \bm x, \bm 0) = \frac{\partial X}{\partial x_i}(t, \bm x, \bm 0).
       \end{align*}

    これを仮定の常微分方程式に当てはめると次のようになる：

    .. math::

       \begin{align*}
       &\diff{}{t}(F(t, \bm x + s\bm v) - F(t, \bm x)) = X(t, F(t, \bm x + s\bm v)) - X(t, F(t, \bm x))\\
       &= \sum_{i = 1}^n(f_i(t, \bm x + s\bm v) - f_i(t, \bm x)) Y_i(t, F(t, \bm x), F(t, \bm x + s\bm v) - F(t, \bm x)).
       \end{align*}

  * 行列 :math:`Y = (Y_i)_i` に対して
    :math:`Y(s) = (Y_i(t, F(t, \bm x), F(t, \bm x + s\bm v) - F(t, \bm x))_i` とおくと、
    常微分方程式 :math:`\displaystyle \diff{\bm u}{t} = Y(s)\bm u`
    （★）の解は先ほどの極限の対象となる。

    * :math:`Y(s)` は :math:`s` について連続である。
    * そして :math:`s = 0` のときも連続に定義されている。
      解は（★）の解に収束する。この根拠は :ref:`注意 6.3.2 <tsuboi05.6.3.2>` から来ている。

      .. math::

         Y(0) = \frac{\partial \xi_i}{\partial x_j}(t, F(t, \bm x))

  * （☆）の :math:`A_{ij}(t, \bm x)` は次を満たす：

    * :math:`A_{ij}(t_0, \bm x) = \delta_{ij}`
    * （☆）の次に書いた常微分方程式

    :math:`\displaystyle \frac{\partial \xi_i}{\partial x_k}(t, F(t, \bm x))` を
    :math:`\bm x` をパラメーターとして見ると再び :ref:`注意 6.3.2 <tsuboi05.6.3.2>` から
    :math:`A_{ij}` は :math:`\bm x` について連続である。

    したがって :math:`F` は :math:`\bm x` について :math:`C^1` 級である。

.. _tsuboi05.6.3.4:

* 注意 6.3.4: :math:`\displaystyle \frac{\partial F(t, \bm x)}{\partial t} = X(t, F(t, \bm x))` は
  :math:`\bm x` と :math:`t` のどちらについても連続であることが
  :math:`F` が :math:`C^1` 級であることに注意。

.. _tsuboi05.6.3.5:

* 問題 6.3.5: ベクトル場が :math:`C^\infty` 級ならば解は :math:`C^\infty` 級である

  :math:`\fn{X}{(a, b) \times U}\RR^n` が :math:`C^\infty` 級であるならば、
  :math:`t = t_0` で解 :math:`\bm x` を持つ関数 :math:`F(t, \bm x)` は :math:`C^\infty` 級である。

  * まず :math:`A_{ij}(t, \bm x) = \dfrac{\partial f_i}{\partial x_j}(t, \bm x)`
    とおくとこうなる（再掲）：

    .. math::

       \diff{A_{ij}(t, \bm x)}{t} = \sum_{k = 1}^n \frac{\partial \xi_i}{\partial x_k}(t, F(t, \bm x)) A_{kj}(t, \bm x).

  * 帰納法で示す：
    「:math:`X` が :math:`C^r` 級であるとき、解 :math:`F` も :math:`C^r` 級である」とすると、

    #. 偏微分の項は :math:`C^r` 級である。
       なぜならば :math:`\dfrac{\partial \xi_i}{\partial x_k}` と :math:`F` の両方が
       :math:`C^r` 級であるから。

    #. :math:`\displaystyle \diff{F(t, \bm x)}{t} = X(t, F(t, \bm x))` については
       :math:`X` と :math:`F` が :math:`C^r` 級だから :math:`t` について
       :math:`C^r` 級である。

    ゆえに :math:`F` は :math:`C^{r + 1}` 級である。

.. _tsuboi05.6.3.6:

* 注意 6.3.6

  #. :math:`C^\infty` 級ベクトル場フローを生成するならば、
     そのフローは :math:`C^\infty` 級である。

  #. パラメーターに依存する場合、パラメーターに対して :math:`C^\infty` 級に依存するベクトル場が生成するフローもまた
     パラメーターに対して :math:`C^\infty` 級に依存する。

6.4 コンパクト多様体上のベクトル場
======================================================================
コンパクト多様体上の :math:`C^\infty` 級ベクトル場はフロー :math:`F_t` を生成する。

.. _tsuboi05.6.4.1:

* 定理 6.4.1: :math:`\displaystyle X = \diff{F_t}{t} \circ F_{-t}`

  * いつもの開被覆からさらに次のような :math:`V_i, W_i` をとる：

    * :math:`U_i \supset \closure{V_i} \supset V_i \supset \closure{W_i} \supset W_i`
    * :math:`\bigcup W_i = M`

  * 証明は三段階に分けて理解する。

    #. :math:`C^\infty` 級写像 :math:`\displaystyle \fn{F}{(-\eps, \eps) \times M}\RR^n,\quad \diff{F}{t}(t, x) = X(F(t, x))` が存在することを示す。

       * :math:`\displaystyle X = \sum_{k}\xi_k^{(i)}\frac{\partial}{\partial x_k^{(i)}}` とおく。
         閉包のコンパクト性から :math:`\varphi_i(V_i)` 上で有界連続でリプシッツ条件を満たす。

       * :math:`\varphi_i(\closure{W_i}) \subset \varphi_i(V_i)` において次のような :math:`\eps^{(i)} > 0` が存在する：

         .. math::
            :nowrap:

            \begin{align*}
            & \fn{F^{(i)}}{(-\eps^{(i)}, \eps^{(i)}) \times \varphi_i(\closure{W_i})}\varphi_i(V_i)\\
            & \diff{F^{(i)}}{t}(t, \bm x) = \xi^{(i)}(F^{(i)}(t, \bm x))\\
            \end{align*}

         ここで :math:`\xi^{(i)} = (\xi_1^{(i)}, \dotsc, \xi_n^{(i)})` とした。

       * :math:`\eps = \min\set{\eps^{(i)}}` とすると全ての :math:`x \in M` に対して次の性質を満たすような近傍 :math:`W^i` が存在する：

         .. math::
            :nowrap:

            \begin{align*}
            & F^i(t, x) = \varphi_i\inv(F^{(i)}(t, \varphi_i(x)))\\
            & \fn{F_x^i}{(-\eps, \eps)}M\\
            & \diff{F_x^i}{t}(t) = X(F_x^i(t)).
            \end{align*}

       * 別の :math:`W_j \owns x` について :math:`F_x^j` を上のように定義すると
         :math:`F_x^j = F_x^i` となる（常微分方程式の解の比較）。

    #. 解の接続。上記写像の定義域を :math:`\RR \times M` にまで拡張した写像が存在することを示す。

       * :math:`\displaystyle t \in \left(-\eps,\ \frac{\eps}{2}\eps\right)` のときは
         :math:`\displaystyle t \in \left(\frac{n - 1}{2}\eps,\ \frac{n + 1}{2}\eps\right)` に対して改めて
         :math:`\displaystyle F(t, x) = F\!\left(t - \frac{n - 1}{2}\eps,\ F\!\left(\frac{n - 1}{2}\eps,\ x\right)\!\right)` とする。

       * :math:`\displaystyle t \in \left(-\frac{\eps}{2}\eps,\ \eps\right)` のときは
         上でやった区間の「反対側」に対して改めて
         :math:`\displaystyle F(t, x) = F\!\left( t + \frac{n - 1}{2}\eps,\ F\!\left( -\frac{n - 1}{2}\eps,\ x\right)\!\right)` とする。

       どちらも :math:`\displaystyle \diff{F}{t}(t, x) = X(F(t, x))` が成り立っている。

    #. :math:`F(t + s, x) = F(t, F(s, x))` を示す。

.. _tsuboi05.6.4.3:

* 例題 6.4.3: 連結コンパクト一次元多様体が向き付け可能であることを使えば、
  多様体上にゼロでないベクトル場が存在することがわかり、
  :math:`M` と :math:`\RR/\ZZ` は微分同相であると言える。

  * 各座標近傍 :math:`U_i` に対し 1 の分割 :math:`\lambda_i` を導入する。
  * :math:`U_i` に台を持つベクトル場 :math:`\displaystyle \lambda_i \frac{\partial}{\partial t^{(i)}}` を考える。
    ここで :math:`t^{(i)}` は座標とする。

  * :math:`\displaystyle X = \sum_i \lambda_i \frac{\partial}{\partial t^{(i)}} \ne 0` が求めるものの一つである。

    * :math:`D\gamma_{ij} > 0` および :math:`\sum_i \lambda_i = 1` を利用する。

      .. math::

         X = \sum_i \lambda_i (D\gamma_{ji} \circ \varphi_i)\frac{\partial}{\partial t^{(i)}} > 0.

  * :math:`\varphi_t` を :math:`X` のフローとする（記号が座標とカブっている）。
    フローの軌道は前に述べたように 3 通りなので、これで場合分けする。

    #. 一点のみのケースはあらかじめ仮定より除外されている。
    #. :math:`M` 全体となるケースはコンパクト性により円周と同相である。
    #. :math:`M` と一致しないケース：

       :math:`A = \set{\varphi_t(x_0) \sth t \in \RR}` をとり、
       :math:`x \in M \setminus A` とする。
       ここで次のような近傍 :math:`U_i \owns x` が存在するが、
       これは :math:`X` の :math:`U_i` 上の軌道が :math:`U_i` を含むことになり、
       :math:`U_i \subset A` となって :math:`x \in M \setminus A` に矛盾する：

       .. math::

          x \in U_i,\ U_i \cap A \ne \varnothing.

.. _tsuboi05.6.4.4:

* 注意 6.4.4 は長いが、連結コンパクト一次元多様体が向き付け可能であること自体の証明だ。
  フロー、連結成分直和分割、接写像、中間値の定理などを使う。

.. _tsuboi05.6.4.5:

* 問題 6.4.5: 次の条件を満たす :math:`\displaystyle \mu\frac{\partial}{\partial x_1}` が生成するフロー
  :math:`\varPhi_t` の :math:`\displaystyle \lim_{t \to \infty}\varPhi_t(\bm x)` と
  :math:`\displaystyle \lim_{t \to -\infty}\varPhi_t(\bm x)` の値

  * :math:`\fn{\mu}{\RR^n}\RR` は :math:`C^\infty` 級で、
  * :math:`\supp \mu = \set{\bm x \in \RR^n \sth \norm{\bm x} \le 1},`
  * :math:`\norm{\bm x} < 1 \implies \mu(\bm x) > 0` と仮定する。

  #. 単位超球面上およびその外側

     :math:`\mu(\bm x) = 0` なので極限値はどちらも :math:`\bm x` となる。

  #. 単位超球面内部の場合

     * 内部ではベクトル場が非ゼロであるので、どちらの極限も球面上の点となる。
     * :math:`\varPhi_t(\bm x) = (\varphi_t(\bm x), x_2, \dotsc, x_n)` と書けるが、

       * :math:`t < 0 \implies \varphi_t(\bm x) < x_1,`
       * :math:`t > 0 \implies \varphi_t(\bm x) > x_1`

       なので次のようになるという解釈か：

       .. math::

          \lim_{t \to \pm\infty}\varPhi_t(\bm x) = (
            \pm\sqrt{1 - x_2^2 - \dotsb - x_n^2},
            x_2, \dotsc, x_n).

     解答例では具体的に :math:`\varphi_t` を求めていないように読める。

6.5 連結多様体上の部分集合の比較
======================================================================
連結多様体上の点は平等であり、特別な点は存在しない (p. 135)。

.. _tsuboi05.6.5.1:

* 例題 6.5.1: 連結多様体上の任意の二点について、一方を他方に写す微分同相写像が存在する。

  * 証明には :ref:`問題 6.4.5 <tsuboi05.6.4.5>` の技法を用いる。
  * 連結多様体上の一点を固定して、微分同相で写り合う点は同値関係となる。
    この同値類が開集合であることを示す必要がある。

    .. math::

       A_{x_1} = \set{x \in M \sth \exists \fn{F}{M}M,\ F(x_1) = x}.

    を考えると、こういう集合が同値類になって :math:`M` を非交和分割できる。

  * <同値類が開集合であることを示したから、閉集合でもある> (p. 135) とあるが、
    ここが理解できない。

.. _tsuboi05.6.5.2:

* 注意 6.5.2

  * アイソトピーもとれることが上のようにしてわかる。
  * コンパクト外では恒等写像としておけば微分同相写像であるようにできる。

.. _tsuboi05.6.5.3:

* 問題 6.5.3: 多様体次元が 2 以上の連結多様体上には、
  相異なる :math:`n` 点と別の相異なる :math:`n` 点とについて、一方を他方に写す微分同相写像が存在する。

  * 証明は帰納法による。

    #. 一点対一点の場合は :ref:`例題 6.5.1 <tsuboi05.6.5.1>` により成り立つ。
    #. :math:`x_1, \dots, x_{n - 1} \in M` を :math:`y_1, \dots, y_{n - 1} \in M` にそれぞれ写す
       微分同相写像 :math:`\fn{F_1}{M}M` が存在すると仮定する。

       * :math:`M' = M \setminus \set{y_1, \dots, y_{n - 1}}` とおくと、これは連結である（この証明がメインか？）。
       * :math:`\fn{F'}{M'}M,\quad F'(F_1(x_n)) = y_n` となる :math:`F'` が
         :ref:`例題 6.5.1 <tsuboi05.6.5.1>` により存在する。
       * :math:`F'` の定義域を元の多様体に次のように拡張して :math:`\hat{F'}` とすれば、
         :math:`F = \hat{F'} \circ F_1` が求める微分同相写像だ。

         * 点 :math:`y_i` の近傍の点 :math:`y` に対しては :math:`F' = \id\ \text{i.e. } F'(y) = y.`

.. _tsuboi05.6.5.4:

* 問題 6.5.4: 連結多様体上の任意の二点 :math:`x_0, x_1` に対して次のようなフロー :math:`F_t` が存在する：
  :math:`F_t(x_0) = x_1.`

  * :ref:`問題 6.4.5 <tsuboi05.6.4.5>` の要領で座標近傍に台を持つフロー :math:`F_t` を構成する。
  * :ref:`問題 6.5.3 <tsuboi05.6.5.3>` によると次のような微分同相写像 :math:`\fn{G}{M}M` が存在する：
    :math:`G(y_0) = x_0,\ G(y_1) = x_1.`
  * 合成写像 :math:`G \circ F_t \circ G\inv` を改めて :math:`F_t` とすれば
    それが求めるフローである。

:math:`\fn{F}{M}N` の二つの正則値 :math:`y_0, y_1` に対する :math:`F\inv(y_0), F\inv(y_1)` の比較をしたい。

.. _tsuboi05.6.5.5:

* 例題 6.5.5: ベクトル場の射影

  * :math:`M, N` をコンパクト連結多様体、
  * :math:`F \in C^\infty(M, N),`
  * :math:`\xi, \eta` をベクトル場とする。
  * :math:`\xi, \eta` の生成するフローをそれぞれ :math:`\varphi_t, \psi_t` とする。
  * :math:`\forall x \in M, F_*(\xi(x)) = \eta(F(x)) \implies F(\varphi_t(x)) = \psi_t(F(x)).`

  * 証明するには :math:`\displaystyle \diff{F(\varphi_t(x))}{t} = \eta(F(\varphi_t(x)))` を示す。

    .. math::

       \diff{F(\varphi_t(x))}{t} = F_*\left(\diff{\varphi_t(x)}{t}\right)
       = F_*\left(\xi(\varphi_t(x))\right)
       = \eta(F(\varphi_t(x))).

    等号の根拠は順に接写像の性質、
    ベクトル場 :math:`\xi` がフロー :math:`\varphi_t(x)` を生成すること、
    射影条件による。

    一方、:math:`t = t_0` のとき :math:`F(\varphi_0(x)) = F(x).`
    常微分方程式の解の一意性により :math:`\psi_t(F(x)) = F(\varphi_t(x)).`

.. _tsuboi05.6.5.6:

* 問題 6.5.6: コンパクト連結多様体 :math:`M` 上の :math:`C^\infty` 級関数 :math:`f` について
  :math:`[a, b] \subset \RR` はすべて正則値であるとすると、次が成り立つ：
  :math:`f\inv([a, b])` と :math:`f\inv(a) \times [a, b]` は微分同相である。

  * 次のようにおく：

    * :math:`\set{(U_i, \varphi_i)}_{i = 1, \dotsc, k}` を有限開被覆、
    * :math:`\lambda_i(x) \le 0` を :math:`U_i` を台とする 1 の分割、
    * また、:math:`f\inv([a, b])` と交わる :math:`\varphi_t` の第一座標成分
      :math:`x_1{(i)} = f` であると仮定してもよい（なぜか）。

  * ベクトル場 :math:`X_i = \lambda_i(x)\dfrac{\partial}{\partial x_1^{(i)}}` は
    :math:`M \setminus U_i` 上ゼロである。
  * :math:`(f_*)_x(X_i) = \lambda_i(x)\dfrac{\partial}{\partial t}.`
  * :math:`\xi = \sum(X_i)` とすると :math:`(f_*)_x\xi(x) = \sum\lambda_i(x)\dfrac{\partial}{\partial t} = \dfrac{\partial}{\partial t}.`
    したがって :math:`\xi` の生成するフロー :math:`F_t` について次が成り立つ：

    .. math::

       x \in f\inv([a, b]),\ a - f(x) \le t \le b - f(x) \implies f(F_t(x)) = f(x) + t.

  * 次に写像 :math:`\fn{p}{f\inv([a, b])}f\inv(a)` を
    :math:`x \longmapsto F_{a - f(x)}(x)` で定義する（なかなか思いつかない）。

    * さらに写像 :math:`\fn{(p, f)}{f\inv([a, b])}f\inv \times [a, b]` を考える。
      この逆写像を :math:`G(x', t)` とおくと :math:`G(x', t) = F_{t - a}(x').`

    * :math:`(p, f)` と :math:`G` のどちらも :math:`C^\infty` 級であるので、
      これらは微分同相写像である。

.. _tsuboi05.6.5.7:

* 問題 6.5.7: フローボックス定理

  * 仮定

    * :math:`M` を :math:`m` 次元コンパクト多様体、
    * :math:`N \subset M` を :math:`m - 1` 次元コンパクト部分多様体、
    * :math:`\xi` をベクトル場、
    * :math:`\varphi_t(x)` を :math:`\xi` が生成するフロー、
    * :math:`\forall x \in N, \xi(x) \notin T_x N` とする
      （部分多様体から見れば接ベクトルがはみ出す）。

  * 結論

    * 次を満たす写像と数 :math:`\eps > 0` が存在する：
      写像 :math:`(-\eps, \eps) \times N \longto M` が :math:`M` の開集合への埋め込みである。

  * 証明

    * まず写像 :math:`\fn{F}{\RR \times N}M` を
      :math:`F: (t, x) \longmapsto \varphi_t(x)` で定義する。
      :math:`t = 0` で接写像 :math:`\fn{F_*}{\RR \times T_xN}T_xM` を考えると
      点 :math:`(0, x)` で次が成り立つ：

      .. math::

         \begin{align*}
         &F_*|T_xN = \id_{T_xN},\\
         &F_*|\left(\frac{\partial}{\partial t}\right)_{(0, x)} = \xi(x).
         \end{align*}

      よって :math:`\rank F_* = m` である。

  * 逆写像定理より :math:`\zeroset \times N` 上では :math:`F` は単射である。
  * :ref:`例題 4.3.1 <tsuboi05.4.3.1>` より :math:`F` は

    * :math:`\zeroset \times N` の近傍、すなわち :math:`(-\eps, \eps) \times N` から
    * :math:`N \subset M` の近傍への

    微分同相写像である。

6.6 第 6 章の解答
======================================================================
ノートはすでに書いた。
