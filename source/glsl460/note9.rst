======================================================================
GLSL 4.60 仕様書 読書ノート 9 of ?
======================================================================

先に仕様書の内容をそっくりに写して、それから削る形でノートに仕上げたい。

.. contents:: ノート目次

9. Shading Language Grammar
======================================================================

.. admonition:: コメント

   トークン、文法については
   `仕様書本文 <https://www.khronos.org/registry/OpenGL/specs/gl/GLSLangSpec.4.60.html#shading-language-grammar>`__
   をその都度参照することにする。

文法は字句解析の出力から供給される。字句解析から返されるトークンはこの章の最初のテキストブロックにすべて掲載されている。

.. admonition:: コメント

   トークンが大量に列挙されている。キーワードを大文字で書いたものがほとんどのようだ。

   ``LEFT_OP``, ``RIGHT_OP``, ``INC_OP``, ``DEC_OP``, ``LE_OP``, など、
   これまで見たことがないトークンがある。あとで定義される？

上記のトークンに関して OpenGL Shading Language の文法を記述したものが二番目のテキストブロックにある。
開始規則は *translation_unit* だ。
空のシェーダー（前処理の後、解析するトークンがないもの）は有効であり、
その結果、下記の文法には空のトークンストリームを受け入れる規則がないにも関わらず、コンパイルエラーは発生しない。

.. admonition:: コメント

   これまでのしばしば目にしたような BNF で文法のすべてが定義されている。
   雰囲気を伝えるために一例を挙げておく：

   | *translation_unit* :
   |     *external_declaration*
   |     *translation_unit* *external_declaration*
   |
   | *external_declaration* :
   |     *function_definition*
   |     *declaration*
   |     *SEMICOLON*
   |
   | *function_definition* :
   |     *function_prototype* *compound_statement_no_new_scope*

   *SEMICOLON* など、全部大文字の単語はトークンだと解釈できるように記されているようだ。

   | *declaration* :
   |     *function_prototype SEMICOLON*
   |     *init_declarator_list SEMICOLON*
   |     *PRECISION precision_qualifier type_specifier SEMICOLON*
   |     *type_qualifier IDENTIFIER LEFT_BRACE struct_declaration_list RIGHT_BRACE SEMICOLON*
   |     *type_qualifier IDENTIFIER LEFT_BRACE struct_declaration_list RIGHT_BRACE IDENTIFIER SEMICOLON*
   |     *type_qualifier IDENTIFIER LEFT_BRACE struct_declaration_list RIGHT_BRACE IDENTIFIER array_specifier SEMICOLON*
   |     *type_qualifier SEMICOLON*
   |     *type_qualifier IDENTIFIER SEMICOLON*
   |     *type_qualifier IDENTIFIER identifier_list SEMICOLON*

一般的に、上記の文法は OpenGL Shading Language の超集合を記述している。
文法的には純粋に有効な構成要素も、当仕様書の他の箇所では禁止されている。

10. Acknowledgments
======================================================================

本仕様書は、過去のバージョンの Open GL およびOpen GL ES 言語仕様書に貢献された人々と、
本バージョンに貢献された以下の人々の仕事に基づいている：

.. admonition:: コメント

   30 名ほどの協力者の氏名と、あれば所属が列挙されている。
   NVIDIA, AMD, Intel, Apple, etc. すごい。

   `仕様書本文 <https://www.khronos.org/registry/OpenGL/specs/gl/GLSLangSpec.4.60.html##acknowledgments>`__
   参照。

11. Normative References
======================================================================

.. admonition:: コメント

   * 標準 C++ (1998),
   * Open GL ES 3.2 (2016),
   * Open GL 4.6 コアプロファイル (2016),
   * IEEE 754 (2008),
   * SPIR-V 1.3,
   * Vulkan 1.1 (2019)

   の仕様を挙げている。

12. Non-Normative SPIR-V Mappings
======================================================================

この付録の内容：

* Vulkan と OpenGLの両方について、SPIR-V を使用した場合と使用しない場合の機能を比較。
* GLSL と SPIR-V の両機能が論理的にどのように対応しているか。

12.1. Feature Comparisons
----------------------------------------------------------------------

OpenGL、Vulkan ともに、以下の機能を削除した：

* サブルーチン
* 共有およびまとめられたブロックレイアウト
* すでに非推奨となっているテクスチャー関数 (e.g. ``texture2D()``)
* すでに非推奨となっているノイズ関数 (e.g. ``noise1()``)
* 互換性プロファイルの機能
* ``gl_DepthRangeParameters`` と ``gl_NumSamples``

Vulkan では以下の機能を削除したが、OpenGL ではまだ残している：

* 既定の一様変数、不透明型に対して：
  ``UniformConstant`` 格納クラスは、大域スコープの個々の変数に使用することができる。
  つまり、一様変数は、GLSL 4.5 以上でブロックになっている組み込みメンバーでない限り、
  ブロックの中にある必要はない。
* GLSL 不可分カウンター束縛は ``offset`` レイアウト修飾子を持つ。
  → SPIR-V の ``Offset`` 装飾を使っている ``AtomicCounter`` 格納クラス。
* GLSL の ``origin_lower_left`` → SPIR-V の ``OriginLowerLeft``
* 頂点シェーダーでの入力倍数の位置に関する特別な規則
* ``gl_VertexID`` と ``gl_InstanceID``

OpenGL、Vulkan ともに、以下の機能が追加：

* 特殊化定数
* 宣言順とは異なる順序でメンバーを編成できる ``offset``
* 一様・バッファーブロックの ``offset`` および ``align`` レイアウト修飾子を、
  サポートしていなかったバージョンに対応

Vulkan のみ以下の機能が追加：

* 押し込み一定バッファー
* 別々のテクスチャーと採取器のシェーダー混合（SPIR-V ``OpTypeSampler``)
* 記述子集合（存在するならば ``DescriptorSet``  0でなければならない）
* ``gl_VertexIndex`` と ``gl_InstanceIndex``
* サブパス入力対象と入力付属 (``input_attachment_index``)

OpenGL、Vulkanともに、以下の機能が変更：

* ``gl_FragColor`` が暗黙のブロードキャストを示さなくなる。

Vulkan のみ以下の機能が変更：

* 精度修飾子 ``mediump``, ``lowp`` はデスクトップ版では削除されず、
  すべてのバージョンで尊重される（デスクトップ版の既定精度はすべての型で ``highp`` だ）。
* 一様変数の配列とバッファーブロックの配列は、要素ごとではなく、
  オブジェクト全体に対して一つの束縛番号しか受け取らなくなった。
* 既定原点は ``origin_lower_left`` ではなく ``origin_upper_left`` となった。

Vulkan は SPIR-V 環境仕様で UBO や SSBO などの資源の多次元配列を許さない。
SPIR-V はそれをサポートしており、OpenGL はすでに GLSL シェーダーでこれを許可している。
SPIR-V for OpenGL でも許可されている。

12.2. Mapping from GLSL to SPIR-V
----------------------------------------------------------------------

.. admonition:: コメント

   以下、私には読む必要が全くないトピックのはずだ。

12.2.1. Specialization Constants
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SPIR-V 特殊化定数は、クライアント API で後から設定することができ、
``layout(constant_id=...)`` を用いて宣言することができる。
例えば、既定値が 12 の特殊化定数を作るには次のようにする：

.. code:: glsl

   layout(constant_id = 17) const int arraySize = 12;

上記 17 は API や他のツールが後にこの特定の特殊化定数を参照するための ID だ。
API や中間ツールは、実行コードに完全に下げられる前に、その値を別の定数の整数に変更することができる。
最終的に下げられる前に変更されない場合は 12 の値を維持する。

.. admonition:: コメント

   原文の意味がつかめなかった。動詞 lower の意味がわからない。

特殊化定数は、畳み込みがないということ以外は ``const`` のセマンティクスを持つ。
したがって、配列は ``arraySize`` で宣言することができる：

.. code:: glsl

   vec4 data[arraySize];  // legal, even though arraySize might change

特殊化定数は式の中に入れることができる：

.. code:: glsl

   vec4 data2[arraySize + 2];

これにより、シェーダーを実行コードに落とし込む際に、
``data2`` のサイズが ``arraySize`` の持つ定数値よりも 2 だけ大きくなる。

特殊化定数で形成された式もまた、シェーダー内では特殊化定数のように振る舞う。定数のようにではない。

.. code:: glsl

   arraySize + 2       // a specialization constant (with no constant_id)

このような式は定数と同じ場所で使用できる。

``constant_id`` はスカラー整数、スカラー浮動小数点、スカラー真偽値のどれかにしか適用できない。

基本的な演算子とコンストラクターしか特殊化定数に適用できず、結果として特殊化定数が得られる：

.. code:: glsl

   layout(constant_id = 17) const int arraySize = 12;
   sin(float(arraySize));    // result is not a specialization constant

SPIR-V 特殊化定数はスカラーしか対象としていないが、ベクトルはスカラーの演算で作ることができる：

.. code:: glsl

   layout(constant_id = 18) const int scX = 1;
   layout(constant_id = 19) const int scZ = 1;
   const vec3 scVec = vec3(scX, 1, scZ);  // partially specialized vector

組み込み変数には ``constant_id`` を付けることができる：

.. code:: glsl

   layout(constant_id = 18) gl_MaxImageUnits;

これにより特殊化定数のようになる。
これは完全な再宣言ではなく、他のすべての特性は元の組み込み宣言からそのまま残されている。

組み込みベクトル ``gl_WorkGroupSize`` は、
``in`` 修飾子に適用される特別レイアウト ``local_size_{xyz}_id`` を用いて特化できる。
例えば：

.. code:: glsl

   layout(local_size_x_id = 18, local_size_z_id = 19) in;

これにより ``gl_WorkGroupSize.y`` は非特殊化定数として残り、
``gl_WorkGroupSize`` は部分的に特殊化されたベクトルとなる。
その ``x`` および ``z`` 成分は、IDの 18 および 19 を使用して後で特殊化することができる。

12.2.2. Vulkan Only: Push Constants
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

プッシュ定数は、一様ブロック宣言に適用される新しい *layout-qualifier-id* ``push_constant``
を使って宣言された一様ブロック内に宿る。
API は定数の集合を push-constant バッファーに書き込み、
シェーダーは ``push_constant`` ブロックから定数を読み込む：

.. code:: glsl

   layout(push_constant) uniform BlockName {
       int member1;
       float member2;
       ...
   } InstanceName; // optional instance name
   ... = InstanceName.member2; // read a push constant

``push_constant`` 一様ブロックに使用されるメモリーアカウンティングは他の一様ブロックとは異なる。
それを収める必要がある隔離した小さなメモリープールがある。
既定では ``push_constant`` バッファーは ``std430`` の梱包規則に従う。

12.2.3. Vulkan Only: Descriptor Sets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

記述子集合内の各シェーダー資源には、記述子集合のレイアウト内での位置を定義する
集合番号、束縛番号、配列要素の組が割り当てられる。
GLSL では、集合番号および束縛番号は、それぞれ ``set`` および ``binding``
レイアウト修飾子を介して割り当てられ、配列要素は、配列の最初の要素のインデックスがゼロに等しい
（非配列変数の場合は配列要素がゼロ）ことから、暗黙のうちに連続して割り当てられる：

.. code:: glsl

   // Assign set number = M, binding number = N, array element = 0
   layout (set=M, binding=N) uniform sampler2D variableName;
   // Assign set number = M, binding number = N for all array elements,
   // and array element = i for the ith member of an array of size I.
   layout (set=M, binding=N) uniform sampler2D variableNameArray[I];
   For example, two combined texture/sampler objects can be declared in two different descriptor sets as follows

   layout(set = 0, binding = 0) uniform sampler2D ts3;
   layout(set = 1, binding = 0) uniform sampler2D ts4;

記述子集合の操作モデルの詳細については API 文書にある。

12.2.4. Vulkan Only: Samplers, Images, Textures, and Buffers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Storage Images
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

格納画像は GLSL シェーダーソースの中で、適切な次元の一様画像変数と、
必要に応じてフォーマットレイアウト修飾子を用いて宣言される。

.. code:: glsl

   layout (set=m, binding=n, r32f) uniform image2D myStorageImage;

これは次の SPIR-V に対応する：

.. code:: text

           ...
   %1 = OpExtInstImport "GLSL.std.450"
           ...
           OpName %9 "myStorageImage"
           OpDecorate %9 DescriptorSet m
           OpDecorate %9 Binding n
   %2 = OpTypeVoid
   %3 = OpTypeFunction %2
   %6 = OpTypeFloat 32
   %7 = OpTypeImage %6 2D 0 0 0 2 R32f
   %8 = OpTypePointer UniformConstant %7
   %9 = OpVariable %8 UniformConstant
           ...

Samplers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

SPIR-V 採取器は GLSL シェーダーのソースでは一様 ``sampler`` 型と ``samplerShadow`` 型を使って宣言される：

.. code:: glsl

   layout (set=m, binding=n) uniform sampler mySampler;

これは次の SPIR-V に対応する：

.. code:: text

           ...
   %1 = OpExtInstImport "GLSL.std.450"
           ...
           OpName %8 "mySampler"
           OpDecorate %8 DescriptorSet m
           OpDecorate %8 Binding n
   %2 = OpTypeVoid
   %3 = OpTypeFunction %2
   %6 = OpTypeSampler
   %7 = OpTypePointer UniformConstant %6
   %8 = OpVariable %7 UniformConstant
           ...

Textures (Sampled Images)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

テクスチャーは GLSL シェーダソースでは、適切な次元の一様テクスチャー変数を使って宣言される：

.. code:: glsl

   layout (set=m, binding=n) uniform texture2D mySampledImage;

これは次の SPIR-V に対応する：

.. code:: text

           ...
   %1 = OpExtInstImport "GLSL.std.450"
           ...
           OpName %9 "mySampledImage"
           OpDecorate %9 DescriptorSet m
           OpDecorate %9 Binding n
   %2 = OpTypeVoid
   %3 = OpTypeFunction %2
   %6 = OpTypeFloat 32
   %7 = OpTypeImage %6 2D 0 0 0 1 Unknown
   %8 = OpTypePointer UniformConstant %7
   %9 = OpVariable %8 UniformConstant
           ...

Combined Texture and Samplers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

混合テクスチャーと採取器は GLSL シェーダソースの中では適切な次元の一様テクスチャー混合採取器変数を使って宣言される：

.. code:: glsl

   layout (set=m, binding=n) uniform sampler2D myCombinedImageSampler;

これは次の SPIR-V に対応する：

.. code:: text

           ...
   %1 = OpExtInstImport "GLSL.std.450"
           ...
           OpName %10 "myCombinedImageSampler"
           OpDecorate %10 DescriptorSet m
           OpDecorate %10 Binding n
   %2 = OpTypeVoid
   %3 = OpTypeFunction %2
   %6 = OpTypeFloat 32
   %7 = OpTypeImage %6 2D 0 0 0 1 Unknown
   %8 = OpTypeSampledImage %7
   %9 = OpTypePointer UniformConstant %8
   %10 = OpVariable %9 UniformConstant
           ...

なお、混合画像採取器記述子は、上述の節と同様に、
シェーダー内では単なる画像または採取器として参照することができる。

Combining Separate Samplers and Textures
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

キーワード ``sampler`` で宣言された採取器は、フィルタリング情報のみを含み、
テクスチャーや画像を含まない：

.. code:: glsl

   uniform sampler s;    // a handle to filtering information

``texture2D`` のようなキーワードで宣言されたテクスチャーは、画像情報のみを含み、
フィルタリング情報を含まない：

.. code:: glsl

   uniform texture2D t;  // a handle to a texture (an image in SPIR-V)

コンストラクターを使用して、テクスチャー検索呼び出しを行う際に、
採取器とテクスチャーを合成することができる：

.. code:: glsl

   texture(sampler2D(t, s), ...);

この機能をわかりやすく示すために、上記で ``layout()`` の情報を省略したことに注意。

Texture Buffers (Uniform Texel Buffers)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

テクスチャーバッファーは、GLSL シェーダソースでは一様 ``textureBuffer`` 変数を使って宣言される：

.. code:: glsl

   layout (set=m, binding=n) uniform textureBuffer myUniformTexelBuffer;

これは次の SPIR-V に対応する：

.. code:: text

           ...
   %1 = OpExtInstImport "GLSL.std.450"
           ...
           OpName %9 "myUniformTexelBuffer"
           OpDecorate %9 DescriptorSet m
           OpDecorate %9 Binding n
   %2 = OpTypeVoid
   %3 = OpTypeFunction %2
   %6 = OpTypeFloat 32
   %7 = OpTypeImage %6 Buffer 0 0 0 1 Unknown
   %8 = OpTypePointer UniformConstant %7
   %9 = OpVariable %8 UniformConstant
           ...

Image Buffers (Storage Texel Buffers)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

画像バッファーは、GLSL シェーダーソース中では一様 ``imageBuffer`` 変数を使って宣言される：

.. code:: glsl

   layout (set=m, binding=n, r32f) uniform imageBuffer myStorageTexelBuffer;

これは次の SPIR-V に対応する：

.. code:: text

           ...
   %1 = OpExtInstImport "GLSL.std.450"
           ...
           OpName %9 "myStorageTexelBuffer"
           OpDecorate %9 DescriptorSet m
           OpDecorate %9 Binding n
   %2 = OpTypeVoid
   %3 = OpTypeFunction %2
   %6 = OpTypeFloat 32
   %7 = OpTypeImage %6 Buffer 0 0 0 2 R32f
   %8 = OpTypePointer UniformConstant %7
   %9 = OpVariable %8 UniformConstant
           ...

Storage Buffers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

GLSL シェーダーのソースでは、バッファー格納修飾子とブロック構文を使って格納バッファーを宣言する：

.. code:: glsl

   layout (set=m, binding=n) buffer myStorageBuffer
   {
       vec4 myElement[];
   };

これは次の SPIR-V に対応する：

.. code:: text

           ...
   %1 = OpExtInstImport "GLSL.std.450"
           ...
           OpName %9 "myStorageBuffer"
           OpMemberName %9 0 "myElement"
           OpName %11 ""
           OpDecorate %8 ArrayStride 16
           OpMemberDecorate %9 0 Offset 0
           OpDecorate %9 BufferBlock
           OpDecorate %11 DescriptorSet m
           OpDecorate %11 Binding n
   %2 = OpTypeVoid
   %3 = OpTypeFunction %2
   %6 = OpTypeFloat 32
   %7 = OpTypeVector %6 4
   %8 = OpTypeRuntimeArray %7
   %9 = OpTypeStruct %8
   %10 = OpTypePointer Uniform %9
   %11 = OpVariable %10 Uniform
           ...

Uniform Buffers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Uniform buffers are declared in GLSL shader source using the uniform storage qualifier and block syntax:

.. code:: glsl

   layout (set=m, binding=n) uniform myUniformBuffer
   {
       vec4 myElement[32];
   };

これは次の SPIR-V に対応する：

.. code:: text

           ...
   %1 = OpExtInstImport "GLSL.std.450"
           ...
           OpName %11 "myUniformBuffer"
           OpMemberName %11 0 "myElement"
           OpName %13 ""
           OpDecorate %10 ArrayStride 16
           OpMemberDecorate %11 0 Offset 0
           OpDecorate %11 Block
           OpDecorate %13 DescriptorSet m
           OpDecorate %13 Binding n
   %2 = OpTypeVoid
   %3 = OpTypeFunction %2
   %6 = OpTypeFloat 32
   %7 = OpTypeVector %6 4
   %8 = OpTypeInt 32 0
   %9 = OpConstant %8 32
   %10 = OpTypeArray %7 %9
   %11 = OpTypeStruct %10
   %12 = OpTypePointer Uniform %11
   %13 = OpVariable %12 Uniform
           ...

Subpass Inputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

一つのレンダリングパスの中で、サブパスは結果を出力対象に書き込むことができ、
その結果を次のサブパスが入力サブパスとして読み取ることができる。
「サブパス入力」機能とは、出力対象を読み取る機能だ。

サブパス入力は、フラグメントシェーダーでしか利用できない、新しい型の集合を通して読み込まれる：

| ``subpassInput``
| ``subpassInputMS``
| ``isubpassInput``
| ``isubpassInputMS``
| ``usubpassInput``
| ``usubpassInputMS``

抽出器や画像オブジェクトとは異なり、サブパス入力はフラグメントの
``(x, y, layer)`` 座標によって暗黙のうちに指定される。

入力付属物は、記述子集合と束縛番号に加えて、入力付属物のインデックスで装飾される。

.. code:: glsl

   layout (input_attachment_index=i, set=m, binding=n) uniform subpassInput myInputAttachment;

これは次の SPIR-V に対応する：

.. code:: text

        ...
   %1 = OpExtInstImport "GLSL.std.450"
           ...
           OpName %9 "myInputAttachment"
           OpDecorate %9 DescriptorSet m
           OpDecorate %9 Binding n
           OpDecorate %9 InputAttachmentIndex i
   %2 = OpTypeVoid
   %3 = OpTypeFunction %2
   %6 = OpTypeFloat 32
   %7 = OpTypeImage %6 SubpassData 0 0 0 2 Unknown
   %8 = OpTypePointer UniformConstant %7
   %9 = OpVariable %8 UniformConstant
           ...

An input_attachment_index of i selects the ith entry in the input pass list. (See API specification for more information.)
``input_attachment_index`` が ``i`` の場合、入力パスリストのi番目のエントリを選択します。(詳細はAPI仕様を参照)。

These objects support reading the subpass input through the following functions:

これらのオブジェクトは、以下の関数によってサブパス入力の読み込みをサポートしています。

.. code:: glsl

   gvec4 subpassLoad(gsubpassInput   subpass);
   gvec4 subpassLoad(gsubpassInputMS subpass, int sample);

12.2.5. Mapping Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

gl_FragColor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

フラグメント段階組み込み ``gl_FragColor`` は、すべての出力へのブロードキャストを意味するが、
SPIR-V には存在しない。
``gl_FragColor`` への書き込みが許可されているシェーダーはやはり書き込みが可能だが、

* ``gl_FragColor`` と同じ型の
* 位置 0 で装飾されている
* 組み込みとして装飾されていない

出力への書き込みを意味するだけだ。

暗黙のブロードキャストはない。

Vulkan gl_VertexIndex and gl_InstanceIndex
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

既存の組み込み変数 ``gl_VertexID`` と ``gl_InstanceID`` の代わりに、
新しい組み込み変数 ``gl_VertexIndex`` と ``gl_InstanceIndex`` が加わる。

インデックスが何らかの基準オフセットに対して相対的である場合、
これらの組み込み変数は Vulkan では以下のような値を取るように定義されている：

.. csv-table::
   :delim: @

   ``gl_VertexIndex`` @ base, base + 1, base + 2, ...
   ``gl_InstanceIndex`` @ base, base + 1, base + 2, ...

基準となるものが何であるかは、状況によって異なる。

.. admonition:: コメント

   これ以降、コード片を引用するのをほとんどやめる。

Storage Classes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: コメント

   `本文 <https://www.khronos.org/registry/OpenGL/specs/gl/GLSLangSpec.4.60.html#_storage_classes>`__ 参照。

Input/Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

入力・出力ブロックや変数の対応は、GLSL や ESSL のすべてのバージョンで同じだ。
あるバージョンで利用可能な変数やメンバーの位置は次のとおりだ。

これらは SPIR-V の個々の変数に写され、同様の綴り方の組み込み装飾が一緒になる（特記事項を除く）：

どの段階でも：

.. admonition:: コメント

   `本文 <https://www.khronos.org/registry/OpenGL/specs/gl/GLSLangSpec.4.60.html#_mapping_variables>`__ 参照。

計算段階：

.. admonition:: コメント

   本文参照。

フラグメント段階：

.. admonition:: コメント

   本文参照。

これらは、疑似コードが暗示するように、
SPIR-V ブロックに写され、メンバーには同様の綴り方の組み込み装飾が一緒になる：

非フラグメント段階：

.. admonition:: コメント

   本文参照。

SPIR-V の各段階には、高々一つの入力ブロックと一つの出力ブロックがある。
インターフェイスを共有する段階間では、メンバーの部分集合と順序が一致する。

12.2.6. Vulkan Only: Mapping of Precision Qualifiers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: コメント

   `本文 <https://www.khronos.org/registry/OpenGL/specs/gl/GLSLangSpec.4.60.html#_vulkan_only_mapping_of_precision_qualifiers>`__ 参照。

12.2.7. Mapping of precise:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: コメント

   `本文 <https://www.khronos.org/registry/OpenGL/specs/gl/GLSLangSpec.4.60.html#_mapping_of_precise>`__ 参照。

12.2.8. OpenGL Mapping of atomic_uint offset layout qualifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: コメント

   `本文 <https://www.khronos.org/registry/OpenGL/specs/gl/GLSLangSpec.4.60.html#_opengl_mapping_of_atomic_uint_offset_layout_qualifier>`__ 参照。

12.2.9. Mapping of Images
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: コメント

   `本文 <https://www.khronos.org/registry/OpenGL/specs/gl/GLSLangSpec.4.60.html#_mapping_of_images>`__ 参照。

12.2.10. Mapping of Layouts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: コメント

   `本文 <https://www.khronos.org/registry/OpenGL/specs/gl/GLSLangSpec.4.60.html#_mapping_of_layouts>`__ 参照。

12.2.11. Mapping of barriers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: コメント

   `本文 <https://www.khronos.org/registry/OpenGL/specs/gl/GLSLangSpec.4.60.html#_mapping_of_barriers>`__ 参照。

12.2.12. Mapping of atomics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: コメント

   `本文 <https://www.khronos.org/registry/OpenGL/specs/gl/GLSLangSpec.4.60.html#_mapping_of_atomics>`__ 参照。

12.2.13. OpenGL Only: Mapping of Atomics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: コメント

   `本文 <https://www.khronos.org/registry/OpenGL/specs/gl/GLSLangSpec.4.60.html#_opengl_only_mapping_of_atomics>`__ 参照。

12.2.14. Mapping of other instructions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: コメント

   `本文 <https://www.khronos.org/registry/OpenGL/specs/gl/GLSLangSpec.4.60.html#_mapping_of_other_instructions>`__ 参照。
