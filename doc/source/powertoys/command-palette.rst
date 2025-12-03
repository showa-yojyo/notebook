======================================================================
Command Palette 利用ノート
======================================================================

.. |pt| replace:: PowerToys
.. |palette| replace:: `Command Palette`_
.. |kb| replace:: :kbd:`Win`

.. |Enter| replace:: :kbd:`Enter`
.. |Shift| replace:: :kbd:`Shift`
.. |Ctrl| replace:: :kbd:`Ctrl`
.. |Del| replace:: :kbd:`Delete`
.. |Ctrl+Shift| replace:: :kbd:`Ctrl` + :kbd:`Shift`

本稿は |pt| の |palette| 機能に関する記述だ。

.. attention::

   :doc:`./index` 冒頭の前提条件に留意すること。

.. contents:: 見出し一覧
   :local:

概要
======================================================================

|palette| はデスクトップからアプリケーションやコマンドをタイプ入力で起動する設計
のランチャーだ。Windows における :kbd:`Win` + :kbd:`R` を押すと開くダイアログ
ボックス（ファイル名を指定して実行）の上級使用者向けという意識のある機能だと考え
られる。

|palette| には次の機能がある：

* Windows の :guilabel:`ファイル名を指定して実行` に備わる機能

  * アプリケーション、フォルダー、ファイルを検索する
  * コマンドを実行する (e.g., :command:`cmd`, :command:`Shell:startup`)
  * システムコマンドを実行する
  * Web ページを開く
* 開いているウィンドウを切り替える
* 電卓で簡単な計算を行う
* Web ページにブックマークを追加する
* Web 検索

使用法
======================================================================

以下、ランチャー UI を発射ウィンドウと記す。

#. 発射ウィンドウを開く
#. 入力欄で適当にタイプする or 発射項目を一覧から指定してからタイプする

発射ウィンドウを開く方法は複数ある。例えば：

* キーバインドを押す
* タスクトレイアイコンをクリックする

タイプしている途中に |palette| が文字列から適切な処理となるように残りの文字列を
補完し、ウィンドウ内に何を行うかを示す。使用者はそれを見て納得してから |Enter|
を押して実行する。アプリケーションが走ったり、Windows Explorer やブラウザーが開
いたりするだろう。

入力
======================================================================

入力欄に文字をタイプするときの挙動は、おそらく次のようなものだと考えられる：

#. 効力のある拡張のすべてが、入力途中の文字列に基づいて固有の曖昧検索する。
#. それぞれの拡張の暫定的な検索結果が発射候補一覧にすべて現れる。

使用者はタイプを途中で止めるのが普通で、一覧の中から所望の結果項目をキーボードや
マウスで選択し、発射ウィンドウ右下のコンテキストガイドに従ってさらなる操作を行う。

発射構文
----------------------------------------------------------------------

発射ウィンドウの入力欄で入力する文字列のうち、特別に処理される構文を次に記す：

.. csv-table::
   :delim: @
   :header-rows: 1
   :widths: auto

   構文 @ 実行
   :samp:`> {command-line}` @ コマンド :samp:`{command-line}` を実行
   :samp:`?? {query}` @ Web 検索エンジンに :samp:`query` を検索させてブラウザーを開く
   :samp:`file {query}` @ ファイルやフォルダーを検索して開く
   :samp:`= {expr}` @ 数式を評価
   :samp:`$` @ Windows 設定発射モード
   :samp:`<` @ 走行中プログラムを検索
   :samp:`:` @ Windows レジストリーのキーを検索
   :samp:`)` @ 日付、時刻を適当な書式で出力

設定により、特別処理それぞれの On/Off を切り替えることが可能だ。

発射項目
----------------------------------------------------------------------

本節では既定構成で発射対象を探し出す拡張を記す。

.. _anchor-pt-palette-all-apps:

All Apps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

この発射拡張はシステムにインストールされているアプリケーションを補完して検索候補
一覧に追加する。対象アプリケーション集合に関しては記述を割愛する。

通常の操作はアプリケーションを実行するものだが、キーバインドやコンテキストメ
ニューを用いることで対象アプリケーションに対する他の操作も可能だ。例えば次の操作
が可能だ：

.. csv-table::
   :delim: @
   :header-rows: 1
   :widths: auto

   キーバインド @ 操作
   |Enter| @ 実行する
   |Ctrl+Shift| + |Enter| @ 管理者として実行する
   |Ctrl+Shift| + :kbd:`U` @ 別のユーザーとして実行する
   |Ctrl+Shift| + :kbd:`C` @ パスをクリップボードにコピーする
   |Ctrl+Shift| + :kbd:`E` @ 実行ファイルの場所を Windows Explorer で開く
   |Ctrl+Shift| + :kbd:`R` @ 実行ファイルの場所を :program:`cmd` で開く
   |Ctrl+Shift| + |Del| @ アンインストールする
   |Ctrl| + :kbd:`P` @ 項目の一覧におけるピン留めを切り替える

.. https://github.com/microsoft/PowerToys/blob/main/doc/devdocs/modules/launcher/plugins/program.md

Run commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

発射拡張 Run commands はコマンドを補完し、実行またはその他の操作を行う。おそらく
Windows の Run ダイアログボックスが受け付ける入力をすべて受け入れると考えられる。

通常の操作はコマンドを実行するものだが、キーバインドやコンテキストメニューを用い
ることで対象コマンドに対する他の操作も可能だ。:ref:`anchor-pt-palette-all-apps`
の表と似ているので割愛する。

.. https://github.com/microsoft/PowerToys/blob/main/doc/devdocs/modules/launcher/plugins/shell.md

Calculator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

発射拡張 Calculator は入力した数式を評価して一覧部分に出力する。評価に対して可能
な操作は次のとおり：

.. csv-table::
   :delim: @
   :header-rows: 1
   :widths: auto

   キーバインド @ 操作
   |Enter| @ クリップボードに保存する
   |Ctrl| + |Enter| @ 電卓用一覧に保存する

また、評価をコンテキストメニューから十六進数表記と二進数表記を確認できる。

.. todo::

   この電卓の構文や関数の仕様は？

Search files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

発射拡張 Search files はファイルシステムに存在するファイルを対象とする。

.. csv-table::
   :delim: @
   :header-rows: 1
   :widths: auto

   キーバインド @ 操作
   |Enter| @ 開く
   |Ctrl| + |Enter| @ プログラムを選択して開く
   |Ctrl+Shift| + :kbd:`C` @ パスをクリップボードにコピーする
   |Ctrl+Shift| + :kbd:`E` @ ファイルの場所を Windows Explorer で開く
   |Ctrl+Shift| + :kbd:`R` @ ファイルの場所を :program:`cmd` で開く

Add bookmark
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

発射拡張 Add bookmark を拡張一覧から選択して |Enter| を押すと、ブックマーク追加
UI が一覧表示領域に現れる。

入力中に発射候補一覧に現れた既存のブックマーク項目に対しては、次の操作などが可能
だ：

.. csv-table::
   :delim: @
   :header-rows: 1
   :widths: auto

   キーバインド @ 操作
   |Enter| @ 対象ページを開く
   |Ctrl| + |Enter| @ 対象ブックマークの URL またはパスをクリップボードにコピーする
   |Ctrl+Shift| + :kbd:`C`: @ 同上
   |Ctrl+Shift| + |Del| @ 対象ブックマークを削除する

Switch between open windows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

発射拡張 Switch between open windows は Windows 標準機能である Task Switcher の
上位互換機能だ。次のように用いる：

#. 当項目を一覧から選択するか、入力欄一文字目に ``<`` をタイプする
#. 所望のアプリケーション名を一覧から選択する（入力欄にその文字列をタイプして
   絞り込める）

次の操作が可能（ウィンドウが最小化されていないと操作しやすい）：

.. csv-table::
   :delim: @
   :header-rows: 1
   :widths: auto

   キーバインド @ 操作
   |Enter| @ 対象ウィンドウに切り替える
   |Ctrl| + |Enter| @ 対象ウィンドウを閉じる
   |Ctrl| + |Del| @ 対象ウィンドウのプロセスを殺す

.. https://github.com/microsoft/PowerToys/blob/main/doc/devdocs/modules/launcher/plugins/windowwalker.md

Search the Web
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

発射拡張 Search the Web は本稿執筆時点ではまったく使い物にならない。GitHub で
コード履歴を見ると開発進行中のようだ。しばらくしてから調査、評価する。

.. https://github.com/microsoft/PowerToys/blob/main/doc/devdocs/modules/launcher/plugins/websearch.md

Clipboard History
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

発射拡張 Clipboard History は発射一覧にクリップボード履歴項目を並べる。この一覧
項目を選択すると次の操作が可能になる：

.. csv-table::
   :delim: @
   :header-rows: 1
   :widths: auto

   キーバインド @ 操作
   |Enter| @ クリップボードの内容をこの値で上書きする
   |Ctrl| + |Enter| @ さらに貼り付ける
   |Ctrl| + :kbd:`O` @ クリップボード内容が URL やファイルパスの場合にその対象を開く
   |Ctrl+Shift| + |Del| @ クリップボード項目を履歴から削除する

Search WinGet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

発射拡張 Search WinGet はおそらく ``winget search`` を実行して結果を一覧に出力す
る。一覧項目から実行可能な操作は、パッケージがシステムに存在するか否かで変化す
る。

インストール済みのパッケージに対しては、:ref:`anchor-pt-palette-all-apps` と同様
の操作が可能だ。

インストールされていないパッケージに対しては、|Enter| 一発でインストール操作が可
能となる。ただ、:program:`winget` でパッケージをインストールするときのオプション
を指定する UI が見当たらない。

Windows Terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

発射拡張 Windows Terminal はそのプロファイルを発射する。アプリケーション Windows
Terminal の設定で開くことが可能なすべてのプロファイルを発射可能だ。

候補一覧にある項目を選択すると、次の操作が可能になる：

.. csv-table::
   :delim: @
   :header-rows: 1
   :widths: auto

   キーバインド @ 操作
   |Enter| @ セッションを開く
   |Ctrl| + |Enter| @ 管理者権限でセッションを開く

ウィンドウの開き方（新規ウィンドウなのか新規タブなのか）はアプリケーション側の設
定に従う。

Windows Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

発射拡張 Windows Settings では次の三つの類型から Windows 設定アプリケーションを
検索して発射する：

* 設定 (``ms-settings:``)
* コントロールパネル (:program:`control.exe`)
* Microsoft 管理コンソール (:program:`mmc.exe`)

.. admonition:: 利用者ノート

   アプリケーションを発射するよりも、その実行ファイル名を知るのに有用な拡張かも
   しれない。例えば ``.msc`` と入力欄にタイプすると、一覧の内容は次のようになる
   だろう：

   .. sourcecode::
      :caption: Windows Settings 発射拡張にて ``.msc`` で絞り込む

      TPM 管理
      WMI コントロール
      イベント ビューアー
      コンピューター管理
      コンポーネント サービス
      サービス
      ...

   ここから所望の項目を見つけ、|Ctrl| + |Enter| を押すと実行ファイル名がクリップ
   ボードの内容になる。例えば「ディスクの管理」ならば :file:`diskmgmt.msc` だと
   わかるという具合だ。

.. https://github.com/microsoft/PowerToys/blob/main/doc/devdocs/modules/launcher/plugins/windowssettings.md

Registry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

発射拡張 Registry は Windows Registry キーを補完するのに用いられる。例えば入力欄
で ``HKLM\HARD`` とタイプすると、候補一覧に ``HKEY_LOCAL_MACHINE\HARDWARE`` が現
れる。

候補一覧にある項目を選択すると、次の操作が可能になる：

.. csv-table::
   :delim: @
   :header-rows: 1
   :widths: auto

   キーバインド @ 操作
   |Enter| @ :program:`regedit` でキーを開く
   |Ctrl| + |Enter| @ キー名をクリップボードにコピーする

Windows Services
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

発射拡張 Windows Services が発射主体になると、OS サービスだけが発射候補一覧に挙
がる。このとき、発射ウィンドウの右上にドロップダウンリストが現れる。項目は次の四
つであり、対応する状態のサービスを絞り込んで一覧に示す：

* :guilabel:`All Services`
* :guilabel:`Running`
* :guilabel:`Stopped`
* :guilabel:`Paused`

対象サービスを決めたら、現在の状態が許す限りの操作を行うことが可能だ。例えば
稼働中のサービスに対しては停止するか、または開くことが可能だ。

この発射拡張はおそらく Windows :program:`services.msc` の上位互換機能を目指して
いる。

Time and Date
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

発射拡張 Time and Date は空入力に対しては現在の時刻をさまざまな書式を用いて一覧
に示す。有効な書式の入力に対しては、その値を一覧部分に出力する。

出力後、|Enter| を押せば値がクリップボードにコピーされる。

.. admonition:: 利用者ノート

   この発射拡張機能の書式機能を利用する場合は、UI 言語が英語でないと使い物になら
   ない。現在、|pt| の UI 言語が |palette| に適用されておらず、私が困っている。

.. https://github.com/microsoft/PowerToys/blob/main/doc/devdocs/modules/launcher/plugins/timedate.md

Windows System Command
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

発射拡張 Windows System Command は次のようなコマンドを直接実行する。オプション的
な動作は特になく、せいぜいクリップボードにコピーするのみだ。

* :command:`shutdown` 系操作：シャットダウン、再起動、ログアウト、休止
* ロック
* ゴミ箱操作：開く、空にする
* Windows Explorer を再起動する
* UEFI ファームウェアの設定
* IP / MAC アドレス項目ではネットワーク接続情報を確認する

.. https://github.com/microsoft/PowerToys/blob/main/doc/devdocs/modules/launcher/plugins/system.md

PowerToys 側設定画面
======================================================================

|palette| の設定画面は二つ設けられている。|pt| 本体のものと、発射ウィンドウ固有
のウィンドウに分かれている。本節では |pt| 側 UI を記す。

:guilabel:`Enable Command Palette`
   On にすることで |palette| 機能が活動する。すなわち、次に記す設定キーバインド
   を押すと画面に UI が登場する。

Activation
----------------------------------------------------------------------

:guilabel:`Activation shortcut`
    Command Palette 側設定画面を開くためのキーバインドを指定する。

    既定値 :kbd:`Win` + :kbd:`Alt` + :kbd:`Space` のままでいい。

Command Palette Settings ウィンドウ
======================================================================

発射ウィンドウの左下にある :guilabel:`Settings` アイコンを押すと開く設定ウィンド
ウの UI について記す。

Command Palette 固有の設定画面は :guilabel:`General` と :guilabel:`Extensions`
の二画面構成となっている。

.. admonition:: 利用者ノート

   |pt| での言語設定を英語にしても、OS での言語設定値が参照されてこの画面の UI
   文言が示されるようだ。未来の後世のバージョンで修正されることを信じていたい。

   UI 項目に付記されている文章は読みやすいが、項目名がなっていない。

General
----------------------------------------------------------------------

Activation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Activation key`
   PowerToys 側設定画面における同名項目と同一。
:guilabel:`Use low-level keyboard hook`
   Off でいい。
:guilabel:`Ignore shortcut in fullscreen mode`
   別プログラムを全画面表示にしていて、|palette| を使いたい場合があるならば、そ
   の場合に限り On にしろ。
:guilabel:`Go home when activated`
   Off でいい。都度 |kb| を押せ。
:guilabel:`Highlight search on activate`
   入力欄における前回入力文字列を活かしたい場合が少なければ Off のほうがいい。
:guilabel:`Preferred monitor position`
   この設定はモニターを複数用いている環境向けだ。どのモニターに対して |palette|
   を開くのかを次のいずれかに指定する：

   * :guilabel:`Monitor with mouse cursor`
   * :guilabel:`Primary monitor`
   * :guilabel:`Monitor with focused window`
   * :guilabel:`Don't move`

Behavior
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Show app details`
   On にすると、アプリケーションの検索中に UI の右側に検索結果候補項目の類型やパ
   スなどの情報を示すようになる。
:guilabel:`Backspace goes back`
   On にしたい。
:guilabel:`Single-click activation`
   On にすると、検索結果欄の項目をクリックするだけで対象を発射するように動作する。
:guilabel:`Show system tray icon`
   Off にしたい。タスクトレイから |palette| アイコンを消してキーバインドを使って
   UI を開きたい。
:guilabel:`Disable animations`
   On にする。このアニメーションが何を指すのかわからない。

For Developers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Enable external reload`
   On にすると、外部プロセスがコマンド ``x-cmdpal://reload`` を使用して
   |palette| の再読み込みを要求できるようになる。

Extensions
----------------------------------------------------------------------

この一覧のうち、スイッチが On になっている項目が発射ウィンドウの初期検索結果欄に
配列される。

拡張項目のスイッチでない部分をクリックすると、その項目固有の設定画面が開く。

.. todo::

   使える項目に関しては、最適構成を模索してここに記す。

   * Search the Web は Off にしたい
   * Search WinGet は Off にしたい

.. _Command Palette: https://learn.microsoft.com/en-us/windows/powertoys/command-palette/

.. 以上
