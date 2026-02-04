================================================================================
What's New In Python 3.14 ノート
================================================================================

`What's New In Python 3.14 <https://docs.python.org/3/whatsnew/3.14.html>`__ を
たどりながら調査。興味のあるものしか読まない。

.. contents:: 見出し一覧
   :local:

New features
================================================================================

PEP 750: Template string literals
--------------------------------------------------------------------------------

| A template string literal or t-string is a string literal that is prefixed
| with ‘t’ or ‘T’. These strings follow the same syntax rules as formatted
| string literals. (2.5.8 t-strings)

定義方法や書式・変換指定は従来の f-string と同様だが、この形式で定義した文字列は
実は文字列ではなく ``string.templatelib.TemplateString`` オブジェクトになる。

* `string.templatelib — Support for template string literals <https://docs.python.org/3/library/string.templatelib.html>`__

| Templates provide developers with access to the string and its interpolated
| values before they are combined. This brings native flexible string processing
| to the Python language and enables safety checks, web templating,
| domain-specific languages, and more. (PEP 750)

コードを見るほうが理解が早い：

.. sourcecode:: python
   :caption: t-string の基本性質を簡単に示すコード片
   :force:

   name = "World"
   t = t"Hello {name}"

   assert t.strings[0] == "Hello "
   assert t.interpolations[0].value == "World"
   assert t.interpolations[0].expression == "name"

   contents = list(t)
   assert len(contents) == 2
   assert contents[0] == "Hello "
   assert contents[1].value == "World"
   assert contents[1].expression == "name"

ここまで試して気付いたが、オブジェクトの最終形を普通の文字列として一発で出力する
方法が用意されていない。それがこの新型クラスの狙いでもあるようだ。ユーザー入力を
検証する処理と文字列を組み立てる処理が一体化したものをプログラマーが定義するのだ。

Improved error messages
--------------------------------------------------------------------------------

インタプリターからの ``SyntaxError`` メッセージがわかりやすくなった。

* インタプリターが Python キーワードに酷似した単語を検出すると、エラーメッセージ
  内で正しいキーワードを提案する。
* ``else`` 節に続く ``elif`` 文に対しては専用のエラーメッセージが表示される。
* 三項演算子の ``else`` 後の条件式に文が渡されたり、``if`` の前に ``pass``,
  ``break``, ``continue`` のいずれかが渡されたりした場合、式が必要な箇所をエラー
  メッセージ中で強調表示する。
* 不正に閉じられた文字列が検出された場合、エラーメッセージがその文字列が意図的に
  文字列の部分であるかもしれないことを示唆する。
* 文字列の接頭辞が複数付いていてそれらに互換性がない場合のエラーメッセージ
* 次のような ``as`` に関係するエラーメッセージ：

  * ``import ... as ...``
  * ``from ... import ... as ...``
  * ``except ... as ...``
  * ``case ... as ...``
* ハッシュ化できない型のオブジェクトを ``dict`` や ``set`` に追加しようとした際
  のエラーメッセージ
* 句 ``async with`` が適切な場所で ``with`` を指定した場合、またはその反対の指定
  を行った場合のエラーメッセージ

Asyncio introspection capabilities
--------------------------------------------------------------------------------

モジュール ``asyncio`` に CLI が搭載された。コマンドは ``ps`` と ``pstree`` の二
つある。どちらもプロセスを ID の値で指定して、実行中の ``asyncio`` タスクに関す
る情報を標準出力に示すものだ。

この機能は長時間実行される、または停止した非同期プログラムの調査に有用だ。

タスクの情報は次で構成される：

* タスクの名前
* タスクのコルーチンスタック
* タスクを待機しているタスクの集合

コマンド ``ps`` と ``pstree`` はこの情報を表形式と、非同期呼び出し関係に関する木
形式でそれぞれ出力する。

引数はプロセス ID 一個のみだ。オプションは ``-h, --help`` しかない。

.. todo::

   可能ならば、長時間実行の非同期プログラムを走らせて、コマンド
   ``python -m asyncio pstree`` の実際の出力をここに記したい。

Other language changes
================================================================================

* 複素数の値に対して inf と nan を複合させた演算結果が C++11 におけるそれと適合
  するようになった。
* Python の最適化オプション ``-O`` 絡みの ``SyntaxError`` 検出精度が上がった。

Built-ins
--------------------------------------------------------------------------------

* メソッド ``fromhex()`` の機能向上。クラス ``bytes`` と ``bytearray`` のこれら
  のメソッドは、引数として ASCII ``bytes`` 値（実質的には ASCII 文字列値）や
  ``bytes`` 風オブジェクトを受け容れる。
* クラスメソッド ``from_number()`` の追加。クラス ``float`` と ``complex`` に対
  してこのメソッドが追加した。与える引数は実数でなければならない。コンストラク
  ターのように扱いたい。
* 文字列書式における浮動小数点表示形式の端数部分で、千の位区切り記号として ``_``
  と ``,`` を用いることが許される。例えば ``format(123456.123456, '_._f')`` がエ
  ラーでなくなった。
* 関数 ``int()`` は ``__trunc__()`` を呼び出さない。整数に変換したいクラスは次の
  いずれかを実装することが不可欠になった：

  * ``__int__()``
  * ``__index__()``
* 関数 ``map()`` にキーワード専用引数 ``strict`` が追加。関数 ``zip()`` のそれと
  同じ仕様だ。
* クラス ``memoryview`` が generic になった。つまり、型注釈を付けるときに何の型
  の器なのかを示せるようになった。
* ブール値の文脈で ``NotImplemented`` を使用すると ``TypeError`` が発生するよう
  になった。

   >>> if NotImplemented:
   ...     pass
   ...
   Traceback (most recent call last):
     File "<python-input-18>", line 1, in <module>
       if NotImplemented:
          ^^^^^^^^^^^^^^
   TypeError: NotImplemented should not be used in a boolean context
* 三引数 ``pow()`` は必要に応じて ``__rpow__()`` を試みるようになった。
* ``super`` オブジェクトはコピー可能かつ pickle 可能になった。

Command line and environment
--------------------------------------------------------------------------------

コマンド ``python -c`` が実行前にコード引数のインデントを自動的に解除するように
なった（コード文字列の各行から共通の先頭空白が取り除かれ、実行される）。

PEP 758: Allow ``except`` and ``except*`` expressions without brackets
--------------------------------------------------------------------------------

``except`` / ``except*`` 式のどちらにおいても、``as`` 句が使用されていないような
場合に、例外型を列挙するときに欠かせなかった囲む括弧が省略可能になった（もちろん
囲んでもかまわない）。PEP 758 から例を引用する：

.. sourcecode:: python
   :caption: PEP 758 より
   :force:

   try:
       ...
   except ExceptionA, ExceptionB, ExceptionC:
       ...

捕捉する例外に名前を付ける場合には括弧が必須であるのは変わらない理由は、試しに上
のコードに括弧を加えぬままに ``as e`` を付けて、じっと眺めていればわかる。

PEP 765: Control flow in finally blocks
--------------------------------------------------------------------------------

例外処理の ``finally`` 節が次の文を含むとき、それは ``SyntaxWarning`` を生じるよ
うになった：

* ``break``
* ``continue``
* ``return``

というのは、そのようなコードを書いて実際にこのような制御文が実行される場合、例外
が再送出されない、つまり、例外が失われるという言語仕様があるのだ。

.. sourcecode:: pycon
   :caption: PEP 765 を Python 3.14 で検証する例
   :force:

   >>> def test_control_flow_in_finally_block():
   ...     try:
   ...         raise ValueError
   ...     finally:
   ...         return 1
   ...     return 0
   ...
   <python-input-0>:5: SyntaxWarning: 'return' in a 'finally' block
   >>> test_control_flow_in_finally_block()
   1

Default interactive shell
--------------------------------------------------------------------------------

対話型シェルで Python 構文の強調表示がなされるようになった。オフにしたい場合には
環境変数 :envvar:`PYTHON_BASIC_REPL` を定義しろ。

.. note::

   この環境変数を定義しなくても、Python はよそで用いられる次の環境変数を考慮して
   強調表示をやめる：

   * :envvar:`TERM`
   * :envvar:`NO_COLOR`
   * :envvar:`FORCE_COLOR`

さらに対話型シェルは ``import`` 文における自動補完を応援するようになった。例：

* ``import co`` までタイプして :kbd:`Tab` を押すと、名前の先頭が ``co`` から始ま
  るモジュール一覧が候補として示される。
* ``from concurrent import i`` までタイプして :kbd:`Tab` を押すと、標準モジュー
  ル ``concurrent`` のサブモジュールであって、名前の先頭が ``i`` で始まるものの
  一覧が候補として示される。

New modules
================================================================================

``annotationlib``
   次の注釈用の道具を含むモジュール：

   * 関数 ``get_annotations()``
   * 書式設定に用いる列挙型
   * クラス ``ForwardRef``
   * 関数 ``__annotate__`` を呼び出すための補助関数
``compression``
   圧縮関連モジュール用のパッケージ。Zstandard 圧縮形式を使用することが可能にな
   る新モジュールを含む。

   次の既存＆新圧縮アルゴリズム搭載標準モジュール群を含む：

   * ``bz2``
   * ``gzip``
   * ``lzma``
   * ``zlib``
   * ``compression.zstd``
``concurrent.interpreters``
   標準ライブラリーにあるインタプリター複数を使用することが可能となるモジュール。
``string.templatelib``
   先述の t-strings を使用可能にするモジュール。

Improved modules
================================================================================

興味のあるものや遭遇しそうな問題を含むモジュールに絞って記していく。

``argparse``
--------------------------------------------------------------------------------

``asyncio``
--------------------------------------------------------------------------------

``calendar``
--------------------------------------------------------------------------------

コマンド ``python -m calendar`` を実行したときに、今日が強調表示されるようになっ
た。この挙動は次の環境変数により変更することが可能だ：

* :ennvar:`PYTHON_COLORS`
* :envvar:`NO_COLOR`
* :envvar:`FORCE_COLOR`

``configparser``
--------------------------------------------------------------------------------

* 読み取り不能設定ファイルへの書き込みを行わなくなった。
* 区切り文字を含むキーやセクションヘッダーパターンで始まるキーへの ``write()``
  を試みると例外 ``InvalidWriteError`` が送出するようになった。

``datetime``
--------------------------------------------------------------------------------

次のクラスにクラスメソッド ``strptime()`` が加わった：

* ``datetime.date``
* ``datetime.time``

.. sourcecode:: pycon
   :caption: An example of ``datetime.time.strptime()``
   :force:

   >>> from datetime import import time
   >>> time.strptime("2 時 50 分", "%H 時 %M 分")
   datetime.time(2, 50)

``decimal``
--------------------------------------------------------------------------------

クラスメソッド ``from_number()`` が加わった。戻り値の型を除けば、このメソッドは
上述の ``float`` や ``complex`` のそれと同様に動作する。

算術演算環境として ``IEEEContext`` 型を新たに使用可能になった。

.. sourcecode:: pycon
   :caption: An example of using ``IEEEContext``
   :force:

   >>> 1 / 7
   0.14285714285714285
   >>> from decimal import Decimal, IEEEContext, localcontext
   >>> print(Decimal('1.0') / Decimal('7.0'))
   0.1428571428571428571428571429
   >>> decimal.IEEEContext(64)
   Context(prec=16, rounding=ROUND_HALF_EVEN, Emin=-383, Emax=384, capitals=1, clamp=1, flags=[], traps=[])
   >>> ctx = _
   >>> with localcontext(ctx):
   ...     print(Decimal('1.0') / Decimal('7.0'))
   ...
   0.1428571428571429

``fractions``
--------------------------------------------------------------------------------

メソッド ``as_integer_ratio()`` を持つオブジェクトならば、何であってもそれから
``Fraction`` オブジェクトを生成可能になった。

クラス ``Fraction`` にクラスメソッド ``from_number()`` が加わった。意味は先述の
同名メソッドと同様にはたらくが、引数は次のいずれかを満たす必要がある：

* 値の型が ``numbers.Integral``, ``numbers.Rational``, ``float``,
  ``decimal.Decimal`` のいずれかである。
* オブジェクトがメソッド ``as_integer_ratio()`` を有する。

``functools``
--------------------------------------------------------------------------------

関数 ``reduce()`` の最初の引数をキーワード引数として渡せるようになった。

.. sourcecode:: pycon
   :caption: An example of passing initial parameter to ``reduce()``
   :force:

   >>> from functools import reduce
   >>> reduce(lambda x, y: x + y, range(5))
   10
   >>> reduce(lambda x, y: x + y, range(5), initial=-10)
   0

``getpass``
--------------------------------------------------------------------------------

関数 ``getpass()`` がキーワードオプション引数 ``echo_char`` を備えた。キーボード
フィードバックを実現する。タイプするたびにダミー文字を表示し、削除されると消去す
る。

.. sourcecode:: python
   :caption: An example of using ``echo_char`` parameter
   :force:

   from getpass import getpass

   pin = getpass('Enter PIN: ', echo_char='*')

``heapq``
--------------------------------------------------------------------------------

次の最大ヒープ関数を搭載した：

* ``heapify_max()``
* ``heappush_max()``
* ``heappop_max()``
* ``heapreplace_max()``
* ``heappushpop_max()``

公式文書にある、ストリーミング入力から中央値を求めるアルゴリズムコードは必読。

``io``
--------------------------------------------------------------------------------

ファイルやその他のストリームから読み書きするための汎用プロトコルが追加：

* ``Reader[T]``
* ``Writer[T]``

``T`` は通常 ``str`` または ``bytes`` となるが、ストリームから読み書き可能である
型ならば何でもかまわない。これらのプロトコルは ``typing.IO`` 系プロトコルのより
簡素な代替型だ。

``json``
--------------------------------------------------------------------------------

CLI が ``python -m json`` でいけるようになった。

``math``
--------------------------------------------------------------------------------

このモジュールが示すエラーメッセージ ``math domain error`` が状況に応じた、より
詳しい説明に改善した。

.. sourcecode:: console
   :caption: Python 3.13 と 3.14 との間の ``math`` からのエラーメッセージの違い
   :force:

   $ mamba run -n python-3.13 python -c "import math; math.sqrt(-5)"
   Traceback (most recent call last):
     File "<string>", line 1, in <module>
       import math; math.sqrt(-5)
                    ~~~~~~~~~^^^^
   ValueError: math domain error
   $ mamba run -n python-3.14 python -c "import math; math.sqrt(-5)"
   Traceback (most recent call last):
     File "<string>", line 1, in <module>
       import math; math.sqrt(-5)
                    ~~~~~~~~~^^^^
   ValueError: expected a nonnegative input, got -5.0

``mimetypes``
--------------------------------------------------------------------------------

CLI が実装された。下の例のように利用できる：

.. sourcecode:: console
   :caption: Examples of running ``python -m mimetypes``
   :force:

   $ python -m mimetypes filename.png
   type: image/png encoding: None
   $ python -m mimetypes --extension text/javascript
   .js

``operators``
--------------------------------------------------------------------------------

次の述語関数が加わった：

* ``is_none()``
* ``is_not_none()``

``os``
--------------------------------------------------------------------------------

関数 ``reload_environ()`` が加わった。この関数の目的は、プロセス外部で環境変数が
変更されたときに、値 ``os.environ`` を更新できるようにするものだ。

``pathlib``
--------------------------------------------------------------------------------

クラス ``Path`` にファイルとディレクトリーを再帰的に運ぶ次のメソッドが加わった：

* ``copy()``, ``move()``: 宛先にファイルまたはディレクトリー木をコピーまたは移動
* ``copy_into()``, ``move_into()``: 宛先ディレクトリーの中にコピーまたは移動

``pdb``
--------------------------------------------------------------------------------


``re``
--------------------------------------------------------------------------------

* メタキャラクター :regexp:`\z` が使用可能になった。意味は大文字版と同じ。
* メタキャラクター :regexp:`\B` が空文字列に合致するようになった。これにより、こ
  のメタキャラクターの意味はいつでもメタキャラクター :regexp:`\b` と反対になる。

``types``
--------------------------------------------------------------------------------


``typing``
--------------------------------------------------------------------------------


``unicodedata``
--------------------------------------------------------------------------------

Unicode データベースが Unicode 16.0.0 に更新した。

.. seealso::

   `Unicode 16.0.0 <https://www.unicode.org/versions/Unicode16.0.0/>`__

``unittest``
--------------------------------------------------------------------------------

``uuid``
--------------------------------------------------------------------------------

CLI ``python -m uuid`` にオプション ``--count`` が使用可能になった。UUID を一度
の実行で複数個生成する。これは :program:`uuidgen` にない機能だ。

Optimizations
================================================================================

ここは一般プログラマーには重要ではないかもしれない。ほとんどチェックしていない。

Removed
================================================================================

Deprecated
================================================================================

古いやり方をいつまで経っても採用し続けないように、一通りチェックする。文書化され
ていない機能や特定のプラットフォーム固有の挙動に関するものがほとんどだ。

Porting to Python 3.14
================================================================================

本節以降、個人的には対応項目なし。

----

興味がある項目は以上？
