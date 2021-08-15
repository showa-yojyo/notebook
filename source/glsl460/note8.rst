======================================================================
GLSL 4.60 仕様書 読書ノート 8 of ?
======================================================================

先に仕様書の内容をそっくりに写して、それから削る形でノートに仕上げたい。

.. contents:: ノート目次

8. Built-In Functions
======================================================================

OpenGL Shading Language はスカラーおよびベクトル演算についてさまざまな組み込み便利関数を定義する。
これらの組込み関数の多くは、複数の種類のシェーダーで使用することができるが、
ハードウェアに直接写像することを目的としたものも中にはあり、そのようなものは特定の種類のシェーダーでしか使用できない。

組み込み関数は、基本的に三つのカテゴリーに分類される：

* テクスチャーマップへのアクセスのように、必要なハードウェア機能を便利な方法で公開するもの。
  これらの関数をシェーダーで模倣する方法が言語にはないもの。
* 自明な操作 (``clamp``, ``mix``, etc.) を表現するもので、
  ユーザーが書くのがひじょうに簡単かつ、一般的なもので、ハードウェアが直接サポートしている場合もある。
  コンパイラーにとって式を複雑なアセンブラー命令に変換するのはとても難しい問題だ。
* グラフィックスのハードウェアがいずれは加速するであろう操作を表す式。
  三角関数はこのカテゴリーに入る。

多くの関数は、一般的な C ライブラリーにある同名の関数と似ているが、
従来のスカラー入力だけでなく、ベクトル入力もサポートしている。

組み込み関数は最適であると想定されているので、
アプリケーションは、自分のシェーダーコードで同等の計算を行うよりも、組み込み関数を使用するべきだ。
例えば、処理内容をハードウェアが直接サポートしている可能性がある。

同じ名前と引数リストを再宣言して定義するだけで、ユーザーコードが組み込み関数を自分のものに置き換えることができる。
組み込み関数はユーザー版関数よりも外側のスコープにあるため、これを行うと、
再宣言された関数と同じ名前の組み込み関数はすべて隠蔽される。

以下で仕様になる組み込み関数で、入力引数および対応する出力が

* ``float``, ``vec2``, ``vec3``, ``vec4`` の場合 ``genFType`` を、
* ``int``, ``ivec2``, ``ivec3``, ``ivec4`` の場合 ``genIType`` を、
* ``uint``, ``uvec2``, ``uvec3``, ``uvec4`` の場合 ``genUType`` を、
* ``bool``, ``bvec2``, ``bvec3``, ``bvec4`` の場合 ``genBType`` を、
* ``double``, ``dvec2``, ``dvec3``, ``dvec4`` の場合 ``genDType`` を

引数として使用する。

関数の特定の用途では ``genFType``, ``genIType``, ``genUType``, ``genBType``
に置き換わる実際の型は、すべての引数と戻り値の型に対して、同じ数の成分を持たなければならない。
同様に、

* ``mat`` は単精度成分を持つ任意の行列基本型に、
* ``dmat``は倍精度成分を持つ任意の行列基本型に

それぞれ使用される。

組込み関数には有効精度修飾がある。
この精度を明示的に設定することはできず、結果の精度とは異なる場合がある。

注意：一般的に、Vulkan を対象にしていない限り、精度修飾は無視される。

組み込み関数の演算の精度修飾は、その仮引数と実引数（入力引数）の精度修飾に基づいて行われる。
仮引数が精度修飾子を指定している場合はそれが使用され、
そうでない場合は実際の（呼び出し）実引数の精度修飾が使用される。
これらの中で最も高い精度が組み込み関数の演算の精度となる。
一般的に、これは組み込み関数のすべての実引数にわたって適用されるが、例外がある：

* ``bitfieldExtract`` と ``bitfieldInsert`` は引数 ``offset`` と ``bits`` を無視する。
* 関数 ``interpolateAt`` は引数 ``interpolant`` のみを見ます。

組み込み関数の結果の精度修飾は、以下のいずれかの方法で決定される：

テクスチャー採取、画像ロード、画像格納の各関数では、
戻り値型の精度はテクスチャーを混合した採取器型の精度と合致する：

.. code:: glsl

   uniform lowp sampler2D texSampler;
   highp vec2 coord;
   ...
   lowp vec4 col = texture (texSampler, coord); // texture() returns lowp

そうでなければ：

* 結果精度修飾子を指定しないプロトタイプでは、その精度は（先に定義したように）演算の精度と同じになる。
* 結果精度修飾子を指定するプロトタイプでは、指定された精度修飾子が結果精度修飾子となる。

以下の節の組み込み関数が方程式を指定する場合、式全体が演算の精度で評価される。
これにより、正しい結果が演算精度で表現できる場合であったとしても、
アンダーフローやオーバーフローが発生する可能性がある。

8.1. Angle and Trigonometry Functions
----------------------------------------------------------------------

角度として指定された関数の引数は弧度法単位だとみなされる。
これらの関数でゼロ除算エラーが発生することはない。除数が 0 の場合には結果は未定義となる。

これらはすべて成分ごとに演算する。記述は成分ごとに成り立つ。

.. admonition:: コメント

   この節以降も、ノートには関数シグニチャーをすべて記す。
   機能が自明なものについては演算仕様を書かない。

.. code:: glsl

   genFType radians(genFType degrees);
   genFType degrees(genFType radians);
   genFType sin(genFType angle);
   genFType cos(genFType angle);
   genFType tan(genFType angle);
   genFType asin(genFType x);
   genFType acos(genFType x);
   genFType atan(genFType y, genFType x);
   genFType atan(genFType y_over_x);
   genFType sinh(genFType x);
   genFType cosh(genFType x);
   genFType tanh(genFType x);
   genFType asinh(genFType x);
   genFType acosh(genFType x);
   genFType atanh(genFType x);

.. admonition:: コメント

   ``atan`` の引数を二つとる方は、よその言語では atan2 と呼ばれる。座標成分の順序はそれに準じている。

   ``atanh`` の記述に「結果は :math:`{x \ge 1}` の場合未定義だ」とあるが、
   おそらく :math:`{x \le -1}` の場合も未定義だと考えるのがいい。

8.2. Exponential Functions
----------------------------------------------------------------------

これらはすべて成分ごとに演算する。記述は成分ごとに成り立つ。

.. code:: glsl

   genFType pow(genFType x, genFType y);
   genFType exp(genFType x);
   genFType log(genFType x);
   genFType exp2(genFType x);
   genFType log2(genFType x);
   genFType sqrt(genFType x);
   genDType sqrt(genDType x);
   genFType inversesqrt(genFType x);
   genDType inversesqrt(genDType x);

.. admonition:: コメント

   ``exp2(x)`` は数学的には ``exp(2, x)`` を意味する。
   ``log2(x)`` も同じように ``log(2, x)`` と意味は同じだろう。
   ``inversesqrt(x)`` は ``1 / sqrt(x)`` を意味する。
   これらの「専用版」はおそらく「汎用版」よりもアルゴリズムが良いことが期待される。

8.3. Common Functions
----------------------------------------------------------------------

これらはすべて成分ごとに演算する。記述は成分ごとに成り立つ。

.. admonition:: コメント

   テキスト量が多いので、今度は関数シグニチャーをオーバーロード一つに絞って引用する。

.. glossary::

   ``genFType abs(genFType x)``, etc.
       よその言語によくあるものと同じ。

   ``genFType sign(genFType x)``, etc.
       引数の符号に応じて 1.0, 0.0, -1.0 を返す。

   ``genFType floor(genFType x)``, etc.
       よその言語によくあるものと同じ。

   ``genFType trunc(genFType x)``, etc.
       絶対値が ``x`` の絶対値よりも大きくないような、
       ``x`` に最も近い整数を（戻り値型で）返す。

   ``genFType round(genFType x)``, etc.
       ``x`` に最も近い整数を（戻り値型で）返す。
       端数 0.5 は、実装によって選択された方向に、おそらく最も速い方向に丸められる。
       ということは、すべての ``x`` の値に対して ``round(x) == roundEven(x)`` という可能性も含まれる。

   ``genFType roundEven(genFType x)``, etc.
       ``x`` に最も近い整数を（戻り値型で）返す。
       0.5 の小数部は、最も近い偶数の整数に丸められる。
       例えば 3.5 と 4.5 はどちらも 4.0 を返す。

   ``genFType ceil(genFType x)``, etc.
       よその言語によくあるものと同じ。

   ``genFType fract(genFType x)``, etc.
       ``return x - floor(x);``

   ``genFType mod(genFType x, float y)``, etc.
      ``return x - y * floor(x / y);`

   ``genFType modf(genFType x, out genFType i)``, etc.

       ``x`` の小数部を返し、
       ``i`` に整数部を ``genFType`` 型の値として代入する。
       戻り値と出力引数は、どちらも ``x`` と同じ符号になる。

   ``genFType min(genFType x, genFType y)``, etc.
       よその言語によくあるものと同じ。

   ``genFType max(genFType x, genFType y)``, etc.
       よその言語によくあるものと同じ。

   ``genFType clamp(genFType x, genFType minVal, genFType maxVal)``, etc.
       ``return min(max(x, minVal), maxVal);``
       ``minVal > maxVal`` なる引数に対しては結果は未定義だ。

   ``genFType mix(genFType x, genFType y, genFType a)``, etc.
       ``x`` と ``y`` の線形補間、つまり ``x * (1 - a) + y * a`` を返す。

   ``genFType mix(genFType x, genFType y, genBType a)``, etc.

       射影。

       ``a`` の成分が ``false`` の場合は、対応する ``x`` の成分を返す。
       ``a`` の成分が ``true`` の場合は、対応する ``y`` の成分を返す。
       選択されていない成分は、無効な浮動小数点値であることが許容され、結果には影響しない。

   ``genFType step(genFType edge, genFType x)``, etc.
       ``x < edge`` の場合は 0.0 を、そうでない場合は 1.0 を返す。

   ``genFType smoothstep(genFType edge0, genFType edge1, genFType x)``, etc.
       ``x <= edge0`` なら 0.0 を、
       ``x >= edge1`` なら 1.0 を返し、
       ``edge0 < x < edge1`` のときは 0 と 1 の間で滑らかな Hermite 補間を行う。
       滑らかな遷移をする閾値関数が欲しい場合にこれは便利だ。
       これは次と等価だ：

       .. code:: glsl

          genFType t;
          t = clamp ((x - edge0) / (edge1 - edge0), 0, 1);
          return t * t * (3 - 2 * t);

       ``edge0 >= edge1`` なる引数に対しては結果は未定義だ。

   ``genBType isnan(genFType x)``, etc.
       ``x`` が NaN である場合には ``true`` を返し、それ以外は ``false`` を返す。
       ``NaN`` が実装されていない場合は常に ``false`` を返す。

   ``genBType isinf(genFType x)``, etc.
       よその言語によくあるものと同じ。

   ``genIType floatBitsToInt(highp genFType value)``
   ``genUType floatBitsToUint(highp genFType value)``
       浮動小数点値の符号方式を表す符号付きまたは符号なしの整数値を返す。
       浮動小数点値のビットレベル表現は維持される。

   ``genFType intBitsToFloat(highp genIType value)``
   ``genFType uintBitsToFloat(highp genUType value)``
       浮動小数点値を符号付きまたは符号なしの整数で符号化したものに対応する浮動小数点値を返す。
       NaN が渡された場合、そのことを合図せず、結果の値は未定義だ。
       Inf が渡された場合、結果の値は対応する Inf になる。
       それ以外の場合はビットレベルの表現が維持される。

   ``genFType fma(genFType a, genFType b, genFType c)``, etc.
       ``return a * b + c;``
       戻り値が最終的に ``precise`` と宣言された変数で消費される用途では、

       * ``fma()`` は単一の演算とみなされる一方で、
         ``precise`` と宣言された変数で消費される式 ``a * b + c`` は二つの演算とみなされる。
       * ``fma()`` の精度は、式 ``a * b + c`` のそれとは異なる可能性がある。
       * ``fma()`` は ``precise`` 変数によって消費される他のどの ``fma()`` とも同じ精度で計算され、
         同じ入力値の ``a``, ``b``, ``c`` に対して不変の結果を与える。

       ``precise`` 消費がない場合、
       ``fma()`` と 式 ``a * b + c`` の間の演算数や精度の違いに特別な制約はない。

   ``genFType frexp(highp genFType x, out highp genIType exp)``
   ``genDType frexp(genDType x, out genIType exp)``
       範囲 :math:`{[0.5, 1.0]}` の浮動小数点の有効数字 (significand) と、2 の整数指数に ``x`` を分割する：

       :math:`x = s \times 2^{e}`

       有効数字はこの関数によって返され、指数は引数 ``exp`` に返される。
       浮動小数点の値が 0 の場合、有効数字と指数はともに 0 となる。

       実装が符号付きゼロをサポートしている場合、マイナスゼロの入力値はマイナスゼロの有効数字を返す必要がある。
       無限大であったり、数ではない浮動小数点値の場合、結果は未定義だ。

       入力がベクトルの場合、この演算は成分ごとに行われる。
       戻り値と ``exp`` に書き込まれる値は、引数 ``x`` と同じ数の成分を持つベクトルだ。

   ``genFType ldexp(highp genFType x, highp genIType exp)``
   ``genDType ldexp(genDType x, genIType exp)``
       ``x`` と、それに対応する ``exp`` の 2 の整数指数から、浮動小数点数を構築してそれを返す。

       この積が大きすぎて浮動小数点型で表現できない場合は、結果は未定義だ。

       for zero and all finite non-denormalized values.
       ``exp`` が単精度で +128 または倍精度で +1024 よりも大きい場合、戻り値は未定義だ。
       ``exp`` が単精度で -126 または倍精度で -1022 よりも小さい場合、戻り値はゼロに flush される可能性がある。
       さらに、
       ``frexp()`` を使って値を有効数字と指数に分割し、
       ``ldexp()`` を使って浮動小数点値を再構成すると、
       ゼロおよび有限非正規化値すべてに対して元の入力が得られるはずだ。

       入力がベクトルの場合、この演算は成分ごとに行われる。
       ``exp`` に渡された値と戻り値は、引数 ``x`` と同じ数の成分を持つベクトルとなる。

8.4. Floating-Point Pack and Unpack Functions
----------------------------------------------------------------------

これらの機能は成分単位ではなく、それぞれの場合で記述されるように動作する。

.. glossary::

   ``highp uint packUnorm2x16(vec2 v)``
   ``highp uint packSnorm2x16(vec2 v)``
   ``uint packUnorm4x8(vec4 v)``
   ``uint packSnorm4x8(vec4 v)``
       まず、正規化された浮動小数点値 ``v`` の各成分を 16 ビット (2x16)
       または 8 ビット (4x8) の整数値に変換する。
       そして、その結果を 32 ビットの符号なし整数にパックして返す。

       ``v`` の成分 ``c`` の固定小数点への変換は次のように行われる：

       * ``packUnorm2x16``: ``round(clamp(c, 0, +1) * 65535.0)``
       * ``packSnorm2x16``: ``round(clamp(c, -1, +1) * 32767.0)``
       * ``packUnorm4x8``: ``round(clamp(c, 0, +1) * 255.0)``
       * ``packSnorm4x8``: ``round(clamp(c, -1, +1) * 127.0)``

       ベクトルの最初の成分は出力の最下位ビットに、最後の成分は最上位ビットに書き込まれる。

   ``vec2 unpackUnorm2x16(highp uint p)``
   ``vec2 unpackSnorm2x16(highp uint p)``
   ``vec4 unpackUnorm4x8(highp uint p)``
   ``vec4 unpackSnorm4x8(highp uint p)``
       まず、32 ビット符号なし整数 ``p`` を、16 ビット符号なし整数の対、
       16 ビット符号あり整数の対、4 つの 8 ビット符号なし整数、
       4 つの 8 ビット符号あり整数にそれぞれアンパックする。
       その後、各成分を正規化された浮動小数点値に変換して、
       2 成分または 4 成分のベクトルを生成する。

       アンパックされた固定小数点値 ``f`` の浮動小数点への変換は次のように行われる：

       * ``unpackUnorm2x16``: ``f / 65535.0``
       * ``unpackSnorm2x16:``: ``clamp(f / 32767.0, -1, +1)``
       * ``unpackUnorm4x8``： ``F / 255.0``
       * ``unpackSnorm4x8``： ``clamp(f / 127.0, -1, +1)``

       返されたベクトルの最初の成分は、入力の最下位ビットから抽出され、
       最後の成分は最上位ビットから抽出される。

   ``uint packHalf2x16(vec2 v)``

      浮動小数点ベクトルの 2 成分を API の 16 ビット浮動小数点表現に変換し、
      その二つの 16 ビット整数を 32 ビット符号なし整数にパックした符号なし整数を返す。

      ベクトルの第一成分は結果の最下位 16 ビットを、第二成分は最上位 16 ビットを表す。

   ``vec2 unpackHalf2x16(uint v)``
       32 ビット符号なし整数を 16 ビット値の対に展開し、それらの値を
       API に従って 16ビット浮動小数点数として解釈し、
       32 ビット浮動小数点値に変換した成分を持つ二成分浮動小数点ベクトルを返す。

       ベクトルの第一成分と第二成分は ``v`` の最下位 16 ビットと最上位 16 ビットからそれぞれ得られる。

   ``double packDouble2x32(uvec2 v)``
       ``v`` の成分を 64 ビットの値にパックして得られる倍精度の値を返す。
       IEEE 754 Inf または NaN が作成された場合、それは信号を出さず、
       結果の浮動小数点値は未定義だ。
       それ以外の場合は ``v`` のビットレベルの表現が保存される。
       ベクトルの第一成分と第二成分は最下位 32 ビットと最上位 32 ビットをそれぞれ指定する。

   ``uvec2 unpackDouble2x32(double v)``
       ``v`` の符号なし整数二成分ベクトル表現を返す。
       ``v`` のビットレベル表現は保持される。
       ベクトルの第一成分と第二成分は ``double`` の最下位 32 ビットと最上位 32 ビットをそれぞれ含む。

8.5. Geometric Functions
----------------------------------------------------------------------

8.5.1. Refraction Equation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


8.6. Matrix Functions
----------------------------------------------------------------------


8.7. Vector Relational Functions
----------------------------------------------------------------------


8.8. Integer Functions
----------------------------------------------------------------------


8.9. Texture Functions
----------------------------------------------------------------------

8.9.1. Texture Query Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


8.9.2. Texel Lookup Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


8.9.3. Explicit Gradients
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


8.9.4. Texture Gather Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


8.9.5. Compatibility Profile Texture Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



8.10. Atomic Counter Functions
----------------------------------------------------------------------


8.11. Atomic Memory Functions
----------------------------------------------------------------------


8.12. Image Functions
----------------------------------------------------------------------


8.13. Geometry Shader Functions
----------------------------------------------------------------------


8.14. Fragment Processing Functions
----------------------------------------------------------------------

8.14.1. Derivative Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


8.14.2. Interpolation Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



8.15. Noise Functions
----------------------------------------------------------------------


8.16. Shader Invocation Control Functions
----------------------------------------------------------------------


8.17. Shader Memory Control Functions
----------------------------------------------------------------------


8.18. Subpass-Input Functions
----------------------------------------------------------------------


8.19. Shader Invocation Group Functions
----------------------------------------------------------------------
