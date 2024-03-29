======================================================================
What's New In Python 3.9 ノート
======================================================================

`What's New In Python 3.9 <https://docs.python.org/3/whatsnew/3.9.html>`__ をた
どりながら調査。興味のあるものしか読まない。

.. contents:: ノート目次

New Features
======================================================================

* クラス ``dict`` にマージ・更新操作用の演算子 ``|``, ``|=`` が追加

  * ``d1.update(d2)`` を ``d1 |= d2`` と書けるようになった。
  * あるいは ``{**d1, **d2}`` を ``d1 | d2`` と書けるようになった。

* 文字列系クラスに接頭辞・接尾辞を削除するためのメソッド ``.removeprefix()``,
  ``.removesuffix()`` が追加

  .. code:: pycon

     >>> '<td>19</td>'.removeprefix('<td>').removesuffix('</td>')
     '19'

* ``typing.List`` や ``typing.Dict`` などをアノテーションで使わなくても済む。

Other Language Changes
======================================================================

* ``__import__()`` は相対インポート絡みの例外発生時に ``ImportError`` を送出する
  ようになった。
* スクリプトファイルを実行すると、コマンドライン引数で指定されたファイル名の絶対
  パスを覚えるようになった。 ``__main__`` モジュールの ``__file__`` の値は相対パ
  スではなく絶対パスとなる。スクリプト中で作業ディレクトリーが変化しても、これら
  のパスは有効であり続ける。
* :code:`"".replace("", s, n)` の挙動が変わり、``s`` を返すようになった。

  * 「空文字列に含まれる空文字列を最大 ``n`` 個まで ``s`` に置換しろ」の意。

* 有効であるどんな式もデコレーターとして使えるようになった。以前は文法が相当限定
  的だった。
* モジュール ``typing`` のヘルプ周りを改善した。

  * IPython などで各要素を ``?`` で表示するときの文言が改善されたと読める。

* ``aclose()``, ``asend()``, ``athrow()`` を平行実行するのは禁止とする。そして
  ``ag_running`` は実際の非同期ジェネレーターの稼動状態を表すようになった。

  * これは何か例を見たい。

* 次におけるメソッド ``__iter__`` を呼び出す際の予期せぬエラーは ``TypeError``
  でマスクされなくなった。

  * 演算子 ``in``
  * 関数 ``operator.contains()``
  * 関数 ``operator.indexOf()``
  * 関数 ``operator.countOf()``

New Modules
======================================================================

``zoneinfo``
----------------------------------------------------------------------

今は利用する機会がないので後回し。以下、動作確認したモジュール要素。

クラス ``zoneinfo.ZoneInfo()`` で適当にタイムゾーンを二つ作って時刻の変換処理。

.. code:: pycon

   >>> from datetime import datetime
   >>> import zoneinfo
   >>> tokyo = zoneinfo.ZoneInfo('Asia/Tokyo')
   >>> la = zoneinfo.ZoneInfo('America/Los_Angeles')
   >>> dt = datetime.today()
   >>> dt.astimezone(tokyo)
   datetime.datetime(2021, 2, 13, 23, 8, 5, 929591, tzinfo=zoneinfo.ZoneInfo(key='Asia/Tokyo'))
   >>> dt.astimezone(la)
   datetime.datetime(2021, 2, 13, 6, 8, 5, 929591, tzinfo=zoneinfo.ZoneInfo(key='America/Los_Angeles'))

関数 ``zoneinfo.available_timezones()`` は利用可能なタイムゾーンの文字列全てから
なる集合を返す。この関数は大量のファイルを開くので気をつけるようにと注意書きがあ
る。

関数 ``zoneinfo.reset_tzpath()``: タイムゾーンを検索する際に用いられるファイルシ
ステムパスを上書きする。引数はパス文字列のリストなど。WSL だと
:file:`/usr/share/zoneinfo` などが利用できる。

変数 ``zoneinfo.TZPATH``: 文字列のリスト。読み取り専用。タイムゾーンを検索する際
に用いられるファイルシステムパス。

``graphlib``
----------------------------------------------------------------------

今のところ、トポロジカルソートのためのクラス ``TopologicalSorter`` がある。
NetworkX で学習したようなことができる。

.. code:: pycon

   >>> from graphlib import TopologicalSorter
   >>> graph = {
   ...     'プラチナキング': {'ドラゴスライム', 'エビルエスターク'},
   ...     'ドラゴスライム': {'スライム', 'リザードマン'},
   ...     'エビルエスターク': {'アンドレアル', 'デスマシーン'},
   ...     'アンドレアル': {'サンダーラット', 'ゲリュオン'},
   ...     'ゲリュオン': {'リザードマン', 'ダンビラムーチョ'},
   ...     'デスマシーン': {'ゴーレム', 'プロトキラー'},
   ...     'ゴーレム': {'ばくだん岩', 'バーサーカー'},
   ...     'プロトキラー': {'サンダーラット', 'ゴーレム'},}
   ...
   >>> ts = TopologicalSorter(graph)
   >>> tuple(ts.static_order())
   ('スライム',
    'リザードマン',
    'サンダーラット',
    'ダンビラムーチョ',
    'バーサーカー',
    'ばくだん岩',
    'ドラゴスライム',
    'ゲリュオン',
    'ゴーレム',
    'アンドレアル',
    'プロトキラー',
    'デスマシーン',
    'エビルエスターク',
    'プラチナキング')

Improved Modules
======================================================================

とても全部は見られないので、使ったことがあるモジュールに絞って記す。

``asyncio``
----------------------------------------------------------------------

イベントループに新しいコルーチン ``shutdown_default_executor()`` が加わった。こ
のメソッドは既定の executor を完了させることを予約して、``ThreadPoolExecutor``
にあるスレッドのすべてが終了するまで (to join) 待機するというものだ。さらに、関
数 ``run()`` がこのコルーチンを利用するように更新した。

新しいコルーチン ``to_thread()`` が加わった。関数を別スレッドで非同期的に実行す
る。おもに、別々のスレッド同士から IO バウンドな関数を実行する際にイベントループ
をブロックするのを避けるために用いられる。本質的には、キーワード引数を直接取るこ
とができる ``run_in_executor()`` の高水準版として機能する。

タイムアウトによりタスクをキャンセルするときに、タイムアウトがゼロまたは負の場合
においても、正のタイムアウトの場合のように ``wait_for()`` がキャンセルを完了する
まで待機するようになった。

``concurrent.futures``
----------------------------------------------------------------------

そういえばこのモジュールはここのところ特に利用していない。

クラス ``Executor`` のメソッド ``.shutdown()`` に引数 ``cancel_futures`` が加
わった。この引数は executor をシャットダウンする前に実行開始前保留中の futures
が完了するまで待機する代わりに、それらのすべてをキャンセルするものだ。

``ThreadPoolExecutor`` および ``ProcessPoolExecutor`` からデーモンスレッドをなく
した。これは subinterpreters（この用語は注を要する）の互換性とシャットダウン処理
における予測可能性を向上する。

再利用するのに使える稼動していないワーカーがないときに限り
``ProcessPoolExecutor`` にあるワーカーが要求に応じて排出されるようになった。これ
は開始時のオーバーヘッドを最適化し、稼働していないワーカーに対して失われる CPU
時間を縮小する。

``datetime``
----------------------------------------------------------------------

クラス ``date`` およびクラス ``datetine`` メソッド ``.isocalendar()`` の返す値が
単なる ``tuple`` から ``namedtuple`` に置き換わった。メンバー ``.year``,
``.week``, ``.weekday`` を持つ。

.. code:: pycon

   >>> from datetime import date

   >>> date.today()
   datetime.date(2021, 2, 14)

   >>> _.isocalendar()
   datetime.IsoCalendarDate(year=2021, week=6, weekday=7)

``http``
----------------------------------------------------------------------

次のステータスコードが追加した。

* ``HTTPStatus.EARLY_HINTS`` (103)
* ``HTTPStatus.IM_A_TEAPOT`` (418)
* ``HTTPStatus.TOO_EARLY`` (425)

``inspect``
----------------------------------------------------------------------

クラス ``BoundArguments`` のメンバー ``arguments`` の型が
``collections.OrderedDict`` から単なる ``dict`` に変更した。理由が述べられていな
いが、これは ``dict`` のキーの順序の決まり方が変わったことと関係があるだろう。

``ipaddress``
----------------------------------------------------------------------

IPv6 に対応。IPv6 をサポートする新しいクラスがいくつかと、既存の関数が新クラスの
オブジェクトを扱えるようになったということだ。

``math``
----------------------------------------------------------------------

数学モジュールは重要なので他よりも少し丁寧に調べる。

* 関数 ``gcd()`` が任意の個数の整数を引数として受け付けるようになった。これで複
  数の整数の最大公約数が欲しいときに ``functools.reduce()`` する必要がなくなる。

  .. code:: pycon

     >>> import math
     >>> import functools
     >>> functools.reduce(math.gcd, [27, 15, 300])
     3
     >>> math.gcd(*[27, 15, 300])
     3
     >>> math.gcd(27, 15, 300)
     3

* 関数 ``lcm()`` が追加。そのシグニチャーは上記の ``gcd()`` に準じる。
* 関数 ``nextafter()`` が追加。浮動小数点数 ``x``, ``y`` を与えて、``x`` の
  ``y`` へ向かう「計算機的に次の」浮動小数点数を返すというものだ。``y`` は
  ``x`` と明確に異なる値ならば何でもよい。紛れがないように ``math.inf`` や
  ``-math.inf`` でもいい。

  .. code:: pycon

     >>> import math
     >>> math.nextafter(1.11, 2)
     1.1100000000000003
     >>> math.nextafter(1.11, 0)
     1.1099999999999999

* 関数 ``ulp()`` が追加。平たく言うと ``ulp(x)`` の値は ``x`` に最も近い浮動小数
  点数 ``a``, ``b`` （ただし ``a <= x <= b`` かつ ``a < b`` とする）に対して
  ``b - x`` または ``x - a`` のうち意味のあるほうの値に等しいと憶えておけばいい。

  * ``x > 0`` の場合、:code:`x + math.ulp(x) == math.nextafter(x, math.inf)` が
    成り立つ。
  * ``x < 0`` の場合、:code:`math.ulp(x) == -math.ulp(x)` が成り立つ。

  .. code:: pycon

     >>> import math
     >>> x = 2
     >>> math.ulp(x)
     4.440892098500626e-16
     >>> a = math.nextafter(x, x - 10); a
     1.9999999999999998
     >>> b = math.nextafter(x, x + 10); b
     2.0000000000000004
     >>> x - a, b - x
     (2.220446049250313e-16, 4.440892098500626e-16)

``multiprocessing``
----------------------------------------------------------------------

クラス ``SimpleQueue`` にメソッド ``.close()`` が追加。クライアントがキューを明
示的に閉じることができる。

``os``
----------------------------------------------------------------------

改正項目が複数あるが、用のありそうなものに絞る。

* 関数 ``unsetenv()`` が Windows でも利用可能になった。
* 関数 ``putenv()`` と ``unsetenv()`` が常に利用可能になった。

``pathlib``
----------------------------------------------------------------------

クラス ``Path`` のメソッド ``.readlink()`` が追加。関数 ``os.readlink()`` のよう
に振る舞う。

私の WSL 環境の例。ホームに Windows のユーザープロファイルフォルダーのサブフォル
ダーへのシンボリックリンクがいくつかあるので、一つ試す。

.. code:: pycon

   >>> import pathlib
   >>> p = pathlib.Path('Documents')
   >>> p.readlink()
   PosixPath('/mnt/c/Users/xxxxxxxx/Documents')

``pdb``
----------------------------------------------------------------------

Windows でもファイル :file:`~/.pdbrc` を参照するようになった。

``pprint``
----------------------------------------------------------------------

関数 ``pprint()`` が ``types.SimpleNamespace`` にも対応。

``pydoc``
----------------------------------------------------------------------

クラス、関数、メソッド等々だけでなく、とにかく ``__doc__`` を属性として持つもの
に対してならば何でもPython コンソールでの ``help()`` や IPython の ``?`` が機能
するようになった。

``random``
----------------------------------------------------------------------

クラス ``Random`` に指定した長さのランダムな ``bytes`` オブジェクトを返すメソッ
ド ``.randbytes()`` が追加。

``socket``
----------------------------------------------------------------------

関数 ``send_fds()`` および ``recv_fds()`` が追加。ただしこれらが利用可能なのは
``sendmsg()`` と ``SCM_RIGHTS`` の仕組みをサポートしているような UNIX とする。

.. todo::

   これらが WSL の Python で機能するか試す。

``sys``
----------------------------------------------------------------------

属性 ``platlibdir`` が追加。プラットフォーム固有のライブラリーディレクトリーの名
前を表す。標準ライブラリーやインストールされている拡張モジュールのパスを組み立て
るのに利用されるものだ。この値はプラットフォームほとんどでは文字列 ``"lib"``
だ。モノによっては ``"lib64"`` になっている。

以前は ``stderr`` は非対話モードではブロックバッファーされていた（言われてみると
そんな記憶がある）。今では ``stderr`` は既定では行バッファーされる。つまり一行ご
とに標準エラー出力への出力が行われる。

``time``
----------------------------------------------------------------------

AIX にもナノ秒解像度を有する関数 ``thread_time()`` が実装された。これは 10 ミリ
秒解像度の ``clock_gettime(CLOCK_THREAD_CPUTIME_ID)`` よりも高精度であることに注
意。

``typing``
----------------------------------------------------------------------

型 ``Annotated`` が追加。コンテキスト固有のメタデータで既存の型をデコレートする
のに使う。さらに関数 ``get_type_hints()`` に引数 ``include_extras`` が新しく追
加。この引数はそのようなメタデータに実行時にアクセスするのに指定するものだ。

``unicodedata``
----------------------------------------------------------------------

Unicode データベースがバージョン 13.0.0 にアップグレード。

``xml``
----------------------------------------------------------------------

クラス ``etree.ElementTree`` のオブジェクトを XML ファイルにシリアライズするとき
に、属性内にある空白文字は保たれるようになった。改行文字は ``\n`` に正規化されな
くなった。

Deprecated
======================================================================

これも注目したい点だけ挙げる。

* 関数 ``math.factorial()`` は非負の整数に等しい浮動小数点数を引数として受け付け
  なくなる。そのような引数が与えられると、例外 ``DeprecationWarning`` を送出す
  る。
* モジュール ``random`` は現在ハッシュ化可能な型ならば何でもシード値として受け付
  けている。まずいことに、そのようなものには決まったハッシュ値になることが保証さ
  れない型がある。 Python 3.9 以降はシードとなり得る型を次のものに制限する：
  ``None``, ``int``, ``float``, ``str``, ``bytes``, ``bytearray``.
* ``asyncio.wait()`` に対してコルーチンオブジェクトを明示的に与えることを勧めら
  れたものではないとし、 Python 3.11 において廃止する。
* 関数 ``random.shuffle()`` の引数 ``random`` を勧められないものとする。

Removed
======================================================================

* クラス ``array.array`` のメソッド ``.tostring()`` および ``.fromstring()`` は
  削除した。それぞれ ``.tobytes()``, ``.frombytes()`` の別名だった。
* クラス ``threading.Thread`` のメソッド ``isAlive()`` は削除した。代わりに
  ``.is_alive()`` を使うこと。
* クラス ``ElementTree`` および ``Element`` のメソッド ``.getchildren()``,
  ``.getiterator()`` は削除した。代替コードは次のとおり：

  * :code:`x.getchildren()` を :code:`iter(x)` や :code:`list(x)` に書き換える。
  * :code:`x.getiterator()` を :code:`x.iter()` や :code:`list(x.iter())` に書き
    換える。

* 関数 ``fractions.gcd()`` は削除した（というかモジュールを引っ越したようだ）。
  これは ``math.gcd()`` に置き換えられる。
* 関数 ``json.loads()`` の引数 ``encoding`` が削除。
* 次の二つの構文はもうサポートされない：

  .. code:: python

     with (await asyncio.lock):
         # ...

     with (yield from asyncio.lock):
         # ...

  代わりに次のように書く：

  .. code:: python

     async with lock:
         # ....

  このことは ``asyncio.Condition`` と ``asyncio.Semaphore`` についても成り立つ。

* クラス ``asyncio.Task`` のメソッド ``.current_task()`` および ``.all_tasks()``
  が削除。代わりに関数 ``asyncio.current_task()`` と ``asyncio.all_tasks()`` を
  それぞれ使うことができる。
* クラス ``html.parser.HTMLParser`` のメソッド ``.unescape()`` が削除。文字参照
  を対応する Unicode 文字に変換するのには関数 ``html.unescape()`` を使用する。
