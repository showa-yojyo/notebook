======================================================================
Calc Guide Chapter 15, Setting up and Customizing ノート
======================================================================

.. include:: ./calc-inc.txt

.. contents:: 章見出し
   :depth: 3
   :local:

Introduction
======================================================================

この章では |OptionsDlg| にある設定オプションの一部を見ていく。その他のオプション
や、ここで紹介するオプションの詳細については |Help| や |Guide| に説明がある。

この章では、|MenuBar|、ツールバー、キーバインドの一般的なカスタマイズについても
説明する。その他のカスタマイズは LibreOffice の Web サイトや他の設備者からインス
トールできる拡張機能によって簡単に行うことができる。

LibreOffice options
======================================================================

この節では LibreOffice の部品すべてに適用される設定のうち、Calc の使用者にとって
特に重要な設定をやる。

#. :menuselection:`&Tools-->&Options...` を選択して |OptionsDlg| を開く。左側の
   木は開いている LibreOffice アプリケーションによって異なる。
#. `LibreOffice` の横にある展開記号をクリックする。部分木がドロップダウンする。

.. note::

   |OptionsDlg| の下部にある |ResetButton| は、どのページであっても押せばダイア
   ログボックスを開いた時点の状態にリセットされる。

User data
----------------------------------------------------------------------

このページの項目は LibreOffice の雛形やウィザードで使用される。たとえば Calc で
は、文書性質の `Created` フィールドと `Modified` フィールドを埋めるために、ここ
に保存された姓と名を使用する。これらのフィールドは、印刷されたスプレッドシートの
フッターや、コメントに関連付けられた名前としても使用される。自分の名前を表示した
い場合は、|UserDataPage| のフォームに入力しろ。

View
----------------------------------------------------------------------

|LibreOfficeViewPage| のオプションは、ツールバーや |Sidebar| の図像寸法やスタイ
ルなど、文書ウィンドウの容貌や動作に影響する。個人の好みに合わせて設定しろ。

Print
----------------------------------------------------------------------

|LibreOfficePrintPage| では既定プリンターといちばんよく使う印刷方法に合わせて選
択肢を決める。印刷時になって |PrintDlg| で変更することも可能。

Calc 固有の印刷オプションがあり、それについては後述。

|Calc07| も参照しろ。

Paths
----------------------------------------------------------------------

|PathsPage| では LibreOffice に関連するか使用されるファイルの場所を設定可能だ。
項目によっては、少なくとも二つのパスが表示される：

* 共有フォルダー
* ユーザー固有フォルダー

Security
----------------------------------------------------------------------

|SecurityPage| では文書の保存やマクロを含む文書を開くときの機密保全オプションを
指定可能だ。

:guilabel:`Security Options and Warnings`
   変更を記録したり、複数の版を保存したり、文書に隠し情報や覚書を含めたりする場
   合に、一部の受信者にその情報を見せたくない場合は、その情報を削除するよう警告
   を表示したり、LibreOffice が自動的に削除したりすることが可能だ。これらの情報
   の多くは、LibreOffice の既定形式である OpenDocument Format でも、|PDF| を含む
   他の形式で保存されたファイルでも、削除されない限りファイルに保持される。

   :guilabel:`O&ptions...` ボタンで特定の選択肢を持つ別のダイアログが開く。
:guilabel:`Passwords for Web Connections`
   マスターパスワードを入力すると、使用者名とパスワードが必要な Web サイトに簡単
   にアクセスできるようになる。

   :guilabel:`Persistently &save passwords for web connections` をオンにすると、
   :guilabel:`Set Master Password` ダイアログボックスが開く。LibreOffice は Web
   サーバーからファイルにアクセスするために使用するパスワードのすべてを安全に保
   存する。マスターパスワードを入力した後、一覧からパスワードを取り出すことがで
   きます。
:guilabel:`Macro Security`
   :guilabel:`Macro Securit&y...` ボタンを押すと |MacroSecurityDlg| が開き、マク
   ロ実行の機密保全度を調整したり、信頼できる給源を指定したりする。
:guilabel:`Certificate Path`
   LibreOffice を使って文書に電子署名をすることができます。電子署名には個人署名
   証明書が必要だ。OS のほとんどが自己署名証明書を生成可能だ。ただし、（個人の身
   許を確認した上で）外部機関が発行する個人証明書は自己署名証明書よりも信頼性が
   高い。これらの証明書を安全に保存する方法が LibreOffice にはないが、他のプログ
   ラムを使用して保存された証明書にアクセスすることは可能だ。
   :guilabel:`Certificate` ボタンを押し、使用する証明書保管庫を選択する。

   .. note::

      :guilabel:`Certificate Path` オプションは Linux および macOS でのみ表示さ
      れる。Windows では LibreOffice は証明書の保存と取得に Windows の既定の場所
      を用いる。

:guilabel:`TSAs`
   LibreOffice で作成された PDF 文書のタイムスタンプ認証 URL をオプションで選択
   できる。|PDF| の電子署名に信頼できるタイムスタンプを追加すると、データの整合
   性を示すデジタルシールと、ファイルが署名された信頼できる日時が与えられる。信
   頼できるタイムスタンプを持つ |PDF| 文書の受信者は文書がいつデジタル署名または
   電子署名されたかを確認できるだけでなく、タイムスタンプが証明する日付以降に文
   書が変更されていないことも確認できる。

Security Options and Warnings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`&Remove personal information on saving`
   これをオンにすると、ファイルを保存する際に、ファイル性質から使用者データがつ
   ねに削除される。特定の文書から個人情報を手動で削除するには、このオプションを
   オフにしてから、|MenuBar| から |FilePropertiesM| でダイアログボックスを開き、
   |GeneralTab| にある :guilabel:`&Reset Properties` ボタンを押す。
:guilabel:`Ctrl-click required &to open hyperlinks`
   LibreOffice のほとんどのコンポーネントの既定動作はハイパーリンクからリンク先
   の文書を開く動作は |Ctrl| を押しながらクリックするというものだ。これをシング
   ルクリックでハイパーリンクを開くように設定することも可能だ。

他の選択項目は自明。

Application colors
----------------------------------------------------------------------

|ApplicationColors| では、どの |UI| 要素を表示するかと、それらの要素の表示に使用
する色を指定可能だ。

* スプレッドシートの区画まで一覧をスクロール。
* 格子線やその他の画面上の表示器の既定色を変更するには、色の横にある▼をクリック
  し、ドロップダウンリストから新しい色を選択する。
* 変更を配色として保存したいならば :guilabel:`&Save` を押し、:guilabel:`&Name of
  color scheme` 欄に名前を入力して |OK| を押せ。

.. admonition:: 利用者ノート

   本節の記述は若干古い可能性がある。現況と合っていない。

Advanced options
----------------------------------------------------------------------

|LibreOfficeAdvancedPage| で注目したい選択肢は次のものだ：

:guilabel:`Enable experimental features (may be unstable)` をオンにすると、未完
成機能や既知バグを含む機能が利用可能になる。そのような機能の集合はバージョンによ
り異なる。

:guilabel:`Enable macro recording (may be limited)` をオンにすると、マクロ記録コ
マンドが利用可能になる（オンにしないと |Calc13| の記述内容を検証できない）。

Options for loading and saving documents
======================================================================

:menuselection:`Load/Save-->` 以下の選択肢のうち、Calc での作業に最も関連性の高
いものの一部のみを説明。それ以外については |Guide| 参照。

General
----------------------------------------------------------------------

|LoadSaveGeneralPage| の選択肢の多くは、この手の事務作業ソフト利用者には慣れ親し
んでいるものだ。Calc で重要なのは :guilabel:`Default File Format and ODF
Settings` 項目各種だ。

:guilabel:`ODF format version` は OpenDocument Format (ODF) version 1.3
Extended 形式で文書を保存する。これを変更する必要はめったにない。

:guilabel:`D&ocument type` ドロップダウンリストを :guilabel:`Spreadsheets
(Calc)` にまず合わせる。日常的に Microsoft Excel ユーザーと文書を共有する場合は
:guilabel:`Always sa&ve as` を XLSX など Excel 形式のいずれかに変更するとよい。

* 個々のファイルを保存する段になって Excel 形式を選択することは可能だ。
* 作業コピーを ODS 形式で常に保存し、共有に必要になった時点で XLSX 形式のファイ
  ルを作成するようにするのがよい。

VBA Properties
----------------------------------------------------------------------

:menuselection:`Load/Save-->VBA Properties` ページでは LibreOffice で開いた
Microsoft Office 文書の VBA マクロの取り扱いを構成する。

* Word, Excel, PowerPoint の三区画で load/execute/save のいずれかをオンオフ指定。
* :guilabel:`Load Basic` をオンにすると、

  * LibreOffice でマクロ編集が可能になる。
  * 変更コードは ODF 文書に保存される。
  * Microsoft Office 形式に保存する場合に変更は消失する。
* :guilabel:`Save original Basic code` をオンにすると、

  * マクロは LibreOffice では動作しない。
  * Microsoft Office 形式で保存すると、マクロは変更されずに保持される。
  * :guilabel:`Load Basic` 設定よりも強い。両方オンのときの挙動に注意。
* :guilabel:`Executable code` をオンにすると、コードは保存されるが不活性状態をと
  る。IDE で確かめるとコードがコメントアウトされているはずだ。

Microsoft Office
----------------------------------------------------------------------

:menuselection:`Load/Save-->Microsoft Office` ページでは Microsoft Office OLE
オブジェクト、例えばスプレッドシートや数式などのリンクまたは埋め込みオブジェク
ト、文書をインポートまたはエクスポートする際の処理を選択する。

* :guilabel:`[L]` 欄チェックは Microsoft から LibreOffice に読み込みときにオブ
  ジェクトを変換する。
* :guilabel:`[S]` 欄チェックは LibreOffice から Microsoft 形式に保存するときにオ
  ブジェクトを変換する。

.. admonition:: 利用者ノート

   :guilabel:`Character Highlighting` オプションが実現する機能がわからない。

:guilabel:`Create MSO lock file` をオンにすると、Microsoft Office 形式のファイル
を開くときに、LibreOffice ロックファイルと Microsoft Office ロックファイルを両方
作成される。

HTML Compatibility
----------------------------------------------------------------------

:menuselection:`Load/Save-->HTML Compatibility` で選択した内容は、LibreOffice
による HTML ページの読み込みと書き出しに影響する。

Calc 利用者としては :guilabel:`Export` 区画の設定に主な関心がある。

:guilabel:`LibreOffice &Basic` をオンにすると、HTML 形式へのエクスポート時にマク
ロが含まれるようになる。

* マクロを作成する前にこれをオンにする必要がある。
* マクロは HTML 文書のヘッダーに置く必要がある。IDE でマクロを作成すると、HTML
  文書のソースコードのヘッダーに表示される。

:guilabel:`LibreOffice &Basic` がオフのとき :guilabel:`Display &warning` が利用
可能になる。このオプションがオンである場合、HTML にエクスポート時に LibreOffice
Basic マクロが失われるという警告が表示される。

:guilabel:`&Print layout` をオンにすると現在の文書の印刷レイアウトもエクスポート
される。HTML フィルターは文書の印刷用に CSS2 に対応している。これらの機能は、印
刷レイアウトのエクスポートが有効になっている場合に限り有効だ。

:guilabel:`&Copy local image to Internet` をオンにするのは、FTP を用いる場合、か
つ埋め込み画像を自動的にサーバーにアップロードする場合だ。

Calc-specific options
======================================================================

|OptionsDlg| :menuselection:`LibreOffice Calc` 以下の設定項目。

General
----------------------------------------------------------------------

|CalcGeneralPage| の選択肢は、測定に使用する単位、既定タブストップ位置、リンクと
フィールドの更新、その他さまざまな入力設定に有効だ。

:guilabel:`Metrics` 区画にある項目はスプレッドシートで用いられる距離単位とタブス
トップの距離だ。後者はソフトスペース何個とかではなく、``1.25 cm`` などの現実の距
離で指定される。

:guilabel:`Update links when opening` 区画。ここでの構成がリンク（図式や画像）を
大量に含むスプレッドシートの読み込み時間に影響する。

.. admonition:: 利用者ノート

   バランスをとって :guilabel:`&On request` にしておく。

:guilabel:`Input Settings` 区画。細かい項目が並ぶ。

* :guilabel:`Press Enter to &move selection` はオンにするなら :guilabel:`Down`
  一択だろう。オフにすると |Enter| でセル移動なしになる。
* :guilabel:`Press Enter to switch to &edit mode` をオンにすると |Enter| がセル
  に対する編集モードオンオフキーとなる。
* :guilabel:`Press Enter to paste and clear clipboard` をオフにすると、セル
  |Enter| でのコピー無効化かつ貼り付け後のクリップボード消去無効化。

  * オフのほうが好みである可能性がある。

* :guilabel:`Expand &formatting` は選択セルの書式属性を空の隣接セルに自動的に適
  用するかどうかを決めるものだ。

  * 影響範囲を確認するには |Ctrl| + :kbd:`*` を押す（テンキーのほう）
  * ヘッダー行や日付列でこれが働くと特にうれしい。
* :guilabel:`Expand &references when new columns/rows are inserted` は、例えば
  A1:B1 の範囲を参照する数式がどこかにあるとする。列 B の後に新しい列が挿入され
  た場合、参照を A1:C1 に展開するかどうかを決めるオプションだ。
* :guilabel:`Update references when sorting range of cells` がオンである場合に限
  り、セル範囲が並び替えられたときにセルへの参照が更新される。
* :guilabel:`Highlight sele&ction in column/row headers` をオンにすると選択セル
  に対する列や行のヘッダーを強調表示する。
* :guilabel:`Use printer metrics for text formatting` をオンにすると既定プリン
  ターの性質を用いてスプレッドシート表示書式を与える。

  * |MenuBar| :menuselection:`&File-->P&rinter Settings...` で開くダイアログ
    ボックスの :guilabel:`&Properties...` を押すと表示される性質。
  * プリンターにページ設定オプションがある場合は、その設定が文書に適用される。

  オフの場合にはページは汎用プリンター用に設定される。
* :guilabel:`Show overwrite &warning when pasting data` をオンにするとクリップ
  ボードの内容をセルに貼り付けるときにデータが失われることがある場合に警告が現れ
  る。
* :guilabel:`Position cell reference with selection` は |Ctrl+Shift| + 矢印キー
  でセル範囲選択を拡張するときに、拡大直後のジャンプ先のセルが変化する。ガイドの
  記述がわかりにくい。

Defaults
----------------------------------------------------------------------

|CalcDefaultsPage| では新しいスプレッドシートを開始したときのシートの数を入力し
たり、シート名の接頭辞を指定したりする。|Calc01| 参照。

View
----------------------------------------------------------------------

|CalcViewPage| では文書ウィンドウを画面上で表示したときの容貌と動作を構成する。

Display section
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* :guilabel:`&Formulas` をオンにするとセルの内容を数式として（結果ではなく）表示
  する。
* :guilabel:`Zero val&ues` をオフにするとセルの値がゼロの場合、空のセルを表示す
  る。
* :guilabel:`&Comment indicator` をオフにするとセル右上隅の三角が示されない。
* :guilabel:`&Formula indicator and hint` をオンにすると、数式を含むセルの左下隅
  に青い三角形が示される。その三角形の上にマウスポインターを置くと、ツールチップ
  がポップアップしてそこに数式が示される。
* :guilabel:`Value h&ighlighting` をオンにするとシート内のすべての値または数式の
  結果が強調表示される。このオプションが有効であると、文書で割り当てられている色
  は使われない。

  * テキストは黒
  * 数値、日付、論理値は青
  * 数式は緑
* :guilabel:`&Anchor` をオンにすると、画像などのオブジェクトがセルに繋ぎ留められ
  ている場合、対象セルに錨の図像が表示される。
* :guilabel:`&Show references in color` をオンにすると、参照を含むセルが編集用に
  選択されると同時に、各参照が数式内で色付き表示され、参照されたセル範囲が色付き
  の枠線で囲まれる。

Window section
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

スプレッドシートウィンドウの要素表示切り替えオプションの集まり：

* 列ヘッダーと行ヘッダー
* 水平/垂直スクロールバー
* シートタブ
* アウトライン記号

:guilabel:`Sh&eet tabs` がオフの場合、Navigator でしかシートを切り替えることがで
きない。

:guilabel:`Summary o&n search` は |Calc02| で述べられた :guilabel:`Search
Results` ダイアログボックスの表示を制御する。

Visual Aids section
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`&Grid lines` ドロップダウンリストで画面上でのシート罫線を設定する。

* :guilabel:`Show`
* :guilabel:`Show on colored cells`
* :guilabel:`Hide`: 表はセルの回りに罫線がない無地の背景で描かれる。

印刷上のシート罫線設定は |MenuBar| :menuselection:`F&ormat-->Page Style...` で開
くダイアログボックスの :guilabel:`Sheet` タブで行う。

:guilabel:`Pointe&r`: スプレッドシートのセル格子上にマウスポインターを置く
と、通常は既定ポインターが矢印で表示される。しかし、別のポインターを使用すると、
アイコンのテーマで定義されたポインターの形状（通常は太い十字）に切り替える。

:guilabel:`&Page breaks` をオンにすると定義された印刷領域内で改頁を表示する。

:guilabel:`Helplines &while moving` をオンにすると、図面、プロット、画像などのオ
ブジェクトを画面上で移動するときに、位置合わせのためのスナップ線が描画される。

Objects section
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

画像、プロット、図面物の表示切り替え。

Zoom section
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`S&ynchronize sheets` をオンにすると、選択した拡大倍率がスプレッドシー
ト内のシートすべてに適用される。

Calculate
----------------------------------------------------------------------

|CalculatePage| でスプレッドシートの計算設定を構成する。

Formulas Wildcards section
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

検索と文字列比較に関する動作。|Calc08| を参照しろ。

:guilabel:`Enable w&ildcards in formulas`
   Microsoft Excelとの相互運用性が必要な場合はこの選択肢を採れ。
:guilabel:`Enable r&egular expressions in formulas`
   ワイルドカードは無効に、正規表現が有効になる。
:guilabel:`No wildcards or regular expressions in formulas`
   リテラル文字列でしか評価しない。

Date section
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

日数から数字への内部変換の開始日を選択する。ここは触れないほうがいい。

General Calculations section
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Case &sensitive`
   セルの内容を比較する際に大文字と小文字を区別するかどうかを指定する。例えば中
   身がそれぞれ ``Test`` と ``test`` であるセル同士の比較評価が変わる。関数
   ``EXACT`` は常に case-sensitive だ。
:guilabel:`&Precision as shown`
   これがオフの場合、数値は丸められて表示され、内部では原数値を用いて計算され
   る。
:guilabel:`Search criteria = and <> must apply to &whole cells`
   これは search と match の違いを述べていると考えられる。文字列 ``day`` を検索
   しようとして、``Friday``, ``Sunday``, ``days`` などにヒットさせたいかどうかで
   オンオフを決めろ。

   .. admonition:: 利用者ノート

      オンにするとテキスト検索が「厳しく」なる。上級者はこれをオンにして、ワイル
      ドカードや正規表現を駆使した検索を行うのだろうか。

:guilabel:`&Automatically find column and row labels`
   列見出しの下または行見出しの右に、それらの見出しのテキストを使用してデータ範
   囲に名前を付ける。
:guilabel:`&Limit decimals for general number format`
   一般的数値書式を持つ数値に対して表示される小数部の桁数を制限する。

Iterative References section
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

反復参照とは問題が解けるまで継続的に反復される数式だ。反復計算中に実行される近似
段階数と解の精度を設定する区画だ。

:guilabel:`&Iterations`
   これをオンにしないと反復参照が有効にならない。無効時、反復参照がエラーを引き
   起こす。
:guilabel:`&Steps`
   反復回数を設定する。
:guilabel:`&Minimum change`
   立て続けの二段階の結果の差がこの設定値より小さい場合、反復は停止する。

CPU Threading Settings section
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Enable multi-threaded calculation` については |Calc08| を参照。オフに
する意味がない。

Formula
----------------------------------------------------------------------

|FormulaPage| で数式オプションを構成する。

Formula Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Formula &syntax` ではセルの番地を指示する方式をドロップダウンリストか
ら選択する。例えばシートSheet2 におけるセル C4 の指定方式はそれぞれ次のように表
される：

* :guilabel:`Calc A1` では ``$Sheet2.C4``
* :guilabel:`Excel A1` では ``Sheet2!C4``
* :guilabel:`Excel R1C1` では ``Sheet2!R[3]C[2]``

:guilabel:`&Use English function names` はオンにするに決まっている。

Separators
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* 関数呼び出しの引数リストで実引数を区切る文字
* 配列列の区切り文字
* 配列行の区切り文字

を指定する。

Detailed Calculation Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

カスタム設定の場合は :guilabel:`Custom` を選択して :guilabel:`Details...` を押
す。参照構文と空の文字列をゼロとして扱うかどうかを決める。

Recalculation on File Load
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

計算式の再計算はファイルによっては読み込みにかなりの時間がかかる。

:guilabel:`Excel 2007 and newer`
   巨大スプレッドシートのデータをすぐに更新する必要がない場合は、再計算を適切な
   時点まで延期可能だ。Calc では Excel 2007 および最近のスプレッドシートに対し
   て、読み込み時間を短縮可能だ。
:guilabel:`ODF spreadsheet (not saved by LibreOffice)`
   最近のバージョンの Calc では、スプレッドシートの数式結果が ODF ファイルに
   キャッシュされる。この機能により、Calc によって保存された巨大 ODF スプレッド
   シートを高速に再計算可能なのだが、他のプログラムによって保存された ODF スプ
   レッドシートでは、そのようなキャッシュされた数式結果が存在しない可能性があ
   る。上記項目と同様に、再計算を延期可能だ。

どちらの項目にも次の選択肢がある：

* :guilabel:`Never recalculate`
* :guilabel:`Always recalculate`
* :guilabel:`Prompt user`

Calc で保存された |ODF| スプレッドシートは最初の二つのオプションの面子を立てる。

Sort Lists
----------------------------------------------------------------------

並べ替え一覧の表示、定義、削除、編集を行うのは :menuselection:`LibreOffice
Calc-->Sort Lists` ページだ。

* ここでの一覧はデータ入力時に一連のセルを埋めるなど、並べ替え以外の用途にも用
  いられる。
* 並べ替え一覧は辞書式順や数値順ではなく、特定の順序で配列される一覧だ。

Chapter 2 も参照しろ。

Changes
----------------------------------------------------------------------

|CalcChangesPage| では差分表示における挿入、削除、その他の変更に特定の色を割り当
てることと、変更者に基く色を割り当てることが可能。ここで選択した色は、|MenuBar|
|EditTrackRecordM| が有効になっている場合に適用される。

Compatibility
----------------------------------------------------------------------

:menuselection:`LibreOffice Calc-->Compatibility` ページでは LibreOffice の既
定キーバインドと旧 OpenOffice のそれを切り替えるために設けられているようだ。

Grid options
----------------------------------------------------------------------

:menuselection:`LibreOffice Calc-->Grid` ページで上手に設定を構成すると、スプ
レッドシートに追加するプロットやその他のオブジェクトの位置を高精度で合わせること
が可能になる。スナップ機能も備えられている。

操作中にスナップを一時的にオフにするには |Ctrl| を押しながらドラッグする。

.. rubric:: Grid 区画

:guilabel:`Sn&ap to grid` をオンにするとスナップ機能が有効になる。

:guilabel:`V&isible grid` をオンにすると画面上に格子点を描画する。印刷には現れな
い。

.. rubric:: Resolution and Subdivision 区画

格子の水平および垂直の格子点および中間点間の間隔を設定する。

:guilabel:`Synchronize a&xes` をオンにすると現在の格子設定を軸対称に変更する。
ページ上の項目を変更すると、それに対となる項目が同時に更新する。

Print options
----------------------------------------------------------------------

|CalcPrintPage| を使用して、スプレッドシートの印刷の既定値を選択する。これらを印
刷ジョブ個別で上書きしてよい。

Default colors for charts
======================================================================

|OptionsDlg| :menuselection:`Charts` にはページが一つしかない。

:menuselection:`Charts-->Default Colors` ページを使って、図式に使われる既定色
を変更したり、与えられる一覧に新しいデータ系列を追加したりする。

データ系列の既定色を変更するには、左側の列で :samp:`Data Series {#}` を選択し、
:guilabel:`Color Table` で必要な色を摘む。

別のデータ系列を追加するには :guilabel:`&Add` を押し、新しい系列を選択して必要な
色を摘む。

:guilabel:`&Default` を押すと、プログラムのインストール時の色設定が復元する。

Customizing the user interface
======================================================================

|MenuBar|、ツールバー、キーバインド、タブ付きインターフェイスを誂えたり、新しい
メニューやツールバーを追加したり、イベントにマクロを割り当てたりする。

.. tip::

   |MenuBar| とツールバーの変更は雛形に保存することが可能だ。その方法とは、ま
   ず、文書にそれらを保存する。次に、|Calc05| で説明するように、その文書を雛形と
   して保存するというものだ。

Menu content
----------------------------------------------------------------------

メニューを誂えるには、

#. |MenuBar| |CustomizeM| を選択して |CustomizeDlg| を開く。
#. |MenusTab| または |ContextMenusTab| をクリック

両者の操作はほとんど同じであるので、以下、|MenusTab| に焦点を当てた記述となる。

Modifying an existing menu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. :guilabel:`S&cope` ドロップダウンリストで、変更メニュー保存先を Calc 全体か選
   択文書かを指定する。
#. :guilabel:`&Target` ドロップダウンリストで、誂えたいメニューの親項目を指定す
   る。
#. コマンドを追加するには :guilabel:`&Available Commands` 一覧でコマンド項目をク
   リックし、右矢印ボタンを押す。

   * :guilabel:`&Search` 欄や :guilabel:`Categor&y` ドロップダウンリストでコマン
     ド一覧を絞り込める。
   * 右端の上下矢印ボタンでコマンドを一覧の所望の位置に移動する。
#. 選択したメニューからコマンドを削除するには、割り当てられたコマンド一覧でその
   コマンド項目をクリックし、左矢印ボタンを押す。
#. 区切りや部分メニューを挿入するには、:guilabel:`&Customize` 区画の
   :menuselection:`&Insert-->Insert Separator` や
   :menuselection:`&Insert-->Insert Submenu` を実行する。
#. メニュー項目のラベルを変えるには、それを選択してから
   :guilabel:`&Modify-->&Rename...` を実行。
#. |OK| で確定。

Creating a new menu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. :guilabel:`&Target` 区画の歯車ボタンを押して :guilabel:`&Add...` を実行して
   :guilabel:`New Menu` ダイアログボックスを開く。
#. :guilabel:`&Menu name` 欄に新しい名前を入力。
#. 上下矢印ボタンで新しいメニューの位置を決定。
#. |OK| で確定。

新規メニューにはコマンドを追加する必要がある。

Creating an accelerator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

カスタムメニューの名前の一文字をキーバインドとして割り当てる（キーに対応する文字
に下線が引かれる）。|Alt| を押しながらその文字キーを押すと、対応コマンドが呼び出
される。

方法は、上記メニューラベル指定時に対象文字の直前に ``~`` を付けるというものだ。

.. admonition:: 利用者ノート

   Windows API と違う文字を使うので注意。

* 関連するコマンドにすでに割り当てられている文字を使わないように注意。
* 同じ文字とキーの組み合わせは、異なるメニュー項目に関連するコマンドには使用して
  よいが、同じメニュー項目に関連するコマンドには使用不可。

Toolbars
----------------------------------------------------------------------

ツールバーを誂えるには、図像の選択や繋留位置の固定など、いくつかのやり方がある。
本節では、ツールバーを新築する方法と、ツールバー上の図像（コマンド）を追加または
削除する方法について述べる。

ツールバーのカスタマイズは |CustomizeDlg| の :guilabel:`Toolbars` タブで行う。

ツールバーを誂える方法は前述のメニューのそれとよく似ている。ツールバーに割り当て
られたコマンドの表示状態を決める手順があり、:guilabel:`Assi&gned Commands` 一覧
の図像横にあるチェックボックスをオンまたはオフにする。

Creating a new toolbar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. |CustomizeM| を選択。
#. :guilabel:`Toolbars` タブで :guilabel:`Target` 欄横のボタンを押してドロップダ
   ウンリストから :guilabel:`&Add...` を選択して |NameDlg| を開く。
#. 新規ツールバーの名前を入力してドロップダウンリスト :guilabel:`&Save in` から
   メニュー保存先を Calc 全体か選択文書かを指定する。
#. |OK| を押す。

新しいツールバーが |CustomizeDlg| のツールバー一覧に表示される。このツールバーに
コマンドを追加する手順は、ツールバーの変更に関する前述のものと同じだ。

Choosing icons for toolbar commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ツールバーのボタンは :guilabel:`&Target` ドロップダウンリスト脇のメニューから表
示方式を指定可能だ：

* :guilabel:`&Icon and text`
* :guilabel:`Icon &only`
* :guilabel:`&Text only`

コマンドの図像を選択するには、

#. コマンドを選択
#. :menuselection:`&Modify-->Change Icon...` を実行
#. :guilabel:`Change Icon` ダイアログボックスで、利用可能なアイコンをスクロール
   して選択
#. |OK| を押す

自作図像を使用する術もあるが割愛。

既定図像に戻すには :menuselection:`&Modify-->Reset Icon` を実行。

Tabbed interface
----------------------------------------------------------------------

Calc のコマンド群はインストール直後の時点では、階層メニューと図像であふれたツー
ルバーにグループ化されている。LibreOffice にはさらに、コマンドや中身のコンテキス
トグループを表示する、他の |UI| の変種も搭載している。|Calc16| 参照。

LibreOffice の UI のうち、ノートブックバーを使用する変種は三つある：

* Tabbed
* Tabbed Compact
* Groupedbar Compact

これらの変種では作業場所の上部の領域がタブに分割され、タブそれぞれにコンテキスト
ごとにグループ化された図像集が表示される。コンテキストが変化するのは、例えば図表
や画像など、文書でどんなオブジェクトが選択されているかによる。

|CustomizeDlg| の :guilabel:`Notebookbar` にあるチェックボックスを使って、タブ付
き UI のうち最近選択されたものに（ない場合は Tabbed に）対して、用意されている各
オプションの表示状態を切り替える。

Keyboard shortcuts
----------------------------------------------------------------------

組み込みのキーバインド (Appendix A) を使用するだけでなく、独自に定義することが可
能だ。LibreOffice の標準機能または独自のマクロにキーバインドを割り当て、
LibreOffice プログラム全体または Calc でのみ使用するように保存可能だ。

* OS が予約しているキーバインドと競合するものはやめろ。
* |CustomizeDlg| の一覧で灰色表示されているキーは割当不可を意味する。

#. |MenuBar| から |CustomizeM| を選択。
#. :guilabel:`Keyboard` タブ
#. 新規キーバインドが Calc 全体か選択文書のどちらで有効であるかを指定
#. :guilabel:`&Category` と :guilabel:`&Function` 一覧から必要な項目を選択
#. :guilabel:`Shortcut Keys` 一覧で目的のキーバインドを選択
#. :guilabel:`&Modify` を押す
#. |OK| を押す

希望のキーバインドがすでに使用中の場合、それをまず削除する必要がある。

Saving changes to a file
----------------------------------------------------------------------

キーバインド変更は後で使用するためにキーバインド構成ファイルに保存可能だ。その方
法は：

#. キーバインド設定完了後、:guilabel:`&Save...` ボタンを押す。
#. :guilabel:`Save Keyboard Configuration` ダイアログボックスで :guilabel:`File
   name` 欄に構成ファイルの名前を入力する。
#. |Save| を押す。

Loading a saved keyboard configuration
----------------------------------------------------------------------

保存したキーバインドファイルをロードして現在の設定を置き換える方法：

#. ダイアログボックスの右側にある :guilabel:`&Load...` を押す
#. :guilabel:`Load Keyboard Configuration` ダイアログボックスで構成ファイルを選
   択

Resetting the shortcut keys
----------------------------------------------------------------------

キーバインドすべてを既定値に戻すにはダイアログボックスの右側にある |ResetButton|
を押す。確認メッセージは表示されないことに注意しろ。

.. admonition:: 利用者ノート

   このタブだけリセットボタンの配置が違う。

Running macros from key combinations
----------------------------------------------------------------------

マクロ (|Calc13|) を実行するキーバインドを定義することも可能だ。これらのキーバイ
ンドは厳密にユーザー定義だ。

Assigning macros to events
======================================================================

LibreOffice では、たとえば、文書が開かれた、キーが押された、マウスが動いたなどを
総称してイベントが起こったという。マクロをイベントに関連付けると、イベントが発生
したときにそのマクロが実行される。

イベントとマクロを関連付けるには |CustomizeDlg| の |EventsTab| を使用する。詳細
は |Guide| を参照しろ。

Adding functionality with extensions
======================================================================

   An extension is a package that can be installed into LibreOffice to add new
   functionality.

公式 LibreOffice 拡張置場は <https://extensions.libreoffice.org/> だ。ここにある
ものは無料で入手かつ利用可能。

Installing extensions
----------------------------------------------------------------------

上記の置場から拡張をインストールする手順：

#. |ExtensionsM| or |Ctrl+Alt| + :kbd:`E`
#. |ExtensionsDlg| で :guilabel:`Get more extensions online` をクリック
#. 拡張機能を見つけてダウンロード
#. |ExtensionsDlg| に戻り、:guilabel:`&Add`
#. インストールしたい拡張を見つけて選択し、|Open| を押す

拡張は Calc の他の場所からもインストール可能だ：

* |Sidebar| の :guilabel:`Gallery` にある拡張ボタン
* |TemplatesDlg| の :menuselection:`&Manage-->E&xtensions`
* |OptionsDlg| の |LibreOfficeViewPage| :guilabel:`Icon Theme` 枠内拡張ボタン

Updating extensions
----------------------------------------------------------------------

|ExtensionsDlg| にある :guilabel:`Check for &Updates` を押せ。

Removing and disabling extensions
----------------------------------------------------------------------

インストール済み拡張を削除するには |ExtensionsDlg| で拡張を選択し、
|RemoveButton| を押す。

アンインストールではなく無効にするだけならば :guilabel:`&Disable` を押す。

Adding custom colors
======================================================================

#. 図面オブジェクトを文書内に追加する。
#. オブジェクトを右クリックし、:menuselection:`A&rea...` を実行。
#. |AreaTab| をクリック。
#. :guilabel:`Co&lor` ボタンを押す。
#. :guilabel:`Pal&ette` ドロップダウンリストで追加先パレットを選択。
#. :guilabel:`New` 下でどの方法でもいいから色を指示する。
#. :guilabel:`&Add`
#. 色の名前を入力
#. |OK|
#. 不要な図面オブジェクトを削除。

Setting up document themes
======================================================================

* 文書テーマでは、さまざまな書式選択をワンセットにまとめ、すばやく適用したり変更
  したりできる。
* テーマカラーセットがいくつか用意されている。

独自セットを定義する手順：

#. :menuselection:`F&ormat-->Theme...` を実行して |ThemeDlg| を開く
#. ベーステーマを選択
#. :guilabel:`&Add` を押して |ThemeColorEditDlg| を開く
#. 新規テーマに名前を与え、利用可能なパレットから色を選択
#. |OK| を押して新規テーマを保存

文書テーマの利用に関する指示については |Calc05| を参照しろ。

使用者定義テーマカラー集は文書内にしか保存されない。他の文書で用いるには雛形を作
成する。
