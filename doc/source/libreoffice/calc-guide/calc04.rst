======================================================================
Calc Guide Chapter 4, Formatting Data ノート
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

セル単体またその範囲を選択し、|FormatCellsDlg| を使用すれば、そこから書式設定の
すべてを制御可能だ。

このダイアログボックスは |Ctrl| + :kbd:`1` で開くのが早い。

Multiple lines of text
----------------------------------------------------------------------

複数行テキストの実現には自動折り返しまたは手動改行を使用しろ。

Automatic wrapping
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

セルで複数行テキストを表示する方法は次のどれでも可：

* |FormatCellsDlg| |AlignmentTab| 内 :guilabel:`&Wrap text automatically` をオン
* |Sidebar| :guilabel:`Wrap Text` をオン
* ツールバー :guilabel:`Wrap Text` をオン

Manual line breaks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

セルに改行文字挿入を入力する方法：

* 直接編集ならば |Ctrl| + |Enter| 押し
* 数式バー編集ならば |Shift| + |Enter| 押し

必要に応じて手動でセル幅を変更するか、改行の位置を調整しろ。

Shrinking text to fit a cell
----------------------------------------------------------------------

.. admonition:: 利用者ノート

   この書式設定は嫌いで使わない。割愛。

Formatting numbers
----------------------------------------------------------------------

ツールバー :menuselection:`&View-->&Toolbars-->Formatt&ing` のボタンで間に合う書
式設定であれば、そのボタンを押して変更しろ。一部はキーバインドも設定されている：

.. csv-table::
   :delim: @
   :header-rows: 1
   :widths: auto

   書式 @ キーバインド
   金額 @ |Ctrl| + |Shift| + :kbd:`4`
   百分率 @ |Ctrl| + |Shift| + :kbd:`5`
   数値 @ |Ctrl| + |Shift| + :kbd:`1`
   日付 @ |Ctrl| + |Shift| + :kbd:`3`

より詳細な制御や他の数値書式を選択するには、いつものダイアログの |NumbersTab| を
使え。

Formatting fonts
----------------------------------------------------------------------

|FormattingToolbar| のうち、次の |UI| を使え：

* :guilabel:`Font Name` ドロップダウンリスト
* :guilabel:`Font Size` ドロップダウンリスト
* :guilabel:`Bold` ボタン (|Ctrl| + :kbd:`B`)
* :guilabel:`Italic` ボタン (|Ctrl| + :kbd:`I`)
* :guilabel:`Underline` ボタン (|Ctrl| + :kbd:`U`)

段落の配置を変更するには：

* :guilabel:`Align Left` ボタン (|Ctrl| + :kbd:`L`)
* :guilabel:`Align Center` ボタン (|Ctrl| + :kbd:`E`)
* :guilabel:`Align Right` ボタン (|Ctrl| + :kbd:`R`)

.. admonition:: 利用者ノート

   日本語フォントに斜体は効かない？

詳細は割愛するが、セル内の言語を変更することで、同じ文書内に異なる言語を共存させ
ることが可能。

フォント名ドロップダウンリストの各項目の描画に対して、おそらく表示処理を軽くする
目的で、対応するフォントを使わせないオプションがある（後でやる）。

Font effects
----------------------------------------------------------------------

|FormatCellsDlg| |FontEffectsTab| 内から各種効果を与えられる（利用可能な項目は
|Calc05| で述べられる）。

適用対象は次のいずれか：

* 現在選択中のもの
* キャレットを含む単語全体
* これからタイプする新規テキスト

Text orientation
----------------------------------------------------------------------

|FormatCellsDlg| |AlignmentTab| 内から指定可能な書式を述べている。

縦書き関連で調べるかもしれない。

Using the Formatting toolbar tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|FormattingToolbar| のうち、次のボタンが関係する：

* :guilabel:`Text direction from top to bottom`
* :guilabel:`Right-To-Left`
* :guilabel:`Left-To-Right`

ただし、これらの図像は |OptionsDlg| 設定次第で有効になる。

|LanguagesPage| :guilabel:`Default Language for Documents` で、

* :guilabel:`Asian` および
* :guilabel:`Complex &text layout`

がオンの場合のみだ。

Asian typography
----------------------------------------------------------------------

上記 :guilabel:`Asian` がオンのときに :guilabel:`Asian Typography` タブが
|FormatCellsDlg| に現れる。

* 最初の長い名前のチェックボックスは禁則文字に関する。オンにすると玄人風になる。
* :guilabel:`Apply &spacing between Asian and non-Asian text` は絶対にオンにした
  い。

Formatting cell borders
----------------------------------------------------------------------

セル枠の容姿を設定するには次を使え：

* |FormatCellsDlg| |BordersTab|
* |FormattingToolbar| のドロップダウンリスト

  * :guilabel:`Borders`
  * :guilabel:`Border Style`
  * :guilabel:`Border Color`

Formatting cell backgrounds
----------------------------------------------------------------------

セル背景を設定するには次を使え：

* |FormatCellsDlg| |BackgroundTab|
* |FormattingToolbar|  :guilabel:`Background Color` ドロップダウンリスト

AutoFormat of cells and sheets
======================================================================

Using AutoFormat
----------------------------------------------------------------------

少なくとも三列・行（ヘッダーを含む）上で書式を設定したいセルを選択する。
|MenuBar| から :menuselection:`F&ormat-->AutoFormat &Styles...` を選択してダイア
ログを開く。そこからプリセットのスタイルを選択するか、逆に、シート上でスタイリン
グしてから :guilabel:`Add` ボタンで追加するという機能だ。

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

.. _calc04-anchor-highlighting:

Value highlighting
======================================================================

値強調の表示切替は |Ctrl| + :kbd:`F8` 押しが良い。

この表示は初期状態で有効にしたい。|OptionsDlg| |CalcViewPage| の
:menuselection:`Value h&ighlighting` をオンに設定しろ。

Using conditional formatting
======================================================================

指定した条件によってセルの書式が変わるように設定する機能だ。想定した仕様から外れ
たデータを強調表示するために利用する。

Setting up conditional formatting
----------------------------------------------------------------------

事前条件は :menuselection:`&Data-->Ca&lculate-->Auto&Calculate` がオンになっ
ていることだ。

セルを選択してから :menuselection:`F&ormat-->C&onditional-->` 以下のサブメニュー
各項目を選択するとダイアログがそれぞれ開く。

Condition
   条件を満たすセルデータを強調表示するための書式を規定する。
Color Scale
   セル値に応じて背景色を設定する。何段階かに色分けして表示する。
Data Bar
   棒グラフの棒一本一本を各セル内に描画してデータを表現する。`All Cells` 限定。
Icon Set
   各セルのデータの横に図像を表示し、設定範囲内のどこにデータが位置するのかを視
   覚的に表現する。`All Cells` 限定。
Date
   現在を基準として特定の日付範囲を指定書式で表記する。

Types of conditional formatting
----------------------------------------------------------------------

|ConditionalFormattingDlg| を見ていく。

Cell value
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ドロップダウンリストで設定された条件に従う升目か升目範囲に対して選択スタイルを適
用する。書式設定は升目それぞれに適用され、条件は選択範囲の他の升目の値に依存する
場合がある。

セルの値が数値やテキストの場合に有効な条件一覧：

.. csv-table:: Conditions for number and text in cells
   :delim: |
   :header-rows: 1
   :widths: auto

   項目 | 適用条件
   is equal to | 指定値と等しい場合
   is not equal to | 指定値と等しくない場合
   is duplicate | 範囲内の最低一つのセルの内容が等しい場合
   is not duplicate | セルの内容が範囲内で一意である場合
   begins with | セル内容が指定値から始まる場合
   ends with | セル内容が指定値で始まる場合
   contains | セル内容が指定値を含む場合
   does not contain | セル内容が指定値を含まない場合

この条件は升目内容の内部テキスト変換に適用される。数値は同等のテキスト表現と比較
される。数値の升目書式（通貨、科学、使用者定義、等々）は比較の対象とはならない。

数値の場合にのみ有効な条件一覧もある。

.. list-table:: Conditions for number-only cell values
   :align: left
   :header-rows: 1
   :stub-columns: 0
   :widths: auto

   * - 条件
     - 選択スタイルが適用される場合のセルの値
   * - is less than
     - 定義値より厳密に小さい
   * - is greater than
     - 定義値より厳密に大きい
   * - is less than or equal to
     - 定義値より小さいか等しい
   * - is greater than or equal to
     - 定義値より大きいか等しい
   * - is between
     - 定義値（下限値と上限値）の間（境界値そのものも含む）
   * - is not between
     - 下限値と上限値の間にない（境界値そのものに等しい値は適用）
   * - is in top N elements
     - 範囲の最大値と、同じ範囲の N 番目の大きい要素の間にある
   * - is in bottom N elements
     - 範囲の最小値と、同じ範囲の N 番目の小さい要素の間にある
   * - is in top N percent
     - 範囲内のセル数の上位 N パーセント。例えば、20 セルの範囲で N が 20 の場
       合、その範囲の最後の 4 セルに対してスタイルが適用される。
   * - is in bottom N percent
     - 下位 N パーセント版
   * - is above average
     - セル範囲の値の平均よりも厳密に大きい
   * - is below average
     - セル範囲の値の平均よりも厳密に小さい
   * - is above or equal average
     - セル範囲の平均値より大きいか等しい
   * - is below or equal average
     - セル範囲の平均値より小さいか等しい

.. admonition:: 条件中の平均に関する注意

   関数 `AVERAGE` はデータ範囲内のテキストや空セルを無視する。この関数による結果
   が誤っている疑いがある場合は、データ範囲内のテキストを探せ。データ範囲内のテ
   キスト内容を強調表示するには、:ref:`calc04-anchor-highlighting` を見てそうし
   ろ。

エラーの場合にのみ有効な条件というのもある。右欄にエラーコードを指定する。ノート
割愛。

.. _calc04-anchor-color-scale:

Color Scale
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

条件で `All Cells` 指定時に適用可能で、セルデータ値に応じて背景色を設定する。グラ
デーション、二色、三色から指定。

`Color Scale (2 Entries)` では範囲内の最小値と最大値の色を定義する必要がある。こ
の二つはいくつかの方法で計算することが可能だ：

`Min (Max)`
   範囲の最小値（最大値）。
`Percentile`
   百分位数、並び替えたデータを百等分する 99 個の値それぞれのことで、百分位数一
   つは百分の一部分データ一つにおける最小値から最大値までの値を返す。P = 25 の場
   合、これは第一四分位数を意味する。P = 50 はデータセットの `MEDIAN` でもある。
   有効な入力値は 0 から 100 までだ。
`Value`
   最小（最大）色に固定値を設定する。
`Percent`
   範囲の最小値と最大値で定義された長さの最小値（最大値）の百分率を表す固定値。
   最小値 10% では、区間 [Min, Max] の 10% 以下の値が用いられる。最大値が 80% の
   場合は、区間 [Min, Max] の 80% 以上の値が用いられる。有効な値は 0 から 100 ま
   で。
`Formula`
   等号 ``=`` で始まる、最小（最大）色の数値を計算する数式。値には数値、日付、時
   間を指定可能。入力欄には数式を入力する。

三色では最小最大に加えて、中間値に対する色を指定することもできる。

Data Bar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|ConditionalFormattingDlg| の :guilabel:`More O&ptions...` ボタンを押すと固有オ
プション一覧が表示される。条件に `All Cells` が選択されている場合にのみ使用可。

すべてのセルを Data Bar で書式整形するにはデータ範囲の最小値と最大値を設定しなけ
ればならない。条件オプションは上記の :ref:`calc04-anchor-color-scale` と同じだが、
`Automatic` 選択肢が追加されている：

`Automatic`
   データセットの値に基づいて自動的に最大値を設定する。

.. admonition:: 利用者ノート

   オプションのほとんどは既定値か `Automatic` で十分ではあるが、
   :guilabel:`&Fill` は `Color` にしたい。

`Data Bar` の属性を選択するには、:guilabel:`More O&ptions...` ボタンを押す。
:guilabel:`Data Bar` ダイアログボックスが開く：

Entry values
   データ棒書式整形の最小値と最大値を定義する。:ref:`calc04-anchor-color-scale`
   の最少最大項目での記述を見ろ。
Bar Colors
   正と負の値の色を設定する。棒の塗りつぶし様式を :guilabel:`&Fill` から設定する：

   `Gradient`
      正値（負値）と白の間の色尺度を設定する。
   `Color`
      データ棒全体に正（負）に対する色を使用し、グラデーションは使用しない。
Axis
   データ棒の縦軸の位置を設定する。値は次のとおり：

   `Automatic`
      縦軸を最大値と最小値の中間に置く。
   `Middle`
      縦軸を列の中央に設定する。
   `None`
      縦軸を表示しない。
Bar Lengths
   データ棒の最小（最大）長さを、列幅に対する百分率で設定する。
:guilabel:`&Display bars only`
   セル内の値を表示せず、データ棒しか表示しない。

Icon Set
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Icon Set` は選択された各セルのデータの横に図像を表示し、セルデータが設定した定
義範囲内のどこに位付けられるかを視覚的に示す。利用可能な図像集合には、色つきの矢
印、無彩色矢印、色つきの旗、色つきの標識、記号、棒グラフ、四角形がある。

`Icon Set` は |ConditionalFormattingDlg| が開かれ、条件に `All Cells` が選択され
ている場合にしか触れない。

Date
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Date` はドロップダウンメニューで選択された日付範囲に応じて定義されたスタイルを
適用する。選択肢は形容詞 This, Last, Next を Day, Week, Month, Year の利用可能な
期間に適用することで形成される。例として次のものなどがある：

* Tomorrow
* Last 7 days
* This week
* Next month
* Last year

.. note::

   一週間の端点が何曜日であるかは locale 依存だ。|OptionsDlg| |LanguagesPage| を
   確認しろ。

Formula is
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

右欄の数式の評価がゼロでない場合に選択した見てくれを適用する。数式は真偽値を評価する
テスト条件と同様に表現される。

本書の例ではセル内の日付と現在のそれを比較して整形したい書式を場合分けしている。

Conditional formatting management
----------------------------------------------------------------------

いったん定義した条件付き書式は :menuselection:`F&ormat-->C&onditional-->
&Manage...` で編集可能。

Copying cell styles
----------------------------------------------------------------------

条件付き書式設定に使用した見てくれを他のセルに後で適用する手順：

#. 条件付き書式を設定したセルをクリックし、クリップボードにコピーする。
#. コピーしたセルと同じ書式を適用するセルを選択する。
#. |PasteSpecialDlg| を開く。|Calc02| を見ろ。
#. :guilabel:`For&mats` のみが選択されていることを確認し、|OK| を押して条件付き
   書式をセルに貼り付ける。

Hiding and showing data
======================================================================

Calc では、要素を隠して計算機の画面から見えなくしたり、スプレッドシートを印刷す
るときに印刷されないようにしたりすることが可能だ。たとえば、B 列を隠した場合、A
列から C 列へのコピーを選択すると B 列がコピーされる。隠し要素が再び必要になった
ときは、逆の手順でそれを見せることが可能だ。

Hiding data
----------------------------------------------------------------------

.. ここで言う隠すとは、画面または印刷からという意味に取る。

Sheets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

シートを隠す場合は、シートタブの右クリックメニューから :menuselection:`&Hide
Sheet` を実行する。

Rows and columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

列または行を隠す場合は、列ヘッダーまたは行ヘッダーをクリックして選択状態にし、右
クリックメニューから :menuselection:`&Hide Row` または :menuselection:`&Hide
Column` を実行する。

.. tip::

   隠れた列・行に対する表示器を有効または無効にするには
   :menuselection:`&View-->Hidden &Row/Column Indicator` を選択する。

.. _calc04-anchor-protect-sheet:

Cells
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

個々のセルを隠すのは複雑だ。まず、セルを保護かつ隠しに定義し、次にシートを保護す
る必要がある：

#. 隠したいセルを選択する
#. |FormatCellsDlg| を開く
#. |CellProtectionTab| をクリックし、セルを隠して印刷するオプションを選択する
#. |OK| を押して変更を保存してダイアログボックスを閉じる
#. |MenuBar| の :menuselection:`&Tools-->Protect &Sheet...` またはシートタブ右ク
   リックメニューから :menuselection:`Protect &Sheet...` を選択して
   |ProtectSheetDlg| を開く
#. :guilabel:`P&rotect this sheet and the contents of protected cells` をオンに
   する
#. パスワードを作成し、そのパスワードを確認する
#. 保護セル（またはその裏）を選択できるように、:guilabel:`&Allow all users of
   this sheet to` 内のオプションをオンかオフにする。
#. |OK| を押して変更を保存してダイアログボックスを閉じる

.. note::

   セル内容を隠すと、そうなるのはセルに含まれる内容だけであり、保護されたセルは
   変更できない。空白セルはスプレッドシートに表示されたままだ。

Showing data
----------------------------------------------------------------------

.. admonition:: 読者ノート

   隠したシート、列、行を復元する方法は対応する Show コマンドを実行しろ。

Sheets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|MenuBar| から :menuselection:`&Sheet-->&Show Sheet...` を実行し、ダイアログボッ
クスから表示するシートを選べ。

Rows and columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

先頭列を隠しから見せに戻す場合には選択にコツがいる。行 :guilabel:`1` を選択し、
列ヘッダー :guilabel:`B` の右クリックメニューから :menuselection:`S&how Columns`
を実行するのだ。列の場合、縦横を入れ替えて同様の操作をすることで表示を戻すことに
なる。

#. 隠れた行・列の両隣接行・列を選択する
#. |MenuBar| の :menuselection:`F&ormat-->Ro&ws-->&Show` を選択すると行が、
   :menuselection:`F&ormat-->Colu&mns-->&Show` を選択すると列がそれぞれ現れ、印
   刷できるようになる。
#. または、行または列のヘッダーを右クリックし、コンテキストメニューから
   :menuselection:`Sho&w Rows` または :menuselection:`S&how Columns` を選択

Cells
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. |ProtectSheetDlg| を開く (see :ref:`calc04-anchor-protect-sheet`)
#. シートの保護を解除するパスワードを入力し、|OK| を押す
#. |FormatCellsDlg| を開く
#. |CellProtectionTab| をクリックし、セル隠しオプションの選択をオフにする
#. |OK| を押す

.. note::

   |ProtectSheetDlg| を使用してシートを保護する場合、パスワード欄を空白のままに
   することが可能だ。この場合、上記の手順の一部は生じないか、必要がない。
