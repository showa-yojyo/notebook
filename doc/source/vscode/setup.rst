======================================================================
セットアップ
======================================================================

本章では VS Code 本体を Windows 環境にインストールする方法や、それに関連する事項
について記す。

.. attention::

   :doc:`./index` 冒頭の前提条件に留意すること。

.. contents::

インストール
======================================================================

VS Code をインストールする手段は複数用意されている。主なものを列挙する：

* `公式ダウンロードページ <https://code.visualstudio.com/Download>`__ からインス
  トーラーをダウンロードして実行する。
* Microsoft Store からインストールする。
* Windows Package Manager つまり :program:`winget` でインストールする。

  .. code:: doscon

     > winget install -e --id Microsoft.VisualStudioCode

新調するマシンにインストールするときには :program:`winget` を利用することになる
だろう。それも、おそらくインポート方式になる。:doc:`/winget` 参照。

WSL 対応
----------------------------------------------------------------------

WSL のコンソールから VS Code を開けるようにしておく。実行ファイルのあるパスを
環境変数 PATH に追加すればいい。Bash シェルの場合はファイル
:file:`$HOME/.bash_profile` と :file:`$HOME/.bashrc` を適切に選んで次のような記
述を適宜与える：

.. code:: shell

   # probably in .bash_profile
   if [[ -n "$WSL_DISTRO_NAME" ]]; then
      PATH="${PATH:+${PATH}:/mnt/c/Program Files/Microsoft VS Code/bin}"
      # or
      # PATH="/mnt/c/Program Files/Microsoft VS Code/bin}${PATH:+:${PATH}}"
   fi

   # probably in .bashrc
   export EDITOR='code --wait' # --new-window
   export FCEDIT=$EDITOR
   export GIT_EDITOR=$EDITOR
   # ...

対話的セッションを開始してコマンド :command:`code --version` などを実行して試験
すること。

.. todo::

   コンソールの章で詳しくやった後にリンク。

更新
======================================================================

VS Code 本体の更新もインストール同様、手段が複数ある。
通常は VS Code メインウィンドウの UI から実施する。

1. :guilabel:`Help` メニューまたは Activity Bar 下の歯車アイコンメニューを開く。
2. :guilabel:`Check for Updates...` を選択する。
3. 更新が可能な場合には画面右下に

   > :guilabel:`Restart Visual Studio Code to apply the latest update.`

   というメッセージボックスがポップアップする。:guilabel:`Update Now` ボタンを押
   してプログラムを再起動する。またはやりかけの編集を終えてから手動で
   ウィンドウを閉じても構わない。次の起動時に更新が適用されている。

VS Code にはインストールされている拡張機能に対しても更新するという手順が存在する。
それについては別のページに記す。

バックアップおよび復元
======================================================================

VS Code におけるバックアップ、復元の考え方はユーザー設定のそれを意味する。

.. todo::

   別のページに記してリンク。

アンインストール
======================================================================

Windows から VS Code 本体をアンインストールし、残滓のようなファイル群を手動で削
除するまでを記す。

まず、次のいずれかの（あるいは他の）方法で VS Code 本体を OS から削除する：

* Windows の :guilabel:`プログラムの追加と削除` などからアンインストールを実行する。
* Windows Package Manager つまり :program:`winget` でアンインストールする。

  .. code:: doscon

     > winget uninstall -e --id Microsoft.VisualStudioCode

次に設定ファイルなどを手動で削除する。以下のフォルダーを確認して必要なら削除する：

* :file:`%APPDATA%\Code`
* :file:`%USERPROFILE%\.vscode`
