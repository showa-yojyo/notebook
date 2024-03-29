======================================================================
Python 入門［２＆３対応］読書ノート 1/3
======================================================================

Windows XP の Python 2.6.6 を利用して、本書を読み解いていく。文章を読むだけでは
なく、可能な限りサンプルコードを実際にタイプして実行することを基本作業とする。

インターネットに接続できない環境で作業をするため、それ系の機能は残念ながら試せな
い。

.. include:: /_include/book-details/hosoda10.txt

.. contents:: ノート目次

第 1 章 Python へようこそ
======================================================================

イントロダクション。

1.1 Python の特徴
----------------------------------------------------------------------

* <マジックメソッドによるアスペクト指向プログラミング> (p. 16) なる用語がいきな
  り出てくる。本書は Python の入門書であり、プログラミングの入門書ではないように
  感じた。
* <Python では C や C++ との連携が配慮されています。（略）速度のボトルネックに
  なる部分はほんの一部の特定の処理の場合が多いため、その部分だけ C や C++ で書い
  て、後は Python で書くことで生産性が高くなります> (pp. 16-17) これは是非挑戦し
  てみたい。

* Disney
* Ohloh.net - 後で見ておくこと。

1.2 本書について
----------------------------------------------------------------------

* <本書の目的は、Python の魅力を伝えることです> (p. 19) これは果たせていると思
  う。
* この人気モジュールベストテンの表は面白い。ベストファイブまでは納得のラインナッ
  プなのだが、それ以下が意外。例えばこの本を読むまで ``logging`` なんて使ったこ
  とがない。
* 2-15 章が文法編で、それ以降が実践編。当ノートは実践編を重視する。

第 2 章 実行環境の用意
======================================================================

2.1 Python のインストール
----------------------------------------------------------------------

:file:`C:\\Python26` に加え :file:`C:\\Python26\\Scripts` も ``PATH`` 環境変数に
追加したいところ。

2.2 起動と終了
----------------------------------------------------------------------

* ``help`` 関数が便利。

2.3 Python 開発環境
----------------------------------------------------------------------

テキストエディター対 IDE なわけだが、ここは読む価値がある。

* PyDev は試していない。Eclipse のプラグインと聞いては……。
* Komodo Edit は高機能っぽい。ちょっと使って疲れてやめた。メモリ消費量がちと多め
  か。
* PyScripter はまあまあいい。

  * どういうわけかたまに ini ファイルが壊れるのが痛い。
  * プロジェクトファイルの扱いが面倒過ぎて泣ける。

最近 PyScripter で固定にした。テキスト編集はいつもの Xyzzy で、実行周りを
PyScripter でやる。

第 3 章 Python の基本
======================================================================

3.1 基本操作
----------------------------------------------------------------------

* <従来の割り算はスラッシュ 2 つの ``//`` 演算子に置き換わりました> (p. 36)
* 括弧内ならば自由に改行できる。(p. 40)

3.2 複合文
----------------------------------------------------------------------

* <1 つのインデントは（略）慣例的にスペース 4 つを使うことが推奨されています>
  (p. 41) エディターや IDE の設定を確認しておくこと。
* ``print`` は Python 2 系では式だが、3 系からは関数に変わる。<``print('a')``
  という書き方に関しては、2 系、3 系で互換性があるので、本書では基本的にこの書き
  方を用いています> (p. 45)

3.3 オブジェクト
----------------------------------------------------------------------

* <全てのデータは「オブジェクト」> (p. 46)
* 「変更可能」と「変更不可能」の意味がよくわからない。p. 47 のコード例は正直、理
  解不能。なんで 1 足したくらいで別物になるのだ？

第 4 章 リスト
======================================================================

4.4 リストの更新
----------------------------------------------------------------------

* <メソッドである ``sort`` と ``reverse`` は自分自身を変更し、組み込み関数である
  ``sorted`` と ``reversed`` は新たなリストとして結果を戻します> (p. 64)
* 囲み記事の <要素の比較の度に比較関数を呼び出すよりも、全ての要素にキー関数を適
  用してから比較を行う方が、実行効率が良い> (p. 67) の意味がわからない。

4.6 その他のリストの操作
----------------------------------------------------------------------

* ``b = a[:]`` はコピーだと思っていたが、厳密に言えば「浅いコピー」だ。<深いコ
  ピーは ``copy`` モジュールの ``deepcopy`` 関数を使用して行います> (p. 71)
* リスト内包表記は習得すること。

第 5 章 辞書
======================================================================

5.2 辞書の作成
----------------------------------------------------------------------

* 辞書オブジェクトのコピーは ``copy`` メソッドを利用する。
* ``dict.fromkeys`` メソッドでキーのコレクションから辞書オブジェクトを作成でき
  る。

5.4 辞書の更新
----------------------------------------------------------------------

* ``setdefault`` メソッドは C++ の STL で言うところの ``std::map::operator[]``
  みたいなものか。

5.5
----------------------------------------------------------------------

囲み記事 (p. 90) の ``OrderedDict`` はリストじゃだめなんですか？

5.6 その他の辞書の操作
----------------------------------------------------------------------

* 辞書オブジェクトのコピーも<コンテナ型オブジェクトのため、コピーの際には浅いコ
  ピーと深いコピーの使い分けが必要です> (p. 91)
* <Python 3 から、リスト内包表記のように辞書でも内包表記が使える> (p. 93)

第 6 章
======================================================================

* コレクションオブジェクトを要素列から作成するときいは、列末尾にカンマを入れてお
  く習慣をつけたほうがいいかもしれない。

第 7 章 セット
======================================================================

7.1 セットの概要
----------------------------------------------------------------------

C++ STL の ``set`` みたいなものか。

7.2 セットの作成
----------------------------------------------------------------------

集合演算を行うメソッド名が、馴染みがある名前で助かる。

7.3 セットの読み込み
----------------------------------------------------------------------

``issubset`` と ``issuperset`` はどちらかがあればもう一方は要らない？

7.4 セットの更新
----------------------------------------------------------------------

集合演算名と ``update`` がメソッド名になっているものがある。

7.5 セットの削除
----------------------------------------------------------------------

* <指定した要素が存在しない場合、``remove`` メソッドは ``KeyError`` 例外が発生し
  ますが、``discard`` メソッドは発生しません> (p. 123)

第 8 章 条件分岐とループ
======================================================================

8.1 条件分岐
----------------------------------------------------------------------

* Python は ``elif`` を使う。
* Python には switch 文は存在しない。
* ``bool(-1)`` は私の環境では ``True`` になるのだが？
* <論理演算の戻り値は少し特殊で、演算対象のオブジェクトそのものが返されます> (p.
  134)

8.2 ループ
----------------------------------------------------------------------

* <複数の変数に同時に代入する方法を「アンパック代入」と言い> (p. 137)
* <特殊な構文として、``for`` 文や ``while`` 文のループ処理の後に、``else`` 節
  が記述できます。``break`` 文でループが中断されなかった場合に限り、``else`` ブ
  ロックが実行されます> (p. 139)
