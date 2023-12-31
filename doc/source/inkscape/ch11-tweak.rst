======================================================================
Chapter 11. Tweak Tool
======================================================================

.. contents::

微調整ツールの意義と起動方法を学ぶ：

   The *Tweak Tool* is used to make small changes to objects, paths, and colors.
   While at first objects, paths, and colors may seem to have little to do with
   each other, the use of *Tweak Tool* to edit them is surprisingly very
   similar.

起動方法の例：

* :guilabel:`Toolbox` の津波のようなアイコンのボタンをクリックする。
* :kbd:`Shift` + :kbd:`F2` を押すか、:kbd:`W` を押す。

   The *Tweak Tool* works like a brush that covers a circular part of the
   screen, indicated by an orange circle. The affect of the brush is strongest
   in the center and falls off smoothly till the edge. Two parameters, located
   in the *Tool Controls* affect the “physical” nature of the brush:

Photoshop などのブラシツールの感覚で操作すると読める。ならばパラメーターも同様の
ものがある：

:guilabel:`Width`
   ブラシの寸法。

   * 値は 1 から 100 までが有効で、値 20 が画面画素 100 の半径に対応する。
   * ズーム操作でブラシ寸法を変化できるということになる。
   * :kbd:`←` と :kbd:`→` で値を増減可能。
   * :kbd:`Home` で 1 に設定。
   * :kbd:`End` で 100 に設定。
:guilabel:`Force`
   ブラシの動きが画面上のオブジェクトにどれだけ強く影響するか。

   * 値は 1 から 100 までが有効。
   * :guilabel:`Use the Pressure of the input device to alter...` ボタンが ON に
     なっていると感圧タブレットが効く。
   * :kbd:`↑` で増加。
   * :kbd:`↓` で減少。

:kbd:`Space` キーで選択ツールと往復する手筋に慣れるといい：

   Objects must be selected to be tweaked. Using the :kbd:`Space` Bar is a quick
   way to switch back and forth between the *Select Tool* and the *Tweak Tool*.

ステータスバーでは選択オブジェクトの有無だけが示される：

   Note that there is no onscreen indication of what objects are selected when
   the *Tweak Tool* is in use. If no objects are selected, a message to that
   effect will be displayed in the *Status Bar*.

Tweaking Objects
======================================================================

オブジェクトに対する微調整を見ていく。

   A number of *Tweak Tool* modes modify objects. A typical use would be to
   create an array of cloned objects using the :guilabel:`Create Tiled Clones`
   dialog and then use the *Tweak Tool* to move them around.

整然とした出力に対して微調整ツールの適用を検討しよう。

用意されているモードは次：

:guilabel:`Move objects in any direction`
   ドラッグ方向にオブジェクトを移動する
:guilabel:`Move objects toward cursor; with Shift from cursor`
   オブジェクトをポインターの方に引き寄せたり遠ざけたりする。
:guilabel:`Move objects in random directions`
   オブジェクトをランダムな方向にランダムな量だけ移動する。
:guilabel:`Shrink objects, with Shift enlarge`
   ポインター近傍オブジェクトを拡縮する。
:guilabel:`Rotate objects, with Shift counterclockwise`
   ポインター近傍オブジェクトを回転する。
:guilabel:`Duplicate objects, with Shift delete`
   ポインター近傍オブジェクトをランダムに複製、削除する。

      Duplicates are placed directly over the original so you may not see
      immediately the effect. Switching temporarily to the *Select Tool* via the
      :kbd:`Space` will update the *Status Bar* with the new number of selected
      objects (newly created objects are automatically added to the selection or
      *Group*).

:guilabel:`Blur selected objects more; with Shift, blur less`
   ポインター近傍オブジェクトをぼかしたりくっきりさせたりする。

.. admonition:: 読者ノート

   本書掲載のキーバインドが効くものとそうでないものがある。よって記述を割愛。

Tweaking Paths
======================================================================

パスに対する微調整だから、ノード位置を微調整する機能だと考えられる。しかし、選択
オブジェクトがパス型でなくても、それをパスに変換したものに対して機能する：

   A variety of *Tweak Tool* modes modify paths. If an object is not a path
   (i.e., *Rectangles*, *Ellipses*, text) it is first converted to a path.
   Unlike the *Node Tool*, nodes do not need to be selected.

パス微調整は *Fidelity* というパラメーターを、すべてのモードで共有する。この値が
大きいほどノード数が増えてしまう：

   The range for the parameter is from 1 to 100. A low value gives a rough
   distortion using few nodes, a high value gives a smoother distortion but at
   the cost of creating large numbers of nodes. Note that any path distortion
   will affect the entire path, even the parts that are far away from the
   cursor.

パスは Bezier 曲線や B-Spline 曲線であるので、曲線全体に歪みが波及するのを覚悟し
ないといけない。

   The tool has several known problems. If used on an open path, the path will
   become closed. It doesn't work well on straight lines or lines with just two
   nodes.

パス微調整モードは次の四種：

:guilabel:`Push parts of paths in any direction`
   ドラッグ方向にパスを追いやる。

   .. admonition:: 利用者ノート

      パスが閉曲線に変化するかもしれない。

:guilabel:`Shrink (inset) parts of paths; with Shift to grow (outset)`
   ドラッグしている間にポインター近傍のパスをインセットまたはアウトセットする。
:guilabel:`Attract parts of paths towards cursor; with Shift from cursor`
   ドラッグしている間にポインターの内側か外側にパスをずらす。
:guilabel:`Roughen parts of paths`
   ドラッグしている近傍のパスを粗くする。

さらに元のモードによっては :kbd:`Ctrl` を押すと一時的に縮みモードに、:kbd:`Ctrl`
+ :kbd:`Shift` で育ちモードに切り替わる。

*Tweak Tool* の応用として、ハッチングを調整する事例を挙げている。

本節最後のイラストのハッチングは、:menuselection:`Extensions --> Generate from
Path --> Interpolate` を二度使用して、「直交」する線の集合を作成し、それを円で切
り取ることで作成したとある。この複合パスを :kbd:`Shift` + :kbd:`Ctrl` + :kbd:`K`
と :kbd:`Ctrl` + :kbd:`Alt` + :kbd:`C` した。最後に *Tweak Tool* の *Shrink*
モードで線を引き締めてシェーディング効果を表現しているとある。

Tweaking Colors
======================================================================

   The *Tweak Tool* can be used to make small color changes to objects. In doing
   so, it changes the *Fill* and/or *Stroke* color of an entire object.

ツールモードは二つあって、どちらにも共通するオプションがある。まずモードを知る：

:guilabel:`Paint the tool's color upon selected objects`
   現在の *Fill* と *Stroke* スタイルで彩色する。

   * 次のモードもそうだが、*Fill* と *Stroke* のどちらかが設定されていない場合、
     微調整対象オブジェクトは変化しない。
   * :guilabel:`Shift` を押したままにすると、適用色が反転する。

:guilabel:`Jitter the colors of selected objects`
   色をランダムにする。現在のスタイルは使わない。

共通オプション：

   The *Tweak Tool* in a color mode has four options. It can act independently
   on a color's hue, saturation, lightness (:abbr:`HSL`) and opacity. The
   options can be toggled on independently by the :guilabel:`H`, :guilabel:`S`,
   :guilabel:`L`, and :guilabel:`O` icons next to the :guilabel:`Channel` label
   in the *Tool Controls*.

.. admonition:: 利用者ノート

   塗りつぶしがないオブジェクトの描線の色も、輪郭線のないオブジェクトの色を微調
   整することも不可能となっていことを承知する。

   :guilabel:`Fill and Stroke` ダイアログを開いていれば、ドラッグ中に色の変化す
   るようすを成分ごとに観察できる。
