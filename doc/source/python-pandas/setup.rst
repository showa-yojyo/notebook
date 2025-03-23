======================================================================
環境構築
======================================================================

Pandas_ の環境構築について記す。当ノート著者は Windows PC でプログラミング作業を
しており、 Python_ は Windows Subsystem for Linux (Ubuntu) 環境に Miniconda_ を
インストールすることでそのサードパーティー製ライブラリーを管理している。

.. contents::

ドキュメント準備
======================================================================

オフライン環境で Pandas_ のドキュメントを読めるようにしておく。公式サイトから
Download documentation と書いてあるところの隣のリンクから HTML ファイル版のをダ
ウンロードして、ブラウザーにトップページのブックマークを追加しておく。

インストール
======================================================================

Pandas 本体をインストールする
----------------------------------------------------------------------

上述の理由から、Miniconda の適当な仮想環境を ``conda activate`` した状態で次の一
行を実行することで終わる。

.. code:: console

   bash$ conda install pandas

依存ライブラリーも同時にインストールされるので、これだけで Pandas_ のチュートリ
アルの大部分を実行可能な環境ができる。

お好みでその他のライブラリーをインストールする
----------------------------------------------------------------------

Pandas_ を利用する目的にもよるが、以下に挙げるサードパーティー製ライブラリーも併
せてインストールしておくと良いとされている：

* pytest_, Hypothesis_: 後述する単体テストを実行するため。
* BeautifulSoup4_, lxml_: HTML ファイルを読み込んで DataFrame を生成するため。
* openpyxl_, XLsxWriter, xlrd, xlwt: MS Excel ファイルとの I/O 機能を利用するた
  め。
* Matplotlib_: DataFrame オブジェクトをプロットするため。
* numexpr_, bottleneck_: ある種の計算速度を向上させるため。この二つについては公
  式ドキュメントが recommended dependencies であると述べている。

いずれのライブラリーについても、インストール手段はコンソールからの ``conda
install`` コマンドまたは ``pip install`` コマンドを実行することによる。

テスト
======================================================================

IPython_ のセッションを起動して、次のように単体テストを実行する：

.. code:: ipython

   In [1]: import pandas as pd

   In [2]: pd.test()
   running: pytest --skip-slow --skip-network --skip-db /home/$USER/miniconda3/envs/python-3.9/lib/python3.9/site-packages/pandas
   ================================================= test session starts ==================================================
   platform linux -- Python 3.9.1, pytest-6.2.2, py-1.10.0, pluggy-0.12.0
   rootdir: /home/$USER
   plugins: hypothesis-6.1.0
   collected 152308 items / 14 skipped / 152294 selected

   miniconda3/envs/python-3.9/lib/python3.9/site-packages/pandas/tests/test_aggregation.py ........                 [  0%]
   miniconda3/envs/python-3.9/lib/python3.9/site-packages/pandas/tests/test_algos.py .............................. [  0%]
   （略）
   ========== 22 failed, 134718 passed, 16562 skipped, 1010 xfailed, 3 warnings, 10 errors in 2525.42s (0:42:05) ==========
   An exception has occurred, use %tb to see the full traceback.

   SystemExit: ExitCode.TESTS_FAILED

   /home/$USER/miniconda3/envs/python-3.9/lib/python3.9/site-packages/IPython/core/interactiveshell.py:3426: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.
     warn("To exit: use 'exit', 'quit', or Ctrl-D.", stacklevel=1)

   In [3]:

関連ノート
======================================================================

Python のサードパーティー製ライブラリーのインストール手段全般についてのノートが
すでにある。

* :doc:`/python-upgrade`
* :doc:`/python-miniconda`
* :doc:`/python-pip`

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
.. _Hypothesis: https://hypothesis.readthedocs.io/
.. _openpyxl: https://openpyxl.readthedocs.io/
.. _numexpr: https://github.com/pydata/numexpr
.. _bottleneck: https://github.com/pydata/bottleneck
.. _BeautifulSoup4: https://www.crummy.com/software/BeautifulSoup
.. _lxml: https://lxml.de/
