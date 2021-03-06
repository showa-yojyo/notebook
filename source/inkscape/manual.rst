======================================================================
ヘルプノート
======================================================================
本稿は Inkscape メニューの「ヘルプ＞Inkscape マニュアル（英語）」
を選択するとブラウザーで表示されるドキュメント、
`Inkscape Guide to a Vector Drawing <http://tavmjong.free.fr/INKSCAPE/MANUAL/html/index.php>`_
の読書ノートのつもりだ。

.. contents::

Chapter 1. Quick Start
======================================================================
自分で作ってはみたが、後半に行くほど納得していない。
Google Chrome や Firefox だと SVG ファイルをそのまま閲覧できるようだ。

* https://dl.dropbox.com/u/61006529/inkscape/swedish-flag.svg
* https://dl.dropbox.com/u/61006529/inkscape/eu-flag.svg
* https://dl.dropbox.com/u/61006529/inkscape/fhmc.svg
* https://dl.dropbox.com/u/61006529/inkscape/northern-pacific-railway.svg
* https://dl.dropbox.com/u/61006529/inkscape/isometric.svg
* https://dl.dropbox.com/u/61006529/inkscape/soup.svg
* https://dl.dropbox.com/u/61006529/inkscape/grapevine.svg
* https://dl.dropbox.com/u/61006529/inkscape/button.svg

Chapter 2. Files
======================================================================
体で覚えろ。

Chapter 3. Changing the View
======================================================================
これも体で覚えろ。

Chapter 4. Editing Basics
======================================================================
* Undo: Ctrl+Z or Ctrl+Shift+Y
* Redo: Ctrl+Y or Ctrl+Shift+Z
* History: Chift+Shift+H
* Alt+MLB: Select Under
* Alt+MLB Drag: 紐で選択
* グループのダブルクリックで「グループに入る」
* Layer: Ctrl+Shift+L
* New Layer: Ctrl+Shift+N

Chapter 5. Positioning and Transforming
======================================================================
* Rectangle のスケーリングは特殊。
* 1 inch = 1/12 ft = 2.54 cm = 25.4 mm = 0.0254 m = 6 pc = 72 pt
* bounding box には visual と geometric の二種類がある。
  ストローク幅を考慮に入れたものが後者。
* Rotation center: rotation, skewing
* キーボードによる transformation は覚えておいたほうがよいものがある？

  * 矢印全種
  * .
  * ,
  * [ ]
  * H V

* Ctrl+Shift+M: transform dialog
* Edit > Paste Side 配下のコマンド群
* Guide lines の有効な利用法？
* Grid には直交だけでなく、色々ある？
* Alignment dialog: Ctrl+Shift+A

Chapter 6. Geometric Shapes
======================================================================
* fill と stroke という用語は何で決まったのだろう。
* ショートカットキーを覚える。二通りあるものがある。
  F4 or r: Rectangle のような。
* 3D Boxes 有用？

Chapter 7. Paths
======================================================================
* open/closed/compound
* regular shape を Ctrl+Shift+C するとパス化。
* Bezier 曲線

  * 4 つの点で定義される。数学的に言うと端点と接ベクトル。
  * 通常パスは複数の Bezier 曲線がつながっているもの。

* 鉛筆・ペン・カリグラフィーでパス作成。
* 鉛筆ツール (F6 or p)

  * Shift ドラッグで一時的にスナップ無効化 or 選択パスがあれば、それに追加。
  * Ctrl+L: Simplify
  * Ctrl+MLB: 点を描画。さらに Shift 押しでサイズ倍。

* ペンツール (Shift+F6 or b)

  * click と click-drag を使い分ける。
  * Shift+L, Shift+U がわからん。

* カリグラフィーは後回し。
* ストロークのパス化 (Ctrl+Alt+C)
* パスの編集とノードツールの利用は同義。
* F2 or n
* ノード選択の拡張：マウスホバーマウスホイール or Page Up or Page Down
* Tab で次のノード Shift+Tab で前ノード
* Ctrl+A: 選択パスのノード全選択
* その他諸々

* Insert node: double click or Ctrl+Alt+click
* Ctrl 押しながらクリックドラッグで HV 移動
* Ctrl+Alt 押しドラッグで平行垂線移動

* ハンドル操作

  * Shift 押しドラッグ：両側回転。
  * Ctrl 押しドラッグ：15 度ずつ（デフォルト）回転。
  * Alt 押しドラッグ：回転のみ。大きさは変えない。

* 「選択ノードの変形ハンドルを表示」

* キーボードでノード編集

  * 矢印キーはナッジ。Alt, Shift のコンビで移動量調整。
  * Ctrl+矢印とか無理。
  * 角括弧は回転。

* ノード削除は Del, Back Space, Ctrl+Alt+click のどれでも。
  キーが Insert node と同じなので覚えやすい。

* これらの方はむしろ使わない。

  * Join; Shift+J; ノード連結→間にノード挿入。
  * Break; Shift+B; ノードを取り払い、別の 2 ノードを作成。

* Shift+C; ノードを「折る」
* Shift+S etc.

* ノード専用 Alignment ツール。ノードを等間隔に配列したいときに便利。
* オートスムーズノードは特殊なノード。
  ハンドルの形状が隣接ノードの位置に従って自動で調整が入る。

* Sculpting はよくわからん。
* Offset 4 種。

* Ctrl+K: 複数パスを compound に。
* Shift+R: 逆向き
* Ctrl+L: 冗長ノードの削除。パス簡略化。

Z-order が重要なパス操作

* 例えば appearance は「底」のパスのものを引き継ぐ。
* 「トップが消えてボトムが残る」が原則。
* closed path が演算の対象。
  必要に応じて自動的に closed 形状が評価されて、それが演算に適用される？
* Shape, Text は必要に応じて自動的に Path 化される。
* Cut Path コマンドの結果のみ「肉」がなくなる。

Chapter 8. Live Path Effects (LPEs)
======================================================================
* パスエフェクトエディター (Ctrl+Shift+7) ショートカットが効かない
* サブパス補間等は compound path が対象。あらかじめ 2 パスを Ctrl+K しておく。
* Knot までダラダラ読んだ。
* Pattern Along Path

  * control (skeleton) path
  * skeleton を引き継ぐ →あまりうれしくない
  * pattern は single path でなければならない。

* Ruler: 興味なし
* Sketch: 興味なし
* Spiro: 興味なしだが、G4 連続とか恐ろしい記述が。
* Stitch Subpaths: 興味なし。使い方はわかった。

  * 一部描画が乱れる。

* VonKoch: フラクタル。

Chapter 9. Text
======================================================================
* regular/flowed/linked-flowed の三種類。
* ショートカットは F8 or t
* 文字入力中に Ctrl+U でユニコード入力モード。
* テキストをパス化する場合は、念のため duplicate しておくと吉。
* flowed text の入力方法は、ドラッグで四角形を描いてから。

Selecting Text
----------------------------------------------------------------------
* テキスト入力時のショートカットキーの動きがいつもと異なる。

Editing Text
----------------------------------------------------------------------
* Ctrl+Shift+T: ダイアログ
* Ctrl+Alt+K: スペルチェック

Formatting Text
----------------------------------------------------------------------
* line-height 調整には Ctrl+Alt+< or Ctrl+Alt+>
  * Shift でさらに 10 倍。

* カーニングはカーソル位置で Alt+矢印

* Alt+[ とかどうするの

一度 :file:`preference.xml` の使い方をチェックしたほうがよさそうだ。

Text on a Path
----------------------------------------------------------------------
* パスとテキストを両方選択して Put Path コマンド起動。

Text in a Shape
----------------------------------------------------------------------
* 同様に Alt+W で流し込み。解除は Shift+Alt+W

Chapter 10. Attributes
======================================================================
* Fill は内側、Stroke はパス自身。
* テキストに対しては色は各文字に設定できるが、グラデーションやパターンは全体設定。
* Ctrl+Shift+W でスウォッチダイアログ。縦長だと使いづらい。

Fill and Stroke Paint
----------------------------------------------------------------------
* Inkscape の色は RGBA で表現。各成分は 8 ビットの情報量。
* HSV のことを HSL と呼んでいる。
* スウォッチ

  * LB クリックで選択要素の Fill 色変更
  * Shift+LB クリックで選択要素の Stroke 色変更
  * マウスジェスチャーで落ちる。

* スタイルインジケーター

  * MB クリックで色を None にする。もう一回クリックで黒。

* スポイトツールのことを Dropper Tool と呼ぶ。

  * F7 or d で起動。
  * opacity との絡みもあって、わかりにくい？

* Gradient Tool

  * Ctrl+F1 or g で起動。
  * Stop 挿入 Ctrl+Alt+LB クリック
  * Ctrl+L で冗長なノードを消すらしい。
  * Shift+R で逆転。

* Pattern

  * 備え付けのパターンには実はライセンスがある。
  * patterns/patterns.svg に定義がある？
  * パターンを用意する、パターンを割り当てる、パターンの位置等を調整する、の三段階。
  * パターンを定義するには、適当なオブジェクトを選択して Alt+I で OK
  * Shift+Alt+I: Pattern to Objects
  * パターンの変形がわかりにくい。
  * ハッチングはパターン機能を応用して実現する。

* Fill Rule (even-odd rule) は押さえておいたほうがよい。

Stroke Style
----------------------------------------------------------------------
* Join: miter/round/bevel
* Cap: butt/round/square; ストローク両端だけでなく、ダッシュ各線分にも影響する。
* Marker

  * Object to Marker コマンドがある。
  * マーカーはストローク色を引き継がない。エクステンションで逃れられるらしい。
  * マーカーのサイズはストローク幅に影響される。SVG 直編集。
  * 線を同一位置に複製して、複雑なマーカー線を描ける。

Chapter 11. Tweak Tool
======================================================================
* 要素選択後、W or Shift+F2 で起動。
* 微調整できるモードが色々ある。

Tweaking Paths
----------------------------------------------------------------------
* テキストをパス化したものや、ハッチングに対して適用すると効果的。

Tweaking Colors
----------------------------------------------------------------------
* 偶然に頼って面白い色ができることもある。

Chapter 12. Spray Tool
======================================================================
* モードが 3 つある。copy, clone, single path
* copy mode は Tweak tool と組み合わせて使うと便利。
* clone mode は文字通り。copy mode よりも描画がかなり少ない。
* single path mode はオブジェクトが一体化する。CPU に負荷がかかる。
* 選択後 a or Shift+F3 で起動。

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
* Shift+F7
* Fill カラーが参照される。
* 実は閉領域の定義は各種閾値から決まる。
* Ctrl キーを押しながらクリック→バケツが違うところに適用。

Filling Fidelity
----------------------------------------------------------------------
* ビューのズーム具合によって、バケツの塗り部分の忠実度が異なる。

Filling Multiple Regions
----------------------------------------------------------------------
* Alt キーを押しながらドラッグ→ヒモ選択された領域群がバケツ塗り。

Closing Gaps
----------------------------------------------------------------------
* 破線で囲まれたような形状もバケツ塗りできるオプションがある。

Adding to a Fill
----------------------------------------------------------------------
* アルゴリズムの都合上「塗り漏れ」がスクリーン外に生じることがある。
* その場合は Shift+クリックで、バケツ塗り領域を「追加」できる。

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
* Filter Effects Region: ``-0.1:1.1``

Filter Effects Dialog
----------------------------------------------------------------------
* 新規とエフェクト追加がややこしい。

Mini Tutorial - A Drop Shadow
----------------------------------------------------------------------
https://dl.dropbox.com/u/61006529/inkscape/dropshadow.svg

* Source が変更された場合、自動的にドロップシャドウも更新がかかる。
* テキストに対して compound filter を作成することになる。
* Gaussian blur, Offset, Merge の 3 つを使う。矢印の設定に注意。

Color Filter Primitives
----------------------------------------------------------------------
* RGBA 値の行列による変換と考えてよい。OpenGL のアレっぽい。

Compositing Filter Primitives
----------------------------------------------------------------------
* ``enable-background`` タグの扱いにバグがあるらしい。
* SVG 1.1 の仕様にもバグがあって、とにかく background 周りは不安定。
  1.2 で修正された。

* Blend

  * Normal, Multiply, Screen, Darken, Lighten の 5 種類。

* Composite

  * Over, In, Out, Atop, Xor, Arithmetic

* Merge: Z-order ベースのマージ。

Fill Filter Primitives
----------------------------------------------------------------------
* Flood: バウンディング塗りつぶし？
* その他は未実装だったり、よくわからなかったり。

Lighting Filters Primitives
----------------------------------------------------------------------
* フォーンシェーディングっぽく絵を描くフィルターらしい。

Pixel Manipulation Filter Primitives
----------------------------------------------------------------------
* Convolve
* Displacement Map
* Gaussian Blur: クリッピングやマスキングと絡める場合は適用順序に注意。
* Morphology
* Offset

Complex Examples
----------------------------------------------------------------------
* NEON の例を試した。
  https://dl.dropbox.com/u/61006529/inkscape/neon.svg

Chapter 18. XML Editor
======================================================================
Basic Usage
----------------------------------------------------------------------
* Ctrl+Shift+X で起動できる。
* Set ボタン押しと Ctrl+Enter が同じ。
* 属性 http://www.w3.org/TR/SVG/ に仕様がある。

Examples
----------------------------------------------------------------------
* マーカーに色を与える例があるが、普通はエクステンションで達成する。
* Inkscape はテキストの下線装飾 ``text-decoration: underline`` を実装していない。

Chapter 19. Tiling
======================================================================
* クローンの応用である。
* 編集コマンドのクローンのサブメニューになっている。

Symmetry Tab
----------------------------------------------------------------------
* タイリングのメイン設定である。
* 全 17 タイプ。
* bounding box には geometric のほうを考慮される。

Shift Tab
----------------------------------------------------------------------
* タイルのズレを設定する。
* 六角形をタイルするには (50%, -25%) とすればよい。

Color Tab
----------------------------------------------------------------------
* Fill, Stroke は両方共に unset としておく。

Trace
----------------------------------------------------------------------
これは理解できない。

Tricks
----------------------------------------------------------------------
* オブジェクトを円環状にも渦巻状にも配列することに応用できる。

Chapter 20. Tracing Bitmaps
======================================================================
* やはり使うのが難しいと書いてある。
* Shift+Alt+B で起動。

Single Scans
----------------------------------------------------------------------
* 白黒画像をシングルスキャンする利用例。
* Brightness の閾値を大きくすると、黒みが増える。
* Edge Detection は逆に線が少なくなる。
* Color Quantization: よくわからん。エッジ系。

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
* Ctrl+F2 or o
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
* Restack: オブジェクトの Z-order をその位置に基づいて変える。

Color
----------------------------------------------------------------------
* 色変更各種。

Generate from Path
----------------------------------------------------------------------
* Pattern Along Path がここにもいる。

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
* Gear があるのはここ。

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
* Ctrl+Shift+P
* 設定内容はフォルダーにある preference.xml に保存される。

Inkscape Configuration Files
----------------------------------------------------------------------
* :file:`templates` サブフォルダーに新テンプレを追加することができる。
* :file:`palettes` サブフォルダーに新スウォッチを追加することができる。
  ファイルフォーマットは Gimp と共通のもの。
* :file:`markers/markers.svg` マーカー追加
* :file:`share/keys/defaults.xml` ショートカットキー。

Chapter 25. Using the Command Line
======================================================================
* Inkscape はコマンドラインでも利用可能。
* PDF も開けるが、最初の 1 ページだけ。
* ``--shell`` でシェルモード（対話操作モード）として起動する。
