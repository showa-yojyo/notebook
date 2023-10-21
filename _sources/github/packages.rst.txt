======================================================================
GitHub Packages documentation ノート
======================================================================

`GitHub Packages documentation <https://docs.github.com/en/packages>`__ を読んで
いく。以下、組織回りの記述は読解を割愛することがある。

.. contents::
   :depth: 3

* :guilabel:`Quickstart` → :ref:`Quickstart for GitHub Packages <packages-quickstart>`
* :guilabel:`Reference` → :ref:`Learn GitHub Packages <packages-reference>`

.. _packages-quickstart:

Quickstart for GitHub Packages
======================================================================

JavaScript の簡単なパッケージを構築して発行するというチュートリアルだ。おそらく
GitHub Actions の文書を先に読む方がいい。

チュートリアルは容易だ。Node.js ベースのプロジェクトの発行方法しか習得できていな
いことを忘れるな。

   The workflow that you created will run whenever a new release is created in
   your repository. If the tests pass, then the package will be published to
   GitHub Packages.

``git push`` を実行したらリポジトリーページの右柱のリンク :guilabel:`Releases`
を押す。手順にはなかったが、あらかじめタグを付けておくと良い。フォームを埋めて
:guilabel:`Publish release` ボタンを押すことで、作成したworkflow が引き起こされ
る。Actions 画面でジョブの進捗を確認すると良い。

完成すると、パッケージ一覧が現れる。

   You can view all of the packages you have published.

リポジトリーを一つとったときに、その発行済みパッケージ全てを見られると言ってい
る。方法はリポジトリーメインページの右柱 :guilabel:`Packages` を押す。

このようにして発行されたパッケージは、別のプロジェクトから依存されることが可能と
なる。

   Combining GitHub Packages and GitHub Actions can help you automate nearly
   every aspect of your application development processes.

これらの GitHub 機能を合わせて使えると能力を売り込める？

.. _packages-reference:

Learn GitHub Packages
======================================================================

   GitHub Packages is a software package hosting service that allows you to host
   your software packages privately or publicly and use packages as dependencies
   in your projects.

Introduction to GitHub Packages
----------------------------------------------------------------------

   You can integrate GitHub Packages with GitHub APIs, GitHub Actions, and
   webhooks to create an end-to-end DevOps workflow that includes your code, CI,
   and deployment solutions.

Quickstart で見たのは GitHub Actions を用いた実現だった。

パッケージ登録所の概念を知らないのでどうするか。

パッケージの README はリポジトリーのそれとは異なる？

パッケージにも public or private の性質がある。

   GitHub Packages usage is free for public packages.

それでいい。

   GitHub Packages uses the native package tooling commands you're already
   familiar with to publish and install package versions.

これがあるので :file:`package.json` だの :file:`Gemfile` だのが重要。

   You need an access token to publish, install, and delete private, internal,
   and public packages.

Quickstart で言うと :file:`release-package.yml` で ``secret.GITHUB_TOKEN`` を利
用していた。

   You can configure webhooks to subscribe to package-related events, such as
   when a package is published or updated.

この機能はまだ見たことがない。

About permissions for GitHub Packages
----------------------------------------------------------------------

   The permissions for packages can be scoped either to a user or an
   organization or to a repository.

わかりやすい分類。

   You can change the access control and visibility of the package separately
   from a repository that is connected (or linked) to a package.

パッケージの public/private とリポジトリーのそれは独立していると考えていい。

   You can find a package scoped to a repository by going to the main page of
   the repository and clicking the :guilabel:`Packages` link to the right of the
   page.

このリンクの見てくれがリンクらしからぬものなので、初見だと一覧がないこともあり見
逃しやすい。

   In most registries, to pull a package, you must authenticate with a personal
   access token or ``GITHUB_TOKEN``, regardless of whether the package is public
   or private.

これがあるからトークンの扱いが重要なのだ。

   For packages scoped to a personal account, you can give any person an access
   role.

   When you create a GitHub Actions workflow, you can use the ``GITHUB_TOKEN``
   to publish, install, delete, and restore packages in GitHub Packages without
   needing to store and manage a personal access token.

Quickstart 方式。

リポジトリーを移転する際、パッケージが属する登録所によっては、GitHub がそのリポ
ジトリーに関連するパッケージを移転することがある。

パッケージへアクセスする workflow においては、正しいアクセストークンを使っている
ことと、パッケージへの GitHub Actions アクセスを有効にしていること。

   To ensure your workflows have access to packages stored in registries that
   support granular permissions, you must give GitHub Actions access to the
   repositories where your workflow is run. You can find this setting on your
   package's settings page.

Configuring a package's access control and visibility
----------------------------------------------------------------------

   By default, if you publish a package that is linked to a repository, the
   package automatically inherits the access permissions (but not the
   visibility) of the linked repository.

パッケージの公開・非公開性がリポジトリーから（最初は）決まる。このとき、リポジト
リーに関係する GitHub Actions もパッケージにアクセス可能になる。

   When a package inherits permissions from a repository, to grant or remove
   access to your package, you must configure the permissions settings of the
   linked repository.

   If you publish a package in a registry that only supports repository-scoped
   permissions, the package is always linked to a repository, and always
   inherits the permissions of the linked repository.

前にも見たが登録所によって権限付与の枠組が異なる。

   If a package belongs to a registry that supports granular permissions, anyone
   with admin permissions to the package can set the package to private or
   public, and can grant access permissions for the package that are separate
   from the permissions set at the organization and repository levels.

先にも述べられていたかもしれない。

   When you publish a package, you automatically get admin permissions to the
   package.

   For packages scoped to a personal account, you can give any person an access
   role.

さっきメモし忘れた：

   If you are using a GitHub Actions workflow to manage your packages, you can
   grant an access role to the repository the workflow is stored in by using the
   :guilabel:`Add Repository` button under :guilabel:`Manage Actions access` in
   the package's settings.

権限表を頭に叩き込む。

   If your package is private or internal and scoped to an organization, then
   you can only give access to other organization members or teams.

対象パッケージページ右柱の :guilabel:`Pacakge settings` を押す。権限変更関連の
UI が複数ある。

   If you have admin permissions to a package that is scoped to an organization,
   you can assign read, write, or admin roles to other users and teams.

操作は同様。

   If you want to configure a package's access settings on a granular level,
   separately from the linked repository, you must remove the inherited
   permissions from the package.

:guilabel:`Inherit access from repository (recommended)` をオンにする。

   For packages scoped to a personal account or an organization, to ensure that
   a GitHub Actions workflow has access to your package, you must give explicit
   access to the repository where the workflow is stored.

:guilabel:`Manage Actions access` の脇にある :guilabel:`Add repository` ボタンを
押す。リポジトリー一覧が出るから先は分かる。

Codespaces でも同様の操作を可能。

   When you first publish a package that is scoped to your personal account, the
   default visibility is private and only you can see the package.

これは不本意なので public にする。:guilabel:`Change visibility` を押す。ただし：

   Warning: Once you make a package public, you cannot make it private again.

Connecting a repository to a package
----------------------------------------------------------------------

   When you publish a package that is scoped to a personal account or an
   organization, the package is not linked to a repository by default.

リンクする方がいいのでそう変える。

パッケージ :guilabel:`Connect repository` でリポジトリーを選んで
:guilabel:`Connect repository` を押す。UI が見当たらない？
その場合はすでにリンクされているという理解でいいか。

:file:`Dockerfile` はわからないからパス。Docker をインストールしてみたものの、マ
シンに積んでいるメモリーが貧弱であるせいで動作しなかった。

Publishing a package
----------------------------------------------------------------------

   A repository can be connected to more than one package. To prevent confusion,
   make sure the README and description clearly provide information about each
   package.

README はとにかく丁寧に作ろう。

   You can publish a package to GitHub Packages using any supported package
   client by following the same general guidelines.

次の章でまとめられている。だいたい言語ごとに方法が定まっているという理解だ。

   Publish the package using the instructions for your package client.

パッケージ登録所もよく知らないとダメだ。

Viewing packages
----------------------------------------------------------------------

   By default, you can view all packages you have published.

逆に、見られない状態とは何だ？

   On the package page, GitHub provides metadata for each version, such as the
   publication date. You can see details about the package, including a
   description and installation and usage instructions. You can download any
   assets associated with the package and see information about download
   activity.

特にダウンロード数がはっきり確認できるのは大きい。リポジトリーページ右柱の
:guilabel:`Packages` を押して一覧を見ればわかる。

Installing a package
----------------------------------------------------------------------

   You can install a package from GitHub Packages and use the package as a
   dependency in your own project.

よそのパッケージをインストールしたい。

   After you find a package, you can read the package's description and
   installation and usage instructions on the package page.

Deleting and restoring a package
----------------------------------------------------------------------

自作のパッケージであっても無条件で削除できるわけではない：

   You cannot delete a public package if any version of the package has more
   than 5,000 downloads.

心配には及ばない。

復元条件は：

   On GitHub, you can also restore an entire package or package version, if:

   * You restore the package within 30 days of its deletion.
   * The same package namespace is still available and not used for a new
     package.

パッケージ操作は REST API を介して行うことが可能：

   With registries that support granular permissions, you can use a
   ``GITHUB_TOKEN`` in a GitHub Actions workflow to delete or restore packages
   using the REST API. The token must have admin permission to the package.

普通の削除の手順は次と思われる：

   To delete a version of a repository-scoped package, you must have admin
   permissions to the repository in which the package is published.

パッケージ :guilabel:`View and manage all versions` ページの :guilabel:`Delete`
を押す。

コマンドラインから :command:`curl` で削除可能のようだが割愛。

   To delete an entire repository-scoped package, you must have admin
   permissions to the repository that owns the package.

これには :guilabel:`Delete this package` を押す。

復元手順は UI 操作が今までと異なる。アカウント :menuselection:`Settings -->
Packages` の :guilabel:`Deleted packages` 一覧にモノがあれば :guilabel:`Restore`
可能。

Working with a GitHub Packages registry
======================================================================

Working with the Container registry
----------------------------------------------------------------------

   You can store and manage Docker and OCI images in the Container registry,
   which uses the package namespace ``https://ghcr.io``.

Container 登録所という概念が上記のパッケージ名前空間を用いることを覚えておく。

   The Container registry stores container images within your organization or
   personal account, and allows you to associate an image with a repository.

登録所は誰かのアカウントにある container images というものが置いてある場所。それ
らはリポジトリーと結びつくことの二点を覚えておく。

Container 登録所は現在二種類の image formats を対応している。

   To authenticate to a GitHub Packages registry within a GitHub Actions
   workflow, you can use:

   * ``GITHUB_TOKEN`` to publish packages associated with the workflow
     repository.
   * a personal access token (classic) with at least ``read:packages`` scope to
     install packages associated with other private repositories (which
     ``GITHUB_TOKEN`` can't access).

たぶん前者を使うのがいい。

   This registry supports granular permissions.

この権限が使える登録所に対しては ``GITHUB_TOKEN`` 推奨。

   You can use a ``GITHUB_TOKEN`` in a GitHub Actions workflow to delete or
   restore a package using the REST API, if the token has ``admin`` permission
   to the package.

YAML に REST API を呼び出すコードを書くものと考えられる。

   You can also choose to give access permissions to packages independently for
   GitHub Codespaces and GitHub Actions.

Package ページの UI からそうだと思う。

   GitHub Packages only supports authentication using a personal access token
   (classic).

トークン作成画面のチェックの入れ方は、例えば：

   Select the ``read:packages`` scope to download container images and read
   their metadata.

このトークンを手許の環境に環境変数の値として控えておくことを推奨している。変数名
は ``CR_PAT`` として説明を続けている。こういうコマンドを実行することがあるので：

.. code:: console

   bash$ echo $CR_PAT | docker login ghcr.io -u USERNAME --password-stdin

.. todo::

   :command:`docker` コマンド操作各種

Working with the Docker registry
----------------------------------------------------------------------

   The Docker registry has now been replaced by the Container registry.

だそうなので、前節を習得すれば十分。

名前空間 ``docker.pkg.github.com`` を使っていたが、名前空間 ``https://ghcr.io``
を使う。

   Docker images previously stored in the Docker registry are being
   automatically migrated into the Container registry.

作ったことがないので無関係。

Working with the RubyGems registry
----------------------------------------------------------------------

   You can configure RubyGems to publish a package to GitHub Packages and to use
   packages stored on GitHub Packages as dependencies in a Ruby project with
   Bundler.

RubyGems の場合も：

   This registry supports granular permissions.

Gem を作って配るのが目的だ。その設定をローカルでまず行う：

   To publish new gems, you need to authenticate to GitHub Packages with
   RubyGems by editing your :file:`~/.gem/credentials` file to include your
   personal access token (classic). Create a new :file:`~/.gem/credentials` file
   if this file doesn't exist.

正確なパスをコマンド ``gem env`` で調べるといい。
:file:`~/.local/share/gem/credentials` の可能性がある。

.. code:: text

   ---
   :github: Bearer TOKEN

Gem 設定：

   To install gems, you need to authenticate to GitHub Packages by updating your
   gem sources to include
   ``https://USERNAME:TOKEN@rubygems.pkg.github.com/NAMESPACE/``

.. code:: console

   bash$ gem sources --add https://USERNAME:TOKEN@rubygems.pkg.github.com/NAMESPACE/

Bundler 設定：

   To authenticate with Bundler, configure Bundler to use your personal access
   token (classic), replacing ``USERNAME`` with your GitHub username, ``TOKEN``
   with your personal access token, and ``NAMESPACE`` with the name of the
   personal account or organization to which the gem is scoped.

   .. code:: console

      bash$ bundle config https://rubygems.pkg.github.com/NAMESPACE USERNAME:TOKEN

これまでの手順で発行の準備が整ったと思われる。

   When you first publish a package, the default visibility is private.

これを先述の方法で public に変える。ビルドしたら次のようにして GitHub に発行す
る：

.. code:: console

   $bash gem push --key github --host https://rubygems.pkg.github.com/NAMESPACE GEM_NAME-0.0.1.gem

..

   You can ensure gems will be linked to a repository as soon as they are
   published by including the URL of the GitHub repository in the
   ``github_repo`` field in ``gem.metadata``.

.. code:: ruby

   gem.metadata = { "github_repo" => "ssh://github.com/OWNER/REPOSITORY" }

..

   You can use gems from GitHub Packages much like you use gems from
   rubygems.org.

:file:`Gemfile` に ``source`` を追加する：

.. code:: ruby

   source "https://rubygems.pkg.github.com/NAMESPACE"
   source "https://rubygems.org"

   gem "rails"
   gem "GEM_NAME"

これで ``gem install GEM_NAME`` コマンドでインストール可能だ。

Working with the npm registry
----------------------------------------------------------------------

   This registry supports granular permissions.

ざっと読む限り GitHub に関することは RubyGems と共通している。

   You can authenticate to GitHub Packages with npm by either editing your
   per-user :file:`~/.npmrc` file to include your personal access token
   (classic) or by logging in to npm on the command line using your username and
   personal access token.

設定ファイルパスは :file:`$XDG_CONFIG_HOME/npm/npmrc` とした。以下ではそう読み替
える。こんな感じの行を書く：

.. code:: text

   //npm.pkg.github.com/:_authToken=TOKEN

..

   To authenticate by logging in to npm, use the ``npm login`` command,
   replacing ``USERNAME`` with your GitHub username, ``TOKEN`` with your
   personal access token (classic), and ``PUBLIC-EMAIL-ADDRESS`` with your email
   address.

下のコマンドのようにする：

.. code:: console

   bash$ npm login --scope=@NAMESPACE --auth-type=legacy --registry=https://npm.pkg.github.com
   npm notice Log in on https://npm.pkg.github.com/
   Username: USERNAME
   Password: TOKEN

オプション ``--auth-type=legacy`` の適用条件は本文参照。

   You can connect a package to a repository as soon as the package is published
   by including a repository field in the :file:`package.json` file.

このあたりの記述は Quickstart で実践済みだからわからないことはないと思う。

   You can set up the scope mapping for your project using either a local
   :file:`.npmrc` file in the project or using the ``publishConfig`` option in
   the :file:`package.json`. GitHub Packages only supports scoped npm packages.

プロジェクト用の :file:`.npmrc` を設けるものとする。

   In the :file:`.npmrc` file, use the GitHub Packages URL and account owner so
   GitHub Packages knows where to route package requests.

さっきの ``_authToken=`` 行の近くに書くといい：

.. code:: text

   @NAMESPACE:registry=https://npm.pkg.github.com

それから :file:`package.json` の ``name`` と ``repository`` の値を確認してコマン
ド ``npm publish`` を実行すればよい。

``publishConfig`` を用いる場合は：

.. code:: json

   "publishConfig": {
     "registry": "https://npm.pkg.github.com"
   },

..

   You can install packages from GitHub Packages by adding the packages as
   dependencies in the :file:`package.json` file for your project.

先ほど述べられたものと同じものを書く。

   You also need to add the :file:`.npmrc` file to your project so that all
   requests to install packages will go through GitHub Packages.

:file:`package.json` では依存関係の定義が急所となる：

.. code:: json

   "dependencies": {
     "ORGANIZATION_NAME/PACKAGE_NAME": "1.0.0"
   }

コマンド ``npm install`` でインストール。

Working with the Apache Maven registry
----------------------------------------------------------------------

   You can configure Apache Maven to publish packages to GitHub Packages and to
   use packages stored on GitHub Packages as dependencies in a Java project.

これは Java の話題だ。

   You can authenticate to GitHub Packages with Apache Maven by editing your
   :file:`~/.m2/settings.xml` file to include your personal access token
   (classic). Create a new :file:`~/.m2/settings.xml` file if one doesn't exist.

Maven のユーザー設定ファイルは :file:`~/.m2/settings.xml` であるとして話を進め
る。

``servers`` および ``repositories`` 要素を適宜定義する。

パッケージディレクトリーのファイル :file:`pom.xml` を次のようにする：

.. code:: xml

   <distributionManagement>
      <repository>
        <id>github</id>
        <name>GitHub OWNER Apache Maven Packages</name>
        <url>https://maven.pkg.github.com/OWNER/REPOSITORY</url>
      </repository>
   </distributionManagement>

コマンド ``mvn deploy`` で発行する。

   To install an Apache Maven package from GitHub Packages, edit the
   :file:`pom.xml` file to include the package as a dependency.

.. code:: xml

   <dependencies>
    <dependency>
       <groupId>com.example</groupId>
       <artifactId>test</artifactId>
       <version>1.0.0-SNAPSHOT</version>
     </dependency>
   </dependencies>

コマンド ``mvn install`` でインストール。

Working with the Gradle registry
----------------------------------------------------------------------

こちらも Java の話題か？

   You can authenticate to GitHub Packages with Gradle using either Gradle
   Groovy or Kotlin DSL by editing your :file:`build.gradle` file (Gradle
   Groovy) or :file:`build.gradle.kts` file (Kotlin DSL) file to include your
   personal access token (classic).

..

   Because uppercase letters aren't supported, you must use lowercase letters
   for the repository owner even if the GitHub user or organization name
   contains uppercase letters.

両者の単一パッケージ用と複数パッケージ用の例コードがある。

コマンド ``gradle publish`` で発行する。

   To use a published package from GitHub Packages, add the package as a
   dependency and add the repository to your project.

設定ファイルに ``dependencies`` と ``repositories`` の詳細を記述する。

Working with the NuGet registry
----------------------------------------------------------------------

   You can configure the dotnet command-line interface (CLI) to publish NuGet
   packages to GitHub Packages and to use packages stored on GitHub Packages as
   dependencies in a .NET project.

久しぶりに：

   This registry supports granular permissions.

..

   Use the following command to authenticate to GitHub Packages in a GitHub
   Actions workflow using the ``GITHUB_TOKEN`` instead of hardcoding a personal
   access token in a :file:`nuget.config` file in the repository:

   .. code:: console

      bash$ dotnet nuget add source --username USERNAME --password ${{ secrets.GITHUB_TOKEN }} --store-password-in-clear-text --name github "https://nuget.pkg.github.com/NAMESPACE/index.json"

   To authenticate to GitHub Packages with the :command:`dotnet` command-line
   interface (CLI), create a :file:`nuget.config` file in your project directory
   specifying GitHub Packages as a source under ``packageSources`` for the
   :command:`dotnet` CLI client.

この設定ファイルは XML だ。次のように記述する：

.. code:: xml

   <?xml version="1.0" encoding="utf-8"?>
   <configuration>
       <packageSources>
           <clear />
           <add key="github" value="https://nuget.pkg.github.com/NAMESPACE/index.json" />
       </packageSources>
       <packageSourceCredentials>
           <github>
               <add key="Username" value="USERNAME" />
               <add key="ClearTextPassword" value="TOKEN" />
           </github>
       </packageSourceCredentials>
   </configuration>

..

   You can publish a package to GitHub Packages by authenticating with a
   :file:`nuget.config` file, or by using the ``--api-key`` command line option
   with your GitHub personal access token (classic).

   If you specify a ``RepositoryURL`` in your :file:`nuget.config` file, the
   published package will automatically be connected to the specified
   repository.

トークンを API キーとして用いるか、:file:`nuget.config` を用いるかしてパッケージ
を発行する方法がある。前者は：

.. code:: console

   bash$ dotnet pack --configuration Release
   bash$ dotnet nuget push "bin/Release/PROJECT_NAME.1.0.0.nupkg" --api-key YOUR_GITHUB_PAT --source "github"

後者ではプロジェクトの ``.csproj`` ファイルをこのように書き換えて：

.. code:: xml

   <Project Sdk="Microsoft.NET.Sdk">
     <PropertyGroup>
       <OutputType>Exe</OutputType>
       <TargetFramework>netcoreapp3.0</TargetFramework>
       <PackageId>PROJECT_NAME</PackageId>
       <Version>1.0.0</Version>
       <Authors>AUTHORS</Authors>
       <Company>COMPANY_NAME</Company>
       <PackageDescription>PACKAGE_DESCRIPTION</PackageDescription>
       <RepositoryUrl>https://github.com/OWNER/REPOSITORY</RepositoryUrl>
     </PropertyGroup>
   </Project>

コマンド実行する（オプションが一つ減る）：

.. code:: console

   bash$ dotnet pack --configuration Release
   bash$ dotnet nuget push "bin/Release/PROJECT_NAME.1.0.0.nupkg" --source "github"

Migrating to the Container registry from the Docker registry
----------------------------------------------------------------------

   The Container registry replaces GitHub's Docker registry. If you've stored
   Docker images in the Docker registry, GitHub will gradually migrate the
   images to the Container registry. No action is required on your part.

この移行処理により、パッケージの詳細が変化する：

   * The package icon will be the Container registry logo instead of the Docker
     logo.
   * The domain in the pull URL will be ``ghcr.io`` instead of
     ``docker.pkg.github.com``.

Container 登録所ロゴは角砂糖を等角投影図法で描いたような図像だ。

   Any scripts or GitHub Actions workflows that use the namespace for the Docker
   registry, ``docker.pkg.github.com``, will continue to work after migration to
   the Container registry at ``ghcr.io``.

こういう自動移行が発生すると、GitHub Actions への影響を考慮する習慣を持ちたい。

Managing GitHub packages using GitHub Actions workflows
======================================================================

GitHub Actions を使ったパッケージ処理を見ていく？

Publishing and installing a package with GitHub Actions
----------------------------------------------------------------------

Quickstart で少し見たように：

   You can configure a workflow in GitHub Actions to automatically publish or
   install a package from GitHub Packages.

..

   You can extend the CI and CD capabilities of your repository by publishing or
   installing packages as part of your workflow.

どこかで読んだような文が続く。

   If you want your workflow to access a GitHub Packages registry that does not
   support granular permissions, then we recommend using the ``GITHUB_TOKEN``
   that GitHub automatically creates for your repository when you enable GitHub
   Actions. You should set the permissions for this access token in the workflow
   file to grant read access for the ``contents`` scope and write access for the
   ``packages`` scope.

トークン設定ページを見てこの記述を確認しろ。

   All workflows accessing registries that support granular permissions should
   use the ``GITHUB_TOKEN`` instead of a personal access token.

これも前に見た。

   When you enable GitHub Actions, GitHub installs a GitHub App on your
   repository. The ``GITHUB_TOKEN`` secret is a GitHub App installation access
   token. You can use the installation access token to authenticate on behalf of
   the GitHub App installed on your repository.

この原理を理解する。

``GITHUB_TOKEN`` を使用した workflow がパッケージを作成する場合、既定の権限とア
クセスがある。

   You can use GitHub Actions to automatically publish packages as part of your
   continuous integration (CI) flow.

一環としての発行なので、テストに成功していないと発動しない。

ここで GitHub Actions を使ってモノをビルドし、Docker イメージを自動的に作成して
GitHub Packages に公開する方法を示す例が示されている。リポジトリーに
:file:`.github/workflows/deploy-image.yml` のようなパスに workflow を定義する。

完了すると、新しいパッケージがリポジトリーに表示される。

パッケージのインストールについても同じような考え方をする。

   Installing packages hosted by GitHub Packages through GitHub Actions requires
   minimal configuration or additional authentication when you use the
   ``GITHUB_TOKEN``. Data transfer is also free when an action installs a
   package.

次の利点を覚えておく：

   Using the ``GITHUB_TOKEN``, instead of a personal access token (classic) with
   the repo scope, increases the security of your repository as you don't need
   to use a long-lived personal access token that offers unnecessary access to
   the repository where your workflow is run.

パッケージから workflow にアクセス可能にする：

   To ensure your package has access to your workflow, you must add the
   repository where the workflow is stored to your package.

:guilabel:`Manage Actions access` の :guilabel:`Add Repository`` ボタンを押す。

YAML ファイル内の登録所にログインする箇所で ``${{ secrets.GITHUB_TOKEN }}`` を
使って認証させる。

Example workflows for publishing a package
----------------------------------------------------------------------

次の GitHub Actions documentation 内へのリンクがある：

* Publishing Node.js packages
* Publishing Docker images
* Publishing Java packages with Maven
* Publishing Java packages with Gradle

ノートを取るとしたら、そちらのノートで行う。

About GitHub Packages and GitHub Actions
----------------------------------------------------------------------

   Creating a package at the end of a continuous integration workflow can help
   during code reviews on a pull request.

パッケージ作りもレビューの助けになる？

   Depending on the kind of application you're building, this package can be
   downloaded locally for manual testing, made available for users to download,
   or deployed to a staging or production environment.

レビュー担当者が成果物パッケージをダウンロードして検査できるわけだ。

パッケージを GitHub Packages またはパッケージ登録所に発行する。前者の場合：

   You may want to publish packages to GitHub Packages on every push into the
   default branch. This will allow developers on your project to always be able
   to run and test the latest build from the default branch easily, by
   installing it from GitHub Packages.

後者に対しては：

   You can automate this by creating a workflow that publishes packages to a
   package registry on every release creation.
