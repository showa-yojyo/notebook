======================================================================
What's New In Python 3.6 ノート
======================================================================

What's New In Python 3.6 を読んで、個人的に関心のある項目に注釈を付けていく。

.. contents:: ノート目次

新規機能
======================================================================

* フォーマット済み文字列リテラル。

  * 最初は利用価値がわからなかったが、使ってみると便利だったのでこれ一本にしよ
    う。

    .. code:: python3

       '{} {} {}'.format(a, b, c))
       f'{a} {b} {c}'

       datetime.now().strftime('%T')
       f'{datetime.now():%T}`

* 数値リテラル内のおよびフォーマット文字列内のアンダースコア表記法が追加。最近の
  C++ にもこういう表記法がある。

  .. code:: ipython

     In [1]: 0xFFFF_FFFF
     Out[1]: 4294967295

     In [2]: 0xFF_FE_FF
     Out[2]: 16776959

     In [3]: 0xFF_FE_FFF_FFE
     Out[3]: 1099494850558

  反対方向もできる：

  .. code:: ipython

     In [7]: f'{0xFFFFFFFF:_}'
     Out[7]: '4_294_967_295'

     In [8]: f'{0xFFFFFFFF:_x}'
     Out[8]: 'ffff_ffff'

* 非同期ジェネレーターが追加。``async def`` コルーチン関数から ``yield`` もでき
  る。
* 非同期内包表記 ``async for``, ``await`` が追加。

  * どの ``await`` 内包表記もコルーチン関数の本体でしか利用できない。

* ``__init_subclass__`` クラスメソッドによるサブクラス生成のカスタマイズ。

  .. code:: python3

     def __init_subclass__(cls, **kwargs):
         super().__init_subclass__(**kwargs)
         ...

* ``__set_name__`` わかりにくい。

  * 呼び出されるのは、このメソッドが定義されたクラスのオブジェクトが、別のクラス
    （オーナー）のクラスメンバーとしてそのオブジェクトを生成するときであり、結局
    そのオーナーの定義時ということになる。

    言いたいことはこれだけだ：

    .. code:: ipython

       In [1]: class IntField:
          ...:
          ...:     # this is the new initializer:
          ...:     def __set_name__(self, owner, name):
          ...:         self.name = name
          ...:
          ...: class Model:
          ...:     int_field = IntField()
          ...:

       In [2]: Model.int_field.name
       Out[2]: 'int_field'

* ``os.PathLike`` が表現する新しいインターフェイスが定義された。メソッド
  ``__fspath__()`` を実装するクラスは、それがパスを表すことを示す。このメソッド
  はファイルシステムパスを表す ``str`` なり ``bytes`` なりを返す。

  * 次のようなものを path-like であるという：

    * ``os.PathLike`` を実装するクラスのオブジェクト
    * ファイルシステムパスを表す値をとる ``str`` または ``bytes`` オブジェクト

  * 文字列としてのパスを path-like オブジェクトから得るには次の関数を用いる：

    * ``os.path.fspath()``
    * ``os.path.fsdecode()``
    * ``os.path.fsencode()``

* Windows でファイルおよびコンソールのエンコーディングとを UTF-8 に変更。
* クラス属性の定義の順番が ``__dict__`` で保持されるようになった。
* キーワード引数の順番が保持されるようになった。
* ``global`` 文および ``nonlocal`` 文が、同じスコープにある影響を受ける名前が
  最初に利用される時点よりも先に出現していなければならなくなった。
* モジュールのインポート時に送出される例外が ``ModuleNotFoundError`` に変更され
  た。当然これは ``ImportError`` のサブクラスだ。

新規モジュール
======================================================================

* ``secrets``: 暗号化関係のモジュール。興味なし。

変更モジュール
======================================================================

* ``asyncio`` は安定バージョンになった。
* ``datetime``: ``strftime()`` 系が ISO 8601 日付ディレクティブ ``%G``, ``%u``,
  ``%V`` を認識するようになった。

  次の例は issue12006 による：

  .. ipython::

     In [1]: from datetime import date

     In [2]: f'{date(2013, 12, 31):%Y %V %u}'
     Out[2]: '2013 01 2'

     In [3]: f'{date(2013, 1, 1):%Y %V %u}'
     Out[3]: '2013 01 2'

     In [4]: f'{date(2013, 12, 31):%G %V %u}'
     Out[4]: '2014 01 2'

     In [5]: f'{date(2013, 1, 1):%G %V %u}'
     Out[5]: '2013 01 2'

* ``json``: ``load()``, ``loads()`` がバイナリーを入力として認めるようになった。
* ``math``: 定数 ``tau`` 追加。円周率の倍。地味に便利。

  .. code:: ipython

     In [1]: from math import cos, sin, isclose, tau

     In [2]: from random import random

     In [3]: x = random() * tau

     In [4]: isclose(cos(x), cos(x + tau))
     Out[4]: True

     In [5]: isclose(sin(x), sin(x + tau))
     Out[5]: True

* ``os``, ``os.path`` の各 API が ``os.PathLike`` を受け付けるようになった。
* ``pathlib`` の各 API が ``os.PathLike`` を受け付けるようになった。
* ``random`` に関数 ``choices()`` が追加。
* ``re``

  * 大文字小文字無視オプションなどをグループにしか指定しない機能追加。
    例えば :regexp:`(?i:p)ython` は ``Python`` と ``python`` にしかマッチしな
    い。
  * マッチオブジェクトの :code:`m.group('name')` を :code:`m['name']` と書けるよ
    うになった。

* ``statistics``: ``harmonic_mean()`` 追加。

削除
======================================================================

* いくつかのモジュールに事実上新規に ``__all__`` を定義したので、既存のユーザー
  コードで :code:`from module import *` しているものは影響がある。
* ``json`` の API ですべてのオプション引数がキーワード専用引数になったので、既存
  のユーザーコードに影響する。
