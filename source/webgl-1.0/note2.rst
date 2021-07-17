======================================================================
WebGL Specification 1.0 読書ノート 2
======================================================================

`WebGL Specification <https://www.khronos.org/registry/webgl/specs/latest/1.0/>`__
を読んでいく。

.. contents:: ノート目次

5 DOM Interfaces
======================================================================

本節では、上述の機能へのランタイムアクセスをサポートするために DOM に追加された
インターフェイスと機能について述べられている。

5.1 Types
----------------------------------------------------------------------

本文中の表に列挙された型が以降の節すべてのインターフェイスで用いられるとある。
JavaScript ではなく C 言語のコードで書かれているのが気になる。

5.2 ``WebGLContextAttributes``
----------------------------------------------------------------------

``WebGLContextAttributes`` 辞書には描画面の属性が含まれており、
``getContext`` の二番目の引数として渡される。

* 後述の例と併せて眺めると良い。

5.2.1 Context creation parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ここにある一覧に ``WebGLContextAttributes`` オブジェクトの各属性とその用途について説明がある。

* 各属性のデフォルト値は 5.2 の表のとおり。
* 既定値は ``getContext`` に二番目の引数が渡されなかった場合、
  または指定された名前の属性を持たないユーザーオブジェクトが渡された場合に採用される。

``alpha``
    この値が ``true`` である場合、描画バッファーにアルファーチャンネルがある。

``depth``
    この値が ``true`` の場合、描画バッファーは少なくとも 16 ビットの深度バッファーを持つ。

``stencil``
    この値が ``true`` の場合、描画バッファーは少なくとも 8 ビットのステンシルバッファーを持つ。

``antialias``
    この値が ``true`` で、かつ実装が antialiasing をサポートしている場合、
    描画バッファーは選択した手法と品質を使用してそれを実行する。

``premultipliedAlpha``
    この値が ``true`` の場合、ページ合成器は描画バッファーにあらかじめアルファ値が乗算された色が含まれているとみなす。

    * ``alpha = false`` の場合、このフラグは無視される。
    * ``premultipliedAlpha`` フラグの効果の詳細については Premultiplied Alpha を参照。

``preserveDrawingBuffer``

    この値が ``false`` の場合、Drawing Buffer の項にあるように描画バッファーが提示されると、
    描画バッファーの内容は既定値に消去される。
    描画バッファーのすべての要素（カラー、深度、ステンシル）が消去される。

    この値が ``true`` の場合、バッファーは消去されず、オーナーが消去するか上書きするまで、その値が保持される。
    ``preserveDrawingBuffer`` フラグを ``true`` に設定すると、一部のハードウェアではパフォーマンスに大きな影響を与えることがある。

``powerPreference``
    この WebGL コンテキストに適した GPU の構成を示すヒントをブラウザーに提供する。
    この値は、複数の GPU を備えたシステムでどの GPU を使用するかに影響を与える可能性がある。
    たとえば、デュアル GPU システムでは、レンダリング性能を犠牲にして消費電力の少ない GPU を使用する場合があり得る。
    このプロパティーはヒントに過ぎず、WebGL の実装がこれを無視しても構わない。

    WebGL の実装では、この属性の値にかかわらず、コンテキストの喪失および復元イベントを使用して、電力とメモリーの消費を調整する。

    この属性が取り得る値は次のどれかだ：

    ``"default"``
        どの GPU 構成が最も適しているかをブラウザーに判断させる。これが既定値だ。

    ``"high-performance"``
        消費電力よりもレンダリング性能を優先した GPU 構成を要求する。
        この値を指定すると、モバイル機器のバッテリー駆動時間が大幅に短くなる可能性がある。
        実装では、最初はこの要求を尊重し、しばらくするとコンテキストを失い、
        要求を無視して新しいコンテキストを復元することにしてもかまわない。

        ----

        バックグラウンドの高性能コンテキストを失うことをブラウザーが決定するということがひじょうにありがちなので、
        このオプションを要求するアプリケーションは、堅牢なコンテキスト消失処理を試験し、維持する必要がある。

        ----

    ``"low-power"``
        レンダリング性能よりも省電力を優先した GPU 設定を要求する。
        一般的に、内容が描画パフォーマンスに制約される可能性が低い場合にこの値を使用するべきだ。
        たとえば、

        * 一秒間にワンフレームしかレンダリングしない場合、
        * 単純なシェーダーで比較的単純なジオメトリーのみを描画する場合、
        * 小さな HTML ``canvas`` 要素を使用する場合

        などだ。

        モバイル機器のバッテリー駆動時間が著しく改善される可能性があるので、このオプションを推奨。

``failIfMajorPerformanceCaveat``
    この値が ``true`` の場合、作成された WebGL コンテキストのパフォーマンスが、
    同等の OpenGL 呼び出しを行うネイティブアプリケーションのパフォーマンスよりも大幅に低下すると実装が判断した場合、
    コンテキストの作成を失敗させる。

    * このオプションは使わないと思うので、これ以上調べない。

``desynchronized``
    この値が ``true`` の場合、ブラウザーはキャンバスの描画を最適化して、
    入力イベントからラスタライズまでの待ち時間を短縮することができる。
    そのためには、キャンバスの描画周期をイベントループから非同期化するか、
    通常のブラウザーの描画アルゴリズムを迂回するか、またはその両方を行う必要がある。
    このモードでは、通常の描画の仕組み、ラスタライズ、またはその両方が迂回されるため、
    目に見える tearing artifacts が発生する可能性がある。

    ----

    ブラウザーは、通常、表示されていないバッファでレンダリングを行い、表示のためにスキャンされているバッファーと素早く交換する。
    この技術は tearing artifacts を引き起こす可能性があるという代償を払って遅延を削減する。

    この真偽値の属性は、入力とラスタライズの間の遅延時間が重要な描画アプリケーションなど、
    特定の種類のアプリケーションを実装する際に役立つ。

----

``WebGLContextAttributes`` 引数を ``getContext`` に渡すコード例（仕様書のコードを改変）。
この例では、ページ上に ``canvas1`` という名前の ``canvas`` 要素が存在することを仮定している。

.. code:: javascript

   const canvas = document.getElementById('canvas1');
   const gl = canvas.getContext('webgl',
                                { antialias: false,
                                  stencil: true });

5.3 ``WebGLObject``
----------------------------------------------------------------------

``WebGLObject`` インターフェイスはすべての GL オブジェクトの親となるインターフェイスだ。
各 ``WebGLObject`` は ``invalidated`` フラグを持っており、これは最初はセットされていない。

5.4 ``WebGLBuffer``
----------------------------------------------------------------------

``WebGLBuffer`` インターフェイスは OpenGL バッファーオブジェクトを表現する。
基礎となるオブジェクトは

* ``glGenBuffers`` を呼び出して作成され、
* ``glBindBuffer`` を呼び出して束縛され、
* ``glDeleteBuffers`` を呼び出して削除される。

5.5 ``WebGLFramebuffer``
----------------------------------------------------------------------

``WebGLFramebuffer`` インターフェイスは OpenGL Framebuffer オブジェクトを表現する。
基礎となるオブジェクトは、

* ``glGenFramebuffer`` を呼び出すことで作成され、
* ``glBindFramebuffer`` を呼び出すことで束縛され、
* ``glDeleteFramebuffer`` を呼び出すことで削除される。

5.6 ``WebGLProgram``
----------------------------------------------------------------------

``WebGLProgram`` インターフェイスは OpenGL Program Object を表現する。
基礎となるオブジェクトは、

* ``glCreateProgram`` を呼び出すことで作成され、
* ``glUseProgram`` を呼び出すことで使用され、
* ``glDeleteProgram`` を呼び出すことで削除される。

5.7 ``WebGLRenderbuffer``
----------------------------------------------------------------------

``WebGLRenderbuffer`` インターフェイスは OpenGL Renderbuffer オブジェクトを表現する。
基礎となるオブジェクトは、

* ``glGenRenderbuffers`` を呼び出すことで作成され、
* ``glBindRenderbuffer`` を呼び出すことで束縛され、
* ``glDeleteRenderbuffers`` を呼び出すことで削除マークが付く。

5.8 ``WebGLShader``
----------------------------------------------------------------------

``WebGLShader`` インターフェイスは OpenGL Shader オブジェクトを表現する。
このオブジェクトは、

* ``glCreateShader`` で作成され、
* ``glAttachShader`` でプログラムに取り付けられ、
* ``glDeleteShader`` で削除される。

5.9 ``WebGLTexture``
----------------------------------------------------------------------

``WebGLTexture`` インターフェイスは OpenGL Texture Objectを表現する。
基礎となるオブジェクトは、

* ``glGenTextures`` を呼び出すことで作成され、
* ``glBindTexture`` を呼び出すことで束縛され、
* ``glDeleteTextures`` を呼び出すことで削除される。

5.10 ``WebGLUniformLocation``
----------------------------------------------------------------------

``WebGLUniformLocation`` インターフェイスはシェーダープログラムにおける ``uniform`` 変数の位置を表現する。

5.11 ``WebGLActiveInfo``
----------------------------------------------------------------------

``WebGLActiveInfo`` インターフェイスは
``getActiveAttrib`` および ``getActiveUniform`` の呼び出しが返す情報を表現する。

5.11.1 Attributes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``size``
    要求された変数のサイズ

``type``
    要求された変数のデータ型

``name``
    要求された変数の名前

5.12 ``WebGLShaderPrecisionFormat``
----------------------------------------------------------------------

``WebGLShaderPrecisionFormat`` インターフェイスは
``getShaderPrecisionFormat`` 呼び出しが返す情報を表現する。

5.12.1 Attributes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``rangeMin``
    表現可能な最小値の絶対値の、底を 2 とする対数の値。

``rangeMax``
    表現可能な最大値の絶対値の、底を 2 とする対数の値。

``precision``
    表現可能な精度のビット数。整数フォーマットではこの値は常に 0 とする。

5.13 ``ArrayBuffer`` and Typed Arrays
----------------------------------------------------------------------

* 頂点、インデックス、テクスチャ、その他のデータは、ECMAScript 仕様で定義されている
  ``ArrayBuffer``, *Typed Array*,``DataView`` を使用して WebGL 実装に転送される。
* *Typed Array* は、インターリーブされた異種の頂点データを作成したり、
  大規模な頂点バッファーオブジェクトへデータの個別ブロックをアップロードしたり、
  その他 OpenGL プログラムが必要としたりする使用例のほとんどをサポートする。

----

異なる型の配列を使用して同じ ``ArrayBuffer`` にアクセスするコードの例がある。
それを一部改変してここに記す。
バッファーには浮動小数点の頂点位置 ``(x, y, z)`` と、それに続く 4 つの
unsigned byte の色 ``(r, g, b, a)`` を含む：

.. code:: javascript

   const numVertices = 100; // for example

   // Compute the size needed for the buffer, in bytes and floats
   const vertexSize = 3 * Float32Array.BYTES_PER_ELEMENT +
         4 * Uint8Array.BYTES_PER_ELEMENT;
   const vertexSizeInFloats = vertexSize / Float32Array.BYTES_PER_ELEMENT;

   // Allocate the buffer
   const buf = new ArrayBuffer(numVertices * vertexSize);

   // Map this buffer to a Float32Array to access the positions
   const positionArray = new Float32Array(buf);

   // Map the same buffer to a Uint8Array to access the color
   const colorArray = new Uint8Array(buf);

   // Set up the initial offset of the vertices and colors within the buffer
   let positionIdx = 0;
   let colorIdx = 3 * Float32Array.BYTES_PER_ELEMENT;

   // Initialize the buffer
   for (let i = 0; i < numVertices; i++) {
       positionArray[positionIdx] = ...;
       positionArray[positionIdx + 1] = ...;
       positionArray[positionIdx + 2] = ...;
       colorArray[colorIdx] = ...;
       colorArray[colorIdx + 1] = ...;
       colorArray[colorIdx + 2] = ...;
       colorArray[colorIdx + 3] = ...;
       positionIdx += vertexSizeInFloats;
       colorIdx += vertexSize;
   }

* C/C++ でいう ``sizeof X`` に相当する値の参照方法に注目。
  各 *TypedArray* の ``BYTES_PER_ELEMENT`` を用いる。
* また、上記コードと同様の処理を ``DataView`` を用いても実現できる。

5.14 The WebGL context
----------------------------------------------------------------------

``WebGLRenderingContext`` は、OpenGL ES 2.0 様式のレンダリングを ``canvas`` 要素に許可する API を表現する。

``WebGLRenderingContext`` インターフェイスのメソッド、または
``getExtension`` メソッドが返すインターフェースのどのメソッドの実装をも行う前に、
以下の手順を実行する必要がある：

#. 呼び出されたメソッドに ``WebGLHandlesContextLoss`` 拡張属性が現れる場合は、
   呼び出されたメソッドの実装を行い、その結果を返して、ここの手順を終了する。
#. ``use`` の既定の戻り値を ``false`` にする。
#. webgl context lost フラグが設定されている場合は、
   ``use`` の既定の戻り値を ``true`` にする。

   #. そうでない場合、メソッドの引数に ``invalidate`` フラグが設定された ``WebGLObject`` があれば、
      ``INVALID_OPERATION`` エラーを生成し、 ``use`` の既定の戻り値を ``true`` にする。

#. ``use`` の既定の戻り値を ``true`` の場合、以下の手順を実行する：

   #. 呼び出されたメソッドの戻り値の型が ``any`` または ``nullable`` 型の場合は ``null`` を返す。
   #. メソッドの実装を呼び出すことなしにこのアルゴリズムを終了する。

#. そうでない場合は、呼び出されたメソッドの実装を実行し、その結果を返す。

詳細については、後述の The Context Lost Event を参照しろとある。

----

インターフェイスの仕様を読み解いていく：

* 仕様中に ``TexImageSource`` とある箇所は、次の実際の型のどれでもよい：

  * ``ImageBitmap``
  * ``ImageData``
  * ``HTMLImageElement``
  * ``HTMLCanvasElement``
  * ``HTMLVideoElement``
  * ``OffscreenCanvas``

* 仕様中に ``Float32List`` とある箇所は ``Float32Array`` または浮動小数点型数値の列のどれでもよい。
* 仕様中に ``Int32List`` とある箇所は ``Int32Array`` または整数型数値の列のどれでもよい。
* ``WebGLRenderingContext`` インターフェイスは次の二つに分割されて定義されている：

  * ``WebGLRenderingContextBase``: OpenGL で馴染みの定数、関数の WebGL における対応物と
    WebGL 固有の定数、属性、関数からなる。
  * ``WebGLRenderingContextOverloads``: 引数リストのオーバーロードが複数必要な関数群からなると見られる。

5.14.1 Attributes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``canvas``
    このコンテキストを作成したキャンバスへの参照。

``drawingBufferWidth``
    描画バッファの実際の幅。

``drawingBufferHeight``
    描画バッファの実際の高さ。

最後の二つは要求された幅や高さを満たすことができない実装の場合、
キャンバスの属性 ``width``, ``height`` とはそれぞれ異なることがある。

5.14.2 Getting information about the context
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``getContextAttributes()``
    フラグ webgl context lost が設定されている場合は ``null`` を返す。
    そうでなければ、実際のコンテキストパラメーターのコピーを返す。

5.14.3 Setting and getting state
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

OpenGL ES 2.0 ではレンダリングに使用するための状態を保持する。
ここに記されているグループの呼び出しすべては、特に断りのない限り OpenGL の対応物に対する呼び出しと同じ動作をする。

* ``blendFunc``, ``blendFuncSeparate`` の WebGL から来る制限については次章の記述を参照。
* ``clearDepth`` に対する値 ``depth`` は :math:`{[0, 1]}` に収まるように丸められる。
* ``depthRange`` に対する引数 ``zNear`` と ``zFar`` の値も同様に丸められる。
  かつ ``zNear <= zFar`` でなければならない。
* ``getParameter`` は ``glGet``, ``glGetString`` の対応物だ。

  * 戻り値の型は JavaScript において自然なものとする。
  * 列や *TypedArray* を返す問い合わせのすべてが、毎回新しいオブジェクトを返す。
  * 不適切な問い合わせに対しては ``INVALID_ENUM`` エラーを生成し ``null`` を返す。
  * ``IMPLEMENTATION_COLOR_READ_FORMAT`` または ``IMPLEMENTATION_COLOR_READ_TYPE`` で、
    現在束縛されているフレームバッファーが完全でない場合、
    ``INVALID_OPERATION`` エラーを生成し ``null`` を返す。
  * 次の実引数は、現在の WebGL 実装の何らかの性質を記述する文字列を返す：

    ``VERSION``
        "WebGL 1.0 xxxx" のようなバージョンまたはリリース番号を返す。

    ``SHADING_LANGUAGE_VERSION``
        "WebGL GLSL ES 1.0 xxxx" のようなバージョンまたはリリース番号を返す。

    ``VENDOR``
        この WebGL の実装を担当している会社を返す。

    ``RENDERER``
        レンダラーの名前を返す。この名前はふつうはハードウェアプラットフォームの特定の構成に固有のものだ。

    次章に関連情報アリ。

* ``getError`` はコンテキストの webgl context lost フラグが設定されている場合、
  このメソッドが最初に呼び出されたときに ``CONTEXT_LOST_WEBGL`` を返す。
  その後、コンテキストが回復されるまで ``NO_ERROR`` を返す。
* どの ``isEnabled`` による問い合わせに対しても、同じ戻り値を ``getParameter`` で得ることができる。

  * コンテキストの webgl context lost フラグが設定されている場合は ``false`` を返す。

* ``lineWidth`` には WebGL での制限があり、次章で述べられている。
* ``pixelStorei`` OpenGL ES 2.0 仕様のパラメーターに加えて、次のものも受け付ける。
  これらについては後述。

  * ``UNPACK_FLIP_Y_WEBGL``
  * ``UNPACK_PREMULTIPLY_ALPHA_WEBGL``
  * ``UNPACK_COLORSPACE_CONVERSION_WEBGL``

* ``stencilFuncSeparate``, ``stencilMask`` には WebGL 固有の制限がある。次章で述べられる。

5.14.4 Viewing and clipping
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

描画コマンドは、現在束縛されているフレームバッファー内のピクセルしか変更できない。
また、ビューポートとシザーボックスも描画に影響する。

* ビューポートは正規化されたデバイス座標からウィンドウ座標への x と y のアフィン変換を指定する。

  * ビューポートのサイズは前述したように初期設定される。

* シザーボックスは、描画を制限する矩形を定義する。

  * シザーテストが有効な場合、``clear`` などの描画コマンドで変更できるのはシザーボックス内にあるピクセルだけだ。
    プリミティブの描画は、ビューポート、現在束縛されているフレームバッファー、
    そしてシザーボックスの交点内でしか可能でない。
  * シザーテストが有効でない場合、プリミティブはビューポートと現在束縛されているフレームバッファーの
    共通部分の内側にしか描画されない。

5.14.5 Buffer objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

バッファーオブジェクトは、GLSL シェーダーの頂点属性データを保持する。
重要な概念なので丁寧に理解したい。

----

バッファーオブジェクトのことを VBO と略記することが普通にある。

----

``bindBuffer(target, buffer)``
    与えられた ``WebGLBuffer`` オブジェクトを ``ARRAY_BUFFER`` または ``ELEMENT_ARRAY_BUFFER`` のいずれかの与えられた対象に束縛する。

    * バッファーがこのものとは異なる ``WebGLRenderingContext`` によって生成された場合 ``INVALID_OPERATION`` エラーを生成する。
    * バッファーが ``null`` の場合、現在この対象に束縛されているすべてのバッファーの束縛を解除する。
    * 与えられた ``WebGLBuffer`` オブジェクトはその寿命において
      ``ARRAY_BUFFER`` または ``ELEMENT_ARRAY_BUFFER`` のいずれかの対象にしか束縛されない。
    * バッファーオブジェクトを他の対象にバインドしようとすると
      ``INVALID_OPERATION`` エラーが発生し、現在の束縛はそのまま維持される。
    * 削除マークのついたオブジェクトを束縛しようとすると
      ``INVALID_OPERATION`` エラーが発生し、現在の束縛はそのまま維持される。

``bufferData(target, size, usage)``, ``bufferData(target, data, usage)``
    最初のものは、現在束縛されている ``WebGLBuffer`` オブジェクトのサイズを、渡された対象に設定する。
    バッファーの中身は 0 に初期化される。

    二番目のものは、渡された対象に対して、現在束縛されている ``WebGLBuffer`` オブジェクトのサイズを
    渡されたデータのサイズに設定し、データの内容をバッファーオブジェクトに書き込む。

    * 渡されたデータが ``null`` の場合は ``INVALID_VALUE`` エラーが発生する。

``bufferSubData(target, offset, data)``
    ``target`` に束縛された ``WebGLBuffer`` オブジェクトに対して、
    位置 ``offset`` から始まる ``data`` を書き込む。

    * バッファーオブジェクトの終端を越えてデータが書き込まれる場合は ``INVALID_VALUE`` エラー。
    * ``data`` が ``null`` の場合も ``INVALID_VALUE`` エラー。

``createBuffer()``
    Create a WebGLBuffer object and initialize it with a buffer object name as if by calling glGenBuffers.
    ``WebGLBuffer`` オブジェクトを生成し、``glGenBuffers`` を呼び出したかのようにバッファーオブジェクト名で初期化する。

``deleteBuffer(buffer)``
    ``glDeleteBuffers`` の呼び出しのごとく、渡された ``WebGLBuffer`` が含むバッファーオブジェクトに削除マークを付ける。

    * すでに削除マークが付けられている場合、この呼び出しは効果が特にない。
    * 内包されている GL オブジェクトは JavaScript オブジェクトが破壊されるときに自動的に削除マークが付けられるが、
      このメソッドを使用することでオブジェクトに対して削除マークを早期に付けることができる。
    * ``buffer`` がこれとは異なる ``WebGLRenderingContext`` によって生成されたものである場合 ``INVALID_OPERATION`` エラー。

``getBufferParameter(target, pname)`` (OpenGL ES 2.0 §6.1.3, similar to glGetBufferParameteriv)
    OpenGL の ``glGetBufferParameteriv`` の対応物。``pname`` の値を返す。

    * 戻り値の型は要求された ``pname`` にとって自然な型とする。例えば ``BUFFER_SIZE`` なら整数を返す。
    * ``pname`` がサポートされていない名前のときには ``INVALID_ENUM`` エラー。
    * OpenGL エラーが発生した場合は ``null`` を返す。

``isBuffer(buffer)``
    渡された ``WebGLBuffer`` が有効かどうかを返す。

    * ``buffer`` がこれとは異なる ``WebGLRenderingContext`` によって生成された場合は ``false`` を返す。
    * ``buffer`` の ``invalidated`` フラグが設定されている場合は ``false`` を返す。

5.14.6 Framebuffer objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

フレームバッファーオブジェクトとは、描画バッファーに代わるレンダリング先を提供するものだ。
色、アルファー、深度、ステンシルバッファーの集合体であり、
のちにテクスチャーとして使用される画像のレンダリングとしてよく用いられる。

``bindFramebuffer(target, framebuffer)``
    与えられた ``WebGLFramebuffer`` オブジェクトを、
    ``FRAMEBUFFER`` でなければならない与えられた束縛ポイント ``target`` に束縛する。

    * ``framebuffer`` がこのものとは異なる ``WebGLRenderingContext`` によって生成されたものである場合には ``INVALID_OPERATION エラー``
    * ``framebuffer`` が ``null`` ならば、コンテキストが与える既定のフレームバッファーを束縛し、
      ``target`` の ``FRAMEBUFFER`` の状態を変更または問い合わせるようとする試みは ``INVALID_OPERATION`` エラーとなる。
    * 削除マークのついたオブジェクトを束縛しようとすると ``INVALID_OPERATION`` エラー。現在の束縛はそのまま残る。

``checkFramebufferStatus(target)``
    コンテキストの webgl context lost フラグが設定されている場合は ``FRAMEBUFFER_UNSUPPORTED`` を返す。

``createFramebuffer()``
    ``WebGLFramebuffer`` オブジェクトを作成し、
    ``glGenFramebuffer`` を呼び出したかのようにフレームバッファオブジェクトに名前を与えて初期化する。

``deleteFramebuffer(buffer)``
    ``glDeleteFramebuffers`` の対応物。

    * すでに削除マークが付けられている場合、この呼び出しは効果が特にない。
    * 内包されている GL オブジェクトは JavaScript オブジェクトが破壊されるときに自動的に削除マークが付けられるが、
      このメソッドを使用することでオブジェクトに対して削除マークを早期に付けることができる。
    * ``buffer`` がこのものとは異なる ``WebGLRenderingContext`` によって生成されたものである場合 ``INVALID_OPERATION`` エラー。

``framebufferRenderbuffer(target, attachment, renderbuffertarget, renderbuffer)``
    ``glFramebufferRenderbuffer`` の対応物。

    * ``renderbuffer`` がこのものとは異なる ``WebGLRenderingContext`` によって生成されたものである場合 ``INVALID_OPERATION`` エラー。

``framebufferTexture2D(target, attachment, textarget, texture, level)``
    ``glFramebufferTexture2D`` の対応物。

    * ``texture`` がこのものとは異なる ``WebGLRenderingContext`` によって生成されたものである場合 ``INVALID_OPERATION`` エラー。

``getFramebufferAttachmentParameter(target, attachment, pname)``
    ``glGetFramebufferAttachmentParameteriv`` の対応物。

    戻り値の型は要求された ``pname`` に自然な型とする。
    例えば ``FRAMEBUFFER_ATTACHMENT_OBJECT_NAME`` を求めると

    * 無効な ``pname`` に対しては ``INVALID_ENUM`` エラー。
    * OpenGL エラーが起こった場合には ``null`` を返す。

``isFramebuffer(framebuffer)``
    渡された ``framebuffer`` が有効な ``WebGLFramebuffer`` であるかどうかを返す。

    * ``framebuffer`` がこれとは異なる ``WebGLRenderingContext`` が生成したものである場合は ``false`` を返す。
    * ``framebuffer`` の ``invalidated`` フラグが設定されている場合は ``false`` を返す。

5.14.7 Renderbuffer objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

描画バッファーオブジェクトは、フレームバッファーオブジェクトで使用される個々のバッファーのストレージとされるものだ。

``bindRenderbuffer(target, renderbuffer)``
    与えられた ``WebGLRenderbuffer`` オブジェクトを、
    ``RENDERBUFFER`` でなければならない与えられた束縛ポイント ``target`` に束縛する。

    * ``renderbuffer`` がこのものとは異なる ``WebGLRenderingContext`` によって生成されたものである場合には ``INVALID_OPERATION エラー``
    * ``renderbuffer`` が ``null`` ならば、この ``taget`` に現在束縛されている描画バッファーオブジェクトの束縛は解かれる。
    * 削除マークのついたオブジェクトを束縛しようとすると
      ``INVALID_OPERATION`` エラーが発生する。現在の束縛はそのままになる。

``createRenderbuffer()``
    ``WebGLRenderbuffer`` オブジェクトを生成し、
    ``glGenRenderbuffers`` を呼び出したかのように描画バッファーオブジェクトに名前をつけて初期化する。

``deleteRenderbuffer(renderbuffer)``
    ``glDeleteRenderbuffers`` の対応物。

    * ``renderbuffer`` がこのものとは異なる ``WebGLRenderingContext`` によって生成されたものである場合 ``INVALID_OPERATION`` エラー。
    * 内包されている GL オブジェクトは JavaScript オブジェクトが破壊されるときに自動的に削除マークが付けられるが、
      このメソッドを使用することでオブジェクトに対して削除マークを早期に付けることができる。

``getRenderbufferParameter(target, pname)``
    ``glGetRenderbufferParameteriv`` の対応物。

    戻り値の型は要求された ``pname`` に自然な型とする。だいたい整数。

    * 無効な ``pname`` に対しては ``INVALID_ENUM`` エラー。
    * OpenGL エラーが起こった場合には ``null`` を返す。

``isRenderbuffer(renderbuffer)``
    渡された ``renderbuffer`` が有効な ``WebGLRenderbuffer`` であるかどうかを返す。

    * ``renderbuffer`` がこれとは異なる ``WebGLRenderingContext`` が生成したものである場合は ``false`` を返す。
    * ``renderbuffer`` の ``invalidated`` フラグが設定されている場合は ``false`` を返す。

``renderbufferStorage(target, internalformat, width, height)``
    ``glRenderBufferStorage`` の対応物。

5.14.8 Texture objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

テクスチャーオブジェクトは、テクスチャーを操作するためのストレージと状態を与える。
``WebGLTexture`` が束縛されていない場合、テクスチャーオブジェクトへの変更または問い合わせは
``INVALID_OPERATION`` エラーが発生する。

``bindTexture(target, texture)``
    ``glBindTexure`` の対応物。

    * エラー発生は ``bindFramebuffer`` や ``bindRenderbuffer`` に準じる。

``compressedTexImage2D(target, level, internalformat, width, height, border, pixels)``
``compressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, pixels)``
    ``glCompressedTexImage2D``, ``glCompressedTexSubImage2D`` の対応物。

    * コア WebGL 仕様では、サポートされる圧縮テクスチャーフォーマットを何も定義していない。
    * デフォルトでは、これらのメソッドは ``INVALID_ENUM`` エラーを生成し、直ちに戻る。
      詳しくは次章で述べられる。

``copyTexImage2D``(target, level, internalformat, x, y, width, height, border)``
    ``glCopyTexImage2D`` の対応物。

    この関数は、``texImage2D`` が ``null`` データで呼び出され、続いて ``copyTexSubImage2D`` が呼び出されたかのように振る舞う。

    * ``copyTexSubImage2D`` と同様に、フレームバッファーの外側にある
      source ピクセルについては、対応する destination テクセルはそのまま残されるので、
      まるで ``texImage2D`` が ``null`` データで呼び出されたかのようにゼロ初期化された内容を保持する。
      これにより、フレームバッファーの外側にある source ピクセルに対応する
      destination ピクセルは、関連するテクセルのチャンネルすべてが
      0 に初期化されるという効果もある。
    * この関数が attachment のない完全なフレームバッファーから読み取ろうとした場合、
      ``INVALID_OPERATION`` エラーが発生する。

``copyTexSubImage2D(target, level, xoffset, yoffset, x, y, width, height)``
    ``glCopyTexSubImage2D`` の対応物。

    * フレームバッファーの外側にあるどんなピクセルも、対応する destination ピクセルはそのまま変わらない。
    * この関数が attachment のない完全なフレームバッファーから読み取ろうとした場合、
      ``INVALID_OPERATION`` エラーが発生する。

``createTexture()``
    ``WebGLTexture`` オブジェクトを生成し、``glGenTextures`` を呼び出したかのようにテクスチャオブジェクトに名前をつけて初期化する。

``deleteTexture(texture)``
    ``glDeleteTextures`` の対応物。

    * ``texture`` がこのものとは異なる ``WebGLRenderingContext`` によって生成されたものである場合 ``INVALID_OPERATION`` エラー。
    * 内包されている GL オブジェクトは JavaScript オブジェクトが破壊されるときに自動的に削除マークが付けられるが、
      このメソッドを使用することでオブジェクトに対して削除マークを早期に付けることができる。

``generateMipmap(target)``
    ``glGenerateMipmap`` の対応物。

``getTexParameter(target, pname)``
    ``glGetTexParameter*`` の対応物。

    戻り値の型は要求された ``pname`` に自然な型とする。

    * 無効な ``pname`` に対しては ``INVALID_ENUM`` エラー。
    * OpenGL エラーが起こった場合には ``null`` を返す。

``isTexture(texture)``
    渡された ``texture`` が有効な ``WebGLTexture`` であるかどうかを返す。

    * ``renderbuffer`` がこれとは異なる ``WebGLRenderingContext`` が生成したものである場合は ``false`` を返す。
    * ``renderbuffer`` の ``invalidated`` フラグが設定されている場合は ``false`` を返す。

``texImage2D(target, level, internalformat, width, height, border, format, type, pixels)``
    ``glTexImage2D`` の対応物で、最後の引数が ``ArrayBufferView`` のオーバーロード。

    * ``pixels`` が ``null`` の場合は、ゼロクリアされた十分なサイズのバッファーが渡される。
    * ``pixels`` が ``null`` 以外の場合、``pixels`` の型は読み込まれるデータのそれと一致しなければならない。

      * ``UNSIGNED_BYTE`` であれば ``Uint8Array`` または ``Uint8ClampedArray`` が、
      * ``UNSIGNED_SHORT_5_6_5``, ``UNSIGNED_SHORT_4_4``,
        ``UNSIGNED_SHORT_5_5_5_1`` であれば ``Uint16Array`` が

      渡されなければならない。型が一致しない場合は ``INVALID_OPERATION`` エラー。

    * ``pixels`` が ``null`` ではなくても、そのサイズが指定された
      ``width``, ``height``, ``format``, ``type``,
      ピクセル貯蔵パラメーターが必要とするサイズよりも小さい場合は
      ``INVALID_OPERATION`` エラーが起こる。
    * この関数の動作に影響する WebGL 固有のピクセル貯蔵パラメーターについては、次章で述べられる。

``texImage2D(target, level, internalformat, format, type, source)``
   ``glTexImage2D`` の対応物で、最後の引数が ``TexSourceImage`` のどれかであるオーバーロード。

    * 指定された要素や画像データを、現在束縛されている ``WebGLTexture`` にアップロードする。
    * テクスチャーの幅と高さは、別途述べられる項目が指定するように設定される。
    * 画像データ ``source`` は概念的にはまず ``format`` および ``type`` 引数で
      指定されたデータ型とフォーマットに変換されてから WebGL 実装に転送される。

      * フォーマットの変換表アリ。
      * 画像データのビット精度が失われるようなパックピクセルフォーマットが指定された場合、この精度の損失が必ず起こる。

    * ``source`` から WebGL 実装に転送される最初のピクセルは ``source`` の左上隅のものだ。
      この動作は、``ImageBitmap`` である場合を除き、
      ``UNPACK_FLIP_Y_WEBGL`` ピクセル貯蔵パラメータによって変更される。
    * ``source`` が各チャンネル 8 ビットの RGB または RGBA のロスレス画像を含む
      ``HTMLImageElement`` または ``ImageBitmap`` の場合、
      ブラウザーはチャンネルすべての完全な精度が保持されることを保証する。
    * 元の ``HTMLImageElement`` がアルファーチャンネルを含み、
      ``UNPACK_PREMULTIPLY_ALPHA_WEBGL`` ピクセル貯蔵パラメーターが ``false`` の場合、
      RGB 値が元のファイルフォーマットから直接得られたものであろうと、
      他のカラーフォーマットから変換されたものであろうと、
      アルファーチャンネルによって決して事前に乗算しないことが保証する。

    ----

    ``HTMLCanvasElement`` や ``OffscreenCanvas`` の
    ``CanvasRenderingContext2D`` の実装によっては、色の値が内部的に前乗算形式で保存される。
    このようなキャンバスを ``UNPACK_PREMULTIPLY_ALPHA_WEBGL`` ピクセル貯蔵パラメーターを
    ``false`` に設定した状態で WebGL テクスチャにアップロードすると、
    カラーチャンネルにアルファーチャンネルを乗算し直す必要があるが、
    これは損失の大きい処理だ。
    したがって、WebGL の実装では ``UNPACK_PREMULTIPLY_ALPHA_WEBGL`` ピクセル貯蔵パラメーターが
    ``false`` に設定されているときに、
    ``CanvasRenderingContext2D`` を介してキャンバスに最初に描画され、
    その後 WebGL テクスチャーにアップロードされたときに、
    アルファー値が 1.0 に満たない色を損失なしに保存することを保証できない。

    ----

    * 属性 ``data`` が中立化した ``ImageData`` でこの関数を呼び出すと ``INVALID_VALUE`` エラー。
    * 中立化した ``ImageData`` でこの関数が呼ばれた場合 ``INVALID_VALUE`` エラー。
    * 中立化した ``ImageBitmap`` でこの関数が呼ばれた場合 ``INVALID_VALUE`` エラー。
    * ``Document`` の ``origin`` と異なる ``HTMLImageElement`` または ``HTMLVideoElement`` でこの関数が呼び出された場合、
      または ``Bitmap`` の ``origin-clean`` フラグが ``false`` に設定されている
      ``HTMLCanvasElement``, ``ImageBitmap``, ``OffscreenCanvas`` でこの関数が呼び出された場合には
      ``SECURITY_ERR`` 例外が送出されなければならない。
    * ``source`` が ``null`` の場合は ``INVALID_VALUE`` エラー。

``texParameterf(target, pname, param)``
``texParameteri(target, pname, param)``
    ``glTexParameter{fi}`` の対応物。

``texSubImage2D(target, level, xoffset, yoffset, width, height, format, type, pixels)``
    ``glTexSubImage2D`` の対応物で、最後の引数が ``ArrayBufferView`` のオーバーロード。

    * ``format`` および ``pixels`` 引数の制限については ``texImage2D`` と同じ。
    * ``type`` がテクスチャーの定義に元々使われていた型と一致しない場合 ``INVALID_OPERATION`` エラーが発生。
    * ``pixels`` が ``null`` の場合 ``INVALID_VALUE`` エラー。
    * ``pixels`` が ``null`` でなくでも、そのサイズが、指定された
      ``width``, ``height``, ``format``, ``type``,
      およびピクセル貯蔵パラメーターが必要とするサイズよりも小さい場合は ``INVALID_OPERATION`` エラー。

``texSubImage2D(target, level, xoffset, yoffset, format, type, source)``
    ``glTexSubImage2D`` の対応物で、最後の引数が ``TexSourceImage`` のオーバーロード。

    * 現在束縛されている ``WebGLTexture`` の部分矩形を与えられた要素や画像データの内容で更新する。
    * 更新された部分矩形の幅と高さは、別項で指定されるとおりに決定される。
    * ``format`` および ``type`` 引数の解釈、および
      ``UNPACK_PREMULTIPLY_ALPHA_WEBGL`` ピクセル貯蔵パラメーターに関する注意点については
      ``texImage2D`` を参照すること。
    * ``source`` から WebGL 実装に転送される最初のピクセルは ``source`` の左上隅のものだ。
      この動作は、``ImageBitmap`` である場合を除き、
      ``UNPACK_FLIP_Y_WEBGL`` ピクセル貯蔵パラメータによって変更される。
    * ``type`` がテクスチャーの定義に元々使われていた型と一致しない場合 ``INVALID_OPERATION`` エラーが発生。
    * 属性 ``data`` が中立化した ``ImageData`` でこの関数を呼び出すと ``INVALID_VALUE`` エラー。
    * 中立化した ``ImageBitmap`` でこの関数が呼ばれた場合 ``INVALID_VALUE`` エラー。
    * ``Document`` の ``origin`` と異なる ``HTMLImageElement`` または ``HTMLVideoElement`` でこの関数が呼び出された場合、
      または ``Bitmap`` の ``origin-clean`` フラグが ``false`` に設定されている
      ``HTMLCanvasElement``, ``ImageBitmap``, ``OffscreenCanvas`` でこの関数が呼び出された場合には
      ``SECURITY_ERR`` 例外が送出されなければならない。
    * ``source`` が ``null`` の場合は ``INVALID_VALUE`` エラー。

5.14.9 Programs and Shaders
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

5.14.10 Uniforms and attributes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

5.14.11 Writing to the drawing buffer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

5.14.12 Reading back pixels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

5.14.13 Detecting context lost events
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

5.14.14 Detecting and enabling extensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

5.15 ``WebGLContextEvent``
----------------------------------------------------------------------

5.15.1 Attributes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

5.15.2 The Context Lost Event
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

5.15.3 The Context Restored Event
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

5.15.4 The Context Creation Error Event
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
