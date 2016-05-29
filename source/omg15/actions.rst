======================================================================
16 Actions
======================================================================
UML 2.5 pp. 439-562 に関するノート。

.. todo::

   * unmarshal (v.) のスペリングに注意。
     仕様書では最後の l をどんな場合でも重ねるが、
     辞書によると不定詞では l は一個しかない。

   * reduce (v.) 数学とかプログラミングとかでよくある状況での用法での訳。
     論理的に等価な状態のまま、何かを減らす、少なくする、小さくする……。

.. contents:: ノート目次

16.1 Summary
======================================================================
* Action とは UML における振る舞いの仕様の基本的な単位である。
* Actions は Behaviors に、
  特に Activities と Interactions に含まれている。

.. 16.1.1.1 Concrete Syntax

* UML 仕様は Actions をグラフィカルな記法で表すための比較的単純な集合を提供する。

* 具象的な構文は高水準の構成要素を UML の抽象的な構文で仕様化された Actions へと
  写像することが可能である。

* もっとも原始的な Actions は具体的な構文の写像の最大範囲を
  可能にするために定義されている。

.. 16.1.1.2 Execution Engines

* 実行機関 (an execution engine) とは UML Actions を実行する道具のことである。

* モデル作者は、彼らが
  その実行の最適化に関しての特別の知識を持つときに、
  実行機関に対してヒントを与えることが可能である。

* Actions の実行が UML の実行時の振る舞いを制約する構造的意味に違反するときには、
  Actions の意味は未定義のままとする。

16.2 Actions
======================================================================
.. todo:: ノート作成

16.2.1 Summary
----------------------------------------------------------------------
* 本節では Actions および Pins の初歩的な抽象構文について定義する。
* Pins は Actions の入力と出力を指定するのに用いられる。
* OpaqueAction 以外の Actions の諸々の具象型は後続の節で述べる。

16.2.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 16.1 Actions

16.2.3 Semantics
----------------------------------------------------------------------
.. 16.2.3.1 Actions
.. 16.2.3.2 Opaque Actions
.. 16.2.3.3 Pins
.. 16.2.3.4 Actions and Pins in Activities


16.2.4 Notation
----------------------------------------------------------------------
* Figure 16.2 Action
* Figure 16.3 Local pre- and post-conditions
* Figure 16.4 Pin notations
* Figure 16.5 Pin notations, with arrows
* Figure 16.6 Standalone Pin notations

16.2.5 Examples
----------------------------------------------------------------------
* Figure 16.7 Examples of Actions
* Figure 16.8 Example of action using a tool-specific concrete syntax
* Figure 16.9 Example of an action with local pre- and post-conditions
* Figure 16.10 Pin examples
* Figure 16.11 Specifying selection behavior on an ObjectFlow
* Figure 16.12 Example abstract syntax model showing the use of ActionInputPins

16.3 Invocation Actions
======================================================================
.. todo:: ノート作成

16.3.1 Summary
----------------------------------------------------------------------
* InvocationAction は直接的または間接的にある Behavior の発動に帰着する
  Action である。

* InvocationActions である CallActions には、

  * Operations や Behaviors を呼び出したり、
  * 以前オブジェクト化された Behaviors を開始したりするものがある。

* さらなる InvocationActions の種類には次を考慮したものがある。

  * 信号とその他のオブジェクトの狙いを付けた送信
  * 利用可能な受信者に向けて信号を一斉送信する能力

16.3.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 16.13 Invocation Actions

16.3.3 Semantics
----------------------------------------------------------------------
.. 16.3.3.1 Call Actions
.. 16.3.3.2 Send Actions
.. 16.3.3.3 Invocation Actions and Ports

16.3.4 Notation
----------------------------------------------------------------------
* Figure 16.14 Calling a Behavior
* Figure 16.15 Calling an Activity
* Figure 16.16 Calling an Operation
* Figure 16.17 Calling an Operation, showing the owner name
* Figure 16.18 Sending a Signal
* Figure 16.19 Exception Pin annotations
* Figure 16.20 Effect Pin annotations
* Figure 16.21 Stream Pin annotations
* Figure 16.22 Stream Pin annotations, with filled arrows and rectangles
* Figure 16.23 Alternative input/outputs using ParameterSet notation

16.3.5 Examples
----------------------------------------------------------------------
* Figure 16.24 Invoking an Activity
* Figure 16.25 Sending Signals
* Figure 16.26 Streaming Pin examples
* Figure 16.27 Exception Pin examples
* Figure 16.28 Pin example with effects
* Figure 16.29 Alternative input/outputs using ParameterSets

16.4 Object Actions
======================================================================
.. todo:: ノート作成

16.4.1 Summary
----------------------------------------------------------------------
* オブジェクト Actions は Classifiers のオブジェクトの
  生成、破壊、比較を取り扱う。

* 与えられた Classifier のオブジェクトの読み取りや、
  あるオブジェクトの分類の確認、
  さらに分類の変更をする Actions をも含む。

16.4.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 16.30 Object Actions

16.4.3 Semantics
----------------------------------------------------------------------
.. 16.4.3.1 Create Object Actions
.. 16.4.3.2 Destroy Object Actions
.. 16.4.3.3 Test Identity Actions
.. 16.4.3.4 Read Self Actions
.. 16.4.3.5 Value Specification Actions
.. 16.4.3.6 Read Extent Actions
.. 16.4.3.7 Reclassify Object Actions
.. 16.4.3.8 Read-Is-Classified-Object Actions
.. 16.4.3.9 Start Classifier Behavior Actions

16.4.4 Notation
----------------------------------------------------------------------
* Figure 16.31 ValueSpecificationAction notation

16.4.5 Examples
----------------------------------------------------------------------
* Figure 16.32 ValueSpecificationActions

16.5 Link End Data
======================================================================
.. todo:: ノート作成

16.5.1 Summary
----------------------------------------------------------------------
* リンクオブジェクトではないリンク、
  つまり AssociationClass のオブジェクトではない Association のオブジェクトは、
  Action に対して実行時の値を引き渡すことが不可能である。

* その代わり、リンクはその関連端の値により識別する。
  LinkEndData とはそういうリンクの（片側の）関連端の値の仕様であり、
  LinkActions で用いられるリンクの識別に用いられる。

16.5.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 16.33 Link End Data

16.5.3 Semantics
----------------------------------------------------------------------
.. 16.5.3.1 Link End Data
.. 16.5.3.2 Link End Creation Data
.. 16.5.3.3 Link End Destruction Data

16.5.4 Notation
----------------------------------------------------------------------

16.5.5 Examples
----------------------------------------------------------------------

16.6 Link Actions
======================================================================
.. todo:: ノート作成

16.6.1 Summary
----------------------------------------------------------------------
* LinkActions と ClearAssociationAction は
  Associations とそれらのオブジェクト（リンク）に作用する。

16.6.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 16.34 Link Actions

16.6.3 Semantics
----------------------------------------------------------------------
.. 16.6.3.1 Link Actions
.. 16.6.3.2 Read Link Actions
.. 16.6.3.3 Create Link Action
.. 16.6.3.4 Destroy Link Actions
.. 16.6.3.5 Clear Association Actions

16.6.4 Notation
----------------------------------------------------------------------

16.6.5 Examples
----------------------------------------------------------------------

16.7 Link Object Actions
======================================================================
.. todo:: ノート作成

16.7.1 Summary
----------------------------------------------------------------------
* リンクオブジェクト Actions はリンクオブジェクトに作用する、
  AssociationClasses のオブジェクトである。

* LinkActions もまたリンクオブジェクトに作用するが、
  それらを違うように見分ける。

16.7.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 16.35 Link Object Actions

16.7.3 Semantics
----------------------------------------------------------------------
.. 16.7.3.1 Read Link Object End Actions
.. 16.7.3.2 Read Link Object End Qualifier Actions
.. 16.7.3.3 Create Link Object Actions

16.7.4 Notation
----------------------------------------------------------------------

16.7.5 Examples
----------------------------------------------------------------------

16.8 Structural Feature Actions
======================================================================
.. todo:: ノート作成

16.8.1 Summary
----------------------------------------------------------------------
* StructuralFeatureActions は StructuralFeatures の読み書きを支援する。

16.8.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 16.36 Structural Feature Actions

16.8.3 Semantics
----------------------------------------------------------------------
.. 16.8.3.1 Structural Feature Actions
.. 16.8.3.2 Read Structural Feature Actions
.. 16.8.3.3 Add Structural Feature Value Actions
.. 16.8.3.4 Remove Structural Feature Value Actions
.. 16.8.3.5 Clear Structural Feature Actions

16.8.4 Notation
----------------------------------------------------------------------

16.8.5 Examples
----------------------------------------------------------------------

16.9 Variable Actions
======================================================================
.. todo:: ノート作成

16.9.1 Summary
----------------------------------------------------------------------
* VariableActions は Variables の読み書きを支援する。

16.9.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 16.37 Variable Actions

16.9.3 Semantics
----------------------------------------------------------------------
.. 16.9.3.1 Variable Action
.. 16.9.3.2 Read Variable Actions
.. 16.9.3.3 Add Variable Value Action
.. 16.9.3.4 Remove Variable Value Actions
.. 16.9.3.5 Clear Variable Actions

16.9.4 Notation
----------------------------------------------------------------------
* Figure 16.38 Presentation option for AddVariableValueAction

16.9.5 Examples
----------------------------------------------------------------------

16.10 Accept Event Actions
======================================================================
.. todo:: ノート作成

16.10.1 Summary
----------------------------------------------------------------------
* AcceptEventAction はひとつ以上の Events の出来事を待機する。
* もし受理した Event の出来事がある CallEvent を要求するものならば、
  ひとつの ReplyAction をそれに返信するのに用いてよい。
* もし受理した Event の出来事がある SignalEvent を要求するものならば、
  受信した Signal オブジェクトは、

  * 直ちにその属性の値へと unmarshal されるか、
  * 後になって UnmarshallAction を用いてそうされるかの一方であってよい。

16.10.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 16.39 Accept Event Actions

16.10.3 Semantics
----------------------------------------------------------------------
.. 16.10.3.1 Accept Event Action
.. 16.10.3.2 Accept Call Actions
.. 16.10.3.3 Reply Actions
.. 16.10.3.4 Unmarshall Actions

16.10.4 Notation
----------------------------------------------------------------------
* Figure 16.40 AcceptEventAction notations

16.10.5 Examples
----------------------------------------------------------------------
* Figure 16.41 Implicitly enabled AcceptEventAction
* Figure 16.42 Explicitly enabled AcceptEventAction
* Figure 16.43 Repetitive time event
* Figure 16.44 UnmarshallAction

16.11 Structured Actions
======================================================================
.. todo:: ノート作成

16.11.1 Summary
----------------------------------------------------------------------
* StructuredActivityNode は ActivityGroup でもある Action である。
  つまり、その実行時の振る舞いを定義する ActivityNodes と ActivityEdges を含む。

* StructuredActivityNodes の特殊型、名前を挙げると
  ConditionalNodes, LoopNodes, SequenceNodes らは、
  それらの中にある ExecutableNodes がどのように実行されるのかという、
  それぞれの型固有の制御意味を定義する。

16.11.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 16.45 Structured Actions

16.11.3 Semantics
----------------------------------------------------------------------
.. 16.11.3.1 Structured Activity Nodes
.. 16.11.3.2 Isolation
.. 16.11.3.3 Conditional Nodes
.. 16.11.3.4 Loop Nodes
.. 16.11.3.5 Sequence Nodes

16.11.4 Notation
----------------------------------------------------------------------
* Figure 16.46 Notation for StructuredActivityNode

16.11.5 Examples
----------------------------------------------------------------------

16.12 Expansion Regions
======================================================================
.. todo:: ノート作成

16.12.1 Summary
----------------------------------------------------------------------
* ExpansionRegion は入力コレクションの要素に対応している、
  それが含む要素を複数回実行する StructuredActivityNode である。

16.12.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 16.47 Expansion Regions

16.12.3 Semantics
----------------------------------------------------------------------

16.12.4 Notation
----------------------------------------------------------------------
* Figure 16.48 Expansion Region
* Figure 16.49 Shorthand notation for expansion region containing single node
* Figure 16.50 Full form of previous shorthand notation
* Figure 16.51 Notation for expansion region with one behavior invocation

16.12.5 Examples
----------------------------------------------------------------------
* Figure 16.52 Expansion region with two inputs and one output
* Figure 16.53 Expansion Region
* Figure 16.54 Examples of expansion region shorthand
* Figure 16.55 Shorthand notation for expansion region

16.13 Other Actions
======================================================================
.. todo:: ノート作成

16.13.1 Summary
----------------------------------------------------------------------
* 本節では ReduceAction と RaiseExceptionAction を扱う。
* ReduceAction とはあるコレクションの値らを単一の値にまで reduce するために
  ひとつの Behavior を繰り返し発動する Action である。
* RaiseExceptionAction は例外を送出するための Action である。

16.13.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 16.56 Other Actions

16.13.3 Semantics
----------------------------------------------------------------------
.. 16.13.3.1 Reduce Actions
.. 16.13.3.2 Raise Exception Actions

16.13.4 Notation
----------------------------------------------------------------------

16.13.5 Examples
----------------------------------------------------------------------

16.14 Classifier Descriptions
======================================================================
機械生成による節。

.. 16.14.1 AcceptCallAction [Class]
.. 16.14.2 AcceptEventAction [Class]
.. 16.14.3 Action [Abstract Class]
.. 16.14.4 ActionInputPin [Class]
.. 16.14.5 AddStructuralFeatureValueAction [Class]
.. 16.14.6 AddVariableValueAction [Class]
.. 16.14.7 BroadcastSignalAction [Class]
.. 16.14.8 CallAction [Abstract Class]
.. 16.14.9 CallBehaviorAction [Class]
.. 16.14.10 CallOperationAction [Class]
.. 16.14.11 Clause [Class]
.. 16.14.12 ClearAssociationAction [Class]
.. 16.14.13 ClearStructuralFeatureAction [Class]
.. 16.14.14 ClearVariableAction [Class]
.. 16.14.15 ConditionalNode [Class]
.. 16.14.16 CreateLinkAction [Class]
.. 16.14.17 CreateLinkObjectAction [Class]
.. 16.14.18 CreateObjectAction [Class]
.. 16.14.19 DestroyLinkAction [Class]
.. 16.14.20 DestroyObjectAction [Class]
.. 16.14.21 ExpansionKind [Enumeration]
.. 16.14.22 ExpansionNode [Class]
.. 16.14.23 ExpansionRegion [Class]
.. 16.14.24 InputPin [Class]
.. 16.14.25 InvocationAction [Abstract Class]
.. 16.14.26 LinkAction [Abstract Class]
.. 16.14.27 LinkEndCreationData [Class]
.. 16.14.28 LinkEndData [Class]
.. 16.14.29 LinkEndDestructionData [Class]
.. 16.14.30 LoopNode [Class]
.. 16.14.31 OpaqueAction [Class]
.. 16.14.32 OutputPin [Class]
.. 16.14.33 Pin [Abstract Class]
.. 16.14.34 QualifierValue [Class]
.. 16.14.35 RaiseExceptionAction [Class]
.. 16.14.36 ReadExtentAction [Class]
.. 16.14.37 ReadIsClassifiedObjectAction [Class]
.. 16.14.38 ReadLinkAction [Class]
.. 16.14.39 ReadLinkObjectEndAction [Class]
.. 16.14.40 ReadLinkObjectEndQualifierAction [Class]
.. 16.14.41 ReadSelfAction [Class]
.. 16.14.42 ReadStructuralFeatureAction [Class]
.. 16.14.43 ReadVariableAction [Class]
.. 16.14.44 ReclassifyObjectAction [Class]
.. 16.14.45 ReduceAction [Class]
.. 16.14.46 RemoveStructuralFeatureValueAction [Class]
.. 16.14.47 RemoveVariableValueAction [Class]
.. 16.14.48 ReplyAction [Class]
.. 16.14.49 SendObjectAction [Class]
.. 16.14.50 SendSignalAction [Class]
.. 16.14.51 SequenceNode [Class]
.. 16.14.52 StartClassifierBehaviorAction [Class]
.. 16.14.53 StartObjectBehaviorAction [Class]
.. 16.14.54 StructuralFeatureAction [Abstract Class]
.. 16.14.55 StructuredActivityNode [Class]
.. 16.14.56 TestIdentityAction [Class]
.. 16.14.57 UnmarshallAction [Class]
.. 16.14.58 ValuePin [Class]
.. 16.14.59 ValueSpecificationAction [Class]
.. 16.14.60 VariableAction [Abstract Class]
.. 16.14.61 WriteLinkAction [Abstract Class]
.. 16.14.62 WriteStructuralFeatureAction [Abstract Class]
.. 16.14.63 WriteVariableAction [Abstract Class]

16.15 Association Descriptions
======================================================================
機械生成による節。

.. 16.15.1 A_argument_invocationAction [Association]
.. 16.15.2 A_association_clearAssociationAction [Association]
.. 16.15.3 A_behavior_callBehaviorAction [Association]
.. 16.15.4 A_bodyOutput_clause [Association]
.. 16.15.5 A_bodyOutput_loopNode [Association]
.. 16.15.6 A_bodyPart_loopNode [Association]
.. 16.15.7 A_body_clause [Association]
.. 16.15.8 A_classifier_createObjectAction [Association]
.. 16.15.9 A_classifier_readExtentAction [Association]
.. 16.15.10 A_classifier_readIsClassifiedObjectAction [Association]
.. 16.15.11 A_clause_conditionalNode [Association]
.. 16.15.12 A_collection_reduceAction [Association]
.. 16.15.13 A_context_action [Association]
.. 16.15.14 A_decider_clause [Association]
.. 16.15.15 A_decider_loopNode [Association]
.. 16.15.16 A_destroyAt_linkEndDestructionData [Association]
.. 16.15.17 A_edge_inStructuredNode [Association]
.. 16.15.18 A_endData_createLinkAction [Association]
.. 16.15.19 A_endData_destroyLinkAction [Association]
.. 16.15.20 A_endData_linkAction [Association]
.. 16.15.21 A_end_linkEndData [Association]
.. 16.15.22 A_end_readLinkObjectEndAction [Association]
.. 16.15.23 A_exception_raiseExceptionAction [Association]
.. 16.15.24 A_executableNode_sequenceNode [Association]
.. 16.15.25 A_first_testIdentityAction [Association]
.. 16.15.26 A_fromAction_actionInputPin [Association]
.. 16.15.27 A_inputElement_regionAsInput [Association]
.. 16.15.28 A_inputValue_linkAction [Association]
.. 16.15.29 A_inputValue_opaqueAction [Association]
.. 16.15.30 A_input_action [Association]
.. 16.15.31 A_insertAt_addStructuralFeatureValueAction [Association]
.. 16.15.32 A_insertAt_addVariableValueAction [Association]
.. 16.15.33 A_insertAt_linkEndCreationData [Association]
.. 16.15.34 A_localPostcondition_action [Association]
.. 16.15.35 A_localPrecondition_action [Association]
.. 16.15.36 A_loopVariableInput_loopNode [Association]
.. 16.15.37 A_loopVariable_loopNode [Association]
.. 16.15.38 A_newClassifier_reclassifyObjectAction [Association]
.. 16.15.39 A_node_inStructuredNode [Association]
.. 16.15.40 A_object_clearAssociationAction [Association]
.. 16.15.41 A_object_readIsClassifiedObjectAction [Association]
.. 16.15.42 A_object_readLinkObjectEndAction [Association]
.. 16.15.43 A_object_readLinkObjectEndQualifierAction [Association]
.. 16.15.44 A_object_reclassifyObjectAction [Association]
.. 16.15.45 A_object_startClassifierBehaviorAction [Association]
.. 16.15.46 A_object_startObjectBehaviorAction [Association]
.. 16.15.47 A_object_structuralFeatureAction [Association]
.. 16.15.48 A_object_unmarshallAction [Association]
.. 16.15.49 A_oldClassifier_reclassifyObjectAction [Association]
.. 16.15.50 A_onPort_invocationAction [Association]
.. 16.15.51 A_operation_callOperationAction [Association]
.. 16.15.52 A_outputElement_regionAsOutput [Association]
.. 16.15.53 A_outputValue_opaqueAction [Association]
.. 16.15.54 A_output_action [Association]
.. 16.15.55 A_predecessorClause_successorClause [Association]
.. 16.15.56 A_qualifier_linkEndData [Association]
.. 16.15.57 A_qualifier_qualifierValue [Association]
.. 16.15.58 A_qualifier_readLinkObjectEndQualifierAction [Association]
.. 16.15.59 A_reducer_reduceAction [Association]
.. 16.15.60 A_removeAt_removeStructuralFeatureValueAction [Association]
.. 16.15.61 A_removeAt_removeVariableValueAction [Association]
.. 16.15.62 A_replyToCall_replyAction [Association]
.. 16.15.63 A_replyValue_replyAction [Association]
.. 16.15.64 A_request_sendObjectAction [Association]
.. 16.15.65 A_result_acceptEventAction [Association]
.. 16.15.66 A_result_callAction [Association]
.. 16.15.67 A_result_clearStructuralFeatureAction [Association]
.. 16.15.68 A_result_conditionalNode [Association]
.. 16.15.69 A_result_createLinkObjectAction [Association]
.. 16.15.70 A_result_createObjectAction [Association]
.. 16.15.71 A_result_loopNode [Association]
.. 16.15.72 A_result_readExtentAction [Association]
.. 16.15.73 A_result_readIsClassifiedObjectAction [Association]
.. 16.15.74 A_result_readLinkAction [Association]
.. 16.15.75 A_result_readLinkObjectEndAction [Association]
.. 16.15.76 A_result_readLinkObjectEndQualifierAction [Association]
.. 16.15.77 A_result_readSelfAction [Association]
.. 16.15.78 A_result_readStructuralFeatureAction [Association]
.. 16.15.79 A_result_readVariableAction [Association]
.. 16.15.80 A_result_reduceAction [Association]
.. 16.15.81 A_result_testIdentityAction [Association]
.. 16.15.82 A_result_unmarshallAction [Association]
.. 16.15.83 A_result_valueSpecificationAction [Association]
.. 16.15.84 A_result_writeStructuralFeatureAction [Association]
.. 16.15.85 A_returnInformation_acceptCallAction [Association]
.. 16.15.86 A_returnInformation_replyAction [Association]
.. 16.15.87 A_second_testIdentityAction [Association]
.. 16.15.88 A_setupPart_loopNode [Association]
.. 16.15.89 A_signal_broadcastSignalAction [Association]
.. 16.15.90 A_signal_sendSignalAction [Association]
.. 16.15.91 A_structuralFeature_structuralFeatureAction [Association]
.. 16.15.92 A_structuredNodeInput_structuredActivityNode [Association]
.. 16.15.93 A_structuredNodeOutput_structuredActivityNode [Association]
.. 16.15.94 A_target_callOperationAction [Association]
.. 16.15.95 A_target_destroyObjectAction [Association]
.. 16.15.96 A_target_sendObjectAction [Association]
.. 16.15.97 A_target_sendSignalAction [Association]
.. 16.15.98 A_test_clause [Association]
.. 16.15.99 A_test_loopNode [Association]
.. 16.15.100 A_trigger_acceptEventAction [Association]
.. 16.15.101 A_unmarshallType_unmarshallAction [Association]
.. 16.15.102 A_value_linkEndData [Association]
.. 16.15.103 A_value_qualifierValue [Association]
.. 16.15.104 A_value_valuePin [Association]
.. 16.15.105 A_value_valueSpecificationAction [Association]
.. 16.15.106 A_value_writeStructuralFeatureAction [Association]
.. 16.15.107 A_value_writeVariableAction [Association]
.. 16.15.108 A_variable_scope [Association]
.. 16.15.109 A_variable_variableAction [Association]

.. include:: /_include/uml-refs.txt
