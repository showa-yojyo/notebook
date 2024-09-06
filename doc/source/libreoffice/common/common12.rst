======================================================================
Chapter 12, Configuring LibreOffice ノート
======================================================================

.. include:: ./common-inc.txt

.. contents:: 章見出し
   :depth: 2
   :local:

Introduction
======================================================================

|MenuBar| :menuselection:`&Tools-->&Options...` 選択で開く |OptionsDlg| につい
て。

.. tip::

   選択肢の内容を理解するのが難しい場合は、使用者手引で設定の変更を推奨している
   場合を除き、通常は既定設定のままにしておくのが良い。

LibreOffice options
======================================================================

LibreOffice のすべての部品に適用される選択肢と設定について。

|OptionsDlg| の左側の木は開いている LibreOffice プログラムによって異なる。木の開
閉マークをクリックすると、ダイアログボックスの右側に関連するページが現れる。

.. note::

   使用している LibreOffice のバージョンが US English でない場合、|UI| ラベルの
   一部が本書の図と異なる。

   |OptionsDlg| 右下の |ResetButton| はそのページの値をダイアログボックスを開い
   たときの値にリセットする。

.. admonition:: 利用者ノート

   後述する設定で |UI| 言語を US English にしろ。

User data
----------------------------------------------------------------------

このページの内容は、たとえば、文書性質の作成者や最終編集者、コメントや変更の作成
者、メーリングリストの送信者アドレスなどに用いられる。

ここに正しい使用者情報が表示されていることを確認する必要がある。必要情報が空白で
ある項目は情報を入力し、不要な既存の情報は修正または削除しろ。

文書性質に使用者データを使用しない場合は、開いている LibreOffice ファイルに対し
て |FilePropertiesM| を選択し、|GeneralTab| :guilabel:`&Apply user data` をオフ
にしろ。

:guilabel:`Cryptography` では OpenPGP 暗号化と電子署名に使用する公開鍵を設定す
る。:doc:`common10` を見ろ。

General
----------------------------------------------------------------------

.. rubric:: Help

:guilabel:`&Extended tips`
   |UI| 要素上にマウスカーソルを移動してじっとするとツールチップを表示する。オン
   にするほうが良い。
:guilabel:`&Show "Tip of the Day" dialog on start-up`
   プログラム起動時に :guilabel:`Tip of the Day` ダイアログボックスを開きたいの
   でオンにする。コツの全部を習得したらオフにすればいい。

.. rubric:: Open/Save Dialogs

:guilabel:`&Use LibreOffice dialog`
   LibreOffice に付属のファイルダイアログボックスを使用するかどうか。Windows 標
   準のそれを使用したいので、本ノートではオフを想定している。

View
----------------------------------------------------------------------

文書ウィンドウの表示や動作に影響する。計算機の OS によって異なる選択肢がある。

.. rubric:: Icon Size

すべてのドロップダウンリストの内容を `Small` に設定したい。

.. rubric:: Graphics Output

:guilabel:`Use hard&ware acceleration`
   ハードウェア機能に直接アクセスして画面表示を改善する。オン。
:guilabel:`Use anti-a&liasing`
   オンにすれば画が滑らかに描かれるが、おそらく何かの負担が増す。

   .. tip::

      |Ctrl+Shift| + :kbd:`R` を押してアンチエイリアス設定を変更した後に現在の文
      書の描画を更新し、効果を確認する。

.. rubric:: Font Lists

:guilabel:`Show p&review of fonts`
   フォントドロップダウンリストの描画に影響する。オンしかない。
:guilabel:`Screen font anti-aliasin&g`
   テキストの画面表示を滑らかにする場合にオンにする。アンチエイリアスを適用する
   最小の文字寸法を指定できることに注意。

Print
----------------------------------------------------------------------

LibreOffice の一般的な印刷選択肢は最も一般的な印刷方法に合わせて選択する。

.. rubric:: Settings for

印刷機を持っていないからといって :guilabel:`Print to &file` を選ぶというようなこ
とはしなくて良い？

.. rubric:: Defaults

:guilabel:`Con&vert colors to grayscale` はオンにしてもいいかもしれない。

.. rubric:: Reduce bitmaps

ビットマップを画質を落として印刷することを指定する。解像度を下げることはできるが
上げることはできない。

.. admonition:: 読者ノート

   印刷機に送信されるデータ量を減らすと、印刷ファイルが小さくなり、印刷速度が向
   上することについてはすでに述べられている。

.. rubric:: Reduce transparency

透明物を通常の非透明物と同様に印刷するための選択肢。透明な画像を印刷機に直接送る
ことはできないので、この項目群がある。

.. rubric:: Warnings

印刷開始前に表示される警告を決める。ここにあるもの全部をオンにしたい：

* :guilabel:`P&aper size`
* :guilabel:`Pap&er orientation`
* :guilabel:`&Transparency`

.. rubric:: Reduce Gradient

:guilabel:`Reduce &gradient`
   オンにするとグラデーションは品質を落として印刷される。
:guilabel:`Intermediate &color`
   オンにしてしまうと、グラデーションが単一の中間色のみで印刷される。

Paths
----------------------------------------------------------------------

|PathsPage| では LibreOffice に関連付けられた、または LibreOffice で使用される
ファイルの場所を作業状況に合わせて変更できる。

項目によってはパスが二つ表示されることがある。

* :guilabel:`User Paths` は使用者固有のフォルダーで、通常は単一の計算機内のどこ
  かを指す。
* :guilabel:`Internal Paths` は、LibreOffice がインストールされている共有フォル
  ダーで、通常はネットワーク上にある。

.. tip::

   |PathsPage| にある項目を使用して、AutoText を含むファイルなど、バックアップの
   作成や別の計算機へのコピーに必要なファイルの一覧を作成するがよい。

Fonts
----------------------------------------------------------------------

|LibreOfficeFontPage| では文書に表示される字体の置換を定義可能だ。文書が他の計算
機から受信された場合、使用する計算機システムにインストールされていない字体を含む
可能性がある。必要な場合、このページに表示されている字体を使用して見つからない
フォントを置き換えることが可能だ。この字体置換によって、文書指定字体が変更される
ことはない。

.. rubric:: Replacement Table

したがって、他人が作成した文書を読まない場合にはこのページを触れることはない。

.. rubric:: Font settings for HTML, Basic and SQL Sources

|HTML| と Basic のソースコードを表示するための字体を選択する。愛用しているエディ
ターの設定に合わせる。

Security
----------------------------------------------------------------------

:menuselection:`LibreOffice-->Security` ページでは文書の保存とマクロを含む文書を
開く際の取り扱いを指定する。

.. rubric:: Security Options and Warnings

:guilabel:`O&ptions...` ボタンを押すと |SecurityOptions&WarningsDlg| が開く。文
書内の情報の変更や閲覧を制限する選択肢に出入りできる。:ref:`common10-anchor-B`
を見ろ。

.. rubric:: Passwords for Web Connections

マスターパスワードを入力すると、使用者名とパスワードが必要な Web サイトに簡単に
出入りできるようになる。使わない。

.. rubric:: Macro Security

:guilabel:`Macro Securit&y...` ボタンを押すと |MacroSecurityDlg| が開き、マクロ
の実行と信頼できる供給源を指定するための安全度を調整できる。

.. rubric:: Certificate Path

Windows の場合、LibreOffice は証明書の保存と取得に Windows 既定の場所を用いる。

.. rubric:: TSAs

LibreOffice で作成された |PDF| 文書の :abbr:`TSA (Time Stamp Authority)` |URL|
を随意選択する。信頼できる時刻標記を持つ |PDF| 文書の受信者は、文書がいつ電子署
名されたかを確認できる。

Personalization
----------------------------------------------------------------------

テーマを使用して LibreOffice の全体的な外観を変更できる。:guilabel:`Default
look, do not use Themes` で十分だ。

Application colors
----------------------------------------------------------------------

|ApplicationColors| では LibreOffice の |UI| に使用する色を設定することで
LibreOffice の全体的な外観を変更する。現在使用されている配色の設定は保存可能で、
後で再度読み込むことが可能だ。

色を変更すると、たとえば、文章を書くとき、編集するとき、ページレイアウトやページ
余白を作成するとき、改頁や図を入れるときなど、LibreOffice を使いやすくなる。使用
者は LibreOffice の既定色とは異なる色を好むことがある。

.. note::

   隠蔽不能 |UI| 要素がある。

   マウスカーソルの視認性を高めるには、アプリケーションの背景を 40% から 60% の
   灰色に設定する。背景が `Automatic` に設定されている場合、40% 灰色だ。

Accessibility
----------------------------------------------------------------------

|OptionsDlg| :guilabel:`Accessibility` ページでグラフィックやテキストのアニメー
ションを許可するかどうか、高対比表示、|UI| の字体の変更方法などの選択肢がある。

.. rubric:: Miscellaneous options

:guilabel:`Support &assistive technology tools (program restart required)`
   外付けの画面読み取り、点字機器、音声認識入力装置などの支援用具を使用可能。オ
   ンにする前に、|JRE| を計算機にインストールする必要がある。次の節も見ろ。
:guilabel:`Use te&xt selection cursor in read-only text document`
   読み取り専用文書にキャレットを表示する。DeepL にかけられるようにオンにしたい。
:guilabel:`Allow animated &images`
   |GIF| 画像などのアニメーションを行うかどうか。オフでいい。
:guilabel:`Allow animated &text`
   点滅やスクロールなどのアニメーションテキストをオンにする。|HTML| 的な機能か。
   オフでいい。

.. rubric:: Options for High Contrast Appearance

高対比は OS の設定であって、より読みやすくするためにシステムの配色を変更するもの
だ。高対比モードが有効な場合、升目の境界と影は常にテキスト色で描かれる。その場
合、升目の背景色は無視される。

:guilabel:`High contrast`
   `Automatic` モードを選択すると、システムの背景色がえらく暗い場合に
   LibreOffice が高対比モードに切り替わる。えらく暗いの判断はシステムによる？

:guilabel:`Use automatic font &color for screen display`
   システム色設定を使用して LibreOffice 上の文字を表示する。画面表示に限り影響す
   る。
:guilabel:`&Use system colors for page previews`
   OS の高対比設定をページプレビューに適用する。

Advanced
----------------------------------------------------------------------

|LibreOfficeAdvancedPage| ではどの |JRE| を使用するかなど、Java アプリケーション
の対応選択肢を指定し得る。また、マクロ記録などの実験的な（不安定な）機能を使用す
るかどうかも指定する。

.. rubric:: Java Options

LibreOffice のインストール後に |JRE| がインストールされた場合、または計算機に複
数の |JRE| がインストールされている場合は、ここで LibreOffice が使用する |JRE|
を選択する。 LibreOffice が計算機に複数の |JRE| を検出すると一覧表示する。一覧か
ら使用する |JRE| を選択しろ。

:guilabel:`&Use a Java runtime environment`
   オンにする。

.. rubric:: Optional Features

:guilabel:`Enable experimental features (may be unstable)`
   オフにする。具体的な内容は LibreOffice のバージョンによって異なる。

:guilabel:`Enable macro recording (may be limited)`
   マクロを使う場合にはオンにする。:doc:`common11` を見ろ。

.. note::

   :guilabel:`Expert Configuration` ダイアログボックスにある項目が何をするものな
   のかがわからない場合、既定値のままにしておけ。LibreOffice の使用者プロファイ
   ルが不安定になったり、一貫性がなくなったり、使用できなくなったりする。

Online update
----------------------------------------------------------------------

:menuselection:`LibreOffice-->Online update` ページでは LibreOffice のオンライン
アップデートの自動通知とダウンロードの選択肢を指定する。

.. rubric:: Online Update Options

:guilabel:`&Check for updates automatically`
   定期的にオンライン更新を確認する場合にオンにして、LibreOffice がオンライン更
   新を確認する頻度を指定する。LibreOffice はインターネット接続が検出され次第、
   指定のタイミングで更新を調べる。

   これ単体ならオンにしてもよい。更新がある場合、メインウィンドウの右上に通知が
   来る。

.. rubric:: Download Destination

ダウンロードしたファイルの保存先フォルダーを表示する。

:guilabel:`&Download updates automatically`
   指定したフォルダーへの更新の自動ダウンロードを有効にする。

   LibreOffice 一式はファイル容量がべらぼうに大きいのでオフにするのがいい。私の
   PC では :program:`winget` 実行時に他のアプリケーションと同時に更新する運用に
   している。

.. rubric:: User Agent

LibreOffice のバージョン、OS 情報、ハードウェアに関する基本的な情報を送信する。
オンにしてダウンロードを最適化させたい。

OpenCL
----------------------------------------------------------------------

|OpenCL| を有効にすると、LibreOffice は |GPU| で実行される超高速数値計算の恩恵に
与れる。この機能を使用するには計算機のビデオカードドライバーが |OpenCL| に対応し
ている必要がある。

.. admonition:: 利用者ノート

   :guilabel:`OpenCL is available for use` が表示されていればオンにするのがいい
   はずだ。

Loading and saving documents
======================================================================

|OptionsDlg| :menuselection:`Load/Save-->` 各ページ。

General
----------------------------------------------------------------------

|LoadSaveGeneralPage| では文書保存の既定設定とファイル形式を選択する。

.. rubric:: Load

:guilabel:`&Load user-specific settings with the document`
   LibreOffice 文書には計算機システムから読み込まれた設定が含まれている。文書を
   保存するとこれらの設定も一緒に保存される。オンにすると、文書の読み込み時に、
   保存されている設定が無視され、計算機の設定が優先される。

   これがオンでもオフでも、文書にリンクされたデータ供給源とそのビューは文書と一
   緒に読み込まれる。
:guilabel:`Load &printer settings with the document`
   オンにすると印刷機設定が文書と一緒に読み込まれる。このため、文書がネットワー
   クの向こうにある印刷機に印刷されることがある。これを防ぐには、|PrintDlg| でプ
   印刷機を手動で変更しろ。オフにした場合、文書の印刷には既定の印刷機が使用される。

   これがオンでもオフでも、現在の印刷機設定は文書とともに保存される。
:guilabel:`Load view position with &the document even if it was saved by a different user`
   本書に載っていない。オフにしておく。

.. rubric:: Save

:guilabel:`Save &AutoRecovery information every __ minutes`
   オフでかまわない。
:guilabel:`&Edit document properties before saving`
   ファイルを初めて保存するときと、Save As 実行時に |PropertiesDlg| を開くように
   指定する。オンにするのが上品だろう。
:guilabel:`Al&ways create backup copy`
   オフでいい。
:guilabel:`Save &URLs relative to file system` :guilabel:`Save URLs relative to &internet`
   これらをオンにすると、ファイルシステムやインターネット上の |URL| の相対アドレ
   ス指定が既定で指定される。相対アドレス指定は元文書と被参照文書が同じドライブ
   上にある場合にしか可能でない。

   相対アドレスは常に現在の文書があるディレクトリーから始まる。絶対アドレスは常
   にルートディレクトリーから始まる。

   どちらもオンにしたい。

.. rubric:: Default File Format and ODF Settings

:guilabel:`ODF &format version`
   後方互換性に問題があることもあるが `1.3 Extended (recommended)` が無難。
:guilabel:`D&ocument type`
   既定のファイル形式を定義する文書型を指定する。意外に意味不明。
:guilabel:`Always sa&ve as`
   上で選択された型の文書が、横のドロップダウンリストから選択されたファイル型と
   して常に保存されることを指定する。現在の文書の別のファイル型を |SaveAsDlg| で
   選択することが可能。
:guilabel:`Warn when &not saving in ODF or default format`
   オンにすると、選択された既定形式または |ODF| 形式以外の形式で文書を保存すると
   きに警告が表示される。オンでもオフで問題ない？

VBA properties
----------------------------------------------------------------------

:menuselection:`Load/Save-->VBA Properties` ページでは :abbr:`VBA (Visual Basic
for Applications)` コードによる Microsoft Office 文書の読み込みと保存に関する一
般的な性質を指定する。

割愛。

Microsoft Office
----------------------------------------------------------------------

:menuselection:`Load/Save-->Microsoft Office` ページでは Microsoft Office やその
他の文書のインポートとエクスポートの設定を行う。

.. rubric:: Embedded Objects

Microsoft Office 物体またはその他の |OLE| 物体のインポートおよびエクスポート方法
を指定する。これらの設定は、Microsoft またはその他の |OLE| サーバーが存在しない
場合 (UNIX) または |OLE| 物体を編集できる LibreOffice |OLE| サーバーがない場合に
有効だ。

.. rubric:: Character Highlighting

Microsoft Office には LibreOffice の文字強調表示と同様の文字属性が二つある。
LibreOffice の文字強調表示を Microsoft Office ファイル形式にエクスポートするとき
に LibreOffice が使用する属性（強調表示または網掛け）を選択するには、ここを使え。

:guilabel:`Highlighting`
   LibreOffice の強調表示色と Microsoft の強調表示色 16 色のうち、最も近い色を出
   力する。この文字属性により、Microsoft Office 使用者が Microsoft Office アプリ
   ケーションのハイライトツールで簡単に編集できるようになる。
:guilabel:`Shading`
   すべての RGB 色を他の Microsoft Office 文字属性にエクスポートする。これによ
   り、LibreOffice 文書と Microsoft Office 文書の間で色の忠実性が保たれるもの
   の、Microsoft Office 使用者は Microsoft Office アプリケーションでは一般的に
   使用されていないか、簡単に見つからない道具を使用して、この文字属性を編集する
   必要がある。これは LibreOffice 7.0 以降の既定値だ。

.. rubric:: Lock files

LibreOffice ロックファイルに加えて Microsoft Office ロックファイルを生成する。オ
フだ。

HTML compatibility
----------------------------------------------------------------------

:menuselection:`Load/Save-->HTML compatibility` ページで |HTML| の表示設定を行う。

.. rubric:: Font sizes

|HTML| の ``<font size=1>`` から ``<font size=7>`` タグそれぞれの文字寸法を与え
る。|HTML| の教科書を当たるとこのタグを使うなとある。既定値のまま捨て置く。

.. rubric:: Import

|HTML| 文書をインポートするための設定。インポートする気がないので、項目が三つほ
どあるがこれらも既定値で放置する。

.. rubric:: Export

:guilabel:`LibreOffice &Basic`
   |HTML| 形式へのエクスポート時に LibreOffice Basic の命令を含める。LibreOffice
   Basic スクリプトを作成する前にこれをオンにする必要がある。LibreOffice Basic
   IDE でマクロが作成されると、|HTML| 文書のソーステキストのヘッダーに現れる。
:guilabel:`Display &warning`
   |HTML| にエクスポートするときに LibreOffice Basic マクロが失われる旨を警告する。
:guilabel:`&Print layout`
   選択した場合、現在の文書の印刷レイアウト（例えば、ページ番号と目次）もエクス
   ポートされる。これは、LibreOffice、Mozilla Firefox、MS Internet Explorer で読
   むことが可能だ。
:guilabel:`&Copy local images to internet`
   |FTP| を使用してアップロードする場合、埋め込み画像をインターネットサーバーに
   自動的にアップロードする。|SaveAsDlg| を使用して文書を保存し、インターネット
   上のファイル名として完全な |FTP| |URL| を入力する。

.. |XXXXX| replace:: 一部の選択肢は一度編集するとリセット不可能だ。手動で変更を
   戻すか、|CancelB| を押して |OptionsDlg| を開き直せ。

Language settings
======================================================================

.. |LangLocale| replace:: :menuselection:`Languages and Locales Settings-->Languages`
.. |LangLocaleGeneralPage| replace:: :menuselection:`Languages and Locales Settings-->General` ページ
.. |LangLocalJapanesePage| replace:: :menuselection:`Languages and Locales Settings-->Searching in Japanese` ページ
.. |LangLocalLangAsianLayoutPage| replace:: :menuselection:`Languages and Locales Settings-->Asian Layout` ページ
.. |LangLocalLangToolServerPage| replace:: :menuselection:`Languages and Locales Settings-->Language Tool Server` ページ
.. |LangLocalEnglishSentencePage| replace:: :menuselection:`Languages and Locales Settings-->English Sentence Checking` ページ

|OptionsDlg| |LangLocale| を選択すると、言語、筆記補助器具、言語器具の性質を定義
するページが開く。

.. note::

   |LangLocalJapanesePage| および |LangLocalLangAsianLayoutPage| 両ページは
   |LangLocaleGeneralPage| ページの :guilabel:`Asian` がオンである場合に限り現れ
   る。Complex Text Layout ページは :guilabel:`Complex &text layout` がオンであ
   る場合に限り現れる。

Languages
----------------------------------------------------------------------

|LangLocaleGeneralPage| で文書の既定言語とロケール [#1]_ を設定する。

.. rubric:: Language of

:guilabel:`&User interface`
   メニュー、ウィンドウ、ヘルプファイルなどの |UI| に使用する言語を選択する。追
   加言語パックがインストールされているか、多言語版 LibreOffice がインストールさ
   れている必要がある。

   `Default` 項目は計算機の OS が使用する |UI| 言語だ。この言語が LibreOffice の
   インストールにない場合、LibreOffice のインストール言語が既定の言語だ。

   .. admonition:: 利用者ノート

      本ノートで何度かつづったように、ここは `English (USA)` 一択だ。

.. rubric:: Formats

:guilabel:`&Locale setting`
   国設定のロケール設定を指定する。数値、通貨、度量衡単位の設定に影響する。

   `Default` 項目は OS で使用されるロケールだ。この欄の変更は即座に適用される。
:guilabel:`&Default currency`
   通貨書式と通貨欄で使用する既定通貨を指定する。ロケールの設定が変更されると、
   既定の通貨は自動的に変化する。

   `Default` 項目は選択されているロケール設定によって割り当てられている通貨書式
   に適用される。既定通貨を変更すると、開いているすべての文書が変化する。また、
   通貨書式を使用するダイアログボックスや図像も変化する。
:guilabel:`Decimal separator &key`
   :guilabel:`&Same as locale setting` がオンならば、数字パッドのそれぞれのキー
   が押されると、計算機システムで設定されている小数点区切りキーが使用される。オ
   フの場合はキーボードドライバーソフトウェアで使用されている文字が用いられる。
:guilabel:`Date acceptance &patterns`
   現在のロケールが使用する日付の受け入れパターンを指定する。Calc 表計算や
   Writer 表組の升目入力は、有効な日付として認識される前に、ロケールに依存する日
   付受け入れパターンに一致しなければならない。

   定義された日付受付パターンに対応する数字や文字を升目に入力し、カーソルを升目
   の外に移動する。LibreOffice は自動的にデータ入力を認識し、入力を正しい日付形
   式に変換する。

   当項目の初期パターンはロケール設定によって決まり、これらの初期パターンを変更
   したり、さらにパターンを追加したりすることも可能だ。各パターンを区切るにはセ
   ミコロンを使用しろ。

   .. admonition:: 利用者ノート

      ``Y-M-D`` で通じるか？

.. rubric:: Default Languages for Documents

綴字、類語、分綴に関する言語を指定する。

:guilabel:`&Western`
   欧米アルファベットのスペルチェック機能で使用する言語を指定する（英語というこ
   とになる）。
:guilabel:`As&ian`
   オンにするとアジア言語各種の支援が活動する。たとえば、中国語、日本語、韓国語
   の文字を書くときにオンにすると、|UI| でこれらの言語の支援が活動する。
:guilabel:`Complex &text layout`
   |CTL| のスペルチェックの言語を指定する。本ノートではオフとする。
:guilabel:`&For the current document only`
   オンにすると、既定言語の設定が現在の文書に対してのみ有効にする。

.. rubric:: Enhanced language support

:guilabel:`Ignore s&ystem input language`
   システム入力言語またはキーボードへの変更を無視するかどうかを示す。オンにする
   場合、新しいテキストが入力されると、そのテキストは現在のシステム言語ではな
   く、文書言語または現在の段落に従う。

.. note::

   |XXXXX|

Writing Aids
----------------------------------------------------------------------

.. rubric:: Available Language Modules

LibreOffice にインストールされている言語モジュール一覧。各サブモジュールは複数の
言語で使用可能。モジュール名を選択すると、利用可能なサブモジュールすべてが同時に
活動開始する。モジュール名の選択を解除すると、反対に活動終了する。個々のサブモ
ジュールの活動を切り替えるには |EditButton| をクリックして :guilabel:`Edit
Modules` ダイアログボックスを開く。

.. rubric:: User-defined dictionaries

利用可能な使用者辞書一覧。綴字と分綴に必要な辞書を選択する。

|NewB|
   新しい使用者定義辞書の詳細が追加され、言語が指定される :guilabel:`New
   Dictionary` ダイアログボックスを開く。
:guilabel:`Ed&it...`
   :guilabel:`Edit Custom Dictionary` ダイアログボックスを開き、自作辞書に新しい
   項目を追加したり、既存の項目を編集したりできるようにする。自作辞書が編集され
   ると、ファイルの状態がチェックされる。ファイルが書き込み保護されている場合、
   変更することはできない。

.. rubric:: Options

綴字と分綴に対する選択肢。

Check spelling as you type
   テキスト入力時に単語の綴りが怪しい場合に赤い下線で強調表示する。修正用のコン
   テキストメニューが表示される。
Check grammar as you type
   テキスト入力時に文法的過誤を強調表示する。面白いのでオンにしたい。
Check upper-case words
   綴字検査時に大文字小文字を検査する。
Check words with numbers
   文字だけでなく数字も含む単語を検査する。オフでいいはず。
Check special regions
   綴字検査時に描画テキスト、ヘッダーやフッターのテキスト、表組、テキスト枠など
   の特殊領域を検査する。
Minimal number of characters for hyphenation
   自動分綴に必要な最小文字数。
Characters before line break
   分綴する単語のうち、行末に残さなければならない最小文字数。
Characters after line break
   次の行の先頭に必要なハイフン付き単語の最小文字数。
Hyphenate without inquiry
   手動による分綴に関するプロンプトを表示させない。オフにすると、単語が認識され
   ないときに、ハイフンを入力するための選択肢を含むダイアログボックスが現れる。
Hyphenate special regions
   分綴を脚注、ヘッダー、フッターで行う。
:guilabel:`Edi&t...`
   項目の値を変更するにはまずそれを選択にする。値が必要なものに対してはこのボタ
   ンを押してダイアログボックスを開き、新しい値を入力する。

.. note::

   |XXXXX|

Installing language dictionaries
----------------------------------------------------------------------

LibreOffice を計算機にインストールすると、言語モジュールがいくつか自動的にインス
トールされる。 各言語モジュールには、綴字辞書、分綴辞書、類語辞典の最大三つのサ
ブモジュールを含めることがでる。これらの言語モジュールは LibreOffice では辞書と
通常呼ばれている。

追加の辞書は拡張機能としてインストール可能だ。別の言語辞書を追加する例：

#. |MenuBar| :menuselection:`&Tools-->&Language-->&More Dictionaries Online...`
   で :guilabel:`Extension: Dictionary` ダイアログボックスを開く。
#. 利用可能な辞書一覧から必要な辞書を選択する。
#. 必要に応じて、選択した辞書の詳細情報を調べるために、Web サイトのリンクをク
   リックする。
#. 必要な辞書の下にある :guilabel:`Install` を押すと辞書が LibreOffice にインス
   トールされる。
#. |Close| を押してダイアログボックスを閉じる。
#. 新しい辞書が LibreOffice に登録されるように、文書がすべて保存され、閉じられて
   いることを確認してから LibreOffice を再起動する。

.. admonition:: 利用者ノート

   辞書が少なくてあてにならない。

Searching in Japanese
----------------------------------------------------------------------

日本語の検索選択肢を定義する。これらのコマンドはアジア言語の支援が有効になってか
らアクセスできる。|LangLocaleGeneralPage| から作動しろ。

|LangLocalJapanesePage| では日本語に対する検索性質を指定可能。

.. rubric:: Treat as equal

検索時に等しいものとして扱う選択肢を指定する。

.. rubric:: Ignore

検索時に無視する文字を指定する。

.. admonition:: 利用者ノート

   |UI| 言語を英語することの唯一の難点が、このページが読みにくいことだ。日本語版
   はこうだ：

   .. figure:: https://pbs.twimg.com/media/GW4Q426XIAAPkLu?format=png&name=900x900
      :align: center
      :alt: LibreOffice Options - Languages and Locales Settings - Searching in Japanese
      :figwidth: 100%
      :target: https://pbs.twimg.com/media/GW4Q426XIAAPkLu?format=png&name=900x900

Asian layout
----------------------------------------------------------------------

アジア言語の支援が動作するようになった後に、アジア言語のテキストの組版の既定設定
を構成する。これらの選択肢を動作させるには、|OptionsDlg|
|LangLocalLangAsianLayoutPage| を開く。アジア言語のレイアウトの性質を指定可能だ。

.. rubric:: Kerning

個々の文字間の文字同士の間隔調整の既定設定を定義する。

:guilabel:`&Western text only`
   欧文テキストにのみ適用する。こちらをオンか？
:guilabel:`Western &text and Asian punctuation`
   欧米テキストとアジアの句読点の両方に文字同士の間隔調整を適用する。

.. rubric:: Character Spacing

アジアテキスト、升目、図面物の文字間隔の既定設定を定義する。

:guilabel:`&No compression`
   詰めない。
:guilabel:`&Compress only punctuation`
   句読点のみを詰める。
:guilabel:`Compress punctuation and Japanese Kana`
   句読点と日本語のカナを詰める。

.. rubric:: First and Last Characters

:guilabel:`&Language`
   最初と最後の文字を定義する言語を指定する。当然 `Japanese` を選択する。
:guilabel:`&Default`
   オンにすると選択言語の既定文字が次の二つの欄に入力される。
:guilabel:`Not &at start of line`
   行頭に単独で出現しない文字を指定する。ここで入力された文字が改行後の行頭に位
   置する場合、その文字は自動的に前の行の行末に移動する。例えば、文末の感嘆符が
   この欄に含まれれている場合、この記号が行頭に表示されることはない。
:guilabel:`Not at &end of line`
   行末に単独で出現しない文字を指定する。ここで入力された文字が改行によって行末
   に位置する場合、その文字は自動的に次の行の先頭に移動する。例えば、金額の前に
   表示される通貨記号がこの欄にある場合、この記号が行末に表示されることはない。

.. admonition:: 利用者ノート

   最後の二つの記号の羅列パターンを VS Code のエディター設定に流用できるか？

Complex Text Layout
----------------------------------------------------------------------

現在、LibreOffice はヒンディー語、タイ語、ヘブライ語、アラビア語を |CTL| 言語と
して支援している。

右から左へのテキストフローが選択されている場合でも、埋め込まれた欧文テキストは左
から右に流れる。キャレットは矢印キーに反応する。|ArrowR| と |ArrowL| はキャレッ
トをテキスト終端方向と始端方向へそれぞれ移動させる。

.. admonition:: 読者ノート

   本節のノートは割愛する。

Language tool server
----------------------------------------------------------------------

|LangLocalLangToolServerPage| で LibreOffice で利用可能な言語ツール補助を使用す
るには、:guilabel:`Enable Language Tool` をオンにする。必要に応じて、リンク
<https://languagetool.org/legal/privacy> をクリックして何かを操作する。

English sentence checking
----------------------------------------------------------------------

|LangLocalEnglishSentencePage| では文書で使用されている言語を検査するための選択
肢を選択できる。

----

.. rubric:: 章末注

.. [#1] ロケールという術語の定義は難しい。
