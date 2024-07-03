======================================================================
Error handling
======================================================================

.. contents::
   :depth: 2

Error handling, ``try`` ... ``catch``
======================================================================

<https://javascript.info/try-catch> のノート。

ここで習う構文を使えば、エラーを捕まえて、スクリプトが死ぬのではなく、より合理的
な処理をすることができる。

The ``try`` ... ``catch`` syntax
----------------------------------------------------------------------

ほかのプログラミング言語にも似たものがある：

.. code:: javascript

   try {
       // code...
   } catch (err) {
       // error handling
   }

Error object
----------------------------------------------------------------------

すべての組み込みエラーオブジェクトには次のプロパティーがある：

.. csv-table::
   :delim: |
   :header-rows: 1
   :widths: auto

   Property | Description
   ``name`` | ``"ReferenceError"`` などのエラー名を表す文字列
   ``message`` | エラーの詳細を述べる文字列

Optional ``catch`` binding
----------------------------------------------------------------------

``catch`` 節でエラーを参照しないつもりならば、次のように書ける：

.. code:: javascript

   try {
       // code...
   } catch {
       // error handling
   }

Using ``try`` ... ``catch``
----------------------------------------------------------------------

本文では次のコードを例示している。

.. code:: javascript

   let json = "{ bad json }";
   try {
       let user = JSON.parse(json);
       // ...
   } catch (err) {
       alert("Our apologies, the data has errors, we'll try to request it one more time.");
       alert(err.name);
       alert(err.message);
   }

ここでの ``catch`` 節での対応はエラーメッセージを出力するだけの単純なものだ。実
際には、新しいネットワークリクエストを送る、訪問者に代替手段を提案する、エラーに
関する情報をログ機能に送る、などの処理が考えられる。

Throwing our own errors
----------------------------------------------------------------------

アプリケーション固有のエラーを考える。

``Throw`` operator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

演算子 ``throw`` はエラーを送出する。オペランドにエラーを表現するオブジェクトを
とる。

エラーオブジェクトは何でも送出することができる。組み込みエラーに倣って、
``name`` と ``message`` くらいは持たせるのがいい。

JavaScript には組み込みエラーがたくさんある。状況に合致すればそれらを利用しても
いい。

.. code:: javascript

   let error = new Error(message);
   // or = new SyntaxError(message);
   // or = new ReferenceError(message);

これらの組み込みエラーにおいては ``name`` はコンストラクターの名前となる。

* ``JSON.parse()`` ででたらめな文字列を渡すと ``SyntaxError`` が送出されることを
  見る。
* ``JSON.parse()`` が成功し、戻り値のオブジェクトにアプリケーションが期待するプ
  ロパティーが含まれていない場合、``throw`` 文で固有の例外を送出する。

どちらのエラーも ``catch`` 節一つで処理していることに注意する。

Rethrowing
----------------------------------------------------------------------

``catch`` 節ではアプリケーションが処理できるエラーしか扱いたくない。処理できるか
を判定するのにエラーオブジェクトをテストする。処理できないエラーは再送出する。

* ここでは演算子 ``instanceof`` を使って、エラーの型をテストしている。
* 再送出は ``throw`` 文に捕まえたオブジェクトをそのまま渡すことで行う。

どの ``catch`` ブロックにも処理されなかったエラーが最終的に生じると、スクリプト
は殺される。

``try`` ... ``catch`` ... ``finally``
----------------------------------------------------------------------

JavaScript にも ``finally`` 節がある。意味も他のプログラミング言語のそれと同じ
だ。

``try`` 節に ``return`` 文など、ブロック外へ脱出する命令がある場合にも
``finally`` 節の内容は脱出直前に実行される。

``try`` 節と ``finally`` 節があれば、そのエラー処理での ``catch`` 節は書かなくて
も文法的には問題ない。

この記事では ``finally`` 節で例外を送出するケースについて述べられていない。何か
欲しい。

Global ``catch``
----------------------------------------------------------------------

仕様にはないが、環境は最終的にエラーを処理するための機能を用意している。

* Node.js では ``process.on("uncaughtException")`` がそのために用意されている。
* ブラウザーでは、特別プロパティー ``window.onerror`` に関数を割り当てて、未処理
  エラーに対して実行させることができる。

もっとも、アプリケーションで処理し切れなかったエラーがこの機能で満足に処理できる
という場合はまずないだろう。せいぜい確認用だ。

Tasks
----------------------------------------------------------------------

Finally or just the code?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

もう一つ指摘するとすれば、``catch`` 節で再送出する場合の後始末も対応できること
か。

Custom errors, extending Error
======================================================================

<https://javascript.info/custom-errors> のノート。

JavaScript では ``throw`` を任意のオペランドで使用できる。技術的には、独自のエ
ラークラスは ``Error`` を継承する必要はない。しかし、継承することでエラーオブ
ジェクトを識別するために ``obj instanceof Error`` を使用することが可能になる。し
たがって、``Error`` を継承するのがよい。

アプリケーションが大きくなると、自ずとエラーが階層化される。例えば
``HttpTimeoutError`` は ``HttpError`` を継承する、という具合だ。

Extending ``Error``
----------------------------------------------------------------------

関数 ``readUser(json)`` を自作する状況で、入力にユーザープロパティーが含まれてい
ない場合のエラーをも自作することを考える。そのエラーの定義は、組み込みエラー
``Error`` から継承することにすると、さしあたり次のようなものになる：

.. code:: javascript

   class ValidationError extends Error {
       constructor(message) {
           super(message);
           this.name = "ValidationError";
       }
   }

* ``Error`` のコンストラクターは ``message`` しか受け付けないので、サブクラスで
  ``this.name`` を上書きする。

``readUser(json)`` の呼び出し例は次のようになる。他の言語と比べて ``catch`` 節の
書き方が面倒であることに気づく：

.. code:: javascript

   try {
       let user = readUser('{ "age": 25 }');
       // ...
   } catch (err) {
       if (err instanceof ValidationError) {
         alert("Invalid data: " + err.message);
       } else if (err instanceof SyntaxError) {
         alert("JSON Syntax Error: " + err.message);
       } else {
         throw err;
       }
   }

JavaScript の ``catch`` 節は ``throw`` されたすべてのエラーを捕捉するため、エ
ラータイプによる場合分けを、上のようにより特殊なものから判定していくことになる。

Further inheritance
----------------------------------------------------------------------

``ValidationError`` は汎用エラーとして、もっと特殊なエラーを定義することにする。
そのようなエラーを ``ValidationError`` から継承して定義する。

* 基底クラスのコンストラクターでの ``this.name`` のセットにコツがある。

Wrapping exceptions
----------------------------------------------------------------------

今度は関数 ``readUser(json)`` が送出するエラーを ``ReadError`` に一本化する。関
数内部に設けてある ``try`` 節から何らかのエラーが送出された場合、``catch`` 節で
そのエラーオブジェクトをこの新しいエラー型オブジェクトに持たせる。それから、この
新しいエラーオブジェクトを送出して終わる。

この節のエラー処理に関する議論は美しい。本文のクラスを図式化するとこういう感じに
なる：

.. mermaid::

   classDiagram
       direction TB

       Error <|-- ValidationError
       Error <|-- SyntaxError
       ValidationError <|-- PropertyRequiredError
       Error <|-- ReadError
       Error <--o ReadError : cause

       class Error{
           +string message
           +string name
       }

       class PropertyRequiredError{
           +string property
       }

       class ReadError{
       }

Tasks
----------------------------------------------------------------------

Inherit from SyntaxError
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

組み込みエラーから自作エラーを定義する作法を確認する問題。
