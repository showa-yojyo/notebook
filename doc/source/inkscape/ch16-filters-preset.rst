======================================================================
Chapter 16. Filter Effects - Preset
======================================================================

.. contents::

本章の最初のパラグラフ：

   *Filter Effects* (Filters) are a feature of :abbr:`SVG` that allow an
   :abbr:`SVG` viewer to change the presentation of an object in a well-defined
   manner such as adding texture to a *Fill*, giving an object a blurred shadow,
   or modifying the object's color. Inkscape supports almost all :abbr:`SVG`
   Filter primitives (see next chapter) and includes many *Preset* (predefined)
   filters.

から、フィルター効果という概念の存在と、Inkscape ではそのオブジェクトを原始フィ
ルターと既製フィルターの二段構えで用意していることを推察する。

   Support of *Filters* is rather new in many web browsers. Don't be surprised
   to find bugs. Internet Explorer 9 will still not support filters.

この記述は現代のブラウザー事情では心配する必要はなかろう。

   This chapter covers *Preset* filters, that is those *Filters* that are
   preconstructed for your use. The following chapter covers *Custom* filters
   where you build the filters yourself.

まずは出来合いのフィルターで有用なものを知りたいので、本章を先に取り組みたい。

Use of Preset Filters
======================================================================

オブジェクト選択後にメニュー選択で実行というのが共通手順だ：

   Inkscape includes a couple of hundred *Preset* filters. These filters are
   accessed from the :menuselection:`Filters` menu. To use a built-in filter,
   just select the object(s) you wish to apply it to then select the
   :menuselection:`Filter` from one of the sub-menus. A few of the built-in
   *Filters* have dialogs where you can adjust basic parameters.

フィルターは普通のオブジェクト用とビットマップ用とに大別される。

自作フィルターをメニューに組み込むことができる。

   If you have developed your own *Filters*, you can add them as *Presets* by
   :abbr:`SVG` files with the *Filters* defined to the filters directory (Linux
   :file:`~/.config/inkscape/filters`).

Windows ならば :file:`%APPDATA%\\inkscape\\filters` なのだろう。しかし、このパス
を Inkscape 1.2 の設定ダイアログから見つけることができない。

   By default, the filters will be added to a :guilabel:`Personal` submenu. You
   can have more control over where the filters are placed if you define the
   following attributes:

   * ``inkscape:label``: Command label.
   * ``inkscape:menu``: Submenu name
   * ``inkscape:menu-tooltip``: Tool tip (for *Notification Region*).

   Inkscape includes an :abbr:`SVG` file with samples of all the *Preset
   Filters*. The file, :file:`filters.svg`, is located in the examples directory
   that can be found in the *File* :guilabel:`Open` dialog. Be prepared to wait
   as the file requires processing hundreds of *Filters*.

実際に当該ファイルをテキストエディターで開くと、内容は 2600 行くらいの
:abbr:`SVG` ファイルだ。これを精査すれば自作フィルターの :abbr:`XML` 要素を定義
する方法を解読できるだろう。

ABCs
======================================================================

.. admonition:: 利用者ノート

   Inkscape 1.2 で行方不明。ファイル
   :file:`%ProgramFiles%\\Inkscape\\share\\inkscape\\filters\\filters.svg` を
   ``ABC`` で :program:`grep` して見つからなかったのでないと判断した。

Bevels
======================================================================

.. admonition:: 読者ノート

   以降の表は前述の :abbr:`SVG` ファイルから :program:`xsltproc` で抽出して作成
   した。本文で少し触れているように、メニューは組み込みコマンドと
   :file:`filters.svg` からロード（起動時？）したものがマージされたものだ。前者
   のコマンド名を自動抽出する方法が現在わからないので、せめて後者の一覧だけでも
   ここに残しておく：

   :menuselection:`Filters --> Bevels -->` で言えば、次が組み込みコマンドで
   Inkscape にあって :file:`filters.svg` にないメニュー項目だ：

   * :menuselection:`Diffuse Light...`
   * :menuselection:`Matte Jelly...`
   * :menuselection:`Specular Light...`

   次以降のサブメニューでは組み込みコマンドの言及を省略する。

.. csv-table::
   :delim: |
   :header-rows: 1
   :widths: auto

   Command | Tooltip
   :menuselection:`Bloom` | Soft, cushion-like bevel with matte highlights
   :menuselection:`Bright Metal` | Bright metallic effect for any color
   :menuselection:`Button` | Soft bevel, slightly depressed middle
   :menuselection:`Combined Lighting` | Basic specular bevel to use for building textures
   :menuselection:`Dark Glass` | Illuminated glass effect with light coming from beneath
   :menuselection:`Deep Colors Plastic` | Transparent plastic with deep colors
   :menuselection:`Electronic Microscopy` | Bevel, crude light, discoloration and glow like in electronic microscopy
   :menuselection:`Fat Oil` | Fat oil with some adjustable turbulence
   :menuselection:`Glowing Metal` | Glowing metal texture
   :menuselection:`Jigsaw Piece` | Low, sharp bevel
   :menuselection:`Matte Bevel` | Soft, pastel-colored, blurry bevel
   :menuselection:`Melted Jelly` | Glossy bevel with blurred edges
   :menuselection:`Melted Jelly Matte` | Matte bevel with blurred edges
   :menuselection:`Metal Casting` | Smooth drop-like bevel with metallic finish
   :menuselection:`Molten Metal` | Melting parts of object together, with a glossy bevel and a glow
   :menuselection:`Neon` | Neon light effect
   :menuselection:`Pressed Steel` | Pressed metal with a rolled edge
   :menuselection:`Raised Border` | Strongly raised border around a flat surface
   :menuselection:`Ridged Border` | Ridged border with inner bevel
   :menuselection:`Smart Jelly` | Same as Matte jelly but with more controls
   :menuselection:`Stained Glass` | Illuminated stained glass effect
   :menuselection:`Translucent` | Illuminated translucent plastic or glass effect

Blurs
======================================================================

.. csv-table::
   :delim: |
   :header-rows: 1
   :widths: auto

   Command | Tooltip
   :menuselection:`Apparition` | Edges are partly feathered out
   :menuselection:`Blur Double` | Overlays two copies with different blur amounts and modifiable blend and composite
   :menuselection:`Evanescent` | Blur the contents of objects, preserving the outline and adding progressive transparency at edges

Bumps
======================================================================

   Best for bitmaps, but also useful for normal objects.

本書では両方の実行例を掲載している。

.. csv-table::
   :delim: |
   :header-rows: 1
   :widths: auto

   Command | Tooltip
   :menuselection:`Basic Diffuse Bump` | Matte emboss effect
   :menuselection:`Basic Specular Bump` | Specular emboss effect
   :menuselection:`Basic Two Lights Bump` | Two types of lighting emboss effect
   :menuselection:`Bubbly Bumps` | Flexible bubbles effect with some displacement
   :menuselection:`Bubbly Bumps Alpha` | Same as Bubbly Bumps but with transparent highlights
   :menuselection:`Bubbly Bumps Matte` | Same as Bubbly Bumps but with a diffuse light instead of a specular one
   :menuselection:`Bump Engraving` | Carving emboss effect
   :menuselection:`Canvas Bumps` | Canvas texture with an HSL sensitive height map
   :menuselection:`Canvas Bumps Alpha` | Same as Canvas Bumps but with transparent highlights
   :menuselection:`Canvas Bumps Matte` | Same as Canvas Bumps but with a diffuse light instead of a specular one
   :menuselection:`Convoluted Bump` | Convoluted emboss effect
   :menuselection:`Dark Emboss` | Emboss effect: 3D relief where white is replaced by black
   :menuselection:`Embossed Leather` | Combine a HSL edges detection bump with a leathery or woody and colorizable texture
   :menuselection:`HSL Bumps Alpha` | Same as HSL Bumps but with transparent highlights
   :menuselection:`Jelly Bump` | Convert pictures to thick jelly
   :menuselection:`Linen Canvas` | Painting canvas emboss effect
   :menuselection:`Paper Bump` | Paper like emboss effect
   :menuselection:`Plaster` | Combine a HSL edges detection bump with a matte and crumpled surface effect
   :menuselection:`Plaster Color` | Colored plaster emboss effect
   :menuselection:`Plasticine` | Matte modeling paste emboss effect
   :menuselection:`Plastify` | HSL edges detection bump with a wavy reflective surface effect and variable crumple
   :menuselection:`Relief Print` | Bumps effect with a bevel, color flood and complex lighting
   :menuselection:`Rough Canvas Painting` | Painting canvas emboss effect
   :menuselection:`Thick Acrylic` | Thick acrylic paint texture with high texture depth
   :menuselection:`Thick Paint` | Thick painting effect with turbulence
   :menuselection:`Tinfoil` | Metallic foil effect combining two lighting types and variable crumple
   :menuselection:`Velvet Bumps` | Gives Smooth Bumps velvet like
   :menuselection:`Wrinkled Varnish` | Thick glossy and translucent paint texture with high depth

Color
======================================================================

.. csv-table::
   :delim: |
   :header-rows: 1
   :widths: auto

   Command | Tooltip
   :menuselection:`Black Light` | Light areas turn to black
   :menuselection:`Blend Opposites` | Blend an image with its hue opposite
   :menuselection:`Fluorescence` | Oversaturate colors which can be fluorescent in real world
   :menuselection:`Hue to White` | Fades hue progressively to white
   :menuselection:`Paint Channels` | Colorize separately the three color channels
   :menuselection:`Simulate CMY` | Render Cyan, Magenta and Yellow channels with a colorizable background
   :menuselection:`Soft Colors` | Adds a colorizable edges glow inside objects and pictures
   :menuselection:`Trichrome` | Like Duochrome but with three colors

Distort
======================================================================

.. csv-table::
   :delim: |
   :header-rows: 1
   :widths: auto

   Command | Tooltip
   :menuselection:`Chalk and Sponge` | Low turbulence gives sponge look and high turbulence chalk
   :menuselection:`Lapping` | Something like a water noise
   :menuselection:`Pixel Smear` | Van Gogh painting effect for bitmaps
   :menuselection:`Ripple` | Horizontal rippling of edges
   :menuselection:`Rough and Dilate` | Create a turbulent contour around
   :menuselection:`Roughen Inside` | Roughen all inside shapes
   :menuselection:`Swirl` | Paint objects with a transparent turbulence which wraps around color edges
   :menuselection:`Torn Edges` | Displace the outside of shapes and pictures without altering their content

Fill and Transparency
======================================================================

本書にこの節はないが、Inkscape にこのメニュー項目があるので勝手にノートとして追
加する。

.. csv-table::
   :delim: |
   :header-rows: 1
   :widths: auto

   Command | Tooltip
   :menuselection:`Fast Crop` | Does not filter but adds a filter region
   :menuselection:`Fill Background` | Adds a colorizable opaque background
   :menuselection:`Flatten Transparency` | Adds a white opaque background
   :menuselection:`Monochrome Transparency` | Convert to a colorizable transparent positive or negative
   :menuselection:`Posterized Light Eraser` | Create a semi transparent posterized image
   :menuselection:`Saturation Map` | Creates an approximative semi-transparent and colorizable image of the saturation levels

Image Effects
======================================================================

.. csv-table::
   :delim: |
   :header-rows: 1
   :widths: auto

   Command | Tooltip
   :menuselection:`Age` | Imitate aged photograph
   :menuselection:`Film Grain` | Adds a small scale graininess
   :menuselection:`Sharpen` | Sharpen edges and boundaries within the object, force=0.15
   :menuselection:`Sharpen More` | Sharpen edges and boundaries within the object, force=0.3
   :menuselection:`Soft Focus Lens` | Glowing image content without blurring it

Image Effects, Transparent
======================================================================

メニュー項目 :menuselection:`Image Paint and Draw -->` 以下に対応する節と思われ
る。

.. csv-table::
   :delim: |
   :header-rows: 1
   :widths: auto

   Command | Tooltip
   :menuselection:`Alpha Draw Liquid` | Gives a transparent fluid drawing effect with rough line and filling
   :menuselection:`Alpha Engraving` | Gives a transparent engraving effect with rough line and filling
   :menuselection:`Alpha Engraving B` | Gives a controllable roughness engraving effect to bitmaps and materials
   :menuselection:`Blueprint` | Detect color edges and retrace them in blue
   :menuselection:`Chromolitho Alternate` | Old chromolithographic effect
   :menuselection:`Cross Noise Poster` | Overlay with a small scale screen like noise
   :menuselection:`Cross Noise Poster B` | Adds a small scale screen like noise locally
   :menuselection:`Image Drawing Basic` | Enhance and redraw color edges in 1 bit black and white
   :menuselection:`Light Contour` | Uses vertical specular light to draw lines
   :menuselection:`Liquid Drawing` | Gives a fluid and wavy expressionist drawing effect to images
   :menuselection:`Litho` | Create a two colors lithographic effect
   :menuselection:`Marbled Ink` | Marbled transparency effect which conforms to image detected edges
   :menuselection:`Oil Painting` | Simulate oil painting style
   :menuselection:`Old Postcard` | Slightly posterize and draw edges like on old printed postcards
   :menuselection:`Pencil` | Detect color edges and retrace them in grayscale
   :menuselection:`Poster Color Fun` | Poster Color Fun
   :menuselection:`Poster Draw` | Enhance and redraw edges around posterized areas
   :menuselection:`Poster Rough` | Adds roughness to one of the two channels of the Poster paint filter

Materials
======================================================================

.. csv-table::
   :delim: |
   :header-rows: 1
   :widths: auto

   Command | Tooltip
   :menuselection:`3D Marble` | 3D warped marble texture
   :menuselection:`3D Mother of Pearl` | 3D warped, iridescent pearly shell texture
   :menuselection:`3D Wood` | 3D warped, fibered wood texture
   :menuselection:`Cracked Lava` | A volcanic texture, a little like leather
   :menuselection:`Enamel Jewelry` | Slightly cracked enameled texture
   :menuselection:`Eroded Metal` | Eroded metal texture with ridges, grooves, holes and bumps
   :menuselection:`Flex Metal` | Bright, polished uneven metal casting, colorizable
   :menuselection:`Gold Paste` | Fat pasted cast metal, with golden highlights
   :menuselection:`Gold Splatter` | Splattered cast metal, with golden highlights
   :menuselection:`Iridescent Beeswax` | Waxy texture which keeps its iridescence through color fill change
   :menuselection:`Leopard Fur` | Leopard spots (loses object's own color)
   :menuselection:`Lizard Skin` | Stylized reptile skin texture
   :menuselection:`Metallized Paint` | Metallized effect with a soft lighting, slightly translucent at the edges
   :menuselection:`Peel Off` | Peeling painting on a wall

Morphology
======================================================================

ここは本書と少し異なる。

.. csv-table::
   :delim: |
   :header-rows: 1
   :widths: auto

   Command | Tooltip
   :menuselection:`Black Hole` | Creates a black light inside and outside
   :menuselection:`Contouring Discrete` | Sharp multiple contour for objects
   :menuselection:`Contouring Table` | Blurred multiple contours for objects
   :menuselection:`Cool Outside` | Blurred colorized contour, empty inside
   :menuselection:`Posterized Blur` | Converts blurred contour to posterized steps
   :menuselection:`Warm Inside` | Blurred colorized contour, filled inside

Non Realistic 3D Shaders
======================================================================

.. csv-table::
   :delim: |
   :header-rows: 1
   :widths: auto

   Command | Tooltip
   :menuselection:`Aluminium` | Aluminium effect with sharp brushed reflections
   :menuselection:`Aluminium Emboss` | Satiny aluminium effect with embossing
   :menuselection:`Brush Draw` | Draft painted cartoon shading with a glassy look
   :menuselection:`Brushed Metal` | Satiny metal surface effect
   :menuselection:`Chrome` | Bright chrome effect
   :menuselection:`Chrome Emboss` | Embossed chrome effect
   :menuselection:`Comics` | Comics cartoon drawing effect
   :menuselection:`Comics Cream` | Comics shader with creamy waves transparency
   :menuselection:`Comics Draft` | Draft painted cartoon shading with a glassy look
   :menuselection:`Comics Fading` | Cartoon paint style with some fading at the edges
   :menuselection:`Contour Emboss` | Satiny and embossed contour effect
   :menuselection:`Deep Chrome` | Dark chrome effect
   :menuselection:`Deep Metal` | Deep and dark metal shading
   :menuselection:`Emboss Shader` | Combination of satiny and emboss effect
   :menuselection:`Frosted Glass` | Satiny glass effect
   :menuselection:`Opaline` | Contouring version of smooth shader
   :menuselection:`Refractive Glass` | Double reflection through glass with some refraction
   :menuselection:`Sharp Deco` | Unrealistic reflections with sharp edges
   :menuselection:`Sharp Metal` | Chrome effect with darkened edges

Overlays
======================================================================

悦楽の園とはどういうことだ。

.. csv-table::
   :delim: |
   :header-rows: 1
   :widths: auto

   Command | Tooltip
   :menuselection:`Alpha Monochrome Cracked` | Basic noise fill texture; adjust color in Flood
   :menuselection:`Alpha Turbulent` | Basic noise fill texture; adjust color in Flood
   :menuselection:`Barbed Wire` | Gray bevelled wires with drop shadows
   :menuselection:`Blue Cheese` | Marble-like bluish speckles
   :menuselection:`Canvas Transparency` | Gives a canvas like HSL sensitive transparency.
   :menuselection:`Carnaval` | White splotches evocating carnaval masks
   :menuselection:`Clouds` | Airy, fluffy, sparse white clouds
   :menuselection:`Colorize Turbulent` | Basic noise fill texture; adjust color in Flood
   :menuselection:`Cross Noise` | Adds a small scale screen like graininess
   :menuselection:`Cross Noise B` | Adds a small scale crossy graininess
   :menuselection:`Dots Transparency` | Gives a pointillist HSL sensitive transparency
   :menuselection:`Duotone Turbulent` | Basic noise fill texture; adjust color in Flood
   :menuselection:`Frost` | Flake-like white splotches
   :menuselection:`Garden of Delights` | Phantasmagorical turbulent wisps, like Hieronymus Bosch's Garden of Delights
   :menuselection:`Growing Cells` | Random rounded living cells like fill
   :menuselection:`Light Eraser Cracked` | Basic noise fill texture; adjust color in Flood
   :menuselection:`Liquid` | Colorizable filling with liquid transparency
   :menuselection:`Oil Slick` | Rainbow-colored semitransparent oily splotches
   :menuselection:`People` | Colorized blotches, like a crowd of people
   :menuselection:`Poster Turbulent` | Basic noise fill texture; adjust color in Flood
   :menuselection:`Rough Transparency` | Adds a turbulent transparency which displaces pixels at the same time
   :menuselection:`Rubber Stamp` | Random whiteouts inside
   :menuselection:`Scotland` | Colorized mountain tops out of the fog
   :menuselection:`Shaken Liquid` | Colorizable filling with flow inside like transparency
   :menuselection:`Silhouette Marbled` | Basic noise transparency texture
   :menuselection:`Smear Transparency` | Paint objects with a transparent turbulence which turns around color edges
   :menuselection:`Speckle` | Fill object with sparse translucent specks
   :menuselection:`Swiss Cheese` | Random inner-bevel holes
   :menuselection:`Tartan` | Checkered tartan pattern
   :menuselection:`Tartan Smart` | Highly configurable checkered tartan pattern
   :menuselection:`Tiger Fur` | Tiger fur pattern with folds and bevel around the edges
   :menuselection:`Wavy Tartan` | Tartan pattern with a wavy displacement and bevel around the edges
   :menuselection:`Zebra` | Irregular vertical dark stripes (loses object's own color)

Protrusions
======================================================================

.. csv-table::
   :delim: |
   :header-rows: 1
   :widths: auto

   Command | Tooltip
   :menuselection:`Chewing Gum` | Creates colorizable blotches which smoothly flow over the edges of the lines at their crossings
   :menuselection:`Dripping` | Random paint streaks downwards
   :menuselection:`Fire` | Edges of object are on fire
   :menuselection:`Ink Bleed` | Inky splotches underneath the object

Ridges
======================================================================

.. csv-table::
   :delim: |
   :header-rows: 1
   :widths: auto

   Command | Tooltip
   :menuselection:`Dragee` | Gel Ridge with a pearlescent look
   :menuselection:`Glowing Bubble` | Bubble effect with refraction and glow
   :menuselection:`Matte Ridge` | Soft pastel ridge
   :menuselection:`Metallized Ridge` | Gel Ridge metallized at its top
   :menuselection:`Refractive Gel A` | Gel effect with light refraction
   :menuselection:`Refractive Gel B` | Gel effect with strong refraction
   :menuselection:`Thin Membrane` | Thin like a soap membrane

Scatter
======================================================================

.. csv-table::
   :delim: |
   :header-rows: 1
   :widths: auto

   Command | Tooltip
   :menuselection:`Air Spray` | Convert to small scattered particles with some thickness
   :menuselection:`Cubes` | Scattered cubes; adjust the Morphology primitive to vary size
   :menuselection:`Leaves` | Leaves on the ground in Fall, or living foliage
   :menuselection:`Pointillism` | Gives a turbulent pointillist HSL sensitive transparency

Shadows and Glows
======================================================================

.. csv-table::
   :delim: |
   :header-rows: 1
   :widths: auto

   Command | Tooltip
   :menuselection:`Cutout Glow` | In and out glow with a possible offset and colorizable flood
   :menuselection:`Dark and Glow` | Darkens the edge with an inner blur and adds a flexible glow
   :menuselection:`Emergence` | Cut out, add inner shadow and colorize some parts of an image
   :menuselection:`In and Out` | Inner colorized shadow, outer black shadow
   :menuselection:`Inset` | Shadowy outer bevel

Textures
======================================================================

.. csv-table::
   :delim: |
   :header-rows: 1
   :widths: auto

   Command | Tooltip
   :menuselection:`Bark` | Bark texture, vertical; use with deep colors
   :menuselection:`Blotting Paper` | Inkblot on blotting paper
   :menuselection:`Burnt edges` | Torn edges with a dark inner blur
   :menuselection:`Burst` | Burst balloon texture crumpled and with holes
   :menuselection:`Cracked Glass` | Under a cracked glass
   :menuselection:`Crumpled Plastic` | Crumpled matte plastic, with melted edge
   :menuselection:`Felt` | Felt like texture with color turbulence and slightly darker at the edges
   :menuselection:`Gouache` | Partly opaque water color effect with bleed
   :menuselection:`Ink Paint` | Ink paint on paper with some turbulent color shift
   :menuselection:`Jam Spread` | Glossy clumpy jam spread
   :menuselection:`Melted Rainbow` | Smooth rainbow colors slightly melted along the edges
   :menuselection:`Organic` | Bulging, knotty, slick 3D surface
   :menuselection:`Riddled` | Riddle the surface and add bump to images
   :menuselection:`Rough Paper` | Aquarelle paper effect which can be used for pictures as for objects
   :menuselection:`Rough and Glossy` | Crumpled glossy paper effect which can be used for pictures as for objects
   :menuselection:`Silk Carpet` | Silk carpet texture, horizontal stripes
   :menuselection:`Stone Wall` | Stone wall texture to use with not too saturated colors
   :menuselection:`Tinted Rainbow` | Smooth rainbow colors melted along the edges and colorizable
   :menuselection:`Warped Rainbow` | Smooth rainbow colors warped along the edges and colorizable
   :menuselection:`Watercolor` | Cloudy watercolor effect
   :menuselection:`Wax Print` | Wax print on tissue texture

Transparency Utilities
======================================================================

Inkscape 1.2 にはこの名前のメニューが見当たらない。これに対応するメニューがさっ
き勝手に追加した :menuselection:`Fill and Transparency -->` だろうか。

.. todo::

   :menuselection:`Filters -->` に出てくるコマンド名やキャプションに知らない英単
   語が多く出現する。辞書を自作するべきだろう。
