======================================================================
What's New In Python 3.10 ノート
======================================================================

`What's New In Python 3.10 <https://docs.python.org/3/whatsnew/3.10.html>`__ を
たどりながら調査。興味のあるものしか読まない。

.. contents:: ノート目次

New Features
======================================================================

Parenthesized context managers
----------------------------------------------------------------------

複数行にまたがる継続のための囲み括弧の使用が対応されている。``import`` 文でよく
やるような記法で、複数行に及ぶ長いコンテクストマネージャーの集まりをまとめること
ができる。以下の例はすべて有効だ。

.. code:: python

   with (CtxManager() as example):
       ...

   with (
       CtxManager1(),
       CtxManager2()
   ):
       ...

   with (CtxManager1() as example,
         CtxManager2()):
       ...

   with (CtxManager1(),
         CtxManager2() as example):
       ...

   with (
       CtxManager1() as example1,
       CtxManager2() as example2
   ):
       ...

なお、括弧内に列挙する最後の記述の末尾にカンマが付いていてもよい。

Better error messages
----------------------------------------------------------------------

Python が閉じない括弧を含むコードを解析する場合、解析中に
``SyntaxError: unexpected EOF`` を表示したり、不正な場所を指すのではなく、閉じな
い括弧の位置も含めるようになっている。

同様に、閉じられていない文字列リテラル（シングルクォートとトリプルクォート）を含
むエラーは、EOF/EOL を報告するのではなく、その文字列の開始を指すようになってい
る。

``SyntaxError`` に特化したメッセージが多数追加。詳しくは公式文書を読むといい。と
にかく、一般プログラマーの作業効率が上がったと思っていい。

PEP 634: Structural Pattern Matching
----------------------------------------------------------------------

よその言語でいう switch 文が追加されている。これは説明するのが難しい。公式文書か
ら構文とコード例を引用しておく。

構文は次のように `match-statement` と `case-statement` からなる。

.. code:: text

   match subject:
       case <pattern_1>:
           <action_1>
       case <pattern_2>:
           <action_2>
       case <pattern_3>:
           <action_3>
       case _:
           <action_wildcard>

Simple pattern: match to a literal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

次の例は想像どおりの意味だ。最後の ``case _`` がワイルドカードアクションだ。この
`case-statement` を配置するのはオプショナルだ。その場合 `match-statement` に該当
する `case-statement` が存在しなければ、文全体として `no-op` になる。

.. code:: python

   def http_error(status):
       match status:
           case 400:
               return "Bad request"
           case 404:
               return "Not found"
           case 418:
               return "I'm a teapot"
           case _:
               return "Something's wrong with the internet"

`case-statement` がリテラル式の場合、パイプ記号で選言にすることができる。

.. code:: python

   case 401 | 403 | 404:
      return "Not allowed"

Patterns with a literal and variable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

次の例は変数への代入をする `case-statement` を含む。

.. code:: python

   # point is an (x, y) tuple
   match point:
       case (0, 0):
           print("Origin")
       case (0, y):
           print(f"Y={y}")
       case (x, 0):
           print(f"X={x}")
       case (x, y):
           print(f"X={x}, Y={y}")
       case _:
           raise ValueError("Not a point")

Patterns and classes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

クラスを使ってデータを構成する場合、クラス名の後にコンストラクターのような引数リ
ストが続くパターンを使うことができる。このパターンには、クラスの属性を変数に取り
込む機能がある。

.. code:: python

   class Point:
       x: int
       y: int

   def location(point):
       match point:
           case Point(x=0, y=0):
               print("Origin is the point's location.")
           case Point(x=0, y=y):
               print(f"Y={y} and the point is on the y-axis.")
           case Point(x=x, y=0):
               print(f"X={x} and the point is on the x-axis.")
           case Point():
               print("The point is located somewhere else on the plane.")
           case _:
               print("Not a point")

Patterns with positional parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

位置パラメーターは、例えば ``dataclass`` のような、その属性の順序を提供する組み
込みクラスのいくつかで使用できる。また、クラスで ``__match_args__`` 特殊属性を設
定することにより、パターン内の属性の特定の位置を定義することができる。これを
``("x", "y")`` とすると、以下のパターンはすべて同値だ。すべて属性 ``y`` を変数
``var`` に束縛する。

.. code:: python

   Point(1, var)
   Point(1, y=var)
   Point(x=1, y=var)
   Point(y=var, x=1)

Nested patterns
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

パターンを好きなだけ入れ子にしてよい。例えば、データが短い点のリストである場合、
次の `match-statement` はいずれかにマッチする。

.. code:: python

   match points:
       case []:
           print("No points in the list.")
       case [Point(0, 0)]:
           print("The origin is the only point in the list.")
       case [Point(x, y)]:
           print(f"A single point {x}, {y} is in the list.")
       case [Point(0, y1), Point(0, y2)]:
           print(f"Two points on the Y axis at {y1}, {y2} are in the list.")
       case _:
           print("Something else is found in the list.")

Complex patterns and the wildcard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

複雑なパターンとワイルドカードを組み合わせることもできる。例えば次の例では
``test_available`` は ``('error', code, 100)`` にも ``('error', code, 800)`` に
もマッチする。

.. code:: python

   match test_variable:
       case ('warning', code, 40):
           print("A warning has been received.")
       case ('error', code, _):
           print(f"An error {code} occurred.")

Guard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ガードと呼ばれる ``if`` 節を追加することができる。ガードが偽の場合に ``match``
は次の ``case`` ブロックを試みる。値の取り込みはガードが評価される前に行われるこ
とに注意。

.. code:: python

   match point:
       case Point(x, y) if x == y:
           print(f"The point is located on the diagonal Y=X at {x}.")
       case Point(x, y):
           print(f"Point is not on the diagonal.")

Other Key Features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* 前述のコード例で ``list`` を使っている箇所では ``tuple`` も全く同じ意味を持
  ち、実際には任意のシーケンスにマッチする。技術的には、対象はシーケンスである必
  要がある。パターンはイテレーターにマッチしない。また、よくある間違いを防ぐため
  に、シーケンスパターンは文字列にはマッチしない。
* シーケンスパターンはワイルドカードに対応している。:code:`[x, y, *rest]` と
  :code:`(x, y, *rest)` は unpacking 代入のワイルドカードと同様に機能する。
  ``*`` の後の名前は ``_`` にもなり、それゆえ :code:`(x, y, *_)` は少なくとも二
  つの項目のシーケンスにマッチし、残りの項目は束縛されない。
* 写像のパターン。:code:`{"bandwidth": b, "latency": l}` は ``dict`` から値
  ``"bandwidth"`` および ``"latency"`` を取る。シーケンスパターンとは異なり、余
  分なキーは無視される。ワイルドカードの ``**rest`` も対応されている。ただし、
  ``**_`` は冗長になるため、使用を認められない。
* 部分パターンはキーワード ``as`` を使って捕捉してよい：

  .. code:: python

     case (Point(x1, y1), Point(x2, y2) as p2): ...

  これは ``as`` 節がなかったとしても期待通りに ``x1``, ``y1``, ``x2``, ``y2`` を
  束縛し、``p2`` は ``match`` 文の二番目の項目全体を束縛する。
* ほとんどのリテラルは等号で比較される。``True``, ``False``, ``None`` は同一性
  によって比較される。
* 名前付き定数はをパターン内で使用してもよい。定数が捕捉変数として解釈されるのを
  防ぐために、ドット付きの名前にする必要がある。

  .. code:: python

     from enum import Enum
     class Color(Enum):
         RED = 0
         GREEN = 1
         BLUE = 2

     match color:
         case Color.RED:
             print("I see red!")
         case Color.GREEN:
             print("Grass is green")
         case Color.BLUE:
             print("I'm feeling the blues :(")

Optional EncodingWarning and ``encoding="locale"`` option
----------------------------------------------------------------------

``TextIOWrapper`` と ``open()`` の既定のエンコーディングはプラットフォームとロ
ケールに依存する。ほとんどの UNIX プラットフォームでは UTF-8 が使われているの
で、 UTF-8 ファイルを開くときにエンコードオプションを省略すると、ひじょうにあり
ふれたバグになる。

このようなバグを発見するために例外 ``EncodingWarning`` が加わっている。これは
``sys.flags.warn_default_encoding`` が真で、ロケール固有の既定のエンコーディング
が使われたときに送出される。

警告を有効にするために、オプション ``-X warn_default_encoding`` と環境変数
``PYTHONWARNDEFAULTENCODING`` が加わっている。

New Features Related to Type Hints
======================================================================

型ヒントとモジュール ``typing`` に影響する主な変更点について書いてある。興味がほ
とんどないので、最初の節だけノートに取る。

PEP 604: New Type Union Operator
----------------------------------------------------------------------

型において、``typing.Union`` を使う代わりに、型 ``X`` か ``Y`` のどちらかを表現
する、よりきれいな方法が用意されている。

以前のバージョンの Python では、複数の型の引数を受け取る関数に対して型ヒントを適
用するのに ``typing.Union`` が使われていた。

.. code:: python

   def square(number: Union[int, float]) -> Union[int, float]:
       return number ** 2

この型ヒントをより簡潔なやり方で書ける：

.. code:: python

   def square(number: int | float) -> int | float:
       return number ** 2

この新しい構文は ``isinstance()`` および ``issubclass()`` の第ニ引数としても受け
入れられる。

.. code:: pycon

   >>> isinstance(1, int | str)
   True

Other Language Changes
======================================================================

興味のある変更だけ記す。

* 型 ``int`` にメソッド ``bit_count()`` が追加。整数値の二進数表示に立っている
  ビットの個数を返す。
* 整数の引数を取る組み込み関数および拡張関数は、``Decimal`` や ``Fraction`` な
  ど、損失を承知の上で整数に変換できるオブジェクト（例えば ``__int__()`` メソッ
  ドを持つが ``__index__()`` メソッドを持たない）を受け付けないように変更されて
  いる。
* ``object.__ipow__()`` が ``NotImplemented`` を返す場合、この演算子は期待通りに
  ``object.__pow__()`` と ``object.__rpow__()`` に正しく fall back されるように
  なっている。
* 代入式は ``set`` リテラルや ``set`` 内包、シーケンスインデックス内で、括弧に括
  らなくても使用できるようになっている。
* 静的メソッドとクラスメソッドはメソッド属性 (``__module__``, ``__name__``,
  ``__qualname__``, ``__doc__``, ``__annotations__``) を継承し、新しい属性
  ``__wrapped__`` を持つようになった。さらに、静的メソッドは通常の関数として呼び
  出すことができるようになっている。
* ``float`` 型と ``decimal.Decimal`` 型の ``NaN`` 値のハッシュが、オブジェクトの
  同一性に依存するようになる。以前は ``NaN`` 値が互いに等しくないにもかかわら
  ず、常に 0 にハッシュされていた。このため、複数の ``NaN`` を含む ``dict`` や
  ``set`` を作成する際に、ハッシュの衝突が多発し、実行時の動作が二次のオーダーに
  なる可能性があった。
* 定数 ``__debug__`` を削除すると ``NameError`` ではなく ``SyntaxError`` が発生
  する。
* 例外 ``SyntaxError`` に属性 ``end_lineno`` と ``end_offset`` が追加。これら
  は、確定されない場合は ``None`` になる。

New Modules
======================================================================

何もない。

Improved Modules
======================================================================

興味のあるものや遭遇しそうな問題を含むモジュールに絞って記していく。

``argparse``
----------------------------------------------------------------------

オプション ``--help`` で出力されるメッセージ中の optional arguments という言葉が
options に置き換わっている。もしヘルプメッセージのテストがあるならば、何らかの対
応が必要だろう。

``array``
----------------------------------------------------------------------

メソッド ``array.index()`` にオプショナル引数 ``start`` と ``stop`` が追加されて
いる。まだ試していないが、これらは文字列やシーケンスの対応物と同じ意味だろう。

``bdb``
----------------------------------------------------------------------

関数 ``clearBreakpoints()`` が追加されている。ブレイクポイントすべてをリセットする。
これはデバッグの利便性が上がる。

``bisect``
----------------------------------------------------------------------

モジュール内の関数にオプショナル ``key`` 引数が追加されている。これはキー関数、
つまり照合関数を指定するものだ。

キー関数とはソート、順序付けに使用する値を返す callable だ。

``contextlib``
----------------------------------------------------------------------

コンテキストマネージャー ``contextlib.aclosing()`` が追加されている。これを、非
同期ジェネレーターや非同期的に解放されたリソースを表すオブジェクトを安全に閉じる
ために用いる。

非同期コンテキストマネージャー対応が ``contextlib.nullcontext()`` に追加されてい
る。

``AsyncContextDecorator`` が追加。デコレーターとしての非同期コンテキストマネー
ジャーの使用を対応している。

``dataclasses``
----------------------------------------------------------------------

``__slots__``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``dataclasses.dataclass()`` デコレーターに ``slots`` 引数が追加されている。

Keyword-only fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``dataclasses`` は、生成された ``__init__`` メソッドでキーワードのみのフィールド
を対応している。

.. code:: python

   from dataclasses import dataclass

   # Both name and birthday are keyword-only parameters to the generated __init__ method.
   @dataclass(kw_only=True)
   class Birthday:
       name: str
       birthday: datetime.date

.. code:: python

   from dataclasses import dataclass

   # Here only birthday is keyword-only.
   @dataclass
   class Birthday:
       name: str
       birthday: datetime.date = field(kw_only=True)

個々のフィールドに ``kw_only`` を設定する場合、keyword-only フィールドが非
keyword-only フィールドに続く必要があるため、フィールドの再順序付けに関する規則
があることに注意が要る。

また、``KW_ONLY`` マーカーに続くフィールドすべてが keyword-only であることを指定
することもできる。これがおそらく最もふつうの使用法だろう。

.. code:: python

   from dataclasses import dataclass, KW_ONLY

   # Here, z and t are keyword-only parameters, while x and y are not.
   @dataclass
   class Point:
       x: float
       y: float
       _: KW_ONLY
       z: float = 0.0
       t: float = 0.0

``distutils``
----------------------------------------------------------------------

パッケージ ``distutils`` 全体は Python 3.12 で削除され、非推奨となる。

Python 3.8 で非推奨となった :command:`bdist_wininst` コマンドは削除されている。
Windows でバイナリーパッケージを配布するには :command:`bdist_wheel` コマンドが推
奨される。

``encodings``
----------------------------------------------------------------------

``encodings.normalize_encoding()`` は非 ASCII 文字を無視する。

``fileinput``
----------------------------------------------------------------------

``fileinput.input()`` と ``fileinput.FileInput`` に引数 ``endoocing`` と
``errors`` が追加されている。

``fileinput.hook_compressed()`` がモード ``"r"`` で圧縮されている場合、非圧縮
ファイルのように ``TextIOWrapper`` オブジェクトを返すようになっている。

``glob``
----------------------------------------------------------------------

``glob()`` および ``iglob()`` に、検索対象のルートディレクトリーを指定するための
引数 ``root_dir`` および ``dir_fd`` が追加されている。

``os.path``
----------------------------------------------------------------------

関数 ``os.path.realpath()`` は、キーワードのみ引数 ``strict`` を受け付ける。この
値を ``True`` として呼び出すと、指定パスが存在しないか、シンボリックリンクのルー
プに遭遇した場合に ``OSError`` が発生する。

``pathlib``
----------------------------------------------------------------------

``PurePath.parents`` が ``slice`` に対応している。

``PurePath.parents`` が負のインデックスに対応している。

メソッド ``link_to()`` を置き換える ``Path.hardlink_to`` が追加されている。この
新しいメソッドには ``symlink_to()`` と同じ引数順序がある。

``pathlib.Path.stat()`` と ``chmod()`` は、キーワードのみ引数
``follow_symlinks`` を受け入れる。モジュール ``os`` における、対応する関数との一
貫性のためにそうなっている。

``pprint``
----------------------------------------------------------------------

関数 ``pprint.pprint()`` は新キーワード引数 ``underscore_numbers`` を受け付け
る。

``dataclasses.dataclass`` インスタンスを pretty-print できる。

``statistics``
----------------------------------------------------------------------

関数 ``covarianve()``, ``correlation()``, ``linear_regression()`` が追加されてい
る。それぞれ共分散、Pearson 相関係数、単純な線形回帰を求める。

``sys``
----------------------------------------------------------------------

``sys.orig_argv`` が追加されている。Python 実行形式に渡されるオリジナルのコマン
ドライン引数のリストだ。

``sys.stdlib_module_names`` が追加されている。標準ライブラリーモジュール名のリス
トを含む。

``typing``
----------------------------------------------------------------------

主な変更点は先述の New Features Related to Type Hints で述べられている。以降の変
更ノートはそれを踏まえてのものになる。

PEP 586 で指定された静的型チェッカーの動作と一致するように ``typing.Literal``
の振る舞いが変更されている。

``Literal`` は引数の重複を解消するようになっている。

``Literal`` オブジェクト間の等価比較は、順序に依存しないようなっている。

``Literal`` の比較は、型を考慮するようになっている。たとえば、
:code:`Literal[0] == Literal[False]` は以前は ``True`` と評価されていた。これが
現在は ``False`` となる。この変更に対応するために、内部で使用する型キャッシュが
型の区別に対応できるようになっている。

``Literal`` オブジェクトは、その引数のいずれかがハッシュ化不能の場合、等値比較時
に ``TypeError`` 例外が発生するようになっている。ただし、ハッシュ化不能引数を持
つ ``Literal`` を宣言してもエラーは発生しない。

.. code:: pycon

   >>> from typing import Literal
   >>> Literal[{0}]
   >>> Literal[{0}] == Literal[{False}]
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: unhashable type: 'set'

その他。

``unittest``
----------------------------------------------------------------------

既存の ``assertLogs()`` を補完するメソッド ``assertNoLogs()`` が新しく追加されて
いる。

``urllib.parse``
----------------------------------------------------------------------

Python 3.10 より早いバージョンでは ``urllib.parse.parse_qs()`` および
``urllib.parse.parse_qsl()`` で問い合わせ引数のセパレーターとして ``;`` と ``&``
の両方を使用することができた。これが 3.10 では単一のセパレータキーだけを許可する
ように変更されており、既定値は ``&`` となっている。この変更は ``cgi.parse()``お
よび ``cgi.parse_multipart()`` にも影響する。

URL の一部に改行文字やタブ文字があると、ある種の攻撃が可能になる。WHATWG 仕様に
従い、ASCII の改行文字 ``\n``, ``\r`` とタブ文字 ``\t`` を ``urllib.parse`` の解
析器が URL から取り除いて、このような攻撃を防ぐようにしてある。除去される文字
は、新しいモジュールレベル変数 ``urllib.parse._UNSAFE_URL_BYTES_TO_REMOVE`` が制
御する。

Optimizations
======================================================================

ここは一般プログラマーには重要ではないかもしれない。ほとんどチェックしていない。

* ``str()``, ``bytes()``, ``bytearray()`` の各コンストラクターが高速化。小さいオ
  ブジェクトでは約 30 から 40 パーセント。
* :command:`python3 -m module-name` コマンドの起動時間が平均で 1.4 倍速くなって
  いる。Linux ではこのコマンド実行は Python 3.9 で 69 モジュールを ``import``
  しているが、Python 3.10 では 51 モジュールしか ``import`` しない。
* ``str1 in str2`` や ``str2.find(str1)`` などの部分文字列検索関数で、長い文字列
  での二次のオーダーである何らかのコストを避けるために Crochemore & Perrin の
  Two-Way 文字列検索アルゴリズムを（可能ならば？）使用するようになっている。
* 以下の組み込み関数が、より高速な PEP 590 vectorcall 呼び出しに対応した

  * ``map()``
  * ``filter()``
  * ``reversed()``
  * ``bool()``
  * ``float()``

Deprecated
======================================================================

古いやり方をいつまで経っても採用し続けないように、一通りチェックする。

* 先述のように ``distutils`` 名前空間。Python 3.12 で削除。
* ``random.randrange()`` の非整数型引数。
* ``asyncio.get_event_loop()`` は、実行中のイベントループがない場合、非推奨の警
  告を発する。将来的には ``get_running_loop()`` の別名になる。暗黙的に
  ``Future`` または ``Task`` オブジェクトを生成する次に示す ``asyncio`` 関数は、
  実行中のイベントループがなく、明示的な引数 ``loop`` が渡されない場合に非推奨警
  告を発する：

  * ``ensure_future()``
  * ``wrap_future()``
  * ``gather()``
  * ``shield()``
  * ``as_completed()``
  * ``Future``, ``Task,``, ``StreamReader``, ``StreamReaderProtocol`` 各コンスト
    ラクター

* 以下の ``threading`` メソッド：

  * ``threading.currentThread`` → ``threading.current_thread()``
  * ``threading.activeCount`` → ``threading.active_count()``
  * ``threading.Condition.notifyAll`` → ``threading.Condition.notify_all()``
  * ``threading.Event.isSet`` → ``threading.Event.is_set()``
  * ``threading.Thread.setName`` → ``threading.Thread.name``
  * ``threading.thread.getName`` → ``threading.Thread.name``
  * ``threading.Thread.isDaemon`` → ``threading.Thread.daemon``
  * ``threading.Thread.setDaemon`` → ``threading.Thread.daemon``

Removed
======================================================================

興味のあるものしかチェックしない。

* クラス ``complex`` にあった特殊メソッド ``__int__``, ``__float__``,
  ``__floordiv__``, ``__mod__``, ``__divmod__``, ``__rfloordiv__``,
  ``__rmod__``, ``__rdivmod__``.
* モジュール ``collections`` にあった Abstract Base Classe コレクションへの非推
  奨の別名。
* ``asyncio`` の高水準 API の大部分から Python 3.8 で非推奨となった引数
  ``loop``. この変更の背景にある動機：

  * 高水準 API を単純化する。
  * Python 3.7 以降、高水準 API の関数は暗黙のうちに現在のスレッドの実行中のイベ
    ントループを取得してきた。通常の使用状況のほとんどは、API にイベントループを
    渡す必要はない。
  * イベントループの受け渡しは、特に異なるスレッドで実行されているループを扱うと
    きにエラーが発生しやすい。

  低水準 API は ``loop`` をまだ受け入れることに注意。

Porting to Python 3.10
======================================================================

本節以降、個人的には対応項目なし。
