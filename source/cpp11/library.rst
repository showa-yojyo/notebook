======================================================================
What's New In C++11 標準ライブラリー
======================================================================

このノートでは C++11 で注目すべき標準ライブラリーの機能を学習する。
すでに cpprefjp_ がそのへんをきれいに整理している。
それを利用して、読みながら急所を記していくことにする。
興味のないもの、知らなくて良いものは積極的に無視する。

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
   void iota(ForwardIterator first, ForwardIterator last, T value);
   {
       for(; first != last; ++first){
           *first = value;
           ++value;
       }
   }

増分が ``T& T::operator++()`` の定義で一意的に決まるので、柔軟性がない。

メモリー管理
======================================================================

TBW

入出力
======================================================================

TBW

文字列処理
======================================================================

TBW

関数オブジェクト
======================================================================

TBW

並行プログラミング
======================================================================

TBW

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
