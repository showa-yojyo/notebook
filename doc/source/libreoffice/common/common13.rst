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

改造は LibreOffice Web サイトまたは他の供給人からインストールできる拡張を追
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

Keyboard shortcuts
======================================================================

Using keyboard shortcuts
----------------------------------------------------------------------

LibreOffice の機能の多くはマウスを使用せずにキーボードを使用して実行可能だ。たと
えば、|MenuBar| :menuselection:`&File-->&Open...` コマンドの横に表示されているよ
うに、|Ctrl+O| を押せばこのメニュー項目を選択せずにこのコマンドが開始する。

Creating keyboard shortcuts
----------------------------------------------------------------------

LibreOffice で利用可能なキーバインドを使用するだけでなく、改造キーバインドを作成
することも可能だ。これらの改造キーバインドは LibreOffice の関数またはマクロに割
り当て可能であり、LibreOffice アプリケーションで使用するために保存可能だ。

.. note::

   利用可能なキーバインドの中には、計算機システムで使用する機能またはコマンドと
   して割り当てられているものがある。そのようなキーバインドを LibreOffice の改造
   キーバインドとして使用してはいけない。計算機システムの動作に問題が生じる可能
   性がある。

.. |KeyboardTab| replace:: :guilabel:`Keyboard` タブ
.. |KeysL| replace:: :guilabel:`&Keys` 一覧

#. |CustomizeDlg| を開く。
#. |KeyboardTab| をクリックする。
#. コマンドに新しいキーバインドを割り当てる：

   * LibreOffice アプリケーション全体で利用可能なキーバインドに対しては、ダイア
     ログボックス右上の :guilabel:`Li&breOffice` を選択しろ。
   * 現在の LibreOffice アプリケーションで利用可能なキーバインドに対しては、ダイ
     アログボックス右上のそれを選択する。
#. :guilabel:`&Catagory` からキーバインドに必要な区分を選択する。
#. :guilabel:`&Function` からキーバインドに必要な機能を選択する。
#. :guilabel:`Shortcu&t Keys` から必要なキーバインドを選択し :guilabel:`&Assign`
   ボタンを押す。選択したキーバインドが選択した区分と機能に割り当てられ |KeysL|
   に表示される。
#. |OK| を押して |CustomizeDlg| を閉じる。

.. note::

   すでに機能に割り当てられているキーバインドはすべて |KeysL| に表示される。すで
   に割り当てられているキーバインドを変更することは勧められない。

   |CustomizeDlg| のリストでグレーアウトしているキーバインド、たとえば |F1|,
   |F6|, |F10| などは、使用したり再割り当てしたりすることは不可能だ。

Saving keyboard configurations
----------------------------------------------------------------------

キーバインドの割り当て変更は、キーボード設定ファイルとして保存可能だ。これによ
り、必要に応じて異なるキーボード設定を作成し、適用することが可能だ。また、キー
ボード設定ファイルを複数の使用者に配布することも可能だ。

#. キーバインドの割り当てを調整および変更した後、|CustomizeDlg| の右側にある
   |SaveB| を押し、キーボード設定を保存するためのファイルダイアログボックスを開
   く。
#. キーボード設定ファイルを保存するフォルダーに移動する。
#. 保存ファイルを適当に指定する。
#. |Save| を押してキーボード設定ファイルを保存し、ファイルダイアログボックスを閉
   じる。
#. |OK| を押して |CustomizeDlg| を閉じる。

Loading keyboard configurations
----------------------------------------------------------------------

保存されたキーボード設定ファイルをロードし、既存のキーボード設定を置き換える：

#. |CustomizeDlg| の右側にある :guilabel:`&Load...` ボタンを押すとファイルダイア
   ログボックスが開く。
#. キーボード設定ファイルを保存するフォルダーに移動する。
#. |Open| を押して選択したキーボード設定を LibreOffice に読み込み、ファイルダイ
   アログボックスを閉じる。
#. |OK| を押して |CustomizeDlg| を閉じる。
#. LibreOffice を再起動して、新しいキーボード設定が効いていることを確認する。

Resetting keyboard configuration
----------------------------------------------------------------------

LibreOffice のキーバインドすべてを既定値に戻す方法：

#. |CustomizeDlg| を開く。
#. |KeyboardTab| をクリックする。
#. |CustomizeDlg| の右側にある |ResetButton| を押す。キーボード設定を初期設定に
   戻す際、確認は表示されない。
#. |OK| を押して |CustomizeDlg| を閉じる。
#. LibreOffice を再起動して、既定のキーボード設定が効いていることを確認する。

Assigning macros
======================================================================

マクロを LibreOffice のイベントに割り当てることが可能。割り当てられたマクロは関
連するイベントが発生するたびに自動的に実行される。イベントとは、たとえば、文書が
開かれた、キーが押された、キャレットが移った、などだ。マクロをイベントに関連付け
るには、|CustomizeDlg| |EventsTab| を用いる。イベントをマクロに割り当てる方法の
詳細については :doc:`common11` を見ろ。

Adding extensions
======================================================================

Installing extensions
----------------------------------------------------------------------

拡張とは LibreOffice の機能を向上させるために LibreOffice の中にインストールでき
るプログラムだ。たとえば、雛形、辞書、クリップアートギャラリー、マクロ、ダイアロ
グライブラリーなどを拡張として加えられる。

LibreOffice を計算機にインストールする時点で拡張がいくつかインストールされる。そ
の他の拡張は <https://extensions.libreoffice.org/> にある公式拡張保管庫から無料
でダウンロード可能だ。

拡張は他の供給源からもダウンロードし得る。これらの拡張の中には無料のものも有料の
ものもある。どのような免許と料金が適用されるかはその記述を当たれ。

Installing extensions
----------------------------------------------------------------------

公式拡張保管庫に掲載されている拡張のインストール方法：

.. todo:: steps

#. |MenuBar| |ExtensionsM| で |ExtensionsDlg| を開く。
#. :guilabel:`Get more extensions online...` リンクをクリックする。LibreOffice
   公式拡張保管庫が Webブラウザーで開く。
#. ページ内の検索欄に検索語を入力し、:guilabel:`Search` ボタンを押す。
#. 必要な拡張を見つけてクリックし、選択した拡張の Web ページを開く。
#. 拡張の記述と、使用している LibreOffice のバージョンおよび計算機の OS との互換
   性を確認する。
#. 正しいバージョンの拡張については、:guilabel:`Download` をクリックすると、拡張
   が計算機のダウンロードフォルダーにダウンロードされる。
#. |ExtensionsDlg| で :guilabel:`&Add` ボタンを押してファイルダイアログボックス
   を開く。
#. 拡張のあるフォルダーに移動する。
#. 拡張を選択し |Open| を押す。
#. 拡張がインストールされ、|ExtensionsDlg| に表示される。
#. 必要に応じて、拡張を有効にするために LibreOffice を再起動する。

.. note::

   公式保管庫所蔵でない拡張をインストールするには、その拡張の供給源からモノをダ
   ウンロードし、上記方法の途中手順から再現して拡張をインストールする。

Updating extensions
----------------------------------------------------------------------

.. |ExtensionUpdateDlg| replace:: :guilabel:`Extension Update` ダイアログボックス

拡張の更新を定期的に調べることが必要だ。その方法：

#. |ExtensionsDlg| を開く。
#. :guilabel:`Check for &Updates` ボタンを押して |ExtensionUpdateDlg| を開く。
#. :guilabel:`&Available extensions update` に表示されている拡張を選択し、
   :guilabel:`&Install` を押して拡張を更新する。
#. |ExtensionUpdateDlg| と |ExtensionsDlg| を閉じる。
#. 必要に応じて、拡張の更新を有効にするために LibreOffice を再起動する。

Removing extensions
----------------------------------------------------------------------

不要になった拡張を削除して完全にアンインストールするには次のようにする：

#. |ExtensionsDlg| を開く。
#. 削除する拡張を選択する。
#. |RemoveButton| を押し、拡張の削除を確認する。
#. |ExtensionsDlg| を閉じる。

Disabling extensions
----------------------------------------------------------------------

.. |DisableB| replace:: :guilabel:`&Disable` ボタン

LibreOffice から拡張を削除せずに、拡張を作動させなくする方法：

#. |ExtensionsDlg| を開く。
#. 作動させない拡張を選択する。
#. |DisableB| を押す。ボタンのラベルが変わる。
#. 必要に応じて、:guilabel:`&Enable` ボタンを押すと、LibreOffice で再び拡張機能
   が作動する。

.. note::

   |ExtensionsDlg| で |RemoveButton| と |DisableB| が灰色表示されている場合、そ
   の拡張は削除することも作動不能にさせることもできない。拡張が LibreOffice のイ
   ンストールの一部であるなどに灰色表示になる。

----

.. rubric:: 章末注
