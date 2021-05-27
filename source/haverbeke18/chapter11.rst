======================================================================
Asynchronous Programming
======================================================================

この章はひじょうに重要かつかなり難解な内容であるので、しばらくの間見返すことが多くなるだろう。

.. contents:: ノート目次

Asynchronicity
======================================================================

* 同期プログラミングモデルでは、物事は一度に一つずつ起こる。
  長時間動作する関数を呼び出すと、その処理が終了して結果を返せるようになってから戻る。
  つまり、処理時間だけプログラムが停止してしまう。
* 非同期モデルでは、複数のことを同時に行うことができる。
* 同期モデルでは、アクションの終了を待つことは暗黙の了解であるのに対し、
  非同期モデルではプログラム側で明示的に行われるという。
* ブラウザーと Node.js は、スレッドに頼るのではなく、時間のかかる操作を非同期に行う。
  これは一般的に良いことだと考えられている。

途中の図式をよく憶えておくこと。

Crow tech
======================================================================

ここは別に読まなくても何とかなる。

* カラスはひじょうに賢い鳥であり、道具を使ったり、計画を立てたり、記憶したり、
  さらには仲間同士で通信したりすることができる。
* カラスの文明の多くには計算機を作る能力がある。人間のそれとは違い、
  電子ではなく、シロアリのような昆虫の働きにより操作をする。
* これらの機器は通信するのに光の信号を用いる。
  したがって、視覚的な接続が途切れない巣同士でしか通信できない。
* カラスの計算機は JavaScript を実行する。

Callbacks
======================================================================

* 非同期プログラミングの技法の一つに、ゆっくりとしたアクションを行う関数に
  コールバック関数というおまけの引数を与える方法がある。
  アクションが開始して終了すると、コールバック関数が結果とともに呼び出される。

  * Node.js とブラウザーの両方で使用可能である関数 ``setTimeout`` は、
    指定されたミリ秒待機したのち、コールバック関数を呼び出す。

    .. code:: javascript

       setTimeout(() => console.log("Tick"), 500);

    * 待機は一般的にはあまり重要な作業ではないが、
      アニメーションを更新したり、何かが所定の時間より長くかかっているかどうかを
      チェックしたりするような場合には便利だ。

* コールバックを使用して複数の非同期アクションを連続して実行することは、
  アクション後の計算の継続を処理するために、新しい関数を渡し続けなければならないことを意味する。

ほとんどのカラスの巣の計算機には、長期的なデータ保存用の球根があり、
そこでは情報の断片を小枝に表面加工して、後で取り出すことができるようになっている。
表面加工や検索には時間がかかるため、長期保存のためのインターフェイスは非同期で、
コールバック関数を使用している。

球根は JSON でエンコード可能なデータの断片を名前を付けて保存する。
例えば、カラスが食料を隠した場所の情報を "food caches "という名前で保存するとする。
この名前は、実際のキャッシュを示す他のデータを示す名前の配列を保持することができる。
巣 Big Oak の球根にある貯蔵食料を探すために、カラスは次のようなコードを実行する：

.. code:: javascript

   //import {bigOak} from "./crow-tech";
   const {bigOak} = require("./crow-tech");

   bigOak.readStorage("food caches", caches => {
       let firstCache = caches[0];
       bigOak.readStorage(firstCache, info => {
           console.log(info);
       });
   });

* モジュール ``crow-tech`` はサポートページ <https://eloquentjavascript.net/code/#11> にある。
  リンク先の URL をダウンロードしてローカルディスクに保存した上で
  Node.js から上記コードを実行するときには、インポート行をコメントアウトして、
  CommonJS 風のインポート処理に書き換える必要がある。

  以下同様。

* このようなプログラミングでは非同期アクションを行うたびに別の関数に入ってしまい、
  インデントの深さが増す。複数のアクションを同時に実行するなど、
  もっと複雑なことをする場合には少々厄介になる。

カラスの計算機は、リクエストと応答のペアで通信するように作られている。

* これが意味するのは、ある巣が別の巣にメッセージを送り、
  それからすぐにメッセージが送り返され、受信を確認し、
  場合によってはメッセージで質問されたことへの回答を返信することも含む。
* メッセージそれぞれに「タイプ」のタグが付けられており、メッセージの処理方法を決める。
  私たちのコードは、特定のリクエストタイプに対するハンドラーを定義することができ、
  そのようなリクエストが来ると、対応するハンドラーが呼び出されて応答を生成する。

モジュール ``./crow-tech`` がエクスポートするインターフェイスには通信のための
コールバック型関数が備わっている。巣にはリクエストを送信するメソッド ``send`` がある。

.. code:: javascript

    bigOak.send(
        "Cow Pasture",
        "note",
        "Let's caw loudly at 7PM",
        () => console.log("Note delivered."));

* 引数として、対象となる巣の名前、リクエストタイプ、リクエストそのもの、
  応答が来たときのコールバック関数をそれぞれ引き渡す。
* 巣がこのリクエストを受信できるようにするには、この ``note`` というリクエストタイプを定義する必要がある。
* ハンドラーコードはカラスが全ての巣に飛び回ってインストールしていくようなので気にしないものとする。

.. code:: javascript

   //import {defineRequestType} from "./crow-tech";
   const {defineRequestType} = require("./crow-tech");

   defineRequestType("note", (nest, content, source, done) => {
       console.log(`${nest.name} received note: ${content}`);
       done();
   });

* 関数 ``defineRequestType`` は新しいリクエストタイプを定義する。

  * 前述のコードは ``"note "`` リクエストのサポートを追加している。
    これは、単にノートを指定された巣に送信するものだ。
    この実装では ``console.log`` を呼び出し、リクエストが届いたことを
    確認できるようにしている。
* 巣にはプロパティー ``name`` があり、それらの名前を保持する。
* 最後の引数 ``done`` はリクエスト処理が終わったときに呼び出すコールバック関数だ。

  * ハンドラーの戻り値を応答の値として使用した場合には、
    リクエストハンドラー自身は非同期動作を行えないことになる。
    非同期処理を行う関数は、処理が完了する前にふつうは戻り、
    完了時にコールバックが呼び出されるようになっている。
    そのため、応答が利用可能になったときに合図を送るために、
    何らかの非同期機構が（この場合には別のコールバック関数が）必要になる。

ノート：この段階でもう一度先ほどの ``bigOak.send(...)`` を実行してみるとよい。

* 非同期性は伝染する。

  * 非同期に動作する関数を呼び出す関数は、その関数自体も非同期でなければならない。
  * 結果を得るためにコールバックなどの仕組みを使わなければならない。
  * 単に値を返すだけの場合に比べて、コールバックの呼び出しはやや複雑でエラーが発生しやすい。
    プログラムの大部分をそのように構成するのは良いことではない。

Promises
======================================================================

.. note::

   これも併せて読むといい：
   `Promiseを使う - JavaScript | MDN <https://developer.mozilla.org/ja/docs/Web/JavaScript/Guide/Using_promises>`__

* 抽象概念を扱うには、その概念を値で表すことができれば作業が容易になる。
  非同期アクションの場合、未来のある時点で関数が呼ばれるように仕込む代わりに、
  その未来のイベントを表すオブジェクトを返すこともできる。
  これが標準クラス ``Promiss`` だ。

  * ``Promise`` とは非同期アクションであって、ある時点で完了し、値を生成する可能性のあるものだ。
  * ``Promise`` は、その値が利用可能になったときに、興味のある人に通知することができる。

* ``Promise`` を作成する最も簡単な方法は ``Promise.resolve`` を呼び出すことだ。
  この関数は、指定された値が ``Promise`` でラップされているかどうかを確認する。

  * すでに ``Promise`` である場合は、単純にそれを返す。
  * そうでない場合は、指定された値を結果として返すような、
    すぐに終了する新しい ``Promise`` を返す。

  .. code:: javascript

     let fifteen = Promise.resolve(15);
     fifteen.then(value => console.log(`Got ${value}`));

* ``Promise`` オブジェクトから結果を得るにはメソッド ``then`` を使う。

  * 引数には ``Promise`` が解決、値を生成したときに呼び出されるコールバック関数とする。
  * ``Promise`` オブジェクト一つに対して複数のコールバックを追加することができて、
    当該オブジェクトがすでに解決、つまり終了している後に追加したとしても、それらは呼び出される。
  * メソッド ``then`` はさらに次のようなこともする。
    別の ``Promise`` を返し、それはハンドラー関数が返す値に解決するか、
    またはそれが ``Promise`` を返す場合には、それを待機して、
    それからその結果に解決する。

* ``Promise`` が値を非同期の現実に移す装置だと考えると役に立つ。
* 値を promised か否かで分類するという考え方をするようだ：

  * 通常の値は単にそこにあるだけだ。
  * 約束された値とは値であって、すでにそこにあるかもしれないし、
    未来のある時点で現れるかもしれないものだ。
    ``Promise`` で定義された計算は、このようなラップされた値に作用し、
    その値が利用可能になると非同期に実行される。

* ``Promise`` オブジェクトを作成するには、どこか奇妙なインターフェイスのコンストラクターを使用する。

  * 引数として関数を受け取り、それを直ちに呼び出して、
    ``Promise`` の解決に使用できる関数を渡す。
    例えば ``resolve`` メソッドの代わりにこの方法を動作させて、
    ``Promise`` を作成したコードだけがそれを解決するようにできる。

----

関数 ``readStorage`` に対する ``Promise`` ベースのインターフェイスは次のように定義する：

.. code:: javascript

   function storage(nest, name) {
       return new Promise(resolve => {
           nest.readStorage(name, result => resolve(result));
       });
   }

   storage(bigOak, "enemies").then(value => console.log("Got", value));

* ``Promise`` の主な利点が、非同期関数の使用を単純にするということがわかる。
* コールバックを渡す代わりに、通常の関数と同じように引数として入力を受け取り、
  出力を返す。ただし、通常の関数とは出力がまだ得られていない可能性があるという点が異なる。

Failure
======================================================================

* 非同期計算の一部が例外を送出することがある。
* 非同期プログラミングのコールバックスタイルには、
  失敗をコールバックに適切に報告させるようにするのが極端に難しいという問題がある。
* コールバック関数の引数リストを次のようにする：

  * 第 1 引数はアクションが失敗したことを示すために使用される。
  * 第 2 引数にはアクションが成功したときに生成された値が格納される
  * このようなコールバック関数は、例外を受け取ったかどうかを常にチェックし、
    呼び出した関数が送出した例外を含め、コールバック関数が引き起こした問題を捕捉し、
    正しい関数に与えられるようにしなければならない。

* ``Promise`` は resolved か rejected のどちらかになる。

  * 解決時のハンドラーはアクションが成功するとき、かつそのときにしか呼び出されない。
  * 却下時のハンドラーは ``then`` が返す新しい ``Promise`` に自動的に伝導される。

* ハンドラーが例外を送出すると ``then`` の呼び出しが生成する ``Promise`` は
  自動的に却下される。非同期アクションの連鎖のどこかの要素が失敗すると、
  連鎖全体の結果は却下されたことになり、失敗地点から先の成功ハンドラーは呼び出されない。
* 解決することが値を与えるのと同じように、却下することにも値を与え、これを通常、拒否の理由という。
* ハンドラー関数内の例外が拒絶された場合は、その例外の値が理由として使用される。
  同様に、ハンドラーが却下された ``Promise`` を返すと、その拒絶は次の ``Promise`` に流れる。

  * 却下された ``Promise`` を直ちに新規に作成する関数 ``Promise.reject`` がある。

* このような却下を明示的に処理するために、``Promise`` にはハンドラーを登録するメソッド ``catch`` がある。
  ``then`` ハンドラーが通常の解決を処理するのと同様にして、
  ``Promise`` が却下されたときに呼び出される。

  * 新しい ``Promise`` を返すという点でも ``then`` とよく似ている。
  * この ``Promise`` は、正常に解決された場合は元の ``Promise`` の値に、
    そうでない場合は ``catch`` ハンドラーの結果に解決される。
  * ``catch`` ハンドラーがエラーを送出する場合には、新しい ``Promise`` も却下される。

* ``then`` は 2 番目の引数として却下ハンドラーを取ることもできる。
  これにより、一度のメソッド呼び出しで両方のタイプのハンドラーを与えることができる。
* ``Promise`` コンストラクターに渡された関数は、関数 ``resolve`` と並んで第 2 引数を受け取り、
  それを使って新しい ``Promise`` を却下することができる。

``then`` と ``catch`` の呼び出しが形成する ``Promise`` の値の連鎖を、
非同期の値や失敗が流れていくパイプラインとみなせる。

* このような連鎖はハンドラーを登録することによって構築されていくので、
  各リンクには成功ハンドラーまたは拒絶ハンドラー（またはその両方）が関連付けられている。
* 結果のタイプ（成功または失敗）に合致しないハンドラーは無視される。
  しかし、合致したハンドラーは呼び出され、その結果によって次に来る値のタイプが決定する。

  * ``Promise`` でない値を返した場合は成功、
  * 例外を投げた場合は拒絶、
  * それらのいずれかを返した場合は ``Promise`` の結果となる。

  .. code:: javascript

     new Promise((_, reject) => reject(new Error("Fail")))
         .then(value => console.log("Handler 1"))
         .catch(reason => {
             console.log("Caught failure " + reason);
             return "nothing";
         })
         .then(value => console.log("Handler 2", value));
     // → Caught failure Error: Fail
     // → Handler 2 nothing

  * 上記コードをバラして実行してもわかりにくいことに注意。

* JavaScript の環境が ``Promise`` の却下が処理されなかったことを検知した場合には、
  通常の未処理例外を検知したときと同様に処理する。

Networks are hard
======================================================================

.. todo:: この節をもう一度確認する。

カラスのミラーシステムは、合図を送信するのに十分な光がなかったり、
何かが進路を遮ったり、送信しても受信されないということもある。
このままでは、送信に与えられたコールバックが呼び出されないだけで、
問題に気づかないままにプログラムが停止してしまう。
一定期間応答が得られないと、リクエストがタイムアウトして失敗を報告するようになるといいだろう。

* 多くの場合、伝送の失敗は偶発的なものなので、単にリクエストを再試行するだけで成功することがある。
  そこで、リクエストの送信を自動的に何度か再試行するように変更していく。
* ``Promise`` は良いものだということがわかったので、
  リクエスト関数を ``Promise`` を返すように変更する。
  表現できる内容の点ではコールバックと ``Promise`` は等価だ。
  コールバックベースの関数は ``Promise`` ベースのインターフェイスを公開するためにラップでき、
  その逆もまた成り立つ。

リクエストとその応答が正常に届く場合でも、
例えば、定義されていないリクエストタイプを使おうとした場合や、
ハンドラーがエラーを送出する場合などに、応答が失敗を示すことがある。
これをサポートするために、``send`` と ``defineRequestType`` を前述の規則に従わせる。
コールバックに渡される最初の引数を失敗の理由とし、2 番目の引数を実際の結果とする。

これらは、ラッパーによって ``Promise`` の解決と却下に変換できる。
この ``request`` は後ほどしばしば参照されるたいせつな機能だ。

.. code:: javascript

   class Timeout extends Error {}

   function request(nest, target, type, content) {
       return new Promise((resolve, reject) => {
           let done = false;
           function attempt(n) {
               nest.send(target, type, content, (failed, value) => {
                   done = true;
                   if (failed) reject(failed);
                   else resolve(value);
               });
               setTimeout(() => {
                   if (done) return;
                   else if (n < 3) attempt(n + 1);
                   else reject(new Timeout("Timed out"));
               }, 250);
           }
           attempt(1);
       });
   }

* ``Promise`` は一度しか解決（または却下）できないので、これでうまくいく。
  最初に ``resolve`` または ``reject`` が呼ばれたときに ``Promise`` の結果が決定され、
  他のリクエストが終了した後に戻ってきたリクエストによるそれ以降の呼び出しは無視される。
* 非同期ループを作るためには、再試行のために再帰関数を使う。
  関数 ``attempt`` は、リクエストの送信を一度だけ試みる。
  また、タイムアウトを設定し、250 ミリ秒経過しても応答がない場合は、
  次の試行を開始するか、3 回目の試行であれば、``Promise`` を却下する。
  その理由は ``Timeout`` オブジェクトで表される。

1/4 秒ごとに再試行し、3/4 秒経っても応答がない場合にあきらめるというのは、いかにも恣意的だ。
リクエストが通っていても、ハンドラーが少し時間をかけているだけでリクエストが複数回送信されることもある。
この問題があることを念頭にハンドラーを書く。

----

コールバックから我々自身を完全に切り離すために、先に ``defineRequestType`` のラッパーを定義しておく。
このラッパーでは、ハンドラー関数が ``Promise`` や普通の値を返すことができ、
それをコールバックに送ってくれるというものだ。

.. code:: javascript

   function requestType(name, handler) {
       defineRequestType(name, (nest, content, source,
                                callback) => {
           try {
               Promise.resolve(handler(nest, content, source))
                   .then(response => callback(null, response),
                         failure => callback(failure));
           } catch (exception) {
               callback(exception);
           }
       });
   }

* ``Promise.resolve`` は、ハンドラーからの戻り値がまだ ``Promise`` でない場合に、
  それを ``Promise`` に変換するために使う。これは前に習った。
* ハンドラーの呼び出しを ``try`` ブロックでラップして、ハンドラーが直接送出する例外が
  コールバックに渡されるようにしていることに注意。

  * これは、生のコールバックでエラーを適切に処理することの難しさを表している。
    このような例外を適切に転送するように制御することを忘れがちだ。
    連想制御をしっかりしないと、失敗が正しいコールバックに通知されない。
    ``Promise`` を使えば、このような処理をほとんど自動的に行うことができ、
    我々が間違いにくくなる。

Collections of promises
======================================================================

どの巣の計算機も、送信可能な距離にある他の巣の配列を、そのプロパティー ``neighbors`` に保持している。

どの巣が現在到達可能かを調べるに、それぞれの巣に ``ping`` リクエスト（単に応答を求めるリクエスト）を送信し、
どの巣から応答があるかを見る関数を書くことができる。

同時に実行されている ``Promise`` のコレクションを扱うときには、
関数 ``Promise.all`` が役に立つ。この関数は、配列内のすべての ``Promise`` が解決するのを待機して、

* これらの ``Promise`` が生成した値の配列に解決する ``Promise`` を元の配列と同じ順序で返す。
* いずれかの ``Promise`` が却下された場合 ``Promise.all`` 自体が却下される。

.. code:: javascript

   requestType("ping", () => "pong");

   function availableNeighbors(nest) {
       let requests = nest.neighbors.map(neighbor => {
           return request(nest, neighbor, "ping")
               .then(() => true, () => false);
       });
       return Promise.all(requests).then(result => {
           return nest.neighbors.filter((_, i) => result[i]);
       });
   }

* ある近所の巣が使えない場合、合体 ``Promise`` 全体が失敗してしまうと何もわからぬままになるのは困る。
  そこで、隣人の集合をリクエスト ``Promise`` に変換する関数には、
  成功したリクエストには ``true`` を、却下されたリクエストには ``false`` を生成するハンドラーを付ける。
* 合体 ``Promise`` に対するハンドラーでは、メソッド ``filter`` を使って、
  対応する値が ``false`` である要素を近所の巣の配列から取り除く。

試しに ``availableNeighbors(bigOak).then(neighbors => console.log(neighbors))`` などとしてみるとよい。

Network flooding
======================================================================

ネットワーク全体に情報を流すためには、ある種のリクエストを設定し、
それを自動的に隣の巣に転送するという方法がある。
ネットワーク全体がメッセージを受け取るまで、これらの巣がさらにそれらの隣の巣に転送する。

.. code:: javascript

   import {everywhere} from "./crow-tech";
   //const {everywhere} = require("./crow-tech");

   everywhere(nest => {
       nest.state.gossip = [];
   });

   function sendGossip(nest, message, exceptFor = null) {
       nest.state.gossip.push(message);
       for (let neighbor of nest.neighbors) {
          if (neighbor == exceptFor) continue;
          request(nest, neighbor, "gossip", message);
       }
   }

   requestType("gossip", (nest, message, source) => {
       if (nest.state.gossip.includes(message)) return;
       console.log(`${nest.name} received gossip '${message}' from ${source}`);
       sendGossip(nest, message, source);
   });

* 同じメッセージをネットワーク上で永遠に送り続けることを避けるために、
  巣はすでに見たことのある噂の配列を保持する。
  この配列を定義するために、すべての巣でコードを実行する関数 ``everywhere`` を使って、
  巣の ``state`` オブジェクトにプロパティーを追加する。

  * 例えば ``bigOak.state.gossip`` が定義されて空の配列が値となる。他の巣も同様。

* 巣が重複した噂メッセージを受信した場合、それを無視する。
  しかし、新しいメッセージを受け取ると、送信者以外のすべての隣人に興奮して伝える。
* これにより、新しい噂話がネットワークに広がっていく。
  現在、一部の接続が機能していない場合であっても、
  ある巣への代替経路があれば、そこを経由して噂話が届く。

このようなネットワーク通信スタイルを flooding と呼び、
すべてのノードが情報を持つようになるまで、情報をネットワークに氾濫させる。

Message routing
======================================================================

* あるノードが他の単一のノードと会話をしたい場合には、flooding の手法はあまり効率的でない。
  特にネットワークの規模が大きい場合、データ転送が無駄に多くなる。
* もうひとつの方法は、メッセージがノードからノードへとホップして
  目的地に到達するまでの道を設定することだ。
  これには、ネットワークのレイアウトに関する知識が必要になるという難点がある。
  遠くの巣の方向にリクエストを送るには、どの隣の巣が目的地により近いかを知る必要がある。
  間違った方向に送ってもあまり意味がない。

巣のどれもが自分の直系の隣人のことしか知らないので、
経路を計算するのに必要な情報を持っていない。
巣のネットワークの状態が時間の経過ととも変化することを考慮に入れた方法で、
これらの接続に関する情報をすべての巣に広めなければならない。

ここでも flooding を使うことができるが、与えられたメッセージがすでに受信されているかどうかをチェックする代わりに、
与えられた巣の隣人の新しい集合が、現在持っている集合と等しいかどうかをチェックする。

.. code:: javascript

   requestType("connections", (nest, {name, neighbors},
                               source) => {
       let connections = nest.state.connections;
       if (JSON.stringify(connections.get(name)) == JSON.stringify(neighbors)) return;
       connections.set(name, neighbors);
       broadcastConnections(nest, name, source);
   });

   function broadcastConnections(nest, name, exceptFor = null) {
       for (let neighbor of nest.neighbors) {
           if (neighbor == exceptFor) continue;
           request(nest, neighbor, "connections", {
               name,
               neighbors: nest.state.connections.get(name)
           });
       }
   }

   everywhere(nest => {
       nest.state.connections = new Map();
       nest.state.connections.set(nest.name, nest.neighbors);
       broadcastConnections(nest, nest.name);
   });

* オブジェクトや配列に対して ``==`` はそのまま適用しても意味がないので、
  粗いようだが``JSON.stringify`` を使用している。
* ノードはすぐに接続のブロードキャストを開始し、完全に到達できない巣がない限り、
  すべての巣に最新のネットワークグラフの ``Map`` をすばやく与えるはずだ。

----

グラフでできることは、以前見たように、グラフの中の経路を見つけることだ。
メッセージの宛先に向かう経路があれば、メッセージを送るべき方向がわかる。

以下の関数 ``findRoute`` は、第 7 章の ``findRoute`` とよく似ていて、
ネットワーク上の任意のノードに到達する道を検索する。
ただし、経路全体を返すのではなく、次のステップを返すだけだ。
その次の巣では、ネットワークに関する最新の情報を使って、メッセージをどこに送るかを決定する。

.. code:: javascript

   function findRoute(from, to, connections) {
       let work = [{at: from, via: null}];
       for (let i = 0; i < work.length; i++) {
           let {at, via} = work[i];
           for (let next of connections.get(at) || []) {
               if (next == to) return via;
               if (!work.some(w => w.at == next)) {
                   work.push({at: next, via: via || next});
               }
           }
       }
       return null;
   }

これで遠くの巣にもメッセージを送信できる関数を作ることができる。

* メッセージが直接の隣人に宛てられたものであれば、通常通り送信する。
* そうでない場合は、メッセージをオブジェクトにパックして ``route`` リクエストを使って、
  目標に近い隣人に送り、その隣人は同じ動作を繰り返す。

.. code:: javascript

   function routeRequest(nest, target, type, content) {
       if (nest.neighbors.includes(target)) {
           return request(nest, target, type, content);
       } else {
           let via = findRoute(nest.name, target,
               nest.state.connections);
           if (!via) throw new Error(`No route to ${target}`);
           return request(nest, via, "route",
                          {target, type, content});
       }
   }

   requestType("route", (nest, {target, type, content}) => {
       return routeRequest(nest, target, type, content);
   });

----

原始的な通信システムの上に何層もの機能を構築して、便利に使えるようにした。
これは、実際の計算機ネットワークがどのように機能するかの単純なモデルだ。

* 計算機ネットワークの特徴は、信頼性が低いということにある。
* ネットワークの障害までをも抽象化することはできない。
* ネットワークプログラミングでは、障害を予測して対処することが重要になる。

Async functions
======================================================================

* カラスは重要な情報を保存するために、複数の巣に亘って情報を複製する。
  そうすれば、タカが巣を一つ破壊しても情報は失われない。
* 巣の計算機は、自分のストレージにない情報を取り出すために、
  それがある巣を見つけるまで、ネットワーク上の他の巣をランダムに調べる。

.. code:: javascript

   requestType("storage", (nest, name) => storage(nest, name));

   function findInStorage(nest, name) {
       return storage(nest, name).then(found => {
           if (found != null) return found;
           else return findInRemoteStorage(nest, name);
       });
   }

   function network(nest) {
       return Array.from(nest.state.connections.keys());
   }

   function findInRemoteStorage(nest, name) {
       let sources = network(nest).filter(n => n != nest.name);
       function next() {
           if (sources.length == 0) {
               return Promise.reject(new Error("Not found"));
           } else {
               let source = sources[Math.floor(Math.random() * sources.length)];
               sources = sources.filter(n => n != source);
               return routeRequest(nest, source, "storage", name)
                   .then(value => value != null ? value : next(), next);
           }
       }
       return next();
   }

* ``connections`` は ``Map`` なので ``Object.keys`` は動作しない。

  * メソッド ``keys`` ならあるが、これは配列ではなく反復子を返す。
    反復子または反復可能な値は関数 ``Array.from`` で配列に変換できる。

* ``Promise`` を使っても、これはかなり厄介なコードだ。
  複数の非同期アクションが明らかでないやり方で連結されている。
  また、巣をループのをモデル化するのに再帰関数 ``next`` が必要だ。

  * ``findInRemoteStorage`` の ``then()`` 呼び出しの実引数が特に厄介。

* このコードが実際に行っていることは完全に直線的で、
  常に前のアクションが完了するのを待ってから次のアクションを開始する。
  同期型のプログラミングモデルであれば、もっと単純に表現できる。

----

JavaScript では非同期の計算を記述するために、擬似的同期コードを書くことができる。
**非同期関数** とは、暗黙のうちに ``Promise`` を返し、
その本体の中で他の ``Promise`` を待機することで同期的に見せかける関数だ。

* ここまで読んでようやく ``Promise`` が Python でいう ``concurrent.futures.Future`` に相当するものだと気づく。

関数 ``findInStorage`` を次のように書き換えることができる：

.. code::javascript

   async function findInStorage(nest, name) {
       let local = await storage(nest, name);
       if (local != null) return local;

       let sources = network(nest).filter(n => n != nest.name);
       while (sources.length > 0) {
           let source = sources[Math.floor(Math.random() * sources.length)];

           sources = sources.filter(n => n != source);
           try {
               let found = await routeRequest(nest, source, "storage", name);
               if (found != null) return found;
           } catch (_) {}
       }
       throw new Error("Not found");
   }

* 非同期関数はキーワード ``function`` の前に ``async`` が付く。
* また、メソッドも名前の前に ``async`` と書くことで非同期にすることができる。
* このような関数やメソッドが呼び出されると ``Promise`` が返される。
  本体が何かを返すとすぐにその ``Promise`` は解決される。
  例外が発生した場合は却下される。
* 非同期関数の内部では、式の前に ``await`` という単語を置くことで、
  ``Promise`` の解決を待機してから、元の関数の実行を継続することができる。
* このような関数は、通常の JavaScript 関数とは違って、
  最初から最後まで一度に実行されることはない。
  ``await`` を持つ任意のポイントでフリーズし、後から再開する。

自明ではない非同期コードの場合、この記法は通常、``Promise`` を直接使うよりも便利だ。
複数のアクションを同時に実行するなど、同期モデルに合わないことをする必要がある場合でも、
``await`` と ``Promise`` を直接使うことで簡単に組み合わせられる。

Generators
======================================================================

関数を一時停止し、再開する機能は、非同期関数のほかに、ジェネレーター関数というものもある。
ここには ``Promise`` はない。

* 関数を ``function*`` で定義すると、その関数はジェネレーターになる。
  ジェネレータを呼び出すと第 6 章で説明した反復子が返される。

.. code:: javascript

   function* powers(n) {
       for (let current = n;; current *= n) {
           yield current;
       }
   }

   for (let power of powers(3)) {
       if (power > 50) break;
       console.log(power);
   }
   // → 3
   // → 9
   // → 27

* コードを見る限り、Python のジェネレーターと同じように動作するものだろう。
* ジェネレータ関数を使うと反復子を書くのがはるかに簡単になる。
  第 6 章の練習問題で出てきたクラス ``Group`` の反復子はジェネレーターを使って書ける：

  .. code:: javascript

     Group.prototype[Symbol.iterator] = function*() {
         for (let i = 0; i < this.members.length; i++) {
             yield this.members[i];
         }
     };

* 反復状態を保持するオブジェクトを作成する必要はもうない。
  ``yield`` するたびにジェネレーターがローカルの状態を自動的に保存する。
* ``yield`` 式は、ジェネレーター関数の中でのみ直接発生し、
  その中で定義した内部関数では発生しない。
  ジェネレーターが ``yield`` するときに保存する状態は、
  そのローカル環境と ``yield`` した位置だ。
* 非同期関数は、特殊なタイプのジェネレーターだ。
  呼び出されたときには ``Promise`` を生成し、
  終了時にはそれを解決するか、例外が発生したときに却下する。
* ``Promise`` を ``await`` すると、その ``Promise`` の結果（解決時でも却下時でも）は
  常に ``await`` 式の結果となる。

The event loop
======================================================================

* 非同期的な挙動は、それ自体が空の関数コールスタック上で起こる。
  ``Promise`` がない場合の非同期コードの例外管理が難しい理由の一つがこれだ。
  各コールバックはほとんど空のスタックから始まるので、
  捕捉ハンドラーが例外を送出するときには、ハンドラーはスタック上にない。

.. code:: javascript

   try {
       setTimeout(() => { throw new Error("Woosh");}, 20);
   } catch (_) {
       // This will not run
       console.log("Caught!");
   }

タイムアウトやリクエストの受信といったイベントがどれだけ接近して発生しても、
JavaScript 環境では一度に一つのプログラムしか実行しない。
**イベントループ** と呼ばれる、プログラムの大きなループを実行していると考えることができる。

何もすることがないときは、このループは停止する。
しかし、イベントが入ってくると、キューに追加され、そのコードが次々と実行されていく。
同時に二つのものは実行されないので、ゆっくりと実行されるコードは他のイベントの処理を遅らせる可能性がある。

次の例ではタイムアウトを設定するが、タイムアウトが意図した時点を過ぎるまでダレてしまい、
タイムアウトが遅れる。

.. code:: javascript

   let start = Date.now();
   setTimeout(() => {console.log("Timeout ran at", Date.now() - start);}, 20);
   while (Date.now() < start + 50) {}
   console.log("Wasted time until", Date.now() - start);
   // → Wasted time until 50
   // → Timeout ran at 55

``Promise`` は常に新しいイベントとして解決または却下される。
``Promise`` がすでに解決されていても、それが待機されていると、コールバックはすぐにではなく、
現在のスクリプトが終了してから実行されることになる。

.. code:: javascript

   Promise.resolve("Done").then(console.log);
   console.log("Me first!");
   // → Me first!
   // → Done

Asynchronous bugs
======================================================================

* 非同期プログラムでは実行中に他のコードが実行される隙間があるかもしれない。

カラスには球根の中の数を数える趣味がある。
次のコードは、ある年のすべての巣にあるの数を列挙しようとしている。

カラスには毎年村中で孵化するヒナの数を数えるという趣味がある。
巣ではこの数をストレージ球根に保存する。
次のコードは、ある年のすべての巣の数を列挙するものだ：

.. code:: javascript

   function anyStorage(nest, source, name) {
       if (source == nest.name) return storage(nest, name);
       else return routeRequest(nest, source, "storage", name);
   }

   async function chicks(nest, year) {
       let list = "";
       await Promise.all(network(nest).map(async name => {
           list += `${name}: ${await anyStorage(nest, name, `chicks in ${year}`)}\n`;
       }));
       return list;
   }

* このようにして矢印関数も非同期にできる。

このコードをすぐに怪しいとは思わない。
非同期矢印関数を巣の集合に写像して ``Promise`` の配列を作り、
関数 ``Promise.all`` を使ってこれらすべてを ``await`` してからそれらが構築したリストを返している。
しかし、これには大きな問題がある。この関数は常に一行の出力しか返さず、
最も反応の遅かった巣のリストを返す。それはなぜか。

問題は演算子 ``+=`` にある。この演算子は、文の実行開始時に ``list`` の現在の値を受け取り、
``await`` が終了すると、その値に追加された文字列を加えたものを ``list`` の結合に設定する。

しかし、文が実行を開始してから終了するまでには、非同期の隙間がある。
``map`` 式はリストに何かが追加される前に実行されるので、
それぞれの ``+=`` は空の文字列から始まり、ストレージの取得が終了したときには、
空の文字列にその行を追加した結果である一行のリストに設定されてしまう。

これは、マッピングされた ``Promise`` から行を返し、
``Promise.all`` の結果に対して ``join`` を呼び出すことで簡単に回避することができた。

* いつものように、新しい値を計算することは、既存の値を変更することよりも間違いにくい。

.. code:: javascript

   async function chicks(nest, year) {
       let lines = network(nest).map(async name => {
           return name + ": " +
               await anyStorage(nest, name, `chicks in ${year}`);
           });
       return (await Promise.all(lines)).join("\n");
   }

ノート：適当な巣 ``nest`` に対して例えば ``chicks(nest, 2009)`` を呼び出すと次のようなデータが得られる：

.. code:: text

  Big Oak: 1
  Gilles' Garden: 4
  Butcher Shop: 5
  Hawthorn: 3
  Great Pine: 5
  Chateau: 1
  Fabienne's Garden: 5
  Sportsgrounds: 3
  Jacques' Farm: 5
  Tall Poplar: 3
  Woods: 0
  Church Tower: 4
  Big Maple: 3
  Cow Pasture: 1

* このような間違いは ``await`` を使っているときに特に起こりやすく、
  自分のコードのどこに隙間があるのかを意識する必要がある。
  明示的な非同期性（コールバック、``Promise``, ``await`` など）の利点は、
  このような隙間を見つけるのが比較的簡単だということ。

Summary
======================================================================

* 非同期プログラミングでは、長時間実行されるアクションの待ち時間を、
  アクション中にプログラムをフリーズさせることなく表現することができる。
* JavaScript 環境では、アクションが完了したときに呼び出される関数であるコールバックを使って、
  このスタイルのプログラミングを行うのが一般的だ。
* イベントループでは、このコールバックの実行が重ならないように、
  適切なタイミングで次々と呼び出されるようにスケジュールされている。
* 非同期プログラミングは、将来完了するかもしれないアクションを表すオブジェクトである
  ``Promise`` や、非同期プログラムがあたかも同期プログラムであるかのように
  書くことができる ``async`` 関数によって、より簡単に行うことができる。

Exercises
======================================================================

Tracking the scalpel
----------------------------------------------------------------------

**問題** 村のカラスたちは古い手術ナイフを所有していて、網戸や梱包材を切り裂くなど、特別な仕事に使うことがある。
手術ナイフをすぐに見つけられるように、手術ナイフを別の巣に移すたびに、
手術ナイフが引っ越す前の巣と引っ越す先の巣の両方のストレージに
"scalpel" という名前で、新しい場所を値として追加している。

つまりナイフを見つけるということは、ストレージのエントリーのパンくずのような跡を、
それが巣自体を指し示している巣を見つけるまでたどるということだ。

これを実行する非同期関数 ``locateScalpel`` を書け。
先に定義した ``anyStorage`` 関数を使えば、任意の巣のストレージにアクセスすることができる。
十分な時間が経過しているので、どの巣のストレージにも "scalpel" のエントリーがあるとして構わない。

次に、同じ関数を ``async`` や ``await`` を使わずにもう一度書け。
どちらのバージョンでも、リクエストの失敗が返された ``Promise`` の却下として適切に表示されるか。
それはどのようなものになるか。

**解答** 目標は ``nest.scalpel == nest.name`` なる ``nest`` を見つけることだ。
問いの前半は次のコードで見つかる：

.. code:: javascript

   async function locateScalpel(nest) {
       for(let target of network(nest)){
           let location = await anyStorage(nest, target, "scalpel");
           if(location == target){
               return location;
           }
       }
       throw new Error("Not found");
   }

   locateScalpel(bigOak)
       .then(loc => console.log(`Found in ${loc}`))
       .catch(() => console.log("Not found")); // → Found in Butcher Shop

同じ関数を非同期キーワードを用いずに書くと：

.. code:: javascript

   function locateScalpelSync(nest){
       for(let target of network(nest)){
           let location;
           anyStorage(nest, target, "scalpel")
               .then(value => {
                   location = value;
               });
           if(location == target){
               return location;
           }
       }
       throw new Error("Not found");
   };

これは先ほどのようには動作しない。関数を呼び出すとループが終わって例外が ``throw`` される。

Building ``Promise.all``
----------------------------------------------------------------------

**問題** ``Promise.all`` は ``Promise`` の配列が与えられると、配列内のすべての
``Promise`` が終了するのを待つ ``Promise`` を返す。

* 成功すると結果値の配列が得られる。
* 配列の中の ``Promise`` が失敗すると ``all`` が返す ``Promise`` も失敗し、
  失敗した ``Promise`` の理由を得られる。

このようなことをする普通の関数 ``Promise_all`` を実装しろ。

プロミスが成功または失敗した後は、再び成功または失敗することはできず、
それを解決する関数への呼び出しは無視されることを覚えておくことだ。
これにより、プロミスの失敗を処理する方法を単純化できる。

**解答** これは二時間くらい考えて諦めた。
``Promise`` の配列に対するループを ``Promise`` のコンストラクターに与えるのが急所のようだ。

.. code:: javascript

   function Promise_all(promises) {
       let results = [];
       return new Promise((resolve, reject) => {
           promises.forEach(p => {
               p.then(value => {
                   results.push(value);
                   if (results.length == promises.length) {
                       resolve(results);
                   }
               }).catch(error => reject(error));
           });
       });
   }

なお、上記のコードは本物とは異なり、引数の配列に ``Promise`` でないオブジェクトが含まれる場合の挙動が異なる。

参考：

* `Promise.all() - JavaScript | MDN <https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Promise/all>`__
* `Implementing Promise.all in javascript | by Murali Krishna | Medium <https://medium.com/@muralikv/implementing-promise-all-in-javascript-732076497946>`__
