======================================================================
Chapter 4. Editing Basics
======================================================================

.. contents::

Undo and Redo
======================================================================

*Undo*
  :メニュー: :menuselection:`Edit --> Undo`
  :キーバインド: :kbd:`Ctrl` + :kbd:`Z` または :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`Y`
  :ツールバー: *Commands Bar*
*Redo*
  :メニュー: :menuselection:`Edit --> Redo`
  :キーバインド: :kbd:`Ctrl` + :kbd:`Y` or :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`Z`
  :ツールバー: *Commands Bar*

キーバインドの対称性に注目したい。ズーム操作のマウスクリックでも同様の設計が見ら
れる。

   Multiple changes can also be undone or redone in one step by using the
   :guilabel:`Undo History` dialog.

:guilabel:`History`
   :メニュー: :menuselection:`Edit --> History...`
   :キーバインド: :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`H`

基本的には文書に対する操作履歴がリスト形式で表示されるのだが、気が利いていること
にツリー状になる部分もある：

   Consecutive changes of the same type may be collapsed to one line to improve
   readability; the number of such changes is given on the top line of the
   group. Clicking on the triangle collapses (left) or uncollapses (right) the
   list.

文書全体に対する変更を取り消すという意味で *Revert* コマンドの存在を思い出せるよ
うにすること。

Selecting Objects
======================================================================

オブジェクトを選択するにはかなりの数の手段がある。最も普通な方法は Select Tool だ。
次のいずれかの方法で発動する：

* :kbd:`F1` を押す
* :guilabel:`Toolbox` 内矢印ボタン（先頭にあるボタン）をクリックする

オブジェクトによっては、他の Tool で直接選択可能だ。Rectangle Tool などが該当す
る。選択とは少し違うかもしれないが、オブジェクトをダブルクリックするとそれの編集
モードに変わる。

オブジェクトを同時に複数選択することができる。選択状況が画面下部に随時通知される。

.. admonition:: 読者ノート

   Locked Objects および Hidden Objects については保留して先を急ぐ。

Selecting with the Mouse
----------------------------------------------------------------------

:abbr:`CAD` アプリケーションと同様に、オブジェクトの絵にマウスカーソルを移動させ
てクリックしたりドラッグしたりすることで、その位置や領域にあるオブジェクトを選択
したり解除したりする。まずはクリックから見ていく。

* 単純なクリックでオブジェクト一つを選択する。
* :kbd:`Shift` を押しながらのクリックは、選択状態を反転する。選択と解除を繰り返
  す。
* :kbd:`Alt` を押しながらのクリックは、「下」オブジェクトを選択する。このような
  選択を繰り返して最下層まで到達すると、選択対象が最上層オブジェクトに戻る。

次にドラッグによる選択を下にまとめる。

* 左ボタンドラッグで矩形領域選択。この矩形内に完全に含まれているオブジェクトが選
  択される。
* :kbd:`Shift` を押しながらの左ボタンドラッグは上記の「追加的」版。
* :kbd:`Alt` を押しながらの左ボタンドラッグは矩形選択ではない。マウスの軌跡に交
  差するオブジェクトを順次選択していく。

     This is very useful when needing to select multiple paths as found in
     engravings or hair.

* :kbd:`Shift` + :kbd:`Alt` を押しながらの左ボタンドラッグは上記の「追加的」版。

Selecting with the Keyboard
----------------------------------------------------------------------

キーボードのほうが操作しやすい選択コマンドもある。表にまとめる：

.. csv-table::
   :delim: #
   :header: キーバインド,コマンド
   :widths: auto

   :kbd:`Tab` # Z オーダーで上のオブジェクトを選択
   :kbd:`Shift` + :kbd:`Tab` # Z オーダーで下のオブジェクトを選択
   :kbd:`Ctrl` + :kbd:`A` # Select All
   :kbd:`Ctrl` + :kbd:`Alt` + :kbd:`A` # Select All in All Layers
   :kbd:`!` # Invert Selection
   :kbd:`Alt` + :kbd:`!` # Invert
   :kbd:`Esc` # Deselect

断りのないコマンドについては現在レイヤー内オブジェクトが対象となる。また、非表示
であるか、ロックされているレイヤー上のオブジェクトは選択されない。

Selecting with the Find Dialog
----------------------------------------------------------------------

Inkscape は文書が :abbr:`SVG` つまり :abbr:`XML` であることを利用した検索機能も
用意している。:menuselection:`Edit --> Find...` や :kbd:`Ctrl` + :kbd:`F` で検索
ダイアログを表示できる。UI を見れば機能は理解できると思うので、ノートは省略。

Copying, Pasting, and Deleting Objects
======================================================================

   Inkscape uses the system-wide clipboard (a place where a description of one
   or more objects is stored temporarily in memory). You can copy and paste
   between different instances of Inkscape and other applications that support
   :abbr:`SVG`.

クリップボード系コマンドは異なる :abbr:`SVG` を編集していたり、例えばテキストエディター
で編集していたりするときにその活用が考えられる。

次のコマンドだけは通常編集時にも有用なので、記しておく：

.. csv-table::
   :delim: #
   :header: コマンド,キーバインド,挙動
   :widths: auto

   :menuselection:`Edit --> Duplicate` # :kbd:`Ctrl` + :kbd:`D` # オブジェクトを即時コピー
   :menuselection:`Edit --> Paste Style` # :kbd:`Shift` + :kbd:`Ctrl` + :kbd:`V` # オブジェクトにスタイルを上書き
   :menuselection:`Edit --> Delete` # :kbd:`Delete` # オブジェクトを即時削除

:menuselection:`Edit --> Paste Size` という変種もあるようだ。

Clones
======================================================================

   Cloning is a special way to copy an object. The cloned copy retains a link to
   the original object so if that object is changed, the clone will change in
   the same way.

UNIX でいうと :command:`cp` に対する :command:`ln -s` の考え方に相当する。

   Inkscape has the ability to “relink” clones to a another object. To do this,
   copy the new “original” to the clipboard.

これは知らなかった。応用例を知りたい。

タイリングを除く複製コマンドを表にまとめる：

.. csv-table::
   :delim: #
   :header: コマンド,キーバインド,挙動
   :widths: auto

   :menuselection:`Edit --> Clone --> Create Clone` # :kbd:`Alt` + :kbd:`D` # 複製し、元の真上に配置する。
   :menuselection:`Edit --> Clone --> Unlink Clone` # :kbd:`Shift` + :kbd:`Alt` + :kbd:`D` # 複製関係を廃止する。
   :menuselection:`Edit --> Clone --> Relink to Copied` # n/a # 後述
   :menuselection:`Edit --> Clone --> Select Original` # :kbd:`Shift` + :kbd:`D` # 複製元を選択する。

.. admonition:: 利用者ノート

   :kbd:`Alt` + :kbd:`D` が効かない？

コマンド *Relink to Copied* は複製の参照元を自身の別の複製に設定し直すものらし
い。UNIX の例えを繰り返すと、:command:`ln -s` からの :command:`ln -fs` に相当す
る。別のオブジェクトを指定するのに :menuselection:`Edit --> Copy` を要し、操作に
癖がある。用途がわからないので、私が使うことはなさそうだ。

複製オブジェクトと元オブジェクトを同時に操作するとややこしいことになるから控える。

Ordering Objects (Z-Order)
======================================================================

   The z-order determines the order in which objects are drawn on the canvas.
   Those object with high z-order are drawn last and therefore drawn on top of
   objects with lower z-order. The order is determined by the order that the
   objects are listed in the :abbr:`SVG` file.

後半の記述が特に重要だ。:abbr:`SVG` の直接編集で z-order を調整できることを意味
する。

オブジェクトの z-order を画面で操作するにはキーボードを使うのが最良と思われる：

.. csv-table::
   :delim: #
   :header: コマンド,キーボード,挙動
   :widths: auto

   :menuselection:`Object --> Raise` # :kbd:`PgUp` # z-order を一段階上げる
   :menuselection:`Object --> Lower` # :kbd:`PgDn` # z-order を一段階下げる
   :menuselection:`Object --> Raise to Top` # :kbd:`Home` # z-order を最上層に上げる
   :menuselection:`Object --> Lower to Bottom` # :kbd:`End` # z-order を最下層に上げる

Groups
======================================================================

   A set of objects can be collected into a *Group*. Once placed in a *Group*,
   the objects can be manipulated together, the *Group* acting as a single
   object. *Groups* can be nested; that is, a *Group* can be combined with other
   *Groups* or objects to make a higher level *Group*.

ところで、任意のオブジェクトが包含関係のないグループ二つに同時に所属することはあ
り得るだろうか。

   Objects within *Groups* can be edited and manipulated without breaking up the
   *Group*.

グループ内のオブジェクトを、キー操作と左クリックを絡めて選択することが可能だ。

* :kbd:`Ctrl` を押しながら左クリックで、グループ内のオブジェクトを選択する。この
  コマンドは、オブジェクトが何階層のグループに埋もれていても機能する。
* :kbd:`Ctrl` + :kbd:`Alt` を押しながら左クリックで、グループ内に下のオブジェク
  トを選択する。例によって、最下層のオブジェクトでは最上層のオブジェクトを選択す
  る。
* :kbd:`Shift` + :kbd:`Ctrl` + :kbd:`Alt` を押しながら左クリックで、グループ内で
  オブジェクトの選択状態を切り替える。

   A *Group* can be entered or turned into a temporary *Layer* for editing.

グループに対して入ったり出たりするという操作概念が存在する。このときに生じる一時
的な操作に関して閉じた構造をレイヤーと言っているのだろう。

* 左ダブルクリックで、またはそのグループに入る。空クリックでそこから出る。
* :kbd:`Ctrl` + :kbd:`Enter` でグループに入る。:kbd:`Ctrl` + :kbd:`BackSpace`
  でグループから出る。これらは入れ子グループ用操作だろう。
* 右クリックでグループに対するコンテキストメニューを表示する。

他にも高度な操作があるが割愛。

Layers
======================================================================

Inkscape におけるレイヤー概念は、Photoshop などのアプリケーションにおけるそれと
似ている。同じと言ってもいいかもしれない。

   Internally, *Layers* are just :abbr:`SVG` *Groups* with a few extra Inkscape
   specific parameters that Inkscape uses to control the *Layer* interface. Like
   *Groups*, *Layers* can contain sub-*Layers*.

Layers Dialog
----------------------------------------------------------------------

:guilabel:`Layers` ダイアログは :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`L` で表示を切
り替えるのが楽だろう。たいへんよく用いる。

本書の画像とバージョン 1.2 の UI はだいぶ異なるが、だいたい通用する。文書内のレ
イヤーの配列がツリービューとして表現される。

* 目アイコンでレイヤー表示状態を切替可能
* 錠前アイコンでレイヤー施錠状態を切替可能
* レイヤーノードまたはオブジェクトノードを

  * 右クリックでコンテキストメニュー出現
  * 左ダブルクリックで名称変更可能

* ダイアログ上部のツールバー部分で次の操作ができる：

  * ツリービューとリストビュー（レイヤーのみ一覧する）を切り替える
  * レイヤーを追加する
  * 指定レイヤーまたは指定オブジェクトの z-order を上下する
  * 指定レイヤーまたは指定オブジェクトを削除する

.. admonition:: 利用者ノート

   レイヤーのブレンドモード操作 UI が見当たらない？

Layers Menu
----------------------------------------------------------------------

メインメニューの :menuselection:`Layer` 以下にレイヤー操作コマンド項目がある：

.. csv-table::
   :delim: #
   :header: コマンド,キーバインド,補足
   :widths: auto

   :menuselection:`Layer --> Layers and Objects...` # :kbd:`Shift` + :kbd:`Ctrl` + :kbd:`L` # 前述
   :menuselection:`Layer --> Add Layer...` # :kbd:`Shift` + :kbd:`Ctrl` + :kbd:`N` # レイヤー作成ダイアログボックスが出現する
   :menuselection:`Layer --> Rename Layer...` # n/a # ミニダイアログボックス出現
   :menuselection:`Layer --> Show/Hide Current Layer` # n/a #
   :menuselection:`Layer --> Lock/Unlock Current Layer` # n/a #
   :menuselection:`Layer --> Switch to Layer Above` # :kbd:`Ctrl` + :kbd:`PgUp` # 現在レイヤーを変更
   :menuselection:`Layer --> Switch to Layer Below` # :kbd:`Ctrl` + :kbd:`PgDn` #
   :menuselection:`Layer --> Move Selection to Layer Above` # :kbd:`Shift` + :kbd:`PgUp` # オブジェクトの所属レイヤーを変更
   :menuselection:`Layer --> Move Selection to Layer Below` # :kbd:`Shift` + :kbd:`PgDn` #
   :menuselection:`Layer --> Move Selection to...` # n/a # :guilabel:`Move to Layer` ダイアログ出現
   :menuselection:`Layer --> Layer to Top` # :kbd:`Shift` + :kbd:`Ctrl` + :kbd:`Home` # レイヤー z-order 操作
   :menuselection:`Layer --> Raise Layer` # :kbd:`Shift` + :kbd:`Ctrl` + :kbd:`PgUp` #
   :menuselection:`Layer --> Lower Layer` # :kbd:`Shift` + :kbd:`Ctrl` + :kbd:`PgDn` #
   :menuselection:`Layer --> Layer to Bottom` # :kbd:`Shift` + :kbd:`Ctrl` + :kbd:`End` #
   :menuselection:`Layer --> Duplicate Current Layer` # n/a #
   :menuselection:`Layer --> Delete Current Layer` # n/a #

Status Bar
----------------------------------------------------------------------

ステータスバーに現在のレイヤーとその表示状態、施錠状態を確認できる小さい領域があ
る。旧バージョンのほうが機能性があったようだ？
