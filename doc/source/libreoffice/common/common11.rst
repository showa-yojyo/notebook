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

.. code:: basic

   Sub HelloMacro
       Print "Hello"
   End Sub

マクロを含むライブラリーを作成する手順：

.. |BasicMacrosDlg| replace:: :guilabel:`BASIC Macros` ダイアログボックス
.. |BasicMacroOrgDlg| replace:: :guilabel:`Basic Macro Organizer` ダイアログボックス
.. |MacroToolbar| replace:: :guilabel:`Macro` ツールバー
.. |MacrosBasicM| replace:: :menuselection:`&Tools-->&Macros-->&Organize Macros-->&Basic...`
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

Recording a macro
----------------------------------------------------------------------

LibreOffice でマクロを記録するとき、実際にはプログラミング言語を使用して、特定の
タスクを実行するために必要な手順を記録する。たとえば、文書に同じ情報を繰り返し入
力する必要がある場合、その都度手でコピー＆ペーストしなくても、自動的に情報を入力
するマクロを作成すればいい。

.. note::

   Writer の場合は AutoText 機能の使用も検討しろ。

|OptionsDlg| |LibreOfficeAdvancedPage| を開き、:guilabel:`Enable macro recording
(may be limited)` をオンにしてマクロ記録を動作するようにする。

#. マクロの記録を開始するには、:menuselection:`&Tools-->&Macros-->&Record Macro`
   を選択する。マクロ記録中であることを示す小さなダイアログボックスが現れる。
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

#. :menuselection:`Tools-->Macros-->Run Macro` でマクロ選択ダイアログを開く。
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

----

.. rubric:: 章末注
