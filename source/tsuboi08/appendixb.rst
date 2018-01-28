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

      各頂点が :math:`\sigma` の頂点を頂点とする。

    :math:`x \in \sigma \cap M` における :math:`T_xM` と交わる :math:`\sigma` の
    :math:`N - n` 次元の面 :math:`\tau` を :math:`\RR^N/{T_xM}` への射影によって
    :math:`0 = [T_xM]` を含む単体に写る（？）

    さらに :math:`\partial(\tau * \sigma)\setminus\tau` の単体で
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
