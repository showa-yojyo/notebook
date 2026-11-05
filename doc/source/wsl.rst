================================================================================
Windows Subsystem for Linux 利用ノート
================================================================================

WSL に関する利用ノートをつづる。次の課題を解決したい：

* インストールおよびアップグレードの方法を会得する。
* WSL を管理する方法を会得する。
* Linux ディストリビューション (Ubuntu) に関する操作を会得する。
* WSL に関する構成方法を理解する。
* Windows と WSL/Linux との連携の仕組みを模索する。

Linux 用 Windows Subsytem for Linux (WSL) を使用すると、従来の仮想マシンなどの
オーバーヘッドなしで、コマンドラインツール、ユーティリティー、アプリケーションな
どを含む GNU/Linux 環境のほとんどを、変更せずに Windows 上で直接実行できる。

.. note::

   本ノートの初版を記すのに用いていた Windows 本体、Ubuntu のバージョン情報はそ
   れぞれ次のとおりだ。

   :Windows: 10 Home; 22H2 19045.2006
   :Ubuntu: 20.04 LTS

   その後かなり間が空き Windows 10 のサポート終了に伴う環境移行を敢行。移行後の
   環境は次のとおり：

   :Windows: 11 Pro; 25H2 26200.7019, 26H2 26300.9818
   :Ubuntu: 24.04.3 LTS, 26.04.1 LTS

.. admonition:: 関連ノート

   `WSL Documentation 読書ノート`_

.. contents:: 見出し一覧
   :local:

インストール
================================================================================

公式文書によると最初から :program:`wsl` が利用可能であるようだ。次のコマンドを実
行しろとある：

.. sourcecode:: pwsh-session
   :caption: WSL インストールコマンド
   :force:

   PS> wsl --install

これが上手くいくと WSL が利用可能になる。上のコマンドではインストールオプション
を指定していないため、Linux のディストリビューションとして Ubuntu が暗黙的に選択
される。

既定の Linux ディストリビューションが Ubuntu であることと、私がそれしか利用しな
いことから、本稿ではこれ以降、この二つの単語を区別なしに記述するかもしれない。

アップグレードする
================================================================================

WSL 自体のアップグレード方法は次のコマンド実行による。これで WSL Linux カーネル
が存在する場合に限り、その最新版に更新される。

.. sourcecode:: pwsh-session
   :caption: WSL 更新コマンド
   :force:

   PS > wsl --update

Linux ディストリビューションのアップグレード方法を Ubuntu を例にとって記す。おそ
らく次の方法すべてが等価で有効だ：

1. コンソールから :command:`winget upgrade -e --id Canonical.Ubuntu` を実行
2. Microsoft Store から :program:`Ubuntu on Windows` を更新

Use Cases
================================================================================

プログラム :program:`wsl` が利用者に用意している機能は次の二つに分類される：

* Linux プログラムを実行する
* WSL を管理する

Linux プログラムを実行する
--------------------------------------------------------------------------------

Linux コマンドを指定しないで実行すると、Linux シェルを起動する。

.. sourcecode:: pwsh-session
   :caption: Ubuntu 起動コマンド
   :force:

   PS> wsl
   PS> wsl --distribution Ubuntu

Linux コマンド ``COMMAND_LINE`` を実行するには次のどちらかの形式を入力する。前者
はコマンドラインがシェルに渡る。後者はシェルを起動せずに実行するので、コマンドラ
イン文字列が解析されない。

.. sourcecode:: pwsh-session
   :caption: Linux コマンドを Windows から実行する例

   PS> wsl COMMAND_LINE
   PS> wsl --execute COMMAND_LINE

コマンドにはコマンドラインオプションを付与することもできる。システムにディストリ
ビューションが複数存在する場合には ``--distribution DISTRO_NAME`` で Linux ディ
ストリビューションを指定することが可能。実行環境を指定する ``--cd WORK_DIR`` や
``--user USER`` を使うことがあるかもしれない。

.. sourcecode:: pwsh-session
   :caption: Linux コマンドを Windows から実行する例
   :force:

   PS> wsl --cd /tmp -e pwd
   /tmp

Bash のような引数リストマーカー ``--`` も使える。

WSL を管理する
--------------------------------------------------------------------------------

WSL 管理ツールとしての用途としては、次のものがある：

* :program:`wsl` のコマンドライン仕様を確認する
* WSL に関する情報を確認する
* Linux ディストリビューションを一覧する
* Linux ディストリビューションをインストールする
* WSL カーネルを更新して最新にする
* WSL の各種既定バージョン (1 or 2) を指定する
* Linux ディストリビューションイメージを操作する
* 実行中の仮想マシンすべてを即終了する
* Linux ディストリビューションを終了する
* Linux ディストリビューションを削除する

インストールと更新については記したので、以下ではその他の用途を見ていく。

WSL に関する情報を確認する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

サブコマンド ``--status`` で既定の Linux ディストリビューションの種類、カーネル
バージョンなど、WSL に関する一般的な情報を出力する。簡単なコマンドなので実行例を
記す：

.. sourcecode:: pwsh-session
   :caption: WSL 情報を出力するコマンドの実行例
   :force:

   PS> wsl --status
   Default Distribution: Ubuntu
   Default Version: 2
   WSL1 is not supported with your current machine configuration.
   Please enable the "Windows Subsystem for Linux" optional component to use WSL1.

Linux ディストリビューションを一覧する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

サブコマンド ``--list`` は Linux ディストリビューションを確認する。次の使用状況
があり得る：

* 管理下にあるディストリビューションを一覧する
* 現在実行中のディストリビューションを表示する
* インストール可能なディストリビューションを一覧する

コマンド入出力例を記す：

.. sourcecode:: pwsh-session
   :caption: ``wsl --list`` コマンド実行例
   :force:

   PS> wsl --list
   Windows Subsystem for Linux Distributions:
   Ubuntu (Default)

   PS> wsl --list --all
   Windows Subsystem for Linux Distributions:
   Ubuntu (Default)

   PS> wsl --list --quiet
   Ubuntu

   PS> wsl --list --verbose
     NAME      STATE           VERSION
   * Ubuntu    Running         2

   PS> wsl --list --running
   Windows Subsystem for Linux Distributions:
   Ubuntu (Default)

   PS> wsl --list --online
   The following is a list of valid distributions that can be installed.
   Install using 'wsl.exe --install <Distro>'.

   NAME                            FRIENDLY NAME
   Ubuntu                          Ubuntu
   Ubuntu-26.04                    Ubuntu 26.04 LTS
   Ubuntu-24.04                    Ubuntu 24.04 LTS
   Ubuntu-22.04                    Ubuntu 22.04 LTS
   openSUSE-Tumbleweed             openSUSE Tumbleweed
   openSUSE-Leap-16.1              openSUSE Leap 16.1
   RLCPlus-9                       Rocky Linux Plus 9 (CIQ)
   RLCPlus-10                      Rocky Linux Plus 10 (CIQ)
   SUSE-Linux-Enterprise-15-SP7    SUSE Linux Enterprise 15 SP7
   SUSE-Linux-Enterprise-16.0      SUSE Linux Enterprise 16.0
   kali-linux                      Kali Linux Rolling
   Debian                          Debian GNU/Linux
   AlmaLinux-8                     AlmaLinux OS 8
   AlmaLinux-9                     AlmaLinux OS 9
   AlmaLinux-Kitten-10             AlmaLinux OS Kitten 10
   AlmaLinux-10                    AlmaLinux OS 10
   archlinux                       Arch Linux
   FedoraLinux-45                  Fedora Linux 45
   FedoraLinux-44                  Fedora Linux 44
   eLxr                            eLxr 12.12.0.0 GNU/Linux
   OracleLinux_7_9                 Oracle Linux 7.9
   OracleLinux_8_10                Oracle Linux 8.10
   OracleLinux_9_5                 Oracle Linux 9.5
   SUSE-Linux-Enterprise-15-SP6    SUSE Linux Enterprise 15 SP6

各種の既定バージョンを指定する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: 利用者ノート

   本稿執筆時点では WSL 2 で Ubuntu を利用する状況しかないので、これらの機能を深
   追いしない。

サブコマンド ``--set-default-version`` は WSL の既定バージョンを指定するものだ。

.. sourcecode:: pwsh-session
   :caption: ``wsl --set-default-version`` 実行例
   :force:

   PS> wsl --set-default-version 2
   For information on key differences with WSL 2 please visit https://aka.ms/wsl2
   The operation completed successfully.

サブコマンド ``--set-default`` は既定の Linux ディストリビューションを指定する。
先のコマンドが対象とするバージョンとは、このディストリビューションを利用する WSL
のバージョンものだ。

.. sourcecode:: pwsh-session
   :caption: ``wsl --set-default`` 実行例
   :force:

   PS> wsl --set-default Ubuntu
   The operation completed successfully.

サブコマンド ``--set-version`` は指定ディストリビューションを実行する WSL のバー
ジョンを指定するものだ。Ubuntu を WSL 2 で動作させたい場合には次のようにする：

.. sourcecode:: pwsh-session
   :caption: ``wsl --set-version`` 実行例
   :force:

   PS> wsl --set-version Ubuntu 2
   For information on key differences with WSL 2 please visit https://aka.ms/wsl2
   Conversion in progress, this may take a few minutes.

   The distribution is already the requested version.
   Error code: Wsl/Service/WSL_E_VM_MODE_INVALID_STATE
   If this error was unexpected, please consider searching for existing issues or filing a new issue at https://github.com/microsoft/WSL/issues.

Linux ディストリビューションをインポート・エクスポートする
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. caution::

   この節のコマンド群は採用することがなかった。実際には
   :ref:`anchor-wsl-migration` で述べる手順になった。

サブコマンド ``--import`` および ``--export`` は、Linux ディストリビューションの
ファイルシステムおよびデータ全体を TAR ファイル形式に符号化、復号化する。当然、
利用する用途はバックアップとその回復だ。

バックアップコマンドは ``--export`` を指定する。次のようになる：

.. sourcecode:: pwsh-session
   :caption: ``wsl --export`` で TAR ファイルを出力するコマンド例

   PS> wsl --export Ubuntu ubuntu-bkp.tar

このアーカイブファイルを Linux システムに復元するには ``--import`` する：

.. sourcecode:: pwsh-session
   :caption: ``wsl --import`` で TAR ファイルを出力するコマンド例

   PS> wsl --import DISTRO_NAME DISTRO_LOCATION ubuntu-bkp.tar

ここで引数 ``DISTRO_NAME`` と ``DISTRO_LOCATION`` は復元後の Linux システムの名
前と、それを配置する Windows 視点でのパスを表す。

.. admonition:: 利用者ノート

   記憶領域媒体によって上記サブコマンドの性能に大きな差が生じるようだ。HDD では
   遅く SSD では速いのは想像に難くない。ファイルシステムの断片化がシリアライズ処
   理に影響するとか。現に、私の環境では ``--export`` が何分経っても TAR ファイル
   のサイズが変わらないままだった。

注意点が二つある：

* 作業前に WSL を完全に停止すること。
* ``wsl --export`` するまでは登録解除系のコマンドを決して実行するな。WSL イメー
  ジが消滅する。
* ``wsl --import`` すると、おそらく Ubuntu コンソールを起動したときにユーザーを
  「忘れている」状態でプロンプトが示される。その場合にはファイル
  :file:`/etc/wsl.conf` を root で編集して既定ユーザーを示すこと。

実行中の仮想マシンすべてを即終了する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

サブコマンド ``--shutdown`` は実行中のディストリビューション全部と、WSL 2 仮想マ
シンを直ちに終了する。

.. sourcecode:: pwsh-session
   :caption: WSL を終了するコマンド
   :force:

   PS> wsl --shutdown

仮想マシンを再起動をするには、Linux プログラムを実行するようなコマンド呼び出しを
:program:`wsl` を介して実行すればよい。

.. admonition:: 利用者ノート

   このコマンドは構成変更時など、仮想マシン環境の再起動が必要な場合に実行するの
   が通常の運用だが、PC のメモリー容量が乏しい環境では、メモリーが逼迫してきたと
   きに WSL を終了して、それをやりくりするのに援用することもある。

Linux ディストリビューションを停止する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

サブコマンド ``--terminate`` は指定したディストリビューションを終了する。

.. sourcecode:: pwsh-session
   :caption: ディストリビューションを停止する手順例
   :force:

   PS> wsl --list --running
   Windows Subsystem for Linux Distributions:
   Ubuntu (Default)

   PS> wsl --terminate Ubuntu

   PS> wsl --list --running
   There are no running distributions.

Linux ディストリビューションを抹消する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

このコマンドは Linux ディストリビューションのメジャーアップグレード作業発生時に
利用する可能性があるので、ここに記す。

サブコマンド ``--unregister`` は、指定した Linux ディストリビューションのファイ
ルシステムすべてとその中に含まれるデータすべてを完全に破壊する。

.. sourcecode:: pwsh-session
   :caption: ディストリビューションを完全消去するコマンド例
   :force:

   > wsl --unregister Ubuntu

実行後、:command:`wsl --list --all` の出力を確認すると、この Ubuntu は存在しない
だろう。

構成
================================================================================

.. warning::

   本節では WSL 2 に限定して記述する。

WSL は二段構えの構成手段を採用している。WSL 全体に対するものと、Linux ディストリ
ビューション個別に対応するものだ。どちらもテキストベースのファイルで構成内容を指
示する仕組みだ。WSL が起動するたびにこれらの構成ファイルが（記法が妥当な場合に限
り）読み込まれ、適用される。

ファイル :file:`%USERPROFILE%\\.wslconfig`
--------------------------------------------------------------------------------

ファイル :file:`.wslconfig` は WSL 全体を統括する構成を指示する。Windows のフォ
ルダー ``%USERPROFILE%`` に置かれる。このファイルを手動で設置してかまわない。

.. tip::

   最近の WSL には GUI 構成アプリケーション :program:`wslsettings.exe` が同梱さ
   れている。これを使えば記述ミスがなくなる。

構成項目すべてを理解する必要はまだないので、私の環境の設定内容を記す。

.. sourcecode:: dosini
   :caption: :file:`.wslconfig` ``wsl2`` 区画構成例
   :force:

   [wsl2]
   memory=12G
   processors=2
   swap=1GB
   networkingMode=mirrored

   [experimental]
   autoMemoryReclaim=gradual
   sparseVhd=true

キー ``memory`` は WSL 仮想マシンに割り当てるメモリー容量だ。

キー ``swap`` は WSL 仮想マシンに追加するスワップ領域の容量だ。スワップファイル
がない場合は 0 とする（註＊スワップ領域とは、メモリー需要がハードウェア器機の制
限を超過する状況で使用される「ディスク上のメモリー」だ）。

キー ``networkingMode`` は Windows と仮想環境のネットワーク方式を値に指定する。
値 ``mirrored`` に設定することで、Windows のネットワークインターフェイスを
Ubuntu 側に丸写しする。これにより、次の長所が得られる：

* VPN との互換性向上
* マルチキャスト可能
* IPv6 利用可能

.. admonition:: 関連ノート

   * `.wslconfig <https://gist.github.com/showa-yojyo/4c2d8e631b1accf3ef8655c419f809a3>`__

ファイル :file:`/etc/wsl.conf`
--------------------------------------------------------------------------------

ファイル :file:`/etc/wsl.conf` は Linux ディストリビューションごとに用意できる。
このファイルが指示する構成内容は、当然ながらこのファイルを特定の Linux ディスト
リビューションにしか適用されない。

マニュアルによると次の構成を指示できるようだ：

* 自動マウントを設定する
* ネットワークを設定する
* Windows と WSL の間の相互運用を設定する
* WSL のユーザーを設定する
* ブートを設定する

このファイルを編集するには管理者権限を要する。例えば ``sudo -e /etc/wsl.conf``
を実行してエディターを開くことで編集する。

.. admonition:: 関連ノート

   より細かい解説を次のファイルに記した：

   * `wsl.conf ノート <https://gist.github.com/showa-yojyo/d99d0f14c15b1a64f77e49c482ded9ea>`__

.. _anchor-wsl-migration:

新 PC にディストリビューションを移行する
================================================================================

大まかな手順は次のとおり。実際には VHDX ファイルのサイズを切り詰める工程をエクス
ポート前後に入れる。詳細な手順は資料 wsl1_ と wsl2_ を合わせて見ろ。

移行元環境：

#. Linux 側でゴミファイルを削除する
#. WSL を停止する
#. Linux のイメージファイルをエクスポートする
#. このイメージファイルのサイズを切り詰める
#. このイメージファイルを移行先に設けた共有フォルダーに移す

移行元環境で実行するエクスポートコマンドは上述の TAR 形式ではなく VHDX 形式とし
たい：

.. sourcecode:: pwsh-session
   :caption: ``wsl --export --vhdx`` コマンド例
   :force:

   PS> wsl --export --vhdx Ubuntu "path-to-ext4.vhdx"

移行先環境：

#. WSL をインストールする（必要に応じて Windows を再起動する）
#. イメージファイルを共有フォルダーから管理しやすい場所に移す
#. このイメージファイルをインポートする

移行先環境で実行するインポートコマンドは次のようになる：

.. sourcecode:: pwsh-session
   :caption: ``wsl --import-in-place --vhdx`` コマンド例
   :force:

   PS> wsl --import-in-place Ubuntu "path-to-ext4.vhdx"

イメージファイルのエクスポートを省略して、元イメージをそのまま用いる方法もあるら
しい。それがありなら外付け SSD に入れて複数台からアクセス可能にするかも？

Windows との連携
================================================================================

今すぐ思いつくものを列挙しておく。他にもコツがあるだろう。

* Windows 側の Explorer に Linux ディストリビューションのファイルシステムに
  :guilabel:`ネットワークドライブの割り当て` をしておくといいかもしれない。私は
  U ドライブに ``\\wsl$`` を指定している。
* Windows Terminal を利用しているならば、一度は設定画面を確認しておくべきだ。
  WSLで Linux ディストリビューションを追加すると、便利なことに Windows Terminal
  にプロファイルが自動的に定義される。
* Windows 側で Visual Studio Code を利用しているならば、WSL 関連の追加設定をする
  べきだ。これについては関連ノートに記す。
* Windows の細かい設定を管理するのに PowerShell, つまり :program:`pwsh.exe` を実
  行可能にしておく。
* Windows に PowerToys をインストールしている場合、Peek の CLI 版実行形式をファ
  イルビューワーとして活用する。手順を関連ノートに詳しく記す。
* Windows 環境変数 ``WSLENV`` を所定の書式で定義することで、Windows と Linux と
  で環境変数を共有することが可能だ。`WSL Documentation 読書ノート`_ で具体的な設
  定例を示す。

.. admonition:: 関連ノート

   * :doc:`/wt`
   * :doc:`/vscode/index`
   * `PowerToys.Peek.UI.exe 利用ノート
     <https://gist.github.com/showa-yojyo/bcfb33d895dced528e8c6d04511df9c2>`__

資料
================================================================================

* `Windows Subsystem for Linux Documentation | Microsoft Learn <https://learn.microsoft.com/en-us/windows/wsl/>`__
* `Terminate Running WSL Linux Distro in Windows 10 <https://winaero.com/terminate-running-wsl-linux-distro-windows-10/>`__
* `How to completely remove a Linux distro from WSL | Windows Central <https://www.windowscentral.com/how-completely-remove-linux-distro-wsl>`__

次の二つの資料は Windows 11 新 PC を導入したときにたいへん参考になった：

* `WSL でストレージ不足エラーが発生したときの対処方法：別マシンへ ext4.vhdx を移して復旧する手順 <wsl1>`_
* `[wsl2]ディスク容量が満タンで困った！＞＜でも、Optimize-VHDなんて存在しないとき <wsl2>`_

.. _wsl1: https://qiita.com/ootakazuhiko/items/c08311ad61183c4127f4
.. _wsl2: https://qiita.com/siruku6/items/c91a40d460095013540d
.. _WSL Documentation 読書ノート: https://gist.github.com/showa-yojyo/07644b4ded83b434589affdf6dcccfb4
