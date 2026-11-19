================================================================================
yt-dlp 利用ノート
================================================================================

.. |node| replace:: :program:`node`
.. |uv| replace:: :program:`uv`
.. |yt-dlp| replace:: :program:`yt-dlp`

本稿は yt-dlp_ 利用についてのごく初歩のノートだ。

.. contents:: 見出し一覧
   :local:

概要
================================================================================

YouTube や Twitter にアップロードされている音声ファイルや映像ファイルを PC にダ
ウンロードする道具として、以前は youtube-dl を利用していた。しかし、本稿で述べる
yt-dlp_ のほうが更新活動が活発そうであり、こちらに乗り換えることにした。

本稿では yt-dlp_ を Linux (WSL Ubuntu) から実行することを仮定している。こちらの
ほうがスクリプトを書きやすいし、後処理の柱である FFmpeg も Ubuntu にインストール
してあるのをそのまま利用できるからだ。

インストール・更新・アンインストール
================================================================================

YouTube の性質上、開発中最新版 |yt-dlp| を使うのが最善習慣とされている。したがっ
て、一般の :ref:`python-pkg-install-anchor` の方法を少し変形して適用する。

|uv| を使っている場合は |yt-dlp| をツールインストールしてしまうしかない：

.. sourcecode:: bash
   :caption: |uv| 使用時の |yt-dlp| 実行例

   uv tool install --pre "yt-dlp[default]"

その他の Python パッケージ管理プログラムを使っている場合は、適当な Python 仮想環
境に対して |yt-dlp| をインストールする形になる。その実行時には仮想環境に「入る」
必要がある。

また、Homebrew でも |yt-dlp| を取り扱える。常に最新版ではないだろうが、YouTube
以外の用途には使えると考えられる。

構成・カスタマイズ
================================================================================

WSL 環境で |yt-dlp| の既定動作を変更するには、次のテキストファイルに |yt-dlp| の
命令行オプションを羅列する方法がある：

* :file:`${XDG_CONFIG_HOME}/yt-dlp/config`

記述例はこの後すぐに示す。

.. seealso::

   環境変数 :envvar:`XDG_CONFIG_HOME` については :doc:`/xdg` に記す。

使用方法・コツ
================================================================================

構成ファイルを用意しておく
--------------------------------------------------------------------------------

WSL 環境では、ファイル :file:`${XDG_CONFIG_HOME}/yt-dlp/config` に毎回必ず指定す
る命令行オプションを列挙するのが最善と考えられる。私の場合は：

.. sourcecode:: text
   :caption: :file:`${XDG_CONFIG_HOME}/yt-dlp/config` 記述例

   # yt-dlp configuration file

   --js-runtimes node
   --mtime
   --no-playlist
   --output %(id)s.%(ext)s
   --progress

なお、構成ファイルでは環境変数を記述することが許されている。例えば ``$HOME`` や
``${HOME}`` のように、自然に記述できる。

FFmpeg をインストールしておく
--------------------------------------------------------------------------------

FFmpeg を実行可能な状態にしておけ。詳しくは :doc:/ffmpeg に記す。

YouTube ダウンロードには JavaScript ランタイムが必要
--------------------------------------------------------------------------------

YouTube のファイルをダウンロードしようと |yt-dlp| を実行したら次のような警告が示
される場合についての方策を記す：

   WARNING: [youtube] No supported JavaScript runtime could be found. Only deno
   is enabled by default; to use another runtime add  --js-runtimes
   RUNTIME[:PATH]  to your command/config. YouTube extraction without a JS
   runtime has been deprecated, and some formats may be missing. See
   https://github.com/yt-dlp/yt-dlp/wiki/EJS  for details on installing one

私の場合は次の事前条件が成り立っている：

* |uv| で |yt-dlp| をインストールした（ので、補助パッケージが同梱されていた）
* Ubuntu に NVM を使って |node| を使用可能にできる (e.g. ``nvm use --lts``)

したがって、命令行に ``--js-runtimes node`` を付加すれば、ダウンロードが成功する
ようになる：

.. sourcecode:: bash
   :caption: YouTube の映像ファイルをダウンロードする手順例

   nvm use --lts

   # 冥
   url="https://www.youtube.com/watch?v=UmPQw5h0Q9w"
   options=(
       --no-playlist
       --js-runtimes node
       -t mp4
   )
   yt-dlp "${options[@]}" "$url"

シェルで別名を付けておく
--------------------------------------------------------------------------------

|uv| を使っている場合、かつ、``uv tool install`` でインストールした場合には、パ
スが通っているディレクトリーに |yt-dlp| へのシンボリックリンクが作成されているは
ずだ。そのまま ``yt-dlp`` と打鍵すればいい。インストールしないで |yt-dlp| を利用
する方針であれば、次のような別名を定義するのがいいかもしれない：

 .. sourcecode:: bash
    :caption: |uv| 使用時の |yt-dlp| 実行例

    alias yt-dlp='uvx --pre --from "yt-dlp[default]" yt-dlp'

管理プログラムに Mamba または Micromamba を使い、|yt-dlp| をインストールしてある
仮想環境の名前が ``yt-dlp`` である場合、別名を付けるならば次のようにする：

.. sourcecode:: bash
   :caption: |yt-dlp| を直接実行できない条件下での :command:`alias` 例

   alias yt-dlp='mamba run -n yt-dlp yt-dlp'

別名を使う欠点は、現在の対話モードシェル以外では効果がないということだ。後述する
ようなシェルスクリプトで |yt-dlp| を実行する場合、Bash の使用上、:file:`.bashrc`
で定義した :command:`alias` はスクリプトに引き継がれない。あくまでも、対話モード
での利便性を上げるためだけの方策だと心得ろ。

ラッパーを用意する
--------------------------------------------------------------------------------

用例に応じたシェル関数なりシェルスクリプトなりを用意しておき、すぐに実行可能な準
備を整えるのがいい。例えば、YouTube や Twitter に存在する音声映像 URL から MP3
ファイルを保存することが多い場合は、対話シェルからこんな関数を呼び出せるようにし
ておくのだ：

.. sourcecode:: bash
   :caption: |yt-dlp| を用いるシェルスクリプト例
   :force:

   #!/bin/bash
   # description: download an audio file (mp3) from YouTube

   set -o errexit -o nounset -o pipefail

   url="${1:?Usage: $BASH_ARGV0 URL}"
   options=(-q -t mp3)

   yt-dlp "${options[@]}" "$url"

資料
================================================================================

yt-dlp_
   GitHub リポジトリー。初実行の前には README 部分をていねいに読め。

.. _yt-dlp: https://github.com/yt-dlp/yt-dlp
