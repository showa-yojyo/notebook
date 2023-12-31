======================================================================
その他の話題
======================================================================

.. contents:: ノート目次

インストール
======================================================================

:ref:`python-pkg-proc` を参照。もっとも、Sphinx をインストールしたときに、
Docutils も同時に自動的にインストールされているはず。

各種スクリプト
======================================================================

:file:`$PYTHONHOME/Scripts` に次の Python スクリプトがある。これらが
:doc:`./core` で説明した関数 ``publish_cmdline`` をそのまま利用している。

* :file:`rst2html.py`
* :file:`rst2latex.py`
* :file:`rst2man.py`
* :file:`rst2odt.py`: これだけ関数 ``publish_cmdline_to_binary`` を利用。
* :file:`rst2pseudoxml.py`
* :file:`rst2s5.py`
* :file:`rst2xetex.py`
* :file:`rst2xml.py`
* :file:`rstpep2html.py`

各種オブジェクト生成関数
======================================================================

クライアントに直接コンストラクターを参照させないでオブジェクトを生成させる関数を
まとめる。

並列に置いてあるモジュールをオブジェクトとして返すパターン
----------------------------------------------------------------------

次の関数群が相当する。

* 関数 ``docutils.languages.get_language``
* 関数 ``docutils.parsers.rst.languages.get_language``

コードの構造については :doc:`./languages` で学習した。

モジュールで定義されている所定の名前のクラスを返すパターン
----------------------------------------------------------------------

通常ならばクライアントが対象のモジュールにあるクラスを ``import`` するところを、
所定のキーワードにより対応するクラスを返す関数を呼び出させることで、目的のオブ
ジェクトを生成させるというパターンがある。

次の関数群が相当する。

* 関数 ``docutils.parsers.get_parser_class``
* 関数 ``docutils.readers.get_reader_class``
* 関数 ``docutils.writers.get_writer_class``

いずれも次の擬似コードが示すような構造になっている。

.. code:: python3

   _xxxx_aliases = {
         'name1': 'subpkg1',
         'name2': 'subpkg2',
         ...
         }

   def get_xxxx_class(xxxx_name):
       """Return the Class class from the `xxxx_name` module."""
       xxxx_name = xxxx_name.lower()
       if xxxx_name in _xxxx_aliases:
           xxxx_name = _xxxx_aliases[xxxx_name]
       try:
           module = __import__(xxxx_name, globals(), locals(), level=1)
       except ImportError:
           module = __import__(xxxx_name, globals(), locals(), level=0)
       return module.Class

この関数が宣言されている :file:`__init__.py` が置いてあるディレクトリーにはサブ
パッケージ ``subpkg1``, ``subpkg2``, ... が置いてあるものとする。そしてモジュー
ル :file:`subpkg1/__init__.py` 等には必ずクラス ``Class`` が定義されているという
設計だ。クライアントはこの ``get_xxxx_class`` だけを ``import`` して、引数で単に
文字列を指定するだけで何かクラス ``Class`` が得られる。ただし、このクラスのオブ
ジェクトは生成されていないことに注意。ここからコンストラクターを誰かが呼び出すこ
とになる。

Python コードの手筋など
======================================================================

自分がこれまでほとんど使用してこなかったコードの手筋や技法を駆け足で列挙してい
く。

* クラスフィールド、およびその継承先での上書き
* 組み込み関数 ``__import__``

  * 現代では非推奨機能。代わりに ``importlib.import_module`` を使うらしい。

* 組み込み関数 ``getattr``, ``setattr``, ``hasattr``

  * ``getattr(x, 'y')`` は ``x.y`` を意味する。
  * ``setattr(x, 'y', v)`` は ``x.y = v`` を意味する。
  * 使用例としては :doc:`./visitor` がわかりやすい。

* ``__dict__`` は組み込み関数 ``dir`` のような情報にアクセスする。例えば型 ``X``
  に対して ``pprint.pprint(X.__dict__)`` するとよい。

  * 使用例：クラス ``doutils.parsers.rst.states.Struct`` 自体。
  * 使用例：クラス ``doutils.frontend.Values`` のメソッド ``copy`` の実装。

* ``__bool__`` をオーバーロードすることで、C++ でいうところの ``operator
  bool()`` の機能を真似できる。

* ``self.__class__.__name__`` とするとクラス名が ``str`` オブジェクトで得られる。

参考文献
======================================================================

`Docutils Project Documentation Overview <http://docutils.sourceforge.net/docs/>`_
  Docutils 公式技術文書群公開所。
`PEP 0258 -- Docutils Design Specification <https://www.python.org/dev/peps/pep-0258/>`_
  当ノートを執筆する前にこの文書に気付きたかった。

.. include:: /_include/python-refs-core.txt
