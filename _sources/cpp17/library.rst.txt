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
     // もちろん bool 値に評価される
     vector& vector::operator=(vector&& x) noexcept(xxxx);
     void vector::swap(vector& x) noexcept(xxxx);
     // etc.

* ヘッダーファイル ``<iterator>`` に次のフリー関数が追加：

  * ``std::size()``
  * ``std::empty()``
  * ``std::data()``

* コンテナーに「不完全型の最小サポート」が追加。メンバー関数を呼び出すまでに要素型が完全型になっていれば OK になった。
* ヘッダーファイル ``<memory_resource>`` が追加。よくわからない。
* 標準反復子全般およびクラステンプレート ``std::array`` の変更操作が ``constexpr`` 化。
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

* 反復子の分類 *contiguous iterator* が追加。
  組み込み配列のように、要素同士がメモリー上で隣接しているようなコンテナーに対する反復子であることを意味する。
  次のコンテナーの反復子は contiguous iterator であるとする：

  * クラステンプレート ``std::basic_string``
  * クラステンプレート ``std::array``
  * クラステンプレート ``std::vector`` - ただし特殊化 ``std::vector<bool>`` を除く。
  * クラステンプレート ``std::valarray`` - フリー関数 ``std::begin()``,
    ``std::end()`` により反復子が得られることに注意。

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

  * 範囲 ``[first, first + n)`` を指す反復子 ``i`` に対して ``f(*i)`` を呼び出す。
  * なお、関数 ``f()`` では ``*i`` を変更することが許される。
  * 関数 ``f()`` の戻り値は使われない。
  * 戻り値は反復子 ``first + n`` とする。
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

  * ``init + *first``,
    ``init + *first + *(first + 1)``,
    ``init + *first + *(first + 1) + *(first + 2)``, ... を返す。

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

  * 未初期化記憶域である入力範囲を placement new により初期化して出力範囲に
    ``std::move()`` する。
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

* ヘッダーファイル ``<string_view>`` が追加。クラステンプレート
  ``std::basic_string_view`` を提供。

  * クラステンプレート ``std::basic_string_view`` は生文字列の所有権を持つのではなく、
    既存の文字列を参照して、何らかの情報を与えるというものだ。
    これを参照先の文字列の先頭と、文字列の長さしか管理していないクラスと考えていい。
  * ``.remove_prefix()`` や ``.remove_suffix()`` などというメンバー関数もある。
  * ``std::string_view_literals::operator"" sv()`` でオブジェクトを生成することもできる。

* クラステンプレート ``std::basic_string`` のメンバー関数 ``.data()`` に非 ``const`` 版が追加。
  生文字列を直接変更するのに用いるのだろうか。

* ヘッダーファイル ``<functional>`` に次の二つの関数オブジェクトが追加。
  部分文字列を検索するためのものだ。
  これらはそれぞれ単体でも検索できるし、アルゴリズム ``std::search()`` の引数として与えることもできる。

  * クラステンプレート ``std::boyer_moore_searcher``
  * クラステンプレート ``std::boyer_moore_horspool_searcher``

* ヘッダーファイル ``<charconv>`` に次の関数が追加。
  〈ロケール依存なし、フォーマット解析なし〉で文字列と数値とを変換する。

  * 関数 ``std::to_chars()``
  * 関数 ``std::from_chars()``

* クラステンプレート ``std::char_traits`` の静的メンバー関数の一部に対する ``constexpr`` 対応が追加。

  * メンバー関数 ``.compare()``
  * メンバー関数 ``.find()``
  * メンバー関数 ``.length()``

* ヘッダーファイル ``<cstddef>`` の型 ``std::byte`` が追加。
  次のコードがこの型の定義そのものを正確に表すはずだ：

  .. code::

     enum class byte : unsigned char {};

  * フリー関数の形式で各種ビット演算機能および整数への変換機能が提供される。

並行処理
======================================================================

* ヘッダーファイル ``<shared_mutex>`` およびクラス ``std::shared_mutex`` 追加。

  * クラス ``std::shared_mutex`` は readers-writer lock の mutex を表し、タイムアウトすることがない。
  * このクラスを直接使うよりも、ふつうは RAII 用のクラステンプレート
    ``std::lock_guard()`` もしくは ``std::shared_lock()`` を用いる。
    書くか読むかで使う関数を使い分ける。

* ヘッダーファイル ``<mutex>`` にクラステンプレート ``std::scoped_lock`` 追加。

  * 複数の mutex を管理するための RAII 用クラス。ロックとアンロックの順序に整合性を持たせるために使う。

* クラステンプレート ``std::atomic`` に定数 ``is_always_lock_free`` が追加。
  テンプレート型に対するアトミック操作が常にロックフリーで動作するかどうかを表す ``bool`` 値だ。

* ヘッダーファイル ``<new>`` に次のインライン定数が追加。並行処理に関する知識がないと理解できない概念。

  * ``std::hardware_constructive_interference_size``
  * ``std::hardware_destructive_interference_size``

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

* ヘッダーファイル ``<cmath>`` に物理学で利用されそうな関数が追加。一部を挙げると：

  * ベータ関数 ``std::beta(x, y)``

    * ちなみにガンマ関数は ``std::tgamma(x)`` という。

  * Hermite 多項式 ``std::hermite(n, x)``
  * Legendre 多項式 ``std::legendre(l, x)``

  C でも使われるので「オーバーロード」は関数名が異なる。

* ヘッダーファイル ``<cmath>`` の関数 ``std::hypot(x, y)`` のオーバーロード
  ``std::hypot(x, y, z)`` 追加。

  * C でも使われるので可変数引数版はないのだろう。

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

ヘッダーファイル ``<type_traits>`` に次の機能が追加。

* 値を返す type traits クラステンプレートそれぞれに対応する変数テンプレート版が追加。
  例えばクラステンプレート ``std::is_integral`` に対応する変数テンプレートは
  ``std::is_integral_v`` といい、次のように宣言される：

  .. code:: c++

     template <class T>
     inline constexpr bool is_integral_v = is_integral<T>::value;

* クラステンプレート ``std::void_t`` 追加。次のような仕組みであり、
  SFINAE と組み合わせるというライブラリー設計の手筋があるようだ。

  .. code:: c++

     template <class...>
     using void_t = void;

* クラステンプレート ``std::bool_constant`` 追加。

  .. code:: c++

     template <bool B>
     using bool_constant = integral_constant<bool, B>;

* 論理演算用のクラステンプレートおよびその変数テンプレート版追加。

  * クラステンプレート ``std::conjunction``
  * クラステンプレート ``std::disjunction``
  * クラステンプレート ``std::negation``

* スワップ操作の可能性を決定する次の機能が追加。それぞれ対応する変数テンプレート版もあわせて追加。

  * クラステンプレート ``std::is_swappable`` 追加。
    型の値が ``std::swap()`` により交換可能か。
  * クラステンプレート ``std::is_swappable_with`` 追加。
    二つの型の値が ``std::is_swappable`` であるかどうか。
  * クラステンプレート ``std::is_nothrow_swappable`` 追加。
    ``std::is_swappable`` かつスワップ操作が例外を送出しない保証があるかどうか。
  * クラステンプレート ``is_nothrow_swappable_with`` 追加。
    ``std::is_nothrow_swappable`` かつスワップ操作が例外を送出しない保証があるかどうか。

* 呼び出し可能性を決定する次の機能が追加。それぞれ対応する変数テンプレート版もあわせて追加。

  * クラステンプレート ``std::is_invocable`` 追加。
    ある与えられた型が、別の与えられた型の引数で関数呼び出し可能であるか。
  * クラステンプレート ``std::is_invocable_r`` 追加。
    ``std::is_invocable`` かつまた別の与えられた型の戻り値とするかどうか。
  * クラステンプレート ``std::is_nothrow_invocable``
    ``std::is_invocable`` かつ呼び出しが例外を送出しない保証があるかどうか。
  * クラステンプレート ``std::is_nothrow_invocable_r``
    ``std::is_invocable_r`` かつ呼び出しが例外を送出しない保証があるかどうか。

* クラステンプレート ``std::has_unique_object_representations`` およびその変数テンプレート版追加。

  cpprefjp_ によると〈簡易にハッシュを求めることを将来サポートする前準備として、
  ある型のバイト列をそのままその型のハッシュとして利用できるかを判定するために追加された〉
  そうだ。この記述は実態をよく説明していると思う。

* クラステンプレート ``std::invoke_result`` 追加。
  ``std::invovable`` のような使い方で関数の戻り値型を取得する。cf. ``std::result_of``.

上で私が「クラステンプレート」と書いたところを cpprefjp_ では「メタ関数」と書いていることに注意。

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

* 反復子が指定する範囲から指定個数の要素を無作為抽出する。
* 出力も反復子で指定する。
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

C++11 や C++14 で廃止予定機能と宣告されたライブラリー要素が C++17 で削られる。 とする：

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
    クラステンプレート ``std::mem_fun_t``, ``std::mem_fun1_t``,
    ``std::mem_fun_ref_t``, ``std::mem_fun1_ref_t``,
    ``std::const_mem_fun_t``, ``std::const_mem_fun1_t``,
    ``std::const_mem_fun_ref_t``, ``std::const_mem_fun1_ref_t``

  * テンプレートクラス ``std::function`` における ``uses_allocator`` 周り。

* ヘッダーファイル ``<iostream>`` の各種別名定義

非推奨
======================================================================

C++03 までに提供された機能で廃止予定機能とされるものをここでは列挙する。
最近の機能については今のところ習得が不十分なのでここに書くまでもない。

* ヘッダーファイル ``<iterator>`` のクラステンプレート ``std::iterator`` を廃止予定機能とする。
* ヘッダーファイル ``<memory>`` のうち次の要素を廃止予定機能とする。

  * クラステンプレート ``std::allocator`` の次のメンバーを廃止予定機能とする：

    * 型 ``size_type``, ``difference_type``, ``pointer``, ``const_pointer``,
      ``reference``, ``const_reference``
    * 型 ``rebind``
    * メンバー関数 ``address()``, ``max_size()``, ``construct()``, ``destroy()``
    * メンバー関数 ``allocate()`` の引数 ``hint``

  * 特殊化 ``std::allocator<void>``

  * 関数テンプレート ``std::get_temporary_buffer()``, ``std::return_temporary_buffer()``
  * クラステンプレート ``std::raw_storage_iterator``

* ヘッダーファイル ``<functional>`` のうち次の要素を廃止予定機能とする。

  * 関数テンプレート ``std::not1()``, ``std::not2()``
  * クラステンプレート ``std::unary_negate``, ``std::binary_nagate``
  * 関数オブジェクト各種の型 ``result_type``, ``argument_type``,
    ``first_argument_type``, ``second_argument_type``

* ヘッダーファイル ``<codecvt>`` を廃止予定機能とする。
* ヘッダーファイル ``<exception>`` の関数 ``std::uncaught_exception()`` を廃止予定機能とする。
  代わりに複数形のほうを用いること。

.. include:: /_include/cpp-refs.txt
