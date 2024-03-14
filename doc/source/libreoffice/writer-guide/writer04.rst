======================================================================
Writer Guide Chapter 4, Formatting Text ノート
======================================================================

.. contents::
   :depth: 3
   :local:

Introduction
======================================================================

この章ではテキストの書式設定の基本について習う。

* 段落や文字の書式設定
* 自動書式適用の使用
* 順序なし、順序付き、アウトラインリストの作成

この章の読者が :doc:`Chapter 2 <writer02>` と :doc:`Chapter 3 <writer03>` に
馴染んでいることを仮定される。

:doc:`Chapter 20 <writer20>` にある提案設定に従うことを推奨されている。

ページの書式設定については :doc:`Chapter 5 <writer05>` と :doc:`Chapter 6
<writer06>` で説明する。

Formatting: direct (manual) or styles
----------------------------------------------------------------------

Direct (or Manual) formatting
   特定の段落、文字、ページ、枠、一覧、図表に書式を直接適用する。たとえば、単語
   を選択し、:guilabel:`Formatting` ツールバーのボタンをクリックすると、テキスト
   が太字になったり斜体になったりする。
Styles
   書式設定オプションを一つの名前にまとめる。たとえば、段落スタイルでは、フォン
   トの種類やサイズ、段落を字下げするかどうか、行間の広さ、ページ上での段落
   の揃え方など、さまざまな選択肢を設定する。

Using styles is recommended
----------------------------------------------------------------------

スタイルは書式のグループ全体に同時に適用されるため、文書の書式を一貫したものにし
たり、文書全体の書式を最小限の労力で変更したりすることが簡単にできる。

.. admonition:: 読者ノート

   Writer を使いこなすにはスタイルを中心に物事を考えるのが良いようだ。

LibreOffice では他の多くの処理にもスタイルが使用されている。たとえば、Writer が
目次を作成するときは見出しスタイル（または他の選択したスタイル）を使用する。

スタイルとその使用方法については :doc:`Chapter8 <writer08>` と :doc:`Chapter09
<writer09>` を読め。

スタイルの適用は Sidebar の :guilabel:`Styles` 甲板を使用してすばやく簡単に行う。

Removing manual formatting
----------------------------------------------------------------------

.. note::

   手動書式設定はスタイルを上書きするため、何かスタイルを適用すること削除するこ
   とは不可能だ。

手動書式設定を削除するには、テキストを選択し、次のいずれかを：

* メニューで :menuselection:`F&ormat --> Clear &Direct Formatting` を選択
* 右クリックメニューで :menuselection:`Clear &Direct Formatting` を選択
* :guilabel:`Formatting` ツールバーの :guilabel:`Clear Direct Formatting` 図像を
  クリック
* :kbd:`Ctrl` + :kbd:`M` を押す

Formatting paragraphs using styles
======================================================================

スタイルを段落に適用する方法については :doc:`Chapter8 <writer08>` を読め。

* :guilabel:`Formatting` ツールバーおよび :guilabel:`Formatting (Styles)` ツール
  バーの左端にある :guilabel:`Set Paragraph Style` ドロップダウンリスト
* Sidebar の :guilabel:`Properties` 甲板の上部にある :guilabel:`Set Paragraph
  Style` ドロップダウンリスト
* Sidebar の :guilabel:`Styles` 甲板の :guilabel:`Paragraph Styles` タブ
* メニューの :menuselection:`St&yles` メニュー
* キーバインド :kbd:`Ctrl` + :kbd:`1` から :kbd:`Ctrl` + :kbd:`5`

Formatting paragraphs directly
======================================================================

* :guilabel:`Formatting` ツールバーの図像
* Sidebar の :guilabel:`Properties` 甲板の :guilabel:`Paragraph` 盤
* メニューの :menuselection:`F&ormat` のコマンド

を使用して、多くの書式を段落に適用できる。その他の書式設定オプションは
:guilabel:`Paragraph` ダイアログボックスに用意されている。

Formatting toolbar
----------------------------------------------------------------------

:guilabel:`Formatting` ツールバーには、以下の図像と書式がある：

* :guilabel:`Set Paragraph Style` ドロップダウンリスト
* :guilabel:`Align Left`, :guilabel:`Align Center`, :guilabel:`Align Right`,
  :guilabel:`Justified`
* :guilabel:`Align Top`, :guilabel:`Center Vertically`, :guilabel:`Align Bottom`
* :guilabel:`Toggle Unordered List` パレット
* :guilabel:`Toggle Ordered List` パレット
* :guilabel:`Select Outline Format` パレット
* :guilabel:`Increase Paragraph Spacing`, :guilabel:`Decrease Paragraph Spacing`
* :guilabel:`Increase Indent`, :guilabel:`Decrease Indent`, :guilabel:`Hanging
  Indent`
* :guilabel:`Paragraph` は :guilabel:`Paragraph` ダイアログボックスを開く
* :guilabel:`Set Line Spacing` は間隔を選んだり数値で指定したりする

標準インストールではすべてのツールバー図像が表示されるわけではない。ツールバーを
カスタマイズすることでいつも使うものを追加する。:doc:`Chapter 1 <writer01>` を見
ろ。

Sidebar Properties deck
----------------------------------------------------------------------

Sidebar :guilabel:`Properties` 甲板にはスタイルの適用、文字の手動書式設定、段落
の手動書式設定のための盤がある。必要に応じて展開ボタンをクリックして盤を開け。

:guilabel:`Style` 盤
   :guilabel:`Set Paragraph Style` ドロップダウンリストと、:guilabel:`Clone
   Formatting`, :guilabel:`Update Selected Style`, :guilabel:`New Style from
   Selection` の図像が載っている。この辺は :doc:`Chapter 8 <writer08>` でやる。
:guilabel:`Character` 盤
   後述。
:guilabel:`Paragraph` 盤
   :guilabel:`Formatting` ツールバーにないものも含め、書式設定コントロールをほと
   んど搭載している。ボタン横の下矢印をクリックすると、行間固定やカラーパレッ
   トなど、さらに選択できるコントロールが開く。

各盤のタイトルバーの右側には :guilabel:`More Options` 図像があり、追加設定を含む
関連ダイアログボックスが開く。

.. admonition:: 読者ノート

   タイトルバー右端の右下を向いている小さい矢印のことだ。これをクリックするとダ
   イアログボックスが開くというのが想像しにくいので、あらかじめ知っておくと困ら
   ない。

これらの設定値を変更すると、キャレットのある段落のみ、または複数の段落が選択され
ている場合はそれらの段落に影響する。その型の多くの段落の値を変更するには、段落ス
タイルを用いる方がよい。

Alignment options
----------------------------------------------------------------------

段落の配置を選択するには、盤左上の固まっている横線まみれの図像群を使用する。上の
段はそれぞれ次だ：

* 左揃え
* 右揃え
* 中央揃え
* 両端揃え

両端揃えテキストを使用する場合、最終行は既定で左揃えになる。しかし、最終行を段落
領域の中央に揃えたり、行全体を埋めるために単語間のスペースを増やすように両端揃え
することもできる。:guilabel:`&Expand single word` をオンにすると、両端揃え段落の
最終行が単一単語で構成されている場合、この単語が行の長さいっぱいになるように文字
間に空白を挿入して伸ばす。

これらのオプションは、次のいずれかの操作で表示される :guilabel:`Paragraph` ダイ
アログボックスの :guilabel:`Alignment` タブで制御する：

* メニューの :menuselection:`F&ormat --> P&aragraph...` を選択
* 段落内で右クリックして :menuselection:`P&aragraph --> P&aragraph...` を選択
* Sidebar の :guilabel:`Properties` 甲板にある :guilabel:`Paragraph` 盤の
  :guilabel:`More Options` ボタンをクリック

Line and paragraph spacing
----------------------------------------------------------------------

:guilabel:`Set Line Spacing` はある基準線から次の基準線までの距離を意味する。
フォントサイズによって決まる値だ。

:guilabel:`Set Line Spacing` パレットでは、標準的な間隔を選択するか、カスタム値
を定義することができる。これらの選択肢の違いを確認するには、いくつかのサンプル段
落を作成し、選択範囲を変更しろ。

.. note::

   :guilabel:`Fixed` または :guilabel:`At Least` を除くオプションはすべてフォン
   トの既定を使用する。この二つのオプションは独自の間隔を設定することができ、読
   みやすさを向上させるために、小さなフォントサイズでは特に有用だ。

..

   :dfn:`Paragraph spacing` refers to the vertical spacing between one paragraph
   and the paragraphs above and below it.

段落間隔の現在の値は :guilabel:`Above Paragraph Spacing` 欄と :guilabel:`Below
Paragraph Spacing` 欄に示される。これらの設定の一方か、または両方を個別に変更す
ることが可能だ。

.. tip::

   本書のような計算機文書では段落間隔が使われがちだ。その他の文書では段落インデ
   ント（次の節でやる）がよく使われる。よい設計のためには段落間隔か段落インデン
   トの一方のみを使え。両方を使うな。

Paragraph indentation
----------------------------------------------------------------------

左右のページ余白と段落の間の空間を広げる。その距離を盤右下のスピンボックス付き入
力欄で設定する：

* :guilabel:`Before Text Indent`: 左余白から
* :guilabel:`After Text Indent`: 右余白から
* :guilabel:`First Line Indent`: 最初の行を左余白または指定された余白から

:guilabel:`Hanging Indent` は最初の行を左余白（または余白からの指定字下げ）に残
し、段落の他の行すべてを :guilabel:`First Line Indent` または
:guilabel:`Paragraph` ダイアログボックスで指定された量だけ字下げする。

.. note::

   右から左への言語では :guilabel:`Before Text Indent` と :guilabel:`After Text
   Indent` の動作は逆になる。

Paragraph background color
----------------------------------------------------------------------

:guilabel:`Background Color` をクリックしてパレットを開き、段落の背景色を選択す
る。このパレットでは :guilabel:`Custom Color` をクリックして :guilabel:`Pick a
Color` ダイアログボックスを開き、パレットに追加する新しい色を定義することも可能
だ。

.. note::

   段落が右または左余白から字下げされている場合、背景色は字下げの領域には適用さ
   れない。余白まで色を広げるには、枠、図表、またはその他の方法を使用する。
   :doc:`Chapter 6 <writer06>` 参照。

Settings on the Paragraph dialog
----------------------------------------------------------------------

:guilabel:`Paragraph` ダイアログボックスにはさらにいくつかのタブがある。

* :guilabel:`Tabs`: これはもう少し後で述べる
* :guilabel:`Borders`
* :guilabel:`Drop Caps`
* :guilabel:`Area`
* :guilabel:`Transparency`
* :guilabel:`Text Flow`
* :guilabel:`Outline & List`

詳しくは :doc:`Chapter 8 <writer08>` と :doc:`Chapter 9 <writer09>` を参照しろ。

Borders
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

境界は段落を周囲のテキストから引き離し、主題からはずれた余談を含めるのに便利だ。
例えば、本書の Tips, Notes, Caution では本文の下に境界を使用している。

* 段落の上下左右の任意の組み合わせに境界を追加可能。
* 線のスタイル（実線、点線、破線、二重線）、幅、色を選択でき、これらの選択は段落
  上のすべての境界に適用される。
* 各行から段落の内容までの間隔は上下左右で個別に設定可能。

:guilabel:`Paragraph` ダイアログボックスの :guilabel:`Borders` タブでは段落に影
を適用することも選択可能。

* :guilabel:`Distan&ce` とは影の幅のこと。

次の段落の字下げ、境界線、影のスタイルが現在の段落と同じ場合、:guilabel:`&Merge
with next paragraph` をオンにすると、上線または下線が抑制される。

Drop caps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   :dfn:`Drop capitals` are enlarged letters that mark the start of a new
   chapter or section.

一貫性を高めるため、関連する段落に適用する段落スタイルで設定するのが最適だ。詳細
は :doc:`Chapter 9 <writer09>` を見ろ。

Area
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Area` には次の五種類の塗りつぶしがある：

* 色
* グラデーション
* 画像
* パターン
* ハッチング

塗りつぶしの種類を選択するとその種類で使用できる選択肢が表示される。これらの選択
肢については :doc:`Chapter 5 <writer05>` で見る。独自の塗りつぶしを作成すること
もできる。

Transparency
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Transparency` は段落の背景に影響する。透かしを作成したり、色や画像を
淡く（テキストとの明暗の調子対比を強く）するのに便利だ。これも :doc:`Chapter 5
<writer05>` で詳しくやる。

Text Flow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Text Flow` タブには区画がある。

* :guilabel:`Hyphenation` については :doc:`Chapter 2 <writer02>` を見ろ。
* :guilabel:`Breaks` については :doc:`Chapter 5 <writer05>` を見ろ。

:guilabel:`Options` 区画ではページ下部の段落の扱い方を指定する。

:guilabel:`&Orphan control` と :guilabel:`&Widow control` の行数は、それぞれ
ページ下部と上部に単一行だけがあるのを避けるものだ。

.. admonition:: 読者ノート

   `Widows and orphans - Wikipedia
   <https://en.wikipedia.org/wiki/Widows_and_orphans>`__

   そう言われると LibreOffice Guide 集はページの最後のパラグラフが京極夏彦先生作
   品級にキリが良い終わり方をする。

Outline & List
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Paragraph` ダイアログボックスの :guilabel:`Outline & List` タブには段
落のアウトラインレベルと目録スタイルを選択するオプションがある。段落が順序付き目
録の一部である場合、目録の番号付けを段落から開始し、どの番号から開始するかを指定
する。表示される目録スタイルには次のものがある：

* 組み込み
* カスタム（ユーザー定義）

このタブは :guilabel:`Heading Numbering` ダイアログボックスと同じ機能をカバーし
ていないが、ここで選択されたアウトラインレベルはそこで定義されたアウトラインに関
連している。

* これらの機能の詳細は :doc:`Chapter 8 <writer08>` と :doc:`Chapter 9
  <writer09>` を参照しろ。
* 行番号については :doc:`Chapter 3 <writer03>` を見ろ。

Setting tab stops and indents
----------------------------------------------------------------------

水平定規にはタブストップが表示される。定義したタブストップは、既定のタブストップ
を上書きする。タブの設定は段落全体の字下げだけでなく、段落の一部の字下げ（キー
ボードの :kbd:`Tab` キーを押す）にも影響する。

.. tip::

   段落の先頭など、多くの字下げは段落スタイルで設定できるので、:kbd:`Tab` でする
   必要はない。

既定のタブ間隔を使用すると他の人と文書を共有する場合に書式の問題が発生することが
ある。既定のタブ間隔を使用し、異なる既定のタブ間隔を選択した他の人に文書を送信す
ると、タブ付けられた物は他の人の設定を使用するように変更される。既定を使用する代
わりに、本節で述べられる独自のタブ設定を定義しろ。

選択した一つまたは複数の段落の字下げとタブ設定を定義するには、

#. 段落を右クリックして :menuselection:`P&aragraph --> P&aragraph...` を選択
#. :guilabel:`Paragraph` ダイアログボックスで

   * :guilabel:`Tabs` タブまたは
   * :guilabel:`Indent & Spacing` タブのいずれかを選択

あるいは、水平定規をダブルクリックして、:guilabel:`Paragraph` ダイアログボックス
の :guilabel:`Indent & Spacing` タブを開く。よりよい方法は、その段落スタイルにタ
ブを定義することだ。段落スタイルについては :doc:`Chapter 8 <writer08>` と
:doc:`Chapter 9 <writer09>` を読め。

.. tip::

   タブを使ってページ内の物を空けることは推奨されない。通常は図表や枠を使う方が
   よい選択だ。

Changing the default tab stop interval
----------------------------------------------------------------------

.. caution::

   既定のタブ設定を変更すると、その後に開く文書の既存の既定のタブストップや、変
   更後に挿入されるタブストップにも影響する。

測定単位と既定のタブストップの間隔を設定するには、:guilabel:`Options` ダイアログ
ボックスで :menuselection:`LibreOffice Writer --> General` を選択する。

Changing measurement units for tab stops and rulers
----------------------------------------------------------------------

現在の文書の定規に測定単位を設定、変更するには、水平定規を右クリックして単位一覧
を開く。定規をその単位に変更するには、そのうちの一つを選択する。選択した設定はそ
の定規にしか適用されない。

Formatting characters using styles
======================================================================

文字スタイルを適用するには、文字または単語を選択し、次のいずれかから選択した文字
スタイルを適用する：

* Sidebar の :guilabel:`Styles` 甲板の :guilabel:`Character Styles` タブ
* メニューの :menuselection:`St&yles -->` （機能に制限あり）
* 右クリックメニュー（機能に制限あり）
* :guilabel:`Formatting (Styles)` ツールバー

文字スタイルの詳細については :doc:`Chapter 8 <writer08>` と :doc:`Chapter 9
<writer09>` を読め。

Formatting characters directly
======================================================================

次の UI を用いて書式の多くを文字に適用可能だ：

* :guilabel:`Formatting` ツールバーの図像
* Sidebar の :guilabel:`Properties` 甲板の :guilabel:`Characters` 盤

標準インストールではすべてのツールバー図像が表示されるわけではないが、ツールバー
をカスタマイズしてよく使うものを含めることができる。これらには次のものがある：

* :guilabel:`Font Name`, :guilabel:`Font Size`
* :guilabel:`Bold`, :guilabel:`Italic`, :guilabel:`Underline`, :guilabel:`Double
  Underline`, :guilabel:`Overline`, :guilabel:`Strikethrough`,
  :guilabel:`Outline`
* :guilabel:`Superscript`, :guilabel:`Subscript`
* :guilabel:`Uppercase`, :guilabel:`Lowercase`
* :guilabel:`Increase Font Size`, :guilabel:`Decrease Font Size`
* :guilabel:`Font Color`: パレットあり（以下二つも）
* :guilabel:`Background Color`
* :guilabel:`Character Highlighting Color`

段落全体の（フォント名、サイズ、色などの）特性を変更したり、その他多くの目的に
は、手動で文字を書式設定するのではなく、スタイルの詳細については :doc:`Chapter 8
<writer08>` と :doc:`Chapter 9 <writer09>` を読め。スタイルの適用は Sidebar の
:guilabel:`Styles` 甲板を使用して素早く簡単に行う。

Sidebar の :guilabel:`Properties` 甲板にある :guilabel:`Character` 盤では、横に▼
がある図像では、それをクリックするとフォントの色や文字間隔など、さらなる選択肢の
パレットが開く。

:guilabel:`More Options` ボタンをクリックすると、:guilabel:`Characters` ダイアロ
グボックスが開き、簡易設定用 UI で利用できる以上の選択肢が搭載されている。

.. note::

   直接段落書式が現在の段落スタイルを上書きするように、直接文字書式を文字に適用
   すると、現在の文字スタイル書式が上書きされる。

Font name, size, and effects
----------------------------------------------------------------------

選択した文字に使用するフォント名とサイズを変更するには、次のいずれかを用いる：

* :guilabel:`Formatting` ツールバー
* Sidebar の :guilabel:`Character` 盤
* :guilabel:`Character` ダイアログボックスのドロップダウンメニュー

選択した文字に太字、斜体、下線、取り消し線、影の効果を適用するのも同様。下線効果
には、線種のドロップダウンメニューがある。

:guilabel:`Formatting` ツールバーには Sidebar にはない他の効果として、
:guilabel:`Overline` と :guilabel:`Double Underline` がある。

フォントの色や強調色を選択するには、適切なカラーパレットを開く。強調色の選択は段
落に適用されている背景色よりも優先される。

選択した文字のフォントサイズを調整するには、:guilabel:`Formatting` ツールバーま
たは Sidebar の :guilabel:`Character` 盤にある関連する図像をクリックする。

文字を下付き文字または上付き文字に変更するには（サイズと位置の既定値が用いられ
る）、文字を選択して、:guilabel:`Formatting` ツールバーまたは Sidebar の
:guilabel:`Character` 盤で関連するアイコンをクリックする。

文字間隔をすばやく変更するには、文字を選択して Sidebar の :guilabel:`Set
Character Spacing` ドロップダウンメニューから選択する。

Settings on the Character dialog
----------------------------------------------------------------------

:guilabel:`Character` ダイアログボックスには、この節で述べられるタブ六つがある。
これらのタブのほとんどは :guilabel:`Character Style` ダイアログボックスのものと
同じだ。:doc:`Chapter 9 <writer09>` を参照しろ。

Font and Font Effects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Font` タブで フォント族、スタイル（フォントによって異なるが、通常、レ
ギュラー、ボールド、イタリック）、サイズを指定し、段落の言語（文書の言語と異なる
場合）を指定する。

:guilabel:`Font Effects` タブでは、フォントの色とさまざまな効果を選択する。

Position
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Position` タブはページ上のテキストの位置に影響する選択肢の集まりだ。
このタブは三区画からなる：

:guilabel:`Position` 区画は上付き文字と下付き文字の容貌を指定する。

:guilabel:`Rotation/Scaling` 区画は文字の回転を指定る。

* :guilabel:`Scale width` 欄は回転テキストを拡大縮小するフォント幅の百分率を指定
  する。

:guilabel:`Spacing` 区画は個々の文字の間隔を指定する。

* :guilabel:`Pair kerning` は特定の文字の組み合わせに対して文字間隔を自動的に調
  整する。既定でオン。特定のフォントタイプでのみ使用でき、印刷文書の場合、印刷機
  が対応している場合に限り機能する。

Hyperlink
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Hyperlink` タブは同名のダイアログボックスを使用する代替手段だ。選択肢
は少なく、テキストリンク専用だ。ハイパーリンクは、同じ文書の他の部分、他の文書、
または Web ページにリンクすることが可能だ。

LibreOffice は URL と思われる文字列を認識すると、その文字をハイパーリンクに置き
換え、インターネットリンクの文字スタイルで指定されたとおりにハイパーリンクを書式
設定する。このダイアログボックスでは、別の文字スタイルを選択したり URL を他のテ
キストに置き換えたりすることができる。この機能をオフにする手順は：

#. :menuselection:`&Tools --> AutoCorr&ect --> &AutoCorrect Options...` を選択
#. :guilabel:`Options` タブ
#. :guilabel:`URL Recognition` をオフ

Highlighting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Highlighting` タブは選択した文字の背景色を制御する。
:guilabel:`Highlighting` ドロップダウンパレットに似ている。

Borders
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Borders` タブは :guilabel:`Paragraph` ダイアログボックスのそれと同じ
だ。

Formatting lists using styles
======================================================================

順序なし目録（箇条書き）と順序付き目録（番号付き）の作成には段落スタイルを可能な
限り使用しろ。この目的のために二組の段落スタイルが用意されている。ただし、これら
のスタイルには箇条書きの種類や番号の位置などの設定オプションは含まれていない。こ
れらの設定は段落スタイルに付属させる目録スタイルから得られる。次に挙げる方法で一
緒に使え：

* 順序なし目録を作成するには、段落スタイル :guilabel:`List 1`, :guilabel:`List
  2`, :guilabel:`List 3`, ... などを使え。これらのスタイルは :guilabel:`Bullet`
  目録スタイルを用いる。
* 順序付き目録を作成するには、段落スタイル :guilabel:`Numbering 1`,
  :guilabel:`Numbering 2`, :guilabel:`Numbering 3` ... などを使え。これらのスタ
  イルは同名の目録スタイルを用いる。

段落スタイルを使えば、アウトラインのように目録項目の下に部分項目を持つ入れ子目録
を簡単に作成できる。これには追加レベルの設定を指定する必要がある。入れ子目録を設
定したら、項目の階層を簡単に変更することができる。

項目を一階層下げるには、キャレットを行頭（箇条書きまたは数字の後）に置き、
:kbd:`Tab` を押す。上げるには :kbd:`Shift` + :kbd:`Tab` を押す。

スタイルを使った目録の作成については :doc:`Chapter 8 <writer08>` と
:doc:`Chapter 9 <writer09>` でわかる。

Formatting lists directly
======================================================================

順序付き目録でも順序なし目録でも、書式を直接整えることが可能だ：

* :guilabel:`Bullets and Numbering` ツールバー
* 次のいずれかにある :guilabel:`Toggle Unordered List` と :guilabel:`Toggle
  Ordered List` 図像：

  * :guilabel:`Formatting` ツールバー
  * :guilabel:`Formatting (Styles)` ツールバー
  * Sidebar の :guilabel:`Properties` 甲板の :guilabel:`Paragraph` 盤
* :guilabel:`Bullets and Numbering` ダイアログボックス

単純な順序付き目録または順序なし目録を作成するには：

#. 目録内の段落を選択
#. Sidebarの :guilabel:`Paragraph` 盤で適切な図像をクリック

.. tip::

   最初にテキストを打ち込んでから番号や箇条書きを付けるか、打ち込みながら番号を
   付けるかは個人の好みの問題だ。

.. note::

   これらの方法で適用された箇条書きや番号付けは、メニューの
   :menuselection:`F&ormat --> Clear &Direct Formatting` コマンドを使用して削除
   することは不可能だ。:guilabel:`Formatting` ツールバーなどで関連する図像を切り
   替えることで、選択テキストからこれらをオフにしたり削除したりする。

Using the Bullets and Numbering toolbar
----------------------------------------------------------------------

入れ子になった一覧を作成するには :guilabel:`Bullets and Numbering` ツールバーの
図像を使用する。項目を目録の上下に移動したり、小番号や小箇条を作成したり、箇条書
きのスタイルを変更したり、番号や箇条書きのない段落を追加したり、より詳細なコント
ロールを含む :guilabel:`Bullets and Numbering` ダイアログボックスにアクセスした
りできる。

.. tip::

   キーバインドを使って、段落をアウトライン階層の上下に移動することができる。
   キャレットを段落番号の先頭に置き、次のキーを押す：

   * :kbd:`Tab` で階を下げる
   * :kbd:`Shift` + :kbd:`Tab` で階を上げる

.. tip::

   番号の付いた段落の先頭（つまり、番号の後でテキストの前）にタブストップを挿入
   するには :kbd:`Ctrl` + :kbd:`Tab` を押す。

:guilabel:`Bullets and Numbering` ツールバーの図像を使用して入れ子目録を作成する
と、目録のすべての階層に対して最初は同じ番号（または箇条書き）書式が適用される。
入れ子目録を作成するときに、番号付け形式と箇条書きの組み合わせを使用するには、次
のようにする：

#. 各目録項目をクリック
#. :guilabel:`Formatting` ツールバーまたは Sidebar の :guilabel:`Properties` 甲
   板にある :guilabel:`Toggle Unordered List` と :guilabel:`Toggle Ordered List`
   図像の下にあるドロップダウンパレットの選択肢から一つを選択

もっと良い方法が :doc:`Chapter 12 <writer12>` で述べられる。

Using the Bullets and Numbering palettes on the Sidebar
----------------------------------------------------------------------

Sidebar の :guilabel:`Properties` 甲板にある :guilabel:`Paragraph` 盤で、

* :guilabel:`Toggle Unordered List` コントロールの横にある▼をクリックすると箇条
  書きスタイルのパレットが開き、
* :guilabel:`Toggle Ordered List` コントロールの横にある▼をクリックすると、番号
  付けスタイルのパレットが開く。

これらのパレットの選択を使用して入れ子目録を作成し、:guilabel:`Bullets and
Numbering` ダイアログボックスにアクセスすることができる。Sidebar には
:guilabel:`Bullets and Numbering` ツールバーにあるような、目録内の項目を上下させ
るツールはない。

Using the Bullets and Numbering dialog
----------------------------------------------------------------------

:guilabel:`Bullets and Numbering` ダイアログボックスにはタブが六つある。次の四タ
ブではあらかじめ定義された記号と順序を選択できる：

* :guilabel:`Unordered`
* :guilabel:`Ordered`
* :guilabel:`Outline`: 標準的なアウトライン列から選択
* :guilabel:`Image`: 箇条書きの画像を選択

次の二タブは独自目録を定義するための詳細オプションを設けている：

* :guilabel:`Position`
* :guilabel:`Customize`

これらは :doc:`Chapter 12 <writer12>` で述べられる目録スタイル用のタブと同じだ。

Autoformatting
======================================================================

:guilabel:`AutoCorrect` ダイアログボックスの :guilabel:`Options` タブと
:guilabel:`Localized Options` タブで選択した内容に従って、Writer が文書の一部を
自動的に書式設定するように設定できる。

.. tip::

   文書内で予期せぬ書式変更が発生した場合、この場所で原因を探すとよい。

設定したオプションに従って自動的に書式を設定するには、:menuselection:`&Tools -->
AutoCorr&ect -->` サブメニューから項目をオンまたはオフにする。

:menuselection:`&While Typing`
   打ち込んでいる間に文書を自動的に整える。
:menuselection:`Appl&y`
   文書を自動的に整える。
:menuselection:`Apply and Edit &Changes`
   自動的にファイル内の書式を整え、ダイアログボックスを開いて変更を受理するか却
   下するかを選択する。
:menuselection:`&AutoCorrect Options...`
   :guilabel:`AutoCorrect` ダイアログボックスを開いて、所望の自動書式整形を選択
   する。

:guilabel:`Localized Options` タブは、引用符とアポストロフィー（閉じた一重引用符
のように見える）の書式を制御する。フォントのほとんどには巻いた引用符（スマート引
用符とも呼ばれる）が含まれているが、目的によっては（緯度と経度の分と秒を示すな
ど）真っ直ぐな引用符として書式設定したい場合がある。

.. tip::

   たいていの人はスマート引用符を AutoCorrect 設定にしておき、必要なときに
   :guilabel:`Special Character` ダイアログボックス (:doc:`Chapter 2
   <writer02>`) を使って真っ直ぐな引用符を挿入する。
