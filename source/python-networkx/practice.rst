======================================================================
NetworkX を利用する
======================================================================
.. contents::

基本的なコードの書き方を習得する
======================================================================

以降、次のインポートを断りなしに用いる。

.. code-block:: python3

  import networkx as nx
  import matplotlib.pyplot as plt

小さいグラフを定義して、単純な計算をさせてみることで
NetworkX でのプログラミングの感触を確かめてみよう。

Dijkstra 法による最短経路
----------------------------------------------------------------------
別ページ→ :ref:`dijkstra`

グラフィックを描画する
----------------------------------------------------------------------
先程のグラフを Matplotlib_ の表示機能を利用してウィンドウに出力する方法を示す。
試行錯誤の結果、次のコードが最も見やすいイメージを描画してくれた。

.. literalinclude:: /_sample/networkx/networkx_draw.py
   :language: python3

スクリプトをコンソールから実行すると、
次のイメージを含む Matplotlib ウィンドウが開いたことがある。

なお、関数 ``spring_layout`` のキーワード引数として
``random_state`` を明示的に指定しないと、
この関数は実行するたびにノードの位置をランダムに決定する。
利用者は ``random_state`` の値を試行錯誤の結果、適切なものを発見する必要があるかもしれない。

.. figure:: /_images/networkx-draw.png
   :align: center
   :alt: NetworkX によるグラフの描画
   :width: 640px
   :height: 478px
   :scale: 100%

描画については別項で詳しく論じる。→ :doc:`drawing`

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
.. _PyGraphviz: http://pygraphviz.github.io/
.. _pydot: https://code.google.com/p/pydot/
