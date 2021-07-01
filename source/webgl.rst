======================================================================
WebGL 学習ノート
======================================================================

WebGL プログラミングに関するノート。

.. contents:: ノート目次

資料
======================================================================

WebGL を学習するのに有益な資料を列挙する。

* `WebGL: 2D and 3D graphics for the web - Web APIs \|
  MDN <https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API>`__:
  ここにある資料を基本書としてまずは学習していく。

  * Guides and tutorials を最初から再現、検証していくのがいい。Advanced までやり切る。
  * Standard interfaces では ``WebGLRenderingContext`` を主に調べることになる。
    OpenGL の構成要素とのインターフェイスがこれに集中しているからだ。

    * 各 API の Examples の節も大いに有益だ。

  * WebGL by example の章も一通りやるといい。

* `An intro to modern OpenGL. Table of Contents <https://duriansoftware.com/joe/an-intro-to-modern-opengl.-table-of-contents>`__:
  C 言語で書かれたプログラムの解説だ。WebGL
  コードに書き換えるのといい練習になる。

手筋
======================================================================

WebGL プログラミングの技法を思いつくまま、なるべく初歩的なものから高度なものに列挙する。

* HTML の ``canvas`` タグの使い方を習得する。レンダリングコンテキストオブジェクトをここから得る。

  * ``canvas.getContext('webgl')`` でそれを得る。そのオブジェクト名を
    ``gl`` とすること。決め打っていい。
  * キャンバスのサイズを指定する方法は、タグ属性 ``width`` と
    ``height`` を指定するものと、CSS のそれに指定するものがある。
    いろいろ試したが、タグ属性として無単位で寸法を設定すると絵が綺麗になる。

* ``WebGLRenderingContext`` のメンバー名と、元になっている OpenGL API
  の名前との対応関係を体で理解する。例を挙げると：

  * 定数名 ``GL_COLOR_BUFFER_BIT`` などは ``gl.COLOR_BUFFER_BIT``
    などのようになる。
  * 関数名 ``glVertrexAttribPointer`` などは
    ``gl.vertexAttribPointer`` などのようになる。

* OpenGL の学習と同様に、一色でベタ塗りされた画面を描画できるようになることを最初の目標にするといい。

* JavaScript にある次の配列系クラスを使いこなせるようになる。
  ``Array`` の基本的なインターフェイスはすべて使える：

  * ``Uint8Array``, ``Uint8ClampedArray``: RGBA 値などに応用
  * ``Uint16Array``, ``Uint32Array``: インデックスデータに応用
  * ``Float32Array``: 頂点データなどさまざまな用途に応用
  * ``ArrayBuffer``: バッファーデータに応用
  * ``DataView``: ``ArrayBuffer`` の生バイト列の操作をする。

    * メソッド ``setUint8`` などの第一引数はバイト単位であることに注意。

* メソッド ``gl.createBuffer`` が OpenGL の ``glGenBuffers``
  の代わりになるようだ。

* https://glmatrix.net/ から ``gl-matrix-min.js``
  を入手しておくとよい。適当に unminify して ``s/var/let/g``
  するとさらに良い。

  * ``mat4.create()`` で行列オブジェクトを生成するらしい。この戻り値に対して
    ``perspective``, ``translate`` などのメソッドを呼び出して成分を決める。

* ``gl.VertexAttribPointer`` の引数 ``normalize`` の型が ``GLboolean``
  ではなく JavaScript の基本型の ``Boolean`` であることに注意。これはハマった。

* JavaScript の関数 ``requestAnimationFrame`` の使い方を間違いなく習得すること。

* 画像ファイルからテクスチャーを生成するのに JavaScript のクラス
  ``Image`` を活用することをよく理解すること。特に ``onload``
  で非同期的に ``gl.texImage2D`` を呼び出せるのがたいへん具合が良い。

* このような動的にファイルをロードするコードがある場合、
  ``file://`` から始まるパスで HTML をブラウザーで開くと上手くいかない。
  作業ディレクトリーから HTTP サーバーを起動するのがいいだろう。例えば Python
  利用者ならば次のようにすればサーバーが稼働し、ブラウザーで
  ``http://localhost:8000/demo.html`` のようにすれば画面が出る。

  .. code:: console

     bash$ python -m http.server

* ビデオをテクスチャーに設定することが比較的容易に実現できる。

  * ``documentCreate`` で ``video`` タグを生成し、
    ``onplaying`` と ``ontimeupdate`` イベントハンドラーを実装する手法がある。

* ``script`` タグで GLSL コードが書ける？

  .. code:: html

     <script type="x-shader/x-vertex">...</script>

* 画像からテクスチャーを生成する場合、画像ファイルのフォーマットによってコードが若干変わる。
  例えば PNG と JPEG とでは ``gl.texImage2D`` の実引数を変えないとダメだ。
* GLSL コードを個別にテキストファイルに保存してあるとする。
  これを JavaScript コードから ``fetch`` でロードすることを考えると、
  それを呼び出す関数、さらにそれを呼び出す関数等々を非同期関数に書くのが自然になる。
* ベクトルや行列を仮引数にとる関数を自作する場合、成分の個数に気を配ること。
  ダサいのを覚悟で、成分数を決め打ちしたコードを定義するのが無難だ。
* C/C++ で言う基本型のサイズを JavaScript で得るには、例えば
  ``Float32Array.BYTES_PER_ELEMENT`` などの定数を参照する。
* マウスドラッグに対応するイベントハンドラーは次のものにするのが現代的だ。
  こうするとタッチスクリーンでのタッチイベントにも対応してくれる（と思われる）：

  .. code:: javascript

     canvas.onpointerdown = (event) => {
         canvas.onpointermove = (event) => {
             // Rotate, pan, etc.
         };
         canvas.setPointerCapture(event.pointerId);
     };

     canvas.onpointerup = (event) => {
         canvas.onpointermove = null;
         canvas.releasePointerCapture(event.pointerId);
     };

関連ノート
======================================================================

* :doc:`/haverbeke18/index`: 三周くらい読めば JavaScript プログラミングは大丈夫。
