======================================================================
17 Interactions
======================================================================

.. contents::
   :depth: 4

17.1 Summary
======================================================================

17.1.1 Overview
----------------------------------------------------------------------

Interactions はさまざまな状況で利用される。

* 設計者個人や状況を共通理解する必要がある集団にとって、相互作用の状況をよく把握
  するために用いられる。
* より詳細な設計段階でも用いられる。
* テスト実行時に、システムの trace が相互作用として記述され、以前の局面のものと
  比較することが可能だ。

本章では用語「事跡」を「イベント発生の列」(sequence of event occurrences) の意で
用いる。

   We may denote this by <eventoccurrence1, eventoccurrence2, ...,
   eventoccurrence-n>. We are aware that other parts of the UML language
   definition use the term “trace” for other purposes.

Interaction 仕様は許可される事跡と却下される事跡に半順序 (partial ordering) 制約
を課す。半順序とは、任意の system trace でイベント（複数形）が発生することが可能
（または不可能）な順序を制限するものだ。

   The Interaction package describes the concepts needed to express
   Interactions, depending on their purpose.

相互作用はいくつかの異なる型の図式で示すことが可能だ：

* Sequence Diagrams
* Interaction Overview Diagrams
* Communication Diagrams
* Timing Diagrams: オプション図式型
* Interaction Tables: オプション図式型

Interactions は計算機システム設計の専門家、潜在的な末端利用者や利害関係者らが、
さまざまな詳細度で理解、製造可能であるシステムを記述するための共通の枠組だ。

   Typically when interactions are produced by designers or by running systems,
   the case is that the interactions do not tell the complete story.

プロジェクトによっては、システムの可能な trace すべてを相互作用を通じて文書化す
ることを要求する場合がある。

   The most visible aspects of an Interaction are the messages between
   lifelines. The sequence of the messages is considered important for the
   understanding of the situation.

Interactions はデータの操作には焦点を当てていない。

   By :dfn:`interleaving` we mean the merging of two or more traces such that
   the events from different traces may come in any order in the resulting
   trace, while events within the same trace retain their order.

この意味は、二つのイベントがまった同時に発生すると認識される意味とは異なる。
Interactions を説明するために interleaving 意味を適用する。

17.1.2 Basic trace model
----------------------------------------------------------------------

:doc:`./ch13-common-behavior` では Behaviors の実行に関する一般的な意味が述べら
れている。Interactions とは出現挙動をモデル化する Behaviors の一種だ (13.1)。

Behavior の実行は実行事跡を残す。

   Such a trace is a sequence of event occurrences, which, in this clause, will
   be denoted <e1, e2, ..., en>.

各イベント発生は、その発生時点におけるすべての関連オブジェクトの値に関する情報を
含むこともある。

   The semantics of an Interaction are expressed in terms of a pair [P, I],
   where P is the set of valid traces and I is the set of invalid traces.

* :math:`P \cup I` が事跡の全集合である必要はない。
* 二つの Interactions はその事跡集合対同士が等しい場合、等しい。

..

   The semantics of each construct of an Interaction (such as the various kinds
   of CombinedFragments) are expressed in terms of how they relate to a pair of
   sets of traces.

簡単のため、通常は有効な事跡の集合にしか言及しない。これらの事跡が最もモデル化さ
れるものだから。

17.1.3 Partial ordering constraints on valid and invalid traces
----------------------------------------------------------------------

   The set of valid traces is constrained by a partial ordering of the event
   occurrences in the traces.

無効な事跡の集合も同様だ。

相互作用図では、垂直線それぞれが工程の時間軸を表し、ページが進むにつれて時間が経
過していく。

   The instances in an interaction in principle operate independently of each
   other. No global notion of time is assumed.

* 大域的時間の概念は設けていない。
* オブジェクト間のタイミングの依存関係は、あるメッセージを受信する前にそれを送信
  しなければならないという制約から来るものしかない。

時間はオブジェクト軸それぞれに沿って上から下へと経過するが、正当な時間尺度は仮定
されない。

   If no coregion or parallel operator is introduced, a total time ordering of
   events is assumed along each instance.

別々のオブジェクトのイベントはメッセージ (17.4.3) を通じて、または一般化された順
序付けの枠組を通じて整列される。メッセージはそれが消費されるよりも前にまず送信さ
れなければならない。

   With the generalized ordering mechanism "orderable events" on different
   instances (even in different interactions) can be ordered explicitly.

* 他の順序は規定されない。
* ゆえに、相互作用仕様は含まれるイベントの集合に対して半順序を課す。
* 推移的かつ反対称的かつ非反射的な二項関係は半順序と呼ばれる。

17.1.4 Interaction Diagram Variants
----------------------------------------------------------------------

相互作用図にはさまざまな種類がある：

Sequence Diagrams
  これがもっとも普通の変種。複数の Lifelines 間の Message 交換に焦点を当てるもの
  だ。
Communication Diagrams
  通信する Lifelines の間にある有向辺が引き渡された Messages とその列の記述で装
  飾される、建築学的展望を通して相互作用を示す。
Interaction Overview Diagrams
  制御の流れの概要を示すように相互作用を定義する。一部 Activity 図と類似した記法
  要素がある。これらの要素の記法と一般的な目的は両者で同じではあるが、詳細な意味
  はまったく異なるので、設計者は Overview 図を Activity 図であるかのように解釈す
  るべきではない。
Timing Diagrams
  図の主な目的が時間に関する思考である場合に、相互作用を示すために用いられ
  る。UML 2.5 準拠ツールは Timing Diagrams を実装する必要はない。

本章にある Interaction 図の変種に加えて、オプションとして Interaction Tables を
用いた記法がある (:doc:`./and-tabular-notation`)。

17.2 Interactions
======================================================================

17.2.1 Summary
----------------------------------------------------------------------

本節では次のメタクラスを規定する：

* Interaction
* InteractionFragment
* OccurrenceSpecification
* ExecutionSpecification
* StateInvariant

17.2.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 17.1 Interactions

まず抽象クラス InteractionFragment が NamedElement から特殊化されている。
そして InteractionFragment から残りのメタクラス四つが特殊化されている。

メタクラス Interaction は InteractionFragment であると同時に Behavior でもある。

17.2.3 Semantics
----------------------------------------------------------------------

17.2.3.1 Interactions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Interactions are units of behavior of an enclosing Classifier. Interactions
   focus on the passing of information with Messages between the
   ConnectableElements of the Classifier.

Interaction の意味は事跡の集合の対として与えられる。その二つの事跡の集合は有効な
事跡と無効な事跡を表現する。

* これら二つの集合の和は必ずしも事跡全体を網羅する必要はない。
* 含まれていない事跡はこの Interaction には全く記述されないので、我々はそれらが
  有効か無効かを知ることはできない。

事跡一つはイベント発生の列であり、それぞれはモデル内の OccurrenceSpecification
により記述される。

   The semantics of Interactions are compositional in the sense that the
   semantics of an Interaction is mechanically built from the semantics of its
   constituent InteractionFragments. The constituent InteractionFragments are
   ordered and combined by the seq operation (weak sequencing) as explained in
   17.6.3 (Weak Sequencing)

無効な事跡の集合は Negative CombinedFragment または Assertion CombinedFragment
の用途に関連する。

* 前者の場合、無効な事跡の集合は明示的に指定される。
* 後者は、唯一有効な事跡の集合を明示的に指定することで、無効な事跡の集合を暗に指
  定する。簡単のために、他の構成要素のすべてに対して有効な事跡しか述べられていな
  い。

Behavior として Interaction は一般化可能かつ再定義可能だ。Interaction を特殊化す
ることは、さらなる事跡を元の Interaction に対して単に追加することだ。この特殊化
で定義される事跡は、継承した Interaction の事跡との和集合となる。

   The classifier owning an Interaction may be specialized, and in the
   specialization the Interaction may be redefined.

Interaction の再定義とは、再定義元の Interaction を再定義先の Interaction に交換
することを単に意味し、この交換は所有者の基底型にある InteractionUses に対しても
有効だ。このことは Behavior の他の種類の再定義と似ている。

   A formal Gate may be attached to the inner boundary of an Interaction to
   provide a link point to establish the concrete sender and receiver through an
   InteractionUse of that Interaction.

17.2.3.2 Interaction Fragments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   The semantics of an InteractionFragment is a pair of set of traces. See
   17.1.2 for explanation of how to calculate the traces.

InteractionFragment は取り囲む Interaction に直接含まれるか、CombinedFragment の
InteractionOperand に含まれるかのどちらかでよい。CombinedFragment はそれ自身が
InteractionFragment なので、Interaction 一つの内部に InteractionFragments を深く
入れ子にしてもよい。

17.2.3.3 Occurrence Specifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   The semantics of an OccurrenceSpecification is just the trace of that single
   OccurrenceSpecification.

OccurrenceSpecification の理解とより深い意味は関連 Message とそれが伝える情報次
第だ。

17.2.3.4 Execution Specifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   The trace semantics of Interactions merely see an Execution as the trace
   <start, finish>.

これらの間に発生がある場合がある。

通常、開始発生と終了発生は（ある Message の）受信 OccurrenceSpecification と（あ
る応答 Message の）送信 OccurrenceSpecification などの OccurrenceSpecifications
を表現する。

17.2.3.5 State Invariants
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Constraint は実行中に評価されるものとする。

   The Constraint is evaluated immediately prior to the execution of the next
   OccurrenceSpecification such that all actions that are not explicitly modeled
   have been executed.

Constraint が真の場合、その事跡は有効な事跡だ。反対に偽の場合、その事跡は無効
な事跡だ。

言い換えると、Constraint が偽である StateInvariant を持つ事跡はすべて無効である
とみなされる。

17.2.4 Notation
----------------------------------------------------------------------

17.2.4.1 Interaction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sequence 図における Interaction を表す記法は実線矩形だ。

矩形の左上隅に五角形を描き、そこに文字列 ``sd`` と Interaction 名と引数をこの
順に記す。

この矩形の枠内の記法には次の形式がある：

* Sequence Diagrams
* Communication Diagrams
* Interaction Overview Diagrams
* Timing Diagrams

五角形記述子の内側の記法は Behaviors の名前を表すのに用いる記法一般に従う。

* Interaction Overview Diagrams には生存線句を通して Lifelines の一覧を含めるこ
  とが許される。生存線の一覧は単にその Interaction に関与する Lifelines の一覧
  だ。
* Interaction Overview Diagrams はグラフ節点内のインライン Interactions の中で寿
  命線が明示的に出現していても、それ自体では関与する生存線を示さない。

Interaction 図は一般的な属性と同じ構文を持つ局所的属性の定義を、クラス記号の区画
内に含むことが許される。

これらの属性定義が図の枠の上部付近に示されることもあれば、図の他の場所にある
Comment 記号の中に示されることもある。

17.2.4.2 InteractionFragment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   There is no general notation for an InteractionFragment. The specific
   subclasses of InteractionFragment define their own notation.

17.2.4.3 OccurrenceSpecification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

OccurrenceSpecifications は単に

* Messages の両端もしくは
* ExecutionSpecification の開始・終了

における構文的な点でしかない。

17.2.4.4 ExecutionSpecification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ExecutionSpecifications は生存線上の細い（灰色か白色の）矩形として表現される。

または ExecutionSpecification を幅広のラベル付き矩形により表現してもよく、ラベル
はたいていは実行されたアクションを識別する (Fig. 17.16)。

   For ExecutionSpecifications that refer to atomic actions such as reading
   attributes of a Signal (conveyed by the Message), the Action symbol may be
   associated with the reception OccurrenceSpecification with a line in order to
   emphasize that the whole Action is associated with only one
   OccurrenceSpecification (and start and finish associations refer to the very
   same OccurrenceSpecification).

線の付いた OccurrenceSpecification とは？

   Figure 17.2 Overlapping ExecutionSpecifications

同一生存線上で重なり合う ExecutionSpecifications はやはり重なり合う矩形で表現さ
れる。

17.2.4.5 StateInvariant
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

関連する可能性のある Constraint は生存線上に中括弧に囲まれたテキスト (Fig.
17.17) で示される。

   A conforming tool may show a StateInvariant as a Note associated with an
   OccurrenceSpecification.

状態記号は、Lifeline によって表されるオブジェクトの状態を検査する制約相当のもの
を表す。これは対応する ClassifierBehavior の ``classifierBehavior`` の内部状態で
ある可能性も、その Lifeline の黒箱ビューに基づく外部状態である可能性もある。前者
の場合に ``classifierBehavior`` が状態機械で記述されている場合、その状態の名前は
この状態機械の対応する状態の階層名となるべく合致する。

領域は状態（複数形）の直交領域を表現する。

* 識別子は状態を部分的に定義しさえすればよい。
* 制約の値は指定された状態情報が真であるならば真だ。

17.2.4.6 Formal Gate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

形式 Gate は枠の内側にある単なる点であり、あるメッセージの端子だ。それらには明示
的な名前があってもよい (Fig. 17.4)。

17.2.5 Examples
----------------------------------------------------------------------

   Figure 17.3 An example of an Interaction in the form of a Sequence Diagram

``User`` と ``ACSystem`` 型の匿名生存線間で通信されるメッセージ三つを示している。

矢印がメッセージ。メッセージ ``CardOut`` は受信イベント発生が送信元
OccurrenceSpecifications と逆の順序になっている点で、メッセージ ``OK`` を追い越
している。このような通信は、メッセージが非同期の場合に発生することがある。

最後に、``out_Unlock`` という暗黙的な名前を持つ形式ゲートを介して、``ACSystem``
からその環境へ四番目のメッセージが送信される。

``UserAccepted`` の局所属性 ``PIN`` がこの図式の先頭付近で宣言されている。図式中
の他のどこかの Comment で宣言することも可能だ。

   Figure 17.4 OccurrenceSpecification

メッセージ ``msg`` の矢印の根本が OccurrenceSpecification の例だ。

先と同様に矢印の鏃が図枠に至っている点が形式ゲートの例だ。

   Figure 17.5 Sequence Diagram with time and timing concepts

以前やった時間にまつわる記法が再録されているので復習したい。

* ``User`` はメッセージ ``Code`` を送信。その送信と受信の間の時間が測定される。
* ``ACSystem`` はメッセージを二つ ``User`` に送信する。

  * ``CardOut`` は 0 から 13 時間単位の間継続するように制約される。
  * ``OK`` 受信は ``Code`` 送信から ``d`` から ``3 * d`` の間に制約される。
  * ``OK`` 送信から ``t`` を観測し、受信までの時間を ``t + 3`` 以内に制約する。

17.3 Lifelines
======================================================================

17.3.1 Summary
----------------------------------------------------------------------

本節ではメタクラス Lifeline を規定する。

17.3.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 17.6 Lifelines

Lifeline は NamedElement の一種。継承関係よりも関連のほうが多い。

17.3.3 Semantics
----------------------------------------------------------------------

17.3.3.1 Lifelines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   In an interaction diagram a Lifeline describes the time-line for a process,
   where time increases down the page.

時間軸上のイベント間の距離は、文字どおりの時間の測定値を表すのではなく、ゼロ以外
の時間が経過したことを示すに過ぎない。

同一時間軸上のイベントは、ページの下に向かって直線的に整列される。ただし、並列に
結合した断片の内部で起こる場合、すなわち余領域内の生存線に沿って発生する場合を除
く。

   Within a parallel combined fragment or a coregion, events are not locally
   ordered unless that is directly imposed by a general ordering construct. See
   17.5.3 (General Ordering).

Lifeline に沿った OccurrenceSpecifications の順序は、これらが発生する順序を示す
重要なものだ。この Lifeline 上の OccurrenceSpecifications 間の絶対的な距離はその
意味とは無関係だ。

   The semantics of the Lifeline (within an Interaction) is the semantics of the
   Interaction selecting only OccurrenceSpecifications of this Lifeline.

17.3.4 Notation
----------------------------------------------------------------------

17.3.4.1 Lifeline
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lifeline は「頭」となる矩形と、参加者の生存線を表現する破線スタイルの垂直線から
なる記号で示される。生存線を識別する情報は以下の形式で矩形の内側に示される：

.. code:: bnf

   <lifelineident> ::= (
     [<connectable-element-name>[‘[’ <selector> ‘]’]]
     [‘:’ <connectable-element-type>]
     [<decomposition>])
     | ‘self’

   <selector> ::= <expression>

   <decomposition> ::= ‘ref’ <interactionident> [‘strict’]

* ``<connectable-element-type>`` は ConnectableElement が型付けられた Type の名
  前を指す。
* 構文上は許されているが ``<lifelineident>`` を空にすることは不可能だ。

Lifeline 頭はこの生存線が表現する部品の classifier に基づく形状だ。頭は往々にし
てその名前を含む白い矩形だ。

名前が ``self`` の場合、Lifeline が表現するものは、それを所有する Interaction を
囲む classifier のオブジェクトを表現する。

   Ports of the encloser may be shown separately even when self is included.

ExecutionSpecification を描写するには、Lifeline の線を覆う薄い灰色か白色の矩形を
適用する。

17.3.5 Examples
----------------------------------------------------------------------

Lifelines は先述した Figure 17.3 を参照。

ExecutionSpecification の記法を参照するには後述する Figure 17.14 を参照。

17.4 Messages
======================================================================

17.4.1 Summary
----------------------------------------------------------------------

本節では次のメタクラスを規定する：

* Message
* MessageEnd
* MessageOccurrenceSpecification
* MessageSort
* MessageKind
* DestructionOccurrenceSpecification
* Gate

17.4.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 17.7 Messages

Message と MessageEnd は NamedElement の一種だ。

MessageEnd には特殊型が直接、間接合わせて三個ある。

Message のある属性を実現するために列挙型 MessageKind と MessageSort がある。

17.4.3 Semantics
----------------------------------------------------------------------

17.4.3.1 Messages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   The semantics of a complete Message is simply the trace <sendEvent,
   receiveEvent>.

   A lost Message is a Message where the sending event occurrence is known, but
   there is no receiving event occurrence.

これは Message の宛先が記述の範囲外であるためと解釈される。意味としては
``<sendEvent>`` だ。

   A found Message is a Message where the receiving event occurrence is known,
   but there is no (known) sending event occurrence.

これは例えば、雑事であったり、詳細を記述したくない他の活動であったりする。意味と
しては事跡 ``<receiveEvent>`` だ。

Message の署名は Operation または Signal の一方を参照する。Message の名前は参照
される Operation または Signal の名前と同じでなければならない。

   NOTE. Lifelines cannot directly represent Types. However, any Lifeline
   representing a ConnectableElement with a Type having an Operation with
   ``isStatic`` = true, can accept Messages with a ``signature`` associated with
   that static Operation.

Message 署名が Operation である場合、Message は次のうちの一つを表す：

* ``messageSort`` が ``synchCall`` または ``asyncCall`` である場合、その Message
  はその Operation に対する同期呼び出しまたは非同期呼び出しおよびその Operation
  の実行の開始を表す。この Message の実引数はその Operation の in および inout
  ``ownedParameters`` に対応する。
* ``messageSort`` が ``reply`` である場合、その Message はその Operation の非同
  期呼び出しの戻り値を表す。この Message の実引数はその Operation の out, inout,
  return ``ownedParameters`` に対応する。

Message 署名が Signal である場合、``messageSort`` は ``asyncSignal`` でなければ
ならず、この Message は Signal オブジェクトの非同期送受信を表す。この Message の
実引数はこの Signal の属性に対応する。

Message の実引数は ValueSpecification だ。

   If the Message has a signature and it is not a reply Message, then its
   argument ValueSpecifications are considered to be evaluated at the point of
   the send event of the Message. Their results provide the values for the
   corresponding Operation input parameters or Signal attributes.

作用対象を持たない Expression とその記号としての空文字列からなる引数は、ワイルド
カードとして特別な解釈を持ち、対応する引数または属性の不特定だが合法な値に対応す
る。それ以外の場合、実引数の型は対応する引数または属性の型に準拠しなければならな
い。

   If the Message is a reply, then each of its arguments must be an Expression
   with at most one operand. If an operand is given, it is considered to be
   evaluated at the point of the send event of the Message, and its result
   provides the returned value for the out, inout or return parameter
   corresponding to the argument.

出力引数の型は作用対象の型に従わなければならない。作用対象が与えられない場合、そ
の実引数に対する応答 Message によって返される値はモデル化されない。

   The symbol of the argument Expression of a reply Message represents the
   *assignment target* for the argument, to which the returned value for the
   argument is to be assigned.

このような代入先記号に対する次の値は、標準的な解釈を持つ：

Unknown
   空文字列であり、未知の代入対象を表す。不明な代入先とモデル化された戻り値を持
   たない実引数は出力ワイルドカードだ。
Interaction Parameter
   包囲 Interaction の ``ownedParameter`` の修飾なしの名前であり、out, inout,
   return Parameter のいずれかであるものとする。実引数に対応する Operation
   Parameter の型は Interaction の対象となる ``ownedParameter`` の型に準拠する必
   要がある。
Attribute
   包囲する相互作用の context Behavior の属性または Message の受信側 Lifeline の
   （修飾されるかもしれない）名前だ。

      If an Interaction does not have a context Behavior, then the Interaction
      itself is considered to be the context. The type of the output parameter
      corresponding to the argument must conform to the type of the attribute.

   修飾名は、同じ名前を持つ context と Lifeline の属性、または同じ名前を持つ
   Interaction Parameter の属性を区別するために使われることもあることに注意。

代入先記号には他の値も許されるが、それらの解釈は本仕様で定義されない。

17.4.3.2 Message Ends
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MessageEnd のサブクラスはそれらが表す概念に相応しい特有の意味を定義する。

17.4.3.3 Message Occurrence Specifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MessageOccurrenceSpecification は二つの Lifelines の間にあるメッセージに関連する
送信イベントまたは受信イベントを表す。

17.4.3.4 Destruction Occurrence Specifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DestructionOccurrenceSpecification はそれを含む生存線により記述されるオブジェク
トの破壊を表す。その結果、このオブジェクトが所有する他のオブジェクトが複合によっ
て破壊される可能性がある (:doc:`./ch13-common-behavior`)。

17.4.3.5 Gates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A Gate is a MessageEnd which is used on the boundary of an Interaction, or an
   InteractionUse, or a CombinedFragment to establish the concrete sender and
   receiver for every Message.

Gate オブジェクトは、二つの Message オブジェクトを結びつける対として出現するの
で、それ自身に明示的な順序はない。Gates は MessageEnds であり、次のどちらかの間
に接続点を与える：

* InteractionUse の外側にある Message オブジェクトと使われる Interaction の内側
  にある Message オブジェクト
* CombinedFragment の外側にある Message オブジェクトと CombinedFragment 内の
  InteractionOperand の内側にある Message オブジェクト

MessageOccurrenceSpecifications は次の規則に則った半順序が入る：

* MessageOccurrenceSpecification オブジェクトは所有される Lifeline 上で整列さ
  れ、
* MessageOccurrenceSpecification オブジェクトは Message オブジェクト全体、または
  合致した gates の一対を通じてリンクされた Message オブジェクトの一対間で整列さ
  れる。いずれの場合も、送信側の MessageOccurrenceSpecification オブジェクトは、
  受信側の MessageOccurenceSpecification オブジェクトよりも前に順序付けられる。

Message オブジェクトそのものは整列されない。

   Gate instances, since they occur in a paired manner linking two Message
   instances, are also not themselves explicitly ordered.

Gates は四種類あり、関連により区別される：

形式 Gate
   Interaction に関連付けられる。
実 Gate
   InteractionUse に関連付けられる。
内部 CombinedFragment Gate
   CombinedFragment に関連付けられる。
外部 CombinedFragment Gate
   CombinedFragment に関連付けられる。

Gates は明示的にも暗黙的にも命名される。

   Gates may be identified either by name (if specified), or by a constructed
   identifier formed by concatenating the direction of the message and the
   message name (e.g., out_CardOut, in_CardOut).

Gates は名前によって合致され、形式 Gate は同じ名前を持つ実 Gate と、内部
CombinedFragment Gate は同じ名前を持つ外部 CombinedFragment Gate と合致する。

合致する Gates に対する Messages は対応しなければならない。同一の名前と
``messageSort`` と ``signature`` の特性値が同じで、同じ方向を向いていれば
Messages は対応する。

17.4.4 Notation
----------------------------------------------------------------------

17.4.4.1 Message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Message は送信側 MessageEnd から受信側 MessageEnd までの線分として示される。この
線は送信イベントから受信イベントへたどるとき、水平か下側に向いていなければならな
い。送信イベントと受信イベントは同一生存線上にあってもよい。

線分や鏃の形状は Message の性質を表す。

* ``messageSort == asynchCall || asynchSignal`` ⇒ 鏃を開く
* ``messageSort == synchCall`` ⇒ 鏃を塗りつぶす
* ``messageSort == reply`` ⇒ 破線
* ``messageSort == createMessage`` ⇒ 破線＋開いた鏃
* ``messageSort == deleteMessage`` ⇒ DestructionOccurrenceSpecification で終わる
* 消失 Message ⇒ 終点を小黒丸とする
* 発見 Message ⇒ 始点を小黒丸とする
* Communication 図における Messages は番号とかも添える。後述。

図中の Message ラベルの構文は BNF で定義されている：

.. code:: bnf

   <message-label> ::= <request-message-label> | <reply-message-label> | ‘*’

   <request-message-label> ::= <message-name> [‘(’[<input-argument-list>] ‘)’]

   <input-argument-list> ::= <input-argument> [‘,’<input-argument>*]

   <input-argument> ::= [<in-parameter-name> ‘=’] <value-specification> | ‘-’

``<message-label>`` が‘*’に等しい場合は、より複雑な代替の CombinedFragment の略
記法で、あらゆる型のメッセージを表す。これは State Machines の米印発火装置と合致
させるためだ。

   A request-message-label is used for all sorts of Message other than a reply.

   The message-name appearing in a request-message-label is the name property of
   the Message.

Message に署名がある場合、これがその署名が参照する Operation や Signal の名前に
なる。そうでない場合、名前に制約はない。

   If a request-message-label includes an input-argument-list, then either all
   input-arguments must have an in-parameter-name given or none may have one.

``<in-parameter-names>`` が与えられない場合、``<input-arguments>`` は Message の
引数を順番に表し、``-`` はワイルドカード引数を表す。

Message に署名がある場合、実引数は順番に Operation の in および inout の
``ownedParameters`` または Signal の属性に合致する。実引数はそのような引数や属性
ごとに与えられる必要がある。

   A request-message-label may only have input-arguments with in-parameter-names
   if the Message has a signature.

この場合、``<input-arguments>`` は Operation の in および inout の
``ownedParameters`` または Signal の属性と名前によって合致する。

* 名前が付けられていない引数や属性は、暗黙のワイルドカード引数を持つとみなされ
  る。
* ``<in-parameter-names>`` が指定されている場合、明示的なワイルドカード表記
  ``-`` は使用されない。

..

   If a request-message-label does not include an input-argument-list and the
   Message has a signature, then this denotes that the Message has wildcard
   arguments corresponding to all in and inout ownedParameters of an Operation
   or attributes of a Signal (if any).

括弧は ``<input-argument-list>`` の一部とはみなされないので、
``<input-argument-list>`` のない ``<request-message-label>`` は
``<message-name>`` の後に空の括弧 ``()`` を含めることが許される。

``<reply-message-label>`` は応答 Message に使われる：

.. code:: bnf

   <reply-message-label> ::=
     [<assignment-target> ‘=’]
     <message-name>
     [‘(’ [<output-argument-list>] ‘)’]
     [‘:’ <value-specification>]

   <output-argument-list> ::= <output-argument> [‘,’<output-argument>]*

   <output-argument> ::=
     <out-parameter-name> ‘:’ <value-specification>
     | <assignment-target> ‘=’ <out-parameter-name>
       [‘:’ <value-specification>]

``<reply-message-label>`` に表示される ``<message-name>`` は Message の ``name``
だ。

Message に署名がある場合、これがその署名で参照される Operation の名前になる（そ
の Operation の呼び出しに対する応答であるべきもの）。そうでなければ、名前は制約
されない。

   A reply-message-label may optionally have an assignment-target given to the
   left of the message-name, with a corresponding returned value denoted by the
   optional value-specification given after a colon at the end of the reply-
   message-label.

* Message が return 引数を持つ Operation の署名を持つ場合、この
  ``<assignment-target>`` や ``<value-specification>`` はその引数の実引数に対応
  する。
* Message が return 引数を持たない署名を持つ場合、``<reply-message-label>`` 全体
  に対して ``<assignment-target>`` や ``<value-specification>`` を与えることはで
  きない。

応答 Message が署名を持たない場合、指定できる実引数は上記のように return 引数し
かない。しかし、Message が ``ownParameters`` が out または inout の Operationで
ある署名を持つ場合、これらの引数に対して ``<output-arguments>`` を指定することが
許される。

* ``<output-argument>`` は常に、合致する引数の名前を明示的に指定する。
* 名前が付けられていない引数は、暗黙のワイルドカード実引数を持つとみなされる。し
  たがって、``<output-arguments>`` に明示的なワイルドカード表記は必要ない。

``<reply-message-label>`` が ``<output-argument-list>`` を含まず、Message が署名
を持つ場合、これは Message が（もしあれば）署名の Operation のすべての out およ
び inout ``ownedParameters`` に対応するワイルドカード実引数を持つことを示す。

括弧は ``<outut-argument-list>`` の一部とはみなされないので、
``<output-argument-list>`` のない ``<reply-message-label>`` は
``<message-name>`` の後に空の括弧 ``()`` を含めることが許される。

   An output-argument with an explicit assignment-target given may also
   optionally include a value-specification.

* ``<value-specification>`` が指定された場合、これはその実引数の戻り値を示す。
* そうでない場合、この実引数はモデル化された戻り値を持たない。
* ``<output-argument>`` に明示的な ``<assignment-target>`` が指定されていない場
  合、未知の代入先があるとみなされる。この場合、その実引数の戻り値を示す値指定が
  必要だ。

..

   If the identity of a reply Message is obvious (e.g., when its sendEvent is
   the only reply within the extent of an ExecutionOccurence where there is only
   one receipt of an Operation call message), the label may be omitted to
   simplify the diagram.

応答 Message に署名がある場合、その署名 Operation のすべての return, out, inout
``ownedParameters`` にワイルドカード実引数が指定される。Fig. 17.2 を参照。

17.4.4.2 DestructionOccurrenceSpecification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Figure 17.8 DestructionOccurrenceSpecification symbol

DestructionOccurrenceSpecification は Lifeline の底部にバツ印を記すことで示す。

17.4.4.3 Gate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gates は枠上の単なる点であり、メッセージの端点だ。明示的な名前を持つこともある。
Fig. 17.4 を参照。

17.4.5 Examples
----------------------------------------------------------------------

先述の Figure 17.3 では非同期 Messages しか見なかった。こういう Messages は互い
に追い抜いてもよい。

後述の Figure 17.14 では応答に伴う同期メソッド呼び出しを見る。またオブジェクト
を生成することを表現する Message も見る。

後述の Figure 17.26 では Communication 図における Messages の記法を見る。

メッセージ識別のテキスト的構文のさまざまな応用例を Figure 17.14 で見られる。

17.5 Occurrences
======================================================================

17.5.1 Summary
----------------------------------------------------------------------

本節では次のメタクラスを規定する：

* ActionExecutionSpecification
* BehaviorExecutionSpecification
* ExecutionOccurrenceSpecification
* GeneralOrdering

17.5.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 17.9 Occurrences

ExecutionSpecification の派生元が図では示されていないが、先述の
InteractionFragment だ。

ActionExecutionSpecification と BehaviorExecutionSpecification は兄弟。

17.5.3 Semantics
----------------------------------------------------------------------

17.5.3.1 Action Execution Specificiations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(17.2.3) 参照。

ActionExecutionSpecification は他の挙動が所有するものであることがある作用から生
じるメッセージを指定する相互作用に用いられる。

17.5.3.2 Behavior Execution Specifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(17.2.3) 参照。

BehaviorExecutionSpecification は挙動から生じるメッセージを指定する相互作用に用
いられる。

17.5.3.3 Execution Occurrence Specifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ExecutionOccurrenceSpecification はある生存線上において ExecutionSpecification
の開始イベントもしくは終了イベントを表現する。

17.5.3.4 General Orderings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GeneralOrdering はあり得る列の集合を制限する。OccurrenceSpecifications の半順序
は GeneralOrderings の集合により制約される。

17.5.4 Notation
----------------------------------------------------------------------

17.5.4.1 ActionExecutionSpecificiation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

17.2.4.4 節 (ExecutionSpecification) 参照。

17.5.4.2 BehaviorExecutionSpecification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

17.2.4.4 節 (ExecutionSpecification) 参照。

17.5.4.3 ExecutionOccurrenceSpecification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ExecutionOccurrenceSpecification は生存線上の ExecutionSpecification を表す垂直
な箱の始点または終点で表現される (Figure 17.2)。

17.5.4.4 GeneralOrdering
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GeneralOrdering は二つの OccurrenceSpecifications を接続する点線として示される。
矢印の方向を示す記号は線分の中ほどに描かれる。矢印の鏃には描かない。

17.5.5 Examples
----------------------------------------------------------------------

   Figure 17.10 Example showing GeneralOrdering in a sequence diagram

図式中の斜めに走っている線分が GeneralOrdering の見本だと言っている。

17.6 Fragments
======================================================================

17.6.1 Summary
----------------------------------------------------------------------

本節では次のメタクラスを規定する：

* InteractionOperand
* InteractionConstraint
* CombinedFragment
* ConsiderIgnoreFragment
* Continuation
* InteractionOperatorKind: これは列挙体。

17.6.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 17.11 Fragments

InteractionConstraint と InteractionOperatorKind を除いて抽象クラス
InteractionFragment の直接的または間接的特殊型だ。そのうち InteractionOperand は
Namespace の一種でもある。

InteractionConstraint は Constraint の特殊型だ。

InteractionOperatorKind はやたら literals が多い。

17.6.3 Semantics
----------------------------------------------------------------------

.. todo::

   クロスリファレンスのすべてに誤植があるような気がするので問い合わせる。
   17.6.3.x の x が欠けている。

17.6.3.1 Interaction Operands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   An InteractionOperand is a region within a CombinedFragment, see 17.6.3
   (Combined Fragment).

真である guards を持つ InteractionOperand しか意味の推定に含まない。存在しない場
合、真 guards を意味するとみなす。

InteractionOperand の意味は暗黙の seq 演算 (17.6.3.3) により結合された、その構成
要素たる InteractionFragments により与えられる。

17.6.3.2 Interaction Constraints
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

InteractionConstraints は常に CombinedFragments (17.6.3.3) と関連して用いられ
る。

17.6.3.3 Combined Fragments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   The semantics of a CombinedFragment is dependent upon the
   ``interactionOperator``, as explained below for each kind of
   ``interactionOperator``.

CombinedFragment に関連付けられた Gates は CombinedFragment とその周囲との間の構
文インターフェイスを表現する。これは他の InteractionFragments に対するインター
フェイスであることを意味する。

17.6.3.4 Consider Ignore Fragments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A ConsiderIgnoreFragment is a CombinedFragment with an Ignore or Consider
   ``interactionOperator`` value. See 17.6.3 (Ignore / Consider).

17.6.3.5 Continuations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Continuations have semantics only in connection with Alternative
   CombinedFragments and (weak) sequencing.

Alternative CombinedFragment の InteractionOperand が名前 X の Continuation で終
わる場合、その Continuation X から始まる InteractionFragments しか追加不能だ。

17.6.3.6 Interaction Operator Kind Values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

CombinedFragment の意味を決定するのに ``interactionOperator`` の値が重要だ。

17.6.3.7 Alternatives
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``interactionOperator`` **alt** は CombinedFragment が挙動の選択肢の一つを表現
することを示す。

* 高々一つの作用対象が選ばれる。
* 選択された作用対象はその相互作用のこの時点で真であると評価される guard 式を持
  たねばならない。
* その作用対象が guard を持たない場合、真 guard が暗黙の了解で定まる。

選択肢一つを定義する事跡の集合は、作用対象の（guard された）事跡の和集合だ。

``else`` によって guard される作用対象は CombinedFragment が囲んでいる他の
guards すべての論理和を指す。

作用対象が真と評価される guards を何も持たない場合、どの作用対象も実行されず、囲
んでいる InteractionFragment の残りの部分が実行される。

内部 CombinedFragment Gate が alt CombinedFragment の InteractionOperand のどれ
かに用いられる場合、同名の Gate がその alt CombinedFragment の
InteractionOperand それぞれで用いられなければならない。

17.6.3.8 Option
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``interactionOperator`` **opt** は CombinedFragment がその（ただ一つの）作用対象
が起こるのか、何も起こらないのかの挙動の選択肢一つを表現することを示す。

   An option is semantically equivalent to an alternative CombinedFragment where
   there is one operand with non-empty content and the second operand is empty.

17.6.3.9 Break
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``interactionOperator`` **break** は、作用対象が包囲 InteractionFragment の残り
の部分の代わりに行われるシナリオであるという意味で、CombinedFragment がシナリオ
の中断を表現することを示す。

* その guard が真であるとき、それがある break 作用が選ばれ、包囲
  InteractionFragment の残りが無視される。
* 作用対象の guard が偽であるとき、それがある break 作用は無視され、包囲
  InteractionFragment の残りが選ばれる。

..

   The choice between a break operand without a guard and the rest of the
   enclosing InteractionFragment is done non-deterministically.

``interactionOperator`` break のある CombinedFragment は包囲 InteractionFragment
の Lifelines すべてをなるべく覆う。

17.6.3.10 Parallel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``interactionOperator`` **par** は CombinedFragment が作用対象の挙動の間の並列合
併を表現することを示す。異なる作用対象の OccurrenceSpecifications は各作用対象が
課す順序が保存される限りは、どのような方法でも interleave 可能だ。

並列合併は作用対象内の OccurrenceSpecifications の順序を乱すことなく、作用対象の
OccurrenceSpecifications を interleave する手段すべてを記述する事跡の集合を定義
する。

17.6.3.11 Weak Sequencing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``interactionOperator`` **seq** は CombinedFragment が作用対象の挙動間における弱
い順序付けを表現することを示す。

弱い順序付けは次の性質を有する事跡の集合で定義される：

#. 作用対象それぞれの内部にある OccurrenceSpecifications の順序はその結果で維持
   される。
#. 異なる作用対象からの異なる生存線上の OccurrenceSpecifications はどのような順
   序で来てもよい。
#. 異なる作用対象からの同一生存線上の OccurrenceSpecifications は、最初の作用対
   象の OccurrenceSpecification がその次の作用対象のそれの前に来るように順序付け
   られる。

弱い順序付けは作用対象が関与者の共通部分のない集合にある場合、並列合併に縮約す
る。作用対象が単一関与者にしか作用しない場合、厳密な順序付けになる。

17.6.3.12 Strict Sequencing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   The ``interactionOperator`` **strict** designates that the CombinedFragment
   represents a strict sequencing between the behaviors of the operands.

厳密な順序付けの意味は、その CombinedFragment 内の一階の作用対象の狭義順序を
``interactionOperator`` strict で定義する。したがって、CombinedFragment 内の
OccurrenceSpecification は包囲 CombinedFragment の他の OccurrenceSpecifications
と直接比較されることはない。

17.6.3.13 Negative
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   The ``interactionOperator`` **neg** designates that the CombinedFragment represents
   traces that are defined to be invalid.

``interactionOperator`` が否である CombinedFragment を定義した事跡の集合は、その
（ただ一つの）作用対象によって与えられた事跡の集合と等しいが、この集合は有効な事
跡ではなく無効な事跡の集合だ。

   All InteractionFragments that are different from Negative are considered
   positive meaning that they describe traces that are valid and should be
   possible.

17.6.3.14 Critical Region
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   The ``interactionOperator`` **critical** designates that the CombinedFragment
   represents a critical region. A critical region means that the traces of the
   region cannot be interleaved by other OccurrenceSpecifications (on those
   Lifelines covered by the region).

これは有効な事跡の集合を決定する際に、その区域が包囲断片によって不可分的に扱われ
ることを意味する。

   Even though enclosing CombinedFragments may imply that some
   OccurrenceSpecifications may interleave into the region, such as with
   par-operator, this is prevented by defining a region

このように、包囲構成要素の事跡の集合は critical 区域により制限される。

17.6.3.15 Ignore / Consider
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   The ``interactionOperator`` **ignore** designates that there are some message types
   that are not shown within this combined fragment.

これらのメッセージ型は重要でないと考えることが可能で、対応する実行に現れると暗黙
のうちに無視される。あるいは、無視されるメッセージ型は事跡のどこに現れても構わな
いという意味で了解することも可能だ。

   Conversely, the ``interactionOperator`` **consider** designates which
   messages should be considered within this combined fragment. This is
   equivalent to defining every other message to be ignored.

17.6.3.16 Assertion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   The ``interactionOperator`` assert designates that the CombinedFragment
   represents an assertion.

主張の作用対象の列はただ一つの有効な継続だ。それ以外の継続は無効な事跡となる。

主張は多くの場合、Fig. 17.17 に示すように Ignore や Consider と組み合わせる。

17.6.3.17 Loop
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   The ``interactionOperator`` **loop** designates that the CombinedFragment
   represents a loop.

ループ作用対象は反復回数だ。

* ガードには、ループの反復回数の下限と上限、および真偽式を指定してもよい。
* ループは最小で minint 回、最大で maxint 回反復する。ガードの反復式で指定する。
* 最小回数の反復が実行され、論理式が偽の場合、ループは終了する。
* ループ構文は seq 演算子を再帰的に適用したもので、ループ作用対象はそれ以前の反
  復処理の結果の後に列をなす。

..

   If the loop contains a separate InteractionConstraint with a specification,
   the loop will only continue if that specification evaluates to true during
   execution regardless of the minimum number of iterations specified in the
   loop.

17.6.4 Notation
----------------------------------------------------------------------

17.6.4.1 InteractionOperand
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

InteractionOperands は水平な破線で分離される。この InteractionOperands が一緒に
なって枠で囲まれたCombinedFragment を構成する。

Sequence 図の InteractionOperand の内側では InteractionFragments の順序は単にい
ちばん上の垂直位置で与えられる。

17.6.4.2 InteractionConstraint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

InteractionConstraint はその包含 Interaction または InteractionOperand の中にあ
り、最初のイベント発生が起こる生存線を覆う角括弧で示され、そのイベントの上に位置
する。

.. code:: bnf

   <interactionconstraint> ::= ‘[’ (<Boolean-expression> | ‘else’) ‘]’

InteractionConstraint が省略されているときには真が仮定される。

17.6.4.3 CombinedFragment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sequence 図の CombinedFragment の表記は実線の矩形だ。演算子はその矩形の左上隅の
五角形中に示される。

五角形の記述子中に演算子が複数示されてもかまわない。これは入れ子になった
CombinedFragment の速記法だ。つまり、五角形記述子にある sd strict は入れ子になっ
た二つの CombinedFragments と同じであり、いちばん外側が sd で内側が strict だ。

CombinedFragment の作用対象はこの CombinedFragment のグラフ領域を水平線でタイル
貼りし、作用対象に対応する領域群に分割して表示される。

17.6.4.4 ConsiderIgnoreFragment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ConsiderIgnoreFragment の表記は CombinedFragments のすべてと同じで、
**consider** または **ignore** が演算子を示す。そのメッセージの一覧は次の書式に
従って中括弧で囲まれた作用対象に続く：

.. code:: bnf

   (‘ignore’ | ‘consider’) ‘{’ <message-name> [‘,’ <message-name>]* ‘}’

..

   Note that ignore and consider can be combined with other types of operations
   in a single rectangle (as a shorthand for nested rectangles), such as assert
   consider {msgA, msgB}.

17.6.4.5 Continuation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Continuations are shown with the same symbol as States, but they may cover
   more than one Lifeline.

Continuations は Interaction Overview 図の動線上に現れることもある。

InteractionFragment の中で単独で存在する Continuation は、それを包囲する
InteractionFragment の末端にあるとみなされる。

17.6.4.6 InteractionOperatorKind
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

InteractionOperatorKind の値は CombinedFragment 枠の左上隅の小区画でテキストとし
て与えられる。後述する特別な表記法がある。

17.6.4.7 Strict interactionOperator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

記法上は、含まれる断片の垂直座標が、一つの Lifeline 上だけでなく、
CombinedFragment の全範囲において重要であることを意味する。

* OccurrenceSpecification の垂直位置は、対応する点の垂直位置で指定される。
* 他の InteractionFragments の垂直位置は、その外接矩形の最上部の垂直位置で与えら
  れる。

17.6.4.8 Ignore / Consider interactionOperator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

17.6.4.4 節参照。

17.6.4.9 Loop interactionOperator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bnf

   ‘loop’ [ ‘(’ <minint> [‘,’ <maxint> ] ‘)’]

* ``<minint>`` は正の整数。
* ``<maxint>`` は正の整数。``<minint>`` より大きいか等しいか制限なしを意味する
  ``*``.

..

   If only <minint> is present, this means that <minint> = <maxint> = <integer>.

   If only loop, then this means a loop with unlimited upper bound and with 0 as lower bound.

17.6.4.10 Parallel interactionOperator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

適合ツールは単一 Lifeline 内にある "coregion area" の速記法を用いてよい。

この "coregion" とは、並列結合断片を表す略記法であり、ある Lifeline 上のイベント
発生（または他の入れ子になった断片）の順序が重要でない一般的な状況で用いられる。
Fig. 17.23 参照。

17.6.5 Examples
----------------------------------------------------------------------

InteractionOperand の見本については Figure 17.14 を参照。

InteractionConstraints の見本については Figure 17.14, Figure 17.27 を参照。

さまざまな ``interactionOperators`` のある CombinedFragments の見本については
Figure 17.12, 17.13, 17.14 を参照。

   Figure 17.12 Critical Region

演算子 **par** と **critical** の見本。米国における 911 呼び出しの処理が切れ目な
く処理されなければならないことを示している。

   The operator must make sure to forward the 911-call before doing anything
   else. The normal calls, however, can be freely interleaved.

呼び出しの順序を任意に入れ替えていいと言っている。

   Figure 17.13 Loop CombinedFragment

演算子 **loop** の見本。防御付きの方は入れ子になっている。

   Figure 17.14 CombinedFragment

演算子 **alt** の見本。場合分けであることが図からわかればいい。

   Figure 17.15 Continuation

Sequence 図が二つに分割されていて、左側の図中の **ref** 区画が右側の Sequence 図
自体に対応している。

   Figure 17.16 Continuation interpretation

前述の左右の Sequence 図を合体させるとこれと等価になる。

   Figure 17.17 Ignore, ``consider``, ``assert`` with StateInvariants

図の見出しに ``sd M Ignore {t, r}`` とあるので、メッセージタイプが ``t`` および
``r`` のものは無視されている。実システムではこれらのメッセージを処理するだろう
が、この Interaction では関係がないと言っている。

``Y`` にある ``mystate`` は StateInvariant の例。実行時に ``mystate`` の後に
``Y`` で発生するイベントの直前で評価される。

   This may be the reception of q as specified within the assert-fragment, or it
   may be an event that is specified to be insignificant by the filters.

``consider`` 断片に入れ子になっている ``assert`` 断片は、ここでメッセージ ``v``
が発生すると、メッセージ ``q`` が起こることを期待しているという意味だ。``v``,
``w``, ``q`` 以外のメッセージの出現はテストでは無視される。したがって、``v`` の
後に ``w`` が出現するのは無効な事跡だ。

``{Y.p == 15}`` なる StateInvariant は ``Y`` の次の事象発生に先立って評価され
る。

17.7 Interaction Uses
======================================================================

17.7.1 Summary
----------------------------------------------------------------------

本節では次のメタクラスを規定する：

* InteractionUse
* PartDecomposition

17.7.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 17.18 InteractionUses

InteractionUse は InteractionFragment の特殊型。ValueSpecification に二種類の複
合関連、Gate に 複合関連、Interaction に関連がある。

PartDecomposition は InteractionUse の特殊型。Lifeline から参照される。

17.7.3 Semantics
----------------------------------------------------------------------

17.7.3.1 Interaction Uses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

InteractionUse の意味は、参照先 Interaction の意味の事跡の集合であり、その門が解
決され、その引数を置き換える実引数など、すべての一般部分が束縛されている。

実 Gate はその InteractionUse によって参照される Interaction の具体的な発送者と
受領者を設置するための接続点を備えるために、その InteractionUse の外側の境界に取
り付けられることがある。

17.7.3.2 Part Decompositions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Decomposition of a lifeline within one Interaction by an Interaction (owned
   by the type of the Lifeline’s associated ConnectableElement), is interpreted
   exactly as an InteractionUse.

その分解生存線から出入りするメッセージは実 gates として解釈され、その分解上の対
応する形式 gates に合致する。

分解された Lifeline は InteractionUse として解釈されるので、PartDecompositionの
意味は門と引数が合致した分解により参照される Interaction の意味だ。

CombinedFragment が大域外 (extra-global) であるということは、同じ演算子を持つ
CombinedFragment がその Interaction において分解 Lifeline を覆うことだ。そのより
上の階層の CombinedFragment を完全に理解するには、分解作用対象を作用対象ごとに組
み合わせる必要がある。

17.7.4 Notation
----------------------------------------------------------------------

17.7.4.1 InteractionUse
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

InteractionUse は演算子が **ref** と呼ばれる CombinedFragment 記号として示され
る。名前の構文：

.. code:: bnf

   <name> ::=
      [<attribute-name>‘=’]
      [<collaboration-use>‘.’]
      <interaction-name>
      [‘(’<io-argument> [‘,’<io-argument>]* ‘)’]
      [‘:’<return-value>]

   <io-argument> ::= <in-argument> | ‘out’ <out-argument>

``<attribute-name>`` は Interaction 内の生存線の一つの属性を指す。

``<collaboration-use>`` は協力の生存線を束縛する協力使用の識別だ。その場合、相互
作用名はその協力内にある。Fig. 17.24 参照。

``<io-argumnet>`` は多くの場合 IN 引数に対する実引数だ。OUT または INOUT 引数が
あり、出力値を記述する場合は ``out`` に続けて記述することが可能だ。

   The syntax of argument is explained in the notation sub clause of Messages
   17.4.4 (Message).

   If the InteractionUse returns a value, this may be described following a
   colon at the end of the clause.

17.7.4.2 PartDecomposition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PartDecomposition は (17.3.4) で見られるように Lifeline の見出しにある参照する節
により示される。

部品分解が分解された生存線の下にインラインで示されて、分解句が ``strict`` であれ
ば、これはインライン分解内にある部分生存線すべての上にある構成要素が全順序で整列
されることを示す (17.6.4)。

余分な大域 CombinedFragments はその矩形枠が分解 Interaction の境界の外側に出る。

17.7.4.2.1 Style Guidelines
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

分解に関与する Interaction の名前は、分解される Part の型名と、分解の起点となる
Interaction の名前を含めるとよい。Fig 17.21 参照。

17.7.5 Examples
----------------------------------------------------------------------

   Figure 17.19 InteractionUse

左上隅に **ref** のタグの付いた矩形が InteractionUse の見本だ。

``EstablishAccess`` のほうは実引数まで記してある。一方 ``OpenDoor`` のほうは引数
をとらない。

   Figure 17.20 InteractionUse with value return

評価値を返す挙動をモデル化する、より高度な Interaction だ。

* Lifeline ``a_op_b`` がこの Interaction の戻り値。
* Lifeline ``w`` がこの Interaction の入出力引数。
* InteractionUse は ``a_util_b`` という別の生存線を参照している。

  * オブジェクト ``:xx`` の属性 ``xc`` に戻り値 9 を代入することを示す。
  * 入出力引数 ``w`` の出力としての値が 12 であることを示す。

..

   Figure 17.21 PartDecomposition - the decomposed part

右の Lifeline の見出しの二行目に ``ref AC_UserAccess`` と記されている。この一本
に見える Lifeline が実は次に示す sd と等価だ。

   Figure 17.22 PartDecomposition - the decomposition

前述の ``ACSystem`` を分解がこの図だ。この ``AC_UserAccess`` はクラス
``ACSystem`` が 所有する Interaction だ。

``AC_UserAccess`` には ``ACSystem`` を覆う ``UserAccess`` の構成要素に合致する大
域的構成要素がある。

この Interaction の枠をはみ出ている、左上隅に **opt** とあるのが extra-global
CombinedFragment の例だ。この構文は ``UserAccess`` の CombinedFragment に対応す
る。

   However, we want to indicate that the operands of extra global interaction
   groups are combined one-to-one with similar extra global interaction groups
   of other decompositions of the same original CombinedFragment.

``:AccessPoint`` の下に付いている ``p1`` と ``p2`` は ``inner``
ConnectableElements だ。

   Figure 17.23 Sequence Diagrams where two Lifelines refer to the same set of
   Parts (and Internal Structure)

``sd N`` 内の左向きのメッセージを受け取る順序は任意だ。このことを示すのが、角括
弧で挟まれた部分 (coregion) だ。

この coregion 内で成立している条件が StateInvariant ``{x == 2}`` だ。

   Figure 17.24 Describing Collaborations and their binding

クラス ``E`` に記述されている ``A`` と ``B`` は、``W`` によるとそれぞれ
``superA`` と ``superB`` の特殊型だ。二つの匿名部分 ``:A`` と ``:B`` があり、
``W`` の CollaborationUse ``w1`` は ``x``, ``y`` を ``:A`` と ``:B`` にそれぞれ
束する。

Sequence 図 ``P`` では CollaborationUse ``w1`` を介して利用可能になった
Interaction ``Q`` を用いる。

17.8 Sequence Diagrams
======================================================================

Interaction Diagram の種類でもっとも普通のは Sequence Diagram であり、これは数々
の Lifelines の間を交換する Message に重点を置く。

この図式では交換される Messages の連なりと、それに対応する
OccurrenceSpecifications に注目して相互作用を記述する。

   Interactions that are described by Sequence Diagrams form a basis for
   understanding the semantics of the meta classes in the Interactions package.
   Sequence Diagrams are used for the examples in sub clauses for the
   Interaction sub packages.

17.8.1 Sequence Diagram Notation
----------------------------------------------------------------------

17.8.1.1 Graphic Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Table 17.1 に Sequence Diagrams に含めることができる図表要素一覧が示されている。

17.8.1.2 Graphic Paths
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Table 17.2 に節点間に描かれる経路各種の記号一覧が示されている。

* Messages には、伝えるメッセージの種類に依存して変種がある。ここにあるのは、非
  同期メッセージ、呼び出し、応答を示す。これらは完全メッセージ (17.4.4) だ。
* LostMessage は宛先が記述の範囲外である Message のことだ。
* FoundMessage は受信者が知られている Message のことだが、送信方法は本仕様で記述
  されない。

Interactions は Classifier を包含する挙動の単位だ。Interactions はその
Classifier の ConnectableElement 間の Messages による情報の受け渡しを重んじる。

17.8.2 Example Sequence Diagram
----------------------------------------------------------------------

   Figure 17.25 Overview of Metamodel elements of a Sequence Diagram

上の Interaction ``N`` は説明してもらわなくてももう理解できる。

* 図式全体は ``N`` という名前の Interaction だ。
* Lifeline を二つ有する。Gate に近い順から ``s[u]`` と ``s[k]`` という名前だ。
* ラベル ``m3`` の付いた矢印が二本ある。

  * 枠から出ている Message は暗黙の了解で名前 ``m3_1`` を持つ。
  * Lifelines 間の Message は暗黙の了解で名前 ``m3_2`` を持つ。
  * 枠から出ている矢印の始点は形式 Gate で、暗黙の了解で名前は ``in_m3`` だ。
  * 同矢印の終点は OccurrenceSpecification だ。
  * Lifelines 間の矢印の始点、終点も OccurrenceSpecifications だ。

Interaction モデルにとって周辺的なオブジェクトは省いてあると断りがある。例えば
Part ``s`` や Class ``B`` や Message が参照する連結器が省略されている。

17.9 Communication Diagrams
======================================================================

Communication Diagrams は Lifelines 間の相互作用に関心を集中し、内部構造の設計概
念とメッセージの受け渡しとの対応が中心になる。メッセージの配列は連番で示される。

Communication Diagrams は InteractionUses や CombinedFragments のような構造化機
構を用いない簡単な Sequence Diagrams に対応する。また、メッセージの追い越しは起
こらないか、または無関係と仮定される。

17.9.1 Communication Diagram Notation
----------------------------------------------------------------------

17.9.1.1 Graphic Paths
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: 読者ノート

   見出しの文言は編集ミスと思われる。Graphic Nodes が適切だろう。

Table 17.3 では Communication Diagrams の構成要素各種の記法がまとめられている。
と言ってもノードが Frame と Lifeline の二つしかない。

17.9.1.2 Graphic Paths
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Table 17.4 は項目が一つしかない図表だ。Message はラベル付き実線で記される。

17.9.1.3 Sequence expression
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

列式は ``.`` で区切られた列項のリストで、その後に ``:`` が続く。

各項は、全体的な相互作用の中での手続き的入れ子の階層を表す。すべての制御が同時に
行われる場合、入れ子は生じない。各列項は以下の構文を持つ：

.. code:: text

   [ integer | name ] [ recurrence ]

..

   The integer represents the sequential order of the Message within the next
   higher level of procedural calling. Messages that differ in one integer term
   are sequentially related at that level of nesting.

例えば Message ``3.1.4`` は活性化 ``3.1`` 内の Message ``3.1.3`` に続く。

   The name represents a concurrent thread of control. Messages that differ in
   the final name are concurrent at that level of nesting.

例えば Message ``3.1a`` と ``3.1b`` は活性化 ``3.1`` 内で同時進行する（どちらを
先に実施してもよいし、並列に実施してもよい、の意）。制御のスレッドはすべてが入れ
子の深さの中では等しい。

   The recurrence represents conditional or iterative execution. This represents
   zero or more Messages that are executed depending on the conditions involved.

選択肢は：

.. code:: text

   ‘*’ ‘[’ iteration-clause ‘]’an iteration
   ‘[’ guard ‘]’a branch

..

   An iteration represents a sequence of Messages at the given nesting depth.
   The iteration clause may be omitted (in which case the iteration conditions
   are unspecified). The iteration-clause is meant to be expressed in pseudocode
   or an actual programming language, UML does not prescribe its format.

反復句の例としては：``*[i :=1..n]`` などがあるだろう。

   A guard represents a Message whose execution is contingent on the truth of
   the condition clause.

これもまた擬似コードまたは実際のプログラミング言語で表現されることを意図してい
る。例としては ``[x > y]`` など。

   Note that a branch is notated the same as an iteration without a star.

当反復記法はこの反復内の Messages が順次実行されることを仮定している。それらが同
時に実行される可能性もある。この場合の記法は米印の後に二重縦線を引くものだ。

入れ子になった制御構造では、再帰は内部階層では繰り返されない。各階層の構造はそ
れを囲む context 内で独自の反復を指定する。

17.9.2 Example Communication Diagram
----------------------------------------------------------------------

   Figure 17.26 Communication diagram

メッセージ ``m1`` と ``m3`` が ``:r`` から部分 ``s`` のオブジェクト二つに同時に
送られている。

番号は、他のメッセージがどのように配列されているかを示している。

* ``1b`` の次は ``1b.1``
* ``1b.1.1`` の次は ``1b.1.1``
* ``1a`` と ``1b`` の後に ``2``

17.10 Interaction Overview Diagrams
======================================================================

   Interaction Overview Diagrams define Interactions through a variant of
   Activity Diagrams (described in :doc:`Clause 12 <./ch12-packages>`) in a way
   that promotes overview of the control flow.

Interaction Overview Diagrams では、その節点が Interaction または InteractionUse
である制御の流れの概要に関心がある。この概要度では Lifelines と Messages を表示
しない。

17.10.1 Interaction Overview Diagram Notation
----------------------------------------------------------------------

17.10.1.1 Graphic Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Interaction Overview Diagrams are specialization of Activity Diagrams that
   represent Interactions.

Interaction Overview Diagrams は Activity Diagrams と異なる点がある：

* Activity Diagrams の ObjectNodes の代わりに、Interaction Overview Diagrams に
  は（インライン） Interactions か InteractionUses のどちらか一方しかあることが
  不可能だ。

      Inline Interaction diagrams and InteractionUses are considered special
      forms of CallBehaviorAction.

* 代替 CombinedFragments は DecisionNode と対応する MergeNode で表現される。
* 並列 CombinedFragments は ForkNode と対応する JoinNode で表現される。
* ループ CombinedFragments は簡単な輪で表現される。
* Interaction Overview Diagrams では分岐と接合は正しく入れ子になっている必要があ
  る。これは Activity Diagrams よりも制限が厳しい。
* Interaction Overview Diagrams は Interaction Diagrams の他の形式と同じ種類の枠
  で囲まれる。見出しのテキストには含まれる Lifelines の一覧を含めてもよい。

Table 17.5 では Interaction Overview Diagrams のノード三種が表になっている。

* Frame は特筆することはなさそうだ。
* Interaction はどのような種類でも、Activity 呼び出しとしてインラインで表示する
  ことが許される。インライン図式は匿名でも名前ありでもかまわない。
* InteractionUse については：

     The tools may choose to “explode” the view of an InteractionUse into an
     inline Interaction with the name of the Interaction referred by the
     occurrence. The inline Interaction will then replace the occurrence by a
     replica of the definition Interaction where arguments have replaced
     parameters.

..

   Interaction Overview Diagrams use Activity diagram notation where the nodes
   are either Interactions or InteractionUses. Interaction Overview Diagrams are
   a way to describe Interactions where Messages and Lifelines are abstracted
   away.

もっとも純粋な形式では、Activities はすべて InteractionUses であり、Messages も
Lifelines も図式中に全く現れない。

17.10.2 Examples of Interaction Overview Diagrams
----------------------------------------------------------------------

   Figure 17.27 Interaction Overview Diagram representing a High Level
   Interaction diagram

本文で言うように Activity 図の節点系要素が Interaction や InteractionUse に置き
換わっている図式に見える。

これは Fig. 17.19 で示した挙動を別のやり方で記述したもので、時間的拘束をいくつか
加えてある。

#. Interaction ``EstablishAccess("Illegal PIN")`` で起こる。この実引数は固定。
#. インライン Interaction で示されているメッセージ ``CardOut`` で弱い順序付けが
   起こる。
#. 分岐の一つに InteractionConstraint を持つ決定節点を見つけるという選択肢があ
   る。その制御フローに沿って、別のインライン Interaction と InteractionUse を弱
   い順序で見つける。

17.11 Timing Diagrams
======================================================================

   Timing diagrams focus on conditions changing within and among Lifelines along
   a linear time axis.

Timing Diagrams は個々の classifiers と classifiers の相互作用の両方の挙動を記述
するもので、モデル化された Lifelines の条件に変化を生じるイベントの発生時間に注
意する。

17.11.1 Timing Diagram Notation
----------------------------------------------------------------------

17.11.1.1 Graphic Nodes and Paths
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Table 17.6 で Timing 図の記号すべてが表にまとまっている。

Frame はいつも (17.2.4) と同様。

Message (17.4.4) も先ほどの図式と同様。垂直方向に変わっているが意味は同じはず。

MessageLabel はカプセル型記号と矢印で表記する。

   Labels are only notational shorthands used to prevent cluttering of the
   diagrams with a number of messages crisscrossing the diagram between
   Lifelines that are far apart.

State は classifier, 属性の状態、可算値などのテスト可能状態だ。状態次元を連続的
にすることも許される。StateInvariant (17.2.4) の記述を参照。

   This is illustrative for scenarios where certain entities undergo continuous
   state changes, such as temperature or density.

General value lifeline は接続可能な要素の値を時間の関数として示す。値はテキスト
で明示される。交差は、値が変更されたイベントを表す。

Lifeline (17.3.4) はオブジェクトごとに矩形で表現する。

GeneralOrdering (17.5.4) は点線を引いて途中に鏃を置く。

DestructionOccurrenceSpecification (17.4.4) はバツジルシで表す。

17.11.2 Examples of Timing Diagrams
----------------------------------------------------------------------

   Timing diagrams show change in state or other condition of a structural
   element over time. There are a few forms in use.

Interactions の主要な形式としての Sequence Diagrams は時間観測と時機制約を描いて
もよい。Fig. 17.5 も参照。

   Figure 17.28 A Lifeline for a discrete object

Fig. 17.5 の ``:User`` を Timing Diagram で描いたもの。

``:User`` は ``Idle`` と ``WaitCard`` と ``WaitAccess`` の状態を行ったり来たりす
るようで、その時間的推移がこの図から読み取れる。

   The primary purpose of the timing diagram is to show the change in state or
   condition of a lifeline (representing a Classifier Instance or Classifier
   Role) over linear time.

最も一般的な用途は、受理したイベントや刺激に応答して、オブジェクトの状態が時間と
ともに変化する様子を示すことだ。条件や状態の変化の原因となるイベントを示すことが
望ましい場合、受領したイベントは示されたように (``Code``, ``CardOut``, ``OK``)
注釈が付けられる。

   Figure 17.29 Compact Lifeline with States

上述の図の «more economical and compact» 版。

   Figure 17.30 Timing Diagram with more than one Lifeline and with Messages

Lifelines が複数示され、Message も描かれた、より精緻な Timing Diagram の見本だ。

* ``:User`` に加えて ``:ACSystem`` の Lifeline も記述している。
* これは図を読むときに定規が要る気がする。時間軸上の目盛りとグラフが遠い。

17.12 Classifier Descriptions
======================================================================

機械生成による節。

17.13 Association Descriptions
======================================================================

機械生成による節。

.. include:: /_include/uml-refs.txt
