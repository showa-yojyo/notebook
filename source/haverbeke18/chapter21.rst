======================================================================
Project: Skill-Sharing Website
======================================================================

* この最終章では、スキル共有会で行われる講演を管理するためのウェブサイトを作ることを目標とする。
* 完全なコードは <https://eloquentjavascript.net/code/skillsharing.zip> からダウンロードできる。

.. contents:: ノート目次

Design
======================================================================

このプロジェクトには、Node.js 用に書かれたサーバー部分と、ブラウザー用に書かれたクライアント部分がある。

* サーバーは、システムのデータを保存し、クライアントに提供する。
  また、クライアント側のシステムを実装するファイルを提供する。
* サーバーは、次回の会議に提案された講演のリストを保持しており、クライアントはこのリストを表示する。
  各講演には、発表者名、タイトル、概要、コメントの配列が関連付けられている。
* クライアントでは、ユーザーが新しいトークを提案（リストに追加）したり、
  会話を削除したり、既存の会話にコメントしたりすることができる。
* ユーザーがこのような変更を行うたびに、クライアントは HTTP リクエストを行い、サーバーにそのことを伝える。
* アプリケーションは、現在提案されている会話とそのコメントのライブビューを表示するようにできている。
  どこかの誰かが新しい会話を投稿したり、コメントを追加したりすると、
  そのページをブラウザーで開いているすべての閲覧者がすぐにその変更を確認できるようにする。

これには少々の問題がある。ウェブサーバーがクライアントと接続する方法がなく、
また、どのクライアントが特定のウェブサイトを現在見ているかを知る良い方法もない。

この問題に対する一般的な解決策は **long polling** と呼ばれるものだ。

* これは偶然にも Node_ の設計動機の一つだった。

Long polling
======================================================================

* 何かが変更されたことをクライアントに即座に通知するためには、そのクライアントとの接続が必要だ。
  ウェブブラウザーは通常、接続を受け付けない、クライアントは中継器の背後にいることが多く、
  そのような接続は遮断されてしまうため、サーバーがこの接続を開始することは現実的ではない。
* クライアントが接続を開始し、サーバーが必要なときに情報を送信できるように接続を維持するようにすることができる。
  しかし、HTTP リクエストでは、クライアントがリクエストを送信し、
  サーバーが単一の応答を返してそれだけという単純な情報の流れしかできない。
* 最近のブラウザーでサポートされている WebSockets という技術は、
  任意のデータ交換のために接続を開くことを可能にするが、これを適切に使用するのは少々難しい。

この章ではより単純な手法である long polling を使う。

* クライアントが通常の HTTP リクエストを使ってサーバーに継続的に新しい情報を要求し、
  サーバーは新しい情報がない場合には回答を保留する。

クライアントが定常的にポーリング要求を開いているようにしてある限り、
情報が入手可能になってからサーバーから情報を素早く受け取る。

#. 例えば、Fatma がブラウザーでスキルシェアのアプリケーションを開いている場合、
   そのブラウザーは更新要求を行い、応答を待っていることになる。
#. Iman が Extreme Downhill Unicycling の会話を投稿すると、
#. サーバーは Fatma が更新を待ち構えていることに気づき、
   保留中のリクエストに新しい会話を含む応答を送信する。
#. Fatma のブラウザーはそのデータを受け取り、画面を更新して会話を表示する。

接続のタイムアウトを防ぐために、long polling の技法では通常、各リクエストに最大時間を設ける。
それを過ぎると、サーバーは何も報告することがなくてもとにかく応答し、
その後、クライアントは新しいリクエストを開始する。
周期的にリクエストを再開することで、クライアントは一時的な接続障害やサーバーの問題から回復できるようになり、
技術の堅牢性が向上する。

Long polling を使用している多忙なサーバーでは、何千ものリクエスト待ち、
したがって TCP 接続が開いていることがある。
このようなシステムには、それぞれの接続に個別の制御スレッドを作成することなく、
多くの接続を簡単に管理できる Node_ が適している。

HTTP interface
======================================================================

サーバーやクライアントの設計を始める前に、両者が接触するポイントである、
通信するための HTTP インターフェイスについて考える。

* リクエスト本体と応答本体の書式として JSON を採用する。

  * 第 20 章でやったように HTTP メソッドとヘッダーを上手く利用する。
  * インターフェイスはパス ``/talks`` の周りに構成する。
  * ``/talks`` で始まらないパスを、クライアント側システム用の
    HTML や JavaScript コードなどの静的なファイルを供するのに用いる。

``/talks`` に対する GET リクエストは次のような JSON を返す：

.. code:: json

   [{"title": "Unituning",
     "presenter": "Jamal",
     "summary": "Modifying your cycle for extra style",
     "comments": []}]

新しい会話を作成するには、``/talks/Unituning`` のような URL への PUT リクエストを行う。
二番目の ``/`` の後の部分が会話の名前になる。
PUT リクエストの本体に、プロパティー ``presenter`` と ``summary`` を持つ JSON オブジェクトが含まれている。

会話の名前は URL 中に現れることが許されない空白文字やその他の文字を含むかもしれないので、
そのような URL を構築するときに文字列を関数 ``encodeURIComponent`` で符号化する必要がある。

.. code:: javascript

   console.log("/talks/" + encodeURIComponent("How to Idle"));

アイドリングに関する会話を作りたいというリクエストは次のようなものだ：

.. code:: http

   PUT /talks/How%20to%20Idle HTTP/1.1
   Content-Type: application/json
   Content-Length: 92

   {"presenter": "Maureen",
    "summary": "Standing still on a unicycle"}

このような URL は、会話の JSON 表現を取得する GET リクエストや、
会話を削除する DELETE リクエストもサポートする。

会話にコメントを追加するには、``/talks/Unituning/comments`` のような URL への POST リクエストを使用し、
JSON 本体にプロパティー ``author`` と ``message`` があるようにして行う。

.. code:: http

   POST /talks/Unituning/comments HTTP/1.1
   Content-Type: application/json
   Content-Length: 72

   {"author": "Iman",
    "message": "Will you talk about raising a cycle?"}

Long polling をサポートするために ``/talks`` への GET リクエストに追加のヘッダーを含めることを許す。
このヘッダーは、新しい情報が得られない場合に応答を遅らせるようにサーバに知らせるものだ。
``ETag`` と ``If-None-Match`` という、通常キャッシングを管理するためのヘッダーをペアで使用する。

* ``ETag`` は Entity Tag の意。

サーバーは、レスポンスに ``ETag`` ヘッダーを含めても構わない。
それの値とは、リソースの現在のバージョンを識別する文字列だ。
クライアントは、後でそのリソースを再リクエストする際に、
同じ文字列を値とする ``If-None-Match`` ヘッダーを含めることで、条件付きリクエストを行ってもよい。
リソースが変更されていない場合、サーバーは「変更されていない」を意味するステータスコード 304 で応答し、
キャッシュされたバージョンが依然として最新であることをクライアントに教える。
タグが合致しない場合、サーバーは通常通り応答する。

このように、クライアントがサーバーに会話リストのどのバージョンを持っているかを教え、
サーバーはそのリストが変更されたときに限り応答する仕組みが必要だ。
ただし、すぐに　304 応答を返すのではなく、サーバーは応答を一時停止し、
何か新しいものが利用可能になったときや、所定の時間が経過したときにのみ応答するべきだ。
長時間のポーリングリクエストを通常の条件付きリクエストと区別するために、
``Prefer: wait=90`` という別のヘッダーを与え、クライアントがレスポンスを 90 秒まで待ってもよいことをサーバーに言う。

サーバーは、会話が変わるたびに更新されるバージョンを保持し、それを ``ETag`` の値として使う。
クライアントは、このようなリクエストを行うことで、会話が変更されたときに通知される。

.. code:: http

   GET /talks HTTP/1.1
   If-None-Match: "4"
   Prefer: wait=90

   (time passes)

   HTTP/1.1 200 OK
   Content-Type: application/json
   ETag: "5"
   Content-Length: 295

   [....]

ここで説明したプロトコルでは、いかなるアクセス制御をも行わない。
誰でもコメントしたり、会話を修正したり、削除したりできる。

The server
======================================================================

まずはサーバー側の構築から始める。本節のコードは Node.js 上で動作する。

Routing
----------------------------------------------------------------------

``createServer`` を使って HTTP サーバーを開始する。
新しいリクエストを処理する関数では、我々がサポートしている、
メソッドとパスで決定されるさまざまなリクエストを区別しなければならない。
これを長い ``if`` 文の連鎖で行うこともできるが、もっと良い方法がある。

中継器とは、リクエストを、それを処理できる関数にディスパッチするのを助けるコンポーネントだ。

例えば、正規表現 ``^\/talks\/([^\/]+)$`` に合致するパスを持つ PUT リクエストは、
特定の関数で処理できるように中継器に知らせられる。
さらに、正規表現の括弧で囲まれたパスの意味のある部分を抽出して、処理関数に渡すこともできる。

* ここでは会話名

NPM_ には多くの優れた中継器パッケージがあるが、ここでは原理を理解するために自分自身で書く。

次のコードが ``router.js`` で、サーバーモジュールが必要とするものだ：

.. code:: javascript

   // router.js

   const {parse} = require("url");

   module.exports = class Router {
       constructor() {
           this.routes = [];
       }

       add(method, url, handler) {
           this.routes.push({method, url, handler});
       }

       resolve(context, request) {
           let path = parse(request.url).pathname;
           for (let {method, url, handler} of this.routes) {
               let match = url.exec(path);
               if (!match || request.method != method) continue;
               let urlParts = match.slice(1).map(decodeURIComponent);
               return handler(context, ...urlParts, request);
           }
           return null;
       }
   };

このモジュール はクラス ``Router`` をエクスポートしている。

* メソッド ``add`` で新しいハンドラーを登録する。
* メソッド ``resolve`` でリクエストを解決する。

  * ハンドラーが見つかった場合は応答を返し、そうでない場合は ``null`` を返す。
  * 合致するものが見つかるまで、定義順に経路を一つずつ試す。

ハンドラ関数ーは ``context`` の値 (ここではサーバーのインスタンス)、
正規表現で定義されたグループの合致文字列、そしてリクエストオブジェクトを引数として呼び出される。
生の URL には ``%20`` スタイルのコードを含むかもしれないので、文字列を URL 用に複号しないといけない。

Serving files
----------------------------------------------------------------------

リクエストが中継器で定義されたリクエスト型タイプのどれにも合致マッチしない場合、
サーバーはそれを ``public`` ディレクトリー内のファイルに対するリクエストとして解釈しなければならない。

* 第 20 章で定義したファイルサーバーを使用してこのようなファイルを提供することもできるが、
  ファイルに対する PUT および DELETE リクエストをサポートする必要もなく、
  またキャッシングのサポートのような高度な機能が欲しい。

そこで、代わりに NPM_ のしっかりとした、よくテストされた静的ファイルサーバーとして ``ecstatic`` を採用する。
このパッケージは、設定オブジェクトを使ってリクエスト処理関数を呼び出せる関数をエクスポートしている。

オプション ``root`` を使用して、サーバーがどこでファイルを探すべきかを教える。
処理関数は、リクエストと応答の引数を取り、``createServer`` に直接渡すことで、
ファイルだけを提供するサーバーを作成できる。
しかし、特別に処理すべきリクエストを最初にチェックしたいので、別の関数でラップする：

.. code:: javascript

   const {createServer} = require("http");
   const Router = require("./router");
   const ecstatic = require("ecstatic");

   const router = new Router();
   const defaultHeaders = {"Content-Type": "text/plain"};

   class SkillShareServer {
       constructor(talks) {
           this.talks = talks;
           this.version = 0;
           this.waiting = [];

           let fileServer = ecstatic({root: "./public"});
           this.server = createServer((request, response) => {
               let resolved = router.resolve(this, request);
               if (resolved) {
                   resolved.catch(error => {
                       if (error.status != null) return error;
                       return {body: String(error), status: 500};
                   }).then(({body,
                       status = 200,
                       headers = defaultHeaders}) => {
                       response.writeHead(status, headers);
                       response.end(body);
                   });
               } else {
                   fileServer(request, response);
               }
           });
       }

       start(port) {
           this.server.listen(port);
       }

       stop() {
           this.server.close();
       }
   }

この関数は、前の章のファイルサーバーと同様に、レスポンスを表すオブジェクトに解決する
``Promise`` を返すハンドラーを使用する。その状態を保持するオブジェクトでそのサーバーをラップする。

Talks as resources
----------------------------------------------------------------------

提案された会話はサーバーのプロパティー ``talks`` に格納されている。
プロパティー名がトークの題名であるようなオブジェクトだ。
これらは HTTP リソースとして ``/talks/[title]`` という名前で公開するので、
クライアントが会話を操作するための雑多なメソッドを実装するハンドラーを中継器に追加する必要がある。

会話一つを取得するリクエストのハンドラーは、会話を検索し、その JSON データを返すか、
そうでなければ 404 エラーを返さねばならない。

.. code:: javascript

   const talkPath = /^\/talks\/([^\/]+)$/;
   router.add("GET", talkPath, async (server, title) => {
       if (title in server.talks) {
           return {body: JSON.stringify(server.talks[title]),
                   headers: {"Content-Type": "application/json"}};
       } else {
           return {status: 404, body: `No talk '${title}' found`};
       }
   });

----

会話を削除するには、``takings`` オブジェクトから削除する。

.. code:: javascript

   router.add("DELETE", talkPath, async (server, title) => {
       if (title in server.talks) {
           delete server.talks[title];
           server.updated();
       }
       return {status: 204};
   });

* 後で定義するメソッド ``updated`` は、待機中の long polling リクエストに変更を通知するものだ。

----

リクエスト本体の内容を得るために、関数 ``readStream`` を定義する。
これは読み取り可能なストリームからすべての内容を読み取り、文字列に解決する ``Promise`` を返す。

.. code:: javascript

   function readStream(stream) {
       return new Promise((resolve, reject) => {
           let data = "";
           stream.on("error", reject);
           stream.on("data", chunk => data += chunk.toString());
           stream.on("end", () => resolve(data));
       });
   }

----

リクエスト本体を読み取る必要のあるハンドラーの一つに、新しい会話を作成する際に使用される PUT ハンドラーがある。
PUT ハンドラーは渡されたデータに文字列プロパティー ``presenter`` と ``summary`` があることを確認する必要がある。

* システム外からのデータは壊れていないとは限らない。

データが有効でありそうならば、ハンドラーは新しい会話を表すオブジェクトを ``talks`` に格納し、
場合によっては既存のタイトルの会話を上書きし、再び ``updated`` を呼び出す。

.. code:: javascript

   router.add("PUT", talkPath,
              async (server, title, request) => {
       let requestBody = await readStream(request);
       let talk;

       try { talk = JSON.parse(requestBody); }
       catch (_) { return {status: 400, body: "Invalid JSON"}; }

       if (!talk ||
           typeof talk.presenter != "string" ||
           typeof talk.summary != "string") {
           return {status: 400, body: "Bad talk data"};
       }

       server.talks[title] = {title,
                              presenter: talk.presenter,
                              summary: talk.summary,
                              comments: []};
       server.updated();
       return {status: 204};
   });

----

会話へのコメントの追加も同様だ。
``readStream`` を呼び出してリクエストの内容を取得し、結果のデータを検証して、
有効そうであればコメントとして保存する：

.. code:: javascript

   router.add("POST", /^\/talks\/([^\/]+)\/comments$/,
              async (server, title, request) => {
       let requestBody = await readStream(request);
       let comment;
       try { comment = JSON.parse(requestBody); }
       catch (_) { return {status: 400, body: "Invalid JSON"}; }

       if (!comment ||
           typeof comment.author != "string" ||
           typeof comment.message != "string") {
           return {status: 400, body: "Bad comment data"};
       } else if (title in server.talks) {
           server.talks[title].comments.push(comment);
           server.updated();
           return {status: 204};
       } else {
           return {status: 404, body: `No talk '${title}' found`};
       }
   });

* 存在しない会話にコメントを追加しようとすると、404 エラーが返る。

Long polling support
----------------------------------------------------------------------

このサーバーのいちばん面白い点は long polling 部だ。

``/talks`` に対する GET リクエストが来ると、それは通常のリクエストである場合もあれば、
long polling のそれである場合もある。
クライアントに ``talks`` の配列を送信しなければならない箇所が複数あるので、
まず配列を構築し、ヘッダー ``ETag`` を応答に含めるヘルパーメソッドを定義する：

.. code:: javascript

   SkillShareServer.prototype.talkResponse = function() {
       let talks = [];
       for (let title of Object.keys(this.talks)) {
           talks.push(this.talks[title]);
       }
       return {
           body: JSON.stringify(talks),
           headers: {"Content-Type": "application/json",
                     "ETag": `"${this.version}"`,
                     "Cache-Control": "no-store"}
       };
   };

----

ハンドラーそれ自身はリクエストヘッダーを見て、``If-None-Match`` と ``Prefer`` が存在するかどうかを確認する必要がある。

* Node は、大文字と小文字を区別しないように指定されたヘッダーを、小文字の名前で保存する。

.. code:: javascript

   router.add("GET", /^\/talks$/, async (server, request) => {
       let tag = /"(.*)"/.exec(request.headers["if-none-match"]);
       let wait = /\bwait=(\d+)/.exec(request.headers["prefer"]);

       if (!tag || tag[1] != server.version) {
           return server.talkResponse();
       } else if (!wait) {
           return {status: 304};
       } else {
           return server.waitForChanges(Number(wait[1]));
       }
   });

* タグが指定されていない場合や、サーバーの現在のバージョンと一致しないタグが指定されている場合、
  ハンドラーは会話のリストで応答する。
* リクエストが条件付きで、会話が変更されなかった場合は、
  ``Prefer`` ヘッダーを参照して、応答を遅らせるべきか、すぐにするべきかを判断する。

遅延したリクエストに対するコールバック関数は、サーバーの待機配列に格納され、
何かが起こったときに通知できるようになっている。

メソッド ``waitForChanges`` は、リクエストが十分に待たされたときに 304 ステータスで応答するためのタイマーを即座に設定する。

.. code:: javascript

   SkillShareServer.prototype.waitForChanges = function(time) {
       return new Promise(resolve => {
           this.waiting.push(resolve);
           setTimeout(() => {
               if (!this.waiting.includes(resolve)) return;
               this.waiting = this.waiting.filter(r => r != resolve);
               resolve({status: 304});
           }, time * 1000);
       });
   };

----

メソッド ``updated`` で変更を登録すると、プロパティー ``version`` の値を上げて、
待機中のリクエストすべてを叩き起こす。

.. code:: javascript

   SkillShareServer.prototype.updated = function() {
       this.version++;
       let response = this.talkResponse();
       this.waiting.forEach(resolve => resolve(response));
       this.waiting = [];
   };

----

サーバーコードは以上だ。

``SkillShareServer`` のインスタンスを作成し、ポート 8000 で起動すると、
生成された HTTP サーバーは ``public`` サブディレクトリーのファイルと、
``/talks`` URL の会話管理インターフェースをサーブするようになる。

.. code:: javascript

   new SkillShareServer(Object.create(null)).start(8000);

The client
======================================================================

スキルシェアサイトのクライアント側を、小さな HTML ページ、スタイルシート、
JavaScript ファイルで構成する。

HTML
----------------------------------------------------------------------

* ディレクトリーに対応するパスに直接リクエストがあった場合、Web サーバーでは
  ファイル ``index.html`` を提供しようとすることが広く行われている。
  ``ecstatic`` もこの慣習をサポートしている。
* パス ``/`` へのリクエストが行われると、サーバーはファイル
  ``./public/index.html`` を探し、見つかればそのファイルを返す。
  したがって、ブラウザーがサーバーを指したときにページを表示したい場合は、
  ファイル ``public/index.html`` を置く必要がある。

.. code:: html

   <!doctype html>
   <meta charset="utf-8">
   <title>Skill Sharing</title>
   <link rel="stylesheet" href="skillsharing.css">

   <h1>Skill Sharing</h1>

   <script src="skillsharing_client.js"></script>

* スタイルシートでは、特に、間違いなく会話の間に隙間を設ける。
* 最下部で読み込むスクリプトは、ページの最上部に見出しを追加し、
  クライアントアプリケーションを含む。

Actions
----------------------------------------------------------------------

アプリケーションの状態は、会話のリストとユーザーの名前で構成されており、
``{talks, user}`` オブジェクトに格納する。

ユーザーインターフェースには状態を直接操作したり、HTTP リクエストを送信したりすることは認めず、
ユーザーが何をしようとしているのかを記述するアクションを発信させる。

関数 ``handleAction`` はそれを実現する。
状態の更新はとても単純なので、状態の変更も同じ関数で処理できる：

.. code:: javascript

   function handleAction(state, action) {
       if (action.type == "setUser") {
           localStorage.setItem("userName", action.user);
           return Object.assign({}, state, {user: action.user});
       } else if (action.type == "setTalks") {
           return Object.assign({}, state, {talks: action.talks});
       } else if (action.type == "newTalk") {
           fetchOK(talkURL(action.title), {
               method: "PUT",
               headers: {"Content-Type": "application/json"},
               body: JSON.stringify({
                   presenter: state.user,
                   summary: action.summary
               })
           }).catch(reportError);
       } else if (action.type == "deleteTalk") {
           fetchOK(talkURL(action.talk), {method: "DELETE"})
               .catch(reportError);
       } else if (action.type == "newComment") {
            fetchOK(talkURL(action.talk) + "/comments", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({
                    author: state.user,
                    message: action.message
                })
           }).catch(reportError);
       }
       return state;
   }

* ユーザーの名前を ``localStorage`` に保存し、ページが読み込まれたときに復元する。

サーバーを巻き込む必要のあるアクションは、前述の HTTP インターフェイスに
``fetch`` を使ってネットワークリクエストを行う。
ラッパー関数である ``fetchOK`` を呼び出し、サーバーがエラーコードを返したときに、
返された ``Promise`` が却下されるようにする。

.. code:: javascript

   function fetchOK(url, options) {
       return fetch(url, options).then(response => {
           if (response.status < 400) return response;
           else throw new Error(response.statusText);
       });
   }

* ヘルパー関数 ``talkURL`` (p. 396) は、指定された題の会話の URL を構築するのに使う。
* 関数 ``reportError`` (p. 396) を定義し、リクエストが失敗したときに、
  少なくともユーザーに何か問題があったことを伝えるダイアログボックスを表示する。

Rendering components
----------------------------------------------------------------------

第 19 章で見たのと同じようなアプローチで、アプリケーションをコンポーネントに分割する。
クラスとしてではなく、DOM ノードを直接返す関数として定義すれば十分なものもある。
例えば、ユーザーが名前を入力するフィールドを表示するコンポーネントがそうだ：

.. code:: javascript

   function renderUserField(name, dispatch) {
       return elt("label", {}, "Your name: ", elt("input", {
           type: "text",
           value: name,
           onchange(event) {
               dispatch({type: "setUser", user: event.target.value});
           }
       }));
   }

* DOM 要素を構築する関数 ``elt`` は第 19 章で使用したものとする。

----

同様の関数は、コメントのリストと新しいコメントを追加するためのフォームを含む関数
``renderTalk`` (p. 397) がある。

* イベント ``submit`` のハンドラーは ``form.reset`` を呼び出し、
  アクション ``newComment`` を作成した後にフォームの内容を消去する。
* 中程度の複雑な DOM を作成する場合、このプログラミングスタイルはかなり厄介に見える。

  JSX と呼ばれる広く使われている（非標準の）JavaScript の拡張機能があり、
  これを使うとスクリプトの中に直接 HTMLを書くことができ、
  このようなコードをよりきれいにすることができる。
  このようなコードを実際に実行するには、
  スクリプト上でプログラムを実行して、疑似 HTML を、ここで使用しているような
  JavaScript の関数呼び出しに変換する必要がある。

----

コメントはより単純にレンダリング (pp. 397-398) する。

----

ユーザーが新しい会話を作成するためのフォームは次のようにレンダリングする：

.. code:: javascript

   function renderTalkForm(dispatch) {
       let title = elt("input", {type: "text"});
       let summary = elt("input", {type: "text"});

       return elt("form", {
           onsubmit(event) {
               event.preventDefault();
               dispatch({type: "newTalk",
                         title: title.value,
                         summary: summary.value});
               event.target.reset();
               }
           },
           elt("h3", null, "Submit a Talk"),
           elt("label", null, "Title: ", title),
           elt("label", null, "Summary: ", summary),
           elt("button", {type: "submit"}, "Submit"));
   }

Polling
----------------------------------------------------------------------

アプリケーションを起動するには、現在の会話が必要だ。
最初のロードは long polling 処理（ロード時の ``ETag`` をポーリング時に使用する必要がある）と密接に関係しているため、
サーバーの ``/talks`` をポーリングし続け、会話の新しい集合が利用可能になったときに
コールバック関数を呼び出す関数 ``pollTalks`` を書く。

.. code:: javascript

   async function pollTalks(update) {
       let tag = undefined;
       for (;;) {
           let response;
           try {
               response = await fetchOK("/talks", {
                   headers: tag && {"If-None-Match": tag,
                                    "Prefer": "wait=90"}
               });
           } catch (e) {
               console.log("Request failed: " + e);
               await new Promise(resolve => setTimeout(resolve, 500));
               continue;
           }

           if (response.status == 304) continue;

           tag = response.headers.get("ETag");
           update(await response.json());
       }
   }

これは非同期関数なので、ループしてリクエストを待つのは簡単だ。

この関数は無限ループを実行し、反復するごとに会話のリストを取得する。
普通に取得する場合と、最初のリクエストでない場合は long polling リクエストとなるように、
ヘッダーを含めて取得する場合がある。

* リクエストが失敗すると、この関数はしばらく待ってから再試行する。
  これにより、ネットワーク接続が一時的に切断され、
  その後復帰した場合でも、アプリケーションは回復して更新を続けることができる。
* ``setTimeout`` で解決した ``Promise`` は、非同期関数を強制的に待機状態にするためのものだ。
* サーバーが 304 を返してきた場合、それは long polling リクエストがタイムアウトしたことを意味する。
  そうなれば、この関数は直ちに次のリクエストを開始すればよい。
* レスポンスが 200 であれば、その本体は JSON として読み込まれてコールバックに渡され、
  その ``ETag`` ヘッダー値を次の反復のために保存する。

The application
----------------------------------------------------------------------

クラス ``SkillShareApp`` (pp. 399-400) は、ユーザーインターフェース全体を結びつける。

* 会話が変わると、このコンポーネントは会話すべてを再描画する。単純で無駄が多い。
  この点については演習でなんとかする。

----

このようにして、アプリケーションを起動する：

.. code:: javascript

   function runApp() {
       let user = localStorage.getItem("userName") || "Anon";
       let state, app;

       function dispatch(action) {
           state = handleAction(state, action);
           app.syncState(state);
       }

       pollTalks(talks => {
           if (!app) {
               state = {user, talks};
               app = new SkillShareApp(state, dispatch);
               document.body.appendChild(app.dom);
           } else {
               dispatch({type: "setTalks", talks});
           }
       }).catch(reportError);
   }

   runApp();

サーバーを起動し、<http://localhost:8000> 用にブラウザーウィンドウを二つ隣り合わせに開くと、
一方のウィンドウで実行したアクションがもう一方のウィンドウですぐに表示されることがわかる。

Exercises
======================================================================

Disk persistence
----------------------------------------------------------------------

技能共有サーバーは、データをメモリー上に保持している。
クラッシュしたり、何らかの理由で再起動したりすると、すべての会話やコメントが失われる。

**問題** 会話データをディスクに保存し、再起動時に自動的にデータを再読み込みするように拡張しろ。
効率を気にすることなく、動作する最も単純なことをしろ。

**解答** 会話データを JSON にシリアライズしてダンプやロードしたい。

永続データを更新するタイミングは ``updated`` とする。

.. code:: javascript

    const data_path = './talks.json';

    SkillShareServer.prototype.updated = function () {
        // ...
        writeFile(data_path, JSON.stringify(this.talks), 'utf8', (err) => {
            if (err) throw err;
        });
    };

``SkillShareServer`` のコンストラクターにちょうど ``talks`` 引数がある。
この設計をそのまま活用する。

.. code:: javascript

   const { readFile } = require("fs");

   let talks = Object.create(null);
   try{
       readFile(data_path, 'utf8', (err, data) => {
           if (err) throw err;
           Object.assign(talks, JSON.parse(data));
       });
   }
   catch(e){
       console.log("Failed to load", data_path);
       throw e;
   }

   new SkillShareServer(talks).start(8000);

* 例外処理は実のところ書く必要がない。拡張するときに初めて役に立つ。
* ``Object.assign`` の使用理由については巻末のヒントを参照。

Comment field resets
----------------------------------------------------------------------

会話の全面的な再描画は、通常、DOM ノードとその同一の代替物との違いを見分けることができないので、かなりうまくいく。
しかし、例外もある。一方のブラウザーのウィンドウでトークのコメント欄に何かを入力し始め、
他方のウィンドウでその会話にコメントを追加すると、最初のウィンドウのフィールドが再描画され、
中身とフォーカスの両方が消える。
複数の人が同時にコメントを付けているような熱い議論の場では、これは迷惑だ。

**問題** これを解決する方法を考えろ。

**解答** ``SkillShareServer.syncState`` の処理中で ``this.talks`` と
``state.talks`` の差分を検出して適切な UI 更新を行う。

``this.talks`` が未定義のときはコンストラクターから呼び出されているので、
従来どおりの全更新をする：

.. code:: javascript

   if (this.talks === undefined) {
       this.talkDOM.textContent = "";
       for (let talk of state.talks) {
           this.talkDOM.appendChild(
               renderTalk(talk, this.dispatch));
       }
       this.talks = state.talks;
       return;
   }

次は long polling のいちばん頻繁に発生する場合で、何の変更もないときの処理をする：

.. code:: javascript

   if(this.talks == state.talks){
       return;
   }

本題は会話の配列に変化が生じているときの処理だ。
会話が増えているときには、その会話だけを DOM および ``this.talks`` に追加する：

.. code:: javascript

   const numTalksOld = this.talks.length;
   const numTalksNew = state.talks.length;
   if (numTalksNew > numTalksOld) {
       const talk = state.talks[state.talks.length - 1];
       this.talkDOM.appendChild(
           renderTalk(talk, this.dispatch));
       this.talks.push(talk);
       return;
   }

* 会話は一度に一つしか追加されないと仮定する。
* 追加された会話データは配列の末尾にあるため、このような簡単なコードでよい。
  また、画面でも追加位置は末尾とする。

会話の削除は少しややこしい。会話の比較を ``title`` に基づいて行うのでこういう感じになる：

.. code:: javascript

   if (numTalksNew < numTalksOld) {
       const setOld = new Set(this.talks.map(i => i.title));
       const setNew = new Set(state.talks.map(i => i.title));
       setNew.forEach(i => setOld.delete(i));
       const targetTitle = Array.from(setOld)[0];
       for(const t of this.talkDOM.querySelectorAll("section")){
           if(t.textContent.startsWith(targetTitle)){
               this.talkDOM.removeChild(t);
               break;
           }
       }
       this.talks = this.talks.filter(i => i.title != targetTitle);
       return;
   }

* 会話は一度に一つしか削除されないと仮定する。
* 私（読者）のコードでは集合に基づいて差分会話を発見するので、
  それに対応する DOM 要素がどこにあるのかが添字ではわからない。
  したがって ``querySelectorAll`` してから題名 ``title`` を比較することになった。

  * ``==`` ではなく ``startsWith`` を用いているのは、ノード ``<h2>`` の造りが悪いから。
    題名文字列以外の要素を含んでいるため、先頭が一致していれば十分と判断する。
  * 同じ題名の会話は存在し得ないが、題名の冒頭が同じ会話の組は存在し得る。このときはまともに動かない。

* 最後の ``filter`` は C++ の ``remove_if`` に相当する書き方がわからないからこう書いた。

会話内容が更新されるとき、すなわちコメントが増えるときの処理を次のようにする：

.. code:: javascript

   for(let i = 0; i < numTalksNew; ++i){
       const commentsOld = this.talks[i].comments;
       const commentsNew = state.talks[i].comments;
       if(commentsOld.length < commentsNew.length){
           const commentLast = commentsNew[commentsNew.length - 1];
           const t = this.talkDOM.querySelectorAll("section")[i];
           const f = t.querySelector("form");
           t.insertBefore(renderComment(commentLast), f);
           commentsOld.push(commentLast);
           return;
       }
   }

* コメントは一度に一つしか追加されないと仮定する。
* コメントの DOM の追加位置に注意。
  所属する会話を表す ``<section>`` 内の ``<form>`` の直前が正しい。

.. _Node: https://nodejs.org
.. _NPM: https://npmjs.org
