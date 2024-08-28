======================================================================
Chapter 10 Working with File Formats, Security, and Exporting ノート
======================================================================

.. include:: ./common-inc.txt

.. contents:: 章見出し
   :depth: 3
   :local:

File formats
======================================================================

LibreOffice では |ODF| や |PDF| など、以下に示すさまざまな形式のファイルを開くこ
とが可能だ。たいていの場合 LibreOffice がファイル形式を自動的に検出し、形式を明
示的に選択しなくても開くことが可能だ。

Text documents
----------------------------------------------------------------------

Writer は Open Document テキスト形式 (.odt、.ott、.oth、.odm、.fodt) および以下
の形式（さまざまなレガシー形式を含む）を読むことが可能だ：

* Microsoft Word 6.0/95/97/2000/XP/Mac) (.doc, .dot)
* Microsoft Word 2003 XML (.xml)
* Microsoft Word 2007/2010 XML (.docx, .docm, .dotx, .dotm)
* Microsoft WinWord 5 (.doc)
* Microsoft Works (.wps)
* Text CSV (.csv)
* DocBook (.xml)
* HTML Document (.htm, .html)
* eBook (.pdb)

.. admonition:: 読者ノート

   本稿では本書の一覧から特に重要な形式を抜粋する。以下同様。

Spreadsheets
----------------------------------------------------------------------

Calc では Open Document のスプレッドシート形式 (.ods, .ots, .fods) のほか、以下
の形式（さまざまなレガシー形式を含む）を開くことが可能だ：

* Microsoft Excel 97/2000/XP (.xls, .xlw, and .xlt)
* Microsoft Excel 4.x-5.0/95 (.xls, .xlw, and .xlt)
* Microsoft Excel 97-2003 (.xml)
* Microsoft Excel 2007-365 (.xlsx, .xlsm, .xltx, .xltm)
* Microsoft Excel 2007-2010 binary (.xlsb)
* Rich Text Format (.rtf)
* Text CSV (.csv and .txt)
* HTML Document (.htm and .html files, including Web page queries)

Presentations
----------------------------------------------------------------------

Impress はさまざまな Open Document プレゼンテーション形式 (.odp, .odg, .otp,
.fopd) のほか、以下の形式を開くことが可能だ：

* Microsoft PowerPoint 97/2000/XP (.ppt, .pot)
* Microsoft PowerPoint 2007-365 (.pptx, .pptm, .potx, .potm)
* Portable Document Format (.pdf)

Graphics
----------------------------------------------------------------------

Draw では、Open Document の画像ファイル形式 (.odg, .otg) や |PDF| ファイルのほ
か、以下の画像形式を使用可能だ：

* Adobe Photoshop (.psd)
* Microsoft Publisher 98-2010 (.pub)
* Microsoft Visio 2000-2013 (.vdx; .vsd; .vsdm; .vsdx)
* Bitmap (.bmp)
* |JPG| (.jpeg, .jpg)
* Picture Exchange (.pcx)
* Truevision TGA (.tga, .icb, .vda, .vst)
* Drawing Exchange Format, or Drawing Interchange Format (.dxf)
* Portable Gray Map (.pgm)
* |TIFF| (.tif, .tiff)
* Windows Metafile (.wmf)
* Enhanced Windows Metafile (.emf)
* |PNG| (.png)
* Portable Pixmap (.ppm)
* |SVG| (.svg)
* |GIF| (.gif)
* Photoshop Document (.psd)

Formulas
----------------------------------------------------------------------

Math は OpenOffice.org 1.x (.sxm), StarMath (.smf), MathML (.mml) ファイルで使用
されている形式と同様に、Open Document Formula ファイル (.odf) を利用可能だ。

数式が埋め込まれた Word 文書を開くとき、|OptionsDlg|
:menuselection:`Load/Save-->MicroOffice` ページで :guilabel:`MathType to
LibreOffice Math or reverse` がオンである場合、MS 数式は LibreOffice Math 数式に
自動的に変換される。

----

.. rubric:: 章末注
