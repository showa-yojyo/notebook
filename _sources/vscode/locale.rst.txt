======================================================================
ロケール
======================================================================

VS Code のデフォルトの表示言語は英語で、その他の言語は Marketplace から入手可能な
Language Pack 拡張次第だ。

VS Code は OS の UI 言語を検出し、Marketplace で利用可能な場合は適切な Language
Pack をインストールするように促す。本文のキャプチャー簡体字中国語の Language
Pack を推奨する例だ。

Language Pack 拡張機能をインストールし、プロンプトに従って再起動すると、VS Code
は OS の UI 言語に合致する Language Pack を使用する。

.. admonition:: 利用者ノート

   情報収集の都合上、本ノートでは UI を工場出荷時設定である英語のままにしておく
   のを推奨する。後述の :file:`argv.json` に設定する手法を採る。

.. attention::

   :doc:`./index` 冒頭の前提条件に留意すること。

.. contents::

UI 言語を変更する
======================================================================

コマンド :guilabel:`Configure Display Language` を実行して UI 言語を上書きできる。
コマンドを実行するとコマンドパレットの位置に言語入力欄が現れる。インストールされ
ている言語のロケール別一覧が表示され、現在のものが強調表示される。

オプション :guilabel:`Install additional languages...` を用いて Marketplace から
さらに多くの Language Pack をインストールするか、一覧から別のロケールを選択す
る。後者の場合、VS Code の再起動が必要だ。再起動を促される。

コマンド :guilabel:`Configure Display Language` は、ユーザー VS Code フォルダー
:file:`.vscode` 内のファイル :file:`argv.json` に書き込まれる。

ファイル :file:`argv.json` を直接編集し、VS Code を再起動することでもロケールを
変更可能だ。これにはコマンド :guilabel:`Preferences: Configure Runtime Arguments`
を実行し、当該ファイル :file:`%USERPROFILE%\\argv.json` を Editor で開くといい。

利用可能なロケール
======================================================================

上述のコマンドを実行することで確認可能だ。

Marketplace Language Packs
======================================================================

英語以外のロケールは Marketplace Language Packs で利用可能だ。Language Packs は
:guilabel:`EXTENSIONS` ビューで、言語名と :code:`category:"Language Packs"` を入
力して検索する。

Language Packs を複数インストールすることができる。コマンド
:guilabel:`Configure Display Language` を実行して、現在の UI 言語を選択できるよ
うになる。

UI 言語を設定する
======================================================================

VS Code セッションで特定のロケールを使用したい場合、コマンドラインオプション
``--locale`` を使用すると、VS Code 起動時にロケールを指定することができる。次の
例はコマンドラインオプション ``--locale`` を使用して、VS Code の UI 言語をフラン
ス語に設定するものだ：

.. code:: console

   bash$ code . --locale=fr

このようにコマンドラインオプションで言語指定をする場合には、適切な Language Pack
がインストールされている必要がある。合致するものがインストールされていない場合、
VS Code の UI は英語で表示される。
