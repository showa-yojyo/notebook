======================================================================
Chapter 6. Geometric Shapes
======================================================================

.. contents::

..

   Inkscape provides a number of tools for drawing geometric shapes. The tools
   for drawing regular geometric shapes (rectangles, boxes, ellipses, regular
   polygons, stars, and spirals) are covered here.

形状と同様にスタイルも重要だ。本章で現れる形状には fill と stroke という属性があ
る：

   The style of an object includes attributes that determine how the inside of
   the shape (fill) and how the boundary path (stroke) are drawn. It also
   includes shape-specific attributes such as the number of points in a star.

現在スタイルという考え方があり、新しいオブジェクトに対してはそれがまず適用される。
スタイルは関係ツールの UI で変更可能。

   New objects are drawn with the *Current* style. Some components of the
   *Current* style are displayed (e.g. :guilabel:`Fill` color) or changed (e.g.
   number of points in a star) in the :guilabel:`Tool Controls` of a relevant
   tool.

現在スタイルが更新されるのは、直前に行われたスタイル操作の結果としてそうなる：

   A component of the *Current* style is changed when that component is modified

   By default, the shape tools (except the *Spiral Tool* and *Box Tool*) as well
   as the *Calligraphy Tool* are drawn with a global *Current* style. Changing
   the style for one of these tools, changes the style for all.

角度の属性がある形状を操作するのに用いられるユーザー設定項目がある：

   While drawing some objects (arcs, stars, regular polygons, and spirals), some
   features (such as the orientation of a polygon) can be constrained to
   specific angles with respect to the center of the shape and the horizontal
   axis. These angles are multiples of the :guilabel:`Rotation snap` angle.

前章の復習をする：

   Shapes can be scaled, rotated, and skewed. (See Chapter 5, Positioning and
   Transforming.) When doing so, a transformation is applied to the shape. The
   internal parameters defining the shape (such as the width and height of an
   ellipse) remain unchanged.

Rectangles and Squares
======================================================================

* *Rectangle Tool* の起動方法例：

  * :guilabel:`Toolbox` の当該ボタンを押す
  * :kbd:`F4` を押すか :kbd:`R` を押す

* 長方形を描くには、一方の角から対角線上反対側の角まで、左ボタンドラッグする。
* 正方形を描くには、:kbd:`Ctrl` を押しながらマウスをドラッグする。
  同じ操作で、高さと幅（またはその反対）の比が整数である長方形も描画可能。

  * 特例として、辺が「黄金比」に拘束された長方形も :kbd:`Ctrl` キーで描画可能。

* :kbd:`Shift` キーを押しながらドラッグすると、開始点を中心とするように矩形を描
  く。

矩形を編集するには、*Rectangle Tool* で矩形を左クリックし、矩形を選択する必要が
ある。選択されると、その角の一部にハンドル（小四角と円）が表示される。左上または
右下のハンドル（四角）を左ボタンドラッグすると、矩形の寸法を変更できる。

矩形の角にフィレットを適用することができる。円弧でも楕円弧でもよい：

   There are two ways to do this. The first is to use the handle(s) at the
   top-right corner of the rectangle. Initially, only one handle is visible. If
   this handle is dragged down, a rounded corner in the shape of a quarter
   circle is created. A second handle is now visible. Dragging this second
   handle to the left will create an elliptical rounded corner. Upon dragging
   the second handle, the radii of curvature in the horizontal (x) and vertical
   (y) directions are independent.

マウスよりも細かく制御するには *Rectangle Tool* 起動時にツールバーの
:guilabel:`Rx`, :guilabel:`Ry` 値を編集する。

フィレットを削除するには :guilabel:`Make corners sharp` ボタンを押す。

3D Boxes
======================================================================

*Box Tool* は三次元の箱の絵を描くツールで、次の記述から Inkscape 固有のオブジェ
クトであるように読める：

    A box is composed of an :abbr:`SVG` *Group* of six paths. Information about
    the vanishing points, and so forth are stored in the Inkscape *Name Space*.
    This extra information is only used by the *Box Tool*.

*Box Tool* の起動法は：

* :guilabel:`Toolbox` の当該ボタンを押す
* :kbd:`Shift` + :kbd:`F4` を押すか :kbd:`X` を押す

以下、箱の作図方法が記述されている。

   Use a *Left Mouse Drag* to draw the left side of the box (in the x-y plane).
   The start of the drag sets one corner while the end of the drag sets the
   opposite corner. The other sides of the box are automatically drawn with the
   right side of the box set to a default width.

六面体の一面（四角形）を自然なマウス操作で描くと、他の面（二つあるはず）は自動的
に描かれる。

   Pressing the :kbd:`Shift` while creating the box changes the function of the
   cursor to defining the depth (width of the right side or z dimension) of the
   box.

実際に :kbd:`Shift` キーを押したり離したりしてハンドルをドラッグすると、確かに挙
動が変わるのだが、それがこの記述のとおりなのかどうかがわからない。

   When a box is selected and the *Box Tool* active, a variety of handles are
   displayed. The eight handles at the corners of the box are used to adjust the
   size of the box.

観察の結果、◇型のハンドルが箱の八頂点を示すことがわかった。

   The four in front (see figure below) change the size of the left box face in
   the x-y plane. The other four change the depth (z) of the box.

◇ハンドルの拘束が点によって異なり、前面に付く四点は割と自由にドラッグ可能。それ
以外の四点の◇ハンドルはドラッグが消失点への直線上に拘束される。

   Holding the :kbd:`Shift` down swaps the functions of the handles.

:kbd:`Shift` 押しの場合は割と自由に動くのが後面の四点のほうに交代する。

   With the :kbd:`Ctrl` down, the handles are restricted in movement to lines
   along the box edges or to a box diagonal. This allows adjusting one dimension
   of a box face while keeping the other fixed in the first case or keeping the
   aspect ratio fixed in the latter case.

:kbd:`Ctrl` 押しのハンドル移動拘束によって、箱寸法調整または縦横比の維持を実現す
る。

   Dragging the *Cross* handle moves the box while keeping the same perspective.
   Without a modifier key, the box is kept in the x-y plane. Holding the
   :kbd:`Ctrl` down while dragging limits movement to lines along the box edge
   or along the box diagonal. Holding down the :kbd:`Shift` while dragging moves
   the box in the z direction.

実際にやってみると :kbd:`Ctrl` 押し✕ハンドル移動の挙動が読めない。

   By default, a box is drawn with two vanishing points, one each on the left
   (x) and right (z) sides. The vanishing points are initially placed at the
   edge of the page, halfway between the top and bottom.

消失点の初期位置がページ辺にあるので、そのままでは使い物にならない。調整にコツが
ある：

   The vanishing points can be dragged to new locations. Dragging the points a
   ways off the page will probably give you a more satisfactory perspective than
   the default.

図面内にある箱は消失点を共有するのが普通だが、選択的に消失点を変えることも可能だ。
反対に、異なる消失点を有する箱同士を共有させるように変更することも可能だ：

   All boxes that share the same vanishing points will change together. If you
   wish to change the vanishing points of just selected boxes, hold down the
   :kbd:`Shift` while dragging. If multiple boxes are selected with different
   vanishing points, dragging a vanishing point for one box near that of another
   box will “merge” the points together.

Perspectives
----------------------------------------------------------------------

箱オブジェクト用の *Tool Controls* で専用のボタンを押すことで、消失点を無限遠点
に指定することも可能だ：

   The type of perspective is changed via the *Box Tool Tool Controls*. Each of
   the three perspective points (x, y, and z) can be set to infinity or to a
   specific point. To set or unset a perspective point to infinity, toggle the
   “Parallel Lines” button in the *Tool Controls* next to the appropriate
   angle

無限遠点を使う場合には角度を明示的に入力する必要がある。入力欄へのショートカット
キーがある：

   The angles can be changed via the entry boxes in the *Tool Controls* or by
   using the keyboard shortcuts: x: :kbd:`[`, :kbd:`];` y: :kbd:`(`, :kbd:`);`
   and z: :kbd:`{,` :kbd:`}.`

角度の数値入力に関しては、いつもの規則が適用される：

   The angles will be changed by the :guilabel:`Rotation snap` angle (15° by
   default, settable in the :guilabel:`Steps` section of the :guilabel:`Inkscape
   Preferences` dialog). With the :guilabel:`Alt` key, the angle change will be
   0.5°.

Inkscape 1.2 ではラベルが :guilabel:`Rotation snaps every` という文言になってい
る。

一点透視図法では X と Y の無限遠点ボタンを押す。このとき角度
:guilabel:`X` と :guilabel:`Y` を 180°と 90°にそれぞれ設定する。 Z の無限遠点ボ
タンはオフにし、□消失点ハンドルを任意の位置（図面の中央付近がよい）にドラッグす
る。

二点透視図法では Y の無限遠点ボタンだけを押すのがよい。角度は 90°とする。あとは
X および Z 方向の消失点を適宜ドラッグして設定する。おそらく水平線に置く。

三点透視図法ではすべての消失点を図面上に置く。

等角図法の再現方法もある：

   Boxes can be drawn with an *Isometric Projection* by toggling on all
   “Parallel Line” buttons in the *Tool Controls* and setting the x, y, and z
   angles to be: 150°, 90°, and 30°, respectively.

Attributes
----------------------------------------------------------------------

箱を構成する面それぞれのスタイルを変更することが可能だが、面を選択するにはダブル
クリックは使えない。箱全体が選択されてしまうからだ。そうではなく、いったんグルー
プに入り、それから面をクリックすればよい。この辺の事情がピンと来なければ、グルー
プ選択や z-order が絡む選択方法の記述を再確認すること。

最後に、箱はいつも同じ色で塗られるのが気になるかもしれない。実際はユーザー設定が
関係している。

Ellipses, Circles, and Arcs
======================================================================

楕円ツールの起動方法：

* :guilabel:`Toolbox` の当該ボタンを押す
* :kbd:`F5` を押すか :kbd:`E` キーを押す

楕円や円弧を描くには、マウスの左ボタンドラッグを使用する。

* 楕円はドラッグの始点と終点で定義された長方形に内接するように描かれる。
* 円を描くには :kbd:`Ctrl` を押しながらドラッグ。
  また、高さと幅（またはその反対）比が整数または黄金比の楕円を描くことが可能。

* :kbd:`Shift` キーを押しながらドラッグすると、開始点を中心とした楕円が描かれる。
* :kbd:`Alt` キーを押しながらドラッグすると、ドラッグの始点と終点を通過する楕円
  が描かれる。
* :kbd:`Alt` + :kbd:`Ctrl` キーを押しながらドラッグすると、ドラッグの始点と終点を
  直径とする描かれる。

楕円を編集するには選択してからツールを起動する。ハンドルが現れるのでそれで図形を
編集する：

   When an ellipse is selected and the *Ellipse Tool* is active, the ellipse
   will have a set of handles (small squares and circles) that can be used to
   resize it or convert it to an arc. (The handles are also available if one of
   other shape *Tools* or the *Node Tool* is active.)

□ハンドルは寸法を調整する。○ハンドルは閉曲線を開くのに使う。実は初期状態では二つ
のハンドルが重なって表示されている：

   To convert an ellipse into an arc, use the two *Arc* handles. Initially both
   handles are on top of each other. Drag one handle to set one end of the arc,
   then drag the second handle to set the other end.

○ハンドルを移動するのにいつもの角度調整が可能だ：

   Holding down the :kbd:`Ctrl` key while dragging an *Arc* handle will force
   the angle of the arc to begin or end at a multiple of the :guilabel:`Rotation
   snap` angle (15° by default).

楕円用 *Tool Controls* には上記の操作のための UI がある。角度の方向については珍
しく時計回り方向が正になる：

   The :guilabel:`Start` and :guilabel:`End` angles are defined in degrees and
   are measured in the *clockwise* direction starting at the x-axis.

Regular Polygons and Stars
======================================================================

星ツールの起動方法：

* :guilabel:`Toolbox` の当該ボタンを押す
* :kbd:`Shift` + :kbd:`F6` を押すか :kbd:`*` キーを押す

多角形や星を描くには、いつものようにマウスの左ボタンドラッグを使用する：

   A star will be drawn with the center at the starting point of the drag and
   one vertex at the ending point of the drag. The vertex can be forced to be at
   a multiple of the :guilabel:`Rotation snap` angle (15 degrees by default) by
   holding down the :kbd:`Ctrl` key during the drag.

星形は、図形上の◇ハンドルをドラッグするか、*Star Tool* を選択した状態で *Tool
Controls* 上の設定を使用することで変形できる。ここでは重要なパラメーター二つを変
更することができる：

   The first is an option to specify that the shape drawn be a star or a
   polygon. This is controlled by two toggled buttons.

作成後でも星なのか凸多角形なのかをツールボタン押しで切り替えられるということだ。
また、頂点数も変更可能だ：

   The second is a parameter that controls the number of points in a star or the
   number of corners of a polygon.

次にハンドルの記述を見よう：

   There are two handles for stars (one for polygons). The *Tip* radius handle
   (see the *Notification Region* if in doubt which is which) is used to control
   the position of the tip of a star or corner vertex of a polygon. This is the
   handle that was used when first drawing the star or polygon. Using the
   :kbd:`Ctrl` key while dragging the handle restricts it to a radial line.

このツールに限らず、ハンドルをアクティブにしたときにステータスバーを観察する習慣
を身につけるのが上達への近道と思われる。

   The *Base radius* handle controls the position of the “inner” vertex of a
   star. The *Base radius* handle can be constrained to have an angle halfway
   between adjacent tips by holding down the :kbd:`Ctrl` key while dragging it.
   Note that it is possible that the radius of the *Base* vertex be larger than
   the *Tip* vertex or it can be negative as shown next.

内周頂点をかなり柔軟に制御できるようだ。本書の図を見るとわけがわからない。

フィレットは星、多角形にも適用可能だ：

   Holding the :kbd:`Shift` key while dragging either handle will round the
   corners of the star or pentagon.

そして頂点配置にランダム性を加える操作も用意されている：

   Holding the :kbd:`Alt` key while dragging either handle will move all the
   star's or polygon's vertices independently in a random fashion.

*Tool Controls* の残りの UI は扱いが難しい：

   For stars, it also contains a box to set the :guilabel:`Spoke ratio`. This is
   defined as the ratio of the *Base* radius to the *Tip* radius. Useful values
   are: for a regular 5-pointed star, 0.382; for a regular 6-pointed star,
   0.577; and for a regular 8-pointed star, 0.541.

これは幾何学的な計算から得られる数なので合理的なのだが、次のものはそうではない：

   Numerical values for :guilabel:`Rounded` and :guilabel:`Randomized` can also
   be entered (try ``-10`` for :guilabel:`Rounded`!).

編集し過ぎて手に負えなくなったら形状をリセットすることも可能だ：

   And lastly, there is a *Defaults* button to reset all of the settings to
   their default values.

Spirals
======================================================================

   The *Spiral Tool* can be used to draw Archimedes' spirals.

渦巻きツールの起動方法：

* :guilabel:`Toolbox` の当該ボタンを押す
* :kbd:`F9` を押すか :kbd:`I` キーを押す

渦を巻くには、他の形状ツールと同様に左ボタンドラッグで描く。拘束や角度スナップも
他のツールと同様の法則が働く：

   The start of the drag will be the spiral's center. Holding down the
   :kbd:`Ctrl` key while dragging will constrain the position of the spiral end
   point to a multiple of the :guilabel:`Rotation snap` angle (default 15
   degrees).

渦巻きは曲線の両端点それぞれ編集ハンドル◇がある。通常のドラッグでは、渦巻きの長
さが変化するだけだ：

   Dragging either handle allows rolling and unrolling the spiral from its
   respective end (i.e., making the spiral longer or shorter, or changing the
   radius of the inner and outer ends). Holding down the :kbd:`Ctrl` key forces
   the end to be at a multiple of the :guilabel:`Rotation snap` angle with
   respect to the center. Holding down the :guilabel:`Shift` key while clicking
   on the *Inner* handle will set the inner radius to zero.

内側ハンドルを :kbd:`Alt` を押しつつドラッグすると、渦巻きの発散具合が変化する。
次の数学的仕様により形状が定まる：

   The divergence is a measure of how rapidly the radius changes with respect to
   the angle as the spiral progresses. A divergence of one gives a spiral where
   the distance between successive turns remains uniform (an Archimedes'
   spiral). Divergences smaller (larger) than one give a spiral where the
   distance between successive turns decreases (increases) moving outward.
   Mathematically, the radius of a point is proportional to its angle (measured
   in radians) raised to a power equal to the divergence.

ドラッグをやめてクリックすると初期形状に戻る：

   Clicking on the Inner handle while holding down the :kbd:`Alt` key will reset
   the divergence to one.

外側ハンドルのほうが操作が直観的だ：

   The *Outer* handle can be used to scale and rotate the spiral by dragging it
   with the :kbd:`Shift` key pressed. If both the :kbd:`Shift` and :kbd:`Alt`
   keys are held down, then the spiral will only rotate, keeping the radius
   fixed.

専用 *Tool Controls* で巻数や上述のパラメーター入力を受け付ける欄がある。

渦巻きは塗りつぶしにも対応している。ただし、Inkscape がどのように図形を塗りつぶ
すかを理解する必要がある。これは後述の章まで待つことにする。

   A spiral is basically an open path. The *Fill* is drawn as if the path was
   closed with a line segment between the path ends (the *Inner* and *Outer*
   handles). Then the current *Fill Rule* is applied.
