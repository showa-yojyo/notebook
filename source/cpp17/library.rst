======================================================================
What's New In C++17 標準ライブラリー
======================================================================

このノートでは C++17 で注目すべき標準ライブラリーの機能を学習する。
例によって cpprefjp_ を利用して、読みながら急所を記していくことにする。
興味のないもの、知らなくて良いものは積極的に無視する。

以下、断っても断らなくても名前空間 ``std`` またはその部分空間にライブラリー要素があるものとする。

.. contents::

新ライブラリ
======================================================================

.. - [`<filesystem>`](/reference/filesystem.md)ヘッダを新設し、ファイルシステムライブラリを追加。ファイル、ディレクトリなどを扱う
.. - [`<algorithm>`](/reference/algorithm.md)や[`<numeric>`](/reference/numeric.md)のアルゴリズムに、並列実行のオプションを追加
.. - [`<optional>`](/reference/optional.md)ヘッダを新設し、統一的な有効値と無効値の表現をもつ[`optional`](/reference/optional/optional.md)クラスを追加
.. - [`<variant>`](/reference/variant.md)ヘッダを新設し、型安全な共用体[`variant`](/reference/variant/variant.md)クラスを追加
.. - [`<any>`](/reference/any.md)ヘッダを新設し、なんでも代入できる[`any`](/reference/any/any.md)クラスを追加
.. - 標準ライブラリの参照をC11に更新
..   - [`<cfloat>`](/reference/cfloat.md)に、非正規化数の有無を判定するマクロ、10進数の桁数を表すマクロ、正の最小数を表すマクロを追加
..   - [`<cstdlib>`](/reference/cstdlib.md)に、[`aligned_alloc()`](/reference/cstdlib/aligned_alloc.md)関数を追加
..   - [`<ctime>`](/reference/ctime.md)に、[`TIME_UTC`](/reference/ctime/time_utc.md)マクロ, [`timespec`](/reference/ctime/timespec.md)構造体, [`timespec_get()`](/reference/ctime/timespec_get.md)関数を追加
..   - [`<cstdio>`](/reference/cstdio.md)に、[`vfscanf()`](/reference/cstdio/vfscanf.md.nolink)関数を追加
..   - `<ccomplex>`, `<cstdalign>`, `<cstdbool>`, `<ctgmath>`を非推奨化

コンテナ
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

スマートポインタ
======================================================================

.. - [`shared_ptr`](/reference/memory/shared_ptr.md)を配列に対応
.. - [`shared_ptr`](/reference/memory/shared_ptr.md)クラスに、指定された要素型の[`weak_ptr`](/reference/memory/weak_ptr.md)型を表す`weak_type`メンバ型を追加
.. - [`shared_ptr`](/reference/memory/shared_ptr.md)`::`[`use_count()`](/reference/memory/shared_ptr/use_count.md)の仕様を明確化
.. - [`shared_from_this`](/reference/memory/enable_shared_from_this/shared_from_this.md)の指す先が書き換わらないことを規定
.. - 配列版[`unique_ptr`](/reference/memory/unique_ptr.md)の型変換として、以下のコードが不適格だった：
..
..     ```cpp
..     std::unique_ptr<Foo const * const []> ptr1(new Foo*[10]);
..     Foo const * ptr = ptr1[9];
..     ```
..
..   - このようなコードが適格になるよう、変換コンストラクタと変換代入演算子を追加
..
.. - [`unique_ptr`](/reference/memory/unique_ptr.md)のテンプレート代入演算子に、不足していたSFINAEルールを追加
.. - [`owner_less`](/reference/memory/owner_less.md)で、任意の要素型を持つ[`shared_ptr`](/reference/memory/shared_ptr.md)同士を比較できるようにする

数学
======================================================================

.. - [`<cmath>`](/reference/cmath.md)に[数学の特殊関数](/reference/cmath.md#mathematical-special-functions)を追加
.. - [`hypot()`](/reference/cmath/hypot.md)関数の3引数版を追加
.. - 最大公約数と最小公倍数の関数として、[`gcd()`](/reference/numeric/gcd.md)と[`lcm()`](/reference/numeric/lcm.md)を追加

タプル
======================================================================

.. - タプルを展開して関数呼び出しする[`apply()`](/reference/tuple/apply.md)関数を追加
.. - タプルを任意の型のオブジェクトに変換する[`make_from_tuple()`](/reference/tuple/make_from_tuple.md)関数を追加
.. - 初期化子リストから[`pair`](/reference/utility/pair.md)と[`tuple`](/reference/tuple/tuple.md)を構築しやすくするための改善として、以下のコードが適格になるようコンストラクタの仕様を調整：
..
..     ```cpp
..     std::tuple<int, int> pixel_coordinates()
..     {
..       return {10, -15};  // コンパイルエラー
..     }
..
..     struct NonCopyable { NonCopyable(int); NonCopyable(const NonCopyable&) = delete; };
..
..     std::pair<NonCopyable, double> pmd{42, 3.14}; // C++14ではコンパイルエラー
..                                                   // C++17ではOK
..     ```

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
.. - 乱数用語を変更。乱数生成器の要件に 「URNG (Uniform Random Number Generator, 一様乱数生成器)」という用語を使用していたが、一般的なURNGの用語とは異なり、C++の乱数生成器は一度の呼び出しで、(32ビットを超えるような) より多くのビットを単一の符号なし整数にパックして返すという動作が許可されている。動作の誤解を避けるために、「URBG (Uniform Random Bit Generator)」という用語に変更する

エラーハンドリング
======================================================================

.. - 現在発生している例外の数を取得する[`uncaught_exceptions()`](/reference/exception/uncaught_exceptions.md)関数を追加

取り決め
======================================================================

.. - `std` + 数字の名前空間を予約。C++の今後のバージョンアップで標準ライブラリに大きな変更を加えるときのために、「`std` + 数字」 (正規表現では`std\d*`) の名前空間が予約される

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

非推奨化
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
