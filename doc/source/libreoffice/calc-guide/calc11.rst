======================================================================
Calc Guide Chapter 11, Linking Data ノート
======================================================================

.. include:: ./calc-inc.txt

.. contents:: 章見出し
   :local:
   :depth: 3

Using multiple sheets
======================================================================

Why use multiple sheets?
----------------------------------------------------------------------

|Calc01| ではスプレッドシートにおける複数シートの概念を紹介した。複数シートは情
報整理に役立つ。これらのシート同士をに何らかの関係が定義されれば Calc の能力が完
全に発揮される。次の場合を考える：

.. container::

   John は個人的な財務状況を把握するのに苦労している。彼は銀行口座をいくつか持っ
   ているが、その情報は散乱しており、整理されていない。すべてを一度に見ることが
   できるようになるまで、自分の財務をうまく把握することができない。

   これを解決するために、John は LibreOffice Calc で財務を追跡することにした。
   John は Calc が簡単な数学計算ができることを知っており、口座の残高を一度に確認
   できるように概要シートを設定したい。

.. note::

   今さらだが、MS Excel はワークブックと呼ぶものを Calc はスプレッドシートと呼
   ぶ。Excel も Calc もシートとワークシートという術語を用いる。

Setting up multiple sheets
----------------------------------------------------------------------

スプレッドシートに複数のシートを設定する方法は |Calc01| で学習した。

Identifying sheets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

新規スプレッドシートを開くと `Sheet1` という名前のシートが一枚含まれる。この挙動
を |OptionsDlg| |CalcDefaultsPage| で変更可能だ：

* 新規文書が含むシートの数
* 新規シートの接頭辞

スプレッドシートの下部にあるタブを使ってシートを管理する。

Inserting new sheets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

複数ある方法のどれを選ぶかは利用者次第だ。

* シートタブ左の :guilabel:`+` をクリックする
* |MenuBar| から |InsertSheetM| を実行する
* |MenuBar| から :menuselection:`&Sheet-->Insert Sheet at End` を実行する
* |MenuBar| から :menuselection:`&Sheet-->Insert Shee&t from File...` を実行する
* シートタブ右クリックメニューから |InsertSheetC| を実行する

これらの方法のうち |InsertSheetDlg| が開くものについては、次のオプションを使って
もよい：

* 新規シートの挿入位置を現在シートの前か次のいずれにするか
* 新規シートの枚数
* 新規シートがただ一枚の場合に限り、新規シートの名前

または :guilabel:`Append Sheet` ダイアログボックスが開くものについては、新規シー
トの :guilabel:`&Name` を既定の名前以外のものに指定可能だ。

----

John のスプレッドシートにはシートが六つ必要である。また、これらのシートにそ
れぞれ口座の名前を付けたい：

#. `Summary`
#. `Checking Account`
#. `Savings Account`
#. `Credit Card 1`
#. `Credit Card 2`
#. `Car Loan`

単一シートを持つスプレッドシートを新規作成した後、次のいずれかで達成したい：

* 新規シートを五枚入れし、六枚すべてのシート名を変更する。
* 既存シートの名前を変更し、五シートを新規に一枚ずつ入れる。

シートを入れて後で名前を変更する手順：

#. 正しいシートタブが選択されていることを確認し、|InsertSheetDlg| を開く。
#. 新しいシートの位置を選ぶ。この例では :guilabel:`&After current sheet` を使う。
#. :guilabel:`&New sheet` を選び、:guilabel:`N&o. of sheets` の後に 5 と入力する。
   複数のシートを入れるため :guilabel:`Na&me` 欄は使用不能だ。
#. |OK| を押してシートを入れる。

シートの名前を変更する以降の手順については :ref:`calc11-anchor-renaming` を見ろ。

シートを入れると同時に名前を付ける手順：

#. :ref:`calc11-anchor-renaming` にあるようにして既存のシートの名前を `Summary`
   に変更する。
#. 正しいシートタブが選択されていることを確認し、|InsertSheetDlg| を開く。
#. 新しいシートのシートタブの位置を選ぶ。:guilabel:`Before current sheet` か
   :guilabel:`&After current sheet` の使えるもの。
#. :guilabel:`&New sheet` を選び、:guilabel:`N&o. of sheets` の後に 1 と入力する。
   :guilabel:`Na&me` 欄が使用可能になる。
#. :guilabel:`Na&me` 欄にこの新しいシートの名前、例えば `Checking Account` と入
   力する。
#. |OK| を押してシートを入れる。
#. 新規シートそれぞれに `Savings Account`, `Credit Card 1`, `Credit Card 2`,
   `Car Loan` という名前を付ける工程を繰り返す。

Inserting sheets from a different spreadsheet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

さらに、|InsertSheetDlg| には :guilabel:`&From file` オプションがある。シートを
追加する手順は：

#. |Browse| を押すとファイルダイアログボックスが開く
#. 別の Calc ファイルなどを選択する
#. シート一覧が現れる
#. 追加するシートを選択する

:guilabel:`&Link` をオンにすると、参照様式がシートのコピーではなくリンクになる。

* 他のスプレッドシートから生きたデータを取り込むことを実現する。
* リンクを更新するには |MenuBar| から |EditLinksM| を実行する。
* 自動更新にしたければオプション設定だ。|CalcGeneralPage| の :guilabel:`Update
  links when opening` ラジオボタングループを好みの項目に変えろ。

信頼できるファイルの場所を定義するには |OptionsDlg| |SecurityPage| で
:guilabel:`Macro Security...` ボタンを押してダイアログボックスを開く。
:guilabel:`Trusted Sources` タブをクリックして下の欄を埋める。これはスプレッド
シートでマクロを使用する場合に有用だ。マクロについては |Calc13| を見ろ。照してく
ださい。

.. _calc11-anchor-renaming:

Renaming sheets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

シートには意味がある名前を与えろ。既存シートの名前を変える方法：

* シートタブをダブルクリックする
* シートタブを |Alt| を押しながらクリックする
* シートタブ右クリックメニューから |RenameSheetC| を実行する
* メニューから :menuselection:`&Sheet-->Rename S&heet...` を実行する

以上のいずれの操作でも |RenameSheetDlg| が開く。ここで新しい名前を
:guilabel:`&Name` 欄に入力しろ。

シート名は空であってはならず、既存の名前と重複してはいけない。

.. note::

   次の文字は名前の最初または最後の文字としては使用不可：

   .. code:: text

      : \ / ? * [ ] '

.. tip::

   LibreOffice Calc のインストールによっては、|Alt| を押しながらシート名をクリッ
   クして新しい名前を直接入力することが可能だ。

   .. admonition:: 読者ノート

      この操作はオススメ。ダブルクリックだとポップアップが出るぶん遅い。

----

ここまでの記述により、John は六シートを準備できたとする。

次に勘定元帳を設定する。これは単純な要約で、前回の残高に今回の取引額を加えたもの
である。引き出しの場合は、残高が少なくなるように、現在の取引を負の数で入力する。
基本的な元帳を Figure 8 に示す。

.. admonition:: 読者ノート

   A2:C6 が次のようになっている：

   .. csv-table::
      :delim: @
      :header: Description, Amount, Balance
      :widths: auto

      Opening Balance @ $75.00 @ $75.00
      Pay @ $425.00 @ $500.00
      Groceries @ -$75.00 @ $425.00
      Cable Bill @ -$445.95 @ $380.05

この元帳は `Checking Account` シートに設定されている。総残高は升目 F3 で合計され
る。数式は ``=C3+SUM(B4:B46)`` だ。これは升目 C3 の開始残高と、その後のすべての
取引を合計したものだ。

Referencing other sheets
----------------------------------------------------------------------

他のシートの升目を参照する方法は二つはある：

* キーボードを使って数式を直接入力する
* マウスを使って入力する

----

`Summary` シートには他の各シートの残高を表示する。Figure 8 の例を五つの勘定科目
の各シートにコピーする。現在の残高はシートそれぞれの升目 F3 になる。

Creating the reference with the mouse
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Summary` シート上で五つの勘定残高の場所を設定し、升目参照をどこに置くかわかるよ
うにする。Figure 9 は `Balance` 列が空白の `Summary` シートだ。`Checking Account`
に対する参照を升目 B3 に置きたい。

.. admonition:: 読者ノート

   `Summary` シートの A2:B7 は次のような構成になる：

   .. csv-table::
      :delim: @
      :header: Account, Balance
      :widths: auto

      Checking Account @
      Savings Account @
      Credit Card 1 @
      Credit Card 2 @
      Car Loan @

   以下、`Balance` 列を数式で埋めていく。

升目 B3 に升目参照を作成するには升目を選択して次のようにする：

#. |FormulaBar| の入力行の横にある :guilabel:`=` ボタンをクリックする。
   |FormulaBar| の図像が変わり、|InputLine| に等号が現れる。
#. 参照する升目を含むシートのシートタブをクリックする。この場合は `Checking
   Account` シートだ。
#. `Checking Account` シートの升目 F3 をクリックする。|InputLine| に
   ``$'Checking Account'.F3`` が現れ、選択セルは色のついた枠で囲まれる。
#. |FormulaBar| の |InputLine| にある |FormulaAccept| をクリックするか |Enter|
   を押して終了する。

以上で `Summary` シートの升目 B3 に金額が現れる。

Creating the reference with the keyboard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

セル参照は部分が二つある。ドル記号が前置されたシート名と升目参照だ。これらはピリ
オドで区切られていることに気をつけろ。Calc の既定動作はドル記号を付けて絶対シー
ト参照を形成し、相対升目参照を与えるものだ。

.. note::

   シート名は空白文字を含むため単一引用符で囲み、必須ピリオドは常に引用符の外側
   に置く。

したがって、`Savings Account` の升目参照を単に中に入力すればよい。残高が普通預金
シートの同じ升目である F3 にあると仮定すると、升目参照は

.. code:: text

   =$'Savings Account'.F3

となる。

Protect spreadsheet structure
----------------------------------------------------------------------

文書のシート構成に満足したら、次のシート操作を禁止したい：

* シートを追加
* シートを削除
* シートの順序を変更
* シートの名前を変更

このためには、メニューの :menuselection:`&Tools-->Protect &Spreadsheet
Structure...` を実行して構造を固定する。パスワード入力ダイアログボックスが開く。
パスワードを適当に入力して |OK| を押す。上記の操作が不可になる。

シート操作を解禁するにはこのコマンドを再度実行し、指定のパスワードを入力して
|OK| を押す。

Referencing other documents
======================================================================

.. container::

   John は家族の口座情報を自分のまとめとは別のスプレッドシートファイルに保存する
   ことにした。幸いなことに、Calc は異なるファイルをリンクすることができる。手順
   は単一スプレッドシートの異なるシートについて説明したのと同じで、どのファイル
   にシートがあるかを示すためにもう一手間かける。

Creating the reference with the mouse
----------------------------------------------------------------------

マウスを使って参照を作成するには、スプレッドシートを両方開いておく必要がある。

#. 数式を入力する升目を含むほうのスプレッドシートに切り替える。
#. 数式を入力する升目を選択する。
#. |FormulaBar| の左にある :guilabel:`=` 図像をクリックする。
#. もう一方のスプレッドシートに切り替える。
#. 参照先シートを選択し、参照先セルを選択する。この時点で |Enter| を押せば確定。

   John の場合は `Savings Account` シートを選択して F3 をクリックする。
#. 参照元シートに切り替えて |FormulaBar| の左にある |FormulaAccept| をクリックす
   る。

以上の手順により、升目の内容が適切な参照式になる。

|FormulaBar| の |InputLine| をよく見れば、参照の形式がよくわかるだろう。この行の
内容に基づいて、キーボードを使って参照を作成することができる。

Creating the reference with the keyboard
----------------------------------------------------------------------

参照元セルの内容として、参照先セルに対する参照式を直接入力すればいい。次のような
数式となるはずだ：

   :samp:`='file://{/path/to/ods}'#$'{SheetName}'.CellReference`

Using hyperlinks and URLs
======================================================================

スプレッドシート内から別の場所にジャンプするためにハイパーリンクを使用する。次の
ジャンプ先が実現可能だ：

* 現在のファイルの他の部分
* 別のファイル
* Web ページ

Relative and absolute hyperlinks
----------------------------------------------------------------------

ファイル内ハイパーリンクは相対パスまたは絶対パスのどちらかだ。

* 絶対リンクは対象が移動すると機能しなくなる。
* 相対リンクは開始位置と対象位置が相対的に変わると機能しなくなる。

|OptionsDlg| |LoadSaveGeneralPage| 以下にハイパーリンク保存方法関連オプション項
目が二つある。|URL| を相対的に保存するかどうかを指示する。

ファイルリンクには相対リンクを使うのがよい。相対リンクは作業中のファイルがリンク
先と同じドライブにある場合に限り可能。

相対ハイパーリンクを保存していても、ハイパーリンクは絶対アドレスで常に表示される。
この「絶対」アドレスは、ファイルを移動すると更新される。

.. tip::

   Calc は内部的に絶対パス名を使用するため、ハイパーリンク上にマウスポインターを
   置くと、ヘルプチップに絶対参照が表示される。完全なパスとアドレスは |HTML| エ
   クスポートの結果を表示するとき、|HTML| ファイルをテキストとして読み込むとき、
   テキストエディターで開くときにのみ表示される。

Creating hyperlinks
----------------------------------------------------------------------

スプレッドシートにハイパーリンクを挿入する方法は複数ある：

* |HyperlinkDlg| を開く。セルまたはセル内のテキストを選択し、またはキャレットを
  挿入位置に置き、

  * |MenuBar| から |InsertHyperlinkM| を実行するか、
  * キーバインド |Ctrl| + :kbd:`K` を押す。
* Navigator (|F5|) からハイパーリンクを挿入したい箇所（シートタブやセルなど）に
  項目をドラッグ＆ドロップする。
* ハイパーリンクを入れる場所に対象の |URL| を入力する。入力文字列をハイパーリン
  ク |URL| として Calc に自動認識させるには、|MenuBar| から
  :menuselection:`&Tools-->&AutoCorrect Options...` を実行して、ダイアログボック
  ス内の |OptionsTab| で :guilabel:`URL Recognition` をオンにする。

|HyperlinkDlg| を使用する場合、テキストまたはボタンのいずれかを選択できる。どち
らの場合も、表示されるテキストとリンク先 |URL| を異なるものにすることができる。

ハイパーリンクの色を変更するには、|OptionsDlg| |ApplicationColors| の次の項目の
色を指定しろ：

* `Unvisited links`
* `Visited links`

.. note::

   LibreOffice のアプリケーションすべてにおけるハイパーリンクの色が変更される。

ボタンのハイパーリンクはフォームコントロールの一種だ。他のフォームコントロールと
同様に、Design Mode でボタンを右クリックすることで、繋留・配置が可能だ。フォーム
の詳細については |Writer| を見ろ。

Opening hyperlinks
----------------------------------------------------------------------

ハイパーリンクからジャンプする方法は、ホットテキストの場合は：

* 左クリックか、または |Ctrl| を押しながら左クリックのいずれか
* 右クリックメニューから :menuselection:`&Open Hyperlink` を実行する

ことでジャンプする。左クリック絡みは |OptionsDlg| |SecurityPage| における
|SecurityOptions&WarningsDlg| での項目 :guilabel:`Ctrl-click required &to open
hyperlinks` のオンオフによってどちらの操作が有効であるかが決まる。

ボタンの場合は、Design Mode に入っていない場合には左クリックでジャンプ。Design
Mode へするには、次のいずれかのツールバーの :guilabel:`Design Mode` をオンにする：

* |FormControlsToolbar|
* |FormDesignToolbar|

Hyperlink dialog
----------------------------------------------------------------------

|HyperlinkDlg| を開く方法：

* |MenuBar| |InsertHyperlinkM| 選択
* |StandardToolbar| :guilabel:`Insert Hyperlink` 図像
* キーバインド |Ctrl| + :kbd:`K`

ダイアログの左側でハイパーリンク区分から一つを選択する。

:guilabel:`Further Settings` 区画がハイパーリンク区分すべてに用意されている。こ
れより上の区画にあるコントロールは、ダイアログの左側の区分のどれが選択されている
かによって異なる。

以下は Calc で使用される最も一般的な選択肢の要約だ：

:guilabel:`&Internet`
   :guilabel:`&URL`
      必要な Web アドレスを入力する。
   :guilabel:`Te&xt`
      使用者に表示されるテキストを指定する。ここに何も入力しない場合、リンクテキ
      ストは完全 URL またはパスになる。リンクが相対リンクでファイルを移動した場
      合、対象は変更されるがこのテキストは変更されないことに気をつけろ。
:guilabel:`&Mail`
   メールクライアントがインストールされている場合にのみ機能。

   :guilabel:`Re&cipient`
      受信者のメールアドレスを入力するか、ボタンを押してアクセスされる既存データ
      ベースからアドレスを選択する。
   :guilabel:`&Subject`
      メッセージの件名として使用するテキストを入力する。

   :guilabel:`Te&xt` 欄は :guilabel:`Further Settings` 区画内に設けられている。
   これらのハイパーリンクの機能は、上記の Internet ハイパーリンクと同じだ。
:guilabel:`&Document`
   :guilabel:`&Path`
      開くファイルのパスを指定する。同じスプレッドシート内の対象にリンクする場合
      は空白のままにする。フォルダー図像をクリックすると |OpenFileDlg| が開き、
      開く文書を指定可能。
   :guilabel:`Targ&et`
      オプションで、文書内の対象（特定のシートなど）を指定する。クロスヘア図像を
      クリックすると Navigator が開き、対象を選択することが可能。
:guilabel:`&New Document`
   :guilabel:`Edit &now` / :guilabel:`Edit &later`
      新しく作成した文書をすぐに編集するか、作成だけにするかを指定する。
   :guilabel:`&File`
      作成するファイル名を入力する。パス選択図像をクリックすると、ディレ
      クトリーピッカーダイアログが開く。
   :guilabel:`File &type`
      作成する文書の種類を選択する（テキスト文書、スプレッドシート、図面など）。

:guilabel:`Further Settings` 区画はすべてのハイパーリンク区分に共通する。ただし、
いくつかの選択肢はリンクの種類によって関連性が高く、Internet ハイパーリンクの場
合、この区画では :guilabel:`Text` オプションは省略される。

:guilabel:`F&rame`
   ハイパーリンクの開き方を決定する。Web ブラウザーで開く文書に適用される。選択
   肢は `_top`, `_parent`, `_blank`, `_self` だ。
:guilabel:`F&orm`
   リンクをテキストとして表示するか、ボタンとして表示するかを指定する。
:guilabel:`Te&xt`
   使用者に表示されるテキストを指定する。先ほどのものと同様。
:guilabel:`N&ame`
   |HTML| 文書に適用される。|HTML| コードの `NAME` 属性として追加されるテキスト
   を指定する。

Editing hyperlinks
----------------------------------------------------------------------

既存のホットテキストに対するハイパーリンクを編集する方法はいくつかある：

* ホットテキストを含むセルをクリックし、|InsertHyperlinkC| を実行するか、同等の
  操作を行う。
* ホットテキストを選択して右クリックメニュー |EditHyperlinkC| を実行する。

既存のボタンに対するハイパーリンクの場合、参照先を編集するにはスプレッドシートの
Form Design Mode が有効である必要がある。ボタンを選択した状態で：

* |InsertHyperlinkC| を実行するか、同等の操作を行う。
* 右クリックメニュー :menuselection:`Con&trol Properties...` を実行し、
  :guilabel:`&Label` にある参照先を表す文字列を変更する。

複数のハイパーリンクを編集する場合、すべてを編集するまで |HyperlinkDlg| を開いた
ままにしておくことが可能。適宜 |ApplyButton| を押せ。

ボタンのハイパーリンクを編集するには、Design Mode であるとして、ボタンを選択し、
右クリックメニューから |ControlPropertiesC| を選択する。Calc では |PropertiesDlg|
が開く。Label 欄を編集してボタンテキストを変更し、URL 欄を編集してリンクアドレス
を変更します。|PropertiesDlg| に |OK| はない。

Removing hyperlinks
----------------------------------------------------------------------

ホットテキストの場合は文字列を選択して右クリックメニューから |RemoveHyperlinkC|
を実行しろ。ボタンの場合は編集時と同じ。

Linking to external data
======================================================================

他の文書のデータをリンクとしてスプレッドシートに挿入可能。

.. |ExternalDataDlg| replace:: :guilabel:`External Data` ダイアログボックス

|ExternalDataDlg| を使用する方法と Navigator を使用する方法がある。ファイルに名
前付き範囲、データベース範囲、または名前付き表があり、リンクしたい範囲や表の名前
がわかっている場合は、|ExternalDataDlg| を使用するとすばやく簡単にできる。しか
し、ファイルに複数の範囲や表があり、そのうちの一つしか選択したくない場合、どれが
どれなのか簡単に判断できない。

Calc には外部給源からのリンクデータを含めるための他の方法が用意されている。例え
ば :ref:`calc11-anchor-linking` と :ref:`calc11-anchor-dde` を見ろ。

.. note::

   リンク先のファイルの保存場所によっては、更新処理が完了するまでに数分かかるこ
   とがある。

Using the External Data dialog
----------------------------------------------------------------------

   The :guilabel:`External Data` dialog inserts data from an |HTML|, Calc,
   |CSV|, or Microsoft Excel file into the current sheet as a link. Calc
   utilizes a Web Page Query import filter, enabling you to insert tables from
   |HTML| documents.

この操作をインポートと便宜上呼ぶことにする。インポートの手順は：

#. 外部データインポート先となる ods ファイルを開く
#. インポート先セル範囲の左上セルを選択する
#. メニューから :menuselection:`&Sheet-->E&xternal Links...` を実行

ここで |ExternalDataDlg| が開く。

* :guilabel:`URL of &External Data Source` に場所を入力するか、
* ドロップダウンリストから項目を選択するか、
* |Browse| からアクセスできるファイル選択ダイアログ

からインポート元を選択しろ。インポート元のデータ種別により、以降 |UI| の挙動が異
なる。

* |HTML| ファイルを選択した場合、本書参照。
* |CSV| ファイルを選択した場合、:guilabel:`Text Import` ダイアログボックスが現れ
  る。|Calc01| で述べられている手順に合流する。
* Calc または MS Excelファイルを選択した場合、インポート元に定義されている範囲名
  とデータベース範囲の一覧がダイアログの :guilabel:`&Available Tables/Ranges`
  に埋まる。挿入したい項目を選択しろ。

インポートにより、Navigator の :guilabel:`Linked areas` 欄に新しい項目が追加する。
このような項目を

* ダブルクリックするとシート内のリンクされたデータが強調表示される。
* マウスホバーするとツールチップにリンクされたデータのパスが表示される。

スプレッドシート内のすべての外部データリンクを一覧表示するには、|MenuBar| から
|EditLinksM| を実行する。|EditLinksDlg| が開く。一般には、一覧の一部が外部リンク
だ。

.. note::

   |EditLinksDlg| は |ExternalDataDlg| を使用して作成されていない他のリンクに関
   する情報を表示できる。

|ExternalDataDlg| を使用して作成されたリンクについては、|EditLinksDlg| でリンク
を選択して :guilabel:`&Modify...` ボタンを押すか、リンクをダブルクリックすること
で、再度ダイアログにアクセスできる。:guilabel:`&Break Link` ボタンを押し、選択し
たリンクを解除することを確認すると、以前リンクされていたデータがスプレッドシート
に埋め込まれる。:guilabel:`&Update` ボタンを押すと対象ファイル内のリンクされた
データが元ファイル内のものと一致するように更新される。

.. note::

   |EditLinksDlg| の :guilabel:`Status` 列には、|ExternalDataDlg| を使用して作成
   されたリンクの場合、`Manual` がつねに表示される。この欄に表示される状態は
   |ExternalDataDlg| の :guilabel:`&Update every` 設定を反映したものではない。

Using the Navigator
----------------------------------------------------------------------

Navigator または |Sidebar| |NavigatorDeck| を使用して外部データをリンクすること
もできる。Navigator については |Calc01| を見ろ。

Navigator を使用して外部データへのリンクを作るには：

#. インポート先スプレッドシートを開く。
#. インポート元ファイルを開く（上述のファイル形式が有効）。
#. インポート先で Navigator を開く。|F5| 押しが早い。
#. Navigator 下部のドロップダウンリストからインポート元を選択する。
#. 必要な範囲名またはデータベース範囲項目を選択し、Navigator からインポート先
   シートにドラッグして、データ範囲の左上の升目に移動する。
#. Navigator で、Drag Mode メニューの :menuselection:`Insert &as Link` を選択す
   る。

   範囲名を右クリックし、コンテキストメニューから必要なオプションを選択すること
   で、ドラッグモードを変更することもできる。

   .. tip::

      Navigator の Drag Mode 図像が変わり、現在選択されているドラッグモードが反
      映される。

#. `Range names` または `Database ranges` から必要登録項目を選択し、Navigator か
   ら対象文書へ、データ範囲の左上の升目にドラッグする。
#. Navigator 下部のドロップダウンメニューで対象文書を再選択。`Range names` 横で
   はなく、`Linked areas` 横に :guilabel:`+` 図像が表示される。これをクリックす
   ると、原文書からドラッグされた項目が表示される。

How to find the required data range or table
----------------------------------------------------------------------

Calc の Web Page Query インポートフィルターは Web ページから給源順にデータ範囲
（表）を表示する。さらに範囲名を二つ作成する：

* `HTML_all`: HTML ファイル全体を指定
* `HTML_tables`: HTML ファイル内の表すべてを指定

`TABLE` 要素に `ID` 属性がある場合、連番を付けた範囲と共に、それらの属性値が範囲
名一覧に表示される。

そういう属性値がないインポート元については強調表示機能頼みになる。

Calc で開いた原文書に移動する。Navigator で範囲名をダブルクリックするとその範囲
がシート上で強調表示される。Figure 34 の例は
<https://en.wikipedia.org/wiki/List_of_best-selling_albums> から抽出した、レコー
ド音楽のベストセラーアルバムの世界年別表だ。

|FormulaBar| が表示されている場合、範囲名は左端の :guilabel:`Name` にも表示され
る。範囲名はドロップダウンリストで選択し、ページ上で強調表示することができる。

.. admonition:: 読者ノート

   本書の例を真似ても掲載されている画像のようには現在、ならない。

.. _calc11-anchor-linking:

Linking to registered data sources
======================================================================

さまざまなデータベースと Calc 文書をリンク可能だ。それにはまず、LibreOffice に
データ給源を登録する必要がある。登録とは LibreOffice にデータ給源の型とファイル
がとこに位置するかを知らせることだ。これを行う方法はデータ給源が .odb 形式のデー
タベースであるかどうかによって異なる。

ODB ファイルを登録する手順は |OptionsDlg| を用いる：

.. |CreateDatabaseLinkDlg| replace:: :guilabel:`Create Database Link` ダイアログボックス

#. :menuselection:`LibreOffice Base-->Databases` ページを見る。
   :guilabel:`Registered databases` 一覧を確認する。
#. :guilabel:`&New...` ボタンを押す。|CreateDatabaseLinkDlg| を開く。してパスと
   名前の対応を登録する。
#. データベースファイルの場所を入力するか、ドロップダウンリストからデータベース
   ファイルを選択するか、|Browse| を押して |OpenFileDlg| を開き、データベース
   ファイルを選択する。
#. データベースの登録名として使用する名前を入力し、|OK| 押す。データベースが登録
   済みデータベース目録に追加され、LibreOffice は登録名を使用してデータベースに
   アクセスする。

.. note::

   |CreateDatabaseLinkDlg| の |OK| は :guilabel:`&Database file` 欄と
   :guilabel:`Registered &name` 欄の両方が入力されている場合に有効になる。

ODB ファイル以外のデータ元の登録手順：

#. :menuselection:`&File-->&New-->Data&base...` を実行
#. :guilabel:`Connect to an &existing database` を選択
#. ドロップダウンリストから所望の項目を選択、|Next| を押す。

この後はデータベースの種別により異なるが、最後に |Finish| を押す。

データ給源が登録されると、Calc を含むどの LibreOffice アプリケーションでも使用可
能になる。

.. todo::

   データベース利用ノートと関連するので、試す価値はある。

Viewing data sources
----------------------------------------------------------------------

現在スプレッドシートで利用可能なデータ元を閲覧する方法：

:menuselection:`&View-->&Data Sources...` (|Ctrl+Shift| + |F4|) を実行する

これにより Data Sources 窓がスプレッドシート上部に現れる。この窓は次の四つの部分
からなる。

.. |TableDataToolbar| replace:: :guilabel:`Table Data` ツールバー

|TableDataToolbar|
   |TableDataToolbar| は既定で Data Sources ウィンドウの上部に配置されている。
Data Source Explorer 窓
   Data Source Explorer は既定では Data Sources 窓の左側、|TableDataToolbar| の
   下にある。

   Data Source Explorer には登録されているデータベースの目録が表示される。

   各データベースを表示するには、データベース名の左にある展開アイコンをクリック
   する。同様に、`Queries` の左側にある展開アイコンをクリックすると、選択した
   データベース内の個々の質問を表示できる。表名をクリックすると、その表に保持さ
   れているすべての登録項目が表示される。
選択表の登録項目（表の各行）
   選択表のデータ登録項目は Data Sources 窓の右側、|TableDataToolbar| の下
   の領域に表示される。

   この領域により多くの列を表示するには、|TableDataToolbar| の
   :guilabel:`Explorer On/Off` 図像をクリックしてData Sources Explorer を隠す。
   再度クリックすると現れる。

   データ項目の下には案内棒があり、選択中の登録項目が何であるかと登録項目の総数
   が表示される。これには次のボタン群がある：

   * First record
   * Previous record
   * Next record
   * Last record
   * Add new record
   * 利用可能な列すべてが可視領域に収まらない場合は横スクロールバー、利用可能な
     登録項目すべてが可視領域に収まらない場合は、縦スクロールバーがそれぞれ現れ
     る。
表示切り替えハンドル（最下部の細い矩形）
   Data Sources 窓の中央下部には、窓全体を隠したり見せたりするコントロールがあ
   る。

.. admonition:: 読者ノート

   手許のデータベースファイルが全部破損していて機能を試していない。

Editing data sources
----------------------------------------------------------------------

Data Sources 窓で編集できるのは、登録済みのデータ給源のみ。

編集可能なデータ給源では登録項目の編集、追加、削除が可能だ。編集内容を保存できな
い場合は LibreOffice Base でデータベースを開き、そこで編集する必要がある。また、
列を隠したり、表示に変更を加えたりすることも可能だ。

Launching Base to work on data sources
----------------------------------------------------------------------

右クリックメニューから |EditDatabaseFileC| を実行すると LibreOffice Base が起動
する。データベース、`Tables`, 表名、`Queries`, 質問名を右クリックする。Base に入
ると、表、質問、フォーム、報告書を編集、追加、削除することが可能だ。

Base の使い方については |Guide| または |Base| を見ろ。

Using data sources in Calc spreadsheets
----------------------------------------------------------------------

Data Sources 窓の右側に表示されている表のデータは Calc 文書に配置可能だ。

Data Sources 窓で単一升目、単一行、複数行のどれかを選択し、データをシートにド
ラッグ＆ドロップすることが可能だ。マウスボタンを放した位置にデータが入る。行の場
合、Calc は追加データの上に列見出しも含める。シートに追加するデータの行を選択す
るには：

#. 選択したい最初の行の左にある灰色箱をクリックする。その行が強調表示される。
#. 隣接する複数の行を選択するには |Shift| を押しながら、所望の行最後の灰色箱をク
   リックする。
#. 複数の別々の行を選択するには |Ctrl| を押しながら各行を選択する。
#. すべての行を選択するには、左上隅の灰色箱をクリックする。

別の方法として、|TableDataToolbar| の :guilabel:`Data to Text` 図像を使用すると、
入れたデータの上に列見出しも入る：

#. データの左上に表示したいシートの升目を列名も含めてクリックする。
#. 前の段落で説明したようにして、シートに追加したいデータの行を選択する。
#. |TableDataToolbar| の :guilabel:`Data to Text` 図像をクリックしてデータをシー
   トの升目に入れる。

データ給源の列見出し（フィールド名）をシートにドラッグして、個々の登録項目を一度
に表示、編集するフォームを作成することも可能だ。手順は次のとおり：

#. 使用したいフィールド名を含む列の上部にある灰色箱を、シートで登録項目を表示
   したい場所にドラッグ＆ドロップする。
#. 必要なフィールドをすべて必要な場所に移動するまで繰り返す。
#. Data Sources 窓を閉じる。
#. スプレッドシートを保存し、|MenuBar| の :menuselection:`&Edit-->E&dit Mode` を
   選択するか、|Ctrl+Shift| + :kbd:`M` を押して読み取り専用にする。
#. |MenuBar| の :menuselection:`&File-->Re&load` を選択する。すべてのフィールド
   に選択したデータ給源の最初の登録項目のデータの値が表示される。
#. :menuselection:`&View-->&Toolbars-->Form &Navigation` を選択して
   |FormNavigationToolbar| を表示する。既定ではこのツールバーは |StatusBar| のす
   ぐ上に開く。
#. |FormNavigationToolbar| の矢印をクリックすると、表のさまざまな登録項目が表示
   される。ツールバーには、現在表示されている登録項目と、利用可能な登録項目の総
   数が表示される。登録項目を移動するにつれて現在の登録項目番号が変わり、シート
   のフィールドデータは特定の登録項目番号のデータに対応するように更新される。

Embedding spreadsheets
======================================================================

* スプレッドシートを他の LibreOffice ファイルに埋め込むことが可能だ。
* スプレッドシートは |OLE| 物または |DDE| 物として埋め込み可能。

例えば、Calc スプレッドシートが |DDE| 物として Writer 文書に貼り付けられている場
合、Writer 文書からスプレッドシートを編集することは不可能だ。ただし、元スプレッ
ドシートが更新されると Writer 文書で自動的に更新される。

例：スプレッドシートがリンクされた |OLE| 物として Writer 文書に埋め込まれた場
合、Writer でもスプレッドシートを編集でき、両者が互いに同期する。

Object Linking and Embedding (OLE)
----------------------------------------------------------------------

|OLE| 物の主な利点は：

* ダブルクリックするだけでその内容を素早く編集できる。
* 物のリンクを挿入することもでき、その場合は図像として表示される。

リンクと埋め込みの差異は、元ファイルのその後の変更に追従するか否かだと思ってよい。
後者はデータの静的コピーでしかない。

.. note::

   |OLE| 物が空かつ活動停止中で、図像として表示されていない場合、それは透明にな
   る。

スプレッドシートを |OLE| 物として紙芝居に埋め込む手順：

#. 文書内の |OLE| 物を配置したい位置にキャレットを置く。
#. |MenuBar| の |InsertOLEM| を選択。|InsertOLEDlg| が開き、既定で新規作成オプ
   ションが選択されている。
#. |OLE| 物を新規作成するか、既存ファイルから作成する。

.. admonition:: 読者ノート

   これは Calc 以外のアプリケーションのメニューから Calc 文書を埋め込むことを想
   定した説明になっている？

新しいオブジェクトを作成する手順：

#. :guilabel:`Create &new` を選択し、:guilabel:`Object &Type` 一覧から必要なもの
   を選択する。この例では `LibreOffice 7.2 Spreadsheet` を選択する。
#. |OK| を押す。
#. LibreOffice はスライドに空の器を配置し、情報を入力できるようにする。既定では
   |MenuBar| は Calc |MenuBar| に変化する。スプレッドシートの領域以外のスライド
   をクリックすると、|MenuBar| は元のアプリケーションのそれに戻る。

スプレッドシート領域外をクリックした後、|OLE| 物をダブルクリックして、物の編集
モードに再度入る。その型のファイルを扱うアプリケーション (Calc) が物を開く。

はめ込んだスプレッドシートを保存する手順：

#. スプレッドシートの外側のどこかをクリックして、編集モードから出る。
#. スプレッドシート上で右クリックし、コンテキストメニューから
   :menuselection:`Save Copy &as...` を選択するか、|MenuBar| から
   :menuselection:`&Edit-->OLE Ob&ject-->Save Copy &as...` を選択する。
#. 新しいファイルの名前と保存先のフォルダーを選択する。
#. |Save| を押す。

.. note::

   挿入物が LibreOffice で処理される場合は、物を操作するプログラムへの移行が継ぎ
   目なく行われる。その他の場合は、物が新しい窓に開き、その挿入物を更新するため
   のオプションが |File-->| に表示される。

既存物をはめ込む手順：

#. 既存のファイルから |OLE| 物を作成するために :guilabel:`Create &from file` を
   選択する。 |InsertOLEDlg| が変化する。
#. :guilabel:`&Search...` を押し、|OpenFileDlg| で必要なファイルを選択し |Open|
   を押す。

   .. note::

      この機能は LibreOffice ファイルに限定されない。他の多くのアプリケーション
      の既存ファイルを使用して |OLE| 物を作成可能だ。

#. 物を原ファイルへのリンクとしてはめ込むには :guilabel:`&Link to file` をオンに
   する。そうしないと物が埋め込まれる。
#. 物をファイルの一部ではなく、選択可能な図像として見せたい場合は、
   :guilabel:`&Display as icon` をオンにする。
#. |OK| を押す。はめ込んだファイルの部分が文書に示される。原スプレッドシートに
   シートが複数ある場合は、編集モードでシート間を渡れる。

Other OLE objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Windows では |InsertOLEDlg| で :guilabel:`Create &new` オプションを選択すると
:guilabel:`Object &Type` 一覧に `Further objects` という項目が追加される。

#. `Further objects` の項目をダブルクリックして :guilabel:`オブジェクトの挿入`
   ダイアログボックスを開く。

   .. admonition:: 読者ノート

      LibreOffice ではなく、Windows が備えているダイアログボックスが開く。

#. :guilabel:`オブジェクトの種類 (&T)` 一覧で選択した型の新しい物をはめ込むため
   :guilabel:`新規作成 (&N)` を、既存ファイルから物を新規に作成するには
   :guilabel:`ファイルから作成 (&F)` を選択する。
#. 後者を選択した後 :guilabel:`参照 (&B)...` を押し、はめ込むファイルを選択する。
   挿入物はそれを作成した Windows プログラムで編集可能だ。

   物に代わりにリンクを挿入したい場合は、:guilabel:`アイコンで表示 (&D)` をオン
   にする。
#. |OK| を押す。

Non-linked OLE object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|OLE| 物がリンクされていない場合、新規文書で編集することが可能だ。例えば、
スプレッドシートを Writer 文書に挿入した場合、基本的に Writer の表組と同じように
扱うことが可能だ。ダブルクリックで編集開始。

Linked OLE object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

スプレッドシート |OLE| 物リンクされていて、Writer で変更すると Calc でも変更さ
れ、Calc で変更すると Writer でも変更される。Writer 窓だけを開いていればいいとい
うことになる。

.. note::

   ただし、一度に編集できるスプレッドシートのコピーは一つに限られる。複数の文書
   からリンクされている場合、残りの文書からは参照先が読み取り専用扱いとなる。

.. _calc11-anchor-dde:

Dynamic Data Exchange (DDE)
----------------------------------------------------------------------

文書 A で選択したデータを、リンクされたオリジナルの生コピーとして文書 B に貼り付
けることができる仕組みが |DDE| だ。例えば、Calc スプレッドシートから取得した販売
実績のような、時系列で変化するデータを含む Writer で書かれた報告書があり得る。
|DDE| リンクにより、参照先が更新されると参照元も更新されるため、エラーの可能性が
低くなり、参照元文書を最新の状態に保つ作業が軽減される。

|DDE| は |OLE| の前身に当たる。|DDE| では、物はファイル参照を通じてリンクされる
が埋め込まれない。|DDE| リンクは Calc シートの Calc 升目内、または Writer などの
別の LibreOffice 文書の Calc 升目内に作成できる。

DDE link in Calc
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|PasteSpecialDlg| の :guilabel:`As &Link` をオンにするのが本質的だ。参照先セルを
含むファイルを開いていないとこの操作ができない。

Calc スプレッドシートから別のスプレッドシートへ |DDE| リンクを作成する手順：

#. リンクしたい元のデータを含むスプレッドシートを Calc で開く。
#. |DDE| リンクさせたいセルを選択する。
#. |MenuBar| の |EditCopyM| を選択するか、|StandardToolbar| の :guilabel:`Copy`
   図像をクリックするか、選択領域を右クリックしてコンテキストメニューから
   :menuselection:`Cop&y...` を選択するか、|Ctrl| + :kbd:`C` を押して升目をク
   リップボードにコピーする。
#. リンクデータを含む第二のスプレッドシートを開く。
#. 第二スプレッドシートで、リンクデータを表示したい領域の左上升目をクリックする。
#. 第二スプレッドシートで、|MenuBar| の |PasteSpecialM| を選択するか、その領域の
   左上セルを右クリックしてコンテキストメニューから |PasteSpecialC| を選択する
   か、|Ctrl+Shift| + :kbd:`V` を押す。
#. |PasteSpecialDlg| が開く。
#. |PasteSpecialDlg| で :guilabel:`As &Link` を選択し |OK| を押す。
#. リンクされた升目をクリックすると、|FormulaBar| に ``{='`` で始まる参照が表示
   される。
#. 両方のスプレッドシートを保存して閉じる。

その後、そのスプレッドシートの元のセルを編集して変更を保存すると、次にリンク先の
セルを含むスプレッドシートを開いたときにリンク先の升目の値が更新され、元のセルの
最新値が反映される。

.. note::

   リンクされたデータを含むスプレッドシートを開くと、 外部リンクの自動更新が無効
   になっていることを示す警告メッセージが表示されることがある。リンクされた升目
   の更新を許可するには、関連するボタンを押す必要がある。元のデータを含むスプ
   レッドシートが信頼できるファイルの場所にあり、開くときに信頼できる場所からの
   リンクを常に更新するオプションが選択されていることを確認することで、このメッ
   セージを回避できる。これらの設定は |OptionsDlg| の

   * |SecurityPage| :guilabel:`Macro Securit&y...` ボタンからの
     :guilabel:`Trusted Sources` タブと、
   * |CalcGeneralPage| :guilabel:`Update links when opening section`

   でそれぞれ確認可能。

   .. admonition:: 読者ノート

      二つ目の項目が見当たらない。

DDE link in Writer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Calc から Writer への |DDE| リンクの作成手順は、Calc 内でのそれと同様だ。この機
能の詳細については |Writer| を見ろ。

#. Calc で |DDE| リンクを作成するセルを選択、コピー。
#. Writer 文書の |DDE| リンクを作成する場所に移動。|PasteSpecialM| を選択。
#. Writer に |PasteSpecialDlg| が開く。
#. :guilabel:`&Selection` 一覧で `Dynamic Data Exchange (DDE link)` を選択。
#. |OK| を押す。
#. これで Writer にリンクが作成された。Calc スプレッドシートが更新されると
   Writer の表も自動的に更新される。

XML Source
======================================================================

XML Source 機能を使用すると、既存の表計算文書の升目に、任意に構造化された |XML|
中身からデータをインポートすることができる。この機能では |XML| 中身の構造や使用
者が定義する写像定義に応じて、中身を部分的または全体的にインポートすることができ
る。使用者は同じ文書内の異なる升目位置に写される複数の重複しない部分構造を指定す
ることができ、要素中身、属性値、またはその両方のインポートを選択することができ
る。

.. note::

   XML Source 機能では、現在、|XML| データを一度限りのイベントとしてインポートす
   ることができる。すなわち、データがインポートされると、データ給源に関する情報
   は保存されない。

次のような |XML| ファイルに売上データがあるとする：

.. code:: xml

   <sales>
     <sale>
       <date>01/19/08</date>
       <value>$2,032</value>
       <category>Golf</category>
       <region>West</region>
       <employee>Brigitte</employee>
     </sale>
     <sale>
       <date>01/25/08</date>
       <value>$3,116</value>
       <category>Sailing</category>
       <region>East</region>
       <employee>Hans</employee>
     </sale>
     <sale>
       <date>01/26/08</date>
       <value>$2,811</value>
       <category>Tennis</category>
       <region>South</region>
       <employee>Fritz</employee>
     </sale>
    </sales>

このデータを Calc にインポートするには：

.. |XMLSourceDlg| replace:: :guilabel:`XML Source` ダイアログボックス

#. :menuselection:`&Data-->&XML Source...` を選択する。|XMLSourceDlg| が開く。
#. :guilabel:`Source File` 領域の図像を押す。文書にインポートする |XML| ファイル
   のパスを指定する。
#. 適切なフォルダーに移動し、必要なファイルを選択して |Open| を押す。
#. Calc は指定されたファイルの内容を読み取り、|XMLSourceDlg| の :guilabel:`Map
   to Document` 領域に |XML| の構造を表示する。
#. この例のデータの場合、:guilabel:`Map to Document` 領域で `sale` を選択する。
   これにより、|XML| 中身の `<sale>` 項目すべてがスプレッドシートにインポートさ
   れる。
#. スプレッドシートでデータを表示する領域の左上の升目をクリックする。この例の場
   合、A1 をクリックする。:guilabel:`&Mapped cell` 欄にクリックした升目のテル
   バックが表示される。
#. :guilabel:`&Import` ボタンを押す。この動作は、使用者が与えたリンク定義に基づ
   いてインポート処理を開始する。インポートが終了するとダイアログボックスが閉じ
   る。

|XML| 中身がスプレッドシート内の指定した位置に配置する。

|XMLSourceDlg| の :guilabel:`Map to Document` 領域には ソース |XML| 中身の構造が
木として表示される。最初は空で、ソースファイルを指定すると入力される。

木内の各要素は次の三種類のいずれかだ：

* 記号 ``@`` で表される属性。
* 記号 ``</>`` で表される単一の単発要素。同じ親の下で一度だけ出現する要素だ。文
  書内の単一セルに写される。
* 記号 ``<//>`` で表される反復要素。反復要素とは同じ親の下に複数回出現する要素
  だ。複数の登録項目の単一登録項目を囲む親として機能する。これらの項目は、項目の
  数にヘッダー行を一行追加した高さに等しい範囲にインポートされる。

:guilabel:`&Mapped cell` 欄は要素や属性がリンクされている文書内の升目の位置を指
定する。単発要素や属性の場合はリンクされた要素や属性の値がインポートされる升目を
指す。反復要素であれば登録項目全体とヘッダーがインポートされる範囲の左上の升目を
指す。
