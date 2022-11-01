======================================================================
Visual Studio Code 利用ノート
======================================================================

いつの間にかメインのテキストエディターが `Visual Studio Code
<https://code.visualstudio.com/>`__ になっているので、このへんで知識を整理しよう。

.. attention::

   次の環境・条件で VS Code を利用していることを先に断っておく。

   OS は Windows 10 Home で、WSL (Ubuntu) のファイルシステムにあるファイルを主に
   編集する。Git を中心とするコンソールコマンドは Ubuntu にあるものを実行する。

   バージョン管理ツールは Git しか使わない。他の SCM まで調査の手が回らない。

   VS Code の GUI は英語のまま変えない。

.. toctree::
   :maxdepth: 2

   first
   setup
   extensions
   basics
   navigation
   cli
   intellisense
   refactoring
   debugging
   tasks
   snippets
   emmet
   git
   terminal

..
    GitHub と連携する？
    -- 以下、Getting Started 内にあるか、漏れた項目 --
    UI -- これは本サイトを見ろとしか言えない
        レイアウト
        エディターを水平方向に増やせる workbench.editor.openSideBySideDirection
        ミニマップ
        パンクズ
        エクスプローラー
            OPEN EDITORS
        ビュー
        コマンドパレット
        タブ
            プレビューモード（殺す）
        グループ
        フレームウィンドウ全体
    settings.json
        既定値
        JSON ファイルの絶対パス
        編集
            GUI
            エディター
        推奨設定
        拡張機能に関する設定に注意
    テーマ
        色テーマ Preferences: Color Theme
        色をカスタマイズ
            workbench.colorCustomizations
            editor.tokenColorCustomizations
        自作テーマ
        削除
        アイコンテーマ
    キーバインド
        Keyboard Shortcuts 画面
        キーバインドの衝突を検知する
        自分で変えたキーバインドを検知する
        keybindings.json
        特定のキーバインドを無効化する
        初期状態のキーバインドを表示する
    言語
        英語一択
