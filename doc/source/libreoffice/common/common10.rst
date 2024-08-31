======================================================================
Chapter 10 Working with File Formats, Security, and Exporting ノート
======================================================================

.. include:: ./common-inc.txt

.. contents:: 章見出し
   :depth: 3
   :local:

File formats
======================================================================

LibreOffice では |ODF| や |PDF| など、以下に示すさまざまな形式のファイルを開くこ
とが可能だ。たいていの場合 LibreOffice がファイル形式を自動的に検出し、形式を明
示的に選択しなくても開くことが可能だ。

Text documents
----------------------------------------------------------------------

Writer は Open Document テキスト形式 (.odt、.ott、.oth、.odm、.fodt) および以下
の形式（さまざまなレガシー形式を含む）を読むことが可能だ：

* Microsoft Word 6.0/95/97/2000/XP/Mac) (.doc, .dot)
* Microsoft Word 2003 XML (.xml)
* Microsoft Word 2007/2010 XML (.docx, .docm, .dotx, .dotm)
* Microsoft WinWord 5 (.doc)
* Microsoft Works (.wps)
* Text |CSV| (.csv)
* DocBook (.xml)
* |HTML| Document (.htm, .html)
* eBook (.pdb)

.. admonition:: 読者ノート

   本稿では本書の一覧から特に重要な形式を抜粋する。以下同様。

Spreadsheets
----------------------------------------------------------------------

Calc では Open Document のスプレッドシート形式 (.ods, .ots, .fods) のほか、以下
の形式（さまざまなレガシー形式を含む）を開くことが可能だ：

* Microsoft Excel 97/2000/XP (.xls, .xlw, and .xlt)
* Microsoft Excel 4.x-5.0/95 (.xls, .xlw, and .xlt)
* Microsoft Excel 97-2003 (.xml)
* Microsoft Excel 2007-365 (.xlsx, .xlsm, .xltx, .xltm)
* Microsoft Excel 2007-2010 binary (.xlsb)
* Rich Text Format (.rtf)
* Text |CSV| (.csv, .txt)
* |HTML| Document (.htm, .html)

Presentations
----------------------------------------------------------------------

Impress はさまざまな Open Document プレゼンテーション形式 (.odp, .odg, .otp,
.fopd) のほか、以下の形式を開くことが可能だ：

* Microsoft PowerPoint 97/2000/XP (.ppt, .pot)
* Microsoft PowerPoint 2007-365 (.pptx, .pptm, .potx, .potm)
* Portable Document Format (.pdf)

Graphics
----------------------------------------------------------------------

Draw では、Open Document の画像ファイル形式 (.odg, .otg) や |PDF| ファイルのほ
か、以下の画像形式を使用可能だ：

* Adobe Photoshop (.psd)
* Microsoft Publisher 98-2010 (.pub)
* Microsoft Visio 2000-2013 (.vdx; .vsd; .vsdm; .vsdx)
* Bitmap (.bmp)
* |JPG| (.jpeg, .jpg)
* Picture Exchange (.pcx)
* Truevision TGA (.tga, .icb, .vda, .vst)
* Drawing Exchange Format, or Drawing Interchange Format (.dxf)
* Portable Gray Map (.pgm)
* |TIFF| (.tif, .tiff)
* Windows Metafile (.wmf)
* Enhanced Windows Metafile (.emf)
* |PNG| (.png)
* Portable Pixmap (.ppm)
* |SVG| (.svg)
* |GIF| (.gif)

Formulas
----------------------------------------------------------------------

Math は OpenOffice.org 1.x (.sxm), StarMath (.smf), MathML (.mml) ファイルで使用
されている形式と同様に、Open Document Formula ファイル (.odf) を利用可能だ。

数式が埋め込まれた Word 文書を開くとき、|OptionsDlg|
:menuselection:`Load/Save-->MicroOffice` ページで :guilabel:`MathType to
LibreOffice Math or reverse` がオンである場合、MS 数式は LibreOffice Math 数式に
自動的に変換される。

File formats for saving
======================================================================

LibreOffice ではファイルを |ODF| 形式で保存するのが強く推奨される。ただし、必要
に応じて他の形式で保存することも可能だ。

.. tip::

   文書を共有する必要があり、内容をもう変更する予定がない場合、|PDF| に変換する
   ことが望ましい。LibreOffice ではその変換は用意だ。

Text documents
----------------------------------------------------------------------

|ODF| 以外の保存可能形式は次のとおり：

* Microsoft Word 2007-365 (.docx, .dotx)
* Microsoft Word 97-2003 (.doc)
* Microsoft Word 2003 XML (.xml)
* Rich Text Format (.rtf)
* Text (.txt)
* |HTML| Document (.html, .htm)
* DocBook (.xml)

.. note::

   LibreOffice はパスワードで保護された Microsoft Word 文書を保存可能だ。

Spreadsheets
----------------------------------------------------------------------

|ODF| スプレッドシート形式 (.ods, .ots, and .fods) のほか、次の形式で保存可能：

* Microsoft Excel 2007-365 XML (.xlsx)
* Microsoft Excel 97-2003 (.xls, .xlw)
* Microsoft Excel 97-2003 Template (.xlt)
* Text |CSV| (.csv; .txt)
* Microsoft Excel 2003 XML (.xml)
* |HTML| Document (Calc) (.html, .htm)

Presentations
----------------------------------------------------------------------

|ODF| (.odp, .otp, .fodp, .odg) のほか、次の形式で保存可能。また、Draw 互換の画
像形式への書き出しも可能：

* Microsoft PowerPoint 2007-365 (.pptx, .potm)
* Microsoft PowerPoint 2007-365 AutoPlay (.ppsx)
* Microsoft PowerPoint 97-2003 (.ppt)
* Microsoft PowerPoint 97-2003 Template (.pot)
* Microsoft PowerPoint 97-2003 AutoPlay (.pps)

Drawings
----------------------------------------------------------------------

Draw は |ODF| Drawing 形式で保存でき、画像形式 BMP, |EPS|, |GIF|, |JPG|, |PNG|,
|SVG|, |TIFF| などにエクスポートすることも可能だ。

Writer/Web documents
----------------------------------------------------------------------

Writer/Web は次の形式で保存可能：

* |HTML| document (.html, .htm), as HTML 4.0 Transitional
* Text and Text Encoded (LibreOffice Writer/Web) (.txt)

Exporting files
======================================================================

LibreOffice では、ファイル形式が変更されるファイル操作に対してエクスポートという
用語を使用する。Save As コマンドとは異なり、Export コマンドでは実際の文書の現在
のファイル形式を維持したまま文書が作成される。|MenuBar| |SaveAsM| でファイル形式
が見つからない場合は、|FileExportM| でファイル形式を確認しろ。

|PDF| ファイル形式が必要な場合、LibreOffice は Writer, Calc, Impress, Draw の文
書を |PDF| でエクスポート可能だ。Writer は |EPUB| で書き出すことも可能。また、
LibreOffice は |HTML| および |XHTML| 形式でファイルをエクスポート可能。Draw と
Impress がエクスポート可能な画像ファイル形式もある。

.. note::

   Export コマンドを使用すると、LibreOffice は選択された形式を使用して、ファイル
   の複製を新規ファイルとして作成する。元のファイルは LibreOffice で開いたままだ。

PDF quick export
----------------------------------------------------------------------

ファイルを |PDF| 形式に急速にエクスポートする必要がある場合、LibreOffice はファ
イル形式、ページ範囲、画像圧縮などのさまざまなファイル選択肢を使用者に選択させな
い。|PDF| 形式で急速にエクスポートするには次の手順を実行する：

#. 対象のファイルを LibreOffice で開く。
#. |ExportDlg| を開くために次のいずれかの方法を使う：

   * |StandardToolbar| :guilabel:`Export Directly as PDF` 図像をクリックする。
   * |MenuBar| :menuselection:`&File-->&Export As-->Export &Directly as PDF...`
     を選択する。
#. |ExportDlg| でファイル名を入力し、|PDF| ファイルを出力する場所を選択する。
#. |Save| を押してファイルを作成し、|ExportDlg| を閉じる。

.. note::

   既定では、|PDF| ファイルは中身の改竄や編集から保護されていない。|PDF| ファイ
   ルの内容は LibreOffice Draw などの専用ソフトウェアで編集することが可能だ。

Controlled PDF export
----------------------------------------------------------------------

|PDF| でエクスポートされるファイルの内容や品質をさらに制御する必要がある場合は、
|PDFOptionsDlg| で以下の操作を行う。

#. 対象のファイルを LibreOffice で開く。
#. :menuselection:`&File-->&Export As-->&Export as PDF...` を選択して
   |PDFOptionsDlg| を開く。
#. 各タブページで必要な選択肢を選択する。
#. |ExportB| を押して |ExportDlg| を開く。あとは分かるだろう。

General PDF options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|PDFOptionsDlg| |GeneralTab| で利用可能な選択肢。

Range
   |PDF| ファイルに含まれるページを設定する。

   :guilabel:`&Pages` ならばエクスポートするページを直接指定する。必要であれ
   ば、``3-6;8;10;12`` のような書式を使って、ページ範囲と単一ページを組み合わせ
   て指定可能。

   :guilabel:`&Selection` ならば現在の選択すべてをエクスポートする。

   :guilabel:`&View PDF after export` をオンにすると、エクスポート実行後に既定の
   |PDF| 閲覧ソフトで開いてしまう。
Images
   |PDF| ファイル内の画像のオプションを設定する。既定の :guilabel:`&Lossless
   compression` のままだとファイルサイズが大きくなることに注意したい。
Watermark
   ページの背景中央に薄緑色の透かしテキストを追加する。透かしは元文書の部分では
   ない。

   :guilabel:`Sign with &watermark` 欄に透かし署名に必要なテキストを記入する。こ
   の選択肢を選択すると、透かし署名が |PDF| ページに描かれる。
General
   一般的な |PDF| エクスポート選択肢を設定する。

   :guilabel:`Tagged PDF (add document structure)` をオンにすると、文書内容の構
   造に関する情報を |PDF| ファイルに含める。エクスポートされるタグには、目次、ハ
   イパーリンク、コントロールなどがある。ファイル容量が激増する可能性がある。
Structure
   しおり、コメント、ページレイアウトなど、多様な機能の選択肢を設定する。

   :guilabel:`Export outl&ines` を用いると、Writer 文書のしおりを |PDF| のそれと
   してエクスポートする。アウトライン段落および元文書でハイパーリンクが割り当て
   られているすべての目次項目に対してしおりが作成される。アウトライン階層 1 から
   10 の段落しかエクスポートされない。たとえば、Outline 階層が *Text Body* の場
   合、*Paragraph Style* の既定版である *Title* はエクスポートされない。

   :guilabel:`Comm&ents as PDF annotations` をオンにすると、コメントが註釈として
   |PDF| ファイルに含まれる。LibreOffice で表示されているように Writer 文書のコ
   メントをエクスポートするには、|OptionsDlg| :menuselection:`LibreOffice
   Writer-->Print` ページ内 :guilabel:`Comments` ラジオボタングループで
   :guilabel:`In margins` をオンにする。エクスポートされたページは縮小され、コメ
   ントが余白に配置される。

   :guilabel:`Exp&ort automatically inserted blank pages` をオンにすると、白紙
   ページが |PDF| ファイルに自動的に挟み込まれる。両面印刷する場合に検討するべき
   選択肢だ。たとえば、書籍では通常、奇数（右側）ページから章が始まるように設定
   されている。前の章が奇数ページで終わっている場合、LibreOffice では二つの奇数
   ページの間に空白ページが挟まる。

Initial View PDF options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|PDFOptionsDlg| :guilabel:`Initial View` タブでは、|PDF| ファイルを |PDF| 閲覧
ソフトで既定で開く方法を決定する。

Panes
   基本的には :guilabel:`Out&line and page` を選びたい。ペラ一枚の文書などでは
   :guilabel:`&Page only` でかまわない。
Magnification
   最適値は愛用する閲覧ソフトにより異なると考えられる。:guilabel:`&Default` があ
   まり良くない。:guilabel:`Fit &width` が良いのではないか。
Page layout
   これは文書の目的により選択肢を選ぶのが望ましい。おそらく :guilabel:`&Single
   page` か :guilabel:`Conti&nuous facing` になる。

User Interface PDF options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|PDFOptionsDlg| の :guilabel:`User Interface` タブでは、外部 |PDF| 閲覧ソフトの
インターフェイスの表示方法を指定できる。スライドショーやキオスク型ディスプレイと
して使用される |PDF| ファイルを作成する必要がある場合、これらのオプションは便利
だ。

Window Options
   :guilabel:`&Resize window to initial page`
      初期ページ全体を表示するウィンドウで表示される |PDF| ファイルを生成する。
   :guilabel:`&Center window on screen`
      |PDF| 閲覧ソフトを画面中央に表示させるファイルを生成する。
   :guilabel:`&Open in full screen mode`
      |PDF| 閲覧ソフトを全画面表示モードで開くファイルを生成する。
   :guilabel:`&Display document title`
      |PDF| 閲覧ソフトのタイトバーにファイルタイトルを示すファイルを生成する。
User Interface Options
   メニュー、ツールバー等を隠すかどうかを指定する項目からなる。割愛。
Transitions
   :guilabel:`&Use transition effects` はおそらく Impress 専用。スライド遷移効果
   を |PDF| 効果それぞれにエクスポートする。
Collapse Outlines
   アウトライン木の表示に関わるので、

   :guilabel:`Show &All`
      |PDF| 閲覧ソフトでファイルを開いたときに、すべてのアウトラインレベルをしお
      りとして表示するかどうか。
   :guilabel:`&Visible levels`
      |PDF| 閲覧ソフトでファイルを開いたときに、選択した階層までのしおりを表示す
      る場合に選択する。

Links PDF options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|PDFOptionsDlg| の :guilabel:`Link` タブではアウトラインとハイパーリンクを文書内
でどのように書き出すかを指定する。

General
   :guilabel:`&Export outlines as named destinations`
      オンにすると、文書内の物体名を有効なしおり対象としてエクスポートすることが
      可能になる。これにより、他の文書から名前によって物体をエクスポートすること
      が可能になる。
   :guilabel:`&Convert document references to PDF targets`
      |URL| のファイル名拡張子を ``ODF`` から ``PDF`` に自動的に変換する。参照
      |URL| の拡張子 ``.odt``, ``.odp``, ``.ods``, ``.odg``, ``.odm`` は拡張子
      ``.pdf`` に変換する。
   :guilabel:`Export &URLs relative to file system`
      |URL| はファイルシステム内の相対 |URL| として他の文書にエクスポートする。
Cross-document links
   |PDF| ファイルから他のファイルへのハイパーリンクの処理方法を指定する。

   :guilabel:`&Default mode`
      計算機の OS に従う。
   :guilabel:`&Open with PDF reader application`
      自身以外文書へのリンクは、その文書を現在表示している |PDF| 閲覧ソフトで開
      かれる。そのソフトがハイパーリンク内で指定されているファイル型を扱える必要
      がある。
   :guilabel:`Open &with Internet browser`
      上記項目の Web ブラウザー版。

Security PDF options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|PDFOptionsDlg| :guilabel:`Security` タブではエクスポートされた |PDF| ファイルで
使用される安全保障選択肢を指定する。

.. note::

   パスワードによって設定された文書権限制限は |PDF| 1.5 に準拠した |PDF| 閲覧ソ
   フトによってしか確認されていない。それより古いソフトでは効かない可能性がある。

File Encryption and Permission
   :guilabel:`Set &Passwords...`
      パスワードを入力するダイアログボックスを開く。|PDF| ファイル閲覧者が文書を
      編集または印刷できるパスワードを設定する。
Printing
   :guilabel:`&Not permitted`
      印刷不能。
   :guilabel:`&Low resolution (150 dpi)`
      文書は低解像度でしか印刷されない。この指定を無視するソフトもあるだろう。
   :guilabel:`&High resolution`
      高解像度で印刷可能。
Changes
   :guilabel:`No&t permitted`
      変更不可。
   :guilabel:`&Inserting, deleting, and rotating pages`
      これらの操作を許可する。
   :guilabel:`&Filling in form fields`
      フォーム欄への記入を許可する。
   :guilabel:`&Commenting, filling in form fields`
      コメントとフォーム欄に限り、記入を許可する。
   :guilabel:`&Any except extracting pages`
      ページの抽出を除き、変更をすべて許可する。
Contents
   これらはオンでないと話にならない。

   :guilabel:`Ena&ble copying of content`
      内容はクリップボードにコピーできる。
   :guilabel:`Enable text access for acce&ssibility tools`
      この手段が何なのかわからないが、とにかく有効にする。

Digital Signature PDF options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|PDFOptionsDlg| :guilabel:`Digital Signatures` タブではエクスポートした |PDF|
ファイルにどのように電子署名を付けるかを指定する。

* 電子署名は、|PDF| が本当に元の作者によって作成されたものであり、その文書が署名
  された後に変更されていないことを保証するのに用いられる。
* 署名付き |PDF| エクスポートは、既定の鍵置場かスマートカードにすでに保存
  されている鍵 と X.509 証明書を使う。
* スマートカードを使用する場合、既定の鍵置場で使用にすでに構成されている必要があ
  る。これは通常、スマートカードソフトウェアのインストール時に済んでいる。

.. admonition:: 読者ノート

   この節の内容がまったく理解できないので、丸写ししておく。

Certificate
   :guilabel:`&Use this certificate to digitally sign PDF documents`
      |PDF| エクスポートの署名に使用する証明書を選択する。

      :guilabel:`&Select...`
         :guilabel:`Select Certificate` ダイアログボックスを開く。

         選択した鍵置場で見つかった証明書すべてが表示される。鍵置場がパスワード
         で保護されている場合は、パスワードの入力を求めるプロンプトが表示され
         る。|PIN| で保護されているスマートカードを使用している場合は |PIN| を入
         力するプロンプトが表示される。

         エクスポートした |PDF| の電子署名に使用する証明書を、該当する行をクリッ
         クして選択し :guilabel:`Select` ボタンを押す。

      :guilabel:`Digital Signature` タブの他の欄には証明書が選択された後にのみ出
      入りできる。
   :guilabel:`Certificate &password`
      選択した証明書に関連する秘密鍵を保護するために使用するパスワードを入力す
      る。通常は鍵場所のパスワードだ。
   :guilabel:`&Location`, :guilabel:`Contact &information`, :guilabel:`&Reason`
      |PDF| に適用された電子署名に関する追加情報を記入することができる。これらの
      情報は適切な |PDF| 欄に埋め込まれ、閲覧者に示される。それぞれの欄はすべて
      空白のままでもかまわない。
   :guilabel:`&Time Stamp Authority`
      |PDF| 署名工程が時刻認証局を使って電子署名された時刻標記を取得し、それを署
      名に埋め込む。この時刻標記により、|PDF| の閲覧者は文書署名された時刻を検証
      することができる。

      当欄 |URL| が選択されていない場合、署名に付される時刻標記は現地計算機の現
      在時刻が使用される。

EPUB format export (Writer only)
======================================================================

|EPUB| はスマートフォン、タブレット、計算機、電子書籍閲覧ソフトなどの機器、装置
にダウンロードして読むことができる、拡張子 .epub を持つ電子書籍ファイルのための
標準だ。|EPUB| 形式は中身を含む |HTML| ファイルと、画像などのファイルから構成さ
れるアーカイブファイルとして実装されている。

Writer は |EPUB| にファイルをエクスポートすることができる。テキストのみの文書は
一般的にうまくエクスポートされるが、イラスト、表組、相互参照などで正しくエクス
ポートされないものがある。

Quick EPUB export
----------------------------------------------------------------------

Writer ファイルを |EPUB| ファイル形式に急速エクスポートすることを選択する場合、
|EPUB| ファイルの内容や品質への制御はない。

#. 変換する Writer ファイルを開く。
#. |MenuBar| :menuselection:`&File-->&Export As-->Export Directly &as EPUB` を選
   択し、|ExportDlg| を開く。
#. |EPUB| ファイルを保存するフォルダーに移動する。
#. |FileNameBox| にファイル名を入力する。ファイル形式は .epub 固定。
#. |Save| を押す。

Controlled EPUB export
----------------------------------------------------------------------

出来上がる |EPUB| ファイルの内容と品質を制御するには次のようにする：

#. 変換する Writer ファイルを開く。
#. |MenuBar| :menuselection:`&File-->&Export As-->Export as E&PUB...` を選択し、
   |EPUBExportDlg| を開く。
#. |EPUBExportDlg| の各種選択肢に必要な情報を入力する。詳細は次節を見ろ。
#. |OK| を押して |EPUBExportDlg| を閉じ |ExportDlg| を開く。
#. 以降の手順は急速エクスポートと同じ。

EPUB export options
----------------------------------------------------------------------

.. rubric:: General

:guilabel:`&Version`
   出来上がる |EPUB| ファイルのバージョンを設定する。
:guilabel:`&Split method`
   次の |EPUB| 節の開始を選択する。

   * `Heading`: 文書のアウトライン番号に従って、見出しの次の節を開始する。
   * `Page break`: 改頁で新しい節を開始する。
:guilabel:`&Layout method`
   |EPUB| 文書に生成される配置を決定する。

   * `Reflowable`: 内容は画面に合わせて読者の要求に合わせて配置される。ページス
     タイル情報（ページサイズやヘッダー、フッターなど）がエクスポートされないこ
     とを意味する。
   * `Fixed`: 再配置可能な |EPUB| がその内容に適していない場合、表現をより自由に
     統制できる。

.. rubric:: Customize

:guilabel:`Cover &image`
   自作表紙画像ファイルのパスを入力する。入力項目が空の場合、
   ``cover.{gif,jpg,png,svg}`` のいずれかを指定すると、次の項目で指定されたフォ
   ルダー内の表紙画像を使用する。画像は |EPUB| ファイルに埋め込まれる。
:guilabel:`&Media directory`
   |EPUB| ファイルの自作メディアフォルダーを入力する。ここには上記の表紙画像、自
   作メタデータ、画像リンクを含めることが可能だ。

   既定では、エクスポーターは、現在文書フォルダー内の、自作メディアと自作メタ
   データ用の文書ファイル名と同じ名前のフォルダー内を検索する。たとえば、文書名
   が :file:`MyText.odt` の場合、検索フォルダーは :file:`MyText` だ。

   自作メタデータの場合は、元のファイル名と同じ名前で、拡張子が ``.xmp`` のファ
   イルを与え、内部文書のメタデータを上書きする。上記の例では、自作メタデータは
   :file:`MyText` フォルダーに :file:`MyText.xmp` として存在する必要がある。

   画像リンクが意味することは、相対リンクが画像またはテキストに作成され、メディ
   アフォルダーで利用可能な画像にリンクされている場合、このメディアは |EPUB|
   ファイルでポップアップとして利用可能であることだ。

.. rubric:: Metadata

文書の既定メタデータを上書きする自作メタデータを入力する。これらのテキスト欄は空
白のままにしておくことができる。

:guilabel:`Identi&fier`
   出版の一意の識別子。
:guilabel:`&Title`
   出版の題名を入力。
:guilabel:`&Author`
   出版の著者。
:guilabel:`La&nguage`
   出版の言語。取り得る値については RFC4646 および ISO 639 を参照。
:guilabel:`&Date`
   出版の最終更新日。値は XML Schema date Time に準拠した形式の日付
   (CCYY-MM-DDThh:mm:ssZ) でなければならない。既定値は |ExportDlg| が開いたタイ
   ミングだ。

Creating HTML files
======================================================================

Writer で |ViewWebM| を選択すると、テキスト文書が Web ページとしてどのように描画
されるかが示される。ただし、Web 表示ではどの機能が |HTML| 形式で正しく保存される
か、されないのかが表示されない。テキスト文書から Web ページを作成する方法につい
ては :ref:`common10-anchor-A` を見ろ。

.. admonition:: 利用者ノート

   :menuselection:`&View-->&Normal` で戻す。

Text documents
----------------------------------------------------------------------

以下、「テキスト文書」とは Writer で作成している文書を指す。

.. note::

   テキスト文書を |HTML| や |XHTML| 形式でエクスポートする場合は、文書内でスタイ
   ルを使用することが強く推奨される。テキスト文書を |HTML| として保存することは
   HTML 4.0 Transitional 仕様によって制限されている。事務作業ソフトウェアのテキ
   スト文書は通例、ページ書式など、|HTML| にはない豊富な資源集合を用いる。
   |HTML| 形式でファイルを保存するときに、同じレイアウトを期待できない。

Saving as HTML
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

テキスト文書を |HTML| 形式で保存すると、文書内の画像はすべて埋め込みデータスト
リームとして |HTML| 文書に保存される。画像の場合、|JPG| または |SVG| 形式は
|HTML| として保存され、その他の画像形式はすべて |PNG| として保存される。

テキスト文書から |HTML| ファイルを作成するには |SaveAsM| が使える。保存時に
|FileTypeList| で `HTML Document (Writer) (*.html)` を選択する。

Export as XHTML
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: 読者ノート

   割愛。たぶん実装されてない。

Saving document as a series of web pages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Writer は、大きな文書を目次ページ付きの一連の Web ページとして保存することが可能
だ。

#. 文書内のどの見出しスタイルが新しいページを始めるかを決め、すべての見出しが同
   じ段落スタイル、例えば `Heading 1` になるようにする。
#. |MenuBar| :menuselection:`&File-->Sen&d-->Create &HTML Document` を選択する。
   :guilabel:`Name and Path of the HTML Document` ダイアログボックスが開く。
#. 下部に :guilabel:`Styles` ドロップダウンリストがあるので、そこでどのスタイル
   が新しいページを始めるのかを指定する。
#. |Save| を押して複数ファイルを出力する。作成された |HTML| ファイル群は HTML
   4.0 Transitional 標準に準拠している。

Spreadsheets
----------------------------------------------------------------------

Calc では表計算ファイルを |HTML| 文書として保存可能だ。ファイルがシートを複数含
む場合、追加シートは |HTML| ファイル内で互いに続く。各シートへのリンクは |HTML|
文書の上部に配置される。保存手順の要点を示すと：

* |HTML| ファイルの保存フォルダーを確保する。
* |SaveAsM| が使える。
* |FileTypeList| で `HTML Document (Calc) (.html)` を指定する。

.. admonition:: 利用者ノート

   このスプレッドシートからの HTML 変換機能は意外に便利である可能性がある。家計
   簿で試したら全月のデータが一望できる画面が得られた。

Presentations and drawings
----------------------------------------------------------------------

Exporting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Impress のスライドや Draw の図面は |HTML| 形式で保存することは不可能だが、|HTML|
文書としてエクスポートすることは可能だ。

.. note::

   Impress 文書を |HTML| 形式で保存する場合、生成 |HTML| ファイルには Impress で
   作成されたアニメーションやスライド遷移は保持されない。

   Web ページの設計が以前に作成されていない場合、|HTMLExportDlg| の
   :guilabel:`Assign Design` ページで :guilabel:`Existing` オプションは使用不可。

   当エクスポート機能はファイルを複数生成する。元文書の Web 版に必要なファイルす
   べてを保存するフォルダーを作成する必要がある。そうせずに例えばデスクトップに
   保存すると、|HTML| ファイルと画像ファイルがデスクトップにあふれることになり得
   る。

保存手順は次のとおり：

#. 出力先フォルダーを確保する。
#. |FileExportM| で |ExportDlg| を開く。
#. 先のフォルダーに移動する。
#. 保存事項のうち |FileTypeList| で次のものを指定する：

   * (Impress) `HTML Document (Impress) (.html; .htm)`
   * (Draw) `HTML Document (Draw) (.html; .htm)`
#. |HTMLExportDlg| で必要な選択肢、情報を入力し、:guilabel:`Next` を押してダイア
   ログボックス次のページを開く。
#. |HTML| 設計が望みどおりに完成したら、:guilabel:`Create` を押して
   |HTMLExportDlg| を閉じ、|HTML| ファイルを出力する。

HTML options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: 利用者ノート

   このダイアログボックスがどうしても出せない。保留。

.. _common10-anchor-A:

HTML files using Writer/Web
======================================================================

LibreOffice Writer には |HTML| 形式のファイルを作成、編集、保存できる Writer/Web
という構成がある。Writer/Web は |HTML| 形式の文書を扱う場合にしか使い物にならな
い。

Display modes
----------------------------------------------------------------------

既定では Writer/Web は |HTML| ファイルを Normarl ビューで開く。Writer/Web を Web
ビューに変更するには、|MenuBar| |ViewWebM| を選択する。必要に応じて、Normal
ビューまたは Web ビューを使用して |HTML| 文書の内容を編集および書式設定する。
|HTML| 文書の中身は Web ブラウザーで展示されるように描画される。

Writer/Web は |HTML| 文書のソースコードを表示することも可能だ。|MenuBar|
:menuselection:`&View-->HT&ML Source` を使う。この表示モードは Web ページの書式
やページ要素を変更するために用いる。マークアップの知識と経験が必要だ。

Creating and editing
----------------------------------------------------------------------

|HTML| 文書を作成するには次のようにする：

#. :menuselection:`&File-->&New-->&HTML Document` を選択する。Writer/Web は Web
   表示モードで空白文書を開く。
#. テキスト、画像などの内容物を入力または貼り付けて、文書に中身を追加する。
#. スタイルで中身を編集して書式設定する機能を含め、Writer/Web で利用可能なすべて
   の書式設定資源を使用する。
#. 編集が完了したら、|SaveAsM| で |HTML| ファイル型で文書を保存する。
#. Web ブラウザーで |HTML| 文書を眺め、正しく描画されていることを確認する。

Editing source code
----------------------------------------------------------------------

|HTML| 文書のソースコードを編集するには：

#. |HTML| 文書を開くか作成する。
#. 次のいずれかでビューを開く：

   * |MenuBar| :menuselection:`&View-->HT&ML Source` を選択する。
   * |StandardToolbar| :guilabel:`HTML Source` 図像（中括弧対）をクリックする。
#. ソースコードを編集する。
#. 以下、保存手順に合流。

Previewing HTML documents
----------------------------------------------------------------------

|HTML| ファイルはどの Web ブラウザーでも同じように表示されるわけではないため、複
数のブラウザーで |HTML| 文書を検視する必要がある。LibreOffice で既定の Web ブラ
ウザーを開き、|HTML| 文書ドキュメントを表示するには、次のいずれかの手段をとる：

* |MenuBar| :menuselection:`&File-->Preview in Web &Browser`
* |StandardToolbar| :guilabel:`Preview in Web Browser`
* Web ブラウザーで直接開く。

Writer/Web options
----------------------------------------------------------------------

|OptionsDlg| :menuselection:`LibreOffice Writer/Web` で |HTML| 形式 LibreOffice
文書の基本設定を定義可能だ。

:menuselection:`View`
   テキスト文書の物体表示およびウィンドウ要素の既定の設定を定義する。
:menuselection:`Formatting Aids`
   LibreOffice テキストおよび |HTML| 文書の特定の文字とダイレクトカーソルの表示
   を定義する。
:menuselection:`Grid`
   文書ページに対して構成可能な格子の設定を指定する。この格子は物体の正確な位置
   を決定するのに役立つ。また、この格子を LibreOffice の吸着格子に合わせるように
   設定することも可能だ。
:menuselection:`Print`
   テキストおよび |HTML| 文書に対する印刷設定を指定する。
:menuselection:`Table`
   テキスト文書内の表組の属性を定義する。
:menuselection:`Background`
   |HTML| 文書の背景を指定する。|HTML| 文書を新規に作成する場合と、すでに作成さ
   れている |HTML| 文書に対して有効。この選択肢を使用するには、|HTML| 文書に背景
   が定義されていない必要がある。

Emailing documents
======================================================================

LibreOffice には文書を電子メールの添付ファイルとして送信する方法が複数ある。
文書形式は次の三つから選べる：

* Open Document Format
* Microsoft Office 形式
* Portable Document Format

#. |MenuBar| :menuselection:`&File-->Send-->` から以下のいずれかを選ぶ：

   * :menuselection:`&Email Document...`: 既定のメールプログラムが開き、文書が
     メールメッセージに添付される。
   * :menuselection:`Email as &OpenDocument XXXX...`: LibreOffice 文書形式
     のままファイルを添付する？
   * :menuselection:`Email as &Microsoft XXXX...`: LibreOffice が Microsoft
     Office 形式のファイルを作成し、以下同様。
   * :menuselection:`Email as &PDF...`: |PDFOptionsDlg| がまず開く。次に必
     要な設定を選択し |OK| を押す。以下同様。
#. メールプログラムでメールを送信する。

Files on remote servers
======================================================================

LibreOffice はリモートサーバー [#1]_ に保存されたファイルを開いたり保存したりす
ることが可能だ。

LibreOffice は FTP, WebDav, Windows share, SSH などのよく知られたネットワークプ
ロトコルを使用する文書サーバーを支援している。また、Google Drive や Microsoft
OneNote のような一般的なサービスや、OASIS CMIS 標準を実装した商用およびオープン
ソースのサーバーも支援している。

以下の手順でリモートサーバー接続にアクセスする。実際の手順は OS, 計算機の構成、
リモートファイルサービスの種類によって異なる。

#. 以下のいずれかの方法で |RemoteFilesDlg| を開く：

   * LibreOffice Start Center で :guilabel:`Remote File&s` をクリックする。
   * |MenuBar| :menuselection:`&File-->Open &Remote...` を選択する。
   * |MenuBar| :menuselection:`&File-->Sa&ve Remote...` を選択する。
#. :menuselection:`&Manage Services-->&Add service` を選択して |FileServicesDlg|
   を開く。
#. 選択したファイルサービスによって、リモートサーバーへの接続に必要な引数が異な
   る。
#. テキスト欄に必要な情報を入力する。
#. 必要に応じて :guilabel:`&Label` 欄にリモートサーバーのラベルを入力する。
#. |OK| を押して詳細を保存し |FileServicesDlg| を閉じる。
#. |RemoteFilesDlg| で :guilabel:`&Service` ドロップダウンリストからサービスを選
   択する。
#. リモートファイルがある場所に移動し、必要なファイルを選択する。
#. |OpenB| を押してファイルを開き、|RemoteFilesDlg| を閉じる。

Digital signatures
======================================================================

ファイルに電子署名するには、証明書＝個人鍵が必要だ。個人鍵は秘密鍵と公開鍵の組み
合わせとして、使用する計算機に保存される。これらの鍵は電子署名が適用される際に文
書に追加される。証明書は認証局（民間企業または政府機関）から取得する。

電子署名が文書に適用されると、文書の内容と使用される個人鍵からチェックサムが計算
される。チェックサムと公開鍵は文書とともに保存される。

新しいバージョンの LibreOffice を搭載した別の計算機で文書を開くと、プログラムは
チェックサムを計算し、保存されているチェックサムと比較する。両方のチェックサムが
同じ場合、プログラムは元の文書を開く。

さらに、証明書の公開鍵情報を表示することも可能だ。認証局の Web サイトで公開され
ている公開鍵とこの情報を比較することが可能だ。

Applying digital signatures
----------------------------------------------------------------------

この手順は LibreOffice で文書に電子署名する方法の見本だ。実際の手順は計算機の構
成や OS による。

#. |MenuBar| :menuselection:`&File-->Di&gital Signatures-->Digital
   Signatu&res...` と進み、文書の利用可能な電子署名を一覧表示する
   |DigitalSignDlg| を開く。
#. 文書の保存を催促されたら |Yes| を押す。
#. 必要に応じて :guilabel:`&Sign Document...` ボタンを押して |SelectCertDlg| を
   開く。
#. |SelectCertDlg| で必要な電子署名を選択する。
#. Sign をクリックして文書に電子署名を適用し、|SelectCertDlg| を閉じる。
#. |DigitalSignDlg| で署名リストから必要な電子署名を選択する。
#. |Close| を押して、選択した電子署名を文書に適用し、|DigitalSignDlg| を閉じる。
#. 文書を保存する。

.. note::

   署名された文書は |StatusBar| に電子署名印が表示される。この印をダブルクリック
   すると証明書が表示される。文書一つ電子署名を複数追加可能。

   既存の記述を変更すると電子署名は失効する。ただし、同じ著者による複数の電子署
   名は許容される。各電子署名が異なる記述を持つことができるからだ。

Signature line
----------------------------------------------------------------------

署名欄を含む図版箱を文書に追加することもまた可能だ。著者は任意で文書に署名するこ
とができる。この手法は Writer および Calc 文書で使用可能だ。

Writer または Calc 文書に図版署名箱を追加する手順は次のとおり：

#. |MenuBar| :menuselection:`&Insert-->Signat&ure Line` で |SignLineDlg| を開
   く。
#. 必要な詳細を入力し、必要な選択肢を選択する。
#. |OK| をクリックして |SignLineDlg| を閉じると、署名欄付きの図版箱が文書に入
   る。
#. 署名箱をクリックして選択し、物体選択ハンドルを表示する。
#. 矢印キーを使って、署名箱をページの必要な位置に移動する。通常はページの下部
   だ。
#. 選択した署名箱を右クリックして、|DrawingObjPropToolbar| を開く。
#. :guilabel:`Select anchor for object` をクリックし、ドロップダウンリストの選択
   肢から必要な錨型を選択する。
#. 必要に応じて、|DrawingObjPropToolbar| で利用可能な他の器具を使用して、署名箱
   を文書の要件に合わせて書式設定する。
#. 署名箱の選択を解除して、|DrawingObjPropToolbar| を閉じる。
#. 文書に署名箱を固定して保存する。

Document properties
======================================================================

文書の |PropertiesDlg| を開くには |MenuBar| |FilePropertiesM| を選択する。
|PropertiesDlg| の各タブには文書に関する情報が表示され、文書の性質を変更すること
ができる。

General
----------------------------------------------------------------------

File
   ファイル名
:guilabel:`Change &Password`
   ファイルにパスワードが設定されている場合、パスワードを変更するためのダイアロ
   グボックスを開く。
:guilabel:`&Type`
   現在の文書のファイル型
:guilabel:`&Location`
   ファイルが保存されているフォルダーのパスと名前
:guilabel:`&Size`
   現在の文書の容量をバイト単位で表示
:guilabel:`&Created`
   ファイルが最初に保存された日時と作者
:guilabel:`&Modified`
   最後に LibreOffice ファイル形式で保存された日時と作者
:guilabel:`Template`
   ファイルの作成に使用された雛形
:guilabel:`&Digitally signed`
   ファイルが最後に署名された日時と署名者の名前
:guilabel:`Di&gital Signatures...` ボタン
   |DigitalSignDlg| を開き、現在の文書の電子署名をやりくりする。
:guilabel:`Last pri&nted`
   ファイルが最後に印刷された日時と使用者名

   .. note::

      印刷後、最後に印刷したデータを保存するには文書を保存する必要がある。

:guilabel:`Total &editing time`
   ファイルが作成されてから編集のために開いていた時間。編集時間はファイルが保存
   されると更新される。
:guilabel:`Re&vision number`
   ファイルの保存回数

   :guilabel:`&Apply user data`
      使用者の完全名をファイルに保存する。使用者データは |OptionsDlg|
      |UserDataPage| で変更可能。
   :guilabel:`&Reset Properties` ボタン
      編集時間をゼロに、作成日時を現在の日時に、バージョン番号を 1 にリセットす
      る。変更日と印刷日を削除する。
   :guilabel:`Save preview &image with this document`
      サムネイルプレビューを文書内に |PNG| 形式で保存する。この画像を特定の条件
      下で Windows Explorer などのファイルマネージャーが使用することがある。
   :guilabel:`Pre&ferred resolution for images`
      希望する画像解像度を :abbr:`ppi (points per inch)` 単位で入力する。Writer,
      Impress, Draw 文書に画像を入れ、リストボックスの値に従って画像の寸法を変更
      する際の既定値として使用される。
|ResetButton|
   文書に加えられた変更をすべてリセットする。|PropertiesDlg| のタブすべてで利用
   可能。

Description
----------------------------------------------------------------------

文書に関する編集可能な記述情報を任意で含む。他のファイル形式にメタデータとしてエ
クスポートされる場合がある。

:guilabel:`&Title`
   文書の表題を記入する。
:guilabel:`&Subject`
   文書の件名を記入する。件名は類似する内容の文書を括るのに使用する。
:guilabel:`&Keywords`
   文書の内容を索引化するために必要な単語を記入する。キーワードはカンマで区切る。
   キーワードには空白文字やセミコロンを含めることが可能だ。
:guilabel:`&Comments`
   文書を特定するためのコメントを記入する。

.. tip::

   表題、件名、キーワードは |PDF| Document Properties として |PDF| ファイルにエ
   クスポートされます。入力された値はエクスポートされ、|PDF| Document Properties
   Description の対応する欄に表示される。

Custom Properties
----------------------------------------------------------------------

文書に自作情報欄を追加できる。新しい文書ではこのページは空白の場合がある。新しい
文書が雛形に基づいている場合、このページは自作性質を含むことがある。

Properties
   各自作性質に必要な :guilabel:`Name`, :guilabel:`Type`, :guilabel:`Value` を記
   入する。メタデータとして他のファイル形式にエクスポートされる。
:guilabel:`&Add Property` ボタン
   押すと自作性質一覧に新しい行が追加される。

Security
----------------------------------------------------------------------

現在の文書のパスワードオプションを設定する。

:guilabel:`&Open file read-only`
   この文書を読み取り専用モードでしか開くことを許可しない場合に選択する。

   .. note::

      読み取り専用は偶発的な変更から文書を保護する。文書の複製を編集し、それを元
      の文書と同じ名前で保存することならば可能だ。

:guilabel:`Record &changes`
   変更の記録を有効にする場合に選択します。|MenuBar| |EditTrackRecordM| と同じ。

   .. tip::

      記録状態をパスワードで保護するには :guilabel:`&Protect...` ボタンを押し、
      パスワードを入力する。この文書の他の読者は変更を適用することは可能だが、パ
      スワードを知らなければ変更の記録をさせなくすることは不可能だ。

Font
----------------------------------------------------------------------

:guilabel:`&Embed fonts in the document` を選択すると、文書で使用されているフォン
トすべてが文書保存時に埋め込まれる。|PDF| を作成する際に、他の計算機での表示方法
を制御したい場合に便利だ。

:guilabel:`&Only embed the fonts that are used in documents`: 雛形などで文書に
フォントが定義されているが使用されていない場合、この選択肢を選択することでフォン
トを埋め込まない。Latin, Asian, Complex からどのフォントを埋め込むかを選択可能
だ。

Font Embedding
   この選択肢を選択すると、文書フォントが文書ファイルに埋め込まれ、異なる計算機
   間で運べるようになる。フォントが埋め込まれた文書は容量が大きくなる。対象計算
   機で埋め込みフォントが使用され、文書レイアウトの描画が向上する。

   文書使用ではまれなフォントや、他の計算機では一般的に利用できない自作フォント
   が使用されている場合は、フォント埋め込みを検討しろ。

   .. note::

      フォントライセンスが文書へのフォントの埋め込みを制限することがある。フォン
      トファイルには、文書ファイルに埋め込むことができるかどうか、またどのように
      埋め込むことができるかを示すフラグが含まれている。LibreOffice はこれらのフ
      ラグを解析し、文書ファイルに埋め込むことができるかどうか、またどのように埋
      め込むことができるかを判断する。埋め込まれたフォントを含む文書を開くとき、
      LibreOffice はこれらのフラグを見て、文書の表示や編集が可能かどうかを判断す
      る。

Font scripts to embed
   埋め込むフォントの種類を Latin, Asia, Complex から選択する。

Statistics
----------------------------------------------------------------------

現在のファイルの統計情報（ページ数、単語数、文字数など）を表示する。

Document classification
======================================================================

.. |BAF| replace:: :abbr:`BAF (Business Authentication Framework)`
.. |BAILS| replace:: :abbr:`BAILS (Business Authorization Identification and Labeling Scheme)`

LibreOffice は :abbr:`TSCP (Transglobal Secure Collaboration Participation,
Inc)` が作成した |BAF| 区分三つを含む開かれた標準を実装している：

* 知的財産
* 国家安全保障
* 輸出管理

この区分のそれぞれに |BAILS| という文書分類等級が四つある：

* 非業務用
* 一般業務用
* 機密用
* 社内専用

.. admonition:: 読者ノート

   冒頭の解説がよくわからないので後回し。

文書分類を作動させるには |MenuBar| :menuselection:`&View-->&Toolbars-->TSCP
Classification` を選択する。このツールバーはドロップダウンリスト一つを含む。それ
を使って文書保障度を選ぶ。 LibreOffice は文書性質を追加することで分類策を文書の
メタデータとして保管する。

安全保障策の違反を防ぐため、高等級の内容を低等級の文書に貼り付けることは不可能
だ。

Business Authentication Framework (BAF) Categories
----------------------------------------------------------------------

次は LibreOffice 既定の |BAF| 区分だ：

`Intellectual Property`
   一般的な文書の分類にはこの区分を選択する。

   .. tip::

      `Intellectual Properties` 区分は、透かし、ヘッダーとフッターにあるフィール
      ド、文書領域の上部にある情報バーを使って、文書のレイアウトを変更する。文書
      に入る項目は分類構成ファイルが制御する。

`National Security`
   この区分を選択すると文書に国家安全保障策型が割り当てられる。選択された区分は
   |BAILS| メタデータとして文書とともにファイル性質に保存される。文書レイアウト
   や |UI| に変更は生じない。
`Export Control`
   この区分を選択すると文書に輸出管理策型が割り当てられる。後は National
   Security と同様。

.. note::

   文書分類の支援については、企業のデータ保障策および情報保障責任者に問い合わせ
   ろ。

Default levels of classification
----------------------------------------------------------------------

LibreOffice には業務機密度の高い順に並べられた、以下の |BAILS| を既定で用意して
いる：

`Non-Business`
   この文書に記載されている情報を公表しても業務に影響はない。
`General Business`
   軽微な影響。情報を公開すれば業務に影響を与え、恥をかき、ブランドイメージに軽
   微な損害を与えることがある。
`Confidential`
   中程度の影響。開示された情報はブランドを傷つけ、否定的な報道を生み、収益を失
   う可能性がある。
`Internal use only`
   大損害。否定的な国内メディア（の報道？）、訴訟、罰金、長期にわたるブランドへ
   の印象毀損。

.. admonition:: 利用者ノート

   無記名の家計簿は `Non-Business` に位付けてで良かろう。

Customizing classification levels
----------------------------------------------------------------------

.. admonition:: 利用者ノート

   業務に対する分類の等級をカスタマイズすることは |OptionsDlg| を使えば可能だが、
   おそらく実施しないほうがいい。

Pasting contents
----------------------------------------------------------------------

クリップボードの内容が対象文書よりも高い保障分類度であることを LibreOffice が検
出した場合、貼り付けようと試みると警告が出る。

----

.. rubric:: 章末注

.. [#1] ネットワークの向こう側にある計算機。
