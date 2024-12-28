======================================================================
構成
======================================================================

本節ではコマンド ``git config`` 等による構成に関する事項について記す。構成項目が
ひじょうに多いが、私にとって有用なものを優先して掲載していく。

.. contents:: 見出し一覧
   :local:

概要
======================================================================

Git の個人的構成オプションは既定でファイル :file:`$HOME/.gitconfig` に保存される。
テキストエディターで直接テキストを編集してもよいし、コンソールから ``git config
--global`` で設定を書き込んでもよい。

各コマンドが任意に構成項目を参照するという設計上、すべてのオプションを一覧にまと
めたようなものは存在しない。ここでは設定不可欠な項目とプロによる推奨項目を記すこ
とにする。

設定ファイル
======================================================================

環境変数 ``XDG_CONFIG_HOME`` を :doc:`/xdg` で記したように定義した上で、既定パス
の設定ファイル各種を再配置することを推奨する：

.. code:: console

   $ mv ~/.gitconfig $XDG_CONFIG_HOME/git/gitconfig

このように整理しておくことで、他のアプリケーションのドットファイルと一括して
:file:`$XDG_CONFIG_HOME` ごと Git でバージョン管理することが可能になる。
:file:`.gitignore` などの他の Git 設定ファイルについても同様に扱うのが自然だ。

.. caution::

   設定ファイルの一部が機密情報であるはずなので、そういうものは :ref:`後述
   <git-anchor-user>` のように別ファイルに追い出して、公開リポジトリーに出さない
   運用にしろ。

設定内容
======================================================================

以下、設定ファイルでの記法で個人的に有用な設定項目をセクションごとに列挙してい
く。

セクション ``alias``
----------------------------------------------------------------------

:doc:`./aliases` に記す。

セクション ``branch``
----------------------------------------------------------------------

``branch.autoSetupRebase = always``
  ``git branch``, ``git switch``, ``git checkout`` で新しくブランチができるとき
  に、``merge``ではなく ``rebase`` で ``pull`` させる。

セクション ``browser``
----------------------------------------------------------------------

他の構成項目を設定する過程で付随的に ``browser.<tool>.cmd`` や
``browser.<tool>.path`` を設定する必要が生じたとする。

Cygwin の場合はサブセクションを ``"default-browser"`` とし、``cmd = cygstart``
とすれば Windows の既定のブラウザーを開かせるようにできる。なおかつ固有名詞を
ハードコードすることを避けられる。

.. code:: ini

   [browser "default-browser"]
       cmd = cygstart

同様に、WSL の場合には ``cmd = wslview`` とする。

.. code:: ini

   [browser "default-browser"]
       cmd = wslview

セクション ``color``
----------------------------------------------------------------------

コンソールにおける文字色のオンオフや、色自体を設定するための構成オプションが多数
存在し、サブセクションでそれらを指定する。

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
  ``git status`` の出力する各種テキストの色を次のようにして設定することが
  できる：

  .. code:: ini

     [color "status"]
         added = yellow
         changed = green
         untracked = cyan

``color.ui = auto``
  ``git diff`` や ``git grep`` など、オプション ``--color`` を実装しているコマン
  ドのデフォルトの色使い設定を指示する。値としては ``auto`` で十分だと思われる。

セクション ``core``
----------------------------------------------------------------------

``core.autocrlf = input``
  テキストファイルをコミットするときに、改行文字の変換をどうするのかを指示する。

  値を ``input`` にセットして変換を行わせない。

``core.excludesFile = ~/.gitignore``
  作業コピー内の :file:`.gitignore` と :file:`.git/info/exclude` の記述に加え
  て、ここで設定したファイルもバージョン管理の対象外ファイルの一覧とする。

  この値を設定するよりも、既定値である ``$XDG_CONFIG_HOME/git/ignore`` や
  ``$HOME/.config/git/ignore`` に一覧を移行したほうがいいかもしれない。

``core.editor``
  ログメッセージを編集するためのコマンドを設定する。

  普通は汎用テキストエディターのパスをセットするのだが、この構成オプションを設け
  る代わりに、環境変数 ``GIT_EDITOR`` でそれをセットすることにした。

``core.fileMode = true``
  Cygwin から WSL に作業環境を移行する際にこの設定を ``true`` に変えた。

セクション ``diff``
----------------------------------------------------------------------

``diff.tool = vscode``
  コマンド ``git difftool`` を実行するときに使われる差分ツールを設定する。詳細は
  サブセクション、この場合は ``difftool "vscode"`` に記す。次節の記述を参照。右
  辺でセットする値は Git が規定する名前か、任意の名前を設定できる。ここでは任意
  の名前として ``vscode`` と書いた。

セクション ``difftool``
----------------------------------------------------------------------

``difftool.<tool>.cmd`` や ``difftool.<tool>.path`` を次のように設定する。ここで
シェル変数 ``LOCAL`` と ``REMOTE`` にはそれぞれ差分の pre-image とpost-image と
なる一時ファイルがそれぞれ動的にセットされる。

ツールの特性に合わせて敢えてこれらのパラメーターを入れ替えて指定することもあり得
る。

.. code:: ini

   [difftool vscode]
       cmd = code --wait --diff $LOCAL $REMOTE

``difftool.prompt = false``
  ツールの起動時にプロンプトを出すかどうかを設定する。要らないので ``false`` と
  する。

セクション ``help``
----------------------------------------------------------------------

``help.browser = default-browser``
  ヘルプをウェブブラウザーで見るときのブラウザーを設定する。併せて
  ``browser.<tool>.cmd`` なり ``browser.<tool>.path`` を設定すること。

``help.format = web``
  コンソールでヘルプを見るのはつらいので、HTML 版をブラウザーで見るための設定。
  逆に ``man`` のほうが慣れているならば、この項目を設定しない。

セクション ``merge``
----------------------------------------------------------------------

``merge.ff = false``
  コマンド ``git merge`` 実行時に ``--no-ff`` が付く。

``merge.tool = vscode``
  ``git mergetool`` を実行するときに使われるマージツールを設定する。

  他の構成オプションの例と同様に ``merge.<tool>.cmd`` なり ``merge.<tool>.path``
  を設定すること。次の節も参照。

``merge.log``
  値 ``true`` を設定したい。

セクション ``mergetool``
----------------------------------------------------------------------

``mergetool.<tool>.cmd`` や ``mergetool.<tool>.path`` を次のように設定する。ここ
で ``BASE`` や ``REMOTE`` などのシェル変数を、マージ処理に関連する一時ファイル名
として指示するのに用いる。

.. code:: ini

   [mergetool "vscode"]
       cmd = code --wait $MERGED

``keepBackup = false``
  マージ処理後に、衝突マーカーの付いたファイルを残すかどうかを設定する。要らない
  ので ``false`` とする。

``prompt = false``
  ツールの起動時にプロンプトを出すかどうかを設定する。要らないので ``false`` と
  する。

セクション ``pull``
----------------------------------------------------------------------

``pull.ff = only``
  コマンド ``git pull`` 実行時に ``--ff-only`` が付く。

セクション ``push``
----------------------------------------------------------------------

``push.default = current``
  ``git push`` のように refspec を指定しないでプッシュするときに、実際に何をプッ
  シュするのかを設定する。値を ``current`` とすれば、現在ブランチをリモートの同
  名ブランチにプッシュするようになる。

.. _git-anchor-user:

セクション ``user``
----------------------------------------------------------------------

GitHub にリポジトリーを設置するのであれば要設定。ただし、このセクションは
:file:`$HOME/.gitconfig` に直接記入するのではなく、別のファイルに記載して
``include`` する運用を取ること。

.. code:: ini

   # in ~/.gitconfig:
   [include]
       path = /path/to/gitconfig-user

   # in /path/to/gitconfig-user:
   [user]
       name = xxxx
       email = xxxx

``user.name``
  私の名前をテキストで設定する。

``user.email``
  私のメールアドレスを設定する。

``user.signingKey``
  キーを設定する。設定値が ``git tag`` や ``git commit`` でキーが必要な状況にお
  いて、引数にキーを指示しないでコマンドを実行するときに参照される。

セクション ``web``
----------------------------------------------------------------------

``web.browser = default-browser``
  ウェブブラウザーを利用するコマンドに対して、どのブラウザーを使わせるのかを設定
  する。これを設定する場合、セクション ``browser`` のサブセクション ``browser
  "default-browser"`` を設けて、そこで ``browser.<tool>.cmd`` なり
  ``browser.<tool>.path`` を設定することになる。

  .. code:: ini

     [web]
         browser = default-browser
     [browser "default-browser"]
         cmd = wslview

.. include:: /_include/git-refs.txt
