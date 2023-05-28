======================================================================
Windows Subsystem for Linux GUI 利用ノート
======================================================================

.. contents::

WSLg に関する利用ノートをつづる。次の課題を解決したい：

* インストールおよびアップグレードの方法を会得する。
* WSLg を管理する方法を会得する。
* Linux GUI アプリケーションを起動する方法を会得する。
* 起動不能問題を解決する方法を知る。

.. note::

   本稿でも引き続き WSL と単に言う場合でも WSL 2 を指す。ただし、インストールは
   現在完了していて正常に稼働しているとする。

   WSL の distribution は Ubuntu しかインストールしていないので、以下の記述で
   Ubuntu とある部分すべてを他の distribution に置換して読んでも、機能として成立
   するはずだ。

   WSLg に関する作業に限った話ではないが、Ubuntu パッケージを新しくインストール
   する前には必ず ``apt update`` を実行しておくものとする。

   本稿執筆時の環境情報は次のとおり：

   :Windows: Home version 22H2 Build 19045.2908
   :GPU: Intel HD Graphics 4600
   :WSL 2: 5.15.90.1
   :WSLg: 1.0.50
   :Ubuntu: 22.04.2 LTS

目的
======================================================================

画像を表示したり、音声を再生したりする Linux プログラムを正常に実行したい。ここ
でいう Linux プログラムは、結果としてそうなるものも含む。例えば、Matplotlib プ
ロットを出力する Python スクリプトなども含まれる。

メディアファイルの内容を確認するだけならば Windows 側のアプリケーションを呼び出
せば十分だが、どうしても WSL 側でウィンドウを生成したい場合がある：

* Pillow の ``show`` またはそれを間接的に利用するアプリケーション
* FFmpeg の ``ffplay``

幸い、最近になって WSLg というものが Windows 10 の WSL でも動作するようになって
くれた。WSLg とは何か、開発陣の言葉から引用するとこうだ：

    WSLg is short for Windows Subsystem for Linux GUI and the purpose of the
    project is to enable support for running Linux GUI applications (X11 and
    Wayland) on Windows in a fully integrated desktop experience.

コマンドラインから GUI を起動できるのはひじょうに便利なので、環境構築を確実にし
たい。

.. seealso::

   * :doc:`/python-pillow`
   * :doc:`/python-matplotlib/index`
   * :doc:`/ffmpeg/index`

WSLg をインストール・更新する
======================================================================

私の環境は前述のとおり WSL が稼働している。ここでは WSL のインストールについては
述べず、WSLg のインストール、更新、状態確認に集中して記述する。

WSL のインストールがされていない場合
----------------------------------------------------------------------

   From a command prompt with administrator privileges, run the command ``wsl
   --install -d Ubuntu``, then reboot if prompted.
   （中略）
   Voilà! WSL and WSLg are installed and ready to be used!

WSL すらインストールされていない場合、それをインストールすれば WSLg も同時にイン
ストールされると開発陣の文書に述べられている。そちらのほうが話が早いので、この
ノートは不要かもしれない。

したがって、Windows PC を新調する場合には、難しいことを気にせずに済みそうだ。

WSLg 稼働実績がない場合
----------------------------------------------------------------------

WSLg を一度も動作したことがない場合には Windows 側のコンソールで次のコマンドを実
行しておく必要があるはずだ：

.. code:: posh

   > wsl --update
   > wsl --shutdown

コツをまとめる：

* すべての :command:`wsl` コマンドは管理者として実行する。
* コマンド :command:`wsl --update` は WSL と WSLg の両方を最新に更新すると覚えて
  おいて間違いない。
* 変更を有効にするには WSL の再起動が要る。そのための :command:`wsl --shutdown`
  だ。このコマンドはいつもならメモリー確保目的で実行しているものだ。

あとは GUI パッケージを Ubuntu 端末から :command:`apt` を実行することで得る。こ
れで WSLg が有効になっていて欲しい。

WSLg を更新する
----------------------------------------------------------------------

    To update to the latest version of WSL and WSLg released for preview, simply
    run ``wsl --update`` from an elevated command prompt or powershell.

WSLg 稼働実績がない場合の手順と実質的に同じということになる。WSL を再起動するこ
とを忘れてはいけない。

WSLg をアンインストールする
======================================================================

WSLg をアンインストールする方法はない。WSL をインストールすると WSLg も一緒に付
いてくるのだから。ただし、無効にする方法はある：

    Users wanting to use different servers than the one provided by WSLg can
    change these environment variables. User can also choose to turn off the
    system distro entirely by adding the following entry in their .wslconfig
    file (located at :file:`c:\\users\\MyUser\\.wslconfig`). This will turn off
    support for GUI applications in WSL.

    .. code:: ini

       [wsl2]
       guiApplications=false

動作確認
======================================================================

WSLg のおかげで動作するアプリケーションは、Windows からでも Ubuntu からでも起動
可能だ。

WSLg インストール初期状態では、おそらく Linux GUI アプリケーションもいくつかイン
ストールされている。まずはそれが正しく起動することを確認する。Windows にわざわざ
入れていないもの、例えば ImageMagick 辺りが良い。

Windows から
----------------------------------------------------------------------

Windows メニューの Ubuntu フォルダー以下にある項目を何か選択すると、そのウィンド
ウが起動する。本稿執筆時点での私の Windows スタートメニューのショートカットの宛
先をチェックするとこうだ：

.. csv-table::
   :delim: |
   :header: Application,Command
   :widths: auto

   Caffeine (Ubuntu) | ``wslg.exe -d Ubuntu --cd "~" -- /usr/bin/caffeine``
   ImageMagick (color depth=q16) (Ubuntu) | ``wslg.exe -d Ubuntu --cd "~" -- /usr/bin/display-im6.q16 -nostdin``
   Tilix (Ubuntu) | ``wslg.exe -d Ubuntu --cd "~" -- /usr/bin/tilix``
   WSLView (Ubuntu) | ``wslg.exe -d Ubuntu --cd "~" -- /usr/bin/wslview``

このことから、他の Ubuntu GUI アプリケーションも同じ要領で Windows 側から実行可
能だと思われる。

Ubuntu から
----------------------------------------------------------------------

まず、上記のアプリケーションをコマンドラインから直接実行して、ウィンドウが正常に
出現することを確認したい。万が一 GUI アプリケーションが何もインストールされてい
ない場合には、Ubuntu 端末からパッケージマネージャーで適当なものをまずインストー
ルする。

    If you want to get started with some GUI apps, you can run the following
    commands from your Linux terminal to download and install some popular
    applications. If you are using a different distribution than Ubuntu, it may
    be using a different package manager.

ImageMagick ならばこう：

.. code:: console

   bash$ sudo apt update
   bash$ sudo apt install imagemagick

インストールが完了すると、Ubuntu からコマンドライン実行でアプリケーションが起動
する。起動を確認したらいったん終了し、今度は Windows スタートメニューの Ubuntu
フォルダーを確認する。当該アプリケーションの起動ショートカットが新しく現れている
はずだ。このリンク追加処理は WSLg が行うものだ。

実践例
======================================================================

画像ファイル、音声ファイル、映像ファイルを好きなプログラムで表示、視聴したい。
FFmpeg をインストールすれば :command:`ffplay` でそれらすべてを再生できる：

.. code:: console

   bash$ ffplay speaking-cat.mp4

ImageMagick をインストールすれば、コマンド :command:`display` で画像を専用ウィン
ドウに出力できる：

.. code:: console

   bash$ display funny-cat.jpg

また、Pillow, PyQt など、ウィンドウを開く Python スクリプトも使い物になる。

.. seealso::

   * :doc:`/python-pillow`
   * :doc:`/python-pyqt5`

文献
======================================================================

`Enabling the Windows Subsystem for Linux to include support for Wayland and X server related scenarios <https://github.com/microsoft/wslg>`__
  GitHub にある当開発サイトの README に目を通しておけば、少なくとも正常動作時に
  欲しい情報は十分得られる。異常時には Wiki の関連項目を当たること。
