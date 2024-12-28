======================================================================
Writer Guide Chapter 3, Working with Text: Advanced ノート
======================================================================

.. include:: ./writer-inc.txt

.. contents:: 本章見出し
   :depth: 3
   :local:

Introduction
======================================================================

この章の内容：

* 組み込み言語ツール
* ワイルドカードを含む、高度な検索と置換の手法
* 変更の追跡とコメントの挿入
* 脚注と巻末注
* 文書内リンク
* アウトラインの折りたたみ
* 他の文書から資料を挿入する
* 行番号

この章の読者が |Writer02| に馴染んでいることを仮定される。

|OptionsDlg| |FormattingAidsPage| で段落末尾印、タブ、改行などの書式設定補助項目
を表示する設定にすることも推奨。

テキストの書式設定については |Writer04| を見ろ。

Using built-in language tools
======================================================================

Writer には同一文書内に言語が複数混在している場合の作業を容易にするツールがいく
用意されている：

* :menuselection:`&Tools-->Lan&guage-->` サブメニューにある機能
* |OptionsDlg| :menuselection:`Language Settings-->`
* パラグラフと文字スタイル
* |StatusBar| で使える機能

選択テキストの言語を変更する主な利点は、

* 正しい辞書を使用して綴字を検証
* ローカライズ版の次のものを適用できる：

  * AutoCorrect 置換表
  * 類語辞書
  * 分綴規則

文法チェック辞書も、選択した言語で利用できる場合がある。

段落や文字群の言語を :guilabel:`&None (Do not check spelling)` に設定することも
可能。このオプションは、Web アドレスやプログラミング言語のコード片など、綴字検査
をしたくないテキストを挿入する場合に有用だ。

Using :menuselection:`&Tools-->Lan&guage`
----------------------------------------------------------------------

|MenuBar| :menuselection:`&Tools-->Lan&guage-->` 以下で、文書全体、段落ごと、
あるいは単語や文字ごとに言語を設定可能：

* :menuselection:`&For Selection-->` は選択テキストに指定言語を適用する。適用し
  たい言語がサブメニューに表示されていない場合は :menuselection:`&More...` を選
  択して |CharacterDlg| を開く。
* :menuselection:`For &Paragraph-->` はキャレットのある段落に指定言語を適用す
  る。
* :menuselection:`For &All Text-->` は指定言語を変更後に挿入されたテキストを含
  む文書全体に適用する。

サブメニューの :menuselection:`&Reset to Default Language` オプションは、選択範
囲、段落、全テキストのいずれかを |OptionsDlg| で設定した既定言語に戻す方法のうち
で最も速い。

Using language settings in Options
----------------------------------------------------------------------

文書全体の言語を変更するには |OptionsDlg| |LanguagesPage| を用いる方法もある。
:guilabel:`Default Languages for Documents` 区画では異なる言語として明示的には
マークされていないテキストすべての言語を選択可能だ。

.. caution::

   |OptionsDlg| からの既定言語の変更は LibreOffice の一般設定の変更であるため、
   今後作成される文書すべてに適用される。現在の文書の言語のみを変更する場合は
   :guilabel:`For the current document only` を必ずオンにしろ。

.. note::

   綴字検査はオンになっている言語に対してしか機能しない。所望の言語の横にこの記
   号が表示されていない場合は、|MenuBar| から :menuselection:`&Tools-->Lan&guage
   -->&More Dictionaries Online...` を使って辞書をインストールすることが可能。

Using paragraph and character styles
----------------------------------------------------------------------

|ParagraphStyleDlg| |FontTab| で言語を変更すると、その段落スタイルを使用する段落
すべての言語が変更される。

単一文書に異なる言語の段落全体を含めるには、言語ごとに異なる段落スタイルを使用し
ろ。例えば、英語とフランス語の段落を含む文書で、`BodyText-EN` と `BodyText-FR`
を定義することなど考えられる。

スタイルの言語設定を管理する方法の詳細については |Writer09| で習う。

Using the Status bar
----------------------------------------------------------------------

段落を文書の他の部分の言語と異なる言語で検査するように設定するには、段落にキャ
レットを置き、|StatusBar| の言語を変更する。この変更は、選択した段落のみに影響す
る。

綴字検査に使用される言語も |StatusBar| の使用中ページスタイルの横に表示され
る。|StatusBar| の言語をクリックするとポップアップメニューが現れる。

.. admonition:: 読者ノート

   たぶん :guilabel:`[None]` と示されている部分を指している。

先述のように、このサブメニューにある :menuselection:`&Reset to Default Language`
が段落や文書全体を既定言語に戻す最速の方法だ。

Advanced find and replace techniques
======================================================================

単語や語句の検索と置換 (|Writer02|) に加えて、|Find&ReplaceDlg| を使って、段落ス
タイルやテキスト書式の検索と置換を行うことが可能だ。

Find and replace paragraph styles
----------------------------------------------------------------------

複数素材を組み合わせると、文書内の段落スタイルが不要になることがある。段落のすべ
てをあるスタイルから別のスタイルにすばやく変更する手順は：

#. |Find&ReplaceDlg| :guilabel:`Other &options` で :guilabel:`Paragraph St&yles`
   を選択する。文書で使用されている段落スタイルの一覧が表示される。

   * テキストの書式や属性を指定している場合、このオプションは
     :guilabel:`Including Styles` と表示される。
   * :guilabel:`&No Format` を選択すると属性が削除され、オプションが
     :guilabel:`Paragraph St&yles` に戻る。

#. 検索、置換したいスタイルを選択する。
#. :guilabel:`Find`, :guilabel:`Find &All`, :guilabel:`&Replace`,
   :guilabel:`Replace A&ll` を適宜押す。

置換したい各スタイルについて、手順 2 と 3 を繰り返す。

Find and replace text formatting
----------------------------------------------------------------------

上述の段落スタイルの :menuselection:`Find and Rep&lace...` とは異なり、検索され
る書式や属性は :guilabel:`&Find` または :guilabel:`Re&place` 欄の中ではなく下に
表示される。ドロップダウンリスト右側の下矢印をクリックしても選択肢は表示されな
い。

文書内の書式の種類を見つける手順：

#. :guilabel:`Other &options` を展開する。
#. 以前の書式基準をすべて消去するには :guilabel:`&Find` 欄をフォーカスして
   :guilabel:`&No Format` ボタンをクリックする。選択した置換オプションを消去する
   方法も :guilabel:`Re&place` 欄を同様に用いる。
#. :guilabel:`For&mat...` ボタンを押すと :guilabel:`Character` ダイアログボック
   スとよく似た :guilabel:`Formatting` ダイアログボックスが開く。いずれかのタブ
   から書式を選択する。
#. 直接書式設定によってのみ適用されたこの書式を見つけるには :guilabel:`Including
   Styles` をオフのままにする。文字または段落スタイルの内部にも適用されている書
   式を見つけるにはオンにする。
#. :guilabel:`Find &All` を選択すると、見つかったすべての書式が強調表示される。
#. 選択した書式を置き換えるには、:guilabel:`Re&place` 欄をクリックし、
   :guilabel:`For&mat...` を選択して、置換先書式を指定する。
#. :guilabel:`Find Pre&vious` → :guilabel:`&Replace` または :guilabel:`Find
   Ne&xt` → :guilabel:`&Replace` を使用して、書式を順次置き換る。すべての書式を
   一度に変更するには :guilabel:`Replace &All` を押す。
#. 次にこのダイアログボックスを使用するときに失敗するのを避けるために、選択した
   すべての書式基準を消去する。

文書内の特定の語句の書式を変更する手順：

#. :guilabel:`&Find` 欄に単語または語句を入力する。
#. :guilabel:`Re&place` 欄に新しいテキストを入力し、変更する書式を選択する。

   同じ単語や語句をそのままにして書式だけを変更したい場合でも単語や語句を入力し
   ろ。
#. 先ほどの手順のように :guilabel:`Find` ボタンと :guilabel:`&Replace` ボタンを
   一つずつ押していったり、一度だけ :guilabel:`Replace &All` を押したりする。

Similarity search
----------------------------------------------------------------------

この選択肢は :guilabel:`&Find` テキストと類似する用語を検索する。たとえば、類似
検索では二文字だけ異なる単語を見つけることが可能だ。

:guilabel:`S&imilarity search` をオンにし、:guilabel:`Similarities...` ボタンを
押すと、検索語の長さと異なる文字数でテキスト検索を変更できるダイアログボックスが
開く。

:guilabel:`&Exchange characters`
   交換可能な検索語の文字数。例えば、交換可能な文字を二文字指定した場合、"black"
   と "crack" は類似しているとみなされる。
:guilabel:`&Add characters`
   単語が検索語の文字数を超えることが可能である最大文字数。
:guilabel:`&Remove characters`
   単語が検索語より短くなることが可能である文字数。
:guilabel:`&Combine`
   類似検索設定の任意の組み合わせに一致する用語を検索するならオン。

Search with wildcards and regular expressions
----------------------------------------------------------------------

   A :dfn:`wildcard` is a special character that represents one or more
   unspecified characters.

ワイルドカードにせよ正規表現にせよ、それらを用いて複数の検索を一つにまとめること
で、時間と労力を節約することが可能だ。

検索および置換時にワイルドカードと正規表現を使用するには、次の手順に従う：

#. |Find&ReplaceDlg| で :guilabel:`Other &options` を展開する。
#. :guilabel:`Re&gular expressions` をオンにする。
#. 検索テキスト（ワイルドカードを含む）を :guilabel:`&Find` 欄に入力し、置換テキ
   ストがあればそれを :guilabel:`Re&place` 欄に入力する。
#. :guilabel:`Find`, :guilabel:`Find &All`, :guilabel:`&Replace`,
   :guilabel:`Replace All` のいずれかを押す。

.. note::

   ワイルドカードとして定義された文字を検索するには、その文字の前にバックスラッ
   シュを入力する。例えば `$5.00` というテキストを見つけるには
   :regexp:`\\$5\\.00` を検索する。

Tracking changes to a document
======================================================================

文書に加えられた変更を記録するには、次のような方法がある：

* 文書のコピーに変更を加えた後、Writer を使って二つのファイルを比較し、変更点を
  表示する。この方法は、他の方法によるファイルサイズや複雑さの増加を回避できるた
  め、文書で作業しているのが自分一人の場合に特に便利だ。
* 元のファイルの一部として保存されたバージョンを保存する。この方法は、特に多くの
  バージョンを保存する場合、大きな文書や複雑な文書で問題を引き起こす可能性があ
  る。
* Writer の変更印（「赤線」だとか「改訂印」と呼ばれる）を使用して、追加、削除、
  移動された資料や変更された書式を示す。後になって各変更を確認し、受理または却下
  することが可能だ。

次の変更追跡機能の使い方が述べられている：

* テキスト、画像、図表、その他の挿入と削除を追跡する
* 段落スタイルと文字スタイルの属性の変更を追跡する
* 空行を含む図表の行の挿入と削除を追跡する
* 追加または削除された資料とは異なる色で移動した資料を表示する
* Navigator を使用して移動した資料を追跡する
* 脚注の削除と挿入を追跡する
* 目録項目での項目番号の変更を表示する

.. note::

   すべての変更が記録されるわけではない。例えば、タブストップを左揃えから右揃え
   に変更したくらいでは記録されない。

Preparing a document for review
----------------------------------------------------------------------

文書を他の人に送付して査読や編集を依頼する場合、編集者や査読者が改印をオンにする
必要がないように、最初に文書を準備しておく。文書を保護した後、それ以降の使用者が
保護をオフにしたり、変更を受理したり却下したりするには、正しいパスワードを入力す
る必要がある。

.. |TrackChangesToolbar| replace:: :guilabel:`Track Changes` ツールバー

#. 文書を開く。:menuselection:`&File-->Versions...` を選択して、その文書に複数の
   版が含まれているかどうかを確認する。複数の版が表示されている場合は、現在版を
   別の名前で別の文書として保存し、この新しい文書を査読コピーとして使用する。
#. 査読コピーを開いた状態で、変更の記録がオンになっていることを確認する。記録が
   オンになっていると、次が強調表示される：

   * |MenuBar| |EditTrackRecordM| 項目
   * |TrackChangesToolbar| の :guilabel:`Record Track Changes` 図像
#. 次のいずれかを行う：

   * |TrackChangesToolbar| の :guilabel:`Protect Track Changes` をクリック
   * :menuselection:`&Edit-->Track Chan&ges-->&Protect...` を選択
#. :guilabel:`Enter Password` ダイアログボックスが開く。パスワードを二度入力。
#. |OK| を押す。

.. tip::

   上記の手順 2 と 3 の代わりに、|FilePropertiesM| から |SecurityTab| を選択し、
   :guilabel:`Record &changes` をオンにしてから :guilabel:`&Protect...` を押して
   パスワードを入力する方法もある。

Track Changes menu and toolbar
----------------------------------------------------------------------

:menuselection:`Track Chan&ges-->` メニューに加えて、同じ機能のボタンを含む便利
なツールバーが用意されている。|TrackChangesToolbar| を有効にするには
:menuselection:`&View-->&Toolbars-->Track Chan&ges` をクリックする。このツール
バーは使いやすい場所に繋留することも、浮遊させておくことも可能だ。

Recording changes
----------------------------------------------------------------------

変更の記録（追跡）を開始するには、次のいずれかを行う：

* |TrackChangesToolbar| の :guilabel:`Record Track Changes` をクリック
* |MenuBar| の |EditTrackRecordM| を選択

変更の表示を表示または非表示にするには、

* |TrackChangesToolbar| の :guilabel:`Show track changes` をクリック
* |MenuBar| の |EditTrackShowM| を選択

追跡された変更にコメントを入力するには、変更箇所にキャレットを置き、次のいずれか
を行う：

* |EditTrackCommentM| を選択
* |TrackChangesToolbar| の :guilabel:`Insert Track Change Comment` ボタンをク
  リック

変更記録を停止するには |EditTrackRecordM| を再度選択する。

Recording inserted, deleted, and moved material
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

初期設定では挿入されたテキストには下線が引かれ、削除されたテキストには取り消し線
が引かれ、どちらにも色が入り、余白に変更印が表示される。

既存の図表では、削除された行はピンク色で、挿入された行はシアン色で表示される。新
しい空白の表は余白にマークされるが、行に色は付かない。

移動した箇所は緑色で表示され、二重下線（新しい場所）または二重の取り消し線（古い
場所）で示される。

Recording changes of paragraph styles and other formatting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

異なる段落スタイルが段落に適用されると、その変更は余白にマークで示される。

初期設定では文字スタイルの変更または手動で適用された文字属性は、属性（斜体や下線
など）に加えて太字、色付きテキストで示され、変更は余白にマークで示される。

目録番号の変更では、目録項目すべての元の番号と新しい番号が表示される。

Outline tracking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

アウトライン追跡では、Navigator を使用して、見出しとそれの同階層の次の見出しの間
にあるあらゆる物という、文書の部分全体の順序の変更を追跡する。変更追跡を有効にし
た状態で Navigator の :guilabel:`Move Heading Up` および :guilabel:`Move Heading
Down` ボタンを使用すると、ドラッグ＆ドロップやカット＆ペーストで移動した物と同じ
ように、移動した物がマークされ追跡される。

アウトライン追跡は初期状態で有効になっている。無効にするには、

#. Navigator 上で :guilabel:`Headings` を右クリックし、
#. コンテキストメニューから :menuselection:`Outline &Tracking-->&Off` を選択す
   る。

Viewing changes and comments
----------------------------------------------------------------------

追跡された変更にマウスポインターを合わせると、変更の種類、作成者、日付、時刻を示
すヘルプヒントが表示される。拡張ヒントを有効にすると、この変更に対して記録された
コメントも表示される。

記録されたコメントは、拡張ヒントとして表示されるだけでなく、|ManageChangesDlg|
の目録にも表示される。変更にコメントが記録されていない場合、コメントフィールドは
空白になる。

追跡された変更から次の変更に移動するには、|TrackChangesToolbar| の
:guilabel:`Previous Change` と :guilabel:`Next Change` 図像を使用する。

初期設定では追跡された変更はインライン表示される。削除または挿入を余白に表示する
には、|TrackChangesToolbar| の :guilabel:`Show track changes` ドロップダウンメ
ニューから選択する。

Accepting or rejecting changes
----------------------------------------------------------------------

記録された変更を受理したり却下したりするには、次のいずれかを使用する：

* |TrackChangesToolbar|
* :menuselection:`Track Chan&ges-->` メニュー
* 右クリックメニュー
* |ManageChangesDlg|
* Sidebar 内 :guilabel:`Manage Changes` 甲板

.. rubric:: Track Changes menu and toolbar

:menuselection:`&Edit-->Track Chan&ges-->` サブメニューに表示されているのと同
じ機能のボタンがある。

.. rubric:: Right-click (context) menu

#. 追跡された変更が表示されていない場合は、|TrackChangesToolbar| の
   :guilabel:`Show track changes` 図像をクリックするか、|MenuBar| で
   |EditTrackShowM| を選択する。
#. 記録された変更の上にマウスポインターを置く。箱が表示され、変更の種類、変更
   者、日時に関する情報が表示される。
#. コンテキストメニューから :menuselection:`Accept Change` または
   :menuselection:`Reject Change` を選択する。

.. rubric:: Manage Changes dialog and Sidebar deck

#. |TrackChangesToolbar| の :guilabel:`Manage Track Changes` 図像をクリックする
   か、|MenuBar| から :menuselection:`&Edit-->Track Chan&ges--> &Manage...` を選
   択する。
#. |ManageChangesDlg| が開き、受理も却下もされていない変更が表示される。Sidebar
   の :guilabel:`Manage Changes` 図像をクリックすることでも同じ情報が表示される。
#. ダイアログボックスで変更を選択すると、その変更自体が文書内で強調表示されるの
   で、何が変更されたかを目視で確認可能だ。
#. :guilabel:`Accept` または :guilabel:`Reject` をクリックして、選択した変更を受
   理または却下する。変更を個別に確認したくない場合は :guilabel:`Accept All` ま
   たは :guilabel:`Reject All` を押すことも可能だ。

特定の人の変更だけを表示したい場合などでは |ManageChangesDlg| :guilabel:`Filter`
タブを用いる。絞り込み条件を指定した後 :guilabel:`List` タブに戻り、条件を満たす
変更を表示する。

Comparing documents
----------------------------------------------------------------------

査読者が自分の行った変更を追跡し忘れることがある。元の文書と編集後の文書を比較す
れば、変更箇所を見つけることが可能だ。比較するには：

#. 編集済みの文書を開く。
#. |EditTrackCompareM| を選択するか、|TrackChangesToolbar| の :guilabel:`Compare
   Non-Track Changed Document` 図像をクリック。
#. :guilabel:`Compare to Original Document` ダイアログボックスで元の文書を選択
   し、|Open| を押す。

Writer は変更を見つけて印を付け、|ManageChangesDlg| を表示する。このダイアログ
ボックスから、前述のように変更内容を確認し、変更を許可または却下することが可能
だ。

この機能で使用する詳細さの度合いを設定するには、|OptionsDlg|
:menuselection:`LibreOffice Writer-->Compare` ページで設定を構成する。
|Writer20| で詳細が述べられる。

Merging modified documents
----------------------------------------------------------------------

ここまで説明した工程は一度に一人の査読者が担当する場合に効果的だが、複数の査読者
全員が文書の編集済みコピーを返信することもある。Writer には、追跡された変更を含
む文書を元の文書に併合する機能があるが、この機能を実現するための条件はかなり限定
的だ：編集された文書が異なるのは記録された変更点のみであり、その他の原文はすべて
同一でなければならない。

文書を併合するには（原文書ではなく）編集された文書すべてに変更が記録されている必
要がある。

#. 原文書を開く。
#. |EditTrackMergeM| を選択するか、|TrackChangesToolbar| の :guilabel:`Merge
   Track Changed Document` 図像をクリックする。
#. ファイル選択ダイアログボックスが開く。原文書に

   * その後の変更がない場合、そのコピーは併合される。
   * 何らかの変更が加えられている場合、併合が失敗したことを知らせるエラーダイア
     ログボックスが開く。
#. 文書が併合されると、原文書にコピーから記録された変更が表示される。
#. すべてのコピーが併合されるまで繰り返す。

これで記録された変更のすべてが開いているコピーに含まれる。このファイルを別の名前
で保存しろ。

Adding other comments
======================================================================

これまで見てきたコメント機能とは別に、著者と査読者が意見を交換したり、提案を求め
たり、注意が必要な項目に印を付けたりするために使用できるコメント機能がある。

段落を複数含むテキストブロックを選択してコメント用に強調することも、一箇所にコメ
ントを挿入することも可能だ。コメントを挿入するには、

#. テキストを選択するか、コメントを参照する場所にキャレットを置く。
#. 次のいずれかを行う：

   * 右クリックして :menuselection:`Inser&t Comment` を選択
   * キーバインド |Ctrl+Alt| + :kbd:`C`
   * |TrackChangesToolbar| の :guilabel:`Insert Comment` 図像をク
     リック

コメントの錨点はページの右側にあるコメントテキスト入力欄と点線で結ばれている。ま
た、水平定規の右側に :guilabel:`Comments` ボタンが追加され、これをクリックするこ
とでコメントの表示有無を切り替えることが可能だ。

コメントを作成すると、その作成者名と作成タイムスタンプが自動的に追加される。この
名前には |OptionsDlg| |UserDataPage| の内容が使われる。

コメントを入力し終えたら、文書のページ上の他の場所をクリックしろ。そうしないと、
コメント欄から移動できなくなる。

複数の人が文書を編集した場合、各執筆者には異なる背景色が自動的に割り当てられる。
ある著者が別の著者のコメントと重なるテキストを選択した場合、二番目のコメントは最
初のコメントと入れ子になる。

コメントを右クリックするか、左下の矢印をクリックすると、コンテキストメニューが表
示され、

* 現在のコメント、
* 現在のコメントスレッド全体、
* 同じ作者のコメントすべて、
* 文書内のコメントすべて

を削除可能だ。このメニューから :menuselection:`Format All Comments...` を選択す
ると、コメントのテキストに基本的な書式を適用するダイアログを開くことも可能だ。
フォントの種類、サイズ、配置を |MenuBar| で変更することも可能だ。

文書が査読、コメントされ、原著者の行動が必要な場合、コメントのコンテキストメ
ニューの選択肢を使用して各コメントに Resolved または Unresolved の目印を付けるこ
とが可能だ。Resolved のコメントをマークすると、コメント欄の日付の下に
:guilabel:`Resolved` という文字が挿入される。|MenuBar| の :menuselection:`&View
-->Resolved Comments` を使用して、文書内のすべての解決済みコメントの表示を切り
替えることが可能だ。コメントに回答を追加することも可能だ。

あるコメントから別のコメントに移動するには、Navigator を開き、
:guilabel:`Comments` ノードを展開する。コメントテキストをダブルクリックすれば
キャレットが文書内のコメントの錨点に移動する。

また、Navigator 上部の :guilabel:`Navigate By` ボックスで :guilabel:`Comments`
を選択し、その横にある上下の矢印をクリックして、次のコメントや前のコメントに移動
することも可能だ。キーボードを使用して移動することも可能だ：

* |Ctrl+Alt| + |PgDn|
* |Ctrl+Alt| + |PgUp|

文書内のコメントを印刷するには、|PrintDlg| の :guilabel:`Co&mments` ドロップダウ
ンリストでいずれかのオプションを選択する。

Using footnotes and endnotes
======================================================================

脚注は参照されているページの床下に表示される。注は文書の最後に集められる。

脚注と巻末注を効果的に扱うには以下を行う必要がある：

* 初期設定値が合わない場合は、脚注を挿入して書式を定義する。
* ページ上の脚注の位置と、区切り線の色と線スタイルを定義する。|Writer05| で述べ
  られる。

Inserting footnotes and endnotes
----------------------------------------------------------------------

脚注または巻末注を挿入するには：

#. 脚注または巻末注印を表示したい位置にキャレットを置く。
#. |MenuBar| で :menuselection:`&Insert-->Footnote and Endno&te-->` から関連項目
   を選択するか、|StandardToolbar| の :guilabel:`Insert Footnote` または
   :guilabel:`Insert Endnote` 図像をクリックする。
#. 脚注または巻末注マーカーがテキストに挿入され、選択に応じて、キャレットがペー
   ジ床板の脚注領域または文書末尾の巻末注領域に移動する。この領域に脚注または巻
   末注の内容を入力する。

脚注、巻末釈の設定を変更するには、|MenuBar| の :menuselection:`&Tools-->
&Footnotes and Endnotes...` を選択する。

脚注設定で指定された自動番号付け順序を使用するか、カスタム番号を指定するかを選択
するには、

#. :menuselection:`&Insert-->Footnote and Endno&te-->&Footnote or Endnote...`
#. :guilabel:`Insert Footnote/Endnote` ダイアログボックスで指定する。

既存の脚注や注は、他のテキストを編集するのと同じ方法で編集することが可能だ。

脚注や注を削除するには脚注マーカーを削除する。脚注や注の内容は自動的に削除さ
れ、他の脚注や注の番号も自動的に調整される。

Formatting footnotes and endnotes
----------------------------------------------------------------------

脚注自身の書式を設定するには、|MenuBar| の :menuselection:`&Tools-->&Footnotes
and Endnotes...` を選択する。:guilabel:`Settings of Footnotes and Endnotes` ダイ
アログボックスで構成する。

Linking to another part of a document
======================================================================

トピックの順序を入れ替えたり、資料を追加または削除したり、見出しを書き換えたりす
ると、文書内の他の部分への入力済み相互参照は簡単に古くなる。

Writer には参照を最新の状態に保つための方法が二つ備わっている：

* ハイパーリンク
* 自動相互参照

どちらの方法も、同じ文書の他の部分や別の文書にリンク可能だ。

どちらの方法も結果は同じだ。文書を開いているときにリンクを |Ctrl| を押しつつク
リックすると、被参照項目に直接飛ぶ。しかし、両者には大きな違いもある：

* ハイパーリンクのテキストは、リンクされた項目のテキストを変更しても自動的には更
  新されないが、変更されたテキストは相互参照で自動的に更新される。
* ハイパーリンクを使用する場合、リンクの内容（テキストやページ番号など）を選ぶ余
  地がないが、相互参照を使用する場合、選択肢がある。
* 画像などのオブジェクトにハイパーリンクし、そのハイパーリンクに有用なテキストを
  表示させるには、そのようなオブジェクトに有用な名前を明示的に与えるか、
  |HyperlinkDlg| を使って表示テキストを変更する。対照的に、キャプション付きの図
  への相互参照は、有用なテキストを自動的に表示するように設定でき、名前の変種もい
  くつか選択可能だ。
* Writer 文書を |HTML| ファイルに保存すると、ハイパーリンクは生きたままだが、相
  互参照はそうではない。

  * |PDF| ファイルにエクスポートすると、両方とも生きたままになる。

Using cross-references
----------------------------------------------------------------------

見出し、キャプション、その他のリンクされた項目が書き換えられた場合に相互参照のテ
キストが更新されるようにするには自動相互参照を使用する。詳しくは |Writer17| でや
る。

Using bookmarks
----------------------------------------------------------------------

ブックマークは Navigator に一覧表示され、マウスをシングルクリックするだけでそこ
から直接アクセス可能だ。|HTML| 文書ではブックマークはハイパーリンクで飛ぶことが
可能である錨に変換される。ブックマークへの相互参照も可能だ。これも詳しくは
|Writer17| でやる。

Using hyperlinks
----------------------------------------------------------------------

Web サイトのアドレスや URL など、ハイパーリンクとして使用できるテキストを入力し、
|Space| または |Enter| を押すと、Writer は自動的にハイパーリンクを作成し、テキス
トに書式を適用する。

この機能が有効にならない場合は :menuselection:`&Tools-->AutoCorr&ect-->
&AutoCorrect Options...` を使用してこの機能を有効に可能だ。|OptionsTab| で
:guilabel:`URL Recognition` をオンにする。

LibreOffice で特定の URL をハイパーリンクに変換したくない場合は、書式設定が適用
された直後にハイパーリンクにキャレットを置いて右クリックし、|RemoveHyperlinkC|
を選択する。

また、Navigator や |HyperlinkDlg| を使って、

* 文書の他の部分、他の文書や文書の一部、電子メールアドレスへのハイパーリンクを挿
  入したり、
* ハイパーリンクすべてを修正することも可能だ。

*Getting Started Guide* に詳細がある。

LibreOffice 内でハイパーリンクを活性にする標準の動作は |Ctrl| 押しクリック
だ。この動作を変更するには、

#. |OptionsDlg| を開く
#. |SecurityPage| を開く
#. :guilabel:`O&ptions...` ボタンを押して |SecurityOptions&WarningsDlg| を開く。
#. :guilabel:`Ctrl-click required &to open hyperlinks` をオフにする

Editing hyperlinks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ハイパーリンクを編集する手順：

#. リンクテキスト内の任意の場所をクリック
#. 以下のいずれかを行い |HyperlinkDlg| を開く：

   * コンテキストメニューから |EditHyperlinkC| を選択
   * |StandardToolbar| の :guilabel:`Hyperlink` 図像をクリック
   * |MenuBar| から |EditHyperlinkM| を選択
#. 変更を加え |ApplyButton| を押す

複数のハイパーリンクを編集する必要がある場合は、すべてのハイパーリンクを編集する
まで |HyperlinkDlg| を開いたままにしておくことが可能だ。

ハイパーリンクの色を変更する手順：

#. |OptionsDlg|
#. |ApplicationColors|
#. :guilabel:`General` 区画の :guilabel:`Unvisited links` または
   :guilabel:`Visited links` にスクロールしてこれらの選択肢をオンにして、新しい
   色を選択
#. |OK| を押す。

これにより、LibreOffice プログラムのすべてでハイパーリンクの色が変更される。

Rearranging headings and text using the Navigator
======================================================================

Navigator には見出しとそれに関連するテキストを文書内の別の場所に移動する方法がい
くつか用意されている：

* ドラッグ
* 図像
* コンテキストメニュー

見出しの左にある :guilabel:`+` をクリックすると、小見出し一覧が展開する。必要な
見出しをより簡単に見つけるには、:menuselection:`Show &Up to Outline-->` の選択
を変更して、数レベルの見出しのみを表示する。

見出しとそれに関連するテキストや節を文書内で上下に移動させ、見出しのアウトライン
レベルは変更しないようにするには、次のいずれかを実行する：

* Navigator で移動したいテキストブロックの見出しをクリックし、その見出しを見出し
  リストの新しい位置にドラッグする。
* Navigator 目録で見出しをクリックし、

  * :guilabel:`Move Heading Up` または
  * :guilabel:`Move Heading Down`

  図像のいずれかをクリックする。
* Navigator 目録で見出しを右クリックし、コンテキストメニューで

  * :menuselection:`&Move Heading Up` または
  * :menuselection:`Move &Heading Down`

  を選択する。

選択した見出しのみを移動し、関連するテキストを移動しないようにするには次のいずれ
かを行う：

* |Ctrl| を押しながらドラッグ
* 図像をクリック
* コンテキストメニューから選択

.. admonition:: 読者ノート

   これらのコマンドにはキーバインドも定義されている。

   * Move Heading Up: |Ctrl| + |ArrowU|
   * Move Heading Down: |Ctrl| + |ArrowD|

見出しの位置を変えずに、見出しのアウトラインレベル（例えば `Heading 2` から
`Heading 1` や `Heading 3` に上下させる）とそれに関連する小見出しを変更するに
は、次のいずれかを実行する：

* Navigator で見出しを選択し、次の図像のいずれかをクリックする：

  * :guilabel:`Promote Outline Level`
  * :guilabel:`Demote Outline Level`

* Navigatorで見出しを右クリックし、コンテキストメニューから次のメニュー項目を選
  択する：

  * :menuselection:`&Promote Outline Level`
  * :menuselection:`Demote &Outline Level`

選択した見出しのアウトラインレベルだけを変更し、関連する小見出しは変更しないよう
にするには、|Ctrl| を押しながら次のいずれかを実行する：

* 図像をクリック
* コンテキストメニューから選択

.. admonition:: 読者ノート

   これらのコマンドにはキーバインドも定義されている。

   * Promote Outline Level: |Ctrl| + |ArrowL|
   * Demote Outline Level: |Ctrl| + |ArrowR|

Outline folding
======================================================================

アウトラインの折りたたみを使用すると、テキスト、画像、図表、枠、図形、テキスト
ボックスなど、見出しの下にある中身すべての表示有無を切り替えられる。この機能を使
うと編集や読書のために適切な位置まですばやくスクロール可能だ。

.. note::

   この機能を有効にするには |OptionsDlg| |WriterViewPage| で、

   * :guilabel:`&Show outline-folding buttons` を選択する。
   * オプションで :guilabel:`Include sub &levels` を選択する。

Using the Navigator
----------------------------------------------------------------------

Navigator を開き :guilabel:`Heading` を表示する。見出しを何か右クリックし、
:menuselection:`Outline &Folding-->&Toggle` を選択すると、その見出しと同じレベ
ルの次の見出しの間の内容表示有無が切り替わる。

Using a mouse
----------------------------------------------------------------------

見出しの上にマウスポインターを置くと、左余白に小さな矢印が表示される。アウトライ
ンの折りたたみが有効であることを示す。

* 下矢印は見出しとその内容が表示されていることを示す。
* 右矢印は見出しが隠れた内容を持つことを示す。

|Ctrl| を押す。マウスポインターの形が変わったらクリックしてその見出しから同
じレベルの次の見出しまでの間の内容の表示有無を切り替える。

Saving, printing, and exporting folded contents
----------------------------------------------------------------------

Open Document Format (.odt) で保存された文書は隠される内容と見られる内容の現在の
設定が保持される。文書内容は折りたたみ設定の影響を受けない。

.. note::

   隠された内容や折りたたまれた内容は印刷されず、|PDF| にエクスポートされない。
   文書全体を印刷またはエクスポートするにはアウトラインの折りたたみをオフにしろ。

Inserting material from other documents
======================================================================

執筆中の文書で、他のファイルの素材を再利用すれば良いと願うことがあるだろう。例え
ば、共通する段落を含む説明書を書くとする。この段落を各文書に再入力したり、コピー
＆ペーストすることも当然可能だが、共通の段落が編集された場合、その情報が出現する
すべての文書でその情報を更新する必要が生じる。

Writer にはこれらの作業を容易にするツールがいくつかある：

* |Writer06| で説明する |InsertSectionDlg|
* Navigator のドラッグモードにある項目二つ

Navigator ツールを使用するには、まず原文書から挿入したい項目を選択し、

* Insert as Link または
* Insert as Copy

を選択する。この方法では、画像、|OLE| オブジェクト、参照、索引のリンクやコピーを
作成することは不可能だ。

Insert as Link
   ドラッグ＆ドロップした場所に選択した項目をリンクとして挿入する。テキストは保
   護された節として挿入され、原文書へのリンクとしてマークされる。リンクの内容は
   原文書が変更されると自動的に更新される。文書内のリンクを手動で更新するには
   |UpdateLinksM| を実行する。
Insert as Copy
   ドラッグ＆ドロップした場所に選択した項目の独立したコピーを挿入する。テキスト
   は節の中にあるが保護されていない。コピー項目は現文書が変更されても更新されな
   い。節を削除して内容を通常のテキストとして残すことが可能だ。

Line numbering
======================================================================

余白の行番号は、法律文書、詩、プログラミングコードなどでよく使われる。Writer で
は文書全体または選択した段落に行番号を挿入することが可能だ。行番号は文書を印刷す
る際にも載る。行番号の間に分離を追加することも可能だ。

何行ごとに番号を振るか、番号の種類、各ページで番号を振り直すかどうかを選択でき
る。さらに、テキスト分離を別の番号付け方式に設定することも可能だ。

.. admonition:: 読者ノート

   ここは意味がわからない。

文書全体に行番号を追加するには、

#. :menuselection:`&Tools-->&Line Numbering...` を選択し、:guilabel:`Line
   Numbering` ダイアログボックスを開く。
#. 左上隅にある :guilabel:`&Show numbering` をオンにする。
#. 必要なオプションを選択する。
#. |OK| を押す。

文書全体の行番号付けを無効にするには、`Default Paragraph Style` を編集する。段落
スタイルはすべてが `Default Paragraph Style` に基づいているから。

#. Sidebar の |StylesDeck| で :guilabel:`Paragraph Styles` 図像をクリック
#. 木から `Default Paragraph Style` を右クリックし :menuselection:`&Edit
   Style...` を選択
#. |Outline&ListTab| をクリック
#. :guilabel:`&Include this paragraph in line numbering` をオフ
#. |OK| を押す。

特定の段落に行番号を付ける手順：

#. まず文書に対する当該機能を無効にする（上記）
#. 行番号を付けたい段落を選択
#. 次のどちらかを選択：

   * |MenuBar| から :menuselection:`F&ormat-->P&aragraph...`
   * 右クリックメニューから :menuselection:`P&aragraph-->P&aragraph`
#. |ParagraphDlg| の |Outline&ListTab| で :guilabel:`&Include this paragraph in
   line numbering` をオン
#. |OK| を押す。

また、段落を選択して |ParagraphDlg| を開き :guilabel:`&Include this paragraph in
line numbering` をオフにすれば、それ以外のほとんどの段落では有効にしたまま、特定
の段落に対して行番号を無効にすることが可能だ。

行番号を含む段落スタイルを作成し、行番号を付けたい段落に適用することも可能だ。
たとえば、文書内のサンプルコードの行に番号を付けるには、通常のテキストとは異なる
フォントや字下げを使用すればいい。

開始行番号を指定する手順：

#. 段落内をクリックし、上の手順で |ParagraphDlg| を開く
#. |Outline&ListTab| で :guilabel:`&Include this paragraph in line numbering` が
   オンであることを確認する
#. :guilabel:`Rest&art a this paragraph` をオン
#. :guilabel:`&Start with` 欄に行番号を入力
#. |OK| を押す。
