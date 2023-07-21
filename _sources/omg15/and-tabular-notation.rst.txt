======================================================================
Annex D: Tabular Notation for Sequence Diagrams
======================================================================

.. contents::
   :depth: 2

この付録では sequence 図のオプションの表形式記法を述べる。

Lifeline Class
   Lifeline の Class 名。Lifeline 記号に Class 名がない場合は省略する。
Lifeline Instance
   Lifeline の Instance 名。Lifeline 記号に Instance 名がない場合は省略する。
Constraint
   何らかの制約を表す。例えば斜線の指示は ``{delay}`` と表記される。
   CombinedFragments を表現するために、それらの演算子は角括弧で飾られたインデッ
   クスを使って示す。InteractionUse の場合には、``ref(M.sq)`` のような感じで、参
   照される Interaction Diagram を指定する Diagram ID に ``ref`` タグを付けて括
   弧でくくって示す。

   .. admonition:: 読者ノート

     「角括弧で飾られたインデックス」というのは配列の表記法を思い浮かべればよい。

Message Sending Class
   到着矢印それぞれに向けられるメッセージを送信するクラスの名前。
Message Sending Instance
   到着矢印それぞれに向けられるメッセージを送信するオブジェクトの名前。
   InteractionUse から出発するメッセージである Gate メッセージの場合、
   ``_(M.sq)`` のように、参照される Interaction Diagram を指定する Diagram ID に
   アンダースコアを括弧でくくって示す。
Diagram ID
   対応する sequence/communication 図を記述する文書を識別し、対応する
   sequence/communication 図を含むファイルの名前を指定することが可能だ。
Generated instance name
   sequence/communication 図のオブジェクト記号それぞれに与えられる識別子名。識別
   子名は文書ごとに一意だ。
Sequence Number
   sequence/communication 図上の対応するメッセージ番号。
Weak Order
   イベントの半順序を指定するが、個々の生存線上で、あるいは横断して、与えられた
   メッセージ受信イベントは、そのメッセージ送信イベントの後に起こることが必要
   だ。イベントは ``e`` + イベント順 + イベント方向（到着か出発）として示す。

   .. admonition:: 読者ノート

      イベント方向は ``i`` か ``o`` らしい。
Message name
   sequence/communication 図上の対応するメッセージ名。
Parameter
   sequence/communication 図上の対応するメッセージの引数変数名と引数型の集合。
Return value
   sequence/communication 図上の対応するメッセージの戻り値の型。
Message Receiving Class
   出発矢印それぞれから向けられたメッセージを受信するクラスの名前。
Message Receiving Instance
   出発矢印それぞれから向けられたメッセージを受信するオブジェクトの名前。普通の
   オブジェクト記号からの出発メッセージである Gate メッセージの場合、
   ``(out_s)`` のようにタグ ``out_`` の付いたメッセージ名を括弧で括って示す。
Other End
   各メッセージの別の端子のイベント順序。

D.1 Examples
======================================================================

   Figure D.1 Sequence diagram enhanced with identification of the Event
   occurrences

説明用の sequence 図。Event 発生地点にはフキダシで名前が付けられている。

   Table D.1 Interaction Table describing Figure D.1

上述の図を tabular notation で表現したもの。仮にこれを書くなら、おそらく Weak
Order の列をまず埋めるだろう。

   Figure D.2 Sequence diagram with guards, parallel composition and
   alternatives

説明用の sequence 図。Lifeline は A のみで、par の中に alt が入れ子になってい
る。

   Table D.2 Interaction Table for Figure D.2

上述の図を tabular notation で表現したもの。``in_y`` のような Message Sending
Instance の書き方があることに注意。

.. include:: /_include/uml-refs.txt
