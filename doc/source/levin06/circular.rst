======================================================================
Circular & Elliptical Shaping Functions
======================================================================

`Circular & Elliptical Shaping Functions - Golan Levin and Collaborators <http://www.flong.com/archive/texts/code/shapers_circ/>`__ ノート。
区間 :math:`{[0, 1]}` を定義域とする、ある種の二次式の平方根を利用する整形関数が紹介されている。

.. contents:: ノート目次

Circular Interpolation: Ease-In and Ease-Out
======================================================================

.. math::

   \begin{aligned}
   y &= 1 - \sqrt{1 - x^2}, && \text{ease-in interpolation},\\
   y &= \sqrt{1 - (1 - x^2)}, && \text{ease-out interpolation}.\\
   \end{aligned}

* 素早くコードを書ける。
* 平方根を使用しているため、計算効率は低い。

実装の急所：特になし。

Double-Circle Seat
======================================================================

.. math::

   y = \begin{cases}
   \sqrt{a^2 - (x - a)^2}, && 0 \lt x \lt a,\\
   1 - \sqrt{(1 - a)^2 - (a - x)^2}, && a \le x \le 1.\\
   \end{cases}

* 円弧二つを水平方向の接線で結合した形。
* 引数 :math:`a` は :math:`{(0, 1)}` の範囲にあり、単位正方形の対角線沿いに曲線の変曲点の位置を決定する。

実装の急所

* いつものように :math:`a` のチェックが必要。
* あらかじめ平方関数を書いておく。

Double-Circle Sigmoid
======================================================================

.. math::

   y = \begin{cases}
   a - \sqrt{a^2 - x^2}, && 0 \lt x \lt a,\\
   a + \sqrt{(1 - a)^2 - (x - 1)^2}, && a \le x \le 1.\\
   \end{cases}

* この sigmoid な整形関数は、円弧二つが垂直方向の接線で結合されることで形成される。
* 引数 :math:`a` は :math:`{(0, 1)}` の範囲にあり、単位正方形の対角線沿いに曲線の変曲点の位置を決定する。

実装の急所は前項と同じ。

Double-Elliptic Seat
======================================================================

.. math::

   y = \begin{cases}
   \dfrac{b}{a} \sqrt{a^2 - (x - a)^2}, && 0 \lt x \lt a,\\
   1 - \dfrac{1 - b}{1 - a} \sqrt{(1 - a)^2 - (x - a)^2}, && a \le x \le 1.\\
   \end{cases}

* このシート状の関数は、楕円弧二つが結合してできるもので、Double-Circle Seat の一般化だ。
* 楕円弧二つが点 :math:`{(a, b)}` で水平方向の接線で結合されている。

実装の急所は前項と同じ。

Double-Elliptic Sigmoid
======================================================================

.. math::

   y = \begin{cases}
   b \left(1 - \dfrac{\sqrt{a^2 - x^2} }{a} \right), && 0 \lt x \lt a,\\
   b + \dfrac{1 - b}{1 - a} \sqrt{(1 - a)^2 - (x - 1)^2}, && a \le x \le 1.\\
   \end{cases}

* この sigmoid な関数は、楕円弧二つが結合してできており、Double-Circle Sigmoid の一般化だ。
* 楕円弧二つが点 :math:`{(a, b)}` で垂直方向の接線で結合されている。

実装の急所は前項と同じ。

Double-Linear with Circular Fillet
======================================================================

この節には二本の直線を指定半径でフィレット処理するときのアルゴリズムが記述されている。
今回の目的には使わないのでノートを取らない。

Circular Arc Through a Given Point
======================================================================

この節には指定された三点を通過する円の作図アルゴリズムが記述されている。
今回の目的には使わないのでノートを取らない。
