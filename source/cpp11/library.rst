======================================================================
What's New In C++11 標準ライブラリー
======================================================================

このノートでは C++11 で注目すべき標準ライブラリーの機能を学習する。
すでに cpprefjp_ がそのへんをきれいに整理している。
それを利用して、読みながら急所を記していくことにする。
興味のないもの、知らなくて良いものは積極的に無視する。

以下、断っても断らなくても名前空間 ``std`` にライブラリー要素があるものとする。

.. contents::

コンテナー
======================================================================

固定長配列 ``std::array``
----------------------------------------------------------------------

* ヘッダーファイル ``<array>`` に定義がある。
* 組み込み配列で事欠かないので後回しでいい。
* ``.size()`` と ``.fill()`` が少し便利なくらいか。

単方向リンクリスト ``std::forward_list``
----------------------------------------------------------------------

* ヘッダーファイル ``forward_list`` に定義がある。
* 一言で言えば「末尾がよくわからないリスト」か。例えば ``.front()`` はあるが ``.back()`` がない。
  その他、メンバー関数の名前が ``_front`` や ``_after`` で終わるものがある。

ハッシュベースの連想コンテナー
----------------------------------------------------------------------

従来の ``std::map``, ``std::multimap``, ``std::set``, ``std::multiset`` のハッシュ実装が追加された。
これらは積極的に採用するべきだろう。

* クラステンプレート ``std::unordered_map`` は役割としては ``std::map`` と同じだ。
  違いはハッシュによる実装だということだ。

  * ヘッダーファイル ``<unordered_map>`` に定義がある。
  * インターフェイスは ``std::map`` とよく似ているので、使い方がわからないというようなことはなさそうだ。
  * デモコードの ``um["5th"]`` が 0 を返すことに注意。オブジェクトが存在しないときは、新しい要素が追加される。

* クラステンプレート ``std::unordered_multimap`` は ``std::map`` に対する ``std::multimap`` と類比的なコンテナー型だ。
  つまり、同一キーに対して複数の異なる値を格納することが許されるハッシュマップだ。

  * ヘッダーファイル ``<unordered_map>`` に定義がある。
  * インターフェイスは ``std::unordered_map`` と同様。``operator[]`` についての注意も同様。

* クラステンプレート ``std::unordered_set`` は ``std::set`` のハッシュ実装版と考えて良い。

  * ヘッダーファイル ``<unordered_set>`` に定義がある。
  * 特定の要素が含まれるかどうかのテストには ``.count()`` を用いるのは C++03 から変わりない。
    後年の仕様変更で ``.contains()`` が登場する。

* クラステンプレート ``std::unordered_multiset`` は ``std::set`` に対する ``std::multiset`` と類比的なコンテナー型だ。
  Python でいう ``collections.Counter`` のような役割を期待したい。

  * ヘッダーファイル ``<unordered_set>`` に定義がある。
  * インターフェイスは ``std::unordered_set`` と同様。

コンテナー全般がムーブセマンティクスに対応
----------------------------------------------------------------------

言語仕様で習ったように、コピー処理が省ける文法が追加された。
そこでそれをサポートするメンバー関数のオーバーロードが既存のコンテナーに追加された。

* クラステンプレートのパラメータ ``T`` はムーブ構築のみ可能な型も許される。
* ``push_back()`` や ``insert()`` 等の要素追加のためのメンバ関数が、
  一時オブジェクトも受け取れて、move で挿入することが許される。
* 要素追加のためのメンバ関数として、クラステンプレートのパラメータ ``T`` のコンストラクタ引数を受け取り、
  一時オブジェクトの生成コストを減らせるものが追加。

  * ``emplace()``
  * ``emplace_back()``
  * ``emplace_front()``

  例えば次のコードが有効であるとする。

  .. code:: c++

     commands.push_back(Command("save", false, false));

  このコードは次のように書ける：

  .. code:: c++

     commands.emplace_back("save", false, false);

初期化子リストでオブジェクトを初期化できる
----------------------------------------------------------------------

:doc:`./language` で習ったように、特に標準ライブラリーのコンテナーのオブジェクトを
次のようにしても初期化することができる（実はイコール記号も不要）：

.. code:: c++

   std::vector<int> v = {1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9};

連想コンテナーの場合には結果的に中括弧が入れ子になるだろう。

クラステンプレート ``std::initializer_list`` 追加
----------------------------------------------------------------------

* ヘッダーファイルは ``<initializer_list>`` だ。
* 初期化リストを渡したい関数の引数リストに ``initializer_list<T>`` オブジェクトを（値渡しで）受けとる。
* ``.begin()`` と ``.end()`` があるので、ループで全要素を順にアクセスすることができる。

:doc:`./language` も参照。

イテレーター
======================================================================

関数テンプレート ``std::next()`` および ``std::prev()`` 追加
----------------------------------------------------------------------

受け取ったイテレーターを指定数ぶん次へ進めた、または前へ戻したイテレーターを返す。

* どちらもヘッダーファイル ``<iterator>`` で宣言されている。
* オプショナルにいくつ進めるかを指定できる。デフォルト引数は 1 である。

  * たぶん ``it + 2`` とか ``it - 5`` というコードで間に合うと思うがどうだろう。

* C++03 に ``advance()`` というものがあるが、これとは異なって引数のイテレーターを動かさない。

クラステンプレート ``std::move_iterator`` 追加
----------------------------------------------------------------------

間接参照時に、参照先の要素を move するためのアダプターとして振る舞う。

* ヘッダーファイル ``<iterator>`` に定義されている。
* オブジェクトを生成するにはコンストラクターよりも ``make_move_iterator()`` を呼び出すのが普通。
* デモコードでは ``std::unique_ptr`` の ``std::vector`` オブジェクトを ``assign()`` している。
  この代入はコピーではなくムーブ代入となる。

関数テンプレート ``std::begin()`` および ``std::end()`` 追加
----------------------------------------------------------------------

これらの関数の意味は想像通りだ。フリー関数として提供されるというのが本質的だ。

* ヘッダーファイル ``<iterator>`` で提供されているが、これをインクルードする必要はない。
  新スタイルの ``for`` ループを成立させるためにこれらの関数テンプレートが存在する必要がある。
* 適用できるオブジェクトの型は

  * メンバー関数としての ``.begin()``, ``.end()`` を持つものか、
  * 組み込みの配列

  のどちらかとなっている。

アルゴリズム
======================================================================

C++ といえばアルゴリズムというくらい私はこれを重視している。
以下、ヘッダーファイルは断らない限り ``<algorithm>`` をインクルードするものとする。

関数テンプレート ``std::all_of()``, ``std::any_of()``
----------------------------------------------------------------------

Python の組み込み関数 ``all()`` および ``any()`` の C++ 版だ。
指定範囲が空のときの戻り値も Python と同様の考え方（というより数学）に基づき、それぞれ ``true``, ``false`` を返す。

.. code:: c++

   template <class InputIterator, class Predicate>
   bool all_of(InputIterator first,
               InputIterator last,
               Predicate pred);

   template <class InputIterator, class Predicate>
   bool any_of(InputIterator first,
               InputIterator last,
               Predicate pred);

関数テンプレート ``std::find_if_not()``
----------------------------------------------------------------------

指定された述語が偽であるような最初の要素を指すイテレーターを戻すアルゴリズムだ。
おそらく ``std::find()`` とラムダ式と否定を組み合わせるのが面倒だから提供されているのだろう。

.. code:: c++

   template <class InputIterator, class Predicate>
   InputIterator find_if_not(InputIterator first,
                             InputIterator last,
                             Predicate pred);

関数テンプレート ``std::copy_n()``
----------------------------------------------------------------------

イテレーターの指す要素から初めて、指定個数だけ要素をコピーするアルゴリズムだ。

.. code:: c++

   template <class InputIterator, class Size, class OutputIterator>
   OutputIterator copy_n(InputIterator first,
                         Size n,
                         OutputIterator result);

従来は ``std::copy(first, first + n, result)`` としていた。

関数テンプレート ``std::copy_if()``
----------------------------------------------------------------------

範囲 ``[first, last)`` にある要素から、述語 ``pred`` が真であるような要素だけを
イテレーター ``result`` 以降に戻すアルゴリズムだ。

.. code:: c++

   template <class InputIterator, class OutputIterator, class Predicate>
   OutputIterator copy_if(InputIterator first,
                          InputIterator last,
                          OutputIterator result,
                          Predicate pred);

古の C++ の書籍でその不存在を不思議がられていたアルゴリズムがついに実装された。

関数テンプレート ``std::move()``, ``std::move_backward()``
----------------------------------------------------------------------

これらは ``std::copy()``, ``std::copy_backward()`` の move 版アルゴリズムだ。
だいたい次のようなものだと覚えておいて良い。実際の実装はもっと凝っているだろう：

.. code:: c++

   template <class InputIterator, class OutputIterator>
   OutputIterator move(
       InputIterator first,
       InputIterator last,
       OutputIterator result)
   {
        while(first != last){
            *result++ = move(*first++); // この move は単体版
        }
        return result;
   }

   template<class BidirectionalIterator1, class BidirectionalIterator2>
   BidirectionalIterator2 move_backward(
       BidirectionalIterator1 first,
       BidirectionalIterator1 last,
       BidirectionalIterator2 result)
   {
       while(first != last){
           *--result = move(*--last); // この move は単体版
       }
       return result;
   }

最後に、copy 系と move 系のアルゴリズムでは C++03 と同じく、
入力と出力の範囲が重なり合わないように注意する必要があることを記しておく。

関数テンプレート ``std::shuffle()``
----------------------------------------------------------------------

範囲 ``[first, last)`` をランダムにシャッフルするアルゴリズムだ。
Python の ``random.shuffle()`` と同じ役割を期待する。

関数テンプレート ``std::is_sorted()``
----------------------------------------------------------------------

範囲 ``[first, last)`` がソート済みであるかどうかをテストするアルゴリズムだ。

.. code:: c++

   template <class ForwardIterator>
   bool is_sorted(ForwardIterator first,
                  ForwardIterator last);

   template <class ForwardIterator, class Compare>
   bool is_sorted(ForwardIterator first,
                  ForwardIterator last,
                  Compare comp);

補助関数に ``std::is_sorted_until()`` というものがあり、これの戻り値と
``last`` が等しいかどうかで、指定範囲全体がソート済みであるかどうかを決定するようだ。

関数テンプレート ``std::min()``, ``std::max()`` に初期化リスト版追加
----------------------------------------------------------------------

``std::min()`` も ``std::max()`` も追加内容は同じなので ``min`` だけ記す。

C++03 までは引数をちょうど二つとる関数しかなかったが、C++11 では
``std::initializer_list<T>`` 型オブジェクトを受け取るものが追加された。
これにより、``std::min()`` は有限集合を引数に取るとみなすことができるようになった。

.. code:: c++

   template <class T>
   T min(initializer_list<T> t);

   template <class T, class Compare>
   T min(initializer_list<T> t, Compare comp);

* 呼び出し事前条件は通常版の ``std::min()`` に準じるものとする。
* ``initializer_list`` 版では引数が 0 個である可能性があるが、それは呼び出し側で避ける。

関数テンプレート ``std::minmax()``, ``std::minmax_element()``
----------------------------------------------------------------------

そうなると、一度の呼び出しで最小値と最大値を同時に得ることもできる。
そこでこれらのアルゴリズムも C++11 で提供されるようになった。

.. code:: c++

   template <class T>
   pair<const T&, const T&> minmax(const T& a, const T& b);

   template <class T, class Compare>
   pair<const T&, const T&> minmax(const T& a, const T& b, Compare comp);

   template <class T>
   pair<T, T> minmax(initializer_list<T> t);

   template <class T, class Compare>
   pair<T, T> minmax(initializer_list<T> t, Compare comp);

* 呼び出し事前条件は ``std::min()``, ``std::max()`` に準じるものとする。
* 戻り値の ``.first`` と ``.second`` がそれぞれ最小値と最大値。

関数テンプレート ``std::iota()``
----------------------------------------------------------------------

アルゴリズムというのとは違うが、この枠で紹介されているのでここで習う。

関数テンプレート ``std::iota()`` はヘッダーファイル ``<numeric>`` が提供するもので、
開始値を指定して、そこから連続した値の数列を生成するために用いられる。
シェルで言うなら ``seq`` のような、Python で言うなら ``range()`` のような働きをする。

.. code:: c++

   template <class ForwardIterator, class T>
   void iota(ForwardIterator first, ForwardIterator last, Tue);
   {
       for(; first != last; ++first){
           *first =ue;
           ++value;
       }
   }

増分が ``T& T::operator++()`` の定義で一意的に決まるので、柔軟性がない。

メモリー管理
======================================================================

C++11 では強力なスマートポインターが追加された。Boost 出身の機能と思われる。

クラステンプレート ``std::allocator_traits``
----------------------------------------------------------------------

TBW

クラステンプレート ``std::shared_ptr`` および ``std::unique_ptr``
----------------------------------------------------------------------

これらは C++11 の目玉の一つと考える。どちらもヘッダーファイル ``<memory>`` にある。

* ``std::shared_ptr`` は一つのポインターの所有権を複数のオブジェクトで共有することができる

  * 内部的には参照カウンター方式で参照数を管理している。これはスレッドセーフとする。
  * フリー関数 ``std::make_shared<T>()`` でオブジェクトを作成するとよい。
    なぜならコンストラクターの呼び出しを書くのが面倒だから。

* ``std::unique_ptr`` はポインターの所有権を唯一保持するオブジェクトを意味する。

  * ``std::auto_ptr`` を完全に置き換えるテンプレートだ。
  * コピー代入操作はサポートされない。ムーブ代入はサポートされるが、所有権が代入先に移ることを意味する。
  * 配列もサポート。
  * フリー関数 ``std::make_unique<T>()`` でオブジェクトを作成するとよい。

クラステンプレート ``std::auto_ptr`` を非推奨とする
----------------------------------------------------------------------

この存在が C++11 の新概念と新機能のいくつかの誕生に貢献していると考えたい。
非推奨になっても私は ``std::auto_ptr`` のことを忘れない。

関数テンプレート ``std::addressof()``
----------------------------------------------------------------------

演算子 ``operator&()`` がオーバーロードされている型のオブジェクトに対しても、
そのアドレスを取得することが可能であるように、関数 ``std::addressof()`` が追加された。

.. code:: c++

   template <class T>
   T* addressof(T& r) noexcept;

ヘッダーファイル ``<memory>`` にある。

入出力
======================================================================

ヘッダーファイル ``<istream>`` および ``<ostream>`` に次の関数テンプレート ``operator>>()`` および
``operator<<()`` が追加。一時オブジェクトとしてのストリームというのが想像しづらいのだが。

.. code:: c++

   // <istream>
   template<class CharT, class Traits, class T>
   basic_istream<CharT, Traits>& operator>>(basic_istream<CharT, Traits>&& is, T& x);

   // <ostream>
   template<class CharT, class Traits, class T>
   basic_ostream<CharT, Traits>& operator<<(basic_ostream<CharT, Traits>&& os, const T& x);

文字列処理
======================================================================

新しい文字列型と一方が文字列型であるような型変換関数が追加された。

クラス ``std::u16string`` および ``std::u32string``
----------------------------------------------------------------------

あるクラステンプレートの別名なのだが、表題の文字列型が新たに追加された。
言語仕様のところで見てきた ``char16_t`` と ``char32_t`` をそれぞれ文字型とする文字列型だ。
両方ともヘッダーファイル ``<string>`` にある。

.. code:: c++

   using u16string = basic_string<char16_t>;
   using u32string = basic_string<char32_t>;

本質的には ``std::basic_string`` であるので、使い方は ``std::string`` と同じだと考える。

クラステンプレート ``std::wstring_convert``
----------------------------------------------------------------------

ヘッダーファイル ``<locale>`` にあるクラステンプレート ``std::wstring_convert`` は
マルチバイト文字とワイド文字列の相互変換を行う機能を提供する。

大雑把に説明すると、変換したい二つの文字列型をテンプレート引数として指定して、メンバー関数
``.from_bytes()`` や ``.to_bytes()`` などを利用することを想定しているようだ。

関数 ``std::to_string()`` および ``std::to_wstring()``
----------------------------------------------------------------------

ヘッダーファイル ``<string>`` に以下の関数が追加された。
これらのオーバーロードは ``sprintf()`` または ``swprintf()`` によって数値を文字列に変換する。

.. code:: c++

   string to_string(int);
   string to_string(unsigned int);
   string to_string(long);
   string to_string(unsigned long);
   string to_string(long long);
   string to_string(unsigned long long);
   string to_string(float);
   string to_string(double);
   string to_string(long double);
   wstring to_wstring(int);
   wstring to_wstring(unsigned int);
   wstring to_wstring(long);
   wstring to_wstring(unsigned long);
   wstring to_wstring(long long);
   wstring to_wstring(unsigned long long);
   wstring to_wstring(float);
   wstring to_wstring(double);
   wstring to_wstring(long double);

関数 ``std::stoi()``, ``std::stof()`` など
----------------------------------------------------------------------

ヘッダーファイル ``<string>`` に以下の関数が追加された。いずれも文字列を数値に変換する。

.. code:: c++

   double stod(const std::string& str, std::size_t* idx = nullptr);
   double stod(const std::wstring& str, std::size_t* idx = nullptr);
   float stof(const std::string& str, std::size_t* idx = nullptr);
   float stof(const std::wstring& str, std::size_t* idx = nullptr);
   int stoi(const std::string& str, std::size_t* idx = nullptr, int base = 10);
   int stoi(const std::wstring& str, std::size_t* idx = nullptr, int base = 10);
   long stol(const std::string& str, std::size_t* idx = nullptr, long base = 10);
   long stol(const std::wstring& str, std::size_t* idx = nullptr, long base = 10);
   long double stold(const std::string& str, std::size_t* idx = nullptr);
   long double stold(const std::wstring& str, std::size_t* idx = nullptr);
   long long stoll(const std::string& str,
                   std::size_t* idx = nullptr,
                   long long base = 10);
   long long stoll(const std::wstring& str,
                   std::size_t* idx = nullptr,
                   long long base = 10);
   unsigned long stoul(const std::string& str,
                       std::size_t* idx = nullptr,
                       unsigned long base = 10);
   unsigned long stoul(const std::wstring& str,
                       std::size_t* idx = nullptr,
                       unsigned long base = 10);
   unsigned long long stoull(const std::string& str,
                             std::size_t* idx = nullptr,
                             unsigned long long base = 10);
   unsigned long long stoull(const std::wstring& str,
                             std::size_t* idx = nullptr,
                             unsigned long long base = 10);

* 数値への変換が行われなかった場合に ``std::invalid_argument`` を送出する。
* 数値が変換範囲外であるときなどの場合に ``std::out_of_range`` を送出する。
* これらはグローバルロケールの影響を受けて異なる結果を出力する。

関数オブジェクト
======================================================================

自然なインターフェイスの関数オブジェクトアダプター、バインダーが新規に追加された。
これによって、従来のアダプター、バインダーが非推奨とされることに注意したい。

``std::function``, ``std::bind()`` は必修。

クラステンプレート ``std::function``
----------------------------------------------------------------------

パラメータの型リスト ``ArgTypes...``、戻り値の型 ``R`` に合致するあらゆる関数的な
オブジェクトを保持し、``operator()`` でそれを呼び出すことができるクラステンプレートだ。

.. code:: c++

   template <class R, class... ArgTypes>
   class function<R(ArgTypes...)>;

* ヘッダーファイル ``<functional>`` をインクルードして利用する。
* ``std::function`` のテンプレート引数の指定方法が不慣れなので修練が必要だ。
* コンストラクターは、関数ポインター、関数オブジェクト、ラムダ式など、関数的なオブジェクトを引数に取る。
* ``operator()`` で保持している関数を呼び出し、その戻り値そのものを戻す。
* 本機能の追加に伴い、``std::unary_function``, ``std::binary_function``, etc. は非推奨となる。

関数テンプレート ``std::bind()``
----------------------------------------------------------------------

バインダーというのは次のような性質の関数であると考えるのが早い。
引数として関数オブジェクトと、その引数の一部をとる。そして本体を呼び出すときになって初めて残りの引数を指定して本体を呼び出す装置だ。

.. code:: c++

   template <class F, class... BoundArgs>
   unspecified bind(F&& f, BoundArgs&&... bound_args);

   template <class R, class F, class... BoundArgs>
   unspecified bind(F&& f, BoundArgs&&... bound_args);

ここで ``f`` と　``bound_args`` は関数オブジェクトとその引数リストをそれぞれ意味する。
引数リストは実引数とプレースホルダーで構成される。

* ヘッダーファイル ``<functional>`` をインクルードして利用する。
* プレースホルダーは ``_1``, ``_2``, ... のような識別子であり、ふつうは

  .. code:: c++

     using namespace std::placeholders;

  を宣言してから用いる。

  プレースホルダー ``_i`` は、後で呼び出すときの第 ``i`` 引数をこの引数位置で渡す、の意。

* 本機能の追加に伴い、``std::bind1st()``, ``std::bind2nd()`` は非推奨となる。
  練習問題として、これらを ``std::bind()`` で実装するといい。

関数テンプレート ``std::mem_fn()``
----------------------------------------------------------------------

関数オブジェクトのメンバー関数版と言っていいのか。

.. code:: c++

   template <class R, class T>
   unspecified mem_fn(R T::* pm);

よくあるユースケースは、ユーザー定義型のオブジェクト（のポインター）からなるコンテナーがあるときに、

.. code:: c++

   std::for_each(c.begin(), c.end(), std::mem_fn(&MyClass::func));

とするものだ。

* ヘッダーファイル ``<functional>`` をインクルードして利用する。
* 本機能の追加に伴い、``std::mem_fun()``, ``std::mem_fun_ref()`` は非推奨となる。

左辺値参照を渡すための各種要素
----------------------------------------------------------------------

アダプターやバインダーで引数として参照を明示的に指定するための一連の要素を記す。

.. code:: c++

   template <class T>
   class reference_wrapper;

   template <class T>
   reference_wrapper<T> ref(T& t) noexcept;

   template <class T>
   reference_wrapper<T> ref(reference_wrapper<T> t) noexcept;

   template <class T>
   reference_wrapper<const T> cref(const T& t) noexcept;

   template <class T>
   reference_wrapper<const T> cref(reference_wrapper<T> t) noexcept;

* ヘッダーファイル ``<functional>`` をインクルードして利用する。
* クラステンプレート ``std::reference_wrapper`` は関数テンプレートに変数を参照として渡すために用いられる。
* 関数テンプレート ``std::ref()`` は変数への参照を保持する ``std::reference_wrapper`` オブジェクトを生成して戻す。
  関数テンプレート ``std::cref()`` はその ``const`` 参照版だ。
* 生の参照を引数にとるオーバーロードは ``std::reference_wrapper`` オブジェクトを生成するが、
  他方、``std::reference_wrapper`` オブジェクトを引数に取るオーバーロードは受け取った引数そのものを戻す。

クラステンプレート ``std::hash``
----------------------------------------------------------------------

先述のようにハッシュ系連想コンテナーが提供される。そのためにはキーのためにハッシュ計算が必要だ。
Python でいう特殊メソッド ``__hash__()`` に相当する。

.. code:: c++

   template <class T> struct hash;

   template <> struct hash<bool>;
   template <> struct hash<char>;
   template <> struct hash<signed char>;
   // ...

   template<class T> struct hash<T*>;

* ヘッダーファイル ``<functional>`` をインクルードして利用する。
* 組み込み型のほとんど、および任意のポインター型に対してはテンプレートの特殊化が定義されている。
  それ以外の型についてはハッシュ計算を ``operator()`` を定義することで、
  必要に応じてユーザーが実装しなければならない。

ビット演算関数オブジェクト
----------------------------------------------------------------------

二項演算子 ``&``, ``|``, ``^`` を作用させる関数オブジェクト
``std::bit_and``, ``std::bit_or``, ``std::xor`` が追加された。

シグニチャーはすべて同様なので、``&`` を示す。

.. code:: c++

   template <typename T>
   struct bit_and
   {
       T operator()(const T& x, const T& y) const;
       using first_argument_type = T;
       using second_argument_type = T;
       using result_type = T;
   };

ヘッダーファイル ``<functional>`` をインクルードして利用する。

並行プログラミング
======================================================================

マルチスレッドプログラミングの材料が突如 C++ にやってきたようだ。

クラス ``std::thread``
----------------------------------------------------------------------

Python の ``threading.thread`` のようなクラスが新規追加されたようだ。

* ヘッダーファイル ``<thread>`` で宣言されている。
* このクラスのオブジェクトはコピー不能。
* 非自明なコンストラクターの引数リストは ``functional.bind()`` のそれとよく似ている。
  ただし、このスレッド関数の引数の全てと戻り値は move-construct 可能である必要がある。
* メンバー関数 ``.join()`` で呼び出し元のスレッドをブロックする。Python と同じ。
* メンバー関数 ``.detach()`` という、オブジェクトと内的スレッドを切り離す機能がある。
  意味としてはスマートポインターの ``.release()`` と同じだろう。

クラス ``std::mutex`` などの排他制御装置
----------------------------------------------------------------------

クラス ``std::mutex`` に絞って記す。意味は Python のそれと同じ。

* ヘッダーファイル ``<mutex>`` で宣言されている。
* このクラスのオブジェクトはコピー不能。
* メンバー関数 ``.lock()`` および ``.unlock()`` が提供されている。
  これらの呼び出しにより排他制御をオン・オフする。
  ただし ``.unlock()`` はデストラクターで自動的に呼び出されるわけではない。
  別途クラス ``std::lock_guard`` などのオブジェクトを作成することで、そのコンストラクターとデストラクターがそれぞれ
  ``.lock()`` と ``.unlock()`` を呼び出す。

関数テンプレート ``std::call_once()``
----------------------------------------------------------------------

関数 ``std::call_once()`` は複数スレッドから呼び出されたいが、実際には一度しか処理をしたくないときに利用するものだ。
メインスレッドで支度しておけばよさそうなものだが？

.. code:: c++

   template <class Callable, class ...Args>
   void call_once(once_flag& flag, Callable func, Args&&... args);

* ヘッダーファイル ``<mutex>`` で宣言されている。
* 第一引数はクラス ``std::once_flag`` のオブジェクトだ。``call_once()`` の初回の呼び出し時のみ
  オブジェクトが初期状態であることにより、一度しか処理をしないことができるというわけだ。

クラス ``std::condition_variable`` と ``std::condition_variable_any``
----------------------------------------------------------------------

クラス ``std::condition_variable`` は Python でいう ``threading.Condition`` と同じように、
特定の条件を満たすまでスレッドの実行を待機するのに用いられる。

* ヘッダーファイル ``<condition_variable>`` で宣言されている。
* コピー不能。さらにムーブ不能。
* メンバー関数 ``.wait()`` 系で条件を指定するとともにスレッドを待機させる。
  指定方式により使用するメンバー関数が異なる。
* メンバー関数 ``.notify_one()`` または ``.notify_all()`` で待機解除を通知する。
* ロックは ``std::unique_lock`` しか使えない。

クラス ``std::condition_variable_any`` は ``std::unique_lock`` 以外のロックも併用可能な
``std::condition_variable`` とみなしてよい。

Future デザインパターン
----------------------------------------------------------------------

ヘッダーファイル ``<future>`` からクラステンプレート ``std::future`` や
``std::promise`` が提供されている。Python の ``concurrent.futures`` のようなもののはずだが、
インターフェイスはやや異なるようだ。

* クラステンプレート ``std::future`` には次のようなメンバー関数がある。

  * ``.get()``: サブスレッドの処理結果を得る。
  * ``.wait()`` 系。サブスレッドの処理が終わるまで待機する。

* クラステンプレート ``std::promise`` には次のようなメンバー関数がある。

  * ``.get_future()``: サブスレッドの処理結果を保持している ``std::future`` オブジェクトを得る。
  * ``.set_value()``, ``.set_exception()``: サブスレッドが処理結果を出力するのに用いる。

アトミック操作
----------------------------------------------------------------------

ヘッダーファイル ``<atomic>`` が新たに追加され、そこでは組み込み型に対するアトミック操作をするための
特殊化テンプレートが定義されている。

例えば整数系の型については ``.fetch_add()``, ``.fetch_sub()`` などの算術演算のアトミック版が提供されている。

ユーティリティー
======================================================================

TBW

エラー報告
======================================================================

TBW

正規表現
======================================================================

TBW

乱数
======================================================================

TBW

C 互換ライブラリー
======================================================================

TBW

.. include:: /_include/cpp-refs.txt
