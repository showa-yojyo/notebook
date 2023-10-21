======================================================================
GitHub Issues documentation
======================================================================

`GitHub Issues documentation <https://docs.github.com/en/issues>`__ を読んでこの
機能を理解し、上手に利用する。

.. contents::
   :depth: 3

* :guilabel:`Overview` → :ref:`About issues <issues-overview>`
* :guilabel:`Quickstart` → :ref:`Quickstart for GitHub Issues
  <issues-quickstart>`

Tracking your work with issues
======================================================================

.. _issues-overview:

About issues
----------------------------------------------------------------------

   To indicate that work is in progress, you can link an issue to a pull
   request. When the pull request merges, the linked issue automatically closes.

これは気づかなんだ。

   Issues can be created in a variety of ways, so you can choose the most
   convenient method for your workflow.

リポジトリーから作成するのが普通だが、それ以外の方法がたくさんある。

   To track issues as part of a larger issue, you can use task lists. To
   categorize related issues, you can use labels and milestones.

Issue を出して時間が経ってから、想定より大きい問題だと気づきがちだ。そういう場合
に課題一覧を利用して、問題を分割する。分割統治法。

   To quickly find links to recently updated issues you're subscribed to, visit
   your dashboard.

よそのリポジトリーのバグ修正状況を追いたい場合はある。

   To help contributors open meaningful issues that provide the information that
   you need, you can use issue forms and issue templates.

テンプレートをそういうふうに利用するのか。

コメント欄で ``@`` や ``#`` を使える。

   When a conversation in an issue is better suited for a discussion, you can
   convert the issue to a discussion.

これをすぐにでも試したい。

.. _issues-quickstart:

Quickstart for GitHub Issues
----------------------------------------------------------------------

あるリポジトリーに対して Issues を利用するには、次の二つが必要：

* 対象リポジトリーに対して write 権限がある利用者である
* 対象リポジトリーが Issues 機能を有効にしている

まず空の issue の作り方を習う。いつでも言えることだが：

   There are multiple ways to create an issue; you can choose the most
   convenient method for your workflow.

GitHub ならリポジトリー :menuselection:`Issues --> New issue`. なぜわざわざ空と
断るかというと、テンプレートが用意されたリポジトリーがあるからだ：

   Your repository may use issue templates and issue forms to encourage
   contributors to provide specific information. If your repository uses issue
   templates, click :guilabel:`Open a blank issue`.

フォームを埋める。

   For example, if this is a bug report, describe the steps to reproduce the
   bug, the expected result, and the actual result.

ここで task list を定義することが可能：

   Add a task list to your issue by prefacing list items with ``[ ]``.

角括弧の中は空白文字。次の例のようにリストを書き込むと、プレビューあるいは投稿後
の表示ではチェックボックス付きのリストとして描画される：

.. code:: markdown

   - [ ] #70
   - [ ] https://github.com/oct-org/oct-repo/issues/1752
   - [ ] Update aliens and cannon game logic

課題リストについては後述。

   Add a label to categorize your issue.

Issue フォーム右柱を見ろ。バグ報告なら ``bug`` を、機能改善なら ``enhancement``
をそれぞれ付けるといった具合だ。ラベルを複数付けることも可能だ。

   You can add a milestone to track the issue as part of a date based target. A
   milestone will show the progress of the issues as the target date approaches.

マイルストーンの意味は後述。対象期間にどれだけの issues が片付くかを知るための材
料だ。

   To communicate responsibility, you can assign the issue to a member of your
   organization.

孤独のリポジトリーでは不要。自動的に所有者に割り当てる機能があるとうれしい。

   You can add the issue to an existing project and populate metadata for the
   project.

プロジェクトに関する章が別にあり、大量の文書からなる。

Issue を提出するタイミングはわりと柔軟だ：

   Click :guilabel:`Submit new issue` to create your issue. You can edit any of
   the above fields after creating the issue.

投稿された issue にコメントを加えることが可能だ。

Creating an issue
----------------------------------------------------------------------

上述の Issue 画面から以外の作成方法を知る。

GitHub CLI から作成する：

.. code:: console

   bash$ gh issue create --title "My new issue" --body "Here are more details."
   bash$ gh issue create \
     --title "My new issue" \
     --body "Here are more details." \
     --assignee @me,monalisa \
     --label "bug,help wanted" \
     --project onboarding \
     --milestone "learning codebase"

..

   You can open a new issue from a comment in an issue or pull request.

Issue に付いているコメントの :menuselection:`... --> Reference in new issue` を
押す。フォームを埋めて :guilabel:`Create issue` を押す。新 Issue 画面が出る。

   You can open a new issue from a specific line or lines of code in a file or
   pull request.

リポジトリーにあるファイルまたは pull request のファイルにあるコードを表示する。
次に目的の行の番号を選択する。範囲になるならば複数行可。:menuselection:`... -->
Reference in new issue` を押す。新 Issue 画面が出る。

   When you create an issue from a discussion, the contents of the discussion
   post will be automatically included in the issue body, and any labels will be
   retained. Creating an issue from a discussion does not convert the discussion
   to an issue or delete the existing discussion.

リポジトリー :guilabel:`Discussions` ページの項目から :guilabel:`Create issue
from discussion` を押す。フォームを埋めて :guilabel:`Submit new issue` を押す。

   You can quickly create issues without leaving your project. When using a view
   that is grouped by a field, creating an issue in that group will
   automatically set the new issue's field to the group's value.

プロジェクトは大掛かりな GitHub 機能なので別に章が設けられている。

   Within an issue, you can use task lists to break work into smaller tasks and
   track the full set of work to completion.

これを issues に変換可能。項目上にマウスをホバーさせると右側にマルが描かれる。ク
リックすると変換。課題一覧は元 issue の description 内にある必要があるらしく、コ
メントに課題一覧を書いても上記のような挙動にはならない。

   You can use query parameters to open issues.

..

   You must have the proper permissions for any action to use the equivalent
   query parameter.

ただ、これは URL を組み立てるのが面倒。利用しないと思う。

   If you're using issues to track and prioritize your work, you can use issues
   to track code scanning alerts.

高度な手順。

About slash commands
----------------------------------------------------------------------

   Slash commands make it easier to type more complex Markdown, such as tables,
   tasklists, and code blocks.

記述欄、コメント欄の入力中に ``/code`` などとタイプすると入力支援（補完機能）が
作動する：

* ``/code``
* ``/details``
* ``/savedreplies``
* ``/table``
* ``/tasklist``: Issue 作成時に動く？
* ``/template``: テンプレート中で動く？

Linking a pull request to an issue
----------------------------------------------------------------------

   You can link an issue to a pull request manually or using a supported keyword
   in the pull request description.

この節で述べられるものが機能するには、pull requests は既定ブランチに対するもので
ある必要がある。

   When you merge a linked pull request into the default branch of a repository,
   its linked issue is automatically closed.

これは便利。リンク方法は：

   You can link a pull request to an issue by using a supported keyword in the
   pull request's description or in a commit message.

キーワードを書くのはコミットログでもいい。さらに、

   Merging the referencing pull request also closes the referenced pull request.

キーワードは ``close``, ``fix``, ``resolve`` など。構文は本文参照。複数 issues
を参照するときにはキーワードも複数書くようだ。

   You can manually link up to ten issues to each pull request. The issue and
   pull request must be in the same repository.

Pull request 画面右柱の :guilabel:`Development` を押すと issues 一覧が現れる。そ
こから選ぶ。Issues からも同様の手順で pull request にリンクさせられる。

Creating a branch to work on an issue
----------------------------------------------------------------------

   You can create a branch to work on an issue directly from the issue page and
   get started right away.

作業の流れとして自然なのがいい。

   Branches connected to an issue are shown under the "Development" section in
   the sidebar of an issue. When you create a pull request for one of these
   branches, it is automatically linked to the issue. The connection with that
   branch is removed and only the pull request is shown in the "Development"
   section.

対象 issue の右柱 :menuselection:`Development --> Create a branch` を押す。
フォームを埋めて :guilabel:`Create branch` を押す。

ここで :guilabel:`Checkout locally` オプションで終わると Git コマンドが現れる。
ローカルでコマンドを実行して作業をするのが無難か。

Assigning issues and pull requests to other GitHub users
----------------------------------------------------------------------

   You can assign multiple people to each issue or pull request

孤独のリポジトリーだと複数人に割り当てられることに気づかない。

また、同時に一人に複数項目を割り当てられる。一覧の左に並んでいるチェックボックス
を使う。

Viewing all of your issues and pull requests
----------------------------------------------------------------------

   Your issue and pull request dashboards are available at the top of any page.

受信箱の左が Issues ボタンと Pull requests ボタンだ。

Filtering and searching issues and pull requests
----------------------------------------------------------------------

   Issues and pull requests come with a set of default filters you can apply to
   organize your listings.

テキストで検索するというより、フィルターを主に使う。一覧画面の虫眼鏡の左にフィル
ターがある。

   Once you've assigned an issue or pull request to someone, you can find items
   based on who's working on them.

一覧ヘッダー右上にある :guilabel:`Assignee` を押す。

   The issues and pull requests search bar allows you to define your own custom
   filters and sort by a wide variety of criteria.

虫眼鏡入力欄。特殊な文字列で検索してもよい。``is:open is:pr author:showa-yojyo``
など。

   Filters can be sorted to provide better information during a specific time
   period.

一覧ヘッダー右上の :guilabel:`Sort` を押す。基準を順序一覧から指定する。

   When you filter or sort issues and pull requests, your browser's URL is
   automatically updated to match the new view.

検索実行後にブラウザーの URL を他人に渡せばいい。

Marking issues or pull requests as a duplicate
----------------------------------------------------------------------

   To mark an issue or pull request as a duplicate, type "Duplicate of" followed
   by an issue or pull request number in the body of a new comment.

専用の UI があるわけではない。

   You can unmark duplicate issues and pull requests by clicking
   :guilabel:`Undo` in the timeline.

Pinning an issue to your repository
----------------------------------------------------------------------

   You can pin up to three important issues above the issues list in your
   repository.

Issue 画面右列の :guilabel:`Pin issue` を押す。

Transferring an issue to another repository
----------------------------------------------------------------------

   Note: You can only transfer issues between repositories owned by the same
   user or organization account. A private repository issue cannot be
   transferred to a public repository.

..

   When you transfer an issue, comments and assignees are retained. Labels and
   milestones are also retained if they're present in the target repository,
   with labels matching by name and milestones matching by both name and due
   date.

Issue 画面右列の :guilabel:`Transfer issue` を押す。移動先のリポジトリーを選んで
:guilabel:`Transfer issue` を押す。

Closing an issue
----------------------------------------------------------------------

コメント内キーワードを使わない方法。

Issue 画面最後の :guilabel:`Close issue` を押す。ドロップダウンにするとオプショ
ン。

Deleting an issue
----------------------------------------------------------------------

削除処理は強い。

   Collaborators do not receive a notification when issues are deleted.

Issue 画面右列の :guilabel:`Delete issue` を押す。

Planning and tracking work for your team or project
----------------------------------------------------------------------

   In this guide, you will learn how to create and set up a repository for
   collaborating with a group of people, create issue templates and forms, open
   issues and use task lists to break down work, and establish a project board
   for organizing and tracking issues.

ここは一般論のページ。

   When starting a new project, initiative, or feature, the first step is to
   create a repository.

リポジトリーにも分類があると言っている：

* Product repositories
* Project repositories
* Team repositories
* Personal repositories

権限にうるさい人には：

   You can create multiple, separate repositories if you want different access
   permissions for the source code and for tracking issues and discussions.

これまで何度も何度も言われているように :file:`README` は重要。

   A README is often the first item a visitor to your repository will see, so
   you can also provide information on how users or contributors can get started
   with the project and how to contact the team.

参加者向けにもう一つ、:file:`CONTRIBUTING.md` も用意する：

   You can also create a :file:`CONTRIBUTING.md` file specifically to contain
   guidelines on how users or contributors can contribute and interact with the
   team or project, such as how to open a bug fix issue or request an
   improvement.

テンプレート：

   Once you have identified the most common issue types for your team, you can
   create issue templates and forms for your repository. Issue templates and
   forms allow you to create a standardized list of templates that a contributor
   can choose from when they open an issue in your repository.

テンプレートは複数用意可能？

   Task lists have additional functionality when added to the body of an issue.

さっき見た。

   Issues are useful when you create them for discussion of specific details,
   such as bug or performance reports, planning for the next quarter, or design
   for a new initiative. Discussions are useful for open-ended brainstorming or
   feedback, outside the codebase and across repositories.

..

   You can create labels for a repository to categorize issues, pull requests,
   and discussions.

ラベルを新規作成することはほとんどなかった。本文では ``front-end`` という、それ
らしいものを定義している。

   A project is a customizable spreadsheet that integrates with your issues and
   pull requests on GitHub, automatically staying up-to-date with the
   information on GitHub.

Planning and tracking with Projects
======================================================================

→ :doc:`./projects`

Managing your issues with tasklists
======================================================================

→ :doc:`./tasklists`

Organizing your work with projects (classic)
======================================================================

これは古びているので割愛。

Using labels and milestones to track work
======================================================================

これは平易なので省略しても問題ない。

Managing labels
----------------------------------------------------------------------

   You can manage your work on GitHub by creating labels to categorize issues,
   pull requests, and discussions. You can apply labels in the repository the
   label was created in.

GitHub が標準ラベルと規定しているものは次のものだ。意味を誤解しそうなものもあ
る：

* :guilabel:`bug`
* :guilabel:`documentation`
* :guilabel:`duplicate`
* :guilabel:`enhancement`
* :guilabel:`good first issue`
* :guilabel:`help wanted`
* :guilabel:`invalid`: もう無関係になったことを示す
* :guilabel:`question`: より多くの情報を要することを示す
* :guilabel:`wontfix`: 作業が続行されないことを示す

..

   Issues with the :guilabel:`good first issue` label are used to populate the
   repository's contribute page.

ラベル作成方法：Issues または Pull requests 画面の検索欄右にある
:guilabel:`Labels` を押す。ラベル一覧画面が現れる。ここで :guilabel:`New label`
を押す。フォームを埋めて :guilabel:`Create label` を押す。

ラベル編集方法：ラベル一覧の対象項目右にある :guilabel:`Edit` を押す。作成時の画
面が現れる。フォームを埋めて :guilabel:`Save changes` を押す。

ラベル削除方法：ラベル一覧の対象項目右にある :guilabel:`Delete` を押す。

About milestones
----------------------------------------------------------------------

   When you create a milestone, you can associate it with issues and pull
   requests.

マイルストーンとは締切日のような概念だと考えられる：

   From the milestone page, you can see:

   * A user-provided description of the milestone, which can include information
     like a project overview, relevant teams, and projected due dates
   * The milestone's due date
   * The milestone's completion percentage
   * The number of open and closed issues and pull requests associated with the
     milestone
   * A list of the open and closed issues and pull requests associated with the
     milestone

そして issues と pull requests に優先度を与えることが可能だ：

You can prioritize open issues and pull requests in a milestone by clicking to
the left of an issue or pull request's checkbox, dragging it to a new location,
and dropping it.

Creating and editing milestones for issues and pull requests
----------------------------------------------------------------------

#. Issues または Pull requests 画面の検索欄右にある :guilabel:`Milestones` を押
   す。
#. 作成する場合は :guilabel:`New milestone` を、編集する場合は対象項目枠内のリン
   ク :guilabel:`Edit` をそれぞれ押す。削除する場合はリンク :guilabel:`Delete`
   を押す。
#. フォームを埋めて作成の場合は :guilabel:`Create milestone` を、編集の場合は
   :guilabel:`Save changes` をそれぞれ押す。

Associating milestones with issues and pull requests
----------------------------------------------------------------------

#. Issues または Pull requests 一覧で、マイルストーンを設定したい項目にチェック
   を入れる。
#. 一覧表ヘッダー右上の :guilabel:`Milestones` ドロップダウンリストを押し、設定
   したいマイルストーンを押す。

Filtering issues and pull requests by milestone
----------------------------------------------------------------------

Issues または Pull requests 画面の検索欄右にある :guilabel:`Milestones` を押す。
興味のあるマイルストーン項目を押す。関連する issues や pull requests を表示する
リンクが現れる。

Viewing your milestone's progress
----------------------------------------------------------------------

同様にして簡単な統計を観察できる。
