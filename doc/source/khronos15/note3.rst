======================================================================
WebGL Specification 1.0 読書ノート 3 of 4
======================================================================

`WebGL Specification <https://www.khronos.org/registry/webgl/specs/latest/1.0/>`__
を読んでいく。

.. contents:: ノート目次

.. _khronos15-6:

6 Differences Between WebGL and OpenGL ES 2.0
======================================================================

この節では OpenGL ES 2.0 API に対する WebGL API の変更点について述べられている。
さまざまな OS やデバイス間での移植性を高めるのが目的のようだ。

.. _khronos15-6.1:

6.1 Buffer Object Binding
----------------------------------------------------------------------

* 指定されたバッファーオブジェクトには頂点またはインデックスのいずれか一方が含ま
  れ、両方は含まれないことを意味する。
* ``WebGLBuffer`` の型は ``bindBuffer`` の引数として初回に渡されたときに初期化さ
  れる。同じ ``WebGLBuffer`` を他の束縛点に束縛しようとする ``bindBuffer`` への
  以降の呼び出しは ``INVALID_OPERATION`` エラーとなり、束縛点の状態は変更しな
  い。

6.2 No Client Side Arrays
----------------------------------------------------------------------

* WebGL はクライアントサイドの配列をサポートしていない。
* ``enableVertexAttribArray`` によって頂点属性が配列として有効になっているにもか
  かわらず、その属性にバッファーが束縛されていない場合（通常は ``bindBuffer`` と
  ``vertexAttribPointer`` を使用）、描画コマンド ``drawArrays`` または
  ``drawElements`` は ``INVALID_OPERATION`` エラーとなる。
* インデックス付きの描画コマンド ``drawElements`` が呼び出され、
  ``ELEMENT_ARRAY_BUFFER`` 束縛点に ``WebGLBuffer`` が束縛されていない場合は
  ``INVALID_OPERATION`` エラーが発生する。
* ``ARRAY_BUFFER`` 束縛点に束縛された ``WebGLBuffer`` がない状態で
  ``vertexAttribPointer`` が呼び出され、``offset`` が 0 以外の場合
  ``INVALID_OPERATION`` エラーとなる。

.. admonition:: Rationale

   クライアント側の配列がサポートされていないにもかかわらず、
   ``VERTEX_ATTRIB_ARRAY_BUFFER_BINDING`` を ``null`` に設定することを認めると、
   束縛を元の状態にクリアすることができる。これは他の方法では厳密には不可能だ。

6.3 No Default Textures
----------------------------------------------------------------------

WebGL はデフォルトのテクスチャーをサポートしない。

テクスチャー関連の操作や問い合わせを成功させるためには、``null`` ではない
``WebGLTexture`` オブジェクトが束縛されている必要がある。

6.4 No Shader Binaries
----------------------------------------------------------------------

* コンパイルされたシェーダーのバイナリー表現へのアクセスを WebGL はサポートしな
  い。これには OpenGL ES 2.0 ShaderBinary エントリーポイントを含む。
* また、WebGL では ``getParameter`` を通じてシェーダーのバイナリー形式やシェー
  ダーコンパイラーの有無を問い合わせることもサポートされていない。
* WebGL の実装すべてが、オンラインのシェーダーコンパイラーを暗黙のうちにサポート
  する必要がある。

.. _khronos15-6.5:

6.5 Buffer Offset and Stride Requirements
----------------------------------------------------------------------

* ``drawElements`` および ``vertexAttribPointer`` への ``offset`` 引数、および
  ``vertexAttribPointer`` への ``stride`` 引数は、呼び出しに渡されたデータ型のサ
  イズの倍数でなければならない。そうでない場合は ``INVALID_OPERATION`` エラーと
  なる。

.. admonition:: Rationale

   これは OpenGL ES 2.0.25 [GLES20]_ p24 の要件に準拠している。

* さらに ``drawElements`` の ``offset`` 引数は非負でなければならない。そうでない
  場合は ``INVALID_VALUE`` エラーとなる。

.. _khronos15-6.6:

6.6 Enabled Vertex Attributes and Range Checking
----------------------------------------------------------------------

アクティブな頂点属性が配列として有効になっている場合に、``drawArrays`` で直接的
に、またはインデックス付きの描画から ``drawElements`` で間接的にデータを取得する
必要がある描画コマンドを呼び出すと、``WebGLBuffer`` の境界外のデータを要求する可
能性がある。このような場合、以下の動作のいずれかが起こる。

1. WebGL の実装では、``INVALID_OPERATION`` エラーとなり、ジオメトリーが描画され
   ないことがある。
2. 範囲外の頂点取得が以下のいずれかの値を返すことがある：

   * バッファーオブジェクト内の任意の場所にある値。
   * ゼロか、またはベクトル読み込みに対しては ``(0, 0, 0, x)`` の形のベクトル。
     ここで ``x`` はベクトル成分の型で表現される有効な値であり、以下のいずれか：

     * 整数成分の場合 0, 1, または表現可能な最大の正の整数値
     * 浮動小数点成分の場合 0.0 または 1.0

.. admonition:: Non-normative

   この動作は [KHRROBUSTACCESS]_ で定義されたものと同じだ。

頂点の属性が配列として有効であり、その属性にバッファーが束縛されていて、その属性
を現在のプログラムが消費していない場合、束縛されたバッファーのサイズに関わらず、
``drawArrays`` や ``drawElements`` を呼び出すときにエラーが発生することはない。

6.7 Out-of-bounds fetches from the index buffer
----------------------------------------------------------------------

``ELEMENT_ARRAY_BUFFER`` の境界外のインデックス要素を取得するような
``drawElements`` 呼び出しは ``INVALID_OPERATION`` エラーとなる。

6.8 Framebuffer Object Attachments
----------------------------------------------------------------------

WebGL はフレームバッファーオブジェクトの付着点 ``DEPTH_STENCIL_ATTACHMENT`` と、
レンダーバッファーの内部フォーマット ``DEPTH_STENCIL`` を加える。

* 奥行きとステンシルバッファーの両方をフレームバッファーオブジェクトに取り付ける
  には、

  #. ``DEPTH_STENCIL`` 内部フォーマットにて ``renderbufferStorage`` を呼び出し、
  #. 次に ``DEPTH_STENCIL_ATTACHMENT`` 付着点にて ``framebufferRenderbuffer`` を
     呼び出す。

* ``DEPTH_ATTACHMENT`` 付着点に取り付けられたレンダーバッファーは、
  ``DEPTH_COMPONENT16`` 内部フォーマットで割り当てられなければならない。
* ``STENCIL_ATTACHMENT`` 付着点に取り付けられたレンダーバッファーは、
  ``STENCIL_INDEX8`` 内部フォーマットで割り当てられなければならない。
* ``DEPTH_STENCIL_ATTACHMENT`` 付着点に取り付けられたレンダーバッファーは、
  ``DEPTH_STENCIL`` 内部フォーマットで割り当てられなければなりません。

WebGL では、次の付着点の組み合わせと同時にレンダーバッファーを取り付けるとエラー
になる：

* ``DEPTH_ATTACHMENT`` + ``DEPTH_STENCIL_ATTACHMENT``
* ``STENCIL_ATTACHMENT`` + ``DEPTH_STENCIL_ATTACHMENT``
* ``DEPTH_ATTACHMENT`` + ``STENCIL_ATTACHMENT``

上記の拘束条件のいずれかに違反している場合：

* ``checkFramebufferStatus`` は ``FRAMEBUFFER_UNSUPPORTED`` を返すものとする。
* フレームバッファーを変更または読み取る次の呼び出しは
  ``INVALID_FRAMEBUFFER_OPERATION`` エラーとなり、フレームバッファー、
  destination テクスチャーまたは destination メモリーの内容物に触ることなく、
  早々に戻らなければならない。

  * ``clear``
  * ``copyTexImage2D``
  * ``copyTexSubImage2D``
  * ``drawArrays``
  * ``drawElements``
  * ``readPixels``

以下のフレームバッファーオブジェクトの取り付けの組み合わせは、すべての取り付けが
フレームバッファー付着完全であり、ゼロではなく、同じ幅と高さを持つ場合、フレーム
バッファーがフレームバッファー完全になる必要がある：

* ``COLOR_ATTACHMENT0`` = ``RGBA``/``UNSIGNED_BYTE`` テクスチャー
* ``COLOR_ATTACHMENT0`` = ``RGBA``/``UNSIGNED_BYTE`` テクスチャー +
  ``DEPTH_ATTACHMENT`` = ``DEPTH_COMPONENT16`` レンダーバッファー
* ``COLOR_ATTACHMENT0`` = ``RGBA``/``UNSIGNED_BYTE`` テクスチャー +
  ``DEPTH_STENCIL_ATTACHMENT`` = ``DEPTH_STENCIL`` レンダーバッファー

.. _khronos15-6.9:

6.9 Texture Upload Width and Height
----------------------------------------------------------------------

``texImage2D`` が設定するテクスチャーの寸法、および ``texSubImage2D`` で更新され
る部分矩形の寸法は、``width`` と ``height`` の引数が明示的に指定されない限り、
アップロードされた ``TexImageSource`` ``source`` オブジェクトに基づいて決定す
る。

----

型が ``ImageData`` である ``source`` の場合
    テクスチャーの寸法は ``ImageData`` オブジェクトの ``width`` と ``height`` の
    プロパティーの現在の値に設定され、そのオブジェクトの実際のピクセル幅と高さを
    表す。

型が ``HTMLImageElement`` である ``source`` の場合
    ビットマップがアップロードされた場合、テクスチャーの寸法は、アップロードされ
    たビットマップの寸法（ピクセル単位）に設定される。

    SVG イメージがアップロードされた場合、テクスチャー寸法は、
    ``HTMLImageElement`` オブジェクトの ``width`` および ``height`` プロパティー
    の現在の値に設定される。

型が ``HTMLCanvasElement`` または ``OffscreenCanvas`` である ``source`` の場合
    テクスチャーの寸法は、キャンバスオブジェクトの ``width`` と ``height`` プロ
    パティーの現在の値に設定される。

型が ``HTMLVideoElement`` または ``VideoFrame`` [WEBCODECS]_ である ``source``
    の場合テクスチャーの寸法は、ビデオのアップロードされたフレームの寸法（ピクセ
    ル単位）に設定される。

.. _khronos15-6.10:

6.10 Pixel Storage Parameters
----------------------------------------------------------------------

WebGL では ``pixelStorei`` に次の追加パラメーターをサポートする：

``UNPACK_FLIP_Y_WEBGL``
    設定されている場合、それ以降の ``texImage2D`` または ``texSubImage2D`` の呼
    び出しの際に、元データを垂直に反転し、概念的には最後の行を最初に転送するよう
    になる。

    * 初期値は ``false`` とする。ゼロ以外の値は ``true`` と解釈される。

``UNPACK_PREMULTIPLY_ALPHA_WEBGL``
    設定された場合、それ以降の ``texImage2D`` または ``texSubImage2D`` の呼び出
    しの際に、元データのアルファーチャンネルが存在する場合は、それをデータ転送中
    にカラーチャンネルに乗算する。

    * 初期値は ``false`` とする。ゼロ以外の値は ``true`` と解釈される。

``UNPACK_COLORSPACE_CONVERSION_WEBGL``
    ``BROWSER_DEFAULT_WEBGL`` に設定された場合、``HTMLImageElement`` を取る後続
    の ``texImage2D`` および ``texSubImage2D`` 呼び出し中に、ブラウザーの既定の色
    空間変換を適用する。

    * 正確な変換は、ブラウザーとファイルタイプの両方に固有のものとなる。
    * ``NONE`` に設定された場合、色空間の変換を適用しない。
    * 初期値は ``BROWSER_DEFAULT_WEBGL`` とする。
    * ``TexImageSource`` が ``ImageBitmap`` の場合は、これら三つの引数を無視す
      る。代わりに、同等の ``ImageBitmapOptions`` を使用して、所望のフォーマット
      の ``ImageBitmap`` を作成する必要がある。

.. _khronos15-6.11:

6.11 Reading Pixels Outside the Framebuffer
----------------------------------------------------------------------

WebGL にはフレームバッファーを読み込む関数が三つある。

* ``copyTexImage2D``
* ``copyTexSubImage2D``
* ``readPixels``

``copyTexImage2D`` は、束縛フレームバッファーの外側にあるどのピクセルに対しても
RGBA 値 ``(0, 0, 0, 0)`` を生成するように定義されている。

``copyTexSubImage2D`` と ``readPixels`` は、束縛フレームバッファーの外側にあるど
のピクセルに対しても、対応する destination 範囲に触れぬように定義されている。

.. _khronos15-6.12:

6.12 Stencil Separate Mask and Reference Value
----------------------------------------------------------------------

WebGL では、ステンシルテストが有効で、現在束縛されているフレームバッファーにステ
ンシルバッファーがある場合、以下のいずれかのケースが成立している間の描画は違法と
する。これを行うと ``INVALID_OPERATION`` エラーだ。

* ``(STENCIL_WRITEMASK & maxStencilValue) != (STENCIL_BACK_WRITEMASK & maxStencilValue)``

  （面の ``FRONT`` および ``BACK`` の値それぞれに関連付けられた ``mask`` 引数に対する ``stencilMaskSeparate`` で指定されたとして）
* ``(STENCIL_VALUE_MASK & maxStencilValue) != (STENCIL_BACK_VALUE_MASK & maxStencilValue)``

  （面の ``FRONT`` および ``BACK`` の値それぞれに関連付けられた ``mask`` 引数に対する ``stencilFuncSeparate`` で指定されたとして）
* ``clamp(STENCIL_REF, 0, maxStencilValue) != clamp(STENCIL_BACK_REF, 0, maxStencilValue)``

  （面の ``FRONT`` および ``BACK`` の値それぞれに関連付けられた ``ref`` 引数に対する ``stencilFuncSeparate`` で指定されたとして）

ここで、``maxStencilValue`` は ``((1 << s) - 1)`` であり、``s`` は描画フレーム
バッファーのステンシルビット数とする。

* ステンシルビットが存在しない場合は、これらのチェックは常に合格とする。

.. _khronos15-6.13:

6.13 Vertex Attribute Data Stride
----------------------------------------------------------------------

WebGL は 255 バイトまでの頂点属性データまたがりをサポートしている。``stride``
引数の値が 255 を超えると ``vertexAttribPointer`` の呼び出しは ``INVALID_VALUE``
エラーとなる。

.. _khronos15-6.14:

6.14 Viewport Depth Range
----------------------------------------------------------------------

WebGL は近平面が遠平面よりも大きな値に写像される奥行き範囲をサポートしていない。
``zNear`` が ``zFar`` よりも大きい場合、``depthRange`` の呼び出しは
``INVALID_OPERATION`` エラーとなる。

.. _khronos15-6.15:

6.15 Blending With Constant Color
----------------------------------------------------------------------

WebGL ではブレンド関数の ``source`` および ``destination`` 因数として、コンスタ
ント色とコンスタントアルファーを一緒に使用することはできない。

* ``blendFunc`` の呼び出しでは、二つの因数の一方が ``CONSTANT_COLOR`` または
  ``ONE_MINUS_CONSTANT_COLOR`` に設定され、もう一方が ``CONSTANT_ALPHA`` または
  ``ONE_MINUS_CONSTANT_ALPHA`` に設定されている場合、``INVALID_OPERATION`` エ
  ラーとなる。

* ``blendFuncSeparate`` の呼び出しでは、次の場合に ``INVALID_OPERATION`` エラー
  となる：

  * ``srcRGB`` が ``CONSTANT_COLOR`` または ``ONE_MINUS_CONSTANT_COLOR`` に設定
    され、``dstRGB`` が ``CONSTANT_ALPHA`` または ``ONE_MINUS_CONSTANT_ALPHA``
    に設定された場合、
  * またはその逆の場合。

6.16 Fixed point support
----------------------------------------------------------------------

WebGL は ``GL_FIXED`` データ型をサポートしない。

.. _khronos15-6.17:

6.17 GLSL Constructs
----------------------------------------------------------------------

:ref:`khronos15-4.3` によって、``webgl_`` および ``_webgl_`` で始まる識別子は
WebGL で使用するために予約されている。

6.18 Extension Queries
----------------------------------------------------------------------

* OpenGL ES 2.0 では ``glGetString(GL_EXTENSIONS)`` を呼び出すことで利用可能な拡
  張機能が決定し、空白文字で区切られた拡張機能文字列のリストを返す。
* WebGL は、``EXTENSIONS`` 列挙が削除された。代わって、利用可能な拡張機能の集合
  を決定するのに ``getSupportedExtensions`` を呼び出す。

.. _khronos15-6.19:

6.19 Compressed Texture Support
----------------------------------------------------------------------

コア WebGL では、サポートされる圧縮テクスチャーフォーマットが定義されていない。
そのため、他の拡張機能が有効になっていない場合は

* ``compressedTexImage2D`` と ``compressedTexSubImage2D`` は ``INVALID_ENUM`` エ
  ラーとなる。
* 引数 ``COMPRESSED_TEXTURE_FORMATS`` を指定して ``getParameter`` を呼び出すと、
  空の ``Uint32Array`` 型配列が返される。

.. _khronos15-6.20:

6.20 Maximum GLSL Token Size
----------------------------------------------------------------------

* GLSL ES [GLES20GLSL]_ ではトークンの長さに制限を設けていない。
* WebGL では 256 文字までのトークンをサポートする必要がある。256 文字より長い
  トークンを含むシェーダーはコンパイルに失敗せねばならない。

.. _khronos15-6.21:

6.21 Characters Outside the GLSL Source Character Set
----------------------------------------------------------------------

WebGL は、任意の ``DOMString`` [DOMSTRING]_ をエラーなしで ``shaderSource`` に渡
すことをサポートしている。しかし、シェーダーのコンパイル時には、GLSL の前処理と
コメントの除去を行った後、残りのすべての文字が [GLES20GLSL]_ の文字集合内になけ
ればならない。そうでなければ、シェーダーのコンパイルに失敗せねばならない。

特に、これは次のことを認める：

* コメント中の非 ASCII Unicode 文字
* 前処理器が排除するブロック内にある無効な文字

  .. code:: glsl

     #ifdef __cplusplus
     #line 42 "foo.glsl"
     #endif

  二重引用符は GLSL の文字集合外のものだが、前処理で除去されるので許される。

.. admonition:: Rationale

   GLSL ES [GLES20GLSL]_では、シェーディング言語 OpenGL ES のソース文字集合セッ
   トを、一般に ASCII と呼ばれる ISO/IEC 646:1991 の部分集合として定義してる。
   GLSL の実装によっては、コメントであっても ASCII の範囲外の文字を許さないもの
   もある。ブラウザーは DOMString の全文字集合の前処理を正しく処理しなければなら
   ないが、 WebGL の実装は一般的に、安全のために GLSL ドライバーに送られるシェー
   ダソースがASCII のみを含むようにするべきだ。実装では、必要に応じて空行を挿入
   するなどして、デバッグのために行番号を保持するべきだ。

この集合に含まれていない文字を含む文字列が、他のシェーダー関連のエントリーポイント
``bindAttribLocation``, ``getAttribLocation``, ``getUniformLocation`` に渡された場合、
``INVALID_VALUE`` エラーとなる。

.. _khronos15-6.22:

6.22 Maximum Nesting of Structures in GLSL Shaders
----------------------------------------------------------------------

WebGLでは GLSL シェーダー内の構造体の入れ子の数に制限がある。

* 入れ子は、構造体のフィールドが別の構造体型を参照している場合に起こる。
* GLSL ES [GLES20GLSL]_ では、埋め込み構造体の定義を禁止している。
* トップレベルの構造体定義のフィールドの入れ子階層は 1 とする。

WebGL では構造体の入れ子階層が 4 までサポートされている必要がある。

* 4 階層以上の入れ子を含むシェーダーはコンパイルに失敗せねばならない。

.. _khronos15-6.23:

6.23 Maximum Uniform and Attribute Location Lengths
----------------------------------------------------------------------

WebGL では ``uniform`` や ``attribute`` の位置の長さに 256 文字という制限を設け
ている。

6.24 String Length Queries
----------------------------------------------------------------------

WebGL では、列挙型

* ``INFO_LOG_LENGTH``
* ``SHADER_SOURCE_LENGTH``
* ``ACTIVE_UNIFORM_MAX_LENGTH``
* ``ACTIVE_ATTRIBUTE_MAX_LENGTH``

が削除された。OpenGL ES 2.0 では、``glGetActiveAttrib`` などの呼び出しに渡される
バッファーのサイズを決定するために、これらの列挙型が必要だった。 WebGL では、類
似の呼び出し

* ``getActiveAttrib``,
* ``getActiveUniform``,
* ``getProgramInfoLog``,
* ``getShaderInfoLog``,
* ``getShaderSource``

はすべて ``DOMString`` を返す。

6.25 Texture Type in ``texSubImage2D`` Calls
----------------------------------------------------------------------

WebGL では ``texSubImage2D`` に渡される ``type`` 引数は、テクスチャーオブジェク
トを最初に定義した（つまり ``texImage2D`` を使用した）ときに使用された ``type``
と一致しなければならない。

.. _khronos15-6.26:

6.26 Packing Restrictions for Uniforms and Varyings
----------------------------------------------------------------------

OpenGL ES Shading Language, Version 1.00 [GLES20GLSL]_ の Appendix A, Section 7
"Counting of Varyings and Uniforms" では、シェーダー内のすべての ``uniform`` 変
数と ``varying`` 変数に必要な記憶域を計算するための保守的なアルゴリズムを定義し
ている。

GLSL ES では、Appendix A で定義されたパッキングアルゴリズムが成功すると、その
シェーダーは対象プラットフォームでのコンパイルに成功しなければならないとある。

WebGL ではさらに、シェーダーの ``uniform`` 変数またはプログラムの ``varing`` 変
数のいずれかでパッキングアルゴリズムが失敗した場合、コンパイルまたはリンクが失敗
することを要求する。

レジスターの固定サイズのグリッドを使用する代わりに、対象アーキテクチャーの行数は
次の方法で決定する：

* 頂点シェーダーで ``uniform`` 変数をカウントするときは
  ``getParameter(MAX_VERTEX_UNIFORM_VECTORS)``
* フラグメントシェーダーで ``uniform`` 変数をカウントするときは
  ``getParameter(MAX_FRAGMENT_UNIFORM_VECTORS)``
* ``varying`` 変数をカウントするときは ``getParameter(MAX_VARYING_VECTORS)``

.. admonition:: Non-normative:

   * 上の記述はパッキングアルゴリズムによる制約のために、シェーダーやプログラム
     のコンパイルやリンクが失敗しなければならない状況を定義している。このアルゴ
     リズムによって変数が正常にパッキングされる必要最小限の量よりも多くの変数を
     使用するシェーダーが正常にコンパイルされることは保証していない。
   * スカラー配列を拡張して複数の列を消費するなど、非効率的な実装が見受けられ
     る。
   * 開発者は、複数の変数の列への自動パッキングに大きく依存することは避けるべき
     だ。代わりに、``vec4`` のようなより大きな変数を定義し、明示的に右端の列に値
     を詰めるように。

6.27 Feedback Loops Between Textures and the Framebuffer
----------------------------------------------------------------------

* OpenGL ES 2.0 では、同じテクスチャーへの書き込みと読み込みの両方を行う呼び出し
  が可能であり、フィードバックループが発生する。このようなフィードバックループが
  存在する場合、未定義の動作が生じることが明記されている。
* WebGL では、このようなフィードバックループを引き起こすような操作を行うと、
  ``INVALID_OPERATION`` エラーとなる。

.. _khronos15-6.28:

6.28 Reading From a Missing Attachment
----------------------------------------------------------------------

OpenGL ES 2.0 では、色 attachment のない完全フレームバッファーから色データに関す
る ``readPixels`` を行うというように、attachment のないデータをコマンドが
``source`` にしようとした場合にどうなるかは規定されていない。

WebGL では、欠落 attachment からのデータを必要とするこのような操作は
``INVALID_OPERATION`` エラーとなる。

これは次の関数に適用される：

* ``copyTexImage2D``
* ``copyTexSubImage2D``
* ``readPixels``

6.29 Drawing To a Missing Attachment
----------------------------------------------------------------------

OpenGL ES 2.0 では、色 attachment のない完全フレームバッファーから描画バッファー
を消去するなどのような、コマンドが見つからない attachment に描画しようとしたとき
にどうなるかが規定されていない。

WebGL API では、欠落 attachment に描画するような操作は、その attachment に何も描
画しない。エラーではない。

これは次の関数に適用される：

* ``clear``
* ``drawArrays``
* ``drawElements``

.. _khronos15-6.30:

6.30 NaN Line Width
----------------------------------------------------------------------

``lineWidth`` に渡される ``width`` 引数に ``NaN`` が設定されていると、
``INVALID_VALUE`` エラーとなり、線幅を変更しない。

6.31 Attribute Aliasing
----------------------------------------------------------------------

アプリケーションでは、複数の属性名を同じ場所に束縛することが可能だ。これはエイリ
アスと呼ばれている。同じ場所にエイリアスされた複数の属性が実行プログラムで有効な
場合、``linkProgram`` は失敗するはずだ。

6.32 Initial value for gl_Position
----------------------------------------------------------------------

* GLSL ES [GLES20GLSL]_ では、頂点シェーダーで書き込まれない限り ``gl_Position``
  の値は未定義とされている。
* WebGL では ``gl_Position`` の初期値が ``(0,0,0,0)`` であることを保証している。

6.33 GLSL ES Global Variable Initialization
----------------------------------------------------------------------

* GLSL ES 1.00 [GLES20GLSL]_ では、グローバル変数の初期化子を定数式に限定してい
  る。
* WebGL では、GLSL ES 1.00 のシェーダーのグローバル変数の初期化子に、``const``
  で修飾されていない他のグローバル変数や、``uniform`` 値を使用することが認められ
  ている。

グローバル変数の初期化子はグローバル初期化子式でなければならず、次のいずれかで定
義される：

* 定数式
* ユーザー定義のグローバル変数
* ``uniform``
* グローバル初期化子式であるオペランドに対する演算子によって形成される式。グロー
  バル初期化子ベクトル、グローバル初期化子行列の要素、またはグローバル初期化子構
  造のフィールドの取得を含む。
* すべてのグローバル初期化子式を実引数とするコンストラクター
* 実引数がすべてグローバル初期化子式である組み込み関数呼び出し（ただし、テクス
  チャールックアップ関数を除く）

グローバル初期化子式では、次のものは使用できない：

* ユーザー定義関数
* ``attribute`` と ``varying``
* 定数式を除く組み込み変数
* 代入やその他の操作における左辺値としてのグローバル変数

グローバル変数の初期化子が修正されていない GLSL ES 仕様に違反している場合、すな
わち、グローバル変数の初期化子が定数式でない場合、コンパイラーは警告を生成する必
要がある。

.. admonition:: Rationale

   この動作は数年前 から WebGL の実装に存在していた。この動作を GLSL ES に合わせ
   て修正することは、既存の内容との互換性に大きな影響を与える。

6.34 GLSL ES Preprocessor ``defined`` Operator
----------------------------------------------------------------------

* GLSL ES 前処理器仕様が参照する C++ 標準では、``#if`` または ``#elif`` 指令の
  制御式を解析する際に、マクロ置換によって定義された演算子が生成されると、動作は
  未定義となる。 WebGL で処理されるシェーダーコードが、前処理器式の内部でマクロ
  置換時に定義されたトークンを生成すると、コンパイラエラーとなる。
* これは演算子 ``defined`` を扱う前処理器指示子の外側でのマクロ展開には影響しな
  い。
* ``defined`` をマクロ名として使用した場合にも C++ 標準では、動作は未定義だ。
  WebGL では、``defined`` をマクロ名として使用すると、コンパイラーエラーが必ず発
  生する。

.. admonition:: Rationale

   ネイティブ API 仕様で未定義の動作が許容されている場合、WebGL の動作には一貫性
   がなければならない。

6.35 GLSL ES ``#extension`` directive location
----------------------------------------------------------------------

* GLSL ES 1.00 [GLES20GLSL]_ では、拡張仕様に別段の定めがない限り、
  ``#extension`` 指令は、前処理器トークンでないものの前に置かなければならないと
  定められている。
* WebGL では、GLSL ES 1.00 のシェーダーでは ``#extension`` は常に非前処理器トー
  クンの後に置かれてもかまわない。
* GLSL ES 1.00 シェーダーにおける ``#extension`` 指令のスコープは常にシェーダー
  全体であり、後に置かれる ``#extension`` はシェーダー全体で先に置かれたものを上
  書きする。

.. admonition:: Rationale

   ``#extension`` 指令をどこに配置するかを拡張に決定させるということが結果的に仕
   様に多くの解釈の余地を与えた。実際に、GLES の実装では GLSL ES 仕様に書かれて
   いる規則を守っていないし、WebGL の実装でも同様だ。

   規則を緩和することが、既存の内容の互換性を保ちつつ、仕様を明確にする唯一の方
   法なのだ。

6.36 Completeness of Cube Map Framebuffer Attachments
----------------------------------------------------------------------

WebGL では、立方体が完全でないキューブマップの面は、フレームバッファーの取り付け
が完全でない。不完全なキューブマップの面が取り付けられているときにフレームバッ
ファーの状態を問い合わせると、``FRAMEBUFFER_INCOMPLETE_ATTACHMENT`` が返されなけ
ればならない。

.. admonition:: Rationale

   最近の OpenGL コアバージョンや OpenGL ES 3.0 とそれ以降など、WebGL が実装され
   ている API では、フレームバッファーの付着物として使用されるキューブマップの面
   は完全なキューブマップの一部であることという要件がある。例えば、OpenGL ES
   3.0.4 §4.4.4 "Framebuffer Completeness" の節 "Framebuffer Attachment
   Completeness" を見ろ。

6.37 Transferring vertices when current program is null
----------------------------------------------------------------------

頂点を GL に転送するコマンドは、``CURRENT_PROGRAM`` が ``null`` の場合
``INVALID_OPERATION`` エラーとなる。このようなコマンドには ``drawElements`` と
``drawArrays`` がある。

6.38 Fragment shader output
----------------------------------------------------------------------

フラグメントシェーダーが ``gl_FragColor`` と ``gl_FragData`` のどちらにも書き込
まない場合、シェーダー実行後のフラグメント色の値は変更されない。

6.39 Initial values for GLSL local and global variables
----------------------------------------------------------------------

* GLSL ES [GLES20GLSL]_ では、ローカル変数やグローバル変数の値は、シェーダーで初
  期化されない限り未定義のままだ。
* WebGL では、このような変数が ``0.0``, ``vec4(0.0)``, ``0``, ``false`` などに初
  期化されることを保証する。

6.40 Vertex attribute conversions from normalized signed integers to floating point
-----------------------------------------------------------------------

OpenGL ES 2.0 の 節 2.1.2 "Data Conversions" の部分節 "Conversion from Integer
to Floating-Point" では、ビット幅が ``b`` である正規化された符号付き整数 ``c``
から浮動小数点値 ``f`` への変換を次のように定義している：

.. code:: c

   f = (2*c + 1) / (2^b - 1)

正規化された符号付き頂点 ``attribute`` を浮動小数点に変換する際、WebGL 1.0 の実
装ではオプションでこの変換則を使用することができ、ゼロが保持される：

.. code:: c

   f = max(c / (2^(b - 1) - 1), -1.0)

.. admonition:: Rationale

   WebGL 1.0 がベースにしている API の中には、二番目の規則を使用しているものがあ
   る。この変換は固定機能のハードウェアで行われるため、どちらかの動作に倣うこと
   はできない。この動作の違いは、ほとんどのアプリケーションには影響しないので、
   どちらの動作が使われているかを判断する問い合わせは、WebGL のレンダリングコン
   テキストには追加されていない。

6.41 Uniform and attribute name collisions
----------------------------------------------------------------------

WebGL プログラムに取り付けらているシェーダーのいずれかが、静的に使用される頂点
``attribute`` と同じ名前の ``uniform`` を宣言している場合、プログラムのリンクは
失敗する。

.. admonition:: Non-normative

   この動作は、GLSL ES 3.00.6 の 12.47 節で指定されているものとは異なる。

.. admonition:: Rationale

   OpenGL ドライバーの一部が ``uniform`` と頂点 ``attribute`` が同じ名前であるこ
   とを受け付けないことにより、 WebGL の実装では数年前からこの動作を採用してい
   る。

6.42 Wide point primitive clipping
----------------------------------------------------------------------

``POINTS`` プリミティブは、頂点がクリップボリュームの外にあっても、近距離および
遠距離のクリップ平面内にある場合は、破棄されることもされないこともある。

.. admonition:: Rationale

   GLES と GLでは、外れ点のクリッピングの動作が異なる。この動作の違いは、実装
   上、回避することができない。

   OpenGL ES 2.0.25 p46 [GLES20]_:
       考慮中のプリミティブが点ならば、クリッピングは、それが近または遠のクリッ
       プ面の外側にある場合、それを破棄する。そうでない場合には変更されずに合格
       とする。

   OpenGL 3.2 Core p97 [GL32CORE]_:
       考慮中のプリミティブが点ならば、クリッピングは、それがクリップボリューム
       内にある場合は変更されずに合格とし、そうでない場合は破棄する。
