======================================================================
Peek 利用ノート
======================================================================

本稿は PowerToys の Peek_ 機能に関する記述だ。

.. attention::

   :doc:`./index` 冒頭の前提条件に留意すること。

.. contents:: 見出し一覧
   :local:

使い方
======================================================================

Windows Explorer でファイルを一つ選択し、Peek_ 機能発動キーを押す。するとビュー
ワーが開く。ファイルの種類を考慮したプレビューが実現する。画像、音楽、ビデオファ
イルを選択するならば、それぞれでプレビューウィンドウに適切なコントローラーが備
わっている。

プレビューウィンドウ
======================================================================

ファイルを Peek_ ウィンドウでプレビューするときの特徴を記す。

* 矢印キーを押すと、プレビュー対象が Explorer でいう前や後ろのファイルに移る。
* :guilabel:`Open with...` をクリックするか :kbd:`Enter` を押すと、対象ファ
  イルが既定のプログラムで開く。
* :guilabel:`Pin the window...` が効いているように思えない。
* プレビュー領域にマウスカーソルを hover すると、対象ファイルの属性がツールチッ
  プに示される。
* :guilabel:`Del` を押すと :guilabel:`Delete file?` ポップアップが開く。

コマンドライン版
======================================================================

CLI で運用したい場合、:program:`PowerToys.Peek.UI.exe` を用いることが可能だ。例
えば WSL Ubuntu で :program:`wslview` の代わりに用いると使い勝手が良くなるかもし
れない。

.. admonition:: 利用者ノート

   Peek_ を :program:`winget install --scope=machine` でインストールした場合、こ
   のプログラムは次のパスに存在する：

   .. sourcecode:: text

      C:\Program Files\PowerToys\WinUI3Apps

設定
======================================================================

:guilabel:`Enable Peek` を On にすれば _Peek 機能自体が有効になる。プレビューの
出し方については Activation 構成で決定される。

Activation
----------------------------------------------------------------------

:guilabel:`Activation method`
   ファイルを選択したあと、どうすればプレビューを出してよいのかを指定する。

   * :guilabel:`Custom shortcut`: 下記ショートカット入力によって出す。こちらを採
      りたい。
   * :guilabel:`Spacebar`: :kbd:`Space` 押しでプレビューを出す。

   :guilabel:`Activation shortcut`
      :kbd:`Ctrl` + :kbd:`Space` が既定値。

Behavior
----------------------------------------------------------------------

:guilabel:`Always run without elevation (even if PowerToys is elevated)`
   On が望ましい。
:guilabel:`Automatically close the Peek window after it loses focus`
   :guilabel:`Peek` ウィンドウが自動的に消えるのが嫌なので Off にする。
:guilabel:`Confirm before deleting files`
   Off にすると、プレビュー中に :guilabel:`Del` を押したときに対象ファイルがゴミ
   箱へ直行する。

Preview
----------------------------------------------------------------------

:guilabel:`Source code files (Monaco)`
   オプション名はソースファイルだが、テキストファイル全般と考えるほうがいいか。

   ここにある項目群はそれぞれ File Explorer add-ons の :ref:`Preview
   Pane<anchor-add-ons-preview>` にある同名項目と同様だ。

.. _Peek: https://learn.microsoft.com/en-us/windows/powertoys/peek

.. 以上
