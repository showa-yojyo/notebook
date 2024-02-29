======================================================================
LibreOffice Writer 利用ノート
======================================================================

.. note::

   :Platform: Windows 10
   :Version: 7.6.4.1 x86_64

.. contents::

個人的必修機能 Writer 編
======================================================================

* PDF 保存 (:menuselection:`&File --> &Export As --> &Export as PDF...`)
* 改頁挿入（原稿用紙上所望の位置で :kbd:`Ctrl` + :kbd:`Enter` を押す）
* ダミーテキスト挿入（原稿用紙上で ``df`` とタイプして :kbd:`F3` を押す）
* 自動保存オンオフ（オプションダイアログから）
* ヘッダーおよびフッター挿入 (:menuselection:`&Insert -> He&ader and Footer`)
* ヘッダーおよびフッター編集（当該箇所に専用メニューが現れる）
* ページ番号挿入 (:menuselection:`&Insert --> &Page Number`)
* TOC 作成 (:menuselection:`&Insert --> Table of contents and Inde&x --> Table
  of contents, &Index or Bibliography...`)

  * 章・節見出しを定義（書式設定による）

* 原稿用紙の縦長横長設定 (Orientation)
* 段落記号表示オンオフ (:kbd:`Ctrl` + :kbd:`F10` )
* ズーム（己の「ホーム倍率」設定のキーバインドを記憶しろ）
* 番号あり・なしリスト操作 (:kbd:`Shift` + :kbd:`F12`; :kbd:`F12`)
* ハイパーリンク (:kbd:`Ctrl` + :kbd:`K`)
* 画像挿入 (:menuselection:`&Insert --> &Image...` )
* 画像圧縮（画像上でコンテキストメニューを見ろ）
* 画像とテキストの配置制御（チュートリアルを繰り返し実習しろ）
* MRU ファイル一覧削除
* 行間設定 (:menuselection:`Format& --> &Spacing...`)

個人的必修キーバインド Writer 編
======================================================================

.. csv-table::
   :delim: |
   :header: キーバインド,コマンド,動作
   :widths: auto

   :kbd:`F2` | Edit Formula | 数式編集欄を開く
   :kbd:`F3` | Run AutoText Entry | ノートで述べた
   :kbd:`F4` | Image Properties | :guilabel:`Image` ダイアログを開く
   :kbd:`F5` | Navigator | :guilabel:`Navigator` ダイアログを開く
   :kbd:`F8` | Select Cycle | 選択部分を徐々に拡張する
   :kbd:`F9` | Fields | フィールドを更新する
   :kbd:`F12` | Ordered List | ノートで述べた
   :kbd:`Shift` + :kbd:`F3` | Cycle Case | 英文編集でよくやる変換
   :kbd:`Shift` + :kbd:`F8` | MultiSelection On | 複数のテキスト選択を続ける
   :kbd:`Shift` + :kbd:`F11` | New | :guilabel:`New Style from Selection` ダイアログを開く
   :kbd:`Shift` + :kbd:`F12` | Unordered List | ノートで述べた
   :kbd:`Shift` + :kbd:`Enter` | Insert Manual Row Break | 改行挿入
   :kbd:`Ctrl` + :kbd:`0` | Body Text | 本文スタイル
   :kbd:`Ctrl` + :kbd:`1` | Heading 1 | 見出しスタイル
   :kbd:`Ctrl` + :kbd:`2` | Heading 2 | 見出しスタイル
   :kbd:`Ctrl` + :kbd:`3` | Heading 3 | 見出しスタイル
   :kbd:`Ctrl` + :kbd:`4` | Heading 4 | 見出しスタイル
   :kbd:`Ctrl` + :kbd:`5` | Heading 5 | 見出しスタイル
   :kbd:`Ctrl` + :kbd:`B` | Bold | 太字
   :kbd:`Ctrl` + :kbd:`D` | Double Underline | 二重下線
   :kbd:`Ctrl` + :kbd:`E` | Center | 中央揃え
   :kbd:`Ctrl` + :kbd:`G` | Go to Page | :guilabel:`Go to Page` ダイアログを開く
   :kbd:`Ctrl` + :kbd:`I` | Italic | 斜体
   :kbd:`Ctrl` + :kbd:`J` | Justified | 両端（均等）揃え
   :kbd:`Ctrl` + :kbd:`L` | Left | 左揃え
   :kbd:`Ctrl` + :kbd:`R` | Right | 右揃え
   :kbd:`Ctrl` + :kbd:`U` | Underline | 下線
   :kbd:`Ctrl` + :kbd:`[` | Decrease | 文字サイズ調整
   :kbd:`Ctrl` + :kbd:`]` | Increase | 文字サイズ調整
   :kbd:`Ctrl` + :kbd:`F2` | More Fields | :guilabel:`Fields` ダイアログを開く
   :kbd:`Ctrl` + :kbd:`F3` | AutoText | ノートで述べた
   :kbd:`Ctrl` + :kbd:`F8` | Field Shadings | フィールド部分の網掛けオンオフ切り替え
   :kbd:`Ctrl` + :kbd:`F9` | Field Names | DeepL とかぶるキーバインド
   :kbd:`Ctrl` + :kbd:`F10` | Formatting Marks | ノートで述べた
   :kbd:`Ctrl` + :kbd:`F12` | Table | Insert Table ダイアログを開く
   :kbd:`Ctrl` + :kbd:`↓` | To Next Paragraph | 次のパラグラフの先頭へジャンプ
   :kbd:`Ctrl` + :kbd:`↑` | To Paragraph Begin | 前のパラグラフの先頭へジャンプ
   :kbd:`Ctrl` + :kbd:`PageUp` | To Header | ヘッダーへジャンプ
   :kbd:`Ctrl` + :kbd:`PageDown` | To Footer | フッターへジャンプ
   :kbd:`Ctrl` + :kbd:`Enter` | Page Break | 改頁を挿入する
   :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`J` | Full Screen | 全画面表示切り替え
   :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`R` | Rulers | 定規表示切り替え
   :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`V` | Paste Special | :guilabel:`Paste Special` ダイアログを開く
   :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`F5` | Go to Page | もう一つのキーバインド
   :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`F8` | Block Area | 矩形選択モード切り替え
   :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`F12` | No List | リストを解除する
   :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`BackSpace` | Delete to Start of Sentence | キャレットから当該文末まで削除する
   :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`Delete` | Delete to End of Sentence | キャレットから当該文頭まで削除する
   :kbd:`Alt` + :kbd:`5` | Open the Page Deck | ウィンドウ右ドックを開く
   :kbd:`Alt` + :kbd:`6` | Open the Style Inspector Deck | ウィンドウ右ドックを開く
   :kbd:`Alt` + :kbd:`PageUp` | To Begin of Previous Page | 前のページの先頭文字へジャンプ
   :kbd:`Alt` + :kbd:`PageDown` | To Begin of Next Page | 次のページの先頭文字へジャンプ
   :kbd:`Alt` + :kbd:`Shift` + :kbd:`F8` | Block Area | もう一つのキーバインド
   :kbd:`Alt` + :kbd:`Shift` + :kbd:`PageUp` | Select to Begin of Previous Page | これは使い物にならない
   :kbd:`Alt` + :kbd:`Shift` + :kbd:`PageDown` | Select to Begin of Next Page | キャレットから次ページの先頭文字まで選択する
   :kbd:`Ctrl` + :kbd:`Alt` + :kbd:`↓` | Move Item Down | 対象項目を下へずらす
   :kbd:`Ctrl` + :kbd:`Alt` + :kbd:`↑` | Move Item Up | 対象項目を上へずらす
   :kbd:`Ctrl` + :kbd:`Alt` + :kbd:`Shift` + :kbd:`V` | Paste Unformatted Text | 書式抜きでテキストを貼り付ける

.. _LibreOffice: https://www.libreoffice.org/
