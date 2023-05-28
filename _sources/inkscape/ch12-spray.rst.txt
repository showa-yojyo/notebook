======================================================================
Chapter 12. Spray Tool
======================================================================

.. contents::

「オブジェクトの複写を吹き付けるエアブラシ」という表現は優れていると思う：

   The *Spray Tool* is used to distribute copies of an object (or objects) much
   like an airbrush would paint drops.

マリオペイントのスタンプツールと言われたほうがわかりやすい。

モードは四つある。最初の三つは本書に記述があるが、最後のものは自分で調べる。

:guilabel:`Spray copies of the initial selection`
   互いに独立した個別のオブジェクトとして複製を巻き散らす。一つのオブジェクトの
   属性を別のオブジェクトから独立して変更できる。

   このモードは、特に *Tweak Tool* で操作するオブジェクトを作成するときに便利
   だ。

:guilabel:`Spray clones of the initial selection`
   ツールチップの文言が上のものと酷似しているが、複製がシンボリックリンク的であ
   るという違いがある。元オブジェクトの属性を変更すると、複製すべての属性が変化
   する。

   このモードは先のモードよりもレンダラーへの負荷が中程度に低い。

:guilabel:`Spray objects in a single path`
   このモードだけは本書のイラストで挙動を理解するしかない：

      The copies are merged into one path with overlaps removed.

   * 元オブジェクトの型によっては、それを最初にパスに変換する必要がある。
   * オブジェクトの重なりは削除される。
   * このモードは :abbr:`CPU` をより酷使する。

:guilabel:`Delete sprayed items from selection`
   おそらくスプレー元オブジェクトを指定してからドラッグすることで、スプレーオブ
   ジェクトをドラッグで消去する。

* copy mode は :guilabel:`Tweak` tool と組み合わせて使うと便利。
* clone mode は文字通り。copy mode よりも描画がかなり少ない。
* single path mode はオブジェクトが一体化する。:abbr:`CPU` に負荷がかかる。
* 選択後 a or :kbd:`Shift` + :kbd:`F3` で起動。

*Spray Tool* の起動方法は次のどれか：

* :guilabel:`Toolbox` から :guilabel:`Spray copy or clone objects` アイコンをク
  リックする。
* :kbd:`Shift` + :kbd:`F3` を押すか :kbd:`A` を押す。

他のツール同様、起動中は :kbd:`Space` 押しで *Select Tool* と往復できる。

*Spray Tool* のパラメーター、オプションは次のツールバー内の UI で制御する：

:guilabel:`Width`
   スプレーの範囲。この円内にオブジェクトが散布される。

   数値周りの仕様は *Tweak Tool* の :guilabel:`Width` と同様。

:guilabel:`Amount`
   オブジェクトをどれくらい多くスプレーするか。

   数値周りの仕様は *Tweak Tool* の :guilabel:`Force` と同様。

:guilabel:`Rotation`
   当ツールは各コピーにランダムな回転を加えるのだが、その最大回転量を指定する。

   * 値は 0 から 100 までが有効。0 は回転しない。
   * 値 100 が ±180°に相当する。

:guilabel:`Scale`
   当ツールは各コピーをランダムに拡縮するのだが、その最大倍率を指定する。

   * 値は 0 から 100 までが有効。1 は拡縮しない。
   * 値 100 が最大二倍に相当する。

:guilabel:`Scatter`
   オブジェクトをどのように散布するかを指定する。

   値は 1 から 100 までが有効。1 はポインターの下にあるオブジェクトすべてがスプ
   レーされることを表し、100 はスプレー領域に均等に分布することを表す。

:guilabel:`Focus`
   散布されるオブジェクトの広がりを指定する。

   値は 0 から 100 までが有効。0 はポインターの下にあるアイテムすべてが散布さ
   れ、100 は散布領域の境界にあるオブジェクトが散布される。

一部 UI 項目は感圧式入力装置に対応しているが、私は使わないのでノートを省略。

:guilabel:`Scatter` と :guilabel:`Focus` の違いが文面からだとわかりにくいが、
前者はスプレー噴射口、後者はスプレーを持つ手の振り方を制御するものだと思う。
