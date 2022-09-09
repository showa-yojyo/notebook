======================================================================
グラフ用語と実装要素の対応早見表
======================================================================
ここまで書いておいてなんだが、間違いが多そうだ。

.. contents::

* ``G``, ``G1``, ``G2``, ... 等はグラフクラスのいずれかのインスタンスを表す。
* ``n``, ``n1``, ``n2``, ... , ``s``, ``t`` 等はノードを指す。
* ``e``, ``e1``, ``e2``, ... 等はエッジを指す。
* ``k``, ``k1``, ``k2``, ... 等は 0 または正の整数を指す。
* モジュール名を省略して記す。
  場合により ``nx`` 以外のもの（グローバルやサブモジュール）がある。
* 紙幅の都合上、関数、メソッド等の引数を一部省略している。
* グラフ理論は応用範囲の広さゆえに同義語の多い用語が多い。
  この次の表でまとめる。

================================================= =================================================
専門用語                                          関係のある機能
================================================= =================================================
acyclic                                           See acyclic graph.
acyclic graph                                     :code:`is_directed_acyclic_graph(G)`, :code:`topological_sort(G, ...)`.
adjacency matrix                                  :code:`adjacency_matrix(G, ...)`
adjacency list                                    :code:`G.adjacency_list()`, :code:`G.adjacency_iter()`.
adjacent                                          :code:`G.adjacency_iter()`, :code:`G.neighbors(n)`, :code:`G[n]`, etc.
alternating path                                  TBW
ancestor                                          :code:`ancestors(G, n)`
anti-edge                                         :code:`not G.has_edge(n1, n2)`
anti-triangle                                     :code:`not (G.has_edge(n1, n2) and G.has_edge(n2, n3) and G.has_edge(n3, n1))`
arborescence                                      :code:`is_arborescence(G)`, i.e. :code:`is_tree(G) and max(G.in_degree().values()) > 1`.
arc                                               特にグラフが有向のときの edge の別名であることが多い。
articulation point                                :code:`articulation_points(G)`. a.k.a. cut vertex.
backward arc                                      TBW
balanced k-partite graph                          調査中
biclique                                          :code:`k_clique_communities(G, 2, ...)`
biconnected                                       :code:`is_biconnected(G)`
biconnected component                             :code:`biconnected_components(G)`, :code:`biconnected_component_edges(G)`,
bipartite graph                                   | :code:`is_bipartite(G)`, :code:`is_bipartite_node_set(G, nodes)`, :code:`sets(G)`.
                                                  | :code:`complete_bipartite_graph(n1, n2, ...)`, :code:`bipartite_random_graph(k1, k2, p, ...)`, etc. 生成系メソッドが豊富にある。
biregular graph                                   :code:`degs = G.degrees().values(); d = min(degs); D = max(degs); all(i == d or i == D for i in degs)`.
block                                             :code:`blockmodel(G, ...)`
block cut vertex tree                             TBW
block decomposition                               TBW
bond                                              UNKNOWN
branch                                            See edge.
bridge                                            UNKNOWN
Brook's theorem                                   TBW
capacity                                          フロー系関数の引数に見られる。
center                                            :code:`center(G, ...)`
child                                             :code:`G.predecessors(n)`
choosability                                      TBW
chromatic number                                  UNKNOWN
circuit                                           一般の circuit はないらしい。オイラー回路限定。See Eulerian circuit.
circumference                                     UNKNOWN
claw                                              UNKNOWN
clique                                            :code:`find_cliques(G)`, :code:`k_clique_communities(G, 2, ...)`, 調査中。
clique number                                     :code:`graph_clique_number(G, ...)`, 調査中。
color, colored, identified                        :code:`color(G)`
complement                                        :code:`complement(G, ...)`
complete                                          See complete graph.
complete graph                                    | :code:`complete_graph(k, ...)`.
                                                  | 参考までに :code:`networkx.algorithms.chordal.chordal_alg._is_complete_graph(G)` を見ておくとよい。
complete multipartite graph                       | :code:`complete_bipartite_graph(k1, k2, ...)` まではある。
                                                  | ``[0, k1)``, ``[k1, k1 + k2)`` がパーツ。
connected component                               | :code:`connected_components(G)`,
                                                  | :code:`connected_component_subgraphs(G)`,
                                                  | :code:`number_connected_components(G)`, etc.
connected graph                                   :code:`is_connected(G)`, i.e. :code:`number_connected_components(G) == 1`.
connectivity                                      | :code:`all_pairs_node_connectivity(G, ...)`,
                                                  | :code:`edge_connectivity(G, ...)`,
                                                  | :code:`node_connectivity(G, ...)`, etc.
cotree                                            ``G`` とその spanning tree のエッジ全部 ``T`` さえあれば :code:`C = Graph(); C.add_edges_from(set(G.edges()) - set(T.edges()))` とか。
crossing                                          UNKNOWN
crossing number                                   UNKNOWN
cut                                               :code:`minimum_cut(G, s, t, ...)`
cut edge                                          :code:`minimum_edge_cut(G, ...)`, :code:`minimum_st_edge_cut(G, s, t, ...)`.
cut set                                           カット系関数の戻り値は cut set である。
cut vertex                                        :code:`minimum_node_cut(G, ...)`, :code:`minimum_st_node_cut(G, s, t, ...)`.
cycle                                             | :code:`G.add_cycle(...)`,
                                                  | :code:`cycle_basis(G, ...)`,
                                                  | :code:`simple_cycles(G)`,
                                                  | :code:`cycle_graph(k, ...)`.
DAG                                               See acyclic graph.
descendant                                        :code:`descendants(G, n)`
degree                                            | :code:`G.degree(...)`, :code:`G.degree_iter(...)`, 
                                                  | :code:`G.in_degree(...)`, :code:`G.in_degree_iter(...)`,
                                                  | :code:`G.out_degree(...)`, :code:`G.out_degree_iter(...)`.
                                                  | ``...`` はすべて :code:`nbunch=None, weight=None` となっている。
degree sequence                                   :code:`degree(G).values()` で得られる。
depth                                             See DFS.
DFS                                               | :code:`dfs_edges(G, source=None)`,
                                                  | :code:`dfs_labeled_edges(G, source=None)`,
                                                  | :code:`dfs_postorder_nodes(G, source=None)`,
                                                  | :code:`dfs_predecessors(G, source=None)`,
                                                  | :code:`dfs_preorder_nodes(G, source=None)`,
                                                  | :code:`dfs_successors(G, source=None)`,
                                                  | :code:`dfs_tree(G, source)`.
diagram                                           :code:`draw_networkx(G, ...)` 系統の関数で図を出力する。
diameter                                          :code:`diameter(G, ...)`
digon                                             :code:`(i for i in simple_cycles(G) if len(i) == 2)`
digraph                                           See directed graph.
Dijkstra's algorithm                              :code:`single_source_dijkstra(G, s, ...)`, :code:`dijkstra_path_length(G, s, t, ...)`, etc.
Dirac's theorem                                   :code:`n = len(G); all(d >= n/2 for d in G.degree().values())` ならば ``G`` は Hamiltonian である。
directed                                          See directed graph.
directed cycle/circuit                            :code:`simple_cycles(G)`
directed graph                                    | :code:`DiGraph(...)`, :code:`MultiDiGraph(...)`.
                                                  | :code:`is_directed(G)`, :code:`G.to_directed()`.
directed tree                                     See arborescence.
disconnected graph                                :code:`not is_connected(G)`.
disconnecting set                                 調査中
distance                                          | :code:`shortest_path_length(G, ...)`,
                                                  | :code:`single_source_shortest_path_length(G, source, ...)`,
                                                  | :code:`single_source_dijkstra_path_length(G, source, ...)`, etc.
dominate                                          See dominating set.
dominating set                                    :code:`dominating_set(G, ...)`, :code:`is_dominating_set(G, ...)`.
dual                                              UNKNOWN
eccentricity                                      :code:`eccentricity(G, ...)`
edge                                              | :code:`G.edges(...)`, :code:`edges_iter(G, ...)`,
                                                  | :code:`G.add_edge(n1, n2, ...)`, :code:`G.add_edges_from(ebunch, ...)`,
                                                  | :code:`G.remove_edge(n1, n2)`, :code:`G.remove_edges_from(ebunch)`, etc.
edge cut                                          See cut edge.
edgeless graph                                    :code:`G.number_of_edges() == 0`, :code:`null_graph()`, :code:`trivial_graph()`.
elementary cycle                                  :code:`simple_cycles(G)`
elementary path                                   :code:`all_simple_paths(G, n1, n2)` で代用するか。
embeddable                                        UNKNOWN
embedding                                         UNKNOWN
equipartite graph                                 UNKNOWN
Eulerian circuit                                  :code:`eulerian_circuit(G, ...)`
Eulerian digraph                                  :code:`is_eulerian(G)` と :code:`G.is_directed()` を用いる。
Eulerian path                                     :code:`eulerian_circuit(G, ...)` では求まらない？
Eulerian tour                                     See Eulerian circuit.
Eulerian trail                                    See Eulerian path.
end block                                         TBW
even cycle                                        :code:`(i for i in simple_cycles(G) if len(i) % 2 == 0)`
face                                              UNKNOWN
factor                                            TBW
flow augmenting method                            TBW
flow augmenting path                              :code:`shortest_augmenting_path(G, s, t, ...)`
forest                                            :code:`is_forest(G)`
forward arc                                       TBW
fundamental cycle/circuit                         TBW
fundamental cut set                               TBW
girth                                             UNKNOWN
graph                                             :code:`Graph(...)`, :code:`DiGraph(...)`, :code:`MultiGraph(...)`, :code:`MultiDiGraph(...)`.
graph invariant                                   TBW
graph labeling                                    :code:`G.graph[label] = value`, :code:`G.node[n][label] = value`, :code:`G.edge[e][label] = value`, etc.
Hamiltonian connected graph                       UNKNOWN
Hamiltonian cycle                                 UNKNOWN
Hamiltonian graph                                 UNKNOWN
Hamiltonian path                                  UNKNOWN
head                                              See initial vertex.
height                                            練習問題とする。
homomorphic                                       UNKNOWN
hyperedge                                         UNKNOWN
in degree                                         :code:`G.in_degree(...)`, :code:`G.in_degree_iter(...)`.
incident                                          :code:`incidence_matrix(G, ...)`
independence number                               UNKNOWN
independent                                       See independent set.
independent set                                   :code:`maximum_independent_set(G)`
induced subgraph                                  :code:`subgraph(G, nbunch)`
infinite                                          NetworkX は infinite graph をサポートしていないだろう。
initial vertex                                    | (1) 有向エッジ :code:`e = (v1, v2)` とすると ``e1`` がそれ。
                                                  | (2) walk の始点という意味を採る文献あり。
in-neighborhood                                   :code:`G.predecessors(n)`
internally disjoint                               TBW
isolated vertex                                   :code:`isolates(G)`, :code:`is_isolate(G, n)`.
isomorphic                                        | :code:`is_isomorphic(G1, G2, ...)`,
                                                  | :code:`could_be_isomorphic(G1, G2, ...)`, :code:`fast_could_be_isomorphic(G1, G2, ...)`, :code:`faster_could_be_isomorphic(G1, G2, ...)`.
                                                  | 戻り値の意味からして用法には要注意。
isthmus                                           See bridge.
k-ary tree                                        練習問題とする。
k-choosable                                       TBW
k-clique                                          :code:`k_clique_communities(G, k, ...)`
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
Kruskal's algorithm                               :code:`minimum_spanning_edges(G, ...)`, :code:`minimum_spanning_tree(G, ...)`.
labeling method                                   TBW
leaf                                              有向木 ``G`` に対して :code:`[n for n,d in G.out_degree().items() if d == 0]`
length of a cycle/circuit                         :code:`len(ebunch)`, :code:`len(nbunch)`.
length of a walk                                  :code:`len(ebunch)`, :code:`len(nbunch) - 1`.
list-chromatic number                             TBW
list coloring                                     TBW
list function                                     TBW
loop                                              :code:`G.nodes_with_selfloops()`, :code:`G.selfloop_edges(...)`, :code:`G.number_of_selfloops()`.
matching                                          :code:`min_maximal_matching(G)`
matching number                                   TBW
maximum degree                                    :code:`max(degree(G).values())`
maximum flow                                      :code:`maximum_flow(G, s, t, ...)`, :code:`maximum_flow_value(G, s, t, ...)`.
maximum matching                                  :code:`maximal_matching(G)`, :code:`max_weight_matching(G, ...)`
Menger's theorem                                  TBW
minimum degree                                    :code:`min(degree(G).values())`
minimum spanning tree                             :code:`minimum_spanning_tree(G, ...)`
minor                                             TBW
multigraph                                        :code:`MultiGraph(...)`, :code:`MultiDiGraph(...)`.
multipartite graph                                NetworkX は k = 2 までサポートか。
multiple                                          See multigraph.
multiple edge                                     練習問題とする。
node                                              | :code:`G.nodes(...)`,
                                                  | :code:`G.add_node(n, ...)`, :code:`G.add_nodes_from(nodes, ...)`,
                                                  | :code:`G.remove_node(n)`, :code:`G.remove_nodes_from(nodes)`,
                                                  | :code:`G.has_node(n)`, etc.
null graph                                        :code:`null_graph()`
odd cycle                                         :code:`(i for i in simple_cycles(G) if len(i) % 2 == 1)`
order                                             :code:`G.order()`, :code:`G.number_of_nodes()`.
orientation                                       TBW
oriented graph                                    directed graph と同義ではないのか。
out degree                                        :code:`G.out_degree(...)`, :code:`G.out_degree_iter(...)`.
outer face                                        TBW
outerplanar graph                                 TBW
outerplane graph                                  TBW
out-neighborhood                                  :code:`G.successors(n)`
pancyclic graph                                   練習問題とする。
parent                                            :code:`G.predecessors(n)`
partite set                                       TBW
path                                              :code:`G.add_path(...)`, 調査中。
perfect graph                                     TBW
perfect matching                                  TBW
peripheral vertex                                 :code:`ecc = eccentricity(G); M = max(ecc); (k for k, v in ecc.items() if v == M)`
Petersen                                          :code:`petersen_graph(...)`
planar graph                                      TBW
plane graph                                       TBW
Prim's algorithm                                  使われていないのではないか。
pseudograph                                       :code:`is_pseudographical(...)`
radius                                            :code:`radius(G, ...)`
reachable                                         :code:`single_source_dijkstra(G, n1, n2=None, ...)`
regular                                           See regular graph.
regular graph                                     :code:`d = degree(G); all(d[0] == i for i in d.values())`
resitual network                                  :code:`build_residual_network(G, capacity)`
root node                                         有向木 ``G`` に対して :code:`[n for n,d in G.in_degree().items() if d == 0][0]`
rooted tree                                       See arborescence.
saturated                                         TBW
semiregular                                       regular 系は調査中
separating set                                    See cut set.
shortest path                                     :code:`shortest_path(G, ...)`, :code:`all_shortest_path(G, s, t, ...)`, etc.
simple                                            See simple graph.
simple cycle                                      :code:`simple_cycles(G)`. See also simple path.
simple graph                                      :code:`Graph()`, :code:`DiGraph()`. 多重でないグラフの意。
simple path                                       :code:`all_simple_paths(G, n1, n2)` ですべての路が求まる。
sink                                              :code:`(n for n in G if G.out_degree(n) == 0)`
size of a graph                                   :code:`G.size(...)`. エッジの本数もしくはエッジの重みの和。
source                                            :code:`(n for n in G if G.in_degree(n) == 0)`
spanning matching                                 See perfect matching.
spanning subgraph                                 ``G`` から任意のエッジ（複数可）を取り除けば得られる。
spanning tree                                     :code:`nx.minimum_spanning_tree(G, ...)`, ただし入力によっては tree というよりは forest が得られる。
stable set                                        See independent set.
star                                              :code:`G.add_star(...)`, :code:`star_graph(k, ...)`.
staset                                            See independent set.
strongly connected                                :code:`is_strongly_connected(G)`
strongly connected component                      | :code:`strongly_connected_components(G)`,
                                                  | :code:`strongly_connected_component_subgraphs(G)`,
                                                  | :code:`number_strongly_connected_components(G)`, etc.
strongly regular graph                            練習問題とする。
subdivision                                       TBW
subgraph                                          | :code:`subgraph(G, nbunch)` による部分グラフは指定点集合からの induced subgraph である。
                                                  | :code:`attracting_component_subgraphs(G, ...)`, etc. 関連機能多数。
subtree                                           :code:`nx.is_tree(H)`, ``H`` はグラフ ``G`` の部分グラフ。
tail                                              See terminal vertex.
terminal vertex                                   | (1) :code:`e = (v1, v2)` とすると ``e2`` がそれ。
                                                  | (2) walk の終点という意味を採る文献あり。
theta graph                                       TBW
thickness                                         TBW
totally disconnected graph                        TBW
tour                                              See circuit.
tournament                                        :code:`complete_graph(k, ...).to_directed()`
traceable graph                                   TBW
traceable path                                    TBW
trail                                             より条件の厳しい path 系の機能で代用する？
tree                                              | :code:`is_tree(G)`. ``G`` が無向でも有向でも多重でも機能する（単純無向グラフ扱いして判定する）。
                                                  | :code:`dfs_tree(G, n)` で ``G`` からノード ``n`` を root とする有向木を生成できる。
triangle                                          :code:`triangles(G, ...)`
tripartite graph                                  NetworkX は k = 2 までサポートか。
Tutte's theorem                                   TBW
undirected                                        See undirected graph.
undirected edge                                   ``Graph``, ``MultiGraph`` の edge の意。
undirected graph                                  | ``Graph``, ``MultiGraph``. ``Di`` を冠していないクラスが無向グラフ。
                                                  | :code:`not is_directed(G)`, :code:`G.to_undirected()`.
unicyclic graph                                   TBW
unidentified                                      TBW
universal graph                                   See complete graph.
unsaturated                                       TBW
unweighted                                        NetworkX のエッジ関連アルゴリズムは、原則的にエッジの weight を参照するか否かを指定できる。
valency                                           See degree.
walk                                              より条件の厳しい path 系の機能で代用する？
weakly connected                                  :code:`is_weakly_connected(G)`
weakly connected components                       :code:`number_weakly_connected_components(G)`, :code:`weakly_connected_components(G)`.
weight of a subgraph                              練習問題とする。
weighted                                          See weighted graph.
weighted graph                                    | :code:`G.edge[e]['weight'] = value`
                                                  | :code:`G.add_weighted_edges_from(...)` のように明示的に重み付きエッジをセットすることもある。
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
