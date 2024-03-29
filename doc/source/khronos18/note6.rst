======================================================================
OpenGL Shading Language 4.60 Specification 読書ノート Part 6
======================================================================

`仕様書該当部分 <https://www.khronos.org/registry/OpenGL/specs/gl/GLSLangSpec.4.60.html#statements-and-structure>`__

先に仕様書の内容をそっくりに写して、それから削る形でノートに仕上げたい。

.. contents:: ノート目次

6. Statements and Structure
======================================================================

OpenGL Shading Language の基本的な言語構成要素は次のとおり：

* 文と宣言
* 関数定義
* 選択 (``if`` ... ``else``, ``switch`` ... ``case`` ... ``default``)
* 反復 (``for``, ``while``, ``do`` ... ``while``)
* ジャンプ (``discard``, ``return``, ``break``, ``continue``)

----

シェーダーの全体的な構造は次のとおり：

| *translation-unit* :
|     *global-declaration*
|     *translation-unit global-declaration*
|
| *global-declaration* :
|     *function-definition*
|     *declaration*

つまり、シェーダとは宣言と関数本体の並びだということだ。関数本体は次のように定義
される：

| *function-definition* :
|     *function-prototype* ``{`` *statement-list* ``}``
|
| *statement-list* :
|     *statement*
|     *statement-list* *statement*
|
| *statement* :
|     *compound-statement*
|     *simple-statement*

中括弧 ``{ }`` は、一連の文を複文にまとめるために使用される。

| *compound-statement* :
|     ``{`` *statement-list* ``}``
|
| *simple-statement* :
|     *declaration-statement*
|     *expression-statement*
|     *selection-statement*
|     *iteration-statement*
|     *jump-statement*

単純な宣言、式、ジャンプ文はセミコロンで終わる。

以上には若干の簡略化がある。:ref:`khronos18-9` で規定されている完全な文法を最終
的な仕様とするべきだ。

宣言と式についてはすでに説明したとおりだ。

.. admonition:: 読者ノート

   この章は文法の解説になる。よほど際立つ仕様がない限りはおかしな理解をしないと
   思う。

.. _khronos18-6.1:

6.1. Function Definitions
----------------------------------------------------------------------

上述の文法が示すように、有効なシェーダーは一連の大域宣言と関数定義からなる。関数
一つは次の例が示すように宣言される：

.. code:: glsl

   // prototype
   returnType functionName (type0 arg0, type1 arg1, ..., typen argn);

そして関数一つは次のように定義される：

.. code:: glsl

   // definition
   returnType functionName (type0 arg0, type1 arg1, ..., typen argn)
   {
       // do some computation
       return returnValue;
   }

ここで ``returnType`` は欠かすことができず、かつ ``void`` であってはならない。ま
た：

.. code:: glsl

   void functionName (type0 arg0, type1 arg1, ..., typen argn)
   {
       // do some computation
       return; // optional
   }

``returnValue`` の型が ``returnType`` と合致しない場合、``returnValue`` の型を
``returnType`` に変換する暗黙の変換が :ref:`khronos18-4.1.10` に指定されていなけ
れば、コンパイルエラーになる。

``typeN`` のそれぞれは型を含まなければならず、引数修飾子をオプションで含むことが
できる。宣言の中の仮引数名（上記でいう ``args`` のどれでも）は、宣言形式と定義形
式の両方においてオプションだ。

関数を呼び出すには、関数名の後に括弧 ``( )`` で囲んだ実引数のリストを使用するこ
とによる。

実引数および戻り値の型として、サイズ付き配列を使用することができる。いずれの場合
も、配列のサイズを明示的に指定する必要がある。また、配列のサイズは、関数の宣言で
指定されたサイズと一致しなければならない。

引数の型として構造体も認められている。また、戻り値の型も構造体とすることができ
る。

関数を宣言、定義するための構文については :ref:`khronos18-9` を参照。

関数はすべて、呼び出される前に、プロトタイプで宣言するか、または本体を伴って定義
するかのどちらかが必要だ。例えば：

.. code:: glsl

   float myfunc (float f,      // f is an input parameter
                 out float g); // g is an output parameter

値を返さない関数は ``void`` として宣言しなければならない。``void`` 関数では
``return`` 引数なしで ``return`` を使用することができる。``return`` 文は値しか受
け付けない。

.. code:: glsl

   void func1() { }
   void func2() { return func1(); } // illegal return statement

関数の戻り値の型には、精度修飾子しか許されない。仮引数は引数、精度、記憶修飾子を
持つことができるが、他の修飾子を持てない。

入力引数を受け取らない関数では、引数リストに ``void`` を使用する必要はない。プロ
トタイプ（または定義）が必要なため、空の引数リスト ``()`` が宣言されても曖昧さが
ない。引数リストとしての ``(void)`` という「慣用句」は、便宜上用意されている。

関数名はオーバーロード可能だ。引数の型が異なる限りは、同じ関数名を複数の関数に使
用することができる。関数名が同じ引数型で二度宣言された場合は、戻り値の型とすべて
の修飾子も一致しなければならず、同じ関数が宣言されたことになる。

例：

.. code:: glsl

   vec4 f(in vec4 x, out vec4 y);       // (A)
   vec4 f(in vec4 x, out uvec4 y);      // (B) okay, different argument type
   vec4 f(in ivec4 x, out dvec4 y);     // (C) okay, different argument type
   int f(in vec4 x, out vec4 y);        // error, only return type differs
   vec4 f(in vec4 x, in vec4 y);        // error, only qualifier differs
   vec4 f(const in vec4 x, out vec4 y); // error, only qualifier differs

関数の呼び出しが解決されると、すべての引数の型が完全に一致するかどうかが調べられ
る。厳密に一致するものが見つかると、他の関数はすべて無視され、完全に一致したもの
が採用される。完全に一致するものが見つからない場合は、一致するものを見つけるため
に :ref:`khronos18-4.1.10` の暗黙の変換が適用される。入力引数（``in`` または
``inout`` または既定）の型が不一致の場合、呼び出し引数型から仮引数型への変換があ
ることが必要だ。出力引数（``out`` または ``inout``）の型が不一致の場合、仮引数型
から呼び出し元実引数型への変換があることが必要だ。

暗黙の変換を使用して複数の合致関数を見つけることができるのであれば、単一の最良の
合致関数が求められる。最良合致を決定するために、呼び出し引数と仮引数型の間の変換
は、各関数の引数とマッチする関数の対で比較される。これらの比較が行われた後、各
マッチング関数の対が比較される。次の場合、関数宣言 A は関数宣言 B よりも一致度が
高いと考えられる：

* 少なくとも一つの関数実引数について、A でのその実引数に対する変換が B のそれよ
  りも優る場合。および
* B での変換が A でのそれよりも優る関数実引数がない場合。

単一の関数宣言が、他のすべての一致する関数宣言よりも良く合致していると考えられる
場合は、それが採用される。そうでなければ、曖昧なオーバーロード関数呼び出しに対す
る意味論的なコンパイルエラーが発生する。

あるマッチにおける単一実引数に対する変換が、他のそれに優るかどうかを判定するため
に次の規則が順に適用される：

1. 厳密に一致する方が暗黙の変換を伴う一致に優る。
2. ``float`` から ``double`` への暗黙の変換を含む一致は、他の暗黙の変換を含む一
   致に優る。
3. ``int`` または ``uint`` から ``float`` への暗黙の変換を含む一致は、それらの整
   数型から ``double`` へのそれに優る。

上記の規則のどれも特定の変換の対に適用されない場合、どの変換も他の変換に優るとは
みなされない。

上記の関数プロトタイプ (A), (B), (C) に対して、規則が呼び出し引数の型の異なる集
合にどのように適用されるかを次に示す：

.. code:: glsl

   f(vec4, vec4)   // exact match of vec4 f(in vec4 x, out vec4 y)
   f(vec4, uvec4)  // exact match of vec4 f(in vec4 x, out uvec4 y)
   f(vec4, ivec4)  // matched to vec4 f(in vec4 x, out vec4 y)
                   // (C) not relevant, can't convert vec4 to
                   // ivec4. (A) better than (B) for 2nd
                   // argument (rule 3), same on first argument.
   f(ivec4, vec4); // NOT matched. All three match by implicit
                   // conversion. (C) is better than (A) and (B)
                   // on the first argument. (A) is better than
                   // (B) and (C).

ユーザー定義関数は複数の宣言が可能だ、定義は一つに限る。

----

シェーダーは組み込み関数を再定義することができる。組み込み関数を呼び出す前に
シェーダ内で再宣言した場合（つまりプロトタイプが見える場合）、リンカーはその呼び
出しをリンクされているシェーダーの集合内に限定して解決しようとする。

関数 ``main`` はシェーダー実行形式の入場地点として使用される。シェーダーは
``main`` という関数を含む必要はないが、単一のシェーダー実行形式を形成するために
リンクされたシェーダーの集合の中のシェーダーが一つは含まれていなければならず、そ
うでなければリンクエラーとなる。この関数は引数のない、戻り値のない ``void`` 型の
関数として宣言しなければならない。

.. code:: glsl

   void main()
   {
       ...
   }

関数 ``main`` には ``return`` の用途がある。詳細は :ref:`khronos18-6.4` 参照。

関数 ``main`` を引数や戻り値の型を伴って宣言なり定義なりをすると、コンパイルエ
ラーまたはリンクエラーとなる。

.. _khronos18-6.1.1:

6.1.1. Function Calling Conventions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

関数は値渡しで呼び出される。つまり、入力引数は呼び出し時に関数内に入力コピーさ
れ、出力引数は関数終了前に呼び出し元に出力コピーされる。関数は引数の局所コピーに
働くので、関数内の変数のエイリアスに関する問題はない。どの引数がコピーされるのか
ということを関数の定義や宣言で制御する。

* キーワード ``in`` は、引数が入力コピーされ、出力コピーされないことを示す修飾子
  として使用される。
* キーワード ``out`` は、引数が出力コピーされ、入力コピーされないことを示す修飾
  子として使用される。引数が不必要にコピーされるのを避けるために、可能な限り使用
  されるべきだ。
* キーワード ``inout`` は、引数を入力コピーと出力コピーの両方で使用することを示
  す修飾子として使用される。これは ``in`` と ``out`` の両方を指定するのと同じ意
  味だ。
* このような修飾子を付けずに宣言された関数引数は、``in`` を指定したのと同じ意味
  になる。

.. admonition:: 読者ノート

   コピーインとコピーアウトと書くのをやめた。

すべての引数は、呼び出し時に左から右の順に、厳密に一度だけ評価される。``in`` 引
数の評価は、仮引数にコピーされる値となる。``out`` 引数が評価されると、関数が戻る
ときに値をコピーするために使用される左辺値が得られる。``inout`` 引数を評価する
と、値と左辺値の両方が得られる。値は呼び出し時に仮引数にコピーされ、左辺値は関数
が戻ったときに値をコピーするために使用される。

出力引数が呼び出し元に出力コピーされる順序は未定義だ。

前の節で述べた関数マッチングで引数の型変換が必要である場合、これらの変換は入力コ
ピーおよび出力コピーのタイミングで適用される。

関数では、入力限定の引数への書き込みが許される。関数のコピーしか変更されない。こ
れを防ぐには、引数を ``const`` 修飾子で宣言する。

関数を呼び出す際に、``out`` または ``inout`` として宣言された引数に、左辺値とし
て評価されない式を渡すことはできない。そうでないとコンパイルエラーが発生する。

| *function-prototype* :
|     *precision-qualifier* *type* *function-name* ``(`` *parameter-qualifiers* *precision-qualifier* *type* *name* *array-specifier* , ... ``)``
|
| *type* :
|     any basic type, array type, structure name, or structure definition
|
| *parameter-qualifiers* :
|     *empty*
|     list of *parameter-qualifier*
|
| *parameter-qualifier* :
|     ``const``
|     ``in``
|     ``out``
|     ``inout``
|     ``precise``
|     *memory-qualifier*
|     *precision-qualifier*
|
| *name* :
|     empty
|     identifier
|
| *array-specifier* :
|     empty
|     ``[`` *integral-constant-expression* ``]``

``const`` 修飾子を ``out`` や ``inout`` と一緒に使うことはできない（コンパイルエ
ラー）。上記は、関数の宣言（プロトタイプ）と定義の両方に使用される。したがって、
関数定義は名前のない引数を持つことができる。

再帰は静的なものでも許されない。プログラムの静的な関数呼び出しグラフに循環が含ま
れている場合、静的な再帰が存在する。これには、サブルーチン一様（後述）として宣言
された変数を介したすべての潜在的な関数呼び出しが含まれる。単一のコンパイル単位
（シェーダー）が、静的再帰またはサブルーチン変数を介した再帰の可能性を含む場合、
コンパイルエラーまたはリンクエラー。

6.1.2. Subroutines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: 読者ノート

   この言語には関数とは別にサブルーチンというプログラム構成要素が存在するのだ。
   たいへん興味深い。

サブルーチンは、シェーダーの再コンパイルを必要とせずに、実行中に一つまたはより多
くの関数呼び出しの対象を変更できるような方法でシェーダーをコンパイルするための装
置だ。例えば、単一のシェーダーで複数の照光アルゴリズムに対する対処とともにコンパ
イルし、異なる種類の光や表面素材を処理することができる。このようなシェーダーを使
用するアプリケーションでは、サブルーチンの一様変数の値を変化させることで、照光ア
ルゴリズムを切り替えることができる。サブルーチンを使用するには、サブルーチン型を
宣言し、一つまたはより多くの関数をそのサブルーチン型に関連付け、その型のサブルー
チン変数を宣言する。変数関数に現在代入されている関数は、関数名をサブルーチン変数
名に置き換えた関数呼び出し構文を使って呼び出される。サブルーチン変数は一様変数で
あり、OpenGL API の命令 ``glUniformSubroutinesuiv`` によってしか特定の機能に代入
されない。

SPIR-V の生成時にはサブルーチン機能は使用できない。

サブルーチン型は、関数宣言と同様の文を用いて、次のように ``subroutine`` キーワー
ドを用いて宣言する。

.. code:: glsl

   subroutine returnType subroutineTypeName(type0 arg0, type1 arg1,
                                            ..., typen argn);

関数宣言と同様に、仮引数名 ``args`` はオプションだ。関数は ``subroutine`` キー
ワードと関数が合致するサブルーチン型のリストを使って関数を定義することで、マッチ
する宣言のサブルーチン型と関連付けられる：

.. code:: glsl

   subroutine(subroutineTypeName0, ..., subroutineTypeNameN)
   returnType functionName(type0 arg0, type1 arg1, ..., typen argn)
   { ... } // function body

関数と関連する各サブルーチン型の間で、引数と戻り値の型が一致しない場合はコンパイ
ルエラー。

``subroutine`` 宣言された関数は本体を含まなければならない。オーバーロードされた
関数を ``subroutine`` 宣言することはできない。シェーダーや段階に同名の関数が二つ
以上含まれている場合、その関数名がサブルーチン型に関連付けられていると、プログラ
ムのコンパイルやリンクに失敗する。

``subroutine`` 宣言された関数は、非サブルーチン関数宣言・呼び出しと同様に、
``functionName`` を静的に使用して直接呼び出すこともできる。

サブルーチン型変数は **サブルーチン一様変数** (subroutine uniforms) であることが
要求され、サブルーチン一様変数宣言で特定のサブルーチン型で宣言される。

.. code:: glsl

   subroutine uniform subroutineTypeName subroutineVarName;

サブルーチン一様変数は、関数が呼び出されるのと同じ方法で呼び出される。サブルーチ
ン変数（またはサブルーチン変数配列の要素）が特定の関数に関連付けられている場合、
その変数を介したすべての関数呼び出しは、その特定の関数を呼び出す。

他の一様変数とは異なり、サブルーチン一様変数は、変数が宣言されたシェーダーの実行
段階にスコープされる。

サブルーチン変数は、明示的なサイズの配列として宣言することができ、動的一様な式で
しかインデックスを付けることができない。

下記いずれかの場所以外での ``subroutine`` キーワードの使用はコンパイルエラーとなる：

* 大域スコープでサブルーチン型を宣言する。
* 関数をサブルーチンとして宣言する、または
* サブルーチン変数を大域スコープで宣言する。

.. _khronos18-6.2:

6.2. Selection
----------------------------------------------------------------------

.. admonition:: 読者ノート

   この仕様は C/C++ と同等と思っていて困らない。

当言語における条件付き制御構造は ``if``, ``if`` ... ``else``, ``switch`` のいず
れかの文によって行われる：

| *selection-statement* :
|     ``if`` ``(`` *bool-expression* ``)`` *statement*
|     ``if`` ``(`` *bool-expression* ``)`` *statement* ``else`` *statement*
|     ``switch`` ``(`` *init-expression* ``)`` ``{`` *switch-statement-listopt* ``}``

ここで *switch-statement-list* は、0 個以上の *switch-statement* と言語で定義さ
れた他の文のリストを含む入れ子のスコープであって、*switch-statement* はいくつか
の形式のラベルを追加する。つまり：

| *switch-statement-list* :
|     *switch-statement*
|     *switch-statement-list* *switch-statement*
|
| *switch-statement* :
|     ``case`` *constant-expression* ``:``
|     ``default`` ``:`` *statement*

上記の文法は、この節での議論を援助することを目的としており、正式な文法は
:ref:`khronos18-9` にある。

----

``if`` 式が ``true`` と評価されると最初の文が実行される。``if`` 式が ``false``
と評価されると ``else`` 部がある場合には二番目の文が実行される。

条件式の *bool-expression* には、型が真偽型だと評価される式すべてが使用できる。
ベクトル型は ``if`` 式として認められない。

条件式は入れ子にすることができる。

----

``switch`` 文の *init-expression* の型はスカラー整数でなければならない。``case``
ラベル内の *constant-expression* の値の型もスカラー整数でなければならない。これ
らの値の任意の対が「等しい値」であるかどうかが判定され、型が一致しない場合は、比
較が行われる前に ``int`` を ``uint`` に変換する暗黙の変換が行われる。``case`` ラ
ベルに *init-expression* と同じ値の *constant-expression* があれば、そのラベルの
後に実行が続く。そうでない場合、``default`` ラベルがあれば、そのラベルの後に実行
が続けられる。それ以外の場合は、``switch`` 文の残りの部分を飛ばして実行する。複
数の ``default`` や重複する *constant-expression* があるとコンパイルエラー。ルー
プや他の ``switch`` 文の中に入れ子になっていない ``break`` 文（入れ子になってい
ないか、``if`` 文や ``if`` ... ``else`` 文の中にのみ入れ子になっている）は、
``switch`` 文の残りの部分も飛ばす。C/C++ でいうところの fall through ラベルは認
められているが、ラベルと ``switch`` 文の終わりの間に文がないとコンパイルエラー。
``switch`` 文では最初の ``case`` 文の前に文を記述することはできない。

``case`` ラベルと ``default`` ラベルは ``switch`` 文の中でしか出現しない。
``case`` ラベルや ``default`` ラベルは、対応する ``switch`` 内の他の文や複文の中
に入れ子にすることはできない。

.. _khronos18-6.3:

6.3. Iteration
----------------------------------------------------------------------

.. admonition:: 読者ノート

   この仕様も C/C++ と同等と思っていても困らない。

``for``, ``while``, ``do`` ループ：

| for (init-expression; condition-expression; loop-expression)
|     sub-statement
|
| while (condition-expression)
|     sub-statement
|
| do
|     statement
| while (condition-expression)

``for`` ループは、まず *init-expression* を評価し、次に *condition-expression*
を評価する。*condition-expression* が真と評価されると、ループの本体が実行され
る。本体が実行された後、``for`` ループは、次に *loop-expression* を評価し、次に
*condition-expression* を評価するためにループバックし、 *condition-expression*
の評価が偽になるまで繰り返す。その後、ループは本体を飛ばし *loop-expression* を
飛ばして終了する。*loop-expression* 式で変更された変数は、スコープ内にあれば、
ループが終了した後もその値を維持する。*init-expression* や
*condition-expression* で宣言された変数は、``for`` ループの *sub-statement* が
終了するまでしかスコープに入らない。

``while`` ループは、まず *condition-expression* を評価する。真であれば、本体が実
行される。その後、*condition-expression* が偽と評価されてループを終了し、本体が
飛ばされるまでこの処理が繰り返される。*condition-expression* で宣言された変数は
``while`` ループの *sub-statement* が終了するまでしかスコープに入らない。

``do`` ... ``while`` ループは、まず本体を実行し、次に *condition-expression* を
実行する。これを *condition-expression* が偽と評価されるまで繰り返し、ループを終
了する。

----

*condition-expression* の表現は、真偽で評価されなければならない。

*condition-expression* と *init-expression* は、どちらも変数を宣言して初期化する
ことができる。ただし、*do-while* ループでは *condition-expression* で変数を宣言
することはできない。変数のスコープは、ループの本体を構成する副文の終わりまでしか
ない。

ループは入れ子にすることができる。

非停止ループも許される。非常に長いループや非停止ループの結果はプラットフォームに
よって異なる。

.. _khronos18-6.4:

6.4. Jumps
----------------------------------------------------------------------

これらがジャンプだ：

| *jump_statement* :
|     ``continue`` ``;``
|     ``break`` ``;``
|     ``return`` ``;``
|     ``return`` *expression* ``;``
|     ``discard`` ``;`` // in the fragment shader language only

``goto`` などの構造化されていない制御構造はない。

``continue`` ジャンプはループの中でしか使用されない。このジャンプは、それが含ま
れる最も内側のループの本体の残りの部分を飛ばす。``while`` および ``do`` ...
``while`` ループでは、このジャンプはループ *condition-expression* の次の評価に移
り、そこから先は前述どおりにループが継続する。``for`` ループの場合は、
*loop-expression* に続いて *condition-expression* にジャンプする。

``break`` ジャンプは、ループと ``switch`` 文で使用できる。``break`` ジャンプは、
それを含む最も内側にあるループや ``switch`` 文を直ちに終了させるだけだ。
*condition-expression*, *loop-expression*, *switch-statement* はそれ以上実行され
ない。

``discard`` キーワードは断片シェーダー内でしか使用できない。断片シェーダー内で
は、現在の断片に対する操作を放棄するために使用することができる。このキーワードを
使用すると、断片が破棄され、どのバッファーへの更新も行われない。シェーダー格納
バッファーなどの他のバッファーへの以前の書き込みは影響を受けない。制御フローが
シェーダーから抜けて、この制御フローが非一様な場合（基本形状内の異なる断片が異な
る制御パスを取る場合）、その後の暗黙的または明示的な微分係数は未定義となる。これ
は通常、例えば条件文の中で使用される：

.. code:: glsl

   if (intensity < 0.0)
       discard;

断片シェーダーは、断片のアルファー値を判定し、その結果に基づいて断片を廃棄するこ
とができる。ただし、網羅検査は断片シェーダーの実行後に行われ、網羅検査によってア
ルファー値が変化することがあるので注意が必要だ。

``return`` ジャンプは現在の関数を直ちに終了させる。もし ``expression`` があれ
ば、それがその関数の戻り値となる。

関数 ``main`` は ``return`` を使うことができる。これは関数の終わりに到達したとき
と同じ方法で ``main`` を単に終了させるだけだ。断片シェーダーでの ``discard`` の
使用を意味するものではない。出力を定義する前に ``main`` で ``return`` を使用する
と、出力を定義する前に ``main`` の最後に到達するのと同じ動作になる。
