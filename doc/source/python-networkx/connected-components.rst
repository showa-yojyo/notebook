======================================================================
連結成分
======================================================================

本稿では NetworkX_ の提供する機能を利用して、グラフの連結成分を得る方法について
述べる。まず、ある有向グラフの強連結成分を得る手順について、例を挙げて説明する。
それから、「強」でない種類の連結成分について記すつもりだ。

.. contents::

強連結成分
======================================================================

有向グラフの強連結成分を求めることは、興味のある問題であることが多い。例えば、有
向グラフの強連結成分の集まりと、成分同士を接続する元のグラフの辺の組の集まりと
で、有向部分グラフを考えることがある。その連結部分をひとつ取ってみれば、これは
DAG となっている。

とりあえず、ここで考えるサンプルコードを示す。コードの流れは次のようなものであ
る。

#. グラフを構築する
#. 強連結成分を得る
#. 自明でない強連結成分を標準出力に書き出す

.. literalinclude:: /_sample/networkx/strongly_connected_components.py
   :language: python3
   :lines: 1-13,220-

コード中のグラフ ``G`` は原作版ドラクエ 8 の錬金レシピの依存関係を基に構成した
（多重）有向グラフだ。素材アイテムおよび生成アイテムがグラフの点であり、アイテム
間の依存関係を生成方向に結んだ線分がグラフのエッジとなる。また、生成アイテムに必
要な素材アイテム数をそのエッジの重みとした（今回の例では意味は重要でない）。

.. literalinclude:: /_sample/networkx/strongly_connected_components.py
   :language: python3
   :lines: 13-205

まず、興味のある有向グラフの強連結成分をすべて求めることにする。ただし、連結成分
のうち構成する点がひとつしかないものについては興味がないので、複数点からなる連結
成分だけを出力する。

.. literalinclude:: /_sample/networkx/strongly_connected_components.py
   :language: python3
   :lines: 206-219

本コードを実行すると、次の結果が得られる。これが意味するところは、各連結成分内で
は、その各アイテム（ノード）に錬金操作に関する推移律が成り立つということだ。例え
ば「ふつうのチーズ」から（複数の）錬金操作を経ての「超辛チーズ」の生成可能性を示
している。逆に「超辛チーズ」から「ふつうのチーズ」の生成可能性も示している（ゲー
ムでは勿体ないからやらないほうがよい）。

.. code-block:: text

   ['太陽のかんむり', 'ドクロのかぶと']
   ['超辛チーズ', 'ふつうのチーズ', '辛口チーズ', '激辛チーズ', '冷たいチーズ', 'こおりのチーズ', 'こごえるチーズ', 'かがやくチーズ']
   ['古びたつるぎ', 'はぐれメタルの剣']
   ['アモールの水', 'せいすい']
   ['あくまのムチ', 'バスターウィップ']
   ['騎士団の盾', '騎士団の服']
   ['石のぼうし', '石のオノ']
   ['女神の盾', '死神の盾']
   ['はめつの盾', 'メタルキングの盾']
   ['サタンヘルム', 'ミスリルヘルム']
   ['ゾンビメイル', 'プラチナメイル']
   ['ドクロの指輪', 'ソーサリーリング']
   ['もろはのつるぎ', 'もろはのつるぎ・改']

その他の連結成分
======================================================================

.. todo::

   その他の連結成分について述べる。

.. _NetworkX: https://networkx.github.io/
