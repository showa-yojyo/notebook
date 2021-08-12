======================================================================
GLSL 4.60 仕様書 読書ノート 5 of ?
======================================================================

だんだん翻訳だけで済ませるようになってきた。

.. contents:: ノート目次

5. Operators and Expressions
======================================================================

5.1. Operators
----------------------------------------------------------------------

.. admonition:: コメント

   順位、意味、記号、結合性からなる演算子表が本文ではここにある。
   馴染みがある C++ と酷似しているので省略。

アドレスを得る演算子や逆参照演算子はない。
型キャスト演算子はなく、代わりにコンストラクターが使われる。

5.2. Array Operations
----------------------------------------------------------------------

:ref:`5.7. Structure and Array Operations` にまとめられた。

5.3. Function Calls
----------------------------------------------------------------------

関数が値を返す場合、その関数への呼び出しは式として使用することができ、
その型は関数の宣言または定義 (:ref:`6.1. Function Definitions`) に使用された型になる。

5.4. Constructors
----------------------------------------------------------------------

コンストラクターは関数呼び出しの構文を使用しており、関数名は型であり、
呼び出しによってその型のオブジェクトを作成する。
コンストラクタは初期化子でも式でも同じように使われる (:ref:`9. Shading Language Grammar`)。
引数は構築された値を初期化するのに使用される。
コンストラクターは、あるスカラー型から別のスカラー型へのデータ型変換を要求したり、
小さな型からより大きな型を構築したり、大きな型を小さな型に縮小したりするのに使用できる。

一般的に、コンストラクターは、事前決定されたプロトタイプを持つ組み込み関数ではない。
配列と構造体の場合、各要素またはメンバーに対して厳密に一つの実引数がコンストラクター内にある必要がある。
他の型では、実引数は初期化を行うのに十分な数の成分を提供しなければならず、
すべてを使用できないほど多くの実引数を含めるとコンパイルエラーとなる。
詳細を今から述べていく。
以降のプロトタイプは実のところ、単なる例の部分集合だ。

5.4.1. Conversion and Scalar Constructors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

スカラー型同士の変換は、以下のプロトタイプが示すように行われる：

.. code:: glsl

   int(uint)     // converts an unsigned integer to a signed integer
   int(bool)     // converts a Boolean value to an int
   // etc.

コンストラクターを使用して浮動小数点型を整数型に変換する場合、
浮動小数点値の端数部分は抜け落ちる。負の浮動小数点値を ``uint`` 型に変換することは未定義だ。

単精度浮動小数点の仮数部よりも多くのビットの精度を持つ整数値は、
浮動小数点に変換すると精度が失われる。

整数型または浮動小数点型を ``bool`` に変換するコンストラクターを使用した場合、
0 および 0.0 は ``false`` に変換され、0 以外の値は ``true`` に変換される。
コンストラクターで ``bool`` を任意の整数型または浮動小数点型に変換する場合、
``false`` は 0 または 0.0 に変換され、
``true`` は 1 または 1.0 に変換される。

コンストラクター ``int(uint)`` は、引数のビットパターンを保持し、
その符号ビットが設定されている場合は、引数の値を変更する。
コンストラクター ``uint(int)`` は、引数のビットパターンを保持し、
負の値ならばその値を変更する。

``float(float)`` のような恒等コンストラクターも合法だが、ほとんど使用しない。

非スカラー引数を持つスカラーコンストラクターは、
非スカラーから最初の要素を取るために使用できる。たとえばコンストラクター
``float(vec3)`` は ``vec3`` 引数の第一成分を選択する。

.. admonition:: コメント

   やはり C++ の感覚で書けるようだ。

   最後で言及されている種のコンストラクターの何がうれしいのかは今のところわからない。

5.4.2. Vector and Matrix Constructors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コンストラクターをスカラー、ベクトル、または行列の集合から、
ベクトルまたは行列を作成するのに使用できる。これには、ベクトルを縮める（？）機能も含まれる。

ベクトルコンストラクターの引数が単一スカラーである場合、
構築されるベクトルのすべての成分はそのスカラー値で初期化される。
行列コンストラクターの引数が単一スカラーである場合、
行列の対角線上のすべての成分をそのスカラー値で初期化し、残りの成分は 0.0 に初期化される。

複数のスカラー、複数のベクトル、複数の行列、あるいはこれらの混合物からベクトル一つを構築する場合、
ベクトルの成分は実引数の成分から順番に構築される。
実引数は左から右へと消費され、各実引数は次の実引数の成分が消費される前に、
そのすべての成分が順に消費される。
複数のスカラー、ベクタトル、またはそれらの混合物から行列一つを構築する場合も同様だ。
行列の構成要素は列優先 (column-major) で構築され、消費される。
これらの場合、構築される値の成分すべてに初期化子を与えるには、
引数に十分な成分が与えられていなければならない。
最後に使用される実引数を超える余分な実引数を与えるとコンパイルエラーとなる。

行列から行列が構築される場合、引数に対応する成分（列 i, 行 j）を持つ
結果の各成分（同）はそこから初期化される。その他の成分はすべて単位行列に初期化される。
行列コンストラクターに行列の実引数が与えられた場合、それ以外の引数があるとコンパイルエラーとなる。

コンストラクターに対する引数の基本型 (``bool``, ``int``, ``float``, ``double``)
が、構築されるオブジェクトの基本型と一致しない場合は、
前述のスカラー構築規則を使って引数を変換する。

便利なベクトルコンストラクターには次のようなものがある：

.. code:: glsl

   vec3(float)          // initializes each component of the vec3 with the float
   vec4(ivec4)          // makes a vec4 with component-wise conversion
   vec4(mat2)           // the vec4 is column 0 followed by column 1
   vec2(float, float)   // initializes a vec2 with 2 floats
   ivec3(int, int, int) // initializes an ivec3 with 3 ints
   bvec4(int, int, float, float) // uses 4 Boolean conversions
   vec2(vec3)           // drops the third component of a vec3
   vec3(vec4)           // drops the fourth component of a vec4
   vec3(vec2, float)    // vec3.x = vec2.x, vec3.y = vec2.y, vec3.z = float
   vec3(float, vec2)    // vec3.x = float, vec3.y = vec2.x, vec3.z = vec2.y
   vec4(vec3, float)
   vec4(float, vec3)
   vec4(vec2, vec2)

これらの利用例を挙げる：

.. code:: glsl

   vec4 color = vec4(0.0, 1.0, 0.0, 1.0);
   vec4 rgba = vec4(1.0);      // sets each component to 1.0
   vec3 rgb = vec3(color);     // drop the 4th component

行列の対角成分を、他のすべての要素がゼロになるように初期化するには：

.. code:: glsl

   mat2(float)
   mat3(float)
   mat4(float)

.. admonition:: コメント

   これは先程言及があった。

ベクトルやスカラーを指定して行列を初期化する場合、成分は列優先で行列の要素に割り当てられる：

.. code:: glsl

   mat2(vec2, vec2);                 // one column per argument
   mat3(vec3, vec3, vec3);           // one column per argument
   mat4(vec4, vec4, vec4, vec4);     // one column per argument
   mat3x2(vec2, vec2, vec2);         // one column per argument
   dmat2(dvec2, dvec2);
   dmat3(dvec3, dvec3, dvec3);
   dmat4(dvec4, dvec4, dvec4, dvec4);
   mat2(float, float,                // first column
        float, float);               // second column
   mat3(float, float, float,         // first column
        float, float, float,         // second column
        float, float, float);        // third column
   mat4(float, float, float, float,  // first column
        float, float, float, float,  // second column
        float, float, float, float,  // third column
        float, float, float, float); // fourth column
   mat2x3(vec2, float,               // first column
          vec2, float);              // second column
   dmat2x4(dvec3, double,            // first column
           double, dvec3);           // second column

行列を初期化するのに十分な成分があれば、ベクトルやスカラーから行列を構成することも可能で，
他にも様々な可能性がある。例：

.. code:: glsl

   mat3x3(mat4x4); // takes the upper-left 3x3 of the mat4x4
   mat2x3(mat4x2); // takes the upper-left 2x2 of the mat4x4, last row is 0,0
   mat4x4(mat3x3); // puts the mat3x3 in the upper-left, sets the lower right
                   // component to 1, and the rest to 0

5.4.3. Structure Constructors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

構造体がいったん定義され、その型に名前が付けられると、
その構造体のインスタンスを構築するために、同じ名前のコンストラクターが利用可能になる：

.. code:: glsl

   struct light {
       float intensity;
       vec3 position;
   };

   light lightVar = light(3.0, vec3(1.0, 2.0, 3.0));

コンストラクターに対する実引数は構造体のメンバーを設定するために使用され、
メンバーごとに引数を一つ使用して順番に設定される。
各引数は設定するメンバーと同じ型であるか、
:ref:`4.1.10. Implicit Conversions` の項に従うメンバーの型に変換できる型でなければならない。

構造体コンストラクターは初期化子としても使われ、式の中でも使われる。

5.4.4. Array Constructors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

配列型はコンストラクター名としても使用でき、式や初期化子の中で使用することができる：

.. code:: glsl

   const float c[3] = float[3](5.0, 7.2, 1.1);
   const float d[3] = float[](5.0, 7.2, 1.1);

   float g;
   ...
   float a[5] = float[5](g, 1, g, 2.3, g);
   float b[3];

   b = float[3](g, g + 1.0, g + 2.0);

Each argument must be the same type as the element type of the array, or be a type that can be converted to the element type of the array according to “Implicit Conversions”.
構築される配列のサイズと実引数の個数がまったく同じである必要がある。
コンストラクターにサイズが指定されていない場合、
配列は指定された実引数の個数だけ明示的にサイズ調整される。
実引数は、構築された配列の要素に、要素 0 から順に代入される。
:ref:`4.1.10. Implicit Conversions` の項に従う配列の要素型に変換できる型でなければならない。

配列の配列も同様に構築され、どの次元のサイズもオプションだ。

.. code:: glsl

   vec4 b[2] = ...;
   vec4[3][2](b, b, b);    // constructor
   vec4[][2](b, b, b);     // constructor, valid, size deduced
   vec4[3][](b, b, b);     // constructor, valid, size deduced
   vec4[][](b, b, b);      // constructor, valid, both sizes deduced

5.4.5. Texture-Combined Sampler Constructors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

テクスチャー混合採取器コンストラクターは Vulkan を対象にしている場合にしか使用できない。

and consuming a texture and a sampler or samplerShadow. For example:
テクスチャー混合採取器型は、
``sampler2D`` のように、同型のコンストラクターである初期化子を使って宣言することができ、
テクスチャーと ``sampler`` または ``samplerShadow`` を消費する。例えば：

.. code:: glsl

   layout(...) uniform sampler s;   // handle to filtering information
   layout(...) uniform texture2D t; // handle to a texture
   layout(...) in vec2 tCoord;
   ...
   texture(sampler2D(t, s), tCoord);

テクスチャー混合採取器コンストラクターの結果は変数に代入できない：

.. code:: glsl

   ... sampler2D sConstruct = sampler2D(t, s);  // ERROR

テクスチャー混合採取器コンストラクターは関数の引数でしか消費されない。

配列のテクスチャー混合採取器コンストラクターは非合法だ：

.. code:: glsl

   layout(...) uniform texture2D tArray[6];
   ...
   ... sampler2D[](tArray, s) ...  // ERROR

* テクスチャー混合抽出器型のどれでもコンストラクターとして使用できる。
* そのコンストラクターの型は宣言する変数の型と合致していなければならない。
* コンストラクターの第一実引数はテクスチャー型でなければならない。
* コンストラクターの第二実引数は ``sampler`` 型または ``samplerShadow`` 型スカラーでなければならない。
* テクスチャー型の ``1D``, ``2D``, ``3D``, ``Cube``, ``Rect``, ``Buffer``, ``MS``, ``Array`` は、
  構築された型のものと合致しなければならない。
  つまり、第一引数の型とコンストラクターの型は同じ綴りで終わる。
* 任意の抽出器型を消費する制御フロー構造（例：条件演算子）は存在しない。

----

``Shadow`` の不一致は、コンストラクターとその第二実引数の間では許容される。
テクスチャー混合非シャドウ抽出器は ``samplerShadow`` から構築でき、
テクスチャー混合シャドウ抽出器は ``sampler`` から構築できる。

5.5. Vector and Scalar Components and Length
----------------------------------------------------------------------

The names of the components of a vector or scalar are denoted by a single letter. As a notational convenience, several letters are associated with each component based on common usage of position, color or texture coordinate vectors. The individual components can be selected by following the variable name with period (.) and then the component name.
ベクトルやスカラーの構成要素の名前は一文字で表される。
表記上の便宜のため、位置、色、テクスチャー座標のベクトルの一般的な使用方法に基づいて、
各成分に複数の文字が関連付けられている。
個々の成分を選択するには、変数名の後にピリオド ``.`` を付け、次に成分名を付ける。

サポートされている成分名は次のとおり：

.. csv-table::
   :delim: @

   ``{ x, y, z, w }`` @ 点や法線を表すベクトルにアクセスするときに便利
   ``{ r, g, b, a }`` @ 色を表すベクトルにアクセスする際に便利
   ``{ s, t, p, q }`` @ テクスチャー座標を表すベクトルにアクセスするときに便利

例えば ``x``, ``r``, ``s`` という成分名は、ベクトルの中の同じ成分の同義語だ。
また、スカラーの唯一の成分の名前でもある。

なお、テクスチャー座標の第三成分は、カラーの ``r`` (red) との混同を避けるために
``p`` と改名されている。

型に対して宣言されている以上の成分にアクセスするとコンパイルエラーになる。
例えば次のようになる：

.. code:: glsl

   vec2 pos;
   float height;
   pos.x       // is legal
   pos.z       // is illegal
   height.x    // is legal
   height.y    // is illegal

成分選択構文では、ピリオド ``.`` の後に（同じ名前集合の）名前を付けて、
複数の成分を選択することができる：

.. code:: glsl

   vec4 v4;
   v4.rgba;    // is a vec4 and the same as just using v4,
   v4.rgb;     // is a vec3,
   v4.b;       // is a float,
   v4.xy;      // is a vec2,
   v4.xgba;    // is illegal - the component names do not come from the same set

四つを超える成分を選択することはできない：

.. code:: glsl

   vec4 v4;
   v4.xyzwxy;      // is illegal since it has 6 components
   (v4.xyzwxy).xy; // is illegal since the intermediate value has 6 components

成分の順序を変えてかきまぜ (swizzle) たり、複製したりすることができる：

.. code:: glsl

   vec4 pos = vec4(1.0, 2.0, 3.0, 4.0);
   vec4 swiz = pos.wzyx;   // swiz = (4.0, 3.0, 2.0, 1.0)
   vec4 dup = pos.xxyy;    // dup = (1.0, 1.0, 2.0, 2.0)

この記法は、コンストラクターの構文よりも簡潔だ。
右辺値を形成するために、ベクトルまたはスカラーの右辺値になる任意の式に適用することができる。

成分グループ記法は式の左辺に出現することができる：

.. code:: glsl

   vec4 pos = vec4(1.0, 2.0, 3.0, 4.0);
   pos.xw = vec2(5.0, 6.0);        // pos = (5.0, 2.0, 3.0, 6.0)
   pos.wx = vec2(7.0, 8.0);        // pos = (8.0, 2.0, 3.0, 7.0)
   pos.xx = vec2(3.0, 4.0);        // illegal - 'x' used twice
   pos.xy = vec3(1.0, 2.0, 3.0);   // illegal - mismatch between vec2 and vec3

左辺値を形成するためには、左辺値にかきまぜをさらに適用し、
重複する成分を含まないようにする必要がある。
その結果、指定された成分の個数に応じて、スカラーまたはベクトル型左辺値が生成される。

配列添字構文は数値インデックスを提供するためにベクトルにも適用できる。
つまり：

.. code:: glsl

   vec4 pos;

``pos[2]`` は ``pos`` の三番目の要素を指し、
``pos.z`` と等値だ。これにより、ベクトルへの変数ンデックスが可能になり、
成分への一般的なアクセス方法にもなる。
添字には任意の整数式を使用できる。第一成分はインデックス 0 だ。
負の値またはベクトルのサイズ以上の値を持つ定整数式を使用してベクトルを読み書きするとコンパイルエラー。
非定数式でインデックスを作成する場合、インデックスが負の値、
またはベクトルのサイズ以上の値の場合、動作は未定義だ。

メソッドは ``length()`` ベクトルに適用できる。結果はベクトルの成分の個数だ：

.. code:: glsl

   vec3 v;
   const int L = v.length();

これは定数 ``L`` を 3 として設定する。

ベクトルの ``.length()`` の戻り値の型は ``int`` で、値は定数式だ。

5.6. Matrix Components
----------------------------------------------------------------------

行列の成分は、配列添字構文を使用してアクセスできる。
行列に単一の添字を適用すると、行列は列ベクトルの配列として扱われ、
行列（の列サイズ）と同じサイズのベクトルを型とする単一の列が選択される。
一番左の列は列 0 だ。
二番目の添字は、結果のベクトルを先にベクトルについて定義したように操作する。
したがって、二つの添字はまず列を選択し、次に行を選択する。

.. code:: glsl

   mat4 m;
   m[1] = vec4(2.0);   // sets the second column to all 2.0
   m[0][0] = 1.0;      // sets the upper left element to 1.0
   m[2][3] = 2.0;      // sets the 4th element of the third column to 2.0

非定数式で行列の境界外にある成分にアクセスするときの動作は未定義だ。
定数式で行列の境界外にある行列にアクセスするとコンパイルエラーになる。

.. admonition:: コメント

   原文がおかしい？

メソッド ``length()`` を行列に適用することができる。結果は行列の列数だ：

.. code:: glsl

   mat3x4 v;
   const int L = v.length();

このコードは定数 ``L`` を 3 にする。

行列の ``.length()`` の戻り値の型は ``int`` で、値は定数式だ。

5.7. Structure and Array Operations
----------------------------------------------------------------------

構造体のメンバーや配列の ``length()`` メソッドは、ピリオド ``.`` を使って選択される。

配列や構造体を全体として操作できるのは、次の演算子しかない：

.. csv-table::
   :delim: @

   field selector @ ``.``
   equality @ ``==``, ``!=``
   assignment @ ``=``
   Ternary operator @ ``?:``
   Sequence operator @ ``,``
   indexing (arrays only) @ ``[ ]``

等号演算子と代入演算子は、オペランド二つのサイズと型が同じ場合に限り使用できる。
オペランドに不透明型を含めることはできない。
構造体型は宣言された構造体と同じでなければならない。
配列オペランドは両方とも明示的にサイズがあるものでなければならない。
等号演算子を使用する場合、構造体は、すべてのメンバーが構成要素ごとに等しい場合かつその場合に限り等しく、
配列は、すべての要素が要素ごとに等しい場合かつその場合に限り等しい。

配列の要素にアクセスするには，配列添字演算子 ``[ ]`` を使用する：

.. code:: glsl

   diffuseColor += lightIntensity[3] * NdotL;

配列のインデックスはゼロから始まる。
配列の要素は、型が ``int`` または ``uint`` の式を使用してアクセスされる。

シェーダーが 0 より小さいか、そのサイズ以上に添字を配列に与える場合の動作は未定義だ。

配列は、メソッド演算子 ``.`` と ``length`` メソッドを使ってアクセスし、
配列のサイズを問い合わせることもできる：

.. code:: glsl

   lightIntensity.length() // return the size of the array

5.8. Assignments
----------------------------------------------------------------------

変数名への値の代入は、代入演算子 ``=`` で行う。

| *lvalue-expression* = *rvalue-expression*

The other assignment operators are
*lvalue-expression* は、左辺値に評価される。
代入演算子は *rvalue-expression* の値を左辺値に格納し、
*lvalue-expression* の型と精度を持つ右辺値を返す。
*lvalue-expression* と *rvalue-expression* は同じ型でなければならず、
または式は *lvalue-expression* の型に変換する
:ref:`4.1.10. Implicit Conversions` の表の型を持っていなければならず、
その場合、代入が行われる前に *rvalue-expression* で暗黙の変換が行われる。
その他の必要な型変換は、コンストラクターで明示的に指定しなければならない。
左辺値が書き込み可能でない場合は、コンパイルエラー。
組み込み型の変数、構造体や配列全体、構造体のメンバー、フィールドセレクター ``.``
を適用して成分を選択した左辺値、フィールドを繰り返さないかきまぜ、
括弧内の左辺値、配列の添え字演算子 ``[ ]`` で参照される左辺値は、すべて左辺値だ。
その他の二項式または単項式、関数名、フィールドが繰り返されるかきまぜ、
および定数は左辺値にできない。
条件演算子 ``?:`` も左辺値としては使用できない。
不正な式を左辺値として使用すると、コンパイルエラー。

代入の左側にある式は、その右側にある式よりも先に評価される。

他の代入演算子は ``+=`` のようなものたちだ（本文参照）。

ここでは、一般的な表現

| *lvalue* *op*= *expression*

と次の文は同値だ：

| *lvalue* = *lvalue* *op* *expression*

ここで、
*lvalue* は *lvalue-expression* が返す値、
*op* は後述のとおりで、
*lvalue-expression* と *expression* は
*op* と ``=`` の両方の意味的要件を満たさなければならない。

変数を書き込んだり、または初期化したりする前に変数を読み出すことは合法だが、その値は未定義だ。

5.9. Expressions
----------------------------------------------------------------------

.. admonition:: コメント

   当言語の式を構築するすべての要素が列挙されているが、詳細過ぎるので省略。
   いちおう面白い。

式の構文の完全な仕様については :ref:`9. Shading Language Grammar` を参照。

5.10. Vector and Matrix Operations
----------------------------------------------------------------------

いくつかの例外を除いて、演算は成分ごとに行われる。
通常、演算子がベクトルや行列を操作する場合、その演算子はベクトルや行列の各成分を独立して操作する。
例えば、以下のようになる：

.. code:: glsl

   vec3 v, u;
   float f;
   v = u + f;

これは次と同値だ：

.. code:: glsl

   v.x = u.x + f;
   v.y = u.y + f;
   v.z = u.z + f;

.. code:: glsl

   vec3 v, u, w;
   w = v + u;

これは次と同値だ：

.. code:: glsl

   w.x = v.x + u.x;
   w.y = v.y + u.y;
   w.z = v.z + u.z;

また、ほとんどの演算子、すべての整数および浮動小数点のベクトルおよび行列の型についても同様だ。
例外は、行列とベクトルの乗算、ベクトルと行列の乗算、行列と行列の乗算だ。
これらは成分ごとの演算ではなく、正しい線形代数的な乗算を行う。

.. code:: glsl

   vec3 v, u;
   mat3 m;
   u = v * m;

これは次と同値だ：

.. code:: glsl

   u.x = dot(v, m[0]); // m[0] is the left column of m
   u.y = dot(v, m[1]); // dot(a,b) is the inner (dot) product of a and b
   u.z = dot(v, m[2]);

そして

.. code:: glsl

   u = m * v;

これは次と同値だ：

.. code:: glsl

   u.x = m[0].x * v.x + m[1].x * v.y + m[2].x * v.z;
   u.y = m[0].y * v.x + m[1].y * v.y + m[2].y * v.z;
   u.z = m[0].z * v.x + m[1].z * v.y + m[2].z * v.z;

そして

.. code:: glsl

   mat3 m, n, r;
   r = m * n;

これは次と同値だ：

.. code:: glsl

   r[0].x = m[0].x * n[0].x + m[1].x * n[0].y + m[2].x * n[0].z;
   r[1].x = m[0].x * n[1].x + m[1].x * n[1].y + m[2].x * n[1].z;
   r[2].x = m[0].x * n[2].x + m[1].x * n[2].y + m[2].x * n[2].z;
   r[0].y = m[0].y * n[0].x + m[1].y * n[0].y + m[2].y * n[0].z;
   r[1].y = m[0].y * n[1].x + m[1].y * n[1].y + m[2].y * n[1].z;
   r[2].y = m[0].y * n[2].x + m[1].y * n[2].y + m[2].y * n[2].z;
   r[0].z = m[0].z * n[0].x + m[1].z * n[0].y + m[2].z * n[0].z;
   r[1].z = m[0].z * n[1].x + m[1].z * n[1].y + m[2].z * n[1].z;
   r[2].z = m[0].z * n[2].x + m[1].z * n[2].y + m[2].z * n[2].z;

また、他のサイズのベクトルや行列についても同様だ。

.. admonition:: コメント

   要するにスカラー積か線形変換になる。

5.11. Out-of-Bounds Accesses
----------------------------------------------------------------------

前述の節サブセクションの配列、ベクトル、行列、構造体へのアクセスでは、
境界外のアクセスは未定義の動作を引き起こした。しかし、API を通じて堅牢バッファーアクセスを有効にすると、
そのようなアクセスはアクティブなプログラムのメモリー連続格納領域 (extent) 内に束縛される。
他のプログラムからメモリーにアクセスすることはできないし、
アクセスによってプログラムが異常終了することもない。
境界外の読み取りは、未定義の値を返し、
アクティブなプログラムの他の変数の値やゼロが含まれる。
境界外書き込みでは、計算されたインデックスの値とアクティブプログラムのメモリーの範囲との関係によって、
アクティブプログラムの他の変数が破棄されたり、上書きされたりする。
境界外のアクセスに対する定義された動作を必要とするアプリケーションは、
配列を逆参照する前に計算されたインデックスすべてを確認する必要がある。

5.12. Specialization-Constant Operations
----------------------------------------------------------------------

特殊化定数操作は SPIR-V を対象とする場合にしか利用できない。

この節で議論される操作のいくつかしか特殊化定数に適用されず、
特殊化定数となる結果を生じることがある。そのような操作を以下に示す。
特殊化定数がこれらの演算子の一つと他の定数か特殊化定数で演算されると、
結果は暗黙のうちに特殊化定数となる。

* 次のいずれかの型から次のいずれかの型への型変換を行う ``int()``, ``uint()``, ``bool()`` コンストラクター各種：

  * ``int``
  * ``uint``
  * ``bool``

* 上記の変換コンストラクターのベクトル版
* 許容された上記の暗黙的な変換
* かきまぜ。例：``foo.yx``
* 整数型または符号なし整数型に適用される場合の次のもの：

  * 単項マイナス ``-``
  * 二項演算 (``+``, ``-``, ``*``, ``/``, ``%``)
  * ビットシフト (``<<``, ``>>``)
  * ビット別演算 (``&``, ``|``, ``^``)

* 整数型スカラーや符号なし整数型スカラーに適用される場合の次のもの：

  * 比較演算 (``==``, ``!=``, ``>``, `>=``, ``<``, ``<=``)

* 真偽スカラー型に適用される場合の次のもの：

  * 否定 (``!``)
  * 論理演算 (``&&``, ``||``, ``^^``)
  * 比較 (``==``, ``!=``)

* 条件演算子 ``?:``
