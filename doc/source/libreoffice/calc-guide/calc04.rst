======================================================================
Calc Guide Chapter 4 Formatting Data ノート
======================================================================

.. include:: ./calc-inc.txt

.. contents:: 章見出し
   :local:

Introduction
======================================================================

セルに対する設定に関する次の三点を習得しろ：

* 手動書式設定
* スタイル書式設定
* 条件付き書式設定

Formatting data
======================================================================

セル単体またその範囲を選択し、:guilabel:`Format Cells` ダイアログボックスを使用
すれば、そこから書式設定のすべてを制御可能だ。

このダイアログボックスは :kbd:`Ctrl` + :kbd:`1` で開くのが早い。

Multiple lines of text
----------------------------------------------------------------------

複数行テキストの実現には自動折り返しまたは手動改行を使用しろ。

Automatic wrapping
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

セルで複数行テキストを表示する方法は次のどれでも可：

* :guilabel:`Format Cells` ダイアログ :guilabel:`Alignment` タブ内
  :guilabel:`&Wrap text automatically` をオン
* サイドバー :guilabel:`Wrap Text` をオン
* ツールバー :guilabel:`Wrap Text` をオン

Manual line breaks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

セルに改行文字挿入を入力する方法：

* 直接編集ならば :kbd:`Ctrl` + :kbd:`Enter` 押し
* 数式バー編集ならば :kbd:`Shift` + :kbd:`Enter` 押し

必要に応じて手動でセル幅を変更するか、改行の位置を調整しろ。

Shrinking text to fit a cell
----------------------------------------------------------------------

.. admonition:: 利用者ノート

   この書式設定は嫌いで使わない。割愛。

Formatting numbers
----------------------------------------------------------------------

ツールバー :menuselection:`&View --> &Toolbars --> Formatt&ing` のボタンで間に合
う書式設定であれば、そのボタンを押して変更しろ。一部はキーバインドも設定されてい
る：

.. csv-table::
   :delim: |
   :header: 書式,キーバインド
   :widths: auto

   金額 | :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`4`
   百分率 | :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`5`
   数値 | :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`1`
   日付 | :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`3`

より詳細な制御や他の数値書式を選択するには、いつものダイアログの
:guilabel:`Numbers` タブを使え。

Formatting fonts
----------------------------------------------------------------------

:guilabel:`Formatting` ツールバーのうち、次の UI を使え：

* :guilabel:`Font Name` ドロップダウンリスト
* :guilabel:`Font Size` ドロップダウンリスト
* :guilabel:`Bold` ボタン (:kbd:`Ctrl` + :kbd:`B`)
* :guilabel:`Italic` ボタン (:kbd:`Ctrl` + :kbd:`I`)
* :guilabel:`Underline` ボタン (:kbd:`Ctrl` + :kbd:`U`)

段落の配置を変更するには：

* :guilabel:`Align Left` ボタン (:kbd:`Ctrl` + :kbd:`L`)
* :guilabel:`Align Center` ボタン (:kbd:`Ctrl` + :kbd:`E`)
* :guilabel:`Align Right` ボタン (:kbd:`Ctrl` + :kbd:`R`)

.. admonition:: 利用者ノート

   日本語フォントに斜体は効かない？

詳細は割愛するが、セル内の言語を変更することで、同じ文書内に異なる言語を共存させ
ることが可能。

フォント名ドロップダウンリストの各項目の描画に対して、おそらく表示処理を軽くする
目的で、対応するフォントを使わせないオプションがある（後でやる）。

Font effects
----------------------------------------------------------------------

:guilabel:`Format Cells` ダイアログ :guilabel:`Font Effects` タブ内から各種効果
を与えられる（利用可能な項目は Chapter 5 で述べられる）。

適用対象は次のいずれか：

* 現在選択中のもの
* キャレットを含む単語全体
* これからタイプする新規テキスト

Text orientation
----------------------------------------------------------------------

:guilabel:`Format Cells` ダイアログ :guilabel:`Alignment` タブ内から指定可能な書
式を述べている。

縦書き関連で調べるかもしれない。

Using the Formatting toolbar tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Formatting` ツールバーのうち、次のボタンが関係する：

* :guilabel:`Text direction from top to bottom`
* :guilabel:`Right-To-Left`
* :guilabel:`Left-To-Right`

ただし、これらのアイコンは :guilabel:`Options` ダイアログ設定次第で有効になる。

:menuselection:`Language Settings --> Languages --> Default Language for
Documents` で、

* :guilabel:`Asian` および
* :guilabel:`Complex &text layout`

がオンの場合のみだ。

Asian typography
----------------------------------------------------------------------

上記 :guilabel:`Asian` がオンのときに :guilabel:`Asian Typography` タブがセル書
式ダイアログに現れる。

* 最初の長い名前のチェックボックスは禁則文字に関する。オンにすると玄人風になる。
* :guilabel:`Apply &spacing between Asian and non-Asian text` は絶対にオンにした
  い。

Formatting cell borders
----------------------------------------------------------------------

セル枠の容姿を設定するには次を使え：

* :guilabel:`Format Cells` ダイアログ :guilabel:`Borders` タブ内 UI
* :guilabel:`Formatting` ツールバーのドロップダウンリスト

  * :guilabel:`Borders`
  * :guilabel:`Border Style`
  * :guilabel:`Border Color`

Formatting cell backgrounds
----------------------------------------------------------------------

セル背景を設定するには次を使え：

* :guilabel:`Format Cells` ダイアログ :guilabel:`Background` タブ内 UI
* :guilabel:`Formatting` ツールバー :guilabel:`Background Color` ドロップダウン
  リスト

AutoFormat of cells and sheets
======================================================================

Using AutoFormat
----------------------------------------------------------------------

少なくとも三列・行（ヘッダーを含む）上で書式を設定したいセルを選択する。メニュー
:menuselection:`F&ormat --> AutoFormat &Styles...` でダイアログを開く。そこから
プリセットのスタイルを選択するか、逆に、シート上でスタイリングしてから
:guilabel:`Add` ボタンで追加するという機能だ。

Defining a new AutoFormat
----------------------------------------------------------------------

AutoFormat を新規定義すると、スプレッドシートすべてで使用可能なものとなる。

#. 適当なセルグループに対して、あらかじめフォント、枠、背景の容姿を与えておく
#. 最低でも 4x4 のセル範囲を選択する
#. 上記コマンドで :guilabel:`AutoFormat Style` ダイアログボックスを開く
#. :guilabel:`&Add` ボタンを押す
#. 意味のある名前を与える

これで :guilabel:`Format` 一覧に新規 AutoFormat 項目が現れる。

* AutoFormat ではセルスタイルは使用しない。選択範囲に直接書式を適用する。
* 新しい AutoFormat は ユーザープロファイルに保存され、スプレッドシート文書の一
  部にはならない（別のユーザーが当該文書を開く状況を想定すると注意点に気づけ
  る）。

.. admonition:: 利用者ノート

   微妙に失敗する。適用時に日付や金額のセル書式が失われる。

Value highlighting
======================================================================

値強調の表示切替は :kbd:`Ctrl` + :kbd:`F8` 押しが良い。

この表示は初期状態で有効にしたい。設定ダイアログの :menuselection:`LibreOffice
Calc --> View` 画面の :menuselection:`Display --> Value h&ighlighting` をオンに
設定しろ。

Using conditional formatting
======================================================================

指定した条件によってセルの書式が変わるように設定する機能だ。想定した仕様から外れ
たデータを強調表示するために利用する。

Setting up conditional formatting
----------------------------------------------------------------------

事前条件は :menuselection:`&Data --> Ca&lculate --> Auto&Calculate` がオンになっ
ていることだ。

セルを選択してから :menuselection:`F&ormat --> C&onditional -->` 以下のサブメ
ニュー各項目を選択するとダイアログがそれぞれ開く。

Condition
   条件を満たすセルデータを強調表示するための書式を規定する。
Color Scale
   セル値に応じて背景色を設定する。何段階かに色分けして表示する。
Data Bar
   棒グラフの棒一本一本を各セル内に描画してデータを表現する。All Cells 限定。
Icon Set
   各セルのデータの横に図像を表示し、設定範囲内のどこにデータが位置するのかを視
   覚的に表現する。All Cells 限定。
Date
   現在を基準として特定の日付範囲を指定書式で表記する。

Types of conditional formatting
----------------------------------------------------------------------

:guilabel:`Condition` ダイアログを見ていく。

Cell value
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

条件は選択範囲でない他のセルの値に依存することがある。

セルの値が数値やテキストの場合に有効な条件一覧（最後の四つは数値には指定しないほ
うがいいだろう）：

.. csv-table::
   :delim: |
   :header: 項目,適用条件
   :widths: auto

   is equal to | 指定値と等しい場合
   is not equal to | 指定値と等しくない場合
   is duplicate | 範囲内の最低一つのセルの内容が等しい場合
   is not duplicate | セルの内容が範囲内で一意である場合
   begins with | セル内容が指定値から始まる場合
   ends with | セル内容が指定値で始まる場合
   contains | セル内容が指定値を含む場合
   does not contain | セル内容が指定値を含まない場合

数値の場合にのみ有効な条件一覧もある。本書参照。

エラーの場合にのみ有効な条件というのもある。右欄にエラーコードを指定する。

Color Scale
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

条件で :guilabel:`All Cells` 指定時に適用可能で、セルデータ値に応じて背景色を設
定する。グラデーション、二色、三色から指定。

二色では範囲の最小最大に対応する色を定義する。計算方法は複数ある。

三色では最小最大に加えて、中間値に対する色を指定することもできる。

Data Bar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

条件で :guilabel:`All Cells` 指定時に適用可能で、各セルに棒グラフの棒一本を対応
させて描く。こちらは Color Scale で使用可能のオプションの他に
:guilabel:`Automatic` も指定可能だ。

:guilabel:`More Options` ボタンを押すと固有オプション一覧が表示される。

.. admonition:: 利用者ノート

   オプションのほとんどは既定値か :guilabel:`Automatic` で十分ではあるが、
   :guilabel:`&Fill` は :guilabel:`Color` にしたい。

Icon Set
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

条件で :guilabel:`All Cells` 指定時に適用可能で、選択された各セルのデータの横に
図像を表示し、セルデータが設定した定義範囲内のどこにあるかを視覚的に示す。

図像の個数は用意済み集合に応じて決まる。

Date
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ドロップダウンメニューで選択された日付範囲に応じて定義されたスタイルを適用する。

オプションは形容詞 This, Last, Next を Day, Week, Month, Year の利用可能な期間に
適用することで形成される。例として次のものなどがある：

* Tomorrow
* Last 7 days
* This week
* Next month
* Last year

一週間の端点が何曜日であるかは locale 依存だ。設定ダイアログ
:menuselection:`Language Settings --> Languages` を確認しろ。

Formula is
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

右欄の数式の評価がゼロでない場合に容姿を適用する。数式は真偽値を評価するテスト条
件と同様に表現される。

Conditional formatting management
----------------------------------------------------------------------

いったん定義した条件付き書式は :menuselection:`F&ormat --> C&onditional -->
&Manage...` で編集可能。

Copying cell styles
----------------------------------------------------------------------

条件付き書式設定に使用した容姿を、後で他のセルに適用するには Paste Special コマ
ンドを利用する。:guilabel:`Format` のみを選択した状態で :guilabel:`&OK` を押す。

Hiding and showing data
======================================================================

ここで言う非表示とは、画面または印刷からという意味に取る。

Hiding data
----------------------------------------------------------------------

Sheets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

シートを非表示とする場合は、シートタブの右クリックメニューから
:menuselection:`&Hide Sheet` を実行する。

Rows and columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

列または行を非表示にする場合は、列ヘッダーまたは行ヘッダーをクリックして選択状態
にし、右クリックメニューから :menuselection:`&Hide Row` または
:menuselection:`&Hide Column` を実行する。

Cells
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

セルを非表示にする場合、次の少し複雑な手順を要する。この手続きで、画面上では空欄
になる：

1. セルの :kbd:`Ctrl` + :kbd:`1` ダイアログ :guilabel:`Cell Protection` タブのそ
   れらしい項目をオンにする。
2. 当該セルのあるシートタブの右クリックメニューから :menuselection:`&Protect
   Sheet...` を実行し、:guilabel:`Protect this sheet and the contents of
   protected cells` をオンにする。ダイアログ上のその他の項目も適宜設定する。

Showing data
----------------------------------------------------------------------

非表示にしたシート、列、行を復元する方法は対応する Show コマンドを実行しろ。

Sheets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

メニュー :menuselection:`&Sheet --> &Show Sheet...` を実行し、ダイアログボックス
から表示するシートを選べ。

Rows and columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

先頭列を非表示から表示に戻す場合には選択にコツがいる。行 :guilabel:`1` を選択
し、列ヘッダー :guilabel:`B` の右クリックメニューから :menuselection:`Show
Columns` を実行するのだ。列の場合、縦横を入れ替えて同様の操作をすることで表示を
戻すことになる。

Cells
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

非表示（保護）セルの復元方法は、先ほどのダイアログ指定値を通常セルのものと同等に
すればいいだろう。パスワードに注意。
