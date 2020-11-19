======================================================================
What's New In C++17 標準ライブラリー
======================================================================

このノートでは C++17 で注目すべき標準ライブラリーの機能を学習する。
例によって cpprefjp_ を利用して、読みながら急所を記していくことにする。
興味のないもの、知らなくて良いものは積極的に無視する。

以下、断っても断らなくても名前空間 ``std`` またはその部分空間にライブラリー要素があるものとする。

.. contents::

新ライブラリー
======================================================================

* ヘッダーファイル追加

  * ヘッダーファイル ``<filesystem>`` 追加。そういえば今までなかった。
  * ヘッダーファイル ``<algorithm>`` や ``<numeric>`` の関数に並列実行機能オプション追加。
  * ヘッダーファイル ``<optional>`` 追加。Boost 出身と思われる。
  * ヘッダーファイル ``<variant>`` 追加。Boost 出身と思われる。
  * ヘッダーファイル ``<any>`` 追加。Boost 出身と思われる。

* 標準ライブラリーの参照を C11 に更新。これは C++ というより C なので割愛。

コンテナー
======================================================================

* コンテナーのコピー、ムーブ、および ``swap()`` に例外仕様 ``noexcept`` が追加。

  .. code:: c++

     vector::vector(vector&& x) noexcept;

     // xxxx 部分は複雑なので仕様書を確認すること
     vector& vector::operator=(vector&& x) noexcept(xxxx);
     void vector::swap(vector& x) noexcept(xxxx);
     // etc.

* ヘッダーファイル ``<iterator>`` に次のフリー関数が追加：

  * ``std::size()``
  * ``std::empty()``
  * ``std::data()``

* コンテナーに「不完全型の最小サポート」が追加。メンバー関数を呼び出すまでに要素型が完全型になっていれば OK になった。
* ヘッダーファイル ``<memory_resource>`` が追加。よくわからない。
* 標準イテレーター全般およびクラステンプレート ``std::array`` の変更操作が ``constexpr`` 化。
* コンテナーのメンバー関数 ``.emplace_front()``, ``.emplace_back()`` が生成した値を返すようになった。

  * この仕様変更はどうだろう。それなら自分でコンストラクターを呼び出して ``.push_front()``,
    ``.push_back()`` でいいのでは？

* 連想コンテナーに次のメンバー関数が追加：

  * ``.extract()``: 要素を他のコンテナーに移すためのノードと呼ばれるオブジェクトを返す。
  * ``.insert(node_type&&)``: よそから引き出したノードをこのコンテナーに挿し込む。
  * ``.merge()``: 重複しないキーの要素をこのコンテナーに取り込む。

* クラステンプレート ``std::map``, ``std::unordered_map`` それぞれに次のメンバー関数が追加：

  * ``.try_emplace()``: 指定キーが不在の場合に限り emplace する（そうでなければ何もしない）。
  * ``.insert_or_assign()``: Python の ``dict`` における ``m[key] = value`` のように振る舞う。

* イテレーターの分類 *contiguous iterator* が追加。
  組み込み配列のように、要素同士がメモリー上で隣接しているようなコンテナーに対するイテレーターであることを意味する。
  次のコンテナーのイテレーターは contiguous iterator であるとする：

  * クラステンプレート ``std::basic_string``
  * クラステンプレート ``std::array``
  * クラステンプレート ``std::vector`` - ただし特殊化 ``std::vector<bool>`` を除く。
  * クラステンプレート ``std::valarray`` - フリー関数 ``std::begin()``, ``std::end()`` によりイテレーターが得られることに注意。

アルゴリズム
======================================================================

ヘッダーファイル ``<algorithm>``
----------------------------------------------------------------------

* 関数テンプレート ``std::sample()`` が追加。後述。
* 関数テンプレート ``std::for_each_n()`` が追加。

  .. code:: c++

     template <class InputIterator, class Size, class Function>
     InputIterator for_each_n(
         InputIterator first,
         Size n,
         Function f);

  * 範囲 ``[first, first + n)`` を指すイテレーター ``i`` に対して ``f(*i)`` を呼び出す。
  * なお、関数 ``f()`` では ``*i`` を変更することが許される。
  * 関数 ``f()`` の戻り値は使われない。
  * 戻り値はイテレーター ``first + n`` とする。
  * さらに並列バージョンがある。割愛。

* 関数テンプレート ``std::clamp()`` が追加。

  .. code:: c++

     template <class T>
     constexpr const T& clamp(const T& v, const T& low, const T& high);

     template <class T, class Compare>
     constexpr const T& clamp(const T& v, const T& low, const T& high, Compare comp);

  * 意味は OpenGL のそれと同じ。第一引数 ``v`` が clamp される。

ヘッダーファイル ``<numeric>``
----------------------------------------------------------------------

* 関数テンプレート ``std::reduce()`` が追加。

  .. code:: c++

     template <class InputIterator>
     typename iterator_traits<InputIterator>::value_type
     reduce(InputIterator first, InputIterator last);

     template <class InputIterator, class T>
     T reduce(InputIterator first, InputIterator last, T init);

     template <class InputIterator, class T, class BinaryOperation>
     T reduce(InputIterator first, InputIterator last, T init,
              BinaryOperation binary_op);

  * 機能は他のプログラミング言語に見られるものと同じ。
  * 演算を引数に取らないものは ``operator+()`` による集計を行う。
  * さらに並列バージョンがある。割愛。

* 関数テンプレート ``std::inclusive_scan()`` が追加。部分和を順次計算する。

  * ``init + *first``, ``init + *first + *(first + 1)``, ``init + *first + *(first + 1) + *(first + 2)``, ... を返す。

* 関数テンプレート ``std::exclusive_scan()`` が追加。こちらも部分和を順次計算する。

  * ``init``, ``init + *first``, ``init + *first + *(first + 1)``, ... を返す。

* 関数テンプレート ``std::transform_reduce()`` が追加。

  * 意味は上述の ``std::reduce()`` をしながら ``std::transform()`` するというようなものだ。
  * ``std::transform()`` のように、入力範囲が一つのものと二つのものがある。

* 関数テンプレート ``std::transform_inclusive_scan()`` が追加。詳細割愛。
* 関数テンプレート ``std::transform_exclusive_scan()`` が追加。詳細割愛。

ヘッダーファイル ``<functional>``
----------------------------------------------------------------------

* ``std::not_fn()`` 追加。指定された述語の意味を否定するような述語を返す。
* ``std::invoke()`` 追加。これは意味がわからない。

ヘッダーファイル ``<memory>``
----------------------------------------------------------------------

* 関数テンプレート ``std::destroy_at()`` が追加。

  * 与えられたポインターに対してデストラクターを明示的に呼び出す。
  * 通常は placement new により生成されたオブジェクトに対して適用する。

* 関数テンプレート ``std::destroy()`` が追加。
  上記 ``std::destroy_at()`` の始点と終点による範囲バージョン。
* 関数テンプレート ``std::destroy_n()`` が追加。
  これも上記 ``std::destroy_at()`` の始点と長さによる範囲バージョン。

* 関数テンプレート ``std::uninitialized_move()`` が追加。

  * 未初期化記憶域である入力範囲を placement new により初期化して出力範囲に ``std::move()`` する。
  * 入力範囲の指定は始点と終点による。

* 関数テンプレート ``std::uninitialized_move_n()`` が追加。

  * 上述の ``std::uninitialized_move()`` の入力範囲の指定が始点と長さによるもの。

* 関数テンプレート ``std::uninitialized_value_construct()`` が追加。

  * 未初期化記憶域である入力範囲を placement new により初期化して出力範囲に出力する。
    その際、ゼロ初期化をともなう。
  * 上記の入力範囲の指定は始点と終点による。

* 関数テンプレート ``std::uninitialized_value_construct_n()`` が追加。

  * 上述の ``std::uninitialized_value_construct()`` の入力範囲の指定が始点と長さによるもの。

* 関数テンプレート ``std::uninitialized_default_construct()`` が追加。

  * ``std::uninitialized_value_construct()`` の「ゼロで初期化しない」バージョン。
    次のような構造体のオブジェクトを大量に扱う際には初期化しないほうがいいだろう：

    .. code::

       struct Point3D
       {
           double x;
           double y;
           double z;
       };

* 関数テンプレート ``std::uninitialized_default_construct_n()`` が追加。

  * ``std::uninitialized_value_construct_n()`` の「ゼロで初期化しない」バージョン。

ヘッダーファイル ``<utility>``
----------------------------------------------------------------------

関数テンプレート ``std::as_const()`` が追加。
左辺値参照を ``const`` 左辺値参照に変換する。ユースケース不明。

.. code:: c++

   template <class T>
   constexpr add_const_t<T>& as_const(T& t) noexcept;

   template <class T>
   void as_const(const T&&) = delete;

文字列
======================================================================

.. - [`<string_view>`](/reference/string_view.md)ヘッダを新設し、所有権を持たない文字列クラスである[`basic_string_view`](/reference/string_view/basic_string_view.md)を追加
.. - [`basic_string::data()`](/reference/string/basic_string/data.md)メンバ関数の非`const`版を追加
.. - 文字列検索アルゴリズムとして、「ボイヤー・ムーア法 (Boyer-Moore)」の[`std::boyer_moore_searcher`](/reference/functional/boyer_moore_searcher.md)関数オブジェクトと「ボイヤー・ムーア・ホースプール法 (Boyer-Moore-Horspool)」の[`std::boyer_moore_horspool_searcher`](/reference/functional/boyer_moore_horspool_searcher.md)関数オブジェクトを追加。[`std::search()`](/reference/algorithm/search.md)関数のポリシーとして、検索アルゴリズムを指定する
.. - ロケール依存なし、フォーマット解析なしの高速な文字列・数値変換関数として、[`to_chars()`](/reference/charconv/to_chars.md)と[`from_chars()`](/reference/charconv/from_chars.md)を追加
.. - [`char_traits`](/reference/string/char_traits.md)クラスを`constexpr`に対応
.. - バイトデータを表す[`byte`](/reference/cstddef/byte.md)型を追加

並行処理
======================================================================

.. - タイムアウト機能がないReaders-writer lockのミューテックスとして、[`shared_mutex`](/reference/shared_mutex/shared_mutex.md)クラスを追加
.. - スコープ付きロックの可変引数版として、[`scoped_lock`](/reference/mutex/scoped_lock.md)クラスを追加
.. - [`atomic`](/reference/atomic/atomic.md)クラスに、指定された要素型に対するアトミック操作がロックフリー(非ミューテックス)に振る舞うかを判定するために`is_always_lock_free`定数を追加
.. - false sharingとtrue sharingを制御するための機能として、[`hardware_destructive_interference_size`](/reference/new/hardware_destructive_interference_size.md)定数と、[`hardware_constructive_interference_size`](/reference/new/hardware_constructive_interference_size.md)定数を追加

スマートポインター
======================================================================

* クラステンプレート ``std::shared_ptr``

  * 配列に対応
  * メンバー型 ``weak_type`` 追加。指定された要素型の ``weak_ptr`` に等しい。
  * メンバー関数 ``use_count()`` 文書化。

* クラステンプレート ``std::enable_shared_from_this`` の使用法が規定された。

  * TODO: ``std::enable_shared_from_this`` 自体は利用法が限定的なので、ほんとうに使えるか確認すること。

* クラステンプレート ``std::unique_ptr``

  * 配列版の型変換が不当に不適格とされていた不具合を解消するべく、
    変換コンストラクターと変換代入演算子が追加。
  * テンプレート代入演算子が修正。

* その他

数学
======================================================================

* ヘッダーファイル ``<cmath>`` に物理学で利用されそうな関数が追加。一部を列挙すると：

  * ベータ関数 ``std::beta(x, y)``

    * ちなみにガンマ関数は ``std::tgamma(x)`` という。

  * Hermite 多項式 ``std::hermite(n, x)``
  * Legendre 多項式 ``std::legendre(l, x)``

  C でも使われるので「オーバーロード」は関数名が異なる。

* ヘッダーファイル ``<cmath>`` の関数 ``std::hypot(x, y)`` のオーバーロード
  ``std::hypot(x, y, z)`` 追加。

  * C でも使われるので多変数版はないのだろう。

* ヘッダーファイル ``<numeric>`` に関数 ``std::gcd()`` と ``std::lcm()`` が追加。

  .. code:: c++

     template <class M, class N>
     constexpr common_type_t<M, N> gcd(M m, N n);

     template <class M, class N>
     constexpr common_type_t<M, N> lcm(M m, N n);

  見るからに引数 ``m`` と ``n`` に要件があるが、常識的に使えば問題ないはずなので深く立ち入らない。

タプル
======================================================================

* 関数テンプレート ``std::apply()`` 追加。

  .. code:: c++

     template<class F, class Tuple>
     constexpr decltype(auto) apply(F&& f, Tuple&& t);

  意味は ``f(t.get<0>(), t.get<1>(), ...)`` だろう。

* 関数テンプレート ``std::make_from_tuple()`` 追加。Boost

  .. code:: c++

     template <class T, class Tuple>
     constexpr T make_from_tuple(Tuple&& t);

  型 ``T`` のオブジェクトを ``T`` のコンストラクターなどにより生成することになるだろう。

* ``std::pair`` および ``std::tuple`` を初期化子リストから生成しやすくなった。

型特性
======================================================================

.. - 値を返す型特性クラスの`constexpr`変数テンプレート版を追加。変数テンプレート版は、末尾に`_v`が付く。`v`は`value` (値) を意味する
.. - 型特性クラスを定義しやすくするために、[`void_t`](/reference/type_traits/void_t.md)を追加
.. - `bool`定数を表す[`bool_constant`](/reference/type_traits/bool_constant.md)を追加
.. - コンパイル時条件の論理演算のために、論理積である[`conjunction`](/reference/type_traits/conjunction.md)、論理和である[`disjunction`](/reference/type_traits/disjunction.md)、否定である[`negation`](/reference/type_traits/negation.md)を追加
.. - `swap`可能かを判定する型特性クラスとして、[`is_swappable_with`](/reference/type_traits/is_swappable_with.md)、[`is_swappable`](/reference/type_traits/is_swappable.md)、[`is_nothrow_swappable_with`](/reference/type_traits/is_nothrow_swappable_with.md)、[`is_nothrow_swappable`](/reference/type_traits/is_nothrow_swappable.md)を追加
.. - 関数が呼び出し可能かを判定する型特性として、[`is_invocable`](/reference/type_traits/is_invocable.md)、[`is_invocable_r`](/reference/type_traits/is_invocable_r.md)、[`is_nothrow_invocable`](/reference/type_traits/is_nothrow_invocable.md)、[`is_nothrow_invocable_r`](/reference/type_traits/is_nothrow_invocable_r.md)を追加
.. - 自動的にハッシュ値が求められる型かを判定するために[`has_unique_object_representations`](/reference/type_traits/has_unique_object_representations.md)型特性を追加
.. - [`invoke()`](/reference/functional/invoke.md)の追加にともない、関数の戻り値型を取得する型特性[`invoke_result`](/reference/type_traits/invoke_result.md)を追加。これまでの[`result_of`](/reference/type_traits/result_of.md)と違って関数型のテンプレート引数を使用しないため、それによって起こっていた厄介な問題を回避する

時間演算
======================================================================

* クラステンプレート ``std::chrono:duration`` に対する次の操作が追加：

  * 関数テンプレート ``std::chrono::floor()`` 追加
  * 関数テンプレート ``std::chrono::ceil()`` 追加
  * 関数テンプレート ``std::chrono::round()`` 追加
  * 関数テンプレート ``std::chrono::abs()`` 追加

* クラステンプレート ``std::chrono:time_point`` に対する次の操作が追加：

  * 関数テンプレート ``std::chrono::floor()`` 追加
  * 関数テンプレート ``std::chrono::ceil()`` 追加
  * 関数テンプレート ``std::chrono::round()`` 追加

* 上記二つのクラステンプレートの変更操作を ``constexpr`` に対応。
  ``std::chrono::duration`` のほうを次に示す：

  .. code:: c++

     std::chrono::duration& operator++();
     std::chrono::duration& operator--();
     std::chrono::duration& operator+=(const std::chrono::duration&);
     std::chrono::duration& operator-=(const std::chrono::duration&);
     std::chrono::duration& operator*=(const std::chrono::duration::rep&);
     std::chrono::duration& operator/=(const std::chrono::duration::rep&);
     std::chrono::duration& operator%=(const std::chrono::duration::rep&);
     std::chrono::duration& operator%=(const std::chrono::duration&);

乱数
======================================================================

ヘッダーファイル ``<algorithm>`` に関数テンプレート ``sample()`` 追加。

* イテレーターが指定する範囲から指定個数の要素をランダムに抽出する。
* 出力もイテレーターで指定する。
* いつものように乱数エンジンを仕込むコードを書くのが面倒そうだ。

エラーハンドリング
======================================================================

ヘッダーファイル ``<exception>`` に関数 ``std::uncaught_exceptions()`` 追加。

* この関数は現在発生している例外の数を返す。
* 複数形であることに注意。単数形の関数は C++17 にて廃止。

予約済み名前空間
======================================================================

次の名前の名前空間が標準ライブラリーのために予約される。

* ``std`` + 数字

廃止
======================================================================

C++11 や C++14 で deprecated と宣告されたライブラリー要素が C++17 で削られる。 とする：

* クラステンプレート ``std::auto_ptr`` 削除。``std::unique_ptr`` などに移行すること。
* 関数テンプレート ``std::random_shuffle()`` 削除。``std::shuffle()`` に移行すること。
* 旧例外仕様に関連する次の要素：

  * 関数 ``std::unexpected()``, ``std::set_unexpected()``, ``std::get_unexpected()``
  * 型 ``std::unexpected_handler``

* ヘッダーファイル ``<functional>`` における以下の要素

  * 関数 ``std::bind1st()``, ``std::bind2nd()``
  * クラステンプレート ``std::binder1st``, ``std::binder2nd``
  * 関数 ``std::ptr_fun()``, クラス ``std::pointer_to_unary_function``,
    ``std::pointer_to_binary_function``
  * 関数 ``std::mem_fun()``, ``std::mem_fun_ref()``,
    クラステンプレート ``std::mem_fun_t``, ``std::mem_fun1_t``, ``std::mem_fun_ref_t``, ``std::mem_fun1_ref_t``,
    ``std::const_mem_fun_t``, ``std::const_mem_fun1_t``, ``std::const_mem_fun_ref_t``, ``std::const_mem_fun1_ref_t``

  * テンプレートクラス ``std::function`` における ``uses_allocator`` 周り。

* ヘッダーファイル ``<iostream>`` の各種別名定義

非推奨
======================================================================

C++03 までに提供された機能で deprecated とされるものをここでは列挙する。
最近の機能については今のところ習得が不十分なのでここに書くまでもない。

* ヘッダーファイル ``<iterator>`` のクラステンプレート ``std::iterator`` を deprecated とする。
* ヘッダーファイル ``<memory>`` のうち次の要素を deprecated とする。

  * クラステンプレート ``std::allocator`` の次のメンバーを deprecated とする：

    * 型 ``size_type``, ``difference_type``, ``pointer``, ``const_pointer``, ``reference``, ``const_reference``
    * 型 ``rebind``
    * メンバー関数 ``address()``, ``max_size()``, ``construct()``, ``destroy()``
    * メンバー関数 ``allocate()`` の引数 ``hint``

  * 特殊化 ``std::allocator<void>``

  * 関数テンプレート ``std::get_temporary_buffer()``, ``std::return_temporary_buffer()``
  * クラステンプレート ``std::raw_storage_iterator``

* ヘッダーファイル ``<functional>`` のうち次の要素を deprecated とする。

  * 関数テンプレート ``std::not1()``, ``std::not2()``
  * クラステンプレート ``std::unary_negate``, ``std::binary_nagate``
  * 関数オブジェクト各種の型 ``result_type``, ``argument_type``,
    ``first_argument_type``, ``second_argument_type``

* ヘッダーファイル ``<codecvt>`` を deprecated とする。
* ヘッダーファイル ``<exception>`` の関数 ``std::uncaught_exception()`` を deprecated とする。
  代わりに複数形のほうを用いること。

.. include:: /_include/cpp-refs.txt
