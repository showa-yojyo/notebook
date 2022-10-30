======================================================================
Git のインターフェイスとしての VS Code
======================================================================

VS Code にはバージョン管理機能も有しており、特に Git は拡張機能のインストールな
しですぐに利用可能だ。コマンドライン操作のほうが慣れている人が多いだろうが、UI
で敢えて操作することで、バージョン管理操作に関する何らかの発見が期待できる。

以下、断りのない限りワークスペースは Git で管理されているディレクトリーからなる
とする。

.. attention::

   :doc:`./index` 冒頭の前提条件に留意すること。

.. contents::

SOURCE CONTROL ビュー
======================================================================

VS Code で次のいずれかの操作により、Side バーに :guilabel:`SOURCE CONTROL`
ビューが表示される：

* コマンド :guilabel:`View: Show Source Control` をコマンドパレットから直接実行
  する
* ショートカットキー :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`G` を押す
* Activity バーの上から三番目の履歴グラフを模したアイコンをクリックする

このビューではワークスペースのファイルを管理するリポジトリーそれぞれに対する変更
点の要約が示される。

リポジトリー
----------------------------------------------------------------------

リポジトリーごとに次のセクションに分かれている：

* :guilabel:`Merge Changes` には TODO
* :guilabel:`Staged Changes` には :command:`git add` されたファイルが示される。
* :guilabel:`Changes` には変更されているファイルであって、ステージに乗っていない
  ものが示される。


ステージ操作・編集・変更確認
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ファイル項目を右クリックしてコンテキストメニューを表示すると次の操作が行える：

.. csv-table::
   :delim: @
   :header: メニュー項目,操作

   :guilabel:`Open Changes` @ 対象ファイルのインデックスに対する差分を read-only エディターで開く。
   :guilabel:`Open File` @ 対象ファイルをエディターで開く。
   :guilabel:`Open File (HEAD)` @ 対象ファイルの HEAD 版を read-only エディターで開く。
   :guilabel:`Discard Changes` @ 対象ファイルを :command:`git restore` する。
   :guilabel:`Unstage Changes` @ 対象ファイルを :command:`git restore --staged` する。
   :guilabel:`Stage Changes` @ 対象ファイルを :command:`git add` する。
   :guilabel:`Add to .gitignore` @ 対象ファイルを ``.gitignore`` に追加する。
   :guilabel:`Reveal in Explorer View` @ EXPLORER ビューに切り替え、対象ファイルを示す。

ファイル項目にマウスホバーでアイコンが描かれるので、クリックして対応するコマンド
を実行してもよい。

ファイル項目右端に :command:`git status` コード（インデックスに対する変更区分）
が示される。

ファイル項目を普通にクリックすると上述の :guilabel:`Open Changes` が実行される。

ファイル項目のドラッグ＆ドロップでステージ操作をすることもできる。

詳細なステージ操作はリポジトリーセクション右上の三点アイコンをクリックする。
:menuselection:`... --> Changes` のサブメニューに次のコマンドが存在する：

.. csv-table::
   :delim: @
   :header: メニュー項目,相当する Git 操作

   :guilabel:`Stage All Changes`   @ :command:`git add -A .`
   :guilabel:`Unstage All Changes` @ :command:`git restore --staged .`
   :guilabel:`Discard All Changes` @ :command:`git restore .``

コミット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コミットログは :guilabel:`SOURCE CONTROL` ビュー各リポジトリーセクション最上部
のテキストボックスに入力する。

* 改行文字は :kbd:`Shift` + :kbd:`Enter` で入力する。
* :kbd:`Ctrl` + :kbd:`Enter` で :command:`git commit` 相当を実行する。

詳細なコミットをする場合、リポジトリーセクション右上の三点アイコンをクリックする。
:menuselection:`... --> Commit` のサブメニューに次のようなコマンドがある：

.. csv-table::
   :delim: @
   :header: メニュー項目,相当する Git 操作

   :guilabel:`Commit` @ ステージにファイルがある場合に :command:`git commit`
   :guilabel:`Commit Staged` @ ステージにファイルがある場合に :command:`git commit`
   :guilabel:`Commit All` @ :command:`git add -A . && git commit`
   :guilabel:`Undo Last Commit` @ :command:`git reset --soft HEAD~`
   :guilabel:`Abort Rebase` @ :command:`git rebase --abort`?
   :guilabel:`Commit Staged (Amend)` @ :command:`git commit --amend`
   :guilabel:`Commit All (Amend)` @ :command:`git add -A . && git commit --amend`
   :guilabel:`Commit Staged (Signed Off)` @ :command:`git commit --signoff`
   :guilabel:`Commit All (Signed Off)` @ :command:`git add -A . && git commit --signoff`

特に有用なのは :guilabel:`Undo Last Commit` と :guilabel:`Commit Staged (Amend)`
だろう。逆にありがたくないのは :guilabel:`Commit All` 系だ。これを実行するワーク
フローが良いものだとは思えない。

リポジトリー操作
======================================================================


リポジトリーを複製する
----------------------------------------------------------------------


リポジトリーを初期化する
----------------------------------------------------------------------


ブランチとタグ
----------------------------------------------------------------------


リモート
----------------------------------------------------------------------


ステータスバー
======================================================================

VS Code の左下には、リポジトリーの状態を示すインジケーターがある。
私の環境だと :guilabel:`WSL: Ubuntu` のすぐ右隣にある。
ここには次の情報が常時示される：

* 現在のブランチ (e.g. ``main``)
* ローカルリポジトリーが clean であるか否かを示す記号 ``*``
* 現在のブランチの受信・送信コミット数

このインジケーターをクリックするとコマンド :guilabel:`Git: Checkout to ...` を実
行することになる。

現在のブランチに上流ブランチが設定されている場合には、インジケーターのさらに右側
に丸矢印アイコンがある。クリックするとコマンド :guilabel:`Git: Sync` を実行する。
これはリモートの変更をローカルリポジトリに取り込み、ローカルのコミットを
:command:`git push -u origin` する。上流ブランチが設定されていない場合には
コマンド :guilabel:`Git: Publish Branch...` が代わりに実行される。

エディター
======================================================================


衝突表示
======================================================================


差分表示
======================================================================


タイムラインビュー
======================================================================


拡張機能
======================================================================


出力確認
======================================================================

VS Code の Git 操作コマンドが実際に実行するコマンドラインを確認する方法がある。
コマンド :guilabel:`Git: Show Git Output` を直接実行する。

1. :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`U` を押すなどして、画面下部パネルの
   :guilabel:`OUTPUT` を開く。
2. タブバー右側ドロップダウンリストから :guilabel:`Git` を選択する。

ログが表示される。タイムスタンプ、コマンドライン、実行時間を確認できる。

Git 側の設定で VS Code を絡める
======================================================================

各種ログエディター、差分、マージに VS Code を使用するように、Git のユーザー構成
ファイル ``$HOME/.gitconfig`` または ``$HOME/.config/gitconfig`` に次の記述を含
めるといい。特に、この記述があれば :command:`git difftool` と
:command:`git mergetool` それぞれのコマンド実行で VS Code が利用できることに注目
したい。差分確認や手動マージでは GUI ベースの作業の方が楽だ。

.. code:: text

   [core]
       editor = code --wait
   [diff]
       tool = vscode-diff
   [difftool "vscode-diff"]
       cmd = code --wait --diff $LOCAL $REMOTE
   [merge]
       tool = code
   [mergetool "code"]
       cmd = code --wait --merge $REMOTE $LOCAL $BASE $MERGED
