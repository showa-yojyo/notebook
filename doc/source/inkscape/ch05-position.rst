======================================================================
Chapter 5. Positioning and Transforming
======================================================================

.. contents::

Inkscape はオブジェクトとそれに適用する座標変換を区別して管理していると理解でき
る。

   One key thing to know is that transforming a *Regular Shape* object or a
   *Group* of objects by the methods described in this chapter does not
   (usually) change the underlying description of the object(s).

   For example, suppose you have an ellipse that is 100 pixels wide but you need
   it to have a width of 50 pixels. There are two different ways to achieve the
   required width. The first is to scale the object by 50% in the horizontal (x)
   direction. The underlying definition of the ellipse width remains 100 pixels
   but when the ellipse is drawn a scale factor of 50% is applied in the
   horizontal direction. The second way to change the ellipse is to use the
   *Ellipse* Tool to resize the ellipse. In this case, the underlying
   description of the ellipse changes and no scale factor is applied.

前者は楕円と縮尺変換で表現し、後者は楕円自身の定義を変更するというものだ。

   An exception to this rule is for *Rectangle* objects. Inkscape will attempt
   to change the description of the rectangle itself when a simple
   transformation is applied.

:guilabel:`Rectangle` の拡縮変換は例外で、Inkscape はなるべく矩形自身を変更しよ
うとする。

Inkscape Coordinates
======================================================================

数学と違い、座標系の距離単位を確認するのが重要だ。

   When you open the main Inkscape window, *Rulers* are drawn by default at the
   top and left edges of the canvas. -略- The units of the *Rulers* are the same
   as the default units of the canvas. If you hover the pointer over a *Ruler*,
   a tool tip will show the current unit.

単位系の変換は次にように定められている。Inkscape 以外でも通用するので記憶してお
くと便利だ：

   Conversion between the units is fairly straightforward: 1 inch = 1/12 ft =
   2.54 cm = 25.4 mm = 0.0254 m = 6 pc = 72 pt.

キャンバス座標系と :abbr:`SVG` 標準座標系は異なることを理解する：

   One confusing aspect is that Inkscape uses a different scale internally. On
   the canvas, the x and y coordinates increase as one moves right or up.
   Internally the y coordinate is flipped as per the :abbr:`SVG` standard. Thus,
   (0, 0) is defined from the upper-left corner of the page region internally
   but at the bottom-left corner in the canvas window.

キャンバスのほうが右手座標系であることに注意したい。すると角度の測量も Inkscape
の画面上ではそれに準じる向きを正とする。

以上のシステムは既定値についての記述であり、ユーザー設定でオプションを変更でき
る。

Transformations
======================================================================

対象に座標変換を適用するには、それをまず選択状態にしておく必要がある：

   Each method begins by selecting an object or group of objects to be
   transformed. The *Select Tool* must be active for making transformations with
   the mouse or keyboard.

座標変換に関して注意点がいくつかある。箇条書きにしてまとめておく：

1. :abbr:`SVG` 画素と画面画素の区別がある。後者を使う変換操作はズームレベルに依
   存する。
2. オブジェクトの bounding box (BB) に二つの定義がある。視覚的か幾何的かで区別さ
   れる。
3. 先述のとおり、座標変換対象は通常その定義を変更されない
4. *Select* ツール使用時に *Tools* コントロールでオンオフを切り替えられるオプ
   ションが多数ある。
5. 回転変換と傾斜変換には中心点の概念がある。

項目 4. は描線の太さ、矩形の丸角、グラデーション、パターンに対する拡縮変換、移動
変換に影響する。

Transforms with the Mouse
----------------------------------------------------------------------

Translations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

左ボタンドラッグでオブジェクトを直観的に移動する。

:kbd:`Alt` を押しながらドラッグすると、開始位置に関係なく選択オブジェクトを移動
する。開始位置のオブジェクトを選択しない。

:kbd:`Ctrl` を押しながらドラッグすると、座標軸に対して平行に移動するようになる。

:kbd:`Shift` を押しながらドラッグすると、*Grids* に対するスナップが一時的に無効
になる。

上記のキーを伴う操作は組み合わせても機能する。

Scaling, Rotating, and Skewing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Inkscape オブジェクトを選択すると、座標変換制御用の UI が描画される。それを操作
することで表題の座標変換を大まかに指定する。

   When an object or objects are first selected, eight double-headed arrows will
   appear in a rectangle around the selection. A *Left Mouse Drag* of any handle
   will rescale the selection. The corner arrows will scale both in the
   horizontal (x) and vertical (y) directions. The side arrows will scale in
   only one direction.

オブジェクトを選択すると、最初に拡縮変換指定用のハンドルが現れ、もう一度クリック
するか、特定のキー操作によりハンドルが回転変換指定用に切り替わる：

   Clicking a second time on a selected object or using the keyboard shortcut
   :kbd:`Shift` + :kbd:`S` will change the direction of the double-headed
   arrows. Now, a *Left Mouse Drag* of a handle will rotate the selection if
   used on a corner arrow, or skew the selection if used on a side arrow. Click
   again to revert to the scaling mode.

また、回転中心ハンドルも指定可能だ：

   Rotation takes place around the *Rotation* center indicated by a
   “plus”-shaped handle.

回転中心の配置方法は本書参照（細かくてまとめるのが億劫だ）。

移動変換同様に、修飾キーを伴うドラッグ操作が用意されている：

   The :kbd:`Shift`, :kbd:`Ctrl`, and :kbd:`Alt` keys can be used with the *Left
   Mouse Drag*. They can be used in combination when scaling, rotating, or
   skewing.

Scaling
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:kbd:`Ctrl` 押しドラッグは縦横比を維持して拡縮する。

:kbd:`Shift` 押しドラッグは選択中心に関して対称的に拡縮する。

:kbd:`Alt` 押しドラッグは縮尺を整数倍または分子が 1 の単純な分数に制限する。縮尺
が負の値の場合、図形は反転する。

Rotating and Skewing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:kbd:`Ctrl` 押しドラッグは回転や傾斜を回転スナップ角の倍数に拘束する。

:kbd:`Shift` 押しドラッグは回転の場合は反対側の角を、傾斜の場合は反対側の辺を固
定する。拡縮操作の挙動と対照的であることに注意。

Transforms with the Keyboard
----------------------------------------------------------------------

キーボードで座標変換を実行する場合、キーの組み合わせによっては、変換の大きさは
ユーザー設定の :guilabel:`Steps` タブで設定できるパラメーターによって決まる。

.. admonition:: 利用者ノート

   設定ダイアログには検索欄があるので、そこに ``Steps`` と入力すればいい。
   その他の設定項目についても同じ方法が使える。

Translations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

矢印キーで選択オブジェクトを上下左右に動かすことができる。

.. csv-table::
   :delim: |
   :header-rows: 1
   :widths: auto

   キーバインド | 挙動
   矢印キー | :guilabel:`Arrow Keys move by` 量だけ移動
   :kbd:`Shift` + 矢印キー | 矢印キー単発だけのときの十倍移動
   :kbd:`Alt` + 矢印キー | 画面画素一個分だけ移動
   :kbd:`Alt` + :kbd:`Shift` + 矢印キー | 画面画素十個分だけ移動

Scaling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

拡縮変換は対象オブジェクトの BB の重心周りになされる。

.. csv-table::
   :delim: |
   :header-rows: 1
   :widths: auto

   キーバインド | 挙動
   :kbd:`.` or :kbd:`>` | 拡大
   :kbd:`,` or :kbd:`<` | 縮小
   :kbd:`Ctrl` + :kbd:`.` or :kbd:`Ctrl` + :kbd:`>` | 二倍の大きさになる
   :kbd:`Ctrl` + :kbd:`,` or :kbd:`Ctrl` + :kbd:`<` | 半分の大きさになる
   :kbd:`Alt` + :kbd:`.` or :kbd:`Alt` + :kbd:`>` | 画面画素単位ずつ拡大
   :kbd:`Alt` + :kbd:`,` or :kbd:`Alt` + :kbd:`<` | 画面画素単位ずつ縮小

修飾キーなしの拡縮はユーザー設定の :guilabel:`> and < scale` 値だけ大きさが変わ
る。

:kbd:`Alt` 押しの拡縮変換では、画面画素一つの長さを BB 中心から最も遠い端までの
距離で割った値を係数とする。

.. admonition:: 利用者ノート

   例えば :kbd:`>` は :kbd:`Shift` + :kbd:`.` のことだが、要するに :kbd:`Shift`
   を押しても押さなくてもかまわないということだ。

Rotation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

先述のとおり、回転変換の中心を BB 中心以外であるようにもできる。ここでのユーザー
設定値とは :guilabel:`Rotation snaps every` が適用される。

.. csv-table::
   :delim: |
   :header-rows: 1
   :widths: auto

   キーバインド | 操作
   :kbd:`[` | 左にユーザー設定値だけ回転
   :kbd:`]` | 右にユーザー設定値だけ回転
   :kbd:`Ctrl` + :kbd:`[` | 左に 90 度回転
   :kbd:`Ctrl` + :kbd:`]` | 右に 90 度回転
   :kbd:`Alt` + :kbd:`[` | 左に画面画素一つ分だけ回転
   :kbd:`Alt` + :kbd:`]` | 右に画面画素一つ分だけ回転

:kbd:`Alt` 押しの回転変換の量がわかりにくいが、画面画素長を BB 中心からその頂点
までの距離で割った値の正接とある。

Flipping
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Flip around center point of bounding box if in scaling mode or around
   horizontal/vertical line passing through *Rotation* center if in
   rotation/skewing mode.

.. csv-table::
   :delim: |
   :header-rows: 1
   :widths: auto

   キーバインド | 操作
   :kbd:`H` | 水平に反転
   :kbd:`V` | 垂直に反転

Transforms with the Tool Controls Bar
----------------------------------------------------------------------

:guilabel:`Tool Controls Bar` の :guilabel:`X`, :guilabel:`Y`, :guilabel:`W`,
:guilabel:`H` でも移動や寸法変更を適用できる。錠前アイコンをクリックすると、縦横
比を固定したまま変換できるようになる。

Transforms with the Object Drop-Down Menu
----------------------------------------------------------------------

メインメニュー :menuselection:`Object` にある項目でも一部の変換操作を実行できる：

* :menuselection:`Object --> Rotate 90°CW`
* :menuselection:`Object --> Rotate 90°CCW`
* :menuselection:`Object --> Flip Horizontal`
* :menuselection:`Object --> Flip Vertical`

.. admonition:: 利用者ノート

   キーボードのほうが早い。

Transforms with the Transform Dialog
----------------------------------------------------------------------

   Objects can be moved, scaled, rotated, and skewed using the
   :guilabel:`Transform` dialog (:menuselection:`Object --> Transform...`
   :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`M`). There is a different tab in the
   dialog for each of these transforms. In addition, there is a
   :guilabel:`Matrix` tab that allows the application of a *Transformation
   Matrix* to a selection.

細かい数値入力で座標変換する場合にはこの UI を利用する。行列成分を直接指定するこ
とも可能だ。

   The :guilabel:`Transform` dialog contains an option to apply the chosen
   transformation to a selection as a group or to the individual objects within
   the selection. (This option has no effect for the :guilabel:`Matrix` tab.)

変換の適用先がグループ全体なのか、グループを構成する要素一つ一つなのかを決められ
る。:guilabel:`Apply to each object separately` にチェックを入れると後者を指定す
ることになる。

Move Tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Relative move` だけ注意。入力値が移動量なのか、移動先座標なのかを指定
するものだ。変換対象が複数ある場合に挙動の違いが顕著になる。

Scale Tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Scale proportionally` をオンにすると、対象の BB 縦横比を固定しつつ拡
縮する。

Rotate Tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

UI が単純なので見ればわかる。回転の向きを切り替えるボタンもあるが、正が左周りを
意味するのが Inkscape では基本だ。

Skew Tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   You can skew in the horizontal and vertical directions separately. The
   skewing is relative to the center of the bounding box. The magnitude of the
   skew can be specified as a distance, percentage, or angle. In all cases, the
   skew is relative to the size of the bounding box.

.. admonition:: 利用者ノート

   馴染みのない変換なので後回しにする。

Matrix Tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

このタブでは同次変換行列を直接設定することができる。行列の形は次のとおり：

.. math::
   :nowrap:

   \begin{aligned}
   \begin{pmatrix}
   A & C & E\\
   B & D & F\\
   0 & 0 & 1
   \end{pmatrix}
   \end{aligned}

行列は点に対して左から作用する。

   The tab includes the option :guilabel:`Edit current matrix` to select if the
   entered matrix should post-multiply the existing transformation matrix
   (option not selected) or if it should replace the current matrix (option
   selected).

問題は次の仕様だ。どちらの行列を編集するかによって、座標変換が基づく座標系が異な
るという：

   the transformation matrix is with respect to the point :math:`(0, 0)` in
   screen coordinates if not editing the current matrix. If editing the current
   matrix, the transformation is with respect to the *User Coordinate System*
   which, if an object is not in a *Group*, is equivalent to the :abbr:`SVG`
   coordinate system (*Initial View Port*) where the origin is at the top-left
   corner of the page. See the :abbr:`SVG` standard for more details.

さらに、ダイアログ上で見えている数値と、:abbr:`SVG` に記述されるそれとがユーザー
設定により異なる場合があることに注意する：

   Second, Inkscape will modify the matrix and other parameters of an object
   internally so that the internal E and F terms are zero if the
   :guilabel:`Store transformation` parameter under the :guilabel:`Transforms`
   section in the :guilabel:`Inkscape Preferences` dialog is set to
   :guilabel:`Optimized`. This means, for example, that for a horizontal skew of
   a rectangle, the internal height parameter may change. The displayed object
   will still look correct.

Transforms with Paste Size Commands
----------------------------------------------------------------------

:menuselection:`Edit --> Paste Size --> Paste something` 系コマンドについて。ク
リップボードにいったん基準となるオブジェクトを置く必要がある。

   To use the commands, first copy (or cut) a selection with the desired
   dimension(s) to load the selection into the clipboard.

次のコマンドは、クリップボードに合わせて選択範囲を全体的に拡縮する：

* :menuselection:`Edit --> Paste Size --> Paste Size`
* :menuselection:`Edit --> Paste Size --> Paste Width`
* :menuselection:`Edit --> Paste Size --> Paste Height`

次のコマンドは、クリップボードに合わせてオブジェクトそれぞれを拡縮する：

* :menuselection:`Edit --> Paste Size --> Paste Size Separately`
* :menuselection:`Edit --> Paste Size --> Paste Width Separately`
* :menuselection:`Edit --> Paste Size --> Paste Height Separately`

寸法は BB によって決まる。

Transforms with the XML Editor
----------------------------------------------------------------------

   Full control over the transformation of an object is available through the
   :guilabel:`XML Editor` dialog (:menuselection:`Edit --> XML Editor...`
   (:guilabel:`Shift` + :guilabel:`Ctrl` + :guilabel:`X`)).

文書の本体である :abbr:`XML` を直接編集することで座標変換を完全に調整することが
可能だ。特に行列成分を編集するときには、その出現順序を正確に理解しておく必要があ
る：

   Any transform an object is subject to is described by the ``transform``
   attribute. A transform can be of type ``translate``, ``scale``, ``rotate``,
   ``skewX``, ``skewY``, or ``matrix``. In most cases, the transform will be of
   the ``matrix`` type. A matrix entry contains the *Transformation Matrix* in
   the order (A, B, C, D, E, F) where (ACE) is the first row of the matrix.

前述の適用座標系が何であるかに関する注意をここでも意識すること。

Snapping
======================================================================

.. admonition:: 読者ノート

   前半のパラグラフの内容が Inkscape 1.2 に即していないので、自分で調べてまとめ
   るしかない。

:guilabel:`Preferences` の :menuselection:`Behavior --> Snapping` 内の設定項目と
して流用できる記述がある：

:guilabel:`Delay (in seconds)`
   マウスカーソルの移動が停止してからスナップが行われるまでの遅延時間。スナップ
   対象が多い場合に効果的だ。

:guilabel:`Only snap the node closest to pointer`
   読んで字のごとく。ノード数が多い場合に効果的。

:guilabel:`Weight factor`
   複数のスナップが可能な場合、この値がスナップ点とスナップ対象の間の最小距離を
   優先するか、カーソルに最も近いスナップ点を使用するようなスナップを優先するか
   を決定する。0 に近いほど前者に、1 に近いほど後者に強くスナップする。

Snapping Objects
----------------------------------------------------------------------

:guilabel:`Snap Controls Bar` に様々なスナップ点や対象のオンオフを切り替えるボタ
ンがある。この UI はいくつかの区画からなる。

1. チェックボックス :guilabel:`Enable snapping` のみの区画。スナップ（ガイド線と
   グリッドをも含む）のオンオフを大域的に切り替える。
2. チェックボックス :guilabel:`Bounding boxes` が先頭にある区画。BB で定義された
   点へのスナップと、その点からのスナップに関するものだ。
3. チェックボックス :guilabel:`Nodes` が先頭にある区画。ノードとハンドルへのス
   ナップのオプションで構成される。
4. チェックボックス :guilabel:`Other points` が先頭にある区画。
5. チェックボックス :guilabel:`Alignment` が先頭にある区画。
6. 残るは、グリッド、ガイド線、ページ境界へのスナップのオンとオフを切り替えるた
   めのチェックボックスそれぞれがある。

:guilabel:`Enable snapping` はキーバインド :kbd:`%` を叩くほうが早い。

本書で解説があるのは 2. と 3. だ。BB のスナップで注意するのは :guilabel:`Edges`
だろうか：

   Note that edges are never snap points.

ノード系は :abbr:`CAD` でよく世話になっていたから大丈夫。

Guides
----------------------------------------------------------------------

   Guide Lines are individual lines that can be arbitrarily placed. They are
   defined by an x-y anchor (origin point) through which the line passes and an
   angle. The anchor is shown as a small circle on the line.

グリッドが規則性を特徴とするのに対して、ガイド線は任意に配置できる。

ガイド線の表示切り替えはメインメニューから :menuselection:`View --> Guides` を選
択するか、キーバインド :kbd:`|` を押す。ガイド線は表示状態でなければ有効にならな
い。

Guide Creation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ガイド線は水平や垂直のものならワープロソフトの感覚で引ける。

   To create a *Guide Line*, *Left Mouse Drag* from the left *Ruler* onto the
   canvas for a vertical *Guide Line* or from the top *Ruler* for a horizontal
   *Guide Line*.

定規部分からキャンバスにドラッグするとガイド線が追加されていく。

   An angled *Guide Line* can be created by dragging from the end
   of a *Ruler*. By default, the angle is set to 45° if a rectangular *Grid* is
   displayed or parallel to the angled lines if an axonometric *Grid* is
   displayed.

後者の状況がわからない。

Guide Adjustment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Guide Lines can be translated and rotated using the mouse

いったんガイド線を引くと、それをマウスでずらしたり回したりできる。

* 左ボタンドラッグで直線とアンカーを並進移動。ページの外にドラッグすると削除。

  * :kbd:`Shift` を押しながらだとアンカーを中心にガイド線を回転。ドラッグ開始位
    置をアンカーと一致させないようにすること。
  * :kbd:`Ctrl` を押しながらだとアンカーをガイド線上に拘束しつつ移動。
  * :kbd:`Ctrl` + :kbd:`Shift` を押しながらだと 15 度（既定値）の整数倍だけガイ
    ド線を回転。

* :kbd:`Del`: ガイド線上にある限り、それを削除。

   *Guide Lines* can be precisely placed by using the :guilabel:`Guide Line`
   dialog, called up by double-clicking on a *Guide Line*. A check box toggles
   between absolute and relative placement.

ラベルを設定可能であるなど、UI がバージョン 1.2 では本書のスクリーンショットと異
なる。

Guides Created from Objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Guide Lines can be created from objects using the :menuselection:`Object -->
   Object to Guides` (:kbd:`Shift` + :kbd:`G`) command. -略- In each case, the
   selected objects are deleted unless the :guilabel:`Keep objects after
   conversion to guides entry` is checked in the :guilabel:`Tools` section of
   the :guilabel:`Inkscape Preferences` dialog.

ガイド線をオブジェクトから生成する状況では、用済みになったオブジェクトを削除する
のが一般的であるようだ。

本書では矩形、三角形、円などから生成されるガイド線の仕様を説明している。当ノート
では割愛。

グループを選択する場合には、その構成要素それぞれに対してガイド線が生成される。

Grid
----------------------------------------------------------------------

グリッドといっても正方形以外にも正三角形からなるものもある：

   A *Grid* is composed of two or three sets of evenly spaced parallel lines. A
   *Rectangular Grid* consists of horizontal and vertical lines, much like a
   sheet of ordinary graph paper. An *Axonometric Grid* consists of three sets
   of parallel lines, typically one vertical and two at 30° angles from the
   horizontal. It is often used to draw three-dimensional objects.

グリッドは編集中の文書に関連付けられていて、アプリケーションの設定ではない：

   *Grids* can be created and edited on the :guilabel:`Grids` tab of the
   :guilabel:`Document Properties` dialog. To create a *Grid*, select the type
   (:guilabel:`Rectangular` or :guilabel:`Axonometric`) from the drop-down menu
   at the top of the dialog and then click on the :guilabel:`New` button. The
   parameters for the new *Grid* will then be editable under a tab in the bottom
   of the dialog. It is possible to have more than one *Grid* defined (and in
   use). Each *Grid* will have a tab entry.

実際に設定画面の UI を見ると、:abbr:`CAD` の作業平面のそれと共通する属性もいくつ
かある。新規グリッドの属性の初期値はアプリケーション設定で決まる：

   The default *Grid* parameters can be modified in the *Grids* section of the
   :guilabel:`Inkscape Preferences` dialog.

複数のグリッドを文書に追加することが可能なのは、図面を異なるウィンドウで表示する
ことを念頭に置いていることによる。グリッドごとに表示状態や有効状態を切り替えられ
ることに注意：

   Different “views” of the same drawing share the same *Grids* but the *Grids*
   can be enabled or made visible independently for each view.

Alignment and Distribution of Objects
======================================================================

:guilabel:`Align and Distribute` ダイアログの表示方法をまず記憶する：

* :menuselection:`Object --> Align and Distribute`
* :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`A`

   Two types of positioning are available: alignment where the centers or edges
   of objects are aligned to one another, and distributing where objects are
   distributed in some direction based on their centers or edges.

以下、:guilabel:`Align` タブ UI と操作の記述がしばらく続く。

Align
----------------------------------------------------------------------

オブジェクトの位置を揃えるには、:guilabel:`Relative to` で揃える基準となるものを
指定する。次のような選択肢からなる：

* オブジェクト：最初の選択、最後の選択、最大寸法のもの、最小寸法のもの。
* ページ
* 図面
* 選択範囲

:guilabel:`Move selection as group` をチェックすると、選択オブジェクト全体が位置
合わせ中にだけグループ化されて扱われる。これは手動でグループ化したり解除したりす
る手間を省く。

どこに揃えるかを対応するボタンを押して指定する。アイコンを見ればどうなるかわか
る。

.. admonition:: 読書ノート

   次の便利なキーバインドが定義されている。配列操作には :guilabel:`Relative to`
   での指示が反映されるのだが、状況次第ではダイアログを表示せずともオブジェクト
   を配列することができることが期待できる。

   .. csv-table::
      :delim: |
      :header-rows: 1
      :widths: auto

      キーバインド | 操作
      :kbd:`Ctrl` + :kbd:`Alt` + :kbd:`H` | Center on vertical axis
      :kbd:`Ctrl` + :kbd:`Alt` + :kbd:`T` | Center on horizontal axis
      :kbd:`Ctrl` + :kbd:`Alt` + :kbd:`Num5` | 上記の操作の合成
      :kbd:`Ctrl` + :kbd:`Alt` + :kbd:`Num4` | Align left edges
      :kbd:`Ctrl` + :kbd:`Alt` + :kbd:`Num8` | Align top edges
      :kbd:`Ctrl` + :kbd:`Alt` + :kbd:`Num6` | Align right edges
      :kbd:`Ctrl` + :kbd:`Alt` + :kbd:`Num2` | Align bottom edges

Distribute: Uniform
----------------------------------------------------------------------

オブジェクトを水平または垂直方向に一様にばらけさせる。

   The distribution of objects is between the two objects at the extremes (i.e.,
   the leftmost and rightmost objects for horizontal distribution). The
   definition of which is the leftmost and rightmost object is made using the
   objects' bounding boxes, and it may depend on the type of distribution
   selected. For example, if a distribution is based on the rightmost edge of
   the objects, then the objects rightmost edge will be used to determine which
   objects are at the extremes.

わかりやすいアイコンの付いたボタンを押して選択オブジェクトを配置する。

Distribute: Non-Uniform
----------------------------------------------------------------------

バージョン 1.2 では :guilabel:`Rearrange` という区画にさらなる操作とともに整理さ
れている。ツールボタン左から：

* グラフ構造のノードをいい感じに配置する
* オブジェクトの位置を入れ替える

  * 選択順
  * z-order
  * 巡回

* 中心からランダムに配置する
* オブジェクトの塊を解く（端から端までの距離をより均等にするようにを移動させる）

Distribute: Remove Overlaps
----------------------------------------------------------------------

   Two entry boxes, one for the horizontal direction and the other for the
   vertical direction, allow the addition of a minimum space between adjacent
   objects.

Rows and Columns
----------------------------------------------------------------------

この節の記述は :guilabel:`Grid` タブの UI に相当する。複数オブジェクトを行列に配
置するためのものだ。次のような方法で配置しようとする：

   The algorithm for determining the order the objects are placed in the array
   attempts to preserve any existing rows. For this algorithm, the bounding box
   of each object is used. Technically, the objects are first sorted by their
   vertical positions. Then objects that overlap vertically are sorted by their
   horizontal positions. Finally, the objects are placed from left to right and
   from top to bottom in the array.

ここまでの手順はオブジェクトの並び順しか決めない。座標の調整にまだ指定が要る：

   For placing objects, the grid is divided into cells. First, the cell size and
   placement is determined and then the objects are positioned inside the cells,
   one object to one cell.

   Cells are given the height of the tallest object if the :guilabel:`Equal
   height` box is checked; otherwise, they are given the height of the tallest
   object in their row. A similar policy is followed for width.

セル間隔を等間隔にするのか、手動で距離を指定するのかを選択しなければいけない：

   If the :guilabel:`Fit into selection` option is selected, the rows and
   columns of cells are evenly spaced with the edge rows and columns flush
   against the bounding box of the selection. If the :guilabel:`Set spacing`
   option is selected, the rows and columns are separated by the amount entered
   in the :guilabel:`Row` spacing and :guilabel:`Column` spacing entry boxes.
   The spacing can be negative.

:guilabel:`Alignment` のラジオボタンを押して、各セルにあるオブジェクトをどの辺に
揃えるのかを決める。その際、注意点がある：

   Note that the bounding box of all the objects after alignment may not be the
   same as the bounding box of the selection prior to alignment even though the
   :guilabel:`Fit to selection` option has been chosen. This is because the
   selection bounding box has been used to place the cells. The objects within
   the cells may not touch the cell walls.
