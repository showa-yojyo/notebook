======================================================================
Pull requests documentation ノート
======================================================================

`Pull requests documentation <https://docs.github.com/en/pull-requests>`__ は
GitHub が生み出した文化、pull request に関する記述からなる。

.. contents::
   :depth: 3

* :guilabel:`Overview` は妙に深い節にある :ref:`About pull requests
  <pull-requests-overview>` へ

Committing changes to your project
======================================================================

Creating and editing commits
----------------------------------------------------------------------

About commits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Git assigns each commit a unique ID, called a SHA or hash

ファイルの SHA とは別のものとなる。

この後見ていくもの：

* 締結
* 共同作業者
* 組織
* コミット順序の変更

..

   You can see which branch a commit is on by looking at the labels beneath the
   commit on the commit page.

リポジトリーページの :guilabel:`(number) commits` を押し、コミット項目のログメッ
セージを押す。このページでブランチ名などを確認可能。

   If the commit is part of an unmerged pull request, you can click the link to
   go to the pull request.

コミットが複数ファイルを含むとき、ページ左側にツリーが表示される。

Creating a commit with multiple authors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   You can attribute a commit to more than one author by adding one or more
   ``Co-authored-by`` trailers to the commit's message.

これは知らなんだ。

共同コミット者の GitHub で通用するメールアドレスを知っている必要がある。例の
``no-reply`` アドレスを利用している場合はそれで通す。

Git では共同コミット者を指定するには、コミットログを次のように記入する。空行二つ
に注意：

.. code:: console

   bash$ git commit -m "Refactor usability tests.
   >
   >
   > Co-authored-by: NAME <NAME@EXAMPLE.COM>
   > Co-authored-by: ANOTHER-NAME <ANOTHER-NAME@EXAMPLE.COM>"

GitHub での方法はコミットログ欄で同様の書式を採用するようだ。

Creating a commit on behalf of an organization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

割愛。

Changing a commit message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   In Git, the text of the commit message is part of the commit. Changing the
   commit message will change the commit ID

GitHub にプッシュする前かつコミット直後なら ``git commit --amend -m MESSAGE`` で
事足りる。そうでない場合、ローカルで ``git rebase -i`` などでログメッセージを修
正し、プッシュし直す：

.. code:: console

   bash$ git push --force-with-lease origin BRANCH

..

   As before, amending the commit message will result in a new commit with a new
   ID. However, in this case, every commit that follows the amended commit will
   also get a new ID because each commit also contains the id of its parent.

Viewing and comparing commits
----------------------------------------------------------------------

Comparing commits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   To compare different versions of your repository, append ``/compare`` to your
   repository's path.

例えば ``https://github.com/octocat/linguist/compare/master...octocat:master``
のようにする。

比較は ``base`` と ``compare`` の対象二つを取る。

   The most common use of ``Compare`` is to compare branches, such as when
   you're starting a new pull request.

..

   To compare branches, you can select a branch name from the ``compare`` drop
   down menu at the top of the page.

タグ同士の比較も普通だ。リリースの差分を確認したい場合がある：

   To compare tags, you can select a tag name from the ``compare`` drop-down
   menu at the top of the page.

任意のコミットを比較する場合、URL を直接入力するほうが早い：

   For example, this URL uses the shortened seven-character SHA codes to compare
   commits ``f75c570`` and ``3391dcc``:
   ``https://github.com/github-linguist/linguist/compare/f75c570..3391dcc``.

リポジトリーをまたぐ比較もあり得る：

   To compare branches on different repositories, preface the branch names with
   user names.

Differences between commit views
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GitHub には次の二つのコミット情報表示方式があり、場合によっては表示が異なる：

   * Navigating directly to the commits page of a repository
   * Clicking on a file, then clicking :guilabel:`History`, to get to the commit
     history for a specific file

Troubleshooting commits
----------------------------------------------------------------------

Commit exists on GitHub but not in my local clone
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

誰かが ``git push --force`` した可能性などがある。

まず、念のため ``git fetch REMOTE`` する。

   You can use ``git fetch upstream`` to get information from a repository
   you've forked, or ``git fetch origin`` to get information from a repository
   you've only cloned.

誰かが対象コミットを含むブランチを削除した場合、一時的に当該ブランチを GitHubに
プッシュしてもらう：

.. code:: console

   bash$ git branch recover-B B
   bash$ git push upstream B:recover-B

その後、他の人が ``git fetch upstream recover-B`` する。

   Avoid force pushing to a repository unless absolutely necessary. This is
   especially true if more than one person can push to the repository.

Why are my commits linked to the wrong user?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

メールアドレスが関係している。

   If your commits are linked to another user, that means the email address in
   your local Git configuration settings is connected to that user's account on
   GitHub. In this case, you can change the email in your local Git
   configuration settings and add the new email address to your account on
   GitHub.com account to link future commits to your account.

アカウント :menuselection:`Settings --> Emails` ページを確認すること。

:guilabel:`GitHub Commits` ページ各項目に自分のコミットに自分の名前が出ない場合
は次のどれかになるようだ：

:guilabel:`Unrecognized author`
  メールありの場合となしの場合で対処が異なる。
:guilabel:`Invalid email`
  これはローカルの、つまり Git の ``user.email`` 設定がなされていない。

Collaborating with pull requests
======================================================================

Getting started
----------------------------------------------------------------------

About collaborative development models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   The way you use pull requests depends on the type of development model you
   use in your project. You can use the fork and pull model or the shared
   repository model.

二つ述べられている：

* Fork and pull model
* Shared repository model

ブランチをどのリポジトリーに設けるかが大きな差異であると見立てたが？

Working with forks
----------------------------------------------------------------------

About forks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A fork is a new repository that shares code and visibility settings with the
   original “upstream” repository.

特徴は次の二点に集約されるか：

   After you fork a repository, you can fetch updates from the upstream
   repository to keep your fork up to date, and you can propose changes from
   your fork to the upstream repository with pull requests.

GitHub 上では、フォークはその川上リポジトリーが名前の下に示される。

   After a fork is deleted, you cannot restore the fork.

特に、

   If you delete a private repository, all forks of the repository are deleted.

Pull request をしないつもりなら、用意されていればテンプレートから作成する手もあ
る。

About permissions and visibility of forks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   If you fork a private repository that belongs to a personal account, external
   collaborators also get access to the fork.

これは不思議な感じがある。

   You cannot change the visibility of a fork.

こういう概念がある：

   All repositories belong to a repository network.

フォークを扱う場合、自分のリポジトリーからのフォークを許可する場合、安全保障上考
慮する点がいくつもある。特に、川上リポジトリーの所有者はフォークに対して介入でき
ないと考える方がいい。

   The permissions and visibility of forks depend on whether the upstream
   repository is public or private, and whether it is owned by an organization.

さっきから次の条件が何かひっかかる：

   If you fork a private repository that belongs to a personal account, external
   collaborators also get access to the fork.

次の公開リポジトリーに対するフォークの公開性は明瞭：

   All forks of public repositories are public. You cannot change the visibility
   of a fork.

私設フォークの権限は川上リポジトリーのそれを継承する。ある意味では、川上の権限者
はフォークに口出しできるのか？

   Private forks inherit the permissions structure of the upstream repository.

Configuring a remote repository for a fork
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   You must configure a remote that points to the upstream repository in Git to
   sync changes you make in a fork with the original repository.

これは Git の基本なので必ず習得するべし。

.. code:: console

   bash$ git remote add upstream https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git

Syncing a fork
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

フォークリポジトリー画面の :guilabel:`Sync fork` を押す。

ローカルからコマンドで実行する方法がある：

.. code:: console

   bash$ gh repo sync owner/cli-fork -b BRANCH_NAME

Git では（この方法はフォークの意義をよく表していると思う）：

.. code:: console

   bash$ git fetch upstream
   bash$ git checkout main
   bash$ git merge upstream/main

Allowing changes to a pull request branch created from a fork
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   If the pull request author wants greater collaboration, they can grant
   maintainers of the upstream repository (that is, anyone with push access to
   the upstream repository) permission to commit to the pull request's compare
   branch.

フォーク側が川上に許可をすると読めるが？

GitHub の操作として、Pull request したい人が川上リポジトリーの :guilabel:`Pull
requests` 画面に行き、対象リクエストの :guilabel:`Allow edits from maintainers`
を押すらしい？

What happens to forks when a repository is deleted or changes visibility?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   When you delete a private repository, all of its private forks are also
   deleted.

ただしクローンならば維持される。

   When you delete a public repository, one of the existing public forks is
   chosen to be the new upstream repository.

この法則はリポジトリーネットワークと関係しているはず。

   If a public repository is made private, its public forks are split off into a
   new network.

この場合が複雑で、フォーク側の pull request 先が少なくとも本来の川上リポジトリー
ではなくなる。

Collaborating on repositories with code quality features
----------------------------------------------------------------------

ワークフロー品質管理とは？

About status checks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Status checks are based on external processes, such as continuous integration
   builds, which run for each push you make to a repository. You can see the
   pending, passing, or failing state of status checks next to individual
   commits in your pull request.

Pull request 欄に表示されるもので、通常のコミットには現れない？

   *Checks* are different from *statuses* in that they provide line annotations,
   more detailed messaging, and are only available for use with GitHub Apps.

..

   When *checks* are set up in a repository, pull requests have a
   :guilabel:`Checks` tab where you can view detailed build output from status
   checks and rerun failed checks.

Pull request 画面の :guilabel:`Checks` で確認。

   When a specific line in a commit causes a check to fail, you will see details
   about the failure, warning, or notice next to the relevant code in the
   :guilabel:`Files` tab of the pull request.

コミットの checks を省略させたり、要求させたりすることをコミットログで指示可能。
例によって二行の空行の後に指示をする：

.. code:: console

   bash$ git commit -m "Refactor usability tests
   >
   >
   request-checks: true"

Troubleshooting required status checks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   After you enable required status checks, your branch may need to be
   up-to-date with the base branch before merging.

..

   You won't be able to push local changes to a protected branch until all
   required status checks pass.

手堅い。

   Sometimes, the results of the status checks for the test merge commit and
   head commit will conflict.

これはプロジェクト進行が怪しいのではないか。

この辺りは後ほど。

Proposing changes to your work with pull requests
----------------------------------------------------------------------

これが本題なのでは。

About branches
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Typically, you might create a new branch from the default branch of your
   repository. You can then work on this new branch in isolation from changes
   that other people are making to the repository. A branch you create to build
   a feature is commonly referred to as a feature branch or topic branch.

ブランチは本体から孤立させる役目がある。トピックブランチには同義語が多い。

   You can also use a branch to publish a GitHub Pages site.

これは別の章でやる。

次は既定ブランチの定義であり、GitHub 固有の概念と考える方がいい：

   The default branch is the branch that GitHub displays when anyone visits your
   repository. The default branch is also the initial branch that Git checks out
   locally when someone clones the repository.

Pull request を始める：

   Once you're satisfied with your work, you can open a pull request to merge
   the changes in the current branch (the head branch) into another branch (the
   base branch).

Pull request が完了したら、用済みブランチを削除する。

保護ブランチは、それがなければどういうことがあり得るかを理解するのがいい：

   If you're working on a branch that's protected, you won't be able to delete
   or force push to the branch.

保護ブランチの性質はたくさんある。次に挙げる項目のうち、最初のもの以外は設定によ
る：

* ブランチに対する削除、強制 push は不可。
* CI 試験に合格するまでマージ不可。
* 評価がなされるまではマージ不可。
* コード所有者が許可するまでマージ不可。
* 署名と検証がないものはマージ不可。

Creating and deleting branches within your repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ブランチを GitHub で作成、削除する方法。割愛。

   If the branch you want to delete is associated with an open pull request, you
   must merge or close the pull request before deleting the branch.

ブランチに関連する未済 pull requests を道連れに削除する。

.. _pull-requests-overview:

About pull requests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pull request は次の用途を想定した操作だ：

* GitHub 上のリポジトリーでブランチに push した変更を他の人に伝える。
* 協力者と変更の可能性について議論、確認する。
* 変更が base ブランチにマージされる前に、さらに関連コミットを追加する。

Pull request は GitHub 上の操作なので、Git 単体ではなく GitHub ツールで実施す
るものだ。

   After initializing a pull request, you'll see a review page that shows a
   high-level overview of the changes between your branch (the compare branch)
   and the repository's base branch.

ここで compare と base を術語と捉え、pull requests 関連文書の読み込みを効率的に
したい。

   Once you've created a pull request, you can push commits from your topic
   branch to add them to your existing pull request. These commits will appear
   in chronological order within your pull request and the changes will be
   visible in the :guilabel:`Files changed` tab.

ブランチをマージするのが目的なので、コミットは一般に複数あってかまわないというこ
とだ。

他の協力者たちはこのようなブランチに対して評価することが可能。コミットを追加する
ことさえ可能。

   You can see information about the branch's current deployment status and past
   deployment activity on the :guilabel:`Conversation` tab.

会話タブで配備状態を確認できるというのは不思議な感じがする？

   After you're happy with the proposed changes, you can merge the pull request.

マージ完了をもってブランチ作成者の目的は果たされる。

Draft pull requests という機能がある：

   When you create a pull request, you can choose to create a pull request that
   is ready for review or a draft pull request. Draft pull requests cannot be
   merged, and code owners are not automatically requested to review draft pull
   requests.

マージ可否と審査の有無が通常と下書きの違いだと読める。

   The compare and pull request pages use different methods to calculate the
   diff for changed files:

差分の違いが少し理解しにくい。評価時は後者の差分を使い、マージ時には前者の差分が
本質的ということか？

About comparing branches in pull requests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* :guilabel:`Files changed` を押すと差分が表示される画面になる。
* 差分表示モードがいくつかある。
* 大規模 pull request の概要をつかむために、各種フィルターを利用する。

..

   There are two comparison methods for the git diff command; two-dot
   (``git diff A..B``) and three-dot (``git diff A...B``). By default, pull
   requests on GitHub show a three-dot diff.

   The three-dot comparison shows the difference between the latest common
   commit of both branches (merge base) and the most recent version of the topic
   branch.

この記述だとまだわかりづらい。

   Since the three-dot comparison compares with the merge base, it is focusing
   on "what a pull request introduces".

..

   In contrast, by comparing the branches using the three-dot comparison,
   changes in the topic branch are always in the diff if the base branch is
   updated, because the diff shows all of the changes since the branches
   diverged.

これでようやく理解できる。そしてマージはしょっちゅう行うほうが良い：

   To avoid getting confused, merge the base branch (for example, main) into
   your topic branch frequently. By merging the base branch, the diffs shown by
   two-dot and three-dot comparisons are the same.

Creating a pull request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

対象リポジトリーに書き込み権限がない場合、それをフォークするところから始める。

   Pull requests can only be opened between two branches that are different.

用語を二つ確認する：

   When thinking about branches, remember that the *base branch* is where
   changes should be applied, the *head branch* contains what you would like to
   be applied.

:guilabel:`Compare & pull request` ボタンを押す。それから :guilabel:`Create Pull
Request` を押す。

GitHub CLI でも作成可能だ。コマンドラインオプションにブランチは指定したい：

.. code:: console

   bash$ gh pr create \
     --base my-base-branch --head my-changed-branch \
     --title "The bug is fixed" \
     --body "Everything works again" \
     --label "bug,help wanted" \
     --reviewer monalisa,hubot

Creating a pull request from a fork
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   If your pull request compares your topic branch with a branch in the upstream
   repository as the base branch, then your topic branch is also called the
   compare branch of the pull request.

トピックブランチと比較ブランチは同じ概念だと考えて支障はない。

まず、フォーム元リポジトリーページを開く。ファイル一覧の上にあるボタン
:guilabel:`Compare & pull request` を押す。:guilabel:`Open a pull request` ペー
ジが開く。そこに小さく書いてある :guilabel:`compare across forks` を押す。

* ``base``: 川上
* ``head``: compare ブランチ

:guilabel:`Allow edits from maintainers` を押す。:guilabel:`Create Pull Request`
を押せるように進む。

Using query parameters to create a pull request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Use query parameters to create custom URLs to open pull requests with
   pre-populated fields.

HTTP リクエストで pull request を開く。これを使うぐらいなら GitHub CLI
でいいだろう。

Changing the stage of a pull request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   You can mark a draft pull request as ready for review or convert a pull
   request to a draft.

* 下書きの :guilabel:`Ready for review` を押す。
* Pull request の :guilabel:`Convert to draft` を押す。

Requesting a pull request review
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   After you create a pull request, you can ask a specific person to review the
   changes you've proposed.

..

   Owners and collaborators on a repository owned by a personal account can
   assign pull request reviews.

   Suggested reviewers are based on ``git blame`` data.

:guilabel:`Reviewers` 欄を見ればわかる？

Keeping your pull request in sync with the base branch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Updating your pull request with the latest changes from the base branch can
   help catch problems prior to merging.

これはさっき述べられた。

:guilabel:`Pull requests` 画面のリクエスト項目にある :guilabel:`Update branch`
などを押す。ドロップダウンリストにマージオプションがある。

Changing the base branch of a pull request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   After a pull request is opened, you can change the base branch to compare the
   changes in the pull request against a different branch.

この機能は要るのか？

Committing changes to a pull request branch created from a fork
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   You can commit changes on a pull request branch that was created from a fork
   of your repository with permission from the pull request creator.

Git 操作で当該ブランチをローカルにクローンして、普通にコミットする。

Addressing merge conflicts
----------------------------------------------------------------------

マージ衝突の解決方法と見ていく？

About merge conflicts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Often, merge conflicts happen when people make different changes to the same
   line of the same file, or when one person edits a file and another person
   deletes the same file.

それ以外の違いは Git が自然に解消してくれる。

   The :guilabel:`Merge pull request` button is deactivated until you've
   resolved all conflicts between the compare branch and base branch.

衝突の解消は手動による編集が基本だ。

衝突を解消するまで、そのブランチの作業は先に進めないとみなしていい。

Resolving a merge conflict on GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   You can resolve simple merge conflicts that involve competing line changes on
   GitHub, using the conflict editor.

衝突解消のための専用編集ツールを使う場合。

:guilabel:`Pull requests` 画面の :guilabel:`Resolve conflicts` を押す。このボタ
ンがグレーになっているときは GitHub でもお手上げという複雑な衝突であるので、ほん
とうに手作業でやるしかない。次節参照。

ファイル内の衝突をすべて解決したら :guilabel:`Mark as resolved` を押す。

最後の一つ前の段階で、マージ先のブランチをもう一度確認する。マージ先のブランチが
わからずに衝突解消作業をしていたわけではないのだが。

最終的に :guilabel:`Merge pull request` ボタンを押せるようにする。

Resolving a merge conflict using the command line
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

この節は GitHub とは独立して理解する。

コマンドラインとテキストエディターで解消するのが基本だ。``git status`` すると
``both modified`` であるファイルが含まれているはず。

エディターで衝突マークが追加されたファイルを目と手で編集する。ファイルを保存した
ら Git でコミットする。これでブランチが正常化する。

ファイル自体が衝突する場合（削除や改名）はテキスト編集というより Git コマンドで
解消する。``git add``, ``git rm`` などを確定する。

Reviewing changes in pull requests
----------------------------------------------------------------------

   After a pull request has been opened, you can review and discuss the set of
   proposed changes.

一連の文書で現れる各文章の代名詞主語が誰を指しているのか不明瞭な場合が多いのが気
になる。

About pull request reviews
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

評価：コメント、許可、要求

   You can define which individuals or teams own certain types or areas of code
   in a :file:`CODEOWNERS` file.

急所：

   A review has three possible statuses:

   * :guilabel:`Comment`: Submit general feedback without explicitly approving
     the changes or requesting additional changes.
   * :guilabel:`Approve`: Submit feedback and approve merging the changes
     proposed in the pull request.
   * :guilabel:`Request changes`: Submit feedback that must be addressed before
     the pull request can be merged.

マージ可かどうかを見分ける方法：

   If your repository requires approving reviews from people with ``write`` or
   ``admin`` permissions, then any approvals from people with these permissions
   are denoted with a green check mark, and approvals from people without these
   permissions have a gray check mark. Approvals with a gray check mark do not
   affect whether the pull request can be merged.

:guilabel:`Conversation` にも解消状態が存在する：

   To indicate that a conversation on the :guilabel:`Files changed` tab is
   complete, click :guilabel:`Resolve conversation`.

:guilabel:`Files changed` タブの左下辺りに :guilabel:`Conversations` を押すと会
話があれば出る。

評価を再依頼することが可能。

Reviewing proposed changes in a pull request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

現行のコードの差分を確認しながら批評する。

   While reviewing the files in a pull request, you can leave individual
   comments on specific changes. After you finish reviewing each file, you can
   mark the file as viewed.

これで見逃しがないことを期待する。

:guilabel:`Files changed` タブのすぐ下辺りの歯車アイコンで差分表示を
:guilabel:`united` か :guilabel:`split` か選ぶ。

差分の chunk ごとにコメントを付すことが可能。

:guilabel:`Start a review` や :guilabel:`Add review comment` を押す。

   If the pull request contains changes to dependencies you can use the
   dependency review for a manifest or lock file to see what has changed and
   check whether the changes introduce security vulnerabilities.

この種の差分は :guilabel:`rich diff` を押すと特殊な表示となる。バージョンが目立
つような。

   After you finish reviewing a file, you can mark the file as viewed, and the
   file will collapse. If the file changes after you view the file, it will be
   unmarked as viewed.

:guilabel:`Viewed` にチェックがつく。

:guilabel:`Review changes` を押して :guilabel:`Submit review` を押せば評価完了。

Filtering files in a pull request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   To help you quickly review changes in a large pull request, you can filter
   changed files or use the file tree to navigate between files.

大規模な変更はもらいたくないものだ。

:guilabel:`Files changed` タブ下メニューにある :guilabel:`File filter` を押す
と、いい感じのフィルターオプションが現れる。

Finding changed methods and functions in a pull request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   You can quickly find proposed changes to a method or function in a pull
   request in ``.go``, ``.js``, ``.ts``, ``.py``, ``.php``, and ``.rb`` files.

怪しい触れ込みだ。

:menuselection:`Files changed --> Jump to` のドロップダウンリストに関数一覧が現
れるようだ。

Commenting on a pull request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

何度も見てきたように：

   You can comment on a pull request's :guilabel:`Conversation` tab to leave
   general comments, questions, or props. You can also suggest changes that the
   author of the pull request can apply directly from your comment.

:menuselection:`Files changed --> Conversations` でその pull request の会話すべ
てを見つけられる。

Viewing a pull request review
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Conversation` ページの下部、:guilabel:`View all changes` を押す。

Reviewing dependency changes in a pull request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   If a pull request contains changes to dependencies, you can view a summary of
   what has changed and whether there are known vulnerabilities in any of the
   dependencies.

そして前に習ったように：

   It provides an easily understandable visualization of dependency changes with
   a rich diff on the :guilabel:`Files Changed` tab of a pull request.

この評価で得られる情報とは：

   * Which dependencies were added, removed, or updated, along with the release
     dates.
   * How many projects use these components.
   * Vulnerability data for these dependencies.

次のような特別アクションがある：

   You can use the dependency review action to help enforce dependency reviews
   on pull requests in your repository.

表示順序で優遇される：

   Any added or changed dependencies that have vulnerabilities are listed first,
   ordered by severity and then by dependency name. This means that the highest
   severity dependencies are always at the top of a dependency review.

Incorporating feedback in your pull request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

評価者が pull request に対して変更を提案するとどうなるか。

   you can also apply suggested changes if you have write access to the upstream
   repository.

これがわからない。誰が適用できるのか。

   Applying one suggested change or a batch of suggested changes creates a
   single commit on the compare branch of the pull request.

実質的には当該 pull request に対して新規コミットが加わる。さらに、

   Each person who suggested a change included in the commit will be a co-author
   of the commit.

やり方は？

:guilabel:`Commit suggestion` と :guilabel:`Add suggestion to batch` を押す。

Approving a pull request with required reviews
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

評価が必要かどうかはリポジトリーの性質らしい。

   If a pull request you approved has changed significantly, you can dismiss
   your review.

Pull request を提出した者が評価結果を却下可能だと読める。次の節で述べられる
ものか。

:guilabel:`Approve` からの :guilabel:`Submit review` で評価は終わる。

   Pull request authors cannot approve their own pull requests.

この条件と矛盾する条件を考える。

Dismissing a pull request review
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   If your repository requires reviews, you can dismiss pull request reviews
   that are no longer valid or are unable to be approved by the reviewer.

ああ、却下するというのは自分の提出を撤回するということか。

   When you dismiss a review, you must add a comment explaining why you
   dismissed it. Your comment will be added to the pull request conversation.

却下するには :guilabel:`Dismiss review` を押す。弁解を記入する必要がある。

Checking out pull requests locally
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   When someone sends you a pull request from a fork or branch of your
   repository, you can merge it locally to resolve a merge conflict or to test
   and verify the changes before merging on GitHub.

この話題が最後ということは、この手法は主流ではないということか。

休眠 pull request を再生するには、pull request ID がわかっていれば、次のコマン
ドでコードを得られる：

.. code:: console

   bash$ git fetch origin pull/ID/head:BRANCH_NAME

このブランチで作業を引き継いでプッシュすれば pull request を新しい ID で再発行可
能となる。

   The remote ``refs/pull/`` namespace is read-only.

したがって、ここにはプッシュできない。

GitHub CLI が使えるなら：

.. code:: console

   bash$ gh pr checkout PULL-REQUEST

Incorporating changes from a pull request
----------------------------------------------------------------------

   You can propose changes to your work on GitHub through pull requests. Learn
   how to create, manage, and merge pull requests.

About pull request merges
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

基本的には ``git merge`` の様式の議論だ。

   When you click the default :guilabel:`Merge pull request` option on a pull
   request on GitHub.com, all commits from the feature branch are added to the
   base branch in a merge commit. The pull request is merged using the
   ``--no-ff`` option.

マージオプション ``--no-ff`` がオンであるということを承知しおく。

   When you select the :guilabel:`Squash and merge` option on a pull request on
   GitHub.com, the pull request's commits are squashed into a single commit.

作業途中のコミットが含まれているブランチだから、それらを縮合していいと考える。こ
ちらは ``--ff`` でマージ。

   When you squash and merge, GitHub generates a default commit message, which
   you can edit.

Git の生成する既定メッセージと異なる。

   If you plan to continue work on the head branch of a pull request after the
   pull request is merged, we recommend you don't squash and merge the pull
   request.

なるほど。``--squash`` を多用する作業では衝突を生じやすい。

   When you select the :guilabel:`Rebase and merge` option on a pull request on
   GitHub.com, all commits from the topic branch (or head branch) are added onto
   the base branch individually without a merge commit.

ただし、次の仕様上の事実に注意する：

   The rebase and merge behavior on GitHub deviates slightly from ``git
   rebase``.

あとは間接的マージという概念の記述。割愛。

Merging a pull request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

マージの基本的な考え方：

   In a pull request, you propose that changes you've made on a head branch
   should be merged into a base branch. By default, any pull request can be
   merged at any time, unless the head branch is in conflict with the base
   branch.

他にも状態チェックやブランチ保護などの条件もある。全てクリアできていれば：

   You can configure a pull request to merge automatically when all merge
   requirements are met.

マージ衝突の解消を Git 操作で（ブラウザーでもコンソールでも他でも）行う。解消し
たらマージ。最終的に作業用ブランチは不要になる。

   The repository may be configured so that the head branch for a pull request
   is automatically deleted when you merge a pull request.

自動処理設定をオンにしておく。

マージでは通常 ``git merge --no-ff`` コマンドが働く。

   You can link a pull request to an issue to show that a fix is in progress and
   to automatically close the issue when someone merges the pull request.

このページに GitHub 上のマージ手順が記載されている。

#. リポジトリー :menuselection:`Pull requests` ページで pull request を一つ選
   ぶ。
#. ページ下部の :guilabel:`Merge pull request` ドロップダウンからマージ方法を選
   択してボタンを押す。
#. コミットメッセージを整える。
#. 場合によっては（マージコミット作成時）提出者のメールアドレスを指定する。
#. :guilabel:`Confirm` ボタンを押す。
#. 不要になったブランチを削除する。

GitHub CLI で処理することも可能。このようにするようだ：

.. code:: console

   gh pr merge MERGE_ID \
     --squash \
     --body COMMIT_MESSAGE \
     --delete-branch

Automatically merging a pull request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

自動マージ有効化について。

   If you enable auto-merge for a pull request, the pull request will merge
   automatically when all required reviews are met and all required status
   checks have passed.

自動マージを有効にしていても、一定の状況下で無効になる。

   For example, if a maintainer enables auto-merge for a pull request from a
   fork, auto-merge will be disabled after a contributor pushes new changes to
   the pull request.

有効化設定は pull request ごとに対しての操作だ。自動マージを有効化したい pull
request 画面を開く。

Merging a pull request with a merge queue
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

マージを待っている行列がある。ステータスチェックを待つ必要がない。

   Using a merge queue is particularly useful on branches that have a relatively
   high number of pull requests merging each day from many different users.

だからウチには要らない。

ステータスチェックが終わっている Pull request 画面の :guilabel:`Merge when
ready` を押す。反対に、キューから除きたくなったら :guilabel:`Remove from queue`
を押す。

マージキューを観察するにはブランチページを開く。キューが空でなければリンクがある
はず。

マージキューから pull request が削除される場合がある。理由はタイムラインから確認
可能。

Closing a pull request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   You may choose to close a pull request without merging it into the upstream
   branch.

閉じる前に次をチェック：

   Tip: If you opened a pull request with the wrong base branch, rather than
   closing it out and opening a new one, you can instead change the base branch.

Pull request 画面を開いて :guilabel:`Close pull request` を押す。場合によっては
専用ブランチを削除する。

Reverting a pull request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

これはマージ後の取り消しを念頭に置いている。

   Reverting a pull request on GitHub creates a new pull request that contains
   one revert of the merge commit from the original merged pull request.

考え方は ``git revert`` と同様だろう。

:guilabel:`Conversation` 画面のタイムラインにおけるマージ項目右側
:guilabel:`Revert` ボタンを押す。
