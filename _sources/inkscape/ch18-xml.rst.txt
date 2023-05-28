======================================================================
Chapter 18. XML Editor
======================================================================

.. contents::

Inkscape は :abbr:`SVG` という :abbr:`XML` データを編集するアプリケーションであ
るので、利便性を高めるべくテキストエディターのように編集するための :abbr:`GUI`
も備えている。

   The :guilabel:`XML Editor` dialog allows one to directly edit the :abbr:`XML`
   description of an :abbr:`SVG` drawing. (Recall that Inkscape is an
   :abbr:`SVG`-based drawing program and that :abbr:`SVG` is an
   :abbr:`XML`-based file format.)

   The ability to directly edit an :abbr:`SVG` :abbr:`XML` file is very
   powerful. It allows the user more control over objects in their drawing such
   as specifying the exact size or position of an object and by giving access to
   :abbr:`SVG` parameters that are not directly or easily available through the
   Inkscape interface.

Basic Usage
======================================================================

:guilabel:`XML Editor` ダイアログを開くには次のいずれかを行う：

* :menuselection:`Edit --> XML Editor...` を選択する
* :kbd:`Shift` + :kbd:`Ctrl` + :kbd:`X`

ダイアログ内にはツリーコントロールを含む UI が示される。特に、オブジェクトを表現
する :abbr:`SVG` ノードを選択すると、右側にその属性一覧が出力される：

   Upon adding an ellipse to the drawing, an entry (node) is added for the new
   ellipse under the formerly empty *Layer* (see next figure). The line is
   highlighted and the ellipse's parameters are shown on the right. Note that
   the name of the object is given in the highlighted line (in this case,
   ``path1599``).

.. admonition:: 読者ノート

   Inkscape 1.2 ではダイアログ右下のレイアウトボタンでビュー分割方式を垂直か水平
   に選択可能。本書の記述は水平方式に対応している。

   属性の表示自体もダイアログ左下の :guilabel:`Show attributes` スイッチで切替可
   能。

楕円オブジェクトを編集するのに :abbr:`GUI` に戻って *Ellipse Tool* を起動しなく
ても、この属性一覧 UI から編集することが可能だ：

   Now, suppose you would like the ellipse to have a width of 400 pixels (i.e.,
   a radius of 200 pixels in the *x* direction). You can specify this by
   clicking on the ``sodipodi:rx`` attribute. The attribute is shown below with
   the current value in the attribute entry box.

編集確定操作は本書の記述とは異なり、即時反映される。以降同様。

ここにない属性を追加することも可能だ：

   To add a new attribute, type the name of the new attribute in the upper entry
   box, enter the value in the lower entry box, and then either click the
   :guilabel:`Set` button or use :kbd:`Ctrl` + :kbd:`Enter`.

ここでも明示的な確定処理は現存しない。

属性を追加するのなら意味があるものにしたいが、Inkscape はそういう入力支援を対応
していないようだ。:abbr:`SVG` 仕様を自分で確認するしかないか：

   Sometimes it is useful to know what the allowed attributes are for a given
   type of object. The :abbr:`SVG` standard is described in detail at the
   `Official W3C SVG <http://www.w3.org/TR/SVG/>`__ website.

しかも、Inkscape は :abbr:`SVG` 仕様のすべてに対応しているわけではないので、なお
さら欲しい：

   Note that not all the :abbr:`SVG` standard is currently supported in
   Inkscape. It is possible, however, to add nonsupported attributes via the
   :guilabel:`XML Editor`. These attributes may not be displayed by Inkscape but
   will appear in any program that supports those attributes.

Inkscape が生成する :abbr:`SVG` データ :abbr:`SVG` 標準部分と Inkscape 独自部分
に分類される。特に、よく見かける ``sodipodi`` 要素についてその意味が述べられてい
る：

   In the above example, the attributes with the ``sodipodi`` tag are internal
   to Inkscape (the ``sodipodi`` tag is the result of Inkscape being branched
   from the Sodipodi program). These attributes are used to calculate the “real”
   :abbr:`SVG` path definition given by the ``d`` attribute.

Inkscape の *Export* コマンドは独自データを含まない可能性があると述べている：

   The Inkscape internal elements should be ignored by other :abbr:`SVG`
   rendering programs. This may not always be true, thus Inkscape includes the
   possibility to export a drawing without the Inkscape internal elements.

利用者としてはむしろその挙動を期待している。

Editing XML Nodes
======================================================================

:guilabel:`XML Editor` ダイアログのツールバーアイコンの説明。必要に応じて本書の
記述を Inkscape 1.2 に合わせるように修正して記す。

:guilabel:`New element node`
   属性が何もない空のノードを追加する。したがって役に立たない。
:guilabel:`New text node`
   空文字列を追加する（内容を編集するのは右ビューで）。テキストオブジェクトの文
   字列を編集する場合にも使える。
:guilabel:`Duplicate node`
   選択ノードを深く複製する。複製ノードは元ノードの次ノードになる。ID が新規に割
   り振られる。これを利用者が決めてもかまわない。
:guilabel:`Delete node`
   選択ノードをその子孫ノード全てを込みで削除する。

----

:guilabel:`Unindent node`
   ノードを一階層上に移動する。グループ内のオブジェクトの場合、オブジェクトを
   グループから削除することに相当する。
:guilabel:`Indent node`
   ノードを一階層下に移動する。同階層で上にある最も近いノードの下に移動する。
:guilabel:`Raise node`
   同じ親を持つ前のノードのその前にノードを移動する。描画オブジェクトで言えば
   z-order を上げることに相当する。
:guilabel:`Lower node`
   同じ親を持つ次のノードのその次にノードを移動する。描画オブジェクトで言えば
   z-order を下げることに相当する。

属性一つを削除するにはポリバケツをクリック。

Examples
======================================================================

   A few examples are given here to show the possibilities of “hand” editing the
   :abbr:`XML` file.

手で編集することの可能性のほうが高いはずなのだが。

Adding Color to a Marker Arrow
----------------------------------------------------------------------

現行の Inkscape ではマーカーの色は線のそれと一致するように描画されるが：

   This section is kept for pedagogical reasons.

逆にマーカーの色をパスの色と変えることを試せる。XML Editor で対応ノードを探索す
ることから始める：

   To add color to a marker, open up the :guilabel:`XML Editor`. Select the path
   with the marker in the canvas window. In the ``style`` attribute for the
   line, locate the marker entry (``marker-end:url(#Arrow2Lend)``, for example).

マーカーの ID が判明したので、それをツリーの特定のノードの子から探索する：

   Then expand the ``<svg:defs>`` line by clicking on the triangle at the
   beginning of the line (if not already expanded). You should see an entry for
   the marker. Select that entry.

パスの属性一覧と似たような画面が右側に出るので、``style`` 定義文字列を次のように
編集する：

   The attributes for the marker should be displayed on the right. Select the
   ``style`` attribute. Add ``fill:#rrggbb`` to the attributes in the entry box
   at the bottom right, where ``#rrggbb`` is the :abbr:`RGB` color in
   hexadecimal form (obtainable from the attributes for the path).

これで色が変わるが、初期値の色に戻すために定義を消してもいい：

   The marker should change color. If it doesn't, then expand the
   ``<svg:marker>`` line. Select the path entry and remove any Fill and/or
   Stroke paint. For this change to show up, you must save and reopen the
   :abbr:`SVG` file.

Underlined Text
----------------------------------------------------------------------

   Underlined text cannot be added through the normal Inkscape interface, nor
   will Inkscape display underlines. But you can add underlined text that will
   be displayed properly by another :abbr:`SVG` program.

確かに Inkscape はテキストに下線を装飾するための :abbr:`GUI` を備えていない。

   To underline text, open the :guilabel:`XML Editor`. Select the text you wish
   underlined. Go to the ``<svg:tspan>`` object found inside an ``<svg:text>``
   tag. If you are selecting part of the text, you may need to add some
   attribute temporarily (color for example) to create a corresponding ``tspan``
   object; the color can be removed later. Add to the style: ``text-decoration:
   underline``.

うれしいことに、Inkscape の図面描画においても下線が描かれる。同様のスタイル追加
で下線の色を指定する (e.g. ``text-decoration-color:#rrggbb``) なども可能だろう。
