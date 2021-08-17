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

これらは成分単位ではなく、ベクトルとして演算する。

.. glossary::

   ``float length(genFType x)``, etc.
       ベクトル ``x`` の長さを返す。

   ``float distance(genFType p0, genFType p1)``, etc.
       ``p0`` と ``p1`` の間の距離、すなわち ``length(p0 - p1)`` を返す。

   ``float dot(genFType x, genFType y)``, etc.
       ``x`` と ``y`` のスカラー積を返す。

   ``vec3 cross(vec3 x, vec3 y)``, etc.
       ``x`` と ``y`` のベクトル積を返す。

   ``genFType normalize(genFType x)``, etc.
       ``x`` と同じ方向だが、長さが 1 であるベクトル、つまり ``x / length(x)`` を返す。

   ``vec4 ftransform()`` compatibility profile only
       互換性プロファイルを使用している場合に限って有効だ。コア OpenGLでは ``invariant`` を使用しろ。
       頂点シェーダー限定。この関数は、入力される頂点値が OpenGL の固定機能変換で生成されるのと
       厳密に同じ結果を生成する方法で変換されることを保証する。
       これは ``gl_Position`` を計算する用途を意図している：

       .. code:: glsl

          gl_Position = ftransform()

       この関数は、例えば、アプリケーションが同じ幾何を別々のパスでレンダリングしていて、
       あるパスでは固定機能パスを使ってレンダリングし、
       別のパスではプログラム可能シェーダーを使っている場合などに使用するべきだ。

   ``genFType faceforward(genFType N, genFType I, genFType Nref)``, etc.
       ``dot(Nref, I) < 0`` の場合は ``N`` を、そうでない場合は ``-N`` を返す。

   ``genFType reflect(genFType I, genFType N)``, etc.
       入射ベクトル ``I`` と面方位 ``N`` に対して、反射方向 ``I - 2 * dot(N, I) * N`` を返す。
       ``N`` は正規化されている必要がある。

   ``genFType refract(genFType I, genFType N, float eta)``, etc.
       入射ベクトル ``I`` と曲面法線 ``N`` と屈折率の比 ``eta`` に対する
       屈折ベクトルを返す。この結果は屈折方程式 (:ref:`8.5.1. Refraction Equation`)
       によって算出される。

       ベクトル ``I`` と ``N`` は正規化されている必要がある。

8.5.1. Refraction Equation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: コメント

   方程式が書かれているが、これを書き直してここに載せたい。

8.6. Matrix Functions
----------------------------------------------------------------------

次の各組み込み行列関数には、単精度浮動小数点バージョンと倍精度浮動小数点バージョンがある。
仕様書本書では単精度浮動小数点バージョンに絞って記述しているが、本ノートではさらに絞る。

.. glossary::

   ``mat matrixCompMult(mat x, mat y)``
       行列 ``x`` に行列 ``y`` を成分ごとに乗算する。
       すなわち ``result[i][j] == x[i][j] * y[i][j]`` となる。

       注意：線形代数的な行列の乗算を行うには、乗算演算子 ``*`` を使用する。

   ``mat2 outerProduct(vec2 c, vec2 r)``,
   ...
   ``mat4x3 outerProduct(vec3 c, vec4 r)``
       ``c`` を列ベクトル、``r`` を行ベクトルとして扱い、
       線形代数的な行列乗算を行い、行数が ``c`` の構成要素の個数、
       列数が ``r`` の構成要素の個数である行列を生成する。

   ``mat2 transpose(mat2 m)``,
   ...
   ``mat4x3 transpose(mat3x4 m)``
       ``m`` の転置行列を返す。

   ``float determinant(mat2 m)``, etc.
       ``m`` の行列式を返す。

   ``mat2 inverse(mat2 m)``, etc.
       ``m`` の逆行列を返す。
       ``m`` が非正則行列または条件の悪い（ほぼ非正則の）場合、返される行列の値は未定義とする。

.. admonition:: コメント

   線形代数的な加法や乗法は、本文にも触れられているように、自然な演算子がサポートされている。

8.7. Vector Relational Functions
----------------------------------------------------------------------

関係演算子と比較演算子はスカラーを演算するように定義されており、スカラーの真偽型値を生成する。
ベクトルの結果を得るには次に述べる組み込み関数を使う。
以降では，一覧にある型に対して、次のプレースホルダーが使用されている：

.. csv-table::
   :delim: @
   :header: プレースホルダー, 許可される型
   :widths: , ,

   ``bvec`` @ ``bvec2``, ``bvec3``, ``bvec4``
   ``ivec`` @ ``ivec2``, ``ivec3``, ``ivec4``
   ``uvec`` @ ``uvec2``, ``uvec3``, ``uvec4``
   ``vec`` @ ``vec2``, ``vec3``, ``vec4``, ``dvec2``, ``dvec3``, ``dvec4``

どのような場合でも、どの呼び出しでも入力ベクトルすべてと戻り値ベクトルのサイズは一致しなければならない。

.. glossary::

   ``bvec lessThan(vec x, vec y)``, etc.
       演算 ``<`` の結果を成分ごとに行ったベクトルを返す。

   ``bvec lessThanEqual(vec x, vec y)``, etc.
       演算 ``<=`` の結果を成分ごとに行ったベクトルを返す。

   ``bvec greaterThan(vec x, vec y)``, etc.
       演算 ``>`` の結果を成分ごとに行ったベクトルを返す。

   ``bvec greaterThanEqual(vec x, vec y)``, etc.
       演算 ``>=`` の結果を成分ごとに行ったベクトルを返す。

   ``bvec equal(vec x, vec y)``, etc.
       演算 ``==`` の結果を成分ごとに行ったベクトルを返す。

   ``bvec notEqual(vec x, vec y)``, etc.
       演算 ``!=`` の結果を成分ごとに行ったベクトルを返す。

   ``bool any(bvec x)``
       成分のいずれかが ``true`` ならば ``true`` を返す。

   ``bool all(bvec x)``
       成分すべてが ``true`` である場合、かつその場合に限り ``true`` を返す。

   ``bvec not(bvec x)``
       単項演算 ``!`` の結果を成分ごとに行ったベクトルを返す。

.. admonition:: コメント

   仕様はひじょうに常識的なものだが、ベクトル成分ごとの論理演算をどういうときに使うのかまだわからない。

8.8. Integer Functions
----------------------------------------------------------------------

これらはすべて成分単位で演算をする。記述は成分ごとに対するものだ。
記号 ``[a, b]``とは、ビット番号 ``a`` からビット番号 ``b`` までのビットセットを意味する。
最下位のビットはビット 0 とする。最下位ビットから順に数え上げることをビット数と呼ぶ。

.. glossary::

   ``genUType uaddCarry(highp genUType x, highp genUType y, out lowp genUType carry)``
       32 ビット符号なし整数の加算 ``x + y`` をし、:math:`{2^{32}}` を基準とした和を返す。
       和が :math:`{2^{32}}` より小さければ値 ``carry`` は 0 に、そうでなければ 1 になる。

   ``genUType usubBorrow(highp genUType x, highp genUType y, out lowp genUType borrow)``
       32 ビット符号なし整数の減算 ``x - y`` をする。差が非負であれば差を、
       そうでなければ :math:`{2^{32}}` に差を加えた値を返す。
       値 ``borrow`` は ``x >= y`` の場合は 0 に、そうでなければ 1 になる。

   ``void umulExtended(highp genUType x, highp genUType y, out highp genUType msb, out highp genUType lsb)``
   ``void imulExtended(highp genIType x, highp genIType y, out highp genIType msb, out highp genIType lsb)``
       32 ビット符号なし/あり整数の乗算 ``x * y`` をする。
       64 ビットの結果を返す。
       最下位の 32 ビットが ``lsb`` に、最上位の 32 ビットが ``msb`` にそれぞれ返される。

   ``genIType bitfieldExtract(genIType value, int offset, int bits)``, etc.
       ``value`` からビット ``[offset, offset + bits - 1]`` を抽出して、結果の最下位ビットに返す。

       符号なしデータ型の場合、結果の最上位ビットには 0 がセットされる。
       符号ありデータ型の場合、結果の最上位ビットにビット ``offset + bits - 1`` がセットされる。

       ``bits`` が 0 の場合、結果は 0 にある。
       ``offset`` または ``bits`` が負の値の場合、
       または ``offset`` と ``bits`` の和がオペランドの格納に使用されたビット数よりも大きい場合、
       結果は未定義だ。
       ベクトルバージョンの ``bitfieldExtract()`` では、
       ``offset`` と ``bits`` の値の一対が、すべての成分で共有されることに注意。

   ``genIType bitfieldInsert(genIType base, genIType insert, int offset, int bits)``, etc.
       ``insert`` の最下位ビットを ``base`` に挿入する。

       結果は、``insert`` のビット ``[0, bits - 1]`` からビット ``[offset, offset + bits - 1]`` が取られ、
       その他のビットは ``base`` の対応するビットから直接取られる。

       ``bits`` が 0 の場合、結果は単に ``base`` になる。
       ``offset`` または ``bits`` が負の値の場合、
       または ``offset`` と ``bits`` の和がオペランドの格納に使用されたビット数よりも大きい場合、
       結果は未定義だ。
       ベクトルバージョンの ``bitfieldInsert()`` では、
       ``offset`` と ``bits`` の値の一対がすべての成分で共有されることに注意。

   ``genIType bitfieldReverse(highp genIType value)``, etc.
       ``value`` のビットを反転させる。結果のビット番号 ``n`` は、
       ``value`` のビット ``(bits - 1) - n`` から取られます。
       ここで ``bits`` とは値を表現するのに使用される全ビット数だ。

   ``genIType bitCount(genIType value)``, etc.
       ``value`` の二進表現における 1 が立っているビットの個数を返す。

   ``genIType findLSB(genIType value)``, etc.
       ``value`` の二進表現における最下位ビットのビット番号を返す。
       値がゼロの場合は -1 を返す。

   ``genIType findMSB(highp genIType value)``, etc.
       ``value`` の二進表現における最上位ビットのビット番号を返す。

       正の整数の場合、結果はビットが 1 である最も上位のビット番号になる。
       負の整数の場合、結果はビットが 0 である最も上位のビット番号になる。
       ``value`` がゼロまたは -1 ならば -1 を返す。

.. admonition:: コメント

   昔のドラクエのアセンブリコードを解析していたときにコードのノートを記録していた
   ときと感覚がよく似ている。

8.9. Texture Functions
----------------------------------------------------------------------

.. note::

    原文の英語を、次のように機械的に単語を日本語に読み換える：

    * level-of-detail: 詳細度

テクスチャー検索関数はすべてのシェーディング段階で利用可能だ。
ただし、詳細度はフラグメントシェーダーでのみ暗黙的に計算される。
その他のシェーダーは、基準となる詳細度がゼロとして計算されたかのように動作する。
後述の表の関数は、API で設定されたテクスチャー混合採取器を介したテクスチャーへのアクセスを提供する。
サイズ、画素フォーマット、次元数、フィルタリング方法、ミップマップレベル数、
奥行き比較などのテクスチャーの性質もまた API 呼び出しによって定義される。
このような性質は、以下に定義する組み込み関数を介してテクスチャーにアクセスする際に考慮される。

テクスチャーデータは、単精度浮動小数点、符号なし正規化整数、符号なし整数、
符号あり整数のいずれかのデータとして GL に格納される。
これはテクスチャーの内部フォーマットの種類によって決定される。

テクスチャー検索関数は、検索関数に渡された採取器型に応じて、
浮動小数点、符号なし整数、符号あり整数のいずれかで結果を返すことができる。
テクスチャーへのアクセスには、正しい採取器型を使用するように注意しなければならない。
以下の表は、サポートされている採取器型とテクスチャーの内部フォーマットの組み合わせを示す。
空白のエントリーはサポートされていない。
サポートされていない組み合わせの場合、テクスチャー検索を行うと未定義の値を返す。

奥行き・ステンシルテクスチャーの場合、内部テクスチャーフォーマットは
API を通じてセットとされるアクセスされる成分によって決定される。
奥行き・ステンシルテクスチャーモードが ``DEPTH_COMPONENT`` に設定されている場合は、
奥行き成分の内部フォーマットが使用される。
奥行き・ステンシルテクスチャーモードが ``STENCIL_INDEX`` に設定されている場合、
ステンシル成分の内部フォーマットが使用されるべきだ。

.. admonition:: コメント

   `本文の表 <https://www.khronos.org/registry/OpenGL/specs/gl/GLSLangSpec.4.60.html#texture-functions>`__

整数抽出器型の場合、テクスチャー検索の結果は ``ivec4`` だ。
符号なし整数の抽出器型が使用された場合、テクスチャー検索の結果は ``uvec4`` だ。
浮動小数点の抽出器型が使用されている場合、テクスチャー検索の結果は ``vec4`` だ。

以下のプロトタイプでは、戻り値型 ``gvec4`` の ``g`` は、
``vec4``, ``ivec4``, ``uvec4`` の戻り値の型を作る、無、
``i``, ``u`` のいずれかのプレースホルダーとして使用される。
これらの場合、抽出器引数の型も ``g`` で始まり、戻り値の型で行われたのと同じ置換を示します。
これは、上述のように、戻り値の型の基本的な型に合わせて、
単精度浮動小数点、符号あり整数、または符号なし整数の抽出器だ。

シャドウ形式（抽出器引数がシャドウ型）の場合、
抽出器に束縛された奥行きテクスチャーの奥行き比較検索は、
OpenGL 仕様書 8.23 "Texture Comparison Modes" で説明されているように行われる。
どの成分が :math:`D_{ref}` を指定しているかについては以下の表にある。
抽出器に束縛されたテクスチャーは奥行きテクスチャーでなければならず、そうでなければ結果は未定義となる。
奥行き比較をオンにした状態で、奥行きテクスチャーを表現する抽出器に非シャドウテクスチャーの呼び出しが行われた場合、
結果は未定義となる。
奥行き比較がオフになっている奥行きテクスチャを表す抽出器にシャドウテクスチャーの呼び出しが行われた場合、
結果は未定義となる。
奥行きテクスチャーを表現していない抽出器に対してシャドウテクスチャーの呼び出しが行われた場合、
結果は未定義となる。

以下の関数のすべてで、フラグメントシェーダーの場合、引数 ``bias`` はオプションだ。
引数 ``bias`` は他のシェーダー段階では受け付けられない。
フラグメントシェーダーでは ``bias`` が存在する場合、テクスチャーアクセス操作を行う前に、
暗黙の詳細度に追加される。
矩形テクスチャー、多重採取テクスチャー、テクスチャバッファーの場合、
ミップマップが許可されていないため ``bias`` や ``lod`` はサポートされていない。

暗黙の詳細度は次のように選択される：
ミップマップされていないテクスチャーの場合、そのテクスチャーが直接使用される。
ミップマップされていてフラグメントシェーダーで実行されている場合、
実装によって計算された詳細度がテクスチャーの検索に使用される。
ミップマップされていて非フラグメントシェーダーで実行されている場合は、基準テクスチャーが使用される。

テクスチャー関数（非 Lod および非 Grad バージョン）の中には、
暗黙的な微分係数を必要とするものがある。
暗黙的な微分係数は、非一様制御フロー内および
非フラグメントシェーダーのテクスチャーを取ってくるものでは未定義だ。

``Cube`` 形式の場合、OpenGL 仕様書の 8.13 "Cube Map Texture Selection" で説明されているように、
``P`` の方向はニ次元テクスチャーの検索をどの面で行うかを選択するために使用される。

``Array`` 形式の場合、使用される配列レイヤーは次のようになる：

| max(0, min(d − 1, ⌊layer + 0.5⌋))

ここで ``d`` はテクスチャー配列の奥行きで、
``layer`` は以下の表に示された成分のものだ。

8.9.1. Texture Query Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

関数 ``textureSize``はテクスチャー混合抽出器に対して特定のテクスチャーレベルの寸法を問い合わせる。

関数 ``textureQueryLod`` はフラグメントシェーダーでしか利用可能でない。
これらの関数は ``P`` の成分を取り、テクスチャーパイプが通常のテクスチャー検索で
そのテクスチャーにアクセスするために使用する詳細度情報を計算する。
詳細度 :math:`\lambda^{\prime}`（OpenGL 仕様書の式 3.18）は、
詳細度バイアスの後、範囲 ``[TEXTURE_MIN_LOD, TEXTURE_MAX_LOD]`` に clamp するのに先立って得られる。
また、アクセスされるミップマップ配列も計算される。
詳細度一つにアクセスする場合は、基準レベルに対する詳細度の番号が返される。
複数の詳細度にアクセスする場合は、二つのレベルの間の浮動小数点数が返され、
その小数部分は、計算され clamp された詳細度の小数部分に等しい。

.. admonition:: コメント

   使用されるアルゴリズムが疑似コードで示されているが略。

値 ``maxAccessibleLevel`` は、ミップマップ配列の最小のアクセス可能なレベルのレベル番号
（OpenGL 仕様書の 8.14.3 "Mipmapping" の ``q`` 値）から基準レベルを引いたものだ。

.. glossary::

   ``int textureSize(gsampler1D sampler, int lod)``,
   ...
   ``ivec3 textureSize(gsampler2DMSArray sampler)``
       OpenGL 仕様の 8.11 "Texture Queries" に述べられている、抽出器 ``sampler`` に束縛されたテクスチャーの詳細度 ``lod`` の寸法を返す（存在すれば）。
       戻り値の成分には、テクスチャーの幅、高さ、奥行きが順に埋められる。

       配列形式の場合、戻り値の最後の成分は、テクスチャー配列のレイヤー数、またはテクスチャーキューブマップ配列のキューブ数となる。

   ``vec2 textureQueryLod(gsampler1D sampler, float P)``,
   ...
   ``vec2 textureQueryLod(samplerCubeArrayShadow sampler, vec3 P)``
       戻り値の ``x`` 成分に、アクセスされるミップマップ配列を返す。

       基準レベルに対する計算された詳細度を戻り値の ``y`` 成分に返す。

       不完全なテクスチャーに対して呼び出された場合の結果は未定義だ。

   ``int textureQueryLevels(gsampler1D sampler)``,
   ...
   ``int textureQueryLevels(samplerCubeArrayShadow sampler)``
       ``sampler`` に関連付けられたテクスチャーでアクセス可能なミップマップレベルの数を返す。

       ``sampler`` にテクスチャーが関連付けられていない場合や不完全なテクスチャーの場合は、値 0 を返す。

       すべてのシェーダー段階で利用可能。

   ``int textureSamples(gsampler2DMS sampler)``,
   ``int textureSamples(gsampler2DMSArray sampler)``
       ``sampler`` に束縛されているテクスチャーの標本数を返す。

8.9.2. Texel Lookup Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. glossary::

   ``gvec4 texture(gsampler1D sampler, float P [, float bias] )``,
   ...
   ``float texture(sampler2DArrayShadow sampler, vec4 P)``,
   ...
   ``float texture(samplerCubeArrayShadow sampler, vec4 P, float compare)``
       テクスチャー座標 ``P`` を使って、現在 ``sampler`` に束縛されているテクスチャーの検索を行う。

       シャドウ形式の場合：引数 ``compare`` がない場合は、座標 ``P`` の最後の成分が
       :math:`D_{ref}` として使用され、配列レイヤーは ``P``の最後から 2 番目の成分から生成される。
       ``P`` の 2 番目の成分は 1D シャドウ検索では使用されない。

       シャドウ以外の形式の場合：配列レイヤーは ``P`` の最後の成分から来る。

   ``gvec4 textureProj(gsampler1D sampler, vec2 P [, float bias] )``, ...
   ``gvec4 textureProj(gsampler2DRect sampler, vec3 P)``, ...
       投影によるテクスチャー検索を行う。
       ``P`` の最後の成分を含まない、
       ``P`` から消費されるテクスチャー座標は、
       ``P`` の最後の成分で除算され、投影座標 :math:`P^{\prime}` を形成する。
       その結果、シャドウ形式における ``P`` の第 3 成分が :math:`D_{ref}` として使用される。
       ``P`` の第 3 成分は ``sampler`` の型が ``gsampler2D`` で、
       ``P`` の型が ``vec4`` の場合には無視される。
       これらの値が計算された後、テクスチャー検索は ``texture`` の場合と同様に行われる。

   ``gvec4 textureLod(gsampler1D sampler, float P, float lod)``, etc.
       ``texture`` のようにテクスチャー検索を行うが、明示的な詳細度を持つ：
       ``lod`` は :math:`\lambda_{base}` を指定し、偏微分を次のようにセットする：

       .. todo::

          偏微分の式を TeX で書く。

       OpenGL 仕様 8.14 "Texture Minification" と同式 8.4-8.6 を参照。

   ``gvec4 textureOffset(gsampler1D sampler, float P, int offset [, float bias] )``, ...
   ``gvec4 textureOffset(gsampler2DRect sampler, vec2 P, ivec2 offset)``, ...
   ``float textureOffset(sampler1DShadow sampler, vec3 P, int offset [, float bias] )``, ...
   ``float textureOffset(sampler2DArrayShadow sampler, vec4 P, ivec2 offset)``
       各テクセルを検索する前に ``(u, v, w)`` テクセル座標に ``offset`` を追加して、
       ``texture`` と同様にテクセル検索を行う。
       オフセット値は定数表現でなければならない。
       限られた範囲のオフセット値がサポートされている。
       オフセット値の最小値と最大値は実装依存であり、
       それぞれ ``gl_MinProgramTexelOffset`` と ``gl_MaxProgramTexelOffset`` で与えられる。

       なお、オフセットはテクスチャー配列のレイヤー座標には適用されない。
       これについては OpenGL 仕様の 8.14.2 "Coordinate Wrapping and Texel Selection"
       で詳しく説明されており、オフセットは :math:`{(\delta_u, \delta_v, \delta_w)}` となる。
       なお、キューブマップに対してはテクセルオフセットはサポートされていない。

   ``gvec4 texelFetch(gsampler1D sampler, int P, int lod)``, ...
   ``gvec4 texelFetch(gsampler2DRect sampler, ivec2 P)``, ...
   ``gvec4 texelFetch(gsampler1DArray sampler, ivec2 P, int lod)``, ...
   ``gvec4 texelFetch(gsamplerBuffer sampler, int P)``,
   ``gvec4 texelFetch(gsampler2DMS sampler, ivec2 P, int sample)``, ...
       整数テクスチャー座標 ``P`` を使用して ``sampler`` からテクセル一つを検索する。
       配列レイヤーは、配列形式に対する ``P`` の最後の成分から来る。
       詳細度 ``lod`` が存在する場合は、OpenGL 仕様 11.1.3.2 "Texel Fetches"
       および 8.14.1 "Scale Factor and Level of Detail" に記述のあるとおりだ。

   ``gvec4 texelFetchOffset(gsampler1D sampler, int P, int lod, int offset)``, etc.
       ``texelFetch`` と同様に単一のテクセルを ``textureOffset`` で記述されたように
       ``offset`` を使って取ってくる。

   ``gvec4 textureProjOffset(gsampler1D sampler, vec2 P, int offset [, float bias] )``, ...
   ``gvec4 textureProjOffset(gsampler2DRect sampler, vec3 P, ivec2 offset)``, ...
   ``float textureProjOffset(sampler1DShadow sampler, vec4 P, int offset [, float bias] )``, ...
       ``textureProj`` に記述されているようにして投影テクスチャー検索を行い、
       ``textureOffset`` に記述されているようにして ``offset`` によるオフセットを行う。

   ``gvec4 textureLodOffset(gsampler1D sampler, float P, float lod, int offset)``, etc.
       明示的な詳細度でオフセットテクスチャー検索を行う。
       ``textureLod`` および ``textureOffset`` を参照。

   ``gvec4 textureProjLod(gsampler1D sampler, vec2 P, float lod)``, etc.
       明示的な詳細度で投影テクスチャー検索を行う。
       ``textureProj`` と ``textureLod`` を参照。

   ``gvec4 textureProjLodOffset(gsampler1D sampler, vec2 P, float lod, int offset)``, etc.
       明示的な詳細度でオフセット射影テクスチャー検索を行う。
       ``textureProj``, ``textureLod``, ``textureOffset`` を参照。

   ``gvec4 textureGrad(gsampler1D sampler, float P, float dPdx, float dPdy)``, etc.
       ``texture`` のようにしてテクスチャー検索を行うが、以下の明示的な勾配を使う。
       ``P`` の偏微分は、ウィンドウ ``x`` とウィンドウ ``y`` に関する。
       キューブバージョンでは ``P`` の偏導関数は、テクスチャー座標が適切なキューブ面に投影される前に使用される座標系にあると仮定する。

   ``gvec4 textureGradOffset(gsampler1D sampler, float P, float dPdx, float dPdy, int offset)``, etc.
       ``textureGrad`` と ``textureOffset`` で説明されているように、
       明示的な勾配とオフセットの両方を持つテクスチャー検索を行う。

   ``gvec4 textureProjGrad(gsampler1D sampler, vec2 P, float dPdx, float dPdy)``, etc.
       ``textureProj`` で記述されているように、射影的に、
       また ``textureGrad`` で記述されているように明示的に勾配を用いて、
       テクスチャー検索を行う。
       偏微分 ``dPdx`` と ``dPdy`` はすでに投影されているものとする。

   ``gvec4 textureProjGradOffset(gsampler1D sampler, vec2 P, float dPdx, float dPdy, int offset)``, etc.
       ``textureProjGrad`` で記述されているように、投影された、明示的な勾配を持った、また、
       ``textureOffset`` で記述されているように、オフセットを持つ、テクスチャー検索を行う。

8.9.3. Explicit Gradients
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

前述の ``textureGrad`` 関数では、明示的な勾配は以下のようにテクスチャー検索を制御する。

.. admonition:: コメント

   `本文の数式 <https://www.khronos.org/registry/OpenGL/specs/gl/GLSLangSpec.4.60.html#explicit-gradients>`__

8.9.4. Texture Gather Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

テクスチャー収集関数は、単一の浮動小数点ベクトルオペランドの成分をテクスチャー座標として受け取り、
指定されたテクスチャー画像の基準詳細度から採取する四つのテクセルからなる集合を決定し、
テクセルそれぞれから一つの成分とって 4 成分結果ベクトルに返す。

テクスチャー収集操作を行う際には、最小化フィルターと拡大フィルターは無視され、
OpenGL 仕様の ``LINEAR`` フィルタリング規則がテクスチャー画像の基準レベルに適用され、
四つのテクセル :math:`{i_0 j_1, i_1 j_1, i_1 j_0, i_0 j_0}` を特定する。
これらのテクセルは 表 15.1 に従ってテクスチャー基準色 :math:`{(R_s, G_s, B_s, A_s)}` に変換され、
その後、OpenGL 仕様の 15.2.1 "Texture Access" で説明されているように、
テクスチャーかき混ぜが適用される。
四成分ベクトルは、かき混ぜた後のテクスチャーソース色のそれぞれから選択された成分を
:math:`{(i_0 j_1, i_1 j_1, i_1 j_0, i_0 j_0)}` の順に取ることで組み立てられる。

テクスチャー混合シャドウ抽出器型を使用するテクスチャー収集関数の場合、
四つのテクセル検索のそれぞれは、``(refZ)`` で渡された奥行き参照値との奥行き比較を行い、
その比較結果を結果ベクトルの適切な成分に返す。

他のテクスチャー検索関数と同様に、テクスチャー収集の結果は、

* シャドウ抽出器に対しては、参照されるテクスチャーが奥行きテクスチャーでないか、
  奥行き比較が無効になっている場合、または
* 非シャドウ抽出器に対しては、参照されるテクスチャーが深度比較を有効にした深度テクスチャである場合

には未定義だ。

.. glossary::

   ``gvec4 textureGather(gsampler2D sampler, vec2 P [, int comp])``, ...
   ``vec4 textureGather(sampler2DShadow sampler, vec2 P, float refZ)``, ...
       次を返す：

       .. code:: glsl

          vec4(Sample_i0_j1(P, base).comp,
               Sample_i1_j1(P, base).comp,
               Sample_i1_j0(P, base).comp,
               Sample_i0_j0(P, base).comp)

       指定された場合、引数 ``comp`` は 0, 1, 2, 3 のいずれかの値を持つ定整数式でなければならず、
       各テクセルの 4 成分ベクトル検索結果の ``x``, ``y``, ``z``, ``w`` のかき混ぜた後の成分をそれぞれ識別する。
       ``comp`` が指定されない場合は 0 として扱われ、各テクセルの ``x`` 成分を選択して結果を生成する。

   ``gvec4 textureGatherOffset(gsampler2D sampler, vec2 P, ivec2 offset, [ int comp])``, ...
   ``vec4 textureGatherOffset(sampler2DShadow sampler, vec2 P, float refZ, ivec2 offset)``, ...
   ``gvec4 textureGatherOffset(gsampler2DRect sampler, vec2 P, ivec2 offset [ int comp])``
   ``vec4 textureGatherOffset(sampler2DRectShadow sampler, vec2 P, float refZ, ivec2 offset)``
       ``offset`` が変数（非定数）であり、実装依存の最小および最大オフセット値がそれぞれ
       ``MIN_PROGRAM_TEXTURE_GATHER_OFFSET`` および ``MAX_PROGRAM_TEXTURE_GATHER_OFFSET``
       によって与えられることを除いて、
       ``textureOffset`` に記述されているように ``offset`` によって ``textureGather`` のようにテクスチャー収集操作を実行する。

   ``gvec4 textureGatherOffsets(gsampler2D sampler, vec2 P, ivec2 offsets[4] [, int comp])``, ...
   ``vec4 textureGatherOffsets(sampler2DShadow sampler, vec2 P, float refZ, ivec2 offsets[4])``, ...
   ``gvec4 textureGatherOffsets(gsampler2DRect sampler, vec2 P, ivec2 offsets[4] [, int comp])``
   ``vec4 textureGatherOffsets(sampler2DRectShadow sampler, vec2 P, float refZ, ivec2 offsets[4])``
       ``offsets`` が採取する四つのテクセルの位置を決定するために使用されることを除けば
       ``textureGatherOffset`` と同じように操作する。
       四つのテクセルそれぞれが ``offsets`` の対応するオフセットを ``(u, v)`` 座標オフセットとして ``P`` に適用し、
       四テクセルの ``LINEAR`` 足跡を特定し、その足跡のテクセル :math`i_0 j_0` を選択することで得られる。
       ``offsets`` に指定する値は、定整数式でなければならない。

8.9.5. Compatibility Profile Texture Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

以下のテクスチャー機能は、互換性プロファイルにしかない：

.. admonition:: コメント

   後回し。

8.10. Atomic Counter Functions
----------------------------------------------------------------------

この節の不可分カウンター操作は、互いに不可分に操作する。
つまり、あるシェーダー実体化のどの特定のカウンターに対するこれらの操作は、
別のシェーダー実体化の同じカウンターに対するこれらのどの操作とも不可分だ。
これらの操作がカウンターへの他のアクセス方法に対して不可分であることや、
別々のカウンターに適用されたときに直列化されることは保証されない。
このような場合、不可分性や直列性を求めるならば、フェンスやバリア、
あるいは他の形式の同期を追加的に使用する必要がある。

内在するカウンターは 32 ビットの符号なし整数だ。演算の結果は :math:{[0, 2^{32}-1]}` に折り返される。

.. glossary::

   ``uint atomicCounterIncrement(atomic_uint c)``
       不可分に

       1. ``c`` に対するカウンターをインクリメントして
       2. インクリメント操作に先立ってその値を返す。

       これら二つのステップは、この節の不可分カウンター関数に関しては不可分に行われる。

   ``uint atomicCounterDecrement(atomic_uint c)``
       上記関数のデクリメント版。

   ``uint atomicCounter(atomic_uint c)``
      ``c`` に対するカウンター値を返す。

   ``uint atomicCounterAdd(atomic_uint c, uint data)``
       不可分に

       1. ``c`` に対するカウンターに ``data`` を加算して
       2. その演算に先立ってその値を返す。

       これら二つのステップは、この節の不可分カウンター関数に関しては不可分に行われる。

   ``uint atomicCounterSubtract(atomic_uint c, uint data)``
       上記関数の減算版。

   ``uint atomicCounterMin(atomic_uint c, uint data)``
       不可分的に

       1. ``c`` に対するカウンターを、カウンターの値と ``data`` の値の最小値に設定して
       2. 演算に先立ってその値を返す。

       これら二つのステップは、この節の不可分カウンター関数に関しては不可分に行われる。

   ``uint atomicCounterMax(atomic_uint c, uint data)``
       上記関数の最大値版。

   ``uint atomicCounterAnd(atomic_uint c, uint data)``
       不可分的に

       1. ``c`` に対するカウンターを、カウンターの値と ``data`` の値のビットごとの論理積にセットして
       2. 演算に先立ってその値を返す。

       これら二つのステップは、この節の不可分カウンター関数に関しては不可分に行われる。

   ``uint atomicCounterOr(atomic_uint c, uint data)``
       上記関数の論理和版。

   ``uint atomicCounterXor(atomic_uint c, uint data)``
       上記関数の排他的論理和版。

   ``uint atomicCounterExchange(atomic_uint c, uint data)``
       不可分的に

       1. ``c`` に対するカウンター値を ``data`` の値にセットして
       2. 演算に先立ってその値を返す。

       これら二つのステップは、この節の不可分カウンター関数に関しては不可分に行われる。

   ``uint atomicCounterCompSwap(atomic_uint c, uint compare, uint data)``
       不可分的に

       1. ``compare`` の値と ``c`` に対するカウンター値を比較し、
       2. 値が等しければ ``c`` に対するカウンター値を ``data`` の値にセットして
       3. 演算に先立ってその値を返す。

       これら三つのステップは、この節の不可分カウンター関数に関しては不可分に行われる。

8.11. Atomic Memory Functions
----------------------------------------------------------------------

不可分記憶関数はバッファーオブジェクトまたは共有変数格納に格納された個々の符号あり
または符号なしの整数に対して不可分な操作を行う。
すべての不可分記憶操作は、メモリーから値を読み取り、以下に述べる操作のいずれかを使用して新しい値を計算し、
新しい値をメモリーに書き込み、読み取った元の値を返す。
不可分操作によって更新されるメモリーの内容は、元の値が読み込まれてから新しい値が書き込まれるまでの間、
シェーダーの呼び出しにおける他の割り当てや不可分記憶関数によって変更されないことが保証されている。

不可分記憶関数は限られた変数の集合に対してしかサポートされていない。
不可分記憶関数の ``mem`` 引数に渡された値が、バッファーや共有変数に対応していない場合、
シェーダーのコンパイルに失敗する。不可分記憶関数の ``mem`` 引数に配列の要素やベクトルの単一成分を渡しても、
そのもとになる配列やベクトルがバッファーや共有変数である限りは問題ない。

この節の組み込み関数はすべて、プロトタイプに記載されていないにもかかわらず、
``restrict``, ``coherent``, ``volatile`` 記憶修飾の組み合わせを持つ引数を受け入れる。
不可分操作は、組み込み関数の仮引数の記憶修飾ではなく、呼び出した引数のそれによって要求されたとおりに動作する。

.. glossary::

   ``uint atomicAdd(inout uint mem, uint data)``
   ``int atomicAdd(inout int mem, int data)``
       ``mem`` の内容に ``data`` の値を加えて新しい値を計算する。

   ``uint atomicMin(inout uint mem, uint data)``
   ``int atomicMin(inout int mem, int data)``
       ``data`` の値と ``mem`` の内容の最小値を取って新しい値を計算する。

   ``uint atomicMax(inout uint mem, uint data)``
   ``int atomicMax(inout int mem, int data)``
       上記の最大値版。

   ``uint atomicAnd(inout uint mem, uint data)``
   ``int atomicAnd(inout int mem, int data)``
       ``data`` の値と ``mem`` の内容をビットごとに論理積をとることで新しい値を計算する。

   ``uint atomicOr(inout uint mem, uint data)``
   ``int atomicOr(inout int mem, int data)``
       上記関数の論理和版。

   ``uint atomicXor(inout uint mem, uint data)``
   ``int atomicXor(inout int mem, int data)``
       上記関数の排他的論理和版。

   ``uint atomicExchange(inout uint mem, uint data)``
   ``int atomicExchange(inout int mem, int data)``
       ``data`` の値を単にコピーして新しい値を計算する。

   ``uint atomicCompSwap(inout uint mem, uint compare, uint data)``
   ``int atomicCompSwap(inout int mem, int compare, int data)``
       ``compare`` の値と ``mem`` の内容を比較する。
       値が等しい場合、新しい値は ``data`` で与えられ、
       そうでない場合は ``mem`` の元の内容から取得される。

8.12. Image Functions
----------------------------------------------------------------------

画像基本型のいずれかを使用する変数は、この節で定義する組み込みシェーダーの
画像記憶関数によって、テクスチャーの個々のテクセルを読み書きするために使用することができる。
各画像変数は、テクスチャー画像が取り付けられている画像単位を参照する。

画像メモリーがアクセスメモリー以下の機能を持つ場合、
画像中の個々のテクセルは ``P`` の値に対応する ``(i)``, ``(i, j)``, ``(i, j, k)`` のどれかの座標を用いて識別される。
多重標本テクスチャーに対応する ``image2DMS`` および ``image2DMSArray`` 変数
（およびそれに対応する ``int``/``unsigned int`` 型）では、
各テクセルが複数の標本を持つことがあり、個々の標本は整数の ``sample`` 引数を使って識別される。
座標と標本番号は OpenGL 仕様の 8.26 "Texture Image Loads and Stores" に記述されている方法で個々のテクセルを選択するのに使用される。

ロードとストアは浮動小数点数、整数、符号なし整数型をサポートする。
下にあるデータ型のうち ``gimage`` で始まるものは、
前節の ``"gvec"`` や ``"gsampler"`` と同様に、
``"image"``, ``"iimage"``, ``"uimage"`` のいずれかで始まる型を意味するプレースホルダーを果たす。

以下のプロトタイプの ``IMAGE_PARAMS`` は 33 個の別々の関数を表すプレースホルダーで、
それぞれが異なる型の画像変数に対応する。
``IMAGE_PARAMS`` のプレースホルダーは、以下の引数リストのいずれかで置き換えられる：

.. code:: glsl

   (gimage2D image, ivec2 P)
   (gimage3D image, ivec3 P)
   (gimageCube image, ivec3 P)
   (gimageBuffer image, int P)
   (gimage2DArray image, ivec3 P)
   (gimageCubeArray image, ivec3 P)
   (gimage1D image, int P)
   (gimage1DArray image, ivec2 P)
   (gimage2DRect image, ivec2 P)
   (gimage2DMS image, ivec2 P, int sample)
   (gimage2DMSArray image, ivec3 P, int sample)

ここで、各行は三種類の画像変数型のいずれかを表し、
``image``, ``P``, ``sample`` は操作する個々のテクセルを指定する。
``image``, ``P``, ``sample`` から操作する個々のテクセルを特定する方法、
およびテクセルの読み書き方法は、OpenGL 仕様 8.26 "Texture Image Loads and Store" で規定されている。

不可分関数は、画像変数の個々のテクセルまたは標本に対して操作を行う。
不可分記憶操作は、選択されたテクセルから値を読み取り、後述する操作のいずれかを使用して新しい値を計算し、
選択されたテクセルに新しい値を書き込み、読み取った元の値を返す。
不可分操作によって更新されるテクセルの内容は、元の値が読み込まれてから新しい値が書き込まれるまでの間に、
他の画像格納や不可分関数によって変更されないことが保証される。

不可分記憶操作は、すべての画像変数型の部分集合にしかサポートしない。
``image`` は以下のいずれかでなければならない：

* 符号あり整数画像変数（型が ``"iimage"`` で始まる）で、フォーマット修飾子が ``r32i`` であり、
  ``int`` 型の ``data`` 引数で使用される。
* 符号なし整数画像変数（型が ``"uimage"`` で始まる）で、フォーマット修飾子が ``r32ui`` であり、
  ``uint`` 型の ``data`` 引数で使用される。
a float image variable (type starts “image”) and a format qualifier of r32f, used with a data argument of type float (imageAtomicExchange only).
* 浮動小数点数画像変数（型がは ``"image"`` で始まる）で、フォーマット修飾子が ``r32f`` であり、
  ``float`` 型の ``data`` 引数で使用される。
  該当するのは ``imageAtomicExchange`` しかない。

この節の組み込み関数はすべて、プロトタイプに記載されていないにもかかわらず、
``restrict``, ``coherent``, ``volatile`` 記憶修飾の組み合わせを持つ引数を受け入れる。
画像操作は、組み込み関数の仮引数の記憶修飾ではなく、呼び出した引数のそれによって要求されたとおりに動作する。

.. glossary::

   ``int imageSize(readonly writeonly gimage1D image)``, etc.
       画像の寸法または ``image`` に束縛された画像の寸法を返す。
       配列された画像の場合、戻り値の最後の成分に配列のサイズが格納される。
       キューブ画像の場合は、一つの面の寸法と、
       配列されている場合はキューブマップ配列内のキューブの数しか返さない。
       注意: ``readonly writeonly`` という修飾語は、
       ``readonly`` と ``writeonly`` の両方で修飾された変数か、またはどちらの修飾もない変数を受け入れる。
       これは、仮引数が背後にあるメモリーの読み取りにも書き込みにも使用されないことを意味する。

   ``int imageSamples(readonly writeonly gimage2DMS image)``
   ``int imageSamples(readonly writeonly gimage2DMSArray image)``
       画像または ``image`` に束縛されている画像の標本数を返す。

   ``gvec4 imageLoad(readonly IMAGE_PARAMS)``
       画像単位 ``image`` から座標 ``P`` のテクセルをロードする。
       多重標本ロードの場合、標本番号は ``sample`` で与えられる。
       ``image``, ``P``, ``sample`` で有効なテクセルが特定されると、
       メモリー上で選択されたテクセルを表すビットは、
       OpenGL 仕様 8.26 "Texture Image Loads and Stores" で記述されている方法で、
       ``vec4``, ``ivec4``, ``uvec4`` に変換されて返される。

   ``void imageStore(writeonly IMAGE_PARAMS, gvec4 data)``
       ``image`` で指定された画像の座標 ``P`` のテクセルに ``data`` を格納する。
       多重標本格納の場合、標本番号を ``sample`` で指定する。
       ``image``, ``P``, ``sample`` で有効なテクセルが特定されると、
       データを表現するためのビットは、
       OpenGL 仕様 8.26 "Texture Image Loads and Stores" で記述されている方法で
       画像単位のフォーマットに変換され、指定されたテクセルに格納される。

   ``uint imageAtomicAdd(IMAGE_PARAMS, uint data)``
   ``int imageAtomicAdd(IMAGE_PARAMS, int data)``
       選択されたテクセルの内容に ``data`` の値を加算して新しい値を計算する。

   ``uint imageAtomicMin(IMAGE_PARAMS, uint data)``
   ``int imageAtomicMin(IMAGE_PARAMS, int data)``
       選択されたテクセルの内容と ``data`` の値との最小値を取ることで、新しい値を計算する。

   ``uint imageAtomicMax(IMAGE_PARAMS, uint data)``
   ``int imageAtomicMax(IMAGE_PARAMS, int data)``
       上記関数の最大値版。

   ``uint imageAtomicAnd(IMAGE_PARAMS, uint data)``
   ``int imageAtomicAnd(IMAGE_PARAMS, int data)``
       選択されたテクセルの内容と ``data`` の値とをビットごとに論理積をとることにより、新しい値を計算する。

   ``uint imageAtomicOr(IMAGE_PARAMS, uint data)``
   ``int imageAtomicOr(IMAGE_PARAMS, int data)``
       上記関数の論理和版。

   ``uint imageAtomicXor(IMAGE_PARAMS, uint data)``
   ``int imageAtomicXor(IMAGE_PARAMS, int data)``
       上記関数の排他的論理和版。

   ``uint imageAtomicExchange(IMAGE_PARAMS, uint data)``
   ``int imageAtomicExchange(IMAGE_PARAMS, int data)``
   ``float imageAtomicExchange(IMAGE_PARAMS, float data)``
       ``data`` の値を単にコピーして新しい値を計算する。

   ``uint imageAtomicCompSwap(IMAGE_PARAMS, uint compare, uint data)``
   ``int imageAtomicCompSwap(IMAGE_PARAMS, int compare, int data)``
       選択されたテクセルと ``compare`` の値と内容を比較する。
       値が等しい場合は新しい値が ``data`` で与えられ、
       そうでない場合はテクセルから読み込まれた元の値から取得される。

8.13. Geometry Shader Functions
----------------------------------------------------------------------

これらの機能は、幾何シェーダーでしか利用できない。

.. glossary::

   ``void EmitStreamVertex(int stream)``
       出力変数の現在の値を ``stream`` の現在の出力基本形状に放出する。
       ``stream`` 実引数は定整数でなければならない。
       この呼び出しから戻ると、出力変数すべての値は未定義だ。
       複数の出力ストリームがサポートされている場合にしか使用できない。

   ``void EndStreamPrimitive(int stream)``
       ``stream`` の現在の出力基本形状を完了し、新しいものを開始する。
       ``stream`` 実引数は定整数式でなければならない。頂点は放出されない。
       複数の出力ストリームがサポートされている場合にしか使用できない。

   ``void EmitVertex()``
       出力変数の現在の値を、現在の出力基本形状に出力する。
       複数の出力ストリームがサポートされている場合、これは ``EmitStreamVertex(0)`` を呼び出すことと等価だ。
       この呼び出しから戻ると、出力変数の値は未定義だ。

   ``void EndPrimitive()``
       現在の出力基本形状を完了し、新しいものを開始する。
       複数の出力ストリームがサポートされている場合、これは ``EndStreamPrimitive(0)`` を呼び出すことと等価だ。
       頂点は放出されない。

関数 ``EmitStreamVertex()`` は頂点が完成したことを指定する。
頂点は、ストリームに関連付けられた組み込みおよびユーザー定義の出力変数すべての現在の値を使用して、
頂点ストリーム ``stream`` の現在の出力基本形状に追加される。
``EmitStreamVertex()`` 呼び出し後は、出力ストリームすべてに対する出力変数すべての値が未定義だ。
幾何シェーダー呼び出しが、出力レイアウト修飾子 ``max_vertices`` で許可されている以上の頂点を放出していた場合、
``EmitStreamVertex()`` 呼び出しの結果は未定義となる。

関数 ``EndStreamPrimitive()`` は、頂点ストリームの現在の出力基本形状が完了し、
その後の ``EmitStreamVertex()`` によって（同型の）新しい出力基本形状が開始することを指定する。
この関数は頂点を放出しない。
出力レイアウトが ``points`` と宣言されている場合、
``EndStreamPrimitive()`` の呼び出しはオプションだ。

幾何シェーダーは、ストリームそれぞれについて頂点のない出力基本形状の状態から始まる。
幾何シェーダーが停止すると、ストリームそれぞれの現在の出力基本形状が自動的に完成する。
幾何シェーダーが単一の基本形状しか書き込まないならば ``EndStreamPrimitive()`` を呼び出す必要はない。

複数出力ストリームは出力基本形状型が ``points`` と宣言されている場合に限りサポートされる。
``EmitStreamVertex()`` や ``EndStreamPrimitive()`` を呼び出す幾何シェーダーが
プログラムに含まれていて、その出力基本形状型が ``points`` でない場合は、
コンパイルエラーまたはリンクエラーとなる。

8.14. Fragment Processing Functions
----------------------------------------------------------------------

フラグメント処理機能はフラグメントシェーダーでしか利用できない。

8.14.1. Derivative Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

微分は計算的に高く付き、数値的に不安定な場合がある。
そのため、実装では、高速だが完全には正確ではない導関数の計算を使用して、
真の微分係数を近似することにしても構わない。非一様な制御フローでは、微分は未定義だ。

微分に期待される動作は、右・左微分を使って指定される。

.. admonition:: コメント

   ここに定義式が MathJax で定義されている。
   式 (1a) と (1b) が右微分係数、(2a) と (2b) が左微分係数の近似式に読める。
   本文参照。

単標本ラスタライズの場合、式 (1b)と (2b) で :math`{\dd{x} \le 1.0}.`
多重標本ラスタライズの場合、式 (1b)と (2b) で :math`{\dd{x} \le 2.0}.`

:math:`{\dd{F}\dd{y}}` も同様に近似される。

多重標本ラスタライズでは、任意のフラグメントまたは標本に対して、隣接するフラグメントまたは標本を考慮することができる。

典型的な例としては、2x2の正方形のフラグメントまたは標本を考慮し、
行ごとに独立した ``dFdxFine`` と列ごとに独立した ``dFdyFine`` を計算する一方で、
2x2 の正方形全体に対しては、単一の ``dFdxCoarse`` と単一の ``dFdyCoarse`` しか計算しないというものがある。
したがって、すべての二次の粗い導関数、
たとえば ``dFdxCoarse(dFdxCoarse(x))`` は、非線形の引数であっても 0 になる可能性がある。
しかし、二次微分、例えば ``dFdxFine(dFdyFine(x))`` は、
2x2 正方形内で計算された独立した微分の差を適切に反映する。

この方法は、スクリーン座標ではなく、ウィンドウ座標によって変わるという制約のもと、
フラグメントごとに異なっていても構わない。
OpenGL 仕様 14.2 "Invariance" に記述されている不変性の要件は、微分計算では緩和されているが、
これはメソッドがフラグメント位置の関数である可能性があるためだ。

一部の実装では、GL ヒント（OpenGL 仕様 21.4 "Hints" 参照）を与えることで、
``dFdx`` および ``dFdy`` の微分精度を変化させ、ユーザーが画質と速度のトレードオフを行えるようにしている。
これらのヒントは ``dFdxCoarse``, ``dFdyCoarse``, ``dFdxFine``, ``dFdyFine`` には影響しない。

.. glossary::

   ``genFType dFdx(genFType p)``
       ``dFdxFine(p)`` または ``dFdxCoarse(p)`` のいずれかを返す。
       これは実装上の選択に基づいており、おそらくどちらか速い方、
       または品質と速度のヒントを通じて API が選択する方によって行われる。

   ``genFType dFdy(genFType p)``
       上記の ``y`` 版。

   ``genFType dFdxFine(genFType p)``
       ウィンドウ ``x`` 座標に関する ``p`` の偏微分を返す。
       現在のフラグメントとそのすぐ隣のフラグメントの ``p`` の値に基づいて、局所差分を使用する。

   ``genFType dFdyFine(genFType p)``
       上記の ``y`` 版。

   ``genFType dFdxCoarse(genFType p)``
       ウィンドウ ``x`` 座標に対する ``p`` の偏微分を返す。
       現在のフラグメントの隣接する部分の ``p`` の値に基づいて局所的な差分をとり、
       現在のフラグメントの ``p`` の値を含める場合もあるが、必ずしもそうはしない。
       つまり、与えられた領域では、実装は ``dFdxFine(p)`` で許容されるよりも
       少なく一意的な位置で微分を計算することができる。

   ``genFType dFdyCoarse(genFType p)``
       上記の ``y`` 版。

   ``genFType fwidth(genFType p)``
       ``abs(dFdx(p)) + abs(dFdy(p))`` を返す。

   ``genFType fwidthFine(genFType p)``
       ``abs(dFdxFine(p)) + abs(dFdyFine(p))`` を返す。

   ``genFType fwidthCoarse(genFType p)``
       ``abs(dFdxCoarse(p)) + abs(dFdyCoarse(p))`` を返す。

8.14.2. Interpolation Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

組み込み補間関数は、シェーダー指定の ``(x, y)`` 位置でフラグメントシェーダーの
入力変数の補間値を計算するために利用できる。
組み込み関数を呼び出すたびに別の ``(x, y)`` 位置が使用され、
それらの位置は入力の既定値を生成するために使用される既定の ``(x, y)`` 位置とは異なる場合がある。

すべての補間関数において ``interpolant`` は ``in`` 宣言の左辺値でなければならない。
``in`` 宣言には、変数、ブロックまたは構造体のメンバー、配列要素、またはこれらの組み合わせが含まれる。
さらに、成分選択演算子 (``.xy``, ``.xxz``, etc.) を ``interpolant`` に適用することができる。
この場合、補間関数は ``interpolant`` の値に成分選択演算子を適用した結果を返す。
例えば ``interpolateAt(v.xxz)`` は ``interpolateAt(v).xxz`` を返すように定義されている。
配列された入力は、一般的な（非一様）整数表現でインデックスを付けることができる。

``interpolant`` が ``flat`` 修飾子付きで宣言されている場合、
補間された値は単一基本形状に対してどこでも同じ値になる。
そのため、補間に使用される位置は影響せず、関数は同じ値を返すだけだ。
``interpolant`` が ``centroid`` 修飾子付きで宣言されている場合、
``interpolateAtSample()`` と ``interpolateAtOffset()`` が返す値は、
通常 ``centroid`` 修飾子で使われる位置を無視して、指定された位置で評価されます。
``interpolant`` が ``noperspective`` 修飾子付きで宣言された場合、
補間された値は遠近法補正なしで計算される。

.. glossary::

   ``float interpolateAtCentroid(float interpolant)``, etc.
       処理されている画素と基本形状の両方の内側の位置で採取された入力 ``interpolant`` 関数の値を返す。
       得られる値は、修飾子 ``centroid``を付けて宣言された場合、入力変数に割り当てられた値と同じになる。

   ``float interpolateAtSample(float interpolant, int sample)``, etc.
       標本番号 ``sample`` の位置にある入力 ``interpolant`` 変数の値を返す。
       多重標本バッファーが利用できない場合、入力変数は画素の中心で評価される。
       標本 ``sample`` が存在しない場合、入力変数の補間に使用される位置は未定義だ。

   ``float interpolateAtOffset(float interpolant, vec2 offset)``, etc.
       ``offset`` で指定された画素の中心からのオフセットで採取された入力 ``interpolant`` の値を返す。
       ``offset`` の浮動小数点成分二つは、それぞれ ``x`` 方向と ``y`` 方向の画素単位のオフセットを表す。

       オフセットが ``(0, 0)`` の場合は画素の中心を表す。
       この関数がサポートするオフセットの範囲と粒度は実装依存だ。

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
