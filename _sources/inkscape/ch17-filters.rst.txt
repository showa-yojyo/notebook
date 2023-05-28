======================================================================
Chapter 17. Filter Effects - Custom
======================================================================

.. contents::

Basic Use
======================================================================

   *Filters* can be defined and applied through the :guilabel:`Filter Effects`
   dialog. The :guilabel:`Gaussian Blur` filter can also be used directly
   through the :guilabel:`Fill and Stroke` dialog. The :guilabel:`Blend` filter
   can also be applied to an entire *Layer* through the :guilabel:`Layers`
   dialog.

メインメニューから :menuselection:`Filters --> Filter Editor...` を選択すると、
このダイアログが出現する。ここに挙げられた二つのフィルターは、他の UI からも操作
可能ということで先に述べられているのだろう。

   The :guilabel:`Fill and Stroke` dialog has a :guilabel:`Blur` slider that
   when moved from zero, creates and attaches a *Gaussian Blur* filter to
   selected objects. If the slider is reset to zero, the filter is automatically
   removed and deleted.

ぼかし効果は :guilabel:`Fill and Stroke` ダイアログの下にある専用スライダーで設
定可能。値をゼロにすればフィルターが削除されたことになる。使い勝手が良い。

   The same principle works on the :guilabel:`Layers` dialog where a choosing
   anything but :guilabel:`Normal` creates a *Blend* filter and attaches it to
   the *Layer*. Setting the drop-down menu back to :menuselection:`Normal`
   deletes the filter.

そもそも :guilabel:`Layers` ダイアログが存在しない。

フィルターを削除するためのメニュー項目がある：

   *Filters* can also be removed from an object by using the menu entry
   :menuselection:`Filters --> Remove Filters`.

:guilabel:`Filter Effects` ダイアログの用途は二つある：

#. 原始的フィルターから複雑なフィルターを組み立てる
#. オブジェクトにフィルターをかける

原始的 *Filter* に対する入力として使用されるグラフィックの源は、別の原始的
*Filter* による出力または次のいずれかとある：

   * :guilabel:`Source Graphic`. Use the object as the source for the *Filter*
     primitive.
   * :guilabel:`Source Alpha`. Use the *Alpha* of the object as the source for
     the Filter primitive.
   * :guilabel:`Background Image`. Use the region under the *Filter* at the time
     the *Filter* is invoked.
   * :guilabel:`Background Alpha`. Use the *Alpha* of the region under the
     *Filter* at the time the *Filter* is invoked.
   * :guilabel:`Fill Paint`: Not implemented. Use the *Fill* of the target
     object as the input to a *Filter* primitive as if the object had an
     infinite extent. Useful if the *Fill* is a *Gradient* or *Pattern* with
     transparent or semitransparent regions.
   * :guilabel:`Stroke Paint`: Not implemented. Use the *Stroke* of the target
     object as the input to a *Filter* primitive (see :guilabel:`Fill Paint`
     above).

フィルターは対象オブジェクトの占める領域そのものではなく、それに対して相対的に定
まるある領域にかかる。これを本文では *Filter Effects Region* と呼んでいる：

   By default, the *Filter Effects Region* ranges from -0.1 to 1.1 in units of
   the object's bounding box width and height. This area may not always be
   sufficient. For example, if a large shift is prescribed in the *Offset*
   filter, the area must be increased.

フィルター効果領域を数値指定することが可能だ：

   The area can be adjusted under the :guilabel:`Filter General Settings` tab of
   the :guilabel:`Filter Effects` dialog. (It can also be set through the
   :guilabel:`XML Editor` dialog, attributes *x*, *y*, *width*, and *height*.)

Filter Effects Dialog
======================================================================

:guilabel:`Filter Effects` ダイアログの操作方法が述べられている。新規とエフェク
ト追加がややこしい。

Adding a Filter
----------------------------------------------------------------------

新規作成ボタンを押してフィルター項目を追加するか、既存のフィルターを複製して名前
を変えて（現在の図面で利用可能な）フィルターを追加する。

   Click on the :guilabel:`New` button on the left to add a new filter.
   Alternatively, right-click on an existing filter in the :guilabel:`Filter`
   list to duplicate it. The name of the filter can also be changed by clicking
   on the name.

Defining a Filter
----------------------------------------------------------------------

:guilabel:`Filter Effects` 右下区間のヘッダー部分はボタンとドロップダウンリスト
からなることに注意。Inkscape の UI はボタンがわかりにくいことが多い。

   A filter is defined by selecting filter primitives from the drop-down list
   next to the :guilabel:`Add Effect` button. A short description of the filter
   is displayed when a filter is selected. The description can be toggled on or
   off under the :guilabel:`Filters` tab of the Inkscape :guilabel:`Preferences`
   dialog.

適当な原始的フィルターをドロップダウンリストから選んで左のボタンを押すと、ダイア
ログ右上区画の内容が更新する：

   Once a primitive is selected, click on the :guilabel:`Add Effect` button to
   add it to the filter. The input(s) of the filters are automatically attached
   to the :guilabel:`Source Graphic` or the output of a previously added filter
   primitive.

次の記述がまだわからない：

   The default connections are shown as gray lines originating from a triangle
   right of the filter primitive name. Explicitly defined connections are shown
   in black.

矢印の三角部分をドラッグすると、なぜか始点部分を右にある別の列に割り当て直せる：

   The inputs of a filter can be reassigned by click-dragging from the triangle
   at the right of the filter name to one of the columns on the right (e.g.,
   :guilabel:`Source Graphic`), or by click-dragging to another of the filter
   primitives.

原始的フィルターの順序入れ替えを直感的な操作で行える：

   The filter primitives can be reordered by click-dragging a filter primitive
   in the list to another place in the list.

フィルター効果を微調整することが図面の描画の乱れを生じた場合には、適当に再描画さ
せてやればよいようだ：

   Inkscape may fail to update the display when tweaking *Filter Effects*
   parameters. Nudging the object up and down is sufficient to force an update.

Applying a Filter
----------------------------------------------------------------------

   To apply a filter to an object(s), select the object(s) and check the box
   next to the filter name. Uncheck the box to remove a filter. If multiple
   objects are selected with different filters, all the boxes corresponding to
   those filters will be checked.

選択状態のオブジェクトが存在しないとチェックボックスは操作不能であり続けるよう
だ。

Mini Tutorial - A Drop Shadow
======================================================================

この節に関して気になることがあれば、もう本書を再読して欲しい。

   Drop shadows are a perfect use for filters. The shadow automatically updates
   when the source object changes. Here is a step-by-step tutorial on creating a
   drop shadow:

.. raw:: html

   <object class="svg" data="../_images/dropshadow.svg" type="image/svg+xml"></object>

* :guilabel:`Source` が変更された場合、自動的にドロップシャドウも更新がかかる。
* テキストに対して複合フィルターを作成することになる。
* :guilabel:`Gaussian blur`, :guilabel:`Offset`, :guilabel:`Merge` の三つを使
  う。矢印の設定に注意。

Color Filter Primitives
======================================================================

:abbr:`RGBA` 値の行列による変換と考えてよい。OpenGL のアレっぽい。

Color Matrix
----------------------------------------------------------------------

色行列は :abbr:`RGBA` 列ベクトルに左から乗じて別の :abbr:`RGBA` 列ベクトルに変換
するような五次正方行列だ（本書参照）。座標変換行列の類比で言うと並進移動項がある
ので、本書のような成分構成になる。

   Four types of transformations are defined, of which three are special classes
   of the first.

というわけで見ていこう：

:guilabel:`Matrix`
   行列の有効成分全てを完全に指定する。一般的な場合。
:guilabel:`Saturate`
   彩度を下げるには、数 :math:`{s \in [0, 1]}` を一つ指定する。:abbr:`RGB` 値の
   みが変化する。公式は本書参照。
:guilabel:`Hue Rotate`
   数値一つを指定することで色相をずらす。これもまた :abbr:`RGB` 値のみが変化す
   る。正確な計算式はかなり複雑で、赤→黄→緑→右…と回転していくだけではない。
:guilabel:`Luminance to Alpha`
   輝度は一定の計算式でアルファーに変換される。公式は本書参照。

:abbr:`RGB` 対角行列の要素 :math:`a_{00}, a_{11}, a_{22}` を :math:`-1` にし、五
列目の上位三要素 :math:`a_{04}, a_{14}, a_{24}` を :math:`1` とすることで明暗を
逆転した変換を作成することができる。

Component Transfer
----------------------------------------------------------------------

   Partially implemented, No user interface.

概要を覚えるに留める：

   The *Component Transfer* primitive changes the :abbr:`RGB` and *Alpha* of an
   object by applying independent functions to each of the :abbr:`RGB` and
   *Alpha* input values. The following modes for defining the functions are
   available: *Identity*, *Table*, *Discrete*, *Linear*, and *Gamma*.

Compositing Filter Primitives
======================================================================

原始フィルターは複数組み合わせて graphics を合成するものだ。

   These primitives composite two or more graphics. The graphics may be from an
   object, a background, or the output of another primitive.

``enable-background`` タグの扱いにバグがあるらしい。しかし、下記の回避策はレイ
ヤーダイアログが存在しない Inkscape 1.2 では採用不能か：

   Inkscape has a problem in using one of these filters. When using either
   :guilabel:`Background Image` or :guilabel:`Background Alpha` as an input to
   the filter, the ``enabled-background`` tag must be added to the :abbr:`SVG`
   file (this tells :abbr:`SVG` renderers to keep a copy of the background in
   memory). This is not done. A work-around is to use the :guilabel:`Layers`
   dialog to add a *Blend* filter to a *Layer*. The *Layer* blend can then be
   removed, leaving the necessary tag in place.

:abbr:`SVG` 1.1 の仕様にバグがあって、透明度のある背景で合成すると、それが二重に
なるというものだ。それを回避する方法を自明な回避策を含め三つ紹介している：

   The first is to avoid using a :guilabel:`Background Image` or
   :guilabel:`Background Alpha` as a filter input.

第二の方法は、アルファー値最大の :abbr:`RGBA` 値を持つ色で置き換えることだ。この
方法はフィルター合成問題に関係なく、知っていて損はない：

   The second is to replace a transparent background with a solid background
   (you can use the *Dropper Tool* to replace a transparent :guilabel:`Fill`
   with an equivalent solid :guilabel:`Fill` [turn off :guilabel:`Pick alpha` in
   the *Tool Controls*]).

第三の方法は白背景からマージフィルターで開始するものだ。最終出力に透過部分を含ま
せたい場合には使えない：

   The third is to use the *Flood* filter to create a solid white background and
   include this as the first input to a *Merge* filter (if using a *Merge*
   filter, include the flood first; if using a *Blend* or *Composite* filter,
   add a *Merge* filter with the first input being the output from the *Flood*
   filter and the second input being the output from the *Blend* or *Composite*
   filter). This solution runs into trouble when it is desired that the overall
   image have transparency.

   The :abbr:`SVG` 1.2 standard corrects this deficiency.

Inkscape が出力する :abbr:`SVG` ファイルはエディターで確認すると 1.1 のままのは
ず。

Blend
----------------------------------------------------------------------

真っ先に習うべき原始フィルターはブレンドで間違いない。

   The *Blend* primitive blends two overlapping objects or an object with its
   background by doing a pixel-by-pixel combination using one of five defined
   blend modes. The five modes are listed below. Except for the *Normal* mode,
   the result is independent of which object is on top.

まず記号を定義しておく：

* 添字 :math:`a` および :math:`b` を重なるオブジェクト同士のそれぞれ上下のものを
  指すのに用いる。
* 添字 :math:`r` で結果を表す。
* :math:`{c \in [0, 1]}` をオブジェクトの :abbr:`RGB` 値とする。A 値は込められて
  いる。
* :math:`{q \in [0, 1]}` をオブジェクトの A 値とする。

:guilabel:`Normal`
   フィルターが存在しないかのように、上のオブジェクトは下のオブジェクトの前にあ
   る。

   .. math::

      c_r = (1 - q_a)c_b + c_a.

:guilabel:`Multiply`
   上オブジェクト色が下オブジェクト色になっている透明なものを通して見える。

   .. math::

      c_r = (1 - q_a)c_b + (1 - q_b)c_a + c_a c_b.

:guilabel:`Screen`
   上オブジェクト色が下のそれに光を加える。上下のオブジェクトがそれぞれ独立して
   スクリーンに投影されているようなもの。

   .. math::

      c_r = c_b + c_a - c_a c_b.

:guilabel:`Darken`
   上のオブジェクトが下のオブジェクトを暗くする。

   .. math::

      c_r = \min\{(1 - q_a)c_b + c_a, (1 - q_b)c_a + c_b\}.

:guilabel:`Lighten`
   上のオブジェクトが下のオブジェクトを明るくする。

   .. math::

      c_r = \max\{(1 - q_a)c_b + c_a, (1 - q_b)c_a + c_b\}.

.. admonition:: 読者ノート

   本書のイラスト二つを自分で再現して納得なり理解なりすること。

   :guilabel:`Screen` と :guilabel:`Lighten` が似ている理由を説明できるようにな
   ること。

Composite
----------------------------------------------------------------------

   The *Composite* filter primitive allows two overlapping objects or an object
   and background to be merged pixel-by-pixel according to a mode-dependent
   rule.

このモードでは前述の背景が二重に考慮される不具合に注意すること：

   See the introduction to this section for problems when using a background as
   one of the inputs.

:guilabel:`Over`
   The upper object is placed over the lower object. This is equivalent to the
   normal way overlapping objects are drawn.
:guilabel:`In`
   下オブジェクトが上オブジェクトの残留部分を決める。
:guilabel:`Out`
   下オブジェクトが上オブジェクトの消滅部分を決める。
:guilabel:`Atop`
   :guilabel:`In` かつそうでない下オブジェクト部分が見える。
:guilabel:`Xor`
   上下オブジェクトの非共通部分が見える。
:guilabel:`Arithmetic`
   :math:`i_1, i_2` をオブジェクトの入力値とし、さらに値 :math:`K_k` を指定して
   次の式で決める：

   .. math::

      K_1 i_1 i_2 + K_2 i_1 + K_3 i_2 + K_4.

Merge
----------------------------------------------------------------------

*Merge* は特に三つ以上の原始フィルターの結合を z-order に従って順次行うフィル
ターだ。その原理は単純だ：

   The *Merge* filter allows the combining of two or more objects or outputs of
   filter primitives. It works by layering one image on top of another, much as
   regular objects are layered on top of each other in z-order, or, for the case
   of two inputs, as the *Composite* filter primitive using the :guilabel:`Over`
   mode.

Fill Filter Primitives
======================================================================

フィルター領域に対して何らかの塗りつぶしを施す原始フィルターをいくつか見ていく。

Flood
----------------------------------------------------------------------

   The *Flood* primitive fills the *Filter Effects Region* with a specified
   color and opacity. This filter primitive is most useful when combined with
   other filters primitives.

せっかくフィルター加工した領域をベタ塗りするのかと感じられる。そこで本書で例示さ
れている工程は、前節で紹介された *Composite In* とパターン塗りつぶしなどを組み合
わせて意味のある効果を実現していることがわかる。

Image
----------------------------------------------------------------------

   Partially Implemented.

Inkscape 1.2 でも未完全実装であるかを確認したい。

   The *Image* primitive renders an external graphics file or an internal
   :abbr:`SVG` object. It allows more than one object to be referenced in a
   complex filter (the first being the object attached to the filter).

JPEG ファイルや PNG ファイルを描画させることが可能であるのはもちろん、同一図面内
の :abbr:`SVG` オブジェクトでもよい。

   Unfortunately, this very useful filter primitive is not yet fully implemented
   in Inkscape with only external images supported.

「部分的に実装されていない」というのは、この :abbr:`SVG` 参照の機能のことだろう。

   The :abbr:`GUI` will create a reference with an absolute path to the external
   image. Use the :guilabel:`XML Editor` to change an absolute path to a
   relative one if required.

相対パスが実は指定可能であることをよく憶えておく。*Image* フィルターを使っている
:abbr:`SVG` ファイルをバージョン管理するなら変更必須だ。

画像は対象の BB に収まるように拡縮されるのが普通だ：

   By default, the image is shrunk or stretched to fit inside the bounding box
   of the object to which the filter is attached.

   The placement of the image within the bounding box can be controlled using
   the parameters *x*, *y*, *width*, and *height*. The coordinate system is the
   same as used for the object. The :guilabel:`XML Editor` must be used to
   modify these parameters. An additional parameter, *preserveAspectRatio*, is
   not supported by Inkscape.

縦横比固定オプションらしきものも未対応だ。残念。

   The *Image* implementation in Inkscape does not correctly position images.
   Other :abbr:`SVG` renderers will display the image differently from Inkscape
   as a result.

これはブラウザーで試験できる。

Tile
----------------------------------------------------------------------

   Not implemented.

   The *Tile* primitive fills a rectangular region with a repeated input image.

CSS でいう ``background-image: repeat`` に相当するものだ。

Turbulence
----------------------------------------------------------------------

*Turbulence* は大理石の表面や雲のような人工的テクスチャーを作成する用途の原始
vフィルターだ。

   The *Turbulence* primitive allows the creation of artificial textures such as
   marble surfaces or clouds. It is based on the work of Ken Perlin who won an
   Academy Award for creating realistic textures with computers.

Perlin 氏の方法を簡略化したものを実装しているようで、ある区間でランダムな強度を
生成し、その点を滑らかにつなげるというものだそうだ：

   Perlin solved the problem of using random numbers to produce smooth random
   fluctuations in color. A simplified version of his method is to generate
   random intensities at given intervals and then connect these points smoothly
   together.

ブラウザーの一部はフィルターの特定の属性を修正しないと Inkscape と異なる描画結果
を生じる：

   Note that Firefox, Opera, and Batik will render this filter differently than
   Inkscape if the attribute ``color-interpolation-filters="sRGB"`` is not added
   to the filter definition.

   The :abbr:`RGB` and *Alpha* components are each derived separately.

:guilabel:`Type` では二つから選択する：

   The :guilabel:`Type` menu can be set to either :guilabel:`Fractal Noise` or
   :guilabel:`Turbulence`. :guilabel:`Turbulence` tends to have more dramatic
   dark regions as the absolute values of the noise terms are used, creating
   “visual cusps”.

ノイズ項の絶対値が大きくなるにつれ暗部を劇的に有するようになり、視覚的尖りが生じ
がちだ。

ノイズは画面解像度に依存する：

   The *Base Frequency* is defined by default in terms of inverse *Screen*
   pixels. For example, a frequency of 0.1 would have a “wave length” of 10
   pixels. Inkscape cannot yet create resolution independent noise.

まるで音楽理論を読んでいるようだ。和音が多いと調和が失せるようなもので、空間と色
の変化が見えなくなるほど小さくなり過ぎる。:abbr:`CPU` にもやさしくない：

   The number of *Octaves* determines the complexity of the noise, the more
   *Octaves*, the more complex. Each *Octave* adds a term with twice the
   *Frequency* but half the amplitude. Using more than four or five *Octaves*
   isn't so useful as the spatial and color variations become too small to be
   seen (and increases the :abbr:`CPU` load).

このフィルターは疑似乱数生成器を用いる。原理的には :abbr:`SVG` ビューワーが異
なっていても同じ生成器をなるべく使い、同じ模様をなるべく生じるようにする：

   If you use the filter twice on two identical objects, the textures should be
   the same. Changing the seed will force the random-number sequence to be
   different and thus the textures will be different too.

Lighting Filters Primitives
======================================================================

ここで扱うフィルターを記述するのに 3D グラフィックス理論の Phong 照光処理の術語
を用いる。

   Two primitives, *Diffuse Lighting* and *Specular Lighting*, are included to
   simulate light shining on objects. They represent two of the three parts of
   the Phong reflection model for modeling light in computer graphics.

環境光、拡散光、鏡面光の説明を見ていく。環境光だけは :abbr:`SVG` との関係が述べ
られている：

   Ambient light: The light present everywhere in a scene. In :abbr:`SVG` this
   would be represented by a solid *Fill*.

拡散光と鏡面光の説明は、一般の CG 理論のそれと同じように述べられている。本ノート
では割愛。

   An illustration of the components of the Phong model.

このドーナツのイラストで注意することは、拡散と鏡面の赤い光源が画面左上の無限遠点
にあるらしいということだ。ここでは背景は無視する。

Phong モデルは ray tracing をしない。

   The contour of an object in the z (out of the drawing) direction is described
   by a *bump map* that is defined by the *Alpha* channel of an object. The
   values of the pixel and the neighboring pixels in the *bump map* define the
   normal to the surface for the pixel.

バンプマップとしてオブジェクトのアルファー値を利用する。これが照光処理の急所であ
る法線方向を決定する。

   The two lighting filters share in common most of their attributes such as the
   type of light source, its color, and its position; thus we'll discuss them
   together.

:dfn:`Diffuse Color`, :dfn:`Specular Color`
   光源色。
:dfn:`Surface Scale`
   表面への法線を計算するための縮尺。数値は表面の最大高（アルファー値 1 に対応）
   を座標系単位で表す。
:dfn:`Diffuse` or :dfn:`Specular Reflection Constant`
   表面に当たった光のうち、どの程度が拡散 or 鏡面反射されるか。
:dfn:`Exponent`
   （鏡面照光のみ）鏡面反射の鋭さすなわち狭さを決定する。最小値は 1.0 で、反射が
   広く鈍い表面となり、反対に値が大きくなると反射が狭くなり、より洗練された表面
   となる。
:dfn:`Kernel Unit Length`
   未使用らしい。
:dfn:`Light Source`
   次のいずれか：

   * :dfn:`Distant Light`
   * :dfn:`Point Light`
   * :dfn:`Spot Light`

   When applying a lighting filter with a large *Surface Scale*, the limited
   resolution of the *bump map* may create artifacts. These can be removed by
   applying a small amount of *Gaussian blur* to the image.

ちらつきをごまかすちょっとした手筋だ。本書次のイラストはその採用例を示している。

Distant Light Source
----------------------------------------------------------------------

   無限遠点からの光線を表現するには、次の属性二つを定義する：

:dfn:`Azimuth`
   方位角。描画面における光源の方向角。角度は水平軸 (x) から右回りに定義す
   るという、Inkscape ではイレギュラーな測定方法による。
:dfn:`Elevation`
   標高。図面平面上方にあるとされる光源の方向角。

イラストでは球を模したオブジェクトが列になっている。無限遠点からの光を浴びている
ので、どれもハイライトとシェードが同じような見てくれになる。結果的に球全体も同じ
見てくれになる。

Point Light Source
----------------------------------------------------------------------

光源の座標を z 成分も含めて直接指定する。本書のイラストで十分説明できている。

Spot Light Source
----------------------------------------------------------------------

点光源に円錐の傘をかぶせたようなモデルだと考えていい。円錐の幾何データを設定する
必要がある：

   This light source simulates a point light source near an illuminated object
   but with a limited cone of light. One triple set of numbers (x, y, z) is
   required to set the *Location* of the light and another to set the direction
   the center of the cone points (*Points At*).

   The *Specular Exponent* sets how well-focused is the light; the higher the
   value, the more sharply focused the light. The *Cone Angle* (degrees) defines
   the maximum angle for the light.

本書のイラストにスポットライトの傘をオーバーレイしたいところだ。

Pixel Manipulation Filter Primitives
======================================================================

   These primitives move pixels or blend adjacent pixels.

ということはこの節の原始フィルターは畳み込みではないかと思う。

Convolve Matrix
----------------------------------------------------------------------

やはりそうだった。

   The *Convolve Matrix* primitive uses neighboring pixels to modify the color
   of a pixel. How the pixel is changed is determined by an :math:`{N \times M}`
   matrix with one entry for each neighboring pixel.

この数式を見ると、行列の中身の和に違和感があるが読み進める。

   The following is an example of a “Gaussian Blur” that uses a :math:`{5 \times
   5}` matrix around the center pixel. The :guilabel:`Kernel` is an integer
   representation of a 2-dimensional *Gaussian* with a standard deviation of 1.4
   pixels. It is normalized by the :guilabel:`Divisor`.

当フィルターの :guilabel:`Effect parameters` の構成は次のとおり：

:guilabel:`Size`
   行列 *Kernel* の寸法。
:guilabel:`Target`
   どの行列成分が対象画素に対応するか、既定では対象画素に *Kernel* を中央合わせ
   する。
:guilabel:`Kernel`
   行列 *Kernel* の全成分。
:guilabel:`Divisor`
   行列 *Kernel* の全成分をこの値で除算する。
:guilabel:`Bias`
   行列乗算の後に加算する値。
:guilabel:`Edge Mode`
   入力画像を拡張して、境界部分の画素を評価できるようにする方式。

   .. csv-table::
      :delim: |
      :header: 名前,方式
      :widths: auto

      :guilabel:`Duplicate` | 全端の画素を複製
      :guilabel:`Wrap` | 足りない画素を入力画像の逆側から取得
      :guilabel:`none` | ゼロ画素を使う

   Inkscape 1.2 でもこうか：

      At the moment Inkscape does not use this parameter despite it being in the
      user interface.

:guilabel:`Preserve Alpha`
   アルファー値を入力から直接複写するか、:abbr:`RGB` と同じように計算するかのどちらか。

このフィルターは画素評価と結びついていて、像が解像度に依存して決定することを意味
する：

   The *Convolve Matrix* primitive is necessarily linked to evaluating pixels.
   By default, the pixel size is that of the display. This means that the
   resulting image is not resolution independent.

Examples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: 読者ノート

   割愛。

Displacement Map
----------------------------------------------------------------------

変位写像はビットマップを二つ用いる原始フィルターだ。一方が他方を歪ませる。次の式
で新しい座標に変換する：

.. math::

   \begin{aligned}
   x^{\prime} &= s C_X(x, y) - \frac{1}{2}.\\
   y^{\prime} &= s C_Y(x, y) - \frac{1}{2}.
   \end{aligned}

ここで :math:`s` は縮尺であり、:math:`C_X, C_Y` は :abbr:`RGB` 成分または *A* 成分のい
ずれかで、X チャンネル属性および Y チャンネル属性で選択可能だ。両チャンネルは異
なる色に写像することができる。

本書の赤と緑のイラストがこのフィルターの意味をよく説明している。

   In the following examples, the *x* displacement is set to red and the *y*
   displacement is set to green. The olive green background corresponds to red
   and green values of 127, which corresponds (almost) to no displacement.

Gaussian Blur
----------------------------------------------------------------------

Photoshop でおなじみのガウスぼかしが Inkscape でも実現できる。原理は：

   The primitive creates an output image by using a Gaussian weighted average of
   the input pixels around the location of each corresponding output pixel.

   Internally, the amount of blur is defined in terms of the *blur radius*,
   which for the mathematically inclined is just the standard deviation of the
   Gaussian. Technically, a Gaussian function extends to infinity. For practical
   reasons, the limit of an object's blur is two times the *blur radius* outside
   the *bounding box* at maximum blur.

ぼかし半径という引数が効果のほとんどを決定する。

このフィルターは :abbr:`CPU` を酷使する。アプリケーション設定で品質を下げて楽に
させる：

   The *Gaussian Blur* primitive is highly :abbr:`CPU` intensive. The output is
   a trade-off between speed and quality. One can set the *Blur* quality for the
   screen display in the Inkscape :guilabel:`Preferences` dialog
   (:menuselection:`File --> Inkscape Preferences...` (:kbd:`Shift` +
   :kbd:`Ctrl` + :kbd:`P`)) under the :guilabel:`Filter` entry. Choosing a
   low-quality option will affect blurring of thin objects the most. Bitmap
   export is always done at the highest quality (and thus may be slow).

このフィルターは人気があるので、他の UI からも利用可能だ：

   A *Gaussian Blur* filter can be created through both the :guilabel:`Filter
   Effects` and the :guilabel:`Fill and Stroke` dialogs.

Blurring with the Fill and Stroke Dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Fill and Stroke` でのぼかし指定が簡潔で良い。スライダー操作が楽だ。た
だし、ぼかし半径の指定法が異なる：

   In this dialog, the amount of blurring is defined in terms of a percentage. A
   blurring of 100% (the maximum blurring allowed) is equivalent to a blur
   radius of 1/8 of the bounding box perimeter. For a square bounding box, this
   would be half of a side.

対称的なぼかししか適用できないが、単純な方がいい場合が多いので問題ない：

   Only a symmetric blur can be applied with this dialog.

ぼかしを後から調整する方法がある：

   Blurs created through the :guilabel:`Fill and Stroke` dialog depend on the
   size of the blurred object. To get the exact same amount of blur on different
   size objects, you can either use the :menuselection:`Edit --> Paste Style`
   (:kbd:`Shift` + :kbd:`Ctrl` + :kbd:`V`) command (if all the attributes are to
   be the same) or use the :guilabel:`Filter Effects` dialog to set the *blur
   radius* (standard deviation) to the same values.

Blurring with the Filter Effects dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

専用ダイアログを用いると、当然ながらよりぼかし指定を精緻に行える：

   Through this dialog you can create asymmetric blurs as well as have precise
   control over the *blur radius*. You can also build more complicated filters
   as demonstrated in the *Drop Shadow* example earlier in this chapter.

Blurring Examples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gradient Blurring
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   A Rectangle with a radial Gradient

昔のビートマニアでこんなアニメーションを見た記憶がある。

Clipping and Masking
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   The *Gaussian Blur* primitive is applied to an object before any *Clipping*
   or *Masking*. This will give a sharp edge along the clipping path to a
   blurred object. If you wish the clipped edge to be blurred, put it in a
   *Group* by itself and then blur the *Group*. If you want a feathered edge to
   an object like a bitmap, create a white transparency mask with the edge
   blurred.

ぼかしを入れたオブジェクトを切り抜くか、切り抜いたオブジェクトにぼかしを入れるか
ということで、無論どちらも実現可能だ。

Tile Clones
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   The :guilabel:`Create Tiled Clones` dialog has an option to vary the
   :guilabel:`Blur Radius` under the :guilabel:`Blur and opacity` tab.

Morphology
----------------------------------------------------------------------

   The *Morphology* primitive “fattens” or “thins” an object. The *Operator*
   attribute can either be *Dilate* or *Erode*. The amount of change is
   controlled by the *Radius* attribute. It can have independent *x* and *y*
   values.

Dilate と Erode で Google 検索すると、類似アプリケーションがたくさん存在するよう
だ。

Offset
----------------------------------------------------------------------

オブジェクトを上下左右にずらすだけのフィルターだ。

   If the specified offset is large, the filter region needs to be enlarged. You
   can increase the filter region under the :guilabel:`Filter General Settings`
   tab at the bottom of the :guilabel:`Filter Effects` dialog.

Complex Examples
======================================================================

原始フィルターから組み立てた複雑なフィルターの例。

Emboss
----------------------------------------------------------------------

   This example uses the *Color Matrix* to convert a photograph into an *Alpha*
   layer. The *Alpha* layer is then embossed by the *Diffuse Lighting* filter.

Neon
----------------------------------------------------------------------

   This example uses the *Morphology* primitive to create the glow around a neon
   tube. The glow color is derived from the neon color using the *Color Matrix*
   primitive. A couple *Gaussian Blur* primitives create the soft feel of the
   neon and a *Merge* primitive combines the neon and glow together.

試した：

.. raw:: html

   <object class="svg" data="../_images/neon.svg" type="image/svg+xml"></object>

Stereoscopic Pictures
----------------------------------------------------------------------

   This example uses the *Displacement Map* filter primitive to create a
   stereoscopic picture. The *Turbulence* primitive is used to generate a
   picture that is distorted with the *Displacement Map* primitive.

Solar Flare
----------------------------------------------------------------------

   This example uses the *Turbulence* primitive to modify a radial *Gradient*,
   thus simulating a solar flare during an eclipse.
