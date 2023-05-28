======================================================================
Chapter 19. Tiling
======================================================================

.. contents::

私がいた世界と tessellation の意味合いが若干異なるので、注意する意味で引用する：

   Tiling or tessellation is the covering of a surface with the repeated use of
   the same shape tile. A typical example is the tiling in a bathroom.

同一のタイルを反復するだけではつまらないので、Inkscape では工夫を入れる：

   In Inkscape, this concept is expanded to include a multitude of options,
   including progressively changing the tile size, spacing, and orientation.

この手法の基本は複製パターンにある。第四章を復習しておくといい。

   While random use of the :guilabel:`Tile Clones` dialog can produce exquisite
   patterns, it is useful to understand the fundamentals of tessellation in
   order to have more control over the final design.

基本は大切だ。

   To construct a tiling, open up the :guilabel:`Create Tiled Clones` dialog
   (:menuselection:`Edit --> Clone --> Create Tiled Clones...`).

このコマンドが複製メニューの下にあることが面白い。

当分 :guilabel:`Create Tiled Clones` ダイアログのスクリーンショットに基づいて解
説が続く。ダイアログ下部がモードに依らない固定 UI になっている。

:guilabel:`Rows, columns`
   矩形タイルの敷き詰め時にしか適切でない。
:guilabel:`Width, height`
   被覆対象領域の寸法。
:guilabel:`Used saved size and position of the tile`
   オンにすると前回コマンド実行時における基礎タイルの寸法と位置を使用するように
   なる。後で基礎タイルを更新して BB が変更された場合にもタイル間の間隔が保たれ
   る。
:guilabel:`Reset`
   タブの下にある項目を既定値に戻す。
:guilabel:`Remove`
   基礎タイル選択中に押すとコマンドを undo する。
:guilabel:`Unclump`
   複製タイルをある程度ランダムに撒き散らす。反復実行可能。
:guilabel:`Create`
   敷き詰めコマンドを実行する

単純な例が示されている。円を P1 モードで 2x2 に敷き詰めした結果だ。元オブジェク
トがまだそこにあることと、BB に基づいて配置されていることを理解する。

:guilabel:`Symmetry` Tab
======================================================================

対称性が基本中の基本ということで、このタブが先頭にある。

   The Symmetry tab is at the heart of the tiling process. Understanding the
   different symmetries is necessary to have full control over the outcome of a
   tiling.

   It is known that there are 17 such tiling symmetries. (See: Wikipedia entry.)
   All 17 symmetries are included in the Inkscape :guilabel:`Create Tiled
   Clones` dialog.

矩形モノと六角形モノがそれぞれ 12 個、5 個ある。後者のタイプでは基礎タイルの BB
が問題になる。三角形のほうが BB より真に小さいので、場合によってはタイルが重なり
合う：

   Inkscape uses the bounding box of an object to determine the basic tile size.
   For rectangular base tiles, the bounding box corresponds to the base tile.
   However, for triangular base tiles, the base tile covers only part of the
   bounding box area. This can result in tiles “overlapping” if an object
   extends outside the base tile shape (but is still within the bounding box) as
   in the tiling in the introduction to this chapter.

敷き詰め実行後に基礎タイルを変更してもタイル同士が重なり合うことが起こり得る。

敷き詰め後に基礎タイルの寸法を変更する場合には :guilabel:`XML Editor` ダイアログ
を使うなどして、:abbr:`SVG` データを直接修正する：

   If you need to adjust the base tile size after having created a tiling, you
   can use the :abbr:`XML` Editor dialog to change the parameters
   ``inkscape:tile-h`` and ``inkscape:tile-w`` (these will appear after you have
   cloned the object and are used only if the Use saved size and position of the
   tile button is checked).

:guilabel:`Shift` Tab
======================================================================

ここでは敷き詰めたタイルをさまざまな方式でずらす。次のオプションがある：

:guilabel:`Shift X`, :guilabel:`Shift Y`
   BB の幅と高さを単位として、タイルの間隔をずらす。ランダムな変異を与えるオプ
   ションもある。
:guilabel:`Exponent`
   各タイルの位置が :math:`{(1 + s_x)^{p_x},}{(1 + s_y)^{p_y}}` となるように
   :math:`p_x, p_y` を与える。
:guilabel:`Alternate`
   加算と減算を交互に行ってずらす。
:guilabel:`Cumulate`
   例えば上述のずらし量が 10% である場合、通常、後続のタイル間隔は 10%, 20%,
   30%, ... となる。このオプションを使うと、間隔が 10%, (10+20)%, (10+20+30)%,
   ... となる。タイルの拡縮も行うときにタイル間隔を一定に保つのに便利だ。
:guilabel:`Exclude tile`
   タイルの幅または高さをタイル間隔の計算で除外する。これは回転オプションを使用
   してタイルを円周上に配置する場合に便利だ。

ここにある四枚の P1 ベースの Shift は理解できる。

   Question: What is the symmetry of closely packed hexagons? The answer is P1
   as can be seen below. One can use this fact to trivially generate the board
   for the game Hex invented independently by the mathematicians Piet Hein and
   John Nash.

前節で注意されたように、P1 で平行四辺形を敷き詰められる。平面を六角形で敷き詰め
ることは、イラストのように平行四辺形を分割したものを P1 で敷き詰めることと同じだ
から、これも可能だ：

   Closely packed hexagons have a P1 symmetry tiling as shown on the left. On
   the right is the board for the game Hex. To generate both tilings, a hexagon
   was tiled using a shift in x of 50% and a shift in y of -25% per row.

六角形を敷き詰めるには (x, y) に対するずらし量を (50%, -25%) とすればよい。

:guilabel:`Scale` Tab
======================================================================

行と列の位置に応じてタイルの寸法を増減させる。

:guilabel:`Scale X`, :guilabel:`Scale Y`
   各タイルを百分率指定で拡縮する。ランダム因数を追加するのもあり。
:guilabel:`Exponent`
   :math:`S` が :math:`S^p` となるように :math:`p` を指定してタイルを拡縮する。
:guilabel:`Base`
   対数渦を作成するために用いられるオプション。
   :math:`S` が :math:`b^{S-1}` となるように :math:`b` を指定する。つまり
   :math:`{b = 1}` の場合は拡縮変更なし。
   収束する渦には 1 より小さい値を、発散する渦には 1 より大きい値を指定する。真
   の対数渦は、:math:`2.718` またはその逆数 :math:`0.368` で :math:`b` を指定す
   る。
:guilabel:`Alternate`
   タイルの拡大・縮小を交互に行うかどうか。
:guilabel:`Cumulate`
   拡縮が累積的であるかどうか（前節参照）。

イラスト二枚目の隙間を潰す技法を習得しておきたい：

   A general rule is that to keep scaled tiles just touching, specify a
   cumulative shift that is half of the scaling (in percent).

:guilabel:`Rotation` Tab
======================================================================

行と列の位置に応じてタイルが回転する。それぞれの回転中心はオブジェクト編集時の回
転操作における中心だ。

:guilabel:`Angle`
   回転角度。ランダム因数を追加するのもあり。
:guilabel:`Alternate`
   回転の向きを交互に入れ替えるかどうか。
:guilabel:`Cumulate`
   回転量が累積的であるかどうか（前節参照）。

イラストを見てオプションが想像できるので問題ない。

:guilabel:`Blur and Opacity` Tab
======================================================================

   The :guilabel:`Blur and opacity` tab allows one to change the *blur* and/or
   *transparency* of each tile depending on the row and column position.

Blur
----------------------------------------------------------------------

   A *Gaussian Blur* filter can be applied to each clone with different blurring
   values.

カモーンカカカモーンの仕上げに利用することが考えられる。

   The blur change is specified in percent. The change in blur can be specified
   to :guilabel:`Alternate` between a positive and negative value; however, a
   negative blur value can be entered in the :guilabel:`Per row` and
   :guilabel:`Per column` boxes. A :guilabel:`Randomizer` factor can also be
   specified.

いつもと同じオプションだが、ぼかしの値を負にするということは、いったん正にした値
を元に直そうとするということだ。

Opacity
----------------------------------------------------------------------

   The opacity change is specified in percent. The change in opacity can be
   specified to :guilabel:`Alternate` between a positive and negative value. A
   :guilabel:`Randomizer` factor can also be specified.

こちらも同じことが言える。

:guilabel:`Color` Tab
======================================================================

行と列の位置に応じて各タイルの色を変更する。ただし、色空間は :abbr:`HSL` 固定で
百分率指定とする：

   The *Hue* repeats itself after a change of 100%. The full scale for
   *Saturation* and *Lightness* components are each 100%. The changes in the
   three parameters can be specified to :guilabel:`Alternate` between a positive
   and negative change. A :guilabel:`Randomizer` factor can also be specified.

Hue が境界値で何色になるのかを調べておくほうがいいだろう。残りのオプションはよそ
のタブと同様。

このタブでの指定を有効にするには、オブジェクトの地の属性を *Unset* にしておくな
ど、準備が要る：

   Two key points: First, the :guilabel:`Fill` and/or :guilabel:`Stroke paint`
   must be specified as *Unset* (see the section called “Fill and Stroke
   Paint”). Second, an *Initial color* must be specified by using the
   :guilabel:`Initial color of tiled clones` dialog accessible by clicking on
   the color button next to the :guilabel:`Initial Color` label.

グレースケールのタイルを作成したくとも、白や黒の初期色を設定することは不可能だ：

   Note that it is meaningless to have only a shift in *Hue* with a starting
   color of black or white. This is like trying to walk east from the North
   Pole.

:guilabel:`Trace`
======================================================================

最後のタブだ。これまでのタブではタイルの描画属性を行と列の番号で決定するのが基本
的だったが、このモードはタイルの場所にあるオブジェクトやビットマップの描画属性が
決定する：

   The :guilabel:`Trace` tab allows one to set the color, size, and transparency
   of the tiles by the color or transparency of the objects (including bitmaps)
   that are placed under the location of the tiling. To enable this feature, the
   :guilabel:`Trace the drawing under the tiles` box must be checked.

このタブは三区画ある。

1. :guilabel:`Pick from the drawing`
2. :guilabel:`Tweak the picked value`
3. :guilabel:`Apply the value to the clones`

区画 1 では下絵の属性を指定する。色の場合には :abbr:`HSL` または :abbr:`RGB` か
ら成分指定方式を選択できる。

区画 2 では入力値を補正する：

   One can specify a Gamma correction or add a randomization factor to the
   input. One can also invert the input.

区画 3 ではタイルのどの属性に影響を与えるかを指定する：

   Options include *Presence* (the probability that a given tile will be drawn),
   color, size, and opacity.

色変更については :guilabel:`Color` タブと同じ理由で *Unset* 属性が要る。

   The color will only be changed for regions of the base tile that have *Unset*
   fill.

み変更される。

最後の虹背景のデモでは、アルファー値が放射グラデーションで定義されていることに注
意して観察すること：

   The inside of the rainbow is defined as a white gradient stop with zero
   *Alpha*. The last outside stop is defined with a red color and with zero
   *Alpha*. For most figures, a star inside an unfilled rectangle is used as the
   base tile. The star has been given an *Unset* fill when color is selected in
   the output.

Tricks
======================================================================

これまで見てきたデモはタイルを縦横に配列するものが多かったが、円環状にも渦巻状に
も配列することも可能だ：

   To put a tile along an arc use the P1 symmetry with one row of tiles. Check
   the :guilabel:`Exclude` tile box. The *Rotation center* is used as the center
   of rotation.

最初の二つのデモは EU 旗で見たデザインと似ているようだが、☆の姿勢が異なる：

   The base tile is drawn on the left, showing the *Rotation center* of the tile.
   On the right is after a P1 tiling with a per column shift removed by checking
   the :guilabel:`Exclude` tile box and with a rotation of 60%.

   The next figure shows how 12 stars can be put in a circle. This would have
   been an alternative way of placing the stars in the European Union flag if
   the stars did not need to be placed with one of their points straight up.

同じ技法を用いて螺旋曲線上にオブジェクトを配列することが可能だ。螺旋曲線なので、
数値の指定をそれらしくしないと不格好になることに注意する：

   Stars on a logarithmic spiral. The tile size is increased by 2.5% with
   :guilabel:`Base` set to 2.7. Each tile is rotated 20°.

   Stars on a logarithmic spiral. The tile size is increased by 2.5% with
   :guilabel:`Base` set to 2.7. Each tile is rotated 20°. The per column shift
   has been set to 60% (with the :guilabel:`Exclude` tile box checked).

VJ GYO 的なデザインの解説を読んでいく。

   A “P1 symmetry” tiling. 8 rows, 21 columns. *Rotation* of -11.5° per row and
   20.6° per column, *Scale* of 39.3% per row and 24.2% per column with a
   :guilabel:`Base` of 2.7 for both *x* and *y*. The pattern matches that for a
   pine cone with 8 rows in one direction and 13 in the other.

   For the mathematicians: note that 13 times the per column scaling is equal to
   8 times the per row scaling and that 13 times the per column rotation minus 8
   times the per row rotation is equal to 360°. This is due to the constraint
   that the 14th star in the first row is the same as the 9th star in the first
   column.

8 行 21 列の敷き詰め。行方向でも列方向でも回転および縮小がかかる。最初から数えて
9 番目のタイルが二行目の最初のタイルに相当するように角度を調整しているようだ。

   A circle tiled on an arc. The red circle with the Rotation center moved off
   center was the source tile.

これはノーヒントで再現したい。
