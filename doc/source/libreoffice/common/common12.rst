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

.. note::

   一部の選択肢は一度編集するとリセット不可能だ。手動で変更を戻すか、|CancelB|
   を押して |OptionsDlg| を開き直せ。

----

.. rubric:: 章末注
