======================================================================
Quick Accent 利用ノート
======================================================================

Quick Accent はアクセント付きアルファベットを入力するときに、キーボードが対応し
ていない場合に有用なツールだ。

.. attention::

   :doc:`./index` 冒頭の前提条件に留意すること。

.. contents:: 見出し一覧
   :local:

使い方
======================================================================

Quick Accent 設定画面を開き、スイッチ :guilabel:`Enable Quick Accent` を On にし
ておく。

アクセントをつけたい文字のキーを押しながら、稼働キー（後述）を押して稼働状態にす
る。そのまま押し続けると、複数の文字からアクセントをつけたい文字を選択するための
ツールバー（本稿では以下アクセント文字一覧と呼ぶ）のようなものが画面に出現する。
例えば文字 ``a`` にウムラウトをつけたいとする。このとき、まずキー :kbd:`A` を押
し、そのまま離さずに :kbd:`Space` を押すと画面上に次のボタンからなるアクセント文
字一覧が出る：

.. sourcecode:: text

   à â á ä ã å æ ...

:kbd:`Space` か左右の矢印キーを叩いて所望の文字、この場合には左から四番目の文字
を選択して :kbd:`A` キーから指を離すことで入力中の文字が入れ替わる。

設定
======================================================================

Activation
----------------------------------------------------------------------

:guilabel:`Activation key`
   アクセントを付けたいキーを長押ししたときにアクセント文字一覧ツールバーを出現
   させるキー。次のいずれかを選択できる：

   * :kbd:`←` or :kbd:`→`
   * :kbd:`Space`
   * :kbd:`←` or :kbd:`→` or :kbd:`Space`
:guilabel:`Do not activate when Game Mode is on`
   On にしておくのが無難と考えられる。

Characters
----------------------------------------------------------------------

:guilabel:`Choose character sets`
   Quick Accent 入力を有効にする文字集合を選択的に決定することが可能だ。

   :guilabel:`All available`
      チェックを入れると、この機能が支援する文字集合すべてに対して有効になる。

      チェックを外すと、この下にある文字集合一覧から対象を選択することが可能にな
      る。

   * :guilabel:`Language sets`
   * :guilabel:`Special sets`

Toolbar
----------------------------------------------------------------------

:guilabel:`Toolbar position`
   画面上のどこにツールバーを表示するかを :guilabel:`Top center` などの項目一覧
   から選択して指定する。
:guilabel:`Show the Unicode code and name of the currently selected character`
   アクセント付き文字といっしょに、そのコードポイントと文字名を併記する。On でい
   い。
:guilabel:`Sort characters by usage frequency`
   文字が多い場合の使い勝手に影響するので On にする。
:guilabel:`Start selection from the left`
   詳細不明。

Behavior
----------------------------------------------------------------------

:guilabel:`Input delay (ms)`
   稼働キーをどのくらい押し続けるとアクセント文字一覧ツールバーが出現するかを指
   定する。
:guilabel:`Excluded apps`
   :doc:`./always-on-top` や :doc:`./mouse-utilities` の同名設定項目と同様。

.. 以上
