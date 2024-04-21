======================================================================
Calc Guide Chapter 16 User Interface Variants ノート
======================================================================

.. include:: ./calc-inc.txt

.. contents:: 章見出し
   :depth: 3
   :local:

Introduction
======================================================================

既定では LibreOffice のコマンドは階層式メニューと図像満載のツールバーにまとめら
れている。これは古典的な UI であり、本書の他の多くの章における各種説明でも想定さ
れていることだ。

古典的 UI はひじょうに柔軟で、多くの UI 部品の表示有無、位置変更、ツールバー、メ
ニューに割り当てられたコマンドの再定義、メニューやツールバーの新規作成、個々の
キーバインドの再定義などが可能だ。

ここからが本題で、古典的 UI を含む UI 変種は次で全てだ：

* Standard Toolbar
* Tabbed: MS Office で使われているリボンに最もよく似ている UI
* Single Toolbar: 画面解像度の低い環境の利用者向け
* Sidebar
* Tabbed Compact: 省スペース版 Tabbed
* Groupedbar Compact: 最も頻繁に使用される機能を図像で、その他の機能をドロッ
  プダウンメニューで表示する。縦長空間が好ましい。
* Contextual Single: 文脈依存の内容である一行のツールバー

これらのうち Standard Toolbar, Single Toolbar, Sidebar, Contextual Single は古典
的 UI で使用されている部品の代替構成と考えられる。他の三つは notebook bar の使用
に基づく。

Selecting the user interface
======================================================================

Calc をセットアップすると既定 UI は Standard Toolbar になる。利用者は上述の UI
のいずれかを選択し、いつでも切り替えることが可能だ。

#. メニュー :menuselection:`&View --> User &Interface...` を実行
#. ダイアログボックス :guilabel:`On the Select Your Preferred User Interface` で
   :guilabel:`UI variants` から一つ選ぶ。選択肢を変えると右側のプレビューとメモ
   が示される。
#. 選択した内容を LibreOffice のすべてのコンポーネントに適用するか、Calc にのみ
   適用するかを決めて、該当するボタンを押す。
#. :guilabel:`&Close`

選択した内容に合わせて Calc ウィンドウが更新される。

Standard interfaces
======================================================================

Standard Toolbar, Single Toolbar, Sidebar インターフェイスは密接に関連する。これ
らの既定構成を以下見ていく。

Standard Toolbar
   LibreOffice のインストール時に選択されている古典的 UI だ。次の構成を取る：

   * ツールバーが二つ (:guilabel:`Standard`, :guilabel:`Formatting`)
   * Sidebar
   * タブパネルにタブが五つ
Single Toolbar
   * ツールバーは頻繁に使用される機能を含む :guilabel:`Standard (Single Mode)`
     しか見せない。
   * Sidebar は :guilabel:`Show/Hide` ボタンしか見せない。
Sidebar
   * ツールバーは :guilabel:`Standard` 一つが表示。
   * Sidebar は完全に開く。

メニュー :menuselection:`&View -->` を使って、これら三つの変種それぞれの要素の表
示有無を変更することが可能。メニュー、ツールバー、キーバインドの設定は
:menuselection:`&Tools --> &Customize...` ダイアログボックスのタブで変更可能。

これらの変種は notebook bar を土台にしていないため、:menuselection:`&Tools -->
&Customize...` ダイアログボックスの :guilabel:`Notebookbar` タブには構成の選択肢
がない。

Contextual Single
======================================================================

Contextual Single 変種の初期構成は：

* メニューは表示される
* ツールバーは表示されない

ツールバーは現在の操作対象に対応して自動的に見えたり隠れたりする。例えば、

* 画像が選択されていれば :guilabel:`Image` ツールバーが、
* 図面オブジェクトが選択されていれば :guilabel:`Drawing Object Properties` ツー
  ルバーが

表示されるという具合だ。

Contextual Single 変種に UI を切り替えると、Sidebar がまだ開かれていない場合、自
動的に開く。

メニュー :menuselection:`&View -->` を使って、これら三つの変種それぞれの要素の表
示有無を変更することが可能。メニュー、ツールバー、キーバインドの設定は
:menuselection:`&Tools --> &Customize...` ダイアログボックスのタブで変更可能。

この変種も notebook bar を土台にしていないため、:menuselection:`&Tools -->
&Customize...` ダイアログボックスの :guilabel:`Notebookbar` タブには構成の選択肢
がない。

Tabbed interface
======================================================================

Introduction
----------------------------------------------------------------------

Tabbed インターフェイスは Microsoft Office のような専売特許の事務ソフトウェアか
ら来た利用者は馴染みのあるもの。これには

* メニューバー
* 図像バー
* タブバー
* アクティブなタブの図像
* 1つ以上のタブ固有のメニュー
* クイックメニュー

が搭載されている。図像バーの :guilabel:`Menubar` 図像をクリックすると、メニュー
バーの表示有無が切り替わる。

Calc ではこの UI には常に表示される九つの固定タブと、時々表示される六つの追加タ
ブがある。

* 各タブには時々の対象物ごとにまとめられた図像集合が示される。
* 各タブの右端には固有のドロップダウンメニューがある。
* クイックメニュー（ハンバーガー）はすべてのタブで共通。

:menuselection:`&Tools --> &Customize...` ダイアログボックスのタブ
:guilabel:`Notebookbar` を用いて Tabbed インターフェイスをカスタマイズし、さまざ
まなタブの図像それぞれの表示有無を切り替えることが可能だ。Chapter 15 を参照し
ろ。図像寸法も調整可能だ。

タブの図像が Calc ウィンドウの幅に収まらない場合は、行の右端に :guilabel:`»` が
表示される。これを押せば現在表示されていない追加オプションが現れる。

Icon bar
----------------------------------------------------------------------

図像バーはタブの左に位置する。見ればわかるが図像集合の編成は左から：

#. :guilabel:`Menubar`: メニューバー表示有無切り替え
#. :guilabel:`Open (Ctrl+O)`
#. :guilabel:`Save (Ctrl+S)`
#. :guilabel:`Undo (Ctrl+Z)`: これと次の図像のツールチップは前後に実行したコマン
   ドで内容末尾がその動作を示す文字列になる。
#. :guilabel:`Redo (Ctrl+Y)`
#. :guilabel:`Print (Ctrl+P)`

Quick menu
----------------------------------------------------------------------

タブの右側にはクイックメニュー（ハンバーガー）があり、よく使われるコマンドやリン
クが記載されている。

Fixed tabs
----------------------------------------------------------------------

固定タブは次の九つだ：

* :guilabel:`&File`
* :guilabel:`&Home`
* :guilabel:`&Insert`
* :guilabel:`&Layout`
* :guilabel:`&Data`
* :guilabel:`&Review`
* :guilabel:`&View`
* :guilabel:`E&xtension`
* :guilabel:`&Tools`

各固定タブには関連メニューがあり、タブの右端にあるボタンからアクセスする。このボ
タンにはタブと同じ名前が付けられている。

本書のスクリーンショットについて、次の点に注意しろ：

* 撮影用に Calc のメインウィンドウを小さくしているため、タブのほとんどに
  :guilabel:`»` が示され、選択肢の一部が見えていない。
* 図像が表示されている各タブについて、:guilabel:`»` を押したときに表示される追
  加選択肢を示す別の図を含んでいる。
* タブの右端にあるメニューの内容を示す図が付いている。

.. admonition:: 利用者ノート

   本書のスクリーンショットでは横長のウィンドウを真っ二つに切断して続けて示して
   いる。それがわかれば誤解のおそれはないと考えられる。

File tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`&File` タブには :menuselection:`&File` と :menuselection:`&Help` のメ
ニューがある。それらの隣にはそれぞれ :guilabel:`Close` 図像と
:guilabel:`LibreOffice Help` の図像がある。

.. admonition:: 利用者ノート

   この内容なら古典的メニュー UI のほうが使いやすい。

Home tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`&Home` タブには :menuselection:`&Home` メニューボタン一つがある。そ
して次の三つの図像がこれに隣接する：

* :guilabel:`Find and Replace (Ctrl+H)`
* :guilabel:`Sort Ascending`
* :guilabel:`AutoFilter (Ctrl+Shift+L)`

.. admonition:: 利用者ノート

   Paste Special コマンドのための UI が見当たらない。キーバインドで事足りるから
   なのか、使用頻度の都合によるのか。

Insert tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`&Insert` タブには :menuselection:`&Insert` メニューボタン一つが右端に
ある。これに次の三つの図像が隣接する：

* :guilabel:`Insert or Edit Pivot Table`
* :guilabel:`Show Draw Functions`
* :guilabel:`Function List`

.. admonition:: 利用者ノート

   * :guilabel:`Show Draw Functions` をオンにすると :guilabel:`Drawing` ツールバー
     が浮遊状態で表示される。
   * :guilabel:`Function List` は Sidebar が開く。

Layout tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`&Layout` タブ右端にあるメニューボタンは一個で
:menuselection:`&Layout`だ。それに :guilabel:`Format Page` 図像が隣接する。

.. admonition:: 利用者ノート

   このタブにはセル、シート、ヘッダー、フッター、行、列といった対象に関するコマ
   ンドがまとまっているようだ。

Data tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`&Data` タブ右端には :menuselection:`&Data` メニューボタン一つがある。そ
して次の三つの図像がこれに隣接する（この組み合わせはさっき見たものだ）：

* :guilabel:`Find and Replace (Ctrl+H)`
* :guilabel:`Sort Ascending`
* :guilabel:`AutoFilter (Ctrl+Shift+L)`

Review tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`&Review` タブ右端には :menuselection:`&Review` メニューボタンが一つあ
る。ここに隣接するのは :guilabel:`Manage Track Changes` 図像だ。

.. admonition:: 利用者ノート

   ただし図像脇のラベルは :guilabel:`Manage` だ。

View tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`&View` タブ右端には :menuselection:`&View` メニューボタン一つがある。
:guilabel:`Zoom` 図像がこれに隣接する。

Extension tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`E&xtension` タブにあるメニューボタンは :menuselection:`E&xtension` 一
つだ。このメニューボタンには :guilabel:`Extension Manager (Ctrl+Alt+E)` 図像一つ
が隣接している。

.. admonition:: 利用者ノート

   * ただし図像横のラベルは :guilabel:`Extension` だ。
   * 本書の記述は拡張が何も入っていない状態に基づいていると考えられる。拡張が UI
     要素をタブに追加する構造のはずだ。

Tools tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`&Tools` タブにあるメニューボタンは :menuselection:`&Tools` 一つだ。こ
のメニューボタンには :guilabel:`Options` 図像一つが隣接している。

Additional tabs
----------------------------------------------------------------------

追加タブは物を選択すると :guilabel:`&View` タブと :guilabel:`E&xtension` タブの
間に現れる。次の六つだ：

* :guilabel:`&Draw`
* :guilabel:`Fo&rm`
* :guilabel:`Ima&ge`
* :guilabel:`&Media`
* :guilabel:`&Object`
* :guilabel:`&Print`

Draw tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`&Draw` タブは図面物を選択するときに現れる。

:guilabel:`&Draw` タブ右端には :menuselection:`&Draw` メニューボタン一つがある。
そして次の図像がこれに隣接する：

* :guilabel:`Area`
* :guilabel:`Line`
* :guilabel:`Position and Size`

Form tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Fo&rm` タブは設計モードでフォーム部品が選択されたときに現れる。

:guilabel:`Fo&rm` タブ右端には :menuselection:`Fo&rm` メニューボタン一つがある。
:guilabel:`Form Properties` 図像がこれに隣接する。

Image tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Ima&ge` タブは画像を選択すると現れる。

:guilabel:`Ima&ge` タブ右端には :menuselection:`Ima&ge` メニューボタン一つがあ
る。これに次の四つの図像が隣接する：

* :guilabel:`Save`
* :guilabel:`Area`
* :guilabel:`Line`
* :guilabel:`Position and Size`

Media tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`&Media` タブはメディアオブジェクトを選択すると現れる。

:guilabel:`&Media` タブ右端には :menuselection:`&Media` メニューボタン一つがあ
る。これに次の三つの図像が隣接する：

* :guilabel:`Area`
* :guilabel:`Line`
* :guilabel:`Position and Size`

.. admonition:: 利用者ノート

   AVI 音声ファイルで試した。

Object tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`&Object` タブは OLE オブジェクトなどを選択すると現れる。

:guilabel:`&Object` タブ右端には :menuselection:`&Object` メニューボタン一つがあ
る。これに次の三つの図像が隣接する：

* :guilabel:`Area`
* :guilabel:`Line`
* :guilabel:`Position and Size`

Print tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`&Print` タブは印刷プレビューが選択されている間現れる。

:guilabel:`&Print` タブ右端には :menuselection:`&Print` メニューボタン一つがあ
る。これに :guilabel:`Full Screen` 図像が隣接する。

.. admonition:: 利用者ノート

   このタブがいちばん自然に使えるタブだと思う。

Tabbed Compact interface
======================================================================

Tabbed Compact インターフェイスは前節の Tabbed インターフェイスをより凝縮させた
ものだ。タブの編成が Tabbed 無印と同じであるが、各タブのコマンドは一行に表並ぶた
め、垂直方向に占める画面帯域が少なく済む。

個々のタブとタブメニューの内容は、Tabbed 無印インターフェースの対応する部品と同
様だ。

Tabbed Compact インターフェイスは :menuselection:`&Tools --> &Customize...` ダイ
アログボックスの :guilabel:`Notebookbar` を使ってカスタマイズ可能であり、さまざ
まなタブ内の図像それぞれの表示有無を切り替えることが可能だ。Chapter 15 を参照し
ろ。

:guilabel:`Options` ダイアログボックスの :menuselection:`LibreOffice --> View`
ページの :guilabel:`Icon Size` 区画 :menuselection:`&Notebookbar` ドロップダウン
リストで図像サイズを調整可能だ。

Groupedbar Compact interface
======================================================================

Groupedbar Compact インターフェイスはコマンドをまとめるのにツールバーやタブを利
用しない。代わりに、操作時点の状況（例えば空セルを選択している等）に応じてコマン
ド群がグループ化され、縦線で視覚的に区切られている。各グループには図像、メニュー、
その他のコントロールが適宜配置される。

Tabbed インターフェイスの動作と同様に、グループすべてがメインウィンドウの幅に収
まらない場合、右側に :guilabel:`»` が表示される。これを押すと見えていないグルー
プが追加的に示される。

グループの多くはニューボタンの上に位置する図像を複数持つ。メニューボタンを押す
とグループに関連するコマンドのメニューにアクセス可能だ。

.. admonition:: 利用者ノート

   初見では違和感がある。

Groupedbar Compact インターフェイスに表示されるグループは使用状況によって変化す
る。例えば、現在画像が選択されている状況では :menuselection:`F&ont`,
:menuselection:`&Paragarah` グループなどが隠れ、:menuselection:`Im&age`,
:menuselection:`&Arrange` などのグループが現れる。

Groupedbar Compact インターフェイスの右端には次の一連の図像を含む小領域がある：

* :guilabel:`Find and Replace (Ctrl+H)`
* :guilabel:`LibreOffice Help`
* :guilabel:`Close`

これらは :menuselection:`&Menu` ラベルのあるボタンの上部に位置する。このメニュー
の内容は常時決まったコマンドを搭載している。

Groupedbar Compact インターフェイスは :menuselection:`&Tools --> &Customize...`
ダイアログボックスのタブ :guilabel:`Notebookbar` を用いてカスタマイズ可能だ。

:guilabel:`Options` ダイアログボックスの :menuselection:`LibreOffice --> View`
ページの :guilabel:`Icon Size` 区画 :menuselection:`&Notebookbar` ドロップダウン
リストで図像サイズを調整可能だ。
