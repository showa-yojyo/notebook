======================================================================
Image Resizer
======================================================================

Image Resizer は Windows エクスプローラーのコンテキストメニューを拡張し、画像
ファイルに対して作用する。画像の寸法を前もって設定しておいたものに拡縮する機能
だ。汎用画像編集アプリケーションを起動するのが億劫な場合に活用できる。

まずは :guilabel:`Image Resizer を有効化する` を ON にする。

.. attention::

   :doc:`./index` 冒頭の前提条件に留意すること。

.. contents::

コンテキストメニュー
======================================================================

エクスプローラーで Image Resizer が対応している画像ファイルを選択してコンテキス
トメニューを表示させると、次の項目がメニューにある：

* :guilabel:`画面のサイズ変更`
* :guilabel:`右に回転`
* :guilabel:`左に回転`

サイズ変更コマンドだけが追加入力を要求する。

設定
======================================================================

イメージサイズ
----------------------------------------------------------------------

既定のプリセットについては名称から自然に理解されるとおりの内容だ。

:guilabel:`新しいボタン` を押すとプリセットを追加できる。次の属性を指定すること
が可能だ：

.. csv-table::
   :delim: @
   :header-rows: 1
   :widths: auto

   属性 @ 主旨
   :guilabel:`名前` @ UI に表示されるラベル
   :guilabel:`サイズに合わせて調整` @ リサイズ後の寸法仕様
   :guilabel:`幅` @ リサイズ後の画像の幅
   :guilabel:`高さ` @ リサイズ後の画像の高さ
   :guilabel:`ユニット` @ 上記寸法の単位

:guilabel:`サイズに合わせて調整` の選択肢は三つだ：

:guilabel:`幅に合わせて調整`
    指定された寸法全体を画像で埋める。画像を比例して拡縮する。必要に応じて画像を
    切り落とす。
:guilabel:`サイズに合わせて調整`
    画像全体を指定された寸法に収める。画像を一様に拡縮する。画像を切り落とさない。
:guilabel:`引き伸ばし`
    指定された寸法全体を画像で埋める。必要に応じて、画像を不釣り合いに引き伸ばす。
    画像を切り落とさない。

なお、:guilabel:`幅` や :guilabel:`高さ` を空白のままにすることも可能だ。寸法は
元画像の縦横比に基づいて計算される。

エンコード
----------------------------------------------------------------------

:guilabel:`フォールバックエンコーダー` はリサイズ後のファイルが元のフォーマット
で保存できない場合に適用される。例えば .wmf 画像形式は Image Resizer が読み込む
ことはできるが、この形式で出力することができない。つまり、新画像を元のフォーマッ
トで保存できない。このようなとき、当該設定項目で指定された画像形式で保存される。

あくまでもフォールバックなので、変換処理に応用することはできない。例えば BMP か
ら JPEG に変換するような用途には使えない。

JPEG, PNG, TIFF それぞれで保存する場合には、ちょっとしたオプションが用意されてい
る。詳細は割愛。

ファイル
----------------------------------------------------------------------

:guilabel:`ファイル名の形式` で新ファイルの名前のテンプレを指定する。パーセント
なんとかのプレースホルダー各種の意味は、入力欄横のボタンをクリックすると記述が現
れる。

ファイル名に使用できない文字は ``_`` に置換される。

:guilabel:`ファイルの変更されたタイムスタンプ` で、リサイズされた画像ファイルの
最終更新日を保持するか、操作の際に更新するかを選択する。

.. admonition:: 利用者ノート

   推奨設定を記す：

   * :guilabel:`ファイル名の形式` をより単純にする。たとえば :code:`%1-%2` くら
     いでいい。
   * :guilabel:`ファイルの変更されたタイムスタンプ` を
     :guilabel:`元のファイルのタイムスタンプ` に変更する。
