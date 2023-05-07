======================================================================
Chapter 17. Filter Effects - Custom
======================================================================

Basic Use
----------------------------------------------------------------------

* ガウスぼかしフィルターはいつもの色ダイアログでも設定できる。
* ブレンドフィルターはレイヤーダイアログでも設定できる。
* フィルター削除はそれ用のメニューがある。
* :guilabel:`Filter Effects Region`: ``-0.1:1.1``

Filter Effects Dialog
----------------------------------------------------------------------

* 新規とエフェクト追加がややこしい。

Mini Tutorial - A Drop Shadow
----------------------------------------------------------------------

<https://dl.dropbox.com/u/61006529/inkscape/dropshadow.svg>

* :guilabel:`Source` が変更された場合、自動的にドロップシャドウも更新がかかる。
* テキストに対して compound filter を作成することになる。
* :guilabel:`Gaussian blur`, :guilabel:`Offset`, :guilabel:`Merge` の 3 つを使
  う。矢印の設定に注意。

Color Filter Primitives
----------------------------------------------------------------------

* RGBA 値の行列による変換と考えてよい。OpenGL のアレっぽい。

Compositing Filter Primitives
----------------------------------------------------------------------

* ``enable-background`` タグの扱いにバグがあるらしい。
* SVG 1.1 の仕様にもバグがあって、とにかく background 周りは不安定。1.2 で修正さ
  れた。

* :guilabel:`Blend`

  * :guilabel:`Normal`, :guilabel:`Multiply`, :guilabel:`Screen`,
    :guilabel:`Darken`, :guilabel:`Lighten` の 5 種類。

* :guilabel:`Composite`

  * :guilabel:`Over`, :guilabel:`In`, :guilabel:`Out`, :guilabel:`Atop`,
    :guilabel:`Xor`, :guilabel:`Arithmetic`

* :guilabel:`Merge`: Z-order ベースのマージ。

Fill Filter Primitives
----------------------------------------------------------------------

* :guilabel:`Flood`: バウンディング塗りつぶし？
* その他は未実装だったり、よくわからなかったり。

Lighting Filters Primitives
----------------------------------------------------------------------

* フォーンシェーディングっぽく絵を描くフィルターらしい。

Pixel Manipulation Filter Primitives
----------------------------------------------------------------------

* :guilabel:`Convolve`
* :guilabel:`Displacement Map`
* :guilabel:`Gaussian Blur`: クリッピングやマスキングと絡める場合は適用順序に注
  意。
* :guilabel:`Morphology`
* :guilabel:`Offset`

Complex Examples
----------------------------------------------------------------------

* NEON の例を試した。<https://dl.dropbox.com/u/61006529/inkscape/neon.svg>
