======================================================================
Windows Package Manager CLI 利用ノート
======================================================================

このノートの目的は Windows 10/11 における :program:`winget` の利用手引となること
だ。従来はプログラムごとにインストーラーを手動でダウンロード、実行することで更新
してきた Windows プログラムのアップグレード作業が、本ツールを導入することで著し
く楽になる。

.. contents:: ノート目次

インストール
======================================================================

.. caution::

   本節は Windows 11 では不要だ。

Windows Package Manager CLI のインストール手順を簡単に記す。

まずコマンドプロンプトを起動する。おもむろに :command:`winget -v` を実行する。
バージョン番号に preview が付いている場合にはこれをアンインストールする。
何も実行されないようならば問題なく次の工程に進むこと。

本プログラムを Windows にインストールする。Microsoft Store 経由でインストールす
るのが推奨手段とされている。検索ボックスで :code:`App Installer` と入力して検索
する。出てくるものをインストールする。この問い合わせ文字列がわかりにくかった。

インストールが終わったらコマンド :command:`winget -v` を実行して利用可能であるこ
とを確認する。

設定
======================================================================

Windows Package Manager CLI の設定手順について簡単に記す。

CLI であるので、利用者の中では既定のコマンドラインオプションがあれば、それらをテ
キストファイルにあらかじめ指定しておく方式となる。

コマンド :command:`winget settings` を実行すると、設定ファイルがテキストエディ
ターに開かれる（存在しない場合は :program:`winget` がこのファイルを用意してそれ
を開く）。実際には、このファイルは次のパスに位置する：

.. sourcecode:: text
   :force:

   %LOCALAPPDATA%\Packages\Microsoft.DesktopAppInstaller_8wekyb3d8bbwe\LocalState\settings.json

設定項目仕様は公式サイトの `WinGet CLI Settings`_ に記載されている。

現在試行中の設定内容を次に示す：

.. sourcecode:: json
   :caption: :file:`settings.json` 構成例
   :force:

   {
       "$schema": "https://aka.ms/winget-settings.schema.json",
       "source": {
           "autoUpdateIntervalInMinutes": 0,
           "installBehavior": {
               "preferences": {
                   "scope": "machine"
               }
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

この中では ``scope`` の指定が最も重要だ。このオプションを指定しないとインストー
ル系コマンドでユーザーインストールが実施されるはずであり、パッケージの在り処が
``%PROGRAMFILES%`` 系ではなく ``%APPDATA%`` 系になってしまう。この挙動を許すと、
ストレージバックアップの邪魔になる。

利用例
======================================================================

Windows Package Manager CLI の性質上、利用例は限定される。

.. note::

   UNIX/Linux コマンドとは異なり :command:`winget` はコマンドライン文字列の大文
   字小文字を区別しない。

バージョンを確認する
----------------------------------------------------------------------

.. sourcecode:: pwsh-session
   :caption: :program:`winget` のバージョン情報を示す
   :force:

   PS> winget -v
   v1.12.350

コマンド一覧を確認する
----------------------------------------------------------------------

引数なしでコマンド :command:`winget` を実行すると、出力の一部にコマンド一覧が現
れる。その内容の一部を次に引用する：

.. sourcecode:: text
   :caption: :program:`winget` ヘルプ出力（抄）
   :force:

   usage: winget  [<command>] [<options>]

   The following commands are available:
     install    Installs the given package
     show       Shows information about a package
     source     Manage sources of packages
     search     Find and show basic info of packages
     list       Display installed packages
     upgrade    Shows and performs available upgrades
     uninstall  Uninstalls the given package
     hash       Helper to hash installer files
     validate   Validates a manifest file
     settings   Open settings or set administrator settings
     features   Shows the status of experimental features
     export     Exports a list of the installed packages
     import     Installs all the packages in a file
     pin        Manage package pins
     configure  Configures the system into a desired state
     download   Downloads the installer from a given package
     repair     Repairs the selected package
     dscv3      DSC v3 resource commands
     mcp        MCP information

   ...

サブコマンドの一覧がわかる。それぞれのコマンドラインの仕様は ``--help`` で見れば
よい。例えば：

.. sourcecode:: pwsh-session
   :caption: ``winget upgrade`` のヘルプを出力するコマンド
   :force:

   PS> winget upgrade --help

プログラムを探す
----------------------------------------------------------------------

端末ウィンドウを開いたはいいが、パッケージの ID をうっかり忘れた場合に役に立つコ
マンドがある：

.. sourcecode:: pwsh-session
   :caption: ``winget search`` 実行例
   :force:

   PS> winget search VLC
   Name             Id                   Version              Match        Source
   -------------------------------------------------------------------------------
   VLC              XPDM1ZW6815MQM       Unknown                           msstore
   VLC UWP          9NBLGGH4VVNH         Unknown                           msstore
   VLC media player VideoLAN.VLC         3.0.21               Moniker: vlc winget
   pympress         Cimbali.pympress     1.8.6                Tag: vlc     winget
   Screenbox        Starpine.Screenbox   0.16.0               Tag: vlc     winget
   Streamlink       Streamlink.Streamli… 7.6.0-1              Tag: vlc     winget
   wcap             mmozeiko.wcap        2025.05.26           Tag: vlc     winget
   SubRenamer       qwqcode.SubRenamer   2.4.0                Tag: vlc     winget
   tuna             univrsal.tuna        1.9.11               Tag: vlc     winget
   VLC media player VideoLAN.VLC.Nightly 4.0.0.0-nightly2025…              winget

この出力により、インストールコマンドは ``winget install --id VideoLAN.VLC`` であ
ることを思い出すことができるのだ。

プログラムをインストールする
----------------------------------------------------------------------

次のコマンドは VS Code を Microsoft Store や :program:`winget` のリポジトリーな
どから検索して、存在すればインストールする：

.. sourcecode:: pwsh-session
   :caption: ``winget install`` コマンド例
   :force:

   PS> winget install --exact --id Microsoft.VisualStudioCode

この方式では、オプション ``--id`` の引数を知っていなければならない。例えば、コマ
ンド :command:`winget search` を実行するなどして、欲しいプログラムごとに情報を別
途得るといい。

前述の設定ファイルでシステムインストールを指定していない場合には（そうするべきだ
がひとまず）オプション ``--scope machine`` をさらに加えてユーザーインストールを
回避したい。

プログラムをアンインストールする
----------------------------------------------------------------------

スコープを間違えたなど、インストールしたばかりのパッケージをアンインストールする
ときには ``winget uninstall`` を実行する。適切なコマンドライン引数がコマンド履歴
に残っているはずなので、それをそのまま使え。

.. sourcecode:: pwsh-session
   :caption: ``winget uninstall`` コマンド例
   :force:

   PS> winget uninstall --exact --id Microsoft.VisualStudioCode

既存のプログラムを更新する
----------------------------------------------------------------------

すでにインストール済みのプログラムのバージョンを最新にしたい。これがもっとも多い
利用例だと思う。特定のプログラムだけ更新する場合と、管理可能なプログラムすべてを
更新する場合とがある。どちらも同じサブコマンド ``upgrade`` を実行する：

.. sourcecode:: pwsh-session
   :caption: ``winget upgrade`` コマンド例
   :force:

   PS> winget upgrade --exact --id Microsoft.VisualStudioCode
   PS> winget upgrade --all

どのプログラムが更新対象であるかを調べるには、引数なしで実行し ``Available`` 列
を見ればよい。

.. sourcecode:: pwsh-session
   :caption: 更新候補一覧を得る例
   :force:

   PS> winget upgrade
   Name                    Id                   Version     Available   Source
   ---------------------------------------------------------------------------
   Google 日本語入力       Google.JapaneseIME   2.31.5840.0 2.32.5990.0 winget
   Zoom Workplace (64-bit) Zoom.Zoom            6.6.19369   6.6.19875   winget
   Dropbox                 Dropbox.Dropbox      235.4.5905  236.3.5770  winget
   OBS Studio              OBSProject.OBSStudio 32.0.1      32.0.2      winget
   4 upgrades available.

.. tip::

   ``Id`` 列を十分長く出力したいなどの整形をしたい場合は PowerShell の機能を使え。

新しい Windows PC に移行する
----------------------------------------------------------------------

新しい Windows PC でも同じプログラム集合を利用したいのが自然だ。Python のパッ
ケージ環境を移行するのと考え方は似ている。プログラム一覧を移行元でエクスポートし
て、移行先でインポートするという手順だ。

.. sourcecode:: pwsh-session
   :caption: ``winget export`` コマンド例
   :force:

   PS> winget export -o winget.json

この例では JSON ファイル :file:`winget.json` が生成される。このファイルを移行先
システムに USB 記憶機器やネットワーク接続などの手段でコピーし、そのフォルダーへ
移動してインポートコマンドを実行する：

.. sourcecode:: pwsh-session
   :caption: ``winget export`` コマンド例
   :force:

   PS> winget import -i winget.json

成功した場合に限り、このファイルを削除しろ。

移行先環境の :program:`winget` 環境が未整備であると、システムインストールではな
く既定のユーザーインストールになってしまう。繰り返すが ``--scope machine`` もし
くは設定ファイルでの指示を忘れるな。

その他
======================================================================

何ヶ月経ってもパッケージをアップグレードしてくれないとき
----------------------------------------------------------------------

コマンド :command:`winget upgrade` でいつまでも更新可能なパッケージがないと表示
され続ける場合、コマンド :command:`winget source update` で解決する場合がある。

.. sourcecode:: pwsh-session
   :caption: ``winget source update`` 実行例
   :force:

   PS> winget source update
   Updating all sources...
   Updating source: msstore...
   Done
   Updating source: winget...
     ██████████████████████████████  100%
   Done
   Updating source: winget-font...
   Done

このあと :command:`winget upgrade` すると、更新可能なパッケージ一覧が出力される
ことがある。

最近のバージョンでは自動更新されているように見受けられる。

資料
======================================================================

公式文書や先人たちの成果をありがたくいただくことにする。

* `GitHub - microsoft/winget-cli: Windows Package Manager CLI (aka winget) <https://github.com/microsoft/winget-cli>`__:
  本ノートではこれを公式サイトとみなす。

  * `WinGet CLI Settings`_: 設定ファイル解説。
* `Windows Package Manager - Wikipedia <https://en.wikipedia.org/wiki/Windows_Package_Manager>`__:
  簡潔で読みやすい。
* `Windows 環境再構築をコマンドラインで自動化可能にする Microsoft 製ツール「winget」とは <https://atmarkit.itmedia.co.jp/ait/articles/2012/03/news017.html>`__:
  このタイトルが目的だ。
* `How to Use WINGET on Windows 11 - All Things How <https://allthings.how/how-to-use-winget-on-windows-11/>`__:
  包括的で良い。一般的な利用例は全部書かれていると思ってかまわないだろう。この内
  容は Windows 10 でも役に立つ。

.. _`WinGet CLI Settings`: https://github.com/microsoft/winget-cli/blob/master/doc/Settings.md
