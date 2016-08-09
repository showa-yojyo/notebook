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
毎回このイメージが描画されれば話は終わるのだが、困った点が見つかった。
NetworkX のグラフ描画ルーチンの特性上、
クライアントが十分な描画用のパラメーターを与えないと、
ノードの位置をランダムに決定するようだ。
例えばこのコードを二度三度と実行してみるとよい。
イメージがその度に異なっているのがわかるハズだ。
これでは作業の要件によっては支障をきたすかもしれない。

.. figure:: /_static/networkx-draw.png
   :align: center
   :alt: NetworkX によるグラフの描画
   :width: 363px
   :height: 308px
   :scale: 100%

描画については別項で詳しく論じる。→ :doc:`drawing`

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
.. _PyGraphviz: http://pygraphviz.github.io/
.. _pydot: https://code.google.com/p/pydot/
