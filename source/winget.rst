======================================================================
Windows Package Manager CLI 利用ノート
======================================================================

このノートの目的は、Windows 10 で :command:`winget` を利用可能な状態にすることだ。
成功すれば、手動で更新していた各種 Windows プログラムのアップグレード作業が著しく楽になるはずだ。

.. contents:: ノート目次

リンク
======================================================================

本稿でゴチャゴチャ記すことはしたくない。公式文書や先人たちの成果をありがたくいただくことにする。

* `GitHub - microsoft/winget-cli: Windows Package Manager CLI (aka winget) <https://github.com/microsoft/winget-cli>`__:
  本ノートではこれを公式サイトとみなす。
* `Windows Package Manager - Wikipedia <https://en.wikipedia.org/wiki/Windows_Package_Manager>`__:
  簡潔で読みやすい。
* `Windows 環境再構築をコマンドラインで自動化可能にする Microsoft 製ツール「winget」とは <https://atmarkit.itmedia.co.jp/ait/articles/2012/03/news017.html>`__:
  このタイトルが目的だ。
* `コマンド一発でアプリをセットアップ ～CUI のアプリ管理ツール「winget」が v1.0 に - 窓の杜 <https://forest.watch.impress.co.jp/docs/news/1327406.html>`__:
  この記事で役に立つ内容はインストール手順だろう。
* `How to Use WINGET on Windows 11 - All Things How <https://allthings.how/how-to-use-winget-on-windows-11/>`__:
  包括的で良い。一般的な利用例は全部書かれていると思ってかまわないだろう。
  この内容は Windows 10 でも役に立つ。

インストール
======================================================================

Windows Package Manager CLI のインストール手順を簡単に記す。

まずコマンドプロンプトを起動する。おもむろに :command:`winget -v` を実行する。
バージョン番号に preview が付いている場合にはこれをアンインストールする。
何も実行されないようならば問題なく次の工程に進むこと。

本プログラムを Windows にインストールする。Microsoft Store 経由でインストールするのが推奨手段とされている。
検索ボックスで App Installer と入力して検索する。出てくるものをインストールする。
この問い合わせ文字列がわかりにくかった。

インストールが終わったらコマンド :command:`winget -v` を実行して利用可能であることを確認する。

.. code:: doscon

   > winget -v
   v1.1.13405

設定
======================================================================

Windows Package Manager CLI の設定手順について簡単に記す。

CLI であるので、利用者の中では既定のコマンドラインオプションがあれば、
それらをテキストファイルにあらかじめ指定しておく方式となる。

コマンド :command:`winget settings` を実行すると、設定ファイルがテキストエディターに開かれる。
設定ファイルは JSON ファイル ``settings.json`` だ。
これは複雑なパスに配置されているのでバックアップやバージョン管理の際に注意を要する。

.. code:: text

   %LOCALAPPDATA%\Packages\Microsoft.DesktopAppInstaller_8wekyb3d8bbwe\LocalState\settings.json

設定項目仕様は公式サイトの ``Settings.md`` に記載されている。

現在試行中の設定内容を次に示す：

.. code:: json

   {
       "$schema": "https://aka.ms/winget-settings.schema.json",
       "source": {
           "autoUpdateIntervalInMinutes": 0
       },
       "installBehavior": {
           "preferences": {
               "scope": "machine"
           }
       },
       "telemetry": {
           "disable": true
       },
       "network": {
           "downloader": "default",
           "doProgressTimeoutInSeconds": 60
       }
   }

利用例
======================================================================

Windows Package Manager CLI の性質上、利用例は限定される。

.. note::

   UNIX/Linux コマンドとは異なり ``winget`` はコマンドライン文字列の大文字小文字を区別しない。

コマンド一覧を確認する
----------------------------------------------------------------------

引数なしでコマンド ``winget`` を実行すると、出力の一部にコマンド一覧が現れる。
次にその内容を引用する：

.. code:: text

   使用状況: winget [<コマンド>] [<オプション>]

   使用できるコマンドは次のとおりです:
     install    指定されたパッケージをインストール
     show       パッケージに関する情報を表示します
     source     パッケージのソースの管理
     search     アプリの基本情報を見つけて表示
     list       インストール済みパッケージを表示する
     upgrade    指定されたパッケージをアップグレードします
     uninstall  指定されたパッケージをアンインストール
     hash       インストーラー ファイルをハッシュするヘルパー
     validate   マニフェスト ファイルを検証
     settings   設定を開くか、管理者設定を設定する
     features   試験的な機能の状態を表示
     export     インストールされているパッケージのリストをエクスポート
     import     ファイル中のすべてのパッケージをインストール

   特定のコマンドの詳細については、そのコマンドにヘルプ引数を渡します。 [-?]

   次のオプションを使用できます。
     -v,--version  ツールのバージョンを表示
     --info        ツールの一般情報を表示

   詳細については、次を参照してください。 https://aka.ms/winget-command-help

プログラムをインストールする
----------------------------------------------------------------------

次のコマンドは VS Code を Microsoft Store や WinGet のリポジトリーなどから検索して、
存在すればインストールする：

.. code:: doscon

   > winget install --exact --id Microsoft.VisualStudioCode

この方式では、オプション ``--id`` の引数を知っていなければならない。
例えば、コマンド ``winget search`` を実行するなどして、欲しいプログラムごとに情報を別途得るといい。

既存のプログラムを更新する
----------------------------------------------------------------------

すでにインストール済みのプログラムのバージョンを最新にしたい。これがもっとも多い利用例だと思う。
特定のプログラムだけ更新する場合と、管理可能なプログラムすべてを更新する場合とがある。

.. code:: doscon

   > winget upgrade --exact --id Microsoft.VisualStudioCode
   > winget upgrade --all

どのプログラムが更新対象であるかを調べるには、引数なしで実行し Available 列を見ればよい。

.. code:: doscon

   > winget upgrade

新しい Windows PC に移行する
----------------------------------------------------------------------

新しい Windows PC でも同じプログラム集合を利用したいのが自然だ。
Python のパッケージ環境を移行するのと考え方は似ている。
プログラム一覧を移行元でエクスポートして、移行先でインポートするという手順だ。

.. code:: doscon

   > winget export -o winget.json

JSON ファイルが生成される。これを移行先システムに何らかの手段でコピーし、インポートする：

.. code:: doscon

   > winget import -i winget.json

その他
======================================================================

WSL からコマンドを実行できるようにする
----------------------------------------------------------------------

通常、パスが通っていれば WSL 環境でも `winget.exe` を実行することは可能だ。

.. code::text

   %LOCALAPPDATA%\Microsoft\WindowsApps\winget.exe
