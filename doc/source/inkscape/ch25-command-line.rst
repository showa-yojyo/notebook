======================================================================
Chapter 25. Using the Command Line
======================================================================

.. contents::

コマンドラインで Inkscape を操縦できればたいへんうれしい。何ができるのか見ていこ
う。

   Inkscape has the ability to batch process *SVG* files without opening up the
   Graphics User Interface (*GUI*). The available options can be divided into a
   few categories: general commands, exporting commands (including printing),
   and query commands.

コマンドラインからならば PDF の最初のページは読めるようだ。

   Most Inkscape commands are attached to verbs. Any verb can be called from the
   command line with the ``--verb`` argument, allowing complex processing to
   take place. However, it is not possible to set parameters. A list of all
   verbs can be obtained using ``--verb-list``. It does not appear possible to
   suppress the *GUI* when using the ``--verb`` argument.

インターフェイスにクセがあるように感じられる。とにかくオプション ``--verb`` を指
定すると Inkscape のウィンドウが出現されることは憶えておこう。

   Here is a simple example of opening a file, selecting an object, flipping it,
   and then saving the file. The Star has an id of ``MyStar``.

   .. code:: console

      $ inkscape --select=MyStar --verb ObjectFlipVertically --verb FileSave --verb FileClose MyStar.svg

このコマンド例から次のことが推測される：

* ``--select=<ID>`` で図面内にある ID が ``<ID>`` であるオブジェクトを指定する。
* ``--verb <COMMAND>`` で Inkscape のコマンド ``<COMMAND>`` を実行する。
* ``--verb <COMMAND>`` を複数与えることが可能。おそらく順次実行する。
* 最後の引数が入力 SVG ファイルパス。

.. admonition:: 読者ノート

   * Windows 版の場合は :program:`inkscape.com` に対してコマンドライン実行をする
     こと。
   * 後述するようにこのコマンド形式は古い。もう通用しない。

コマンドラインオプションの書き方は GNU 様式だ：

   Most options have two forms: a short form preceded by one dash and a long
   form proceeded by two dashes. Some options take parameters that can (usually)
   be attached to the option with an ``=`` sign (e.g., ``--export-png=my.png``)
   or separated by a space (e.g., ``--export-png my.png``).

対話モードも実装されている。即時実行モードと同じコマンドが利用可能だ：

   Inkscape has a shell mode, entered by calling Inkscape from the command line
   with the ``--shell`` option. There are no new capabilities using this
   command; it is simply to allow one to execute multiple independent commands
   without restarting Inkscape each time. Here is an example of exporting the
   :file:`MyStar.svg` to a *PNG*:

   .. code:: console

      $ inkscape --shell
      Inkscape 0.48 interactive shell mode. Type 'quit' to quit.
      > MyStar.svg --export-png=MyStar.png
      Background RRGGBBAA: ffffff00
      Area 0:0:150:150 exported to 150 x 150 pixels (90 dpi)
      Bitmap saved as: MyStar.png
      > quit

入力 SVG ファイルの指定方法はこれでいいのか。

General Command Line Options
======================================================================

.. admonition:: 読者ノート

   この節の内容は読み替えないと Inkscape 1.2 で通じない。以下では読み替えたもの
   を記す。

.. option:: -?, --help

   コマンドラインオプションの一覧と各オプションの簡単な説明を出力する。

.. option:: -V, --version

   バージョンを出力する。GUI 版の :menuselection:`Help --> About Inkscape` が表
   示する情報と同一。

.. option:: --system-data-directory

   Windows 10 ならパス :file:`%PROGRAMFILES%\\Inkscape\\share` を出力する。

.. option:: --user-data-directory

   Windows 10 ならパス :file:`%APPDATA%\\inkscape` を出力する。

.. option:: --actions=ACTION(:ARG)[;ACTION(:ARG)]*

   実行するコマンド列を指定する。指定順に実行する。

.. option:: --action-list

   :option:`--actions` として有効なコマンドすべてを出力する。簡単な説明も付く。

.. option:: --select=OBJECT-ID[,OBJECT-ID]*

   指定された ID を持つオブジェクトを選択する。

.. option:: --vacuum-defs

   *SVG* ファイルの ``<defs>`` から未使用の定義を削除する。GUI で言う
   :menuselection:`File --> Clean Up Document` コマンドに相当する。新しいファイ
   ルを作成するものではない。

Export Command Line Options
======================================================================

GUI で使われるエクスポートコマンドは CUI でも利用可能だ。

   Inkscape can be used to convert *SVG* files to another form. Right now, the
   command line can be used to generate Portable Network Graphic (*PNG*),
   PostScript (*PS*), Encapsulated PostScript (*EPS*), Portable Document Files
   (*PDF*), Enhanced Metafile Files (*EMF*-Windows only), and plain *SVG* files.
   More options are available from within Inkscape using the :guilabel:`Save As`
   or :guilabel:`Export Bitmap` dialogs.

   The export options can be divided into three classes: those that specify the
   output format, those that specify the region to export, and those that
   specify properties such as background color in the exported image.

以下、この三類型それぞれのコマンドラインオプションを見ていく。

Format Options
----------------------------------------------------------------------

.. admonition:: 読者ノート

   Inkscape 1.2 の仕様と本書の記述を折衷したノートを以下では綴る。

.. option:: --export-type=TYPE[,TYPE]*

   エクスポートするファイルの形式を指定する。次の値のいずれかを指定する：

   * ``svg``
   * ``png``
   * ``ps``
   * ``eps``
   * ``pdf``
   * ``emf``
   * ``wmf``
   * ``xam``

   カンマ区切りで指定形式を可能。その場合はファイルが複数保存される？

.. option:: -o, --export-filename=FILENAME

   出力ファイルパスを指定する。ファイル種類は拡張子があればそれから推測される。
   ``FILENAME`` を ``-`` にすると標準出力に書き出す。

例えば Linux では出力を PostScript ファイルに送るコマンドは次のようなものだ（他
にも考えられる）：

.. code:: console

   $inkscape -o test.ps test.svg

Export Region Options
----------------------------------------------------------------------

基本的にはビットマップ形式でエクスポートしたい。

.. option:: -a, --export-area=x0:y0:x1:y1

   エクスポートする矩形領域を指定する。左下隅と右上隅の座標を指定する。単位は図
   面のユーザー単位だ。

   次は図面が 200×100 だとしたら、その左半分を PNG に書き出すコマンドラインの例
   だ：

   .. code:: console

      $ inkscape --export-area=0:0:100:100 -o test.png test.svg

.. option:: -C, --export-area-page

   ページ領域をエクスポートする。

.. option:: -D, --export-area-drawing

   図面内のオブジェクトすべての BB 内部をエクスポートする。

      Note that :option:`--export-area-page` overides
      :option:`--export-area-drawing`.

.. option:: --export-area-snap

   このオプションはエクスポート領域を微調整するためのものだ。次の効果を期待でき
   る：

      This option has two effects: (1) If you have aligned all your objects to a
      pixel grid (to reduce anti-aliasing effects) but the export area bounding
      box is not aligned to the grid, it will ensure that the exported pixmap
      will be aligned to the same grid. (2) It will ensure that the edges of the
      drawing will not be clipped.

.. option:: -i, --export-id=OBJECT-ID[;OBJECT-ID]*

   The area exported will be defined by the bounding box of the named object.
   The exported drawing will include the parts of any other objects that fall
   within this bounding box.

   指定オブジェクトの BB 領域をエクスポートする。出力図面にはこの BB に含まれる
   他のオブジェクトの部分も含む。したがって、このオプションは使いにくいと考えら
   れる：

      The name of a given object can be found by selecting the object from
      within Inkscape and looking at the :guilabel:`XML Editor`. (Of course, if
      you do this, you may as well export using the :guilabel:`Export Bitmap`
      dialog.)

.. option:: -j, --export-id-only

   指定オブジェクトしかエクスポートしない。ただし上述の :option:`--export-id` と
   同時に指定する必要がある。

Export Property Options
----------------------------------------------------------------------

   The first few options are for bitmap exports, while the last few are for *PS*
   and *EPS* export.

ビットマップオプションをより重視したい。

.. option:: -d, --export-dpi

   エクスポート形式がビットマップか否かで指定方法を分ける。

   ビットマップの場合は、エクスポート画像は与えられた数値とユーザー単位との比で
   拡縮されたものだ：

   The default value is 90, which matches the internal scale used by Inkscape;
   that is, a value of 90 means that one Inkscape pixel corresponds to one
   exported pixel. A value of 72 means that one Inkscape point corresponds to
   one exported pixel. (See the section called “Inkscape Coordinates”.) This
   option overrides the :option:`--export-use-hints` option.

   ビットマップでない場合にはフィルターをドット絵に変換する際の解像度を意味す
   る。こちらもやはり：

      The default values is 90 dpi.

.. option:: -w, --export-width=WIDTH

   エクスポート画像の横寸法をこの値になるように拡縮する。:option:`--export-dpi`
   指定を上書きする。

.. option:: -h, --export-height=HEIGHT

   エクスポート画像の縦寸法をこの値になるように拡縮する。:option:`--export-dpi`
   指定を上書きする。

.. option:: -b, --export-background=COLOR

   ビットマップエクスポートの背景色を指定する。SVG が対応していれば色文字列を使
   用できる。

   If this option is not used, the color specified by the ``pagecolor``
   attribute in the section ``sodipodi:namedview`` of the SVG file will be used
   (if it is defined).

.. option:: -y, --export-background-opacity=VALUE

   エクスポート画像の背景色のアルファー値を指定する。

      Either a number between 0.0 and 1.0 or an integer from 0 to 255 can be
      used, where the smaller number in both cases corresponds to full
      transparency and the larger number corresponds to full opacity.

.. option:: -t, --export-use-hints

   何度も同じオブジェクトをエクスポートする状況で便利なオプションだ：

      If you have previously saved an object to a bitmap image from within
      Inkscape (and saved the file afterward), you can use this option to export
      the object to a bitmap file with the same name and resolution. Must be
      used with the :option:`--export-id` option.

.. option:: -T, --export-text-to-path

   テキストをパスに変換する。最重要オプションの可能性まである：

      The text objects should be converted to paths prior to export to a *PS* or
      *EPS* export. Then ensures that the text will be rendered properly
      regardless of which fonts are installed on a computer that displays or a
      printer that prints the resulting file.

Query Command Line Options
======================================================================

SVG ファイル内のオブジェクトの位置、寸法を確認するコマンドがある。

   The key here is knowing the ID (name) of the object for which you desire the
   information. The ID name must be given. The exported numbers use the SVG
   coordinate system.

対象オブジェクトの ID を実行時に知っている必要があるという点が急所だ。

   Here is an example of finding the *x* position of the zoom-in icon in the
   default icon file on a Linux system:

   .. code:: console

      $ inkscape --query-id=zoom-in -X /usr/share/inkscape/icons/icons.svg

本題とは無関係だが、上記の :file:`icons.svg` に相当するファイルが Windows 版
Inkscape 1.2 のディレクトリー以下に見当たらない。試したい。

.. option:: -I, --query-id=OBJECT-ID[,OBJECT-ID]*

   オブジェクト ID を指定する。

.. option:: -S, --query-all

   全オブジェクト表示に相当する：

      Return a comma separated list of id, x, y, w, and h for all objects
      (including *SVG* file, *Layers*, and *Groups*) in file. Each object is on
      its own line.

   以下のオプションを複数組み合わせて数字を出力すると改行で区切られるので使い勝
   手が悪いが、このオプションは一行に一オブジェクトのデータが出力される。

.. option:: -X, --query-x

   オブジェクトの x 座標を得る。なお、いずれの問い合わせオプションでも座標系は
   SVG 座標系が使われる。

.. option:: -Y, --query-y

   オブジェクトの y 座標を得る。

.. option:: -W, --query-width

   オブジェクトの横幅を得る。

.. option:: -H, --query-height

   オブジェクトの縦幅を得る。

最後の四つのオプションはテキスト処理の観点から使いにくい：

.. code:: console

   $ inkscape -I rect312645 -XYWH drawing.svg
   134.17
   398.69
   14.1732
   14.1732
