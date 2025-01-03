======================================================================
Calc Guide Chapter 9, Using Pivot Tables ノート
======================================================================

.. include:: ./calc-inc.txt

.. contents:: 章見出し
   :depth: 3
   :local:

Introduction
======================================================================

ピボットテーブルは、大量のデータを簡単に組み合わせ、比較、分析、要約するための
ツールだ。これを使用すると、ソースデータのさまざまな概要や関心分野の詳細を表示し
たり、報告書を作成したりできる。

Database preconditions
----------------------------------------------------------------------

ピボットテーブルで作業するには、行と列で構成される、データベースのテーブルに似た
生データの一覧が必要だ。フィールド名は一覧の最初の行だ。

データ給源は外部ファイルまたはデータベースだ。最も単純な例として、データが Calc
スプレッドシートで与えられている、並べ替え機能を単に使えば済むことがある。

リスト形式のデータを処理するために、Calc はスプレッドシートのどこにリストがある
かを知る必要がある。リストはシート内のどの位置にあってもかまわない。スプレッド
シートには関連性のないリストを複数含めることができる。

Calc はリストを自動的に認識する。次のロジックを使用する：選択した升目を起点に、
周囲のセル上下左右すべてを調べる。空の行または列を検出した場合、またはスプレッド
シートの左または上の境界に当たった場合、リスト境界を認識する。つまり、リストに空
の行や列がない場合にのみ、説明した関数が正しく動作する。

.. tip::

   Calc がリストを自動的に正しく認識させるため、リスト内に空の行や空の列がないこ
   とを確認しろ。

ピボットテーブルを作成する前にセルを複数選択した場合、上述の自動認識ロジックは適
用されない。その代わりに、Calc は選択セルをそのまま使用してピボットテーブルを作
成するとみなす。

.. tip::

   ピボットテーブルの作成を開始する前に、必ず升目を一つだけ選択しろ。これによ
   り、Calc はデータリストの全範囲を自動的に判断する。

比較的よくある誤りの原因は、リストを誤って宣言してしまい、それを並び替えてしまう
ことだ。升目を複数選択した場合、例えば列全体を選択した場合、並び替えによって一行
にまとまるべきデータが混ざり合ってしまう。

このような形式的な側面に加えて、リストの論理構造もとても重要だ。

.. note::

   Calc リストは正規形、つまり単純な線形構造を持たなければならない。

データを入力するときは、アウトライン、グループ、概略を追加しない。以下は、経験の
浅い表計算使用者がよく犯す間違いだ：

* 例えば、記事のグループごとにシートを設ける。こうしてしまうと、分析が各グループ
  内でしか不可能だ。
* 売上一覧で金額の列を一つしか作らず、各従業員の金額の列を作成したとする。この場
  合、さまざまな列のデータをグループ化することは困難だ。したがって、ピボットテー
  ブルを使用した分析は不可能だ。ピボットテーブルで分析するにはデータがすべて同じ
  列に入力されている必要がある
* 金額を時系列順に入力し、各月末に合計を作成したとする。この場合、ピボットテーブ
  ルは合計を他の値と同等に扱うため、異なる基準でリストを並べ替えることは不可能だ。
  月次結果の取得は高速で簡単なピボットテーブル機能の一つだ。

Data sources
----------------------------------------------------------------------

ピボットテーブルのデータ給源としては、Calc スプレッドシートまたは LibreOffice
に登録されている外部データソースが考えられる。

Calc spreadsheet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Calc スプレッドシートでリストを分析するのは、最も単純でよく使われる用例だ。リス
トは定期的に更新されたり、他のアプリケーションからデータをインポートしたりする。

リストデータはスプレッドシートに直接入力することも、別のファイルやアプリケーショ
ンからコピーすることもある。また、Web Page Query の入力フィルターを使用し
て、|HTML| ファイル、|CSV| ファイル、Calc スプレッドシート、Microsoft Excel スプ
レッドシートからデータをはめ込むことも可能だ。詳細については |Calc11| を参照し
ろ。

別のアプリケーションからデータを挿入する際の Calc の動作はデータの形式によって異
なる。データが一般的なスプレッドシート形式の場合、直接コピーされる。このダイアロ
グボックスの詳細については |Calc01| を見ろ。

Registered data source
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

登録済みデータ給源とは LibreOffice 以外のデータベースに保存されているデータへの
接続だ。これを使用する場合、分析対象のデータはスプレッドシートに保存されない。
Calc では LibreOffice Base で作成および管理されているデータベース以外にも、
さまざまなデータ給源を使用可能だ。|Calc11| を見ろ。

Using shortcuts
----------------------------------------------------------------------

Calc でピボットテーブルを頻繁に使用する場合、組み込みメニューの頻繁な使用に不便
を感じる。組み込みキーバインドがすでに与えられている場合がある。例として、選択
データ範囲をグループ化する :kbd:`F12` がある。その他の場合、組み込みのツールバー
にはすでに関連する図像が用意されていることがある。例えば、|StandardToolbar| にお
ける :guilabel:`Insert or Edit Pivot Table` 図像だ。

組み込みのキーバインドやツールバーを使用するだけでなく、独自に定義することもでき
る。|Calc15| を見ろ。

Creating a pivot table
----------------------------------------------------------------------

Calc に生データリストの全範囲を自動的に決定させたい場合は、このリスト内の升目を
一つ選択する。明示的に定義したい場合は、関連する升目すべてを選択する。

ピボットテーブルを作成するコマンドは次のいずれか：

* セルが選択されている状態で、|MenuBar| の :menuselection:`&Insert-->Pi&vot
  Table...` を実行
* :menuselection:`&Data-->&Pivot Table-->&Insert or Edit...` を実行
* |StandardToolbar| の :guilabel:`Insert or Edit Pivot Table` 図像を押す

|SelectSourceDlg| が表示され、選択したデータ升目、名前がすでに設定されている升目
範囲、または LibreOffice に登録済みのデータ給源のいずれかを使用するか選択でき
る。

.. note::

   名前付き範囲の詳細については |Calc14| を、登録データ給源へのリンクの詳細につ
   いては |Calc11| を見ろ。

|SelectSourceDlg| で |OK| を押すと |PivotTableLayoutDlg| が表示される。

The Pivot Table Layout dialog
======================================================================

ピボットテーブルの機能は |PivotTableLayoutDlg| とスプレッドシートでの結果の操作
を通じて管理する。当節では前者について見ていく。

.. tip::

   ピボットテーブルの初期作成後に |PivotTableLayoutDlg| を再度表示するには、ピ
   ボットテーブルの任意の升目をクリックしてから上述のピボットテーブル作成手順と
   同じことをするか、ピボットテーブルの任意の升目を右クリックしてコンテキストメ
   ニューから |PropertiesC| を選択する。

Basic layout
----------------------------------------------------------------------

|PivotTableLayoutDlg| にはピボットテーブルの間取りを示す領域が四つある：

* |Filters|
* |ColumnFields|
* |RowFields|
* |DataFields|

これらのほかに、原データリストのフィールド名を含む |AvailableFields| がある。間
取りを選択するには、|AvailableFields| から他の四領域にフィールドをドラッグ＆ド
ロップする。

|DataFields| には最低一つはフィールドが必要だ。上級者はここにフィールドを複数使
用する。当欄には、例えば `SUM` などの集計関数が使用される。

|RowFields| と |ColumnFields| は結果がどのグループからソートされるかを示す。多く
の場合、行または列の小計を得るために、一度に複数のフィールドが使用される。フィー
ルドの順序は、全体的なものから特定のものへの合計の順序を与える。

例えば、`Region` と `Employee` を |RowFields| エリアにドラッグすると
合計が地域に分割される。地域内にはさまざまな従業員の一覧が表示される。

|Filters| に配置されたフィールドは、ドロップダウンリストとして結果のピボットテー
ブルの上部に表示される。結果の概要では選択したベースデータの一部しかみが考慮され
ない。例えば、|Filters| に `Employee` を含めると、従業員ごとに表示される結果を絞
り込み処理できる。

フィールドを四領域から削除する場合、項目をドラッグ＆ドラップで |AvailableFields|
に戻す。

.. tip::

   選択したフィールドを |PivotTableLayoutDlg| のある領域から別の領域に素早く移動
   するには、|Alt| を押しながら、対象領域のラベルの下線付きの文字に対応するキー
   を押す。

.. note::

   既定では、Calc は |ColumnFields| に `Data` を入れる。`Data` は必要に応じて
   |ColumnFields| と |RowFields| 領域の間で移動できる。`Data` はその領域のフィー
   ルドリスト内での位置によっては、ピボットテーブルの結果に `Data` というラベル
   のボタンが表示され、結果の間取りに影響を与えることがある。この機能を使用しな
   い場合は `Data` をその領域のフィールドリストの最後に配置しろ。

.. admonition:: 読者ノート

   |ColumnFields| に最初から入っている `Data` は使うつもりがなくても、自分で追加
   した項目の下に移動させておけ。

More Options
----------------------------------------------------------------------

|PivotTableLayoutDlg| を展開して、さらにオプションを表示するには、
:guilabel:`O&ptions` および :guilabel:`Source and Destination` ラベルに隣接する
プラス記号をクリックする。

ダイアログの :guilabel:`O&ptions` をクリックするとチェックボックスが複数現れる。
好みで。

ダイアログの :guilabel:`Source and Destination` をクリックすると、ピボットテーブ
ルの入出力場所を編集可能な入力欄が現れる。これを使えば新シートに表を生成しないよ
うにできる。

.. rubric:: Options

:guilabel:`&Ignore empty rows`
   原データが推奨形式でない場合、ピボットテーブルに空行を無視させる。
:guilabel:`Identif&y categories`
   原データにリスト内の項目がなく、推奨されるデータ構造を満たしていない場合、ピ
   ボットテーブルはその上に一覧された区分にそれを追加する。オフにするとピボット
   テーブルは `(empty)` を入れる。

   オフにすると、ピボットテーブルには区分 `(empty)` が表示される。

   論理的には、オンの場合の動作の方が優れている。空項目が表示されるリストは並べ
   替えや絞り込みなどの機能が使用できないため、有用性が低い。
:guilabel:`Total colum&ns`, :guilabel:`Total ro&ws`
   これらのオプションを使用すると、ピボットテーブルに各列の合計を表示する行を追
   加するか、各行の合計を表示する列を右端に追加するかを決定できる。項目が累積さ
   れている場合や比較の結果である場合など、無意味であることもある。
:guilabel:`Add fi&lter`
   ピボットテーブルの結果の上に `Filter` というラベルの付いた升目を追加するかど
   うかを指定する。これにより、ピボットテーブル内に追加の絞り込みオプションが追
   加される。:ref:`calc09-anchor-filtering` を見ろ。

   .. note::

      このオプションによる絞り込みと、|PivotTableLayoutDlg| の |Filters| に
      フィールドを含めることで搭載される絞り込みとは独立している。

:guilabel:`&Enable drill to details`
   合計列または合計行から生成された升目を含め、ピボットテーブルの結果のデータセ
   ル一つをダブルクリックすると、新しいシートが開き、個々の項目の詳細な一覧が表
   示される。行または列フィールド領域の升目をダブルクリックする
   と、:guilabel:`Show Detail` ダイアログが開く。この機能がオフである場合、ダブ
   ルクリックはスプレッドシート内での通常の編集機能を維持する。詳細については
   :ref:`calc09-anchor-drilling` でやる。

.. rubric:: Destination

:guilabel:`Source`
   この領域の :guilabel:`Selection` フィールドには、シート名と、ピボットテーブル
   の原データを含む升目範囲が表示される。原スプレッドシートに名前付き範囲がある
   場合は :guilabel:`Named ran&ge` オプションで選択できる。
:guilabel:`Destination`
   この領域のコントロールは結果を表示する場所を定義する。

   :guilabel:`New sheet` を選択すると、スプレッドシートファイルに新規シートが追
   加され、そこに結果が配置される。新規シートには :samp:`Pivot
   Table_sheetname_{X}` という形式で名前が付けられる。ここで `X` には作成された
   表の番号が入る。`Sales List` という名前のシートの場合を例に挙げると、最初に作
   成されるピボットテーブルの新規シートの名前は `Pivot Table_Sales List_1` だ。
   各新規シートは給源シートの隣に加わる。

   対象スプレッドシートに名前付き範囲がある場合は :guilabel:`Named range` オプ
   ションで選択できる。

   この領域の :guilabel:`Selection` フィールドには、シート名とピボットテーブルの
   結果の升目範囲が表示される。

.. tip::

   ピボットテーブルを原データと同じシートに表示するには、:guilabel:`Destination`
   領域の :guilabel:`Selection` をオンにし、右側にある Shrink ボタンを押し、シー
   トの空の領域の適切な升目をクリックして Expand ボタンを押し、
   |PivotTableLayoutDlg| の |OK| を押す。

More settings for the fields: Field options
----------------------------------------------------------------------

前節のオプションはピボットテーブル全般に有効だ。また、ピボットテーブル間取りに現
在含まれているフィールドの設定も変更できる。フィールドの設定を変更するに
は、|PivotTableLayoutDlg| の |Filters|, |ColumnFields|, |RowFields|,
|DataFields| のいずれかでそのフィールドをダブルクリックする。|AvailableFields|
のフィールドをダブルクリックしても効果はない。|DataFields| のフィールドで使用で
きるオプションは、他の三領域のフィールドで使用できるそれとは異なる。

Options for data fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* |DataFields| 欄とそれ以外でダイアログの内容が若干異なる。
* :guilabel:`Subtotals` をオンにして小計を表示させることも可能。試すときにはマ
  ニュアルのように行フィールドを二つ以上指定するとわかりやすい。

ダイアログの :guilabel:`&Options...` ボタンで開くダイアログボックスで、さらなる
表示周りの項目を指定可能。

* :guilabel:`Compact Layout` オプションが魅力的だが、日付の書式が保存されないよ
  うで困る。

|PivotTableLayoutDlg| の |DataFields| ある対象フィールドをダブルクリックすると
|DataFieldDlg| が開く。

|DataFieldDlg| では集計関数を選択可能だ。`Sum` 関数などを使用することがよくある。
標準偏差や勘定関数などの他の関数も使用可能。例えば、勘定関数は数値以外のデータ
フィールドに便利だ。

.. |ShowItemsWithoutData| replace:: :guilabel:`Show it&ems without data`

空の列や行を結果表に含めるには |ShowItemsWithoutData| をオンにする。

.. |DisplayedValue| replace:: :guilabel:`&Displayed Value` 区画

ダイアログの |DisplayedValue| を展開するにはプラス記号をクリックする。

|DisplayedValue| では集計機能を使用した分析に関する他の可能性を選択可能だ。
:guilabel:`&Type` の設定によっては :guilabel:`&Base field` と :guilabel:`Ba&se
item` の定義を選択する必要がある。

.. todo:: 余裕があれば Table 1 をまとめろ。

Options for row and column fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|PivotTableLayoutDlg| の |RowFields| または |ColumnFields| でフィールドをダブル
クリックすると、|DataFieldDlg| が表示される。

.. admonition:: 読者ノート

   |DataFields| のダブルクリックのときとは構成が異なる。

各区分の小計を表示するかどうかを選択可能だ。既定では活動していない。小計が有用で
あるのは、ある行または列フィールドの値が、別の（サブ）フィールドの小計に分割可能
である場合に限る。

データフィールド（前述）にも使用できる小計を計算するには、|DataFieldDlg|
:guilabel:`Subtotals` 区画で :guilabel:`&Automatic` を選択する。

.. |UserDef| replace:: :guilabel:`&User-defined`

使用する小計の型を選択するには |UserDef| を選択し、計算したい小計の型を一覧から
クリックする。この一覧にある関数は |UserDef| が選択されている場合に限り使用可と
なる。

通常、基となるデータベースに項目がない区分の行や列はピボットテーブル上では見えな
い。|ShowItemsWithoutData| をオンにすると、これらを強制的に表示できる。

|DataFieldDlg| の :guilabel:`&Options...` ボタンを押して |DataFieldOptionsDlg|
にアクセスする。これを使用して |PivotTableLayoutDlg| の|ColumnFields| と
|RowFields| のフィールドに対する追加オプションを指定する。

用意されている選択肢は次のとおり：

.. _calc09-anchor-sort-by:

:guilabel:`Sort by`
   列または行を並べ替えたいデータフィールドを指定する。

   * :guilabel:`&Ascending` は最小値から最大値へ昇順に並び替わる。対象フィールド
     がダイアログを開いたフィールドである場合、項目は名前順に並べ替わる。データ
     フィールドが選択された場合は、項目は選択されたデータフィールドの結果値で並
     び替わる。
   * :guilabel:`&Descending` はその降順版。
   * :guilabel:`&Manual` は値が辞書式配列に並べ替わる。
:guilabel:`Display Options`
   例外的でない行を除いた、すべての行フィールドの表示オプションを指定可
   能。Layout ドロップダウンリストから、リストボックス内のフィールドの間取りモー
   ドを選択する。ピボットテーブルの各項目のデータの後に空行を追加するには
   :guilabel:`&Empty line after each item`を選択する。:guilabel:`&Repeat item
   labels` を必要に応じてオンまたはオフにする。

   :guilabel:`&Layout` ドロップダウンリストには間取りモードオプションが四つあ
   る。要求に最も適した間取りを選択しろ：

   * `Tabular layout`
   * `Outline layout with subtotals at the top`
   * `Outline layout with subtotals at the bottom`
   * `Compact layout`
:guilabel:`Show Automatically`
   指定したフィールドで並び替えるときに、上位または下位何個の項目を表示するかを
   与える。:guilabel:`&Show` をオンにして自動的に表示する項目の最大数を入力す
   る。:guilabel:`&From` ドロップダウンリストでは指定された順序で最上位または最
   下位の項目を選択する。:guilabel:`Using field` ドロップダウンリストでデータを
   並べ替えるデータフィールドを選択する。
:guilabel:`Hide &Items`
   計算から隠す項目をオンにする。
:guilabel:`Hierarch&y`
   フィールドに階層が複数ある場合、使用するものを選択する。ピボットテーブルは
   データ階層を含む外部原データに基づいている必要がある。ほとんどの使用者にとっ
   て、Calc は 一つのフィールドに複数の階層を設けないため、通常このオプションは
   灰色表示される。ピボットテーブル拡張を使用する場合、その拡張で一部のフィール
   ドに階層を複数定義するとこの選択肢が使用できるようになる可能性がある。その拡
   張の仕様を見ないとわからない。

Options for filter fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|Filters| のフィールドに対する |DataFieldDlg| は |RowFields| と |ColumnFields|
のフィールドに対するそれと同じ設定だ。ピボットテーブルの柔軟性を利用すれば、絞り
込み、列、行の間で異なるフィールドを切り替えることが可能だ。フィールドは指定した
設定を保持する。絞り込みフィールドには行または列フィールドと同じ性質がある。これ
らの設定はフィールドを絞り込みフィールドとしてではなく、行または列フィールドとし
て使用する場合に限り効果がある。

Working with the results of the pivot table
======================================================================

|PivotTableLayoutDlg| はたいへん柔軟で、マウスを数回クリックするだけでピボット
テーブルを完全に再構築できる。

Changing the layout
----------------------------------------------------------------------

ピボットテーブル上で |PivotTableLayoutDlg| を開いて、フィールドをドラッグ＆ド
ロップし直せば、表のレイアウトを容易に変更可能だ。そして、ピボットテーブルの結果
ビューでも操作可能なものがある。それらしい UI 要素をマウスでドラッグして試して覚
えろ。

一部の操作は、ピボットテーブルの結果ビューでも実行可能。結果内で、絞り込み、列、
行フィールドのいずれかを別の位置にドラッグしろ。行から列への移動など、別のフィー
ルドに移動する場合は、マウスポインターの形が開始時の形（矢印の頭の水平または垂直
のブロック）から反対に変わり、ドロップできるようになる。

列、行、絞り込みフィールドをピボットテーブルから削除するには、そのフィールドをク
リックして表の外へドラッグしろ。|PivotTableLayoutDlg| に戻って設定し直さない限
り、削除したフィールドは戻らない。

Grouping rows or columns of a pivot table
----------------------------------------------------------------------

分析や要約の多くでは、区分をグループ化する必要がある。クラスで結果を併合可能だ。
グループ化はそれがまだなされていないピボットテーブルでしか実行不可だ。

正しい升目領域を選択したら、|MenuBar| の |DataGroupM| を選択するか、:kbd:`F12`
を押す。グループ化される値の型はグループ化がどのように機能するかを主に決定するも
のだ。スカラー値か、グループ化したいテキストなどの値かを区別する必要がある。

.. note::

   グループ化する前に、グループ化されていないデータでピボットテーブルを作成する
   必要がある。ピボットテーブルの作成に必要な時間は、基本データの規模ではなく、
   列と行の数によって主に決まる。グループ化により、少ない行数と列数でピボット
   テーブルを作成できる。データ給源によっては、ピボットテーブルに多くの区分を含
   めることが可能だ。

グループ化を解除するには、グループ内をクリックし、:menuselection:`&Data-->&Group
and Outline-->&Ungroup...` を選択するか、:kbd:`F12` を押す。

.. admonition:: 読者ノート

   ピボットテーブルに対するグループ化の動作を己の家計簿で確認した。

Grouping of categories with scalar values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

スカラー値をグループ化するには、グループ化する区分の行または列の升目を一つ選択す
る。そして次のいずれかを行う：

* |MenuBar| の |DataGroupM| を選択
* :kbd:`F12` を押す

これにより :guilabel:`Grouping` ダイアログボックスが開く。どの値の範囲でグループ
化するかを:guilabel:`Start` と :guilabel:`End` で定義できる。既定設定は最小値か
ら最大値までの全範囲だ。:guilabel:`Group by` ではクラスサイズ（区間サイズ）を入
力できる。

.. admonition:: 読者ノート

   動作確認できず。

Grouping of categories with date / time values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

日付・時刻値をグループ化するのも前節と同様の手順を実行する。

:guilabel:`Group by` フィールドで指定するクラスサイズは、日付時刻の場合、日単位
の時間間隔を明示的に指定する代わりに、定義済みの時間間隔（秒、分、時、日、月、四
半期、年）のいずれかを選択できる。

Grouping without automatic creation of intervals
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

区分のいくつか（例えば、テキストフィールドを含むカテゴリー）では、区間を作成する
ことはできない。そのようなフィールドに対しては、どの値をグループにまとめるかを定
義することならば可能だ。

これらの区分をグループ化するには、ピボットテーブルの結果で、グループにまとめたい
個々のフィールド値をすべて選択する。そのような選択状態で |MenuBar| の
|DataGroupM| を選択するか、:kbd:`F12` を押して選択升目をグループ化する。

.. tip::

   |Ctrl| を押しながらクリックすることで、連続していない複数の升目を選択可能。

.. admonition:: 読者ノート

   家計簿で、例えば「場所」の列で「ビッグエー墨田業平店」と「ビッグエー墨田京島
   店」を選択して :kbd:`F12` を押すと、この機能のありがたさを理解できる。

入力フィールドの名前を編集することで、グループと新しく作成されたグループフィール
ドの既定の名前を変更できる。例えば、`Group2` を `Technical` に）。後で間取りを変
更した場合でも、ピボットテーブルはこれらの設定を記憶する。

グループの部分合計を追加するには、ピボットテーブルの結果を右クリックし、
|PropertiesC| を選択する。|RowFields| の対象項目をダブルクリックし、
|DataFieldDlg| の :guilabel:`&Automatic` を選択する。|OK| を押していく。

まだ有効になっていない場合は、|PivotTableLayoutDlg| で :guilabel:`&Enable drill
to details` を選択する。対象列の名前およびグループフィールド登録項目をダブルク
リックして、グループ登録項目木を操作する。

.. note::

   構造化されたデータベースを使用すると、ピボットテーブル内で手動で並べ替えを行
   う必要がなくなる。

Sorting the result
----------------------------------------------------------------------

ピボットテーブルの結果は、既定では、列および行の区分が昇順で表示されるように並べ
替えられる。並べ替え順序を変更する方法：

* 列の見出しにあるドロップダウンメニューで並べ替え順序を選択する
* ドラッグ＆ドロップを使用して手動で並べ替える
* 該当する行または行の |DataFieldOptionsDlg| で並べ替え順序を選択

.. _calc09-anchor-drop-down:

Select sort order from drop-down menus on each column heading
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

登録項目を並べ替える最も簡単な方法は、行または列フィールドの列見出しの右側にある
▼をクリックし、次の並べ替え選択肢のいずれかを選択することだ。

* `Sort Ascending`
* `Sort Descending`
* `Custom Sort`

`Custom Sort` を選択すると、|OptionsDlg| |SortListsPage| で定義済みのカスタム並
べ替えのいずれかに従って並べ替えが行われる。並べ替えリストの作成と使用の詳細につ
いては |Calc02| を見ろ。

このダイアログにはピボットテーブルのデータを簡単に絞り込み処理する機能もある。必
要な個々のチェックボックスをオンにして、ピボットテーブルの結果に表示されるデータ
を選択する。すべてを表示する、現在の項目のみ見せる、現在の項目のみ隠す、といった
選択肢が設けられている。|OK| を押して、選択した絞り込み処理を有効にする。絞り込
みが実行されると、▼の色が青地に白に変わり、右下に小さな白い四角が追加される。

Sort manually by using drag and drop
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ピボットテーブルの結果で区分の値を持つ升目を移動することで、区分内の順序を変更で
きる。ドラッグした升目はドロップした升目の前にねじ込まれる。

Calc では、升目が選択されていなければならず、キャレットがセル内にあるだけでは不
十分であることに気をつけろ。選択升目の背景は異なる色になる。升目一つに目印を付け
るには次のいずれかを実行する：

* 升目をクリックし、さらに |Shift| を押しながらクリックする。
* マウスボタンを押し、升目二つにまたがる範囲をドラッグし、マウスボタンを放さずに
  最初の升目にドラッグする。マウスボタンを離す。これで、ドラッグ＆ドロップで個々
  の升目を動かすことができる。

升目を複数選択するには、余分なキーを押さずに升目を一つマークし、|Shift| または
|Ctrl| を押しながら他の升目をクリックする。

Sort automatically
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

自動的に並べ替えるには、ピボットテーブル内で右クリックし、|PropertiesC| を選択す
る。|PivotTableLayoutDlg| が開く。

並べ替えたい行または列フィールドをダブルクリックします。開いた
|DataFieldDlg| で :guilabel:`&Options...` を押して
|DataFieldOptionsDlg| を表示する。

:guilabel:`Sort by` で :ref:`並び替え選択肢<calc09-anchor-sort-by>` を決める。

.. _calc09-anchor-drilling:

Drilling (showing details)
----------------------------------------------------------------------

ドリル機能を使用すると、ピボットテーブルの結果中に単一の、圧縮された値の関連詳細
データを見られる。この機能は |PivotTableLayoutDlg| で :guilabel:`&Enable drill
to details` をオンにした場合に限り使用できる。

ドリルを活動させるには升目をダブルクリックするか、:menuselection:`&Data-->&Group
and Outline-->&Show Details` を選択する。可能性は二つ：

#. 活性升目が行または列フィールドの場合、ドリルが意味するところは別のフィールド
   の区分への追加的な分解だ。

   :guilabel:`Show Detail` ダイアログが表示され、さらに細分化するフィールドを選
   択できる。

   詳細を再度隠すには `Golf` 升目をダブルクリックするか、
   :menuselection:`&Data-->&Group and Outline-->&Hide Details` を選択する。

   ピボットテーブルは、選択したフィールドを追加して隠すことで、選択フィールドを
   記憶し、次に当該フィールドをドリルダウンするときにダイアログが表示されないよ
   うにする。選択した項目を削除するには、 |PivotTableLayoutDlg| を開き、
   |RowFields| または |ColumnFields| 領域の不要な選択項目を削除する。
#. 活性升目がデータフィールドである場合、ドリルダウンすると、この値に集約される
   データ給源のすべてのデータ登録項目の一覧が表示される。

   このような升目をダブルクリックすると、この値に含まれるすべてのデータセットの
   新規一覧が新規シートに表示される。

.. admonition:: 読者ノート

   家計簿でいうと交通費で試すとわかりやすい。最初の場合は交通機関や「交通費」
   を、最後の場合は金額をダブルクリックすることにそれぞれ相当する。後者の場合、
   新規シートが現れて、乗車ごとの明細が示される。

.. _calc09-anchor-filtering:

Filtering
----------------------------------------------------------------------

ピボットテーブルの分析をデータベースに含まれる情報の部分集合に制限するために、ピ
ボットテーブル結果を絞り込むことが可能だ。

.. note::

   原データを含むシートで使用された AutoFilter または標準フィルターはピボット
   テーブルの分析処理には影響しない。ピボットテーブルでは開始時に選択された完全
   なリストが常に使用される。

これを行うには、結果の左上の絞り込みボタンをクリックするか、結果内で右クリック
し、コンテキストメニューから :menuselection:`&Filter...` を選択する。

.. note::

   絞り込みボタンは |PivotTableLayoutDlg| の :guilabel:`Add fi&lter` がオンであ
   る場合にしか使用できない。

|FilterDlg| では標準フィルターと同様にして絞り込みオプションを三つまで定義できる。
このダイアログボックスの :guilabel:`Op&tions` 区画のコントロールは
|StandardFilterDlg| のそれに似ている。|Calc02| を見ろ。

ピボットテーブルに表示されるデータは、列見出しの右側のドロップダウンまたは絞り込
みフィールドを使用して絞り込むことも可能だ。列見出しによる絞り込みについては
:ref:`calc09-anchor-drop-down` を見ろ。

|PivotTableLayoutDlg| の |Filters| 領域に配置したフィールドは、ピボットテーブル
の結果を絞り込むもう一つの実用的な方法だ。その利点は、使用する絞り込み基準が明確
に示されることにある。絞り込みフィールドボタンの右側にある▼をクリックすると、関
連する絞り込みダイアログにアクセスできる。

.. _calc09-anchor-filtering-status:

絞り込みフィールドボタンに隣接するテキストは、絞り込み状態を示す：

* 何も絞られていない場合は `- all -`
* 全てではないが複数の項目が絞られる場合は `- multiple -`
* その値だけが絞られる場合はその値

.. _calc09-anchor-refresh:

Updating (refreshing) changed values
----------------------------------------------------------------------

ピボットテーブルを作成した後で原データを変更しても作成された表は自動的に更新され
ない。こういう場合はピボットテーブルを手動で更新する必要がある。

更新するにはピボットテーブルをクリックして次のいずれかを実行する：

* |MenuBar| から :menuselection:`&Data-->&Pivot Table-->&Refresh`
* 右クリックメニューから :menuselection:`&Refresh`

原データの登録項目が増減した場合には、|PivotTableLayoutDlg| :guilabel:`Source`
欄で範囲を変更することで表を更新可能だ。より複雑な変更が生じた場合には、ピボット
テーブル全体を作り直せ。

Cell formatting
----------------------------------------------------------------------

ピボットテーブルの結果領域の升目書式は自動的に整形される。この書式設定は、Calc
にあるすべてのツールを用いて変更可能だ。ただし、直接書式設定を使用してピボット
テーブルの設計に変更を加えると、次に表を更新するときに自動適用される書式設定に戻
る。

ピボットテーブルの作成時に、標準升目スタイルがまだ含まれていない場合は文書中のス
タイル一覧に追加される。これらのスタイルそれぞれがピボットテーブルの部分に適用さ
れる。これらのピボットテーブルスタイルはカスタマイズ可能だ。ピボットテーブルのス
タイルは次のとおり：

* `Pivot Table Category`
* `Pivot Table Corner`
* `Pivot Table Field`
* `Pivot Table Result`
* `Pivot Table Title`
* `Pivot Table Value`

カスタマイズしたければ、このスタイルを :menuselection:`&Edit Style...` すればい
い。

.. tip::

   ピボットテーブルスタイルを使用しろ。更新時にピボットテーブルの形式が予期せず
   変更されなくなり、文書内にあるピボットテーブルすべてが同じ体裁をとることが保
   証できる。

データフィールドの数値形式について、Calc は原リストにおける対応する升目で使用さ
れている数値形式を採用する。ほとんどの場合、これは便利だ。ただし、結果が分数また
は百分率の場合、ピボットテーブルはこれが問題になり得るということを認識しない。数
値の形式を手動で修正できるが、上の議論のとおり、そのような修正は次の更新以降無効
だ。

Deleting a pivot table
----------------------------------------------------------------------

ピボットテーブルを削除する方法は次のいずれかを実行する：

* |MenuBar| から :menuselection:`&Data-->&Pivot Table-->&Delete`
* 右クリックメニューから :menuselection:`&Delete`

ピボットテーブル専用シートを割り当てている場合には、シート丸ごと削除でもいい。

.. caution::

   関連付けられたピボットチャートがあるピボットテーブルを削除すると、ピボット
   チャートも削除される。このような場合、削除を確認するためのダイアログボックス
   が表示される。

Using pivot table results elsewhere
======================================================================

The problem
----------------------------------------------------------------------

通常、値を含むセルのアドレスを入力して値への参照を作成する。例えば、式 ``=C6*2``
は、升目 C6 への参照を作成し、2 倍した値を返す。この升目がピボットテーブルの結果
領域にある場合は、行フィールドと列フィールドの特定の区分を参照して計算された結果
が格納される。Figure 47 では、升目 C6 に、区分が `Sailing` である `Employee`
`Hans` の売上値の合計が格納されてる。升目 C12 の数式はこの値を使う。

.. admonition:: 読者ノート

   C12 は明白にピボットテーブル結果外のアドレスであるとする。

原データまたはピボットテーブルの間取りが変更された場合は、`Sailing` 区分に属する
`Hans` の売上値が別の升目に表示される可能性があることを考慮する必要がある。数式
はまだ升目 C6 を参照しているため、間違った値が使用される。正しい値は別の場所にあ
る。

The solution: Function `GETPIVOTDATA()`
----------------------------------------------------------------------

関数 `GETPIVOTDATA` を使用してピボットテーブル内の値への参照を、この値の特定の識
別区分を使用して取得する。この関数はピボットテーブルの結果をスプレッドシート内の
別の場所で再利用する場合に、Calc の数式内で使用可能だ。

Syntax
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

変種が二つある：

.. code:: text

   =GETPIVOTDATA(Target Field; Pivot Table[; Field 1; Item 1][; ... [Field 126; Item 126]])
   =GETPIVOTDATA(Pivot Table; Constraints)

最初の変種中、角括弧はそれが囲んでいる引数がオプションであることを示す。

First syntax variation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

引数 `Target Field` は関数内で使用するピボットテーブルのデータフィールドを指定す
る。ピボットテーブルにデータフィールドが一つしかない場合、この項目は無視されるの
だが、いずれにせよ入力する必要はある。

ピボットテーブルにデータフィールドが複数ある場合は、データ給源のフィールド名
(e.g. "Sales Value") またはデータフィールド自体のフィールド名 (e.g. "Sum - Sales
Value") を入力する必要がある。

引数 `Pivot Table` は使用するピボットテーブルを指定する。文書内にはピボットテー
ブルが複数含まれている場合がある。ここにはピボットテーブルの領域内のセル参照を入
力する。ピボットテーブルの左上隅の升目を常に使用すると、間取りが変更されても、そ
のセルが常にピボットテーブル内にあることを保証できる。

.. rubric:: 例

.. code:: text

   =GETPIVOTDATA("Sales Value";A1)

最初の二つの引数のみを入力すると、関数はピボットテーブルの合計結果を返す。

フィールド名と要素のペアとしてさらに引数を追加して、特定の部分合計を取得可能だ。
Figure 49 の例では、`Hans for Sailing` の部分合計を取得するため、セル C12 の数式
は以下のようになる：

.. code:: text

   =GETPIVOTDATA("Sales Value",A1,"Employee","Hans","Category","Sailing")

.. admonition:: 読者ノート

   Figure 各種は本書実物を参照しろ。だいだいわかるだろう。

Second syntax variation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

引数 `Pivot Table` は最初の構文変種と同じ方法で指定する。

引数 `Constraints` にはピボットテーブルから取得する値を指定するリストを空白で
区切って入力する。データフィールドが複数ある場合は、このリストにデータフィールド
名を含める必要がある。特定の部分結果を選択するには、:samp:`{Field
name}[{Element}]` の形式で登録項目を追加する。

Figure 50 の例では、`Sailing` の `Hans` の部分合計を取得する場合、セル C12 の数式は
以下のようになる：

.. code:: text

   =GETPIVOTDATA(A1,"Sales Value Employee[Hans] Category[Sailing]")

Using pivot charts
======================================================================

Introduction
----------------------------------------------------------------------

ピボットテーブルはデータを再編成、操作、要約するための強力なツールであり、ピボッ
トチャートはピボットテーブルの情報を視覚的表現を設ける。ピボットテーブルの出力か
らピボットチャートを作成でき、ピボットテーブルが変更された場合はピボットチャート
も変更される。

ピボットチャートは |Calc03| で説明した、より一般的な統計図表の特殊な実例だ。ピ
ボットチャートと Calc の他の図表の主な違いは次のとおりだ：

* ピボットチャートはピボットテーブルから発行されたデータの変化を追跡し、それに応
  じて自身のデータ系列とデータ範囲を自動調整する。
* ピボットチャートボタンがピボットチャートに備わっている。これらのボタンはピボッ
  トチャート独自のもので、通常の図表にはない。ボタンの重要な目的は、基礎となるピ
  ボットテーブルの間取りを表すことで、ピボットテーブルのフィールドが表示される。
  絞り込みフィールドを表すボタンはピボットテーブルの上部にある。行フィールドを表
  すボタンは、ピボットチャートの下部に表示される。列フィールドを表すボタンはピ
  ボットチャートの右側の凡例に重ねて表示される。ピボットチャートのボタンを使用し
  て、ピボットチャートに表示されるデータを絞り込むことも可能だ。

Creating a pivot chart
----------------------------------------------------------------------

ピボットチャートの作成方法は次のいずれか：

* メインメニュー :menuselection:`&Insert-->&Chart...`
* |StandardToolbar| の :guilabel:`Insert Chart` を押す

Calc がピボットテーブルを検出し、|ChartWizard| が開く。|ChartWizard| を使用し
て、ピボットチャートの図表型と図表要素を選択可能だ。このウィザードは通常のグラフ
に対応するそれと似ているが、ピボットチャートの場合、データ範囲とデータ系列を定義
する手順が無効になっている。

ウィザードの最初の手順段階では、図表型を選択し、通常の図表と同じオプションが利用
できる。

第二段階は図表要素を選択することであり、これらは通常の図表と同様だ。

|Finish| を押してウィザードを閉じ、ピボットチャートを作成する。

Editing a pivot chart
----------------------------------------------------------------------

ピボットチャートを作成した後、それを移動したり、寸法を変更したり、見てくれを改善
したいことがある。Calc にはグラフの種類、グラフ要素、フォント、色、その他多くの
オプションを変更するためのツールが搭載されている。ピボットチャートで使用できる機
能は、通常のチャートで使用できる機能と同じなので、|Calc03| を見ろ。

Updating a pivot chart
----------------------------------------------------------------------

ピボットテーブルの原データが変更された場合は、ピボットテーブルを更新すると、ピ
ボットチャートもそれに応じて更新される。ピボットテーブル（すなわちピボットチャー
ト）を更新する方法は :ref:`calc09-anchor-refresh` を見ろ。

Filtering a pivot chart
----------------------------------------------------------------------

ピボットチャートから不要なデータを削除するには絞り込みを使え。

ピボットテーブルに適用される絞り込みはすべて、連動しているピボットチャートにも等
しく影響する。ピボットテーブルの多様な絞り込みの仕組みについては
:ref:`calc09-anchor-filtering` を見ろ。

ピボットチャートのボタンには関連するポップアップ操作があることを示す▼がある。絞
り込みが適用されている場合、この▼は黒から青に変わる。ピボットチャートボタンは
チャートをダブルクリックすると操作可能になり、チャートの周囲に灰色の枠が表示され
る。この操作によりピボットチャートは編集モードになる。

ピボットチャートの上部にある絞り込みフィールドボタンをクリックすると簡素なダイア
ログが表示される。これを使ってピボットテーブル・チャートに適用される絞り込みを変
更する。ボタンの凡例の右側の部分には :ref:`絞り込み状態
<calc09-anchor-filtering-status>` が示される。

ピボットチャートの下部と右側にある、▼を含むボタンをクリックすると、並べ替えと絞
り込みのダイアログにアクセスできる。これを使用して、ピボットテーブル・チャートに
適用される並べ替えおよび絞り込みを変更する。

Deleting a pivot chart
----------------------------------------------------------------------

ピボットチャートを削除するには、チャートを選択状態にして |Del| を押せ。

.. note::

   ピボットチャートを削除しても関連するピボットテーブルに影響はない。

.. caution::

   関連付けられたピボットチャートがあるピボットテーブルを削除すると、ピボット
   チャートも削除される。このとき、ピボットテーブルの削除を確認するダイアログ
   ボックスが表示される。
