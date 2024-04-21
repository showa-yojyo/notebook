======================================================================
Calc Guide Chapter 7 Printing, Exporting, Emailing, and Signing ノート
======================================================================

.. include:: ./calc-inc.txt

.. contents:: 章見出し
   :local:

Printing
======================================================================

Quick printing
----------------------------------------------------------------------

:guilabel:`Standard` ツールバーに :guilabel:`Print Directly` ボタンを表示させ
ておくと便利だ。

Controlling printing
----------------------------------------------------------------------

印刷をさらに制御するには :kbd:`Ctrl` + :kbd:`P` 押しで :guilabel:`Print` ダイア
ログボックスを開く。

:guilabel:`Pre&view` チェックボックスをオンにすると便利だ。

General tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Printer` では印刷機自体の選択、それに対するオプション設定を行う。

:guilabel:`Range and Copies` では次を指定する：

* 印刷するシートとページ
* 片面印刷または両面印刷
* 印刷部数
* 複数部数を丁合するかどうか、
* 印刷するページの順序

:guilabel:`Page Layout` では次を指定する：

* 用紙サイズ
* 縦向き、横向き
* 用紙当たりに印刷するページ数
* 用紙内で印刷する順番
* 各ページの周囲に枠線を引くかどうか

LibreOffice Calc tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

空のページをどう扱うかを指定するだけか。

Printing multiple pages on a single piece of paper
----------------------------------------------------------------------

スプレッドシートの複数ページを紙一枚に印刷する手順：

#. 上述の手順で :guilabel:`Print` ダイアログボックスを開く。
#. :guilabel:`General` タブ :guilabel:`Page Layout` 区画 :guilabel:`Pages per
   sheet` ドロップダウンリストで用紙一枚当たりに印刷するシートのページ数を選択す
   る。
#. 用紙一枚にページを複数印刷する場合には :guilabel:`Order` ドロップダウンリスト
   で印刷順序を選択する。
#. シートの各ページを区別するには :guilabel:`Dra&w a border around each page` を
   オンにする。
#. :guilabel:`&Print` を押す。

Selecting what to print
----------------------------------------------------------------------

:guilabel:`&From which` ドロップダウンリストで :guilabel:`Print All Sheets` を選
択すると、文書内のシートすべてが印刷される。単一シート、複数シート、セルを選択し
て印刷することも可能だ。

シートを一枚ずつ or シート範囲を印刷する手順：

#. スプレッドシートでシートタブをクリックして印刷対象シートを選択する。
#. 上述の方法で :guilabel:`Print` ダイアログボックスを開く。
#. :guilabel:`&From which` ドロップダウンリストで :guilabel:`Print Selected
   Sheets` を選択する。
#. :guilabel:`&Print` を押す。

セルの選択を印刷する手順：

#. スプレッドシートで印刷するセルを選択する。
#. :guilabel:`Print` ダイアログボックスを開く。
#. :guilabel:`&From which` ドロップダウンリストで :guilabel:`Print Selected
   Cells` を選択する。
#. :guilabel:`&Print` を押す。

Printing in grayscale on a color printer
----------------------------------------------------------------------

カラープリンターでもスプレッドシートをモノクロ印刷したい場合がある。

個々のファイルについて、プリンター設定を変更してモノクロ印刷することが可能。

#. :guilabel:`Print` ダイアログボックスを開く。
#. :guilabel:`Printer` の :guilabel:`Properties...` を押す。
#. この画面は印刷機によって異なるが、色設定の項目があるはずだ。白黒印刷が有効に
   なるオプションを選択する。

次の方法を採ると、Calc だけでなく LibreOffice すべてのアプリケーションで印刷設定
が変更される：

#. オプションダイアログで :menuselection:`LibreOffice --> Printer` に移動。
#. :guilabel:`Con&vert colors to grayscale` を選択。
#. :guilabel:`&OK` を押す。

Previewing pages/sheets before printing
----------------------------------------------------------------------

印刷前に Calc でシートをプレビューする方法：

#. :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`O` で印刷プレビューモード切り替え
#. :guilabel:`Print Preview` ツールバーが :guilabel:`Formatting` ツールバーと交
   代する。

Using print ranges
======================================================================

* スプレッドシート上のどのセル範囲を印刷するかを定義可能。
* 定義された印刷範囲に含まれないシート上のセルは、印刷されない。
* 印刷範囲が定義されていないシートは印刷されません。
* ユーザー定義の印刷範囲を作成すると、既存の定義済みの印刷範囲が置き換わる。

Defining and printing a print range
----------------------------------------------------------------------

印刷範囲を自分で定義してもよい：

#. セル範囲を選択する。
#. :menuselection:`F&ormat --> Prin&t Ranges --> &Define` を実行する。

オプション設定 :menuselection:`LibreOffice Calc --> View` ページの
:guilabel:`Page breaks` がオンならば自動改頁線が画面上に描かれる。これで印刷範囲
に含まれるセルが定義されている。

Editing a print range
----------------------------------------------------------------------

印刷範囲を編集することが可能。

* セルを追加
* セルを削除
* 繰り返す行や列を定義

#. :menuselection:`F&ormat --> Prin&t Ranges --> &Edit...` を実行する。
#. :guilabel:`Edit Print Ranges` ダイアログボックスが開く。
#. 単一範囲のみが定義されている場合、:guilabel:`Print Range` テキストボックスの
   どこかをクリックすると、定義された印刷範囲が青枠で囲まれて表示される。
#. 複数のセル範囲を定義するには、各セル範囲を ``,`` で区切る。:kbd:`Ctrl` を押し
   ながらセル範囲を選択すれば新しいセル範囲を追加することも可能。
#. :guilabel:`&OK` を押す。

Viewing print ranges
----------------------------------------------------------------------

* 印刷範囲定義後、改頁は自動的になされる。
* :menuselection:`&View --> &Page Break` で改頁プレビュー、
  :menuselection:`&View --> &Normal` で改頁プレビュー終わり。

印刷範囲は、既定では青枠で囲まれ、各ページの中央に薄い灰色のページ番号が示され
る。非印刷領域は灰色の背景。

Named print ranges
----------------------------------------------------------------------

繰り返し印刷するセル範囲を定義することも可能。スプレッドシートの異なる領域を異な
る報告書用に印刷する場合に便利だ。このような用途に名前付き印刷範囲を複数定義する
ことが可能だ。

Defining and naming
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. 対象セルを選択する。
#. :menuselection:`&Sheet --> &Named Ranges and Expressions --> &Define...` を実
   行して :guilabel:`Define Name` ダイアログボックスを開く。
#. :guilabel:`&Name` 欄に名前をタイプする。
#. :guilabel:`Range or formula &expression` のセル範囲を調整してもよい。
#. :guilabel:`&Scope` ドロップダウンリストは :guilabel:`Document (Global)` のま
   まにする。
#. 下部に畳まれている :guilabel:`&Print range` をオンにする。
#. :guilabel:`&Add` を押して確定。

Printing a named range
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. :menuselection:`F&ormat --> Prin&t Ranges --> &Edit...` を実行。
#. :guilabel:`Edit Print Ranges` ダイアログボックスで :guilabel:`Print Range` ド
   ロップダウンリストから使いたい名前付き範囲を選択する。
#. :guilabel:`&OK` を押す。

ワークシートを改頁プレビューモードにしていれば、この時点で上記手順結果が確認でき
る。

Deleting a named print range
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. :menuselection:`&Sheet --> &Named Ranges and Expressions --> &Manage...`
   (:kbd:`Ctrl` + :kbd:`F3`) 実行
#. :guilabel:`Manage Name` ダイアログボックスで対象名前付き範囲を選択
#. :guilabel:`&Delete` ボタン

Removing print ranges
----------------------------------------------------------------------

定義済み印刷範囲を除去する方法：

#. :menuselection:`F&ormat --> Prin&t Ranges --> &Clear`

名前付き印刷範囲を除去する方法はこれとは異なる。すぐ上の節で述べた方法を用いる。

Repeat printing of rows or columns
----------------------------------------------------------------------

スプレッドシートが複数ページに印刷される場合、特定の行または列を定義して、各印刷
ページで繰り返し印刷することが可能。

Using print ranges
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. 上述の方法で :guilabel:`Edit Print Ranges` ダイアログボックスを開く。
#. :guilabel:`Rows to Repeat` 欄には反復して印刷する行の参照を入力する。E.g.
   ``$1``.
#. :guilabel:`Rows to Column` 欄には反復して印刷する列の参照を入力する。E.g.
   ``$A``.
#. :guilabel:`&OK`.

Using named print ranges
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

行または列の反復印刷に用いる名前の反復印刷を定義することも可能だ：

#. 先述の方法で、反復印刷する行・列を名前付き定義する。
#. :guilabel:`Define Name` ダイアログボックスで

   * 反復印刷する列と行を定義する。
   * :guilabel:`Repeat column` や :guilabel:`Repeat row` をオンにする。
#. :guilabel:`&Add` を押す。
#. :guilabel:`Edit Print Ranges` ダイアログボックスを開く。
#. :guilabel:`Rows to Repeat`, :guilabel:`Columns to Repeat` ドロップダウンリス
   トに定義済み名前付き印刷範囲を指定する。
#. :guilabel:`&OK` を押す。

Page breaks
======================================================================

ページ分割は列方向と行方向の二種類ある。

* :menuselection:`&Sheet --> Insert Page &Break -->` 各コマンドでセルの上または
  左にページ行分割または列分割を挿入する。
* :menuselection:`&Sheet --> Delete Page &Break -->` 各コマンドは上記それぞれの
  逆操作だ。

改頁プレビューでは太い青線で描かれる。この色はオプション設定で変更可能だ。

Inserting page breaks
----------------------------------------------------------------------

#. 手動改頁を挿入したいセルを選択。
#. :menuselection:`&Sheet --> Insert Page &Break -->` のサブコマンドを列または行
   に応じて実行。

または：

#. :menuselection:`&View --> &Page Break` を実行。
#. 手動改頁を挿入したいセルを選択。
#. 右クリックメニュー :guilabel:`&Row Break` or :guilabel:`&Column Break` を実
   行。

Deleting page breaks
----------------------------------------------------------------------

#. 手動改頁を削除したいところにあるセルを選択。
#. :menuselection:`&Sheet --> Delete Page &Break -->` のサブコマンドを列または行
   に応じて実行。

Deleting multiple page breaks
----------------------------------------------------------------------

手動改頁を一括削除する方法がある。それは右クリックメニューから
:menuselection:`Delete Page &Breaks` を実行することだ。

Printing options for page styles
======================================================================

スプレッドシートにページスタイル (Chapter 5) を使用する場合、ページスタイル内に
印刷オプションを含めることが可能だ。たとえば、ページの順序、詳細、印刷する尺度な
どだ。

:guilabel:`Page Style: Default` ダイアログを開く方法を知る。複数ある：

* メインメニューから :menuselection:`F&ormat --> &Page Style...` コマンドを実行
* サイドバー :guilabel:`Styles` 内で

  1. :guilabel:`Page Styles` ボタンを押して
  2. :guilabel:`Default` 項目右クリックメニューから :guilabel:`&Edit Style...`
     コマンドを実行
* ステータスバー :guilabel:`Default` をダブルクリック

:guilabel:`Sheet` タブの設定に注意する。

.. todo::

   ここに上記タブページにあるオプション項目説明が入る。

Headers and footers
======================================================================

スプレッドシートのヘッダー、フッターをオンにする方法：

* ヘッダーとフッターは、事前に決めたテキストであり、シート領域の外側かつ天井また
  は床下に印刷される。
* ヘッダーとフッターは同じように設定され、同じページスタイルを使用する左右のペー
  ジで中身が異なることが可能。

Setting headers and footers
----------------------------------------------------------------------

:guilabel:`Page Style: Default` ダイアログの :guilabel:`Header` タブと
:guilabel:`Footer` タブでそれぞれ設定可能。

特に :guilabel:`&Edit...` ボタンを押すと、Writer と同じようにフィールドを使って
内容を設定することが可能だ。

#. 対象シートを選択する。
#. 前述のコマンドで :guilabel:`Page Style` ダイアログボックスを開く。
#. :guilabel:`Header` タブをクリックする（以下手順、:guilabel:`Footer` タブでも
   同様に通じる）。
#. :guilabel:`Hea&der on` をオンにする。
#. その他のオプションを要件に応じて入力。
#. :guilabel:`&OK` を押す。

Header or footer contents
----------------------------------------------------------------------

スプレッドシートのヘッダーとフッターには、テキスト用の枠が三つある。各列は空で
も、他の列と異なる内容でもかまわない。

ヘッダーを設定する手順：

#. 対象シートを選択する。
#. :guilabel:`Page Style` ダイアログボックスを開く。
#. :guilabel:`Header` タブをクリックする
#. :guilabel:`&Edit` を押して :guilabel:`Header` ダイアログボックスを開く。

このダイアログボックスは一見込み入った構造だが、各タブの構成はだいたい同一だ。

#. ヘッダーに標準内容を入力するならば、ドロップダウンリストから選択する。
#. ヘッダーに独自内容を入力する場合、テキストを入力するか、:guilabel:`Custom
   header` アイコンを押す。
#. ヘッダーテキストの容姿を変更するには :guilabel:`Text Attributes` をクリックし
   て同名ダイアログボックスを開く。そこでフォントや効果を指定可能。
#. :guilabel:`&OK` を押す。

:guilabel:`Custom header` アイコン各種の意味は試していればわかる。

フッターを設定する手順も同様。

Exporting to PDF
======================================================================

Quick export to PDF
----------------------------------------------------------------------

直近に適用した PDF 設定に基づいてスプレッドシート全体を PDF に保存するには、
:guilabel:`Standard` ツールバー :guilabel:`Export Directly as PDF` アイコンをク
リックするのがよい。

Controlling PDF content and quality
----------------------------------------------------------------------

:guilabel:`PDF Options` ダイアログで出力 PDF のオプションを細かく指定可能。

.. admonition:: 利用者ノート

   職務経歴書やスキルシートを PDF に変換して提出する前に利用したい。

General tab of PDF Options dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

詳細は *Getting Started Guide* を参照。

:guilabel:`Whole Sheet Export` を選択すると、当ダイアログボックスの他の多くの設
定を無視する。

Initial View tab of PDF Options dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

このタブでは PDF ファイルを閲覧プログラムで開くときのコマンドラインオプションを
選択可能。

User Interface tab of PDF Options dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

このタブも。

Links tab of PDF Options dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

このタブではしおりやハイパーリンクの PDF への書き出し方法を選択可能だ。

Security tab of PDF Options dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* PDF ファイルを作成する際に暗号化とパスワードを設定するにはこのタブを使え。
* 暗号化とパスワードを設定することで、印刷の制限や PDF ファイルに対する変更やコ
  ピーを制限する。

:guilabel:`Set Passwords` ダイアログボックスではパスワードを最大二種類設定する。

* :guilabel:`Set open password`: ファイルを開くためのパスワード
* :guilabel:`Set permission password`: 読者が PDF ファイルで許されることを制限す
  るパスワード

権限設定は PDF 閲覧プログラムがその設定を考慮する場合にしか有効でない。

Digital Signatures tab of PDF Options dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: 利用者ノート

   Windows 利用者は無視してよい？ ひとまずノートを割愛。

Exporting to other formats
======================================================================

Calc では次の二つのコマンドの意味を区別している：

* :menuselection:`&File --> Save &As...`: 別のスプレッドシートファイル形式で保存
  する場合
* :menuselection:`&File --> Expor&t...`: Web ページを作成する場合

Emailing spreadsheets
======================================================================

スプレッドシートを電子メールの添付ファイルとして送信する方法：

#. :menuselection:`&File --> Sen&d -->` 各種コマンドを実行：

   * :menuselection:`&Email Document...`: 現在の形式
   * :menuselection:`Email as &OpenDocument Spreadsheet...`: 拡張子 .ods 形式
   * :menuselection:`Email as &Microsoft Excel...`: 拡張子 .xlsx 形式
   * :menuselection:`Email as P&DF...`
#. シートを当該項目形式に変換保存されたファイルが添付された状態のメール草稿編集
   中のメールクライアント画面が開く。それを用いて送信する。

Digital signing of documents
======================================================================

* 文書にデジタル署名するには、個人鍵＝証明書が必要。

  * 個人鍵は秘密鍵と公開鍵の組み合わせとして PC に保存される。
  * 証明書は認証局（民間企業または政府機関）から取得するものだ。
* デジタル署名を文書に適用すると、その内容と署名者の個人鍵からチェックサムが計算
  される。チェックサムと公開鍵が文書とともに保存される。
* 後で LibreOffice で文書を開くと、プログラムはチェックサムを再計算し、保存済み
  チェックサムと比較する。両方が同じであればよい。

  * プログラムは証明書の公開鍵情報を示すこと可能。公開鍵を認証局の Web サイトで
    公開されているそれと比較することが可能。

誰かが文書の何かを変更するとそれによってデジタル署名が破られることを理解しろ。

Windows では署名を検証するための Windows 機能が使用される。証明書の取得方法、管
理方法、署名の検証方法の詳細については LibreOffice ヘルプの記述を参照しろとあ
る。

Applying a digital signature
----------------------------------------------------------------------

以下の手順は、文書に電子署名をする方法の一例だ。実際の手順は OS など、環境により
異なる：

#. ファイルを開く。
#. :menuselection:`&File --> Di&gital Signatures --> Digital Signatu&res...` コ
   マンドを実行。:guilabel:`Digital Signatures` ダイアログボックスが開く。
#. :guilabel:`&Sign Document...` を押す。ダイアログボックスが開く。
#. 使用する証明書を選択して :guilabel:`Si&gn` を押す。ダイアログボックスが閉じ
   る。
#. 証明書が :guilabel:`Digital Signatures` ダイアログボックスに示され、名前横に
   デジタル署名の状態を示す図像が描かれる。
#. :guilabel:`&Close` を押す。

署名のある文書はステータスバーに図像が描かれる。それをダブルクリックすると証明書
が示される。

ファイル一つに署名を複数追加可能。

これが最重要事項なのだが、デジタル署名後に文書に変更を加えると電子署名は自動的に
削除される。再度電子署名を行うには上記の手順を再実施する必要がある。

.. admonition:: 利用者ノート

   以上の手続きは Windows だと難しいかもしれない。

Signing multiple times with the same signature
----------------------------------------------------------------------

ここで述べる複数署名とは、同一著者による異なる署名をも含意する。

既存の記述の値を変更すると、その署名は無効になる。

Digitally signing macros
----------------------------------------------------------------------

文書ではなく、ファイルの部分であるマクロに対して署名をしたい場合には
:menuselection:`&Tools --> &Macros --> Digital &Signature...` コマンドを実行す
る。手続きの流れは同様。

Removing personal data
======================================================================

オプションダイアログの :menuselection:`LibreOffice --> Security` の
:guilabel:`O&ptions...` を押してダイアログを開き、良さそうなオプションをオンにし
ろ。

:menuselection:`&File --> Proper&ties...` コマンドを実行。:guilabel:`General` タ
ブで：

* :guilabel:`&Apply user data` をオフにする
* :guilabel:`&Reset Properties` を押す
