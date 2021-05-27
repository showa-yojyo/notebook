======================================================================
Drawing on Canvas
======================================================================

ブラウザーでグラフィックスを扱う方法はいくつかある。
一つは SVG であり、もう一つはキャンバスだ。
前者はベクトルデータ、後者はラスターデータという際立った違いがある。

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

* 属性 ``xmlns`` は要素を異なる XML 名前空間に変える。
  URL により識別されるこの名前空間は、現在使っている方言を指定する。
* HTML には存在しない ``<circle>`` や ``<rect>`` タグは SVG においては意味がある。
  属性が指定するスタイルと位置を使って図形を描画する。
* これらのタグは DOM 要素を生成する。HTML タグと同様に JavaScript から操作できる。
  例えば次のようなコードは有効だ：

  .. code:: javascript

     let circle = document.querySelector("circle");
     circle.setAttribute("fill", "cyan");

The canvas element
======================================================================

* キャンバスグラフィックは ``<canvas>`` 要素に描画できる。
  このような要素に属性 ``width`` と ``height`` をピクセル単位で与えて寸法を決められる。
* 新しいキャンバスは空だ。完全に透明なので、文書内の何もない空間として現れる。
* タグ ``<canvas>`` は色々なスタイルの描画を可能にすることを意図している。
  現在は次の二つの描画スタイルが広くサポートされている：

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
* キャンバスの座標系は HTML 同様、左上隅を原点とし、そこから Y 軸が画面下方に向かう。

Lines and surfaces
======================================================================

* キャンバスインターフェイスでは図形に対して、その領域に一定の色やパターンを与えて
  塗りつぶしたり、輪郭に沿って線を引いたりすることができる。
  同じ用語が SVG でも使われる。

  * メソッド ``fillRect`` は矩形を塗りつぶす。
    引数には矩形の左上の座標、矩形の幅、高さをとる。
  * メソッド ``strokeRect`` は矩形の輪郭を描く。

* どちらのメソッドもこれ以上の引数は取らない。
  塗りつぶしの色、線の太さなどはメソッドの引数ではなく、
  コンテキストオブジェクトのプロパティーが決定する。

  * プロパティー ``fillStyle`` は図形の塗りつぶし方法を制御する。
    CSS で使われる色記法を用いて色を指定する文字列を値とする。
  * プロパティー ``strokeStyle`` は描線の色を決定する。
  * プロパティー ``lineWidth`` は描線の太さを決定する。任意の正の数を指定できる。

.. code:: javascript

   let cx = document.querySelector("canvas").getContext("2d");
   cx.strokeStyle = "blue";
   cx.strokeRect(5, 5, 50, 50);
   cx.lineWidth = 5;
   cx.strokeRect(135, 5, 50, 50);

* このコードで ``<canvas>`` に ``width`` や ``height`` が指定されていないことに注意。
  既定値が適用される。

Paths
======================================================================

パスとは線分の列だ。2D キャンバスインターフェイスはパスを記述するのに独特のアプローチをとる。
これは完全に副作用でなされるものだ。パスは保存したり受け渡したりするような値ではない。
パスで何かをするときには、その形状を記述するためにメソッドをいくつか続けて呼び出す。

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

* パスをメソッド ``fill`` で塗りつぶすことができる。各形状が個別に塗りつぶされる。
* パスは複数の形状を含むことができる。メソッド ``moveTo`` を呼び出すと形状が一つ始まる。
* パスが閉曲線を構成していることを塗りつぶしの前提としているので、
  閉じていないパスを塗りつぶすと、パスの端点に線分が補完されたかのようにした形状を塗りつぶす。

  * メソッド ``closePath`` を使って、そのような線分を明示的に追加することもできる。

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

メソッド ``bezierCurveTo`` もまた曲線を描くものだ。
これは始点と終点とそれぞれに接線を与えるインターフェイスがある（三次曲線なので点が 4 つ要る）。

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

* 他のパス描画メソッドと同様に、メソッド ``arc`` が描く曲線は直前のパス断片に接続される。
  これを避けるには

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

円グラフを構成する扇形の内角を ``count`` の割合に応じて計算するところまで示すと次のようなコード
(p. 303) になる：

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

テキストを描くメソッドには ``fillText`` と ``strokeText`` がある。
後者はアウトラインしている文字には便利だが、ふつうは ``fillText`` が必要とするものだ。

.. code:: javascript

   let cx = document.querySelector("canvas").getContext("2d");
   cx.font = "28px Georgia";
   cx.fillStyle = "fuchsia";
   cx.fillText("I can draw text, too!", 10, 50);

* プロパティ ``font`` に対してテキストのサイズ、スタイル、フォントを指定する。

  * ``italic`` や ``bold`` を文字列の先頭に追加してもいい。

* メソッド ``fillText``, ``strokeText`` の最後の二つの引数でテキストの描画位置を指定する。
  位置とは、文字のベースラインに相当する。アルファベットの j とか p の下の部分が突き出るような線だ。
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

* ブラウザーがまだ読み込めていない可能性があるのですぐには描き始めない。
  イベント ``load`` のハンドラーを登録して、読み込まれてから描画する。

.. code:: javascript

   let cx = document.querySelector("canvas").getContext("2d");
   let img = document.createElement("img");
   img.src = "img/hat.png";
   img.addEventListener("load", () => {
       for (let x = 10; x < 200; x += 30) {
           cx.drawImage(img, x, 10);
       }
   });

* ``drawImage`` にさらに二つ引数を追加して、元サイズとは異なる幅と高さを指定することもできる。

----

``drawImage`` に引数を 9 個与えると、画像の一部だけを描画することができる。

* 第 2, 3, 4, 5 引数はコピー元画像の矩形範囲を位置と寸法で指定する。
* 第 6, 7, 8, 9 引数はコピー先の矩形範囲を位置と寸法で指定する。

この仕様を利用して、複数のスプライトを単一の画像ファイルにまとめて、スライスして描画する技法がある。
特に、スプライトを順次描画することでアニメーションにするという応用がある。

キャンバスにある絵をアニメーションにするにはメソッド ``clearRect`` が役に立つ。
メソッド ``fillRect`` は色を着けるが、これは透明にして直前に描かれたピクセルを消去する。

次のコードは画像をロードし、次のフレーム（コマ）を描画するための時間的間隔を仕込んでそれをする。
各スプライトの寸法が 24x30 であることはわかっているとする：

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

* 変数 ``cycle`` はアニメーション内の位置を追跡する。
  各フレームでこの値をインクリメントして、適宜剰余演算子を使って 0 から 7 の範囲に収める。
  この値は現在のスプライトの全画像における x 座標を計算する。

Transformation
======================================================================

* メソッド ``scale`` を呼び出すと、以降の描画に拡縮変換が施される。
  このメソッドは引数を二つとる。それぞれ水平方向と垂直方向の係数だ。

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

* 絵の向きを場所を変えずに反転するには ``cx.scale(-1, 1)`` だけでは足りない。
  反転画像がビューポートの外に出るだけになる。

----

* メソッド ``rotate`` で図形を回転させる。
* メソッド ``translate`` で図形を移動させる。
* このような図形変換メソッドは重ねて行われる。
  それぞれの変換はその直前の変換に対して相対的に行われる。例えば、

  * 水平方向に 10 ピクセル移動させるのを二度呼び出すと、20 ピクセル移動させることになる。
  * 最初に座標系原点を :math:`(50, 50)` に移動した後、
    何度か回転させると、その回転は :math:`(50, 50)` を中心に回転する。
  * 最初に回転させてから :math:`(50, 50)` だけ移動すると、回転した座標系に対して移動が行われる。
    その結果、異なる向きを生じる。座標変換を適用する順序がだいじだ。

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

* OpenGL の ``glPushMatrix`` や ``glPopMatrix`` のような仕組みが 2D キャンバスにもある。

  * メソッド ``save`` と ``restore`` を用いる。やはり座標変換のスタックを操作するようなものだ。
  * メソッド ``resetTransform`` を呼び出すと座標変換を完全にリセットする。

* 本書 p. 309 の関数 ``branch`` は座標変換を変更する関数が何をできるかを示している。
  再帰呼び出しを利用して典型的なフラクタルを描画する。

Back to the game
======================================================================

以上で、前章のゲームのためにキャンバスを使った表示システムを構築するのに十分な知識を得た。
新しい表示システムでは、色の着いた箱を見せるだけではなく、ゲーム要素を表現する画像を
``drawImage`` で描く。

* ``CanvasDisplay`` (pp. 310-311) という別の表示オブジェクトを定義し、
  前章における ``DOMDisplay`` と同じインターフェイスを、つまり
  メソッド ``syncState`` と ``clear`` を備えるようにする。
* このオブジェクトは ``DOMDisplay`` よりわずかに多くの情報を保持する。

  * ``DOM`` 要素のスクロール位置を使うのではなく、独自のビューポートを追跡して、
    ステージのどの部分を見ているのかを知らせるようにする。
  * プロパティー ``flipPlayer`` を持たせ、プレイヤーが静止しているときでも、直前に動いた方向を向き続けるようにする。

----

メソッド ``syncState`` (p. 311) は、最初に新しいビューポートを計算して、適当な位置にゲームシーンを描画する。

.. code:: javascript

   CanvasDisplay.prototype.syncState = function(state) {
       this.updateViewport(state);
       this.clearDisplay(state.status);
       this.drawBackground(state.level);
       this.drawActors(state.actors);
   };

* ``DOMDisplay`` とは対照的に、このスタイルでは更新のたびに背景を再描画する必要がある。
  キャンバス上の図形は単なるピクセルであるため、描画後にそれを削除・消去する良い方法はない。
  したがって、キャンバスを更新するただ一つの方法は、表示を消去してシーンを再描画することだ。
* スクロールすることもできるが、その場合には背景を別の位置に変える必要がある。

----

メソッド ``updateViewport`` (pp. 311-312) は ``DOMDisplay.scrollPlayerIntoView`` に似ている。
プレイヤーが画面の端に近づき過ぎているかをチェックし、その場合にはビューポートを移動する。

----

表示を消去する (p. 312) ときには、ゲームに勝ったときとそうでないときでは、違う色を使う。

----

背景を描画 (pp. 312-313) するのに、現在のビューポートで見えているタイルの中から、
前章のメソッド ``touches`` と同じ手法で、順番に表示する。

* 空ではないタイルは ``drawImage`` を使って描かれる。

  * 画像 ``otherSprites`` はプレイヤー以外の要素に使われる画像からなる。
    左から順に壁用、溶岩用、コイン用のスプライトだ。
  * ``DOMDisplay`` と同じ尺度を使うつもりなので、背景のタイルは 20x20 ピクセルだ。
    したがって、溶岩タイルのオフセットは 20 であり、壁タイルのそれはゼロだ。

* スプライト画像がロードされるのを待つことを気にする必要はない。
  まだロードされていない画像で ``drawImage`` を呼び出すことは単に何もしないで終わるだけだ。
  そのため、最初の 2, 3 フレームは、画像のロード中にゲームの描画に失敗するかもしれない。
  しかし、これは深刻な問題というわけではない。画面を更新し続けているため、
  ロードが完了すると直ちに正しいシーンが現れる。

----

ここでは p. 305 に掲載されている歩くキャラクターをプレイヤーを表現するのに使う。
それを描画するコードは、プレイヤーの現在の動きに従って、正しいスプライトと方向を決める必要がある。
最初の 8 個のスプライトが歩行アニメーションだ。

* プレイヤーが床上を移動してるときには、現在の時刻に基づいてスプライトを循環させる。

  * 60 ミリ秒ごとにフレームを切り替えたいので、コード中に ``/ 60`` の処理がある。
  * プレイヤーが静止するときには 9 番目のスプライトを描く。
  * ジャンプ時には画像のいちばん右にある 10 番目のスプライトを使う。

* スプライト幅はプレイヤーオブジェクトのそれよりもわずかに大きい。
  これは、足や腕のスペースを確保するために 16 ピクセルではなく 24 ピクセルになっているからだ。
  メソッドでは x 座標と幅を量 ``playerXOverlap`` により調整しなければならない。

* メソッド ``drawPlayer`` (pp. 313-314) は、ゲーム内のすべての出演者の描画を担当するメソッド
  ``drawActors`` (pp. 314-315) から呼び出される。

プレイヤー以外のものを描くときには、その種類を見て正しいスプライトのオフセットを見つける。
溶岩タイルはオフセット 20 に、コインスプライトは 40 にそれぞれある。

キャンバスの原点はステージの左上隅ではなく、ビューポートの左上隅に対応するので、
出演者の位置を計算するときには、ビューポートの位置を差し引かなければならない。

* メソッド ``translate`` を使ってもよい。どちらでも動く。

新しい表示システムの説明は以上だ。スクリーンショットが本書 p.315 にある。

Choosing a graphics interface
======================================================================

ブラウザー上でグラフィックスを生成する必要があるときには、
素の HTML, SVG, キャンバスのいずれかを選択することができることを見てきた。
どの選択肢にも長所と短所がある。

* 素の HTML は単純であることが長所だ。テキストともよく組み込める。
  SVG もキャンバスもテキストを描くことはできるが、位置を調整することと複数行を折り返すことはできない。
  HTML ベースの画像では、テキストブロックを含めるのがずっと容易だ。
* SVG はズーム操作に強い。どんな倍率でも見栄えが良い鮮明なグラフィックスを生成する。
  HTML とは異なり、SVG は描画用途に設計されているため、この目的には適している。
* SVG も HTML も DOM を構築する。
  これにより、要素の修正が考えられるようになる。
  ユーザーの行動に応じたり、アニメーションの一部だったりで、
  大きな絵の小さな部分を繰り返し変更するような場合、キャンバスで行うと必要以上に高くつく。

  * DOM では、画像の中のどの要素にもマウスイベントハンドラーを登録することができる。
    キャンバスではそれができない。

* キャンバスのピクセル指向のアプローチは、膨大な数の微小要素を描くようなときには有利だ。
  データ構造を構築するのではなく、同じピクセル面に繰り返し描画するだけなので、
  キャンバスでは一図形あたりのコストが安くつく。

  * また、シーンを 1 ピクセルずつレンダリングするような効果や、
    JavaScript を使って画像を後処理するなどの、ピクセルベースのアプローチでなければ
    現実的に処理できない効果もキャンバスにならばある。

場合によっては、これらの手法を組み合わせることもできる。
例えば、SVG やキャンバスでグラフを描き、その絵の上に HTML 要素を配置することで
テキストによる情報を見せることができる。

多くを求めないアプリケーションであれば、どのインターフェイスを選ぶかは重要ではない。
本章でゲーム用に作成した表示システムは、文字の描画やマウス操作の処理や異常に多い数の要素をさばく必要がないので、
これら三つのグラフィックス技術のいずれを用いても実装することもできた。

Summary
======================================================================

* 本章ではブラウザーでグラフィックスを描画する技術について議論した。特に
  ``<canvas>`` 要素に焦点を当てた。

  * ``<canvas>`` ノードはプログラムで描画することができる文書内の領域だ。
    描画はメソッド ``getContext`` で生成された描画コンテキストオブジェクトを介してなされる。

* 2D 描画インターフェイスでは、さまざまな図形を塗りつぶしたり、描いたりすることができる。

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

    * 引数を追加的に与えることで、画像の特定の部分を扱うことができる。
      今回のゲームプログラムではこの機能を使用してスプライトを扱った。

* 2D 描画コンテキストは座標変換をサポートしている。

  * 描画コンテキストには現在の変換情報が保持されている。
    これをメソッド ``translate``, ``scale``, ``rotate`` でさらに変換できる。
  * 座標変換はその後の描画処理すべてに影響する。
  * 座標変換はメソッド ``save`` で保存、 ``restore`` で復元することができる。

* キャンバスへのアニメーション表示の際、
  再描画の前にキャンバスの一部を消去するのにメソッド ``clearRect`` が使える。

Exercises
======================================================================

.. todo:: 問題をやるのは後回し。
