======================================================================
Chapter 03: Language Runtime Enhancements ノート
======================================================================

`Chapter 03: Language Runtime Enhancements <https://changkun.de/modern-cpp/en-us/03-runtime/>`__
についてのノート。

.. contents::

3.1 Lambda Expression
======================================================================

ラムダ式は現代の C++ で最も重要な機能の一つであり、ラムダ式は匿名関数のように機
能する。匿名関数が使えるのは、関数が必要だが、それを呼び出すのに名前を使いたくな
いときだ。こういう状況は何度も何度もある。それゆえ匿名関数は、現代のプログラミン
グ言語のほとんどでは標準で備わっている。というようなことを著者は述べている。

Basics
----------------------------------------------------------------------

ラムダ式の構文をまず頭に叩き込む。関数定義の構文に対応物がない高栄養素である捕捉
リストを見ていく。それをまず三つに分類する：

1. value capture: 通常関数の値渡しに対応する。
2. reference capture: 通常関数の参照渡しに対応する。
3. implicit capture: 捕捉リストをコンパイラーに任せる。
4. expression capture: 前述の 1. と 2. は外側スコープで宣言された変数なので、こ
   れらの捕捉メソッドは lvalue を捕捉して rvalue を捕捉しない。

Value capture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

重要なのは、取り込まれた変数が、ラムダ式が呼び出されたときではなく、ラムダ式が定
義されたときにコピーされることだ。

.. code:: c++

   void lambda_value_capture() {
       int value = 1;
       auto copy_value = [value] {
           return value;
       };
       value = 100;
       auto stored_value = copy_value();
       std::cout << "stored_value = " << stored_value << std::endl;
       assert(stored_value == 1);
       assert(value == 100);
   }

Reference capture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

上記コードのラムダ式を以下に替えると、今度は ``stored_value == 100`` で終了する。

.. code:: c++

   auto copy_value = [&value] {
        return value;
   };

Implicit capture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

捕捉リストを手動で書くのではなく、コンパイラーに任せることもできる。このとき捕捉
リストに ``&`` や ``=`` を書くことで、参照や値のキャプチャーを宣言することができ
る。

.. csv-table::
   :delim: |
   :header-rows: 1
   :widths: auto

   記法 | 分類
   ``[]`` | 空
   ``[name1, name2, ...]`` | 値捕捉
   ``[&]`` | 参照捕捉（コンパイラー自身に参照リストであることを推論させる）
   ``[=]`` | 値捕捉（コンパイラー自身に値リストであることを推論させる）

Expression capture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: 読者ノート

   理解には rvalue の概念に加え、スマートポインターの知識が必要。
   :doc:`./chapter05` を先に目を通してから取り組む。

先述の値捕捉および参照捕捉は外側有効域で宣言された変数なので、これらの捕捉メソッ
ドは lvalue を捕捉して rvalue を捕捉しない。

C++14 からは捕捉対象を任意の式で初期化でき、rvalue の捕捉が可能になる。宣言され
ることになる捕捉変数の型は式によって判定され、その判定は ``auto`` を使うのと同じ
だ。例：

.. code:: c++

   #include <iostream>
   #include <memory>  // std::make_unique
   #include <utility> // std::move

   void lambda_expression_capture() {
       auto important = std::make_unique<int>(1);
       auto add = [v1 = 1, v2 = std::move(important)](int x, int y) -> int {
           return x + y + v1 + *v2;
       };
       std::cout << add(3, 4) << std::endl;
   }

スマートポインターオブジェクト ``important`` が ``[=]`` による値捕捉では捕捉でき
ないことに注意する。いったん rvalue に所有権ごと引き渡して式中で初期化する
(``v2``) 必要がある。

.. admonition:: 読者ノート

   捕捉リストの ``v1``, ``v2`` の定義に対して、型が明記されていないので C++ コー
   ドとしては異例だという印象を強く受ける。

Generic Lambda
----------------------------------------------------------------------

ラムダ関数の仮引数にキーワード ``auto`` を使えばテンプレートのように扱える。

.. code:: c++

   void lambda_generic() {
       auto generic = [](auto x, auto y) {
           return x + y;
       };

       std::cout << generic(1, 2) << std::endl;
       std::cout << generic(1.1, 2.2) << std::endl;
   }

JavaScript 感覚だ。

3.2 Function Object Wrapper
======================================================================

この機能は標準ライブラリの一部であり、C++ のランタイム機能を強化するものだ。この
部分も重要なので、導入のためにここに記すとある。

``std::function``
----------------------------------------------------------------------

ラムダ式の本質は、関数オブジェクト型に似たクラス型のオブジェクトであるということ
だ。前者と後者をそれぞれクロージャー型、クロージャーオブジェクトと呼ぶ。ラムダ式
の捕捉リストが空の場合、クロージャーオブジェクトを関数ポインター値に変換して受け
渡すことなども可能だ。本文の例コードから ``auto`` や ``using`` が便利であること
がわかる。

これらから callable の概念が抽象化され、それをラップするのが ``std::function``
だ。関数ポインターに比べれば型安全度が相対的に高い。関数ポインターをラップする
例：

.. code:: c++

   #include <functional>
   #include <iostream>

   int foo(int para) {
       return para;
   }

   int main() {
       std::function<int(int)> func = foo;
       std::cout << func(10) << std::endl;
   }

ラムダ式をラップする例：

.. code:: c++

   #include <functional>
   #include <iostream>

   int main() {
       int important = 10;
       std::function<int(int)> func = [&](int value) -> int {
           return 1 + value + important;
       };
       std::cout << func(10) << std::endl;
   }

``std::bind`` and ``std::placeholder``
----------------------------------------------------------------------

関数呼び出しの実引数を束縛するために ``std::bind`` が使われる。実引数の用意がで
きるタイミングがバラバラのときに有用だ：

.. code:: c++

   int foo(int a, int b, int c) {
       // ...
   }

   int main() {
       // bind parameter 1, 2 on function foo,
       // and use std::placeholders::_1 as placeholder for the first parameter.
       auto bindFoo = std::bind(foo, std::placeholders::_1, 1, 2);

       // when call bindFoo, we only need one param left
       bindFoo(1);
   }

3.3 Rvalue Reference
----------------------------------------------------------------------

Rvalue 参照は、C++11 での導入により歴史的な問題を大量に解決した重要な概念だ。
``std::vector``, ``std::string`` などの余分なオーバーヘッドを排除し、関数オブ
ジェクトコンテナー ``std::function`` の実現を可能にするものだ。

lvalue, rvalue, prvalue, xvalue
----------------------------------------------------------------------

.. admonition:: 読者ノート

   これらの概念を図式化したものを既存ノートから引用する：

   .. mermaid:: /_include/c++-expr-cat.mmd
      :align: center
      :alt: Expression category taxonomy
      :caption: Expression category taxonomy

prvalue (pure rvalue, purely rvalue) は、

* ``10``, ``true`` などの純粋なリテラルか、
* ``1 + 2`` などの評価結果がリテラルまたは匿名一時オブジェクトと等価である

かのどちらかだ。非参照によって返される一時変数、演算式によって生成される一時変
数、元のリテラル、ラムダ式はすべて純粋な rvalue だ。特に、リテラル（文字列リテラ
ルを除く）は prvalue だ。文字列リテラルは例外的に ``const char`` 配列型の lvalue
であるとする。

xvalue (expiring value) は C++11 が rvalue 参照を導入するために提案した概念で
（つまり従来の C++ では、prvalue と rvalue は同じ概念）、破棄されるが移動できる
値を意味する。

.. code:: c++

   std::vector<int> foo() {
       std::vector<int> temp = {1, 2, 3, 4};
       return temp;
   }

   std::vector<int> v = foo();

ここで ``foo()`` で生成された戻り値は一時的な値だ。``v`` にコピーされると即座に
破棄され、取得・変更することはできない。C++11 以降、コンパイラーは lvalue である
``temp`` に対して、``static_cast<std::vector<int> &&>(temp)`` と同等の暗黙の
rvalue変換を行い、``v`` は ``foo`` が返す値をローカルに move させるという作業を
行うようになった。

rvalue reference and lvalue reference
----------------------------------------------------------------------

xvalue を取得するには、rvalue 参照の宣言 ``T&&`` を使用する。rvalue 参照の宣言
は、この一時的な値の寿命を延長する。変数が生きている限り、xvalue は存続する。

C++11 では、lvalue 引数を無条件に rvalue に変換する ``std::move`` がある。
``std::move`` は宣言がヘッダーファイル ``<utility>`` にある。これを使えば、例え
ば rvalue の一時オブジェクトを簡単に取得することができる。

.. code:: c++

   std::string lv1 = "string,";       // lv1 is a lvalue
   // std::string&& r1 = lv1;          // illegal, rvalue can't ref to lvalue
   std::string&& rv1 = std::move(lv1); // legal, std::move can convert lvalue to rvalue

Move semantics
----------------------------------------------------------------------

従来の C++ ではコピーコンストラクターやコピー代入演算子でしかクラスオブジェクト
の複製を設計していなかった。資源の移動を実装するには、呼び出し側が先に複製してか
ら破壊するメソッドを使う必要があり、そうでなければ、移動先のオブジェクトのイン
ターフェースを自分で実装する必要があった。

こうなると大量のデータが複製され、時間と空間を浪費していた。rvalue 参照の導入
は、複製と移動の概念の混同を解消する狙いがある。

本文の例では、次のコンストラクターが鍵だ：

.. code:: c++

   class A{
      int* pointer;

   public:
      A() : pointer(new int(1)) {
      }

      A(A& a) : pointer(new int(*a.pointer)) {}

      A(A&& a) : pointer(a.pointer) {
          a.pointer = nullptr;
      }

      ~A(){
          delete pointer;
      }

      // ...
   };

   // avoid compiler optimization
   A return_rvalue(bool test) {
       A a, b;
       if(test) return a; // equal to static_cast<A&&>(a);
       else return b; // equal to static_cast<A&&>(b);
   }

   int main() {
       A obj = return_rvalue(false);
       // ...
   }

関数 ``main`` の一行目の右辺が xvalue として評価される。その結果、左辺 ``obj``
の初期化にはコンストラクター ``A(A&&)`` が採用される。``obj.pointer`` は xvalue
のメンバーデータ ``pointer`` と同一であり、このコンストラクター内部で xvalue の
``pointer`` は ``nullptr`` にリセットされる。さらに、xvalue に対してデストラク
ターが直ちに呼び出され、``nullptr`` は安全に処理される。

標準ライブラリーにもこの形式のコンストラクター、代入演算子が提供されている。文字
列の例：

.. code:: c++

   std::string str = "Hello world.";
   std::vector<std::string> v;

   // use push_back(const T&&),
   // no copy the string will be moved to vector,
   // and therefore std::move can reduce copy cost
   v.push_back(std::move(str));

.. admonition:: 読者ノート

   ``const T&&`` は ``const`` なのか？

Perfect forwarding
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

従来の C++ では参照型を参照し続けることできなかった。しかし、rvalue 参照の登場に
よりこの慣習が撤回され、lvalue 参照と rvalue 参照の両方を参照することができる規
則に変わった。

関数テンプレートで ``T&&`` を使用すると、rvalue 参照ができない場合があり、
lvalue が渡されると、この関数への参照は lvalue として導出されることになる。より
正確には、テンプレート引数がどのような参照型であっても、引数の型が右参照である場
合に限り、テンプレート引数は右参照型として導出されることができる。これによ
り、lvalueの受け渡しが成功する。

**完全転送** (perfect forwarding) とは、引数を渡す際に元の引数の型を維持したまま
転送する（渡す）ことを意味する。lvalue 参照は lvalue 参照を、rvalue 参照は
rvalue 参照を維持する。この問題を解決するために、``std::forward`` を使って引数を
転送する必要がある。

``std::forward<T>(v)`` は ``static_cast<T&&>(v)`` に他ならない。

Conclusion
----------------------------------------------------------------------

本章で紹介する機能はすべて知っておいて損はない：

* ラムダ式
* 関数オブジェクトコンテナー ``std::function``
* rvalue 参照

Further Readings
----------------------------------------------------------------------

Bjarne Stroustrup, The Design and Evolution of C++ は邦訳書が確かあったか？
