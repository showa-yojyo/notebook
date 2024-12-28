======================================================================
拡張
======================================================================

VS Code はエディター本体と拡張に機能を分割する設計が上手く働いているアプリケー
ションだ。編集効率を向上させる拡張を見つけ、組み込み、調節する技法を習得したい。

.. attention::

   :doc:`./index` 冒頭の前提条件に留意すること。

.. contents::

拡張ビュー
======================================================================

次のいずれかの操作により Side Bar の表示が拡張ビューに変化する：

* ショートカットキー :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`X` を押す。
* Activity Bar 最下部歯車アイコンクリックからの :menuselection:`Extensions` を選
  択する。
* Side Bar が表示されているならば、Activity Bar から四角が離れているアイコンをク
  リックする。

このビューに付属する UI やコマンドを介して VS Code 拡張機能を操作する。

検索
======================================================================

先に検索方法を記す。まずは拡張ビュー上部のテキストボックスに欲しい機能を叙述した
文字列を入力する。すると、問い合わせに合致する機能一覧がテキストボックスの下部領
域に配列される。ここで次の操作が可能だ：

* 項目をクリックする。エディター領域に当該拡張機能の紹介ページを表示する。
* 項目の右下にある :guilabel:`Install` ボタンを押す。当該機能が VS Code にインス
  トールされる。たいていの場合、拡張機能が有効になるために VS Code 本体の再起動
  を要求される。

フィルターすなわち問い合わせパターン
----------------------------------------------------------------------

拡張ビュー最上部右上の漏斗アイコンをクリックすると、絞り込み項目からなるメニュー
が表示される。項目を選択すると、検索ボックスの入力文字列が対応する問い合わせで置
き換わる。

拡張機能の採用方針としては、まず Recommended 検索か Category 検索をベースに、検
索結果に示されているダウンロード数と評価数を参考にするのがいいだろう。ここに
Sort フィルターを組み合わせる。検索入力例：

| :code:`@category:"keymaps" emacs @sort:rating`

検索結果を消去する
----------------------------------------------------------------------

拡張ビュー最上部右上のハンバーガーバツアイコンをクリックすると、検索出力が消去さ
れて、現在管理されている拡張機能一覧が出力される。

管理
======================================================================

以下、拡張ビューは検索をしていない状態であるとする。

拡張ビュー最上部右上の三点アイコンをクリックすると、拡張機能のある種の集合に対す
る操作項目からなるメニューが表示される。次のような操作が可能だ：

.. csv-table::
   :delim: @
   :header-rows: 1
   :widths: auto

   項目 @ 操作
   :menuselection:`Check for Extension Updates` @ 拡張の更新が容易されているかを見に行く
   :menuselection:`Update All Extensions` @ 更新可能な拡張すべてを更新する
   :menuselection:`Enable All Extensions` @ 拡張すべてを有効にする
   :menuselection:`Disable All Installed Extensions` @ 拡張すべてを無効にする
   :menuselection:`Show Running Extensions` @ 稼働中の拡張を一覧する

拡張ビューには、現在 VS Code 上で管理可能な拡張機能項目が列挙される。各項目の右
下に小さく描かれている歯車アイコンをクリックすると、拡張機能管理コマンドからなる
メニューが表示される。

個別の拡張に対しては次のような操作が可能だ：

.. csv-table::
   :delim: @
   :header-rows: 1
   :widths: auto

   項目 @ 操作
   :menuselection:`Enable` @ この拡張機能を有効にする
   :menuselection:`Enable (Workspace)` @ この拡張機能を現在のワークスペースに対しては有効にする
   :menuselection:`Disable` @ この拡張機能を無効にする
   :menuselection:`Disable (Workspace)` @ この拡張機能を現在のワークスペースに対しては無効にする
   :menuselection:`Uninstall` @ この拡張機能をアンインストールする
   :menuselection:`Copy` @ この拡張機能の情報をテキスト形式でクリップボードにコピーする
   :menuselection:`Copy Extension ID` @ この拡張機能の ID 文字列をクリップボードにコピーする
   :menuselection:`Extension Settings` @ この拡張機能の設定を操作する

更新
----------------------------------------------------------------------

更新操作は個々の拡張に対しても、可能な拡張すべてに対しても行うことができる。
自動更新と手動更新のどちらも可能なので、自分の環境に合わせたものを採用できる。

自動更新を望むなら拡張ビュー上部右上の三点アイコンを押し、
:menuselection:`… --> Auto Update Extensions --> All Extensions` にチェックを入
れておく。

手動で更新したいならば、:menuselection:`… --> Auto Update Extensions --> None`
にチェックを入れておく。これで自動更新が無効になる。

自動更新が無効であるときに :menuselection:`… --> Check for Extension Updates` を
選択する。すると拡張ビューに対象候補であり得る拡張機能の項目が列挙される。次のい
ずれかで更新が始まる：

* （個別）目的の拡張項目の右下にあるボタン :guilabel:`Update` を押す。
* （全部）メニュー項目 :menuselection:`… --> Update All Extensions` を選択する。

構成
======================================================================

拡張機能によっては :file:`settings.json` を編集することでオプションを指定するこ
ともできる。拡張ビュー上に対象となる拡張機能を表示し、先述のメニュー項目
:menuselection:`Extension Settings` から編集画面を表示させ、適宜指定する。

:doc:`./settings` を参照。

コマンドライン
======================================================================

:doc:`./cli` の章の拡張機能関連の記述を参照。

コマンドラインを利用することで、拡張機能の操作をより自動化することもできる。
別の環境で現在の環境を再現する状況などに応用できるだろう。

.. _vscode-favorite-extensions:

個人的にインストールしておきたい拡張
======================================================================

好みの言語別拡張を以下に記す。その言語を扱うワークスペースで有効にすればいい。

.. list-table:: 個人的にインストールしておきたい拡張
   :widths: auto
   :header-rows: 1

   * - 名前
     - コメント
   * - `Awesome Emacs Keymap
       <https://marketplace.visualstudio.com/items?itemName=tuttieee.emacs-mcx>`__
     -  元 :program:`xyzzy` 使いとして、この手の拡張を導入したい手はない。
   * - `Rewrap
       <https://marketplace.visualstudio.com/items?itemName=stkb.rewrap>`__
     - :kbd:`Alt` + :kbd:`Q` 一発で選択範囲を既定桁数で折り返せる手軽な拡張だ。
   * - `WSL
       <https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl>`__
     - WSL のファイルシステムにワークスペースを用意するのに必須の拡張だ。
   * - `Live Server
       <https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer>`__
     - ローカル HTTP サーバーを実現する拡張だ。
   * - `Markdown All in One
       <https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one>`__
     - 日記を Markdown で書く習慣があるのでこの拡張を導入している。
   * - `Markdown Preview Mermaid Support
       <https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid>`__
     - Mermaid 図式コードを含む Markdown 文書をプレビューするときに、それを描画
       するための拡張だ。
   * - `learn-yaml
       <https://marketplace.visualstudio.com/items?itemName=docsmsft.docs-yaml>`__
     - YAML コードに関するコード片補完、スキーマ指定、構文検証各機能を備える拡
       張だ。
   * - `Esbonio
       <https://marketplace.visualstudio.com/items?itemName=swyddfa.esbonio>`__
     - Sphinx を使うワークスペースで使えるかもしれない拡張だ。
   * - `Python
       <https://marketplace.visualstudio.com/items?itemName=ms-python.python>`__
     - Python 開発用機能拡張詰め合わせ。
   * - `Jupyter
       <https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter>`__
     - Jupyter notebook を取り扱うための拡張詰め合わせ。
   * - `C/C++ Extension Pack
       <https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools-extension-pack>`__
     - C++ 開発のための各種拡張詰め合わせ。
   * - `Extension Pack for Java
       <https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-pack>`__
     - Java 開発のための各種拡張詰め合わせ。

よその推奨拡張一覧を見ていると、現在 deprecated なものが含まれることがある。これ
は、超人気サードパーティー製拡張は標準拡張に昇格することがあるためだ。
