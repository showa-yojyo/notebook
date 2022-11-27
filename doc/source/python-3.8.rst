======================================================================
What's New In Python 3.8 ノート
======================================================================

`What's New In Python 3.8 <https://docs.python.org/3/whatsnew/3.8.html>`__ をた
どりながら調査。興味のあるものしか読まない。

.. contents:: ノート目次

New Features
======================================================================

* 代入文 ``:=``

  * ふつうの ``=`` と微妙に異なる。
  * この演算子は内包記法と相性が良いようだ。

  .. code:: pycon

     >>> [y for x in range(10) if (y := x**2 - x) > 0]
     [2, 6, 12, 20, 30, 42, 56, 72]

* 位置専用引数

  * 引数リストのスラッシュまでが位置専用引数を意味し、キーワード引数のような形で
    は値渡しできない。
  * この構文は私は使わないだろうが、既存関数のヘルプを参照するときにこの知識が要
    るわけだ。

  .. code:: pycon

     >>> help(len)
     Help on built-in function len in module builtins:

     len(obj, /)
         Return the number of items in a container.

     >>> len(obj=[2,3,4])
     TypeError: len() takes no keyword arguments
     >>> len([2,3,4])
     3

* f-string での ``=`` を用いたオブジェクトの表現

  * 中括弧の中に評価したい Python 式に加えて等号を置くと、式を表す文字列がそのま
    ま保たれる機能だ。
  * 次は公式文書からそっくり拝借した利用例だ。

  .. code:: pycon

     >>> from math import cos, radians
     >>> theta = 30
     >>> f'{theta=} {cos(radians(theta))=:.3f}'
     'theta=30 cos(radians(theta))=0.866'

Other Language Changes
======================================================================

* メソッド ``.as_integer_ratio()``

  * ``float`` や ``decimal.Decimal`` のメソッドだったが、さらに ``bool``,
    ``int``, ``fractions.Fraction`` もこれをサポートするようになった。
  * ``Fraction`` にこれまでサポートされていなかったというのは驚きだ。

    .. code:: pycon

       >>> True.as_integer_ratio()
       (1, 1)
       >>> False.as_integer_ratio()
       (0, 1)
       >>> (10).as_integer_ratio()
       (10, 1)
       >>> (-10).as_integer_ratio()
       (-10, 1)
       >>> (0).as_integer_ratio()
       (0, 1)
       >>> from fractions import Fraction
       >>> Fraction(-123, 456).as_integer_ratio()
       (-41, 152)

* 正規表現で Unicode の文字名を :regexp:`\N{name}` の形で書けるようになった。例
  えば「🀀」にマッチする正規表現は次でもよい：

  .. code:: pycon

     >>> import re
     >>> text = 'ドラは🀀になりました'
     >>> re.search(r'\N{MAHJONG TILE EAST WIND}', text)
     <re.Match object; span=(3, 4), match='🀀'>

* 逆順サポートが ``dict``, ``dictview`` に追加された。使う気がしない。
* 関数 ``pow(base, exp, mod)`` で整数のべき乗の剰余を計算する際に、``base`` が
  ``mod`` と互いに素ならば ``exp`` に負の数を許容するようになった。次のコードは
  公式文書からとってきたものだ：

  .. code:: pycon

     >>> pow(38, -1, 137)
     119
     >>> 38 * pow(38, -1, 137) % 137
     1

  * これは Diophantus 方程式を解くのに利用できる。これも公式からとってきた例だ
    が、方程式

    .. math::

       4258x + 147y = 369

    の解を一つ見つけよう。これを次のように書き換えれば：

    .. math::

       4258x \equiv 369 \pmod{147}

    Python で次のコードで :math:`x` および :math:`y` を求められることに気づく：

    .. code:: pycon

       >>> x = 369 * pow(4258, -1, 147) % 147
       >>> y = (4258 * x - 369) // -147
       >>> 4258 * x + 147 * y
       369

* ``dict`` の内包表現はキー、値の順に評価される。

New Modules
======================================================================

* ``importlib.metadata``

  * このモジュールはサードパーティー製パッケージからバージョン、エントリーポイン
    トなどの諸データを得る機能を提供する。

    .. code:: pycon

       >>> import importlib.metadata
       >>> importlib.metadata.version('sympy')
       '1.5.1'
       >>> sympy_metadata
       <email.message.Message at 0x2237c4d4820>
       >>> list(_)
       ['Metadata-Version',
        'Name',
        'Version',
        'Summary',
        'Home-page',
        'Author',
        'Author-email',
        'License',
        'Keywords',
        'Platform',
        'Classifier',
        'Classifier',
        'Classifier',
        'Classifier',
        'Classifier',
        'Classifier',
        'Classifier',
        'Classifier',
        'Classifier',
        'Classifier',
        'Classifier',
        'Classifier',
        'Classifier',
        'Classifier',
        'Classifier',
        'Requires-Python',
        'Requires-Dist']
       >>> sympy_metadata = importlib.metadata.metadata('sympy')
       >>> sympy_metadata['Author']
       'SymPy development team'
       >>> sympy_metadata['Summary']
       'Computer algebra system (CAS) in Python'
       >>> sympy_metadata['Keywords']
       'Math CAS'

Improved Modules
======================================================================

``asyncio``
----------------------------------------------------------------------

* Python 3.7 で新設された ``run()`` が安定 API に昇格した。
* シェルで :command:`python -m asyncio` を実行すると、専用対話型インタプリタが起
  動する。
* Windows では、イベントループのデフォルトが ``ProactorEventLoop`` になった。併
  せて、``ProactorEventLoop`` が ``KeyboardInterrupt`` によって中断できるように
  なった。
* ``Task`` オブジェクトに名前をつけることができる。生成時に ``name`` を指定する
  か、メソッド ``set_name()`` を呼べばできる。名前は ``repr()`` 出力やメソッド
  ``get_name()`` の返り値でわかる。

``collections``
----------------------------------------------------------------------

* ``namedtuple`` のメソッド ``_asdict()`` の返り値の型が単なる ``dict`` に変更さ
  れた。

``cProfile``
----------------------------------------------------------------------

* クラス ``Profile`` がコンテキストマネジャーをサポートした。つまり ``with`` 文
  でプロファイルがとれる。

  .. code:: pycon

     >>> def fib(n):
     ...     if n == 0:
     ...         return 0
     ...     elif n == 1:
     ...         return 1
     ...     else:
     ...         return fib(n - 1) + fib(n - 2)
     ...
     >>> from cProfile import Profile
     >>> with Profile() as profiler:
     ...     for i in range(10):
     ...         print(fib(i))
     ...
     0
     1
     1
     2
     3
     5
     8
     13
     21
     34

     >>> profiler.print_stats()
              488 function calls (222 primitive calls) in 0.028 seconds

        Ordered by: standard name

        ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        276/10    0.000    0.000    0.000    0.000 <ipython-input-107-8190ac52035f>:1(fib)
            20    0.000    0.000    0.028    0.001 ansitowin32.py:160(write)
            20    0.000    0.000    0.028    0.001 ansitowin32.py:177(write_and_convert)
            20    0.000    0.000    0.027    0.001 ansitowin32.py:193(write_plain_text)
            20    0.000    0.000    0.000    0.000 ansitowin32.py:245(convert_osc)
            20    0.000    0.000    0.028    0.001 ansitowin32.py:40(write)
             1    0.000    0.000    0.000    0.000 cProfile.py:133(__exit__)
            20    0.000    0.000    0.000    0.000 {built-in method builtins.len}
            10    0.000    0.000    0.028    0.003 {built-in method builtins.print}
             1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
            40    0.000    0.000    0.000    0.000 {method 'finditer' of 're.Pattern' objects}
            20    0.004    0.000    0.004    0.000 {method 'flush' of '_io.TextIOWrapper' objects}
            20    0.023    0.001    0.023    0.001 {method 'write' of '_io.TextIOWrapper' objects}

``csv``
----------------------------------------------------------------------

* ``csv.DictReader`` が返す iterable が単なる ``dict`` になった。

``datetime``
----------------------------------------------------------------------

* クラスメソッドが二点追加された。これらの逆メソッドはすでにサポート済みだ。

  * ``date.fromisocalendar(year, week, day)``
  * ``datetime.fromisocalendar(year, week, day)``

  .. code:: pycon

     >>> from datetime import date, datetime
     >>> date.fromisocalendar(2020, 18, 7)
     datetime.date(2020, 5, 3)
     >>> datetime.fromisocalendar(2020, 18, 7)
     datetime.datetime(2020, 5, 3, 0, 0)

``functools``
----------------------------------------------------------------------

* ``lru_cache()`` が従来の用法に加えて decorator そのものとしても使えるように
  なった。

  .. code:: pycon

     >>> from functools import lru_cache
     >>> @lru_cache
     ... def fib(n):
     ...     if n == 0:
     ...         return 0
     ...     elif n == 1:
     ...         return 1
     ...     else:
     ...         return fib(n - 1) + fib(n - 2)
     ...

* ``cached_property()`` が追加された。一度計算すれば二度と変わらないような値を返
  すメソッドに適用すると効率が良い。
* ``singledispatchmethod()`` が追加された。名前からわかるように
  ``singledispatch()`` のメソッド版だ。

``itertools``
----------------------------------------------------------------------

* 関数 ``accumulate()`` にオプション引数 ``initial`` が追加された。

``math``
----------------------------------------------------------------------

* 関数 ``dist()`` が追加された。

  * Pythagoras の定理に基づく二点間に距離を計算する。
  * 点は iterable で与えることができる。二点の次元は同じであるものとする。

* 関数 ``hypot()`` の二次元制限が廃止された。
* 関数 ``prod()`` が追加された。組み込み関数 ``sum()`` の乗算版だ。
* 関数 ``perm()`` が追加された。順列の数を計算する。
* 関数 ``comb()`` が追加された。二項係数を計算する。
* 関数 ``isqrt()`` が追加された。非負整数を取り非負整数を返す。

``os.path``
----------------------------------------------------------------------

* 関数のうち、パス文字列を判定して真偽値を返す ``exists()`` などが
  ``ValueError`` またはそのサブクラスの例外を送出していたような状況において、単
  に ``False`` を返すように変更された。パス文字列が OS レベルで表現できないよう
  な文字なりバイトなりを含むときにそうなる。
* Windows では 関数 ``expanduser()`` が環境変数 ``USERPROFILE`` を ``HOME`` より
  も優先するようになった。
* その他の Windows 対応。

``pathlib``
----------------------------------------------------------------------

* Path のメソッドのうち、パス文字列を判定して真偽値を返す ``exists()`` などにつ
  いても ``os.path`` での変更と同じものがなされた。

``pprint``
----------------------------------------------------------------------

* 関数に引数 ``sort_dicts`` が追加された。

  * 既定値は True であるが、True と False のどちらも用途があるので考えて使う。
  * それに伴い関数 ``pp()`` が追加された。:code:`sort_dicts=False` として
    関数 ``pprint()`` を呼び出すようなものだ。

``statistics``
----------------------------------------------------------------------

使えるものが相当数追加されている。

* 関数 ``fmean()`` が追加された。関数 ``mean()`` の浮動小数点特化版。
* 関数 ``geometric_mean()`` が追加された。こちらはデータを浮動小数点に変換してか
  ら演算する。
* 関数 ``multimode()`` が追加された。最頻値が複数あればそれをすべて返す。
* 関数 ``quantiles()`` が追加された。分割点のほうを返す。

  * キーワード引数 ``n`` で分割数を指定する。既定値は 4 だ。
  * キーワード引数 ``method`` でアルゴリズムを指定する。 ``'inclusive'`` か
    ``'exclusive'`` を指定する。既定値は後者だ。

* クラス ``NormalDist`` が追加された。もちろん正規分布を意味する。

  * コンストラクターから生成するときは期待値と標準偏差を与える。
  * クラスメソッド ``.from_samples()`` でデータから生成することもできる。
  * Library Reference の記述がひじょうに丁寧なので読んでおく。

``unicodedata``
----------------------------------------------------------------------

* Unicode 12.1.0 に対応。
* 関数 ``is_normalized()`` が追加された。与えられた文字列が NFC, NFKC, NFD, NFKD
  正規形なのかどうかを返す。

以上
