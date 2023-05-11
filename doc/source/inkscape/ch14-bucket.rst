======================================================================
Chapter 14. Paint Bucket Tool
======================================================================

.. contents::

Photoshop などのバケツツールと同じだが、SVG ならではの挙動があることに注意する。

   Inspired by the need for cartoonists to color their drawings, the *Paint
   Bucket Tool* flood fills a region with a color. True to an SVG drawing
   program, the new object is defined by vectors and thus is fully scalable. The
   region to be filled, however, is defined by the pixels on the screen at the
   time of the fill.

Simple Use
======================================================================

   The simplest use is to fill an area defined by two different objects.

起動方法は次のいずれか：

* :guilabel:`Toolbox` にある :guilabel:`Fill bounded areas` をクリックする。
* :kbd:`Shift` + :kbd:`F7` または :kbd:`U` を押す。

それから、

   click in the overlapping region. A new object is created with the current
   Fill color.

塗りつぶしの計算法をいちおう確認しておく：

   The filling algorithm recursively adds neighboring areas to the region until
   pixels are found that don't meet the criteria determined by the parameters in
   the *Tool Controls*.

対象領域の色合いがグラデーションのように一様でない場合に、クリック位置の色にどれ
だけ近ければ出力領域に含まれるかを指定する入力欄がツールバーにある：

   The :guilabel:`Threshold` parameter controls how close a color must match the
   color (or *Alpha*) under the cursor. Lower thresholds will match a smaller
   range.

Photoshop と考え方は一緒のようで、色のどの成分を閾値と比較するのかを指定すること
ができる：

   The :guilabel:`Fill by` parameter controls what color value is used to
   determine the the color matching. Choices are: :guilabel:`Visible Colors`
   (default), :guilabel:`Red`, :guilabel:`Blue`, :guilabel:`Green`,
   :guilabel:`Hue`, :guilabel:`Saturation`, :guilabel:`Lightness`, and
   :guilabel:`Alpha`.

:kbd:`Ctrl` 押しクリックで、そこにあるオブジェクトを単に現在のスタイルにするとい
う操作もある：

   Holding the :kbd:`Ctrl` down while clicking on an object with the *Paint
   Bucket Tool* will set the *Fill* and *Stroke* to the current style without
   preforming any filling.

.. admonition:: 利用者ノート

   :kbd:`Shift` 押しクリックも実装されている。塗りつぶして生成されるオブジェクト
   が順次前回のそれに $\cup$ される。

Filling Fidelity
======================================================================

塗りつぶしの原理を確認しよう：

   The filling process works first by determining which pixels should be filled
   and then tracing those pixels to produce a vectorized path. The tracing
   process has limited precision which can result in inaccuracies in the filled
   region.

したがって、塗りつぶし領域を精巧に表示するためにズームインするのが有効な手段とな
る：

   The first way is to zoom in on the region you are filling. Zooming in
   increases the number of screen pixels in the filled region which results in a
   more accurate tracing.

もう一つの方法は、塗りつぶし領域専用のレイヤーを定義し、元の線を前面からかぶせる
ようにするものだ：

   The second way to improve the filling accuracy is to expand the fill region
   slightly in a process akin to “trapping” that printers use to account for
   small misalignments in their printing plates. This works especially well for
   cartoons where the fills can be put on a separate *Layer* beneath a *Layer*
   containing the black lines.

このとき、塗りつぶし領域を膨張、収縮させることが考えられる。それを制御するのが
ツールバーの :guilabel:`Grow/shrink by` 欄だ：

   The amount of expansion is controlled by the :guilabel:`Grow/shrink by`
   parameter. As the name suggests, one can both expand and reduce the fill
   area.

Filling Multiple Regions
======================================================================

   Click-dragging the *Paint Bucket Tool* while holding the :kbd:`Alt` key down
   across several noncontiguous regions will cause all the regions to be filled.
   (Not holding the :kbd:`Alt` down will cause the borders to also be filled.)

:kbd:`Alt` キーを押しながらドラッグすると、ヒモ選択された領域群が塗りつぶされ
る。これらの領域は群全体として連結である必要はない。

:kbd:`Shift` + クリックでのバケツ塗りで代用可能と考えられる。

Closing Gaps
======================================================================

破線で囲まれたような形状もバケツ塗りできるオプションがある。バケツツールあるある
に、塗りつぶそうとした領域の境界が微妙に閉じていなくて、色が漏れる失敗がある。こ
れを防止できる。

   Small gaps in borders can be “filled” by setting the :guilabel:`Close gaps`
   to a value other than :guilabel:`None`. This prevents fills from leaking into
   undesired areas just because there is a small break in a line (as might
   happen in tracing a cartoon).

このオプションは画面画素を使うので、ズームレベルによって結果が異なることなどに注
意する。

Adding to a Fill
======================================================================

アルゴリズムの都合上「塗り漏れ」がスクリーン外に生じることがある。

   Since the *Paint Bucket Tool* uses pixels to calculate the area to be
   enclosed, Inkscape will clip the region off-screen to prevent the number of
   pixels that go into the filling algorithm from becoming too large.

その場合は手作業でバケツ塗り領域を追加する。そうすると継ぎ目が生じる可能性がある
ので、対応策が二つ紹介されている：

   If this happens you can either zoom out to do the fill or you can do the fill
   in pieces. By holding the :kbd:`Shift` down while clicking you can add to an
   existing fill. Unfortunately, this can lead to rendering artifacts between
   adjacent pieces even though they are part of the same path. Two solutions:

   #. Set the :guilabel:`Grow/shrink by` parameter to 0.10. This will ensure a
      slight overlap during the filling process. The overlap is removed in the
      unioning step.
   #. Use the Node Tool to adjust the nodes to overlap areas and then use the
      :guilabel:`Path --> Union` (:kbd:`Ctrl` + :kbd:`+`) command to remove the
      overlap.
