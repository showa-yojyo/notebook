======================================================================
Data Structures: Objects and Arrays
======================================================================

`Eloquent JavaScript <https://eloquentjavascript.net/>`__ Chapter 4 の読書ノート。

本書のウェブページ <https://eloquentjavascript.net/code> では特定の章の内容に
沿ったコードを実行することができる。別の環境で演習問題に取り組む場合は、本章の完
全なコードをリンク先からダウンロードすることになる。

.. contents::

The weresquirrel
======================================================================

プログラミング言語の教科書でリス男の小説が突如始まる。

Data sets
======================================================================

JavaScript には値の並びを格納するためのデータ型が用意されている。これは配列と呼
ばれ、角括弧で囲まれた値のリストをカンマで区切って定義する。構文は Python の
``list`` に似ているようだ。

.. code:: javascript

   let listOfNumbers = [2, 3, 5, 7, 11];
   console.assert(listOfNumbers[2] == 5);
   console.assert(listOfNumbers[0] == 2);
   console.assert(listOfNumbers[2 - 1] == 3);

Properties
======================================================================

* JavaScript ではオブジェクトのほとんどすべてがプロパティーを有する。例外は
  ``null`` と ``undefined`` だ。
* JavaScript でプロパティーにアクセスするには、ドットと角括弧の二つの方法があ
  る。

  * だから ``value.x`` が有効な式であるとすれば ``value["x"]`` も有効だ。

* 配列の要素は、その配列のプロパティーとして格納される。

Methods
======================================================================

* 関数を含むプロパティーはふつうはその値のメソッドと呼ばれる。

Objects
======================================================================

* 型 ``object`` の値は、プロパティーのコレクションとみなせる。オブジェクトを作成
  する一つの方法は、中括弧を使ってプロパティーを列挙するというものだ。

.. code:: javascript

   let day1 = {
       squirrel: false,
       events: ["work", "touched tree", "pizza", "running"]
   };

* JavaScript では、中括弧には意味が二つある。

  * 文のブロックを定義するもの
  * そうでなければオブジェクトを定義するもの

* 存在しないプロパティーを読み取ると、値 ``undefined`` が得られる。
* プロパティーの値がすでに存在している場合は置き換えられ、存在しない場合は新しい
  プロパティーが存在しない場合は、オブジェクトに新しいプロパティーを作成する。
* 単項演算子 ``delete`` をオブジェクトのプロパティーに適用すると、指定されたプロ
  パティーをオブジェクトから削除する。Python の ``del`` に似ている。
* 演算子 ``in`` は、文字列とオブジェクトに適用すると、そのオブジェクトに指定した
  名前のプロパティーがあるかどうかをテストする。
* 関数 ``Object.keys`` にオブジェクトを渡すと、オブジェクトのプロパティー名を表
  す文字列の配列が返る。
* 関数 ``Object.assign`` は、あるオブジェクトのすべてのプロパティーを別のオブ
  ジェクトにコピーする。

.. code:: javascript

   console.log(Object.keys({x: 0, y: 0, z: 2}));
   // → ["x", "y", "z"]

   let objectA = {a: 1, b: 2};
   Object.assign(objectA, {b: 3, c: 4});
   console.log(objectA);
   // → {a: 1, b: 3, c: 4}

Mutability
======================================================================

* 数値、文字列、ブーリアンなど、これまでの章で説明してきた値の種類は、すべて
  mutable だ。これらの型の値を変更することはできない。
* 変数には変更可能なものと一定のものがあるが、これは値の振る舞いとは別のもの。
* オブジェクトへの ``const`` 定義は、それ自体は変更されず、同じオブジェクトを指
  し続けるものの、そのオブジェクトの中身は変更される可能性がある。
* 演算子 ``==`` でオブジェクトを比較する場合、同一性によって比較する。異なるオブ
  ジェクトを比較すると、たとえ同一のプロパティーを持っていたとしても ``false``
  を返す。

The lycanthrope's log
======================================================================

* ブレース記法のプロパティー名の後に値がない場合、その値は同じ名前のものとなる。
* 相関係数の説明がある。
* :math:`\varphi \approx 0.069` となり、わずか。ピザを食べても変身には影響しない
  だろう。

Computing correlation
======================================================================

* JavaScript では、2×2 の表を 4 要素の配列で表すことができる。
* しかし、平板な配列を使うほうが単純で、表にアクセスする式を短くすることができ
  る。

結果として得られたデータセットは本章のコーディングサンドボックス
<https://eloquentjavascript.net/code#4> にある。ここでは ``JOURNAL`` とダウン
ロード可能なファイルに保存されている。

* 指定した値が配列内に存在するかどうかをテストするメソッド ``includes`` がある。

残るは、記録されたタイプのすべてのイベントの相関関係を見つけて、何か目立つものが
ないかどうかを見ることとなった。

Array loop
======================================================================

現代の JavaScript では配列、文字列、その他のデータ構造をループするのに次の構文を
使える：

.. code:: javascript

   for (let entry of JOURNAL) {
       console.log(`${entry.events.length} events.`);
   }

The final analysis
======================================================================

分析の結果、ピーナッツを食べることがリスに変身する確率に強い正の影響を与えるこ
と、歯を磨くと大きな負の効果があることが観察された。

Further arrayology
======================================================================

配列のメソッドをいくつか挙げる。

* ``unshift`` と ``shift`` はそれぞれ先頭に対して要素を追加、削除する。
* ``indexOf`` と ``lastIndexOf`` は想像通りの振る舞いをする。
* ``slice`` は Python のそれと似ている。
* ``concat`` は Python の ``extend`` と同等。二項演算子 ``+`` と同じ。

Strings and their properties
======================================================================

* ``indexOf`` には引数に文字列を与えられることに注意する。
* ``slice`` は配列のそれと同等の振る舞いをする。
* ``trim`` は Python の ``strip`` に相当する。
* ``padStart`` というメソッドが存在する。

  .. code:: javascript

     console.assert("6".padStart(3, "0") == "006");

* ``split`` は Python と同様。
* ``join`` は Python と主客転倒している。
* ``repeat`` がある。

Rest parameters
======================================================================

* JavaScript でも可変個引数関数を定義することができる。関数の最後の引数の前に
  ``...`` を書く。
* 引数の配列をとる関数を呼び出す際にも、同様の三点表記が使える。
* ある配列を他の配列に埋め込むようなこともできる。

.. code:: javascript

   function max(...numbers) {
       let result = -Infinity;
       for (let number of numbers) {
           if (number > result) result = number;
       }
       return result;
   }

   let numbers = [5, 1, 7];
   console.assert(max(...numbers) == 7);

   // read another array into the new array.
   let words = ["never", "fully"];
   console.assert(["will", ...words, "understand"]);

The Math object
======================================================================

* ``Math`` はオブジェクトというよりも単なる名前空間のように捉えたい。ここにある
  関数や値が大域変数である必要がないようにしたいので、こういう形式になっている。
* 乱数機能は ``Math`` にある。

Destructuring
======================================================================

.. code:: javascript

   function phi(table) {
       return (table[3] * table[0] - table[2] * table[1]) /
           Math.sqrt((table[2] + table[3]) *
               (table[0] + table[1]) *
               (table[1] + table[3]) *
               (table[0] + table[2]));
   }

これは次のようにも書ける：

.. code:: javascript

   function phi([n00, n01, n10, n11]) {
       return (n11 * n00 - n10 * n01) /
           Math.sqrt((n10 + n11) * (n00 + n01) *
           (n01 + n11) * (n00 + n10));
   }

また、次のようにすることでオブジェクトのプロパティーの値を得られる。

.. code:: javascript

   let {name} = {name: "Faraji", age: 23};
   // or let {age} = {name: "Faraji", age: 23};
   // or let {name, age} = {name: "Faraji", age: 23};
   console.assert(name == "Faraji");

JSON
======================================================================

JSON という一般的なシリアライズフォーマットがある。

* JavaScript 以外の言語でも、Web 上のデータ保存・通信フォーマットとして広く使わ
  れている。
* JavaScript には、JSON との間でデータを変換するための関数 ``JSON.stringify`` と
  ``JSON.parse`` がある。

Summary
======================================================================

* オブジェクトや配列は、複数の値を一つの値にまとめるものだ。
* JavaScript のほとんどの値はプロパティを持っているが、例外は ``null`` と
  ``undefined`` の二つ。
* プロパティーにアクセスするには ``value.prop`` または ``value["prop"]`` のよう
  に書く。
* 配列は通常、型が同じ値を任意の個数だけ格納する。プロパティーの名前には数字を使
  用する。
* 配列要素を ``for`` ループで反復するときには ``for(let element of array){ ...
  }`` のような特別な構文を利用できる。

Exercises
======================================================================

The sum of a range
----------------------------------------------------------------------

**問題**：

* ``start`` と ``end`` の二つの引数を取り、その区間のすべての数を含む配列を返す
  関数 ``range`` を書け。区間終点は ``end`` と一致するものとする。
* 次に、数の配列を受け取り、これらの数の合計を返す関数 ``sum`` を書け。
* 関数 ``range`` に ``step`` を実装しろ。``step`` が指定されない場合は、以前の動
  作に対応して、要素は 1 ずつ増える。

  * ``range(1, 10, 2)`` は ``[1, 3, 5, 7, 9]`` を返す。
  * 負の値でも動作するようにして ``range(5, 2, -1)`` は ``[5, 4, 3, 2]`` を返
    す。

**解答**：単純な ``range`` をまず書く：

.. code:: javascript

   function range(start, end) {
       console.assert(Number.isSafeInteger(start));
       console.assert(Number.isSafeInteger(end));
       console.assert(start <= end);

       let a = [start];
       for (let i = start; i < end; ++i) {
           a.push(i);
       }
       return a;
   }

関数 ``sum`` は色々書き方がありそうだが：

.. code:: javascript

   function sum(a){
       return a.reduce((total, current) => total + current, 0);
   }

   console.assert(sum(range(1, 10)) == 55);

関数 ``range`` のステップバージョン：

.. code:: javascript

   function range(start, end, step = 1) {
       console.assert(Number.isSafeInteger(start));
       console.assert(Number.isSafeInteger(end));
       console.assert(Number.isSafeInteger(step));
       console.assert(step != 0);

       let a = [start];
       if(start < end && step > 0){
           for (let i = start + step; i < end; i += step) {
               a.push(b);
           }
       }
       else if(start > end && step < 0){
           for (let i = start + step; i > end; i += step) {
               a.push(b);
           }
       }
       return a;
   }

Reversing an array
----------------------------------------------------------------------

**問題**：次の関数を配列の ``reverse`` を用いずに書け：

* 関数 ``reverseArray``
* 関数 ``reverseArrayInPlace``

前章の副作用や純粋関数についての注意点を思い返して、より多くの場面で役に立つと考
えられるのはどちらか。また、実行速度はどちらが速いか。

**解答**：関数 ``reverseArray`` を先に実装する。

.. code:: javascript

   function reverseArray(a){
       let newArray = new Array(a.length);
       for(let i = 0, j = a.length - 1; i < a.length; ++i, --j){
           newArray[j] = a[i];
       }
       return newArray;
   }

あるいは ``a`` をコピーして ``reverseArrayInPlace`` を呼び出す実装も考えられる。

.. code:: javascript

   function reverseArrayInPlace(a){
       const mid = a.length / 2;
       for(let i = 0, j = a.length - 1; i < mid; ++i, --j){
           [a[i], a[j]] = [a[j], a[i]];
       }
   }

* 使いやすいのは古いオブジェクトを壊さない ``reverseArray`` のほうだろう。
* 実行速度はメモリーの確保が生じない in-place のほうが優れている。

A list
----------------------------------------------------------------------

JavaScript では単方向リストを次のように表現することが考えられる：

.. code:: javascript

   let list = {
       value: 1,
       rest: {
           value: 2,
           rest: {
               value: 3,
               rest: null
           }
       }
   };

リストの良いところは、その構造の一部を共有できることだ。例えば、2つの新しい値
``{value: 0, rest: list}`` と ``{value: -1, rest: list}`` を作成したとすると、こ
れらはどちらも独立したリストだが、最後の三つの要素を構成する構造を共有している。
また、元のリストも有効なままだ。

**問題**：

* 配列 ``[1, 2, 3]`` を入力として与えると、上記のようなデータ構造のオブジェクト
  を返す関数 ``arrayToList`` を書け。
* また、リストから配列を生成する関数 ``listToArray`` も書け。そして、ヘルパー関
  数 ``prepend`` を追加しろ。この関数は要素とリストを受け取って、要素を入力リス
  トの先頭に追加する **新しい** リストを作成するものとする。
* 関数 ``nth`` を書け。リストとインデックスを受け取り、リスト内の指定された位置
  の要素を返すものだ。そのような要素がない場合は ``undefined`` を返せ。
* 関数 ``nth`` を再帰で実装していなければ、再帰版も書け。

**解答**：あまりエレガントではないコードだが：

.. code:: javascript

   function arrayToList(a){
       let list = {"value": null, "rest": null};
       if(a.length == 0){
           return list;
       }

       let cur = list;
       let i = 0;
       for(; i < a.length - 1; ++i){
           cur.value = a[i];
           cur.rest = {"value": null, "rest": null};
           cur = cur.rest;
       }
       cur.value = a[i];
       cur.rest = null;
       return list;
   }

   function listToArray(list){
       let a = [list.value];
       let cur = list.rest;
       while(cur.rest != null){
           a.push(cur.value);
           cur = cur.rest;
       }
       a.push(cur.value);
       return a;
   }

後半は新しいリストを作成することに注意する：

.. code:: javascript

   function prepend(element, list){
       let arr = listToArray(list);
       arr.unshift(element);
       return arrayToList(arr);
   }

   function nth(list, index){
       console.assert(Number.isSafeInteger(index) && index >= 0);
       let cur = list;
       for(index-- && cur != null; cur = cur.rest);
       return cur ? cur.value : undefined;
   }

   function nth_recursive(list, index){
       console.assert(Number.isSafeInteger(index) && index >= 0);
       if(index == 0){
           return list.value;
       }
       return nth_recursive(list.rest, index - 1);
   }

Deep comparison
----------------------------------------------------------------------

**問題**：二つ値を受け取り、それらが同じ値または同じプロパティを持つオブジェクト
である場合にのみ真を返す関数 ``deepEqual`` を書け。プロパティーの値は、
``deepEqual`` の再帰で比較したときに等しい。

* ヒント：値を演算子 ``===`` を使って直接比較するか、または値のプロパティーすべ
  てを比較するかを調べるには、演算子 ``typeof`` を使う。ただし ``typeof null``
  も ``"object"`` を生成することに注意すること。
* ヒント：関数 ``Object.keys`` は、オブジェクトのプロパティーを調べて比較したい
  ときに便利だ。

**解答**：問題文から求めるものが再帰関数であることが明らかだ。

.. code:: javascript

   function deepEqual(lhs, rhs){
       if (lhs && rhs && typeof lhs == 'object' && typeof rhs == 'object') {
           const keys = Object.keys(lhs);
           if (keys.length != Object.keys(rhs).length){
               return false;
           }

           for(const key of keys){
               if(!deepEqual(lhs[key], rhs[key])){
                   return false;
               }
           }
           return true;
       }

       return a === b;
   }

というか、インターネットに解がある：
`eloquent - Deep Compare JavaScript function - Stack Overflow <https://stackoverflow.com/questions/48728515/deep-compare-javascript-function>`__

以上
