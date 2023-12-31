======================================================================
What's New In Python 3.3 ノート
======================================================================

What's New In Python 3.3 を読んで、個人的に関心のある項目に注釈を付けていく。

.. contents:: ノート目次

組み込み機能
======================================================================

* ``bytes`` と ``bytearray`` のメソッドでバイト値を引数にするようなものについて、
  0 から 255 の整数を入力することが許されるようになった。

  ROM 解析コードを書くのに明らかに便利。

* ``list`` と ``bytearray`` に ``copy()``, ``clear()`` が追加。

  * ``copy()`` はいわゆる浅いコピーを実現する。
  * ``clear()`` が今までなかったのは驚き。

* ``OSError`` 例外階層が変更され、単純化された。

  .. code-block:: text

     OSError
      +-- BlockingIOError
      +-- ChildProcessError
      +-- ConnectionError
      |    +-- BrokenPipeError
      |    +-- ConnectionAbortedError
      |    +-- ConnectionRefusedError
      |    +-- ConnectionResetError
      +-- FileExistsError
      +-- FileNotFoundError
      +-- InterruptedError
      +-- IsADirectoryError
      +-- NotADirectoryError
      +-- PermissionError
      +-- ProcessLookupError
      +-- TimeoutError

  * ``IOError`` や ``WindowsError`` が ``OSError`` に吸収されたと考えてよい。

    .. code:: ipython

       In [29]: IOError
       Out[29]: OSError

       In [30]: WindowsError
       Out[30]: OSError

  * 例えば ``FileExistsError`` や ``FileNotFoundError`` といったサブクラスが新規
    追加。これらにより ``IOError.errno`` を調べて処理を分岐するようなコードを書
    くのをやめられる。

* クラスと関数に ``__qualname__`` という属性が追加した。その要素を包含する名前空
  間のパスが見える。
* ``print()`` に ``flush`` キーワード引数が追加。想像通りの振る舞いをする。

文法仕様
======================================================================

* ``yield from`` 式の追加。

  * 例外処理を考慮に入れなければ ``yield from X`` は ``for i in X: yield i`` と
    同値。
  * この構文のおかげで generator を小分けにできる。

    .. code:: python3

       def generator(args1, args2):
           yield from subgenerator1(args1)
           yield from subgenerator2(args2)

       g = generator(x, y)

* ``raise X from none`` 式の追加。``except`` 節で本来の例外を別のものに変換する
  ときに、本来のエラーメッセージを潰すことができる。C++ の感覚だと不思議だ。
* Unicode リテラル値のためのプレフィックスが復活した。
* raw bytes リテラルとして :code:`br"..."` だけでなく :code:`rb"..."` とも書ける
  ようになった。

  ``rb`` しか使ったことがない。ちなみに生バイトリテラルはバイトデータの正規表現
  を指定するのに使える。

新規モジュール
======================================================================

* ``unittest.mock``

変更モジュール
======================================================================

* ``abc``

  * ``@abstractproperty``, ``@abstractclassmethod``, ``@abstractstaticmethod``
    が軒並み非推奨。``@abstractmethod`` に対応する組み込み関数を渡すように。

  * この場合 ``@abstractmethod`` のほうを内側に置く。

    .. code:: python3

       class SomeClass(metaclass=ABCMeta):

           @property
           @abstractmethod
           def some_abstract_property(self):
               return ...

           @classmethod
           @abstractmethod
           def some_abstract_classmethod(cls, args):
               ...

           @staticmethod
           @abstractmethod
           def some_static_method(args):
               ...

  * ``ABCMeta.register()`` が戻り値としてサブクラスを返すようになった。このこと
    でクラスに対するデコレーターとしても使えるようになった。

* ``codecs`` に ``cp65001`` が Windows 専用コーデックとして追加。
* ``collections``

  * ``ChainMap`` が追加。
  * ``Counter`` に ``+=``, ``-=``, etc. が追加。

* ``io``: ``open()`` に排他フラグ ``x`` が追加。既存のファイルと同じ名前のものを
  開こうとすると例外 ``FileExistsError`` を送出する。
* ``itertools.accumulate()`` が二項関数を受け付けるようになった。
* ``math.log2()`` が追加。なんと ``math.log(x, 2)`` より正確であることが期待でき
  る。
* ``mmap.read()`` を引数なしで呼び出し、バイト列を受け取ることができる。
* ``multiprocessing`` 周り。要研究。
* ``pdb`` タブ補完がより便利になった。コマンド名だけでなく、引数も補完する。
* ``sys.implementation`` 追加。``sys.version_info`` をメンバーとして含む。
* ``time``

  * ``perf_counter()`` や ``process_time()`` などの関数が追加。
  * ``clock_`` 系関数追加。UNIX のみ。
  * ``sleep()`` に負の値を渡すと ``ValueError`` を送出するように変更。
  * ``clock()`` はプラットフォーム依存。
    これではなく ``perf_counter()`` や ``process_time()`` を使う。

  .. code:: ipython

     In [16]: import time

     In [17]: time.get_clock_info('clock')
     Out[17]: namespace(adjustable=False, implementation='QueryPerformanceCounter()', monotonic=True, resolution=9.3302207716839e-07)

     In [19]: time.get_clock_info('perf_counter')
     Out[19]: namespace(adjustable=False, implementation='QueryPerformanceCounter()', monotonic=True, resolution=9.3302207716839e-07)

     In [20]: time.get_clock_info('process_time')
     Out[20]: namespace(adjustable=False, implementation='GetProcessTimes()', monotonic=True, resolution=1e-07)

     In [22]: time.perf_counter()
     Out[22]: 119.36619157182497

     In [23]: time.perf_counter()
     Out[23]: 124.75250189869993

     In [24]: time.process_time()
     Out[24]: 10.09375

     In [25]: time.process_time()
     Out[25]: 10.140625

* ``webbrowser`` が Google Chrome をサポート。
* ``xml.etree.ElementTree`` はこの名前で C 実装版が採用されるようになった。

その他
======================================================================

* Windows 版には py というスクリプトランチャーが配備されるようで、
  Python の複数のバージョンが環境にある場合の起動が柔軟にできるようだ。
