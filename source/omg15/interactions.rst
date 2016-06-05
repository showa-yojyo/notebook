======================================================================
17 Interactions
======================================================================
UML 2.5 pp. 563-636 に関するノート。

.. note::

   * lifeline (n.) 某文書では「生存線」という用語を採用しているようなので
     拝借する。

.. contents:: ノート目次
   :depth: 2

17.1 Summary
======================================================================

17.1.1 Overview
----------------------------------------------------------------------
* Interactions はいくらかの異なる状況で利用される。

  * 相互作用の状況を共通の理解が必要な個人設計者やグループが
    理解するのを達成するために Interactions は用いられる。

  * Interactions はより詳細な設計曲面の間も用いられる。

* 本章では用語 trace を「出来事の連続」(sequence of occurrences) の意で用いる。
  このことは trace-semantics の範囲での普通の用途によく一致し、
  Interactions の意味を記述するのに望ましい方法である。

* Interaction 仕様は許可された traces と却下された traces に
  半順序 (partial ordering) 制約を課す。

  * 半順序とは任意の与えられた system trace において、
    イベント (pl.) が起こることが可能（または不可能）な順序を
    制限するものである。

* Interaction パッケージは Interactions を表現するのに必要となる
  概念を記述するもので、それらの目的に依存する。

  * Timing Diagrams と Interaction Tables はオプション。

* Interactions は
  様々な詳細さの度合いで、
  計算機システム設計の専門家、潜在的なエンドユーザー、
  未来のシステムの利害関係者らにより、
  理解されたり製造されたりし得るシステムを記述するための共通の方法である。

* 典型的には Interactions は設計者または稼動システムにより提示されるときには、
  その場合はその Interactions は完全な物語を語ることはない。

* Interaction の最も明白な特徴 (aspects) は
  生存線 (lifelines) の間にあるメッセージである。
  メッセージ (pl.) の連続が状況の理解に重要であると考えられる。

* 我々は interleaving という言葉を、次の意味を表すものとして用いる。

  ふたつまたはそれ以上の traces を併合することであり、
  異なる traces から来たイベントが結果の trace にどのような順序で現れても
  構わないが、同じ trace 内にあるイベントは元の順序関係を維持するものとする。

17.1.2 Basic trace model
----------------------------------------------------------------------
* :doc:`./common-behavior` では Behaviors の実行の一般的な意味を述べた。
  Interactions とは emergent な振る舞いをモデル化する Behaviors の一種である。

  * この章ではひとつの trace を ``<e1, e2, ..., en>`` のように記すことにする。

* ひとつの Interaction の意味は対 ``[P, I]`` の記法で表現される。
  ここで ``P`` は有効な traces の集合であり、
  ``I`` は無効な traces の集合である。

  * ``P`` と ``I`` の和集合が traces の全集合である必要はない。
  * ふたつの Interactions が等価となるのは、
    両者の trace-sets の対が等しいときである。

17.1.3 Partial ordering constraints on valid and invalid traces
----------------------------------------------------------------------
* 有効な traces の集合は traces にある出来事の発生の半順序によって
  制限されている。無効な traces の集合も同様である。

* 相互作用図において垂直線それぞれが工程の時系列を記述する。
  ここで時間はページの下へ向かって進む。

* ある相互作用における事例らは原則的に互いに独立して作用する。

* 時間は事例軸それぞれの上端から下端へと経過するが、正確な時間尺度は仮定されない。

* 別々の事例の出来事はメッセージを通じて整列されるか、
  または一般化した整列方法を通じて整列される。

  * メッセージはそれが消費されるよりも前にまず送信されなければならない。

  * 推移的かつ反対称的かつ **非反射的** な二項関係は半順序であると呼ばれる。

17.1.4 Interaction Diagram Variants
----------------------------------------------------------------------
* 相互作用図は種々の変種がある。
  それぞれについて別個の節でその記法を定義していく。

  Sequence Diagrams
    これがもっとも普通の変種。
    Message が Lifelines 間を交わすのを焦点に当てる。

  Communication Diagrams
    通信する Lifelines の間にある有向辺を
    引き渡された Messages とそれらの順序の記述で装飾した、
    構築的な view を通じて相互作用を示す。

  Interaction Overview Diagrams
    制御の流れの概観を促進する方法で相互作用を定義する。
    一部 Activity 図と類似した記法要素がある。
    これらの要素の記法と目的は両者で同じではあるが、
    詳細な意味はまったく異なるので、設計者は
    Overview 図を Activity 図であるかのように解釈するべきではない。

  Timing Diagrams
    図の主な目的が時間について思考することであるときに
    相互作用を示すのに用いられる。
    UML 2.5 に準拠するツールは Timing Diagrams を実装する必要はない。

* 本章の扱う変種に加えて、Interaction Tables を用いる
  さらなるオプション記法がある。

17.2 Interactions
======================================================================

17.2.1 Summary
----------------------------------------------------------------------
* 本節では 5 個程度のメタクラスの構文、意味、記法を仕様化する。

17.2.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 17.1 Interactions

  * まず抽象クラス InteractionFragment が NamedElement から特殊化されている。
    そして InteractionFragment から残りの 4 メタクラスが特殊化されている。

  * メタクラス Interaction は InteractionFragment であると同時に
    Behavior でもある。

17.2.3 Semantics
----------------------------------------------------------------------
.. 17.2.3.1 Interactions

* Interactions は enclosing Classifier の振る舞いの構成単位である。

* Interaction の意味は traces の集合の対として与えられる。
  その対のそれぞれは有効な traces と無効な traces を表現する。

* ひとつの trace はイベント発生の連続列のひとつであり、
  そのそれぞれはモデルにある OccurrenceSpecification により記述される。

* 有効な traces の集合は Negative CombinedFragment または
  Assertion CombinedFragment の用途に関連する。

* Behavior としての Interaction は一般化可能かつ再定義可能である。

* Interaction を所有している classifier は特殊化されてもよいし、
  Interaction の特殊化は再定義されてもよい。

* 形式的な Gate は Interaction の内側の境界部に取り付けられ、
  その Interaction の InteractionUse を通して
  具象送信者と受信者を樹立するリンク点を与えてもよい。

.. 17.2.3.2 Interaction Fragments

* InteractionFragment の意味は traces の集合の一対である。
* InteractionFragment は enclosing Interaction に直接含まれるか、
  CombinedFragment の InteractionOperand の内側に含まれるかの
  どちらかであることが許される。

.. 17.2.3.3 Occurrence Specifications

* OccurrenceSpecification の意味は単に単一の OccurrenceSpecification の
  trace である。

* OccurrenceSpecification の理解とより深い意味は
  関連 Message とそれが伝える情報とに依存する。

.. 17.2.3.4 Execution Specifications

* Interactions の trace の意味は
  ``<start, finish>`` とみなした Execution を見るだけである。？？？

.. 17.2.3.5 State Invariants

* Constraint は実行中の間じゅうに評価されると仮定する。

  * Constraint は
    明示的にモデル化されないアクションすべてが実行し終わるように、
    次の OccurrenceSpecification の実行の直前に評価される。

  * Constraint が真ならば、その trace は有効な trace である。
    反対に偽ならば、その trace は無効な trace である。

  * 言い換えると、偽に評価される Constraint のある StateInvariant を持つ
    traces はすべて無効であると判断される。

17.2.4 Notation
----------------------------------------------------------------------
.. 17.2.4.1 Interaction

* Sequence 図における Interaction を表す記法は実線矩形である。

  * 矩形の左上隅に五角形を描き、そこに
    文字列 ``sd`` と Interaction 名と引数をこの順に記す。

* 五角形の記述子の内側の記法は Behaviors の名前を表すのに用いる
  記法一般に従う。

* Interaction 図は局所的な属性の定義を含むことが許される。
  その構文は一般にはクラスシンボル区画で示されるものと同じである。

  * これらの属性が現れることが許されるのは、
    図の枠の上部付近または図のどこかのコメントシンボル内部である。

.. 17.2.4.2 InteractionFragment

* InteractionFragment については一般的な記法がない。
  個々のサブクラスが独自の記法を定義する。

.. 17.2.4.3 OccurrenceSpecification

* OccurrenceSpecifications は単に

  * Messages の両端もしくは
  * ExecutionSpecification の開始・終了

  における構文的な点である。

.. 17.2.4.4 ExecutionSpecification

* ExecutionSpecifications は生存線上の細い（灰色か白色の）矩形として表現される。

* または ExecutionSpecification を幅広のラベル付き矩形により表現してもよく、
  ラベルはたいていは実行されたアクションを識別する。

* ある Signal の属性を読み取るというような不可分なアクション (pl.) を参照する
  ExecutionSpecification の代わりに、
  Action 全体がただひとつの OccurrenceSpecification に関連していることを
  強調する目的で、
  Action シンボルは線の付いた受領 OccurrenceSpecification に関連してもよい。

* Figure 17.2 Overlapping ExecutionSpecifications

  * 同一生存線上で重なりあう ExecutionSpecifications は
    やはり重なりあう矩形で表現される。

.. 17.2.4.5 StateInvariant

* 起こり得る関連 Constraint は生存線上に中括弧に囲まれたテキストで示される。

* 準拠ツールは StateInvariant を
  OccurrenceSpecification に関連した Note として示してもよい。

* 状態シンボルは
  Lifeline により表現されるオブジェクトの状態を調べる制約の等価性を表現する。

* 領域は状態 (pl.) の直交領域を表現する。
  識別子は状態を部分的に定義しさえすればよい。

.. 17.2.4.6 Formal Gate

* 形式的な Gate は枠の内側にある単なる点であり、メッセージの端点である。

17.2.5 Examples
----------------------------------------------------------------------
* Figure 17.3 An example of an Interaction in the form of a Sequence Diagram

  * 矢印がメッセージ。
  * 明らかにメッセージ CardOut と OK が非同期的に見える。
  * 最後のメッセージ Unlock の出口が formal Gate の例である。

* Figure 17.4 OccurrenceSpecification

  * メッセージ msg の矢印の根本が OccurrenceSpecification の例である。
  * 先と同様に矢印の矢先が図枠に至っている点が formal Gate の例である。

* Figure 17.5 Sequence Diagram with time and timing concepts

  * 以前やった時間にまつわる記法が再録されているので復習したい。
    例えば CardOut は 0 から 13 時間単位の間じゅう継続するように拘束されている。

17.3 Lifelines
======================================================================

17.3.1 Summary
----------------------------------------------------------------------
* メタクラス Lifeline の構文法、意味、および表記法を仕様化する。

17.3.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 17.6 Lifelines

  * Lifeline は NamedElement の一種。
  * 継承関係よりも関連のほうが多い。

17.3.3 Semantics
----------------------------------------------------------------------
* 相互作用図において Lifeline はある工程のタイムラインを記述する。
  ここで時間はページの下に向かって進む。

* 同一タイムライン上のイベントはページの下に向かって線形に整列されているが、
  それらが並行に結合した部分 (fragment) の内部で起こる場合、
  すなわちそれらがある coregion 内部にある生存線に沿う場合は除外する。

* Lifeline に沿う OccurrenceSpecifications の順番は
  これらの OccurrenceSpecifications が発生する順番を示している。

* Interaction にある Lifeline の意味とは、
  この Lifeline の OccurrenceSpecifications しか選択しない
  Interaction の意味のことである。

17.3.4 Notation
----------------------------------------------------------------------
.. 17.3.4.1 Lifeline

* Lifeline は「見出し」となる矩形と、
  参加者の生存線を表現する破線スタイルの垂直線とからなるシンボルで示される。

* (pp. 570-571) 矩形の内部に表示される、生存線を識別する情報の書式
  ``<lifelineident>`` は少々ごちゃごちゃしている。

  * この BNF の構文的には空文字列も認められるようだが、ダメである。

* Lifeline の見出しの形状はこの生存線が表現する部品用の
  classifier に基づく。
  見出しは往々にしてその名前を含む白い矩形になる。

* 名前が ``self`` ならば、Lifeline が表現するものは、
  自身を所有する Interaction を囲む classifier のオブジェクトを表現する。

* ExecutionSpecification を描写するには、
  Lifeline の線を覆う薄い灰色か白色の矩形を当てはめる。

17.3.5 Examples
----------------------------------------------------------------------
* Lifelines は先述した Figure 17.3 を参照。
* ExecutionSpecification の記法を参照するには後述する Figure 17.14 を参照。

17.4 Messages
======================================================================
.. todo:: ノート作成

17.4.1 Summary
----------------------------------------------------------------------

17.4.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 17.7 Messages

17.4.3 Semantics
----------------------------------------------------------------------

17.4.4 Notation
----------------------------------------------------------------------
* Figure 17.8 DestructionOccurrenceSpecification symbol

17.4.5 Examples
----------------------------------------------------------------------

17.5 Occurrences
======================================================================
.. todo:: ノート作成

17.5.1 Summary
----------------------------------------------------------------------

17.5.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 17.9 Occurrences

17.5.3 Semantics
----------------------------------------------------------------------

17.5.4 Notation
----------------------------------------------------------------------

17.5.5 Examples
----------------------------------------------------------------------
* Figure 17.10 Example showing GeneralOrdering in a sequence diagram

17.6 Fragments
======================================================================
.. todo:: ノート作成

17.6.1 Summary
----------------------------------------------------------------------

17.6.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 17.11 Fragments

17.6.3 Semantics
----------------------------------------------------------------------

17.6.4 Notation
----------------------------------------------------------------------

17.6.5 Examples
----------------------------------------------------------------------
* Figure 17.12 Critical Region
* Figure 17.13 Loop CombinedFragment
* Figure 17.14 CombinedFragment
* Figure 17.15 Continuation
* Figure 17.16 Continuation interpretation
* Figure 17.17 Ignore, consider, assert with StateInvariants

17.7 Interaction Uses
======================================================================
.. todo:: ノート作成

17.7.1 Summary
----------------------------------------------------------------------

17.7.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 17.18 InteractionUses

17.7.3 Semantics
----------------------------------------------------------------------

17.7.4 Notation
----------------------------------------------------------------------

17.7.5 Examples
----------------------------------------------------------------------
* Figure 17.19 InteractionUse
* Figure 17.20 InteractionUse with value return
* Figure 17.21 PartDecomposition - the decomposed part
* Figure 17.22 PartDecomposition - the decomposition
* Figure 17.23 Sequence Diagrams where two Lifelines refer to (...)
* Figure 17.24 Describing Collaborations and their binding

17.8 Sequence Diagrams
======================================================================
.. todo:: ノート作成

17.8.1 Sequence Diagram Notation
----------------------------------------------------------------------

17.8.2 Example Sequence Diagram
----------------------------------------------------------------------
* Figure 17.25 Overview of Metamodel elements of a Sequence Diagram

17.9 Communication Diagrams
======================================================================
.. todo:: ノート作成

17.9.1 Communication Diagram Notation
----------------------------------------------------------------------

17.9.2 Example Communication Diagram
----------------------------------------------------------------------
* Figure 17.26 Communication diagram

17.10 Interaction Overview Diagrams
======================================================================
.. todo:: ノート作成

17.10.1 Interaction Overview Diagram Notation
----------------------------------------------------------------------

17.10.2 Examples of Interaction Overview Diagrams
----------------------------------------------------------------------
* Figure 17.27 Interaction Overview Diagram representing a High Level Interaction diagram

17.11 Timing Diagrams
======================================================================
.. todo:: ノート作成

17.11.1 Timing Diagram Notation
----------------------------------------------------------------------

17.11.2 Examples of Timing Diagrams
----------------------------------------------------------------------
* Figure 17.28 A Lifeline for a discrete object
* Figure 17.29 Compact Lifeline with States
* Figure 17.30 Timing Diagram with more than one Lifeline and with Messages

17.12 Classifier Descriptions
======================================================================
機械生成による節。

.. 17.12.1 ActionExecutionSpecification [Class]
.. 17.12.2 BehaviorExecutionSpecification [Class]
.. 17.12.3 CombinedFragment [Class]
.. 17.12.4 ConsiderIgnoreFragment [Class]
.. 17.12.5 Continuation [Class]
.. 17.12.6 DestructionOccurrenceSpecification [Class]
.. 17.12.7 ExecutionOccurrenceSpecification [Class]
.. 17.12.8 ExecutionSpecification [Abstract Class]
.. 17.12.9 Gate [Class]
.. 17.12.10 GeneralOrdering [Class]
.. 17.12.11 Interaction [Class]
.. 17.12.12 InteractionConstraint [Class]
.. 17.12.13 InteractionFragment [Abstract Class]
.. 17.12.14 InteractionOperand [Class]
.. 17.12.15 InteractionOperatorKind [Enumeration]
.. 17.12.16 InteractionUse [Class]
.. 17.12.17 Lifeline [Class]
.. 17.12.18 Message [Class]
.. 17.12.19 MessageEnd [Abstract Class]
.. 17.12.20 MessageKind [Enumeration]
.. 17.12.21 MessageOccurrenceSpecification [Class]
.. 17.12.22 MessageSort [Enumeration]
.. 17.12.23 OccurrenceSpecification [Class]
.. 17.12.24 PartDecomposition [Class]
.. 17.12.25 StateInvariant [Class]

17.13 Association Descriptions
======================================================================
機械生成による節。

.. 17.13.1 A_action_actionExecutionSpecification [Association]
.. 17.13.2 A_action_interaction [Association]
.. 17.13.3 A_actualGate_interactionUse [Association]
.. 17.13.4 A_argument_interactionUse [Association]
.. 17.13.5 A_argument_message [Association]
.. 17.13.6 A_before_toAfter [Association]
.. 17.13.7 A_behavior_behaviorExecutionSpecification [Association]
.. 17.13.8 A_cfragmentGate_combinedFragment [Association]
.. 17.13.9 A_connector_message [Association]
.. 17.13.10 A_covered_coveredBy [Association]
.. 17.13.11 A_covered_events [Association]
.. 17.13.12 A_covered_stateInvariant [Association]
.. 17.13.13 A_decomposedAs_lifeline [Association]
.. 17.13.14 A_execution_executionOccurrenceSpecification [Association]
.. 17.13.15 A_finish_executionSpecification [Association]
.. 17.13.16 A_formalGate_interaction [Association]
.. 17.13.17 A_fragment_enclosingInteraction [Association]
.. 17.13.18 A_fragment_enclosingOperand [Association]
.. 17.13.19 A_generalOrdering_interactionFragment [Association]
.. 17.13.20 A_guard_interactionOperand [Association]
.. 17.13.21 A_invariant_stateInvariant [Association]
.. 17.13.22 A_lifeline_interaction [Association]
.. 17.13.23 A_maxint_interactionConstraint [Association]
.. 17.13.24 A_message_considerIgnoreFragment [Association]
.. 17.13.25 A_message_interaction [Association]
.. 17.13.26 A_message_messageEnd [Association]
.. 17.13.27 A_minint_interactionConstraint [Association]
.. 17.13.28 A_operand_combinedFragment [Association]
.. 17.13.29 A_receiveEvent_endMessage [Association]
.. 17.13.30 A_refersTo_interactionUse [Association]
.. 17.13.31 A_represents_lifeline [Association]
.. 17.13.32 A_returnValueRecipient_interactionUse [Association]
.. 17.13.33 A_returnValue_interactionUse [Association]
.. 17.13.34 A_selector_lifeline [Association]
.. 17.13.35 A_sendEvent_endMessage [Association]
.. 17.13.36 A_signature_message [Association]
.. 17.13.37 A_start_executionSpecification [Association]
.. 17.13.38 A_toBefore_after [Association]

.. include:: /_include/uml-refs.txt
