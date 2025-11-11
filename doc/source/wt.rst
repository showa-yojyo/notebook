======================================================================
Windows Terminal 利用ノート
======================================================================

.. |msstore| replace:: `Microsoft Store`_
.. |wt| replace:: `Windows Terminal`_

|wt| はさまざまな端末ウィンドウをそれらの親ウィンドウとしてまとめることができる
便利なソフトウェアだ。

* タブインターフェイス、
* ウィンドウ分割ペイン、
* Unicode/UTF-8 対応、
* GPU による高速レンダリング、
* テーマ（配色、フォント）、
* ショートカットキー設定

など、機能を豊富に備えている。

.. note::

   :Version: 1.14.2281.0, 1.23.12811.0.
   :OS: Windows 10 Home, Windows 11 Pro.

.. contents:: 見出し一覧
   :local:

インストールする
======================================================================

Windows 10 でインストールする場合
----------------------------------------------------------------------

|wt| をインストールには複数の方法が用意されているようだが、次のどちらかが望まし
い：

* |msstore| 経由でインストール
* Windows 標準のコマンドライン上などから :program:`winget` でインストール

.. sourcecode:: pwsh-session
   :caption: :program:`winget` を使うインストール方法（システムインストール不能）
   :force:

   PS> winget install -e --id Microsoft.WindowsTerminal

.. sourcecode:: text
   :caption: Windows Terminal の既定のインストールパス

   ``%LOCALAPPDATA%\Microsoft\WindowsApps\wt.exe

新マシンでのインストール手段は、旧マシンで :command:`winget export` したプログラ
ムリストを :command:`winget import` してインストールすることを想定している。

Windows 11 でインストールする場合
----------------------------------------------------------------------

Windows 11 では Home/Pro を問わず、|wt| があらかじめインストールされている。

アップグレードする
======================================================================

`Windows Terminal`_ 自身は自動更新機能を実装していないようなので、採用したインス
トール手段に対応したアップグレード手段を採る。

* |msstore| でインストールした場合には自動更新が有効ならそうなる。心配なら
  |msstore| の更新ボタンを押せばいい。
* :program:`winget` を利用してインストールした場合には ``winget upgrade`` を実行
  する。
* Windows 11 のインストール済みパッケージは |msstore| の機能により自動更新される
  だろう。

設定をバックアップする
======================================================================

|wt| の設定内容は次のパスで示される JSON ファイルに保存されている。これをバック
アップなりバージョン管理するだけだ。

.. sourcecode:: text
   :caption: Windows Terminal の既定の設定ファイルパス

   %LOCALAPPDATA%\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json

|wt| をアンインストールするとこの設定ファイルも失われる。間違いに備えてファイル
:file:`settings.json` を必ずバックアップをしろ。

アンインストールする
======================================================================

アンインストールしてはならない。話がややこしくなる。

使用方法
======================================================================

|wt| を初めて起動したときには設定が出荷時のものに過ぎないから、おそらく使い物に
ならない。後述の構成設定を適宜済ませてから、再度メインウィンドウに戻る。

|wt| を適切に構成すると、メインウィンドウにタブが一つ以上表示される。各タブが何
らかのコンソール画面に対応しているので、作業したいものをアクティブにして、コマン
ドライン操作をすればいい。

|wt| を終了する必要がある場合には、すべてのタブに対するコンソール上でシェル固有
の :command:`exit` コマンドを実行するか、メインウィンドウ自体をバツボタンを押す
などする。

構成設定
======================================================================

|wt| の設定は上述の JSON ファイルを直接的に編集するか、設定画面経由で間接的に編
集することで実現する。設定画面を表示するには、メインウィンドウのメニューバー的な
ところの :guilabel:`v` をクリックすると出現するメニュー内にある項目
:menuselection:`Settings` を選択する。

以下、要となるオプションのみを記す。

:guilabel:`Startup`
    |wt| 起動時に影響するオプションを決定する。

    * :guilabel:`Default profile`: :guilabel:`Ubuntu`
    * :guilabel:`Language`: :guilabel:`English (United States)`
    * :guilabel:`When Terminal starts`: :guilabel:`Open a tab with the default profile`
    * :guilabel:`New instance behavior`: :guilabel:`Attach to the most recently used window`
    * :guilabel:`Launch size` で列数（横）と行数を適宜指定する。
:guilabel:`Interaction`
    |wt| と私との間に起こる動作に影響するオプションを選択する。ここは既定値のま
    までよかろう。
:guilabel:`Appearance`
    |wt| の見てくれを調整するオプション画面だ。

    どのソフトウェアを使うときにも言えることだが、Google 検索で調べ物をするとき
    の便宜を図るべく、UI を英語にしておく。そして、見てくれの調整に注力して時間
    を浪費するようなことは避ける。

    * :guilabel:`Application Theme`: :guilabel:`Use Windows theme`
    * :guilabel:`Use acrylic material in the tab row`: OFF
    * :guilabel:`Tab width mode`: :guilabel:`Compact`
    * :guilabel:`Pane animations`: OFF
:guilabel:`Color schemes`
    |wt| の配色を調整する、あるいは配色全体を定義するための画面だ。したがって、
    ここに手を出す必要はない。
:guilabel:`Rendering`
    |wt| の描画効率最適化を図る項目からなる画面だが、素人お断りという空気だ。全
    部既定値のままでよかろう。
:guilabel:`Compatibility`
    触らないでおく。
:guilabel:`Actions`
    |wt| で定義されているショートカットキーの集合だ。常用するシェルのキーバイン
    ドと衝突するものがないかどうかを確認しておくべきだ。反対に、ここにあるコマン
    ドで有用なものは是非習得するべきだ。それは後述する。
:guilabel:`New Tab Menu`
    初期状態で問題ないが、要らないプロファイルを削るために編集してもかまわない。

Profiles
----------------------------------------------------------------------

:guilabel:`Defaults` とプロファイル個別の設定を二段構えで指定する構えを取っている。
前者でコンソールすべてに共通する設定をし、後者でシェルごとの設定項目を上書きする
と考えればいい。

:guilabel:`Defaults`
    コンソールすべてに共通する設定をする。

    :guilabel:`Run this profile as Administrator`: OFF

    :guilabel:`Appearance`
        コンソール画面すべてに共通する設定項目の集合。

        * :guilabel:`Font face`: こだわりのフォントがあるならば設定してもよい。
        * :guilabel:`Font size`: 上記に合わせて指定する。
        * :guilabel:`Cursor shape`: キャレットの形状を指定する。
        * :guilabel:`Cursor color`: ``#rrggbb`` 形式でいったん指定しておき、JSON
          ファイルで最終調整するのがよい。
        * :guilabel:`Scrollbar visibility`: :guilabel:`Always`
    :guilabel:`Advanced`
        どの範疇にも該当しないような設定項目の居場所となる画面だ。

        * :guilabel:`History size`: 小さい数にしない。
        * :guilabel:`Profile termination behavior`: `Automatic` で問題ないが、場
          合によっては :guilabel:`Close only when ...` でいいかもしれない。
        * :guilabel:`Display marks on the scrollbar`: ON にすると便利。
プロファイル個別画面
    私の現在の環境では Ubuntu, PowerShell, Command Prompt と並んでいる。どの設定
    画面も項目の構造に差異はないので、まとめて説明する。

    :guilabel:`Command Line` は念入りに確認しておく。Ubuntu の場合には

    .. sourcecode:: text

       wsl.exe ~ -d Ubuntu

    のように指定しておく。初期値のままではわかりにくい。

    UI 言語を英語にした手前、:guilabel:`コマンド プロンプト` のプロファイル名を
    ``Command Prompt`` に変更しておく。

覚えておきたい Windows Terminal 内コマンド
======================================================================

最初のうちは次のものだけでいい。そのうち画面分割とかに手を出し始めたら関連コマン
ドを習得するようにしても間に合う。

.. csv-table::
   :delim: @
   :header-rows: 1
   :widths: auto

   コマンド @ ショートカットキー
   テキスト全選択 @ :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`A`
   検索 @ :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`F`
   少量だけ上へスクロール @ :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`↑`
   少量だけ下へスクロール @ :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`↓`
   ページ高だけ上へスクロール @ :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`PgUp`
   ページ高だけ下へスクロール @ :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`PgDn`
   コンソール画面の最上部に移動 @ :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`Home`
   コンソール画面の最下部に移動 @ :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`End`
   設定画面タブを開く @ :kbd:`Ctrl` + :kbd:`,`
   設定 JSON ファイルを開く @ :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`,`

.. note::

   コンソール内でのキャレット移動は、各対話的シェルに関する設定に従う。

Windows Terminal 自身へのコマンドライン引数
======================================================================

|wt| を :guilabel:`ファイル名を指定して実行ダイアログ` やコマンドラインから起動
する場合には、次のようなコマンドライン引数およびオプションを与えることもできる：

.. code:: text

   wt.exe [options] [command ; ]

これを使う状況というのは、普段とは異なる構成で |wt| を起動するときに限られるだろ
う。この機能にはまだ手を出さなくていいだろう。

細かい機能
======================================================================

タブを右クリックすると、専用コンテキストメニューが表示される。これを使って、タブ
のラベル文字列を編集したり、色を変更したりできる。

マウスはテキスト選択以外にも、キーボード操作と組み合わせてズームや背景の透明度調
整に利用できる。しかし、これらの機能はむしろ無効化したい。

マウスカーソルを URL 上にホバーさせると下線が出てくる。通常設定ならばこの状態で
:kbd:`Ctrl` を押しつつクリックすると、そのページが Web ブラウザー内に開く。

その他
======================================================================

|wt| にはアクション、画面分割など、拡張性のある機能が他にもまだ存在するし、マウ
ス操作でのテキスト選択、Quake モードなどのまだ見ぬ機能も残っている。しかし、本
ノートではそこまで踏み込まないことにする。これまでに記した内容で十分な作業効率が
確保できる。

.. _Windows Terminal: https://aka.ms/terminal
.. _Microsoft Store: https://apps.microsoft.com/home
