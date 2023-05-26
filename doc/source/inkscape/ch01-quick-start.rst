======================================================================
Chapter 1. Quick Start
======================================================================

.. contents::

The Anatomy of the Inkscape Window
======================================================================

バージョン 0.92 時点での記述だが、構造を理解する目的では現在バージョン 1.2 でも
通用する内容だ。ウィンドウ、パネル、コントロールなどの UI 構成要素の名称や機能を
おおまかに把握しておけばいい。

The Swedish Flag—A Short Example
======================================================================

.. admonition:: 読者ノート

   本章の SVG は本文を読みながら作ったが、後半に行くほど納得していない。Google
   Chrome や Firefox など、現代的なウェブブラウザーならば SVG ファイルをそのまま
   表示するので、本ノートにそのまま掲載していく。

   当ノートは Sphinx で HTML を生成しているが、``image`` や ``figure`` ディレク
   ティブではなく（これらでも描画できる）、本書の終盤で推奨されているように、
   ``raw`` ディレクティブで HTML ``object`` タグを直接入力して SVG ファイルを
   描画させるようにしている。右クリックで SVG コードを確認できる。

例として単純な意匠の国旗を SVG で再現している。次のような事項を扱う：

   This example will cover: setting a custom drawing size, setting up a Grid to
   help precisely place objects, the use of the Rectangle Tool, changing the
   color of objects, and finally saving a drawing and exporting the drawing into
   a form suitable for use on a web page.

すべての内容が重要だ。特に、寸法や座標を厳密に制御する方法を習得するのを優先する
べきだ。

.. raw:: html

   <object class="svg" data="../_images/swedish-flag.svg" type="image/svg+xml"></object>

The European Flag—A More Elaborate Example
======================================================================

この演習では複製操作が重要だ。回転などの基本的な変換操作を含む。また、ガイド線の
追加という珍しい操作も教えてくれる。

.. raw:: html

   <object class="svg" data="../_images/eu-flag.svg" type="image/svg+xml"></object>

A Hiking Club Logo—An Exercise in Paths
======================================================================

テキストとパスの操作を理解する。テキストをパスに変換することができることを覚えて
おく。

.. raw:: html

   <object class="svg" data="../_images/fhmc.svg" type="image/svg+xml"></object>

The Northern Pacific Railway Logo—A Tracing Example
======================================================================

   Inkscape's auto-tracing capability is very useful for turning existing
   artwork into SVG drawings.

本節の例では比較的単純な図形をトレースしているが、実写画像なども資源が潤沢にあり
さえすれば可能だ。

.. raw:: html

   <object class="svg" data="../_images/northern-pacific-railway.svg" type="image/svg+xml"></object>

A Box for Cards—An Isometric Projection
======================================================================

   Inkscape includes axonometric Grids that can be used to rapidly draw
   isometrically projected boxes. However, the method described here works best
   when drawings are included on the sides of the boxes as distorting the sides
   requires two precise transformations (scaling and skewing).

EU 旗の節で利用した機能と同じものを用いてアイソメ図を描く。

.. raw:: html

   <object class="svg" data="../_images/isometric.svg" type="image/svg+xml"></object>

.. admonition:: 読者ノート

   私の作ではテキストが一部はみ出している。これはチュートリアルの責任ではない。

A Can of Soup—A Three-Dimensional Drawing with Gradients
======================================================================

グラデーションを主に習得する。この例はモノクロだが、Inkscape では何色でも構成可
能だ。

.. raw:: html

   <object class="svg" data="../_images/soup.svg" type="image/svg+xml"></object>

A Vine Design—A Tiling Example
======================================================================

:menuselection:`Edit --> Clone --> Create Tiled Clones...` を使った複製。対称性
がキモだ。

.. raw:: html

   <object class="svg" data="../_images/grapevines.svg" type="image/svg+xml"></object>

An SVG Button—SVG and the Web
======================================================================

ボタン色アニメーションおよび JavaScript コードでのイベントハンドラーを SVG に仕
込む方法を紹介している。

.. raw:: html

   <object class="svg" data="../_images/button.svg" type="image/svg+xml"></object>

A Neon Sign—Animation
======================================================================

   While Inkscape cannot directly handle animation, it is possible to use
   Inkscape drawings as a starting point for creating animation. This tutorial
   demonstrates two techniques for creating an animated neon sign. It also
   discusses a number of issues the artist must consider in creating the
   animations.

バージョン 1.2 でもそうなのか、後で確認したい。

   The full tutorial can be found in the print and PDF versions of the book. For
   more information, check the book's web site.

本節および以降の節におけるチュートリアルは本に記載があるようだ。

A Bank Note—Security Features
======================================================================

   Inkscape has many features that allow one to design attractive bank notes
   complete with a variety of security features.

この記述を真に受けない方がいいだろう。

A Bottle—Photorealism
======================================================================

   Inkscape can be used to produce photo-realistic drawings. Inkscape features
   that are useful for this include: Gradients, the Gaussian Blur filter, and
   Bitmap Tracing. This tutorial uses all of these to produce a realistic
   drawing of an old seltzer bottle. The source photograph is available on the
   book's website.

本書の画像を見るとひじょうに魅力的な表現を達成している。本を買った方がいい。
