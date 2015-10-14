======================================================================
トポロジカルソート
======================================================================
本稿では NetworkX_ の提供する機能を利用して、
有向グラフのトポロジカルソートを実行する方法について述べる。
NetworkX_ でトポロジカルソートを実現する関数は
``nx.topological_sort`` と ``nx.lexicographical_topological_sort`` である。
まずは前者を見ていく。

.. contents::

先にグラフ概形とサンプルコード全体を示す。

.. image:: /_static/networkx-dag.png
   :alt: Public Domain
   :scale: 100%
   :target: http://commons.wikimedia.org/wiki/File:Directed_acyclic_graph_3.svg

.. literalinclude:: /_sample/networkx/tsort.py
   :language: python3

基本事項
----------------------------------------------------------------------
グラフがトポロジカルソートを適用できる条件は、
グラフが有向かつ閉路がないことが条件となる。
つまり、グラフが DAG であることが条件である。
NetworkX_ では関数 ``nx.is_directed_acyclic_graph`` でグラフが DAG であるか否かをテストできる。
そして実は DAG 性の判定はトポロジカルソートで実装されている。

そして、トポロジカルソートで少々注意を要するのは、
一般的にはその結果が一意に決まらないということだろうか。
サンプルコードは Wikipedia_ で DAG を論じるときによく参照されるグラフを拝借した。
ページ中程に複数のソート結果が紹介されている。

関数 ``print_sort`` ではジェネレーター ``nx.topological_sort`` を呼び出し、
実行結果を標準出力に書き出す。
結果はこのようになった。
見事に Wikipedia_ のどのソート結果とも異なる順列が得られた。

.. code-block:: text

   [7, 5, 11, 2, 3, 10, 8, 9]

しかし、これもまたトポロジカルソートの要件を満たしていることが容易に確認できる。
ちなみに図のグラフのノードにわざわざ私が色を塗ったのは、
色の明るいノードの順に得られるのでは、
という予想だった。そしてそれは見事に外れたようだ。

辞書式トポロジカルソート
----------------------------------------------------------------------
NetworkX_ におけるもう一つのトポロジカルソートの実装である。
DFS 法を再帰的に呼び出す方式によるものだ。

試しに先のグラフに lexicographical 版を適用してみると、異なるソート結果が得られた。
Wikipedia_ の <smallest-numbered available vertex first> の結果と一致する。

>>> list(nx.lexicographical_topological_sort(G))
[3, 5, 7, 8, 11, 2, 9, 10]

ちなみに先に紹介した ``nx.topological_sort`` の実装はスキーナ本
（邦訳：『アルゴリズム実装マニュアル』）から取ってきているらしい。

.. _NetworkX: https://networkx.github.io/
.. _Wikipedia: http://en.wikipedia.org/wiki/Topological_sorting
