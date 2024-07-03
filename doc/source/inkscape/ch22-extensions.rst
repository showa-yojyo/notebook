======================================================================
Chapter 22. Extensions
======================================================================

.. contents::

Inkscape の拡張システムはプロセス内部から Python などのスクリプトを実行する形式
をとる。

   Some of the included *Extensions* might be of marginal use to the average
   user. However, much can be learned by examining the code in order to write
   your own scripts. Look in the :file:`share/inkscape/extensions` directory for
   the code.

確かに Python スクリプトファイルがいくつも置いてある。Inkscape API のようなもの
があり、それを呼び出すようなものか、フレームワークになっていて特定のメソッドを上
書きするようなものか。

   Often, an *Extension* can be used to quickly prototype a feature that may be
   included natively in a future version of Inkscape. *Extensions* are also a
   good way to add a feature that may have limited use by the general Inkscape
   community and thus not warrant the long-term commitment of adding the feature
   to the main code base.

玉石混淆という言葉が思い出される。拡張が動かない場合はログファイルを確認する：

   If an extension doesn't work, it may be that you are missing some external
   dependency. You can check if this is the case by looking at the log file
   :file:`extensions-errors.log` in your Inkscape preferences directory (Linux:
   :file:`.config/inkscape`, Windows: :file:`Documents and
   Settings\\USER\\Application Data\\Inkscape`).

拡張は同期的にも非同期的にも実行可能だ：

   *Extensions* can be run live, that is, the script code can be run
   automatically in the background, responding immediately to changes in
   parameters. This can both be good (see results of parameter changes
   immediately) or bad (updating before a parameter is fully modified). Each
   *Extension* dialog has a button to toggle on and off this :guilabel:`Live
   Preview`.

拡張コマンドは大分類されている：

.. csv-table::
   :delim: |
   :header-rows: 1
   :widths: auto

   分類 | 操作
   Arrange | オブジェクトを配列し直す
   Color | オブジェクトの色を変える
   Generate from Path | パスオブジェクトからオブジェクトを新しく作成する
   Images | Inkscape ファイルに画像を埋め込む
   JessyInk | ウェブブラウザーで表示できる表現を用意する
   Modify Path | 既存パスを変更する
   Raster | ビットマップの色を操作する
   Render | オブジェクトを新しく作成する
   Text | テキストを操作する
   Visualize Path | パスに関する情報を表現する
   Web | JavaScript 引数を追加したり描画をビットマップにスライスしたりする

そして、直前に実行した拡張を実行するためのコマンドがある：

   Two entries under the :menuselection:`Extensions` menu allow you quick access
   to the previously used extension. The first, :menuselection:`Extensions -->
   Previous Extension`, will run the extension with the same parameters. The
   second, :menuselection:`Extensions --> Previous Extension Settings...`, will
   pop up the parameters dialog.

Arrange
======================================================================

   This category rearranges objects in a drawing. At the moment there is just
   one extension in this category.

ここに記述がある :menuselection:`Restack...` の他に、Inkscape 1.2 では
:menuselection:`Deep ungroup...` もある。

Restack
----------------------------------------------------------------------

オブジェクト群の z-order を変更するコマンドだ。

:guilabel:`Restack Direction`
   本書とは違って :guilabel:`Preset` か :guilabel:`Custom` かをまず指定する。
   前者ならば次のメニューから指定する：

   * Left to Right
   * Bottom to Top
   * Right to Left
   * Top to Bottom
   * Radial Outward
   * Radial Inward

   後者ならば :guilabel:`Angle` を指定する：

   In the last case the angle is given in the :guilabel:`Angle` entry box where
   the angle is defined counterclockwise with zero corresponding to left to
   right.

:guilabel:`Object Reference Point`
   オブジェクト BB のどこに基づいて z-order 再配置に利用するかを指定する。

.. admonition:: 読者ノート

   スライスハムのデモを見ると、この機能の目的は理解できるが、角度指定の挙動が理
   解できない。

Color
======================================================================

この分類にある拡張はオブジェクトやグループの色を操作するものだ。

   The color mapping is calculated in the :abbr:`RGB` color space except for the
   extensions that modify :abbr:`HSL` values, which are calculated in
   :abbr:`HSL` color space.

オブジェクトやグループが選択されていなくてもこの機能は働き、その場合は図面全体に
作用する：

   If no objects are selected, the color change will be applied to the entire
   drawing. An object's *Stroke* and any *Gradient* are also changed.

.. admonition:: 読者ノート

   ビットマップには効かない。:menuselection:`Filters --> Color` を当たる。

Black and White
----------------------------------------------------------------------

デモイラストを見れば機能は一目瞭然だ。計算方法は、

   The extension first calculates brightness (luma) using the YUV_ color space
   (for NTSC and PAL standard definition television) and then applies a
   threshold of 50%.

ということで、ビデオ映像でよく使われる色空間で操作される。また、現行バージョンで
は閾値を指定可能だ。

Brighter
----------------------------------------------------------------------

   This extension has the property of making dark colors more intense but
   washing out light colors. The effect is subtle so multiple applications may
   be required.

上記の性質があるので、効き目を弱くしてあり、複数実行を前提とする設計になっている
と考えられる。

Custom
----------------------------------------------------------------------

   This extension allows color custom transformation functions to be defined.
   Standard math operations are allowed such as ``+``, ``-``, ``*``, and ``/``.
   If a resulting value is outside the allowed limits, it is set at the minimum
   or maximum allowed value.

Python コードの ``ast.parse`` で評価される。シフト演算やべき乗、Python 組み込み
関数も利用可能ということだ。

Darker
----------------------------------------------------------------------

   Darken the color of an object or Group of objects. Each R, G, and B component
   of a color is set to 90% of its previous value. The effect is subtle so
   multiple applications may be required.

Brighter 機能と同じ注意が当てはまる。

Desaturate
----------------------------------------------------------------------

脱色という珍しい操作だ。

   This sets the values of R, G, and B to the average of the maximum of R, G,
   and B; and the minimum of R, G, and B. For example, R would be set to ``(max(
   R, G, B) + min(R, G, B))/2``.

Grayscale
----------------------------------------------------------------------

こちらも彩度が失せる操作だ。この数式には馴染みがある。

   Change the color to a gray using the formula for Luminance used by the NTSC
   and PAL television standards. This sets the color to a lightness (Y) defined
   by: ``Y = 0.229 × R + 0.587; × G + 0.114 × B``.

Less Hue
----------------------------------------------------------------------

色相の値を 18 度下げる機能だ（ゼロで実行すると 343 度になる）。

   The hue is decreased by 5% (of the full hue range) or equivalently, a
   rotation of 18° around the color circle. This, for example, means that a pure
   red picks up a touch of blue in the :abbr:`RGB` color space.

Less Light
----------------------------------------------------------------------

輝度を現在の 5% だけ下げる。100 から開始するならば 95, 91, 86, ... のように推移
するという意味だ。

   The lightness is decreased by 5% (of the full lightness range). If the
   lightness is already less than 5%, it is set to 0%. The effect is subtle so
   multiple applications may be required.

Less Saturation
----------------------------------------------------------------------

彩度を最大値の 5% だけ下げる。

   The saturation is decreased by 5% (of the full saturation range). If the
   saturation is already less than 5%, it is set to 0%. The effect is subtle so
   multiple applications may be required.

More Hue
----------------------------------------------------------------------

Less Hue の逆機能。

More Light
----------------------------------------------------------------------

Less Light の逆機能。

More Saturation
----------------------------------------------------------------------

Less Staturation の逆機能。

Negative
----------------------------------------------------------------------

:abbr:`RGB` の各成分に対して、その補数で置き換える。

   For example, an R value of 64 (25%) becomes an R value of 191 (255 - 64, or
   75%).

Randomize
----------------------------------------------------------------------

   Randomize the color of selected objects or all objects if no object is
   selected. You can choose which of the :abbr:`HSL` color parameters to
   randomize (hue, saturation, and/or lightness).

Opacity も操作可能。スライダーバーで指定する値は振れ幅のような値と考えられる。

Remove Blue
----------------------------------------------------------------------

   Set the B value in :abbr:`RGB` to 0.

Remove Green
----------------------------------------------------------------------

   Set the G value in :abbr:`RGB` to 0.

Remove Red
----------------------------------------------------------------------

   Set the R value in :abbr:`RGB` to 0.

Replace color
----------------------------------------------------------------------

完全マッチによる色置換だ。イラスト作成ソフトだから意味がある。

   Color to be replaced must match exactly.

RGB Barrel
----------------------------------------------------------------------

   Rotates color (hue) by 120° around the color circle.

Generate from Path
======================================================================

   This group of extensions creates new objects from one or more existing paths.

Extrude
----------------------------------------------------------------------

3D モデリングのそれとは毛色が異なる。

プロファイルパスの対応するノード同士を線分でつなぐだけと思われる。オプションに
よっては塗りつぶす。イラストは星型から星型に押し出しているのでわかりやすい。滑ら
かな曲線で試すと最後のオプションの意味がわかりやすくなる。

Inset/Outset Halo
----------------------------------------------------------------------

   Why would you want to use this extension when Inkscape now supports filters?

:menuselection:`Filters --> Shadows ang Glows --> In and Out` のことだろうか。

Interpolate
----------------------------------------------------------------------

いわゆる「中割り」を生成する機能だ：

   Draws a series of lines that interpolate the space between two paths. The
   options include setting the number of :guilabel:`Interpolation Steps`
   (in-between lines), an :guilabel:`Exponent` factor that controls the spacing
   between interpolated paths (zero for even spacing), specifying if the
   original paths should be duplicated (:guilabel:`Duplicate Endpaths`), and
   specifying that the path style should also be interpolated.

試したところ、簡単なパスでも計算時間を比較的要するようだ。

補間処理はノード同士の対応を見るので、実行前にパスの向きを確認しておくといい。以
前習った手筋が使える：

   The starting point of a path can be found by selecting the path with the
   *Node Tool* and then using the :kbd:`Tab` key. If no node is already
   selected, the first node in the path will be selected.

凝ったグラデーションを描くのにこの機能を応用することも可能だ：

   The interpolation extension can also be used to simulate gradients of
   different symmetries. When calling the extension, the smaller path should be
   selected first.

星型のイラストはこの応用例が重要である可能性を示している。線形と放射だけで間に合
わない場合はこれだ。

Motion
----------------------------------------------------------------------

実行してみると、これこそ私の思う Extrude コマンドだ：

   Simulates motion. Draws a copy of the selected object behind the original and
   then connects corresponding nodes with lines to form a group of closed paths.
   The direction and offset of the copied object can be specified. The new
   objects inherit the attributes of the original but can be edited as a group.

パス操作に自信があれば押し出し先の図形を縮小するなどして遠近法を表現することも可
能：

   One can also use this extension to simulate perspective by reducing the size
   of the copy along with the associated nodes.

Pattern Along Path (Extension)
----------------------------------------------------------------------

Live Path Effects にある同名の機能を参照。パターンパス、軌跡パスの順に選択してか
ら拡張コマンドを起動し、実行する。

パターンを反復する場合、その配列原則は次のとおり：

   The bounding box of the pattern is used for placing the pattern along the
   path, with the bounding box of one pattern copy touching the bounding box of
   the next copy (if no additional spacing is specified).

:guilabel:`Pattern Along Path` ダイアログで指定可能なオプションのうち、注意の要
る項目だけノート：

:guilabel:`Deformation type`
   次の二つから選択する：

   :guilabel:`Snake`
      幼いころに遊んだ蛇のおもちゃのような変形および配列をする。英語による記述の
      ほうがいい：

         The pattern is rotated and deformed to follow the path such that all
         points with the same horizontal (x) position in the pattern will be on
         the same normal (perpendicular line) to the path, and all points with
         the same vertical (y) position in the pattern will be placed the same
         distance from the path.
   :guilabel:`Ribbon`
      こちらは軌跡パスに沿う法線方向か接線方向のいずれかのみ変形する。

   どちらの選択肢も :guilabel:`Pattern is vertical` 指定の有無を参照する。

:guilabel:`Pattern is vertical`
   パターンの向きを 90 度回転して処理する。

   The Pattern along Path is a very useful extension but it does have a few
   quirks. One is that if the pattern is moved before use, the results may be
   less than ideal. Another is that different parts of the pattern can be
   distorted in different ways as seen in figures that follow.

イラストの青チェッカフラグパターンをどう定義したのかも気になる。

   The following example shows a pattern placed on both straight and curved
   paths. If the radius of curvature is too small, the pattern may be grossly
   distorted.

要するに、激しく曲がっているパスにパターンを配列すると大きく歪む可能性が高い。

ラーメン丼の雷紋などを作図するのにもこの機能は利用できる。少し高度な技術を要す
る：

   Care must be taken that the pattern lines up at the corners. This can be done
   by making the distance between the corner nodes multiples of the pattern
   width or by breaking the path into disconnected pieces at the corners (use
   the :guilabel:`Break Path at Selected Nodes` option in the *Node Tool* *Tool
   Controls*) and using the :guilabel:`Repeated, stretched` option.

デモイラスト (5a) を見る。どちらも中央のパターンをパスに変換した矩形に乗せたもの
だ。

* 左側：矩形の辺の長さがパターンの幅の倍数になるように設定。
* 右側：各コーナーノードで Break 済み。

デモイラスト (5b) では辺の長さがパターン幅の倍数でないため、角でパターンが一直線
にならない。:guilabel:`Copies of the pattern` の選択肢を適切に変えてパターンが角
で不連続にならないようにする。

太陽のデモはグラデーションの赤がどこから出てきたのか示されていないが、パターンに
あらかじめ設定しておくと考えるのが自然だ。

テキストをパスに沿って配列する応用はよくある：

   One use of :guilabel:`the Single, stretched` option is to put text on a path.
   The text must be converted to a path first (:menuselection:`Path --> Object
   to Path` (:kbd:`Shift` + :kbd:`Ctrl` + :kbd:`C`)).

花柄を作図するのにも使えないことはない：

   Another use of the :guilabel:`Single, stretched` option is to create
   flourishes. (As of v0.47, this is better done by applying the “teardrop” as a
   custom shape with the *Bezier Tool*. One would not need to add the extra
   nodes.)

Scatter
----------------------------------------------------------------------

前項の機能と類似したものだ：

   This extension places a pattern along one or more target paths. It is almost
   identical to the *Pattern along Path* extension except that the pattern is
   not deformed.

固有オプション説明：

:guilabel:`Follow path orientation`
   変形なしの :guilabel:`Snake` と思っていい。

:guilabel:`Stretch spaces to fit skeleton length`
   軌跡パスを均等に埋めるようにパターン分身間に空間を追加する。

:guilabel:`Original pattern will be`
   *Pattern along Path* とは違って変形の可能性がないのでこれらの選択肢がある：

   * :guilabel:`Moved`
   * :guilabel:`Copied`
   * :guilabel:`Cloned`

Voronoi
----------------------------------------------------------------------

   The line segments are derived by distributing sites (points) semi-randomly in
   an area and then constructing line segments where each point on the segment
   is equal distance to the two closest sites forming cells around each site.

.. admonition:: 読者ノート

   Inkscape 1.2 の :menuselection:`Extensions --> Generate from Path --> Voronoi
   Pattern...` に相当する。

利用方法は単純だ：

   To use this extension, select a path or object and then call up the
   extension. There are two settings:

:guilabel:`Average size of cell (px)`
   平均細胞寸法。

:guilabel:`Size of Border (px)`:
   平均細胞寸法より大きい正の数を指定すると、滑らかにタイル化できるパターンにな
   る。負の数を指定すると、辺付近の点集合が削除され、境界付近の細胞が大きくな
   る。

この拡張で重要なことは、生じたパターンが *Fill* として指定可能であることだ：

   After applying this extension, you will have a *Pattern* that is applied to
   the *Fill* of the object that was selected. The *Pattern* can be shifted,
   scaled, and rotated like any other *Pattern*. It can also be applied to other
   objects through the :guilabel:`Fill` tab of the :guilabel:`Fill and Stroke`
   dialog.

Images
======================================================================

Extract One Image
----------------------------------------------------------------------

:menuselection:`Extensions --> Images --> Extract Images` に統合されたと思われ
る。

   This extension will extract the selected bitmap image from the drawing. The
   destination filename must be given (and not just the path [Bug]). The
   filename extension (e.g., “.png”) is automatically added. As of v0.48,
   relative paths are relative to the user's home directory.

この文章からわかるようにこの拡張は使い物にならない。出力先を指定する UI がまとも
でない。

Embed All Images
----------------------------------------------------------------------

   It is possible to embed the images inside an Inkscape :abbr:`SVG` file with
   this extension. Simply call this extension to embed all bitmap images in the
   file. This may make your :abbr:`SVG` file quite large. Only :abbr:`PNG` and
   :abbr:`JPEG` files may be embedded.

この機能は :abbr:`SVG` を gist.github.com などにアップロードする場合には使えるか
もしれない。Markdown に :abbr:`PNG`/:abbr:`JPEG` を埋め込むようなものだろう。

JessyInk (Presentations)
======================================================================

Web ブラウザー用のスライドショーを作る機能のようだ。

   The JessyInk package of extensions allows one to use Inkscape to produce a
   sophisticated web-based presentation, complete with master slides, automatic
   page numbering, transitions between slides and within slides, and page
   zooming. JessyInk works by embedding JavaScript into your :abbr:`SVG` file.
   The JavaScript then manipulates Inkscape *Layers* to run the presentation.

:abbr:`SVG` はその仕様上 JavaScript コードを抱える能力があり、それを利用した拡張
だ。

   Perhaps the best way to see what JessyInk can do is to run the demonstration
   that can be found in the Featured downloads section on the JessyInk Home
   Page.

それらしいページをインターネットから検索することができない。

使い方を見ていく。

   To use JessyInk you first need to add the JessyInk JavaScript code to your
   :abbr:`SVG` file. This is done by calling up the :guilabel:`Install/Update...`
   dialog and clicking on the :guilabel:`Apply` button. The code can be removed
   by using the :guilabel:`Uninstall/remove` dialog.

前者のダイアログは Python などのパッケージ更新処理に類似している。後者は一覧の中
から不要な効果を選択して図面から取り除くというものだ。

   Once the code is installed, each *Layer* becomes a slide in the presentation.
   The order of the *Layers* in the drawing corresponds to the order of the
   slides in the presentation. One slide can be designated as the *Master slide*
   which will be displayed as background to all the other slides.

背景付き紙芝居と解釈できる。

Master Slide
----------------------------------------------------------------------

   To create a master slide, first create a layer with all the objects you wish
   to appear on all slides. Give the slide a name using the :guilabel:`Layer`
   dialog (``Master Slide`` is a good choice). Then call up the
   :guilabel:`Master Slide` dialog via the :menuselection:`Master Slide...` menu
   entry. Enter the slide name and click the :guilabel:`Apply` button.

マスタースライド用レイヤーを指定するには、上記専用ダイアログからレイヤー名をキー
ボードで入力する。したがって、対象レイヤーをひねくれた名前にできない。

マスタースライドは単なる背景ではない。連番（ページ）付与などの便利な機能がある。

   You can add a few special Auto-texts to the *Master Slide*. The most useful
   is the *Slide number* which will automatically display the correct slide
   number on each slide. You can also display the total number of slides
   (excluding the *Master Slide* and the title (*Layer*) name of each slide.

ページ番号を表示する手順を見ていく。マスターレイヤーにダミーテキストを配置してか
ら自動テキストダイアログで操作する：

   To add Auto-text, put dummy text on the *Master Slide* where you want the
   Auto-text to be located. The Auto-text will be displayed with the style of
   the dummy text. Select the dummy text and then on the :guilabel:`Auto-texts`
   dialog select the desired type and hit the :guilabel:`Apply` button. You will
   not see any change to the text in Inkscape but when viewing the presentation
   in a Web browser, the correct Auto-text will be displayed.

デモの記述からすると、次のことが読める：

   * 文字列 ``Slide Title`` が各スライドのレイヤー名に置換される。
   * 文字列 ``#/#`` が総ページ数付き現在ページに置換される。

Transitions
----------------------------------------------------------------------

   Transitions between slides can be added with the :guilabel:`Transitions`
   dialog. Each slide can have a transition before (in) and after (out) its
   display.

FFmpeg でよくやるからわかりやすい。次の仕様が便利だ：

   A default transition type can be assigned to the *Master Slide* which will
   then be used by all slides that don't have an explicit transition assigned to
   them.

必要なスライド（レイヤー）ごとに in と out の両方を指定する：

   There are three types of transitions: :guilabel:`appear`, where the slide
   appears instantly; :guilabel:`fade`, where the slide fades in or out; and
   :guilabel:`pop` where the slide fades in or out and grows or shrinks. The
   transition time for :guilabel:`fade` and :guilabel:`pop` can be set in the
   dialog.

   To set a transition effect, call up the :guilabel:`Transition` dialog and the
   enter the *Layer* name that you which the transition to apply to. Select the
   transition type and click the :guilabel:`Apply` button. No visible change
   will be seen in Inkscape.

実際に処理するのはウェブブラウザーだが、スライド（レイヤー）が含む画像によっては
この処理は :abbr:`CPU` を食う：

   They can eat up a lot of :abbr:`CPU`, especially if using large bitmap images
   or *Gradients* and *Filters*.

Effects
----------------------------------------------------------------------

同一レイヤー内でのオブジェクトまたはグループ表示操作を実現する。

   For example, you can have a series of bullet points that appear one at a
   time. The same types of effects as for transitions are available:
   :guilabel:`appear`, :guilabel:`fade`, and :guilabel:`pop`. The order in which
   different effects are applied during a presentation is determined by the
   Order parameter. Effects with the same order number will appear at the same
   time.

例によって UI が良くない。手作業が多くて面倒そうだ：

   To add an effect, select an object or a *Group* and then call up the
   :guilabel:`Effects` dialog. Select the type of effect and specify an order.
   Finally, click on the :guilabel:`Apply` button.

Views
----------------------------------------------------------------------

   Views are away to zoom in and out to part of a slide. Rotation is also
   possible. Views can be mixed with effects. The order is determined by the
   :guilabel:`Order` parameter.

ビュー範囲を指定するのに Inkscape の矩形オブジェクトを用いる：

   To set a view, add a *Rectangle* to a slide. Removing the *Fill* and adding a
   light color *Stroke* allows viewing the rest of the slide easily. With the
   *Rectangle* selected, call up the :guilabel:`View` dialog, set the
   :guilabel:`Order` parameter and click :guilabel:`Apply`.

ビューを取り消したい場合にはダイアログの :guilabel:`Remove View` をチェック。

Miscellaneous
----------------------------------------------------------------------

他の機能をまとめて紹介：

:menuselection:`Keys bindings`
   再生中の使用するキーバインドを設定する。
:menuselection:`Mouse handler`
   再生中のマウスイベントハンドラーを設定する（三択）。
:menuselection:`Summary`
   :abbr:`SVG` ファイルに埋め込まれた JessyInk スクリプトの概要を作成する。
:menuselection:`Video`
   :abbr:`HTML` の ``video`` タグを追加するスライドショーに埋め込めるようにする。

Presenting
----------------------------------------------------------------------

完成したスライドショーは :abbr:`SVG` 対応ウェブブラウザーで開くことが可能だ。最
初のページは自動で表示され、次のキー操作でスライドを変える：

.. csv-table::
   :delim: |
   :header-rows: 1
   :widths: auto

   キーバインド | 操作
   :kbd:`→` or :kbd:`PgDn` | 進む
   :kbd:`←` or :kbd:`PgUp` | 戻る
   :kbd:`↑` or :kbd:`↓` | Effect 抜きで進行

再生中に利用できる特別機能：

Index Sheet
   :kbd:`I` を押すことで発動。スライドのサムネイルを九枚表示し、矢印キーでスライ
   ドを移動できる。もう一度 :kbd:`I` を押すと、強調表示されたスライドの冒頭に戻
   る。
Drawing Mode
   :kbd:`D` を押すと描画モードのオンオフを切り替える。マウスポインターがペンに
   なってお絵描きができる。

   * ストローク属性はキーで制御する。詳しくは :guilabel:`Key bindings` ダイアロ
     グを開いて:guilabel:`Drawing mode` タブにある（ここの UI もどうかしてい
     る）。
   * :kbd:`Z` を押すと線が一本元に戻る。

White Board Slides
   :kbd:`N` キーを押すと空白スライドが挿入される。この上記のモードで白板として利
   用するといい。

Modify Path
======================================================================

Add Nodes
----------------------------------------------------------------------

   Adds nodes to a path, leaving the shape of the path unchanged. The nodes are
   added evenly spaced. The number of nodes is either specified or by setting a
   minimum specified spacing.

形状を変えずにパスにノードを等間隔に追加すると、マーカーを付けるのに役に立つ。

Color Markers to Match Stroke
----------------------------------------------------------------------

これは現行バージョンの :menuselection:`Extensions --> Modify Path --> Color
Markers` に相当する。マーカーの *Fill* と *Stroke color* をどちらも編集できる。

Convert to Dashes
----------------------------------------------------------------------

   The extension takes a *Path* with *Dashes* and converts each *Dash* into a
   separate sub-path. This is to allow desktop cutting plotters to cut dashed
   lines.

部分パスで構成される複合パスに変換する。

Edge 3D
----------------------------------------------------------------------

この拡張コマンドは、パスが定義する領域を立体的に見せるためのハイライトと影を表現
するためのパスオブジェクトを追加する：

   Adds highlights and shadows to simulate 3D objects like buttons. The
   extension works by adding paths that are blurred via the *Gaussian Blur*
   filter and then clipped. The paths have partial transparency, with white for
   highlights and black for shadows.

対象オブジェクトは厳密にパス型である必要があり、場合によってはノードを追加して見
栄えを良くすることになる。

Envelope
----------------------------------------------------------------------

こういう操作を envelop というのか：

   Distorts a path so that the path's original *bounding box* is mapped to the
   edges of a quadrilateral.

変形させたいパスと、対応先四角形パスをこの順に選択してからコマンドを実行する。

   To use the extension, select the path to transform first, then add the
   quadrilateral path to the selection. Regular shape objects must be converted
   to a path before transformation.

対応先四角形パスの向きが重要だ。必要に応じてパスを逆向きにする。

Flatten Bezier
----------------------------------------------------------------------

Bezier 曲線パスを近似ポリラインに変換する拡張コマンドだ。

   This extension converts selected Bezier curves to an approximation composed
   of straight-line paths. The number of line segments used is determined by the
   :guilabel:`Flatness` parameter. The smaller the :guilabel:`Flatness`, the
   more line segments are used.

平坦度が小さいほど細やかなポリラインに変換される。つまり近似精度が高い。

Fractalize
----------------------------------------------------------------------

:abbr:`CAD` 出身のプログラマーからすると異色のコマンドに見える：

   This extension turns a straight-line segment into a crooked segment. It works
   by finding the midpoint of the line segment, adding a node at that point, and
   then moving the node a random distance perpendicular to the original path
   direction. This division routine is called recursively depending on the
   setting of the :guilabel:`Subdivisions` entry in the dialog, doubling the
   number of resulting segments for each increase by one.

入力欄の数は折れ線数を意味しない。二分法で折れ線が生じるのでこのような仕様なのだ。

   The :guilabel:`Smoothness` of the path can also be specified. The magnitude
   of the perpendicular displacement is a random function with the limits
   determined by ±(Segment length)/(1 + Smoothness).

平滑度が大きいほど「揺らぎ」が小さくなる。

   The extension will also work on a curved path by turning the path into a
   series of line segments between the path's nodes.

この場合にはポリラインの断片それぞれに対して再帰的細分を施す。

Interpolate Attribute in a Group
----------------------------------------------------------------------

   This extension takes the objects in a *Group* or a selection and assigns a
   value to some attribute of each object, interpolating between two extremes to
   determine the value. Note that the order of the objects in the :abbr:`SVG`
   file determines the order in which the interpolated attributes are assigned.

この拡張コマンドの意味は本書のデモ二つを見れば理解できる。

   Options include interpolating color, width, height, scale, and position.

試したところ、色の補間はおそらく :abbr:`HSL` 色空間が用いられるのではないかと思
う。

Jitter Nodes
----------------------------------------------------------------------

   Randomly shift nodes and/or node handles.

著しい偶発的効果をもたらす拡張コマンドは使いこなせない。

Perspective
----------------------------------------------------------------------

Envelop と同じだが、

   This extension requires the Numpy (Numerical Python) package.

という凝った物になっている。四角形パスの操作方法が参考になるので習得しよう：

   -略- in most cases, the quadrilateral path should be started from the
   lower-left corner and proceed in a clockwise direction. The :kbd:`Tab` key
   will cycle through the nodes in order when the *Node Tool* is in use. If no
   node is selected, then the starting node will be highlighted on the first use
   of the :kbd:`Tab` key. To change the starting node, break the path at the
   desired start node (v0.47) or one node before (v0.48) and then rejoin.

Pixelsnap
----------------------------------------------------------------------

ビットマップ書き出しをするときに絵がにじまないように補正する拡張コマンドだ。この
ように数値を精密に編集する：

   Filled objects are adjusted so that their edges are aligned with pixel
   boundaries. Paths are first adjusted to have an integer pixel width, and then
   adjusted so the stroke edges align with the boundaries.

一般的にはオブジェクトの移動を伴う。このコマンドを実行したら、そのオブジェクトに
はもう触らないようにする。

Rubber Stretch
----------------------------------------------------------------------

   Distorts a path as if the path was stretched vertically or the path was
   squeezed horizontally. The amount of the distortion is controlled by the
   Strength and Curve parameters. Adding extra nodes may produce a better
   result.

圧縮オチの作画の補助になるだろう。

Straighten Segments
----------------------------------------------------------------------

Flatten Bezier コマンドと似ているが、こちらは接線を変える：

   The amount of straightening can be specified. A :guilabel:`Behavior` value of
   1 moves the node handles toward the nodes, a value of 2 moves the node
   handles to a point one-third of the distance between the node and the
   neighboring node. There is little visual difference between these two
   options.

接線の長さを短くすることでノード間の曲線を平坦にしていくという考え方だ。

Whirl
----------------------------------------------------------------------

パスオブジェクトを点の周りにねじる。

   This extension twists an object around a point, like what might happen if you
   dropped things in whirling water (except the farther away from the center,
   the greater the displacement for this extension).

   The center of view is used for the center of the whirl. To whirl around the
   center of an object, select the object and then use :menuselection:`View -->
   Zoom --> Zoom Selection` (:kbd:`3`) to center the view on the object.

Raster
======================================================================

Raster 系拡張機能群はビットマップを操作する。

* GIMP のような本格的なビットマップエディターを使いたくないときに便利だ。
* 拡張機能はすべて ImageMagick に依存している。
* 拡張機能を適用すると、ビットマップは、変更された内部ビットマップに置き換わる。

   Note that these extensions only work on a bitmap. Some of the extensions can
   be duplicated by using *Filters* which also work on all objects and don't
   permanently change the bitmap file.

多重にラスター操作をする場合には、バックアップに何らかのフィルターを利用するとい
うことか。

Render
======================================================================

3D Polyhedrons
----------------------------------------------------------------------

照光処理があったからもしやと思ったら、やはりポリゴン（のイラスト）を描画する機能
がある。

   Selecting this extension pops up a dialog with three tabs. The first tab,
   :guilabel:`Model file`, controls the type of polyhedron that is specified in
   the :guilabel:`Object` drop-down menu. If :guilabel:`Load From` file is
   selected, the description in the file specified in the :guilabel:`Filename:`
   entry box is used. In the :guilabel:`Object Type` tab you can specify if the
   source file describes the object with edges or faces.

デモイラスト 1 のように出来合いのポリゴンを生成することも、上にあるように STL
ファイルなどを解釈して記述されているポリゴンを描画することも可能だ（いつもの
ティーポットで確認）。

   The second tab, :guilabel:`View`, allows you to rotate the polyhedron. Up to
   six rotations are allowed (for the mathematicians: why six when any unique
   rotation can be specified by only three orthogonal rotations?).

確かにクセのある UI だ。もっとも回転を三つ指定させるとしても筋が良いとは言えな
い。座標系が気になるが、その都度確認すればいいだろう。

   The third tab, :guilabel:`Style`, allows you to set all kinds of style
   parameters

この辺のオプションは 3D をやっている利用者ならば一見して見てわかる。問題ない。

Alphabet Soup
----------------------------------------------------------------------

   This extension generates exotic-looking text by recombining parts of
   characters from mostly the Latin alphabet in a way that the original text is
   discernible.

画像生成 AI が描きそうな文字を生成する拡張コマンドだ。入力文字列によっては
discernible でない出力が得られる。

Barcode
----------------------------------------------------------------------

この節の説明は :menuselection:`Extensions --> Render --> Barcode --> Classic...`
のもので、Inkscape 1.2 では :menuselection:`Datamatrix...` と :menuselection:`QR
Code...` が存在する。

Barcode — Datamatrix
----------------------------------------------------------------------

   This extension generates a Datamatrix barcode.

ダンジョンマスターの階層マップのような図像を生成するコマンドだ。

Calendar
----------------------------------------------------------------------

   祝日以外の全てが構成可能なカレンダー。その気になれば特定の日だけ色を手作業で
   変えればいいので、オリジナルグッズを作成したい人には有用か。

Cartesian Grid
----------------------------------------------------------------------

方眼紙を生成する。対数方眼紙も対応。両軸指定可。

   This extension generates Cartesian grids. Options include number of
   subdivisions, number of sub-subdivisions, linear versus logarithmic
   divisions, and line widths. For polar coordinates see *Polar Grid* extension.

メニュー項目は :menuselection:`Extensions --> Render --> Grids --> Cartesian
Grid...` だ。

Draw From Triangle
----------------------------------------------------------------------

   This extension is a geometrician's dream. It allows you to create an almost
   infinite number of constructions based on a triangle. The triangle is defined
   by the first three nodes in a path (even if the path is not a triangle). The
   path must be closed and the nodes connected by straight lines.

実際にコマンドを起動して :guilabel:`Draw From Triangle` ダイアログの各ダブを見る
と感動する。作図ツールとしての価値が高まった。

Foldable Box
----------------------------------------------------------------------

   This extension draws the pattern for a foldable box as one might use for the
   input in a desktop cutting plotter (after modifying the paths). The
   individual sides and tabs are each represented by separate paths which are
   all in a *Group*.

直方体紙パックの寸法を指定してその展開図を作図するコマンドだ。同時に変なガイド線
も生じる。

Function Plotter
----------------------------------------------------------------------

Matplotlib を引っ張り出す機会が減るか？

* 先に自分で矩形を描く。それからこのコマンドを起動する。
* 横軸を :math:`2\pi` の整数倍に整えるオプションがある。周期関数をプロットしやす
  い。
* 関数の一次微分を与えるオプションがあるのが興味深い。

   The function is plotted in the :abbr:`SVG` coordinate system, which has the
   y-axis upside down. The extension inserts a minus sign automatically to
   correct for this.

:guilabel:`Y value of rectangle's bottom` 値などで調整する。

   All Python math functions are allowed (as long as they return a single
   value), including Python random number functions. The :guilabel:`Help` Tab
   has a list of some of the available functions.

それよりもその左の :guilabel:`Functions` タブのほうがいい。

指定矩形を単位円の外接矩形とする極座標プロットも可能。その際の作法を知っている必
要がある：

   When the :guilabel:`Use polar coordinates` option is selected, the x-range is
   set to -1 at the left of the rectangle and +1 at the right side. The x values
   entered in the extension's dialog are used for the angle domain (in radians).
   The :guilabel:`Isotropic scaling` parameter is ignored. :guilabel:`Calculate
   first derivative numerically` must also be selected.

現代の環境で Python 2 系である可能性はもうゼロだと思う：

   Note that depending on the version, Python may return an integer if you
   divide two integers: thus, 4/5 = 0, while 4.0/5.0 = 0.8.

Gear
----------------------------------------------------------------------

イラストに示されているが、:guilabel:`Number of Teeth` を :math:`N`,
:guilabel:`Circular Pitch` を :math:`P`, ピッチ円半径を :math:`R` とすると次の等
式が成り立つ：

.. math::

   2\pi R = NP.

圧力角の普通の値は三つだ：

   14.5, 20, and 25 degrees.

Grid
----------------------------------------------------------------------

:menuselection:`Extensions --> Render --> Grids --> Grid...` コマンドだ。

   This extension fills the bounding box of an object with a grid. The grid
   spacing and offset can be independently set in the horizontal and vertical
   directions. The grid line width can also be set.

後から方眼紙を敷くという手順前後感がある。

Guides Creator
----------------------------------------------------------------------

ページ寸法に基づいて一定の規則でガイド線を引く拡張コマンドだ。等間隔だったり黄金
比だったり。比率だったり。

LaTeX Formula
----------------------------------------------------------------------

これは重要。利用する機会が必ずまた訪れる。しかし利用可能条件が Inkscape の外部に
ある：

   This extension turns a LaTeX string into a path. The string is typed into a
   dialog box. The extension requires that Ghostscript, LaTeX, and Pstoedit_ to
   be installed and in the execution path. Pstoedit_ must include the GNU
   libplot :abbr:`SVG` driver or the shareware :abbr:`SVG` plug-in, available
   for Windows at the Pstoedit_ website. The resulting formula is rendered as a
   path.

L-System (Fractal-Lindenmayer)
----------------------------------------------------------------------

これは使いこなせない。

Parametric Curves
----------------------------------------------------------------------

   This extension generates parametric curves. It was derived from the *Function
   Plotter* extension and shares many of its parameters.

ダイアログの UI がほとんど同じだ。

Perfect-Bound Cover Template
----------------------------------------------------------------------

:menuselection:`Extensions --> Render --> Layout --> Perfect-Bound Cover
Template...` で起動する。製本の表紙テンプレートを作成する拡張コマンドだ。ガイド
線を引く。

   The template sets the document to the correct size and creates guides for the
   front cover, back cover, and spine of the book, including the specified
   bleed.

ダイアログからいろいろと指定できるようでいて、長さ単位が固定の項目がある：

   The dialog allows for specifying a variety of parameters including the number
   of pages in the book and the thickness of each page. The extension is biased
   toward English measurements.

Polar Grid
----------------------------------------------------------------------

メニュー項目は :menuselection:`Extensions --> Render --> Grids --> Polar
Grid...` にある。

   This extension generates polar grids. Options include number of subdivisions,
   linear versus logarithmic divisions, line widths, and angle labels. For
   Cartesian coordinates see *Cartesian Grid* extension.

Printing Marks
----------------------------------------------------------------------

メニュー項目は :menuselection:`Extensions --> Render --> Layout --> Printing
Marks...` にある。印刷物の隅に目にすることがあるマークを生成する拡張機能だ。次の
オプションからなる：

   Options include generating crop marks, bleed marks, registration marks, star
   target, color bars, and page information.

   At the moment, the marks are generated “off” the page. The
   :guilabel:`Selection` option in the :guilabel:`Set crop marks to` drop-down
   menu in the :guilabel:`Positioning` tab does not work.

Inkscape 1.2 では選択オブジェクトに対しても機能する。

   Note that the printing marks are created on a locked *Layer* named
   :guilabel:`Printing Marks`.

なお、このコマンドには Live Preview 機能がない。

Random Tree
----------------------------------------------------------------------

   Draw a random tree made of straight-line segments. This is a classic from
   *Turtle Geometry*. This implementation is rather limited.

使わない。

Spirograph
----------------------------------------------------------------------

   Draw a Spirograph; that is, an epitrochoid or hypotrochoid curve.

   * `Epitrochoid -- from Wolfram MathWorld <https://mathworld.wolfram.com/Epitrochoid.html>`__
   * `Hypotrochoid -- from Wolfram MathWorld <https://mathworld.wolfram.com/Hypotrochoid.html>`__

使う半径は三つある：

.. csv-table::
   :delim: |
   :header-rows: 1
   :widths: auto

   引数 | 意味
   :guilabel:`R - Ring Radius` | 固定円の半径
   :guilabel:`r - Gear Radius` | 運動円の半径
   :guilabel:`d - Pen Radius` | 描画点の半径

次に hypotrochoid か epitrochoid かを指定する：

   In addition, one must choose if the *Gear* travels *Inside* or *Outside* the
   *Ring*.

残りのオプションは適当に。

   The ratio of “r” to “R” determines the structure of the curve. Take, for
   example, an “r” of 36 and an “R” of 48. The ratio reduced to its simplest
   form is 3/4. This indicates that the *Gear* will make a total of four “loops”
   as it circles the *Ring* three times. Simple ratios make simple curves.

この手の周期的パラメトリック曲線によく見られる比の考え方だ。この分母が偶数のもの
については図形の中央が塗りつぶされない：

   If you use an Even-odd fill rule, the center of the figure will be unfilled
   if the denominator is even.

無理数になることはないのだが、それに近づけることは当然可能だ。そうなるとなかなか
ループが一周しない。その際、この拡張機能は次のように振る舞う：

   Unlike the case with a real Spirograph that utilizes plastic gears, it is
   possible to specify values of “r” and “R” that don't form a rational number
   ratio. In this case, the curve never closes on itself and is of infinite
   length. To avoid such infinities, the extension limits the number of nodes to
   1000. If the numerator or denominator of the ratio in the simplest form is a
   large integer, the *Spirograph* may run out of nodes.

対処法は：

   In this case, decreasing the :guilabel:`Quality` may help.

実機では作図できないような半径を与えて作図することも可能だ：

   Also, unlike a “real” Spirograph, the *Spirograph* extension allows “d” to be
   greater than “r”. This results in small loops along the *Ring*.

Triangle
----------------------------------------------------------------------

辺の長さ and/or 頂点の角度を必要なだけ指定して三角形を作図する拡張機能だ。

   Although there are six parameter entry boxes, only three are used at any one
   time. Which three are used is specified in the :guilabel:`Mode` drop-down
   menu. Side *c* is always at the bottom.

:guilabel:`From Three Sides` や :guilabel:`From Sides a, b and Angle c` などの
モードがある。一意に定まらなそうな選択肢が紛れ込んでいる気がする。

Wireframe Sphere
----------------------------------------------------------------------

球を緯線や経線を描くことで表現する機能だ。

   This extension generates a wire frame sphere using ellipses to represent
   lines of latitude and longitude. The number of lines can be specified as well
   as the orientation of the sphere. An option allows the removal of hidden
   lines.

Text
======================================================================

Convert to Braille
----------------------------------------------------------------------

ASCII テキストを点字に置換する拡張コマンドだ。正常に機能するためには環境が整って
いる必要がある：

   Note: you must have a font that has Unicode Braille glyphs installed on your
   system (e.g. Deja Vu Sans). Windows users may need to explicitly select that
   font.

確かに DejaVu Sans 系字体を指定するとそれらしい点字が出力される。

Lorem Ipsum
----------------------------------------------------------------------

Lorem Ipsum 文字列を生成して矩形に流し込むコマンドだ。

   The text is generated into a *flowed text box*. If no *flowed text box* has
   been defined, one is created on a new *Layer* with the size of the page.

前者の方式がコマンド用途からすれば自然だ。

Replace Text
----------------------------------------------------------------------

文字列置換コマンド。図面内にあるテキストオブジェクトすべてに対して一括置換する場
合に使える。

Split Text
----------------------------------------------------------------------

この拡張コマンドに関しては、次の助言に従うべきだろう：

   The use of this extension is normally not recommended. By splitting text into
   separate parts, the semantics of the text is lost. For example, it can no
   longer be selected as one unit in a web browser or indexed by search engines.
   :abbr:`SVG` has been designed to allow text to be manipulated (e.g.
   individual letters or words having different styles) without losing the
   semantic value. It is better to rely on these :abbr:`SVG` features than to
   break apart text.

Change Case
----------------------------------------------------------------------

:menuselection:`Extensions --> Render --> Text --> Change Case` サブメニューにコ
マンドがある。一般的なテキストエディターにない変換があるのは創作用途か。

* :menuselection:`fLIP cASE`
* :menuselection:`lower case`
* :menuselection:`rANdOm CasE`
* :menuselection:`Sentense case`
* :menuselection:`Title Case`
* :menuselection:`UPPER CASE`

Visualize Path
======================================================================

Dimensions
----------------------------------------------------------------------

   Adds :abbr:`CAD`-style dimension arrows to an object. In v0.47, this
   extension only works on paths; in v0.48, it also works on *Shapes* and
   *Groups*. It uses an object's bounding box to determine placement of arrows.
   The arrows and original object are placed inside a *Group*.

矢印だけが描かれるので、長さそのものを表すテキストが欲しいならば自前で用意せねば
ならない。それなら本当に :abbr:`CAD` を使えという話だ。

Draw Handles
----------------------------------------------------------------------

   This extension draws the handle lines that one would see if editing the nodes
   of a path. It would be of more use if it included the drawing of the handle
   and node symbols.

接線ベクトルだけを作図すると考えていい。

Measure Path
----------------------------------------------------------------------

   This extension measures the length or area (added in v0.48) of a path,
   printing the length or area alongside the path

Dimensions はこれと組み合わせて使えばいい。

Number Nodes
----------------------------------------------------------------------

   This extension numbers the nodes of a path. It is useful for creating an
   old-fashioned *Connect-the-Dots* puzzle. (It is also an example of how to
   access the path data in an :abbr:`SVG` file for writing your own extension.)
   The original path is turned into a path with no stroke but with dot markers.
   The dots are then numbered.

パスを添字付き点列に変換するコマンドとして捉えたい。

Web
======================================================================

Web で使用する :abbr:`SVG` を用意するのに使いたい拡張コマンドだ。

JavaScript
----------------------------------------------------------------------

   This submenu has two entries. The first allows events linked to one object
   (mouse over, clicking on, etc.) to control the attributes of another object.
   The second allows events linked to one object to transmit that object's
   attributes to another. These extensions embed JavaScript into the :abbr:`SVG`
   file. The JavaScript comes from the InkWeb package.

イベントハンドラーを実装する機能を期待しているのだが、この記述からはそう読み切れ
ない。

Set Attributes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   This extension creates the JavaScript so that an action (clicking on, mouse
   passing over, etc.) with one object changes the attributes of another object.

オブジェクトが二つ関係することを押さえる。

   The list of attributes to change is entered, separated by spaces, in the
   :guilabel:`Attribute to set` entry box (e.g., ``fill stroke stroke-width``).

:abbr:`SVG` 要素の属性名を指定すればいいようだ。

   The action that will cause the change is set in the :guilabel:`When the set
   must be done` drop-down menu.

メニューは ``on click`` や ``on mouse over`` のように、JavaScript イベントに明ら
対応している名前の項目からなる。

   The list of new values is entered, separated by spaces, in the
   :guilabel:`Value to set` entry box. The list of values must match the
   :guilabel:`Attributes to set line` (e.g., ``green black 2px``).

この UI ならそうだろう。

   The next option specifies if this action should come before, after, or
   replace any previously defined actions. The final option determines, in the
   case where more than two objects are selected, if the first selected object
   controls all the other selected objects or if the last selected object is
   controlled by actions on all the other selected objects.

この記述の意味がわからない。

----

デモを検証する。オブジェクト二つを選択してから当コマンドを起動する。それから次の
ように指定する：

.. csv-table::
   :delim: |
   :header-rows: 1
   :widths: auto

   項目 | 値
   :guilabel:`Attribute to set` | ``fill stroke stroke-width``
   :guilabel:`When the set must be done` | ``on click``
   :guilabel:`Value to set` | ``green black 5px``

すると最初のオブジェクトをクリックすると、次のオブジェクトの色が緑に変わり、境界
線の幅が 5px に変わるという。

図面を XML Editor で確認すると、それを実装している JavaScript コードを含む
``svg:script`` 要素ができている。コードの品質は高いとは言えない。そして選択オブ
ジェクトに対応する図形ノードに ``onclick`` 属性が付与されている。値は短い
JavaScript コードだ。

Transmit Attributes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Set Attributes* 拡張コマンドの属性値複製版だ。

   This extension creates the JavaScript so that an action (clicking on, mouse
   passing over, etc.) with one object changes specified attributes of another
   object to have the same value as the first.

UI もほぼ同じ。

Web Slicer
----------------------------------------------------------------------

   This extension facilitates slicing a drawing into rectangular bitmaps for use
   in Web pages. It will optionally export :abbr:`CSS` and :abbr:`HTML` code for
   use with the bitmaps.

Inkscape で製図した :abbr:`SVG` を丸ごと使うのではなく、ウェブブラウザーに乗せる
ために部分を切り出すということか。

   There are two steps in using this extension. First, the :guilabel:`Create a
   slicer rectangle` dialog is used to define a set of named rectangles for the
   areas that are to be exported.

矩形は複数定義できる。それぞれ別のフォーマットを指定することもできる：

   Each rectangle can specify a different target format (:abbr:`PNG`,
   :abbr:`JPEG`, or :abbr:`GIF`) and optionally, a background color. The
   rectangles are stored in a separate *Layer* named :guilabel:`Web Slicer`.

矩形が完成したらエクスポートを専用ダイアログで実施する：

   After defining the rectangles, the rectangle regions are exported using the
   :guilabel:`Export layout pieces and HTML+CSS code` dialog. A third dialog can
   be used to add attributes in the HTML.

Create a rectangle dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

矩形を二段階で定義することになる。

   The dialog consists of a number of entry boxes for specifying export
   rectangles. Note that the placement of the rectangle is not defined in this
   dialog. After clicking the :guilabel:`Apply` button, a partially opaque
   rectangle will be created. You move and resize this rectangle to cover the
   area that should be exported.

ダイアログ主要部分の入力項目は次のとおり：

:guilabel:`Name`
   エクスポート矩形の名前。
:guilabel:`Format`
   ``PNG``, ``JPG``, ``GIF`` から指定。
:guilabel:`DPI`
   ビットマップ解像度。
:guilabel:`Force dimension`
   ビットマップの正確な寸法（ピクセル単位）。これを指定すると DPI は無視される。
:guilabel:`Background color`
   矩形背景色。Inkscape の図面画面では塗りつぶし色としては使われない。

ダイアログ副部分にはタブが三つある：

   Three tabs allow additional parameters to be specified. Note that the
   :guilabel:`HTML` tab specifies attributes that apply to the export rectangle.

Export layout pieces and HTML+CSS code dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   This dialog allows you to specify where the output files should be stored and
   if :abbr:`HTML` and :abbr:`CSS` code should be produced. Note that the
   :abbr:`HTML` and :abbr:`CSS` code is not intended to be the final product but
   instead allows you to quickly check the output and to generate code that can
   be pasted into other files. Clicking the :guilabel:`Apply` button does the
   actual export.

.. admonition:: 読者ノート

   手許の Inkscape 1.2 では残念ながら Python がエラーで終了する。検証不能。

Set a layout group dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   All of the attributes applied to the rectangles and :abbr:`HTML` export are
   stored in ``<svg:desc>`` tags. These tags are not easy to edit via the
   :guilabel:`XML Editor` dialog. It may be easier to edit the :abbr:`SVG` file
   in a text editor.

どう難しいのかわからない。右側のテキストエリアで普通に編集できそうだが。

.. _Pstoedit: https://www.pstoedit.com/
.. _YUV: https://en.wikipedia.org/wiki/YUV

