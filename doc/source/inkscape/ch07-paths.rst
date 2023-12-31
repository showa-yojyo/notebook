======================================================================
Chapter 7. Paths
======================================================================

.. contents::

当マニュアルはパスを二章構成で述べている。本章は用語、表現方法、作成、編集につい
て、次章は効果について述べる。

パス一本は *Open* または *Closed* のいずれか一方であるのか、またはそのようなパス
を合成したもの、*Compound* のいずれかとなる。

前章で述べたようなオブジェクトを選択して :menuselection:`Path --> Object to
Path` を決定するか、:kbd:`Ctrl` + :kbd:`Shift` + :kbd:`C` を押すと、対象はパスに
変換される。この逆操作はない。

Bezier Curves
======================================================================

この節で記述されている Bezier 曲線の構成は、Inkscape 固有のものでは全然なく、他
のアプリケーションでも論理的には同じはずだ。要点を箇条書きでまとめておく：

* 通常、パスは Bezier 曲線が複数結合しているものだ（前述の *Compound* でなけれ
  ば）。
* Bezier 曲線一本は四点で定義される。両端点とそれぞれにおける接ベクトルを定義す
  る。

なお、「ノード」という場合は端点を、「ハンドル」という場合は接ベクトルの逆側の点
にあるものを意味する。

   Two or more Bezier curves can be joined to form a more complex path. The node
   where they are joined may be smooth, indicated by a square (normal) or circle
   (auto-smooth node, see *Auto-smooth Nodes*).

   Or the node may be a corner node, also referred to as a cusp node, indicated
   by a diamond, where an abrupt change in direction is allowed.

Bezier 曲線の結節点のハンドルの形状で smooth なのか corner a.k.a. cusp なのかを
見極められる。もっとも、曲線のつながり具合を画面で見れば一目瞭然だが。

Bezier 曲線は一般には三次曲線だが、次数は下げてもかまわない：

   The segment between two nodes may be a curve or a line. Note that there are
   no control points for line segments.

Creating Paths
======================================================================

   Paths can be created by the *Pencil* (Freehand), *Bezier* (Pen), and
   *Calligraphy* drawing tools. They can also be created by conversion from a
   regular shape or text object.

なお、スタイルは鉛筆と Bezier が一画面画素幅の黒線で描かれる一方、カリグラフィー
はどこかで前述した *Current* スタイルが採用される。

The Pencil Tool
----------------------------------------------------------------------

鉛筆ツールでは単にドラッグで線を引く。次の方法で起動：

* :guilabel:`Toolbox` の鉛筆ボタンをクリックする
* :kbd:`F6` または :kbd:`P` を押す

作図中に :kbd:`Shift` キーを使うと、二つの挙動があり得る：

   Holding down the :kbd:`Shift` key while drawing temporary disables nodes
   snapping to the *Grid* or *Guide Lines*. It also, if a path is selected, add
   the new sub-path to the selected path.

.. admonition:: 利用者ノート

   :kbd:`Alt` キーを押しながらうんぬんの記述を Inkscape 1.2 で再現できない。

引いた線が短いと思ったら、端点から続きを描くことが可能だ：

   As long as a path is selected, you can extend the path by click-dragging from
   one of the path's ends. To prevent adding to a path, deselect the path with
   the :kbd:`Esc` key.

引いている線を捨てたくなったら :kbd:`Esc` を押してキャンセルするといい。

フリーハンドでの曲線作図は表現する形状に対して必要以上に制御点が多くなるの
が通例だ。Inkscape ではそれを間引くコマンドが用意されている：

* :menuselection:`Path --> Simplify` を選択する
* :kbd:`Ctrl` + :kbd:`L` を押す

選択パスが複数あるときには、単純化は二通りの方式が考えられる。

   There are two possible modes for the simplify command. The default is to
   treat all of the selected paths as one object. The second mode is to treat
   each sub-path separately. To use the second mode, add an entry in the
   ``options`` section with ``simplifyindividualpaths`` set to 1 in the
   :file:`preferences.xml` file.

.. admonition:: 利用者ノート

   パスを個別に単純化するのが自然だと考えられる。処理する制御点を決定する要因は
   曲線の形状しかないのだから。連結成分が複数あるパスを考えると、そのほうが有利
   なはずだ。

ここからは鉛筆用のツールバーを見ていく。最初のボタン群は Inkscape 1.2 では次の三
つある：

* :guilabel:`Create regular Bezier path`
* :guilabel:`Create Spiro path`
* :guilabel:`Create BSpline path`

本書では言及されていない B-Spline 曲線を試しに引いてみると、端点以外のハンドルす
べてが制御点となっている。

:guilabel:`Smoothing` は単純化のパラメーターを指定する欄。有効な値は 1 から 100
までだ。大きいほど曲線が滑らかになる。

:guilabel:`Shape` ドロップダウンリストについては次の *Bezier Tool* の節で後述す
る。

   Using the *Pencil Tool*, a high *Smoothness* value is more useful. The width
   can be adjusted by varying the :guilabel:`Width` parameter in the
   :guilabel:`Path Effect Editor` dialog when the path is selected.

鉛筆で点を打てることを知っておく：

   Single dots can be created by using :kbd:`Ctrl` + *Left Mouse Click*. The
   size of the dot can be set in the *Pencil* section of the :guilabel:`Inkscape
   Preferences` dialog as a multiple of the current *Stroke* width. The dot is
   represented in :abbr:`SVG` as a filled path. Adding the :kbd:`Shift` key
   doubles the dot size (and prevents snapping) while adding the :kbd:`Alt`
   creates a random-size dot. The *Bezier Tool* has the same options.

修飾キーで点の寸法を倍々にしていったり、ランダムにしたりすることもできる。

.. admonition:: 利用者ノート

   おそらく後者の用途が打点描法の主と思われる。手描きツールなのだから。

The Bezier (Pen) Tool
----------------------------------------------------------------------

Bezier 曲線の性質により即した操作で作図する。ツール起動例：

* :guilabel:`Toolbox` 上のペンアイコンのあるボタンを押す
* :kbd:`Shift` + :kbd:`F6` を押すか :kbd:`B` を押す

作図中のマウス操作方法は割愛。終わり方だけ確認する：

   To end the path, press :kbd:`Enter` or do a *Right Mouse Click* after placing
   the last Bezier curve end point.

コツ一覧から理解できるものを記しておく：

* 線分を引くにはクリックのみで両端点を打つ。
* 作図中に矢印キーを押すと、直前に打ったノードがその方向に動く。

  * :kbd:`Shift` を押しながらだと通常の十倍移動する。
  * :kbd:`Alt` を押しながらだと画面画素一個分移動する。

* ノードを直前ノードに対して :guilabel:`Rotation snaps every` 角度の倍数で拘束す
  るには :kbd:`Ctrl` を押しながら打つ。
* 制御点をノードに対して :guilabel:`Rotation snaps every` 角度の倍数で拘束するに
  も :kbd:`Ctrl` を押しながら打つ。
* 最後に打ったノードを消すには :kbd:`Backspace` または :kbd:`Del` を押す。
* 作図中にキャンセルするには :kbd:`Esc` を押す。
* 作図中に :kbd:`Shift` + :kbd:`L` を押すと、未完部分曲線から線分に変化する。
* 作図中に :kbd:`Shift` + :kbd:`U` を押すと、未完部分線分が曲線に変化する。
* 作図済みのパスの延長するには、パスを選択して対象端点をクリックするか、さらにド
  ラッグする。
* パスを閉曲線として作図するには、終点定義時に視点をクリックする。

ここからペンツールの *Tool Controls* を見ていく。

:guilabel:`Mode` は次の五つから一つだけを押し込める：

* :guilabel:`Create regular Bezier path`
* :guilabel:`Create Spiro path`
* :guilabel:`Create BSpline path`
* :guilabel:`Create a sequence of straight line segments`
* :guilabel:`Create a sequence of paraxial line segments`

最後のモードは座標軸に平行な線分群を作図する：

   Each line segment is normally drawn perpendicular to the previous segment.
   Holding the :kbd:`Shift` key down allows drawing a segment collinear to the
   previous segment. A path is closed with an L-shaped section, the direction
   can be changed by holding down the :kbd:`Shift` key.

:guilabel:`Shape` ドロップダウンリストでは :guilabel:`None` 以外の項目が選択され
ていると、描画後のパスに形状を適用する。*Single, stretched* モードで *Pattern
Along Path* 効果を使用することに相当する。次章で説明？

.. admonition:: 利用者ノート

   :guilabel:`Scale` 欄は？

ペンツールでも鉛筆ツール同様の操作で点を打つことができるが：

   This works only when in one of the straight line modes.

The Calligraphy Tool
----------------------------------------------------------------------

   As the name suggests, the *Calligraphy Tool* can be used to draw calligraphic
   lines. The resulting paths are different than those drawn with the *Pencil*
   and *Bezier* tools in that they are composed of two parallel (or almost
   parallel) sub-paths, allowing the resulting line to have a variable width.
   The path is not stroked, but the *Fill* is solid

カリグラフィーのパスを描き始めるには次のどれかをする：

* :guilabel:`Toolbox` 内の万年筆ボタンを押す
* :kbd:`Ctrl` + :kbd:`F6` を押すか :kbd:`C` を押す

線の引き方自体は鉛筆ツールと同様。

   The Calligraphy Tutorial (:menuselection:`Help --> Tutorials --> Inkscape:
   Calligraphy`) has many ideas on how to use the *Calligraphy Tool*.

これを実践してから以降の記述を読むのがいいだろう。

Using a Tablet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: 利用者ノート

   タブレットを持っていないので、この節をスキップする。

Hatchings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: 利用者ノート

   やる気が出たら読む。

Paths from Other Objects
----------------------------------------------------------------------

パスを間接的に生成する方法はいくつかある：

1. 通常の図形やテキストをパスに変換する
2. ストロークからパスへの変換で、パスを平行な部分パスからなる閉パスに変換する
3. ビットマップをトレースする

Object to Path
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド実行による。次のどれかで実行される：

* :menuselection:`Path --> Object to Path` を選択
* :kbd:`Shift` + :kbd:`Ctrl` + :kbd:`C` を押す

パスに変換してしまうと、元の型に固有の操作が不能になる：

   Once an object is converted, the object loses any special knowledge
   associated with its previous existence. For example, the text font cannot be
   changed.

テキストからの変換では次のわかりやすい性質がある：

   Converting text to path produces a *Group* of paths with one path for each
   glyph.

Stroke to Path
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A stroked path can be converted to a filled object consisting of two parallel
   sub-paths using :menuselection:`Path --> Stroke to Path` (:kbd:`Ctrl` +
   :kbd:`Alt` + :kbd:`C`). The path should have a non-zero thickness. The before
   and after objects look the same but have different structure and behavior.

本書のうどんの麺の例がわかりやすい。

このコマンドは曲線オフセットに援用できる：

   Simply draw the path you desire, setting the width to the desired gap plus
   the desired final stroke width. Convert the stroke to path, remove the fill,
   and add the stroke paint. The line segments at the ends can be removed if
   desired by selecting each pair of end nodes and using the :guilabel:`Delete
   segment between two non-endpoint nodes` command in the *Node Tool* - *Tool
   Controls* (see next section).

フィレットのある多角形を作図するのにも利用できる：

   The trick is to use a wide *Stroke* and set the :guilabel:`Join` style to
   *Round*.

Editing Paths
======================================================================

Using the Node Tool
----------------------------------------------------------------------

パスを編集するツールは名前が三つ挙げられる：

   Paths are normally edited using the *Node Tool*. This flexible tool enables
   the addition, deletion, and movement of nodes. A *Sculpting* mode allows easy
   fine tuning of paths with many nodes. *Auto-smooth* nodes enable nodes to be
   moved while maintaining smooth curves.

*Node Tool* の起動方法：

* :guilabel:`Toolbox` の :guilabel:`Edit paths by nodes` ボタンを押す
* :kbd:`F2` または :kbd:`N` を押す

ツールが起動してからパスをクリックするなどして選択すると、対象ノードすべてが表示
される。

ノード操作はオブジェクト操作と同じ感覚で行える：

   Many of the things you can do with objects, you can do with nodes using the
   same methods. This is especially true for selecting and moving nodes. For
   example, the *Arrow* keys move selected objects by the :guilabel:`Nudge
   factor` when the *Select Tool* is active; they move selected nodes by the
   :guilabel:`Nudge factor` when the *Node Tool* is active.

.. admonition:: 読者ノート

   本文中で :guilabel:`Nudge factor` とあるところはすべて :guilabel:`Arrow keys
   move by` と読み換えるといい。

Selecting Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ノード（□か◇）を選択すると、その接線ハンドルはもちろん、隣接ノードの接線ハンドル
も示される。これが邪魔であるようなら、ツールバーの :guilabel:`Show Bezier
handles of selected nodes` ボタンを出っ張らせておく。

ノードを選択するには左クリックを絡める：

* 直接左クリックすると、当該ノードが選択される。
* ノード上でマウスポインターをホバーすると赤く強調表示されて、選択（または解除）
  する。
* ノードをクリックドラッグすると、ノードの選択と移動をいっぺんに行う。

ノードではなくパスを左クリックする場合もある：

.. admonition:: 読者ノート

   この記述は正確にはパスではなく、その凸包線であると考えられる。以下、本書の記
   述を適宜修正して記す。

* クリックした場所の両脇にある最も近いノードが選択される。
* クリック可能なパスの上にマウスをホバーすると、ポインターが方向マークに変わる。
* 凸包線上をクリックドラッグすることで、パスを調整することができる。この場合、隣
  接ノードは選択されない。

左ボタンドラッグは、ラバーバンド範囲内のノードすべてを選択する。

* :kbd:`Shift` キーを使用しない限り、ドラッグはパス上で開始してはいけない。
* :kbd:`Shift` キーを使用すると、ノードの上でなくてもドラッグを開始することがで
  きる。

   Nodes can be added (or removed) from the selection by holding down the
   :kbd:`Shift` key while using one of the previous methods.

マウスホイールや :kbd:`PgUp` / :kbd:`PgDn` で面白いノード選択操作ができる：

   Nodes can also be added to or removed from the selection by hovering the
   cursor over a node and using the *Mouse Wheel*, moving “up” to add nodes and
   “down” to remove nodes. The Page Up and Page Down keys can be used in place
   of the *Mouse Wheel*

この up/down ノード候補は二通りあり得る。マウスポインターからの距離順か、ノード
曲線に沿った距離順だ。このモードは :kbd:`Ctrl` キーで切り替える。

:kbd:`Tab` は巡回的にノードを選択していく：

   :kbd:`Tab` selects the next node in a path if one is already selected. This
   is usually the adjacent node in the direction the path was drawn. If no node
   is selected, it will select the first node. :kbd:`Shift` + :kbd:`Tab` will
   select the previous node in a path.

選択パスのノード全選択、選択反転はキー操作で可能：

  :kbd:`Ctrl` + :kbd:`A` selects all nodes in a selected path. :kbd:`!` inverts
  the node selection for any sub-path with at least one node selected.
  :kbd:`Alt` + :kbd:`!` inverts the node selection for the entire path (or
  paths).

Editing Nodes with the Mouse
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   The mouse can be used to move nodes and handles by dragging them. It can also
   be used to alter the shape of a path between two nodes by dragging the path.
   And finally, nodes can be inserted anywhere along a path by double-clicking
   the path or by clicking the path while holding down the :kbd:`Ctrl` +
   :kbd:`Alt` keys.

Nodes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

左ボタンドラッグ
   選択したノードを移動。ドラッグが始まるのが選択ノード上か非選択ノード上かで移
   動様式が異なる。前者ならば選択ノードすべてが移動し、後者ならばポインター位置
   のノードが選択されてからそれが移動する。
:kbd:`Ctrl` + 左ボタンドラッグ
   選択ノードを水平方向または垂直方向に移動する。
:kbd:`Ctrl` + :kbd:`Alt` + 左ボタンドラッグ
   選択ノードをハンドルと平行な線または垂直線に沿って移動する。ただし、ポイン
   ターがドラッグを開始したノードに属するハンドルに基づく。

   .. admonition:: 利用者ノート

      この操作が確認できない。

:kbd:`Shift` + 左ボタンドラッグ
   グリッドやガイド線に対してノードがスナップするのを一時的に無効にする。

Handles
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

接線ベクトルの端点に画面上○で示されるのがハンドルだ。

   A handle becomes active when the mouse hovers over its control point. The
   control point will turn red.

左ボタンドラッグ
   ハンドルを移動する。
:kbd:`Shift` + 左ボタンドラッグ
   ハンドルとその反対のハンドルを同時に回転する（両ハンドルとノードが直線上にあ
   る）。
:kbd:`Ctrl` + 左ボタンドラッグ
   ハンドルを次のいずれかにスナップする：

   * :guilabel:`Rotate snaps every` 度の倍数だけ回転スナップ（いつもの）
   * 元のハンドル方向の直線上
   * 元のハンドル方向と直交する直線上
   * 反対のハンドル方向と直交する直線上

   .. admonition:: 読者ノート

      一部確認できない。

:kbd:`Alt` + :kbd:`Ctrl` + 左ボタンドラッグ
   接ベクトルの長さは固定し、角度しか変化しないようにする。

Editing Nodes with the Keyboard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   The keyboard can also be used to add and delete nodes, change the type of
   node, and to join or break paths.

キーボードには :kbd:`Ctrl` と :kbd:`Alt` が二つずつあるはずだが、Inkscape のノー
ド操作ではこれらを区別することがある：

   In this section, :kbd:`Left-` and :kbd:`Right-` applied to the :kbd:`Ctrl`
   and :kbd:`Alt` modifying keys refers to the keys on the left and right side
   of the :kbd:`Space` bar. Using a left modifying key causes the left handle of
   a node to be modified; using a right modifying key modifies the rightmost
   handle. The definition of which handle is left or right is not always
   completely obvious as when one handle is directly above the other or when the
   leftmost handle is moved to the right of the former rightmost handle.

両者が垂直に並んでいない限りは問題ないだろう。本ノートでは修飾キーに対する左と右
の記載を紛らわしくない限り省く。アプリケーション上の操作は区別して理解すること。

   The scaling and rotating operations described below are different if one node
   is selected as compared to two or more nodes. If two or more nodes are
   selected, the nodes act like an object and scale or rotate around the center
   of the selection, -略- If the mouse is over a node, then that node is used as
   the center of rotation. It is also possible to flip the nodes horizontally
   and vertically by using keyboard shortcuts.

Translations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

オブジェクトに対するキー操作と同じ。オブジェクトの代わりにノードに作用す
る。:kbd:`Alt` キーは画素単位指示のためでしかないので、移動操作時には左右の区別
なし。

Scaling Handles
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

接ベクトルを伸縮するキー操作がある。

   These items only apply when one node is selected.

紙幅の都合上、延長操作だけ記す：

:kbd:`.` or :kbd:`>`
   選択ノードの両側のハンドルを :guilabel:`> and < scale by` の値だけ伸ばす（既
   定値は 2 :abbr:`SVG` 画素）。
:kbd:`Ctrl` + :kbd:`.` or :kbd:`Ctrl` + :kbd:`>`
   選択ノードの片側にあるハンドルを :guilabel:`> and < scale by` の値だけ伸ば
   す。
:kbd:`Alt` + :kbd:`.` or :kbd:`Alt` + :kbd:`>`
   選択ノードの片側にあるハンドルを画面画素一つ分だけ伸ばす。

ベクトルを縮めるには :kbd:`.` or :kbd:`>` の代わりに :kbd:`,` or :kbd:`<` を押
す。同じ名前の修飾キーは二つあるので、それで左側か右側かを区別する。

Rotating Handles
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

これらの回転操作も前節の操作方法同様、ノードがただ一つだけ選択されているときにし
か適用されない。紙幅の都合上、左回転だけ示す：

:kbd:`[`
   選択ノードのハンドルを左回りに :guilabel:`Rotaion snaps every` 角度だけ回転す
   る。
:kbd:`Ctrl` + :kbd:`[`
   選択ノードの片側にあるハンドルを左回りに :guilabel:`Rotaion snaps every` 角度
   だけ回転する。角ノード専用。
:kbd:`Alt` + :kbd:`[`
   選択ノードの片側にあるハンドルを左回りに画面画素一つ分だけ回転する。

右回転の場合は :kbd:`[` の代わりに :kbd:`]` を押す。修飾キーの関する注意は伸縮時
と同様。

Using the Node Tool-Tool Controls
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   The *Node Tool*-*Tool Controls* provides an easy way to access many of the
   methods of editing nodes.

これも本書の記述と 1.2 とで違いがあるようだ。最初の区画から見ていく。

:guilabel:`Insert new nodes into selected segments`, :kbd:`Ins`
   ノードをパス断片上に追加する。パス断片の選択方法だが、そもそもパスをクリック
   するとその位置に最も近いパス上の点を含むパス断片が、その両端ノードを選択状態
   にすることで論理的に選択されると考えていい。

   パスをダブルクリックするか、:kbd:`Ctrl` + :kbd:`Alt` を押しつつパスをクリック
   することでも、ノードを追加する。

   ノード追加では、隣接ノードのハンドルを調整してパスの形状をなるべく維持する。

ボタン右の三角形
   これをクリックすると、ノード追加サブメニューが表示される：

   * :menuselection:`Insert node at min X`
   * :menuselection:`Insert node at max X`
   * :menuselection:`Insert node at min Y`
   * :menuselection:`Insert node at max Y`

   項目名の示すパス断片上の位置にノードを追加する。

:guilabel:`Delete selected nodes`, :kbd:`Backspace`, :kbd:`Del`, :kbd:`Ctrl` + :kbd:`Alt` + 左ボタンクリック
   ノード削除では、隣接ノードのハンドルを調整してパスの形状がなるべく維持され
   る。この調整を防ぐには :kbd:`Ctrl` を押しながら :kbd:`Backspace` or
   :kbd:`Del` を押す。

----

:guilabel:`Join selected endnodes`, :kbd:`Shift` + :kbd:`J`
   通常、マージされたノードは、両端点の中点に配置される。ショートカットキーで
   は、マウスを端点の一つに合わせると、マージされたノードはその位置に配置され
   る。複数の端点が選択されている場合の挙動は次のように述べられている：

      If more than two end nodes are selected, pairs of end nodes will be
      merged, starting with the end nodes closest to each other until either
      zero or one end nodes are selected. If zero or one end node is selected at
      the start, then any adjacent stretches of selected nodes (including
      non-end nodes), will be merged into one node.

:guilabel:`Break path at selected nodes`, :guilabel:`Shift` + :guilabel:`B`
   選択ノードそれぞれが相異なるパス断片の端点二つに変換される。

----

:guilabel:`Join selected endnodes with a new segment`
   端点が二つ以上選択された場合、端点のペアが端点が 0または 1 個に処理されるま
   で、互いに最も近い端点から始めて断片で結合される。

   開始時に 0 または 1 個の端点が選択されている場合、選択ノードの隣接伸び具合
   （非終端含む）は、中点が削除され、最も外側の選択ノード間に断片一つが残され
   る。

:guilabel:`Delete segment between two non-endpoint nodes`
   非端点間のパス断片を削除する。パスの連結成分が増える。

----

:guilabel:`Make selected nodes corner`, :kbd:`Shift` + :kbd:`C`
   ノードがすでに尖点であるならば、そのハンドルは両方とも引っ込んでいる。
:guilabel:`Make selected nodes smooth`, :kbd:`Shift` + :kbd:`S`
   ショートカットキー押しのほうがポインター位置を使える分有利だ：

      When the keyboard shortcut is used, placing the mouse over a handle will
      preserve the position of that handle, rotating the partner handle, if
      extended, to be collinear.

   両側接ベクトルが同じ方向、同じ大きさに調整するのが主旨だ：

      If the partner handle is not extended, the partner handle will be extended
      so that it is collinear and of the same length as the preserved handle. If
      the node is next to one straight line segment (the other segment being
      curved) and the opposite handle is not collinear with the segment, the
      keyboard shortcut will rotate it to be collinear, extending the handle if
      necessary.

:guilabel:`Make selected nodes symmetric`, :kbd:`Shift` + :kbd:`Y`
   ノード自体に対称属性みたいなものが付与されるようで、以後のハンドル操作では相
   方ハンドルが対称的に変化する。

:guilabel:`Make selected nodes auto-smooth nodes`, :kbd:`Shift` + :kbd:`A`
   自動平滑ノードについては後述。

----

:guilabel:`Make selected segments lines`, :kbd:`Shift` + :kbd:`L`
   伸びているハンドルが引っ込む。
:guilabel:`Make selected segments curves`, :kbd:`Shift` + :kbd:`U`
   断片は直線のままで、曲率を変えられるようにハンドルは伸びている。

----

:guilabel:`Convert selected objects to paths`, :kbd:`Shift` + :kbd:`Ctrl` + :kbd:`C`
   :menuselection:`Path --> Object to Path` と同じ。
:guilabel:`Convert selected object's stroke to paths`, :kbd:`Ctrl` + :kbd:`Alt` + :kbd:`C`
   :menuselection:`Path --> Stroke to Path` と同じ。

----

ノード座標コントロールは見れくれどおりの機能。

----

:guilabel:`Show clipping paths of selected objects`
   クリップパスを編集可能にする。クリップパスとオブジェクトは同時に編集可能（ク
   リップパスが実際のパスである場合のみ）。
:guilabel:`Show masks paths of selected objects`
   マスクパスを編集可能にする。パスは青色で表示される。マスクパスとオブジェク
   トは同時に編集可能（マスクパスが実際のパスである場合のみ）。
:guilabel:`Show next editable path effect parameter`, :kbd:`F7`
   LPE のパラメータリストをトグルします。

----

:guilabel:`Show transformation handles of selected nodes`
   座標変換用の BB の表示オンオフ。
:guilabel:`Show Bezier handles of selected nodes`
   ハンドルの表示と非表示を切り替える。
:guilabel:`Show path outline (without path effect)`
   パスの輪郭を表示する。パスの一部がクリップまたはマスクされている場合（緑のパ
   ス）、またはパスに LPE が適用されている場合（赤のパス）に便利。

Editing Nodes with the Align and Distribute Dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:menuselection:`Object --> Align and Distribute` で表示される :guilabel:`Align
and Distribute` ダイアログには *Node Tool* 使用時には UI が特別になる。ここのコ
マンドは、選択ノードを整列または分配させるもので、線上にマーカーを均等に配置する
のに便利だ。

:guilabel:`Align selected nodes along a horizontal line`
:guilabel:`Align selected nodes along a vertical line`
:guilabel:`Distribute selected nodes horizontally`
:guilabel:`Distribute selected nodes vertically`

最初の二つについては :guilabel:`Relative to` オプションが指定可能：

* :guilabel:`Last selected`
* :guilabel:`First selected`
* :guilabel:`Middle selected`
* :guilabel:`Min value`
* :guilabel:`Max value`

Auto-Smooth Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

自動平滑ノードの定義：

   An auto-smooth node is a special node that will automatically adjust to
   maintain a smooth path when it or one of its neighboring nodes are moved.

ノードを自動平滑ノードに指定する方法：

   To create auto-smooth nodes, select the nodes and either use the keyboard
   shortcut :kbd:`Shift` + :kbd:`A` or click on the icon in the *Tool Controls*.

自動平滑ノードをただの平滑ノードに戻す方法がある。不意に戻ることはないようだ：

   Auto-smooth nodes revert to normal smooth nodes if their handles are
   explicitly adjusted or if the path is dragged on either side of the node.

自動平滑ノードは、対応する接ベクトルが一定の距離や角度内に収まるように振る舞う：

   Auto-smooth nodes work by adjustments to the length and direction of the
   node's handles. The length of the handles are kept about one-third of the
   distance to the neighboring nodes, and the change in direction is a function
   of the relative position of the neighboring nodes.

Sculpting Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

塑像モードでは複数ノードを一斉に調整するという特徴がある。複数ノードを選択してか
ら、そのうちの一つをドラッグすることで塑像を実現するという理解でいいだろう：

   The *Sculpting* mode of the *Node Tool* allows one to easily manipulate a
   complex path, adjusting multiple nodes at the same time. The basic use is to
   select a group of nodes and then drag one of the selected nodes with the
   mouse while holding down the :kbd:`Alt` key. Only the dragged node moves the
   full amount.

ノードの移動量はグループの端に行けば行くほど少なく、端のものは不動だ。正規分布を
想像していい：

   The selected nodes at the end remain fixed, and all the other selected nodes
   will move a distance that is a function of how far they are from the dragged
   node. The function takes the form of a *Bell Curve* distribution.

.. admonition:: 読者ノート

   この鐘曲線のイラストを自分で作図して再現するとノード操作の練習にもなる。

Path Offset Commands
----------------------------------------------------------------------

オフセットは意外に単純な手段で実現されている：

   Each allows a path to be enlarged or reduced by moving each point
   perpendicular to a line tangent to the path at that point.

図形やテキストをオフセットするのに、手動でパスに変換する必要はない：

   A regular shape or text object is converted to a path automatically, except
   for the *Linked offset* command.

オフセット曲線はなぜか閉曲線だ。

   The new paths are all closed, even if the original is open.

オフセットコマンドは :menuselection:`Path` メニューの中程にある：

:menuselection:`Path --> Inset`, :kbd:`Ctrl` + :kbd:`9`
   パスを内側に画素二つ分だけ動かす。
:menuselection:`Path --> Outset`, :kbd:`Ctrl` + :kbd:`0`
   パスを外側に画素二つ分だけ動かす。

   .. admonition:: 読者ノート

      キーバインドが本書と異なる。私の Inkscape の挙動に合わせる。

:menuselection:`Path --> Dynamic Offset`, :kbd:`Ctrl` + :kbd:`J`
   パスを内側または外側に動かす。

   * *Node Tool* がある状態で表示されるハンドルでオフセットの大きさを制御する。
   * 元のパスは保存される。オフセットを変更してもパスは劣化しない。
   * 元のパスは変換後は編集不可。編集するには、:menuselection:`Path --> Object
     to Path` (:kbd:`Shift` + :kbd:`Ctrl` + :kbd:`C`) で、オフセットパスを通常の
     パスに変換すればいい。

:menuselection:`Path --> Linked Offset`, :kbd:`Ctrl` + :kbd:`Alt` + :kbd:`J`
   パスを複製し、拡大または縮小する。ハンドルでオフセットの大きさを制御する。

   * 元のオブジェクトはパスに変換されず、編集可能なまま。
   * 変更はオフセットパスに反映される。
   * *Linked Offset* パスは複数作成可能。

Miscellaneous Path Commands
----------------------------------------------------------------------

   The commands have in common that they act on the entire path, and not on a
   subset of a path's nodes.

:menuselection:`Path --> Combine`, :kbd:`Ctrl` + :kbd:`K`
   選択パスを複合パスに結合する。グループ内のパス配置に関係なく、どのよ
   うなパスの集合に対しても機能する。

   ということは、結合というか、和集合を形成するコマンドだ。
:menuselection:`Path --> Break Apart`, :kbd:`Shift` + :kbd:`Ctrl` + :kbd:`K`
   選択複合パスを単純パスに分解する。

----

:menuselection:`Path --> Simplify`, :kbd:`Ctrl` + :kbd:`L`
   パスの形状をほぼそのままに、ノード数を減らす。

   * 選択範囲が広いほど、より大胆に簡略化される。
   * 反復実行可能。設定時間 (0.5s) 以内に繰り返すと、単純化もより大胆になる。
   * 単純化の閾値は :guilabel:`Inkscape Preferences` ダイアログの
     :menuselection:`Behavior --> Simplification threshold` で変更することが可
     能。

:menuselection:`Path --> Reverse`, :kbd:`Shift` + :kbd:`R`
   ショートカットキーが機能するのは *Node Tool* 有効時のみ。

   パスの方向を逆にすると、:kbd:`Tab` でノードを選択する順番やマーカー（矢印な
   ど）の方向などに影響する。

Path Operations
======================================================================

複数パスから新しいパスを作成するようなコマンドがたくさんあるうち、ここでは
z-order が重要なものを見ていく。

   In all cases except for the *Cut Path* command, the *Fill* and *Stroke* of
   the new path is inherited from the bottom path. For some operations, the top
   path can be thought of as operating on the bottom path; that is, part of the
   bottom path remains and the top path is thrown away.

「天井が消えて底が残る」が原則だ。例えば見てくれは底のパスのものを引き継ぐ。

:menuselection:`Path --> Union`, :kbd:`Ctrl` + :kbd:`+`
   元のパスすべての領域を含む、新しいパスを作成する。

      A union of one path removes self-intersections, creating individual
      sub-paths for each section.

:menuselection:`Path -->Difference`, :kbd:`Ctrl` + :kbd:`-`
   パス二つの差を取る。天井パスにしかない領域が底パスから消去される。
:menuselection:`Path -->Intersection`, :kbd:`Ctrl` + :kbd:`*`
   パスすべてが交差する領域を取る。
:menuselection:`Path -->Exclusion`, :kbd:`Ctrl` + :kbd:`^`
   パスを排他的に消去する。複数の部分パスからなる単一の新しいパスを作成する。こ
   のパス計算は *Even-Odd Fill* 規則に基づく。
:menuselection:`Path -->Division`, :kbd:`Ctrl` + :kbd:`/`
   パス二つの分割。第一パスが第二パスによって分割される。新しいパスが複数生成す
   る。
:menuselection:`Path -->Cut Path`, :kbd:`Ctrl` + :kbd:`Alt` + :kbd:`/`
   分割ではなく切断をする。新しいパスは塗りつぶしを持たない。
