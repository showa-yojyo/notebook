======================================================================
Annex D: Tabular Notation for Sequence Diagrams
======================================================================
UML 2.5 pp. 747-749 に関するノート。
Tabular Notation を利用する予定がなければ読まなくてもよいかもしれない。

.. contents:: ノート目次

* この付録では sequence 図の代わりの表の表記法の特徴を述べる。
  この表記法をなす表の列の記述は次のようなものである。

  #. Lifeline Class:
     Lifeline の Class を指名する。
     Lifeline 記号上に Class 名がなければ、このクラス名は省略する。

  #. Lifeline Instance:
     Lifeline の Instance を指名する。
     Lifeline 記号上に Instance 名がなければ、このオブジェクト名は省略する。

  #. Constraint:
     ある種の制約を指定する。
     例えば斜線の記号は ``{delay}`` を意味する。
     CombinedFragments を表現するために、それらの演算子は
     角括弧で飾られるインデックスを使って示す。
     InteractionUse の場合には、
     括弧付きの Diagram ID として示し、
     参照される Interaction Diagram を指定し、
     ``ref(M.sq)`` のような感じで ``ref`` タグを使う。

     * 「角括弧で飾られるインデックス」というのは
       配列の表記法を思い浮かべればよい。

  #. Message Sending Class:
     入って来る矢印それぞれに向けてクラス名を送信するメッセージを指名する。

  #. Message Sending Instance:
     入って来る矢印それぞれに向けてオブジェクト名を送信するメッセージを指名する。
     InteractionUse から出て行く Gate メッセージの場合には、
     括弧付きの Diagram ID として示し、
     参照される Interaction Diagram を指定し、
     ``_(M.sq)`` のような感じでアンダースコアを使う。

  #. Diagram ID:
     対応する sequence/communication 図を記述する文書を識別し、
     対応する sequence/communication 図を含むファイルの名前の可能性がある。

  #. Generated instance name:
     sequence/communication 図のオブジェクト記号それぞれに与えられる
     識別子の名前。
     各文書で識別子の名前は一意である。

  #. Sequence Number:
     sequence/communication 図上の対応するメッセージ番号。

  #. Weak Order:
     イベントの半順序を指定するが、
     メッセージ受信イベントはそのメッセージ送信イベントの後に発生する必要がある
     ことを考慮した上で、
     個別の生存線上と生存線を横断した順序として決まる。
     Events は ``e`` + イベント順 + イベント方向 として示す。

     * イベント方向は ``i`` か ``o`` らしい。

  #. Message name:
     sequence/communication 図上の対応するメッセージ名。

  #. Parameter:
     sequence/communication 図上の対応するメッセージの
     引数の変数名と引数型の集合。

  #. Return value:
     sequence/communication 図上の対応するメッセージの戻り値の型。

  #. Message Receiving Class:
     出て行く矢印それぞれに向けてクラス名を受信するメッセージを指名する。

  #. Message Receiving Instance:
     出て行く矢印それぞれに向けてオブジェクト名を受信するメッセージを指名する。
     普通のオブジェクト記号から出て行く Gate メッセージの場合には、
     ``(out_s)`` のようにタグ ``out_`` の付いた
     括弧付きのメッセージ名として示す。

  #. Other End:
     各メッセージの別の端 (another end) のイベント順序を指名する。

D.1 Examples
======================================================================
* Figure D.1 Sequence diagram enhanced with identification of the Event occurrences

  * 説明用の sequence 図。
  * Event 発生地点にはフキダシで名前が付けられている。

* Table D.1 Interaction Table describing Figure D.1

  * 上述の図を tabular notation で表現したもの。
  * 仮にこれを書くなら、おそらく Weak Order の列をまず埋めるだろう。

* Figure D.2 Sequence diagram with guards, parallel composition and alternatives

  * 説明用の sequence 図。
    Lifeline は A のみで、par の中に alt が入れ子になっている。

* Table D.2 Interaction Table for Figure D.2

  * 上述の図を tabular notation で表現したもの。
  * ``in_y`` のような Message Sending Instance の書き方があることに注意。

.. include:: /_include/uml-refs.txt
