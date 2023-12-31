======================================================================
Chapter 13. Eraser Tool
======================================================================

.. contents::

Photoshop で言う消しゴムツールに相当するものを習得する。

   The *Eraser Tool* is used to erase parts of a drawing. It has two modes. The
   *Touch* mode removes objects from a drawing, while the *Cut Out* mode removes
   parts of objects.

当ツールの起動方法例：

* :guilabel:`Toolbox` 内 :guilabel:`Erase objects or paths` アイコンをクリックす
  る。
* :kbd:`Shift` + :kbd:`E` を押す。

.. admonition:: 読者ノート

   当ツールも感圧式入力装置対応済み。個人的に使わないはずなのでノートでは立ち入
   らない。

   Inkscape 1.2 ではもう一つ、:guilabel:`Clip from objects` アイコンがツールバー
   にある。このモードの記述が本書にはないが、本章の記述と後述される *Clip Tool*
   からの類比で挙動を理解することは可能だろう。

Eraser Touch Mode
======================================================================

Midas 王のごとく、触れたオブジェクトを削除する。

   In *Touch* mode, one uses the *Eraser Tool* to draw a red “touch” line. Any
   object that the line touches will be deleted when the stroke is finished.

鉛筆ツールの要領でキャンバスをドラッグすると赤線が引かれる。それを交わるオブジェ
クトすべてを消去する。

このモードにするにはツールバーの :guilabel:`Delete objects touchde by eraser` ア
イコンのボタンを押す。

Eraser Cut Out Mode
======================================================================

今度はマウスで描く赤線の形状に意味がある：

   In the *Cut-Out* mode, the eraser is used to draw a red path, similar to a
   path created by the *Calligraphy Tool*. This path is then subtracted from any
   other paths it crosses.

うどんのように太い線を描くとする。このとき、オブジェクトとうどんの共通部分が削ら
れる。Boolean 演算をするのだろう。したがって、パスと互換性のないオブジェクトは当
ツールの適用範囲外だ：

   *Regular Shapes* crossed are first converted to paths. This mode does not
   work on bitmap images or directly on *Groups* (enter *Groups* first to use).
   If many objects are crossed, it may take awhile for the subtraction to be
   processed.

このモードにするには、ツールバーの :guilabel:`Cut out from paths and shapes` ア
イコンをクリックする。
