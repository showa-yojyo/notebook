======================================================================
Visual Studio Code 利用ノート
======================================================================

いつの間にかメインのテキストエディターが `Visual Studio Code
<https://code.visualstudio.com/>`__ になっているので、このへんで知識を整理しよう。

.. attention::

   次の環境・条件で VS Code を利用していることを先に断っておく。

   OS は Windows 10 Home で、WSL (Ubuntu) のファイルシステムにあるファイルを主に編集する。
   Git を中心とするコンソールコマンドは Ubuntu にあるものを実行する前提だ。

   VS Code の GUI は英語のまま変えていない。

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

..
    [DONE] first
    [DONE] setup
    [DONE] extensions
    [DONE] basics
    [DONE] navigation
    [DONE] cli
    [DONE] intellisense
    [DONE] refactoring
    [DONE] debugging
    [DONE] tasks
    [WIP] snippets
    テキスト補完系
        Emmet
            概念（普通の意味での補完）
            変数置換
            後処理
            自作 snippets.json
    ----
    バージョン管理 Git 前提
        ステージ操作
            コミット
        リポジトリー操作
            クローン
            ブランチとタグ
            リモート
        ステータスバー
        エディター
        コンフリクト表示
        差分表示
        タイムラインビュー
        拡張機能
        出力確認
        Git の設定に VS Code を指定する
            コミットログエディター
            差分ビューワー
            マージエディター
    GitHub と連携する？
    ----
    コンソール
        画面を出す
        複数シェルに対応
        コンソール管理
        画面を分割
        エディターの横に出す
        ナビゲーション（スクロール）
        コピー＆ペースト
        マウス操作
        検索
        Terminal: Run Selected Text in Active Terminal
        巨大表示
        全選択
        pwd
        画面サイズ固定
        プロファイル
            WSL
        見てくれ
        高級機能
            セッション
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
