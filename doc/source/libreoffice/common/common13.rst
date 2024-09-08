======================================================================
Chapter 13, Customizing LibreOffice ノート
======================================================================

.. include:: ./common-inc.txt

.. contents:: 章見出し
   :depth: 2
   :local:

Introduction
======================================================================

この章では次のような改造について説明する：

* LibreOffice のメニュー、ツールバー、キーバインド、タブインターフェイス
* メニューやツールバーを追加したり、イベントにマクロを割り当てたりする
* さまざまな |UI| の変種を選択して使用する

改造は LibreOffice Web サイトまたは他の供給人からインストールできる拡張機能を追
加することでも行える。TODO を見ろ。

.. note::

   改造したメニューとツールバーは雛形に保存可能だ。改造物は文書に作成され、その
   文書が雛形として保存される。詳しくは :doc:`common04` を見ろ。

Menu customization
======================================================================

|MenuBar| やコンテキストメニューのメニューやコマンドは、追加、並べ替え、削除など
の変更が可能だ。メニューを改造するには、|MenuBar| |CustomizeM| を選択し
|MenusTab| または |ContextMenusTab| を選択する。これらのタブは似ている。

Customizing existing menus
----------------------------------------------------------------------

本文の説明は Writer のメニューを改造する例だが、他の LibreOffice アプリケーショ
ンのメニューも同様の手順で改造可能だ。

.. _common13-anchor-A:

Adding commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. |TargetL| replace:: :guilabel:`&Target` ドロップダウンリスト
.. |AssignedCommandsL| replace:: :guilabel:`&Available Commands` 一覧
.. |AvailableCommandsL| replace:: :guilabel:`&Available Commands` 一覧

#. |CustomizeM| で |CustomizeDlg| を開く。
#. |MenusTab| をクリックしてページを開く。:guilabel:`S&cope` ドロップダウンリス
   トで `LibreOffice Writer` が現れている。
#. |TargetL| から改造するメニューを選択する。このドロップダウンリストは選択メ
   ニューで使用可能なサブメニューも含む。
#. |AssignedCommandsL| に選択メニューに必要なコマンドがないことを確認する。一覧
   をスクロールする必要があるかもしれない。
#. 必要に応じて、:guilabel:`&Search` 欄にコマンド名を入力し、
   |AvailableCommandsL| でコマンドを検索する。
#. 必要に応じて、:guilabel:`Categor&y` ドロップダウンリストからコマンドの区分を
   選択する。
#. |AvailableCommandsL| で必要なコマンドを選択する。スクロールする必要があるかも
   しれない。
#. 右矢印をクリックして、必要なコマンドを |AssignedCommandsL| に追加する。
#. 必要であれば、上矢印または下矢印をクリックして、|AssignedCommandsL| の正しい
   位置にコマンドを移す。
#. 必要であれば、新しく入れたコマンドの上にメニュー区切り線を入れる。ダイアログ
   ボックス下部から :menuselection:`&Insert-->Insert Separator` を選択しろ。
#. 必要であればサブメニューを入れろ。上の手順を参考にしろ。
#. 必要であればコマンドの名前を変更する。追加したコマンドを選択状態にしてダイア
   ログボックス下部から :menuselection:`&Modify-->Rename...` を選択しろ。
#. |OK| を押して |CustomizeDlg| を閉じる。

Removing commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. |CustomizeM| で |CustomizeDlg| を開く。
#. |MenusTab| をクリックしてページを開く。:guilabel:`S&cope` ドロップダウンリス
   トで `LibreOffice Writer` が現れている。
#. |AssignedCommandsL| で削除するコマンドを選択する。
#. 左矢印をクリックして選択コマンドを |AvailableCommandsL| に移す。
#. |OK| を押して |CustomizeDlg| を閉じる。

Creating new menus
----------------------------------------------------------------------

以下は、Writer で新しいメニューを作成する手順だ。他の LibreOffice アプリケーショ
ンのメニューも同様だ。

.. |NewMenuDlg| replace:: :guilabel:`New Menu` ダイアログボックス

#. |CustomizeM| で |CustomizeDlg| を開く。
#. |MenusTab| をクリックしてページを開く。
#. |TargetL| の隣にあるハンバーガーボタンを押してメニューを開く。
#. :menuselection:`&Add...` を選択し、|NewMenuDlg| を開く。
#. :guilabel:`&Menu name` 欄に新しいメニューの名前を入力する。新しいメニューの名
   前はメニュー一覧の一番下の Menu の位置に表示される。
#. 新しいメニューを選択し、上下の矢印を使用して :guilabel:`Menu &position` 一覧
   の新しいメニューの位置を変える。
#. |OK| を押して |NewMenuDlg| を閉じると新しいメニューが |AssignedCommandsL| を
   空にして |TargetL| に表示される。
#. :ref:`common13-anchor-A` のようにして新しいメニューにコマンドを追加する。
#. |OK| を押して |CustomizeDlg| を閉じる。

Creating a shortcut character
----------------------------------------------------------------------

.. |RenameDlg| replace:: :guilabel:`Rename` ダイアログボックス

Windows のみ、メニューコマンドのキーボードショートカットとして文字を割り当てるこ
とができる。文字はメニューコマンドの名前に下線が引かれる。例えば、|Alt| +
:kbd:`O` の組み合わせで |MenuBar| :menuselection:`F&ormat-->` を開くには文字 `O`
が使われる。

.. admonition:: 利用者ノート

   |Alt| を一回押さないと下線がメニュー項目内の一文字に引かれない。

メニューコマンドにキーボードショートカットとして文字を追加する手順：

#. |CustomizeM| で |CustomizeDlg| を開く。
#. |MenusTab| をクリックしてページを開く。
#. |TargetL| からメニューを選択する。
#. |AssignedCommandsL| からメニューコマンドを選択する。
#. |TargetL| のハンバーガーをクリックするとメニューが開く。
#. メニューから :menuselection:`Rename...` を押して |RenameDlg| を開く。
#. キーボードショートカットとして使用する文字の前にチルダ ``~`` を追加する。
#. |OK| を押して |RenameDlg| を閉じる。

.. note::

   キーボードショートカットとして文字を割り当てる場合、使用する文字がすでに他の
   メニューコマンドに割り当てられていないことを確認しろ。

----

.. rubric:: 章末注
