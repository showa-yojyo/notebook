======================================================================
Chapter 10. Attributes
======================================================================

.. contents::

章見出しは Attributes と大きく構えているが、実際は塗りつぶしと筆跡だ。

   An object has attributes such as color and line style. An attribute can apply
   to the *Fill* or to the *Stroke* of the object. The *Fill* refers to how the
   area inside an object's boundary path is painted while the *Stroke* refers to
   the path itself. The *Fill* or *Stroke* (*Stroke* paint) can be a single
   color, a *Gradient* of colors, a *Pattern*, or nothing at all. With the
   exception of a few small differences, *Fill* and *Stroke* paint have the same
   properties and are treated together in the following discussion.

テキストに関しては事情が若干異なる。色は各文字に設定できる。

   Text can be given the same attributes as other objects with a few small
   differences: Individual letters, words, or phrases can be given different
   solid colors, but *Gradients* and *Patterns* must be assigned to an entire
   text object.

Inkscape はオブジェクトに属性を与える手段をいくつも用意している。

:guilabel:`Fill and Stroke` ダイアログ
   :menuselection:`Object --> Fill and Stroke` または :kbd:`Shift` + :kbd:`Ctrl`
   + :kbd:`F` で出現。

      Three tabs in the dialog allow the setting of the *Fill*, *Stroke paint*,
      and *Stroke style*. At the very bottom of the dialog is a slider and entry
      box for the *Opacity* to set the overall opacity (or transparency) of an
      object.

:guilabel:`Palette`
   :menuselection:`View --> Show/Hide --> Palette` または :kbd:`Shift` +
   :kbd:`Alt` + :kbd:`P` で UI 表示を切り替える。

   * クリックで *Fill* を変更。
   * :kbd:`Shift` + クリックで *Stroke paint* を変更。

:guilabel:`Swatches` ダイアログ
   :menuselection:`View --> Swatches...` または :kbd:`Shift` + :kbd:`Ctrl` +
   :kbd:`W` で出現。

   :guilabel:`Palette` と同様にしてオブジェクトの色を指定する。

*Style Indicator* メニュー
   ステータスバー左の :guilabel:`Fill`, :guilabel:`Stroke` ラベルの右側を
   右クリックするとメニューが何か表示される。

*Color Gestures* と *Stroke Width Gestures*
   *Style Indicator* から左ボタンドラッグで色味が動的に変わるようだ。

*Dropper Tool*
   他のオブジェクトから *Fill* と *Stroke paint* をピックする。この手のソフトに
   よくあるスポイトツールだ。

*Gradient Tool*
   グラデーションを作成したり編集したりする。

:menuselection:`Edit --> Paste Style` (:kbd:`Shift` + :kbd:`Ctrl` + :kbd:`V`)
   別のオブジェクトの属性を適用する。元オブジェクトは :menuselection:`Edit -->
   Copy` (:kbd:`Ctrl` + :kbd:`C`) でクリップボードに複製してから、対象オブジェク
   トを選択してこのコマンドを使う。

XML Editor
   属性を編集するというよりは、:abbr:`SVG` 標準に定義されているが、Inkscape UI
   で直接アクセスできない属性に便利だ。

Fill and Stroke Paint
======================================================================

   The use of these options for the *Fill* and the *Stroke paint* is basically
   the same, so we'll use the word fill to talk about both at the same time.

:guilabel:`Fill and Stroke` ダイアログの :guilabel:`Fill` タブおよび
:guilabel:`Stroke paint` タブの下にある UI を見ていく。タブの真下にあるアイコン
列を左から列挙すると：

.. csv-table::
   :delim: |
   :header-rows: 1
   :widths: auto

   ボタン | 塗り
   :guilabel:`No paint` | 透明
   :guilabel:`Flat` | ベタ塗り
   :guilabel:`Linear Gradient` | 線形グラデーション
   :guilabel:`Radial Gradient` | 放射状グラデーション
   :guilabel:`Mesh Gradient` | OpenGL のようなグラデーション？
   :guilabel:`Pattern` | 反復するパターンで埋め尽くす
   :guilabel:`Custom Swatch` | 文書依存の swatch
   :guilabel:`Unset paint` | 未設定にする

グラデーションは *Gradient Tool* でも取り扱われる。

Flat (Solid) Colors
----------------------------------------------------------------------

Inkscape は色を ``#RRGGBB`` または ``#RRGGBBAA`` の形式で内部的に取り扱う。

   Inkscape supports base ICC profile functionality through the use of
   LittleCMS_. Setting up color management can be done under the
   :guilabel:`Color` management section in the :guilabel:`Inkscape Preferences`
   dialog. You can declare multiple ICC profiles for a document in the
   :guilabel:`Color Management` tab of the :guilabel:`Document Properties`
   dialog. If everything is setup properly the “Color Managed View” can be
   toggled on/off via :menuselection:`View --> Color-managed View` or by
   clicking on the icon in the lower right corner of the window.

上級者向けの ICC プロファイル機能というものがあるが、深く立ち入らない。

Fill and Stroke Dialog—Color
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   When the use of a flat (or solid) color is specified for the *Fill* and
   *Stroke paint* of an object, the corresponding tab of the :guilabel:`Fill and
   Stroke` dialog will show five sub-tabs, each one corresponding to a different
   method of specifying the color plus one for color management.

文の後半の意味がまだわからないが先に進む。

ホイールコントロールではない方の色成分指定 UI の記述だ：

   Except for the :guilabel:`Wheel` tab, each color parameter can be set by
   either dragging a slider (small triangles), typing the desired value into the
   entry box, using the up/down arrows in the widget (*Right Mouse Click* on an
   arrow causes the value to change to the minimum or maximum, *Middle Mouse
   Click* cause the value to increment or decrement by 10), or the
   :kbd:`Up`/:kbd:`Down` Arrow keys after the entry box is selected. The slider
   bar shows the current value (triangles) and what the color will look like as
   that slider is dragged.

第四成分、アルファー値は 0 ほど透明に近い：

   The A or *Alpha* attribute specifies how transparent the fill should be, 0
   for completely transparent and 255 (100) for completely opaque in the case of
   the :abbr:`RGB`, :abbr:`HSL`, and *Wheel* (:abbr:`CMYK`) methods.

RGB
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

これはさすがにノート不要。

   This is the native method for computer screens.

HSL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   :abbr:`HSL` (Hue, Saturation, Lightness) is a method for specifying color in
   terms of hue (color in optical spectrum), saturation (intensity-purity), and
   lightness. The range for saturation is from a pure color to gray. The range
   for lightness is from black to pure color to white.

:abbr:`HSL` は虹色を作るときに便利な色モデルだ。

.. admonition:: 利用者ノート

   Inkscape 1.2 では :abbr:`HSV` も利用可能。

CMYK
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:abbr:`CMYK` は減色法に基づく印刷用色モデルだ。次が囲み記事で注意されている：

   Inkscape stores color internally in the :abbr:`RGB` format. This is the only
   color specification supported by :abbr:`SVG`. Furthermore, the entry boxes
   are set up so that the value in one is always zero. (Any color in :abbr:`RGB`
   color space can be defined using only three of the :abbr:`CMYK` terms. The
   definition is not unique.)

Wheel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

本節の記述はおそらく現行バージョンの :abbr:`HSL` モードに吸収されている。
:guilabel:`Color Wheel` ボタンでこの UI の表示を切り替える。

次の記述はその UI のそれとしてはなお有効のようだ：

   Dragging the line around the circle changes the *Hue*. Dragging the small
   circle within the triangle parallel to the edge that varies from white to
   black changes the *Lightness* and dragging perpendicular to that edge changes
   the *Saturation*.

○マーカーを底辺上またはその垂線上に沿ってドラッグすると、色成分コントロールの
:guilabel:`L` や :guilabel:`S` が変化することが確認できる。

CMS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   This tab allows editing of colors managed by an icc profile if enabled.

それゆえ、既定設定だと ``<none>`` しか一覧にない。

Palette and Swatches Dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Swatches` ダイアログを表示するには：

* メニュー :menuselection:`View --> Swatches...`
* キーバインド :kbd:`Shift` + :kbd:`Ctrl` + :kbd:`W`

*Palette* の表示を切り替えるのは

* :menuselection:`View --> Show/Hide --> Palette`
* キーバインド :kbd:`Shift` + :kbd:`Alt` + :kbd:`P`

次のマウス操作が *Palette* と *Swatches* で有効：

* 左クリックすると、選択オブジェクトまたは選択グラデーション止の色を変える。
* :kbd:`Shift` + 左クリックすると、選択オブジェクトの描線色を変える。現在色も変
  わる（オブジェクト選択は不要）。
* 左ボタンドラッグをオブジェクトの *Fill*, *Stroke*, グラデーション止のどれかへ
  行うと、それが swatch 色に変わる。
* :kbd:`Shift` + 左ボタンドラッグをオブジェクトの任意の場所にすると *Stroke* 色
  を設定する（オブジェクト選択は不要）。現在色はそのまま。
* 右クリックすると、小さなダイアログが開き、選択オブジェクトの *Fill* または
  *Stroke* に swatch 色を割り当てる。現在色も変わる。

  操作しているのがカスタムスウォッチならば、swatch 色を編集または削除することも
  できる。

パレットの自作を設定ファイルから行うこともできる。詳細は別の章で述べられる：

   Inkscape has a variety of built-in palettes (some copied from Gimp). More
   palettes can be added by installing palette files in the directory
   :file:`share/palettes`. The files use the Gimp palette file structure where
   colors are defined in terms of a triplet of numbers in a :abbr:`RGB` format.

*Palette* と *Swatches* の隅にある▲▼アイコンとハンバーガーアイコンは便利だ：

   Both the *Palette* and the :guilabel:`Swatches` dialog have a pull-down menu
   (far right, small arrow) where you can set the size and shape of the
   swatches, if the colors should be displayed in one row or in multiple rows,
   and which palette should be used. Hovering the pointer over a swatch will
   display a color's name in a tool tip and in the *Status Bar*. A scroll bar
   gives access to colors in a palette that are not displayed when there are too
   many colors to fit.

Style Indicator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Style Indicator* とはステータスバーの左にある選択オブジェクトなどの情報表示領域
を言う：

   The *Style Indicator* located on the left side of the *Status Bar* displays
   information on selected objects, text fragments, or *Gradient* stops. The
   indicator includes a number of methods to alter style, including: pop-up
   menus, targets for *Drag and Drop* colors, and *Color Gestures*.

Display
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   The *Style Indicator* has three parts showing :guilabel:`Fill`,
   :guilabel:`Stroke` paint, and opacity (:guilabel:`O`), which show attributes
   for selected objects or text fragments. The :guilabel:`Fill` and
   :guilabel:`Stroke` paint parts are referred to as the *fill indicators*.

:guilabel:`Fill:` 矩形の内容と意味は次のとおり：

.. csv-table::
   :delim: |
   :header-rows: 1
   :widths: auto

   表示 | 意味
   実際の色 | 左側と右側がそれぞれアルファーなしありの色
   :guilabel:`N/A` | オブジェクトが選択されていない
   :guilabel:`None` | 定義されている塗りつぶしがない
   :guilabel:`Unset` | 塗りつぶしが未設定
   :guilabel:`L` | 線形グラデーション
   :guilabel:`R` | 放射グラデーション
   :guilabel:`Pattern` | 塗りつぶしはパターンである
   :guilabel:`≠` | オブジェクトが複数選択されていて異なる塗りつぶしである

オブジェクトが複数選択されていて、すべてに塗りつぶしが定義されている場合、次のよ
うな表示になる：

.. csv-table::
   :delim: |
   :header-rows: 1
   :widths: auto

   表示 | 意味
   :guilabel:`m` | すべてが同じ塗りつぶし色だ
   :guilabel:`a` | 異なる塗りつぶし色がある（平均色を表示）

*Style Indicator* は三部分それぞれに固有の機能がある。

*Fill Indicator*
   * 左クリックで :guilabel:`Fill and Stroke` ダイアログ :guilabel:`Fill` タブを
     開く。
   * 中クリックで、選択オブジェクトの塗りを定義されている場合は削除、そうでない
     場合は黒に設定。
   * 右クリックで *Fill* 操作コマンドからなるポップアップメニューを開く。
*Stroke indicator*
   * 左クリックで :guilabel:`Fill and Stroke` ダイアログ :guilabel:`Stroke
     paint` タブを開く。
   * 右クリックで *Stroke paint* 操作コマンドからなるポップアップメニューを開
     く。
*Opacity*
   * 数値欄を右クリックで 25% 刻みのプリセット値からなるポップアップメニューを表
     示する。
   * :guilabel:`O` ラベルを中クリックすると、0%, 50%, 100% の値を循環する。

Fill Indicator Pop-up Menu
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

上で「操作コマンドからなるポップアップメニュー」と記したものの説明。*Fill* 版と
*Stroke paint* 版はそっくりなので、片方を理解すれば十分だろう。

Color Gestures
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

この機能をどう活用していいのかわからない。

   *Color Gestures* is the name given to changing the color of a *Fill*,
   *Stroke*, or *Gradient Stop* by dragging the mouse from a fill indicator into
   the Inkscape window.

マウス操作が独特だ：

   The principle is that as you drag the mouse, the color will change
   proportionally to the distance from a 45° line from the indicator. The
   farther away you are, the more subtle the changes can be. Changes are made in
   the :abbr:`HSL` color space.

:abbr:`HSL` モデルは極座標に基づくものだからこういう動作を考案したのだろうか。

* :kbd:`Shift` を押しながらドラッグすると彩度が変化。
* :kbd:`Ctrl` を押しながらドラッグすると明度が変化。

   When a key modifier is changed, the “zero” line (normally at 45°) changes to
   pass through the current cursor position. This is to avoid abrupt changes in
   color when changing modifiers. The :kbd:`Alt` modifier disables changes to
   the color so that the cursor can be repositioned.

そんな細やかなマウス捌きはできない。

念のために複数オブジェクトやグラデーション選択時の挙動について述べられている：

   If more than one object or *Gradient Stop* is selected, the starting color
   will be the average color of the selected items and the final color will be
   the same. If you wish to shift the color in the same way for a number of
   objects but preserve the relative differences use the *Tweak Tool*.

Dropper Tool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

この手のソフトによくあるスポイトツールだ。

   The *Fill* and *Stroke paint* color of an object can be changed by using the
   *Dropper Tool* to grab an existing color in the drawing. Options allow for
   grabbing the average color over a circular region, inverting the grabbed
   color, and saving the grabbed color to the system clipboard (as a
   :abbr:`RGBA` hexadecimal number).

スポイトツールは選択ツールと反復して使うことになるので、この操作を習得しておく：

   To use the *Dropper Tool*, first select the object that you want to modify
   with a tool other than the *Dropper Tool*. Recall that you can switch
   temporarily to the *Select Tool* by using the :kbd:`Space` Bar.

   Then select the *Dropper Tool* by clicking on the icon (:kbd:`F7` or
   :kbd:`D`) in the *Tool Controls*. Finally click with the *Dropper Tool* on
   the desired color. The shortcut :kbd:`D` will toggle between the *Dropper
   Tool* and any other tool.

例によって修飾キーと絡める操作もある：

   The :kbd:`Shift` causes the chosen color to be applied to the object's
   *Stroke paint* rather than the *Fill*. The :kbd:`Alt` causes the inverse
   color to be applied. The :kbd:`Shift` and :kbd:`Alt` keys can be used in
   combination.

反転色というのは文字通りで、例えば桃色をスポイトすると緑を取れる。

左クリック
   *Fill* 色を採取する。
左ボタンドラッグ
   ドラッグ中にできた円の *Fill* 色を採取した平均値を得る。
:kbd:`Ctrl` + :kbd:`C`
   ポインター下の色を 8 桁の 16 進数 rrggbbaa 形式でシステムクリップボードにコ
   ピーする。

*Dropper Tool* のツールバーにはラジオボタンが二つあるだけだ。

   The *Dropper Tool* *Tool Controls* has two buttons that determine if the
   opacity (*Alpha*) of a color should be :guilabel:`Picked` and/or
   :guilabel:`Assigned`. These settings affect the way a color is picked if the
   “Picked” object has an opacity different from 100% (or 1.0).

ボタンの状態は次の三通り：

Pick opacity disabled
   例えば、塗りが濃紺で遮光度が 50% のオブジェクトから色をピックすると、遮光度が
   100% の水色になる。設定されたオブジェクトの遮光度はそのまま。
Pick opacity enabled, Assign alpha disabled
   選択された色は、そのオブジェクトの遮光度が 100% だった場合の色。例えば濃紺の
   オブジェクトの遮光度が 50% であれば、濃紺・遮光度 100% の色になる。設定された
   オブジェクトの遮光度はそのまま。
Pick opacity enabled, Assign opacity enabled
   色と遮光度は、いずれもピックしたオブジェクトからコピーされる。遮光度 50% の濃
   紺のオブジェクトは、遮光度 50% の濃紺の塗りで構成される水色になる。設定された
   オブジェクトの遮光度が変更される。

最後の場合だけは、他のオブジェクトの上にない遮光度を持つオブジェクトから色をピッ
クした場合にのみ適用される。

Gradients
----------------------------------------------------------------------

   There are three parts to using a *Gradient*; each treated in the next three
   sections:

   #. Attach a *Gradient* to an object.
   #. Edit the *Stops*.
   #. Adjust the orientation and extent of the *Gradient*.

   The use of linear and radial *Gradients* is essentially the same and both
   will be treated together.

グラデーションをオブジェクトと一緒に変形させたい場合は、選択ツールが使用されてい
るときにツールコントロールにある :guilabel:`Move gradients (in fill or stroke)
along with the objects` ボタンをオンにする。

* :kbd:`Ctrl` + :kbd:`F1` or :kbd:`G` で起動。
* :kbd:`Stop` 挿入 :kbd:`Ctrl` + :kbd:`Alt` + LB クリック
* :kbd:`Ctrl` + :kbd:`L` で冗長なノードを消すらしい。
* :kbd:`Shift` + :kbd:`R` で逆転。

Attaching Gradients to Objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   *Gradients* can be attached to an object either with the :guilabel:`Fill and
   Stroke` dialog or through the use of the *Gradient Tool*.

まず :guilabel:`Fill and Stroke` ダイアログでグラデーションを定義する方法を知る：

   To attach a *Gradient* with the :guilabel:`Fill and Stroke` dialog, simply
   select an object and click on either the linear icon or radial *Gradient*
   icons in the dialog. A *Gradient* with two *Stops* will automatically be
   created and applied to the object. The *Stops* will have the color of the
   previous *Fill* with one *Stop* having full opacity and the other full
   transparency.

二つの停止位置はどちらも前の塗りつぶし色で初期化される。一方は遮光度が 100% で、
他方は 0% で初期化される。

一度作成したグラデーションは再利用できるし、描線にも割り当てられる：

   An already defined *Gradient* can be assigned to the object by selecting the
   *Gradient* from the drop-down menu under the :guilabel:`Fill` tab of the
   :guilabel:`Fill and Stroke` dialog. A *Gradient* can also be assigned to the
   *Stroke* of an object under the :guilabel:`Stroke paint` tab.

*Gradient Tool* を使うには、次の方法がある：

* :guilabel:`Toolbox` の :guilabel:`Create and edit gradients` ボタンを押す。
* :kbd:`Ctrl` + :kbd:`F1` を押すか :kbd:`G` を押す。

*Gradient Tool* の操作方法：

   The *Gradient Tool* *Tool Controls* has options to choose a linear icon or a
   radial icon *Gradient* and the application of the *Gradient* to the *Fill*
   icon or *Stroke* icon of an object. Once the options are selected, *Left
   Mouse Drag* across an object to attach a *Gradient*. The start and stop point
   of the drag will define the range of the *Gradient* (where the start and end
   *Stops* are placed, see below). If an already defined *Gradient* has been
   chosen from the drop-down menu in the *Tool Controls* it will be applied to
   the object. Otherwise a two *Stop Gradient* will automatically be created
   with both *Stops* the color of the objects existing *Fill* and with one
   *Stop* full opacity and the other with full transparency.

Editing Stops
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   They can be edited onscreen. This is much more convenient than using the
   :guilabel:`Gradient Editor` dialog.

Onscreen Editing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   An object with a *Gradient* displays *Gradient* handles when the *Gradient
   Tool*, *Node Tool*, or one of the shape tools is active (the latter two if
   enabled in the :guilabel:`Inkscape Preferences` dialog). Some editing actions
   work when any of these tools is active, others work only with the *Gradient
   Tool*.

ハンドルの意味は次のとおり：

.. csv-table::
   :delim: |
   :header-rows: 1
   :widths: auto

   ハンドル | 停止点
   ○ | 開始
   ◇ | 中間
   □ | 終了

停止点は、グラデーションツール、ノードツール、シェイプツールのいずれかを使って
クリックすることで選択できる。パスのノードの感覚で操作する。

新しい中間停止を追加するには、オブジェクトを選択してグラデーションツールを開き、
次のいずれかを実行する（パスにノードを追加する操作と類似しているものがあることに
注意）：

* グラデーションパスをダブルクリックする
* グラデーションの上で :kbd:`Ctrl` + :kbd:`Alt` を押しつつ左クリック
* 隣り同士の停止点を選択してから :kbd:`Insert` を押す（中点に中間色で生成される）
* *Palette* または :guilabel:`Swatches` ダイアログからグラデーションパスへ色をド
  ラッグする

中間の停止点を削除するには、グラデーションツールを開いた状態で次を行う：

* :kbd:`Ctrl` + :kbd:`Alt` を押しつつ対象停止点上を左クリック
* 選択停止点に対して :kbd:`Del` を押す
* :kbd:`Ctrl` + :kbd:`L` を押すとグラデーション単純化を試みる（パス単純化と類比
  的に）

中間の停止点を移動するには：

* *Gradient Tool*, *Node Tool*, 図形ツールのいずれかを使ってドラッグする。

  * 複数の停止点が選択されている場合、すべて一緒に移動する。
  * :kbd:`Ctrl` 押しドラッグすると、選択されていない最も近い停止点間の距
    離の 1/10 の倍数で停止点がスナップされる。
  * :kbd:`Alt` 押しドラッグすると、選択されている停止点がドラッグしたものからど
    れだけ離れているかに応じて移動する。

* 停止点を選択し、*Gradient Tool* を開いた状態で、矢印キーを押す。

  * 複数の停止点が選択されている場合、すべて一緒に移動する。
  * :kbd:`Shift` を併用すると移動が十倍に加速する。
  * :kbd:`Alt` を併用すると、選択停止点が画面画素一個分ずつ移動する。
  * :kbd:`Shift` + :kbd:`Alt` を使用すると、選択停止点が画面画素十個分ずつ移動す
    る。

停止点は前後の停止点を超えて動かすことはできない。

停止点の色や遮光度を編集する方法も複数ある：

   In general, if no *Stop* is selected, indicators and changes apply to the
   whole object; if one *Stop* is selected, indicators and changes apply to that
   *Stop*; and if multiple *Stops* are selected, indicators show an average
   value for the selected *Stops* and changes apply to all selected *Stops*.

場合分けが複雑なのでいつもと違うやり方をすると忘れる。

:guilabel:`Fill and Stroke` ダイアログ
   停止点が選択されていない場合、グラデーションは :guilabel:`Fill` または
   :guilabel:`Stroke paint` タブでプレビュー。選択停止点がある場合は、その現在の
   色と遮光度の値が表示されまる。変更は選択停止点すべてに適用される。
*Style Indicator*
   停止点が選択されていない場合、インジケータはグラデーションを *Fill* と
   *Stroke* の両方についてプレビュー。選択されている場合にはその停止点の現在の値
   が表示される。変更は選択停止点すべてに適用される。
ドラッグ＆ドロップ
   *Palette* または :guilabel:`Swatches` ダイアログから停止点へ色をドラッグ可
   能。またはグラデーションパス上にドラッグすると停止点が追加。
コピー＆ペースト
   色はクリップボードで読み書きできる。:menuselection:`Edit --> Copy` を選ぶか
   :kbd:`Ctrl` + :kbd:`C` を押すと、停止点が一つだけ選択されているならばその色と
   遮光度が、複数選択されているならば平均色が複写される。:menuselection:`Edit
   --> Paste Style` を選ぶか :kbd:`Shift` + :kbd:`Ctrl` + :kbd:`V` を押すと、選
   択停止点すべてに対してクリップボードから色と遮光度が複写される。

Using the Gradient Editor Dialog
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   It is envisioned that this dialog be removed as redundant in the future.

ということらしいので割愛。

Adjusting Gradients
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

グラデーションは色だけではなくて向きや大きさを変えられる。

   Once a *Gradient* has been applied to an object, the orientation and extent
   of the *Gradient* can be changed via dragging the outer two *Gradient Stops*
   indicated by the square and circle handles.

線形グラデーションのハンドルの意味はよく知っているとおりだ：

   For linear *Gradients*, one set of handles define the range of the
   *Gradient*. The *Gradient* is parallel to the line connecting the two
   handles.

放射グラデーションのハンドルは少し複雑だ：

   For radial *Gradients*, there are two sets of handles (or *Stops*) at right
   angles to each other, sharing the square center handle. The center, handle
   controls the origin of the *Gradient* (one “edge”), while the two circular
   handles control the range of the *Gradient* in orthogonal directions. This
   allows a radial *Gradient* to have an elliptical shape.

グラデーションハンドル自体が特別な移動をすることがある：

   *Gradient* handles from two different objects will snap together if one is
   placed over the other. This facilitates aligning *Gradients* between
   different objects. The handles will then move together.

複数オブジェクトがグラデーションを共有することもある：

   If multiple objects are selected when a *Gradient* is created, all the
   objects will share a common *Gradient*.

指定可能な UI がここにしかないというオプションもある：

   An option only accessible through the *Gradient* tabs of the :guilabel:`Fill
   and Stroke` dialog is defining how the area outside the *Gradient* range is
   filled.

:guilabel:`Repeat` というドロップダウンリストには次の三つの選択肢がある：

.. csv-table::
   :delim: |
   :header-rows: 1
   :widths: auto

   モード | グラデーション
   :guilabel:`None` | 停止点の色で塗りつぶす
   :guilabel:`Direct` | 同じグラデーションを反復
   :guilabel:`Reflected` | 同じグラデーションを反射

グラデーション反転操作が可能だ：

   The keyboard shortcut :kbd:`Shift` + :kbd:`R` reverses the *Gradient*
   direction when the *Gradient Tool* is active. This is especially useful for
   radial *Gradients* where one cannot just drag the *Gradient* handles to
   reverse the *Gradient*.

Meshes
----------------------------------------------------------------------

   Like *Gradients*, *Meshes* have a smooth blending from one color to
   another... FIXME

.. admonition:: 利用者ノート

   本書には記述が一切ないので、読者が試すしかない。

   おそらく Bezier 曲線からなる四辺が現れる。Bezier 曲面か。この各頂点◇にこれま
   で見てきた方法で色と遮光度を指定する。曲面上の UV 座標で最終的な色と遮光度が
   決まるはずだ。それが対象オブジェクトの点の色と遮光度として割り当てられると考
   えられる。

   ということは、Bezier 曲面も学習しなければならないということか。

Patterns
----------------------------------------------------------------------

ベタ塗りやグラデーションの他に「柄」で塗りつぶすこともできる。ぶどうのチュートリ
アルを思い出せ：

   Any object or set of objects can be turned into a *Pattern* and used in the
   fill of an object. The *Pattern* can be shifted, rotated, and stretched as
   necessary. Inkscape includes a set of *Patterns* accessible through the
   :guilabel:`Fill and Stroke` dialog. The Vine Design tutorial covers creating
   and using *Patterns*.

Inkscape 備え付けのパターンには実はライセンスがある。勝手に public license だと
思い込まぬこと。そして、同梱パターンと自作パターンは同一設定ファイルに位置する：

   The *Patterns* included with Inkscape are defined in the file
   :file:`patterns/patterns.svg` located in the Inkscape :file:`share`
   directory. Edit or replace this file to include your own stock *Patterns*.

パターン使用手順は二、三段階からなる：

   The first, optional step, is to create a *Pattern*. The second is to apply
   the newly created *Pattern* or an Inkscape provided *Pattern* to an object.
   And the third is to adjust the *Pattern* position and scaling as necessary.

Creating Patterns
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Simply select the object or objects you wish to use as a *Pattern* and then
   use the :guilabel:`Object --> Pattern --> Objects to Pattern` (:kbd:`Alt` +
   :kbd:`I`) command.

パターンを定義するためだけにオブジェクトを作成しただけであれば、それは削除しても
かまわない：

   After converting the selection to a *Pattern*, the original selection is
   replaced by a *Rectangle* shape object filled with the new *Pattern* (and
   with an invisible stroke). This new object can be deleted but the *Pattern*
   will remain. *Patterns* have a life of their own.

パターンの反復単位寸法はパターンオブジェクト全ての BB とする。

ではパターン内のオブジェクトを編集したい場合にはどうするか。

   The object(s) in any *Pattern* can be edited by selecting an object that is
   filled with that *Pattern* and then using the :guilabel:`Object --> Pattern
   --> Pattern to Objects` (:kbd:`Shift` + :kbd:`Alt` + :kbd:`I`) command. The
   original objects will reappear in their original place (built-in *Patterns*
   will appear in the upper-left corner).

編集後はパターンに戻る。新旧どちらのパターンも利用可能な状態になる。したがって、
旧パターンを適用していたオブジェクトの見てくれは変わらない。

   The new *Pattern* must be “reapplied” to the object the *Pattern* came from.

Using Patterns
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   To change the fill of an object to a *Pattern*, simply click on the
   :guilabel:`Pattern` icon in the :guilabel:`Fill and Stroke` dialog. Then
   select the required *Pattern* from the pull-down menu. User created
   *Patterns* will be listed first.

出来合いのパターンは縞々が多い。水増しか。

オブジェクトの座標変換に関するパターンの挙動はツールバーの :guilabel:`Move
patterns (in fill or stroke) along with the objects` でオンオフを指示する。

Adjusting Patterns
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

パターン自体へ座標変換を施すことが可能だ：

   Adjusting *Patterns* is done by a set of handles. The handles will appear
   when an object with a *Pattern* fill is selected and the node or one of the
   shape tools is active. The handles will appear on the original objects that
   defined the *Pattern*, or the former location of those objects if they have
   been moved or deleted (unless the *Pattern* has been previously adjusted).

出来合いのパターンに対してはハンドル位置がどこに出るのかというと、

パターンのハンドルによる座標変換操作方法は、図形オブジェクトのそれと同様のよう
だ：

   To adjust the origin, scale, and orientation of the *Pattern*, drag the
   translation handle (×), scale handle (square), and rotation handle (circle).

これは憶えておくと便利：

   For :abbr:`SVG` viewers that don't support clipping, you can crop a bitmap by
   turning the bitmap into a *Pattern* and using it to fill an arbitrary path.

Hatchings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

パターン機能を応用したハッチング実装例。縞々を巧みに使う。

Custom Swatches
----------------------------------------------------------------------

*Custom Swatches* は :guilabel:`Auto` パレットに単色とグラデーションを自動的に追
加して生成される。

   *Custom Swatches* allow per document palettes with swatches of solid colors
   and *Gradients*. *Custom Swatches* are automatically added to a special
   :guilabel:`Auto` palette as they are created (selectable in the *Palette* or
   :guilabel:`Swatches` dialog). Solid color swatches are implemented as
   one-stop *Gradients*.

最初は空だが、色指定中の :guilabel:`Swatch` ボタンを押すと追加される。手動ではな
いか：

   To create a *Custom Swatch*, with an object selected that has the desired
   solid fill or *Gradient*, click on the icon in the :guilabel:`Fill and
   Stroke` dialog (in the :guilabel:`Fill` or :guilabel:`Stroke paint` tab as
   appropriate).

:guilabel:`Swatch fill` 画面で色を編集すると、図面内でそれを参照しているオブジェ
クトが更新されて変色する。

.. admonition:: 利用者ノート

   プログラミング技法で言うと定数を宣言するようなものだ。したがって、この機能を
   多用するべきかもしれない。

*Custom Swatch* をオブジェクトの塗りに割り当てる方法は見ればわかるだろう。
削除したい場合は、右クリックメニューを使う：

   To delete a swatch, select :menuselection:`Delete` from the menu that pops up
   when you *Right Click* on the swatch in the *Palette* or :guilabel:`Swatches`
   dialog (the :guilabel:`Auto` palette must be selected).

   Note that using :menuselection:`File --> Vacuum Defs` will not remove unused
   swatches.

Inkscape 1.2 で相当するコマンド :menuselection:`File --> Clean Up Document` は未
使用の swatch を削除するように見える。

Fill Rule
----------------------------------------------------------------------

ここで述べられている塗りつぶし法則は Inkscape 以外でも応用が効くので習得するべき
だ。

パスが自己交差しているときなどに、どの領域を塗りつぶすかを決定する計算法だ。この
規則オブジェクトの *Fill* にのみ適用され *Stroke paint* には適用されない。選択肢
は右側のボタン二つだ。

:guilabel:`Any path self-intersections or... (fill-rule: evenodd)`
   パスに対して、それを横断するような直線を脳内で引いて考える。交点が生じるたび
   にカウンターを増やしていき、その値が奇数か偶数かで閉領域を塗るか否かを決定す
   る。
:guilabel:`Fill is solid unless... (fill-rule: nonzero)`
   これも同様に横断直線との交点を考える。こちらは交点におけるパスの向き（左右）
   でカウンターの増減を決める。カウンターが非ゼロの領域は内部とみなして塗る。

Stroke Style
======================================================================

描線については属性が色以外にもいくつかある：

   In addition to *Stroke paint*, discussed in the previous section, *Stroke*
   attributes include stroke *Width*, *Join* style, *Cap* style, *Dashes*, and
   *Markers*.

これらの属性値を指定する場所は今までと同じだ：

   All of these attributes can be set using the :guilabel:`Stroke style` tab in
   the :guilabel:`Fill and Stroke` dialog. *Stroke width* can also be set using
   the *Style Indicator* (see below).

Stroke Width
----------------------------------------------------------------------

描線の太さを指定する場所および方法は以下に述べる三つだ。

:guilabel:`Stroke style` タブ
   これは UI を見れば一目瞭然。単位指定用ドロップダウンリストが併設。

*Style Indicator*
   描線色欄の右側に記されている数字に注目する：

      A *Right Mouse Click* on the *Stroke width* part of the *Style Indicator*
      opens a pop-up menu that allows the stroke width unit to be changed as
      well as a preset width to be selected. The stroke can also be removed with
      this menu.

   プリセット数値がキリ番なので、入力欄とキーボードを使うよりは手軽だ。

*Stroke Gestures*
   *Style Indicator* の *Fill Indicator* でやったマウスジェスチャーと同様の操作
   で描線の太さをおおまかに変更できる。ドラッグ開始位置は描線太さ欄とする。

      The principle is that as you drag the mouse, the line width will change
      proportionally to the distance from a 45° line from the indicator. The
      farther away you are, the more subtle the changes can be. The maximum
      width increase is a factor of 4 and the minimum width is zero.

描線を有するオブジェクトが座標変換するときの、線の太さの変更オプションもある。意
味はグラデーションとパターンそれぞれの対応オプションと同様だ：

   If you want the line width to transform with an object, you must toggle on
   this option using the :guilabel:`When scaling objects, scale the stroke width
   by the same proportion` icon that is in the *Tool Controls* when the *Select
   Tool* is in use.

Join Style
----------------------------------------------------------------------

   The Join style is how two lines meeting at a corner should be joined
   together. The options are:

   * :guilabel:`Miter join`
   * :guilabel:`Round join`
   * :guilabel:`Bevel join`

Miter と Bevel の使い分けのコツが次の記述から読み取れる。また、交点の状況によっ
ては Miter 指定でも Bevel として描かれることがある：

   When the *Miter* option is selected, the length of the projection can become
   quite long if the two lines intersect at a small angle. In this case, it may
   be preferable to use the *Bevel* style. The *Miter limit* controls the point
   at which a *Miter join* automatically is converted to a *Bevel join*. If the
   distance from the inner intersection point to the tip of the triangle (``m``
   in the following figure) measured in stroke widths is more than the *Miter
   limit*, the join will be drawn in the *Bevel* style.

Cap Style
----------------------------------------------------------------------

   The *Cap* style determines how the end of a line is drawn. The options are:

   * :guilabel:`Butt cap`
   * :guilabel:`Round cap`
   * :guilabel:`Square cap`

この属性は描線両端だけでなく、ダッシュ各線分にも影響する。

Dashes
----------------------------------------------------------------------

UI は :guilabel:`Dash pattern` ドロップダウンリストと :guilabel:`pattern offset`
欄で構成される。

   The patterns scale with the stroke width.

   The offset shifts the Dash pattern along the path. The units are in stroke
   width.

Markers
----------------------------------------------------------------------

   *Markers* are objects like arrow heads placed along a path. Different
   *Markers* can be specified for the start, middle, and end of a path. *Middle
   Markers* are placed at the location of every non-end node.

マーカー描画を考慮すると、形状に関係のない中間ノードを配置することもある？

マーカーを自作する方法がある：

   A custom *Marker* can be created by selecting the object or objects that you
   wish to use as a *Marker* and then using the :menuselection:`Object -->
   Object to Marker` command. The selected objects will disappear and a new
   entry will appear in the *Marker* pull-down menus of the :menuselection:`Fill
   and Stroke` dialog.

マーカーの幾何的仕様：

   The *Marker* is created assuming a horizontal orientation for the path. The
   point of attachment to a node is the center of the bounding box for the
   *Marker*.

マーカーには問題が二点あるそうだ：

   Two problems exist with *Markers*. The first is that *Markers* do not take
   the color of the stroke.

これに関しては 1.2 では修正されているように見える。ハサミの色が描線と一致する。
以前は確かに記述されているとおりだった。

   The second problem is that *Markers* scale with line width. The line width
   had to be reduced in the above figure for the scissors examples, to give the
   scissors a reasonable size. Again, one could edit the :abbr:`SVG` file to
   adjust the *Marker* size.

これはこのとおり。:abbr:`SVG` 直接編集という最終手段が使える。

Complex Strokes
----------------------------------------------------------------------

異なるストローク属性を持つパスを重ね合わせることで、複雑なマーカー付きの線を描け
る。クローン系コマンドを巧妙に応用するといい。

.. _LittleCMS: https://www.littlecms.com/
