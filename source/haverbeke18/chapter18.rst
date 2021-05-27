======================================================================
HTTP and Forms
======================================================================

HTTP についてさらに詳しく説明し、ブラウザーの JavaScript がどうアクセスするのかを説明する。

.. contents:: ノート目次

The protocol
======================================================================

ブラウザーのアドレスバーに ``eloquentjavascript.net/18_http.html`` と入力すると、

#. ブラウザーはまず ``eloquentjavascript`` に関連するサーバーのアドレスを検索する。
#. （この場合はポート番号の明示的な指定がないので既定の）80 番ポートで TCP 接続を試みる。
#. そのサーバーが存在し、かつ接続が受け入れられると、ブラウザーは次のようなものを送信する：

.. code:: http

   GET /18_http.html HTTP/1.1
   Host: eloquentjavascript.net
   User-Agent: Your browser's name

すると、サーバーは同じ接続を介して次のように応答する：

.. code:: http

   HTTP/1.1 200 OK
   Content-Length: 65585
   Content-Type: text/html
   Last-Modified: Mon, 08 Jan 2018 10:29:45 GMT

   <!doctype html>
   ... the rest of the document

----

ブラウザーは、空行の後の返答の一部である本体を受け取り、一体の HTML 文書として表示する。

* クライアントから送られてくる情報を **リクエスト** という。
  次の行で始まる：

  .. code:: text

     GET /18_http.html HTTP/1.1

  * 最初の単語はリクエストのメソッドだ。この ``GET`` は指定されたリソースを取得したいことを意味する。

    * ``GET`` の他に一般的なメソッドは：

      * ``DELETE`` はリソースの削除を、
      * ``PUT`` はリソースの作成または置換、
      * ``POST`` はリソースへの情報送信をそれぞれ意味する。

    * サーバーには、受信したリクエストすべてを実行する義務がないことに注意すること。

* メソッドの次の部分は、リクエストが適用されるリソースのパスだ。

  * いちばん単純な場合ではリソースは単にサーバーにあるファイルだが、
    プロトコルはいつでもそうであることを求めていない。
    ファイルであるかのように転送されるものなら何でも構わない。
  * サーバーの多くはその場で応答を生成する。
    例えば ``https://github.com/marijnh`` を開くと、GitHub のサーバーは

    #. データベースから ``marijhn`` というユーザーを検索する。
    #. 見つかったらそのユーザーのプロフィールページを生成して、
    #. それをクライアントに送り返す。

* リソースパスの次の部分 ``HTTP/1.1`` は、使用している HTTP のバージョンを示す。

  * 実際にはウェブサイトの多くで HTTP2 を使用していて、
    これは 1.1 と同じコンセプトをサポートしているが、高速化のためにかなり複雑なものだ。
  * ブラウザーは与えられたサーバーと通信する際に自動的に適当なバージョンに切り替える。
    どのバージョンを使ってもリクエストの結果は同じだ。
  * 1.1 のほうがわかりやすく、扱いも簡単であるので、それに焦点を当てる。

----

サーバーからの応答は、バージョンから始まり、応答のステータスがその後に続く。
最初は三桁のステータスコードで、それから人間が読める文字列が続く。

.. code::text

   HTTP/1.1 200 OK

* 2 で始まるステータスはリクエストが成功したことを意味する。
* 4 で始まるステータスはリクエストに問題があったことを意味する。

  * 404 はもっとも有名な HTTP ステータスコードで、リソースが見つからないことを意味する。

* 5 で始まるコードは、サーバーでエラーが発生したことをいみする。

リクエストや応答の最初の行の次は任意の行数で **ヘッダー** が来る。

* ヘッダーとは ``name: value`` 形式の行で、リクエストや応答に関する追加情報だ。

  .. code:: text

     Content-Length: 65585
     Content-Type: text/html
     Last-Modified: Thu, 04 Jan 2018 14:05:30 GMT

  * 上の例では応答文書のサイズ、種類、最終更新に関する情報を送っている。
  * ``Host`` など必須のものもあるが、ヘッダーのほとんどは、
    クライアントとサーバーがリクエストや応答に含めるかどうかを自由に決めることができる。

----

リクエストと応答のどちらにおいても、ヘッダーの後には空行が入る。
その後に送信されるデータを含む本体が続く。

* ``GET``, ``DELETE`` リクエストはデータを送信しない。
* ``PUT``, ``POST`` リクエストはデータを送信する。
* エラー応答のように、応答タイプの一部は本体を必要としない。

Browsers and HTTP
======================================================================

* リクエストした HTML ページが画像や JavaScript ファイルなど、
  他のリソースを参照している場合には、それらも取得する。
* そういうときにはブラウザーは素早く取得するために一つずつ応答を待つのではなく、
  複数の ``GET`` リクエストを同時にする。

HTML ページにはユーザーが情報を入力してサーバーに送信するためのフォームが含まれていることがある。

.. code:: html

   <form method="GET" action="example/message.html">
     <p>Name: <input type="text" name="name"></p>
     <p>Message:<br><textarea name="message"></textarea></p>
     <p><button type="submit">Send</button></p>
   </form>

* このフォームには記入欄が二つある。名前とメッセージだ。
* 送信ボタンをクリックすると、フォーム内容が送信される。
  記入欄の内容を一つのリクエストにまとめて送信し、ブラウザーはその結果に進める。

  * ``<form>`` 要素の属性 ``attribute`` が ``GET`` であるか、またはこの属性が省略されている場合、
    フォーム情報は問い合わせ文字列としてアクション URL の末尾に追加される。

    .. code:: text

       GET /example/message.html?name=Jean&message=Yes%3F HTTP/1.1

    * ``?`` マークは URL のパス部分の終わりと問い合わせの始まりを示す。
    * このマークの後には名前と値のペアの列が続く。
    * ペアとペアを仕切る ``&`` マークがある。
    * URL エンコーディングと呼ばれる方法で、いくつかの文字は独自のコードに置き換えるという不文律があるらしい。
      記号 ``%`` のあとに二つの 16 進数を使う。

      * JavaScript にはこのための関数 ``encodeURIComponent`` および
        ``decodeURIComponent`` がある。

        .. code:: javascript

           console.assert(encodeURIComponent("Yes?") == "Yes%3F");
           console.assert(decodeURIComponent("Yes%3F") == "Yes?");

----

先ほどのフォームの例で属性 ``method`` を ``POST`` に変更すると、
HTTP リクエストは ``POST`` メソッドを使用することになり、問い合わせ文字列を
URL の末尾に追加するのではなく、リクエストの本体に追加することになる。

.. code:: text

   POST /example/message.html HTTP/1.1
   Content-length: 24
   Content-type: application/x-www-form-urlencoded
   name=Jean&message=Yes%3F

* ``GET`` リクエストは副作用のない、単に情報をねだるリクエストに使用すること。
  サーバー上の何かを変更するリクエストは ``POST`` など、別のメソッドで表現する必要がある。
* 多くの場合、ブラウザーは暗黙のうちに ``GET`` リクエストを行うことがある。
  たとえば、ユーザーがこの後すぐに必要になると確信されるリソースを前もって取得する場合などだ。

Fetch
======================================================================

ブラウザーの JavaScript が HTTP リクエストを行うためのインターフェイスを ``fetch`` という。
これは比較的新しいものなので、ブラウザーのインターフェイスとしては珍しい ``Promise`` を使っている。

.. code:: javascript

   fetch("example/data.txt").then(response => {
       console.log(response.status); // → 200
       console.log(response.headers.get("Content-Type")); // → text/plain
   });

関数 ``fetch`` を呼び出すと ``Response`` オブジェクトに解決する ``Promise`` が返される。
この ``Response`` にはステータスコード、ヘッダーなどのサーバーからの応答に関するステータスなどの情報を含む。

* ヘッダーはキーを大文字と小文字を区別しないで扱う ``Map`` のようなオブジェクトにラップされる。
  これは ``headers.get("Content-Type")`` でも ``headers.get("content-TYPE")`` でも同じ値を得られることになる。
* サーバーがエラーコードで応答した場合でも、``fetch`` が返す ``Promise`` は正常に解決する。
* ネットワークエラーが発生した場合や、リクエストの宛先となるサーバーが見つからない場合には、却下されることもある。
* 関数 ``fetch`` の最初の引数は、リクエスト URL だ。

  * それが ``http://`` などのプロトコル名で始まっていない場合、現在の文書に対する相対パスのようにに解釈される。
  * スラッシュ ``/`` で始まる場合は、現在のパスを置き換える。サーバー名の後ろの部分だ。
  * スラッシュで始まらない場合は、現在のパスの最後のスラッシュ文字までの部分が相対 URL の前に置かれる。

----

* 応答の実際の内容を得るにはメソッド ``text`` を呼ぶ。
* 初めの ``Promise`` はレスポンスのヘッダーを受信するとすぐに解決される。
  そして、応答本体は読むのに時間がかかるので、これも ``Promise`` を返す。

.. code:: javascript

   fetch("example/data.txt")
       .then(resp => resp.text())
       .then(text => console.log(text)); // This is the content of data.txt

* 同様のメソッド ``json`` は、本体を JSON として解析すると得られる値に解決する
  ``Promise`` を返すか、有効でない JSON の場合には却下する ``Promise`` を返す。

----

関数 ``fetch`` は ``GET`` メソッドを使ってリクエストを行うので、リクエスト本体は含まれない。
これを、第二引数に追加のオプションを含むおオブジェクトを渡すことで、異なる設定ができる。

.. code:: javascript

   fetch("example/data.txt", {method: "DELETE"}).then(resp => {
       console.log(resp.status); // → 405
   });

----

* リクエスト本体を追加するオプション ``body`` がある。
* ヘッダーを設定するオプション ``headers`` がある。

  * 例えば、このリクエストにはヘッダー ``Range`` があり、サーバーに応答の一部だけを返すように指示する。

    .. code:: javascript

       fetch("example/data.txt", {headers: {Range: "bytes=8-19"}})
           .then(resp => resp.text())
           .then(console.log); // the content

----

``Host`` や ``Range`` など、サーバーが本体のサイズを把握するのに必要なリクエストヘッダーを
ブラウザーが自動的に追加する。ここに独自のヘッダーを追加することで、
認証情報や受信したいファイル形式をサーバーに知らせることができる。

HTTP sandboxing
======================================================================

セキュリティーに関する問題から、ブラウザーはスクリプトが他のドメインに
HTTP リクエストを行うことを禁止している。

正当な理由で複数のドメインにアクセスしたいシステムにとってはこれは厄介だ。
サーバーは、次のようなヘッダーを応答に含めることで、
他のドメインからのリクエストを許可することをクライアントに明示することができる：

.. code:: text

   Access-Control-Allow-Origin: *
   Appreciating HTTP

----

クライアントサーバーシステムの通信をモデル化する方法がいくつかある。

* よく使われるのはリモートプロシージャーコールのモデルだ
  通信は通常の関数呼び出しのパターンに従うが、実際には別のマシンで関数が実行されている。
  この関数呼び出しをリクエストの形で実現する。
* もう一つの方法は、リソースと HTTP メソッドの概念を中心に通信を構築することだ。
  例えば、リモートプロシージャー ``addUser`` の代わりに
  ``/users/larry`` への ``PUT`` リクエストを使うといった具合だ。

二番目の方法ではリソースをキャッシュするなど、HTTP が提供する機能のいくつかが使いやすくなる。
HTTP で使われる概念はよく設計されていて、サーバーインターフェイスを設計する原理の役に立つ集合をもたらす。

Security and HTTPS
======================================================================

``https://`` で始まる URL に使用されるプロトコルは、HTTP トラフィックを読み取りや改竄が困難な方法でラップする。

#. データを交換する前に、クライアントは次のことを検証する：
   ブラウザーが認識している認証局から発行された暗号証明書を持っていることを証明させることで、
   サーバーが主張するとおりの人物であるかどうかを確認する。
#. 次に、接続に乗るデータすべてが暗号化される。

このように HTTPS が正しく機能すれば、なりすましや盗聴を防ぐことができる。

HTTPS は完璧ではなく、偽造されたり盗難されたりした証明書や、通信の盗聴などにより、
HTTPS が失敗する事件がいろいろとあったが、素の HTTP よりもはるかに安全だ。

Form fields
======================================================================

フォームは Web サイトがユーザーの投稿する情報を HTTP リクエストで送信するために元々設計された。
この設計は、サーバーとの対話的操作が常に新しいページに移動して起こることを仮定している。

フォーム記入欄の要素は DOM の一部であり、他の要素にはない多くのプロパティーやイベントをサポートしている。
これらにより、JavaScript で記入欄の入力を検証したり、制御したり、
フォームに新しい機能を追加したりできる。

フォームとは ``<form>`` タグの中に記入欄をいくつかまとめたものだ。
HTML では、単純なチェックボックス、ドロップダウンメニュー、テキストボックスなど、
さまざまな様式の記入欄が用意されている。

多くの記入欄型は ``<input>`` タグを使う。このタグの属性 ``type`` を使って記入欄の様式を選ぶ。
よく使われる型は：

.. csv-table::
   :delim: |
   :header: 型, 様式

   ``text`` | 単一行エディットボックス
   ``password`` | ``text`` と同じだがタイプされた文字をマスクする
   ``checkbox`` | チェックボックス
   ``radio`` | ラジオボタン
   ``file`` | ファイルを選択する記入欄

フォーム記入欄は必ずしも ``<form>`` タグ内に記述する必要はない。ページのどこにでも配置できる。
このようなフォームなし記入欄は送信できないが、JavaScript を使って入力に応答するときには、
記入欄を普通の手段で送信したくないことがしばしばある。

----

複数行のテキスト記入欄には ``<textarea>`` という独自のタグがある。
このタグは終了タグを必要とし、値の代わりにこのタグの間にはさまれたテキストを使用する。

.. code:: html

   <textarea>
   one
   two
   three
   </textarea>

----

``<select>`` タグは、あらかじめ定義された選択肢の中から記入欄を作成すうのに使う。

.. code:: html

   <select>
     <option>Pancakes</option>
     <option>Pudding</option>
     <option>Ice cream</option>
   </select>

----

フォームの記入欄の値が変更されるとイベント ``change`` が発射する。

Focus
======================================================================

HTML の要素の大部分とは違って、フォーム記入欄はキーボードでフォーカスを得ることができる。
クリックされたり作動させたりすると、フォーム記入欄は現在のアクティブな要素となり、
キーボード入力を受け付けるようになる。

* テキスト記入欄に入力できるのは、それにフォーカスされているときだけだ。
* その他の記入欄はキーボードイベントに対する反応が異なる。
  例えば ``<select>`` はユーザーが入力したテキストを含む選択肢に移動しようとし、
  矢印キーに反応して選択を上下に動かす。

* JavaScript からフォーカスを制御するにはメソッド ``focus`` および ``blur`` を使用する。

  * メソッド ``focus`` はそれが呼び出された DOM 要素にフォーカスする。
  * メソッド ``blur`` はフォーカスを消し去る。
  * プロパティー ``document.activeElement`` の値は、現在フォーカスされている要素だ。

.. code:: html

   <input type="text">
   <script>
   document.querySelector("input").focus();
   console.log(document.activeElement.tagName); // → INPUT

   document.querySelector("input").blur();
   console.log(document.activeElement.tagName); // → BODY
   </script>

----

ページによってはユーザーがある入力欄をすぐに操作したいと期待される場合がある。
文書のロード時に JavaScript でフォーカスを与えることもできるが、
それよりも HTML の属性 ``autofocus`` を使うほうがいい。

----

伝統的なブラウザーでは、ユーザーが :kbd:`Tab` キーを押して文書内でフォーカスを移動することができる。
要素がフォーカスされる順序を属性 ``tabindex`` で変更できる。

.. code:: html

   <input type="text" tabindex=1> <a href=".">(help)</a>
   <button onclick="console.log('ok')" tabindex=2>OK</button>

* デフォルトでは、HTML 要素のほとんどはフォーカスされない。
  しかし属性 ``tabindex`` を追加して、フォーカスできるようにすることができる
* 属性 ``tabindex`` の値を ``-1`` に設定すると、タブがその要素を飛ばすようになる。

Disabled fields
======================================================================

フォーム記入欄のすべては属性 ``disabled`` により無効化できる。

.. code:: html

    <button>I'm all right</button>
    <button disabled>I'm out</button>

* この属性は値を持たずに指定することができる。
* 無効化された記入欄は、フォーカスや変更ができず、ブラウザーはそれらの GUI をグレーアウトする。

プログラムが、ボタンやその他のコントロールによるアクションを処理している最中に、
サーバーとの通信が必要になり、時間がかかる場合がある。
そのような場合には、アクションが完了するまでコントロールを無効にするとよい。
ユーザーの誤操作を防止する効果がある。

The form as a whole
======================================================================

* ``<form>`` 要素が含む入力欄には、それの対応する DOM 要素にはプロパティー ``form`` があり、
  値はこれを含む ``<form>`` 要素に相当する DOM 要素だ。
* ``<form>`` 要素にはプロパティー ``elements`` があり、
  そのフォームが含む記入欄の配列のようなコレクションになっている。
* フォーム記入欄の属性 ``name`` は、フォームが送信されるときに記入欄の値がどのように識別されるかを決定する。
  また、フォームのプロパティー ``elements`` に参照する際のプロパティー名としても使用できる。

  * 配列風のオブジェクトとしても、マップ風のオブジェクトとしてもふるまう。

.. code:: html

   <form action="example/submit.html">
     Name: <input type="text" name="name"><br>
     Password: <input type="password" name="password"><br>
     <button type="submit">Log in</button>
   </form>
   <script>
     let form = document.querySelector("form");
     console.log(form.elements[1].type); // password
     console.log(form.elements.password.type); // password
     console.assert(form.elements.name.form == form);
   </script>

----

属性 ``type`` の値が ``submit`` であるボタンを押すとフォームが送信される。
フォーム記入欄がフォーカスされているときに :kbd:`Enter` を押しても同じ効果がある。

フォームを送信することは、ブラウザーがそのフォームの属性 ``action`` で示されるページに
``GET`` または ``POST`` リクエストを使って移動することをふつうは意味する。
しかし、それが起こる前にイベント ``submit`` が発射する。
このイベントを JavaScript を使って処理し、イベントオブジェクトのメソッド
``preventDefault`` を呼び出すことで既定の振る舞いを防ぐことができる。

.. code:: html

   <form action="example/submit.html">
     Value: <input type="text" name="value">
     <button type="submit">Save</button>
   </form>
   <script>
     let form = document.querySelector("form");
     form.addEventListener("submit", event => {
         console.log("Saving value", form.elements.value.value);
         event.preventDefault();
     });
   </script>

JavaScript でイベント ``submit`` を横取りするのことは色々な用途がある。

* ユーザー入力の検証、エラーメッセージの表示。
* フォームを送信する通常の方法を完全に無効にする。
* プログラムが入力を処理し、関数 ``fetch`` を使ってページの再読み込みなしにサーバーに送信することもできる。

Text fields
======================================================================

* ``<textarea>`` タグと ``<input>`` タグが作るテキストやパスワードタイプの入力欄は
  インターフェイスが共通している。

  * DOM 要素に現在の入力内容を文字列として値に持つプロパティー ``value`` がある。
    このプロパティーに別の文字列を代入すると、記入欄の内容が変化する。
  * プロパティー ``selectionStart`` と ``selectionEnd`` は選択テキストの情報を持つ。
    何も選択されていないと、これらのプロパティーはどちらもカーソルの位置を示す。

----

例えば、Khasekhemwy についての記事を書こうとしているが、彼の名前の綴り方がわからないとする。
次のコードは ``<textarea>`` タグにイベントハンドラを設定して、
:kbd:`F2` キーを押すと ``Khasekhemwy`` という文字列を挿入するイベントハンドラーを仕込むものだ：

.. code:: html

   <textarea></textarea>
   <script>
     let textarea = document.querySelector("textarea");
     textarea.addEventListener("keydown", event => {
         // The key code for F2 happens to be 113
         if (event.keyCode == 113) {
             replaceSelection(textarea, "Khasekhemwy");
             event.preventDefault();
         }
     });
     function replaceSelection(field, word) {
         let from = field.selectionStart, to = field.selectionEnd;
         field.value = field.value.slice(0, from) + word +
         field.value.slice(to);
         // Put the cursor after the word
         field.selectionStart = from + word.length;
         field.selectionEnd = from + word.length;
     }
   </script>

関数 ``replaceSelection`` は、記入欄の内容のうち、現在選択されている部分を
指定された文字列で置き換え、その後ろにカーソルを移動させる。

----

記入欄のイベント ``change`` は文字が入力される度に発射するのではなく、
内容が変更された後に記入欄がフォーカスを失うと発射する。
記入欄の変更に即座に反応するためには、代わりにイベント ``input`` に対してイベントハンドラーを登録する。
このイベントはユーザーが文字を入力したり、テキストを削除したり、記入欄の内容を操作するたびに発射する。

Checkboxes and radio buttons
======================================================================

チェックボックスの値は真偽値をとるプロパティー ``checked`` で読み書きする。

.. code:: html

   <label>
     <input type="checkbox" id="purple"> Make this page purple
   </label>
   <script>
     let checkbox = document.querySelector("#purple");
     checkbox.addEventListener("change", () => {
         document.body.style.background =
         checkbox.checked ? "mediumpurple" : "";
     });
   </script>

* ``<label>`` タグは文書の一部と ``<input>`` を関連付ける。
  ラベル上の任意の場所をクリックすると関連付けた記入欄がアクティブになり、
  チェックボックスやラジオボタンの場合は、記入欄がフォーカスされ、値が切り替わる。

----

ラジオボタンは同じ ``name`` 属性を持つ他のそれと暗黙のうちにリンクしていて、
一度にそのうちの一つしかアクティブな状態にならない。

次の例はラジオボタンの選択を変更するたびに文書の背景色をラベルが示すものに変化させるというものだ：

.. code:: html

   Color:
   <label>
     <input type="radio" name="color" value="orange"> Orange
   </label>
     <label>
   <input type="radio" name="color" value="lightgreen"> Green
   </label>
   <label>
     <input type="radio" name="color" value="lightblue"> Blue
   </label>
   <script>
     let buttons = document.querySelectorAll("[name=color]");
     for (let button of Array.from(buttons)) {
         button.addEventListener("change", () => {
             document.body.style.background = button.value;
         });
     }
   </script>

Select fields
======================================================================

* 選択欄は、概念的にはラジオボタンに似ている。ユーザーが一連の選択肢から選ぶことができる。
  ラジオボタンの場合は選択肢のレイアウトを自分で決めることができるが、
  ``<select>`` タグの外観はブラウザーが決める。
* 選択欄には、（ラジオボタンではなく）チェックボックスのリストのようなものもある。
  ``<select>`` タグに属性 ``multiple`` が与えられている場合、ユーザーは任意の数の選択肢を選択することができる。
  これは、ブラウザーのほとんどが、通常の選択欄とは異なる表示をする。
  通常、それを開いたときにしか選択肢の一覧を表示しないドロップダウンコントロールとして描画する。
* ``<option>`` タグはそれぞれが値を持つ。
  この値を定義するには属性 ``value`` で定義する。
  されていない場合には、``<option>`` タグ内のテキストがその値として採用される。
* ``<select>`` 要素の属性 ``value`` は、現在選択されている選択肢をとる。
  しかし、複数欄の場合、現在選択されているオプションのうち一つしか値が表示されないので、
  このプロパティーには意味があまりない。

* ``<select>`` にある ``<option>`` タグは、選択欄のプロパティー ``options`` を通じて、
  配列のようなオブジェクトとしてアクセスできる。

  * 各選択肢にはプロパティー ``selected`` があり、その選択肢が現在選択されているかどうかを示す。
    このプロパティーは選択肢の選択状態を変更するのにも使える。

この例では、複数選択欄から選択値を抽出して、個々のビットから二進数を構成する。
:kbd:`Ctrl` を押しながら複数の選択肢を選択する。

.. code:: html

   <select multiple>
     <option value="1">0001</option>
     <option value="2">0010</option>
     <option value="4">0100</option>
     <option value="8">1000</option>
   </select> = <span id="output">0</span>

   <script>
     let select = document.querySelector("select");
     let output = document.querySelector("#output");
     select.addEventListener("change", () => {
         let number = 0;
         for (let option of Array.from(select.options)) {
             if (option.selected) {
                 number += Number(option.value);
             }
         }
         output.textContent = number;
     });
   </script>

File fields
======================================================================

スクリプトは、ユーザーのプライベートなファイルを簡単に読み始めることはできない。
しかし、ユーザーがファイル欄でファイルを選択すると、
ブラウザーはスクリプトがそのファイルを読んでもよいという意味に解釈する。

ファイル欄は通常、choose や browse などのラベルが付いたボタンのように見え、
その横には選択されたファイルの情報が表示されている。

.. code:: html

   <input type="file">
   <script>
     let input = document.querySelector("input");
     input.addEventListener("change", () => {
         if (input.files.length > 0) {
             let file = input.files[0];
             console.log("You chose", file.name);
             if (file.type) console.log("It has type", file.type);
         }
     });
   </script>

ファイル欄のプロパティー ``files`` は選択したファイルを格納した配列風オブジェクトで、最初は空だ。
ファイル欄は属性 ``multiple`` がサポートされているので、複数ファイルを同時に選択できる。

オブジェクト ``files`` 内のオブジェクトは次のプロパティーを持つ：

* ``name``: ファイル名
* ``size``: ファイルサイズ（バイト単位）
* ``type``: ``text/plain`` や ``image/jpeg`` などのメディアタイプ。

ファイルの内容を持つプロパティーはないので、自分で取得する。
ディスクからのファイルの読み込みには時間がかかるので、非同期処理を書く：

.. code:: html

   <input type="file" multiple>
   <script>
     let input = document.querySelector("input");
     input.addEventListener("change", () => {
         for (let file of Array.from(input.files)) {
             let reader = new FileReader();
             reader.addEventListener("load", () => {
                 console.log("File", file.name, "starts with",
                     reader.result.slice(0, 20));
             });
             reader.readAsText(file);
         }
     });
   </script>

ファイル欄のプロパティー ``files`` 内のオブジェクトごとにオブジェクト ``FileReader`` を生成してファイルを読み取る。
イベント ``load`` にハンドラーを登録し、そこでファイルのテキストを読み込み、プロパティー ``result`` に格納する。

``FileReader`` は何らかの理由でファイルの読み込みに失敗した場合、イベント ``error`` を発射する。
エラーオブジェクトが ``FileReader`` のプロパティー ``error`` に格納される。
このインターフェースは ``Promise`` が言語の一部になる前に設計されたものだ。
次のように ``Promise`` でラップすることもできる：

.. code:: javascript

   function readFileText(file) {
       return new Promise((resolve, reject) => {
           let reader = new FileReader();
           reader.addEventListener(
               "load", () => resolve(reader.result));
           reader.addEventListener(
               "error", () => reject(reader.error));
           reader.readAsText(file);
       });
   }

Storing data client-side
======================================================================

単純な HTML ページにフォームとイベントハンドラーを利用したちょっとした JavaScript を付けると、
基本的な作業を自動化する小さな補助プログラムとなるミニアプリケーションとなる。

このようなアプリケーションでは、セッション間で何かを記憶しておく必要がある。JavaScript の変数は
ページが閉じられるたびに捨てられてしまうから使えない。
サーバーを用意してインターネットに接続し、そこにアプリケーションが何かを保存することもできるが、
それでは余計な仕事が増え、複雑になってしまう。時には、データをブラウザーに保存するだけで十分な場合もある。

オブジェクト ``localStorage`` を使用すると、ページの再読み込みにも耐えられる方法でデータを保存できる。
このオブジェクトでは、名前の下に文字列の値を収めることができる。

.. code:: javascript

   localStorage.setItem("username", "marijn");
   console.log(localStorage.getItem("username")); // → marijn
   localStorage.removeItem("username");

``localStorage`` の値は、上書きされるか、``removeItem`` が削除するか、
ユーザーがローカルデータを消去するまで残り続ける。

ドメインが異なるサイトは、異なるストレージ区画になる。
つまり、あるサイトの ``localStorage`` に保存されたデータは、原則として、
そのサイトのスクリプトでしか読み書きできないということになる。

ブラウザーは、サイトが ``localStorage`` に保存できるデータのサイズを制限する。

----

次のコード (pp. 337-338) は、粗いメモを取るアプリケーションを実装している。
名前の付いたノートの集合を保持し、編集したり、新しいものを作成することができる。

* このスクリプトは、``localStorage`` に格納されている ``"Notes"`` の値から開始状態を取得する。

  * または、それがない場合は、買い物リストだけを持つ例の状態を作成する。
  * 存在しないフィールドを ``localStorage`` から読み込むと ``null`` が返される。
  * ``JSON.parse`` に ``null`` を渡すと、文字列 ``"null"`` を解析して ``null`` を返す。

* メソッド ``setState`` は、DOM が所定の状態を示していることを確認して
  新しい状態を ``localStorage`` に保存する。
  イベントハンドラーがこの関数を呼び出して新しい状態に移る。

この例で ``Object.assign`` を使っているのは、古い ``state.notes`` の複製である新しいオブジェクト
を作成することを意図しているが、プロパティが一つ追加または上書きされている。

* ``Object.assign`` は最初の引数を取り、それ以降の引数からすべてのプロパティーをそれに追加する。
  したがって、空のオブジェクトを与えると、新しいオブジェクトを埋めることになる。
* 第三引数の角括弧表記は動的な値を名前とするプロパティを作成するのに使う。

----

``localStorage`` に似たオブジェクトに ``sessionStorage`` というものがある。

両者の違いは、``sessionStorage`` の内容が各セッションの終了時に忘れられることだ。
ブラウザのほとんどが、ブラウザが閉じられるたびに、各セッションの終了時に内容を忘れる。

Summary
======================================================================

HTTP の仕組みについて議論した。

* クライアントはリクエストを送信する。リクエストとは ``GET`` などのメソッド一つとリソース一つを特定するパスを含むものだ。
* サーバーはリクエストの処理を決めて、ステータスコードと応答本体を使って応答する。
* リクエストと応答の両方とも、ヘッダーという追加情報を含むことがある。
* ブラウザー JavaScript が HTTP リクエストを行うためのインターフェイスを ``fetch`` という。
  こういうふうにしてリクエストする：

  .. code:: javascript

     fetch("/18_http.html").then(r => r.text()).then(text => {
         console.log(`The page starts with ${text.slice(0, 15)}`);
     });

* ブラウザーはページの表示に必要な（ページ以外の）リソースをも得るために
  ``GET`` リクエストを行う。

----

ページはフォームを含むことがある。
ユーザーが入力した情報を、フォームが投稿されたときに新しいページへのリクエストとして送信する。

* HTML は各種フォーム記入欄を表現することができる。
* このような記入欄は JavaScript で検証したり操作したりすることができる。

  * 記入欄は変更されると ``change`` イベントが発射する。
  * テキストが入力されると ``input`` イベントが発射する。
  * キーボードフォーカスがあるとキーボードイベントを受け取る。
  * プロパティー ``value`` や ``checked`` を記入欄の内容に対する読み書きに使用する。

* フォームが投稿されると ``submit`` イベントが発射する。

  * JavaScript でこのイベントの ``preventDefault`` を呼び出して、
    ブラウザーの既定の所作を無効化することができる。

* フォーム記入欄要素は ``<form>`` タグの外にも出現する。
* ユーザーがファイル選択欄でローカルファイルシステムからファイルを選択すると、
  JavaScript から ``FileReader`` を使用してそのファイルの内容にアクセスできる。
* オブジェクト ``localStorage`` および ``sessionStorage`` を使用して、
  ページの再読み込みに耐えられるように情報を保存するために使用できる。

  * ``localStorage`` はユーザーがデータを消去するまで永久に保存する。
  * ``sessionStorage`` はブラウザーを閉じるまで保存される。

Exercises
======================================================================

.. todo:: 問題をやるのは後回し。
