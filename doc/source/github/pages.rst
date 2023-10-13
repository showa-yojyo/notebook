======================================================================
GitHub Pages documentation ノート
======================================================================

`GitHub Pages documentation <https://docs.github.com/en/pages>`__ は当読書ノート
を公表する場の基盤となる機能に関する文書だ。全部読んで然るべきだろう。

.. contents::
   :depth: 3

* :guilabel:`Quickstart` → 個別記事である Quickstart for GitHub Pages
* :guilabel:`Overview` → :ref:`About GitHub Pages <pages-about-github-pages>`

Quickstart for GitHub Pages
======================================================================

   GitHub Pages are public webpages hosted and published through GitHub.

ウェブページを公表する場と単純に考えても問題ない。

最初に個人サイトを作成する手順をまとめる。アカウント名が ``username`` だとする
と、サイト名は ``username.github.io`` だ。以下、 ``username`` を適宜自分のアカウ
ント名に置き換えて読め。

#. GitHub 画面天井右上メニュー :menuselection:`+ --> New repository` 選択。
#. :guilabel:`Repository name` に ``username.github.io`` を記入。
#. このリポジトリー画面 :menuselection:`Settings --> Pages` ページを開く。
#. :menuselection:`Build and deployment --> Source` に :guilabel:`Deploy from a
   branch` を指定。
#. :menuselection:`Build and deployment --> Branch` に発表したいウェブサイトの源
   があるブランチを指定。

:file:`README.md` も書いておくといい。

   Visit ``username.github.io`` to view your new website. Note that it can take
   up to 10 minutes for changes to your site to publish after you push the
   changes to GitHub.

サイトの題名を変えるには、:file:`_config.yml` を編集する。

.. admonition:: 読者ノート

   このように GitHub でアカウント名ベースのリポジトリーを初期化すると、Jekyll
   ベースのサイトを生成してくれるようだ。

Getting started with GitHub Pages
======================================================================

.. _pages-about-github-pages:

About GitHub Pages
----------------------------------------------------------------------

   GitHub Pages is a static site hosting service that takes HTML, CSS, and
   JavaScript files straight from a repository on GitHub, optionally runs the
   files through a build process, and publishes a website.

もう実践済みなのでよく理解している。

   You can host your site on GitHub's github.io domain or your own custom
   domain.

後者は知らない。

   There are three types of GitHub Pages sites: project, user, and organization.

組織以外はよく知っている。

   To publish a user site, you must create a repository owned by your personal
   account that's named ``<username>.github.io``. To publish an organization
   site, you must create a repository owned by an organization that's named
   ``<organization>.github.io``.

この記述から利用者サイトと組織サイトは同様に理解可能とわかる。

URL について：

   Unless you're using a custom domain, project sites are available at
   ``http(s)://<username>.github.io/<repository>`` or
   ``http(s)://<organization>.github.io/<repository>``.

カスタムドメインについては後述。

   Warning: GitHub Pages sites are publicly available on the internet, even if
   the repository for the site is private.

GitHub の言う private の意味は通常のそれとはけっこう異なることが多い。

   If you do not need any control over the build process for your site, we
   recommend that you publish your site when changes are pushed to a specific
   branch.

通常はこれで事足りる。本文にあるように、特定のサブディレクトリーの内容がそのまま
サイトになる。

   If you want to use a build process other than Jekyll or you do not want a
   dedicated branch to hold your compiled static files, we recommend that you
   write a GitHub Actions workflow to publish your site.

Sphinx はこのパターンを適用する典型だ。

   If you publish your site from a source branch, GitHub Pages will use Jekyll
   to build your site by default.

特に断りのない限り Jekyll サイトだと GitHub に思われる。断る方法はファイル
:file:`.nojekyll` を文書ルートに置いておくことだ。

   GitHub Pages does not support server-side languages such as PHP, Ruby, or
   Python.

それは残念だ。

   GitHub Pages sites are subject to the following usage limits:

破る可能性のある項目を頭に叩き込め：

   * GitHub Pages source repositories have a recommended limit of 1 GB.
   * Published GitHub Pages sites may be no larger than 1 GB.
   * GitHub Pages deployments will timeout if they take longer than 10 minutes.

当読書ノートにおいて、ビルド時間 10 分以内条件がそろそろ危ない。これらの利用枠を
超える使い方をするとGitHub からメールが来るようだ。

   When a GitHub Pages site is visited, the visitor's IP address is logged and
   stored for security purposes, regardless of whether the visitor has signed
   into GitHub or not.

そのデータはリポジトリー所有者に提供してもらえないか。

Creating a GitHub Pages site
----------------------------------------------------------------------

   If you want to create a GitHub Pages site for a repository where not all of
   the files in the repository are related to the site, you will be able to
   configure a publishing source for your site.

普通はこのパターンだと思う。

   Create the entry file for your site. GitHub Pages will look for an
   :file:`index.html`, :file:`index.md`, or :file:`README.md` file as the entry
   file for your site.

パターンその一：

   For example, if your publishing source is the :file:`/docs` folder on the
   ``main`` branch, your entry file must be located in the :file:`/docs` folder
   on a branch called ``main``.

パターンその二：

   If your publishing source is a GitHub Actions workflow, the artifact that you
   deploy must include the entry file at the top level of the artifact.

リポジトリー :menuselection:`Settings --> Pages` を開いて、:guilabel:`Visit
site` ボタンがあればサイトが公開されている。ない場合にはカスタムビルドで公開する
ことにしているということ。後述。

   You can add more pages to your site by creating more new files. Each file
   will be available on your site in the same directory structure as your
   publishing source.

通常のウェブサイトの作り方と同じだ。

   To customize your site even more, you can use Jekyll, a static site generator
   with built-in support for GitHub Pages.

Jekyll を使ったウェブサイトの作成法についてもこの後習得する。

Using custom workflows with GitHub Pages
----------------------------------------------------------------------

   To start using custom workflows you must first enable them for your current
   repository.

..

   GitHub Actions enables the use of GitHub Pages through the configure-pages
   action, which also lets you gather different metadata about a website.

これは聞いたことがない。

.. code:: yaml

   - name: Configure GitHub Pages
     uses: actions/configure-pages@v3

..

   This action helps support deployment from any static site generator to GitHub
   Pages.

もう一つアクションがある。これは圧縮する利点が今のところないので利用しない：

   The ``upload-pages-artifact`` actions enables you to package and upload
   artifacts. The GitHub Pages artifact should be a compressed ``gzip`` archive
   containing a single ``tar`` file.

ファイルを定位置に置くアクションは：

   The ``deploy-pages`` action handles the necessary setup for deploying
   artifacts.

Workflow の書き方を工夫する：

   You can link your ``build`` and ``deploy`` jobs in a single workflow file,
   eliminating the need to create two separate files to get the same result.

ジョブ ``deploy`` で ``needs: build`` としていることに注目する？

Configuring a publishing source for your GitHub Pages site
----------------------------------------------------------------------

ブランチからサイトを掲載する方法は、

#. リポジトリー :menuselection:`Settings --> Pages` を開く。
#. :menuselection:`Build and deployment --> Source` を :guilabel:`Deploy from a
   branch` にする。
#. :guilabel:`Branch` 下のドロップダウンリストから :guilabel:`gh-pages` など目当
   てのブランチを選択する。
#. 原稿ディレクトリーを指定する場合がある。
#. :guilabel:`Save` を押して終わる。

   Commits pushed by a GitHub Actions workflow that uses the ``GITHUB_TOKEN`` do
   not trigger a GitHub Pages build.

逆に感じられるので注意しておく。

   If you choose the :file:`docs` folder on any branch as your publishing
   source, then later remove the :file:`/docs` folder from that branch in your
   repository, your site won't build and you'll get a page build error message
   for a missing :file:`/docs` folder.

これはやったことがない。

   Most external CI workflows "deploy" to GitHub Pages by committing the build
   output to the ``gh-pages`` branch of the repository, and typically include a
   :file:`.nojekyll` file. When this happens, the GitHub Actions workflow will
   detect the state that the branch does not need a build step, and will execute
   only the steps necessary to deploy the site to GitHub Pages servers.

カスタム GitHub Actions でサイトを掲載する方法は、

#. リポジトリー :menuselection:`Settings --> Pages` を開く。
#. :menuselection:`Build and deployment --> Source` を :guilabel:`GitHub Actions` にする。
#. 画面が変わり、初期設定時ならば出来合いの workflow を選択し、動作する workflow
   が自分のところにあればいらない。

カスタム workflow の一般的な構造が記されている。よく覚えておく。

   The starter workflows use a deployment environment called ``github-pages``.
   If your repository does not already include an environment called
   ``github-pages``, the environment will be created automatically.

掲載元になるブランチを保護しておく。

Deleting a GitHub Pages site
----------------------------------------------------------------------

リポジトリー丸ごと削除すればサイトも削除される。リポジトリーを生かしてサイトを削
除する方法： :guilabel:`Source` に :guilabel:`None` を選択する。

サイトは残しておくが掲載処理をやめることは可能だ。別に述べる。

Unpublishing a GitHub Pages site
----------------------------------------------------------------------

さっき述べたように：

   This is different from deleting the site.

リポジトリー :menuselection:`Settings --> Pages` を開いて :guilabel:`Visit site`
ボタン脇の :guilabel:`...` から :guilabel:`Unpublish site` を押す。

明示的に掲載するとサイトも掲載も復活する。

Changing the visibility of your GitHub Pages site
----------------------------------------------------------------------

   Note: To publish a GitHub Pages site privately, your organization must use
   GitHub Enterprise Cloud.

ゆえに割愛。

Creating a custom 404 page for your GitHub Pages site
----------------------------------------------------------------------

掲載元ルートディレクトリーに :file:`404.html` または :file:`404.md` を作成する。
Markdown ならば front matter に次を入れる：

.. code:: markdown

   ---
   permalink: /404.html
   ---

Securing your GitHub Pages site with HTTPS
----------------------------------------------------------------------

   You can enforce HTTPS for your GitHub Pages site to transparently redirect
   all HTTP requests to HTTPS.

これはいい。ぜひ実施しよう。リポジトリー :menuselection:`Settings --> Pages -->
Enforce HTTPS` を押す。

   If you enable HTTPS for your GitHub Pages site but your site's HTML still
   references images, CSS, or JavaScript over HTTP, then your site is serving
   mixed content. Serving mixed content may make your site less secure and cause
   trouble loading assets.

こんな間抜けなことはしていないはずだが、いちおう確認して ``https://`` に置き換え
る。

Using submodules with GitHub Pages
----------------------------------------------------------------------

   You can use submodules with GitHub Pages to include other projects in your
   site's code.

これは何だ？

   If the repository for your GitHub Pages site contains submodules, their
   contents will automatically be pulled in when your site is built.

Git の submodule 機能と深く関係していると思われる。このコマンドを使ったことがな
いので、そこから学ぶ必要がある。

* ただし public リポジトリーのサイトしか指せない。
* 読み取り専用 ``https://`` URL のみを submodules に対して使うこと。これは
  :file:`.gitmodule` で可能。

Troubleshooting 404 errors for GitHub Pages sites
----------------------------------------------------------------------

サイトを掲載したはずなのに 404 エラーが生じる理由と対処法。割愛。

Setting up a GitHub Pages site with Jekyll
======================================================================

About GitHub Pages and Jekyll
----------------------------------------------------------------------

これを読む時点ですでに Jekyll ブログを二つ作成している。

   We recommend using Jekyll with GitHub Pages. If you prefer, you can use other
   static site generators or customize your own build process locally or on
   another server.

どちらを採用する場合でも対応できるようにしておきたい。

ルートに置く :file:`_config.yml` について：

   Some configuration settings cannot be changed for GitHub Pages sites.

それは本書の YAML コードの内容だと思われる。

   GitHub Pages uses plugins that are enabled by default and cannot be disabled:

Jekyll ブログをローカルで確認するときにこれらを持ってくる必要があるか？

   For a list of supported plugins, see "Dependency versions" on the GitHub
   Pages site. For usage information for a specific plugin, see the plugin's
   documentation.

有用なものがあれば取り込みたい。

   GitHub Pages cannot build sites using unsupported plugins. If you want to use
   unsupported plugins, generate your site locally and then push your site's
   static files to GitHub.

その手があったか。

   If you are publishing from a branch, changes to your site are published
   automatically when the changes are merged into your site's publishing source.

動作確認はローカルで Jekyll をインストールしてすればいい。

Creating a GitHub Pages site with Jekyll
----------------------------------------------------------------------

   We recommend using `Bundler <https://bundler.io/>`__ to install and run
   Jekyll. Bundler manages Ruby gem dependencies, reduces Jekyll build errors,
   and prevents environment-related bugs.

ローカルに Ruby をインストールして Bundler をインストールする。前者はすでにシス
テムにあるはず。

掲載元初期状態でのコマンド実行の流れ概要：

.. code:: console

   bash$ mkdir docs
   bash$ cd docs
   bash$ git checkout --orphan gh-pages
   bash$ git rm -rf .
   bash$ jekyll new --skip-bundle .

ファイル :file:`Gemfile` が生成される。これを本書の指示どおり編集する。その後に
コマンド ``bundle install`` を実行してモノをインストールする。これで Jekyll が動
作する環境になった。

Testing your GitHub Pages site locally with Jekyll
----------------------------------------------------------------------

Jekyll がローカルリポジトリーで動作するようになったら、サーバーを稼働させてテス
ト可能となる：

.. code:: console

   bash$ bundle exec jekyll serve

この出力から localhost のアドレスを拾ってブラウザーで開いて、ページを閲覧するこ
とに成功すればよい。

   If the ``github-pages`` gem on your computer is out of date with the
   ``github-pages`` gem on the GitHub Pages server, your site may look different
   when built locally than when published on GitHub.

定期的に（できれば自動で）更新したい：

.. code:: console

   bash$ bundle update github-pages

Adding content to your GitHub Pages site using Jekyll
----------------------------------------------------------------------

通常の Jekyll ブログと同様。コツをまとめておく：

* page と post を区別する
* front matter での設定を気をつける

特に post はファイル名に日付を含めることが必要だ。

Setting a Markdown processor for your GitHub Pages site using Jekyll
----------------------------------------------------------------------

   GitHub Pages supports two Markdown processors: kramdown and GitHub's own
   Markdown processor, which is used to render GitHub Flavored Markdown (GFM)
   throughout GitHub.

Jekyll 設定ファイル :file:`_config.yml` に ``markdown: kramdown`` または
``markdown: GFM`` のいずれかが書ける。後者を採用すれば GitHub 風 Markdown
で書ける。

Adding a theme to your GitHub Pages site using Jekyll
----------------------------------------------------------------------

Jekyll ブログ生成時には :file:`_config.yml` には ``theme: minima``
とある。この値がテーマを指定する。

   To use any other Jekyll theme hosted on GitHub, type
   ``remote_theme: THEME-NAME``, replacing ``THEME-NAME`` with the name of the
   theme as shown in the ``README`` of the theme's repository.

スタイルシートのカスタマイズは次の手順による：

#. ファイル :file:`assets/css/style.scss` を用意する。
#. そこに ``@import "{{ site.theme }}";`` を含む。
#. この行以降にカスタム CSS や Sass を追加する。

HTML レイアウトのカスタマイズは :file:`_layouts` サブディレクトリー以下に適切な
ファイル名でテンプレートを上書きする。これは Jekyll の文書を参照するほうがいい。

About Jekyll build errors for GitHub Pages sites
----------------------------------------------------------------------

   If Jekyll does attempt to build your site and encounters an error, you will
   receive a build error message.

メールで通知が来る。

   We recommend testing your site locally, which allows you to see build error
   messages on the command line, and addressing any build failures before
   pushing changes to GitHub.

この確認方法がもっとも基本だ。

   If you are publishing with a custom GitHub Actions workflow, in order to see
   build error messages in your pull request, you must configure your workflow
   to run on the ``pull_request`` trigger. When you do this, we recommend that
   you skip any deploy steps if the workflow was triggered by the
   ``pull_request`` event.

Pull request をもらうことはないので必要はないのだが、練習しておきたい。

CI でテストするにはコマンド ``bundle exec jekyll build`` を呼び出すように仕掛け
る。

Troubleshooting Jekyll build errors for GitHub Pages sites
----------------------------------------------------------------------

   If Jekyll encounters an error building your GitHub Pages site locally or on
   GitHub, you can use error messages to troubleshoot.

現在では十分訓練されたため、ほとんどエラーを見ない。以下割愛。

Configuring a custom domain for your GitHub Pages site
======================================================================

About custom domains and GitHub Pages
----------------------------------------------------------------------

   GitHub Pages supports using custom domains, or changing the root of your
   site's URL from the default, like ``octocat.github.io``, to any domain you
   own.

既定ドメインで十分。

   GitHub Pages works with two types of domains: subdomains and apex domains.

凡例は本書参照。

   We recommend always using a ``www`` subdomain, even if you also use an apex
   domain. When you create a new site with an apex domain, we automatically
   attempt to secure the ``www`` subdomain for use when serving your site's
   content, but you need to make the DNS changes to use the ``www`` subdomain.

サブドメインは ``www`` が無難だ。カスタムドメインを有効に設定すると：

   For example, if the custom domain for your user site is ``www.octocat.com``,
   and you have a project site with no custom domain configured that is
   published from a repository called ``octo-project``, the GitHub Pages site
   for that repository will be available at ``www.octocat.com/octo-project``.

サブドメインについて詳しく：

   Subdomains are configured with a ``CNAME`` record through your DNS provider.

..

   ``www`` subdomains are the most stable type of custom domain because ``www``
   subdomains are not affected by changes to the IP addresses of GitHub's
   servers.

カスタムサブドメイン：

   For example, you can create a site called ``blog.example.com`` and customize
   that section independently from ``www.example.com``.

サブドメインを含まないドメインもよく見かける：

   An apex domain is configured with an ``A``, ``ALIAS``, or ``ANAME`` record
   through your DNS provider.

..

   If you configure the correct records for each domain type through your DNS
   provider, GitHub Pages will automatically create redirects between the
   domains. For example, if you configure ``www.example.com`` as the custom
   domain for your site, and you have GitHub Pages DNS records set up for the
   apex and ``www`` domains, then ``example.com`` will redirect to
   ``www.example.com``.

乗っ取りに注意：

   If your GitHub Pages site is disabled but has a custom domain set up, it is
   at risk of a domain takeover.

..

   There are a couple of reasons your site might be automatically disabled.

Managing a custom domain for your GitHub Pages site
----------------------------------------------------------------------

   Make sure you add your custom domain to your GitHub Pages site before
   configuring your custom domain with your DNS provider.

先に GitHub で設定する。

リポジトリー :menuselection:`Settings --> Pages --> Custom domain` で適当に入力
して :guilabel:`Save` を押す。ここで次のことが起こる：

   If you are publishing your site from a branch, this will create a commit that
   adds a ``CNAME`` file to the root of your source branch. If you are
   publishing your site with a custom GitHub Actions workflow, no ``CNAME`` file
   is created.

一人プロジェクトのときにはローカルリポジトリーで ``git pull`` しておくのを忘れな
いようにする。

次に DNS provider に移動して ``CNAME`` レコードを作成する。詳細不明。最後にコン
ソールからコマンド :command:`dig` で確認する。

.. code:: console

   bash$ dig WWW.EXAMPLE.COM +nostats +nocomments +nocmd

カスタムドメインを削除する場合は :guilabel:`Save` ではなく :guilabel:`Remove` を
押す。

Verifying your custom domain for GitHub Pages
----------------------------------------------------------------------

   Verifying your domain stops other GitHub users from taking over your custom
   domain and using it to publish their own GitHub Pages site.

時間がかかる：

   If you are verifying a domain you own, which is currently in use by another
   user or organization, to make it available for your GitHub Pages website;
   note that the process to release the domain from its current location will
   take 7 days to complete.

.. admonition:: 読者ノート

   現在実施不可能

Troubleshooting custom domains and GitHub Pages
----------------------------------------------------------------------

.. admonition:: 読者ノート

   現在実施不可能
