======================================================================
PowerRename 利用ノート
======================================================================

PowerRename は Linux におけるコマンド :command:`rename` の GUI 版と解釈できる。

.. attention::

   :doc:`./index` 冒頭の前提条件に留意すること。

.. contents:: 見出し一覧
   :local:

概要
======================================================================

PowerRename はファイルを多数一括処理することを念頭に置くツールだ。ここで言う一括
処理とは、次を意図する：

* どのファイルにも名前を重複することなく、多数のファイルを改名する。
* ファイル名の対象部分に対して検索と置換を実行する。
* 複数のファイルに対して正規表現を用いた改名をする。
* 一括改名を確定する前にプレビューウィンドウで結果を確認する。
* 改名操作が完了した後に元に戻すことができる。

PowerRename 画面
======================================================================

メイン画面は Windows Explorer から間接的に表示させるものだ：

1. Windows Explorer でファイルを普通は複数選択する。
2. コンテキストメニューを表示する。設定次第では :kbd:`Shift` キーを押したまま表
   示する。
3. 項目 :menuselection:`Rename with PowerRename` を選択する。

これで :guilabel:`PowerRename` 画面が表示される。選択した項目の数が表示され、検
索値や置換値、オプションのリスト、入力した検索値や置換値の結果を表示するプレ
ビューウィンドウが表示される。

左側のテキストボックス二つを操作する。Linux の :command:`rename` の要領で、置換
前後のファイル名パターンを指定する。

一つ目のテキストボックスに文字列または正規表現を入力すると、PowerRename は条件に
合致するファイルを選択範囲から絞り込む。合致した項目は右側のプレビューウィンドウ
に表示される。二つ目のテキストボックスには、先ほどの指定部分を置き換えるテキスト
を入力する。プレビューウィンドウで元の変更前後のファイル名を確認できる。

Use regular expressions
----------------------------------------------------------------------

:guilabel:`Use regular expressions` をチェックした場合、一つ目の入力欄の値は正規
表現として解釈される。この場合、置換値には正規表現変数を含めることもできる。

チェックされていない場合、文字列はプレーンテキストとして解釈され、これが二つ目の
入力欄のテキストに置換される。

Match all occurrences
----------------------------------------------------------------------

:guilabel:`Match all occurrences` をチェックすると、同一ファイル名内（同一行内の
可能性あり）に指定パターンが複数箇所出現する場合、そのすべてに対して置換が適用さ
れる。

正規表現を使用する場合はこれにチェックを入れたい。

.. admonition:: 利用者ノート

   次の二つの違いと同じ：

   * :command:`sed s/pattern/replacement/g`
   * :command:`sed s/pattern/replacement/`

Case sensitive
----------------------------------------------------------------------

:guilabel:`Case sensitive` をチェックすると、一つ目の入力欄で指定したものは、大
文字と小文字が同じ場合にのみ、項目内のテキストと一致する。既定値はオフだ。

Replace terms
----------------------------------------------------------------------

:guilabel:`Replace with` テキストボックスの右にあるヒントボタンを押すことで、置
換後のパターン用文字列一覧が現れる。ここから項目を選択すると、当該パターン文字列
がテキストボックスに挿し込まれる。

ファイルに関わるタイムスタンプとして、``$YYYY`` などのパターンを第ニ入力欄で利用
可能だ。右にあるアイコンをクリックするとサポートされているパターンを表示し、そこ
から選択することも可能だ。オプションは :ref:`anchor-rename-time` で選べ。

.. admonition:: 利用者ノート

   この一覧にある Replace using advanced counter syntax や Replace using random
   values はもしかしたら有用であるかもしれない。

Apply to
----------------------------------------------------------------------

:guilabel:`Apply to` は合致したファイルのどの部分に対して置換を適用するのかを細
かく指定するオプションと、ファイル、フォルダー単位の除外指定がある。

コンボボックス：

.. csv-table::
   :delim: @
   :header-rows: 1
   :widths: auto

   値 @ 主旨
   :guilabel:`Filename + extension` @ ファイル名全体に置換を適用する
   :guilabel:`Filename only` @ ファイル名の :command:`basename` に置換を適用する
   :guilabel:`Extension only` @ 拡張子にしか置換を適用しない

紙アイコンのトグルボタン三つ：

:guilabel:`Include files`
   Off にするとファイルが対象外となる
:guilabel:`Include folders`
   Off にするとフォルダーが対象外となる
:guilabel:`Include subfolders`
   Off にするとフォルダー内のファイルは対象外となる

Text formatting
----------------------------------------------------------------------

最初の四つのコントロールはラジオボタンだ。次のうちから高々一つをオンにして構わな
い：

* :guilabel:`lowercase`
* :guilabel:`UPPSERCASE`
* :guilabel:`Title case`
* :guilabel:`Capitalize Each Word`

:guilabel:`Enumeration features`
   On にすると、操作で変更されたファイル名に数字の接尾辞を付加する。例えば
   :file:`foo.jpg` は :file:`foo (1).jpg` といった具合だ。
:guilabel:`Random string features`
   使ったことがない。

.. _anchor-rename-time:

Time used for replacement
----------------------------------------------------------------------

変更後のファイル名にタイムスタンプ情報を含める場合、どの時刻を採用するかを次から
決める：

* :guilabel:`Creation Time`
* :guilabel:`Modification Time`
* :guilabel:`Access Time`

おそらく二番目を用いるのが一般的だと思われる。UNIX ならコマンド ``date -r`` で得
られる情報に相当するだろうから。

Filter
----------------------------------------------------------------------

右上の漏斗アイコンのメニューは項目がラジオボタン的動作をする。いずれか一方を選択
する。

:guilabel:`Show all files`
   ファイルすべてを一覧に出現させる。
:guilabel:`Only show files that will be renamed`
   名前が変更されるファイルしか一覧に出現させない。

設定
======================================================================

:guilabel:`Enable PowerRename` を On にすることで Explorer のコンテキストメニュー
が本機能に対応する。

Shell integration
----------------------------------------------------------------------

ドロップダウンリスト :guilabel:`Show PowerRename in` で、Explorer のコンテキスト
メニューにいつ出現させるかを指定できる。

.. csv-table::
   :delim: @
   :header-rows: 1
   :widths: auto

   値 @ 主旨
   :guilabel:`Default and extended context menu` @ メニュー表示時に常時出現する
   :guilabel:`Extended context menu only` @ :kbd:`Shift` キーを押しながらメニューを表示しないと出現しない

Auto-complete
----------------------------------------------------------------------

:guilabel:`Enable auto-complete for the search & replace fields`
   PowerRename の過去の使用実績に基づいて、検索欄および置換欄で使用する文字列を
   自動的に補完するかどうか。Off でいいと思う。

   :guilabel:`Maximum number of items`
       表示する検索・置換候補の最大数。
:guilabel:`Show recently used strings`
   On にすれば、PowerRename 開始時に直近の入力値が検索欄と置換欄に記入済みとな
   る。これも Off でいいと思う。

Behavior
----------------------------------------------------------------------

PowerRename の既定の正規表現エンジンは ECMAScript の文法に対応している。
:guilabel:`Use Boost library` を On にすると、正規表現エンジンが Boost になる。
これにより、標準ライブラリーでは対応されていない lookaround のような正規表現構文
が有効になる。

.. 以上
