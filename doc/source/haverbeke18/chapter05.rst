======================================================================
Higher-Order Functions
======================================================================

`Eloquent JavaScript <https://eloquentjavascript.net/>`__ Chapter 5 の読書ノート。

前章までの記述から JavaScript にも高階関数の概念が存在することは想像できる。本章
でそれを議論している。

.. contents::

Abstraction
======================================================================

* 抽象化は詳細を隠し、問題をより高い（言い換えるとより抽象的な）水準で語る能力を
  与えてくれる。
* 抽象度が低過ぎることに気づくことは、プログラミングにおいて有用な技能だ。

Abstracting repetition
======================================================================

プログラミングでは、与えられた回数だけ何かを反復するというのは普通のことだ。この
ことをどれだけ抽象化できるかを考える。

.. code:: javascript

   function repeat(n, action) {
       for (let i = 0; i < n; i++) {
           action(i);
       }
   }

   repeat(3, console.log);

   let labels = [];
   repeat(5, i => {
       labels.push(`Unit ${i + 1}`);
       });

Higher-order functions
======================================================================

他の関数を引数にとったり、返したり、その関数を操作する関数を :dfn:`高階関数` と
いう。この用語は、関数とそれ以外の値を厳格に区別する数学から持って来られた。

* 高階関数は、単なる値ではなく、動作を抽象化することができる。
* 配列メソッド ``forEach`` は ``for`` ループのようなものを高階関数として提供す
  る。

この例が少し難しい：

.. code:: javascript

   function unless(test, then) {
   if (!test) then();
   }

   repeat(3, n => {
       unless(n % 2 == 1, () => {
           console.log(n, "is even");
       });
   });
   // → 0 is even
   // → 2 is even

Script data set
======================================================================

ここからはラテン語、キリル文字、アラビア語などの文字体系である scripts に関する
データを使用する。データはコーディングサンドボックス
<https://eloquentjavascript.net/code#5> の変数 ``SCRIPTS`` が利用できる。これに
は Unicode で定義されている 140 の文字に関する情報が含まれている。

* それは配列であって、次のようなオブジェクトを 140 個含んでいるようだ：

  .. code:: javascript

     {
         name: "Coptic",
         ranges: [[994, 1008], [11392, 11508], [11513, 11520]],
         direction: "ltr",
         year: -200,
         living: false,
         link: "https://en.wikipedia.org/wiki/Coptic_alphabet"
     }

Filtering arrays
======================================================================

配列のメソッド ``filter`` を使って、与えた条件を満たす要素だけを抽出する。

.. code:: javascript

    console.log(SCRIPTS.filter(s => s.direction == "ttb"));
    // → [{name: "Mongolian", …}, …]

このような操作をする関数は純粋関数であることに注意。

Transforming with map
======================================================================

配列のメソッド ``map`` は、すべての要素に与えた関数を適用し、返された値から新し
い配列を作成する。

.. code:: javascript

   let rtlScripts = SCRIPTS.filter(s => s.direction == "rtl");
   console.log(map(rtlScripts, s => s.name));
   // → ["Adlam", "Arabic", "Imperial Aramaic", ...]

Summarizing with reduce
======================================================================

配列から単一の値を計算することも普通だ。具体的には、配列から要素を一つ取り出し、
その要素を次の要素と組み合わせることを繰り返して値を構築する。
関数型プログラミングではこのパターンを表現する高階関数の操作を reduce や fold と
呼ぶ。

* 配列のメソッド ``reduce`` がこれを実現する。
* 上で述べた「要素を一つ取り出し」ができない場合の値を引数として指定することもで
  きる。

.. code:: javascript

   console.assert([1, 2, 3, 4].reduce((a, b) => a + b) == 10);

Composability
======================================================================

高階関数が活躍するのは、操作を合成する必要があるときだ。

.. code:: javascript

   function average(array) {
       return array.reduce((a, b) => a + b) / array.length;
   }

   console.log(Math.round(average(
       SCRIPTS.filter(s => s.living).map(s => s.year))));
   console.log(Math.round(average(
       SCRIPTS.filter(s => !s.living).map(s => s.year))));

* 普通は高階関数を合成したようなコードのほうが扱いやすいので、それを好む。巨大な
  配列を何度も処理するのであれば、抽象度の低い様式のコードのほうが速いかもしれな
  い。

Strings and character codes
======================================================================

JavaScript における Unicode の符号化の話題が続くが、面倒なので保留する。

* 絵文字の出現により、誰もが二単位文字を使うようになり、このような問題に対処する
  負担はより公平になっている。
* 後から追加されたメソッド ``codePointAt`` は Unicode の完全な文字を与える。

Recognizing text
======================================================================

* 配列のメソッド ``findIndex`` には述語関数を与える。
* イギリスのイヌは woof と吠え、ロシアのイヌは тяв と吠える。

Summary
======================================================================

* 配列には高階関数のメソッドがたくさんある。

  * メソッド ``forEach`` は要素を反復処理させることができる。
  * メソッド ``filter`` は与えられた述語が ``true`` を返す要素しか含まない新しい
    配列を返す。
  * メソッド ``map`` は与えられた関数に各要素を引数として渡して返される値からな
    る新しい配列を返す。
  * メソッド ``reduce`` は与えられた関数を使って、要素すべてを一つの値にまとめ
    る。
  * メソッド ``some`` は、与えられた述語にマッチする要素を配列自身が含むかどうか
    をテストする。
  * メソッド ``findIndex`` は述語にマッチする最初の要素の位置を返す。

Exercises
======================================================================

Flattening
----------------------------------------------------------------------

**問題** メソッド ``reduce`` とメソッド ``concat`` を組み合わせて配列の配列を、
元の配列の要素をすべて含む単一の配列にしろ。

**解答** 原文から、二次元配列を一次元配列に平坦にする処理として実装する：

.. code:: javascript

   function flatten(array){
       return array.reduce((total, i) => total.concat(i), []);
   }

   flatten([[1, 2, 3], [4, 5, 6], [7, 8, 9]]); // → [1, 2, 3, 4, 5, 6, 7, 8, 9]

Your own loop
----------------------------------------------------------------------

**問題** 引数として値、テスト関数、更新関数、本体関数をする ``for`` 文のようなも
のを与える高階関数 ``loop`` を書け。

* 反復のたびに、まず現在のループの値に対してテスト関数を実行し、それが偽を返した
  ら停止する。
* その後、現在の値を与えて本体関数を呼び出す。
* 最後に、更新関数を呼び出して新しい値を生成し、最初から始める。
* 関数を定義する際に、実際のループ処理を行うために通常のループを使用することがで
  きる。

**解答** つまらないものができた：

.. code:: javascript

   function loop(){
       function inner(value, test, update, body){
           for(; test(value); value = update(value)){
               body(value);
           }
           return value;
       }
       return inner;
   }

Everything
----------------------------------------------------------------------

**問題** メソッド ``some`` の類比で、配列にはメソッド ``every`` がある。このメ
ソッドは、与えられた述語が配列の要素全てに対して真を返すときに真を返す。メソッド
``some`` と ``every`` はそれぞれ配列に作用する演算子 ``||`` および ``&&`` のよう
なものだ。

配列と述語を引数にとる関数として ``every`` を実装しろ。二バージョン書け：

* ループを使う
* メソッド ``some`` を使う

**解答** 前半は単純に：

.. code:: javascript

   function every(array, pred){
       for(const i of array){
           if(!pred(i)){
               return false;
           }
       }
       return true;
   }

後半は De Morgan の法則を応用する：

.. code:: javascript

   function every(array, pred){
       return !array.some(i => !pred(i));
   }

Dominant writing direction
----------------------------------------------------------------------

**問題** テキストの文字列の中で dominant writing direction を計算する関数を書
け。

* dominant writing direction とは、スクリプトが関連付けられている文字の大部分を
  占める方向だ。
* 各スクリプトオブジェクトにはプロパティー ``direction`` があり、値 ``"ltr"``,
  ``"rtl"``, ``"ttb"`` のいずれかをとる。
* ヒント：この章で定義した関数 ``characterScript`` と ``countBy`` が使えるはず
  だ。

**解答** 本文中の関数 ``textScripts`` を改変する：

.. code:: javascript

   function textScripts(text) {
       const scripts = countBy(text, char => {
           const script = characterScript(char.codePointAt(0));
           return script ? script.direction : "none";
       }).filter(({name}) => name != "none");

       if(scripts.length == 0){
           return undefined;
       }

       return scripts.reduce(
           (dominant, i) => dominant = dominant.count < i.count ? i : dominant);
   }

* ``Math.max`` の述語バージョンが存在しない？

以上
