======================================================================
マッチング
======================================================================

本稿では NetworkX_ の機能を利用して、グラフのマッチング問題各種を解く手順につい
てを記す。

.. contents::

極大マッチング
======================================================================

極大マッチングは関数呼び出し一発で求められる。

Wikipedia_ のイラストを参考にしてグラフを構築し、それぞれに対して関数
``nx.maximal_matching`` を呼び出すコードを書いた。目的は、結果とイラストを比較し
て NetworkX_ の機能を確認することだ。

.. literalinclude:: /_sample/networkx/maximal_matching.py
   :language: python3

実行結果は次の通り。当該記事の図とは異なるエッジセットが得られた。図の上の行がオ
リジナルで、下の行が本プログラムによる極大マッチングだ。確かにこのエッジセットも
それぞれのグラフの極大マッチングである

.. code:: console

   bash$ python maximal-matching.py
   {(0, 1)}
   {(0, 1), (2, 4), (3, 5)}
   {(0, 1), (2, 4)}

.. figure:: /_images/networkx-maximal-matching.png
   :align: center
   :alt: Licensed under CC-BY-SA 3.0
   :width: 300px
   :height: 120px
   :scale: 100%
   :target: http://commons.wikimedia.org/wiki/File:Maximal-matching.svg

最小極大マッチング
======================================================================

関数 ``min_maximal_matching`` が最小極大マッチングを求めるものなのだろうが、その
実装は……。

最大マッチング
======================================================================

最大マッチングも関数呼び出し一発で求められる。こちらの例も Wikipedia_ から拝借し
て、結果を見比べてみよう。

コード例は左記の物とほぼ同様につき、差分のみを示す。関数
``nx.max_weight_matching`` にはキーワード引数があるが、今回は未使用とする。

.. literalinclude:: /_sample/networkx/maximum_matching.py
   :language: python3
   :lines: 6-10

実行結果は次の通り。戻り値の型がノードとノードの辞書なのがマッチング感を演出して
いるように見受けられる。

.. code:: console

   bash$ python maximum_matching.py
   {0: 2, 1: 5, 2: 0, 5: 1}
   {0: 1, 1: 0, 2: 4, 3: 5, 4: 2, 5: 3}
   {1: 3, 2: 4, 3: 1, 4: 2}

こちらも当該記事とは異なるエッジセットが得られた。図の上の行がオリジナルで、下の
行が本プログラムによる最大マッチングだ。

.. figure:: /_images/networkx-maximum-matching.png
   :align: center
   :alt: Licensed under CC-BY-SA 3.0
   :width: 300px
   :height: 120px
   :scale: 100%
   :target: http://commons.wikimedia.org/wiki/File:Maximal-matching.svg

.. todo::

   あとは完全マッチング問題の解法を記述したい。

.. _NetworkX: https://networkx.github.io/
.. _Wikipedia: http://en.wikipedia.org/wiki/Matching_(graph_theory)
