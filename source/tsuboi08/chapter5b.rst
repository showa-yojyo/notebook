======================================================================
第 5 章 多様体の位相と微分形式 2/2
======================================================================

記号が錯綜しているので何とかしたい。

.. contents:: ノート目次

5.3 閉微分形式のポアンカレ双対（展開）
======================================================================

5.3.1 閉形式の外積とポアンカレ双対
----------------------------------------------------------------------
* :math:`M` の次元を :math:`n` とし、:math:`p + q = n` とする。
  ポアンカレの双対定理と第 3 章の内容を組み合わせると次のように書ける：

  .. math::

     \H^p(M) \cong H_p(M) \cong H^q(M) \cong \H^q(M).

  :math:`\alpha \in Z^p(M)` に対応して :math:`H_p(M)` のあるチェインが、
  :math:`\beta \in Z^q(M)` に対応して :math:`H_q(M)` のあるコチェインが
  それぞれ対応すると考えられる。

.. _tsuboi08.5.3.1:

* 定理 5.3.1:

  * :math:`M` をコンパクトかつ向き付けられた n 次元連結多様体とする。
  * :math:`K` を :math:`M` の三角形分割とする。
  * :math:`\beta \in Z^q(M)` が定める :math:`Z^q(K^*)` の
    :math:`Z_p(K)` の元を math:`PD(\beta)` とする。つまり：

    .. math::

       PD(\beta) = \sum_{\sigma \in Z_p(K)}\left(\int_{\sigma^*}\!\beta\right)\sigma

    と定義する。

  このとき、すべての :math:`\alpha \in Z^p(M)` に対して次が成り立つ：

  .. math::

     \int_M\!\alpha \wedge \beta = \int_{PD(\beta)}\!\alpha.

  証明は後ほど与える。

..

* :math:`PD(\beta)` の構成にはポアンカレ双対定理による同型 :math:`H^q(K^*) \cong H_p(K)` を用いている。
* :math:`PD(\beta)` がサイクルであることは、
  :math:`\partial(PD(\beta)) = 0` であることが
  :ref:`補題 5.2.6 <tsuboi08.5.2.6>` の等式とストークスの定理から言える。

.. _tsuboi08.5.3.2:

* 注意 5.3.2: :math:`PD(\beta)` は
  :math:`M` の三角形分割の p 次元サイクルとしてとられている。

.. _tsuboi08.5.3.3:

* 例 5.3.3:

  * \(1) :math:`M_1, M_2` を向き付けられた :math:`m_1, m_2` 次元コンパクト多様体とする。

    * :math:`\alpha_i \in \Omega^{m_i}(M_i)\quad(i = 1, 2)` を
      :math:`\displaystyle \int_{M_i}\!\alpha_i = 1` を満たす微分形式とする。
    * 直積多様体から各多様体への射影を :math:`\fn{\pi_i}{M_1 \times M_2}M_i\quad(i = 1, 2)` とする。

    このとき :math:`\displaystyle\int_{M_1 \times M_2}\!\pi_1^*\alpha_1 \wedge \pi_2^*\alpha_2 = 1`
    が成り立つ。

    :math:`\pi_2^*\alpha_2` のポアンカレ双対は、ある :math:`x_2 \in M_2` が存在して
    部分多様体 :math:`M_1 \times \set{x_2}` で与えられる：

    .. math::

       PD(\pi_2^*\alpha_2) = M_1 \times \set{x_2}

  * \(2) :math:`T^n = \RR^n/\ZZ^n` とする。

    閉形式 :math:`\dd x_{i_1} \wedge \dotsb \wedge \dd x_{i_p} \in Z^p(T^n)\quad(i_1 < \dotsb < i_p)`
    のポアンカレ双対は次で与えられる：

    .. math::

       \sgn\begin{pmatrix}
       1 & \cdots & \cdots & \cdots & n\\
       j_1 & \cdots & j_{n - p} & i_1 & \cdots i_p
       \end{pmatrix}
       T_{j_1 \cdots j_{n - p}}^{n - p}.

    ただし：

    * :math:`\set{i_1, \dotsc, i_p} \cup \set{j_1, \dotsc, j_{n - p}} = \set{1, \dotsc, n}\quad(j_1 < \dotsb < j_{n - p})`
    * :math:`T_{j_1 \cdots j_{n - p}}^{n - p} = (\RR e_{j_1} \oplus \dotsb \oplus \RR e_{j_{n - p}})/(\ZZ e_{j_1} \oplus \dotsb \oplus \ZZ e_{j_{n - p}})`

.. _tsuboi08.5.3.4:

* 定理 5.3.4: カップ積は非退化双線型形式である

  * :math:`M` をコンパクトな向き付け可能な n 次元多様体であり、
  * :math:`n = p + q` と書くとき、

  カップ積 :math:`\fn{\cup}{\H^p(M) \times \H^q(M)}\H^n(M)` は非退化双線型形式である。

  1. :ref:`定理 5.3.1 <tsuboi08.5.3.1>` の右辺 :math:`\H^p(M)` と
     :math:`H_p(M)` が双対空間であることから、これらの元の積は非退化である。

  2. :ref:`定理 5.3.1 <tsuboi08.5.3.1>` の左辺を :math:`\H^p(M)` と :math:`\H^q(M)` の
     間の積とみると、それも非退化である。

  3. :ref:`定理 2.9.6 <tsuboi08.2.9.6>` により、主張は正しい。

.. _tsuboi08.5.3.5:

* 注意 5.3.5:

  * :math:`\fn{\cap}{H^q(M) \times H_n(M)}H^p(M)` が
    :math:`\RR` 係数のホモロジー群、コホモロジー群について
    :math:`\langle[\alpha] \cup [\beta], [M]\rangle = \langle[\alpha], [\beta] \cap [M]\rangle`
    であるように定義される。

  * :math:`[PD(\beta)] = [\beta] \cap [M].`

.. _tsuboi08.5.3.6:

* 例題 5.3.6: コンパクト連結向き付け可能 2 次元多様体の 1 次元ホモロジー群は偶数次元である

  カップ積 :math:`\fn{\cup}{\H^1(M) \times \H^1(M)}\H^2(M)\quad(\cong \RR)` を考える。

  1. :ref:`定理 5.3.4 <tsuboi08.5.3.4>` により、このカップ積は非退化である。
  2. このカップ積は交代形式である。なぜなら、
     :ref:`定義 2.9.5 <tsuboi08.2.9.5>` によると、このカップ積が
     :math:`Z^1(M)` 同士の積から導かれたものであるからだ。

  3. ここがわからないのだが、1. と 2. のような双線型形式が存在するには、
     :math:`\dim \H^1(M)` が偶数であることが必要である。

     線形代数的な考察によるらしい。このカップ積は
     :math:`\alpha \cup \beta = {}^t\!aAb` なる実交代行列 :math:`A` で表現されて、
     その固有値の性質を理解すればよいと言っている。

.. _tsuboi08.5.3.7:

* 問題 5.3.7: コンパクト向き付け可能 :math:`4k + 2` 次元多様体のオイラー標数は偶数である

  :ref:`問題 5.2.9 <tsuboi08.5.2.9>` と :ref:`例題 5.3.6 <tsuboi08.5.3.6>` を
  混ぜたような問題だ。

  1. :math:`M` を :math:`4k + 2\quad(k \ge 0)` 次元コンパクト向き付け可能多様体とし、
     オイラー標数を実際に計算する：

     .. math::

        \begin{align*}
        \chi(M)
        &= \sum_{p = 0}^{4k + 2}(-1)^p\dim H^p(M)\\
        &= \left(\sum_{p = 0}^{2k} + \sum_{p = 2k + 1}^{2k + 1} + \sum_{p = 2k + 2}^{4k + 2}\right)((-1)^p\dim H^p(M))\\
        &= \sum_{p = 0}^{2k}(-1)^p\dim H^p(M) + (-1)^(2k + 1)\dim H^{2k + 1}(M) + \sum_{p = 2k + 2}^{4k + 2}(-1)^p\dim^{4k + 2 - p}(M)\\
        &= 2 \sum_{p = 0}^{2k}(-1)^p\dim H^p(M) + \dim H^{2k + 1}(M).
        \end{align*}

  2. したがって :math:`\dim H^{2k + 1}(M) \in 2\ZZ` を示せば十分。

     カップ積 :math:`\fn{\cup}{\H^{2k + 1}(M) \times \H^{2k + 1}(M)}\H^{4k + 2}(M) \cong \RR`
     を考えることによって、
     :ref:`例題 5.3.6 <tsuboi08.5.3.6>` と同じ論理により求める次元は偶数である。

5.3.2 単体的ドラーム理論と閉形式のポアンカレ双対
----------------------------------------------------------------------
* この節で :ref:`定理 5.3.1 <tsuboi08.5.3.1>` を証明する。

  * :math:`\alpha, \beta` のドラーム・コホモロジー類をそれぞれ
    :math:`\bar\alpha, \bar\beta` とすると、この定理で主張する等式が成り立つことは、
    次の等式が成り立つことと同値である：

    .. math::

       \int_M\!\bar\alpha \wedge \bar\beta = \int_{PD(\bar\beta)}\!\bar\alpha.

  * :ref:`定理 3.3.7 <tsuboi08.3.3.7>` の証明を利用する。
    以下、標準 k 形式を :math:`\omega_{i_0 \dots i_k} \in \Omega^k(K)` で表す。

  * また、:math:`\bar\alpha, \bar\beta` の展開式を次のように表す：

    .. math::

       \begin{align*}
       \bar\alpha &= \sum_{i_0 < \dotsb i_p}\left(
         \int_{\langle e_{i_0} \dots e_{i_p}\rangle}\!\alpha\right)
         \omega_{i_0 \dots i_p},\\
       \bar\beta &= \sum_{j_0 < \dotsb j_q}\left(
         \int_{\langle e_{j_0} \dots e_{j_q}\rangle}\!\beta\right)
         \omega_{j_0 \dots j_q},\\
       \end{align*}

.. _tsuboi08.5.3.8:

* 補題 5.3.8: 上述の外積の積分に関する準備

  * :math:`n = p + q` とする。
  * :math:`I = \set{i_0, \dotsc, i_p},\ J = \set{j_0, \dotsc, j_q},\ L = \set{l_0, \dotsc, l_n}`
    をいずれも相異なる昇順の添字の集合とする。
  * :math:`I \subset L` かつ :math:`J \subset L` であるとする。
  * :math:`\omega_I \colon= \omega_{i_0 \dots i_p} \in \Omega^p(\sigma_L)`,
    :math:`\omega_J \colon= \omega_{j_0 \dots j_q} \in \Omega^q(\sigma_L)` とする。

  このとき次のことが成り立つ：

  * Case 1: :math:`\Abs{I \cap J} \ge 2 \implies \omega_I \wedge \omega_J = 0.`
  * Case 2: :math:`\set{i_s = j_r} = I \cap J \implies (L = I \cup J \iff i_s = j_r = l_{s + r})`
    かつ次の等式が成り立つ：

    .. math::

       \int_{\sigma_L}\!\omega_I \wedge \omega_J =
       (-1)^{s + r}
       \sgn\begin{pmatrix}
         L\setminus\set{l_{s + r}}\\
         (I\setminus\set{i_s})(J\setminus\set{j_r})
       \end{pmatrix}
       \frac{p!q!}{(n + 1)!}

  1. Case 1 をさらに二つの場合に分けて証明する。

     :math:`\Abs{I \cap J} > 2` ならば次の二つの微分形式の両方に含まれる添字
     :math:`l \in (I\setminus\set{i_s})(J\setminus\set{j_r})` が存在する：

     .. math::

        \begin{align*}
        t_{i_s}\,\dd t_{i_0} \wedge \overset{\text{pop }\dd x_{i_s}}{\dotsb} \wedge \dd t_{i_p}\\
        t_{j_r}\,\dd t_{j_0} \wedge \overset{\text{pop }\dd x_{j_r}}{\dotsb} \wedge \dd t_{j_q}
        \end{align*}

     ゆえに :math:`\omega_I \wedge \omega_J = 0.`

  2. Case 1 の後半を証明する。

     :math:`\Abs{I \cap J} = 2` ならば、添字 :math:`i_s = j_r < i_{s'} = j_{r'}` で、
     :math:`I \cap J` に含まれるようなものが存在する。外積を展開することを考えると
     （式内の丸括弧部分は 1. のような微分形式のメイン部分）：

     .. math::

        \begin{align*}
        \omega_I \wedge \omega_J
        &= p! q! (-1)^{s + r'}t_{i_s}t_{j_{r'}} (\text{pop }\dd x_{i_s} \text{ and } \dd x_{j_{r'}})\\
        &\quad
         + p! q! (-1)^{s' + r}t_{i_{s'}}t_{j_r} (\text{pop }\dd x_{i_{s'}} \text{ and } \dd x_{j_r})
        \end{align*}

     このとき微分形式メイン部分の添字の順序を例えば
     :math:`i_0\dots i_p j_0 \dots j_{r-1} j_{r+1}\dots i_{r'-1}i_{r'+1}\dots {j_q}`
     のように揃えることを考えると、

     * 第一項の符号は :math:`(-1)^p` で、
     * 第二項の符号は :math:`(-1)^{p - 1}` のようになる。

     ゆえに :math:`\omega_I \wedge \omega_J = 0.`

  3. Case 2 を証明する。

     * 外積の展開式を 3 項に分ける：

       .. math::

          \begin{align*}
          \omega_I \wedge \omega_J
          &= p! q! (-1)^{s + r} t_{i_s}t_{j_r}\,\dd t_{i_0} \wedge \overset{\text{pop }\dd x_{i_s}}{\dotsb} \wedge \overset{\text{pop }\dd x_{j_r}}{\dotsb} \dd t_{j_q}\\
          &\quad + p! q! \sum_{k = 0,\ \ne r}^q (-1){s + k} t_{i_s}t_{j_k}\, \dd t_{i_0} \wedge \overset{\text{pop }\dd x_{i_s}}{\dotsb} \wedge \overset{\text{pop }\dd x_{j_k}}{\dotsb} \dd t_{j_q}\\
          &\quad + p! q! \sum_{k = 0,\ \ne s}^q (-1){k + r} t_{i_k}t_{j_r}\, \dd t_{i_0} \wedge \overset{\text{pop }\dd x_{i_k}}{\dotsb} \wedge \overset{\text{pop }\dd x_{j_r}}{\dotsb} \dd t_{j_q}.
          \end{align*}

     * この第 2 項の外積後半部
       :math:`\dd t_{j_r}` に :math:`\displaystyle -\sum_{l \ne j_r} \dd t_l` を、
       第 3 項の外積前半部
       :math:`\dd t_{i_s}` に :math:`\displaystyle -\sum_{l \ne i_s} \dd t_l` を
       それぞれ代入していく。

     * 結果的に次のように書ける：

       .. math::

          \omega_I \wedge \omega_J =
          (-1)^{s + r}p! q! t_{i_s}\,
          \dd t_{i_s} \wedge \dd t_{i_0} \wedge
          \overset{\text{pop }\dd x_{i_s}}{\dotsb}
          \wedge i_p \wedge j_0
          \wedge
          \overset{\text{pop }\dd x_{j_r}}{\dotsb}
          \wedge j_q.

      * これを利用して：

        .. math::

           \begin{align*}
           \int_{\sigma_L}\!\omega_I \wedge \omega_J
           &= \sgn\begin{pmatrix}
                 L\setminus\set{l_{s + r}}\\
                 (I\setminus\set{i_s})(J\setminus\set{j_r})
              \end{pmatrix}
              \int_{\sigma_L}\!\
              (-1)^{s + r} p! q! t_{l_{s + r}}
              \dd t_{l_0} \wedge
              \overset{\text{pop }\dd t_{l_{s + r}}}{\dotsb}
              \wedge \dd t_{l_n}\\
           &= \sgn\begin{pmatrix}
              L\\
              IJ
              \end{pmatrix}
              \frac{p! q!}{(n + 1)!}.
           \end{align*}

      ただし最後の等号に次の :ref:`問題 5.3.9 <tsuboi08.5.3.9>` を利用する。

  以上により、積分 :math:`\displaystyle \int_{\sigma_L}\!\omega_I \wedge \omega_J` が求まった。

.. _tsuboi08.5.3.9:

* 問題 5.3.9: 上の証明の一部

  .. math::

     \int_{\sigma_L}\!(-1)^l t_{i_l}\,
     \dd t_{i_0} \wedge
     \overset{\text{pop }\dd t_{i_l}}{\dotsb}
     \wedge \dd t_{i_n}
     = \frac{1}{(n + 1)!}.

  定義に戻って積分を計算するしかない。
  3.2 節 (p. 95) と 3.3.3 節 (p. 106) が参考になる。

  .. math::

     \begin{align*}
     \int_{\sigma_L}\!(-1)^l t_{i_l}\,
       \dd(1 - t_1) \wedge \dd(t_1 - t_2) \wedge
       \overset{\text{pop }\dd(t_l - t_{l + 1})}{\dotsb} \wedge
       \dd(t_n)
     &= \int_{\sigma_L}\!(-1)^l (t_l - t_{l + 1})(-1)^l
       \dd t_1 \wedge \dotsb \wedge \dd t_n\\
     &= \int_{t_1 = 0}^{t_1 = 1}\!
        \int_{t_2 = 0}^{t_2 = t_1}\!
        \dotsi
        \int_{t_n = 0}^{t_n = t_{n - 1}}\!
          (t_l - t_{l + 1})\,\dd t_n \dots \dd t_1\\
     &= \frac{n - l + 1}{(n + 1)!} - \frac{n - l}{(n + 1)!}\\
     &= \frac{1}{(n + 1)!}.
     \end{align*}

  * 最初の等号は各外微分を展開することによる。
  * 次の等号は、体積形式の単体に沿う積分の定義による。
  * その次の等号は単純な多項式（単項式）の累次積分の展開に過ぎないのだが、
    実は計算が合わないで困っている。

.. _tsuboi08.5.3.10:

* 補題 5.3.10: 積分に関するさらなる等式

  * :math:`I, J, L` をこれまでのものと同じ添字の集合とする。
    ただし :math:`I \subset L,\ J \subset L` であるとする。
  * :math:`M` を向き付けられた n 次元多様体であるとする。
  * :math:`K` を :math:`M` の三角形分割であるとする。
  * :math:`\sigma_I = \langle e_{i_0} \dots e_{i_p}\rangle \in K` とおく。
  * :math:`\sigma_L = \langle e_{l_0} \dots e_{l_n}\rangle \prec \sigma_I^*` とおく。
  * :math:`\sigma_I^*|\sigma_L` で部分単体を表すものとする。

  このとき次の等号が成り立つ：

  .. math::

     \int_{\sigma_I^*|\sigma_L}\!\omega_J
     = \sgn_M(\sigma_L)\int_{\sigma_L}\!\omega_I \wedge \omega_J.

  証明はかなりの手間がかかる。

  1. :math:`\Abs{I \cap J} \ge 2` のときは :math:`\omega_J|(\sigma_I^*|\sigma_L) = 0`
     となって左辺はゼロである。一方 :ref:`補題 5.3.8 <tsuboi08.5.3.8>` により右辺もゼロである。

     * :math:`\sigma_I^*|\sigma_L` の単体は、ある単体の列
       :math:`\sigma_I = \tau^q \prec \tau^{q + 1} \prec \dotsb \prec \tau^{q + p} = \sigma_L`
       が存在して、各重心頂点を用いて :math:`\langle b_{\tau^q}b_{\tau^{q + 1}}\dots b_{\tau^{q + p}}\rangle`
       の形になる。

       * :math:`\sigma_I` と :math:`\sigma_I^*` を取り違えないように注意。

     * :math:`j_r, j_{r'} \in I \cap J\quad(j_r \ne j_{r'})` とする。
       上述の重心頂点を用いた単体は、重心座標について :math:`t_{j_r}\quad(= t_{j_{r'}})` で
       表される :math:`\sigma_L` の部分空間上にある。

       * ここ、すぐに理解できるか？

     * 標準 q 形式 :math:`\omega_{j_1 \dots j_q}` の展開式において、
       :math:`\displaystyle t_{j_k} = 1 - \sum_{v \ne k}t_{j_v}` を
       :math:`t_{j_k} \ne t_{j_r}, t_{j_{r'}}` のところに代入すると
       外積 :math:`\dd t_{j_r} \wedge \dd t_{j_{r'}}` を含む。
       よってゼロである。

       * ここ、計算して確認していない。

  2. 二つの単体 :math:`\sigma_I = \langle e_{i_0} \dots e_{i_p}\rangle` と
     :math:`\sigma_J = \langle e_{j_0} \dots e_{j_q}\rangle` がただ一つの頂点
     :math:`i_s = j_r` を共有している場合は以下のようになる。

     * :math:`I \cup J = L.`
     * :math:`\sigma_I^*` に現れる :math:`\bsd(K) \cap \sigma_L` の単体を記述したい。

       * :math:`A = a_0\dots a_q` を :math:`J` の置換であり :math:`a_0 = i_s` であるものとする。
       * :math:`\displaystyle \sigma_A = \langle e_{a_0}\dots e_{a_q}\rangle = \sgn\begin{pmatrix}J\\A\end{pmatrix}\sigma_J`
         とおく。

     * :math:`w = 0, \dotsc, q` に対して :math:`\tau^{p + w} = \langle e_{j_0} \dots e_{j_q} e_{a_1}\dots e_{a_q}\rangle`
       とする。

       * :math:`\tau^p = \sigma_I` である。:math:`a_0 = i_s,\ e_{a_0} = e_{i_s}` による。
       * :math:`\tau^{p + w}` の重心は次で表される：

         .. math::

            b_{\tau^{p + w}} = \frac{1}{p + w + 1}
            \left(\sigma_{u = 0}^p e_{i_u} +
              \sigma_{v = 1}^w e_{a_v}\right).

  3. 標準 q 形式 :math:`\omega_J` の 1. の単体に沿う積分を計算する。

     * :math:`b_{\tau^{p + w}} - b_{\tau^{p + w - 1}}` を計算しておく：

       .. math::

          b_{\tau^{p + w}} - b_{\tau^{p + w - 1}} =
          -\frac{1}{(p + w)(p + w + 1)}
            \left(\sigma_{u = 0}^p e_{i_u} + \sigma_{v = 1}^{w - 1} e_{a_v}\right)
          + \frac{1}{p + w + 1} e_{a_w}.

       * 本書の数式、符号が間違っていると思われる。
         後続の数式からしても、初項にはマイナスが要る。

     * この積分は次の写像 :math:`(x_1, \dotsc, x_q) \longmapsto ?` により
       :math:`\Delta^q` に引き戻した q 形式の積分である：

       .. math::

          \begin{align*}
          (x_1, \dotsc, x_q) \longmapsto
          & \frac{1}{p + 1}\sum e_{i_u}\\
          & + x_1(b_{\tau^{p + 1}} - b_{\tau^{p}})\\
          & + x_2(b_{\tau^{p + 2}} - b_{\tau^{p + 1}})\\
          & \dots\\
          & + x_q(b_{\tau^{p + q}} - b_{\tau^{p + q - 1}})
          \end{align*}

     * :math:`\omega_J` の表示に現れる重心座標 :math:`t_{i_0} \dots t_{i_p} t_{a_0} \dots t_{a_q}`
       を求めておくことで :math:`\displaystyle (p + 1)t_{a_0} + \sum_{v = 1}^q t_{a_v} = 1` が
       わかる。
     * さらに :math:`\displaystyle \dd t_{a_0} = -\sum_{v = 1}^q \frac{\dd t_{a_v}}{p + 1}.`
     * :math:`\omega_A` を展開する：

       .. math::

          \begin{align*}
          \omega_A
          &= q! \sum_{w = 0}^q (-1)^w t_{a_w}\,\dd t_{a_0} \wedge
             \overset{\text{pop }\dd t_{a_w}}{\dotsb} \wedge
             \dd t_{a_q}\\
          &= \frac{q!}{p + 1}\frac{\dd x_1}{p + 2} \wedge \dotsb \wedge \frac{\dd x_q}{p + q + 1}.
          \end{align*}

     * ここで :math:`\displaystyle \int_{\Delta^q}\!\dd x_1 \dots \dd x_q = \dfrac{1}{q!}` であるから：

       .. math::

          \begin{align*}
          \int_{\langle b_{\tau^q}b_{\tau^{q + 1}}\dots b_{\tau^{q + p}}\rangle}\!\omega_A
          &= \int_{\Delta^q}\!\frac{q!}{p + 1}\frac{\dd x_1}{p + 2}\dotsm \frac{\dd x_q}{p + q}\\
          &= \frac{p!}{(p + q + 1)!}.
          \end{align*}

     * :math:`\displaystyle \omega_A = \sgn\begin{pmatrix}A\\J\end{pmatrix}\omega_J` を用いて
       次を得る：

       .. math::

          \begin{align*}
          \int_{\langle b_{\tau^p} \dots b_{\tau^{p + q}}\rangle}\! \omega_J
          &= \sgn\begin{pmatrix}A\\J\end{pmatrix}\frac{p!}{(p + q + 1)!}\\
          &= (-1)^r \sgn\begin{pmatrix}
            A\setminus\set{a_0}\\
            J\setminus\set{j_r}
            \end{pmatrix}
            \frac{p!}{(p + q + 1)!}
          \end{align*}

  4. :math:`A` を :math:`I \cap A = \set{i_s}` となる :math:`J` の置換とする。

     * :math:`A = a_1 \dots a_q` のように書く。
     * :math:`L` の置換を :math:`i_0 \dots i_p a_1 \dots a_q` のように書く。
     * 単体の列 :math:`\tau^p \prec \dotsb \prec \tau^{p + q}` をとることで、
       :math:`\sigma_I^*|\sigma_L` における双対胞体 :math:`\sigma_I^*` は
       次の和で表される：

       .. math::

          \langle e_{i_0} \dots e_{i_p}\rangle^*
          = \sum_A \sgn_M (\langle
            e_{i_0} \dots e_{i_p}
            e_{a_1} \dots e_{a_q}\rangle)
            \langle b_{\tau^q}b_{\tau^{q + 1}}\dots b_{\tau^{q + p}}\rangle
          \quad(A = a_1\dots a_q).

     * 次の積分を 3. の結果を用いて計算する：

       .. math::

          \begin{align*}
          \int_{\langle e_{i_0} \dots e_{i_p}\rangle^* | \sigma_L}\!\omega_J
          &= \sum_A \sgn_M (\langle
                e_{i_0} \dots e_{i_p}
                e_{a_1} \dots e_{a_q}\rangle)
                \langle b_{\tau^q}b_{\tau^{q + 1}}\dots b_{\tau^{q + p}}\rangle
             (-1)^r \sgn\begin{pmatrix}
               A\setminus\set{a_0}\\
               J\setminus\set{j_r}
               \end{pmatrix}
               \frac{p!}{(p + q + 1)!}\\
          &= \sum_A \sgn_M(\sigma_L)
             (-1)^r \sgn\begin{pmatrix}
               l_0 \dots l_{p + q}\\
               I J\setminus\set{j_r}
               \end{pmatrix}
               \frac{p!}{(p + q + 1)!}\\
          &= \sgn_M(\sigma_L)\sgn\begin{pmatrix}
               L\setminus\set{l_{s + r}}\\
               I\setminus\set{i_s} J\setminus\set{j_r}
               \end{pmatrix}
               \frac{p!}{(p + q + 1)!}\\
          &= \sgn_M(\sigma_L)\int_{\sigma_L}\!\omega_I \wedge \omega_J.
          \end{align*}

       * 最後から二番目の等号では、:math:`r, s, l` の関係によって
         :math:`(-1)^?` のようなものは消えている。

       * 最後の等号に :ref:`補題 5.3.8 <tsuboi08.5.3.8>` を用いた。

  これで主張の等式が成り立つことが示された。

..

ここまできてようやく :ref:`定理 5.3.1 <tsuboi08.5.3.1>` の証明を始める。

1. :math:`\bar\alpha = \displaystyle \sum_{i_0 < \dotsb < i_p} \alpha_{i_0 \dots i_p}\omega_I`,
   :math:`\bar\beta = \displaystyle \sum_{j_0 < \dotsb < j_q} \beta{j_0 \dots j_q}\omega_J`
   とおく。

2. 次の和を基本類 :math:`[M]` を代表するものとする：

   .. math::

      \sum_{l_0 < \dotsb < l_n}\sgn_M(\langle e_{l_0}\dots e_{l_n}\rangle)
        \langle e_{l_0}\dots e_{l_n}\rangle.

3. 左辺を計算する：

   .. math::

      \begin{align*}
      \int_M\!\bar\alpha \wedge \bar\beta
      &= \sum_{l_0 < \dotsb < l_n}\sum_{i_0 < \dotsb < i_p}\sum_{j_0 < \dotsb < j_q}
         \sgn_M(\langle e_{l_0}\dots e_{l_n}\rangle)\alpha_{i_0 \dots i_p}\beta_{j_0 \dots j_q}
         \int_{\langle e_{l_0}\dots e_{l_n}\rangle}\!\omega_I \wedge \omega_J.
      \end{align*}

4. :math:`PD(\bar\beta)` を右辺に代入したい。

   .. math::

      \begin{align*}
      PD(\bar\beta)
      &= \sum_{A}\left(\int_{\sigma_A^*}\!\sum_{j_0 < \dotsb < j_q}\beta_{j_0 \dots j_q}\omega_J\right)\sigma_A\\
      &= \sum_{A}\sum_{j_0 < \dotsb < j_q}\beta_{j_0 \dots j_q}\left(\int_{\sigma_A^*}\!\omega_J\right)\sigma_A
      \end{align*}

   であるから、

   .. math::

      \begin{align*}
      \int_{PD(\bar\beta)}\!\bar\alpha\\
      &= \int_{PD(\bar\beta)}\!\sum_{i_0 < \dotsb < i_p}\alpha_{i_0 \dots i_p}\omega_I\\
      &= \sum_{i_0 < \dotsb < i_p}\alpha_{i_0 \dots i_p} \int_{PD(\bar\beta)}\!\omega_I\\
      &= \sum_{i_0 < \dotsb < i_p}\sum_{A}\sum_{j_0 < \dotsb < j_q} \alpha_{i_0 \dots i_p}\beta_{j_0 \dots j_q}
         \left(\int_{\sigma_A^*}\!\omega_J\right)\int_{\sigma_A}\!\omega_I.
      \end{align*}

5. ここで 4. の末端の積分の値は次のようになる：

   .. math::

      \int_{\sigma_A}\!\omega_I =
      \begin{cases}
      1 & \quad\text{if }A = I,\\
      0 & \quad\text{if }A \ne I.
      \end{cases}

   * :math:`A = I` については p. 106 を参照。
   * :math:`A \ne I` については :math:`\omega_I|\sigma_A` が
     :math:`A \cap I` を添字とする重心座標で書かれていることによる。

6. したがって 4. の式変形を続けると：

   .. math::

      \begin{align*}
      \dots
      &= \sum_{i_0 < \dotsb < i_p}\sum_{j_0 < \dotsb < j_q} \alpha_{i_0 \dots i_p}\beta_{j_0 \dots j_q}
         \left(\int_{\sigma_I^*}\!\omega_J\right)\\
      &= \sum_{i_0 < \dotsb < i_p}\sum_{j_0 < \dotsb < j_q} \alpha_{i_0 \dots i_p}\beta_{j_0 \dots j_q}
         \sum_{l_0 < \dotsb < l_n}\int_{\sigma_I^*|\sigma_L}\!\omega_J.
      \end{align*}

   :math:`J \nsubseteq L` のときは :math:`\omega_J|\sigma_L = 0` である。
   なぜならば :math:`J \cap L` を添字とする重心座標で書かれているからだ。

7. :ref:`補題 5.3.10 <tsuboi08.5.3.10>` を用いると、
   最終的に 3. における左辺の変形と一致する。

5.4 第 5 章の解答
======================================================================
上に書いた。
