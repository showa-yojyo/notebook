======================================================================
Writer Guide Chapter 20, Customizing Writer ノート
======================================================================

.. include:: ./writer-inc.txt
.. |MSWord| replace:: Microsoft Word

.. contents:: 章見出し
   :depth: 3
   :local:

Introduction
======================================================================

この章では |OptionsDlg| にある設定オプションのいくつかを簡単に見ていく。ここにな
いオプションが説明されているのは：

* |Help|
* |Guide|
* これまでの章

この章では、新しいメニューやツールバーの追加、イベントへのマクロの割り当てなど、
|MenuBar|、ツールバー、キーバインドの一般的なカスタマイズについても簡単に説明す
る。その他のカスタマイズは拡張によって行う。また、いくつかの実験的な機能を有効に
して使用することもできる。:ref:`writer20-anchor-themes` を見ろ。

.. tip::

   多くのオプションは上級者やプログラマー向けだ。そのオプションが何をするものな
   のか理解できない場合は、本書の説明で設定を変更することが推奨されていない限
   り、通常は既定設定のままにしておくのが最善だ。

.. note::

   |MenuBar| とツールバーのカスタマイズは雛形に保存することができる。これを行うに
   は、まずそれらを文書に保存し、|Writer10| にあるように、文書を雛形として保存
   する。複数のプロジェクトで作業する場合、こういうものが便利になる。

Choosing options for all of LibreOffice
======================================================================

このセクションでは、LibreOffice のすべてのプログラム (Writer, Calc, Impress,
Draw, Math, Base) に適用される設定のうち、Writer を使用する際に特に重要な設定に
ついて説明する。

|OptionsDlg| を開き、左側の LibreOffice ノードをクリックする。ページの一覧がド
ロップダウンする。一覧の項目を選択すると、ダイアログボックスの右側に該当するペー
ジが表示される。

.. tip::

   |OptionsDlg| のどのページにおいても下部にある |ResetButton| は、そのページの
   値をダイアログボックスを開いたときの値にリセットする。

米国英語以外のバージョンの LibreOffice を使用している場合、フィールドのラベルが
図と異なることがある。

.. admonition:: 読者ノート

   LibreOffice に限ったことではないが、ラベルが説明書と異なっているのはまずいの
   で、UI 言語を米国英語に固定しておくのが良い。設定方法は本章内で示される（は
   ず）。

User data
----------------------------------------------------------------------

Writer は |UserDataPage| に保存されている名前や頭文字を、文書の性質（著者や最終
編集者の情報）、コメントや変更の作成者の名前、メーリングリストの送信者アドレスな
ど、さまざまなことに使用できる。

フォームに入力するか、既存の情報を修正または削除しろ。使用者データを文書の性質の
一部にしたくない場合は、:guilabel:`&Use data for document properties` をオフにし
ろ。

.. tip::

   文書を保存時にキャレットがあったページで開くようにするには、このオプションを
   オンにし、各文書の |FilePropertiesM| と進み、|GeneralTab| で :guilabel:`Apply
   user data` をオンにする。これらの設定が両方とも選択されていない限り、文書は最
   初のページが開かれる。

   または、|LoadSaveGeneralPage| で :guilabel:`Load view position with the
   document even if it was saved by a different user` をオンにする。

:guilabel:`Cryptography` 区画では、OpenPGP 暗号化と電子署名に優先する公開鍵を設
定できる。これらの優先鍵は、文書に署名したり暗号化したりするときに、鍵選択ダイア
ログボックスであらかじめ選択される。|Writer07| を見ろ。

View options
----------------------------------------------------------------------

|LibreOfficeViewPage| のオプションは文書ウィンドウの表示や動作に影響する。好みに
合わせて設定しろ。詳細については |Help| または |Guide| を参照しろ。

Print options
----------------------------------------------------------------------

|LibreOfficePrintPage| では既定の印刷機と最も一般的な印刷方法に合わせて印刷オプ
ションを設定する。

ページの右側にある :guilabel:`Warnings` 区画では、文書で指定された用紙判型または
向きが、使用している印刷機で使用可能なそれと合致しない場合に警告を表示するかどう
かを指定できる。この警告をオンにしておくと、特に標準的な用紙判型が異なる他国の人
が作成した文書を扱う場合に便利だ。

.. tip::

   印刷物がページ上に正しく配置されていなかったり、上下左右が切れていたり、印刷
   機が印刷を拒否する場合、原因としてページ判型の不適合が考えられる。

Paths options
----------------------------------------------------------------------

|PathsPage| では、LibreOffice に関連する、または LibreOffice で使用するファイル
の場所を必要に応じて変更できる。

.. admonition:: 読者ノート

   項目名 (:guilabel:`Type`) を見ると :guilabel:`My Docments` だの
   :guilabel:`Templates` などがあり、パスには :file:`%USERPROFILE&\\Documents`
   や :file:`%APPDATA%\\LibreOffice\\4\\user\\templates` などが設定されている。

   LibreOffice 環境をバックアップする場合、これらのパス内容を保全する。

詳細については |Guide| を参照しろ。

Fonts options
----------------------------------------------------------------------

文書にシステム上にないフォントが含まれている場合、LibreOffice は見つからないフォ
ントを置換する。プログラムが選択するフォントとは異なるフォントを指定するには、
:menuselection:`LibreOffice-->Fonts` ページで代替フォントを指定する。

.. tip::

   `Libreration Fonts <https://github.com/liberationfonts/liberation-fonts>`__
   (Serif, Sans, Mono) は Times, Arial, Courier の代わりによく使われる。

.. note::

   ここでの選択は文書の既定フォントには影響しない。これを行うには
   :ref:`writer20-anchor-fonts` を参照しろ。基本フォント以外のフォントを変更する
   には Writer 文書の新しい既定雛形を作成する。

Security options
----------------------------------------------------------------------

|SecurityPage| では、文書の保存やマクロを含む文書を開く際の保障オプションを選択
できる。ここに記載されていないオプションについては |Help| または |Guide| を見ろ。

:guilabel:`Security Options and Warnings`
   変更を記録したり、複数のバージョンを保存したり、文書に隠し情報やメモを含めた
   りして、一部の受信者にその情報を見せたくない場合は、削除を促す警告を設定した
   り、LibreOffice でその一部を自動的に削除したりすることができる。情報が削除さ
   れない限り、その情報の多くは |PDF| を含む他の形式で保存された場合でも保持され
   る。

:guilabel:`O&ptions...` ボタンを押すと次のオプションがある
|SecurityOptions&WarningsDlg| が開く：

:guilabel:`&Remove personal information on saving`
   これをオンにすると、ファイルを保存する際、ファイル特性から使用者データが常に
   削除される。文書と一緒に個人情報を保存し、特定の文書からのみ手動で個人情報を
   削除できるようにするには、これをオフにしろ。
:guilabel:`Ctrl-click required &to open hyperlinks`
   LibreOffice の既定動作では、ハイパーリンクを |Ctrl| を押しながらクリックする
   ことで対象文書が開く。

Application colors
----------------------------------------------------------------------

ページ余白（テキスト境界）、表型や節の境界線、格子線、その他が表示されていると、
執筆、編集、および（特に）ページレイアウトが容易になることがよくある。さらに、
LibreOffice の既定とは異なる色を使いたい場合もあるだろう。

:menuselection:`LibreOffice-->Application colors` ページでは、どの |UI| 要素を表
示するか、またその表示色を指定できる。

* テキスト境界などの項目に対して表示有無を切り替えるには、要素名の横にあるチェッ
  クボックスをオンまたはオフにする。
* 特定の要素の既定色を変更するには、要素名の横にある :guilabel:`Color setting`
  欄の下矢印をクリックし、ドロップダウンリストから色を選択する。
* 色の変更を配色として保存するには、:guilabel:`&Save` を押し、名前を入力し、|OK|
  を押す。

.. |WriterChangesPage| replace:: :menuselection:`LibreOffice Writer-->Changes` ページ

.. note::

   変更履歴モードで使用する色の設定を変更するには、|OptionsDlg|
   |WriterChangesPage| だ。

Choosing options for loading and saving documents
======================================================================

文書の読み込みと保存のオプションは作業方法に合わせて設定できる。

|OptionsDlg| :menuselection:`Load/Save` ノードをクリックする。

General
----------------------------------------------------------------------

|LoadSaveGeneralPage| の選択肢のほとんどは、他の事務用ソフトウェア使用者にはおな
じみのものだ。いくつかの項目を次に示す：

:guilabel:`Load user-specific settings with the document`
   LibreOffice 文書が保存されると、その使用者のシステムの特定の設定も一緒に保存
   される。その文書を別の使用者のシステムで開くと、前の使用者のシステムで保存さ
   れた設定が使用される。このオプションをオフにすると、現在の使用者の設定が、以
   前に文書と一緒に保存された設定を上書きする。

   このオプションがオフである場合でも、一部は文書と常に一緒に読み込まれる：

   * |PrintM| 設定
   * テキスト表組の前の段落の間隔設定
   * リンク、フィールド機能、チャートの自動更新に関する情報
   * アジアの文字形式に関する情報
   * 文書にリンクされているデータ給源に関する設定
:guilabel:`Load printer settings with the document`
   これをオンにすると、前の使用者の印刷機設定が文書に取り込まれる。事務所環境で
   は |PrintDlg| で印刷機を手動で変更しない限り、文書が離れたネットワーク印刷機
   で印刷される可能性がある。オフにする場合、現在の使用者の既定印刷機が文書の印
   刷に使用される。オンオフにかかわらず、現在の印刷機設定は文書とともに保存され
   る。
:guilabel:`Load view position with the document even if it was saved by a different user`
   ビュー位置とは文書内のキャレット位置を意味する。これをオンにすると、誰が文書
   を保存したかにかかわらず、最後に保存したビュー位置が読み込まれる。
:guilabel:`Save &AutoRecovery information every __ minutes`
   自動回復を有効にするかどうか、および自動回復過程で使用される情報を保存する頻
   度を選択する。自動回復では、クラッシュ時に開いているすべての文書を復元するた
   めに必要な情報が保存される。これをオンにするとシステムクラッシュ後の文書の復
   元が容易になる。既定でオンになっている。
:guilabel:`&Edit document properties before saving`
   これがオンであると、文書の |PropertiesDlg| では、新規文書を初めて保存するとき
   （または名前を付けて保存を使用するとき）に、関連情報を入力するよう求められ
   る。
:guilabel:`Al&ways create backup copy`
   文書を保存するたびに、以前に保存した版の文書をバックアップコピーとして別の
   フォルダに保存する。LibreOffice が新しいバックアップコピーを作成すると、以前
   のバックアップコピーが置き換えられる。バックアップコピーの拡張子は ``.bak``
   だ。このオプションは既定でオンになっている。

   .. tip::

      仕事が長くなる可能性のある著者は、LibreOffice で自動バックアップコピーを作
      成できるようにすることを常に考慮すべきだ。

   .. admonition:: 読者ノート

      上のように言われているが、外部ツールによるバージョン管理体制が整っている場
      合にはオフにしておき、ディスクに余分なバックアップファイルが生じないように
      する。

:guilabel:`Save URLs relative to file system / to internet`
   これらのオプションを使用して、ファイルシステムとインターネット上の URL の相対
   アドレスの既定を選択する。詳細については |Guide| を見ろ。
:guilabel:`Default File Format and ODF Settings`
   |ODF| 形式のバージョン。ここはいじらなくていい。

   :guilabel:`D&ocument type`: |MSWord| 使用者と文書を日常的に共有する場合は
   :guilabel:`Always sa&ve as` オプションを Word 形式のいずれかに変更するとよい
   だろう。個々のファイルを保存するときにも Word 形式を選択することができる。

VBA Properties
----------------------------------------------------------------------

:menuselection:`Load/Save-->VBA Properties` ページでは LibreOffice で開いた
Microsoft Office文書にマクロを保持するかどうかを選択する。詳細は |Guide| を見ろ。

Microsoft Office
----------------------------------------------------------------------

:menuselection:`Load/Save-->Microsoft Office` ページでは Microsoft Office |OLE|
オブジェクトをインポートおよびエクスポートする際の処理を選択する。つまり、対応す
る LibreOffice |OLE| オブジェクトに変換するか、または対応する LibreOffice |OLE|
オブジェクトから変換するか、または元の形式で読み込んで保存する。詳細は |Guide|
を見ろ。

HTML compatibility
----------------------------------------------------------------------

:menuselection:`Load/Save-->HTML Compatibility` ページで選択した内容は、
LibreOffice に読み込んだ |HTML| ページおよび LibreOffice から書き出した |HTML|
ページに影響する。詳細は |Help| および |Guide| を見ろ。

Choosing Writer-specific options
======================================================================

|OptionsDlg| :menuselection:`LibreOffice Writer` ノード以下で選択した設定により、
Writer文書の体裁や動作が決まる。

General options
----------------------------------------------------------------------

|WriterGeneralPage| の選択肢は、リンクやフィールドの更新、定規やその他の測定に使
用する単位、既定のタブストップ位置に作用する。

:guilabel:`Automatically Update Fields`
   作業中にフィールドやチャートが自動的に更新されるのは性能が低下するので避けた
   い場合がある。代わりに、フィールドやチャートの情報を参照する場合に自動更新を
   するといい場合がある。
:guilabel:`Update Links when Loading`
   作業形態によっては文書を読み込んだときにリンクが更新されることを望まない場合
   がある（ファイルがネットワーク上の他のファイルにリンクしているなど）。ネット
   ワークに接続していないときにリンクが更新されるのは避けたいだろう。
:guilabel:`Settings`
   :guilabel:`&Measurement unit`
      文書設計者はフォントサイズと字下げやタブなどを簡単に関連付けることができる
      ため、既定の測定値として :guilabel:`Point` を使用することを推奨している。
   :guilabel:`&Tab stops`
      |Tab| を押すたびにキャレットが移動する距離。この設定が |FormattingToolbar|
      の関連コマンドボタンで適用される字下げ距離にも使用され、段落全体の字下げに
      影響する。

      .. tip::

         不要な変更を避けるには、既定のタブ設定に頼らないことだ。むしろ、段落ス
         タイルまたは個々の段落でタブを定義しろ。|Writer04| を読め。

:guilabel:`Word Count`
   :guilabel:`&Additional separators`
      単語を数える場合は、空白文字、タブ文字、改行、段落区切りに加えて、単語を区
      切る文字も指定する。
   :guilabel:`Show standardized page count`
      編集者や出版社は、指定された文字数や単語数を含むページを「標準」ページと定
      義することが多い。これをオンにすると、そのようなページ数を素早く計算するこ
      とができる。

View options
----------------------------------------------------------------------

|WriterViewPage| は、たとえば画面に画像が表示されない場合に確認するとよいページ
だ。

.. rubric:: Guides

:guilabel:`Helplines &While Moving`
   ヘルプラインは、枠や図面物をページ上に正確に配置するのに役立つ。オンにすると、
   選択した物の高さと幅を示す水平線と垂直線が表示される。物が移動すると作業領域
   全体にこれらの線が広がる。

.. rubric:: Display Fields

:guilabel:`Hidden te&xt`
   条件付きテキストまたは隠しテキストフィールドによって隠されたテキストを表示す
   る。
:guilabel:`Hidden p&aragraphs`
   非表示段落フィールドを含む段落を表示する。|MenuBar|
   :menuselection:`&View-->Field &Hidden Paragraphs` と同等。

.. rubric:: Display tracked changes

:guilabel:`Tracked &deletions in margin`
   既定では、削除箇所はテキスト内に取り消し線付きフォントで表示される。削除箇所
   を本文ではなく余白に表示するには、これをオンにする。
:guilabel:`&Tooltips on tracked changes`
   追跡された変更の上にマウスポインターをかざすと、変更の種類、作成者、日付、時
   刻がツールチップ表示される。

.. rubric:: Outline Folding

:guilabel:`&Show outline-folding buttons`
   文書内で選択されている見出しの近くに矢印の付いたボタンが表示される。これをク
   リックすると、現在の見出しから次の見出しへすべてのテキストを折りたたむことが
   できる。
:guilabel:`Include sub &levels`
   さらにこのオプションもオンにする場合、見出しをクリックすると、その見出しのす
   べてのテキストが次の同じレベルの見出しとそのすべての小見出しに折りたたまれ
   る。

他の選択肢は自明なはずだ。そうでない場合は |Help| を参照しろ。

Formatting Aids options
----------------------------------------------------------------------

|FormattingAidsPage| で必要なオプションを選択しろ。

:guilabel:`Layout Assistance`
   :guilabel:`Math baseline alignment`
      数式物の既定の垂直配置を設定し、テキストの基準線を参照として使用するには、
      これをオンにする。物の垂直方向の配置を変更できるようにするにはオフにする。
      詳細は |Math| を参照。
:guilabel:`Display Formatting`
   |MenuBar| :menuselection:`&View-->For&matting Marks` または |StandardToolbar|
   :guilabel:`Formatting Marks` 図像を選択したときに表示される記号はここにあるオ
   プション群によって決まる。段落末尾やタブなどの記号は、文章作成、編集、ページ
   レイアウトに役立つ。たとえば、空白の段落がある場合や、表や図形の幅が広すぎて
   ページの余白に入り込んでいる場合などに表示される。
:guilabel:`Protected Areas`
   :guilabel:`Enable cursor`
      これがオンである場合、保護領域にキャレットを置くことはできるが、変更を加え
      ることはできない。保護と解除の方法は領域によって異なる。
:guilabel:`Direct Cursor`
   文書内の任意の空白領域にテキスト、画像、表組、枠、その他の物体を入力できる機
   能だ。Writer はテキストや物を配置するために、タブ、空白文字、字下げなどの選択
   肢をはめ込む。これらの選択肢の詳細については |Help| を見ろ。

   .. note::

      Direct cursor 機能は多くの奇妙な書式を引き起こす可能性があり、スタイルの厳
      密な使用とは相容れない。

:guilabel:`Image`
   :guilabel:`&Anchor`
      新しく追加した画像の既定錨を選択する。|Writer11| を見ろ。

Grid options
----------------------------------------------------------------------

:guilabel:`&Snap to grid` は物を最も近い格子線に自動的に移動する。画像や表組など
の物の位置を揃える場合にたいへん便利だ。

:menuselection:`LibreOffice Writer-->Grid` ページでは、この機能を有効にするかど
うかと、使用する格子間隔を指定できる。細分が過ぎると物体の配置を十分に制御できな
い場合がある。

.. _writer20-anchor-fonts:

Basic Fonts options
----------------------------------------------------------------------

:menuselection:`LibreOffice Writer-->Basic Fonts (Western)` ページでは既定の段落
スタイル、見出し、一覧、説明、索引のフォントとフォントサイズを選択できる。これら
の値は文書自体で異なる設定が選択されているか、文書の雛形で定義されていない限り、
新しい文書に適用される。

これらの値を LibreOffice インストール時の既定値に戻すには、:guilabel:`Default`
ボタンを押す。

|LanguagesPage| で :guilabel:`Asian` と :guilabel:`Complex &text layout` のどち
らか一方または両方ともオンである場合、それらのフォント設定の追加ページが設けられ
る。

Print options
----------------------------------------------------------------------

|WriterPrintPage| では Writer 文書と一緒に印刷する項目を既定で選択できる。これら
のオプションは |LibreOfficePrintPage| にある、すべての LibreOffice プログラムの
一般的なオプションに追加される。

いくつか考慮すべきことがある：

* 草稿執筆時に印刷機のインクやトナーを節約するために、:guilabel:`Contents` 区画
  の項目をいくつかオフにする。
* :guilabel:`Print text in blac&k` は色テキスト（画像は含まない）を色印刷機で黒
  として印刷します。白黒印刷機では、このオプションは色テキストを灰色の濃淡ではな
  く黒ベタで印刷する。
* これに比べて、|LibreOfficePrintPage| の :guilabel:`Con&vert colors to
  grayscale` オプションは、色印刷機ではすべてのテキストと画像を灰色度として印刷
  する。[#writer20-footnote-print]_
* 両面印刷でない印刷機で両面印刷する場合、左右のページだけを印刷し、他のページを
  裏返して印刷することができる。

.. tip::

   特定の文書を印刷する際に、これらの既定のいずれかを上書きすることができる。
   |PrintM| を選択し、|PrintDlg| のさまざまなページにあるオプションを使え。

Table options
----------------------------------------------------------------------

:menuselection:`LibreOffice Writer-->Table` ページでは、表組の既定の動作を指定で
きる。詳細については |Help| または |Writer13| を見ろ。

いくつか考慮すべきことがある：

* 表組のほとんどが境界線や見出しを必要とする場合は、それらのオプションを選択する
  とよい。表組のほとんどがページレイアウトに使用される場合は :guilabel:`B&order`
  および :guilabel:`H&eading` をオフにしろ。
* 表組がページ間で分割されないようにするには :guilabel:`&Do not split` をオンに
  しろ。
* 表組中に数値データが含まれている場合は :guilabel:`&Number recognition` は非常
  に便利だ。日付や通貨を認識して書式を適切に設定する。しかし、数字を普通のテキス
  トのままにしておきたい場合、この機能はかなり不快であるのでオフにしろ。
* :guilabel:`Keyboard Handling` 区画はキーバインドを使って升目を移動するときの移
  動距離と、はめ込む行や列の寸法を指定する。この目的のためにキーバインドを使用し
  ない場合は、これらの設定を無視することができる。|Help| を見ろ。
* :guilabel:`Behavior of rows/colomns` 区画では行や列の変更が隣接する行、列、表
  組全体に及ぼす影響を指定する。効果を完全に理解するためにはこれらの選択を試行錯
  誤することになるかもしれない。

Changes options
----------------------------------------------------------------------

Writer の変更履歴機能 (|Writer03|) を使用する場合は、|WriterChangesPage| を使用
して、テキストと書式に対する変更のマーク方法を選択する。変更棒はテキストの行に変
更が加えられた箇所を示すことができ、:guilabel:`Lines Changed` の下で書式指定がな
される。

Comparison options
----------------------------------------------------------------------

:menuselection:`LibreOffice Writer-->Comparison` ページのオプションは、
|Writer03| で説明する文書比較機能 |EditTrackCompareM| で使用する詳細度を決定す
る。

単語単位で比較するか、文字単位で比較するか、または既定の :guilabel:`A&uto` によ
るアルゴリズムを使用して比較するかを選択する。:guilabel:`By w&ord` または
:guilabel:`By &character` を選択すると、乱数の選択肢が有効になる。オプションで、
:guilabel:`Ignore &pieces of length` で比較する最小文字数を指定する。

Compatibility options
----------------------------------------------------------------------

|WriterCompatPage| の設定は |MSWord| から文書をインポートするときに主に使用され
る。これらの設定の効果がよくわからない場合は、既定設定のままにしておけ。以下に説
明されていない設定については |Help| を見ろ。:guilabel:`Use as &Default` ボタンを
選択しない限り、選択したすべての設定は現在の文書にしか適用されない。

:guilabel:`Add spacing between paragraphs and tables`
   LibreOffice Writer では段落間隔の扱いが |MSWord| とは異なる。LibreOffice で段
   落または表組の間隔を定義した場合、この間隔は |MSWord| で定義した間隔に追加さ
   れる。これは現在の文書にしか影響しない。

   このオプションをオンにすると、LibreOffice Writer 文書の段落や表組の間に
   |MSWord| 互換の空きが追加される。
:guilabel:`Add paragraph and table spacing at tops of pages`
   段落や表組の前（上）に空白が表示されるように定義できる。このオプションをオン
   にすると、段落がページや列の先頭にある場合、または段落が文書の最初のページに
   配置されている場合、または手動で改改頁した後にも、段落の上に空白が表示され
   る。これは現在の文書にしか影響しない。

   |MSWord| 文書をインポートすると、変換時に空白が自動的に追加される。
:guilabel:`Add paragraph and table spacing at bottom of table cells`
   段落が表組升目の最後の段落である場合でも、その段落に最下段の空白が追加される
   ように指定する。

AutoCaption options
----------------------------------------------------------------------

Writer 文書の表組、画像、枠、|OLE| 物に説明を自動的にはめ込むことが可能だ。これ
を設定するには、:menuselection:`LibreOffice Writer-->AutoCaption` ページのオプ
ションを使用する。自動的に説明を付けたいオブジェクトを選択する。項目を強調表示し
た状態で説明の性質を指定する。

説明文に供給される区分は次だ：

* `Illustration`
* `Table`
* `Text`
* `Drawing`
* `Figure`

説明ラベルに別の名前を使用するには :guilabel:`Category` 欄にその名前を入力する。

.. note::

   例えば、データ表組だけでなくレイアウトにも表組を使用する場合など、すべての表
   組に説明が必要とは限らない。個々の表組、画像、その他にはいつでも右クリックメ
   ニュー |InsertCaptionM| で説明を追加できる。

章ごとの説明番号の付け方、文字スタイル、枠スタイル、:guilabel:`AutoCaption` ペー
ジのその他の項目については、本書の他の章に記載されている。

Mail Merge Email options
----------------------------------------------------------------------

住所録などのデータ給源を使用して個人情報、住所、その他の情報を定型書簡にはめ込む
ことができる。これらの文書は、郵送用に印刷することも、Writer を通じて電子メール
で送信することもできる。詳細については |Writer14| で述べられている。

:menuselection:`LibreOffice Writer-->Mail Merge Email` ページを使用して、定型書
簡を電子メールで送信するための使用者情報と :abbr:`SMTP (Simple Mail Transfer
Protocol)` サーバー情報を設定する。

Choosing language settings
======================================================================

所望の言語構成を整えるためには作業がいくらか必要になることがある：

* 必要な辞書をインストールする
* ロケールと言語設定の一部を変更する
* 綴字と文法のオプションを選択する
* 言語ツールを有効にする

Install the required dictionaries
----------------------------------------------------------------------

多くの言語モジュールは自動的にインストールされる。言語モジュールには、綴字辞書、
分綴辞書、類語辞典の三つまでのサブモジュールを含めることが可能だ。通常、Writer
ではこれらを辞書と呼ぶ。

他の辞書を追加するには、

#. インターネットに接続されていることを確認
#. |MenuBar| から :menuselection:`&Tools-->Lan&guages-->&More Dictionaries
   Online...` を選択
#. Web ブラウザーが開き、インストール可能な追加辞書へのリンクを含むページが表示
   される。
#. 画面の指示に従って必要な辞書を選択し、インストールしろ。

Change some locale and language settings
----------------------------------------------------------------------

LibreOffice がすべての文書または特定の文書で使用するロケールおよび言語設定の詳細
を変更できる。これらのオプションの詳細については |Help| を見ろ。

|OptionsDlg| |LanguagesPage| で必要に応じて設定を変更する。

.. |EnglishUSA| replace:: :guilabel:`English (USA)`

この例では、すべての適切な設定に |EnglishUSA| が選択されているが、複数の言語を混
在させることもできる。例えば、ドイツで仕事をしているのであれば :guilabel:`&User
interface` は |EnglishUSA| にし、数値、通貨、単位などの設定に影響する
:guilabel:`Locale setting` は :guilabel:`German (Germany)` にすることを好むかも
しれない。

言語設定を、すべての新規文書の既定ではなく、現在の文書にしか適用したくない場合は、
:guilabel:`For the current document only` をオンにする。

システム入力言語の変更は、通常、変更後に文書に入力されたテキストに影響する。この
ような動作をさせたくない場合、:guilabel:`Ignore s&ystem input language` を選択し
ろ。新しいテキストは、システム言語ではなく、文書または段落の言語に従う。

必要に応じて、アジア言語（中国語、日本語、韓国語）の支援と、ヒンディー語、タイ
語、ヘブライ語、アラビア語などの |CTL| 言語の支援を有効にするオプションを選択し
ろ。いずれかを選択すると、|OptionsDlg| を次回開いたときに、言語設定の下にいくつ
かの余分なページが表示される。

Choose spelling and grammar options
----------------------------------------------------------------------

綴字検査と文法検査のオプションを変更するには |WritingAidsPage| を使用する。

いくつか考慮すべきことがある：

.. |CheckSpelling| replace:: :guilabel:`Check spelling as you type`

* |MenuBar| :menuselection:`&Tools-->&Automatic Spell Checking` または
  |StandardToolbar| :guilabel:`Toggle Automatic Spell Checking` 図像を使用して、
  文書内の |CheckSpelling| 設定を上書きできる。
* 入力時に文法検査を行うには |CheckSpelling| も有効にしろ。
* すべての大文字の単語と数字を含む単語を含むカスタム辞書を使用している場合、次を
  オンにしろ：

  * :guilabel:`Check uppercase words`
  * :guilabel:`Check words with numbers`
* :guilabel:`Check special regions` とは、ヘッダー、フッター、枠、表組内のテキス
  トも綴字検査がなされることを意味する。

また、ここではどの使用者定義（カスタム）辞書が活動中であるかを選択、新しいカスタ
ム辞書を追加、辞書を編集、カスタム辞書を削除することができる。システムによってイ
ンストールされた辞書は削除できない。:guilabel:`Available Language Modules` およ
び :guilabel:`User-defined Dictionaries` 区画の使用方法については |Help| を見ろ。

.. tip::

   綴字検査の際、:guilabel:`Add to Dictionary` とマークされた単語は、既定で標準
   辞書に追加される。:guilabel:`Ignore All` とマークされた単語は、無視単語一覧辞
   書に追加される。|Writer02| を読め。

Defining and using custom dictionaries
----------------------------------------------------------------------

さまざまなカスタム（使用者定義）辞書を追加することができる。これには、例外辞書
（避けるべき単語、不正確とマークされる単語）や、プロジェクト固有の用語辞書（不正
確とマークされない単語）が含まれる。文書のセットアップ時に、（標準辞書に加えて）
これらのカスタム辞書を使用する場合は、そのいずれかを選択できる。

|Help| にある *Writing Aids* を読め。

Sentence checking
----------------------------------------------------------------------

LibreOffice では、多くの言語で文を検査できる。これらの検査器はその言語が計算機の
既定言語である場合に既定で有効になる。文検査器の規則集は言語によって異なる。

:menuselection:`Language Settings-->English Sentence Checking` ページで、検査す
る項目、報告する項目、自動変換する項目を選択できる。このメニューは、LibreOffice
に既定でインストールされている英語辞書拡張にもある。
[#writer20-footnote-sentence]_ 検査したいオプション機能を選択する。|Writer02|
を見ろ。

追加の文法検査を選択した後、有効にするには LibreOffice を再起動するか、文書を再
読み込みする必要がある。

Activating Language Tool
----------------------------------------------------------------------

LanguageTool は <https://languagetool.org/> が備えている多言語文法、文体、綴字検
査ツールキットだ。使用方法については Web サイトを参照しろ。

LanguageTool の API キーを所有している場合、:menuselection:`Language
Settings-->LanguageTool Server Settings` で :guilabel:`Enable LanguageTool` をオ
ンにし、要求された情報を入力することで、ツールを有効にすることができる。

.. admonition:: 読者ノート

   これは試してみよう。

Customizing menus
======================================================================

|MenuBar| 上のメニューを追加、並べ替えしたり、コマンドを追加したり、その他の変更
を行うことができる。右クリックメニューも同様に変更できる。

|MenuBar| をカスタマイズするには、|CustomizeM| を選択する。|CustomizeDlg| で
|MenusTab| または |ContextMenusTab| を開く。

Modifying an existing menu
----------------------------------------------------------------------

.. |SearchBox| replace:: :guilabel:`&Search` 欄
.. |ScopeList| replace:: :guilabel:`S&cope` ドロップダウンリスト
.. |TargetList| replace:: :guilabel:`&Target` ドロップダウンリスト
.. |AssignedCommandsList| replace:: :guilabel:`Assi&gned Commands` 一覧
.. |AvailableCommandsList| replace:: :guilabel:`&Available Commands` 一覧

#. |CustomizeDlg| の右上にある |ScopeList| でカスタマイズしたメニューを
   LibreOffice Writer のすべてに適用するか、特定の文書だけに適用するかを選択す
   る。
#. |TargetList| でカスタマイズするメニューを選択する。一覧には主メニューと副メ
   ニューが含まれる。選択したメニューのコマンドは |AssignedCommandsList| に表示
   される。
#. 選択したメニューにコマンドを追加するには、|AvailableCommandsList| でコマンド
   をクリックし、大きな右矢印を押す。左上の |SearchBox| を使用するか、ドロップダ
   ウンリストで区分を選択することで、検索を絞り込むことができる。右側の上下の矢
   印を使用して、一覧内の必要な位置にコマンドを移動する。
#. 選択したメニューからコマンドを削除するには、|AssignedCommandsList| でそのコ
   マンドをクリックし、大きな左矢印を押す。
#. 区切りや副メニューをはめ込むには、はめ込む項目の直前の項目を選択し、
   :menuselection:`&Insert-->` ドロップダウンメニューのコマンドを使用する。
#. メニュー項目の名前を変更するには、|AssignedCommandsList| でその項目を選択し、
   :menuselection:`&Modify-->Rename...` で名前の変更を選択する。
#. すべての変更が終わったら |OK| を押して保存する。

Creating a new menu
----------------------------------------------------------------------

お気に入りメニューや、特定のプロジェクト用のツールを集めたメニューが便利だろう。
新しいメニューを作成するには：

#. |CustomizeDlg| |MenusTab| で :guilabel:`&Target` 横のハンバーガー記号を押し、
   ドロップダウンメニューから :menuselection:`&Add...` を選択し、:guilabel:`New
   Menu` ダイアログボックスを開く。
#. :guilabel:`&Menu name` ボックスに新しいメニューの名前を入力する。
#. 上下の矢印ボタンを使って、新しいメニューを必要な位置に移動する。
#. |OK| を押して保存し、|CustomizeDlg| に戻る。

新しいメニューは |CustomizeDlg| のメニュー一覧に表示される。カスタマイズを保存し
た後、|MenuBar| に表示される。

新しいメニューを作成したら、上で説明したメニューの変更と同様に、いくつかのコマン
ドを追加する必要がある。

Customizing toolbars
======================================================================

ツールバーのカスタマイズには、表示する図像の選択や入渠したツールバーの位置の固
定、ツールバーで使用できる図像（コマンド）一覧の追加や削除など、いくつかの方法が
ある。また、新しいツールバーを作成することもできる。

Modifying existing toolbars
----------------------------------------------------------------------

.. |ToolbarsTab| replace:: :guilabel:`Toolbars` タブ

ツールバーの作成と修正の手順は、メニューの場合と似ている。

#. |MenuBar| から |CustomizeM| を選択する。
#. |CustomizeDlg| |ToolbarsTab| で、右上の |ScopeList| で、この変更したツール
   バーを Writer 用に保存するか、選択した文書用に保存するかを選択する。
#. |TargetList| でカスタマイズするツールバーを選択する。現在のツールバーの内容は
   |AssignedCommandsList| に表示される。
#. 左側の |AvailableCommandsList| でコマンドを選択する。左上の |SearchBox| を使
   用するか、すぐ下のドロップダウンリストで区分を選択することで、検索を絞り込む
   ことができる。
#. 大きな右矢印をクリックして、選択したコマンドをツールバーの
   |AssignedCommandsList| に追加する。右端の上下の矢印を使用して、コマンドをツー
   ルバーに配置する。
#. ツールバーからコマンドを削除するには、右側の |AssignedCommandsList| でコマン
   ドを選択し、大きな左矢印を押す。
#. ツールバーに割り当てられているコマンド表示を切り替えるには、右側の
   |AssignedCommandsList| にある図像のチェックボックスをオンまたはオフにする。
#. 区切りをはめ込むには、それを置きたい場所の直前の項目を選択し、
   :menuselection:`&Insert-->` ドロップダウンメニューのコマンドを使用する。
#. ツールバー項目の名前を変更するには |AssignedCommandsList| で項目を選択し、
   :menuselection:`&Modify-->Rename...` で名前の変更を選択する。

すべての変更が終わったら |OK| を押して保存する。

Creating a new toolbar
----------------------------------------------------------------------

新しいツールバーを作成するには：

#. |MenuBar|  |CustomizeM| を選択する。
#. |CustomizeDlg| |ToolbarsTab| で、|TargetList| の横にあるハンバーガー記号を押
   し、:menuselection:`&Add...` を選択して |NameDlg| を開く。
#. |NameDlg| で、新しいツールバーの名前を入力し、:guilabel:`&Save in` ドロップダ
   ウンリストでこの新しいツールバーの保存先を選択する。

新しいツールバーが |CustomizeDlg| のツールバー一覧に表示される。新しいツールバー
を作成したら、上記のようにコマンドをいくつか追加する必要がある。

Choosing icons for toolbar commands
----------------------------------------------------------------------

.. |ChangeIconDlg| replace:: :guilabel:`Change Icon` ダイアログボックス

ツールバーのボタンには通常、文字ではなく図像が付いているが、すべてのコマンドに図
像が付いているわけではない。コマンドに図像がない場合は、図像を選択できる。図像を
選択するには、右側の一覧でコマンドを選択し、:menuselection:`&Modify-->Change
Icon...` を押す。|ChangeIconDlg| で利用可能な図像をスクロールして選択し、|OK| を
押してコマンドに割り当てる。

カスタム図像を使用するには、画像プログラムで図像を作成し、|ChangeIconDlg| の
:guilabel:`I&mport...` ボタンを押して LibreOffice にインポートする。カスタム図像
は、最高の品質を得るために 16×16 ピクセルの寸法にし、256 色を超えないようにしろ。

Customizing the user interface
======================================================================

.. admonition:: 読者ノート

   |Writer21| の冒頭を読め。

Assigning shortcut keys
======================================================================

.. |KeyboardTab| replace:: :guilabel:`Keyboard` タブ

組み込みのキーバインドを使用するだけでなく、他のキーバインドを定義することもでき
る。キーバインドは LibreOffice の標準機能または独自のマクロに割り当てることがで
き、Writer または LibreOffice プログラム群全体で使用するために保存できる。

キーバインドを自分の要求に合わせるには、|CustomizeDlg| |KeyboardTab| を使用する。

#. キーバインドの割り当てを LibreOffice のプログラム全部で使用するか、Writer で
   しか使用しないかを選択する。
#. ページ上部の :guilabel:`Shortcu&t Keys` 一覧で必要なキーバインドを選択する。
#. :guilabel:`&Category` と :guilabel:`&Function` 一覧で必要な機能を選択する。
#. :guilabel:`&Modify` ボタンを押す。選択したキーが右下の :guilabel:`&Keys` 一覧
   に表示される。
#. |OK| を押す。

必要に応じて繰り返す。

.. note::

   |F1| や |F10| など、|CustomizeDlg| の一覧で灰色表示されているキーバインドは再
   割り当てできない。

Saving changes to a file
----------------------------------------------------------------------

キーバインドの割り当ての変更は、後で使用するためにキーボード設定ファイルに保存す
ることができるので、必要に応じて異なる設定を作成し、適用することができる。キーバ
インドをファイルに保存するには：

#. キーバインドの割り当てを行った後、|CustomizeDlg| の右側にある
   :guilabel:`&Save...` ボタンを押す。
#. :guilabel:`Save Keyboard Configuration` ダイアログボックスで |FileNameBox| に
   キーバインド設定ファイルの名前を入力するか、一覧から既存のファイルを選択す
   る。ファイルを保存する場所を参照する。[#writer20-footnote-cfg]_
#. |Save| を押す。既存のファイルを上書きしようとしている場合は確認ダイアログボッ
   クスが表示されるが、そうでない場合は何も表示されず、ファイルが保存される。

Loading a saved keyboard configuration
----------------------------------------------------------------------

保存したキーボード設定ファイルをロードして既存の設定を置き換えるには、
|CustomizeDlg| の :guilabel:`&Load...` ボタンを押し、:guilabel:`Load Keyboard
Configuration` ダイアログボックスで設定ファイルを選択する。

Resetting the shortcut keys
----------------------------------------------------------------------

すべてのキーバインドを既定値にリセットするには、|CustomizeDlg| の |ResetButton|
を押す。確認ダイアログボックスは表示されない。

Assigning macros to events
======================================================================

LibreOffice では、何かが起こったとき、イベントが発生したと言う。たとえば、文書が
開かれた、キーが押された、マウスが動いたなどだ。マクロをイベントに関連付けると、
イベントが発生したときにマクロが実行される。たとえば、「文書を開く」イベントを割
り当てて、文書の特定のセットアップタスクを実行するマクロを実行するのが一般的な使
い方だ。

マクロをイベントに関連付けるには、|CustomizeDlg| の :guilabel:`Events` タブを使
用する。詳細については |Guide| を参照しろ。

Adding functionality with extensions
----------------------------------------------------------------------

拡張とは、LibreOffice にインストールして新しい機能を追加できるパッケージだ。雛形
集、綴字辞書、クリップアートギャラリー、マクロ、ダイアログボックスライブラリー
は、LibreOffice 拡張としてパッケージにできる。拡張は新しいトップレベルメニュー、
サブメニュー、またはツールバー図像を追加できる。また、拡張には独自の設定がある。

いくつかの拡張は LibreOffice に同梱され、プログラムと一緒にインストールされ
る。これらはインストールオプションを変更することでしか削除できない。その他の拡張
は、さまざまなウェブサイトからダウンロードできる。公式の拡張リポジトリーは
<https://extensions.libreoffice.org/> にある。これらの拡張は無料だ。

他の給源からの拡張には、無料で利用できるものもあれば、有料で利用できるものもあ
る。どのような免状と料金が適用されるか、記述を確認しろ。

好きなフォルダーに拡張をダウンロードしろ。[#writer20-footnote-downloads]_

Installing extensions
----------------------------------------------------------------------

リポジトリーに一覧されている拡張をインストールする手順：

#. |MenuBar| から |ExtensionsM| を選択する。
#. |ExtensionsDlg| で :guilabel:`Get more extensions online...` をクリックする。
#. インターネットブラウザーが開く。インストールしたい拡張を見つけて選択し、計算
   機にダウンロードする。
#. 拡張のダウンロードと保存が完了したら |ExtensionsDlg| に戻り、:guilabel:`&Add`
   を押す。インストールしたい拡張を見つけて選択し、|Open| を押す。拡張のインス
   トールが始まる。免状契約に同意するよう求められる場合がある。
#. インストールが完了すると、拡張が |ExtensionsDlg| に表示される。

レポジトリーに一覧されていない拡張をインストールするには、ダウンロードした後に上
記の 3. に進め。

Updating extensions
----------------------------------------------------------------------

インストールされている拡張の更新を確かめるには、|ExtensionsDlg| の
:guilabel:`Check for &Updates` ボタンを押せ。

Removing and disabling extensions
----------------------------------------------------------------------

インストールした拡張を削除（アンインストール）するには、|ExtensionsDlg| のメイン
ウィンドウで拡張を選択し、|RemoveButton| を押す。

拡張を削除（アンインストール）せずに無効にするには、|ExtensionsDlg| のメインウィ
ンドウで拡張を選択し、:guilabel:`&Disable` ボタンを押す。

Adding fonts
======================================================================

LibreOffice は PostScript (.pfb), TrueType (.ttf), OpenType (.otf) のフォント
ファイル形式を支援している。その他のフォント形式も存在し、OS で支援されている場
合もあるが、これらの形式は選択と品質に制限がある場合がある。

管理者権限があれば、OS から追加のフォントをインストールすることができ、
LibreOffice で使用できるようになり、Writer のフォント一覧に表示される。

Finding free-licensed fonts
----------------------------------------------------------------------

Adobe などの専売特許フォントに加え、何百もの自由免状フォントが利用可能だ。自由免
状フォントは、自由に使用、共有、編集することができる。ほとんどは無償で利用可能
だ。多くは古典的なフォントの複製やそれに近いものだが、中には独自のフォントもあ
る。

多くの Linux ディストリビューションは、パッケージリポジトリーにいくつかの自由免
状フォントを含んでいる。自由免状のフォントを見つけることができる他の場所には、
`The League of Moveable Type <https://www.theleagueofmoveabletype.com/>`__ や
`Font Library <https://fontlibrary.org/>`__ がある。

Adding custom colors
======================================================================

カスタム色を色パレットに追加する手順：

#. 正方形などの図面物を文書に挿入する。
#. 物を右クリックし、コンテキストメニューから :menuselection:`A&rea...` を選択す
   る。
#. :guilabel:`Color` ボタンを押す。:guilabel:`Pa&lette` で新しい色を追加したいパ
   レットを選択する。:guilabel:`New` の下で新しい色を定義するか、
   :guilabel:`Pick` ボタンを押して :guilabel:`Pick a Color` ダイアログボックスで
   色を選択する。
#. 左下の :guilabel:`&Add` ボタンをクリックし、|NameDlg| に新しい色の名前を入力
   し、|OK| を押して保存する。
#. 必要なければ、文書から図面物を削除する。

.. _writer20-anchor-themes:

Setting up document themes
======================================================================

文書テーマは、さまざまな書式選択を一つにまとめ、二回のクリックで適用したり変更し
たりできる。テーマ色は、LibreOffice Writer 7.6 で実装された。フォントと書式の設
定は、後のリリースで予定されている。

LibreOffice にはテーマ色の集合がいくつか用意されている。独自の集合を定義するに
は：

#. |MenuBar| の :menuselection:`F&ormat-->The&me...` を選択する。|ThemeDlg| で開
   始点として使用するテーマを選択し、:guilabel:`&Add` ボタンを押す。
#. |ThemeColorEditDlg| で新しいテーマに名前を付け、利用可能なパレットから色を選
   択する。
#. |OK| を押して新しいテーマを保存し、|ThemeDlg| に表示する。

文書テーマの使い方については |Writer06| を参照しろ。

.. note::

   使用者定義のテーマ色集は文書内にのみ保存され、他の文書で使用するには雛形を作
   成する必要がある。

   テーマは |MSWord| との互換性を高める。ただし、これらはまだ |ODF| の一部ではな
   いため、使用するには ODF 1.3 Extended に保存する必要がある。

----

.. rubric:: 章末注

.. [#writer20-footnote-print] 白黒印刷機では、色付き画像は灰色度として印刷される
   のが通例だ。
.. [#writer20-footnote-sentence] |ExtensionsDlg| で :guilabel:`Engligh spelling
   dictionaries` を選択して :guilabel:`&Options` ボタンを押してメニューを表示する。
.. [#writer20-footnote-cfg] ファイルの拡張子は ``.cfg`` だ。
.. [#writer20-footnote-downloads] 通常は :file:`%USERPROFILE%\\Downloads` だ。
