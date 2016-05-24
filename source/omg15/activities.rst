======================================================================
15 Activities
======================================================================
UML 2.5 pp. 371-438 に関するノート。

.. todo::

   訳語検討。

   * activity (n.)
   * flow (n.) 「流れ」で済ませたい。

.. contents:: ノート目次

15.1 Summary
======================================================================
* Activity とは ノードとエッジのグラフとして指定される Behavior の一種である。

  * ノードの部分集合は実行可能ノード (executable nodes) である。
  * オブジェクトノード (object nodes) は

    #. 実行可能ノードの入出力するデータを保持し、
    #. オブジェクトフロー (object flow) エッジを横断する。

  * 制御ノード (control nodes) は制御フロー (control flow) エッジを経て、
    実行可能ノードの配列を指定する。

* Activities は手続きの計算を記述することも許される。

  #. 他の Activities を発動する Activities の階層を形成するものか、
  #. 直接的に発動される Operations に束縛したメソッドとして
     間接的に発動されることも許される。

* Activities は
  business process engineering と workflow のための
  組織的モデリングにも適用されることが認められている。

15.2 Activities
======================================================================

15.2.1 Summary
----------------------------------------------------------------------
* Activity は下位ユニットの配列として指定される Behavior である。

  * 実行の流れは ActivityNodes と ActivityEdges とがモデル化する。
  * ExecutableNode は下位の振る舞い（算術計算のような）の実行であることがある。

* この節はノードとエッジのグラフとしての activity model の
  根本的な構造および流れの意味を述べる。
  後続の小節では ActivityNodes 各種を述べる。

15.2.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 15.1 Activities

  * Activity, ActivityNode, ActivityEdge, ObjectFlow, ControlFlow 周りを見ていく。
  * Flow とは Edge の一種らしい。

15.2.3 Semantics
----------------------------------------------------------------------
.. todo:: ノート作成
.. 15.2.3.1 Activities
.. 15.2.3.2 Activity Nodes
.. 15.2.3.3 Activity Edges
.. 15.2.3.4 Object Flows
.. 15.2.3.5 Variables
.. 15.2.3.6 Activity Execution
.. 15.2.3.7 Activity Generalization

15.2.4 Notation
----------------------------------------------------------------------
* Activity の記法は、それが含む ActivityNodes と ActivityEdges の
  記法の組み合わせたものに、枠を加えて名前を左上に表示するものとする。

* ActivityParameterNodes は Activity の枠上に表示する。
* Behavior から継承した事前条件と事後条件は、
  キーワード ``«precondition»``, ``«postcondition»``
  と共にテキストとしてそれぞれ示される。

* isSingleExecution が真である Activities にはキーワード ``«singleExecution»`` を用いる。

* Figure 15.2 Activity notation

  * 丸角は Annex A で述べられた枠記法で置き換えてよろしい。
  * 丸角にせよ枠にせよ完全に省略してよろしい。
    その場合には ActivityParameterNodes は図式内のどのような箇所に現れても構わない。

* Figure 15.3 Activity class notation

  * Activity の機能群を図表化するのに Class 記法を利用することもある。
  * キーワードは ``«activity»`` である。

* Figure 15.4 ActivityNode notation

  * ActivityNodes 各種の記法のカタログ。次の節で詳しく議論する。

* Figure 15.5 ActivityEdge notation

  * ActivityEdges 各種の記法のカタログ。
  * 矢先はすべて開いた形状を用いる。
  * イラストにはないが guards を記すには角括弧を用いる。

* Figure 15.6 ActivityEdge connector notation

  * この記法はまともに描くと矢印が長くなるときに採用すればよい。

* Figure 15.7 ActivityEdge notation

  * エッジの weight は中括弧と ValueSpecification の記法を用いる。
  * InterruptibleActivityRegion の interruptingEdge は稲妻型の矢印とする。

* Figure 15.8 ControlFlow notation

  * 制御フローはふたつのアクションを接続する矢印として示す。

* Figure 15.9 ObjectFlow notations

  * オブジェクトフローも矢印として示す。
  * Pins を用いる記法のほうがよい？

* Figure 15.10 Specifying selection behavior on an ObjectFlow

  * selection Behavior の記法にはキーワード ``«selection»`` とコメントを用いる。
  * transformation Behavior も同様にする。キーワードは ``«transformation»`` とする。

* Figure 15.11 Eliding objects flowing on the edge

  * 図式が散らかるのを緩和するために、Pins はある程度省略してよろしい。
    省略されていることをわからせるために、
    矢印の少し上あたりに小さい四角を表示する。

15.2.5 Examples
----------------------------------------------------------------------
* Figure 15.12 Activity node example (...)

  * 代表的な ActivityNodes の記法の見本となる。

* Figure 15.13 ActivityEdge examples

  * 右上。ObjectNode の前後にある矢印は両方 ObjectFlow である。
    Invoice オブジェクトの移動を暗示する。

* Figure 15.14 ObjectFlow example

  * 両者の意味は同じ。オブジェクト Order の移動を暗示している。

* Figure 15.15 Eliding objects flowing on the edge

  * 省略版だとオブジェクトの個数に関わらず小さい四角がひとつになる？

* Figure 15.16 Specifying selection and transformation Behaviors on an ObjectFlow

  * selection および transformation Behaviors の見本。コメント頼み。

* Figure 15.17 Linking a class diagram to an object node

  * アクティビティ図内の ObjectNode Order と、
    Class Order を述べるクラス図とのリンクを表現している。

* Figure 15.18 Specifying multicast and multireceive on the edge

  * キーワード ``«multicast»`` と ``«multireceive»`` の見本。
  * スイムレーンは送信者と受信者を示す重要な機能である。

* Figure 15.19 ActivityEdge connector example

  * 図式中の fork と merge の間にまともに矢印を描くのは面倒なので、
    このようなワープのような記法の支援がある。

* Figure 15.20 Equivalent model

  * ワープ記法不採用版。

* Figure 15.21 ActivityEdge weight examples

  * 左上。constant weight を要求する例。
  * 右上。変数版。
  * 下。Award Bid に遷移する条件？が weight だけから決定しない例。
    この凹五角形ノードの記法の意味はまだやっていない？

* Figure 15.22 Example of an activity with input parameter

  * Requested Order とあるのが入力引数に対応する ActivityParameterNode である。

* Figure 15.23 Part selection workflow example

  * Design Part におけるノード Provide Required Part が、
    下側では Activity として図解化されている。

* Figure 15.24 Trouble ticket workflow example

  * よくあるチケット管理の Activity だろう。

* Figure 15.25 Activity with attributes and operations

  * Activity を Class の記法で示す見本。

15.3 Control Nodes
======================================================================

15.3.1 Summary
----------------------------------------------------------------------

15.3.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 15.26 Control Nodes

  * ControlNode は ActivityNode から派生した型で、
    ControlNode からもかなりの数のクラスが派生している。

15.3.3 Semantics
----------------------------------------------------------------------
.. todo:: ノート作成

15.3.4 Notation
----------------------------------------------------------------------
* Figure 15.27 InitialNode notation

  * 既視感のある黒丸シンボル。

* Figure 15.28 FinalNode notation

  * ActivityFinal は黒丸を丸で囲むシンボル。
  * FlowFinalNode はマルバツシンボル。

* Figure 15.29 ForkNode and JoinNode notation

  * 両者とも太めの線分として記すが、向きは任意でよいらしい。
  * この線分に outgoing/incoming ActivityEdges のシンボルを必要に応じて接続する。

* Figure 15.30 joinSpec notation

  * 位置は線分の付近。
  * 中括弧に ``joinSpec = ...`` を含める。

* Figure 15.31 Combined JoinNode/ ForkNode notation

  * JoinNode と ForkNode が隣接？している状況では、両者を癒着できる。

* Figure 15.32 MergeNode notation

  * MergeNode 自体は白ダイヤモンドシンボルで表す。
  * ふたつ以上の incoming ActivityEdges および
    ひとつの outgoing ActivityEdge を持つ必要がある。

* Figure 15.33 DecisionNode notation

  * DecisionNode 自体は白ダイヤモンドシンボルで表す。
  * ひとつの incoming ActivityEdge および
    ふたつ以上の outgoing ActivityEdges を持つ必要がある。
  * decisionInput はキーワード ``«decisionInput»`` と共にコメントの記法で示す。
  * decisionInputFlow はキーワード ``«decisionInputFlow»`` をその矢印のそばに添える。

* Figure 15.34 Combined MergeNode/DecisionNode notation

  * MergeNode と DecisionNode はシンボルを共有することがある。
  * incoming/outgoing ActivityEdges シンボルを複数示すことになる。

15.3.5 Examples
----------------------------------------------------------------------
* Figure 15.35 InitialNode example

  * InitialNode から無条件で Receive Order ノードに至る。

* Figure 15.36 ForkNode example

  * Fill Order が完了したときに、ShipOrder と SendInvoice の
    両方に制御を引き渡す。

* Figure 15.37 JoinNode example

  * ShipOrder と SendInvoice の両方が完了したときに（同期）、
    Close Order に制御を引き渡す。

* Figure 15.38 joinSpec example

  * 自動販売機の制御が Dispense Drink に引き渡されるには、
    この joinSpec にある条件が満たされる必要がある。

* Figure 15.39 MergeNode example

  * 要注意。場合によっては Ship Item が二度実行される。

* Figure 15.40 DecisionNode example

  * 角括弧を用いることで分岐条件を柔軟に表現できる。

* Figure 15.41 DecisionNode example with decisionInput

  * decisionInput のコメントに分岐条件を書き下している。

* Figure 15.42 ActivityFinalNode example

  * Close Order 完了時に無条件で FinalNode に至る。

* Figure 15.43 ActivityFinalNode example

  * 開始直後の ForkNode でふたつの concurrent flows が始まる。
  * とにかくどちらの流れを経ても FinalNode に至る。

* Figure 15.44 ActivityFinalNode example

  * FinalNode をひとつにまとめても図の意味は変わらない。
  * Notify of Modification からは FinalNode に至らないことに注意（なぜか）。

* Figure 15.45 FlowFinalNode example

  * これは Build Component が反復的に実行すると解釈する。
  * それと同時？に Install Component が実行していることに注意。

* Figure 15.46 FlowFinalNode and ActivityFinalNode example

  * ActivityFinalNode に至るとすると、左側のループはもはや実行中ではないはず？

* Figure 15.47 ControlNode examples (...)

  * この Activity には既視感がある。

15.4 Object Nodes
======================================================================

15.4.1 Summary
----------------------------------------------------------------------

15.4.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 15.48 Object Nodes

  * ObjectNode と関連する要素の役割を理解したい。

15.4.3 Semantics
----------------------------------------------------------------------
.. todo:: ノート作成

15.4.4 Notation
----------------------------------------------------------------------
* Figure 15.49 ObjectNode notations

  * ObjectNode は矩形とテキストで示す。
  * コレクションを表現する ObjectNode はそのようにラベルに示す。
  * Signal 付きの ObjectNode は矩形ではなく、初心者マークみたいな多角形で示す。
    左が凹で右が凸。

* Figure 15.50 ObjectNode annotations

  * 付随情報の表記法。

* Figure 15.51 Specifying selection behavior on an ObjectNode

  * ObjectNode の selection Behavior はコメントの記法を用いて示す。
  * キーワード ``«selection»`` が必要。

* Figure 15.52 Notation for stream and exception parameters

  * streaming Parameter に関連する ActivityParameterNode の記法は、
    文字列 ``{stream}`` をノードシンボルの近くに記すものとする。

  * 例外 Parameter に関連する ActivityParameterNode の記法は、
    小さな三角のシンボルをノードシンボルの近くに記すものとする。

* Figure 15.53 Presentation option for flows between pins and parameter nodes

  * Activity の上側の表現と下側の表現は等価である。
  * Parameters は Activity の境界でやり取りする。

* Figure 15.54 Optional CentralBufferNode notation

  * ObjectNode の記法に、オプションでキーワード ``«centralBuffer»`` を付けるものとする。

* Figure 15.55 DataStoreNode notation

  * ObjectNode の記法に、キーワード ``«datastore»`` を付けるものとする。

15.4.5 Examples
----------------------------------------------------------------------
* Figure 15.56 Example of ActivityParameterNodes for regular and exception Parameters

 * ここで見るべきは境界上のノードのみ。
 * Rejected Computer に三角が付いているので、
   このノードが例外である。

* Figure 15.57 Example of ActivityParameterNodes for streaming Parameters

  * 入出力どちらの ActivityParameterNodes でも streaming たり得る。
  * ちなみに streaming であることと例外であることは両立してはならない。

* Figure 15.58 CentralBufferNode example

  * 予備部品と採用部品の区別法を示していないことに注意。

* Figure 15.59 DataStoreNode example

  * selection Behavior の説明が欲しい。
  * Once a year というシンボルがあるが、これは Timer の類だろう。

15.5 Executable Nodes
======================================================================

15.5.1 Summary
----------------------------------------------------------------------

15.5.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 15.60 Executable Nodes

  * ExecutableNode はひとつの ObjectNode に関連する ExceptionHandlers を所有する。
  * ExceptionHandler は Classifiers を例外の型として関連付ける。

15.5.3 Semantics
----------------------------------------------------------------------
.. todo:: ノート作成

15.5.4 Notation
----------------------------------------------------------------------
* Figure 15.61 ExecutableNode notation

  * ExecutableNode シンボルは角丸矩形。
  * ただし特殊型では記法も特殊化されるだろう。

* Figure 15.62 ExceptionHandler notation

  * ExceptionHandler は稲妻矢印として記す。

    * 矢印の始点は protectedNode である。
    * exceptionType の名前を稲妻のそばに記す。
    * 矢印の終点 exceptionInput ノードは小さい四角で示す。

* Figure 15.63 Alternative ExceptionHandler notation

  * 矢印自体を稲妻にする代わりに、ジグザグマークを
    普通の矢印に添えて ExceptionHandler としてもよろしい。

15.5.5 Examples
----------------------------------------------------------------------
* Figure 15.64 ExceptionHandler example

  * 何らかの（方程式を解く？）行列演算の Activity で、例外送出の仕様を表現している。
  * 逆行列が求まらない例外と、オーバーフローの例外を区別している。
  * 経過がどうあれ、Print Results は実行される。

15.6 Activity Groups
======================================================================

15.6.1 Summary
----------------------------------------------------------------------

15.6.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 15.65 ActivityGroups

  * ActivityGroup の特殊型として ActivityPartition と InterruptibleActivityRegion がある。
  * ActivityGroup は subgraph を表現するためのものだろう。

15.6.3 Semantics
----------------------------------------------------------------------
.. todo:: ノート作成

15.6.4 Notation
----------------------------------------------------------------------
* Figure 15.66 ActivityPartition notations

  * 罫線を駆使して ActivityPartition を記す。
    この記法を swimlane と呼ぶ。

* Figure 15.67 ActivityPartition notations

  * 罫線による ActivityPartitions の図式化は実践的ではないことがある。
    その場合にはここで示す代替記法を検討する。

* Figure 15.68 InterruptableActivityRegion

  * InterruptableActivityRegion は破線丸角矩形で記す。
  * その interruptingEdge を先述の記法で記す。

* Figure 15.69 InterruptableActivityRegion alternative notation

  * 先述の通り interruptingEdge の矢印をストレートにしてジグザグマークを添えてもよい。

15.6.5 Examples
----------------------------------------------------------------------
* Figure 15.70 ActivityPartitions using swimlane notation

  * いつもの例題に swimlanes を明記したもの。
  * ところで swimlanes をまたぐ ActivityEdges は、
    どのサブ ActivityPartition の所属でもない。

* Figure 15.71 ActivityPartitions using annotation

  * 先の見本から swimlane を外したもの。
  * 丸括弧とキーワード ``«external»`` で所属する ActivityPartition がわかる。

* Figure 15.72 ActivityPartitions using multidimensional swimlane notation

  * 紙に描くものである以上、多次元と言っても高々 2 である。

* Figure 15.73 InterruptableActivityRegion example

  * InterruptableActivityRegion と凹五角形シンボルの組み合わせは使い易そうだ。

15.7 Classifier Descriptions
======================================================================
機械生成による節。

15.8 Association Descriptions
======================================================================
機械生成による節。

.. 15.8.1 A_containedEdge_inGroup [Association]
.. 15.8.2 A_containedNode_inGroup [Association]
.. 15.8.3 A_decisionInputFlow_decisionNode [Association]
.. 15.8.4 A_decisionInput_decisionNode [Association]
.. 15.8.5 A_edge_activity [Association]
.. 15.8.6 A_edge_inPartition [Association]
.. 15.8.7 A_exceptionInput_exceptionHandler [Association]
.. 15.8.8 A_exceptionType_exceptionHandler [Association]
.. 15.8.9 A_group_inActivity [Association]
.. 15.8.10 A_guard_activityEdge [Association]
.. 15.8.11 A_handlerBody_exceptionHandler [Association]
.. 15.8.12 A_handler_protectedNode [Association]
.. 15.8.13 A_inInterruptibleRegion_node [Association]
.. 15.8.14 A_inPartition_node [Association]
.. 15.8.15 A_inState_objectNode [Association]
.. 15.8.16 A_incoming_target_node [Association]
.. 15.8.17 A_interruptingEdge_interrupts [Association]
.. 15.8.18 A_joinSpec_joinNode [Association]
.. 15.8.19 A_node_activity [Association]
.. 15.8.20 A_outgoing_source_node [Association]
.. 15.8.21 A_parameter_activityParameterNode [Association]
.. 15.8.22 A_partition_activity [Association]
.. 15.8.23 A_redefinedEdge_activityEdge [Association]
.. 15.8.24 A_redefinedNode_activityNode [Association]
.. 15.8.25 A_represents_activityPartition [Association]
.. 15.8.26 A_selection_objectFlow [Association]
.. 15.8.27 A_selection_objectNode [Association]
.. 15.8.28 A_structuredNode_activity [Association]
.. 15.8.29 A_subgroup_superGroup [Association]
.. 15.8.30 A_subpartition_superPartition [Association]
.. 15.8.31 A_transformation_objectFlow [Association]
.. 15.8.32 A_upperBound_objectNode [Association]
.. 15.8.33 A_variable_activityScope [Association]
.. 15.8.34 A_weight_activityEdge [Association]

.. include:: /_include/uml-refs.txt
