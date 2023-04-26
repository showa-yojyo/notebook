======================================================================
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
