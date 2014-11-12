======================================================================
NetworkX 利用ノート
======================================================================

本稿では Python のグラフライブラリーである NetworkX_ のインストール方法、
動作確認、簡単なグラフアルゴリズムの利用例、グラフのイメージ化方法について記す。
余裕があれば、高級なグラフアルゴリズムの応用例をいくつか示したい。

本稿でのグラフとは、計算機科学の教科書に書いてあるような、
ノードとエッジの集合うんぬんのグラフである。
変数と関数のとる値を座標平面にプロットした曲線ではない。
そちらについては :doc:`python-matplotlib` のほうが相応しい。

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
======================================================================
以降、次のインポートを断りなしに用いる。

.. code-block:: python3

  import networkx as nx
  import matplotlib.pyplot as plt

小さいグラフを定義して、単純な計算をさせてみることで NetworkX でのプログラミングの感触を確かめてみよう。

Dijkstra 法による最短経路
----------------------------------------------------------------------
以前行った、別のグラフライブラリーの試験に用いた問題設定を再利用する。
問題は「すべてのノードペアに対して、その最短経路の長さを得る」というものだ。

.. image:: /_static/apgl-findall.png
   :scale: 100%

NetworkX のリファレンスを当たると、関数 ``all_pairs_dijkstra_path_length``
を利用できることがわかる。
イラストのグラフの定義および最短経路の長さを計算するコードは次のようなものになる。

.. literalinclude:: ../sample/networkx/dijkstra.py
   :language: python3

この他にも NetworkX は Dijkstra の名を冠したアルゴリズムを複数実装しており、
「特定の始点終点の組み合わせの最短距離だけ求めたい」、
「経路のノードの順序も求めたい」等の細かい要求の違いにも応えられる。

実行結果は次のようなものになる。出力の見やすさにこだわりがなければ、
単に ``print(all_edges)`` でも各経路の最短距離を目視できる。

.. code-block:: none

   (0,1): 10.0
   (0,2): 14.0
   (0,3): 12.0
   (0,4): 29.0
   (0,5): 33.0
   (1,2):  8.0
   (1,3): 15.0
   (1,4): 19.0
   (1,5): 30.0
   (2,3):  7.0
   (2,5): 22.0
   (3,5): 21.0
   (4,5): 11.0

グラフィックを描画する
----------------------------------------------------------------------
先程のグラフを Matplotlib_ の表示機能を利用してウィンドウに出力する方法を示す。
試行錯誤の結果、次のコードが最も見やすいイメージを描画してくれた。

.. literalinclude:: ../sample/networkx/networkx-draw.py
   :language: python3

スクリプトをコンソールから実行すると、次のイメージを含む Matplotlib ウィンドウが開いたことがある。
毎回このイメージが描画されれば話は終わるのだが、困った点が見つかった。
NetworkX のグラフ描画ルーチンの特性上、クライアントが十分な描画用のパラメーターを与えないと、
ノードの位置をランダムに決定するようだ。
例えばこのコードを二度三度と実行してみるとよい。イメージがその度に異なっているのがわかるハズだ。
これでは作業の要件によっては支障をきたすかもしれない。

.. image:: /_static/networkx-draw.png
   :scale: 100%

Graphviz 形式に出力する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
NetworkX のグラフレイアウトを採用しないで、イメージを生成する方法があるらしい。

PyGraphviz_ が利用できる（これは Graphviz の利用可能性も含む）か、
もしくは pydot_ が利用できる（同様）環境であれば、
NetworkX の提供する次の関数を利用することができるようだ。

.. code-block:: python3

   nx.draw_graphviz(G)
   nx.write_dot(G,'file.dot')

出力の dot ファイルを Graphviz のエンジンに入力すれば、
先程のものよりはマシなイメージを得ることができるかもしれない。

さらなるグラフの応用例
======================================================================
TBW: Dijkstra 法だけではグラフライブラリーのノートとしては物足りない。
本格的なアルゴリズムの応用例を紹介したい。

.. _Python: http://www.python.org/
.. _NetworkX: https://networkx.github.io/
.. _Nose: http://somethingaboutorange.com/mrl/projects/nose/
.. _Numpy: http://scipy.org/NumPy/
.. _Matplotlib: http://matplotlib.sourceforge.net/
.. _PyGraphviz: http://pygraphviz.github.io/
.. _pydot: https://code.google.com/p/pydot/
