======================================================================
Command Not Found 利用ノート
======================================================================

本稿は PowerToys 内 Command Not Found に関する記述だ。

.. attention::

   :doc:`./index` 冒頭の前提条件に留意すること。

.. contents:: 見出し一覧
   :local:

概要
======================================================================

設定画面の記述によると、次のようにある：

   A PowerShell module that detects an error thrown by a command and suggests a
   relevant WinGet package to install, if available.

PowerShell の実行コードが例外を送出したとき、それが何らかの WinGet パッケージさ
え環境に存在すれば対処可能になるものであれば、そのパッケージのインストールを促す
という機能を備えた PowerShell モジュールだろう。

実際には、PowerShell 環境にモジュール ``Microsoft.WinGet.CommandNotFound`` をイ
ンストールし、スタータップファイルに次の有効化コードを追加するという動作をする：

.. sourcecode:: pwsh
   :caption: :file:`Microsoft.PowerShell_profile.ps1` に追加されるコード
   :force:

   #f45873b3-b655-43a6-b217-97c00aa0db58 PowerToys CommandNotFound module

   Import-Module -Name Microsoft.WinGet.CommandNotFound
   #f45873b3-b655-43a6-b217-97c00aa0db58

.. admonition:: 利用者ノート

   * モジュールのインストール場所をユーザーインストールでなく、システムインス
     トールに変えられないだろうか？
   * WSL イメージファイルの容量削減を試みたときに、関連機能がないことがあったが、
     これを用いていれば :program:`diskpart` を使わずに済んだのか。

インストール方法
======================================================================

Command Not Found 設定画面の :guilabel:`Install` ボタンを押せば必要な資材がシス
テムにダウンロードされる。

.. sourcecode:: text
   :caption: インストールメッセージ

   Enabling experimental feature: PSFeedbackProvider
   WARNING: Enabling and disabling experimental features do not take effect until next start of PowerShell.
   WinGet Client module detected
   Microsoft.WinGet.CommandNotFound was not found. Installing...

   Microsoft.WinGet.CommandNotFound module installed

   Module was successfully registered in the profile file.

インストールには事前条件があり、例えば PowerShell のバージョンが 7.4 以上でなけ
ればならない。

.. 以上
