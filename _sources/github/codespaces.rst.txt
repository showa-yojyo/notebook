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

この節の前半部分はブラウザーの VS Code で実施可能。本物の VS Code だと Jupyter
のカーネルを選択するところで、入力欄が空白しかない。

後半部分は囲み記事にあるように、現在実施不能。

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

本節の事前条件に述べられているうち、次は実施済みとする：

* VS Code への GitHub Codespaces 拡張のインストール
* VS Code の Activity Bar に :guilabel:`Remote Explore` アイコンが表示済み
* Side bar の :guilabel:`REMOTE EXPLORER` 右のドロップダウンリストに
  :guilabel:`GitHub Codespaces` を選択した状態にする。

それから UI 操作が記述どおりになっているかを確認すればいい。

* プラスアイコンで codespace を生成できそう。
* 項目の :guilabel:`Connect to Codespace` は機能する。現在の VS Code ウィンドウに
  ロードするので注意。新しいウィンドウで開くコマンドは別にある。
* 項目右クリックメニュー :guilabel:`Delete codespace` も機能しそうだ。

残りは割愛。

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

Customizing your codespace
======================================================================

  GitHub Codespaces is a dedicated environment for you. You can configure your
  repositories with a dev container to define their default GitHub Codespaces
  environment, and personalize your development experience across all of your
  codespaces with dotfiles and :menuselection:`Settings Sync`.

Personalizing GitHub Codespaces for your account
----------------------------------------------------------------------

  GitHub Codespaces personalization applies to any codespace you create.

方法は二つある：

* :menuselection:`Settings Sync`
* リポジトリー ``dotfiles``

まずは :menuselection:`Settings Sync` から見ていく。

  :menuselection:`Settings Sync` allows you to synchronize configurations such
  as settings, keyboard shortcuts, snippets, extensions, and UI state across
  machines and instances of VS Code. （略） For example, a common use of
  :menuselection:`Settings Sync` would be to sync your settings from your VS
  Code desktop application, which you use for local work, to codespaces you open
  in the browser.

まさにこれをやりたい。デスクトップ版の設定は壊さずに codespace のほうを変えたい。

* デスクトップ版 VS Code の :menuselection:`Settings Sync` をオン。
* GitHub でアカウント :menuselection:`Settings --> Codespaces` ページの
  :guilabel:`Settings Sync` をオンにする。
* オプションで逆方向の同期も可能だが、これは要らない。

あるいは、

  Alternatively, you may want to use the same settings across all codespaces you
  open in the web client, while leaving your local VS Code application
  unaffected.

こちらも利用する可能性はあるが、ひとまず保留。

  For codespaces opened in the VS Code web client, :menuselection:`Settings
  Sync` is disabled by default.

  :menuselection:`Settings Sync` is enabled in your user preferences
  automatically if you open a codespace in the web client and turn on
  :menuselection:`Settings Sync` in the codespace.

あとは trusted repositories という考えがあり、それも自動同期の要因になる。

他にも :guilabel:`Settings Sync` が見られる箇所があるが、方法は同様なので省略。

リポジトリー ``dotfiles`` で設定を同期させる方法を見ていく。

  When you create a new codespace, GitHub clones your selected ``dotfiles``
  repository to the codespace environment, and looks for one of the following
  files to set up the environment.

ファイル :file:`install.sh`, etc. をコピーする。ない場合に変なシンボリックリンク
が作られる。

  Any changes to your selected dotfiles repository will apply only to each new
  codespace, and do not affect any existing codespace.

GitHub アカウント :menuselection:`Settings --> Codespaces` ページで
:guilabel:`Automatically install dotfiles` をオンにする。

.. admonition:: 読者ノート

   ただし、可搬性のない内容のドットファイルを書いている自覚がある場合はオフにす
   る。

Renaming a codespace
----------------------------------------------------------------------

ブラウザーの場合は :guilabel:`Your codespaces` 画面の codespace 項目から
:guilabel:`Rename` を押す。

Changing the shell in a codespace
----------------------------------------------------------------------

  If you open a new codespace in the VS Code web client, or connect to a
  codespace over SSH, the terminal opens with a :command:`bash` session running
  by default.

それでいい。新しいシェルなぞ不要。

Changing the machine type for your codespace
----------------------------------------------------------------------

仮想マシンのメモリーとディスク容量を増やしたいときに検討する。

  Each machine type has a different level of resources and a different billing
  tier.

銭によって選択肢が決まる。

  By default the machine type with the lowest valid resources is used when you
  create a codespace. You can choose an alternative machine type either when you
  create a codespace or at any time after you've created a codespace.

変更可能性で言えば、対照的なのが：

  Unpublished codespaces (codespaces created from a template that are not linked
  to a repository on GitHub) always run on a virtual machine with the same
  specifications. You can't change the machine type of an unpublished codespace.

:guilabel:`Your codespaces` 画面 codespace 項目の :guilabel:`Change machine
type` を押す。

  If you changed to a virtual machine with a different storage capacity (for
  example, from 32 GB to 64 GB), your codespace will be unavailable for a short
  time while the machine type is changed.

同サイズの場合には次回起動時に使える。

Setting your default editor for GitHub Codespaces
----------------------------------------------------------------------

アカウント :menuselection:`Settings --> Codespaces --> Editor preference` で：

* Visual Studio Code (desktop application)
* Visual Studio Code (web client application)
* JetBrains Gateway - for opening codespaces in a JetBrains IDE
* JupyterLab - the web interface for Project Jupyter

ただし

  When you create a new codespace from a template, it is always opened in the
  Visual Studio Code web client.

VS Code 側設定は先述のとおり。

  The first time you open a codespace this way you must give permission to open
  the application.

Setting your default region for GitHub Codespaces
----------------------------------------------------------------------

日本から利用する場合には Southeast Asia でいいのか？

Setting your timeout period for GitHub Codespaces
----------------------------------------------------------------------

  A codespace will stop running after a period of inactivity. By default this
  period is 30 minutes, but you can specify a longer or shorter default timeout
  period in your personal settings on GitHub.

アカウント :menuselection:`Settings --> Codespaces --> Default retension period`
で期間を設定して :guilabel:`Save` を押す。

Configuring automatic deletion of your codespaces
----------------------------------------------------------------------

保管料という金銭に関わる概念があるので、保管期間を短く設定することが可能。

  The retention period is reset every time you connect to a codespace, and the
  retention countdown restarts when the codespace is stopped.

Codespace によって保管期間が異なることがある。

削除までの期間は :guilabel:`Codespaces` 画面 codespace 項目右上辺りで確認可能。

:guilabel:`Your codespaces` 画面 codespace 項目の :guilabel:`Keep codespace` を
押すと自動削除を免れる。そのぶん保存域や保管料に跳ね返る。

Setting up your project for GitHub Codespaces
======================================================================

Adding a dev container configuration to your repository
----------------------------------------------------------------------

  You can add a custom dev container configuration to your repository to set up
  the GitHub Codespaces development environment for your codebase.

Introduction to dev containers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  The configuration files for a dev container are contained in a
  :file:`.devcontainer` directory in your repository.

リポジトリーのルートにこの名前のディレクトリーを作成する。構成ファイルを入れる：

  When you create a codespace from a template, you might start with one or more
  dev container configuration files in your workspace.

主な構成ファイルは :file:`devcontainer.json` だ。開発コンテナーというものを規定
する。

  The :file:`devcontainer.json` file is usually located in the
  :file:`.devcontainer` directory of your repository.

内容の方向性：

  Things like linters are good to standardize on, and to require everyone to
  have installed, so they're good to include in your :file:`devcontainer.json`
  file. Things like user interface decorators or themes are personal choices
  that should not be put in the :file:`devcontainer.json` file.

そして：

  You can add a :file:`Dockerfile` as part of your dev container configuration.

:file:`Dockerfile` はコンテナーイメージを作成するために必要な指示を含むテキスト
ファイルだ。

  The :file:`Dockerfile` for a dev container is typically located in the
  :file:`.devcontainer` folder, alongside the :file:`devcontainer.json` in which
  it is referenced.

:file:`Dockerfile` の例が続く。割愛。

  For information about what's included in the default Linux image, see the
  :file:`devcontainers/images` repository.

おそらく、上級者はこの内容を軽くする方向に自作すると考えられる。

  If you use Codespaces in Visual Studio Code, or in a web browser, you can
  create a dev container configuration for your repository by choosing from a
  list of predefined configurations.

VS Code で作業する場合には Dev Containers 拡張があると良い。

  You can add features to a :file:`devcontainer.json` file from VS Code or from
  your repository on GitHub.com.

  If you don't already have a :file:`devcontainer.json` file in your repository,
  you can quickly add one from GitHub.com.

リポジトリー :menuselection:`Code --> Codespaces` を押す。
:guilabel:`Codespaces` の :menuselection:`... --> Configure dev container` を押
す。これで何らかの内容を含む JSON ファイルが開く。

構成ファイルを編集したらコンテナーを再構築するのが普通だ。

Setting up a Node.js project for GitHub Codespaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Get started with a Node.js, JavaScript, or TypeScript project in GitHub
  Codespaces by creating a custom dev container configuration.

とにかくやってみよう。

  After you complete this tutorial, you'll be able to add a dev container
  configuration to your own repository, using either the VS Code web client or
  the VS Code desktop application.

実際やるとハマる箇所が一つ。リビルド後 ``npm start`` するとモジュールがないエ
ラーが生じる。考えにくいが、エディターの拡張が干渉しているらしい。デバッガーを無
効にするとサーバーが動く。

Setting up a C# (.NET) project for GitHub Codespaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`PORT` タブの項目右クリックで :menuselection:`Open in Browser` を押す
手順を覚える。

Setting up a Java project for GitHub Codespaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VS Code の Java 拡張が有効になっていることを確認するべし。いつも無効になっている
から。

Setting up a PHP project for GitHub Codespaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

これは容易い。

Setting up a Python project for GitHub Codespaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Python はよく知っているので問題ない。デバッガーについては他の演習と同様の注意を
する。

Configuring dev containers
----------------------------------------------------------------------

  You can customize the dev container configuration for your repository.

上記の演習が終わったので構成の意味が体では理解できた今やるのがいい。

Setting a minimum specification for codespace machines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Each machine type has different resources (processor cores, memory, storage)
  and, by default, the machine type with the least resources is used.

これは以前確認した。:file:`devcontainer.json` で指定可能だというのが本稿の主旨
だ。

  You can't change the machine type of an unpublished codespace.

.. code:: json

   "hostRequirements": {
      "cpus": 8,
      "memory": "8gb",
      "storage": "32gb"
   }

これにより、GitHub Codespaces 画面上の Machine type 選択欄で低性能項目が選択不能
になる。

Adding features to a devcontainer.json file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  You can use features to quickly add tools, runtimes, or libraries to your
  codespace image.

:file:`devcontainer.json` の ``features`` に値を設定するのだが、先の演習では VS
Code の ``add dev`` 方式でそれを行った。

Automatically opening files in the codespaces for a repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VS Code ブラウザー版限定。演習における README が実例。

.. code:: json

   "customizations": {
     "codespaces": {
       "openFiles": [
         "README.md",
         "scripts/tsconfig.json",
         "docs/main/CODING_STANDARDS.md"
       ]
     }
   }

Specifying recommended secrets for a repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  You should use recommended secrets for secrets that the user who creates the
  codespace, rather than the owner of the repository or organization, must
  provide.

.. code:: json

   "secrets": {
     "NAME_OF_SECRET_1": {
       "description": "This is the description of the secret.",
       "documentationUrl": "https://example.com/link/to/info"
     },
     "NAME_OF_SECRET_2": { }
   }

JSON ファイルに機密情報を記入すると言っている？

  You can omit ``description`` and ``documentationUrl``, as shown by
  ``NAME_OF_SECRET_2`` in the previous code example.

Setting up your repository for GitHub Codespaces
----------------------------------------------------------------------

Facilitating quick creation and resumption of codespaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  You can make it easy for people to work on your repository in a codespace by
  providing a link to the codespace creation page. One place you might want to
  do this is in the :file:`README` file for your repository. For example, you
  can add the link to an :guilabel:`Open in GitHub Codespaces` badge.

百聞は一見に如かず。キャプチャーがわかりやすい。ああアレかと思える。

  Alternatively, you can link to the :guilabel:`Resume codespace` page, which
  provides a quick way for people to open a codespace they were working on
  recently.

こちらも普通か。

.. csv-table::
   :delim: |
   :header: URL,Codespace
   :widths: auto

   ``https://codespaces.new/OWNER/REPO-NAME`` | REPO-NAME の既定ブランチ
   ``https://codespaces.new/OWNER/REPO-NAME/tree/BRANCH-NAME`` | REPO-NAME のブランチ ``BRANCH-NAME``
   ``https://codespaces.new/OWNER/REPO-NAME/pull/PR-SHA`` | Pull request ``PR-SHA`` のブランチ

手順はこう：

  You can use the :guilabel:`Share a deep link` option to configure more options
  for the codespace and build a custom URL, then copy a Markdown or HTML snippet
  for an :guilabel:`Open in GitHub Codespaces` badge.

リポジトリー画面 :menuselection:`Code --> Codespaces` から :guilabel:`Share a
deep link` を押す。その UI を見れば全部わかる。

.. image:: https://github.com/codespaces/badge.svg
   :alt: Open in GitHub Codespaces
   :target: https://codespaces.new/showa-yojyo/showa-yojyo.github.io?quickstart=1

:guilabel:`Quick start` の意味：

  Add ``?quickstart=1`` to a ``codespaces.new`` URL, such as the URLs listed in
  the previous section of this article. This produces a URL that displays a
  :guilabel:`Resume codespace` page.

Setting up a template repository for GitHub Codespaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  You can help people get started with a project by setting up a template
  repository for use with GitHub Codespaces.

テンプレートリポジトリーを自作することが可能。

  If you don't have one, create a :file:`README` for your template repository to
  describe the purpose of your template and how to get started with it.

<https://github.com/codespaces> の :guilabel:`See all` の各テンプレートが参考に
なる。

あとは :file:`devcontainer.json` だ。

Prebuilding your codespaces
======================================================================

  To speed up codespace creation, you can configure your project to prebuild
  codespaces for specific branches in specific regions.

About GitHub Codespaces prebuilds
----------------------------------------------------------------------

  GitHub Codespaces prebuilds help to speed up the creation of new codespaces
  for large or complex repositories.

事前ビルドが有益な可能性がある場合は：

  If it currently takes more than 2 minutes to create a codespace for a
  repository, you are likely to benefit from using prebuilds.

事前ビルドの自動更新あり：

  By default, whenever you push changes to your repository, GitHub Codespaces
  uses GitHub Actions to automatically update your prebuilds.

いいときには :guilabel:`Prebuild ready` ラベルがマシンタイプ一覧項目に現れる。

時間効率に関する説明がここにある。

  By default, each push to a branch that has a prebuild configuration results in
  a GitHub-managed GitHub Actions workflow run to update the prebuild.

プッシュごとに重い処理が入ると考えた方がいい。

Configuring prebuilds
----------------------------------------------------------------------

  You can set up a prebuild configuration for the combination of a specific
  branch of your repository with a specific dev container configuration file.

ブランチごとなのだが、

  Any branches created from a prebuild-enabled parent branch will typically also
  get prebuilds for the same dev container configuration.

..

  Prebuilds are created using GitHub Actions.

無償ではない：

  The prebuild will consume storage space that will either incur a billable
  charge or, for repositories owned by your personal account, will use some of
  your monthly included storage.

事前構築手順：アカウント :menuselection:`Settings --> Codespaces` ページを開く。
:guilabel:`Set up prebuild` ボタンを押してフォームを埋めていく：

* :guilabel:`Configuration` で対象ブランチと :guilabel:`Configuration File` を決
  める。
* :guilabel:`Prebuild triggers` を選択。二番目が良さそうだが？
* :guilabel:`Reduce prebuild available to only specific regions` をオンにして
  :guilabel:`Southeast Asia` のみチェックを入れる。
* :guilabel:`Template history` をなるべく少なくいたい。

最後に :guilabel:`Create` を押す。これを実行する GitHub Actions workflow が起動
する。

Allowing a prebuild to access other repositories
----------------------------------------------------------------------

  You can permit your prebuild to access other GitHub repositories so that it
  can be built successfully.

だんだん複雑になってきている。

:file:`devcontainer.json` で permissions を定義する。

個人アクセストークンのため、新規アカウントを作成することになる。

  we strongly recommend creating a new account with access only to the target
  repositories required for your scenario.

..

  Give the new account read access to the required repositories.

Managing prebuilds
----------------------------------------------------------------------

  The prebuilds that you configure for a repository are created and updated
  using a GitHub Actions workflow, managed by the GitHub Codespaces service.

記述されている UI が確認できない。

Testing dev container configuration changes on a prebuild-enabled branch
----------------------------------------------------------------------

ここも時期尚早。

  After everything looks good, we also recommend creating a new codespace from
  your test branch to ensure everything is working.

Managing your codespaces
======================================================================

Managing secrets for your codespaces
----------------------------------------------------------------------

  You can add secrets to your personal account that you want to use in your
  codespaces.

この節で述べられる方法なら機密情報を設定するそれとして理解できる。

  Once you have created a secret, it will be available when you create a new
  codespace or restart the codespace.

アカウント :menuselection:`Settings --> Codespaces` ページを開く。:guilabel:`New
secrets` でフォームを埋めて :guilabel:`Add secrets` を押す。

  A secret is exported as an environment variable into the user's terminal
  session.

Codespace で機密情報が利用可能になるタイミングに注意。

Managing access to other repositories within your codespace
----------------------------------------------------------------------

  You should only authorize permissions for repositories you know and trust.

Reviewing your security logs for GitHub Codespaces
----------------------------------------------------------------------

  When you perform an action related to GitHub Codespaces in repositories owned
  by your personal account, you can review the actions in the security log.

アカウント :menuselection:`Settings --> Security log` で :guilabel:`codespaces`
イベントをフィルター。

Managing GPG verification for GitHub Codespaces
----------------------------------------------------------------------

  You can allow GitHub to automatically use GPG to sign commits you make in your
  codespaces, so other people can be confident that the changes come from a
  trusted source.

GPG 署名コミットの手法は以前習ったが、その鍵が codespace 環境で自動的に使われる
ことになると考えられる。

  After you enable GPG verification, GitHub will automatically sign commits you
  make in GitHub Codespaces, and the commits will have a verified status on
  GitHub.

署名を適用するリポジトリーを絞れ：

  If you have previously enabled GPG verification for all repositories, we
  recommend changing your preferences to use a selected list of trusted
  repositories.

やり方：アカウント :menuselection:`Settings --> Codespaces` ページを開いて
:guilabel:`GPG verification` で :guilabel:`Enable` を押す。

  Once you enable GPG verification, it will automatically take effect in any new
  codespaces you create from the relevant repositories. To have GPG verification
  take effect in an existing active codespace, you will need to stop and restart
  the codespace.

よく手を入れるリポジトリーを入れておこうか。

Managing GitHub Codespaces for your organization
======================================================================

割愛。

Reference
======================================================================

Allowing your codespace to access a private registry
----------------------------------------------------------------------

これは高度な技術だ。

Using GitHub Copilot in GitHub Codespaces
----------------------------------------------------------------------

無料利用者ゆえ GitHub Copilot は触らない。この項目は実現しないと思う。

Using the GitHub Codespaces plugin for JetBrains
----------------------------------------------------------------------

JetBrains とは？

Using the Visual Studio Code Command Palette in GitHub Codespaces
----------------------------------------------------------------------

おそらく VS Code の GitHub Codespaces 拡張を採用する必要がある。

Security in GitHub Codespaces
----------------------------------------------------------------------

  Two codespaces are never co-located on the same VM.

..

  Each codespace has its own isolated virtual network.

認証周りはどうか。

  If you connect from VS Code, you are prompted to authenticate with GitHub.

..

  Every time a codespace is created or restarted, it's assigned a new GitHub
  token with an automatic expiry period.

ポートはどうか。

  All forwarded ports are private by default, which means that you will need to
  authenticate before you can access the port.

機密情報はどうか。

  Always use secrets when you want to use sensitive information (such as access
  tokens) in a codespace. You can access your secrets as environment variables
  in the codespace, including from the terminal.

..

  Secrets are not copied into the environment if you don't have write access to
  the codespace's repository.

これを試すことはできるか：

  The :file:`devcontainer.json` file can contain powerful features, such as
  installing third-party extensions and running arbitrary code supplied in a
  ``postCreateCommand``.

..

  VS Code's :menuselection:`Settings Sync` can allow potentially malicious
  content to transfer across devices.

そんなバカな。

Disaster recovery for GitHub Codespaces
----------------------------------------------------------------------

  This article describes guidance for a disaster recovery scenario, when a whole
  region experiences an outage due to major natural disaster or widespread
  service interruption.

安全な地域に退避する。

Troubleshooting GitHub Codespaces
======================================================================

GitHub Codespaces logs
----------------------------------------------------------------------

.. code:: console

   bash$ gh codespace logs
   bash$ gh codespace logs -c <CODESPACE-NAME>

* :guilabel:`Codespaces: Export Logs`
* :guilabel:`Codespaces: View Creation Log`

ブラウザーの開発ツールの :guilabel:`Console` を見てもいい。

  If you encounter issues using GitHub Codespaces in a Chromium-based browser,
  you can check if you're experiencing another known issue with VS Code in the
  ``microsoft/vscode`` repository.

..

  If the :guilabel:`Simple Browser` tab does not open automatically, you can
  open the :guilabel:`Simple Browser` manually to view the application.

これはおすすめ。

Troubleshooting GitHub Codespaces clients
----------------------------------------------------------------------

  If you encounter issues using GitHub Codespaces in a Chromium-based browser,
  you can check if you're experiencing another known issue with VS Code in the
  `microsoft/vscode
  <https://github.com/microsoft/vscode/issues?q=is%3Aissue+is%3Aopen>`__
  repository.

Getting the most out of your included usage
----------------------------------------------------------------------

一ヶ月経てば無料利用枠が回復する。

  There are two types of Codespaces usage: compute and storage.

それぞれに対して利用料金が求められる。ディスク消費量は Codespaces ページで一覧か
ら確認可能。ただし：

  Although prebuilds are not listed on the :guilabel:`Your codespaces` page,
  prebuilds created for a repository consume storage even if you do not
  currently have any codespaces for that repository.

チュートリアルで作成していたら削除だ。

  You can check which image was used to create a codespace's dev container. In
  the Terminal of your codespace, run this command.

  .. code:: console

     bash$ devcontainer-info

このコマンドは codespace で実行するのか？

後半のコツをよく読んでおく。

Exporting changes to a branch
----------------------------------------------------------------------

リポジトリー :menuselection:`Code --> Codespaces` で対象 codespace の右側
:menuselection:`... --> Export changes to a branch` を押す。ブランチ名を確認して
:guilabel:`Create branch` ボタンを押す。

Troubleshooting creation and deletion of codespaces
----------------------------------------------------------------------

.. code:: console

   bash$ sudo apt autoremove
   bash$ sudo apt clean
   bash$ sudo find / -printf '%s %p\n' | sort -nr | head -10
   bash$ docker system prune
   bash$ git clean -i

Troubleshooting authentication to a repository
----------------------------------------------------------------------

これは難しい。

Troubleshooting your connection to GitHub Codespaces
----------------------------------------------------------------------

これは易しい。

Troubleshooting prebuilds
----------------------------------------------------------------------

事前構築の可否は仮想マシンの種類で決まる。

GitHub Codespaces をブラウザーで編集することにしている場合、:guilabel:`Setting
up your codespace` ページに事前構築が codesace があったと示される。

デスクトップ版 VS Code の場合にはコンソール内に長めのメッセージが示される。

Codespace 生成後、次の GitHub CLI コマンドで事前構築か否かを知ることが可能：

.. code:: console

   bash$ gh api /user/codespaces/$CODESPACE_NAME --jq .prebuild

ここからが問題と解決法の記述。

  By default, each time you push to a prebuild-enabled branch, the prebuild is
  updated. If the push involves a change to the dev container configuration
  then, while the update is in progress, the :guilabel:`Prebuild Ready` label is
  removed from the list of machine types.

ビルド中ならば当然そうなる。

特定のブランチに :guilabel:`Prebuild Ready` ラベルが表示されていない場合、確認し
たい事項：

* 当該ブランチに事前構築構成があること。
* 事前構築構成が例えば Southeast Asia を含むこと。
* コンテナーの設定に対する変更が有効ブランチに push されたかどうかを確認する。
* GitHub Actions の :guilabel:`Codespaces Prebuilds` の進行を確認する。

残りもこのような感じであらゆる原因が列挙されて解説されている。

Troubleshooting personalization options for GitHub Codespaces
----------------------------------------------------------------------

* GitHub アカウント :menuselection:`Settings --> Codespaces` ページの
  :guilabel:`Automatically install dotfiles` を確認する。
* Codespace の :file:`/workspaces/.codespaces/.persistedshare/dotfiles` を確認す
  る。
* :file:`/workspaces/.codespaces/.persistedshare/` にある次のファイルを確認する：

  * :file:`EnvironmentLog.txt`
  * :file:`creation.log`

..

  If the configuration from your dotfiles is correctly picked up, but part of
  the configuration is incompatible with codespaces, use the
  :envvar:`CODESPACES` environment variable to add conditional logic for
  codespace-specific configuration settings.

VS Code の :guilabel:`Settings Sync` をオフにする手順は、コマンドパレットを適当
に検索すればわかる。

Troubleshooting port forwarding for GitHub Codespaces
----------------------------------------------------------------------

  If a port is not automatically forwarded, you can forward it manually.

..

  Typically, you can make a forwarded port accessible publicly, or within the
  organization that owns a repository.

..

  If you reference a forwarded port in your code, for example in a test, we
  recommend that you use an environment variable instead of hardcoding the URL.

Troubleshooting GPG verification for GitHub Codespaces
----------------------------------------------------------------------

GPG 署名全般に関しては Authentication の章で学んだ。

  To have GPG verification take effect in an existing active codespace, you will
  need to stop and restart the codespace.

自動で署名するということは、Git 設定が次のようになっていることを意味する：

  When you enable GPG verification, GitHub Codespaces signs all the commits you
  make in codespaces by default. It does this by setting the ``commit.gpgsign``
  Git configuration value to ``true``.

GitHub 側の自動設定とドットファイルの設定内容が食い違っている場合に問題になるだ
ろう。

ここからは詳細な解決策が記されているので、実際問題になったら本文を当たることにす
る。

Working with support for GitHub Codespaces
----------------------------------------------------------------------

  Each codespace has a unique name that is a combination of your GitHub handle,
  two or three automatically generated words, and some random characters.

言われてみれば codespace の名前の初期値は変なものだ。

  Every codespace also has an ID (identifier). This is not shown by default in
  Visual Studio Code so you may need to update the settings for the GitHub
  Codespaces extension before you can access the ID.

VS Code のサイドバーに :guilabel:`CODESPACE PERFORMANCE` 区画を表示させる。この
最初の項目が ID だ。
