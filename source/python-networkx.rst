======================================================================
NetworkX 利用ノート
======================================================================

TBW: NetworkX パッケージの概要、グラフの概要、応用の例示を記述する。

.. contents:: ノート目次

.. note::

   * OS

     * Windows 7 Home Premium SP 1 64bit

   * 本稿において、利用した各パッケージのバージョンは次のとおり。

     * Python_: 3.4.1
     * NetworkX_: 1.9.1
     * Nose_: 1.3.4
     * Numpy_: 1.9.1
     * Matplotlib_: 1.4.2

関連リンク
======================================================================
NetworkX_
  公式サイト。インストール方法から基本的な利用方法、応用等が文書化されている。

関連ノート
======================================================================
* :doc:`python-nose`
* :doc:`python-matplotlib`

セットアップ
======================================================================
NetworkX 自身のインストールおよび、依存パッケージのインストールについて説明する。

NetworkX をインストールする
----------------------------------------------------------------------
NetworkX は純粋に Python モジュールの集合体として構成されているようなので（未確認）、
pip からインストールすればよい。

.. code-block:: console

   $ pip --install networkx

インストールの成功を確認する
----------------------------------------------------------------------
NetworkX のユニットテストを実行して、結果が正常であればインストール成功とみなそう。
Nose_ が環境にあれば、次の操作でテストの実行となる。
NumPy や SciPy のそれと同じスタイルなので馴染みやすい。

次のコードは、Python コマンドライン上から NetworkX のユニットテストを実行するものだ。

.. code-block:: pycon

   >> import networkx as nx
   >> nx.test(verbosity=2)
   Running NetworkX tests:test_approx_clust_coeff.test_petersen ... ok
   test_approx_clust_coeff.test_tetrahedral ... ok
   test_approx_clust_coeff.test_dodecahedral ... ok
   test_approx_clust_coeff.test_empty ... ok
   ... 省略 ...
   networkx.tests.test_relabel.TestRelabel.test_relabel_selfloop ... ok
   networkx.tests.test_relabel.TestRelabel.test_relabel_toposort ... ok

   ----------------------------------------------------------------------
   Ran 1741 tests in 77.348s

   OK (SKIP=4)

``verbosity=2`` でテストすると、いくつかスキップされる項目が出てくる。
これらより、NetworkX がサポートしていて現在の環境に存在しないサードパーティー製パッケージが判明する。

.. code-block:: none

   SKIP: PyGraphviz not available.
   SKIP: pydot not available.
   SKIP: ogr not available.
   SKIP: yaml not available.

NetworkX の基本的なコードの書き方を習得する
==================================================
以降、次のインポートを断りなしに用いる。

.. code-block:: python3

  import networkx as nx
  import matplotlib.pyplot as plt

TBW: グラフアルゴリズムの紹介とサンプルコードを適当に記述する。

.. _Python: http://www.python.org/
.. _NetworkX: https://networkx.github.io/
.. _Nose: http://somethingaboutorange.com/mrl/projects/nose/
.. _Numpy: http://scipy.org/NumPy/
.. _Matplotlib: http://matplotlib.sourceforge.net/
