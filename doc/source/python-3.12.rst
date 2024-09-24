======================================================================
What's New In Python 3.12 ノート
======================================================================

`What's New In Python 3.12 <https://docs.python.org/3/whatsnew/3.12.html>`__ を
たどりながら調査。興味のあるものしか読まない。

.. contents:: ノート目次
   :local:

New Features
======================================================================

PEP 695: Type Parameter Syntax
----------------------------------------------------------------------

Python の術語では generic というのだが、C++ の関数テンプレートやクラステンプレー
トに相当するコードの記法が改善した。例えば次のようなコードが合法になる：

.. sourcecode:: python
   :caption: ``std::minmax`` のような Python 関数

   def minmax[T](a: T, b: T) -> (T, T):
       return (b, a) if b < a else (a, b)

さらに、``TypeAliasType`` のオブジェクトを生成する ``type`` 文を使用して、型別名
を宣言する新しい方法が導入された：

.. sourcecode:: python
   :caption: ``type`` 文を用いた型別名の例

   type Point2D = tuple[float, float]
   type Point3D[T] = tuple[T, T, T]

``TypeVarTuple`` と ``ParamSpec`` 宣言する新文法：

.. sourcecode:: python
   :caption: ``type`` による ``TypeVarTuple`` および ``ParamSpec`` の宣言例

   type IntFunc[**P] = Callable[P, int]  # ParamSpec
   type LabeledTuple[*Ts] = tuple[str, *Ts]  # TypeVarTuple

一行目は ``P = typing.ParamSpec('P')`` を含意する。ただし ``P`` というオブジェク
トを生成するわけではない。``IntFunc`` が「単品」で使える。

二行目は ``Ts = typing.TypeVarTuple('Ts')`` を含意する。ただし ``Ts`` というオブ
ジェクトを生成するわけではない。

また、束縛や制約を持つ ``TypeVar`` も同様に宣言可能だ：

.. sourcecode:: python
   :caption: ``type`` による束縛 ``TypeVar`` および制約 ``TypeVar`` の宣言例

   type HashableSequence[T: Hashable] = Sequence[T]  # TypeVar with bound
   type IntOrStrSequence[T: (int, str)] = Sequence[T]  # TypeVar with constraints

一行目は ``T = typing.TypeVar('T', bound=typing.Hashable)`` を含意するが ``T``
そのものとしては生成しない。

同様に、二行目は ``T = typing.TypeVar('T', int, str)`` を含意するが ``T`` そのも
のは生成しない。

PEP 701: Syntactic formalization of f-strings
----------------------------------------------------------------------

.. rubric:: 引用符の再利用

以前は f-string を囲む引用符と同じ記号を再利用すると ``SyntaxError`` が送出して
いた。例えば ``f"..."`` では ``...`` の部分に ``"`` を入れることはできなかった。
これが可能になった。

.. sourcecode:: ipython
   :caption: 二重引用符を f-string の中でも使える

   In [1]: things = []

   In [2]: f"These are the things: {", ".join(things)}"
   Out[2]: 'These are the things: '

そして、f-strings は有効な Python 式を式部品の中に含むことができるようになったの
で、f-strings を入れ子にすることができるようになった。

.. rubric:: 複数行の式とコメント

以前は f-string 式は一行で定義する必要があった。Python 3.12 では複数行にわたる
f-string を定義し、インラインコメントを追加できるようになった。

.. rubric:: バックスラッシュと Unicode 文字

以前の f-string 式はどんなバックスラッシュ文字をも含むことが不可能だった。特に、
Unicode エスケープシーケンスに悪影響があった。

.. sourcecode:: ipython
   :caption: 以前は改行文字すら入れられなかった

   In [1]: a = ["Hello", "world"]

   In [2]: f"{"\n".join(a)}"
   Out[2]: 'Hello\nworld'

.. rubric:: エラーメッセージの精度向上

以上の文字列解析機能強化により、副産物として f-string のエラーメッセージがより正
確になり、エラーの正確な場所が含まれるようになった。

PEP 688: Making the buffer protocol accessible in Python
----------------------------------------------------------------------

メソッド ``__buffer__()`` を実装したクラスがバッファー型として使用できる。このメ
ソッドはオブジェクトに内在する記憶域を開陳するオブジェクトを返す。

このようなオブジェクトの論理的な基底型が ``collections.abc.Buffer`` だ。これは型
註釈などでバッファーオブジェクトを表現する標準的な方法を搭載している。

.. sourcecode:: python
   :caption: Example of ``collections.abc.Buffer``
   :force:

   def need_buffer(b: Buffer) -> memoryview:
       return memoryview(b)

   need_buffer(b"xy")  # ok
   need_buffer("xy")  # rejected by static type checkers

``Buffer`` はバッファー型を判定するために ``isinstance()`` と ``issubclass()``
でも使える。

独自バッファー実装例は <https://peps.python.org/pep-0688/> を見ろ。

PEP 709: Comprehension inlining
----------------------------------------------------------------------

内包記法周りが主に速度の点で強化。

Improved Error Messages
----------------------------------------------------------------------

よりわかりやすいメッセージに改良。

New Features Related to Type Hints
======================================================================

型ヒントとモジュール ``typing`` に影響する主な変更点について書いてある。

.. todo::

   * PEP 692: Using ``TypedDict`` for more precise ``**kwargs`` typing
   * PEP 698: Override Decorator for Static Typing

   どちらも難しい。

Other Language Changes
======================================================================

* ヌル文字を含むソースコードを解析すると ``SyntaxError`` が生じる。
* 有効なエスケープシーケンスではないバックスラッシュ文字のペアが生じるのは
  ``DeprecationWarning`` ではなく ``SyntaxWarning`` に変更した。正規表現を書いて
  いるときなどに出くわすかもしれない。
* :doc:`./python-3.11` であったように、数 ``0o377`` より大きな値の八進数エスケー
  プが生じる例外が ``DeprecationWarning`` から ``SyntaxWarning`` に変更した。い
  ずれエラーになる予定とのこと。
* ``try``-``except*`` 構文が ``ExceptionGroup`` 全体を処理し、他の例外を一つ発生
  させる場合、その例外は ``ExceptionGroup`` にラップされなくなった。バージョン
  3.11.4+ にもこの変更が適用された。
* 引数として ``True`` か ``False`` を期待する組み込み関数全てと拡張関数の
  callable 全てが、``bool`` と ``int`` だけでなく、任意の型の引数を受け付けるよ
  うになった。明示的に真偽値にキャストしなくて済むということだから便利だ。
* ``sum()`` で Neumaier 和を採用。浮動小数点数または ``int`` と浮動小数点数の混
  合を合計する際の精度と可換性が向上した。
  `Improve accuracy of builtin sum() for float inputs
  <https://github.com/python/cpython/issues/100425>`__ を見ろ。
* And more?

New Modules
======================================================================

何もない。

Improved Modules
======================================================================

``array``
----------------------------------------------------------------------

クラス ``array`` が添字対応し、汎用型になる。以前は ``a[0]`` などが書けなかった
ということか？

``asyncio``
----------------------------------------------------------------------

* イベントループは各プラットフォームで利用可能な最適の見張りを使用するようになっ
  た。手動で見張りを設定することは勧められない。
* ``run()`` に ``loop_factory`` 引数が追加。自家製イベントループ工場を指定可能。
* ``iscoroutine()`` は ``asyncio`` がジェネレーターベースのコルーチンを支持しな
  いため、ジェネレーターに対して ``False`` を返すように変更した。
* ``wait()`` と ``as_completed()`` はジェネレーターが ``yield`` するタスクを受け
  付けるようになった。

``calendar``
----------------------------------------------------------------------

列挙型 ``Month`` および ``Day`` が追加。一年の月と曜日を定義する。

.. sourcecode:: ipython
   :caption: ``calendar.Month`` and ``calendar.Day``

   In [1]: from calendar import Month, Day

   In [2]: Month
   Out[2]: <enum 'Month'>

   In [3]: list(Month)
   Out[3]:
   [calendar.JANUARY,
    calendar.FEBRUARY,
    calendar.MARCH,
    calendar.APRIL,
    calendar.MAY,
    calendar.JUNE,
    calendar.JULY,
    calendar.AUGUST,
    calendar.SEPTEMBER,
    calendar.OCTOBER,
    calendar.NOVEMBER,
    calendar.DECEMBER]

   In [4]: list(Day)
   Out[4]:
   [calendar.MONDAY,
    calendar.TUESDAY,
    calendar.WEDNESDAY,
    calendar.THURSDAY,
    calendar.FRIDAY,
    calendar.SATURDAY,
    calendar.SUNDAY]

.. admonition:: 利用者ノート

   月曜の値は 0 であることを確認。

``csv``
----------------------------------------------------------------------

フラグに ``QUOTE_NOTNULL`` と ``QUOTE_STRINGS`` が追加。

``QUOTE_NOTNULL``
   出力の場合、``None`` でないフィールド全てを引用符で囲む。``QUOTE_ALL`` と似て
   いるようだがフィールド値が ``None`` である場合に、空の（引用符で囲まれていな
   い）文字列を書き込むという点が異なる。空（引用符で囲まれていない）フィールド
   を ``None`` だと解釈し、それ以外は ``QUOTE_ALL`` と同じ動作をする。

   入力の場合、空の（引用符で囲まれていない）フィールドを ``None`` として解釈し、
   それ以外は ``QUOTE_ALL`` として動作する。
``QUOTE_STRINGS``
   出力の場合、文字列フィールドを常に引用符で囲む。``QUOTE_NONNUMERIC`` に似てい
   るようだが、フィールド値が ``None`` である場合に、空の（引用符で囲まれていな
   い）文字列を書き込むという点が異なる。

   入力の場合、空の（引用符で囲まれていない）文字列を ``None`` だと解釈し、それ
   以外は ``QUOTE_NONNUMERIC`` として動作する。

``fractions``
----------------------------------------------------------------------

``Fraction`` 型のオブジェクトが関数 ``format()`` などでの浮動小数点数書式に対応
した。

.. sourcecode:: ipython
   :caption: 例えば e, E, f, F, g, G, % が使える。

   In [1]: from fractions import Fraction as F

   In [2]: x = F(1, 8)

   In [3]: f'{x:.3e} {x:.3f} {x:.3g} {x:.3%}'
   Out[3]: '1.250e-01 0.125 0.125 12.500%'

``itertools``
----------------------------------------------------------------------

ジェネレーター ``batched()`` が追加。反復可能なデータを指定長の ``tuple`` に一括
する。これはコード片を見るほうが理解が早い：

.. sourcecode:: python
   :caption: ``batched()``

   def batched(iterable, n):
       # batched('ABCDEFG', 3) → ABC DEF G
       if n < 1:
           raise ValueError('n must be at least one')
       iterator = iter(iterable)
       while batch := tuple(islice(iterator, n)):
           yield batch

``math``
----------------------------------------------------------------------

関数 ``sumprod(p, q)`` 追加。ドット積。

関数 ``nextafter(x, y)`` を拡張。一度に複数のステップを上下に移動するための
``steps`` 引数を追加。拡張動機はこういうコードを書かざるを得なかったことがあった
かららしい：

.. sourcecode:: python

   x = nextafter(nextafter(nextafter(x, inf), inf), inf)

``os``, ``os.path``
----------------------------------------------------------------------

Windows に関係する新機能が多いようなので割愛。

``pathlib``
----------------------------------------------------------------------

ディレクトリー木を走査し、その中のファイルまたはディレクトリーすべての名前を生成
するためのメソッド ``walk()`` がクラス ``Path`` に追加した。動作は関数
``os.walk()`` と同様。

``PurePath.relative_to()`` に ``walk_up`` オプション引数が追加。結果に ``..`` が
入ることが許される。この動作は関数 ``os.path.relpath()`` と整合する。

.. sourcecode:: ipython
   :caption: ``p.relative_to(other, walk_up=True)``

   In [1]: from pathlib import PurePosixPath

   In [2]: p = PurePosixPath('/etc/passwd')

   In [3]: p.relative_to('/usr', walk_up=True)
   Out[3]: PurePosixPath('../etc/passwd')

``pdb``
----------------------------------------------------------------------

デバッグセッションのために一時的に値を保持し、現在のフレームや戻り値のような値に
素早くアクセスできる簡易変数が追加。

一時的なグローバル変数を設定するには、例えば、``$foo = 1`` とすると、デバッガー
セッションで使用できるグローバル変数 ``$foo`` を設定する。簡易変数はプログラムの
実行が再開されると消去されるので、``foo = 1`` のような通常の変数を使う場合に比べ
てプログラムに支障をきたす可能性は低くなる。

簡易変数が三つ、あらかじめ用意されている：

.. csv-table::
   :delim: @
   :header-rows: 1
   :widths: auto

   簡易変数 @ 意味
   ``$_frame`` @ デバッグしている現在のフレーム
   ``$_retval`` @ フレームが return している場合、その戻り値
   ``$_exception`` @ フレームが例外を raise している場合、その例外

``random``
----------------------------------------------------------------------

二項分布 ``binomialvariate(n=1, p=0.5)`` 追加。各試行での成功確率を ``p`` とし、
独立した ``n`` 回の試行の成功回数を返す。

指数分布 ``expovariate()`` に既定引数 ``lambd=1.0`` が追加。

``shutil``
----------------------------------------------------------------------

``rmtree()`` に引数 ``onexc`` が追加。これは ``onerror`` のようなエラーハンド
ラーであるが、例外オブジェクトを受け取るものだ。

``sqlite3``
----------------------------------------------------------------------

なんと CLI が実装された。

.. sourcecode:: console

   $ python -m sqlite3
   sqlite3 shell, running on SQLite version 3.45.3
   Connected to a transient in-memory database

   Each command will be run using execute() on the cursor.
   Type ".help" for more information; type ".quit" or CTRL-D to quit.
   sqlite>

``statistics``
----------------------------------------------------------------------

関数 ``correlation()`` が拡張。ランク付けされたデータの Spearman 相関を計算する
メソッド ``ranked`` を追加： ``correlation(x, y, method='ranked')``.

``sys``
----------------------------------------------------------------------

今回は割愛。

``tempfile``
----------------------------------------------------------------------

関数 ``mkdtemp(suffix=None, prefix=None, dir=None)`` は ``dir`` 引数が相対パスで
あっても、絶対パスを常に返す。

``typing``
----------------------------------------------------------------------

.. todo::

   例によって難しいから後にする。

``unicodedata``
----------------------------------------------------------------------

Unicode データベースがバージョン `15.0.0
<https://www.unicode.org/versions/Unicode15.0.0/>`__ に更新した。

.. admonition:: 読者ノート

   個人的には使いたい文字がないので軽視する。

``unittest``
----------------------------------------------------------------------

コマンドラインオプション :samp:`--durations={N}` は最も遅いテストケース `N` 個を
示す。

``uuid``
----------------------------------------------------------------------

.. sourcecode:: console
   :caption: ``uuid`` CLI

   $ python -m uuid
   8cb09e58-2154-4b36-9bea-2806403d956e

.. admonition:: 読者ノート

   これは使う可能性が高いから忘れないでおく。

Optimizations
======================================================================

ここは一般プログラマーには重要ではないかもしれない。ほとんどチェックしていない。

Deprecated
======================================================================

古いやり方をいつまで経っても採用し続けないように、一通りチェックする。

定数 ``calendar.January`` および ``calendar.February`` が咎められる。それぞれ列
挙型メンバー ``calendar.JANUARY`` および ``calendar.FEBRUARY`` に置き換えろ。

クラス ``datetime.datetime`` で ``utcnow()`` と ``utcfromtimestamp()`` は将来の
バージョンで削除される予定。代わりに：

.. sourcecode:: ipython

   In [1]: from datetime import datetime, timezone

   In [2]: datetime.now(timezone.utc)
   Out[2]: datetime.datetime(2024, 9, 26, 2, 26, 26, 338492, tzinfo=datetime.timezone.utc)

   In [3]: import time

   In [4]: datetime.fromtimestamp(time.time(), timezone.utc)
   Out[4]: datetime.datetime(2024, 9, 26, 2, 28, 47, 722403, tzinfo=datetime.timezone.utc)

関数 ``suhtil.rmtree()`` の ``onerror`` 引数。代わりに ``onexc`` 引数を使え。

``sys.last_type``, ``sys.last_value``, ``sys.last_traceback`` は咎められる。代わ
りに ``sys.last_exc`` を使え。

``typing.``

``typing.Hashable`` と ``typing.Sized`` はそれぞれ ``collections.abc.Hashable``
と ``collections.abc.Sized`` の別名だった。

Python 3.9 から使用を咎められる ``typing.ByteString`` は、使用時に
``DeprecationWarning`` を送出する。

次の非同期系送出関数。それぞれの単一引数版を使え：

* ``coroutine.throw(type[, value[, traceback]])``
* ``generator.throw(type[, value[, traceback]])``
* ``coroutine agen.athrow(type[, value[, traceback]])``

``bool`` 値に対するビット反転演算子。Python 3.16 からはエラー。代わりに演算子
``not`` を使え。

.. admonition:: 読者ノート

   ``~True`` と ``~False`` の値がそれぞれ ``-2``, ``-1`` になる。

Removed
======================================================================

``configparser``
----------------------------------------------------------------------

``ParsingError`` から ``filename`` 属性・引数がなくなった。代えて ``source`` 属
性・引数を使え。

クラス ``SafeConfigParser`` はもはや存在しない。代わりに、より短い名前
``ConfigParser`` を使え。

クラス ``ConfigParser`` からメソッド ``readfp()`` が消えた。代わりに
``read_file()`` を使え。

.. admonition:: 読者ノート

   手許のコードを確認したが、影響はないようだ。

``distutils``
----------------------------------------------------------------------

パッケージ全体が削除された。

``unittest``
----------------------------------------------------------------------

クラス ``TestCase`` のかなりのメソッド別名が取り除かれた。量が多いのでいちいち確
認するしかないが、例えば ``assertEquals()`` は ``assertEqual()`` と改めろ。

テストコードが古い場合、道具を使って置換するといい：
<https://github.com/isidentical/teyit>

Porting to Python 3.12
======================================================================

本節以降、個人的には対応項目なし。

Changes in the Python API
----------------------------------------------------------------------

正規表現における数値グループ参照とグループ名に対して、数値参照として受け入れられ
るのは ASCII 数字の並びだけになった。<https://github.com/python/cpython/issues/91760>
参照。

関数 ``random.randrange()`` で、実引数が正の整数としては怪しい値 (e.g. 10.2) だ
と ``TypeError`` を送出するようになった。

----

興味がある項目は以上？
