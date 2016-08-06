======================================================================
応用テク
======================================================================
本稿では LaTeX 表記の実現や 3D プロット等、比較的高度な Matplotlib_ の機能を利用する。

.. contents::

LaTeX 表現
======================================================================
Matplotlib のプロットに LaTeX 書式の画像化を埋め込む方法を説明する。

Matplotlib のすべてのテキスト API は LaTeX の数式を受け付けてくれる。
文字列内の ``$`` で囲まれた部分が LaTeX 表現と認識されるようだ。
何も工夫しないでいると文字列がバックスラッシュの嵐になるので、
Python のコードで raw string 形式で数式を含む文字列を定義するのが吉だろう。

次のスクリプトは Matplotlib のサンプルコードを一部改変したものである。
IPython_ を起動していれば、下記コードをクリップボードにコピーして、
コンソールで ``%paste`` すれば結果が見られる。

.. literalinclude:: /_sample/mpl/tex.py
   :language: python3

実行結果は次のような画像の表示となる（良いグラフとはとても言えない）。
乱数を利用しているヒストグラム部分は毎回絵が変わる。
図の凡例およびキャプション後半に注意して欲しい。ギリシア文字を含む数式が見える。

* 凡例内の数式は関数 ``plt.plot`` のキーワード引数 ``label`` の値の LaTeX と対応している。
* 図のキャプションのギリシア文字は、関数 ``plt.title`` に渡す値の LaTeX と対応している。

.. figure:: /_static/mpl-tex.png
   :align: center
   :alt: LaTeX 数式
   :width: 815px
   :height: 615px
   :scale: 50%

3 次元プロット
======================================================================
曲面を描画することもあるのでプロットという表現が微妙なのだが、
とにかく空間的に 3 次元のデータを図にすることができる。

.. figure:: /_static/scipy-spline-3d.png
   :align: center
   :alt: 簡単な空間曲線のプロット
   :width: 815px
   :height: 615px
   :scale: 50%

パッケージ ``matplotlib`` と同じ階層に ``mpl_toolkits`` という別のパッケージがある。
ここにある機能を利用すると、3 次元プロットをウィンドウに描画することができる。
これはマウス操作によるビューのズームおよび回転を実現している優れものである。

ノート :doc:`/python-scipy/interpolate` で示した例を再掲する。

.. literalinclude:: /_sample/scipy/interp_spline_3d.py
   :language: python3

Matplotlib 関連の処理の説明を補足する
（曲線データに関しての説明は先のページを参照）。

* 関数 ``gca`` の呼び出しでカレントの Axes を指定する際に、
  キーワード引数 ``projection`` を ``3d`` とすることで 3D プロット専用の Axes を生成し、
  同時にカレントにセットする。

  * このメソッド呼び出しが成功するには ``Axes3D`` のインポートが必要。

* メソッド ``ax.scatter`` と ``ax.plot`` を用いて次の形状をプロットする。

  #. 入力データである通過点 (black)
  #. SciPy_ で計算した、出力データである 3 次元スプライン曲線の制御点列 (pink)
  #. 出力データである 3 次元スプライン曲線 (deeppink)

* メソッド ``ax.text`` で通過点のプロットにその xyz 座標をテキストとして表示する。
* 各種メソッドでラベルや凡例を図に添える。

.. note::

   Python 3.5 環境移行直後の実行結果の出力を記す（一部を手動で改行した）。
   何やら警告の例外が発生している。

   .. code-block:: text

      knot vector:
       [0.000 0.000 0.000 0.000 1.000 1.000 1.000 1.000]
      control points:
       [[0.000 150.000 150.000 0.000]
       [0.000 -116.667 216.667 100.000]
       [0.000 50.000 100.000 150.000]]
      degree:
       3
      parameter values:
       [0.000 0.333 0.667 1.000]
      f(0.000) = [0.000 0.000 0.000]
      f(0.333) = [100.000 -0.000 50.000]
      f(0.667) = [100.000 100.000 100.000]
      f(1.000) = [0.000 100.000 150.000]
      d:\python35\lib\site-packages\matplotlib\collections.py:590: FutureWarning: elementwise comparison failed;
      returning scalar instead, but in the future will perform elementwise comparison
        if self._edgecolors == str('face'):

.. include:: /_include/python-refs-sci.txt
