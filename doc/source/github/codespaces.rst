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
