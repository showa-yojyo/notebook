======================================================================
構成
======================================================================

本節ではコマンド :command:`git config` 等による構成に関する事項について記す。構
成項目がひじょうに多いが、私にとって有用なものを優先して掲載していく。

.. contents::

概要
======================================================================

Git の個人的な構成オプションはファイル :file:`~/.gitconfig` に保存する。テキスト
エディターで直接テキストを編集してもよいし、コンソールから :command:`git config
--global` で設定を書き込んでもよい。

各コマンドが任意に構成項目を参照するという設計上、すべてのオプションを一覧にまと
めたようなものは存在しない。ここでは設定不可欠な項目とプロによる推奨項目を記すこ
とにする。

設定内容
======================================================================

``alias``
----------------------------------------------------------------------

:doc:`./aliases` に記す。

``branch``
----------------------------------------------------------------------

``branch.autoSetupRebase = always``
  :command:`git branch` や :command:`git checkout` で新しくブランチができるとき
  に、:command:`merge` ではなく :command:`rebase` で :command:`pull` させる。

``browser``
----------------------------------------------------------------------

他の構成項目を設定する過程で付随的に ``browser.<tool>.cmd`` や
``browser.<tool>.path`` を設定する必要が生じた場合、次のように設定する。

.. code:: ini

   [browser "sleipnir"]
       cmd = 'C:/Program Files (x86)/Fenrir Inc/Sleipnir6/bin/Sleipnir.exe'

Cygwin の場合は ``cmd = cygstart`` とすれば Windows の既定のブラウザーを開かせる
ようにできる。なおかつ固有名詞をハードコードすることを避けられる。

``color``
----------------------------------------------------------------------

コンソールにおける文字色のオンオフや、色自体を設定するための構成オプショオンが多
数存在する。

``color.branch.<slot>``
  ブランチの色をカスタマイズする場合は次のように設定する：

  .. code:: ini

     [color "branch"]
         current = yellow reverse
         local = yellow
         remote = green

``color.diff.<slot>``
  差分テキストの色をカスタマイズする場合は次のように設定する：

  .. code:: ini

     [color "diff"]
         meta = yellow bold
         frag = magenta bold
         old = red bold
         new = green bold

``color.status``
  :command:`git status` の出力する各種テキストの色を次のようにして設定することが
  できる：

  .. code:: ini

     [color "status"]
         added = yellow
         changed = green
         untracked = cyan

``color.ui = auto``
  :command:`git diff` や :command:`git grep` など、オプション ``--color`` を実装
  しているコマンドのデフォルトの色使い設定を指示する。

  値としては ``auto`` で十分だと思われる。

``core``
----------------------------------------------------------------------

``core.autocrlf = input``
  テキストファイルをコミットするときに、改行文字の変換をどうするのかを指示する。

  ``input`` にセットして変換を行わせない。

``core.excludesFile = ~/.gitignore``
  作業コピー内の :file:`.gitignore` と :file:`.git/info/exclude` の記述に加え
  て、ここで設定したファイルもバージョン管理の対象外ファイルの一覧とする。

  自分のホームディレクトリーに汎用の :file:`.gitignore` を置いて、こういう感じで
  設定する。

``core.editor``
  ログメッセージを編集するためのコマンドを設定する。

  普通は汎用テキストエディターのパスをセットするのだが、この構成オプションを設け
  る代わりに、環境変数 ``GIT_EDITOR`` でそれをセットすることにした。

``diff``
----------------------------------------------------------------------

``diff.tool = tortoisediff``
  :command:`git difftool` を実行するときに使われる差分ツールを設定する。

  右辺でセットする値は Git が規定する名前か、任意の名前を設定できる。ここでは
  ``tortoisediff`` と書いたが、これは Git の知らないものである。このような場合
  は、さらに ``difftool.<tool>.cmd`` オプションを設定する必要がある。

``difftool``
----------------------------------------------------------------------

``difftool.<tool>.cmd`` や ``difftool.<tool>.path`` を次のように設定する。ここで
シェル変数 ``LOCAL`` と ``REMOTE`` にはそれぞれ差分の pre-image とpost-image と
なる一時ファイルがそれぞれ動的にセットされる。

ツールの特性に合わせて敢えてこれらのパラメーターを入れ替えて指定することもあり得
る。

.. code:: ini

   [difftool tortoisediff]
       difftool.cmd = \"C:/Program Files/TortoiseGIT/bin/TortoiseGitMerge.exe\" -mine:\"$REMOTE\" -base:\"$LOCAL\"

``difftool.prompt = false``
  ツールの起動時にプロンプトを出すかどうかを設定する。要らないので ``false`` と
  する。

``help``
----------------------------------------------------------------------

``help.browser = sleipnir``
  ヘルプをウェブブラウザーで見るときのブラウザーを設定する。

  併せて ``browser.<tool>.cmd`` なり ``browser.<tool>.path`` を設定すること。

``help.format = web``
  コンソールでヘルプを見るのはつらいので、HTML 版をブラウザーで見るための設定。

``merge``
----------------------------------------------------------------------

``merge.tool = tortoisemerge``
  ``git mergetool`` を実行するときに使われるマージツールを設定する。

  他の構成オプションの例と同様に ``merge.<tool>.cmd`` なり ``merge.<tool>.path``
  を設定すること。

``merge.log``
  値 ``true`` を設定したい。

``mergetool``
----------------------------------------------------------------------

``mergetool.<tool>.cmd`` や ``mergetool.<tool>.path`` を次のように設定する。ここ
で ``BASE`` や ``REMOTE`` などのシェル変数を、マージ処理に関連する一時ファイル名
として指示するのに用いる。

.. code:: ini

   [mergetool "tortoisemerge"]
       mergetool.cmd = \"C:/Program Files/TortoiseGit/bin/TortoiseGitMerge.exe\" -base:\"$BASE\" -theirs:\"$REMOTE\" -mine:\"$LOCAL\" -merged:\"$MERGED\"

``keepBackup = false``
  マージ処理後に、衝突マーカーの付いたファイルを残すかどうかを設定する。要らない
  ので ``false`` とする。

``prompt = false``
  ツールの起動時にプロンプトを出すかどうかを設定する。要らないので ``false`` と
  する。

``push``
----------------------------------------------------------------------

``push.default = current``
  ``git push`` のように refspec を指定しないでプッシュするときに、実際に何をプッ
  シュするのかを設定する。

  値を ``current`` とすれば、カレントブランチをリモートの同名のブランチにプッ
  シュするようになる。

``user``
----------------------------------------------------------------------

GitHub にリポジトリーを設置するのであれば要設定。

``user.name``
  私の名前をテキストで設定する。

``user.email``
  私のメールアドレスを設定する。

``user.signingKey``
  キーを設定する。

  ここでの設定値が :command:`git tag` や :command:`git commit` でキーが必要な状
  況において、引数にキーを指示しないでコマンドを実行するときに参照される。

``web``
----------------------------------------------------------------------

``web.browser = sleipnir``
  ウェブブラウザーを利用するコマンドに対して、どのブラウザーを使わせるのかを設定
  する。

  これも ``browser.<tool>.cmd`` なり ``browser.<tool>.path`` を設定すること。

.. include:: /_include/git-refs.txt
