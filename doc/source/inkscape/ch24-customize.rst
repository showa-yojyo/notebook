======================================================================
Chapter 24. Customization
======================================================================

.. contents::

この章はもっと前に持ってきてもいいかもしれない。

   The easiest way to make customizations is through the Inkscape
   :guilabel:`Preferences` dialog. More extensive customizations can be made by
   modifying files in or adding files to the Inkscape preferences directories.
   The directory for changes shared by all users is :file:`share/inkscape`. The
   directory for personal changes is :file:`~/.config/inkscape/` on Linux or
   :file:`%userprofile%\\Application Data\\Inkscape\\` on Windows.

Windows 10 の場合のパスは :file:`%APPDATA%\\Roaming\\inkscape` だと思う。

Inkscape Preferences Dialog
======================================================================

これまでざんざん言及されている設定ダイアログだ：

   Inkscape is most easily customizable through the Inkscape
   :guilabel:`Preferences` dialog (:file:`File --> Inkscape Preferences...`
   (:kbd:`Shift` + :kbd:`Ctrl` + :kbd:`P`)).

重要なオプションの復習：

   It is worthwhile to scan through the options under each entry. The most
   important options have already been mentioned in the text. They include:
   Setting the :guilabel:`Rotation snap angle` and other scaling parameters
   under the :guilabel:`Step` entry;

Inkscape 1.2 では :menuselection:`Behavior --> Steps` ページの
:guilabel:`Rotation snaps every` ドロップダウンメニューに相当する。値は 90 の約
数にするのが自然だと思うが、一覧をチェックしたところ 36 とかある。

   determining if transformations should be :guilabel:`Optimized` or
   :guilabel:`Preserved` under the :guilabel:`Transforms` entry;

同じく :menuselection:`Behavior --> Transforms` ページの :guilabel:`Store
transformation` オプションのことだ。属性 ``transforms`` を割り当てるか否かを決め
るものだ。

   and setting the :guilabel:`Default export resolution` under the
   :guilabel:`Misc` entry.

これは :menuselection:`Imported Images` ページの :guilabel:`Export` 区画にある。

   All the preferences are stored in the file :file:`preferences.xml` located on
   Linux at :file:`~/.config/inkscape/` and on Windows at
   :file:`%userprofile%\\Application Data\\Inkscape\\`.

設定内容は上記のフォルダーにある :file:`preference.xml` に保存される。冒頭に記し
たように、Windows 10 の場合のパスはそことは異なる。

   There are quite a few preferences, some undocumented, that are accessible
   only by hand-editing this file.

この手の項目を多く知っているといいことがあるだろうか。

Inkscape Configuration Files
======================================================================

* :file:`templates` サブフォルダーに新テンプレを追加することができる。
* :file:`palettes` サブフォルダーに新スウォッチを追加することができる。ファイル
  フォーマットは GIMP と共通のもの。
* :file:`markers/markers.svg` マーカー追加
* :file:`share/keys/defaults.xml` ショートカットキー。

   Inkscape can be fully customized through the configuration files, usually
   located in the :file:`share/inkscape` directory (:file:`/usr/share/inkscape`
   in Linux).

システムレベルカスタマイズということだな。

Preferences
----------------------------------------------------------------------

設定ダイアログでは設定不能なオプションを見ていく。

Alternative Alt Key
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Some window managers use :kbd:`Alt` + Left Mouse Drag and :kbd:`Alt` + Left
   Mouse Click for their own purposes, thereby preventing Inkscape from
   receiving the mouse input.

Windows 版 Inkscape は上記操作に関して変なことが起こらない。気にしない。

Outline Mode Colors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   You can specify the colors used in the *Outline Mode* in the group
   ``id="wireframecolors"`` section. Colors are specified in decimal form
   (converted from a rgba hexadecimal value to base ten).

:file:`preferences.xml` の実際の内容を記すとわかりやすい：

.. code:: xml

   <group
      id="wireframecolors"
      onlight="255"
      ondark="4294967295"
      images="4278190335"
      clips="16711935"
      masks="65535" />

.. csv-table::
   :delim: |
   :header: 属性,意味
   :widths: auto

   ``onlight`` | 描線が明るい背景をまたぐときの色
   ``ondark`` | 描線が暗い背景をまたぐときの色
   ``images`` | 像の輪郭色
   ``clips`` | クリップパス色
   ``masks`` | マスク色

面白いのは、Inkscape 起動時点でアウトラインモードにする設定方法があることだ：

   You can force Inkscape to start up in *Outline Mode* by changing the value of
   outline in the group ``id="startmode"`` to 1.

SVG Output
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A number of preferences control the way content is written to the :abbr:`SVG`
   files. They can be found in the group ``id="svgoutput"`` section. Most can
   also be found in the :abbr:`SVG` output section of the Inkscape
   :guilabel:`Preferences` dialog.

こちらは :file:`preferences.xml` をテキストエディターで編集する必要性は低いよう
だ。

.. csv-table::
   :delim: |
   :header: 属性,意味
   :widths: auto

   ``usenamedcolors`` | ``blue``, ``black`` などのキーワードを使うか 16 進数表記を使うか
   ``numericalprecision`` | 数値に対して書き出される有効数字の桁数
   ``minimumexponent`` | :math:`{10^x}` までの正の値をゼロとみなす（指数は負）
   ``indent`` | :abbr:`SVG` ファイル内タグの入れ子レベルの空白文字数
   ``inlineattrs`` | 属性を同じ行に置くか改行で区切るか

Custom Templates
----------------------------------------------------------------------

テンプレートは重要なので習得すること。

   New drawing templates can be added by adding new files to the directory
   :file:`share/inkscape/templates` (for system-wide use) or to the
   :file:`templates` subdirectory in your Inkscape preferences directory.

まずは後者のディレクトリーだけを使えばいい。

   The :file:`templates` directory is listed under the :guilabel:`Places` part
   of the :guilabel:`Save As` dialog.

この UI は少なくとも Windows 版では確認できない。

既定のテンプレートは特別に扱われる：

   You can directly save any :abbr:`SVG` file to this directory. Saving the file as
   :file:`default.svg` will replace your current default template.

よく使う描画要素の集合をあらかじめ作成しておいたものをテンプレートファイルとして
配置するのが基本的だ：

   Objects, gradients, patterns, and so forth, can be added to an empty Inkscape
   :abbr:`SVG` file and then saved and placed in the :file:`templates`
   directory. When that file is selected in the list of templates, you will have
   access to all the objects, gradients, and patterns you previously defined.

Custom Swatches or Palettes
----------------------------------------------------------------------

ただしパレットはテンプレートファイルではなく、専用形式でカスタマイズを配置でき
る：

   You can add custom *Swatches* (*Palettes*) to Inkscape by adding the
   appropriate files under the :file:`share/inkscape/palettes` directory.

GIMP とファイル形式が同じなので、シンボリックリンクで共有させる管理方法が考えら
れる：

   The file format follows the Gimp palettes file format so palettes can be
   shared between the two programs.

   The file format is very simple, as the following example five-color palette
   file shows.

   .. code:: text

      GIMP Palette
      Name: MyPalette
      #
        0   0   0 Black
      255   0   0 Red
        0 255   0 Green
        0   0 255 Blue
      255 255 255 White

* 一行目は ``GIMP Palette`` 固定。
* 二行目はパレット名を示す。この名前が Inkscape UI で使われる。
* ``#`` から始まる行は行末までコメント。
* あとはスウォッチ定義が続く。

     There is one color per line. Each color is defined as three numbers
     representing the values of red, green, and blue followed by a name (shown
     when the cursor hovers over the swatch). The range of values is 0-255,
     where 255 means that the corresponding color is fully turned on.

Custom Markers
----------------------------------------------------------------------

オリジナル描線マーカーを使う方法もある：

   It is possible to add custom markers to Inkscape by editing the file
   containing the marker definitions :file:`share/inkscape/markers/markers.svg`.

本書のデモ。おそらく Inkscape であらかじめ well-defined なパスオブジェクトを作成
し、その :abbr:`SVG` タグ以下を ``<marker>...</marker>`` 部分にコピー＆ペースト
して用意すると考えられる：

   Here is the definition needed to add a “diamond node” marker. It differs from
   the diamond markers included with Inkscape in that the center of the diamond
   is gray and the orientation doesn't depend on the slope of the lines.

   .. code:: xml

      <marker style="overflow:visible;"
         id="DiamondNode"
         refX="0.0"
         refY="0.0"
         orient="0.0"
         inkscape:stockid="DiamondNode">
        <path
           transform="scale(0.8) rotate(180)"
           style="fill-rule:evenodd;stroke:#000000;fill:#BFBFBF;
                  stroke-width:0.5pt;marker-start:none;"
           d="M 0.0,2.5 L 2.5,0.0 L 0.0,-2.5 L -2.5,0.0 L 0.0,2.5 z "
           id="path1234"
           sodipodi:nodetypes="ccccc" />
      </marker>

マーカーの構造を知るには :abbr:`SVG` 仕様書を当たる。

Custom Keyboard Shortcuts
----------------------------------------------------------------------

キーバインドも設定ファイルでカスタマイズ可能。

   You can change the keyboard shortcuts used by Inkscape by editing or
   replacing the file :file:`share/keys/defaults.xml`.

既定のキーバインド集合をファイル名置換により挿げ替える方法でカスタマイズする：

   There are a number of alternative shortcuts available. To use them, simply
   rename the file to :file:`defaults.xml`.

Inkscape が用意しているキーバインド定義 :abbr:`XML` ファイルは Windows ならば
:file:`%PROGRAMFILES%\\Inkscape\\share\\inkscape\\keys` 以下にある。

.. csv-table::
   :delim: |
   :header: ファイル,キーバインド
   :widths: auto

   :file:`acd-canvas.xml` | ACD Systems Canvas 11
   :file:`adobe-illustrator-cs2.xml` | Adobe Illustrator
   :file:`carbon.xml` | Inkscape carbon MacOSX
   :file:`corel-draw-x4.xml` | Corel DRAW
   :file:`corel-draw-x8.xml` | Corel DRAW X8
   :file:`default.xml` | Inkscape default
   :file:`inkscape.xml` | Inkscape default
   :file:`macromedia-freehand-mx.xml` | Macromedia Freehand
   :file:`right-handed-illustration.xml` | Right Handed Illustration
   :file:`xara.xml` | Xara
   :file:`zoner-draw.xml` | Zoner Draw

Right Handed Illustration が面白い：

   for use in drawing on a tablet with a stylus held by the right hand; most
   commonly keyboard shortcuts are accessible with the left hand

ところで、ユーザー設定はシステム設定に優先する。使いたいキーバインドを自分の設定
ファイルに定義するのは安全だ：

   You can also add shortcuts to a :file:`keys/defaults.xml` in your Inkscape
   preferences directory. These will override any shortcuts defined in the
   system-wide :file:`defaults.xml` file. See the comments in the default file
   for more details.

キーバインドカスタマイズの枠組みがあるということは、コマンドを文字列で表現する手
段が用意されているということでもある：

   One particularly handy shortcut customization is to bind often-used
   *Extensions* to keys. Here is an example of binding the / key to the *Add
   Nodes* extension:

   .. code:: xml

      <?xml version="1.0"?>
      <keys name="My Customization">
        <bind key="slash" action="org.ekips.filter.addnodes" display="true"/>
      </keys>

属性 ``action`` の有効な値一覧が個人的に欲しい。
