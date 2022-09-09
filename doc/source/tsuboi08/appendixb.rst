======================================================================
付録 多様体の三角形分割の構成（展開） 2/2
======================================================================

* \4. 多様体と :math:`\widehat{L}` の交わり方と記述する。

.. _tsuboi08.appendix.4.1:

  * 4.1 :math:`x \in M` について :math:`\sigma` を :math:`B_{8\delta_0}(x)` に含まれる
    :math:`\widehat{L}` の k 単体であるとする。このとき：

    .. math::

       \sigma \cap M \ne \varnothing \implies k \ge N - n,\ T_xM \cap \sigma \ne \varnothing.

    :ref:`1.7 <tsuboi08.appendix.1.7>`,
    :ref:`2.4 <tsuboi08.appendix.1.7>`,
    :ref:`3.1 <tsuboi08.appendix.1.7>` を用いる。

    :math:`y \in \sigma \cap M` を考える。
    :math:`\sigma` の面 :math:`\tau` で :math:`\dist(\tau, T_xM) < 2(1 + 2\rho_0)\delta_0 c`
    となり、その中で次元が最小のものを考える。

.. _tsuboi08.appendix.4.2:

  * 4.2 再び :math:`x \in M` について :math:`\sigma` を :math:`B_{8\delta_0}(x)` に含まれる
    :math:`\widehat{L}` の k 単体であるとする。このとき：

    .. math::

       \sigma \cap T_xM \ne \varnothing \implies k \ge N - n,\ M \cap \sigma \ne \varnothing.

    * :ref:`2.4 <tsuboi08.appendix.2.4>`, :ref:`3.1 <tsuboi08.appendix.3.1>`,
      :ref:`3.3 <tsuboi08.appendix.3.3>`, :ref:`1.7 <tsuboi08.appendix.1.7>`,
      :ref:`3.2 <tsuboi08.appendix.3.2>` を用いる。
    * :ref:`4.1 <tsuboi08.appendix.4.1>` の :math:`\sigma` の面 :math:`\tau` と同様のものを考える。

.. _tsuboi08.appendix.4.3:

  * 4.3 :math:`\sigma^{N - n}` を :math:`\widehat{L}` の :math:`N - n` 単体であるとすると、
    これは :math:`M` と高々一点で交わる。

    :ref:`1.1 <tsuboi08.appendix.1.1>` と :ref:`3.2 <tsuboi08.appendix.3.2>` による。
    :math:`y, z \in \sigma^{N - n} \cap M` に対して：

    .. math::

       \begin{align*}
       \norm{(y - \pi(y)) - (z - \pi(z))}
       &\ge \eps\norm{\pi(y) - \pi(z)}\\
       &\ge \frac{ac^2}{2^4}\norm{\pi(y) - \pi(z)}.
       \end{align*}

    ここで :ref:`3.2 <tsuboi08.appendix.3.2>` によると：

    .. math::

       \norm{(y - \pi(y)) - (z - \pi(z))} \ge 2c \norm{\pi(y) - \pi(z)}.

    :math:`\dfrac{ac^2}{2^4} < 2c` だから :math:`y = z` が必要である。

.. _tsuboi08.appendix.4.4:

  * 4.4 :math:`\sigma` を :math:`\widehat{L}` の :math:`N - n + k` 単体であるとすると、
    :math:`\sigma \cap M \ne \varnothing` であるならば、次のような :math:`N - n` 単体が存在する：

      各頂点 :math:`v` が :math:`\sigma` の頂点を頂点とする。

    :math:`x \in \sigma \cap M` における :math:`T_xM` と交わる :math:`\sigma` の
    :math:`N - n` 次元の面 :math:`\tau` を :math:`\RR^N/{T_xM}` への射影によって
    :math:`0 = [T_xM]` を含む単体に写る（？）

    さらに :math:`\partial(\tau * v)\setminus\tau` の単体で
    :math:`0 = [T_xM]` を含む単体に写るものがある。それに対して
    :math:`? \cap T_xM \ne \varnothing` かつ :math:`? \subset B_{8\delta_0}(x)` により
    :ref:`4.2 <tsuboi08.appendix.4.2>` を用いて :math:`? \cap M \ne \varnothing.`

.. _tsuboi08.appendix.4.5:

  * 4.5 :math:`\sigma^{N - n} = \langle v_0 \dots v_{N - n}\rangle` と :math:`M` が交わるならば、
    交点の重心座標は :math:`2c` 以上である。すなわち、交点を :math:`\psi(\sigma^{N - n})` を書くと、

      :math:`\displaystyle \sum_{i = 0}^{N - n}t_i v_i` と表すときに
      :math:`t_i \ge 2c\quad(i = 0, \dotsc, N - n)` である。

    :math:`v_i` の対面 :math:`\tau_i = \langle v_0 \dots v_{i - 1} v_{i + 1} \dots v_{N - n}`
    を含む affine 空間 :math:`P(\tau_i)` からの距離を考える：

    .. math::

       \dist(v_i, P(\tau_i)) \le \diam(\sigma^{N - n}) \le (1 + 2\rho_0)\delta_0 c.

    :ref:`2.4 <tsuboi08.appendix.2.4>` より

    .. math::

       \dist(\psi(\sigma^{N - n}), P(\tau_i)) \ge 2(1 + 2\rho_0)\delta_0 c.

.. _tsuboi08.appendix.4.6:

  * 4.6 :math:`\displaystyle \psi(\sigma^{N - n + k}) = \sum_{i = 0}^{N - n + k}t_i v_i\quad(k \ge 1)`
    と書くとき、:math:`t_i \ge \dfrac{2c}{k_N}.`

    :math:`\sigma^{N - n + k} = \langle v_0 \dots v_{N - n + k}\rangle \cap M = \varnothing` ならば、
    :math:`\tau_1, \dotsc, \tau_m \subset \sigma^{N - n + k}` を :math:`N - n` 単体であり、
    いずれも :math:`M` と交わるとすると、
    :ref:`4.4 <tsuboi08.appendix.4.4>` と :ref:`4.5 <tsuboi08.appendix.4.5>` により：

    .. math::

       \psi(\sigma^{N - n + k}) = \frac{1}{m}\sum_{i = 1}^m \psi(\tau_i).

* \5. 多様体の近くに単体複体 :math:`K` を構成する。

.. _tsuboi08.appendix.5.1:

  * 5.1 :math:`\widehat{L}` の :math:`N - n` 単体の列である
    :math:`\sigma^{N - k} \prec \sigma^{N - k + 1} \prec \dotsb \prec \sigma^N` と
    :math:`M` との交点 :math:`\tau_1, \dotsc, \tau_m` を基に
    :math:`M` の近くに単体複体 :math:`K` を構成する。

    * :ref:`4.4 <tsuboi08.appendix.4.4>` および
      :ref:`4.4 <tsuboi08.appendix.4.6>` の
      :math:`\psi(\sigma^{N - n}),\ \psi(\sigma^{N - k + 1})` を用いる。

    * 上記単体の列に :math:`K` の n 単体
      :math:`\langle \psi(\sigma^{N - k}), \dotsc, \psi(\sigma^N)\rangle` を対応させる
      ことができる。

.. _tsuboi08.appendix.5.2:

  * 5.2

    * もし :math:`x \in M` に対して単体 :math:`\tau \subset K` が
      :math:`\tau \subset B_{6\delta_0}(x)` を満たすならば、
      :math:`\tau` を含む :math:`\widehat{L}` の単体は :math:`B_{8\delta_0}(x)` に含まれる。

    * 単体 :math:`\tau \subset K` のすべての頂点は :math:`B_{8\eps\delta_0}(T_xM)` に
      含まれる。なぜならばどの頂点も :math:`B_{8\eps\delta_0}(T_xM)` にある
      :math:`M` の点の平均が :math:`\tau` の頂点であるからだ。

    * それゆえに :math:`\tau \subset B_{8\eps\delta_0}(T_xM).`

    :math:`B_{6\delta_0}(x)` に含まれる :math:`K` の単体は
    :math:`B_{16\eps\delta_0}(M)` にも含まれる。

* \6. 法束の射影の制限が求める三角形分割であることを示す。

  :math:`B_{16\eps\delta_0}(M) \subset U` としてよい。
  :ref:`1.2 <tsuboi08.appendix.1.2>` の射影 :math:`\fn{p_M|K}{K}M` が求めるものであることを示す。

.. _tsuboi08.appendix.6.1:

  * 6.1 「:math:`T_xM \cap B_{8\delta}(x)`」 と 「:math:`B_{8\delta}(x)` に含まれる
    :math:`\widehat{L}` の :math:`N - n + k` 単体」との共通部分は k 次元凸包である。

    * 「:math:`T_xM \cap B_{4\delta}(x)` に交わる :math:`\widehat{L}` の :math:`N` 単体全体」
      と T_xM の共通部分をとる。すると「:math:`T_xM \cap B_{4\delta}(x)` を含む集合」の
      凸包による分割が得られる。

    * この凸包による胞体分割に対する正則分割 :math:`K_1` を考える。

    * :math:`\sigma^{N - n}`, :math:`\sigma^{N - n + k}` を :math:`\widehat{L}` の単体であるとする。
    * :math:`\varphi(\sigma^{N - n})` を :math:`\sigma^{N - n}` と :math:`T_xM` との交点とする。

    * :math:`\sigma^{N - n + k}` と :math:`T_xM` は
      :math:`\varphi(\tau_i)\quad(i = 1, \dotsc, m)` で張られる凸包となる。
      ここで :math:`\tau_i\quad(i = 1, \dotsc, m)` は
      :math:`\sigma^{N - n + k}` の :math:`N - n` 面であり、
      :math:`T_xM` と交わるものであるとする。

    * :math:`\varphi(\sigma^{N - n + k}) = \dfrac{1}{m}\sum{i = 1}^m \varphi(\tau_i)` とおく。

    * :math:`K_1` は :math:`T_xM \cap B_{4\delta}(x)` においては
      :math:`T_xM` の単体分割を与える（単体複体である）。

      * :math:`\widehat{L}` の単体列 :math:`\sigma^{N - n} \prec \sigma^{N - n + 1} \prec \dotsb \prec \sigma^N` と
      * :math:`K_1` の単体 :math:`\langle\sigma^{N - n} \sigma^{N - n + 1} \dots \sigma^N\rangle` とを

      対応させることができる。

    以下、:math:`K` と :math:`K_1` を :math:`T_xM \cap B_{4\delta}(x)` に交わる
    :math:`\widehat{L}` の N 単体全体との共通部分で考える。

.. _tsuboi08.appendix.6.2:

  * 6.2 単体複体 :math:`K, K_1` の間に頂点を頂点に写す単体写像
    :math:`\psi(\sigma^{N - n + k}) \longto \varphi(\sigma^{N - n + k})` が定義され、
    単体複体間の同型を導く。

    :math:`K_1` の単体分割は

    * :math:`T_xM` の分割であり、
    * PL 多様体の条件を満たしている

    から、:math:`K` も PL 多様体の条件を満たしている。

    * 図 A.5 の見方：平らな形状が :math:`K, K_1, T_xM` だろう。

.. _tsuboi08.appendix.6.3:

  * 6.3 単体複体 :math:`K_t` を構成する。

    .. math::

       \langle\varphi_t(\sigma^{N - n})\varphi_t(\sigma^{N - n + 1})\dots\varphi_t(\sigma^{N})\rangle.

    を n 単体とする。ここで :math:`\varphi_t` は次の式で定義するものとする：

    .. math::

       \varphi_t(\sigma^{N - n + k}) = (1 - t)\psi(\sigma^{N - n + k}) + t\varphi(\sigma^{N - n + k})
       \quad(0 \le k \le n).

    * :ref:`4.6 <tsuboi08.appendix.4.6>` が根拠。

    :ref:`4.5 <tsuboi08.appendix.4.5>` と :ref:`4.6 <tsuboi08.appendix.4.6>` と同様に
    :math:`\varphi(\sigma^{N - n}),\ \varphi(\sigma^{N - n + k})`
    の重心座標を考える。

    * :ref:`4.5 <tsuboi08.appendix.4.5>` と :ref:`2.4 <tsuboi08.appendix.2.4>` から
      :math:`\dist(\varphi(\sigma^{N - n}), P(\tau_i)) \ge 2^2(1 + 2\rho_0)\delta_0 c` より
      :math:`t_i \ge 2^2c \ge 2c.`

    * :ref:`4.6 <tsuboi08.appendix.4.6>` で :math:`t_i \ge \dfrac{2^2c}{k_N} \ge \dfrac{2c}{k_N}.`

    :math:`K_t` の頂点 :math:`\varphi(\sigma^{N - n + k})` の重心座標について
    :math:`t_i \ge \dfrac{2c}{k_N}.`

    * 内分点であるから。

.. _tsuboi08.appendix.6.4:

  * 6.4 :math:`K_t` の n 単体 :math:`\tau^n = \langle\varphi_t(\sigma^{N - n})\varphi_t(\sigma^{N - n + 1})\dots\varphi_t(\sigma^{N})\rangle`
    について、affine 空間 :math:`P(\langle\varphi_t(\sigma^{N - n})\varphi_t(\sigma^{N - n + 1})\dots\varphi_t(\sigma^{N})\rangle)` と
    :math:`\psi(\sigma^{N - n + k + 1})` の距離は
    :math:`\dfrac{H\delta_0}{\sqrt{N}}\dfrac{2c}{k_N} \ge \dfrac{\delta_0}{\sqrt{N}}\dfrac{c}{k_N}`
    以上である。

    * :ref:`6.3 <tsuboi08.appendix.6.3>` を用いた。

    したがって :math:`\tau^n` の辺長も :math:`\dfrac{\delta_0}{\sqrt{N}}\dfrac{c}{k_N}` 以上である。
    「体積」にいたっては

    .. math::

       \dfrac{\delta_0^n}{n!\sqrt{N}^n}\dfrac{c^n}{k_N^n}

    以上である。

.. _tsuboi08.appendix.6.5:

  * 6.5 単体 :math:`\sigma = \langle v_0 \dots v_k\rangle` に対して
    :math:`\sigma` を含む :math:`\RR^k` 上での :math:`\sigma` の体積
    :math:`\operatorname{vol}_k(\sigma),\ \sum_{i = 1}^k a_i(v_i - v_0)` について
    次の不等式が成り立つ：

    .. math::

       \abs{a_i}\norm{v_i - v_0} \le
       \dfrac{\norm{\sum_{i = 1}^k a_i(v_i - v_0)} \prod_{i = 1}^k \norm{v_i - v_0}}
             {k! \operatorname{vol}_k(\sigma)}.

    * 考えてみよう。

.. _tsuboi08.appendix.6.6:

  * 6.6 :math:`K, K_1` を結ぶ :math:`K_t` の n 単体 :math:`\sigma_t` が
    :math:`p_M` の一点の逆像に横断的であることを示す。

    * :math:`\sigma_t` が :math:`\pi_{T_pM}` と十分な角度をもって横断的であることを
      示せば十分。

    * :math:`\bm v_{(i, t)} = \varphi_t(\sigma^{N - n + i}) - \varphi_t(\sigma^{N - n})` とする。
    * :math:`\displaystyle \bm u = \sum_{i = 1}^n a_i \bm v_{(i, t)}` を
      :math:`\sigma_t` 上の単位ベクトルであるとする。

      * 微妙な表現である気がする。

    * 次のような評価が :ref:`6.4 <tsuboi08.appendix.6.4>`, :ref:`6.5 <tsuboi08.appendix.6.5>` を用いて得られる：

      .. math::

         \begin{align*}
         \norm{\bm u - \pi(\bm u)}
         &\le \dots\\
         &\le \frac{a}{2c^{n - 1}}(1 + 2\rho_0)^n k_N^{n + 1} n \sqrt{N}^{n + 1}.
         \end{align*}

    * :math:`a` の値を調整することで :math:`\norm{\bm u - \pi(\bm u)} \le \dfrac{1}{2}`
      となり、「十分横断的である」ことが示される。

    * :ref:`1.2 <tsuboi08.appendix.1.2>` より :math:`p_M` の一点の逆像に横断的である。

    * :math:`t = 1` のとき :math:`\fn{p_M}{K_1}M` は n 単体の上で局所的に向きを保つ
      微分同相写像であるから、:math:`t = 0` でもそれは成り立つ。
      これが :math:`K` の単体から :math:`M` への微分同相写像となる。
