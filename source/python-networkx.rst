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
ここまで書いておいてなんだが、間違いが多そうだ。

* ``G``, ``G1``, ``G2``, ... 等はグラフクラスのいずれかのインスタンスを表す。
* ``n``, ``n1``, ``n2``, ... , ``s``, ``t`` 等はノードを指す。
* ``e``, ``e1``, ``e2``, ... 等はエッジを指す。
* ``k``, ``k1``, ``k2``, ... 等は 0 または正の整数を指す。
* モジュール名を省略して記す。場合により ``nx`` 以外のもの（グローバルやサブモジュール）がある。
* 紙幅の都合上、関数、メソッド等の引数を一部省略している。
* グラフ理論は応用範囲の広さゆえに同義語の多い用語が多い。この次の表でまとめる。

================================================= =================================================
専門用語                                          関係のある機能
================================================= =================================================
acyclic                                           See acyclic graph.
acyclic graph                                     ``is_directed_acyclic_graph(G)``, ``topological_sort(G, ...)``.
adjacency matrix                                  ``adjacency_matrix(G, ...)``
adjacency list                                    ``G.adjacency_list()``, ``G.adjacency_iter()``.
adjacent                                          ``G.adjacency_iter()``, ``G.neighbors(n)``, ``G[n]``, etc.
alternating path                                  TBW
ancestor                                          ``ancestors(G, n)``
anti-edge                                         ``not G.has_edge(n1, n2)``
anti-triangle                                     ``not (G.has_edge(n1, n2) and G.has_edge(n2, n3) and G.has_edge(n3, n1))``
arborescence                                      ``is_arborescence(G)``, i.e. ``is_tree(G) and max(G.in_degree().values()) > 1``.
arc                                               特にグラフが有向のときの edge の別名であることが多い。
articulation point                                ``articulation_points(G)``. a.k.a. cut vertex.
backward arc                                      TBW
balanced k-partite graph                          調査中
biclique                                          ``k_clique_communities(G, 2, ...)``
biconnected                                       ``is_biconnected(G)``
biconnected component                             ``biconnected_components(G)``, ``biconnected_component_edges(G)``,
bipartite graph                                   | ``is_bipartite(G)``, ``is_bipartite_node_set(G, nodes)``, ``sets(G)``.
                                                  | ``complete_bipartite_graph(n1, n2, ...)``, ``bipartite_random_graph(k1, k2, p, ...)``, etc. 生成系メソッドが豊富にある。
biregular graph                                   ``degs = G.degrees().values(); d = min(degs); D = max(degs); all(i == d or i == D for i in degs)``.
block                                             ``blockmodel(G, ...)``
block cut vertex tree                             TBW
block decomposition                               TBW
bond                                              UNKNOWN
branch                                            See edge.
bridge                                            UNKNOWN
Brook's theorem                                   TBW
capacity                                          フロー系関数の引数に見られる。
center                                            ``center(G, ...)``
child                                             ``G.predecessors(n)``
choosability                                      TBW
chromatic number                                  UNKNOWN
circuit                                           一般の circuit はないらしい。オイラー回路限定。See Eulerian circuit.
circumference                                     UNKNOWN
claw                                              UNKNOWN
clique                                            ``find_cliques(G)``, ``k_clique_communities(G, 2, ...)``, 調査中。
clique number                                     ``graph_clique_number(G, ...)``, 調査中。
color, colored, identified                        ``color(G)``
complement                                        ``complement(G, ...)``
complete                                          See complete graph.
complete graph                                    | ``complete_graph(k, ...)``.
                                                  | 参考までに ``networkx.algorithms.chordal.chordal_alg._is_complete_graph(G)`` を見ておくとよい。
complete multipartite graph                       | ``complete_bipartite_graph(k1, k2, ...)`` まではある。
                                                  | ``[0, k1)``, ``[k1, k1 + k2)`` がパーツ。
connected component                               | ``connected_components(G)``,
                                                  | ``connected_component_subgraphs(G)``,
                                                  | ``number_connected_components(G)``, etc.
connected graph                                   ``is_connected(G)``, i.e. ``number_connected_components(G) == 1``.
connectivity                                      | ``all_pairs_node_connectivity(G, ...)``,
                                                  | ``edge_connectivity(G, ...)``,
                                                  | ``node_connectivity(G, ...)``, etc.
cotree                                            ``G`` とその spanning tree のエッジ全部 ``T`` さえあれば ``C = Graph(); C.add_edges_from(set(G.edges()) - set(T.edges()))`` とか。
crossing                                          UNKNOWN
crossing number                                   UNKNOWN
cut                                               ``minimum_cut(G, s, t, ...)``
cut edge                                          ``minimum_edge_cut(G, ...)``, ``minimum_st_edge_cut(G, s, t, ...)``.
cut set                                           カット系関数の戻り値は cut set である。
cut vertex                                        ``minimum_node_cut(G, ...)``, ``minimum_st_node_cut(G, s, t, ...)``.
cycle                                             | ``G.add_cycle(...)``,
                                                  | ``cycle_basis(G, ...)``,
                                                  | ``simple_cycles(G)``,
                                                  | ``cycle_graph(k, ...)``.
DAG                                               See acyclic graph.
descendant                                        ``descendants(G, n)``
degree                                            | ``G.degree(...)``, ``G.degree_iter(...)``, 
                                                  | ``G.in_degree(...)``, ``G.in_degree_iter(...)``,
                                                  | ``G.out_degree(...)``, ``G.out_degree_iter(...)``.
                                                  | ``...`` はすべて ``nbunch=None, weight=None`` となっている。
degree sequence                                   ``degree(G).values()`` で得られる。
depth                                             See DFS.
DFS                                               | ``dfs_edges(G, source=None)``,
                                                  | ``dfs_labeled_edges(G, source=None)``,
                                                  | ``dfs_postorder_nodes(G, source=None)``,
                                                  | ``dfs_predecessors(G, source=None)``,
                                                  | ``dfs_preorder_nodes(G, source=None)``,
                                                  | ``dfs_successors(G, source=None)``,
                                                  | ``dfs_tree(G, source)``.
diagram                                           ``draw_networkx(G, ...)`` 系統の関数で図を出力する。
diameter                                          ``diameter(G, ...)``
digon                                             ``(i for i in simple_cycles(G) if len(i) == 2)``
digraph                                           See directed graph.
Dijkstra's algorithm                              ``single_source_dijkstra(G, s, ...)``,``dijkstra_path_length(G, s, t, ...)``, etc.
Dirac's theorem                                   ``n = len(G); all(d >= n/2 for d in G.degree().values())`` ならば ``G`` は Hamiltonian である。
directed                                          See directed graph.
directed cycle/circuit                            ``simple_cycles(G)``
directed graph                                    | ``DiGraph(...)``, ``MultiDiGraph(...)``.
                                                  | ``is_directed(G)``, ``G.to_directed()``.
directed tree                                     See arborescence.
disconnected graph                                ``not is_connected(G)``.
disconnecting set                                 調査中
distance                                          | ``shortest_path_length(G, ...)``,
                                                  | ``single_source_shortest_path_length(G, source, ...)``,
                                                  | ``single_source_dijkstra_path_length(G, source, ...)``, etc.
dominate                                          See dominating set.
dominating set                                    ``dominating_set(G, ...)``, ``is_dominating_set(G, ...)``.
dual                                              UNKNOWN
eccentricity                                      ``eccentricity(G, ...)``
edge                                              | ``G.edges(...)``, ``edges_iter(G, ...)``,
                                                  | ``G.add_edge(n1, n2, ...)``, ``G.add_edges_from(ebunch, ...)``,
                                                  | ``G.remove_edge(n1, n2)``, ``G.remove_edges_from(ebunch)``, etc.
edge cut                                          See cut edge.
edgeless graph                                    ``G.number_of_edges() == 0``, ``null_graph()``, ``trivial_graph()``.
elementary cycle                                  ``simple_cycles(G)``
elementary path                                   ``all_simple_paths(G, n1, n2)`` で代用するか。
embeddable                                        UNKNOWN
embedding                                         UNKNOWN
equipartite graph                                 UNKNOWN
Eulerian circuit                                  ``eulerian_circuit(G, ...)``
Eulerian digraph                                  ``is_eulerian(G)`` と ``G.is_directed()`` を用いる。
Eulerian path                                     ``eulerian_circuit(G, ...)`` では求まらない？
Eulerian tour                                     See Eulerian circuit.
Eulerian trail                                    See Eulerian path.
end block                                         TBW
even cycle                                        ``(i for i in simple_cycles(G) if len(i) % 2 == 0)``
face                                              UNKNOWN
factor                                            TBW
flow augmenting method                            TBW
flow augmenting path                              ``shortest_augmenting_path(G, s, t, ...)``
forest                                            ``is_forest(G)``
forward arc                                       TBW
fundamental cycle/circuit                         TBW
fundamental cut set                               TBW
girth                                             UNKNOWN
graph                                             ``Graph(...)``, ``DiGraph(...)``, ``MultiGraph(...)``, ``MultiDiGraph(...)``.
graph invariant                                   TBW
graph labeling                                    ``G.graph[label] = value``, ``G.node[n][label] = value``, ``G.edge[e][label] = value``, etc.
Hamiltonian connected graph                       UNKNOWN
Hamiltonian cycle                                 UNKNOWN
Hamiltonian graph                                 UNKNOWN
Hamiltonian path                                  UNKNOWN
head                                              See initial vertex.
height                                            練習問題とする。
homomorphic                                       UNKNOWN
hyperedge                                         UNKNOWN
in degree                                         ``G.in_degree(...)``, ``G.in_degree_iter(...)``.
incident                                          ``incidence_matrix(G, ...)``
independence number                               UNKNOWN
independent                                       See independent set.
independent set                                   ``maximum_independent_set(G)``
induced subgraph                                  ``subgraph(G, nbunch)``
infinite                                          NetworkX は infinite graph をサポートしていないだろう。
initial vertex                                    | (1) 有向エッジ ``e = (v1, v2)`` とすると ``e1`` がそれ。
                                                  | (2) walk の始点という意味を採る文献あり。
in-neighborhood                                   ``G.predecessors(n)``
internally disjoint                               TBW
isolated vertex                                   ``isolates(G)``, ``is_isolate(G, n)``.
isomorphic                                        | ``is_isomorphic(G1, G2, ...)``,
                                                  | ``could_be_isomorphic(G1, G2, ...)``, ``fast_could_be_isomorphic(G1, G2, ...)``, ``faster_could_be_isomorphic(G1, G2, ...)``.
                                                  | 戻り値の意味からして用法には要注意。
isthmus                                           See bridge.
k-ary tree                                        練習問題とする。
k-choosable                                       TBW
k-clique                                          ``k_clique_communities(G, k, ...)``
k-colorable graph                                 UNKNOWN
k-connected                                       See k-vertex connected.
k-edge connected                                  TBW
k-factor                                          TBW
k-vertex connected                                TBW
k-partite graph                                   NetworkX は k = 2 までサポートか。
k-regular graph                                   See regular graph.
k-spanner                                         TBW
k-th power                                        TBW
kernel                                            調査中
knot                                              TBW
Kruskal's algorithm                               ``minimum_spanning_edges(G, ...)``, ``minimum_spanning_tree(G, ...)``.
labeling method                                   TBW
leaf                                              有向木 ``G`` に対して ``[n for n,d in G.out_degree().items() if d == 0]``
length of a cycle/circuit                         ``len(ebunch)``, ``len(nbunch)``.
length of a walk                                  ``len(ebunch)``, ``len(nbunch) - 1``.
list-chromatic number                             TBW
list coloring                                     TBW
list function                                     TBW
loop                                              ``G.nodes_with_selfloops()``, ``G.selfloop_edges(...)``, ``G.number_of_selfloops()``.
matching                                          ``min_maximal_matching(G)``
matching number                                   TBW
maximum degree                                    ``max(degree(G).values())``
maximum flow                                      ``maximum_flow(G, s, t, ...)``, ``maximum_flow_value(G, s, t, ...)``.
maximum matching                                  ``maximal_matching(G)``, ``max_weight_matching(G, ...)``
Menger's theorem                                  TBW
minimum degree                                    ``min(degree(G).values())``
minimum spanning tree                             ``minimum_spanning_tree(G, ...)``
minor                                             TBW
multigraph                                        ``MultiGraph(...)``, ``MultiDiGraph(...)``.
multipartite graph                                NetworkX は k = 2 までサポートか。
multiple                                          See multigraph.
multiple edge                                     練習問題とする。
node                                              | ``G.nodes(...)``,
                                                  | ``G.add_node(n, ...)``, ``G.add_nodes_from(nodes, ...)``,
                                                  | ``G.remove_node(n)``, ``G.remove_nodes_from(nodes)``,
                                                  | ``G.has_node(n)``, etc.
null graph                                        ``null_graph()``
odd cycle                                         ``(i for i in simple_cycles(G) if len(i) % 2 == 1)``
order                                             ``G.order()``, ``G.number_of_nodes()``.
orientation                                       TBW
oriented graph                                    directed graph と同義ではないのか。
out degree                                        ``G.out_degree(...)``, ``G.out_degree_iter(...)``.
outer face                                        TBW
outerplanar graph                                 TBW
outerplane graph                                  TBW
out-neighborhood                                  ``G.successors(n)``
pancyclic graph                                   練習問題とする。
parent                                            ``G.predecessors(n)``
partite set                                       TBW
path                                              ``G.add_path(...)``, 調査中。
perfect graph                                     TBW
perfect matching                                  TBW
peripheral vertex                                 ``ecc = eccentricity(G); M = max(ecc); (k for k, v in ecc.items() if v == M)``
Petersen                                          ``petersen_graph(...)``
planar graph                                      TBW
plane graph                                       TBW
Prim's algorithm                                  使われていないのではないか。
pseudograph                                       ``is_pseudographical(...)``
radius                                            ``radius(G, ...)``
reachable                                         ``single_source_dijkstra(G, n1, n2=None, ...)``
regular                                           See regular graph.
regular graph                                     ``d = degree(G); all(d[0] == i for i in d.values())``
resitual network                                  ``build_residual_network(G, capacity)``
root node                                         有向木 ``G`` に対して ``[n for n,d in G.in_degree().items() if d == 0][0]``
rooted tree                                       See arborescence.
saturated                                         TBW
semiregular                                       regular 系は調査中
separating set                                    See cut set.
shortest path                                     ``shortest_path(G, ...)``, ``all_shortest_path(G, s, t, ...)``, etc.
simple                                            See simple graph.
simple cycle                                      ``simple_cycles(G)``. See also simple path.
simple graph                                      ``Graph()``, ``DiGraph()``. 多重でないグラフの意。
simple path                                       ``all_simple_paths(G, n1, n2)`` ですべての路が求まる。
sink                                              ``(n for n in G if G.out_degree(n) == 0)``
size of a graph                                   ``G.size(...)``. エッジの本数もしくはエッジの重みの和。
source                                            ``(n for n in G if G.in_degree(n) == 0)``
spanning matching                                 See perfect matching.
spanning subgraph                                 ``G`` から任意のエッジ（複数可）を取り除けば得られる。
spanning tree                                     ``nx.minimum_spanning_tree(G, ...)``, ただし入力によっては tree というよりは forest が得られる。
stable set                                        See independent set.
star                                              ``G.add_star(...)``, ``star_graph(k, ...)``.
staset                                            See independent set.
strongly connected                                ``is_strongly_connected(G)``
strongly connected component                      | ``strongly_connected_components(G)``,
                                                  | ``strongly_connected_component_subgraphs(G)``,
                                                  | ``number_strongly_connected_components(G)``, etc.
strongly regular graph                            練習問題とする。
subdivision                                       TBW
subgraph                                          | ``subgraph(G, nbunch)`` による部分グラフは指定点集合からの induced subgraph である。
                                                  | ``attracting_component_subgraphs(G, ...)``, etc. 関連機能多数。
subtree                                           ``nx.is_tree(H)``, ``H`` はグラフ ``G`` の部分グラフ。
tail                                              See terminal vertex.
terminal vertex                                   | (1) ``e = (v1, v2)`` とすると ``e2`` がそれ。
                                                  | (2) walk の終点という意味を採る文献あり。
theta graph                                       TBW
thickness                                         TBW
totally disconnected graph                        TBW
tour                                              See circuit.
tournament                                        ``complete_graph(k, ...).to_directed()``
traceable graph                                   TBW
traceable path                                    TBW
trail                                             より条件の厳しい path 系の機能で代用する？
tree                                              | ``is_tree(G)``. ``G`` が無向でも有向でも多重でも機能する（単純無向グラフ扱いして判定する）。
                                                  | ``dfs_tree(G, n)`` で ``G`` からノード ``n`` を root とする有向木を生成できる。
triangle                                          ``triangles(G, ...)``
tripartite graph                                  NetworkX は k = 2 までサポートか。
Tutte's theorem                                   TBW
undirected                                        See undirected graph.
undirected edge                                   ``Graph``, ``MultiGraph`` の edge の意。
undirected graph                                  | ``Graph``, ``MultiGraph``. ``Di`` を冠していないクラスが無向グラフ。
                                                  | ``not is_directed(G)``, ``G.to_undirected()``.
unicyclic graph                                   TBW
unidentified                                      TBW
universal graph                                   See complete graph.
unsaturated                                       TBW
unweighted                                        NetworkX のエッジ関連アルゴリズムは、原則的にエッジの weight を参照するか否かを指定できる。
valency                                           See degree.
walk                                              より条件の厳しい path 系の機能で代用する？
weakly connected                                  ``is_weakly_connected(G)``
weakly connected components                       ``number_weakly_connected_components(G)``, ``weakly_connected_components(G)``.
weight of a subgraph                              練習問題とする。
weighted                                          See weighted graph.
weighted graph                                    | ``G.edge[e]['weight'] = value``
                                                  | ``G.add_weighted_edges_from(...)`` のように明示的に重み付きエッジをセットすることもある。
Whitney's theorem                                 TBW 複数あるか。
================================================= =================================================

次に頻出の同義語・類義語リストを示す。なるべく先頭の単語を優先して記した。

* グラフ graph/network
* ノード node/vertex/point/site
* エッジ edge/link/branch/line/(arc)

  * arc は有向グラフのエッジの意味にとることが多いようだ。

* 閉路 cycle/circuit/tour/closed path

  * ただし（端点以外での）ノードの重複を許すものを circuit, そうでないものを cycle と呼ぶことにする。
    すなわち closed path の意味でのみ cycle と呼び、
    それ以外は closed trail という意味で circuit, tour が同義語とみなすらしい。

* 道 walk/route

さらなるグラフの応用例
======================================================================
.. todo::

   Dijkstra 法だけではグラフライブラリーのノートとしては物足りない。
   本格的なアルゴリズムの応用例を紹介したい。

.. _Python: http://www.python.org/
.. _NetworkX: https://networkx.github.io/
.. _Nose: http://somethingaboutorange.com/mrl/projects/nose/
.. _Numpy: http://scipy.org/NumPy/
.. _Matplotlib: http://matplotlib.sourceforge.net/
.. _PyGraphviz: http://pygraphviz.github.io/
.. _pydot: https://code.google.com/p/pydot/
