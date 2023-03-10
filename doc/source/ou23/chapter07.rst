======================================================================
Chapter 07: Parallelism and Concurrency
======================================================================

`Chapter 07: Parallelism and Concurrency <https://changkun.de/modern-cpp/en-us/07-thread/>`__
に関するノート。

.. contents::

7.1 Basic of Parallelism
======================================================================

* ``std::thread`` が並行プログラミングの基礎となるものだ。
* 使用する際にはヘッダーファイル ``<thread>`` を含める。
* ID を取得する ``get_id()`` やスレッドに参集する ``join()`` など、基本的な操作
  が多数ある。

.. code:: c++

   #include <iostream>
   #include <thread>

   int main() {
       std::thread t([](){
           std::cout << "hello world." << std::endl;
       });
       t.join();
       return 0;
   }

7.2 Mutex and Critical Section
======================================================================

C++11 では排他制御に関連するクラス群が導入され、関連するすべての関数がヘッダー
ファイル ``<mutex>`` に記述されている。

C++11 で最も基本的な排他制御クラスは ``std::mutex`` だ。これをインスタンス化する
ことで排他制御ができる。メンバー関数 ``lock()``/``unlock()`` で施錠、解錠するこ
とができる。しかし、実際にはこれらを直接呼び出さない方がよい。C++11 では RAII 対
応したクラステンプレート ``std::lock_guard`` も用意されている。

.. code:: c++

   int v = 1;

   void critical_section(int change_v) {
       static std::mutex mtx;
       std::lock_guard<std::mutex> lock(mtx);

       // execute contention works
       v = change_v;

       // mtx will be released after leaving the scope
   }

オブジェクト ``lock`` がスタックに生成されるため、``critical_section()`` が正常
に返ろうが、途中で例外が発生しようが、スコープ終了時点でスタックのロールバックが
発生し、デストラクター経由で ``unlock()`` が自動的に呼び出されることに注意する。

``std::lock_guard`` よりも柔軟なのが ``std::unique_lock``
だ。``std::unique_lock`` オブジェクトは排他的所有権を持つ ``mutex`` オブジェクト
に対する施錠と解錠を管理する。他の ``unique_lock`` オブジェクトに ``mutex`` オブ
ジェクト所有権はあり得ない。したがって、並行プログラミングでは
``std::unique_lock`` を使用するのが望ましい。

``std::lock_guard`` は ``lock``/``unlock`` を明示的に呼び出すことができない。一
方 ``std::unique_lock`` は宣言後の任意の場所で呼び出すことができる。施錠の有効域
を狭め、より高い並行性を実現する。

条件変数 ``std::condition_variable::wait`` を使用する場合、引数には
``std::unique_lock`` を使用する必要がある。例コードが欲しい。

.. code:: c++

   int v = 1;

   void critical_section(int change_v) {
       static std::mutex mtx;
       std::unique_lock<std::mutex> lock(mtx);
       // do contention operations
       v = change_v;
       std::cout << v << std::endl;
       // release the lock
       lock.unlock();

       // during this period,
       // others are allowed to acquire v

       // start another group of contention operations
       // lock again
       lock.lock();
       v += 1;
       std::cout << v << std::endl;
   }

.. admonition:: 読者ノート

   果たしてそうか？

7.3 Future
======================================================================

C++11 で ``std::future`` が導入される以前は、以下のようなやり方が普通だった：

1. スレッド A を作る
2. スレッド A でタスク B を開始する
3. 準備ができたらイベントを送り、
4. その結果をグローバル変数に保存する
5. メイン機能のスレッド A は他のことをやっている
6. 結果が必要になったら、関数の実行結果を待つスレッドが呼び出される

``std::future`` はこの処理を簡略化する。非同期タスクの結果を取得するために利用す
る。スレッド同期の簡単な手段、すなわちバリアたり得ることが容易に想像できる。

本書の次のコード例では ``future`` オブジェクトをまともに生成するために
``packaged_task`` というものを用いているが、後でスレッド同期 (``result.wait()``)
を実現する。

.. code:: c++

   #include <iostream>
   #include <thread>
   #include <future>

   int main() {
       // pack a lambda expression that returns 7 into a std::packaged_task
       std::packaged_task<int()> task([](){return 7;});

       // get the future of task
       std::future<int> result = task.get_future();    // run task in a thread
       std::thread(std::move(task)).detach();
       std::cout << "waiting...";
       result.wait(); // block until future has arrived

       // output result
       std::cout << "done!" << std:: endl << "future result is "
                 << result.get() << std::endl;
       return 0;
   }

7.4 Condition Variable
======================================================================

条件変数 ``std::condition_variable`` はデッドロックを解決するために生まれ、排他
制御だけでは不十分な場合のために導入された。例えば、あるスレッドが実行を続けるた
めに、ある条件が真になるのを待つ必要があるという場合がある。デッドウェイトループ
は、他のすべてのスレッドがクリティカルセクションに入るのに失敗するため、条件が真
になったときにデッドロックが発生する可能性がある。
``std::condition_variable::notify_one()`` はスレッドを目覚めさせるために、
``std::condition_variable::notify_all()`` はすべてのスレッドに通知するために用い
られる。

本書のコード生産者消費者モデルの例。まずは ``main`` の先頭の変数宣言を調べる。こ
れらのオブジェクト、変数すべてを生産者と消費者のどちらも参照する。

.. code:: c++

   std::queue<int> produced_nums;
   std::mutex mtx;
   std::condition_variable cv;
   bool notified = false;  // notification sign

次に生産者スレッドのタスクを見る。本文の言うように ``unique_lock`` を用いる。
0.5 秒ふかしてからキューに値を押し込み、フラグをオンにして ``cv.notify_all`` を
呼び出すというものだ：

.. code:: c++

   auto producer = [&]() {
       for (int i = 0; ; i++) {
           std::this_thread::sleep_for(std::chrono::milliseconds(500));
           std::unique_lock<std::mutex> lock(mtx);
           std::cout << "producing " << i << std::endl;
           produced_nums.push(i);
           notified = true;
           cv.notify_all();
       }
   };

消費者スレッドタスク。消費者は複数ある。排他制御スコープが二つに分かれていること
に注意。生産物を消費した後のフラグの変更が怪しい。

.. code:: c++

   auto consumer = [&]() {
       for (;;) {
           std::unique_lock<std::mutex> lock(mtx);
           while (!notified) {  // avoid spurious wakeup
               cv.wait(lock);
           }
           // temporal unlock to allow producer produces more rather than
           // let consumer hold the lock until its consumed.
           lock.unlock();
           // consumer is slower
           std::this_thread::sleep_for(std::chrono::milliseconds(1000));
           lock.lock();
           if (!produced_nums.empty()) {
               std::cout << "consuming " << produced_nums.front() << std::endl;
               produced_nums.pop();
           }
           notified = false;
       }
   };

あとは生産者スレッド一つと消費者スレッド複数を生成して、その全てに対して ``join``
するコードが続く。

生産者では ``notify_one()`` を使用することもできるがそれは推められない。複数の消
費者が存在する場合、ここでの消費者の実装は単にロック保持を放棄しているが、他の消
費者がこのロックを奪い合うことが可能になり、複数消費者間の並行性をより活用するこ
とができるからだ。

とはいえ、実際には ``std::mutex`` の排他性から、複数の消費者が並列消費者キューで
中身を生成できることは期待できないので、やはりよりきめ細かい取り組み方が必要だ。

7.5 Atomic Operation and Memory Model
======================================================================

次のコードを実行すると、``b`` の値は何であるかという問題だ：

.. code:: c++

   #include <thread>
   #include <iostream>

   int main() {
       int a = 0;
       volatile int flag = 0;

       std::thread t1([&]() {
           while (flag != 1);

           int b = a;
           std::cout << "b = " << b << std::endl;
       });

       std::thread t2([&]() {
           a = 5;
           flag = 1;
       });

       t1.join();
       t2.join();
       return 0;
   }

結論から言うと ``b = 0`` の場合もあり得る。``a`` や ``flag`` については並列ス
レッドで読み書きを行うため、コード自体の挙動が未定義なのだ。競合が発生している。
また、読み書きの競合を無視しても、CPU の out-of-order 実行や、コンパイラーによる
命令の並べ替えの影響を受ける可能性がある。つまり ``flag = 1`` の後に ``a = 5``
を発生させる可能性がある。

.. admonition:: 読者ノート

   このコードを手許の環境で実行したら ``b = 5`` がいつでも出力される。
   ``volatile`` を付けても外しても。

用語をよく習得しておくこと。

Atomic Operation
----------------------------------------------------------------------

排他制御の実装には次の基本原則があるため、OS レベルの機能となる：

1. スレッド間の自動的な状態遷移、つまり「ロック」状態を提供する
2. 排他制御操作の間、操作される変数のメモリーがクリティカルセクションから隔離さ
   れていることを保証する

この同期条件は強力で、最終的に CPU 命令にコンパイルされるとき、多くの命令のよう
に振る舞うことになる。不可分操作しか必要としない（中間状態を必要としない）変数に
はこれは厳しいようだ。

現代の CPU アーキテクチャーでは、CPU 命令レベルでの不可分操作が提供されていると
いうことを理解する必要がある。したがって、C++11 のマルチスレッド共有変数の読み書
きでは、``std::atomic`` の導入により、不可分型をインスタンス化することになる。不
可分型の読み書きは、命令群から単一の CPU 命令へ最小化される。例：

.. code:: c++

   std::atomic<int> counter;

また、整数や浮動小数点数の不可分型に対応した基本的な数値演算関数が用意されている：

.. code:: c++

   #include <atomic>
   #include <thread>
   #include <iostream>

   std::atomic<int> count = {0};

   int main() {
       std::thread t1([](){
           count.fetch_add(1);
       });
       std::thread t2([](){
           count++;        // identical to fetch_add
           count += 1;     // identical to fetch_add
       });
       t1.join();
       t2.join();
       std::cout << count << std::endl;
       return 0;
   }

``atomic<int>::operator++()`` も ``atomic<int>::operator+=(1)`` も
``atomic<int>::fetch_add(1)`` と同じだと言っている。

不可分操作を提供できない操作もある。型が ``T`` 不可分操作をサポートするかどうか
を確認するには、``std::atomic<T>::is_lock_free`` をチェックすればいい。

.. code:: c++

   #include <atomic>
   #include <iostream>

   struct A {
       float x;
       int y;
       long long z;
   };

   int main() {
       std::atomic<A> a;
       std::cout << std::boolalpha << a.is_lock_free() << std::endl;
       return 0;
   }

.. admonition:: 読者ノート

   このコードは最初、手許の g++ でコンパイルエラーとなった。調べるとリンクオプ
   ション ``-latomic`` が要るのだった。

Consistency Model
----------------------------------------------------------------------

複数のスレッドが並列に実行されるシステムはおおよそ分散システムと見なすことができ
る。分散システムでは、通信やローカル操作でさえも時間を消費し、信頼性の低い通信も
発生する。

複数のスレッドにまたがる変数 ``v`` の操作を不可分、つまり ``v`` を操作するどのス
レッドも他のスレッドと並行して ``v`` の変化を認識するように強制すると、変数
``v`` に対して逐次実行として振る舞うプログラムは、マルチスレッドの導入による効率
化の恩恵を受けられない。これを適切に高速化するためには、プロセス間同期条件を弱め
る。

原理的には、各スレッドはクラスターノード一つに対応することができ、スレッド間の通
信はクラスターノード間の通信とほぼ等価だ。プロセス間の同期条件を弱めるために、以
下で述べられる四種の異なる整合性モデルを考慮する。

Linear Consistency
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

強い整合性、不可分整合性とも呼ばれる。ある読み出し操作が特定のデータの最新の書き
込みを読み出し、操作の順序がグローバル時計下の順序とすべてのスレッドで一致するこ
とを必要とする。

.. code:: text

           x.store(1)      x.load()
   T1 ---------+----------------+------>


   T2 -------------------+------------->
                   x.store(2)

この場合、スレッド ``T1``, ``T2`` による ``x`` への二度の書き込み操作は不可分で
あり、 ``x.store(1)`` は ``x.store(2)`` の前に厳密に起こり、``x.store(2)`` は
``x.load()`` の前に厳密に起こる。線形一貫性のための大域時計の要件は達成するのが
難しいので、この条件よりも弱い条件で他の一貫性のためのアルゴリズムを研究し続ける
理由は注目に値する。

Sequential Consistency
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ここでも、どのような読み出し操作でも、最後に書き込まれたデータを読み出すことを要
求する。ただし大域時計の順序との一貫性は要求しない。

.. code:: text

           x.store(1)  x.store(3)   x.load()
   T1 ---------+-----------+----------+----->


   T2 ---------------+---------------------->
                 x.store(2)

または

.. code:: text

           x.store(1)  x.store(3)   x.load()
   T1 ---------+-----------+----------+----->


   T2 ------+------------------------------->
         x.store(2)

逐次整合性の要求下では、``x.load()`` は最終的に書き込まれたデータを読まなければ
ならない。``T2`` の ``x.store(2)`` が ``x.store(3)`` より前に発生するならば、
``x.store(1)`` には何の保証もないことになる。

因果的整合性
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

要件はさらに緩和され、因果関係のある操作の順序しか保証されず、因果関係のない操作
の順序は要求されない。

.. code:: text

         a = 1      b = 2
   T1 ----+-----------+---------------------------->


   T2 ------+--------------------+--------+-------->
         x.store(3)         c = a + b    y.load()

または

.. code:: text

         a = 1      b = 2
   T1 ----+-----------+---------------------------->


   T2 ------+--------------------+--------+-------->
         x.store(3)          y.load()   c = a + b

または

.. code:: text

        b = 2       a = 1
   T1 ----+-----------+---------------------------->


   T2 ------+--------------------+--------+-------->
         y.load()            c = a + b  x.store(3)

上に挙げたどの三つの例でも工程全体で

* ``c`` だけが ``a`` と ``b`` に依存関係を持ち、
* ``x`` と ``y`` はこの例では関連性がない

ため、すべて因果的整合性がある（実際の場面では、``x`` と ``y`` が関連していない
と判断するには何らかの根拠が要る）。

Final Consistency
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

これが最も弱い整合性要件だ。操作が将来のある時点で観察されることの保証しかせず、
それが観察される時間を要求しない。よって、例えば、操作が観測される時間が常に有界
であることを指定するなどして、この条件を少し厳しくすることも可能だ。

.. code:: text

       x.store(3)  x.store(4)
   T1 ----+-----------+-------------------------------------------->


   T2 ---------+------------+--------------------+--------+-------->
            x.read      x.read()           x.read()   x.read()

上記の場合、``x`` の初期値を ``0`` とすると、``T2`` における四度の ``x.read()``
の結果は以下の場合が考えられ、これに限定されない：

.. csv-table::
   :delim: |
   :header: ``x.read()``,状況
   :widths: auto

   3, 4, 4, 4 | ``x`` への書き込み動作がただちに確認された
   0, 3, 3, 4 | ``x`` への書き込み動作の観測時間に遅延がある
   0, 0, 0, 4 | 最後の読み出しで最終的な ``x`` の値を読み出したが、それまでの変化は観察されなかった
   0, 0, 0, 0 | ``x`` への書き込み動作は現在の時間帯では観測されない（しかし ``x == 4`` という状況は将来のある時点で観測される可能性がある）

Memory Orders
----------------------------------------------------------------------

さまざまな強度要件整合性を実現するために、C++11 では不可分操作のためのメモリー順
序を六種類定義している。オプション ``std::memory_order`` は複数スレッド間の同期
モデルを四つ表現する。

Relaxed model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

このモデルでは単一スレッド内の不可分操作は順次実行される。命令の並び替えは許され
ないが、異なるスレッド間の不可分操作の順序は任意である。
``std::memory_order_relaxed`` で指定。例：

.. code:: c++

   std::atomic<int> counter = {0};
   std::vector<std::thread> vt;
   for (int i = 0; i < 100; ++i) {
       vt.emplace_back([&](){
           counter.fetch_add(1, std::memory_order_relaxed);
       });
   }

   for (auto& t : vt) {
       t.join();
   }
   std::cout << "current counter:" << counter << std::endl;

.. admonition:: 読者ノート

   * ``counter.fetch_add(1)`` はカウンターを 1 増やすのをクリティカルセクション
     で行うものと思ってよい。
   * ``v.emplace_back(args)`` は ``v.push_back(T(args))`` のようなもの。
   * 実行結果は ``100`` が出力されるはずだ。手許の環境でそうなる。

Release/consumption model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

このモデルでは、あるスレッドが値を変更する必要があるときに、別のスレッドがその値
に対する特定の操作に依存するようになる場合、つまり、後者が前者に依存するようにな
る場合、プロセス間の操作順序を制限するようにする。

具体的には、スレッド A が ``x`` への書き込み三つを完了し、スレッド B が ``x`` へ
の最初の二つの書き込みとは無関係に、``x`` への書き込みのうち三番目だけに依存する
場合、A が ``x.release()`` を開始すると（ここで ``std::memory_order_release`` を
使う）、オプション ``std::memory_order_consume`` によって、B は ``x.load()`` が
呼ばれたときに A 内の ``x`` への三度目の書き込みを観測する。

.. code:: c++

   // initialize as nullptr to prevent consumer load a dangling pointer
   std::atomic<int*> ptr(nullptr);

   int v;
   std::thread producer([&]() {
       int* p = new int(42);
       v = 1024;
       ptr.store(p, std::memory_order_release);
   });

   std::thread consumer([&]() {
       int* p;
       while(!(p = ptr.load(std::memory_order_consume)));

       std::cout << "*p: " << *p << std::endl;
       std::cout << "v: " << v << std::endl;
   });

   producer.join();
   consumer.join();

このコードを実行すると ``*p: 42`` と ``v: 1024`` が出力される。

Release/Acquire model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

このモデルでは、``std::memory_order_release`` と ``std::memory_order_acquire``
の間のタイミングを指定することで、異なるスレッド間の不可分操作の順序制限をさらに
厳しくすることができる。解放操作の前の書き込み操作のすべてが他のどのスレッドから
も見える。

``std::memory_order_release`` は、解放操作後にそれ以前の書き込みが発生しないこと
を保証する（後方バリア）。

``std::memory_order_acquire`` は、取得操作後の読み取りまたは書き込みが獲得操作の
前に発生しないようにする（前進バリア）。

オプションの ``std::memory_order_acq_rel`` はこの二つを組み合わせて、現在のス
レッドのメモリーへの読み書きが、この操作の前後で順序が変わって交差しないように、
メモリーバリアを一意に決定する。

.. code:: c++

   std::vector<int> v;
   std::atomic<int> flag = {0};

   std::thread release([&]() {
       v.push_back(42);
       flag.store(1, std::memory_order_release);
   });

   std::thread acqrel([&]() {
       int expected = 1; // must before compare_exchange_strong
       while(!flag.compare_exchange_strong(expected, 2, std::memory_order_acq_rel))
           expected = 1; // must after compare_exchange_strong
       // flag has changed to 2
   });
   std::thread acquire([&]() {
       while(flag.load(std::memory_order_acquire) < 2);

       std::cout << v[0] << std::endl; // must be 42
   });

   release.join();
   acqrel.join();
   acquire.join();

今回 ``compare_exchange_strong`` という比較・交換プリミティブを使用するが、これ
には ``compare_exchange_weak`` という弱バージョンがあり、交換が成功しても失敗を
返すことができる。その理由は、一部のプラットフォームで偽失敗が発生するためで、具
体的には、CPU がコンテキストスイッチを行った際に、別のスレッドが同じアドレスを
ロードすることによって不整合が発生する。さらに、``compare_exchange_strong`` の性
能は ``compare_exchange_weak`` より若干劣るかもしれないが、ほとんどの場
合、``compare_exchange_weak`` はその使用の複雑さを考えると、推奨されない。

この例では ``flag`` と ``expected`` の値が一定の条件で exchange されるというのだ
ろう。

Sequential Consistent Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

このモデルでは、不可分操作は順序整合性を満たすが、その分、性能上の損失が発生し得
る。これを ``std::memory_order_seq_cst`` で明示的に指定する。

.. code:: c++

   std::atomic<int> counter = {0};
   std::vector<std::thread> vt;
   for (int i = 0; i < 100; ++i) {
       vt.emplace_back([&](){
           counter.fetch_add(1, std::memory_order_seq_cst);
       });
   }

   for (auto& t : vt) {
       t.join();
   }
   std::cout << "current counter:" << counter << std::endl;

この例は、最初の例で不可分演算のメモリー順序を ``memory_order_seq_cst`` に変更した
だけだ。出力はもちろん ``100`` だ。この二種類の性能差を測定するといい。

Conclusion
======================================================================

* 並行プログラミングの重要なツール

  * ``std::thread``
  * ``std::mutex``
  * ``std::future``
* メモリーモデル

Exercises
======================================================================

1. ``ThreadPool`` を実装しろ。コンストラクター、メソッド ``enqueue``, etc.
2. ``std::atomic<bool>`` を使って排他制御を実装しろ。

Further Readings
======================================================================

`C++ Concurrency in Action <https://www.amazon.com/dp/1617294691/ref=cm_sw_em_r_mt_dp_U_siEmDbRMMF960>`__
    専門書
`Thread document <https://en.cppreference.com/w/cpp/thread>`__
    本章が要点を整理する元になった機能群。
Herlihy, M. P. & Wing, J. M. (1990). Linearizability: a correctness condition for concurrent objects. ACM Transactions on Programming Languages and Systems, 12(3), 463-492. <https://doi.org/10.1145/78969.78972>
    何かの論文。
