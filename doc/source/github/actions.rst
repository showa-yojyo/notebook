======================================================================
GitHub Actions documentation ノート
======================================================================

`GitHub Actions documentation <https://docs.github.com/en/actions>`__ 読書ノー
ト。自動化を実現する機能を極めればある意味最強なので、熟読したい。しかし、長い。

.. contents::
   :depth: 3

* :guilabel:`Overview` → :ref:`Understanding GitHub Actions <actions-overview>`
* :guilabel:`Quickstart` → :ref:`Quickstart for GitHub Actions <actions-quickstart>`

.. todo::

   詰める記事一覧

   * Using starter workflows
   * Automating builds and tests
   * Deployment
   * Managing issues and pull requests
   * Examples

.. _actions-quickstart:

Quickstart for GitHub Actions
======================================================================

リポジトリーに workflow を作成する方法：

#. ディレクトリー :file:`.github/workflows` を用意する
#. ここに GitHub Actions の仕様を満たす YAML ファイルを置く。

この記事のデモ workflow は、GitHub に何かをプッシュすると引き起こされる。

Workflow の結果を観察する方法：

#. リポジトリー画面から :menuselection:`Actions` を開く。
#. 左柱から workflow の名前を探して押す。
#. 一覧から観察したい実行の名前を探して押す。
#. 左柱からジョブを探して押す。

これで右側にログが表示される。

   GitHub provides preconfigured starter workflows that you can customize to
   create your own continuous integration workflow.

出来合いの workflow をカスタマイズして実戦投入することがよくある。

   You can browse the full list of starter workflows in the
   `actions/starter-workflows <https://github.com/actions/starter-workflows>`__
   repository.

馴染みのあるものはすぐには見つからない。

Learn GitHub Actions
======================================================================

.. _actions-overview:

Understanding GitHub Actions
----------------------------------------------------------------------

   GitHub Actions is a continuous integration and continuous delivery (CI/CD)
   platform that allows you to automate your build, test, and deployment
   pipeline. You can create workflows that build and test every pull request to
   your repository, or deploy merged pull requests to production.

CI/CD 初心者だが、GitHub Actions は何かを自動化するための機能だという理解で、こ
のまま読み進めることにする。

   GitHub Actions goes beyond just DevOps and lets you run workflows when other
   events happen in your repository.

DevOps も何たるかを知らない。

   You can configure a GitHub Actions workflow to be triggered when an event
   occurs in your repository, such as a pull request being opened or an issue
   being created.

リポジトリーに対する何らかのイベント発生時に workflow というものが実施されると。
次の用語の関係を理解してから進む：

* Runner
* Job
* Step

次は Workflow の定義だと思っていい：

   A workflow is a configurable automated process that will run one or more
   jobs.

一つの YAML ファイルに複数構成可能らしい。このファイルはリポジトリーの
:file:`/.github/workflow` に配置するものだ。

イベントは定義よりも実例を列挙されたほうが理解しやすい：

   For example, activity can originate from GitHub when someone creates a pull
   request, opens an issue, or pushes a commit to a repository.

ジョブとステップは同時に定義される：

   A job is a set of steps in a workflow that is executed on the same runner.
   Each step is either a shell script that will be executed, or an action that
   will be run. Steps are executed in order and are dependent on each other.

アクションの定義は少々わかりにくい。理解を後回しにしたい：

   An action is a custom application for the GitHub Actions platform that
   performs a complex but frequently repeated task.

ランナーはわかりやすい。物理的な概念だから：

   A runner is a server that runs your workflows when they're triggered.

Workflow ファイル :file:`learn-github-actions.yml` の一行ごとの解説をきっちり読
む。YAML データについての次の仕様を覚えておく：

* ``name`` はリポジトリー Actions ページの左柱に現れる。意外だが指定は任意。
* ``run-name`` はその右側の一項目として現れる。
* ``on [push]`` は workflow 発動イベントがリポジトリーへの push であることを指定
  している。``on`` は値としてリストをとる。
* ``jobs`` でジョブをグループ化している。次のキーはジョブ名を指示する。
* ``runs-on`` でランナーを指定する。値 ``ubuntu-latest`` はそのままの意味。
* ``steps`` でステップをグループ化している。値としてリストをとる。
* ``uses`` はアクションを指定する。詳細はまだわからない。
* ``run`` はランナー上のコマンドを記述する。コマンドラインそのものだ。

.. admonition:: 読者ノート

   YAML の文法を別途学習する必要がある。特にリストと辞書の記法が重要だ。

   When your workflow is triggered, a workflow run is created that executes the
   workflow. After a workflow run has started, you can see a visualization graph
   of the run's progress and view each step's activity on GitHub.

   `Best YAML Viewer Online <https://jsonformatter.org/yaml-viewer>`__
   で YAML をツリービューで示せる。

Workflow 実行の状況を確認するには、リポジトリー :menuselection:`Actions` から最
新の実行を調べる。

Finding and customizing actions
----------------------------------------------------------------------

アクションが定義されている可能性のある場所は：

* The same repository as your workflow file
* Any public repository
* A published Docker container image on Docker Hub

三つ目は想像不能。

   GitHub Marketplace is a central location for you to find actions created by
   the GitHub community.

リポジトリー画面から YAML ファイルを鉛筆ボタンで編集しようとすると、一般のファイ
ルでは出ない UI が右柱に現れる。:guilabel:`Marketplace` タブで
:guilabel:`Featured Actions` 一覧が出る。

   You can add an action to your workflow by referencing the action in your
   workflow file.

..

   To keep your workflow stable even when updates are made to an action, you can
   reference the version of the action to use by specifying the Git or Docker
   tag number in your workflow file.

:guilabel:`Featured Actions` から一つ選んでクリックすると当該アクションの詳細な
記述が表示される。:guilabel:`Installation` 見出しの少し下にあるクリップボードコ
ピーアイコンを押す。そのテキストを見れば YAML ファイルにどう組み込むべきかがわか
る。引数を適宜設定する。

リポジトリー内に自作アクションを定義することも可能。YAML の ``uses`` キーに自作
アクションのパスを指定すればいい。``{owner}/{repo}@{ref}`` のような形式でも動作
するようだ。よく見かける ``actions/setup-node@v3`` のような指定はその実例の一つ
だ。

.. code:: text

   |-- hello-world (repository)
   |   |__ .github
   |       └── workflows
   |           └── my-first-workflow.yml
   |       └── actions
   |           |__ hello-world-action
   |               └── action.yml

``v3`` はタグ名だ。タグ名ではなく SHA を指定する場合には、GitHub
で通じるような省略形はダメだ。

   An action often accepts or requires inputs and generates outputs that you can
   use.

   To see the inputs and outputs of an action, check the :file:`action.yml` or
   :file:`action.yaml` in the root directory of the repository.

この YAML はリポジトリーのルートにあると言っている。

.. code:: yaml

   inputs:
     file-path: # id of input
       description: "Path to test script"
       required: true
       default: "test-file.js"
   outputs:
     results-file: # id of output
       description: "Path to results file"

入力はわかりやすいが出力がどんなものか想像できない。

   The ``outputs`` keyword defines an output called ``results-file``, which
   tells you where to locate the results.

Essential features of GitHub Actions
----------------------------------------------------------------------

   If you need to use custom environment variables, you can set these in your
   YAML workflow file.

.. code:: yaml

   jobs:
     example-job:
         steps:
           - name: Connect to PostgreSQL
             run: node client.js
             env:
               POSTGRES_HOST: postgres
               POSTGRES_PORT: 5432

上の例では、環境変数 ``POSTGRES_{HOST,PORT}`` を定義する。コマンド ``node
client.js`` からそれらの値が参照可能になる。

コマンドやスクリプトを実行するのはランナーだ。スクリプトがあるのはリポジトリーの
はずなので、

   To use a workflow to run a script stored in your repository you must first
   check out the repository to the runner.

作業ディレクトリーの指定も可能。``working-directory:`` で指示する。スクリプトは
実行可能でなければならない。実行可能にする手段はなんでもいい。例では ``run:`` で
``chmod +x`` している。

   If your job generates files that you want to share with another job in the
   same workflow, or if you want to save the files for later reference, you can
   store them in GitHub as artifacts.

ジョブ同士が何かを共有する手段はこのファイルしかない？

.. code:: yaml

   uses: actions/upload-artifact@v3
   with:
     name: output-log-file
     path: output.log

を先にやってから、

.. code:: yaml

   uses: actions/download-artifact@v3
   with:
     name: output-log-file

とする。

   To download an artifact from the same workflow run, your download job should
   specify ``needs: upload-job-name`` so it doesn't start until the upload job
   finishes.

この例を見たい。

Expressions
----------------------------------------------------------------------

   You can use expressions to programmatically set environment variables in
   workflow files and access contexts. An expression can be any combination of
   literal values, references to a context, or functions. You can combine
   literals, context references, and functions using operators.

環境変数を式で設定する：

.. code:: yaml

   env:
     MY_ENV_VAR: ${{ <expression> }}

..

   As part of an expression, you can use boolean, null, number, or string data
   types.

リテラル式は JavaScript に似ている：

.. code:: yaml

   env:
     myNull: ${{ null }}
     myBoolean: ${{ false }}
     myIntegerNumber: ${{ 711 }}
     myFloatNumber: ${{ -9.2 }}
     myHexNumber: ${{ 0xff }}
     myExponentialNumber: ${{ -2.99e-2 }}
     myString: Mona the Octocat
     myStringInBraces: ${{ 'It''s open source!' }}

組み込み関数が存在する。割愛。``format`` くらいは習得しておくか。ステータス関数
も重要か。

Contexts
----------------------------------------------------------------------

   Contexts are a way to access information about workflow runs, variables,
   runner environments, jobs, and steps. Each context is an object that contains
   properties, which can be strings or other objects.

..

   GitHub Actions includes a collection of variables called contexts and a
   similar collection of variables called default variables.

この二つは利用可能なタイミングが異なる：

   You can use most contexts at any point in your workflow, including when
   default variables would be unavailable.

既定環境変数はジョブを実行するランナー上にしか存在しない。

   You can print the contents of contexts to the log for debugging. The
   ``toJSON`` function is required to pretty-print JSON objects to the log.

ただし、どこかに機密情報が含まれている可能性を考慮する。

   The ``github`` context contains information about the workflow run and the
   event that triggered the run. You can also read most of the ``github``
   context data in environment variables.

特にこれには ``github.token`` が含まれる。

   The ``env`` context contains variables that have been set in a workflow, job,
   or step. It does not contain variables inherited by the runner process.

..

   The ``vars`` context contains custom configuration variables set at the
   organization, repository, and environment levels.

   The ``job`` context contains information about the currently running job.

``job.status`` はよく見ることを期待できる。

   The ``jobs`` context is only available in reusable workflows, and can only be
   used to set outputs for a reusable workflow.

再利用可能とは？

   The ``steps`` context contains information about the steps in the current job
   that have an ``id`` specified and have already run.

..

   The ``runner`` context contains information about the runner that is
   executing the current job.

これは想像しやすい。``runner.os`` などの値がある。

   The ``secrets`` context contains the names and values of secrets that are
   available to a workflow run. The ``secrets`` context is not available for
   composite actions due to security reasons.

``secrets.GITHUB_TOKEN`` は workflow 実行ごとに作成される。

   The ``needs`` context contains outputs from all jobs that are defined as a
   direct dependency of the current job.

..

   The ``inputs`` context contains input properties passed to an action, to a
   reusable workflow, or to a manually triggered workflow.

Variables
----------------------------------------------------------------------

   GitHub sets default variables for each GitHub Actions workflow run. You can
   also set custom variables for use in a single workflow or multiple workflows.

..

   You can store any configuration data such as compiler flags, usernames, or
   server names as variables.

定義方法は二つある。

   To set a custom environment variable for a single workflow, you can define it
   using the ``env`` key in the workflow file.

これは今まで見た方法だ。

   You can use either runner environment variables or contexts in ``run`` steps,
   but in the parts of a workflow that are not sent to the runner you must use
   contexts to access variable values.

変数展開の書式はランナー、``runs-on`` 値による。Ubuntu なら Bash だから ``$VAR``
のように書く。

   When you set an environment variable, you cannot use any of the default
   environment variable names.

上書きは意味がない。

   Note: You can list the entire set of environment variables that are available
   to a workflow step by using ``run: env`` in a step and then examining the
   output for the step.

これは試してもよい。

第二の方法は：

   You can create configuration variables for use across multiple workflows, and
   can define them at either the organization, repository, or environment level.

..

   When you define configuration variables, they are automatically available in
   the ``vars`` context.

リポジトリー :menuselection:`Settings --> Secrets and variables --> Actions` の
ページを開いて、:guilabel:`Variables` タブを押す。見れば分かる。

   You can access environment variable values using the ``env`` context and
   configuration variable values using the ``vars`` context.

``${{ CONTEXT.PROPERTY }}`` 記法はランナーの違いを吸収するためにある。

   You will commonly use either the ``env`` or ``github`` context to access
   variable values in parts of the workflow that are processed before jobs are
   sent to runners.

..

   Because default environment variables are set by GitHub and not defined in a
   workflow, they are not accessible through the ``env`` context.

対応する情報が ``github`` に存在することが多い。

   We strongly recommend that actions use variables to access the filesystem
   rather than using hardcoded file paths.

心得る。

   You can write a single workflow file that can be used for different operating
   systems by using the ``RUNNER_OS`` default environment variable and the
   corresponding context property ``${{ runner.os }}``.

ランナーの OS 種別ごとに処理を分けるのは悪手ではないか。

Usage limits, billing, and administration
----------------------------------------------------------------------

   There are usage limits for GitHub Actions workflows. Usage charges apply to
   repositories that go beyond the amount of free minutes and storage for a
   repository.

無駄な workflow を無効化しておく。

   GitHub Actions usage is free for standard GitHub-hosted runners in public
   repositories, and for self-hosted runners.

それは良かった。

   In addition to the usage limits, you must ensure that you use GitHub Actions
   within the GitHub Terms of Service.

利用規約が実はある。

   You can configure the artifact and log retention period for your repository,
   organization, or enterprise account.

成果物とは？

   You can enable and disable individual workflows in your repository on GitHub.

重要な操作なので、先に習得しておく。

Examples
======================================================================

Using scripts to test your code on a runner
----------------------------------------------------------------------

   When this workflow is triggered, it automatically runs a script that checks
   whether the GitHub Docs site has any broken links.

実戦投入されている workflow を解説されるのはありがたい。

* ``on`` キーは複数のイベントを指定可能。

   * イベント ``workflow_dispatch`` は手動で workflow を発動させるのに必要。

* ``push`` キーにはブランチを列挙することが多いようだ。
* ``permissions`` は後で述べる。

この workflow では ``check-links`` キーでジョブを定義する。

* ``steps`` でジョブを列挙する。
* ``uses`` にはアクションを記述する。
* ``run`` にはコマンドラインを記述する。

アクション ``trilom/file-changes-action`` は本文参照。特定のファイルを出力するこ
とに注意。これを動作させるために先述の ``permission`` 定義が必要だ。

スクリプト :file:`script/rendered-content-link-checker.mjs` を実行するステップを
よく見て覚える。

Using the GitHub CLI on a runner
----------------------------------------------------------------------

イベントとして ``on`` に ``schedule`` と書ける：

   The ``schedule`` event lets you use cron syntax to define a regular interval
   for automatically triggering the workflow.

ジョブ序盤、``if`` でこれが動作するリポジトリーを制限している：

   Only run the ``check_all_english_links job`` if the repository is named
   ``docs-internal`` and is within the ``github`` organization.

``steps`` の直前に ``env`` を置いて環境変数を定義しておく。

   Uses the ``peter-evans/create-issue-from-file`` action to create a new GitHub
   issue.

このステップは難しい。最後の ``${{ failure() }}`` の長い処理もどうなっているの
か。``run`` の値がシェルスクリプトになっているだろうが。

Using concurrency, expressions, and a test matrix
----------------------------------------------------------------------

``runs-on`` の記述が複雑だ：

   This configures the job to run on a GitHub-hosted runner or a self-hosted
   runner, depending on the repository running the workflow.

この例では ``strategy`` が急所だ。

   Setting ``fail-fast`` to ``false`` prevents GitHub from cancelling all
   in-progress jobs if any matrix job fails.

``matrix`` で ``test-group`` という配列を定義する。この配列の要素それぞれはテス
トを表す？最後のステップで ``npm test -- tests/${{ matrix.test-group }}/`` とい
うコマンドを実行する。配列の要素それぞれに対して ``run`` されるのか？

Using workflows
======================================================================

About workflows
----------------------------------------------------------------------

Quickstart のおさらい。

Triggering a workflow
----------------------------------------------------------------------

   When you use the repository's ``GITHUB_TOKEN`` to perform tasks, events
   triggered by the ``GITHUB_TOKEN``, with the exception of
   ``workflow_dispatch`` and ``repository_dispatch``, will not create a new
   workflow run. This prevents you from accidentally creating recursive workflow
   runs.

したがって、ある workflow 発動中に別の workflow が発動することはない。最初の例の
二つをよく比較しろ。

   If you specify multiple events, only one of those events needs to occur to
   trigger your workflow. If multiple triggering events for your workflow occur
   at the same time, multiple workflow runs will be triggered.

これは迷惑な気がする。

   You can use activity types and filters to further control when your workflow
   will run.

イベント名のケツにコロンが付く書き方だ。

   Some events have activity types that give you more control over when your
   workflow should run. Use ``on.<event_name>.types`` to define the type of
   event activity that will trigger a workflow run.

例えば：

.. code:: yaml

   on:
     issues:
       types:
         - opened
         - labeled

先ほどの規則によると、二つのラベルがある issue が開くとこの workflow が三回走
る。

   Some events have filters that give you more control over when your workflow
   should run.

..

   When using the ``pull_request`` and ``pull_request_target`` events, you can
   configure a workflow to run only for pull requests that target specific
   branches.

例：

.. code:: yaml

   on:
     pull_request:
       # Sequence of patterns matched against refs/heads
       branches:
         - main
         - 'mona/octocat'
         - 'releases/**'

反対のものもある：

   Use the ``branches-ignore`` filter when you only want to exclude branch name
   patterns. You cannot use both the ``branches`` and ``branches-ignore``
   filters for the same event in a workflow.

..

   When using the ``push`` event, you can configure a workflow to run on
   specific branches or tags.

例：

.. code:: yaml

   on:
     push:
       # Sequence of patterns matched against refs/heads
       branches:
         - main
         - 'mona/octocat'
         - 'releases/**'
       # Sequence of patterns matched against refs/tags
       tags:
         - v2
         - v1.*

こちらも反対のものがある。割愛。

   When using the ``push`` and ``pull_request`` events, you can configure a
   workflow to run based on what file paths are changed. Path filters are not
   evaluated for pushes of tags.

次の例は JavaScript ファイルを push すると発動する：

.. code:: yaml

   on:
     push:
       paths:
         - '**.js'

こちらも反対のものがある。割愛。

   When using the ``workflow_run`` event, you can specify what branches the
   triggering workflow must run on in order to trigger your workflow.

次の workflow は ``Build`` という workflow が ``canary`` 以外のブランチで実行さ
れた場合に限り発動する：

.. code:: yaml

   on:
     workflow_run:
       workflows: ["Build"]
       types: [requested]
       branches-ignore:
         - "canary"

..

   When using the ``workflow_dispatch`` event, you can optionally specify inputs
   that are passed to the workflow. The triggered workflow receives the inputs
   in the ``inputs`` context.

例が長いので割愛。入力値を定義するのに用いる。

   Information about the event that triggered a workflow run is available in the
   ``github.event`` context.

..

   You can also print the entire ``github.event`` context to see what properties
   are available for the event that triggered your workflow:

``${{ toJSON(github.event) }}`` として標準出力などに書き出す。

   You can use conditionals to further control whether jobs or steps in your
   workflow will run.

例えば

.. code:: yaml

   if: github.event.label.name == 'bug'

..

   If you want to manually trigger a specific job in a workflow, you can use an
   environment that requires approval from a specific team or user.

誰かの許可が要る。``environment: production`` の説明がしっくりこない。

Manually running a workflow
----------------------------------------------------------------------

   When a workflow is configured to run on the ``workflow_dispatch`` event, you
   can run the workflow using the Actions tab on GitHub, GitHub CLI, or the REST
   API.

必要条件の一つを述べていなかった：

   To trigger the ``workflow_dispatch`` event, your workflow must be in the
   default branch.

対象の workflow 画面にある :guilabel:`Run workflow` を押す。そしてブランチを指定
する。

GitHub CLI を使うことでも手動発動可能：

.. code:: console

   bash$ gh workflow run WORKFLOW

ここで ``WORKFLOW`` は対象 workflow の名前または ID またはファイル名とする。

コマンドライン引数がいろいろあるので、必要になったら調べる。コマンド ``gh run
watch`` で途中経過を調べられるかもしれない。

Disabling and enabling a workflow
----------------------------------------------------------------------

この操作は重要なので GitHub ユーザーは自力で見つけたと思う。

   Disabling a workflow allows you to stop a workflow from being triggered
   without having to delete the file from the repo. You can easily re-enable the
   workflow again on GitHub.

リポジトリー :menuselection:`Actions --> (target workflow) --> Disable workflow`
を押す。すでに無効になっている場合、反対に :guilabel:`Enable workflow` が現れ
る。

GitHub CLI を使うことでも設定可能：

.. code:: console

   bash$ gh workflow disable WORKFLOW
   bash$ gh workflow enable WORKFLOW

Events that trigger workflows
----------------------------------------------------------------------

   You can configure your workflows to run when specific activity on GitHub
   happens, at a scheduled time, or when an event outside of GitHub occurs.

この節は ``on`` に指定できる値のレファレンスだ。使いたいイベントを控えておくか？

Workflow syntax for GitHub Actions
----------------------------------------------------------------------

   Workflow files use YAML syntax, and must have either a ``.yml`` or ``.yaml``
   file extension.

この節は YAML のキー仕様とフィルター早見表からなる。必要に応じて当たる。

Workflow commands for GitHub Actions
----------------------------------------------------------------------

   Actions can communicate with the runner machine to set environment variables,
   output values used by other actions, add debug messages to the output logs,
   and other tasks.

..

   Most workflow commands use the echo command in a specific format, while
   others are invoked by writing to a file.

   Use the ``::`` syntax to run the workflow commands within your YAML file;
   these commands are then sent to the runner over stdout.

よその YAML を見て ``::`` が出てきたらこの節を当たればいい。

   The step that creates or updates the environment variable does not have
   access to the new value, but all subsequent steps in a job will have access.

TODO: まだ読んでいないところが少し残った。

Reusing workflows
----------------------------------------------------------------------

   Rather than copying and pasting from one workflow to another, you can make
   workflows reusable.

モジュールみたいなものか？

   If you reuse a workflow from a different repository, any actions in the
   called workflow run as if they were part of the caller workflow.

そうでないとおかしい。

   Starter workflows allow everyone in your organization who has permission to
   create workflows to do so more quickly and easily.

とにかく Starter workflow という何か便利なものがあるようだ。

   For a workflow to be reusable, the values for on must include
   ``workflow_call``:

   .. code:: yaml

      on:
        workflow_call:

データの受け渡し。``secrets: inherit`` に注目。

もう気付いているが：

   You call a reusable workflow by using the ``uses`` keyword.

引数の指定はキーが二種類ある：

   To pass named inputs to a called workflow, use the ``with`` keyword in a job.
   Use the ``secrets`` keyword to pass named secrets.

さっき見た ``matrix`` の説明は次がわかりやすい：

   A matrix strategy lets you use variables in a single job definition to
   automatically create multiple job runs that are based on the combinations of
   the variables.

出力をやる。

   A reusable workflow may generate data that you want to use in the caller
   workflow. To use these outputs, you must specify them as the outputs of the
   reusable workflow.

どうも ``on.workflow_call.outputs`` 部分でキー名で出力変数名を指定するらしい。わ
かりにくいからこの例を実際に動かすほうがいいだろう。

Required workflows
----------------------------------------------------------------------

   A required workflow is triggered by ``pull_request`` and
   ``pull_request_target`` default events and appears as a required status
   check, which blocks the ability to merge the pull request until the required
   workflow succeeds.

この種の workflow は色々と条件があり、際立っているのは：

   When a workflow is run as a required workflow it will ignore all the filters
   in the ``on:`` section, for example: ``branches``, ``branches-ignore``,
   ``paths``, ``types`` etc.

..

   After a required workflow has run at least once in a repository, you can view
   its workflow runs in that repository's "Actions" tab.

リポジトリー :menuselection:`Actions` ページ左柱に :guilabel:`Required
workflows` 一覧が示される。

Caching dependencies to speed up workflows
----------------------------------------------------------------------

   For example, package and dependency management tools such as Maven, Gradle,
   npm, and Yarn keep a local cache of downloaded dependencies.

こういう頻繁に利用するものをとっておける。

   To cache dependencies for a job, you can use GitHub's ``cache`` action.

すぐ次のパッケージとアクションの対応表で想像付く。

   Multiple workflow runs in a repository can share caches. A cache created for
   a branch in a workflow run can be accessed and restored from another workflow
   run for the same repository and branch.

アクション ``cache`` の基本動作は：

   The ``cache`` action will attempt to restore a cache based on the ``key`` you
   provide. When the action finds a cache that exactly matches the key, the
   action restores the cached files to the ``path`` you configure.

..

   On a cache miss, the action automatically creates a new cache if the job
   completes successfully.

この後しばらくして YAML 例が示される。設定が難しいので諦める。

   You can use the web interface to view a list of cache entries for a
   repository.

リポジトリー :menuselection:`Actions --> Caches` ページで閲覧可能。

そこではキャッシュを削除することが可能。:guilabel:`Delete` ボタンを押す。

Storing workflow data as artifacts
----------------------------------------------------------------------

   Artifacts allow you to share data between jobs in a workflow and store data
   once that workflow has completed.

定義：

   An artifact is a file or collection of files produced during a workflow run.

..

   Storing artifacts uses storage space on GitHub.

   GitHub provides two actions that you can use to upload and download build
   artifacts.

..

   You can use the ``upload-artifact`` action to upload artifacts.

YAML 例から抜粋：

.. code:: yaml

   - name: Archive production artifacts
     uses: actions/upload-artifact@v3
     with:
       name: dist-without-markdown
       path: |
         dist
         !dist/**/*.md
   - name: Archive code coverage results
     uses: actions/upload-artifact@v3
     with:
       name: code-coverage-report
       path: output/test/code-coverage.html

..

   During a workflow run, you can use the ``download-artifact`` action to
   download artifacts that were previously uploaded in the same workflow run.

   Specify an artifact's name to download an individual artifact. If you
   uploaded an artifact without specifying a name, the default name is
   ``artifact``.

   .. code:: yaml

      - name: Download a single artifact
        uses: actions/download-artifact@v3
        with:
          name: my-artifact

``name`` を指定しない場合、実行中 workflow の成果物すべてをダウンロードする。

   You can use the ``upload-artifact`` and ``download-artifact`` actions to
   share data between jobs in a workflow.

..

   Jobs that are dependent on a previous job's artifacts must wait for the
   dependent job to complete successfully.

このために ``needs`` を指定する。最後の例はわかりやすい。

Creating starter workflows for your organization
----------------------------------------------------------------------

   When you create a new workflow, you can choose a starter workflow and some or
   all of the work of writing the workflow will be done for you.

..

   Starter workflows can be created by users with write access to the
   organization's :file:`.github` repository.

組織のリポジトリーの :file:`.github` というのが急所だ。

YAML ファイルの他にメタデータというものを用意する必要がある。

組織リポジトリーの :file:`.github/workflow-templates` に新しい workflow を入れ
る。

   If you need to refer to a repository's default branch, you can use the
   ``$default-branch`` placeholder.

メタデータの置き方：

   Create a metadata file inside the :file:`workflow-templates` directory. The
   metadata file must have the same name as the workflow file, but instead of
   the ``.yml`` extension, it must be appended with ``.properties.json``.

Using starter workflows
----------------------------------------------------------------------

   For example, if you use Node.js, GitHub will suggest a starter workflow file
   that installs your Node.js packages and runs your tests.

リポジトリーの内容に応じて workflow を提案してくるようだ。

リポジトリー :file:`Actions --> New workflow` で色々と提案されるから、いいものを
選択して :guilabel:`Configure` を押す。そこからは見ればわかる。

Sharing workflows, secrets, and runners with your organization
----------------------------------------------------------------------

組織を利用する場合には読む。

   An organization allows you to centrally store and manage secrets, artifacts,
   and self-hosted runners.

特に言いたいのは次か：

   When creating a secret or variable in an organization, you can use a policy
   to limit which repositories can access it.

組織 :menuselection:`Settings --> Secrets and variables --> Actions` ページで項
目を追加する。

Using GitHub CLI in workflows
----------------------------------------------------------------------

   For each step that uses GitHub CLI, you must set an environment variable
   called ``GITHUB_TOKEN`` to a token with the required scopes.

:command:`gh` を使う ``run`` のあるスコープから次が有効ならばいい：

.. code:: yaml

   env:
       GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

Using jobs
======================================================================

Using jobs in a workflow
----------------------------------------------------------------------

   A workflow run is made up of one or more ``jobs``, which run in parallel by
   default. To run jobs sequentially, you can define dependencies on other jobs
   using the ``jobs.<job_id>.needs`` keyword.

次の例では ``job1``, ``job2``, ``job3`` の順に走ることになる。ただし、必要とされ
ている job が成功終了した場合に限る：

.. code:: yaml

   jobs:
     job1:
     job2:
       needs: job1
     job3:
       needs: [job1, job2]

成否に関わらず後続を走らせる場合には ``if: {{ always() }}`` を指定する。

Choosing the runner for a job
----------------------------------------------------------------------

   Use ``jobs.<job_id>.runs-on`` to define the type of machine to run the job
   on.

私個人では Linux だけ対応すれば十分だ。これでいい：

.. code:: yaml

   jobs:
     job_id:
       runs-on: ubuntu-latest

Using conditions to control job execution
----------------------------------------------------------------------

   You can use the ``jobs.<job_id>.if`` conditional to prevent a job from running
   unless a condition is met.

.. code:: yaml

   jobs:
     job_id:
       if: github.repository == 'USER/REPO'
       runs-on: ubuntu-latest

なお、値となる式をダブル中括弧で囲むのが安全だ。

Using a matrix for your jobs
----------------------------------------------------------------------

利用するつもりがないので割愛。

Using concurrency
----------------------------------------------------------------------

.. todo::

   この機能は重要だと思えるが、少し読んだだけでは理解不能。

Using environments for jobs
----------------------------------------------------------------------

   Use ``jobs.<job_id>.environment`` to define the environment that the job
   references.

下のように構成すると、ステップ出力を URL として用いることになる：

.. code:: yaml

   environment:
     name: production_environment
     url: ${{ steps.step_id.outputs.url_output }}

Running jobs in a container
----------------------------------------------------------------------

   Use ``jobs.<job_id>.container`` to create a container to run any steps in a
   job that don't already specify a container. If you have steps that use both
   script and container actions, the container actions will run as sibling
   containers on the same network with the same volume mounts.

.. todo::

   コンテナーを理解していないので後回し。

Setting default values for jobs
----------------------------------------------------------------------

   Use ``defaults`` to create a map of default settings that will apply to all
   jobs in the workflow.

シェルと作業ディレクトリーは特別扱いらしい：

   You can use ``defaults.run`` to provide default ``shell`` and
   ``working-directory`` options for all run steps in a workflow.

次のコードですべてのジョブで ``shell`` と ``working-directory`` の既定値を決め
る：

.. code:: yaml

   defaults:
     run:
       shell: bash
       working-directory: ./scripts

Assigning permissions to jobs
----------------------------------------------------------------------

   You can use ``permissions`` to modify the default permissions granted to the
   :envvar:`GITHUB_TOKEN`, adding or removing access as required, so that you
   only allow the minimum required access.

トークンが表す権限を修正したものを使うと言っている？

   You can use ``permissions`` either as a top-level key, to apply to all jobs
   in the workflow, or within specific jobs.

そして、次の有効域ごとに ``read``, ``write``, ``none`` のいずれかを割り当てる：

* ``actions``
* ``checks``
* ``contents``
* ``deployments``
* ``discussions``
* ``id-token``
* ``issues``
* ``packages``
* ``pages``
* ``pull-requests``
* ``repository-projects``
* ``security-events``
* ``statuses``

例えば ``pages: write`` は GitHub Pages の構築を要求する動作だ。

.. code:: yaml

   permissions:
     pages: write

次のような略記法？も使える：

* ``permissions: read-all``
* ``permissions: write-all``
* ``permissions: {}``

..

  You can specify ``permissions`` at the top level of a workflow, so that the
  setting applies to all jobs in the workflow.

つまり YAML ファイルでインデントがない位置に ``permissions:`` を指定可能。

個別ジョブを有効域とする ``permissions`` を指定することも可能。

Defining outputs for jobs
----------------------------------------------------------------------

   You can use ``jobs.<job_id>.outputs`` to create a map of outputs for a job.
   Job outputs are available to all downstream jobs that depend on this job.

出力は文字列とする。最大 1MB の長さ。一つの workflow 全体で 50MB まで。

ジョブの「川下」を指定するのに先述の ``jobs.<job_id>.needs`` を指定することに注
意。

本文の例 YAML を丸ごと理解すること。

Manage workflow runs
======================================================================

Re-running workflows and jobs
----------------------------------------------------------------------

   You can re-run a workflow run, all failed jobs in a workflow run, or specific
   jobs in a workflow run up to 30 days after its initial run.

* どちらの再実行時でも、元実行時と同じ ``GITHUB_SHA`` と ``GITHUB_REF`` が用いら
  れる。
* 再実行時の権限として元実行時の権限が採用される。
* ジョブ再実行はログの保持期間を経過すると不可。
* ジョブ再実行時にはデバッグログ出力を有効にすることが可能。

全ジョブ再実行方法は、まず :guilabel:`Actions` ページで左柱から所望の workflow
を探して押す。実行名を押して実行概要を見る。成否によって項目が若干異なるが、
:guilabel:`Re-run jobs` を押す。

失敗ジョブ（と後続ジョブ）を再実行する方法もある。実行環境は元実行時のものが適用
される。手順は先ほどのものとほぼ同じ。違いは :guilabel:`Re-run failed jobs` を押
すところだけ。

特定のジョブを再実行する方法もある。左柱のジョブ項目名の右にある再実行ボタンを押
す。

.. todo::

   再利用可能 workflow を再実行する方法

最後の実行結果を観察する方法は実行結果右上の :guilabel:`Latest` ドロップダウンリ
ストを使う。

Canceling a workflow
----------------------------------------------------------------------

リポジトリーに対する書き込み権限を有していることが必要だ。

まず :guilabel:`Actions` ページで左柱から所望の workflow を探して押す。実行名を
押して実行概要を見る。右上の :guilabel:`Cancel workflow` を押す。

キャンセルする際には資源の解放が正しく行われるかどうかを意識する。本文で述べられ
ているアルゴリズムの 4 と 5 を理解することが重要だ。これに耐え得るジョブを記述す
るべきだ。

Approving workflow runs from public forks
----------------------------------------------------------------------

   By default, all first-time contributors require approval to run workflows.

外部の人間が workflow を好き勝手に書き換える可能性を牽制している。

Approving workflow runs from private forks
----------------------------------------------------------------------

   When someone without write access submits a pull request to a private
   repository, a maintainer may need to approve any workflow runs.

当アカウントには起こり得ない事象だ。割愛。

Reviewing deployments
----------------------------------------------------------------------

   Jobs that reference an environment configured with required reviewers will
   wait for an approval before starting. While a job is awaiting approval, it
   has a status of "Waiting".

評価が必要な workflow の実行履歴ページを開き、:guilabel:`Review deployments` を
押す。対象のジョブ環境を選択する。評価次第で :guilabel:`Approve and deploy` または
:guilabel:`Reject` を押す。

.. todo::

   Bypassing deployment protection rules

Skipping workflow runs
----------------------------------------------------------------------

   Workflows that would otherwise be triggered using ``on: push`` or ``on:
   pull_request`` won't be triggered if you add any of the following strings to
   the commit message in a push, or the HEAD commit of a pull request:

   * ``[skip ci]``
   * ``[ci skip]``
   * ``[no ci]``
   * ``[skip actions]``
   * ``[actions skip]``

これを知っていることで workflow 画面で :guilabel:`Disable` しなくて済むというこ
とだ。そしてこれを忘れぬように：

   To allow the pull request to be merged you can push a new commit to the pull
   request without the skip instruction in the commit message.

Deleting a workflow run
----------------------------------------------------------------------

   You can delete a workflow run that has been completed, or is more than two
   weeks old.

削除したい workflow の実行履歴ページを開き、項目欄右の :menuselection:`... -->
Delete workflow run` を押す。ダイアログが出るので Yes を押す。

Downloading workflow artifacts
----------------------------------------------------------------------

:guilabel:`Actions` ページで左柱から所望の workflow を探して押す。実行名を押して
実行概要を出す。この :guilabel:`Artifacts` 節に成果物リンクがある。

Removing workflow artifacts
----------------------------------------------------------------------

成果物を削除すれば記憶域が回復する。

上述の手順で :guilabel:`Artifacts` を表示し、成果物項目右側のゴミバケツを押す。

成果物とログの保有期間のカスタマイズは後述。

Build and test
======================================================================

.. admonition:: 読者ノート

   Python の節と出来合いのものを使わない節を読めば workflow の構造は理解可能。

About continuous integration
----------------------------------------------------------------------

   When you commit code to your repository, you can continuously build and test
   the code to make sure that the commit doesn't introduce errors.

これが CI の基本的な考え方だ。

   You can build and test updates locally before pushing code to a repository,
   or you can use a CI server that checks for new code commits in a repository.

CI 目的のサーバーが存在するということを覚えておく。

   CI using GitHub Actions offers workflows that can build the code in your
   repository and run your tests.

CI を実現する workflow を書くことになる。

   When you set up CI in your repository, GitHub analyzes the code in your
   repository and recommends CI workflows based on the language and framework in
   your repository. For example, if you use Node.js, GitHub will suggest a
   starter workflow that installs your Node.js packages and runs your tests.

リポジトリーの構造がある程度一般的であることが暗黙的に期待されている。

Building and testing Go
----------------------------------------------------------------------

   Search for "go".

Building and testing Java with Ant
----------------------------------------------------------------------

   Search for "Java with Ant".

Building and testing Java with Gradle
----------------------------------------------------------------------

   Search for "Java with Gradle".

Building and testing Java with Maven
----------------------------------------------------------------------

   Search for "Java with Maven".

Building and testing .NET
----------------------------------------------------------------------

   Search for "dotnet".

Building and testing Node.js
----------------------------------------------------------------------

   Search for "Node.js".

Building and testing PowerShell
----------------------------------------------------------------------

   ここは出来合いのものを使わない？

Building and testing Python
----------------------------------------------------------------------

   To get started quickly, add a starter workflow to the
   :file:`.github/workflows` directory of your repository.

#. リポジトリー :menuselection:`Actions` ページに移動。
#. 左柱の :guilabel:`New workflow` を押す。
#. "Python application" を検索して検索結果の :guilabel:`Configure` を押す。

内容を適宜編集してコミットし、:file:`.github/workflows/python-app.yml` を得る。

まずは Python バージョンを決める。

   To use a pre-installed version of Python or PyPy on a GitHub-hosted runner,
   use the ``setup-python`` action. This action finds a specific version of
   Python or PyPy from the tools cache on each runner and adds the necessary
   binaries to :envvar:`PATH`, which persists for the rest of the job.

単一バージョンを指定したい。次のように書く：

.. code:: yaml

   - name: Set up Python
     # This is the version of the action for setting up Python, not the Python version.
     uses: actions/setup-python@v4
     with:
       # Semantic version range syntax or exact version of a Python version
       python-version: '3.x'

..

   You can use :command:`pip` to install dependencies from the PyPI package
   registry before building and testing your code.

依存パッケージをインストールするようにしたい。ステップとして次のように書く：

.. code:: yaml

   - name: Install dependencies
     run: python -m pip install --upgrade pip setuptools wheel

:command:`pip` 自体を upgrade してから :file:`requirements.txt` に指定された依存
パッケージを更新させる方法もある：

.. code:: yaml

   - name: Install dependencies
     run: |
       python -m pip install --upgrade pip
       pip install -r requirements.txt

依存パッケージをキャッシュする機能も有している：

.. code:: yaml

   - uses: actions/setup-python@v4
     with:
       python-version: '3.11'
       cache: 'pip'
   - run: pip install -r requirements.txt
   - run: pip test

ビルドの次はテストだ。本文の例は pytest を採用している：

.. code:: yaml

   - name: Test with pytest
     run: |
       pip install pytest pytest-cov
       pytest tests.py --doctest-modules --junitxml=junit/test-results.xml --cov=com --cov-report=xml --cov-report=html

成果物をアップロードするには ``actions/upload-artifact`` を用いる：

.. code:: yaml

   - name: Upload pytest test results
     uses: actions/upload-artifact@v3
     with:
       name: pytest-results-${{ matrix.python-version }}
       path: junit/test-results-${{ matrix.python-version }}.xml
     # Use always() to always run this step to publish test results when there are test failures
     if: ${{ always() }}

製品を PyPI などのパッケージ置場に登録して終わることも可能だ。その場合には登録者
が置場の API トークンを保持している必要がある。

Building and testing Ruby
----------------------------------------------------------------------

   Search for "ruby".

Building and testing Swift
----------------------------------------------------------------------

   Search for "swift".

Building and testing Xamarin applications
----------------------------------------------------------------------

   ここは出来合いのものを使わない？

Using containerized services
======================================================================

以下の内容のようなので丸ごと割愛：

* About service containers
* Creating PostgreSQL service containers
* Creating Redis service containers

Publish packages
======================================================================

About packaging with GitHub Actions
----------------------------------------------------------------------

発行場所は GitHub でもよそでも可能。

   After building and testing your code, a packaging step can produce a runnable
   or deployable artifact. Depending on the kind of application you're building,
   this package can be downloaded locally for manual testing, made available for
   users to download, or deployed to a staging or production environment.

Workflow が成果物を出力して、一般人に対してダウンロード可能になる。

   In addition to uploading packaging artifacts for testing in a continuous
   integration workflow, you can create workflows that build your project and
   publish packages to a package registry.

成果物を出力する場合が CI とパッケージ置場への発行の二通りあると言っている：

   You may want to publish packages to GitHub Packages on every push into the
   default branch.

および：

   You can automate this by creating a workflow that publishes packages to a
   package registry on every release creation.

Publishing Docker images
----------------------------------------------------------------------

   Each time you create a new release on GitHub, you can trigger a workflow to
   publish your image. The workflow in the example below runs when the
   ``release`` event triggers with the ``created`` activity type.

この考え方は Docker 以外の他の発行手順でも通じる。

Docker 公式アクションを用いる：

* ``docker/login-action``
* ``docker/metadata-action``
* ``docker/build-push-action``

当然ながら：

   To push to Docker Hub, you will need to have a Docker Hub account, and have a
   Docker Hub repository created.

単一の workflow で発行場所は GitHub Packages と Docker Hub のどちらか一方または
両方に指定することが可能だ。

Publishing Java packages with Gradle
----------------------------------------------------------------------

パッケージ置場への認証に使用するユーザー名とパスワードまたはトークンの環境変数を
:file:`build.gradle` で設定する必要がある。

Maven Central Repository というパッケージ置場にコマンド ``gradle publish`` を実
行してパッケージを発行する。

   In the deploy step, you’ll need to set environment variables for the username
   and password or token that you use to authenticate to the Maven repository.

Gradle 公式アクションを用いる：

* ``gradle/wrapper-validation-action``
* ``gradle/gradle-build-action``

Publishing Java packages with Maven
----------------------------------------------------------------------

コマンド ``mvn --batch-mode deploy`` の実行でパッケージ置場に配備する。

Maven Central Repository と GitHub Packages の両方に置く場合、

* 構成ファイル :file:`pom.xml` をどう書けばいいか不明。
* `actions/setup-java` を用いるステップを二度実行することになる。
* コマンド ``mvn --batch-mode deploy`` を実行するステップを、異なる引数で二度実
  行する。

Publishing Node.js packages
----------------------------------------------------------------------

   If you add steps in your workflow to configure the ``publishConfig`` fields
   in your :file:`package.json` file, you don't need to specify the
   ``registry-url`` using the ``setup-node`` action, but you will be limited to
   publishing the package to one registry.

..

   By default, :command:`npm` uses the ``name`` field of the
   :file:`package.json` file to determine the name of your published package.

..

   If you're publishing a package that includes a scope prefix, include the
   scope in the name of your :file:`package.json` file

* ``actions/setup-node`` を用いる。

  * このアクションは :file:`.npmrc` を生成する。
  * ``registry-url:`` にパッケージ置場の URL を指定する。
  * ``scope:`` を上述のように指定する場合がある。E.g. ``@octocat``.

* コマンド ``npm publish`` を実行する。

  * ``env.NODE_AUTH_TOKEN`` を ``secrets`` 経由で設定する。

Manage issues and pull requests
======================================================================

Using GitHub Actions for project management
----------------------------------------------------------------------

GitHub Actions を用いて Issues や pull requests の対処を自動化することが可能だ。

   For example, you can create a workflow that runs every time an issue is
   created to add a label, leave a comment, and move the issue onto a project
   board.

リポジトリーに対して何かイベントが発生したときや、定期的に workflow を実行させる
ように構成することが可能だ。ここで興味があるのは次のようなタイミングだ：

   * An issue is opened, assigned, or labeled.
   * A comment is added to an issue.
   * A project card is created or moved.
   * A scheduled time.

以降の数節で何を対処することが可能なのかを見ていく。

Adding labels to issues
----------------------------------------------------------------------

   The `actions/github-script
   <https://github.com/marketplace/actions/github-script>`__ action allows you
   to easily use the GitHub API in a workflow.

次の YAML コードはその用例だ。確かに API を直接操作しているように読める：

.. code:: yaml

   - uses: actions/github-script@v6
     with:
       script: |
         github.rest.issues.addLabels({
           issue_number: context.issue.number,
           owner: context.repo.owner,
           repo: context.repo.repo,
           labels: ["triage"]
         })

YAML ルートに以下のコードを書くと、当該リポジトリーの issue が開いた時にこの
workflow が引き起こされる：

.. code:: yaml

   on:
     issues:
       types:
         - reopened
         - opened

Closing inactive issues
----------------------------------------------------------------------

ジョブの ``permissions:`` で ``issues:`` と ``pull-requests:`` を ``write`` にし
ておく。

Workflow を定期的に引き起こすコード：

.. code:: yaml

   on:
     schedule:
       - cron: "30 1 * * *"

..

   In the example above, the workflow will run every day at 1:30 UTC.

ステップでは `actions/stale
<https://github.com/marketplace/actions/close-stale-issues>`__ を用いる：

.. code:: yaml

   - uses: actions/stale@v5
     with:
       days-before-issue-stale: 30
       days-before-issue-close: 14
       stale-issue-label: "stale"
       stale-issue-message: "This issue is stale because it has been open for 30 days with no activity."
       close-issue-message: "This issue was closed because it has been inactive for 14 days since being marked as stale."
       days-before-pr-stale: -1
       days-before-pr-close: -1
       repo-token: ${{ secrets.GITHUB_TOKEN }}

アクションの各引数は名前が意味を示しているので、カンでカスタマイズしてよい。

Commenting on an issue when a label is added
----------------------------------------------------------------------

これは ``help-wanted`` ラベルの付いた新 issue に助けを求めるコメントを追加する
workflow だ。急所だけ列挙すると：

* ``on.issues.types: [labeled]``
* ``jobs.add-comment.if: github.event.label.name == 'help-wanted'``

このジョブの最初のステップについて：

* ``.uses = peter-evans/create-or-update-comment@<SHA>`` の SHA 値はどう与える？
* ``.with.issue-number`` に ``${{ github.event.issue.number }}`` を与える。
* ``.with.body`` にコメント本文を与える。

Moving assigned issues on project boards
----------------------------------------------------------------------

割愛。

Removing a label when a card is added to a project board column
----------------------------------------------------------------------

割愛。

Scheduling issue creation
----------------------------------------------------------------------

ジョブ名を ``create_issue`` とする。

* ``on.schedule.cron: 20 07 * * 1`` は毎週月曜 7:20 を意味する。
* ``jobs.create_issue.permissions.issues: write`` とする。

このジョブの最初のステップについて：

* ``.uses: imjohnbo/issue-bot@<SHA>`` の SHA 値はどう与える？
* ``.with.assignees: "monalisa, doctocat, hubot"``
* ``.with.labels: "weekly sync, docs-team"``
* ``.with.titles:`` 適当なタイトル
* ``.with.body:`` Markdown のテンプレ
* ``.env.GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}``

Migrate to GitHub Actions
======================================================================

Using GitHub Actions Importer to automate migrations
----------------------------------------------------------------------

節見出しが次のようになっている：

* Automating migration with GitHub Actions Importer
* Extending GitHub Actions Importer with custom transformers
* Supplemental arguments and settings
* Migrating from Azure DevOps with GitHub Actions Importer
* Migrating from Bamboo with GitHub Actions Importer
* Migrating from Bitbucket Pipelines with GitHub Actions Importer
* Migrating from CircleCI with GitHub Actions Importer
* Migrating from GitLab with GitHub Actions Importer
* Migrating from Jenkins with GitHub Actions Importer
* Migrating from Travis CI with GitHub Actions Importer

どの CI も持っていないので割愛。

Manually migrating to GitHub Actions
----------------------------------------------------------------------

同じ理由により割愛。

Monitoring and troubleshooting workflows
======================================================================

About monitoring and troubleshooting
----------------------------------------------------------------------

   Every workflow run generates a real-time graph that illustrates the run
   progress. You can use this graph to monitor and debug workflows.

実行時にグラフが更新されていくので、ページを開いたまま眺めていることが可能。

   A status badge shows whether a workflow is currently failing or passing. A
   common place to add a status badge is in the :file:`README.md` file of your
   repository, but you can add it to any web page you'd like.

まともなリポジトリーの説明文でよくみかけるバッヂだ。

   If the workflow logs do not provide enough detail to diagnose why a workflow,
   job, or step is not working as expected, you can enable additional debug
   logging.

手許の環境で実行できない以上、こういう機能は必須だ。

   If you attempt to cancel a workflow and the cancellation doesn't succeed,
   make sure you aren't using the ``always`` expression.

この式を内規で禁じたい。

Using the visualization graph
----------------------------------------------------------------------

#. リポジトリー画面から :menuselection:`Actions` を開く。
#. 左柱から workflow の名前を探して押す。
#. 一覧から観察したい実行の名前を探して押す。

画面右に当該 workflow を構成するジョブを節とするグラフが描画される。グラフの辺は
ジョブ間の依存関係を示す。各ジョブ名の左横の印がその状態を示す。

Adding a workflow status badge
----------------------------------------------------------------------

   A status badge shows whether a workflow is currently failing or passing.

これがバッヂの基本的な役割だ。

   You can also display the status of a workflow run for a specific ``branch``
   or ``event`` using the branch and event query parameters in the URL.

バッヂの表示方法を見ていく。

   You can build the URL for a workflow status badge using the name of the
   workflow file:

   | https://github.com/OWNER/REPOSITORY/actions/workflows/WORKFLOW-FILE/badge.svg

URL の引数を見ていく。

   To display the status of a workflow run for a specific branch, add
   ``?branch=BRANCH-NAME`` to the end of the status badge URL.

これはブランチの状態を知らせるときに利用する。

   To display the status of workflow runs triggered by the push event, add
   ``?event=push`` to the end of the status badge URL.

対象ブランチの現在の状態に対するビルド結果を表示する。

.. admonition:: 読者ノート

   バッヂの見てくれは workflow 名称＋状態文字列。

Viewing workflow run history
----------------------------------------------------------------------

これまで何度も見ているものなので割愛。

Viewing job execution time
----------------------------------------------------------------------

左柱の :guilabel:`Run details --> Usage` を押すと、右側に実行時間明細が表示され
る。

Using workflow run logs
----------------------------------------------------------------------

   GitHub Actions use the Checks API to output statuses, results, and logs for a
   workflow.

今は言葉だけ覚えておく。

   In addition to the steps configured in the workflow file, GitHub adds two
   additional steps to each job to set up and complete the job's execution.
   These steps are logged in the workflow run with the names :guilabel:`Set up
   job` and :guilabel:`Complete job`.

ということは workflow が空であるということはあり得ない。

いつものようにジョブ画面を開く。画面右側にジョブを構成するステップが縦に並ぶ。

   Any failed steps are automatically expanded to display the results.

ログを検索することが可能だ。ステップ一覧の右上にある検索欄を用いる。

ログをダウンロードするには、検索欄右の歯車ボタンを押して
:menuselection:`Download log archive` を押す。

ログを削除するには workflow 画面に移動する。右上ボタンから :menuselection:`...
--> Delete all logs` を押す。

Enabling debug logging
----------------------------------------------------------------------

   These extra logs are enabled by setting secrets or variables in the
   repository containing the workflow

リポジトリー所有者ならば十分。

   Runner diagnostic logging provides additional log files that contain
   information about how a runner is executing a job.

* The runner process log
* The worker process log

ログを有効にするには、リポジトリーの秘密 or 変数 ``ACTIONS_RUNNER_DEBUG`` を
``true`` に設定する必要がある。秘密として指定するほうの値が優先される。

ログは :file:`runner-diagnostic-logs` からダウンロードする。

より詳細なログを求めるならばリポジトリーの秘密 or 変数 ``ACTIONS_STEP_DEBUG`` を
``true`` に設定する。デバッグイベントを含むログが得られる。

Notifications for workflow runs
----------------------------------------------------------------------

* 成功時の通知は無効化しておきたい。
* スケジュールイベントによる通知は発生条件が複雑だ。

Security guides
======================================================================

Security hardening for GitHub Actions
----------------------------------------------------------------------

Understanding the risk of script injections は必見。インラインでシェルスクリプト
を記述するときには注入攻撃を意識すること。外部アクション呼び出し、面倒でも変数導
入、トークンによる認証組み込みなどで強化する。

サードパーティー製 workflow の再利用はいつでも善。

Using secrets in GitHub Actions
----------------------------------------------------------------------

   Secrets are variables that you create in an organization, repository, or
   repository environment. The secrets that you create are available to use in
   GitHub Actions workflows.

秘密は変数の一種だ。組織、リポジトリー、環境の三層それぞれが有効照準であるように
値を持たせる。このノートでは個人リポジトリーのみ注目する。

   To make a secret available to an action, you must set the secret as an input
   or environment variable in the workflow file.

ログに秘密を出力することは不可能だと思っておく。

最小権限の原則について実例を述べている。

個人リポジトリーに秘密を追加する方法は次のとおり。操作者は所有者であることを仮定
する：

#. リポジトリーから :menuselection:`Settings --> Secrets and variables -->
   Actions` にアクセス。
#. :guilabel:`Secrets` を押す。
#. :guilabel:`New repository secret` を押す。
#. フォームの :guilabel:`Name` と :guilabel:`Secret` を記入する。
#. :guilabel:`Add secret` を押す。

Workflow コード中では、

   Secrets cannot be directly referenced in ``if:`` conditionals.

秘密の値はパイプに流さないようにしたい：

   Avoid passing secrets between processes from the command line, whenever
   possible. Command-line processes may be visible to other users (using the ps
   command) or captured by security audit events.

Workflow ログ削除機能を情報漏洩目的で用いる場合がある。

Automatic token authentication
----------------------------------------------------------------------

   At the start of each workflow job, GitHub automatically creates a unique
   ``GITHUB_TOKEN`` secret to use in your workflow.

   When you enable GitHub Actions, GitHub installs a GitHub App on your
   repository. The ``GITHUB_TOKEN`` secret is a GitHub App installation access
   token.

話が見えない。

トークンを ``${{ secrets.GITHUB_TOKEN }}`` の形で workflow から参照する。

   When you use the repository's ``GITHUB_TOKEN`` to perform tasks, events
   triggered by the ``GITHUB_TOKEN``, with the exception of
   ``workflow_dispatch`` and ``repository_dispatch``, will not create a new
   workflow run.

この仕組みは workflow の二重発動を防ぐ。

   Commits pushed by a GitHub Actions workflow that uses the ``GITHUB_TOKEN`` do
   not trigger a GitHub Pages build.

この仕様は何かに利用できるか？

   The following table shows the permissions granted to the ``GITHUB_TOKEN`` by
   default.

この表のヘッダーの Scope 以外の意味がわからない。

   You can modify the permissions for the ``GITHUB_TOKEN`` in individual workflow
   files.

   You can see the permissions that ``GITHUB_TOKEN`` had for a specific job in
   the :guilabel:`Set up job` section of the workflow run log.

``GITHUB_TOKEN Permissions`` を含む行をクリックすると詳細が示される。

   You can use the permissions key in your workflow file to modify permissions
   for the ``GITHUB_TOKEN`` for an entire workflow or for individual jobs. This
   allows you to configure the minimum required permissions for a workflow or
   job.

具体的方法は？

   If you need a token that requires permissions that aren't available in the
   ``GITHUB_TOKEN``, you can create a GitHub App and generate an installation
   access token within your workflow.

これはアプリケーションの章で見ていく？

Creating actions
======================================================================

自作、再利用、共有。

About custom actions
----------------------------------------------------------------------

アクションの概要：

   You can write your own actions to use in your workflow or share the actions
   you build with the GitHub community. To share actions you've built with
   everyone, your repository must be public.

   Actions can run directly on a machine or in a Docker container. You can
   define an action's inputs, outputs, and environment variables.

アクションは次の三種類ある：

* Docker コンテナー (Linux only)
* JavaScript
* 複合

Docker コンテナーはアクションコードに環境が付属したものと考えられる。

   Because of the latency to build and retrieve the container, Docker container
   actions are slower than JavaScript actions.

JavaScript はアクションの作りがわかりやすい。どのランナーでも動作するように、
JavaScript で閉じたコードを書かねばならない。

複合アクションは何が複合なのかというと：

   A *composite* action allows you to combine multiple workflow steps within one
   action.

カスタムアクションは専用リポジトリーに作成するのが望ましい。

カスタムアクションを公にするならば、バージョン管理をまともにやる。

   We recommend using tags for actions release management. Using this approach,
   your users can easily distinguish between major and minor versions:

今まで見てきたように、YAML コードでアクションの名前に SHA やタグを指定することが
普通だ。

:file:`README` でアクションの仕様を明示しておく：

   * A detailed description of what the action does
   * Required input and output arguments
   * Optional input and output arguments
   * Secrets the action uses
   * Environment variables the action uses
   * An example of how to use your action in a workflow

最後に、GitHub Marketplace で入手できること、モノを述べている：

   While both GitHub Actions and GitHub Apps provide ways to build automation
   and workflow tools, they each have strengths that make them useful in
   different ways.

Creating a Docker container action
----------------------------------------------------------------------

私の手に余る話題なので割愛。

Creating a JavaScript action
----------------------------------------------------------------------

:file:`README` の内容は本書のままではダメで、Example usage の YAML コードの
``uses:`` の引数を自分のものに合わせる。

最初の ``git tag`` コマンドでは ``v1.1`` ではなく ``v1.0`` にしておくと、後ほど
の改訂版タグ ``v1.1`` と整合する。

パッケージ ``vercel/ncc`` 導入後にアクションが機能しなくなる。次のエラーがジョブ
の初期化時に生じる：

| Could not find file '/home/runner/work/_actions/_temp_6252a79a-7686-4d73-ad49-7a00b221fd2d/_staging/showa-yojyo-hello-world-javascript-action-243bf14/node_modules/.bin/uuid'.

Creating a composite action
----------------------------------------------------------------------

実習モノなので後回し。この章を読み終わってから。

Metadata syntax for GitHub Actions
----------------------------------------------------------------------

   All actions require a metadata file. The metadata filename must be either
   :file:`action.yml` or :file:`action.yaml`. The data in the metadata file
   defines the inputs, outputs, and runs configuration for your action.

このファイルも YAML で記述する。その仕様が本節に述べられている。

Dockerfile support for GitHub Actions
----------------------------------------------------------------------

Docker は後回し。

Setting exit codes for actions
----------------------------------------------------------------------

   GitHub uses the exit code to set the action's check run status, which can be
   ``success`` or ``failure``.

UNIX と同じでゼロが成功で、それ以外は失敗。

   If you are creating a JavaScript action, you can use the actions toolkit
   ``@actions/core`` package to log a message and set a failure exit code. For
   example:

   .. code:: java

      try {
        // something
      } catch (error) {
        core.setFailed(error.message);
      }

Publishing actions in GitHub Marketplace
----------------------------------------------------------------------

   When you plan to publish your action to GitHub Marketplace, you'll need to
   ensure that the repository only includes the metadata file, code, and files
   necessary for the action.

ある種の要件を満たしていると GitHub による審査を免除されるようだ。

   You can add the action you've created to GitHub Marketplace by tagging it as
   a new release and publishing it.

TODO: 手順まとめ

   To remove a published action from GitHub Marketplace, you'll need to update
   each published release.

単に撤回することはできないか？

Sharing actions and workflows from your private repository
----------------------------------------------------------------------

   Any actions or reusable workflows stored in the private repository can be
   used in workflows defined in other private repositories owned by the same
   organization or user. Actions and reusable workflows stored in private
   repositories cannot be used in public repositories.

非公開リポジトリーのものは公開リポジトリーから利用不能という原則は変わらない。

リポジトリー :menuselection:`Settings --> Actions --> General` ページを開いて、
いちばん下にある :guilabel:`Accessible from repositories owned by the user` をオ
ンにする。

Sharing actions and workflows with your organization
----------------------------------------------------------------------

割愛。

Releasing and maintaining actions
----------------------------------------------------------------------

実践のコツ集。

Developing a third party CLI action
----------------------------------------------------------------------

   You can write an action to provide a way for users to access your servers via
   a configured CLI environment on GitHub Actions runners.

これも実習モノか。
