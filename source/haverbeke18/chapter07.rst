======================================================================
Project: A Robot
======================================================================

グラフを構築して最短経路を探索するような問題を JavaScript で解く。
Dijkstra のアルゴリズムの一つ前のようなものだろうか。

.. contents::

Meadowfield
======================================================================

あまり大きくはない Meadowfield 村には 11 の場所があり、それらの間に 14 の道がある。
この村の道路ネットワークはグラフ理論の意味でのグラフを形成する。

.. todo::

   教科書のコードを Graphviz などで図式にして、画像をここに貼り付けるといいかもしれない。

* 最初の配列 ``roads`` は ``"Alice's House-Bob's House"`` や ``Alice's House-Cabin"``
  のように ``${place1}-${place2}`` という構造の文字列からなる。
* このデータをもとに、次で定義する関数 ``buildGraph`` で隣接リストタイプのグラフ構造にする。

  * ``let graph = Object.create(null)`` で空のグラフを構築する。
    これは ``let graph = {}`` とは異なる。
  * 関数 ``addEdge`` で隣接リストを構築していることが読み取れる。
  * 関数 ``buildGraph`` 末尾のループの感じはよく憶えておきたい。
    配列に対して ``.map()`` を適用した一時配列を反復するというのはスクレイピングではよくある。

.. code:: javascript

   function buildGraph(edges) {
       let graph = Object.create(null);
       function addEdge(from, to) {
           if (graph[from] == null) {
               graph[from] = [to];
           } else {
               graph[from].push(to);
           }
       }

       for (let [from, to] of edges.map(r => r.split("-"))) {
           addEdge(from, to);
           addEdge(to, from);
       }
       return graph;
   }

The task
======================================================================

* 配達ロボットは村じゅうを移動する。上述の場所のあらゆるところに宛先が書かれた小包がある。
* ロボットは小包を見つけるとそれを拾って目的地に着くとそれを着荷する。
* すべての小包を配達した時点でタスクを終了する。

本書の設計方針は、何らかの配達状況をまず管理するというものだ。

* クラス ``VillageState``

  * コンストラクターで場所と小包を引数とする。小包は配列。
  * メソッド ``move`` は目的地を引数とする。

    * グラフを見て、この場所が目的地と隣接しているのならば ``this`` を返す。
    * そうでない場合は小包の場所をチェックすることになる。
      次のようにして新しい ``VillageState`` を返す：

      .. code:: javascript

         let parcels = this.parcels.map(p => {
             if (p.place != this.place) return p;
             return {place: destination, address: p.address};
             }).filter(p => p.place != p.address);
         return new VillageState(destination, parcels);

* 小包は ``place`` と ``address`` を持つ ``object`` であるとする。

このクラスを例えば次のように使う。``roads`` の定義によると郵便局と
Alice の家が隣接しているのでこういう結果となる。

.. code:: javascript

   let first = new VillageState(
       "Post Office",
       [{place: "Post Office", address: "Alice's House"}]
   );
   let next = first.move("Alice's House");
   console.assert(next.place == "Alice's House");
   console.log(next.parcels); // → []
   console.assert(first.place == "Post Office");

* 初期状態では、ロボットが郵便局にいて、小包が届いていないという状況を表す。

Persistent data
======================================================================

* 関数 ``Object.freeze`` は引数のオブジェクトのプロパティーの全てを動的に ``const`` にするような機能だ。
* 本文の感じからすると、これを使うことで何らかの効率上のトレードオフが生じるようだ。

.. code:: javascript

   let object = Object.freeze({value: 5});
   object.value = 10;
   console.assert(object.value == 5);

Simulation
======================================================================

* ``VillageState`` オブジェクトを受け取り、近くにある場所の名前を返す関数として配達ロボットを捉える。
* 物事を記憶し、計画を立てて実行できるロボットを設計したいので、
  ロボットにメモリーを渡し、新しいメモリーを返すようにする。
  そのため、ロボットが返すのは、移動したい方向と、次に移動したときに返されるメモリーの値を含むオブジェクトだ。

.. code:: javascript

   function runRobot(state, robot, memory) {
       for (let turn = 0;; turn++) {
           if (state.parcels.length == 0) {
               console.log(`Done in ${turn} turns`);
               break;
           }
           let action = robot(state, memory);
           state = state.move(action.direction);
           memory = action.memory;
           console.log(`Moved to ${action.direction}`);
       }
   }

* ロボットは小包がある場所をすべて訪れてすべての小包を受け取り、
  小包が宛てられた場所をすべて訪れて小包を届けなければならない。
* ロボットは毎回ランダムな方向に歩く。
* かなりの確率で最終的にすべての小包を見つけて、ある時点で配達すべき場所に到達する。

.. code:: javascript

   function randomPick(array) {
       let choice = Math.floor(Math.random() * array.length);
       return array[choice];
   }

   function randomRobot(state) {
       return {direction: randomPick(roadGraph[state.place])};
   }

* 関数 ``randomPick`` は与えられた配列のランダムなインデックスを返す。

  * ``Math.random()`` は 0 から 1 の間の数字を返す。
  * JavaScript には Python の ``int()`` 相当がないので、わざわざ ``Math.floor()`` を利用することになる。

* 関数 ``randomRobot`` は先述のロボット的関数の一つなので、本来ならば第二引数 ``memory`` があるのだが、
  本関数でそれを利用しないので、前章までのどこかで習ったようにこれを引数リストから削除しても構わない。

ロボットを動かすために、小包いくつかから新しい状態を生成する関数を定義したい。
これをクラス ``VillageState`` の静的メソッドとして実装する。

.. code:: javascript

   VillageState.random = function(parcelCount = 5) {
       let parcels = [];
       for (let i = 0; i < parcelCount; i++) {
           let address = randomPick(Object.keys(roadGraph));
           let place;
           do {
               place = randomPick(Object.keys(roadGraph));
           } while (place == address);
           parcels.push({place, address});
       }
       return new VillageState("Post Office", parcels);
   };

* 宛先と同じ場所から小包が送られてくるわけがない。
  宛名と同じ場所を抽選してしまったら、そうでなくなるまで抽選したい。
  上の ``do`` ループはそれを遂行する。

The mail truck's route
======================================================================

上述のロボット関数は何しろランダムなので効率が悪い。

もし村のすべての場所を一筆書きのように通過する経路を見つけたら、
その経路を二度走らせて確実に配達することができる。
それが郵便局から開始するとして次のようなものだとわかっているとする：

.. code:: javascript

   const mailRoute = [
       "Alice's House", "Cabin", "Alice's House", "Bob's House",
       "Town Hall", "Daria's House", "Ernie's House",
       "Grete's House", "Shop", "Grete's House", "Farm",
       "Marketplace", "Post Office"
   ];

経路をたどるロボットを実装するためには、ロボットに記憶が必要だ。

.. code:: javascript

   function routeRobot(state, memory) {
       if (memory.length == 0) {
           memory = mailRoute;
       }
       return {direction: memory[0], memory: memory.slice(1)};
   }

* 今度のロボット関数は第二引数を使用する。
* ロボットは残りの経路を記憶し、最初の要素を毎ターン切り落とす。

Pathfinding
======================================================================

最短経路を決定するアルゴリズムを書く。

* A から B への経路を探すときには、A から始まるものしか興味がない。
* 同じ場所を 2 回通るような効率の悪いに決まっているルートには興味がない。

.. code:: javascript

    function findRoute(graph, from, to) {
        let work = [{at: from, route: []}];
        for (let i = 0; i < work.length; i++) {
            let {at, route} = work[i];
            for (let place of graph[at]) {
                if (place == to) return route.concat(place);
                if (!work.some(w => w.at == place)) {
                    work.push({at: place, route: route.concat(place)});
                }
            }
        }
    }

* 探索は正しい順序で行う。最初に到達した場所を最初に探索しなければならない。
  到達した場所をすぐに探索することはできない（そこから到達した場所もすぐに探索することになるから）。
* 配列 ``work`` は次に探索すべき場所と、そこに至るまでの経路を配列したものだ。

  * 最初は開始位置と空の経路ルートだけで始める。
  * 検索は、配列の次の項目を取って、そこを探索する。
    つまり、その場所から行くすべての道を調べる。その中の一つがゴールであれば
    完全な経路を返すことができまる。そうでなければ、

    * その場所を見たことがなければ、リストに新しい項目が追加されます。
    * 以前に見たことがあれば、短い経路を最初に見ているので、
      その場所への長い経路か、その場所と同じ経路を見つけたことになる。
      これ以上探索する必要はない。

これを視覚的に想像すると、スタート地点から既知のルートが網の目のように這い出て、四方八方に均等に広がっていく様子がわかります。
（ただし、自分自身に絡みつくことはありません）。

* このコードには作業配列に要素がなくなったときの処理は含まれていない。
  これはグラフが単連結であることを仮定できることによる（任意のノード間に経路が存在することが保証されている）。

本章の最後のロボット関数は次のものだ：

.. code:: javascript

   function goalOrientedRobot({place, parcels}, route) {
       if (route.length == 0) {
           let parcel = parcels[0];
           if (parcel.place != place) {.
               route = findRoute(roadGraph, place, parcel.place);
           } else {
               route = findRoute(roadGraph, place, parcel.address);
           }
       }
       return {direction: route[0], memory: route.slice(1)};
   }

引数 ``route`` は従来のロボット関数と同様に移動方向のリストを意味する。
そのリストが空になるたびに、次の行動を決定する。

* セット内の最初の未配達の小包を受け取り、

  * その小包がまだ拾われていなければ、その小包に向かう経路を計画する。
  * その小包がすでに拾われていれば、まだ配達する必要があるので、代わりに配達先への経路を作成する。

* このロボット関数は ``routeRobot`` よりは若干マシだが、それでも最適とは言えないとのこと。

Exercises
======================================================================

.. todo:: 問題をやるのは後回し。
