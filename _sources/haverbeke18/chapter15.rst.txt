======================================================================
Handling Events
======================================================================

`Eloquent JavaScript <https://eloquentjavascript.net/>`__ Chapter 15 の読書ノート。

マウスやキーボードの操作など、ユーザーが直接入力することで動作するものがある。そ
のようなものをリアルタイムで処理する方法を学習する。

.. contents:: ノート目次

Event handlers
======================================================================

* ポーリング方式でイベントを処理するのは避けたい。より良い仕組みは、システムにイ
  ベントの発生を活発に通知させることだ。
* ブラウザーでは、特定のイベントを処理するハンドラーとして関数を登録することがで
  きる。

  .. code:: html

     <p>Click this document to activate the handler.</p>
     <script>
       window.addEventListener("click", () => {
           console.log("You knocked?");
       });
     </script>

  * 変数 ``window`` はブラウザーが提供する組み込みオブジェクトだ。これは
    ``document`` を含むブラウザーウィンドウを表す。
  * メソッド ``window.addEventListener`` を呼び出すと、第一引数で指定したイベン
    トが発生するたびに、第二引数で指定したコールバックを呼び出すようになる。

Events and DOM nodes
======================================================================

* ブラウザーのイベントハンドラーは何に登録されているか？
* 前節では ``window.addEventListener`` の例を示されたが、そこでいう ``window``
  や ``addEventListener`` のようなものが他にもいくつかある。
* :dfn:`イベントリスナー` とは、イベントハンドラーが登録されているオブジェクトで
  あって、イベントが起こるときにしか呼び出されないものをいう。

  .. code:: html

     <button>Click me</button>
     <p>No handler here.</p>
     <script>
       let button = document.querySelector("button");
       button.addEventListener("click", () => {
           console.log("Button clicked.");
       });
     </script>

  このコードでは前節のようなウィンドウ全体にではなく、``button`` ノードにハンド
  ラーを登録している。文書内のボタン以外の部分をクリックしてもハンドラーは実行さ
  れない。

  * ノードに ``onclick`` 属性を与えても同様の効果を与えられる。
  * 一般には、イベント名に接頭辞 ``on`` を付けたものを名前とする属性を定義するこ
    とでハンドラーを登録することができる。

* メソッド ``removeEventListener`` はハンドラーを削除する。引数リストは
  ``addEventListener`` と同じだ。

Event objects
======================================================================

* イベントハンドラー関数には引数、すなわちイベントオブジェクトが渡される。これに
  はイベントに関する付加情報が含まれる。例えば、どのマウスボタンが押されたかなど
  を得ることができる。

  .. code:: html

     <button>Click me any way you want</button>
     <script>
       let button = document.querySelector("button");
       button.addEventListener("mousedown", event => {
           if (event.button == 0) {
               console.log("Left button");
           } else if (event.button == 1) {
               console.log("Middle button");
           } else if (event.button == 2) {
               console.log("Right button");
           }
       });
     </script>

* イベントオブジェクトに含まれる情報は、イベントの種類による。
* プロパティー ``type`` は種類によらず共通であり、``"click"`` や ``"mousedown"``
  などの、イベントを特定する文字列を値とする。

Propagation
======================================================================

* イベントタイプの大部分について、ノードに登録されたハンドラーはその子ノードで発
  生したイベントも受け取る。例えば ``<p>`` に含まれる ``<button>`` がクリックさ
  れると、``<p>`` のイベントハンドラーにもクリックイベントがわかる。
* ただし ``<p>`` と ``<button>`` の両方にハンドラーがある場合には、より具体的な
  ハンドラーである ``<button>`` のそれが先に処理される。
* イベントは、発生したノードからその親ノード、さらにその親ノード、……。文書の根へ
  と親の方向に伝わる。
* 最後に登録されているハンドラーすべての順番が回ったあとに、ウィンドウ全体に登録
  されているハンドラーがイベントに応答する。
* イベントハンドラーは、イベントメソッド ``stopPropagation`` を呼び出して、この
  連鎖を断ち切ることがいつでもできる。これは次のような状況で役に立つ：

  .. code:: html

     <p>A paragraph with a <button>button</button>.</p>
     <script>
       let para = document.querySelector("p");
       let button = document.querySelector("button");
       para.addEventListener("mousedown", () => {
           console.log("Handler for paragraph.");
       });
       button.addEventListener("mousedown", event => {
           console.log("Handler for button.");
           if (event.button == 2) event.stopPropagation();
       });
     </script>

* イベントオブジェクトの大半には、イベントがどこのノードから来たのかを参照するプ
  ロパティー ``target`` がある。これを参照することで、予期せぬイベントを誤って処
  理することを回避できる。
* プロパティー ``target`` を使って、特定の型のイベントを広範囲に投げることもでき
  る。次の例では ``<button>`` 一つ一つにハンドラーを登録するのではなく、
  ``document.body`` にハンドラーを登録しておくことで、イベント発生元がボタンのと
  きに限り処理することになる：

  .. code:: html

     <button>A</button>
     <button>B</button>
     <button>C</button>
     <script>
       document.body.addEventListener("click", event => {
           if (event.target.nodeName == "BUTTON") {
               console.log("Clicked", event.target.textContent);
           }
       });
     </script>

Default actions
======================================================================

* イベントの多くには関連した既定の動作がある。次のような例がある：

  * リンク上でならば、クリックすることはリンク先へ移動する。
  * ウィンドウ上でならば、下矢印キーを押すことは画面を下にスクロールする。右ク
    リックすることは、コンテキストメニューが表示する。

* イベントの種類のほとんどでは、既定の挙動を起こす前に JavaScript のイベントハン
  ドラーが呼び出される。イベントメソッド ``preventDefault`` を呼び出すと、このよ
  うなことを禁止できる。

  * これを利用して、独自のキーボードショートカットやコンテキストメニューを実装で
    きる。
  * 禁じ手だが、ユーザーが期待する動作を不当に妨害することができる：

    .. code:: html

       <a href="https://developer.mozilla.org/">MDN</a>
       <script>
         let link = document.querySelector("a");
         link.addEventListener("click", event => {
             console.log("Nope.");
             event.preventDefault();
         });
       </script>

* ブラウザーによっては、まったく横取りできないイベントもある。Chrome では
  :kbd:`Ctrl` + :kbd:`W` は JavaScript では処理できない。

Key events
======================================================================

* キーボードのキーが押されると、ブラウザーはイベント ``"keydown"`` を発生させ、
  離すとイベント ``keyup`` が発生する。

  * ``keydown`` が起こるのはキーが押されたときだけではない。押しっぱなしにしてい
    る間、繰り返し発生する。

* イベントのプロパティー ``key`` を見てキーの種別を確認する。
* :kbd:`Enter` などの特別なキーの場合、キー名が文字列で格納されている。
* :kbd:`Shift` を押しながらキーを押すと、キー名にも影響する。
* 修飾キーも普通のキーと同様にイベントを生成するが、キーの組み合わせを探すときに
  はプロパティー ``shiftKey``, ``altKey``, ``metaKey`` の値を見るといい。

  .. code:: javascript

     window.addEventListener("keydown", event => {
         if (event.key == " " && event.ctrlKey) {
             console.log("Continuing!");
         }
     });

* キーイベントが発生する DOM ノードは、キーが押されるときにフォーカスのある要素
  によって決まる。
* ノードのほとんどはフォーカスを持つことはないが、リンク、ボタン、フォームフィー
  ルドは持つことができる。
* 特にフォーカスされているノードがないときには ``document.body`` がキーイベント
  の対象ノードとして働く。
* ユーザーがテキストを入力しているときに、それが何かを把握するためにキーイベント
  を利用することは問題がある。プラットフォームの一部、特に Android の仮想キー
  ボードでは、入力テキストの種類によってはキーの押し方と合致しない。
* 何かがタイプされたことに気づくには ``<input>`` タグや ``<text>`` タグなどの入
  力可能な要素が必要だ。これらの要素は、ユーザーが内容を変更するたびに ``input``
  イベントを発射する。
* 実際の入力内容を読み取る最良の方法は、フォーカスされているフィールドから直接読
  むことだ。

Pointer events
======================================================================

画面上にある物を指示する方法には二つの主流がある。これらは異なる種類のイベントを
発生する。

* マウス（タッチパッドやトラックボール等、マウス風に動作する機器を含む）
* タッチスクリーン

Mouse clicks
----------------------------------------------------------------------

マウスボタンを押すとさまざまなイベントが発射する。

* ``mousedown`` と ``mouseup`` イベントがあり、キーイベントの ``keydown`` と
  ``keyup`` イベントにそれぞれ似ている。
* ``mouseup`` イベントの後 ``click`` イベントが、マウスボタンを押すのと離すのと
  の両方が起こった最もそれらしいノードで発射する。例えば、あるノードでマウスボタ
  ンを押した後、別のノードにポインターを移動させてボタンを離すと、``click`` イベ
  ントはその両者を含むノードで起こる。
* クリックが二度近接して起こると、一つの ``dblclick`` イベントもまた発射する。そ
  れは二度目の ``click`` イベントの後に発射する。

マウスイベントが発生した位置についての正確な情報は、

* イベントのプロパティー ``clientX``, ``clientY`` を参照することで得られる。この
  座標はウィンドウの左上隅を原点とする座標系における、ピクセル単位で表された座標
  だ。
* あるいは ``pageX``, ``pageY`` を用いる。この座標は文書全体の左上隅を原点とする
  座標系におけるピクセル単位で表された座標だ。

Mouse motion
----------------------------------------------------------------------

マウスポインターが動くごとにイベント ``mousemove`` が発射する。このイベントが有
用なのは、マウスドラッグ機能を実装する場合だろう。

.. code:: html

   <p>Drag the bar to change its width:</p>
   <div style="background: orange; width: 60px; height: 20px">
   </div>

   <script>
     let lastX; // Tracks the last observed mouse X position
     let bar = document.querySelector("div");
     bar.addEventListener("mousedown", event => {
         if (event.button == 0) {
             lastX = event.clientX;
             window.addEventListener("mousemove", moved);
             event.preventDefault(); // Prevent selection
         }
     });

     function moved(event) {
         if (event.buttons == 0) {
             window.removeEventListener("mousemove", moved);
         } else {
             let dist = event.clientX - lastX;
             let newWidth = Math.max(10, bar.offsetWidth + dist);
             bar.style.width = newWidth + "px";
             lastX = event.clientX;
         }
     }
   </script>

* ``mousemove`` ハンドラーを ``window`` に登録していることに注意する。たとえバー
  のリサイズ中にマウスが外に飛び出したとしても、ボタンが押されている限りはバーの
  サイズを更新したいのだ。
* そして、マウスボタンが離されたときにサイズ変更を止めたい。そのために、現在押さ
  れているボタンを知らせてくれるプロパティー ``buttons`` を使うことができる。

  * この値がゼロならばボタンは何も押されていない。
  * 押されているボタンがあれば、この値はそのボタンのコードの和を表す。コードは次
    のとおり：

    * 左 1
    * 右 2
    * 中 4

Touch events
----------------------------------------------------------------------

タッチスクリーンに対する接触操作は、それ特有のイベントを発射する。

* 指が画面に触れ始めると ``touchstart`` イベントが起こる。
* 接触中に指を動かすと ``touchmove`` イベントが起こる。
* 画面に接触するのをやめると ``touchend`` イベントが起こる。

タッチスクリーンの多くが同時に複数の指を検出できるので、これらのイベントに単一の
座標の集合が関連付けられるというものではない。イベントオブジェクトのプロパティー
``touches`` というのがあり、これは座標の配列のような要素を値とする。

* 配列要素の成分は ``clientX``, ``clientY``, ``pageX``, ``pageY`` という。

次の例は、画面を指すごとに赤い丸を描くというものだ：

.. code:: html

   <style>
     dot { position: absolute; display: block;
     border: 2px solid red; border-radius: 50px;
     height: 100px; width: 100px; }
   </style>

   <p>Touch this page</p>

   <script>
     function update(event) {
         for (let dot; dot = document.querySelector("dot");) {
             dot.remove();
         }

         for (let i = 0; i < event.touches.length; i++) {
             let {pageX, pageY} = event.touches[i];
             let dot = document.createElement("dot");
             dot.style.left = (pageX - 50) + "px";
             dot.style.top = (pageY - 50) + "px";
             document.body.appendChild(dot);
         }
     }
     window.addEventListener("touchstart", update);
     window.addEventListener("touchmove", update);
     window.addEventListener("touchend", update);
   </script>

* このイベントにおいても ``preventDefault`` を呼び出すことが有用なことがある。

Scroll events
======================================================================

* 要素がスクロールされると ``scroll`` イベントが発射する。
* 以下の例は、文書上にプログレスバーを描き、スクロールダウンするとそれが満たされ
  るように更新する：

  .. code:: html

     <style>
       #progress {
           border-bottom: 2px solid blue;
           width: 0;
           position: fixed;
           top: 0; left: 0;
       }
     </style>

     <div id="progress"></div>

     <script>
       // Create some content
       document.body.appendChild(document.createTextNode(
           "supercalifragilisticexpialidocious ".repeat(1000)));

       let bar = document.querySelector("#progress");
       window.addEventListener("scroll", () => {
           let max = document.body.scrollHeight - innerHeight;
           bar.style.width = `${(pageYOffset / max) * 100}%`;
       });
     </script>

  * 要素の ``position`` を ``fixed`` とすると、絶対位置のように動作するが、文書
    の残りの部分と共にスクロールするのを防ぎもする。すると、プログレスバーが上部
    に留まるようになる。
  * プログレスバーの幅は、進行状況を示すために変更される。ここで単位として
    ``px`` ではなく ``%`` としている。要素がページ幅に対して相対的なサイズになる
    ようにしてある。
  * 大域変数 ``innerHeight`` はウィンドウの高さを値とする。この値はスクロール可
    能な高さの合計値から減算した値でなければならない。
  * ウィンドウの幅を表す ``innerWidth`` もある。現在のスクロール位置である
    ``pageYOffset`` を最大スクロール位置で除算して100 倍すれば、進行状況の百分率
    を得る。

スクロールイベントで ``preventDefault`` を呼び出しでも、それは防げられない。実
は、イベントハンドラーはスクロールが行われたあとに呼び出される。

Focus events
======================================================================

* 要素がフォーカスされると、ブラウザーはその要素にイベント ``focus`` を発射す
  る。
* 要素がフォーカスされなくなると、その要素にイベント ``blur`` が発射する。
* これまでのイベントとは異なり、この二つのイベントは親要素に伝導しない。子要素が
  フォーカスを得たり失ったりしても親要素のハンドラーにはそれが通知されない。

次の例は、フォーカスされているテキストフィールドのヘルプを表示する：

.. code:: html

   <p>Name: <input type="text" data-help="Your full name"></p>
   <p>Age: <input type="text" data-help="Your age in years"></p>
   <p id="help"></p>

   <script>
     let help = document.querySelector("#help");
     let fields = document.querySelectorAll("input");

     for (let field of Array.from(fields)) {
         field.addEventListener("focus", event => {
             let text = event.target.getAttribute("data-help");
             help.textContent = text;
         });
         field.addEventListener("blur", event => {
             help.textContent = "";
         });
     }
   </script>

* ユーザーがブラウザー、すなわち文書が表示されているウィンドウに出入りすると、オ
  ブジェクト ``window`` はイベント ``blur``, ``focus`` を受け取る。

Load event
======================================================================

ページのロードが完了すると、イベント ``load`` が ``window`` と ``document.body``
で発射する。

* このイベントは、文書全体の構築完了を必要とする初期化アクションをスケジュールす
  るのによく使われる。特に ``<script>`` タグの内容は、そのタグが現れるとすぐに実
  行されるので、場合によっては早過ぎる可能性がある。
* ``<img>`` や ``<script>`` タグなど、外部ファイルをロードする要素にも ``load``
  イベントがあり、その外部ファイルがロードされたことを示す。
* イベント ``load`` は親ノードに伝導しない。

ページが閉じられたり、リンクをたどって出ていったりすると、イベント
``beforeunload`` が発射する。

* このイベントの主な用途は、ユーザーが文書を閉じて誤って作業を失うことを防止する
  ことだ。
* もし、このイベントを ``preventDefault`` して、イベントのプロパティー
  ``returnValue`` に文字列をセットすると、ブラウザーはユーザーにダイアログボック
  スを表示して、本当にページを離れるつもりなのかを確認する。

  * 悪質なサイトが怪しい広告を表示するなど、この機能を悪用するため、近頃のブラウ
    ザーはこのダイアログボックスを表示しなくなった。

Events and the event loop
======================================================================

イベントループからすれば、ブラウザーのイベントハンドラーは非同期通知のように振る
舞う。イベントハンドラーはイベントが起こるときにスケジュールに入るが、実行中の他
のスクリプトが完了するのを待機しなければ、自分が実行する機会を得られない。

* イベントは他に何も実行されていないときにしか処理されないということだ。
* イベントループが他の作業と結びついている場合、それを処理する時間ができるまで、
  ページとの相互作用が遅延する。
* 長時間実行されるイベントハンドラーか、短時間でもイベントハンドラーがたくさんあ
  ると、仕事を増やし過ぎればページが重くなり使いにくくなる。

どうしても時間のかかる処理をページを固まらせることなくバックグラウンドでしたい場
合には、ブラウザーには Web ワーカーというものを提供する。

* :dfn:`ワーカー` とは JavaScript プロセスであって、メインスクリプトと並行して実
  行されるものをいう。これはそれ独自のタイムライン上で走る。

例を出す。数の平方を計算することは重く、長時間を要するものであり、これを別のス
レッドで実行したいとする。そこで :file:`code/squareworker.js` というスクリプトを
書き、メッセージに応答して平方を計算し、メッセージを返すようにする。

.. code:: javascript

   addEventListener("message", event => {
       postMessage(event.data * event.data);
   });

* ワーカーは大域名前空間やその他データをメインスクリプトの環境と共有しない。その
  代わりに、ワーカーとはメッセージをやり取りして通信する必要がある。

次のコードはスクリプトを実行しているワーカーを作り出し、メッセージをいくつか送信
して、応答を出力する：

.. code:: javascript

   let squareWorker = new Worker("code/squareworker.js");
   squareWorker.addEventListener("message", event => {
       console.log("The worker responded:", event.data);
   });

   squareWorker.postMessage(10);
   squareWorker.postMessage(24);

* メソッド ``postMessage`` はメッセージを送信する。このメッセージは ``message``
  イベントを受信側に発射する。
* ワーカーを作成したスクリプトは ``Worker`` オブジェクトを通じてメッセージを送受
  信する。
* その大域名前空間上で直接送受信することで、そのスクリプトと対話する。
* JSON として表現できる値しかメッセージとして送信することができない。相手は値そ
  のものではなく、そのコピーを受信する。

Timers
======================================================================

* 関数 ``setTimeout`` はすでに第 11 章で見た。指定したミリ秒後に指定した関数を呼
  び出されるようにするというものだ。
* 時々この関数のスケジュールを取り消したいことがある。それには ``setTimeout`` の
  戻り値を保存しておき、それを関数``clearTimeout`` に引き渡して呼び出せばよい。

  .. code:: javascript

     let bombTimer = setTimeout(() => {
         console.log("BOOM!");
     }, 500);

     if (Math.random() < 0.5) { // 50% chance
         console.log("Defused.");
         clearTimeout(bombTimer);
     }

* 関数 ``cancelAnimationFrame`` は上記 ``clearTimeout`` と同じように機能する。こ
  の関数を関数 ``requestAnimationFrame`` を呼び出したときの戻り値を実引数として
  呼び出すと、そのフレームを（まだ呼び出されていなければ）取り消す。
* 関数 ``setInterval``, ``clearInterval`` は繰り返しタイマーを設定するために用い
  られる。指定のミリ秒間隔で何かを繰り返させるものだ。

  .. code:: javascript

     let ticks = 0;
     let clock = setInterval(() => {
         console.log("tick", ticks++);
         if (ticks == 10) {
             clearInterval(clock);
             console.log("stop.");
         }
     }, 200);

Debouncing
======================================================================

イベント ``mousemove`` や ``scrollevent`` のように、急速に連続発射されがちなイベ
ントに対するイベントハンドラーを、時間を食うようなものにしないことが肝要だ。そう
しないと、文書との相互作用が始まるのが遅いと感じさせてしまう。

そのようなイベントハンドラーで何か自明でないことをする必要があるならば、関数
``setTimeout`` を利用してそれを頻繁に行わないようにする。このことをイベントの
debouncing という。これにはわずかに違うアプローチがいくつかある。

次に示す最初の例では、ユーザーが何かを入力したときに反応をしたいのだが、入力イベ
ントごとに直ちにそうしたいわけではない。

* ユーザーが素早く入力しているときには、一時停止が起こるまで待ちたい。
* イベントハンドラーではなく、タイムアウトを設定する。

  * 前回のタイムアウトがもしあればそれも解除する。
  * タイムアウト遅延よりも短いようなイベントが近接して発生した場合、直前のタイム
    アウトも解除する。

.. code:: html

   <textarea>Type something here...</textarea>
   <script>
     let textarea = document.querySelector("textarea");
     let timeout;
     textarea.addEventListener("input", () => {
         clearTimeout(timeout);
         timeout = setTimeout(() => console.log("Typed!"), 500);
     });
   </script>

* 関数 ``clearTimeout`` については、以下のものを実引数とする場合を気にする必要は
  ない：

  * 値 ``undefined``
  * すでにタイムアウトしているもの

  したがって ``clearTimeout`` を呼び出すタイミングにも注意する必要はない。

応答間隔を一定時間以上空けたいが、一連のイベントの間で発射したい場合は、少し異な
るパターンを使うことができる。たとえば、マウスの現在の座標を表示すること
で、"mousemove " イベントに 250ms ごとに応答したいとする。次のコードはそれを実現
する：

.. code:: javascript

   let scheduled = null;
   window.addEventListener("mousemove", event => {
       if (!scheduled) {
           setTimeout(() => {
               document.body.textContent = `Mouse at ${scheduled.pageX}, ${scheduled.pageY}`;
               scheduled = null;
           }, 250);
       }
       scheduled = event;
   });

Summary
======================================================================

* イベントハンドラーは Web ページ内で発生したイベントを検出し、反応することを可
  能にする。
* メソッド ``addEventListner`` はハンドラーを登録するのに使う。
* イベントには ``keydown`` や ``focus`` などの、種類を識別するものがある。
* イベントの大部分は特定の DOM 要素で呼び出されて、その祖先に向かって伝わる。そ
  れらの要素に関連付けられたハンドラーがイベントを処理できる。
* イベントハンドラーが呼び出されると、イベントに関する追加情報であるイベントオブ
  ジェクトが渡される。このイベントオブジェクトには次のようなメソッドがある：

  * ``stopPropagation``: イベントのさらなる伝導を停止する。
  * ``preventDefault``: ブラウザーの既定の処理を禁止する。

* キーを押すとイベント ``keydown`` と ``keyup`` が発射する。
* マウスボタンを押すとイベント ``mousedown``, ``mouseup``, ``click`` が発射す
  る。
* マウスが移動するとイベント ``mousemove`` が発射する。
* タッチスクリーンの相互作用ではイベント ``touchstart``, ``touchmove``,
  ``touch`` が発射する。
* スクロールはイベント ``scroll`` で検出される。
* フォーカスの変化はイベント ``focus`` と ``blur`` で検出される。
* 文書がロードを完了するとイベント ``load`` がウィンドウに対して発射する。

Exercises
======================================================================

Balloon
----------------------------------------------------------------------

**問題** 吹き出しを表示するページを書け（絵文字🎈を使用）。上矢印を押すと 10% 膨
らみ、下矢印を押すと 10% 縮むようにしろ。

* 親要素の ``font-size`` (``style.fontSize``) で、テキストのサイズを制御できる。
  値には単位を含めることを忘れるな。
* 矢印キーのキー名は ``ArrowUp`` と ``ArrowDown`` だ。ページをスクロールすること
  なく、風船だけを変更するようにしろ。

これがうまくいったら、風船をある大きさ以上に膨らませると、爆発する機能を追加し
ろ。この場合、爆発するということは、風船が絵文字💥に置き換えられ、イベントハンド
ラーは削除される（これ以上爆発を膨らませたり縮めたりできないように）。

**解答** 前半と後半をまとめて：

.. code:: html

   <span id="baloon" style="font-size: 100px;">🎈</span>
   <script>
       function resizeBaloon(event){
           const baloon = document.querySelector("span#baloon");
           const fontSize = baloon.style.fontSize;
           const size = fontSize.replace(/\D+/, '');
           const unit = fontSize.replace(/\d+/, '');
           if(event.key == "ArrowUp"){
               updateBaloon(baloon, Math.floor(size * 1.1), unit);
               event.preventDefault();
           }
           else if(event.key == "ArrowDown"){
               updateBaloon(baloon, Math.floor(size * 0.9), unit);
               event.preventDefault();
           }
       }
       function updateBaloon(baloon, size, unit){
           baloon.style.fontSize = size + unit;
           console.log(baloon.style.fontSize);
           if(size > 150){
               console.log("explode");
               const newSpan = document.createElement("span");
               newSpan.setAttribute("id", "newSpan");
               newSpan.setAttribute("style", `font-size: ${baloon.style.fontSize}`);
               newSpan.appendChild(document.createTextNode("💥"));
               baloon.parentNode.replaceChild(newSpan, baloon);
               window.removeEventListener("keyup", resizeBaloon);
           }
       }

       window.addEventListener("keyup", resizeBaloon);
   </script>

* ``replaceChild`` の利用例が本書中にまだないので、そこに手間取った。
* 爆発後のノードのスタイルを爆発前のそれの複製にしたいが方法が不明。

Mouse trail
----------------------------------------------------------------------

JavaScript の黎明期はアニメーションを多用した派手なページが全盛の時代だった。そ
れが流行していた頃、この言語を使って実に刺激的な方法が考案された。そのようなもの
の一つにマウス軌跡がある。ページ上でマウスポインターを動かすと、それを追う一連の
要素だ。

**問題** マウス軌跡を実装しろ。サイズと背景色が固定された絶対配置の ``<div>`` 要
素を使え。例として Mouse clicks セクションのコードを参照しろ。このような要素をた
くさん作り、マウスが動いたときに、マウスポインターの軌跡の中にそれらを表示しろ。

これに対しては様々な方法論が考えられる。最初に行う簡単な方策は、一定数の軌跡要素
を保持し、イベント ``mousemove`` が発生するたびに次の要素をマウスの現在位置に移
動させるというサイクルを行うというものだ。

**解答** 軌跡の尻尾の色を減衰させるなどして派手にすることもできるが単純にする：

.. code:: html

   <style>
   .dot {
       height: 8px; width: 8px;
       border-radius: 4px;
       background: deeppink;
       position: absolute;
   }
   </style>
   <script>
       const numDots = 20;

       window.addEventListener("mousemove", event => {
           const dots = document.querySelectorAll("div.dot");
           const dot = document.createElement("div");
           dot.className = "dot";
           dot.style.left = event.x + "px";
           dot.style.top = event.y + "px";
           if(dots?.length >= numDots){
               document.body.removeChild(dots[0]);
           }
           document.body.appendChild(dot);
       });
   </script>

Tabs
----------------------------------------------------------------------

タブ付きパネルは、ユーザーインターフェースで広く使われている。タブパネルでは、要
素の上に突き出た複数のタブから選択することで、インターフェースパネルを選択するこ
とができる。

**問題** 単純なタブ型インターフェースを実装しろ：DOM ノードを入力とし、そのノー
ドの子要素を表示するタブ付きインターフェイスを出力する関数 ``asTabs`` を書け。

* ノードの先頭に、子要素ごとに、子要素の属性 ``data-tabname`` から取得したテキス
  トを含む ``<button>`` 要素のリストを挿入する。
* 元の子要素のうち一つを除いてすべてを（スタイルで ``display: none`` として）隠
  す。
* 現在表示されているノードは、ボタンをクリックして選択できる。

これがうまくいったら、現在選択されているタブのボタンのスタイルを変えて、どのタブ
が選択されているか明らかになるように拡張しろ。

**解答** 前半だけ解く。汎用性を求めていないので殴り書きのまま提出する。

.. code:: javascript

   function asTabs(node){
       const newNode = document.createElement("div");
       for(const child of node.children){
           child.style.display = "none";
           const tabName = child.getAttribute("data-tabname")
           const button = document.createElement("button");
           button.setAttribute("tab", tabName);
           button.appendChild(document.createTextNode(tabName));
           button.addEventListener("click", event => {
               const tabName = event.target.getAttribute("tab");
               for(let pane of document.querySelectorAll("[data-tabname]")){
                   if(pane.getAttribute("data-tabname") == tabName){
                       pane.style.display = '';
                   }
                   else{
                       pane.style.display = 'none';
                   }
               }
           });
           newNode.appendChild(button);
       }
       return newNode;
   }

* ``event.target`` でイベント発生源を参照できることを忘れていた。
* CSS セレクターはやはり便利だ。

HTML 側ではこういう感じになる：

.. code:: html

   <ul id="tab_target">
     <li data-tabname="Tab0">Pane A</li>
     <li data-tabname="Tab1">Pane B</li>
     <li data-tabname="Tab2">Pane C</li>
     <li data-tabname="Tab3">Pane D</li>
   </ul>
   <script>
   const ui = asTabs(document.getElementById("tab_target"));
   document.body.insertBefore(ui, null);
   </script>

問題の後半は ``updateAllButtons(event.target)`` のような呼び出しで適当にスタイル
を変更するコードを書けばいい。省略。

以上
