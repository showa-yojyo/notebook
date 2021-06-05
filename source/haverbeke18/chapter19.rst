======================================================================
Project: A Pixel Art Editor
======================================================================

この章では MS Paint のようなアプリケーションをブラウザーの上に実装する。

.. contents:: ノート目次

Components
======================================================================

このアプリケーションのインターフェースは、

* 上部に大きな ``<canvas>`` 要素があり、その下にいくつかのフォームフィールドがある。
* ユーザーは ``<select>`` フィールドからツールを選択し、
  キャンバス上をクリック、タッチ、またはドラッグして絵を描く。
* ツールには、

  * 単一のピクセルや矩形を描くもの、
  * 領域を塗りつぶすもの、
  * 絵から色を選ぶものなどがある。

インターフェイスをコンポーネントの集合体として構成する。

* コンポーネントとは、DOM の一部に対して責任があるオブジェクトであり、
  その中に他のコンポーネントを含むこともある。

アプリケーションの状態は次の要素で構成する。
ここでは状態が一つの値に収まるようにし、インターフェイスコンポーネントは
いつでも現在の状態に基づいて表示されるようにする：

* 現在の画像
* 選択されているツール
* 選択されている色

状態がまず存在して、それに基づいてインターフェイスが描画される。
インターフェイスコンポーネントはユーザーの動作に反応して状態を更新することもあるが、
そのときにコンポーネントはこの新しい状態に同期する機会を得る。

各コンポーネントは新しい状態になると、子コンポーネントにも更新を通知するようにする。

* 状態の更新をオブジェクトとして表現する。これをアクションと呼ぶ。
  コンポーネントはこのようなアクションを生成し、それらをディスパッチして、中央の状態管理関数に与える。
  この関数は次の状態を計算し、その後、インターフェイスコンポーネントは自身を新しい状態に更新する。

ユーザーインターフェースを実行することと、いくつかの構造をそれに当てはめるという厄介なタスクがある。
それらは状態更新サイクルに支えられる。

状態は DOM がどのように見えるかを決定するので、DOM イベントが状態を変えるには、
その状態にアクションをディスパッチするしかない。

このアプローチには多くの変種があり、それぞれに長所と短所があるが、中心となる考えは同じだ。
状態の変化は well-defined な単一の通路を経由するべきだ。

コンポーネントはあるインターフェイスに適合したクラスとする。

* コンストラクターには、ある状態（アプリケーション全体のそれかもしれないし、小さな値かもしれない）が与えられ、
  それはプロパティー ``dom`` を構築するのに使う。
* コンストラクターの大部分は時間経過によらない別の値も受け取る。
  例えばアクソンをディスパッチするための関数などだ。
* メソッド ``syncState`` があり、新しい状態の値に同期するために呼び出される。
  このメソッドは引数を一つ取り、それはコンストラクターの第一引数と同じ型の状態とする。

The state
======================================================================

* アプリケーションの状態は次のものをプロパティーに持つオブジェクトとする：

  * ``picture``
  * ``tool``
  * ``color``

----

``picture`` はそれ自体オブジェクトであり、次のプロパティーを持つ：

* ``width``
* ``height``
* ``pixel``: 第 6 章の行列クラスと同様に、ピクセルが上から下に向かって一行ずつ一つの配列に格納される。

.. code:: javascript

   class Picture {
       constructor(width, height, pixels) {
           this.width = width;
           this.height = height;
           this.pixels = pixels;
       }
       static empty(width, height, color) {
           let pixels = new Array(width * height).fill(color);
           return new Picture(width, height, pixels);
       }
       pixel(x, y) {
           return this.pixels[x + y * this.width];
       }
       draw(pixels) {
           let copy = this.pixels.slice();
           for (let {x, y, color} of pixels) {
               copy[x + y * this.width] = color;
           }
           return new Picture(this.width, this.height, copy);
       }
   }

* メソッド ``draw`` は更新されたピクセルの配列を受け取り、
  それらのピクセルを上書きした新しい ``Picture`` オブジェクトを生成する。

  * 引数なしの ``slice`` を用いてピクセル配列全体をコピーする。

* メソッド ``empty`` でこれまで見られなかった配列の機能を二つ利用している。

  * 配列のコンストラクターに数を指定して呼び出すと、その長さの空の配列を生成する。
  * メソッド ``fill`` は指定した値で配列を埋める。

  これらを使って、すべてのピクセルが同じ色の配列を生成する。

----

``color`` は記号 ``#`` と六桁の 16 進数（赤緑青それぞれ二桁ずつ）からなる伝統的な CSS 色コードを値とする。

* これは HTML の色入力欄が使用する記法であり、``<canvas>`` の描画コンテキストの
  プロパティー ``fillStyle`` でも使用できるため、このプログラムにおいて実用的な方法だ。

----

インターフェイスがアクションを、以前の状態のプロパティーを上書きするオブジェクトとしてディスパッチできるようにする。
ユーザーが ``color`` フィールドを変更すると、
``{color: field.value}`` のようなオブジェクトがディスパッチされ、
そこからこの更新関数が新しい状態を計算することできる：

.. code:: javascript

   function updateState(state, action) {
       return Object.assign({}, state, action);
   }

* ``Object.assign`` を使用して、まず空のオブジェクトに ``state`` のプロパティーを追加し、
  ``action`` のプロパティーのいくつかで上書きするという、このやや面倒なパターンは、
  immutable なオブジェクトを使う JavaScript コードでは普通に見られるものだ。

  * 他のオブジェクトのすべてのプロパティーをオブジェクト式に含めるための、
    より便利な表記法としては、演算子 ``...`` が使われる（これは本書執筆時点で標準化最終段階にある）。
    これを使えば先ほどのコードを ``{...state, ...action}`` と書くことができる。

DOM building
======================================================================

インターフェイスコンポーネントが行う主なことの一つは、DOM 構造の作成だ。
そのために冗長な DOM メソッド群を直接使用したくないので、ここでは関数
``elt`` を少し拡張したバージョンを使用する。

.. code:: javascript

   function elt(type, props, ...children) {
       let dom = document.createElement(type);
       if (props) Object.assign(dom, props);
       for (let child of children) {
           if (typeof child != "string") dom.appendChild(child);
           else dom.appendChild(document.createTextNode(child));
       }
       return dom;
   }

以前のものとの主な違いは、属性ではなくプロパティーを DOM ノードに割り当てる点だ。
これが意味するのは、任意の属性を設定することはできないが、値が文字列ではないプロパティー
（例えば ``onclick`` のような）を設定することはできるということだ。

これにより、次のようにしてイベントハンドラーを登録することができる：

.. code:: html

   <body>
     <script>
       document.body.appendChild(elt("button", {
           onclick: () => console.log("click")
       }, "The button"));
     </script>
   </body>

The canvas
======================================================================

絵をカラーボックスのグリッドとして表示するインターフェースの部分だ。
このコンポーネントは、絵の表示と、その絵に関するポインターイベントを
アプリケーションの他の部分に伝えることを担当する。

* そのため、アプリケーション全体の状態ではなく、現在の絵だけを知っているコンポーネントとして定義することができる。
  アプリケーション全体の動作を知らないので、アクションを直接ディスパッチすることはできない。
  そうではなく、ポインターイベントに反応するときには、
  このコンポーネントを作成したコードが与えたコールバックを呼び出して、
  アプリケーション固有の部分を処理する。

.. code:: javascript

   const scale = 10;

   class PictureCanvas {
       constructor(picture, pointerDown) {
           this.dom = elt("canvas", {
               onmousedown: event => this.mouse(event, pointerDown),
               ontouchstart: event => this.touch(event, pointerDown)
           });
           this.syncState(picture);
       }
       syncState(picture) {
           if (this.picture == picture) return;
           this.picture = picture;
           drawPicture(this.picture, this.dom, scale);
       }
   }

* 各ピクセルを定数 ``scale`` で決められた 10 ドッド四方の正方形として描画する。
* 不要な作業を避けるべく、コンポーネントは現在の絵を追跡し、
  メソッド ``syncState`` は新しい絵が与えられたときにしか再描画を行わない。

----

実際の描画関数は、``scale`` と ``picture`` の寸法に基づいて ``canvas`` のそれを設定し、
各ピクセルに一つ一つ、一連の正方形で埋めていく。

.. code:: javascript

   function drawPicture(picture, canvas, scale) {
       canvas.width = picture.width * scale;
       canvas.height = picture.height * scale;
       let cx = canvas.getContext("2d");
       for (let y = 0; y < picture.height; y++) {
           for (let x = 0; x < picture.width; x++) {
               cx.fillStyle = picture.pixel(x, y);
               cx.fillRect(x * scale, y * scale, scale, scale);
           }
       }
   }

----

絵のあるキャンバス上にマウスがあるときに左ボタンが押されると、
このコンポーネントは ``pointerDown`` コールバックを呼び出し、クリックされたピクセルの位置を絵座標系で与える。
これで絵に対するマウス操作が実装される。

* このコールバックは、別のコールバック関数を返すことができ、
  ボタンを押している間にポインターが別のピクセルに移動したときに通知される。

.. code:: javascript

   PictureCanvas.prototype.mouse = function(downEvent, onDown) {
       if (downEvent.button != 0) return;

       let pos = pointerPosition(downEvent, this.dom);
       let onMove = onDown(pos);
       if (!onMove) return;

       let move = moveEvent => {
           if (moveEvent.buttons == 0) {
               this.dom.removeEventListener("mousemove", move);
           } else {
               let newPos = pointerPosition(moveEvent, this.dom);
               if (newPos.x == pos.x && newPos.y == pos.y) return;
               pos = newPos;
               onMove(newPos);
           }
       };
       this.dom.addEventListener("mousemove", move);
   };

   function pointerPosition(pos, domNode) {
       let rect = domNode.getBoundingClientRect();
       return {x: Math.floor((pos.clientX - rect.left) / scale),
               y: Math.floor((pos.clientY - rect.top) / scale)};
   }

* ピクセルのサイズがわかっていて、メソッド ``getBoundingClientRect`` を使って
  画面上のキャンバスの位置がわかることから、マウスイベント座標
  ``clientX``, ``clientY`` から絵座標に移動することができる。

  * 特定のピクセルを参照するように、関数 ``Math.floor`` を使って除算結果を整数にする。

----

タッチイベントの場合も同様 (pp. 348-349) だが、異なるイベントを使用することと、
パンを防ぐためにイベント ``touchstart`` で ``preventDefault`` を間違いなく呼び出すことが必要だ。

タッチイベントの場合、``clientX``, ``clientY`` をはイベントオブジェクトでは直接利用できない。
プロパティー ``touches`` の最初のタッチオブジェクトの座標を利用する。

The application
======================================================================

アプリケーションを一つ一つ建てられるように、
絵キャンバスの殻とツールとコントロールの動的な集合としてメインコンポーネントを実装する。

コントロールとは絵の下に現れるインターフェイス要素だ。
コンポーネントのコンストラクターからなる配列として備え付けられる。

ツールはピクセルを描いたり領域を塗りつぶしたりする。

* アプリケーションは利用可能なツールの集合を ``<select>`` フィールドとして表示する。
* 選択中のツールは、ユーザーがポインター機器を使って絵を操作するときに起こることを決定する。
* 利用可なツールの集合はドロップダウンメニューに表示される名前を、それが示す関数を対応付けるオブジェクトとして与える。
* このような関数は絵の位置、現在のアプリケーションの状態、ディスパッチ関数を引数として受け取る。
  また、ポインターが別のピクセルに移動すると、新しい位置と現在の状態を指定して呼び出される
  移動ハンドラー関数を返すこともある。

.. code:: javascript

   class PixelEditor {
       constructor(state, config) {
           let {tools, controls, dispatch} = config;
           this.state = state;

           this.canvas = new PictureCanvas(state.picture, pos => {
               let tool = tools[this.state.tool];
               let onMove = tool(pos, this.state, dispatch);
               if (onMove) return pos => onMove(pos, this.state);
           });
           this.controls = controls.map(
               Control => new Control(state, config));
           this.dom = elt("div", {}, this.canvas.dom, elt("br"),
                          ...this.controls.reduce(
                          (a, c) => a.concat(" ", c.dom), []));
       }

       syncState(state) {
           this.state = state;
           this.canvas.syncState(state.picture);
           for (let ctrl of this.controls) ctrl.syncState(state);
       }
   }

* ``PictureCanvas`` に与えられたポインターハンドラーは、
  現在選択されているツールを適切な引数で呼び出し、
  もしそれが移動ハンドラーを返すならば、状態も受け取るように適応させる。
* すべてのコントロールは、アプリケーションの状態が変化したときに更新できるように構築され、
  ``this.controls`` に収められる。

  * メソッド ``reduce`` の呼び出しでコントロールの DOM 要素の間に隙間を作る。
    こうすると窮屈なみてくれにならない。

----

ツール選択メニューは各ツールを選択肢とする ``<select>`` 要素を生成し、
ユーザーが異なるツールを選択すると、アプリケーションの状態を更新する
イベント ``change`` に対するイベントハンドラーを仕込む。

.. code:: javascript

   class ToolSelect {
       constructor(state, {tools, dispatch}) {
           this.select = elt("select", {
               onchange: () => dispatch({tool: this.select.value})
           }, ...Object.keys(tools).map(name => elt("option", {
               selected: name == state.tool
           }, name)));
           this.dom = elt("label", null, "🖌 Tool: ", this.select);
       }
       syncState(state) { this.select.value = state.tool; }
   }

* ラベルテキストとフィールドを ``<label>`` 要素で包み込むことで、
  ラベルがそのフィールドに属していることをブラウザーに知らせ、
  ラベルがクリックされるなどするとフィールドがフォーカスされるようにする。

----

色を変更するためのコントロールを追加する。

HTML の ``<input>`` 要素の属性 ``type`` に ``color`` を指定すると、
色を選択するための専用のフォーム記入欄ができる。

* この記入欄の値は常に ``#RRGGBB`` 形式の CSS 色コードだ。
* ユーザーがこの記入欄をいじると、ブラウザーは色選択インターフェイスを表示する。

当コントロールはそのような記入欄を作成し、アプリケーションの ``state`` の
プロパティー ``color`` と同期するように結びつける。

.. code:: javascript

   class ColorSelect {
       constructor(state, {dispatch}) {
           this.input = elt("input", {
               type: "color",
               value: state.color,
               onchange: () => dispatch({color: this.input.value})
           });
           this.dom = elt("label", null, "🎨 Color: ", this.input);
       }
       syncState(state) { this.input.value = state.color; }
   }

Drawing tools
======================================================================

何かを描く前に、キャンバス上のマウスやタッチのイベントの機能を制御するツールが必要だ。

最も基本的なツールは描画ツールで、クリックやタップしたピクセルを現在選択している色に変える。
このツールは指定ピクセルが現在選択中の色に変更されるように絵を更新するアクションをディスパッチする。

.. code:: javascript

   function draw(pos, state, dispatch) {
       function drawPixel({x, y}, state) {
           let drawn = {x, y, color: state.color};
           dispatch({picture: state.picture.draw([drawn])});
       }
       drawPixel(pos, state);
       return drawPixel;
   }

この関数はすぐに関数 ``drawPixel`` を呼び出すが、なおかつ、
ユーザーが絵の上でドラッグやスワイプをしたときに、
新たに触られたピクセルに対して再度 ``drawPixel`` が呼び出されるようにこれを返しもする。

----

矩形ツールはドラッグを開始した点とドラッグした点の間に矩形を描く。

.. code:: javascript

   function rectangle(start, state, dispatch) {
       function drawRectangle(pos) {
           let xStart = Math.min(start.x, pos.x);
           let yStart = Math.min(start.y, pos.y);
           let xEnd = Math.max(start.x, pos.x);
           let yEnd = Math.max(start.y, pos.y);
           let drawn = [];
           for (let y = yStart; y <= yEnd; y++) {
               for (let x = xStart; x <= xEnd; x++) {
                   drawn.push({x, y, color: state.color});
               }
           }
           dispatch({picture: state.picture.draw(drawn)});
       }
       drawRectangle(start);
       return drawRectangle;
   }

この実装で重要なのは、ドラッグしたときに、矩形が元の状態から絵の上に再描画されることだ。
そうすることで、中間的な矩形が最終的な絵に残ることなく、
矩形を作成しつつ大きくしたり小さくしたりすることができる。

* 絵を immutable オブジェクトにしたことが活きている。

----

塗りつぶしツールはポインターの下のピクセルと、それに隣接する同じ色のピクセルすべてを塗りつぶすツールだ。

* 隣接とは、水平方向または垂直方向に直接隣接していることを意味する。
* 塗りつぶしのアルゴリズムは第 7 章の経路探索に少し似ている。
  グラフから経路を探すのではなく、格子から連結しているピクセルを探す。

.. code:: javascript

   const around = [{dx: -1, dy: 0}, {dx: 1, dy: 0},
                   {dx: 0, dy: -1}, {dx: 0, dy: 1}];

   function fill({x, y}, state, dispatch) {
       let targetColor = state.picture.pixel(x, y);
       let drawn = [{x, y, color: state.color}];
       for (let done = 0; done < drawn.length; done++) {
           for (let {dx, dy} of around) {
               let x = drawn[done].x + dx, y = drawn[done].y + dy;
               if (x >= 0 && x < state.picture.width &&
                   y >= 0 && y < state.picture.height &&
                   state.picture.pixel(x, y) == targetColor &&
                   !drawn.some(p => p.x == x && p.y == y)) {
                   drawn.push({x, y, color: state.color});
               }
           }
       }
       dispatch({picture: state.picture.draw(drawn)});
   }

* 描画されたピクセルの配列とこの関数の作業用リストを兼用している。
* 各ピクセルに到達するたびに、隣接ピクセルの色と塗りつぶし済みかどうかを確認しなければならない。
* 新しいピクセルを追加すると、ループカウンターは描画された配列の長さよりも遅れる。
  先行するピクセルはまだ探索する必要がある。
  カウンターが長さに追いつくときは、未探索のピクセルが残っていないということなので、この関数を終了する。

----

色摘出ツールは絵の中の色を指定して、それを現在の描画色として使う。

.. code:: javascript

   function pick(pos, state, dispatch) {
       dispatch({color: state.picture.pixel(pos.x, pos.y)});
   }

Saving and loading
=======================================================================

現在の絵を画像ファイルとしてダウンロードするためのボタンを追加する。

.. code:: javascript

   class SaveButton {
       constructor(state) {
           this.picture = state.picture;
           this.dom = elt("button", {
               onclick: () => this.save()
           }, "💾 Save");
       }

       save() {
           let canvas = elt("canvas");
           drawPicture(this.picture, canvas, 1);
           let link = elt("a", {
               href: canvas.toDataURL(),
               download: "pixelart.png"
           });
           document.body.appendChild(link);
           link.click();
           link.remove();
       }

       syncState(state) { this.picture = state.picture; }
   }

このコンポーネントは、保存時にアクセスできるように現在の絵を追跡している。
画像ファイルを作成するために ``<canvas>`` 要素を使用し、その上に画像を実寸大で描画する。

``<canvas>`` 要素のメソッド ``toDataURL`` 呼び出しは ``data://`` で始まる URL を返す。
``http://`` や ``https://`` の URL とは異なり、``data://`` URL はリソース全体を文字列中に含む。
したがって、ひじょうに長くなるものの、ブラウザー上で任意の画像へのリンクを作成することができる。

ブラウザーに画像を実際にダウンロードさせるには、この URL を指し示す ``link`` 要素を作成し、
属性 ``download`` を付ける。このリンクをクリックすると、ブラウザーはファイル保存ダイアログボックスを表示する。
そのリンクを文書に追加し、クリックをシミュレートして、削除する。

----

既存の画像ファイルをアプリケーションに読み込めるようにする。
そのために再びボタンコンポーネントを定義する。

.. code:: javascript

   class LoadButton {
       constructor(_, {dispatch}) {
           this.dom = elt("button", {
               onclick: () => startLoad(dispatch)
               }, "📁 Load");
       }

       syncState() {}
   }

   function startLoad(dispatch) {
       let input = elt("input", {
           type: "file",
           onchange: () => finishLoad(input.files[0], dispatch)
       });
       document.body.appendChild(input);
       input.click();
       input.remove();
   }

* ユーザーのコンピュータにあるファイルにアクセスするには、
  ユーザーがファイル入力フィールドでファイルを選択する必要がある。
  しかし、ロードボタンをファイル入力フィールドのように見せたくないので、
  ボタンがクリックされたときにファイル入力を作成し、
  このファイル入力自体がクリックされたふりをする。

----

ユーザーがファイルを選択すると、``FileReader`` を使ってその内容にアクセスすることができ、
これも ``data://`` 形式の URL として使える。この URL を使って ``<img>`` 要素を作ることができるが、
画像のピクセルに直接アクセスすることができないため、そこから ``Picture`` オブジェクトを作ることはできない。

.. code:: javascript

   function finishLoad(file, dispatch) {
       if (file == null) return;
       let reader = new FileReader();
       reader.addEventListener("load", () => {
           let image = elt("img", {
           onload: () => dispatch({
               picture: pictureFromImage(image)
           }),
           src: reader.result
           });
       });
       reader.readAsDataURL(file);
   }

ピクセルにアクセスするには、まず ``<canvas>`` 要素に画像を描画する。
キャンバスコンテキストにはメソッド ``getImageData`` があるので、スクリプトからそのピクセルを読み取れる。
つまり、画像をキャンバスに描画したら、それにアクセスして ``Picture`` オブジェクトを構築できる。

.. code:: javascript

   function pictureFromImage(image) {
       let width = Math.min(100, image.width);
       let height = Math.min(100, image.height);
       let canvas = elt("canvas", {width, height});
       let cx = canvas.getContext("2d");
       cx.drawImage(image, 0, 0);
       let pixels = [];
       let {data} = cx.getImageData(0, 0, width, height);

       function hex(n) {
           return n.toString(16).padStart(2, "0");
       }

       for (let i = 0; i < data.length; i += 4) {
           let [r, g, b] = data.slice(i, i + 3);
           pixels.push("#" + hex(r) + hex(g) + hex(b));
       }

       return new Picture(width, height, pixels);
   }

画像の寸法を 100x100 ピクセルに制限する。
これ以上大きくすると、画面上で巨大に見えてしまい、インターフェースが遅くなるかもしれない。

コンテキストのメソッド ``getImageData`` が返すオブジェクトのプロパティー ``data`` は色成分の配列だ。
引数で指定された矩形内の各ピクセルには、ピクセルの RGBA 成分が 0 から 255 までの数で格納されている。

* 本アプリケーションではアルファ値は使わない。
* ヘルパー関数 ``hex`` は数を 16 進数表記にするのに定義されている。
  JavaScript ではこういうのを自前で書かないといけないようだ。

Undo history
======================================================================

変更を元に戻せるようにするには、絵の以前のバージョンを保存しておく必要がある。
アプリケーションの状態に追加的なフィールドを必要とする。

絵の以前のバージョンを保存するのに配列 ``done`` を追加することにする。
このプロパティーを維持するのには配列に絵を追加する、より複雑な状態更新関数が要る。

変更のすべてではなく、一定の時間的間隔をおいた変更しか保存したくない。
そうするには、最後に絵を履歴に保存した時刻を追跡するプロパティー ``doneAt`` が要る。

.. code:: javascript

   function historyUpdateState(state, action) {
       if (action.undo == true) {
           if (state.done.length == 0) return state;
           return Object.assign({}, state, {
               picture: state.done[0],
               done: state.done.slice(1),
               doneAt: 0
           });
       } else if (action.picture && state.doneAt < Date.now() - 1000) {
           return Object.assign({}, state, action, {
               done: [state.picture, ...state.done],
               doneAt: Date.now()
           });
       } else {
           return Object.assign({}, state, action);
       }
   }

アクションが元に戻すアクションの場合、この関数は履歴から最新の絵を取り出し
それを現在の絵にする。プロパティー ``doneAt`` の値をゼロにすることで、
次の変更時には絵が履歴に保存されることを保証し、必要に応じて履歴を別の時刻に戻すことができる。

また、アクションが新しい絵を含み、かつ最後に何かを保存したのが一秒以上前ならば、
プロパティー ``done`` と ``doneAt`` を更新して直前の絵を保存する。

----

元に戻すボタンコンポーネントは多くをしない。
クリックされると元に戻すアクションをディスパッチし、元に戻すものがないときは自身をグレーアウトする。

.. code:: javascript

   class UndoButton {
       constructor(state, {dispatch}) {
           this.dom = elt("button", {
               onclick: () => dispatch({undo: true}),
               disabled: state.done.length == 0
           }, "⮪ Undo");
       }
       syncState(state) {
           this.dom.disabled = state.done.length == 0;
       }
   }

Let's draw
======================================================================

アプリケーションを仕掛けるには、状態、ツールの集合、コントロールの集合、
ディスパッチ関数を生成する必要がある。これらを ``PixelEditor`` コンストラクターに渡して
主要コンポーネントを作成できる。

.. code:: javascript

   const startState = {
       tool: "draw",
       color: "#000000",
       picture: Picture.empty(60, 30, "#f0f0f0"),
       done: [],
       doneAt: 0
   };
   const baseTools = {draw, fill, rectangle, pick};
   const baseControls = [
       ToolSelect, ColorSelect, SaveButton, LoadButton, UndoButton
   ];

   function startPixelEditor({state = startState,
                              tools = baseTools,
                              controls = baseControls}) {
       let app = new PixelEditor(state, {
           tools,
           controls,
           dispatch(action) {
               state = historyUpdateState(state, action);
               app.syncState(state);
           }
       });
       return app.dom;
   }

オブジェクトや配列を分割代入するとき、変数名の後ろに ``=`` を付けると変数名に既定値を与えることができる。
これは、プロパティーがない場合や ``undefined`` を保持する場合に用いられる。

関数 ``startPixelEditor`` はいくつかのオプションのプロパティーを持つオブジェクトを引数に取る。
例えばプロパティー ``tools`` を与えない場合、その値は ``baseTools`` になる。

次のようにして実際のエディターを画面に表示する：

.. code:: html

   <div></div>
   <script>
   document.querySelector("div").appendChild(startPixelEditor({}));
   </script>

Why is this so hard?
======================================================================

この節は著者の主張がよくわからないので省略。

Exercises
======================================================================

Keyboard bindings
----------------------------------------------------------------------

**問題** アプリケーションにキーボードショートカットを追加しろ。

* ツール名の最初の文字でそのツールを選択し、
* :kbd:`Ctrl` + :kbd:`Z` でアンドゥを起動しろ。

これを ``PixelEditor`` を変更することで行え。
値がゼロのプロパティー ``tabIndex`` を折り返しの ``<div>`` に設定し、キーボードフォーカスを受けられるようにしろ。
なお、属性 ``tabindex`` に対応するプロパティーは ``tabIndex`` と大文字の I が使われているが
関数 ``elt`` はプロパティー名を期待することに注意しろ。

キーイベントハンドラーを上記 ``<div>`` に直接登録しろ。
つまり、キーボードで操作する前に、アプリケーションをクリックしたり、タッチしたりする必要がある。
キーボードイベントには ``ctrlKey`` と ``metaKey`` のプロパティーがあり、
これらのキーが押されているかどうかを確認することができることを忘れるな。

**解答** ツール選択は ``PixelEditor.constructor`` のコードで ``this.dom`` を定義するところを
次のように変更する：

.. code:: javascript

   this.dom = elt("div", {
       tabIndex: 0,
       onkeydown: (event) => {
           const toolNames = Object.keys(tools);
           const toolName = toolNames.find(name => name[0] == event.key);
           if(toolName){
               const selectNode = this.controls[0].select;
               selectNode.value = toolName;
               selectNode.onchange();
               event.preventDefault();
               return;
           }
       }
   }, // ...

* ドロップダウンリストの項目を直接変更してハンドラー ``onchange`` を直接呼び出すという下品なコードだ。

後半のアンドゥ発動は、この ``onkeydown`` にさらにコードを追加するわけだが、凝ったことをするとハマりがちだ。
とりあえずこう書いておき：

.. code:: javascript

   for(const dom of this.controls.map(i => c.dom)){
       if(dom.onkeydown){
           dom.onkeydown(event);
       }
   }

クラス ``UndoButton`` の ``this.dom`` に ``onkeydown`` を追加しておく：

.. code:: javascript

   onkeydown: (event) => {
       if(event.key == "z" && event.ctrlKey){
           this.dom.click();
           event.preventDefault();
       }
   },

* 困ったことに ``event.preventDefault()`` したか否かをテストする手段がわからない。
  もしこれ以上の処理を禁止するのであれば即 ``return`` する。

Efficient drawing
----------------------------------------------------------------------

描画の際、アプリケーションが行う作業の大半は ``drawPicture`` で起こる。
新しい状態を作成して DOM の残りの部分を更新するのはそれほど高くつかないが、
キャンバス上のすべてのピクセルを再描画するのはかなりの労力を要する。

**問題** 実際に変化したピクセルしか再描画しないように、メソッド ``PictureCanvas.syncState`` を高速化する方法を考えろ。
``drawPicture`` は保存ボタンでも使用されているので、変更する場合は、
以前の使用方法が壊れないようにするか、別の名前で新しいバージョンを作成することだ。

また、要素 ``<canvas>`` の ``width`` や ``height`` のプロパティーを設定して寸法を変更すると、
それを消去して完全に透明になることにも注意しろ。

**解答** ``PictureCanvas.syncState`` が ``drawPicture`` を呼び出すときに
新旧のピクセルバッファーが一瞬同時に存在するので、これを比較して差分だけを描画しろというのが題意だ。
したがって、まず呼び出し側を次のように変更する：

.. code:: javascript

    syncState(picture) {
        if (this.picture == picture) return;
        drawPicture(picture, this.picture, this.dom, scale);
        this.picture = picture;
    }

描画関数を差分のみ彩色するように書き換える：

.. code:: javascript

   function drawPicture(newPicture, oldPicture, canvas, scale) {
       // Also note that changing the size of a <canvas> element,
       // by setting its width or height properties, clears it, making it
       // entirely transparent again.
       if (!oldPicture) {
           canvas.width = newPicture.width * scale;
           canvas.height = newPicture.height * scale;
       }

       let cx = canvas.getContext("2d");
       for (let y = 0; y < newPicture.height; y++) {
           for (let x = 0; x < newPicture.width; x++) {
               if (oldPicture &&
                   oldPicture.pixel(x, y) == newPicture.pixel(x, y)) {
                   continue;
               }
               cx.fillStyle = newPicture.pixel(x, y);
               cx.fillRect(x * scale, y * scale, scale, scale);
           }
       }
   }

最後に ``SaveButton`` のハンドラーを調整する：

.. code:: javascript

   save() {
       let canvas = elt("canvas");
       drawPicture(this.picture, null, canvas, 1);
       // ...
   }

Circles
----------------------------------------------------------------------

**問題** ドラッグすると円が描かれるツール ``circle`` を定義しろ。
円の中心は、ドラッグやタッチを開始した位置にあり、その半径はドラッグした距離に応じて決まる。

**解答** マウスやタッチによる操作が矩形ツールと似ているので、コードもそれに倣う。

.. code:: javascript

   function circle(start, state, dispatch) {
       function drawCircle(pos) {
           const radiusSquared = (start.x - pos.x)**2 + (start.y - pos.y)**2;
           const radius = Math.sqrt(radiusSquared);
           const xStart = Math.floor(Math.max(0, start.x - radius));
           const xEnd = Math.floor(Math.min(state.picture.width, start.x + radius));
           const yStart = Math.floor(Math.min(0, start.y - radius));
           const yEnd = Math.floor(Math.max(state.picture.height, start.y + radius));
           const drawn = [];
           for (let y = yStart; y <= yEnd; y++) {
               const yDeltaSquared = (start.y - y)**2;
               for (let x = xStart; x <= xEnd; x++) {
                   const xDeltaSquared = (start.x - x)**2;
                   if(xDeltaSquared + yDeltaSquared <= radiusSquared){
                       drawn.push({ x, y, color: state.color });
                   }
               }
           }
           dispatch({ picture: state.picture.draw(drawn) });
       }
       drawCircle(start);
       return drawCircle;
   }

* ピクセルをループする際にカウンターと境界値の両方が整数になるように注意すること。
* 上の数値計算には高速化の余地があるはずだが（関数 ``Math.sqrt`` の使用を避けたい）、
  この演習はそういう趣旨ではないのでやらない。

このツールをエディターに組み込むには、例えば次のように変更する：

.. code:: javascript

   const baseTools = { draw, fill, rectangle, circle, pick };

Proper lines
----------------------------------------------------------------------

ほとんどのブラウザーでは、描画ツールを選択して画像上をすばやくドラッグしても閉じた線が得られない。
これは、``mousemove`` や ``touchmove`` のイベントが、すべてのピクセルに到達するほど速く発射しなかったことによる。

**問題** ``draw`` ツールを改良して、完全な線を描けるようにしろ。
上記イベントハンドラー関数に前回の位置を記憶させ、それを現在の位置に連結する必要がある。
ピクセルは任意の距離だけ離して存在し得るので、補間する線を引く関数を書かねばならない。

二つのピクセル間の線とは、始点から終点まで可能な限り直線で結ばれたピクセルの連鎖だ。
斜めに隣接するピクセルも連結されたものとして扱う（本書の図を参照。左側のほうが望ましい）。

任意の二点間に直線を引くコードがあれば、それを用いたドラッグの開始点と終了点の間に直線を引くラインツールも定義しておくのもいいだろう。

**解答** この課題は前のものよりも高度だ。時間がよりかかる。

.. todo:: 早く次に行きたいので後回しにする。
