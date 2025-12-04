======================================================================
File Explorer add-ons 利用ノート
======================================================================

File Explorer add-ons は Windows Explorer のプレビュー表示を拡張する。ファイルの
サムネイル表示とプレビューウィンドウに現在選択中のファイルの内容が反映される。例
えば Markdown ファイル、SVG ファイルのプレビューができるようになる。

.. attention::

   :doc:`./index` 冒頭の前提条件に留意すること。

.. contents:: 見出し一覧
   :local:

設定
======================================================================

PowerToys 自体の稼働と共に File Explorer add-ons 機能も稼働するらしい。

.. _anchor-add-ons-preview:

Preview Pane
----------------------------------------------------------------------

Explorer の :menuselection:`表示 --> プレビューウィンドウ` の機能を強化する。
Markdown, SVG, PDF, G-code, 各種ソースコードファイルにも対応する。

設定画面には上述のファイルタイプごとに有効無効スイッチが用意されているので、それ
ぞれ好みでオンオフを設定する。:guilabel:`Source code files` はさらにオプションが
ある：

:guilabel:`Wrap text`
   On にすると、ファイルの内容をプレビュー区画右端で改行するように出力する。好み
   で Off にする。
:guilabel:`Try to format the source for preview`
   On にすると、Markdown および XML ファイルの内容を整形したものをプレビュー区画
   に出力するようになる。
:guilabel:`Maximum file size to preview`
   巨大なテキストファイルのプレビューを無条件で認めるわけにはいかないようで、容
   量に上限を設けなければならない。
:guilabel:`Font size`
   フォントはわからぬが寸法を設定することが可能。
:guilabel:`Enable sticky scroll`
   Visual Studio Code のそれのようなスクロールモードを有効にする。例えば JSON
   ファイルならばスコープの釣り合いがわかりやすくなる。
:guilabel:`Show minimap`
   Visual Studio Code のそれのような地図を右上に示すようになる。

.. admonition:: 利用者ノート

   驚いたことに STL ファイルや OBJ ファイルもプレビュー表示対応している。Utah
   ティーポットのデータをマウスドラッグで回転させることすら可能だ。

Thumbnail icon Preview
----------------------------------------------------------------------

サムネイルの表示自体は Windows Explorer の内蔵機能だ。PowerToys はそれに対して
SVG, PDF, G-code, STL ファイル用のプレビューを実装している。

設定画面にこれらのファイルタイプごとに有効無効スイッチが用意されているので、それ
ぞれ好みでオンオフを設定する。

.. admonition:: 利用者ノート

   サムネイルにならない場合は、Explorer のフォルダーオプションがアイコン表示固定
   になっているはずだ。:menuselection:`表示 --> 詳細設定` からチェックボックス
   :guilabel:`常にアイコンを表示し、縮小版は表示しない` をオフにすると絵が出る。

.. 以上
