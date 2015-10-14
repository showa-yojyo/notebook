セットアップ
======================================================================
NetworkX_ 自身のインストールおよび、依存パッケージのインストールについて説明する。

.. contents::

NetworkX をインストールする
----------------------------------------------------------------------
NetworkX は純粋に Python モジュールの集合体として構成されているようなので（未確認）、
pip からインストールすればよい。

.. code-block:: console

   $ pip --install networkx

もしくは開発版レポジトリーからクローンして改造して利用するのもありだ。
場合によっては master ブランチを利用せず、任意の過去バージョンのブランチをチェックアウトすることも考えられる。

.. code-block:: console

   $ git clone https://github.com/networkx/networkx.git
   ...
   $ cd networkx
   $ pip install -e .

インストールの成功を確認する
----------------------------------------------------------------------
NetworkX のユニットテストを実行して、結果が正常であればインストール成功とみなそう。
Nose_ が環境にあれば、次の操作でテストの実行となる。
NumPy_ や SciPy_ のそれと同じスタイルなので馴染みやすい。

次のコードは、Python コマンドライン上から NetworkX のユニットテストを実行するものだ。

.. code-block:: pycon

   >> import networkx as nx
   >> nx.test(verbosity=2)
   Running NetworkX tests:test_approx_clust_coeff.test_petersen ... ok
   test_approx_clust_coeff.test_tetrahedral ... ok
   test_approx_clust_coeff.test_dodecahedral ... ok
   test_approx_clust_coeff.test_empty ... ok
   ... 省略 ...
   ----------------------------------------------------------------------
   Ran 2272 tests in 136.216s

   FAILED (SKIP=4, errors=1, failures=1)

``verbosity=2`` でテストすると、いくつかスキップされる項目が出てくる。
これらより、NetworkX がサポートしていて現在の環境に存在しないサードパーティー製パッケージが判明する。

.. code-block:: none

   SKIP: PyGraphviz not available.
   SKIP: pydot not available.
   SKIP: ogr not available.
   SKIP: yaml not available.

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
.. _NetworkX: https://networkx.github.io/
