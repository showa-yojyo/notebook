======================================================================
Calc Guide Chapter 6, Using Images and Graphics ノート
======================================================================

.. include:: ./calc-inc.txt

.. contents:: 章見出し
   :local:
   :depth: 3

Introduction
======================================================================

Calc で読み込める形式の一覧は LibreOffice |Help| から確認しろ。

Calc で画像を使用する方法は LibreOffice の他のプログラムでそれを使用する方法と似
てる。詳細については |Guide| または |Draw| を参照しろ。

.. note::

   次の一節はだいじなのでそのままコピーしておく：

      In LibreOffice, the terms *graphics* and *images* refer to both pictures
      and drawing objects. Often the word images is used when referring to
      pictures and other graphics that are not drawing objects.

Adding graphics (images) to a spreadsheet
======================================================================

Inserting an image file
----------------------------------------------------------------------

画像が計算機に保存されているファイルの場合は以下に記されるいずれかの方法でスプ
レッドシートに挿入することが可能だ。

Drag and drop
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Explorer などから画像ファイルをシート内にドラッグ＆ドロップすればいい。この方法
では画像のコピーが文書内に保存される（この形態を埋め込みという）。

|Ctrl+Shift| を押しながらドラッグすると、埋め込みではなくリンクになる。

Insert Image dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. スプレッドシート上、画像を示す位置をクリックする
#. |MenuBar| で :menuselection:`&Insert-->&Image...` を実行する
#. |InsertImageDlg| で使う画像ファイルに移動して選択する
#. 埋め込みかリンクかを :guilabel:`Link` チェックボックスで指定する
#. :guilabel:`Anchor` ドロップダウンリストから錨を選択する：

   * `To cell`
   * `To cell (resize with cell)`
   * `To page`

   これらのオプションの詳細は :ref:`calc06-anchor-anchoring` を見ろ。

#. |Open| を押すと画像ファイルの内容が指定した升目などに描かれる。

.. note::

   画像をリンクすることを選択した場合、リンクを続行するか、代わりに画像を埋め込
   むかのオプションを含むメッセージボックスを表示することがある。この確認を今後
   表示しないようにするための選択が用意されている。

Linking or embedding an image file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

画像をスプレッドシートに埋め込むと、その画像はスプレッドシートファイルの永続的な
部分となる。埋め込んだ画像に加えた変更は元画像ファイルに影響しない。

|InsertImageDlg| で :guilabel:`Link` をオンにしたか、ドラッグ＆ドロップで
|Ctrl+Shift| を使用した場合、画像を埋め込まれるのではなく、画像を含むファイルへ
のリンクが生じる。画像は文書に描画されるが、文書を保存すると、画像そのものではな
く、画像ファイルへの参照だけが含むようにする。文書と画像は別々のファイルとして残
り、文書を再度開いたときに初めてマージされます。

リンクと埋め込みの長所短所比較は、シンボリックリンクとハードリンクのそれととても
似ている。

リンクを多用する場合には |MenuBar| :menuselection:`&Edit-->Lin&ks to External
Files...` コマンドが重要だ。参照を差し替えたり、埋め込みに変えたりすることが可能
だ。

.. note::

   文書に同じ画像を何度もはめ込む場合、リンクを作成したほうが良いと思うかもしれ
   ない。しかし、LibreOffice では文書に画像ファイルのコピーを一つしか埋め込まな
   いため、その必要はない。コピーの一つや二つを削除しても、同じファイルの他のコ
   ピーには影響しない。

Embedding linked images
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

リンクはいつでも埋め込みに変えることが可能。手順：

#. |MenuBar| から |EditLinksM| を実行して |EditLinksDlg| を開く
#. 目的の画像項目を一覧から選択
#. :guilabel:`&Break Link` ボタンを押す

.. note::

   埋め込み画像からリンク画像にするのは面倒だ。それぞれのファイルを再度はめ込む
   際に :guilabel:`Link` をオンにし、一つずつ置き換える必要がある。

Inserting an image from the clipboard
----------------------------------------------------------------------

システムクリップボードの内容が画像データの場合、|EditPasteM| (|Ctrl| + :kbd:`V`)
でそれを埋め込める。

.. caution::

   画像を貼り付ける前にコピー元のアプリケーションを終了すると、クリップボードに
   保存されていた画像が失われる可能性がある。

Inserting an image using a scanner
----------------------------------------------------------------------

光学走査装置が PC に接続されている場合、そこから取り込むコマンドがある：

#. |MenuBar| から :menuselection:`&Insert-->&Media-->&Scan-->&Select Source...`
   を実行
#. 光学走査装置を選択
#. 画像を挿入する場所にポインターを置く
#. |MenuBar| から :menuselection:`&Insert-->&Media-->&Scan-->&Request...` を実行

通常は画像を画像処理プログラムへいったん取り込み、整形してファイルに保存してから
それを先述の方法で追加するのが品質上望ましい。

Inserting an image from the Gallery
----------------------------------------------------------------------

Gallery は文書に挿入できる画像や音声などの再利用可能な物をグループ化する便利な方
法だ。Gallery は LibreOffice プログラムすべてで利用可能だ。LibreOffice に付属の
画像だけでなく、自分で作成した画像を追加することも可能だ。|Guide| を見ろ。

#. |MenuBar| から :menuselection:`&View-->&Gallery` を実行
#. テーマを選択
#. 物をクリック
#. 文書中にそれをドラッグ＆ドロップするか、右クリックメニューで
   :menuselection:`&Insert` を実行

Modifying images
======================================================================

* Calc で行った画像修正は、埋め込みであれリンクであれ、元画像には影響しない。
* 簡易な修正ならば Calc にある機能を用いてよい。

Using the Image toolbar
----------------------------------------------------------------------

画像を入れたり、既存の画像を選択すると |FormattingToolbar| の代わりに
|ImageToolbar| が現れる。現れない場合には |MenuBar| から
:menuselection:`&View-->&Toolbars-->Ima&ge` を選択しろ。

|FormattingToolbar| の構成：

:guilabel:`Select anchor for object` ドロップダウンリスト
   画像をセルに固定するかページに固定するかを選択する。
   :ref:`calc06-anchor-anchoring` を見ろ。
:guilabel:`Align Objects` ドロップダウンリスト
   画像が複数選択されている場合、画像同士の水平・垂直方向の位置関係を調整する。
   :ref:`calc06-anchor-aligning` を見ろ。
画像を積み重ねる順番に配置する
   :ref:`calc06-anchor-arranging` を見ろ。

   * :guilabel:`Bring to Front`
   * :guilabel:`Forward One`
   * :guilabel:`Back One`
   * :guilabel:`Send to Back`
   * :guilabel:`To Foreground`
   * :guilabel:`To Background`
画像の境界線の属性設定
   * :guilabel:`Line Style` ドロップダウンリスト
   * :guilabel:`Line Width` スピンボタン
   * :guilabel:`Line Color` ドロップダウンリスト
:guilabel:`Area Style / Filling` ドロップダウンリスト
   画像そのものではなく、画像を含む背景領域の色やその他の特性を設定する。背景を
   見えるようにするには画像の透明度を適切な高さに設定する必要がある。領域を変更
   する方法の詳細については |Draw| を見ろ。
:guilabel:`Shadow` ボタン
   画像周囲に既定の影を描く効果を設定する。影効果を調整するには
   :menuselection:`F&ormat-->Text B&ox and Shape-->A&rea...` を選択して
   :guilabel:`Area` ダイアログボックスを開き、:guilabel:`Shadow` タブをクリック
   する。
:guilabel:`Filter` ドロップダウンリスト
   :guilabel:`Image Filter` ツールバーを開く。|Draw| 参照。
:guilabel:`Image Mode` ドロップダウンリスト
   画像の描画を次から選んで変更する：

   * `Default`
   * `Grayscale`
   * `White/Black`
   * `Watermark`
:guilabel:`Crop Image` ボタン
   画像の周囲に切り抜きハンドルを配置する。ハンドルをドラッグすると画像の端を切
   り抜く（隠す）ことができる。
:guilabel:`Flip Horizontally` ボタンと :guilabel:`Flip Vertically` ボタン
   画像の向きを変える。
:guilabel:`Rotate` ボタン
   画像の周囲に回転ハンドルを配置する。
:guilabel:`Transparency` スピンボタン
   画像の透明度を 0% から 100% の間に調整する。
:guilabel:`Color` ボタン
   :guilabel:`Color` ツールバーを開き、赤、緑、青、明度、対比（どう和訳するべき
   か）、ガンマ値を調整する。

Using the Properties deck in the Sidebar
----------------------------------------------------------------------

|ImageToolbar| の設定の一部は、画像選択中に |Sidebar| |PropertiesDeck| でも利用
可能だ。ここには :guilabel:`Image`, :guilabel:`Line`, :guilabel:`Position and
Size`, :guilabel:`Columns` 設定がある。

Adding text
----------------------------------------------------------------------

画像や図面物にテキストを追加可能。そのようなテキストは画像が再配置されるときに画
像と一緒に移動する。

#. 画像をダブルクリックする。:guilabel:`Text Formatting` ツールバーが開く。
#. テキストをタイプし、このツールバーを用いて書式を与える。

このようなテキストを調整するには、画像右クリックメニューから
:menuselection:`&Text...` を実行する。ダイアログボックスが開く。ここで調整しろ。

.. _calc06-anchor-transform:

Positioning, resizing, and arranging images
======================================================================

Using the mouse
----------------------------------------------------------------------

画像の幾何を修正するには、他の描画ソフトの感覚でマウスを用いればいい。キーボード
を併用する編集動作もある。

* 画像の元の比率を維持するには、コーナーハンドルのいずれかをドラッグしろ。
* 比率を変更したい場合は |Shift| を押しながらコーナーハンドルのいずれかをドラッ
  グしろ。

Using the Position and Size dialog
----------------------------------------------------------------------

スプレッドシートで画像の位置と寸法を正確に指定するには、まず次のいずれかを選択す
る：

* |MenuBar| から :menuselection:`:menuselection:`F&ormat-->Text B&ox and
  Shape-->Position and Si&ze...`
* 右クリックメニューから :menuselection:`Position and Si&ze...`

|Position&SizeDlg| が開く。|Pos&SizeTab| でこれらの値を設定可能だ：

Position
   スプレッドシート上の選択画像の位置。

   :guilabel:`Position &X`
      グリッドで選択された基点からの水平距離。
   :guilabel:`Position &Y`
      グリッドで選択した基点からの垂直距離。
Size
   選択した基点に対する画像の幅と高さ。
Protect
   誤って画像が移動したり、寸法が変更されたりするのを防ぐために、関連オプション
   を選択。

座標単位系および画像の寸法に用いる測定単位は |OptionsDlg| |CalcGeneralPage|
:guilabel:`Measurement &unit` で設定する。

位置と寸法の既定の基点はスプレッドシートの左上隅だ。この基点を一時的に変更して、
位置決めや寸法記入を簡単にすることが可能。この変更は一度きりで、
|Position&SizeDlg| を閉じると基点は標準の左上隅の位置にリセットされる。

画像を回転させたり斜めにしたりすることもできる。|Position&SizeDlg| の
:guilabel:`Rotation` タブまたは :guilabel:`Slant & Corner Radius` タブを使う。詳
しくは |Draw| を見ろ。

.. _calc06-anchor-arranging:

Arranging images
----------------------------------------------------------------------

スプレッドシートに配置する各画像は、重ね掛かっているかどうかにかかわらず、直前の
画像に連続して重ね合わせられる。テキストの重ね順は変更不能だ。

#. 変更したい画像を選択する。
#. |MenuBar| から :menuselection:`F&ormat-->A&rrange-->` を選択するか、画像を右
   クリックし、コンテキストメニューから :menuselection:`A&rrange-->` を選択する。
#. または、|ImageToolbar| の配置図像六つのいずれかをクリックし、画像をすばやく上
   下に移動する。

移動選択肢は次のとおり：

:menuselection:`&Bring to Front`
   選択した画像を積み重ね順の天井に移し、他のどの画像の前にもあるようにする。
:menuselection:`&Forward One`
   選択した画像を1段上に移動し、積み重ね順の一番上に近づけます。
:menuselection:`Back &One`
   選択画像を一段下に移す。積み重ね順の底に近づく。
:menuselection:`&Send to Back`
   選択画像を積み重ね順の底に移し、他のどの画像の後ろにもあるようにする。
:menuselection:`&To Foreground`
   選択画像をテキストの前面に移す。
:menuselection:`To Ba&ckground`
   選択画像をテキストの後面に移す。背景画像を選択し、それを修正したり置き換えた
   りするには Navigator を使う必要がある。

.. _calc06-anchor-anchoring:

Anchoring images
----------------------------------------------------------------------

他の何かとの位置関係を保つように画像を錨で繋留しろ。

`To Page`
   画像をページに留まらせ、特定の場所に配置する。
`To Cell`
   画像を升目に留まらせ、固定されている内容と共に表示される。例えば画像がセル
   B10 に繋留している場合、新しい行がすぐ上に挿入されたとする。このとき、画像は
   B11 に繋留し直す。
`To Cell (resize with cell)`
   錨セルの寸法を変更すると、画像のそれも変更される。

選択画像を繋留させたり、使用する錨の種類を変更するには：

#. 次のいずれかで関連メニューを開く：

   * |MenuBar| から :menuselection:`F&ormat-->Anc&hor-->` を選択
   * 画像右クリックメニュー :menuselection:`Anc&hor-->` 各種コマンドを選択
   * |ImageToolbar| から :guilabel:`Anchor` 図像をクリック
#. 対応するメニュー項目を選択：

   * :menuselection:`To &Page`
   * :menuselection:`To &Cell`
   * :menuselection:`To Cell (&resize with cell)`

.. tip::

   画像の寸法を升目のそれに変更するには、画像右クリックメニューから
   :menuselection:`&Fit to Cell Size` を実行しろ。

.. _calc06-anchor-aligning:

Aligning images
----------------------------------------------------------------------

ワークシートに画像が複数ある場合、これらを整列させて体裁を整えることが可能だ。

選択肢には、画像を水平に揃えるもの（左、中央、右）と、画像を垂直に揃える（上、中
央、下）ものがある。手順は：

#. 対象画像を |Shift| を押しながらクリックするなどして同時に選択する。
#. 右クリックメニュー :menuselection:`Alig&n Objects-->` のいずれかのコマンドを
   実行する。

.. tip::

   |ImageToolbar| の :guilabel:`Align Objects` 図像自体から選択した画像をすばや
   く左揃えにできる。

.. _calc06-anchor-grouping:

Grouping and ungrouping images
----------------------------------------------------------------------

画像グループの考え方は Inkscape などと同じだ。次の関連コマンドがメニュー
:menuselection:`F&ormat-->&Group` にある：

* :menuselection:`&Group`, :menuselection:`&Ungroup`
* :menuselection:`&Enter Group`, :menuselection:`E&xit Group`

.. note::

   画像グループは `To Page` モードで繋留される。錨はいつもどおり変更可能だ。

Using LibreOffice's drawing tools
======================================================================

Calc にも LibreOffice の他のプログラムと同様に、長方形、円、線、テキスト、その他
の図形を使用して、簡単な図などの図面を作成するためのさまざまなツールがある。複数
の図面物をグループ化して、移動や寸法を変更をしても相対的な位置や比率が維持される
ようにすることが可能だ。

複雑な図面を作成する必要がある場合は、LibreOffice Draw を使用し、それをスプレッ
ドシートに挿入することが推奨される。|Draw| を見ろ。

Drawing toolbar
----------------------------------------------------------------------

:menuselection:`&View-->&Toolbars-->Dra&wing` で |DrawingToolbar| を表示する。こ
れを使って簡単な図形をシートに挿入することが可能だ。

|DrawingToolbar| が開くとツール集が表示される。ツールの上にマウスポインターを置
くと、その機能を説明するツールチップが表示される。右側の小さな▼はツールのパレッ
トを開く。|DrawingToolbar| にツールを追加するには、ツールバーの何もない場所で右
クリックし、コンテキストメニューから :guilabel:`Visible &Buttons-->` を選択する。

#. |DrawingToolbar| のボタンを押す。マウスポインターが十字ポインター
   に、|FormattingToolbar| が |DrawingObjPropToolbar| にそれぞれ変化する。
#. 図面物を示したい場所に十字ポインターを移動し、クリック、ドラッグして作図する。
   マウスボタンを放す。選択された描画機能は活動中のままなので、同じ種類の別の物
   を描画することが可能。

押した描画コマンドを取り消すには、次のいずれかの操作をしろ：

* 同じツールバーボタンをもう一度クリックする
* |Esc| を押す
* |DrawingToolbar| の :guilabel:`Select` ボタンを押す

図面物の性質（塗りつぶしの色、線の種類と太さ、錨など）を編集するには、次が使え
る：

* |DrawingObjPropToolbar|
* |Sidebar| |PropertiesDeck|
* 右クリックメニューの関連コマンド各種

Setting the properties of drawing objects
----------------------------------------------------------------------

描画物の性質の詳細については |Draw| を見ろ。

描画前に図面物の既定特性を設定することが可能。これらの既定特性は現在のスプレッド
シートにのみ適用され、閉じても保持されない。

#. |DrawingToolbar| の :guilabel:`Select` ボタンを押す
#. |DrawingObjPropToolbar| ではボタン等がいくつか活動中になっている。各性質に用
   いる既定値を設定することが可能だ。

物を描画したり、他の物とグループ化したりすると、より多くの特性が活動中になる。こ
れらはツールバー等の関連 UI に反映される。

既存の図面物の性質を編集するには、前節最後に述べた方法により可能。

Resizing drawing objects
----------------------------------------------------------------------

画像の場合と同様のハンドルによる操作が図面物に適用される。
:ref:`calc06-anchor-transform` を見ろ。

Grouping and ungrouping drawing objects
----------------------------------------------------------------------

画像の場合と同様に図面物もグループになり得る。:ref:`calc06-anchor-grouping` を見
ろ。

Additional tools
======================================================================

画像や図面物の右クリックメニューにはその他雑多なコマンドがある。

* :menuselection:`A&ssign Macro...` でマクロを図面物に仕込める。マクロ
  を学んでからここに戻れ。
* 個人的に注意したいものは :menuselection:`Co&mpress...` だ。埋め込んだ画像デー
  タを圧縮すればファイルサイズが小さくなる。

:menuselection:`Alt &Text...`
   画像には表題と説明という形でメタデータを追加可能だ。この情報は画面読み上げソ
   フトや、文書を |HTML| にエクスポートする際の代替テキスト属性 ALT として用いら
   れる。
:menuselection:`N&ame...`
   画像に割り当てるカスタム名を追加可能だ。Navigator で画像を検索しやすくなる。
   画像に名前を付けると、複数人が同じスプレッドシートで作業しているときに、画像
   を識別しやすくもなる。
:menuselection:`&Rot&ate or F&lip`
   画像を回転させたり、水平または垂直に反転させることが可能だ。
:menuselection:`A&ssign Macro...`
   画像にプログラム可能な機能を追加できるように :guilabel:`Assign Macro` ダイア
   ログを開く。詳しくは |Calc13| を見ろ。
|EditHyperlinkC|
   画像からスプレッドシート内の別の場所、別の文書、Web ページへのハイパーリンク
   を定義する。|HyperlinkDlg| を開くには、コンテキストメニュー |EditHyperlinkC|
   を選択する。ハイパーリンクの詳細については |Calc11| を見ろ。
:menuselection:`Co&mpress...`
   画像を圧縮してスプレッドシートのファイルサイズを小さくできる。コンテキストメ
   ニューの :menuselection:`Compress...` を選択すると :guilabel:`Compress Image`
   ダイアログが開き、圧縮オプションを設定できり。図面物ではこのオプションは使用
   できない。
:menuselection:`Edit &with External Tool`
   外部ツールを使って画像を編集可能。|OpenFileDlg| は計算機の設定によって異なる。
   図面物では使用できない。

.. admonition:: 読者ノート

   * :menuselection:`Alt &Text...` 項目は本書と名称が異なるので現況に合わせた。
   * |EditHyperlinkC| は対象がハイパーリンクを有する場合にのみコンテキストメ
     ニューに現れる項目のようだ。

Using Fontwork
======================================================================

Fontwork を使うと、画像的なテキスト芸術作品を作成し、作品をより魅力的にすること
ができる。テキスト芸術作品にはさまざまな設定（線、領域、位置、寸法等）があるため
に選択肢が多くある。

Fontwork は LibreOffice の各プログラムで利用できる、各プログラムが描画する方法に
は小さな違いがある。

.. admonition:: 読者ノート

   文字列だけからロゴタイプを生成する機能だ。

Creating a Fontwork object
----------------------------------------------------------------------

#. :menuselection:`&View-->&Toolbars-->Fontwor&k` 実行
#. :guilabel:`Insert Fontwork Text` を押す
#. :guilabel:`Fontwork Gallery` から一つ選択し |OK| を押す

Fontwork テキストを編集するには対象をダブルクリックしろ。

#. テキストを選択し、対象物の上に表示される黒い Fontwork テキストの代わりに、独
   自のテキストを打ち込め。
#. 変更を適用するには、空いている場所のどこかをクリックするか、|Esc| を押せ。

Editing a Fontwork object
----------------------------------------------------------------------

Fontwork オブジェクトを選択して次を使え：

* :guilabel:`Fontwork` ツールバー
* |FormattingToolbar|
* 右クリックメニュー

詳しくは |Guide| を見ろ。

Generating a QR or Barcode
======================================================================

QR コード生成機能とバーコード生成機能は、任意の文字列や URL をそれぞれの形式に符
号化し、画像を出力するもので、これをスプレッドシートに含めることが可能だ。

:menuselection:`&Insert-->&OLE Object-->QR and &Barcode...` コマンドで開くダイア
ログは、入力文字列からコード画像を生成して現在のシートに出力する。
:guilabel:`&URL/Text` 欄に入力し、:guilabel:`Error correction` 係数を選択し、境
界線の太さをドット単位で入力し、|OK| を押せ。

生成された後、その画像上で右クリックメニューから :menuselection:`&Edit
Barcode...` を実行すれば編集可能。
