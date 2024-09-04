======================================================================
Chapter 11, Getting Started with Macros ノート
======================================================================

.. include:: ./common-inc.txt

.. contents:: 章見出し
   :depth: 2
   :local:

Introduction
======================================================================

LibreOffice におけるマクロの意義は MS Office と同じようだ。

マクロを作成する最も簡単な方法は、オープンソースの LibreOffice Basic スクリプト
言語を使用して LibreOffice の |UI| で一連の操作を記録することだ。これらのマクロ
は、組み込みの LibreOffice Basic Integrated Development Environment (IDE) を使用
して、記録後に編集および拡張することが可能だ。

LibreOffice で最も強力なマクロは、スクリプト言語：

* LibreOffice Basic
* Python
* JavaScript
* BeanShell

のいずれかを使用して作成する。この章では既定のマクロスクリプト言語である
LibreOffice Basic を中心にマクロ機能の概要を説明する。残りのスクリプト言語につい
ては、入門的な例をいくつか含むのみ。

Your first macros
======================================================================

.. _common11-anchor-B:

Adding a macro
----------------------------------------------------------------------

ここでは、本やインターネットで見つけた既存のマクロを使用することを想定している。
マクロを手に入れたら、そのマクロを含むライブラリーとモジュールを作成する。その構
成については :ref:`common11-anchor-D` を見ろ。

.. sourcecode:: vbnet

   Sub HelloMacro
       Print "Hello"
   End Sub

マクロを含むライブラリーを作成する手順：

.. |BasicMacrosDlg| replace:: :guilabel:`BASIC Macros` ダイアログボックス
.. |BasicMacroOrgDlg| replace:: :guilabel:`Basic Macro Organizer` ダイアログボックス
.. |MacroSelectorDlg| replace:: :guilabel:`Macro Selector` ダイアログボックス
.. |MacroToolbar| replace:: :guilabel:`Macro` ツールバー
.. |MacrosBasicM| replace:: :menuselection:`&Tools-->&Macros-->&Organize Macros-->&Basic...`
.. |MacrosRunM| replace:: :menuselection:`&Tools-->&Macros-->R&un Macro...`
.. |MacrosRecordM| replace:: :menuselection:`&Tools-->&Macros-->&Record Macro`
.. |EditB| replace:: :guilabel:`&Edit` ボタン
.. |OrganizerB| replace:: :guilabel:`&Organizer` ボタン
.. |RunB| replace:: :guilabel:`&Run` ボタン
.. |RunI| replace:: :guilabel:`&Run` 図像
.. |LibrariesTab| replace:: :guilabel:`Libraries` タブ

#. LibreOffice アプリケーションを何か開く。
#. |MenuBar| |MacrosBasicM| を選択する。
#. |OrganizerB| を押す。|BasicMacroOrgDlg| で |LibrariesTab| を開く。
#. :guilabel:`L&ocation` を既定の場所である `My Macros & Dialogs` に設定する。
#. |NewB| を押す :guilabel:`New Library` ダイアログボックスが開く。
#. ライブラリー名を記入して |OK| を押す。ここでは `TestLibrary` とする。
#. |BasicMacroOrgDlg| に戻ったら :guilabel:`Modules` タブを開く。
#. Module 一覧で `My Macros` を展開し、ライブラリー `TestLibrary` を選択する。
   `Module1` というモジュールがすでに存在し、マクロを含めることができる。必要で
   あれば |NewB| を押して、ライブラリーに別のモジュールを作成可能。
#. `Module1` 選択し、|EditB| を押して IDE を開く。これを使ってマクロの作成、編
   集、実行、デバッグを行う。
#. 新しいモジュールが作成されると、コメントと ``Main`` という空のマクロが含まれ
   ている。
#. 新しいマクロを ``Sub Main`` の前か ``End Sub`` の後に追加する。

   .. tip::

      ``Main`` サブルーチンを削ってもかまわない。

#. （随意）マクロが期待どおりに記述されているかどうかを確認するには、
   |MacroToolbar| :guilabel:`Compile` 図像をクリックする。
#. :guilabel:`Object Catalog` ウィンドウの :menuselection:`TestLibrary-->Module
   1` で `HelloMacro` サブルーチンをダブルクリックし、

   * |MacroToolbar| |RunI| をクリックするか、
   * |F5| を押して、

   モジュール内の `HelloMacro` サブルーチンを実行する。
#. |OK| を押して結果を閉じる。
#. モジュール内の任意のマクロを選択して実行するには、

   * |StandardToolbar| :guilabel:`Select Macro` 図像をクリックするか、
   * :menuselection:`&Tools-->&Organize Macros-->&Basic...` に進む。
#. マクロを選択し、|RunB| を押す。

.. _common11-anchor-A:

Recording a macro
----------------------------------------------------------------------

LibreOffice でマクロを記録するとき、実際にはプログラミング言語を使用して、特定の
作業を実行するために必要な手順を記録する。たとえば、文書に同じ情報を繰り返し入力
する必要がある場合、その都度手でコピー＆ペーストしなくても、自動的に情報を入力す
るマクロを作成すればいい。

.. note::

   Writer の場合は AutoText 機能の使用も検討しろ。

|OptionsDlg| |LibreOfficeAdvancedPage| を開き、:guilabel:`Enable macro recording
(may be limited)` をオンにしてマクロ記録を動作するようにする。

#. マクロの記録を開始するには、|MacrosRecordM| を選択する。マクロ記録中であるこ
   とを示す小さなダイアログボックスが現れる。
#. マクロ実行時になったら入力したいテキストを文書に入力する
#. ミニダイアログの Stop Recording を押す。これにより |BasicMacrosDlg| が開く。
#. `My Macros` を開く。
#. :menuselection:`My Macros-->Standard`
#. `Standard` ライブラリーを選択し、マクロを保存する既存のモジュールを選択する。
#. :guilabel:`Macro Name` を入力する。この説明では `EntryMyName` とする。
#. |SaveB| を押してマクロを保存し、|BasicMacrosDlg| を閉じる。

上記のすべての手順を実行すると、選択したモジュール内に `EnterMyName` というマク
ロが作成される。

Running a macro
----------------------------------------------------------------------

#. |MacrosRunM| でマクロ選択ダイアログを開く。
#. 例えば、新しく作成したマクロ `EnterMyName` を選択し、|RunB| を押す。
#. または、|MacrosBasicM| で |BasicMacrosDlg| を開き、マクロを選択して |RunB| を
   押す。

.. _common11-anchor-C:

Viewing and editing macros
----------------------------------------------------------------------

作成したマクロを表示、編集するには：

#. |MacrosBasicM| で |BasicMacrosDlg| を開く。
#. 新しいマクロ `EnterMyName` を選択し |EditB| を押す。IDE が開き、マクロコード
   が表示される。

Commenting with REM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basic マクロコードのコメントは ``REM`` や単引用符から始まり行末で終わる。

Defining subroutines with SUB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

個々のマクロはサブルーチンに格納される。サブルーチンはキーワード ``SUB`` で始ま
り、終わりは ``END SUB`` で示される。

* 引数を取るサブルーチンを書くことができる。これはサブルーチンをゼロから作成する
  場合にのみ可能だ。LibreOffice に記録されたマクロは引数を受け付けない。
* サブルーチンのもう一つの種類は関数と呼ばれるもので、これは処理の結果として値を
  返すサブルーチンだ。関数は先頭に ``FUNCTION`` というキーワードをつけて定義す
  る。LibreOffice に記録されたマクロはサブルーチンのみを定義する。

Defining variables using DIM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

変数を定義するときは ``DIM`` キーワードを使用する。

`EnterMyName` マクロでは、変数 ``document`` と ``dispatcher`` は ``object`` 型と
して定義されている。その他の一般的な変数型には文字列、整数、日付がある。配列型の
変数は一つの変数に値を複数格納することができる。配列は通常ゼロから始まる。

Explaining macro code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

割愛。ここに何かを綴るよりは本書を直接当たるほうがいい。

Creating a macro
======================================================================

マクロを作成する場合、記録する前に次を思うことが重要だ：

* 作業を単純なコマンドセットとして書けるか。
* マクロの最終コマンドで、カーソルが次のコマンドに対応できる状態になるようにス
  テップを配置できるか。あるいは、使用者が対象文書のテキストやデータ入力に戻れる
  ようにできるか。

A more complex example of a macro
----------------------------------------------------------------------

ある一般的なマクロ作業は、Web サイトからデータの行と列をコピーし、テキスト文書で
表として整形することだ。通常、このマクロは次のように動作する：

#. Web サイトからデータをクリップボードにコピーする。
#. おかしな書式や書体を避けるため、書式なしのテキストとして Writer 文書に貼り付
   ける。
#. :menuselection:`T&able-->&Convert-->&Text to Table...` を使えるように、列間に
   タブを入れてテキストを再整形する。

上記の二つの問いを念頭に置いて、テキストを検査し、整形するマクロを記録できること
を確認する。コピーされたデータの例として、Web 上のどこかにある FontWeight 定数を
説明するテキストを考える。この例の最初の列は定数名を示し、それぞれの後には空白と
タブが続き、各行の末尾には二つの空白がある。

.. sourcecode:: text
   :caption: 実際には間にタブ文字があったり行末に空白文字があったりする

   DONTKNOW       The font weight is not specified/known.
   THIN           specifies a 50% font weight.
   ULTRALIGHT     specifies a 60% font weight.
   LIGHT          specifies a 75% font weight.
   SEMILIGHT      specifies a 90% font weight.
   NORMAL         specifies a normal font weight.
   SEMIBOLD       specifies a 110% font weight.
   BOLD           specifies a 150% font weight.
   ULTRABOLD      specifies a 175% font weight.
   BLACK          specifies a 200% font weight.

この例では、表の一列目に書体の太さの数値を、二列目に定数名を、三列目にテキストの
説明を記録する。この作業はある行を除けば簡単に達成する。以下は、カーソルがテキス
ト ``THIN`` から始まる行の先頭にあると仮定して、キーストロークを使用してこのマク
ロを記録する手順だ。

#. マクロ記録が作動する状態であることを確認する。
#. |MacrosRecordM| 選択。マクロ記録開始。
#. キーボードのみで先ほどのテキストを編集する。細かい記述は割愛。
#. マクロの記録を停止し、マクロを保存する。:ref:`common11-anchor-A` を見ろ。

マクロを実際に記録するよりも、これらの手順を読んで書く方がはるかに時間がかかる。

このマクロを実行するには、記録されたステップを適用したい行の先頭にカーソルを置
く。次に |MacrosRunM| を選択し、`CopyNumToCol1` マクロを選択して |RunB| を押す。

.. admonition:: 読者ノート

   生成されたコードをよく観察すると、キーバインドに対応するコマンドがそのまま記
   述されていることがわかる。|Ctrl| + |ArrowR| を押す、ではなく、GoToNextWord を
   実行する、のような表現だ。

上記の手順は、マクロ作成時に想定した書式に一行目が従っている場合にのみ正しく機能
することに注意。このマクロを ``DONTKNOW`` や ``NORMAL`` の行で実行すると、これら
の行は書式が異なるので、結果は期待どおりにはならない。

Running a macro quickly
----------------------------------------------------------------------

|MacrosRunM| でマクロを繰り返し実行するのは不便なので、キーバインドを割り当て
て、マクロを素速く起動する。`CopyNumToCol1` マクロに |Ctrl+K| を割り当てる手順：

#. |CustomizeM| を選択して |CustomizeDlg| を開く。
#. :guilabel:`Keyboard` タブを開く。
#. 下側を適当に選択して `CopyNumToCol1` マクロを選択する。
#. 上側からキーバインド |Ctrl+K| を選択して `CopyNumToCol1` マクロに割り当てるの
   に :guilabel:`&Assign` ボタンを押す。

Limitations of the macro recorder
======================================================================

Macro Recorder には記録できない動作がある。この制限がどこから生じるのかを見てい
く。

Understanding the dispatch framework
----------------------------------------------------------------------

例えば |MenuBar| :menuselection:`&File-->&Save` 選択やキーバインド |Ctrl+S| や
|StandardToolbar| :guilabel:`Save` 図像クリックは、それらが「ファイルを保存する
コマンド」を何かに発送する。コマンドが処理可能な何かにまで到着すると、ファイル保
存が実際に実行される。

発送コマンドはテキストであり、例えば ``.uno:GoToStartOfLine`` のようなものだ。

How the macro recorder uses the dispatch framework
----------------------------------------------------------------------

Macro Recorder は発送フレームワークが生成するコマンドしか登録しないが、そのよう
なコマンドがすべて完了するというわけでもない。たとえば、物体を入れると次のような
コードが生成される：

.. sourcecode:: vbnet

   dispatcher.executeDispatch(document, ".uno:InsertObject", "", 0, Array())

どのような物体を作成するかを指定することは不可能だ。物体をファイルから入れる場
合、どのファイルを入れるかを指定できない。マクロの記録中に |OptionsDlg| を使用し
て設定項目を開いて変更した場合、生成されたマクロは設定の変更を記録しない（コメン
トアウトされたコード片が生じる）。

ダイアログボックスを何か開くとコマンドは生成するが、ダイアログボックス内で行われ
た作業は通常記録されない。Macro Recorder が何を捉えることができるかは、試してみ
るまでわからない（例えば、検索ダイアログボックスからの動作は適切に捉えられる）。

Other options
----------------------------------------------------------------------

Macro Recorder を使っても解決できない問題があるときに、LibreOffice 物体を使用し
て実際のコードを記述する。LibreOffice 物体を学ぶのはたいへんだ。

.. _common11-anchor-D:

Macro organization
======================================================================

LibreOffice では「マクロ ⊂ モジュール ⊂ ライブラリー ⊂ コンテナー」という構造を
とる。モジュールは通常、使用者との対話や計算などの機能を分割する。個々のマクロは
サブルーチンや関数だ。

|MacrosBasicM| を選択し、|BasicMacrosDlg| を開く。利用可能なコンテナーはすべて
:guilabel:`Macro From` 一覧に表示され、文書はそれぞれライブラリーを複数含むこと
ができるコンテナーだ。アプリケーション自体が二つのコンテナーとして機能する。一つ
は LibreOffice とともに配布されるマクロ用のコンテナーで `LibreOffice Macros` と
呼ばれ、もう一つは個人用マクロ用のコンテナーで `My Macros` と呼ばれる。

`LibreOffice Macros` はアプリケーション実行時コードと一緒に保存され、基本、編集
不可だ。`LibreOffice Macros` コンテナーには独自のマクロを保存してはいけない。

マクロが単一の文書にしか適用されない場合を除き、マクロは `My Macros` コンテナー
に格納される。`My Macros` コンテナーは使用者領域またはホームディレクトリーに保存
される。

.. admonition:: 利用者ノート

   Windows ならば ``APPDATA`` とか ``USERPROFILE`` だ。

マクロが文書に含まれている場合、記録されたマクロはその文書上で動作しようとする。
というのも、その動作には主に ``ThisComponent`` を使用しているからだ。

すべてのコンテナーは `Standard` という名前のライブラリーを含む。`Standard` ライ
ブラリーを使用する代わりに、意味のある名前を持つ独自のライブラリーを作成するのが
良い。`Standard` とは異なり、独自のライブラリーを他のコンテナーにインポートする
ことが可能だ。

.. caution::

   LibreOffice では、ライブラリーをコンテナーにインポートすることは可能だが、
   `Standard` という名前のライブラリーを上書きすることはできない。そのため、
   `Standard` ライブラリーにマクロを保存すると、そのマクロを別のコンテナーにイン
   ポートできなくなる。

モジュールにも意味のある名前をなるべくつけろ。

`My Macros` という名前のコンテナーに保存されたマクロはすべての文書で使用可能だ。
文書にマクロを保存するのは、文書が共有され、マクロを文書に含めたい場合に便利だ。

`Standard` ライブラリーと `Template` ライブラリーは自動的にロードされるが、その
他のライブラリーマクロは、それらを含むライブラリーがロードされるまで使用可能にな
らない。ロードされたライブラリーはロードされていないそれとは表示が異なる。ライブ
ラリーとそれに含まれるモジュールをロードするには、ライブラリーをダブルクリックす
る。

.. _common11-anchor-E:

Where are macros stored?
----------------------------------------------------------------------

LibreOffice は、使用者固有のデータをホームディレクトリー内のフォルダーに保存する。
設定データの保存場所を確認するには、|OptionsDlg| |PathsPage| を開く。Basic で記
述された使用者マクロは :file:`LibreOffice/4/user/basic` に保存される。

Exporting macros
----------------------------------------------------------------------

マクロライブラリーをエクスポートして、再利用したり他の人と共有したりしたい場合は
LibreOffice Basic Macro Organizer を用いる。

#. |MacrosBasicM| を選択し、|OrganizerB| を押す。
#. |LibrariesTab| をクリックし、エクスポートしたいライブラリーを選択する。
#. :guilabel:`&Export...` ボタンを押し、:guilabel:`Export &as BASIC Library` を
   選択する。
#. ライブラリーの保存先を選択し、|Save| を押す。

ライブラリーがエクスポートされると、LibreOffice はライブラリーに関連するすべての
ファイルを含むフォルダーを作成する。

.. admonition:: 読者ノート

   拡張子 .xlb, .xba を持つファイルがある。

Importing macros
----------------------------------------------------------------------

|BasicMacroOrgDlg| ではマクロライブラリーを文書にインポートしたり、ライブラリー、
モジュール、ダイアログボックスの作成、削除、名前の変更が行える。

#. |LibrariesTab| で使用するコンテナーを選択し、:guilabel:`&Import...` ボタンを
   押してマクロライブラリーをインポートする。
#. インポートするライブラリーのあるフォルダーに移動する。:file:`dialog.xlb` と
   :file:`script.xlb` のどちらかを選択できる。どちらのファイルを選択しても、マク
   ロをインポートできる。文書に含まれるライブラリーをインポートするには文書ファ
   イルを選択する。
#. ファイルを選択し、|Open| を押して続行し、:guilabel:`Import Libraries` ダイア
   ログボックスを開く。
#. ライブラリーをインポートするための選択肢を選択する。
#. |OK| を押すと選択したマクロライブラリーがインポートされる。

Downloading macros to import
----------------------------------------------------------------------

LibreOffice 社会が作成したマクロをインターネット上で見つけることができる。マクロ
には、文書に含まれているもの、通常のファイルとしてインポートする必要があるもの、
テキストとして公開されていて Basic IDE にコピー＆ペーストする必要があるものがあ
ります。マクロをライブラリーに追加する方法については :ref:`common11-anchor-B` を、
Basic IDE を使用してマクロを編集する方法については :ref:`common11-anchor-C` をそ
れぞれ見ろ。

* <https://www.pitonyak.org/oo.php>
* <https://www.pitonyak.org/database/>
* <https://wiki.documentfoundation.org/Macros>
* <https://forum.openoffice.org/en/forum/>

How to run a macro
======================================================================

マクロを |MacrosRunM| で実行するのは、マクロを頻繁に使用する場合は効率的ではない。
マクロにキーバインドを割り当てることもできるが、ツールバー図像、メニュー項目、
イベント、文書埋め込みボタンにマクロを接続することも可能だ。どの方法を採用するか
を決めるのに、次のような質問をするのもよい：

* マクロは一つの文書だけで利用できるようにすべきか、それともすべての文書で利用で
  きるようにしたいか？
* マクロは Calc 文書など特定の文書型用か？
* マクロの使用頻度は？

その答えによって、マクロの保存場所と実行形態が決まる。例えば、めったに使わないマ
クロをツールバーに追加することはないだろう。選択肢を決めるのに、次の判断基準表を
検討するといい（興味深いのでそのまま引用する）：

.. list-table:: Where to store a macro
   :align: left
   :header-rows: 1
   :stub-columns: 1
   :widths: auto

   * - 格納場所
     - 全ソフト
     - 特定ソフト
     - 文書専用
   * - ツールバー
     - No
     - Yes
     - Yes
   * - メニュー
     - No
     - Yes
     - Yes
   * - キーバインド
     - Yes
     - Yes
     - No
   * - イベント
     - Yes
     - No
     - Yes

Toolbars, menu items, and keyboard shortcuts
----------------------------------------------------------------------

|CustomizeDlg| を使ってメニュー、キーバインド、ツールバーを改造する。このダイア
ログボックスを開くには |CustomizeM| を選択する。詳しくは :doc:`common13` を見ろ。

Events
----------------------------------------------------------------------

LibreOffice では、たとえば、文書を開く、変更された状態が変化する、マウスカーソル
を移動するなどはすべてイベントだ。イベントを引き金としてマクロを実行し得る。マク
ロはイベントハンドラーと呼ばれる。

.. caution::

   イベントハンドラーを設定する際には注意が必要だ。たとえば、文書が変更されるた
   びに呼び出されるイベントハンドラーを書くときに、そのイベントが正しく処理され
   ないと、問題が発生し得る。その結果、イベントハンドラーが LibreOffice を強制終
   了させる可能性がある。

#. |CustomizeDlg| を開き |EventsTab| を選択する。このダイアログボックスのイベン
   トはアプリケーション全体と特定の文書に関連するものだ。
#. :guilabel:`&Save in` ドロップダウンで、`LibreOffice` または特定の文書を選択
   し、イベントを保存する。
#. 一般的な使用方法は、特定のマクロを呼び出すために文書を開くイベントを割り当て
   るものだ。マクロは文書の特定の準備作業を実行する。必要なイベントを選択し、
   :guilabel:`M&acro...` ボタンを押して |MacroSelectorDlg| を開く。
#. 必要なマクロを選択し、|OK| を押してマクロをイベントに割り当てる。イベントがマ
   クロに割り当てられたことが |EventsTab| に表示される。

文書内の多くの物体はイベント発生時にマクロを呼び出すように設定できる。最も一般的
な使い方は、ボタンなどのコントロールを文書に追加することだ。図版をダブルクリック
しても、:guilabel:`Macros` タブのあるダイアログボックスが開き、イベントにマクロ
を割り当てることが可能だ。

Using extensions
======================================================================

拡張とは、LibreOffice にインストールして新しい機能を追加するコードのことだ。拡張
はほとんどのプログラミング言語で記述でき、単純なものから洗練されたものまである。
拡張は次のような型に分類される：

* Calc アドイン。Calc に新しい機能を搭載するもので、通常の組み込み関数のように動
  作する新しい関数を含む。
* 新しい部品と機能。通常、新しいメニューやツールバーなど、ある程度の |UI| 統合を
  含む。
* 新しい統計図表型の図表アドイン。
* 綴字検査などの言語部品。
* 文書雛形と画像。

個々の拡張はいろいろな場所にあるが、現在、拡張の保管庫と文書は
<https://extensions.libreoffice.org/> と
<https://libreplanet.org/wiki/Group:OpenOfficeExtensions/List> にそれぞれある。
拡張の入手とインストールの詳細については :doc:`common13` を見ろ。

Writing macros without the recorder
======================================================================

LibreOffice を構成する物体に直接入出するコードでマクロを書くことも可能だ。つ
まり、より高度なプログラミング論理を用いて、文書を直接操作するマクロを作成するこ
とが可能だ。

LibreOffice の内部物体を直接操作することは、この章を超える高度な論題だ。それで
も、これがどのように機能するかを簡単な例で説明する。

An example of a macro in code for Writer
----------------------------------------------------------------------

Writer 文書の末尾に文字列 Hello を追加するマクロを、記録なしで作成した簡単
なコードをライブラリーに追加する手順：

#. |MacrosBasicM| を選択。
#. `My Macros` でマクロを作成したいライブラリーに移動する。ここでは
   `TestLibrary` とする。
#. ライブラリーですでに利用可能なモジュールの一つを選択する。新しいモジュールを
   作成したい場合は、|OrganizerB| を押し、新しいモジュールを追加する。
#. モジュールを選択した状態で |EditB| を押す。Basic IDE ウィンドウが開き、選択し
   たモジュールに実装されているマクロのコードが表示される。
#. コードをモジュールに入力する。

.. admonition:: 利用者ノート

   Basic コードの編集は IDE はもちろん、Visual Studio Code でさえ快適に行うこと
   は期待できない。たとえば自動字下げ機能がすぐに見つけられない。

An example of a macro in code for Calc
----------------------------------------------------------------------

LibreOffice Calc の機能を拡張する強力な方法の一つは、繰り返し作業を自動化するマ
クロを作成することだ。単純な升目処理や書式設定から高度なデータ操作まで、さまざま
な作業を実行するマクロを記述できる。

本書のコード例は升目範囲を分析して、すべての値が 0 から 100 の間かどうかを判断す
る。50 から 100 までは薄緑色で、0 から 50 までは薄赤色で升目をマークする。範囲外
の値が見つかった場合は、警告を表示し薄い灰色でマークする。

.. Listing 6: Calc macro to format ranges based on values

マクロをライブラリーに追加手順は前節と同様。このマクロを実行するには、まず新しい
Calc シートを作成し、升目範囲に数値を追加する。

The ScriptForge library
======================================================================

ScriptForge ライブラリーは一連のサービスで構成されており、各サービスは特定の主題
に関連するメソッドやプロパティーを与える。たとえば、Dialog サービスではスクリプ
トモジュールで利用可能なダイアログボックスに入出でき、Database サービスでは
Base 文書でSQL コマンドを実行できる。

既存の Calc 文書を開き、`NewSheet` という名前の新しいシートを作成して、升目 A1
に文字列 Hello を入れるマクロを ScriptForge ライブラリーを使用して Basic で記述し
たコードだ。

.. sourcecode:: vbnet
   :caption: ScriptForge ライブラリーを使うマクロ例

   Sub CreateSheetExample
       GlobalScope.BasicLibraries.LoadLibrary("ScriptForge")
       Dim ui as Object, myDoc as Object
       ui = CreateScriptService("UI")

       Set myDoc = ui.OpenDocument("/home/user/Documents/myfile.ods")
       myDoc.InsertSheet("NewSheet")
       myDoc.SetValue("NewSheet.A1", "Hello")
       myDoc.Activate("NewSheet")
       myDoc.Save()
       myDoc.CloseDocument()
   End Sub

.. admonition:: 読者ノート

   試すときにはファイルパスを既存のものに変える必要がある。保存メソッドか閉じる
   メソッドをコメントアウトしておくとよい。

UNO Object Inspector
======================================================================

LibreOffice にはアプリケーションのほぼすべての側面を自動化するために使用できる広
範な |API| がある。LibreOffice で使用される部品モデルは |UNO| として知られてい
る。

スクリプト言語の LibreOffice マクロは |UNO| |API| を使用する。XSCRIPTCONTEXT イ
ンターフェイスを LibreOffice Basic, Python, JavaScript, BeanShell のマクロスクリ
プトに与え、文書に対して動作を実行するために必要なさまざまなインターフェイスへの
入出手段を設けている。

.. admonition:: 読者ノート

   XSCRIPTCONTEXT とは？

.. |Inspector| replace:: :guilabel:`UNO Object Inspector`

|Inspector| はマクロ開発者が物体を検査し、物体への入出方法を学習し、マクロで
使用するのに役立つ。この機能は Writer, Calc, Impress, Drawで利用できる。この機能
を有効にするには |MenuBar| :menuselection:`&Tool-->Develo&pment Tool` を選択す
る。

ウィンドウ左側には |DOM| 補助装置があり、文書内の物体すべてを探索できる。物体を
選択すると、それに関する情報がウィンドウの右側に表示される：

:guilabel:`Interfaces`
   実装されているインターフェイスすべての名前
:guilabel:`Services`
   物体が支援する工作すべての名前
:guilabel:`Properties`
   物体で利用可能な性質すべての名前と型
:guilabel:`Methods`
   物体が呼び出すことができるメソッドすべての名前、引数、戻り値の型

.. |CurSelB| replace:: :guilabel:`Current Selection`

|DOM| 補助装置を使って物体を検査する代わりに |CurSelB| を切り替えることで、文書内
で現在選択されている物体を直接検査することもある。

例えば、Writer 文書で選択テキストの背景色を変更したいとする。テキストの一部を選
択し、|Inspector| を開いて |CurSelB| を切り替え、目的の効果に一致する性質を探し
て物体の性質を調べることができる（この例では ``CharBackColor`` を見つけたい）。

この性質を使用して、選択テキストの背景色を変更するマクロを書くことができる。

Overview of Python, BeanShell, and JavaScript macros
======================================================================

LibreOffice では、馴染みのある言語で書かれたマクロを支援している。Python,
BeanShell, JavaScript だ。

マクロは、スクリプト言語すべてで同じように構成されている。`LibreOffice Macros`
コンテナーには LibreOffice のインストール時に用意されているマクロがすべて格納さ
れる。

`My Macros` コンテナーには LibreOffice 文書で使用できるようにしたマクロが格納さ
れる。各文書には他の文書では使用できないマクロを含めることもできる。

記録機能を使用する場合、マクロは LibreOffice Basic で作成される。その他のスクリ
プト言語を使用するには、自分でコードを記述する必要がある。

|MacrosRunM| を使用してマクロの実行を選択すると、|MacroSelectorDlg| が現れる。こ
こで利用可能な言語で書かれたマクロを選択して実行できる。

:guilabel:`&Tools-->&Macro-->&Edit Macros..` を使用してマクロを編集すると
LibreOffice Basic IDE が起動する。このウィンドウでは利用可能な LibreOffice Basic
マクロを選択して編集できるが、他の言語のマクロは選択できない。

.. tip::

   <https://api.libreoffice.org/> を見ろ。

Python macros
----------------------------------------------------------------------

:menuselection:`&Tools-->&Macros-->&Organize Macros-->&Python...` を選択する。

:guilabel:`Python Macros` ダイアログボックスが現れる。Python スクリプトを編集お
よびデバッグする機能は、現在のところ LibreOffice の標準 |UI| に統合されていな
い。任意の Python エディターを使用してスクリプトを作成し、これらのファイルを適切
なフォルダーに配置するのだ。:ref:`common11-anchor-E` を見ろ。

.. tip::

   :abbr:`APSO (Alternative Python Script Organizer)` 拡張機能を使うと Python ス
   クリプトの編集や整理が簡単になる：<https://gitlab.com/jmzambon/apso> を見ろ。

   LibreOffice での Python スクリプトの詳細については、
   <https://wiki.documentfoundation.org/Macros/Python_Basics> を見ろ。

BeanShell macros
----------------------------------------------------------------------

割愛。

JavaScript macros
----------------------------------------------------------------------

:menuselection:`&Tools-->&Macros-->&Organize Macros-->&JavaScript...` を選択す
る。

:guilabel:`JavaScript Macros` ダイアログボックスの |EditB| を押すと Rhino
JavaScript Debugger に出入りできる。この道具の詳しい使い方は
<https://developer.mozilla.org/en-US/docs/Mozilla/Projects/Rhino/Debugger> で見
つかる。

.. admonition:: 読者ノート

   リンクが死んでいて話にならない。

Finding more information
======================================================================

|F1| を押して LibreOffice ヘルプページを開く。LibreOffice ヘルプシステムの左上に
あるヘルプセットを表示するドロップダウンリストから `Basic` を選択する。

.. admonition:: 利用者ノート

   ヘルプが出ない。

Included material
----------------------------------------------------------------------

LibreOffice には多くの優れたマクロが含まれています。

|BasicMacrosDlg| を開いて :menuselection:`Application Macros-->Tools` ライブラ
リーを展開する。`WritedbgInfo` や `printdbgInfo` などの良い例がある。

Online resources
----------------------------------------------------------------------

マクロプログラミングに関する情報資料：

* <https://wiki.documentfoundation.org/Macros>
* <https://ask.libreoffice.org/>
* <https://wiki.documentfoundation.org/Documentation/Other_Documentation_and_Resources>
* <http://forum.openoffice.org/en/forum/>

Printed and ebook materials
----------------------------------------------------------------------

* `OpenOffice.org Macros Explained <https://www.pitonyak.org/OOME_3_0.pdf>`__:
  LibreOffice Basic でも通用する。669 ページの大著。
* <https://www.packtpub.com/openoffice-ooobasic-calc-automation/book>: 表計算なら。
