======================================================================
Get started with GitHub documentation ノート
======================================================================

`Get started with GitHub documentation <https://docs.github.com/en/get-started>`__
をよく読もう。他の章はここまで網羅的に目を通さないようにしたい。

.. contents::

Quickstart
======================================================================

    Get started using GitHub to manage Git repositories and collaborate with
    others.

後者にはほとんど興味がなく、前者を極めたい。

Hello World
----------------------------------------------------------------------

    This tutorial teaches you GitHub essentials like repositories, branches,
    commits, and pull requests. You'll create your own Hello World repository
    and learn GitHub's pull request workflow, a popular way to create and review
    code.

すでにリポジトリーを何個も何個も持っている利用者は読み飛ばし可だと思うが、油断し
てはいけない。

    To complete this tutorial, you need a GitHub account and Internet access.

* 画面右上の :guilabel:`New Repository`
* «By default, your repository has one branch named ``main`` that is considered
  to be the definitive branch.»
* :guilabel:`Repository` 画面の :guilabel:`Create branch`

こんな感じでブラウザーごしで Git 操作を続けていくチュートリアルだ。この後は
pull request を生じてマージする流れになる。

Set up Git
----------------------------------------------------------------------

この記事で注目すべきは Authenticating with GitHub from Git か。

HTTPS か SSH か。HTTPS を推奨している。

    If you clone with SSH, you must generate SSH keys on each computer you use
    to push or pull from GitHub.

Create a repo
----------------------------------------------------------------------

    In the command line, navigate to the directory where you would like to
    create a local clone of your new project.

GitHub CLI を使ってリポジトリーを「直接」生成する方法を述べている。

    To create a repository for your project, use the ``gh repo create``
    subcommand. When prompted, select :guilabel:`Create a new repository` on
    GitHub from scratch and enter the name of your new project. If you want your
    project to belong to an organization instead of to your personal account,
    specify the organization name and project name with
    ``organization-name/project-name``.

実際には GitHub に新規リポジトリーをコンソールでいきなり作成することはない。
一度だけ試したらもうやらないだろう。

    Follow the interactive prompts. To clone the repository locally, confirm yes
    when asked if you would like to clone the remote project directory.

対話的に操作するのだが、Python コードで書かれている処理に興味がわく。

    Alternatively, to skip the prompts supply the repository name and a
    visibility flag (``--public``, ``--private``, or ``--internal``). For
    example, ``gh repo create project-name --public``. To clone the repository
    locally, pass the ``--clone`` flag.

通常の Git 操作コマンドについてはノートを割愛。以下同様。

Fork a repo
----------------------------------------------------------------------

GitHub では fork と pull request はセットで行う。

.. code:: console

   bash$ gh repo fork REPOSITORY
   bash$ gh repo fork REPOSITORY --clone=true

..

    When you fork a project in order to propose changes to the upstream
    repository, you can configure Git to pull changes from the upstream repository
    into the local clone of your fork.

これをやらないとオリジナルに対して中身がどんどんかけ離れていく。

.. code:: console

   bash$ gh repo fork REPOSITORY --remote=true

* Creating branches
* Opening pull requests

フォーク後に Git 操作で「川上」を設定することになる。

    You have now forked a repository, practiced cloning your fork, and
    configured an upstream repository.

GitHub flow
----------------------------------------------------------------------

    GitHub flow is a lightweight, branch-based workflow. The GitHub flow is
    useful for everyone, not just developers.

重要度がわからない。

    Ideally, each commit contains an isolated, complete change. This makes it
    easy to revert your changes if you decide to take a different approach.

バージョン管理の基本だ。

    Make a separate branch for each set of unrelated changes

これも基本だ。

    Pull request review is so valuable that some repositories require an
    approving review before pull requests can be merged.

厳しい管理をしているプロジェクトではそうだろう。

    If you link with a keyword, the issue will close automatically when the pull
    request merges.

これは後ほどやる。

    If your repository has checks configured to run on pull requests, you will
    see any checks that failed on your pull request.

これも後ほどやる。

    Branch protection settings may block merging if your pull request does not
    meet certain requirements.

これも後ほど。何の規則も追加せずに保護するということも可能。

Contributing to projects
----------------------------------------------------------------------

フォークに関する話題を見ていく。

    If you want to contribute to someone else's project but don't have write
    access to the repository, you can use a "fork and pull request" workflow.

これが contribution の基本。

フォークすなわち新しいリポジトリー。フォークはクローンありとなしがある。クローン
はローカルにリポジトリーを作る。

.. code:: console

   bash$ gh repo fork REPOSITORY --clone=true

次の一文は GitHub Discussions を読んでから考える：

    Pull Requests are an area for discussion.

Be social
----------------------------------------------------------------------

人、リポジトリー、組織が対象となる。

    When you follow someone on GitHub, you will get notifications on your personal
    dashboard about their public activity.

フォローの意味を知る。

    To follow someone, click :guilabel:`Follow` on a person's profile page.

フォロー方法はこれしかないか？

リポジトリーの上部にある :guilabel:`Watch` を押すと、そのリポジトリーを次の意味
で追うことができる：

    When the owner updates the repository, you will see the changes in your
    personal dashboard.

GitHub というと Git リポジトリー集積場という印象があったが、共同作業のための道具
を備える場でもある：

    GitHub provides built-in collaborative communication tools, allowing you to
    interact closely with your community when building great software.

* Pull request
* Issues
* Discussions

自分が所属している組織は :guilabel:`Your organizations` で確認する：

    From your dashboard, click the drop down menu of your username on the left
    side of your dashboard.

組織をフォローすると何が起こるか：

    When you follow organizations on GitHub, you'll see their public activity on
    your personal dashboard.

組織をフォローする方法：

    To follow an organization, in the header of the organization's page, click
    :guilabel:`Follow`.

星の意味とはブックマークだ：

    You can star interesting projects to make them easy to find again later.

Communicating on GitHub
----------------------------------------------------------------------

* GitHub Issues: often referred to as GitHub's bug-tracking system.
* Pull requests: allow you to propose specific changes.
* GitHub Discussions: often do not result in an actionable task.

今のところ Discussions に馴染みがない。

GitHub glossary
----------------------------------------------------------------------

用語集。

* access token
* authentication code
* CA certificate
* code frequency graph: ユーザー概要ページの下に出てくるカレンダーのことか？
* contributor: collaborator ではない
* deploy key
* enterprise account: こういう enterprise は企業の意。
* fenced code block: いつも書くコードブロック記法についている名前はこれだ。
* identicon
* key fingerprint
* Linguist: こんな便利なものが。
* OAuth app
* OAuth token
* punch graph
* recovery code
* single sign-on: SSO
* SSH key: いい説明なのだろうが、まだ理解しない。
* star: ブックマークの他にも、感謝の意という側面もある。
* watch: リポジトリーだけでなく issue も watch 可能。

Git cheatsheet
----------------------------------------------------------------------

これは自作した。

Learning resources
----------------------------------------------------------------------

これらの資料を見るのはこの文書をクリアしてからだ。

* `GitHub Skills <https://skills.github.com/>`__

Onboarding
======================================================================

Getting started with your GitHub account
----------------------------------------------------------------------

この記事は重要。

    With a personal account on GitHub, you can import or create repositories,
    collaborate with others, and connect with the GitHub community.

* Part 1 Configuring your GitHub account

  * 個人アカウントを生成したら二段階認証の活性化まで突き進め。
  * パスワードを十分強くしろ。
  * GitHub Free でいい。
  * メールアドレスをまともにしろ。
  * 二段階認証でパスキーを指定したい。
  * プロフィール画面と貢献を確認しろ。

* Part 2 Using GitHub's tools and processes

  * Git をまともに利用できるようになり、ローカル設定をまともにしろ。
  * GitHub とやり取りする方法を決めろ。

    * ブラウザー
    * GitHub Desktop
    * IDE or text editor: VS Code など
    * GitHub CLI
    * GitHub API
    * 生の Git
  * Markdown: GitHub で書き物をするときはこの書法を使う。
  * 検索。検索範囲と検索語が急所。
  * ファイル閲覧。GitHub ではリポジトリー内のファイルを操作することが可能。
* Part 3 Collaborating on GitHub

  * リポジトリーは作成・複製・フォークするものだ。
  * GitHub の外部からプロジェクトを輸入することが可能。
  * リポジトリー所有者はそれを完全に制御することが可能。
  * リポジトリーを所有者が設定、管理する。
  * 協力者に向けて環境を整える。
  * GitHub Issues や pull requests でプロジェクト進行を管理する。
  * 通知をやりくりする。
  * GitHub Pages を利用して GitHub に置いたリポジトリーを基にウェブサイトを直接
    生成する。

    * GitHub Pages は重要。
  * GitHub Discussions を利用して共同体を形成しやすくする。
* Part 4 Customizing and automating your work on GitHub

  * ここが全然わかっていない。
  * GitHub Marketplace: 機能を追加してワークフローを改善する統合機能がある。
    無料・有料のツールを検索、閲覧、インストール可能：

    * GitHub Apps
    * OAuth ソフト
    * GitHub Actions
  * GitHub API

    * REST API or GraphQL API
    * 一般的な作業を自動化
    * データをバックアップ
    * GitHub を拡張する統合機能を作成
  * GitHub Actions

    * GitHub の開発ワークフローを GitHub上で自動化・カスタマイズする。
    * 独自のアクションを作成可能
    * 共同体で共有されているアクションを使用・カスタマイズ可能
  * GitHub Packages: GitHub Packages is a software package hosting service that
    allows you to host your software packages privately or publicly and use
    packages as dependencies in your projects.
* Part 5 Building securely on GitHub

  * 安全保障機能の選択肢はリポジトリーによって異なる。
  * リポジトリーを保護する

    * リポジトリー安全保障設定を行うことで保護することが可能。

      * アクセス管理
      * 安全保障政策の設定
      * 依存関係の管理
      * など
    * 公開リポジトリーではコードとスキャンを設定して脆弱性を自動的に特定し、トー
      クンと鍵が公開されないようにすることも可能。
  * プロジェクトの外部依存関係も安全保障範囲となる。
* Part 6 Participating in GitHub's community

  * オープンソースプロジェクトに貢献する。
  * GitHub Community Support とやり取りする。
  * GitHub Docs を読み込む。
  * GitHub Skills を履修する。これはやるつもり。
  * GitHub Sponsors を介してプロジェクトを金銭的に支援する。

Getting started with GitHub Team
----------------------------------------------------------------------

GitHub Team: 組織アカウントで複数人が同時に複数プロジェクトで共同作業を行う。

* Part 1: Configuring your account on GitHub.com

  * 組織を作って請求を設ける。組織については別途。
  * 請求設定の管理
  * 組織の請求設定にアクセスまたは変更できるのは、所有者または請求支配人の役割の
    組織構成員のみ。
* Part 2: Adding members and setting up teams

  * 組織を作ってから構成員を集める。権限、役割を付与する。離脱や復帰も可。
  * 組織構成員の集合を team と呼んでいる。入れ子可能。
  * 団体に対しても設定の考え方がある。
  * «You can give organization members, teams, and outside collaborators
    different levels of access to repositories owned by your organization with
    repository roles.» とは？
* Part 3: Managing security for your organization

  * 構成員に対する安全保障設定？
  * 組織の安全保障のためのさまざまな安全保障機能

    * «security policies, dependency graphs, secret scanning and Dependabot
      security and version updates»
  * 組織の監査ログ
* Part 4: Setting organization level policies

  * 組織内の行動、機能に対する権限、施策を定める。
  * 例：組織内リポジトリーの作成を禁止する。
  * リポジトリーに対する権限を定める。
  * リポジトリーの public/private を定める。
  * :file:`CONTRIBUTING.md`, :file:`CODE_OF_CONDUCT.md` などを作成する。
* Part 5: Customizing and automating your work on GitHub

  * 作業を自動化したりカスタマイズしたりすることが可能。
  * GitHub Marketplace を使う。
  * GitHub API を使う。
  * GitHub Actions を使う。これがいちばん自動化、カスタマイズの実現に近いか。
  * GitHub Packages を使う。ソフトパッケージ配布場所サービス。
* Part 6: Participating in GitHub's community

  * オープンソースプロジェクトに貢献する。見つける方法はどこかに述べられていた。
  * GitHub Community Support とやり取りする。
  * GitHub Docs を読み込む。
  * GitHub Skills を履修する。これはやるつもり。
  * GitHub Sponsors を介してプロジェクトを金銭的に支援する。
  * GitHub Support とやり取りする。

Getting started with GitHub Enterprise Cloud
----------------------------------------------------------------------

GitHub Enterprise Cloud は企業アカウントのための枠組だ。割愛。

Learning about GitHub
======================================================================

開発過程を改善し、他人とともに働こうではないか。

GitHub's plans
----------------------------------------------------------------------

料金プランの概要。

* About GitHub's plans

  * 無料と有料がある。GitHub Pricing で一覧できる。
* GitHub Free for personal accounts

  * 個人アカウント向け
  * パブリックリポジトリーは全機能搭載かつ無制限
  * プライベートリポジトリーは機能制限付きかつ無制限
  * 共同作業者も無制限
  * 詳細は本文参照。
* GitHub Pro

  * GitHub Free の上位プラン
* GitHub Free for organizations

  * GitHub Free for personal accounts のやや上位プラン
* GitHub Team

  * GitHub Free for organizations のやや上位プラン
* GitHub Enterprise

  * 企業向けプラン

GitHub Actions の利用はおおむね無料。

Docs versions
----------------------------------------------------------------------

この文書群のページ上部のドロップダウンリストから :guilabel:`Free, Pro & Team` を
選択する。現在のプランはページ URL を確認したり、ページ見出しをを確認すればい
い。

* URL が ``https://github.com`` から始まっていればフリー系。
* GitHub トレードマークのすぐ横にテキストがなければフリー系。

GitHub language support
----------------------------------------------------------------------

GitHub 機能でサポートされているプログラミング言語の概要。GitHub が知っているどの
言語でも、コードを検索したり構文強調を効かせたりすることが可能。

中核言語は C, C++, C#, Go, Java, JavaScript, PHP, Python, Ruby, Scala,
TypeScript.

Types of GitHub accounts
----------------------------------------------------------------------

* Personal accounts

  * Your personal account can own resources such as repositories, packages, and
    projects. Any time you take any action on GitHub.com, such as creating an
    issue or reviewing a pull request, the action is attributed to your personal
    account.
* Organization accounts

  * 組織は無制限に多くの人が一度に多くのプロジェクトで一緒に働ける共有アカウントだ。
* Enterprise accounts

マシンユーザーなる概念があるようだ。

Access permissions
----------------------------------------------------------------------

    A permission is the ability to perform a specific action. For example, the
    ability to delete an issue is a permission. A role is a set of permissions
    you can assign to individuals or teams.

GitHub Advanced Security
----------------------------------------------------------------------

    Some features of GitHub Advanced Security are also available for public
    repositories on GitHub.com

GitHub Advanced Security を利用するにはライセンス料金が必要。ライセンスに対応す
る機能は次の三つ：

* Code scanning
* Secret scanning
* Dependency review

しかし、無料リポジトリーでも公開ならば利用可能。

Changes to GitHub plans
----------------------------------------------------------------------

    As of April 14, 2020, GitHub announced that all of the core GitHub features
    are now free for everyone.

プランをダウングレードすることも可能。関係ないが。

Signing up for GitHub
======================================================================

Sign up for a new GitHub account
----------------------------------------------------------------------

新しい personal account を作成するならばサインアウトしてから。価格設定ページにア
クセスして、所望の項目の upgrade ボタンを押す。

Verify your email address
----------------------------------------------------------------------

主要メールアドレスの設定を堅実にしておく。メールアドレスがいい加減だと不可能なア
クションが多い。

* Create or fork repositories
* Create issues or pull requests
* Comment on issues, pull requests, or commits
* Authorize OAuth app applications
* Generate personal access tokens
* Receive email notifications
* Star repositories
* Create or update project boards, including adding cards
* Create or update gists
* Create or use GitHub Actions
* Sponsor developers with GitHub Sponsors
* Accept organization invitations

次が重要だった：

    If you'd like to keep your email address private, you can use a
    GitHub-provided ``noreply`` email address.

:menuselection:`Settings --> Emails --> Resend verification email`

Enterprise Cloud trial
----------------------------------------------------------------------

割愛。

Enterprise Server trial
----------------------------------------------------------------------

割愛。

Using GitHub
======================================================================

Feature preview
----------------------------------------------------------------------

画面右上から :guilabel:`Feature preview` を押すとメニューが現れる。

Supported browsers
----------------------------------------------------------------------

次のブラウザーの最新版は必ず使える：

* Apple Safari
* Google Chrome
* Microsoft Edge
* Mozilla Firefox

GitHub CLI
----------------------------------------------------------------------

    GitHub CLI is a command-line tool that brings pull requests, issues, GitHub
    Actions, and other GitHub features to your terminal, so you can do all your
    work in one place.

これを使いこなせるようになる。後ほど詳しく。

GitHub Desktop
----------------------------------------------------------------------

これは未知。導入するかしないか決めない。WSL に作ったローカルリポジトリーをまとも
に取り扱ってくれるというのならば動けるようにしておいて損はないのだが。

GitHub Mobile
----------------------------------------------------------------------

    GitHub Mobile is available as an Android and iOS app.

これはやるか。認証の学習にもなる。

ちょっとした機能的制限があるようだ。

    If you configure the language on your device to a supported language, GitHub
    Mobile will default to the language. You can change the language for GitHub
    Mobile in GitHub Mobile's :guilabel:`Settings` menu.

日本語が支援されているので、英語に設定するには明示的に手動で。

Keyboard shortcuts
----------------------------------------------------------------------

    Typing :kbd:`?` on GitHub brings up a dialog box that lists the keyboard
    shortcuts available for that page.

なるほど。これは便利だ。

GitHub Command Palette
----------------------------------------------------------------------

* About the GitHub Command Palette

  * コマンドパレットは候補が最適化されて出現する。
* Opening the GitHub Command Palette

  * まず :guilabel:`Feature preview` で :guilabel:`Enable` する。
  * :kbd:`Ctrl` + :kbd:`K` でパレットが出現。

* Navigating with the GitHub Command Palette

  * :kbd:`Tab`, :kbd:`Ctrl`, :kbd:`Del`, :kbd:`BackSpace` を活用する。
  * :kbd:`Enter` で確定。:kbd:`Ctrl` + :kbd:`Enter` でブラウザーのタブを追加して
    開く。

* Searching with the GitHub Command Palette

  * :kbd:`#` Search for issues, pull requests, discussions, and projects
  * :kbd:`!` Search for projects
  * :kbd:`@` Search for users, organizations, and repositories
  * :kbd:`/` Search for files within a repository scope

* Running commands from the GitHub Command Palette

  * :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`K` で入力欄に ``>`` の付いたパレットが出
    現。
* Closing the command palette

  * :kbd:`Esc` がよい。
* GitHub Command Palette reference

  * いいコマンドがあまりない。

Allow network access
----------------------------------------------------------------------

関係ない。

Connectivity problems
----------------------------------------------------------------------

これも関係ない。

Writing on GitHub
======================================================================

この節が長い。

Start writing on GitHub
----------------------------------------------------------------------

Quickstart for writing on GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Learn advanced formatting features by creating a :file:`README` for your
    GitHub profile.

* Introduction

  * Markdown で書く。
* Creating or editing your profile README

  * If you don't already have a profile README, you can add one.
  * アカウント名と同名のリポジトリーを作成する。その README を編集する。
* Adding an image to suit your visitors

  * HTML に ``picture`` というタグがあるのか。
* Adding a table
* Adding a collapsed section

  * HTML に ``details`` というタグがあるのか。
* Adding a quote
* Adding a comment
* Saving your work

  * 当然だが ``main`` ブランチのファイルが画面に反映する。

About writing and formatting on GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GitHub の Markdown は標準のそれとは少し異なる。

    Every comment field on GitHub contains a text formatting toolbar, which
    allows you to format your text without learning Markdown syntax.

:menuselection:`Settings --> Appearance --> Use a fixed-width (monospace) font
when editing Markdown`

Basic writing and formatting syntax
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

文書内に見出しを深く設けると TOC を用意してくれる。

``pitcure`` タグの詳細な使用法。

Alerts は使いたくなる。

Work with advanced formatting
----------------------------------------------------------------------

Organizing information with tables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* 表の記法
* 表のマス内の記法
* 文字寄せ

Organizing information with collapsed sections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``details`` タグで折りたたみ区画を作れば Markdown を効率化できる。これは HTML5
標準のタグだが、この中身として Markdown コードを混入させることが可能。

Creating and highlighting code blocks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

構文強調機能はさすがにすでに利用している。

    You can also use code blocks to create diagrams in Markdown. GitHub supports
    Mermaid, GeoJSON, TopoJSON, and ASCII STL syntax.

Creating diagrams
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* About creating diagrams

  * Diagram rendering is available in GitHub Issues, GitHub Discussions, pull
    requests, wikis, and Markdown files.
* Creating Mermaid diagrams

  * すでに利用済み。
* Creating GeoJSON and TopoJSON maps

  * You can use GeoJSON or TopoJSON syntax to create interactive maps.
  * ここで言う maps は地図のこと。
* Creating STL 3D models

  * なんと……。GitHub は何を考えているのだ。

Writing mathematical expressions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* About writing mathematical expressions

  * Markdown 内の LaTeX コードの描画には MathJax を利用している。Jekyll ブログの
    既定エンジンとは異なる。
* Writing inline expressions

  * ドルマークで挟む方式と、ドルマークとバッククオートをくっつけたパターン同士で
    挟む方式がある。後者は開始記号と終了記号が見分けられるので好みだ。ただし
    GitHub による拡張。
* Writing expressions as blocks

  * ダブルドルマークで挟む方式
  * コードブロックで構文を ``math`` とする方式（これも GitHub 固有）
* Writing dollar signs in line with and within mathematical expressions

  * 常識的な方法でエスケープ可能。

Autolinked references and URLs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    References to URLs, issues, pull requests, and commits are automatically
    shortened and converted into links.

* URLs: これはわかりやすい。
* Issues and pull requests: Short link というルールがある。
* Labels

  * When referencing the URL of a label in Markdown, the label is automatically
    rendered.
* Commit SHAs

  * References to a commit's SHA hash are automatically converted into shortened
    links to the commit on GitHub.
* Custom autolinks to external resources

  * If custom autolink references are configured for a repository, then
    references to external resources, like a JIRA issue or Zendesk ticket,
    convert into shortened links. なるほど。

Attaching files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    To attach a file to an issue or pull request conversation, drag and drop it
    into the comment box. Alternatively, you can click the bar at the bottom of
    the comment box to browse, select, and add a file from your computer.

GitHub 上のページにファイルを添付できることになるが、そのわりに上限が 10MB もあ
る。

MP4 に関する次のコツは有益だ：

    Note: Video codec compatibility is browser specific, and it's possible that
    a video you upload to one browser is not viewable on another browser. At the
    moment we recommend using h.264 for greatest compatibility.

About task lists
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    You can use task lists to break the work for an issue or pull request into
    smaller tasks, then track the full set of work to completion.

ほう。

    You can use Markdown to create a task list in any comment on GitHub. If you
    reference an issue, pull request, or discussion in a task list, the
    reference will unfurl to show the title and state.

このリストの項目を issue に変換することが可能。要するに issue や pull request を
細分するための機能だ。

Creating a permanent link to a code snippet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    You can create a permanent link to a specific line or range of lines of code
    in a specific version of a file or pull request.

* Linking to code: コード中のテキストを選択して、行表示部分にマウスを持っていく
  と :guilabel:`...` が現れる。メニューにある :guilabel:`Copy permalink` を押
  す。
* Linking to Markdown: URL の仕様

Using keywords in issues and pull requests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    To link a pull request to an issue to show that a fix is in progress and to
    automatically close the issue when someone merges the pull request, type one
    of the following keywords followed by a reference to the issue.

    * close
    * closes
    * closed
    * fix
    * fixes
    * fixed
    * resolve
    * resolves
    * resolved

魔法の言葉がもう一種類ある：

    To mark an issue or pull request as a duplicate, type "Duplicate of"
    followed by the issue or pull request number it duplicates in the body of a
    new comment.

Work with saved replies
----------------------------------------------------------------------

    To save time and make sure you're delivering a consistent message, you can
    add saved replies to issue and pull request comments.

嫌いな機能だ。

About saved replies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Saved replies are tied to your personal account. Once they're created, you'll
    be able to use them across repositories and organizations.

Creating a saved reply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:menuselection:`Settings --> Saved replies`.

このフォームを見れば機能のすべてを了解するだろう。

Editing a saved reply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

割愛。

Deleting a saved reply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

バツボタン。

Using saved replies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コメント欄のツールバーに呼び出しボタンがある。

Share content with gists
----------------------------------------------------------------------

Creating gists
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

これだけ注意：

    Secret gists aren't private. If you send the URL of a secret gist to a
    friend, they'll be able to see it.

Gist のファイルをページに埋め込むことが可能：

    To embed a specific gist file, append the Embed URL with ``?file=FILENAME``.

* Creating a gist: 方法が複数ある。

  * ``gh gist create``
  * Gist のホームページから作成

Forking and cloning gists
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gist ページはリポジトリーの一種なので、フォークも複製も考えられる。ドロップダウ
ンメニューを見ればやり方はわかるだろう。

Saving gists with stars
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gist ページに対してもリポジトリー同様に星をつけることが可能。行動の意味も同じ。

Explore projects
======================================================================

Contribute to open source
----------------------------------------------------------------------

自分に関連するオープンソースプロジェクトに貢献する方法を見つける。

* Discovering relevant projects

  * ``https://github.com/topics/<topic>`` にアクセス
  * Explore GitHub
  * メールマガジン
* Finding good first issues

  * ``github.com/<owner>/<repository>/contribute`` で初心者用
* Opening an issue

  * バグを見つけたと思ったら、すでに報告済みでないかを確認しろ。
* Validating an issue or pull request

  * 報告されているバグを再現したり、テストするのも貢献の一形態だ。

Save repos with stars
----------------------------------------------------------------------

星の機能については GitHub ユーザーは文書を読む前に慣れていると思う。

Following people
----------------------------------------------------------------------

* About followers on GitHub

  * 誰かを follow すると、ダッシュボードにその行動が示される。
  * その人物がリポジトリーに星をつけると、それがおすすめとして示される。
* Following a user on GitHub

  * 対象のプロフィール画面の :guilabel:`Follow` をクリック
* Unfollowing a user on GitHub

  * 対象のプロフィール画面の :guilabel:`Unfollow` をクリック

Following organizations
----------------------------------------------------------------------

組織版。

Getting started with Git
======================================================================

ここは Git の基本だろう。GitHub との連携に注目する。

Set your username
----------------------------------------------------------------------

.. code:: console

   bash$ git config --global user.name XXXXXXX

リポジトリー単位で設定するには、当該リポジトリーの :file:`gitconfig` にコマンド
を作用させる。

Caching credentials
----------------------------------------------------------------------

    If you're cloning GitHub repositories using HTTPS, we recommend you use
    GitHub CLI or Git Credential Manager (GCM) to remember your credentials.

SSH でやっているから流し読みか？

    GitHub CLI will automatically store your Git credentials for you when you
    choose HTTPS as your preferred protocol for Git operations and answer "yes"
    to the prompt asking if you would like to authenticate to Git with your
    GitHub credentials.

コマンド ``gh auth login`` を実行する。

    With GCM, you don't have to manually create and store a personal access
    token, as GCM manages authentication on your behalf, including 2FA
    (two-factor authentication).

GCM をインストールするのが必要。後で詳しく。

リポジトリーを HTTPS でクローンした場合にこのような認証が発生する。

    Once you've authenticated successfully, your credentials are stored on your
    system and will be used every time you clone an HTTPS URL. Git will not
    require you to type your credentials in the command line again unless you
    change your credentials.

Git passwords
----------------------------------------------------------------------

逆に、GitHub にアクセスするたびにユーザー名とパスワードの入力を求められる場合は、
クローン URL を HTTPS にしているということだ。

    However, it also prompts you to enter your GitHub credentials every time you
    pull or push a repository.

入力を省略するようにするには：

    You can avoid being prompted for your password by configuring Git to cache
    your credentials for you. Once you've configured credential caching, Git
    automatically uses your cached personal access token when you pull or push a
    repository using HTTPS.

macOS Keychain credentials
----------------------------------------------------------------------

Mac は使っていないので割愛。

Git workflows
----------------------------------------------------------------------

この節には情報がない。後で。

About remote repositories
----------------------------------------------------------------------

所有者をまたぐリポジトリーの操作についてか。

* About remote repositories

  * 次のタイプの URL にしか push 不能：

    * An HTTPS URL like ``https://github.com/user/repo.git``
    * An SSH URL, like ``git@github.com:user/repo.git``
  * Git はリモート URL に名前を付ける。通常 ``origin`` だ。
* Creating remote repositories

  * ``git remote add origin <REMOTE_URL>``
  * ``git remote set-url XXXXXXX``
* Choosing a URL for your remote repository

  * クローンのためのコマンドはリポジトリー画面の :menuselection:`Code --> Clone`
    で得る。
* Cloning with HTTPS URLs

  * HTTP はプロキシーやファイアーウォールを通る。
  * 次の Git コマンドでユーザー名とパスワード入力を要求される：
    ``clone``, ``fetch``, ``pull``, ``push``.
  * To clone a repository without authenticating to GitHub on the command line,
    you can use GitHub Desktop to clone instead. For more information, see
    "Cloning a repository from GitHub to GitHub Desktop."
* Cloning with SSH URLs

  * To use these URLs, you must generate an SSH keypair on your computer and add
    the public key to your account on GitHub.com.
  * 次の Git コマンドでパスワードと SSH キーパスフレーズ入力を要求される：
    ``clone``, ``fetch``, ``pull``, ``push``.
* Cloning with GitHub CLI: 別途述べる。
* Cloning with Subversion: 割愛。

Manage remote repositories
----------------------------------------------------------------------

* Adding a remote repository

  * ローカルリポジトリーにリモートリポジトリーを追加する方法だ。
  * 先述のように ``git remote add origin
    https://github.com/OWNER/REPOSITORY.git`` だ。
* Changing a remote repository's URL

  * ``git remote set-url origin https://github.com/OWNER/REPOSITORY.git``
  * 記録し忘れていたが Password-based authentication for Git has been removed in
    favor of more secure authentication methods.
  * HTTPS から SSH に変えたいときなどに実行。
* Renaming a remote repository

  * ``git remote rename OLD NEW`` を実行。
* Removing a remote repository

  * ``git remote rm NAME`` を実行。Git の各種コマンドで名前 ``NAME`` が使えなく
    なる。

Associate text editors
----------------------------------------------------------------------

.. code:: console

   bash$ git config --global core.editor "code --wait"

Handle line endings
----------------------------------------------------------------------

* ``git config --global core.autocrlf``
* ファイル :file:`.gitattributes` で ``text eol=lf`` とするのが望みなのだが、最
  良ではないようだ。

..

    After you set the core.autocrlf option or commit a :file:`.gitattributes`
    file, Git automatically changes line endings to match your new
    configuration. You may find that Git reports changes to files that you have
    not modified.

これは知らなんだ。

Ignoring files
----------------------------------------------------------------------

    GitHub maintains an official list of recommended :file:`.gitignore` files
    for many popular operating systems, environments, and languages in the
    "github/gitignore" public repository.

これを参考にして自分のリポジトリーの :file:`.gitignore` を編成するといい。

    To always ignore a certain file or directory, add it to a file named ignore
    that's located inside the directory :file:`~/.config/git`. By default, Git
    will ignore any files and directories that are listed in the global
    configuration file :file:`~/.config/git/ignore`.

これは設置済みだった。

無視したいファイルパターンを :file:`.gitignore` に書けない場合は：

    Use your favorite text editor to open the file called
    :file:`.git/info/exclude` within the root of your Git repository. Any rule
    you add here will not be checked in, and will only ignore files for your
    local repository.

Using Git
======================================================================

About Git
----------------------------------------------------------------------

    GitHub hosts Git repositories and provides developers with tools to ship
    better code through command line features, issues (threaded discussions),
    pull requests, code review, or the use of a collection of free and
    for-purchase apps in the GitHub Marketplace.

Push commits to a remote
----------------------------------------------------------------------

.. code:: console

   bash$ git push REMOTE-NAME :BRANCH-NAME

このコマンドがなぜリモートのブランチを削除することになるのか、仕組みを理解するといい。

フォークしたリポジトリーのリモートリポジトリーは、ローカルから見ると複数ある。

Get changes from a remote
----------------------------------------------------------------------

* ``git clone`` については先述のとおり。
* ``git fetch`` はマージなしで追跡先の各種ブランチ、タグを得る。
* ``git merge`` では通常、リモート追跡ブランチをローカルブランチにマージする。
  ``git merge REMOTE-NAME/BRANCH-NAME``.
* 練習だと思って ``git pull`` は使わないという手もある。

  * 失敗したら ``git merge --abort`` を実行する。

Non-fast-forward error
----------------------------------------------------------------------

個人でやっていれば出ないエラーだが、対処法は知っておく必要がある。

.. code:: console

   bash$ git fetch origin
   bash$ git merge origin YOUR_BRANCH_NAME

もちろん ``git pull`` を使っても可。

Splitting a subfolder
----------------------------------------------------------------------

    You can turn a folder within a Git repository into a brand new repository.

この手法は何かのときに使うかもしれないので読む。

    However, note that the new repository won't have the branches and tags of
    the original repository.

.. code:: console

   bash$ git clone https://github.com/USERNAME/REPOSITORY-NAME
   bash$ cd REPOSITORY-NAME
   bash$ git filter-repo --path FOLDER-NAME/

ここでは ``FOLDER-NAME`` 以下を残したい。

About Git subtree merges
----------------------------------------------------------------------

    If you need to manage multiple projects within a single repository, you can
    use a subtree merge to handle all the references.

これは聞いたことがない。

この記事のコマンドをまねて理解することは可能。ポイントは：

.. code:: console

   bash$ git merge -s ours --no-commit --allow-unrelated-histories spoon-knife/main
   bash$ git read-tree --prefix=spoon-knife/ -u spoon-knife/main
   bash$ git pull -s subtree spoon-knife main

About Git rebase
----------------------------------------------------------------------

``git rebase -i`` の基本が述べられている。

Git rebase
----------------------------------------------------------------------

``git rebase`` 後のブランチを ``git push`` するにはオプションが必要。
``--force`` はよく使うが ``--force-with-lease`` は知らなんだ。

Resolve conflicts after rebase
----------------------------------------------------------------------

マージが衝突した場合の、ごく一般的な対処方法だ。これらの技法はよそのリポジトリー
を研究するときによく使うはずだ。

Special characters in names
----------------------------------------------------------------------

    If possible, create branch and tag names that don't contain special
    characters, as these would need to be escaped.

..

    GitHub restricts a small number of branch and tag names from being pushed
    up.

Troubleshooting the 2 GB push limit
----------------------------------------------------------------------

    GitHub has a maximum 2 GB limit for a single push.

* プッシュを細分するしかない。
* ブランチのサイズが重要。
* コミットは一つずつプッシュすることが可能：
  ``git push REMOTE-NAME <YOUR_COMMIT_SHA_NUMBER>:refs/heads/BRANCH-NAME``

..

    If the repository does not have any history, or your initial commit was over
    2 GB on its own and you don't mind resetting the Git history, you can also
    start from scratch.

最初からリポジトリーを構築することで ``git lfs install`` を実行できる。

ビデオファイルメインのリポジトリーをやるときがあるかもしれない。そのときはこの記
事が役に立つ。

Subversion
======================================================================

    You can use Subversion clients and some Subversion workflows and properties
    with GitHub.

Git を使っているのならばわざわざ旧式の VCS を採用することはない。

Subversion & Git differences
----------------------------------------------------------------------

* ブランチやタグに相当するものはサブディレクトリーの形式で表現される。
* サブプロジェクトについてはこの記述では概要が見えない。
* 履歴は後から変更されないものとする。

..

    Note: Subversion support will be removed from GitHub on January 8, 2024. A
    future release of GitHub Enterprise Server after January 8, 2024 will also
    remove Subversion support.

Support for Subversion clients
----------------------------------------------------------------------

    GitHub supports Subversion clients via the HTTPS protocol. We use a
    Subversion bridge to communicate svn commands to GitHub.

..

    Subversion checkouts are different: they mix the repository data in the
    working directories, so there is a working directory for each branch and tag
    you've checked out. For repositories with many branches and tags, checking
    out everything can be a bandwidth burden, so you should start with a partial
    checkout.

以降の記述からすると、任意の GitHub Repository を :command:`svn` で取り扱い可能
であるように読める？

.. code:: console

   bash$ svn co --depth empty https://github.com/USER/REPO
   bash$ svn up trunk
   bash$ svn up --depth empty branches

これは立ち入らなくていい。

Properties supported by GitHub
----------------------------------------------------------------------

次の三つは support している：

* svn:executable
* svn:mime-type
* svn:ignore

その他はしていない。

Exploring integrations
======================================================================

About using integrations
----------------------------------------------------------------------

    Integrations are tools and services that connect with GitHub to complement
    and extend your workflow.

GitHub Actions というものを使う場合にここへ至る。

    You can discover many integrations in GitHub Marketplace.

About building integrations
----------------------------------------------------------------------

    Many integrations are GitHub Apps, GitHub Actions workflows, or custom
    actions for GitHub Actions workflows.

* GitHub Apps are integrations that run on the app owner's server or on a user
  device.
* GitHub Actions workflows are workflows that run when specific events occur on
  GitHub.
* Custom actions are code that can be executed by a GitHub Actions workflow.

詳しくは別の章で。

    If your integration is a GitHub App or custom action, you can publish your
    integration on GitHub Marketplace.

Featured integrations
----------------------------------------------------------------------

    Use GitHub extensions to work seamlessly in repositories on GitHub.com
    within third-party applications.

..

    With the GitHub for Visual Studio Code extension, you can review and manage
    GitHub pull requests in VS Code.

GitHub Pull Requests and Issues か？

    You can integrate your personal or organization account on GitHub.com with
    third-party team communication tools, such as Slack or Microsoft Teams.

Twitter はないのか。

GitHub Developer Program
----------------------------------------------------------------------

    If you build tools that integrate with GitHub, you can join the GitHub
    Developer Program.

これはない。

Archive account and public repos
======================================================================

Request account archive
----------------------------------------------------------------------

    You can export and review the metadata that GitHub stores about your
    personal account.

自分のアカウントのみか。

    When you request an export of your personal data through settings on
    GitHub.com, GitHub packages your personal data in a ``tar.gz`` file and
    sends you an email to your primary email address with a download link.

リンクの期限は一週間。

:menuselection:`Settings --> Account --> Export account data` の
:guilabel:`Start export`.

このリンクはメールで知る。リンクを無効にするには同じように :guilabel:`Delete` を
押す。

GitHub Archive program
----------------------------------------------------------------------

    People with admin permissions to a public repository can opt into or out of
    the GitHub Archive Program.

リポジトリー :menuselection:`Settings --> Features --> Preserve this repository`.
