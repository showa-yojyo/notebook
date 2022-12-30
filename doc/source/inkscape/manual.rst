======================================================================
ヘルプノート
======================================================================

本稿は Inkscape メニューの :menuselection:`ヘルプ --> Inkscape マニュアル（英語）`
を選択するとブラウザーで表示されるドキュメント、
`Inkscape Guide to a Vector Drawing <http://tavmjong.free.fr/INKSCAPE/MANUAL/html/index.php>`_
の読書ノートのつもりだ。

.. contents::

Chapter 1. Quick Start
======================================================================

自分で作ってはみたが、後半に行くほど納得していない。
Google Chrome や Firefox だと SVG ファイルをそのまま閲覧できるようだ。

* <https://dl.dropbox.com/u/61006529/inkscape/swedish-flag.svg>
* <https://dl.dropbox.com/u/61006529/inkscape/eu-flag.svg>
* <https://dl.dropbox.com/u/61006529/inkscape/fhmc.svg>
* <https://dl.dropbox.com/u/61006529/inkscape/northern-pacific-railway.svg>
* <https://dl.dropbox.com/u/61006529/inkscape/isometric.svg>
* <https://dl.dropbox.com/u/61006529/inkscape/soup.svg>
* <https://dl.dropbox.com/u/61006529/inkscape/grapevine.svg>
* <https://dl.dropbox.com/u/61006529/inkscape/button.svg>

Chapter 2. Files
======================================================================

体で覚えろ。

Chapter 3. Changing the View
======================================================================

これも体で覚えろ。

Chapter 4. Editing Basics
======================================================================

* :guilabel:`Undo`: :kbd:`Ctrl` + :kbd:`Z` or :kbd:`Ctrl` + :kbd:`Shift` +
  :kbd:`Y`
* :guilabel:`Redo`: :kbd:`Ctrl` + :kbd:`Y` or :kbd:`Ctrl` + :kbd:`Shift` +
  :kbd:`Z`
* :guilabel:`History`: :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`H`
* :kbd:`Alt` + MLB: :guilabel:`Select Under`
* :kbd:`Alt` + MLB Drag: 紐で選択
* グループのダブルクリックで「グループに入る」
* :guilabel:`Layer`: :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`L`
* :guilabel:`New Layer`: :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`N`

Chapter 5. Positioning and Transforming
======================================================================

* :guilabel:`Rectangle` のスケーリングは特殊。
* 1 inch = 1/12 ft = 2.54 cm = 25.4 mm = 0.0254 m = 6 pc = 72 pt
* bounding box には visual と geometric の二種類がある。
  ストローク幅を考慮に入れたものが後者。
* :guilabel:`Rotation center`: rotation, skewing
* キーボードによる transformation は覚えておいたほうがよいものがある？

  * 矢印全種
  * :kbd:`.`
  * :kbd:`,`
  * :kbd:`[`, :kbd:`]`
  * :kbd:`H`, :kbd:`V`

* :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`M`: transform dialog
* :menuselection:`Edit --> Paste` :guilabel:`Side` 配下のコマンド群
* :guilabel:`Guide` lines の有効な利用法？
* :guilabel:`Grid` には直交だけでなく、色々ある？
* :guilabel:`Alignment` dialog: :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`A`

Chapter 6. Geometric Shapes
======================================================================

* fill と stroke という用語は何で決まったのだろう。
* ショートカットキーを覚える。二通りあるものがある。
  :kbd:`F4` or :kbd:`R`: :guilabel:`Rectangle` のような。
* 3D Boxes 有用？

Chapter 7. Paths
======================================================================

* open/closed/compound
* regular shape を :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`C` するとパス化。
* Bezier 曲線

  * 4 つの点で定義される。数学的に言うと端点と接ベクトル。
  * 通常パスは複数の Bezier 曲線がつながっているもの。

* 鉛筆・ペン・カリグラフィーでパス作成。
* 鉛筆ツール (:kbd:`F6` or :kbd:`P`)

  * :kbd:`Shift`: ドラッグで一時的にスナップ無効化 or 選択パスがあれば、それに追
    加。
  * :kbd:`Ctrl` + :kbd:`L`: :guilabel:`Simplify`
  * :kbd:`Ctrl` + MLB: 点を描画。さらに :kbd:`Shift` 押しでサイズ倍。

* ペンツール (:kbd:`Shift` + :kbd:`F6` or :kbd:`B`)

  * click と click-drag を使い分ける。
  * :kbd:`Shift` + :kbd:`L`, :kbd:`Shift` + :kbd:`U` がわからん。

* カリグラフィーは後回し。
* ストロークのパス化 (:kbd:`Ctrl` + :kbd:`Alt` + :kbd:`C`)
* パスの編集とノードツールの利用は同義。
* :kbd:`F2` or :kbd:`N`
* ノード選択の拡張：マウスホバーマウスホイール or :kbd:`Page Up` or :kbd:`Page Down`
* :kbd:`Tab` で次のノード :kbd:`Shift` + :kbd:`Tab` で前ノード
* :kbd:`Ctrl` + :kbd:`A`: 選択パスのノード全選択
* その他諸々

* :guilabel:`Insert node`: double click or :kbd:`Ctrl` + :kbd:`Alt` + click
* :kbd:`Ctrl` 押しながらクリックドラッグで HV 移動
* :kbd:`Ctrl` + :kbd:`Alt` 押しドラッグで平行垂線移動

* ハンドル操作

  * :kbd:`Shift` 押しドラッグ：両側回転。
  * :kbd:`Ctrl` 押しドラッグ：15 度ずつ（デフォルト）回転。
  * :kbd:`Alt` 押しドラッグ：回転のみ。大きさは変えない。

* 「選択ノードの変形ハンドルを表示」
* キーボードでノード編集

  * 矢印キーはナッジ。:kbd:`Alt`, :kbd:`Shift` のコンビで移動量調整。
  * :kbd:`Ctrl` + 矢印とか無理。
  * 角括弧は回転。

* ノード削除は :kbd:`Del`, :kbd:`BackSpace`, :kbd:`Ctrl` + :kbd:`Alt` + click
  のどれでも。キーが :guilabel:`Insert node` と同じなので覚えやすい。

* これらの方はむしろ使わない。

  * :guilabel:`Join`; :kbd:`Shift` + :kbd:`J`; ノード連結→間にノード挿入。
  * :guilabel:`Break`: :kbd:`Shift` + :kbd:`B`; ノードを取り払い、別の 2 ノード
    を作成。

* :kbd:`Shift` + :kbd:`C`; ノードを「折る」
* :kbd:`Shift` + :kbd:`S` etc.

* ノード専用 :guilabel:`Alignment` ツール。ノードを等間隔に配列したいときに便
  利。
* オートスムーズノードは特殊なノード。ハンドルの形状が隣接ノードの位置に従って自
  動で調整が入る。

* :guilabel:`Sculpting` はよくわからん。
* :guilabel:`Offset` 4 種。

* :kbd:`Ctrl` + :kbd:`K`: 複数パスを compound に。
* :kbd:`Shift` + :kbd:`R`: 逆向き
* :kbd:`Ctrl` + :kbd:`L`: 冗長ノードの削除。パス簡略化。

Z-order が重要なパス操作

* 例えば appearance は「底」のパスのものを引き継ぐ。
* 「トップが消えてボトムが残る」が原則。
* closed path が演算の対象。
  必要に応じて自動的に closed 形状が評価されて、それが演算に適用される？
* Shape, Text は必要に応じて自動的に Path 化される。
* :guilabel:`Cut Path` コマンドの結果のみ「肉」がなくなる。

Chapter 8. Live Path Effects (LPEs)
======================================================================

* パスエフェクトエディター (:kbd:`Ctrl` + :kbd:`Shift` + :kbd:`7`) ショートカッ
  トが効かない
* サブパス補間等は compound path が対象。あらかじめ 2 パスを :kbd:`Ctrl` +
  :kbd:`K` しておく。
* :guilabel:`Knot` までダラダラ読んだ。
* :guilabel:`Pattern Along Path`

  * control (skeleton) path
  * skeleton を引き継ぐ →あまりうれしくない
  * pattern は single path でなければならない。

* :guilabel:`Ruler`: 興味なし
* :guilabel:`Sketch`: 興味なし
* :guilabel:`Spiro`: 興味なしだが、G4 連続とか恐ろしい記述が。
* :guilabel:`Stitch Subpaths`: 興味なし。使い方はわかった。

  * 一部描画が乱れる。

* :guilabel:`VonKoch`: フラクタル。

Chapter 9. Text
======================================================================

* regular/flowed/linked-flowed の三種類。
* ショートカットは :kbd:`F8` or :kbd:`T`.
* 文字入力中に :kbd:`Ctrl` + :kbd:`U` で Unicode 入力モード。
* テキストをパス化する場合は、念のため duplicate しておくと吉。
* flowed text の入力方法は、ドラッグで四角形を描いてから。

Selecting Text
----------------------------------------------------------------------

* テキスト入力時のショートカットキーの動きがいつもと異なる。

Editing Text
----------------------------------------------------------------------

* :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`T`: ダイアログ
* :kbd:`Ctrl` + :kbd:`Alt` + :kbd:`K`: スペルチェック

Formatting Text
----------------------------------------------------------------------

* line-height 調整には :kbd:`Ctrl` + :kbd:`Alt` + :kbd:`<` or :kbd:`Ctrl` +
  :kbd:`Alt` + :kbd:`>`

  * :kbd:`Shift` でさらに 10 倍。

* カーニングはカーソル位置で :kbd:`Alt` + 矢印
* :kbd:`Alt` + :kbd:`[` とかどうするの

一度 :file:`preference.xml` の使い方をチェックしたほうがよさそうだ。

Text on a Path
----------------------------------------------------------------------

* パスとテキストを両方選択して :guilabel:`Put Path` コマンド起動。

Text in a Shape
----------------------------------------------------------------------

* 同様に :kbd:`Alt` + :kbd:`W` で流し込み。解除は :kbd:`Shift` + :kbd:`Alt` +
  :kbd:`W`.

Chapter 10. Attributes
======================================================================

* :guilabel:`Fill` は内側、:guilabel:`Stroke` はパス自身。
* テキストに対しては色は各文字に設定できるが、グラデーションやパターンは全体設
  定。
* :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`W` でスウォッチダイアログ。縦長だと使いづら
  い。

Fill and Stroke Paint
----------------------------------------------------------------------

* Inkscape の色は RGBA で表現。各成分は 8 ビットの情報量。
* HSV のことを HSL と呼んでいる。
* スウォッチ

  * LB クリックで選択要素の :guilabel:`Fill` 色変更
  * :kbd:`Shift` + LB クリックで選択要素の :guilabel:`Stroke` 色変更
  * マウスジェスチャーで落ちる。

* スタイルインジケーター

  * MB クリックで色を :guilabel:`None` にする。もう一回クリックで黒。

* スポイトツールのことを :guilabel:`Dropper Tool` と呼ぶ。

  * :guilabel:`F7` or :guilabel:`D` で起動。
  * opacity との絡みもあって、わかりにくい？

* :guilabel:`Gradient Tool`

  * :kbd:`Ctrl` + :kbd:`F1` or :kbd:`G` で起動。
  * :kbd:`Stop` 挿入 :kbd:`Ctrl` + :kbd:`Alt` + LB クリック
  * :kbd:`Ctrl` + :kbd:`L` で冗長なノードを消すらしい。
  * :kbd:`Shift` + :kbd:`R` で逆転。

* :kbd:`Pattern`

  * 備え付けのパターンには実はライセンスがある。
  * :file:`patterns/patterns.svg` に定義がある？
  * パターンを用意する、パターンを割り当てる、パターンの位置等を調整する、の三段
    階。
  * パターンを定義するには、適当なオブジェクトを選択して :kbd:`Alt` + :kbd:`I`
    で OK.
  * :kbd:`Shift` + :kbd:`Alt` + :kbd:`I`: :guilabel:`Pattern to Objects`
  * パターンの変形がわかりにくい。
  * ハッチングはパターン機能を応用して実現する。

* :guilabel:`Fill Rule` (even-odd rule) は押さえておいたほうがよい。

Stroke Style
----------------------------------------------------------------------

* :guilabel:`Join`: miter/round/bevel
* :guilabel:`Cap`: butt/round/square; ストローク両端だけでなく、ダッシュ各線分に
  も影響する。
* :guilabel:`Marker`

  * :guilabel:`Object to Marker` コマンドがある。
  * マーカーはストローク色を引き継がない。エクステンションで逃れられるらしい。
  * マーカーのサイズはストローク幅に影響される。SVG 直編集。
  * 線を同一位置に複製して、複雑なマーカー線を描ける。

Chapter 11. Tweak Tool
======================================================================

* 要素選択後、:kbd:`W` or :kbd:`Shift` + :kbd:`F2` で起動。
* 微調整できるモードが色々ある。

Tweaking Paths
----------------------------------------------------------------------

* テキストをパス化したものや、ハッチングに対して適用すると効果的。

Tweaking Colors
----------------------------------------------------------------------

* 偶然に頼って面白い色ができることもある。

Chapter 12. Spray Tool
======================================================================

* モードが 3 つある。copy, clone, single path.
* copy mode は :guilabel:`Tweak` tool と組み合わせて使うと便利。
* clone mode は文字通り。copy mode よりも描画がかなり少ない。
* single path mode はオブジェクトが一体化する。CPU に負荷がかかる。
* 選択後 a or :kbd:`Shift` + :kbd:`F3` で起動。

Chapter 13. Eraser Tool
======================================================================

Eraser Touch Mode
----------------------------------------------------------------------

* マウスのドラッグ軌跡上にかぶるオブジェクトを削除する。

Eraser Cut Out Mode
----------------------------------------------------------------------

* マウスのドラッグ軌跡にかぶる部分ををオブジェクトから削る。

Chapter 14. Paint Bucket Tool
======================================================================

閉領域を塗りつぶす機能。

Simple Use
----------------------------------------------------------------------

* :kbd:`Shift` + :kbd:`F7`
* :guilabel:`Fill` カラーが参照される。
* 実は閉領域の定義は各種閾値から決まる。
* :kbd:`Ctrl` キーを押しながらクリック→バケツが違うところに適用。

Filling Fidelity
----------------------------------------------------------------------

* ビューのズーム具合によって、バケツの塗り部分の忠実度が異なる。

Filling Multiple Regions
----------------------------------------------------------------------

* :kbd:`Alt` キーを押しながらドラッグ→ヒモ選択された領域群がバケツ塗り。

Closing Gaps
----------------------------------------------------------------------

* 破線で囲まれたような形状もバケツ塗りできるオプションがある。

Adding to a Fill
----------------------------------------------------------------------

* アルゴリズムの都合上「塗り漏れ」がスクリーン外に生じることがある。
* その場合は :kbd:`Shift` + クリックで、バケツ塗り領域を「追加」できる。

Chapter 15. Clipping and Masking
======================================================================

* クリッピングとマスキングは「オブジェクトのどの部分を見せる」のかという方法だ。
* クリッピングはパスが形状を定義する。
* マスキングは透明度を定義する。

Clipping
----------------------------------------------------------------------

* パス・レギュラーシェイプ・レギュラーテキストがクリッピングパスたり得る。
* オブジェクトまたはグループをクリップできる。
* クリッピングパスはクリップされるオブジェクトの「上」にある必要がある。
* 両者を選択してクリップコマンド発動。

Masking
----------------------------------------------------------------------

* 任意の要素をマスキング要素として使える。
* マスキング要素の opacity がマスクされる側の opacity を決める。
* 次のルールで透明具合色が決まる

  * マスクで黒い部分は完全に透明になる。
  * マスクでアルファ値の弱い部分は完全に透明になる。
  * マスクの外側は完全に透明になる。

* マスク要素がマスクされる側の「上」にある。
* 両者選択でマスク発動。
* マスク解除コマンドもある。

マスクイメージは普通モノクロで十分間に合う。
適用後は被マスク要素の色味がむしろ生き残る。

Chapter 16. Filter Effects - Preset
======================================================================

Use of Preset Filters
----------------------------------------------------------------------

* オブジェクト選択後にメニュー選択で実行。
* フィルターは大別すると、通常オブジェクト用とビットマップ用がある。
* 自作フィルターをメニューに組み込むことができる。
  :file:`~/.config/inkscape/filters`

* 以降のセクション、サンプルイメージのカタログ。

Chapter 17. Filter Effects - Custom
======================================================================

Basic Use
----------------------------------------------------------------------

* ガウスぼかしフィルターはいつもの色ダイアログでも設定できる。
* ブレンドフィルターはレイヤーダイアログでも設定できる。
* フィルター削除はそれ用のメニューがある。
* :guilabel:`Filter Effects Region`: ``-0.1:1.1``

Filter Effects Dialog
----------------------------------------------------------------------

* 新規とエフェクト追加がややこしい。

Mini Tutorial - A Drop Shadow
----------------------------------------------------------------------

<https://dl.dropbox.com/u/61006529/inkscape/dropshadow.svg>

* :guilabel:`Source` が変更された場合、自動的にドロップシャドウも更新がかかる。
* テキストに対して compound filter を作成することになる。
* :guilabel:`Gaussian blur`, :guilabel:`Offset`, :guilabel:`Merge` の 3 つを使
  う。矢印の設定に注意。

Color Filter Primitives
----------------------------------------------------------------------

* RGBA 値の行列による変換と考えてよい。OpenGL のアレっぽい。

Compositing Filter Primitives
----------------------------------------------------------------------

* ``enable-background`` タグの扱いにバグがあるらしい。
* SVG 1.1 の仕様にもバグがあって、とにかく background 周りは不安定。1.2 で修正さ
  れた。

* :guilabel:`Blend`

  * :guilabel:`Normal`, :guilabel:`Multiply`, :guilabel:`Screen`,
    :guilabel:`Darken`, :guilabel:`Lighten` の 5 種類。

* :guilabel:`Composite`

  * :guilabel:`Over`, :guilabel:`In`, :guilabel:`Out`, :guilabel:`Atop`,
    :guilabel:`Xor`, :guilabel:`Arithmetic`

* :guilabel:`Merge`: Z-order ベースのマージ。

Fill Filter Primitives
----------------------------------------------------------------------

* :guilabel:`Flood`: バウンディング塗りつぶし？
* その他は未実装だったり、よくわからなかったり。

Lighting Filters Primitives
----------------------------------------------------------------------

* フォーンシェーディングっぽく絵を描くフィルターらしい。

Pixel Manipulation Filter Primitives
----------------------------------------------------------------------

* :guilabel:`Convolve`
* :guilabel:`Displacement Map`
* :guilabel:`Gaussian Blur`: クリッピングやマスキングと絡める場合は適用順序に注
  意。
* :guilabel:`Morphology`
* :guilabel:`Offset`

Complex Examples
----------------------------------------------------------------------

* NEON の例を試した。<https://dl.dropbox.com/u/61006529/inkscape/neon.svg>

Chapter 18. XML Editor
======================================================================

Basic Usage
----------------------------------------------------------------------

* :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`X` で起動できる。
* :guilabel:`Set` ボタン押しと :kbd:`Ctrl` + :kbd:`Enter` が同じ。
* 属性 <http://www.w3.org/TR/SVG/> に仕様がある。

Examples
----------------------------------------------------------------------

* マーカーに色を与える例があるが、普通はエクステンションで達成する。
* Inkscape はテキストの下線装飾 ``text-decoration: underline`` を実装していない。

Chapter 19. Tiling
======================================================================

* クローンの応用である。
* 編集コマンドのクローンのサブメニューになっている。

:guilabel:`Symmetry` Tab
----------------------------------------------------------------------

* タイリングのメイン設定である。
* 全 17 タイプ。
* bounding box には geometric のほうを考慮される。

:guilabel:`Shift` Tab
----------------------------------------------------------------------

* タイルのズレを設定する。
* 六角形をタイルするには (50%, -25%) とすればよい。

:guilabel:`Color` Tab
----------------------------------------------------------------------

* :guilabel:`Fill`, :guilabel:`Stroke` は両方共に unset としておく。

Trace
----------------------------------------------------------------------

これは理解できない。

Tricks
----------------------------------------------------------------------

* オブジェクトを円環状にも渦巻状にも配列することに応用できる。

Chapter 20. Tracing Bitmaps
======================================================================

* やはり使うのが難しいと書いてある。
* :kbd:`Shift` + :kbd:`Alt` + :kbd:`B` で起動。

Single Scans
----------------------------------------------------------------------

* 白黒画像をシングルスキャンする利用例。
* :guilabel:`Brightness` の閾値を大きくすると、黒みが増える。
* :guilabel:`Edge Detection` は逆に線が少なくなる。
* :guilabel:`Color Quantization`: よくわからん。エッジ系。

Multiple Scans
----------------------------------------------------------------------

手に負えん。

Common Options
----------------------------------------------------------------------

* パスの簡略化をなるべくしたほうがよさそう。

SIOX
----------------------------------------------------------------------

* Simple Interactive Object Extraction
* オブジェクトを背景から切り離す技術。

Chapter 21. Connectors
======================================================================

* バグがあって、オブジェクトを上下にナッジ移動させてもコネクターが追随しない。

Creating Connectors
----------------------------------------------------------------------

* :kbd:`Ctrl` + :kbd:`F2` or :kbd:`O`
* テキストにはコネクターが直には付かない。

Chapter 22. Extensions
======================================================================

* Inkscape の内部で動作するスクリプト (Perl pr Python)
* :file:`share/inkscape/extensions` directory
* :file:`src/extension/internal`
* :file:`extensions-errors.log`
* Live Preview

Arrange
----------------------------------------------------------------------

* :guilabel:`Restack`: オブジェクトの Z-order をその位置に基づいて変える。

Color
----------------------------------------------------------------------

* 色変更各種。

Generate from Path
----------------------------------------------------------------------

* :guilabel:`Pattern Along Path` がここにもいる。

JessyInk (Presentations)
----------------------------------------------------------------------

* Web ブラウザー用のスライドショーを作る機能？

Modify Path
----------------------------------------------------------------------

* ノード追加
* マーカーに色を着ける
* etc.

Raster
----------------------------------------------------------------------

* ビットマップのピクセルを操作する。

Render
----------------------------------------------------------------------

* :guilabel:`Gear` があるのはここ。

Web
----------------------------------------------------------------------

* Web Slicer が明らかに面白そう。

Chapter 24. Customization
======================================================================

* 設定ダイアログを利用する方法と、フォルダーにあるファイルを修正する方法。

  * all users: :file:`share/inkscape`
  * personal changes: :file:`~/.config/inkscape` または
    :file:`%USERPROFILE%\\Application Data\\Inkscape`

Inkscape Preferences Dialog
----------------------------------------------------------------------

* :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`P`
* 設定内容はフォルダーにある :file:`preference.xml` に保存される。

Inkscape Configuration Files
----------------------------------------------------------------------

* :file:`templates` サブフォルダーに新テンプレを追加することができる。
* :file:`palettes` サブフォルダーに新スウォッチを追加することができる。ファイル
  フォーマットは GIMP と共通のもの。
* :file:`markers/markers.svg` マーカー追加
* :file:`share/keys/defaults.xml` ショートカットキー。

Chapter 25. Using the Command Line
======================================================================

* Inkscape はコマンドラインでも利用可能。
* PDF も開けるが、最初の 1 ページだけ。
* ``--shell`` でシェルモード（対話操作モード）として起動する。
