======================================================================
GitHub Actions documentation ノート
======================================================================

`GitHub Actions documentation <https://docs.github.com/en/actions>`__ 読書ノー
ト。自動化を実現する機能を極めればある意味最強なので、熟読したい。しかし、長い。

.. contents::
   :depth: 2

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

Workflow ファイルの一行ごとの解説をきっちり読む。YAML
データについての次の仕様を覚えておく：

* ``name`` はリポジトリー Actions ページの左柱に現れる。
* ``run-name`` はその右側の一項目として現れる。
* ``on [push]`` は workflow 発動イベントがリポジトリーへの push であることを指定
  している。
* ``jobs`` でジョブをグループ化している。次のキーはジョブ名を指示する。
* ``runs-on`` でランナーを指定する。値 ``ubuntu-latest`` はそのままの意味。
* ``steps`` でステップをグループ化している。
* ``uses`` はアクションを指定する。詳細はまだわからない。
* ``run`` はランナー上のコマンドを記述する。コマンドラインそのものだ。

..

   When your workflow is triggered, a workflow run is created that executes the
   workflow. After a workflow run has started, you can see a visualization graph
   of the run's progress and view each step's activity on GitHub.

Workflow 実行の状況を確認するには、リポジトリー ``Actions`` から最新の実行を調べ
る。
