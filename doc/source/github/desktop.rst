======================================================================
GitHub Desktop documentation ノート
======================================================================

`GitHub Desktop documentation <https://docs.github.com/en/desktop>`__ を読む。
しかし、CLI のほうをメインでやってきたいので、Desktop は読み流す程度に留める。
以下、組織回りや Enterprise は割愛することがある。

.. contents::
   :depth: 3

* :guilabel:`Overview` → すぐ下の章
* :guilabel:`Quickstart` → :ref:`Getting started with GitHub Desktop
  <desktop-quickstart>`

Overview
======================================================================

About GitHub Desktop
----------------------------------------------------------------------

   GitHub Desktop is a free, open source application that helps you to work with
   files hosted on GitHub or other Git hosting services.

GitHub オンリーかと思いこんでいたが、そうではない。

   Because GitHub Desktop has a graphical user interface, it simplifies many of
   the aspects of Git that can be challenging for new users, such as memorizing
   commands and visualizing the changes you're making.

GUI アプリケーションということはやはりそういうことだろう。

   Unlike other Git clients, GitHub Desktop is specifically designed for use
   with GitHub, so it can make you more productive when working with
   repositories on GitHub.

とりわけ認証周りの機能に期待できる。

リポジトリーは `desktop/desktop <https://github.com/desktop/desktop>`__ にある。

.. _desktop-quickstart:

Getting started with GitHub Desktop
----------------------------------------------------------------------

インストーラーは `GitHub Desktop <https://desktop.github.com/>`__ にある。

.. code:: powershell

   PS > winget install -e --id GitHub.GitHubDesktop --source winget

GitHub アカウントはすでに開設したものとする。

:menuselection:`File --> Options --> Accounts` にて :guilabel:`Sign in` を押す。

:guilabel:`Preferences` で設定を好きにする。これは使用中随時触れる。

次のコマンドなどが設けられていて、実行すると GitHub に関係する操作が行われる。

* :menuselection:`File --> New repository...`
* :menuselection:`File --> Add local repository...`
* :menuselection:`File --> Clone repository...`

これらを含む主要機能は後で詳述。

Creating your first repository using GitHub Desktop
----------------------------------------------------------------------

   The tutorial will introduce the basics of working with Git and GitHub,
   including installing a text editor, creating a branch, making a commit,
   pushing to GitHub.com, and opening a pull request. The tutorial is available
   if you do not have any repositories on GitHub Desktop yet.

ふつうの :command:`git` を使っても完遂可能なチュートリアル。

   If you do not have any repositories associated with GitHub Desktop, you will
   see a "Let's get started!" view, where you can choose to create and clone a
   tutorial repository, clone an existing repository from the Internet, create a
   new repository, or add an existing repository from your hard drive.

この一覧は GitHub ログイン時に決定したものか？

GitHub Desktop の Tutorial を進めながらこの文書、特に画面キャプチャーを見るとい
い。このローカルリポジトリーは
:file:`%USERPROFILE%\\Documents\\GitHub\\desktop-tutorial` だ。

Supported operating systems for GitHub Desktop
----------------------------------------------------------------------

   Windows 10 64-bit or later. You must have a 64-bit operating system to run
   GitHub Desktop.

GitHub Desktop keyboard shortcuts
----------------------------------------------------------------------

後回し。

Launching GitHub Desktop from the command line
----------------------------------------------------------------------

実行ファイル名は ``github`` であることを覚えておく。 Windows の場合、
:file:`%APPDATA%\\Local\\GitHubDesktop\\bin` に Bash スクリプトとして置いてある。

* 引数なしで実行すると前回開いていたリポジトリーで開く。
* 引数をリポジトリーのパスにするとそれが開く。
* 引数を ``.`` にするとそこが開く。

WSL 内のリポジトリーからはパスの関係で使えない？

Installing and authenticating to GitHub Desktop
======================================================================

Setting up GitHub Desktop
----------------------------------------------------------------------

   After authenticating your account, you are ready to manage and contribute to
   projects with GitHub Desktop.

..

   You must have Git installed before using GitHub Desktop.

ところがなぜかインストールしていない Git 操作を Windows 側で実現できている。

   You can adjust defaults and settings to tailor GitHub Desktop to your needs.

Installing GitHub Desktop
----------------------------------------------------------------------

割愛。インストールパスを変更できたらありがたいのだが。

Authenticating to GitHub in GitHub Desktop
----------------------------------------------------------------------

   To keep your account secure, you must authenticate before you can use GitHub
   Desktop to access resources on GitHub.

メニュー :menuselection:`File --> Options...` を押す。:menuselection:`Accounts
--> Sign in` を押す。それからいつもブラウザーでしているのと同様に GitHub にログ
インする。

   If you encounter an authentication error, first try signing out and signing
   back in to your account on GitHub Desktop.

いちおうログアウトするのか。

残りはエラーに実際に遭遇してから。

About connections to GitHub in GitHub Desktop
----------------------------------------------------------------------

何度も何度も述べることだが：

   To connect to GitHub from GitHub Desktop, you must authenticate your account.

これでリモートリポジトリーにアクセス可能となる。

   GitHub Desktop caches your credentials (username and password or personal
   access token) and uses the credentials to authenticate for each connection to
   the remote repository.

だから認証処理は最初の一度でいい。キャッシュを削除する方法を知らない。

   GitHub Desktop connects to GitHub using HTTPS. If you use GitHub Desktop to
   access repositories that were cloned using SSH, you may encounter errors. To
   connect to a repository that was cloned using SSH, change the remote's URLs.

この現象は心当たりがある。SSH を HTTPS に変えたら動作するか確認しよう。

Updating GitHub Desktop
----------------------------------------------------------------------

メニュー :menuselection:`Help --> About GitHub Desktop` を押す。ダイアログの
:guilabel:`Check for updates` を押す。更新があれば GitHub Desktop を再起動すれば
いい。

Uninstalling GitHub Desktop
----------------------------------------------------------------------

Windows の標準的な手順でアンインストールすればいい。

Configuring and customizing GitHub Desktop
======================================================================

Configuring Git for GitHub Desktop
----------------------------------------------------------------------

   GitHub Desktop uses your local Git configuration settings

Windows には Git をインストールしていないから設定も空のはずだが動作するのは？

   If the email address that has been set in your Git configuration does not
   match an email address associated with the GitHub account you are currently
   logged in to, GitHub Desktop will show a warning prior to committing.

メニュー :menuselection:`File --> Options...` を押して :guilabel:`Git` 画面を開
く。項目数が少ないから迷わない。

使用しないが：

   You can change the name and email address used to author commits in a
   specific repository.

ただ、メニュー :menuselection:`Repository --> Repository settings...` があること
は覚えておく。

Configuring basic settings in GitHub Desktop
----------------------------------------------------------------------

メニュー :menuselection:`File --> Options...` の画面説明。いじったほうが早い。

Configuring a default editor in GitHub Desktop
----------------------------------------------------------------------

`VS Code <https://code.visualstudio.com/>`__ 以外はまったく聞いたことがない。

Setting a theme for GitHub Desktop
----------------------------------------------------------------------

:menuselection:`Options... --> Appearance` の説明。:guilabel:`Light` に固定す
る。

About Git Large File Storage and GitHub Desktop
----------------------------------------------------------------------

   GitHub Desktop includes Git Large File Storage for managing large files.

もしかすると、このために Desktop の用途があるかもしれない。

   To use Git LFS with GitHub Desktop, you must configure Git LFS using the
   command line.

ここが残念。

Adding and cloning repositories
======================================================================

Adding a repository from your local computer to GitHub Desktop
----------------------------------------------------------------------

メニュー :menuselection:`File --> Add local repository...` の説明。結局警告が出
て進めない。

Adding an existing project to GitHub using GitHub Desktop
----------------------------------------------------------------------

まずコンソールで ``git remote remove origin`` を実行してリモートリポジトリーへの
参照を外す。それからこのローカルリポジトリーを :guilabel:`Add local repository`
する。すると :guilabel:`Publish repository` を押せる。

Cloning and forking repositories from GitHub Desktop
----------------------------------------------------------------------

   Repositories on GitHub are remote repositories. You can clone or fork a
   repository with GitHub Desktop to create a local repository on your computer.

..

   When you try to use GitHub Desktop to clone a repository that you do not have
   write access to, GitHub Desktop will prompt you to create a fork
   automatically.

これは便利。

メニュー :menuselection:`File --> Clone repository...` を押す。フォークにするか
どうかの指定も可能。

   Creating an alias does not affect the repository's name on GitHub. In the
   repositories list, aliases appear in italics.

日本語で別名を付けても斜体になる。

Cloning a repository from GitHub to GitHub Desktop
----------------------------------------------------------------------

ブラウザーと Desktop の両方をログイン状態にしておく。ブラウザー側 GitHub リポジ
トリー画面の :menuselection:`Code --> Local --> Open with GitHub Desktop` を選
ぶ。

Making changes in a branch
======================================================================

Managing branches in GitHub Desktop
----------------------------------------------------------------------

   You can always create a branch in GitHub Desktop if you have read access to a
   repository, but you can only push the branch to GitHub if you have write
   access to the repository.

..

   GitHub Desktop will show a warning and prevent the branch from being created
   if the branch does not follow the rulesets.

Rulesets は学習してこなかったような。

ブランチは画面上部のドロップダウンを開いて、名前を記入して :guilabel:`New
Branch` ボタンを押す。必要に応じてダイアログから base ブランチを指定して
:guilabel:`Create Branch` ボタンを押す。

コミットからブランチを作る場合には画面上部左側ドロップダウンの
:guilabel:`History` から。対象コミットを右クリックするとメニューが現れる。
:guilabel:`Create Branch from Commit` を押す。

このようなブランチをリモートに送るには :guilabel:`Publish branch` する。

ブランチの切り替えも可能。

ブランチの削除はメニュー :menuselection:`Branch --> Delete...`

Committing and reviewing changes to your project in GitHub Desktop
----------------------------------------------------------------------

   If the commits you make in GitHub Desktop are associated with the wrong
   account on GitHub, update the email address in your Git configuration using
   GitHub Desktop.

..

   You can change the way diffs are displayed in GitHub Desktop to suit your
   reviewing needs.

差分表示に出てくる歯車アイコンを押せばわかる。

   As you make changes to files in your text editor and save them locally, you
   will also see the changes in GitHub Desktop.

VS Code でも同様の機能があるからわかる。

   If one file contains multiple changes, but you only want some of those
   changes to be included in a commit, you can create a partial commit.

``git add -p`` のようなことが可能。方法は：

   To exclude changed lines from your commit, click one or more changed lines so
   the blue disappears. The lines that are still highlighted in blue will be
   included in the commit.

..

   If you have uncommitted changes that you don't want to keep, you can discard
   the changes. This will remove the changes from the files on your computer.

画面上左ドロップダウンリストの :guilabel:`Changes` でファイルを選択。右クリック
メニュー :guilabel:`Discard Changes`, :guilabel:`Discard Selected Changes` など
を選択。

   You can discard one or more changed lines that are uncommitted.

さっきの青ハイライト行の記述を参照。

コミットログは画面左下に記入欄がある。VS Code を使っているとこれが見つけにくい。

   Optionally, to attribute a commit to another author, click the add co-authors
   icon and type the username(s) you want to include.

これは良い機能。

コマンド ``git push`` に相当する UI は画面上の右。

Stashing changes in GitHub Desktop
----------------------------------------------------------------------

画面上左ドロップダウンリストの :guilabel:`Changes` リストで右クリックメニュー。
:guilabel:`Stash all changes`を押す。作業後、退避していたファイルをローカルブラ
ンチに復帰するにはリスト下の :guilabel:`Stashed changes` から
:guilabel:`Restore` する。要らなくなった場合には :guilabel:`Discard` を押す。

Viewing the branch history in GitHub Desktop
----------------------------------------------------------------------

画面上左 :guilabel:`History` でコミットを適当に選択していれば差分やら何やらを確
認できる。

Pushing changes to GitHub from GitHub Desktop
----------------------------------------------------------------------

   If someone has made commits on the remote that are not on your local branch,
   GitHub Desktop will prompt you to fetch the new commits before pushing your
   changes to avoid merge conflicts.

良い。

普通の push は画面上右列 :guilabel:`Push origin` を押す。

   Optionally, click :guilabel:`Preview Pull Request` to open a preview dialog
   where you can review your changes and begin to create a pull request.

これも良い。

Managing commits
======================================================================

   You can use GitHub Desktop to amend, cherry-pick, reorder, revert, and squash
   commits.

Reverting a commit in GitHub Desktop
----------------------------------------------------------------------

   When you revert to a previous commit, the revert is also a commit. The
   original commit also remains in the repository's history.

素の Git での revert に等しい。

   Tip: When you revert multiple commits, it's best to revert in order from
   newest to oldest. If you revert commits in a different order, you may see
   merge conflicts.

これはいいことを聞いた。

:guilabel:`History` のコミット一覧項目の右クリックメニューに :guilabel:`Revert
Changes in Commit` がある。

Cherry-picking a commit in GitHub Desktop
----------------------------------------------------------------------

個人的に馴染みのない操作なので記述を多めに拾う。

   You can use GitHub Desktop to pick a specific commit on one branch and copy
   the commit to another branch.

利用例：

   For example, if you commit a bug fix to a feature branch, you can cherry-pick
   the commit with the bug fix to other branches of your project.

まず画面上中 :guilabel:`Branches` から、所望のコミットを有するブランチを選択す
る。それから画面左 :guilabel:`History` で対象のコミットを選択。右クリックメ
ニューから :guilabel:`Cherry-pick commit` を押す。

Reordering commits in GitHub Desktop
----------------------------------------------------------------------

:guilabel:`History` のコミットリストで項目をドラッグアンドドロップで並び替えるこ
とが可能。

衝突の解消が必要になりがちだが、対処法は割愛。

Squashing commits in GitHub Desktop
----------------------------------------------------------------------

:guilabel:`History` のコミットリストで、一つにまとめたい項目群を対象コミットの上
にドラッグアンドドロップ。:guilabel:`Squash Commits` を押す。

Amending a commit in GitHub Desktop
----------------------------------------------------------------------

:guilabel:`History` のコミットリスト項目の右クリックメニューに
:menuselection:`Amend Commit...` があるから押す。あとは見ればわかる。
:guilabel:`Amend last commit` を押して確定。

Managing tags in GitHub Desktop
----------------------------------------------------------------------

   GitHub Desktop allows you to create annotated tags.

:guilabel:`History` のコミットリスト項目の右クリックメニューに :guilabel:`Create
Tag...` がある。

コミットに付いたタグは、コミット画面の上部に記載される。

:guilabel:`History` のコミットリスト項目の右クリックメニューに :guilabel:`Delete
Tag...` がある。削除できるのは push 前のコミットに限る。

Checking out a commit in GitHub Desktop
----------------------------------------------------------------------

:guilabel:`History` のコミットリスト項目の右クリックメニューから
:menuselection:`Checkout Commit` を押す。このとき、画面上中が
:guilabel:`Detached HEAD` 表記になる。この状態から脱するには他のブランチへ切り替
える。

Working with your remote repository on GitHub or GitHub Enterprise
======================================================================

Creating an issue or pull request from GitHub Desktop
----------------------------------------------------------------------

   You can create an issue in your project's repository with GitHub Desktop.

   You can create a pull request in your project's repository with GitHub
   Desktop.

Pull request を作りに行く前に、ブランチを GitHub に push しておくこと。

Issue 作成方法：

メニュー :menuselection:`Repository --> Create issue on GitHub` を選択。するとリ
ポジトリーの設定次第で issue テンプレが開くか、空 issue 入力画面が開く。

Pull request 作成方法：画面にある :guilabel:`Preview Pull Request` を押す。問題
なければ :guilabel:`Create Pull Request` を押す。ブラウザーが開く。通常の pull
request 作成手順に合流する。

Syncing your branch in GitHub Desktop
----------------------------------------------------------------------

   You can sync your local branch with the remote repository by pulling any
   commits that have been added to the branch on GitHub since the last time you
   synced.

孤独なプロジェクトだとこういう作業は発生しない。

   To request that changes from your branch are merged into another branch, in
   the same repository or in another repository in the network, you can create a
   pull request on GitHub Desktop.

この動機が pull request の基本。

リモートからローカルブランチへの処理：

画面上中の :guilabel:`Current branch` ドロップダウンリストから対象のローカルブラ
ンチを選択し、画面上右の :guilabel:`Fetch origin` を押す。ここが :guilabel:`Pull
origin` 表記になっている場合、リモートにあるコミットなら何でもローカルへ持ってく
る。

ブランチのマージ処理：画面上中の :guilabel:`Current branch` ドロップダウンリスト
の最下部の :guilabel:`Choose a branch` ボタンを押す。マージするブランチを選択。

:menuselection:`Branch --> Rebase current branch...` では一方のブランチを他のブ
ランチに rebase する。これを実施すると画面右上の表記が :guilabel:`Force push
origin` になる。

:menuselection:`Branch --> Squash and merge into current branch...` は
``--squash`` マージする。

Viewing a pull request in GitHub Desktop
----------------------------------------------------------------------

   In GitHub Desktop, you can open (or "check out") the head branch of a pull
   request to view the changes a contributor is suggesting. For example, you can
   see a history of the commits that the contributor has made, and see which
   files the commits modified, added, or deleted.

..

   You cannot comment on a pull request from GitHub Desktop.

それはなぜか。

GitHub Desktop で pull request ブランチを開くには次のようにする：画面上中ドロッ
プダウンの :guilabel:`Pull requests` タブをクリック。

   When you have opened a pull request branch, you can view the contents of the
   branch in an editor, view the diff and commit history of the contributor's
   updates, and view and re-run checks.

GitHub サイトから pull request を GitHub Desktop で開くこともある。Pull request
画面の :menuselection:`Code --> Local --> Checkout with GitHub Desktop` を押す。

   You can view the commit history of the branch if you want to see how the
   contributor arrived at the set of changes they're suggesting.

:guilabel:`History` にある :guilabel:`Select Branch to Compare...` に pull
request の base ブランチを指示する。それから :guilabel:`Ahead` タブをクリックす
る。

:menuselection:`Branch --> View pull request on GitHub` で GitHub サイトの pull
request 画面が開く。

Viewing and re-running checks in GitHub Desktop
----------------------------------------------------------------------

   GitHub Desktop displays the status of checks that have run in your pull
   request branches. The checks badge next to the branch name will display the
   pending, passing, or failing state of the checks.

これは便利。Pull request ブランチ名の右にある番号をクリックする。

Configuring notifications in GitHub Desktop
----------------------------------------------------------------------

   GitHub Desktop will keep you up-to-date with notifications about events that
   occur in your pull request branch.

..

   Clicking the notification will display a dialog with details about the
   checks. Once you've reviewed why the checks have failed, you can re-run the
   checks, or quickly switch to the pull request branch to get started on fixing
   the errors.

メニュー :menuselection:`File --> Options...` の :menuselection:`Notifications
--> Enable notifications` をオンにする。さらに Windows 側の通知設定も手動で変更
する。

Changing the remote URL for a repository in GitHub Desktop
----------------------------------------------------------------------

メニュー :menuselection:`Repository --> Repository settings... --> Primary
remote repository` の URL を書き換えて :guilabel:`Save` を押す。
