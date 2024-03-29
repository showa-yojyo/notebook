======================================================================
Project: A Programming Language
======================================================================

`Eloquent JavaScript <https://eloquentjavascript.net/>`__ Chapter 12 の読書ノート。

本章では JavaScript でプログラミング言語を自作する。

.. contents:: ノート目次

Parsing
======================================================================

* プログラミング言語でいちばん目につくのはその構文、記法だ。
* 解析器 (parser) とはプログラムであって、テキストの断片を読み込んで、それに含ま
  れるプログラムの構造を反映したデータ構造を生成するものだ。

  * 入力テキストが不適格な場合には、解析器はその誤りを指摘しなければならない。

* これから設計する言語 Egg は、単純で一様な構文を持つ。

  * Egg にあるすべては式とする。
  * 式は変数名、数字、文字列、アプリケーションのいずれかの名前とする。

    * アプリケーションは関数呼び出しに使用されるが、さらに``if`` や ``while`` 文
      などの構成にも使用される。

* 解析器を単純にするべく、

  * 文字列はバックスラッシュエスケープのようないかなるものをサポートしない。文字
    列は、二重引用符以外の文字を二重引用符で囲んだものとする。
  * 数字は、数字の列とする。
  * 変数名は、空白文字ではなく、構文上特別な意味を持たない任意の文字で構成できる
    ものとする。

アプリケーションの記述方法は、JavaScript と同様とする。式の後に括弧を付け、その
括弧の間に任意の数の引数を、コンマで区切って記述するものとする。

.. code:: text

   do(define(x, 10),
      f(>(x, 5),
          print("large"),
          print("small")))

* Egg 言語の一様性が意味するところは、JavaScript では演算子であるものが、この言
  語では普通の変数名であるということであって、他の関数のように適用されるというこ
  とだ。
* Egg の構文にはブロックの概念がなく、複数のことを順番に行うことを表現する
  ``do`` 構造が必要だ。
* 解析機がプログラムを記述するのに用いるデータ構造は式オブジェクトからなる。式オ
  ブジェクトのそれぞれには、種類を示すプロパティー ``type`` と、オブジェクトの内
  容を記述するためにあるその他のプロパティーがある。

* ``type`` の値が

  * ``"value"`` である式はリテラル文字列・数値を表す。それらのプロパティー
    ``value`` は文字列・数値を含む。
  * ``"word"`` である式は識別子を表す。そのようなオブジェクトにはプロパティー
    ``name`` があって、文字列として識別子の名前を保持する。
  * ``"apply"`` である式はアプリケーションを表す。

    * プロパティー ``operator`` は適用される式を表す。
    * プロパティー ``args`` は実引数の式からなる配列を保持する。

先ほどのコード片における ``>(x, 5)`` の部分は次のように表現されるだろう：

.. code:: javascript

   {
       type: "apply",
       operator: {type: "word", name: ">"},
       args: [
           {type: "word", name: "x"},
           {type: "value", value: 5}
       ]
   }

* このようなデータ構造を :dfn:`構文木` (syntax tree) という。

  * 第 9 章で見た INI ファイルの解析器とは対照的だ。
  * 木構造を解析するには再帰的な解析関数を書くことになる。

* 関数 ``parseExpression`` を定義する。

  * 入力：文字列
  * 出力：文字列の先頭にある式のデータ構造を含むオブジェクト
  * 出力：解析した後に残る文字列の部分

  部分式を解析するときにこの関数を再度呼び出して、引数の式と残りの文字列を得る。
  この残りには、さらに多くの引数があるかもしれない。

解析器の最初の部分はこのようなものだ：

.. code:: javascript

   function parseExpression(program) {
       program = skipSpace(program);
       let match, expr;

       if (match = /^"([^"]*)"/.exec(program)) {
           expr = {type: "value", value: match[1]};
       } else if (match = /^\d+\b/.exec(program)) {
           expr = {type: "value", value: Number(match[0])};
       } else if (match = /^[^\s(),#"]+/.exec(program)) {
           expr = {type: "word", name: match[0]};
       } else {
           throw new SyntaxError("Unexpected syntax: " + program);
       }
       return parseApply(expr, program.slice(match[0].length));
   }

   function skipSpace(string) {
       let first = string.search(/\S/);
       if (first == -1) return "";
       return string.slice(first);
   }

* 関数 ``skipSpace`` はプログラム文字列の余分な空白文字を捨てるのに使われる。

  * ノート：空白文字しか含まない文字列を与えると、そのときに限り空文字列を返す。
  * ノート：基本的には Python でいう ``str.lstrip`` だ。

* 空白文字を処理してから、関数 ``parseExpression`` は正規表現を用いてEgg がサ
  ポートする三種の要素（文字列、数字、単語）を判定する。判定できたら対応するデー
  タ構造を構築する。

  * ノート：正規表現から、数は十進数表記の正の整数に限るようだ。
  * ノート：単語の正規表現に ``#`` を除外していることは後で意味が出てくる。

* ``SyntaxError`` は JavaScript 標準例外型だ。

プログラム文字列からマッチした部分を切り取り、その部分を式のオブジェクトと一緒に
関数 ``parseApply`` に引き渡す。式がアプリケーションであるかどうかをチェックし、
そうならば括弧でくくられた引数を解析する。

.. code:: javascript

   function parseApply(expr, program) {
       program = skipSpace(program);
       if (program[0] != "(") {
           return {expr: expr, rest: program};
       }

       program = skipSpace(program.slice(1));
       expr = {type: "apply", operator: expr, args: []};
       while (program[0] != ")") {
           let arg = parseExpression(program);
           expr.args.push(arg.expr);

           program = skipSpace(arg.rest);
           if (program[0] == ",") {
               program = skipSpace(program.slice(1));
           } else if (program[0] != ")") {
               throw new SyntaxError("Expected ',' or ')'");
           }
       }
       return parseApply(expr, program.slice(1));
   }

* プログラムの次の文字が開き括弧でない場合、これはアプリケーションではないので、
  関数 ``parseApply`` は与えられた式を返す。そうでなければ、開き括弧を飛ばして、
  このアプリケーション式の構文木オブジェクトを作成する。その後、関数
  ``parseExpression`` を再帰的に呼び出して、閉じ括弧が見つかるまで各引数を解析す
  る。この再帰は ``parseApply`` と ``parseExpression`` が相互に呼び出すことで間
  接的に行われる。

  .. admonition:: 読者ノート

     二つの関数が互いに依存しあっていることに注意する。

* アプリケーション式は例えば ``multiplier(2)(1)`` などのように、それ自体が apply
  されることがあるため、``parseApply`` はアプリケーションを解析した後に、再度自
  分自身を呼び出して、別の括弧のペアが続くかどうかをチェックする必要がある。

以上が Egg の解析に必要なものだ。式を解析した後、入力文字列の最後に到達したかど
うかを確認する便利な関数 ``parse`` でラップする。そしてプログラムのデータ構造が
得られる。

.. code:: javascript

   function parse(program) {
       let {expr, rest} = parseExpression(program);
       if (skipSpace(rest).length > 0) {
           throw new SyntaxError("Unexpected text after program");
       }
       return expr;
   }

   console.log(parse("+(a, 10)"));
   // → {type: "apply",
   //     operator: {type: "word", name: "+"},
   //     args: [{type: "word", name: "a"},
   //     {type: "value", value: 10}]}

The evaluator
======================================================================

評価器に構文木と名前と値を関連付けるスコープオブジェクトを与えると構文木が表現す
る式を評価して、それが生成する値を返す。

.. code:: javascript

   const specialForms = Object.create(null);

   function evaluate(expr, scope) {
       if (expr.type == "value") {
           return expr.value;
       } else if (expr.type == "word") {
           if (expr.name in scope) {
               return scope[expr.name];
           } else {
               throw new ReferenceError(`Undefined binding: ${expr.name}`);
           }
       } else if (expr.type == "apply") {
           let {operator, args} = expr;
           if (operator.type == "word" && operator.name in specialForms) {
               return specialForms[operator.name](expr.args, scope);
           } else {
               let op = evaluate(operator, scope);
               if (typeof op == "function") {
                   return op(...args.map(arg => evaluate(arg, scope)));
               } else {
                   throw new TypeError("Applying a non-function.");
               }
           }
       }
   }

* 評価器にはそれぞれの式の種類に応じたコードがある。

  * リテラル値（これも式の一種）はその値を生成する。
  * 変数については、それがスコープ内に本当に定義されているかをチェックする必要が
    ある。定義されている場合に限り、変数の値を取りに行く。
  * アプリケーションはより複雑だ。

    * ``if`` 文のように特別な形式ならば何も評価せずにこの形式を処理する関数に実
      引数式をスコープとともに渡す。
    * 通常の呼び出しであれば、演算子を評価してそれが関数であることを確認し、評価
      された実引数でそれを呼び出す。

* Egg の関数値を表すのに JavaScript のプレーンな関数値を用いる。
* 関数 ``evaluate`` の再帰的な構造は解析器の類似した構造と似ていて、どちらも言語
  自身の構造を反映している。解析器と評価器を統合して、解析中に評価することもでき
  る。しかし、上記のように分割するとプログラムをより明確にする。

Egg の通訳に必要なのは以上で、実に単純なものだ。しかし、特別な形式をいくつか定義
したり、便利な値を環境に追加したりしないと、多くのことがまだできない。

Special forms
======================================================================

オブジェクト ``specialForms`` を Egg における特別な構文を定義するのに使う。この
オブジェクトはタントとそのような形式を評価する関数とを関連付ける。

まず ``if`` を追加する：

.. code:: javascript

   specialForms.if = (args, scope) => {
       if (args.length != 3) {
           throw new SyntaxError("Wrong number of args to if");
       } else if (evaluate(args[0], scope) !== false) {
           return evaluate(args[1], scope);
       } else {
           return evaluate(args[2], scope);
       }
   };

* Egg の ``if`` 文はちょうど三つの引数を期待する。まず最初の引数を評価して、その
  結果 ``false`` でなければ二番目の引数を評価してそれを返す。``false`` ならば三
  番目の引数を評価してそれを返す。

  * JavaScript の ``if`` というよりは、三項演算子により似ている。
  * これは式であり文ではない。つまり、第二引数または第三引数の結果を生成する。

* さらに ``if`` の条件値の処理方法も異なる。上のコードから明らかにゼロや空の文字
  列を ``false`` 扱いせず、厳密に値 ``false`` を扱う。
* ``if`` を通常の関数ではなく、特別な形式で表現する理由とは、関数への実引数すべ
  てが関数が呼び出されるよりも前に評価される一方で、この ``if`` は、第一引数の値
  に応じて第二引数か第三引数のいずれか一方のみを評価する必要があるからだ。

``while`` 形式も同様にする。

.. code:: javascript

   specialForms.while = (args, scope) => {
       if (args.length != 2) {
           throw new SyntaxError("Wrong number of args to while");
       }
       while (evaluate(args[0], scope) !== false) {
           evaluate(args[1], scope);
       }

       // Since undefined does not exist in Egg, we return false,
       // for lack of a meaningful result.
       return false;
   };

``do`` ループはすべての引数を上から下へ実行する。評価は最後の引数が生成する値
だ。

.. code:: javascript

   specialForms.do = (args, scope) => {
       let value = false;
       for (let arg of args) {
           value = evaluate(arg, scope);
       }
       return value;
   };

変数を定義する機能を実装するために ``define`` という形式も作る。

* 第一引数：単語
* 第二引数：その単語に割り当てる値を生成する式

.. code:: javascript

   specialForms.define = (args, scope) => {
       if (args.length != 2 || args[0].type != "word") {
           throw new SyntaxError("Incorrect use of define");
       }
       let value = evaluate(args[1], scope);
       scope[args[0].name] = value;
       return value;
   };

The environment
======================================================================

評価器が受理するスコープはオブジェクトであって、

* そのプロパティーの名前が変数名と対応し、かつ
* そのプロパティーの値が、変数が束縛されている値に対応する

ようなものだ。

先ほどの ``if`` 文を使用できるようにするには、真偽値にアクセスしなければならな
い。真偽値は二つしかないので、特別な構文は不要だ。単に二つの名前を ``true`` と
``false`` に束縛する。

.. code:: javascript

   const topScope = Object.create(null);

   topScope.true = true;
   topScope.false = false;

* ここで ``topScope`` は大域名前空間を表す。
* これにより真偽値を否定する簡単な式を評価できるようになった。

  .. code:: javascript

     let prog = parse(`if(true, false, true)`);
     evaluate(prog, topScope); // → false

基本的な算術演算子と比較演算子を提供するべく、関数値をいくつか大域名前空間に追加
する。コードを短く保つために、演算子を個別に定義するのではなく JavaScript にある
``Function`` を利用してループ内で一連の演算子を合成する。

.. code:: javascript

   for (let op of ["+", "-", "*", "/", "==", "<", ">"]) {
       topScope[op] = Function("a, b", `return a ${op} b;`);
   }

値を出力する手段が欲しいので ``console.log`` を関数にラップしてそれを ``print``
を名付けることにする。

.. code:: javascript

   topScope.print = value => {
       console.log(value);
       return value;
   };

以上で簡単なプログラムを書くのに十分な初頭的なツールが用意できた。

次の関数 ``run`` は、プログラムを解析して新しいスコープで実行するものだ。

.. code:: javascript

   function run(program) {
       return evaluate(parse(program), Object.create(topScope));
   }

オブジェクトプロトタイプの連鎖を使って入れ子になったスコープを表現して、プログラ
ムが大域名前空間を変更することなしに、そのローカルスコープに変数を追加できるはず
だ。

.. code:: javascript

   run(`
   do(define(total, 0),
      define(count, 1),
      while(<(count, 11),
            do(define(total, +(total, count)),
               define(count, +(count, 1)))),
      print(total))
   `);
   // → 55

* 150 行未満のコードで実装された言語で書かれたものだと思えば悪くない。

Functions
======================================================================

関数機能 ``fun`` 文を定義する。これはそれほど難しくない。

* 最後の引数を関数の本体として扱い、
* それ以外の引数すべてを関数の引数リストとして使用する。

.. code:: javascript

   specialForms.fun = (args, scope) => {
       if (!args.length) {
           throw new SyntaxError("Functions need a body");
       }
       let body = args[args.length - 1];
       let params = args.slice(0, args.length - 1).map(expr => {
           if (expr.type != "word") {
               throw new SyntaxError("Parameter names must be words");
           }
           return expr.name;
       });

       return function() {
           if (arguments.length != params.length) {
               throw new TypeError("Wrong number of arguments");
           }
           let localScope = Object.create(scope);
           for (let i = 0; i < arguments.length; i++) {
               localScope[params[i]] = arguments[i];
           }
           return evaluate(body, localScope);
       };
   };

Egg の関数は固有の関数スコープを有する。``fun`` が生成する関数は、この関数スコー
プを作成し、実引数の変数を追加する。それから、このスコープで関数本体を評価して結
果を返す。

.. code:: javascript

   run(`
   do(define(plusOne, fun(a, +(a, 1))),
      print(plusOne(10)))
   `);
   // → 11

   run(`
   do(define(pow, fun(base, exp,
      if(==(exp, 0), 1, *(base, pow(base, -(exp, 1)))))),
      print(pow(2, 10)))
   `);
   // → 1024

Compilation
======================================================================

* ここまでで実装したのは **インタープリター** だ。インタープリターは評価の際に解
  析器が生成したプログラムの表現に直接作用する。
* :dfn:`コンパイル` とは、解析と実行の間に段階をもう一つ追加する工程だ。これによ
  り、プログラムをより効率的に評価できるものに変換する。
* 伝統的には、コンパイルとはプログラムを機械語に変換することを指すが、プログラム
  を別の表現に変換する工程すべてをコンパイルとみなすこともできる。
* Egg に対する評価戦略としては次のようなものも考えられた。最初にプログラムを
  JavaScript のそれに変換し、``Function`` を使って JavaScript のコンパイラーを起
  動し、その結果を実行するというものだ。

  * これが正しく実装されれば、Egg はひじょうに高速に実行され、なおかつ実装もまっ
    たく単純だ。

Cheating
======================================================================

* Egg の ``if`` と ``while`` の定義をするときに、これらが JavaScript でのそれら
  のちょっとしたラッパーであることに気付いたはずだ。値にいたっては JavaScript の
  値だ。
* JavaScript の上での Egg の実装と、機械が提供する生の機能から直接プログラミング
  言語を実装するのが要求する手間と複雑さを比較すると、その差は歴然としている。
* この章ではプログラミング言語がどのように働くのかを理想的に印象づけた。
* 何かを達成するには、すべてを自分でするよりも、ずるいことをするのが効果的だ。
* この章のおもちゃのような言語はともかく、小さな言語を書くことが実際の仕事で役に
  立つこともある。

  * そのような言語は、一般的なそれと似ている必要はない。
  * 仮に JavaScript に正規表現が存在しなかったならば、自分で正規表現の解析器や評
    価器を独自に書くこともできるだろう。

* :dfn:`ドメイン固有言語` という考え方もある。汎用言語よりも適切な状況があり得
  る。

Exercises
======================================================================

Arrays
----------------------------------------------------------------------

**問題** 次の三つの関数をトップスコープに追加して Egg の配列機能を追加しろ：

* 引数の値を含む配列を構築する ``array(...values)``、
* 配列の長さを取得する ``length(array)``
* 配列から n 番目の要素を取得する ``element(array, n)``

**解答** これは単純に書いてよいだろう：

.. code:: javascript

  topScope.array = (...args) => [...args];
  topScope.length = arr => arr.length;
  topScope.element = (arr, n) => arr[n];

Closure
----------------------------------------------------------------------

**問題** ``fun`` を定義したやり方は、Egg の関数に周囲のスコープを参照することを
許す。つまり、関数の本体に対して、それが定義された時点で見えているローカルな値を
使用するのを許す。JavaScript の関数がそうであるのと同様だ。

次のプログラムはそのことを説明する。関数 ``f`` は自分の引数を ``f`` に対する実引
数に追加する関数を返す。つまり、変数 ``a`` を使えるようにするには、``f`` 内部の
ローカルスコープにアクセスする必要がある。

.. code:: text

   run(`
       do(define(f, fun(a, fun(b, +(a, b)))),
       print(f(4)(5)))
   `);
   // → 9

形式 ``fun`` の定義に戻って、どのような仕組みでこれが動作するのかを動作するのか
を述べろ。

**解答** このコードを JavaScript に翻訳すると：

.. code:: javascript

  function f(a){
      function b(){
          return a + b;
      };
      return b;
  }

``specialForms.fun`` の定義において、関数の本体とスコープを決定するコードは次の
ものだ：

.. code:: javascript

   let localScope = Object.create(scope);
   //console.log(Object.getPrototypeOf(localScope));
   for (let i = 0; i < arguments.length; i++) {
       localScope[params[i]] = arguments[i];
       //console.log(`localScope[${params[i]}] = ${arguments[i]}`);
   }
   return evaluate(body, localScope);

まず ``f`` の定義が起こる。その ``localScope`` に新たに ``a`` が入る。

次に ``b`` の定義が起こる。このとき ``localScope`` のプロトタイプの部分である
``scope`` に ``a`` が含まれていることに注意する。それに対して ``b`` が入る。

したがって、関数 ``b`` は ``f`` のローカルスコープにある ``a`` を参照することが
できる。

Comments
----------------------------------------------------------------------

**問題** 記号 ``#`` を見つけたら、その行の残りの部分をコメントとして扱い、
JavaScript の ``//`` と同じようにそれを無視したい。

この機能をサポートするために、解析器に大きな変更を加える必要はない。
``skipSpace`` がコメントを空白文字のように飛ばすように変更するだけで、
``skipSpace`` が呼び出されるすべてのポイントでコメントも飛ばされるようになる。こ
の変更を加えろ。

**解答** 素直に考えると次のようになる：

.. code:: javascript

   function skipSpace(string) {
       const first = string.search(/\S/);
       if (first == -1) return "";
       return string.slice(first).replace(/#.*/g, "");
   }

ただし、文字列リテラル中に ``#`` を含むようなプログラムに対しては構文エラーを生
じる。

Fixing scope
----------------------------------------------------------------------

現在、変数に値を割り当てる唯一の方法は ``define`` しかない。この構文は、新しい変
数を定義する方法としても、既存の変数に新しい値を与える方法としても機能する。この
曖昧さは問題になる。非ローカル変数に新しい値を与えようとすると、代わりに同じ名前
のローカル変数を定義してしまうことになる。

**問題** ``define`` と同じように、変数に新しい値を与える ``specialForm`` を追加
しろ：内側のスコープにまだ存在していなければ、外側のスコープの変数を更新する。変
数が全く定義されていない場合は、``ReferenceError`` を送出しろ。

* スコープを単純なオブジェクトで表現する手法は、これまでは便利だったが、ここから
  は少々邪魔になる。ここではオブジェクトのプロトタイプを返す
  ``Object.getPrototypeOf`` 関数を使うといいだろう。
* また、スコープは ``Object.prototype`` から派生していないので、スコープに対して
  ``hasOwnProperty`` を呼び出すには、次のような不器用な式を使わなければならない
  ことにも留意しろ：

.. code:: javascript

   Object.prototype.hasOwnProperty.call(scope, name);

**解答** これは時間がかかった。キーワードを ``put`` にすると次のようなコードにな
る：

.. code:: javascript

   specialForms.put = (args, scope) => {
       if (args.length != 2 || args[0].type != "word") {
           throw new SyntaxError("Incorrect use of put");
       }
       const name = args[0].name;
       const value = evaluate(args[1], scope);
       if(Object.prototype.hasOwnProperty.call(scope, name)){
           scope[name] = value;
           return value;
       }
       if(name in scope){
           Object.getPrototypeOf(scope)[name] = value;
           return value;
       }

       throw new ReferenceError(`Incorrect use of put; ${name} is undefined`);
   };

急所は問題文から推察されるように、プロトタイプの理解ができているかどうかだ。次の
ようなコードを修正して色々なパターンを試す：

.. code:: text

   run(`
       do(
           define(x, 3),
           print(x),
           define(
               f, fun(
                   do(
                       #define(x, 0),
                       put(x, 222),
                       #put(y, 222),
                       print("put"),
                       print(x)
                   )
               )
           ),
           f(),
           print("final"),
           print(x)
       )`
   );

以上
