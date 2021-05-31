======================================================================
Project: A Platform Game
======================================================================

この章では JavaScript と HTML とで 2D アクションゲームを実装する。

.. contents:: ノート目次

The game
======================================================================

Thomas Palef 作 `Dark Blue <https://www.lessmilk.com/games/10>`__ をベースにゲームを作る。
面白さと最小限主義の両方を兼ね備えていることとと、あまり多くのコードを使わずに作ることができることから選ばれた。

* このゲームの外観は本書 p. 271 の図式のようなものだ。ファミコン的で抽象的だが、これが良い。

  * 暗い四角はプレイヤーを表す。

    * プレイヤーの目標は溶岩を避けつつコインを集めることとする。
    * すべてのコインを回収すれば一面クリアとする。
    * プレイヤーは左右の矢印キーでその方向に歩行することができる。
    * 上矢印でジャンプする。

  * 黄色い四角はコインを表す。
  * 赤いものは溶岩を表す。

* ゲームは格子状に配置された固定背景と、そこに重ねられた何か動く要素から構成される。
* 格子内には空、固形物、溶岩のいずれかを配置する。これらは格子にフィットする。
* 動く要素とは、プレイヤー、コイン、溶岩の一部とし、これらは格子に拘束されず、滑らかに動作して構わない。

The technology
======================================================================

ゲームを描画するのにブラウザー DOM を使い、ユーザー入力を読み取るのにキーイベントを処理することにする。

* 画面やキーボードに関係するコードは、ゲーム全体を作るのに必要な作業のうちのわずかだ。
  ゲーム要素のすべてが色のついた四角なので描画は簡単だ。
  DOM 要素を作成し、適宜スタイルを指定するだけだ。
* 背景は固定グリッドなので、一つの表要素として表現することができる。
  自由に動ける要素は ``position: absolute`` なスタイルを与えて背景に重ねる。

Levels
======================================================================

ステージを設計するのに人間が読み書きできる方法が欲しい。
すべてが格子上から動き始めてもかまわないので、各文字がゲーム要素を表すような大きな文字列を使う。
小さなステージでは次のようなものになる：

.. code:: javascript

   let simpleLevelPlan = `
   ......................
   ..#................#..
   ..#..............=.#..
   ..#.........o.o....#..
   ..#.@......#####...#..
   ..#####............#..
   ......#++++++++++++#..
   ......##############..
   ......................`;

記号の意味を次のようにする：

.. csv-table::
   :delim: !
   :header: 記号, 要素

   ``.`` ! 空
   ``#`` ! 壁とか床
   ``+`` ! 溶岩
   ``@`` ! プレイヤーの開始位置
   ``o`` ! コイン
   ``=`` ! 水平方向に往復する溶岩の塊
   ``|`` ! 垂直方向に移動する溶岩の塊
   ``v`` ! 垂直下向きに落ちる溶岩の滴下

* 溶岩の滴下は下方にしか移動せず、床に衝突すると最初の位置まで跳ねて戻る。

ゲーム全体をプレイヤーがクリアしなければならない複数の面で構成する。

* すべてのコインを回収すると一面クリアとなる。
* プレイヤーが溶岩に接触すると、現在の面をその初期状態に復元し、
  プレイヤーをスタート地点に戻して再挑戦となる。

Reading a level
======================================================================

ステージをオブジェクトとして表現するべくクラス ``Level`` を定義する。
本書 pp. 273-274 参照。

* コンストラクターの引数は、前節で仕様を定めた文字列とする。

  .. code:: javascript

     constructor(plan) {
         let rows = plan.trim().split("\n").map(l => [...l]);
         this.height = rows.length;
         this.width = rows[0].length;
         this.startActors = [];
         this.rows = rows.map((row, y) => {
             return row.map((ch, x) => {
                 let type = levelChars[ch];
                 if (typeof type == "string") return type;
                 this.startActors.push(type.create(new Vec(x, y), ch));
             return "empty";
         });
     });

  * ``rows = plan.trim().split("\n").map(l => [...l])`` で同じ長さの文字列の配列が得られることに注意。
    最終的に ``this.rows`` には文字の配列の配列がセットされる。
  * ``this.width``, ``this.height`` はこの面の寸法のようなものだ。
  * 出演者を背景格子から分離する必要がある。それを ``this.startActors`` に格納したい。

    * 配列メソッド ``map`` の第二引数には、配列のインデックスが渡される。
    * この要素は ``"empty"``, ``"wall"``, ``"lava"`` などが格納されることになる。

  * オブジェクト ``levelChars`` が唐突に用いられている。
    これは背景要素と出演者要素をクラスに写像するためのものだ。

    * ``type`` が出演者クラスのときには、その静的メソッド ``create`` を呼び出してオブジェクトを生成する。
    * ``"."`` に対しては ``"empty"`` を返す。

  * 出演者要素の位置を ``Vec`` オブジェクトで格納する。第 6 章の演習で見たような
    プロパティー ``x``, ``y`` を有するオブジェクトだ。

ゲームが進行すると、出演者要素は別の場所に移動したり、あるいは（コインが回収されるとそうなるように）完全に消滅したりする。
実行中のゲームの状態を追跡するため、クラス ``State`` を定義する。

* コードは本書 pp. 274-275 にある。
* ゲームが終了すると、プロパティー ``status`` が値 ``"lost"`` または ``"won"`` に変化する。

Actors
======================================================================

出演者オブジェクトは、移動している要素の現在の位置と状態を表す。
出演者オブジェクトすべてでインターフェイスが共通だ。

* プロパティー ``pos`` は自身の左上隅座標とする。
* プロパティー ``size`` は自身の寸法とする。
* メソッド ``update`` は、ある時間ステップの後の新しい状態と位置を計算する。
  出演者の行動を予測再現するのに利用する。
* プロパティー ``type`` は、自身の出演者としての型を示す文字列とする。
  これに基づいて出演者を表す矩形の外観を描画する。

  * ``"player"``
  * ``"coin"``
  * ``"lava"``

* 出演者クラスには静的メソッド ``create`` があり、これを ``Level`` コンストラクターが呼び出す。

----

クラス ``Vec`` を定義する。ノート割愛。

----

ここから出演者種別に応じたクラスを定義していく。メソッド ``update`` は後回し。

----

クラス ``Player`` (p. 276) は力学的な運動を再現するために位置と速度を保持する。

* コンストラクターは自明なものになる。
* メソッド ``get type`` は文字列 ``"player"`` を返す。
* 静的メソッド ``create`` は位置を受け取るだけとする。

  * プレイヤーの高さは 1.5 ブロック分なので、初期位置を "@" の位置から半ブロック上に設定する。
    こうすると出現したブロックの底辺とぴったり合う。

* 最後に、クラススコープの外で ``Player.prototype.size`` を適当な ``Vec`` に設定する。
  プロトタイプを利用することは、このプロパティーが全オブジェクトで共通であることから必然だ。

----

``Lava`` (p. 276) を構築するときには、基となっているキャラクターに応じた異なる方法でオブジェクトを初期化する必要がある。

* 活動的な溶岩は障害物に当たるまで速度を保って移動する。
* その時点で、溶岩にプロパティー ``reset`` があれば最初の位置に跳び戻る。
* そうでない場合は速度を反転させ逆方向に戻っていく。
* 静的メソッド ``create`` はコンストラクターで受け取った記号を見て、正しい溶岩を作成する。

----

``Coin`` (pp. 277-278) は比較的単純で、ほどんどその場にいるだけだ。

* ただし演出としてわずかに垂直方向に振動させることにする。
  この運動を追跡するためにコインオブジェクトには基本位置と、振動の位相を追跡するプロパティー ``wobble`` を持たせる。
  これらを組み合わせてコインの実際の位置 ``pos`` を決定する。
* コインすべてが同期して振動するような状況を避けたいので、各コインの初期位相をランダムにする。

----

これで先述のオブジェクト ``levelChars`` を定義できる。
``Level`` オブジェクトを生成するのに必要な部品を全て与える。

.. code:: javascript

   const levelChars = {
       ".": "empty",
       "#": "wall",
       "+": "lava",
       "@": Player,
       "o": Coin,
       "=": Lava,
       "|": Lava,
       "v": Lava
   };

   let simpleLevel = new Level(simpleLevelPlan);
   console.log(`${simpleLevel.width} by ${simpleLevel.height}`); // → 22 by 9

Encapsulation as a burden
======================================================================

この章のコードはカプセル化についてほとんど考慮していない。その理由は：

* コードを掲載する紙幅をそれほど割くことが出来ない。
* カプセル化には余分な労力がかかる。プログラムが大きくなり、
  さらなる概念やインターフェイスの導入に迫られる。
  厳密なインターフェイスによる分離に適したシステムの切り口もあれば、そうでないものもある。
  不適切なものをカプセル化することは、多くのエネルギーを浪費することになる。
* このゲームのさまざまな要素が密接に結合している。

次の章で、このゲームを別の方法で描画する予定なので、描画システムだけはカプセル化する。

* 描画をインターフェイスの背後に置くことで、同じゲームプログラムをそこにロードして、
  別の描画モジュールをプラグインすることができる。

Drawing
======================================================================

描画オブジェクトを定義することで描画コードをカプセル化して、ステージと状態を表示する。
この章で定義する表示タイプは DOM 要素を使ってステージを見せるので ``DOMDisplay`` という。

スタイルシートを使って、ゲーム要素の実際の色やその他固定プロパティーを設定する。

* ゲーム要素を作成する際に、そのスタイルプロパティーを直接設定することもできるが、
  プログラムが冗長になる。

次の補助関数 (p.280) は要素を作成して、属性と子ノードを与える簡単な手段となる：

.. code:: javascript

   function elt(name, attrs, ...children) {
       let dom = document.createElement(name);
       for (let attr of Object.keys(attrs)) {
           dom.setAttribute(attr, attrs[attr]);
       }
       for (let child of children) {
           dom.appendChild(child);
       }
       return dom;
   }

* クラス ``DOMDisplay`` (p. 280)

  * ``DOMDisplay`` オブジェクトは、それを追加するべき親要素と ``Level`` オブジェクトを与えると作成される。
  * メソッド ``clear`` は DOM オブジェクトのメソッド ``remove`` を呼び出す。
  * ステージの背景格子は変更されることがないので一度だけ描画する。
  * 出演者はその表示が与えられた状態に行進されるごとに再描画される。
  * プロパティー ``actorLayer`` は、出演者を保持する要素を追跡して、容易に取り外したり置き換えたりできるようにするために使う。

関数 ``drawGrid`` (pp. 280-281) で背景の格子を描く。

* 座標や寸法は格子のブロック単位で追跡する。
  ピクセル単位を設定するときには、この座標を拡大する必要がある。
* 定数 ``scale`` は一ブロックが画面に占めるピクセル数を表す。
* 背景は ``<table>`` 要素として描かれる。これは ``Level`` のプロパティー ``rows`` の構造とよく合っており、

  * 格子の各行が表の行要素 ``<tr>`` になる。
  * 格子内の文字列はセル要素 ``<td>`` のクラス名として用いる。

* 演算子 ``...`` は子ノードの配列を別の実引数として関数 ``elt`` に渡すためにある。

表を我々が欲しいように見せる CSS コードが本書の p. 281 にある。スタイリングの説明があるが割愛。

* 関数 ``drawActor`` (pp. 281-282)

  * 各出演者を描画するには、それ用の DOM 要素を作成してプロパティーを適宜設定する。
  * 途中のピクセル単位系を必要とする箇所では、先ほどの定数 ``scale`` を参照する。

メソッド ``syncState`` (p. 282) は特定の状態を表示させるために呼び出す。

.. code:: javascript

  DOMDisplay.prototype.syncState = function(state) {
      if (this.actorLayer) this.actorLayer.remove();
      this.actorLayer = drawActors(state.actors);
      this.dom.appendChild(this.actorLayer);
      this.dom.className = `game ${state.status}`;
      this.scrollPlayerIntoView(state);
  };

* 最初に、古い出演者の絵があればそれを消去し、次に出演者を新しい位置に再描画する。
* ステージの現在の状態をクラス名としてラッパーに追加することで、
  ゲームに勝ったときと負けたときとでプレイヤーのスタイルを変えることができる。

  .. code:: css

     .lost .player {
         background: rgb(160, 64, 64);
     }
     .won .player {
         box-shadow: -4px -7px 8px white, 4px -7px 8px white;
     }

  * 溶岩に接触するとプレイヤーの色が暗い赤に変わる。
  * 最後のコインを回収すると、左上と右上にぼかした白い影を付けて後光のように見せる。

* ビューポートにステージが収まっているとは限らないので、
  メソッド ``scrollPlayerIntoView`` の呼び出しが必要となる。

  * ステージがビューポートの外にはみ出している場合には、ビューポートをスクロールして
    プレイヤーがビューポートの中心に来るように調整する。

    * それを CSS の ``.game`` で実現している。特に ``overflow: hidden`` に注意。
      さらに ``position: relative`` も効いている。

メソッド ``scrollPlayerIntoView`` (pp. 283-284) ではプレイヤーの位置を見つけてラッピング要素のスクロール位置を更新する。
位置の変更には、要素のプロパティー ``scrollLeft`` と ``scrollTop`` を変更する。

* 出演者の中心を求めるには、その位置に寸法の半分を加算する。
  途中までステージ座標系で計算し、最後に ``scale`` を乗じてピクセル座標系に変換する。
* プレイヤーの位置が許容範囲の外側にいないかなどを検める。
* 画面中央部にスクロールに関して中立な領域があると、多少の動作でスクロールしなくなって快適だ。

これで小さなステージを表示することができるようになった。

.. code:: html

   <link rel="stylesheet" href="css/game.css">
   <script>
     let simpleLevel = new Level(simpleLevelPlan);
     let display = new DOMDisplay(document.body, simpleLevel);
     display.syncState(State.start(simpleLevel));
   </script>

Motion and collision
======================================================================

これでゲームに動きを加えられるところまでたどり着いた。
この種のゲームのほどんとが採用する基本的なアプローチとは、
時間を短時間の区間に分割して、その区間ごとに速度と時間の積だけ出演者を動かすというものだ。

* 時間を秒単位で計測するので、速度は秒速で表される。

物を動かすことは容易い。難しいのは物体間の相互作業を扱うことだ。

* プレイヤーが壁や床に当たるときには、それを通り抜けてはいけない。プレイヤーを止める必要がある。
* コインに当たった場合は、それを回収しなければならない。
* 溶岩に当たったらミスにしないといけない。

物理エンジンなどは使えないから、この章では矩形の物体間の衝突しか扱わない。かなり単純な方法で処理する。

プレイヤーや溶岩の塊を動かす前に、その動きが壁の内側に入るかどうかをテストする。
入る場合には、その動きを単に取り消す。このような衝突への対応は出演者によって異なる。

* プレイヤーは停止する。
* 溶岩の塊は跳ね返る。
* この方法だと、物体が実際に接触する前に運動停止してしまうので、時間区間を相当小さくすることが求められる。
* もう一つの方法は、より良いものだがより複雑だ。正確な接触点を見つけてそこに動かすことだ。

ここでは単純な方法を採用する。アニメーションが小ステップで進むようにすることで、この問題を隠す。

ある矩形が指定する種類の格子要素に接触するかどうかを判定するメソッド (p．286) だ。

.. code:: javascript

   Level.prototype.touches = function(pos, size, type) {
       let xStart = Math.floor(pos.x);
       let xEnd = Math.ceil(pos.x + size.x);
       let yStart = Math.floor(pos.y);
       let yEnd = Math.ceil(pos.y + size.y);

       for (let y = yStart; y < yEnd; y++) {
           for (let x = xStart; x < xEnd; x++) {
               let isOutside = x < 0 || x >= this.width ||
                               y < 0 || y >= this.height;
               let here = isOutside ? "wall" : this.rows[y][x];
               if (here == type) return true;
           }
       }
       return false;
   };

* 引数の ``pos`` と ``size`` がテストしたい物体の矩形を指定する。
* ``Math.floor`` や ``Math.ceil`` も使って、物体が重なる格子の集合を計算する。
* 一致する格子があれば ``true`` を返す。

----

クラス ``State`` のメソッド ``update`` (pp. 286-287) では
クラス ``Level`` のメソッド ``touches`` を用いてプレイヤーが溶岩に接触しているかどうかを理解する。

.. code:: javascript

   State.prototype.update = function(time, keys) {
       let actors = this.actors.map(actor => actor.update(time, this, keys));
       let newState = new State(this.level, actors, this.status);

       if (newState.status != "playing") return newState;

       let player = newState.player;
       if (this.level.touches(player.pos, player.size, "lava")) {
           return new State(this.level, actors, "lost");
       }

       for (let actor of actors) {
           if (actor != player && overlap(actor, player)) {
               newState = actor.collide(newState);
           }
       }
       return newState;
   };

* 引数は時間ステップと、押されているキーが何であるかを表すデータだ。
* 最初に出演者すべてに対してメソッド ``update`` を呼び出す。更新された出演者の配列を得る。

  * 出演者は時間ステップ、キー、状態をも得る。それに基づいて更新することができるようになる。
  * 実際にはプレイヤーしかキーを読み取らない。キーボードで制御されるただ一つの出演者だ。

* ゲームがすでに終了しているならば、それ以上の処理は必要ない。
* ゲームが途中ならば、プレイヤーが背景の溶岩に触れているかどうかをテストする。

  * 触れているならば負けでゲーム終了とする。
  * 他の出演者がプレイヤーに重なっているかをテストする。

----

出演者同士の重なり合いを関数 ``overlap`` (p. 287) で検出する。
二つの出演者オブジェクトを引数にとり、それらが接触し合っていると ``true`` を返す。
各座標軸同士で重なっている場合がそうだ。

* 素朴な boundary box 同士の比較なので引用省略。

----

いずれかの出演者が重なり合うときは、その出演者のメソッド ``collide`` (p. 288) で状態を更新する機会だ。

* 溶岩出演者にふれるとゲーム状態は ``"lost"`` になる。
* コインは触れると消滅する。ステージ中の最後のコインのときには状態が ``"won"`` になる。

.. code:: javascript

   Lava.prototype.collide = function(state) {
       return new State(state.level, state.actors, "lost");
   };

   Coin.prototype.collide = function(state) {
       let filtered = state.actors.filter(a => a != this);
       let status = state.status;
       if (!filtered.some(a => a.type == "coin")) status = "won";
       return new State(state.level, filtered, status);
   };

Actor updates
======================================================================

``Actor`` オブジェクトのメソッド ``update`` 各種は引数として時間ステップ、状態、キー情報を取る。
これらの変数名を ``time``, ``state``, ``keys`` とする。

----

``Lava`` では ``keys`` を無視する。引数リストにも書かない。

.. code:: javascript

   Lava.prototype.update = function(time, state) {
       let newPos = this.pos.plus(this.speed.times(time));
       if (!state.level.touches(newPos, this.size, "wall")) {
           return new Lava(newPos, this.speed, this.reset);
       } else if (this.reset) {
           return new Lava(this.reset, this.speed, this.reset);
       } else {
           return new Lava(this.pos, this.speed.times(-1));
       }
   };

* 移動距離を計算し、古い位置にそれを加えて新しい位置を計算する。

  * その新しい位置に障害がなければそこに移動する。
  * 障害がある場合、溶岩塊の種類によって動作が異なる。

    * 滴り落ちるタイプのものは ``reset`` 位置がある。そこに戻る。
    * 跳ねるタイプのものは逆方向に動き出すように速度を反転する。

----

コインはメソッド ``update`` (p. 289) を使うことでフラフラと揺らす。
コインについては格子との衝突はない。

.. code:: javascript

   const wobbleSpeed = 8, wobbleDist = 0.07;

   Coin.prototype.update = function(time) {
       let wobble = this.wobble + time * wobbleSpeed;
       let wobblePos = Math.sin(wobble) * wobbleDist;
       return new Coin(this.basePos.plus(new Vec(0, wobblePos)),
                       this.basePos, wobble);
   };

* プロパティー ``wobble`` は時間を追跡するためにインクリメントされ、正弦関数の引数として用いる。
* コインの現在位置はコイン原点と波に基づく変位から計算する。

----

``Player`` の動きは座標軸ごと個別に処理する。
というのは、床に当たるときには水平方向の動きは変わらないし、
壁に当たるときには落下やジャンプの動きは変わらないからだ。

.. code:: javascript

   const playerXSpeed = 7;
   const gravity = 30;
   const jumpSpeed = 17;

   Player.prototype.update = function(time, state, keys) {
       let xSpeed = 0;
       if (keys.ArrowLeft) xSpeed -= playerXSpeed;
       if (keys.ArrowRight) xSpeed += playerXSpeed;
       let pos = this.pos;
       let movedX = pos.plus(new Vec(xSpeed * time, 0));
       if (!state.level.touches(movedX, this.size, "wall")) {
           pos = movedX;
       }

       let ySpeed = this.speed.y + time * gravity;
       let movedY = pos.plus(new Vec(0, ySpeed * time));
       if (!state.level.touches(movedY, this.size, "wall")) {
       pos = movedY;
       } else if (keys.ArrowUp && ySpeed > 0) {
           ySpeed = -jumpSpeed;
       } else {
           ySpeed = 0;
       }
       return new Player(pos, new Vec(xSpeed, ySpeed));
   };

* 水平方向の運動は左右矢印キーの状態から計算する。

  * この動作が作る新しい位置をさえぎる壁がなければ、それを採用する。
  * そうでなければ、古い位置を維持する。

* 垂直方法の運動はさらにジャンプと重力を再現する必要がある。

  * 垂直方法の速度 ``ySpeed`` は重力を考慮して加速する。
  * 床や天井があるかチェックする。何にも当たっていなければ新しい位置を採用する。
    そうでなければ上下方向で場合分けする。

    * 上矢印キーを押された状態でプレイヤーが落ちているときには、
      速度に比較的大きな負の値をセットする。こうするとプレイヤーはジャンプすることになる。
    * そうでない場合には単に何かにぶつかったということなので、スピードをゼロにする。

ゲーム中に現れる重力、ジャンプの初速、その他の定数ほとんどは試行錯誤により設定した。
著者が納得する組み合わせを発見するまで試したとある。

Tracking keys
======================================================================

キーを押している間はずっとその効果（プレイヤーの移動）が持続するようにしたい。

矢印キー各種の現在の状態をとっておくキーハンドラーを仕掛ける必要がある。
また、これらのキーに対してメソッド ``preventDefault`` を呼び出すことで
ブラウザー既定の動作であるページのスクロールを抑止する。

関数 ``trackKeys`` (pp. 290-291) はキーの名前の配列から、それらのキーの現在位置を
追跡するオブジェクトを返す。

* イベント ``keydown`` と ``keyup`` に対するイベントハンドラーを登録し、
* イベントが含むキーコードが追跡中のコードの集合にあれば、オブジェクトを更新する。

.. code:: javascript

   function trackKeys(keys) {
       let down = Object.create(null);
       function track(event) {
          if (keys.includes(event.key)) {
              down[event.key] = event.type == "keydown";
              event.preventDefault();
          }
       }
       window.addEventListener("keydown", track);
       window.addEventListener("keyup", track);
       return down;
   }
   const arrowKeys = trackKeys(["ArrowLeft", "ArrowRight", "ArrowUp"]);

Running the game
======================================================================

* 第 14 章の関数 ``requestAnimationFrame`` がゲームのアニメーションに適した方法を与える。
  しかし、インターフェイスがまったく原始的だ。
  この関数を使用するには、前回の関数を呼び出した時刻を追跡し、
  フレーム（コマ）ごとに関数 ``requestAnimationFrame`` を呼び出す必要がある。

* そこで、これらの退屈な箇所を便利なインターフェイスにラップする補助関数
  ``runAnimation`` (p. 291) を定義する。これを単に呼び出すだけで済むようになる。

  * 引数として、時間差を引数にとり、ワンフレームを描画する関数 ``frameFunc`` を与える。
  * その関数 ``frameFunc`` が ``false`` を返すときには、アニメーションは停止する。

.. code:: javascript

   function runAnimation(frameFunc) {
       let lastTime = null;
       function frame(time) {
           if (lastTime != null) {
               let timeStep = Math.min(time - lastTime, 100) / 1000;
               if (frameFunc(timeStep) === false) return;
           }
           lastTime = time;
           requestAnimationFrame(frame);
       }
       requestAnimationFrame(frame);
   }

* 最大フレームステップは 0.1 秒 に設定した。
* ページが表示されているブラウザーのタブなりウィンドウなりが隠されると、
  関数 ``requestAnimationFrame`` の呼び出しはそれが再度表示されるまで中断される。
  この場合 ``lastTime`` と ``time`` の差は、ページが隠れていた時間丸ごとになる。
  一気にゲームを進行すると、プレイヤーが床から落ちるなどのおかしな副作用が起こるかもしれない。
* この関数は時間を秒に変換してわかりやすくしてある。

----

関数 ``runLevel`` (p. 292) は ``Level`` オブジェクトと表示コンストラクターを引数とし、
``Promise`` を返す。

* ステージを ``document.body`` 内に表示してユーザーにプレイさせる。
* ステージが終了すると、さらに 1 秒待機する。それから表示を消去し、
  アニメーションを停止し、ゲームの終了状態に対する ``Promise`` を解決する。

.. code:: javascript

   function runLevel(level, Display) {
       let display = new Display(document.body, level);
       let state = State.start(level);
       let ending = 1;

       return new Promise(resolve => {
           runAnimation(time => {
               state = state.update(time, arrowKeys);
               display.syncState(state);
               if (state.status == "playing") {
                   return true;
               } else if (ending > 0) {
                   ending -= time;
                   return true;
               } else {
                   display.clear();
                   resolve(state.status);
                   return false;
               }
           });
       });
   }

----

ゲームは一連のステージからなる。

* プレイヤーが死ぬたびに現在のステージがやり直しとなる。
* ステージクリアすると、次のステージに進む。

これを次の非同期関数 ``runGame`` (pp. 292-293) で実現する。
ステージ設計（文字列）の配列と表示コンストラクターを引数にとる。

.. code:: javascript

   async function runGame(plans, Display) {
       for (let level = 0; level < plans.length;) {
           let status = await runLevel(new Level(plans[level]), Display);
           if (status == "won") level++;
       }
       console.log("You've won!");
   }

関数 ``runLevel`` は ``Promise`` を返すので、それを呼び出す当関数は非同期関数として書く。
プレイヤーがゲームを終了したときに解決される別の ``Promise`` を返す。

----

`本書のサンドボックス <https://eloquentjavascript.net/code#16>`__ に変数
``GAME_LEVELS`` で利用可能なステージ設計の集合がある。
このページではそれらを関数 ``runGame`` に与えて実際にゲームを開始する。

.. code:: html

   <link rel="stylesheet" href="css/game.css">
   <body>
   <script>
   runGame(GAME_LEVELS, DOMDisplay);
   </script>
   </body>

Exercises
======================================================================

Game over
----------------------------------------------------------------------

この手のゲームにはプレイヤーは限られたライフでスタートし、死ぬたびにライフが一つ減るという伝統がある。
ライフがなくなると、ゲームは最初から再開となる。

**問題** ``runGame`` を調整してライフを実装しろ。
プレイヤーには三つのライフから開始させろ。
ステージが開始するたびに現在のライフ数を ``console.log`` を使って出力しろ。

**解答** 残機がゼロになると最初のステージからやり直しという意味で実装する：

.. code:: javascript

   const lifeMax = 3;

   async function runGame(plans, Display) {
     let lives = lifeMax;
     for (let level = 0; level < plans.length;) {
         console.log(`1P START. LIFE: ${lives}`);
         const status = await runLevel(new Level(plans[level]), Display);
         if (status == "won") {
             level++;
         }
         else if (status == "lost") {
             lives--;
             console.log("1P FAILED.");
             if (lives == 0) {
                 console.log("1P GAME OVER. RESTART.");
                 level = 0;
                 lives = lifeMax;
             }
         }
     }
     console.log("You've won!");
 }

Pausing the game
----------------------------------------------------------------------

**問題** :kbd:`Esc` キーを押すことでゲームを一時停止したり、解除したりできるようにしろ。
これは関数 ``runLevel`` を別のキーボードイベントハンドラーを使用するように変更し、
:kbd:`Esc` キーが押されるたびにアニメーションを中断または再開することで実現できる。

``runAnimation`` インターフェースは一見するとこのような機能に適していないように見えるが、
``runLevel`` の呼び出し方を変更すればいける。

この機能が動作したら、他にも試せることがある。
これまでのキーボードイベントハンドラーの登録方法には少々問題がある。
オブジェクト ``arrowKeys`` は現在グローバル変数であり、
そのイベントハンドラーはゲームが実行されていなくても維持されている。
これはシステムから漏れているとも言える。
``trackKeys`` を拡張してハンドラーの登録を解除する方法を用意し、
``runLevel`` を変更して、開始時にハンドラーを登録し、終了時に再び登録を解除するようにしろ。

**解答** まず :kbd:`Esc` のハンドラーとフラグをいったんグローバルスコープに定義する：

.. code:: javascript

   let paused = false;

   window.addEventListener("keyup", event => {
       if(event.key != "Escape"){
           return;
       }
       paused = !paused;
       event.preventDefault();
   });

関数 ``runAnimation`` の呼び出しにおいて、実引数のコールバックの最初を次のように変える：

.. code:: javascript

   state = state.update(time, arrowKeys);
   if (paused) {
       return false;
   }

関数 ``runAnimationFrame`` では二箇所を修正する。コールバックが ``false`` を返すときに
ポーズがかかったのならば ``requestAnimationFrame`` に対するコールバックを専用のものに差し替える：

.. code:: javascript

   if (frameFunc(timeStep) === false){
       if (paused) {
           lastTime = time;
           requestAnimationFrame(suspend);
       }
       return;
   }

ポーズ専用コールバックの中身は次のようなものだ：

.. code:: javascript

   function suspend() {
       requestAnimationFrame(paused ? suspend : frame);
   }


後半はまず ``trackKeys`` の終了間際をこうする：

.. code:: javascript

   const untrack = () => {
       window.removeEventListener("keydown", track);
       window.removeEventListener("keyup", track);
   };

   return [down, untrack];

それから ``arrowKeys`` の初期化を ``runLevel`` の序盤に移転する：

.. code:: javascript

   const [arrowKeys, untrack] = trackKeys(["ArrowLeft", "ArrowRight", "ArrowUp"]);

最後に ``Promise`` のコールバックの最後の ``else`` ブロックに
``untrack();`` の呼び出しを追加すればいいだろう。

A monster
----------------------------------------------------------------------

この手のゲームではジャンプして倒すことができる敵がいるという伝統がある。

**問題** そのような出演者タイプをゲームに追加しろ。

これをモンスターと呼ぶ。モンスターは水平方向にしか動かない。
プレイヤーの方向に移動したり、水平方向の溶岩のように跳ね返ったり、
好きな動きのパターンをさせることができる。このクラスは落下の処理をする必要はないが、
モンスターが壁を通らないようにする必要がある。

モンスターがプレイヤーに触れるときの効果は、プレイヤーがモンスターの上に飛び乗っているかどうかによる。
プレイヤーの下半身がモンスターの上半身の近くにあるかどうかをチェックすることでおおよその効果を得られる。
乗っていればモンスターは消え、そうでなければプレイヤーのミスとする。

**解答** TBW
