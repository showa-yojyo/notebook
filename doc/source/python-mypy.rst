======================================================================
mypy 利用ノート
======================================================================

.. contents:: 章見出し
   :local:

概要
======================================================================

   Mypy is a static type checker for Python.

型チェッカーというのは構文チェッカーの特殊なものであるとひとまず理解しておけばい
い。

   Type checkers help ensure that you're using variables and functions in your
   code correctly. With mypy, add type hints (`PEP 484`_) to your Python
   programs, and mypy will warn you when you use those types incorrectly.

Python 言語仕様には、変数、関数、クラス、等々のコード構成要素に対して、その型を
専用形式で注釈を付けることが可能であるというものがある。実際に型ヒントをコードに
付与するようになると実感できるが、Python コードの可読性が高まるという恩恵をも感
じる。関数の引数リストを見るだけで、実引数の型に関する必要条件がわかるというのは
読み書きにおいて大きい利点だ。Mypy_ はそのように注釈が付いたコードを解析、報告す
る道具の一つだと述べている。

   Python is a dynamic language, so usually you'll only see errors in your code
   when you attempt to run it. Mypy is a static checker, so it finds bugs in
   your programs without even running them!

型注釈付きコードを、それを実際に実行する前に検証することを mypy_ は目的とする。

インストール・更新・アンインストール
======================================================================

複数人で共用するプロジェクトの開発環境に mypy_ をインストールする事例では、その
プロジェクトの定める手順に従え。README や :file:`pyproject.toml` を読めば判明す
る。

自分が所有する作業用仮想環境にインストールするならば、愛用している仮想環境ツール
がインストールコマンドを実装している場合にはそれを使え。私ならば Miniconda_ であ
るから、例えば次のようにする：

.. sourcecode:: console
   :caption: 現在の conda 仮想環境に mypy をインストールする
   :force:

   conda install -c conda-forge mypy

インストール手順の説明は以上だ。mypy_ の更新、アンインストールの手順は、対応する
条件におけるインストール手順に合致する手順を選べ。例えば :program:`conda` を使っ
ているのならば ``conda uninstall mypy`` を走らせる。

.. seealso::

   :doc:`/python-miniconda`

構成・カスタマイズ
======================================================================

使用方法・コツ
======================================================================

資料集
======================================================================

`mypy documentation`_
   公式文書。First Step 章にあるページが重要だ。
`PEP 484 - Type Hints`_
   TBW

.. include:: /_include/python-refs-core.txt
.. _mypy:
.. _mypy documentation: https://mypy.readthedocs.io/en/stable/
.. _PEP 484:
.. _PEP 484 - Type Hints: https://peps.python.org/pep-0484/
