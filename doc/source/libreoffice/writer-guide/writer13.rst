======================================================================
Writer Guide Chapter 13, Tables ノート
======================================================================

.. include:: ./abbrev.txt

.. contents:: 章見出し
   :depth: 3
   :local:

Introduction
======================================================================

表組は大量の情報を整理して表示するのに便利な方法だ。例えば：

* 技術、財務、統計報告書
* 製品の説明、価格、特性、写真を示す目録
* 請求書または請求書
* 住所、年齢、職業、その他の情報を含む名簿

表組は資料を整理するためにスプレッドシートの代わりとしてよく使われる。巧みに設計
された表は、読者が著者の主張したいことをよりよく理解するのに役立つ。通常、表組は
テキストや数字に用いるが、写真など他の物を升目に入れることもできる。
:ref:`writer13-anchor-spreadsheet` を参照。

また、表組をページレイアウトのツールとして使うことで、複数のタブ文字を使う代わり
に、文書内の領域にテキストを配置することもできる。他の例としては、ヘッダーやフッ
ターで、ページ番号や文書表題など、異なる要素の独立した配置を援護することがある。
このような表組の使い方については |Chapter06| で述べられている。

Tools for working with tables
======================================================================

.. |TableToolbar| replace:: :guilabel:`Table` ツールバー
.. |PropertiesDeck| replace:: :guilabel:`Properties` 甲板
.. |TablePanel| replace:: :guilabel:`Table` 盤

この章で説明する表組コマンドのすべては、メニュー :menuselection:`T&able-->` と
|TableToolbar| にある。また、表組のコンテキストメニューや Sidebar
|PropertiesDeck| |TablePanel| にもある。

表組を作成したり、既存の表組を選択すると、自動的に |TableToolbar| が表示される。
ツールバーの入渠と浮動、およびツールバー上の特定のツールの表記切り替え方法につい
ては |Chapter01| を見ろ。

.. admonition:: 読者ノート

   本書ではここに |TableToolbar| の図解が示されている。さしずめ図表コマンド図鑑
   というところだ。

キャレットが表組内にある場合、Sidebar |PropertiesDeck| は表組性質を含む。

Creating a table
======================================================================

Writer 文書で表組を作成する前に、視覚的な仕上がりの想定と、必要な行数と列数の見
積もりを持っておくと便利だ。引数のすべては後で変更可能だが、完全に整形された表組
の変更には多大な労力を要しがちだため、前もって考えておくと時間の節約になる。

.. _writer13-anchor-new:

Creating a new table
----------------------------------------------------------------------

.. |InsertTableDlg| replace:: :guilabel:`Insert Table` ダイアログボックス

既定性質で表組をすばやく作成するには、|StandardToolbar| :guilabel:`Insert Table`
図像をクリックする。ドロップダウン小窓で表組の規模を選択する。最後の列の最後の行
にしたい升目をクリックして表組を作成する。

新しい表組を作成し、表の性質を指定するには、表組を表示したい場所にキャレットを置
き、次のいずれかの方法で |InsertTableDlg| を開く：

* メニュー :menuselection:`T&able --> Insert &Table...` を選択
* キーバインド :kbd:`Ctrl` + :guilabel:`F12`
* |StandardToolbar| で :guilabel:`Insert Table` 図像をクリックし、ドロップダウ
  ン小窓の下部にある :guilabel:`&More Options...` を選択

|InsertTableDlg| :guilabel:`General` 区画 :guilabel:`&Name` 欄に、Writer が生成し
た既定名とは異なる名前を入力できる。これは、Navigator を使用して表組にすばやく飛
ぶ場合に便利だ。

:guilabel:`&Columns` 欄と :guilabel:`&Rows` 欄で新しい表組の列と行の数を指定する。
必要に応じて、後で表組の寸法を変更することができる。

:guilabel:`Options` で初期表組特性を設定する：

:guilabel:`Hea&ding`
   表組内で見出しを使用できるようにし、見出しとして使用する行数を定義する。二行
   目、場合によっては三行目の見出しは、複雑な表組の小見出しに便利だ。

   既定の表見出し段落スタイルは見出し行に適用される。これらの既定設定を変更する
   には、表見出し段落スタイルを編集する。
:guilabel:`Repeat heading rows on new &pages`
   表組が複数のページにまたがる場合、見出し行が後続ページの先頭で繰り返されるよ
   うにする。
:guilabel:`Heading ro&ws`
   見出しに使用する行数を指定する。既定は 1 だ。
:guilabel:`Don't &split table over pages`
   表が複数のページにまたがるのを防ぐ。これは、表組がページの終わり近くで始ま
   り、次のページに完全に配置されていた方が見栄えが良かった場合に便利だ。図表が
   ページの早い位置から始まっているが、すべて収まらない場合、この設定はページの
   区切りが不格好になる可能性がある。図表が一ページに収まらないほど長くなる場合
   は、このオプションをオフにするか、図表を手動で分割しろ。

:guilabel:`Styles` 区画には表組スタイルとしても知られる、いくつかの定義済み表組
レイアウトが一覧されている。:ref:`writer13-anchor-styling` を参照。一覧から希望
の表組オプションを選択し、下見することができる。

選択したら、:guilabel:`&Insert` を押す。テキストエリアと同じ幅（左ページの余白か
ら右ページの余白まで）の表組が作成され、すべての列と行がそれぞれ同じ幅と高さにな
る。列と行は必要に応じて後で調整可能。

Creating nested tables
----------------------------------------------------------------------

表組の中に表組を作成し、想像力と実用性によってのみ制限される深さまで入れ子にする
ことができる。入れ子の表組は特にページレイアウトに便利だ。これを実現するには、既
存の表組の升目をクリックし、上記の :ref:`writer13-anchor-new` で述べた方法のいず
れかを使用する。

Using AutoCorrect to create a table
----------------------------------------------------------------------

プラス記号で区切られたハイフンやタブを連続して入力して表組を作成することもでき
る。

* プラス記号は列の区切りを示すのに使用し、
* ハイフンやタブは列の幅を示すのに使用する。

この設定は |Options| :menuselection:`LibreOffice Writer-->General` ページで変更
できる。

例えば、この文字列：

.. code:: text

   +-----------------+---------------+------+

はこのような表組を作成する：

.. csv-table::
   :widths: 17, 15, 6

   ,,

.. note::

   この機能は :menuselection:`&Tools-->AutoCorr&ect-->&AutoCorrect Options...`
   で有効性を切り替えられる。:guilabel:`Options` ページで :guilabel:`Create
   table` のオンオフを切り替える。

Creating a table from formatted text
----------------------------------------------------------------------

.. |TextToTable| replace:: :menuselection:`T&able-->&Convert-->&Text to Table...`

書式付きテキストから表組を作成するには、テキストを選択し、メニューから
|TextToTable| を選択する。変換するテキストには列の区切りを示す文字が含まれていな
ければならない。段落マークは表組の行の終わりを示す。

.. tip::

   他の方法による表組の作成とは異なり、テキストから表組への変換では、元のテキス
   トに適用された段落スタイルと文字スタイルが保持される。

   #. 必要に応じてテキストを編集し、列の区切り文字が必要な位置にあることを確認す
      る。変換するテキストを選択し、|TextToTable| を選択して、:guilabel:`Convert
      Text to Table` ダイアログボックスを開く。
   #. :menuselection:`Separate Text At` 区画にはテキストの列の区切り文字として四
      つのオプションがある。既定のカンマを選択するか、ボックスに任意の文字を入力
      するには :guilabel:`Othe&r` を選択、指定する。

      オプションは |InsertTableDlg| と同じだ。
   #. |OK| を押してテキストを変換する。

Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

この例では、以下のテキストを表に変換する。

| Row 1 Column 1; Row 1 Column 2; Row 1 Column 3
| Row 2 Column 1; Row 2 Column 2; Row 2 Column 3

この場合、要素間の区切りはセミコロンだ。テキストを選択し、|TextToTable| を選択す
る。次のような結果が得られる：

.. csv-table::
   :delim: ;
   :widths: auto

   Row 1 Column 1; Row 1 Column 2; Row 1 Column 3
   Row 2 Column 1; Row 2 Column 2; Row 2 Column 3

.. tip::

   表組をプレーンテキストに変換することもできる。表組の内容を別のプログラムにエ
   クスポートする場合に便利だ。表組の任意の場所にキャレットを置き、メニューから
   :menuselection:`T&able-->&Convert-->T&able to Text...` を選択し、好みの行区切
   り文字を選んで |OK| を押して終了する。

Inserting a portion of a spreadsheet
----------------------------------------------------------------------

スプレッドシート領域を Writer 文書に Writer 表組としてコピーする手順：

#. Writer 文書とスプレッドシートの両方を開く。
#. コピーしたいシート領域を選択し、

   * コンテキストメニューから :menuselection:`&Copy` を選択するか、
   * |Ctrl+C| を押す。

#. Writer 文書内をクリックして

   * コンテキストメニューから :menuselection:`&Paste` を選択するか、
   * |Ctrl+V| を押す。

   あるいはコピーしたい領域を Writer 文書にドラッグする。

Writer 文書にスプレッドシートを挿入する他の方法については |Chapter19| も見ろ。

Formatting the table layout
======================================================================

表組の書式設定は、表組のレイアウトの書式設定（この節の主題）と、表組のテキストの
書式設定（次節）の二段階で行う。

.. tip::

   表組レイアウトや表組テキストの同様の書式を複数の表組に適用する場合、表組スタ
   イルを使用することで作業を高速化し一貫性を持たせることができる。
   :ref:`writer13-anchor-styling` を見ろ。

レイアウトの書式整形には次の操作の一つ以上が含まれる：

* 表組の寸法とページ上の位置の調整
* 行や列の寸法の調整
* 行や列の追加や削除
* 個々の升目の結合や分割
* 境界や背景の変更

Default parameters
----------------------------------------------------------------------

|InsertTableDlg| または |StandardToolbar| :guilabel:`Insert Table` 図像を使用し
て表組を作成する場合、次の既定が設定される：

* 升目は `Table Contents` 段落スタイルを使用する。既定雛形では、このスタイルは
  `Default Paragraph Style` と同じだ。
* 既定表組は余白から余白（テキスト領域）までのすべての場所を占有する。
* 既定表組には格子に細い黒い縁取りがある。
* :guilabel:`Hea&ding` オプションを有効にすると、見出し行（複数行の場合がある）
  の升目は `Table Heading` 段落スタイルを使用する。

.. _writer13-anchor-dialog:

Resizing and positioning the table
----------------------------------------------------------------------

表組のサイズを素早く変更するには、

#. まずマウスポインターを左辺か右辺に移動させる。
#. ポインターの形が変わったら境界線を新しい位置までドラッグする。

この方法は最初か最後の列のサイズを変更するだけで、ページ上の表組の配置は変更しな
い。

.. |TablePropertiesDlg| replace:: :guilabel:`Table Properties` ダイアログボックス

ページ上の表組の寸法と位置を精密に制御するには |TablePropertiesDlg| を使用する。
出現させるには次のいずれかを行う：

* メニューの :menuselection:`T&able-->&Properties...` を選択
* 表組の任意の場所を右クリックしてコンテキストメニューから
  :menuselection:`&Table Properties...` を選択
* Sidebar |PropertiesDeck| |TablePanel| :guilabel:`More Options` をクリック

.. |Spacing| replace:: :guilabel:`Spacing`
.. |Automatic| replace:: :guilabel:`A&utomatic`
.. |Left| replace:: :guilabel:`&Left`
.. |Right| replace:: :guilabel:`R&ight`
.. |From left| replace:: :guilabel:`&From left`
.. |Center| replace:: :guilabel:`&Center`
.. |Manual| replace:: :guilabel:`&Manual`

ダイアログボックスの |TableTab| では表組の揃え方を設定できる：

|Automatic|
   既定設定。テキストエリアの幅を埋める。
|Left|
   表組を左余白に揃える。
|Right|
   表組を右余白に揃える。
|From left|
   表組を左余白からどのくらい離れた位置に揃えるかを |Spacing| で指定。
|Center|
   表組を左余白と右余白の中間に配置する。表組の幅が余白より大きい場合、表組は余
   白の外にはみ出る。
|Manual|
   左右の余白からの距離を |Spacing| で指定。

|Automatic| 以外の整列オプションを選択すると、:guilabel:`Properties` 区画の
:guilabel:`W&idth` 欄が活動を開始し、表組の希望の寸法を入力できる。
:guilabel:`Relati&ve` をオンにすると、テキスト領域に対する幅の割合が表示される。

|Spacing| 区画で :guilabel:`&Above` と :guilabel:`&Below` 欄を使い、テキストと表
組の間隔を変更する。

表組の寸法がテキストエリアのそれより小さい場合、|Left| と |Right| にはいくらかの
値が書き込まれる。そうでない場合は、これらの値は利用不可だ。値を入力することがで
きるのは：

* |Manual| で揃え方を選択する場合は |Left| と |Right| の両方の欄
* |From left|, |Right|, |Center| のいずれかを選択した場合は |Left| 欄
* |Left| を選択した場合は |Right| 欄

.. admonition:: 読者ノート

   |TablePropertiesDlg| には :guilabel:`Properties` 区画が二つある気がする。

Specifying text flow
----------------------------------------------------------------------

.. |TableTab| replace:: :guilabel:`Table` タブ
.. |TextFlowTab| replace:: :guilabel:`Text Flow` タブ
.. |PositionTab| replace:: :guilabel:`Position` タブ

|TablePropertiesDlg| |TextFlowTab| では次のことができる：

* 表組の前後に改頁または改段をはめ込む。:guilabel:`&Break` オプションを、

  * :guilabel:`&Page` または :guilabel:`Col&umn` と、
  * :guilabel:`Be&fore` または :guilabel:`&After`

  オプションと組み合わせて使用する。表組の前に改頁を挿入する場
  合、:guilabel:`With Page St&yle` と新しいページスタイルを選択することで、改頁
  に使用するページスタイルを変更することもできる。改頁と同様に、:guilabel:`Page
  &number` 欄を使ってページ番号をリセットすることもできる。
* :guilabel:`Allow &table to split across pages and columns` をオフにして、表組
  を一ページに収める。この項目がオフの間、次の項目は活動停止になる。
* :guilabel:`Allow row to break a&cross pages and columns` をオフにして各行を一
  ページで保持する。
* 改頁を挿入した場合、表組と直後の段落を一緒に保つには :guilabel:`&Keep with
  next paragraph` を使用しろ。
* 各ページで繰り返される表組の見出し行の数を選択するには :guilabel:`R&epeat
  heading` とそれに関連する数値欄を使用する。複雑な表組では読みやすく理解しやす
  くするために二、三行の見出し行が必要になることがある。
* :guilabel:`Text &orientation` ドロップダウンリストを使って升目内のテキストの向
  きを次から選択する：

  * :guilabel:`Horizontal`
  * :guilabel:`Vertical (top to bottom)`
  * :guilabel:`Vertical (bottom to top)`
  * :guilabel:`Use superordinate object settings`: ページの既定テキスト流し込み
    設定を用いるの意
* 表組または選択升目内のテキストの垂直方向揃え方を選択する。選択肢は

  * 升目の上端に揃える
  * 升目の中央に揃える
  * 升目の下端に揃える

  だ。この整列は |TablePropertiesDlg| |TableTab| で利用できる左右の整列オプショ
  ンに加えて行われる。

.. note::

   表組の見出し行は二ページにまたがることはできないが、他の行は可能だ。一行の表
   組（しばしばページレイアウトの目的で使用される）は既定で見出しを含むように設
   定されている場合、ページをまたいで分割されることはない。解決策は、表組が見出
   し行なしで定義されていることを確認することだ。

Resizing rows and columns
----------------------------------------------------------------------

表組の行の高さや列の幅はいくつかの方法で調整できる。

* マウスポインターを升目の端の横に移動し、両頭の矢印が表示されたら、マウス左ボタ
  ンをクリックしたまま、境界線を希望の位置までドラッグし、マウスボタンを放す。
* 水平定規では、列の区切りは二本の細い灰色の線で示され、垂直定規でも同様に行の区
  切りが示される。行または列の寸法を変更するには、該当する仕切りの上でマウスボタ
  ンを押したまま、希望の位置までドラッグする。
* 以下で述べられるようにキーボードを使用する。

メニューから :menuselection:`T&able-->Si&ze-->` 以下の項目に寸法変更のオプション
がいくつか用意されている：

* :menuselection:`&Column Width...` または :menuselection:`&Row Height...` を選
  択して、表組の選択可能な各列または行の寸法欄に数値を入力する。
* :menuselection:`Minimial Column &Width` または :menuselection:`&Minimal Row
  Height` は選択された列または行の幅をできるだけ狭くし、なおかつその内容を収まる
  ようにする。行または列は、すべて同じ高さまたは幅になるとは限らない。
* :menuselection:`O&ptimal Column Width` または :menuselection:`&Optimal Row
  Height` は選択された列または行を、任意の行の最大文字または任意の列の最長項目に
  合うようにする。
* :menuselection:`&Distribute Columns Evenly`, :menuselection:`Distribute Rows
  &Evenly` をそれぞれ使って、すべての列と行を同じ幅または高さにそれぞれ戻すこと
  ができる。

.. |ColumnsTab| replace:: :guilabel:`Columns` タブ

各列の幅をより細かく制御するには |TablePropertiesDlg| |ColumnsTab| を用いる。

* メニューの :menuselection:`T&able-->&Properties...` を選択するか、
* 表組の任意の場所を右クリックしてコンテキストメニューから
  :menuselection:`&Table Properties...` を選択するか、
* Sidebar |PropertiesDeck| |TablePanel| :guilabel:`More Options` をクリック

する。|TablePropertiesDlg| で |ColumnsTab| を選択する。

.. |AdaptTableWidth| replace:: :menuselection:`Adapt table &width`

* |AdaptTableWidth|: 表組がすでにページ余白まで伸びている場合、それ以上幅を広げ
  ることはできず、|AdaptTableWidth| オプションは列幅を縮小するためにのみ使用でき
  る。表の幅が狭い場合、列の幅を広げると表全体の幅が広がります。|TableTab|
  :guilabel:`Alignment` 区画で |Automatic| が選択されている場合、このオプション
  を使用できない。

  |AdaptTableWidth| がオンの状態で表組の幅がすでに余白を超えて広がっている場合、
  列の幅を変更しようとするとその列の寸法が自動的に縮小され、他の列の寸法はそのま
  まに、表組がページの余白まで縮小される。
* :guilabel:`Ad&just columns proportionally` をオンにすると、一つの列が変更され
  たときに、列のすべての幅が同じ割合で変更される。たとえば、ある列のサイズを半分
  にすると、他のすべての列のサイズも半分になる。|TableTab| :guilabel:`Alignment`
  区画で |Automatic| が選択されている場合、このオプションを使用できない。
* :guilabel:`&Remaining space` は余白の限界にぶつかる前に、表組があとどれくらい
  拡大できるかを示す。この値は読み取り専用で、表組の幅がすでに左右の余白の間の広
  さより大きい場合、負の値にはならない。
* :guilabel:`Column width` では個々の列を調整することができる。列が六つ以上ある
  場合は、右と左にある矢印を使用して、すべての列を表示する。オプションが選択され
  ていない場合、表組の幅を一定に保つため、調整中の列の右側の列が自動的に変更され
  る。一番右の列を調整すると、最初の列が変更される。

.. tip::

   |TablePropertiesDlg| から始めるよりも、マウスを使って新しい表組の大まかな調整
   を行い、|TablePropertiesDlg| の |ColumnsTab| と |TableTab| タブを使ってレイア
   ウトを微調整する方が効率的な場合が多い。

キーボードを使って表組の寸法を変更することもできる：

#. 変更したい升目にキャレットを置く。
#. :kbd:`Alt` を押しながら矢印キーを使う。

   * 左と右の矢印キーは、升目の右端の境界を動かして列幅を調整する。
   * 上下の矢印キーは、升目の下端の境界を動かすことで、行の高さを調整する（可能
     な場合）。

.. admonition:: 読者ノート

   この操作は Calc スプレッドシートでも成立するようだ。

.. |ConfigTable| replace:: :menuselection:`LibreOffice Writer-->Table` ページ

寸法変更引数とキーボード操作の動作を調整するには |Options| |ConfigTable| を開く。

:guilabel:`Move cells` 区画の :guilabel:`&Row` と :guilabel:`&Column` の値を使用
して、寸法変更中にワンストロークで生じる変更量を決定する。:guilabel:`Behavior of
rows/columns` 区画では寸法変更時に次の計略から一つを選択できる：

:guilabel:`&Fixed`
   寸法変更は隣接する升目に限定的に影響し、表組全体には影響しない。升目の寸法を
   変更しても、表組の幅は変化しない。
:guilabel:`Fi&xed, proportional`
   升目の寸法を変更すると、他の升目すべても比例して寸法変更されるが、表組の幅を
   維持するために反対方向に変更される。
:guilabel:`&Variable`
   升目の寸法変更が表組の寸法に影響する。例えば、升目を広げると表組の幅が広が
   る。これが既定の選択肢だ。

Inserting rows and columns
----------------------------------------------------------------------

行または列をすばやく挿入するには、追加したい場所の前後にキャレットを置き、次のい
ずれかを実行する：

* 選択行の上または下に行を挿入するには、次のいずれかにある :guilabel:`Rows
  Above` 図像または :guilabel:`Rows Below` 図像をクリック：

  * |TableToolbar|
  * Sidebar |PropertiesDeck| |TablePanel|
* 選択列行の前または後ろに列を挿入するには、次のいずれかにある
  :guilabel:`Columns Before` 図像または :guilabel:`Columns After` 図像をクリッ
  ク：

  * |TableToolbar|
  * Sidebar |PropertiesDeck| |TablePanel|
* 次のメニュー項目のいずれかを選択：

  * :menuselection:`T&able-->&Insert-->Rows &Above`
  * :menuselection:`T&able-->&Insert-->Rows &Below`
  * :menuselection:`T&able-->&Insert-->Columns B&efore`
  * :menuselection:`T&able-->&Insert-->Columns A&fter`

* 右クリックメニューから次のいずれかを選択：

  * :menuselection:`&Insert-->Rows &Above`
  * :menuselection:`&Insert-->Rows &Below`
  * :menuselection:`&Insert-->Columns B&efore`
  * :menuselection:`&Insert-->Columns A&fter`

任意の個数の行または列をはめるには：

#. 新しい行または列を追加したい場所にキャレットを置く。
#. 次のいずれかを選択する：

   * メニューから :menuselection:`T&able-->&Insert-->&Rows...`
   * メニューから :menuselection:`T&able-->&Insert-->&Column...`
   * 右クリックメニューから :menuselection:`&Insert-->&Rows...`
   * 右クリックメニューから :menuselection:`&Insert-->&Column...`

#. :guilabel:`Insert Rows` や :guilabel:`Insert Columns` ダイアログボックスで追
   加する行または列の数と、選択した行または列の前に追加するか後に追加するかを選
   択する。

   * :guilabel:`&Number` に挿入する行数または列数を設定
   * :guilabel:`Position` に :guilabel:`&Before selection`, :guilabel:`&Above
     selection`, :guilabel:`&After selection`, :guilabel:`&Below selection` のい
     ずれかを設定
#. |OK| を押してダイアログボックスを閉じる。

.. tip::

   どのように挿入されたかにかかわらず、新しい行や列は、キャレットが位置した行や
   列と同じ書式を持つ。

Deleting rows and columns
----------------------------------------------------------------------

行または列をすばやく削除するには、削除したい行または列を選択し、次のいずれかを実
行する：

* 次のいずれかにある :guilabel:`Delete selected rows` または :guilabel:`Delete
  selected columns` 図像をクリック：

  * |TableToolbar|
  * Sidebar |PropertiesDeck| |TablePanel|
* 右クリックメニューから次のいずれかを選択：

  * :menuselection:`&Delete-->&Rows`
  * :menuselection:`&Delete-->&Columns`
* メニュー項目の次のいずれかを選択：

  * :menuselection:`T&able-->&Delete-->&Rows`
  * :menuselection:`T&able-->&Delete-->&Columns`

Merging and splitting cells
----------------------------------------------------------------------

升目を融合する普通の使い方としては、表組の幅全体を占める見出し行や、複数列にまた
がる小見出し行を作ることがある。

升目のグループを一つに統合する手順：

#. 結合する升目を選択する
#. 次のいずれかを行う：

   * 右クリックし :menuselection:`Merg&e Cells` を選択
   * メニューから :menuselection:`T&able-->&Merge Cells` を選択
   * |TableToolbar| にある :guilabel:`Merge Cells` をクリック
   * Sidebar |PropertiesDeck| |TablePanel| にある :guilabel:`Merge Cells` をク
     リック

   升目の内容すべては融合した升目に現れる。

升目を複数の升目に分割する手順：

.. |SplitCells| replace:: :guilabel:`Split Cells`

#. キャレットを升目内に置く
#. 次のいずれかを行う：

   * 右クリックし :menuselection:`Split Cells...` を選択
   * メニューから :menuselection:`T&able-->Sp&lit Cells...` を選択
   * |TableToolbar| にある |SplitCells| をクリック
   * Sidebar |PropertiesDeck| |TablePanel| にある |SplitCells| をクリック

#. |SplitCells| ダイアログボックスで升目の分割方法と作成する升目の数を選択する。
   升目は水平方向（行が増える）または垂直方向（列が増える）に分割できる。

升目の結合や分割は他のレイアウト書式設定が完了した後に行うのが一般には最善だ。列
や行を削除するような操作の中には、升目の結合や分割がなされた表組に適用すると、結
果が予測しにくくなるものがある。

Specifying table borders
----------------------------------------------------------------------

.. |BordersTab| replace:: :guilabel:`Borders` タブ
.. |UserDefinedArea| replace:: :guilabel:`&User-defined` 部分

表組の境界を素早く適用するには、次のいずれかを用いる：

* |TableToolbar| の :guilabel:`Borders`, :guilabel:`Border Style`,
  :guilabel:`Border Color` 各図像のドロップダウンパレット
* Sidebar |PropertiesDeck| |TablePanel|

より詳細に制御するには |TablePropertiesDlg| |BordersTab| を用いる。

:guilabel:`Line Arrangement`
   枠線がどこに来るのかを指定する。升目グループが選択されている場合、その境界は
   それらの升目にしか適用されない。選択された升目の外縁と升目分割の枠線のスタイ
   ルを個別に指定することができる。Writer は既定の配置を用意しているが、
   |UserDefinedArea| でカスタマイズしたい行をクリックすることで、自在の配置にす
   ることができる。升目が複数選択されている場合、その仕切り線だけでなく、選択範
   囲の辺も選択することが可能だ。

   .. note::

      選択された升目に異なるスタイルの枠線がある場合、|UserDefinedArea| には枠線
      が灰色の線で表示される。灰色の線をクリックする回数で、境界スタイルが順次切
      り替わる：

      #. 新しい境界スタイルを選択
      #. 境界をそのままにする
      #. 境界を削除する

:guilabel:`Line`
   境界の体裁を指定する。:guilabel:`St&yle` と :guilabel:`&Color` ドロップダウン
   リストから選択し、:guilabel:`&Width` を指定することができる。指定内容が
   |UserDefinedArea| の黒い矢印で強調表示された枠線に適用される。
:guilabel:`Padding`
   境界と升目内容の間にどれだけの間隔を残すかを指定する。間隔は左右上下の境界に
   対して個別に指定できる。:guilabel:`&Synchronize` をオンにすると四辺の間隔が等
   しくなる。
:guilabel:`Shadow Style`
   ここにある性質は常に表組全体に適用される。影は次の三成分からなる：

   * 位置
   * 表組からの距離
   * 色
:guilabel:`&Merge adjacent line styles`
  これがオンだ場合、境界を共有する二つの升目では、その境界が横並びや上下にな
  るのではなく、融合する。

.. tip::

   |TablePropertiesDlg| |BordersTab| ですべてをリセットするには、
   :guilabel:`Pr&esets` にある :guilabel:`No Borders` 図像をクリックする。

Selecting background colors and images
----------------------------------------------------------------------

.. |BackgroundTab| replace:: :guilabel:`Background` タブ

表組の背景はデータの可読性を大幅に向上させたり、重要な部分（見出しや特定の升目な
ど）を視覚的に強調したり、表組をより魅力的にする。背景は無地と画像の二種類から選
択可能だ。背景は、表組全体、単一の升目、行のいずれに対しても適用可能だ。

* |TableToolbar| :guilabel:`Table Cell Background Color` 図像
* |PropertiesDeck| |TablePanel| にあるドロップダウンパレット

を使用すると、升目の背景に色をすばやく適用できる。さらに操作したい場合や、画像を
背景に使用したい場合は、|TablePropertiesDlg| |BackgroundTab| を使用する。

.. tip::

   背景と前景（通常はテキスト）の色の対比を考量しろ。背景色や画像は、テキストを
   より読みやすくするために透明度を適用することもできる。行背景オプションは別の
   色の行を作成したり、表の見出しに別の背景を割り当てたりするのにとても便利だ。

.. note::

   升目に対して選択した背景は行の背景の手前にあり、行の背景は表の背景の手間にあ
   る（隠れる）。

升目、行、表組の背景を設定する手順

#. キャレットを作業したい升目、行、表組内の任意の場所に置く。升目のグループに背
   景を適用したい場合はグループを選択する。
#. :ref:`前述<writer13-anchor-dialog>` の方法で |TablePropertiesDlg| を開く。
#. |BackgroundTab| をクリック。
#. 設定を升目、行、表組のいずれに適用するかを選択する。

   :guilabel:`Cell`
      変更は選択された升目、またはキャレットが現在ある升目にしか適用されない。升
      目が複数選択されている場合でも背景設定は各升目に個別に適用される。
   :guilabel:`Row`
      変更はキャレットがある行全体に影響する。
   :guilabel:`Table`
      キャレットの位置や選択されている升目に関係なく、変更は表全体の背景を設定す
      る。
#. 色を適用するには :guilabel:`Color` ボタンを押し、色を選択して |OK| を押す。
#. 画像を適用するには :guilabel:`Image` ボタンをクリックする。それから、

   * 与えられた画像から選択するか、:guilabel:`Add / Import` ボタンを押す。
   * :guilabel:`Options` で画像の配置型を選択する。

     :guilabel:`Style`
        画像を表示する方法：カスタム位置・寸法、タイル状、伸縮
     :guilabel:`Size`
        必要な画像の縦横比または尺度オプションを選択
     :guilabel:`Position`
        画像を表示する場所
   * 画像を適用するには |OK| を押す。

Displaying or hiding table boundaries
----------------------------------------------------------------------

表組境界とは、LibreOffice で境界線を有効にしていない状態で画面を表示したときに升
目の周囲に表示される薄い線の集合だ。通常は灰色だ。これらの境界線は印刷されない。
表組をページレイアウトに使用する場合に特に便利だ。

印刷ページと同じように、境界線なしで表を画面に表示するには、
:menuselection:`&View-->Table Boundaries` をオフにするか、|Options|
:menuselection:`LibreOffice-->Application Colors` ページで、テキスト、表、ヘッ
ダーとフッター、図、文書のその他の部分の境界線有無を切り替えたり、境界線の色を選
択したりできる。

境界線をオフにしても表組の境界線は隠されない。

.. _writer13-anchor-styling:

Creating and applying table styles
======================================================================

表組スタイルを使用すると、数回クリックするだけで凝った書式を適用できる。他のスタ
イルと同様に、表組スタイルを使用すると文書内で一貫した体裁の表組を作成できる。

Applying a table style
----------------------------------------------------------------------

.. |StylesDeck| replace:: :guilabel:`Styles` 甲板
.. |TableStyles| replace:: :guilabel:`Table Styles`
.. |AutoFormatDlg| replace:: :guilabel:`AutoFormat` ダイアログボックス

表組スタイルを適用するには、Sidebar |StylesDeck| |TableStyles| 図像をクリックす
る。表組の任意の場所にキャレットを置き、スタイル名をダブルクリックする。

より詳細に制御するには、メニューの :menuselection:`T&able-->AutoFormat
Styles...` を選択するか、|TableToolbar| :guilabel:`AutoFormat Styles` 図像をク
リックする。|AutoFormatDlg| で一覧から書式を選択し、表組に使用する機能（フォント、
配置、枠線など）を選択して |OK| を押す。表組が整形される。

.. tip::

   書式を選択し、:guilabel:`Rename` ボタンを押すと書式の名前を変更できる。このダ
   イアログボックスと Sidebar |TableStyles| ページで名前が変更される。

   書式を選択して :guilabel:`Delete` ボタンを押すと書式を削除できる。ただし、
   `Default Table Style` を変更したり削除したりすることはできない。

Creating a table style
----------------------------------------------------------------------

Sidebar |StylesDeck| |TableStyles| タブには表組スタイルを素早く適用する方法があ
るが、これらは AutoFormat 機能を使用して作成される。次の手順だ：

#. 表組を作成する。フォント、配置、枠線、背景、番号の書式など、好きなように書式
   を設定する。
#. 表組の任意の場所にキャレットを置く。前述の方法で |AutoFormatDlg| を開く。
#. ダイアログボックスで新しい表スタイルに含める書式を選択し、:guilabel:`&Add` ボ
   タンを押す。
#. ポップアップダイアログボックスで新しいスタイルの名前を入力する。
#. |OK| を押す。

新しいスタイルは |AutoFormatDlg| の書式一覧と、Sidebar |StylesDeck| |TableStyles|
一覧に追加される。

表組スタイルは次の表組レベル性質も含む：

* Break
* Keep with next paragraph
* Repeat heading
* Allow table to split across pages
* Allow rows to break across pages
* Merge adjacent line styles
* Table shadow

.. tip::

   これらのスタイルには表型書式の表幅と列幅は含まれない。あらかじめ定義された完
   全な書式で表を挿入するには、それを AutoText として保存しろ。|Chapter02| を見
   ろ。

Formatting the table text
======================================================================

表組のレイアウトを設定したら、個々の升目内のテキストの書式設定に着手できる。テキ
スト内の他の段落と同様に、手動で書式を適用することもできるが、一貫性と保守のしや
すさを考慮し、段落スタイルと文字スタイルを使用する。その他に考慮すべき点として
は、テキストの流し込み、桁揃え、向きがある。

各升目を他の升目から独立して書式設定することもできるし、升目を選択してから書式設
定することで、複数の升目を同時に書式設定することもできる。

.. tip::

   基本表組テキスト書式整形は、表組スタイルを選択し、変更したい升目だけを変更す
   ることで適用できる。

Vertical alignment
----------------------------------------------------------------------

既定では、表組に入力されたテキストは升目の左上に揃えられる。上記のように表組全体
の既定を変更することも、個別に選択した升目の既定を変更することもできる。

特定の升目のテキストを縦に揃えるには：

#. 変更したい升目にキャレットを置くか、複数の升目を選択する。
#. |TableToolbar| の図像をクリックする：

   * :guilabel:`Align Top`,
   * :guilabel:`Center Vertically`
   * :guilabel:`Align Bottom`

Number formats
----------------------------------------------------------------------

数値書式は、表組全体、升目グループ、または単一の升目に設定できる。例えば、升目を
特定の通貨で表示したり、小数点以下四桁で表示したり、特定の日付形式で表示したりす
ることができる。

数値認識では、テキスト表内の数値を認識し、数値として書式設定する。
:guilabel:`&Number recognition` が選択されていない場合、数値はテキスト形式で保存
され、自動的に左揃えになる。数値認識を有効にするには、|Options| |ConfigTable| で
:guilabel:`Input in Tables` 区画のオプションを選択する。

升目の数値書式を設定するには、升目を選択してから次のいずれかを行う：

* |TableToolbar| の一般的な書式の図像をクリック
* メニューから :menuselection:`T&able-->&Number Format...` を選択

.. |FormatNumberDlg| replace:: :guilabel:`Format Number` ダイアログボックス

|FormatNumberDlg| では、数値データのさまざまな区分のオプションを設定できる。

* :guilabel:`C&ategory` 一覧で通貨、日付、テキストなど、必要な区分を選択する。
* :guilabel:`Fo&rmat` 一覧で選択した区分の書式を選択する。
* 日付のようないくつかの区分では :guilabel:`&Language` 一覧を使用して言語を変更
  することができる。

.. tip::

   ダイアログボックスの下部にある :guilabel:`Format Code` 区画に選択した区分と書
   式に対応する書式コードを表示する。例えば、``31 Dec 1999`` のような日付形式を
   選択した場合、対応するコードは ``D MMM YYYY`` となる。上級使用者はこの書式
   コードを簡単にカスタマイズしたり、新しい使用者定義コードを作成することができ
   る。

Rotating text in a table cell
----------------------------------------------------------------------

表の升目内のテキストを 90 度または 270 度回転させることができる。テキストの回転
は狭い列に長い見出しを付ける場合に便利だ。

* 回転させるテキストを選択し、:menuselection:`F&ormat-->C&haracter...` を選択す
  るか、右クリックしてコンテキストメニューから
  :menuselection:`C&haracter-->C&haracter...` を選択する。
* |PositionTab| の :guilabel:`Rotation / Scaling` 区画で回転角度を選択し、オプ
  ションで :guilabel:`Scale &width` を変更し、|OK| を押す。

.. note::

   表升目内のテキストの回転は |Chapter09| で説明する段落スタイルの使用でも実現で
   きる。

Data entry and manipulation in tables
======================================================================

Moving between cells
----------------------------------------------------------------------

表内の升目間を移動するには、マウス、矢印キー、または :kbd:`Tab` を使用する。

矢印キーはキャレットを左右に一文字ずつ移動させる。升目が空の場合、矢印キーを押す
と隣の升目にキャレットが移動する。

:kbd:`Tab` は次の升目に直接移動し、キャレットが表組の最後の升目にある場合は新し
い行を作成する。:kbd:`Shift` + :kbd:`Tab` を押すと、キャレットが一升戻る。

.. tip::

   升目のテキストの一部として Tab 文字を入力するには、:kbd:`Ctrl` + :kbd:`Tab`
   とする。

表組の最初や最後に移動するには、それぞれキーバインド

* :kbd:`Ctrl` + :kbd:`Home`
* :kbd:`Ctrl` + :kbd:`End`

を使う。キャレットがある升目が空の場合、表組の最初や最後に移動する。升目に内容が
ある場合、押すとまず升目の先頭や末尾に移動し、次に押すと表組の最初や最後に移動す
る。もう一度押すと文書の最初や先頭に移動する。

Sorting data in a table
----------------------------------------------------------------------

スプレッドシートと同様に、表組のデータも並び替えられる。並べ替えは三段階まで指定
できる（例えば、まず年齢を数値で並べ替え、次に各年齢内の名前を辞書式に並べ替え
る）。

表組のデータを並べ替えるには

#. 並び替える表組（またはその一部）を選択する。
#. メニューの :menuselection:`T&able-->So&rt...` を選択するか、|TableToolbar| の
   :guilabel:`Sort` 図像をクリックする。
#. :guilabel:`Sort` ダイアログボックスが表示される。

   * 行と列のどちらの方向に並び替えるかを決める。既定の並び替え方向は行で、その
     結果、列のデータが並び替わる。
   * 正しい順序で、並び替えるキーを三つまで選択する。
   * 各キーについて、並び替える列または行、並び替えが数値か英数字か、昇順か降順
     かを選択する。
   * 並び替えを実行するには |OK| を押す。

.. note::

   並べ替えの影響を受ける可能性のある升目をすべて選択しろ。例えば、ある列の升目
   だけを選択すると、並べ替えはその列だけに影響し、他の列は変更されない。このよ
   うな場合、行のデータが混ざってしまう危険性がある。

.. _writer13-anchor-spreadsheet:

Using spreadsheet functions in a table
----------------------------------------------------------------------

簡単な数学関数の多くでは、Writer 表組は基本的なスプレッドシートとして使用でき
る。スプレッドシートと同じように、表の各升目は文字（列）と数字（行）で識別され
る。例えば、升目 C4 は左から三列目、上から四行目の升目だ。キャレットが升目にある
と、表組名とこの升目参照が Status バーに表示される。

.. tip::

  表組での基本スプレッドシート関数は LibreOffice Calc とほとんど同じだ。主な違い
  は升目参照の書式が異なることだ。升目 A2 は Calc ではそのまま A2 と参照される
  が、Writer 表組では <A2> と表記される。

例えば、升目 <B1> と <C2> に数字がそれぞれあり、升目 <A1> に二つの合計を表示した
いとする。合計するには次のようにする：

.. |Formula| replace:: :guilabel:`Insert or Edit Formula`
.. |FormulaBar| replace:: Formula バー
.. |Apply| replace:: :guilabel:`Apply` 印

#. 升目 <A1> をクリックして

   * :kbd:`=` を押す
   * メニューの :menuselection:`T&able-->Edit &Formula` を選択
   * :kbd:`F2` を押す
   * |TableToolbar| の :guilabel:`Sum` 図像または |Formula| 図像をクリック
   * Sidebar |PropertiesDeck| |TablePanel| にある |Formula| 図像をクリック

   作業場の上部に Formula バーが自動的に表示される。バーの左端には選択した升目の
   座標が表示される。
#. 升目 <B1> をクリックする。この升目の識別子が自動的にFormula バーに表示され、升目
   <A1> にはめ込まれる。
#. :kbd:`+` キーを押す
#. 升目 <C2> をクリックする。最終的な数式 ``=<B1>+<C2>`` が選択した升目と
   Formula バー入力欄の両方に表示される。
#. :kbd:`Enter` を押すか、|FormulaBar| |Apply| をクリックすると升目内の数式が計
   算結果に置き換わる。

.. tip::

   上記の手順は升目の数式を表示して編集できるようにする方法でもある。

   表組で使用できる数学関数の一覧を表示するには :guilabel:`Functions` 図像をク
   リックする。

連続する升目を合計するには、行、列、または行と列の矩形の升目を選択すればよい。し
たがって、例えば数字の列の和を得るには次のようにする：

#. 空の升目に等号 ``=`` を入力する。
#. 足し合わせる升目、この場合は A2 から A5 までの升目を選択する。数式は
   ``=<A2:A5>`` のようにする。
#. :kbd:`Enter` を押すか、|FormulaBar| |Apply| をクリックする。

関数を使うときは、升目参照を手入力するか、選択する。したがって、上で追加した四つ
の数字 (A2, A3, A4, A5) を合計するには次のようにする：

#. 空の升目に等号 ``=`` を入力する。
#. ``sum`` と入力するか、:guilabel:`Functions` 一覧から :menuselection:`&Sum` を
   選択する。
#. 連続した升目を選択する。数式は ``=sum<A2:A5>`` のようにする。
#. :kbd:`Enter` を押すか、|FormulaBar| |Apply| をクリックする。

.. caution::

   Writer では、表組の行や列を加除しても数式は自動的に更新されないが、升目の値を
   変更すると結果が更新される。複雑な数式を使用する場合は、Calc スプレッドシート
   を Writer 文書に埋め込むことを検討しろ。|Chapter19| を見ろ。

Additional table operations
======================================================================

Protecting cells in a table
----------------------------------------------------------------------

表組の個々の升目の内容を変更から保護することができる。升目が保護されると、メ
ニュー項目のほとんどとツールバー図像のほとんどが無効になる。

.. note::

   この保護は安全な保護を意図したものではない。偶発的な変更から升目を保護するも
   のだ。

升目の保護をオンにするには、升目にキャレットを置くか升目を選択してから、

* |TableToolbar| の :guilabel:`Protect Cells` 図像をクリックするか、
* メニューの :menuselection:`T&able-->Pr&otect Cells` を選択する。

オフにするには、

* |TableToolbar| の :guilabel:`Unprotect Cells` 図像をクリック
* メニューの :menuselection:`T&able-->&Unprotect Cells` を選択

現在の表組全体、または選択したすべての表組の保護を解除するには :kbd:`Shift` +
:kbd:`Ctrl` + :guilabel:`T` を押す。

.. tip::

   保護された升目にキャレットを置くことができない場合は、キャレットを有効にする
   必要がある。|Options| :menuselection:`LibreOffice Writer-->Formatting Aids`
   ページ :guilabel:`Protected Area` で :guilabel:`Enable cursor` をオンにする。

Adding a caption
----------------------------------------------------------------------

.. |InsertCaptionDlg| replace:: :guilabel:`Insert Caption` ダイアログボックス

どの表組にも簡単に説明を追加できる。Writer は説明が付けられた表組すべてを記録し、
番号を自動的に付け、表組へのリンクを更新する。表組に説明を追加するには：

#. 表組内の任意の場所で次のいずれかを行う：

   * 右クリックメニューから :menuselection:`Insert Caption...` を選択
   * メニューから :menuselection:`&Insert-->Caption` を選択
   * |TableToolbar| :guilabel:`Insert Caption` 図像をクリック
#. |InsertCaptionDlg| の :guilabel:`Properties` で :guilabel:`Categor&y`,
   :guilabel:`N&umbering`, 区切りパターンを選択する。説明の位置の規定は表組の上
   部だが、必要なら変更可能だ。
#. ダイアログボックス上部の :guilabel:`C&aption` 欄に説明テキストを入力
#. |OK| を押す

表組に説明を自動的に追加させるように Writer を構成することもできる。手順は
|Chapter11| で説明した、画像に説明を自動的に追加する方法と同じだ。

Cross-referencing to a table
----------------------------------------------------------------------

説明付きの表組に相互参照を挿入することができる。相互参照をクリックすると読者はそ
の表組に直接ジャンプする。詳細は |Chapter17| を見ろ。

Splitting a table
----------------------------------------------------------------------

一つの表組を二つの表組に分割したり、二つの表組を一つの表組に合体したりすることが
できる。表組は水平方向に分割される。分割点より上の行は一つの表組に入れられ、下の
行は別の表組に入れられる。表組を分割するには：

#. キャレットを分割後の二番目の表組の最上行にある升目に置く。キャレットのすぐ上
   で表が分割される。
#. 次のいずれかを行う：

   * メニュー :menuselection:`T&able-->Split T&able...` を選択
   * |TableToolbar| :guilabel:`Split Table` 図像をクリック
#. :guilabel:`Split Table` ダイアログボックスが開き、見出し行の処理方法を選択で
   きる。
#. |OK| をクリックする。表組が空白の段落で区切られた二つの表組に分割される。

.. note::

   一方の表組の升目に、もう一方の表組のデータを使用した数式が含まれている場合、
   それらの升目にはエラーメッセージが表示される。

Merging tables
----------------------------------------------------------------------

二つの表組を合体する手順：

#. 表組と表組の間の空白の段落を削除する。これを行うには、:kbd:`Backspace` ではな
   く :kbd:`Delete` を使用する必要がある。
#. 表組のいずれかの升目を選択する。
#. メニューから :menuselection:`T&able-->Mer&ge Table` を選択する。

.. tip::

   段落の位置を明白にし、簡単に削除するには、

   * :menuselection:`&View-->For&matting Marks` を選択
   * キーバインド :kbd:`Ctrl` + :guilabel:`F10`
   * |StandardToolbar| :guilabel:`¶` 図像をクリック

Deleting a table
----------------------------------------------------------------------

表組を削除するには次のいずれかの操作を行う：

* 表組の任意の場所を右クリックし、:menuselection:`&Delete-->&Table` を選択
* 表組の任意の場所をクリックし、メニューから
  :menuselection:`T&able-->&Delete-->&Table` を選択
* 表組の前の段落の終わりから、表組の後の段落の始まりまでを選択し、
  :kbd:`Delete` または :kbd:`Backspace` を押す

.. note::

   三番目の方法は表組の後の段落を表組の前の段落に融合する。

Copying a table
----------------------------------------------------------------------

文書のある部分から表組をコピーし、別の部分に貼り付けるには：

#. 表組を選択する
#. |Ctrl+C| を押すか、|StandardToolbar| :guilabel:`Copy` 図像をクリック
#. 表組をコピーしたい場所をクリック
#. |Ctrl+V| を押すか、|StandardToolbar| :guilabel:`Paste` 図像をクリック

Moving a table
----------------------------------------------------------------------

文書のある部分から別の部分に表組を移動するには：

#. 表組を選択
#. |Ctrl+X| を押すか、|StandardToolbar| :guilabel:`Cut` 図像をクリック
#. 表組を移動したい場所をクリック
#. |Ctrl+V| を押すか、|StandardToolbar| :guilabel:`Paste` 図像をクリック

升目の内容と書式が貼り付けられる。

Inserting a paragraph before or after a table
----------------------------------------------------------------------

表組の前に段落を挿入する手順：

#. 最初の（左上の）升目のテキストやその他の内容の前にキャレットを置く
#. :kbd:`Alt` + :kbd:`Enter`

表組の後に段落を挿入する手順：

#. 最後の（右下の）升目のテキストの後にキャレットを置く
#. :kbd:`Alt` + :kbd:`Enter`

Using tables as a page layout tool
======================================================================

表組はタブや空白文字を使用する代わりに、文書内のテキストを配置するページレイアウ
トツールとして使用することができる。ページレイアウトでの表組の使用に関する詳
細とコツについては |Chapter06| を見ろ。
