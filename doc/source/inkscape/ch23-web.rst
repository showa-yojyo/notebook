======================================================================
Chapter 23. SVG and the Web
======================================================================

.. contents::

ページ右側の囲み記事 The origins of HTML5 では :abbr:`XHTML` の衰亡と
:abbr:`HTML5` の契機について述べている。読まなくていいはずだ。

章本文の冒頭に行こう。

   :abbr:`SVG` plays nicely with other web technologies: :abbr:`SVG` files can
   be embedded into web pages, they can contain hypertext links, and they can be
   can be scripted and animated. And now with :abbr:`HTML5`, :abbr:`SVG` will be
   everywhere.

前章で見たように、:abbr:`SVG` ファイルをウェブブラウザーで表示するか、それ以上の
ことが可能だ。

   Inkscape has mostly been developed as a tool for artists and not for web
   graphics but it is still possible with a little work and knowledge to use
   Inkscape to create web graphics.

この事実は意外かもしれないが、そのことは囲み記事の前半で述べられている事実から窺
える。

   Current versions of Firefox, Opera, Safari, and Chrome include almost
   complete support (Firefox doesn't handle :abbr:`SVG` fonts and Safari 5
   doesn't handle filters). Internet Explorer 9 will offer almost full
   :abbr:`SVG` support (missing :abbr:`SVG` fonts, :abbr:`SMIL` animation, and
   filters).

Web ブラウザーが :abbr:`SVG` に対応しているかどうかを心配する必要は基本的にはな
さそうだ。

現代的なブラウザーにおいてはインライン :abbr:`SVG` もアリだ：

   The upcoming :abbr:`HTML5 (Hypertext Markup Language, version 5)`
   specification allows “inline SVG”. :abbr:`HTML5` defines two different
   syntaxes: :abbr:`HTML` and XML. All major Web browsers will support
   :abbr:`HTML` syntax in the very near future. All major browsers except
   Internet Explorer (prior to version 9) already support inline :abbr:`SVG`
   with :abbr:`XML` syntax as well as in :abbr:`XHTML` proper.

ブラウザー各種の最新状況一覧を提供する者がいるようだ。下記リンク先の検索欄に
``svg`` とか入力して結果を見るといい。

   For an up-to-date list of which browsers support what, take a look at the
   `When can I use... <https://caniuse.com/>`__ website. Chrome is frequently
   updated (every six weeks!), Firefox, Opera, Safari less so, and, well you
   probably already know about Internet Explorer.

   A web page displaying the examples discussed here is available at the `book's
   website <http://tavmjong.free.fr/INKSCAPE/>`__. Several web pages for testing
   browser support of :abbr:`SVG` can also be found there.

この章の題名と同じリンクをクリックすると、ささやかな例が示される。できれば複数の
ブラウザーで確認するのがいい。それよりもトップページの時計がよくできていて感心す
る。

Simple SVG Display
======================================================================

   There are many different ways to display :abbr:`SVG` files in a web page. The
   simplest way is just to link to an :abbr:`SVG` file with the ``<a>`` tag. Web
   browsers that support :abbr:`SVG` will display the drawing by itself.

したがって、Inkscape で作成した :abbr:`SVG` ファイルをブラウザーにドラッグアンド
ドロップすると、その内容が表示される。

   To include :abbr:`SVG` content as part of a web page one can use one of the
   following options:

   * ``<object>`` tag.
   * ``<embed>`` tag.
   * ``<iframe>`` tag.
   * ``<img>`` tag.
   * Inline SVG.
   * CSS ``background``.

このうち ``<img>`` を使うのは当ノートでも適用している。``<iframe>`` と CSS
``background`` も良さそうだ。

The ``<object>`` Tag
----------------------------------------------------------------------

このタグはブラウザーが :abbr:`SVG` ファイルを扱えない場合の対応策を用意している。

   The ``<object>`` tag is the primary way to include an external :abbr:`SVG`
   file. The main advantage of using this tag is that there is a natural
   mechanism for displaying a fallback in case the :abbr:`SVG` is not rendered.

:abbr:`SVG` を読み込むための ``<object>`` タグの書き方はこうなる：

   The tag requires defining a ``data`` attribute which is the location of the
   :abbr:`SVG` file, normally a relative path. Defining the ``type`` attribute
   is highly recommended as it allows browsers to avoid downloading content they
   do not support. For :abbr:`SVG` the type is ``"image/svg+xml"``.

古いブラウザーのために、対応する PNG ファイルを Inkscape のエクスポート機能で用
意して、そこに置くのが親切だ：

   If the :abbr:`SVG` is not rendered, the browser will try to render the
   content between the opening ``<object>`` and closing ``</object>`` tags. A
   :abbr:`PNG` version of the :abbr:`SVG` would normally be a good choice to put
   here.

タグの定義例から急所の :abbr:`HTML` コードを次に抜粋する。上記の記述に沿っている
ことを確認できる：

   .. code:: html

      <object type="image/svg+xml" data="web_square.svg">
        <img src="web_square.png" alt="Blue Square"/>
      </object>

The ``<embed>`` Tag
----------------------------------------------------------------------

この馴染みのないタグの説明から：

   It is intended for including content that needs an external plug-in to work.
   The Adobe plug-in requires the use of the ``<embed>`` tag and supporting this
   tag is the only real reason for its use with :abbr:`SVG`. There is no
   fallback mechanism if the :abbr:`SVG` content is not displayed. Note that
   Chrome 8 and Safari 5 may require width and height attributes to avoid scroll
   bars. Safari 5 also incorrectly displays :abbr:`SVGs` with non-transparent
   backgrounds.

ならば使う理由がない。

   Here is an example of using the ``<embed>`` tag. Only the src attribute is
   required.

   .. code:: html

      <embed src="web_square.svg"/>

The ``<iframe>`` Tag
----------------------------------------------------------------------

まず ``<iframe>`` タグの歴史から：

   The ``<iframe>`` tag, deprecated in :abbr:`HTML4` and :abbr:`XHTML`, has
   resurfaced in :abbr:`HTML5` with the purpose of “sandboxing” content that
   might pose a security risk.

このタグを利用して :abbr:`SVG` ファイルを描画するときの性質：

   There is no fallback if the :abbr:`SVG` content cannot be displayed. A frame
   will be drawn around the :abbr:`SVG`. It can be removed by setting the
   attribute frameborder to 0 (note that this is not valid :abbr:`HTML5`). The
   size of the frame can be set using the width and height attributes. If the
   size of the frame is too small to contain the :abbr:`SVG`, scroll bars will
   be used. Safari 5 incorrectly displays :abbr:`SVGs` with non-transparent
   backgrounds.

枠が描かれたり、スクロールバーが付いたりするのは WebGL の学習時にも体験している
が、:abbr:`SVG` ファイル読み込み描画に対しても事情は同じか。

こちらは終了タグが必要となる：

   .. code:: html

      <iframe src="web_square.svg"></iframe>

The ``<img>`` Tag
----------------------------------------------------------------------

使い慣れている ``<img>`` タグで :abbr:`SVG` ファイルを指定することが可能だ。しか
し、そうすると :abbr:`SVG` が備えている利点を活かせないことになる：

   There are two reasons not to use the ``<img>`` tag with :abbr:`SVGs`. The
   first is that there is no fallback mechanism if the browser cannot render the
   image. The second is an :abbr:`SVG` rendered this way is not allowed to run
   any scripts or have any interaction (e.g. links).

Inline SVG
----------------------------------------------------------------------

インライン :abbr:`SVG` は基本的には HTML5 でやるほうがいいようだ：

   * To include :abbr:`SVG` using :abbr:`HTML` syntax you must use a browser
     with an :abbr:`HTML5` parser.
   * All the major web browsers except Internet Explorer already support SVG
     with :abbr:`XML` syntax (as well as in :abbr:`XHTML`).
   * An :abbr:`HTML5` file normally ends with ``.html`` when using :abbr:`HTML`
     syntax and ``.xhtml`` or ``.xml``; when using :abbr:`XML` syntax.

次はインライン :abbr:`SVG` の例だ。名前空間周りで苦労するのはどこでも一緒か：

   Note that the two Name Space declarations are optional with :abbr:`HTML5`
   syntax. The :abbr:`SVG` has been stripped of all unnecessary parts such as
   items in the Inkscape Name Space.

コードは急所を抜粋：

   .. code:: html

      <svg
         xmlns="http://www.w3.org/2000/svg"
         version="1.1"
         width="150"
         height="150">
        <rect
   	      width="90"
   	      height="90"
   	      x="30"
   	      y="30"
   	      style="fill:#0000ff;fill-opacity:0.75;stroke:#000000"/>

ここで ``xmlns`` の行は «Required for :abbr:`XHTML`, optional for :abbr:`HTML5`»
だ。

CSS Background
----------------------------------------------------------------------

古いブラウザーのための fallback も込めた定義例：

   .. code:: css

      body {
        background-image: url('background.png');
        background-image: none, url('background.svg'), url('background.png');
        background-size: 100% 100%;
      }

Supporting Older Browsers
----------------------------------------------------------------------

古いブラウザーなんか全部無視で構わず、次のことを実践すればもう十分だ：

   At the moment, the best way to include :abbr:`SVG` content in a web page is
   to use the ``<object>`` tag with a :abbr:`PNG` fallback. This is a simple
   method that will automatically take care of support for older versions of
   Internet Explorer.

Positioning SVG
======================================================================

   This section is based on current browser behaviour and the :abbr:`SVG`
   specification. There is active discussion on changing the specification by
   the :abbr:`SVG` standards group.

それでも真剣に読む。

   There are two steps. The first is to determine the viewport or area allocated
   to the :abbr:`SVG` by the web page, the second is to determine how the
   :abbr:`SVG` fits into the viewport. For this discussion we will assume the
   :abbr:`SVG` is being inserted via the ``<object>`` tag.

最初の段階はこういう感じだという：

#. ``<object>`` タグに ``width`` または ``height`` 属性が定義されている場合、こ
   れがビューポートの寸法となる。
#. ``<object>`` に固定した ``width`` と ``height`` がなく、かつ :abbr:`SVG` に固
   定した ``width`` と ``height`` があれば、その :abbr:`SVG` 値によってビュー
   ポート寸法を決定する
#. それでもビューポートが決定されない場合、:abbr:`SVG` の幅と高さが 100% であれ
   ば、ビューポートは ``<object>`` タグが利用できる空間を埋め尽くす。

寸法の信頼性については次の助言がある：

   Think of the :abbr:`SVG` ``width`` and ``height`` attributes as
   recommendations to the renderer about the size of the viewport if the
   :abbr:`HTML` doesn't define the size. They are not(!) always the width and
   height of the drawing.

第二段階は想像がつかないのでよく読む：

   Now that the viewport is defined, how the :abbr:`SVG` is fitted inside that
   viewport must be determined. Again this is a several step process:

これも長いのでまとめる：

* :abbr:`SVG` 側にもビューポートを指定する属性 ``viewBox`` があることがある。

  * 値はおそらく矩形。
  * さらに属性 ``preserveAspectRatio`` というものがあり、縦横比を維持するかどう
    かを決める以上のことを指定する。
  * この二つの属性により、:abbr:`SVG` ビューポートを第一段階で決定したビューポー
    トに写像する。

* :abbr:`SVG` に ``viewBox`` が定義されていない場合は決め打ち：

  * ビューポートの左上隅が :abbr:`SVG` 原点（通常は左上隅）に写像。
  * :abbr:`SVG` はユーザー単位（画素）が画面画素に対応するように拡縮される。
  * :abbr:`SVG` が（属性 ``width``, ``height`` が定義する）ビューポートより大き
    い場合、スクロールバーが表示されることがある。

本書イラストは ``<object>`` による :abbr:`SVG` 配置方法の違いを示している。黒枠
以内の絵を注目する。一つ目のイラストはビューポートを比較するためのものだ。

.. csv-table::
   :delim: |
   :header: case, object width, object height, svg width, svg height, viewBox
   :widths: auto

   1 | 120 | 120 | 150 | 100 | undef
   2 | 120 | 120 | undef | undef | 0 0 150 100
   3 | undef | undef | 150 | 100 | undef
   3' | undef | undef | undef | undef | 0 0 150 100

いちばん自然に描画されているのは case 3 = case 3' で、余計な部分が見えていなく、
かつ絵の伸縮が生じていない。Case 1 では図形の伸縮はなく、原点も一致している。図
形の右側が見えない。図形の下側もブラウザーが描画する。Case 2 では図形全体が縮小
されて描画され、外側が見える。ブラウザー側ビューポート中央に収まっている。

二つ目のイラストは ``preserveAspectRatio`` の値の違いを説明するものだ。

   One possible value, not shown, is none in which case the :abbr:`SVG` is
   stretched to fit the viewport. The other possible values take the form:
   ``xAYB C``, where ``A`` and ``B`` can have the values ``Min``, ``Mid``, or
   ``Max``; and ``C`` can have the value ``meet`` or ``slice``. The values ``A``
   and ``B`` determine which part of the viewport and ``viewBox`` are aligned
   while the value of ``C`` determines if the image is scaled so that two edges
   of the ``viewBox`` coincide with the viewport while the other two are inside
   (``meet``) or if two edges of the ``viewBox`` coincide with the viewport
   while the other two are outside (``slice``).

上の段はすべて ``meet`` 型なので、指定辺でないほうの辺に関する描画は縦横比を維持
しつつ縮小されて ``<object>`` ビューポートに収まる。下の段はすべて ``slice`` 型
なので、拡大されてビューポートに収まらない図形の一部が切り落とされる。

属性 ``viewBox`` を設定する専用 UI は Inkscape に備わっていないが、XML Editor を
上手く使えば設定可能だ。

   To set the ``viewBox`` attribute in Inkscape: Open the :guilabel:`XML Editor`
   dialog and select the :abbr:`SVG` root element (``<svg:svg...>``). In an
   Inkscape created file, the ``width`` and ``height`` attributes will have been
   defined while the ``viewBox`` will not have been defined. -略- If it is not
   defined, click on the text entry box near the bottom of the window, in the
   same line as the :guilabel:`Set` button. Type in ``viewBox``. Then in the box
   below, type in four numbers separated by spaces, the *x* and *y* values of
   the upper-left corner (normally ``0`` and ``0``) and the *width* and
   *height*. The values are in user units (pixels). Click on the :guilabel:`Set`
   button or use :kbd:`Ctrl` + :kbd:`Enter` to register your values. Once the
   ``viewBox`` is defined, you can modify the ``width`` and ``height``
   attributes including deleting them or changing them to ``100%``.

属性 ``viewBox`` を定義したことで、他の属性変更により値が連動するようになる：

   Modifying the Width and Height in the :guilabel:`Document Properties` dialog
   will now modify the ``viewBox`` if ``width`` and ``height`` attributes are
   not defined in fixed units, otherwise it will modify the ``width`` and
   ``height`` attributes as well as proportionally modify the ``viewBox``
   attribute.

Adding Links
======================================================================

:abbr:`SVG` にもハイパーリンクの概念があり、:abbr:`HTML` のそれよりも複雑である
とのことだ。

   The :abbr:`SVG` specification uses XLinks, which are more powerful but also
   more complicated than the original :abbr:`HTML` links. We'll cover only the
   most simple use of *XLinks* here and refer you to the *XLink* specification
   from the *W3C* consortium for more details.

オブジェクトにリンクを追加することができるようだ。操作方法にクセがある：

   To add a link to an object, Right-Mouse Click on the object. Select
   :menuselection:`Add link` from the pop-up menu. Although nothing will seem to
   have happened, this will put an ``<svg:a>`` wrapper around the object
   (viewable with the :menuselection:`Edit --> XML Editor...` (:kbd:`Shift` +
   :kbd:`Ctrl` + :kbd:`X`) dialog).

   The link wrapper ``<svg:a>`` acts as a group. To edit a wrapped object, you
   must double-click on the object to enter the wrapper. It is also possible to
   create a wrapper within a wrapper by accident. Pay attention to the
   *Notification Region* or use the :menuselection:`Edit --> XML Editor...`
   (:kbd:`Shift` + :kbd:`Ctrl` + :kbd:`X`) dialog to keep track of what level
   you are at.

リンクがグループの構造であることを知らなければ、マウス操作時に混乱するところだっ
た。

   The attributes of an object's links can be modified through the
   :guilabel:`Link attributes` dialog that can be opened by selecting the
   :menuselection:`Link Properties` entry from the menu that pops up from a
   second Right-Mouse Click on the object (this time, you are clicking on the
   wrapper).

:guilabel:`Link` ダイアログを出して、オブジェクトにウェブページへのリンクを追加
するには：

   To link an object to another web page, only the :guilabel:`Href` attribute
   must be supplied. An example reference is ``http://www.w3.org/`` which is a
   link to the World Wide Web consortium.

本書のデモが壊れている。

   The following listing shows an :abbr:`SVG` file with a link from the blue
   square. It can be directly displayed in a web browser or included via the
   ``<object>`` tag in an :abbr:`HTML` or :abbr:`XHTML` file.

:abbr:`SVG` ファイルとして保存して、ブラウザーにドラッグアンドドロップして手軽に
試すといい。

   .. code:: xml

      <?xml version="1.0" encoding="UTF-8" standalone="no"?>
      <svg
         xmlns="http://www.w3.org/2000/svg"
         xmlns:xlink="http://www.w3.org/1999/xlink"
         version="1.1"
         width="150"
         height="150">
        <a xlink:href="http://www.w3.org/">
          <rect
           width="90"
           height="90"
           x="30"
           y="30"
           style="fill:#0000ff;fill-opacity:0.75;stroke:#000000"/>
        </a>
      </svg>

:guilabel:`Link attributes` ダイアログの項目を見ていく。

   Although the :guilabel:`Link attributes` dialog contains many entries, only a
   few are of great use. A couple have only one allowed value.

先述の XLink 仕様書を参照すれば正式な説明が確認できる。

Using Style Sheets
======================================================================

ここで言うスタイルシートとは :abbr:`HTML` を書くときに使うものと同じだ：

   :abbr:`SVG` drawings can use :abbr:`CSS` (Cascading Style Sheets) to control
   the presentation of the drawing objects. Support for style sheets is in its
   infancy in Inkscape. One can, however, do a few simple useful things.

コード例を引用する：

   .. code:: xml

      <svg
         xmlns="http://www.w3.org/2000/svg"
         xmlns:xlink="http://www.w3.org/1999/xlink"
         version="1.1"
         width="150"
         height="150">
        <style type="text/css">
         rect:hover {fill-opacity:1.0}
        </style>
        <a xlink:href="http://www.w3.org/"
           style="fill-opacity:0.75">
          <rect
           width="90"
           height="90"
           x="30"
           y="30"
           style="fill:#0000ff;stroke:#000000"/>
        </a>
      </svg>

このコード中の ``<style>...</style>`` 部分では ``<rect>`` 要素のマウスホバーで
``fill-opacity`` が最大になるようにしている。

一方、リンク要素 ``<a>...</a>`` 全体に（グループであるかのように考える）対して属
性 ``style`` で通常の ``fill-opacity`` が 75 パーセントであるように指示してい
る。

``<rect/>`` 要素ノードに対して属性 ``style`` で ``fill`` と ``stroke`` を直接設
定している。

では ``style`` 属性をどう設定するのか：

   The ``style`` attribute can either be added through a text editor or with a
   bit of difficulty through the Inkscape :guilabel:`XML Editor`
   (:menuselection:`Edit --> XML Editor...` (:kbd:`Shift` + :kbd:`Ctrl` +
   :kbd:`X`)) dialog.

上の例では属性の移動が必要だ：

   The ``fill-opacity`` attribute must be moved from the rectangle and put into
   a wrapper of the rectangle (in this case the ``<a>`` tag).

本書では XML Editor ダイアログでスタイルシートを追加する手順を挙げている。この節
をそのままチュートリアルとして利用できる。しかし最後の

   Save, but do NOT save as a plain :abbr:`SVG` file as this removes the ``hover``
   attribute from the :abbr:`CSS` style node. (Bug)

が気になる。

Adding JavaScript
======================================================================

オブジェクトの属性に JavaScript コードを置ける？

   :abbr:`SVG` drawings can use JavaScript (ECMAScript) to do complex
   manipulation of the objects in the drawing. In this example, the style sheet
   of the last example is replaced by simple JavaScript calls. The
   :guilabel:`Object Properties` dialog (:menuselection:`Object --> Object
   Properties...` (:kbd:`Shift` + :kbd:`Ctrl` + :kbd:`O`)) can be used to add
   the calls.

ダイアログのいちばん下に :guilabel:`Interactivity` という区画がある。

   To modify the previous example to use JavaScript, first remove the style
   section (use the :guilabel:`XML Editor` dialog). Next, open the
   :guilabel:`Object Properties` dialog. Select the square (make sure the square
   is selected and not the ``<a>`` wrapper, you can do this by first
   double-clicking the square and then clicking on it again). Then click on the
   triangle next to :guilabel:`Interactivity` in the :guilabel:`Object
   Properties` dialog to expose the JavaScript options.

マウスイベントハンドラー項目などが列挙されているので、JavaScript コードを直接記
入する：

   Add the following to ``onmouseover``: ``setAttribute('fill-opacity','1.0')``
   and the following to ``onmouseout``: ``setAttribute('fill-opacity','0.75')``.

仕上げは図面のファイル保存で、保存オプションを表示する保存コマンド、例えば
:menuselection:`File --> Save As...` などを実行して次のようにする：

   That's it! Do not save as :guilabel:`Plain SVG` as the JavaScript commands
   will be (erroneously) stripped out. You can save it as :guilabel:`Optimized
   SVG`.

ダイアログ画面。:guilabel:`Title` と :guilabel:`Description` を埋めておくのはい
い習慣だ：

   While the :guilabel:`Object Properties` dialog is open we can fill the
   ``title`` and ``desc`` attributes. These attributes can be specified for any
   object in an :abbr:`SVG` document, including *Groups*. The ``title``
   attribute is intended to be used for a tool tip. This is only implemented in
   some :abbr:`SVG` browsers like Opera. (Firefox 3.5 will put in the window
   title area the first title found in the document). The ``desc``
   (:guilabel:`Description`) attribute is used to store a description of the
   object. It is not normally intended for display.

ID も機械的なものから変えるのが良い：

   One final touch is to change the :guilabel:`Id` to a more descriptive name.

Simple Animation
======================================================================

まともな JavaScript コードを書く題材が来た。アニメーションだ。

   The :abbr:`SVG` standard provides support for animating drawings both
   internally through animation elements and externally through scripts. This
   section will demonstrate a simple animation using ECMAscript (a standard that
   JavaScript and JScript are dialects of).

ただし、Inkscape にはその対応がない。テキスト編集をすることにする。また、これま
で述べられたように、簡単なものならば既存の機能が対応している：

   Note that Inkscape added some limited support for scripts in v0.47 through
   the *Set Attributes* and *Transmit Attributes* extensions.

本書の例は正方形が左右に振動し続けるアニメーションだ。その上、これまでの機能も併
せ持つ：

   In the following :abbr:`SVG` drawing, the blue square oscillates back and
   forth (in a supporting :abbr:`SVG` viewer). The square still changes opacity
   when the mouse is over it and it still contains a hypertext link.

完全な :abbr:`SVG` コードが掲載されているが、要所に絞って見ていく。まずルート要
素だ：

   .. code:: xml

      <svg
         xmlns="http://www.w3.org/2000/svg"
         xmlns:xlink="http://www.w3.org/1999/xlink"
         version="1.1"
         onload="Start(evt)"
         width="150"
         height="150">

属性 ``onload`` は :abbr:`HTML` と同じ意味。このコードを実行する。関数 ``Start``
本体はこの次にある：

.. code:: xml

   <script type="text/ecmascript">
   <![CDATA[
     // -略-
     function Start(evt) {
       // -略-
       the_rect = evt.target.ownerDocument.getElementById("BlueRect");
       Oscillate();
     }

     function Oscillate() {
       // -略-
       the_rect.setAttribute("transform", "translate(" +x_pos+ ", 0.0 )");
       setTimeout("Oscillate()", delta_time)
     }

     window.Oscillate = Oscillate
   ]]>
   </script>

``<svg>`` 要素の子要素に ``<script>`` を定義し、JavaScript コードを普通に書く。

Inkscape for the Web
======================================================================

   This section focuses on ways to prepare Inkscape :abbr:`SVGs` for the web.

   A number of items have already been covered in this chapter. This section
   covers cleaning up the :abbr:`SVG` source.

掃除
   最終的に未使用になったデータを削除するコマンドがある。プログラミングで言うガ
   ベージコレクションのような操作を利用者自身で行う。

      As a drawing is created, items like *Gradients*, *Patterns*, *Markers*,
      and *Filters* are stored in the ``<defs>`` section of the :abbr:`SVG`
      file. If you later delete an object with, for example, a *Gradient*, the
      *Gradient* is not deleted.

   現行版では :menuselection:`File --> Clean Up Document` コマンドが相当する。

Save as Plain SVG
   図面を Inkscape 上でもはや編集しないのであればこのコマンドを使える。Inkscape
   固有のデータを削った上で :abbr:`SVG` ファイルを保存する。

      It can be removed by choosing the :guilabel:`Plain SVG` option in the
      drop-down menu in the :guilabel:`Save As` dialog.

Save as Optimized SVG
   保存オプションを細かく指定できる。

      Choosing :guilabel:`Optimized SVG` in the drop-down menu in the
      :guilabel:`Save As` dialog will pop-up a dialog that allows you to
      customize the saved :abbr:`SVG` file.

   :guilabel:`Optimized SVG Output` というダイアログが現れる。オプション名は本書
   と Inkscape 1.2 で異なるものがある。ここでは後者に合わせる。

   :guilabel:`Shorten color values`
      色全てを ``#rrggbb`` 形式、可能ならば ``#rgb`` 形式に書き換える。
   :guilabel:`Convert CSS attributes to XML attributes`
      ``style="fill:#ff0000"`` のような定義を ``fill="#ff0000"`` に書き換える。
      しかし：

         It will probably result in slightly larger files. If you plan on using
         :abbr:`CSS` to style objects, don't enable this option.
   :guilabel:`Embed rasters images`
      :abbr:`SVG` ファイルにビットマップデータを符号化して直接埋め込む。
   :guilabel:`Keep editor data`
      Inkscape 固有のデータを残すかどうか。
   :guilabel:`Enable viewboxing`
      これはオンにすると最適化方向からは離れるが、有用であることがある：

         If a ``viewBox`` attribute is not present, creates one using the
         ``width`` and ``height`` attributes, and then sets both ``width`` and
         ``height`` attributes to ``100%``. This is useful if you wish your
         :abbr:`SVG` file to automatically scale to use all available space on a
         web page.
   :guilabel:`Remove the XML declaration`
      ``<?xml version="1.0"?>`` を削るかどうかだった。
   :guilabel:`Number of significant digits for coordinates`
      Web 用途ではそこまで高精度の値は必要ない。

         Sets numerical precision on all coordinates and attributes. Drawings
         meant for the web rarely need precision greater than three or four
         decimal places.

      アプリケーション設定で低精度にしておく方法もある：

         You can also set the default numerical precision used by Inkscape in
         the Inkscape :guilabel:`Preferences` dialog in the :abbr:`SVG` output
         section (Numerical precision).
   :guilabel:`Indentation characters`
      :abbr:`XML` タグのインデント文字を選べる。

         Options are :guilabel:`Space`, :guilabel:`Tab`, and :guilabel:`None`.
         In all cases, each tag with attributes is placed on one line.

複製を優先する
   シンボリックリンク的複製は安い。

      References usually take up less file space than copies.
図面を単純にする
   微小オブジェクトを削除したり、描画領域の外部にオブジェクトを置かぬようにした
   り、パスのノード数を間引いたりしてデータ量を減らす。次のコマンドを利用しよ
   う：

   * :menuselection:`View --> DisplayMode --> Outline`
   * :menuselection:`Path --> Simplify`
