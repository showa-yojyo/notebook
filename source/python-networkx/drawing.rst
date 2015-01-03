======================================================================
グラフを描画する
======================================================================
本稿では NetworkX_ のグラフインスタンスをグラフィカルに描画する方法について記す。
NetworkX の描画機能は、以下で紹介する外部パッケージのいずれかの力を借りて実現している。

ここで紹介する外部パッケージのいずれを採用するにせよ、グラフ描画の編集については最終的には手作業が入りがちだ。
自作プログラムが出力した dot ファイルの記述は、そのまま Graphviz_ のプロセッサーにかけると、
こちらの想定した形状にはなってくれていない場合がほとんどだ。
それでテキストエディターで dot のコードを修正することになる。
例えば、完全グラフのデモなら、ノードが正多角形を構成するような描画になるように dot を編集するのだ。

本稿で利用する各パッケージのバージョンは次のとおり。
一部再掲になるが、特にバージョン情報が重要になるので、まとめて記しておく。

* Python: 3.4.1
* NetworkX_: 1.9.1
* Matplotlib_: 1.4.2
* Graphviz_: 2.38
* PyGraphviz: 後述
* pydot: 後述
* Pyparsing_: 2.0.3

.. contents::
   
Matplotlib との連携
======================================================================
.. todo::

   記事を書く。
   出力描画がショボイので、乗り気ではない。

PyGraphviz との連携
======================================================================
.. todo::

   記事を書く。

pydot との連携
======================================================================
本家の pydot_ は Python3 に対応していない。それゆえ NetworkX からの連携は公式にはできないことになっている。
本稿では、そこを何とかクリアする。

Python3 動作版 pydot のセットアップ
----------------------------------------------------------------------
試行錯誤した結果、どうも `nlhepler 版 pydot <https://github.com/nlhepler/pydot>`_
を利用するのがもっとも安定した動作実績を得られることがわかったので、本稿ではそれを採用する。
バージョンは 1.0.29 だ。

.. code-block:: console

   $ git clone https://github.com/nlhepler/pydot.git
   $ cd pydot
   $ pip install -e .

モジュール ``networkx.drawing.nx_pydot`` の関数の動作確認
----------------------------------------------------------------------
以上の環境で、簡単な NetworkX のグラフインスタンスを作成し、
モジュール ``networkx.drawing.nx_pydot`` がエクスポートしている各関数の動作を確認した。

>>> N = nx.complete_graph(5)
>>> P = nx.to_pydot(N)
>>> path = 'D:/Temp/nx_pydot.dot'
>>> nx.write_dot(N, path)
>>> # etc.

現時点での利用可否状況は次のような感じだと思う。

=========================== ========================================
関数                        呼び出し結果
=========================== ========================================
``nx.from_pydot(P)``        | NG
                            | ``NameError: name 'basestring' is not defined``
``nx.to_pydot(N, ...)``     OK
``nx.write_dot(G, path)``   OK
``nx.read_dot(path)``       | NG
                            | ``NameError: name 'basestring' is not defined``
``nx.pydot_layout(G, ...)`` | NG
                            | ``IndexError: list index out of range``
                            | or
                            | ``pydot.InvocationException: Program terminated with status: 1. stderr follows: ...``
=========================== ========================================

NG な結果が多いが、ユーザーが手動で 2to3.py して修正したファイル ``nx_pydot.py``
を上書きすれば、ふたつの NameError は解決する。
バグレポート的なものを私の方から NetworkX 開発陣へ提出しておきたい。

最後の関数 ``nx.pydot_layout`` の失敗は、例外送出のケースが 2 通りある。
どちらも状況がわからない。

以上のことから、利用パターンは次のものに限られるのではないだろうか。

* dot 形式のテキストファイルを ``nx.read_dot`` して、NetworkX のグラフインスタンスを生成する。
  それから、所望のグラフアルゴリズムを適用する。
* NetworkX のグラフインスタンスをグラフィカルに描画したい場合は、関数
  ``nx.write_dot`` を用いて dot ファイルに書き出し、Graphviz のツールで画像化する。

.. todo::

   ``nx.pydot_layout`` 問題をクリアする。

.. _NetworkX: https://networkx.github.io/
.. _Matplotlib: http://matplotlib.sourceforge.net/
.. _Graphviz: http://www.graphviz.org/
.. _PyGraphviz: http://pygraphviz.github.io/
.. _pydot: https://code.google.com/p/pydot/
.. _Pyparsing: http://pyparsing.wikispaces.com/
