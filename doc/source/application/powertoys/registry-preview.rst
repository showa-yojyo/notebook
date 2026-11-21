======================================================================
Registry Preview 利用ノート
======================================================================

.. |regedit| replace:: :program:`regedit`
.. |regpre| replace:: `Registry Preview`_
.. |ui| replace:: :guilabel:`RegistryPreview`

本稿は PowerToys の |regpre| 機能に関する記述だ。

.. attention::

   :doc:`./index` 冒頭の前提条件に留意すること。

.. contents:: 見出し一覧
   :local:

概要
======================================================================

|regpre| は Windows レジストリーファイルエディターだと解釈できる。キーの検索機能
や、安全性確認機能が備わっている。

|ui| を開くには、Explorer で ``.reg`` ファイルを選択し、コンテキストメニューにあ
る

RegistryPreview ウィンドウ
======================================================================

|ui| ウィンドウの構成は次のようなものだ：

* ツールバー
* エディター領域
* ツリービュー領域
* キーの値領域

ツールバーの構成は次のとおり：

:guilabel:`New`
   割愛。
:guilabel:`Open...`
   割愛。
:guilabel:`Reload`
   レジストリーファイルを |ui| にロードし直す。ファイル内容を外部で変更した場合
   に意味があるコマンドだ。
:guilabel:`Save`
   割愛。
:guilabel:`Save as...`
   割愛。
:guilabel:`Edit`
   レジストリーファイルの内容をメモ帳で開く。含む値によってはエラーが生じる。
:guilabel:`Write to Registry`
   ビューワーにある内容をレジストリーに書き込む。
:guilabel:`Open Registry Editor`
   |regedit| が開く。
:guilabel:`Open Key`
   ツリービューで強調されているキーの位置を基に |regedit| が開く。

エディター領域ではレジストリーファイルの生の内容を編集する。一般のテキストエディ
ターで ``.reg`` ファイルを編集するのと同じ。

.. admonition:: 利用者ノート

   |regpre| の素晴らしい点は、この編集中にレジストリーファイルとして不正な形式に
   なった瞬間に、ツリービューや値ビューで Error がはっきりと示されることだ。

ツリービューはファイルに含まれるレジストリキーの木表現だ。この表現はエディターで
のファイル内容編集と連動する。この木表現において、レジストリキーを選択すると、そ
のキーの値が下部にある領域に示される。

設定
======================================================================

:guilabel:`Enable Registry Preview` を On にしないと |regpre| 機能は使用可能にな
らない。これにより、Windows Explorer の ``.reg`` ファイルに関するコンテキストメ
ニューに :menuselection:`Registry Preview` が現れる。

Open
----------------------------------------------------------------------

:guilabel:`Open Registry Preview`
   ここをクリックすると |ui| ウィンドウが直接開く。
:guilabel:`Make Registry Preview the default app for .reg files`
   このスイッチを On にすると、Explorer で拡張子 ``.reg`` のファイルを開くときに
   |ui| ウィンドウで開かれるようになる。Explorer コンテキストメニューの
   :guilabel:`開く` のアイコンが |regpre| のものになるはずだ。

   これは On にしておきたい。レジストリーファイルを誤って実行する確率が格段に下
   がる。

.. _Registry Preview: https://learn.microsoft.com/en-us/windows/powertoys/registry-preview

.. 以上
