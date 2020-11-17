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

.. - コンテナのコピー・ムーブ、`swap`操作に`noexcept`を追加
.. - コンテナの要素情報にアクセスする非メンバ関数として、[`<iterator>`](/reference/iterator.md)に [`size()`](/reference/iterator/size.md), [`empty()`](/reference/iterator/empty.md), [`data()`](/reference/iterator/data.md)関数を追加
.. - コンテナに不完全型の最小サポートを追加。[`vector`](/reference/vector.md), [`list`](/reference/list/list.md), [`forward_list`](/reference/forward_list/forward_list.md)の要素型に、不完全型の指定を許可。ただし、これらのコンテナのなんらかのメンバ関数を呼び出す前には、要素型が完全型になっていること
.. - 多相アロケータとメモリプール。[`<memory_resource>`](/reference/memory_resource.md)が新設され、アロケートする型を規定しないアロケータと、それを利用したメモリプールの仕組みが導入される
.. - 標準イテレータ全般と[`array`](/reference/array/array.md)の変更操作に`constexpr`を追加
.. - `emplace_front()`と`emplace_back()`メンバ関数で、追加された要素を返すようにする
.. - 連想コンテナの接合機能を追加。ほかのコンテナに要素を移すために抽出する`extract()`メンバ関数、抽出された要素をほかのコンテナに移すための`insert()`メンバ関数のオーバーロード、2つの連想コンテナをまるごと接合する`merge()`メンバ関数を追加
.. - `map`と`unordered_map`に、挿入失敗時の動作を規定した新たなメンバ関数として、`try_emplace()`と`insert_or_assign()`を追加
.. - イテレータの分類に「隣接イテレータ (contiguous iterator)」を追加。要素間のメモリが隣接していることを表す。以下のコンテナのイテレータは、隣接イテレータであることが規定される：
..   - [`basic_string`](/reference/string/basic_string.md)
..   - [`array`](/reference/array/array.md)
..   - `bool`以外を要素型とする[`vector`](/reference/vector.md)
..   - [`valarray`](/reference/valarray/valarray.md) (の非メンバ関数である[`std::begin()`](/reference/valarray/valarray/begin_free.md)、[`std::end()`](/reference/valarray/valarray/end_free.md)で返されるイテレータは隣接イテレータ)

アルゴリズム
======================================================================

.. - ランダムサンプリングアルゴリズムとして、[`sample()`](/reference/algorithm/sample.md)を追加
.. - 並列アルゴリズムの追加にともない、[`<algorithm>`](/reference/algorithm.md)に[`for_each_n()`](/reference/algorithm/for_each_n.md)を追加
.. - 並列アルゴリズムの追加にともない、[`<numeric>`](/reference/numeric.md)に以下を追加：
..   - [`accumulate()`](/reference/numeric/accumulate.md)の計算順序を規定しないバージョンである、[`reduce()`](/reference/numeric/reduce.md)を追加
..   - 部分和を求める関数[`partial_sum()`](/reference/numeric/partial_sum.md)を、i番目の部分和を求める際にi番目の要素を含める・含めないで分割し、[`inclusive_scan()`](/reference/numeric/inclusive_scan.md)と[`exclusive_scan()`](/reference/numeric/exclusive_scan.md)を追加
..   - 値を変換しながら畳み込む[`transform_reduce()`](/reference/numeric/transform_reduce.md)を追加
..   - 値を変換しながら部分和を求める関数として、[`transform_inclusive_scan()`](/reference/numeric/transform_inclusive_scan.md)と[`transform_exclusive_scan()`](/reference/numeric/transform_exclusive_scan.md)を追加
.. - 値を範囲内に収める[`clamp()`](/reference/algorithm/clamp.md)関数を追加
.. - `bool`を返す関数オブジェクトの結果を反転させる[`not_fn()`](/reference/functional/not_fn.md)関数を追加
.. - [*INVOKE*](/reference/concepts/Invoke.md)要件に従った関数呼び出しをする[`invoke()`](/reference/functional/invoke.md)関数を追加
.. - [`reference_wrapper`](/reference/functional/reference_wrapper.md)がTriviallyCopyableであることを保証
.. - オブジェクトを`const`にする[`as_const()`](/reference/utility/as_const.md)関数を追加
.. - 未初期化メモリのアルゴリズムと、デストラクタ呼び出しの関数として、以下の関数を追加： [`destroy_at()`](/reference/memory/destroy_at.md), [`destroy()`](/reference/memory/destroy.md), [`destroy_n()`](/reference/memory/destroy_n.md), [`uninitialized_move()`](/reference/memory/uninitialized_move.md), [`uninitialized_move_n()`](/reference/memory/uninitialized_move_n.md), [`uninitialized_value_construct()`](/reference/memory/uninitialized_value_construct.md), [`uninitialized_value_construct_n()`](/reference/memory/uninitialized_value_construct_n.md), [`uninitialized_default_construct()`](/reference/memory/uninitialized_default_construct.md), [`uninitialized_default_construct_n()`](/reference/memory/uninitialized_default_construct_n.md)

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

.. - [`duration`](/reference/chrono/duration.md)の丸め演算として、切り下げをする[`floor()`](/reference/chrono/duration/floor.md)、切り上げをする[`ceil()`](/reference/chrono/duration/ceil.md)、最近接遇数への丸めをする[`round()`](/reference/chrono/duration/round.md)、絶対値を求める[`abs()`](/reference/chrono/duration/abs.md)を追加
.. - [`time_point`](/reference/chrono/time_point.md)の丸め演算として、切り下げをする[`floor()`](/reference/chrono/time_point/floor.md)、切り上げをする[`ceil()`](/reference/chrono/time_point/ceil.md)、最近接遇数への丸めをする[`round()`](/reference/chrono/time_point/round.md)を追加
.. - [`duration`](/reference/chrono/duration.md)クラスと[`time_point`](/reference/chrono/time_point.md)クラスの変更操作を`constexpr`に対応

乱数
======================================================================

.. - ランダムサンプリングアルゴリズムとして、[`sample()`](/reference/algorithm/sample.md)を追加
.. - 乱数用語を変更。乱数生成器の要件に 「URNG (Uniform Random Number Generator, 一様乱数生成器)」という用語を使用していたが、
..   一般的なURNGの用語とは異なり、C++の乱数生成器は一度の呼び出しで、(32ビットを超えるような)
..   より多くのビットを単一の符号なし整数にパックして返すという動作が許可されている。
..   動作の誤解を避けるために、「URBG (Uniform Random Bit Generator)」という用語に変更する

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
