======================================================================
Microsoft PowerToys 利用ノート
======================================================================

.. |toys| replace:: PowerToys

`Microsoft PowerToys <https://docs.microsoft.com/ja-jp/windows/powertoys/>`__
についての雑多なノートを綴る。

.. note::

   本ノートを記すのに用いている Windows および |toys| のバージョン情報はそれぞれ
   次のとおりだ。

   :OS: Windows 11 Home Pro version 25H2
   :PowerToys: v0.95.1

.. contents:: 見出し一覧
   :local:

事前条件
======================================================================

インストールまたはアップグレードの際には OS がインターネットに接続されており、
かつ :program:`winget` が利用可能であるものとする。

インストールとアップグレード
======================================================================

インストール方法は複数あるが、:program:`winget` での JSON ファイルから他のソフト
ウェアと一斉にインストールする運用を想定している。

|toys| 単体をインストールするならば、コンソールから次のコマンドを実行する：

.. sourcecode:: pwsh-session
   :caption: :program:`winget` による PowerToys インストール例
   :force:

   PS> winget install -e --id Microsoft.PowerToys --scope machine

更新はコマンド ``winget update`` で行う。

全般設定
======================================================================

|toys| の設定画面を開くには、タスクトレイのアイコンをクリックして現れるポップ
アップにある歯車アイコンをクリックする。左柱から :guilabel:`General` をクリック
する。ここで |toys| に関する全般的な構成をする。

.. note::

   UI 言語は英語に設定するものとして記述する。

Version & updates
----------------------------------------------------------------------

起動中の |toys| のバージョン番号を確認することができ、この項目をクリックすると次
の UI が現れる：

:guilabel:`Download and install updates automatically`
   チェックを入れる。
:guilabel:`Show notifications for new updates`
   チェックを外しておく。
:guilabel:`Show the release notes after an update`
   チェックを入れる。

この画面を開いた時点で更新プログラムがある場合、:samp:`An update is ready to
install: v{X}.{Y}.{Z}` のような文言が示される。:guilabel:`Install now` ボタンを
押してパッケージを更新しろ。

Administrator mode
----------------------------------------------------------------------

管理者モードの確認および設定、管理者モードに関する詳細情報の確認をすることが可能
だ。

:guilabel:`Running as administrator`
   右側のドロップダウンリストが :guilabel:`Restart PowerToys as administrator`
   を示したまま無効化されているはずだ。
:guilabel:`Always run as administrator`
   チェックを入れたままにしておくのが無難のはずだ。
:guilabel:`Show a warning for functionality issues when running alongside elevated applications`
   これもチェックを入れておく。

一般モードから管理者モードに切り替えるときには |toys| が再起動する。その逆は不能
になっており、管理者モードで |toys| を開くと、この設定項目が変更不能になる。

Appearance & behavior
----------------------------------------------------------------------

:guilabel:`Language`
   :guilabel:`English` を設定する。既定では OS 言語に合致する値だ。
:guilabel:`Theme`
   OS に合わせるのが無難だ。次のいずれかに指定する：

   * :guilabel:`Dark`
   * :guilabel:`Light`
   * :guilabel:`Windows default`
:guilabel:`Run at startup`
   Off にしておく。好きなタイミングで手動で起動したい。
:guilabel:`Show system tray icon`
   On にしておくが、慣れたら Off でも行けるだろう。

Back up & restore
----------------------------------------------------------------------

:guilabel:`Back up and restore your settings`
   この項目自体をクリックすると、バックアップに関する詳細が示される。

   :guilabel:`Location` によると、次のフォルダー以下に JSON ファイル群が大量に保
   存されることを確認できる。これらが |toys| およびサブソフト群の設定内容を保持
   しているのだろう：

   .. sourcecode:: text
      :caption: |toys| 設定ファイル群格納フォルダーパス

      %LOCALAPPDATA%\Microsoft\PowerToys

Experimentation
----------------------------------------------------------------------

:guilabel:`Allow experimentation with new features`
   On にしておく。

Diagnostics & feedback
----------------------------------------------------------------------

:guilabel:`Diagnostic data`
   Off にする。
:guilabel:`Save logs to this device`
   診断を無効にするのでログファイルは保存する必要がない。
:guilabel:`Generate bug report package`
   ログファイルを保存しないので、圧縮ファイルを作ることもない。

ユーティリティー概要
======================================================================

|toys| は各種アプリケーションの複合体と考えるほうがわかりやすい。アプリケーショ
ン同士の連携は全くないものと捉えるべきだ。

以下では |toys| をそれぞれのアプリケーション単位について簡単に述べていく。きちん
とした仕様は先述の文書のリンク先各ページに述べられている。

.. toctree::
   :glob:
   :maxdepth: 1
   :titlesonly:

   *

.. 以上
