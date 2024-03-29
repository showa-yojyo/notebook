======================================================================
Calc Guide Chapter 3 Creating Charts and Graphs ノート
======================================================================

.. contents::
   :depth: 2
   :local:

Introduction
======================================================================

次の入門書を読んで情報を視覚的に表現するのに効果的な方法を学ぶといい：

* Cleveland, W. S. (1994). *The Elements of Graphing Data* (2nd ed.). Hobart
  Press.
* Tufte, E. R. (2001). *The Visual Display of Quantitative Information* (2nd
  ed.). Graphics Press.

Chart Wizard
======================================================================

:guilabel:`Chart Wizard` は図式のたたき台を生成するのに用いるのであって、調整な
どは後からやる。

Overview of Chart Wizard
----------------------------------------------------------------------

#. 名前、区分、ラベルなど、図式に含めるデータすべてを含むセルを選択する。
#. :menuselection:`&Insert --> &Chart...` を実行。
#. :guilabel:`Chart Wizard` ダイアログボックスで図式種別やその他の選択肢を決定す
   る。
#. :guilabel:`&Finish` ボタンを押す。

Selecting chart type
----------------------------------------------------------------------

基本的な図式型が十種類ある。既定の図式は 2D Column 型だ。ダイアログボックス右側
の枠内に選択された変種が強調表示される。

図式種別を変更する手順：

#. :guilabel:`Choose a Chart Type` 欄で図式種別を選択する。
#. 必要なら右枠内の変種を選択する。
#. 3D 図式を使うには :guilabel:`3D Look` をオンにする。

   * さらに :guilabel:`Realistic` か :guilabel:`Simple` を選択する。
   * Column, Bar, Pie, Area 図式に限り有効なオプションだ。
#. :guilabel:`&Next -->` を押して後述要素に変更を加える。
#. :guilabel:`&Finish` を押す。

Selecting data range
----------------------------------------------------------------------

:guilabel:`Chart Wizard` の二段階目で自動選択された対象範囲を手動で修正する。

#. 必要ならば :guilabel:`Data range` 欄のセル参照を変更する。
#. データ系列を行と列のどちらに並べるかを指示する。
#. 最初の行、列をラベルとして用いるかを選択する。
#. :guilabel:`&Next -->` を押して後述要素に変更を加える。
#. :guilabel:`&Finish` を押す。

Selecting non-adjacent data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

隣接していないセル複数からデータ範囲を作成するには、セル範囲とセル範囲をカンマや
セミコロン区切りで併記する。

.. code:: text

   $Sheet1.A1:A5,$Sheet1.D1:D5

区切り文字は次の設定ダイアログボックスオプションから設定、確認する：

* :menuselection:`Language Settings --> Languages` :guilabel:`Locale setting`
* :menuselection:`LibreOffice Calc --> Formula` :guilabel:`Array co&lumn`

Linking to external data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

外的データ源にリンクする機能がある。これにより、外部データが変更されると、図式が
自動的に更新する。

リンクできるファイルの種類は：

* HTML
* Calc
* Base
* CSV
* Excel
* 登録済みのデータ源

Chapter 11 参照。

Selecting data series
----------------------------------------------------------------------

:guilabel:`Chart Wizard` の三段階目でデータを微調整する。各データ系列は共通デー
タ集合が含まれる。この段階では各データ系列の入力範囲を変更し、図式でのデータ表現
方法を整理する。不要なデータ削除や軸に沿うデータのプロット方法の指定を含む。

Organizing data series
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

図式が期待どおりに描かれていない場合、最初に確認することは：

* データ系列すべてが正しく定義されている。
* データが行か列か。
* 最初の行か列をラベルとみなしている。

データ系列それぞれの名前は :guilabel:`Data &series` 一覧に表示される。これを整理
するには、項目を指定し、次の操作を一つ以上行う：

* データ系列の名前を変更する。右側の :guilabel:`&Data ranges` 内
  :guilabel:`Name` を選択して :guilabel:`Ran&ge for Name` 欄でセル参照を編集。
* データ系列区分のセル参照を変更する。:guilabel:`&Categories` 欄でセル参照を編
  集。
* データ系列を追加する。:guilabel:`&Add` ボタンを押して、それから新規データ系列
  のデータ範囲を定義する。
* データ系列を削除する。対象データ系列を選択後 :guilabel:`&Remove` ボタンを押
  す。
* データ系列の順序を入れ替える。:guilabel:`↑` または :guilabel:`↓` を押す。

異なるデータ系列は個別の列または行でなければならない。

Setting data series ranges
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

本文では最初のパラグラフで値と区分の区別を理解しろとある。

* 図式のほとんどは値データと区分データの両方を必要とする。
* 区分と値はそれぞれ X 軸と Y 軸に沿ってプロットされる。
* 散布図と泡図では例外的に両軸に値データを使用する。

特定の図式型に定義することができるデータ範囲は :guilabel:`&Data ranges` 欄に表示
される。

:guilabel:`Border Color` および :guilabel:`Fill Color` は空欄にすると既定の色が
採用される。明示的に RGBA 値を指定しても条件付き書式を用いてもよい。

前ページで :guilabel:`Data series in &columns` と :guilabel:`&First row as
label` がオンの場合、選択データの列ラベルがデータ系列名であるとみなされる。同様
に、:guilabel:`Data series in &rows` と :guilabel:`F&irst column as label` がオ
ンの場合、選択データの行ラベルがデータ系列名であるとみなされる。

先述のように、:guilabel:`Name` ではデータ系列名を変更する。

:guilabel:`Y-Values` は数値であり、縦軸に沿ってプロットされがちだが、必ずしもそ
うとは限らない。

:guilabel:`Categories` は区分データ範囲を定義する。

図式の種類によっては標準以外にもデータ範囲を定義する場合がある。

Selecting chart elements
----------------------------------------------------------------------

四段階目は図式要素ページだ。見出し、副見出し、軸名、格子を追加または変更する。

:guilabel:`Finish` をクリックするとウィザードは終了するが、図式は灰色の枠で示さ
れた編集モードのままであり、まだ修正することがかなう。編集モードを終了するには図
式の外側のセルをクリックしろ。

Using the Sidebar to change chart settings
======================================================================

図式の性質を Sidebar で調整可能だ。開き方は：

* :menuselection:`&View --> Sidebar` 実行
* :kbd:`Ctrl` + :kbd:`F5` 押し

Sidebar の内容は図式が選択されているか、編集モードであるかによって異なる。

* 選択時は :guilabel:`Properties` デッキは :guilabel:`Area` から始まる。
* 編集モードでは :guilabel:`Properties` デッキは :guilabel:`Chart Type` から始ま
  る。

Modifying charts
======================================================================

図式の容貌を調整するための方法を見ていく。変更内容に応じて次のいずれかの方法で修
正する：

* 図式をクリックしてそのオブジェクト性質を編集する。寸法、シート内での位置、整
  列、枠、等。
* 編集モード。データ選択、図式種、軸、見出し、データ系列、ラベル等々を変更する。

Overview of using edit mode
----------------------------------------------------------------------

* 図式にない要素を追加するには :menuselection:`&Insert -->` 以下のコマンドを実行
  する。
* 見出し、軸名、壁（背景）、凡例の位置や寸法を変更するにはまず対象をクリックす
  る。マウスポインターの絵が変わったらドラッグする。
* ダイアログボックスやメニューなどの基本的な方法で要素を修正する。
* 見出しと軸名はダブルクリックで文言を修正。その他の項目テキストはシート上のデー
  タ内のテキストを修正。
* 列や棒などをクリックして関連データ系列を選択、編集する。

Entering edit mode
----------------------------------------------------------------------

図式を編集するにはダブルクリック、または右クリックメニューから
:menuselection:`&Edit` を選択する。

* 図式に灰色枠が現れる。
* 図式編集モードに入ると、メニューと :guilabel:`Formatting` ツールバーが変化す
  る。

以降の当分の間は図式編集モードにおける挙動が記されている。

Insert menu
----------------------------------------------------------------------

Wizard で指定したことがある項目とそうでない項目がある。そうでないものを記すと、

* :menuselection:`--> &Grids...`: 各軸の大格子と小格子の表示切り替えオプション
* :menuselection:`--> Tre&nd Line...`: 回帰線指定
* :menuselection:`--> Mean &Value Lines`: データ系列に対する平均値線を表示
* :menuselection:`--> X Error &Bars`, :menuselection:`--> Y Error &Bars`: 後述す
  る。

Format menu
----------------------------------------------------------------------

* テキスト系の要素に対するコマンドを実行すると、それ用の書式設定ダイアログボック
  スが開く。
* 曲線系の要素に対するコマンドを実行すると、:guilabel:`Line` タブのみを有するダ
  イアログボックスが開く。
* :menuselection:`--> Chart Wall...` 系コマンドを実行すると、その枠、内部、透明
  度を指定するダイアログボックスが開く。
* :menuselection:`--> Chart T&ype...`: 図式種別を変更する。2D でも 3D でも。
* :menuselection:`--> &3D View...`: 3D 図式専用コマンド。
* :menuselection:`--> Format &Selection...`: 選択要素に対応する設定ダイアログ
  ボックスが開く。塗りつぶし、枠、位置、透明度、フォント、ラベル、尺度……。
* :menuselection:`--> Arrange&ment -->`: Z-order 昇降操作。

Formatting toolbar
----------------------------------------------------------------------

:guilabel:`Select Chart Element` ドロップダウンリストは当ツールバー固有の UI で
あって、これを用いると図式要素を簡単に選択可能だ。

Selecting and moving chart elements
======================================================================

Selecting chart elements
----------------------------------------------------------------------

編集モード中、マウスで図式中の要素をピックするのにはコツがいる。

Moving chart elements
----------------------------------------------------------------------

* 点やデータ系列を個別に移動させることは不可能だが、円グラフは例外で可能だ。
* 一部の要素は矢印キーで微小距離だけ移動させることが可能。
* 3D 図式要素を選択すると丸いハンドルが表示されることがある。角度を制御。さらに
  クリックすると、四角いハンドルになり、寸法や位置を制御。

Changing chart type
======================================================================

先述のように :menuselection:`F&ormat --> Chart T&ype...` を実行しろ。

Titles, subtitles, and axis names
======================================================================

* 図式の題名、副題、軸ラベルを設定するには :menuselection:`&Insert -->
  &Titles...` でダイアログを開く

Creating or changing text
----------------------------------------------------------------------

見出し、副見出し、軸名のテキストを変える方法はこれまで見てきたとおりだ。

図式作成時になかったものを作成したい場合には、

#. 編集モードに入って
#. :menuselection:`&Insert --> &Titles...` を実行し
#. :guilabel:`Titles` ダイアログボックスで対応する空欄を埋めて
#. :guilabel:`&OK` を押す。

Formatting text
----------------------------------------------------------------------

見出し、副見出し、軸名のテキストの書式設定手順：

#. 編集モードに入って
#. :menuselection:`F&ormat --> &Title -->` のいずれかのコマンドを実行
#. 開いたダイアログボックスで書式設定項目を指定
#. :guilabel:`&OK` を押す。

Legends
======================================================================

凡例が表示されると、データ系列名と棒、線、点などの視覚表現が表示される。回帰直線
と平均線がオンになっている場合は、凡例内にも表示される。

Positioning, inserting, or deleting legends
----------------------------------------------------------------------

* サイドバー :menuselection:`Elements --> Legend` 区画
* 図式編集モードメニュー :menuselection:`&Insert --> &Legend...`

Inserting or deleting only
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

編集モードに入って次のいずれかを実行しろ：

* :guilabel:`Formatting` ツールバー :guilabel:`Legend On/Off` ボタンを押す
* 図式右クリックメニュー :menuselection:`Insert &Legend` または
  :menuselection:`Delete &Legend` を実行

Positioning, inserting, and deleting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ダイアログボックスを使って凡例を配置し、挿入や削除を行う：

#. 編集モードに入る
#. :menuselection:`&Insert --> &Legend...`
#. :guilabel:`&Display Legend` オンオフ
#. オンの場合はラジオボタンの項目を選択する
#. :guilabel:`&OK`

より精密な配置には先述の数値入力ダイアログボックスを利用しろ。

Formatting legends
----------------------------------------------------------------------

#. 編集モードに入る
#. :menuselection:`F&ormat --> &Legend...`
#. :guilabel:`Legend` ダイアログボックスで項目指定
#. :guilabel:`&OK`

Formatting chart backgrounds
======================================================================

図式の背景は次の三つに分類される：

* chart area
* chart wall
* chart floor

これらに対する枠、領域、透明度オプションを設定する手順（領域の場合で記すが、残り
も同様）：

#. 編集モードに入る
#. :menuselection:`F&ormat --> Chart &Area...` を実行
#. :guilabel:`Borders`, :guilabel:`Area`, :guilabel:`Transparancy` 各タブから所
   望の設定を選択
#. :guilabel:`&OK`

Data range and series
======================================================================

データ範囲の定義と変更、二次 Y 軸へのデータ整列、データ系列の見てくれの書式設定
など。

Changing data ranges
----------------------------------------------------------------------

スプレッドシートで（データそのものではなく）データ範囲が変化した場合、その変更を
反映するように図式設定を変更しろ。

Replacing data by dragging
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

データセットを別のものに手動で置き換える方法：

#. マウスで新規データすべてを選択
#. データを図式上にドラッグ＆ドロップ
#. 開いた :guilabel:`Change Source Data Range` ダイアログボックスで最初の列また
   は行にラベルを含むかどうかを指定
#. :guilabel:`&OK`

Modifying the data range and data series
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. 編集モードに入る
#. :guilabel:`F&ormat --> Data Ranges...` 実行でダイアログボックスを開く
#. :guilabel:`Data Range` タブでデータ範囲を指定し直す
#. :guilabel:`Data Series` タブでデータ系列を指定し直す
#. :guilabel:`&OK`

Opening the Data Series dialog
----------------------------------------------------------------------

#. 編集モードに入る
#. 図式中のデータ系列をクリックするか、:guilabel:`Formatting` ツールバーの
   :guilabel:`Select Chart Element` ドロップダウンリストからデータ系列を選択する
#. :menuselection:`F&ormat --> Format &Selection...`

これで :guilabel:`Data Series` ダイアログボックスが開く。UI は図式種別によって変
わる。

Alignment, spacing, and plot options
----------------------------------------------------------------------

Aligning data to secondary Y axis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* データ単位や尺度が異なる場合には二次 Y 軸が使えることがある。
* 円グラフとネット図ではデータ系列を二次 Y 軸に揃えることは不可。

データ系列を二次 Y 軸に揃える手順：

#. 対象データ系列を :guilabel:`Data Series` ダイアログボックスで開く
#. :guilabel:`Options` タブで :guilabel:`Secondary Y axis` をオン
#. :guilabel:`&OK`

Spacing and plot options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Data Series` ダイアログボックス :guilabel:`Options` タブが含む図式種
別に応じた追加設定とは：

.. todo:: 後でやる

Area, transparency, and borders
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

スタイリング設定用タブは見ればわかるから割愛。

Lines, areas, and data point icons
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

折れ線図や散布図などでは :guilabel:`Options` と :guilabel:`Line` タブしかない。

.. admonition:: 利用者ノート

   折れ線プロットで点線や破線を使うのはおそらく悪手だ。見せられたものではない。

Assigning colors
----------------------------------------------------------------------

データ系列の表示色は次の三つの方法で指定する：

* 既定の配色を変更する
* :guilabel:`Data Series` ダイアログボックスを使用する
* データ範囲を使って枠線と塗りつぶしの色を設定する

Changing default color scheme
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

オプション設定 :menuselection:`Charts --> Default Colors` で各データ系列色を指定
する。ここでの設定色が以降に作成する図式の既定色を決定する。

Using Data Series dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

先述のように :guilabel:`Data Series` ダイアログボックスで線、領域、境界線に色を
割り当てる。

Using data ranges to assign colors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``COLOR`` 関数というものがあり、:guilabel:`Data Series` タブで境界線と塗りつぶし
色のデータ範囲に対して数値を割り当てる。

色を直接割り当てるというより、条件付き書式を使用して、特定の色を使用する際の基準
を定義するほうが色指定としての関数の使い方として自然か。

.. code:: text

   =IF(B2>100,COLOR(240,240,0,20),COLOR(150,0,150,20))

Formatting data points
----------------------------------------------------------------------

列や棒などの見てくれを調整するには :guilabel:`Data Point` ダイアログボックスを使
え。

#. 編集モードに入る
#. 対象データポイントをゆっくりと二度クリックする。四角いハンドルが示される。
#. :menuselection:`F&ormat --> Format &Selection...`
#. 所望オプションを適用
#. :guilabel:`&OK`

図式内のデータ点にマウスポインターがホバーすると、当該点番号、系列番号、データ点
の X 値と Y 値がツールチップで示される。

Axes
======================================================================

Add or remove axis labels
----------------------------------------------------------------------

値や区分の軸ラベルを追加削除するには :guilabel:`Axes` ダイアログボックスを用い
る。

#. 編集モードに入る
#. :menuselection:`&Insert --> &Axes...`
#. チェックボックスを操作
#. :guilabel:`&OK`

このダイアログボックスで Secondary 項目各種を選択すると、プロットの反対側に同一
内容のラベルが示される。これらに対して異なる単位や間隔を指定する方法は後述。

データ系列を二次 Y 軸揃えにすることも可能。

Edit and format axes
----------------------------------------------------------------------

:guilabel:`Axes` ダイアログボックスはより広範なオプションを有する。選択軸、図式
種別、2D/3D によってオプション集合が決まる。

#. 編集モードに入る
#. :menuselection:`F&ormat --> A&xis -->` のいずれかを実行
#. 適当なタブをクリックして必要な変更を行う
#. :guilabel:`&OK`

以下、各ページのオプション説明。

Defining scales
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Scale` タブでは一次軸に対して自動生成された尺度を修正したり、二次軸に
対して一次軸とは異なる尺度を与えたりする。このタブの内容も図式種別により変化す
る。

.. todo:: オプション

X 軸が期待通りに時間を表示しない場合は、:guilabel:`Scale` タブで最小時刻と最大時
刻を手動で入力すると問題が解決することがある。

Positioning axis, labels, and interval marks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Positioning` タブは軸ラベルと間隔印の位置を制御する。

.. todo:: オプション

Line tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Line` タブは :guilabel:`Data Series` ダイアログボックスのそれと同じ内
容だ。ただし :guilabel:`Icon` 区画がない。

Label tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Label` タブはラベル表示の切り替えと、ラベルが図式内に収まらない場合の
処理を指定する。

.. todo:: Options

Numbers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Numebrs` タブは軸で用いられる数値の属性を指定する。スプレッドシートで
の書式どおりでよい場合と、ここで独自に書式設定したものを採用したい場合がある。前
者ならば :guilabel:`So&urce format` をオンにする。

UI は Chapter 4 で習ったものと同様。

Font and Font effects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

こちらも Chapter 4 と同様。

Asian Typography
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

こちらも Chapter 4 と同様。

Hierarchical axis labels
----------------------------------------------------------------------

複数階層区分を図式軸に沿って階層的に表示することが可能。階層軸ラベルは初期指定が
適切ならば自動生成される。

.. admonition:: 利用者ノート

   本書の図表を再現して図式を Wizard で作成するといい。最上位階層に空白セルを置
   く必要があるのが気になる。

Data labels
======================================================================

データラベルは図式内のデータ点の側に情報を表示するものだ。詳細な情報を表示すると
きに特定のデータを強調するのに便利なものだ。

Adding and formatting data labels for a data series
----------------------------------------------------------------------

#. 編集モードに入る
#. データ系列を選択する（クリックか :guilabel:`Select Chart Element` ドロップダ
   ウンリスト）
#. 例えばメニュー :menuselection:`&Insert --> &Data Labels...` で
   :guilabel:`Data Labels` ダイアログボックスを開く
#. オプション（後述）を選択する
#. :guilabel:`&OK...`

:guilabel:`Data Labels` ダイアログボックスのほとんどのタブは既出のものと同じだ
が、:guilabel:`Data Labels` タブはこの機能専用のものだ。

:guilabel:`&Category` をオンにすると、冒頭の機能を実現できることがわかる。

Data labels for individual data point
----------------------------------------------------------------------

すべてのデータ点ではなく、特定のものにデータラベルを貼ることが適切なことがある。
乱雑さを抑え、重要なデータを強調したい。

Adding a single data label
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. 編集モードに入る
#. データ点をクリックし、もう一度ゆっくりクリックする
#. 右クリックメニュー :menuselection:`&Insert Single Data Label`

Formatting the label for a single data point
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

同じような操作で右クリックメニュー :menuselection:`Format &Single Data Label...`
を実行する。UI は前述のもの。

Removing data labels
----------------------------------------------------------------------

本節の操作は図式編集モードであることを必要とする。

Removing all data labels from a single data series
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

データ系列のどこかを右クリックして :menuselection:`Delete Data Label&s` を実行す
る。

Removing a data label from a single data point
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. 上述のようにデータ点をクリック
#. 右クリックメニュー :menuselection:`Delete Single Data &Label`

Removing all data labels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. データラベルやデータ系列が選択されていないことを確認
#. メニュー :menuselection:`&Insert --> &Data Labels`
#. ダイアログボックスで削除するデータラベルのオプションをすべてオフにする
#. :guilabel:`&OK`

Chart Data Tables
======================================================================

図式が表現する基礎データをその下に自動的に表形式で配置、表示するという機能だ。こ
の図表が図式 X 軸ラベルの代わりになる。網図と円グラフ以外で使用可能。

Inserting a chart data table
----------------------------------------------------------------------

#. 編集モードに入る
#. :menuselection:`&Insert --> Data Tabl&e...`
#. :guilabel:`Show data tabl&e...` をオン
#. :guilabel:`&OK`

Removing a chart data table
----------------------------------------------------------------------

:guilabel:`Show data tabl&e...` をオフにするか、図式内のデータ表右クリックメ
ニューから :menuselection:`Delete Data &Table` を実行。

Modifying the properties of a chart data table
----------------------------------------------------------------------

:guilabel:`Data Table` ダイアログボックスの説明。割愛。

データ表に対して :menuselection:`F&ormat --> Format &Selection...` を実行可能。

Grids
======================================================================

方眼紙の設定。軸に沿って区間を分割する。円グラフ以外で有効。

* 数字の付いた濃い線が太線。
* その間の薄い線が細線。

Adding/removing grid lines
----------------------------------------------------------------------

#. 編集モードに入る
#. :menuselection:`&Insert --> &Grids...`
#. :guilabel:`Major Grids` と :guilabel:`Minor Grids` の各オプションをオンまたは
   オフ
#. :guilabel:`&OK`

または :guilabel:`Formatting` ツールバーの :guilabel:`Horizontal Grids` または
:guilabel:`Vertical Grids` をオンオフ。

水平、垂直という言葉は図式種別によっては紛らわしいかもしれない。

Formatting grids
----------------------------------------------------------------------

関連ダイアログボックスがもう一つある：

#. 編集モードに入る
#. :menuselection:`F&ormat --> &Grid -->` 各種コマンド
#. 書式オプションを設定する
#. :guilabel:`&OK`

3D charts
======================================================================

.. admonition:: 利用者ノート

   本章最後に残す。

Setting 3D look
----------------------------------------------------------------------

Formatting 3D view
----------------------------------------------------------------------

Rotation and perspective
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Rotating 3D charts interactively
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Appearance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Illumination
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Trend and mean value lines
======================================================================

* Calc には、直線、対数、指数、累乗、多項式、移動平均など、回帰の種類が豊富に用
  意されている。
* 回帰線は円グラフ、網グラフ、泡グラフ、株価図を除くすべての 2D 図式に追加可能。
* 凡例には回帰線が自動的に含まれる。

回帰線が意味を持つ図式で利用するのが自然だ。

Adding and modifying trend lines
----------------------------------------------------------------------

回帰線は一度に一つのデータ系列に追加する。

#. 編集モードに入る
#. データ系列を選択する（先述）
#. :menuselection:`&Insert --> Tre&nd Line...` でダイアログボックスを開く
#. 回帰種別と必要なオプションを選択（後述）
#. :guilabel:`&OK`

Regression types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

横軸変数と縦軸変数に ``x`` と ``f(x)`` がそれぞれ既定で使われている。回帰線ダイ
アログの :guilabel:`X Variable Name` および :guilabel:`Y Variable Name` を変え
ろ。

関数の概形は :guilabel:`Moving Average` 以外ならば名前からわかる。

データ系列一つに対して複数の回帰線を追加することが可能。

Trend line options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Formatting trend lines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* 回帰線の色は最初に挿入されたときは対応するデータ系列と同じだ。
* 回帰線のスタイルを変更するには、:guilabel:`Trend Line` ダイアログボックスの
  :guilabel:`Line` タブを用いる。オプションは容易に理解可能。

Formatting trend line equations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Trend Line` ダイアログボックス :guilabel:`Type` タブで
:guilabel:`Show Equation` をオンにすれば図式内に回帰線方程式が示される。

.. todo::

   To format trend line eq.

Deleting trend lines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. 編集モードに入る
#. 回帰線をクリックして :kbd:`Del` キーを押すか、右クリックメニュー
   :menuselection:`Delete Tre&nd Line` を実行
#. :guilabel:`&OK`

Mean value lines
----------------------------------------------------------------------

平均値線は回帰線の特殊型だ。データ系列の平均値の水平線が図式内に引かれる。

Inserting mean value lines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

データ系列すべてに対して平均値線を引く手順：

#. 編集モードに入る
#. :menuselection:`&Insert --> Mean &Value Lines` 実行

単一データ系列に対して平均値線を引く手順：

#. 編集モードに入る
#. データ系列を一つ選択する（先述の方法による）
#. :menuselection:`&Insert --> Mean &Value Lines` か右クリックメニュー
   :menuselection:`Insert Mean &Value Line` 実行

Modifying mean value lines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

平均値線は作成時点では対応するデータ系列と同じ色だ。スタイル変更方法は：

#. 編集モードに入る
#. :guilabel:`Mean Value Line` ダイアログボックス開く。方法は：

   * 右クリックメニュー :menuselection:`&Format Mean Value Line...`
   * 平均値線をピックして :menuselection:`F&ormat --> Format &Selection...`

#. 所望の変更を与える
#. :guilabel:`&OK`

UI の意味は回帰線のものと同じだ。

Deleting mean value lines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. 編集モードに入る
#. データ系列を一つ選択する（先述の方法による）
#. :kbd:`Del` を押すか右クリックメニュー :menuselection:`Delete Mean &Value
   Line` 実行

Error bars
======================================================================

誤差棒は 2D 図式のみに作成できる。

Inserting error bars
----------------------------------------------------------------------

データ系列が選択されていない場合は、データ系列すべてに X または Y の誤差棒が挿入
される。

#. 編集モードに入る
#. :menuselection:`&Insert --> X &Error Bars` か :menuselection:`&Insert --> Y
   Error &Bars` を実行
#. ダイアログでオプション（後述）を指定
#. :guilabel:`&OK`

単一データ系列に対して誤差棒を示すには、それを選択状態にしてから上述の手順をとれ
ばいい。

Error Bars dialog options
----------------------------------------------------------------------

:guilabel:`Error Category` では選択肢を一つ選ぶ。

* :guilabel:`&None` は削除コマンド用項目（後述）
* :guilabel:`&Constant Value` は誤差を正負の定数で表示する。これらの値は
  :guilabel:`Parameters` 区画で指定する。
* :guilabel:`&Percentage` は誤差をデータ点に対する百分率で示す。これも
  :guilabel:`Parameters` 区画で指定する。
* ラジオボタンの第三項目はドロップダウンリストになっている。

  * :guilabel:`Standard Error`
  * :guilabel:`Standard Deviation`
  * :guilabel:`Variance`
  * :guilabel:`Error Margin` は :guilabel:`Parameters` 区画で指定する許容範囲を
    用いる。
* :guilabel:`Cell &Range` はあるセル範囲で定義された誤差値を用いる。セル範囲は
  :guilabel:`Parameters` 区画で指定する。
* :guilabel:`Error Indicator` では誤差の絵が正負両方を示すのか、どちらか一方しか
  示さないかを選択する。

Modifying error bars
----------------------------------------------------------------------

誤差棒の変更は一度に一系列だけ、:guilabel:`Error Bars` ダイアログボックスで行う。

#. 編集モードに入る
#. データ系列を選択（先述）して :menuselection:`F&ormat --> Format &Selection...`
#. 所望の選択肢を指定
#. :guilabel:`&OK`

Deleting error bars
----------------------------------------------------------------------

データ系列すべてに対しての誤差棒一括削除手順：

#. 編集モードに入る
#. どのデータ系列選択されていないようにする
#. :menuselection:`&Insert --> X Error &Bars` か :menuselection:`&Insert --> Y
   Error &Bars` を実行してダイアログボックスを開く
#. :guilabel:`&None` を選択
#. :guilabel:`&OK`

単一データ系列に対する誤差棒削除は右クリックメニュー :menuselection:`Delete X
Error &Bars` か :menuselection:`Delete Y Error &Bars` を実行

Adding drawing objects to charts
======================================================================

:guilabel:`Drawing` ツールバーの記述。Chapter 6 を読めばいい。

図式に図面オブジェクトを配置するには、編集モードであることが必要。そうしないと、
図面オブジェクトが図式ではなくシートの方にリンクする。

Resizing, moving, and positioning charts
======================================================================

図式の幾何を変更するには、まずは選択モードでそれをクリックする。次にマウスやキー
ボードを使って操作するか、専用ダイアログボックスで変更を指示する。求められる精度
によって使い分けたり併用したりするのが良い。

Changing interactively
----------------------------------------------------------------------

Resizing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. 図式をクリックして正方形ハンドルを境界に現す。
#. ハンドルのいずれかをドラッグする。

   * マウスポインターは図式寸法を拡縮する方向を示す。
   * 角のハンドルをドラッグすると縦横比が維持される。
#. 図式の外側をクリックして選択モードから脱する。

Moving
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

移動量に応じた手順がある。微小距離の移動方法は：

#. 図式をクリックして正方形ハンドルを境界に現す。
#. 矢印キーを押して一度に二、三ドット動かす。:kbd:`Alt` キーを押しながら矢印キー
   を押せば一度に一ドット動かす。
#. 図式の外側をクリックして選択モードから脱する。

一気に動すにはキーボードの代わりにマウスでドラッグ＆ドロップする。

Position and Size dialog
----------------------------------------------------------------------

#. 図式右クリックメニュー :menuselection:`Position and Si&ze...` を実行
#. :guilabel:`Position and Size` ダイアログボックスのタブを一つ選択して選択肢を
   指定
#. :guilabel:`&OK`

幾何変更時は図式の幾何の固定に使用する点に対応する :guilabel:`&Base point` ラジ
オボタンのいずれかをクリックしろ。

幾何のいずれかを :guilabel:`Protect` 区画の適切なチェックボックスをオンにして不
意の変更から保護することが可能。採用した選択肢はダイアログボックスを閉じた後も有
効だ。ダイアログボックスを閉じた後、基点は既定位置にリセットされる。

Position and Size
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Position` と :guilabel:`Size` 各区画はこれまでの記述で理解しろ。
:guilabel:`Protect` 区画についてはすぐ上で述べられている。:guilabel:`Adapt` 区画
は無視しろ。

Rotation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

さっきもそうだったかもしれないが :guilabel:`Pivot Point` 区画のスピンボックス二
つとラジオボタンが中途半端に連動している？

Slant & Corner Radius
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Corner Radius` と :guilabel:`Control Point 1` などは無視しろ。

:guilabel:`Slant` は軸に沿って図式を傾ける。その軸の角度を -89 から 90 の範囲で
指定する。

Selecting multiple charts
======================================================================

複数の図式を選択するには、:kbd:`Shift` キーを押しながらクリックしていけばいい。
すると、図式全部をカバーする位置に操作ハンドルが描画される。これにより、選択図式
が一体化したかのように操作可能。有効な操作は：

* :menuselection:`&Edit --> &Cut` と :menuselection:`&Edit --> &Paste`
* :guilabel:`Position and Size` ダイアログボックス使用
* :guilabel:`Drawing Object Properties` ツールバー使用

Changing overall appearance of charts
----------------------------------------------------------------------

Chapter 6 と *Draw Guide* を参照。

Copying, exporting, and deleting charts
======================================================================

Copying charts in the same spreadsheet document
----------------------------------------------------------------------

コピー図式に対しても原データに加えられた変更が反映される。

Copying to another LibreOffice document
----------------------------------------------------------------------

図式をコピーして別の LibreOffice 文書に貼り付けると、原データとのリンクが失われ
る。データは図式とともに保持され、データ範囲ではなくデータ表と呼ばれる。

Chapter 11 も参照。

Keeping original data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

元のデータを図式に使用することを目的とする場合は、普通に上記と同じ手順で図式をコ
ピーし別の文書に貼り付ける。

Modifying original data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

反対に、元データを修正する場合は次のようにする：

#. 編集モードに入る
#. 図式右クリックメニュー :menuselection:`&Data Table...` を実行
#. 開いたダイアログボックスでデータを編集する。
#. :guilabel:`&Close`

.. admonition:: 利用者ノート

   試すときは Calc 以外の、例えば Writer の新規文書に貼り付けて編集を試みると印
   象が強くて良い。

Dragging replacement data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

図式が Calc にあるままで、置換データが同一スプレッドシートにある場合は、新しい
データを選択し図式上にドラッグする。

Exporting chart images
----------------------------------------------------------------------

LibreOffice 以外のアプリケーションでも使えるように、図式をよく使う画像形式でエク
スポート可能だ。

#. 右クリックメニュー :menuselection:`Export as &Image`
#. 保存ダイアログボックスで :guilabel:`ファイルの種類 (&T)` を選択して保存先パス
   を指定
#. :guilabel:`保存 (&S)`

Deleting charts
----------------------------------------------------------------------

図式を選択して枠にハンドルが示されたら :kbd:`Del` を押せ。

Gallery of chart types
======================================================================

どの図式型を採用するかはメッセージに集中しろとある。

Column charts
----------------------------------------------------------------------

* 棒の高さは値に比例する。
* X 軸と Y 軸は区分と値をそれぞれ現す。
* 経時的な傾向を示すデータを説明するのに用いられる。
* 比較的少数のデータ点に向いている。

  * より大きな時系列には line chart がより適切と考えられる。

Bar charts
----------------------------------------------------------------------

* 棒を横に表示するのが column chart との違い。他の図式とは異なり Y 軸が水平だ。
* 時間が重要な要素でないときに使いやすい。
* 区分名が長かったり、区分が多い場合には column chart よりも好まれることがある。

Pie charts
----------------------------------------------------------------------

* 各値を同一円に収まる扇形として示し、各扇形の面積が値に比例するという図式だ。
* 部門別の支出を比較するなど、比率を比較するのに適した図式だ。
* データ区分が少ない場合に効果的な図式だ。
* ドーナツ型は二組の関連情報を表現するのに使われる。内周がどうしても小さくなるの
  でデータによっては注意が要る。

Area charts
----------------------------------------------------------------------

* ある区分から次の区分への変化の量を強調するのに使いたい図式。
* 折れ線プロットよりも視覚的印象を強く与える。

Normal area charts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Normal ではこういう見てくれの図式であるので、透明度の値を指定して使い物になる。
データが重なり合うので、最初のデータ系列の背面にデータの一部が欠けるようなことが
起こる。

Stacked area charts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* データ系列の各点を他のデータ系列に加え、合計面積を表現するような変種と、
* 系列の各値を全体に対する百分率で表現する

変種がある。

Line charts
----------------------------------------------------------------------

* 連続性を強調したいときに傾向、経時変化を示すのに使える。
* 値は Y 軸上の点に、X 軸は区分（多くの場合は時系列）を示す。
* 各データ系列の Y 値は線で結ぶことがある。

:guilabel:`&Stack series` をオンにすると、Y 値の累積値が互いの上に示される。

:guilabel:`Line type` ドロップダウンリストではデータ点の接続様式を指定する。面白
いのは :guilabel:`Smooth` だ。ダイアログが開いて補間方式を次から指定する：

* :guilabel:`Cubic spline`
* :guilabel:`B-spline`

線スタイルで 3D にすると読者を惑わせるかもしれないので、単に線を太くしろ。

Scatter or XY charts
----------------------------------------------------------------------

両軸に値を含む図式で、特に精密かつ複雑なデータ同士の関係を理解するのに有用だ。
量的変数間の統計的関連を調べるのに使われがちだ。複数データ系列を含められる。

慣例上、変数の一つが試験者によって制御されるか、変化に一貫性がある（時間変化な
ど）場合、それを独立変数とみなして X 軸にプロットする。

XY chart variants
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* :guilabel:`Points Only`: データ点のみを示す（記号で点を表現）
* :guilabel:`Points and Lines`: データ点と折れ線を両方示す。
* :guilabel:`Lines Only`: データ点同士の間の折れ線のみ示す。描画順序に注意。
* :guilabel:`3D Lines`: 線のみれくれが帯のようになる。データ点描画なし。

:guilabel:`&Sort by X values` で X 値の順序に線を描くように指定可能。データ系列が
元データでバラバラのときに使える。

:guilabel:`Line type` は先述のものと同じ（はず）。

Examples of XY or scatter charts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

実習節。データ系列を行にとって月名ヘッダーを無視すればいい。

.. code:: text

   Apr	May	Jun	Jul	Aug	Sep	Oct	Nov
   Yen	102	105	178	165	122	98	134	97
   Dollar	56	57	67	90	64	56	78	34
   Rupee	209	230	256	231	201	199	230	223
   Yuan	69	78	75	76	69	95	69	70

Bubble charts
----------------------------------------------------------------------

泡図は三変数を二次元で表現できる散布図の変種だ。

* データ点を泡で表現する。
* 変数二つは X 軸と Y 軸に沿ってプロットされ、第三変数は泡の相対的な大きさで表現
  される。
* データ系列はいくつでも含められる。

泡図は金融データや社会的人口統計学的データを表現するのによく使われる。

バブル・チャートのデータ系列ダイアログには、
バブルの大きさを決定するデータ範囲を定義する項目がある。 チャート・ウィザードの
データ系列ページで、バブル・チャートを手動で作成する必要があるかもしれない。

Net charts
----------------------------------------------------------------------

* データ値を放射状の輻上の点として表示し、各輻（他の図式の Y 軸相当）が変数を表
  す。
* 時系列ではないが、科学実験の変数のように異なる状況を示すデータを比較する。特に
  群れや外れ値を表示するのに便利だ。
* 一般に、三軸から八軸の間が最善で、それを超えると図式が混乱する。
* この図式で見える面積に惑わされてはいけない。

Stock charts
----------------------------------------------------------------------

株価図は、始値、終値、底値、上値、終値を表示することで、株価や株式の市場動向を示
す。取引量も表示でき、X 軸は通常時系列を表す。

Chart Wizard で株価図を設定する場合、データ配置が所定のものである必要がある。ど
の列を株価の始値、安値、高値、終値、取引高とするかを指定する。別途、手動での調整
が必要な場合もある。

.. admonition:: 利用者ノート

   個人的に利用することがない図式だから、作成オプションの細かい点は割愛。

Stock chart variants
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. todo::

   図式の読み方は知りたいから割愛しない。

Column and line charts
----------------------------------------------------------------------

経時的な売上高（柱）と利益率の回帰（折れ線）のような、異なるが関連するデータ系列
二つを表示するのに使える。医療検査や品質管理で使用されるような、一定の最小線と最
大線を表示することも可能。

:guilabel:`Chart Type` ダイアログボックスで線の本数を指定する。データの最初の列
または行が区分で、データの最後の列または行が線になる。

* :guilabel:`Columns and Lines` は柱を並べて描き、それぞれの値を簡単に比較できる
  ようにする。
* :guilabel:`Stacked Columns and Lines` では柱を互いに上に積み重ね、柱一つの高さ
  はデータ値の合計を示す。
* 柱と線の色を一致させるように書式設定しろ。
* 二次 Y 軸を使え。

Pivot charts
----------------------------------------------------------------------

ピボット表に対して :menuselection:`&Insert --> &Chart...` で作成される図式だ。こ
の図式は本章で記述されている他の図式の多くの性質があるものの、固有の性質も有す
る。Chapter 9 参照。

Create box plots with whiskers in Calc
======================================================================

箱ヒゲ図を手動で作図する手順が記述されている：データ系列を行に並べ、凡例のない
stacked column 図の最小値、第一四分位値、中央値、第三四分位値、最大値を、箱ヒゲ
図に変換することで表現する。

第一四分位値と第三四分位値の差を計算する場合、データ系列が偶数データ量か奇数デー
タ量かが急所だ。データ量が偶数、奇数の場合は関数 ``QUARTILE.EXC``,
``QUARTILE.INC`` をそれぞれ用いる。

``MIN``, ``MEDIAN``, ``MAX`` 各関数を最小値、中央値、最大値をそれぞれ計算するた
めに使用可能。

Converting the column chart to box plot
----------------------------------------------------------------------

箱ヒゲ図を stacked column 図から手動で変換作図する手順：

.. todo::

   実習終了後に記載

`How to create boxplot with whiskers - The Document Foundation Wiki
<https://wiki.documentfoundation.org/Documentation/HowTo/Calc/BoxplotWithWhiskers>`__
参照。

Sparklines
======================================================================

   Sparklines are small, simple, cell-sized charts that convey the general shape
   of data variation within a dataset.

* 経時変化を示すために用いられ、軸や座標抜きで描かれるのが通常だ。
* MS Excel の閃光線と互換性がある。

Creating a sparkline
----------------------------------------------------------------------

閃光線を作成する手順：

#. 原データ行または列を選択
#. :menuselection:`&Insert --> Spark&line...` を実行して
   :guilabel:`Sparkline Properties` ダイアログボックスを開く
#. :guilabel:`Output range` 欄に出力先セルを指定
#. オプションを適宜埋める
#. :guilabel:`&OK...`

ダイアログボックスの入力欄：

.. todo::

   TBW

* 閃光線は一セルに限られる。
* 閃光線の寸法を大きくするには、それを含むセルの寸法を大きくする。

Types of sparkline
----------------------------------------------------------------------

閃光線の種類は三つ：

* Line: データ値を接続する折れ線
* Column: 各データ値を現す縦棒
* Stacked: 正または負の値に対して、上または下に等しい大きさの縦棒

Creating multiple sparklines
----------------------------------------------------------------------

一度に複数の閃光線を作成する方法がある：

#. 原データの複数行や複数列を選択
#. メニュー :menuselection:`&Insert --> Spark&line`
#. :guilabel:`&Input range` の行または列と同じ数のセルを :guilabel:`Output
   &range` に選択
#. ダイアログボックスでオプション値を設定
#. :guilabel:`&OK`

新規閃光線は入力範囲と同じ順序で出力範囲に描画される。これらはグループを形成す
る。

:guilabel:`&Vertical minimum` または :guilabel:`Vertical maxim&um` を
:guilabel:`Group` に設定すると、関連する各閃光線の Y 軸は、閃光線すべてのデータ
からの最小値または最大値を含むように拡大される。

Modifying a sparkline
----------------------------------------------------------------------

Updating a sparkline's data range
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. 閃光線右クリックメニュー :menuselection:`Spar&klines --> Edi&t Sparkline...`
#. :guilabel:`Sparkline Data Range` ダイアログボックス :guilabel:`&Data range`
   を更新する
#. :guilabel:`&OK`

Updating a sparkline's formatting properties
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

閃光線の書式設定を更新する手順：

#. 閃光線右クリックメニュー :menuselection:`Spar&klines --> &Sparkline...`
#. :guilabel:`Sparkline Properties` ダイアログボックスで必要に応じてオプションを
   変更する
#. :guilabel:`&OK`

Sparkline groups
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

閃光線はセル一つに対して定義されるものだが、複数の閃光線をグループにまとめること
が可能だ。

* 閃光線グループは描画書式を共有するものだ。
* 複数の閃光線が一度に作成されると、それらはまず同じ閃光線グループを共有する。
  このグループの描画書式を変更すると、所属する閃光線すべてに影響する。
* 閃光線を選択すると、同じグループ内の閃光線すべてが強調表示される。

Modifying the formatting properties of a sparkline group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

閃光線グループの描画書式を更新する手順：

#. グループ内の閃光線一つから右クリックメニュー :menuselection:`Spar&klines -->
   &Edit Sparkline Group...`
#. :guilabel:`Sparkline Properties` ダイアログボックスで必要に応じてオプションを
   変更する
#. :guilabel:`&OK`

Grouping and ungrouping sparklines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

グループ化手順：

#. 所望の書式を有する閃光線をまず選択
#. それ以外の閃光線を追加的に選択
#. 右クリックメニュー :menuselection:`Spar&klines --> Gr&oup Sparklines`

閃光線をグループから外し、個別に書式設定可能にするには、対象閃光線を選択し、以下
のいずれかを実行：

* 右クリックメニュー :menuselection:`Spar&klines --> &Ungroup Sparklines`
* メニュー :menuselection:`F&ormat --> Spar&klines --> &Ungroup Sparklines`

Deleting sparklines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

単一閃光線を削除するには、それを選択して次のいずれかを実行：

* :kbd:`Del` を押す
* 右クリックメニュー :menuselection:`Spar&klines --> &Delete Sparkline`
* メニュー :menuselection:`F&ormat --> Spar&klines --> &Delete Sparkline`

グループ内の閃光線すべてを削除するには、まず閃光線一つを選択して次のいずれかを実
行：

* 右クリックメニュー :menuselection:`Spar&klines --> Delete &Sparkline Group`
* メニュー :menuselection:`F&ormat --> Spar&klines --> Delete Sparkline &Group`
