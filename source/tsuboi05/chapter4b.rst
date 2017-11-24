======================================================================
第 4 章 接空間（後編）
======================================================================

.. contents:: ノート目次

4.4 部分多様体
======================================================================

* 定義 4.4.1: 部分多様体

  * 多様体 :math:`N` に対して :math:`M \subset N` に次の性質があるとき、
    それを p 次元部分多様体であるという。

    .. math::
       :nowrap:

       \begin{align*}
       \forall x_0 \in M, \exists(U, \varphi): M \cap U = \set{x \in U \sth x_{p + 1} = \dots = x_n = 0}
       \end{align*}

`微分可能構造 <http://mathworld.wolfram.com/SmoothStructure.html>`__
  座標近傍系の同値類について注意しておく。
  座標近傍系の両立という概念の上位互換な概念が微分可能構造だ。

:math:`\fn{F}{M}N,\ \rank F_* = \min{m = \dim M, n = \dim N}` とすると、

.. math::

   (y_i \circ F \circ \varphi\inv) =
   \begin{cases}
   x_i & \quad \text{if } m \le n \text{ and } i = 1, \dotsc, m\\
     0 & \quad \text{if } m \le n \text{ and } i = m + 1, \dotsc, n\\
   x_i & \quad \text{if } m \ge n \text{ and } i = 1, \dotsc, n.
   \end{cases}

最後のケースでは特に :math:`F\inv(F(x_0)) \cap U = \set{x \in U \sth x_{m + 1} = \dots = x_n = 0}` は
:math:`m - n` 次元部分多様体である。

`はめ込み <http://mathworld.wolfram.com/Immersion.html>`__
  :math:`m < n` のときに、
  写像 :math:`\fn{F}{M}N` に対し、:math:`\rank F_* = m` であればはめ込みであるという。

`埋め込み <http://mathworld.wolfram.com/Embedding.html>`__
  はめ込み :math:`F` によって :math:`N` の位相から誘導される位相が
  :math:`M` の位相そのものと一致するような
  :math:`F` は埋め込みであるという。

  * :math:`F(M)` は :math:`N` の正則な部分多様体となる。

.. _tsuboi05.4.4.2:

* 定理 4.4.2: はめ込みが単射であれば、コンパクトな多様体の像は部分多様体となる。

`沈み込み <http://mathworld.wolfram.com/Submersion.html>`__
  :math:`m \ge n` の場合に
  任意の :math:`x \in M` に対して :math:`\rank F_* = n` となるとき、
  この写像は沈み込みであるという。

  * :math:`F\inv(y)` は :math:`m - n` 次元部分多様体となる。
  * この特殊な状況を :ref:`例題 8.6.1 ファイブレーション定理 <tsuboi05.8.6.1>` で取り扱う。

.. _tsuboi05.4.4.3:

* 例題 4.4.3: 部分多様体間の :math:`C^\infty` 級写像が誘導する写像も :math:`C^\infty` 級となる。

  * 仮定をまとめる：

    * :math:`N_1, N_2` をそれぞれ :math:`n_1, n_2` 次元多様体とし、
    * :math:`C^\infty` 級写像 :math:`\fn{F}{N_1}N_2` があり、
    * :math:`M_1 \subset N_1,\ M_2 \subset N_2` はそれぞれ部分多様体であり、
    * さらに :math:`F(M_1) \subset M_2` が成り立つとする。

  * :math:`M_2 \subset N_2` が部分多様体であるので、
    次のような :math:`F(x_0) \in M_2 \subset N_2` の座標近傍 :math:`(V, \varphi),\ \varphi = (y_1, \dotsc, y_{n_2})` がある：
    :math:`M_2 \cap V = \set{y_{{m_2} + 1}, \dotsc, y_{n_2} = 0}.`

  * 残りの座標成分のほうを考えと
    :math:`(y_1, \dotsc, y_{m_2}) \circ F \circ \varphi\inv` が :math:`C^\infty` 級となる。
    したがって 誘導される写像 :math:`\fn{G}{M_1}M_2` も :math:`C^\infty` 級となる。

* 問題 4.4.4: :math:`GL_2(\RR)` と :math:`SL_n(\RR)`

  * 前者は :math:`n^2` 次元多様体、後者は :math:`n^2 - 1` 次元部分多様体である。

    * 大前提として :math:`M_n(\RR)` は座標近傍系を空間全体を近傍とし、
      各成分の値をそのまま座標とする座標近傍一つからなるものを考えれば、
      これは :math:`n^2` 次元多様体である。

    * GL については :math:`GL_n(\RR) = \set{A \in M_n(\RR) \sth \det A \ne 0}` である。
      連続写像 :math:`\fn{\det}{M_n(\RR)}\RR` の開集合 :math:`\set{x \in \RR \sth x \ne 0}` の
      逆像とみなすことで開集合となり、先ほどと同じ要領で座標近傍系を構成すれば
      :math:`n^2` 次元多様体である。

    * SL について。まず定義を書き下してみると :math:`SL_n(\RR) = \set{A \in GL_n(\RR) \sth \det A = 1}` だ。
      今度は :math:`\det\inv(1)` である。

      * :math:`\det` のヤコビ行列なるものを考える。余因子展開を意識することで
        :math:`\det(x_{ij}) = \sum x_{ij} A_{ij}` のように書かれるから、
        :math:`\displaystyle \frac{\partial \det}{\partial x_{ij}} = A_{ij}` で、
        右辺は :math:`(n - 1)^2` 次正方行列の行列式になっている。

      * SL では :math:`D\det \ne 0` であることに注意。
        :math:`\det` は :math:`n^2` 次元から :math:`1` 次元への関数であり、
        陰関数定理により、ある近傍 :math:`W` と :math:`C^\infty` 級写像（座標になる）
        :math:`\fn{\varphi}{W}\RR^{n^2 - 1}` が存在する。

  * 行列の積、逆行列を取る演算はどちらも :math:`C^\infty` 級の写像である。

    * 両者ともリー群なので :ref:`問題 4.3.3 <tsuboi05.4.4.3>` を利用できる。
    * 積も逆行列も多項式の演算に、せいぜい非ゼロの値の除算が加わるものなので
      :math:`C^\infty` 級の写像だという主張には問題あるまい。

* 問題 4.4.5: 直交群 :math:`O(n)` は多様体である。

  * 写像 :math:`C: A \longmapsto {}^t\!AA` を考える。

    * 直交群は :math:`C\inv(I_n)` となる。
    * :math:`C` は :math:`C^\infty` 級である。

  * 微分を考える。ここが少し思いつかない。

    * まずは :math:`C(A + X) - C(A) = {}^t\!XA + {}^t\!AX + {}^t\!XX.`
      これの極限 :math:`X \to O` が :math:`DC_{(A)}X` である。

    * :math:`DC_{(A)}X = {}^t\!XA + {}^t\!AX` という形をよく見ると二つの写像
      :math:`X \longmapsto {}^AX` と :math:`X \longmapsto {}^t\!X + X` の合成であることに気付く。

      * :math:`\rank(X \longmapsto {}^AX) = n^2` である。
      * :math:`\displaystyle \rank({}^t\!X + X) = \frac{n(n + 1)}{2})` である。

      以上より合成写像のランクは :math:`\displaystyle \frac{n(n + 1)}{2}` である。

  * よって陰関数定理により、:math:`C\inv(I_n) = O(n)` の
    近傍 :math:`W` と :math:`C^\infty` 級写像 :math:`W \longto \RR^\frac{n(n - 1)}{2}` が存在する。

    * 写像 :math:`\fn{C}{M_n(\RR)}M_n(\RR)` は :math:`n^2` 次元空間から
      :math:`\displaystyle \frac{n(n + 1)}{2}` 次元空間へのものだとわかったことによる。

* 例題 4.4.7: 横断的に交わる二つの部分多様体の共通部もまた部分多様体である。

  * :math:`\forall x \in X \cap Z, T_x Y + T_x Z = T_x X` が仮定、
    :math:`Y \cap Z \subset X` が部分多様体であることが結論。

  以下、ノートの都合上 :math:`a = \dim X - \dim Y,\ b = \dim X - \dim Z` と書く。

  * :math:`x_0 \in Y \cap Z` の座標近傍を :math:`(U, \varphi)` とする。
  * まず次のような写像 :math:`\fn{F_Y}{U}\RR^a` が存在する：
    :math:`U \cap Y = F_Y\inv(F_Y(x_0)).`
  * さらに :math:`\forall x \in U, \rank F_{Y*} = a\quad(\fn{F_{Y*}}{T_xX}\RR^a.)`
  * 同様な性質の :math:`F_Z` も存在する。

  * 写像の直積を構成することで :math:`F_{Y*}, F_{Z*}` を適当に制限すると同型写像が得られることを示す：

    .. math::

       \fn{(F_{Y*}, F_{Z*})}{U}\RR^a \times \RR^b.

    * 接空間を :math:`T_xY = (T_xY \cap T_xZ) \oplus V_Y` のように部分空間の直和に分解する。
      このとき :math:`F_{Y*}|V_Y \cong \RR^a` となる。
      :math:`T_xZ` についても同様に :math:`V_Z` を定義する。

    * :math:`(F_{Y*}, F_{Z*})|(V_Y \oplus V_Z) \cong \RR^a \oplus \RR^b.`
      :math:`\rank(F_{Y*}, F_{Z*}) = a + b = 2\dim X - \dim Y - \dim Z.` が得られた。

  * :math:`U \cap (Y \cup Z) = (F_Y, F_Z)\inv(F_Y(x_0), F_Z(x_0))` において、
    :math:`X` 内で :math:`U` を動かすことによって
    :math:`Y \cap Z` が :math:`\dim X - (2\dim X - \dim Y - \dim Z) = \dim Y + \dim Z - \dim X` 次元の部分多様体であることがわかる。

4.5 接束（展開）
======================================================================
冒頭のユークリッド空間内の多様体から多様体と接空間のペアの空間を構成する部分は前座。

`接束 <http://mathworld.wolfram.com/TangentBundle.html>`__
  前章の記号 :math:`V_i, V_{ij}, \gamma_{ij}` 等を流用する。
  次のようにして構成する商空間を多様体の接束という：

  #. 直和 :math:`\bigsqcup V_i` に同値関係 :math:`x_i \sim x_j \iff x_i = \gamma_{ij}(x_j)` を導入する。
     このとき、商空間 :math:`X = (\bigsqcup V_i / \sim)` は :math:`M` と微分同相になる（
     :ref:`例題 3.5.2 <tsuboi05.3.5.2>` などを参照）。

  #. 直積の直和 :math:`\bigsqcup (V_i \times \RR^n)` に次の同値関係を導入する。

     .. math::
        :nowrap:

        \begin{align*}
        (x_i, v_i) \sim (x_j, v_j) \iff \exists \gamma_{ij}:
        x_i = \gamma_{ij}(x_j),\ v_i = (D\gamma_{ij})_{(x_j)} v_j
        \end{align*}

     同値関係となる理由：

     * 写像 :math:`G_{ij}: (x_i, v_i) \longmapsto (\gamma_{ij}(xj), (D\gamma_{ij})_{(x_j)} v_j)` を考える。
       これは微分同相となる。
     * そして :math:`G_{ij} \circ G_{jk} = G_{ik}` （ただし :math:`G_{ii} = \id` と約束する）が成り立つ。

     このとき、商空間 :math:`Y = (\bigsqcup (V_i \times \RR^n))/\sim` はハウスドルフとなり、
     :math:`2n` 次元多様体となる。

     ハウスドルフとなる理由（面倒）：

     * 射影をいくつか定義して、その合成写像による商空間の開集合の逆像もまた開集合であることを示し、
       :math:`Y \longto X` に連続写像が存在することを示せる。
     * 次に、直和から商空間への射影二種 :math:`p_x, p_y` を適宜制限して同相写像を得る。
     * 写像 :math:`\fn{P\inv}{p_x(V_i)}p_x(V_i) \times \RR^n` が同相であることを示す。
     * 最後に :ref:`問題 3.5.3 <tsuboi05.3.5.3>` を利用する。

  接束は `ベクトル束 <http://mathworld.wolfram.com/VectorBundle.html>`__ の一種である (pp. 85-86)。

* 問題 4.5.2: :math:`F \in C^\infty(M, N)` の引き起こす接束の間の写像
  :math:`\fn{F_*}{TM}TN` は :math:`C^\infty` 級である。

  * :math:`TM` は :math:`\bigcup \varphi_i(U_i) \times \RR^m` の商空間である。
  * :math:`TM` の座標近傍系は :math:`\varphi_i(U_i) \times \RR^m` の像および
    そこからの逆写像として定義される。
  * 以上、:math:`TN` も同様。
  * それゆえ、次の写像は :math:`F` が :math:`C^\infty` 級であれば
    :math:`C^\infty` 級となる：

    .. math::

       (\bm u_i, \bm v_i) \longmapsto ((\psi \circ F \circ \varphi_i\inv)(\bm u_i),
                                      D(\psi \circ F \circ \varphi_i\inv)_{(\bm u_i)}(\bm v_i)).

.. _tsuboi05.4.5.3:

* 問題 4.5.3: ユークリッド空間内の多様体 :math:`M \subset \RR^N` に対して
  :math:`TM` と :math:`X = \set{(x, v) \sth x \in M, v \in T_x M}` は微分同相である。

  * 点 :math:`\bm x^0 \in M` の近傍におけるグラフ表示から :math:`X` のグラフ表示を構成する。

    .. math::

       \bm x^0 = (\bm x_1^0, \bm x_2^0) \in \RR^p \times \RR^{N - p},

    :math:`\bm x_1^0 \in W` 上のグラフ表示 :math:`\fn{g}{W}\RR^{N - p},\ M \cap U = \set{(\bm x_1, g(\bm x_1)) \sth \bm x_1 \in W}`
    とすると :math:`\bm v \in T_{(\bm x_1, g(\bm x_1))}M \iff \bm v = (\bm v_1, Dg_{(\bm x_1)}\bm v_1)).`

    :math:`X \cap (U \times \RR^N) = \set{(\bm x_1, g(\bm x_1)), (\bm v_1, Dg_{(\bm x_1)}\bm v_1)) \sth (\bm u_1, \bm v_1) \in W \times \RR^p}.`

  * :math:`TM` は :math:`M` のパラメーター表示による被覆 :math:`\set{\Phi_i(W_i)}` について
    商空間 :math:`\bigcup W_i \times \RR^p` として定義されている。

  * 写像 :math:`(\bm u, \bm v) \longmapsto (\Phi_i(\bm u), {D\Phi_i}_{(\bm u)}(\bm v))` は連続であり、
    :math:`TM` の定義から逆写像もまた連続、:math:`C^\infty` 級である。
