======================================================================
What's New In Python 3.11 ノート
======================================================================

`What's New In Python 3.11 <https://docs.python.org/3/whatsnew/3.11.html>`__ を
たどりながら調査。興味のあるものしか読まない。

.. contents:: ノート目次
   :local:

New Features
======================================================================

例外にかかわる二つの機能を習得する。

PEP 654: Exception Groups and ``except*``
----------------------------------------------------------------------

組み込み型 ``ExceptionGroup`` は複数の例外をまとめて発生させることを可能する。関
連して、新しい例外捕捉構文 ``except*`` が登場。``ExceptionGroup`` の部分に合致す
るものをまとめて拾う。

Python documentation `8.9. Raising and Handling Multiple Unrelated Exceptions
<https://docs.python.org/3/tutorial/errors.html#tut-exception-groups>`__ を見ろ。

.. admonition:: 読者ノート

   Composite パターンを思い出せ。

PEP 678: Exceptions can be enriched with notes
----------------------------------------------------------------------

例外型にメソッド ``add_note()`` が追加。例外処理ブロックで捕捉した例外オブジェク
トに対して処理者が情報を追加するために用いる。追加した注意事項は既定のトレース
バックに含まれる。

Python documentation `8.10 Enriching Exceptions with Notes
<https://docs.python.org/3/tutorial/errors.html#tut-exception-notes>`__ を見ろ。

.. admonition:: 読者ノート

   一つの例外オブジェクトに対して ``add_note()`` を複数回呼び出して情報追加を複
   数回に分けることが可能だ。

New Features Related to Type Hints
======================================================================

型ヒントとモジュール ``typing`` に影響する主な変更点について書いてある。ここを
チェックする前に次の資料を先に読んでおくと良い。要点を Python 公式より絞っていて
入門者向きだ：

`mypy <https://mypy.readthedocs.io/en/stable/index.html>`__

PEP 673: ``Self`` type
----------------------------------------------------------------------

``typing.Self`` は現在囲まれているクラスを表す特別な型だ。メソッドが ``return
self`` で終わる場合や、クラスメソッドの場合に、その戻り値註釈として用いるのが基
本的だ。

.. sourcecode:: python
   :caption: What's New から持ってきた例

   from typing import Self

   class MyLock:
     def __enter__(self) -> Self:
         self.lock()
         return self

PEP 675: Arbitrary literal string type
----------------------------------------------------------------------

``typing.LiteralString`` はリテラル文字列のみを含む特殊な型だ。文字列リテラルは
すべて ``LiteralString`` と互換性がある。しかし、単なる ``str`` として型付けられ
たオブジェクトは互換性がない。

.. sourcecode:: python
   :caption: PEP 675 から持ってきた例

   from typing import LiteralString

   def add_limit(query: LiteralString) -> LiteralString:
       return query + " LIMIT = 1"

   def my_query(query: LiteralString, user_id: str) -> None:
       sql_connection().execute(add_limit(query), (user_id,))

Other Language Changes
======================================================================

開梱式が ``for`` 文の ``in`` 部分で書けるようになった。例：

.. sourcecode:: python
   :caption: Starred unpacking expressions can now be used in for statements

   a = [0, 1, 2]
   b = (3, 4, 5)
   for i in *a, *b:
       print(i)

----

非同期関数にある内包の内部で非同期内包を使用できるようになった。この場合、外側の
内包は暗黙的に非同期になる。例：

.. sourcecode:: python
   :caption: bpo-33346 から持ってきた例：

   async def test():
       return { n: [x async for x in some_async_function(n)] for n in range(3)}

.. admonition:: 読者ノート

   これをきちんと説明するのは難しい。

----

次の二つが追加：

* :program:`python` に対する ``-P`` コマンドラインオプション
* 環境変数 :envvar:`PYTHONSAFEPATH`

このオプションはスクリプトの実行時に次のディレクトリーを ``sys.path`` に自動的に
入れることを無効にする：

* スクリプトを実行する場合は現在ディレクトリー
* オプション ``-c`` と ``-m`` を使用する場合は現在ディレクトリー

----

F-strings の ``format_spec`` にオプション ``z`` が加わった。これは書式精度で丸め
た後、負のゼロを正のゼロとして表記する：

>>> x = -.0001
>>> f'{x}'
'-0.0001'
>>> f'{x:.2f}'
'-0.00'
>>> f'{x:z.2f}'
'0.00'

New Modules
======================================================================

モジュール ``tomllib`` は TOML_ という言語を解析する機能群を備えている。この言語
は Hatch などのモダンなサードパーティーパッケージが構成ファイルのフォーマットと
して採用するものだ。特に、Python プロジェクトのルートディレクトリーにファイル
:file:`pyproject.toml` を配置し、そこにプロジェクト固有の設定項目を記すという運
用になりがちだ。

Improved Modules
======================================================================

``contextlib``
----------------------------------------------------------------------

一連の処理を ``with`` ブロックに記述し、それを特定のディレクトリーで実行した後、
ブロックを抜ければ作業ディレクトリーが自動的に復元したい場合に
``contextlib.chdir()`` を用いるとよい。

``contextlib.chdir()`` は ``os.chdir()`` の単純な context manager ラッパーだ。平
行実行安全では全くない。

``datetime``
----------------------------------------------------------------------

``from datetime import UTC`` と書けるようになった。``UTC`` は ``timezone.utc``
と同じものだ。

``datetime.date``, ``datetime.time``, ``datetime.datetime`` の
``fromisoformat()`` が ISO 8601 書式の大部分を解釈するようになった。おそらく上記
改善と関係がある。

``enum``
----------------------------------------------------------------------

.. admonition:: 読者ノート

   良い復習になるので `Enum HOWTO
   <https://docs.python.org/3/howto/enum.html#enum-basic-tutorial>`__ を読め。

``StrEnum`` が追加。メンバー値を文字列で定義する列挙型だ。``ReprEnum`` も追加さ
れたが、前者をもっぱら使えばいい。おそらく、このことと関連して
``Enum.__format__()`` が ``Enum.__str__()`` と同じ結果をが常に返すようになった。

``Flag`` で次が実現可能になった：

* ``len(MyFlag.MY_MEMBER)``
* 反復処理 (e.g. ``list(MyFlag)``)
* メンバーに対する演算子 ``in`` および ``not in`` の作用

``Flag`` を変更し、複合値 (e.g. 3, 6, 10) は別名として扱う。正準とみなされるのは
2 のべき乗値しかないようになった。反転フラグは正の等価値に変換される。

.. admonition:: 読者ノート

   ``Flag`` に関する一連の記述は、実のところ意味がよくわからない。

``math``
----------------------------------------------------------------------

関数 ``exp2()`` と ``cbrt()`` の追加。C99 にそれぞれある対応物の仕様に準じるもの
と思われる。

``math.pow()`` のコーナーケースの動作が IEE754 仕様と整合するように変更：

>>> math.pow(0.0, -math.inf)
inf
>>> math.pow(-0.0, -math.inf)
inf

``operator``
----------------------------------------------------------------------

関数 ``call`` が追加。呼び出し ``call(obj, *args, **kwargs)`` は呼び出し
``obj(*args, **kwargs)`` に等しい。

.. admonition:: 読者ノート

   古の組み込み関数 ``apply`` とは微妙に異なる。

``pathlib``
----------------------------------------------------------------------

クラス ``Path`` のメソッド ``.glob()`` および ``.rglob()`` は第一引数がパス名部
品の区切り文字、つまり ``os.sep`` や ``os.altsep`` で終わっている場合、ディレク
トリーのみを返す。

.. admonition:: 利用者ノート

   Bash で言うところの ``echo *`` と ``echo */`` の違いのようなものだろう。

``re``
----------------------------------------------------------------------

正規表現で原子グループ ``(?>...)`` と所有量化子 ``*+``, ``++``, ``?+``,
``{m,n}+`` が使えるようになった。検索が失敗する場合に効率が上がることが期待でき
る。

原子グループの例を示す。正規表現は `Regex Tutorial - Atomic Grouping
<https://www.regular-expressions.info/atomic.html>`__ より引用した：

>>> s = r'''Consider the regex \b(integer|insert|in)\b and the subject integers. Obviously, because
...: of the word boundaries, these don't match. What's not so obvious is that the regex engine will
...: spend quite some effort figuring this out.'''
>>> re.findall(r'\b(integer|insert|in)\b', s)
['integer', 'insert', 'in']
>>> re.findall(r'\b(integer|insert|in)\b', s)
['integer', 'insert', 'in']

所有量化子の例を示す。正規表現は `Regex Tutorial - Possessive Quantifiers
<https://www.regular-expressions.info/possessive.html>`__ から引用した：

>>> re.search(r'"[^"]*"', '"abc')

>>> re.search(r'"[^"]*+"', '"abc')

《基本的には、:samp:`{X}*+` の代わりに :samp:`(?>{X}*)` と書く》そうだ。

``shutil``
----------------------------------------------------------------------

関数 ``rmtree()`` にオプション引数 ``dir_fd`` が追加。ファイル記述子を与える。
ファイル記述子を与えると、この関数は第一引数であるパスを ``dir_fd`` からの相対パ
スであると解釈する。

.. admonition:: 読者ノート

   これだけ読んでも何のことがわからぬならば ``os.supports_dir_fd`` と
   ``os.rmdir`` を調べるといい。

``string``
----------------------------------------------------------------------

``Template`` に ``get_identifiers()`` と ``is_valid()`` が追加。それぞれは有効な
プレースホルダー（「ここに◯◯を入れる」ことを示すもの）すべてと、無効なプレースホ
ルダーがあるか否かを返す。

>>> from string import Template
>>> s = Template('${who} liles ${what}')
>>> s.get_identifiers()
['who', 'what']
>>> s.is_valid()
True
>>> s = Template('Give ${who} $100')
>>> s.is_valid()
False

``sys``
----------------------------------------------------------------------

関数 ``exc_info()`` は、例外 ``e`` が現在処理されているとすると、
``(type(e), e, e.__traceback__)`` を返す。つまり、次の三点を知ることができる：

* 例外型
* 例外オブジェクト自身
* 例外が最後に発生した時点でのコールスタック

関数 ``exception()`` が追加。``sys.exc_info()[1]`` を返す。

``timer``
----------------------------------------------------------------------

関数 ``sleep()`` が UNIX では ``clock_nanosleep()`` または ``nanosleep()`` を利
用可能ならば用いるようになった。Windows では :math:`10^{-7}` 秒の分解能を有する
タイマーを用いるようになった。

``typing``
----------------------------------------------------------------------

先述の型ヒントにまつわる機能以外にも新機能がある。

.. todo::

   型ヒントの仕組みに慣れたらここを埋める。

``unicodedata``
----------------------------------------------------------------------

Unicode データベースがバージョン 14.0.0 に更新した。

.. admonition:: 読者ノート

   個人的には使いたい文字がないので軽視する。

Optimizations
======================================================================

ここは一般プログラマーには重要ではないかもしれない。ほとんどチェックしていない。

Deprecated
======================================================================

``@classmethod`` を連結すること。他の記述子 (e.g. ``property``) をラップするため
に使用できなくなった。

``0o377`` より大きな値を持つ ``str`` リテラルおよび ``bytes`` リテラルでの八進数
エスケープは ``DeprecationWarning`` を送出するようになった。

パッケージ ``lib2to3`` および :program:`2to3` ツール。Python 3.10 以降を解析でき
ないことがある。

``locale.getdefaultlocale()`` 関数。代えて：

* ``locale.setlocale()``
* ``locale.getpreferredencoding(False)``
* ``locale.getlocale()``

``locale.resetlocale()`` 関数。代えて ``locale.setlocale(locale.LC_ALL, "")`` を
使え。

Removed
======================================================================

``asyncio.coroutine()`` デコレーターが削除。ジェネレータベースのコルーチンは
``async``/``await`` コードと互換。代わりに ``async def`` を使え。

Porting to Python 3.11
======================================================================

``random.shuffle()`` の ``random`` オプション引数が削除。以前はシャッフルに使用
するランダム関数は任意に指定可能だったが、現在は ``random.random()`` が常に用い
られる。

``re`` 正規表現構文において、グローバルインラインフラグ (e.g. ``(?i)``) は正規表
現の先頭以外での使用は咎められる。

``re`` モジュールでは、いくつかの長年のバグが修正され、まれに捕捉グループが誤っ
たものになることがあった。そのため、これらの場合には捕捉の出力が変わることがある。

.. _TOML: https://toml.io/
