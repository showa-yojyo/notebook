======================================================================
Chapter 02: Language Usability Enhancements
======================================================================

`Chapter 02: Language Usability Enhancements <https://changkun.de/modern-cpp/en-us/02-usability>`__
についてのノート。

プログラム実行以前に起こる言語動作を言語可用性と呼ぶことがある。宣言、変数や定数
の定義、コードの流れの制御、オブジェクト指向関数、テンプレートプログラミングなど
が該当する。

.. contents::

2.1 Constants
======================================================================

``nullptr``
----------------------------------------------------------------------

C++11 では本物の null pointer と整数値 0 を区別するために特別に使用されるキー
ワード ``nullptr`` が導入された。``nullptr`` の型は ``nullptr_t`` で、任意のポイ
ンターやメンバーポインター型に暗黙的に変換できる。それらと比較演算子 ``==``,
``!=`` で比較することが可能だ。

``nullptr`` を直接使う習慣を身に着けろ。

``constexpr``
----------------------------------------------------------------------

C++11 では、関数やオブジェクトのコンストラクターがコンパイル時に定数式になること
を明示的に宣言できる ``constexpr`` を用意している。このキーワードは、対象がコン
パイル時に定数式になることをコンパイラーに検証させるものだ。

C++14 から ``constexpr`` が付く関数は、ローカル変数、ループ、分岐などの簡単なス
テートメントが内部で使用可能になった。本書の再帰関数の例を確認しておくこと。

2.2 Variables and initialization
======================================================================

``if``-``switch``
----------------------------------------------------------------------

C++17 では ``if`` 文と ``switch`` 文の丸括弧内で変数宣言および初期化が可能となっ
た。 ``for`` 文の初期化部分と同じようなものと考えられる。

Initializer list
----------------------------------------------------------------------

従来の C++ ではオブジェクトによって初期化方法が異なる。普通の配列、POD は中括弧
記法で初期化できる。これを初期化リストと呼ぶ。一方、クラスオブジェクトの初期化に
は、コピー構文を使うか、丸括弧を使う（コンストラクター呼び出し）必要がある。

C++11 では ``std::initializer_list`` を用いてクラスオブジェクトの初期化を通常の
配列とPOD 初期化方法と同様の記法で行えるようにすることが可能だ。

.. code:: c++

   #include <initializer_list>
   #include <vector>

   class MagicFoo {
       std::vector<int> vec;
   public:
       MagicFoo(std::initializer_list<int> list) {
           for (std::initializer_list<int>::iterator it = list.begin();
                it != list.end(); ++it)
               vec.push_back(*it);
       }
   };

.. admonition:: 読者ノート

   もちろん ``std::vector`` にも初期化リストを引数に取るコンストラクターが用意さ
   れている。それにそのまま渡せばいい。

上のコンストラクターがあれば、次のようにオブジェクトを生成できる：

.. code:: c++

   MagicFoo magicFoo = {1, 2, 3, 4, 5};

この種のコンストラクターを初期化リストコンストラクターと呼ぶ。この例ではコンスト
ラクターを実装したが、通常の関数の引数リストでも初期化リストを置ける。

Structured binding
======================================================================

Python や JavaScript で見るような他の言語で提供されている複数戻り値に似た機能だ。
C++17 から次のように書ける：

.. code:: c++

   auto [x, y, z] = std::make_tuple(1, 2.3, "456");

2.3 Type inference
======================================================================

C++11 では ``auto`` と ``decltype`` というキーワードを導入して型導出を実装し、コ
ンパイラーに変数の型を考慮させるようにした。他の現代的プログラミング言語と同じく
らいに変数の型を気にしなくていいようになった。

``auto``
----------------------------------------------------------------------

``auto`` は従来の C++ では、変数が ``register`` 宣言されていなければ、自動的に自
動変数として扱われるというものだったが、C++11 から意味が全然異なるものに変貌し
た。

.. code:: c++

   auto i = 5;              // i as int
   auto arr = new auto(10); // arr as int *

C++ 20 以降、関数の引数としても ``auto`` を使うこともできる。

.. code:: c++

   int add(auto x, auto y) {
       return x + y;
   }

``decltype``
----------------------------------------------------------------------

キーワード ``decltype`` は式からその型をコンパイラーに推論させる。例：

.. code:: c++

   auto x = 1;
   auto y = 2;
   decltype(x + y) z;

Tail type inference
----------------------------------------------------------------------

新しい順に述べる。C++14 では次の関数テンプレートの戻り値型 ``auto`` が適法だ：

.. code:: c++

   template<typename T, typename U>
   auto add(T x, U y){
       return x + y;
   }

C++11 の時点から次のような文法があった。戻り値型のところに ``decltype(x + y)``
と書ければ一貫性があるのだが、この時点ではコンパイラーは式を構成する ``x``,
``y`` が何であるか解らないので、このような新文法ができた：

.. code:: c++

   template<typename T, typename U>
   auto add(T x, U y) -> decltype(x + y){
       return x + y;
   }

従来の C++ では戻り値型もテンプレート型に書かざるを得なかった。これでは呼び出し
コードを書くのが面倒だ：

.. code:: c++

   template<typename R, typename T, typename U>
   R add(T x, U y) {
       return x + y;
   }

``decltype(auto)``
----------------------------------------------------------------------

.. admonition:: 読者ノート

   :doc:`./chapter03` 内の完全転送を理解してからここに戻ることを推奨されている。

簡単に言うと、``decltype(auto)`` は転送関数やパッケージの戻り値の型を導出するた
めに使われるものだ、``decltype`` の引数式を明示的に指定する必要はないということ
だ。例えば、次の関数があり、それらを個別にラップする関数を定義することを考える：

.. code:: c++

   std::string lookup1();
   std::string& lookup2();

C++11 まででも通じる文法で、次のよう定義される関数を現代的に書き換えることを考え
る：

.. code:: c++

   std::string look_up_a_string_1() {
       return lookup1();
   }
   std::string& look_up_a_string_2() {
       return lookup2();
   }

このような面倒なパラメータ転送は ``decltype(auto)`` を使ってコンパイラーに任せる：

.. code:: c++

   decltype(auto) look_up_a_string_1() {
       return lookup1();
   }
   decltype(auto) look_up_a_string_2() {
       return lookup2();
   }

.. admonition:: 読者ノート

   この節の内容でプログラマーが楽をできる要素は、変数宣言＆初期化における型およ
   び、関数テンプレート、関数定義時における戻り値の型だととりあえず覚えておく。
   コードを書くときには ``auto``, ``decltype(expr)``, ``decltype(auto)`` のどれ
   かが利用できないかを意識すればいい。

2.4 Control flow
======================================================================

``if constexpr``
----------------------------------------------------------------------

C++17 では ``if`` 文に ``constexpr`` キーワードが導入され、コードの中で定数式の
条件を宣言することができる。コンパイル時に分岐判定を完了させればプログラムを効率
化できる。

.. code:: c++

   template<typename T>
   auto print_type_info(const T& t) {
       if constexpr (std::is_integral<T>::value) {
           return t + 1;
       } else {
           return t + 0.001;
       }
   }

.. admonition:: 読者ノート

   上記の関数テンプレートは同じ関数本体で特殊化なしに二つ以上の関数定義を与えて
   いる。

Range-based for loop
----------------------------------------------------------------------

C++11 では範囲ベースの反復法が導入され、Python のように簡潔なループが書ける。

.. code:: c++

   for (auto element: vec)
       std::cout << element << std::endl; // read only
   for (auto &element: vec)
       element += 1;                      // writeable

.. admonition:: 読者ノート

   この結果、標準ファンクターとバインダーの価値が下がった。

2.5 Templates
======================================================================

テンプレートの思想は、コンパイル時に処理できる問題はすべてコンパイル時に放り込
み、実行時にはそれらのコアな動的サービスのみを処理することで、実行時の性能を大幅
に最適化することにある。

Extern Templates
----------------------------------------------------------------------

従来の C++ では、テンプレートは使用されるときにしかコンパイラによってインスタン
ス化されない。つまり、各コンパイル単位 (.cpp) でコンパイルされたコードの中に、完
全に定義されたテンプレートが存在する限り、そのテンプレートはインスタンス化される
ことになる。その結果、インスタンス化が繰り返されるため、コンパイル時間が長くな
る。

このため、C++11 ではテンプレートをインスタンス化するタイミングをコンパイラーに明
示的に指示できるようにした。次の構文により実現する：

.. code:: c++

   extern template class std::vector<double>; // should not instantiation in current file

The ">"
----------------------------------------------------------------------

次のコードは C++11 からはコンパイルエラーが生じなくなっている。つまり、コンパイ
ラーがシフト演算子に解釈しなくなった：

.. code:: c++

   std::vector<std::vector<int>> matrix;

Type alias templates
----------------------------------------------------------------------

C++11では ``using`` を使って次のような別名宣言を与えることができる：

.. code:: c++

   // typedef int (*process)(void *);
   using NewProcess = int(*)(void *);

上記のものは ``typedef`` 記法に対して選択肢が単に増えただけだが、次のものはそう
ではなく、代えが効かない。前提として「テンプレートは型ではない」ことを理解してお
く。

.. code:: c++

   template<typename T, typename U>
   class MagicType {
       // ...
   };

   template<typename T>
   using TrueDarkMagic = MagicType<std::vector<T>, std::string>;

Variadic templates
----------------------------------------------------------------------

テンプレート引数リストが可変個になり得る：

.. code:: c++

   template<typename... Ts> class Magic;

引数を一個以上にしたいならばこう書けばいい：

.. code:: c++

   template<typename Require, typename... Args> class Magic;

テンプレート引数と同様にして、関数引数でも ``...`` 表記を用いて可変長引数を表現
できる：

.. code:: c++

   template<typename... Args> void printf(const std::string &str, Args... args);

引数の個数は ``sizeof...`` で得られる。仮引数自体のアクセス方法は複数ある。まず
は再帰テンプレート展開だ：

.. code:: c++

   template<typename T0>
   void printf1(T0 value) {
       // ...
   }

   template<typename T, typename... Ts>
   void printf1(T value, Ts... args) {
       // ...
       printf1(args...);
   }

次に、C++17 の変数引数テンプレート展開に対応したやり方だ：

.. code:: c++

   template<typename T0, typename... T>
   void printf2(T0 t0, T... t) {
       // ...
       if constexpr (sizeof...(t) > 0) printf2(t...);
   }

最後に、初期化リストとラムダ式を組み合わる方法を紹介してこの節を締めている：

.. code:: c++

   template<typename T, typename... Ts>
   auto printf3(T value, Ts... args) {
       std::cout << value << std::endl;
       std::initializer_list<T>{([&args] {
           std::cout << args << std::endl;
       }(), value)...};
   }

.. admonition:: 読者ノート

   この定義はすぐには理解しがたい。まず

   .. code:: c++

      ([&args] {std::cout << args << std::endl; }()

   でラムダ式を定義してその場で呼び出している。これを ``A`` とおくと、

   .. code:: c++

      std::initializer_list<T>{(A, value)...};

   が現れる。これにより引数の出力が完了することが読める。

Fold expression
----------------------------------------------------------------------

C++17 からは ``...`` の用法がさらに拡張される：

.. code:: c++

   template<typename ... T>
   auto sum(T ... t) {
       return (t + ...);
   }

Non-type template parameter deduction
----------------------------------------------------------------------

型だけではなく、リテラルをテンプレート引数とすることができるのは従来どおりだが、
それに対してもキーワード ``auto`` を用いることが C++17 から許される。例：

.. code:: c++

   template <auto value>
   void foo() {
       std::cout << value << std::endl;
   }

   int main() {
       foo<10>(); // value as int
   }

.. admonition:: 読者ノート

   説明のためだけの例なので、上記コードに実用性は皆無だ。むしろ先の例を再利用し
   てこうしたい：

   .. code:: c++

      template <typename T, auto BufSize>
      class buffer_t {
          T data[BufSize];

      public:
          T& alloc();
          void free(T& item);
      }

      buffer_t<int, 100> buf; // 100 as template parameter

2.6 Object-oriented
======================================================================

Delegate constructor
----------------------------------------------------------------------

C++11 からコンストラクターが同じクラス内の別のコンストラクターを呼び出すことがで
きる。コードの簡略化が図られる。コロンのあとから中括弧を開くまでの部分から呼び出
せる。

Inheritance constructor
----------------------------------------------------------------------

C++11 ではキーワード ``using`` を使って継承コンストラクターの概念を導入してい
る。派生クラスに対して、基底クラスと同じ引数リストのコンストラクターを利用できる
仕組みだ：

.. code:: c++

   class Base{
       int value1;
       int value2;
   public:
       Base() : value1(1){}

       // delegate Base() constructor
       Base(int value) : Base(){
           value2 = value;
       }
   };

   class Subclass : public Base {
   public:
       // inheritance constructor
       // E.g. Subclass s{3};
       using Base::Base;
   };

.. admonition:: 読者ノート

   この例で ``Base(int)`` コンストラクターはメンバー ``value2`` を中括弧の外側で
   初期化できないことに注意。委譲コンストラクター側で初期化されるからだ。

Explicit virtual function overwrite
----------------------------------------------------------------------

昔から C++ をやっているプログラマーならば、次のメンバー関数 ``Subclass::foo`` は
polymorphism が効くことがわかるが、現代の C++ では紛れがないようにする工夫が加
わった。

.. code:: c++

   struct Base {
       virtual void foo();
   };

   struct SubClass: Base {
       void foo();
   };

``override``
----------------------------------------------------------------------

仮想関数に対して明示的に ``override`` と修飾すると、それが基底クラスにある場合に
限り、当該メンバー関数をコンパイラーが認めるようになる。

.. code:: c++

   struct Base {
       virtual void foo(int);
   };

   struct SubClass: Base {
       virtual void foo(int) override; // legal
       virtual void foo(float) override; // illegal, no virtual function in super class
   };

``final``
----------------------------------------------------------------------

本書の記述からすると、キーワード ``final`` は Java にある概念を拝借したものと思
われる。

.. code:: c++

   struct Base {
       virtual void foo() final;
   };

   // legal
   struct SubClass1 final: Base {};

   // illegal, SubClass1 has final
   struct SubClass2 : SubClass1 {};

   struct SubClass3: Base {
       // illegal, foo has final
       void foo();
   };

* ``final`` 宣言されたクラス (e.g. ``Subclass1``) を継承することは許されない。
* ``final`` 宣言された仮想関数 (e.g. ``Base::foo``) をオーバーライドすることは許
  されない。

Explicit delete default function
----------------------------------------------------------------------

一定の条件下で特別メンバー関数をコンパイラーが自動生成するという挙動を、現代の
C++ ではキーワードを付与することで抑止させることが可能だ。逆に、自動生成を明示的
に命じることも可能だ：

.. code:: c++

   class Magic {
   public:
       Magic() = default; // explicit let compiler use default constructor
       Magic& operator=(const Magic&) = delete; // explicit declare refuse constructor
       Magic(int magic_number);
   }

自動生成を有効にするには、メンバー宣言を明示的に与え、そのセミコロンの直前に
``= default`` を記す。反対に無効にするには、同様に ``= delete`` を記す。

.. admonition:: 読者ノート

   これらの文法は純粋仮想関数の ``= 0`` 指定と整合している。

Strongly typed enumerations
----------------------------------------------------------------------

``enum class`` の説明。別の本でやったのでノートを省略する。

* 列挙型の値の既定型が ``int`` であるという解釈になる。
* 値を出力したい場合に面倒な手続きを踏むと読める。

Conclusion
======================================================================

現代の C++ における言語操作性の向上について、最も重要な機能だと思われるものは次
のものだと著者は述べている：

* 自動型推論
* 反復の範囲
* 初期化リスト
* 可変長変数引数テンプレート

Exercises
======================================================================

いずれも C++17 以上でコンパイルする必要がある。

1. このプログラムがやりたいことは、マップの値を対応するハッシュ値に置き換えるこ
   とだ。構文は ``main`` 関数の最後にあるとおり。

   ``&&`` は ``&`` でも動作する。効率は前者のほうが良いことは後ほど習う。

2. 本文中の ``sum`` の例をベースにすると楽であることはすぐにわかる。
   なお、引数の個数がゼロである場合の考慮は不要。コンパイルエラーで構わない。
