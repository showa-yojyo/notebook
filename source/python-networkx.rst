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

残念ながら、現在どちらのパッケージとも Python 3 には公式に対応していないので、
上記コードを実行することができない。
出力の dot ファイルを Graphviz のエンジンに入力すれば、
先程のものよりはマシなイメージを得ることができるかもしれないだけに惜しい。

グラフ用語と実装要素の対応早見表
----------------------------------------------------------------------

* ``G`` はグラフクラスのいずれかのインスタンスを表す。状況で判断する。
* モジュール名を省略して記す。場合により ``nx`` 以外のものがある。
* 紙幅の都合上、関数、メソッド等の引数を一部省略しているか、またはまったく記していない。
  従って引数を取らないものと省略形との区別は（一度は本物のドキュメントまたはコードに当たらないと）できない。

================================================= =================================================
専門用語                                          関係のある機能
================================================= =================================================
acyclic                                           See acyclic graph.
acyclic graph                                     ``is_acyclic_directed_graph(G)``
adjacency matrix                                  ``adjacency_matric(G, ...)``
adjacent                                          ``G.adjacency_iter()``, ``G.neighbors(n)``, etc.
anti-edge                                         TBW
anti-triangle                                     TBW
arborescence                                      ``is_arborescence(G)``, i.e. ``is_tree(G) and max(G.in_degree().values()) > 1``.
arc                                               グラフが有向のときの edge の別名。
articulation point                                ``articulation_points(G)``
balanced k-partite graph                          UNKNOWN
biclique                                          ``k_clique_communities(G, 2, ...)``
biconnected                                       ``is_bi_connected(G)`` NetworkX では bi connected と綴るようだ。
biconnected component                             ``bi_connected_components(G)``, ``bi_connected_component_edges(G)``,
bipartite graph                                   ``is_partite(G)``, etc. 生成系メソッドが豊富にある。
biregular graph                                   regular 系は調査中
block                                             ``blockmodel(G, ...)``
bond                                              UNKNOWN
bridge                                            UNKNOWN
center                                            ``center(G, ...)``
circuit                                           See cycle.
circumference                                     UNKNOWN
claw                                              UNKNOWN
clique                                            ``find_cliques(G)``, ``k_clique_communities(G, 2, ...)``, 調査中。
clique number                                     ``graph_clique_number(G, ...)``, 調査中。
color, colored, identified                        ``color(G)``
complement                                        ``complement(G, ...)``
complete                                          See complete graph.
complete graph                                    ``complete_graph(k, ...)``.
complete multipartite graph                       ``complete_bipartite_graph(k1, k2, ...)`` まではある。
component                                         ``connected_components(G)``, ``number_connected_components(G)``, etc.
connected graph                                   ``is_connected(G)``, 
connectivity                                      ``all_pairs_node_connectivity(G, ...)``, ``edge_connectivity(G, ...)``, ``node_connectivity(G, ...)``, etc.
crossing                                          UNKNOWN
crossing number                                   UNKNOWN
cut                                               カット系は調査中
cut edge                                          カット系は調査中
cut set                                           カット系は調査中
cut vertex                                        カット系は調査中
cycle                                             ``G.add_cycle(...)``, ``cycle_basis(G, ...)``, ``simple_cycles(G)``
DAG                                               See acyclic graph.
degree                                            ``G.degree()``, ``G.in_degree()``, ``G.out_degree()``, ``G.degree_iter()``, ``G.in_degree_iter()``, ``G.out_degree_iter()``.
degree sequence                                   ``degree(G).values()`` で得られる。
diagram                                           UNKNOWN
diameter                                          ``diameter(G, ...)``
digon                                             UNKNOWN
digraph                                           See directed graph.
directed                                          See directed graph.
directed cycle                                    ``simple_cycles(G)``
directed graph                                    | ``DiGraph()``, ``MultiDiGraph()``.
                                                  | ``is_directed(G), ``G.to_directed()``.
disconnected graph                                調査中
disconnecting set                                 調査中
distance                                          調査中
dominate                                          See dominating set.
dominating set                                    ``dominating_set(G, ...)``, ``is_dominating_set(G, ...)``.
dual                                              UNKNOWN
eccentricity                                      ``eccentricity(G, ...)``
edge                                              ``G.edges()``, ``G.edges_iter()``, ``G.add_edge()``, ``G.add_edges_from()``, ``G.remove_edge()``, ``G.remove_edges_from()``, etc.
edge cut                                          カット系は調査中
edgeless graph                                    ``G.number_of_edges() == 0``, ``null_graph()``, ``trivial_graph()``.
embeddable                                        UNKNOWN
embedding                                         UNKNOWN
equipartite graph                                 UNKNOWN
Eulerian circuit                                  ``eulerian_circuit(G, ...)``
Eulerian cycle                                    See Eulerian circuit.
Eulerian digraph                                  ``is_eulerian(G)`` と ``G.is_directed()`` を用いる。
Eulerian path                                     TBW
Eulerian tour                                     TBW
Eulerian trail                                    TBW
even cycle                                        TBW
face                                              UNKNOWN
factor                                            TBW
forest                                            ``is_forest(G)``
girth                                             UNKNOWN
graph, network                                    ``Graph()``, ``DiGraph()``, ``MultiGraph()``, ``MultiDiGraph()``.
graph invariant                                   TBW
graph labeling                                    TBW
.. graph, network                                    TBW
Hamiltonian connected graph                       UNKNOWN
Hamiltonian cycle                                 UNKNOWN
Hamiltonian graph                                 UNKNOWN
Hamiltonian path                                  UNKNOWN
head                                              UNKNOWN
.. H-free graf                                       TBW
homomorphic                                       UNKNOWN
hyperedge                                         UNKNOWN
in degree                                         ``G.in_degree()``, ``G.in_degree_iter()``.
incident                                          ``incidence_matric(G, ...)``?
independence number                               UNKNOWN
independent                                       See independent set.
independent set                                   ``maximum_independent_set(G)``
induced subgraph                                  ``G.subgraph(nbunch)``
infinite                                          UNKNOWN
initial vertex                                    ``e = (v1, v2)`` とすると ``e1`` がそれ。
in-neighborhood                                   TBW
internally disjoint                               TBW
isolated vertex                                   ``isolates(G)``, ``is_isolate(G, n)``.
isomorphic                                        | ``is_isomorphic(G1, G2, ...)``, ``could_be_isomorphic(G1, G2, ...)``, fast_could_be_isomorphic(G1, G2, ...)``, ``faster_could_be_isomorphic(G1, G2, ...)``.
                                                  | 戻り値の意味からして用法には要注意。
isthmus                                           TBW
k-ary tree                                        TBW
k-clique                                          ``k_clique_communities(G, k, ...)``
k-colorable graph                                 TBW
k-connected                                       TBW
k-edge-connected                                  TBW
kernel                                            調査中
k-factor                                          TBW
knot                                              TBW
k-partite graph                                   NetworkX は k = 2 までサポートか。
k-regular graph                                   regular 系は調査中
k-spanner                                         TBW
k-th power                                        TBW
length of a cycle                                 多数ありそう。
length of a path or walk                          多数ありそう。
link                                              See edge.
loop                                              | 自己ループのことか？
                                                  | ``G.self_loop_edges()``, ``G.nodes_with_self_loops()``, ``G.number_of_self_loops()``.
.. loop, cycle                                       TBW*
matching number                                   TBW
maximum degree                                    TBW
minor                                             TBW
multigraph                                        ``MultiGraph()``, ``MultiDiGraph()``.
multipartite graph                                NetworkX は k = 2 までサポートか。
multiple                                          See multigraph.
multiple edge                                     TBW*
network                                           See graph.
null graph                                        ``null_graph()``
odd cycle                                         TBW
order                                             ``G.order()``
orientation                                       TBW
oriented graph                                    TBW
out degree                                        ``G.out_degree()``, ``G.out_degree_iter()``.
outer face                                        TBW
outerplanar graph                                 TBW
outerplane graph                                  TBW
out-neighborhood                                  TBW
pancyclic graph                                   TBW
partite set                                       TBW
path                                              ``G.add_path(...)``, 調査中。
perfect matching                                  TBW
peripheral vertex                                 TBW
planar graph                                      TBW
plane graph                                       TBW
point, node, vertex                               ``G.nodes()``, ``G.add_node()``, ``G.add_nodes_from()``, ``G.remove_node()``, ``G.remove_nodes_from()``, etc.
pseudograph                                       ``is_pseudographical(...)``
radius                                            ``radius(G, ...)``
reachable                                         関連機能多数
regular                                           regular 系は調査中
regular graph                                     regular 系は調査中
route                                             TBW
semiregular                                       regular 系は調査中
separating set                                    TBW
simple                                            See simple graph.
simple graph                                      ``Graph()``, ``DiGraph()``. 多重でないグラフの意。
sink                                              TBW
size of a graph                                   TBW
source                                            TBW
spanning matching                                 spanning 系は調査中
spanning subgraph                                 spanning 系は調査中
spanning tree                                     spanning 系は調査中
stable set                                        TBW
star                                              ``G.add_star(...)``, ``star_graph(k, ...)``.
.. staset                                            TBW
strongly connected                                ``is_strongly_connected(G)``
strongly connected component                      ``number_strongly_connected_components(G)``, ``strongly_connected_components(G)``, etc.
strongly regular graph                            regular 系は調査中
subgraph                                          関連機能多数
subtree                                           TBW
tail                                              TBW
terminal vertex                                   ``e = (v1, v2)`` とすると ``e2`` がそれ。
theta graph                                       TBW
thickness                                         TBW
totally disconnected graph                        TBW
tournament                                        TBW
traceable graph                                   TBW
traceable path                                    TBW
trail                                             TBW
tree                                              ``is_tree(G)``
triangle                                          ``triangles(G, ...)``
tripartite graph                                  NetworkX は k = 2 までサポートか。
undirected                                        ``Graph``, ``MultiGraph``. ``Di`` を冠していないグラフクラス。
undirected edge                                   ``Graph``, ``MultiGraph`` の edge の意。
unicyclic graph                                   TBW
unidentified                                      TBW
universal graph                                   TBW
unweighted                                        | ``single_source_shortest_path_length(G, ...)``, ``all_pairs_shortest_path_length(G, ...)``, etc.
                                                  | ``networkx.algorithms.shortest_paths.unweighted`` モジュールにあるもの。
valency                                           TBW
vertex                                            See point, node, vertex
vertex cut                                        カット系は調査中
walk                                              TBW
weakly connected                                  ``is_weakly_connected(G)``
weakly connected components                       ``number_weakly_connected_components(G)``, ``weakly_connected_components(G)``.
weight of a subgraph                              TBW
weighted                                          | ``dijkstra_path(G, ...)``, ``bellman_ford(G, ...)``, etc.
                                                  | ``networkx.algorithms.shortest_paths.weighted`` モジュールにあるもの。
weighted graph                                    ``G.add_weighted_edges_from(...)`` のように明示的に重み付きエッジをセットすることもある。
Wiener index of a graph                           TBW
Wiener index of a vertex                          TBW
Wiener polynomial of an undirected graph          TBW
================================================= =================================================

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
