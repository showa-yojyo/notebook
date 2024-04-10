======================================================================
Writer Guide Chapter 21, User Interface Variants ノート
======================================================================

.. include:: ./abbrev.txt

.. contents:: 章見出し
   :depth: 3
   :local:

Introduction
======================================================================

既定では、LibreOffice Writer のコマンドはカスケードメニューと図像で満載のツール
バーに集積している。これらのメニューとツールバーについては関連するタスクと機能に
ついて説明する章それぞれで述べた。

さらに、コマンドや中身のコンテキストグループを表示する、その他の |UI| の変種を搭
載している。この章ではこれらの |UI| の変種について説明し、各変種を使用する際の
ツールや機能の場所についての簡易説明書を与える。

Selecting the user interface
======================================================================

Writer の構成時にこれらの |UI| のいずれかを選択し、いつでも標準インターフェイス
と切り替えることができる。

.. |PreferredUIDlg| replace:: :guilabel:`Select Your Preferred User Interface` ダイアログボックス

#. :menuselection:`&View-->User &Interface...` を選択する。
#. |PreferredUIDlg| で左の変種から一つを選ぶ。
#. LibreOffice プログラムすべてか、Writer にのみ選択を適用するため、関連するボタ
   ンを押す。
#. |Close| を押してダイアログボックスを閉じる。

実験的な機能を有効にしている [#writer21-footnote-advanced]_ 場合、左側にさらに選
択肢が表示されることがある。

Standard interfaces
======================================================================

|PreferredUIDlg| の選択肢のうち三つについては |Chapter01| で説明済みだ：

Standard Toolbar
   |StandardToolbar| と |FormattingToolbar| の二つのツールバーが表示される基本
   モード。Sidebar にはタブしか表示されない。
Single Toolbar
   よく使う機能を備えたツールバー一つしかない。Sidebar には :guilabel:`Hide` ボ
   タンしか表示されない。
Sidebar
   Sidebar が完全に開き、ツールバーは |FormattingToolbar| 一つしか表示されない。

各標準 |UI| の要素は、メニューの :menuselection:`&View-->` から変更できる。

Tabbed interface
======================================================================

Tabbed インターフェイスは Microsoft Office のような専売特許の事務ソフトウェアか
ら来た利用者は馴染みのあるもの。これには

* メニューバー
* 図像バー
* タブバー
* アクティブなタブの図像
* 一つ以上のタブ固有のメニュー
* クイックメニュー

が搭載されている。図像バーの :guilabel:`Menubar` 図像をクリックすると、メニュー
バーの表示有無が切り替わる。

Writer ではこの |UI| には常に表示される九つの固定タブと、時々表示される五つの追
加タブがある。

* 時々というのは、キャレットの位置や選択した項目によって変化することだ。
* 各タブの右端には固有のドロップダウンメニューがある。
* クイックメニュー（ハンバーガー）はすべてのタブで共通。

|CustomizeDlg| のタブ :guilabel:`Notebookbar` を用いて Tabbed インターフェイスを
カスタマイズし、さまざまなタブの図像それぞれの表示有無を切り替えることが可能
だ。|Chapter20| を参照しろ。

タブの図像が Writer ウィンドウの幅に収まらない場合は、行の右端に :guilabel:`»`
が表示される。これを押せば現在表示されていない追加オプションが現れる。

Icon bar
----------------------------------------------------------------------

図像バーはタブの左に位置する。見ればわかるが図像集合の編成は左から：

.. list-table:: title
   :align: left
   :header-rows: 0
   :stub-columns: 0
   :widths: auto

   * - Menu bar
     - メニューバー表示有無切り替え
   * - :guilabel:`Open (Ctrl+O)`
     - |OpenFileDlg| を開き、ファイルを選択する。
   * - :guilabel:`Save (Ctrl+S)`
     - このファイルを保存する。
   * - :guilabel:`Undo (Ctrl+Z)`
     - 最後に実行した操作を元に戻す。
   * - :guilabel:`Redo (Ctrl+Y)`
     - 最後に取り消した操作をやり直す。
   * - :guilabel:`Print (Ctrl+P)`
     - |PrintDlg| を開く。

Quick menu
----------------------------------------------------------------------

タブの右側にはクイックメニュー（ハンバーガー）があり、よく使われるコマンドやリン
クが記載されている。

Fixed tabs
----------------------------------------------------------------------

.. |FileTUTab| replace:: :guilabel:`&File`
.. |HomeTUTab| replace:: :guilabel:`&Home`
.. |InsertTUTab| replace:: :guilabel:`&Insert`
.. |LayoutTUTab| replace:: :guilabel:`&Layout`
.. |ReferencesTUTab| replace:: :guilabel:`Reference&s`
.. |ReviewTUTab| replace:: :guilabel:`&Review`
.. |ViewTUTab| replace:: :guilabel:`&View`
.. |ExtensionTUTab| replace:: :guilabel:`E&xtension`
.. |ToolsTUTab| replace:: :guilabel:`&Tools`

固定タブは次の九つだ：

* |FileTUTab|
* |HomeTUTab|
* |InsertTUTab|
* |LayoutTUTab|
* |ReferencesTUTab|
* |ReviewTUTab|
* |ViewTUTab|
* |ExtensionTUTab|
* |ToolsTUTab|

以降、各タブについて説明する。

File tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|FileTUTab| には、新規文書の作成、文書の開く、保存、印刷、閉じる、雛形の管理、
|PDF| や |EPUB| ファイルへの書き出し、文書性質表示、電子署名追加、既存 |PDF|
ファイルへの署名などのコマンドがある。

|FileTUTab| には |File-->| と |Help-->| メニューがある。

* |File-->| にはタブ上の図像と同じコマンドが含まれている。
* |Help-->| メニューにはさまざまな資料へのリンクが用意されている。

Home tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|HomeTUTab| タブには、テキストの切り取り、コピー、貼り付け、書式整形、一般的な項目
の挿入（画像、表組、特殊文字、改頁）、スタイルの適用、更新、編集などのコマンドが
ある。

:menuselection:`&Home-->` メニューにはタブにないコマンドがある。

Insert tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|InsertTUTab| には、よく使われる多くの項目をはめ込むためのコマンドを搭載している。

|Insert-->| にも同じコマンドがいくつかある。

Layout tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|LayoutTUTab| はページレイアウトに関するコマンドを搭載している。

:menuselection:`&Layout-->` メニューにも同じ項目のコマンドが少しはある。

References tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|ReferencesTUTab| は目次、索引、脚注・巻末注、相互参照、書誌、フィールドを操作す
るためのコマンドを搭載している。

:menuselection:`Referenece&s-->` メニューにも同じコマンドが多数用意されている。

Review tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|ReviewTUTab| は編集を支援する。記録、表示有無切り替え、変更点の管理に素早くアク
セスできる。

:menuselection:`&Review` メニューは同じコマンドが多くある。

View tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|ViewTUTab| は文書の画面表示に関するコマンドを搭載する。

|View-->| にも同じコマンドが多数用意されている。

Extension tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|ExtensionTUTab| には |ExtensionsDlg| にアクセスするためのメニューしかない。

.. admonition:: 利用者ノート

   インストールしている拡張次第では、タブの中身にコマンドが並ぶ。

Tools tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|ToolsTUTab| にはマクロ、差し込み印刷、フォーム作成のためのいくつかのツールが用意
されている。

|Tools-->| にも同じコマンドがいくつかある。

Additional tabs
----------------------------------------------------------------------

追加タブは、アイテムが選択されると表示され、|ViewTUTab| と |ExtensionTUTab| の間
に表示される。Writer の追加タブは：

.. |DrawTUTab| replace:: :guilabel:`&Draw` タブ
.. |ImageTUTab| replace:: :guilabel:`Ima&ge` タブ
.. |MediaTUTab| replace:: :guilabel:`&Media` タブ
.. |ObjectTUTab| replace:: :guilabel:`&Object` タブ
.. |TableTUTab| replace:: :guilabel:`&Table` タブ

* |DrawTUTab|
* |ImageTUTab|
* |MediaTUTab|
* |ObjectTUTab|
* |TableTUTab|

Draw tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|DrawTUTab| は図面物が選択されているときに表示される。このタブには、図面物に説明を
付けたり修正したりするためのコマンドや、Fontwork 物をはめ込んだり修正したりする
ためのコマンドが用意されている。

:menuselection:`&Draw-->` メニューは図面物によって異なるコマンドの部分集合を備え
る。

Image tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|ImageTUTab| には、説明、トリミング、境界線と領域のスタイルと色、錨、折り返し、位
置決め、絞り込みなど、画像を扱うためのコマンドが用意されている。

:menuselection:`Ima&ge-->` メニューには画像を扱うためのダイアログボックスへのリン
クがある。

Media tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|MediaTUTab| には音声または映像ファイルを配置し、実行するためのコマンドがある。

:menuselection:`&Media-->` メニューにも同じコマンドがある。

Object tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|ObjectTUTab| には、選択した物の位置、寸法変更、リンク、色、境界線の選択などのコマ
ンドがある。

:menuselection:`&Object-->` メニューにも同じコマンドがいくつかある。

Table tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|TableTUTab| はキャレットが表組内にあるときに開かれる。

:menuselection:`&Table-->` メニューにはタブに表示されていないコマンドもある。

Tabbed Compact interface
======================================================================

Tabbed Compact インターフェイスには Tabbed インターフェイスと同じタブがあるが、
各タブのコマンドは図像一列で配列され、その多くはドロップダウンメニューで選択可能
であるようになっている。

Groupedbar Compact interface
======================================================================

Groupedbar Compact インターフェイスは図像とメニューの集合として組織されたコマン
ドを含むグループに分割されている。

Groupedbar メニューは |UI| を変更する便利な方法を含む、コマンドの部分集合を用意
している。

Contextual Single interface
======================================================================

Contextual Single インターフェイスは標準的なメニューと、状況に応じて中身が変化す
る単一ツールバーを表示する。

----

.. rubric:: 章末注

.. [#writer21-footnote-advanced] |OptionsDlg|
   :menuselection:`LibreOffice-->Advanced` ページ :guilabel:`Enable experimental
   features (may be unstable)` をオン
