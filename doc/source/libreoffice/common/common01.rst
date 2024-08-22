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
バー、|MenuBar|、|StandardToolbar| があり、ウィンドウの下部に |StatusBar| がある。

特殊な UI も搭載されている。それについては :doc:`common13` 参照。

Title bar
----------------------------------------------------------------------

Title バーに基本的には現在の文書のファイル名が示される。文書が新規作成されると、
文書名は :guilabel:`Untitled X` のようなものになる。ここで X は数字。新規文書に
は作成順に番号が付けられる。

Menu bar
----------------------------------------------------------------------

Writer を例に挙げて |MenuBar| にあるメニューを解説している。省略。

Toolbars
----------------------------------------------------------------------

LibreOffice のツールバーはそれが見えている場合、docked か floating のどちらかの
状態をとる。

既定では、|StandardToolbar| はどのアプリケーションでもウィンドウ上部に docked で
あり、二番目のツールバーが何であるかはアプリケーションによって異なる。

特に重要なのは、二番目のツールバーは状況依存型であることだ。通常は何が選択されて
いるかによってツールセットが変化する。そのため、例えば Writer で描画物が選択され
ている場合、描画物の書式設定ツールセットである |DrawingObjPropToolbar| が
|FormattingToolbar| に取って代わる。描画物の選択を解除すると
|DrawingObjPropToolbar| が閉じ、|FormattingToolbar| が再び開く。

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
ツールのポップアップの集まりだ。ツールパレットは、次の例を使用して floating ツー
ルバーにすることが可能だ。

#. |DrawingToolbar| の :guilabel:`Basic Shapes` をクリックしてツールパレットを開
   く。
#. ツールバーハンドル（……に見える部分）をクリックし、ツールパレットを開いている
   文書上めがけてドラッグする。
#. ツールバーハンドルを離すと、ツールパレットは floating ツールバーになる。

.. note::

   ツールバーハンドルが表示されていない場合、ツールパレットまたはツールバーは
   docked 位置に固定されているため、それを解除する必要がある。この次の節を参照。

Locking and unlocking toolbars
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ツールバー全部を完全固定する手段が用意されている。|MenuBar| から
:menuselection:`&View-->&Toolbars-->&Lock Toolbars` を選択するのだ。ただし
LibreOffice を再起動する必要がある。このコマンドメニュー項目にチェック印が付いて
いれば、ツールバーロックが機能していることを示す。

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

* 表組にキャレットが置かれると :guilabel:`Table` ツールバーが開く
* 順序付き一覧または順序なし一覧にキャレットが置かれると :guilabel:`Bullets and
  Numbering` ツールバーが開く
* 画像が選択されると |ImageToolbar| が開く

Customizing toolbars
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ツールバーを floating にするとタイトルバーに ▼ がある。このドロップダウンメ
ニューにある :menuselection:`Visible &Buttons-->` 以下の項目チェックをオンオフす
ることでコマンドセットをカスタマイズすることが可能だ。

* 項目 :menuselection:`&Customize Toolbar...` を選択すると |CustomizeDlg| が開く。
  ここでさらにツールを追加する。詳しくは :doc:`common13` 参照。
* 選択した floating ツールバーを既定位置に dock するには項目
  :menuselection:`&Dock Toolbar` を選択する。タイトルバーダブルクリックのほうが
  早い。
* すべての floating ツールバーを既定位置に dock するには項目
  :menuselection:`Dock &All Toolbars` を選択する。
* 等々

Context menus
----------------------------------------------------------------------

段落や画像などの対象物を右クリックすることでポップアップメニューが開く。利用でき
る機能や選択肢は対象物が何であるかにより異なる。これが便利であるのは、特にメ
ニューやツールバー内の所望のコマンド位置が不明な場合だ。

Status bar
----------------------------------------------------------------------

|StatusBar| は文書に関する情報を提示するほか、いくつかの機能をすばやく変更する便
利な方法も含まれている。アプリケーション固有項目がある。

万が一 |StatusBar| が見えないという場合は |MenuBar|
:menuselection:`&View-->Status &Bar` のチェック状態を確認しろ。

本書では Impress における |StatusBar| の構成を例に挙げて、文書の関連情報がどう示
されているのかを述べている。割愛。

Sidebar
----------------------------------------------------------------------

既定では |Sidebar| はどのアプリケーションでもワークスペースの右側に現れる。

|Sidebar| の表示切替は |MenuBar| :menuselection:`&View-->Sidebar` のチェックを切
り替えるか、キーバインド |Ctrl+F5| で行う。

|Sidebar| は甲板が複数あり、甲板それぞれにはには文書を書式設定するための道具や選
択肢が含まれている。UI 構成は文書の種類とアプリケーションによる。甲板は盤で構成
され、|Sidebar| 右側にあるアイコンバーで甲板を切り替える。

すべての LibreOffice アプリケーションに現れる甲板もある：

* |PropertiesDeck|
* |StylesDeck|
* |GalleryDeck|
* |NavigatorDeck|

|Sidebar| 表示切替には左側にある縦に細長いボタンをクリックする。

|Sidebar| を undock して floating 状態にするには次の方法がある：

* |Sidebar| 右上のハンバーガーをクリックして :menuselection:`Undock` を選択する。
* キーバインド |Ctrl+Shift| + |F10| を押す。

反対に、|Sidebar| をメインウィンドウの通常配置に dock するには次の方法がある：

* |Sidebar| 右上のハンバーガーをクリックして :menuselection:`Dock` を選択する。
* キーバインド |Ctrl+Shift| + |F10| を押す。

Working with documents
======================================================================

New documents
----------------------------------------------------------------------

LibreOffice アプリケーションは新規文書を作成する方法が複数ある。

* Start Center を開いてアプリケーション名をクリックする
* Start Center にある :guilabel:`Templates` をクリックする
* |MenuBar| :menuselection:`&File-->&New-->` から文書形式を選択する
* |StandardToolbar| にある :guilabel:`New` ボタン脇の ▼ をクリックして以下同様
* キーバインド |Ctrl+N| を押す
* |MenuBar| :menuselection:`&File-->&Wizards-->` サブメニューから以下同様

Opening existing documents
----------------------------------------------------------------------

既存の LibreOffice 文書を適切なアプリケーションで開く方法も複数ある：

* Start Center で :guilabel:`Open File` をクリック
* |MenuBar| から :menuselection:`&File-->&Open...` を選択
* |StandardToolbar| から :guilabel:`Open` を押す
* キーバインド |Ctrl+O| を押す

以上の方法ではファイルダイアログボックスが開く。そこで開くファイルを指定する。

* Start Center で :guilabel:`Recent Documents` をクリック
* |MenuBar| から :menuselection:`&File-->Recent Doc&uments-->` サブメニューを出す

以上の方法ではファイル一覧が示される。そこで開くファイルを指定する。

.. note::

   直近ファイル一覧は LibreOffice が独自に覚えているファイルなので、ファイルシス
   テムにはすでに存在しない場合がある。その場合にはサムネイル上の操作により一覧
   から排除するといい。なお、右上のハンバーガーメニューに一括排除コマンドがあ
   る。

Saving documents
----------------------------------------------------------------------

LibreOffice は文書を保存する方式が複数ある。

Save
   現在のファイルパスを保持したまま、すべての変更を保存する。

   * |MenuBar| :menuselection:`&File-->&Save...` を実行
   * キーバインド |Ctrl+S| を押す
   * |StandardToolbar| :guilabel:`Save` 図像を押す
Save As
   文書を新規作成したり、ファイルパスやファイル形式を変更したり、計算機システム
   上の別の場所にファイルを保存したりする。

   * |MenuBar| |SaveAsM| を実行
   * キーバインド |Ctrl+Shift| + :kbd:`S` を押す
   * |StandardToolbar| :guilabel:`Save` 図像脇 ▼ をクリックしてドロップダウンメ
     ニューから :menuselection:`Save &As...` を実行
Save a Copy
   現在の文書のコピーを、計算機システムの別の場所に保存する。現在の文書は編集す
   るために開いたままだ。

   * |MenuBar| :menuselection:`&File-->&Save a cop&y...` を実行
   * |StandardToolbar| :guilabel:`Save` 図像脇 ▼ をクリックしてドロップダウンメ
     ニューから :menuselection:`&Save a cop&y...` を実行
Save All
   LibreOffice で開いているすべてのファイルを保存する。|MenuBar|
   :menuselection:`&File-->Sa&ve All` を実行する。

Saving documents automatically
----------------------------------------------------------------------

LibreOffice でファイルを自動的に保存する必要がある場合は、AutoRecovery 機能を使
用する。ファイルが自動的に保存されると、LibreOffice は最後に保存された状態のファ
イルを上書きする。ファイルの自動保存には次の設定が要る：

#. |OptionsDlg| を開く
#. |LoadSaveGeneralPage| を開く
#. :guilabel:`Save` 区画にある関連項目を指定する
#. |OK| を押してダイアログボックスを閉じる

.. admonition:: 利用者ノート

   この機能はオフにしておく。

Using the Navigator
----------------------------------------------------------------------

Navigator は文書にある要素を木構造で表現するビューだと考えられる。これは専用ダイ
アログボックスまたは |Sidebar| の一甲板として利用可能だ。

* ダイアログボックス版は |F5| キーを押して表示切替
* |Sidebar| 版はいったん全体を |Ctrl| + |F5| キーを押すなどして表示状態にしてから
  対応図像をクリックするか、キーバインド |Alt| + :kbd:`4` を押す

Navigator の利便性を損なわぬように、物を簡単に見つけることができるように、物には
識別しやすい名前を付けろ。対象物を右クリックし、コンテキストメニューから
:menuselection:`&Rename...` を実行すればいい。

Displaying multiple view of a document
----------------------------------------------------------------------

LibreOffice は同じ文書に対してビューを複数開くことが可能だ。使わないので省略。

Undoing and redoing changes
----------------------------------------------------------------------

Undoing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

いちばん普通の発動手順はキーバインド |Ctrl+Z| だ。

Web ブラウザーの閲覧履歴のように、特定の状態に戻す方法もある。|StandardToolbar|
の :guilabel:`Undo` 図像脇 ▼ ドロップダウンメニューから特定の時点を選択する。

Redoing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

いちばん普通の発動手順はキーバインド |Ctrl+Y| だ。これも Undo コマンド同様に特定
の時点まで文書の状態を復元できる。

Repeating undo and redo commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

文書に対して最後に行った Undo または Redo 可能なコマンドを反復して実行する方法が
ある：

* キーバインド |Ctrl+Shift| + :kbd:`Y`
* |MenuBar| :menuselection:`&Edit-->&Repeat`

.. admonition:: 利用者ノート

   これは意外に便利な可能性がある。

Reloading documents
----------------------------------------------------------------------

|MenuBar| :menuselection:`&File-->Re&load` は GIMP でいうところの
:menuselection:`&File-->Re&vert` に相当する。まず使わない。

Closing documents
----------------------------------------------------------------------

|MenuBar| :menuselection:`&File-->&Close` コマンドを実行すると、開いている文書が
閉じられる。その際、文書が一つしかなかった場合には LibreOffice Start Center が開
く。

.. admonition:: 利用者ノート

   アプリケーション本体を終了するコマンドと文書を閉じるコマンドは、関係はあるが
   別物であると考えたい。

Printing
======================================================================

Default printer
----------------------------------------------------------------------

|StandardToolbar| :guilabel:`Print Directly` 図像にマウスをホバーさせると、
ツールチップテキストで既定印刷機を確認可能。

Quick printing
----------------------------------------------------------------------

上述のコマンドで開いている文書全体を既定印刷機を使って印刷する「クイック印刷」が
可能だ。これは |StandardToolbar| にあるこの図像からでしか実行できないようなので、
これだけはツールバーから隠さないようにしておくのがいい。

Printer setup
----------------------------------------------------------------------

.. note::

   |PrinterSetupDlg| に :guilabel:`Options` のある LibreOffice アプリケーション
   は Writer か Calc しかない。

LibreOffice に対して印刷機を設定する手順は次のようなものだ。印刷機を実際に備えな
いといけない。Microsoft Print to PDF でもいいが。

#. 印刷機と計算機を接続する。
#. |MenuBar| :menuselection:`&File-->P&rinter Settings...` で |PrinterSetupDlg|
   を開く。
#. :guilabel:`Option&s...` ボタンを押して |PrinterOptionsDlg| を開く。
#. 必要な選択肢を選択し、|OK| を押して |PrinterOptionsDlg| を閉じる。
#. 必要に応じて |PrinterSetupDlg| :guilabel:`&Properties...` を押して OS 搭載の
   既定印刷機プロパティーシートを開く。
#. 必要な性質を選択し、|OK| を押してプロパティーシートを閉じる。
#. |OK| を押して |PrinterSetupDlg| を閉じる。

LibreOffice printing options
----------------------------------------------------------------------

General printing options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

計算機に印刷機をインストールした後ならば、LibreOffice の一般的な印刷オプションを
カスタマイズ可能だ。|OptionsDlg| |LibreOfficePrintPage| を開く。LibreOffice の一
般的な印刷オプションのうち、私が触りそうなものを挙げておく。

* :guilabel:`Con&vert colors to grayscale` チェックボックス
* :guilabel:`Warnings` 区画のチェックボックス全部

  * :guilabel:`P&aper size`
  * :guilabel:`Pap&er orientation`
  * :guilabel:`&Transparency`

.. note::

   LibreOffice から印刷機への送信データ量を削減すると印刷ファイルが小さくなり、
   印刷速度が向上する。ただし、印刷品質とのトレードオフとなる。

LibreOffice modules printing options
----------------------------------------------------------------------

LibreOffice アプリケーション別印刷設定の出し方は：

#. |OptionsDlg| を開く
#. アプリケーションの名前 (e.g. LibreOffice Calc) ノードから
   :menuselection:`Print` を選択する

次の選択肢がアプリケーションによってあったりなかったりする：

* 印刷するページ、シート、スライドを（個別に）選択する
* 複数のページ、シート、スライドを一ページに印刷する
* パンフレットとして印刷する
* 封筒として印刷する
* ラベルや名刺として印刷する
* 印刷前にプレビューする

Controlling printing
----------------------------------------------------------------------

印刷直前に |PrintDlg| で印刷をさらに制御することが可能だ。

General printing options — Windows or Linux
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Impress の |PrintDlg| |GeneralTab| の例が述べられている。Writer や Calc でも似た
構成になると考えられる。

General printing options — macOS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

割愛。

LibreOffice module printing options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

割愛。アプリケーション個別の説明書にある印刷の章を参照。

Brochure printing
----------------------------------------------------------------------

Writer, Impress, Draw では、文書を正しい順序で印刷し、冊子に仕上げることが可能
だ。ページ数のかさむ職務経歴書をまとめるのに使えるか？

Single sided printing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

片面印刷しかできない印刷機で小冊子を作成する方法の例。

#. |PrintDlg| を開く。
#. |GeneralTab| では必要に応じて印刷機を選択する。
#. :guilabel:`Pr&operties...` ボタンを押して印刷機のプロパティーシートを開き、紙
   面に対するページ設定で指定したのと同じ向きに印刷機が設定されていることを確認
   する。冊子印刷の場合はここが急所だ。
#. |OK| を押して |PrintDlg| に戻る。
#. |R&C| で :guilabel:`All Slides` を選択する。冊子を作成するには最低四頁が必
   要。
#. |R&C| で必要な部数に合わせて :guilabel:`&Number of copies required` を指定。
#. :guilabel:`Label` で :guilabel:`Broch&ure` を選択。
#. |R&C| :guilabel:`Inclu&de` ドロップダウンリストで :guilabel:`Even slides` を
   選択。
#. |OK| を押して文書の偶数頁を印刷する。
#. 印刷したページを印刷機から取り出し、正しい向きで印刷機給紙場所に戻して、用紙
   の反対側に印刷する用意をする（正しい配置を見つけるのに試行錯誤が必要な場合が
   ある）。
#. |R&C| :guilabel:`Inclu&de` ドロップダウンリストで :guilabel:`Odd slides` を選
   択。
#. |R&C| で :guilabel:`&Number of copies required` を偶数頁のときと同じ値に指定。
#. |OK| を押して文書の奇数頁を印刷する。ダイアログボックスを閉じてよい。
#. 冊子を綴じる。

Double sided or duplex printing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

両面印刷が可能な印刷機で冊子を印刷すれば製本がさらに容易になる。片面手順のときと
の違いは：

* |R&C| で :guilabel:`Print on both sides (duplex long edge)` または
  :guilabel:`Print on both sides (duplex short edge)` を選択。通常、縦印刷には長
  辺綴じ、横印刷には短辺綴じを使用する。
* |R&C| で :guilabel:`C&ollate` をオンにする。この選択肢は同じ文書を複数部印刷す
  る場合に限り有効だ。

Print previewing
----------------------------------------------------------------------

Writer および Calc では、印刷前にプレビュー可能。この機能は特に文書を両面印刷す
る場合に便利で、文書を印刷する前に間違いがないことを確認する。

#. |PrintPreviewToolbar| を次のように開く：

   * |MenuBar| |FilePrintPreviewM| を選択
   * |StandardToolbar| |TogglePrintPreviewI| をクリック
   * キーバインド |Ctrl+Shift| + :kbd:`O` を押す
#. ツールバーの左側にある図像から必要なプレビューを選択する
#. 印刷プレビューから文書を印刷するには、|PrintPreviewToolbar| :guilabel:`Print`
   図像をクリックして |PrintDlg| を開く。
#. プレビューを閉じるには、|PrintPreviewToolbar| :guilabel:`Close Preview` をク
   リックする。文書が通常の表示に戻る。

----

.. rubric:: 章末注
