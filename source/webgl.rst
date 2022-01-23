======================================================================
WebGL 学習ノート
======================================================================

WebGL プログラミングに関するノート。OpenGL についての私の知識が古くなってしまっているので、
それも併せて学習していこう。

現状、全然整理し切れていない。

.. contents:: ノート目次

資料
======================================================================

WebGL を学習するのに有益な資料を列挙する。これとは別に、純正 OpenGL 用解説資料を
WebGL に翻訳しながら学習するということも有力だ。

* `WebGL Overview - The Khronos Group Inc <https://www.khronos.org/webgl/>`__:
  WebGL 総本山。関連仕様書をダウンロードしてローカルディスクに保存しておくと吉。
  なお、DeepL を利用する都合上、PDF よりは HTML のほうが具合がいい。
* `WebGL: 2D and 3D graphics for the web - Web APIs \|
  MDN <https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API>`__:
  ここにある資料を基本書としてまずは学習していく。

  * Guides and tutorials を最初から再現、検証していくのがいい。Advanced までやり切る。
  * Standard interfaces では ``WebGLRenderingContext`` を主に調べることになる。
    OpenGL の構成要素とのインターフェイスがこれに集中しているからだ。

    * 各 API の Examples の節も大いに有益だ。

  * WebGL by example の章も一通りやるといい。

* `An intro to modern OpenGL. Table of Contents <https://duriansoftware.com/joe/an-intro-to-modern-opengl.-table-of-contents>`__:
  C 言語で書かれたプログラムの解説だ。WebGL コードに書き換えるのといい練習になる。
* `WebGL Fundamentals <https://webglfundamentals.org/>`__: OpenGL のそれも含む基礎から学ぶ。
  このサイトの造りは恐ろしく良い。熟読推奨。
* `WebGL2 Fundamentals <https://webgl2fundamentals.org/>`__: 上記サイトの続編。
  今ならこちらだけを読むほうがいい。熟読推奨。
* `glMatrix <https://glmatrix.net/>`__: ベクトルや行列の演算をする JavaScript ライブラリー。
  効率を優先する必要があるからだろうが、インターフェイスに若干クセがある。
* `The Book of Shaders <https://thebookofshaders.com/>`__:
  断片シェーダーの技法に磨きをかける一冊。GLSL のバージョンがやや古いところを読者がカバーしたい。
  おすすめは easing の概念を丹念に説明した章だ。
  グラフィックス以外にも応用が効くものなので、時間をかけて習得する価値がある。

環境構築
======================================================================

* モダンなブラウザーとテキストエディター
* HTTP サーバーを起動できるようにしておく。
  例えば Python を使えるのならば次のコマンドでカレントディレクトリーをルートにして
  サーバーが開始する。<http://localhost:8000/> を開くと ``./index.html`` が表示される。

  .. code:: console

     bash$ python -m http.server 8000 --bind 127.0.0.1

手筋
======================================================================

WebGL プログラミングの技法を思いつくまま、なるべく初歩的なものから高度なものに列挙する。

基本的には WebGL 2 を採用する。

.. code:: javascript

   const canvas = document.querySelector("#mycanvas");
   const gl = canvas.getContext('webgl2');

未整理項目
----------------------------------------------------------------------

* WebGL 2 を使う場合

  * GLSL コードの物理的な一行目を次の内容にする：

    .. code:: glsl

       #version 300 es

    よりモダンなシェーダーの書き方を別途学習する必要がある。
    ``layout(location = i)`` 記法が利用できるのは大きい。
  * VAO を使う必要があるはず。次のような構造のコードができる：

    .. code:: javascript

       const vao = gl.createVertexArray();
       gl.bindVertexArray(vao);

       // gl.bindBuffer, gl.enableVertexAttribArray, etc.

       gl.deleteVertexArray(vao);

* シェーダーコードに次のような宣言が必要：

  .. code:: glsl

     precision highp float;

Hello world
----------------------------------------------------------------------

* OpenGL の学習と同様に、一色でベタ塗りされた画面を描画できるようになることを最初の目標にするといい。
* ``script`` タグで GLSL コードが書ける。

  .. code:: html

     <script type="x-shader/x-vertex" id="shader">...</script>

  この形式では ``document.querySelector("#shader").innerHTML`` を
  ``gl.shaderSource`` に実引数として渡すことで動作する。

* GLSL コードを個別にテキストファイルに保存してあるとする。
  これを JavaScript コードから ``fetch`` でロードすることを考えると、
  それを呼び出す関数、さらにそれを呼び出す関数等々を非同期関数に書くのが自然になる。

OpenGL との相違点と JavaScript 固有の事情
----------------------------------------------------------------------

* ``WebGLRenderingContext`` のメンバー名と、元になっている OpenGL API
  の名前との対応関係を体で理解する。例を挙げると：

  * 定数名 ``GL_COLOR_BUFFER_BIT`` などは ``gl.COLOR_BUFFER_BIT``
    などのようになる。
  * 関数名 ``glVertrexAttribPointer`` などは
    ``gl.vertexAttribPointer`` などのようになる。

* WebGL は OpenGL 同様に強力に型付けされたデータを必要とするので、
  次の JavaScript クラスを使いこなせるようにしておくことだ：

  * ``Uint8Array``, ``Uint8ClampedArray``: RGBA 値などに応用
  * ``Uint16Array``, ``Uint32Array``: インデックスデータに応用
  * ``Float32Array``: 頂点データなどさまざまな用途に応用
  * ``ArrayBuffer``: バッファーデータに応用
  * ``DataView``: ``ArrayBuffer`` の生バイト列の操作をする。

    * メソッド ``setUint8`` などの第一引数はバイト単位であることに注意。

* C/C++ で言う基本型のサイズを JavaScript で得るには、例えば
  ``Float32Array.BYTES_PER_ELEMENT`` などの定数を参照する。
* メソッド ``gl.createBuffer`` が OpenGL の ``glGenBuffers`` の代わりになるようだ。
  同様にメソッド ``gl.createTexture`` が OpenGL の ``glGenTextures`` の代わりになる。
  WebGL にはこの種のメソッドがあと二つある。
* ``gl.uniformMatrix[234]fv`` の第二引数は ``false`` でなければならない。
* 例えば ``gl.VertexAttribPointer`` の引数 ``normalize`` の型が ``GLboolean``
  ではなく JavaScript の基本型の ``Boolean`` であることに注意。これはハマった。

キャンバス
----------------------------------------------------------------------

* HTML の ``canvas`` タグの使い方を習得する。レンダリングコンテキストオブジェクトをここから得る。

  * ``canvas.getContext('webgl')`` でそれを得る。そのオブジェクト名を
    ``gl`` とすること。決め打っていい。
  * ``gl.canvas`` でキャンバスを参照する。

* 例えば射影行列など、実際の描画領域としてキャンバスのアスペクト比を考慮するならば、
  ``clientWidth``, ``clientHeight`` を採用する。

  * 一般に、キャンバスの寸法としてこれらのプロパティーを使うのが原則だ。

* キャンバスのサイズは二種類あって、ピクセル単位のものと表示単位のものがある。

  * ``canvas`` タグの属性として設定する方法。
  * それに加えて CSS から `width` と `height` が設定されている場合、
    WebGL の描画バッファーのサイズはタグ属性のほうを採る。
  * タグ要素 `clientWidth`, `clientHeight` は CSS ピクセル単位。
    手動で `canvas.width` などに代入する。

* リサイズしたら ``gl.viewport`` が基本的だ。
* ブラウザーにはズーム機能があるので ``window.devicePixelRatio`` のような情報を利用する。
  やみくもに ``devicePixelRatio`` を使用すると、パフォーマンスが著しく低下する。
* ``getBoundingClientRect()`` も ``clientWidth`` などの寸法を返すが、整数とは限らない。
* ``ResizeObserver`` で ``content-box`` か ``device-pixel-content-box`` の変化の通知を受け取るようにする。
* CSS の ``box-sizing: border-box`` を理解すると何かとよい。

アニメーション
----------------------------------------------------------------------

WebGL に限った話ではないが：

* JavaScript の関数 ``requestAnimationFrame`` の使い方を間違いなく習得すること。
* アニメーションをフレームレートに依存しないようにすること。前回描画時刻と現在との差分を利用する。

イベント処理
----------------------------------------------------------------------

* キャンバスでキーボードイベントを扱う場合には ``tabindex`` 属性の値を HTML で設定する。

  * さらに、キャンバスがフォーカスされているときに枠が付かないように
    ``outline: none`` を CSS で設定するのが自然だ。

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

ベクトル・行列・アフィン変換
----------------------------------------------------------------------

* ベクトルや行列を仮引数にとる関数を自作する場合、成分の個数に気を配ること。
  ダサいのを覚悟で、成分数を決め打ちしたコードを定義するのが無難だ。

  ベクトルの単位化を計算するコードを書いたときに、格好つけて
  ``Array.reduce`` で書いたら ``w`` 成分の存在を忘れていてみっともないことになった。
* 数学の表記とコード上の見かけは行と列が入れ替わっている。
  行列を一重配列で表現するとき、数学で言う列ベクトルを配列することになる。
  列ベクトルの成分を横に並べて、列ベクトルを縦に並べるからそうなる。

  これを頭の片隅に入れておけば混乱しない：

  .. code:: c++

     // c++
     struct Mat4x4 {
         Vec4 column[4];
     }

* 上述の glMatrix のサイトから ``gl-matrix-min.js``
  を入手しておくとよい。適当に unminify して ``s/var/let/g``
  するとさらに良い。

  * ``mat4.create()`` で行列オブジェクトを生成するらしい。この戻り値に対して
    ``perspective``, ``translate`` などのメソッドを呼び出して成分を決める。

テクスチャー・画像・ビデオ
----------------------------------------------------------------------

* 画像ファイルからテクスチャーを生成するのに JavaScript のクラス
  ``Image`` を活用することをよく理解すること。特に ``onload``
  で非同期的に ``gl.texImage2D`` を呼び出せるのがたいへん具合が良い。

  * このような動的にファイルをロードするコードがある場合、
    ``file://`` から始まるパスで HTML をブラウザーで開くと上手くいかない。
    作業ディレクトリーから HTTP サーバーを起動するのが普通だ。

* HTML キャンバスで ``context.getImageData`` がセキュリティーエラーを出すことがある。
  画像のソースがよそのドメインからだとこうなる。

  * WebGL は同じドメイン以外の画像を禁止している。
  * ``Image.crossOrigin`` の値をどう設定するかが重要だ。
    イメージソースと自分のサイトのドメインが一致していなければ、この値をとりあえず空文字列にする。
    それから `.url` に所望のアドレスを代入すると、先方ドメインが寛容ならば画像が得られる。

* ビデオをテクスチャーに設定することが比較的容易に実現できる。

  * ``documentCreate`` で ``video`` タグを生成し、
    ``onplaying`` と ``ontimeupdate`` イベントハンドラーを実装する手法がある。

* サポートされているテクスチャーユニットの数をシェーダーごとにあらかじめ確認しておくといい。

  .. code:: javascript

     gl.getParameter(gl.MAX_TEXTURE_IMAGE_UNITS);
     gl.getParameter(gl.MAX_VERTEX_TEXTURE_IMAGE_UNITS);

* DirectX 由来のデータ形式はテクスチャー座標が垂直軸方向に反転していると思っていい。

  * ``gl.pixelStorei(gl.UNPACK_FLIP_Y_WEBGL, true)``
  * 圧縮テクスチャーから ``gl.compressedTexImage2D`` で座標データを展開するときには、
    手動で座標成分を ``t = 1 - t`` するのが無難だ。

テキスト
----------------------------------------------------------------------

* キャンバスの上に HTML の何らかの要素を CSS の能力でオーバーレイすればとりあえずはテキストを描ける。
* やりたいことが 3D シーン内にある何かに対して相対的な位置にテキストを描くことならば、
  射影計算を JavaScript 内でやることになる。
* キャンバスの ``getContext("2d")`` によるテキスト描画でもいい。
* DOM ではなくこれを使う利点は、テキスト以外にも描画できるものがあるということだ。
* テキストの描かれたテクスチャーを作成する方法も当然考えられる。
  そして、それを動的に生成する方法もあり得る。
* 背景色を消すために OpenGL のブレンド機能を有効にする。
* WebGL に限らないが、動的に内容が変化するテキストを描画することは、コストがかかる。

透過処理・アルファーブレンディング
----------------------------------------------------------------------

特に C で書かれたチュートリアルを WebGL に移植するときに問題になるのがアルファーの扱いだ。
ベタ移植して出力イメージが何かおかしいときにはアルファーの扱いの違いが原因になっていることがある。
次のようにしてもう一度実行して画像をチェックしろ：

.. code:: javascript

  const gl = canvas.getContext('webgl2', {alpha: false});

データフォーマット
----------------------------------------------------------------------

* Blender OBJ フォーマットのローダーはインターネットに転がっているので、そのまま拝借する。
  自作してもいいが、それにより得られる経験値は多くはない。
  あるものを利用するほうがいい。
* DDS のローダーを書くのはそこまで難しくはない。<https://gist.github.com/showa-yojyo/a21b1feb0dca84bcc61fe50c4c00c714>

関連ノート
======================================================================

* :doc:`/haverbeke18/index`: 三周くらい読めば JavaScript プログラミングは大丈夫。
* :doc:`/khronos15/index`: これを省略して 2.0 だけを読むべきだった。
* :doc:`/khronos18/index`: シェーディングコードで何をするのが良しとされるのかを理解したい。
* :doc:`/angel05/index`: 古い OpenGL の概念がどれくらい生き残っているのかを確かめられる。
