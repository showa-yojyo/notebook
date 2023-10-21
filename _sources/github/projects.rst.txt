======================================================================
Planning and tracking with Projects ノート
======================================================================

本章は GitHub Issues documentation の部分だ。見出しが Issues と並列しているので
ノートを分割した。

本ノートでは組織回りを割愛することがある。

.. contents::
   :depth: 3

Learning about Projects
======================================================================

About Projects
----------------------------------------------------------------------

GitHub で言うプロジェクトは issues と pull requests を統合する何かであると規定し
ている。何かは三とおりある：

   A project is an adaptable spreadsheet, task-board, and road map that
   integrates with your issues and pull requests on GitHub to help you plan and
   track your work effectively.

この機能の目的は issues と pull requests の情報を次のように扱うことだ：

   Information is synced automatically to your project as you make changes,
   updating your views and charts. This integration works both ways, so that
   when you change information about a pull request or issue in your project,
   the pull request or issue reflects that information.

ここでは field というものを issues や pull requests に与えることが可能だ。

Projects は自動化を支援している。

Projects の直轄機能というわけではないが、課題一覧というものがある。この機能につ
いては別途記述されている：

   You can use tasklists to build hierarchies of issues, dividing your issues
   into smaller subtasks, and creating new relationships between your issues.

プロジェクトの情報の眺めを分析目的に合わせて調節することが可能だ：

   You can save these views, allowing you to quickly return to them as needed
   and make them available to your team. Views not only let you scope down the
   items listed but also offer two different layout options.

Quickstart for Projects
----------------------------------------------------------------------

利用者プロジェクト作成手順：

#. :menuselection:`Your profile --> Projects --> New project`
#. ここで次のいずれかを押す：

   * テンプレート
   * :guilabel:`Table`
   * :guilabel:`Board`
#. :guilabel:`Create` を押す

プロジェクトを新規作成したら :guilabel:`README` を執筆する。手順：

#. プロジェクトページ右上 :menuselection:`... --> Settings`
#. 画面内 :guilabel:`README` を埋める
#. 編集後に :guilabel:`Save` を押す

プロジェクトに既存または草稿 issue を追加することが可能。前者の場合、issue また
は pull request の URL を指定して作成する。後者の場合の手順は URL ではなく考えを
直接記入する。

以降のチュートリアル内容：

* 反復欄 (an iteration field) というものを追加
* Priority 欄を追加
* ビューを Priority の値でグループ分けする
* ビューを保存する
* プロジェクト進行状況をわかりやすく示すビューレイアウトを追加する
* 組み込みの自動化機能を構成する：

  #. プロジェクト右上 :menuselection:`... --> Workflows` を押す
  #. :guilabel:`Default workflows` を調べるといい

Best practices for Projects
----------------------------------------------------------------------

   You can use Projects to manage your work on GitHub, where your issues and
   pull requests live.

コツの見出しだけ列挙しておく：

* Break down large issues into smaller issues
* Communicate
* Make use of the description and README
* Use views
* Have a single source of truth
* Use automation
* Use different field types

課題を小分けすると作業を管理しやすくなり、並行して作業できるようになる。また、
pull request を吟味しやすくもなる。

README ファイルには次のことを明記する：

   * Explaining the purpose of the project.
   * Describing the project views and how to use them.
   * Including relevant links and people to contact for more information.

Project の View 機能でさまざまな角度から検証する。例：

   * Filter by status to view all un-started items
   * Group by a custom priority field to monitor the volume of high priority
     items
   * Sort by a custom date field to view the items with the earliest target
     ship date

真実の一元化というのは次のようなことを言っている：

   For example, track a target ship date in a single location instead of spread
   across multiple fields. Then, if the target ship date shifts, you only need
   to update the date in one location.

自動化というのはプロジェクトが最新に保たれている可能性を上げることでもある。

   Projects offers built-in workflows.

自動化機能の枠組は複数ある：

   GitHub Actions and the GraphQL API enable you to automate routine project
   management tasks.

   Use an iteration field to schedule work or create a timeline. You can group
   by iteration to see if items are balanced between iterations, or you can
   filter to focus on a single iteration.

これは専門家でないと無理だ。

Creating projects
======================================================================

Creating a project
----------------------------------------------------------------------

これはもう習った。

Copying an existing project
----------------------------------------------------------------------

割愛。

Migrating from projects (classic)
----------------------------------------------------------------------

昔どこかのリポジトリーに作ってしまった可能性があるので、見つけたら実施する。

Managing items in your project
======================================================================

Adding items to your project
----------------------------------------------------------------------

:guilabel:`Add item` についての詳しい記述。

Converting draft issues to issues
----------------------------------------------------------------------

ドロップダウンリストを開いてみるか :menuselection:`...` メニューを開いてみるとコ
マンドが現れる。

Editing items in your project
----------------------------------------------------------------------

表形式のビューではスプレッドシート風の操作をする。

Archiving items from your project
----------------------------------------------------------------------

   You can archive an item to keep the context about the item in the project but
   remove it from the project views.

ということは消えていない。

例によって ドロップダウンリストを開いてみるか :menuselection:`...` メニューを開
いてみると :guilabel:`Arcihive` コマンドが現れる。

   You can delete an item to remove it from the project entirely.

:guilabel:`Delete from project` コマンドが現れる。

Understanding fields
======================================================================

About text and number fields
----------------------------------------------------------------------

   You can use text fields to include notes or any other freeform text in your
   project.

..

   Text fields can be used in filters, for example: ``field:"exact text"``.

   Number fields can also be used in filters.

* 比較演算子が使える。
* 範囲指定が使える。

About date fields
----------------------------------------------------------------------

   You can filter for date values using the ``YYYY-MM-DD`` format, for example:
   ``date:2022-07-01``.

* 比較演算子が使える。
* 範囲指定が使える。
* ``@today`` が使える。

About single select fields
----------------------------------------------------------------------

   You can filter by your single select fields by specifying the option, for
   example: ``fieldname:option``.

About iteration fields
----------------------------------------------------------------------

   You can filter for iterations by specifying the iteration name or
   ``@current`` for the current iteration, ``@previous`` for the previous
   iteration, or ``@next`` for the next iteration.

比較演算子が使える。

   You can insert breaks into your iterations to communicate when you are taking
   time away from scheduled work. The duration of a new break defaults to the
   length of the most recently created iteration.

Project :menuselection:`Settings --> Iteration` の右側の水平線をクリック。

About Tracks and Tracked by fields
----------------------------------------------------------------------

内容が実際と異なる？

Renaming custom fields
----------------------------------------------------------------------

Project :guilabel:`Settings` 左柱の自作フィールド名を押す。右側で編集。

Deleting custom fields
----------------------------------------------------------------------

Project :guilabel:`Settings` 左柱の自作フィールド名を押す。右側で
:guilabel:`Delete field` を押す。

Customizing views in your project
======================================================================

Changing the layout of a view
----------------------------------------------------------------------

   You can set each view in your project to a different layout.

ビューのタブにあるドロップダウンリストから選べ：

* :guilabel:`Table`
* :guilabel:`Board`
* :guilabel:`Roadmap`

Customizing the table layout
----------------------------------------------------------------------

列の表示はビュータブのドロップダウンリストから :guilabel:`Fields:` でも変更可能。

値でグループ化することが可能。ビュータブのドロップダウンリストから
:guilabel:`Group by:` でも変更可能。

   You can slice your items by a field to view a list of the field values in a
   separate panel. When you click on a value in the slice panel, the current
   view will adjust to only show items with that value.

ビュータブのドロップダウンリストから :guilabel:`Slice by:` で設定。

テーブル列や行の入れ替えはマウスのドラッグアンドドロップで可能。

当然ソート可能。:guilabel:`Sort by:` を見ろ。

集計機能もあるらしい。:guilabel:`Field sum:` がある場合がある？

Customizing the board layout
----------------------------------------------------------------------

   The board layout spreads your issues, pull requests, and draft issues across
   customizable columns.

次のビュー設定があり得る：

* Setting a limit on the number of items in a column
* Showing and hiding fields
* Setting the column field in board layout
* Showing and hiding columns in board layout
* Slicing by field values
* Sorting by field values
* Grouping by field values
* Showing the sum of a number field

指定方法はビュータブのドロップダウンリストからそれらしいコマンドを実行する。

Customizing the roadmap layout
----------------------------------------------------------------------

* Setting the start and target date fields
* Setting vertical markers
* Setting the zoom level

Roadmap ヘッダー :guilabel:`Date fields` を押して開始日と終了日を指定する。

:guilabel:`Markers` を押してどのマーカーを示すのかを指示する。

   You can choose the density of items on your roadmap.

虫眼鏡ボタンで指定する。選択肢は：

* :guilabel:`Month`
* :guilabel:`Quarter`
* :guilabel:`Year`

次の操作はビューヘッダータブのドロップダウンリストから：

* Slicing by field values
* Sorting by field values
* Grouping by field values
* Showing the sum of a number field

Filtering projects
----------------------------------------------------------------------

   You can customize which items appear in your views using filters for item
   metadata, such as assignees and the labels applied to issues, and by the
   fields in your project. You can combine filters and save them as views.

ビューのタブの真下にあるテキストボックスに検索パターンを指示する。

Managing your views
----------------------------------------------------------------------

* :guilabel:`New View` でタブ追加。
* 既存タブのドロップダウンリストに :guilabel:`Duplicate view` コマンドあり。
* ドロップダウンリストの下にある :guilabel:`Save` でビューを保存。
* タブはドラッグアンドドロップで左右に移動可能。
* 既存タブのドロップダウンリストに :guilabel:`Rename view` コマンドあり。
* 既存タブのドロップダウンリストに :guilabel:`Delete view` コマンドあり。

Automating your project
======================================================================

Using the built-in automations
----------------------------------------------------------------------

   For example, you can automatically set the status to :guilabel:`Todo` when an
   item is added to your project or set the status to :guilabel:`Done` when an
   issue is closed.

組み込み workflow の設定方法： Project 画面右上 :menuselection:`... -->
Workflows` を押す。左列から所望の workflow を押す。右側の右上 :guilabel:`Edit`
ボタンを押す。:guilabel:`Set Value` 下のドロップダウンリストから状態を選択。最後
に :guilabel:`Save and turn on workflow` を押して確定。

Using the API to manage Projects
----------------------------------------------------------------------

高度な話題と思われる。割愛。

Automating Projects using Actions
----------------------------------------------------------------------

   A project can span multiple repositories, but a workflow is specific to a
   repository. Add the workflow to each repository that you want your project to
   track.

..

   You may also want to use the ``actions/add-to-project`` workflow, which is
   maintained by GitHub and will add the current issue or pull request to the
   project specified.

ここも難しい。中止。

Adding items automatically
----------------------------------------------------------------------

   You can configure your project's built-in workflows to automatically add new
   items as they are created or updated in a repository.

..

   The auto-add workflow supports a subset of filters. You can use the following
   filters when configuring your workflow.

``is``, ``label``, ``reason``, ``assignee``, ``no`` の五つが利用可能。

   The auto-add workflow is limited per plan.

Free プランでは一件のみ。だからだいじに取っておくのがいい。

複製方法は知る必要なし。UI が無効になっている。

Archiving items automatically
----------------------------------------------------------------------

   You can configure your project's built-in workflows to automatically archive
   items.

..

   The auto-archive workflow supports a subset of filters.

``is``, ``reason``, ``updated`` の三つが利用可能。

   When you enable automatic archiving for issues or pull requests, items in
   your project that already meet your criteria will also be archived.

方法： Project 画面右上 :menuselection:`... --> Workflows` を押す。左列から
:guilabel:`Auto-archive items` を押す。右側の右上 :guilabel:`Edit` ボタンを押
す。テキストボックスに問い合わせ文を入力。最後に :guilabel:`Save and turn on
workflow` を押して確定。

Viewing insights from your project
======================================================================

About insights for Projects
======================================================================

   You can use insights for Projects to view, create, and customize charts that
   use the items added to your project as their source data.

..

   For example, you can create charts to show how many items are assigned to
   each individual, or how many issues are assigned to each upcoming iteration.

   Historical charts track changes to the state of your project items.

Creating charts
======================================================================

Project 画面右上のプロットボタンを押す。:guilabel:`New chart` を押すと統計図表が
現れる。右側フィルターを記入したら :guilabel:`Save changes` を押す。

Configuring charts
======================================================================

統計図表右上の :guilabel:`Configure` ボタンを押すと：

* :guilabel:`Layout` でプロット種別を選択可能
* :guilabel:`X-axis`, :guilabel:`Y-axis` でどの統計を見るのかを選択可能
* オプションで集計可能

Managing your project
======================================================================

Managing visibility of your projects
----------------------------------------------------------------------

   Projects can be public or private.

Project 画面右上 :menuselection:`... --> Settings --> Project settings -->
Visibility` ドロップダウンリストで :guilabel:`Private` か :guilabel:`Public` を
指定。

Managing access to your projects
----------------------------------------------------------------------

   Admins of user-level projects can invite individual collaborators and manage
   their access.

Project 画面右上 :menuselection:`... --> Settings --> Manage access --> Invite
collaborators` でアクセスを与えたいアカウントを指定する。

:guilabel:`Role` ドロップダウンリストで :guilabel:`Admin`, :guilabel:`Write`,
:guilabel:`Read` のどれかを指示する。:guilabel:`Invite` ボタンで確定。

すでにアクセスを与えた協力者から剥奪するには、同様の手順でアカウントを指定して
:guilabel:`Remove` ボタンを押す。

Managing project templates in your organization
----------------------------------------------------------------------

   You can create templates or set projects as templates in your organization,
   allowing other people to select your template as the base for projects they
   create.

..

   The projects you have marked as templates are made available in the "Select a
   template" pop-up window when other people create projects in your
   organization.

変わった機能だ？

テンプレートの作成方法：

画面右上 :guilabel:`Your organizations` から組織を選択し、:guilabel:`Projects`
を押す。画面左列の :guilabel:`Templates` を押して右側の :guilabel:`New template`
を押す。

プロジェクトをテンプレートとする方法：

Project の右上 :menuselection:`... --> Settings` を押す。:guilabel:`Make
template` をオンにする。

   If you have write or admin permissions for a project in your organization,
   you can choose to copy the project as a template.

Project の右上 :menuselection:`... --> Settings` を押す。:guilabel:`Copy as
template` ボタンを押す。

Closing and deleting your projects
----------------------------------------------------------------------

Project 画面右上 :menuselection:`... --> Settings --> Project settings -->
Delete this project` で削除、同 :guilabel:`Close this project` で閉じる。

閉じた Project は再開可能らしい。

Adding your project to a repository
----------------------------------------------------------------------

リポジトリー :menuselection:`Projects --> Link project`

Adding your project to a team
----------------------------------------------------------------------

割愛。
