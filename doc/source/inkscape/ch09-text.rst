======================================================================
Chapter 9. Text
======================================================================

.. contents::

テキスト周りの技法を身に着けておくとポスターや字幕作成の即戦力となる。しっかり読
んでいく。ワープロソフトと同じことは当然実現できる：

   Inkscape has a sophisticated system for creating and manipulating text. Text
   strings can include *Bold* or *Italicized* substrings and changes in font
   type and size. Text can be justified on the right and/or left. It can be
   horizontal or vertical.

それに加えて図面ソフト、描画ソフトならではの機能が用意されている。

   Individual characters can be kerned. Text can be put on a path or flowed into
   an arbitrarily shaped path.

テキストはオブジェクトとしては三種類存在する：

   There are three types of text objects in Inkscape. The first is regular text.
   The second is flowed text; this is a text object that includes a rectangular
   frame. The third is linked-flowed text. This is a text object where the text
   is flowed into a separate arbitrary shape or path object(s). It is discussed
   at the end of this chapter.

よくわからないテキストに対しては、とりあえずピックしてステータスバーを確認すると
いいようだ：

   When a text object is selected, its type is shown in the *Notification
   Region*.

Creating Text
======================================================================

テキストオブジェクトを作成するには：

* :guilabel:`Toolbox` の :guilabel:`Create and edit text objects` ボタンをクリッ
  ク
* :kbd:`F8` または :kbd:`T` を押す。

まずは標準テキストの作成方法を見ていく。これがいちばん単純な作成方法だし、今まで
もっとも採用してきたものだと思う：

   There are two ways to add text to an Inkscape drawing. The first is as
   *regular* text. In this case, as text is typed, the *text box* grows to
   accommodate the text. Line breaks must be manually added.

二つ目はテキストを収容する矩形を先に指定するものだ：

   The second way to enter text is as a *flowed* text object. The text is typed
   into a presized rectangular text box. Line breaks are automatically made. The
   *flowed* text object includes both the box and text and is thus moved and
   transformed as such.

以降、これらに共通する注意が述べられていく。

* *Text Tool* で既存のテキストをクリックすると、対象オブジェクトが選択され、キャ
  レットがクリック位置に最も近い文字の間に置かれる。その後、文字列を編集すること
  ができるようになる。
* テキスト入力モードではキーバインドの多くが機能しない。テンキーの符号キーは
  :kbd:`NumLock` がオフのときにはズーム機能が効く。
* 特別な文字に対する入力方法が二つある（ノート割愛）。
* 対応フォントがないと、テキストが表示されないことがある。この問題を回避するため
  に、テキストをパスに変換などすると、テキスト編集の機会が失われる。次のようなコ
  ツが知られている：

     Make a duplicate of the text before you convert the text to a path. Put the
     copy on a separate layer and make that layer invisible. Then if you ever
     need to edit the text as a text object, you will have a copy available.

* テキストオブジェクトを選択すると、最初の行の baseline の左側に小さな□が表示
  される。これが baseline anchor で、スナップや位置揃えに使われる。

Entering Regular Text
----------------------------------------------------------------------

すでに知っていることだが：

   To add *regular* text, click on the document where you desire the text to
   start. You should see a cursor (blinking bar) indicating you are in the text
   enter mode and showing where the text will start. To add text, just start
   typing. You can enter multiline text by inserting a carriage return. The text
   box will grow as text is entered.

Entering Flowed Text
----------------------------------------------------------------------

本題に入る前に *flowed* text は SVG 規格に採用されてない場合の対処法について述べ
られている：

   Flowed text was a draft SVG 1.2 specification that will not in the end be
   adopted. The text is not likely to be viewable by other renderers. In
   addition, some programs will not render any of a file with flowed text
   (Squiggle, for example). You can convert the flowed text to a regular text
   object before saving to avoid this problem.

流し込みテキストの作成方法を見ていく。ツールを起動してからクリックではなく、ク
リックドラッグで矩形を描くのだ：

   To add *flowed* text, click-drag on the document with the *Text Tool* to
   create a blue rectangle box for the text. Once the box is drawn, you can move
   the cursor into the box area and begin to type. Carriage returns are
   automatically made.

テキストを大量にタイプしていくと、描画が急に消えて矩形の描線が青から赤になる。

   Instead the rectangle will turn red to indicate that not all the text is
   displayed. The box can be enlarged or the proportions changed by dragging on
   the handle at the lower-right side with the *Text Tool*, *Node Tool*, or any
   of the shape tools; however, the text box will only be shown when using the*
   Text Tool*.

流し込みテキストではこの矩形の操作が急所になるようだ。箱の変形に合わせて内容物も
一緒に移動する。

   Use the :kbd:`Ctrl` key while dragging to constrain the change in box size to
   a horizontal or vertical direction. The box and text can be moved together.

Selecting Text
======================================================================

   Editing and applying attributes to text requires positioning the cursor or
   selecting text. The following methods are available when using the *Text
   Tool*

テキストエディターのキーバインドやマウス操作を習得するのと同じようにして、テキス
ト内でのキャレットの移動や文字列選択操作を習得すること。

Editing Text
======================================================================

先述の方法でテキスト編集モードになれば、クリップボード操作を含む Windows の編集
コントロール同様のキー操作が利用可能だ。さらに、別の編集手順もある：

   An alternative way to edit text is to use the :guilabel:`Text` tab of the
   :guilabel:`Text and Font` dialog (:menuselection:`Text --> Text and Font...`
   (:kbd:`Shift` + :kbd:`Ctrl` + :kbd:`T`)). Editing text in the tab may be
   easier, especially for long texts.

Spell Checking
----------------------------------------------------------------------

いざとなれば Inkscape ではなく、他のソフトで実現可能だが：

   To spell check a document, call up the :guilabel:`Check Spelling` dialog
   (:menuselection:`Text --> Check Spelling...` (:kbd:`Ctrl` + :kbd:`Alt` +
   :kbd:`K`)). When a suspect word is found, it will be highlighted on the
   canvas by a red box. If using the *Text Tool*, the cursor will be placed at
   the start of the word. And if the :guilabel:`Text` tab of the :guilabel:`Text
   and Font` dialog is open, the word will underlined with a red squiggle.

Inkscape を実行するプラットフォームで校正機能構成が異なる：

   You can select which languages to use (up to three) in the
   :guilabel:`Inkscape Preferences` dialog in the :guilabel:`Spellcheck`
   section. At the moment, on Windows, only an English dictionary is included.
   On Linux, one can install additional dictionaries by installing the Gnu
   Aspell package with any language packs required.

やはり Inkscape 外の環境でチェックするほうがいい。

Formatting Text
======================================================================

この節でいう書式は :guilabel:`Font and Text` ダイアログで指定可能な属性とする。
他の型のオブジェクトと共通するものについては次の章で。

テキスト書式を制御する方法は次の三つを

#. テキストに対する *Tool Controls* を使う
#. キーバインドによる
#. :guilabel:`Text and Font` ダイアログを使う

同じ UI でも操作手順によって結果が異なることに注意する：

   When changing properties of text, if characters within a text object are
   selected, the changes apply only to those characters. Otherwise, the changes
   apply to all selected text objects (to select more than one text object,
   switch temporarily to the *Select Tool*). Changes made when no text object is
   selected (or a new blank text object is created) change the default style.

Font Family
----------------------------------------------------------------------

*Font Family* の設定はキーバインド以外の方法で行える。二つは挙動が若干異なる。

ツールバーから設定する場合、いちばん左にあるドロップダウンリストを使う。
Inkscape で利用可能なフォントが一覧される。

* フォントプレビューが重い場合、:guilabel:`Inkscape Preferences` ダイアログ
  :menuselection:`Tools --> Text --> Show font samples in the
  drop-down menu` をオフにして無効にする。
* :file:`preference.xml` でサンプルテキストを独自設定することができる。
* :kbd:`Alt` + :kbd:`X` でドロップダウンリストにフォーカスが行く。
* エディットコントロールは編集可能。フォントのインクリメンタルサーチ欄。

:guilabel:`Text and Font` ダイアログから設定する場合、:guilabel:`Apply` ボタンを
明示的に押さないと図面内のテキストが更新されない。

Font Size
----------------------------------------------------------------------

   In both cases, the font size (in pixels) can be selected from a drop-down
   menu.

とあるのだが、ツールバーのほうはフォントサイズの単位を別のドロップダウンリストか
ら選択できる。

   The change takes effect upon selection or hitting :guilabel:`Enter` in the
   case of the *Tool Controls* and upon clicking :guilabel:`Apply` in the case
   of the :guilabel:`Text and Font` dialog.

この決定アクションは他の属性に対しても必要のようなので、以降はノートを省略。

Font Style
----------------------------------------------------------------------

基本はこれ：

.. csv-table::
   :delim: |
   :header: キーバインド,コマンド
   :widths: auto

   :kbd:`Ctrl` + :kbd:`B` | 太字オンオフ
   :kbd:`Ctrl` + :kbd:`I` | 斜体オンオフ

ものによっては他の書式もある。それはダイアログの方でいじる：

   A font may have other styles available (e.g. narrow, semi-bold). All possible
   styles (including *Bold*, and *Italic/Oblique*) can be selected in the
   :guilabel:`Style` section of the :guilabel:`Text and Font` dialog.

Justification
----------------------------------------------------------------------

ツールバーの :guilabel:`Text alignment` ドロップダウンリストにある四種から選択。
項目は上から順に：

* Align left
* Center
* Align right
* Justify (left and right justified)

最後の選択肢は流し込みテキストのみ有効。

Superscripts and Subscripts
----------------------------------------------------------------------

ツールバーの :guilabel:`Toggle superscript` および :guilabel:`Toggle subscript`
ボタンで処理する。

   The selected text will be shifted up or down and reduced in size.
   Superscripts and subscripts can be removed by selecting and then clicking on
   the same icons.

実装は次のようになっている：

   Inkscape implements superscripts and subscripts by setting the
   ``baseline-shift`` attribute to either ``"super"`` or ``"sub"``, and by
   setting the ``font-size`` attribute to ``65%``. Inkscape will only recognize
   a superscript or subscript if the ``baseline-shift`` attribute is set in this
   manner.

Line Spacing
----------------------------------------------------------------------

行間の（横書きなら）高さを調整する。SVG 標準でない属性を内部的に保持することで実
現しているようだ：

   Note that although Inkscape uses the attribute ``line-spacing`` to store the
   line spacing value, it is not part of the SVG standard (it is, however, part
   of the CSS standard). Inkscape uses the value to position lines of text.

ツールバーの :guilabel:`Spaces between baselines` 欄に数値を入力することで調整する。

キーバインドによる調整が可能。量が画面ズームに依存する：

   It can also be changed by the following keyboard shortcuts (note adjustments
   are specified in Screen pixels and thus depend on the zoom level):

.. admonition:: 読者ノート

   本書のキーバインドが効かない。

Word Spacing
----------------------------------------------------------------------

   Word spacing can be changed via an entry box in the *Tool Controls*.

Inkscape 1.2 ではツールバーに ``Spacing`` と書かれたボタンがあり、これを押すと入
力欄が複数出現する。このうち :guilabel:`Spacing between words` ツールチップがマ
ウスホバーでポップアップする入力欄で単語間の間隔を変更する。

   Changes apply to selected text if text is selected or to the entire text
   block if not.

Letter Spacing
----------------------------------------------------------------------

ツールバー内 ``Spacing`` ボタンを押し、マウスホバーで :guilabel:`Spacing between
letters` ツールチップが出現する入力欄で文字間隔を変更する。

.. admonition:: 読者ノート

   本書のキーバインドが効かない。

Kerning, Shifting, and Rotating Characters
----------------------------------------------------------------------

   Individual characters in a line of *regular* (but not *flowed*) text may be
   shifted left or right to change their *kerning*, shifted up or down, or
   *rotated*. (Both *regular* and *flowed* text do utilize the internal
   *kerning* that is included with fonts.)

   All *manual* kerning/shifts/rotations can be removed with the
   :menuselection:`Text --> Remove Manual Kerns` command.

Kerning and Shifting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ツールバー内 ``Spacing`` ボタンを押し、:guilabel:`Horizontal kerning (px)` や
:guilabel:`Vertical kerning (px)` がツールチップである入力欄で調整できる。

.. csv-table::
   :delim: |
   :header: キーバインド,コマンド
   :widths: auto

   :kbd:`Alt` + 矢印 | 画面画素一個分だけ文字を対応するキー方向にずらす
   :kbd:`Shift` + :kbd:`Alt` + 矢印 | 上記の十倍バージョン

.. admonition:: 利用者ノート

   カーニングコマンドが文字列に対して全然効かない。UI 動作は正常と思われる。

Rotating
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ツールバー内 ``Spacing`` ボタンを押し、:guilabel:`Character Rotation (degree)`
がツールチップである入力欄で調整できる。

   If no characters are selected, only the character following the text cursor
   will be rotated. If characters are selected, all the selected characters will
   be rotated.

.. csv-table::
   :delim: |
   :header: キーバインド,コマンド
   :widths: auto

   :kbd:`Ctrl` + :kbd:`[` | 左回りに 90 度回転
   :kbd:`Ctrl` + :kbd:`]` | 右回りに 90 度回転

.. admonition:: 利用者ノート

   文字回転機能はかろうじて動く。本書の示す :kbd:`Alt` キーを使う回転は効かな
   い。

   そもそも調整欄とテキスト欄を往復して編集作業をするというのがおかしい。

Orientation
----------------------------------------------------------------------

これは本書の記述と Inkscape 1.2 とでだいぶ異なっている。関係があると思われるツー
ルバーのドロップダウンリストが三つある：

:guilabel:`Block progression`
   テキストブロックにおける行の進行方向とでも言えるか。次の三つの選択肢がある：

   * 横書き
   * 縦書き（行は右から左に進む）
   * 縦書き（行は左から右に進む）

:guilabel:`Text (glyph) orientation in vertical direction`
   縦書きのときの文字の向きを指定する。英数字系に回転を入れるかどうか。あるいは
   全角文字系にも回転を入れるかどうかを組み合わせた選択肢から指定する。

:guilabel:`Text direction for normally horizontal text`
   これがよくわからない。アイコンからすると ``ltr`` or ``rtl`` に思えるが、実際
   に使ってみるとそんなことはないような。

Text on a Path
======================================================================

   To place text on a path, enter the text as a *Regular* text or *Flowed* text.
   Draw the desired path. Select both text and path, then use the
   :menuselection:`Text --> Put on Path` command. The text should now appear along
   the path.

次の事実は他のコマンドでも通用するので心得ておく：

   Note that *Shapes* except for *Rectangles* are described internally by
   Inkscape as paths and thus don't require converting to a path.

その場編集に関する次の記述から、当コマンドは複製コマンドの変種であると推察でき
る：

   Both the text and the path can be edited in place. The text should adjust to
   any changes in the path. The path can be made invisible by selecting only the
   path, then removing the *Stroke* paint with the :guilabel:`Fill and Stroke`
   dialog. To select an invisible path for editing, select the text and use
   :guilabel:`Edit --> Clone --> Select Original` (:kbd:`Shift` + :kbd:`D`). To
   remove text from a path, use :guilabel:`Text --> Remove from Path`.

このパス削除コマンドが複製解除コマンドと同じ挙動であるかどうかを確認したい。

   Text can be adjusted or moved relative to the path.

パスの向きがテキストの配置に大きく関係する。変だなと思ったらパス反転でいい。

   Text on a path is initially placed on the “left” side of the path (referenced
   from the path direction) starting at the beginning of the path. One can
   change the direction of the text (and the side it is placed on) by reversing
   the direction of the path (e.g., :guilabel:`Path --> Reverse` (:kbd:`Shift` +
   :kbd:`R`)). If the text is center justified prior to being put on a path, it
   will centered along the path.

本書囲み記事の円弧にテキストを配置する例は実践的だ。オブジェクト反転コマンドも使
える。

Text in a Shape
======================================================================

   Text can be flowed inside any arbitrary shape by linking a text object to a
   shape or path.

古銭形に流し込まれたテキストのイラストだと、この閉曲線二つがパス全体なのだろう。
作成手順は次のとおり。

   To create a linked flowed text object, select a text object and one or more
   shape/path objects. Then use the :guilabel:`Text --> Flow into Frame`
   (:kbd:`Alt` + :kbd:`W`) command. If multiple shape/path objects are selected,
   the text will flow into the last object selected first.

連結成分が複数ある選択では、選択順序がテキストの配置に影響する。

:menuselection:`Text --> Put on Path` と同じように、このオブジェクト構造も複製に
基づいている。前項と同じ性質がある。

   *Flowed* text can be converted back to a *regular* text object with the
   :menuselection:`Text --> Unflow` (:kbd:`Shift` + :kbd:`Alt` + :kbd:`W`). The
   resulting text will be on a single line.

   The :menuselection:`Text --> Convert to Text` command converts *link-flowed*
   text to a *regular* text object while preserving the appearance of the text.
   The text is still editable but will no longer reflow inside the shape or path
   frame. This is necessary for display of the drawing in another SVG renderer.
