======================================================================
グラフを描画する
======================================================================

本稿では NetworkX_ のグラフインスタンスをグラフィカルに描画する方法について記
す。 NetworkX の描画機能は、以下で紹介する外部パッケージのいずれかの力を借りて実
現している。

ここで紹介する外部パッケージのいずれを採用するにせよ、グラフ描画の編集については
最終的には手作業が入りがちだ。自作プログラムが出力した dot ファイルの記述をその
まま Graphviz_ のプロセッサーにかけると、ほとんどの場合にこちらの想定した形状に
なってくれていない。それでテキストエディターで dot のコードを修正することにな
る。例えば、完全グラフのデモなら、ノードが正多角形を構成するような描画になるよう
に dot を編集するのだ。

.. contents::

Matplotlib との連携
======================================================================

関数 ``nx.draw_networkx`` 系統の描画関数だけでグラフをウィンドウに描画するコード
の例を示す。日本語テキストが描画可能であることを示したいので、ノードラベルをすべ
て日本語文字列とした。

.. literalinclude:: /_sample/networkx/drawing_mpl.py
   :language: python3

コードの解説は正直に言って自信がない。

* ``G.reverse`` については深い意味はなく、グラフの辺の向きをアイテムの生成方向に
  したかっただけ。
* ``nx.shell_layout`` は勘。キーワード引数の指定が面倒なため、デフォルト任せ。
* グラフ描画のメインは ``nx.draw`` なのだが、普通は ``nx.draw_networkx`` を使っ
  たほうがよさそうだ。ここではエッジラベルとノードラベルの描画をそれぞれ細かく指
  示したかったので、単純版である ``nx.draw`` を採用した。
* ノードラベルは日本語なので、適切なフォントをセットする必要がある。どうも
  Matplotlib のインスタンスを直接操作せねばならぬようなので、このようにした。

実行結果を次に示す：

.. figure:: /_images/networkx-drawing-mpl.png
   :align: center
   :alt: 賢者の石レシピ
   :width: 640px
   :height: 478px
   :scale: 100%

PyGraphviz との連携
======================================================================

Python 3.5 環境では、現時点で PyGraphviz_ を利用するには自分でビルドをする必要が
ありそうだ。

.. code:: console

   bash$ git clone https://github.com/pygraphviz/pygraphviz.git
   Cloning into 'pygraphviz'...
   中略
   Checking connectivity... done.

   bash$ cd pygraphviz
   bash$ pip install -e .
   Obtaining file:///D:/home/yojyo/devel/pygraphviz
   Installing collected packages: pygraphviz
     Running setup.py develop for pygraphviz
       中略
       building 'pygraphviz._graphviz' extension
       error: Unable to find vcvarsall.bat

.. warning::

   こちらは最新環境では試していない。

pydot との連携
======================================================================

本家の pydot_ は Python3 に対応していない。それゆえ NetworkX からの連携は公式に
はできないことになっている。本稿では、そこを何とかクリアする。

Python3 動作版 pydot のセットアップ
----------------------------------------------------------------------

試行錯誤した結果、どうも `nlhepler 版 pydot
<https://github.com/nlhepler/pydot>`_ を利用するのがもっとも安定した動作実績を得
られることがわかった。バージョンは 1.0.29 だ。

.. code:: console

   bash$ git clone https://github.com/nlhepler/pydot.git
   bash$ cd pydot
   bash$ pip install -e .

パッケージ nxpydot のセットアップ
----------------------------------------------------------------------

別の方法を見つけたので記す。それは nxpydot_ というサードパーティー製パッケージを
利用するやり方だ。本稿ではこちらを採用する。

.. code:: console

   bash$ pip install nxpydot
   Collecting nxpydot
     Downloading nxpydot-0.1-py3-none-any.whl
   Collecting pydotplus (from nxpydot)
     Downloading pydotplus-2.0.2.tar.gz (278kB)
       ...
   Requirement already satisfied (use --upgrade to upgrade): pyparsing>=2.0.1 in d:\miniconda3\lib\site-packages (from pydotplus->nxpydot)
   Building wheels for collected packages: pydotplus
     Running setup.py bdist_wheel for pydotplus ... done
     ...
   Successfully built pydotplus
   Installing collected packages: pydotplus, nxpydot
   Successfully installed nxpydot-0.1 pydotplus-2.0.2

モジュール ``networkx.nx_pydot`` の関数の動作確認
----------------------------------------------------------------------

以上の環境で、簡単な NetworkX のグラフインスタンスを作成し、モジュール
``networkx.nx_pydot`` がエクスポートしている各関数の動作を確認した。

>>> N = nx.complete_graph(5)
>>> P = nx.nx_pydot.to_pydot(N)
>>> path = 'D:/Temp/nx_pydot.dot'
>>> nx.nx_pydot.write_dot(N, path)
>>> # etc.

現時点での利用可否状況は次のような感じだと思う：

.. csv-table::
   :delim: @
   :header-rows: 1
   :widths: auto

   関数 @ 呼び出し結果
   ``nx.nx_pydot.from_pydot(P)``@OK
   ``nx.nx_pydot.to_pydot(N, ...)``@OK
   ``nx.nx_pydot.write_dot(P, path)``@OK
   ``nx.nx_pydot.read_dot(path)``@OK
   ``nx.nx_pydot.pydot_layout(G, ...)``@OK

テキストファイルの内容はこのようになる：

.. code-block:: text

   strict graph "complete_graph(5)" {
   0;
   1;
   2;
   3;
   4;
   0 -- 1;
   0 -- 2;
   0 -- 3;
   0 -- 4;
   1 -- 2;
   1 -- 3;
   1 -- 4;
   2 -- 3;
   2 -- 4;
   3 -- 4;
   }

形状別描画手引
======================================================================

完全グラフを正多角形の頂点に描画したい
----------------------------------------------------------------------

完全グラフを描画するには、描画関数 ``nx.draw_circular`` 一発で済ませるか、あるい
はレイアウト関数 ``nx.circular_layout`` と汎用描画関数の組み合わせのどちらかを利
用したい。ここでは後者の例を示す。コード中の ``if`` ブロックの ``else`` の処理は
自力でグラフノードの座標を指示する一例であるが、出来合いのものを利用するのが望ま
しい。実物の ``nx.circular_layout`` の実装はもっとスマートだ。

.. literalinclude:: /_sample/networkx/drawing_comp.py
   :language: python3

正多角形を描くだけのサンプルではビジュアル的にさみしいので、点の色に変化をつけて
みた。

コード中の ``set_aspect`` うんぬんは Matplotlib 側の事情による。私の環境では、こ
の呼び出しを行わないとプロットの座標系の縦横比が 1 : 1 にならない。

実行結果は次のようになるはずだ。仮に自力で点の座標を指示すると、原点を中止とする
単位円周上に配列される。もっとも、グラフを図示するときには点の物理的な座標は気に
しないはずなので、``plt.axis('off')`` する等して座標軸の描画をやめるとよい。

.. figure:: /_images/networkx-drawing-comp.png
   :align: center
   :alt: 正 17 角形
   :width: 821px
   :height: 620px
   :scale: 50%

木を描画したい
----------------------------------------------------------------------

結論から言うと Graphviz 任せになる。コツは関数 ``nx.pydot_layout`` のキーワード
引数 ``prog`` を下のように指示することのようだ。

.. literalinclude:: /_sample/networkx/drawing_tree.py
   :language: python3

実行結果は次のようになるはずだ。例によって議論の本筋とは無関係にノードを着色して
ある。

.. figure:: /_images/networkx-drawing-tree.png
   :align: center
   :alt: 完全二分木
   :width: 452px
   :height: 295px
   :scale: 80%

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
.. _NetworkX: https://networkx.github.io/
.. _Graphviz: http://www.graphviz.org/
.. _PyGraphviz: http://pygraphviz.github.io/
.. _pydot: https://code.google.com/p/pydot/
.. _Pyparsing: http://pyparsing.wikispaces.com/
.. _nxpydot: http://github.com/pfmoore/nxpydot
