======================================================================
Drawing on Canvas
======================================================================

`Eloquent JavaScript <https://eloquentjavascript.net/>`__ Chapter 17 の読書ノート。

ブラウザーでグラフィックスを扱う方法はいくつかある。一つは SVG であり、もう一つ
はキャンバスだ。前者はベクトルデータ、後者はラスターデータという際立った違いがあ
る。

.. contents:: ノート目次

SVG
======================================================================

本書では SVG を細かく述べることはしない。

これは単純な SVG 画像のある HTML 文書だ：

.. code:: html

   <p>Normal HTML here.</p>
   <svg xmlns="http://www.w3.org/2000/svg">
     <circle r="50" cx="50" cy="50" fill="red"/>
     <rect x="120" y="5" width="90" height="90" stroke="blue" fill="none"/>
   </svg>

* 属性 ``xmlns`` は要素を異なる XML 名前空間に変える。URL により識別されるこの名
  前空間は、現在使っている方言を指定する。
* HTML には存在しない ``<circle>`` や ``<rect>`` タグは SVG においては意味があ
  る。属性が指定するスタイルと位置を使って図形を描画する。
* これらのタグは DOM 要素を生成する。HTML タグと同様に JavaScript から操作でき
  る。例えば次のようなコードは有効だ：

  .. code:: javascript

     let circle = document.querySelector("circle");
     circle.setAttribute("fill", "cyan");

.. admonition:: 読者ノート

   Google Chrome などの開発ツールを使えば上記のコード片を簡単に試せる。

The canvas element
======================================================================

* キャンバスグラフィックは ``<canvas>`` 要素に描画できる。このような要素に属性
  ``width`` と ``height`` をピクセル単位で与えて寸法を決められる。
* 新しいキャンバスは空だ。完全に透明なので、文書内の何もない空間として現れる。
* タグ ``<canvas>`` は色々なスタイルの描画を可能にすることを意図している。現在は
  次の二つの描画スタイルが広くサポートされている：

  * ``"2d"``: 2 次元のグラフィックス
  * ``"webgl"``: OpenGL インターフェイスによる 3 次元のグラフィックス

本書では WebGL については議論するつもりはない。

* ``<canvas>`` DOM 要素のメソッド ``getContext`` を使ってコンテキストを作成する。

.. code:: html

   <p>Before canvas.</p>
   <canvas width="120" height="60"></canvas>
   <p>After canvas.</p>
   <script>
     let canvas = document.querySelector("canvas");
     let context = canvas.getContext("2d");
     context.fillStyle = "red";
     context.fillRect(10, 10, 100, 50);
   </script>

* コードから想像されるような図形が描画される。
* キャンバスの座標系は HTML 同様、左上隅を原点とし、そこから Y 軸が画面下方に向
  かう。

Lines and surfaces
======================================================================

* キャンバスインターフェイスでは図形に対して、その領域に一定の色やパターンを与え
  て塗りつぶしたり、輪郭に沿って線を引いたりすることができる。同じ用語が SVG で
  も使われる。

  * メソッド ``fillRect`` は矩形を塗りつぶす。引数には矩形の左上の座標、矩形の
    幅、高さをとる。
  * メソッド ``strokeRect`` は矩形の輪郭を描く。

* どちらのメソッドもこれ以上の引数は取らない。塗りつぶしの色、線の太さなどはメ
  ソッドの引数ではなく、コンテキストオブジェクトのプロパティーが決定する。

  * プロパティー ``fillStyle`` は図形の塗りつぶし方法を制御する。CSS で使われる
    色記法を用いて色を指定する文字列を値とする。
  * プロパティー ``strokeStyle`` は描線の色を決定する。
  * プロパティー ``lineWidth`` は描線の太さを決定する。任意の正の数を指定でき
    る。

.. code:: javascript

   let cx = document.querySelector("canvas").getContext("2d");
   cx.strokeStyle = "blue";
   cx.strokeRect(5, 5, 50, 50);
   cx.lineWidth = 5;
   cx.strokeRect(135, 5, 50, 50);

* このコードで ``<canvas>`` に ``width`` や ``height`` が指定されていないことに
  注意。既定値が適用される。

Paths
======================================================================

パスとは線分の列だ。2D キャンバスインターフェイスはパスを記述するのに独特のアプ
ローチをとる。これは完全に副作用でなされるものだ。パスは保存したり受け渡したりす
るような値ではない。パスで何かをするときには、その形状を記述するためにメソッドを
いくつか続けて呼び出す。

次の例 (pp. 298-299) は水平な線分を 9 本描くものだ：

.. code:: javascript

   let cx = document.querySelector("canvas").getContext("2d");
   cx.beginPath();
   for (let y = 10; y < 100; y += 10) {
       cx.moveTo(10, y);
       cx.lineTo(90, y);
   }

* コンテキストメソッド ``beginPath`` を呼び出しでパス描画の開始を宣言する？
* メソッド ``lineTo`` で指定終点まで線分を一本描く。
* 先にメソッド ``moveTo`` でその始点を指定する。
* 最後にメソッド ``stroke`` で一気に線を引く。

----

* パスをメソッド ``fill`` で塗りつぶすことができる。各形状が個別に塗りつぶされ
  る。
* パスは複数の形状を含むことができる。メソッド ``moveTo`` を呼び出すと形状が一つ
  始まる。
* パスが閉曲線を構成していることを塗りつぶしの前提としているので、閉じていないパ
  スを塗りつぶすと、パスの端点に線分が補完されたかのようにした形状を塗りつぶす。

  * メソッド ``closePath`` を使って、そのような線分を明示的に追加することもでき
    る。

.. code:: javascript

   let cx = document.querySelector("canvas").getContext("2d");
   cx.beginPath();
   cx.moveTo(50, 10);
   cx.lineTo(10, 70);
   cx.lineTo(90, 70);
   cx.fill();

Curves
======================================================================

パスには真っ直ぐな線分だけではなく、簡単な曲線も含められる。

* メソッド ``quadraticCurveTo`` は指定した点に曲線を描く。

  * さらに、この曲線の曲率を決めるのに目標点と制御点を与える。
  * これが放物線の始点における接線ベクトルを指示すると考える。

.. code:: javascript

   let cx = document.querySelector("canvas").getContext("2d");
   cx.beginPath();
   cx.moveTo(10, 90);
   // control=(60,10) goal=(90,90)
   cx.quadraticCurveTo(60, 10, 90, 90);
   cx.lineTo(60, 10);
   cx.closePath();
   cx.stroke();

----

メソッド ``bezierCurveTo`` もまた曲線を描くものだ。これは始点と終点とそれぞれに
接線を与えるインターフェイスがある（三次曲線なので点が 4 つ要る）。

.. code:: javascript

   let cx = document.querySelector("canvas").getContext("2d");
   cx.beginPath();
   cx.moveTo(10, 90);
   // control1=(10,10) control2=(90,10) goal=(50,90)
   cx.bezierCurveTo(10, 10, 90, 10, 50, 90);
   cx.lineTo(90, 10);
   cx.lineTo(10, 10);
   cx.closePath();
   cx.stroke();

* 二つの制御点は、曲線のそれぞれの端点における接線方向を指定する。
* この曲線は扱いが難しい。

----

メソッド ``arc`` で円弧を描く。次のものを指定する：

* 円の中心
* 半径
* 開始角度
* 終了角度

.. code:: javascript

   let cx = document.querySelector("canvas").getContext("2d");
   cx.beginPath();
   // center=(50,50) radius=40 angle=0 to 7
   cx.arc(50, 50, 40, 0, 7);
   // center=(150,50) radius=40 angle=0 to π½
   cx.arc(150, 50, 40, 0, 0.5 * Math.PI);
   cx.stroke();

* 他のパス描画メソッドと同様に、メソッド ``arc`` が描く曲線は直前のパス断片に接
  続される。これを避けるには

  * メソッド ``moveTo`` を呼び出すか、
  * 新しいパスを開始する。

Drawing a pie chart
======================================================================

次の JSON 風データから円グラフを描くことを考える：

.. code:: javascript

   const results = [
       {name: "Satisfied", count: 1043, color: "lightblue"},
       {name: "Neutral", count: 563, color: "lightgreen"},
       {name: "Unsatisfied", count: 510, color: "pink"},
       {name: "No comment", count: 175, color: "silver"}
   ];

円グラフを構成する扇形の内角を ``count`` の割合に応じて計算するところまで示すと
次のようなコード (p. 303) になる：

.. code:: html

   <canvas width="200" height="200"></canvas>
   <script>
     let cx = document.querySelector("canvas").getContext("2d");
     let total = results.reduce((sum, {count}) => sum + count, 0);
     // Start at the top
     let currentAngle = -0.5 * Math.PI;
     for (let result of results) {
         let sliceAngle = (result.count / total) * 2 * Math.PI;
         cx.beginPath();
         // center=100,100, radius=100
         // from current angle, clockwise by slice's angle
         cx.arc(100, 100, 100, currentAngle, currentAngle + sliceAngle);
         currentAngle += sliceAngle;
         cx.lineTo(100, 100);
         cx.fillStyle = result.color;
         cx.fill();
     }
   </script>

ラベルを付けたいので、次にキャンバスにテキストを追加する。

Text
======================================================================

テキストを描くメソッドには ``fillText`` と ``strokeText`` がある。後者はアウトラ
インしている文字には便利だが、ふつうは ``fillText`` が必要とするものだ。

.. code:: javascript

   let cx = document.querySelector("canvas").getContext("2d");
   cx.font = "28px Georgia";
   cx.fillStyle = "fuchsia";
   cx.fillText("I can draw text, too!", 10, 50);

* プロパティ ``font`` に対してテキストのサイズ、スタイル、フォントを指定する。

  * ``italic`` や ``bold`` を文字列の先頭に追加してもいい。

* メソッド ``fillText``, ``strokeText`` の最後の二つの引数でテキストの描画位置を
  指定する。位置とは、文字のベースラインに相当する。アルファベットの j とか p の
  下の部分が突き出るような線だ。
* プロパティー ``textAlign`` でテキストの水平方向の位置を指定する。値は：

  * ``center``
  * ``end``

* プロパティー ``textBaseline`` でテキストの垂直方向の位置を指定する。値は：

  * ``top``
  * ``middle``
  * ``bottom``

Images
======================================================================

メソッド ``drawImage`` はピクセルデータをキャンバスに描く。

* ピクセルデータは ``<img>`` 要素や他のキャンバスから取得する。

次の例では ``<img>`` 要素を作成して画像ファイルを読み込む。

* ブラウザーがまだ読み込めていない可能性があるのですぐには描き始めない。イベント
  ``load`` のハンドラーを登録して、読み込まれてから描画する。

.. code:: javascript

   let cx = document.querySelector("canvas").getContext("2d");
   let img = document.createElement("img");
   img.src = "img/hat.png";
   img.addEventListener("load", () => {
       for (let x = 10; x < 200; x += 30) {
           cx.drawImage(img, x, 10);
       }
   });

* ``drawImage`` にさらに二つ引数を追加して、元サイズとは異なる幅と高さを指定する
  こともできる。

----

``drawImage`` に引数を 9 個与えると、画像の一部だけを描画することができる。

* 第 2, 3, 4, 5 引数はコピー元画像の矩形範囲を位置と寸法で指定する。
* 第 6, 7, 8, 9 引数はコピー先の矩形範囲を位置と寸法で指定する。

この仕様を利用して、複数のスプライトを単一の画像ファイルにまとめて、スライスして
描画する技法がある。特に、スプライトを順次描画することでアニメーションにするとい
う応用がある。

キャンバスにある絵をアニメーションにするにはメソッド ``clearRect`` が役に立つ。
メソッド ``fillRect`` は色を着けるが、これは透明にして直前に描かれたピクセルを消
去する。

次のコードは画像をロードし、次のフレーム（コマ）を描画するための時間的間隔を仕込
んでそれをする。各スプライトの寸法が 24x30 であることはわかっているとする：

.. code:: javascript

   let cx = document.querySelector("canvas").getContext("2d");
   let img = document.createElement("img");
   img.src = "img/player.png";
   let spriteW = 24, spriteH = 30;
   img.addEventListener("load", () => {
       let cycle = 0;
       setInterval(() => {
           cx.clearRect(0, 0, spriteW, spriteH);
           cx.drawImage(img,
               // source rectangle
               cycle * spriteW, 0, spriteW, spriteH,
               // destination rectangle
               0, 0, spriteW, spriteH);
           cycle = (cycle + 1) % 8;
       }, 120);
   });

* 変数 ``cycle`` はアニメーション内の位置を追跡する。各フレームでこの値をインク
  リメントして、適宜剰余演算子を使って 0 から 7 の範囲に収める。この値は現在のス
  プライトの全画像における x 座標を計算する。

Transformation
======================================================================

* メソッド ``scale`` を呼び出すと、以降の描画に拡縮変換が施される。このメソッド
  は引数を二つとる。それぞれ水平方向と垂直方向の係数だ。

  次のコードは円の幅と逆さをそれぞれ 3 倍、半分にする：

  .. code:: javascript

     let cx = document.querySelector("canvas").getContext("2d");
     cx.scale(3, .5);
     cx.beginPath();
     cx.arc(50, 50, 40, 0, 7);
     cx.lineWidth = 3;
     cx.stroke();

  * 拡縮変換は線幅を含む全ての描画要素に適用される。
  * 符号も考慮される。負の係数は原点に関して反転する。

* 絵の向きを場所を変えずに反転するには ``cx.scale(-1, 1)`` だけでは足りない。反
  転画像がビューポートの外に出るだけになる。

----

* メソッド ``rotate`` で図形を回転させる。
* メソッド ``translate`` で図形を移動させる。
* このような図形変換メソッドは重ねて行われる。それぞれの変換はその直前の変換に対
  して相対的に行われる。例えば、

  * 水平方向に 10 ピクセル移動させるのを二度呼び出すと、20 ピクセル移動させるこ
    とになる。
  * 最初に座標系原点を :math:`(50, 50)` に移動した後、何度か回転させると、その回
    転は :math:`(50, 50)` を中心に回転する。
  * 最初に回転させてから :math:`(50, 50)` だけ移動すると、回転した座標系に対して
    移動が行われる。その結果、異なる向きを生じる。座標変換を適用する順序がだいじ
    だ。

ある垂直軸に沿って絵を反転させるには次のようにする：

.. code:: javascript

   function flipHorizontally(context, around) {
       context.translate(around, 0);
       context.scale(-1, 1);
       context.translate(-around, 0);
   }

これで位置 :math:`(100, 100)` に鏡像を描くことができる。

.. code:: javascript

   let cx = document.querySelector("canvas").getContext("2d");
   let img = document.createElement("img");
   img.src = "img/player.png";
   let spriteW = 24, spriteH = 30;
   img.addEventListener("load", () => {
       flipHorizontally(cx, 100 + spriteW / 2);
       cx.drawImage(img,
           0, 0, spriteW, spriteH,
           100, 0, spriteW, spriteH);
   });

Storing and clearing transformations
======================================================================

* OpenGL の ``glPushMatrix`` や ``glPopMatrix`` のような仕組みが 2D キャンバスに
  もある。

  * メソッド ``save`` と ``restore`` を用いる。やはり座標変換のスタックを操作す
    るようなものだ。
  * メソッド ``resetTransform`` を呼び出すと座標変換を完全にリセットする。

* 本書 p. 309 の関数 ``branch`` は座標変換を変更する関数が何をできるかを示してい
  る。再帰呼び出しを利用して典型的なフラクタルを描画する。

Back to the game
======================================================================

以上で、前章のゲームのためにキャンバスを使った表示システムを構築するのに十分な知
識を得た。新しい表示システムでは、色の着いた箱を見せるだけではなく、ゲーム要素を
表現する画像を``drawImage`` で描く。

* ``CanvasDisplay`` (pp. 310-311) という別の表示オブジェクトを定義し、前章におけ
  る ``DOMDisplay`` と同じインターフェイスを、つまりメソッド ``syncState`` と
  ``clear`` を備えるようにする。
* このオブジェクトは ``DOMDisplay`` よりわずかに多くの情報を保持する。

  * ``DOM`` 要素のスクロール位置を使うのではなく、独自のビューポートを追跡して、
    ステージのどの部分を見ているのかを知らせるようにする。
  * プロパティー ``flipPlayer`` を持たせ、プレイヤーが静止しているときでも、直前
    に動いた方向を向き続けるようにする。

----

メソッド ``syncState`` (p. 311) は、最初に新しいビューポートを計算して、適当な位
置にゲームシーンを描画する。

.. code:: javascript

   CanvasDisplay.prototype.syncState = function(state) {
       this.updateViewport(state);
       this.clearDisplay(state.status);
       this.drawBackground(state.level);
       this.drawActors(state.actors);
   };

* ``DOMDisplay`` とは対照的に、このスタイルでは更新のたびに背景を再描画する必要
  がある。キャンバス上の図形は単なるピクセルであるため、描画後にそれを削除・消去
  する良い方法はない。したがって、キャンバスを更新するただ一つの方法は、表示を消
  去してシーンを再描画することだ。
* スクロールすることもできるが、その場合には背景を別の位置に変える必要がある。

----

メソッド ``updateViewport`` (pp. 311-312) は ``DOMDisplay.scrollPlayerIntoView``
に似ている。プレイヤーが画面の端に近づき過ぎているかをチェックし、その場合には
ビューポートを移動する。

----

表示を消去する (p. 312) ときには、ゲームに勝ったときとそうでないときでは、違う色
を使う。

----

背景を描画 (pp. 312-313) するのに、現在のビューポートで見えているタイルの中か
ら、前章のメソッド ``touches`` と同じ手法で、順番に表示する。

* 空ではないタイルは ``drawImage`` を使って描かれる。

  * 画像 ``otherSprites`` はプレイヤー以外の要素に使われる画像からなる。左から順
    に壁用、溶岩用、コイン用のスプライトだ。
  * ``DOMDisplay`` と同じ尺度を使うつもりなので、背景のタイルは 20x20 ピクセル
    だ。したがって、溶岩タイルのオフセットは 20 であり、壁タイルのそれはゼロだ。

* スプライト画像がロードされるのを待つことを気にする必要はない。まだロードされて
  いない画像で ``drawImage`` を呼び出すことは単に何もしないで終わるだけだ。その
  ため、最初の 2, 3 フレームは、画像のロード中にゲームの描画に失敗するかもしれな
  い。しかし、これは深刻な問題というわけではない。画面を更新し続けているため、
  ロードが完了すると直ちに正しいシーンが現れる。

----

ここでは p. 305 に掲載されている歩くキャラクターをプレイヤーを表現するのに使う。
それを描画するコードは、プレイヤーの現在の動きに従って、正しいスプライトと方向を
決める必要がある。最初の 8 個のスプライトが歩行アニメーションだ。

* プレイヤーが床上を移動してるときには、現在の時刻に基づいてスプライトを循環させ
  る。

  * 60 ミリ秒ごとにフレームを切り替えたいので、コード中に ``/ 60`` の処理があ
    る。
  * プレイヤーが静止するときには 9 番目のスプライトを描く。
  * ジャンプ時には画像のいちばん右にある 10 番目のスプライトを使う。

* スプライト幅はプレイヤーオブジェクトのそれよりもわずかに大きい。これは、足や腕
  のスペースを確保するために 16 ピクセルではなく 24 ピクセルになっているからだ。
  メソッドでは x 座標と幅を量 ``playerXOverlap`` により調整しなければならない。
* メソッド ``drawPlayer`` (pp. 313-314) は、ゲーム内のすべての出演者の描画を担当
  するメソッド ``drawActors`` (pp. 314-315) から呼び出される。

プレイヤー以外のものを描くときには、その種類を見て正しいスプライトのオフセットを
見つける。溶岩タイルはオフセット 20 に、コインスプライトは 40 にそれぞれある。

キャンバスの原点はステージの左上隅ではなく、ビューポートの左上隅に対応するので、
出演者の位置を計算するときには、ビューポートの位置を差し引かなければならない。

* メソッド ``translate`` を使ってもよい。どちらでも動く。

新しい表示システムの説明は以上だ。スクリーンショットが本書 p.315 にある。

Choosing a graphics interface
======================================================================

ブラウザー上でグラフィックスを生成する必要があるときには、素の HTML, SVG, キャン
バスのいずれかを選択することができることを見てきた。どの選択肢にも長所と短所があ
る。

* 素の HTML は単純であることが長所だ。テキストともよく組み込める。SVG もキャンバ
  スもテキストを描くことはできるが、位置を調整することと複数行を折り返すことはで
  きない。HTML ベースの画像では、テキストブロックを含めるのがずっと容易だ。
* SVG はズーム操作に強い。どんな倍率でも見栄えが良い鮮明なグラフィックスを生成す
  る。HTML とは異なり、SVG は描画用途に設計されているため、この目的には適してい
  る。
* SVG も HTML も DOM を構築する。これにより、要素の修正が考えられるようになる。
  ユーザーの行動に応じたり、アニメーションの一部だったりで、大きな絵の小さな部分
  を繰り返し変更するような場合、キャンバスで行うと必要以上に高くつく。

  * DOM では、画像の中のどの要素にもマウスイベントハンドラーを登録することができ
    る。キャンバスではそれができない。

* キャンバスのピクセル指向のアプローチは、膨大な数の微小要素を描くようなときには
  有利だ。データ構造を構築するのではなく、同じピクセル面に繰り返し描画するだけな
  ので、キャンバスでは一図形あたりのコストが安くつく。

  * また、シーンを 1 ピクセルずつレンダリングするような効果や、JavaScript を使っ
    て画像を後処理するなどの、ピクセルベースのアプローチでなければ現実的に処理で
    きない効果もキャンバスにならばある。

場合によっては、これらの手法を組み合わせることもできる。例えば、SVG やキャンバス
でグラフを描き、その絵の上に HTML 要素を配置することでテキストによる情報を見せる
ことができる。

多くを求めないアプリケーションであれば、どのインターフェイスを選ぶかは重要ではな
い。本章でゲーム用に作成した表示システムは、文字の描画やマウス操作の処理や異常に
多い数の要素をさばく必要がないので、これら三つのグラフィックス技術のいずれを用い
ても実装することもできた。

Summary
======================================================================

* 本章ではブラウザーでグラフィックスを描画する技術について議論した。特に
  ``<canvas>`` 要素に焦点を当てた。

  * ``<canvas>`` ノードはプログラムで描画することができる文書内の領域だ。描画は
    メソッド ``getContext`` で生成された描画コンテキストオブジェクトを介してなさ
    れる。

* 2D 描画インターフェイスでは、さまざまな図形を塗りつぶしたり、描いたりすること
  ができる。

  * ``fillStyle``
  * ``lineWidth``
  * 矩形やテキストは一度のメソッド呼び出しで描画できる。

    * ``fillRect``, ``strokeRect``
    * ``fillText``, ``strokeText``

  * 自作図形を作成するにはパスを作図する必要がある。

    * ``beginPath``
    * ``moveTo``, ``lineTo``
    * ``fill``, ``stroke``

  * 画像や他のキャンバスのピクセルをキャンバスに置くには ``drawImage`` を呼ぶ。

    * 引数を追加的に与えることで、画像の特定の部分を扱うことができる。今回のゲー
      ムプログラムではこの機能を使用してスプライトを扱った。

* 2D 描画コンテキストは座標変換をサポートしている。

  * 描画コンテキストには現在の変換情報が保持されている。これをメソッド
    ``translate``, ``scale``, ``rotate`` でさらに変換できる。
  * 座標変換はその後の描画処理すべてに影響する。
  * 座標変換はメソッド ``save`` で保存、``restore`` で復元することができる。

* キャンバスへのアニメーション表示の際、再描画の前にキャンバスの一部を消去するの
  にメソッド ``clearRect`` が使える。

Exercises
======================================================================

Shapes
----------------------------------------------------------------------

**問題** 次の図形をキャンバスに描画するプログラムを書け：

#. 台形
#. 赤いダイヤ（長方形を 45 度回転させたもの）
#. ジグザグの線
#. 100 本の線分で構成された螺旋状の線
#. 黄色い星（本書 p.317 参照）

形ごとに関数を作ることをお勧めする。位置、そして指定必須ではないものとして、サイ
ズや点の個数などのプロパティーを引数として渡せ。そうではないほうの方法は、数字を
ハードコードすることで、コード全体を不必要に難しくしがちだ。コードを読むのも修正
するのも無駄に難しくなる。

**解答** 関数を書くときは引数をどうするかが重要だ。座標変換で済むものは省く方針
で行く。

.. code:: javascript

  function drawTrapezoid(cx, a, b, s){
      cx.beginPath();
      cx.moveTo(0, 0);
      cx.lineTo(a, 0);
      cx.lineTo(a - s, b);
      cx.lineTo(s, b);
      cx.closePath();
      cx.stroke();
  }

赤いダイヤは外接する円の半径を引数としたい。中心は呼び出し元が座標変換を施すこと
で設定される：

.. code:: javascript

   function drawDiamond(cx, radius){
       cx.fillStyle = "red";
       cx.beginPath();
       cx.moveTo(radius, 0);
       cx.lineTo(0, radius);
       cx.lineTo(-radius, 0);
       cx.lineTo(0, -radius);
       cx.closePath();
       cx.fill();
   }

ジグザグは外接する矩形の寸法と間隔を与える。間隔がゼロのときは例外を送出したいが
略。それ以外の幾何的性質は呼び出し元で座標変換を与えることで設定する：

.. code:: javascript

   function drawZigzag(cx, size, pitch){
       const count = size / pitch;
       pitch /= 2;
       cx.beginPath();
       cx.moveTo(0, 0);
       for(let i = 0, j = 0; i < count; i++){
           cx.lineTo(size, j += pitch);
           cx.lineTo(0, j += pitch);
       }
       cx.stroke();
   }

螺旋などのパラメトリック曲線を描くにはそれを近似する折れ線を描くことになる（以
下、三角関数の呼び出しを最適化することはしない）：

.. code:: javascript

   function drawSpiral(cx, size, winding = 5){
       const numLine = 100;
       const maxAngle = Math.PI * 2 * winding;
       const dtheta = maxAngle / numLine;
       cx.beginPath();
       cx.moveTo(0, 0);
       for(let i = 1; i < numLine; ++i){
           const t = dtheta * i;
           const r = size * i / numLine;
           cx.lineTo(r * Math.cos(t), r * Math.sin(t));
       }
       cx.lineTo(size * Math.cos(maxAngle), size * Math.sin(maxAngle));
       cx.stroke();
   }

黄色い星の問題が実はいちばん易しい：

.. code:: javascript

   function drawStar(cx, r = 1, num = 8){
       cx.fillStyle = "yellow";
       cx.beginPath();
       cx.moveTo(0, 0);
       for(let i = 0; i < num; ++i){
           const t = i * Math.PI * 2 / num;
           cx.quadraticCurveTo(0, 0, r * Math.cos(t), r * Math.sin(t));
       }
       cx.quadraticCurveTo(0, 0, r, 0);
       cx.fill();
   }

The pie chart
----------------------------------------------------------------------

**問題** この章では、円グラフを描くプログラムの例を紹介した。これを修正して、各
カテゴリーの名前を、そのカテゴリーを表すスライスの横に表示しろ。他のデータセット
にも適用できるように、このテキストを自動的に配置するための見栄えの良い方法を見つ
けろ。カテゴリーはラベルのための十分なスペースを確保できる大きさであると仮定して
かまわない。

**解答** テキストの配置を見栄え良くするという課題が上手くいかなくて、ここだけヒ
ントを参考にした：

まず ``for`` ループの外側でフォントの静的な性質を設定する：

.. code:: javascript

   cx.font = "16px Georgia";
   cx.textBaseline = "middle";

この ``textBaseline`` の設定は相当手練なフォント使いでないと発想できない。

ループを次のように修正する：

.. code:: javascript

   const centerX = 200, centerY = 150;
   const radius = 100;
   const total = results.reduce((sum, { count }) => sum + count, 0);
   // Start at the top
   let currentAngle = -0.5 * Math.PI;
   for (const result of results) {
       const sliceAngle = (result.count / total) * 2 * Math.PI;
       cx.beginPath();
       // center=100,100, radius=100
       // from current angle, clockwise by slice's angle
       cx.arc(centerX, centerY, radius, currentAngle, currentAngle + sliceAngle);
       const middleAngle = currentAngle + sliceAngle / 2;
       currentAngle += sliceAngle;
       cx.lineTo(centerX, centerY);
       cx.fillStyle = result.color;
       cx.fill();

       const labelX = radius * Math.cos(middleAngle);
       const labelY = radius * Math.sin(middleAngle);
       cx.fillStyle = "black";
       cx.textAlign = labelX < 0 ? "right" : "left";
       cx.fillText(result.name, centerX + labelX, centerY + labelY);
   }

* キャンバスの寸法は題意に従い HTML 側で十分大きくしておくといい。
* ``middleAngle`` を計算して ``fillText`` に入力するラベル位置を決定することは容
  易に思いつく。
* 急所は ``textAlign`` を円グラフの左右で指定を分けるという点だ。

A bouncing ball
----------------------------------------------------------------------

**問題** 第 14 章と第 16 章で紹介した ``requestAnimationFrame`` の技法を使って、
跳ね返るボールが入った箱を描け。ボールは一定の速さで動き、箱の側面に当たると跳ね
返る。

* 箱は ``strokeRect`` で容易に描ける。箱の寸法が縦と横で異なるようなら、それらを
  保持する変数を定義しろ。
* 丸い玉を作るには、パスを始めて ``arc(x, y, radius, 0, 7)`` を呼び出せ。それか
  らパスを塗りつぶせ。
* 玉の位置と速度を模すには第 16 章のクラス ``Vec`` を使える。初速を与えて、各フ
  レーム（コマ）でその速度と経過時間を乗じろ。
* 玉が垂直に立つ壁に十分過ぎるほど接近するときに速度の ``x`` 成分を反転しろ。水
  平の壁に衝突するときには同様にして ``y`` 成分を反転しろ。
* 新しい位置と速度を見出したら、シーン全体を ``clearRect`` で消去し、再描画し
  ろ。

**解答** まず以前手に入れた ``Vec`` のコードを利用可能にしておく。下準備部分の
コードは次のようになる：

.. code:: javascript

   const canvas = document.querySelector("canvas");
   const cx = canvas.getContext("2d");
   const ball = {
       color: "red",
       radius: 10,
       pos: new Vec(canvas.width / 2, canvas.height / 2),
       speed: new Vec(3.0, 0.0),
   };

次にアニメーションのコードの骨格を書く：

.. code:: javascript

   function animate(time, lastTime) {
       if (lastTime != null) {
         const delta = time - lastTime;
         ball.speed.y += delta * 0.01;
       }

       // motion of the ball...

       cx.clearRect(0, 0, canvas.width, canvas.height);
       cx.strokeStyle = "black";
       cx.strokeRect(0, 0, canvas.width, canvas.height);
       cx.beginPath();
       cx.arc(ball.pos.x, ball.pos.y, ball.radius, 0, 6.29);
       cx.closePath();
       cx.fillStyle = ball.color;
       cx.fill();
       requestAnimationFrame(newTime => animate(newTime, time));
  }
  requestAnimationFrame(animate);

* まずキャンバス全域を消去する。それから矩形を描く。次に玉を描く。
* 以前のゲームでやったように垂直軸方向に加速度を与える。

コメントを入れた箇所に玉の運動を定義する。前章の ``Player.prototype.update`` が
参考になる：

.. code:: javascript

   const newx = ball.pos.x + ball.speed.x;
   if (ball.pos.x < ball.radius) {
       ball.pos.x = ball.radius;
       ball.speed.x = -ball.speed.x;
   }
   else if (ball.pos.x > canvas.width - ball.radius) {
       ball.pos.x = canvas.width - ball.radius;
       ball.speed.x = -ball.speed.x;
   }
   else {
       ball.pos.x = newx;
   }

   const newy = ball.pos.y + ball.speed.y;
   if (ball.pos.y < ball.radius) {
       ball.pos.y = ball.radius;
       ball.speed.y = -ball.speed.y;
   }
   else if (ball.pos.y > canvas.height - ball.radius) {
       ball.pos.y = canvas.height - ball.radius;
       ball.speed.y = -ball.speed.y;
   }
   else {
       ball.pos.y = newy;
   }

コードが汚い。

Precomputed mirroring
----------------------------------------------------------------------

座標変換の残念な点は、ビットマップの描画が遅くなることだ。各ピクセルの位置とサイ
ズを変換しなければならないので、将来的にはブラウザーが変換をより賢くする可能性も
あるが、現在は、ビットマップの描画にかかる時間が大幅に増加する。

我々のゲームのようなものでは、変換された単一のスプライトを描くだけなのでこのこと
は問題ではないが、何百ものキャラクターや、爆発で回転する何千もの粒子を描く必要が
あるとしたらどうだろう。

**問題** 追加の画像ファイルを読み込まずに、また、フレームごとに変換された
``drawImage`` を呼び出さずに、キャラクターを反転させて描く方法を考えろ。

**解答** 課せられた制約は

* 画像ファイルは一枚しか使えないことと、
* 反転画像を生成するのは一度限りであること

の二つだ。

あまり興味がないので巻末のヒントを読む。こういう感じで鏡像を仕込んでおくようだ：

.. code:: javascript

   const cvSource = document.createElement("canvas");
   cvSource.setAttribute("id", "image-source");
   const cvFlipped = document.createElement("flipped");
   cvFlipped.setAttribute("id", "image-flipped");

   const img = document.createElement("img");
   img.src = "source.png";
   img.addEventListener("load", () => {
       cxSource.drawImage(img, 0, 0);
       flipHorizontally(cxSource, img.width / 2);
       cxFlipped.drawImage(cvSource, 0, 0);
   });

あるいはイベントハンドラーを二つに分割しても行けるだろう。

以後、任意のキャンバス上で鏡像を描画することができる：

.. code:: javascript

   function drawFlippedImage(dest, x, y){
       dest.drawImage(document.querySelector("image-flipped"), x, y);
   }

以上
