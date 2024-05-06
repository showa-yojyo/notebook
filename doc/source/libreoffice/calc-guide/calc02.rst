======================================================================
Calc Guide Chapter 2, Entering and Editing Data ノート
======================================================================

.. include:: ./calc-inc.txt

.. contents:: 章見出し
   :depth: 3
   :local:

Introduction
======================================================================

セルにデータを入力するさまざまな方法を述べる章だ。

Entering data
======================================================================

データ入力のほとんどはキーボードを使って行う。

Numbers
----------------------------------------------------------------------

セルをクリックしてキーボードから数を入力する（テンキーを用いるのが普通）。

Negative numbers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

負の値を入力するには、プログラミング言語のコードのように ``-1234`` のように負の
符号と数を続けてタイプするか、あるいは ``(1234)`` のように絶対値を丸括弧で囲むと
いう方法もある。

Leading zeroes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

たとえば ``01481`` のように、先頭にゼロを含む数値が入力されると、Calc は先頭のゼ
ロを削る。数値の書式とセル内の最小文字数の両方を保持したい。次の方法のいずれかを
使用して先頭のゼロを埋めさせる：

#. セルを選択
#. 次のどれかを実行：

   * |MenuBar| :menuselection:`F&ormat-->Ce&lls...`
   * 右クリックメニュー :menuselection:`&Format Cells...`
   * キーバインド |Ctrl| + :kbd:`1`
#. |NumbersTab| 内 :guilabel:`C&ategory` から :guilabel:`Number` を選択
#. :guilabel:`Leading &zeros` 欄に必要最小限の文字数を入力する。例えば ``4`` を
   入力したとすると、セルへの入力 ``12`` は ``0012`` となる。
#. |OK| を押す

あるいは |Sidebar| |PropertiesDeck| (|Alt| + :kbd:`1`) で同様の指示をする。

Numbers as text
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

数字は以下のいずれかの方法でテキストに変換することが可能：

#. セルを選択
#. 先述の方法で |FormatCellsDlg| を開く
#. |NumbersTab| 内 :guilabel:`C&ategory` から :guilabel:`Text` を選択
#. |OK| を押す

|Sidebar| |PropertiesDeck| も使える。

数字が（郵便番号など）計算用途でない場合には、数字の前に ``'`` を入力することで
テキスト扱い可能。セルのフォーカスを移動すると ``'`` は削除され、先頭のゼロは保
持され、数値は左揃えのテキストに変換される。

Text
----------------------------------------------------------------------

セルをクリックしてテキストを入力する。

* テキストは左揃え既定。
* セルには複数行テキストを入力可能。改行は |Ctrl| + |Enter| を押して入れる。

|FormulaBar| では複数行テキストを入力する場合に :guilabel:`Input Line` 欄を縦に
拡張することが可能。右側にある▼をクリックすると複数行になる。

* :guilabel:`Input Line` の下端を上下にドラッグして高さを操作可能。
* :guilabel:`Input Line` を一行の高さに戻すには、▲をクリックする。

Date and time
----------------------------------------------------------------------

日付時刻の入力は微妙な問題なので、本文を引用する：

   Select the cell and type the date or time. You can separate the date elements
   with a slash (``/``) or a hyphen (``-``) or use text, for example ``10 Oct
   2020``. The date format automatically changes to the selected format used by
   Calc.

私の場合は日本語ロケールのことを考慮しないといけない。

* |OptionsDlg| |LanguagesPage| の :guilabel:`Date acceptance &patterns` 欄でパ
  ターンを個別に定義しろ。
* どのロケールでも ISO 8601 YYYY-MM-DD パターンでの入力を受け付けるので、これを
  用いることを習慣化しておきたい。

時間を入力するときは、10:43:45 のように、時間要素をコロンで区切る。時刻の書式は
Calc が決めるものに自動的に変更される。その設定方法は：

#. セルを選択して |FormatCellsDlg| を開く
#. |NumbersTab| で :guilabel:`C&ategory` 欄から :guilabel:`Date` か
   :guilabel:`Time` を選択
#. :guilabel:`Fo&rmat` 一覧から所望の日付・時刻書式を選択
#. |OK| を押す

日付書式はシステムまたは文書の言語設定の影響を受ける。

Special characters
----------------------------------------------------------------------

:menuselection:`&Insert-->S&pecial Character...` コマンドで :guilabel:`Special
Characters` ダイアログボックスが開く。

.. admonition:: 利用者ノート

   Google 日本語入力を愛用しているならばこの機能は使わない。対象文字のコードを知
   らないと指定に時間がかかり過ぎる。文字名で検索できるなどの機能があっていいか
   もしれない。

AutoCorrect options
----------------------------------------------------------------------

AutoCorrect を使用したデータ入力中に、当機能が有効である限り、変更の多くが自動的
に適用されます。AutoCorrect による変更を取り消すには Undo するか、または変更箇所
に戻り、自動修正を手動で置き換えろ。

:menuselection:`&Tools-->&AutoCorrect Options...` で自動訂正に関する設定が可
能。

Inserting dashes
----------------------------------------------------------------------

マイナス記号をダッシュに置換する変換表が仕込まれている。マイナスの前後の空白文字
有無でダッシュの長さが変わることもあるようだ。

.. seealso::

   欧文ではこの辺の記法を気にすることを覚えておく。

   `ハイフン・マイナス・enダッシュ・emダッシュの違いと使い分け
   <https://u.muroran-it.ac.jp/hydrogen/semi_dash01.html>`__

Speeding up data entry
======================================================================

* ドラッグ＆ドロップ
* AutoInput ツール
* Fill ツール
* 選択リスト
* Data Entry Form

同じスプレッドシートの複数のシートに同時に情報を入力する機能もある。

AutoInput tool
----------------------------------------------------------------------

AutoInput 機能は同じ列の他の入力に基づいて、自動的に入力を補完する。テキストがセ
ル内で強調表示されている場合、自動入力は次のように使用できる：

* |Enter| を押すと補完を確定かつ次のセルへ移動
* |F2| を押すと補完を確定かつキャレットをセル内に留める
* 候補が複数ある場合は

  * 部分的に補完して |ArrowR| を押す
  * |Ctrl| + |Tab| や |Ctrl| + |Shift| + |Tab| で前後の補完候補に切り替える
* |Alt| + |ArrowD| で AutoInput 全候補ドロップダウンリスト表示

関数名と合致する文字を使用して数式を入力すると、関数一覧がヘルプヒントとして表示
される。

AutoInput 機能のオンオフは :menuselection:`&Tools-->&AutoInput` を実行。

Fill tool
----------------------------------------------------------------------

既存の内容を複製したり、セル範囲に一連の内容を作成したりするコマンド。

#. コピーしたい内容を含むセルを選択。
#. マウスポインターを任意の方向にドラッグするか、|Shift| を押しながら、埋めたい
   最後のセルをクリック。
#. :menuselection:`&Sheet-->F&ill Cells-->` 以下にある埋めたい方向に対応するコマ
   ンドを実行。

   * 下方向にはキーバインド |Ctrl| + :kbd:`D` が割り当て済み。

または、

#. 中身を含むセルを選択
#. 選択セルの右下隅にある選択ハンドルの上にマウスポインターを移動（絵が変形）
#. 埋めたい方向（縦または横）にドラッグする。元のセルにテキストが含まれていれ
   ば、テキストが自動的にコピーされる。

   元のセルに、定義済み一覧の数値またはテキストが含まれている場合は、系列が作成
   される。複製したい場合には |Ctrl| を押しながらドラッグする。

Using a fill series
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:menuselection:`&Sheet-->F&ill Cells-->Fill S&eries...` を実行すると
:guilabel:`Fill Series` ダイアログボックスが開く。必要な系列の型を選択するか、独
自の一覧を作成する。

* :guilabel:`Series Type` ラジオボタン :guilabel:`&Growth` オプションは等比数列
  で埋めるのに有用。
* :guilabel:`Time Unit` ラジオボタン :guilabel:`&Weekday` オプションは平日で埋め
  る（土日を飛ばす）。

Defining a fill series
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

連続データ自作方法は |OptionsDlg| |SortListsPage| を調べろ。

Fill with random numbers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. :menuselection:`&Sheet-->F&ill Cells-->Fill R&andom Number`
#. :guilabel:`Cell &range` を確認
#. :guilabel:`Random Number Generator` 区画の入力欄で乱数仕様を指定
#. |OK| を押す

分布関数としては有名どころはだいたい用意されている。それに応じて関連引数も指定す
る。

:guilabel:`Enable roundin&g` と :guilabel:`Decimal &places` では出力を整数にする
ことはできない？

Selection lists
----------------------------------------------------------------------

|Alt| + |ArrowD| でドロップダウンリスト表示。

Data Entry Form tool
----------------------------------------------------------------------

:menuselection:`&Data-->F&orm...` という登録項目追加機能がある。このコマンドは
スプレッドシートでの表データ入力を省力化する。

* データ登録項目の入力、編集、削除が可能
* ダイアログボックスで操作するのでシートをスクロールすることを回避できる
* データ表にはヘッダー行が必須で、各セルの内容が列の見出しになる。各ヘッダーセル
  の内容はダイアログボックスの各データ欄のラベルになる。

使い方：

#. データ表内のヘッダーまたはデータセルを選択
#. 上記コマンドを実行して :guilabel:`Data Form` ダイアログボックスを開く
#. 先頭データが入力されているが、加除編集して適当なボタンを押す
#. |Close| を押す

ダイアログボックス右柱の各ボタンの役割は見ればわかる。

新しい登録項目を入力する前に最後の登録項目に移動しないと、現在の登録項目が編集さ
れる。

Merging and splitting cells
======================================================================

Merging
----------------------------------------------------------------------

.. admonition:: 利用者ノート

   実際の |UI| と本文の記述が合致していない。特に右クリックメニュー。

連続セルを選択し、一つに併合することが可能だ。

#. 併合したい連続セル範囲を選択
#. 次のいずれかを実行：

   * |MenuBar| :menuselection:`F&ormat-->M&erge and Unmerge Cells-->&Merge
     Cells...`
   * |FormattingToolbar| :guilabel:`Merge Cells`
#. セルに何らかのデータが含まれている場合 :guilabel:`Merge Cells` ダイアログボッ
   クスが開く
#. |OK| を押す

セルを併合するとスプレッドシート内の数式に計算エラーが発生することがある。

Splitting
----------------------------------------------------------------------

併合の逆操作だ。セル内のデータはすべて最初のセルに残る。セルが併合される前に非表
示のセルに内容があった場合は、その内容を手動で正しいセルに移動する必要がある。

#. 併合セルを選択
#. 次のいずれかを実行：

   * |MenuBar| :menuselection:`F&ormat-->M&erge and Unmerge Cells-->&Unmerge
     Cells...`
   * |FormattingToolbar| :guilabel:`Unmerge Cells`

Sharing content between sheets
======================================================================

複数のシートの同じセルに同じ情報を、各シートに個別に入力する代わりに、複数のシー
トに同時に入力する方法がある。

#. |SelectSheetsM| を実行して |SelectSheetsDlg| を開く
#. 対象シートを一覧から選択
#. |OK| を押す
#. シートのセルに何か入力すると、選択シートすべてでその入力がなされる
#. シート選択を解除

|Calc01| で述べられたマウスクリック方式でも可。

Validating cell contents
======================================================================

セルに対して入力値に制約を定義する機能がある。

Defining validation
----------------------------------------------------------------------

セルに入力された新しいデータを検証する：

#. 対象セルを選択
#. :menuselection:`&Data-->&Validity...` を実行して :guilabel:`Validity` ダイア
   ログボックスを開く
#. :guilabel:`Criteria`, :guilabel:`Input Help`, :guilabel:`Error Alert` 各タブ
   ページにある選択肢を使用して、そのセルに入力が許される内容の型を定義する。

Criteria options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

このタブページでは入力セルの検証規則を指定する。例えば 1 から 10 までの数である
とか、20 文字以下のテキストであるなどの基準を定義するものだ。

ここで使用できる選択肢は :guilabel:`Allow` ドロップダウンリストで選択した内容に
よって異なる。

* :guilabel:`Cell range` はセル範囲に指定された値のみを許可する。セル範囲は、
  明示的に指定するほかにも、データベース範囲、名前付き範囲を指定することも可。
* :guilabel:`List` は一覧で指定された値または文字列のみを許可する。文字列と値は
  混在可。 数は値で評価されるため数 1 を一覧に含めておくと 100% という入力も有効
  になる。
* :guilabel:`Custom` は :guilabel:`&Formula` に入力された数式に対応するものを許
  す。

それ以外の |UI|:

:guilabel:`Allow &empty cells` は :menuselection:`&Tools-->&Detective-->
&Mark Invalid Data` と組み合わせて、空白セルを無効であると表示するか否かを指定す
る。

:guilabel:`Show selection list` は選択可能なすべての有効な文字列または値の一覧を
示す。この一覧は、セルの右にある下矢印をクリックするか、セルを選択して
|Alt| + |ArrowD| を押すことで開く。

.. admonition:: 利用者ノート

   このリスト機能は多用したい。

:guilabel:`&Data` ドロップダウンリストと

* :guilabel:`&Value` 欄
* :guilabel:`&Minimum` 欄と :guilabel:`Ma&ximum` 欄

はセットで指定する。

:guilabel:`&Formula` 欄はカスタム検証を行うために真偽値に評価される数式を入力す
る。例えばセル A4 でこのコマンドを実行したならば ``ISEVEN(A4)`` のように与えられ
る。

Input Help options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

シート上でセルを選択したときにポップアップ表示するメッセージを入力する。
:guilabel:`&Title` と :guilabel:`&Input help` の内容が同じツールチップ内に描かれ
る。

Error Alert options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

このタブページではセルに無効なデータが入力されたときに表示されるエラーメッセージ
を定義する。

:guilabel:`&Action` ドロップダウンリストではセルに無効なデータが入力されたときの
動作を選択する。

* :guilabel:`Stop` は完全拒否。
* :guilabel:`Warning` と :guilabel:`Information` は |OK| か
  :guilabel:`&Cancel` かをシート利用者に選ばせるようにする。
* :guilabel:`Macro` は |Browse| で指定する、無効データが入力されたときに実行した
  いマクロを選択する。

Calc Detective
----------------------------------------------------------------------

ここに挙げるコマンドは無効なデータを含むスプレッドシートセルを発見するために使う
ものだ。

#. :menuselection:`&Tools-->&Detective-->&Mark Invalid Data` を実行して無効
   データを含むセルを検出する。これにより無効セルに印が付く。
#. そのようなセルを訂正する。
#. :menuselection:`&Tools-->&Detective-->Remove All Traces` を実行して無効印
   を消去する。

妥当規則はセル書式の部分だ。したがって、後述される |DeleteContentsDlg| の
:guilabel:`Delete all` を行うと削除される。

Editing data
======================================================================

Deleting data
----------------------------------------------------------------------

Deleting cell data only
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

セルの書式を損なわず中身を消去するだけなら |Del| 押しで十分。

Deleting cells
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

次の操作は完全削除だ。削除されたセルの下か右にあるものが跡地を埋める。

#. セル一個またはセル範囲を選択
#. |MenuBar| :menuselection:`&Sheet-->Delete C&ells...` 実行またはキーバインド
   |Ctrl| + :kbd:`-` 押し
#. |DeleteCellsDlg| にある選択肢を決める
#. |OK| を押す

Deleting data and formatting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

書式も消すなら：

#. セル一個またはセル範囲を選択
#. |MenuBar| :menuselection:`&Sheet-->Cle&ar Cells...` またはキーバインド
   |BackSpace|
#. |DeleteContentsDlg| にあるチェックボックスを適宜オンにする
#. |OK| を押す

Replacing data
----------------------------------------------------------------------

* セルのデータを完全に置き換えて新しいデータを挿入するには、セルを選択して新しい
  データを入力する。
* データは置き換わるが、セルで使用されている元の書式は保持される。
* または、|FormulaBar| :guilabel:`Input line` をクリックし、データをダブルクリッ
  クして強調表示状態にし、新しいデータを入力する。

Editing data
----------------------------------------------------------------------

セルからデータすべてを削除することなく（一文字だけ変えたい場合など）、内容を編集
する必要がある場合がある。

Using the keyboard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. 対象セルを選択
#. |F2| を押し、キャレットをセルの末端に置く
#. 矢印キーでセルに新しいデータを入力する位置にキャレットを移動し、|Del| や
   |BackSpace| を押して不要なデータを消去してから入力する
#. |Enter| を押して確定

Using the mouse
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. 対象セルをダブルクリック
#. セル内のデータの編集を開始したい位置にキャレットを移動
#. あるいは、クリックでセルを選択し、|FormulaBar| の :guilabel:`Input line` に
   キャレットを移動し、セル内のデータの編集を開始したい位置でクリック
#. 他のセルをクリックして選択解除して内容を確定

Paste Special function
----------------------------------------------------------------------

特殊貼り付け機能を使用すると、元のセルまたはセル範囲内のデータの選択した部分（書
式や数式の結果など）を別のセルに貼り付けることが可能だ。

Paste Special dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. セル一個またはセル範囲を選択
#. 次のいずれかでコピーコマンドを実行

   * |MenuBar| |EditCopyM|
   * |StandardToolbar| :guilabel:`Copy` ボタン
   * 右クリックメニュー :menuselection:`Cop&y`
   * キーバインド |Ctrl| + :kbd:`C`
#. 対象セル一個またはセル範囲を選択
#. 次のいずれかで |PasteSpecialDlg| を開く

   * |PasteSpecialM|
   * 右クリックメニュー |PasteSpecialC|
   * キーバインド |Ctrl+Shift| + :kbd:`V`
#. オプションを適宜指定
#. |OK|

:guilabel:`&Run immediately` をオンにするのは :guilabel:`Presets` グループにある
ボタンを使うときだ。

Paste Special options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Paste` グループから貼り付けたいクリップボード内容形式を選択する。

:guilabel:`Operations` ではセルを貼り付けるときに適用する操作を選択する。

* :guilabel:`None` は対象セルの内容を置き換える。
* :guilabel:`Add`, :guilabel:`Su&btract`, :guilabel:`Mult&iply`,
  :guilabel:`Divide` はクリップボードのセルの値を対象セルの値に加算、減算、乗
  算、除算をそれぞれ行う。クリップボードにコメントがある場合は、コメントを対象セ
  ルに追加する。

:guilabel:`Options` はいろいろ。

* :guilabel:`S&kip empty cells` がオンだと対象セルをクリップボードの空セルに置き
  換えない。オフだと空セルをゼロとして扱う。
* :guilabel:`Trans&pose` をオンにすると、クリップボードにある範囲の行、列を出力
  範囲の列、行としてそれぞれ貼り付ける。
* :guilabel:`As &Link` をオンにすると、セル範囲がリンクとして挿入される。原ファ
  イル内のセルに加えられた変更が対象ファイルで更新される。

  * 空のセルに加えられた変更が対象ファイルでも更新されるようにするには、
    :guilabel:`&All` がオンになっていることが必要。
  * 同一スプレッドシート内のシートをリンクすることも可能。
  * 他のファイルにリンクすると、DDE リンクが作成される。

:guilabel:`Shift Cells` はクリップボード内容が挿入されるときの対象セルに対するず
らし方を設定する。

Paste Only options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

テキスト、数値、数式だけを対象のセルまたはセル範囲にコピーしたい場合：

#. セル一個またはセル範囲を選択してコピーを実行
#. 対象セル一個またはセル範囲を選択
#. Paste Special コマンドを実行
#. :guilabel:`Text`, :guilabel:`Number`, :guilabel:`Formula` を選択

あるいは専用コマンドを実行する：

* :menuselection:`&Edit-->Paste &Special-->Paste &Only Text`
* :menuselection:`&Edit-->Paste &Special-->Paste Only &Numbers`
* :menuselection:`&Edit-->Paste &Special-->Paste Only &Formula`

Insert cell fields
----------------------------------------------------------------------

Calc でもフィールドが使える。日付、シート名、文書名にリンクしたフィールドをセル
に挿入可能。

#. セルを選択してダブルクリックし編集モードに入る
#. 右クリックメニューから関連コマンドを実行

   * :menuselection:`Insert &Field-->&Date`
   * :menuselection:`Insert &Field-->&Sheet Name`
   * :menuselection:`Insert &Field-->Document &Title`

文書名はファイルの |PropertiesDlg| の |DescriptionTab| で定義されたものではなく、
スプレッドシートの名前を指す。

.. admonition:: 利用者ノート

   そんなことはない。

|Ctrl| + |Shift| + |F9| 押しでスプレッドシートの保存時または再計算時にフィールド
が更新される。

Group and outline
======================================================================

データの概要を作成し、行または列を束ねることで、クリック一発で束ねられた行または
列を折りたたんだり、展開したりして表示状態を切り替えることが可能だ。

これらの表示 GUI はプラスまたはマイナス記号で示され、行または列の表示状態を切り
替える。ただし、束同士が入れ子になっている場合は、GUI に番号ボタンがあるので、入
れ子になっている束の異なる階層を隠すことが可能だ。

Grouping
----------------------------------------------------------------------

行や列を括る方法：

#. スプレッドシートで括りたいセルを選択
#. :menuselection:`&Data-->&Group and Outline-->&Group...` または |F12| で
   :guilabel:`Group` ダイアログボックスを開く
#. :guilabel:`&Rows` または :guilabel:`&Columns` を選択
#. |OK| を押す

括られた行の左または列の上に |UI| が表示される。

Hiding details
----------------------------------------------------------------------

行または列の詳細（シート上の表示）を隠すには、次のいずれかを実行する：

* 当該 GUI のマイナスボタンをクリック
* 括られているセル一つを選択して |MenuBar| から :menuselection:`&Data-->&Group
  and Outline-->&Hide Details` を実行

対象行または列が隠され、GUI のマイナスボタンがプラスボタンに変化する。

Showing details
----------------------------------------------------------------------

行または列の隠れているグループの詳細を表示するには、次のいずれかを実行：

* 当該 GUI のプラスボタンをクリック
* 隠れている部分を挟む両側のセルを選択して |MenuBar| から
  :menuselection:`&Data-->&Group and Outline-->&Show Details` を実行

隠れていた対象行または列が現れる。GUI のプラスボタンがマイナスボタンに変化する。

Ungrouping
----------------------------------------------------------------------

行グループまたは列グループを解散する方法：

#. 行グループまたは列グループが隠れていないようにする
#. グループ内のセル一つをクリック
#. |MenuBar| から :menuselection:`&Data-->&Group and Outline-->&Ungroup...` を実
   行するか |Ctrl| + |F12| を押す
#. 場合によっては :guilabel:`Ungroup` ダイアログが開き、ここで :guilabel:`&Rows`
   か :guilabel:`&Columns` を指定する

入れ子グループがある場合、最後に作成されたグループしか解散されない。

AutoOutline
----------------------------------------------------------------------

選択したセル範囲に数式や参照が含まれている場合、Calc は自動的に選択範囲を概略化
できる。本文の例では値の列が左から三つ連続して、四列目でそれらの和を取る構造が二
度続いている。この連続した三列二つが自動的に束ねられるということだ。

AutoOutline 機能を適用するには |MenuBar| :menuselection:`&Data-->&Group and
Outline-->&AutoOutline...` を実行する。

Removing
----------------------------------------------------------------------

:menuselection:`&Data-->&Group and Outline-->&Remove AutoOutline...` を実行
する。

Filtering
======================================================================

   A :dfn:`filter` is a list of conditions that each entry has to meet to be
   displayed.

三種類ある：

* Standard
* AutoFilter
* Advanced

Applying a standard filter
----------------------------------------------------------------------

標準絞り込みは AutoFilters よりも複雑で、AND 演算と OR 演算を組み合わせて最大八
つの絞り込み条件を設定可能。主に数値に有効なフィルターだが、テキストにも使えるも
のがある。

#. セル範囲を選択
#. :menuselection:`&Data-->More &Filters-->&Standard Filter...` 実行
#. 判定条件と絞り込みオプションを指定
#. |OK| を押す

指定した絞り込み条件とオプションに合致する登録項目が表示される。

|StandardFilterDlg| では全体的な絞り込み条件を形成するために結合される条件を定義
する。各絞り込み条件は論理演算子の方、フィールド名、論理条件、値を示すことによっ
て指定する。

Applying an AutoFilter
----------------------------------------------------------------------

AutoFilter ではデータ列の最上行にドロップダウンリストを追加し、表示行を選択可能
にする。この一覧には選択されたセル内の一意の項目が字句順に配列されて表示される。

AutoFilter は最初にデータベース範囲を定義しなくても、複数のシートで使用可能。

#. スプレッドシートのセル範囲をクリックする。同じシートに AutoFilter を複数適用
   する場合は、まずデータベース範囲を定義してから、その範囲に対して AutoFilter
   を適用する。
#. 次のいずれか：

   * |MenuBar| :menuselection:`&Data-->Auto&Filter` 実行
   * |StandardToolbar| 内 :guilabel:`AutoFilter` 図像クリック
   * キーバインド |Ctrl| + |Shift| + :kbd:`L`
#. 絞り込み基準として設定したい値を含む列の▼ボタンをクリック
#. 値を選択するか、検索項目欄に条件として使用する文字列を入力する。
#. :guilabel:`OK`

* AutoFilter の影響を受ける行は番号が青色で表示される。
* 絞り込み条件が作成された列にはドロップダウンリスト▼が青色で表示される。

Filtering by color
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

関心のある列のセルで使用されている背景色や文字色でデータを絞り込める。

* ドロップダウンリストから :menuselection:`Filter by Color-->Background Color`
  にこの列内の背景色一覧が現れる。選択色と合致するセルを含む行が表示される。
* :menuselection:`Filter by Color-->Font Color` も同様に機能する。

Filtering by condition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:menuselection:`Filter by Condition-->` 以下にある絞り込み項目は次のとおり：

* :menuselection:`Empty` は空セルの行のみを表示するように絞り込む。
* :menuselection:`Not Empty` は中身のあるセルの行のみを表示。
* :menuselection:`Top 10` は上位十位の値のセルを持つ行を表示する。

  * 値が一意である場合、十行も表示されない。
  * 値が一意でない場合、十行以上表示されることがある。
* :menuselection:`Bottom 10` はその下位十位版。
* :menuselection:`Standard Filter...` は |StandardFilterDlg| を開く。

Applying an advanced filter
----------------------------------------------------------------------

スプレッドシートの空白領域に絞り込み要件を自分で入力し、専用ダイアログボックスで
参照して絞り込みを適用するという使い方をする。|Calc14| 参照。

Sorting records
======================================================================

並び替えは絞り込みの後に行うのが便利だ。

また、新しい情報を表に追加するときにも、並べ替えは役に立つ。表が長い場合、適切な
場所に行を追加するよりも、表の一番下に新しい情報を追加する方が簡単なことが多い。
情報を追加したら、登録項目を並べ替えて表を更新すればよい。

Sort dialog
----------------------------------------------------------------------

ダイアログボックスの開き方と指定方法：

#. 並べ替えるセル、行、列を選択する。
#. 次のいずれかを実行：

   * |MenuBar| から |SortM| を実行
   * |StandardToolbar| :guilabel:`Sort` 図像をクリック
#. |OptionsTab| で行と列のどちらを並び替えるかなどの選択肢を決める。
#. |SortCriteriaTab| でドロップダウンリストから基準を選択する。
#. :guilabel:`&Ascending` か :guilabel:`&Descending` を選択
#. その他
#. |OK| を押す

Sort options
----------------------------------------------------------------------

:guilabel:`Case &sensitive` をオンにするとアジア言語については特別な処理が施され
る。本書の囲み記事参照。

:guilabel:`&Enable natural sort` をオンにすると文字列 A1, A2, A3, A4, A5, A6,
..., A19, A20, A21 のような配列を辞書式に並び替えることから避ける。

:guilabel:`&Copy sort results to` は並べ替えられたデータを指定セル範囲にコピーす
る。並べ替えられたデータを表示したい名前付きセル範囲を選択するか、入力欄にセル範
囲を入力する。

Quick sort
----------------------------------------------------------------------

スプレッドシートの列にテキスト書式のヘッダーがある場合は次のコマンドが使える：

* :menuselection:`&Data-->Sort &Ascending`
* :menuselection:`&Data-->Sort Descend&ing`

AutoFilter が適用済みの場合、そこの :menuselection:`Sort Ascending` や
:menuselection:`Sort Descending` を使える。もう一つ、:menuselection:`Sort by
Color` メニューも使える。:menuselection:`Filter by Color` の並び替え版だと考えら
れる。

Find and replace
======================================================================

Calc には文書内のテキストを検索する方法として、

* ツールバー :guilabel:`Find` と
* |Find&ReplaceDlg|

がある。ツールバーは素早く簡単に使えるが、ダイアログボックスを使うよりも機能が制
限される。

Find toolbar
----------------------------------------------------------------------

#. ツールバーを表示する。次のいずれかを実行：

   * :menuselection:`&View-->&Toolbars-->&Find`
   * :menuselection:`&Edit-->&Find...`
   * キーバインド |Ctrl| + :kbd:`F`

   このツールバーは通常、メインウィンドウの左下に繋留している。これを解除して移
   動してもよい。
#. :guilabel:`Find` 欄に検索語をタイプする。
#. 検索精度を上げるには次のオプションを使え。

   * :guilabel:`Match Case`
   * :guilabel:`Find All`
   * :guilabel:`Formatted Display`
#. :guilabel:`Find Next` または :guilabel:`Find Previous` 図像をクリック。同じ用
   語の他の出現箇所を検索するには図像をクリックし続けろ。

Find and Replace dialog
----------------------------------------------------------------------

|Find&ReplaceDlg| の開き方は次のどれでもよい：

* |MenuBar| :menuselection:`&Edit-->Find and Rep&lace...` を実行
* |StandardToolbar| :guilabel:`Find and Replace` 図像をクリック
* キーバインド |Ctrl| + :kbd:`H`

Finding
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. :guilabel:`Find` 欄に検索条件を入力
#. その下にある基本オプションを指定
#. :guilabel:`Other &options` をクリックして検索絞り込みの数を増やしてもいい
#. :guilabel:`Find &Next` をクリックして検索条件の最初の項目を検索
#. さらに :guilabel:`Find &Next` をクリックして次の項目検索を繰り返す。

   もしくは :guilabel:`Find &All` をクリックして検索条件を含むセルすべてを検索す
   る。これらのセルはシート上で強調表示される。|SearchResultsDlg| が表示され、セ
   ル場所が一覧表示される。

Replacing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. :guilabel:`Find` 欄に検索条件を入力
#. その下にある基本オプションを指定
#. :guilabel:`Re&place` 欄に置換内容を入力
#. :guilabel:`Other &options` をクリックして検索絞り込みの数を増やしてもいい
#. 合致するセルを一つずつ進み、内容を置き換えるかどうかを選択する：

   #. :guilabel:`Find &Next` をクリックして検索条件の最初の項目を検索
   #. 必要に応じて :guilabel:`&Replace` してセル内容を :guilabel:`Re&place` 欄の
      内容に置き換える。
   #. 必要なだけこれを繰り返す。

   あるいは、検索条件を一つ一つ止めずに、すべてのものを検索して置換するには
   :guilabel:`Replace A&ll` をクリックする。|SearchResultsDlg| が表示され、影響
   を受けるセルが一覧表示される。

.. admonition:: 読者ノート

   本書の囲み記事の記述からすると、:guilabel:`Replace A&ll` 操作を完全に undo す
   るのに、出現数だけ undo コマンドを実行しないとダメらしい。

Find and Replace options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`&Find` 区画で気をつけるオプション：

* :guilabel:`For&matted display` は説明が難しい。例えばシート上は ``1,400`` と表
  示されているセルがあるとする。しかし桁区切りのカンマが書式によるものである場
  合、これをオンにすると、検索欄に文字通りに ``1,400`` と入力した場合に検索ヒッ
  トするようになる（そうでない場合は ``1400`` でヒットする）。
* :guilabel:`&Entire cells` をオンにすると、検索テキストと同じ内容のセルを検索す
  る。

:guilabel:`Other &options` 区画で気をつけるオプション：

* :guilabel:`C&urrent selection only` をオンにすると、選択テキストか選択セルしか
  検索しに行かない。
* :guilabel:`Cell st&yles` をオンにすると指定したスタイルであるセル内容を検索する。

  * :guilabel:`&Find` ドロップダウンリストからスタイルを選択
  * 置換スタイルを指定するには :guilabel:`Re&place` ドロップダウンリストから
* :guilabel:`Re&gular expressions` をオンにすると正規表現での検索が有効になる。
  後述。
* :guilabel:`S&imilarity search` をオンにすると :guilabel:`&Find` 欄のテキストに
  類似する語を検索する。

  :guilabel:`Similarities...` ボタンを押して、:guilabel:`Similarity Search` ダイ
  アログボックスを開く。ここにある文字数指定が類似検索に対する引数のようだ。
* :guilabel:`Search in` ドロップダウンリストでは :guilabel:`Formulas`,
  :guilabel:`Values`, :guilabel:`Comments` のいずれかを選択し、指定した文字列を
  検索する。

|OptionsDlg| |LanguagesPage| の指定によっては他にも選択肢が現れる。日本語の場合
は :guilabel:`Sounds like (&Japanese)` というチェックボックスと詳細設定ダイアロ
グボックスが使える。

.. admonition:: 利用者ノート

   |UI| を英語にしていると詳細設定ダイアログボックスの各項目が何がなんだかわから
   ないことに注意。

Search Results dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All 系を実行すると開くダイアログボックス。処理結果を要約する。

:guilabel:`Show this dialog` をオフにすると、今後 All 系を実行してもこのダイアロ
グボックスは開かない。|OptionsDlg| |CalcViewPage| :guilabel:`Summary on search`
をオフにするのと同じだ。

Searching and filtering with regular expressions
======================================================================

Calc は `International Components for Unicode (ICU)
<https://unicode-org.github.io/icu/userguide/strings/regexp.html>` のオープン
ソース正規表現パッケージを利用している。

正規表現が登場するのは次の三箇所だ：

* :menuselection:`&Edit-->Find and Rep&lace...`
* :menuselection:`&Data-->More &Filters-->&Standard Filter...`
* :menuselection:`&Data-->More &Filters-->&Advanced Filter...`
* 関数 (|Calc08|)

関数の多くで検索条件に正規表現を使用できる。これらは |OptionsDlg|
|CalculatePage| 内 :guilabel:`Enable r&egular expressions in formulas` がオンの
場合にのみ正しく動作する。また、:guilabel:`Search criteria = and <> must apply
to &whole cells` をオンにし、数式内の検索条件がセルの内容全体に一致するようにす
ることが推奨されている。

本書の例その一は Brigitte に対するミススペリングを置換修正するものだ。誤り方が複
数あるが、いずれも最初の三文字だけは共通しているのでそれを利用している。ダイアロ
グボックスの指定は次のとおりだ：

* :guilabel:`&Find`: :regexp:`^Bri.*`
* :guilabel:`Re&place`: ``Brigitte``
* :guilabel:`Re&gular expressions`: オン

本書の例その二では北と東の地域から、テニスとゴルフの区分に関連するデータのみを表
示する。|StandardFilterDlg| の指定の前半は次のとおりだ。これらを :guilabel:`AND`
で接続する：

.. csv-table::
   :delim: @
   :header: Field name,Condition,Value
   :widths: auto

   :guilabel:`Category` @ :guilabel:`=` @ :regexp:`Tennis|Golf`
   :guilabel:`Region` @ :guilabel:`=` @ :regexp:`North|East`

後半では、当然ながら :guilabel:`Regular &expressions` をオンにする。これら二つの
例のシート内容：

.. csv-table::
   :delim: |
   :header: Date,Sales Value,Category,Region,Employee
   :widths: auto

   2024-02-21 | $410 | Tennis | North | Kurt
   2024-03-21 | $1,508 | Golf | East | Bridget
   2024-04-21 | $2,340 | Sailing | South | Brigid
   2024-05-21 | $4,872 | Tennis | East | Brigitte
   2024-06-21 | $3,821 | Tennis | South | Fritz
   2024-07-21 | $2,623 | Tennis | East | Fritz
   2024-08-21 | $3,739 | Golf | South | Fritz
   2024-09-21 | $4,195 | Golf | West | Brigid
   2024-10-21 | $2,023 | Golf | East | Bridget
   2024-11-21 | $1,804 | Tennis | West | Bridget
   2024-12-21 | $1,858 | Tennis | North | Kurt
   2025-01-21 | $579 | Sailing | West | Brigid
   2025-02-21 | $4,842 | Golf | North | Brigid
   2025-03-21 | $2,827 | Tennis | East | Bridget

例その三では、関数呼び出しで正規表現を与える。|Calc08| に正規表現を利用可能な関
数一覧がある。

.. csv-table::
   :delim: |
   :header: Product Name,Sales,Revenue
   :widths: auto

   Pencil | 20 | 65
   Pen | 35 | 85
   Notebook | 20 | 190
   Book | 17| 180
   Pencil case | 12 | 96
