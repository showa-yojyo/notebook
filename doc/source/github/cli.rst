======================================================================
GitHub CLI documentation ノート
======================================================================

`GitHub CLI documentation <https://docs.github.com/en/github-cli>`__ を見ていく。
ブラウザーとコンソールを往復するのが億劫な人に最適な道具だ。

.. contents:: 見出し一覧
   :depth: 3
   :local:

* :guilabel:`Overview` → :ref:`About GitHub CLI <cli-overview>`
* :guilabel:`Quickstart` → :ref:`GitHub CLI <cli-quickstart>`
* :guilabel:`Reference` → :ref:`GitHub CLI reference <cli-reference>`

.. _cli-overview:

About GitHub CLI
======================================================================

   GitHub CLI is an open source tool for using GitHub from your computer's
   command line.

コンソールから GitHub の操作各種を実行可能。開発環境とブラウザーを往復するのを省
けるから効率向上が期待できる。

   * View, create, clone, and fork repositories
   * Create, close, edit, and view issues and pull requests
   * Review, diff, and merge pull requests
   * Run, view, and list workflows
   * Create, list, view, and delete releases
   * Create, edit, list, view, and delete gists
   * List, create, delete, and connect to a codespace
   * Retrieve information from the GitHub API

素の :command:`git` とどう違うのか：

   GitHub CLI (:command:`gh`) is specifically for working with GitHub. It allows
   you to use the command line to interact with GitHub in all sorts of ways, as
   illustrated by the previous list.

GitHub の自動化に利用したい。

導入および更新は :command:`conda` で行う：

.. code:: console

   bash$ conda install gh --channel conda-forge
   bash$ conda update gh --channel conda-forge

エラーが出たら ``--channel conda-forge`` を省いて様子を見たい。

.. seealso::

   `cli/cli: GitHub’s official command line tool <https://github.com/cli/cli>`__

.. _cli-quickstart:

GitHub CLI quickstart
======================================================================

   Authenticate with GitHub by running this command from your terminal.

コマンド ``gh auth login`` を最初の一度だけ実行するようだが、その結果：

   GitHub CLI automatically stores your Git credentials for you when you choose
   HTTPS as your preferred protocol for Git operations and answer "yes" to the
   prompt asking if you would like to authenticate to Git with your GitHub
   credentials.

となる。これを検証するには ``gh auth status`` を実行すればいいようだ：

.. code:: console

   bash$ gh auth status
   github.com
     ✓ Logged in to github.com as showa-yojyo (/home/USERNAME/.config/gh/hosts.yml)
     ✓ Git operations for github.com configured to use ssh protocol.
     ✓ Token: gho_************************************
     ✓ Token scopes: admin:public_key, gist, read:org, repo

便利コマンド集：

.. csv-table::
   :delim: |
   :header: コマンド,挙動
   :widths: auto

   ``gh status`` | 現在の自分の作業状況を示す
   ``gh repo view OWNER/REPO`` | リポジトリーの記述と README を示す
   ``gh repo clone OWNER/REPO`` | リポジトリーをローカルに clone する
   ``gh repo create`` | リポジトリーを対話的に作成する
   ``gh issue list --repo OWNER/REPO`` | リポジトリーの最近の issues を示す
   ``gh pr list --repo OWNER/REPO`` | リポジトリーの最近の pull requests を示す
   ``gh pr list --label LABEL-NAME`` | ラベルを指定して最近の pull requests を示す
   ``gh codespace create`` | Codespace を対話的に作成する
   ``gh codespace list`` | Codespaces 一覧を示す

.. admonition:: 読者ノート

   Codespaces に関するコマンドは 403 エラーが生じる。コマンド ``gh auth refresh
   -h github.com -s codespace`` を実行するように促されるが？

   Enter ``gh`` for a reminder of the top-level GitHub CLI commands that you can
   use.

ヘルプは他のコマンドと同様に：

   For each command, and each subsidiary subcommand, you can append the
   ``--help`` flag to find out how it's used.

カスタマイズ：

   You can change configuration settings and add aliases or extensions, to make
   GitHub CLI work the way that suits you best.

おそらく Git に影響を受けた設計になっている。

   Enter ``gh config set SUBCOMMANDS`` to configure GitHub CLI's settings,
   replacing ``SUBCOMMANDS`` with the setting you want to adjust.

これは ``gh config --help`` と ``gh config set --help`` を確認してから使う。

   Define aliases for commands that you commonly run.

これはわかりやすい。しかし使わない。

   Create or add custom commands with GitHub CLI extensions.

これも Git に同等の機能があるから理解可能。しかし使わない。

.. admonition:: 読者ノート

   :program:`gh` の設定ファイルは既定では :file:`$XDG_CONFIG_HOME/gh` 以下に配置
   される。このディレクトリーの意味については :doc:`/xdg` 参照。

Creating GitHub CLI extensions
======================================================================

カスタムコマンドを作る。

   You need a repository for each extension that you create. The repository name
   must start with ``gh-``. The rest of the repository name is the name of the
   extension.

リポジトリーの存在をカスタムコマンド作成の前提とする。

   Note: Running ``gh extension create`` with no arguments will start an
   interactive wizard.

拡張コマンド名を指示して作成開始する方法：

.. code:: console

   bash$ gh extension create EXTENSION-NAME

対話的に処理する。

   You can use the ``--precompiled=go`` argument to create a Go-based project
   for your extension, including Go scaffolding, workflow scaffolding, and
   starter code.

これは個人的には利用しないか。

Go 以外のプログラミング言語でコードを書く場合：

   You can use the ``--precompiled=other`` argument to create a project for your
   non-Go precompiled extension, including workflow scaffolding.

スクリプト型実行可能ファイルでもカスタムコマンドを定義可能。スクリプトを作り
``gh extension install .`` を実行する。皆に利用させるためにはさらに：

.. code:: console

   bash$ git init -b main
   bash$ git add . && git commit -m "initial commit"
   bash$ gh repo create gh-EXTENSION-NAME --source=. --public --push

..

   Some GitHub CLI core commands will prompt the user for input. When scripting
   with those commands, a prompt is often undesirable.

コマンドライン引数をきっちり実装する。

   Many core commands support the ``--json`` flag for fetching data
   programatically.

JSON で出力して何かに食わせやすくする。

   If there is not a core command to fetch specific data from GitHub, you can
   use the gh api command to access the GitHub API.

コマンド ``gh api user`` などを実行すればわかるが、JSON で何かが出力される。
Twitter API でデータ処理をするのとひじょうに似ている。

Go 言語周りのトピックがもう一つあるが割愛。

Using GitHub CLI extensions
======================================================================

反対に、他人が作ったカスタムコマンドを利用する。どこの馬の骨が作ったコマンドとも
限らないので：

   To mitigate risk when using third-party extensions, audit the source code of
   the extension before installing or updating the extension.

カスタムコマンドの顕著な特徴：

   Extensions are locally installed and are scoped to the user. Therefore, if
   you access GitHub CLI from a different machine or another user accesses
   GitHub CLI from the same machine, the extension will not be available.

`gh-extension · GitHub Topics <https://github.com/topics/gh-extension>`__

インストール方法：

.. code:: console

   bash$ gh extension install REPO

..

   To install an extension, use the ``extensions install`` subcommand. Replace
   the ``repo`` parameter with the repository of the extension. You can use the
   full URL, such as ``https://github.com/octocat/gh-whoami``, or just the owner
   and repository, such as ``octocat/gh-whoami``.

開発版は事情が異なる：

   To install an extension in development from the current directory, use ``.``
   as the value for the ``repo`` parameter.

上書きインストールを試みるとエラーになる。直前に明示的にアンインストールすることだ。

   To view all installed extensions, use the ``extensions list`` subcommand.

カスタムコマンドを更新する方法はある：

.. code:: console

   bash$ gh extension upgrade EXTENSION
   bash$ gh extension upgrade --all

..

   To uninstall an extension, use the ``extensions remove`` subcommand.

.. _cli-reference:

GitHub CLI reference
======================================================================

頭に叩き込む必要があるコマンド：

.. csv-table::
   :delim: |
   :header: コマンド,挙動
   :widths: auto

   ``gh`` | 最上位コマンドすべてを示す
   ``gh COMMAND`` | ``COMMAND`` のサブコマンドすべてを示す
   ``gh environment`` | ``gh`` が参照する環境変数一覧を示す
   ``gh config`` | 設定可能な GitHub CLI 項目を示す
   ``gh COMMAND [SUBCOMMAND ...] --help`` | コマンド ``gh COMMAND [SUBCOMMAND ...]`` の利用法を出力する

ブラウザーでまとめて情報を得るには次のマニュアルページを参照する： `GitHub CLI
\| Take GitHub to the command line <https://cli.github.com/manual/gh>`__
