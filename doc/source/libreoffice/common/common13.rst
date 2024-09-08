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

.. |SearchE| replace:: :guilabel:`&Search` 欄
.. |ScopeL| replace:: :guilabel:`S&cope` ドロップダウンリスト
.. |CategoryL| replace:: :guilabel:`Categor&y` ドロップダウンリスト
.. |TargetL| replace:: :guilabel:`&Target` ドロップダウンリスト
.. |AssignedCommandsL| replace:: :guilabel:`&Available Commands` 一覧
.. |AvailableCommandsL| replace:: :guilabel:`&Available Commands` 一覧

#. |CustomizeM| で |CustomizeDlg| を開く。
#. |MenusTab| をクリックしてページを開く。|ScopeL| で `LibreOffice Writer` が現
   れている。
#. |TargetL| から改造するメニューを選択する。このドロップダウンリストは選択メ
   ニューで使用可能なサブメニューも含む。
#. |AssignedCommandsL| に選択メニューに必要なコマンドがないことを確認する。一覧
   をスクロールする必要があるかもしれない。
#. 必要に応じて、|SearchE| にコマンド名を入力し、
   |AvailableCommandsL| でコマンドを検索する。
#. 必要に応じて、|CategoryL| からコマンドの区分を選択する。
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

.. _common13-anchor-B:

Removing commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. |CustomizeM| で |CustomizeDlg| を開く。
#. |MenusTab| をクリックしてページを開く。
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
#. :ref:`common13-anchor-A` の要領で新しいメニューにコマンドを追加する。
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

Toolbar customization
======================================================================

.. |ToolbarsTab| replace:: :guilabel:`Toolbars` タブ

この節では、新しいツールバーを作成する方法と、既存のツールバー上の図像を追加また
は削除する方法について述べる。

|CustomizeDlg| |ToolbarsTab| をツールバーを改造したり、新しいツールバーを作成し
たりするために使用する。出現方法は：

* ツールバーの何もない場所で右クリックし、コンテキストメニューから
  :menuselection:`&Customize Toolbar...` を選択する。
* |MenuBar| :menuselection:`&View-->&Toolbars-->&Customize...` を選択する。
* |MenuBar| |CustomizeM| を選択し、ダイアログボックスが開いたら |ToolbarsTab| を
  クリックする。

.. note::

   LibreOffice でツールバーを改造または作成する場合は、LibreOffice アプリケー
   ションが開いており、文書が何か開いていることを確認しろ。

.. _common13-anchor-C:

Toolbar customization
----------------------------------------------------------------------

Adding tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. |CustomizeDlg| を開き、|ToolbarsTab| をクリックする。
#. |ScopeL| で表示されている LibreOffice アプリケーションまたは表示されている文
   書のいずれかを選択する。

   .. note::

      |ScopeL| で表示されている文書が選択されている場合、ツールバーの改造はその
      選択された文書に対してのみ有効となる。

#. |TargetL| で改造するツールバーを選択する。選択したツールバーの道具は
   |AssignedCommandsL| に表示される。
#. |AvailableCommandsL| で道具を選択する。
#. あるいは、|AvailableCommandsL| に表示される道具の数を減らすのに以下のいずれか
   の方法を使用する：

   * |SearchE| に検索語を入力する
   * |CategoryL| からカテゴリを選択する
#. 右矢印をクリックして、必要なコマンドを |AssignedCommandsL| に追加する。
#. |AssignedCommandsL| の上下の矢印を使用して、選択したツールバーの必要な位置に
   道具を配置する。
#. 必要に応じて区切り線を入れたり除いたりする。:ref:`common13-anchor-A` の要領だ。
#. 必要に応じて名前を変える。これも。
#. |OK| を押して |CustomizeDlg| を閉じる。

Removing tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`common13-anchor-B` の記述で |MenusTab| の代わりに |ToolbarsTab| を使えば手
順は同じになる。

Creating new toolbars
----------------------------------------------------------------------

#. |CustomizeDlg| を開き、|ToolbarsTab| をクリックする。
#. |ScopeL| で表示されている LibreOffice アプリケーションまたは表示されている文
   書のいずれかを選択する。
#. |TargetL| の隣にあるハンバーガーボタンを押してメニューを開く。
#. :menuselection:`&Add...` を選択し、|NameDlg| を開く。
#. :guilabel:`&Toolbar name` 欄に新しいツールバーの名前を入力する。
#. :guilabel:`&Save in` 欄で新しいツールバーを保存する場所を選択する。保存先
   は、LibreOffice アプリケーションか、一覧にある文書のいずれかだ。
#. |OK| を押して |NameDlg| を閉じる。
#. :ref:`common13-anchor-C` の要領で必要なツールを新しいツールバーに追加する。
#. |OK| を押して |CustomizeDlg| を閉じる。

Changing tool icons
----------------------------------------------------------------------

.. |ChangeIconDlg| replace:: :guilabel:`Change Icon` ダイアログボックス

ツールバー上の道具は図像で示される。次のようにして変更可能だ：

#. |CustomizeDlg| を開き、|ToolbarsTab| をクリックする。
#. |TargetL| で図像を改造ツールバーを選択する。
#. |AssignedCommandsL| で図像を変更する道具を選択する。
#. ダイアログボックス下の :menuselection:`&Modify-->Change Icon...` を選択するか、
   選択したツールを右クリックし、:menuselection:`&Change Icon...` を選択して
   |ChangeIconDlg| を開く。
#. 図像のプレビュー欄に表示されている利用可能な図像から図像を選択する。
#. |OK| を押して選択した道具の図像を変更し、|ChangeIconDlg| を閉じる。
#. |OK| を押して |CustomizeDlg| を閉じる。

.. note::

   図像は外部プログラムを使って作成し、LibreOffice にインポートすることが可能だ。
   図像の推奨解像度は 16x16 だ。異なる寸法の図像は自動的に拡縮される。

----

.. rubric:: 章末注
