======================================================================
グラフを描画する
======================================================================
本稿では NetworkX_ のグラフインスタンスをグラフィカルに描画する方法について記す。
NetworkX の描画機能は、以下で紹介する外部パッケージのいずれかの力を借りて実現している。

ここで紹介する外部パッケージのいずれを採用するにせよ、
グラフ描画の編集については最終的には手作業が入りがちだ。
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
関数 ``nx.draw_networkx`` 系統の描画関数だけでグラフをウィンドウに描画するコードの例を示す。
日本語テキストが描画可能であることを示したいので、ノードラベルをすべて日本語文字列とした。

.. literalinclude:: /_sample/networkx/drawing-mpl.py
   :language: python3

コードの解説は正直に言って自信がない。

* ``G.reverse`` については深い意味はなく、
  グラフの辺の向きをアイテムの生成方向にしたかっただけ。
* ``nx.shell_layout`` は勘。キーワード引数の指定が面倒なため、デフォルト任せ。
* グラフ描画のメインは ``nx.draw`` なのだが、
  普通は ``nx.draw_networkx`` を使ったほうがよさそうだ。
  ここではエッジラベルとノードラベルの描画をそれぞれ細かく指示したかったので、
  単純版である ``nx.draw`` を採用した。
* ノードラベルは日本語なので、適切なフォントをセットする必要がある。
  どうも Matplotlib のインスタンスを直接操作せねばならぬようなので、このようにした。

例によって実行するたびにグラフの見てくれが異なる場合がある。次の図はその一例と思って欲しい。

.. image:: /_static/networkx-drawing-mpl.png
   :scale: 100%

PyGraphviz との連携
======================================================================
Python3 環境では、現時点で PyGraphviz_ を利用するという選択肢はない。
開発版 (1.3rc) のパッケージ `利用要件 <http://pygraphviz.github.io/documentation/development/install.html#requirements>`_
によると、<PyGraphviz does not work with Python 3> とこれ以上ない明確さで非サポートを宣言している。

pydot との連携
======================================================================
本家の pydot_ は Python3 に対応していない。
それゆえ NetworkX からの連携は公式にはできないことになっている。
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

* dot 形式のテキストファイルを ``nx.read_dot`` して、
  NetworkX のグラフインスタンスを生成する。
  それから、所望のグラフアルゴリズムを適用する。
* NetworkX のグラフインスタンスをグラフィカルに描画したい場合は、関数
  ``nx.write_dot`` を用いて dot ファイルに書き出し、Graphviz のツールで画像化する。

.. todo::

   ``nx.pydot_layout`` 問題をクリアする。

形状別描画手引
======================================================================

完全グラフを正多角形の頂点に描画したい
----------------------------------------------------------------------
完全グラフを描画するには、描画関数 ``nx.draw_circular`` 一発で済ませるか、
あるいはレイアウト関数 ``nx.circular_layout`` と汎用描画関数の組み合わせのどちらかを利用したい。
ここでは後者の例を示す。
コード中の if ブロックの else の処理は自力でグラフノードの座標を指示する一例であるが、
出来合いのものを利用するのが望ましい。
実物の ``nx.circular_layout`` の実装はもっとスマートだ。

.. literalinclude:: /_sample/networkx/drawing-comp.py
   :language: python3

正多角形を描くだけのサンプルではビジュアル的にさみしいので、点の色に変化をつけてみた。

コード中の ``set_aspect`` うんぬんは Matplotlib 側の事情による。
私の環境では、この呼び出しを行わないとプロットの座標系の縦横比が 1 : 1 にならない。

実行結果は次のようになるはずだ。
仮に自力で点の座標を指示すると、原点を中止とする単位円周上に配列される。
もっとも、グラフを図示するときには点の物理的な座標は気にしないはずなので、
``plt.axis('off')`` する等して座標軸の描画をやめるとよい。

.. image:: /_static/networkx-drawing-comp.png
   :scale: 50%

木を描画したい
----------------------------------------------------------------------
結論から言うと Graphviz 任せになる。
コツは関数 ``nx.pydot_layout`` のキーワード引数 ``prog`` を下のように指示することのようだ。

.. literalinclude:: /_sample/networkx/drawing-tree.py
   :language: python3

実行結果は次のようになるはずだ。例によって議論の本筋とは無関係にノードを着色してある。

.. image:: /_static/networkx-drawing-tree.png
   :scale: 80%

ただし先述の ``IndexError`` を引き起こさぬように、NetworkX のコードを改造しなくてはならない。
それは、``nx_pydot.py`` に定義されている関数 ``pydot_layout`` の途中の
``encode('utf-8')`` の呼び出しをコメントアウトすることだ。
こちらの修正はさらに上述の Python3 版 pydot の導入とセットで行うこと。

.. include:: /_include/python-refs.txt
.. _NetworkX: https://networkx.github.io/
.. _Graphviz: http://www.graphviz.org/
.. _PyGraphviz: http://pygraphviz.github.io/
.. _pydot: https://code.google.com/p/pydot/
.. _Pyparsing: http://pyparsing.wikispaces.com/
