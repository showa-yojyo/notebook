======================================================================
Workspaces 利用ノート
======================================================================

.. |wsp| replace:: Workspaces_
.. |editor| replace:: :guilabel:`Workspaces Editor`
.. |capture| replace:: :guilabel:`Snapshot creator`
.. |kb| replace:: :kbd:`Win` + :kbd:`Ctrl` + :kbd:`@`

本稿は PowerToys の |wsp| 機能に関する記述だ。

.. attention::

   :doc:`./index` 冒頭の前提条件に留意すること。

.. contents:: 見出し一覧
   :local:

概要
======================================================================

|wsp| は Windows の無料ソフトでありがちなランチャーアプリケーションだ。設定した
プログラム群を、それぞれのウィンドウが所定の位置と大きさであるように起動する。

Workspaces Editor
======================================================================

|editor| の UI について記す。

:guilabel:`Create Workspace`
   |capture| ダイアログボックスを開き、キャプチャー操作を開始する。
検索欄
   作業場またはアプリケーションを検索できる。
:guilabel:`Sort by`
   作業場一覧をどの順序で並び替えるかを次の選択肢から決める：

   * :guilabel:`Last launched`
   * :guilabel:`Created`
   * :guilabel:`Name`
作業場一覧
   作業場項目一つの UI 構成は次のとおり：

   :guilabel:`...`
      三点アイコンは作業場を操作するコマンドのメニューだ。メニュー項目はたぶん次
      の二つしかない：

      :menuselection:`Edit`
         この作業場項目に関する :guilabel:`Edit Workspace` 画面を開く。
      :menuselection:`Remove`
         この作業場項目を項目一覧から削除する。確認メッセージはない。
   :guilabel:`Launch`
      この作業場項目で設定されているプログラム群のプロセスを順次開始する。

Create Workspace 画面
----------------------------------------------------------------------

|capture| ダイアログボックスが終わると |editor| のこの画面に移る。プログラムを選
択したり、ウィンドウの配置やコマンドライン引数を調整したりする場所だ。

プレビュー領域
   作業場のウィンドウ位置のスケッチが示される。

   :guilabel:`Launch & edit`
      このボタンを押すと |capture| 操作をもう一度やり直すことになる。
   :guilabel:`Revert`
      今やり直したキャプチャーの状態を破棄して、その前にキャプチャーした状態に戻
      す。
作業場の特徴を指定する部分
   :guilabel:`Workspace name`
      作業場の名前を指定する。既定値は :samp:`Workspace {n}` のような文字列だ。

      作業場の内容を表現する名前を与えろ。
   :guilabel:`Create desktop shortcut`
      これをチェックすると、この作業場を発射するための Windows ショートカット
      ファイルがデスクトップに生成する。

      後でショートカットをスタートメニューやタスクバーなどに適宜移動してよい。
   :guilabel:`Move existing windows`
      チェックすると、発射済みのアプリケーションは作業場内の指定位置に移動され、
      それ以外のアプリケーションは新たに発射される。

      これは基本的にチェックを入れておきたい。
:guilabel:`Screen 1`
   画面内に描画されているアプリケーション（次節を見ろ）の一覧。
:guilabel:`Minimized`
   ウィンドウが最小化されているアプリケーションの一覧。
:guilabel:`Cancel`
   作業場の構成変更を中止して |editor| ホーム画面に戻る。
:guilabel:`Save workspace`
   作業場の構成更新を確定して |editor| ホーム画面に戻る。

アプリケーション項目
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Remove` / :guilabel:`Add back`
   このアプリケーションを一覧から削除する / 削除したがやめて一覧に戻す。
:guilabel:`CLI arguments`
   このアプリケーションのプロセスを生成するときのコマンドライン引数を指定する。
   指定する場合、アプリケーション名の下に引数文字列がそのまま示される。

   例えば、Visual Studio Code で WSL Ubuntu ファイルシステムにあるパスを開きたい
   場合には、次のようなコマンドライン引数を指定する：

   .. sourcecode:: text

      --remote wsl+Ubuntu /path/to/file-or-directory
:guilabel:`Launch as Admin`
   チェックを入れると、このアプリケーションは管理者権限で走る。
:guilabel:`Window position`
   アプリケーションウィンドウの配置を次の選択肢から指定する：

   * :guilabel:`Custom`: ウィンドウの座標と寸法を具体的に指定する。キャプチャー
     時点での値が初期値となる。
   * :guilabel:`Maximized`
   * :guilabel:`Minimized`

Edit Workspace 画面
----------------------------------------------------------------------

:guilabel:`Edit Workspace` 画面は作業場項目に対して :guilabel:`Edit` ボタンを押
すと現れるものだ。UI 構成は :guilabel:`Create Workspace` 画面と同様だ。

Snapshot Creator ダイアログボックス
======================================================================

|capture| ダイアログボックスが表示されている間、使用者はデスクトップ上のウィンド
ウ群を、場所を移したり寸法を変えたりして調整する。

:guilabel:`Cancel`
   ウィンドウ群の間取りをやめて |editor| に戻る。内容は以前どおり。
:guilabel:`Capture`
   ウィンドウ群の間取りを確定して |editor| に移る。そこではこの間取りをさらに調
   整することができる。

設定
======================================================================

:guilabel:`Enable Workspaces` を On にして |wsp| を有効にする。つまり、設定した
キーバインドを押すと |editor| が開くようになる。

Activation
----------------------------------------------------------------------

:guilabel:`Activation shortcut`
   |editor| を開くキーバインド。既定の |kb| でいい。
:guilabel:`Open editor`
   |editor| を直接開く。

.. _Workspaces: https://learn.microsoft.com/en-us/windows/powertoys/workspaces

.. 以上
