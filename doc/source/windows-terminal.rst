======================================================================
Windows Terminal 利用ノート
======================================================================

`Windows Terminal <https://aka.ms/terminal>`__ はさまざまな CLI プロセス群を一箇
所にまとめることができる便利なソフトウェアだ。

* タブインターフェイス、
* ウィンドウ分割ペイン、
* Unicode/UTF-8 対応、
* GPU による高速レンダリング、
* テーマ（配色、フォント）、
* ショートカットキー設定

など、機能を豊富に備えている。

.. note::

   :Version: 1.14.2281.0
   :OS: Windows 10 Home

.. contents::

インストールする
======================================================================

Windows Terminal をインストールには複数の方法が用意されているようだが、次のどち
らかが望ましい。

* Microsoft Store 経由でインストール
* Windows 標準のコマンドライン上などから :program:`winget` でインストール

新マシンでのインストール手段は、旧マシンで :command:`winget export` したプログラ
ムリストを :command:`winget import` してインストールすることを想定している。

アップグレードする
======================================================================

Windows Terminal は自動更新機能を実装していないようなので、採用したインストール
手段に対応したアップグレード手段を採る。

* Microsoft Store の更新ボタンを押す
* コマンド :command:`winget upgrade` を実行する

設定をバックアップする
======================================================================

Windows Terminal の設定内容は次のパスで示される JSON ファイルに保存されている。
これをバックアップなりバージョン管理するだけだ。

.. code:: text

   %LOCALAPPDATA%\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json

.. warning::

   厳密に言うと、Windows Terminal のインストール方法によってパスに差異がある。
   現物を確認してから JSON ファイルを操作すること。

使用方法
======================================================================

初めて Windows Terminal を起動したときには設定が出荷時のものに過ぎないから、おそ
らく使い物にならない。後述の構成設定を適宜済ませてから、再度メインウィンドウに戻
る。

Windows Terminal を適切に構成すると、メインウィンドウにタブが一つ以上表示される。
各タブが何らかのコンソール画面に対応しているので、作業したいものをアクティブにして、
コマンドライン操作をすればいい。

Windows Terminal を終了する必要がある場合には、すべてのタブに対するコンソール上
でシェル固有の :command:`exit` コマンドを実行するか、メインウィンドウ自体をバツ
ボタンを押すなどする。

構成設定
======================================================================

Windows Terminal の設定は上述の JSON ファイルを直接的に編集するか、設定画面経由
で間接的に編集することで実現する。設定画面を表示するには、メインウィンドウのメ
ニューバー的なところの :guilabel:`v` をクリックすると出現するメニュー内にある項目
:guilabel:`設定` を選択する。

以下、要となるオプションのみを記す。

Startup
    Windows Terminal 起動時に影響するオプションを決定する。

    * :guilabel:`Default profile`: :guilabel:`Bash (WSL2)`
    * :guilabel:`When Terminal starts`: :guilabel:`Open a tab with the default profile`
    * :guilabel:`Launch size` で列数（横）と行数を適宜指定する。
Interaction
    Windows Terminal と私との間に起こる動作に影響するオプションを選択する。

    * :guilabel:`Automatically copy selection to clipboard`: OFF
    * :guilabel:`Text format when copying`: :guilabel:`Plain text only`
    * :guilabel:`Remove trailing white-space in rectangular selection`: ON
    * :guilabel:`Remove trailing white-space when pasting`: ON
    * :guilabel:`Snap window resizing to character grid`: ON
    * :guilabel:`Automatically focus pane on mouse hover`: OFF
    * :guilabel:`Automatically detect URLs and make them clickable`: ON
Appearance
    Windows Terminal の見てくれを調整するオプション画面だ。

    どのソフトウェアを使うときにも言えることだが、
    Google 検索で調べ物をするときの便宜を図るべく、UI を英語にしておく。
    そして、見てくれの調整に注力して時間を浪費するようなことは避ける。

    * :guilabel:`Language (requires relaunch)`: :guilabel:`English (United States)`
    * :guilabel:`Always show tabs`: ON
    * :guilabel:`Hide the title bar (requires relaunch)`: OFF
    * :guilabel:`Always on top`: OFF
    * :guilabel:`Tab width mode` を好みの値に設定。
    * :guilabel:`Pane animations`: OFF
Color schemes
    Windows Terminal の配色を調整する、あるいは配色全体を定義するための画面だ。
    したがって、ここに手を出す必要はない。
Rendering
    Windows Terminal の描画効率最適化を図る項目からなる画面だが、素人お断りとい
    う空気だ。全部既定値のままでよかろう。
Actions
    Windows Terminal で定義されているショートカットキーの集合だ。
    常用するシェルのキーバインドと衝突するものがないかどうかを確認しておくべきだ。
    反対に、ここにあるコマンドで有用なものは是非習得するべきだ。それは後述する。

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
        * :guilabel:`Scrollbar visibility`: :guilabel:`Visible`
    :guilabel:`Advanced`
        どの範疇にも該当しないような設定項目の居場所となる画面だ。

        * :guilabel:`History size`: 大きい数字にしておく。
        * :guilabel:`Profile termination behavior`: 場合によっては無条件に閉じる
          でいいかもしれない。
プロファイル個別画面
    私の現在の環境では Bash (WSL2), Windows Powershell, cmd, etc. と並んでいる。
    どの設定画面も項目の構造に差異はないので、まとめて説明する。

    * :guilabel:`Command Line` は念入りに確認しておく。WSL2 の場合には
      :code:`wsl.exe ~ -d Ubuntu` のように指定しておく。
    * :guilabel:`Icon` は適宜指定しておく。見てくれに関する項目ではあるが、他人
      に画面を見せるときにわかりやすさが圧倒的に良くなるので、明示的にファイルパ
      スを与える。

    :guilabel:`Appearance`, :guilabel:`Advanced` 各サブ画面については先述のとお
    り。ただし :guilabel:`Run this profile as Administrator` については ON に上
    書きするプロファイルが考えられる。管理者権限で起動したい :program:`cmd` など
    があり得る。

覚えておきたい Windows Terminal 内コマンド
======================================================================

最初のうちは次のものだけでいい。そのうち画面分割とかに手を出し始めたら関連コマン
ドを習得するようにしても間に合う。

.. csv-table::
   :delim: @
   :header: コマンド,ショートカットキー

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

インストール形態にもよるが、Windows Terminal をコマンドラインから起動する場合には、
次のようなコマンドライン引数およびオプションを与えることもできる：

.. code:: text

   wt.exe [options] [command ; ]

これを使う状況というのは、普段とは異なる構成で Windows Terminal を起動するときに
限られるだろう。この機能にはまだ手を出さなくていいだろう。

細かい機能
======================================================================

タブを右クリックすると、専用コンテキストメニューが表示される。これを使って、タブ
のラベル文字列を編集したり、色を変更したりできる。

マウスはテキスト選択以外にも、キーボード操作と組み合わせてズームや背景の透明度調
整に利用できる。これらの機能はむしろ無効化したい。

マウスを URL 上にホバーさせると下線が出てくる。この状態で :kbd:`Ctrl` キーを押し
つつクリックすると、そのページが Web ブラウザー内に開く。

その他
======================================================================

Windows Terminal にはアクション、画面分割など、拡張性のある機能が他にもまだ存在
するし、マウス操作でのテキスト選択、Quake モードなどのまだ見ぬ機能も残っている。
しかし、本ノートではそこまで踏み込まないことにする。これまでに記した内容で十分な
作業効率が確保できる。

関連ノート
======================================================================

:doc:`/winget`
    :program:`winget` を Windows Terminal をインストール・アップグレードするのに
    使う可能性が高い。
