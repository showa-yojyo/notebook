======================================================================
Binary data, files
======================================================================

.. contents::
   :depth: 2

JavaScript でバイナリーデータやバイナリーファイルを扱う方法を学習する。

``ArrayBuffer``, binary arrays
======================================================================

https://javascript.info/arraybuffer-binary-arrays の学習ノート。

Web 開発では、バイナリーデータに出会うのはファイル（作成、アップロード、ダウン
ロード）を扱う際がほとんどだ。画像処理もそうだ。これらはすべて JavaScript で可能
であり、バイナリー演算は高性能だ。そのためのクラスがたくさんある。いくつか挙げる
と：

* ``ArrayBuffer``
* ``Uint8Array``
* ``DataView``
* ``Blob``
* ``File``

JavaScript のバイナリーデータは、他の言語の標準的な実装とは異なる。

基本的なバイナリーオブジェクトは ``ArrayBuffer`` で、固定長の連続したメモリー領
域への参照だ。次のコードで 16 バイトの連続したメモリー領域を確保し、ゼロで埋めて
おく：

.. code:: javascript

   let buffer = new ArrayBuffer(16);

----

``ArrayBuffer`` は何かの配列ではない。``Array`` と共通点がないのだ：

* 長さは固定で、増やしたり減らしたりしない。
* メモリーにちょうどの容量が必要だ。
* 個々のバイトにアクセスするには、``buffer[index]`` のようにするのではなく、別に
  ビューオブジェクトが必要だ。

----

ビューオブジェクトは、それ自体には何も保存しない。
``ArrayBuffer`` に格納されたバイトに解釈を与えるのは、次のクラスだ：

* ``Uint8Array``: ``ArrayBuffer`` の各バイトを個別の数値として扱い、0 から 255
  までの値を指定できる。このような値を 8 ビット符号なし整数と呼ぶ。
* ``Uint16Array``: 2 バイトごとに整数として扱い、0 から 65535 までの値をとれる。
  16 ビット符号なし整数。
* ``Uint32Array``: 4 バイトごとに整数として扱い、0 から 4294967295 までの値をと
  れる。32 ビット符号なし整数。
* ``Float64Array``: 8 バイトごとに、:math:`{5.0 \times 10^{-324}}` から
  :math:`{1.8 \times 10^{308}}` までの浮動小数点数として扱う。

したがって、16 バイトの ``ArrayBuffer`` バイナリーデータを、

* 16 個の「小さな数」、
* 8 個の大きな数（各 2 バイト）、
* 4 個のさらに大きな数（各 4 バイト）、
* 2 個の高精度浮動小数点値（各 8 バイト）

のいずれにも解釈することができる。

``ArrayBuffer`` は中核となるオブジェクトであり、すべての根源であり、生のバイナ
リーデータだ。この中に書き込んだり、反復したり、基本的に操作のほとんどすべてを行
う場合は、ビューを用いる必要がある。

.. admonition:: 学習者ノート

   このコード例からわかるように、上記のビュークラスを ``ArrayBuffer`` オブジェ
   クトから生成して、そのビューのメソッドを呼び出す形で元のバイナリーデータを参
   照したり操作したりするのが基本だ。

``TypedArray``
----------------------------------------------------------------------

これらのビューの共通項は ``TypedArray`` だ。これらは同じメソッドとプロパティーの
集合を共有する。

``TypedArray`` と呼ばれるコンストラクターがあるわけではなく、``Int8Array`` や
``Uint8Array`` などの ``ArrayBuffer`` 上のビューを表す共通の呼び名のようなものだ
と捉えられる。以下、例えば ``new TypedArray`` のようなコードは ``new Int8Array``
や ``new Uint8Array`` などのいずれかを意味するものとする。

型付き配列は通常の配列のように振る舞う。インデックスを持ち、反復可能だ。型付き配
列のコンストラクターは引数の型によって異なる挙動を呈する。

本書ではオーバーロードのようなものが五つあると言っている：

.. code:: javascript

   new TypedArray(buffer, [byteOffset], [length]);
   new TypedArray(object);
   new TypedArray(typedArray);
   new TypedArray(length);
   new TypedArray();

1. すでに見たように、``ArrayBuffer`` オブジェクト ``buffer`` が与えられると、そ
   の上にビューが生成される。オプションで、開始する ``byteOffset`` と ``length``
   を指定すると、ビューはバッファーの一部だけを扱う。
2. ``Array`` あるいは配列風オブジェクト ``object`` が与えられると、それと同じ長
   さの型付き配列を生成し、オブジェクトの内容をそこへコピーする。これを利用し
   て、最初からデータを入れておくことができる。
3. もし、別の ``TypedArray`` ``typedArray`` が与えられると、同じように、それと同
   じ長さの型付き配列を作成し、値をコピーする。必要に応じて、値は新しい型に変換
   される。
4. 数値引数 ``length`` から生成する場合、その要素数を含む型付き配列を生成する。
   そのバイト長は長さに要素一つあたりのバイト数 ``TypedArray.BYTES_PER_ELEMENT``
   を乗じた値に等しい。
5. デフォルトコンストラクターは長さゼロの型付き配列を生成する。

``ArrayBuffer`` に言及することなく、直接 ``TypedArray`` を生成しても、ビューは基
礎となる ``ArrayBuffer`` がないことには存在できないため、自動的に生成される。

基礎となる ``ArrayBuffer`` に参照するために、``TypedArray`` には次のプロパティー
がある：

* ``buffer``: ``ArrayBuffer`` を参照する。
* ``byteLength``: ``ArrayBuffer`` の長さ。

したがって、元のバッファーを共有させながら、一つのビューから別のビューに移動する
ことができる。

.. code:: javascript

   let arr8 = new Uint8Array([0, 1, 2, 3]);
   // another view on the same data
   let arr16 = new Uint16Array(arr8.buffer);

ビュー一覧割愛。

----

``Int8Array`` のような名前のビューがあるにもかかわらず、JavaScript には int や
int8 のような単一値型はない。``Int8Array`` とは、これらの個々の値の配列ではな
く、``ArrayBuffer`` のビューであるため、これは理にかなっている。

Out-of-bounds behavior
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

型付き配列に境界外の値を書き込もうとすると、エラーにはならないものの余分なビット
が切り捨てられる。例えば、``Uint8Array`` に 256 を書き込もうとする。二進数では
256 は b100000000 だ。``Uint8Array`` は値一つにつき 8 ビットしか用意していない
ので、利用できる範囲は 0 から 255 までだ。

大きな数値の場合は、右端の（桁の小さい方の）8 ビットだけが格納され、残りは切り捨
てられる。すなわち、256 の場合には 0 になる。257 の場合には 1 になる。言い換える
と、mod 256 で保存される。

``Uint8ClampedArray`` はこの点で特殊で、この動作が異なる。255 より大きい数には
255 を、負の数には 0 を保存する。画像処理に用いると便利だ。

``TypedArray`` methods
----------------------------------------------------------------------

``TypedArray`` は通常の ``Array`` のメソッドがあるが、特筆すべき例外がある。

反復処理、``map``, ``slice``, ``find``, ``reduce`` などはできる。しかし、できな
いこともある。

* メソッド ``splice``: なぜなら、型付き配列はバッファー上のビューであり、バッ
  ファーとは固定かつ連続したメモリー領域だからだ。
* メソッド ``concat``

追加的に、メソッドが二つある：

* ``arr.set(fromArr, [offset])``: ``fromArr`` から ``arr`` にすべての要素をコ
  ピーし、位置は ``offset`` から始まる。
* ``arr.subarray([begin, end])``: ``begin`` から ``end`` まで同じ型の新しい
  ビューを生成する。これはメソッド ``slice`` に似ているが、何もコピーせず、ただ
  新しいビューを生成して、与えられたデータ片を操作するだけだ。

これらのメソッドにより、型付き配列のコピーや混合、既存の配列からの新しい配列の生
成などができる。

``DataView``
----------------------------------------------------------------------

``DataView`` は ``ArrayBuffer`` の上にある特殊で柔軟な「型なし」ビューだ。これに
より、任意のオフセットのデータに任意のフォーマットでアクセスできる。

* 型付き配列の場合、コンストラクターでフォーマットを指定する。配列全体は一様であ
  るものとする。``arr[i]`` で i 番目の数を表す。
* 一方、``DataView`` では、``getUint8(i)`` や ``getUint16(i)`` のようなメソッド
  でデータを参照する。フォーマットはコンストラクターの実行時ではなく、メソッド呼
  び出し時に選択する。

.. code:: javascript

   new DataView(buffer, [byteOffset], [byteLength]);

* ``buffer``: 基礎となる ``ArrayBuffer`` オブジェクト。型付き配列とは異なり、
  ``DataView`` は自分自身でバッファーを生成しない。利用者が用意する必要がある。
* ``byteOffset``: ビューの開始バイト位置。
* ``byteLength``: ビューのバイト長。

``DataView`` は、さまざまな形式のデータを同じバッファーに格納する場合に便利だ。
例えば、16 ビット整数と 32 ビット浮動小数点数のペアの連なりを格納する場合、
``DataView`` を使えばアクセスが容易だ。

Tasks
----------------------------------------------------------------------

Concatenate typed arrays
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``Uint8Array`` オブジェクトからなる配列が与えられたとき、それらを一つの配列に連
結して返す関数 ``concat(arrays)`` を書け。

.. admonition:: 学習者ノート

   テストコードを見れば題意は理解できる。まずは適切な長さの ``Uint8Array`` オブ
   ジェクトを生成して、元の要素をコピーしていけば動く関数はできる。実行時効率を
   考えて、適切なメソッドを採用するのに神経を使え。

   ``TypedArray`` を使う問題では、言われていなくても実行時効率を要求されていると
   想定するのが普通だ。そうでなければ、こんな型は使わないのだから。

TextDecoder and TextEncoder
======================================================================

<https://javascript.info/text-decoder> の学習ノート。

バイナリーデータが実際には文字列である場合はどうだろう。例えば、テキストデータを
含むファイルを受け取った。組み込み ``TextDecoder`` オブジェクトを使えば、与えら
れたバッファーと符号方式に対して、その値を実際の JavaScript 文字列に読み込むこと
ができる。

その処理をするために、次のオブジェクトをまず生成する：

.. code:: javascript

   let decoder = new TextDecoder([label], [options]);

* ``label``: 既定値は ``utf-8`` だが、``big5``, ``windows-1251``, その他多くの符
  号方式が対応済みだ。
* ``options``

  * ``fatal: true/false``: もし ``true`` ならば、復号できない文字の場合に例外を
    発生させる。そうでなければ文字 ``\uFFFD`` に置換する。
  * ``ignoreBOM: true/false``: BOM を無視するかどうか。ほとんど必要ない。

それからメソッドを呼び出すことで文字列を得る：

.. code:: javascript

   let str = decoder.decode([input], [options]);

* ``input``: 復号するべき ``BufferSource`` オブジェクト。
* ``options``

  * ``stream: true/false``: ストリームを復号するときに、デコーダーが繰り返し呼び
    出され、データの塊を受信するときに ``true`` とする。この場合、マルチバイト文
    字が塊の間で分割されることがある。このオプションは ``TextDecoder`` に「未完
    成の」文字を記憶させ、次の塊が来たときに復号するように指示する。

例を見ると、``input`` には ``TypedArray`` オブジェクトを渡している。

``TextEncoder``
----------------------------------------------------------------------

``TextEncoder`` はその逆で、文字列をバイト列に変換する。

.. code:: javascript

   let encoder = new TextEncoder();

符号化形式は UTF-8 しか対応しない。

メソッドは二つある：

* ``encode(str)``: 文字列 ``str`` から変換されて得られる ``Uint8Array`` を返す。
* ``encodeInto(str, destination)``: 文字列 ``str`` を ``Uint8Array`` であるべき
   ``destination`` に符号化する。

.. admonition:: 学習者ノート

   UTF-8 しか対応していないので、``Uint8Array`` でアクセスするべきバイト列が生じ
   る。

``Blob``
======================================================================

<https://javascript.info/blob> の学習ノート。

``ArrayBuffer`` と ``TypedArray`` 各種は ECMA 標準規格の一部であり、同時に
JavaScript の一部でもある。ブラウザーには高水準のオブジェクトがさらにあり、とり
わけ ``Blob`` がある。

``Blob`` はオプションの文字列 ``type`` （通常は MIME-type）と ``blobParts``
（他の ``Blob`` オブジェクト、文字列、``BufferSource`` の連なり）で構成されてい
る。

.. admonition:: 学習者ノート

   本書の模式図を頭に叩き込んでおくといい。

.. code:: javascript

   new Blob(blobParts, options);

* ``blobParts``: ``Blob``/``BufferSource``/``String`` の配列。
* ``options``

  * ``type``: Blob の種類を表す文字列値。例えば "image/png" のような MIME-type
    であることが普通だ。
  * ``endings``: ``Blob`` を現在の OS の EOL に対応させるために、行末を変換する
    かどうか。既定値は "transparent" だが、"native" にすることもできる。前者は何
    もせず、後者は OS 固有の EOL に変換する。

``Blob`` オブジェクトから部分を取り出すにはメソッド ``slice()`` を用いる。引数は
``array.slice()`` と同様で、負の数も許される。

.. code:: javascript

   blob.slice([byteStart], [byteEnd], [contentType]);

* ``byteStart``: 開始バイト位置
* ``byteEnd``: 終了バイト位置（の一つ次）
* ``contentType``: 得られる部分の型。既定値は ``blob`` と同じ。

----

``Blob`` 内のデータを直接変更することはできない。しかし、``Blob`` の一部を
``slice`` し、そこから新しい ``Blob`` オブジェクトを生成し、それらを新しい
``Blob`` に混ぜるなどすることは可能だ。

この動作は JavaScript の文字列に似ている。文字列の中の文字を変更することはできな
いが、新たに修正した文字列を作ることはできる。

JavaScript では、こういうオブジェクトの性質を「オブジェクトが immutable である」
という。

``Blob`` as URL
----------------------------------------------------------------------

``Blob`` は、``<a>``, ``<img>`` などのタグの URL として簡単に使用でき、その中身
を表示することができる。

プロパティー ``type`` のおかげで、``Blob`` オブジェクトをダウンロード・アップ
ロードすることもでき、その値はネットワーク要求で Content-Type に自然になる。

リンクをクリックすると、hello world の中身を含む動的に生成された ``Blob`` がファ
イルとしてダウンロードされる例：

.. code:: html

   <!-- download attribute forces the browser to download instead of navigating -->
   <a download="hello.txt" href='#' id="link">Download</a>

   <script>
   let blob = new Blob(["Hello, world!"], {type: 'text/plain'});

   link.href = URL.createObjectURL(blob);
   </script>

また、JavaScript でリンクを動的に作成し、``link.click()`` でクリックを模倣する
と、ダウンロードが自動的に開始する。 HTML を一切使用せずに、動的に生成された
``Blob`` をダウンロードさせる類似のコード：

.. code:: javascript

   let link = document.createElement('a');
   link.download = 'hello.txt';

   let blob = new Blob(['Hello, world!'], {type: 'text/plain'});

   link.href = URL.createObjectURL(blob);

   link.click();

   URL.revokeObjectURL(link.href);

``URL.createObjectURL()`` は ``Blob`` を受け取り、``blob:<origin>/<uuid>`` とい
う形式から``Blob`` に対応する一意の URL を生成する。

``link.href`` の値はこのようなものだ：

.. code:: text

   blob:https://javascript.info/1e67e00e-860d-40a5-89ae-6ab0cbee6273

``URL.createObjectURL()`` が生成した URL それぞれに対して、ブラウザーは
URL から ``Blob`` への写像を内部に保存する。そのため、そのような URL は短いが、
``Blob`` にアクセスできます。

生成された URL（およびそれを含むリンク）は、現在のドキュメントが開いている間のみ
有効だ。また、``<img>``, ``<a>`` など、URL を基本的には必要とするあらゆるオブ
ジェクトで ``Blob`` を参照できる。

しかし、副作用がある。``Blob`` の写像がある一方で、``Blob`` 自体はメモリーに常駐
する。ブラウザーはこれを解放できない。

写像はドキュメントのアンロード時に自動的に消去されるため、``Blob`` オブジェクト
はそのときに解放される。しかし、ページの寿命が長い場合、解法はすぐには起こらな
い。

そのため、URL を作成すると、その ``Blob`` は不要になったとしても、メモリーに格納
され続ける。

``URL.revokeObjectURL(url)`` は内部写像から参照を削除し、``Blob`` を削除して（他
に参照がない場合）、メモリーを解放することができる。

最後の例では、``Blob`` を一度だけ使用してすぐにダウンロードすることを意図してい
るため、``URL.revokeObjectURL(link.href)`` をすぐに呼び出している。

クリック可能な HTML リンクを使用する前の例では、
``URL.revokeObjectURL(link.href)`` を呼び出すことはしないが、これは ``Blob`` の
URL が無効になるからだ。失効後、写像が削除されると、URL は機能しなくなる。

``Blob`` to base64
----------------------------------------------------------------------

``URL.createObjectURL()`` の代わりに、``Blob`` を base64 符号文字列に変換するこ
ともできる。この文字符号形式は、バイナリーデータを 0 から 64 までの ASCII コード
を使った超安全な「読み取り可能」文字列として表す。さらに重要なのは、この符号化形
式をデータ URL で使用できることだ。

データ URL は次のような形式をとる。

.. code:: text

   data:[<mediatype>][;base64],<data>

このような URL は通常の URL と同じように、どこでも使用できる。

.. code:: html

   <img src="data:image/png;base64,R0lGODlhDAAMAKIFAF5LAP/zxAAAANyuAP/gaP///wAAAAAAACH5BAEAAAUALAAAAAAMAAwAAAMlWLPcGjDKFYi9lxKBOaGcF35DhWHamZUW0K4mAbiwWtuf0uxFAgA7">

.. figure:: data:image/png;base64,R0lGODlhDAAMAKIFAF5LAP/zxAAAANyuAP/gaP///wAAAAAAACH5BAEAAAUALAAAAAAMAAwAAAMlWLPcGjDKFYi9lxKBOaGcF35DhWHamZUW0K4mAbiwWtuf0uxFAgA7
   :alt: Smiley

   Smiley

ブラウザーはこの文字列を復号し、画像を描画する。``Blob`` を base64 に変換するた
めに、組み込み ``FileReader`` オブジェクトを用いる。これは、複数の形式の
``Blob`` からデータを読み取ることができる。

本書のデモでは ``Blob`` を base64 でダウンロードする。要点をかいつまむと、

* ``A`` タグを動的に生成し、属性 ``download`` にファイルパスを指定する。
* ``Blob`` オブジェクトを生成する。引数は文字列配列と text/plain を指定するオプ
  ション。
* ``FileReader`` オブジェクトを生成する。
* メソッド ``readAsDataURL()`` を呼び出し、引数に ``Blob`` オブジェクトを渡す。
* イベントハンドラー ``onload`` を次のように実装する：先のリンクの属性 ``href``
  に ``FileReader`` の結果を代入し、``click()`` を発動する。

``Blob`` の URL を作成する方法はどちらも使用可能だ。通常は
``URL.createObjectURL(blob)`` の方がより単純かつ高速だ。

``URL.createObjectURL(blob)`` を用いる方法：

* メモリーを大切にするならば、それを消去する必要がある。
* ``Blob`` へは直接アクセスする。符号処理をしない。

``Blob`` をデータ URL に変換する方法：

* 何も無効化する必要なない。
* 符号化処理に、大きな ``Blob`` オブジェクト性能、メモリー損失を生じる。

Image to blob
----------------------------------------------------------------------

画像や画像部分の ``Blob`` を作成したり、ページのスクリーンショットを撮ることもで
きる。これはどこかにアップロードするのに便利だ。

画像の操作は ``<canvas>`` 要素で行う。

1. ``canvas.drawImage()`` を使って画像をキャンバスに描画する。
2. ``Blob`` を生成し、終了時にコールバックを実行するメソッド
   ``canvas.toBlob(callback, format, quality)`` を呼び出す。

本書の例では画像をコピーしている。
``blob`` を作る前に画像から切り取り、またはキャンバス上で変形することが可能だ。

.. admonition:: 学習者ノート

   ここでは ``getContext('2d')`` しているのでこういう処理になっているが、
   ``getContext('webgl2')`` で WebGL 描画をしたものをコピーするようなこともでき
   るだろう。

コールバックではなく、非同期呼び出しも対応している：

.. code:: javascript

   let blob = await new Promise(resolve => canvasElem.toBlob(resolve, 'image/png'));

ページのスクリーンショットを行うにはライブラリーを利用するのが普通らしい。そのよ
うなライブラリーは、ページをスキャンしてキャンバスに描画する。そして、上記と同じ
方法でその ``Blob`` を得る、といった具合だ。

From ``Blob`` to ``ArrayBuffer``
----------------------------------------------------------------------

``Blob`` コンストラクターで ``BufferSource`` を含むほとんどすべてのものからオブ
ジェクトを生成できる。低水準処理を行う必要があるならば、非同期メソッド
``blob.arrayBuffer()`` で最低水準の ``ArrayBuffer`` を得られる。

From ``Blob`` to stream
----------------------------------------------------------------------

2GB を超える ``Blob`` を読み書きする場合、``arrayBuffer()`` を使用するとより多く
のメモリーを消費するようになる。この場合、``blob`` をストリームに直接変換するこ
とができる。

ストリームとは、部分ごとに読み取むか、または書き込むことができる特別なオブジェク
トだ。断片的な処理に適したデータに対して便利だ。

``Blob`` のメソッド ``stream()`` は ``ReadableStream`` を返し、これを読み込むと
``Blob`` に含まれるデータが返される。

.. code:: javascript

   // get readableStream from blob
   const readableStream = blob.stream();
   const stream = readableStream.getReader();

   while (true) {
       // for each iteration: value is the next blob fragment
       let { done, value } = await stream.read();
       if (done) {
           // no more data in the stream
           break;
       }

       // do something with the data portion we've just read from the blob
   }

.. admonition:: 学習者ノート

   おそらくこのループはもっと現代的な書き方がある。

File and FileReader
======================================================================

<https://javascript.info/file> の学習ノート。

``File`` オブジェクトは ``Blob`` を継承し、ファイルシステム関連の機能を拡張した
ものだ。まず、コンストラクターだ：

.. code:: javascript

   new File(fileParts, fileName, [options])

* ``fileParts``: ``Blob``/``BufferSource``/``String`` 値の配列。
* ``fileName``: ファイル名である文字列。
* ``options``

  * ``lastModified``: 最終更新のタイムスタンプ値。整数。

次に、``<input type="file">`` やドラッグ＆ドロップなど、ブラウザーのインター
フェースからファイルを取得する場合、ファイルは OS からこの情報を取得する。

``File`` には ``Blob`` と同じプロパティーがある。それ以外にもある：

* ``name``: ファイル名、
* ``lastModified``: 最終更新のタイムスタンプ。

``<input type="file">`` から ``File`` オブジェクトを取得する方法：

.. code:: html

   <input type="file" onchange="showFile(this)">

   <script>
   function showFile(input) {
       let file = input.files[0];

       alert(`File name: ${file.name}`); // e.g my.png
       alert(`Last modified: ${file.lastModified}`); // e.g 1552830408824
   }
   </script>

``<input>`` は複数のファイルを選択することができるので、``input.files`` はそれら
のファイルを含む配列風オブジェクトだ。

``FileReader``
----------------------------------------------------------------------

``FileReader`` は ``Blob`` オブジェクトからデータを読み取ることだけを目的とした
オブジェクトだ。ディスクからの読み込みに時間がかかることがあるため、イベントを使
用してデータを届ける。

.. code:: javascript

   let reader = new FileReader(); // no arguments

主要メソッド：

* ``readAsArrayBuffer(blob)``: バイナリー形式 ``ArrayBuffer`` にデータを読み込
  む。
* ``readAsText(blob, [encoding])``: 与えられた符号形式でテキスト文字列としてデー
  タを読み込む。
* ``readAsDataURL(blob)``: バイナリデータを読み取り、base64 データ URL として符
  号化する。
* ``abort()``: 操作をキャンセルする。

これらの ``read*()`` メソッドの選択は、どの形式を好むか、データをどのように使う
かによる。

* ``readAsArrayBuffer``: バイナリーファイル用で、低水準操作を実行する。スライス
  操作のような高水準操作については、``File`` は ``Blob`` であるので、読み込まず
  に直接呼び出せる。
* ``readAsText``: テキストファイルに対して、文字列を取得したい場合。
* ``readAsDataURL``: ``img`` または他のタグの ``src`` でこのデータを使用する場
  合。ファイルを ``URL.createObjectURL(file)`` で読み込むという方法もある。

読み込みが進むとイベントが起こる。最も広く使われているのは ``load`` と ``error``
だ。

* ``loadstart``: 読み込み開始
* ``progress``: 読み込み中
* ``load``: エラーなしで読み込み完了
* ``abort``: ``abort()`` 呼び出し発生
* ``error``: エラー発生
* ``loadend``: 読み込み終了（成功でも失敗でも）

読み取りが終了したら、その結果を参照できる：

* ``reader.result``
* ``reader.error``

本書のコード例をよく見ておく。

----

``FileReader`` は ``File`` というより ``Blob`` を読み込む機能なので、これを利用
して、``Blob`` オブジェクトを別の形式に変換できる。

* ``readAsArrayBuffer``: ``ArrayBuffer``
* ``readAsText``: 文字列
* ``readAsDataURL``: base64 データ URL

----

Web Workers には、``FileReaderSync`` と呼ばれる ``FileReader`` の同期型も存在す
る。その読み込みメソッド ``read*()`` はイベントを生成せず、通常の関数と同じよう
に結果を返す。なぜなら、Web Workers では、ファイルからの読み取り中に発生する同期
呼び出しの遅延がほとんど重要ではないからだ。ページには影響しない。
