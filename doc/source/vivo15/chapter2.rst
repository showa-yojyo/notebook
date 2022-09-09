======================================================================
Algorithmic drawing
======================================================================

.. contents:: ノート目次

Shaping functions
======================================================================

個人的にはこの章が本書の神髄であると評価している。シェーダー以外にもつぶしが効く。

* 一次元の関数を作る方法を理解する。
* 最初の二つのライブコードでプロットの描画方法がわかる。
  なお、線形補間の処理には GLSL 関数 ``mix`` を利用できる。
* 0 から 1 の値を黒から白の間の灰色に線形に対応させる。

--------------

演習問題

* ``pow`` に代えて ``exp``, ``log``, ``sqrt`` を試せ。

解答

何も工夫しないと定義域と値域の都合で ``exp`` と ``log`` ではプロット曲線が現れない。
実引数である ``st.x`` に下駄を履かせる。

Step and Smoothstep
----------------------------------------------------------------------

これまでの人生で一度も有効活用したことがない関数だ。
これらは断片シェーダーの実装でたいへん活躍する。

* この節で取り扱う GLSL 関数二つは補間に用いる。
  細工しなければ定義域は実数全体、値域は閉区間 :math:`{[0, 1]}` となる。
* 関数 ``step(edge, x)``: 階段関数。

  * シェーダーコードにおいては条件分岐、たとえば ``if`` 文の回避に使うことも多い。

* 関数 ``smoothstep(a, b, x)``: 三次関数。これらの関数を補間に応用する。

  * 例えば ``smoothstep(a, a + d, x) - smoothstep(a + d, a + 2 * d, x)`` でベルカーブ。

この段階では関数の合成にまだ踏み込まない。踏み込んだほうが良かった。

Sine and Cosine
----------------------------------------------------------------------

値が :math:`{[-1, 1]}` にある滑らかな関数として利用する。

* 関数 ``sin(x)`` など。三角関数の波長と振幅の調整法。

  * サインカーブの ``floor`` と ``ceil`` の和を取ると -1, 1 を取るデジタル信号になる。

* 関数 ``abs(x)`` や ``fract(x)`` で合成すること。

--------------

演習問題

* ``sin`` を計算する前に ``x`` に時間 ``u_time`` を加えろ。
* ``sin`` を計算する前に ``x`` に ``PI`` を掛けろ。位相が縮小し、各周期が 2 ごとに繰り返されるだろう。
* 時間 ``u_time`` を ``x`` に乗じてから ``sin`` を計算しろ。
  位相間の周波数がますます圧縮されていくだろう。
* ``sin(x)`` に 1.0 を加えろ。すべての波が上にずれて、すべての値が 0.0 から 2.0 の間になっているだろう。
* ``sin(x)`` に 2.0 を掛けろ。振幅が倍になる。
* ``sin(x)`` の絶対値 (``abs()``) を計算しろ。弾んだボールの跡のようになるだろう。
* ``sin(x)`` の結果の小数部分 (``fract()``) だけを取り出せ。
* ``sin(x)`` の結果の整数の大きい方(``ceil()``) と小さい方 (``floor()``) を足すと、
  1 と -1 の値のデジタル波になる。

回答

この練習では ``u_time`` がすでに大きくなっていて、プロットが読みづらくなっている可能性がある。
そこは適当に工夫する。要点をまとめると：

* ``sin`` の引数に定数を掛けると、波が横方向に伸縮する。引数の絶対値を大きくすると縮む。
* ``sin`` に定数を掛けると、波が縦方向に伸縮する。係数の絶対値を大きくすると伸びる。
* ``fract`` の結果は少々驚く。これのおかげで「小数部分」の定義を明確に習得できた。
* ``ceil`` と ``floor`` の加工では、実は離散的に値 :math:`\pm 2` が生じる。

Some extra useful functions
----------------------------------------------------------------------

関数 ``mod``, ``fract``, ``sign``, ``clamp``, ``min``, ``max`` を体で覚える。

* ``mod(x, y)`` の定義を言えるようにしておく必要がある。
* ``sign(x)`` は -1, 0, 1 のいずれかを返す。この 0 が便利な場合とそうでない場合がある。

====================== ===============================================
関数呼び出し           プロット
====================== ===============================================
``mod(x, 0.5)``        いわば半三角波。連続部分は単調増加。
``fract(x)``           これも半三角波だが上のものの倍の三角形を描く。
``ceil(x)``            上り階段。 :math:`{[-1, 1]}` を通る。
``floor(x)``           上り階段。 :math:`{[0, 1]}` を通る。
``sign(x)``            左が -1 右が 1 の奇関数。ただし原点は例外。
``abs(x)``             V 字を描く。
``clamp(x, 0.0, 1.0)`` :math:`{[0, 1]}` だけ上り坂になる。あとは直線。
``min(0.0, x)``        上り坂から平らに変化。
``max(0.0, x)``        平らから上り坂に変化。
====================== ===============================================

Advance shaping functions
----------------------------------------------------------------------

これら単体でノートのページが丸々埋まるのでまともに取り組むか悩む。

* `Polynomial Shaping Functions - Golan Levin and Collaborators <http://www.flong.com/archive/texts/code/shapers_poly/>`__
* `Exponential Shaping Functions - Golan Levin and Collaborators <http://www.flong.com/archive/texts/code/shapers_exp/>`__
* `Circular & Elliptical Shaping Functions - Golan Levin and Collaborators <http://www.flong.com/archive/texts/code/shapers_circ/>`__
* `Bezier and Other Parametric Shaping Functions - Golan Levin and Collaborators <http://www.flong.com/archive/texts/code/shapers_bez/>`__
* `Inigo Quilez :: fractals, computer graphics, mathematics, shaders, demoscene and more <https://www.iquilezles.org/www/articles/functions/functions.htm>`__

Exercise
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

単純な数式の関数を習得して損はないだろう。
関数 ``pow`` を多用するので関数 ``abs`` も併用するようだ。
非負だとわかっている合成関数ならば ``abs`` 呼び出しを省略する。

.. code:: glsl

   y = 1. - sqrt(abs(x));
   y = 1. - abs(x);
   y = 1. - x * x;

For your toolbox
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Grapher (Mac only)
* `Graphtoy <https://graphtoy.com/>`__: これは良い。ノートにペンでスケッチする手間が省ける。
* `Shadershop <http://tobyschachman.com/Shadershop/editor/>`__: 操作が難しい。

一変数関数プロットツールということなら Matplotlib や SymPy で事足りる。

Colors
======================================================================

* ``vec3``, ``vec4`` のメンバーのアクセス方法
* ベクトル成分に対する swizzling と呼ばれるアクセス方法

--------------

次のようなスニペットを愛用しているテキストエディターに仕込んでおけとある：

.. code:: text

   vec3($1, $2, $3)
   vec4($1, $2, $3, ${4:1.0})

Mixing color
----------------------------------------------------------------------

* 関数 ``mix`` で二つの値をパーセンテージで混合できる。線形内分補間。
* こういう関数も利用できる：\ `Easing Functions Cheat Sheet <https://easings.net/>`__

Playing with gradients
----------------------------------------------------------------------

* 関数 ``mix`` は ``float`` 型だけでなく、同型の ``vecN`` を渡すこともできる。

--------------

演習問題

* ターナーの夕日をイメージしたグラデーションを作成しろ。
* ``u_time`` を使って、日の出と日没の間をアニメーションにしろ。
* これまでに学んだことを使って虹を作れ。
* 関数 ``step`` を使ってカラフルな旗を作れ。

解答

ターナーの課題は三色使いたい。線形グラデーションをうまく指定する。
水平方向の座標成分についてはどうでもいい。

.. code:: glsl

   vec3 skyblue = vec3(.5294, .8078, .9216);
   vec3 white = vec3(1., 1., 1.);
   vec3 darkorange = vec3(1., 0.59, 0.);

   void main() {
       vec2 st = gl_FragCoord.xy / u_resolution.xy;
       float height = fract(st.y * 2.);
       vec3 color = step(-.5, -st.y) * mix(darkorange, white, height)
           + step(.5, st.y) * mix(white, skyblue, height);
       // ...
   }

アニメーションのは中間地点を時刻とともに下方向へ移動させる方針で行く。

.. code:: glsl

   float sunset = fract(u_time);
       vec2 st = gl_FragCoord.xy / u_resolution.xy;
       vec3 color = step(-sunset, -st.y) * mix(
           darkorange, white, fract(st.y) / sunset) +
           step(sunset, st.y) * mix(
               white, skyblue, mix(st.y - sunset, 1., st.y - sunset));
       // ...

虹は次のようなコードになる。曲線を描くのは頑張ればこの時点でもできるが……。
原色の中間が暗いのがいやならば、さらなる色を定義して補間処理を追加すればいいのだが、
その問題は次の節で解決する。

.. code:: glsl

   vec3 red = vec3(1., 0., 0.);
   vec3 green = vec3(0., 1., 0.);
   vec3 blue = vec3(0., 0., 1.);

   void main() {
       vec2 st = gl_FragCoord.xy / u_resolution.xy;
       float N = 3.;
       vec3 color
           = (step(0., st.y) - step(1./N, st.y)) * mix(red, green, st.y * N)
           + (step(1./N, st.y) - step(2./N, st.y)) * mix(green, blue, (st.y - 1./N) * N)
           + (step(2./N, st.y) - step(3./N, st.y)) * mix(blue, red, (st.y - 2./N) * N);
       // ...
   }

上のコードの ``mix`` 部分を色ベクトルで置き換えるとカラフルな旗になる。

HSB
----------------------------------------------------------------------

* 関数 ``rgb2hsv`` と ``hsv2rgb`` の実装。このコードはよそにも用意されているだろう。
* ``rgb = rgb*rgb*(3.0-2.0*rgb)`` の式は Hermite 補間、すなわち
  ``smoothstep`` に見える。

HSB in polar coordinates
----------------------------------------------------------------------

* HSB は極座標で考えるのが普通。したがって関数 ``length`` や ``atan`` が有用。
* GLSL ベクトルに対しては次のような関数も用意されている：

  * `length <https://thebookofshaders.com/glossary/?search=length>`__
  * `distance <https://thebookofshaders.com/glossary/?search=distance>`__
  * `dot <https://thebookofshaders.com/glossary/?search=dot>`__
  * `cross <https://thebookofshaders.com/glossary/?search=cross>`__
  * `normalize <https://thebookofshaders.com/glossary/?search=normalize>`__
  * `faceforward <https://thebookofshaders.com/glossary/?search=faceforward>`__
  * `reflect <https://thebookofshaders.com/glossary/?search=reflect>`__
  * `refract <https://thebookofshaders.com/glossary/?search=refract>`__
  * `lessThan <https://thebookofshaders.com/glossary/?search=lessThan>`__
  * `lessThanEqual <https://thebookofshaders.com/glossary/?search=lessThanEqual>`__
  * `greaterThan <https://thebookofshaders.com/glossary/?search=greaterThan>`__
  * `greaterThanEqual <https://thebookofshaders.com/glossary/?search=greaterThanEqual>`__
  * `equal <https://thebookofshaders.com/glossary/?search=equal>`__
  * `notEqual <https://thebookofshaders.com/glossary/?search=notEqual>`__

--------------

演習問題

* 待機中マウスカーソルみたいなものを描け。
* HSB から RGB への変換機能と一緒に shaping 機能を使い、
  特定の色相値を拡大し、それ以外の色相値を縮小しろ。
* RYB 色空間版のカラーピッカーのパレットを描け。
* *Interaction of Color* (Josef Albers, 2006) を読み、問題文の下にあるシェーダー例を練習として使え。

解答

マウスカーソルの問題は次の一行を加えれば十分：

.. code:: glsl

   color *= step(0.5, radius) - step(0.75, radius);

色相拡縮だが、少しむずかしい。まず条件を少し特殊化したものを考える：

* 特定の色相 :math:`h` を 0.5 に固定する。
* :math:`d` をゼロに十分近い正数とおき、

  * 拡大する色相を :math:`{[h - d, h + d)}` に含まれものとする。
  * 縮小する色相を :math:`{[0, d) \cup [1 - d, 1)}` に含まれるものとして固定する。

* 拡縮を一次関数によって変換する。

ロジックをスケッチすると次のようになる。初版：

.. code:: glsl

   // Map the angle (-PI to PI) to the Hue (from 0 to 1)
   // and the Saturation to the radius
   float hue = angle / TWO_PI + 0.5;

   float d = 0.1;
   float x1 = d;
   float x2 = 1. - d;
   float y1 = (1. - d) * .5;
   float y2 = (1. + d) * .5;

   if(0. <= hue && hue < x1){
       hue = mix(0., y1, hue/d);
   }
   else if(x1 <= hue && hue < x2){
       hue = mix(y1, y2, (hue - x1) / (x2 - x1));
   }
   else{
       hue = mix(y2, 1., (hue - x2) / (1. - x2));
   }

   color = hsb2rgb(vec3(hue, radius, 1.0));

ここから条件分岐などをシェーダーらしく書き直す：

.. code:: glsl

   float pulse(float a, float b, float x){
       return step(a, x) - step(b, x);
   }

として関数 ``pulse`` を定義すると一連の ``if`` 文を次の式に置き換えられる：

.. code:: glsl

   hue = pulse(0., x1, hue) * mix(0., y1, hue/d)
       + pulse(x1, x2, hue) * mix(y1, y2, (hue - x1) / (x2 - x1))
       + pulse(x2, 1., hue) * mix(y2, 1., (hue - x2) / (1. - x2));

各項をさらに関数化する。

.. code:: glsl

   float slope(float x1, float x2, float y1, float y2, float hue){
       return pulse(x1, x2, hue) * mix(y1, y2, (hue - x1) / (x2 - x1));
   }

   // ...

   hue = slope(0., x1, 0., y1, hue)
       + slope(x1, x2, y1, y2, hue)
       + slope(x2, 1., y2, 1., hue);

RYB 問題は上の回答を変形させれば解けるだろう。

Interaction of Color 問題はよくわからない。コードを見て終わりとするしかない。

* 関数 ``rect`` は後ほど登場する。
* ここでの ``mix`` と ``step`` の使い方は基本的なので、確実に習得したい。
  ``mix`` の入れ子から分岐処理が見える。
* なるほど ``st.y = 1. - st.y`` とすれば上下逆になる。
* 対称な位置にある矩形二つを一度の関数呼び出しで描けるのは面白い。

Note about functions and arguments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GLSL の関数引数リストの ``in``, ``out``, ``inout`` について。

Shapes
======================================================================

単純な図形を並列に描く手法を習得する。

Rectangle
----------------------------------------------------------------------

* 関数 ``step`` を二次元的に採用して矩形を定義する方法

  * L 型を反復する方法
  * ロ型を反復する方法

.. code:: glsl

   vec2 bl = step(vec2(0.1), st); // bottom-left
   vec2 tr = step(vec2(0.1), 1.0 - st); // top-right
   color = vec3(bl.x * bl.y * tr.x * tr.y);

--------------

演習問題

* 矩形のサイズと比率を変更しろ。
* ``step`` の代わりに ``smoothstep`` を使って実験しろ。ぼやけたエッジからエレガントで滑らかな境界線になる。
* ``floor`` を使った別の実装を考えろ。
* 最も気に入った実装を選び、将来的に再利用できるようにその関数を作れ。関数は柔軟で効率的なものにしろ
* 矩形の輪郭を描くだけの別の関数を作れ。
* 同じキャンバスの中で、異なる矩形を移動したり配置したりするにはどうしたらいいか。
  方法がわかったらモンドリアンのような平面構成をして自分の技術を誇示しろ。

解答

この問題から、関数 ``step`` を使える場合には ``smoothstep`` で置き換わるかどうかを考えると良いことがわかる。

次のように ``floor`` を使うと同じ結果が得られる：

.. code:: glsl

   vec2 bl = floor(0.9 + st);
   vec2 tr = floor(1.9 - st);

キャンバス全域を矩形で囲む関数 ``rectangle`` を定義する。
柔軟にすることを要求されているが、初版なので色々と決め打ちする。
線幅や矩形のサイズ、位置を引数リストに追加することが考えられる。

.. code:: glsl

   float rectangle(vec2 st, float border_width){
       vec2 border = vec2(max(0.01, border_width));
       // bottom-left
       vec2 bl = step(border, st);
       float pct = bl.x * bl.y;

       // top-right
       vec2 tr = step(border, 1.0 - st);
       pct *= tr.x * tr.y;
       return pct;
   }

単純塗りつぶしバージョン。以前定義した関数 ``pulse`` を用いる。

.. code:: glsl

   float rectangle(vec2 st, vec2 bl, vec2 tr){
       return pulse(bl.x, tr.x, st.x) * pulse(bl.y, tr.y, st.y);
   }

複数の異なる矩形を描くのは条件を与えれば容易だ：

* 背景は黒とする。
* どの矩形も白とする。

これならば上記の ``rectangle`` を呼び出した戻り値をその都度 ``max`` を取っていけばいい。
矩形に色が着いていたり、相異なる矩形が重なり合うことを考えると問題が難しくなる。

Circles
----------------------------------------------------------------------

* 円を描く方法

--------------

演習問題

* そこから何が推測できるのか。
* これを使ってどのように円を描くことができるか。
* 上のコードを修正して、円のグラデーション全体をキャンバス内に収めろ。

解答

当然だが、固定点から距離が一定であるピクセルだけを他の色で描けば円が現れる。

.. code:: glsl

   float d = .01;
   vec3 color = 1. - vec3(step(.5 - d, pct) - step(.5, pct));

いつものように ``smooth`` に代えて ``smoothstep`` を使うと描線が滑らかになる。

グラデーション全体をキャンバス内に収めるだけならば次のように修正すれば十分：

.. code:: glsl

   vec3 color = vec3(pct) * 2.;

Distance field
----------------------------------------------------------------------

距離場の概念：平面から非負実数への写像という解釈でよかろう。

--------------

演習問題

* ``step`` を使って、0.5 以上のものを白に、以下のものを黒にしろ。
* 背景と前景の色を反転させろ。
* ``smoothstep`` を使って、円の境界線が滑らかになるように様々な値を試せ。
* 満足のいく実装ができたら、将来的に再利用できるように、その関数を用意しろ。
* 円に色を与えろ。
* 円が大きくなったり小さくなったりするのをアニメーションで表現して、
  心臓の鼓動を真似てみろ。
* この円を動かすのはどうか。移動させて、キャンバスに異なる円を配置することはできるか。
* 異なった関数や操作を使って、距離場を組み合わせるとどうなるか。
* この技法を使って三つの合成を作れ。アニメーションがあればなお良し。

解答

白と黒はそれぞれ ``vec3(1, 1, 1)``, ``vec3(0, 0, 0)`` だから：

.. code:: glsl

   // Turn everything above 0.5 to white and everything below to black
   vec3 color = vec3(step(.5, pct));

   // Invert the color
   color = 1. - color;

関数 ``smoothstep`` を使うのはよくやるのでもう大丈夫だろう。

.. code:: glsl

   float radius = .5;
   float line_width = .01;
   vec3 color = vec3(smoothstep(radius - line_width, radius, pct) - smoothstep(radius, radius + line_width, pct));

関数として定義するのはまだ早い。引数リストが確定してからだ。

色を付けるのは単に好きな色を成分ごとの乗算をすればいい。

.. code:: glsl

   vec3 line_color = vec3(1., 0., 0.);
   // ...
   color *= line_color;

円を伸び縮みさせるには、上のコード片で言うところの ``radius`` を ``u_time`` の関数にすればよい。
振幅が小さめの周期関数を採用すると良い。解答略。

円を動かすとは、文脈上円の中心を運動させるという意味しか残っていない。
円の中心を運動させるには、\ ``distance`` の行の実引数を工夫すればいい。

.. code:: glsl

   pct = distance(st,vec2(0.5 - .25 * sin(u_time), 0.5 + .1 * sin(u_time)));

以下略。

For your tool box
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``sqrt`` を可能な限り避けて ``dot`` で済ませる。
これは GLSL に限らず幾何学プログラミング全般での基本だ。

Useful properties of a Distance Field
----------------------------------------------------------------------

距離場を用いて何らかの視覚的表現を実装することはよくある。

Polar shapes
----------------------------------------------------------------------

正規化された座標 ``st`` からキャンバスの中心を原点とする極座標空間の座標 ``(r, theta)`` を得る公式：

.. code:: glsl

   vec2 pos = vec2(0.5) - st;
   float r = length(pos) * 2.0;
   float theta = atan(pos.y, pos.x);

--------------

演習問題

* これらの形状をアニメーションにしろ。
* さまざまな shaping 関数を組み合わせて形状に穴を開け、花や雪の結晶、歯車などを作れ。
* 前章で使用した関数 ``plot`` を使って輪郭だけを描け。

解答

アニメーションは色々考えられるが、偏角 ``a`` またはプロット ``f`` を ``u_time`` で加工するのが普通だろう。

.. code:: glsl

   const float TAU = radians(360.);

   void main(){
       // ...

       float a = atan(pos.y, pos.x) - mod(u_time, TAU);
   }

穴をあける問題は少し手を抜いて、白を白で引くと黒になることを利用する：

.. code:: glsl

   float a = atan(pos.y,pos.x) + u_time;

   // ...

   float cog = smoothstep(-.5, 1., cos(a * 10.)) * 0.2 + 0.5;
   float hole = .2;

   color = vec3(1. - smoothstep(cog, cog + 0.02, r));
   color -= vec3(1. - smoothstep(hole, hole + 0.02, r));

プロットの問題は興味深い結果が得られる。前章で使用した実装はこういうものだった：

.. code:: glsl

   float plot(vec2 st, float pct){
       return smoothstep(pct - 0.02, pct, st.y) -
           smoothstep(pct, pct + 0.02, st.y);
   }

題意を好意的に解釈して極座標用に書き直すことにする：

.. code:: glsl

   float plot(float r, float pct){
       return smoothstep(pct - 0.02, pct, r) -
           smoothstep(pct, pct + 0.02, r);
   }

しかし、これをそのまま適用するとプロット曲線の太さが原点から遠ざかるほど太くなって不格好だ。
そこでこのように調整する。少しましになる：

.. code:: glsl

   float plot(float r, float pct){
       flot line_width = 0.02 / max(r, .001);
       return smoothstep(pct - line_width, pct, r) -
           smoothstep(pct, pct + line_width, r);
   }

Combining powers
----------------------------------------------------------------------

極座標を距離場に応用する。

--------------

演習問題

* この節の例を使って、正多角形の位置と頂点数を入力とし、距離場の値を返す関数を書け。
* ``min`` と ``max`` を使って距離場を混ぜ合わせろ。
* 幾何学的なロゴを選び、距離場を使って複写しろ。

解答

最初の問題はリファクタリングに過ぎない：

.. code:: glsl

   float regular_polygon(int N, float size, vec2 st){
       // Angle and radius from the current pixel
       float theta = atan(st.y, st.x) + PI;
       float radius = TWO_PI / float(N);

       // Shaping function that modulate the distance
       float d = cos(floor(.5 + theta / radius) * radius - theta) * length(st);
       float e = .01;
       return 1.0 - smoothstep(size - e, size + e, d);
   }

正多角形の最初の頂点が x 軸上に来るのか y 軸上に来るのかで ``atan`` 呼び出しの引数の順序を入れ替えるといい。
気に入らないのは、距離場の定義が良くないのか、頂点数によって多角形の半径がどんどん小さくなることだ。
これは正直なんとかしたい（ベクトルの問題ゆえ難しくはない）。

距離場の混ぜ合わせは ``max`` を取ると正多角形同士の和集合が現れ、\ ``min`` を取ると積集合が現れる。

幾何学的なロゴタイプで何かいいのがあれば試したい。

Matrices
======================================================================

Translate
----------------------------------------------------------------------

ここはいい。

Rotations
----------------------------------------------------------------------

ここはいい。

* この節で ``mat2``, ``mat3``, ``mat4`` を導入する。
* この TeX を書いたのは誰だろう。なっていない。
* ``mat2`` への引数の渡し方が本文の説明と GLSL のコードとで合致していない。
  GLSL では列ベクトルを並べる。このコードで見かけ上動作している理由は、
  世界座標系を回転させることで、相対的にオブジェクトが反時計回りするから。
  本ノートでは ``mat2(cos(t), sin(t), -sin(t), cos(t))`` の順で統一する。

--------------

演習問題

* 45 行目のコメントを外して、何が起こるか確かめろ。
* 37 行目と 39 行目の回転前と回転後の並進をコメントして、その結果を確かめろ。
* 回転を使って、並進の練習でシミュレーションしたアニメーションを改善しろ。

解答

45 行目のコメントを外すと背景にデバッグ色が着く。
これにより、座標変換がすべての画素に施されていることが納得できる。

``st += vec(0.5)`` などをコメントアウトすると、回転中心がキャンバスの左下のままになるのがわかる。

最後の問題は並進の練習では回転ベクトルを直接計算していたので、
そこを行列の乗算に置き換えろという趣旨だろう。
ただ、どう書き換えても以前のコードのほうが保守しやすいだろう。

Scale
----------------------------------------------------------------------

特にない。

--------------

演習問題

* 42 行目のコメントを外すと、空間座標が拡縮されているのがわかる。
* 37 行目と 39 行目の拡縮の前と後の並進をコメントするとどうなるか。
* 回転行列と拡縮行列を組み合わせろ。順番が重要であることに注意しろ。
* ニセの UI または HUD を設計して構築しろ。Ndel 氏による ShaderToy の\ `例 <https://www.shadertoy.com/view/4s2SRt>`__\ が参考になる。

解答

今回もオブジェクト座標系ではなく世界座標系に対して拡縮している。
したがって、拡縮前後の並進をやめると左下（の少しずれた位置）を中心に描画全体が拡縮する。

回転を組み合わせるのは ``scale`` の前か後ろになる。
いつものように世界座標系を回転させるので、次のコードは十字の形状を時計回りに回転する。

.. code:: glsl

   float t = u_time;
   float c = cos(t);
   float s = sin(t);
   mat2 R = mat2(c, s, -s, c);
   mat2 S = scale(vec2(0.5, 0.5));
   st = R * S * st;
   st += vec2(0.5);

HUD の問題は何を言っているのかわからない。

Other uses for matrices: YUV color
----------------------------------------------------------------------

YUV とは色空間の一種で、写真やビデオのアナログ符号化処理に使用される。
人間の知覚範囲を考慮して、C 成分の帯域を狭くしてある。

Patterns
======================================================================

* シェーダプログラムは画素単位で実行される。形状をどれだけ反復して計算回数は一定だ。
  したがって、断片シェーダーはタイルパターンに特に適していると言える。
* 正規化した二次元座標を拡大してから ``fract`` を適用する手法が基本的だ。
  これにより、正規化されたキャンバスを格子状に区切ることができる。

--------------

演習問題

* 空間にさまざまな数値を乗算しろ。浮動小数点の値を使ったり、\ ``x`` と ``y`` の値を変えろ。
* このタイリング手法を使って、再利用可能な関数を作れ。
* 空間を 3x3 に分けろ。画素がどのセルにあるかを知る方法を見つけ、それを使って表示される形を変えろ。
  三目並べを構成しろ。

解答

係数として特に次の性質の数を採用する：

* 整数でない浮動小数点数。上辺と右辺のタイルが部分しか描かれない。
* 負の数。色の分布が反転する。

成分ごとに係数を変えると、タイルに縦横比がつき、タイルの並ぶ個数が成分別に異なるようになる。

「キャンバスを横何個かける縦何個のタイル列に分割する」関数を定義する：

.. code:: glsl

   vec2 tile(float scalar, in vec2 st){
       return fract(scalar * st);
   }

   vec2 tile(in vec2 scalar, in vec2 st){
       return fract(scalar * st);
   }

これを使えばキャンバスを 3x3 に分割する処理は一行で記述できる：

.. code:: glsl

   tile(st, 3.);

``st`` がどのセルに属すかは、係数の逆数を整数倍した区間のどこに属するかで決まる。
例えば ``scalar = 3.`` とする。仮に ``1. / scalar <= st.x && st.x < 2. / scalar``
ならば ``st`` は中央の列のどこかにある。ただし ``st`` は係数倍される前の値とする。
GLSL なので ``floor`` が適任だ：

.. code:: glsl

   ivec2(floor(st * scalar))

さらにバツジルシを描く関数が必要だ。前章の ``cross`` を拝借すればできるだろう。
セルの条件分岐はどうする？

Apply matrices inside patterns
----------------------------------------------------------------------

各セルに対して前章で習った座標変換の手法を適用することができる。

--------------

演習問題

* このパターンをアニメーション化する面白い方法を考えろ。
  色、形、動きのアニメーションを考えろ。
  三種類のアニメーションを作れ。
* さまざまな形を合成して、より複雑なパターンを作り直せ。
* 異なるパターンのレイヤーを組み合わせて、独自のスコットランド風タータンパターンを作れ。

解答

その他の要素に関するアニメーションは学習済みなので、パターン自体をアニメーションするかどうかを中心に考えたい。

* 分割自体を時刻によって変化させる。このコードで言うと ``zoom`` への実引数を ``u_time`` 依存にする。
* 回転角を ``u_time`` に依存する。
* ボックスの色を ``u_time`` に依存する。

残りの問題は難しいから後回し。

Offset patterns
----------------------------------------------------------------------

関数 ``mod`` を利用した偶数奇数の判定方法を理解する。

.. code:: glsl

   y = step(1.0, mod(x, 2.0));

反復パターンに対するオフセット指定手法を理解する。
レンガの例では、奇数行のパターンだけ半ブロック分横にずらすという処理を示している。
関数 ``brickTile`` がそれを実現している。

.. code:: glsl

   st.x += step(1., mod(st.y, 2.0)) * 0.5;

--------------

演習問題

* これを時間に応じてオフセットを移動させろ。
* 偶数行が左に、奇数行が右に動くアニメーションを作れ。
* この効果を列でも再現できるか。
* X 軸と Y 軸のオフセットを組み合わせて、参考デモのように書き換えろ。

解答

関数 ``brickTile`` を順次機能拡張する方針をとる。引数 ``offset`` を追加する：

.. code:: glsl

   vec2 brickTile(vec2 st, float zoom, float offset){
       st *= zoom;
       st.x += step(1., mod(st.y, 2.0)) * offset;
       return fract(st);
   }

呼び出し箇所を修正する：

.. code:: glsl

   st = brickTile(st, 5.0, fract(u_time));

偶数奇数で互い違いにオフセットさせるには、偶数、奇数を
-1, 1 にそれぞれ写像することができれば十分だ。次のようにする：

.. code:: glsl

   vec2 brickTile(vec2 st, float zoom, float offset){
       st *= zoom;
       st.x += offset * (2. * step(.001, step(1., mod(st.y, 2.))) - 1.);
       return fract(st);
   }

列で再現するには上記の ``xy`` を ``yx`` に入れ替えた版を作る必要があるが、
この二つのバージョンを一つの関数にまとめられる：

.. code:: glsl

   vec2 brickTile(vec2 st, float zoom, float offset){
       st *= zoom;
       float limit = offset * .5;
       st += (offset * (2. * step(1., mod(st, 2.)) - 1.)
           // (1, 0) or (0, 1)
           * vec2(1. - step(.5, limit), step(.5, limit))).yx;
       return fract(st);
   }

呼び出しを例えば次のように変更する：

.. code:: glsl

   // Apply the brick tiling
   st = brickTile(st, 5.0, fract(u_time) * 2.);

Truchet Tiles
----------------------------------------------------------------------

一つのセルをもう一度四つ切りに細分する。次の処理を ``zoom`` の直後に行う：

.. code:: glsl

   //  Scale the coordinate system by 2x2
   st *= 2.;

   // Give each cell an index number
   // according to its position
   float index = step(1., mod(st.x, 2.)) + step(1., mod(st.y, 2.)) * 2.;

   //      |
   //  2   |   3
   //      |
   //--------------
   //      |
   //  0   |   1
   //      |

   // Make each cell between 0.0 - 1.0
   st = fract(st);

ここまでは分かり易い。次に細分されたセルの ``index`` に応じてパターンを変換する。

.. code:: glsl

   // Rotate each cell according to the index
   if(index == 1.){
       // Rotate cell 1 by 90 degrees
       st = rotate2D(st, PI * 0.5);
   } else if(index == 2.0){
       // Rotate cell 2 by -90 degrees
       st = rotate2D(st, PI * -0.5);
   } else if(index == 3.0){
       // Rotate cell 3 by 180 degrees
       st = rotate2D(st, PI);
   }

例によって ``if`` 文が気に入らないので ``step`` で書き換える。
神経質なようだが修練だと考えればいい。

.. code:: glsl

   st = fract(st);

   float theta1 = PI * 0.5;
   float theta2 = PI * -0.5;
   float theta3 = PI;
   float theta
       = theta1 * step(1., index)
       + (theta2 - theta1) * step(2., index)
       + (theta3 - theta2) * step(3., index);

   return rotate2D(st, theta);

--------------

演習問題

* 69 行目から 72 行目までをコメント、アンコメント、複製して新しいデザインを作れ。
* 黒と白の三角形を、半円、回転した四角形、線などの別の要素に変えろ。
* 要素の位置に応じて回転させる他のパターンをコードにしろ。
* 要素の位置に応じて他の性質が変化するパターンを作れ。
* この節の原則を適用できる、必ずしもパターンではない何か他のものを考えろ(例：易経の易卦）。

解答

コメント・アンコメント・コピー問題は色々試す。回転にアニメーションが施されているから、
二つの回転角をずらすと面白い効果を得る。

黒と白の三角形を生じているのは次に引用するコードの RGB 部分だ。これを今までのパターン定義関数に置き換える：

.. code:: glsl

   // step(st.x,st.y) just makes a b&w triangles
   // but you can use whatever design you want.
   gl_FragColor = vec4(vec3(step(st.x, st.y)), 1.0);

値 ``index`` に応じて「他の性質」を決めるコードを追加すればいいだろう。

最後の六十四卦をモチーフにしたパターンはコードが全部読めるのだが、コメントがないので理解に時間を要する。
有益な技法がいくつか埋め込まれているので、時間をかけて解読すれば得られるものがある。

Making your own rules
----------------------------------------------------------------------

手続き型パターンの作成は、再利用可能な最小限の要素を見つけるための精神的な訓練だと著者は主張している。

* 古代ギリシャの蛇行文様
* 中国の格子文様
* アラビアの幾何学模様
* アフリカのゴージャスな布地のデザイン

パターンの世界には学ぶべきものがたくさんあるとも言っている。
