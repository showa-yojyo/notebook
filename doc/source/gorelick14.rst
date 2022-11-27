======================================================================
ハイパフォーマンス Python 読書ノート
======================================================================

開発環境の揃わない旅の途中に読んだので、特別なツールの挙動を確認するなどの本質的
な作業が一部残っているが、ノートをとっておく。本書は Python 2 ベースでパフォーマ
ンスを評価しているが、私は Python 3 で確認しながら読み進めた。

:著者: Micha Gorelick, Ian Ozsvald
:訳者: 相川愛三
:出版社: オライリー・ジャパン
:ISBN: 978-4-87311-740-9
:関連 URL: `紹介ページ <https://www.oreilly.co.jp/books/9784873117409/>`__

.. contents:: ノート目次

訳者まえがき
======================================================================

* 本書は単なるテクニック本とは違う。
* 本書で中心的に紹介している各技術はかなり成熟していて、今後も陳腐化することはな
  いはずだ。この知識は長く使えると思う。
* 原書のクセの強い英語についての具体的な愚痴。

まえがき
======================================================================

* <Python は、ラピッド開発、実環境へのデプロイ、スケーラブルなシステム作りに適し
  ています>
* 本書は主に CPU バウンドの問題を扱う。データ転送、メモリバウンドの問題も触れ
  る。
* 本書は中級者～上級者 Python プログラマー向け。
* 本書が提供するトピック一覧で目を引いたもの：

  * コンパイラと JIT 計算
  * 並行処理
  * ``multiprocessing``
  * クラスタコンピューティング
  * RAM の節約

* Python 2.7 は 2020 年に引退する。
* 本書のライセンスは CC BY-NC-ND 3.0 に基づく。

  **High Performance Python** by Micha Gorelick and Ian Ozsvald (O'Reilly).
  Copyright 2014 Micha Gorelick and Ian Ozsvald, 978-1-449-36159-4.

1 章 高性能な Python を理解する
======================================================================

Python というよりは計算機の基礎を理解するための章だ。

各章の冒頭には、読者が読了後に理解したはずの事項を列挙してある。本ノートではそれ
らの問いに答えていこうと思う。

* コンピュータアーキテクチャの構成要素とは何か？

  1) 演算装置
  2) 記憶装置
  3) 両者の接続装置

* 一般に、構成要素にはどんなものがあるか？

  1) CPU, GPU
  2) ハードディスク、SSD, RAM, L1/L2 キャッシュ（ただしキャッシュは CPU 内部にあ
     る）
  3) フロントサイドバス、バックサイドバス、外部バス

* Python は下層のコンピュータアーキテクチャをどのように抽象化しているのか？

  配列のメモリ確保、配置、解放、データの CPU への転送順というような
  計算機の低水準要素を、プログラマーが意識せずに済むように抽象化している。

* Python のコードを最適化するうえでの障壁は何か？

  * ベクトル化をすぐに適用できない
  * 次の計算に用いるデータをキャッシュに格納しておくようにする手法が適用しにくい
  * 動的型付け言語であることからくる最適化機会の損失全般
  * 並列処理化のときの GIL: コア数にかかわらず一度に一つの命令しか実行しない

* 性能問題にはどんなものがあるか？

  * 計算量。単位時間あたりにどれだけ多くの計算を実行できるか。
  * 記憶量。どれだけ多くのデータをどれだけ記憶できるか。
  * 処理量。データをどれだけ速く入出力できるか。
  * 転送量。データをどれだけ速く転送できるか。

----

ここからは GitHub リポジトリーにあるサンプルプログラムの分析ノート。章ごとにサブ
ディレクトリーが設けられていて、著者が執筆時に試したはずのコード群やプロファイル
結果が管理されている。

当ノートでも可能な限りコードを実行していく。序盤から当たり前のようにサードパー
ティー製パッケージを必要とするものが出てくるが、この章はまだ素の環境で再現が可能
だ。

* :file:`check_prime.py`: このロジックで素数を判定できたらたいしたものだ。
* :file:`reducing_operations.py`: ループを早めに抜けることの重要性。

  * ここでの ``timeit`` モジュールの応用法は本書を通じて用いられる。
  * この手の判定は ``return needle in haystack`` と書くのが自然だ。
    ここに書いてある ``search_fast()`` よりも高速だ。

2 章 ボトルネック発見のためのプロファイリング
======================================================================

本章はしっかり理解したほうがいい。このジュリア集合のコードをきちんと書いて測定す
ること。コードは著者のリポジトリーにあるのだが、あえて写経してもそのタイプ時間以
外には損はないと思われる。

本章冒頭の問いに答えてみよう。

* コード上のスピードと RAM のボトルネックをどのように特定するのか？

  一言で言えば「プロファイリングをする」こと。

* CPU とメモリの使用量をどのように測定するのか？

  いろいろなツールがある。実行時間の測定には次に挙げるものが：

  * IPython の ``%timeit`` コマンド
  * Python 標準の ``time``, ``timeit`` モジュール
  * Python 標準の ``cProfile`` モジュール

    * RunSnakeRun という補助ツールがある。ビジュアル。

  * Unix の :command:`time` コマンド（ただし組み込みでないほう）

    * GNU :command:`time` というものだろう。 Cygwin でも存在すると思われるが、ど
      のパッケージに含まれているのか不明。それゆえ入手できずじまい。

  * ``line_profiler``

    * これは入手が若干面倒そうだ。
      ``error: Microsoft Visual C++ 14.0 is required.``

  * :command:`perf stat`

  メモリの測定については次に挙げるものが便利だ：

  * ``heapy``: TODO: ``guppy`` インストール

  * ``dowser``: これは :command:`pip install dowser` で利用可能になる。
    依存パッケージ CherryPy も同時にインストールされる。
    ただし、Python 3 対応がなされていない。
    本書を理解するために勝手に :command:`2to3` しておく。

  * ``memory_profiler``:
    これは :command:`pip install memory_profiler` で容易に利用可能になる。コマン
    ドラインツール :command:`mprof` および IPython 用コマンド ``%memit`` を含む。

* プロファイリングの深さをどのように選ぶのか？

  実行時間測定結果を分析して、コストの高い場所を特定する？

* 長時間実行するアプリケーションをどのようにプロファイリングするのか？

  アプリケーションの動作に依存してメモリの挙動が異なるのならば、インタラクティブ
  に確認するのが望ましい。本書では ``dowser`` というサービスを稼働させて、ブラウ
  ザーから確認するような手法を紹介している。

* CPython の内部では何が起こっているのか？

  CPython 仮想マシンの内部で実行される低水準バイトコードを確認したい。それには
  Python の ``dis`` モジュールの機能を利用する。``dis.dis(python_code)`` とする
  と、アセンブリのようなテキストが出力される。

* 性能をチューニングしながら、どのようにコードの正しさを維持するのか？

  チューニング中も単体テストを活用する。また、テストがすべてのコードをカバーして
  いることを確認するために :file:`coverage.py` を使う。

本章で指摘しているコード改善点をまとめておく。

* ``p and q`` のような条件判定では ``p`` が ``q`` よりも早く評価されるように選
  ぶ。

  述語を複数並べて論理積を判定する場合には、これらの述語を判定コストの小さい順に
  左から並べるのが定石。他の言語でも同様。

* Python では ``n += 1`` のようなコードさえ遅い。

本章で紹介されている技法のうち、すぐにでも採り入れられるものをまとめておく。

* 時間測定を自動化するデコレーター。このコードは手許に保存しても丸暗記してもよ
  い。
* 標準モジュール ``timeit`` をコマンドラインから実行する。

  .. code:: console

     bash$ python -m timeit -n 5 -r 5 -s "COMMANDS"

* Unix の :command:`time` コマンド。組み込み版を呼ばぬよう注意すること。

  .. code:: console

     bash$ /usr/bin/time -p python SCRIPT
     bash$ /usr/bin/time --verbose -p python SCRIPT

* 標準モジュール ``cProfile`` をコマンドラインから実行する。

  .. code:: console

     bash$ python -m cProfile -s cumulative SCRIPT

  あるいは IPython で :command:`%run -p` コマンドを実行する。:command:`%prun` で
  もいい。

  .. code:: ipython

     In [1]: %run -p -s cumulative SCRIPT

  統計情報をファイルに書き出して、標準モジュール ``pstats`` の機能で分析する。

  .. code:: console

     bash$ python -m cProfile -s profile.stats SCRIPT

  IPython ならばこうする。ダンプファイルは IPython セッションで分析するのが便利
  なので、こちらのほうがいいか。

  .. code:: ipython

     In [1]: %run -p -D profile.stats cpu_profiling/julia1_nopil.py

     In [2]: from pstats import Stats
     In [3]: p = Stats('profile.stats')
     In [4]: p.sort_stats('cumulative')
     In [5]: p.print_stats()
     In [6]: p.print_callers()
     In [7]: p.print_callees()

  このノートには記さないが、統計情報出力が横長過ぎて驚く。

* 簡単なコード片ならば IPython の ``%timeit`` コマンドが手軽に使える。

  .. code:: ipython

     In [1]: %timeit CODE

----

以下、GitHub リポジトリーにあるリソースの分析。この章に対応するディレクトリーに
ある :file:`chapter_recipe.txt` のコードを追体験するのがいい。他の章にもこういう
のを作ればよかったのに。

* 共通

  * すべて Python 2 コードなので、手動で Python 3 化しないと私の環境では動かせな
    い。
  * ``if __name__ == __main__:`` を含むスクリプトは冒頭に
    ``#!/usr/bin/env python`` と入れてほしい。
  * 私の環境では計算時間が 3 倍弱かかる。

* :file:`cpu_profiling/`: GNU :command:`time` での測定が残。
* :file:`decorator_time/`: 見るべきはデコレーター関数 ``timefn()`` だ。
* :file:`dowser/`: ブラウザーでリアルタイムに観察する。

  * 関数 ``launch_memory_usage_server()`` でそれ周りのコードは完結している。これ
    をジュリア集合の計算直前に呼び出して、CherryPy サーバーを走らせるとのこと。
  * 自分で <http://localhost:8080/> のページを表示する。``builtins.list`` の
    TRACE リンク先を見ればよい。

* :file:`guppy/`: TODO: Install ``guppy``
* :file:`line_profiler/`: TODO: Install :file:`kernprof.py`
* :file:`memory_profiler/`: どうやらメモリ量の計測は時間がかかる傾向がある。

  * コマンド :command:`mprof run` を使うときのコマンドラインは次のようにする：

    .. code:: console

       bash$ python D:/Miniconda3/Scripts/mprof run julia1_memoryprofiler.py

    * その後にコマンド :command:`mprof plot` でグラフを描く。

* :file:`noop_profile_decorator/`: 本文の何もしない ``@profile`` デコレーターの
  記述を参照。
* :file:`visualise_nonconvergence/`: このプロットはダメだ。コードをいじって点列
  がほんとうに発散することを見るといい。

3 章 リストとタプル
======================================================================

本章は「小手先のテクニック」に属する。この本に手が伸びるプログラマーならば、ここ
に述べられていることはすでに理解しているはず。

本章冒頭の問いに答えてみよう。

* リストとタプルの長所は？

  どちらもデータ構造としては配列であるので、その長所を有する。

  格納要素へのランダムアクセスが可能であること。つまり特定位置にある要素へ定数時
  間でアクセスできる。

* リストとタプルの探索の計算オーダーは？

  どちらも線形時間だ。ただしソート済みならば二分探索による対数時間。

* その計算オーダーの理由は？

  線形時間である理由は、格納要素が単純に配列されているからもっとも単純な探索アル
  ゴリズムである線形探索しか使えないことによる。

* リストとタプルの違いは？

  前者は動的であり、後者は静的であると表現できる。特に mutable という視点で見る
  と両者の違いが区別がつく。タプルはいったん生成するとその時点で内容が固定化され
  るので、メモリもそれ以上消費しない。

* リストに追加するときの動作は？

  C++ 標準の ``std::vector`` のそれと同じ議論が成り立つ。メモリの再確保および格
  納要素（参照型だが）のコピーという高価な処理が発生する。本書の図 3-3 は頭に叩
  き込んでおく（細かいサイズは覚えなくていい）。

* リストとタプルを使うのが適当なときは？

  * リストは構成が変更されるときに用いる。 「プログラミング言語」だの「ある人物
    の身体測定値各種」だの、内容が常に更新されていたり、値が追加される可能性が高
    いものを表現するのに向いている。

  * タプルはそうでないときに用いる。データが変化しない「素数の最初の n 個」だの
    「ある人物の誕生日および生誕地」だのを表現するのに向いている。

----

以下、GitHub リポジトリーにあるリソースの分析。

* 本編とは関係ない感想だが :command:`2to3` は ``range(...)`` を
  ``list(range(...))`` に変換する。
* :file:`binary_search.py`: 二分検索のアルゴリズム実装例。C++ の
  ``std::upper_bound()`` 風。
* :file:`binary_vs_linear.py`: 線形検索アルゴリズム実装例とその時間測定コード。

  * ソート済みのものをソートすることに注意したい。

* :file:`bisect_example.py`: ``bisect.insort()`` および ``bisect.bisect_left()``
  の使用例。
* :file:`linear_search.py`: 線形検索アルゴリズム実装例とその時間測定コード。明ら
  かに二分検索より遅いことが体感でわかる。PC のファンもうるさくなる。

4 章 辞書と集合
======================================================================

本章は「小手先のテクニック」に属する。

本章冒頭の問いに答えてみよう。

* 辞書と集合の長所は？

  * 探索のコストが定数時間
  * 挿入のコストが定数時間

* 辞書と集合の共通点は？

  参照可能で他と重複しない要素を格納するオブジェクトであること。参照に用いるオブ
  ジェクト（キー）の型がハッシュ可能なデータ型であること。

* 辞書を使うときのオーバーヘッドは？

  ハッシュ値の衝突時に発生する新しい格納位置を決定する計算。

* 辞書の性能を向上させる方法は？

  * ハッシュの取りうる値の範囲を広げて、プローブ計算の発生を抑制する。
  * ハッシュ関数のエントロピーを大きくする。

* Python が名前空間を管理するためにどのように辞書を使っているか？

  1) ローカル変数を ``locals()`` を検索する。
  2) そこになければ ``globals()`` を検索する。
  3) そこにもなければ ``__builtin__.locals()`` を検索する。

以下雑感など。

* ある型が :dfn:`ハッシュ可能` であるとは、次のものを実装している型であるときを
  いう：

  1) ``__hash__()`` と
  2) ``__eq__()`` または ``__cmp__()`` のいずれか一方（または両方）

  前者はキーのハッシュ値を得るのに、後者は二つのハッシュ値を比較するのに用いられ
  る。

* ところで Python の辞書と集合は C++ での ``std::hash_map`` と ``std::hash_set``
  にそれぞれ相当するのだろうか。

* ハッシュから要素を削除するときの振る舞いは最初の説明だけからはわからない。本書
  の例でいうと、Rome を削除してから Barcelona を削除（というか検索）するときの詳
  細を説明できるようにしたい。

  1) 要素追加時に衝突があれば、そのことをバケットに記憶させておくか、
  2) 要素削除時にキーを prove させ続けて、可能性のあるバケットを全部見るのか、
  3) それでもない方法なのか。

  答え：<バケットが空であるが、ハッシュ値の衝突時に考慮すべき値が続いていること
  を示す特別な値> を削除済みバケットに書き込むことで対処する。

* ハッシュ表成長の 2/3 ルールを知らないと、与えられた要素数を収容する辞書のサイ
  ズが見積もれない。
* ハッシュ関数のエントロピーの式中の確率 :math:`p(i)` の意味がわからない。ハッ
  シュ値が :math:`i` になる確率といっているが、ハッシュ値全体の集合がわからない
  と。

  いずれにせよ、この :math:`S` の値を最大にする確率関数を導くハッシュ関数を
  **理想ハッシュ関数** という。

----

以下、GitHub リポジトリーにあるリソースの分析。

* :file:`custom_vs_default_hash.py`: 自作 ``Point`` クラスにどのようにハッシュ関
  数を実装すべきかを示すスクリプト。上のノート参照。
* :file:`dict_probing.py`: ハッシュの基礎理論を説明するためのスクリプト。

  * 関数 ``sample_probe()`` 内の ``format`` が動かないかもしれない。 ForceHash
    オブジェクトを ``{: >10}`` に渡せないようだ？この右揃え指定を外すと出力でき
    る：

    .. code-block:: text

       First 10 samples for hash 0b00000111: [7, 3, 0, 1, 6, 7, 4, 5, 2, 3]
       First 10 samples for hash 0b11100111: [7, 3, 7, 4, 5, 2, 3, 0, 1, 6]
       First 10 samples for hash 0b01110111: [7, 3, 3, 0, 1, 6, 7, 4, 5, 2]
       First 10 samples for hash 0b01110001: [1, 7, 7, 4, 5, 2, 3, 0, 1, 6]
       First 10 samples for hash 0b01110000: [0, 1, 1, 6, 7, 4, 5, 2, 3, 0]

* :file:`naive_hash_function.py`: 粗雑なハッシュ関数実装例。
* :file:`namespace.py`: インポートされた関数の呼び出し効率について。

  .. code:: ipython

     In [45]: import namespace

     In [47]: %timeit namespace.test1(123456)
     975 ns ± 5.18 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

     In [48]: %timeit namespace.test2(123456)
     828 ns ± 3.38 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

     In [49]: %timeit namespace.test3(123456)
     856 ns ± 2.58 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

* :file:`namespace_loop.py`: 上と同様。

  .. code:: ipython

     In [50]: import namespace_loop

     In [51]: %timeit namespace_loop.tight_loop_slow(10000)
     5.67 ms ± 38.7 μs per loop (mean ± std. dev. of 7 runs, 100 loops each)

     In [52]: %timeit namespace_loop.tight_loop_fast(10000)
     5.34 ms ± 35 μs per loop (mean ± std. dev. of 7 runs, 100 loops each)

* :file:`timing_hash_function.py`: アルファベット二文字からなる全文字列の集合か
  ら特定の文字列を検索する。ただしハッシュ関数を二通り定義し、それぞれの検索効率
  を計測する。
* :file:`unique_lookup.py`: 電話番号検索のリスト対集合。本文の記述参照。

5 章 イテレータとジェネレータ
======================================================================

本章は「小手先のテクニック」に属する。

本章冒頭の問いに答えてみよう。

* ジェネレータを使うと、どのようにメモリを節約できるか？

  ジェネレータを使わないとすると、リストや辞書型のオブジェクトが別に必要になる。
  そのときは、リスト自身の生成や要素を保持するのに必要となるメモリの確保が発生す
  る。

* ジェネレータを使うべき場面はどんなときか？

  1) メモリに乗り切らないようなデータを反復するときなど。
  2) データ生成とデータ処理を切り分けるときなど（前者をジェネレータが担当する）。

* 複雑なジェネレータの処理を定義するために、どのように ``itertools`` を使うの
  か？

  与えられた問題を解決するのに役立つ関数を ``itertools`` から見つけて、場合に
  よっては関数を複数組み合わせてジェネレータを定義する。

* 遅延評価が便利な場面と、そうでないときはいつか？

  遅延評価では、明示的に要求された計算のみが実行される傾向がある。つまり、不必要
  な計算が実行されないことが期待できる。

  そうでないとき：ワンパス or オンライン処理

----

以下雑感。

* オンライン平均アルゴリズムは知らなかった。ここでは標準偏差を求めて、データ中の
  最大値が値 :math:`\mu + 3 \sigma` を超えるデータがあればその日のデータを異常と
  みなすという応用だ。
* Python 3 では使えないコードがあるので、読者は内包表記に直したい：

  * ``ifilter(None, X)`` は ``(x for x in X if x)`` の意。
  * ``imap(check_anomaly, data_day)`` は ``(check_anomaly(x) for x in
    data_day)`` の意。

  とにかくジェネレーターを駆使して遅延評価に持ち込めていればよい。

----

以下、GitHub リポジトリーにあるリソースの分析。

* :file:`fibonacci.py`: ある値以下の Fibonacci 数を勘定する実装が 3 個ある。これ
  までの知識をもって計測するといい。

  .. code:: ipython

     In [63]: %timeit fibonacci.fibonacci_naive()
     8.64 μs ± 23 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

     In [64]: %timeit fibonacci.fibonacci_generator()
     13.4 μs ± 48.4 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

     In [65]: %timeit fibonacci.fibonacci_succinct()
     17.7 ms ± 44.4 μs per loop (mean ± std. dev. of 7 runs, 100 loops each)

* :file:`iter_vs_list_comprehension.py`

  * スクリプト名とは裏腹に、内包表記リストに対する比較対象はジェネレーターである
    ように見える。
  * ``memory_profiler`` が利用可能になったので、イテレーターと内包表記の比較結果
    を記す。数値出力周りのコードを一部改変した：

    .. code:: console

       bash$ python iter_vs_list_comprehension.py
       divisible_by_three_list with 10,000,000 entries took 2.903 seconds and used 126.980 MB
       divisible_by_three_iterator with 10,000,000 entries took 2.994 seconds and used 0.000 MB

    ただし、実際の実行時間は上記出力値よりもずっと長い。

  * 特に、関数 ``timeit.timeit()`` の使い方と ``memory_profiler.memory_usage()``
    の使い方を見ておくこと。

* :file:`lazy_data_analysis.py`

  * 本書とは無関係だが、バージョンがわからないが私のところの :command:`2to3` が
    ``from itertools import (count, groupby, ifilter, imap, islice)`` を完全に見
    逃す。
  * :file:`lazy_data_analysis.py` を実行すると浮動小数点数と ``None`` との比較が
    発生するらしく、実行時に ``TypeError`` が送出する。コードを見たら関数
    ``check_anomaly()`` の仮引数名が ``xxx_todo_changeme`` だった……。

 *  関数 ``rolling_window_grouper()`` で ``OSError`` が送出するというバグがあっ
    て結局プログラムが異常終了するしかない。これは
    ``datetime.datetime.fromtimestamp()`` に変な値を渡すときの C の
    ``localtime()`` か ``gmtime()`` がエラー終了するという挙動によるらしい。

6 章 行列とベクトルの計算
======================================================================

この章ではある 2 次元拡散方程式の計算スクリプトを徐々に高速化していく。実際に
コードを編集してプロファイルを取って分析していくことで理解が進む。

* スクリプトとプロファイル結果を同時にバージョン管理して差分を分析するといい。プ
  ロファイルは Python 標準の ``cProfile`` で十分間に合う。

  * IPython で作業をしているならば :command:`%run -p [profile-options] duffusion.py`
    でいい。

* NumPy は必要。SciPy はあるといいなくらい。
* 本編では line_profiler, perf を利用しているが、私は試せなかった。

  * `numexpr <https://github.com/pydata/numexpr>`__ は入手できた。

本章冒頭の問いに答えてみよう。

* ベクトルの計算のボトルネックは何か？

  Python の事情としては次の二点が挙げられる。C/C++ の事情と比較すると説明しやす
  い：

  1) ``list`` が実データへのポインターを保持していること
  2) バイトコードが ``for`` ループのベクトル化に最適化されていないこと

* CPU が計算を実行する効率を調べるツールは何か？

  本書著者は CPU バウンドの問題を見つけるのに最適なツールとして
  ``line_profiler`` を挙げている。 :command:`kernprof.py -lv diffusion.py` のよ
  うなコマンドライン実行結果を分析する。

* ``numpy`` を用いると Python だけを使って書くよりも数値計算の効率がよい理由は何
  か？

  1) NumPy は数値配列処理に特化して最適化されたオブジェクトを使っていること
  2) メモリ使用を局所化し、CPU のベクトル演算命令を使っていること

* キャッシュミスとページフォールトとは何か？

  キャッシュミス
    キャッシュ上にデータがなく、RAM から取得する必要がある場合を指す？ CPU バウ
    ンド処理にキャッシュミスが発生すると実行効率が悪化する原因になる。

  ページフォールト
    ページフォールトとは OS のメモリ確保機構の一部であり、あるメモリが初めて使わ
    れるときに、実行中のプログラムを一時停止し、適切なメモリを割り当てるようなも
    の。 I/O 処理にダメージを与える。

* コード上のメモリ確保を追跡する方法は？

  Linux にある :program:`perf` というツールはプログラムを実行しながら CPU の様子
  を詳細に調べることができる。 :command:`perf stat -e ... python diffusion.py`
  のようなコマンドライン実行結果を分析する。

----

以下、GitHub リポジトリーにあるリソースの分析。この章のディレクトリーは本文同様
盛りだくさんだ。

* :file:`diffusion_1d/`: 純 Python 実装による ``diffusion_python`` をベースライ
  ンとして、その改良版との計算コストの比較をする :file:`_benchmark.py` というス
  クリプトがある。これを単に実行すればよい。

  実行すると :file:`README.md` のようなテキストが出力される。ただしこのディレク
  トリーにあるものはたぶんミス。私の実行結果を次に示す：

  .. code:: console

     bash$ python _benchmark.py
     Grid size:  (1024,)
     Pure Python: 0.05s (1.020675e-03s per iteration)
     python+memory: 0.05s (9.606266e-04s per iteration)[1.06x speedup]
     numpy+memory: 0.01s (2.201748e-04s per iteration)[4.64x speedup]
     numpy: 0.01s (2.201176e-04s per iteration)[4.64x speedup]
     numpy+memory2: 0.00s (6.000996e-05s per iteration)[17.01x speedup]
     numpy+memory2+numexpr: 0.01s (2.001524e-04s per iteration)[5.10x speedup]
     numpy+memory+scipy: 0.01s (1.400852e-04s per iteration)[7.29x speedup]

     Grid size:  (2048,)
     Pure Python: 0.05s (1.060696e-03s per iteration)
     python+memory: 0.05s (1.000648e-03s per iteration)[1.06x speedup]
     numpy+memory: 0.01s (2.201748e-04s per iteration)[4.82x speedup]
     numpy: 0.01s (2.201176e-04s per iteration)[4.82x speedup]
     numpy+memory2: 0.00s (4.000664e-05s per iteration)[26.51x speedup]
     numpy+memory2+numexpr: 0.01s (2.001333e-04s per iteration)[5.30x speedup]
     numpy+memory+scipy: 0.01s (1.200771e-04s per iteration)[8.83x speedup]

     Grid size:  (8192,)
     Pure Python: 0.05s (9.806252e-04s per iteration)
     python+memory: 0.05s (9.806204e-04s per iteration)[1.00x speedup]
     numpy+memory: 0.01s (2.601624e-04s per iteration)[3.77x speedup]
     numpy: 0.01s (2.401590e-04s per iteration)[4.08x speedup]
     numpy+memory2: 0.00s (8.004189e-05s per iteration)[12.25x speedup]
     numpy+memory2+numexpr: 0.01s (1.601553e-04s per iteration)[6.12x speedup]
     numpy+memory+scipy: 0.02s (3.201962e-04s per iteration)[3.06x speedup]

  * サードパーティー製の ``numexpr`` が必要だ。

* :file:`diffusion_2d/`: 上記の 2 次元版。256 サイズだけ試す（重いから）：

  .. code:: console

     bash$ python _benchmark.py
     Grid size:  (256, 256)
     Pure Python: 10.31s (2.062975e-01s per iteration)
     python+memory: 10.33s (2.066978e-01s per iteration)[1.00x speedup]
     numpy+memory: 0.13s (2.541723e-03s per iteration)[81.16x speedup]
     numpy: 0.35s (6.944637e-03s per iteration)[29.71x speedup]
     numpy+memory2: 0.10s (1.921268e-03s per iteration)[107.38x speedup]
     numpy+memory2+numexpr: 0.11s (2.221475e-03s per iteration)[92.87x speedup]
     numpy+memory+scipy: 0.17s (3.422313e-03s per iteration)[60.28x speedup]

* :file:`norm/`: :file:`Makefile` があるので、これでメモリなり処理時間なりを計測
  する。

7 章 C にコンパイルする
======================================================================

本章は本書の目玉の一つと見られる。残念ながら手許にコンパイラーがないので何もでき
ない。

でも冒頭の問いには回答を用意したい。

* どうすれば Python のコードを低水準コードとして実行できるか？

  コンパイラーを用いて、Python コードを機械語に変換する。コンパイラーには
  Cython, Shed Skin, Numba, Pythan, PyPy などがある。

* JIT コンパイラと AOT コンパイラの違いとは何か？

  * JIT: Just In Time すなわち必要になったときにコンパイルする

    コード使用時に初めて必要部分がコンパイルされるので、未コンパイル時にスクリプ
    トを実行するとまずコンパイルするので、実行がひじょうに遅くなる（これをコール
    ドスタート問題という）。

  * AOT: Ahead Of Time すなわち事前にコンパイルすることで、静的なライブラリーを
    生成する。

* コンパイルによって Python よりも高速化できる処理にはどんなものがあるか？

  数学的な処理で、同じ演算を大量に反復するような、あるいは反復処理時に多数の一時
  的なオブジェクトが生成されるような処理がコンパイルによる高速化の対象となりやす
  い。

* データ型の注釈をつけると、なぜコンパイルされた Python コードが高速化できるの
  か？

  C コンパイラが最適化できるように。

* C や Fortran を使って、どのようにモジュールを書くのか？

  それらの言語でコンパイルしたコードをアクセスできる外部関数インターフェイスを使
  う。

* C や Fortran のライブラリを、どのように Python で使うのか？

  * C に対しては Python 標準の ``ctype`` モジュールや ``cffi`` モジュール
  * Fortran に対しては :command:`f2py` コマンド

----

以下、GitHub リポジトリーにあるリソースの分析。

* 前章以上に豊富なコード群。しかしコンパイラーがないので何もできない。

8 章 並行処理
======================================================================

大事なテーマだと思うが、意外にページ数を割いていない。

* 並行処理とは何で、どのように役立つか？

  イベントループを実行して、さまざまなイベントに応じてプログラムのさまざまな部分
  を実行するような処理。例えば、I/O 待ち時間の間に他の処理（タスク）に活用する。

* 並行処理と並列処理の違いは何か？

  TBW

* 並行処理ができるタスクは何で、できないタスクは何か？

  TBW

* 並行処理にまつわるパラダイムにはどのようなものがあるのか？

  * ``gevent``: ``Future`` 形式
  * ``tornado``: コールバックと ``Future`` の両方
  * ``asyncio``: コールバックと ``Future`` の両方

  ``Future`` とコルーチンを同義語として読んだが……。

* 並行処理を活用するのはどんなときか？

  I/O バウンドの問題を含む処理。

* 並行処理はどのようにプログラムを高速化するのか？

  TBW

----

以下、GitHub リポジトリーにあるリソースの分析。

* :file:`cralwer/`

  * 実行時エラーは出るものの、ベンチマーク構成が素晴らしい。こういうコードを書け
    るようになりたいものだ。

  * :file:`benchmark.sh` で :file:`server.py` をバックグラウンドで起動してからの
    計測対象群を実行する手際の良さに注目したい。

    * 最後に :file:`visualize.py` でこれまでの出力をプロットして PNG 形式で保存
      するというのもしゃれている。

    * :file:`asyncio/crawler.py` を実行するときだけ、環境変数 ``PYTHONPATH`` を
      退避するのはなぜか。

  * :file:`server.py` は HTTP サーバーを実装したもので、サードパーティー製である
    Tornado を利用している。

    * ``ujson`` なるモジュールをインポートしているが、これはたぶんここには存在し
      ない。

  * 各サブディレクトリーの :file:`crawler.py` の読み方がわからない場合は
    :file:`asyncio/` にあるものを基準に解読できそうだ。

* :file:`primes/`

  * ``grequests`` が必要。
  * :file:`primes.py` を編集して ``__slot__`` の中身からメソッドを取り除く。
    ``ValueError: 'save' in __slots__ conflicts with class variable`` を解決する
    ため。
  * 手動で :file:`server.py` を起動しておく。

9 章 ``multiprocessing`` モジュール
======================================================================

本書では Linux を対象としているので、本章で Windows ユーザーがいくらか困る。特に
Pool の選択肢が大幅に狭められていることに気づく。

* ``multiprocessing`` モジュールは何を提供するのか？

  * プロセスとスレッドを使った並列処理を実現できる。
  * 一台のマシンでマルチコアの並列処理をする。
  * 一般には CPU バウンドの問題を解く処理（群）を並列化するのに使う。

* プロセスとスレッドの違いは何か？

  * スレッドには GIL 競合によるオーバーヘッドの有無などが挙げられる。
  * スレッドは I/O バウンドの処理には適するが、CPU バウンドの問題解決には不適切
    だ。
  * 違いは他にもあるだろう。

* プロセスプールの適切な選択方法は？

  TBW

* プロセスを実行するための非永続型キュー（待ち行列）の使い方は？

  * 負荷が変動するときや、時間が経つにつれて負荷が次々と発生する場合に使う。
  * 非永続型なので、電源喪失やディスク故障のような失敗に対応するのが必要な場合は
    使わない。

* プロセス間通信の損失は何か？

  * データのコピーを通信するということだから、RAM に負担がかかる。

* 複数の CPU を使って ``numpy`` のデータを処理する方法は？

  * 配列データを複数プロセス間で共有する方法は？と同じ意味。

    1) メモリ領域を共有可能にするには ``multiprocessing.Array`` を使う。
    2) 共有領域を関数 ``numpy.frombuffer()`` に渡して ``numpy`` 配列を生成する。

* データの欠損を回避するためにロックする必要があるのはなぜか？

  * 共有データを同期的に読み書きすることで整合性を保つ仕組みがロックだ。

----

以下雑感。

* 私の PC はコア数 2 なので、本章の内容が十分に検証できない。
* 素数分布のコード、出力結果がソートされているわけではないことに注意。
* 省略されている ``create_range.create()`` 関数の実装は次のようなものと思われる：

  .. code:: python3

     def create(start, end, num_processes):
         a = np.linspace(start, int(np.sqrt(end)) + 1, num_range, dtype=int)
         return ((i, j) for i, j in zip(a, a[1:]))

* Python 3.6.5 で試しているからか、次のような不具合があった：

  * RawValue をフラグとして用いるコードが成功しない。
    ``TypeError: this type has no size`` となる。
  * ``mmap.write_byte(FLAG_CLEAR)`` が成立しない。
    ``TypeError: an integer is required (got type bytes)`` となる。

* ロックの例題 ``ex2_nolock`` は成功率が案外高くて困る。
  :command:`python -m timeit` で 10 回反復させて 9 回正しい結果が得られたことも。

  * コンテキストマネージャーを用いずに、つまり ``acquire()`` と ``release()`` を
    明示的に書くほうが若干速いらしいが、こんなことは知らないふりをしていいだろ
    う。

まともに本章に取り組むと一日潰れる。

----

以下、GitHub リポジトリーにあるリソースの分析。この章に対応するディレクトリーに
ある :file:`chapter_recipe.txt` のコードを追体験するのがいい。

* :file:`locking/`

  * :file:`ex1_lock.py` がやたら遅いわロックに失敗するわで、いいところがない。
  * :file:`ex3_redis.py` だけ Redis が必要。

* :file:`np_shared_example/`: NumPy 配列の共有化という、たいへん難しいテーマ。

  * :file:`np_shared.py`: 共有配列を設定する。

    * ``multiprocessing.Array`` と ``numpy.frombuffer()`` を組み合わせる。
    * ``map.pool()`` で指定される 4 プロセス（ワーカー）それぞれがその配列にアク
      セスする。
    * サブディレクトリーのものはマルチプロセスまたはスレッドのどちらかによる配列
      アクセス（書き込み）。

* :file:`pi_estimation/`: モンテカルロ法。

  * :file:`pi_lists_parallel/`

    * :file:`pi_lists_parallel.py`: マルチプロセスまたはスレッドのどちらかによる
      ``pool.map()`` によるモンテカルロ法円周率見積もり並列処理。
    * :file:`profile_cpu_usage.py`: 上のスクリプトをいろいろなコマンドラインオプ
      ション値で
      実行し、プロファイルを取る。

      * らしいのだが、意味をなさないコードがある。修正方法も推測不能。

        .. code:: python3

           if args.processes:
               xargs.append("--processes")
               SLEEP_FOR = {8: 3, 4: 4, 2: 7, 1: 15}[args.nbr_processes]
           else:
               print("THREADED VERSION")
               SLEEP_FOR = {4: 20}[args.nbr_processes]

      * ``subprocess.Popen`` 使用。

  * :file:`pi_monte_carlo_diagram/`: よくある円周率の見積もり。単位円に外接する
    正方形内に多数の点をランダムに取り、その点のうちで単位円に含まれるものとそう
    でないものの比を用れば、近似的に円周率を計算できる。
  * :file:`pi_processes_parallel/`: 以下のコードでは Python 3 化するときに
    ``nbr_samples_in_total`` と ``nbr_samples_per_worker`` を ``int`` 型に手動で
    修正する必要がある。

    * :file:`pi_numpy_parallel_worker.py`: 上記 :file:`pi_lists_parallel.py` の
      NumPy 版。
    * :file:`pi_numpy_serial.py`: 上のスクリプト内に定義されている関数
      ``estimate_nbr_points_in_quarter_circle()`` を一回実行する。
    * :file:`pi_numpy_serial_blocks.py`: 逐次処理。

* :file:`prime_generation/`

  * :file:`plot_serial_vs_queue_times.py`: 意味不明。
  * :file:`primes.py`: もっとも単純な素数列挙コード。
  * :file:`primes_pool.py`: ``multiprocessing.Pool`` 使用。
  * :file:`primes_queue.py`: ``multiprocessing.Queue`` 使用。
  * :file:`primes_queue_jobs_feeder_thread.py`: Pool と Queue に加えて
    ``threading.Thread`` 使用。
  * :file:`primes_queue_less_work.py`: :file:`primes_queue.py` の探索対象を半分
    にしたもの。

* :file:`prime_validation/`: プロセス間通信で素数判定

  素数判定という重いプログラムを実行するわけだが、実行途中で処理を殺すのがマルチ
  プロセスゆえたいへん面倒なので注意したい。

  次のスクリプト群は素数判定自身に関係するコード。ロジックについては本文参照。

  * :file:`create_range.py`: 素数判定計算並行化のために整数区間を等分割する関数。
  * :file:`primes.py`: 関数 ``check_prime()`` を ``timeit.repeat()`` で計測する。
  * :file:`primes_pool_per_number1.py`: 整数区間を等分割して素数判定に入る。
  * :file:`primes_pool_per_number2.py`: 上の若い素数は判定をスキップする版。

  以下はフラグ系。

  * :file:`primes_pool_per_number_manager.py`: ``multiprocessing.Manager`` 使用。
  * :file:`primes_pool_per_number_value.py`: Manager + Value を RawValue にした版。
  * :file:`primes_pool_per_number_value_withinit.py`: 上のものに謎の初期化コード
    を入れた版。
  * :file:`primes_pool_per_number_redis.py`: RawValue を Redis というインメモリ
    データベースで置き換えた版。

  以下は ``mmap`` 系。

  * :file:`primes_pool_per_number_mmap.py`: ``mmap.mmap`` 使用。ただし Python 3
    化すると ``mem.write_byte()`` の呼び出しで例外送出。以下の例でも同様。
    ``FLAG_XXX`` を整数にするのが楽な修正方法。
  * :file:`primes_pool_per_number_mmap2.py`: 上の微調整版。
  * :file:`primes_pool_per_number_mmap3.py`: 上のループ二段階化版。
  * :file:`primes_pool_per_number_mmap4.py`: 上のフラグを局所変数化した版。
  * :file:`primes_understand_comms_frequency.py`: 先の mmap3 の通信状況をわかり
    やすくする版。

10 章 クラスタとジョブキュー
======================================================================

手許にマシンがノート PC 一丁しかないので、この章は残念だが通読しない。

* なぜクラスタが便利なのか？

  * マシンを追加することで計算の要求条件を拡大できる。
  * マシンを追加することで信頼性が上がる。
  * 動的にスケールするシステムを組むのに使える。さらにコストも調節できる。
  * マシンが物理的に離れていてもかまわない。
  * あるいはさまざまなソフトウェア環境の上でも動作できる（上級者向け）。

* クラスタリングのコストは何か？

  * システム管理それ自体がコスト。複数機の面倒をみるのはたいへん。システムの更新
    に必要な時間と費用がかさむ。
  * クラスタリング特有のアルゴリズムや同期管理を設計するコスト。

* ``multiprocessing`` による解法をクラスタに対応させるにはどうすればよいか？

  * Parallel Python のインターフェイスが ``multiprocessing`` と非常に似ているの
    で、例えば ``multiprocessing`` を用いたコードをクラスタ用に書き換えるのはわ
    ずかな時間の作業で済む。

* IPython のクラスタ機能はどのように動作するか？

  * マルチコアを持つ一台のマシンで容易に使える。
  * IPython がローカル環境とリモート処理エンジンの両方のインターフェイスとなる。
  * ZeroMQ などへの依存性がある。
  * リモートのクラスタをローカルなそれと同様に簡単に使える。
  * プロジェクトは次の構成要素からなる：

    * エンジン：Python のインタプリター
    * コントローラー：エンジンとのインターフェイスおよび処理の分散を担当する
    * ダイレクトビュー：？
    * 負荷分散ビュー：？
    * ハブ：エンジン、スケジューラー、クライアントを追跡する
    * スケジューラー：非同期インターフェイス

* NSQ を使うとどのように堅牢な実用システムを組めるか？

  * NSQ は永続性がある。あるマシンが停止しても、ジョブは他のマシンで再開する。
  * 使いこなすにはシステム管理と開発の技量が必要だ。
  * pub/sub/consumer パターンとでもいうべき設計思想。

----

以下雑感。

* クラスタとは複数の計算機を使って一つの共通タスクを解くシステムだが、このシステ
  ムを単一のシステムとしてみなすのが本質的だ。
* TODO: Install Parallel Python (``pp``)
* TODO: Install IPython Parallel (``ipcluster``)

  * 例 10-3 の ``IPython.parallel`` は IPython 4.0 でとっくに deprecated になっ
    ている。

----

以下、GitHub リポジトリーにあるリソースの分析。この章のコードも気合が入ってい
る。

* :file:`ipythonparallel/`
* :file:`nsq/`
* :file:`parallelpython/`
* :file:`pi_hypotenuse/`
* :file:`pi_trig/`
* :file:`primes/`
* :file:`queue/`

11 章 RAM 使用量を削減する
======================================================================

データには質量がある。これは至言だ。

* なぜ RAM の使用量を減らすべきなのか？

  * 他のプログラムも RAM を使用するから。

* 大量の数を記憶するのに ``numpy`` と ``array`` が優れているのはなぜか？

  * Python 組み込みのリストでは、異なる要素ごとにメモリのコストがかかる。一
    方、``numpy`` と ``array`` は ``int`` のような基本データ型を効率よく記憶す
    る。 C 言語の配列のように連続した RAM 領域を確保する。
  * Python は 基本データ型のオブジェクトを（使われなくなっても後の利用のために）
    キャッシュする。
  * NumPy はさらに ``complex`` と ``datetime`` も効率よく扱える。

* どのようにしたら大量のテキストを効率よく RAM 上に記憶できるのか？

  * 文字列を記憶するために、トライや DAWG といったデータ構造を採用すること。共通
    接頭辞検索という検索手法と相性がよい。

* どのようにしたらたった 1 バイトで 1e77 (:math:`10^{77}`) まで（近似的に）数え
  られるか？
* Bloom フィルタとは何で、必要になる理由は何か？

----

以下雑感。

* 本書と私の手許の IPython 上とでの ``array?`` の出力が異なる。こちらの
  ``array.array?`` に近い。
* ``sys.getsizeof()`` の結果は想像より大きい。しかも実際にはみてくれの値よりも多
  くのメモリを消費しているはずだ。例えばリストの ``getsizeof()`` はリストオブ
  ジェクトそのものが消費するバイト数しか返さない。含んでいる要素のバイト数は勘定
  に入らない。
* Python 3.3 以降では Unicode のメモリ効率が飛躍的に改善したことは知っておく。
* トライと DAWG の概念の違いは頭に叩き込んでおく。
* TODO: Install ``dawg``
* 確率的データ構造の説明が頭に入らない。読者が URL の資料を見るのが前提の文章だ。

  * どれも精度を犠牲にするがメモリの消費量を大幅に削減する特徴がある。
  * どれも冪等性という性質がある。同じ入力値を繰り返し与えても状態は変わらない。
  * 指数と対数を利用するものが多いようだ。
  * Morris counter: カウンターを :math:`2^N` の形で表現するが、管理するのは
    :math:`N` のみ。カウンターは :math:`i` 回目の増分時に確率
    :math:`\dfrac{1}{2^i}` で実施する。
  * K-最小値：K 個の最小かつ一意なハッシュ値を保持する。ハッシュ値間の距離を近似
    することで総数を推定する。
  * Bloom filter: ``x in X`` タイプの問い合わせを確率的に実現する。値を複数の整
    数値として表現する。そのために複数のハッシュ値を用いる。 「同じハッシュ値の
    集合を持つ値は同じだろう」という期待による。
  * LogLog counter: 先頭に 0 が続くハッシュ値を記録して、それまでに勘定した要素
    数を推定する。

----

以下、GitHub リポジトリーにあるリソースの分析。この章のコードも気合が入ってい
る。

* :file:`getsizeof/`: 本文中にある ``asizeof`` の説明を参照。
* :file:`compressing_text/`: 大量テキストから単語を検索する。

  <Wikipedia の部分ダンプから構築したテストセット> がないので再現は無理か。あと
  著者は UNIX 使いだと思っているが Windows-1252 エンコードを採用するのはなぜだ。

  * :file:`text_example.py`: 関数 ``read_words()`` の実装。
  * :file:`text_example_datrie.py`: ``datrie`` モジュールが必要。
  * :file:`text_example_dawg.py`: ``dawg`` モジュールが必要。
  * :file:`text_example_hattrie.py`: ``hat_trie`` モジュールが必要。
  * :file:`text_example_list.py`: テキストをソートしないリストに記憶して検索す
    る。
  * :file:`text_example_list_bisect.py`: 上のソート済みリスト版。ベンチマークの
    ベースライン。
  * :file:`text_example_set.py`: テキストを集合に記憶して検索する。
  * :file:`text_example_trie.py`: ``marisa_trie`` モジュールが必要。

* :file:`morris_counter_example/`: Morris カウンター。

  * :file:`morris_counter.py`: クラス ``MorrisCounter`` の実装。本文のそれより複
    雑。
  * :file:`show_morris_counter.py`: クラス ``MorrisCounter`` のデモ。

* :file:`probabilistic_datastructures/`

  モジュール ``mmh3`` がハッシュのために必要だ。

  * :file:`morriscounter.py`: 本文どおりのクラス ``MorrisCounter`` の実装。
  * :file:`kminvalues.py`: クラス ``KMinValues`` の実装。

  以下 Bloom フィルター系。

  * :file:`bloomfilter.py`: クラス ``BloomFilter`` の実装。
  * :file:`scalingbloomfilter.py`: クラス ``ScakingBloomFilter`` の実装。
    上の ``BloomFilter`` と has-a 関係がある。

  以下 LogLog カウンター系。

  * :file:`ll.py`: クラス ``LL`` の実装。本文でいう簡単な LogLog カウンター。
  * :file:`llregister.py`: クラス ``LogLogRegister`` の実装。
  * :file:`superll.py`: クラス ``SuperLL`` の実装。
  * :file:`hyperloglog.py`: クラス ``HyperLogLog`` の実装。

  * :file:`_benchmark.py`: 上記各種カウンターのベンチマークスクリプト。

    * 実行するには :file:`enwiki-latest-pages-articles.tokens` なるファイルが必
      要。
    * あと ``countmemaybe`` というパッケージが必要。

12 章 現場に学ぶ
======================================================================

Python の性能を追求するのが目的の本書において異色の章だが、いちおう読む。

* 成功しているスタートアップ企業は、どのように大量のデータを扱い機械学習している
  のか？

  TBW

* どんな監視技術やデプロイ技術を使えばシステムを安定化できるのか？

  * SaltStack: サーバーのプロビジョニング用
  * Circus: 長時間実行プロセスの管理
  * Redis: クラスタリング
  * Fabric: タスク実行
  * Vagrant: システム構築（デプロイ）
  * etc.

* 成功している CTO は、技術や開発チームからどんな教訓を得ているのか？

  * Python はプロトタイピング用の言語であるという以上に便利だ。
  * スタートアップ初期は特に実践的になることが重要だ。
  * 常にプロトタイプを作ってはコードや性能を改善する。

* PyPy はどのくらい広範に適用できるのか？

  * 小さなプロジェクトから中規模プロジェクトまでは実績あり。
  * プロトコルの実装や圧縮アルゴリズムの実装に用いた実績あり。
    後者のスピードには驚いたそうだ。

付録 A サンプルプログラムについて
======================================================================

* <https://github.com/mynameisfiber/high_performance_python>
* :file:`Makefile` がいくつかあるので、ターゲットを確認しておく。
* Python 2 対応コードなので、Python 3 化は利用者それぞれで実施する。コマンドライ
  ンは :command:`2to3 -w .` でよさそうだ。

* サンプルプログラムが利用しているサードパーティーパッケージのうち、主要なものを
  まとめておく：

  ================ ======== ===========================================
  パッケージ       入手方法 備考
  ================ ======== ===========================================
  runsnake         pip      wxPython が必要
  line_profiler    pip      VC コンパイラーが必要
  memory_profiler  pip
  guppy            pip
  dowser           pip
  coverage         pip      本書のサンプルでは未使用
  numexpr          pip      NumPy が必要
  gevent           pip
  grequests        pip
  tornado          pip      なぜかすでに手許にあった
  Twisted          pip
  Redis            ?
  lockfile         pip
  pp               pip
  ipclustrer       pip
  NSQ              ?
  dawg             github?
  marisa_trie      github?
  datrie           github?
  hat_trie         github?
  countmemaybe     github?
  mmh3             ?
  ================ ======== ===========================================
