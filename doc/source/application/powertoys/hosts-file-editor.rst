======================================================================
Hosts File Editor 利用ノート
======================================================================

.. |editor| replace:: Hosts File Editor
.. |hosts| replace:: :file:`%SystemRoot%\\System32\\drivers\\etc\\hosts`
.. |toys| replace:: :program:`PowerToys`

|editor| はファイル |hosts| の設定を編集するためのユーティリティーだ。観念的には
UNIX 系 OS において :file:`/etc/hosts` としてよく知られているファイルと同じもの
だ。

ファイルパスがわかっていて、管理者権限をどうにでもできる使用者ならば、普通のテキ
ストエディターで編集しても全然構わないものだ。

.. attention::

   :doc:`./index` 冒頭の前提条件に留意すること。

.. contents:: 見出し一覧
   :local:

Hosts File Editor ウィンドウ
======================================================================

|editor| ウィンドウはファイル |hosts| の内容を一覧形式で表現する UI だ。この UI
は登録済みのホスト項目の On/Off を切り替えたり、項目を削除したりするのに用いるた
めのものだ。

以下、このウィンドウのコントロールを記す。

New entry ボタン
----------------------------------------------------------------------

|toys| 本体の設定で |editor| が有効になっていることをまず確認する必要がある。

新しいエントリーを追加するにはボタン :guilabel:`New entry` を押して
:guilabel:`Add new entry` フォームを表示する。それから次の項目を埋める：

.. csv-table::
   :delim: @
   :header-rows: 1
   :widths: auto

   入力欄 @ 入力値
   :guilabel:`Address` @ IP アドレス
   :guilabel:`Host`    @ ホスト名
   :guilabel:`Comment` @ 記入目的を確認するためのコメント

最後にスイッチ :guilabel:`Active` が有効になっていることを確認し、ボタン
:guilabel:`Add` を押す。

Filters ボタン
----------------------------------------------------------------------

ホストファイルのエントリーを絞るには、漏斗アイコンをクリックし、

* :guilabel:`Address`
* :guilabel:`Host`
* :guilabel:`Comment`

のいずれかに文字列を入力する。

Open hosts file ボタン
----------------------------------------------------------------------

:guilabel:`Open hosts file` ボタンを押すと、ファイル |hosts| がテキストエディ
ターで開く。

.. admonition:: 利用者ノート

   このテキストエディターはメモ帳固定？

Settings ボタン
----------------------------------------------------------------------

:guilabel:`Settings` ボタンを押すと、|toys| 設定画面の |editor| ページに移動す
る。

バックアップ
======================================================================

|editor| は編集前にファイル |hosts| をバックアップする。バックアップファイルはこ
のフォルダーに :file:`hosts_PowerToysBackup_YYYYMMDDHHMSS` のような名前で置かれ
る。

設定
======================================================================

:guilabel:`Enable Hosts File Editor` を On にすれば |editor| を開くことが可能に
なる。

Activation
----------------------------------------------------------------------

:guilabel:`Open Hosts File Editor`
   この設定画面でこの項目を選択することで |editor| を開いてもかまわない。
:guilabel:`Open as administrator`
   これが On であることがファイル |hosts| を保存するのに必要だ。
:guilabel:`Show a warning at startup`
   専用エディターを開いた瞬間に、DNS の名前解決変更可能性があることを警告しても
   らうかどうかを決める。案外うっとうしいので Off とする。

Behavior
----------------------------------------------------------------------

:guilabel:`Placement of additional content`
   行を :guilabel:`Top` と :guilabel:`Bottom` のどちらから追加していくかを選ぶ。
:guilabel:`Consider loopback addresses as duplicates`
   Off とする。
:guilabel:`No leading spaces`
   有効ホスト指定行の先頭を空白文字から始めたくないときには On にするという理解
   でいい？
:guilabel:`Encoding`
   なんでもいいはずだが :guilabel:`UTF-8` を指定しておくのが無難だ。

.. 以上
