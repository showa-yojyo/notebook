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

    この真偽値の属性 ``desynchronized`` は、入力からラスタライズまでの待ち時間の遅延が急所となる描画アプリケーションなど、
    特定の種類のアプリケーションを実装する際に役立つ。[MULTIPLEBUFFERING]_

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

* 頂点、インデックス、テクスチャ、その他のデータは、ECMAScript [ECMASCRIPT]_ で定義されている
  ``ArrayBuffer``, *Typed Array*, ``DataView`` を使用して WebGL 実装に転送される。
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

``getBufferParameter(target, pname)``
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

.. glossary::

   ``bindTexture(target, texture)``
       ``glBindTexure`` の対応物。

       * エラー発生は ``bindFramebuffer`` や ``bindRenderbuffer`` に準じる。

   ``compressedTexImage2D(target, level, internalformat, width, height, border, pixels)``
   ``compressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, pixels)``
       ``glCompressedTexImage2D``, ``glCompressedTexSubImage2D`` の対応物。

       * コア WebGL 仕様では、サポートされる圧縮テクスチャーフォーマットを何も定義していない。
       * デフォルトでは、これらのメソッドは ``INVALID_ENUM`` エラーを生成し、直ちに戻る。
         詳しくは次章で述べられる。

   ``copyTexImage2D(target, level, internalformat, x, y, width, height, border)``
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

WebGL でもレンダリングには OpenGL ES のシェーディング言語である
GLSL ES で記述されたシェーダーを使用する必要がある。シェーダーは、

#. ソースコード文字列を ``shaderSource`` で読み込み、
#. それを ``compileShader`` でコンパイルして
#. ``attachShader`` でプログラムに添付し、
#. ``linkProgram`` でリンクしてから
#. ``useProgram`` で使用する必要がある。

----

``attachShader(program, shader)``
    ``glAttachShader`` の対応物。

    * ``program`` または ``shader`` シェーダーのいずれかが、このものとは異なる
      ``WebGLRenderingContext`` によって生成されたものである場合 ``INVALID_OPERATION`` エラー。

``bindAttribLocation(program, index, name)``
    ``glBindAttribLocation`` の対応物。

    * ``program`` がこれとは異なる ``WebGLRenderingContext`` が生成したものである場合 ``INVALID_OPERATION`` エラー。
    * ``name`` が定義された制限よりも長い場合、``INVALID_VALUE`` エラー。
    * ``name`` が予約されている WebGL 接頭辞のいずれかで始まる場合 ``INVALID_OPERATION`` エラー。
    * WebGL の実装で行われる追加の検証については別項を参照。

``compileShader(shader)``
    ``glCompileShader`` の対応物。

    * ``shader`` がこれとは異なる ``WebGLRenderingContext`` が生成したものである場合 ``INVALID_OPERATION`` エラー。
    * WebGL の実装であることによる追加的な制約、サポートされる構造、検証については、関連する記述を参照すること。

``createProgram()``
    ``glCreateProgram`` の対応物。

    ``WebGLProgram`` オブジェクトを生成し、``glCreateProgram`` を呼び出したかのようにプログラムオブジェクトに名前を付けて初期化する。

``createShader(type)``
    ``glCreateShader`` の対応物。

    * ``WebGLShader`` オブジェクトを生成し、まるで
      ``glCreateShader`` を呼び出したかのようにシェーダーオブジェクト名を付けて初期化する。

``deleteProgram(program)``
    ``glDeleteProgram`` の対応物。

    * ``program`` または ``shader`` シェーダーのいずれかが、このものとは異なる
      ``WebGLRenderingContext`` によって生成されたものである場合 ``INVALID_OPERATION`` エラー。
    * まるで ``glDeleteProgram`` を呼び出すかのように、``program`` に含まれるプログラムオブジェクトを削除するようにマークする。
    * 内包されている GL オブジェクトには JavaScript オブジェクトが破棄されたときに自動的に削除マークが付けられるが、
      このメソッドを呼び出すことで、オブジェクトに早期に削除マークを付けることができる。
    * 下層の GL オブジェクトは、JS オブジェクトが破棄されたときに自動的に削除マークが付けられますが、このメソッドを使用すると、オブジェクトを早期に削除マークすることができます。

``deleteShader(shader)``
    ``glDeleteShader`` の対応物。

    * まるで ``glDeleteShader`` を呼び出すかのように ``shader`` に含まれるシェーダーオブジェクトを削除するようにマークする。
    * 内包されている GL オブジェクトには JavaScript オブジェクトが破棄されたときに自動的に削除マークが付けられるが、
      このメソッドを呼び出すことで、オブジェクトに早期に削除マークを付けることができる。
    * ``shader`` がこれとは異なる ``WebGLRenderingContext`` が生成したものである場合 ``INVALID_OPERATION`` エラー。

``detachShader(program, shader)``
    ``glDetachShader`` の対応物。

    * ``program`` または ``shader`` シェーダーのいずれかが、このものとは異なる
      ``WebGLRenderingContext`` によって生成されたものである場合 ``INVALID_OPERATION`` エラー。

``getAttachedShaders(program)``
    ``glGetAttachedShaders`` の対応物。

    * ``program`` に取り付けたれたシェーダーのリストを返す。
    * ``program`` がこれとは異なる ``WebGLRenderingContext`` が生成したものである場合 ``INVALID_OPERATION`` エラー。
    * この関数の実行中に OpenGL エラーが発生した場合は ``null`` を返す。

``getProgramParameter(program, pname)``
    ``glGetProgramParameter`` の対応物。

    * ``program`` がこれとは異なる ``WebGLRenderingContext`` が生成したものである場合 ``INVALID_OPERATION`` エラー。
    * ``program`` に応じた ``pname`` の値を返す。戻り値の型は要求された名前に対して自然な型とする。
    * ``pname`` の値は次のいずれかとする：

      * ``DELETE_STATUS``
      * ``LINK_STATUS``
      * ``VALIDATE_STATUS``
      * ``ATTACHED_SHADERS``
      * ``ACTIVE_ATTRIBUTES``
      * ``ACTIVE_UNIFORMS``

      これ以外の値は ``INVALID_ENUM`` エラーとし ``null`` を返す。

    * この関数の実行中に OpenGL エラーが発生した場合は ``null`` を返す。

``getProgramInfoLog(program)``
    ``glGetProgramInfoLog`` の対応物。

    * ``program`` がこれとは異なる ``WebGLRenderingContext`` が生成したものである場合 ``INVALID_OPERATION`` エラー。
    * この関数の実行中に OpenGL エラーが発生した場合は ``null`` を返す。

``getShaderParameter(shader, pname)``
    ``glGetShaderParameter`` の対応物。

    * ``shader`` がこれとは異なる ``WebGLRenderingContext`` が生成したものである場合 ``INVALID_OPERATION`` エラー。
    * ``shader`` に応じた ``pname`` の値を返す。戻り値の型は要求された名前に対して自然な型とする。
    * ``pname`` の値は次のいずれかとする：

      * ``SHADER_TYPE``
      * ``DELETE_STATUS``
      * ``COMPILE_STATUS``

      これ以外の値は ``INVALID_ENUM`` エラーとし ``null`` を返す。

    * この関数の実行中に OpenGL エラーが発生した場合は ``null`` を返す。

``getShaderPrecisionFormat(shadertype, precisiontype)``
    ``glGetShaderPrecisionFormat`` の対応物。

    指定されたシェーダーの数値フォーマットの範囲と精度を記述した ``WebGLShaderPrecisionFormat`` を返す。

    * ``shadertype`` の値は ``FRAGMENT_SHADER`` または ``VERTEX_SHADER`` だ。
    * ``precisiontype`` の値は次のいずれかとする：

      * ``LOW_FLOAT``
      * ``MEDIUM_FLOAT``
      * ``HIGH_FLOAT``
      * ``LOW_INT``
      * ``MEDIUM_INT``
      * ``HIGH_INT``

    * この関数の実行中に OpenGL エラーが発生した場合は ``null`` を返す。

``getShaderInfoLog(shader)``
    ``glGetShaderInfoLog`` の対応物。

    * ``shader`` がこれとは異なる ``WebGLRenderingContext`` が生成したものである場合 ``INVALID_OPERATION`` エラー。
    * この関数の実行中に OpenGL エラーが発生した場合は ``null`` を返す。

``getShaderSource(shader)``
    ``glGetShaderSource`` の対応物。

    * ``shader`` がこれとは異なる ``WebGLRenderingContext`` で生成されたものならば ``INVALID_OPERATION`` エラー。
    * この関数の実行中に OpenGL エラーが発生した場合は ``null`` を返す。

``isProgram(program)``
    ``glIsProgram`` の対応物。

    * 渡された ``WebGLProgram`` が有効かどうかを返す。
    * ``program`` がこれと異なる ``WebGLRenderingContext`` によって生成されたものならば ``false`` を返す。
    * ``program`` の ``invalidated`` フラグが設定されている場合は ``false`` を返す。

``isShader(shader)``
    ``glIsShader`` の対応物。

    * 渡された ``WebGLShader`` が有効かどうかを返す。
    * ``shader`` がこれと異なる ``WebGLRenderingContext`` によって生成されたものならば ``false`` を返す。
    * ``shader`` の ``invalidated`` フラグが設定されている場合は ``false`` を返す。

``linkProgram(program)``
    ``glLinkProgram`` の対応物。

    * 動作の詳細は OpenGL ES 2.0 どおりだが、以下の点が明確になっている：

      * ``linkProgram`` は、このグループの中で、渡されたプログラムのリンク状態や、
        参照する内部実行コードに影響を与える唯一のAPIです。
      * プログラムからのシェーダーオブジェクトの取り付けおよび取り外し、
        プログラムに取り付けられたシェーダーオブジェクトの修正、およびコンパイルなどの操作は、
        そのプログラムのリンク状態にも、そのプログラムが参照する実行コードにも影響を与えない。

    * ``program`` が、これとは異なる ``WebGLRenderingContext`` が生成したものである場合 ``INVALID_OPERATION`` エラー。
    * 与えられた ``program`` が正常にリンクされ、``useProgram`` で定義された現在使用中のプログラムオブジェクトでもある場合、
      生成された実行コードは現在のレンダリング状態の一部として直ちにインストールされる。
      それ以外の場合は、現在のレンダリング状態で参照されている実行可能コードは、
      ``linkProgram`` の呼び出しによって変更されることはない。
    * WebGL の実装で実施される追加的な制約や実行される検証については別項で述べられる。

``shaderSource(shader, source)``
    ``glShaderSource`` の対応物。

    * ``shader`` がこれとは異なる ``WebGLRenderingContext`` が生成したものである場合 ``INVALID_OPERATION`` エラー。
    * WebGL の実装であることによる追加的な制約、サポートされる構造、検証については、関連する記述を参照すること。

``useProgram(program)``
    ``glUseProgram`` の対応物。

    * ``program`` がこれとは異なる ``WebGLRenderingContext`` が生成したものである場合 ``INVALID_OPERATION`` エラー。

``validateProgram(program)``
    ``glValidateProgram`` の対応物。

    * ``program`` がこれとは異なる ``WebGLRenderingContext`` が生成したものである場合 ``INVALID_OPERATION`` エラー。

5.14.10 Uniforms and attributes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

シェーダーで使われる値は、ユニフォームや頂点の属性として渡される。

----

.. glossary::

   ``disableVertexAttribArray(index)``
   ``enableVertexAttribArray(index)``
       インデックスの頂点属性を配列として無効・有効にする。

       * WebGL では有効な頂点属性に関して OpenGL ES 2.0 以上の規則が適用される。

   ``getActiveAttrib(program, index)``
       ``program`` の ``index`` の頂点属性のサイズ、型、名前を記述した ``WebGLActiveInfo`` オブジェクトを返す。

       * ``index`` が範囲外の場合は ``INVALID_VALUE`` エラーを発生して ``null`` を返す。
       * ``program`` がこれとは異なる ``WebGLRenderingContext`` が生成したものである場合は ``INVALID_OPERATION`` エラー。
       * この関数の実行中に OpenGL エラーが発生した場合は ``null`` を返す。

   ``getActiveUniform(program, index)``
       ``program`` の ``index`` にあるユニフォームのサイズ、型、名前を記述した ``WebGLActiveInfo`` オブジェクトを返す。

       * ``index`` が範囲外の場合は ``INVALID_VALUE`` エラーを発生して ``null`` を返す。
       * ``program`` がこれとは異なる ``WebGLRenderingContext`` が生成したものである場合は ``INVALID_OPERATION`` エラー。
       * この関数の実行中に OpenGL エラーが発生した場合は ``null`` を返す。

   ``getAttribLocation(program, name)``
       ``glGetAttribLocation`` の対応物。

       * ``program`` がこれとは異なる ``WebGLRenderingContext`` が生成したものである場合は ``INVALID_OPERATION`` エラーとなり ``-1`` を返す。
       * ``name`` が定義された制限よりも長い場合は ``INVALID_VALUE`` エラーとなり ``-1`` を返す。
       * ``name`` が予約されている WebGL 接頭辞のいずれかで始まる場合は ``-1`` を返す。
       * コンテキストの webgl context lost フラグが設定されている場合は ``-1`` を返す。
       * ``program`` の ``invalidated`` フラグが設定されている場合は ``INVALID_OPERATION`` エラーとなり ``-1`` を返す。
       * WebGL の実装で行われる追加の検証については、別項を参照すること。

   ``getUniform(program, location)``
       ``program`` の ``location`` にあるユニフォームの値を返す。

       * 戻り値の型はユニフォーム型によって決まる。表にまとめられている。
       * 列や *TypedArray* を返すすべての問い合わせは、毎回新しいオブジェクトを返す。
       * ``program`` または ``location`` が、自身の ``WebGLRenderingContext``
         とは異なるコンテキストが生成したものである場合には ``INVALID_OPERATION`` エラー。
       * この関数の実行中に OpenGL エラーが発生した場合は ``null`` を返す。

   ``getUniformLocation(program, name)``
       ``program`` 内の特定のユニフォーム変数の位置を表す ``WebGLUniformLocation`` を返す。

       * ``name`` が ``program`` 内のアクティブなユニフォーム変数に対応していない場合、戻り値は ``null`` となる。
       * ``program`` がこれとは異なる ``WebGLRenderingContext`` が生成したものである場合は ``INVALID_OPERATION`` エラー。
       * ``name`` が定義された制限よりも長い場合は ``INVALID_VALUE`` エラーとなり ``null`` を返す。
       * ``name`` が予約されている WebGL 接頭辞のいずれかで始まる場合は ``null`` を返す。
       * WebGL の実装で行われる追加の検証については、別項を参照すること。
       * この関数の実行中に OpenGL エラーが発生した場合は ``null`` を返す。

   ``getVertexAttrib(index, pname)``
       ``index`` の頂点属性について ``pname`` が要求する情報を返す。

       * 戻り値の型は要求された情報に応じて決まる。表にまとめられている。
       * 列や *TypedArray* を返すすべての問い合わせは、毎回新しいオブジェクトを返す。
       * 無効な ``pname`` を与えると ``INVALID_ENUM`` エラー。
       * OpenGL エラーが起こると ``null`` を返す。

   ``getVertexAttribOffset(index, pname)``
       ``glGetVertexAttribOffset`` の対応物。

       * コンテキストの webgl context lost フラグが設定されている場合は 0 を返す。

   ``uniform[1234][fi](location, ...)``
   ``uniform[1234][fi]v(location, ...)``
   ``uniformMatrix[234]fv(location, transpose, ...)``
       各関数は、指定されたユニフォームまたはユニフォームを指定された値に設定します。

       * ``location`` が ``null`` ではなく、現在使用しているプログラムから以前に
         ``getUniformLocation`` を呼び出して取得したものでない場合 ``INVALID_OPERATION`` エラーになる。
       * ``location`` が ``null`` の場合、渡されたデータは静かに無視され、ユニフォーム変数は変更されない。
       * ベクトル形式（名前が ``v`` で終わる関数）に渡された配列の長さが無効な場合 ``INVALID_VALUE`` エラー。

         * 長さが無効であるとは、長さが短すぎるか、割り当てられた型の整数倍でないものをいう。

       ----

       ``uniform1i`` を使用してサンプラーのユニフォームを更新すると、
       一部の実装でパフォーマンス上の問題が発生する。
       サンプラーユニフォームが参照するテクスチャーを変更するには、
       ユニフォーム自体を更新するために ``uniform1i`` を使用するよりも、
       ユニフォームが参照するテクスチャーユニットに新しいテクスチャーを束縛する方が望ましい。

   ``vertexAttrib[1234]f(index, ...)``
   ``vertexAttrib[1234]fv(index, ...)``
       ``index`` の頂点属性を、与えられた定数値に設定する。

       * ``vertexAttrib`` で設定された値は、``drawArrays`` や ``drawElements`` の呼び出しが間にあったとしても、
         ``CURRENT_VERTEX_ATTRIB`` パラメーターを持つ ``vertexAttrib`` 関数から返されることが保証される。
       * ベクトル形式（名前が ``v`` で終わる関数）に渡された配列の長さが無効な場合 ``INVALID_VALUE`` エラー。

   ``vertexAttribPointer(index, size, type, normalized, stride, offset)``
       ``ARRAY_BUFFER`` ターゲットに束縛されている ``WebGLBuffer`` オブジェクトを
       ``index`` の頂点属性に割り当てる。

       * ``size`` は属性ごとの成分の数。
       * ``stride`` および ``offset`` はバイト単位。
       * ``stride`` および ``offset`` は ``type`` と ``size`` に適していなければならず、
         そうでなければ ``INVALID_OPERATION`` エラーとなる。
       * ``offset`` が負の値の場合は ``INVALID_VALUE`` エラーとなる。
       * ``WebGLBuffer`` が ``ARRAY_BUFFER`` ターゲットに束縛されておらず、
         ``offset`` が 0 以外の場合は ``INVALID_OPERATION`` エラーとなる。
       * WebGL では、サポートされる ``stride`` の最大値は 255 だ。

5.14.11 Writing to the drawing buffer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

OpenGL ES 2.0 には、描画バッファーへのレンダリングを可能にする呼び出しが三つある：

* ``clear``
* ``drawArrays``
* ``drawElements``

さらに、レンダリングは、描画バッファーかフレームバッファーオブジェクトに対して行うことができる。
描画バッファーへのレンダリングが指示された場合、三つのレンダリング呼び出しのいずれかを実行すると、
次の合成操作の開始時に、描画バッファーが HTML ページ合成器に提示される。

これらの呼び出しのいずれかが完全なフレームバッファの欠落した attachment に描画しようとした場合、
その attachment には何も描画されず、エラーが発生することもない。

----

``clear(mask)``
    ``glClear`` の対応物。

``drawArrays(mode, first, count)``
    ``glDrawArrays`` の対応物。

    * ``first`` が負の値の場合 ``INVALID_VALUE`` エラー。
    * ``CURRENT_PROGRAM`` が ``null`` の場合 ``INVALID_OPERATION`` エラー。

``drawElements(mode, count, type, offset)``
    ``glDrawElements`` の対応物。

    現在束縛されている要素配列バッファーを使用して描画する。

    * ``offset`` はバイト単位で、``type`` のサイズの有効な倍数でなければならない。
    * ``offset`` は非負でなければならず、そうでなければ ``INVALID_VALUE`` エラーとなる。
    * ``count`` が 0 より大きい場合は ``ELEMENT_ARRAY_BUFFER`` バインディングポイントに非 ``null`` の
      ``WebGLBuffer`` が束縛されていなければならず、そうでない場合は ``INVALID_OPERATION`` エラーとなる。
    * ``CURRENT_PROGRAM`` が ``null`` の場合は ``INVALID_OPERATION`` エラー。
    * WebGL では ``drawArays`` および ``drawElements`` の呼び出し時に
      OpenGL ES 2.0 で指定されている以上のエラーチェックを行う。

``finish()``
    ``glFinish`` の対応物。

``flush()``
    ``glFlush`` の対応物。

5.14.12 Reading back pixels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

現在のフレームバッファ内のピクセルを ``ArrayBufferView`` オブジェクトに読み戻すことができる。

----

``readPixels(x, y, width, height, format, type, pixels)``
    フレームバッファーの指定された矩形内のピクセルデータでピクセルを埋める。

    * ``readPixels`` が返すデータは、最後に送信された描画コマンドの時点でのものでなければならない。

    If this function attempts to read from a complete framebuffer with a missing color attachment, an INVALID_OPERATION error is generated per Reading from a Missing Attachment.

    * ピクセルの ``type`` は読み込まれるデータのそれと一致していなければならない。例えば、

      * ``UNSIGNED_BYTE`` であれば、``Uint8Array`` または ``Uint8ClampedArray`` を、
      * ``UNSIGNED_SHORT_5_6_5``, ``UNSIGNED_SHORT_4_4_4``, ``UNSIGNED_SHORT_5_5_5_1`` であれば、``Uint16Array`` を、
      * ``FLOAT`` であれば ``Float32Array`` を

      供給しなければならない。タイプが一致しない場合 ``INVALID_OPERATION`` エラーとなる。

    * ``format`` と ``type`` の組み合わせは二つしかない。

      * ``format = RGBA`` で ``type = UNSIGNED_BYTE``
      * 実装で選択されたフォーマット

      このフォーマットの ``format`` と ``type`` の値は、``getParameter`` に定数
      ``IMPLEMENTATION_COLOR_READ_FORMAT`` と ``IMPLEMENTATION_COLOR_READ_TYPE`` を指定して呼び出すことで決定できる。

      * 実装で選択されるフォーマットは、現在束縛されているレンダリング面のフォーマットに応じて異なる場合がある。
      * サポートされていない ``format`` と ``type`` の組み合わせの場合 ``INVALID_OPERATION`` エラーとなる。

    * ``IMPLEMENTATION_COLOR_READ_[FORMAT,TYPE]`` の問い合わせは、他で使用されていない列挙型を返すことがあるため、
      これらの列挙型を ``readPixels`` に提供しても、必ずしも ``INVALID_ENUM`` エラーとなるわけではない。
    * ``pixels`` が ``null`` の場合 ``INVALID_VALUE`` エラーとなる。
    * ``pixels`` が ``null`` ではないが、ピクセル格納モードを考慮して、
      指定された矩形内のすべてのピクセルを取得するのに十分な大きさではない場合、
      ``INVALID_OPERATION`` エラーとなる。
    * フレームバッファーの外側にあるピクセルについては、対応する destination バッファーの範囲はそのままだ。
    * この関数が、色 attachment がない完全なフレームバッファーから読み取ろうとすると、
      ``INVALID_OPERATION`` エラーとなる。

5.14.13 Detecting context lost events
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

モバイル機器の電源イベントなどが発生すると WebGL レンダリングコンテキストが失われ、
アプリケーションの再構築が必要になることがある。

----

``isContextLost()``
    フラグ webgl context lost が設定されているかどうかを返す。

5.14.14 Detecting and enabling extensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* WebGL の実装は、拡張装置を最初に使って機能を有効にすることなしに、
  追加のパラメーター、定数、関数をサポートしてはならない。

  * 関数 ``getSupportedExtensions`` は、この実装がサポートする拡張機能の文字列の配列を返す。
  * 拡張機能を有効にするには、これらの文字列のうちの一つを関数 ``getExtension`` に渡すことだ。

    * この呼び出しは、その拡張機能で定義されているあらゆる定数と関数を含むオブジェクトを返す。
    * このオブジェクトの定義はその拡張機能に固有のものであり、拡張機能の仕様が定義せねばならないものだ。

* いったん拡張が有効になると、WebGL コンテキストが失われても無効にしかならない。

  * ただし ``WEBGL_lose_context`` 拡張は例外だ。コンテキストが失われてもアクティブな状態を維持する。
  * ``getExtension`` が返すオブジェクトなどの、無効である拡張機能が参照するオブジェクトは、
    いずれも WebGL レンダリングコンテキストに関連付けられなくなる。
  * ``WebGLObject`` から派生したすべての拡張オブジェクトのフラグ ``invalidated`` は
    ``true`` に設定される。
  * コンテキストが失われた後の拡張機能のメソッドの動作は先の節で定義した。

* 拡張機能を無効にする仕組みは他にはない。
* 大文字小文字を区別しない比較を考慮して、同じ拡張文字列で
  ``getExtension`` を複数回呼び出すと、その拡張が有効である限り、
  同一のオブジェクトが返されなければならない。

  * 最初に ``getExtension`` を呼び出して有効にすることなしに任意の拡張機能を使用しようとすると、
    適切な GL エラーが起こらねばならず、その機能を使用してはならない。

* 本仕様では、どんな拡張をも定義しない。個別の WebGL 実装がサポートする拡張は、
  個別の WebGL 拡張レジストリーが定義する。

----

``getSupportedExtensions()``
    サポートされているすべての拡張文字列の一覧を返す。

``getExtension(name)``
    ``getSupportedExtensions`` から返された名前の一つに対して、
    ``name`` が ASCII の大文字と小文字を区別せずに一致する [HTML]_ ときに、
    かつそのときに限りオブジェクトを返す。そうでない場合は ``null`` を返す。

    * ``getExtensions`` から返されるオブジェクトには、その拡張機能が提供する定数や関数が含まれている。
    * 拡張機能が定数や関数を定義していない場合には、返されるオブジェクトにそういうものが含まれていなくてもかまわないが、
      それでも一意のオブジェクトを返さなければならない。
      このオブジェクトは、その拡張機能が有効であることを示すために用いられる。

5.15 ``WebGLContextEvent``
----------------------------------------------------------------------

WebGL はレンダリングコンテキストの状態の重要な変更に対応して ``WebGLContextEvent`` イベントを生成する。
イベントは DOM イベントシステム [DOM3EVENTS]_ を使って送信され、レンダリングコンテキストに関連付けられたキャンバスに急送される。
``WebGLContextEvent`` イベントを発生させることができる状態変化の種類には、コンテキストの

* 消滅、
* 回復、
* 作成不能

がある。

``e`` という名前のコンテキストイベントが発生するということは、

* ``type`` 属性 [DOM4]_ が ``e`` に初期化され、
* ``cancelable`` 属性が ``true`` に初期化され、
* ``isTrusted`` 属性が ``true`` に初期化された

``WebGLContextEvent`` インターフェイスを使用するイベントが、
指定されたオブジェクトに急送されるということだ。

----

* ``WebGLContextEvent``
* ``WebGLContextEventInit``

----

この節に並んでいるタスクすべて [HTML]_ の発生源は WebGL タスク発生源だ。

5.15.1 Attributes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``statusMessage``
    追加情報を含む文字列。追加情報がない場合は空。

5.15.2 The Context Lost Event
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ブラウザーが ``WebGLRenderingContext`` コンテキストに関連付けられた
描画バッファーが失われたことを検出すると、次の手順を実行する：

#. ``canvas`` をコンテキストの ``canvas`` とする。
#. コンテキストの webgl context lost フラグが設定されている場合は、手順をここで中止する。
#. コンテキストの webgl context lost フラグを設定する。
#. このコンテキストで作成された各 ``WebGLObject`` インスタンスの ``invalidated`` フラグを設定する。
#. ``WEBGL_lose_context`` 以外のすべての拡張機能を無効にする。
#. 以下の手順を実行するタスクをキューに入れる：

   #. ``webglcontextlost`` という名前のコンテキストイベントを ``canvas`` で発射させ、
      その ``statusMessage`` 属性を空に設定する。
   #. イベントの ``canceled`` フラグが設定されていない場合は、手順をここで中止する。
   #. 以下の手順を非同期で実行する：

      * 回復可能な描画バッファーを待機する。
      * コンテキストの描画バッファーを復元するタスクをキューに入れる。

----

以下のコード（仕様書のものを一部改変）は、``webglcontextlost`` イベントのデフォルトの動作を防ぎ、
``webglcontextrestored`` イベントの発信を可能にするものだ：

.. code:: javascript

   canvas.addEventListener("webglcontextlost", e => {
       e.preventDefault();
   }, false);

5.15.3 The Context Restored Event
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ブラウザーが ``WebGLRenderingContext`` コンテキストの描画バッファーを復元するには、次の手順を実行する必要がある：

#. ``canvas`` をコンテキストに関連付けられた ``canvas`` とする。
#. コンテキストの webgl context lost フラグが設定されていない場合は、ここで手順を中止する。
#. コンテキストの作成パラメーターで指定された設定を使用して描画バッファーを生成し、
   その描画バッファーをコンテキストに関連付け、以前の描画バッファーを破棄する。
#. コンテキストの webgl context lost flag をクリアします。
#. コンテキストの OpenGL エラー状態をリセットする。
#. ``webglcontextrestored`` という名前の WebGL コンテキストイベントを ``canvas`` で発射させ、
   その ``statusMessage`` 属性を空にする。

----

コンテキストがすると、それまでに作成されたテクスチャーやバッファーなどの WebGL リソースが無効になる。
以前に有効だった拡張は復元されない。
変更された状態や破棄された拡張やリソースすべてをアプリケーションが復元する必要がある。

----

アプリケーションがコンテキストの消失と復元をどのように処理するかを示す擬似コード：

.. code:: javascript

   function initializeGame() {
       initializeWorld();
       initializeResources();
   }

   function initializeResources() {
       initializeShaders();
       initializeBuffers();
       initializeTextures();

       // ready to draw, start the main loop
       renderFrame();
   }

   function renderFrame() {
       updateWorld();
       drawSkyBox();
       drawWalls();
       drawMonsters();

       requestId = window.requestAnimationFrame(renderFrame, canvas);
   }

   canvas.addEventListener("webglcontextlost", event => {
       // inform WebGL that we handle context restoration
       event.preventDefault();

       // Stop rendering
       window.cancelAnimationFrame(requestId);
   }, false);

   canvas.addEventListener("webglcontextrestored", event => {
       initializeResources();
   }, false);

   initializeGame();

* コンテキストがなくなったときにはアニメーションをいったん止める。
* コンテキストが復活したときにはリソース各種を自力で初期化し直す。
  だから、リソース初期化コードをカプセル化しておく（普通は関数の形式で）のはたいせつだ。
  そのあとアニメーションを再開させるのも忘れてはならない。

5.15.4 The Context Creation Error Event
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ブラウザーが WebGL コンテキスト作成エラーをキャンバスで発射する場合には次の手順を実行する：

#. ``canvas`` で ``webglcontextcreationerror`` という名前の WebGL コンテキストイベントを発射し、
   オプションで ``statusMessage`` 属性に失敗の性質に関するプラットフォーム依存の文字列を設定する。

----

次のコードは、アプリケーションがコンテキスト作成の失敗に関する情報を取得する方法を示すものだ：

.. code:: javascript

   let errorInfo = "";

   function onContextCreationError(event) {
       canvas.removeEventListener("webglcontextcreationerror", onContextCreationError, false);
       errorInfo = e.statusMessage || "Unknown";
   }

   canvas.addEventListener("webglcontextcreationerror", onContextCreationError, false);

   const gl = canvas.getContext("webgl");
   if(!gl) {
       alert("A WebGL context could not be created.\nReason: " + errorInfo);
   }
