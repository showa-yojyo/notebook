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

インストール直後の最初にやるべきこと
======================================================================

VS Code をインストールしてまずは普通の Windows アプリケーションと同様に実行する。


公式文書群に目を通す
----------------------------------------------------------------------

ブラウザーで `Documentation for Visual Studio Code <https://code.visualstudio.com/docs>`__
以下にある文書群すべてを閲覧するのがいいだろう。画面左側の列に見出しがあるが、そ
のうち次のものは絶対に一読するべきだ。

Overview
    特に `Intro Videos <https://code.visualstudio.com/docs/getstarted/introvideos>`__
    は全編視聴するといい。言葉だけの説明では伝わらない部分を映像で補うことができる。
SETUP
    なにはさておき VS Code を利用可能な状態に持っていかねばならない。
GET STARTED
    VS Code にまつわる基本的な用語をまずは習得する。
USER GUIDE
    一読だけではなく、後で何度もここに戻ってくる。
SOURCE CONTROL
    Git を念頭に置くことになるが、バージョン管理システムとの連携を理解する。
TERMINAL
    内蔵コンソールの特徴を知っておく。

なお、本ノートはこの構成に可能な限り則って VS Code の諸要素について述べていく。

Get Started にある一連の課題を消化する
----------------------------------------------------------------------

VS Code メインメニューの :guilabel:`Help / Get Started` を開く。使い始めの頃は
Welcome ページの右側に Walkthroughs というものが出てくる。
これらのチュートリアルを一つ一つ愚直に消化することで VS Code 上の作業を体に覚え込ませる。
あとで拡張機能をインストールするときに、ここに Walkthrough が追加されることもある。

また、:guilabel:`Help / Editor Playground` を開いて、VS Code の特徴的な編集機能各種を
説明とテキストフィールドで体感する。これを利用して、次の機能を会得する：

マルチカーソル編集
    ブロック選択、出現箇所全選択、カーソル追加などを試せる。
IntelliSense
    編集中のコードと外部モジュールに対する、コード支援と引数の提案をする機能である
    IntelliSense を試せる。
行アクション
    行を素速く移動して、コードの並び替えを行うチュートリアルだ。
リネームリファクタリング
    コードベース全体のシンボルの名前を高速に変更することができることを知る。
整形
    ドキュメントまたは選択に対する整形コマンドを習得する。
コード折りたたみ
    他の部分を折りたたんで、コードの最も関連性の高い部分に焦点を当てたいときに使える。
エラーと警告
    編集中にエラーと警告を表示する。
スニペット
    スニペットと呼ばれるコード片を使って編集時間を短縮する。
Emmet
    Emmet というコード補完機能の支援により、HTML/CSS 編集能力を次の水準へ引き上げる。
JavaScript 型チェック
    TypeScript を使用して JavaScript ファイルの型チェックを設定なしで実行する。

.. todo::

   理解・習得状況を確認できるようにチェックリストが欲しい。

..
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
