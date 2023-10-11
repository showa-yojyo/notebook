======================================================================
Repositories documentation ノート
======================================================================

`Repositories documentation <https://docs.github.com/en/repositories>`__ は
GitHub の基本機能であるリポジトリーに関する記述なので全文読みたい。

.. contents::

* :guilabel:`Quickstart` は Get started の Quickstart へ
* :guilabel:`Overview` は Creating and managing repositories の About
  repositores へ
* 組織絡みは割愛。

Creating and managing repositories
======================================================================

About repositories
----------------------------------------------------------------------

* Visibility を設定可能 (public or private)
* アカウント個別に何らかの操作権限を与えることも可能
* GitHub Free プランでも無制限
* Issues を利用可能
* Discussions を利用可能
* Pull requests 可能

..

  Private repositories are only accessible to you, people you explicitly share
  access with, and, for organization repositories, certain organization members.

英語の private は «belonging to or for the use of one particular person or group
of people only» (OED) を意味するので、語義どおりだ。

  People with admin permissions for a repository can change an existing
  repository's visibility.

リポジトリー創設者だけが変更可能というわけではない。他の性質についてもこの法則が
たぶん成り立つ。

リポジトリー内の閲覧と差分に対する制限について、

* GitHub と API のどちらでも制限される。だいたい同じ制限。
* 生ファイルを raw.githubusercontent.com からアクセス可能。これは
  :guilabel:`Raw` ボタン。
* 差分が巨大になる可能性があるので、コミットなどにも制限がある：

    In a pull request, no total diff may exceed 20,000 lines that you can load or
    1 MB of raw diff data.

Best practices for repositories
----------------------------------------------------------------------

リポジトリーごとに :file:`README` を設ける。

  You can add a :file:`README` file to a repository to communicate important
  information about your project. A :file:`README`, along with a repository
  license, citation file, contribution guidelines, and a code of conduct,
  communicates expectations for your project and helps you manage contributions.

このようにたくさんの役割を果たすので、人の目に触れるものについては用意することに
する。

フォークよりもブランチを良しとする。

* 単一のリポジトリーで作業し、ブランチ間で pull request をするのがよい。
* 保護ブランチ機能を活用する。

Git Large File Storage を利用する。別の節で詳しくやる。

  To track large files in a Git repository, we recommend using Git Large File
  Storage (Git LFS).

GitHub ではファイルサイズの上限が設けられている。

Creating a new repository
----------------------------------------------------------------------

ブラウザーで作成する方法は、画面右上プラスボタンから :guilabel:`New repository`
を押す。テンプレートを利用する場合としない場合とで操作が異なる。しない場合には次
のファイルを追加可能：

* :file:`README`
* :file:`.gitignore`
* ライセンスファイル

URL で直接生成する方法もある。次のような URL にアクセスするとリポジトリーが生成
されるようだ：

.. code:: text

   https://github.com/new?name=XXXX&owner=YYYY

問い合わせ引数は色々用意されている。

Creating a repository from a template
----------------------------------------------------------------------

  You can generate a new repository with the same directory structure and files
  as an existing repository.

これは有用な機能だが、Git 本体に欲しい。

  Branches created from a template have unrelated histories, which means you
  cannot create pull requests or merge between the branches.

強いて言えば fork に近い。履歴をテンプレート元リポジトリーから全く引き継がない。

テンプレートから作成する方法。Codespaces のときと似た位置に UI があ
る。:menuselection:`Use this template --> Create a new repository`.

Creating a template repository
----------------------------------------------------------------------

* リポジトリーを作成してからそれをテンプレートにすればよい。
* テンプレートリポジトリーには Git LFS を使って保存されたファイルを含められな
  い。

リポジトリー画面 :menuselection:`Settings --> Template Repository` をオン。

Creating an issues-only repository
----------------------------------------------------------------------

この話題は要るか？

Duplicating a repository
----------------------------------------------------------------------

これは用語の確認と Git だけで閉じた操作ということで意味がある。

.. code:: console

   bash$ git clone --bare https://github.com/EXAMPLE-USER/OLD-REPOSITORY.git
   bash$ cd OLD-REPOSITORY.git
   bash$ git push --mirror https://github.com/EXAMPLE-USER/NEW-REPOSITORY.git
   bash$ cd ..
   bash$ rm -rf OLD-REPOSITORY.git

LFS 絡みのときは：

.. code:: console

   bash$ git clone --bare https://github.com/EXAMPLE-USER/OLD-REPOSITORY.git
   bash$ cd OLD-REPOSITORY.git
   bash$ git lfs fetch --all
   bash$ git push --mirror https://github.com/EXAMPLE-USER/NEW-REPOSITORY.git
   bash$ git lfs push --all https://github.com/EXAMPLE-USER/NEW-REPOSITORY.git
   bash$ cd ..
   bash$ rm -rf OLD-REPOSITORY.git

Cloning a repository
----------------------------------------------------------------------

GitHub のリポジトリーをローカルにクローンする方法。超基本。

.. code:: console

   bash$ git clone https://github.com/PATH-TO/REPOSITORY
   # or
   bash$ gh repo clone https://github.com/PATH-TO/REPOSITORY

Troubleshooting cloning errors
----------------------------------------------------------------------

HTTPS を使う場合のよくあるエラーはかなり研究されているようだ。

  These errors usually indicate you have an old version of Git, or you don't
  have access to the repository.

次の事項を確認する：

* ``git --version``
* ``git remote -v``
* 個人アクセストークン

..

  When prompted for a username and password, make sure you use an account that
  has access to the repository.

SSH 鍵を設定済みなら SSH 版 URL を使える。

Error: Repository not found の場合は次を確認：

* ``git@github.com:user/repo.git`` のスペリング
* 権限
* SSH の場合は ``ssh -T git@github.com`` の出力

Error: Remote HEAD refers to nonexistent ref, unable to checkout の場合は：

  This error occurs if the default branch of a repository has been deleted on
  GitHub.com.

``git branch -a`` して適切なものに ``git checkout`` する。

Renaming a repository
----------------------------------------------------------------------

リポジトリー :menuselection:`Settings --> Repository name` ページで変更後の名前
を記入して :guilabel:`Rename` する。

* 変更後、ローカルクローンで ``git remote set-url origin NEW_URL`` すること。
* 古い名前をいつか再利用しようとしないこと。リダイレクトが壊れる。

Transferring a repository
----------------------------------------------------------------------

これはやりたくない。

  When you transfer a repository to a new owner, they can immediately administer
  the repository's contents, issues, pull requests, releases, projects
  (classic), and settings. You can also change the repository name while
  transferring a repository.

引っ越し不能なリポジトリーもある。

* GitHub Pages の URL 関連の問題があることに注意。
* リポジトリー :menuselection:`Settings --> Transfer --> New owner`.

Deleting a repository
----------------------------------------------------------------------

これはやりたくない。

削除してから 90 日以内ならば復元できるリポジトリーもあるが、基本はやり直し不能と
思ったほうがいい。

リポジトリー :menuselection:`Settings --> Delete this repository`.

Restoring a deleted repository
----------------------------------------------------------------------

これは想定していない。

フォークが関係していることで復元不能となる場合がある。

アカウント :menuselection:`Settings --> Repositories --> Deleted repositories`
で対象項目 :guilabel:`Restore` を押す。

Managing your repository's settings and features
======================================================================

Customizing your repository
----------------------------------------------------------------------

About READMEs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  :file:`README` files typically include information on:

  * What the project does
  * Why the project is useful
  * How users can get started with the project
  * Where users can get help with your project
  * Who maintains and contributes to the project

:file:`README` を置くディレクトリーは次のいずれかになり、GitHub はこの順に優先す
る：

* :file:`/.github/`
* :file:`/`
* :file:`/docs/`

..

  If you add a :file:`README` file to the root of a public repository with the
  same name as your username, that :file:`README` will automatically appear on
  your profile page.

.. todo::

   これは後で実施する。

:file:`README` の TOC がリポジトリートップページ内表示領域のハンバーガーマークか
らアクセス可能。

:file:`README` 内容で相対リンクを示すことが可能。基準はこのファイルのディレクト
リー。

  A :file:`README` should contain only the necessary information for developers
  to get started using and contributing to your project. Longer documentation is
  best suited for wikis.

Licensing a repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  For your repository to truly be open source, you'll need to license it so that
  others are free to use, change, and distribute the software.

ライセンスはまったくわからない。そういう人は `Choose an open source license |
Choose a License <https://choosealicense.com/>`__ で手がかりを得る。

  However, without a license, the default copyright laws apply, meaning that you
  retain all rights to your source code and no one may reproduce, distribute, or
  create derivative works from your work.

普通の著作権のほうが無難ではないか。しかし、リポジトリーを公開している以上はオー
プンソースにするのが自然だろう。

  As a best practice, we encourage you to include the license file with your
  project.

ファイル :file:`LICENSE`, :file:`LICENSE.txt`, :file:`LICENSE.md`,
:file:`LICENSE.rst` のどれかをリポジトリーのルートに置くのが普通。

ライセンスで検索することが可能。

GitHub でリポジトリーを新規作成する時点で :guilabel:`Choose a license` で既存の
ライセンスから指定可能。

Displaying a sponsor button in your repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

スポンサーなどいないので割愛するか。

  You can configure your sponsor button by editing a :file:`FUNDING.yml` file in
  your repository's :file:`.github` folder, on the default branch.

.. code:: yaml

   github: [octocat, surftocat]
   patreon: octocat
   tidelift: npm/octo-package
   custom: ["https://www.paypal.me/octocat", octocat.com]

リポジトリー :menuselection:`Settings --> Generel --> Sponsorships` をオン。さら
に :guilabel:`Set up sponsor button` を押すと、上記ファイルの追加編集画面が現れ
る。

Customizing your repository's social media preview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Twitter や Facebook からリポジトリー URL にリンクしてもらうと指定の絵が出る仕組
みだ。

  Tip: Your image should be a PNG, JPG, or GIF file under 1 MB in size. For the
  best quality rendering, we recommend a size of at least 640 by 320 pixels
  (1280 by 640 pixels for best display).

リポジトリー :menuselection:`Settings --> Social Preview` に画像をアップロードす
るのだろう。

Classifying your repository with topics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

リポジトリーの右の柱にあるキーワード集合。

  To browse the most used topics, go to https://github.com/topics/.

リポジトリー :guilabel:`About` 歯車クリック。

About code owners
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  You can use a :file:`CODEOWNERS` file to define individuals or teams that are
  responsible for code in a repository.

なぜ責任者を明示するのか。

  Code owners are automatically requested for review when someone opens a pull
  request that modifies code that they own.

リポジトリーのファイル画面で :guilabel:`Owned by` マークが表示される。

ファイル :file:`CODEOWNERS` の場所は :file:`README` と同じ仕様のようだ。

  :file:`CODEOWNERS` files must be under 3 MB in size.

:file:`CODEOWNERS` の構文は :file:`.gitignore` のそれに似ている。

.. todo::

   まず簡単なリポジトリーで実践する。意義があるようなら力を入れているリポジト
   リーでも用意する。

About repository languages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  GitHub uses the open source `Linguist library
  <https://github.com/github-linguist/linguist>`__ to determine file languages
  for syntax highlighting and repository statistics.

GitHub が自動判定する。

About CITATION files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

これを書きこなせたら見栄えがいい。専門家向けだろう。

  You can add a :file:`CITATION.cff` file to the root of a repository to let
  others know how you would like them to cite your work.

これを用意するとこうなる：

  When you add a :file:`CITATION.cff` file to the default branch of your
  repository, a link is automatically added to the repository landing page in
  the right sidebar, with the label :guilabel:`Cite this repository`.

Enabling features for your repository
----------------------------------------------------------------------

Disabling issues
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

他人からバグ報告をもらいたくない場合に Issues 機能を無効にする。リポジトリー
:menuselection:`Settings --> Features --> Issues` をオフにする。

Disabling classic projects in a repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

リポジトリー :menuselection:`Settings --> Features --> Projects` をオフにする。

Managing GitHub Actions settings for a repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

リポジトリー :menuselection:`Settings --> Actions --> Actions permissions` 以下
を調整する。

リポジトリー :menuselection:`Settings --> Actions --> General --> Fork pull
request workflows from outside collaborators` 以下を調整する。

``GITHUB_TOKEN`` 権限を構成する：リポジトリー :menuselection:`Settings -->
Actions --> General --> Workflow permissions` 以下を調整。

  By default, when you create a new repository in your personal account,
  workflows are not allowed to create or approve pull requests.

チェックボックスのほう。

  You can configure the retention period for GitHub Actions artifacts and logs
  in your repository.

実は private のほうが長期間保存可能。

リポジトリー :menuselection:`Settings --> Actions --> General --> Artifact and
log retention` 以下を調整。

Enabling or disabling GitHub Discussions for a repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

リポジトリー :menuselection:`Settings --> General --> Features --> Discussion`
をオンかオフ。

Managing security and analysis settings for your repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

リポジトリー :menuselection:`Settings --> Code security and analysis` 各機能の
:guilabel:`Enable` ボタンを押す。

Managing repository settings
----------------------------------------------------------------------

リポジトリーの機能を選択する。

Setting repository visibility
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

リポジトリーを public/private にすることの違いと、public/private に変更する方法
を理解する。

Managing teams and people with access to your repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

割愛。

Managing the forking policy for your repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  You can allow or prevent the forking of a specific private repository owned by
  an organization.

割愛。

Managing pull request reviews in your repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  You can limit which users can approve or request changes to a pull requests in
  a public repository.

依頼者を制限するわけではないことに注意。

  When you enable code review limits, anyone can comment on pull requests in
  your public repository, but only people with read access or higher can approve
  pull requests or request changes.

査読者を制限するオプションであると読める？

リポジトリー :menuselection:`Settings --> Moderation options --> Code review
limits` 以下をいじる。

Managing the commit signoff policy for your repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  You can require users to automatically sign off on the commits they make to
  your repository using GitHub's web interface.

サインオフはコミットの内容を保証するための仕組みらしい。

  Compulsory commit signoffs only apply to commits made via the web interface.

ローカルでコミットする場合は本項の範囲外ということか。

  You can determine whether a repository you are contributing to has compulsory
  commit signoffs enabled by checking the header of the commit form at the
  bottom of the file you are editing. After compulsory commit signoff has been
  enabled, the header will read :guilabel:`Sign off and commit changes`.

ブラウザー経由でファイルを変更するときに確認したい。

リポジトリー :menuselection:`Settings --> General --> Require contributors to
sign off on web-based commits` をオンにする。

Managing the push policy for your repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  You can limit how many branches and tags can be updated in a single push.

ちなみに ``git push --mirror`` も禁止できる。

リポジトリー :menuselection:`Settings --> General --> Limit how many branches
and tags can be updated in a single push` をオンにして :guilabel:`Up to` 値を設
定する。推奨値は 5 だ。なぜなら Git では一度の push でブランチの名前を変更するに
は、ブランチの削除とブランチの作成という二つが必要だからだ。

Managing Git LFS objects in archives of your repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コードアーカイブに LFS を含めるか否か。

リポジトリー :menuselection:`Settings --> General --> Include Git LFS objects in
archives` をオンオフ。

About email notifications for pushes to your repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  You can choose to automatically send email notifications to a specific email
  address when anyone pushes to the repository.

リポジトリー :menuselection:`Settings --> Email notifications` を選択。番号を入
れて次へ。

Configuring autolinks to reference external resources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

割愛。

Configuring tag protection rules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

リポジトリー :menuselection:`Settings --> Tags --> New rule` を押す。このパター
ンにマッチするタグを作成することが不可能になる？

Configuring branches and merges in your repository
----------------------------------------------------------------------

Managing branches in your repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Whenever you propose a change in Git, you create a new branch.

ということになっている。

Viewing branches in your repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

リポジトリー画面左上のブランチボタンに :guilabel:`View all branches` リンクがあ
る。リンク先の画面ではブランチ一覧から検索したりフィルターしたりすることが可能。

:guilabel:`Stale branshes` に現れるものが削除候補だ。

Renaming a branch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``master`` を ``main`` に変更するなど、状況は思いつく。

  When you rename a branch on GitHub.com, any URLs that contain the old branch
  name are automatically redirected to the equivalent URL for the renamed
  branch.

ローカルリポジトリーの対応ブランチも rename する必要が生じる。その案内も対応。
さらに GitHub Actions も自動更新されたりはしない。

:guilabel:`View all branches` リンク先の項目鉛筆ボタンから rename 可能。

ローカルで必要となる作業は：

.. code:: console

   bash$ git branch -m OLD-BRANCH-NAME NEW-BRANCH-NAME
   bash$ git fetch origin
   bash$ git branch -u origin/NEW-BRANCH-NAME NEW-BRANCH-NAME
   bash$ git remote set-head origin -a
   # おまけで：
   bash$ git remote prune origin

Changing the default branch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  The default branch is the base branch for pull requests and code commits.

リポジトリー :menuselection:`Settings --> General --> Default branch` で設定。

Deleting and restoring branches in a pull request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  You can delete a branch that is associated with a pull request if the pull
  request has been merged or closed and there are no other open pull requests
  referencing the branch.

処理済みの :guilabel:`Pull request` ページ下部に :guilabel:`Delete branch` があ
るからそれを押す。復元したい場合も同様の手順。

Configuring pull request merges
----------------------------------------------------------------------

About merge methods on GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  The default merge method creates a merge commit.

これは Git 単体の話？

  The rebase and merge behavior on GitHub deviates slightly from ``git rebase``.

このことを承知しておく。

以前述べたように GitHub 上でのマージでは sign off が効かなくなる。

Configuring commit merging for pull requests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

リポジトリー :menuselection:`Settings --> General --> Pull Requests` で
:guilabel:`Allow merge commits` をオンにする。

  If you select more than one merge method, collaborators can choose which type
  of merge commit to use when they merge a pull request.

Configuring commit squashing for pull requests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

リポジトリー :menuselection:`Settings --> General --> Pull Requests` で
:guilabel:`Allow squash merging` をオンにする。

Configuring commit rebasing for pull requests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

リポジトリー :menuselection:`Settings --> General --> Pull Requests` で
:guilabel:`Allow rebase merging` をオンにする。

Managing a merge queue
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Using a merge queue is particularly useful on branches that have a relatively
  high number of pull requests merging each day from many different users.

したがって割愛。

Managing suggestions to update pull request branches
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pull request には base ブランチの最新状態に追いついていて欲しい。

リポジトリー :menuselection:`Settings --> General --> Pull Requests` で
:guilabel:`Always suggest updating pull request branches` をオンにする。

Managing auto-merge for pull requests in your repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  If you allow auto-merge for pull requests in your repository, people with
  write permissions can configure individual pull requests in the repository to
  merge automatically when all merge requirements are met.

リポジトリー :menuselection:`Settings --> General --> Pull Requests` で
:guilabel:`Allow auto-merge` をオンにする。

Managing the automatic deletion of branches
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

リポジトリー :menuselection:`Settings --> General --> Pull Requests` で
:guilabel:`Automatically delete head branches` をオンにする。

Managing protected branches
----------------------------------------------------------------------

  For example, you can block pull requests that don't pass status checks or
  require that pull requests have a specific number of approving reviews before
  they can be merged.

About protected branches
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

この機能の主旨はブランチに対する push, merge, delete から保護することだ。

  By default, the restrictions of a branch protection rule don't apply to people
  with admin permissions to the repository or custom roles with the "bypass
  branch protections" permission.

保護機能は特権を有する人には効かない。これはオプション設定で効かせられる。

  Required status checks ensure that all required CI tests are passing before
  collaborators can make changes to a protected branch. Required status checks
  can be checks or statuses.

この辺の術語整理は Pull requests の章で改めて行う。

  When you enable required commit signing on a branch, contributors and bots can
  only push commits that have been signed and verified to the branch.

とにかく署名コミットならばいいわけで、どこかの馬の骨のコミットでも許される。した
がって、それほど有意義には思えぬが？

  A strictly linear commit history can help teams reverse changes more easily.

これは良さそうだ。

  You can require that changes are successfully deployed to specific
  environments before a branch can be merged.

..

  Locking a branch ensures that no commits can be made to the branch.

この保護機能がいちばん強い規則だと思う。

Managing a branch protection rule
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

リポジトリー :menuselection:`Settings --> Branches --> Add branch protection
rules` を押す。パターンを記入、オプションを追加する。

上級者向け機能。割愛。

Managing rulesets for a repository
----------------------------------------------------------------------

About rulesets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  A ruleset is a named list of rules that applies to a repository. You can
  create rulesets to control how people can interact with selected branches and
  tags in a repository.

リポジトリーにおける法律だと考えられる。既視感のある機能だ。

  When you create a ruleset, you can allow certain users to bypass the rules in
  the ruleset. This can be users with a certain role, such as repository
  administrator, or it can be specific teams or GitHub Apps.

明示的に許可されないと、管理人だろうがアプリケーションだろうが法に縛られる。

Rulesets のほうが branch protection よりも望ましい。本書にあるように柔軟性で優る。

  If the same rule is defined in different ways across the aggregated rulesets,
  the most restrictive version of the rule applies.

この原則を覚えておく必要がある。

Creating rulesets for a repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

リポジトリー :menuselection:`Settings --> Rules --> Rulesets` で緑ボタンを押す。

Managing rulesets for a repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ブランチ一覧画面で Rulesets を有するブランチの盾アイコンを押す。

Available rules for rulesets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

名前だけ挙げておくと：

* Restrict creations
* Restrict updates
* Restrict deletions
* Require linear history
* Require deployments to succeed before merging
* Require signed commits
* Require a pull request before merging
* Require status checks to pass before merging
* Block force pushes

Troubleshooting rules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Depending on which rules are active, you may need to edit your commit history
  locally before you can push your commits to the remote branch.

や、

  If a branch or tag is targeted by rules restricting the metadata of commits,
  your commits may be rejected if part of the commit's metadata does not match a
  certain pattern.

を覚えておく。

Working with files
======================================================================

Managing files
----------------------------------------------------------------------

Creating new files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

アクセス権のないリポジトリーにファイルを追加しようとしないこと。リポジトリーを
フォークしようという流れになる。

次のような情報を追加しないこと：

* Passwords
* SSH keys
* AWS access keys
* API keys
* Credit card numbers
* PIN numbers

リポジトリーページの対象ディレクトリーに対応するページを開いて
:menuselection:`Add file --> Create new file` を押す。ファイル名を決めて内容を記
入する。

コミットをしないと追加とは言えない？

ブランチを決める。Pull request にするかどうかということだ。

最後に :guilabel:`Commit changes` か :guilabel:`Propose changes` を押す。後者の
場合、追加確定にはならない？

Adding a file to a repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Files that you add to a repository via a browser are limited to 25 MiB per
  file. You can add larger files, up to 100 MiB each, via the command line.
  （略） To add files larger than 100 MiB, you must use Git Large File Storage.

リポジトリーページの対象ディレクトリーに対応するページを開いて
:menuselection:`Add file --> Upload files` を押す。ファイル名を決めて内容を記入
する。

コマンドラインで Git による手順でも当然かまわない。以下のファイル操作に関しても
だ。

Moving a file to a new location
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

移動したいファイルのページを開いて鉛筆ボタンを押す。ファイルパスを相対パスで入
力。

Editing files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

編集したいファイルのページを開いて鉛筆ボタンを押す。内容を書き換える。リポジト
リーの所有者が自分か他人かで最終手順がやや異なる。

Renaming a file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ファイル移動と同じ。

Deleting files in a repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

削除したいファイルのページを開いて右上の…から :guilabel:`Delete file` を押す。そ
れからはいつもと同じ。ディレクトリーの場合も同様の手順。

Customizing how changed files appear on GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Use a :file:`.gitattributes` file to mark files that match a given "pattern"
  with the specified attributes.

.. code:: text

   search/index.json linguist-generated=true

このようにすると :file:`search/index.json` に対しては GitHub 上で差分出力を表示
しなくなる。

Using files
----------------------------------------------------------------------

Navigating code on GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ソースコードを表示すると、シンボルの定義位置、参照位置などにジャンプする機能があ
る。キーボードショートカットを覚えておくと便利。

ファイルを :guilabel:`Code` モードで表示させ、右上の :guilabel:`Open symbols
panel` を押す。

リポジトリーをまたぐジャンプが可能である場合もある？

  Code navigation only works for repositories with fewer than 100,000 files.

Viewing a file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  You can view raw file content or trace changes to lines in a file and discover
  how parts of the file evolved over time.

:guilabel:`Raw` ボタンを押すと、ファイル内容を整形なしで表示する。

* :guilabel:`Copy raw file` を押すと、テキストをクリップボードにコピーする。
* :guilabel:`Download raw file` を押すと、対象ファイルをダウンロードすることが可
  能。
* :guilabel:`Blame` ボタンを押すと ``git blame`` を整形したものを表示する。

この機能に関して :file:`.git-blame-ignore-revs` なる特殊ファイルが考慮される。

  All revisions specified in the :file:`.git-blame-ignore-revs` file, which must
  be in the root directory of your repository, are hidden from the blame view
  using Git's ``git blame --ignore-revs-file`` configuration setting.

Getting permanent links to files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  When viewing a file on GitHub.com, you can press the :kbd:`y` key to update
  the URL to a permalink to the exact version of the file you see.

この URL は欲しい場合があるかもしれない。

.. code:: text

   https://github.com/github/USERNAME/blob/SHA/FILEPATH

Downloading source code archives
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  You can download a snapshot of the code in your repository.

よそのリポジトリーに対して利用するかもしれない。

  These snapshots are generated by the ``git archive`` command in one of two
  formats: tarball or zipball.

したがって履歴は含まれず、モノを手軽に得られる。

リポジトリートップの :menuselection:`Code --> Local --> Download ZIP` を押す。

まともなリポジトリーならリリース番号やタグでアーカイブを配布している。その場合は
右の柱にリンクがある。

Working with non-code files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  GitHub supports rendering and diffing in a number of non-code file formats.

次に挙げるデータファイルの描画：

* Rendering and diffing images
* 3D File Viewer
* Rendering CSV and TSV data
* Rendering PDF documents
* Rendering differences in prose documents
* Mapping GeoJSON/TopoJSON files on GitHub
* Working with Jupyter Notebook files on GitHub
* Displaying Mermaid files on GitHub

..

  SVGs don't currently support inline scripting or animation.

これはがんばっていただきたい。

  GitHub can host and render 3D files with the ``.stl`` extension.

これを試してみたい。よほど重いデータでなければ描画してくれそうだ。

  To display your 3D file elsewhere on the internet, modify this template and
  place it on any HTML page that supports JavaScript:

  .. code:: html

     <script src="https://embed.github.com/view/3d/<username>/<repo>/<ref>/<path_to_file>"></script>

Managing large files
----------------------------------------------------------------------

  You can manage large files with Git Large File Storage.

About large files on GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  GitHub limits the size of files you can track in regular Git repositories.

ローカルで成立していても GitHub で弾かれるということがあり得る。

  If you attempt to add or update a file that is larger than 50 MiB, you will
  receive a warning from Git.

* Windows エクスプローラーの表示なら 52MB 程度。
* 100MiB を超えるとさすがに弾かれる。

..

  We recommend repositories remain small, ideally less than 1 GB, and less than
  5 GB is strongly recommended.

これは正直気になる。

  You can find advice and a tool for repository analysis in the
  ``github/git-sizer`` repository.

試したい。

About Git Large File Storage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Git LFS handles large files by storing references to the file in the
  repository, but not the actual file itself.

からくりはよくわからない。

Installing Git Large File Storage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`git-lfs.github.com <https://git-lfs.com/>`__ でモノをダウンロードする。同梱され
ている :file:`install.sh` を実行する。

.. code:: console

   bash$ sudo ./install.sh
   bash$ git lfs install

これもやるだけやってみる。

Configuring Git Large File Storage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Once Git LFS is installed, you need to associate it with a large file in your
  repository.

すでに対象がリポジトリーに格納されている場合には二度手間のようになる：

  If there are existing files in your repository that you'd like to use GitHub
  with, you need to first remove them from the repository and then add them to
  Git LFS locally.

ファイルパターンと LFS を関連付ける：

.. code:: console

   bash$ git lfs track "*.psd"

..

  This command amends your repository's :file:`.gitattributes` file and
  associates large files with Git LFS.

それから ``git add`` などの操作を行う。プッシュ時にファイルのアップロードに関す
る診断情報が表示されることになる。

About storage and bandwidth usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

こういう規則がある：

  When you commit and push a change to a file tracked with Git LFS, a new
  version of the entire file is pushed and the total file size is counted
  against the repository owner's storage limit. When you download a file tracked
  with Git LFS, the total file size is counted against the repository owner's
  bandwidth limit. Git LFS uploads do not count against the bandwidth limit.

GitHub Actions も帯域幅を消費することがある。記憶域枠や帯域幅枠を超える場合、良
くないことが起こると思っていていい。

Collaboration with Git Large File Storage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

プロジェクト関係者全員が LFS を構成していると思わないほうがいい。

Moving a file in your repository to Git Large File Storage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

先述のように、いったん削除してから LFS に関連付けて追加し直す。

Removing files from Git Large File Storage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

誤って追加した機密データを履歴から削除するのと同等の手間がかかる。
詳しくは ``filter-repo`` を述べるところでやる。

LFS 自身をリポジトリーから外すには：

.. code:: console

   bash$ git lfs uninstall

リポジトリーから LFS オブジェクトを削除するのも面倒なことになる。リポジトリー全
体の作り直しまである。

Resolving Git Large File Storage upload failures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ここに述べられていることは怪しい。

.. code:: console

   bash$ git lfs install
   bash$ git lfs push --all origin

Releasing projects on GitHub
======================================================================

  You can create a release to package software, release notes, and binary files
  for other people to download.

らしい装置が出てきた。

About releases
----------------------------------------------------------------------

  Releases are based on Git tags, which mark a specific point in your
  repository's history.

ただしリリース日はタグの日付とは異なることがある。

リリースノートは手動でも自動でも作成可能。後者に興味がある。

リリースには依存関係がある場合がある。

  You can also use the Releases API to gather information, such as the number of
  times people download a release asset.

リリースに含まれるファイルには 2GiB 容量枠が設けられているが、リリース全体にはそ
ういう制限がない。

Managing releases in a repository
----------------------------------------------------------------------

GitHub CLI では次のようにタグを指定して、対話的にリリースする。

.. code:: console

   bash$ gh release create TAG
   # or specify arguments
   bash$ gh release create v1.3.2 \
     --title "v1.3.2 (beta)" \
     --notes "this is a beta release" \
     --prerelease

みっともないが削除も可能：

.. code:: console

   bash$ gh release delete TAG -y

GitHub リポジトリー画面からでもリリース可能。:menuselection:`Releases --> Draft
a new release` から手なりで。

既存リリースの編集はブラウザーから行うしかない。

Viewing your repository's releases and tags
----------------------------------------------------------------------

.. code:: console

   bash$ gh release view

Searching a repository's releases
----------------------------------------------------------------------

リポジトリー :guilabel:`Releases` ページで検索可能。

Linking to releases
----------------------------------------------------------------------

リポジトリー :guilabel:`Releases` ページのどこかに書いてある。最新リリースの URL
は次のような形だ： ``https://github.com/USER/REPOSITORY/releases/latest``

Comparing releases
----------------------------------------------------------------------

リポジトリー :guilabel:`Releases` ページの左柱に :guilabel:`Compare` がある。

Automatically generated release notes
----------------------------------------------------------------------

  Automatically generated release notes include a list of merged pull requests,
  a list of contributors to the release, and a link to a full changelog.

リポジトリー画面右柱 :guilabel:`Releases` を押す。そのページで :guilabel:`Draft
a new release` を押す。 :guilabel:`Choose a tag` ドロップダウンリストで対象のタ
グを選択する。:guilabel:`Generate release notes` を押す。フォームを埋めて次のど
ちらかを押して終わる：

* :guilabel:`Publish release`
* :guilabel:`Save draft`

自動生成リリースノートの構成方法は、リポジトリーにファイル
:file:`.github/release.yml` を用意する。この YAML ファイルには次の項目が必要だ：

``changelog.categories[*].title``
  リリースノートにおける変更点の区分のタイトル
``changelog.categories[*].labels``
  Pull requests をこの区分とするラベル

Automation for release forms with query parameters
----------------------------------------------------------------------

URL に引数を付ければ自動でリリースを定義できる？

.. code:: text

   https://github.com/OWNER/REPO/releases/new?tag=TAG
   https://github.com/OWNER/REPO/releases/new?target=TARGET
   https://github.com/OWNER/REPO/releases/new?tag=TAG&title=TITLE
   https://github.com/OWNER/REPO/releases/new?body=BODY
   https://github.com/OWNER/REPO/releases/new?prerelease=1

Viewing activity and data for your repository
======================================================================

  Gain insight into your repository by viewing activity and data.

Viewing deployment activity for your repository
----------------------------------------------------------------------

この機能は成果物を配備するプロジェクト向け。読書ノートで言うと Sphinx ビルドした
HTML ファイル群全体ということか。

リポジトリーページ右柱 :guilabel:`Environments` 下に ``github-pages`` などの成果
物一覧がある。

About repository graphs
----------------------------------------------------------------------

  If you maintain a repository, you can use this data to get a better
  understanding of who's using your repository and why they're using it.

なお、GitHub Free の公開リポジトリーでしか利用不能なリポジトリーグラフがある。

Using Pulse to view a summary of repository activity
----------------------------------------------------------------------

  You can use Pulse to see an overview of a repository's pull request, issue,
  and commit activity.

リポジトリーページの :guilabel:`Insights` を押す。

Viewing traffic to a repository
----------------------------------------------------------------------

リポジトリー :menuselection:`Insights --> Traffic`

Viewing a project's contributors
----------------------------------------------------------------------

リポジトリー :menuselection:`Insights --> Contrinutors`

Analyzing changes to a repository's content
----------------------------------------------------------------------

  You can see all commits made to a repository in the past year (excluding merge
  commits) in the :guilabel:`Commit` graph.

リポジトリー :menuselection:`Insights --> Commits`

リポジトリー :menuselection:`Insights --> Code frequency`

Understanding connections between repositories
----------------------------------------------------------------------

  The network graph displays the branch history of the entire repository
  network, including fork branches.

リポジトリー :menuselection:`Insights --> Network`

リポジトリー :menuselection:`Insights --> Forks`

Using the activity view to see changes to a repository
----------------------------------------------------------------------

  For example, you can choose to filter by :guilabel:`Force pushes`, to see all
  force pushes to the repository.

これは楽しそうだ。

リポジトリーページ右柱の :guilabel:`Activity` から、上のを見るには
:menuselection:`All activities --> Force pushes` を押す。

Archiving a GitHub repository
======================================================================

  You can archive, back up, and cite your work using GitHub, the API, or
  third-party tools and services.

引用とは？

Archiving repositories
----------------------------------------------------------------------

リポジトリーを保管することで、全てが読み取り専用になる。

  To make changes in an archived repository, you must unarchive the repository
  first.

解除できるのか。

  We recommend that you close all issues and pull requests, as well as update
  the :file:`README` file and description, before you archive a repository.

当然だ。

リポジトリー :menuselection:`Settings --> Danger Zone --> Archive this
repository` を押す。

保管解除は同じような手順による。

About archiving content and data on GitHub
----------------------------------------------------------------------

  By default, all public repositories are included in the GitHub Archive
  Program, a partnership between GitHub and organizations such as Software
  Heritage Foundation and Internet Archive to ensure the long-term preservation
  of the world's open source software.

海外人はこういう保護意識がしっかりしている。

  If you want third parties to consider your work on GitHub for archiving, you
  can add an open source license to your projects.

なのでリポジトリーにライセンス声明があることが重要。

Referencing and citing content
----------------------------------------------------------------------

  To make your repositories easier to reference in academic literature, you can
  create persistent identifiers, also known as Digital Object Identifiers
  (DOIs).

リポジトリーが公開であることが必要。

ここは割愛していいか。

Backing up a repository
----------------------------------------------------------------------

GitHub をバックアップ領域として利用しているので割愛。
