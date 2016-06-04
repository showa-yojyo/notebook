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
.. todo:: ノート作成

17.2.1 Summary
----------------------------------------------------------------------

17.2.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 17.1 Interactions

17.2.3 Semantics
----------------------------------------------------------------------

17.2.4 Notation
----------------------------------------------------------------------
* Figure 17.2 Overlapping ExecutionSpecifications

17.2.5 Examples
----------------------------------------------------------------------
* Figure 17.3 An example of an Interaction in the form of a Sequence Diagram
* Figure 17.4 OccurrenceSpecification
* Figure 17.5 Sequence Diagram with time and timing concepts

17.3 Lifelines
======================================================================
.. todo:: ノート作成

17.3.1 Summary
----------------------------------------------------------------------

17.3.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 17.6 Lifelines

17.3.3 Semantics
----------------------------------------------------------------------

17.3.4 Notation
----------------------------------------------------------------------

17.3.5 Examples
----------------------------------------------------------------------

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
