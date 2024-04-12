======================================================================
Writer Guide Chapter 1, Introducing Writer ノート
======================================================================

.. include:: ./abbrev.txt

.. contents:: 本章見出し
   :depth: 2
   :local:

What is Writer?
======================================================================

Writer は LibreOffice のワードプロセッサープログラムだ。ワードプロセッサーの通常
の機能（テキスト入力、編集、書式設定、綴字検査、類語辞典、分綴、自動訂正、検索と
置換など）に加え、重要な機能を他にも搭載している。おいおい見ていく。

Parts of the main Writer window
======================================================================

Writer を起動したときにデスクトップに現れるウィンドウの構成を述べている。

.. note::

   本章の記述はメニューとツールバー主体の GUI についてであって、他にも変種 UI を
   搭載している。:doc:`Chapter 20 <writer20>` 参照。

Title bar
----------------------------------------------------------------------

* タイトルバーはメインウィンドウ最上部にある横長の部分だ。
* タイトルバーには、現在の文書の名前が表示される。新規に作成された文書である場合、
  その名前は :guilabel:`Untitled 1` のようになる。

Menu bar
----------------------------------------------------------------------

タイトルバーの下にあるメニューを本書ではメニューバーと呼称している。本ノートで
は便宜上、単にメニューと記すことが多い。

メニュー項目のラベルに関する一般的な規約が記されている（割愛）。

Sidebar
----------------------------------------------------------------------

Sidebar を開くには :menuselection:`&View --> Sidebar` や :kbd:`Ctrl` + :kbd:`F5`
を用いる。

Sidebar は既定では次の八つの甲板で構成されている：

* :guilabel:`Properties`
* :guilabel:`Styles`
* :guilabel:`Gallery`
* :guilabel:`Navigator`
* :guilabel:`Page`
* :guilabel:`Style Inspector`
* :guilabel:`Manage Changes`
* :guilabel:`Accessibility Check`

各甲板はタイトルバーと内容盤で構成される。盤はツールバーとダイアログボックスを組
み合わせたようなものだ。Sidebar 盤はツールバーと多くの機能を共有している。

盤には :guilabel:`More Options...` ボタンがあるものがあり、これを押すとダイアロ
グボックスが modal で開く。

Sidebar の繋留状態と浮遊状態を切り替えるにはハンバーガーメニューから
:menuselection:`Undock` を実行する。このメニューから
:menuselection:`Customization -->` を使えば Sidebar に乗せるタブを選択可能。

各甲板の概要：

:guilabel:`Properties` 盤
   文書内容を整えるためのツールが並んでいる。選択対象の種類によって盤構成が変化
   する。次の種類については記述がある：

   * テキスト
   * 図表
   * 画像
   * 図面物
   * 枠
   * 映像や音声
:guilabel:`Styles` 盤
   文書で使用されているスタイルの管理、既存スタイル適用、新規スタイル作成、スタ
   イル変更を行う。:doc:`Chapter 8 <writer08>`, :doc:`Chapter 9 <writer09>` で詳
   しく見る。
:guilabel:`Gallery` 盤
   Gallery テーマに含まれる画像と図式を示す。区画が二つある：

   * テーマ名をリストしたもの(矢印、箇条書き、ダイアグラムなど)
   * 選択したテーマに含まれる画像を表示するもの

   詳細については :doc:`Chapter 11 <writer11>` で取り扱う。
:guilabel:`Navigator` 盤
   文書を拾い見て、見出し、図表、枠、画像などの内容品目を選択して整理する。
   :ref:`writer01-anchor1` で詳しくやる。
:guilabel:`Page` 盤
   ページ様式を整えるツールが並ぶ。盤は四つ：

   * :guilabel:`Format`
   * :guilabel:`Styles`
   * :guilabel:`Header`
   * :guilabel:`Footer`

   .. note::

      当甲板のオプションを変更すると、使用中のページスタイルが変更され、現在の
      ページだけでなく、この文書で同じページスタイルを使用しているすべてのページ
      に影響する。

:guilabel:`Style Inspector` 盤
   段落様式、文字様式、手動（直接）整形の属性すべてを表示する。:doc:`Chapter 9
   <writer09>` 参照。
:guilabel:`Manage Changes` 盤
   まだ受理も却下もされていない、追跡された変更を列挙している。ダブルクリックす
   ると変更箇所に飛ぶ。:doc:`Chater 3 <writer03>` 参照。
:guilabel:`Accessibility Check` 盤
   文書内で検出された accessibility の問題を列挙する。ダブルクリックすると問題の
   場所に飛ぶ。:doc:`Chapter 7 <writer07>` 参照。

Toolbars
----------------------------------------------------------------------

初期設定では :guilabel:`Standard` ツールバーが作業場所の上部に繋留されている。

第二のツールバーは :guilabel:`Formatting` だ。この内容はキャレットの現在の位置や
選択物によって決まり、関連するツールが表示される。

Writer にはキャレットや選択範囲の現在の位置に対応するいくつかの追加的ツールバー
がある。例えば、キャレットが

* 図表内にあるときは :guilabel:`Table` ツールバーが、
* 番号付き目録や箇条書き目録内にあるときは :guilabel:`Bullets and Numbering`
  ツールバーが

それぞれ表示される。

:menuselection:`&View --> User &Interface...` で :guilabel:`Sin&gle Toolbar` を
採用すると、ツールバーが単一行になる。

Displaying or hiding toolbars
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ツールバーの表示有無を切り替えるには、

#. メニュー :menuselection:`&View --> &Toolbars -->` に進む
#. 対象ツールバーに対応する項目を選択

活動中のツールバーには、名前の横にチェックマークが表示される。ツールパレットから
作成されたツールバーは、表示メニューには表示されない。

ツールバーを隠す方法としては他にも、対象ツールバー内で右クリックし、
:menuselection:`Close &Toolbar` を実行してもよい。

Sub-menus and tool palettes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ツールバーの図像で、右側に小さな▼があるものはサブメニューやツールパレット、その
他の項目選択方法が表示される。

ツールパレットとはツールバーの一つのツールに付属するツールのポップアップ集だ。

* パレットは浮遊ツールバーにすることもできる。
* 親ツールバーから取り外すと、タイトルバーが表示される。
* ツールパレットは画面の端に沿って浮遊させたり、既存のツールバー領域の一つに繋留
  させたりすることが可能。

.. note::

   ツールパレット上部の点々が表示されていない場合はツールバーが施錠されている。
   次節参照。

Locking and unlocking toolbars
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ツールバーをすべて固定するには：

#. :menuselection:`&View --> &Toolbars --> &Lock Toolbars`
#. LibreOffice を再起動

ツールバーを単品で固定するには：

#. :menuselection:`&View --> &Toolbars --> &Lock Toolbars` がオフであることを確
   認
#. 対象ツールバー右クリックメニュー :menuselection:`&Lock Toolbar Position`

Docking, locking, and moving toolbars
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

繋留されたツールバーは左端の点線ハンドルで表される。繋留を解除し、新しい位置に繋
留移動することも、浮遊したままにしておくことも可能だ。ツールバーの繋留を解除する
方法は：

#. マウスポインターをツールバーハンドルに持って来る
#. ドラッグを開始し、目的地へドラッグする
#. マウスボタンを離す

浮遊ツールバーを移動するには、タイトルバーを目的地までドラッグするか、メインウィ
ンドウの上部か下部へ繋留する。

浮遊ツールバーを繋留するには、

* そのタイトルバーダブルクリックするか、
* ツールバーのどこかを右クリックし :menuselection:`&Dock Toolbar` を実行する。

.. tip::

   ツールバーの点線ハンドルが表示されていない場合は施錠されている。解錠するには
   右クリックメニュー :menuselection:`&Lock Toolbar Position` をオフにする。

浮遊ツールバーをすべて繋留するには、右クリックメニュー :menuselection:`Dock All
Toolbars` を実行

繋留されたツールバーをその位置に固定するには、右クリックメニュー
:menuselection:`&Lock Toolbar Position` を実行。

選択したツールバーを閉じるには、右クリックしてメニュー :menuselection:`Close
&Toolbar` を実行。

Customizing toolbars
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ツールバーのカスタマイズオプションにアクセスするには、ツールバー上を右クリックし
てメニューを開く。

選択したツールバーに定義されている図像の表示有無を切り替えるには、

#. メニュー項目 :menuselection:`Visible &Buttons -->` 以下に移動
#. 対象コマンドの図像選択状態を切り替える

:menuselection:`Customize` ダイアログボックスを開くには次のいずれかを行う：

* 右クリックメニューの :menuselection:`&Customize Toolbar...`
* メニュー :menuselection:`&View --> &Toolbars --> &Customize...`

新規ツールバーを作成することが可能だ。:doc:`Chapter 20 <writer20>` 参照。

Rulers
----------------------------------------------------------------------

作業場の上部に位置する水平定規は初期設定で現れているが、左側の垂直定規はそうでは
ない。これを出現させるには、次のいずれかの操作をする：

* メニュー :menuselection:`&View --> &Rules --> &Vertical Ruler`
* |OptionsDlg| |WriterViewPage| :guilabel:`Verti&cal ruler` をオンにする

両者を表示有無をすばやく切り替えるには :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`R` を
押せ。

Status bar
----------------------------------------------------------------------

Status バーは作業場の下部に位置する。この棒には文書情報と文書機能をすばやく変更
する便利な方法が表示される。

以下、各区画を順に記述している：

文書変更状態
   この FD 図像は文書に未保存の変更があるかどうかを示すために色が変わる。これを
   クリックすることで文書を保存可能。
ページ番号
   現在の列ページ番号、文書総ページ数、現在のページ番号（列ページ番号と異なる場
   合）を表示する。

   文書内にしおりが定義されている場合、この区画を右クリックするとしおり一覧が表
   示される。しおりをクリックすると、キャレットが文書内のその位置に飛ぶ。

   この区画をクリックして :guilabel:`Go to Page` ダイアログボックスを開き、文書
   内の特定のページに飛ぶことが可能だ。
単語数と文字数
   文書中の単語数と文字数が表示され、編集するたびに更新される。テキストの一部を
   選択すると、その選択部分の集計が一時的に文書内のの合計に置き換わる。

   * ここに表示される文字数は空白を含む。空白を除いた文字数を表示するには、この
     区画をクリックするか、メニュー :menuselection:`&Tools --> &Word Count...`
     を実行しろ。
   * 文書全体の単語数と文字数（およびページ数、図表、画像、その他の統計）を表示
     するには :menuselection:`&File --> Propert&ies...` を実行して
     :guilabel:`Statistics` タブを見ろ。
Accessibility 検査状態
   メニュー :menuselection:`&Tools --> Automatic Accessibility Checking` がオン
   である場合、この区画には図像が表示され、文書中の accessibility の問題がいくつ
   あるかを示すツールチップが表示される。Sidebar :guilabel:`Accessibility Check`
   タブに詳細が記載されている。
ページ様式
   現在のページのページ様式が表示される。

   * 別のページ様式を選択するにはこの区画を右クリックしろ。ページ様式一覧が
     ポップアップ表示されるので、クリックして選択しろ。
   * 現在のページ様式の属性を編集するにはこの区画をクリックしろ。:guilabel:`Page
     Style` ダイアログボックスが開く。

   .. caution::

      ここで変更すると、設定方法次第では他のページに割り当てられている様式に影響
      することがある。:doc:`Chapter 8 <writer08>` と :doc:`Chapter 9 <writer09>`
      を参照しろ。

テキスト言語
   綴字、分綴、類語辞典に使用される言語とローカライズが表示される。

   クリックするとメニューが表示され、選択したテキストまたはキャレットのある段落
   の別の言語またはローカライズを選択可能。:doc:`Chapter 3 <writer03>` 参照。

   * テキストを綴字検査から除外するために :menuselection:`&None (Do not
     check spelling)` を選択したり、
   * :menuselection:`&Reset to Default Language` で初期設定言語にリセットするこ
     とも可能だ。
   * :menuselection:`&More...` を選択すると :guilabel:`Character` ダイアログボッ
     クスが開く。
挿入モード
   クリックすると上書きモードになり、もう一度クリックすると挿入モードに戻る。

   * 上書きモードでは、キャレット位置以降のテキストが入力したテキストに置き換え
     られる。
   * :menuselection:`&Edit --> Track Chan&ges --> &Record` が活動中では使えな
     い。
選択モード
   クリックすると選択モード一覧

   * :menuselection:`&Standard selection`
   * :menuselection:`&Extending selection`
   * :menuselection:`&Adding selection`
   * :menuselection:`&Block selection`

   が表示され、クリックするとその選択モードになる。:doc:`Chapter 3 <writer03>`
   参照。図像はモードを示すように変化し、ツールチップはモード名を示す。
署名
   :doc:`Chapter 7 <writer07>` 参照。

   * 文書が署名されている場合、図像が表示される。
   * 図像をクリックすると証明書を表示する。
節情報または物情報
   キャレットが節、見出し、目録に項目にあるときか、または物（画像や図表など）が
   選択されているとき、その項目に関する情報がここに表示される。この区画をクリッ
   クすると、関連するダイアログボックスが開く。
ビューレイアウト
   対応する図像をクリックすると、

   * 単一ページ
   * 複数ページ
   * ブックレイアウト

   のビューが切り替える。どのビューでも文書編集可能。ズーム設定は選択された
   ビューレイアウトとウィンドウ幅と連動して、文書ウィンドウに表示されるページ数
   を決定する。
ズーム
   表示倍率を変更するには次のどれかを行う：

   * ズームスライダーをドラッグ
   * 正負符号をクリック
   * 百分率を右クリックして選択できる倍率値のリストをポップアップ
   * 百分率を右クリックして :guilabel:`Zoom & View Layout` ダイアログボックスを
     開く

Context (right-click) menus
======================================================================

コンテクストメニューは、段落やグラフィックなどを右クリックすることで開く。コンテ
キストメニューが開いたときに利用できる機能や選択肢は、選択されている物よって異な
る。特に、メニューやツールバーのどこにその機能があるのかわからない場合は、この方
法がいちばん簡単だ。

Dialogs
======================================================================

ほとんどの場合、ダイアログボックスが開いている間は文書そのものではなく、ダイアロ
グボックスだけを操作することが許される。ダイアログボックスを閉じると再び文書を操
作できるようになる。

.. admonition:: 読者ノート

   このようなダイアログボックスの挙動を modal であるということにする。

通常、:guilabel:`&OK` または同様のボタンをクリックすると、変更が保存されてダイア
ログボックスが閉じる。:guilabel:`&Cancel` をクリックすると、変更は保存されずにダ
閉じる。

ダイアログボックスの中には modeless であるものがあり、ダイアログボックスと文書を
往復することが可能だ。例としては :guilabel:`Find & Replace` ダイアログボックスが
ある。

Document views
======================================================================

Writer には文書を表示、編集する方法が三つある：

* :menuselection:`&View --> &Normal`
* :menuselection:`&View --> &Web`
* :menuselection:`&View --> F&ull Screen`

Normal ビュー
   * Writer の既定ビューだ。
   * 文書を印刷したり、|PDF| として書き出したりしたときの見てくれが表示される。
   * Status バーの Zoom スライダーと View Layout 図像を使って倍率を変更可能。
   * :menuselection:`&View --> Whitespac&e` はヘッダーとフッター、およびページ間
     の隙間の表示有無を切り替える。これは Status バーで単一ページ表示がアクティ
     ブな場合にのみ機能する。全画面表示でも機能する。
Web ビュー
   * 文書を Web ブラウザーで表示した場合の見えくれを表示する。
   * Zoom スライダーのみが使用できる。
   * Status バーの :guilabel:`View Layout` 図像各種は無効になり、:guilabel:`Zoom
     & View Layout` ダイアログボックスの選択肢のほとんどは使用不可だ。
全画面
   ツールバーや Sidebar は表示されず、あらかじめ選択されているズームやレイアウト
   設定を使用して、文書が利用可能である領域すべてを使用する。

   フルスクリーン表示を終了して前の表示に戻るには次のいずれかの操作をする：

   * :kbd:`Esc` を押す
   * 左上にある浮遊ツールバーの :guilabel:`Full Screen` ボタンをクリックする
   * :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`J` を押す

.. tip::

   メニューから :menuselection:`&Files --> Print Pr&eview...` を使うか、キーバイ
   ンド :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`O` で文書を表示することもできるが、こ
   のビューで編集はできない。:doc:`Chapter 7 <writer07>` を参照しろ。

Starting a new document
======================================================================

LibreOffice では文書をすでに開いている場合、新規文書を作成すると新規ウィンドウが
開く。新規文書の方法は：

* LibreOffice が起動しているが文書が開かれていない場合、Start Center が表示され
  る。ここで図像のいずれかをクリックしてその種類の新規文書を開くか、
  :guilabel:`Templates` 図像をクリックしてテンプレートを使用して新規文書を開始す
  る。
* メニュー :menuselection:`&File --> &New -->` を使い、サブメニューで文書の種類
  を選択する。
* Writer が開いているときにはキーバインド :kbd:`Ctrl` + :kbd:`N` で新規文書を作
  成する。
* LibreOffice で文書がすでに開かれている場合、:guilabel:`Standard` ツールバーの
  :guilabel:`New` 図像をクリックすると、表示されている種類の新規文書が新規ウィン
  ドウに作成される。このアイコンは最後に作成された LibreOffice プログラムによっ
  て変わる。

  * この図像の右にある小さな▼をクリックし、ドロップダウンメニューから文書の種類
    を選択する。

From the Start Center
----------------------------------------------------------------------

Start Center から文書を作成するには：

* 左柱 :guilabel:`&Writer Document` をクリックする。
* 左柱 :guilabel:`T&emplates` をクリックしてテンプレートを選択し、新規文書を作成
  する。

表示される文書の集合を絞るには、:menuselection:`Filter` ドロップダウンリストで文
書の種類を選択する。

利用できなくなった文書を一覧から削除するには右上のハンバーガーメニューを使用す
る。

From a template
----------------------------------------------------------------------

   A template is a set of predefined styles and settings that is used to create
   a new document.

例えば、本書の章はすべて同じテンプレートに基づいて執筆されている。その結果、どの
章も同じヘッダーとフッターを持ち、同じフォントが使われ、同じような見てくれになっ
ている。

テンプレートは自作したり拡張倉庫からダウンロードしたりして拡充可能だ。この話題に
ついては :doc:`Chapter 10 <writer10>` で見ていく。

:guilabel:`Template` ダイアログボックスの開き方は次のいずれかだ：

* キーバインド :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`N`
* メニューから :menuselection:`&File --> Tem&plates > &Manage Templates...`
* メニューから :menuselection:`&File --> &New --> Te&mplates`
* :guilabel:`Standard` ツールバーの :guilabel:`New` 図像の横にある▼をクリック
  し、ドロップダウンリストで :guilabel:`Te&mplates` を選択

テンプレートに基づいて新規文書を作成するには、目的のテンプレートを

* ダブルクリックするか、
* 右クリックメニューから :menuselection:`&Open` を選択する。

Opening an existing document
======================================================================

文書が何も開いていない場合には次のいずれか：

* Start Center で :guilabel:`&Open File` か :guilabel:`Remote File&s` をクリック
* メニューから :menuselection:`&File --> &Open...` か :menuselection:`&File -->
  Open &Remote` を選択
* キーバインド :kbd:`Ctrl` + :kbd:`O`
* Start Center に表示される :guilabel:`&Recent Documents` の一覧からサムネイルを
  クリック

.. note::

   名前が変わったり、別の場所に移ったりしても、文書が Start Center に残って表示
   される。サムネイルを削除するにはマウスポインターを浮かせていると右上にやがて
   現れるバツボタンを押す。

文書がすでに開いている場合には：

* :guilabel:`Standard` ツールバーの :guilabel:`Open` 図像をクリック

  * :guilabel:`Open` 図像の右側にある小▼をクリックし、最近開いた文書一覧から選択
    するか、:menuselection:`Open &Remote File...` を選択
* :menuselection:`&File --> Recent Doc&uments -->` から選択

それから Windows Explorer などの OS 機能から新規文書を作成する方法がある。

Opening files not in OpenDocument Text (.odt) format
----------------------------------------------------------------------

LibreOffice が認識する形式の既存文書を開くにはWindows Explorer などのファイルマ
ネジャーで文書図像をダブルクリックする。

Windows 計算機に Microsoft Office がインストールされていない場合、または
Microsoft Office がインストールされているが Word ファイルタイプ (.doc or .docx)
が LibreOffice と関連付けられている場合、Word ファイルをダブルクリックすると
LibreOffice Writer でそのファイルが開く。

間違ったアプリケーションでファイルが開かないようにするには、ファイルをダブルク
リックせずに、ファイルを右クリックして、:menuselection:`プログラムから開く
(&H)...` から LibreOffice を選択しろ。

Saving a document
======================================================================

保存コマンドが複数ある：

Save
   文書本体、現在のファイルパスを保持する。
Save As
   新規文書を作成したり、ファイル名やファイル形式を変更したり、計算機の別の場所
   に保存したりする。
Save Remote
   文書が遠隔サーバーにすでに保存されているか、これから保存される場合に実行する。
Save a Copy
   現在の文書の複製を保存し、さらに現在の文書を編集を続けるために開いたままにす
   る。
Save All
   現在開いているファイルをすべて保存する。

Save commands
----------------------------------------------------------------------

Save a new file or a previously-saved file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

次のどれかを行う：

* キーバインド :kbd:`Ctrl` + :kbd:`S`
* メニューから :menuselection:`&File --> &Save` を選択
* :guilabel:`Standard` ツールバー :guilabel:`Save` 図像をクリック

初めてファイルとして保存する場合に限り、上記のいずれかを選択すると
:guilabel:`名前を付けて保存` ダイアログボックスが表示される。

Save to a remote server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

詳しくは :ref:`writer01-anchor2`

#. メニューから :menuselection:`&File -> Sa&ve Remote...` を選択
#. :guilabel:`名前を付けて保存` ダイアログボックスで保存先を指定、確認
#. :guilabel:`保存 (&S)` ボタンを押す

Save a copy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

このコマンドを使用すると、文書を開いたまま編集を続けることができ、また現
在のバージョンの別個の複製を保存する。

#. メニューから :menuselection:`&File -> Save a Cop&y...` を選択
#. :guilabel:`名前を付けて保存` ダイアログボックスで名前、種類、保存先を指定、確
   認
#. :guilabel:`保存 (&S)` ボタンを押す

この操作では複製は開かれない。原文書は開いたままになる。

Save all
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

メニューから :menuselection:`&File -> Sa&ve All` を選択すると、開いているファイ
ルすべてが名前、形式、パスを変更せずに保存される。

Save As command
----------------------------------------------------------------------

ファイル名やファイル形式を変更したり、計算機上の別の場所に保存したりすることで、
現在の版を新しい文書として保存する。

次のいずれかで :guilabel:`名前を付けて保存` ダイアログボックスを開く：

* メニューから :menuselection:`&File --> Save &As...` を選択
* キーバインド :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`S`

.. note::

   LibreOffice では |PDF| や :abbr:`ePub (Electronic PUBlication)` など、ファイ
   ルタイプの変更を伴うファイル操作に対して export という用語を用いる。
   :doc:`Chapter 7 <writer07>` で見ていく。

Saving documents automatically
----------------------------------------------------------------------

Writer は文書を一時ファイルに定期的に自動保存し、バックアップを作成する。時間間
隔を設定したり、自動保存やバックアップをオフにする手順は次のとおり：

#. |OptionsDlg| を開く
#. :menuselection:`Load/Save --> General` ページを開く
#. :guilabel:`Save &AutoRecovery information every` をオンにして時間間隔を指定す
   る
#. :guilabel:`Al&ways create backup copy` を好みで設定する
#. :guilabel:`&OK` を押す
#. LibreOffice を再起動するように促されたらすぐに再起動するか、後で再起動するか
   を選択する

変更は再起動後から有効。

バックアップコピーは :menuselection:`LibreOffice --> Path` ページで指定したフォ
ルダーに蓄積する。

:doc:`Chapter 20 <writer20>` 参照。

Saving as a Microsoft Word document
----------------------------------------------------------------------

Save As コマンド実行途中でファイル形式を指定する際に、ドロップダウンリストから求
める Microsoft Word 形式の一つを指定すればいい。

.. tip::

   Writer で文書を Microsoft Word 形式でいつでも保存するには :guilabel:`Options`
   ダイアログボックスの :menuselection:`Load/Save --> General` ページを開いて、
   下の方にある :guilabel:`Always sa&ve as` の値を希望のファイル形式に設定する。

Exchanging documents with users of Apple Pages
----------------------------------------------------------------------

Writer は Apple Pages 形式 (.pages) のファイルを開いて編集することは可能だが、そ
のファイル形式で保存したり、にエクスポートしたりすることは不可能だ。Apple Pages
は OpenDocument 形式のファイルを開くことが不可能であるため、Pages 利用者とファイ
ルを共有する必要がある場合は、.odtファイルを .rtf や .docx などの互換性のある形
式に保存しろ。

Using password protection and OpenPGP encryption
======================================================================

LibreOffice には二種類の文書保護機能がある：

* パスワードによる保護
* OpenPGP による暗号化

保存パスワードで暗号化されたファイルはパスワードなしでは復号不能。文書を復号する
必要のある者にパスワードを送信する必要がある。OpenPGP 暗号化では、文書はアルゴリ
ズムを使って暗号化される。暗号化には鍵が必要だ。

各キーは一度だけ使用され、文書とともに送信される。

Password protection
----------------------------------------------------------------------

LibreOffice にはパスワード保護が二つある：

* 読み取り保護。パスワードなしではファイルを閲覧できない。
* 書き込み保護。読み取り専用モードでファイルを閲覧できるが、パスワードなしでは変
  更できない。

文書をパスワードで保護する手順：

#. メニューから :menuselection:`&File --> Save &As...` を選択
#. 保存ダイアログボックス左下にある :guilabel:`Save with password` をオンにし、
   :guilabel:`保存 (&S)` を押す
#. :guilabel:`Save Password` ダイアログボックスではいろいろ選択肢がある。

   * 文書を読み取り禁止にするには、上部にある入力欄二つにパスワードを入力する。
   * 文書を書き込み禁止にするには :guilabel:`&Options` をクリックして
     :guilabel:`Open &file read-only` をオンにする。
   * 書き込みは保護するが、選択した人に編集を許可するには、:guilabel:`Open file
     read-only` をオンにし、かつ下にある入力欄二つにパスワードを入力する。
#. :guilabel:`&OK` を押す

.. caution::

   パスワードを紛失すると文書の内容を復元することはほとんど不可能。

Changing or removing the password for a document
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

文書がパスワードで保護されている場合、文書を開いている間にパスワードを変更または
削除することが可能だ：

#. メニューから :menuselection:`&File --> Propert&ies...` を選択
#. :guilabel:`General` タブをクリック
#. :guilabel:`Change &Password` ボタンを押す

OpenPGP encryption
----------------------------------------------------------------------

LibreOffice は計算機にインストールされている OpenPGP ソフトウェアを使用する。

OpenPGP アプリケーションでは個人用暗号鍵ペアを定義する必要がある。

OpenPGP 暗号化は受信者の公開鍵を使用する必要がある。この鍵は計算機に保存されてい
る OpenPGP key chain で使用できる必要がある。

.. admonition:: 読者ノート

   これは全然試せていない。

.. _writer01-anchor2:

Opening and saving files on remote servers
======================================================================

LibreOffice は、遠隔サーバーに保存されたファイルを開いたり保存したりできる。

* 遠隔サーバーにファイルを保存しておけば、さまざまな端末で文書を扱える。
* 遠隔サーバーにファイルを保存することで、文書をバックアップし、端末の紛失や記憶
  ストレージの故障からデータを守る。
* ファイル出納をチェックできるサーバーならば、ファイルの使用やアクセスを管理する
  ことが可能だ。

LibreOffice は

* :abbr:`FTP (File Transfer Protocol)`,
* WebDav
* Windows share
* :abbr:`SSH (Secure SHell)`

などのよく知られたネットワークプロトコルを使用する多くの文書サーバーに対応してい
る。

また、Google Drive や Microsoft OneNote のような一般的なサービスや、OASIS CMIS
標準を実装した商用およびオープンソースのサーバーにも対応してる。

Moving quickly through a document
======================================================================

文書内を素早く移動し、特定の項目を見つける方法各種：

* :guilabel:`Go to Page`
* Navigator
* アウトライン折りたたみ
* 覚書

Using Go to Page
----------------------------------------------------------------------

次の方法で、文書内の特定のページに飛べる：

* Navigator の右上にある Go to Page 欄を使う。
* :guilabel:`Go to Page` ダイアログボックスを使う。入力欄に移動先のページ番号を
  入力し、:guilabel:`&OK` をクリックする。

:guilabel:`Go to Page` ダイアログボックスの開き方は次のどれでもかまわない：

* Status Bar 上のページ番号欄をクリック
* メニューから :menuselection:`&Edit --> Go t&o Page...` を選択
* キーバインド :kbd:`Ctrl` + :kbd:`G`

.. _writer01-anchor1:

Using the Navigator
----------------------------------------------------------------------

Navigator には見出し、図表、テキスト枠、画像、しおり、その他の物が一覧表示される。
Navigator を開くには次のいずれかを行う：

* Sidebar 右柱 :guilabel:`Tab` 盤上の :guilabel:`Navigator` タブをクリック
* :guilabel:`Standard` ツールバーの :guilabel:`Navigator` 図像があればクリック
* キーバインド :kbd:`F5`
* メニュー :menuselection:`&View --> Na&vigator` をオン

品目内項目一覧を見るには正符号をクリックする。

.. note::

   マスター文書では Navigator 機能はここで述べられているものと異なる。
   :doc:`Chapter 16 <writer16>` で見る。

Navigator は文書内を移動したり、項目を探したりするための便利な方法をいくつか搭載
している。機能名だけ羅列しておく：

* Navigate By
* Header/Footer
* Anchor ↔ Text
* Set Reminder
* Previous/Next
* Go to Page
* Content Navigation View
* List Box On/Off
* Heading Levels Shown
* Drag Mode
* Promote/Demote Level
* Promote/Demote Chapter

.. note::

   文書内の隠秘部分は Navigator では灰色で表示され、ツールチップとして
   :guilabel:`hidden` という文字が表示される。:doc:`Chapter 6 <writer06>` 参照。

.. tip::

   オブジェクトには識別できる名前が付けられている方が見つけやすい。既定では
   LibreOffice は Image1, Image2, Table1, Table2, etc. の名前を与える。これらの
   名前は、オブジェクトが文書に追加された順に付けられる。文書内のそれらの位置と
   は一致しない場合がある。

   オブジェクトの名前は挿入後に変更可能。たとえば、画像の名前を変更するには、

   #. Navigator でその名前を右クリック
   #. コンテキストメニュー :menuselection:`Rename...` を選択
   #. ビューが画像に飛び、:guilabel:`Rename object` ダイアログボックスが開く
   #. :guilabel:`&New name` 欄に入力
   #. :guilabel:`&OK` を押して確定

   画像を直接右クリックして :menuselection:`&Properties...` を選んでも変更可能。

Using outline folding
----------------------------------------------------------------------

アウトライン折りたたみを使えば、テキスト、画像、図表、枠、図形、テキストボックス
など、見出しの下にある内容すべてを隠したり現したりすることが可能だ。

この機能を有効にするには

#. |OptionsDlg| を開く
#. :menuselection:`LibreOffice Writer --> View` ページを開く
#. :guilabel:`&Show outline-folding buttons` をオンにする
#. 好みで :guilabel:`Include sub &levels` をオンにする

アウトライン折りたたみは Navigator と連動し、マウスを使って直接行える。詳しくは
:doc:`Chapter 3 <writer03>` でやる。

Setting reminders
----------------------------------------------------------------------

覚書を使うと、後で文書に戻りたい場所に印をつけることができる。

現在のキャレット位置に覚書を設定するには Navigator の :guilabel:`Set Reminder`
図像をクリックする。

* 覚書を設定できるのは文書一つに対しては最大五つまで
* 六つ目の覚書を設定すると最初のものは削除される

覚書は文書内で強調されず、Navigator にも列挙されないため、覚書がどこにあるかはわ
からない。

覚書間を飛ぶには、

#. :guilabel:`Navigate By` ドロップダウンリストで :guilabel:`Reminder` を選択
#. :guilabel:`Previous Reminder` 図像と :guilabel:`Next Reminder` 図像をクリック

覚書は文書に保存されない。

Undoing and redoing changes
======================================================================

元に戻す：

* キーバインド :kbd:`Ctrl` + :kbd:`Z`
* メニューから :menuselection:`&Edit --> &Undo`
* :guilabel:`Standard` ツールバーの :guilabel:`Undo` 図像をクリック

  この図像の右にある▼をクリックすると元に戻せる変更すべての一覧が現れる。
  この一覧上で連続する変更を選択し、一気に戻すことが可能だ。

変更が取り消された後、Redo コマンドが有効になる：

* メニューから :menuselection:`&Edit --> &Redo`
* キーバインド :kbd:`Ctrl` + :kbd:`Y`
* :guilabel:`Standard` ツールバーの :guilabel:`Redo` 図像をクリック

  Undo と同様に、:guilabel:`Redo` 図像の▼をクリックすると、元に戻せる変更の一覧
  が表示される。

Displaying multiple views of a document
======================================================================

LibreOffice では、同じ文書を複数のビューで同時に開き、閲覧、編集することが可能だ。

これらのビューは、異なるページを表示したり、異なるズームレベルを適用したり、その
他の設定を使用したりできるウィンドウに表示される。ウィンドウの一つで文書を変更す
ると、他のウィンドウにも即座に反映される。あるページから別のページに情報をコピー
したり移動したりする場合に便利だろう。

文書を表示するウィンドウを新規に開くには、メニューから :menuselection:`&Window
--> &New Window` を選択する。

* 開かれた各ウィンドウにはタイトルバーのファイル名に番号が自動的に付けられる。
* 他の LibreOffice 文書を同時に開いている場合、ウィンドウの一覧にはそれらも含ま
  れる。
* アクティブウィンドウには一覧のファイル名の横に印が示される。
* ウィンドウを切り替えるには、次のどれかを行う：

  * 一覧内の名前をクリック
  * ウィンドウが表示されている場合はウィンドウ自体をクリック

アクティブウィンドウを閉めるには、次のいずれかを行う：

* :menuselection:`&Window --> &Close Window`
* キーバインド :kbd:`Ctrl` + :kbd:`W`
* メニューバーかタイトルバーの :kbd:`Close` 図像をクリック

Reloading a document
======================================================================

.. admonition:: 読者ノート

   他のアプリケーションで言うところの Revert に近い。

文書を再読み込みするには、メニューから :menuselection:`&File --> Re&load` を選択
する。前回の保存以降にファイルに変更を加えた場合、Reload を実行すると前回の変更
が破棄されることを警告する確認ダイアログボックスが表示される。

Closing a document
======================================================================

文書を閉じるには次のいずれかを行う：

* メニューから :menuselection:`&File --> &Close` を選択
* メニューバーの右端 (Windows) のバツボタンをクリック

Windows で最後の文書を閉じると、LibreOffice Start Center が開く。

最後の変更以降、文書が保存されていない場合はメッセージボックスが表示される。
