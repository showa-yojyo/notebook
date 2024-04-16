======================================================================
LibreOffice Calc Chapter 13 Macros ノート
======================================================================

.. include:: ./calc-inc.txt

.. contents:: 章見出し
   :local:

Introduction
======================================================================

マクロとは、後で使用するために保存される一連のコマンドやキー操作のことだ。

* 例：開いているスプレッドシートの現在のセルに自分の住所を入力するマクロ

マクロを使用すると、単純なタスクと複雑なタスクの両方を自動化できる。

マクロを作成する最も簡単な方法は、Calc の UI を通じて一連の操作を記録することだ。

BASIC 言語の方言である LibreOffice Basic スクリプト言語により記録したマクロを保
存する。そして LibreOffice Basic IDE を使用して編集および拡張可能。

マクロを作成する言語としては次の四つのスクリプト言語が対応されている：

* LibreOffice Basic
* Python
* JavaScript
* BeanShell

On Visual Basic for Applications (VBA) compatibility
======================================================================

LibreOffice Basic 言語と VBA 言語は BASIC の方言だ。

MS Excel で書かれたマクロを LibreOffice で使用したい場合は、まず LibreOffice
Basic IDE でコードを編集する必要がある。

Using the macro recorder
======================================================================

.. admonition:: 利用者ノート

   *Getting Started Guide* を先に読んでおいたほうがいいかもしれない。

まず、オプション設定から :menuselection:`LibreOffice --> Advanced` ページでオプ
ション :guilabel:`Enable macro recording (may be limited)` をオンにしておけ。

本書手順では、スプレッドシートのセル範囲に対して、乗算を伴う特殊な貼り付けを
実行するマクロを作成する。要点を記すと：

#. :menuselection:`&Tools --> &Macros --> &Record Macro` で開始。テキストエディ
   ターにおけるキーボードマクロ開始のようなものだと考えられる。:guilabel:`Record
   Macro` ミニウィンドウが現れる。
#. 所望のシート編集を行う。
#. ミニウィンドウ内の :guilabel:`Stop Recording` を押して収録終了。

正常な操作が収録されると :guilabel:`Basic Macros` ダイアログボックスが開く。以
下、収録内容を編集する手順：

#. :guilabel:`Save Macro` ツリーで現在文書ノードの子にある :guilabel:`Standard`
   を選択する。
#. タブの :guilabel:`&New...` を押して :guilabel:`New Module` ダイアログボックス
   を出し、意味のある名前を入力して :guilabel:`&OK` を押す。

:guilabel:`Basic Macros` ダイアログボックスの :guilabel:`Save Macro In` ツリーに
はライブラリー容器、ライブラリー、モジュール、マクロが階層化されている。

ライブラリ名、モジュール名、マクロ名に使用可能な文字が規定されているので注意。一
般的なプログラミング言語にありがちな規則だと思っていい。

Write your own functions
======================================================================

Create a function macro
----------------------------------------------------------------------

マクロを作成し、関数を呼び出すようにそれを実行することが可能。単純な関数マクロの
定義手順：

#. :menuselection:`&Tools --> &Macros --> &Organize Macros --> &Basic...` を実行
   して :guilabel:`Basic Macros` ダイアログボックスを開く。
#. :guilabel:`&Organizer...` を押す。:guilabel:`Basic Macro Organizer` ダイアロ
   グボックスが開く。
#. :guilabel:`Libraries` タブを開く。
#. :guilabel:`L&ocation` ドロップダウンリストを現在文書に合わせるなどし
   て、:guilabel:`&Library` 欄の一覧を更新する。
#. :guilabel:`&New...` を押す。
#. 意味のある名前を記入して :guilabel:`&OK` を押す。一覧が更新する。
#. 今入力した名前の項目を選択して :guilabel:`&Edit...` を押す。IDE が開く。

以下、このエディターで VBA 的コードを書いて保存し、シートのセルから数式の形でそ
れを呼び出すという流れになる。

Using a macro as a function
----------------------------------------------------------------------

セルを選択し、数式バーにマクロ呼び出しコードを入力すると、Calc がマクロを検出して
呼び出し、そのセルに結果を表示する。

Macro security warnings
----------------------------------------------------------------------

.. admonition:: 利用者ノート

   本節の内容が再現できない。実際にスプレッドシートを開き直すと本書のスクリーン
   ショットのようなものは現れず。シート上部に警告が表示される。そこには
   :guilabel:`&Enable Macros` ボタンのようなものは存在しない。

   これはオプション設定の :menuselection:`LibreOffice --> Security` ページの
   :guilabel:`Macro &security...` を押して、:guilabel:`Trusted Sources` タブの
   信用ファイルパス一覧を操作して回避することにする。

Loaded / unloaded libraries
----------------------------------------------------------------------

スプレッドシートを開くとロードされるマクロライブラリーは次の二種類だ：

* My Macros ライブラリー容器内の Standard ライブラリー
* 文書自身の Standard ライブラリー

それゆえ、先ほどのスプレッドシートを再度開くと、マクロ関数呼び出しのセルは
``#NAME?`` エラーとなる。これを修正する手順は本書のように二段階に分かれる：

#. :guilabel:`Basic Macros` ダイアログボックスを開いて、ツリーノードを選択するこ
   とで対象ライブラリーをロードする。
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
#. 削除対象のマクロを選択して :guilabel:`Delete` を押す。
#. 確認で :guilabel:`&Yes` を押す。
#. :guilabel:`&Close` を押す。

不要なモジュールを削除する手順：

#. 上述のように :guilabel:`Macros` ダイアログボックスを開く。
#. :guilabel:`Organizer` を押して :guilabel:`Basic Macro Organizer` を開く。
#. :guilabel:`Modules` タブが開いているので、削除対象モジュールを選択する。
#. :guilabel:`&Delete` を押す。
#. 確認で :guilabel:`&Yes` を押す。
#. :guilabel:`&Close` を押す。

Accessing cells directly
======================================================================

LibreOffice の内部オブジェクトに直接アクセスして、Calc 文書を操作できる。

* ``ThisComponent.getSheets()`` によってシートにアクセスする。
* ``getCellByPosition(col, row)`` で特定の行と列のセルを得る。

セルオブジェクトのメソッドはとりあえず次を知っておくといい。適切な値を設定するに
は、対応する ``set`` 関数を使用する：

* ``getValue()``
* ``getString()``
* ``getFormula()``

シートオブジェクトの ``getCellRangeByName`` メソッドはセルまたはセル範囲を返す。
セル範囲は配列の配列としてデータを返すので、二次元の配列として扱うよりも面倒だ。

マクロが Calc 関数として呼び出される場合、関数を含むセルを除き、マクロが呼び出さ
れたシート内のセルの値を変更することはない。

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

先述のマクロ記録機能を使用すると Calc は LibreOffice Basic でマクロを作成する。
その他のスクリプト言語を使用するには、自分でコードを記述する必要がある。

:menuselection:`&Tools --> &Macros --> R&un Macro...` コマンドは上記の言語のいず
れも実行可能だ。

:menuselection:`&Tools --> &Macros > &Edit Macros...` コマンドは Basic マクロだけ
選択、編集可能だ。

BeanShell macros
----------------------------------------------------------------------

   BeanShell is a Java-like scripting language that was first released in 1999.

メニューから :menuselection:`&Tools --> &Macros --> &Organize Macros -->
B&eanShell...` を実行すると :guilabel:`BeanShell Macros` ダイアログボックスが開
く。

.. admonition:: 利用者ノート

   JRE が有効になっている必要がある。無効なら確認ダイアログボックスが開く。

:guilabel:`&Edit...` ボタンを押せばデバッグウィンドウが開く。

JavaScript macros
----------------------------------------------------------------------

同じような操作で :guilabel:`JavaScript Macros` ダイアログボックスが開く。編集ボ
タンをクリックすると `Rhino JavaScript <https://github.com/mozilla/rhino>`__ デ
バッガーが開く。

Python macros
----------------------------------------------------------------------

同じような操作で :guilabel:`Python Macros` ダイアログボックスが開く。

.. admonition:: 利用者ノート

   HelloWorld を実行したら Writer が起動する。なぜだ？

ScriptForge library
======================================================================

ScriptForge ライブラリーの目的は LibreOffice API やコマンドを学ぶことなく、マク
ロの作成を簡単にすることだ。

ScriptForge ライブラリーは LibreOffice Basic と Python を対応している。各サービ
スには特定のトピックに関連するメソッドやプロパティーがある。

* *Getting Started Guide* の関連章に ScriptForge に関する補足説明と例が記載され
  ている。
* LibreOffice ヘルプシステムの索引で ScriptForge を検索すると情報があるはずだ。

Built-in object inspector
======================================================================

プログラマーにとって、:abbr:`UNO (Universal Network Objects)` オブジェクト型や、
サービス、メソッド、プロパティーを発見することは主要な課題の一つだ。

メニューから :menuselection:`&Tools --> Develo&pment Tools` を実行するとビュー
ワーが開く。メインウィンドウ下部にドッキングしている。

Working with VBA macros
======================================================================

* Calc が Excel ワークブックを読み込むにもかかわらず、その VBA が Calc で動作し
  ない主な理由は、Calc がワークシート上のセルなどのワークブック部品にアクセスす
  るために異なる仕組みを用いているためだ。
* VBA コードを変換するには LibreOffice で VBA コードをまず読み込む必要がある。

Loading VBA code
----------------------------------------------------------------------

設定ダイアログボックスの :menuselection:`Load/Save --> VBA Properties` ページで
は、LibreOffice で開いた MS Office 文書のマクロを保持するかどうかを選択可能。

* コードを読み込み、それを変更するとそのコードは MS Office 形式保存時には保存さ
  れない。
* :guilabel:`&Save original Basic code` は :guilabel:`Load Basic &code` より優先
  される。

Option VBASupport statement
----------------------------------------------------------------------

``Option VBASupport`` 文は LibreOffice Basic が一部の VBA 文、関数、オブジェクト
を対応することを指定する。

* このオプションはモジュール内の実行可能コードの前に追加する。
* VBA のサポートは完全ではないものの、一般的な使用パターンの大部分を網羅している。
* VBASupport が有効な場合、LibreOffice Basic 関数の引数と戻り値は VBA の引数と同
  じだ（無効の場合は異なる）。

VBA UserForms (LibreOffice Basic Dialogs)
----------------------------------------------------------------------

フォーム（ダイアログボックス）は VBA オプションでは自動的に変換処理されない。本
書のコードのように手動で直せ。

Conclusion
======================================================================

本章に登場した各話題は本来は一章を割り当てるような大きいものだ。

`LibreOffice 拡張機能のウェブサイト <https://extensions.libreoffice.org/>`__ に
は LibreOffice Basic クイックレファレンスカード集がある。
