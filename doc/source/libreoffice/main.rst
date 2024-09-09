======================================================================
LibreOffice 共通ノート（簡易版）
======================================================================

.. note::

   :Platform: Windows 10
   :Version: 7.6.4.1 x86_64

.. contents:: 本章見出し
   :local:

LibreOffice 関連資料
======================================================================

LibreOffice_
   本拠地ホームページ。プログラム本体だけでなく利用者手引も入手するべし。
`libreofficehelp.com <https://www.libreofficehelp.com/>`__
   ブログ構造のチュートリアル。公式ガイドを読む前に習得していくのもアリだ。

インストール方法
======================================================================

公式サイトからインストーラーをダウンロードして実行するのもよいが、本ノートでは
パッケージ管理ツール :program:`winget` の使用を推奨する。

.. code:: pwsh

   winget install -e --id TheDocumentFoundation.LibreOffice

.. seealso::

   :doc:`/winget`

個人的必修技法
======================================================================

* LibreOffice のバージョン (:menuselection:`&Help --> &About LibreOffice`)
* オプションダイアログは :kbd:`Alt` + :kbd:`F12` で開く
* キーバインド確認方法 (:menuselection:`&Tools --> &Customize...`)
* UI をチュートリアル推奨様式に変更

以下、各アプリケーション個別設定になる。

* パスワード付与保存 (:menuselection:`&File --> Save &As...`)
* 既定雛形変更 (:menuselection:`&File --> Te&mplates --> &Manage Templates...`)

個人的設定オプション
======================================================================

ほとんどの項目で既定値が良い。自分好みの値に変更するものと、既定値のままであって
も意識するべき構成を以下に記す。

* LibreOffice

  * General

    * Help

      * :guilabel:`&Extended tips` をオン
      * :guilabel:`Warn if local help is not installed` はオフ
      * :guilabel:`Show "Tip of the Day" dialog on start-up` をオン
    * Open/Save Dialogs

      * :guilabel:`&Use LibreOffice dialogs` をオフ

    * Help Improve LibreOffice

      * :guilabel:`Sen&d crash reports to The Document Foundation` をオン
  * Security

    * Security Options and Warnings の :guilabel:`O&ptions...` ボタン

      * :guilabel:`&Remove personal information on saving` をオン
  * Online Update

    * Online Update Options

      * :guilabel:`&Check for updates automatically` は :guilabel:`Every da&y`
    * User Agent

      * :guilabel:`&Send OS version and basic hardware information` をオン
* Load/Save

  * Save

    * :guilabel:`Save &AutoRecovery information every` をオンにして何分でもいい
      から指定
    * :guilabel:`Al&ways create backup copy` をオフ
* Language Settings

  * Languages

    * Language Of

      * :guilabel:`&User interface` を :guilabel:`English (USA)` に

    * Formats

      * :guilabel:`Date acceptance &patterns` から自分が使わないものを除外する
  * Asian Layout については既定値よりも良い設定がある可能性がある

設定バックアップ方法
----------------------------------------------------------------------

:guilabel:`Options` ダイアログで :menuselection:`LibreOffice --> Path` をクリッ
クすると :guilabel:`Paths used by LibreOffice` 一覧が示される。このうち、パスが

   :file:`%APPDATA%\\LibreOffice\\4\\user`

のフォルダー以下が LibreOffice カスタマイズ設定置場と考えられる。したがって、こ
こはバックアップをするべきだろう。Git によるバージョン管理をするなり、オンライン
ストレージへの同期を定期的に実施するなり、対応しろ。

個人的必修キーバインド共通編
======================================================================

Writer, Calc など、LibreOffice プログラム共通に通用するキーバインドのうち、常用
するものを以下に記す。Windows 標準のキーバインドは省略。便利なものを積極的に採り
入れろ。

キーバインドは :menuselection:`&Tools --> &Customize...` ダイアログの
:guilabel:`Keyboard` で確認可能。ただしこの UI は使いにくい。

.. csv-table::
   :delim: |
   :header-rows: 1
   :widths: auto

   キーバインド | コマンド | 動作
   :kbd:`Shift` + :kbd:`Esc` | Search Commands | コマンドパレットを開く
   :kbd:`Ctrl` + :kbd:`H` | Find and Replace | :guilabel:`Find and Replace` ダイアログを開く
   :kbd:`Ctrl` + :kbd:`K` | Hyperlink | ハイパーリンクを定義する
   :kbd:`Ctrl` + :kbd:`Q` | Exit | うっかり押して終了しないように覚えておくこと
   :kbd:`Ctrl` + :kbd:`W` | Close Window | これも
   :kbd:`Ctrl` + :kbd:`Y` | Redo | Redo コマンドはキーバインドが二種類ある
   :kbd:`Ctrl` + :kbd:`Z` | Undo | Undo コマンドはこれのみ
   :kbd:`Ctrl` + :kbd:`F5` | Control Focus | ウィンドウ右柱に注目
   :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`N` | Templates | :guilabel:`Templates` ダイアログを開く
   :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`S` | Save As | :guilabel:`Save As` ダイアログを開く
   :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`Y` | Repeat | 直前の入力を反復する？
   :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`Z` | Redo | Redo コマンドはキーバインドが二種類ある
   :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`PageUp` | Zoom In | ウィンドウ主領域をズーム
   :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`PageDown` | Zoom Out | ウィンドウ主領域をズーム
   :kbd:`Alt` + :kbd:`1` | Open the Properties Deck | 画面右端のドックを開く
   :kbd:`Alt` + :kbd:`2` | Open the Styles Deck | 画面右端のドックを開く
   :kbd:`Alt` + :kbd:`4` | Open the Navigator Deck | 画面右端のドックを開く
   :kbd:`Alt` + :kbd:`F12` | Options | 設定ダイアログを表示
   :kbd:`Ctrl` + :kbd:`Alt` + :kbd:`C` | Comment | 付箋作成

.. _LibreOffice: https://www.libreoffice.org/
