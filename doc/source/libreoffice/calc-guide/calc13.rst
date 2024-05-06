======================================================================
LibreOffice Calc Chapter 13, Macros ノート
======================================================================

.. include:: ./calc-inc.txt
.. |UNO| replace:: :abbr:`UNO (Universal Network Objects)`

.. contents:: 章見出し
   :local:

Introduction
======================================================================

|Guide| の Chapter Getting Started with Macros の章では LibreOffice で使用できる
マクロ機能を紹介している。この章では、Calc スプレッドシート内でのマクロの使用に
ついてさらなる入門情報を与える。

マクロとは、後で使用するために保存される一連のコマンドやキー操作のことだ。例：開
いているスプレッドシートの現在の升目に自分の住所を入力するマクロ。マクロを使用す
ると、単純なタスクと複雑なタスクの両方を自動化できる。また、Calc に組み込まれて
いない新しい機能を導入することもできる。

マクロを作成する最も簡単な方法は、Calc の UI を通じて一連の操作を記録することだ。
BASIC 言語の方言である LibreOffice Basic スクリプト言語により記録したマクロを保
存する。そして LibreOffice Basic IDE を使用して編集および拡張可能。

マクロを作成する言語としては次の四つのスクリプト言語が対応されている：

* LibreOffice Basic
* Python
* JavaScript
* BeanShell

本章では LibreOffice Basic に焦点を当てる。

On Visual Basic for Applications (VBA) compatibility
======================================================================

LibreOffice Basic 言語と VBA 言語は BASIC の方言だ。MS Excel で書かれたマクロを
LibreOffice で使用したい場合は、まず LibreOffice Basic IDE でコードを編集する必
要がある。

VBA で書かれた Excel マクロを変換するためのコツは本章最後に詳しい。

Using the macro recorder
======================================================================

|Guide| の Getting Started With Macros の章にはマクロレコーダーの使用方法と生成
された LibreOffice Basic スクリプトの理解方法の例が記載されている。以下の手順で
は |Guide| のより詳細な説明を省略して Calc スプレッドシート固有の例を示す。スプ
レッドシートの升目範囲に対して、乗算を伴う特殊な貼り付けを実行するマクロを作成
し、保存する。

.. admonition:: 利用者ノート

   *Getting Started Guide* を先に読んでおいたほうがいいかもしれない。

.. note::

   まず、|OptionsDlg| |LibreOfficeAdvancedPage| でオプション :guilabel:`Enable
   macro recording (may be limited)` をオンにしておけ。

.. |BasicMacrosDlg| replace:: :guilabel:`Basic Macros` ダイアログボックス

#. |MenuBar| の :menuselection:`&File-->&New-->&Spreadsheet` で新しいスプレッド
   シートを作成する。
#. 新しいスプレッドシートの `Sheet1` の 升目 A1:C3 に次の数値を入力する：

   ==  ==  ===
    1   8    9
    2   7   10
    3   6   11
   ==  ==  ===

#. 数値 3 が入っている升目 A3 を選択し、クリップボードにコピーする。
#. 範囲 A1:C3 のすべての升目を選択する。
#. |MenuBar| の :menuselection:`&Tools-->&Macros-->&Record Macro` で開始。テキス
   トエディターにおけるキーボードマクロ開始のようなものだと考えられ
   る。:guilabel:`Record Macro` 小窓が現れる。
#. |MenuBar| の |PasteSpecialM| を選択。|PasteSpecialDlg| が開く。
#. :guilabel:`Paste` 領域で :guilabel:`&All` をオン、:guilabel:`Operations` 領域
   で :guilabel:`Mult&iply` をオンにし |OK| を押す。升目 A1:C3 の値が三倍になる。
#. 小窓内の :guilabel:`Stop Recording` を押して収録終了。|BasicMacrosDlg| の変種
   が開く。

   .. note::

      |BasicMacrosDlg| の :guilabel:`Save Macros In` 領域に既存の LibreOffice
      Basic マクロが見える。このマクロはライブラリーコンテナー、ライブラリー、モ
      ジュール、マクロに階層化されている。各ライブラリーコンテナー名の左側にある
      プラスマイナス図像を使用して、そのコンテナー内のライブラリー、モジュール、
      マクロを見渡せる。

#. :guilabel:`Save Macro In` で現在の文書の登録項目を選択する。この例では現在の
   文書は保存されていないので、既定の名前 `Untitled 1` で参照される。
#. 保存された文書には `Standard` という名前のマクロライブラリーが含まれる。この
   ライブラリーは必要になるまで作成されないので、この手順の例では、この時点で
   は、新しい文書にはライブラリーが含まれていない。
#. :guilabel:`New Mod&ule` ボタンを押す。:guilabel:`New Module` ダイアログボック
   スが開く。新しいモジュールの名前を入力するか、既定の `Module1` のままにする。

   .. note::

      ライブラリー名、モジュール名、マクロ名に使用可能な文字が規定されているので
      注意。一般的なプログラミング言語にありがちな規則だと思っていい。

#. |OK| を押して新しいモジュールを作成する。現在の文書にはマクロライブラリーが存
   在しないため、`Standard` ライブラリーが作成される。
#. |BasicMacrosDlg| の :guilabel:`Save Macro In` 領域で新しく作成したモジュール
   の登録項目を選択し、:guilabel:`Macro Name` ボックスにテキスト `PasteMultiply`
   を入力し、 |Save| を押す。

マクロは `PasteMultiply` という名前で、`Untitled 1` 文書の `Standard` ライブラ
リー内の新しく作成されたモジュールに保存される。

.. note::

   LibreOffice で使用されている部品モデルは |UNO| であり、マクロレコーダーはほと
   んどのコマンドに |UNO| ディスパッチャーを使用している。しかし、この技術的手法
   には問題が二つある。一つはディスパッチが完全に文書化されておらず、変更される
   可能性があることだ。もう一つはマクロの記録中に開かれるダイアログボックスの値
   のいくつかをレコーダーが無視することだ。したがって、複雑なマクロを記録して
   も、実際にはすべてが期待どおりに実行されないことがある。詳細については |Help|
   の索引を検索しろ。

Write your own functions
======================================================================

Create a function macro
----------------------------------------------------------------------

マクロを作成し、関数を呼び出すようにそれを実行することが可能。単純な関数マクロの
定義手順：

.. |MacrosOrganizeBasicM| replace:: :menuselection:`&Tools-->&Macros-->&Organize Macros-->&Basic...`
.. |BasicMacroOrganizerDlg| replace:: :guilabel:`Basic Macro Organizer` ダイアログボックス

#. 新規スプレッドシートを作成し、:file:`CalcTestMacros.ods` という名前で保存し
   て、開いたままにする。
#. |MenuBar| から |MacrosOrganizeBasicM| を選択して |BasicMacrosDlg| を開く。こ
   の状況での |BasicMacrosDlg| の間取りは、:guilabel:`Record Macro` ダイアログ
   ボックスの :guilabel:`Stop Recording` ボタンを押したときのものとは異なることに
   気をつけろ。
#. :guilabel:`Macro From` 領域には、現在開いている LibreOffice 文書に関連するも
   のも含め、利用可能なマクロライブラリーコンテナが一覧される。`My Macros` には
   使用者が作成または LibreOffice に追加したマクロが含まれ、複数の文書で使用可能
   だ。`LibreOffice Macros` には LibreOffice のインストール時に含まれている、変
   更されるべきではないマクロが含まれる。
#. :guilabel:`&Organizer...` を押す。|BasicMacroOrganizerDlg| が開く。

   :guilabel:`Libraries` タブを開く。:guilabel:`L&ocation` ドロップダウンリスト
   で現在文書に合わせる :guilabel:`&Library` 欄の一覧が更新され、空の `Standard`
   ライブラリーの名前が示される。
#. :guilabel:`&New...` を押して :guilabel:`New Library` ダイアログボックスを開
   き、この文書の新規ライブラリーを作成する。
#. 意味のある名前を記入して |OK| を押してライブラリーを作成する。この説明中では
   名前を `AuthorsCalcMacros` とする。 |BasicMacroOrganizerDlg| の
   :guilabel:`&Library` 領域が更新され、新しく作成されたライブラリーの名前が表示
   される。ライブラリー名は 30 文字まで使用できる。ダイアログボックスには名前の
   一部しか表示されない場合がある。
#. :guilabel:`&Library` で `AuthorsCalcMacros` 項目を選択し、|EditButton| を押し
   てライブラリーを編集する。`Module1` と `Main` という名前のマクロが自動的に生
   成する。LibreOffice Basic 統合開発環境 (IDE) が開く。

   LibreOffice Basic IDE の既定構成は以下のとおり：

   * |MenuBar|
   * ツールバー二つ。:guilabel:`Macro` ツールバーにはプログラムを編集したりテス
     トしたりするための図像各種が用意されている。
   * :guilabel:`Object Catalog` 窓では必要なライブラリーコンテナー、ライブラ
     リー、モジュール、マクロを選択できる。
   * Editor  LibreOffice Basic のプログラムコードを編集する。左側の列はプログラ
     ムコードにブレイクポイントを設定するために使用する。
   * :guilabel:`Watch` 窓にはシングルステップ処理中の変数や配列の内容が表示され
     る。
   * :guilabel:`Call Stack` 窓は関数のコールスタックに関する情報を与える。
   * タブが並ぶ部分
   * |StatusBar|

   LibreOffice Basic IDE は LibreOffice Basic マクロの開発とデバッグのための強力
   な機能を搭載している。この機能の詳細については |Help| を参照しろ。
#. Editor Window でコードを修正する。重要な追加点は、値 5 を返す ``NumberFive``
   関数の作成だ。

   .. tip::

      ``Option Explicit`` 文はすべての変数を使用する前に宣言することを強制する。
      ``Option Explicit`` が省略された場合、変数は最初の使用時に自動的に
      ``Variant`` 型として定義される。

#. LibreOffice Basic IDE 内で |MenuBar| の :menuselection:`&File-->&Save` を選択
   するか、|StandardToolbar| の :guilabel:`Save` 図像をクリックするか、|Ctrl| +
   :kbd:`S` を押して、変更した `Module1` を保存する。

Using a macro as a function
----------------------------------------------------------------------

セルを選択し、数式バーにマクロ呼び出しコードを入力すると、Calc がマクロを検出して
呼び出し、そのセルに結果を表示する。

新しく作成した :file:`CalcTestMacros.ods` スプレッドシートを使用して、セルを選択
し、数式 ``=NumberFive()`` を入力する。Calc がマクロを検出して呼び出し、その
セルに結果 (5) を表示する。

.. tip::

   関数名は大文字と小文字を区別しない。図では関数名は ``NumberFive`` と入力され
   ているが、Calc は |FormulaBar| に ``NUMBERFIVE`` と表示する。

Macro security warnings
----------------------------------------------------------------------

.. admonition:: 利用者ノート

   本節の内容が再現できない。実際にスプレッドシートを開き直すと本書のスクリーン
   ショットのようなものは現れず。シート上部に警告が表示される。そこには
   :guilabel:`&Enable Macros` ボタンのようなものは存在しない。

   これは |OptionsDlg| |SecurityPage| の :guilabel:`Macro &security...` を押し
   て、:guilabel:`Trusted Sources` タブの信用ファイルパス一覧を操作して回避する
   ことにする。

Calc 文書を保存して閉じ、再度開け。|OptionsDlg| |SecurityPage| にある
:guilabel:`Macro Securit&y...` を使用してアクセスした |MacroSecurityDlg| の設定
によっては警告されることがある。

警告ダイアログボックスに :guilabel:`&Enable Macros` ボタンがある場合、それを押す
必要がある。文書にマクロが含まれることが予想されない場合は、マクロがウイルスであ
る場合に備えて、:guilabel:`&Disable Macros` を押す方が安全だ。

設定により無効である旨の警告の場合、文書内でのマクロ実行は許可されない。|OK| を
押して警告を消す。

マクロを無効にして文書を読み込むと、Calc はマクロ関数を見つけることができず、影
響を受けるセルにテキスト `#NAME?` を表示してエラーを指摘する。

Loaded / unloaded libraries
----------------------------------------------------------------------

スプレッドシートを開くとき、利用可能なライブラリコンテナーで見つかるマクロライブ
ラリーすべてを開かない。代わりに、自動的に `My Macros` ライブラリコンテナー内の
`Standard` ライブラリーと、文書自体の `Standard` ライブラリーしか読み込まない。

:file:`CalcTestMacros.ods` スプレッドシートを再度開くと、Calc には `NumberFive`
という名前の関数が含まれていないため、この関数があるかどうか、表示され、読み込ま
れているすべてのマクロライブラリーが調べられる。`LibreOffice Macros`, `My
Macros`, および文書にロードされたライブラリーで、適切な名前の関数があるかどうか
が調べられる。本章での初期実装では `NumberFive` 関数は `AuthorsCalcMacros` ライ
ブラリーに格納されている。そのため `NumberFive` 関数は見つからず、呼び出された升
目にエラー状態が表示される。

|MenuBar| |MacrosOrganizeBasicM| を使用して |BasicMacrosDlg| を開け。ロードされ
たライブラリーの図像は、ロードされていないライブラリー (`AuthorsCalcMacros`) の
それとは見てくれが異なる。

ライブラリーをロードするために `AuthorsCalcMacros` の横にある展開図像をクリック
しろ。図像の見てくれが変わり、ライブラリーがロードされたことを示唆する。|Close|
を押して |BasicMacrosDlg| を閉じろ。

最初の実装では ``=NumberFive()`` を含む升目はまだエラーになっている。Calc は升目
を編集するか何らかの方法で変更しない限り、エラー中のセルを再計算しない。通常の解
決策は、関数として使用されるマクロを `Standard` ライブラリーに格納することだ。マ
クロの規模が大きい場合や数が多い場合は、希望する名前のスタブが `Standard` ライブ
ラリーに格納される。スタブマクロは実装を含むライブラリーをロードし、実装を呼び出
す。次の手順だ。

#. |MenuBar| |MacrosOrganizeBasicM| を使用して、|BasicMacrosDlg| を開く。
   `NumberFive` マクロを選択し、|EditButton| を押して編集用のマクロを開く。
#. LibreOffice Basic IDE が開く。キャレットは Editor 窓の関数 `NumberFive` の行
   に置かれる。関数のコードが TODO と一致するように、`NumberFive` の名前を
   `NumberFive_Implementation` に変更する。
#. LibreOffice Basic IDE の |StandardToolbar| の :guilabel:`Select Macro` ボタン
   を押して |BasicMacrosDlg| を開く。
#. :file:`CalcTestMacros.ods` 内の `Standard` ライブラリーを選択し、
   :guilabel:`New` ボタンを押して新しいモジュールを作成する。`CalcFunctions` な
   ど意味のある名前を入力し、|OK| を押す。Calc は自動的に `Main` という名前のマ
   クロを作成し、編集用にモジュールを開く。
#. `Standard` ライブラリーの `CalcFunctions` モジュールに `AuthorsCalcMacros` ラ
   イブラリーがまだロードされていなければロードし、実装関数を呼び出すマクロを作成
   する。TODO
#. 保存して閉じ、Calc 文書を再度開く。今度は、マクロが有効になっていれば、
   `NumberFive` 関数は期待どおりに動作する。

.. admonition:: 読者ノート

   スプレッドシートを開くとロードされるマクロライブラリーは次の二種類だ：

   * `My Macros` ライブラリー容器内の `Standard` ライブラリー
   * 文書自身の `Standard` ライブラリー

   それゆえ、先ほどのスプレッドシートを再度開くと、マクロ関数呼び出しのセルは
   ``#NAME?`` エラーとなる。これを修正する手順は本書のように二段階に分かれる：

   #. |BasicMacrosDlg| を開いて、ツリーノードを選択することで対象ライブラリーを
      ロードする。
   #. マクロ実装を次のように修正する：

      * 本体実装を MyMacros/Standard/CalcFunctions に移転する。
      * 旧関数はそのラッパーとする。

Passing arguments to a macro
----------------------------------------------------------------------

本文で示されている関数で用いられている重要な技法とは：

#. 仮引数に ``Optional`` キーワードを付ける。
#. オプション引数を関数 ``IsMissing`` で実引数が与えられたかをチェックする。
#. 関数 ``IsArray`` で値が配列であるかどうかをチェックする。
#. 関数に ``PositiveSum(A2:B5)`` のように範囲が渡される場合に備え、関数
   ``LBound`` と ``UBound`` を用いて配列の境界を決定する（前者は 1 であることが
   確定しているが、コードの一貫性を高めるためにこう書く）。

本書で次に示されている関数のように、引数リストは一般的なプログラミング言語のそれ
のように記述される。

Arguments are passed as values
----------------------------------------------------------------------

Calc からマクロに渡される引数は常に値 (by-value) だ。つまり、どのセルが使用され
たかを知ることはできない。どのセルが参照されたかを知る必要がある場合は、範囲を文
字列として渡し、その文字列を解析して、参照されたセル内の値を取得するなどする。

Writing macros that act like built-in functions
----------------------------------------------------------------------

Calc はマクロを関数として検出、呼び出すが、組み込み関数としての振る舞いはしない。
例えば、マクロは関数一覧に現れない。

Deleting LibreOffice Basic macros
----------------------------------------------------------------------

マクロを削除したい場合とモジュールを削除したい場合がある。不要なマクロを削除する
手順は：

#. 上述のように :guilabel:`Macros` ダイアログボックスを開く。
#. 削除対象のマクロを選択して :guilabel:`&Delete` を押す。
#. 確認で |Yes| を押す。
#. |Close| を押す。

不要なモジュールを削除する手順：

#. 上述のように :guilabel:`Macros` ダイアログボックスを開く。
#. :guilabel:`Organizer` を押して |BasicMacroOrganizerDlg| を開く。
#. :guilabel:`Modules` タブが開いているので、削除対象モジュールを選択する。
#. :guilabel:`&Delete` を押す。
#. 確認で |Yes| を押す。
#. |Close| を押す。

Accessing cells directly
======================================================================

LibreOffice の内部オブジェクトに直接アクセスして、Calc 文書を操作できる。

* ``ThisComponent.getSheets()`` によってシートにアクセスする。
* ``getCellByPosition(col, row)`` で特定の行と列のセルを得る。

.. tip::

   セルオブジェクトのメソッドはとりあえず次を知っておくといい。適切な値を設定す
   るには、対応する ``set`` 関数を使用する：

   * ``getValue()``
   * ``getString()``
   * ``getFormula()``

シートオブジェクトの ``getCellRangeByName`` メソッドはセルまたはセル範囲を返す。
セル範囲は配列の配列としてデータを返すので、二次元の配列として扱うよりも面倒だ。

.. tip::

   マクロが Calc 関数として呼び出される場合、関数を含むセルを除き、マクロが呼び
   出されたシート内のセルの値を変更することはない。

Sorting
======================================================================

ソートをコードで実現しようとすると、本書のように案外いろいろなオブジェクトの面倒
面倒を見なければならないということを覚えておけば今はいいだろう。

Overview of BeanShell, JavaScript, and Python macros
======================================================================

Introduction
----------------------------------------------------------------------

ここまで見てきたコードは LibreOffice Basic という言語だ。他にも次の言語を対応し
ている：

* BeanShell
* JavaScript
* Python

マクロの構成は四つのスクリプト言語すべてで同じだ。`LibreOffice Macros` コンテ
ナーには LibreOffice のインストール時に供給されるマクロすべてが含まれる。`My
Macros` ライブラリコンテナーには LibreOffice 文書で使用できるマクロを含む。各文
書には他の文書では使用できないマクロを格納することもできる。

先述のマクロ記録機能を使用すると Calc は LibreOffice Basic でマクロを作成する。
その他のスクリプト言語を使用するには、自分でコードを記述する必要がある。

:menuselection:`&Tools-->&Macros-->R&un Macro...` コマンドは上記の言語のいず
れも実行可能だ。

:menuselection:`&Tools-->&Macros-->&Edit Macros...` コマンドは Basic マクロだけ
選択、編集可能だ。

LibreOffice で使用されているコンポーネントモデルは |UNO| として知られている。ス
クリプト言語の LibreOffice マクロは |UNO| 実行時 API を使用する。XSCRIPTCONTEXT
インターフェイスが四言語すべてのマクロスクリプトに対して用意され、文書に対して何
らかの動作を実行するために必要となるさまざまなインターフェイスへのアクセス手段を
備えている。

.. admonition:: 読者ノート

   LibreOffice の前身である OpenOffice から存在するものらしい？

BeanShell macros
----------------------------------------------------------------------

   BeanShell is a Java-like scripting language that was first released in 1999.

|MenuBar| から :menuselection:`&Tools-->&Macros-->&Organize Macros-->
B&eanShell...` を実行すると :guilabel:`BeanShell Macros` ダイアログボックスが開
く。

.. admonition:: 利用者ノート

   JRE が有効になっている必要がある。無効なら確認ダイアログボックスが開く。

|EditButton| を押せばデバッグウィンドウが開く。

JavaScript macros
----------------------------------------------------------------------

同じような操作で :guilabel:`JavaScript Macros` ダイアログボックスが開く。
|EditButton| を押すと `Rhino JavaScript <https://github.com/mozilla/rhino>`__ デ
バッガーが開く。

Python macros
----------------------------------------------------------------------

同じような操作で :guilabel:`Python Macros` ダイアログボックスが開く。

Python スクリプトを編集およびデバッグする機能は、現在のところ LibreOffice の標準
|UI| に統合されていない。愛用テキストエディターや外部 IDE を使用して Python スク
リプトを編集すればいい。Alternative Python Script Organizer (APSO) 拡張機能は、
特に文書に埋め込まれた Python スクリプトの編集を容易にする。APSO を使用すると、
愛用コードエディターを設定したり、統合 Python シェルを起動したり、Python スクリ
プトをデバッグしたりすることが可能だ。

詳細については LibreOffice |Help| システムで *Python macros* を検索し、
<https://wiki.documentfoundation.org/Macros/Python_Design_Guide> の関連節を見
ろ。

.. admonition:: 利用者ノート

   HelloWorld を実行したら Writer が起動する。なぜだ？

ScriptForge library
======================================================================

ScriptForge ライブラリーの目的は LibreOffice API やコマンドを学ぶことなく、マク
ロの作成を簡単にすることだ。

ScriptForge ライブラリーは LibreOffice Basic と Python を対応している。各サービ
スには特定のトピックに関連するメソッドやプロパティーがある。

* |Guide| の関連章に ScriptForge に関する補足説明と例が記載されている。
* LibreOffice ヘルプシステムの索引で ScriptForge を検索すると情報があるはずだ。

Built-in object inspector
======================================================================

プログラマーにとって、|UNO| オブジェクト型や、サービス、メソッド、性質を発見する
ことは主要な課題の一つだ。

|MenuBar| から :menuselection:`&Tools-->Develo&pment Tools` を実行するとビュー
ワーが開く。メインウィンドウ下部に入渠している。

ウィンドウの左側は DOM 案内図で構成され、使用者は文書内の物全てを渡り歩くことが
できる。物が選択されるとそれに関する次の情報が窓右側のタブに示される：

* 実装されているインターフェイス全ての名前
* 支援するサービス全ての名前
* 利用可能な性質全ての名前と型
* 呼び出せるメソッド全ての名前、引数、戻り値の型

DOM 案内図を使って物を検査する代わりに、Current Selection ボタンを切り替えること
で文書内で現在選択されている物を直接検査することが可能。

|Guide| の *Getting Started with Macros* には組み込み物検査に関する追加情報が含
まれている。より詳細な情報や例は LibreOffice |Help| の索引で *development tools*
を検索しろ。

Working with VBA macros
======================================================================

Calc が Excel ワークブックを読み込むにもかかわらず、その VBA が Calc で動作しな
い主な理由は、Calc がワークシート上のセルなどのワークブック部品にアクセスするた
めに異なる仕組みを用いているためだ。

VBA コードを変換するには LibreOffice で VBA コードをまず読み込む必要がある。

Loading VBA code
----------------------------------------------------------------------

|OptionsDlg| :menuselection:`Load/Save-->VBA Properties` ページでは LibreOffice
で開いた MS Office 文書のマクロを保持するかどうかを選択可能。

:guilabel:`Load Basic &code` をオンにすると LibreOffice でマクロを編集できる。変
更したコードは |ODF| 文書に保存されるが、Microsoft Office 形式に保存した場合は保
持されない。

:guilabel:`&Save original Basic code` をオンにする場合、マクロは LibreOffice で
は動作しないが、ファイルを Microsoft Office 形式で保存すると変更されずに保持され
る。

VBA コードを含む Microsoft Word または Excel ファイルをインポートする場合、
:guilabel:`E&xecutable code` をオンにすることができる。通常、コードは保存される
が、機能停止状態になる [#calc13-footnote-1]_ のに対し、オンにするとコードが実行
可能状態になる。

:guilabel:`&Save original Basic code` は :guilabel:`Load Basic &code` より優先さ
れる。両方ともオンであり、LibreOffice で無効化されたコードを編集する場合、
Microsoft Office 形式で保存するときに元の VBA コードが保存される。

存在し得るマクロウイルスを Microsoft Office 文書から除去するには
:guilabel:`&Save original Basic code` をオフにする。文書は VBA コードなしで保存
される。

Option VBASupport statement
----------------------------------------------------------------------

``Option VBASupport`` 文は LibreOffice Basic が一部の VBA 文、関数、オブジェクト
を対応することを指定する。

.. note::

   VBA に対する支援は完全ではないが、一般的な使用例の大部分に及ぶ。

VBASupport が有効である場合、LibreOffice Basic 関数の引数および戻り値は VBA 関数
の引数および戻り値と同じになる。無効になっている場合、LibreOffice Basic 関数は
VBA 関数とは異なる引数や戻り値を受け取ることがある。

VBA UserForms (LibreOffice Basic Dialogs)
----------------------------------------------------------------------

フォーム（ダイアログボックス）は VBA オプションでは自動的に変換処理されない。本
書のコードのように手動で直せ。

Conclusion
======================================================================

本章に登場した各話題は本来は一章を割り当てるような大きいものだ。

`LibreOffice 拡張機能のウェブサイト <https://extensions.libreoffice.org/>`__ に
は LibreOffice Basic クイックレファレンスカード集がある。

----

.. rubric:: 章末注

.. [#calc13-footnote-1] Basic IDE で確認すると、すべてコメントアウトされているこ
    とがわかる。
