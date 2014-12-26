======================================================================
連結度
======================================================================
本稿では NetworkX_ にある、グラフの点および辺連結度に関係する機能を記す。

.. contents::

辺連結度と点連結度
======================================================================
辺連結度、点連結度は関数 ``nx.edge_connectivity`` と ``nx.node_connectivity``
でそれぞれ得られる。ここでは無向グラフいくつかに対して単に各連結度を計算した。

.. image:: /_static/networkx-connectivity.png
   :scale: 100%

.. literalinclude:: ../../sample/networkx/connectivity.py
   :language: python3

実行結果は次のようになる。

.. code-block:: console

   $ python connectivity.py
   G0 is and 1-connected 1-edge connected.
   G1 is and 1-connected 1-edge connected.
   G2 is and 1-connected 2-edge connected.
   G3 is and 2-connected 2-edge connected.

最小カットセット
======================================================================
関数 ``nx.minimum_edge_cut`` と ``nx.minimum_node_cut`` を利用すれば、
グラフの辺、点に関する最小のカットセットを得られる。
これらの関数のキーワード引数を用いて、カットに関する始点 s と終点 t を指定する。
グラフを非連結にするようなカットを任意に一つ得たい場合には、これらの指定を省略することもできる。

次のコードは図のグラフに対して、両カット関数を色々な (s, t) の組み合わせで呼び出すものだ。

.. image:: /_static/networkx-cutset.png
   :scale: 100%

.. literalinclude:: ../../sample/networkx/cutset.py
   :language: python3

実行結果は次のようになる。よく見るとあまり面白くない。

.. code-block:: console

   $ python34 cutset.py
   G: [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (3, 4), (3, 5), (4, 6), (5, 6), (5, 7)]
   minimum_edge_cut:
   (s, t) = (0, 7): cutset = {(5, 7)}
   (s, t) = (0, 6): cutset = {(5, 6), (4, 6)}
   (s, t) = (1, 7): cutset = {(5, 7)}
   minimum_node_cut:
   (s, t) = (0, 7): cutset = {5}
   (s, t) = (0, 6): cutset = {4, 5}
   (s, t) = (1, 7): cutset = {5}

.. _NetworkX: https://networkx.github.io/
