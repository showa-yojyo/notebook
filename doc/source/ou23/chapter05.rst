======================================================================
Chapter 05: Smart Pointers and Memory Management
======================================================================

`Chapter 05 Smart Pointers and Memory Management <https://changkun.de/modern-cpp/en-us/05-pointers/>`__
についてのノート。

.. contents::

5.1 RAII and Reference Counting
======================================================================

* 参照カウンターの概念をおさらいしておくこと。
* RAII の格言を忘れぬこと。

従来の C++ ではリソースを解放するために ``new`` と ``delete`` を使うことを忘れな
いようにする必要があった。C++11 で参照カウンターを利用したスマートポインターの概
念が導入され、プログラマーが手動で解放することを気にする必要がなくなった。ヘッ
ダーファイル ``<memory>`` をインクルードしてスマートポインター各種を用いる。

参照カウンターはガベージコレクションの手法よりも、不用オブジェクトを早く回収する
ことができ、再利用処理中に長い待ち時間が発生することはない。資源の寿命をより明確
に示す。

5.2 ``std::shared_ptr``
======================================================================

クラステンプレート ``std::shared_ptr`` がいちばん普通の参照カウンター方式スマー
トポインターであり、カウンターがゼロになると管理下の資源を解放する。

関数テンプレート ``std::make_shared`` を使えば、明示的に ``new`` を使う必要がな
くなる。``std::make_shared`` は指定引数からオブジェクトを生成、確保する。そし
て、このオブジェクト型の ``std::shared_ptr`` オブジェクトを返す。

.. code:: c++

   auto pointer = std::make_shared<int>(10);

``std::shared_ptr`` には次のようなメソッドがある：

.. csv-table::
   :delim: |
   :header: メソッド,操作
   :widths: auto

   ``get()`` | 生のポインターを得る
   ``reset()`` | 参照カウントを減らす
   ``use_count()`` | 参照カウントを見る

コード例で注目したいのは：

* スマートポインターの宣言と初期化に ``auto`` を常に使うのが良い。
* コピーコンストラクターでカウンターが増える。この例では関数 ``foo`` の呼び出し
  が値渡しであるので、コピーが発動する。
* ``reset()`` を呼び出したスマートポインターの生のポインターは ``nullptr`` とな
  る。かつ、共有関係にあるスマートポインターすべての参照カウンターが減る。

5.3 ``std::unique_ptr``
======================================================================

スマートポインター ``std::unique_ptr`` は排他的で、同じ生ポインターを共有するよ
うな他のスマートポインターの存在しないことを保証する。つまりコピーすることができ
ない。しかし、``std::move`` を使って、他の ``unique_ptr`` に移すことなどは可能で
あることに注意。

``std::make_shared`` の ``std::unique_ptr`` 版は C++11 では存在しない。

5.4 ``std::weak_ptr``
======================================================================

``std::shared_ptr`` は次のような使い方をすると解放漏れが生じる。デストラクターを
実装して、デバッガーでステップ実行すればわかる：

.. code:: c++

   class A;
   class B;

   class A {
   public:
       std::shared_ptr<B> pointer;
   };

   class B {
   public:
       std::shared_ptr<A> pointer;
   };

   auto a = std::make_shared<A>();
   auto b = std::make_shared<B>();
   a->pointer = b;
   b->pointer = a;

ここで ``std::weak_ptr`` を採用する。これは参照カウンターを増やさない。
``A::pointer`` または ``B::pointer`` の少なくとも一方の ``shared_ptr`` を
``weak_ptr`` にすれば ``A`` と ``B`` 双方のデストラクターが作動する。

``std::weak_ptr`` には ``operator*`` や ``operator->`` が実装されていないため、
生の資源を操作することはできない。

``std::weak_ptr`` は ``std::shared_ptr`` が存在するかどうかをチェックすることが
できる。

``std::weak_ptr::expired()`` は資源が解放されていない場合に限り ``false`` を返
す。

また、元のオブジェクトを指す ``std::shared_ptr`` を取得する目的で使用することも
できる。

``std::weak_ptr::lock()`` は、資源が解放されていない場合に限り、元の
``std::shared_ptr`` を返す。

.. admonition:: 読者ノート

   本文は ``lock`` しか言及していないが、``owner_before`` というメソッドもある。
   これらを使って本文の例を書き換えたものを考えたい。

   `std::weak_ptr - cppreference.com <https://en.cppreference.com/w/cpp/memory/weak_ptr>`__

Conclusion
======================================================================

多くの言語で一般的な技術であるスマートポインターだが、C++ ではこの技術が最近導入
された。

Further Readings
======================================================================

`c++ - Why does C++11 have make_shared but not make_unique - Stack Overflow <https://stackoverflow.com/questions/12580432/why-does-c11-have-make-shared-but-not-make-unique>`__
  C++14 から ``std::make_unique`` が利用可能だ。
