======================================================================
連結度
======================================================================
本稿では NetworkX_ にある、グラフの点および辺連結度に関係する機能を記す。

.. contents::

関数 ``nx.edge_connectivity`` と ``nx.node_connectivity``
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

.. todo::

   書くことがまだある可能性が高い。

.. _NetworkX: https://networkx.github.io/
