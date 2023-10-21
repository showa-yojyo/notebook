======================================================================
Managing your issues with tasklists ノート
======================================================================

本章は GitHub Issues documentation の部分だ。見出しが Issues と並列しているので
ノートを分割した。

.. contents::

About tasklists
======================================================================

いちばん重要な事項は：

   For the best experience, we recommend adding no more than 50 tasks to a
   tasklist and no more than 5 tasklists per issue. There is a hard limit of 250
   tasks per tasklist and 10 tasklists per issue.

課題一覧の用途：

   You can sketch out a draft of your plans, in either Markdown or in the UI,
   and optionally convert those draft tasks into real issues or add existing
   issues and pull requests to your tasklists.

課題一覧に関係のある issue ページには :guilabel:`Tracked by #(id)` 表示が現れる。

   Tasklists also integrate with your projects. You can add the "Tracks" and
   "Tracked-by fields" to your project views to quickly see the relationships
   between your issues.

これはプロジェクトに関する記述で見ていきたい。

Quickstart for tasklists
======================================================================

この演習の記述における UI が実際と説明とで違う。操作手順は現行 UI でも通用するよ
うに維持されている。

Creating a tasklist
======================================================================

方法は UI とテキスト (Markdown) の二つある。前者は実態に合致していないので、後者
を習得する。

   Once you have started editing your tasklist Markdown, you can add new tasks
   by preceding each new task with ``- [ ]`` and then adding either:

   * A draft task. Draft tasks are text that can later be converted into issues.
   * The full link to an issue or pull request.

後者は issue と同じリポジトリーならば ``#`` と issue 番号の組み合わせで略記可。

Managing tasks in a tasklist
======================================================================

UI が食い違うので割愛。

Using projects and tasklists
======================================================================

Project 検索欄で課題一覧が関わるフィルターを適用可能だと述べている。

   To use the "tracks" and "tracked-by" fields, you will need to add all the
   issues and pull requests that comprise your tasklist to the project.

というのだが、これらの fields が組み込まれていないようだ？

フィルターの書式は次のとおり：

.. code:: text

   tracked-by:"<OWNER>/<REPO>#<ISSUE NUMBER>"
