======================================================================
Advanced Paste 利用ノート
======================================================================

.. |ap| replace:: `Advanced Paste`_
.. |apwin| replace:: :guilabel:`Advanced Paste`
.. |kb-ap| replace:: :kbd:`Win` + :kbd:`Shift` + :kbd:`V`
.. |kb-plain| replace:: :kbd:`Win` + :kbd:`Ctrl` + :kbd:`Alt` + :kbd:`V`

本稿は PowerToys |ap| 機能のうち、AI を使わないものに絞って記述する。

.. attention::

   :doc:`./index` 冒頭の前提条件に留意すること。

.. contents:: 見出し一覧
   :local:

概要
======================================================================

|ap| はクリップボードの内容を別の形式に変換して貼り付ける機能だ。次の機能を含む：

* プレインテキスト、Markdown, JSON, HTML, etc. 変換して貼り付ける
* 画像からテキストを抽出する
* 音声や映像ファイルを MP3 や MP4 に変換する

Advanced Paste ウィンドウ
======================================================================

本節は |apwin| の UI に関する記述だ。

.. |ch| replace:: :guilabel:`Clipboard history`

使用手順は次のとおりだ：

#. 出力を貼り付ける対象をアクティブにする
#. 設定画面のキーバインド (|kb-ap|) を押して |apwin| ウィンドウを開く
#. 必要に応じて |ch| から所望のクリップボードデータを選択する
#. |apwin| ウィンドウの変換候補一覧から所望のコマンドを選択する

.. admonition:: 利用者ノート

   貼り付け対象は変換コマンドによって、エディットボックスだったり、Windows
   Explorer だったり、画像編集アプリケーションのキャンバスだったりする。

|apwin| ウィンドウの構成要素について記述する。

検索欄
   コマンド名を曖昧検索するためのテキストボックスだ。何か文字列を入力するとコマ
   ンド一覧の絞り込みが発生する。
:guilabel:`Paste as plain text`
   ワープロやブラウザーなどの書式を伴うテキストがクリップボードの内容である場
   合、その書式すべてを取り除いたテキストを貼り付ける。
:guilabel:`Paste as markdown`
   クリップボードの内容を Markdown 形式に変換可能である場合、その変換を施したテ
   キストを貼り付ける。

   例えば、ブラウザーでハイパーテキストからなる一覧をクリップボードにコピーした
   直後、編集中の Markdown テキストに貼り付けるという使い方をする。
:guilabel:`Paste as JSON`
   クリップボードの内容を JSON 形式に変換可能である場合、その変換を施したテキス
   トを貼り付ける。
:guilabel:`Paste as .txt file`
   クリップボードの内容がテキストに変換可能である場合、そのテキストを自動生成さ
   れたファイル名で ``.txt`` ファイルに変換して貼り付ける。

   このコマンドを含む、一連のファイルとして貼り付ける系コマンドは、対象ウィンド
   ウが、例えば Windows Explorer のように、ファイルの貼り付けに対応したものであ
   ることを前提とする。生成ファイル名は勝手に決まる。
:guilabel:`Paste as .png file`
   クリップボードの内容がビットマップなどの画像形式である場合、その画像を
   ``.png`` ファイルに変換して貼り付ける。
:guilabel:`Paste as .html file`
   クリップボードの内容が HTML 由来である場合、HTML テキストを内容とするファイル
   に変換して貼り付ける。自己完結した HTML ファイルを生成するとは限らない。
:guilabel:`Transcode to .mp3`
   クリップボードから音声チャンネルを抽出し、MP3 ファイルに変換して保存する。

   YouTube からダウンロードした MP4 ファイルから音声だけ欲しい場合に有用。
:guilabel:`Transcode to .mp4 (H.264/AAC)`
   ビデオファイルを映像は H.264 形式で、音声がある場合には AAC 形式でそれぞれ符
   号化し、MP4 ファイルを生成して保存する。

   MP4 以外のビデオファイルを MP4 形式に変換したい場合にのみ有用。
|ch|
   Windows のクリップボード履歴と同じ内容。

   * 項目を選択すると、クリップボードの内容がその選択データに置き換わる。
   * 三点ボタンをクリックすると、:menuselection:`Delete` 操作を含むメニューが現
     れる。

設定
======================================================================

:guilabel:`Enable Advanced Paste` を On や Off にすることで |ap| 機能の活動を開
始したり停止したりする。

Paste with Al
----------------------------------------------------------------------

.. |enable-ai| replace:: :guilabel:`Enable Paste with Al`

|enable-ai|
   On にすると、AI の能力を借りてクリップボードの内容を変換することができる。こ
   のスイッチを On にするには OpenAI API 鍵が必要だ。
:guilabel:`Enable advanced Al`
   On にすると、複数の変換を連鎖したり、画像やファイルを操作する機能を含める。

Behavior
----------------------------------------------------------------------

|ch|
   On にすると Windows に実装されているクリップボード履歴機能が効くようになる。
   それが |apwin| ウィンドウの |ch| が使用可能になる条件だと考えられる。
:guilabel:`Automatically close the AdvancedPaste window after it loses focus`
   On にすると |apwin| ウィンドウからフォーカスが別に移ったときに勝手に閉じるよ
   うになる。
:guilabel:`Custom format preview`
   On にすると、AI によるカスタム形式の出力を貼り付ける前にプレビューできる。

   このスイッチはなぜか |enable-ai| が Off でも変更できる。いちおう On にしてお
   く。

Actions
----------------------------------------------------------------------

:guilabel:`Actions`
   AI を使う貼り付けの動作を構成する。

   :guilabel:`Add custom action`
      構成するには |enable-ai| が On である必要がある。

      詳細不明。
:guilabel:`Open Advanced Paste window`
   |apwin| ウィンドウを開くキーバインドを指定する。既定 |kb-ap| でいい。
:guilabel:`Paste as plain text directly`
   |apwin| ウィンドウを開かずとも、クリップボードをプレインテキストとして貼り付
   けるキーバインドを指定する。既定 |kb-plain| はキーを押しにくい。
:guilabel:`Paste as Markdown directly`
   同様に、ウィンドウを開かずにクリップボードを Markdown 形式で貼り付けするキー
   バインドを指定する。既定ではキーバインドが割り当てられていない。
:guilabel:`Paste as JSON directly`
   同様に、ウィンドウを開かずにクリップボードを JSON 形式で貼り付けするキーバイ
   ンドを指定する。

Additional actions
----------------------------------------------------------------------

:guilabel:`Image to text`
   画像からテキストを抽出する機能の有無を切り替える。
:guilabel:`Paste as file`
   クリップボード内容を変換してファイルとして貼り付ける機能の有無を切り替える。
   これを On にしないと、次の機能を何も活動させられない：

   * :guilabel:`Paste as .txt file`
   * :guilabel:`Paste as .png file`
   * :guilabel:`Paste as .html file`
:guilabel:`Transcode audio / video`
   これを On にしないと、次の機能を何も活動させられない：

   * :guilabel:`Transcode to .mp3`
   * :guilabel:`Transcode to .mp4 (H.264/AAC)`

.. _Advanced Paste: https://learn.microsoft.com/en-us/windows/powertoys/advanced-paste

.. 以上
