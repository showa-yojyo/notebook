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

:guilabel:`Version & updates` とある場所からは次のことができる：

* 起動中の |toys| のバージョン番号、
* 更新プログラムの有無確認、
* リリースノートの確認、および
* :guilabel:`Show notifications for new updates` するかどうかの切り替えをする。

:guilabel:`Administrator mode` とある場所からは次のことができる：

* 管理者モードの確認および設定
* 管理者モードに関する詳細情報の確認

一般モードから管理者モードに切り替えるときには |toys| が再起動する。その逆は不能
になっており、管理者モードで |toys| を開くと、この設定項目が変更不能になる。

:guilabel:`Appearance & behavior` とある場所からは、次のことができる：

* UI 言語指定。当ノートでは :guilabel:`English` を設定。
* :guilabel:`Theme` を次のいずれかに指定する：

  * :guilabel:`Dark`
  * :guilabel:`Light`
  * :guilabel:`Windows default`
* :guilabel:`Run at startup` スイッチで、OS 起動時に |toys| を起動するかどうかを
  決める。

バックアップ
======================================================================

次のフォルダー以下に JSON ファイル群が大量に保存されている。これらが |toys| およ
びサブソフト群の設定内容を保持しているのだろう。

.. sourcecode:: text
   :caption: |toys| 設定ファイル群格納フォルダーパス

   %LOCALAPPDATA%\Microsoft\PowerToys

全般設定画面の :guilabel:`Back up & restore` 区画にバックアップ用のボタンがある
のでそれを利用するといい。

精選機能集
======================================================================

私が重用したい機能を順不同に記す。使用の度合いはおそらくばらつきがあるだろう。

* File Explorer add-ons は採用決定。テキストエディターを開かなくても JSON ファイ
  ルが確認できたりするのは大きい。
* Image Resizer は使ってみると手軽なので採用する。プリセットは不要。小だけ使う。
  タイムスタンプを保持する設定を推奨。
* Keyboard Manager は条件付きで採用。レジストリーを別の手段で変更していないとき
  に使う。次に Windows PC を新調したときから利用するか。
* PowerRename はいちおう採用。
* Shortcut Guide はこれらのショートカットキーを習得するまで有効にする。

不採用の機能は設定画面のスイッチで無効にしておく。

ユーティリティー概要
======================================================================

|toys| は各種アプリケーションの複合体と考えるほうがわかりやすい。アプリケーショ
ン同士の連携は全くないものと捉えるべきだ。

以下では |toys| をそれぞれのアプリケーション単位について簡単に述べていく。きちん
とした仕様は先述の文書のリンク先各ページに述べられている。

.. toctree::
   :maxdepth: 1

   always-on-top
   awake
   color-picker
   fancy-zones
   file-explorer-add-ons
   file-locksmith
   hosts-file-editor
   image-resizer
   keyboard-manager
   mouse-utilities
   power-rename
   powertoys-run
   quick-accent
   screen-ruler
   shortcut-guide
   text-extractor

.. 以上
