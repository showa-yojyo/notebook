======================================================================
What's New In C++14 標準ライブラリー
======================================================================

このノートでは C++14 で注目すべき標準ライブラリーの機能を学習する。例によって
cpprefjp_ を利用して、読みながら急所を記していくことにする。興味のないもの、知ら
なくて良いものは積極的に無視する。

以下、断っても断らなくても名前空間 ``std`` またはその部分空間にライブラリー要素
があるものとする。

.. contents::

コンテナー
======================================================================

〈順序付き連想コンテナのルックアップ処理で、一時オブジェクトが生成されるコストを
抑える拡張が行われた〉そうだ。

対象クラステンプレート：

* ``std::map``
* ``std::multimap``
* ``std::set``
* ``std::multiset``

対象メンバー関数：

* ``.find()``
* ``.count()``
* ``.lower_bound()``
* ``.upper_bound()``
* ``.equal_range()``

全部同じだろうから ``std::map::find()`` について言うと、次のオーバーロードが追加
された：

.. code:: c++

   template <class K>
   iterator find(const K& x);

   template <class K>
   const_iterator find(const K& x) const;

cpprefjp_ によれば、これらのオーバーロードはキーが ``std::string`` であるような
連想コンテナーに対して有効となり得る。検索操作で文字列リテラルを渡すときに、従来
のオーバーロードにおいてキー型の一時オブジェクトが生成されることを避けられる。そ
のためには ``std::map`` の第三テンプレート引数に適当な型を明示的に指示するよう
だ。

反復子
======================================================================

ForwardIterator に分類される反復子の初期化に関する仕様追加。省略。

アルゴリズム
======================================================================

範囲チェック版アルゴリズムが追加
----------------------------------------------------------------------

範囲を二つとるようなアルゴリズムの一部においてオーバーロードが追加された。それ
は、一つ目の範囲だけでなく二つ目の範囲に対しても終端を指定するものだ。これを用い
れば、利用者側が範囲同士の長さのテストをする手間が省ける。

オーバーロードが追加されるアルゴリズムは次のものだ：

* ``std::mismatch()``
* ``std::equal()``
* ``std::is_permutation()``

念のため ``std::match()`` の述語なし版の従来版と C++14 追加版の関数シグニチャー
を記す：

.. code:: c++

   template <class InputIterator1, class InputIterator2>
   pair<InputIterator1, InputIterator2> mismatch(
       InputIterator1 first1, InputIterator1 last1,
       InputIterator2 first2);

   template <class InputIterator1, class InputIterator2>
   pair<InputIterator1, InputIterator2> mismatch(
       InputIterator1 first1, InputIterator1 last1,
       InputIterator2 first2, InputIterator2 last2);

乱数ライブラリーの一部が推奨されなくなる
----------------------------------------------------------------------

* ``std::rand()`` を使用するコードをヘッダーファイル ``<random>`` で提供されてい
  る乱数生成器と確率分布とを使用するコードに書き換えるのが望ましい。
* ``std::random_shuffle()`` を使用するコードもそれらおよび ``<algorithm>`` で提
  供されている ``std::shuffle()`` とを組み合わせて使用するコードに書き換えるのが
  望ましい。

メモリー管理
======================================================================

ヘッダーファイル ``<memory>`` に関数テンプレート ``std::make_unique()`` が追加。
これは ``std::shared_ptr`` に対する ``std::make_shared`` の ``std::unique_ptr``
版だ。

入出力
======================================================================

ヘッダーファイル ``<iomanip>`` にマニピュレーター ``std::quoted()`` が追加。

出力時には指定の引用符で文字列を挟み、入力時には文字列の両端から指定の引用符を外
すという振る舞いをするようだ。

リテラル演算子
======================================================================

C++14 では以下のリテラル演算子が標準で提供される。

文字列に関わるリテラル演算子
----------------------------------------------------------------------

リテラル文字列の末尾に ``s`` を付すことで下記のように ``std::basic_string`` 系統
の文字列型を指定することができる。

.. csv-table::
   :delim: @
   :header-rows: 1
   :widths: auto

   Example @ Type @ Encoding
   ``"hello"s`` @ ``std::string`` @ unspecified
   ``L"hello"s`` @ ``std::wstring`` @ unspecified
   ``u8"hello"s`` @ ``std::string`` @ utf-8
   ``u"hello"s`` @ ``std::u16string`` @ utf-16
   ``U"hello"s`` @ ``std::u32string`` @ utf-32

時間に関わるリテラル演算子
----------------------------------------------------------------------

クラステンプレート ``std::chrono::duration`` の各型に関するリテラル演算子が追
加。

.. csv-table::
   :delim: @
   :header-rows: 1
   :widths: auto

   Suffix @ Type
   ``ns`` @ ``nanoseconds``
   ``us`` @ ``microseconds``
   ``ms`` @ ``milliseconds``
   ``s`` @ ``seconds``
   ``min`` @ ``minutes``
   ``h`` @ ``hours``

複素数に関わるリテラル演算子
----------------------------------------------------------------------

クラステンプレート ``std::complex`` の各特殊化に関するリテラル演算子が追加。

.. csv-table::
   :delim: @
   :header-rows: 1
   :widths: auto

   Suffix @ Type
   ``i`` @ ``std::complex<double>``
   ``if`` @ ``std::complex<float>``
   ``il`` @ ``std::complex<long double>``

並行プログラミング
======================================================================

ヘッダーファイル ``<shared_mutex>`` が追加。書き込みと読み込みのスレッドが一対多
のときに適する mutex を提供する。

ユーティリティー
======================================================================

* ヘッダーファイル ``<utility>`` に関数テンプレート ``std::exchange()`` が追加。

  .. code:: c++

     template <class T, class U=T>
     T exchange(T& obj, U&& new_val);

  関数の中身の意味は次の通り：

  .. code:: c++

     T old_val = std::move(obj);
     obj = std::forward<U>(new_val);
     return old_val;

  使い途はじっくり考えるといい。

  本関数テンプレートのように、転送参照を仮引数に持つコードではその仮引数を実引数
  とする ``std::forward()`` の呼び出しが現れるはずだ。

* ヘッダーファイル ``<utility>`` にクラステンプレート ``std::integer_sequence`` が追加。

  .. code:: c++

     template <class T, T... I>
     struct integer_sequence {
         using value_type = T;
         static constexpr std::size_t size() noexcept { return sizeof...(I); }
     };

  これも用途が（説明を読んでもなお）わからない。

* クラステンプレート ``std::tuple`` に対するフリー関数 ``get()`` のオーバーロー
  ドが追加。それは自身を型の組とみなし、型を指定することで対応する値を返すもの
  だ。例えば ``std::get<0>(t)`` ではなく ``std::get<int>(t)`` のように呼び出す。

  .. code:: c++

     template <class T, class... Types>
     constexpr T& get(tuple<Types...>& t) noexcept;

     template <class T, class... Types>
     constexpr T&& get(tuple<Types...>&& t) noexcept;

     template <class T, class... Types>
     constexpr const T& get(const tuple<Types...>& t) noexcept;

* ヘッダーファイル ``<type_traits>`` の ``type`` を定義するクラステンプレートに
  ``_t`` で終わる名前の別名テンプレート版を追加。

  これはあとできちんと調べる。

.. include:: /_include/cpp-refs.txt
