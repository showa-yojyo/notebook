======================================================================
Chapter 3. Changing the View
======================================================================

.. contents::

.. admonition:: 利用者ノート

   キーボードだけでビュー操作できると便利な場合が多いので、その観点で有利な操作
   法を覚えたい。

Panning the Canvas
======================================================================

キャンバスへの視点をずらすにはスクロールバーを使うのが自然。スクロールバー自体の
表示を :kbd:`Ctrl` + :kbd:`B` で切り替えられることを覚えておいて損はない。

マウスが使えればホイールで上下移動、:kbd:`Shift` を押しながらだと左右移動。
設定によってはホイールをズーム操作に転用可能だ。

三ボタンマウスならば中クリックドラッグでパン可能。二ボタンマウスならば次のどちら
でもパン可能：

* :kbd:`Shift` と右クリックドラッグ
* :kbd:`Ctrl` と右クリックドラッグ

:kbd:`Ctrl` を押しながら :kbd:`↑` などの矢印キーを押すとその方向にパンする。

Zooming the Canvas
======================================================================

   For many of the options, the zoom changes by a default factor of 1.41 (repeat
   twice to zoom by a factor two).

これは知らなかった。ズーム操作を二操作単位実行すると絵が二倍になると覚えたい。

.. csv-table::
   :delim: #
   :header-rows: 1
   :widths: auto

   操作 # ズーム # 基準位置
   :kbd:`+` # ズームイン # キャンバス中央
   :kbd:`-` # ズームアウト # キャンバス中央
   :kbd:`Ctrl` + 右クリック # ズームイン # マウスカーソル位置
   :kbd:`Shift` + 右クリック # ズームアウト # マウスカーソル位置
   :kbd:`Shift` + 中クリックドラッグ # ズームイン # ラバーバンド選択
   :kbd:`Ctrl` + ホイール # ズーム両方 # マウスカーソル位置

マウスホイールが関係する操作についてはユーザー設定による。

   Zoom section of the Status Bar. This is the best way to select a precise zoom
   level. One can activate the entry box via the keyboard shortcut :kbd:`Alt` +
   :kbd:`Z`.

倍率を自分で入力することも可能だが、むしろこの数値を現在のズーム状態を確認するの
に使える。

あとは :kbd:`F3` で Zoom Tool コマンドを発動できる。マウスカーソルが虫眼鏡になる
のでコマンド入力状態になったことがわかりやすい。キャンバスをクリックするとマウス
カーソル周りにズームが変化する。:kbd:`Shift` を押しながらクリックしたり、
右クリックに変えてみるなどしてズームインとズームアウトを使い分けられる。

メニュー :menuselection:`View --> Zoom` のサブメニューにズームコマンド各種がある。
キーバインドをここで確認してもよい。

:kbd:`Z` 押しでズームツールバーの表示が切り替わるようだ。

   Holding down the :kbd:`Q` key (Q for quick) will temporarily zoom in on
   selected items making it easier to make a small tweak. Releasing the key
   restores the previous zoom.

押しっぱなしにしている間だけ対象をズームインする。見栄えを確認するのに有用だ。

Rotating the Canvas
======================================================================

本書では何も述べられていないので、勝手に書かせてもらう。

:menuselection:`View --> Orientation` のサブメニューに回転系のコマンドが用意され
ているのが確認できる。これらを述べるべきだろう。少し触った限りでわかったことしか
記さないことにする。

.. csv-table::
   :delim: #
   :header-rows: 1
   :widths: auto

   コマンド # 操作
   :menuselection:`Rotate Clockwise` # キャンバスを右回りに 15 度回転する
   :menuselection:`Rotate Counter-Clockwise` # キャンバスを左回りに 15 度回転する
   :menuselection:`Reset Rotation` # キャンバスの回転をクリアする
   :menuselection:`Lock Rotation` # これが意味不明

回転角はおそらくユーザー設定で変更可能と考えられる。

さらにステータスバーには、ズーム倍率欄の隣に、現在のキャンバス回転角度を表示、編
集可能な欄がある。

.. admonition:: 利用者ノート

   いずれにせよ利用しない。

Flipping the Canvas
======================================================================

こちらも勝手に書かせてもらう。:menuselection:`View --> Orientation` のサブメ
ニューに反転系のコマンドが用意されている。

.. csv-table::
   :delim: #
   :header-rows: 1
   :widths: auto

   コマンド # 操作
   :menuselection:`Flip Horizontally` # キャンバス全体を水平に反転する
   :menuselection:`Flip Vertically` # キャンバス全体を垂直に反転する
   :menuselection:`Reset Flipping` # キャンバスの反転状態をクリアする

Miscellaneous View Commands
======================================================================

Hide/Show
----------------------------------------------------------------------

:menuselection:`View --> Hide/Show` のサブメニューに、各ツールバーの表示状態を切
り替えるコマンドがある。

:kbd:`Shift` + :kbd:`F11` ではそれらを一気に切り替える。メインメニューバーすら対
象に含まれる。

Hide/Show Dialogs
----------------------------------------------------------------------

   Inkscape dialogs can be hidden and unhidden with the :menuselection:`View -->
   Show/Hide Dialogs` command.

画面右側にかなりのスペースを占めているパネル全体を一気に切り替えられるのでたいへ
ん有用だ。キーバインドは :kbd:`F12` なので、他アプリケーションのフルスクリーンと
紛らわしい。

Outline Mode
----------------------------------------------------------------------

   Inkscape has an *Outline* or *Wire-frame* mode. In this mode, all paths and
   shapes are drawn as outlines with a one screen-pixel-wide stroke and no fill,
   regardless of zoom level. Text is drawn with an inverse fill and no stroke.
   Images are outlined in red, clip paths in green, and masks in blue.

   The *Outline* mode is useful for seeing the overall structure of a drawing,
   precise node editing, and for finding and selecting those pesky, hidden
   objects that may have been created by accident. The mode is marginally faster
   than the normal mode.

高速描画愛好者でなくてもこのモードはありがたい。描画モードは次の五つある：

* :menuselection:`Normal`
* :menuselection:`Outline`
* :menuselection:`No Filters`
* :menuselection:`Visible Hairlines`
* :menuselection:`Outline Overlay`

:menuselection:`View --> Display Mode --> Cycle` または :kbd:`Ctrl` + :kbd:`Num5`
でこの五つの描画モードを巡回するように切り替える。
:menuselection:`View --> Display Mode --> Toggle` または :kbd:`Ctrl` +
:kbd:`Num5` で通常モードとそれ以外の四つの描画モードで前回適用したものを切り替え
る。

No Filters Mode
----------------------------------------------------------------------

   Inkscape also has an *No Filters* mode where the rendering of *Filters* is
   turned off. This is useful for working on complicated drawings where the use
   of *Filters* causes the rendering to be too slow.

とあるのだが、キャンバス回転と絡めるとぼかしが無効にならないのを確認してしまった。
再描画が不適切であるように感じられる。

Full Screen Mode
----------------------------------------------------------------------

:kbd:`F11` で全画面モードと元画面モードを切り替える。

前述した :kbd:`Shift` + :kbd:`F11` や :kbd:`F12` と複合させてキャンバスにさらに
注目することができる。

Switch Windows
----------------------------------------------------------------------

:menuselection:`View --> Next Window` および :menuselection:`View --> Previous
Window` は Inkscape ウィンドウが複数あるときに機能する。タブブラウザーにおけるタ
ブのような感覚で使うコマンドだ。

Duplicate Window
----------------------------------------------------------------------

同じ文書を複数のウィンドウで確認したいときに用いるコマンド。

Icon Preview
----------------------------------------------------------------------

Inkscape でアイコンイメージを設計するときに多用されるコマンド。
