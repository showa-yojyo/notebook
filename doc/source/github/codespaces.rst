======================================================================
GitHub Codespaces documentation ノート
======================================================================

`GitHub Codespaces documentation <https://docs.github.com/en/codespaces>`__ は文
書がたくさんあるので読むのが厳しい。Codespace は本質的に有料機能なので、私はまず
利用しないはずだ。全文調査せずに切り上げる。

.. contents::

* :guilabel:`Overview` は個別ページの GitHub Codespaces overview へ
* :guilabel:`Quickstart` は Quickstart for GitHub Codespaces へ

GitHub Codespaces overview
======================================================================

  A codespace is a development environment that's hosted in the cloud. You can
  customize your project for GitHub Codespaces by committing configuration files
  to your repository

開発環境を使わせてくれると言っているのだ。その構成は：

  You can choose from a selection of virtual machine types, from 2 cores, 8 GB
  RAM, and 32 GB storage, up to 32 cores, 64 GB RAM, and 128 GB storage.

最低のメモリー 8GB というのは、私が今使っている PC のそれと同じだ。最低ラインで
も十分だ。

  By default, codespaces are created from an Ubuntu Linux image that includes a
  selection of popular languages and tools

WSL で作業している身としてはありがたい環境だ。

  You can connect to your codespaces from your browser, from Visual Studio Code,
  from the JetBrains Gateway application, or by using GitHub CLI. When you
  connect, you are placed within the Docker container.

Docker という術語が出てくるが、不勉強のツケがここに来そうだ。

GitHub Codespaces の利点をキャッチコピーだけ引用しておこう。再利用性、再現性、隔
離などという言葉が浮かぶ：

* Use a preconfigured development environment
* Access the resources you need
* Work anywhere
* Choose your editor
* Work on multiple projects
* Pair program with a teammate
* Publish your web app from a codespace
* Try out a framework

Codespaces の開始手段はいろいろあるようで、本文のリンク先それぞれを読むといい。

  All personal GitHub.com accounts have a monthly quota of free use of GitHub
  Codespaces included in the Free or Pro plan. You can get started using GitHub
  Codespaces on your personal account without changing any settings or providing
  payment details.

ノート冒頭で《本質的には有料機能》と記したが、上記の制約があるからだ。無料枠内で
やりくりせねばならない。

  To customize the runtimes and tools in your codespace, you can create one or
  more dev container configurations for your repository.

カスタマイズするほうが普通だろうが、見慣れぬ術語が出てきて不安だ。

  You can personalize aspects of your codespace environment by using a public
  `dotfiles <https://dotfiles.github.io/tutorials/>`__ repository. You can use
  dotfiles to set shell aliases and preferences, or to install your personal
  preference of the tools you like to use.

最後に、料金について述べられている。専用の節があるのでそこでまとめる。

Getting started with GitHub Codespaces
======================================================================

Quickstart for GitHub Codespaces
----------------------------------------------------------------------

  You'll work in the browser version of Visual Studio Code, which is initially
  the default editor for GitHub Codespaces.

Codespace とは何かと問われたら、上のように答えるのがいちばん伝わる気がする。

このクイックスタートではデモが用意されているので、以下、それを実施していく。

Codespace の作成方法は、まず Codespace テンプレートリポジトリーにアクセスする。
それから :menuselection:`Use this template --> Open in a codespace` を押す。これ
でブラウザーに VS Code に似た UI が現れる。

アプリケーションを起動するには、そこのコンソールで ``npm run dev`` を実行する。
本家同様のトーストが出現する。:guilabel:`Open in Browser` を押す。

アプリケーションを変数して変更を眺めるには：

#. :file:`haikus.json` を編集する。
#. 画面を手動でリフレッシュ。

VS Code での作業の要領で変更部分をすべてコミットすると :guilabel:`Publish
Branch` ボタンが現れる。それを押す。リポジトリーを選択する。これで自分のアカウン
トにリポジトリーが追加される。

  You can enable :menuselection:`Settings Sync` to sync extensions and other
  settings across devices and instances of VS Code. Your synced settings are
  cached in the cloud.

これを ON にすると吉のはずだが、PC で使っている VS Code の拡張構成と使い分けたい
ときは OFF ということになる。その中間が欲しい。

Understanding the codespace lifecycle
----------------------------------------------------------------------

  The lifecycle of a codespace begins when you create a codespace and ends when
  you delete it.

Codespace の寿命管理は常識的なのものであるようだ。

  There are limits to the number of codespaces you can create, and the number of
  codespaces you can run at the same time.

制限は二種類ある。今のところは好きなだけ作成できるような代物ではないと覚えておけ
ばいい。

  When you connect to a codespace through the web, auto-save is enabled
  automatically for the web editor and configured to save changes after a delay.

VS Code のファイル自動保存機能を Codespace 自体に適用したようなものか。

  Your work will be saved on a virtual machine in the cloud.

スペースを一定時間放置すると自動的に片付けられる。自動シャットダウンしてもデータ
は保存される。

用がないときには Codespace を止めておくのが無難だ。

  For example, if you're using a codespace in the VS Code web client and you
  close the browser tab, the codespace remains running on the remote machine.

Codespace 最大の特徴がこれだ。金がかかってはかなわない：

  If you create a codespace, it will continue to accrue storage charges until it
  is deleted, irrespective of whether it is active or stopped.

Deep dive into GitHub Codespaces
----------------------------------------------------------------------

  GitHub Codespaces is an instant, cloud-based development environment that uses
  a container to provide you with common languages, tools, and utilities for
  development.

スペースを開く方法は先述の方法以外にも複数ある：

  You can create a codespace on GitHub.com, in Visual Studio Code, or by using
  GitHub CLI.

GitHub リポジトリーには shallow clone という概念がある。

  Your repository is cloned into the :file:`/workspaces` directory in the
  codespace

コンテナーという概念を理解しないとダメそうだ。コンテナーが作成されてからスペース
に接続。

ファイルの保存については VS Code の Auto Save をオンにしておくとよい。

停止する方法は一つは習得しておく：

* <https://github.com/codespaces> で操作する
* VS Code コマンドパレットから :guilabel:`Codespaces: Stop Current Codespace` を
  実行する
* コンソールから ``gh codespace stop`` を実行する

ポート転送機能を有する。上手くノートにまとめられないので割愛。

  You can work with Git in your codespace either via the Terminal or by using
  the source control features of VS Code or JetBrains.

Codespace で Git 操作をすると何がうれしいかと言うと：

  Because GitHub Codespaces is designed to be ephemeral, you can use it as an
  isolated environment to experiment, check a teammate's pull request, or fix
  merge conflicts.

Codespace を公開するという考え方がある。作業環境を共有するという意図だろう。

  If you already use VS Code, you can use :menuselection:`Settings Sync` to
  automatically sync extensions, settings, themes, and keyboard shortcuts
  between your local instance and any codespaces you create.

VS Code の本物の拡張で設定を同期できる。ただし実行前にまず考えろ。

Codespace のディレクトリー構造について：

  When you create a codespace, your repository is cloned into the
  :file:`/workspaces` directory in your codespace. This is a persistent
  directory that is mounted into the container.

:file:`~/.bashrc` を書ける。

コンテナーの再構築に注意する。これがデータを壊す。

.. admonition:: 読者ノート

   私がコンテナー技術をまったく知らないので、ピンと来ない記述に出くわすと読むの
   が止まる。
