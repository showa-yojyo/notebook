======================================================================
Writer Guide Chapter 14, Mail Merge ノート
======================================================================

.. include:: ./writer-inc.txt
.. |MailMergeDlg| replace:: :guilabel:`Mail Merge` ダイアログボックス

.. contents:: 章見出し
   :depth: 3
   :local:

What is mail merge?
======================================================================

mail merge
   (computing) A software product that uses a file (or database) of names and
   addresses, together with a template document, to produce multiple copies of a
   letter, each personally addressed to a different recipient. -- Wiktionary_

.. admonition:: 読者ノート

   「差し込み印刷」を mail merge に対する訳語として当てるのが一般的であるよう
   だ。

* 定型書簡（受信者一覧に送る文書）
* 宛名札、物理的ファイル・フォルダーの荷札、および同様の目的
* 封筒

可変データは通常、後述するようにデータ給源から入手する。出力がすべて同じである場
合（例えば返信用住所札）、差し込みは手動で入力されたテキストまたは画像を使用でき
る。

この章では差し込み印刷工程について説明する。手順は次のとおり：

#. データ給源の作成と登録
#. 定型書簡、宛名札、封筒の作成と印刷
#. オプションとして、出力結果を直接印刷する代わりに編集可能なファイルに保存する

Creating and registering an address data source
======================================================================

宛名データ給源は宛名札や封筒を作成するための名前と住所の目録を含むデータベース
だ。LibreOffice では、スプレッドシート、Writer 文書を含むテキストファイル、MySQL
などのデータベースからデータベースを作成できる。差し込み印刷で使用する情報が
LibreOffice が直接アクセスできない形式になっている場合は |CSV| ファイルなどにエ
クスポート変換する必要がある。

Writer 文書内からデータ給源に直接アクセスするには、そのデータ給源を登録する必要
がある。これを行う必要は一度しかない：

#. Writer 文書内または LibreOffice Start Center から
   :menuselection:`&File-->&Wizards-->Address &Data Source...` を選択する。
#. |MMWizard| の最初のページの選択肢は OS によって異なる。適切な外部住所帳の種類
   を選択する。

   * スプレッドシートの場合は :guilabel:`&Other external data source` だ。
   * 選択項目によって左柱の :guilabel:`Steps` が変わる場合がある。

   |Next| を押す。
#. |MMWizard| の次のページで :guilabel:`&Settings` ボタンを押す。
#. :guilabel:`Create Address Data Source` ダイアログボックスで
   :guilabel:`Database &type` を選択する。この例では :guilabel:`Spreadsheet` だ。
   |Next| を押す。
#. 次のページで |Browse| を押し、住所情報を含むスプレッドシートに移動する。スプ
   レッドシートを選択し、|Open| を押してダイアログボックスに戻る。
#. 接続が正しく確立されたことをテストするには、ダイアログボックスの右下にある
   :guilabel:`Test Connect&ion` ボタンをクリック押す。接続は正常に確立された旨が
   表示されるはずだが、そうでない場合はエラーメッセージが表示される。
#. |Finish| を押す。
#. 次のページで |Next| を押す。:guilabel:`Field &Assignment` ボタンを押す必要は
   ない。
#. :guilabel:`Data Source Title` ページでは新しいデータベースのファイル名と場所
   が :guilabel:`&Location` 欄に表示される。この名前を変更したり、データベース
   ファイルを別の場所に保存したりすることができる。

   #. :guilabel:`&Embed this address book definition into the current document`
      をオフにする。
   #. |Browse| を押してファイルパスを指定する。

   :guilabel:`Address book name` 欄の名前も変更できる。これは、LibreOffice が
   データ給源一覧に表示する登録名だ。この例では `Addresses` という名前が両方に使
   用されている。
#. |Finish| を押す。

これでデータ給源が登録された。

.. admonition:: 読者ノート

   本書の図版を参考にして :file:`addresses.ods` を自作して上記の手順を再現しろ。
   印刷プレビューまで確認できれば十分だ。

.. _writer14-anchor-form:

Creating a form letter
======================================================================

定型書簡を手動で作成することもできる。これは最も簡単かつ包括的な方法で、ここで説
明されている。あるいは :ref:`Mail Merge Wizard<writer14-anchor-wizard>` を使う。

#. Writer 文書を新規作成するか、既存の定型書簡を開く。
#. 登録されているデータ給源を表示する

   * |MenuBar| :menuselection:`&View-->Data Sources`
   * キーバインド |Ctrl+Shift| + |F4|
#. 定型書簡に使用するデータ給源、この場合は `Addresses` を見つける。このノードと
   `Tables` ノードを展開し、`Sheet1` を選択する。住所データファイルが表示され
   る。
#. 定型書簡すべてに含まれるテキスト、句読点、改行などを入力して、定型書簡を作成
   または修正する。

   差し込み印刷フィールドを必要な箇所（名前や住所など）に追加するには、フィール
   ドの見出しをクリックし、書簡内の適切な箇所にドラッグする。必要に応じて、空白
   やその他の句読点を追加しろ。宛先ブロックの各行の末尾で |Enter| を押す。
#. この例のデータベースには、二番目の住所行 AD2 のフィールドがあり、一部の住所で
   空白になっている。書簡が印刷されるときに住所ブロックに表示される可能性のある
   空白行を削除したい場合は次節で説明する手順を使用できる。そうでない場合は、次
   の手順へ進め。
#. これで文書は印刷準備ができた。

   * |PrintM| を選択し、メッセージボックスで |Yes| を押す。
   * |MailMergeDlg| :guilabel:`Records` 区画で、すべての記録行を印刷するか、選択
     した記録行を印刷するかを選択できる。

     * 印刷する個々の記録行を選択するには |Ctrl| を押しながらクリック。
     * 記録行のブロックを選択するには、ブロック内の最初の記録行を選択し、ブロッ
       ク内の最後の記録行までスクロールして、最後の記録行を |Shift| を押しながら
       クリック。
     * 印刷する記録行番号の範囲を指定することもできる。
   * 手紙を直接印刷機に送信するには、:guilabel:`Output` 区画で
     :guilabel:`&Printer` を選択し、|OK| を押す。または、手紙をファイルに保存し
     て、さらに編集や書式設定を行うこともできる。:ref:`writer14-anchor-save` を
     見ろ。
   * 定型書簡の原型となる文書（雛形）を保存していない場合はただちに保存しろ。定
     型書簡の雛形があれば、他の定型書簡の作成が大幅に簡素化される。

Suppressing blank lines (optional)
----------------------------------------------------------------------

空行を抑制したい場合は次の手順をたどれ：

#. 段落の末尾をクリックし、:menuselection:`&Insert-->Fiel&d-->&More Fields...`
   を選択して |FieldsDlg| を開く。
#. :guilabel:`Functions` タブをクリックし、:guilabel:`&Type` で
   :guilabel:`Hidden Paragraph` を選択する。

   .. note::

      :ref:`Mail Merge Wizard<writer14-anchor-wizard>` を使用する場合、空白行の
      自動抑制を選択して、この段階で説明する作業を避けることができる。

#. 次に :guilabel:`&Condition` 欄をクリックし、空白の住所フィールドを定義する条
   件の詳細を入力する。一般的な形式は

   .. code:: text

      ![Database.Table.Database field]

   例えば、AD2 フィールドが空かどうかをテストする条件は次のようになる：

   .. code:: text

      ![Addresses.Sheet1.AD2]

   この条件を表す別の方法には、

   * ``NOT Addresses.Sheet1.AD2`` や
   * ``Addresses.Sheet1.AD2 EQ ""``

   がある。

#. |Insert| を押す。

.. _writer14-anchor-save:

Saving merged documents
----------------------------------------------------------------------

校正や書式整形のために手紙をファイルに保存することもできる。そのためには

#. |MailMergeDlg| で含める記録行を選択し、:guilabel:`Output` 区画で
   :guilabel:`File` を選択して、ページ上の他の選択肢を活動開始する。
#. 出力を一つの文書（すべての手紙を含む）として保存するか、手紙を個々の文書とし
   て保存するかを選択でき、ファイルの名前、場所、形式を指定できる。
#. |OK| を押す。|SaveAsDlg| で保存した手紙のファイル名を入力し、保存するフォル
   ダーを選択する。手紙は一つの文書に別々のページとして連続して保存されるか、
   個々のファイルに連続した番号が付けられる。

他の文書を編集するのと同じように、手紙を開いて個別に編集することができる。

.. _writer14-anchor-print:

Printing mailing labels
======================================================================

紙札は一般的に住所録（各紙札が異なる住所を示す）を印刷するために使用されるが、返
送先住所シールや CD/DVD などの紙札など、一つの紙札のみを複数部作成するためにも使
用できる。

作業を始める前に使用する紙札の銘柄と型を確認しろ。また、独自の紙札判型を定義する
こともできる。

.. |LabelsDlg| replace:: :guilabel:`Labels` ダイアログボックス

.. tip::

   各紙札に同じ情報を印刷する場合は :guilabel:`Business Cards` ダイアログボック
   スが便利だ。:menuselection:`&File-->&New-->B&usiness Cards` からアクセスでき
   る。|LabelsDlg| と :guilabel:`Business Cards` ダイアログボックスはよく似てい
   る。

Preparing for printing
----------------------------------------------------------------------

印刷用の宛名札を準備する：

.. |LabelTextArea| replace:: :guilabel:`&Label text` 領域
.. |LabelsTab| replace:: :guilabel:`Labels` タブ
.. |NewDocButton| replace:: :guilabel:`&New Document` ボタン
.. |SyncLabelButton| replace:: :guilabel:`Synchronize Labels` ボタン

#. :menuselection:`&File-->&New-->&Labels...` を選択。|LabelsDlg| が開く。
#. |LabelsTab| で :guilabel:`&Database` と :guilabel:`Ta&ble` を選択。
#. :guilabel:`&Database` ドロップダウンリストから紙札で使用する最初のフィールド
   を選択し、左矢印ボタンをクリックして |LabelTextArea| に移動する。
#. 紙札が構成されるまでフィールドを追加し、必要な句読点、空白、行末（段落）を挿
   入し続ける。

   ある OS では、|LabelTextArea| の下にスクロールバーが表示され、段落の末尾がど
   こにあるか見ることができる。他のシステムでは、フィールドが一覧に表示され、段
   落の終端がどこにあるかわからないかもしれない。後で手順 8 で確認できる。
#. :guilabel:`Bra&nd` ドロップダウンリストで紙札巻を選択する。その後、その銘柄型
   が :guilabel:`&Type` ドロップダウンリストに表示される。必要な紙札の判型を選択
   し、手順 7 に進め。紙札シートが一覧にない場合は次の手順に進め。
#. 一覧にない紙札を定義するには：

   #. |LabelsTab| の :guilabel:`&Type` で :guilabel:`[User]` を選択する。次に、
      |LabelsDlg| の |FormatTab| をクリックする。紙札の寸法を測り、左側の入力欄
      それぞれに入力する。

      * :guilabel:`&Horizontal pitch` は隣接する紙札の左端間の距離だ。
      * :guilabel:`&Vertical pitch` はある紙札の上辺とその直下の紙札の上辺との距
        離だ。
   #. 紙札雛形を再度使用する場合は保存することができる。:guilabel:`&Save...` を
      押す。
   #. ポップアップ表示される :guilabel:`Save Label Format` ダイアログボックス
      で、紙札の :guilabel:`&Brand` と :guilabel:`&Type` の名前を入力する。
   #. |OK| を押す。
#. |LabelsDlg| |OptionsTab| で :guilabel:`Synchroni&ze contents` をオンにする。
#. |NewDocButton| を押す。これで、選択した型の紙札ごとに一つずつ、選択した原デー
   タの住所フィールドで埋められた一連の枠を含む一ページの文書が得られた。この文
   書には紙札が一ページしかないように見えるが、印刷または保存された出力は、原
   データから選択されたすべての記録行に十分なページを含むように拡張される。
#. この文書では、次を使用すると段落末尾が表示される：

   * ツールバー :guilabel:`Toggle Formatting Marks` ボタン
   * |MenuBar| :menuselection:`&View-->For&matting Marks`
   * キーバインド |Ctrl| + |F10|
#. 通常は画面の左上隅に |SyncLabelButton| を含む小さなウィンドウが表示されるはず
   だ。
#. 段落末尾やその他の句読点が欠けている場合、またはすべての紙札の一つまたは複数
   のフィールドや行（段落）のフォントやその他の特徴を変更したい場合は、すぐに変
   更できる。左上の紙札で、変更したいフィールドを選択し、手動で変更するか、段落
   スタイルまたは文字スタイルを選択する。不足している句読点を追加する。次に、
   |SyncLabelButton| を押して、これらの変更をすべての紙札に自動的に追加する。

Printing
----------------------------------------------------------------------

#. |PrintM| を選択する。メッセージが表示される。|Yes| を押して印刷する。
#. |MailMergeDlg| ではすべての記録行を印刷するか、選択した記録行を印刷するか
   を選択できる。

   * 印刷する個々の記録行を選択するには |Ctrl| を押しながらクリック。
   * 記録行ブロックを選択するには、ブロック内の最初の記録行を選択し、ブロック内
     の最後の記録行までスクロールして、最後の記録行を |Shift| を押しながら
     クリック。
#. |OK| を押すと紙札が直接印刷機に送信される。紙札をファイルに保存したい場合は
   :guilabel:`Output` 区画 :guilabel:`&File` を選択する。この場合、|OK| を押すと
   |SaveAsDlg| が開き、先述のように、ファイル名と保存場所を入力できる。

.. note::

   紙札の宛名の空白行は、:ref:`Mail Merge Wizard<writer14-anchor-wizard>` を使用
   する場合と同様に自動的に抑制される。

Editing a saved file of mailing labels
----------------------------------------------------------------------

保存した宛名札のファイルを編集するには、他の Writer 文書と同じようにファイルを開
く。

個々の記録行を手作業で編集することはできるが（たとえば、ソーススプレッドシートを
変更して紙札を再生成する必要なくても、誤綴字を正す）、手作業ですべての紙札を一度
に編集することはできない（たとえば、使用するフォントを変更する）。ただし、紙札記
録行に関連付けられた段落スタイルや文字スタイルを編集することはできる：

#. 紙札記録行を右クリックする。コンテキストメニューの
   :menuselection:`P&aragraph-->&Edit Style...` を選択する。
#. |ParagraphStyleDlg| で、フォント名、フォントサイズ、字下げ、その他の属性を変
   更できる。

Printing envelopes
======================================================================

宛名札を印刷する代わりに、封筒に直接印刷することもある。

封筒の作成には構成と印刷という二つの段階がある。|EnvelopeDlg| の |FormatTab| と
|PrinterTab| を使って封筒を印刷するための一般的な設定方法については |Writer07|
を見ろ。

封筒を一通作成するには、宛先欄に名前と住所を入力または貼り付けるか、この節で説明
するように住所データ給源から情報を取得する。

Setting up envelopes for printing
----------------------------------------------------------------------

#. |MenuBar| の :menuselection:`&Insert-->En&velope...` を選択する。
#. |EnvelopeDlg| |EnvelopeTab| で封筒に差出人情報を追加するかどうかを選択する。
   追加する場合は、差出人欄に情報を入力する。あらかじめ差出人情報が印刷された封
   筒を使用する場合は、この記入欄を空にするか、:guilabel:`&Sender` チェックボッ
   クスをオフにする。
#. :ref:`writer14-anchor-print` で説明したように、データ給源の見出しからドラッグ
   ＆ドロップして :guilabel:`Addressee` フィールドを作成し、|NewDocButton| をク
   リックして封筒雛形を作成する。

   または、|NewDocButton| を押し、封筒雛形の上にある Data Source ウィンドウを開
   き、データ給源の見出しを封筒の :guilabel:`Addressee` フィールドにドラッグす
   る。
#. この時点でこの文書を雛形として保存することもできる。

Merging and printing the envelopes
----------------------------------------------------------------------

宛名を統合して封筒を印刷する手順：

#. |PrintM| を選ぶ。メッセージが表示される。|Yes| を押して印刷する。
#. |MailMergeDlg| が開く。定型書簡や宛名札と同様に、データベース内の一つ、複数、
   またはすべての住所録の封筒を印刷するように選択できる。
#. 選択し、|OK| を押すと印刷機に直接印刷される。印刷前に封筒を確認するには
   :ref:`writer14-anchor-save` を見ろ。空白行は自動的に抑制される。

.. _writer14-anchor-wizard:

Using the Mail Merge Wizard to create a form letter
======================================================================

定型書簡を手動で作成する方法については :ref:`writer14-anchor-form` で説明してい
る。|MMWizard| を使用する場合は、その技法はこの節で述べられる。

:menuselection:`&File-->&New-->&Text Document` で新規文書を開き、
:menuselection:`&Tools-->Mail Merge Wi&zard...` を選択する。

Step 1: Select starting document
----------------------------------------------------------------------

|MMWizard| では、開始文書に選択肢がある：

* 現在の文書を使用
* 新規文書を作成
* 既存文書から開始
* 雛形から開始
* 最近保存した文書から開始

この例では新規テキスト文書を開く。

:guilabel:`Use the current &document` を選択し、|Next| を押す。

現在の文書に登録済みデータ給源が関連付けられていない場合は、警告メッセージが表示
される。

#. :guilabel:`Exchange Databases...` ボタンを押して :guilabel:`Exchange
   Databases` ダイアログボックスを開く。
#. :guilabel:`&Available Database` から必要なデータベースを選択する。
#. 必要に応じて |Browse| を押してファイルダイアログボックスを開き、登録する必要
   があるデータベースを見つける。
#. :guilabel:`De&fine` ボタンを押してダイアログボックスを閉じ、選択したデータ
   ベースを文書に関連付ける。

Step 2: Select document type
----------------------------------------------------------------------

|MMWizard| は手紙やメールを作成することができる。この例では、手紙を作成する。
:guilabel:`&Letter` を選択し |Next| を押す。

Step 3: Insert address block
----------------------------------------------------------------------

この段階では三つのことを行う：

#. ウィザードに使用するデータ給源を指定する。データ給源は既存のファイルでなけれ
   ばならない。
#. 文書で使用する住所ブロックを選択する。どのフィールドが表示されるか（例えば、
   国を含めるかどうか）と、それらがどのように見えるかを選択することを意味する。
#. フィールドがすべて正しく一致していることを確認しろ。これは重要だ。例えば、英
   国英語版のウィザードには <Surname> というフィールドがある。スプレッドシートに
   "Last Name" という列がある場合、ウィザードに <Surname> と "Last Name" が等価
   であることを伝える必要がある。これについては :ref:`writer14-anchor-matching`
   で説明している。

Selecting the data source (address list)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. :guilabel:`Select Different A&ddress List...` ボタンの下にある
   :guilabel:`Current address list` が使用したい住所一覧でない場合は、このボタン
   をクリックして :guilabel:`Select Address List` ダイアログボックスを開き、原
   データを選択する。

   まだ住所一覧を作成していない場合は :guilabel:`&Create...` を押せ。この手順で
   は新しい住所録一覧を含む |CSV| ファイルを作成できる。LibreOffice に登録されて
   いないが使用したい住所録がある場合は、:guilabel:`&Add...` を押し、そのファイ
   ルが保存されている場所からファイルを選択する。

   これらの場合それぞれで、新しいデータ給源ファイル (.odb) が作成され、登録され
   る。
#. 住所一覧を選択し、|OK| を押して :guilabel:`Insert Address Block` ダイアロ
   グボックスに戻る。この例では `Addresses` を住所帳として使用する。ウィザー
   ドは特定の記録行を除外することもできる。:guilabel:`&Filter...` を押して選
   べ。

Selecting and optionally editing the address block
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. |SelectAddressBlockDlg| replace:: :guilabel:`Select Address Block` ダイアログボックス
.. |EditAddressBlockDlg| replace:: :guilabel:`Edit Address Block` ダイアログボックス

#. 第二区画では、手紙に表示する宛名ブロックを選択し、その体裁を定義し、その中に
   含まれるフィールドを選択する。主要ページには二つの選択肢がある。

   :guilabel:`&More...` を押すと |SelectAddressBlockDlg| が開き、選択肢が増え
   る。
#. |SelectAddressBlockDlg| には元の二つのブロックに加え、住所ブロックの書式に関
   するその他の選択肢が表示される。また、:guilabel:`Address Block Settins` 区画
   で、オプションで <Country> を入れたり外したりすることもできる。用意されている
   形式は比較的一般的なものだが、好みに合わない場合は、希望に最も近い住所ブロッ
   クを選択して :guilabel:`&Edit...` を押すと |EditAddressBlockDlg| が開く。
#. |EditAddressBlockDlg| では矢印ボタンを使って住所要素を加除できる。要素を移動
   するには右に移すボタンを使う。
#. |OK| を押して |EditAddressBlockDlg| を閉じる。
#. |SelectAddressBlockDlg| で |OK| を押して変更を保存。

.. _writer14-anchor-matching:

Matching the fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

最後に、<Surname> や "Last Name" のような項目が正しく一致するように、ウィザード
のフィールドとスプレッドシートのフィールドを一致させる。

#. ウィザードの第三区画を見ろ。一番下の箱は指定した住所ブロック形式を使用して、
   一度に一つの記録行を表示する。その住所ボックスの下にある右矢印ボタンと左矢
   印ボタンを使って、住所が正しく表示されることを確認しながら段階を踏め。一つか
   二つ表示されたからといって、すべての記録行が正しく表示されているとは思うな。
#. 住所が正しく表示されない場合は、:guilabel:`Match &Fields` を押す。
   :guilabel:`Match Fields` ダイアログボックスには三つの列がある：

   * :guilabel:`Address elements` 列はウィザードが各フィールドに使用する項で、
     <First Name> や <Last Name> のようなものだ。
   * :guilabel:`Matches to field` 列を用いて、各住所要素に対して、それに一致する
     データ給源のフィールドを選択する。
   * :guilabel:`Preview` 列には選択された住所ブロックからこのフィールドに対して
     表示される内容が表示される。一致が正しいかどうかを再確認することができる。
#. すべてのフィールドを一致させたら |OK| を押して |EditAddressBlockDlg| に戻る。
   これで、矢印ボタンを使ってすべての住所を見ると、すべて正しく見えるはずだ。そ
   うでない場合は、|Next| を押して次の段階に進む前に、戻って気に入らないところを
   変更しろ。

   選択した住所ブロックのフィールドすべてを正しく照合するまで次に進むことはでき
   ないので気をつけろ。フィールドの位置に ``<not yet matched>`` と表示されている
   場合は、問題のフィールドが正しく合致していないことを示している。

   .. admonition:: 読者ノート

      次に進むことができないとは、|MMWizard| の第四ページを開けないということだ。

#. 第二区画にある :guilabel:`&Suppress lines with just empty fields` に注目し
   ろ。ウィザードを使用すると、本章で前述した手動定型書簡方式を使用する場合のよ
   うに、独自の条件付き抑制フィールドを作成する必要はない。

Step 4: Create salutation
----------------------------------------------------------------------

この段階ではどんな敬称でも作ることができる。

:guilabel:`General salutation` を有効にするには、:guilabel:`This document should
contain a salutation` をオンにする。一覧には一般的なテキストがいくつか用意されて
いるが、独自のテキストを入力することもできる。:guilabel:`&Preview` に選択したテ
キストが表示される。

:guilabel:`&Insert personalized salutation` をオンにすると、敬称のさらなる構成が
可能になる。

例えば、相手が男性なのか女性なのかで敬称を使い分けることができる。そのためには、
Writer が相手を男性か女性かを知る方法を持たなければならない。スプレッドシートで
は Gender という列があるといい。:guilabel:`Address list field indicating a
female recipient` で、:guilabel:`Fiel&d name` と :guilabel:`Field &value` を
`Gender` と `F` にそれぞれ設定する。

スプレッドシートにそのような列がない場合、または敬称で性別を区別する必要がない場
合は、両者を空のままにして、カスタマイズした :guilabel:`&Male` 一覧ボックスの内
容をすべての受信者への敬称に使用できる。

一例を挙げよう：

#. :guilabel:`&Male` 一覧ボックスの横にある :guilabel:`N&ew...` ボタンを押す。
   :guilabel:`Custom Salutation (Make Recipients)` ダイアログボックスが開く。
#. :guilabel:`Salutation elements` 一覧で :guilabel:`Salutation` を選択し、右側
   の箱 1 にドラッグする。
#. :guilabel:`Customi&ze salutation` 欄で適切な敬称を選択するか、独自のテキスト
   を入力する。必要に応じて編集しろ。
#. :guilabel:`Salutation elements` 一覧から :guilabel:`First Name` を選択し、矢
   印ボタンまたはドラッグして箱 1 に移動する。敬称と名前の間に空白を追加する。
#. :guilabel:`Salutation elements` 一覧から :guilabel:`Last Name` を選択し、箱 1
   に移動する。右矢印ボタンを押して姓と名の間に空白を追加する。
#. 最後に、:guilabel:`Punctuation Mark` を横に移動し、:guilabel:`Customi&ze
   salutation` の選択肢からカンマを選択する。
#. :guilabel:`&Preview` に構成が表示される。
#. 最終的な編集を行う。|OK| を押す。

この方法では、Doctor (Dr) や Reverend (Rev) のような性別を問わない肩書きや、Ms
のような肩書きを使用したり、省略したりすることができる。

Step 5: Adjust layout
----------------------------------------------------------------------

第五段階では、ページ上の住所ブロックと敬称の位置を調整することができる。住所ブ
ロックはページのどこにでも配置できる。敬称は常に左側にあるが、ページの上下に移動
できる。ボタンを使用して要素を移動する。

これで手紙の内容を入力できる Writer 文書が整った。フィールドを差し込んで書簡を印
刷するには、|MenuBar| |PrintM| を選択する。定型書簡を印刷するかどうかを尋ねる
メッセージがポップアップ表示される。|Yes| を押す。

|MailMergeDlg| が開き、オプションで記録行を加除選択し、:guilabel:`Output` 区画
で手紙をすぐに印刷するか (:guilabel:`&Printer`)、後で編集または印刷するために保
存するか (:guilabel:`&File`) を選択する。

:guilabel:`&File` を選択した場合は、出力を単一の文書（すべての手紙を含む）として
保存するか、または個々の文書として保存するかを選択し、ファイルの名前、場所、およ
び形式を指定できる。|OK| を押して手紙を保存する。これで手紙を開き、他の文書と同
じように個別に編集することができる。

.. _Wiktionary: https://en.wiktionary.org/wiki/mail_merge
