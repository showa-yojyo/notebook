======================================================================
Writer Guide Chapter 7, Printing and Publishing ノート
======================================================================

.. include:: ./abbrev.txt
.. |CTL| replace:: :abbr:`CTL (Complex Text Language)`
.. |DPI| replace:: :abbr:`DPI (dots per inch)`
.. |EPS| replace:: :abbr:`EPS (Encapsulated PostScript)`
.. |ISO| replace:: :abbr:`International Organization for Standardization`
.. |PIN| replace:: :abbr:`PIN (Personal Identification Number)`

.. contents:: 本章見出し
   :depth: 3
   :local:

Introduction
======================================================================

LibreOffice Writer 文書の印刷、公開、配布に関する機能について説明する：

* 文書、封筒、付箋を含む印刷
* |PDF|, |EPUB|, その他のファイル形式へのエクスポート
* 文書のメール送信
* 文書の電子署名
* 文書配布前の個人情報の削除
* 改訂
* 公開前文書の accessibility 検査

Quick printing
======================================================================

:guilabel:`Standard` ツールバーに :guilabel:`Print Directl&y` 図像が表示されてい
る場合、それをクリックすると、現在の既定の印刷設定を使用して文書全体を印刷でき
る。図像が表示されていない場合は、ツールバーを右クリックし、
:menuselection:`Visible &Buttons -->` を指して :guilabel:`Print Directl&y` を選
択することで表示させる。

Specifying the default printer
----------------------------------------------------------------------

既定印刷機を指定するにはメニューから :menuselection:`&File --> P&rinter
Settings` を選択する。:guilabel:`Printer Setup` ダイアログボックスが開く。その他
の印刷オプションにアクセスするには :guilabel:`Option&s...` ボタンを押す。

同じ既定オプションは :guilabel:`Options` ダイアログボックスの
:menuselection:`LibreOffice Writer --> Print` で使用でき、より一般的な印刷オプ
ションは :menuselection:`LibreOffice --> Print` で使用できる。詳細については
:doc:`Chapter 20 <writer20>` を見ろ。

Controlling printing using the Print dialog
======================================================================

印刷をより詳細に制御するには :guilabel:`Print` ダイアログボックスを用いる。開き
方は：

* メニュー :menuselection:`&File --> &Print...` を選択
* キーバインド :kbd:`Ctrl` + :kbd:`P`
* :guilabel:`Standard` ツールバーの :guilabel:`&Print` 図像クリック

Print dialog on Windows and Linux
----------------------------------------------------------------------

:guilabel:`Print` ダイアログボックスには二つのタブがあり、以下の節で述べられるさ
まざまな選択肢を取れる。

Selecting general printing options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Print` ダイアログボックスの :guilabel:`General` タブにある選択肢：

* 利用可能な印刷機の一覧から印刷機を選択する
* 印刷するページ、印刷部数、複数部数を照合するかどうか
* 用紙寸法と印刷の向き
* 一枚の用紙に何ページ印刷するか、各ページの周囲に枠線を引くかどうか
* 仮綴本を印刷するかどうか
* ページ順を逆にして印刷するかどうか（一部の印刷機ではページ順に出力するのに便
  利）

Selecting printer and print job options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`General` タブの :guilabel:`Printer` 区画で :guilabel:`Properties` ボ
タンを押すると、選択した印刷機のプロパティダイアログボックスが表示される。そこで
は縦向きまたは横向き、使用する用紙トレイ、印刷する用紙寸法を選択可能だ。

:guilabel:`General` タブの :guilabel:`Range and Copies` 区画の下にある
:guilabel:`Co&llation and Paper Sides` をクリックして、整列したページすべてを含
む一つの印刷ジョブではなく、出力用に別々の印刷ジョブを作成するかどうかを選択す
る。

.. admonition:: 読者ノート

   英語 to collate に「本などのページを集めて正しい順序で並べる」という意味があ
   る。

Selecting what to print
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

文書全体印刷に加えて、ページ単品、ページ範囲、選択部分を印刷することも可能だ。

ページ単品または範囲：

#. :guilabel:`Print` ダイアログボックスの :guilabel:`Range and Copies` 区画で
   :guilabel:`Pa&ges` をオンにする
#. 印刷したいページのページ番号を入力する。左側のプレビュー欄が選択したページ
   を描く。

   * 単品の場合はページ番号だけを記入
   * 範囲の場合はたとえば ``1-4``, ``1,3,7,11``, etc. またはその組み合わせを
     記入

テキストまたは画像の選択：

#. 文書で印刷する素材を選択してから :guilabel:`Print` ダイアログボックスを開く
#. :guilabel:`Print` ダイアログボックスの :guilabel:`Range and Copies` 区画の
   :guilabel:`&Selection` が活動開始。これをオンにする。プレビュー欄に選択素材が
   描かれる。

Choices on the LibreOffice Writer tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`LibreOffice Writer` タブでは、中身の部分集合（画像や隠秘テキストな
ど）を印刷するかどうか、テキストを（色が指定されている場合でも）黒で印刷するかど
うか、自動的に挿入される空白ページを印刷するかどうか、文書内のコメントを印刷する
かどうか、どこに印刷するかを選択可能だ。

選択項目によっては常時使用できないものもある。たとえば、文書にコメントが含まれ
ていない場合、:guilabel:`Co&mments` ドロップダウンリストは無効になる。

Printing multiple pages on a single sheet of paper
----------------------------------------------------------------------

複数ページの文書を一枚の用紙に印刷できる。これを行うには、

#. :guilabel:`Print` ダイアログボックスを開く
#. :guilabel:`General` タブ
#. :guilabel:`Page Layout` 区画で :guilabel:`Pages per S&heet` を展開
#. 一枚の用紙に印刷するページ数を :guilabel:`Pag&es per Sheet` ドロップダウンリ
   ストから選択

一枚に二ページ以上を印刷する場合、用紙の縦横の印刷順序を選択できる。
:guilabel:`Print` ダイアログボックスの左側にあるプレビュー盤が変化し、印刷された
文書の見てくれが描かれる。

Printing a brochure
----------------------------------------------------------------------

一枚の用紙の両面に二ページずつ、印刷したページを二つ折りにしたときにページが正し
い順序で並んで冊子や仮綴本になるように配置した文書を印刷することが可能だ。

.. tip::

   適切な余白、フォントサイズなどを選び、半分の寸法で印刷したときに見栄えがよく
   なるように文書を計画しろ。試行錯誤が必要かもしれない。

片面（単面）印刷機で仮綴本を印刷する手順：

#. :guilabel:`Print` ダイアログボックスの :guilabel:`General` タブの
   :guilabel:`Page Layout` 区画で、いちばん下の :guilabel:`Broch&ure` をオン

   * 左側のプレビューがページが印刷される順序を示すように更新する。
#. 言語設定でアジアまたは |CTL| が選択されている場合、:guilabel:`Print` ダイアロ
   グボックスの :guilabel:`Broch&ure` の近くにドロップダウンリストが表示される。
   この一覧には、

   * :guilabel:`Left-to-right script`
   * :guilabel:`Right-to-left script`

   のオプションがある。必要な設定を選択しろ。
#. :guilabel:`Print` ダイアログボックスの :guilabel:`General` タブの
   :guilabel:`Range and Copies` 区画 :guilabel:`Co&llation and Paper Sides` の下
   にある :guilabel:`Even pages` を選択
#. :guilabel:`&Print` を押す
#. 印刷したページを印刷機から取り出し、正しい向きで印刷機に戻して白紙面に印刷す
   る（印刷機によっては試行錯誤が必要な場合がある）。
#. 今度は :guilabel:`Odd pages` を選択
#. :guilabel:`&Print` を押す

.. tip::

   印刷機が自動的に両面印刷できる場合は :guilabel:`Odd and Even pages` を選択し
   て、印刷実行を一度にすることが可能。

Printing in black and white on a color printer
======================================================================

多色印刷機で文書を白黒で印刷したい場合がある。選択肢がいくつかある。

.. note::

   印刷機によっては選択した設定に関係なく多色刷りになる場合がある。

#. :guilabel:`Print` ダイアログボックスで :guilabel:`Propert&ies...` をクリック
   して印刷機の設定ダイアログボックスを開く。利用可能な選択肢は印刷機によって異
   なるが、カラー設定のオプションが見つかるはずだ。
#. カラーの選択肢には、白黒または無彩色尺がある。無彩色尺を選択する。
#. :guilabel:`&OK` を押す。:guilabel:`Print` ダイアログボックスに戻る。
#. :guilabel:`&Print` を押して文書を印刷する。

すべての彩色テキストと画像を無彩色で印刷するには、LibreOffice の設定を変更する：

#. :guilabel:`Options` ダイアログボックスを開く
#. :menuselection:`LibreOffice --> Print` ページ
#. :guilabel:`Con&vert colors to grayscale` をオン
#. :guilabel:`&OK`

彩色テキストを黒で印刷し、画像を無彩色で印刷するには：

#. :guilabel:`Options` ダイアログボックスを開く
#. :menuselection:`LibreOffice Writer --> Print` ページ
#. :guilabel:`Print text in blac&k` をオン
#. :guilabel:`&OK`

Previewing pages before printing
======================================================================

Writer の通常ページビューでは、各ページが印刷されるときにどのように見えるかが表
示される。このビューでページを編集することも可能だ。両面印刷する文書を設計する場
合、見開きページがどのように見えるかを確認するといいだろう。これを行う方法が二つ
ある：

* :guilabel:`View Layout`: 編集可。Status バーの Book View ボタンを使ってズーム
  を調整する。
* :guilabel:`Print Pr&eview`: 読み取り専用ビュー。

:guilabel:`Print Pr&eview` 実行手順は次のいずれか：

* メニューの :menuselection:`&File --> Print Pr&eview...` を選択
* :guilabel:`Standard` ツールバーの :guilabel:`Toggle Print Preview
  (Ctrl+Shift+O)` 図像をクリック
* キーバインド :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`O`

これで :guilabel:`Formatting` ツールバーの代わりに :guilabel:`Print Preview`
ツールバーが表示する。

#. 必要なプレビュー図像をクリック

   * :guilabel:`Single Page Preview`
   * :guilabel:`Two Pages Preview`
   * :guilabel:`Book Preview`
   * :guilabel:`Multiple Page Preview`

#. このビューから文書を印刷するには :guilabel:`Print` 図像をクリックして
   :guilabel:`Print` ダイアログボックスを開く。印刷オプションを選択し、
   :guilabel:`&Print` を押す。

Printing envelopes
======================================================================

封筒の印刷には組み立てと印刷の二段階からなる。

封筒単品または文書と一緒に印刷するように組み立てる手順：

#. メニューから :menuselection:`&Insert --> En&velope...` を選択
#. :guilabel:`Envelop` ダイアログボックスでは、まず :guilabel:`Envelop` タブから
   始める。

   :guilabel:`Addr&essee` 欄と :guilabel:`&Sender` 欄の情報を確認、追加、編集す
   る。

   * 差出人情報は :guilabel:`Options` ダイアログボックスの
     :menuselection:`LibreOffice --> User Data` ページから取られる。
   * 宛先と差出人の欄には情報を直接入力するか、右側のドロップダウンリストを使用
     して、封筒情報を引き出すデータベースを選択する。データベースから封筒を印刷
     する方法の詳細については :doc:`Chapter 14 <writer14>` を参照。

#. :guilabel:`Format` タブで、宛先と差出人情報の位置を確認または編集する。右下の
   領域はプレビュー。
#. これらのブロックのテキストを書式設定するには、右側の :guilabel:`Edit` ドロッ
   プダウンメニューを押す。二つの選択肢がある

   * :guilabel:`C&haracter...` を選択すると、標準の :guilabel:`Character` ダイア
     ログボックスと同じようなものが開き、テキストの書式を設定することが可能だ。
   * :guilabel:`P&aragraph...` を選択すると、標準の :guilabel:`Paragraph` ダイア
     ログボックスに似たものが開き、段落の属性を設定可能だ。
#. このタブの左下には :guilabel:`Size` 区画がある。ドロップダウンリストから封筒
   の形式を選択する。選択した封筒の幅と高さは、選択した形式の下の欄に表示され
   る。既存形式を選択した場合はこれらの寸法を確認するだけだ。ユーザー定義を選択
   した場合は寸法を編集することが可能になる。
#. 封筒形式指定後、:guilabel:`Printer` タブで、使用する印刷機、組み立て（封筒を
   入れる皿の指定など）、封筒の向きやシフトなどのその他の印刷機オプションを選択
   する。どのオプションが印刷機にとって最適か、また封筒が印刷機内でどのように配
   置される必要があるか、試行を要するかもしれない。
#. 書式設定が終わり、印刷の準備が済んだら :guilabel:`&New Document` または
   :guilabel:`&Insert` のいずれかを押して終了する。

   * :guilabel:`&New Document` は、封筒だけを作成するか、封筒を使って新しい文書
     を開始する。
   * :guilabel:`&Insert` は封筒を既存の文書に一ページ目として挿入する。
#. 他のことをする前にこのファイルを保存しろ。

封筒を印刷するには：

#. メニューから :menuselection:`&File --> &Print...` を選択
#. :guilabel:`Print` ダイアログボックスの :guilabel:`Range and Copies` で
   :guilabel:`Pa&ges` をオンにし、入力欄に 1 を入力する
#. 必要な印刷機（通常の印刷機とは異なる場合がある）を選択
#. :guilabel:`&Print` を押す

Printing labels
======================================================================

付箋は一般的に住所録（各付箋が異なる住所を示す）を印刷するために使用されるが、返
送先住所シールや CD/DVD 用付箋など、一つの付箋を複数部作成するためにも使用できる。

付箋の印刷には、封筒の印刷と同様に、組み立てと印刷という二段階からなる。

Exporting to PDF
======================================================================

LibreOffice では、文書を |PDF| 形式で書き出すことができる。この標準的なファイル
形式は Adobe Reader などの |PDF| 閲覧ソフトを使って、ファイルを人に送信して閲覧
させるのに最適だ。

.. warning::

   |PDF| 文書は既定では内容の捏造や編集から保護されていない。|PDF| 文書の内容は
   LibreOffice Draw などの専用ソフトウェアツールで編集され得る。

.. tip::

   :guilabel:`Save &As...` とは異なり、:guilabel:`Expor&t...` コマンドは選択した
   書式で現在の文書のコピーを新しいファイルに書き込むが、現在の文書と書式はその
   セッションで開いたままになる。

Quick export to PDF
----------------------------------------------------------------------

* :guilabel:`Standard` ツールバーの :guilabel:`Export &Directly as PDF` 図像
* :menuselection:`&File --> &Export As --> Export &Directly as PDF` を選択

:guilabel:`PDF Options` ダイアログボックスで直近に選択した |PDF| 設定を使用して
文書全体が書き出される。ファイル名と保存場所を入力するよう求められるが、ページ範
囲や画像圧縮、その他のオプションを選択する機会はない。

Controlling PDF content and quality
----------------------------------------------------------------------

作成される |PDF| の内容と品質をより精緻に制御するには :menuselection:`&File -->
&Export As --> &Export as PDF` を使用する。:guilabel:`PDF Options` ダイアログ
ボックスが開く。このダイアログボックスには六つのタブ

* :guilabel:`General`
* :guilabel:`Initial View`
* :guilabel:`User Interface`
* :guilabel:`Links`
* :guilabel:`Security`
* :guilabel:`Digital Signatures`

がある。適切な設定を選択し、:guilabel:`E&xport` を押す。次に、作成する |PDF| の
場所とファイル名を入力するよう求められ、:guilabel:`保存 (&S)` を押してファイルを
エクスポートする。

.. note::

   :menuselection:`&File --> Expor&t...` でも |PDF| にエクスポート可能だ。
   :guilabel:`Export` ダイアログボックスで |PDF| 形式、ファイル名、保存場所を選
   択し、:guilabel:`保存 (&S)` を押す。その後、:guilabel:`PDF Options` オプショ
   ンダイアログボックスが開く。適切な設定を選択し :guilabel:`E&xport` をクリック
   する。二つのエクスポート方法の唯一の違いは、手順を実行する順序だ。

General tab of PDF Options dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`General` タブでは |PDF| に含めるページ、画像に使用する圧縮の種類、そ
の他のオプションを選択できる。

:guilabel:`Range` 区画
   :guilabel:`&All`
      文書全体を |PDF| エクスポートする。
   :guilabel:`&Pages`
      ページの範囲をエクスポートするには、例えば ``3-6`` のように指定する。単一
      ページをエクスポートするには ``7;9;11`` というような記法を用いる。また、
      ``3-6;8;10;12`` のような記法でページ範囲と単一ページを組み合わせてエクス
      ポートすることもできる。
   :guilabel:`&Selection`
      選択されている素材すべてをエクスポートする。
   :guilabel:`&View PDF after export`
      既定の |PDF| 閲覧ソフトが開き、新しくエクスポートされた |PDF| が表示され
      る。
:guilabel:`Images` 区画
   :guilabel:`&Lossless compression`
      画質を損なうことなく画像を保存できる。写真に使用するとファイルが大きくなる
      傾向がある。その他の画像や画像にお勧め。
   :guilabel:`&JPEG compression`
      画質の程度を変えることができる。90% に設定すると写真に対してよく働く。ファ
      イルサイズが小さく、画質の低下はほとんど感じられない。
   :guilabel:`Reduce ima&ge resolution`
      |DPI| の低い画像は品質が低いということだ。低い解像度（100 dpi 以下）でもコ
      ンピューターの画面で見るには十分かもしれないが、最近のデバイスの多くはもっ
      と高い解像度を持っている。印刷する場合は、印刷機の能力にもよるが、少なくと
      も 300 dpi か 600 dpi を使うのが一般的に望ましい。|DPI| 設定を高くすると
      ファイルサイズが大きくなる。

.. note::

   プレビューが埋め込まれた |EPS| 画像はプレビューとしてのみ書き出される。プレ
   ビューが埋め込まれていない |EPS| 画像は、空のプレースホルダーとして書き出され
   る。

:guilabel:`Watermark` 区画
   :guilabel:`Sign with &watermark`
      これをオンにすると隣のテキスト欄に入力したテキストの透明なオーバーレイが
      |PDF| の各ページに表示される。
:guilabel:`General` 区画
   :guilabel:`Hybrid PDF (em&bed ODF file)`
      二つのファイル形式を含む |PDF| として文書をエクスポートするにはこの設定を
      使用する。|PDF| 閲覧ソフトでは通常の |PDF| ファイルのように動作し、
      LibreOffice では完全に編集可能のままだ。
   :guilabel:`Archival (P&DF/A, ISO 19005)`
      PDF/A は文書の長期保存のための |ISO| 規格で、忠実な複製に必要なすべての情
      報（フォントなど）を埋め込む一方、その他の要素（フォーム、セキュリティー、
      暗号化など）を禁止している。|PDF| タグが記述されている。

      * :guilabel:`PDF/A-1b` は PDF/A-1 への最低準拠レベルを指す。
      * :guilabel:`PDF/A-2b` は図形や画像のレイヤーや透過が可能なので、ほとんど
        の使用者に推奨される。また、圧縮率が高く、通常より小さなファイルを作成す
        る。
      * :guilabel:`PDF/A-3b` は PDF/A-2b と同じだが、他のファイル形式の埋め込み
        も可能だ。
   :guilabel:`Universal Accessibilit&y (PDF/UA)`
      PDF/UA (|ISO| 14289) 仕様の要件に従った、普遍的な accessibility 準拠 |PDF|
      ファイルを作成する。これがオンの場合、:guilabel:`&Export` を押すと、文書に
      accessibility の問題が含まれている場合に警告ダイアログボックスがポップアッ
      プ表示される。
   :guilabel:`&Tagged PDF (add document structure)`
      タグ付き |PDF| には文書の内容の構造に関する情報が含まれている。これは、異
      なる画面を持つデバイスや、画面読み上げソフトウェアを使用する際に、文書を表
      示するのに役立つ。書き出されるタグには、目次、ハイパーリンク、コントロール
      などがある。このオプションを使用すると、ファイルサイズが大幅に増加する可能
      性がある。
   :guilabel:`Create PDF for&m` - :guilabel:`Submit &format`
      |PDF| ファイル内からフォームを提出する形式を選択する。この設定は文書内で設
      定したコントロールの URL プロパティーを上書きする。|PDF| 文書全体で有効な
      共通の設定は一つしかない：

      * :guilabel:`PDF`: 文書全体を送信
      * :guilabel:`FDF`: コントロールの内容を送信
      * :guilabel:`HTML`
      * :guilabel:`XML`

      ほとんどの場合、|PDF| 形式を選択するだろう。
   :guilabel:`Allow duplicate field &names`
      オンにすると、生成される |PDF| ファイル内の複数のフィールドに同じ名前を使
      用することができる。|PDF| 文書内で最初に出現する名前付きフィールドにデータ
      を入力することができ、同じ名前を持つすべてのフィールドに入力内容が反映され
      る。オフにすると、一意に生成された名前を使ってエクスポートされる。

.. tip::

   商業印刷サービスで |PDF| に透明部分が含まれていないことが要求するものがある。
   対策は :guilabel:`PDF/A-1b` を選択し、:guilabel:`Create PDF for&m` をオフにし
   ろ。

:guilabel:`Structure` 区画
   :guilabel:`Export outl&ines`
      Adobe Reader を含む |PDF| 閲覧ソフトのほとんどで表示されるアウトライン（目
      次一覧）として見出しをエクスポートする。
   :guilabel:`Expo&rt placeholders`
      |PDF| には定義されたプレースホルダーフィールドがすべて含まれ、使用者が入力
      することが可能。
   :guilabel:`Comm&ents as PDF annotations`
      コメントは注釈として |PDF| に含まれる。
   :guilabel:`&Comments in margin`
      ページの内容が縮小され、余白にコメントを印刷する余地が残る。
   :guilabel:`Exp&ort automatically inserted blank pages`
      自動的に挿入された白紙ページが |PDF| に書き出される。これは両面印刷する場
      合に最適だ。たとえば、書籍では通常、章が常に奇数ページから始まるように設定
      されている。前の章が奇数ページで終わると、Writer は二つの奇数ページの間に
      空白ページを挿入する。このオプションは、その白紙ページを書き出すかどうかを
      制御する。
   :guilabel:`&Use reference XObjects`
      参照 XObject は、ある |PDF| ファイルが別の |PDF| ファイルから中身を取り込
      むことを可能にする。詳細は `PDF specification, ISO 32000-2:2017
      <https://www.iso.org/standard/63534.html>`__ の節 8.10.4 に記載されてい
      る。referenceXObjects に慣れていない場合はこの欄をオフのままにしろ。

Initial View tab of PDF Options dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Initial View` タブでは |PDF| を閲覧ソフトが既定で開く方法を選択でき
る。選択内容は自明のはずだ。

|CTL| を有効にしている [#ctl]_ 場合、:guilabel:`Conti&nuous facing` オプションの
下に追加の選択肢がある：

:guilabel:`First page is &left`
   :guilabel:`Conti&nuous facing` は、通常、最初のページは右だ。

User Interface tab of PDF Options dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`User Interface` タブでは |PDF| 閲覧ソフトが内容をどのように表示するか
を制御するためのさらなる設定を行う。説明会で、あるいはキオスク型ディスプレイで使
用する |PDF| を作成している場合に特に便利な選択肢がいくつかある。

:guilabel:`Window Options` 区画
   :guilabel:`&Resize window to initial page`
      ウィンドウを PDF の最初のページに合うようにリサイズする。
   :guilabel:`&Center window on screen`
      ウィンドウを画面の中央に表示する。
   :guilabel:`&Open in full screen mode`
      全画面モードで開く。
   :guilabel:`&Display document title`
      ウィンドウの表題バーに文書の表題を表示する。
:guilabel:`User Interface Options` 区画
   :guilabel:`Hide &menubar`
      メニューを隠す。
   :guilabel:`Hide &toolbar`
      ツールバーを隠す。
   :guilabel:`Hide &window controls`
      その他のウィンドウコントロールを隠す。
:guilabel:`Transitions`
   Writer では使用不能。
:guilabel:`Collapse Outlines`
   :guilabel:`General` タブで :guilabel:`Export outl&ines` がオンになっている場
   合、アウトラインに表示される見出しレベルの数を指定する。

Links tab of PDF Options dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Links` タブでは文書内のリンクを |PDF| に書き出す方法を選択できる。

:guilabel:`General` 区画
   :guilabel:`&Export bookmarks as named destinations`
      Web ページ や |PDF| 文書がリンクできる「名前付き宛先」としてしおりがエクス
      ポートされる。
   :guilabel:`&Convert document references to PDF targets`
      OpenDocument の拡張子 (.odt, .ods, .odp, etc.) を持つ他の文書へのリンクを
      定義している場合、書き出された |PDF| 文書では、そのファイル拡張子は .pdf
      に変換される。
   :guilabel:`Export &URLs relative to file system`
      文書内で相対リンクを定義している場合、このオプションはそれらのリンクを
      |PDF| にエクスポートする。
:guilabel:`Cross-document Links`
   |PDF| ファイル内でクリックされたリンクの動作を定義する。三択。

   :guilabel:`&Default mode`
      リンクは OS 指定の処理をされる。
   :guilabel:`&Open with PDF reader application`
      リンクされた |PDF| 文書を開くには、それを表示するのに使用したのと同じアプ
      リケーションを使用する。
   :guilabel:`Open &with Internet browser`
      リンクされた |PDF| 文書を表示するのに既定の Web ブラウザーを使用する。

Security tab of PDF Options dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|PDF| 書き出しには、中身を（パスワードなしでは開かないように）暗号化し、いくつか
のデジタル著作権管理機能を適用するオプションがある。

* :guilabel:`Set open password` を設定すると、|PDF| はそのパスワードでしか開かな
  い。いったん開くと、使用者がその文書で行えること（例：印刷、コピー、変更）に制
  限はない。
* :guilabel:`Set permission password` を設定すると、誰でも開くことができるが、そ
  の権限を制限することができる。アクセス許可のパスワードを設定すると、
  :guilabel:`Security` ページの他の選択肢が利用可能になる。
* これらの両方を設定すると、正しいパスワードが設定された場合しか開くことができ
  ず、かつ、その権限は制限される。

.. note::

   権限設定は使用者の |PDF| 閲覧ソフトがその設定を慮る場合に限り有効だ。

Digital Signatures tab of PDF Options dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Digital Signatures` 名タブには電子署名付き |PDF| を書き出すための選択
肢がある。

電子署名は次のことを確保するのに用いられる：

* |PDF| が本当に元の作成者によって作成された
* 文書が署名後に変更されていない

署名付き |PDF| エクスポートでは既定の keystore の場所または IC カードに保存され
ている鍵と X.509 証明書が使用される。使用する keystore は証明書の保存と取得に
Windows の既定の場所を使用する。

IC カードを使用する場合、keystore で使用できるように設定されている必要がある。こ
れは通常、IC カードソフトウェアのインストール時に行われる。

* :guilabel:`&Use this certificate to digitally sign PDF documents`:
  :guilabel:`&Select...` ボタンを押すと :guilabel:`Select Certificate` ダイアロ
  グボックスが開き、選択した keystore で見つかったすべての証明書が表示され
  る。Keystore がパスワードで保護されている場合はその入力を求められる。|PIN| で
  保護されている IC カードを使用する場合も |PIN| の入力を求められる。
* 書き出した |PDF| の電子署名に使用する証明書を選択し、:guilabel:`Sign` を押す。

:guilabel:`Digital Signature` タブの他のフィールドすべては証明書が選択された後に
限りアクセス可能だ。

* :guilabel:`Certificate &password`: 選択した証明書に関連する秘密鍵を保護するた
  めに使用するパスワードを入力する。通常、これは keystore パスワードだ。
  Keystore のパスワードが :guilabel:`Select Certificate` ダイアログボックスで既
  に入力されている場合、keystore は既にロック解除されている可能性があり、再度パ
  スワードを入力する必要はない。
* IC カードを使用する場合はここに |PIN| を入力する。一部の IC カードソフトウェア
  では、署名の前に |PIN| の入力を再度求められる。
* :guilabel:`&Location`, :guilabel:`Contact &information`, :guilabel:`&Reason`: オ
  プションで、|PDF| に適用される電子署名に関する追加情報を入力する。この情報は
  |PDF| 内の適切なフィールドに埋め込まれ、閲覧者に表示される。三つのフィールドの
  いずれか、またはすべてを空白のままにすることができる。
* :guilabel:`&Time Stamp Authority`: オプションでタイムスタンプ機関の URL
  を選択する。|PDF| 署名プロセス中、TSA は電子署名されたタイムスタンプを取得し、
  それを署名に埋め込む。閲覧者はこのタイムスタンプを使用して、文書がいつ署名され
  たかを確認できる。
* 選択できる TSA URL の一覧は :guilabel:`Options` ダイアログボックスの
  :menuselection:`LibreOffice --> Security` ページ` :guilabel:`TSAs` で管理され
  る。TSA URL が選択されていない場合（これが既定）、署名にはタイムスタンプが付与
  されず、ローカルコンピューターの現在時刻が使用される。

Exporting to EPUB format
======================================================================

|EPUB| 形式はスマートフォン、タブレット、電子書籍リーダーなどの携帯端末が市場に
登場してから普及した。中身を含む :abbr:`HTML (HyperText Markup Language)` ファイ
ルと、画像やその他の支援ファイルから構成される書庫ファイルとして実装されている。

Writer はファイルを |EPUB| にエクスポートすることが可能だ。テキストしかない文書
は通常うまく書き出されるが、一部の中身（イラスト、図表、相互参照など）は正しく書
き出されないことがある。

Quick export to EPUB
----------------------------------------------------------------------

:menuselection:`&File --> &Export As --> Export Directly &as EPUB` を選択すると、
:guilabel:`EPUB Export` ダイアログボックスで最近選択した |EPUB| 設定を使用
して文書全体が書き出される。|EPUB| ファイルのファイル名と場所を入力しろ。

.. admonition:: 読者ノート

   Export Directly コマンドはいきなり保存ダイアログボックスが出る。オプション指
   定は省略すると覚えておく。

Controlling export to EPUB
----------------------------------------------------------------------

作成される |EPUB| ファイルの内容や品質をより詳細に制御するには
:menuselection:`&File --> &Export As --> Export E&PUB...` を使用する。
:guilabel:`EPUB Export` ダイアログボックスが開く。

:guilabel:`&Version`
   エクスポートする |EPUB| バージョンを選択する。選択肢は次の二つ：

   * :guilabel:`EPUB 2.0`
   * :guilabel:`EPUB 3.0`
:guilabel:`&Split method`
   新しい節を開始する方法を選択する。

   * :guilabel:`Heading`: 文書の見出し番号（アウトラインレベル）に従って見出しか
     ら節を開始する。
   * :guilabel:`Page break`: 改頁で節を開始する。
:guilabel:`Layout method`
   画面の大きさや使用者の好みに合わせて電子書籍の表示を変更するには
   :guilabel:`Reflowable` を選択する（ページサイズやヘッダー、フッターの中身はエ
   クスポートされない）。どのような状況でも電子書籍のレイアウトが変わらないよう
   にするには :guilabel:`Fixed` を選択する。
:guilabel:`Cover &image`
   表紙ページの画像ファイルパス。画像が指定されていない場合、自動的に
   :file:`cover.gif`, :file:`cover.jpg`, :file:`cover.png`, :file:`cover.svg` の
   ような名前の画像を使用する。カスタム表紙画像は |EPUB| ファイルに埋め込まれる。
:guilabel:`&Media directory`
   表紙画像、メタデータ、マルチメディアファイルに対するオプションディレクトリー
   パス。ディレクトリーを指定しない場合、文書ファイル名と同じ名前のディレクト
   リー内の現在の文書ディレクトリーからカスタムメディアとメタデータを探す。
:guilabel:`&Metadata` 区画
   検索に役立つタグを用意しておくファイルの基本情報。これらのフィールドは Writer
   の :menuselection:`&File --> Prpert&ies...` から既定で取得されるメタデータを
   編集するもう一つの機会を与える。

Exporting to other formats
======================================================================

LibreOffice では、ファイル形式の変更を伴うファイル操作の一部に export という術語
を使用している。:menuselection:`&File --> Save As...` で必要なものが見つからない
場合は :menuselection:`&File --> Expor&t...` も参照しろ。Writer はファイルを
:abbr:`XHTML (eXtensible HyperText Markup Language)`, |EPUB|, およびその他の形式
にエクスポートできる。

:menuselection:`&File --> Expor&t...` を選択する。:guilabel:`Export` ダイアログ
ボックスで :guilabel:`ファイル名 (&N)` と :guilabel:`ファイルの種類 (&T)` を選択
して :guilabel:`Export` を押す。

Emailing Writer documents
======================================================================

LibreOffice には Writer 文書をメールの添付ファイルとしてすばやく簡単に送信する方
法がいくつか用意されている。対応ファイル形式は次の三つ：

* .odt: OpenDocumentText; Writer の既定形式
* .docx: Microsoft Word 形式
* .pdf

現在の文書を .odt 形式で送信する手順：

#. :menuselection:`&File --> Sen&d --> &Email Document...` または
   :menuselection:`&File --> Sen&d --> Email as &OpenDocument Text...` を選択。
   インストールされていれば、既定のメールプログラムが開く。文書が新しいメールに
   添付される。
#. メールソフトで受信者、件名、追加したいテキストを入力し、メールを送信する。

:menuselection:`Email as &Microsoft Word...` を選択した場合、Writer はまず Word
形式のファイルを作成し、新しいメールに Word ファイルが添付された状態でメールプロ
グラムを開く。同様に、:menuselection:`Email as P&DF...` を選択した場合、
:guilabel:`PDF Options` ダイアログボックスを開き、必要な設定を選択することができ
る。

Emailing a document to several recipients
----------------------------------------------------------------------

複数の受信者に文書をメールで送信するには、メールプログラムの機能を使用するか、
Writer のメールマージ機能を使ってアドレス帳からメールアドレスを抽出する。

Writer のメールマージを使ってメールを送信するには二つの方法がある：

* :guilabel:`Mail Merge` ウィザードを使用して文書を作成し、送信する。
* ウィザードを使用せずに Writer で文書を作成し、それからウィザードを使用して文書
  を送信する。

:doc:`Chapter 14 <writer14>` で詳しく見ていく。

Digital signing of documents
======================================================================

文書に電子署名するには、証明書としても知られる個人鍵が必要だ。個人鍵は、

* 秘密にしておかなければならない秘密鍵と、
* 文書に署名する際に追加する公開鍵

の組み合わせとして計算機に保存される。証明書は認証局（民間企業または政府機関）か
ら取得できる。

文書に電子署名を適用すると、文書の内容と著者の個人鍵から checksum が計算され、そ
の値と公開鍵が文書と一緒に保存される。

後で誰かが LibreOffice の最新版が入っている計算機で文書を開くと、プログラムは
checksum を再度計算し、保存されている値と比較する。両方が同じであれば、プログラ
変更されていない元の文書が表示されていることをプログラムが告げる。

証明書の公開鍵情報を表示することもできる。その公開鍵を認証局の Web サイトで公開
されている公開鍵と比較することができる。誰かが文書のどこかを変更すると、その変更
によって電子署名が破られる。

証明書の取得方法、管理方法、および署名の検証方法の詳細については、LibreOffice
Help を参照しろ。

.. admonition:: 読者ノート

   どこに？

署名された文書には Status バーに図像が表示される。図像をダブルクリックすると、証
明書を表示できる。文書には署名を複数追加できる。

既存の記述を変更するとその署名は無効になる。ただし、同じ作成者による複数の署名は
許可されている。

Applying a digital signature
----------------------------------------------------------------------

以下の手順は、文書に電子署名をする方法の一例だ。実際の手順は計算機の構成方法やOS
によって異なる。

#. :menuselection:`&File --> Di&gital Signatures --> Digital Signatu&res...` を
   選択する。

   * 文書にコメントや記録された変更が含まれる場合に警告を表示するように
     LibreOffice を設定している場合、文書への署名を続行するかどうかを尋ねるメッ
     セージボックス欄が表示されることがある。
   * 最後の変更以降、文書を保存していない場合は、メッセージボックスが表示され
     る。:guilabel:`&Yes` を都合二度押す。
#. :guilabel:`Digital Signatures` ダイアログボックスが開く。既存の署名がその説明
   とともに一覧表示される。文書に新しい署名を追加するには :guilabel:`&Sign
   Document...` ボタンをクリックする。
#. :guilabel:`Select Certificate` ダイアログボックスで証明書を選択し、オプション
   の説明を追加し、:guilabel:`Sign` を押して戻る。使用された証明書は、その名前の
   横に図像が付いた状態でダイアログボックスに表示される。この図像は、電子署名の
   状態を示す。
#. :guilabel:`Digital Signatures` ダイアログボックスで :guilabel:`&Close` を押し
   て電子署名を適用する。

Including a signature line
----------------------------------------------------------------------

:guilabel:`&Insert --> Signatu&re Line...` を選択して署名行を表す画像欄を生成で
きる。電子証明書を使用して署名行に署名することもできる。

Removing personal data
======================================================================

個人データ、版、コメント、秘密情報、記録変更が、他の人に送信したり、ファイルから
|PDF| を作成する前に、ファイルから削除されていることを保証したい場合がある。

:guilabel:`Options` ダイアログボックスの :menuselection:`LibreOffice -->
Security` ページで :guilabel:`O&ptions...` ボタンを押すと :guilabel:`Security
Options and Warnings` ダイアログボックスが表示され、ファイルに特定の情報が含まれ
ている場合に警告を表示したり、保存時に個人情報を自動的に削除したりするように
LibreOffice を設定することが可能だ。

ファイルから個人データなどを削除するには、

#. :menuselection:`&File --> Propert&ies...`
#. :guilabel:`General` タブで :guilabel:`&Apply user data` をオフ
#. :guilabel:`&Reset Properties` を押す

これにより、作成および変更フィールドの名前が削除され、変更日と印刷日が削除され、
編集時間がゼロに、作成日が現在の日時に、バージョン番号がリセットされる。

バージョン情報を削除するには、

* :menuselection:`&File --> Versions...` を選択。:guilabel:`Existing Versions`
  一覧からバージョンを選択して :guilabel:`&Delete` を押すか、
* ファイルを別の名前で保存する。

Redaction
======================================================================

文書の機密情報を削除したり隠蔽したりするために文書を冗長化し、文書の他の部分を秘
密にしたまま、文書内の情報を選択的に開示できるようにすることができる。例えば、裁
判で文書が召喚された場合、その訴訟に特に関係のない情報は冗長化されることがよくあ
る。

黒塗り手順：

#. 文書を開く
#. メニューから :menuselection:`&Tools --> Re&dact` を選択
#. 文書が再編集用に準備されて Draw に転送されるのを待つ

   ここから Draw での作業になる。:guilabel:`Redaction` ツールバーが開く。
#. ツールバーの :guilabel:`Rectangle Redaction` と :guilabel:`Freeform
   Redaction` ツールを使用して黒塗りする。図形は透明で灰色になるので、何を黒塗り
   しているかがわかる。
#. オプションで :guilabel:`Export Directly as PDF` ツールを使用すると、黒塗りコ
   ピーを |PDF| で作成し、査読用の逐語的な写しとして使用できる。黒塗り項目は透明
   な灰色で表示される。
#. 黒塗りを確定するには :guilabel:`Redacted Export` ツールで希望のオプション（黒
   または白）を選択する。透明な灰色の図形が不透明な黒または白の図形に変換され、
   文書がピクセル化された |PDF| としてエクスポートされる。その中に選択可能テキス
   トはなく、黒塗りした箇所の中身は存在しない。

Auto-redaction
----------------------------------------------------------------------

黒塗りプロセスを部分的に自動化するには、特定の単語（名前など）が文書内のどこに
あっても黒塗りするように定義する。これを行うには、メニューで
:menuselection:`&Tools --> Auto-Redact` を選択し、:guilabel:`Automatic
Redaction` ダイアログボックスを開く。ここでは、用語（対象）の一覧の読み込み、対
象の追加、対象の削除、対象の編集、対象の一覧の保存ができる。

Accessibility checking
======================================================================

LibreOffice には画面読み上げを含む外部機器やアプリケーションの支援を含む、いくつ
かの accessibility 機能が含まれている。

文書を公開する前に、Writerの :guilabel:`&Accessibility Tool` を使用して、一般的
な問題を確認できる。手動で検査を実行するには、メニューの :menuselection:`&Tools
--> &Accessibility Check...` を選択する。|PDF| にエクスポートする場
合、:guilabel:`PDF Export` ダイアログボックスの :guilabel:`General` タブで
:guilabel:`Universal Accessibilit&y (PDF/UA)` をオンにし、:guilabel:`E&xport` を
押すと、警告ダイアログボックスがポップアップ表示される。

:guilabel:`Accessibility Check` ダイアログボックスは既定で Sidebar に表示される。
文書で見つかった問題の一覧が表示される。検査項目には以下が含まれる：

* 文書の表題が設定されていること
* 文書の言語が設定されていること、または使用中のすべてのスタイルに言語が設定され
  ていること
* すべての画像、画像、:abbr:`OLE (Object Linking and Embedding)` オブジェクトに
  代替テキスト（場合によっては表題）が設定されていること
* 表に分割または結合されたセルが含まれていないこと
* 手動の番号付け（統合番号付けを使用していないこと）
* テキストと背景のコントラスト
* 脚注や注は避ける
* 見出しはレベルを飛ばしてはならない

:guilabel:`Fix` ボタンをクリックしてページに飛び、accessibility のために注意が必
要な物または問題を選択する。

.. admonition:: 読者ノート

   Accessibility Check が全然働かない。ボタンはどこにある？

----

.. rubric:: 章末注

.. [#ctl] :guilabel:`Options` ダイアログボックス :menuselection:`Language
    Settings --> Languages` ページ内 :guilabel:`Complex &text layout`
