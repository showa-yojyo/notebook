======================================================================
セットアップ
======================================================================

NetworkX_ 自身のインストールおよび、依存パッケージのインストールについて説明す
る。

.. contents::

NetworkX をインストールする
======================================================================

:ref:`miniconda-anchor-pip` の記述のとおりにインストールすればよい。

もしくは開発版レポジトリーからモジュールをクローンして、場合によっては改造して利
用するのもありだ。

.. code:: console

   bash$ git clone https://github.com/networkx/networkx.git
   ...
   bash$ cd networkx
   bash$ pip install -e .

インストールの成功を確認する
======================================================================

NetworkX の単体試験を実行して結果が正常であればインストール成功とみなそう。
Nose_ が環境にあれば次の操作で試験となる。NumPy_ や SciPy_ のそれと同じスタイル
なので馴染みやすい：

.. code:: pycon

   >>> import networkx as nx
   >>> nx.test(verbosity=2)
   Running NetworkX tests:test_approx_clust_coeff.test_petersen ... ok
   test_approx_clust_coeff.test_tetrahedral ... ok
   test_approx_clust_coeff.test_dodecahedral ... ok
   test_approx_clust_coeff.test_empty ... ok
   ... more results ...
   ----------------------------------------------------------------------
   Ran 2279 tests in 123.392s

   OK (SKIP=4)

``verbosity=2`` で呼び出すいくつかスキップされる項目が出てくる。これらより
NetworkX がサポートしていて現在の環境に存在しないサードパーティー製パッケージが
判明する。

.. code:: text

   SKIP: PyGraphviz not available.
   SKIP: pydot not available.
   SKIP: ogr not available.
   SKIP: yaml not available.

.. admonition:: 利用者ノート

   NetworkX 3.x ではテストモジュールがパッケージから取り除かれた。上記の単体テス
   ト実行関数は現存しない。Nose のことも忘れていい。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
.. _NetworkX: https://networkx.github.io/
