======================================================================
Node.js
======================================================================

これまでは JavaScript を単一の環境、すなわちブラウザーで使ってきた。
本章と次章では JavaScript の技術をブラウザーの外部で活用できるプログラム、
`Node.js <https://nodejs.org>`__ を簡単に導入する。これを使えば、
小さなコマンドラインツールから動的な Web サイトを動かす HTTP サーバーまで、
何でも構築することができる。

* 本章のコードを実行するには、Node.js のバージョン 10.1 以上をインストールする必要がある。

.. contents:: ノート目次

Background
======================================================================

* ネットワークを介して通信するシステムを記述する際の難しい問題の一つが、入出力の管理だ。
  つまり、ネットワークやハードドライブとの間でデータを読み書きすることだ。
  データの移動には時間がかかるが、それを上手にスケジューリングすることで、
  システムがユーザーやネットワークの要求にどれだけ早く反応できるかが大きく変わってくる。
* このようなプログラムには、非同期プログラミングだ有効だ。
  複雑なスレッド管理や同期を行うことなく、複数の機器と同時にデータを送受信できる。
* 当初、 Node_ は非同期プログラミングを簡単便利にすることを目的として開発された。
* JavaScript は入出力を行う組み込みの方法がない数少ないプログラミング言語だ。
  したがって、JavaScript は Node_ のいくぶん奇抜な入出力の方法にフィットすることができ、
  一貫性のない二つのインターフェイスになってしまうことはなかった。
* Node_ が設計された当時、すでにブラウザーでコールバックベースのプログラミングが行われていたため、
  この言語を取り巻く共同体は非同期プログラミングの様式に慣れていた。

The node command
======================================================================

システムに Node.js がインストールされていると :command:`node` というコマンドラインツールが使える。
例えば、次の内容のスクリプトファイル ``hello.js`` があるとする：

.. code:: javascript

  let message = "Hello world";
  console.log(message);

これをコンソールから以下のようにして実行する：

.. code:: console

   $ node hello.js
   Hello world

* メソッド ``console.log`` はブラウザーと同じようにテキストを出力するのだが、
  Node_ ではブラウザーの JavaScript コンソールではなく、プロセスの標準出力ストリームに送られる。

コマンドラインからファイルを与えずに :command:`node` を実行する場合には、
JavaScript のコードを入力するためのプロンプトが表示され、すぐに結果を見ることができる。

.. code:: console

   $ node
   > 1 + 1
   2
   > [-1, -2, -3].map(Math.abs)
   [1, 2, 3]
   > process.exit(0)
   $

* 変数 ``process`` は変数 ``console`` と同様に Node_ で大域的に利用可能だ。

  * メソッド ``process.exit`` はステータスコードを与えてプロセスを終了させる。
  * スクリプトに与えられたコマンドライン引数を調べるには、文字列配列 ``process.argv`` を使う。

    * ``process.argv[0]`` は :command:`node` 自身の名前
    * ``process.argv[1]`` はスクリプトファイル名
    * したがって、実質的にはコマンドライン引数はインデックス 2 から始まる。

    .. code:: console

       $ node showargv.js one --and two
       ["node", "/tmp/showargv.js", "one", "--and", "two"]

* ``Array``, ``Math``, ``JSON`` など、標準的な JavaScript の大域変数のすべてが Node_ の環境にも存在している。
* ただし ``document``, ``prompt`` などのブラウザー関連の機能はない。

Modules
======================================================================

* Node_ は大域名前空間に他にも変数をいくつか置いている。
  組み込み機能にアクセスしたいならば、モジュールシステムにそれをねだる必要がある。
* 第 10 章で述べた関数 ``require`` に基づく CommonJS モジュールシステムが
  Node_ に組み込まれており、組み込みモジュール、ダウンロード済みパッケージ、
  自作プログラムの一部であるファイルなど、あらゆるものをロードするのに使われる。
* 関数 ``require`` が呼ばれると、 Node_ は与えられた文字列をロード可能な
  実際のファイルパスに解決しなければならない。

  * ``/``, ``./``, ``../`` から始まるパスは現在のモジュールパスへの相対パスとして解決される。
  * 拡張子 ``.js`` は省略可能。
  * 必要なパスがディレクトリーを指している場合、 Node_ はそこにある ``index.js`` というファイルをロードしようとする。
  * 相対パスや絶対パスでない文字列が ``require`` に与えられると、
    組み込みモジュールまたはディレクトリー ``node_modules`` にインストールされているモジュールを
    参照していると解釈される。

    * 例 ``require(fs)``

----

二つのファイルからなる小さなプロジェクトを作成する。
最初のものは ``main.js`` といい、コマンドラインから呼び出すことができるスクリプトであって、
文字列を反転するのに使うものとする。

.. code:: javascript

   // main.js

   const {reverse} = require("./reverse");

   // Index 2 holds the first actual command line argument
   let argument = process.argv[2];
   console.log(reverse(argument));

二番目のものは ``reverse.js`` で、文字列を反転させる機能を定義する。
これは ``main.js`` からでも、その他のスクリプトからでも使用できる。

.. code:: javascript

  // reverse.js

  exports.reverse = function(string) {
      return Array.from(string).reverse().join("");
  };

* ``exports`` にプロパティーを追加すると、そのモジュールのインターフェイスに追加する。
  Node.js はファイルを CommonJS モジュールとして扱うので、
  ``main.js`` は ``reverse.js`` からエクスポートされた関数 ``reverse`` を取ることができる。

以上で、このツールを次のように呼び出すことができる：

.. code:: console

   $ node main.js JavaScript
   tpircSavaJ

Installing with NPM
======================================================================

* 第 10 章で導入した NPM_ は JavaScript のオンラインリポジトリーであって、
  その多くは Node_ に対して特殊にかかれている。
  Node_ をインストールすると、このリポジトリーとやり取りするコマンド
  :command:`npm` も使えるようになる。

NPM_ の主な用途はパッケージをダウンロードすることだ。
これを使ってパッケージを取得、インストールすることができる。

.. code:: console

   $ npm install ini
   npm WARN enoent ENOENT: no such file or directory,
   open '/tmp/package.json'
   + ini@1.3.5
   added 1 package in 0.552s
   $ node
   > const {parse} = require("ini");
   > parse("x = 1\ny = 2");
   [Object: null prototype] { x: '1', y: '2' }

上のように :command:`npm install ini` を実行すると NPM_ はディレクトリー ``node_modules`` を作成する。
そのディレクトリーの中に、ライブラリーを含むディレクトリー ``ini`` がある。

* このディレクトリーを開いてコードを見ることができる。
* ``require("ini")`` を呼び出すとこのライブラリーがロードされて、
  関数 ``parse`` を呼び出して構成ファイルを解析することができる。

----

NPM_ はパッケージを中央ディレクトリーではなく、カレントディレクトリーにインストールする。
これには、各アプリケーションがインストールするパッケージを完全に制御できるようになり、
バージョン管理やアプリケーションを削除するときの後始末が容易になるという利点がある。

Package files
======================================================================

:command:`npm install` の例でファイル ``package.json`` が存在しないという警告が表示されるかもしれない。
このファイルを、手動または :command:`npm init` を実行して、プロジェクトごとに作成することが推奨される。
ファイル ``package.json`` には、プロジェクトの名前やバージョンなどの情報、依存関係のリストが含まれてる。

第 7 章のロボットシミュレーションは、第 10 章の演習でモジュール化されているので、
次のようなファイル ``package.json`` があるかもしれない（まだ取り組んでいないのでない）：

.. code:: json

   {
       "author": "Marijn Haverbeke",
       "name": "eloquent-javascript-robot",
       "description": "Simulation of a package-delivery robot",
       "version": "1.0.0",
       "main": "run.js",
       "dependencies": {
           "dijkstrajs": "^1.0.1",
           "random-item": "^1.0.0"
       },
       "license": "ISC"
   }

* インストールするパッケージの名前を指定せずに :command:`npm install` を実行すると、
  NPM_ はファイル ``package.json`` に記載されている依存関係をインストールする。

Versions
======================================================================

* ファイル ``package.json`` には、プログラム自身のバージョンと、依存関係にあるパッケージのバージョンの両方が記されている。
  バージョンは、パッケージが別々に進化するという事実に対処するための手段であり、
  ある時点で存在していたパッケージと連動するように書かれたコードは、
  後に修正されたバージョンのパッケージでは動作しないかもしれない。
* NPM_ は **semantic versioning** と呼ばれる形式に従うことをパッケージに要求している。
  これは、どのバージョンに互換性があるか（古いインターフェースを壊さないか）という情報をバージョン番号に符号化したものだ。

  * ``2.3.0`` のようにピリオドで区切られた 3 つの数字で構成されている。
  * 新しい機能を追加するたびに、真ん中の数字を大きくする。
  * パッケージを使用している既存のコードが新しいバージョンでは動作しないなどの
    互換性が失われる更新では、最初の番号を大きくする。
  * 依存関係のバージョン番号の前に記号 ``^`` を付けると、その番号と互換性のある
    任意のバージョンをインストールしても構わないことを示す。
    例えば ``^2.3.0`` は 2.3.0 以上 3.0.0 未満のバージョンならば何でもよいことを意味する。

* コマンド :command:`npm` は新しいパッケージやパッケージの新バージョンを発行するためにも使う。

  * ファイル ``package.json`` が存在するディレクトリーでコマンド
    :command:`npm install` を実行すると、JSON ファイルに記載されている名前とバージョンの
    パッケージが登録所に公開される。
  * 誰でもパッケージを NPM_ に公開することができる。パッケージ名はそこで使われていないものに限る。

The file system module
======================================================================

Node_ で最もよく使われる組み込みモジュールの一つが ``fs`` で、ファイルシステムを意味する。
ファイルやディレクトリーを扱うための関数をエクスポートする。

.. code:: javascript

   let {readFile} = require("fs");
   readFile("file.txt", "utf8", (error, text) => {
       if (error) throw error;
       console.log("The file contains:", text);
   });

.. code:: javascript

   const {readFile} = require("fs");
   readFile("file.txt", (error, buffer) => {
       if (error) throw error;
       console.log("The file contained", buffer.length, "bytes.", "The first byte is:", buffer[0]);
   });

.. code:: javascript

   const {writeFile} = require("fs");
   writeFile("graffiti.txt", "Node was here", err => {
       if (err) console.log(`Failed to write file: ${err}`);
       else console.log("File written.");
   });

モジュール ``fs`` には ``readdir``, ``stat``, ``rename``, ``unlink`` など、多くの便利な関数がある。

* これらの関数のほとんどは、最後の引数としてコールバック関数を受け取り、
  失敗したときか成功したときのどちらかにそれを呼び出す。

  * 第 11 章で見たように、この方式にはエラー処理が冗長になり、エラーが起こりやすいという大きな欠点がある。

----

``Promise`` は以前から JavaScript にあったが、本書執筆時点では Node.js への統合が進行中だ。
バージョン 10.1 以降、パッケージ ``fs`` はオブジェクト ``promises`` をエクスポートするようになった。
これは関数版とほとんど同じだが、コールバックではなく ``Promise`` を使用する。

.. code:: javascript

   const {readFile} = require("fs").promises;
   readFile("file.txt", "utf8")
       .then(text => console.log("The file contains:", text));

``fs`` の関数の多くに同期版もあり、同じ名前の関数の末尾に ``Sync`` が付く。
例えば ``readFile`` の同期版は ``readFileSync`` という。

.. code:: javascript

   const {readFileSync} = require("fs");
   console.log("The file contains:", readFileSync("file.txt", "utf8"));

同期操作中、プログラムは完全に停止する。

The HTTP module
======================================================================

もうひとつの中心的なモジュールは ``http`` と呼ばれるものだ。
これは HTTP サーバーを起動したり、HTTP リクエストを行うための機能がある。
これだけで HTTP サーバーを起動することができる。

.. code:: javascript

   const {createServer} = require("http");
   let server = createServer((request, response) => {
       response.writeHead(200, {"Content-Type": "text/html"});
       response.write(`
           <h1>Hello!</h1>
           <p>You asked for <code>${request.url}</code></p>
           `);
       response.end();
   });
   server.listen(8000);
   console.log("Listening! (port 8000)");

このスクリプトを自分のマシンで実行し、Web ブラウザーで <http://localhost:8000/hello> にアクセスして
自分のサーバーにリクエストを送ると、小さな HTML ページが返ってくる。

.. code:: console

   bash$ wget -qO- http://localhost:8000/hello

   <h1>Hello!</h1>
   <p>You asked for <code>/hello</code></p>

* 関数 ``createServer`` に引数として渡された関数は、クライアントがサーバーに接続するたびに呼び出される。
* 変数 ``request`` と ``response`` は受信データと送信データを表す。

  * 変数 ``request`` にはリクエストに関する情報が含まれている。例えばプロパティー ``url`` などがある。

ブラウザーでそのページを開くと、自分の計算機にリクエストを送るということになる。
これによりサーバー機能が実行されて、返信が戻って来て、それをブラウザーで見ることができる。

何かを送り返すには ``response`` のメソッドを呼び出す。

* メソッド ``writeHead`` は応答のヘッダーを書き出す。
  このメソッドには 200 のようなステータスコードとヘッダーを含むオブジェクトとを渡す。
  この例では ``Content-Type`` ヘッダーを設定して HTML 文書を送り返すことをクライアントに知らせている。
* メソッド ``write`` で応答本体そのものを送信する。
  データが利用可能になったときに順次クライアントにストリーミングで送信するなど、
  応答を断片的に送信する場合には、このメソッドを複数回呼び出すこともできる。
* メソッド ``end`` が応答終了を知らせる。

``server.listen`` の呼び出しにより、サーバーはポート 8000 で接続の待機を開始する。
このため、このサーバーと通信するには ``localhost:8000`` に接続する必要がある。

このスクリプトを実行すると、プロセスはただ座って待つ。
スクリプトがイベント（この場合はネットワーク接続）を聴取している場合、
:command:`node` はスクリプトの終わりに達しても自動的に終了しない。
:kbd:`Ctrl` + :kbd:`C` を押して終わる。

----

HTTP クライアントとして動作するには、関数 ``request`` を使用する。

.. code:: javascript

   const {request} = require("http");
   let requestStream = request({
       hostname: "eloquentjavascript.net",
       path: "/20_node.html",
       method: "GET",
       headers: {Accept: "text/html"}
   }, response => {
       console.log("Server responded with status code",
       response.statusCode);
   });
   requestStream.end();

* 関数 ``request`` の最初の引数はリクエストを設定する。
  どのサーバーと通信するか、そのサーバーからどのパスをリクエストするか、
  どのメソッドを使うかなどを伝える。
* 二番目の引数は、応答が来たときに呼び出されるべき関数。
  応答のステータスコードを調べるなど、検査するためのオブジェクトを与える。
* サーバーで見た ``response`` オブジェクトと同様に、関数 ``request`` が返すオブジェクトでは、
  メソッド ``write`` で ``request`` にデータを流し込み、
  メソッド ``end`` で ``request`` を終了させることができる。
  GET リクエストは本体にデータを含んではいけないので、この例では ``write`` を使っていない。

同じような関数がモジュール ``https`` にもあり、``https://`` から始まる URL へのリクエストに使用する。

* ノート：先ほどのコードをそのまま実行すると 302 が返ってくる。
  ``require("https")`` とすると 200 が返ってくる。

----

Node の生の機能でリクエストを行うのは冗長だ。
NPM_ にはもっと便利なラッパーパッケージがある。
例えば ``node-fetch`` は ``Promise`` ベースの ``fetch`` インターフェースがある。

Streams
======================================================================

* 書き込み可能ストリームは Node で広く使われている概念だ。

  * メソッド ``write``
  * メソッド ``end``
  * これらのメソッドに追加の引数としてコールバックを指定でき、処理完了時に呼び出される。

* モジュール ``fs`` の関数 ``createWriteStream`` はファイルを指す書き込み可能ストロームを作成する。

  * メソッド ``write`` は少しずつ書き込むことができる。

* 読み取り可能ストリームはもう少し複雑だ。

  * HTTP サーバーのコールバックに渡された変数 ``request`` と
    HTTP クライアントのコールバックに渡された変数 ``response`` は
    どちらも読み込み可能ストリームだ。前者は読み込んでから書き込むが、
    後者は書き込んでから読み込む。
  * ストリームから読み込むことはイベントハンドラーを使って行われる。

Node でイベントを発信するオブジェクトには、ブラウザーの ``addEventListener`` に似たメソッドがある。
このメソッドにイベント名と関数を与えると、与えられたイベントが発生するたびに、
その関数が呼び出されるように登録される。

読み取り可能なストリームには ``data`` と ``end`` のイベントがある。

* ``data`` イベントはデータが入ってくるたびに発射する。
* ``end`` イベントはストリームが終了するたびに呼び出される。

このモデルは、文書全体がまだ利用できない場合であっても、すぐに処理できるようなデータのストリーミングに最も適している。
ファイルは ``fs`` 関数 ``createReadStream`` を使用することで、
読み取り可能なストリームとして読み取ることができる。

次のコードは、リクエスト本体を読み取り、すべて大文字のテキストとしてクライアントにストリームバックするサーバーを作成する：

.. code:: javascript

   const {createServer} = require("http");

   createServer((request, response) => {
       response.writeHead(200, {"Content-Type": "text/plain"});
       request.on("data", chunk =>
           response.write(chunk.toString().toUpperCase()));
       request.on("end", () => response.end());
   }).listen(8000);

データハンドラーに渡される ``chunk`` の値はバイナリーの ``Buffer`` だ。
これをメソッド ``toString`` で UTF-8 符号化された文字に複号することで文字列に変換する。

----

次のコードは大文字サーバーが稼働している状態で起動すると、
そのサーバーにリクエストを送信し、取得した応答を出力する。

.. code:: javascript

   const {request} = require("http");

   request({
       hostname: "localhost",
       port: 8000,
       method: "POST"
   }, response => {
       response.on("data", chunk =>
           process.stdout.write(chunk.toString()));
   }).end("Hello server");
   // → HELLO SERVER

* ここでは ``console.log`` を使わずに ``process.stdout`` で出力している。

  * ``process.stdout`` はプロセスの標準出力で、書き込み可能ストリームだ。
  * ``console.log`` はここでは使わない。これは出力の末尾に改行文字を追加するが、
    応答が複数の塊として入ってくることから相応しくない。

A file server
======================================================================

本節では HTTP サーバーとファイルシステムに関する知識を組み合わせて、
ファイルシステムへのリモートアクセスを可能にする HTTP サーバーを作る。
このようなサーバーは、ウェブアプリケーションがデータを保存・共有したり、
人々に多数のファイルへのアクセスを与えるなど、あらゆる用途がある。

* リソースとしてファイルを扱う場合、HTTP メソッドの GET, PUT, DELETE を使用して
  ファイルの読み取り、書き込み、削除をそれぞれ行うことができる。
* リクエストに含まれるパスは、参照したいファイルシステムのそれとして解釈される。

  * ファイルシステム全体を共有するわけでは一般的にはないので、
    これらのパスはサーバーの作業ディレクトリーを起点とすると解釈する。

ここでは、さまざまな HTTP メソッドを処理する関数を格納するために
``methods`` というオブジェクトを使用して、プログラムを少しずつ構築していく。

メソッドハンドラは非同期関数であって、リクエストオブジェクトを引数として受け取り、
応答を記述したオブジェクトに解決する ``Promise`` を返す。

.. code:: javascript

   const {createServer} = require("http");
   const methods = Object.create(null);

   createServer((request, response) => {
       let handler = methods[request.method] || notAllowed;
       handler(request)
           .catch(error => {
               if (error.status != null) return error;
               return {body: String(error), status: 500};
           })
           .then(({body, status = 200, type = "text/plain"}) => {
               response.writeHead(status, {"Content-Type": type});
               if (body && body.pipe) body.pipe(response);
               else response.end(body);
           });
       }).listen(8000);

   async function notAllowed(request) {
       return {
           status: 405,
           body: `Method ${request.method} not allowed.`
       };
   }

* 405 エラー（特定のメソッドの処理を拒否）応答を返すだけのサーバーが起動する。
* リクエストハンドラーの ``Promise`` が却下された場合、``catch`` 呼び出しはエラーを応答オブジェクトに変換し、
  リクエストの処理に失敗したことを知らせるため、サーバーがエラー応答をクライアントに送り戻すようにする。
* レスポンス記述の ``status`` フィールドは省略可能。デフォルトで 200 が設定される。
* プロパティ ``type`` のコンテントタイプも省略可能。レスポンスはプレーンテキストであるとみなされる。

``body`` の値が

* 読み取り可能なストリームの場合、読み取り可能なストリームから書き込み可能なストリームに
  すべての内容を転送するために使用されるメソッド ``pipe`` がある。
* そうでない場合は ``null``（ボディなし）、文字列、バッファーのいずれかであると見なされ、
  応答のメソッド ``end`` に直接渡される。

----

関数 ``urlPath`` は、リクエスト URL に対応するファイルパスを知るために、
Node の組み込みモジュール ``url`` を使って URL を解析する。
これは ``/file.txt`` のようなパス名を受け取り、それを複号して %20 スタイルのエスケープコードを取り除き、
プログラムの作業ディレクトリーからの相対パスに解決する。

.. code:: javascript

   const {parse} = require("url");
   const {resolve, sep} = require("path");
   const baseDirectory = process.cwd();

   function urlPath(url) {
       let {pathname} = parse(url);
       let path = resolve(decodeURIComponent(pathname).slice(1));
       if (path != baseDirectory && !path.startsWith(baseDirectory + sep)) {
           throw {status: 403, body: "Forbidden"};
       }
       return path;
   }

ネットワークリクエストを受け付けるプログラムでは、セキュリティーについて気を配り始めなければならない。
この場合、注意していないとネットワークにファイルシステム全体を誤って公開する可能性がある。

パスは、例えば、親ディレクトリを参照するために ``../`` を含むことができる。
そのため、 ``/../secret_file`` のようなパスを要求することが明らかに問題のタネになる。
このような問題を避けるために、関数 ``urlPath`` は相対パスを解決する ``path`` モジュールの
関数 ``resolve`` を利用する。それで結果が作業ディレクトリー以下であることを検証する。

関数 ``process.cwd`` を使って作業ディレクトリーを見つけることができる。
``path`` パッケージの変数 ``sep`` は、システムのパス区切り文字だ。
パスがベースディレクトリーから始まっていない場合、この関数は、
リソースへのアクセスが禁止されていることを示す HTTP ステータスコード 403 を使って、
エラー応答オブジェクトを送出する。

ここでは、ディレクトリーを読むときにはファイルのリストを返し、
通常のファイルを読むときにはそのファイルの内容を返すように、GET メソッドを設定する。

----

ファイルの内容を返す際に、どのような Content-Type ヘッダーを設定するか。
ファイルは何でもありだから、サーバーはすべてのファイルに同じ Content-Type を返すことは許されない。

* ``mime`` パッケージは、多数のファイル拡張子に対する正しいタイプを知っている。

次の :command:`npm` コマンドは、サーバースクリプトが存在するディレクトリーに、
特定のバージョンの ``mime`` をインストールする：

.. code:: console

   $ npm install mime@2.2.0

----

要求されたファイルが存在しない場合、返すべき正しい HTTP ステータスコードは 404 だ。
ファイルの情報を調べる関数 ``stat`` を使って、ファイルが存在するかどうかと、
ディレクトリーであるかどうかの両方を調べる。

.. code:: javascript

   const {createReadStream} = require("fs");
   const {stat, readdir} = require("fs").promises;
   const mime = require("mime");

   methods.GET = async function(request) {
       let path = urlPath(request.url);
       let stats;
       try {
           stats = await stat(path);
       } catch (error) {
           if (error.code != "ENOENT") throw error;
           else return {status: 404, body: "File not found"};
       }

       if (stats.isDirectory()) {
           return {body: (await readdir(path)).join("\n")};
       } else {
           return {body: createReadStream(path),
                   type: mime.getType(path)};
       }
   };

* 関数 ``stat`` はディスクに触れる必要があり、時間がかかる可能性があるので、非同期だ。
* コールバック形式ではなく、``Promise`` を使用しているため、
  直接 ``fs`` からインポートするのではなく、``promises`` からインポートする必要がある。
* ファイルが存在しない場合、関数 ``stat`` はプロパティー ``code`` が ``"ENOENT"``
  のエラーオブジェクトを送出する。
* オブジェクト ``stats`` はファイルのサイズや修正日など、ファイルに関する情報を教えてくれる。
* メソッド ``isDirectory`` でディレクトリーなのか普通のファイルなのかを得る。
* ディレクトリー内のファイルの配列を読み込んでクライアントに返すには、関数 ``readdir`` を使う。
* 通常のファイルの場合は、関数 ``createReadStream`` で読み取り可能なストリームを作成し、
  ファイル名に ``mime`` パッケージが与える content type を添えて、それを本体として返す。

----

DELETE リクエストを処理するコードは、もう少し単純だ：

.. code:: javascript

   const {rmdir, unlink} = require("fs").promises;

   methods.DELETE = async function(request) {
       let path = urlPath(request.url);
       let stats;
       try {
           stats = await stat(path);
       } catch (error) {
           if (error.code != "ENOENT") throw error;
           else return {status: 204};
       }

       if (stats.isDirectory()) await rmdir(path);
       else await unlink(path);

       return {status: 204};
   };

* HTTP 応答にデータが含まれていない場合、ステータスコード 204 (no content) を使用してこれを示す。
  削除の応答では、操作が成功したかどうか以上の情報を送信する必要がない。ここで返すのが賢明だ。
* 存在しないファイルを削除しようとすると、エラーではなく成功のステータスコードが返ってくるが、これは不思議ではない。
  削除しようとするファイルが存在しない場合、リクエストの目的はすでに達成されていると言える。
  HTTP 規格では、リクエストを冪等にすることが推奨されている。
  つまり、同じリクエストを複数回行っても、一度だけ行ったときと同じ結果になることが望ましい。

----

以下、PUT リクエストのハンドラーだ：

.. code:: javascript

   const {createWriteStream} = require("fs");

   function pipeStream(from, to) {
       return new Promise((resolve, reject) => {
           from.on("error", reject);
           to.on("error", reject);
           to.on("finish", resolve);
           from.pipe(to);
       });
   }

   methods.PUT = async function(request) {
       let path = urlPath(request.url);
       await pipeStream(request, createWriteStream(path));
       return {status: 204};
   };

* 今回は、ファイルが存在するかどうかを確認する必要はない。ただ上書きするだけだ。
* 今回も ``pipe`` を使って、読み込み可能なストリームから書き込み可能なストリームにデータを移動する（今回はリクエストからファイルに移動）。
  しかし ``pipe`` は ``Promise`` を返すようには書かれていないので、
  ``pipeStream`` というラッパーを書いて、
  ``pipe`` を呼び出した結果の ``Promise`` を作成する。
* ファイルを開く際に何か問題が発生した場合、
  関数 ``createWriteStream`` はストリームを返すが、それはイベント ``error`` を発射する。
  ネットワークが落ちた場合など、リクエストに対する出力ストリームも失敗する可能性がある。
  そこで、両方のストリームのイベント ``error`` イベント同士を連絡して ``Promise`` を却下する。
  ``pipe`` は処理を終えると、出力ストリームを閉じ、イベント ``finish`` を発射する。
  この時点で ``Promise`` を正常に解決することができる。

----

* サーバー用の完全なスクリプトは <https://eloquentjavascript.net/code/file_server.js> にある。
  それをダウンロードして、依存関係をインストールした後、Node と一緒に実行すれば、
  読者自身のファイルサーバーを起動することができる。
* コマンドラインツール :command:`curl` を使って HTTP リクエストを行うことができる。
  次のセッションは自分のサーバーをテストする。

  * オプション ``-X`` はリクエストのメソッドを指定する。
  * オプション ``-d`` はリクエスト本体を含むのに使う。

  .. code:: console

     $ curl http://localhost:8000/file.txt
     File not found
     $ curl -X PUT -d hello http://localhost:8000/file.txt
     $ curl http://localhost:8000/file.txt
     hello
     $ curl -X DELETE http://localhost:8000/file.txt
     $ curl http://localhost:8000/file.txt
     File not found

  * 最初のリクエストは当該ファイルがまだ存在しないので失敗する。
  * PUT リクエストでファイルを作成すると、次回のリクエストでそれの取得に成功する。
  * DELETE リクエストでそれを削除すると、再びそのファイルは失われる。

Summary
======================================================================

Node_ は JavaScript をブラウザー以外のコンテキストで動作させることができるシステムだ。
元々はネットワークタスクのために設計されたもので、ネットワーク内のノードの役割を果たす。
あらゆる種類のスクリプトタスクにもまた適している。

NPM_ はパッケージを提供し、我々は :command:`npm` プログラムでそれらのパッケージを取得してインストールする。
Node_ には、ファイルシステムを操作するためのモジュール ``fs`` や、
HTTP サーバーを実行して HTTP リクエストを行うためのモジュール ``http`` など、
多くの組み込みモジュールが用意されている。

Node_ では、``readFileSync`` のような同期型の関数を明示的に使用しない限り、
すべての入出力は非同期で行われる。このような非同期関数を呼び出す際には、コールバック関数を提供し、
Node_ は準備ができたときにエラー値と結果（利用可能であれば）を伴ってそれらを呼び出す。

Exercises
======================================================================

Search tool
----------------------------------------------------------------------

**問題** コマンドラインから実行できる :command:`grep` に似た動作をする
Node スクリプトを書け。このスクリプトは、

* 最初のコマンドライン引数を正規表現として扱い、それ以降の引数を検索するファイルとして扱う。
* 内容が正規表現に合致するファイルの名前を出力するものとする。

これがうまくいったら、それを拡張して引数がディレクトリーの場合には
そのディレクトリーとそのサブディレクトリー内のすべてのファイルを検索しろ。

ファイルシステムの機能は、非同期型と同期型のどちらを使っても構わない。
複数の非同期動作を同時に要求するようにに設定することで多少の高速化が図れるかもしれないが、
ファイルシステムのほとんどは一度に一つのものしか読めないので、それほど良くはならない。

**解答** オリジナルの ``grep`` のような内容の出力に変えた：

.. code:: javascript

   // USAGE: node grep.js PATTERNS FILES

   const {readFile} = require("fs");
   const {readdir, stat} = require("fs").promises;
   const {sep} = require("path");

   if (process.argv.length < 4) {
       process.stderr.write(`Usage: node ${process.argv[1]} PATTERN [FILE]...\n`);
       process.exit(2);
   }

   const pattern = new RegExp(process.argv[2]);

   process.argv.slice(3).forEach(path => grep(path));

   async function grep(path){
       let stats = await stat(path);
       if(stats.isDirectory()){
           for(const i of await readdir(path)){
               await grep(path + sep + i);
           }
           return;
       }

       readFile(path, "utf8", (error, text) => {
           if(error) throw error;

           text.split("\n").forEach(line => {
               if (line.search(pattern) != -1) {
                   process.stdout.write(`${path}:${line}\n`);
               }
           });
       })
   }

Directory creation
----------------------------------------------------------------------

ファイルサーバーの DELETE メソッドはディレクトリーを削除することができるが、
サーバーには現在ディレクトリーを作成する方法を用意していない。

**問題** MKCOL メソッド ("make collection") のサポートを追加しろ。
MKCOL メソッドは ``fs`` モジュールから ``mkdir`` を呼び出してディレクトリーを作成する。
MKCOL は広く使われている HTTP メソッドではないが、WebDAV 規格には同じ目的で存在している。
WebDAV 規格とは HTTP の上に文書作成に適した規約の集合を規定するものだ。

**解答** クライアントはサーバーに次の方式でリクエストを送信する：

.. code:: console

   bash$ curl -X MKCOL http://localhost:8000/dirname

サーバー側のコードは次のようなものだ：

.. code:: javascript

   const { mkdir } = require("fs").promises;

   methods.MKCOL = async function (request) {
       await mkdir(urlPath(request.url), { recursive: true }, err => {
           if (err) throw err;
       });
       return { status: 204 };
   }

* 冪等性推奨方針とディレクトリー作成オプション ``recursive`` との相性が良い。
* 空文字列を渡しても入力なしエラーであるとはみなさなくていいだろう。

A public space on the web
----------------------------------------------------------------------

ファイルサーバーは、あらゆる種類のファイルを提供し、適切な Content-Type ヘッダーも含めることができるので、
ウェブサイトを提供するために使用することができる。

**問題** 簡単な JavaScript ファイルを含む基本的な HTML ページを書け。
ファイルサーバーが提供するディレクトリーにファイルを置き、ブラウザーで開け。

* 次に、上級者向けの課題として、あるいは週末のプロジェクトとして、
  本書で得た知識をすべて組み合わせて、Web サイトの中から Web サイトを変更するための、
  より使いやすいインターフェイスを構築しろ。
* HTML フォームを使って Web サイトを構成するファイルの内容を編集し、
  第 18 章で説明したように、HTTP リクエストを使ってサーバー上のファイルを更新できるようにしろ。
* まず、一つのファイルだけを編集可能にすることから始めろ。
* 次に、どのファイルを編集するかをユーザーが選択できるようにする。
  ファイルサーバーがディレクトリーの読み込み時にファイルのリストを返すことを利用しろ。

ファイルサーバーが公開しているコードで直接作業をしてはならない。
失敗したときにそこにあるファイルにダメージを与えがちだ。
代わりに、自分の作業は公開されているディレクトリーの外に置いておき、テストのときにそこにコピーしろ。

**解答** 作業が大体想像できる。

.. todo:: 時間を見つけてやる。

.. _Node: https://nodejs.org
.. _NPM: https://npmjs.org
