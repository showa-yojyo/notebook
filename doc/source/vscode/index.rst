======================================================================
Visual Studio Code 利用ノート
======================================================================

いつの間にかメインのテキストエディターが `Visual Studio Code
<https://code.visualstudio.com/>`__ になっているので、このへんで知識を整理しよう。

.. toctree::
   :maxdepth: 2

..
    事前条件
        Windows + WSL
        Awesome Emacs Keymap を利用していること
    初心者の館
        公式文書群
        `ビデオ <https://code.visualstudio.com/docs/getstarted/introvideos>`__
        Help
            Walkthroughs
            Editor Playground
        基本概念
            コマンドパレット
            etc.
    セットアップ
        インストール
        更新
        バックアップ
        復元
        アンインストール
            プログラムの追加と削除から、等々
            手動で削除する必要があるファイル群
    拡張機能（先に触れる必要がある）
        View: Extensions
        インストール・アンインストール
        EXTENSIONS: MARKETPLACE コンテキストメニューコマンド
        検索
        管理
            有効・無効を切り替える
            更新
            推奨パック
            無視パック
        拡張単位を構成
        コマンドライン
    基本編ということになっている（順序を入れ替えたい）
        テキスト編集
            複数キャレット・選択
            スマート選択 (Shift+Alt+←/Shift+Alt+→)
            列選択モード (Ctrl+Shift+Alt+矢印)
        保存
            自動保存
            Hot Exit
        検索と置換
            選択範囲に操作対象を絞れる
            Find/Replace In Files (Ctrl+Shift+F/Ctrl+Shift+H)
            正規表現などの高級なオプション
            検索エディター Open Search Editor, etc.
        整形 Format Document, Format Selection
        畳み込み Folding (Ctrl+Shift+[/Ctrl+Shift+])
        インデント
            自動検出
        エンコーディング
    ナビゲーション（エディター内移動）
        View: Quick Open (Ctrl+Tab/Ctrl+Shift+Tab)
        Go Back/Go Forward (Alt+Left/Alt+Right)
        パンクズ (breadcrumbs.enabled)
        Go to Definition (F12)
        Go to Implementation (Ctrl+F12)
        Go to Symbol (Ctrl+Shift+O)
        Go to References (Shift+F12)
        Peek Definition (Alt+F12)
        Peek Implementation (Ctrl+Shift+F12)
        Go to Bracket (editor.action.jumoToBracket Ctrl+Shift+\)
        Go to Next/Previous Problem (Shift+/Alt+/F8, etc.)
    コマンドライン (code)
        コマンドラインオプション
        本体起動
        拡張機能関連
    IntelliSense
        IntelliSense の役割
        発動方法
    リファクタリング（短く）
        Code Actions (editor.action.codeAction)
        Quick fix
        Extract method/variable
        Rename symbol
    デバッグ（長い）
        実行＆デバッグ
        構成
        デバッグコマンド
            ツールバーに示される基本コマンド群
        ブレイクポイント
            ログポイント
            先進的なブレイクポイント
        ウォッチ
            変数（生の値）
            ウォッチ（評価アリ）
        デバッグコンソール
        etc.
    タスク（長い）
        概要あるいは Hello world
        Tasks: Run Build Task (Ctrl+Shift+B)
        自作タスク
        問題
        例
    テキスト補完系
        スニペッツ
            概念（構文とスコープ）
            組み込みスニペッツ
            自作スニペッツ
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
