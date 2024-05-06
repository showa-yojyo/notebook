======================================================================
Calc Guide Chapter 7, Printing, Exporting, Emailing, and Signing ノート
======================================================================

.. include:: ./calc-inc.txt

.. contents:: 章見出し
   :local:

Printing
======================================================================

Quick printing
----------------------------------------------------------------------

|StandardToolbar| に :guilabel:`Print Directly` ボタンを表示させておくと便利だ。

.. note::

   :guilabel:`Print Directly` 図像の動作を変更して、計算機の既定印刷機ではなく、
   文書に定義されている印刷機に文書を送信することが可能だ。それには |OptionsDlg|
   で |LoadSaveGeneralPage| に進み、:guilabel:`Load printer settings with the
   document` をオンにする。

Controlling printing
----------------------------------------------------------------------

印刷をさらに制御するには |PrintDlg| を開く。次のいずれかで開く：

* |MenuBar| から |FilePrintM| を選択
* |StandardToolbar| から :guilabel:`Print` 図像をクリック
* キーバインド |Ctrl| + :kbd:`P`

:guilabel:`Pre&view` チェックボックスをオンにすると便利だ。

.. note::

   |PrintDlg| で選択したオプションはこの文書の印刷にしか適用されない。

   LibreOffice の既定印刷設定を指定するには |OptionsDlg| の次の場所で行う：

   * |LibreOfficePrintPage|
   * |CalcPrintPage|

   詳細については |Calc15| を見ろ。

|PrintDlg| にはタブが複数あり、以降で説明するようにさまざまな選択肢がある。使用
する計算機の OS によっては本章の図版と現況が異なる場合がある。

|PrintDlg| には :guilabel:`Pre&view` チェックボックスがあり、印刷ページでデータ
がどのように表示されるかのオンオフを切り替えることができる。プレビューはダイアロ
グの左側に描画される。隣接するコントロールで複数のページを巡ることができる。

General tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rubric:: Printer

印刷機自体の選択、それに対するオプション設定を行う。

.. rubric:: Range and Copies

次を指定する：

* 印刷するシートとページ
* 片面印刷または両面印刷
* 印刷部数
* 複数部数を丁合するかどうか
* 印刷するページの順序

:guilabel:`Page Layout` では次を指定する：

* 用紙サイズ
* 縦向き、横向き
* 用紙当たりに印刷するページ数
* 用紙内で印刷する順番
* 各ページの周囲に枠線を引くかどうか

LibreOffice Calc tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

空のページをどう扱うかを指定するだけか。

Printing multiple pages on a single piece of paper
----------------------------------------------------------------------

スプレッドシートの複数ページを紙一枚に印刷する手順：

#. 上述の手順で |PrintDlg| を開く。
#. |GeneralTab| :guilabel:`Page Layout` 区画 :guilabel:`Pages per sheet` ドロッ
   プダウンリストで用紙一枚当たりに印刷するシートのページ数を選択する。
#. 用紙一枚にページを複数印刷する場合には :guilabel:`Order` ドロップダウンリスト
   で印刷順序を選択する。
#. シートの各ページを区別するには :guilabel:`Dra&w a border around each page` を
   オンにする。
#. :guilabel:`&Print` を押す。

.. ここに来る tip のノートは不要

Selecting what to print
----------------------------------------------------------------------

:guilabel:`&From which` ドロップダウンリストで :guilabel:`Print All Sheets` を選
択すると、文書内のシートすべてが印刷される。単一シート、複数シート、セルを選択し
て印刷することも可能だ。

シートを一枚ずつ or シート範囲を印刷する手順：

#. スプレッドシートでシートタブをクリックして印刷対象シートを選択する。シートを
   複数選択する方法については |Calc01| を見ろ。
#. 上述の方法で |PrintDlg| を開く。
#. :guilabel:`&From which` ドロップダウンリストで `Print Selected Sheets` を選択
   する。
#. :guilabel:`&Print` を押す。

セルの選択を印刷する手順：

#. スプレッドシートで印刷するセルを選択する。
#. |PrintDlg| を開く。
#. :guilabel:`&From which` ドロップダウンリストで `Print Selected Cells` を選択
   する。
#. :guilabel:`&Print` を押す。

Printing in grayscale on a color printer
----------------------------------------------------------------------

彩色印刷機でもスプレッドシートを白黒印刷したい場合がある。

.. note::

   印刷機によっては、選択した設定に無関係に色で印刷されることがある。

個々のファイルについて、印刷機設定を変更して白黒印刷することが可能。

#. |PrintDlg| を開く。
#. :guilabel:`Pr&operties...` ボタンを押す。
#. この画面は印刷機によって異なるが、色設定の項目があるはずだ。白黒印刷が有効に
   なるオプションを選択する。

LibreOffice の設定を変更すると、すべての色テキストと画像を無彩色印刷可能だ：

#. |OptionsDlg| で |LibreOfficePrintPage| に移動。
#. :guilabel:`Con&vert colors to grayscale` を選択。
#. |OK| を押す。

.. caution::

   上の方法を採ると、Calc だけでなく LibreOffice すべてのアプリケーションで印刷
   設定が変更される。

Previewing pages/sheets before printing
----------------------------------------------------------------------

印刷前に Calc でシートをプレビューする方法：

#. 印刷プレビューモードを切り替える：

   * |MenuBar| |FilePrintPreviewM|
   * |StandardToolbar| |TogglePrintPreviewI| を押す
   * キーバインド |Ctrl+Shift| + :kbd:`O`
#. |PrintPreviewToolbar| が |FormattingToolbar| と交代する。
#. このビューから先述の方法で |PrintDlg| を開く。
#. 印刷オプションを選択し、:guilabel:`&Print` ボタンを押す。
#. |TogglePrintPreviewI| をもう一度クリックするか、|PrintPreviewToolbar| の右側
   にある :guilabel:`Close Preview` アイコンをクリックすると、通常のスプレッド
   シートビューに戻る。

Using print ranges
======================================================================

* スプレッドシート上のどのセル範囲を印刷するかを定義可能。
* 定義された印刷範囲に含まれないシート上のセルは、印刷されない。
* 印刷範囲が定義されていないシートは印刷されません。
* ユーザー定義の印刷範囲を作成すると、既存の定義済みの印刷範囲が置き換わる。

Defining and printing a print range
----------------------------------------------------------------------

印刷範囲を自分で定義してもよい：

#. 印刷範囲となる升目範囲を選択する。
#. |MenuBar| から :menuselection:`F&ormat-->Prin&t Ranges-->&Define` を選択する。
   |OptionsDlg| |CalcViewPage| の :guilabel:`&Page breaks` がオンならば自動改頁
   線が画面上に描かれる。これで印刷範囲に含まれる升目が定義される。
#. |StandardToolbar| の :guilabel:`Print Directly` を押すか、|PrintDlg| を開いて
   :guilabel:`&Print` を押して、定義した印刷範囲を印刷する。

.. tip::

   印刷範囲の確認は |TogglePrintPreviewI| または |PrintDlg| のプレビュー窓を使用
   して行うことができる。印刷範囲内の升目が描画される。
   :ref:`calc07-anchor-viewing` を見ろ。

Editing a print range
----------------------------------------------------------------------

印刷範囲をいつでも編集することが可能。例えば、升目を追加したり削除したり、反復す
る行や列を定義したりする。後者の定義方法の詳細については
:ref:`calc07-anchor-repeat` を見ろ。

#. |MenuBar| から |FormatPrintRangesEditM| を選択し |EditPrintRangesDlg| を開く。
#. 単一範囲しか定義されていない場合、:guilabel:`Print Range` 欄をクリックすると
   定義した印刷範囲が青枠で囲まれて表示される。
#. 複数のセル範囲を定義するには、各セル範囲を ``,`` で区切る。|Ctrl| を押しなが
   らセル範囲を選択すれば新しいセル範囲を追加することも可能。
#. 印刷範囲を削除するには、:guilabel:`Print Range` 欄で選択、削除する。残りの印
   刷範囲が ``,`` 一つで区切られ、連なりの最後に ``,`` がないことを確認しろ。
#. |OK| を押す。

.. _calc07-anchor-viewing:

Viewing print ranges
----------------------------------------------------------------------

* 印刷範囲定義後、改頁は自動的になされる。
* :menuselection:`&View-->&Page Break` で改頁プレビュー、
  :menuselection:`&View-->&Normal` で改頁プレビュー終わり。

印刷範囲は、既定では青枠で囲まれ、各ページの中央に薄い灰色のページ番号が示され
る。非印刷領域は灰色の背景。

.. _calc07-anchor-named:

Named print ranges
----------------------------------------------------------------------

繰り返し印刷するセル範囲を定義することも可能。スプレッドシートの異なる領域を異な
る報告書用に印刷する場合に便利だ。このような用途に名前付き印刷範囲を複数定義する
ことが可能だ。

Defining and naming
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. 対象セルを選択する。
#. |MenuBar| から :menuselection:`&Sheet-->&Named Ranges and
   Expressions-->&Define...` を実行して |DefineNameDlg| を開く。
#. :guilabel:`&Name` 欄に名前をタイプする。
#. :guilabel:`Range or formula &expression` のセル範囲を調整してもよい。
#. :guilabel:`&Scope` ドロップダウンリストは `Document (Global)` のままにする。
#. 下部に畳まれている :guilabel:`&Print range` をオンにする。
#. :guilabel:`&Add` を押して確定。

Printing a named range
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

印刷する名前付き範囲を選択する手順：

#. |MenuBar| から |FormatPrintRangesEditM| を実行。
#. |EditPrintRangesDlg| で :guilabel:`Print Range` ドロップダウンリストから使い
   たい名前付き範囲を選択する。
#. |OK| を押す。

ワークシートを改頁プレビューモードにしていれば、この時点で上記手順結果が確認でき
る。

.. _calc07-anchor-delete:

Deleting a named print range
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

指定した印刷範囲が不要になった場合に削除する手順：

#. |MenuBar| から :menuselection:`&Sheet-->&Named Ranges and
   Expressions-->&Manage...` (|Ctrl| + |F3|) 実行
#. |ManageNamesDlg| で対象名前付き範囲を選択
#. :guilabel:`&Delete` ボタンを押す

Removing print ranges
----------------------------------------------------------------------

例えば、シート全体を後で印刷する必要がある場合や、追加した範囲の一部を印刷する必
要がなくなった場合など、定義した印刷範囲を削除する必要が生じることがある。

定義済み印刷範囲を除去する方法：

#.

Go to Format > Print Ranges > Clear on the Menu bar to remove all of the defined print ranges in the spreadsheet, except for named print ranges. After the print range is removed, the default page break lines for the selected paper size will appear on the screen (assuming that Tools > Options > LibreOffice Calc > View > Page breaks is enabled).

|MenuBar| の :menuselection:`F&ormat-->Prin&t Ranges-->&Clear` を選択すると、名
前付き印刷範囲を除き、スプレッドシートで定義されている印刷範囲がすべて削除される。
印刷範囲が削除されると、選択した用紙判型の既定の改頁線が画面に描画される。
[#calc07-footer-1]_

名前付き印刷範囲を除去する方法はこれとは異なる。:ref:`calc07-anchor-delete` の方
法を用いる。

.. _calc07-anchor-repeat:

Repeat printing of rows or columns
----------------------------------------------------------------------

スプレッドシートが複数ページに印刷される場合、特定の行または列を定義して、各印刷
ページで繰り返し印刷することが可能。

Using print ranges
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. 上述の方法で |EditPrintRangesDlg| を開く。
#. :guilabel:`Rows to Repeat` 欄には反復して印刷する行の参照を入力する。例えば、
   一、二、三行目を繰り返す場合には ``$1:$3`` と指定する。これにより、本欄は
   `- none -` から `- user defined -` に変化する。

   キャレットを :guilabel:`Rows to Repeat` 欄に置き、マウスを使って、反復印刷し
   たい各行の升目を選択することもできる。行全体を選択する必要はない。
#. :guilabel:`Columns to Repeast` 欄には反復して印刷する列の参照を入力する。例え
   ば、A 列を反復する場合には ``$A`` と指定する。残りは行のときと同様。
#. |OK| を押す。

Using named print ranges
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

行または列の反復印刷に用いる名前の反復印刷を定義することも可能だ：

#. 先述の方法で、反復印刷する行・列を名前付き定義する。
   :ref:`calc07-anchor-named` を見ろ。使用者定義の印刷範囲と同様に、反復印刷した
   い行・列から升目を一つ選択すれば十分だ。
#. |DefineNameDlg| で :guilabel:`Repeat column` や :guilabel:`Repeat row` をオン
   にする。反復印刷する列と行を定義する。
#. :guilabel:`&Add` を押す。ダイアログボックスを閉じる。
#. |MenuBar| から |FormatPrintRangesEditM| を選択し |EditPrintRangesDlg| を開く。
#. :guilabel:`Rows to Repeat`, :guilabel:`Columns to Repeat` ドロップダウンリス
   トに定義済み名前付き印刷範囲を指定する。
#. |OK| を押す。

Page breaks
======================================================================

印刷範囲の定義は強力だが、スプレッドシートが思い通りに印刷されるように改頁を手動
で調整する場合もある。二種類の改頁を入れられる：

行改頁
   選択セルの行の上に改頁を水平方向に入れる。例えば、選択セルが H15 の場合、14
   行目と 15 行目の間に改行が入る。
段改頁
   選択セルのある列の左側に垂直方向改頁を入れる。例えば、選択セルが H15 の場合、
   G 列と H 列の間に改段が作成される。

手動改行が挿入されると、画面上では行または列の間に青い線または太い線として表示さ
れる。実際の見てくれは設定によって異なる。画面上で手動改行を見やすくするには、そ
れをを変更する。|OptionsDlg| |ApplicationColors| で :guilabel:`Spreadsheet` 区画
までスクロールすると、改頁の描画方法を変更可能だ。

.. admonition:: 読者ノート

   手動でも自動でもない、素の改頁色の意味は？

Inserting page breaks
----------------------------------------------------------------------

.. |RowBreakC| replace:: :menuselection:`&Row Break`
.. |ColBreakC| replace:: :menuselection:`&Column Break`

#. 手動改ページを入れたい升目を選択する。
#. |MenuBar| の :menuselection:`&Sheet-->Insert Page &Break-->` を選択する。
#. 升の上に改行を入れるには |RowBreakC| を、升の左に改段を入れるには |ColBreakC|
   をそれぞれ選択する。

あるいは、

#. :menuselection:`&View-->&Page Break` を選択
#. 手動改頁を挿入したい升目を選択
#. 右クリックメニュー |RowBreakC| または |ColBreakC| を選択

|MenuBar| の :menuselection:`&View-->&Normal` を選択してスプレッドシートの標準
ビューに戻る。

.. admonition:: 読者ノート

   標準ビューに戻らず、改頁線が描画され続けていたほうが編集に適している。

Deleting page breaks
----------------------------------------------------------------------

#. 手動改頁を削除したいところにあるセルを選択。
#. :menuselection:`&Sheet-->Delete Page &Break-->` のサブコマンドを列または行
   に応じて実行。

.. note::

   適切な升目が選択されていない場合、|RowBreakC| または |ColBreakC| 項目は灰色で
   表示される。

Deleting multiple page breaks
----------------------------------------------------------------------

手動の行改頁や段改頁が同じスプレッドシートに複数存在する可能性がある。シートから
すべての改頁を削除したい場合は、次のようにする：

手動改頁を一括削除する方法がある。それは右クリックメニューから
:menuselection:`Delete Page &Breaks` を実行することだ。

#. |MenuBar| の :menuselection:`&View-->&Page Break` を選択
#. スプレッドシート内で右クリックし、コンテキストメニューから
   :menuselection:`Delete Page &Breaks` を選択する。シートから手動改頁すべてが削
   除される。
#. 改頁描画をやめたければ |MenuBar| の :menuselection:`&View-->&Normal View` を
   選択

Printing options for page styles
======================================================================

スプレッドシートにページスタイル (|Calc05|) を使用する場合、ページスタイル内に印
刷オプションを含めることが可能だ。たとえば、ページの順序、詳細、印刷する尺度など
だ。ページスタイルを使用すると、シート内のさまざまなシートの印刷オプションをす
ばやく設定して変更できる。

印刷オプションを設定する前に正しいシートを選択していることを確認しろ。
|PageStyleDlg| を開く。その方法は複数ある：

* |MenuBar| から :menuselection:`F&ormat-->&Page Style...` コマンドを実行
* |Sidebar| :guilabel:`Styles` 内で

  #. :guilabel:`Page Styles` ボタンを押して
  #. `Default` 項目右クリックメニューから :guilabel:`&Edit Style...` コマンドを
     実行
* |StatusBar| `Default` をダブルクリック

:guilabel:`Sheet` タブをクリックしろ。ここでページスタイルに関する印刷設定を行
う。ダイアログボックスの表題がこれから変更しようとしているページスタイルの名前を
示す。

.. rubric:: Page Order

シート内のデータが印刷ページに収まらない場合に、番号を付けて印刷する順序を
定義する。

:guilabel:`&Top to bottom, then right`
   シートの左列から下へ縦に印刷する。
:guilabel:`&Left to right, then down`
   シートの最上行から右段に向かって横に印刷する。
:guilabel:`First &page number`
   最初のページを 1 以外の番号で開始したい場合は、この選択肢をオンにする。最初の
   ページの番号をスピンボックスに入力しろ。

.. rubric:: Print

スプレッドシートのどの要素を印刷するかを定義する。

:guilabel:`&Column and row headers`
   列と行のヘッダーを印刷する。
:guilabel:`&Grid`
   格子として升目の境界線を印刷する。画面に描画するには |OptionsDlg|
   |CalcViewPage| :guilabel:`&Grid lines` で選択する。
:guilabel:`&Comments`
   スプレッドシートで定義された説明を印刷する。説明は対応セル参照とともに別ペー
   ジに印刷される。
:guilabel:`&Objects/Images`
   物（印刷可能な）と画像のすべてを印刷スプレッドシートに含む。
:guilabel:`Ch&arts`
   スプレッドシートに入っている統計図表を印刷する。
:guilabel:`&Drawing objects`
   印刷されたスプレッドシートに図面物すべてを含む。
:guilabel:`&Formulas`
   数式の結果ではなく、升目含まれている数式を印刷する。
:guilabel:`&Zero values`
   値がゼロの升目で、0 を印刷することを指定する。

.. rubric:: Scale

印刷されるスプレッドシートのページ尺を定義する。

:guilabel:`Scaling &mode`
   ドロップダウンリストから尺モードを選択する。選択した尺モードに適したコント
   ロールがドロップダウンリストボックスの下に表示される。

   `Reduce/enlarge printout`
      すべての印刷ページを拡大・縮小する倍率を指定する。10% から 400% の範囲で係
      数を百分率で入力する。100% 未満の倍率では紙面が縮小され、それ以上の倍率で
      は拡大される。
   `Shrink print range(s) to width/height`
      現在のページスタイルで各シートが印刷される、横方向と縦方向の最大ページ数を
      指定する。印刷範囲は常に比例して拡大縮小されるため、結果として指定したペー
      ジ数よりも少なくなることがある。どちらかのスピンボックスを消去すると、指定
      されていない寸法は必要なページ数だけ使う。両方を消去すると等倍になる。
   `Shrink print range(s) on number of pages`
      同じページスタイルを使用するシートそれぞれに対して印刷される最大ページ数を
      指定する。尺は定義されたページ数に合わせて必要に応じて適する値になる。

Headers and footers
======================================================================

ヘッダーとフッターとは、定義済みテキストであって、シート領域の外側、上部または下
部に印刷されるものだ。ヘッダーとフッターは同じように設定され、同じページスタイル
を使用する左右のページで異なる中身を持つことができる。

Setting headers and footers
----------------------------------------------------------------------

#. 対象シートを選択する。
#. 前述のコマンドで |PageStyleDlg| を開く。
#. |HeaderTab| または |FooterTab| をクリックする。
#. :guilabel:`Hea&der on` または :guilabel:`&Footer on` をオンにする。
#. 必要に応じて他のオプションの値を入力する。
#. |OK| を押して変更を保存し、閉じる。

他のオプション：

:guilabel:`Hea&der on` or :guilabel:`&Footer on`
   現在のページスタイルにヘッダーまたはフッターを追加する。
:guilabel:`Same co&ntent on left and right pages`
   左右のページで同じヘッダーまたはフッター中身を共有する。左ページと右ページに
   異なるヘッダーまたはフッターを割り当てるには、これをオフにし、|EditButton| を
   押す。:ref:`calc07-anchor-contents` を見ろ。
:guilabel:`Same contents on first &page`
   最初のページに、残りのページとは異なるヘッダーまたはフッターを設定する。異な
   るヘッダーまたはフッターを割り当てるには、これをオフにし、|EditButton| を押す。
   :ref:`calc07-anchor-contents` を見ろ。
:guilabel:`&Left margin`
   左ページ余白とヘッダーまたはフッターの左端の隙間の量を入力する。
:guilabel:`R&ight margin`
   右ページの余白とヘッダーまたはフッターの右端の隙間の量を入力する。
:guilabel:`&Spacing`
   ヘッダーの下端とスプレッドシートの上端、またはフッターの上端とスプレッドシー
   トの下端の間に維持する隙間の量を入力する。
:guilabel:`Heigh&t`
   ヘッダーまたはフッターの高さを入力する。
:guilabel:`&AutoFit height`
   中身合わせてヘッダーまたはフッターの高さを自動的に調整する。
:guilabel:`&More...`
   :guilabel:`Border / Background` ダイアログボックスを開き、ヘッダーやフッター
   の境界や背景色、画像の見てくれを定義する。詳細については |Calc05| を見ろ。
|EditButton|
   |HeaderDlg| または |FooterDlg| を開き、ヘッダーまたはフッターに配置するテキス
   トを追加、編集、書式設定する。詳細については :ref:`calc07-anchor-contents` を
   見ろ。

.. _calc07-anchor-contents:

Header or footer contents
----------------------------------------------------------------------

スプレッドシートのヘッダーとフッターには、テキスト用の枠が三つある。各列は空で
も、他の列と異なる内容でもかまわない。

.. |TextAttrDlg| replace:: :guilabel:`Text Attributes` ダイアログボックス

#. 対象シートを選択する。
#. 前述のコマンドで |PageStyleDlg| を開く。それから |HeaderTab| または
   |FooterTab| をクリックする。
#. |EditButton| を押して |HeaderDlg| または |FooterDlg| を開く。|PageStyleDlg|
   で同じ内容系オプションがオフである場合、|HeaderDlg| または |FooterDlg| にはタ
   ブページが表示され、最初のページと左右のページのヘッダーまたはフッターの内容
   を設定することができる。
#. 標準的な内容をヘッダーまたはフッターに入力するには :guilabel:`&Header` または
   :guilabel:`&Footer` ドロップダウンリストから選択肢を選択する。
#. 独自の内容をヘッダーまたはフッターに入力するには、テキストエリアの一つをク
   リックして

   * テキストを入力するか、
   * :guilabel:`Custom header` または :guilabel:`Custom footer` 図像の一つをク
     リックする。

   これらのアイコンについては後述する。
#. ヘッダーまたはフッターのテキストのスタイルを変更するには、:guilabel:`Text
   Attributes` 図像をクリックして |TextAttrDlg| を開き、フォント、効果、位置を設
   定する。
#. |OK| を押してテキスト属性の変更を保存し |TextAttrDlg| を閉じる。
#. |OK| を押してヘッダーまたはフッターの内容の変更を保存し、|HeaderDlg| または
   |FooterDlg| を閉じる。
#. |OK| を押してヘッダーまたはフッターの変更を保存し、|PageStyleDlg| を閉じる。

:guilabel:`Custom header` または :guilabel:`Custom footer` で利用可能な選択肢：

Text Attributes
   新規または選択したテキストに書式を割り当てることができる |TextAttrDlg| を開
   く。|FontTab|, |FontEffectsTab|, |PositionTab| がある。
Title
   選択した領域にファイル名のプレースホルダーを入れる。クリックして開くドロップ
   ダウンメニューで、`Title`, `File Name`, `Path/File Name` のいずれかを選択す
   る。スプレッドシートに表題が割り当てられていない場合は、ファイル名が代わりに
   入る。
Sheet Name
   スプレッドシートで選択されたシートの名前のプレースホルダーを選択領域に入れる。
Page
   ページ番号のプレースホルダーを選択領域に入れる。これによりスプレッドシートに
   連続したページ番号を付けることができる。
Pages
   スプレッドシートの総ページ数を表すプレースホルダーを選択領域に入れる。
Date
   現在の日付のプレースホルダーを選択領域に入れる。このプレ ースホルダーはスプ
   レッドシートの各ページのヘッダー/フッターに繰り返し表示される。
Time
   現在の時刻のプレースホルダーを選択領域に入れる。このプレースホルダーはスプ
   レッドシートの各ページのヘッダー/フッターに繰り返し表示される。

Exporting to PDF
======================================================================

文書を |PDF| にエクスポート可能だ。この業界標準のファイル形式は、ファイルを誰か
に送信したり、Adobe Acrobat Reader やその他の |PDF| viewer を使用して表示したり
するのに最適だ。

.. caution::

   既定では、|PDF| 文書は内容の改竄や編集から保護されていない。|PDF| 文書の内容
   は LibreOffice Draw などの専用ソフトウェアで編集可能だ。

.. tip::

   Save As とは異なり、Export は現在の文書のコピーを選択した書式で新規ファイルに
   書き出すものだが、現在の文書と書式は開いたままだ。

Quick export to PDF
----------------------------------------------------------------------

直近に適用した |PDF| 設定に基づいてスプレッドシート全体を |PDF| に保存するには、
|StandardToolbar| :guilabel:`Export Directly as PDF` 図像をクリックするのがよ
い。保存先入力するよう求められるものの、ページ範囲や画像圧縮、その他のオプション
を選択する機会はない。

Controlling PDF content and quality
----------------------------------------------------------------------

|PDFOptionsDlg| で出力 |PDF| のオプションを細かく指定可能。|MenuBar| から
:menuselection:`&File-->&Export as PDF...` を選択してダイアログボックスを開く。

.. tip::

   |MenuBar| の |FileExportM| を選択し、ドロップダウンメニューから `PDF -
   Portable Document Format` を選択することでも |PDFOptionsDlg| にアクセスできる。

.. admonition:: 利用者ノート

   職務経歴書やスキルシートを |PDF| に変換して提出する前に利用したい。

General tab of PDF Options dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|GeneralTab| では |PDF| に含めるページ、画像に使用する圧縮の種類、その他オプショ
ンを選択可能だ。詳細については |Guide| または |Help| を見ろ。ほとんどの場合、既
定設定が必要なものだ。

:guilabel:`Whole Sheet Export` を選択すると、当ダイアログボックスの他の多くの設
定を無視する。

.. |SeeWriter07| replace:: :doc:`/libreoffice/writer-guide/writer07` と内容が重複するので、ノートとして先に出来たそちらを見ろ。

.. admonition:: 読者ノート

   |SeeWriter07|

Initial View tab of PDF Options dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

このタブでは |PDF| ファイルを閲覧プログラムで開くときのコマンドラインオプション
を選択可能。

User Interface tab of PDF Options dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: 読者ノート

   |SeeWriter07| :guilabel:`Transitions` は Writer でも Calc でも使用不能。

.. note::

   アウトラインは通常、Calc では使用されない。

Links tab of PDF Options dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: 読者ノート

   |SeeWriter07|

Security tab of PDF Options dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: 読者ノート

   |SeeWriter07|

Digital Signatures tab of PDF Options dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: 読者ノート

   |SeeWriter07|

Exporting to other formats
======================================================================

Calc では次の二つのコマンドの意味を区別している：

* |SaveAsM|: 別のスプレッドシートファイル形式で保存する場合
* |FileExportM|: Web ページを作成する場合

Emailing spreadsheets
======================================================================

スプレッドシートを電子メールの添付ファイルとして送信する方法：

#. :menuselection:`&File-->Sen&d-->` 各種コマンドを実行：

   * :menuselection:`&Email Document...`: 現在の形式
   * :menuselection:`Email as &OpenDocument Spreadsheet...`: 拡張子 .ods 形式
   * :menuselection:`Email as &Microsoft Excel...`: 拡張子 .xlsx 形式
   * :menuselection:`Email as P&DF...`
#. シートを当該項目形式に変換保存されたファイルが添付された状態のメール草稿編集
   中のメールクライアント画面が開く。それを用いて送信する。

Digital signing of documents
======================================================================

.. admonition:: 読者ノート

   |SeeWriter07|

Applying a digital signature
----------------------------------------------------------------------

.. admonition:: 読者ノート

   |SeeWriter07|

Signing multiple times with the same signature
----------------------------------------------------------------------

LibreOffice では署名の記述ができるようになったため、同じ作成者による複数の署名が
許可される。

:menuselection:`&File-->Di&gital Signatures-->Digital Signat&ures...` を選択する
と、ダイアログに既存の署名とその説明（もしあれば）が一覧表示される。

:guilabel:`&Sign Document...` ボタンを押すと、:guilabel:`Select Certificate` ダ
イアログボックスでオプションの説明も求められる。

既存の記述の値を変更すると、その署名は無効になる。

Digitally signing macros
----------------------------------------------------------------------

通常、マクロは文書の一部だ。文書に署名すると、文書内のマクロも自動的に署名される。
文書ではなく、そのようなマクロに対して署名をしたい場合には |MenuBar| から
:menuselection:`&Tools-->&Macros-->Digital &Signature...` を選択し、上述のように
署名を適用する。

Removing personal data
======================================================================

.. admonition:: 読者ノート

   |SeeWriter07|

----

.. rubric:: 章末注

.. [#calc07-footer-1] |OptionsDlg| |CalcViewPage| :guilabel:`&Page breaks` がオ
   ンである場合。
