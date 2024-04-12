======================================================================
Writer Guide Chapter 15, Tables of Contents, Indexes, Bibliographies ノート
======================================================================

.. include:: ./abbrev.txt

.. contents:: 章見出し
   :depth: 3
   :local:

Introduction
======================================================================

LibreOffice Writer を使ってテキスト文書の目次、索引、書誌を作成し、管理する方法
について説明する。他の種類の索引についても簡単に触れている。この説明を理解するた
めには Writer とスタイルについての次の基本的知識が必要だ：

* |Chapter08|
* |Chapter09|

Tables of contents
======================================================================

Writer の目次機能を使えば、文書内の見出しから目次を自動で作成できる。文書の本文
や見出しが表示されているページで見出しのテキストに変更が加えられると、目次が自動
的に更新される。

始める前に、見出しのスタイルが一貫していることを確認しろ。例えば、章の表題には
`Heading 1` スタイルを使い、章の小見出しには `Heading 2`, `Heading 3` スタイルを
使うことができる。

この節では、次の方法を紹介する：

* 既定事項を使用して目次をすばやく作成する
* 目次をカスタマイズする

.. note::

   目次に表示されるさまざまなレベルには、どのようなスタイルでも使用できる。この
   章の例では、既定の `Heading` スタイルを使用している。
   :ref:`writer15-anchor-create-from` で説明されているように、目次に表示する段落
   スタイルを他にも指定することができる。

.. |HeadingNumbersItem| replace:: :menuselection:`&Tools-->Heading &Numbering...`
.. |UpdateIndexItem| replace:: :menuselection:`Update &Index`

.. tip::

   目次に見出しが表示されない場合は、正しい段落スタイルでタグ付けされているか確
   認しろ。見出しのレベル全体が表示されない場合は |HeadingNumbersItem| の設定を
   確認しろ。|Chapter08| を見ろ。

   テキストの追加や削除（見出しが別のページに移動するように）、見出しの追加、削
   除、変更を行った場合は、目次を更新する必要がある。これを行うには目次のどこか
   を右クリックし、コンテキストメニューから |UpdateIndexItem| を選択する。

   .. |FormattingAidsPage| replace:: :menuselection:`LibreOffice Writer-->Formatting Aids` ページ

   目次内にキャレットを配置できない場合は、|OptionsDlg| |FormattingAidsPage|
   :guilabel:`Protected Areas` 区画で :guilabel:`Enable cursor` をオンにしろ。

   目次は灰色背景で表示される。この背景は目次がフィールドであることを思い出させ
   るためのもので、表示されるテキストは自動的に生成される。背景は印刷されず、文
   書が |PDF| に変換された場合も表示されない。この灰色背景をオフにするに
   は、|OptionsDlg| :menuselection:`LibreOffice-->Application Colors` ページで
   :guilabel:`Text Document` 区画までスクロールして、:guilabel:`Index and table`
   をオフにしろ。

   この変更により、見出しとページ番号の間の点々の背後に灰色背景が表示されること
   がある。この網掛けをオフにするには、|OptionsDlg| |FormattingAidsPage| を開き、
   :guilabel:`Display formatting` 区画の :guilabel:`Tabs` をオフにしろ。

.. admonition:: 読者ノート

   :guilabel:`Enable cursor` はオン推奨。テキストをコピーすることがある。

Creating a table of contents quickly
----------------------------------------------------------------------

.. |InsertIndexEntryItem| replace:: :menuselection:`&Insert-->Table of Contents and Inde&x-->&Index Entry...`

書式は無骨かもしれないが、たいていの場合、既定の目次が必要なものすべてであること
がわかるだろう。既定の目次をはめ込む手順は：

#. 見出しレベル（章や節の見出しなど）別に次の段落スタイルを使用して文書を作成
   する：

   * `Heading 1`
   * `Heading 2`
   * `Heading 3`

   これらは目次に表示されるものだ。Writer は最大 10 レベルの見出しを評価できる。
#. 文書中の目次を表示したいところをクリック
#. |InsertTOCItem| を選択
#. |OK| を押す。項目がハイパーリンクとして生成された典型的な目次が出来上がる。

.. caution::

   :menuselection:`&Edit-->Track Chan&ges-->&Show` を有効にしている場合、目次を
   更新すると、削除された見出しが目次に含まれ、削除されたテキストによって目次の
   ページ番号が正しく表示されないため、エラーが発生する可能性がある。この問題を
   避けるには、目次を更新する前に、このオプションが選択解除されていることを確認
   しろ。

Customizing a table of contents
----------------------------------------------------------------------

.. |EditIndexItem| replace:: :menuselection:`Edit Inde&x`

目次は文書のスタイルや要件に合わせてカスタマイズすることができる。

まず、既存の目次の任意の場所で次のいずれかを行い、|TOCDlg| を開く：

* 右クリックメニューから |EditIndexItem| を選択する
* 目次を表示する文書内でクリックし、|InsertTOCItem| を選択

|TOCDlg| にはタブが五つある。それぞれのタブは目次の構造と体裁の異なる側面を網羅
する：

* |TypeTab|: 目次の属性を設定する。
* |EntriesTab| と |StylesTab|: 目次の項目の書式を設定する。
* |ColumnsTab|: 目次を複数の列にする。
* |BackgroundTab|: 目次の背景に色や画像を追加する。

ダイアログボックスの右側にあるプレビューを表示するには、ダイアログボックスの左下
にある :guilabel:`&Preview` をオンにする。

.. note::

   プレビューには |TypeTab|, |EntriesTab|, |StylesTab| で設定した結果が表示され
   る。残りのタブでの変更は表示されない。

   すべての変更を行ったら、|OK| を押して適用する。|ColumnsTab| と|BackgroundTab|
   の設定を既定に戻すには、各タブを順番に選択して |ResetButton| を押す。残りのタ
   ブの設定は手動でリセットする必要がある。

.. _writer15-anchor-type-tab:

Type tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. |TitleBox| replace:: :guilabel:`&Title` 欄
.. |TypeList| replace:: :guilabel:`T&ype` ドロップダウンリスト
.. |Protected| replace:: :guilabel:`&Protected against manual changes` オプション

|TypeTab| を使って目次の属性を設定する。

.. rubric:: Type and Title

|TitleBox|
   目次に別の表題を付けるにはこの欄に指定する。表題を削除するには入力欄を消去す
   る。
|TypeList|
   型を選択する。目次の場合、選択肢が `Table of Contents` に設定されていることを
   確認しろ。他の型の作成については :ref:`writer15-anchor-alphabetic` と
   :ref:`writer15-anchor-other` を見ろ。

    .. note::

       型を変更できるのは最初に作成するときだけだ。いったん型（例えば目次）を定
       義すると、それを変更することはできない。

|Protected|
   既定では、目次が誤って変更されるのを防止するためオンになっている。目次はコン
   テキストメニューかダイアログボックスを使ってしか変更できない。これがオフであ
   る場合、他のテキストと同じように直接変更することができる。しかし、手動による
   変更は目次が更新されたときに失われるので、避けるべきだ。

.. rubric:: Create Index or Table of Contents

この領域の :guilabel:`Fo&r` ドロップダウンリストでは、目次が文書のすべての見出し
（文書全体）を網羅するのか、または目次がはめ込まれている章の見出ししか網羅しない
のかを選択できる。章を指定する見出しレベルは現在の見出しレベルになる。

Writer では目次を作成する際に最大 10 レベルの見出しを使用できる。含まれるレベル
の数を指定するには :guilabel:`Evaluate &up to level` に必要な数を入力する。

.. _writer15-anchor-create-from:
.. rubric:: Create From

この区画は目次の作成に何を使うかを決定する。

:guilabel:`&Headings`
   既定では、Writer は |HeadingNumbersItem| で見出しレベルに関連付けられた段落ス
   タイルで書式整形された段落を使用する。

   見出しレベルに使用する段落スタイルを変更したり、スタイルにアウトラインレベル
   を割り当てることで他の段落スタイルを含めることができる。これらの方法について
   は |Chapter08| で説明している。
:guilabel:`&Additional styles`
   目次に段落スタイルを追加することができる。これは、例えば、付録の見出しを目次
   に含めたい場合に便利だ。:guilabel:`&Headings` もオンである場合、追加されたス
   タイルは見出し番号で定義されたものと一緒に目次に含まれる。これをオンにし、ス
   :guilabel:`Assign &styles...` ボタンを押すと、:guilabel:`Assign Styles` ダイ
   アログボックスが開く。
:guilabel:`Inde&x entries`
   この選択項目は |InsertIndexEntryItem| を使用して文書にはめ込まれた索引登録項
   目を追加する。通常、目次にこの選択を使用することはない。しかし、ダイアログ
   ボックスの上部にある |TypeList| で `Table of Contents` を選択すると、Writer
   は索引登録項目と、アルファベットやその他の索引に含めることを意図した索引登録
   項目を区別する。

Entries tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

目次の項目を定義し、書式整形するには |EntriesTab| を使用する。要素を追加したり削
除したりすることで、各レベルを他のレベルから独立してスタイルを設定できる。

.. |StructureLine| replace:: :guilabel:`&Structure` 行

:guilabel:`&Level` 列の番号をクリックする。|StructureLine| にはそのレベルの登録
項目に含まれる要素が表示される。|StructureLine| に追加できる要素はこのすぐ下に表
示され、追加できない場合は灰色で表示される（たいていの場合、既に使用されているた
め）。

.. _writer15-anchor-toc:

* :guilabel:`LS` はハイパーリンクの開始を表す。
* :guilabel:`N#` は |HeadingNumbersItem| で見出しスタイルに割り当てられた見出し
  番号を表す。|Chapter08| を参照しろ。
* :guilabel:`E` は見出しテキスト、つまり各レベルで使用される段落スタイルで書式整
  形されたテキストを表す。
* :guilabel:`T` はタブストップを表す。
* :guilabel:`#` はページ番号を表す。
* :guilabel:`LE` はハイパーリンクの終わりを表す。
* |StructureLine| の各白色フィールドは空白を表し、カスタムテキストや別の要素を追
  加できる。

.. note::

   :guilabel:`Heading Numbering` ダイアログボックス (see |Chapter08|) で、任意の
   レベルの :guilabel:`Separator` 区画の :guilabel:`&Before` 欄または
   :guilabel:`&After` 欄にテキストが含まれている場合、そのテキストはそのレベルの
   :guilabel:`N#` フィールドの一部になる。構造行を作成する際は、目次の見てくれに
   不要な効果を与えないように注意しろ。

Adding elements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |TabStopButton| replace:: :guilabel:`Ta&b Stop` ボタン

|StructureLine| に要素を追加する手順：

#. 要素をはめ込みたい場所にある白いフィールドをクリックする。
#. |StructureLine| のすぐ下にある活動中ボタンの一つを押す。例えば、タブを追加す
   るには |TabStopButton| を押す。新しい要素を表す図像が |StructureLine| に表示
   される。
#. `Chapter` のようなカスタムテキストを追加するには、白いフィールドにテキストを
   入力する。末尾の空白文字を入れ忘れるな。

Changing elements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|StructureLine| の要素を変更するには、その要素を表す記号列をクリックし、次に
|StructureLine| のすぐ下にあるボタン列で、灰色表記されていないものを押す。例え
ば、章番号をタブストップに変更するには、|StructureLine| で :guilabel:`N#` を押
し、使用可能な要素の列で |TabStopButton| を押す。要素を変更する前にキャンセルす
るには、空白のいずれかをクリックする。

Applying changes to all levels
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

すべてのレベルに同じ構造と書式を適用したい場合は、右側の :guilabel:`&All` ボタン
をクリックする。

Deleting elements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|StructureLine| から要素を削除するには、その要素を表すボタンを押し、
:kbd:`Delete` を押す。例えば、既定のハイパーリンク設定を削除するには、
:guilabel:`LS` をクリックし、:kbd:`Delete` を押す。これを :guilabel:`LE` につい
ても繰り返す。

.. _writer15-anchor-applying:

Applying character styles
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |CharacterStyleList| replace:: :guilabel:`Character sty&le` ドロップダウンリスト

ある要素を、他の行とは少し違ったものにしたい場合もあるだろう。例えば、ページ番号
を太字にしたい場合などだ。要素に文字スタイルを適用する手順は：

#. 適切な文字スタイルが定義されていることを確認する。
#. |StructureLine| でスタイルを適用したい要素を表すボタンを押す。
#. |CharacterStyleList| で必要なスタイルを選択する。

ある文字スタイルの属性を表示または編集するには、|CharacterStyleList| でスタイル
を選択し、|EditButton| を押す。

.. tip::

   ハイパーリンク [#writer15-footnote-hyperlink]_ の既定の文字スタイルは
   `Internet Link` で、既定では下線が引かれ、青色で表示される。

   目次登録項目の既定のハイパーリンクは `Index Link` 文字スタイルに設定されてお
   り、`Internet Link` スタイルとは見てくれが異なる場合がある。インターネットリ
   ンクと同じように表示させたい場合は、|StructureLine| の :guilabel:`LS` を選択
   し、目次登録項目の文字スタイルの選択を `Internet Link` に変更することができ
   る。

   または、`Index Link` に対する属性を変更することもできる。

Tab parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|StructureLine| の :guilabel:`T` をクリックすると表示されるものだ：

* :guilabel:`Fill character`: 使用するタブ文字を選択する。
* :guilabel:`Tab stop position`: 左ページ余白とタブストップの間の距離を指定す
  る。オプションで、タブストップの位置を :guilabel:`Align right` にするか選択す
  る。

Tab position relative to paragraph style indent
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

このオプションを選択すると、個々の書式の設定に従って項目が字下げされる。段落スタ
イルで左字下げが指定されている場合、タブストップはこの字下げからの相対位置とな
る。このオプションが選択されていない場合、タブストップは左余白位置からの相対値と
なる。

.. _writer15-anchor-styles-tab:

Styles tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. |LevelsList| replace:: :guilabel:`L&evels` 一覧
.. |ParagraphStylesList| replace:: :guilabel:`Paragraph &Styles` 一覧

|StylesTab| を使用して、目次の各レベルのテキストを表示するために割り当てる段落ス
タイルを変更する。ほとんどの場合、最善の方法は割り当てられたスタイルはそのまま
に、必要に応じて設定を変更し、目次を思いどおりに表示することだ。

カスタム段落スタイルをアウトラインレベルに適用する手順：

#. |LevelsList| からレベルを選択する。
#. |ParagraphStylesList| から必要な段落スタイルを選択する。
#. :guilabel:`◁` ボタンを押して、選択した段落スタイルを選択したアウトラインレベ
   ルに適用する。

各レベルに割り当てられたスタイルは |LevelsList| の角括弧内に表示される。

アウトラインレベルから段落スタイルを削除するには、|LevelsList| でアウトラインレ
ベルを選択し、:guilabel:`&Default` ボタンを押す。

段落スタイルの属性を表示または編集するには、|ParagraphStylesList| でスタイルをク
リックし、|EditButton| を押す。

Columns tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

目次の列数を変更するには |ColumnsTab| を使用する。複数の列は目次よりもインデック
スで使われがちなので、このタブは索引の節 :ref:`writer15-anchor-columns` に説明が
ある。

.. _writer15-anchor-background-tab:

Background tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

目次の背景に色や画像を追加するには |BackgroundTab| タブを使用する。背景の追加に
ついては |Chapter06| を見ろ。

Adding color
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

目次の背景に色を追加するには、ダイアログボックスの上部にある :guilabel:`&Color`
ボタンを選択し、用意されている色から選択して |OK| を押す。

カスタム背景色の定義については |Chapter20| を参照しろ。

Adding an image
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

目次の背景に画像を追加するには :guilabel:`&Image` ボタンを押す。画像オプションが
表示される。

Deleting a color or an image
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

目次背景から色や画像を削除するには、ダイアログボックスの上部で :guilabel:`&None`
を押す。

Editing a table of contents
----------------------------------------------------------------------

既存の目次を編集するには、目次内の任意の場所を右クリックし、コンテキストメニュー
から |EditIndexItem| を選択する。また、Sidebar の Navigator を開き、
:guilabel:`Indexes` ノードをクリックし、:guilabel:`Table of Contents` をダブルク
リックすることもできる。

|TOCDlg| が開く。前の節で説明したように、目次を編集・保存することができる。

Updating a table of contents
----------------------------------------------------------------------

Writer は目次を自動的に更新しないので、文書の見出しを変更した後は、手動で目次を
更新する必要がある。目次の任意の箇所を右クリックし、コンテキストメニューから
|UpdateIndexItem| を選択する。

Navigator から索引を更新することもできる。:guilabel:`Indexes` ノードを展開し、更
新したい目次名を右クリックし、:menuselection:`&Update` を選択する。

.. admonition:: 読者ノート

   本書の記述よりメニュー構成が平たくなっているので修正した。

Deleting a table of contents
----------------------------------------------------------------------

.. |DeleteIndexItem| replace:: :menuselection:`Delete i&ndex`

文書から目次を削除するには、目次の任意の場所を右クリックし、コンテキストメニュー
から |DeleteIndexItem| を選択する。また、Navigator から削除するには、右クリック
メニューから :menuselection:`&Delete index` を選択する。

削除を確認する文言は出ない。

.. _writer15-anchor-alphabetic:

Alphabetic indexes
======================================================================

アルファベット順の索引は文書中で使用されているキーワードや語句の一覧で、ページ番
号順に記載されていれば、読者が情報をすばやく見つけるのに役立つ。索引は本や文書の
後ろにあるのが一般的だ。

この節では次について説明する：

* 索引項目を手動で追加する方法
* 索引登録ファイルを使用する方法
* アルファベット索引をすばやく作成する方法
* 索引項目の表示をカスタマイズする方法
* 索引の体裁をカスタマイズする方法
* 既存の索引項目を表示・編集する方法

Adding index entries
----------------------------------------------------------------------

.. |InsertIndexDlg| replace:: :guilabel:`Insert Index Entry` ダイアログボックス

索引を作成する前に、手作業で、あるいは :ref:`索引登録ファイル
<writer15-anchor-concordance>` を使って索引項目をいくつか作成する必要がある。手
動で索引項目を作成する手順：

#. 単語を索引に追加するには、その単語のどこかにキャレットを置く。複数の連続する
   単語を単一の項目として追加するには語句全体を選択する。
#. |InsertIndexEntryItem| を選ぶか、または :guilabel:`Insert` ツールバーの
   :guilabel:`Insert Index Entry` 図像をクリックして、|InsertIndexDlg| を表示す
   る。ダイアログボックスが開くと、選択したテキストが :guilabel:`&Entry` 欄に表
   示される。表示された単語や語句をそのまま受け入れることもできるし、 好きなもの
   に変更することもできる。
#. :guilabel:`I&nsert` ボタンを押して項目を作成する。

.. tip::

   単語の最初の文字の直前、または単語の最後の文字の直後にキャレットが置かれた場
   合、そのキャレットはその単語の中にあるとみなされる。

|InsertIndexDlg| を閉じることなく、複数の登録項目を作成することができる。それぞ
れについて：

#. 索引を作成したい文書の場所をクリックする。
#. ダイアログボックス上でもう一度クリックする。
#. 必要に応じて項目を変更し、挿入をクリックする。
#. 登録項目が終了するまでこれを繰り返し、|Close| を押す。

|InsertIndexDlg| の入力欄とその使い方：

:guilabel:`&Index`
   この登録項目の索引の型。既定は `Alphabetical Index` だが、このフィールドを使
   用して、目次や使用者定義の索引や一覧のための追加項目を登録することができる。
   例えば、本文中で言及されている種の学名のみを含む索引と、種の通称名のみを含む
   別の索引が欲しいかもしれない。:ref:`writer15-anchor-other` を見ろ。
:guilabel:`&Entry`
   選択した索引に追加する語句。この語句は文書そのものに含まれている必要はなく、
   同義語や索引に表示させたい他の用語を追加することができる。
:guilabel:`&1st key`
   索引キーとは、関連するページ番号を持たず、ページ番号を持ついくつかの下位登録
   項目を持つ登録項目のことだ。キーを使うと関連するトピックをグループ化するのに
   便利だ。次節参照。
:guilabel:`&2nd key`
   最大で三レベルの索引を持つことができ、第一レベルのキーのいくつかは、（ページ
   番号を持たない）キーでもある第二レベルの登録項目を持つ。この程度の索引の複雑
   さはあまり必要ではない。
:guilabel:`&Main entry`
   同じ用語が複数のページに索引付けされている場合、そのうちの一つのページにその
   トピックに関するより重要な情報や詳細な情報があることが多いので、そのページを
   主な登録項目にしたいものだ。主登録項目、つまり最も重要な登録項目のページ番号
   を目立たせるには、これをオンにし、主索引登録項目のページ番号の文字スタイルを
   太字などに定義する。
:guilabel:`Apply &to all similar texts`
   これをオンにすると、Writer は現在の選択範囲に一致する他の単語や語句を自動的に
   識別して覚える。さらに、:guilabel:`&Whole words only` と :guilabel:`Match
   ca&se` が使用できるようになる。不要なページ番号（その単語の非主流的用法）が索
   引に多数記載される可能性があるため、この選択肢を使用には注意しろ。

Example of using an index key
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

索引キーは下位登録項目をグループ化するための主登録項目だ。例えば、次のようなグ
ループ分けをしたいだろう：

.. code:: text

   LibreOffice
       Calc,  10
       Impress,  15
       Writer,  5

この例では `LibreOffice` が 1st key だ。下位登録項目（ページ番号が表示されてい
る）が索引登録項目だ。トピック `Writer` の索引項目をはめ込むには
|InsertIndexEntryItem| で :guilabel:`&Entry` に `Writer` と入力し、
:guilabel:`&1st key` に `LibreOffice` と入力する。

.. note::

   フィールド陰影が活動中である場合、[#writer15-footnote-shading1]_ 選択した語句
   が索引に追加されると、その語句の背景が灰色でテキストに表示される。索引項目の
   テキストが選択した単語のテキストから変更されている場合、索引項目はその単語の
   先頭または末尾に小さな灰色の四角形でマークされる。

.. _writer15-anchor-concordance:

Creating a concordance
----------------------------------------------------------------------

索引登録ファイルは、索引に追加する単語を列挙したプレーンテキストファイルだ。各行
に一つの単語または語句が定義されている。各行はセミコロンで区切られた七つのフィー
ルドからなる厳密な構造を持っている：

.. code:: text

   Search_term;Alternative_entry;1st_key;2nd_key;Match_case;Word_only

セミコロンとフィールドの内容の間には空白を入れるな。キーとは検索語がその下に置か
れる上位見出しのことだ。

代替項目、一番キー、二番キーを設けない場合は、これらのフィールドを空白のままにし
て、セミコロンが別のフィールドの直後に来るようにしろ。

最後の二つのフィールドは構造が多少異なる。登録項目と同じ大文字または小文字を持つ
登録項目だけが欲しい場合は、最後から二番目のフィールドに `1` を入力する。同様
に、最後のフィールドに `1` を入力すると、登録項目が単語全体であり、大きな単語の
一部でない場合のみを索引に含めるように設定する。最後の二つのフィールドを空白にす
ることもできる。

例えば

.. code:: text

   Macaw;Ara;Parrots;;0;0

で項目 `macaw` が次の状態で登録される:

* `macaw` の下の一覧
* 学名 `ara` の代替一覧
* `Parrots`, `Macaw` の一覧
* 二番キーなし（二つのセミコロンに注意）
* 小文字または大文字で始まる例を含む。
* 単語全体または長い単語の一部である場合

索引登録ファイルが手作業で項目を追加するよりも速いかどうかは議論の余地があるが、
索引登録ファイルがより体系的であることは確かだ。索引登録ファイルの欠点は、目的と
は無関係な一般的な単語の例を含む索引が作成される可能性があることだ。多くの場合、
有用な索引を作るには、手入力と索引登録ファイルとの組み合わせが必要となる場合があ
る。

Creating an alphabetic index quickly
----------------------------------------------------------------------

索引登録項目がいくつかできたところで、索引を作成することができる。

索引を広範囲にカスタマイズすることができるが、ほとんどの場合、選択をいくつかする
だけだ。

索引をすばやく作成するには：

.. |CombineWithF| replace:: :guilabel:`Combine identical entries with f. or &ff.`

#. 索引を追加したい文書内でクリックし、|InsertTOCItem| を選択して |TOCDlg| を開
   く。
#. |TypeTab| |TypeList| で `Alphabetical index` を選択する。
#. :guilabel:`Options` 区画で、:guilabel:`Case sensitive` や |CombineWithF| をオ
   フにすることを検討する。
#. 索引登録ファイルを使用する場合は :guilabel:`&Concordance file` をオンにし、
   :guilabel:`&File` を押して作成した索引登録ファイルを指定する。
#. |OK| を押す。典型的な索引が出来上がる。

Customizing an index
----------------------------------------------------------------------

既存の索引をカスタマイズするには、索引内の任意の場所を右クリックし、コンテキスト
メニューから |EditIndexItem| を選択する。

|TOCDlg| にはタブが五つある。これらのタブはすべて索引をカスタマイズするために使
用することができる。

* |TypeTab|: 索引の属性を設定する。
* |EntriesTab| と |StylesTab|: 索引の項目をフォーマットする。
* |ColumnsTab|: 索引を複数の列に配置する。
* |BackgroundTab|: 索引の背景に色や画像を追加する。

変更後、文書に表示されるように |OK| を押して索引を保存しろ。

Type tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|TypeTab| を使用して索引の基本属性を設定する。

.. admonition:: 読者ノート

   :ref:`最初の説明<writer15-anchor-type-tab>` と重複する記述はしない。

索引の型が `Alphabetical Index` に設定されていることを確認しろ。

その他の選択肢は索引がどのように登録項目を処理するかを決定する。

:guilabel:`Combine identical entries`
   同一登録項目をどのように扱うかを定義する。通常、索引付けされた単語や語句の各
   ページ番号が索引に表示される。しかし、|CombineWithF| をオンにして、これらを結
   合することができる。

   ページ範囲を表示したい場合は :guilabel:`Combine with -` をオンにする。
   ``23-31`` のようなものが表示される。どの文字が大文字かによって異なる登録項目
   を含めるには、:guilabel:`Case sensitive` をオンにする。
:guilabel:`AutoCapitapitali&ze entries`
   文書内の用語の表示に関係なく、各項目の最初の文字を自動的に大文字にする。
:guilabel:`&Keys as separate entries`
   索引キーに独自のページ番号を付けるにはこれをオンにする。
:guilabel:`&Concordance file`
   使用する索引登録ファイルがあればそれを指定する。詳しくは
   :ref:`writer15-anchor-concordance` を見ろ。
:guilabel:`Sort`
   登録項目を表示する際の並び替え方法を定義する。唯一の選択肢は英数字だが、どの
   言語のアルファベットを使うかを定義できる。

Entries tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

各登録項目の表示方法と内容を正確に設定するには |EntriesTab| を用いる。

はじめに、:guilabel:`&Level` 列で要素を書式整形したい索引レベルを選択する。レベ
ル `S` は :guilabel:`Format` 区画で :guilabel:`Alphabetical &delimiter` がオンで
ある場合に、索引登録項目をアルファベット順に分割する単一文字見出しを指す。後です
べての索引レベルに変更を適用できる。|StructureLine| にはそのレベルの登録項目の要
素が表示される。行内の各ボタンは要素一つを表す：

.. |HeadingInfoButton| replace:: :guilabel:`&Heading info` ボタン

* :guilabel:`E` は入力テキスト
* :guilabel:`T` はタブストップ
* :guilabel:`#` はページ番号
* :guilabel:`HI` は章情報。これは既定では存在しないが、|HeadingInfoButton| を押
  すことで追加できる。

|StructureLine| の各白フィールドは空白を表す。目次については :ref:`先述
<writer15-anchor-toc>` のように、要素を追加、変更、削除することができる。

Heading Info
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|HeadingInfoButton| はこのオプションが選択されたときに表示される見出し情報一覧か
ら選択された見出し番号や内容などの見出し情報をはめ込む。見出し情報は
|HeadingNumbersItem| で指定する。

Applying character styles
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|StructureLine| の各要素には書式を追加的に指定することができる。例えば、ページ番
号を他の索引テキストと異なるサイズにしたい場合がある。これを行うには、:ref:`目次
<writer15-anchor-applying>` のように、|StructureLine| の要素の一つに文字スタイル
を適用する。

Formatting entries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:guilabel:`Format` 区画の選択肢を使用して、さらなる書式を適用する。

:guilabel:`Alphabetical &delimiter`
   索引登録項目を、同じ最初の文字で始まるブロックに分け、その文字をヘッダーとし
   て使用するものである。例えば、索引が次のようなものであるとする：

   .. code:: text

      apple,  4
      author, 10
      break,  2
      bus, 4

   そして、この選択肢をオンにすると次のようになる：

   .. code:: text

      A
      apple,  4
      author, 10

      B
      break,  2
      bus, 4

:guilabel:`&Key separated by commas`
   索引の登録項目を同じ行に並べるが、カンマで区切る。
:guilabel:`Tab position relati&ve to Paragraph Style indent`
   これをオンにすると、項目はそれぞれの書式の設定に従って字下げされる。左字下げ
   のある段落スタイルが使用されている場合、タブストップはこの字下げに対して相対
   的になる。このオプションが選択されていない場合、タブストップは左余白位置に対
   して相対的になる。

Styles and Background tabs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|StylesTab| を使用して、索引の各レベルのテキスト表示に割り当てる段落スタイルを変
更する。ほとんどの場合、割り当てられたスタイルはそのままに、必要に応じて設定を変
更することで、索引を思い通りに表示することができる。

|BackgroundTab| は目次と同じだ。これらのタブの詳細については以下の節を見ろ：

* 目次版 :ref:`writer15-anchor-styles-tab`
* 目次版 :ref:`writer15-anchor-background-tab`

.. _writer15-anchor-columns:

Columns tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

索引の列数を変更するには |ColumnsTab| を使う。

Adding multiple columns
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

複数の列に索引を表示するには：

#. :guilabel:`Col&umns` に希望の列数を入力するか、列数を表す図像を選択する。
#. ページ幅に応じて列を均等に配置するには :guilabel:`Auto&Width` をオンにする。
   オフであれば、次の各項目を手動で設定することができる：

   * 各列の幅
   * 列間の間隔
#. 列と列の間に区切り線を入れる：

   * :guilabel:`St&yle`: 既定は `None` で、または三つの線スタイルから選択。
   * :guilabel:`&Widht`: 線の幅。既定は 0.25 pt だ。
   * :guilabel:`&Color`: 区切り線の色を選択する。既定は黒だ。
   * :guilabel:`H&eight`: 行の高さを列全体の高さに対する百分率で指定する。既定は
     100% だ。
   * :guilabel:`Position`: 高さが 100% 未満の場合、列に対する線の位置。

Maintaining an index
----------------------------------------------------------------------

索引の見てくれを変更するには、索引の任意の場所を右クリックし、コンテキストメ
ニューから |EditIndexItem| を選択する。|TOCDlg| が開き、前の節で記載されている五
つのタブを使用して索引を編集・保存することができる。

索引を更新または削除するには、索引内の任意の場所で右クリックし、
|UpdateIndexItem| または |DeleteIndexItem| をそれぞれ選択する。

Viewing and editing existing index entries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

最初の登録項目を追加したら、いくつかの修正を加えることができる。以下の手順で、こ
れらを表示および編集することができる：

#. フィールド陰影が活動中であることを確認する。[#writer15-footnote-shading2]_
#. 文書本文の既存の索引項目のフィールド網掛けにキャレットを置き、右クリックし
   て、内容メニューから |EditIndexItem| を選択する。変更されたテキスト登録項目の
   場合、フィールドの網掛けは単語の直前になる。テキスト項目としてマークされた単
   語の直前にキャレットを置くと、両方の選択条件を満たすことになる。
#. ダイアログボックスが表示される。進む矢印ボタンと戻る矢印ボタンを使って、さま
   ざまな索引項目を移動することができる。一つの単語や語句に複数の登録項目がある
   場合は、矢印の頭に垂直の棒が付いた二列目のボタンが表示され、それぞれの登録項
   目をスクロールすることができる。
#. 索引項目に必要な修正や追加を行い |OK| を押す。

.. _writer15-anchor-other:

Other types of index
======================================================================

アルファベット索引の他にも、図版、表組、物の索引があり、使用者定義の索引を作成す
ることもできる。ここで挙げている例ですべての可能性を示しているわけではない。

他の索引を作成する手順：

#. 索引を作成したい場所にキャレットを置く。
#. メニューで |InsertTOCItem| を選択。
#. |TOCDlg| |TypeList| で索引を選択する。
#. 前の節で説明したものと同様のさまざまなタブで調整する。
#. すべて設定したら |OK| を押す。

Example: Creating a table of figures
----------------------------------------------------------------------

:menuselection:`&Insert-->Caption` を使用するか、|Chapter17| で説明するように数
値範囲変数を使用して手動で図版の説明を作成したならば、図版や図表の目次を作成する
のは簡単だ。

#. |TOCDlg| |TypeList| で `Table of Figures` を選択する。オプションで
   |TitleBox| を変更する。
#. :guilabel:`Create From` 区画で :guilabel:`Capt&ions` が選択されていることを確
   認し、説明の区分を選択する。:guilabel:`Category` の既定は `Figure` で、この例
   では説明に対して `Figure` を使用している。
#. :guilabel:`&Display` で三択：

   * `References`: 次のものを全部含む
   * `Category and Number`
   * `Caption Text`
#. オプションで :guilabel:`Create fro&m additional paragraph style` を選択し、一
   覧からスタイルを選択する。
#. このダイアログボックスのその他のタブは目次について説明したものと同様だ。
#. |OK| を押す。

Bibliographies
======================================================================

   A :dfn:`bibliography` is a list of references used in a document.

参考文献を書誌データベースに保存することも文書自体に保存することもできる。

ここでの内容：

* 書誌データベースを作成し、登録項目を追加および管理する方法
* 文書に参考文献（引用）を追加する方法
* 書誌の書式を設定する方法
* 既存の書誌を更新および編集する方法

.. admonition:: 読者ノート

   これは習得したい。

Citation styles and the bibliographic database
----------------------------------------------------------------------

引用（参考文献）は文書内でも作成できるが、書誌データベースを作成することで、他の
文書での再利用が可能になり、多くの時間を節約することができる。

本文中の引用は、書誌データベースの異なるフィールド（レコード列）への入力と、本
文中の異なる提示が必要だ。参考文献一覧を作成する前に文書に必要な引用スタイルを決
めろ。主なスタイルは次の五つだ：

:abbr:`APA (American Psychological Association)`
   心理学、教育学、その他の社会科学
:abbr:`MLA (Modern Languages Association)`
   文学、芸術、人文科学
Chicago
   歴史と特定の出版物
Turabian
   大学生が一般的に使用する Chicago スタイルの変種
:abbr:`AMA (American Medical Association)`
   医学、健康、生物学

Bibliography Database はどのような引用スタイルを使用する場合でも、本文中の引用の
給源となる。

.. |IdentifierField| replace:: :guilabel:`Identifier` フィールド

どの引用も |IdentifierField| を用いて文書内の引用形式を設定する。この欄に引用ス
タイルに適した形式で引用を追加する。|IdentifierField| を含むすべての必要な情報は
文書内で引用を作成する前に入力する必要がある。

.. tip::

   Writer にはどの文書にも単一の書誌データベースがある。書式を設定するのは面倒で
   あるので、資料の種類ごとに引用の雛形を作成すると良い。

Creating a bibliographic database
----------------------------------------------------------------------

.. |ISBN| replace:: :abbr:`ISBN (International Standard Book Number)`

書誌データベースに新しいテーブルを作成する方法については |Guide| を見ろ。

書誌データベースはさまざまな媒体や状況を網羅しなければならないため、大量のフィー
ルドを含んでいる。また、|ISBN| のような、引用スタイルでは使用されないが、研究中
に役に立つかもしれないフィールドも含まれている。

.. note::

   どのような引用形式を使っても、書誌の単一登録項目に要する項目は六個かそこらで
   済む。異なるのは、資料の種類ごとに必要なフィールドと、各引用スタイルによる
   フィールドの順序だ。

.. |BiblioDatabase| replace:: :guilabel:`Bibliography Database` ウィンドウ
.. |BiblioDatabaseItem| replace:: :menuselection:`&Tools-->&Bibliography Database`

データベースを開くには |BiblioDatabaseItem| を選択する。|BiblioDatabase| が開
く。上部にはスプレッドシートに似た表型レイアウトで、すべての登録項目が表示され
る。下部には選択した項目のフィールドすべてが表示される。

.. |ShortName| replace:: :guilabel:`&Short name`

.. note::

   データベーステーブルの |IdentifierField| と表下の |ShortName| フィールドは同
   じだ。見本データベースのこれらのフィールドの見本登録項目は無意味だ。使用する
   引用スタイルに適した書式に置き換えろ。

Changing the data source
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

使用中のデータ給源を変更するには、

* メニューで :menuselection:`&Data-->&Choose Data Source...` を選択するか、
* |BiblioDatabase| の上部付近にあるツールバーの :guilabel:`Data Source` ボタンを
  押す。

:guilabel:`Choose Data Source` ダイアログボックスに登録済みのデータ給源が一覧表
示される。その中から一つを選択し |OK| を押す。

別のデータ給源を追加（登録）するには |Guide| 説明を参照しろ。

Filtering records
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

書誌データベース内の登録項目に絞り込みを設定するには、|BiblioDatabase| で次のい
ずれかを行う：

* |MenuBar| で :menuselection:`&Data-->&Filter...` を選択
* 上部付近のツールバーで :guilabel:`Standard Filter` 図像をクリック

:guilabel:`Standard Filter` ダイアログボックスで、絞り込むフィールド、条件、値を
選択し、「OK」をクリックする。

Adding entries to the database
----------------------------------------------------------------------

.. |DataSourceView| replace:: Data Source ビュー

登録項目を書誌データベースに追加するには、データベースの |DataSourceView| を使
用する方法と、|BiblioDatabase| を使用する方法の二つの方法がある。

書誌データベースの |DataSourceView| を使用して登録項目を追加するには：

#. メイン |MenuBar| の :menuselection:`&View-->&Data Sources...` を選択するか、
   キーバインド :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`F4` によりウィンドウを開く。
#. Bibliography データベースで正しいデータ表が選択されていることを確認する。必要
   ならば、正しいデータ表を選択するために木を展開する。
#. 一覧の一番下までスクロールし、空行内の関連フィールドを入力する。左上の
   :guilabel:`Save current record` 図像が活動開始する。これをクリックしてデータ
   ベースに追加を保存する。

|BiblioDatabase| を使用して登録項目を追加するには：

#. |MenuBar| の |BiblioDatabaseItem| を選択する。
#. ウィンドウの |MenuBar| で :menuselection:`D&ata-->&Record` を選択するか、横ス
   クロールバーの左にある :guilabel:`+` をクリックする。
#. |ShortName| 欄に登録項目の名前を入力する。必要に応じて他のフィールドも入力す
   る。
#. 登録項目を完成させてデータベースに追加するには、データ表の他の升目をクリック
   する。

Maintaining entries in the database
----------------------------------------------------------------------

データベース内の登録項目を管理するには、|DataSourceView| または |BiblioDatabase|
を使用する。適切な登録項目を選択し、必要に応じてフィールドを変更する。

変更された項目はキャレットが登録項目から移動するとデータベースに自動的に保存され
る。

Advanced: Modifying the bibliographic database
----------------------------------------------------------------------

書誌データベースは、以下にある方法で変更することができる。

.. note::

   LibreOffice のデータベース機能の使い方の詳細については |Guide| を参照しろ。

Column details
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

書誌データベースの列の詳細を変更するには、

* |MenuBar| の :menuselection:`&Data-->&Column Arrangement...` を選択するか、
* ツールバーの :guilabel:`Column Arrangement` ボタンをクリックする。

:guilabel:`Column Layout` ダイアログボックスでは、どのフィールドを列に割り当てる
かを変更することができる。たとえば、ドロップダウンリストの行き先を変更すること
で、:guilabel:`Author(s)` データを |IdentifierField| に入れるように選択できる。
|ShortName| データの列の行き先は、データの行き先が重複しないように、自動的に
`<none>` に設定される。

Field details
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

書誌データベースに変更を加えるには次のようにする：

#. |DataSourceView| を開く。
#. `Bibliography` データベースが選択されていることと、正しいデータ表が選択されて
   いることを確認する。
#. テーブル登録項目 (e.g. `biblio`) を右クリックし、:menuselection:`Edit
   &Database File...` を選択する。LibreOffice Base が開く。
#. 左柱で :guilabel:`&Tables` を選択する。
#. :guilabel:`Tables` で `biblio` を右クリックし :menuselection:`&Edit...` を選
   択すると設計ウィンドウが表示される。
#. これで各フィールドを選択できる。:guilabel:`Field Name` 升目のテキストを選択
   し、必要に応じて入力を変更する。:guilabel:`Field Type` 升目をクリックして選択
   メニューを開き、データ型を変更する。:guilabel:`Field Properties` ではデータ性
   質を変更することができる。選択された各フィールドについて、そのフィールドの説
   明が右に表示される。
#. 完了すると、変更を保存するかどうかの確認が求められる。

Adding references (citations) into a document
----------------------------------------------------------------------

文書に参考文献を追加する方法：

* Writer に組み込まれている書誌データベースなどから
* キーボードから直接

Entering references from a database
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. |InsertBiblioEntryItem| replace:: :menuselection:`&Insert-->Table of Contents and Inde&x-->&Bibliography Entry...`
.. |InsertBiblioEntryDlg| replace:: :guilabel:`Insert bibliography Entry` ダイアログボックス

書誌データベースから文献を文書に追加する手順：

#. キャレットを参照したい場所に置く。
#. |MenuBar| で |InsertBiblioEntryItem| を選択。
#. |InsertBiblioEntryDlg| で :guilabel:`&Bibliography Database` を選択。
#. |ShortName| ドロップダウンリストから文献を選択する。この下に、選択した文献の
   著者名と表題が確認用に示される。
#. 文書に参考文献をはめ込むには |Insert| を押す。
#. すべての参照を挿入し終わったら |Close| を押す。

Entering references from documents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. |DefineBiblioEntryDlg| replace:: :guilabel:`Define Bibliography Entry` ダイアログボックス

外部データベースからではなく、文書に直接書誌項目を入力することもできる。登録項目
を追加したい文書をクリックする。

#. |InsertBiblioEntryItem| を選択。
#. |InsertBiblioEntryDlg| で :guilabel:`&Document content` を選択。
#. :guilabel:`&New` ボタンを押して |DefineBiblioEntryDlg| を開く。

   #. 登録項目に関連するフィールドをすべて入力する。|InsertBiblioEntryDlg| では
      この登録項目が引用に使用される。
   #. |TypeList| からオプションを選択し、|OK| を有効にする。
   #. すべての入力が完了したら |OK| を押す。
   #. |Insert| を押して |ShortName| フィールドを文書に追加し、|Close| を押す。

文書内の登録項目を再利用するには、上記の手順を再開し、新しい登録項目を追加するこ
とを選択する代わりに、現在の登録項目の一覧から必要な |ShortName| を選択する。

Editing a reference
----------------------------------------------------------------------

.. |EditBiblioEntryDlg| replace:: :guilabel:`Edit Bibliography Entry` ダイアログボックス

参照を編集する手順：

#. 項目を右クリックする（キャレットが項目の左に表示される）。
#. コンテキストメニューで :menuselection:`&Bibliography Entry...` を選択する。
   |EditBiblioEntryDlg| が開く。
#. |ShortName| だけを素早く編集するには、テキストボックスをクリックし、登録項目
   を編集し |ApplyButton| を押す。
#. 登録項目の詳細を編集するには、:guilabel:`&Edit` ボタンを押して
   |DefineBiblioEntryDlg| を開く。

   必要な変更を行い、|OK| を押して |EditBiblioEntryDlg| に戻る。
#. |ApplyButton| を押してダイアログボックスを閉じる。

.. note::

   変更された参照は、文書にのみ保存される。給源が書誌データベースの場合、その
   データベースは変更されないままとなる。

Creating the bibliography
----------------------------------------------------------------------

#. 書誌をはめ込みたい箇所にキャレットを置く。
#. |InsertTOCItem| を選択し、|TypeList| を `Bibliography` に変更する。

ダイアログボックスの UI が変化する。以下、手順解説。

Type tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

文書の本文中に参考文献（引用）を表示する方法は二つある：

* 各書誌登録項目の |ShortName| フィールドに記録されたテキストを使用する (e.g.
  Smith, 2001)
* 参照した文書に対して本文中に出てくる順番に ``[1]`` のように番号を振る。

.. tip::

   文書内で使用する引用スタイルを指定するには、|TOCDlg| |TypeTab| を使用する。

書誌の書式は二つの場所で選択する：

* |TOCDlg|
* `Bibliography 1` 段落スタイル (see :ref:`writer15-anchor-para`)

基本設定は |TypeTab| で選択する。

#. 書誌に表題を付けるには |TitleBox| に入力する。必須ではない。
#. |Protected| をオンにすると、書誌が誤って変更されるのを防ぐことができる。書誌
   は右クリックメニューまたは |TOCDlg| でしか変更不能になる。オフである場合、書
   誌は他のテキストと同様に文書ページで直接変更できるが、手動で変更した内容は書
   誌を更新したときに失われる。
#. 書誌項目（引用）に文書本文内で番号を付けるには :guilabel:`&Number entries` を
   選択する。ただし、データベースからの |ShortName| フィールドの内容を文書内に表
   示したい場合はこれをオフにしろ。
#. 文書の本文中に表示される参照される項目の括弧の種類を選択する。
#. 必要な並べ替えを定義する。現在のところ、英数字による並び替えしかサポートされ
   ていない。登録項目が本文に表示される順序による並べ替えは |EntriesTab| タブで
   行う。

Entries tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|EntriesTab| の構造は目次や索引の構造と似ている。

:guilabel:`Type` 区画は、書籍、定期刊行物、Web ページなど、ソースの種類を示す。
|TypeList| の各登録項目には既定構造形式がある。登録項目の |TypeList| から選択す
ることで、そのソースに基づいて、登録項目がどのように現れるかを定義することもでき
るし、単に :guilabel:`All` ボタンを押してすべての登録項目に同じ形式を適用するこ
ともできる。

登録項目の |StructureLine| は書誌データベースで利用可能なフィールドに基づいてい
る。文書に必要な引用スタイルを参照し、必要に応じて |StructureLine| を修正しろ。

構造行から要素を削除するには、要素をクリックし、|RemoveButton| を押す。

要素を追加するにははめ込む |StructureLine| をクリックする。|TabStopButton| また
は |Insert| の左側にあるドロップダウンリストの要素を選択し、|Insert| を押す。ド
ロップダウンリストの要素は書誌データベースにあるフィールドだ。

|StructureLine| の要素のすべては |CharacterStyleList| を使って書式設定できる。た
とえば、書籍や議事録の表題が斜体や太字になるように文字スタイルを定義できる。

登録項目の並べ替え方法を決定するには :guilabel:`Sort by` オプションを変更する。
項目がテキストに表示される順序で並べ替えるには :guilabel:`Document &position` を
選択する。ほとんどの最新の引用スタイルでは :guilabel:`&Content` を選択する。類似
の文献をグループ化するには :guilabel:`Sort keys` を使用する。

Styles, Columns and Background tabs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

これらのタブの詳細については次を参照しろ：

* :ref:`writer15-anchor-styles-tab`
* :ref:`writer15-anchor-columns`
* :ref:`writer15-anchor-background-tab`

.. _writer15-anchor-para:

Modifying the paragraph style for the bibliography
----------------------------------------------------------------------

要件に合わせて `bibliography 1` 段落スタイルを変更することができる。例えば、書誌
一覧の登録項目に番号を付けるには、一覧スタイルを定義し、それを `Bibliography 1`
段落スタイルにリンクする必要がある。これを行う手順：

#. Sidebar |StylesDeck| で |ListStylesTab| をクリックする。`Numbering 123` を右
   クリックし、:menuselection:`&New...` を選択する。
#. |ListStyleDlg| |OrganizerTab| でこのスタイルの名前を入力する。
#. この例では、数字を角括弧で囲む。これを行うには |CustomizeTab| を開き、

   * :guilabel:`&Before` に ``[`` を、
   * :guilabel:`&After` に ``]``

   を入力する。
#. 次に |PositionTab| を開く。:guilabel:`&Indent at` と :guilabel:`&Tab stop at`
   で文書の書誌一覧の項目の二行目以降の字下げ量を指定する。多くの場合、最適な設
   定を確認するために少し試行錯誤が必要だ。
#. |OK| を押して設定を保存し、ダイアログボックスを閉じる。|StylesDeck| に戻り、
   |ParagraphStylesTab| をクリックし、ウィンドウ下部の一覧で `All Styles` を選択
   し、`Bibliography 1` を右クリックして :menuselection:`&Edit Style...` を選択
   する。
#. |ParagraphStyleDlg| |Outline&ListTab| :guilabel:`&List style` から
   `Bibliography` を選択する。
#. |OK| を押して `Bibliography 1` 段落スタイルにこの変更を保存する。

Updating, editing, and deleting an existing bibliography
----------------------------------------------------------------------

書誌内の任意の場所で右クリックする。コンテキストメニューから

* |UpdateIndexItem| で書誌を更新する。
* |EditIndexItem| で |TOCDlg| を開き、書誌を編集・保存できる。
* 確認要求なしで書誌を削除するには |DeleteIndexItem| を選択する。

External bibliography tool
----------------------------------------------------------------------

Writer の書誌機能が制限されすぎていると感じる場合は、macOS, Windows, Linux で利
用可能な無料のオープンソースツール、`Zotero <https://www.zotero.org/>`__ を試し
てみるとよい。Writer の相性も良いと報告されている。

----

.. rubric:: 章末注

.. [#writer15-footnote-hyperlink] :menuselection:`&Insert-->&Hyperlink...` で加
   えたものなど。
.. [#writer15-footnote-shading1] |OptionsDlg|
   :menuselection:`LibreOffice-->Application Colors` ページを確認
.. [#writer15-footnote-shading2] :menuselection:`View--> Field Shadings` または
   :kbd:`Ctrl` + :kbd:`F8`
