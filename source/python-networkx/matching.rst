======================================================================
マッチング
======================================================================
本稿では NetworkX_ の機能を利用して、グラフのマッチング問題各種を解く手順についてを記す。

.. contents::

極大マッチング
======================================================================
極大マッチングは関数呼び出し一発で求められる。

Wikipedia_ のイラストを参考にしてグラフを構築し、それぞれに対して関数 ``nx.maximal_matching`` を呼び出すコードを書いた。
目的は、結果とイラストを比較して NetworkX_ の機能を確認することだ。

.. literalinclude:: ../../sample/networkx/maximal-matching.py
   :language: python3

実行結果は次の通り。当該記事の図とは異なるエッジセットが得られた。
図の上の行がオリジナルで、下の行が本プログラムによる極大マッチングだ。
確かにこのエッジセットもそれぞれのグラフの極大マッチングである

.. code-block:: console

   $ python maximal-matching.py
   {(0, 1)}
   {(0, 1), (2, 4), (3, 5)}
   {(0, 1), (2, 4)}

.. image:: /_static/networkx-maximal-matching.png
   :scale: 100%

.. todo::

   あとは最大マッチング問題、完全マッチング問題の解法を記述したい。

.. _NetworkX: https://networkx.github.io/
.. _Wikipedia: http://en.wikipedia.org/wiki/Matching_(graph_theory)
