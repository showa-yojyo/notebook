======================================================================
Chapter 2. Files
======================================================================

.. contents::

..

   Inkscape until v0.92 used a scale of 90 pixels per inch which lead to
   inconsistent rendering between Inkscape and web browsers when lengths with
   absolute units were used. Inkscape v0.92 uses the correct 96 pixels per inch
   value. Recent versions of Inkscape do not save lengths with absolute units
   but will instead convert them to user units even when the :abbr:`GUI` shows
   lengths with units. The normal user should never have to worry about this.

絶対単位には近づいてはいけないということを覚えておこう。

Creating and Opening Files
======================================================================

主なコマンドを表にまとめておく：

.. csv-table::
   :delim: #
   :header-rows: 1
   :widths: auto

   コマンド # キーバインド,
   :menuselection:`New` # :kbd:`Ctrl` + :kbd:`N` # 内容を新規作成する
   :menuselection:`New from Template...` # :kbd:`Ctrl` + :kbd:`Alt` + :kbd:`N` # テンプレートを選択して内容を作成する
   :menuselection:`Open...` # :kbd:`Ctrl` + :kbd:`O` # ファイルから内容をロードする
   :menuselection:`Open Recent` # n/a # 最近ロードしたファイルを選択してロードする
   :menuselection:`Revert` # n/a # 内容をロードした時点のものに戻す

コマンド :menuselection:`New` は既定テンプレートから作成することに注意する。
Inkscape を起動すると真っ白いキャンバスが表示されるが、実際には既定テンプレート
が適用されている。これについては別の章で述べられる。

コマンド :menuselection:`New from Template...` はテンプレート選択ダイアログが表
示され、そこから封筒や DVD などの項目を選択して文書の初期状態を決定する。テンプ
レートに関しては別の章で述べられる。

既存のファイルを開くときに、それが旧バージョンの Inkscape で作成された
:abbr:`SVG` である場合には単位系の変換機会が与えられる。興味がある場合には本書を
当たるようにする。

コマンド :menuselection:`Revert` は GIMP などのソフトと同じ意味だ。これまでの編
集をすべて破棄してファイルを開き直すようなものだ。

Saving Files
======================================================================

保存コマンドは次の四つだ：

.. csv-table::
   :delim: #
   :header-rows: 1
   :widths: auto

   コマンド # キーバインド,
   :menuselection:`Save` # :kbd:`Ctrl` + :kbd:`S` # 通常の意味での上書き保存
   :menuselection:`Save As...` # :kbd:`Shift` + :kbd:`Ctrl` + :kbd:`S` # 通常の意味での別名保存
   :menuselection:`Save a Copy...` # :kbd:`Shift` + :kbd:`Ctrl` + :kbd:`Alt` + :kbd:`S` # 下記参照
   :menuselection:`Save Template...` # n/a # 編集中の文書をテンプレートとして保存する

:menuselection:`Save a Copy...` は別名保存したときに、現在編集中の文書に関連する
ファイル名を変更しないという特徴がある。Emacs にもそういうコマンドがあったと記憶
している。

:menuselection:`Save Template...` は本書に記述がない新しいコマンドと思われる。
オプションとして既定テンプレートかどうかも指定可能だ。

最後に自動保存機能について述べられている：

   Inkscape will autosave backups if desired. The feature can be toggled on in
   the :menuselection:`Input/Output --> Autosave` section of the Inkscape
   :guilabel:`Preferences` dialog. The interval between saves, the maximum of
   saves to keep, and the directory where the saves are placed can also be set
   here.

この設定は Inkscape いじり始めの早いうちに確認するのが望ましい。既定値が大きい。

Importing Files
======================================================================

   Inkscape is capable of importing many types of vector and bitmap graphics
   files.

インポートは現在編集中の文書に対して機能する。UI としてもドラッグ＆ドロップに対
応しているし、メニュー選択 :menuselection:`File --> Import...` でも実行できる。

Bitmaps Files
----------------------------------------------------------------------

   When bitmap files are imported, a dialog will open offering a number of
   import options.

ファイルダイアログで JPEG などのビットマップ系ファイルを選択すると、オプション指
定ダイアログが現れる。項目をマウスホバーするとツールチップが表示されるので、使い
方はわかると思う。

Vector Files
----------------------------------------------------------------------

   Some vector file formats can include bitmap graphics.

例えば次の形式だ：

* .dxf (AutoCAD)
* .emf (Enhanced Meta File)
* .eps (Encapsulated PostScript)
* .pdf (Adobe Portable Document Format)
* .ps (PostScript)
* .svg (:abbr:`SVG`)
* .svgz (:abbr:`SVG` Compressed)
* .vsd, .vdx, .vsdm, .vsdx (Visio)
* .wmf (Windows Meta File)
* .xaml (Microsoft Application eXtensible Markup Language).

Open Clip Art Library
----------------------------------------------------------------------

:menuselection:`File --> Import Web Image...` を選択すると、かなり長い時間待たさ
れた挙げ句にダイアログボックスが表示される。

1. 右上のドロップダウンリストから :guilabel:`Open Clipart Library` などを選択す
   る。
2. 検索欄で適当な単語を入力する。:kbd:`Enter` で実行。
3. 検索結果に画像と作品名が一覧される。
4. 所望の項目を選択する。
5. ダイアログボックス右下の :kbd:`Import` ボタンを押す。

以上の手順で、出来合いの :abbr:`SVG` が編集中の文書にインポートされる。

Exporting Files
======================================================================

   Exporting methods are divided between exporting :abbr:`PNG (Portable Network
   Graphics)` files and exporting to all other file formats. The :abbr:`PNG`
   graphics standard is a patent unencumbered standard that is supported
   natively by all major web browsers and graphics programs.

もちろん PNG へのエクスポートが重要だ。

Exporting PNG (Portable Network Graphic) Files
----------------------------------------------------------------------

:menuselection:`File --> Export...` を選択するか :kbd:`Ctrl` + :kbd:`Shift` +
:kbd:`S` でエクスポートパネルが画面に現れる。この UI を見ればわかるだろう。

.. admonition:: 読者ノート

   エクスポートを実行する前に、透過させたい部分を確実に透過させるように、文書構
   成要素の表示・非表示状態を意図通りに設定すること。

Exporting Other File Types
----------------------------------------------------------------------

今のところ利用予定がないので読まないでおく。

Printing Files
======================================================================

   Printing your drawing can be done through the :menuselection:`File -->
   Print...` (:kbd:`Ctrl` + :kbd:`P`) dialog. The standard GTK print dialog is
   used. This allows printing to any PostScript-capable printer as well as to
   either a PostScript or :abbr:`PDF` file. Printing uses Cairo-based routines.
   The PostScript back-end makes heavy use of rasterizing the image. This is
   partly due to the fact that PostScript does not support transparency.

Windows 版 Inkscape の場合には標準印刷ダイアログボックスが出現する（ように見え
る）。:abbr:`PDF` や XPS 形式で「印刷」することも可能だ。

:guilabel:`Rendering` タブの :guilabel:`Backend` オプションにも注目。普通は
:guilabel:`Vector` のほうを想定しているはずだ。

Vacuuming Files
======================================================================

   The command :menuselection:`File --> Vacuum Defs` removes unused definitions
   from the ``<defs>`` section of the :abbr:`SVG` file. This includes things
   like unused gradients, patterns, markers, and filters.

現在の UI では :menuselection:`File --> Clean Up Document` に名称変更されている
ようだ。

Document Properties
======================================================================

:menuselection:`File --> Document Properties...` (:kbd:`Shift` + :kbd:`Ctrl` +
:kbd:`D`) で現在編集中の文書の特性各種を確認、設定できるパネルが表示する。

Document Dimensions and Scale
----------------------------------------------------------------------

:guilabel:`Display` タブで文書の寸法や縮尺を随時編集可能だ。

File Metadata and License
----------------------------------------------------------------------

   You can add Metadata to a drawing via the :guilabel:`Metadata` tab of the
   :guilabel:`Document Properties` dialog. This includes a variety of fields
   such as author and copyright date. A license for the document can be selected
   on the :guilabel:`License` tab of the same dialog.

GitHub などの公開リポジトリーに :abbr:`SVG` ファイルを格納する場合には可能な限り
これらの値を入力しておきたい。
