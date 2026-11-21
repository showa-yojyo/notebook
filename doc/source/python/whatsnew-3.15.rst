================================================================================
What's New In Python 3.15 ノート
================================================================================

`What's New In Python 3.15 <https://docs.python.org/3/whatsnew/3.15.html>`__ を
たどりながら調査。興味のあるものしか読まない。

.. contents:: 見出し一覧
   :local:

New features
================================================================================

遅延インポート文 ``lazy import``
--------------------------------------------------------------------------------

次の構文が搭載された：

* :samp:`lazy import {module}`
* :samp:`lazy from {module} import {module_item}`

この ``import`` 文を用いると、*module* や *module_item* が初めて用いられる頃合い
まで読み込みが先送りされる。

この仕組が特に有用なのは、最上位で多数のモジュールを ``import`` するものの、実際
の実行時にはその一部しか使用しないようなパッケージやアプリケーションだ。

モジュール読み込みが失敗する場合、例外送出の頃合いは ``import`` 対象の名前が最初
に用いられた時点だ。

手持ちの Python コードを変更せずに遅延 ``import`` を有効にする方法がある：

* :program:`python` のコマンドラインオプション ``-X lazy_imports`` を指定する
* 環境変数 ``PYTHON_LAZY_IMPORTS`` を使う。

.. list-table:: 遅延オプションの値と動作
   :align: left
   :header-rows: 1
   :stub-columns: 0
   :widths: auto

   * - 値
     - 動作
   * - ``all``
     - ``import`` の全てが lazy になる
   * - ``normal``
     - コード内のキーワード ``lazy`` の有無に従う

この遅延モードに関連する関数が新規に追加した：

.. list-table:: 遅延 ``import`` に関係する関数
   :align: left
   :header-rows: 1
   :stub-columns: 0
   :widths: auto

   * - 関数
     - 動作
   * - ``sys.set_lazy_imports()``
     - 実行時に遅延モードを設定する
   * - ``sys.get_lazy_imports()``
     - 実行時点の遅延モードを確認する

遅延 ``import`` はモジュールスコープでしか認められない。関数内、クラス本体、
``try``/``except``/``finally`` ブロック内で ``lazy`` を使用すると ``SyntaxError``
が送出する。同様に、米印 ``import`` や ``from __future__ import`` を ``lazy`` に
することは不可能だ。

Python 3.15 より前の Python でも動作するコードを書かねばならない場合、モジュール
属性として ``__lazy_modules__`` を定義し、値として遅延 ``import`` 可能なモジュー
ル名を（完全修飾名により）列挙する。そうすることで、それらのモジュールに対する通
常の ``import`` 文は ``lazy`` として扱われる。例を標準ライブラリー文書から引用す
る：

.. sourcecode:: python
   :caption: ``__lazy_modules__`` 定義例
   :force:

   __lazy_modules__ = ["json", "pathlib"]

   import json     # lazy
   import os       # still eager

内蔵型 ``frozendict``
--------------------------------------------------------------------------------

内蔵型 ``frozendict`` が追加。その名前が示す性質を持つ。

* 辞書オブジェクト作成後に値としての変更は不可能。
* 基底型は ``object`` であり、``dict`` ではない。
* キーと値のすべてがハッシュ可能である場合、かつその場合に限り、辞書自身もハッ
  シュ可能だ。
* 項目の追加順序を維持する。
* 比較の際には追加順序は考慮しない。

標準ライブラリーの ``dict`` を受け付ける機能のうち、``frozendict`` も受け付ける
ようになったものがある。

既存コードに ``isinstance(arg, dict)`` のようなコードがあるならば、それを更新す
るべきだろう。

* 案一： ``isinstance(arg, (dict, frozendict))``
* 案二： ``isinstance(arg, collections.abc.Mapping)``

内蔵型 ``sentinel``
--------------------------------------------------------------------------------

内蔵型 ``sentinel`` が追加。機能は一意の値を簡潔な表現で生成することだ。

* オブジェクトを複製しても同一性を保持する。
* 演算子 ``|`` を用いた型表現（←術語がわからない）での使用に対応。
* モジュールと名前で ``import`` が可能なオブジェクトであるときに ``pickle`` 操作
  が可能。

プロファイリング特化パッケージ ``profiling``
--------------------------------------------------------------------------------

モジュール ``profiling`` が新規に追加。下位モジュールが二つ：

* ``profiling.tracing``: ``cProfile`` から移行。関数呼び出し探知モジュール
* ``profiling.sampling``: 統計的性能測定モジュール

互換性確保のため、モジュール ``cProfile`` は上記下位モジュールの別名として存続す
る。モジュール ``profile`` は Python 3.17 で削除する予定だ。

モジュール ``profiling.sampling`` に関する、Python 公式によるテキストをいくつか
引用する：

   This profiler enables low-overhead performance analysis of running Python
   processes without requiring code modification or process restart.

最速：

   ... making it the fastest sampling profiler available for Python (at the time
   of its contribution) and ideal for debugging performance issues in production
   environments. This capability is particularly valuable for debugging
   performance issues in production systems where traditional profiling
   approaches would be too intrusive.

内包記法内の unpack 操作が可能になる
--------------------------------------------------------------------------------

これはコードを見るほうが話が早い。標準手引から引用する：

.. sourcecode:: python
   :caption: 内包記法内の unpack 操作
   :force:

   lists = [[1, 2], [3, 4], [5]]
   [*L for L in lists]  # equivalent to [x for L in lists for x in L]

   sets = [{1, 2}, {2, 3}, {3, 4}]
   {*s for s in sets}  # equivalent to {x for s in sets for x in s}

   dicts = [{'a': 1}, {'b': 2}, {'a': 3}]
   {**d for d in dicts}  # equivalent to {k: v for d in dicts for k,v in d.items()}

   gen = (*L for L in lists)  # equivalent to (x for L in lists for x in L)

込み入った構造のコンテナーを平坦な構造のそれに作り直しやすくなるということだ。例
えば次の手法を避けられるようになった：

* 入れ子の内包表記
* ``itertools.chain()``
* ``itertools.chain.from_iterable()``

Other language changes
================================================================================

* 引数として ``enconding`` があるような内蔵関数、標準ライブラリー関数の全てにおい
  て、未指定時の値が ``utf-8`` であるようになる。

  昔のコードで ``encoding`` の指定がないものは、Python 3.15 に更新すると動作が変
  化すると考えられる。
* Python 本体を含む、Python 各種標準ライブラリー CLI からの端末ウィンドウで各種
  出力がカラフルになる。
* ``ImportError`` / ``ModuleNotFoundError`` の ``__repr__()`` が生成時にキーワー
  ド引数として ``name`` /  ``path`` が指定されていた場合、これらを次の形式で表示
  するようになる：

  * :samp:`name={<name>}`
  * :samp:`path={<path>}`

  例外捕捉時の状況分析に有用だろう。
* 時刻や制限時間を引数とする関数が ``int`` や ``float`` の他に ``Decimal`` や
  ``Fraction`` なども受け付ける。もっとも、精度がそれらの表現に沿うというわけで
  はないようだ。
* ``bytearray.take_bytes(n=None, /)`` が追加。コピーを生じさせずに ``bytearray``
  から ``bytes`` を取り出せる。これを採用することで処理効率が良くなる例：

  * ``bytearray`` を ``bytes`` に変換する
  * ``bytearray`` の部分を得る
* ``bytes.replace()`` にキーワード引数 ``count`` を与えてもよい。

New modules
================================================================================

モジュール ``math.integer`` が新規追加。整数専用の数学関数で構成されている。例え
ば次の関数が用意されている：

* ``comb(n, k, /)``
* ``factorial(n, /)``
* ``gcd(*integers)``
* ``isqrt(n, /)``
* ``lcm(*integers)``
* ``perm(n, k=None, /)``

関数 ``isqrt`` は名前から機能を想像できなかった。Python 標準から記述を引用する：

   Return the integer square root of the nonnegative integer :math:`n`. This is
   the floor of the exact square root of :math:`n`, or equivalently the greatest
   integer a such that :math:`{a^{2} \le n}`.

Improved modules
================================================================================

興味のあるものや遭遇しそうな問題を含むモジュールに絞って記していく。

``array``
--------------------------------------------------------------------------------

複素数配列を扱える。また、16 ビット IEEE 754 バイナリー交換形式浮動小数点数配列
も扱える。

.. list-table:: Python 3.15 で使用可能になる配列型
   :align: left
   :header-rows: 1
   :stub-columns: 0
   :widths: auto

   * - コード
     - C
     - Python
   * - ``'Zf'``
     - ``complex float``
     - ``complex``
   * - ``'Zd'``
     - ``complex double``
     - ``complex``
   * - ``'e'``
     - ``float``
     - ``float``

``asyncio``
--------------------------------------------------------------------------------

メソッド ``TaskGroup.cancel()`` が追加。例えば仕事の目標が達成された場合や、そ
のサービスが不要になった場合などに呼び出すといい。

``calendar``
--------------------------------------------------------------------------------

CLI での出力をよりカラフルにしたり、HTML 出力を HTML5 に移行したり。

``gc``
--------------------------------------------------------------------------------

Python 3.14 初期バージョンでは増分型のゴミ収集をしていたが、現場からメモリー枯渇
が深刻だという声が相次ぎ、これを従来の世代型収集に戻したそうだ。

``math``
--------------------------------------------------------------------------------

* 関数 ``math.isnormal()`` 追加。引数が有限非零数であり、かつ、下記
  ``math.issubnormal()`` が同じ引数に対して ``False`` を返す値か否かを返す。
* 関数 ``math.issubnormal()`` 追加。引数が ``sys.float_info.min`` より小さい絶対
  値を持つ有限非ゼロ数であるか否かを返す。
* 関数 ``math.fmax()``, ``math.fmin()``, ``math.signbit()`` 追加。これらは NaN
  値をいい感じに取り扱う。

``os``
--------------------------------------------------------------------------------

関数 ``os.makedirs()`` に引数 ``parent_mode`` が追加。親から子までの中間ディレク
トリーのファイルモードを指定する。

``pathlib``
--------------------------------------------------------------------------------

メソッド ``pathlib.Path.mkdir()`` にも引数 ``parent_mode`` が追加。

``pdb``
--------------------------------------------------------------------------------

入力シェル未指定時には新しい対話型シェルを用いる。

``pprint``
--------------------------------------------------------------------------------

主力関数群にキーワード引数 ``expand`` が追加。引数が ``True`` である場合、
``indent`` が与えられた際の出力形式が ``json.dumps()`` による pritty-print と同
様になる。

また、t-文字列対応を ``pprint.pprint()`` に追加。

``re``
--------------------------------------------------------------------------------

関数 ``re.prefixmatch()`` およびメソッド ``re.Pattern.prefixmatch()`` が関数
``re.match()`` およびメソッド ``re.Pattern.match()`` それぞれの代替として追加。
Deprecated 節でも述べる。

``subprocess``
--------------------------------------------------------------------------------

メソッド ``subprocess.Popen.wait()`` で ``timeout`` が指定されている場合、動作プ
ラットフォームによっては、プロセスの終了を待機するのに効率的なイベント駆動型メカ
ニズムが採用される。

``typing``
--------------------------------------------------------------------------------

次の更新に関心がある：

   ``TypeVarTuple`` now accepts ``bound``, ``covariant``, ``contravariant``, and
   ``infer_variance`` keyword arguments, matching the interface of ``TypeVar``
   and ``ParamSpec``. bound semantics remain undefined in the specification.

``unicodedata``
--------------------------------------------------------------------------------

Unicode データベースが Unicode 17.0.0 に刷新。

Optimizations
================================================================================

ここは一般プログラマーには重要ではないかもしれない。ほとんどチェックしていない。

Removed
================================================================================

私の持っているコードに影響する削除が存在しないと考えられる。

Deprecated
================================================================================

古いやり方をいつまで経っても採用し続けないように、一通りチェックする。文書化され
ていない機能や特定のプラットフォーム固有の挙動に関するものがほとんどだ。

* 関数 ``re.match()`` が軽く deprecated 扱いとなった。代わりに関数
  ``re.prefixmatch()`` を使え。
* モジュール ``asyncio`` のポリシーシステム
* リテラル値 ``True``, ``False`` に対する単項演算子 ``~`` の適用
* ``os.path.commonprefix()`` ではなく ``os.path.commonpath()`` を使え。

Porting to Python 3.15
================================================================================

気にするのは一点しかない。

``argparse.ArgumentParser.add_argument()`` に短いオプション (e.g. ``-f``) と
``-`` が一つしかないのに名前が長いオプション (e.g. ``-foo``) とが同時に渡される
場合、値 ``dest`` は後者から推論 (e.g. ``foo``) される。

.. include:: /_include/python-refs-core.txt
