======================================================================
Chapter 10. Attributes
======================================================================

* :guilabel:`Fill` は内側、:guilabel:`Stroke` はパス自身。
* テキストに対しては色は各文字に設定できるが、グラデーションやパターンは全体設
  定。
* :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`W` でスウォッチダイアログ。縦長だと使いづら
  い。

Fill and Stroke Paint
----------------------------------------------------------------------

* Inkscape の色は RGBA で表現。各成分は 8 ビットの情報量。
* HSV のことを HSL と呼んでいる。
* スウォッチ

  * LB クリックで選択要素の :guilabel:`Fill` 色変更
  * :kbd:`Shift` + LB クリックで選択要素の :guilabel:`Stroke` 色変更
  * マウスジェスチャーで落ちる。

* スタイルインジケーター

  * MB クリックで色を :guilabel:`None` にする。もう一回クリックで黒。

* スポイトツールのことを :guilabel:`Dropper Tool` と呼ぶ。

  * :guilabel:`F7` or :guilabel:`D` で起動。
  * opacity との絡みもあって、わかりにくい？

* :guilabel:`Gradient Tool`

  * :kbd:`Ctrl` + :kbd:`F1` or :kbd:`G` で起動。
  * :kbd:`Stop` 挿入 :kbd:`Ctrl` + :kbd:`Alt` + LB クリック
  * :kbd:`Ctrl` + :kbd:`L` で冗長なノードを消すらしい。
  * :kbd:`Shift` + :kbd:`R` で逆転。

* :kbd:`Pattern`

  * 備え付けのパターンには実はライセンスがある。
  * :file:`patterns/patterns.svg` に定義がある？
  * パターンを用意する、パターンを割り当てる、パターンの位置等を調整する、の三段
    階。
  * パターンを定義するには、適当なオブジェクトを選択して :kbd:`Alt` + :kbd:`I`
    で OK.
  * :kbd:`Shift` + :kbd:`Alt` + :kbd:`I`: :guilabel:`Pattern to Objects`
  * パターンの変形がわかりにくい。
  * ハッチングはパターン機能を応用して実現する。

* :guilabel:`Fill Rule` (even-odd rule) は押さえておいたほうがよい。

Stroke Style
----------------------------------------------------------------------

* :guilabel:`Join`: miter/round/bevel
* :guilabel:`Cap`: butt/round/square; ストローク両端だけでなく、ダッシュ各線分に
  も影響する。
* :guilabel:`Marker`

  * :guilabel:`Object to Marker` コマンドがある。
  * マーカーはストローク色を引き継がない。エクステンションで逃れられるらしい。
  * マーカーのサイズはストローク幅に影響される。SVG 直編集。
  * 線を同一位置に複製して、複雑なマーカー線を描ける。
