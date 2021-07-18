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

* WebGL API はクライアントサイドの配列をサポートしていない。
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

WebGL API はデフォルトのテクスチャーをサポートしない。

テクスチャー関連の操作や問い合わせを成功させるためには、
``null`` ではない ``WebGLTexture`` オブジェクトが束縛されている必要がある。

6.4 No Shader Binaries
----------------------------------------------------------------------

* コンパイルされたシェーダーのバイナリー表現へのアクセスを WebGL API はサポートしない。
  これには OpenGL ES 2.0 ShaderBinary エントリーポイントを含む。
* また、WebGL API では ``getParameter`` を通じてシェーダーのバイナリー形式や
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

WebGL API では、次の付着点の組み合わせと同時にレンダーバッファーを取り付けるとエラーになる：

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
