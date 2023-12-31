======================================================================
セットアップ
======================================================================

NetworkX_ 自身のインストールおよび、依存パッケージのインストールについて説明す
る。

.. contents::

NetworkX をインストールする
======================================================================

:ref:`python-pkg-proc` のとおりにインストールすればよい。

もしくは開発版レポジトリーからモジュールをクローンして、場合によっては改造して利
用するのもありだ。

.. code:: console

   bash$ git clone https://github.com/networkx/networkx.git
   ...
   bash$ cd networkx
   bash$ pip install -e .

インストールの成功を確認する
======================================================================

NetworkX のユニットテストを実行して、結果が正常であればインストール成功とみなそ
う。Nose_ が環境にあれば、次の操作でテストの実行となる。 NumPy_ や SciPy_ のそれ
と同じスタイルなので馴染みやすい。

次のコードは、Python コマンドライン上から NetworkX のユニットテストを実行するも
のだ：

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

``verbosity=2`` でテストすると、いくつかスキップされる項目が出てくる。これらよ
り、NetworkX がサポートしていて現在の環境に存在しないサードパーティー製パッケー
ジが判明する。

.. code:: text

   SKIP: PyGraphviz not available.
   SKIP: pydot not available.
   SKIP: ogr not available.
   SKIP: yaml not available.

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
.. _NetworkX: https://networkx.github.io/
