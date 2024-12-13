======================================================================
Pytest 利用ノート
======================================================================

Python のテストフレームワークとして著名かつ人気のある pytest_ に関するノートだ。

.. contents:: 章見出し
   :local:

概要
======================================================================

   The pytest framework makes it easy to write small, readable tests, and can
   scale to support complex functional testing for applications and libraries.

インストール・更新・アンインストール
======================================================================

複数人で共用するプロジェクトの開発環境に pytest_ をインストールする事例では、そ
のプロジェクトの定める手順に従え。README や :file:`pyproject.toml` を読めば判明
する。

自分が所有する作業用仮想環境に pytest_ をインストールするならば、愛用している仮
想環境ツールがインストールコマンドを実装している場合にはそれを使え。私ならば
Miniconda_ であるから、例えば次のようにする：

.. sourcecode:: console
   :caption: 現在の conda 仮想環境に pytest をインストールする
   :force:

   conda install -c conda-forge pytest

仮想環境ツールがインストールコマンドを持っていない場合には、対象仮想環境が有効で
あることを確認してから :program:`pip` を使え：

.. sourcecode:: console
   :caption: 昔ながらの pip による pytest インストール手順例
   :force:

   pip install pytest

インストール手順の説明は以上だ。pytest_ の更新、アンインストールの手順は、対応す
る条件におけるインストール手順に合致する手順を選べ。例えば :program:`conda` を
使っているのならば ``conda uninstall pytest`` を走らせる、というようにだ。

構成・カスタマイズ
======================================================================

   Many pytest settings can be set in a `configuration file`, which by
   convention resides in the root directory of your repository.

Pytest_ はプロジェクトごとに構成ファイルを設ける流儀であり、ユーザー構成ファイル
は考えなくてよい。この節の目的は終わった。

何かの過渡期であるようで、ファイル書式が複数ある。プロジェクトのルートディレクト
リーに次のファイルのいずれかが置いてあれば、それが考慮される（この説明は厳密には
正しくないが、理解のためにそう記した）：

* :file:`pytest.ini`
* :file:`pyproject.toml` 内 ``tool.pytest.ini_options`` 区画
* :file:`tox.ini` 内 ``pytest`` 区画
* :file:`setup.cfg` 内 ``tool:pytest`` 区画

今の時代に INI ファイルは書きたくない。私は普通は :file:`pyproject.toml` を用い
る。次のようなコードを与える：

.. sourcecode:: toml
   :caption: :file:`pyproject.toml` における pytest 構成記述例
   :force:

   [tool.pytest.ini_options]
   addopts = "--color=yes --showlocals --strict-markers"
   asyncio_mode = "strict"
   doctest_optionflags = [
     "NORMALIZE_WHITESPACE",
     "ELLIPSIS"
   ]
   filterwarnings = [
     "error",
   ]
   log_cli_level = "INFO"
   markers = [
     "slow",
   ]
   minversion = "7.0"
   python_files = [
     "test_*.py",
     "__init__.py",
   ]
   testpaths = "tests"
   tmp_path_retention_policy = "failed"
   xfail_strict = true

オプションの名称と型は ``pytest --help`` から確認可能。

使用方法・コツ
======================================================================

全般
----------------------------------------------------------------------

.. todo::

   発見し次第追記する。

他のフレームワークから移行するコツ
----------------------------------------------------------------------

標準テストモジュール ``unittest`` を使って構築したテスト一式がある場合、pytest_
に適合させるための作業は本質的には発生しない。コマンドラインで起点となるパスと
PYTHONPATH を適当に指定すれば pytest_ は動作する。

Nose_ から移行する場合、nose2pytest_ を試せ。

資料集
======================================================================

何しろ人気パッケージであり、インターネットを検索すると高品質の記事がいたるところ
にある。それらをすぐに参照できるようにして整理しておくほうが、私が独りよがりな何
やらを書き殴るよりもはるかに良いだろう。

`pytest documentation`_
   公式文書。全ページに目を通せ。掲載コードを可能な限り検証しろ。紙幅の都合上、
   動作に足りないコード片があるものの、理解できている読者ならば補える。
`Effective Python Testing With pytest <https://realpython.com/pytest-python-testing/>`
   Real Python 内解説記事。
`Pytest — A beginner Guide <https://medium.com/@ronakchitlangya1997/pytest-a-beginner-guide-f9d4919cd427>`__
   入門記事で ``xfail`` と ``skip`` に触れているものは珍しい。
`Pytest vs Unittest: A Comparison <https://www.browserstack.com/guide/pytest-vs-unittest>`
   両者を徹底的に比較考量している。長所と短所を列挙し、各項目について双方の性質
   を述べている。記事の造りが堅実であり、すごく参考になる。
`Pytest vs. Unittest: Which Is Better? <https://blog.jetbrains.com/pycharm/2024/03/pytest-vs-unittest/>`__
   こちらも pytest と unittest の比較記事で、コードを示している。
`Pytest: Getting started with automated testing for Python <https://circleci.com/blog/pytest-python-testing/>`__
   CircleCI にある文書。単語 streamline がよく出てくることから、このテストフレー
   ムワークに期待される重要な性質が見えてくる。
`What Is pytest: A Complete pytest Tutorial With Best Practices <https://www.lambdatest.com/learning-hub/pytest-tutorial>`__
   Selenium を使ったアプリケーションのテストを pytest で実施するチュートリアルを
   含む記事（私はまだ試していない）。序盤の統計データも興味深い。

以上のほかにも優等記事が世にあるはずだ。

.. include:: /_include/python-refs-core.txt
.. _pytest documentation: https://docs.pytest.org/en/stable/
.. _nose2pytest: https://github.com/pytest-dev/nose2pytest
