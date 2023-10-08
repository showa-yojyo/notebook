======================================================================
GitHub Codespaces documentation ノート
======================================================================

`GitHub Codespaces documentation <https://docs.github.com/en/codespaces>`__ は文
書がたくさんあるので読むのが厳しい。Codespace は本質的に有料機能なので、私はまず
利用しないはずだ。全文調査せずに切り上げる。

.. contents::

* :guilabel:`Overview` は個別ページの GitHub Codespaces overview へ
* :guilabel:`Quickstart` は Quickstart for GitHub Codespaces へ

GitHub Codespaces overview
======================================================================

  A codespace is a development environment that's hosted in the cloud. You can
  customize your project for GitHub Codespaces by committing configuration files
  to your repository

開発環境を使わせてくれると言っているのだ。その構成は：

  You can choose from a selection of virtual machine types, from 2 cores, 8 GB
  RAM, and 32 GB storage, up to 32 cores, 64 GB RAM, and 128 GB storage.

最低のメモリー 8GB というのは、私が今使っている PC のそれと同じだ。最低ラインで
も十分だ。

  By default, codespaces are created from an Ubuntu Linux image that includes a
  selection of popular languages and tools

WSL で作業している身としてはありがたい環境だ。

  You can connect to your codespaces from your browser, from Visual Studio Code,
  from the JetBrains Gateway application, or by using GitHub CLI. When you
  connect, you are placed within the Docker container.

Docker という術語が出てくるが、不勉強のツケがここに来そうだ。

GitHub Codespaces の利点をキャッチコピーだけ引用しておこう。再利用性、再現性、隔
離などという言葉が浮かぶ：

* Use a preconfigured development environment
* Access the resources you need
* Work anywhere
* Choose your editor
* Work on multiple projects
* Pair program with a teammate
* Publish your web app from a codespace
* Try out a framework

Codespaces の開始手段はいろいろあるようで、本文のリンク先それぞれを読むといい。

  All personal GitHub.com accounts have a monthly quota of free use of GitHub
  Codespaces included in the Free or Pro plan. You can get started using GitHub
  Codespaces on your personal account without changing any settings or providing
  payment details.

ノート冒頭で《本質的には有料機能》と記したが、上記の制約があるからだ。無料枠内で
やりくりせねばならない。

  To customize the runtimes and tools in your codespace, you can create one or
  more dev container configurations for your repository.

カスタマイズするほうが普通だろうが、見慣れぬ術語が出てきて不安だ。

  You can personalize aspects of your codespace environment by using a public
  `dotfiles <https://dotfiles.github.io/tutorials/>`__ repository. You can use
  dotfiles to set shell aliases and preferences, or to install your personal
  preference of the tools you like to use.

最後に、料金について述べられている。専用の節があるのでそこでまとめる。

Getting started with GitHub Codespaces
======================================================================

Quickstart for GitHub Codespaces
----------------------------------------------------------------------

  You'll work in the browser version of Visual Studio Code, which is initially
  the default editor for GitHub Codespaces.

Codespace とは何かと問われたら、上のように答えるのがいちばん伝わる気がする。

このクイックスタートではデモが用意されているので、以下、それを実施していく。

Codespace の作成方法は、まず Codespace テンプレートリポジトリーにアクセスする。
それから :menuselection:`Use this template --> Open in a codespace` を押す。これ
でブラウザーに VS Code に似た UI が現れる。

アプリケーションを起動するには、そこのコンソールで ``npm run dev`` を実行する。
本家同様のトーストが出現する。:guilabel:`Open in Browser` を押す。

アプリケーションを変数して変更を眺めるには：

#. :file:`haikus.json` を編集する。
#. 画面を手動でリフレッシュ。

VS Code での作業の要領で変更部分をすべてコミットすると :guilabel:`Publish
Branch` ボタンが現れる。それを押す。リポジトリーを選択する。これで自分のアカウン
トにリポジトリーが追加される。

  You can enable :menuselection:`Settings Sync` to sync extensions and other
  settings across devices and instances of VS Code. Your synced settings are
  cached in the cloud.

これを ON にすると吉のはずだが、PC で使っている VS Code の拡張構成と使い分けたい
ときは OFF ということになる。その中間が欲しい。

Understanding the codespace lifecycle
----------------------------------------------------------------------

  The lifecycle of a codespace begins when you create a codespace and ends when
  you delete it.

Codespace の寿命管理は常識的なのものであるようだ。

  There are limits to the number of codespaces you can create, and the number of
  codespaces you can run at the same time.

制限は二種類ある。今のところは好きなだけ作成できるような代物ではないと覚えておけ
ばいい。

  When you connect to a codespace through the web, auto-save is enabled
  automatically for the web editor and configured to save changes after a delay.

VS Code のファイル自動保存機能を Codespace 自体に適用したようなものか。

  Your work will be saved on a virtual machine in the cloud.

スペースを一定時間放置すると自動的に片付けられる。自動シャットダウンしてもデータ
は保存される。

用がないときには Codespace を止めておくのが無難だ。

  For example, if you're using a codespace in the VS Code web client and you
  close the browser tab, the codespace remains running on the remote machine.

Codespace 最大の特徴がこれだ。金がかかってはかなわない：

  If you create a codespace, it will continue to accrue storage charges until it
  is deleted, irrespective of whether it is active or stopped.

Deep dive into GitHub Codespaces
----------------------------------------------------------------------

  GitHub Codespaces is an instant, cloud-based development environment that uses
  a container to provide you with common languages, tools, and utilities for
  development.

スペースを開く方法は先述の方法以外にも複数ある：

  You can create a codespace on GitHub.com, in Visual Studio Code, or by using
  GitHub CLI.

GitHub リポジトリーには shallow clone という概念がある。

  Your repository is cloned into the :file:`/workspaces` directory in the
  codespace

コンテナーという概念を理解しないとダメそうだ。コンテナーが作成されてからスペース
に接続。

ファイルの保存については VS Code の Auto Save をオンにしておくとよい。

停止する方法は一つは習得しておく：

* <https://github.com/codespaces> で操作する
* VS Code コマンドパレットから :guilabel:`Codespaces: Stop Current Codespace` を
  実行する
* コンソールから ``gh codespace stop`` を実行する

ポート転送機能を有する。上手くノートにまとめられないので割愛。

  You can work with Git in your codespace either via the Terminal or by using
  the source control features of VS Code or JetBrains.

Codespace で Git 操作をすると何がうれしいかと言うと：

  Because GitHub Codespaces is designed to be ephemeral, you can use it as an
  isolated environment to experiment, check a teammate's pull request, or fix
  merge conflicts.

Codespace を公開するという考え方がある。作業環境を共有するという意図だろう。

  If you already use VS Code, you can use :menuselection:`Settings Sync` to
  automatically sync extensions, settings, themes, and keyboard shortcuts
  between your local instance and any codespaces you create.

VS Code の本物の拡張で設定を同期できる。ただし実行前にまず考えろ。

Codespace のディレクトリー構造について：

  When you create a codespace, your repository is cloned into the
  :file:`/workspaces` directory in your codespace. This is a persistent
  directory that is mounted into the container.

:file:`~/.bashrc` を書ける。

コンテナーの再構築に注意する。これがデータを壊す。

.. admonition:: 読者ノート

   私がコンテナー技術をまったく知らないので、ピンと来ない記述に出くわすと読むの
   が止まる。

Developing in a codespace
======================================================================

  You can use your codespace in the browser or in a choice of code editors.

Developing in a codespace
----------------------------------------------------------------------

GitHub CLI の場合：

  You can use GitHub CLI to create a new codespace, or start an existing
  codespace, and then SSH to it. Once connected, you can work on the command
  line using your preferred command-line tools.

コマンドを細かく記載すると紙面が煩雑になるので、コンソールでヘルプを確認しよう：

.. code:: console

   bash$ gh codespace --help

VS Code の場合は後述。

ブラウザーの場合、<https://github.com/codespaces> で利用可能な Codespaces すべて
を確認する。あるいは：

  Alternatively, you can see any of your codespaces for a specific repository by
  navigating to that repository and selecting :guilabel:`Code`. The dropdown
  menu will display all active codespaces for a repository.

Creating a codespace for a repository
----------------------------------------------------------------------

  You can use GitHub Codespaces on your personal GitHub.com account, with the
  quota of free use included each month for accounts on the Free and Pro plans.

それなら良かった。

  If you create a codespace from a repository, the codespace will be associated
  with a specific branch, which cannot be empty.

GitHub CLI では次のようなコマンドを実行して Codespace を生成する：

.. code:: console

   bash$ gh codespace create -r OWNER/REPO -b BRANCH --devcontainer-path PATH -m MACHINE-TYPE

GitHub Codespaces 拡張が作動中の VS Code では、:guilabel:`Activity Bar` 左柱の
:guilabel:`Remote Explorer` アイコンを押す。サイドバーのプラスボタンを押す。
入力欄でリポジトリー、ブランチ、等々を順次指定することで Codespace を生成する。

ブラウザーでは：

#. リポジトリー画面で対象ブランチを選択する。
#. :menuselection:`Code --> Codespaces --> Create codespace on <BRANCH-NAME>`
#. ここでオプション設定なのだが……。

Creating a codespace from a template
----------------------------------------------------------------------

  If you're starting a new project, you can get started with development work
  quickly by creating a codespace from a template.

Quickstart でやったようなものだ。

空白のテンプレから始めることも可能。

  With a blank template, you'll start with an empty directory, with access to
  cloud-based compute resources and the tools, languages, and runtime
  environments that come preinstalled with the default codespace image. With
  other templates, you'll get starter files for the technology you're working
  with, plus typically some extra files such as a README file, a
  :file:`.gitignore` file, and dev container configuration files containing some
  custom environment configuration.

テンプレートはどこにあるのか： <https://github.com/codespaces> から
:menuselection:`Templates --> See all --> Blank --> Use this template` など。テ
ンプレートリポジトリーから Codespace を開く方法は前述のとおり。

  Typically, Git will come preinstalled, and the working directory will be
  automatically initialized as a Git repository unless you started from GitHub's
  blank template.

Git くらい入れておけばいいじゃないか。

Publish の概念については前述のとおり。

Deleting a codespace
----------------------------------------------------------------------

Codespace の維持にはコストがかかるので、不要なものは削除することだ。

GitHub CLI を使って削除する場合：

  To delete a codespace use the gh codespace delete subcommand and then choose a
  codespace from the list that's displayed.

  .. code:: console

     bash$ gh codespace delete

有用なコマンドラインオプションとして ``--all``, ``--repo``, ``--days`` が挙げら
れている。ヘルプ参照。

GitHub Codespaces 拡張が作動中の VS Code で削除する場合は、:guilabel:`Activity Bar` 左柱の
:guilabel:`Remote Explorer` アイコンを押す。サイドバーの codespace 項目を右ク
リックして :menuselection:`Delete Codespace` を押せばよい。

ブラウザーを使って削除する場合、<https://github.com/codespaces> から
:menuselection:`Your codespaces --> (codespace)` の枠で :menuselection:`... -->
Delete` を押す。

Opening an existing codespace
----------------------------------------------------------------------

  You can reopen any of your active or stopped codespaces on GitHub.com, in a
  JetBrains IDE, in Visual Studio Code, or by using GitHub CLI.

私の言葉では resume に相当する。

GitHub CLI を使って再開する場合、どの環境に再開するのかを指定することも可能だ：

.. code:: console

   bash$ gh codespace code
   bash$ gh codespace code --web
   bash$ gh codespace ssh

上から順に VS Code で、ブラウザーで、SSH 接続コンソールでそれぞれアクセスする。

GitHub Codespaces 拡張が作動中の VS Code で codespace を再開する場合、まず次のど
ちらかのコマンドを実行する：

* :guilabel:`Codespaces: Open Codespace in New Window`
* :guilabel:`Codespaces: Open in Browser`

それから UI で対象 codespace を選択する。同じことになるが、サイドバーの項目から
再開することも可能。

ブラウザーで再開する場合、対象リポジトリー画面を開いてキー :kbd:`,` を押す。それ
から :guilabel:`Resume this codespace` を押す。

アカウント :menuselection:`Your codespaces` から開くことも可能。何で開くかも選択
する。

Working collaboratively in a codespace
----------------------------------------------------------------------

  Visual Studio Live Share lets you collaboratively edit and debug with others
  in real time, within a codespace. You can securely share your current
  codespace, or access a codespace created by someone else.

Live Share 拡張を VS Code にインストールする。私は使わないはずなので割愛。

Using source control in your codespace
----------------------------------------------------------------------

VS Code 上での Git 操作と同様。私は慣れているので割愛。あるいは VS Code ノートへ
のリンクを付けるか。

Using GitHub Codespaces for pull requests
----------------------------------------------------------------------

Pull request ページの :guilabel:`Code` で codespace を開くことが可能だ。

  A codespace is created for the pull request branch and is opened in your
  default editor for GitHub Codespaces.

この codespace を開いたエディターの :guilabel:`Activity Bar` の
:guilabel:`GitHub Pull Request` アイコンを押す。サイドバーに当該 pull request の
変更ファイル一覧がある。UI 操作で適当にレビューする。締めに結果に応じたボタンを
押す。

  Once you have received feedback on a pull request, you can open it in a
  codespace in your web browser, or in VS Code, to see the review comments. From
  there you can respond to comments, add reactions, or dismiss the review.

Stopping and starting a codespace
----------------------------------------------------------------------

  When you stop a codespace, any running processes are stopped. Any saved
  changes in your codespace will still be available when you next start it.

停止しないと次のようになって怖い：

  If you do not explicitly stop a codespace, it will continue to run until it
  times out from inactivity. Closing a codespace does not stop the codespace.

GitHub CLI で停止する場合、次のコマンドを実行する：

.. code:: console

   bash$ gh codespace stop

GitHub Codespaces 拡張が作動中の VS Code で codespace を停止する場合、コマンド
:guilabel:`Codespaces: Stop Codespace` を実行する。再開はコマンド
:guilabel:`Codespaces: Connect to Codespace` を実行する。

ブラウザーを使って codespace を停止する場合、<https://github.com/codespaces> か
ら :menuselection:`Your codespaces --> (codespace)` の枠で :menuselection:`...
--> Stop codespace` を押す。再開は対象 codespace 項目をクリックする。

Forwarding ports in your codespace
----------------------------------------------------------------------

  You can forward ports in your codespace to test and debug your application.
  You can also manage the port protocol and share the port within your
  organization or publicly.

Web アプリケーションのデバッグ用機能と思っていい。

  You can manually forward a port that wasn't forwarded automatically.

VS Code でいう Panel に :guilabel:`PORTS` というタブがある。:guilabel:`Add Port`
でポート番号を追加する。

HTTP を HTTS に変えられる。右クリックメニューの :menuselection:`Change Port
Protocol`.

.. admonition:: 読者ノート

   この記事は難しい。

Rebuilding the container in a codespace
----------------------------------------------------------------------

  When you work in a codespace, your development environment is a Docker
  container that runs on a virtual machine.

Docker を知らないが、とにかく読み続ける。

  By default, when you rebuild a container, GitHub Codespaces will speed up the
  build process by reusing cached images from previous builds of the container.

前回のモノを再利用するので処理は高速だ。それとは異なる完全再構築というのもある？

GutHub CLI を使って codespace を再構築する場合、次のコマンドがそれを実行する：

.. code:: console

   bash$ gh codespace rebuild
   bash$ gh codespace rebuild --full

GitHub Codespaces 拡張が作動中の VS Code で codespace を再構築する場合、次のコマ
ンドがそれを実行する：

* :menuselection:`Codespaces: Rebuild Container`
* :menuselection:`Codespaces: Full Rebuild Container`

以降、:file:`/workspaces` に関する記述が長く続く。このディレクトリーの内容は維持
される。再構築時でも破壊したくないファイルがあれば、このディレクトリーを上手に使
えというようなことが述べられている。

Default environment variables for your codespace
----------------------------------------------------------------------

  GitHub sets default environment variables for every codespace. Commands run in
  codespaces can create, read, and modify environment variables.

ダミーの codespace を生成してこれらの環境変数の値をチェックするといい。

Persisting environment variables and temporary files
----------------------------------------------------------------------

環境変数と一時ファイルを永続化したい。

単独 codespace に関する環境変数については、この codespace を再構築しない限りは
:file:`$HOME/.bashrc` で環境変数を定義するという方法が採れる（シェルは
:command:`bash` を仮定）。

同じリポジトリーに対する codespaces すべての環境変数については、次の方法がある：

* 構成ファイル :file:`devcontainer.json`
* カスタム :file:`Dockerfile`
* secrets を使う

方法その一では、次のように記述すると環境変数が定義できるらしい：

  .. code:: json

     {
         "remoteEnv": {
           "VARNAME": "value"
        }
     }

方法その二では：

  If you are using a custom :file:`Dockerfile` you can set the environment
  variable there by adding ``ENV VARNAME=value``.

方法その三は機微に触れるデータを定義するのに採用する。逆に、その一、その二を採用
してはいけない。

Connecting to a private network
----------------------------------------------------------------------

  You can connect GitHub Codespaces to resources on a private network, including
  package registries, license servers, and on-premises databases.

現在、次の二つの方法がある：

  * Using a GitHub CLI extension to configure your local machine as a gateway to
    remote resources.
  * Using a VPN.

必要になったら調べる。

  IP addresses for codespaces are dynamically assigned, meaning your codespace
  is not guaranteed to have the same IP address day to day.

Getting started with GitHub Codespaces for machine learning
----------------------------------------------------------------------

.. todo::

   ノートの合間に実施する。

Using GitHub Codespaces in Visual Studio Code
----------------------------------------------------------------------

GitHub Codespaces 拡張を VS Code にインストールして GitHub に接続する。

  If you would prefer to open any new codespaces in VS Code automatically, you
  can set your default editor to be VS Code.

これと、

  If you prefer to work in the browser, but want to continue using your existing
  VS Code extensions, themes, and shortcuts, you can turn on
  :menuselection:`Settings Sync`.

これについてはカスタマイズの章で扱う。

.. todo::

   ここから先の練習は取っておく。

Using GitHub Codespaces in your JetBrains IDE
----------------------------------------------------------------------

割愛。

Using GitHub Codespaces with GitHub CLI
----------------------------------------------------------------------

コマンドのクックブックのような節だ。

  To use :command:`gh` to work with GitHub Codespaces, type ``gh codespace
  SUBCOMMAND``

  GitHub Codespaces creates a local SSH key automatically to provide a seamless
  authentication experience.
