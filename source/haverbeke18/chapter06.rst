======================================================================
The Secret Life of Objects
======================================================================

`Eloquent JavaScript <https://eloquentjavascript.net/>`__ Chapter 6 の読書ノート。

本章では JavaScript 流オブジェクト指向プログラミングの様式を見ていく。
C++ や Python との考え方の違いに注目するといいかもしれない。
私がモダンな Java を知っていたらとよかったのだが。

.. contents::

Encapsulation
======================================================================

* オブジェクト指向プログラミングの基本的な考え方とは、プログラムを小さな欠片に分割して、それぞれの状態を管理するというものだ。
* このようなプログラムの断片は、オブジェクトを使ってモデル化される。
  そのインターフェースはメソッドとプロパティーの（クライアントに対しては限定された）集合で構成される。
* 多くの言語は、public と private のプロパティーを区別する方法を提供しているが、
  ミニマリスト的な方法論を採っている JavaScript では、少なくとも今のところはない。

  * 現在、この機能を言語に追加する作業が行われているそうだ。
  * JavaScript のプログラマーは public/private を区別するという考えを利用している。
    一般的に、利用可能なインターフェイスは、ドキュメントやコメントに記述されている。
    また、プロパティがプライベートであることを示すのに、変数名の最初の一文字を ``_`` とするのも一般的だ。

    * ということは Python のプログラマーに近い。

* インターフェースと実装を分離することは素晴らしい考えだ。この考え方をカプセル化と呼ぶ。

Methods
======================================================================

メソッドは関数値を保持するプロパティーに過ぎない。

.. code:: javascript

   let rabbit = {};
   rabbit.speak = function(line) {
       console.log(`The rabbit says '${line}'`);
   };
   rabbit.speak("I'm alive.");

   function speak(line) {
       console.log(`The ${this.type} rabbit says '${line}'`);
   }

   let whiteRabbit = {type: "white", speak};
   let hungryRabbit = {type: "hungry", speak};
   whiteRabbit.speak("Oh my ears and whiskers, how late it's getting!");
   hungryRabbit.speak("I could use a carrot right now.");

メソッドの元になる関数に対して ``call`` メソッドをオブジェクトを第一引数として呼び出すと、
オブジェクトのメソッドの形式でそれが呼び出される：

.. code:: javascript

   speak.call(hungryRabbit, "Burp!");

* キーワード ``this`` を次のようにして用いることもある：

.. code:: javascript

   function normalize() {
       console.log(this.coords.map(n => n / this.length));
   }

   normalize.call({coords: [0, 2, 3], length: 5});

仮に ``map`` の呼び出しに対する実引数がキーワード ``function`` で書かれた関数だったら、
このコードは動作しなかった。

* 上のコードは本書から無修正で引用したものだが、この関数はベクトルの正規化になっていない。

Prototype
======================================================================

オブジェクトのほとんどには、プロトタイプと呼ばれる、プロパティーの代替となる別のオブジェクトがある。

* オブジェクトが持っていないプロパティーが参照されると、まずはそのオブジェクトのプロトタイプが検索される。
  そこにもないときには、次にそのプロトタイプのプロトタイプが検索される、以下それを繰り返す、という具合だ。
  最後に ``Object.prototype`` に到達する。
* ``Object.getPrototypeOf`` は与えられたオブジェクトのプロトタイプを返す。

.. code:: javascript

   console.assert(Object.getPrototypeOf({}) == Object.prototype);
   console.assert(Object.getPrototypeOf(Object.prototype) == null);

* オブジェクトの多くは、そのプロトタイプとして ``Object.prototype`` を直接は持っていない。
* 関数は ``Function.prototype`` から派生する。
* 配列は ``Array.prototype`` から派生する。

.. code:: javascript

   console.assert(Object.getPrototypeOf(Math.max) == Function.prototype);
   console.assert(Object.getPrototypeOf([]) == Array.prototype);

* ``Object.create`` を使用して、特定のプロトタイプを持つオブジェクトを作成することができる。

  .. code:: javascript

     let protoRabbit = {
         speak(line) {
             console.log(`The ${this.type} rabbit says '${line}'`);
         }
     };

     let killerRabbit = Object.create(protoRabbit);
     killerRabbit.type = "killer";
     killerRabbit.speak("SKREEEE!");

  * オブジェクト式の ``speak(line)`` のようなプロパティーは、メソッドを定義するための略記法。
    つまり ``speak: speak(line){ ... }`` ということだ。
  * これは Prototype デザインパターンそのものであり、興味深い。

Classes
======================================================================

JavaScript のプロトタイプシステムは、クラスと呼ばれるオブジェクト指向の概念を、
やや非公式に取り入れたものと解釈される。

* クラスは、どのようなメソッドやプロパティを持っているかなどの型と呼ばれる概念を定義する。
* クラスに対して、どんな値のプロパティーを持つかなどを設定したものをインスタンスと呼ぶ。
* プロトタイプは、メソッドなど、クラスのすべてのインスタンスが同じ値を持つプロパティーを定義するのに便利だ。

.. code:: javascript

   function makeRabbit(type) {
       let rabbit = Object.create(protoRabbit);
       rabbit.type = type;
       return rabbit;
   }

JavaScript はコンストラクターという考え方もサポートする。
キーワード ``new`` を関数呼び出しの前に置くと、その関数はコンストラクターとして扱われる。
正しいプロトタイプを持つオブジェクトが自動的に作成され、
``return`` 文はないものの、それが返される。

.. code:: javascript

   function Rabbit(type) {
       this.type = type;
   }

   Rabbit.prototype.speak = function(line) {
       console.log(`The ${this.type} rabbit says '${line}'`);
   };

   let weirdRabbit = new Rabbit("weird");

* オブジェクトを構築する際に使用されるプロトタイプオブジェクトは、
  コンストラクター関数の ``prototype`` プロパティーを取得することで確認できる。
* コンストラクターの名前は、他の関数と簡単に区別できるように、慣習的に大文字で表記する。
* プロトタイプがコンストラクターに関連付けられているかどうかを理解することは重要。

.. code:: javascript

   console.assert(Object.getPrototypeOf(Rabbit) == Function.prototype);
   console.assert(Object.getPrototypeOf(weirdRabbit) == Rabbit.prototype);

Class notation
======================================================================

前節で JavaScript のクラスは ``prototype`` を持つコンストラクター関数であることを見た。
2015 年までは、そのように書く必要があったが、最近ではそれほど厄介ではない記法を採用している。

.. code:: javascript

   class Rabbit {
       constructor(type) {
           this.type = type;
       }

       speak(line) {
           console.log(`The ${this.type} rabbit says '${line}'`);
       }
   }

   let killerRabbit = new Rabbit("killer");
   let blackRabbit = new Rabbit("black");

* キーワード ``class`` はクラスの定義を開始する。
* コンストラクターを含むメソッドの集合を一度に定義することができる。

  * 任意の数のメソッドを宣言の中括弧内に記述することができる。
  * ``constructor`` という名前のメソッドは特別に扱われる。
    前節の意味でのコンストラクター関数を提供するもので、``Rabbit`` という名前にバインドされる。
  * その他の関数は、そのコンストラクターのプロトタイプにまとめられる。

* 現在、この形式のクラス定義でプロトタイプに追加できるのは、関数を保持するプロパティであるメソッドだけとなっている。
* 関数と同様に、クラスは文の中でも式の中でも使うことができる。
* クラス式では、クラス名を省略することが許される。

  .. code:: javascript

     let object = new class { getWord() { return "hello"; } };
     console.log(object.getWord());

Overriding derived properties
======================================================================

* オブジェクトにプロパティーを追加すると、それがプロトタイプに存在するかどうかに関わらず、
  オブジェクト自体に追加される。
* プロトタイプに同じ名前のプロパティーが既に存在していた場合、
  オブジェクトのプロパティーの後ろに隠れてしまうので、これはオブジェクトに影響を与えない。

.. code:: javascript

   Rabbit.prototype.teeth = "small";
   console.assert(killerRabbit.teeth == "small");

   killerRabbit.teeth = "long, sharp, and bloody";
   console.assert(killerRabbit.teeth == "long, sharp, and bloody");

   console.assert(blackRabbit.teeth == "small");
   console.assert(Rabbit.prototype.teeth == "small");

* 配列に対する ``.toString()`` はオブジェクト一般のそれとは挙動が異なる。
  配列に対して ``.join(",")`` を呼び出したのと同じような結果になる。

Map
======================================================================

今までは Python の ``dict`` のようなデータ構造として次のようにしていた：

.. code:: javascript

   let ages = {
       Boris: 39,
       Liang: 22,
       Júlia: 62
   };
   console.log(`Júlia is ${ages["Júlia"]}`);
   console.log("Is Jack's age known?", "Jack" in ages); // false
   console.log("Is toString's age knew?", "toString" in ages); // true; これがまずい

これは危ないのでクラス ``Map`` を利用する。

.. code:: javascript

   let ages = new Map();
   ages.set("Boris", 39);
   ages.set("Liang", 22);
   ages.set("Júlia", 62);
   console.log(`Júlia is ${ages.get("Júlia")}`); // Júlia is 62
   console.log("Is Jack's age known?", ages.has("Jack")); // false
   console.log(ages.has("toString")); // false

* メソッド ``set``, ``get``, ``has`` は ``Map`` オブジェクトのインターフェースの一部だ。
* 何らかの理由でマップとして扱う必要がある普通のオブジェクトがある場合、
  ``Object.keys()`` がそのオブジェクト自身のキーしか返さないことを知っていると便利だ。
* 演算子 ``in`` の代わりにメソッド ``hasOwnProperty`` を使うこともできる。
  これはオブジェクトのプロトタイプを無視する。

  .. code:: javascript

     console.assert({x: 1}.hasOwnProperty("x"));
     console.assert(!{x: 1}.hasOwnProperty("toString"));

Polymorphism
======================================================================

例えば次のように ``toString()`` を上書きすることができる。こういう技法をポリモーフィズムという。

.. code:: javascript

   Rabbit.prototype.toString = function() {
       return `a ${this.type} rabbit`;
   };

例えば for/of ループもポリモーフィズムの一種だ。
データ構造が特定のインターフェイスを提供することを期待している。

Symbols
======================================================================

* プロパティー名は通常は ``String`` だが ``Symbol`` であることがある。
* ``Symbol`` のオブジェクトは一意的であり、同じ値を二度作ることができない。

  .. code:: javascript

     let sym = Symbol("name");
     console.assert(sym != Symbol("name"));

     Rabbit.prototype[sym] = 55;
     console.assert(blackRabbit[sym] == 55);

* 次のような不思議なことができる。

  .. code:: javascript

     const toStringSymbol = Symbol("toString");
     Array.prototype[toStringSymbol] = function() {
         return `${this.length} cm of blue yarn`;
     };
     console.assert([1, 2].toString() == "1,2");
     console.assert([1, 2][toStringSymbol]() == "2 cm of blue yarn");

今の時点でこの機能に深入りするのは危険な気がする。

The iterator interface
======================================================================

for/of ループに渡されるオブジェクトは、iterable であることが期待される。
あるオブジェクトが iterable であるとは、それが名前が ``Symbol.iterator`` であるメソッドを持つことをいう。

.. code:: javascript

   let okIterator = "OK"[Symbol.iterator]();
   console.log(okIterator.next()); // → {value: "O", done: false}
   console.log(okIterator.next()); // → {value: "K", done: false}
   console.log(okIterator.next()); // → {value: undefined, done: true}

* このメソッドが呼ばれると iterator なるものを返す。
  これが実際に反復処理を行う。これには次の結果を返すメソッド ``next`` を持ち、次の結果を返す。
  その結果とは、次の値を提供するプロパティー ``value`` とプロパティー ``done`` を持つオブジェクトだ。
  これ以上の結果がない場合は ``true`` を、それ以外の場合は ``false`` になるはずだ。
* プロパティー ``next``, ``value``, ``done`` の名前は、``Symbol`` ではなく ``String`` であることに注意が要る。
  というより、``Symbol`` なのは ``iterator`` だけだ。

.. todo:: 行列の要素を反復するためのコードが少しむずかしい。

   Iterator デザインパターンの基本に則っているコードであることは読める。

Getters, setters, and statics
======================================================================

* Python で言う ``@propery`` のようなメソッド機能が JavaScript でもサポートされている。
* Python で言う ``@staticmethod`` のような機能もサポートされている。

.. code:: javascript

   class Temperature {
       constructor(celsius) {
           this.celsius = celsius;
       }

       get fahrenheit() {
           return this.celsius * 1.8 + 32;
       }

       set fahrenheit(value) {
           this.celsius = (value - 32) / 1.8;
       }

       static fromFahrenheit(value) {
           return new Temperature((value - 32) / 1.8);
       }
   }

Inheritance
======================================================================

JavaScript でもサブクラスを定義することができる。本書の例をそのまま引用する。

.. code:: javascript

   class SymmetricMatrix extends Matrix {
       constructor(size, element = (x, y) => undefined) {
           super(size, size, (x, y) => {
               if (x < y) return element(y, x);
               else return element(x, y);
           });
       }
       set(x, y, value) {
           super.set(x, y, value);
           if (x != y) {
               super.set(y, x, value);
           }
       }
   }

   let matrix = new SymmetricMatrix(5, (x, y) => `${x},${y}`);

* 構文としては Java に酷似していて、キーワード ``extends`` を用いて基底クラスを指定し、サブクラスの定義を始める。
* メソッドからキーワード ``super`` を使って、基底クラス自身のメンバーを参照する。

  * Python と使われ方が異なるので注意。いきなりドットを書く。``this`` ではなく ``super`` という感じか。

* 継承は、カプセル化やポリモーフィズムと並んで、オブジェクト指向の基本だ。
  後者の二つが素晴らしいアイデアだと一般的に評価されているのに対し、継承に対しては手ばなしに素晴らしいとは言えない。
  後者二つはプログラム要素間の結合の度合いを明らかに下げるが、継承はむしろ上げてしまう。

The instanceof operator
======================================================================

二項演算子 ``instanceof`` はあるオブジェクトが特定のクラスか、それの派生クラスであるかどうかをテストする。
第一オペランドと第二オペランドにオブジェクトとコンストラクター関数をそれぞれ渡す。

.. code:: javascript

   console.assert(new SymmetricMatrix(2) instanceof SymmetricMatrix);
   console.assert(new SymmetricMatrix(2) instanceof Matrix);
   console.assert(!(new Matrix(2, 2) instanceof SymmetricMatrix));
   console.assert([1] instanceof Array);

Summary
======================================================================

* オブジェクトに付随するプロトタイプという概念がある。
* 単純なオブジェクトはプロトタイプとして ``Object.prototype`` を有する。
* コンストラクターの

  * 通常は名前が大文字で始まる関数となっている。
  * コンストラクターを演算子 ``new`` と一緒に使用して新しいオブジェクトを作成する。
  * オブジェクトのプロトタイプは、コンストラクターのプロパティー ``prototype`` で指定されたオブジェクトとなる。

* オブジェクトのプロパティーにアクセスするたびに、
  関連するメソッドを暗黙的に呼び出すという getter や setter を定義することができる。
* 静的メソッドとは、クラスのプロトタイプではなく、コンストラクターに格納されているメソッドだ。
* 演算子 ``instanceof`` はオブジェクトのクラスをテストする。
* オブジェクトは、そのインターフェースを介してのみオブジェクトとアクセスできるようにすると利用させやすい。
* 複数の型が同じインターフェイスを実装することができる。
  インターフェイスを使用するように書かれたコードは、
  そのインターフェイスを備える、異なるオブジェクトを操作する方法が自動的にわかっている。
  この仕組みをポリモーフィズムという。
* 詳細がわずかしか違わないクラスを複数定義する場合は、継承の技法が有効だ。

Exercises
======================================================================

A vector type
----------------------------------------------------------------------

**問題** 二次元空間のベクトルを表現するクラス ``Vec`` を書け。
これは数 ``x``, ``y`` を引数として取り、同じ名前のプロパティーに保存されるものとする。

次に ``Vec`` のプロトタイプにメソッド ``plus`` および ``minus`` を与えろ。
これらは別のベクトルを引数とし、メソッド名の示唆する新しいベクトルを返す。

取得プロパティー ``length`` をプロトタイプに加えろ。
ベクトルの大きさを計算してそれを返すものだ。

**解答** そういえば JavaScript には演算子のオーバーロード機能はないのだろうか。

.. code:: javascript

   class Vec{
       constructor(x, y){
           this.x = x;
           this.y = y;
       }

       get length() {
           return Math.sqrt(this.x ** 2 + this.y ** 2);
       }
   };

   Vec.prototype.plus = function(other){
       return new Vec(this.x + other.x, this.y + other.y);
   }

   Vec.prototype.minus = function(other){
       return new Vec(this.x - other.x, this.y - other.y);
   }

Groups
----------------------------------------------------------------------

**問題** 次の仕様に従うクラス ``Group`` を書け。

* このクラスには標準 JavaScript にあるクラス ``Set`` のようにメソッド
  ``add``, ``delete``, ``has`` がある。

  * コンストラクターは空の ``Group`` を作成する。
  * メソッド ``add`` は引数がまだメンバーでない場合に限り、それを ``Group`` に追加する。
  * メソッド ``delete`` は引数がメンバーである場合にそれを ``Group`` から削除する。
  * メソッド ``has`` は引数が ``Group`` のメンバーであるかどうかを示す真偽値を返す。

* 二つの値が同じかどうかを判断するには演算子 ``===`` または ``indexOf`` などの同等の何かを使え。

  * ノート：メソッド ``Array.prototype.indexOf`` が暗に使う比較演算は演算子 ``===`` に基づく。

* このクラスには iterable を引数として取り、それを反復して生成されたすべての値を含む
  ``Group`` を作成する静的メソッド ``from`` を実装しろ。

**解答** 基本型 ``Array`` を使って実装して構わないと解釈する。
本物の集合クラスを書くのは無理がある。

.. code:: javascript

   class Group{
       constructor(){
           this.content = [];
       }

       add(element){
           if(!this.has(element)){
               this.content.push(element);
           }
       }

       delete(element){
           const where = this.content.indexOf(element);
           if(where != -1){
               this.content.splice(where, 1);
           }
       }

       has(element){
           return this.content.indexOf(element) != -1;
       }

       static from(iterable){
           const group = new Group;
           for(const i of iterable){
               group.add(i);
           }
           return group;
       }
   }

Iterable groups
----------------------------------------------------------------------

**問題** 前の演習で定義したクラス ``Group`` を iterable にしろ。

``Group`` のメンバーを表すのに配列を使用した場合、
配列に対してメソッド ``Symbol.iterator`` を呼び出して作成した反復子を返すだけではいけない
（それでうまくいったとしても、この演習の目的に反する）。

なお、反復処理中に ``Group`` が変更されたとき、反復子の動作がおかしくなるのは構わないとする。

**解答** 学習中に飛ばした箇所なので、今泥縄でやってみる。

まず ``Group.prototype`` を次のように拡張する：

.. code:: javascript

   Group.prototype[Symbol.iterator] = function(){
       return new GroupIterator(this);
   };

まだ ``GroupIterator`` を書いていないので、書く：

.. code:: javascript

   class GroupIterator{
       constructor(group){
           this.i = 0;
           this.group = group;
       }

       next(){
           const content = this.group.content;
           if(this.i == content.length){
               return {done: true};
           }

           const value = {
               i: this.i,
               value: content[this.i]
           };
           ++this.i;
           return {value, done: false};
       }
   }

Borrowing a method
----------------------------------------------------------------------

**問題** この章の前半で、オブジェクトの ``hasOwnProperty`` は、
プロトタイプのプロパティーを無視したい場合に、
演算子 ``in`` の代わりに、より堅牢な手段として使用できることを述べた。

しかし、マップに ``"hasOwnProperty"`` という単語を含める必要がある場合はどうだろうか。
オブジェクト自身のプロパティがメソッドの値を隠してしまうため、そのメソッドを呼び出すことができなくなる。

``hasOwnProperty`` という名前のプロパティーを持っているオブジェクトに対して、
隠された ``hasOwnProperty`` を参照する方法はあるか。

**解答** ある。
``Object.prototype`` と ``call`` を理解していることが急所の問題だ。

.. code:: javascript

   const myobj = {
       myproperty: "my value",
       hasOwnProperty: i => false,
   };

   console.assert(!myobj.hasOwnProperty('myproperty'));
   console.assert(Object.prototype.hasOwnProperty.call(myobj, 'myproperty'));
   console.assert(Object.prototype.hasOwnProperty.call(myobj, 'hasOwnProperty'));

参考： `Object.prototype.hasOwnProperty() - JavaScript | MDN <https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Object/hasOwnProperty>`__

以上
