======================================================================
WebGL Specification 1.0 読書ノート 3
======================================================================

`WebGL Specification <https://www.khronos.org/registry/webgl/specs/latest/1.0/>`__
を読んでいく。

.. contents:: ノート目次

6 Differences Between WebGL and OpenGL ES 2.0
======================================================================

この節では OpenGL ES 2.0 API に対する WebGL API の変更点について述べられている。
さまざまな OS やデバイス間での移植性を高めるのが目的のようだ。

6.1 Buffer Object Binding
----------------------------------------------------------------------

* 指定されたバッファーオブジェクトには頂点またはインデックスのいずれか一方が含まれ、
  両方は含まれないことを意味する。
* ``WebGLBuffer`` の型は ``bindBuffer`` の引数として初回に渡されたときに初期化される。
  同じ ``WebGLBuffer`` を他の束縛点に束縛しようとする ``bindBuffer`` への以降の呼び出しは
  ``INVALID_OPERATION`` エラーとなり、束縛点の状態は変更しない。

6.2 No Client Side Arrays
----------------------------------------------------------------------

* WebGL はクライアントサイドの配列をサポートしていない。
* ``enableVertexAttribArray`` によって頂点属性が配列として有効になっているにもかかわらず、
  その属性にバッファーが束縛されていない場合（通常は ``bindBuffer`` と ``vertexAttribPointer`` を使用）、
  描画コマンド ``drawArrays`` または ``drawElements`` は ``INVALID_OPERATION`` エラーとなる。
* インデックス付きの描画コマンド ``drawElements`` が呼び出され、
  ``ELEMENT_ARRAY_BUFFER`` 束縛点に ``WebGLBuffer`` が束縛されていない場合は
  ``INVALID_OPERATION`` エラーが発生します。
* ``ARRAY_BUFFER`` 束縛点に束縛された ``WebGLBuffer`` がない状態で ``vertexAttribPointer`` が呼び出され、
  ``offset`` が 0 以外の場合 ``INVALID_OPERATION`` エラーとなる。

----

クライアント側の配列がサポートされていないにもかかわらず、
``VERTEX_ATTRIB_ARRAY_BUFFER_BINDING`` を ``null`` に設定することを認めると、
束縛を元の状態にクリアすることができる。これは他の方法では厳密には不可能だ。

6.3 No Default Textures
----------------------------------------------------------------------

WebGL はデフォルトのテクスチャーをサポートしない。

テクスチャー関連の操作や問い合わせを成功させるためには、
``null`` ではない ``WebGLTexture`` オブジェクトが束縛されている必要がある。

6.4 No Shader Binaries
----------------------------------------------------------------------

* コンパイルされたシェーダーのバイナリー表現へのアクセスを WebGL はサポートしない。
  これには OpenGL ES 2.0 ShaderBinary エントリーポイントを含む。
* また、WebGL では ``getParameter`` を通じてシェーダーのバイナリー形式や
  シェーダーコンパイラーの有無を問い合わせることもサポートされていない。
* WebGL の実装すべてが、オンラインのシェーダーコンパイラーを暗黙のうちにサポートする必要がある。

6.5 Buffer Offset and Stride Requirements
----------------------------------------------------------------------

* ``drawElements`` および ``vertexAttribPointer`` への ``offset`` 引数、
  および ``vertexAttribPointer`` への ``stride`` 引数は、
  呼び出しに渡されたデータ型のサイズの倍数でなければならない。
  そうでない場合は ``INVALID_OPERATION`` エラーとなる。
* さらに ``drawElements`` の ``offset`` 引数は非負でなければならない。
  そうでない場合は ``INVALID_VALUE`` エラーとなる。

6.6 Enabled Vertex Attributes and Range Checking
----------------------------------------------------------------------

アクティブな頂点属性が配列として有効になっている場合に、
``drawArrays`` で直接的に、またはインデックス付きの描画から
``drawElements`` で間接的にデータを取得する必要がある描画コマンドを呼び出すと、
``WebGLBuffer`` の境界外のデータを要求する可能性がある。
このような場合、以下の動作のいずれかが起こる。

* WebGL の実装では、``INVALID_OPERATION`` エラーとなり、ジオメトリーが描画されないことがある。
* 範囲外の頂点取得が以下のいずれかの値を返すことがある：

  * バッファーオブジェクト内の任意の場所にある値。
  * ゼロか、またはベクトル読み込みに対しては ``(0, 0, 0, x)`` の形のベクトル。
    ここで ``x`` はベクトル成分の型で表現される有効な値であり、以下のいずれか：

    * 整数成分の場合 0, 1, または表現可能な最大の正の整数値
    * 浮動小数点成分の場合 0.0 または 1.0

頂点の属性が配列として有効であり、その属性にバッファーが束縛されていて、
その属性を現在のプログラムが消費していない場合、束縛されたバッファーのサイズに関わらず、
``drawArrays`` や ``drawElements`` を呼び出すときにエラーが発生することはない。

6.7 Out-of-bounds fetches from the index buffer
----------------------------------------------------------------------

``ELEMENT_ARRAY_BUFFER`` の境界外のインデックス要素を取得するような
``drawElements`` 呼び出しは ``INVALID_OPERATION`` エラーとなる。

6.8 Framebuffer Object Attachments
----------------------------------------------------------------------

WebGL はフレームバッファーオブジェクトの付着点 ``DEPTH_STENCIL_ATTACHMENT`` と、
レンダーバッファーの内部フォーマット ``DEPTH_STENCIL`` を加える。

* 奥行きとステンシルバッファーの両方をフレームバッファーオブジェクトに取り付けるには、

  #. ``DEPTH_STENCIL`` 内部フォーマットにて ``renderbufferStorage`` を呼び出し、
  #. 次に ``DEPTH_STENCIL_ATTACHMENT`` 付着点にて ``framebufferRenderbuffer`` を呼び出す。

* ``DEPTH_ATTACHMENT`` 付着点に取り付けられたレンダーバッファーは、
  ``DEPTH_COMPONENT16`` 内部フォーマットで割り当てられなければならない。
* ``STENCIL_ATTACHMENT`` 付着点に取り付けられたレンダーバッファーは、
  ``STENCIL_INDEX8`` 内部フォーマットで割り当てられなければならない。
* ``DEPTH_STENCIL_ATTACHMENT`` 付着点に取り付けられたレンダーバッファーは、
  ``DEPTH_STENCIL`` 内部フォーマットで割り当てられなければなりません。

WebGL では、次の付着点の組み合わせと同時にレンダーバッファーを取り付けるとエラーになる：

* ``DEPTH_ATTACHMENT`` + ``DEPTH_STENCIL_ATTACHMENT``
* ``STENCIL_ATTACHMENT`` + ``DEPTH_STENCIL_ATTACHMENT``
* ``DEPTH_ATTACHMENT`` + ``STENCIL_ATTACHMENT``

上記の拘束条件のいずれかに違反している場合：

* ``checkFramebufferStatus`` は ``FRAMEBUFFER_UNSUPPORTED`` を返すものとする。
* フレームバッファーを変更または読み取る次の呼び出しは
  ``INVALID_FRAMEBUFFER_OPERATION`` エラーとなり、
  フレームバッファー、destination テクスチャーまたは destination メモリーの内容物に触ることなく、早々に戻らなければならない。

  * ``clear``
  * ``copyTexImage2D``
  * ``copyTexSubImage2D``
  * ``drawArrays``
  * ``drawElements``
  * ``readPixels``

以下のフレームバッファーオブジェクトの取り付けの組み合わせは、
すべての取り付けがフレームバッファー付着完全であり、
ゼロではなく、同じ幅と高さを持つ場合、フレームバッファーがフレームバッファー完全になる必要がある：

* ``COLOR_ATTACHMENT0`` = ``RGBA``/``UNSIGNED_BYTE`` テクスチャー
* ``COLOR_ATTACHMENT0`` = ``RGBA``/``UNSIGNED_BYTE`` テクスチャー + ``DEPTH_ATTACHMENT`` = ``DEPTH_COMPONENT16`` レンダーバッファー
* ``COLOR_ATTACHMENT0`` = ``RGBA``/``UNSIGNED_BYTE`` テクスチャー + ``DEPTH_STENCIL_ATTACHMENT`` = ``DEPTH_STENCIL`` レンダーバッファー

6.9 Texture Upload Width and Height
----------------------------------------------------------------------

``texImage2D`` が設定するテクスチャーの寸法、および
``texSubImage2D`` で更新される部分矩形の寸法は、
``width`` と ``height`` の引数が明示的に指定されない限り、
アップロードされた ``TexImageSource`` ``source`` オブジェクトに基づいて決定する。

----

型が ``ImageData`` である ``source`` の場合
    テクスチャーの寸法は ``ImageData`` オブジェクトの ``width`` と ``height`` の
    プロパティーの現在の値に設定され、そのオブジェクトの実際のピクセル幅と高さを表す。

型が ``HTMLImageElement`` である ``source`` の場合
    ビットマップがアップロードされた場合、テクスチャーの寸法は、
    アップロードされたビットマップの寸法（ピクセル単位）に設定される。

    SVG イメージがアップロードされた場合、テクスチャー寸法は、
    ``HTMLImageElement`` オブジェクトの ``width`` および ``height`` プロパティーの現在の値に設定される。

型が ``HTMLCanvasElement`` または ``OffscreenCanvas`` である ``source`` の場合
    テクスチャーの寸法は、キャンバスオブジェクトの ``width`` と ``height`` プロパティーの現在の値に設定される。

型が ``HTMLVideoElement`` または ``VideoFrame`` である ``source`` の場合
    テクスチャーの寸法は、ビデオのアップロードされたフレームの寸法（ピクセル単位）に設定される。

6.10 Pixel Storage Parameters
----------------------------------------------------------------------

WebGL では ``pixelStorei`` に次の追加パラメーターをサポートする：

``UNPACK_FLIP_Y_WEBGL``
    設定されている場合、それ以降の ``texImage2D`` または ``texSubImage2D`` の呼び出しの際に、
    元データを垂直に反転し、概念的には最後の行を最初に転送するようになる。

    * 初期値は ``false`` とする。ゼロ以外の値は ``true`` と解釈される。

``UNPACK_PREMULTIPLY_ALPHA_WEBGL``
    設定された場合、それ以降の ``texImage2D`` または ``texSubImage2D`` の呼び出しの際に、
    元データのアルファーチャンネルが存在する場合は、それを
    データ転送中にカラーチャンネルに乗算する。

    * 初期値は ``false`` とする。ゼロ以外の値は ``true`` と解釈される。

``UNPACK_COLORSPACE_CONVERSION_WEBGL``
    ``BROWSER_DEFAULT_WEBGL`` に設定された場合、``HTMLImageElement`` を取る後続の
    ``texImage2D`` および ``texSubImage2D`` 呼び出し中に、ブラウザーの既定の色空間変換を適用する。

    * 正確な変換は、ブラウザーとファイルタイプの両方に固有のものとなる。
    * ``NONE`` に設定された場合、色空間の変換を適用しない。
    * 初期値は ``BROWSER_DEFAULT_WEBGL`` とする。
    * ``TexImageSource`` が ``ImageBitmap`` の場合は、これら三つの引数を無視する。
      代わりに、同等の ``ImageBitmapOptions`` を使用して、所望のフォーマットの
      ``ImageBitmap`` を作成する必要がある。

6.11 Reading Pixels Outside the Framebuffer
----------------------------------------------------------------------

WebGL にはフレームバッファーを読み込む関数が三つある。

* ``copyTexImage2D``
* ``copyTexSubImage2D``
* ``readPixels``

``copyTexImage2D`` は、束縛フレームバッファーの外側にあるどのピクセルに対しても
RGBA 値 ``(0, 0, 0, 0)`` を生成するように定義されている。

``copyTexSubImage2D`` と ``readPixels`` は、束縛フレームバッファーの外側にあるどのピクセルに対しても、
対応する destination 範囲に触れぬように定義されている。

6.12 Stencil Separate Mask and Reference Value
----------------------------------------------------------------------

WebGL では、ステンシルテストが有効で、現在束縛されているフレームバッファーに
ステンシルバッファーがある場合、以下のいずれかのケースが成立している間の描画は違法とする。
これを行うと ``INVALID_OPERATION`` エラーだ。

* ``(STENCIL_WRITEMASK & maxStencilValue) != (STENCIL_BACK_WRITEMASK & maxStencilValue)``

  （面の ``FRONT`` および ``BACK`` の値それぞれに関連付けられた ``mask`` 引数に対する ``stencilMaskSeparate`` で指定されたとして）
* ``(STENCIL_VALUE_MASK & maxStencilValue) != (STENCIL_BACK_VALUE_MASK & maxStencilValue)``

  （面の ``FRONT`` および ``BACK`` の値それぞれに関連付けられた ``mask`` 引数に対する ``stencilFuncSeparate`` で指定されたとして）
* ``clamp(STENCIL_REF, 0, maxStencilValue) != clamp(STENCIL_BACK_REF, 0, maxStencilValue)``

  （面の ``FRONT`` および ``BACK`` の値それぞれに関連付けられた ``ref`` 引数に対する ``stencilFuncSeparate`` で指定されたとして）

ここで、``maxStencilValue`` は ``((1 << s) - 1)`` であり、
``s`` は描画フレームバッファーのステンシルビット数とする。

* ステンシルビットが存在しない場合は、これらのチェックは常に合格とする。

6.13 Vertex Attribute Data Stride
----------------------------------------------------------------------

WebGL は 255 バイトまでの頂点属性データまたがりをサポートしている。
``stride`` 引数の値が 255 を超えると ``vertexAttribPointer`` の呼び出しは ``INVALID_VALUE`` エラーとなる。

6.14 Viewport Depth Range
----------------------------------------------------------------------

WebGL は近平面が遠平面よりも大きな値に写像される奥行き範囲をサポートしていない。
``zNear`` が ``zFar`` よりも大きい場合、
``depthRange`` の呼び出しは ``INVALID_OPERATION`` エラーとなる。

6.15 Blending With Constant Color
----------------------------------------------------------------------

WebGL ではブレンド関数の ``source`` および ``destination`` 因数として、
コンスタント色とコンスタントアルファーを一緒に使用することはできない。

* ``blendFunc`` の呼び出しでは、二つの因数の一方が ``CONSTANT_COLOR`` または ``ONE_MINUS_CONSTANT_COLOR`` に設定され、
  もう一方が ``CONSTANT_ALPHA`` または ``ONE_MINUS_CONSTANT_ALPHA`` に設定されている場合、
  ``INVALID_OPERATION`` エラーとなる。

* ``blendFuncSeparate`` の呼び出しでは、次の場合に ``INVALID_OPERATION`` エラーとなる：

  * ``srcRGB`` が ``CONSTANT_COLOR`` または ``ONE_MINUS_CONSTANT_COLOR`` に設定され、
    ``dstRGB`` が ``CONSTANT_ALPHA`` または ``ONE_MINUS_CONSTANT_ALPHA`` に設定された場合、
  * またはその逆の場合。

6.16 Fixed point support
----------------------------------------------------------------------

WebGL は ``GL_FIXED`` データ型をサポートしない。

6.17 GLSL Constructs
----------------------------------------------------------------------

``webgl_`` および ``_webgl_`` で始まる識別子は WebGL で使用するために予約されている。

6.18 Extension Queries
----------------------------------------------------------------------

* OpenGL ES 2.0 では ``glGetString(GL_EXTENSIONS)`` を呼び出すことで
  利用可能な拡張機能が決定し、空白文字で区切られた拡張機能文字列のリストを返す。
* WebGL は、``EXTENSIONS`` 列挙が削除された。
  代わって、利用可能な拡張機能の集合を決定するのに ``getSupportedExtensions`` を呼び出す。

6.19 Compressed Texture Support
----------------------------------------------------------------------

コア WebGL では、サポートされる圧縮テクスチャーフォーマットが定義されていない。
そのため、他の拡張機能が有効になっていない場合は

* ``compressedTexImage2D`` と ``compressedTexSubImage2D`` は ``INVALID_ENUM`` エラーとなる。
* 引数 ``COMPRESSED_TEXTURE_FORMATS`` を指定して ``getParameter`` を呼び出すと、空の ``Uint32Array`` 型配列が返される。

6.20 Maximum GLSL Token Size
----------------------------------------------------------------------

* GLSL ES ではトークンの長さに制限を設けていない。
* WebGL では 256 文字までのトークンをサポートする必要がある。
  256 文字より長いトークンを含むシェーダーはコンパイルに失敗せねばならない。

6.21 Characters Outside the GLSL Source Character Set
----------------------------------------------------------------------

WebGL は、任意の ``DOMString`` をエラーなしで ``shaderSource`` に渡すことをサポートしている。
しかし、シェーダーのコンパイル時には、GLSL の前処理とコメントの除去を行った後、
残りのすべての文字が GLSL ES 2.0 の文字集合内になければならない。
そうでなければ、シェーダーのコンパイルに失敗せねばならない。

特に、これは次のことを認める：

* コメント中の非 ASCII Unicode 文字
* 前処理器が排除するブロック内にある無効な文字

  .. code:: glsl

     #ifdef __cplusplus
     #line 42 "foo.glsl"
     #endif

  二重引用符は GLSL の文字集合外のものだが、前処理で除去されるので許される。

----

囲み部分の記述はどうでもいいので省略。

----

この集合に含まれていない文字を含む文字列が、他のシェーダー関連のエントリーポイント
``bindAttribLocation``, ``getAttribLocation``, ``getUniformLocation`` に渡された場合、
``INVALID_VALUE`` エラーとなる。

6.22 Maximum Nesting of Structures in GLSL Shaders
----------------------------------------------------------------------

WebGLでは GLSL シェーダー内の構造体の入れ子の数に制限がある。

* 入れ子は、構造体のフィールドが別の構造体型を参照している場合に起こる。
* GLSL ES では、埋め込み構造体の定義を禁止している。
* トップレベルの構造体定義のフィールドの入れ子階層は 1 とする。

WebGL では構造体の入れ子階層が 4 までサポートされている必要がある。

* 4 階層以上の入れ子を含むシェーダーはコンパイルに失敗せねばならない。

6.23 Maximum Uniform and Attribute Location Lengths
----------------------------------------------------------------------

WebGL では ``uniform`` や ``attribute`` の位置の長さに 256 文字という制限を設けている。

6.24 String Length Queries
----------------------------------------------------------------------

WebGL では、列挙型

* ``INFO_LOG_LENGTH``
* ``SHADER_SOURCE_LENGTH``
* ``ACTIVE_UNIFORM_MAX_LENGTH``
* ``ACTIVE_ATTRIBUTE_MAX_LENGTH``

が削除された。
OpenGL ES 2.0 では、``glGetActiveAttrib`` などの呼び出しに渡されるバッファーのサイズを決定するために、
これらの列挙型が必要だった。
WebGL では、類似の呼び出し

* ``getActiveAttrib``,
* ``getActiveUniform``,
* ``getProgramInfoLog``,
* ``getShaderInfoLog``,
* ``getShaderSource``

はすべて ``DOMString`` を返す。

6.25 Texture Type in TexSubImage2D Calls
----------------------------------------------------------------------

WebGL では ``texSubImage2D`` に渡される ``type`` 引数は、
テクスチャーオブジェクトを最初に定義した（つまり ``texImage2D`` を使用した）ときに使用された
``type`` と一致しなければならない。

6.26 Packing Restrictions for Uniforms and Varyings
----------------------------------------------------------------------

OpenGL ES Shading Language, Version 1.00 の Appendix A, Section 7
"Counting of Varyings and Uniforms" では、シェーダー内のすべての ``uniform`` 変数と
``varying`` 変数に必要な記憶域を計算するための保守的なアルゴリズムを定義している。

GLSL ES では、Appendix A で定義されたパッキングアルゴリズムが成功すると、
そのシェーダーは対象プラットフォームでのコンパイルに成功しなければならないとある。

WebGL ではさらに、シェーダーの ``uniform`` 変数またはプログラムの
``varing`` 変数のいずれかでパッキングアルゴリズムが失敗した場合、
コンパイルまたはリンクが失敗することを要求する。

Instead of using a fixed size grid of registers, the number of rows in the target architecture is determined in the following ways:
レジスターの固定サイズのグリッドを使用する代わりに、対象アーキテクチャーの行数は次の方法で決定する：

when counting uniform variables in a vertex shader: getParameter(MAX_VERTEX_UNIFORM_VECTORS)
when counting uniform variables in a fragment shader: getParameter(MAX_FRAGMENT_UNIFORM_VECTORS)
when counting varying variables: getParameter(MAX_VARYING_VECTORS)

* 頂点シェーダーで ``uniform`` 変数をカウントするときは ``getParameter(MAX_VERTEX_UNIFORM_VECTORS)``
* フラグメントシェーダーで ``uniform`` 変数をカウントするときは ``getParameter(MAX_FRAGMENT_UNIFORM_VECTORS)``
* ``varying`` 変数をカウントするときは ``getParameter(MAX_VARYING_VECTORS)``

----

囲み部分の文言はだいたい次のような内容：

* 上の記述はパッキングアルゴリズムによる制約のために、
  シェーダーやプログラムのコンパイルやリンクが失敗しなければならない状況を定義している。
  このアルゴリズムによって変数が正常にパッキングされる必要最小限の量よりも多くの変数を使用するシェーダーが正常にコンパイルされることは保証していない。
* スカラー配列を拡張して複数の列を消費するなど、非効率的な実装が見受けられる。
* 開発者は、複数の変数の列への自動パッキングに大きく依存することは避けるべきだ。
  代わりに、``vec4`` のようなより大きな変数を定義し、
  明示的に右端の列に値を詰めるように。

6.27 Feedback Loops Between Textures and the Framebuffer
----------------------------------------------------------------------

* OpenGL ES 2.0 では、同じテクスチャーへの書き込みと読み込みの両方を行う呼び出しが可能であり、
  フィードバックループが発生する。このようなフィードバックループが存在する場合、
  未定義の動作が生じることが明記されている。
* WebGL では、このようなフィードバックループを引き起こすような操作を行うと、
  ``INVALID_OPERATION`` エラーとなる。

6.28 Reading From a Missing Attachment
----------------------------------------------------------------------

OpenGL ES 2.0 では、色 attachment のない完全フレームバッファーから
色データに関する ``readPixels`` を行うというように、
attachment のないデータをコマンドが ``source`` にしようとした場合にどうなるかは規定されていない。

WebGL では、欠落 attachment からのデータを必要とするこのような操作は
``INVALID_OPERATION`` エラーとなる。

これは次の関数に適用される：

* ``copyTexImage2D``
* ``copyTexSubImage2D``
* ``readPixels``

6.29 Drawing To a Missing Attachment
----------------------------------------------------------------------

In the OpenGL ES 2.0 API, it is not specified what happens when a command tries to draw to a missing attachment, such as clearing a draw buffer from a complete framebuffer that does not have a color attachment.
OpenGL ES 2.0 では、色 attachment のない完全フレームバッファーから
描画バッファーを消去するなどのような、コマンドが見つからない attachment に
描画しようとしたときにどうなるかが規定されていない。

WebGL API では、欠落 attachment に描画するような操作は、
その attachment に何も描画しない。エラーではない。

これは次の関数に適用される：

* ``clear``
* ``drawArrays``
* ``drawElements``

6.30 NaN Line Width
----------------------------------------------------------------------

``lineWidth`` に渡される ``width`` 引数に ``NaN`` が設定されていると、
``INVALID_VALUE`` エラーとなり、線幅を変更しない。

6.31 Attribute Aliasing
----------------------------------------------------------------------

It is possible for an application to bind more than one attribute name to the same location. This is referred to as aliasing. When more than one attributes that are aliased to the same location are active in the executable program, linkProgram should fail.

6.32 Initial value for gl_Position
----------------------------------------------------------------------

The GLSL ES [GLES20GLSL] spec leaves the value of gl_Position as undefined unless it is written to in a vertex shader. WebGL guarantees that gl_Position's initial value is (0,0,0,0).

6.33 GLSL ES Global Variable Initialization
----------------------------------------------------------------------

The GLSL ES 1.00 [GLES20GLSL] spec restricts global variable initializers to be constant expressions. In the WebGL API, it is allowed to use other global variables not qualified with the const qualifier and uniform values in global variable initializers in GLSL ES 1.00 shaders. Global variable initializers must be global initializer expressions, which are defined as one of:

a constant expression
a user-defined global variable
a uniform
an expression formed by an operator on operands that are global initializer expressions, including getting an element of a global initializer vector or global initializer matrix, or a field of a global initializer structure
a constructor whose arguments are all global initializer expressions
a built-in function call whose arguments are all global initializer expressions, with the exception of the texture lookup functions
The following may not be used in global initializer expressions:

User-defined functions
Attributes and varyings
Built-in variables with the exception of constant expressions
Global variables as l-values in an assignment or other operation
Compilers should generate a warning when a global variable initializer is in violation of the unmodified GLSL ES spec i.e. when a global variable initializer is not a constant expression.

This behavior has existed in WebGL implementations for several years. Fixing this behavior to be consistent with the GLSL ES specification would have a large compatibility impact with existing content.

6.34 GLSL ES Preprocessor "defined" Operator
----------------------------------------------------------------------

The C++ standard, which the GLSL ES preprocessor specification refers to, has undefined behavior when the defined operator is generated by macro replacement when parsing the controlling expression of an #if or #elif directive. When shader code processed by the WebGL API generates the token defined during macro replacement inside a preprocessor expression, that must result in a compiler error.

This has no effect on macro expansion outside preprocessor directives that handle the defined operator.

Using defined as a macro name also has undefined behavior in the C++ standard. In the WebGL API, using defined as a macro name must result in a compiler error.

Behavior of the WebGL API should be consistent in cases where the native API spec allows undefined behavior.

6.35 GLSL ES #extension directive location
----------------------------------------------------------------------

The GLSL ES 1.00 [GLES20GLSL] specification mandates that #extension directives must occur before any non-preprocessor tokens unless the extension specification says otherwise. In the WebGL API, #extension directives may always occur after non-preprocessor tokens in GLSL ES 1.00 shaders. The scope of #extension directives in GLSL ES 1.00 shaders is always the whole shader, and #extension directives that occur later override those seen earlier for the whole shader.

Letting extensions determine where the #extension directives should be placed has resulted in a lot of room for interpretation in the spec. In practice GLES implementations have not enforced the rule that's written in the GLSL ES spec, and neither have WebGL implementations, so relaxing the rule is the only way to make the spec well-defined while being compatible with existing content.

6.36 Completeness of Cube Map Framebuffer Attachments
----------------------------------------------------------------------

In the WebGL API, a face of a cube map that is not cube complete is not framebuffer attachment complete. Querying framebuffer status when a face of an incomplete cube map is attached must return FRAMEBUFFER_INCOMPLETE_ATTACHMENT.

APIs that WebGL is implemented on, including recent OpenGL core versions and OpenGL ES 3.0 and newer, have a requirement that cube map faces used as a framebuffer attachment must be part of a cube complete cube map. See for example OpenGL ES 3.0.4 §4.4.4 "Framebuffer Completeness", subsection "Framebuffer Attachment Completeness".

6.37 Transferring vertices when current program is null
----------------------------------------------------------------------

Any command that transfers vertices to the GL generates INVALID_OPERATION if the CURRENT_PROGRAM is null. This includes drawElements and drawArrays.

6.38 Fragment shader output
----------------------------------------------------------------------

If a fragment shader writes to neither gl_FragColor nor gl_FragData, the values of the fragment colors following shader execution are untouched.

6.39 Initial values for GLSL local and global variables
----------------------------------------------------------------------

The GLSL ES [GLES20GLSL] spec leaves the value of local and global variables as undefined unless they are initialized by the shader. WebGL guarantees that such variables are initialized to zero: 0.0, vec4(0.0), 0, false, etc.

6.40 Vertex attribute conversions from normalized signed integers to floating point
----------------------------------------------------------------------

The OpenGL ES 2.0 spec [GLES20] section 2.1.2 "Data Conversions", subsection "Conversion from Integer to Floating-Point" defines conversion from a normalized signed integer c, where the bit width of the type is b, to floating-point value f as:

f = (2*c + 1) / (2^b - 1)
During conversions of signed normalized vertex attributes to floating point, WebGL 1.0 implementations may optionally use this conversion rule, which preserves zeros:
f = max(c / (2^(b - 1) - 1), -1.0)
Some APIs on which WebGL 1.0 is built on use the second rule, and since this conversion is done in fixed-function hardware, it is not possible to emulate one behavior or the other. This difference in behavior does not affect most applications, so a query to determine which behavior is being used has not been added to the WebGL rendering context.

6.41 Uniform and attribute name collisions
----------------------------------------------------------------------

If any of the shaders attached to a WebGL program declare a uniform that has the same name as a statically used vertex attribute, program linking should fail.

This behavior differs from one specified in GLSL ES 3.00.6 section 12.47.
WebGL implementations have enforced this behavior for several years now, due to that some OpenGL drivers don't accept uniforms and vertex attributes with the same name.

6.42 Wide point primitive clipping
----------------------------------------------------------------------

POINTS primitives may or may not be discarded if the vertex lies outside the clip volume, but within the near and far clip planes.

Clipping of wide points works differently in GLES and GL, and this difference in behavior is prohibitive to work around in implementations.

OpenGL ES 2.0.25 p46:

If the primitive under consideration is a point, then clipping discards it if it lies outside the near or far clip plane; otherwise it is passed unchanged.
OpenGL 3.2 Core p97:

If the primitive under consideration is a point, then clipping passes it unchanged if it lies within the clip volume; otherwise, it is discarded.

7 References
======================================================================

[CANVAS]
HTML5: The Canvas Element, World Wide Web Consortium (W3C).
[OFFSCREENCANVAS]
HTML Living Standard - The OffscreenCanvas interface, WHATWG.
[CANVASCONTEXTS]
Canvas Context Registry, WHATWG.
[ECMASCRIPT]
ECMAScript® 2015 Language Specification, Ecma International, 2015.
[GL32CORE]
The OpenGL® Graphics System: A Specification (Version 3.2 (Core Profile) - December 7, 2009), M. Segal, K. Akeley, December 2009.
[GLES20]
OpenGL® ES Common Profile Specification Version 2.0.25, A. Munshi, J. Leech, November 2010.
[GLES20GLSL]
The OpenGL® ES Shading Language Version 1.00, R. Simpson, May 2009.
[REGISTRY]
WebGL Extension Registry
[RFC2119]
Key words for use in RFCs to Indicate Requirement Levels, S. Bradner. IETF, March 1997.
[CSS]
Cascading Style Sheets Level 2 Revision 1 (CSS 2.1) Specification, B. Bos, T. Celik, I. Hickson, H. W. Lie, June 2011.
[CORS]
Cross-Origin Resource Sharing, A. van Kesteren, July 2010.
[DOM4]
DOM4, A. van Kesteren, A. Gregor, Ms2ger.
[DOM3EVENTS]
Document Object Model (DOM) Level 3 Events Specification, Doug Schepers and Jacob Rossi. W3C.
[HTML]
HTML, I. Hickson, June 2011.
[WEBIDL]
Web IDL: W3C Editor’s Draft, C. McCormack, B. Zbarsky, T. Langel.
[ASCII]
International Standard ISO/IEC 646:1991. Information technology - ISO 7-bit coded character set for information interchange
[DOMSTRING]
Document Object Model Core: The DOMString type, World Wide Web Consortium (W3C).
[KHRROBUSTACCESS]
KHR_robust_buffer_access_behavior OpenGL ES extension, Leech, J. and Daniell, P., August, 2014.
[MULTIPLEBUFFERING]
(Non-normative) Multiple buffering. Wikipedia.
[WEBCODECS]
(Non-normative) WebCodecs API, C. Cunningham, P. Adenot, B. Aboba. W3C.

8 Acknowledgments
======================================================================

This specification is produced by the Khronos WebGL Working Group.

Special thanks to: Arun Ranganathan (Mozilla), Chris Marrin (Apple), Jon Leech, Kenneth Russell (Google), Kenneth Waters (Google), Mark Callow (HI), Mark Steele (Mozilla), Oliver Hunt (Apple), Tim Johansson (Opera), Vangelis Kokkevis (Google), Vladimir Vukicevic (Mozilla), Gregg Tavares (Google)

Additional thanks to: Alan Hudson (Yumetech), Benoit Jacob (Mozilla), Bill Licea Kane (AMD), Boris Zbarsky (Mozilla), Cameron McCormack (Mozilla), Cedric Vivier (Zegami), Dan Gessel (Apple), David Ligon (Qualcomm), David Sheets (Ashima Arts), Glenn Maynard, Greg Roth (Nvidia), Jacob Strom (Ericsson), Jeff Gilbert (Mozilla), Kari Pulli (Nokia), Teddie Stenvi (ST-Ericsson), Neil Trevett (Nvidia), Per Wennersten (Ericsson), Per-Erik Brodin (Ericsson), Shiki Okasaka (Google), Tom Olson (ARM), Zhengrong Yao (Ericsson), and the members of the Khronos WebGL Working Group.
