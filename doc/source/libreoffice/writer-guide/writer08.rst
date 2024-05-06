======================================================================
Writer Guide Chapter 8, Introduction to Styles ノート
======================================================================

.. include:: ./writer-inc.txt

.. contents:: 章見出し
   :depth: 3
   :local:

What are styles?
======================================================================

ほとんどの人は物理的属性に従って文書を書くことに慣れている。例えば、フォント族、
フォントサイズ、重み (e.g. Helvetica 12 pt, bold) を指定するといった具合だ。対照
的に、スタイルは **論理的な** 属性だ。例えば、フォント特性の集合を定義し、それを
`Title` や `Heading 1` と呼ぶことができる。スタイルとは、テキストがどのように見
えるかから、テキストが何であるかに見方を転換することだ。

.. admonition:: 読者ノート

   スタイルとは何かと問われたら、テキストに対する書式設定の性質の集合だと答えれ
   ばいい。フォントサイズがいくらだとか、色が何であるとかなどの集合だ。

Why use styles?
----------------------------------------------------------------------

スタイルは文書の一貫性を高めるのに役立つ。たとえば、すべての段落の字下げを変更し
たり、すべての表題のフォントを変更したりすることも可能だ。長い文書ではこの単純な
作業は法外なものになる場合がある。スタイルがこの作業を容易にする。Writer はさら
に、目次の作成など、他の目的にもスタイルを使用する。

:ref:`writer08-anchorA` を見ろ。

Style categories
----------------------------------------------------------------------

Writer にはスタイル区分が六つある：

* `Paragraph` スタイルは段落全体に適用され、目次の作成などにも使用される。
* `Character` スタイルは段落内のテキストブロックに適用され、段落スタイルの例外と
  なる。
* `Page` スタイルはページの書式設定（ページサイズ、余白など）に適用される。
* `Frame` スタイルは枠や画像に適用される。
* `List` スタイルはアウトライン、番号付き一覧、箇条書き一覧に適用される。
* `Table` スタイルはデータ表の見れくれに影響する。

段落は文書すべての構成要素だ。見出しは段落であり、ヘッダー、フッター、番号付き一
覧の項目も段落だ。したがって、段落スタイルは最も頻繁に使われるスタイルであり、こ
の章で最も詳しく扱う。

.. note::

   手動書式設定（直接書式設定）はスタイルを上書きする。スタイルを適用して手動書
   式を取り除くことはできない。

   手動書式を取り除くには、対象テキストを選択して次のいずれかを行う：

   * |MenuBar| から :menuselection:`&Format-->Clear &Direct Formatting` を選択
   * 右クリックメニューから :menuselection:`Clear &Direct Formatting` を選択
   * キーバインド |Ctrl+M|

The Styles deck in the Sidebar
======================================================================

スタイル管理は主に |Sidebar| |StylesDeck| から行える。ここではスタイルの適用、変
更、作成を行うことが可能だ。

まず、次のいずれかを行う：

* |Sidebar| の :guilabel:`Styles` 図像をクリック
* |MenuBar| から :menuselection:`St&yles-->Manage St&yles` を選択
* キーバインド |F11|

|StylesDeck| 上部にある最初の六つの図像はスタイルの品目を選択する。これらの図像
のいずれかをクリックすると、段落スタイルや文字スタイルなど、その品目のスタイル目
録が示される。

甲板下部にある :guilabel:`Show preview` をオンにするとスタイル名が書式の例として
表示される。:guilabel:`Spotlight` をオンにして、|Writer09| で述べられるスタイル
スポットライトを活動開始する。

Filtering the visible styles
----------------------------------------------------------------------

|StylesDeck| 下部にあるドロップダウンメニューでスタイル一覧のフィルターを選択す
る。

執筆初期段階では :guilabel:`All Styles` で使用可能なすべてのスタイルにアクセスで
きるようにしておき、そのうちのいくつかを隠すようにするといい：

#. 除外する各スタイルを |Ctrl| を押しながらクリックで選択
#. これらの項目いずれかを右クリック
#. :menuselection:`&Hide` を選択

文書が発展するにつれて、表示される一覧をすでに使用されているスタイルだけにするの
が手っ取り早い。これには :guilabel:`Applied Styles` で絞り込む。

カスタムスタイルのみを適用したい文書で作業する場合は :guilabel:`Custom Styles`
を代わりに選択する。

:guilabel:`Hierarchical` ビューはどのスタイルが一緒にリンクされているかを明らか
にするので、スタイルを修正するときに最も便利だ。これついては |Writer09| で議論
される。

:guilabel:`Paragraph Styles` ビューではドロップダウンメニューにさらにいくつかの
絞り込みオプションがあり、たとえば :guilabel:`Text Styles` や :guilabel:`Special
Styles` などに限り表示することが可能だ。

Applying styles
======================================================================

スタイルは |Sidebar| の |StylesDeck| を使ってたやすく適用できる。他の方法を使用
して適用することが可能なスタイルもある。

Applying paragraph styles
----------------------------------------------------------------------

.. |StylesMenu| replace:: :menuselection:`St&yles-->`
.. |SetParagraphStyle| replace:: :guilabel:`Set Paragraph Style` ドロップダウンリスト

段落スタイルはいくつかの方法で適用できる：

* |Sidebar| |StylesDeck| |ParagraphStylesTab|
* |MenuBar| |StylesMenu| 以下（普通のスタイル限定）
* コンテキストメニュー（わずか）
* |FormattingToolbar| と |FormattingStylesToolbar| の左端にある
  |SetParagraphStyle|
* |Sidebar| |PropertiesDeck| 上部にある |SetParagraphStyle|
* |FormattingStylesToolbar| （普通のスタイル限定）
* |Sidebar| |StylesDeck| :guilabel:`Fill Format Mode` 図像
* キーバインド |Ctrl| + :kbd:`1` から |Ctrl| + :kbd:`5` (`Heading 1`, ...,
  `Heading 5`)

Using the Styles deck on the Sidebar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

段落にキャレットを置き、|Sidebar| |StylesDeck| |ParagraphStylesTab| でスタイル名
をダブルクリックする。複数の段落を選択して、それらに同じスタイルを一括適用可能。

Using the Styles menu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|MenuBar| の |StylesMenu| には、段落、文字、一覧の各スタイルのほか、スタイルを作
成、編集、管理するためのクイックリンクが用意されている。

|StylesMenu| 以下にスタイルを追加することが可能だ。|Writer20| を見ろ。

段落スタイルを適用するには：

#. 対象段落にキャレットを置く
#. :menuselection:`St&yles-->[name of paragraph style]` を選択

このメニューの他の選択肢についてはこの章で後述。

Using the context (right-click) menu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

段落内の任意の場所で右クリックメニューを開く。:menuselection:`P&aragraph-->` を
指せ。サブメニューにはよく使われる段落スタイルがいくつか含まれている。このサブメ
ニューにも段落スタイルを追加することが可能だ。|Writer20| を見ろ。

Using the Set Paragraph Style list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

文書内で段落スタイルが使用されている場合、その名前は次の場所に共通してある
|SetParagraphStyle| に表示される：

* |FormattingToolbar| 左端付近
* |FormattingStylesToolbar|
* |Sidebar| |PropertiesDeck| 上部

このドロップダウンリストらスタイルを適用するには：

#. 変更したい段落にキャレットを置く
#. 矢印をクリックしてスタイルの一覧をドロップダウン
#. 所望のスタイルを選択

Using the Formatting (Styles) toolbar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|FormattingStylesToolbar| には一般的な段落、文字、一覧のスタイルが含まれている。

段落スタイルを適用するには、段落にキャレットを置き、ツールバーの該当するボタンを
クリックする。このツールバーにもスタイルを追加できる。|Writer20| を見ろ。

Using Fill Format Mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fill Format Mode を使用すると、|StylesDeck| に戻って毎回ダブルクリックしなくて
も、多くの領域にすばやくスタイルを適用できる。散在する段落や単語などの項目を同じ
スタイルで整形するのに便利な方法で、最初に複数の選択を行ってからすべての項目にス
タイルを適用するよりも使いやすい。

#. |Sidebar| |StylesDeck| を開く
#. コピーするスタイルを選択し、右上の :guilabel:`Fill Format Mode` 図像をクリッ
   ク
#. 段落、ページ、枠のスタイルを適用するには、マウスを段落、ページ、枠の上に置い
   てクリック

   * 文字スタイルを適用するにはマウスボタンを押したまま文字を選択する。
   * 単語をクリックするとその単語に文字スタイルが適用される。
#. そのスタイルのすべての変更を行うまで、手順 3 を繰り返す。
#. モードを終了するには、図像をもう一度クリックするか |Esc| を押す

Using keyboard shortcuts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

スタイルを適用するためのキーバインドがいくつか定義済みだ。たとえば、

* |Ctrl| + :kbd:`0` は `Body Text`
* |Ctrl| + :kbd:`1` は `Heading 1`
* |Ctrl| + :kbd:`2` は `Heading 2`

をそれぞれ適用する。

これらのキーバインドを変更したり、独自のキーバインドを定義したりすることも可能。
|Writer20| を見ろ。

Applying character styles
----------------------------------------------------------------------

文字スタイルを適用するには、文字または単語を選択し、以下のいずれかから文字スタイ
ルを適用する：

* |MenuBar| |StylesMenu| 以下（わずか）
* |Sidebar| |StylesDeck| |CharacterStylesTab|
* コンテキストメニュー（わずか）
* |FormattingStylesToolbar|

.. tip::

   文字スタイルを適用する前に、直接書式設定を削除する必要がある場合がある。その
   場合には対象テキストを選択して Clear Direct Formatting コマンドを実行する。

Using the Styles menu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|MenuBar| の |StylesMenu| には、段落、文字、一覧の各スタイルのほか、スタイルを作
成、編集するためのクイックリンクが用意されている。文字スタイルを適用するには：

#. 文字を選択する
#. :menuselection:`St&yles-->[name of character style]` を選択

|StylesMenu| にもスタイルを追加することが可能だ。|Writer20| を見ろ。

Using the Styles deck on the Sidebar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|StylesDeck| を開き、上部の |CharacterStylesTab| をクリックする。利用可能な文字
スタイルの一覧が表示される。文字スタイルを適用するには：

#. スタイルを適用したいテキストを選択するか、一つの単語にキャレットを合わせる
#. |StylesDeck| で適切な文字スタイルをダブルクリック

.. note::

   複数の単語に文字スタイルを適用するには、変更するテキストをすべて選択する必要
   がある。単一の単語にスタイルを適用するには、その単語にキャレットを置くだけで
   よい。一方、段落スタイルはキャレットが置かれた段落全体に適用される。

Using the context (right-click) menu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

テキストのブロックを選択するか、単一単語にキャレットを置き、右クリックしてコンテ
キストメニューを開く。:menuselection:`C&haracter-->` を指す。サブメニューにはよ
く使用される文字スタイルがいくつか含まれている。このサブメニューに文字スタイルを
追加することもできる。|Writer20| を見ろ。

Using the Formatting (Styles) toolbar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|FormattingStylesToolbar| には一般的な段落、文字、一覧のスタイルが含まれている。

文字スタイルを適用するには、テキストを選択するか、単語にキャレットを置いて、ツー
ルバーの関連する図像をクリックする。

このツールバーにもスタイルを追加できる。|Writer20| を見ろ。

Removing or replacing character styles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

テキストから文字スタイルの書式設定を削除したり、文字スタイルを別のスタイルに変更
したりするには、次のようにする：

#. テキストを選択
#. |Sidebar| |StylesDeck| で、上部の |CharacterStylesTab| をクリック
#. 必要な文字スタイルをダブルクリックするか、文字スタイルを削除するのに
   :guilabel:`No Character Style` をダブルクリック

Applying frame styles
----------------------------------------------------------------------

文書に画像などの物体を挿入すると、その周りには見えない枠が自動的につく。枠スタイ
ルを追加して多様性を持たせたい著者もいる。例えば、写真用の枠スタイルと、線画など
の他の画像用の枠スタイルを用意することが可能だ。写真用の枠にはドロップシャドウを
設け、線画用の枠には境界しか付けないことも可能だ。

枠にスタイルを適用するには：

#. 枠を選択
#. |Sidebar| |StylesDeck| 上部の |FrameStylesTab| をクリック
#. 必要な枠スタイルをダブルクリック

枠にスタイルを適用すると、枠をいいように修正できるようになる。枠の意匠のほとんど
はスタイルで設定できるが、以下のオプションは手動で設定する必要がある：

* 繋留：枠をページの他の中身に対してどのように配置するか。

  * :menuselection:`F&ormat-->Anc&hor-->`
  * |Writer11| を見ろ。
* 配置：物体のスタック内での枠の位置

  * :menuselection:`F&ormat-->A&rrange-->`
  * |Writer11| を見ろ。
* ハイパーリンクの追加：枠をクリックすると Web ページなどの他の文書が開くように
  する

  * |InsertHyperlinkM|

枠が選択されると |FormattingToolbar| の代わりに |FrameToolbar| が表示され、コン
テキストメニューにはアンカー、配置、折り返し、整列に関するコマンドが含まれる。

Applying page styles
----------------------------------------------------------------------

ページ上の任意の場所にキャレットを置け。適用されたページスタイルが |StatusBar|
に表示される。

別のページスタイルを適用するには、次のいずれかを行う：

* |StatusBar| のスタイルを右クリックし、コンテキストメニューからスタイルを選択
* |Sidebar| |StylesDeck| を開き、上部にある |PageStylesTab| を選択し、目的のペー
  ジスタイルをダブルクリック

.. caution::

   ページスタイルを変更すると、それ以降のページのスタイルも変更されることがあ
   る。その結果、望むものにならないことがある。一ページだけスタイルを変更するに
   は、手動で改頁を挿入する必要がある場合がある。

|Writer09| にあるように、正しく構成されたページスタイルはほとんどの場合、次の
ページのページスタイルがどうなるべきかという情報を含んでいる。たとえば、

* あるページに `Left Page` スタイルを適用する場合、ページスタイルの設定で、次の
  ページには `Right Page` スタイルが必要であることを指示することが可能だ。
* `First Page` スタイルの後に `Left Page` スタイルまたは `Default Page` スタイル
  が続くこともある。

ページスタイルを変更するもう一つの方法は、手動で改頁を挿入し、後続ページのスタイ
ルを指定することだ。考え方は簡単で、一連のページスタイルを中断し、新しいシーケン
スを開始する。改頁を挿入するには :menuselection:`&Insert-->More &Breaks-->Manual
&Break...` を選択する。

以下、改頁が役立つ一般的な事態二つが述べられる。

Example: Chapters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

想定される事態：

* 章に分かれた本を執筆している
* 各章は `First Page` と呼ばれるページスタイルで始まる
* その次のページでは `Default Page Style` が使われる
* 最終章を除く各章の終わりには、次の章のために `First Page` スタイルに戻る

ある時点で、新しい章を始めたいと思うだろう。その場合には次の工程を採る：

#. キャレットを章末の空白行（空の段落）に置く
#. :menuselection:`&Insert-->More &Breaks-->Manual &Break...` を選択
#. |InsertBreakDlg| が開く：

   * :guilabel:`Type` で :guilabel:`Page break` を選択
   * :guilabel:`Page Style` で :guilabel:`First Page` を選択

.. tip::

   章の表題（通常は `Heading 1`）の段落スタイルに改頁を含めるように定義すること
   で、これらの改頁を自動化することが可能だ。

Example: Page with special formatting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

横長のページや段組の多いページなど、特殊な書式のページを挿入するには、改頁を使用
する。現在のページが `Default Page Style` であると仮定する。

#. :menuselection:`&Insert-->More &Breaks-->Manual &Break...` を選択
#. |InsertBreakDlg| で所望のページスタイルを選択
#. このページに何かを打ち込む
#. もう一度 `Default Page Style` を選択して別の改頁を挿入

.. admonition:: 読者ノート

   図解を読み解くに `Default Page Style` の間に異種ページスタイルを挟むのが本
   質。

Example: A book chapter sequence of pages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. |HeaderOn| replace:: :guilabel:`Hea&der on`
.. |PageLayout| replace:: :guilabel:`&Page layout`

本の章は通常右ページで始まり、章の最初のページは他のページとは異なるレイアウトに
なっている。その章の他のページは、両面印刷のために鏡映しにされる。例えば、ヘッ
ダーやフッターのページ番号はページの外側の端に配置され、内側の端には（綴じられる
ことに備えて）広い余白が設けられる。

カスタマイズ内容をまとめると：

`First Page`
   |PageTab|
      * |PageLayout|: :guilabel:`Only right`
      * :guilabel:`Top`: 6.00 cm
   |HeaderTab|
      * |HeaderOn|: オフ
`Default Page Style`
   |PageTab|
      * |PageLayout|: :guilabel:`Mirrored`
   |HeaderTab|
      * |HeaderOn|: オン
      * :guilabel:`Same co&ntent left/right`: オフ
      * :guilabel:`Same content first &page`: オン

**Step 1.** `First Page` スタイルを構築する。

#. |StylesDeck| で |PageStylesTab| をクリックし、ページスタイルを列挙させる。
#. :guilabel:`First Page` を右クリックし、|EditStyleC| を選択
#. |PageStyleDlg| |OrganizerTab| で :guilabel:`Ne&xt style` を
   :guilabel:`Default Page Style` に変更
#. |PageTab| で次の余白いずれかを指定する：

   * :guilabel:`&Gutter`
   * 綴じ代に :guilabel:`&Left` を大きくする
   * 章表題をページの下に移動させるために :guilabel:`&Top` を大きくする

   ガター余白の使い方については |Writer09| を見ろ。この例では用いていない。
#. |HeaderTab| と |FooterTab| それぞれで |HeaderOn| と :guilabel:`&Footer on` が
   それぞれオフであることを確認
#. |OK| を押す

**Step 2.** `Default Page Style` を構築する。

#. |StylesDeck| |PageStylesTab| で :guilabel:`Default Page Style` を右クリックし、
   |EditStyleC| を選択する
#. |OrganizerTab| で :guilabel:`Ne&xt Style` が `Default Page Style` に設定され
   ていることを確認
#. |PageTab| で

   * |PageLayout| に :guilabel:`Mirrored` を選択
   * :guilabel:`I&nner` と :guilabel:`O&uter` をそれぞれ `First Page` スタイルの
     :guilabel:`&Left` と :guilabel:`&Right` それぞれと同じ値に設定
   * `First Page` スタイルに :guilabel:`&Gutter` が設定されている場合は、ここの
     それも同じ値にする
#. |HeaderTab| で

   * |HeaderOn| オン
   * :guilabel:`Same content first &page` オン
   * :guilabel:`Same co&ntent on left and right` オフ
#. |OK| を押す

**Step 3.** ページヘッダーを仕込む。

#. 文書に改頁を二つ入れる。これで `First Page` スタイルのページが一ページ、
   `Default Page Style` のページが二ページになるはずだ。
#. `Default Page Style` である最初の（左側の）ページで、キャレットをヘッダーに置
   き、ページ番号フィールドを挿入する。段落揃えを左揃えに設定したままにする。
#. `Default Page Style` である次の（右側の）ページで、キャレットをヘッダーに置
   き、ページ番号フィールドを挿入する。段落の配置を右揃えに変更する。
#. ヘッダーの設定に使用した空白ページを削除する。設定はファイルに残る。

**Step 4.** `Heading 1` 段落スタイルを構築し、`First Page` スタイルで章を開始す
る。

#. |StylesDeck| |ParagraphStylesTab| で :guilabel:`Heading 1` を右クリックし、
   |EditStyleC| を選択
#. |ParagraphStyleDlg| |TextFlowTab| で :guilabel:`Breaks` 区画の次の選択肢をオ
   ン：

   * :guilabel:`&Insert`
   * :guilabel:`With page st&yle`

     さらにドロップダウンリストから :guilabel:`First Page` を選択
#. |OK| を押す

以上で、章の表題となる段落に `Heading 1` スタイルを適用すると、新しいページが
`First Page` スタイルで自動的に始まる。

.. note::

   既定では、`Heading 1` 段落スタイルが `Heading (Outline) Level 1` に割り当てら
   れている。段落スタイルのアウトライン階層への割り当ては |HeadingNumberingM| 設
   定で行う。

Applying list styles
----------------------------------------------------------------------

一覧スタイルは、字下げ、番号スタイル（例えば、`1,2,3`; `a,b,c`; 箇条書き）、番号
の後の句読点などの性質を定義するが、フォント、境界、テキストフローなどのそれを定
義するものではない。後者は段落スタイルのものだ。

|StylesMenu| メニューや |Sidebar| |StylesDeck| を使用して一覧スタイルを適用でき
るが、これらの方法は推奨されない。

箇条書き一覧や番号付き一覧の作成には、可能な限り段落スタイルを使え。この目的のた
めに段落スタイルが二セット用意されている。一覧スタイルと段落スタイルは、これらの
方法で一緒に使用することをお勧めする：

* 順序なし一覧を作成するには、段落スタイル `List 1`, `List 2`, `List 3`, etc.
* 順序付き一覧を作成するには、段落スタイル `Numbering 1`, `Numbering 2`,
  `Numbering 3`, etc.

他のスタイルと同様に、番号や箇条書きの記号、字下げなど、これらのスタイルの性質を
再定義することが可能だ。また、これらのシリーズに他の一覧スタイルを定義したり、独
自のシリーズを作成することも可能だ。|Writer09| を見ろ。一覧スタイルの詳細につい
ては |Writer12| を見ろ。

Applying table styles
----------------------------------------------------------------------

図表スタイルとは、フォント、段落間隔、列数、境界、背景色などの性質を規定するもの
だ。

図表スタイルを適用するには、

#. テーブルの任意の場所にキャレットを置く
#. |Sidebar| |StylesDeck| |TableStylesTab| を選択
#. 一覧にあるスタイル名をダブルクリック

図表スタイルの作成については |Writer13| を見ろ。

Creating and modifying styles
======================================================================

Writer には定義済みスタイルが多く用意されており、文書を他の機械、特に異なる言語
版 LibreOffice で共有する場合に便利だが、自分の好みに合わないことがあるかもしれ
ない。定義済みのスタイルを変更したり、独自のカスタムスタイルのライブラリーを作成
して、定義済みのスタイルに加えて、または定義済みのスタイルの代わりに使用すること
が可能だ。

.. note::

   新規作成スタイルや、既存スタイルに加えた変更は、そのスタイルが属する文書内で
   しか使用できない。スタイルは常に文書と共に残る。

   このようなスタイルを他の文書で再利用する場合はスタイルをテンプレートに保存す
   るか、スタイルを他の文書にコピーしろ。|Writer09| を見ろ。

定義済みスタイルとカスタムスタイルの両方を変更するために、次の手段が整備されてい
る：

* 選択範囲からスタイルを作成または更新する
* 他の文書やテンプレートからスタイルを読み込むかコピーする
* |StyleDlg| を使用してスタイルを変更する
* AutoUpdate を使用する（段落スタイルと枠スタイル）
* AutoFormat 自動書式を使用する（図表スタイルのみ）

Using the Styles actions menu
----------------------------------------------------------------------

|StylesDeck| 上部の最後のドロップダウンメニュー :guilabel:`Styles actions` には
三つの機能がある：

* :menuselection:`&New Style from Selection`
* :menuselection:`&Update Selected Style`
* :menuselection:`&Load Styles from Template`

これらの機能は |MenuBar| |StylesMenu| からも利用可能。

New Style from Selection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:menuselection:`&New Style from Selection` を使用すると、現在の文書内の項目の書
式設定から新しいスタイルを作成できる。たとえば、ある段落の書式を好みの表示になる
まで変更し、その書式を新しいスタイルに変更することが可能だ。この方法には次の利点
がある：

* |StyleDlg| で新規スタイルを作成するときのように、必要な書式設定をすべて覚えて
  おく必要がない。時間を節約できる。
* 作成するスタイルで書式設定したときに項目がどのように見えるかをすぐに確認でき
  る。

選択範囲からスタイルを新規作成する手順：

#. 文書内で、目的の書式（段落、枠など）を好みに変更する。スタイルとして保存した
   い項目を選択する。
#. |Sidebar| |StylesDeck| を開き、上部の図像行から作成するスタイルの品目（段落、
   文字など）を選択
#. :menuselection:`Styles actions-->&New Style from Selection` を選択
#. 新規スタイルの名前を入力
#. |OK| を押す

Update Selected Style
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

選択範囲から段落スタイルを更新する手順：

#. 段落を新規作成し（または既存段落を選択し）、字下げ、フォント、配置など、スタ
   イルで変更したい性質全てを編集

   .. note::

      この段落の性質が統一されていることを確認しろ。例えば、段落内に二つの異なる
      フォントサイズがある場合、その性質は更新されない。

#. 段落のどこかをクリック
#. |Sidebar| |StylesDeck| で更新したいスタイルを選択（ダブルクリックではなくシン
   グルクリック）
#. :menuselection:`Styles actions-->&Update Selected Style` を選択

別の区分のスタイル（文字、ページ、枠）を更新する手順も同じだ。問題の項目を選択し
て修正し、更新したいスタイルを選択して :menuselection:`Styles actions-->&Update
Selected Style` を選択しろ。

Load Styles (from a template or document)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

最後の選択肢は :menuselection:`&Load Styles from Template` だ。テンプレートや別
の文書から読み込んで現在の文書にスタイルをコピーする。この方法を使うと、一度にス
タイル全部を、またはスタイルの一群をコピーできる。

#. スタイルをコピーする文書を開く
#. |StylesDeck| で :menuselection:`Styles actions-->&Load Styles from Template`
   を選択
#. スタイルをコピーするテンプレートを見つけて選択
#. ダイアログボックス下部からコピーするスタイルの型をオンにする

   :guilabel:`&Overwrite` をオンにすると、コピーされるスタイルは対象文書内の同名
   スタイルを上書きする。
#. |OK| を押す

必要なスタイルがテンプレートではなくテキスト文書に含まれている場合：

#. コピーするスタイルの型を選択
#. :guilabel:`F&rom file...` ボタンを押してファイルダイアログボックスを開く
#. 所要の文書を選択
#. |Open| を押す

Drag-and-drop a selection to create a style
----------------------------------------------------------------------

新しいスタイルを作成するもう一つの方法は選択テキストを |StylesDeck| にドラッグ＆
ドロップすることだ。

#. |Sidebar| |StylesDeck| を開く
#. 甲板上部にある図像で作成するスタイル品目（例：文字スタイル）を選択
#. スタイルの基となるオブジェクトを選択し、|StylesDeck| にドラッグ
#. :guilabel:`Create Style` ダイアログボックスで新しいスタイルの名前を入力
#. |OK| を押す

.. note::

   この方法はページスタイルや図表スタイルを作成するのには用いられない。

Changing a style using the Style dialog
----------------------------------------------------------------------

|StyleDlg| を使用して（図表スタイルではない）スタイルを変更するには |StylesDeck|
でスタイルを右クリックし、|EditStyleC| を選択する。

表示されるダイアログボックスは選択スタイルの型によって異なる。各スタイルのダイア
ログボックスにはタブがある。これらのダイアログボックスの性質については
|Writer09| を見ろ。

図表スタイルの変更については |Writer13| を見ろ。

Using AutoUpdate
----------------------------------------------------------------------

|ParagraphStyleDlg| および :guilabel:`Frame Style` ダイアログボックスの
|OrganizerTab| には :guilabel:`&AutoUpdate` オプションがある。これがオンであれ
ば、そのスタイルで書式設定された段落に手動で加えた変更がそのスタイルに適用され
る。

.. caution::

   文書内のスタイルを手動で上書きする習慣がある場合は :guilabel:`&AutoUpdate` が
   有効になっていないことを確認しろ。そうしないと、文書が予期せず再整形されるこ
   とになる。

Deleting styles
======================================================================

LibreOffice の定義済みスタイルは使用していない場合でさえ、文書やテンプレートから
削除することは不可能だ。ただし、カスタムスタイルは削除可能だ。

|Sidebar| の |StylesDeck| を使って不要なスタイルを削除するには：

#. 削除するスタイルをそれぞれ選択

   * |Ctrl| を押しながらマウスクリックで複数スタイルを選択可
#. 右メニューから :menuselection:`&Delete...` を選択

   * スタイルが使用中の場合は、警告メッセージが表示され、本当にそのスタイルを削
     除するかどうかを確認するよう求められる。
   * そのスタイルが使用されていない場合、確認なしに即座に削除される。

.. note::

   使用中のスタイルを削除した場合、そのスタイルを持つ物のすべてが、その基底スタ
   イルに戻るが、削除されたスタイルの書式の一部が手動書式として保持される可能性
   がある。

.. tip::

   不要な段落スタイルが使用中の場合、削除前に Find and Replace コマンドを使用し
   て、そのスタイルを代替スタイルに置き換えることが可能だ。|Writer03| を見ろ。

Example: creating and modifying paragraph styles
======================================================================

このセクションでは、カスタム段落スタイルの典型的な使用例を示す。次に挙げる性質を
持つ `Poem` 段落スタイルと `Poen Heading` 段落スタイルを作成する：

* `Poem`: 中央揃え、フォントサイズ 10 pt
* `Poem Heading`: 中央揃え、太字、フォントサイズ 12 pt

さらに、`Poem Heading` スタイルの後には `Poem` スタイルが続く。つまり、`Poem
Heading` 段落スタイルの段落の最後で |Enter| を押すと、次の段落の段落スタイルが
`Poem Heading` に変わる。

.. note::

   `Heading` 段落スタイルを使って見出しを入力し |Enter| を押すと、次のスタイルが
   `Text body` に切り替わるという挙動に注意する。

Creating the Poem paragraph style
----------------------------------------------------------------------

`Default Paragraph Style` を出発点として使用する。

#. |StylesDeck| で |ParagraphStylesTab| をクリック
#. :guilabel:`Default Paragraph Style` を右クリック
#. |NewC| を選択

段落 |StyleDlg| で |OrganizerTab| を選択しろ。カスタムスタイルを作成
するには、上位三項目を構成する必要がある。

:guilabel:`&Name`
   スタイル名なので ``Poem`` を入力。
:guilabel:`Ne&xt Style`
   `Poem` スタイルに後続する段落のスタイル。`Poem` スタイルであるテキストを入力
   している途中に |Enter| を押すと、これが新段落に自動適用される。したがっ
   て :guilabel:`Poem` を指定。
:guilabel:`&Inherit from`
   今回は :guilabel:`- None -` を指定。

:guilabel:`&AutoUpdate` はオフにしろ。

このスタイルの文字揃えとフォントの性質を設定する：

* |AlignmentTab| で :guilabel:`&Center` を選択
* |FontTab| で :guilabel:`12 pt` の :guilabel:`Si&ze` を選択

|OK| を押す。`Poem` スタイル保存される。

Creating the Poem Heading style
----------------------------------------------------------------------

`Poem Heading` スタイルを作成するには、上記と同じ手順を使うが、次の点を変更する：

:guilabel:`Ne&xt Style`
   :guilabel:`Poem` を選択。`Poem Heading` スタイルのテキストを入力中に
   |Enter| を押すと、`Poem Heading` スタイルが新しい段落に自動適用される。
:guilabel:`&Inherit from`
   :guilabel:`Heading` とする。

新しいスタイルの設定を選択する：

* |AlignmentTab| で :guilabel:`&Center` を選択
* |FontTab| で :guilabel:`&Font` を選択し、:guilabel:`12 pt` の :guilabel:`Si&ze`
  を選択

|OK| を押す。`Poem Heading` スタイルが保存される。

Sample poem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

先ほど定義したスタイルを使って詩を入力して、新しいスタイルを検分する。

Changing the formatting of styles
----------------------------------------------------------------------

スタイルの主な利点の一つは、中身が書かれた後で文書の書式を変更できることだ。たと
えば 100 ページの詩集を書き、上記のスタイル設定を使用したとする。その後、著者や
出版社が、詩の体裁が気に入らないだの、中央揃えではなく左揃えがいいだのと言い出
す。

`Poem` と `Poem Heading` スタイルの文字揃えを変更するには：

#. |StylesDeck| で :guilabel:`Poem` を右クリックし |EditStyleC| を選択
#. |AlignmentTab| で :guilabel:`&Left` を選択
#. |OK| を押す。
#. テキストが変更されるのを確認する。
#. これらの変更を `Poem Heading` スタイルに対しても繰り返す。

.. _writer08-anchorA:

Using paragraph styles to define a hierarchy of headings
======================================================================

段落スタイルは Writer の目次機能の急所だ。|HeadingNumberingM| は文書内の見出しの
階層を定義する。見出し階層に割り当てられる既定段落スタイルは Writer 組み込みの見
出しスタイル (e.g. `Heading 1`, `Heading 2`, etc.) だ。ただし、カスタムスタイル
を含め、任意のスタイルで代用することが可能だ。

見出し番号機能を使って定義された見出しは、目次 (|Writer15|) 以外にも使うことが
できる。たとえば、ページのヘッダーやフッターに節見出しを表示するために、フィール
ドがよく使われる (|Writer17|)。

Choosing paragraph styles for heading levels
----------------------------------------------------------------------

アウトラインの見出しに既定見出しスタイルを使用していて、見出し番号付けを使用した
くない場合は、:guilabel:`Chapter Numbering` ダイアログボックスで何もする必要はな
い。既定アウトライン番号付け制度は既定見出しスタイルを使用する。

既定見出しスタイル一つ以上の代わりにカスタムスタイルを使用する手順：

#. |HeadingNumberingM| を選択
#. :guilabel:`Numbering` タブで段落スタイルを変更したい見出しに対応する
   :guilabel:`Level` 欄の番号をクリック
#. :guilabel:`Numbering: Paragraph Style` 区画で、その見出しレベルに割り当てる段
   落スタイルをドロップダウンリストから選択

   この例では `Heading 1` を置き換えるために :guilabel:`My Heading 1` を選択し、
   `Level 2` を置き換えるために :guilabel:`My Heading 2` を選択する。
#. 変更したい番号レベルごとに繰り返す。
#. |OK| を押す

Assigning outline levels to other styles
----------------------------------------------------------------------

Writer では、任意の段落スタイルにアウトラインレベルを割り当てることができる。こ
の機能により、|HeadingNumberingDlg| に一覧されているスタイルを使用して、それらの
見出しを含む目次を作成することができる。たとえば、付録には別のスタイルの順序を使
用するが、付録の見出しや小見出しは、章の見出しや小見出しと同じレベルで目次に表示
されるようにする。

段落スタイルにアウトラインレベルを割り当てる手順：

#. そのスタイルの |Outline&ListTab| を開く
#. ドロップダウンリストから必要なアウトラインレベルを選択
#. |OK| を押す

Setting up heading numbering
----------------------------------------------------------------------

一つ以上の見出しレベルに番号を付けたい場合、多くの選択肢がある。この例では、下図
のような見出しを作成するスキームを定義している：

.. code:: text

   1     This is a Heading 1
   1.1   This is a Heading 2
   1.1.1 This is a Heading 3
   1.1.2 Another Heading 3
   2     Another Heading 1
   2.1   Another Heading 2
   2.1.1 Another Heading 3
   2.2   Another Heading 2
   3     Another Heading 1

|HeadingNumberingDlg| の :guilabel:`Numbering` タブを使用して、番号付け制度とそ
の容貌を定義する。

.. |LevelList| replace:: :guilabel:`&Level` 一覧
.. |NumberList| replace:: :guilabel:`&Number` ドロップダウンリスト
.. |ShowSublevels| replace:: :guilabel:`Sho&w sublevels` スピンボックス
.. |123| replace:: :guilabel:`1, 2, 3,...`

#. |LevelList| から :guilabel:`1` を選ぶ
#. |NumberList| から |123| を選ぶ
#. |LevelList| から :guilabel:`2` を選ぶ
#. |NumberList| から |123| を選ぶ

   |ShowSublevels| が活動開始する。:guilabel:`2` が示される。
#. |LevelList| で :guilabel:`3` を選ぶ
#. |NumberList| で |123| を選ぶ

   |ShowSublevels| に :guilabel:`3` が示される。
