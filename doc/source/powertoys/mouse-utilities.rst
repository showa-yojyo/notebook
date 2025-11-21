======================================================================
Mouse utilities 利用ノート
======================================================================

最初の二つの機能が有用だ。画面をビデオキャプチャーするときに意識するといい。部分
機能ごとに :guilabel:`Appearance & behavior` 設定画面が用意されている。

.. attention::

   :doc:`./index` 冒頭の前提条件に留意すること。

.. contents:: 見出し一覧
   :local:

Find My Mouse
======================================================================

マウスポインターが迷子になったときに、目立つ視覚効果でその位置を示すものというも
のだ。

設定項目 :guilabel:`Enable Find My Mouse` を On にすることで、この機能が有効とな
る。

マウスカーソルを揺さ振るか、左 :kbd:`Ctrl` を二度押すかのどちらかの操作で、マウ
スカーソルの位置をハイライトする。

マウスをクリックするか、何かキーを押すとスポットライトが消灯する。点灯中にマウス
を動かし、止めた直後にスポットライトは消灯する。

設定
----------------------------------------------------------------------

:guilabel:`Activation method`
   視覚効果を発動するための使用者の行動をどれにするかを指定する。

   * :guilabel:`Press Left Control twice`
   * :guilabel:`Press Right Control twice`
   * :guilabel:`Shake mouse`: タッチパッド使用時のときにややこしいことになるから
     これを選ぶのは避ける。
   * :guilabel:`Custom shortcut`: これを選ぶと :guilabel:`Actiqvation shortcut`
     を指定可能になる。

   二つオプションがある：

   :guilabel:`Only activate while holding the Windows key`
      Off でいい。
   :guilabel:`Do not activate when Game Mode is on`
      On に変えてよい。
:guilabel:`Appearance & behavior`
   カスタマイズ構成は次のとおり：

   :guilabel:`Background color`
      オーバーレイの遮光度。下記背景色に適用するアルファブレンド用の値。
   :guilabel:`Spotlight color`
      マウスカーソルを中心とする円の外側の色。白のままでいい。
   :guilabel:`Spotlight radius (px)`
      マウスカーソルを中心とする円の半径。
   :guilabel:`Spotlight initial zoom`
      ズームアニメーション開始時におけるスポットライトズーム係数。値が大きいほ
      ど、スポットライトがカーソル位置に近づくにつれて、アニメーションがより大げ
      さになる。
   :guilabel:`Animation duration (ms)`
      スポットアニメーションの尺。スポットライトが現れるまでの時間。
:guilabel:`Excluded apps`
   :doc:`./always-on-top` の同名設定項目と同様。

.. admonition:: 利用者ノート

   Dungeon Master RTC など、マウスの扱いが特殊なプログラムに適用することが考えら
   れる。

Mouse Highlighter
======================================================================

Mouse Highlighter はマウスクリック（左右どちらか）時にカーソル近傍を丸く強調表示
する機能だ。

1. :guilabel:`Enable Mouse Highlighter` を On にすることで、この機能が有効となる。
2. マウス操作中に :guilabel:`Activation shortcut` で指定されているショートカット
   キーを押すことでハイライトをするか否かを決める。初期設定ショートカットキーは
   :kbd:`Win` + :kbd:`Shift` + :kbd:`H` だ。

設定
----------------------------------------------------------------------

:guilabel:`Activation shortcut`
   上述のキーバインドを変更することが可能だ。

   :guilabel:`Automatically activate on utility startup`
      On にするとキーを押さずに当機能が有効になる。
:guilabel:`Appearance & behavior`
   カスタマイズ構成は次のとおり：

   :guilabel:`Primary button highlight color`
      左ボタンに対する強調色
   :guilabel:`Secondary button highlight color`
      右ボタンに対する強調色
   :guilabel:`Always highlight color`
      ???
   :guilabel:`Highlight mode`
      どのように強調するかを指定する：

      * :guilabel:`Spotlight`
      * :guilabel:`Circle highlight`
   :guilabel:`Radius (px)`
      強調円の半径
   :guilabel:`Fade delay (ms)`
      強調が消滅し始めるまでの時間
   :guilabel:`Fade duration (ms)`
      消滅アニメーションの尺

Mouse Jump
======================================================================

Mouse Jump 機能は使わない。割愛。

Mouse Pointer Crosshairs
======================================================================

画面全体にマウスポインターを中心とした十字線を引く機能だ。

1. 設定画面で :guilabel:`Enable Mouse Pointer Crosshairs` をオンにする。
2. 既定ではキーバインド :kbd:`Win` + :kbd:`Alt` + :kbd:`P` で十字線を出したり消
   したりする。

設定
----------------------------------------------------------------------

:guilabel:`Activation shortcut`
   上述のキーバインドを変更することが可能だ。

   :guilabel:`Automatically activate on utility startup`
      On にするとキーを押さずに当機能が有効になる。
:guilabel:`Appearance & behavior`
   十字線の各線は実は矩形であり、縁と内部それぞれに外見仕様を指定する構成だ。カ
   スタマイズ構成は次のとおり：

   :guilabel:`Crosshairs color`
      十字線の色。
   :guilabel:`Crosshairs opacity (%)`
      十字線のアルファブレンドの値。
   :guilabel:`Crosshairs center radius (px)`
      十字線の交点を中心とするこの半径以内には線が引かれない。
   :guilabel:`Crosshairs thickness (px)`
      十字線の幅（厚み）。
   :guilabel:`Crosshairs border color`, :guilabel:`Crosshairs border size (px)`
      先述を見ろ。
   :guilabel:`Crosshairs orientation`
      十字線を縦線のみまたは横線のみにすることも可能だ：
   :guilabel:`Fix crosshairs length`
      On にすると十字線の長さが画面寸法ではなく、次の項目で指定する値固定になる。

      :guilabel:`Crosshairs fixed length (px)`
         十字線の長さ。
:guilabel:`Gliding cursor`
   キーバインド :kbd:`Win` + :kbd:`Alt` + :kbd:`.` でこのモードにおける「スイッ
   チ」となる。次の順序で動作を切り替える：

   #. 画面に十字線が現れ、垂直軸が水平方向右に移動する。画面端に至ると左端にワー
      プする。
   #. 速度が著しく落ちる。
   #. 今度は水平軸が垂直方向下に移動する。画面端に至ると上端にワープする。
   #. 速度が著しく落ちる。
   #. その座標でのクリックイベントが確定して十字線が消える。

   :guilabel:`Initial line speed`
      上述の記述における初速。著しく落ちるまでの軸の速度。
   :guilabel:`Reduced line speed`
      上述の記述において、著しく落ちたときの軸の速度。

.. 以上
