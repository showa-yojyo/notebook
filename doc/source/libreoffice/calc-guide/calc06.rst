======================================================================
Calc Guide Chapter 6 Using Images and Graphics ノート
======================================================================

.. include:: ./calc-inc.txt

.. contents:: 章見出し
   :local:

Introduction
======================================================================

Calc で読み込める形式の一覧は LibreOffice ヘルプから確認しろ。

次の一節はだいじなのでそのままコピーしておく：

   In LibreOffice, the terms *graphics* and *images* refer to both pictures and
   drawing objects. Often the word images is used when referring to pictures and
   other graphics that are not drawing objects.

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

:kbd:`Ctrl` + :kbd:`Shift` を押しながらドラッグすると、埋め込みではなくリンクに
なる。

Insert Image dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. スプレッドシート上、画像を示す位置をクリックする
#. メインメニュー :menuselection:`&Insert --> &Image...` を実行する
#. ダイアログボックス上、挿入するファイルに移動して選択する
#. 埋め込みかリンクかを :guilabel:`Link` チェックボックスで指定する
#. ドロップダウンリストから固定基準を選択する

これで開くボタンを押すと画像ファイルの内容が指定したセルなどに描かれる。

Linking or embedding an image file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

画像をスプレッドシートに埋め込むと、その画像はスプレッドシートファイルの永続的な
部分となる。埋め込んだ画像に加えた変更は元画像ファイルに影響しない。

画像ファイルへのリンクの場合、画像はスプレッドシートに描画されるが、文書を保存す
ると、画像そのものではなく、画像ファイルへの参照だけを保存する。

リンクと埋め込みの長所短所比較は、シンボリックリンクとハードリンクのそれととても
似ている。

リンクを多用する場合にはメインメニュー :menuselection:`&Edit --> Lin&ks to
External Files...` コマンドが重要だ。参照を差し替えたり、埋め込みに変えたりする
ことが可能だ。

Embedding linked images
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

リンクはいつでも埋め込みに変えることが可能。手順：

#. メニューから :menuselection:`&Edit --> Links to External Files...` を実行して
   ダイアログボックスを開く
#. 目的の画像項目を一覧から選択
#. ボタン :guilabel:`&Break Link` を押す

逆に、埋め込みからリンクに変換するのは面倒だ。

Inserting an image from the clipboard
----------------------------------------------------------------------

システムクリップボードの内容が画像データの場合、:menuselection:`&Edit -->
&Paste` コマンド実行 (:kbd:`Ctrl` + :kbd:`V`) でそれを埋め込める。

Inserting an image using a scanner
----------------------------------------------------------------------

スキャナーが PC に接続されている場合、そこから取り込むコマンドがある：

#. :menuselection:`Insert --> &Media --> &Scan --> &Select Source...` を実行
#. スキャナーを選択
#. 画像を挿入する場所にポインターを置く
#. :menuselection:`&Insert --> &Media --> &Scan --> &Request...` を実行

通常はいったん画像ファイルに保存して整形してからそれを上記の方法で追加するのが品
質上望ましい。

Inserting an image from the Gallery
----------------------------------------------------------------------

Gallery は LibreOffice アプリケーションすべてから使用可能だ。

#. :menuselection:`View --> &Gallery` を実行
#. テーマを選択
#. オブジェクトをクリック
#. 文書中にそれをドラッグ＆ドロップするか、右クリックメニューで
   :menuselection:`&Insert` を実行

Modifying images
======================================================================

* Calc で行った画像修正は、埋め込みであれリンクであれ、元画像には影響しない。
* 簡易な修正ならば Calc にある機能を用いてよい。

Using the Image toolbar
----------------------------------------------------------------------

画像を入れたり、既存の画像を選択すると :guilabel:`Formatting` ツールバーの代わり
に :guilabel:`Image` ツールバーが現れる。このツールバーから実行される操作は：

* :guilabel:`Select anchor for object` ドロップダウンリスト
* :guilabel:`Align Objects` ドロップダウンリスト
* 画像の z-order 操作用ボタン

  * :guilabel:`Bring to Front`
  * :guilabel:`Forward One`
  * :guilabel:`Back One`
  * :guilabel:`Send to Back`
  * :guilabel:`To Foreground`
  * :guilabel:`To Background`
* 画像の境界線の属性を設定する

  * :guilabel:`Line Style` ドロップダウンリスト
  * :guilabel:`Line Width` スピンボタン
  * :guilabel:`Line Color` ドロップダウンリスト
* :guilabel:`Area Style` ドロップダウンリスト。画像を含む背景領域の色でない何か
  の属性を設定する。
* :guilabel:`Filling` ドロップダウンリスト。画像を含む背景領域の色を設定する。
* :guilabel:`Shadow` ボタン。画像周囲に影を描く（調整機能は別のコマンドで）。
* :guilabel:`Filter` ドロップダウンリスト。:guilabel:`Image Filter` ツールバーを
  開く。
* :guilabel:`Image Mode` ドロップダウンリスト。次から選ぶ：

  * :guilabel:`Default`
  * :guilabel:`Grayscale`
  * :guilabel:`White/Black`
  * :guilabel:`Watermark`
* :guilabel:`Crop Image` ボタン。切り抜きハンドルを操作する。
* 反転

  * :guilabel:`Flip Horizontally` ボタン
  * :guilabel:`Flip Vertically` ボタン
* :guilabel:`Rotate` ボタン。回転ハンドルを操作する。
* :guilabel:`Transparency` スピンボタン。透明度を設定する。
* :guilabel:`Color` ボタン。:guilabel:`Color` ツールバーを開く。色調整用。

Using the Properties deck in the Sidebar
----------------------------------------------------------------------

:guilabel:`Image` ツールバーの設定の一部は、画像選択中に Sidebar の
:guilabel:`Properties` デッキでも利用可能だ。

Adding text
----------------------------------------------------------------------

画像や図面オブジェクトにテキストを追加可能。そのようなテキストは画像が再配置され
るときに画像と一緒に移動する。

#. 画像をダブルクリックする。:guilabel:`Text Formatting` ツールバーが開く。
#. テキストをタイプし、このツールバーを用いて書式を与える。

このようなテキストを調整するには、画像右クリックメニューから
:menuselection:`&Text...` を実行する。ダイアログボックスが開く。ここで調整しろ。

Positioning, resizing, and arranging images
======================================================================

Using the mouse
----------------------------------------------------------------------

画像の幾何を修正するには、他の描画ソフトの感覚でマウスを用いればいい。キーボード
を併用する編集動作もある。

* 画像の元の比率を維持するには、コーナーハンドルのいずれかをドラッグしろ。
* 比率を変更したい場合は :kbd:`Shift` を押しながらコーナーハンドルのいずれかをド
  ラッグしろ。

Using the Position and Size dialog
----------------------------------------------------------------------

数値的に制御したいならば右クリックメニューから :menuselection:`Position and
Si&ze...` を実行してダイアログから場所や寸法を指示する。座標単位系は設定ダイアロ
グによる。

位置と寸法の既定の基点はスプレッドシートの左上隅だ。この基点を一時的に変更して、
位置決めや寸法記入を簡単にすることが可能。この変更は一度きりで、ダイアログボック
スを閉じると、基点は標準の左上隅の位置にリセットされる。

Arranging images
----------------------------------------------------------------------

スプレッドシートに配置する各画像の z-order を変更するには右クリックメニュー
:menuselection:`A&rrange -->` 各種コマンドを使え。

Anchoring images
----------------------------------------------------------------------

画像を留まらせ、他の項目との位置関係を保て。錨一覧：

To Page
   画像をページに留まらせ、特定の場所に配置する。
To Cell
   画像をセルに留まらせ、固定されている内容と共に表示される。例えば画像がセル
   B10 に留まらせている場合、新しい行がすぐ上に挿入されたとする。このとき、画像は
   B11 に留まらせ直す。
To Cell (resize with cell)
   錨セルの寸法を変更すると、画像のそれも変更される。

選択した画像を留まらせたり、使用する錨の種類を変更するには右クリックメニュー
:menuselection:`Anc&hor -->` 各種コマンドを使え。

画像をセルの寸法に変更するには、画像右クリックメニューから :menuselection:`&Fit
to Cell Size` を実行しろ。

Aligning images
----------------------------------------------------------------------

ワークシートに画像が複数ある場合、これらを整列させて体裁を整えることが可能だ。

選択肢には、画像を水平に揃えるもの（左、中央、右）と、画像を垂直に揃える（上、中
央、下）ものがある。手順は：

#. 対象画像を :kbd:`Shift` を押しながらクリックするなどして同時に選択する。
#. 右クリックメニュー :menuselection:`Alig&n Objects -->` のいずれかのコマンドを
   実行する。

Grouping and ungrouping images
----------------------------------------------------------------------

画像グループの考え方は Inkscape などと同じだ。次の関連コマンドがメニュー
:menuselection:`F&ormat --> &Group` にある：

* :menuselection:`&Group`, :menuselection:`&Ungroup`
* :menuselection:`&Enter Group`, :menuselection:`E&xit Group`

Using LibreOffice's drawing tools
======================================================================

いわゆる図形ツールだ。

複雑な図面を作成する必要がある場合は、LibreOffice Draw を使用し、それをスプレッ
ドシートに挿入することが推奨される。

Drawing toolbar
----------------------------------------------------------------------

:menuselection:`&View --> &Toolbars --> Dra&wing` で図形ツールバーを表示する。こ
れを使って簡単な図形をシートに挿入することが可能だ。

#. :guilabel:`Drawing` ツールバーのボタンを押す
#. 図面オブジェクトを示したい場所にポインターを移動し、クリック、ドラッグして作
   図する。

押した描画コマンドを取り消すには、次のいずれかの操作をしろ：

* 同じツールバーボタンをもう一度クリックする
* :kbd:`Esc` を押す
* :guilabel:`Drawing` ツールバーの :guilabel:`Select` ボタンを押す

図面オブジェクトの性質を編集するには、次が使える：

* :guilabel:`Drawing Object Properties` ツールバー
* Sidebar 内 :guilabel:`Properties` デッキ
* 右クリックメニューの関連コマンド各種

Setting the properties of drawing objects
----------------------------------------------------------------------

描画前に図面オブジェクトの既定特性を設定することが可能。これらの既定特性は現在の
スプレッドシートにのみ適用され、閉じても保持されない。

#. :guilabel:`Drawing` ツールバーの :guilabel:`Select` ボタンを押す
#. :guilabel:`Drawing Object Properties` ツールバーではボタン等がいくつか active
   になっている。各特性に用いる既定値を設定することが可能だ。

オブジェクトを描画したり、他のオブジェクトとグループ化したりすると、より多くの特
性が active になる。これらはツールバー等の関連 UI に反映される。

Resizing drawing objects
----------------------------------------------------------------------

画像の場合と同様のハンドルによる操作が図面オブジェクトに適用される。

Grouping and ungrouping drawing objects
----------------------------------------------------------------------

画像の場合と同様に図面オブジェクトもグループになり得る。

Additional tools
======================================================================

画像の右クリックメニューにはその他雑多なコマンドがある。

* :menuselection:`A&ssign Macro...` でマクロを図面オブジェクトに仕込める。マクロ
  を学んでからここに戻れ。
* 個人的に注意したいものは :menuselection:`Co&mpress...` だ。埋め込んだ画像デー
  タを圧縮すればファイルサイズが小さくなる。

Using Fontwork
======================================================================

文字列だけからロゴタイプを生成する機能だ。

Creating a Fontwork object
----------------------------------------------------------------------

#. :menuselection:`&View --> &Toolbars --> Fontwor&k` 実行
#. :guilabel:`Insert Fontwork Text` を押す
#. :guilabel:`Fontwork Gallery` から一つ選択し :guilabel:`&OK` を押す

Fontwork テキストを編集するにはオブジェクトをダブルクリックしろ。

Editing a Fontwork object
----------------------------------------------------------------------

Fontwork オブジェクトを選択して次を使え：

* :guilabel:`Fontwork` ツールバー
* :guilabel:`Formatting` ツールバー
* 右クリックメニュー

Generating a QR or Barcode
======================================================================

:menuselection:`&Insert --> &OLE Object --> QR and &Barcode...` コマンドで開くダ
イアログは、入力文字列からコード画像を生成して現在のシートに出力する。

生成された後、その画像上で右クリックメニューから :menuselection:`&Edit
Barcode...` を実行すれば編集可能。
