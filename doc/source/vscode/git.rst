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

* :guilabel:`Merge Changes` には :command:`git merge` 直後に衝突したファイルが示
  される。
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

.. admonition:: 利用者ノート

   「相当する」操作と私が記す場合、VS Code が実行する実際のものと一致するとは限
   らない。実際の Git コマンドを確認するには後述の方法による。

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

VS Code でまだ何も開いていない場合などに、:guilabel:`SOURCE CONTROL` ビューには
次の選択肢がボタンで示される：

* :guilabel:`Open Folder`
* :guilabel:`Clone Repository`

後者を選択すると、コマンド :guilabel:`Git: Clone` が実行される。すると、リポジト
リーのパスを入力することになる。ファイルシステムのパスか、Git リポジトリーの URL
を指定することが可能だ。

パス入力欄の下に :guilabel:`Clone from GitHub` という項目も表示される。
VS Code から GitHub のアカウント認証を行うと（ブラウザーが開くかもしれない）、
リポジトリー検索リストが表示される。ここからリポジトリーを選択することで
:command:`git clone` 相当のことが実現できる。また、複製されたリポジトリー設定に
リモートに対する設定などが自動的になされる。

リポジトリーを初期化する
----------------------------------------------------------------------

リポジトリーでないワークスペースについては :guilabel:`SOURCE CONTROL` ビューの構成
は普段と異なる。

ワークスペースがローカルマシンにある場合、コマンド :guilabel:`Git: Initialize Repository`
で Git リポジトリーを作成することできる。これは :command:`git init` と同じだろう。
実行後、VS Code がワークスペースをローカルリポジトリーであると認識する。

場合によってはコマンド :guilabel:`Publish to GitHub` という選択肢もあり得る。
ワークスペースのフォルダーを GitHub リポジトリーに直接配備し、private か public
かを選択する。

ブランチとタグ
----------------------------------------------------------------------

VS Code から離れずにブランチを操作することが可能だ。コマンドパレットで ``branch``
を検索すると関連コマンドを確認できる。

コマンド :guilabel:`Git: Checkout to...` を実行すると、現在のリポジトリーのすべ
てのブランチおよびタグからなるドロップダウンリストが表示される。項目を選択すると、
現在のブランチがそれに切り替わる。

コマンド :guilabel:`Git:Create Branch` を実行すると、新しいブランチを作成する。
ブランチの名前を指定すると VS Code がそれを作成し、そこに切り替える。
:guilabel:`Create new branch from...` を選択すると、新しいブランチの起点コミット
を指定するための入力欄が表示される。

リモート
----------------------------------------------------------------------

リポジトリーがリモートに接続されていて、チェックアウトしたブランチがリモートブラ
ンチに上流からリンクしているとすると、VS Code はそのようなブランチを push, pull
するコマンドが用意している。これらのコマンドは、リポジトリーセクションのバー右上
の :menuselection:`... --> Pull, Push` 以下にある。

リモートリポジトリー自体を構成するコマンドは :menuselection:`... --> Remote` 以
下から実行可能だ：

.. csv-table::
   :delim: @
   :header: コマンド,操作

   :guilabel:`Add Remote...` @ :command:`git remote add` 相当
   :guilabel:`Remove Remote` @ :command:`git remote rm` 相当

VS Code はリモートから変更点を定期的に取得することができます。この機能はローカル
の変更点がリモートに比べてどれだけ先方または後方にあるのかを表示するのに利用するも
のだ。既定では無効になっており、有効化するには設定ファイルで ``git.autofetch``
の値を指定する。

.. todo::

   認証ヘルパー

ステータスバー
======================================================================

VS Code の左下には、リポジトリーの状態を示すインジケーターがある。私の環境だと
:guilabel:`WSL: Ubuntu` のすぐ右隣にある。ここには次の情報が常時示される：

* 現在のブランチ (e.g. ``main``)
* ローカルリポジトリーが dirty か clean かを示す記号 ``*``
* 現在のブランチの受信・送信コミット数

このインジケーターをクリックすると前述のコマンド :guilabel:`Git: Checkout to ...`
を実行することになる。

現在のブランチに上流ブランチが設定されている場合には、インジケーターのさらに右側
に丸矢印アイコンがある。クリックするとコマンド :guilabel:`Git: Sync` を実行する。
これはリモートの変更をローカルリポジトリに取り込み、ローカルのコミットを
:command:`git push -u origin` する。上流ブランチが設定されていない場合には
コマンド :guilabel:`Git: Publish Branch...` が代わりに実行される。

エディター
======================================================================

リポジトリーのファイルをエディターで開いて編集すると、行番号右の細い隙間と縦スク
ロールバー領域に便利な注釈を動的に追加する。

.. csv-table::
   :delim: @
   :header: 記号,意味

   赤い三角形 @ 直前の版でここにあったテキストが削除されていることを示す
   緑の線 @ 直前の版から追加された行であることを示す
   青い線 @ 直前の版から内容が変更された行であることを示す

差分表示
======================================================================

:command:`git diff` の代わりに VS Code 上で編集ファイルの差分を表示することができる。
それには、対象ファイルに対してコマンド :guilabel:`Git: Open Changes` を実行する。

Git とは無関係に、VS Code の差分関連機能を使って左右比較表示とインライン表示とを
切り替えることができる。

変更行間の移動キーバインドが設定されているが、どちらの表示形式であるかにより異な
る。紛らわしくなるのでここには記さないことにするが、:kbd:`F5` または :kbd:`F7`
に修飾キーを絡めるものだ。

衝突表示
======================================================================

マージ衝突時に Git がマーカーを挿入したファイルを VS Code が認識して、両者の差分をハイライ
ト表示する。さらに、衝突箇所にはどちらか一方または両方の変更を受け入れるためのイ
ンラインアクション実行 UI がある。衝突が解決されると、対象ファイルをステージ処理
し、それらの変更をコミットできるようにする。

インラインアクションは次の四つだ：

.. csv-table::
   :delim: @
   :header: アクション,操作

   :guilabel:`Accept Current` @ 現在ブランチの内容を採用する
   :guilabel:`Accept Incoming` @ マージブランチの内容を採用する
   :guilabel:`Accept Both` @ 双方の内容を連結したものを採用する（適用順序は？）
   :guilabel:`Compare Changes` @ 差分エディターを開く

より丁寧に編集するならば、インラインアクションを実行せずに、エディター右下に現れ
ているボタン :guilabel:`Resolve in Merge Editor` を押す。これで 3-way マージエ
ディターが開く。インラインマージエディターとの違いは、マージ後のエディターでテキ
スト塊を取り除くアクション UI が表示されることだ。これでテキスト塊の適用順を選択
できる。

.. csv-table::
   :delim: @
   :header: アクション,操作

   :guilabel:`Remove Current` @ 現在ブランチ部分の採用を取り消す
   :guilabel:`Remove Incoming` @ マージブランチ部分の採用を取り消す
   :guilabel:`Reset to base` @ マージ編集を全部捨てる

エディター右下のボタン :guilabel:`Complete Merge` ボタンを押すと、当該ファイルが
:guilabel:`Merge Changes` から :guilabel:`Staged Changes` に移る。これを衝突ファ
イルがなくなるまで反復し、最後にコミットする。コミットログはすでにログ入力欄に記
入されている。

.. admonition:: 利用者ノート

   この UI がたいへん便利で、単発の衝突時の作業に重宝する。
   VS Code エディターでの衝突解決方法を必ず習得すること。

TIMELINE ビュー
======================================================================

:guilabel:`EXPLORER` ビューの下部にある :guilabel:`TIMELINE` ビューは、現在の
ファイルの時系列Git コマンドを含むイベントを時系列で配列されている。

ここからコミット項目を選択すると、当時の変更点の差分が表示される。
また、コミット項目上コンテキストメニューからは次のコマンドなどを実行することが可
能だ：

* :guilabel:`Copy Commit ID`
* :guilabel:`Copy Commit Messsage`

拡張機能
======================================================================

.. todo::

   GitHub 関係の拡張しか言及しないので、別の章での記述する？

出力確認
======================================================================

VS Code の Git 操作コマンドが実際に実行するコマンドラインを確認する方法がある。
コマンド :guilabel:`Git: Show Git Output` を直接実行する。

1. :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`U` を押すなどして、画面下部パネルの
   :guilabel:`OUTPUT` を開く。
2. タブバー右側ドロップダウンリストから :guilabel:`Git` を選択する。

ログが表示される。タイムスタンプ、コマンドライン、実行時間を確認できる。

.. admonition:: 利用者ノート

   Git を端末で利用するのを好むならば、このログは一度は見る方がいい。

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
