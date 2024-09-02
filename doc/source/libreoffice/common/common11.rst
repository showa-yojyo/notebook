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

Adding a macro
----------------------------------------------------------------------

ここでは、本やインターネットで見つけた既存のマクロを使用することを想定している。
マクロを手に入れたら、そのマクロを含むライブラリーとモジュールを作成する。

.. todo:: LINK

.. sourcecode:: basic

   Sub HelloMacro
       Print "Hello"
   End Sub

マクロを含むライブラリーを作成する手順：

.. |BasicMacrosDlg| replace:: :guilabel:`BASIC Macros` ダイアログボックス
.. |BasicMacroOrgDlg| replace:: :guilabel:`Basic Macro Organizer` ダイアログボックス
.. |MacroToolbar| replace:: :guilabel:`Macro` ツールバー
.. |MacrosBasicM| replace:: :menuselection:`&Tools-->&Macros-->&Organize Macros-->&Basic...`
.. |MacrosRunM| replace:: :menuselection:`&Tools-->&Macros-->R&un Macro...`
.. |MacrosRecordM| replace:: :menuselection:`&Tools-->&Macros-->&Record Macro`
.. |EditB| replace:: :guilabel:`&Edit` ボタン
.. |RunB| replace:: :guilabel:`&Run` ボタン
.. |RunI| replace:: :guilabel:`&Run` 図像

#. LibreOffice アプリケーションを何か開く。
#. |MenuBar| |MacrosBasicM| を選択する。
#. :guilabel:`&Organizer` ボタンを押す。|BasicMacroOrgDlg| で
   :guilabel:`Libraries` タブを開く。
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

----

.. rubric:: 章末注
