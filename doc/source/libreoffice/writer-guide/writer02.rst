======================================================================
Writer Guide Chapter 2, Working with Text: Basics ノート
======================================================================

.. |CTL| replace:: :abbr:`CTL (Complex Text Language)`

.. contents:: 本章見出し
   :depth: 3
   :local:

Introduction
======================================================================

Writer 環境を本章の記述に合わせるために、:guilabel:`Options` ダイアログボックス
:menuselection:`LibreOffice Writer --> Formatting Aids` ページの
:guilabel:`Display Formatting` 各種オプションをオンにしろ。

これらの目印の表示有無を切り替えるにはメニューから :menuselection:`&View -->
For&matting Marks` を選択する。:doc:`Chapter 20 <writer20>` 参照。

本章で扱うトピック：

* テキストの選択、切り取り、コピー、貼り付け、移動
* テキストの検索と置換
* 特別文字の入れ方
* 綴りや文法のチェック、類語辞典の使用、分綴法の選択肢
* AutoCorrect 機能、単語補完、AutoText 機能、大文字小文字の変更機能

:doc:`次の章 <writer03>` と :doc:`その次の章 <writer04>` も読め。

Selecting text
======================================================================

Writer におけるテキスト選択は他のアプリケーションにおけるものと似ている。テキス
ト上を：

* マウスポインターで選択する
* 複数のクリックを使って次のものを選択する：

  * 単語（ダブルクリック）
  * 文（三重クリック）
  * 段落（四重クリック）

テキストをクリックし、:kbd:`F8` を押して拡張選択モードに入り、矢印キーを使って連
続したテキストブロックを選択することも可能だ。テキストブロックを選択し終わったら
もう一度 :kbd:`F8` を押す。

.. admonition:: 読者ノート

   :kbd:`F8` キーがマウスクリック一発分に相当すると考えられる。

選択モードを変更するには Status バーの図像を使う方法がある。:doc:`前章
<writer01>` で述べた欄を右クリックするとコンテキストメニューに選択肢が表示され
る：

* :menuselection:`&Standard selection`
* :menuselection:`&Extending selection` (:kbd:`F8`)
* :menuselection:`&Adding selection` (:kbd:`Shift` + :kbd:`F8`)
* :menuselection:`&Block selection` (:kbd:`Ctrl` + :kbd:`Shift` + :kbd:`F8`)

項目を選択するとそのモードが有効になる。

Selecting items that are not consecutive
----------------------------------------------------------------------

標準選択モードで、マウスを使って連続しない項目を選択する手順：

#. テキストの最初を選択
#. :kbd:`Ctrl` を押しながらマウスを使って次のテキストを選択する
#. 必要なだけ繰り返す

追加選択モードで、キーボードを使って連続しない項目を選択する手順：

#. 最初のテキストを選択
#. :kbd:`Shift` + :kbd:`F8` を押すか、Sattus バーの :guilabel:`Selection mode`
   図像をクリックし、一覧から :menuselection:`&Adding selection` を選択する
#. :kbd:`Shift` を押しながら次のテキストを選択
#. 必要なだけ繰り返す

.. admonition:: 読者ノート

   この :kbd:`Shift` 押しを忘れやすい。

これにより選択テキストをコピー、削除、スタイル変更などをすることが可能だ。選択し
たテキストでの作業が終了したら :kbd:`Esc` を押して追加選択モードを終了する。

Selecting a vertical block of text
----------------------------------------------------------------------

複数行にまたがる縦長のテキストブロックを選択するにはブロック選択モードを使う。

* メニューから :menuselection:`&Edit --> Selection &Mode --> &Block Area` を選択
* キーバインド :kbd:`Alt` + :kbd:`Shift` + :kbd:`F8`
* Status バー選択モード欄クリックから :menuselection:`&Block selection` を選択

これでマウスまたはキーボードを使って選択範囲を強調できる。

Cutting, copying, and pasting text
======================================================================

Writer でのテキストの切り取りとコピーは他のアプリケーションでのそれに似ている。
ドラッグやメニュー選択、図像、キーバインドを使って、文書内や異なる文書間でテキス
トをコピーしたり移動したりする。また、Web ページなど Writer でない文書からテキス
トをコピーして Writer 文書に貼り付けることも可能だ。

* 移動は選択テキストをドラッグ＆ドロップ
* コピーは :kbd:`Ctrl` を押しながら選択テキストをドラッグ
* キーバインドやメニューを使用する方法もある

テキストを貼り付ける場合、貼り付け元と貼り付け方法によって結果が異なる。Paste コ
マンドを実行すると貼り付けられたテキストは元の書式（太字や斜体など）を維持する。

Web サイトやその他の種類の文書から貼り付けられたテキストは、貼り付け時に書式の一
部として枠や図表に自動的に配置される場合がある。結果が気に入らない場合は Undo し
ろ。

貼り付けられたテキストに挿入位置の様式を継承させる方法は次のいずれか：

* メニュー :menuselection:`&Edit --> Paste &Special -->` を開く
* :guilabel:`Paste` ボタン右の▼をクリック
* キーバインド :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`V`

それから :guilabel:`&Unformatted text` や :guilabel:`&Paste Unformatted text` を
選択する。キーバインド :kbd:`Ctrl` + :kbd:`Alt` + :kbd:`Shift` + :kbd:`V` でも書
式なしテキストを直接貼り付けることが可能だ。

Paste Special メニューの選択肢は貼り付けるテキスト（またはその他のオブジェクト）
の出処や書式によって異なる。

Finding and replacing text
======================================================================

Writer には文書内のテキストをすばやく検索するための :guilabel:`Find` ツールバー
と :guilabel:`Find and Replace` ダイアログボックスの二つの方法がある。これらを使
えば次のことが可能だ：

* 単語や句を検索し、置き換える
* ワイルドカードと正規表現を使って検索を微調整する
* 特定の属性や書式を検索して置換する
* 段落スタイルを検索して置換する

後半の操作については :doc:`Chapter 3 <writer03>` を見ろ。

Using the Find toolbar
----------------------------------------------------------------------

LibreOffice 初期設定では :guilabel:`Find` ツールバーはメインウィンドウの下部、
Status Bar のすぐ上に繋留している。ツールバーが表示されていない場合は次のいずれ
かをしろ：

* メニューから :menuselection:`&View --> &Toolbars --> &Find` を選択
* メニューから :menuselection:`&Edit --> &Find...` を選択
* キーバインド :kbd:`Ctrl` + :kbd:`F`

:guilabel:`Find` ツールバーの使い方は左半分は見ればわかる。

:guilabel:`Find and Replace` ダイアログボックスを開くには :guilabel:`Match Case`
の右にある図像をクリックする。

:guilabel:`Find` ツールバーを閉じるには、左側のバツ印をクリックするか、検索欄に
フォーカスがあるときに :kbd:`Esc` を押す。

Using the Find and Replace dialog
----------------------------------------------------------------------

:guilabel:`Find and Replace` ダイアログボックスを開く方法：

* キーバインド :kbd:`Ctrl` + :kbd:`H`
* メニュー :menuselection:`&Edit --> Find and Rep&lace...` を選択
* :guilabel:`Find` ツールバーの :guilabel:`Find and Replace` 図像をクリック

:guilabel:`Other &options` を展開しておく。

#. :guilabel:`Find` 欄に検索条件を入力
#. テキストを別のテキストに置き換えるならば :guilabel:`Replace` 欄に新しいテキス
   トを入力
#. 大文字小文字を一致させる、単語全体のみを一致させるなど、さまざまな選択肢を取
   ることが可能。

   その他のオプションには、

   * 選択したテキスト内のみを検索する
   * 現在のキャレット位置から文書の先頭に向かって検索する
   * 類似した単語を検索する
   * コメント内を検索する
   * 正規表現（ワイルドカード）を使用する

   などがある。
#. :guilabel:`Find &Next` をクリックして検索条件の最初の項目を検索
#. :guilabel:`&Replace` をクリックしてテキストを置換するか、:guilabel:`Find
   &Next` をまたクリックして次の合致まで飛ぶ

.. tip::

   :guilabel:`Find &All` と :guilabel:`Relace A&ll` を使えば一括処理が可能。

.. note::

   :guilabel:`Replace A&ll` 操作の直前にファイルを保存しておくべし。一括置換失敗
   時に Undo コマンドを出現回数分反復する手間を削れる。

Inserting special characters
======================================================================

:guilabel:`Standard` ツールバー :guilabel:`Special Character` 図像をクリックする
とドロップダウンで最近使用した特別文字の一覧が示され、選択すると当該文字がキャ
レット位置に挿入される。また、ここにある :guilabel:`More Characters...` を押すと
ダイアログボックス :guilabel:`Special Characters` が開く。

:menuselection:`&Insert --> S&pecial Character...` コマンドでダイアログボックス
:guilabel:`Special Characters` が開く。

.. tip::

   * 文字の詳細を表示するにはその文字をクリックする。
   * 文字を挿入してダイアログを開いたままにするには、その文字をダブルクリックす
     る。
   * 文字を挿入してダイアログを閉じるには、クリックしてから :guilabel:`&Insert`
     をクリックする。

フォントによって含まれる特殊文字は異なってくる。

Inserting non-breaking spaces, hyphens, and more
----------------------------------------------------------------------

さまざまな書式印を挿入することが可能だ。これらの目印のほとんどはキーバインドが割
り当てられている。すべてメニュー :menuselection:`&Insert --> Formattin&g Mark
-->` から可能だ。

Non-breaking space
   単語二つが行末で区切られないようにするには、両単語の間に空白を入力するときに
   :kbd:`Ctrl` + :kbd:`Shift` を押す。
Non-breaking hyphen
   例えば ``123-4567`` のように、ハイフンを行末に表示したくない場合にこのコマン
   ドを使用する。キーバインド :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`-` を使う。
Soft Hyphen
   このコマンドは行末で単語を区切る位置を指定する。単語が行末にない場合、ハイフ
   ンは表示されない。キーバインド :kbd:`Ctrl` + :kbd:`-` でこれを挿入する。
Narrow No-break Space
   通常の空白ほど広くない非改行空白を入力するには、:kbd:`Alt` + :kbd:`Shift` を
   押しながら :kbd:`Space` を押す。
No-width Optional Break
   :kbd:`Ctrl` + :kbd:`/` を使用すると、単語内に不可視の空白を挿入することがで
   き、その空白が行の最後の文字である場合に改行となる。|CTL| が有効である場合に
   使用可能。
Word Joiner
   行末でまとまる単語内に見えない空白を挿入する。

|CTL| が有効である場合には次の追加的マークが有効になる：

* Left-to right
* Right-to-Left

Inserting en and em dashes
----------------------------------------------------------------------

.. admonition:: 読者ノート

   :doc:`Calc Guide Chapter 2 <../calc-guide/calc02>` の対応する節を参照しろ。

Checking spelling and grammar
======================================================================

各言語において、それが利用可能である場合、次の四つが既定でインストールされる：

* 綴字検査機能
* 文法検査機能
* 分綴辞書
* 類語辞書

綴字検査機能は文書内の各単語がインストールされている辞書にあるかどうかを判定す
る。文法検査機能は綴字検査機能と組み合わせて動作する。

* 文法検査機能は :guilabel:`Spelling` ダイアログボックスで有効無効を決めることが
  可能だ。
* 綴字と文法は任意の時点で自動的に検査することが可能だ。

Spelling
----------------------------------------------------------------------

綴字の自動検査を有効にするには、次のいずれかを実行する：

* :menuselection:`&Tools --> &Automatic Spell Checking` をオンにする
* :guilabel:`Standard` ツールバーの :guilabel:`Auto Spellchec&k` をオンにする
* :guilabel:`Options` ダイアログボックスを開いて

  #. :menuselection:`Language Settings --> Writing Aids` ページへ行く
  #. 最後の枠内 :guilabel:`Check spelling as you type` をオンにする
  #. :guilabel:`&OK`

自動綴字検査というのは、テキストに含まれる単語を検査して、辞書にない単語に赤波線
を引くというものだ。このような単語を右クリックすると訂正候補メニューが現れる。

* どれかを選択すれば、下線部の単語をそれで置き換える。
* ここにない単語に置き換えたい場合には :menuselection:`&Spelling...` を選択して
  何かをする。
* 辞書にない場合には :menuselection:`&Add to dictionary` で対応する。

.. admonition:: 読者ノート

   この右クリックメニューは四区画に分割されている。内容はそれぞれこうだ：

   * 第一区画：訂正候補
   * 第二区画：文書変更追跡固有コマンド
   * 第三区画：自動訂正コマンド
   * 第四区画：テキストの言語設定コマンド

   詳細は本書参照。私が英文を Writer で執筆することはないので深く踏み込まない。

Spelling and grammar
----------------------------------------------------------------------

文書またはテキスト選択範囲の綴字と文法の複合検査を行うには次のいずれかを実行す
る：

* :menuselection:`&Tools --> &Spelling...` を選択
* :guilabel:`Standard` ツールバーの :guilabel:`Check Spelling` 図像をクリック
* :kbd:`F7` を押す

この機能を使用するには、適切な辞書がインストールされている必要がある。

このコマンドはキャレット位置から先の文書または選択テキストのいずれかを検査する。
認識できない単語が見つかったり、組み込まれている文法規則に違反したりすると、ダイ
アログボックス :guilabel:`Spelling` が開く。検査が文書の最後に達したときに、文書
の先頭からやり直すかどうかを選択可能だ。

ダイアログボックスの左下で :guilabel:`Chec&k grammer` をオンにすると、検出された
文法の誤りも表示される。

:guilabel:`Text langua&ge`
   綴字検査に使用する言語をこのドロップダウンリストから選択する。
:guilabel:`&Not in dictionary`
   誤りを含む文がこの窓に表示される。認識できない単語が見つかるとその単語が強
   調表示される。文や単語をここで編集することが可能。
:guilabel:`&Suggestions`
   強調表示された単語の置換候補が示される。単語を選択して後述の訂正ボタンを押せ
   ばいい。

   文法上の誤りの場合、選択肢は一つとなる。提案を受理するには :guilabel:`Change`
   を選択する。
:guilabel:`&Ignore Once`, :guilabel:`I&gnore All`, :guilabel:`Add to &Dictionary`
   これらのボタンは押すと上記のコンテキストメニューの項目と同じ効果が得られる。
:guilabel:`Ignore Rule`
   文法を検査する場合、提案された変更を無視することも可能。
:guilabel:`Co&rrect`
   未知の単語を提案された単語で置換するか、提案された文法上の変更を加える。
:guilabel:`Correct A&ll`
   その単語のすべての出現箇所を選択された単語で置換する。文法検査には使用不能。
:guilabel:`Add to &AutoCorrect`
   不正確な単語と選択された置換候補の組み合わせを AutoCorrect 置換表に追加する。
   文書には変更を加えない。
:guilabel:`&Undo`
   このダイアログボックスからの変更を元に戻す。:guilabel:`Co&rrect` ボタンを使用
   して単語を置換した場合は使用不能。
:guilabel:`&Options...`
   :guilabel:`Options` ダイアログボックスを開く。使用者定義の辞書を選択したり、
   綴字検査規則を設定したりする。

Grammar
----------------------------------------------------------------------


* :menuselection:`&Tools --> &Automatic Spell Checking` をオンにする
* :guilabel:`Standard` ツールバーの :guilabel:`Auto Spellchec&k` をオンにする
* :guilabel:`Options` ダイアログボックスを開いて

  #. :menuselection:`Language Settings --> Writing Aids` ページへ行く
  #. 最後の枠内 :guilabel:`Check spelling as you type` をオンにする
  #. :guilabel:`&OK`

初期設定では先述の :guilabel:`Check spelling as you type` はオンになっている。こ
のオン状態が自動綴字検査が機能するために必要だ。また、:menuselection:`&Tools -->
Check Spelling...` コマンドを使っていつでも文法を検査したり、入力中の文法検査を
無効にすることも可能だ。

入力中の文法検査が有効な場合、検出された誤りは青い波線で下線表示される。この線を
右クリックするとコンテキストメニューが開く。これも四区画からなる：

* 第一区画は文法違反が疑われる箇所を列挙する。
* 第二区画には修正案が提示される。これを選択すると波線テキストが提示内容に置換さ
  れる。この欄が空白の場合、選択すると、エラーの原因となっている余計な空欄が削除
  される。
* 第三区画では、表示されたエラーを無視するか、:guilabel:`Spelling` ダイアログ
  ボックスを開くかを選択する。
* 第四区画では、選択範囲や段落の言語を設定する。

:guilabel:`More...` リンクは誤り詳細情報 URL がブラウザーで開く。

.. tip::

   波下線に別の色を選択する方法は :doc:`Chapter 20 <writer20>` で会得できる。

English sentence checking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

追加的文法検査ツールを :guilabel:`Options` ダイアログボックスの
:menuselection:`Language Settings --> English Sentence Checking` ページで選択可
能だ。また、メニュー :menuselection:`&Tools --> &Extensions...` で
:guilabel:`English spelling dictionaries` を選択し、:guilabel:`Options` ボタンを
クリックすることも可能だ。

:guilabel:`English Sentence Checking` ページで、検査項目、報告される項目、自動的
に変換される項目を選択する。追加的文法検査を選択した後、効力を発するには
LibreOffice を再起動するか、文書を再読み込みする必要がある。

Grammar checking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`&Possible mistakes`
   例を挙げるしかないが ``it's``, ``he don't``, ``this things`` などの誤りを検査
   する。
:guilabel:`&Capitalization`
   文頭の大文字小文字を検査する。
:guilabel:`&Word duplication`
   既定の 'and', 'or', 'for', 'the' だけでなく、単語すべての重複を検査する。
:guilabel:`Parent&heses`
   括弧と引用符が正しく対になっているか検査する。

Punctuation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Wor&d spacing`
   単語間に空白文字がちょうど一つあるかどうかを検査する。二重、三重空白の実例を
   示す。それを超える分は検査を複数回実行しろ。
:guilabel:`&Quotation marks`
   引用符の対が組版上正しいか、つまり、開始と終了の引用符が正しいものであるかを
   検査する。
:guilabel:`Sentence spacin&g`
   文間に空白文字がちょうど一つあるかどうかをチェックし、余分な空白文字が見つ
   かった場合はそれを示す。
:guilabel:`&Apostrophe`
   アポストロフィーを正しい組版文字に置き換える。
:guilabel:`Mo&re spaces`
   単語と文の間に二つ以上の余分な空白文字がないか調べる。
:guilabel:`&Em dash`, :guilabel:`En &dash`
   （読者ノート：ダッシュに関する基礎知識は先述のリンク先を参照）

   これらのオプションはそれぞれ、空白でない em ダッシュを空白の en ダッシュに置
   き換えたり、空白の en ダッシュを空白でない em ダッシュに置き換えたりする。
:guilabel:`&Multiplication sign`
   乗算記号として使われる x を正しい組版記号に置き換える。
:guilabel:`E&llipsis`
   連続する三つのピリオドを正しい組版記号に置き換える。
:guilabel:`Min&us sign`
   ハイフンを負の符号に置き換える。

Others
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Convert &to metric`, :guilabel:`Convert to &non-metric`
   度量衡変換。
:guilabel:`Thousands separation &of large numbers`
   文書のロケール設定に応じて、有効数字が五桁以上の数値を、カンマ ``,`` を桁区切
   り文字とするか、狭い空白文字を使う :abbr:`ISO (International Organization for
   Standardization)` 形式にして変換する。

Using Language Tool
======================================================================

Language Tool は <https://languagetool.org/> が備えている多言語文法、スタイル、
綴字検査ツールだ。Writer は上記の内蔵文法検査機能とともに、このツールを文法検査
に使用可能だ。Language Tool を有効にすると、:guilabel:`Options` ダイアログボック
スの :menuselection:`Language Settings --> Writing Aids` ページ内
:guilabel:`&Available Language Modules` 一覧に表示される。

Using synonyms and the thesaurus
======================================================================

#. 単語を右クリック
#. コンテキストメニューの :menuselection:`Synony&ms -->` から代替語句のサブメ
   ニューが表示される
#. サブメニューの単語または語句を選択

文書内の強調表示された単語または語句が置き換わる。サブメニューの最下部にある
:menuselection:`&Thesaurus...` を選択すると、類語ダイアログボックスが開く。

.. note::

   この機能は現在の言語に類語辞書がインストールされていない場合に無効だ。

.. admonition:: 読者ノート

   英語の文書でこの機能を駆使して己の語彙を豊富にする用途が考えられる。

Hyphenating words
======================================================================

行末をまたぐ単語の分綴は Writer が自動的に行う（スタイルと辞書を使用する）方法
と、必要に応じて手動で条件付き (soft) hyphen を挿入する方法がある。あるいは分綴
をまったく使わないことも可能だ。

Automatic hyphenation
----------------------------------------------------------------------

このやり方はスタイルを使用し、後述する :guilabel:`Options` ダイアログボックスの
指定を上書きする。

単語の自動分綴オンオフを切り替える手順：

#. Siedbar の :guilabel:`Styles` タブをクリック
#. :guilabel:`&Edit Styles...` 図像をクリック
#. 木から :guilabel:`Default Paragraph Style` を右クリック
#. :menuselection:`Modify` を選択
#. :guilabel:`Paragraph Style` ダイアログで :guilabel:`Text Flow` タブをクリック
#. :guilabel:`Hyphenation` で :guilabel:`Automatically` を切り替える

   * オンの場合、行う時点の基準を設定することも可能。
#. :guilabel:`&OK`

Default Paragraph Style で分綴をオンにすると、このスタイルに基づくすべての段落ス
タイルに影響する。分綴が有効にならないように、他のスタイルを個別に変更することが
可能だ（例えば、見出しに対してはしないようにする）。この話題は :doc:`Chapter 8
<writer08>` と :doc:`Chapter 9 <writer09>` で述べられる。

Hyphenation options
----------------------------------------------------------------------

自動分綴が有効である場合、次の項目を設定可能だ：

:guilabel:`Don't hyphenate words in &CAPS`
   すべて大文字で書かれた単語は分綴しない。
:guilabel:`Don't hyphenate the &last word`
   段落の最後の単語に分綴しない。
:guilabel:`C&haracters at line end`
   行末に残す最小文字数。
:guilabel:`Cha&racters at line begin`
   分綴適用後、行頭に来る部分の最小文字数。
:guilabel:`&Maximum consecutive hyphenated lines`
   分綴が可能である連続する行の最大数。
:guilabel:`&Minimum word length in characters`
   分綴可能最小単語長を文字数で指定。
:guilabel:`Hyphenation &zone`
   単語を分綴できない水平空白の長さを指定する。この値を指定すると、両端揃えテキ
   ストでは単語間の間隔が大きくなり、そうでないテキストでは段落余白からの距離が
   大きくなる。

:guilabel:`Options` ダイアログボックスの :menuselection:`Language Settings -->
Writing Aids` ページ内 :guilabel:`Options` にも分綴設定項目がある。

* 段落スタイルに特定の設定がない場合に適用される。
* 段落スタイルで分綴がオンになっている場合に限り有効。

:guilabel:`Hyphenate without inquiry`
   辞書が認識しない単語を手動で分綴する要求をさせない。オフにすると hyphen を手
   動で入力できるダイアログボックスが開く。
:guilabel:`Hyphenate special regions`
   脚注、ヘッダー、フッターでも分綴が機能する。

Manual hyphenation
----------------------------------------------------------------------

手動で単語を分綴する際、通常の hyphen を使用してはいけない。通常のそれはテキスト
を加除修正したり、余白やフォントサイズを変更したときに、その単語が行末でなくなっ
ても表示されたままになる。必ず *soft hyphen* を使え。

単語内に soft hyphen を挿入するには、それを表示したい位置をクリックして次のいず
れかを実行する：

* キーバインド :kbd:`Ctrl` + :kbd:`-`
* メニューから :menuselection:`&Insert --> Formattin&g Mark --> Insert S&oft
  Hyphen` 選択

この段落の自動分綴がオフになっていても、行末にある単語はこの位置で分綴される。

Using AutoCorrect
======================================================================

AutoCorrect 機能には、よくある誤植の長い目録を搭載しており、自動修正に使われる。
また、特殊文字、絵文字、その他の記号を挿入するためのコードも搭載している。独自の
特殊文字を追加することも可能だ。

AutoCorrect の機能をいくつか無効にしたり、他の機能を変更したり、完全にオフにした
りすることも可能だ。オフにするにはメニューから
:menuselection:`&Tools --> AutoCorr&ect --> &While Typing` をオフにする。

独自の訂正や特殊文字を追加したり、LibreOffice に付属の訂正や特殊文字を変更したり
する方法：

#. :menuselection:`&Tools --> AutoCorr&ect --> &AutoCorrect Options...` を選択
#. :guilabel:`AutoCorrect` ダイアログボックスが開く
#. :guilabel:`Replace` タブで、どの文字列をどのように修正するかを定義

特定の綴りを置き換えるのをやめさせる手順：

#. :guilabel:`Replace` タブで置換対応を選択
#. :guilabel:`&Delete` を押す

新しい綴りを目録に追加する手順：

#. :guilabel:`Replace` タブでの :guilabel:`Repla&ce` 欄と :guilabel:`&Width` 欄
   に綴りを入力
#. :guilabel:`&New` を押す

:guilabel:`AutoCorrect` ダイアログボックスについては :doc:`Chapter 4 <writer04>`
でも述べられる。

Using Word Completion
======================================================================

Word Completion が有効になっている場合、Writer は著者が入力しようとしている単語
を推測し、単語を補完しようとする。著者が :kbd:`Enter` を押せばこの提案を受け入れ
る。

Word Completion をオフにするには：

#. :menuselection:`&Tools --> AutoCorr&ect --> &AutoCorrect Options...` を選択
#. :guilabel:`Word Completion` タブを選択
#. :guilabel:`Enable word &completion` をオフにする

このタブのページで単語補完をカスタマイズ可能だ：

* 受け付けた単語の後に空白を自動的に追加する。
* 入力中にテキストを補完するのではなく、提案された単語をツールチップ表示する。
* 文書の作業中に単語を収集し、後で他の文書で使用するために保存するか、文書を閉じ
  るときに目録から削除するかを選択する。
* 入力候補を受け付けるキーを変更する。
* 単語補完のために記憶される最大単語数と最小単語の長さを変更する。
* 単語補完目録から特定の補完対応を削除する。

.. note::

   自動単語補完は文書内でニ回目に単語を入力したときにしか行われない。

.. admonition:: 利用者ノート

   Google 日本語入力を愛用しているならばこの機能は使わない。

Using AutoText
======================================================================

AutoText を使用すると、テキスト、図表、フィールド、画像、その他の項目を再利用で
きるように保存し、キーバインドを定義して簡単に呼び出すことが可能になる。例え
ば、"Senior Management "と毎回入力するのではなく、"sm" と入力し、:kbd:`F3` を押
すと、その単語が挿入されるように AutoText を設定することが可能だ。

AutoText はフィールドに割り当てると特に強力だ。:doc:`Chapter 17 <writer17>` を読
め。

Creating AutoText
----------------------------------------------------------------------

テキストを AutoText として保存する方法：

#. テキストを文書に入力
#. それを選択
#. メニューから :menuselection:`Tools --> AutoTe&xt...` を選択するかキーバインド
   :kbd:`Ctrl` + :kbd:`F3`
#. :guilabel:`AutoText` ダイアログボックスが開く
#. :guilabel:`Na&me` 欄に AutoText の名前を入力する
#. AutoText の品目（例えば :guilabel:`My AutoText` など）を選択
#. :guilabel:`AutoTe&xt` ドロップダウンをクリック
#. 次のいずれかを選択する：

   * :menuselection:`New`: どこに挿入されても特定の書式を保持
   * :menuselection:`New (text onlly)`: 挿入位置周辺の書式を適用
#. :guilabel:`&Close`

.. tip::

   ドロップダウンメニューが :menuselection:`Import...` しかない場合、名前か選択
   に不備がある。

図表を AutoText として保存する手順：

#. 図表を作成し、必要な書式を設定する。
#. 図表を選択し、メニューから :menuselection:`Tools --> AutoTe&xt...` を選択する
   かキーバインド :kbd:`Ctrl` + :kbd:`F3`
#. AutoText の名前を入力する。または推奨されるショートカットを修正し、AutoText
   項目の品目を選択する。
#. :menuselection:`AutoText --> New` を選択（図表の書式を保持したい）
#. :guilabel:`&Close`

Inserting AutoText
----------------------------------------------------------------------

AutoText を挿入するには、登録されているショートカットを入力して :kbd:`F3` を押
せ。

Printing a list of AutoText entries
----------------------------------------------------------------------

.. admonition:: 読者ノート

   印刷しないので割愛。

Changing the case of selected text
======================================================================

テキストの大文字と小文字をすばやく変更するには、テキストを選択し、メニューから
:menuselection:`&Format --> Te&xt -->` から関連項目のいずれかを選択する。

.. admonition:: 読者ノート

   サブメニューの第五区画以降の項目。

Writer には Title Case を自動的に行う方法はない。

:menuselection:`&Format --> Te&xt -->` メニューには、太字、斜体、上付き文字など
の手動書式設定オプションもある。アジア言語対応が有効になっている場合は、半角、全
角、ひらがな、カタカナなどのオプションもある。

:guilabel:`Character` ダイアログボックスや文字スタイルを使用して、テキストの大文
字と小文字を変更することも可能だ。

#. メニューから :menuselection:`F&ormat --> C&haracter...` を選択
#. :guilabel:`Font Effects` タブをクリック
#. :guilabel:`&Case` ドロップダウンリストから大文字小文字の種類を選択
