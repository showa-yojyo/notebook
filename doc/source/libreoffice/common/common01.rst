======================================================================
Chapter 1, LibreOffice Basics ノート
======================================================================

.. include:: ./common-inc.txt

.. contents:: 章見出し
   :depth: 3
   :local:

Installation and starting LibreOffice
======================================================================

Installation
----------------------------------------------------------------------

Windows では LibreOffice インストール時にショートカットアイコンがデスクトップに
生じるとある。個人的に邪魔なのでこれを削除する。

Starting
----------------------------------------------------------------------

LibreOffice Start Center の使用法について。いちおう確認。

* Start Center に表示されているファイルアイコンを選択すれば、それに対応するアプ
  リケーションが起動することで当該ファイルが開く。
* Start Center で :guilabel:`Templates` を選択し、新規ファイルのテンプレートを選
  択すると、そのテンプレートに関連するアプリケーションが開く。
* :guilabel:`Open File` を選択するとファイルダイアログボックスが開く。そこでファ
  イルを選択し、「開く」ボタンを押すと対応アプリケーションが起動して選択ファイル
  が開く。
* :guilabel:`Remote Files` は選択ファイルがリモートにある場合の方法。

:guilabel:`Filter` ドロップダウンリストに注意。

.. tip::

   Start Center 内にファイルをピン留めすることが可能。

.. note::

   Windows Explorer で LibreOffice アプリケーションに関連するファイルアイコンを
   ダブルクリックすると、対応アプリケーションが必要に応じて起動し、指定ファイル
   が開く。

Closing LibreOffice
----------------------------------------------------------------------

LibreOffice を終了するには、通常の Windows デスクトップアプリケーションに対する
終了手段がそのまま使用可能だ。

* |MenuBar| から :menuselection:`&File-->E&xit` を選択
* キーバインド |Ctrl+Q| を押す
* 開いている文書が一つしかない場合にはアプリケーションウィンドウ右上のバツジルシ
  をクリック

Main LibreOffice window
======================================================================

LibreOffice アプリケーションすべてに共通して、メインウィンドウの上部に Title
バー、Menu バー、Standard ツールバーがあり、ウィンドウの下部に Status バーがあ
る。

特殊な UI も搭載されている。それについては :doc:`common13` 参照。

Title bar
----------------------------------------------------------------------

Title バーに基本的には現在の文書のファイル名が示される。文書が新規作成されると、
文書名は :guilabel:`Untitled X` のようなものになる。ここで X は数字。新規文書に
は作成順に番号が付けられる。

Menu bar
----------------------------------------------------------------------

Writer を例に挙げて Menu バーにあるメニューを解説している。省略。

Toolbars
----------------------------------------------------------------------

LibreOffice のツールバーはそれが見えている場合、docked か floating のどちらかの
状態をとる。

既定では、Standard ツールバーはどのアプリケーションでもウィンドウ上部に docked
であり、二番目のツールバーが何であるかはアプリケーションによって異なる。

特に重要なのは、二番目のツールバーは状況依存型であることだ。通常は何が選択されて
いるかによってツールセットが変化する。そのため、例えば Writer で描画物が選択され
ている場合、描画物の書式設定ツールセットである Drawing Object Properties ツール
バーが Formatting ツールバーに取って代わる。描画物の選択を解除すると、Drawing
Object Properties ツールバーが閉じ、Formatting ツールバーが再び開く。

.. note::

   ツールバーが多いのが嫌な場合、別の UI を検討するといい。:doc:`common13` 参照。

Displaying or closing toolbars
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ツールバーを表示するには :menuselection:`&View-->&Toolbars-->` 以下を調べろ。
チェック印の有無で表示状態がわかる。

Submenus and tool palettes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ツールバーの項目にサブメニューがある場合、ツールアイコンの右側に▼が表示される。
これをクリックすると、さらなるコマンド、ツールパレット、項目を選択する別の方法を
含むサブメニューが表示される。ツールパレットとはツールバーの単一ツールに付属する
ツールのポップアップの集まりだ。ツールパレットは、次の例を使用して floatingツー
ルバーにすることが可能だ。

#. |DrawingToolbar| の Basic Shapes をクリックしてツールパレットを開く。
#. ツールバーハンドル（……に見える部分）をクリックし、ツールパレットを開いている
   文書上めがけてドラッグする。
#. ツールバーハンドルを離すと、ツールパレットは floating ツールバーになる。

.. note::

   ツールバーハンドルが表示されていない場合、ツールパレットまたはツールバーは
   docked 位置に固定されているため、それを解除する必要がある。この次の節を参照。

Locking and unlocking toolbars
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ツールバー全部を完全固定する手段が用意されている。|MenuBar| から
:menuselection:`&View-->&Toolbars-->&Lock Toolbars` を選択するのだ。ただ
し、LibreOffice を再起動する必要がある。このコマンドメニュー項目にチェック印が付
いていれば、ツールバーロックが機能していることを示す。

この状態を解除するには、同じ手順でチェック印を外す。再起動がやはり必要。

ツールバー全部ではなく、単一のツールバーに対して位置を固定したい場合には、ツール
バーの空き地を右クリックして :menuselection:`&Lock Toolbar Position` を選択す
る。項目にチェック印が付く。解除する場合も同じ項目を選択してチェックを外す。

Moving, docking and floating toolbars
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ツールバーが docked かつ固定されていない場合、ツールバーの左端に︙のようなツール
バーハンドルがある。このハンドルはツールバーの位置を制御するためのものだ。

このハンドルをマウスで適当にドラッグすればツールバーの位置がそれらしく移動する。

ツールバーが floating である場合、その移動方法は簡単だ：

* ツールバーのタイトルバーをドラッグする
* ▼をクリックしてドロップダウンメニューから適当なコマンドを実行する

Context sensitive toolbars
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

LibreOffice のツールバーの中には、物が選択されたとき、またはキャレットがテキスト
内に置かれたときにしか開かない、状況依存型のものがある。例:

* 表組にキャレットが置かれると |TableToolbar| が開く
* 順序付き一覧または順序なし一覧にキャレットが置かれると、|BnNToolbar| が開く
* 画像が選択されると |ImageToolbar| が開く

Customizing toolbars
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To customize a toolbar, you can add tools listed in Visible Buttons, or add new tools to a toolbar.
Also, you can access the customization options for a toolbar by right-clicking in an empty space
on a docked toolbar or clicking on the downward triangle ▼ on the title bar of a floating toolbar to
open a context menu:
•

To open the Customize dialog an add more tools to the toolbar, select Customize
Toolbar. If you need more information on customization, see Chapter 13, Customizing
LibreOffice.

•

To dock the selected floating toolbar in its default position, select Dock Toolbar. The
toolbar can be moved to a different docked position.

Main LibreOffice window | 29

•

To dock all floating toolbars in their default positions, select Dock All Toolbars. The
toolbars can be moved to different docked positions.

•

To lock a docked toolbar into its docked position, select Lock Toolbar Position.

•

To close the selected toolbar, click on the X on the right of the toolbar title bar or select
Close Toolbar.

•

Finally, you can select Visible Buttons and select the required tool from the options in
the context menu. Tools already installed on a toolbar are indicated by a check mark next
to the tool icon. The tools are added to the toolbar in the same order as the tools appear
in the context menu. That is, the top tool in the Visible Buttons list is positioned at the
left end of the toolbar. The remaining tools are positioned on the toolbar in a position that
matches its list position.

Context menus
----------------------------------------------------------------------

Context menus, which provide quick access to many menu functions, can be opened by rightclicking on a paragraph, graphic, or other object. When a context menu is opened, the available
functions or options depend on the object that has been selected. A context menu is the easiest
way to use a function or option, especially if its location in the menus or toolbars is not known.
Context menus can also display applicable keyboard shortcuts if one has been created, or tool
icons if available. To use these options, go to Tools > Options > LibreOffice > View (macOS
LibreOffice > Preferences LibreOffice > View) and select the options available in Visibility.

Status bar
----------------------------------------------------------------------

The Status bar is located at the bottom of the workspace. It provides information about the
document and also include convenient ways to change some features quickly. It is similar in
Writer, Calc, Impress, and Draw, but each LibreOffice module includes some module-specific
items. To hide the Status bar, go to View on the Menu bar and deselect Status Bar.
The Impress Status bar is shown in Figure 7 and it has the following components:
Slide number
The slide number currently displayed in the Impress Workspace and the total number of
slides in the presentation.
Information area
Changes depending on the object selected on the current Impress slide. Examples shown
in Table 3.
Table 3: Examples of information
Example selection
Text area
Charts, spreadsheets

30 | Chapter 1, LibreOffice Basics

Examples of information shown
Text Edit: Paragraph x, Row y, Column z
Embedded object (OLE) “ObjectName” selected

Figure 7: The Impress Status bar
1)
2)
3)
4)

Slide number
Information area
Master slide
Cursor position

5)
6)
7)
8)

Object size
Unsaved changes
Digital signature
Text language

9)
10)
11)

Fit slide
Zoom slide
Zoom percentage

Master slide
The master slide associated with the slide or notes pages in the Workspace. You can
right-click this area to view a list of available master slides in Impress. If necessary you
can select a master slide and apply it to the current slide. Double-click to open the
Available Master Slides dialog.
Cursor position/Object size
Shows different information depending on which Impress objects are selected or not:
– When no object is selected, Impress displays the current position (X and Y
coordinates) of the cursor.
– When an object is selected and being resized, this area of the Impress Status bar
shows the size of the object (width and height).
– If an object is currently selected in Impress, the position numbers shows X and Y
coordinates of the upper-left corner and the object size number pair displays the size
of the object. These numbers do not relate to the object itself, but to the selection
outline, which is the smallest possible rectangle that can contain the visible parts of
the object.
– When an object is selected, clicking in these areas opens the Position and Size
dialog.
Unsaved changes
Indicates if there are any unsaved changes in the Impress presentation. Clicking on this
icon saves the document. If the presentation has not been saved before, the Save As
dialog opens giving the opportunity to save the presentation.
Digital signatures
Indicates if the Impress presentation has a digital signature.
Text language
Indicates the language used for any text in an Impress presentation.
Fit slide
When this icon is selected, the displayed slide in the Impress Workspace zooms to fit in
the Workspace.
Zoom slider
When this slider is moved, the slide displayed in the Impress Workspace will adjusts how
the document is viewed (by percentage) in the Workspace.

Main LibreOffice window | 31

Zoom percentage
Indicates the zoom level of the slide displayed in the Impress Workspace. Clicking on
zoom percentage opens the Zoom & View Layout dialog where the settings for zoom
factor and view layout are adjusted.

Sidebar
----------------------------------------------------------------------

By default, the Sidebar is on the right side of a LibreOffice module’s Workspace. An example of
the Writer Sidebar is shown in Figure 8. Go to View > Sidebar on the Menu bar to display or hide
the Sidebar.
The Sidebar contains several decks and each deck contains tools and options for formatting a
document. The number and type of decks used in the Sidebar depend on the type of document
and the current LibreOffice module. Decks are organized into panels and an icon bar on the right
side of the Sidebar allows switching between the different decks.

Figure 8: Example of Properties deck in Writer Sidebar
For all LibreOffice modules, each Sidebar contains Properties, Styles, Gallery, and Navigator
decks. Some LibreOffice modules also have additional decks:
Page and Style Inspector for Writer
Master Slides, Animation, Shapes, and Slide Transition for Impress
Shapes for Draw
Functions for Calc
In LibreOffice, menus, toolbars, and Sidebar panels share many functions across modules. For
example, text can be made bold or italic with the Format menu, the Formatting toolbar, or the
Properties deck. Some Sidebar panels also have a More Options button, which opens a dialog
with additional editing controls. For more detail on options available on the Sidebar, see the
guides for each LibreOffice module.

32 | Chapter 1, LibreOffice Basics

To hide the Sidebar, click on Hide/Show button on the left of the Sidebar (highlighted in
Figure 8). To show the Sidebar, click on the Hide/Show button again.
To undock the Sidebar and make it floating, do the following:
1)

Click on Sidebar Settings at the top right, do the Sidebar.

2)

Select Undock from the options available, or use the keyboard shortcut
Ctrl+Shift+F10 (macOS ⌘+Shift+F10).

To dock the Sidebar into its usual position on the main window, do the following:
1)

Click on Sidebar Settings at the top right of the Sidebar.

2)

Select Dock from the options available, or use the keyboard shortcut Ctrl+Shift+F10
(macOS ⌘+Shift+F10).

Working with documents
======================================================================

New documents
----------------------------------------------------------------------

LibreOffice has multiple methods for creating a new document:
•

Open the LibreOffice Start Center then click on the name of a LibreOffice module. For
example, click on Impress Presentation and a new presentation is created.

•

Click on Templates in the Start Center and the available LibreOffice templates are
displayed. Click on the required template to create a new file and the LibreOffice module
opens with a new document.

•

Go to File > New on the Menu bar and select the type of document from the submenu
that opens. The applicable LibreOffice module also opens.

•

Click on the downward triangle ▼ next to New on the Standard toolbar and select the
type of document from that context menu. For example, click on Drawing and a new
drawing is created. The applicable LibreOffice module also opens.

•

Click on New on the Standard toolbar and a new document is created by the LibreOffice
module. For example, if Writer is open and active, this icon will create a new Writer
document.

•

Use the keyboard shortcut Ctrl+N (macOS ⌘+N) to create a new document. The type
of document created depends on which LibreOffice module is open and active. For
example, if Calc is open and active, a new spreadsheet is created.

•

Go to File > Wizards on the Menu bar and select the type of document from the options
available in the submenu.

Opening existing documents
----------------------------------------------------------------------

To open an existing LibreOffice document in the appropriate module, use one of the following
methods. .
•

Click Open File in the Start Center and select the file.

•

Go to File > Open on the Menu bar and select the file.

•

Click on Open on the Standard toolbar and select the file.

•

Use the keyboard shortcut Ctrl+O (macOS ⌘+O) and select the file.

•

Click Recent Documents in the Start Center and select a recent file from the Center.

Working with documents | 33

•

Go to File > Recent Documents on the Menu bar and select the file from the files
displayed in the context menu.

Notes
Note that the previous names or locations of files that have been renamed or
relocated may still be in the Start Center, and clicking on those types of filenames
will generate an error. To remove the file from the Start Center, hover the cursor
over the thumbnail until an X appears in the upper right corner, and then click on
the X.
When you are selecting a LibreOffice file from the Start Center, Open dialog, or
file browser you can limit the files seen by file type. For example, you select Text
Documents as the file type, only documents that Writer can open are displayed.
If you need to work with files on remote servers, see Chapter 10, Working with
File Formats, Security, and Exporting.
Also, LibreOffice can open files compatible with the Open Document Format
(ODF), which includes many formats from Microsoft. For example, LO can open
MS Word files (*.doc or *.docx) in Writer, MS Excel files (*.xls or *.xlsx) can be
opened in Calc; MS PowerPoint files (*.ppt or *.pptx) can be opened in Impress,
and so on. See Chapter 10, Working with File Formats, Security and Exporting for
more information about working with different file types.

Saving documents
----------------------------------------------------------------------

LibreOffice documents can be saved with one of the following methods:
•

Save — can save all changes made, keeping the current filename and location of the file.
– Go to File > Save on the Menu bar.
– Use the keyboard shortcut Ctrl+S (macOS ⌘+S).
– Click on Save on the Standard toolbar.

•

Save As — can create a new document, change the filename or file format, or save the
file in a different location on a computer system.
– Go to File > Save As on the Menu bar.
– Use the keyboard shortcut Ctrl+Shift+S (macOS ⌘+Shift+S).
– Click on the downward triangle ▼ next to Save on the Standard toolbar and select
Save As from the context menu.

•

Save a Copy — can save a copy of the current document, for example, in a different
location on the computer system. The current document remains open for more editing.
– Go to File > Save a Copy on the Menu bar.
– Click on the downward triangle ▼ next to Save on the Standard toolbar and select
Save a Copy from the context menu.

•

Save All — can save all the files that are open in LibreOffice. Go to File > Save All on
the Menu bar. This option is only available when more than one LibreOffice document is
open.

34 | Chapter 1, LibreOffice Basics

Saving documents automatically
----------------------------------------------------------------------

If you need LibreOffice to save files automatically, you can use the AutoRecovery function. When
files are saved automatically, LibreOffice will overwrite the last saved state of the file. To set up
automatic file saving, do the following:
1)

Go to Tools > Options > Load/Save > General (macOS LibreOffice > Preferences >
Load/Save > General) on the Menu bar.

2)

In Save, select the option AutoRecovery information every and set the time interval in the
box, for example 10 minutes.

3)

Click OK to save the selection and close the dialog.

Using the Navigator
----------------------------------------------------------------------

The Navigator is available as a dialog or Sidebar deck, and it lists all objects contained in a
document in categories. Examples can be seen in examples from Impress and Writer (Figure 9
and Figure 11). The Navigator can be opened with one of the following methods:
•

Navigator dialog: go to View > Navigator on the Menu bar, or use the keyboard shortcut
F5 for Windows and macOS, or Ctrl+Shift+F5 for Linux.

•

Navigator deck on the Sidebar: click on the Navigator icon on the right of the Sidebar, or
use the keyboard shortcut Alt+Ctrl+4 for Windows and Linux, or ⌥+⌘+4 for macOS.

•

To close the Navigator, click on the X on the right of the title bar, or use the keyboard
shortcut. The categories are specific to each LibreOffice module. Click on the right
chevron > next to each category name to open the list of objects contained in each
category. Also, the Navigator provides some functions that are specific to each
LibreOffice module.

Figure 9: Example of Impress Navigator dialog
The Navigator provides an easy method of locating and selecting objects in a document. If
possible you should give each object an easily identified name so you can easily locate an
object, instead of using default names such as Sheet1, Table1, or Image2, and so on. Right-click
on an object in the Navigator dialog, or Sidebar deck and select Rename from the context menu.

Working with documents | 35

Figure 10: Example of separate windows list

Figure 11: Example of Navigator deck in Writer Sidebar

Displaying multiple view of a document
----------------------------------------------------------------------

Users can open multiple views of the same document in LibreOffice. Each view can be displayed
in their own windows and LibreOffice can show different pages, use different zoom levels, or use
other settings. When a user makes a change to the document in one window, it will be reflected
in the other windows. For example, when using Writer, separate views of a document can be
used for copying or moving information from one page to another.
To open a new document window, go to Window > New Window on the Menu bar. In each open
window, the filename of the document will be displayed in the title bar. Figure 10 shows how
separate views of one document can be open at the same time. If other LibreOffice documents
are open at the same time, the LibreOffice windows list also includes these other documents and
the active window has a check mark by its filename. You can switch between windows by clicking
on a name in the list or by clicking on the window itself if it is visible on the display.
To close a window, go to Window > Close Window on the Menu bar, use the keyboard shortcut
Ctrl+W (macOS ⌘+W).
36 | Chapter 1, LibreOffice Basics

Undoing and redoing changes
----------------------------------------------------------------------

Undoing
To undo the most recent change in a document, use one of these methods:
•

Use the keyboard shortcut Ctrl+Z (macOS ⌘+Z).

•

Click on Undo in the Standard toolbar.

•

Go to Edit > Undo on the Menu bar.

•

Click the small triangle ▼ to the right of Undo on the Standard toolbar to open a list of
changes that can be undone. Multiple consecutive changes can be selected and deleted
at the same time.

Redoing
After changes have been undone, changes can be redone using one of the following methods:
•

Use the keyboard shortcut Ctrl+Y (macOS ⌘+Y).

•

Click on Redo in the Standard toolbar.

•

Go to Edit > Redo on the Menu bar.

•

Click the small triangle ▼ to the right of Redo on the Standard toolbar to open a list of
undo commands that can be redone. LibreOffice can select multiple consecutive undo
commands and redo them at the same time.

Repeating undo and redo commands
Repeating undo and redo commands can save several repetitive menu navigation clicks, or
keyboard shortcuts, especially when a command is taken from a context menu or submenu. To
repeat the last undo or redo command applied to a document, use one of the following methods:
•

Use the keyboard shortcut Ctrl+Shift+Y (macOS ⌘+Shift+Y).

•

Go to Edit > Repeat on the Menu bar.

Reloading documents
----------------------------------------------------------------------

If you reload a document in LibreOffice, all the changes made in an editing session after the last
save are discarded. To reload a document, go to File > Reload on the Menu bar.

Note
If you reload a document, a confirmation dialog will open and warn the user that
reloading will discards the last unsaved changes.

Closing documents
----------------------------------------------------------------------

Close a LibreOffice document with one of the following methods:
•

Go to File > Close on the Menu bar.

•

In Windows or Linux — click on the X at the right end of the Menu bar.

•

In macOS — click on the red button at the left end of the title bar.

If the document to be closed is the only document that is open, the following happens:
•

In Windows or Linux — the document closes and the LibreOffice Start Center opens.

•

In macOS — the document closes and the Menu bar remains at the top of the screen.
Working with documents | 37

Note
If the document has not been saved since the last change, a confirmation dialog
opens with a warning message. Select whether to save, or discard, the changes
before closing.

Printing
======================================================================

Default printer
Here are examples of how to setup a default printer on a computer in LibreOffice. The method
will vary depending on the computer and its operating system.

Notes
When printing, the name of the default printer installed on a computer appears in
the Print tool name, Print Directly tool name, Print dialog, and Printer Settings
dialog.
For more information about printing the different types of documents that
LibreOffice can create, see the user guides for each LibreOffice module.
Printing options are not available when viewing a LibreOffice Base table or query.

Windows
1)

Open Settings, then go to Devices > Printers & scanners.

2)

Select a printer from the displayed list.

3)

Select Manage > Set as default and then close Settings.

Linux
1)

Open Settings, then go to Printers.

2)

Select a printer from the displayed list.

3)

Click on the settings icon on the right of the printer name.

4)

Select Use Printer by Default from the drop-down list and close Settings.

macOS
1)

Open System Settings, then open Printers & Scanners.

2)

In Default printer select the printer to use as default printer from the drop-down list, then
close Settings.

Figure 12: Draw Standard toolbar with Print Directly installed

Quick printing
----------------------------------------------------------------------

LibreOffice can do “quick printing,” which prints an entire open document is printed using the
computer’s default printer. To quick print, click on Print Directly on the Standard toolbar.
If Print Directly is not visible on the Standard toolbar, it can be installed as follows:
1)

Right-click in a blank area on the Standard toolbar to open a context menu.

38 | Chapter 1, LibreOffice Basics

2)

Select Visible Buttons from the context menu.

3)

Select Print Directly from the list of available tools to install it on the Standard toolbar, as
shown by the highlighted example in Figure 12.

Printer setup
----------------------------------------------------------------------

LibreOffice’s Printer Setup dialog has the following options:
Printer
Lists information that applies to the selected printer. If the list is empty, install a default
printer for the computer. Refer to the printer and computer user guides for more
information on connecting printers.
Name
Lists the installed printers on the computer. To change the default printer, select a printer
name from the drop-down list.
Status
Describes the current status of the selected printer.
Type
Displays the type of printer that is selected.
Location
Displays the computer connection for the selected printer.
Comments
Displays additional information for the printer.
Properties
Changes the printer settings of the computer operating system for the current document.
Make sure that the layout orientation (Landscape or Portrait) matches the page format set
in Format > Page on the Menu bar.
Options
Opens the Printer Options dialog box allowing the global printer options set in Tools >
Options > LibreOffice Writer or LibreOffice Calc > Print (macOS LibreOffice >
Preferences > LibreOffice Writer or LibreOffice Calc > Print) to be overridden when
printing the current document.

Note
Options in the Printer Settings dialog is only available in LibreOffice Writer and
Calc.
Here is an example of setting up a printer on a computer for LibreOffice:
1)

Connect the printer to the computer. Refer to the printer and computer user guides for
more information on connecting printers.

2)

Go to File > Printer Settings on the Menu bar to open a Printer Setup dialog. Figure 13
shows an example of a Printer Setup dialog.

3)

Click on Options in Printer Setup dialog to open the Printer Options dialog. Figure 14
shows an example of a Printer Options dialog.

4)

Select the required printer options, then click on OK to save the selection and close the
Printer Options dialog.

Printing | 39

Figure 13: Example of a Printer Setup dialog

Figure 14: Example of Printer Options dialog
5)

If necessary, click on Properties in the Printer Setup dialog to open a properties dialog
for the default printer.

6)

Select the required properties, then click on OK to save the selection and close the
properties dialog.

7)

Click OK to save the printer setup and close the Printer Setup Dialog.

40 | Chapter 1, LibreOffice Basics

LibreOffice printing options
----------------------------------------------------------------------

General printing options
After you install a printer on a computer, the general printing options for LibreOffice can be
customized. Go to Tools > Options > LibreOffice > Print (macOS LibreOffice > Preferences >
LibreOffice > Print) to open the Options LibreOffice Print dialog (Figure 15). The general print
options for LibreOffice are as follows:
Settings for
Specifies whether the print settings apply to direct printing or to printing to a file.
Defaults
Convert colors to grayscale
Specifies that all colors in a document are printed only as greyscale.
Include transparent objects
If selected, the reduction in print quality for bitmaps also applies to the transparent
areas of objects.

Figure 15: Options LibreOffice Print dialog
Reduce bitmaps
Specifies that bitmaps are printed with reduced quality. The resolution can only be
reduced and not increased.
Resolution
Specifies the maximum print quality in DPI. The resolution can only be reduced and not
increased.
High print quality
High print quality corresponds to a resolution of 300dpi.
Normal print quality
Normal print quality corresponds to a resolution of 200dpi.

Printing | 41

Note
Reducing the amount of data sent by LibreOffice to the printer increases the print
speed because the print files are smaller. This makes it easier for printers with a
smaller memory when printing large files. However, reducing print data can result
in slightly lower print quality.
Reduce transparency
If selected, transparent objects are printed like normal, non-transparent objects,
depending on your selection in the following two option buttons.
Automatically
Specifies that the transparency is only printed if the transparent area covers less than a
quarter of the entire page.
No transparency
When selected, a transparency does not print.

Note
Transparencies cannot be sent directly to a printer. Transparencies must be
visible to be calculated by LibreOffice as bitmaps and sent to the printer.
Depending on bitmap size and the print resolution, a large amount of data may be
generated.
Warnings
Defines which warnings appear before printing begins.
Paper size
Select this option if a certain paper size is required for printing the current document. If
the paper size used in the document is not provided by the current printer, an error
message opens.
Paper orientation
Select this option if a certain paper orientation is required for printing the current
document. If the format used by the current document is not available from the printer,
an error message opens.
Transparency
Select this option if a warning is required if transparent objects are contained in the
document. When printing a document with transparencies, a dialogue box opens to
enable selection if the transparency is to be printed.
Reduce gradient
If selected, gradients are printed with reduced quality.
Gradient stripes
Specifies the maximum number of gradient stripes for printing.
Intermediate color
Specifies that gradients are only printed in a single intermediate color.

LibreOffice modules printing options
----------------------------------------------------------------------

To open the printing options dialog for each LibreOffice module, go to Tools > Options >
LibreOffice module name > Print (macOS LibreOffice > Preferences > LibreOffice module
name > Print). The different print settings for each LibreOffice module are summarized in
Table 4. For more information, refer to the specific user guide for each module.

42 | Chapter 1, LibreOffice Basics

Table 4: Print options in LibreOffice modules
Feature
Writer
Select pages, sheets, or slides
Yes
to print
Print multiple pages, sheets, or
Yes
slides on one page
Print a brochure
Yes
Print envelopes
Yes
Print labels or business cards Yes
Preview pages or sheets before
Yes
printing

Calc

Impress

Draw

Math

Yes

Yes

Yes

Yes

Yes

Yes

Yes

No

No
No
No

Yes
No
No

Yes
No
No

No
No
No

Yes

No

No

No

Controlling printing
----------------------------------------------------------------------

For more control over printing, open the Print dialog with one of the following methods:
•

Go to File > Print on the Menu bar.

•

Use the keyboard shortcut Ctrl+P (macOS ⌘+P).

•

Click on Print on the Standard toolbar.

General printing options — Windows or Linux
These printing options are available in the Impress Print dialog’s General page for Windows or
Linux (Figure 16).
Printer
Select the printer to use from the printers available in the drop-down list.
Properties
Click on Properties to open the properties dialog for the printer being used. The options
available in this dialog depends on the type of printer connected to the computer and the
computer operating system being used.
Range and Copies
All Slides
Prints all the slides in the presentation.
Selection
Prints the slides selected in LibreOffice Impress.
Slides
Select the page number(s) to print. For multiple pages, use the format 1, 3, 7 or 1 – 5,
7, 9 for page number selection.
Include
Select from the drop-down list Odd and Even Pages, Odd Pages, or Even Pages.
More > Paper sides
Select from the drop-down list Print on one side (simplex), Print on both sides (duplex
long edge), or Print on both sides (duplex short edge).
More > Number of copies
Enter number of printed copies required for the document.
More > Collate
Collates multiple printed copies into separate documents.

Printing | 43

More > Order
Select from Create separate print jobs for collated output (only available when more
than one copy is being printed) or Print in reverse order.

Figure 16: Impress Print dialog — Impress General page — Windows or Linux
Page Layout
Paper size
Select the paper size to use from the drop-down list.
Orientation
Select from the drop-down list Automatic, Portrait, or Landscape.
More > Pages per sheet
Select from the drop-down list how many pages are printed on one sheet of paper.
More > Order
Select from the drop-down list the printing order of multiple pages on one sheet of
paper.
More > Draw a border around each page
When multiple slides are printed on one sheet of paper, a border is drawn around each
slide.
More > Brochure
Prints the document so the pages can be folded into a brochure or booklet.

General printing options — macOS
The following general options are an example of the options available on the General page of the
Impress Print dialog in macOS (Figure 17).
44 | Chapter 1, LibreOffice Basics

Printer
Select the printer to be used from the drop-down list. If the default printer is being used,
then this printer will already be selected.
Presets
Select from the drop-down list a printing preset. The presets available depend on the type
of printer connected to the computer. This also includes any custom presets that have
been created.
Copies
Enter the number of copies to be printed.
Pages
All
Prints all the pages in the document.
From: to:
Select the page number(s) to print. For multiple pages, use the format 1, 3, 7 or 1–5, 7,
9 for page number selection.
Print in Color
If the printer selected is capable of color printing, this selection can be switched off to print
the presentation in monochrome.
Double-Sided
Select this option to print the presentation double sided if the printer selected is capable
of double sided printing.
Media & Quality
Feed from
Allows you to select which paper tray to use from a drop-down list (if the printer has
more than one paper tray).
Media Type
Select the paper type that has been loaded into the paper tray from the drop-down list ,
(for example Envelope, Photo, Plain Paper).
Quality
Select the required level of printing quality.
Layout
Pages per sheet
Select how many slides are printed on one sheet of paper rom the drop-down list.
Layout Direction
Select the printing order of multiple slides on one sheet of paper.
Border
When multiple slides are printed on one sheet of paper, a border is drawn around each
slide.
Two-Sided
Determine how a multi-page document will be bound from a drop-down list: Off; LongEdge binding; Short-Edge binding, Booklet.
Reverse page orientation
If LibreOffice prints the slides in the wrong order, select this option and print the
document again.
Flip horizontally
If LibreOffice prints the pages in the wrong orientation, select this option and print the
document again.

Printing | 45

Figure 17: Print dialog — Impress General page — macOS
Paper Handling
Collate sheets
Allows selected multiple printed copies to be collated into separate documents.
Sheets to Print
Select which slides in the document to print from the drop-down list: (All pages; Odd
only; Even only).
Sheet Order
Selects the page printing order from the drop-down list: Automatic; Normal; Reverse.
Scale to fit paper size
Adjusts the printed slide to fit the paper size.
Destination Paper Size
Only available if Scale to fit paper size has been selected. Selects a paper size from
the options available in the included drop-down list.
Scale down only
Select this option to reduce slide size to fit the paper. Only available if the paper size is
smaller than the slide size.
Watermark
Provides options to print watermark text on the slides, for example Confidential if the
presentation is of a sensitive nature.
Printer info
Shows the details of the selected printer.

46 | Chapter 1, LibreOffice Basics

LibreOffice module printing options
For more information on using specific printing options available in each LibreOffice module, see
the User Guide for each LibreOffice module. For example, specific printing could be for:
Individual pages, slides, or drawings.
Range of pages, slides, or drawings.
Selection of text, or graphics (Writer).
Individual sheets, range of sheets, or selected cells (Calc).
Handouts, outlines, or notes (Impress).
Envelopes, labels, or business cards (Writer).

Brochure printing
----------------------------------------------------------------------

In Writer, Impress, and Draw, documents can be printed in the correct order to form a booklet or
brochure. Below are some examples. Actual brochure printing procedure depends on the
computer operating system and type of printer being used. You may need to experiment to find
the correct method for brochure printing.

Single sided printing
This is an example of how you can create a brochure or booklet with a printer that can only print
single sided pages.
1)

Open the Print dialog using one of the following methods:
– Go to File > Print on the Menu bar.
– Use the keyboard shortcut Ctrl+P (macOS ⌘+P).
– Click on Print on the Standard toolbar.

2)

Click on General to open the page for general print options and, if necessary, select a
printer from the Printer drop-down list of printers available.

3)

Click on Properties to open the printer properties dialog for the printer being used and
check the printer is set to the same page orientation as specified for the page setup for
the pages. Usually page orientation does not matter, but it is important for brochures.

4)

Click OK to close the properties dialog and return to the Print dialog.

5)

In Range and Copies, select All Slides. A minimum of four slides is required to create a
brochure.

6)

In Range and Copies, select the Number of copies required to match the required
number of brochures.

7)

In Layout, select Brochure.

8)

In Range and Copies, select Even slides option in Include.

9)

Click OK to print the even slides in the presentation.

10)

Take the printed pages out of the printer and put them back into the printer in the correct
orientation to print on the other side of the paper. It may be necessary to experiment to
find out the correct arrangement for the printer being used.

11)

In Range and Copies, select Odd slides option in Include.

12)

In Range and Copies, select the same Number of copies used for printing the even
slides.

13)

Click OK to print the odd slides in the presentation and close the Print dialog.

14)

Assemble the brochures and bind them, if necessary.

Printing | 47

Double sided or duplex printing
Printing a brochure with a printer that is capable of double sided, or duplex printing, makes the
task of creating brochures simpler.
1)

Open the Print dialog using one of the following methods:
– Go to File > Print on the Menu bar.
– Use the keyboard shortcut Ctrl+P (macOS ⌘+P).
– Click on Print on the Standard toolbar.

2)

Click on General to open the page for general print options and, if necessary, select a
printer from the Printer drop-down list of printers available.

3)

Click on Properties to open the printer properties dialog for the printer being used and
check the printer is set to the same page orientation (as specified for the page setup for
the slides). Page orientation is especially important for brochures.

4)

Click OK to close the properties dialog and return to the Print dialog.

5)

In Range and Copies, select All Slides. A minimum of four slides is required to create a
brochure.

6)

In Range and Copies, select Print on both sides (duplex long edge) or Print on both
sides (duplex short edge) option. Normally, long edge binding is used for portrait printing
and short edge binding is used for landscape printing.

7)

In Range and Copies, select the Number of copies required to match the required
number of brochures.

8)

In Range and Copies, select the Collate option. This option is only active when printing
multiple copies of the same document.

9)

In Layout, select Brochure.

10)

Click OK to close to the Print dialog and print the required number of pages for the
brochures.

11)

If necessary, bind the brochures to match either long edge or short edge binding.

Figure 18: Print Preview toolbar

Print previewing
----------------------------------------------------------------------

A document can be previewed before it is printed in the Writer and Calc modules. Print
previewing is useful, especially when printing a document double-sided making sure there are no
errors before the document is printed. Print previewing is opened as follows:
1)

Open Print Preview using one of the following methods. The Print Preview toolbar
(Figure 18) opens and the Formatting toolbar closes:
– Go to File > Print Preview on the Menu bar.
– Click on Toggle Print Preview on the Standard toolbar.
– Use the keyboard shortcut Ctrl+Shift+O (macOS ⌘+Shift+O).

2)

Select the required preview from Single Page Preview, Two Pages Preview, Book
Preview, or Multiple Pages Preview.

48 | Chapter 1, LibreOffice Basics

3)

To print the document from Print Preview, click Print on the Print Preview toolbar to open
the Print dialog, then select the printing options and click OK (macOS Print).

4)

To close the preview, click on Close Preview on the Print Preview toolbar. The document
switches back to normal view and the Formatting toolbar reopens replacing the Print
Preview toolbar.

Note
When a document is in Print Preview mode, the document cannot be edited. If
necessary, click on Book view in the Status Bar to display the document in book
format. The document can be edited when using Book view on the Status bar.
Click on Single page view to return the document to normal view.

Using Safe Mode
======================================================================

Safe Mode is used to restore LibreOffice after it has stopped working, fails to launch correctly, or
a file has become corrupted. It starts LibreOffice with a fresh user profile and disables hardware
acceleration.
Go to Help > Restart in Safe Mode on the Menu bar to open the Safe Mode dialog (Figure 19).

Note
It is recommended to use Safe Mode options from the top down (Figure 19)
because the options get more extreme from the top down.
Restore from backup
If you suspect that the problems were caused by recent changes to LibreOffice’s working
state, this option may help you. Since LibreOffice keeps backups of previous
configurations and activated extensions, Restore from backup will allow you to restore the
user configuration, installed extensions (or both), to a previous known working state.
Configure
This Safe Mode option disables either all user extensions, hardware acceleration, or both
functions. This may help you if there are crashes on startup or visual glitches that are
often related to hardware acceleration.
Extensions
If you think that a corrupted extension is blocking or causing LibreOffice to crash, this
option will uninstall all user extensions and reset the state of any shared or bundled
extensions. In the case of shared, or bundled extensions, the option only works if a user
has the proper system access rights. It should be used with caution.
Reset to factory settings
If all of the above fails, this function will reset the settings and user interface modifications
(or the entire user profile) back to factory defaults.
Reset settings and user interface modifications
This function resets any user interface and configuration changes, but keeps items such
as personal dictionary, templates, and so on.
Reset entire user profile
This function erases all customized options and returns a user profile to the factory
default state.

Using Safe Mode | 49

Continue in Safe Mode
If you need to continue in Safe Mode, it allows you to work in LibreOffice with a temporary
profile that was created on startup. Any extensions or configuration options set up
previously have to be reconfigured before using. Keep in mind that any changes made to
the temporary user profile are lost after a restart.

Figure 19: Safe Mode dialog
Restart in Normal Mode
If you have started Safe Mode accidentally, this option discards any changes, terminating
Safe Mode, and restarting LibreOffice normally.
Apply Changes and Restart
Select this option to apply any of the above changes and restart LibreOffice.

Note
If problems are not solved using Safe Mode, selecting Advanced provides
instructions on receiving further aid.
Advanced can allow you to create a zip file of a corrupted user profile, and this
file can be uploaded to the bug tracking system for further investigation by the
LibreOffice developers. Remember that an uploaded user profile may also contain
sensitive information such as installed extensions, personal dictionaries, and
user-specific settings.

50 | Chapter 1, LibreOffice Basics

Getting Started Guide 7.6

----

.. rubric:: 章末注
