======================================================================
15 Activities
======================================================================

.. contents::
   :depth: 4

15.1 Summary
======================================================================

Activity とは Behavior の一種であって、辺により相互接続される節点のグラフとして
指定される (:doc:`./ch13-common-behavior`)。

* その節点の部分集合は、その Activity 全体の低水準手順を具体化する実行可能節点
  だ。
* オブジェクト節点は実行可能節点に入出力するデータを保持し、オブジェクトフロー
  辺を縦断して移動する。

こういう計算モデルが実質的に同時処理であることを理解する：

   Activities are essentially what are commonly called “control and data flow”
   models. Such models of computation are inherently concurrent, as any
   sequencing of activity node execution is modeled explicitly by activity
   edges, and no ordering is mandated for any computation not explicitly
   sequenced.

Activities は何を記述するものなのか：

   Activities may be applied to organizational modeling for business process
   engineering and workflow. In this context, events often originate from inside
   the system, such as the finishing of a task, but also from outside the
   system, such as a customer call. Activities can also be used for information
   system modeling to specify system level processes.

この章の残りは、活動モデルがどのように構造化されるのか、さまざまな種類のオブジェ
クト節点と制御節点について述べられる。

UML では実行可能節点は Actions (:doc:`./ch16-actions`) しかない。

   Actions are required for any significant capabilities of Activities. Actions
   invoke other Behaviors and Operations (see above), access and modify objects,
   as well as link them together, and perform more advanced coordination of
   other Actions (Structured Actions). They are central to the “data flow”
   aspects of Activities, introducing a specialized form of object node (Pins)
   for object flows to get and provide data to Actions.

* Actions を表す具体的構文は Activities を表す具体的構文の部分集合であり、一部は
  本章で規定される。
* Action 表記法は Activity 図でしか現れない。

この章では実行可能節点を使うことで Actions からある程度の独立性を実現するが、そ
れでも :doc:`./ch16-actions` と一緒に読む必要がある。

15.2 Activities
======================================================================

15.2.1 Summary
----------------------------------------------------------------------

   An Activity is a Behavior specified as sequencing of subordinate units, using
   a control and data flow model.

* 実行の流れは ActivityEdges によって接続される ActivityNodes としてモデル化され
  る。
* ExecutableNode は、算術計算、操作の呼び出し、オブジェクト内容の操縦など、従属
  的挙動の実行であることがある。
* ActivityNodes は、同期、決定、同時制御のような、制御の流れに関する構成要素をも
  含む。

..

   This sub clause describes the basic structure and flow semantics of an
   activity model as a graph of nodes and edges. Subsequent sub clauses then
   describe the various kinds of ActivityNodes that an Activity may contain and
   how those nodes may be grouped within the Activity.

15.2.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 15.1 Activities

Activity, Variable, ActivityNode, ActivityEdge, ObjectFlow, ControlFlow 周りを見
ていく。Flow とは Edge の一種らしい。

15.2.3 Semantics
----------------------------------------------------------------------

15.2.3.1 Activities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Activity における ActivityNode 一つの実行は、その Activity 内にある他の
ActivityNodes の実行に影響を与えたり影響されたりすることがある。このような辺はこ
の ActivityNodes を相互に接続する ActivityEdges で表される。

トークンの流れ：

   The effect of one ActivityNode on another is specified by the *flow of
   tokens* over the ActivityEdges between the ActivityNodes.

トークン：

   *Tokens* are not explicitly modeled in an Activity, but are used for
   describing the execution of an Activity.

オブジェクトトークンと ObjectFlow をペアで理解する：

   An :dfn:`object token` is a container for a value that flows over ObjectFlow
   edges (some object tokens can flow over ControlFlow edges, as specified by
   the modeler, see ``isControlType`` for ObjectNodes in sub clause 15.4).

空トークンと制御トークン：

   An object token with no value in it is called a *null* token. A *control
   token* affects execution of ActivityNodes, but does not carry any data, and
   flows only over ControlFlow edges.

同じ値を含んでいるとしても、トークンは他のトークンとは区別される。

ActivityEdge とトークン：

   ActivityEdges are directed, with tokens flowing from the ``source``
   ActivityNode to the ``target`` ActivityNode.

トークンが辺を流れるには条件があるらしい：

   However, tokens *offered* to an ActivityEdge by the ``source`` ActivityNode
   may not immediately flow along the edge. Instead, the tokens only move when
   the offer is *accepted* by the ActivityEdge, which requires at least the
   ``target`` ActivityNode to accept them also, which in turn might depend on
   acceptance of cascading offers of the same tokens to edges and nodes further
   downstream of the ``target``.

* オブジェクトトークンは ObjectNodes によってしか受理されなければならない。
* 制御トークンは ExecutableNodes によってしか受理されなければならない。

ControlNode の用途：

   ControlNodes are used to control the routing of offers through a network of
   ActivityEdges, controlling the flow of accepted tokens.

節点と辺には名前があるが、一意的とは限らない：

   ActivityNodes and ActivityEdges may be named, however, the ``nodes`` and
   ``edges`` of an Activity are not required to have unique names within that
   Activity.

類似する節点に同じ名前を付けるなど、便利なことがあるらしい。

Activity は Namespace の一種であり、その ``members`` は区別できる必要があるのだ
が、Activity の ``nodes`` と ``edges`` は ``ownMembers`` ではなく
``ownElements`` であるため、この必要性は節点と辺の名前付けに影響しない。

   Even though an Activity is a Namespace (a Behavior is a Class, which is a
   Classifier, which is a Namespace), and the members of a Namespace are
   required to be distinguishable (see sub clause 7.4), this constraint does not
   affect the naming of Activity nodes and edges because the nodes and edges of
   an Activity are ownedElements but not ownedMembers of the Activity.

Activities は Classes であり、次のような Properties を支援することが許される：

* 工程の実行時間、コストなど。
* 実行者、完了報告先、使用中の資源のような、オブジェクトに関するリンクを指定する
  Associations
* 開始、停止、中断などのオブジェクトの実行を管理する Operations
* 開始、一時停止などの実行の状態を決定する StateMachines

15.2.3.2 Activity Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   ActivityNodes are used to model the individual steps in the behavior
   specified by an Activity.

ActivityNode が実行される条件にはトークンが関係している：

   An ActivityNode is enabled to begin execution when specified conditions are
   satisfied on the tokens offered to it on ``incoming`` ActivityEdges; the
   conditions depend on the kind of node. When an ActivityNode begins execution,
   tokens are accepted from some or all of its ``incoming`` ActivityEdges and a
   token is *placed on* the node.

節点が実行を完了すると、トークンはそこから除去されて、この節点の ``outgoing``
ActivityEdges の一部または全部に供給される。

ActivityNodes の実行順序について：

   All restrictions on the relative execution order of two or more ActivityNodes
   are explicitly constrained by ActivityEdge relationships. If two
   ActivityNodes are not ordered by ActivityEdge relationships, -略- they may
   execute concurrently.

本文で言う concurrent は一貫して there is no required order in which ... の意味
にとるのがいい。

先のトークン一意性が次の仕様に効いてくる：

   As an ActivityNode may be the ``source`` for multiple ActivityEdges, the same
   token can be offered to multiple ``targets``. However, the same token can
   only be accepted at one ``target`` at a time

トークン一つが同時に複数の ActivityNodes に供給された場合、そのうちの高々一つの
ActivityNode が受理するものとする。どの節点に受理されるかは Activity 流通意味に
よっては完全には決定されない。

ActivityNodes には以下の三種類がある：

ControlNodes
   ActivityEdges 上のトークンの流通を管理する交通スイッチとして機能する。トーク
   ンは ControlNodes 上で休止することは不可能だ。
ObjectNodes
   ``incoming`` ObjectFlows から受理したオブジェクトトークンを保持して、その後そ
   れらを ``outgoing`` ObjectFlows に対して捧げることがある。ControlFlow につい
   ては設計者が指定した例外がある (15.4)。
ExecutableNodes
   Activity の所望の挙動を実際に実施する。

      If an ExecutableNode has ``incoming`` ControlFlows, then there must be
      tokens *offered* on all these flows that it accepts before beginning
      execution. While executing, an ExecutableNode is considered to hold a
      single control token indicating it is executing. When it completes
      execution, it offers control tokens on all ``outgoing`` ControlFlows. All
      ``incoming`` and ``outgoing`` ActivityEdges of an ExecutableNode must be
      ControlFlows.

15.2.3.3 Activity Edges
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ActivityEdge の定義と言っていい：

   An ActivityEdge is a directed connection between two ActivityNodes along
   which tokens may flow, from the ``source`` ActivityNode to the ``target``
   ActivityNode.

トークンと辺の関連：

   Tokens are *offered* to an ActivityEdge by the ``source`` ActivityNode of the
   edge. Offers propagate through ActivityEdges and ControlNodes, according to
   the rules associated with ActivityEdges (see below) and each kind of
   ControlNode (see sub clause 15.3) until they reach an ObjectNode (for object
   tokens) or an ExecutableNode (for control tokens and some object tokens as
   specified by modelers, see ObjectNodes in sub clause 15.4).

ObjectNode および ExecutableNode の各種には、供給されたトークンがいつ受理される
かの規則がある。この種の節点がトークンを受理すると、そのトークンは最初の供給元
ActivityNode から受理側 ActivityNode に流れる。

辺に対するガードの概念：

   An ActivityEdge may have a ``guard``, which is a ValueSpecification that is
   evaluated for each token offered to the edge. An offer shall only pass along
   an ActivityEdge if the ``guard`` for the edge evaluates to true for the
   offered token.

ガードのない辺は任意のトークンに対して真と評価されるガードのある辺と等価だ。

ガートは一般的には DecisionNodes で用いられるが、どの ActivityEdge でも用いてよ
い。

トークンの流通量を辺の ``weight`` が規定することがある：

   Any number of tokens can pass along an ActivityEdge, in groups at one time,
   or individually at different times. The ``weight`` property dictates the
   minimum number of tokens that must traverse the edge at the same time. It is
   a ValueSpecification that is evaluated every time a new token is offered by
   the ``source`` ActivityNode. It must evaluate to a positive
   LiteralUnlimitedNatural and may be a constant.

トークン供給が失敗する状況。All or nothing 方式か：

   If the ActivityEdge has a ``guard``, the ``guard`` must evaluate to true for
   each token offered to the edge that counts towards the minimum. If the
   ``guard`` fails for any of the tokens, and this reduces the number of tokens
   that can be offered to the ``target`` to less than the ``weight``, then all
   the tokens fail to be offered.

* 無制限の場合にはトークンは辺を流れる前にすべて受理されなければならない。
* 辺に重みが指定されていない場合、それに 1 を指定することと同値とする。

ActivityEdges には以下の二種類がある：

ControlFlow
   制御トークンしか渡さない ActivityEdge だ。ActivityNodes の実行を明示的に順序
   立てるために用いられる。
ObjectFlow
   オブジェクトトークンがそれに沿って引き渡すことができる ActivityEdge
   だ。ObjectNodes 間の値の流通をモデル化する。

      Tokens are offered to the ``target`` ActivityNode in the same order as
      they are offered from the ``source``. If multiple tokens are offered at
      the same time, then the tokens are offered in the same order as if they
      had been offered one at a time from the ``source``. If the ``source`` is
      an ObjectNode with an ordering specified, then tokens from the ``source``
      are offered to the ObjectFlow in that order and, consequently, are offered
      from the ObjectFlow to the ``target`` in the same order.

ControlFlows とは異なり、ObjectFlows は多重送受信、ObjectNodes からのトークン選
択、トークン変換に対しての支援をも備えている。

15.2.3.4 Object Flows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

オブジェクトトークンの立場から ObjectFlow を理解すると：

   Object tokens pass over ObjectFlows, carrying data through an Activity via
   their values, or carrying no data (*null tokens*).

空トークンはオプションの値を生成しなかったことを明示的に示す目的などに用いられ
る。

ObjectFlow は変換動作を有することがある：

   An ObjectFlow may have a ``transformation`` Behavior that has a single input
   Parameter and a single output Parameter. If a ``transformation`` Behavior is
   specified, then the Behavior is invoked for each object token offered to the
   ObjectFlow, with the value in the token passed to the Behavior as input (for
   a null token, the behavior is invoked but no value is passed). The output of
   the Behavior is put in an object token that is offered to the ``target``
   ActivityNode instead of the original object token.

* 変換動作の出力引数の多重度上限値が 1 以上であり、この変換が複数値を生成する場
  合、値それぞれが別々のオブジェクトトークンに入れられ、すべてが ``target`` に渡さ
  れる。
* 出力引数の多重度下限値が 0 で、この変換が値を生成しない場合、``target`` に空
  トークンが供給される。

ObjectFlow は選択動作を有することがある：

   An ObjectFlow may have a ``selection`` Behavior that has a single input
   Parameter and a single output Parameter. The input Parameter of the Behavior
   must be unordered, nonunique and have a multiplicity of ``0..*`` (a “bag”),
   and the output Parameter must have a multiplicity upper bound of 1.

ObjectFlow に新しいトークンが供給されたり撤回されたりするたびに、ObjectFlow に現
在供給されているオブジェクトトークンすべての値が Behavior の入力 Parameter に渡
され、``selection`` Behavior が呼び出される。この選択動作は入力された値の中から
一つ選択し、出力する。この出力値はオブジェクトトークンに入れられ、``target``
ActivityNode に渡される。``selection`` Behavior が出力を生成しない場合、空トーク
ンが渡される。

ObjectFlow に ``transformation`` と ``selection`` の両方があるならば：

   then the ``transformation`` Behavior is invoked first when a new token is
   offered to the ObjectFlow and the resulting value is used in the invocation
   of the ``selection`` behavior.

トークンが ``target`` 節点に向けて与えられる間に ``transformation`` または
``selection`` Behavior が使われるので、そのトークンが ``target`` 節点に受け入れ
られる前に何度も同じトークンで実行されることがある。この事は、その Behavior に副
作用があってはならないことを意味する。

   but transformations may for example, navigate from one object to another, get
   an attribute value from an object, or replace a data value with another.

多重送信と多重受信：

   Multicasting and multireceiving are used in conjunction with
   ActivityPartitions (see sub clause 15.6) to model flows between Behaviors
   that are the responsibility of objects determined by a publish and subscribe
   facility. However, the particular publish/subscribe semantics used are not
   specified in this standard.

15.2.3.5 Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ObjectFlows が Activity 内でデータを移動するための主な手段であるならば、
Variables はデータを間接的に引き渡すための代替法だと言える。

* Activity の実行中、この Activity の Variables のそれぞれは一つ以上の値を保持す
  ることが許される。Variables に値を書き込み、その後 Variables から値を読み取る
  Actions がある (16.9)。
* Activity の Variables は Namespace としての Activity の ``ownMembers`` である
  が、この Activity に対して局所的であり、外部からは見えない。

間接的なデータ移動経路：

   The use of a Variable effectively provides indirect data flow paths from the
   point at which a value is written to the Variable to all the points at which
   the value is read from the Variable.

Variable は ConnectableElement の一種であり、それ自体が TypedElement だ。
Variable に保持される値はいずれも Variable の Type と適合しなければならない。
:doc:`./ch11-structured-classifiers` および :doc:`./ch07-common-structure` 参
照。

Variable は MultiplicityElement でもある。:doc:`./ch07-common-structure` 参照。

Variable に値を書き込む唯一の方法が Activity 内の Actions であるため、多重度の強
制が必ずしも可能とは限らない。

15.2.3.6 Activity Execution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   An Activity may have ``precondition`` and ``postcondition`` Constraints, as
   inherited from Behavior (see sub clause 13.2).

* これらは Activity の全呼び出しに対して大局的に適用される。
* Activity 内の Actions は局所的 ``precondition`` と ``postcondition`` を持つこ
  とがある。

Behavior であるので、Activity には Parameters があってもよい。このような
Parameter それぞれに対し、Activity には対応する ActivityParameterNode という
節点がある。

* inout Parameter の場合には入力用と出力用の二つを持つ。
* ActivityParameterNode は Activity 内で Parameter の値を入手できるようにする
  ObjectNode だ。

Activity が呼び出されると、入力 Parameters に渡された値がオブジェクトトークンに
置かれ、Activity の対応する入力 ActivityParameterNode に置かれる。

* 入力 Paramters に値がない場合は空トークンが置かれる。
* これらの ActivityParameterNodes はトークンを ``outgoing`` ActivityEdges に与え
  る。

Activity 呼び出しの最初は、一般の節点はトークンを持っていない：

   However, nodes that do not have incoming edges and require no input data to
   execute are immediately enabled. A single control token is placed on each
   enabled node and they begin executing concurrently. Such nodes include
   ExecutableNodes (see sub clause 15.5) with no incoming ControlFlows and no
   mandatory input data and InitialNodes (see sub clause 15.3).

次はわかりにくい ``isSingleExecution`` の仕様だ：

   On each subsequent invocation of the Activity, the ``isSingleExecution``
   property indicates whether the same execution of the Activity handles tokens
   for all invocations, or a separate execution of the Activity is created for
   each invocation.

単一実行は読んでもよくわからないので飛ばす。既定の個別実行は：

   If a separate execution of the Activity is used for each invocation (this is
   the default), tokens from the various invocations do not interact. For
   example, an Activity that is a ``classifierBehavior`` is invoked when the
   Classifier is instantiated (see sub clause 13.2),

Activity に ``streaming`` Parameters がある場合、単一実行の途中であっても（対応
する ActivityParameterNodes を経て）トークンがその Activity に出入りすることがあ
る。

``streaming`` Parameters のない Activity の実行が完了するのは、実行している節点
がすでになく、実行可能節点がないときか、または ActivityFinalNode (15.3) を用いる
ことで明示的に停止されたときだ。その他方：

   The execution of an Activity with streaming input Parameters shall not
   terminate until the cumulative number of values posted to each of those input
   Parameters (by the invoker of the Activity) is at least equal to the
   Parameter multiplicity lower bound. The execution of an Activity with
   streaming output Parameters shall not terminate until the cumulative number
   of values posted to each of those output Parameters (by the Activity itself)
   is at least equal to the Parameter multiplicity lower bound.

完了時の出力：

   When the execution of an Activity completes, all ActivityParameterNodes
   corresponding to non-streaming output Parameters shall hold at least as many
   non-null object tokens as given by the corresponding Parameter multiplicity
   lower bound.

各出力 ActivityParameterNode のオブジェクトトークンに関連付けられた値は、対応す
る出力 Parameter で Activity から渡され、Activity の呼び出し元が利用できるように
なる。

出力引数が例外の場合：

   An output Parameter may also be identified as an *exception* Parameter by
   having ``isException`` = true (see sub clause 9.4).

* 例外 Parameter に送られた出力は Behavior の他の出力 Parameters に送られること
  を妨げる。
* 例外 Parameter に関連付けられた出力 ActivityParameterNode にオブジェクトトーク
  ンが到着する場合、Activity の実行は直ちに停止する。トークンの値は例外
  Parameter に渡されるが、非 streaming Parameter に関連付けられた他の出力
  ActivityParameterNodes 上のトークンは失われ、その値は関連 Parameters に渡され
  ない。
* Activity が停止する前に streaming 出力 Parameters に送られた値は影響を受けな
  い。

例外を使用する状況は：

   Use exception Parameters on Activities only if it is desired to abort all
   flows in the Activity. For example, if the same execution of an activity is
   being used for all its invocations (i.e., ``isSingleExecution`` = true), then
   multiple streams of tokens will be flowing through the same Activity.

この場合、一つが例外出力に到達したからというだけで、流れのすべてを中断することは
まず望ましくない。

   Arrange for separate invocations of the Activity to use separate executions
   of the Activity (i.e., ``isSingleExecution`` = false) when employing
   exception Parameters, so flows from separate executions will not affect each
   other.

15.2.3.7 Activity Generalization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Activity は Classifier であり、Generalization 関係に関与してよい。

   A specialized Activity inherits the ``nodes`` and ``edges`` of its general
   Activities. ActivityNodes and ActivityEdges are RedefinableElements (see sub
   clause 9.2) that may be redefined in a specialized Activity.

再定義は置き換えということか：

   An ActivityNode in a specialized Activity that redefines an ActivityNode from
   a general Activity is considered to replace the redefined ActivityNode for
   any inherited ActivityEdges that had the redefined ActivityNode as a source
   or target.

総体的 Activity から ActivityEdge を再定義する ActivityEdge は、再定義先の
ActivityEdge を到着または出発辺として持っていた継承先 ActivityNode のいずれに対
しても再定義元 ActivityEdge を置き換えるとみなされる。

   If the redefined ActivityEdge is an incoming or outgoing edge for any
   ActivityNode that is not inherited but is itself redefined, then the
   ActivityEdge is replaced for the redefining ActivityNode.

特殊化 Activity の実行に用いられる節点と辺の有効な集合は、継承先節点と辺（再定義
元節点と辺を含まない）と、その特殊 Activity で定義された節点と辺（再定義先節点と
辺を含む）との和集合だ。

   The execution of the specialized Activity then proceeds as usual, but using a
   graph of nodes and edges constructed from the union sets.

15.2.4 Notation
----------------------------------------------------------------------

   This notation is optional in that a conforming tool may use a textual
   concrete syntax instead.

Activity の記法は ActivityNodes と ActivityEdges の記法の組み合わせに加え、枠線
と左上に表示される名前を加えたものだ。

* ActivityParameterNodes は Activity の枠線上に表示する。
* Behavior から継承した事前条件と事後条件を、キーワード ``«precondition»``,
  ``«postcondition»`` と共にテキスト上の式としてそれぞれ示す。
* ``isSingleExecution`` が真 Activities については、キーワード
  ``«singleExecution»`` を用いる。

   Figure 15.2 Activity notation

* 図の丸角縁は :doc:`./ana-diagrams` で述べられた枠記法で置き換えてよい。
* 丸角縁にせよ枠にせよ完全に省略してよい。その場合には ActivityParameterNodes
  は図式内のどこに現れてもよい。

   Figure 15.3 Activity class notation

この図のように Classes を表す表記法を Activity の特徴を図表化するのに利用するこ
ともある。キーワードは ``«activity»`` だ。

   Figure 15.4 ActivityNode notation

ActivityNodes 各種の記法のカタログ。次の節と :doc:`./ch16-actions` で詳しく議論
する。

   Figure 15.5 ActivityEdge notation

ActivityEdges 各種の記法のカタログ。

* 鏃はすべて開いた形状を用いる。
* 辺に名前がある場合は矢印の近くに表記する。
* イラストにはないが ``guards`` を記すには矢印末尾にある角括弧の中にテキスト表示
  する。

..

   Figure 15.6 ActivityEdge connector notation

ActivityEdge は連結器を使って記すことも許されている。連結器は辺の名前が中に書か
れた小さい丸だ。この記法はまともに描くと矢印が長くなるときに採用すればよい。

ラベルの付いたすべての接続器は、同一 Activity 図で同一ラベルのついた他のものの正
確に一つに対して対になっていなければならない。

   Figure 15.7 ActivityEdge notation

ActivityEdge の重みは中括弧で囲んで表記する：

.. code:: bnf

   <weight-annotation> :: =‘{’ ‘weight’ ‘=’ <value-specification> ‘}’

重みは定数であってもよい値仕様であり、ゼロでない無制限の自然数として評価される。
無制限の重みは ``*`` と表記される。:doc:`ValueSpecifications <./ch08-values>` の
記法を参照。

InterruptibleActivityRegion の ``interruptingEdge`` は稲妻型の矢印とする。
(15.6) も参照。

   Figure 15.8 ControlFlow notation

制御フローは二つの行動を接続する矢印で示す。

   Figure 15.9 ObjectFlow notations

オブジェクトフローも矢印として示す。この図の右上と下は同じ意味。(16.2) も参照。
Pins を用いる記法のほうがよい？

   Figure 15.10 Specifying selection behavior on an ObjectFlow

``selection`` Behavior の記法にはキーワード ``«selection»`` を註釈記号に入れ、適
切な ObjectFlow 記号に取り付けて指定する。

``transformation`` Behavior も同様に、キーワードは ``«transformation»`` を使って
指定する。

コメントとしては Behavior をテキスト表現したもの（例えば OpaqueBehavior の本文な
ど）やテキスト的に表現されていない Behavior の名前を書いてもよい。

   Figure 15.11 Eliding objects flowing on the edge

複雑な図式では乱雑さを避けるために Pins を省略してよい。省略されていることを
示唆するために、小さい正方形を矢印の上に表示してよい。

``effect`` のような、通常 Pin の近くにあるような装飾を流線の端子に表示することが
可能だ。

多重送信および多重受信はそれぞれ ObjectFlow に ``«multicast»`` または
``«multireceive»`` と註釈を付すことで指定する。

15.2.5 Examples
----------------------------------------------------------------------

   Figure 15.12 Activity node example (where the arrowed lines are the only
   non-activity node symbols)

次の種類の ActivityNodes の記法の見本となる。

* ExecutableNodes: ``Receive Order``, ``Fill Order``, etc.
* ObjectNodes: ``Invoice``
* ControlNodes:

  * InitialNode: 先頭の黒丸
  * DecisionNode: 始めの方のダイヤモンド
  * ForkNode, JoinNode: Ship Order 前後の縦棒
  * MergeNode: 終わりの方のダイヤモンド
  * ActivityFinalNode: 末尾の目玉

..

   Figure 15.13 ActivityEdge examples

矢印は ControlFlow か ObjectFlow だ。

左上。``Fill Order`` と ``Ship Order`` を結ぶ矢印は ControlFlow 辺だ。``Fill
Order`` が完了すると ``Ship Order`` に制御が移ることを示している。``Filled`` と
あるのは辺の名前だ。

左下のも同じ意味。矢印をマル A で接続している。

右上。ObjectNode ``Invoice`` の前後にある矢印は両方 ObjectFlow だ。``Invoice``
オブジェクトが ``Send Invoice`` から ``Make Payment`` へ移動することを示す。

   Figure 15.14 ObjectFlow example

両者の意味は同じ。オブジェクト ``Order`` の移動を暗示している。目新しいのは右
側：

   The example on the right has one arrowed line starting from a ``Fill Order``
   OutputPin (an ObjectNode) and ends at a ``Ship Order`` InputPin.

左側の ``Order`` が CentralBufferNode ではないという仮定が必要だが。

   Figure 15.15 Eliding objects flowing on the edge

省略版だとオブジェクトの個数に関わらず小さい正方形が一つになる？

   Figure 15.16 Specifying ``selection`` and ``transformation`` Behaviors on an
   ObjectFlow

``selection`` および ``transformation`` Behaviors の見本。註釈頼み。

* 左の図は ``Order`` が ``Order Priority`` に基づいて出荷され、同じ優先度のもの
  は FIFO 方式でなるべく ``Filled`` されることを示す。
* 右の図は ``Close Order`` の結果 ``Closed`` な ``Order`` を生成する。``Send
  Customer Notice`` は ``Customer`` オブジェクトを必要とする。この変換は
  ``Order`` を受け取り、関連する ``Customer`` オブジェクトを生成する問い合わせ操
  作の呼び出しを指定する。

..

   Figure 15.17 Linking a class diagram to an object node

Activity 図内の ObjectNode ``Order`` と、Class ``Order`` を述べるクラス図と
のリンクを表現している。

   The class diagram shows that filling an order requires order, line item, and
   the customer’s trim-and-finish requirements.

とあるが、この図式からそこまでは読み取れないだろう？

   Figure 15.18 Specifying multicast and multireceive on the edge

キーワード ``«multicast»`` と ``«multireceive»`` の見本。

``RFQs`` は特定の複数 ``Seller`` に送信され、各 ``Seller`` による見積もり回答が
求められる。その後、いくつかの ``Seller`` が ``Quote Responses`` を返す。複数の
応答を受信することができるため、辺には ``«multireceive»`` オプションのラベルが付
けられる。

   Publish/subscribe and other brokered mechanisms can be handled using the
   multicast and multireceive mechanisms.

スイムレーンは送信者と受信者を示す重要な機能だ。

   Figure 15.19 ActivityEdge connector example

図式中の fork と merge の間にまともに矢印を描くのは面倒なので、このようなワープ
のような記法の支援がある。

   Figure 15.20 Equivalent model

Fig. 15.19 のワープ記法不採用版。

   Figure 15.21 ActivityEdge weight examples

左上。定数 ``weight`` を要求する。11 人いないと Form Cricket Team 不能。

右上。変数 ``weight`` を要求する。

下。入札期間が終わるとイベント ``Ready to award bid`` が発生し、``Award Bid`` が
入札すべてを一度に受け取り、落札する一件を選ぶ。この凹五角形節点の記法の意味はま
だやっていない？

   Figure 15.22 Example of an activity with input parameter

``Requested Order`` とあるのが入力引数に対応する ActivityParameterNode だ。呼び
出しのすべてが同じ実行を使用する。

   Figure 15.23 Part selection workflow example

``Standards Engineer`` は ``Provide Required Part`` の部分段階が指定された順序、
指定された条件下で実施されることを保証するが、その段階を必ずしも実施するわけでは
ない。``Standards Engineer`` が工程を管理していても、この部分段階のいくつかは
``Design Engineer`` が実施する。

``Expert Part Search`` では、部品が見つかる場合と見つからない場合がある。
見つからない場合は ``Assign Standards Engineer`` が呼び出される。

``Specify Part Mod Workflow`` は、実行される作業を表す ``Activity`` のオブジェク
トである値を生成する。これらは、スケジューリングと実行のために後続のアクションに
渡される (e.g. ``Schedule Part Mod Workflow``, ``Execute Part Mod Workflow``,
``Research Production Possibility``)。

   As Activities are Classes, instances of them can be passed in object tokens
   and then later be executed. This is an example of runtime Activity
   instantiation and execution.

..

   Figure 15.24 Trouble ticket workflow example

よくあるチケット管理の Activity だろう。

   Figure 15.25 Activity with attributes and operations

Activity のクラスの特徴を Class の記法で示す見本。

15.3 Control Nodes
======================================================================

15.3.1 Summary
----------------------------------------------------------------------

   A ControlNode is a kind of ActivityNode (see sub clause 15.2.2) used to
   manage the flow of tokens between other nodes in an Activity.

InitialNodes, FinalNodes, ForkNodes, JoinNodes, MergeNodes, DecisionNodes など、
さまざまな ControlNode の具象型について述べられる。

15.3.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 15.26 Control Nodes

ControlNode は ActivityNode から派生した型で、ControlNode からもかなりの数のクラ
スが派生している。

15.3.3 Semantics
----------------------------------------------------------------------

15.3.3.1 Initial Node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

InitialNode の定義：

   An InitialNode is a ControlNode that acts as a starting point for executing
   an Activity.

Activity に InitialNode が複数あっても構わない。その場合、Activity を呼び出すと
InitialNode のそれぞれに対して一つずつ、複数の同時制御フローが開始する。

   An InitialNode shall not have any ``incoming`` ActivityEdges

Activity が所有する InitialNode はこの Activity が実行を開始すると常に有効にな
り、そのような InitialNode のそれぞれに制御トークンが一つずつ置かれる。

InitialNode の ``outgoing`` ActivityEdges はすべてが ControlFlows でなければなら
ない。InitialNode に配置された制御トークンはすべて ``outgoing`` ControlFlows に
同時に供給される。

   InitialNodes are an exception to the rule that ControlNodes cannot “hold”
   tokens, but only manage their flow.

15.3.3.2 Final Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A FinalNode is a ControlNode at which a flow in an Activity stops.

* FinalNode には ``outgoing`` ActivityEdges がないものとする。
* FinalNode は ``incoming`` ActivityEdges で供給されたトークンすべてを受理する。

FinalNode には FlowFinalNode と ActivityFinalNode の二種類がある。

FlowFinalNode とは一つの流れを停止する FinalNode だ。FlowFinalNode が
受理したトークンは全て破壊される。Activity 内の他の流れには影響しない。

ActivityFinalNode とは Activity の流れすべてを停止する節点だ。

* Activity が所有する ActivityFinalNode にトークンが到達すると、その Activity の
  実行が停止する。

     If an Activity owns more than one ActivityFinalNode, then the first one to
     accept a token (if any) terminates the execution of the Activity, including
     the execution of any other ActivityFinalNodes.

* Activity の実行が停止すると、出力 ActivityParameterNodes 以外の ObjectNodes に
  保持されているトークンをすべて破壊し、かつ、Activity から同期的に呼び出されて
  いる Behaviors の実行を停止する。ただし非同期的に呼び出されている Behaviors の
  実行には影響しない。
* Activity の実行が停止すると、15.2.3 節で述べたようにその Activity の呼び出しが
  完了する。

Activity の流れの全てを中止するのが望みでなければ、FlowFinalNode を使う。
ActivityFinalNode は使わない。

15.3.3.3 Fork Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ForkNode の定義。前後の辺の本数と性質に注意：

   A ForkNode is a ControlNode that splits a flow into multiple concurrent
   flows. A ForkNode shall have exactly one ``incoming`` ActivityEdge, though it
   may have multiple ``outgoing`` ActivityEdges. If the ``incoming`` edge is a
   ControlFlow, then all ``outgoing`` edges shall be ControlFlows and, if the
   ``incoming`` edge is an ObjectFlow, then all ``outgoing`` edges shall be
   ObjectFlows.

ForkNode とトークンの関係：

   Tokens offered to a ForkNode are offered to all ``outgoing`` ActivityEdges of
   the node. If at least one of these offers is accepted, the offered tokens are
   removed from their original source and the acceptor receives a copy of the
   tokens. Any other offer that was not accepted on an ``outgoing`` edge due to
   the failure of the target to accept it remains pending from that edge and may
   be accepted by the target at a later time. These edges effectively accept
   separate copies of the offered tokens, and offers made to the edges shall
   stand to their targets in the order in which they were accepted by the edge
   (first in, first out).

これは ActivityEdges が下流への移動をブロックされている場合、トークンを保持でき
ないという規則の例外だ。ForkNodes から出る ActivityEdge は保留中の供給がすべて目
標に受理されるまで、受理したトークンを保持し続ける。

* 目標ではなく、それらの ``guard`` の失敗が原因で供給を受理されなかった
  ``outgoing`` ActivityEdges は、それらのトークンの複製を受理しないものとする。
* ForkNode から出発した ActivityEdges に ``guards`` が使われている場合、防御され
  た辺を通過するトークンの到着に下流 JoinNodes が依存しないように設計する必要が
  ある。それが回避できない場合には、ForkNode とその防御のある辺の間に
  DecisionNode をなるべく導入し、防御が失敗する場合にトークンが下流 JoinNode に
  退避させるようにする。

15.3.3.4 Join Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A JoinNode is a ControlNode that synchronizes multiple flows.

* JoinNode には厳密に一つの ``outgoing`` ActivityEdge があるが、``incoming``
  ActivityEdges が複数あることは許される。
* JoinNode の ``incoming`` 辺のどれかが ObjectFlows である場合、``outgoing`` 辺
  は ObjectFlow であるものとする。そうでない場合は ``outgoing`` 辺は ControlFlow
  であるものとする。

次に ``joinSpec`` を理解する：

   Join nodes may have a ``joinSpec``, which is a ValueSpecification that
   determines the condition under which the join will emit a token.

* JoinNode が ``joinSpec`` を持つ場合、この ValueSpecification は JoinNode に新
  しいトークンが供給されるたびに評価される。この評価は、評価中に新しいトークンが
  供給されても中断されないものとし、同時評価が開始されないものとする。
* ValueSpecification は真偽値で評価されなければならない。

``joinSpec`` ValueSpecification がテキスト式で与えられる場合、``incoming`` 辺の
名前を次のものを示すために使ってよい：

* ControlFlow からの供給の有無を示す真偽値
* ObjectFlow から供給されたオブジェクトトークンに関連付けられた値（あれば）

別の方法としては、``joinSpec`` は一つの真偽値演算子の名前を持つ Expression で構
成され、オペランドは指定されない。

``joinSpec`` を持たない場合：

   If a JoinNode does not have a ``joinSpec``, then this is equivalent to a
   ``joinSpec`` Expression with the Boolean operator “and.”

つまり、暗黙の既定 ``joinSpec`` 条件は、``incoming`` ActivityEdge のそれぞれに少
なくとも一つのトークンが与えられていることだ。

JoinNode の ``joinSpec`` が真の場合に何が起こるのか：

   If the (implicit or explicit) ``joinSpec`` of a JoinNode evaluates to true,
   then tokens are offered on the ``outgoing`` ActivityEdge of the JoinNode
   according to the following rules:

#. ``incoming`` 辺に供給されるトークンがすべて制御トークンである場合、その一つが
   ``outgoing`` 辺に供給される。
#. ``incoming`` 辺に供給されるトークンの一部が制御トークンで、多がオブジェクト
   トークンである場合、オブジェクトトークンのみが ``outgoing`` 辺に与えられる。

      Tokens are offered on the ``outgoing`` edge in the same order they were
      offered to the join. If ``isCombinedDuplicate`` is true for the JoinNode,
      then before object tokens are offered to the ``outgoing`` edge, those
      containing objects with the same identity are combined into one token.

この規則を同じ ``incoming`` 辺から供給される複数トークンの場合を含め、JoinNode
に供給されるトークンすべてに適用する。

トークンが出発辺に供給されると何が起こるか：

   If any tokens are offered to the ``outgoing`` ActivityEdge of a JoinNode,
   they shall be accepted by the target or rejected for traversal over the edge
   (e.g., due to a failed guard) before any more tokens are offered to the
   ``outgoing`` edge.

* トークンが縦断拒否された場合、それらはもはや ``outgoing`` 辺に供給されないもの
  とする。
* JoinNode がその ``outgoing`` 辺でトークンを供給することを遮断されている場合、
  不要な ``joinSpec`` 評価を省略することが許される。

15.3.3.5 Merge Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A MergeNode is a control node that brings together multiple flows without
   synchronization.

* MergeNode には厳密に一つの ``outgoing`` ActivityEdge があるものとする。
* MergeNode の ``incoming`` と ``outgoing`` の辺の型は一致しているものとする。
  MergeNode の ``outgoing`` 辺が ControlFlow ならば ``incoming`` 辺はすべて
  ControlFlows でなければならず、``outgoing`` 辺が ObjectFlow ならば
  ``incoming`` 辺はすべて ObjectFlows でなければならない。

MergeNode の ``incoming`` 辺に供給されたトークンはすべて、``outgoing`` 辺に供給
される。流れの同期またはトークンの結合はない。

15.3.3.6 Decision Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A DecisionNode is a ControlNode that chooses between ``outgoing`` flows.

DecisionNode は少なくとも一つ、多くても二つの ``incoming`` ActivityEdge と、少な
くとも一つの ``outgoing`` ActivityEdge を持たなければならない。

二つある到着辺は平等に扱わない：

   If it has two ``incoming`` edges, then one shall be identified as the
   ``decisionInputFlow``, the other being called the :dfn:`primary incoming
   edge`.

DecisionNode の ``incoming`` 辺が一つだけの場合、それが主到着辺となる。

* 主到着辺が ControlFlow である場合、``outgoing`` 辺はすべて ControlFlow でなけ
  ればならない。
* 主到着辺が ObjectFlow である場合、``outgoing`` 辺はすべて ObjectFlow でなけれ
  ばならない。

DecisionNode はトークンをどう処理するか：

   A DecisionNode accepts tokens on its primary incoming edge and offers them to
   all its ``outgoing`` edges. However, each token offered on the primary
   incoming edge shall traverse at most one ``outgoing`` edge. Tokens are not
   duplicated.

DecisionNode の ``outgoing`` 辺のいずれかにガードがある場合、これらのガードは各
到着トークンに対して評価される。

* 評価順序は定義されておらず、同時に評価されることがある。
* DecisionNode の主到着辺が ObjectFlow で、DecisionNode が ``decisionInput`` ま
  たは ``decisionInputFlow`` を持っていない場合、到着オブジェクトトークンに含ま
  れる値は、``outgoing`` ObjectFlow のガードの評価に使用されることがある。

``decisionInputFlow`` の役割：

   If a DecisionNode has a ``decisionInputFlow``, then a token must be offered
   on both the primary incoming edge and the ``decisionInputFlow`` before the
   token from the primary incoming edge is offered to the ``outgoing`` edges.

``decisionInput`` という Bahavior があることがある：

   If a DecisionNode has a ``decisionInput``, then this must be a Behavior with
   a return Parameter and no other output Parameters.

この Behavior はトークンが入力されるたびに呼び出され、Behavior が返す結果は出発
辺の ``guards`` の評価で利用できる。

``decisionInput`` は副作用を持ってはならない。オブジェクトを修正してはならない
が、例えば、オブジェクトから属性値を取得するために、あるオブジェクトから別のオブ
ジェクトに回航することはできる。

   If the primary incoming edge of a DecisionNode is a ControlFlow, and the
   DecisionNode has a ``decisionInput`` but not a ``decisionInputFlow``, then
   the ``decisionInput`` shall have no input Parameters.

ところが、DecisionNode に ``decisionInput`` と ``decisionInputFlow`` の両方があ
る場合、``decisionInput`` には入力 Parameter が一つあり、Behavior が呼び出される
と、``decisionInputFlow`` で供給されるオブジェクトトークンに含まれる値がこの
Parameter を介して渡されるものとする。

DecisionNode の主到着辺上に供給されるトークンは流通経路に制限がある：

   A token offered on the primary incoming edge of a DecisionNode shall not
   traverse any ``outgoing`` edge for which the ``guard`` evaluates to false.

* ``guard`` を持たないか、または真と評価される ``guard`` を持つ出発辺が複数存在す
  る場合、到着トークンはこれらの辺の高々一つを渡らなければならない。
* 遮断されていない出発辺のちょうど一つの対象がトークンを受理する場合、トーク
  ンは対応する辺を通過し、他のすべての供給は撤回される。
* 複数の複数が同時にトークンを受理した場合、トークンは受理した複数に対応する辺の
  一つだけを渡る。どの辺を渡るかはこの仕様では決定されない。

非決定的な挙動を回避するべく、設計者は ``incoming`` トークンそれぞれに対して高々
一つの ``guard`` が真であると評価されるようになるべく取り決めることだ。

真偽テストの短絡評価が認められている：

   If it can be ensured that only one ``guard`` will evaluate to true, a
   conforming implementation is not required to evaluate the ``guards`` on all
   outgoing edges once one has been found to evaluate to true.

DecisionNode 限定で ``else`` という定義済み ``guard`` が使われることがある：

   For use only with DecisionNodes, a predefined ``guard`` “else” (represented
   as an Expression with “else” as its operator and no operands) may be used for
   at most one ``outgoing`` edge. This guard evaluates to true only if the token
   is not accepted by any other ``outgoing`` edge from the DecisionNode.

15.3.4 Notation
----------------------------------------------------------------------

15.3.4.1 Initial and Final Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Figure 15.27 InitialNode notation

InitialNodes は黒塗りの丸として記す。

   Figure 15.28 FinalNode notation

* ActivityFinalNodes は白丸に囲まれた黒丸として記す。
* FlowFinalNodes はバツが内側にある丸として記す。

15.3.4.2 Fork and Join Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Figure 15.29 ForkNode and JoinNode notation

ForkNode と JoinNode の両者に対する表記法は、単に線分だ。この線分に
``outgoing``/``incoming`` ActivityEdges の記号を必要に応じて接続する。

   Figure 15.30 joinSpec notation

JoinNode 上の ``joinSpec`` は JoinNode 記号の近くの註釈で示される。

.. code:: bnf

   <join-spec-annotation> ::= ‘{’ ‘joinSpec’ ‘=’ <value-specification> ‘}’

..

   Figure 15.31 Combined JoinNode/ForkNode notation

JoinNode と ForkNode の機能はこの図のように同じ節点記号を使って組み合わせること
が可能だ。

   This notation maps to a model containing a JoinNode with all the ``incoming``
   ActivityEdges shown in the diagram and one ``outgoing`` ActivityEdge to a
   ForkNode that has all the ``outgoing`` ActivityEdges shown in the diagram.

15.3.4.3 Merge Nodes and Decision Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Figure 15.32 MergeNode notation

MergeNodes と DecisionNodes の記法は菱形だ。

* MergeNode には二つ以上の ``incoming`` ActivityEdges および単一の ``outgoing``
  ActivityEdge が必要だ。
* DecisionNode には単一の ``incoming`` ActivityEdge （``decisionInputFlow`` の可
  能性を除く）と、複数の ``outgoing`` ActivityEdges が必要だ。

   Figure 15.33 DecisionNode notation

* ``decisionInput`` はキーワード ``«decisionInput»`` と共に註釈の記法で示す。
* ``decisionInputFlow`` はその流れを註釈するキーワード ``«decisionInputFlow»``
  によって識別される。

   Figure 15.34 Combined MergeNode/DecisionNode notation

MergeNode と DecisionNode の機能は同じ節点記号を用いることで組み合わせることが可
能だ。``incoming`` 流れの高々一つが ``decisionInputFlow`` として註釈されることが
ある。

   This notation maps to a model containing a MergeNode with all the
   ``incoming`` edges shown in the diagram and one ``outgoing`` edge to a
   DecisionNode that has all the ``outgoing`` edges shown in the diagram.

15.3.5 Examples
----------------------------------------------------------------------

15.3.5.1 Initial Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

黒丸ノード。

   Figure 15.35 InitialNode example

Activity の実行の開始時点において、InitialNode は ``Receive Order``
ExecutableNode に制御を渡す。

15.3.5.2 Fork and Join Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

棒ノード二種。

   Figure 15.36 ForkNode example

``Fill Order`` が完了したときに、ForkNode は ``Ship Order`` と ``Send Invoice``
の両方に制御を渡す。

   Figure 15.37 JoinNode example

JoinNode は ``Ship Order`` と ``Send Invoice`` の処理を同期するのに使われる。両
方が完了したときに ``Close Order`` に制御を引き渡す。

   Figure 15.38 ``joinSpec`` example

自動販売機の制御が ``Dispense Drink`` に引き渡されるには、この ``joinSpec`` にあ
る条件が満たされる必要がある：

   .. code:: text

      {joinSpec =
       A and B
       and the total coin value
       inserted is >= drink price}

15.3.5.3 Merge and Decision Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

菱形ノード二種。

   Figure 15.39 MergeNode example

``Buy Item`` と ``Make Item`` のどちらか一方または両方共が実行されたのかもしれ
ない。

場合によっては ``Ship Item`` が二度実行される：

   As *each* completes, control is passed to Ship Item. That is, if only one of
   Buy Item or Make Item completes, then Ship Item is executed only once; if
   both complete, Ship Item is executed twice

   Figure 15.40 DecisionNode example

角括弧を用いることで分岐条件を柔軟に表現できる。

   Figure 15.41 DecisionNode example with ``decisionInput``

``decisionInput`` の註釈に分岐条件を書き下している。

   As the item has been removed from inventory, the reorder level should also be
   checked; and if the actual level falls below a pre-specified reorder point,
   more of the same type of item should be reordered.

15.3.5.4 Final Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

目玉とマルバツノード。

   Figure 15.42 ActivityFinalNode example

``Close Order`` 完了時に FinalNode に至る。Activity は停止する。

   Figure 15.43 ActivityFinalNode example

開始直後の ForkNode で二つの concurrent flows が始まる。

   The first one to reach the ActivityFinalNode aborts the other.

とにかくどちらの流れを経ても FinalNode に至る。

   Figure 15.44 ActivityFinalNode example

* FinalNode を一つにまとめても図の意味は変わらない。
* ``Notify of Modification`` からは FinalNode に至らないことに注意（なぜか）。

   Figure 15.45 FlowFinalNode example

これは ``Build`` Component が反復的に実行すると解釈する。それと同時？に
``Install`` Component が実行していることに注意。

   Figure 15.46 FlowFinalNode and ActivityFinalNode example

* JoinNode は ``Ship Order`` と ``Accept Payment`` の両方が完了したときに
  MergeNode に制御が渡されることを示す。
* 注文が拒否されるたびに、制御は ``Close Order`` に渡される。
* ``Close Order`` が完了すると、制御は ActivityFinalNode に渡される。

ActivityFinalNode に至るとすると、左側のループはもはや実行中ではないはず？

15.3.5.5 Various Control Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Figure 15.47 ControlNode examples (with accompanying actions and control
   flows)

この Activity には既視感がある。

15.4 Object Nodes
======================================================================

15.4.1 Summary
----------------------------------------------------------------------

   An ObjectNode is a kind of ActivityNode (see sub clause 15.2.2) used to hold
   value-containing object tokens during the course of the execution of an
   Activity.

本節ではその具象型三種 ActivityParameterNodes, CentralBufferNodes,
DataStoreNodes ばかりでなく、ObjectNode 一般の話を述べる。

ObjectNode の四番目の種類である Pins は、常に Actions に関連付けられる。
:doc:`./ch16-actions` で述べられる。

15.4.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 15.48 Object Nodes

ObjectNode と関連する要素の役割を理解したい。

15.4.3 Semantics
----------------------------------------------------------------------

15.4.3.1 Object Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ObjectNode は Activity の実行中にオブジェクトトークンを保持する。

* ObjectNode が保持するトークンは ``incoming`` ActivityEdges から到着する。
* ObjectNode が保持するトークンは ``outgoing`` ActivityEdges を出発することが許
  される。
* トークンは ``outgoing`` 辺の一つしか通過していくことが許されない。

ObjectNode は値が同じオブジェクトトークンを複数含められる。そのようなトークンは
通常は結合しない。

   ObjectNodes are TypedElements (see sub clause 7.3).

* ObjectNode に ``type`` が指定されている場合、ObjectNode が保持するオブジェクト
  トークンはどれも ObjectNode の ``type`` に適合する値でなければならない。
* 指定されていない場合、値はどんな ``type`` の値であってもよい。
* 空トークンは任意の型であるとみなせる。

ObjectNodes は States の ``inState`` 集合を指定することも許される。

   If such a set is specified, then any object token held by the ObjectNode
   shall have a value with a ``type`` that has or inherits a StateMachine as its
   ``classifierBehavior`` that has all of the states in the ``inState`` set, and
   whose instance for the given value shall be in a state configuration
   containing all of the States specified in the ``inState`` set

ObjectNode はその ``upperBound`` で指定されている場合、それを超える個数のトーク
ンを含むことは許されない。また、この ValueSpecification は UnlimitedNatural 値に
評価されるものとする。

* ``upperBound`` は、トークンが ObjectNode に供給されるたび、または ObjectNode
  から削除されるたびに評価される。ObjectNode がすでに保持しているトークンの数が
  評価された ``upperBound`` 以上である場合、ObjectNode は保持しているトークンの
  いくつかが削除されるまで、それ以上のトークンを受理しないものとする。一つ以上の
  トークンが削除された結果、保持しているトークンの数が評価された ``upperBound``
  値以下になった場合、ObjectNode は ``upperBound`` の限界まで保留中の供給を受理
  することが許される。
* ``upperBound`` が ``*`` と評価された場合、ObjectNode が保持できるトークン数に
  制限はない。

ObjectNode の ``ordering`` は、この節点が保持するトークンを ``outgoing``
ActivityEdges に供給する順序を指定する。この特性には次の値の一つをとる：

``unordered``
   順序を定義しない。
``FIFO``
   ObjectNode が受理した順番で ``outgoing`` 辺に与える。
``LIFO``
   ObjectNode が受理したのと逆の順番で ``outgoing`` 辺に与える。
``ordered``
   ``selection`` Behavior を用いた設計者定義による順序とする。

``selection`` の仕様：

* ``ordering == ordered`` であるとき、かつそのときに限って、ObjectNode には
  ``selection`` Behavior があるものとする。
* ``selection`` は入力 Parameter と出力 Parameter を一つずつ持つものとする。

  * この入力 Parameter は多重度 ``0..*``, unordered, non-unique である必要があ
    る。
  * この出力 Parameter は多重度が ``1..1`` である必要がある。

* ObjectNode が型付けられていない場合、これらの Parameters も片付けられていない
  ものとする。そうでない場合、入力 Parameter と出力 Parameter はそれぞれ
  ObjectNode と同じ ``type`` か上位型を持つものとする。

``selection`` の実行：

   The ``selection`` Behavior of an ObjectNode is executed whenever a token is
   to be offered to the ``outgoing`` edges of the node. The values contained in
   all the object tokens held by the Object Node are passed as input to the
   Behavior invocation.

この Behavior はこれらの値のいずれかを選択して返す。この値を含むオブジェクトトー
クンが ObjectNode の ``outgoing`` 辺に供給される。

ObjectNode の ``selection`` Behavior はその ``outgoing`` ObjectFlows の
``selection`` Behavior によって上書きされる (15.2.3)。

トークンの追い越しに関する記述があるが、よくわからないので省略。

ControlFlow はある性質の ObjectNode に出入りする：

   If ``isControlType`` = true for an ObjectNode, ControlFlows may be
   ``incoming`` to and ``outgoing`` from the ObjectNode, objects tokens can come
   into or go out of the ObjectNode along ControlFlows, and these tokens can
   flow along ControlFlows reached downstream of the ObjectNode.

15.4.3.2 Activity Parameter Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Activity は Behavior の一種なので (13.2) Parameters があることがある。

   When the Activity is invoked, values may be passed into the Activity
   execution on input Parameters (i.e., those with direction in or inout) and
   values may be passed out of the Activity execution on output Parameters
   (i.e., those with direction inout, out or return).

Activity ではその入出力は ActivityParameterNodes を用いて処理される。

* ActivityParameterNode それぞれはその節点を所有する Activity の Parameter 一つ
  に関連付けられる。
* ActivityParameterNode の ``type`` は関連付けられた Parameter の ``type`` と同
  じであるものとする。

ActivityParameterNode はすべてが ``incoming`` ActivityEdges であるか、すべてが
``outgoing`` ActivityEdges であるかのどちらかであるものとする。

   An ActivityParameterNode with ``outgoing`` edges is an input
   ActivityParameterNode, while an ActivityParameterNode with ``incoming`` edges
   is an output ActivityParameterNode.

Activity が持つ ActivityParameterNodes の内訳：

   An Activity shall have one ActivityParameterNode corresponding to each in,
   out, or return Parameter and two ActivityParameterNodes for each inout
   Parameter.

* 入力 Parameter は 出力 ActivityParameterNode に関連付けてはならない。
* 出力または戻り Parameter は入力 ActivityParameterNode に関連付けてはならない
  （辺が接続されていない ActivityParameterNode に関連付けることは許される）。
* 出力 Parameter は高々一つの入力 ActivityParameterNode と高々一つの出力
  ActivityParameterNode に関連付けられなければならない。

オブジェクトトークンが出力 ActivityParameterNode に流れ込むことが考えられる：

   An output ActivityParameterNode accepts all tokens offered to it, which are
   then placed onto the node. If an output ActivityParameterNode is associated
   with a non-streaming Parameter, then, when the execution of the containing
   Activity completes, the values contained in the object tokens held by the
   ActivityParameterNode are passed out of the execution on the Parameter.

この Parameter に順序が付けられている場合、その値は ActivityParameterNode のトー
クン順序に対応して順序が付けられる。

Parameter が streaming の場合はどうか。入力 ActivityParameterNode の場合は：

   If an input ActivityParameterNode is associated with a streaming Parameter,
   then, whenever a new value is posted to the Parameter, that value is wrapped
   in an object token, placed on the ActivityParameterNode and offered to all
   outgoing edges.

出力 ActivityParameterNode の場合は上記の反対の工程が起こる。

15.4.3.3 Central Buffer Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

CentralBufferNode は ``incoming`` ObjectFlows と ``outgoing`` ObjectFlows の間の
緩衝材として機能する。オブジェクトトークンを溜めこんでおく場所だ。

15.4.3.4 Data Store Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A DataStoreNode is a CentralBufferNode that holds its object tokens
   persistently while its activity is executing.

DataStoreNode が保持するオブジェクトトークンは下流の ObjectNode が受理すると、そ
のトークンはまず通常の CentralBufferNode の意味で DataStoreNode から取り除かれ
る。そのとき、オブジェクトトークンはコピーされてすぐにこの DataStoreNode に戻さ
れる。

   Thus, the values held by a DataStoreNode appear to persist for the duration
   of each execution of its containing activity, even as tokens move downstream
   from the node.

DataStoreNode がオブジェクトトークンを受理するとき、そのトークンがすでにその節点
が保持するトークンに含まれるオブジェクトと同一の ID を有するオブジェクトを含む場
合、重複するオブジェクトトークンが DataStoreNode 上に配置されないものとする。正
規の CentralBufferNode とは異なり、DataStoreNode はオブジェクト群を一意に含む。

   The ``selection`` and ``transformation`` Behaviors on ``outgoing``
   ObjectFlows can be used to get information out of a DataStoreNode as if a
   query were being performed.

例えば、``selection`` は取得するオブジェクトを特定し、``transformation`` はその
オブジェクトの属性値を取得可能だ。

15.4.4 Notation
----------------------------------------------------------------------

15.4.4.1 Object Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Figure 15.49 ObjectNode notations

* ObjectNodes は矩形で示す。
* 節点をラベル付ける名前を記号の内側に置き、名前は ObjectNode の ``type`` を示す
  か、``name:type`` の形式で節点の ``name`` と ``type`` を示す。
* その型がコレクションを表現する ObjectNode はそのようにラベルすることが許され
  る。
* 型として Signal を持つ ObjectNode は矩形ではなく、初心者マークみたいな多角形で
  示す。左が凹で右が凸。

..

   Figure 15.50 ObjectNode annotations

ObjectNode に States の ``inState`` 集合がある場合、この集合にある States の名前
は付きカンマ区切りリストとして ObjectNode の名前の下の中括弧内に記述される。

   Values for ``upperBound``, ``ordering`` and ``isControlType`` are notated by
   placing an annotation with the following form beneath the ObjectNode symbol
   (as shown in Figure 15.50):

.. code:: bnf

   <object-node-annotation> ::= ‘{’ <object-node-property> ( ‘,’ <object-node-property> )* ‘}’
   <object-node-property> ::= ‘upperBound’ ‘=’ <value-specification> |
                              ‘ordering’ ‘=’ <object-node-ordering-kind> |
                              ‘controlType’
   <object-node-ordering-kind> ::= ‘unordered’ | ‘ordered’ | ‘FIFO’ | ‘LIFO’

..

   Figure 15.51 Specifying selection behavior on an ObjectNode

ObjectNode の ``selection`` Behavior は ObjectNode 記号に付属するキーワード
``«selection»`` を持つ註釈記号の中で指定される。

15.4.4.2 Activity Parameter Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ActivityParameterNode は ObjectNode として記されるが、付随する Parameter の完
全テキスト仕様が普通の名前・型ラベルの代わりに ActivityParameterNode をラベル
付けするのに用いられる。

   Figure 15.52 Notation for stream and exception parameters

* ``streaming`` Parameter に関連する ActivityParameterNode の記法は、文字列
  ``{stream}`` を節点記号の近くに記すものとする。
* 例外 Parameter に関連する ActivityParameterNode の記法は、小さな三角を節点
  記号の近くに記すものとする。

   Figure 15.53 Presentation option for flows between pins and parameter nodes

* Activity の上側の表現と下側の表現は等価だ。
* Parameters は Activity の境界でやり取りする。

15.4.4.3 Central Buffer and Data Store Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Figure 15.54 Optional CentralBufferNode notation

CentralBufferNode 記号はキーワード ``«centralBuffer»`` を含んでもよい。

   Figure 15.55 DataStoreNode notation

DataStoreNode はキーワード ``«datastore»`` が付いた ObjectNode として記す。

15.4.5 Examples
----------------------------------------------------------------------

15.4.5.1 Activity Parameter Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Figure 15.56 Example of ActivityParameterNodes for regular and exception
   Parameters

ここで見るべきは境界上の節点のみ。``Rejected Computer`` に三角が付いているので、
この節点が例外だ。

   Figure 15.57 Example of ActivityParameterNodes for streaming Parameters

Fig. 15.55 と似ているが右側が異なる。

* 入出力どちらの ActivityParameterNodes でも ``streaming`` たり得る。
* ちなみに ``streaming`` であることと例外であることは両立してはならない。

15.4.5.2 Central Buffer and Data Store Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Figure 15.58 CentralBufferNode example

予備部品と採用部品の区別法を示していないことに注意。

   All the parts that are not used will be packed as spares, and vice versa,
   because each token can only be drawn from the CentralBufferNode by one
   outgoing edge. The choice in this example is non-deterministic.

   Figure 15.59 DataStoreNode example

* ``selection`` Behavior の説明が欲しい。
* ``Once a year`` という記号があるが、これは Timer の類だろう。

AcceptEventAction がその年次制御トークンを生成すると、JoinNode の結合条件が満た
され、``Personnel Database`` からの出発辺が ``{weight=*}`` であるため、シリアラ
イズされたすべての従業員レコードのオブジェクトトークンが ``Review Employee`` に
流れることが可能だ。

15.5 Executable Nodes
======================================================================

15.5.1 Summary
----------------------------------------------------------------------

   An ExecutableNode is a kind of ActivityNode that may be executed as a step in
   the overall desired behavior of the containing Activity.

一般的に、Activity 内の ControlNodes と ObjectNodes は、シーケンスの制御と
Activity 内の ExecutableNodes 間のデータの流れを管理するために主に存在する。

ExecutableNodes の具象型はすべてが Actions (:doc:`./ch16-actions`) だ。本節では
Activity 内の ExecutableNodes の一般的な意味と、ExecutableNode に
ExceptionHandler を付属させる能力について述べられる。

15.5.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 15.60 Executable Nodes

* ExecutableNode は一つの ObjectNode に関連する ExceptionHandlers を所有する。
* ExceptionHandler は Classifiers を例外の型として関連付ける。

15.5.3 Semantics
----------------------------------------------------------------------

15.5.3.1 Executable Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   An ExecutableNode is an ActivityNode that carries out a substantive
   behavioral step of the Activity that contains it.

ExecutableNode の ``incoming`` と ``outcoming`` はすべて ControlFlow でなければ
ならない。

ExecutableNode はデータを消費したり生産したりすることがあるが、そうするには関連
する ObjectNodes を通じたうえでなければならない。

   An ExecutableNode shall not execute until all ``incoming`` ControlFlows (if
   any) are offering tokens. That is, there is an implicit join on the
   ``incoming`` Control Flows.

ExecutableNode は実行を開始する前に、``incoming`` ControlFlows から供給される
トークンすべてを受理する。複数のトークンが供給されている場合、すべて消費する。

   While the ExecutableNode is executing, it is considered to hold a single
   control indicating it is execution.

場合によっては ExecutableNode 一つの複数同時実行が一斉に進行することがある
(16.2)。この場合 ExecutableNode は同時実行それぞれに対して制御トークンを一つ保持
する。

制御トークンの行方：

   When an ExecutableNode completes an execution, the control token representing
   that execution is removed from the ExecutableNode and control tokens are
   offered on all ``outgoing`` ControlFlows of the ExecutableNode.

つまり、ExecutableNode から ``outgoing`` ControlFlows への制御の流れの暗黙の分岐
が存在する。

15.5.3.2 Exceptions and Exception Handlers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

例外は実行の完了様式が正常ではないことを識別するために用いられる値だ。
ExecutableNode の実行中に例外が発生し、この実行内で処理されない場合、実行は停止
され、この例外が当 ExecutableNode の外部へと伝わる。

ExecutableNode は例外処理機能を有することがある：

   An ExecutableNode may have one or more ExceptionHandlers that are used to
   deal with exceptions that may be propagated out of the ExecutableNode, which
   is the ``protectedNode`` of those ``handlers``.

例外が ``protectedNode`` から伝わると、この ``handlers`` 集合は例外に合致する処
理者を探す。

* ``handler`` は例外の ``type`` がその ``exceptionTypes`` の一つと同じか、または
  その派生型である場合に合致する。
* 合致する場合、``handler`` は例外を捕捉する。
* 複数の合致がある場合、厳密に一つの ``handler`` が捕捉するが、どれであるのかは
  定義されない。

例外を捕捉すると何が起こるか：

   If an ExceptionHandler catches an exception, the exception is wrapped in an
   object token that is placed on the ``exceptionInput`` ObjectNode for the
   handler. The ``handlerBody`` of the ExceptionHandler is then executed.

``handlerBody`` の実行は ``exceptionInput`` を介して捕捉した例外を入手することが
許される。

例外が処理されると次のようにして制御トークンが供給される：

   When the ``handlerBody`` of an ExceptionHandler completes execution after an
   exception is caught, control tokens are offered on the ``outgoing``
   ControlFlows of the ``protectedNode`` of the ExceptionHandler, in exactly the
   same way as if the ``protectedNode`` completed normally.

``protectedNode`` が OutputPins を持つ Action (16.2) である場合、``handlerBody``
も合致する OutputPins を持つ Action でなければならず、``handlerBody`` の
OutputPins に置かれたトークンはすべて ``protectedNode`` の OutputPins に転送され
る。

``handlerBody`` は孤立点のようなものだ：

   A ``handlerBody`` shall have no ``incoming`` or ``outgoing`` ActivityEdges.
   An ExecutableNode acting as a ``handlerBody`` is not enabled to execute in
   any case other than in response to an exception being caught by its handler.

``handlerBody`` に対する所有権：

   The ``handlerBody`` of an ExceptionHandler shall have the same owner as the
   ``protectedNode`` of the ExceptionHandler and shall own the
   ``exceptionInput`` of the ExceptionHandler.

``exceptionInput`` の型は

* 型付けられていないか、
* ExceptionHandler の ``exceptionTypes`` すべてと同じ型か、
* ExceptionHandler の ``exceptionTypes`` すべての汎化型だ。

..

   Typically, the ``handlerBody`` will be a StructuredActivityNode and the
   ``exceptionInput`` will be an InputPin for it (see sub clause 16.11 on
   StructuredActivityNodes).

例外を処理しないとようにするとこうなる：

   If an ExecutableNode propagates an exception and the node either has no
   ``handlers``, or no ``handler`` matches the propagated exception, then the
   exception continues to propagate outward. If the exception is not caught at
   all within the execution of the containing Activity, then the Activity
   execution terminates and the exception is propagated out of the Activity.

Activity が同期的に呼び出された場合、例外は呼び出し元に伝わる。非同期的に呼び出
された場合、例外は失われる。

15.5.4 Notation
----------------------------------------------------------------------

15.5.4.1 Executable Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Figure 15.61 ExecutableNode notation

ExecutableNode は一般的には丸い角の矩形として描かれる。

Actions のさまざまな種類に対するより特殊な記法は :doc:`./ch16-actions` で述べら
れる。

15.5.4.2 Exception Handlers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Figure 15.62 ExceptionHandler notation

ExceptionHandler は稲妻記号で描かれる。

* 矢印の始点は ``protectedNode`` だ。
* 稲妻の隣に ``exceptionType`` の名前を記す。
* 矢印の終点 ``exceptionInput`` 節点は小さい正方形で示す。
* 複数の ExceptionHandlers を同じ ``protectedNode`` に取り付けてもかまわない。

   Figure 15.63 Alternative ExceptionHandler notation

矢印自体を稲妻にする代わりに、ジグザグマークを普通の矢印に添えて ExceptionHandle
を表記としてもよい。

15.5.5 Examples
----------------------------------------------------------------------

   Figure 15.64 ExceptionHandler example

まず逆行列を求め、それからベクトルを乗じることで別のベクトルを得る。

行列が非正則ならば、逆行列演算は失敗するはずで ``SingularMatrix`` 例外が送出され
る。この例外は ``exceptionType`` ``SingularMatrix`` に対する ExceptionHandler に
より処理されるが、それは ``Substitute Vector1 Action`` を含む領域を実行する。

逆行列演算またはベクトル乗算のどちらかの処理中に ``Overflow`` 例外が発生すると
``Substitute Vector1 Action`` を含む領域が実行される。

行列演算が例外なしで完了するか、ExceptionHandlers のうちの一つが引き起こしたかに
関わらず、次に動作 ``Print Results`` が実行される。

15.6 Activity Groups
======================================================================

15.6.1 Summary
----------------------------------------------------------------------

   ActivityGoups are a grouping constructs for ActivityNodes and ActivityEdges.

節点と辺は複数の集団に所属することが可能だ。

本節では ActivityGroup の二つの具象型、 ActivityPartitions と
InterruptibleActivityRegions について述べる。

StructuredActivityNode は ActivityGroup の第三の種類だが、Actions でもある。
:doc:`./ch16-actions` で議論する。

15.6.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 15.65 ActivityGroups

* ActivityGroup の特殊型として ActivityPartition と InterruptibleActivityRegion
  がある。
* ActivityGroup は ``subgraph`` を表現するためのものだろう。

15.6.3 Semantics
----------------------------------------------------------------------

15.6.3.1 Activity Partitions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ActivityPartition の定義：

   An ActivityPartition is a kind of ActivityGroup for identifying ActivityNodes
   that have some characteristics in common. ActivityPartitions can share
   contents.

* 多くの場合、業務モデルにおける組織単位に相当する。
* Activity の節点間で特性や資源を割り当てるために用いられることがある。

ActivityPartitions はモデルのトークン流通に影響を及ぼさない。役目としては：

   They constrain and provide a view on the Behaviors invoked due to the
   execution of the ``containedNodes`` and ``containedEdges`` of the partition,
   including Operation calls and Signal sends. This may be due not only to the
   execution of explicit InvocationActions (see sub clause 16.3) but also the
   implicit invocation of, e.g., ``transformation`` and ``specification``
   Behaviors.

この制約は次にあるように、仕切り ``represents`` 要素の種類によって異なる：

Classifier
   呼び出し先 Behaviors は ``represents`` の Classifier のオブジェクトが担う。

      The ``context`` of all invoked Behaviors shall be the Classifier.
      Operation calls and Signal sends within the partition shall target objects
      at runtime that are instances of the Classifier.

InstanceSpecification
   呼び出し先 Behaviors は ``represents`` の InstanceSpecification によりモデ
   ル化されるオブジェクトが担う。

   * 呼び出し先 Behaviors すべての ``context`` はこの InstanceSpecification の
     Classifier であるものとする。
   * 仕切り内の Operation 呼び出しと Signal 送信は InstanceSpecification によっ
     てモデル化されたオブジェクトを対象とするものとする。

Property
   呼び出し先 Behaviors は ``represents`` の Property が保持するオブジェクトが担
   う。

   * 仕切り内の Operation 呼び出しと Signal 送信は実行時にこの Property が保持す
     るオブジェクトを対象とする。
   * 呼び出しは各値に対して同時に行われたものとして扱われ、そのオブジェクトすべ
     てが完了するまで呼び出しは完了しない。

ActivityPartition は上に挙げた以外の他の種類の Elements を表現してもよいが、当仕
様書はそれらの意味を定義しない。

ActivityPartition は入れ子になり得る：

   An ActivityPartition may have ``subpartitions``. If an ActivityPartition has
   ``isDimension`` = true, then it is a dimension partition for its
   ``subpartitions``.

寸法仕切りは他の ActivityPartitions に含まれてはいけない。

ActivityPartition が Property を表現し、その ``subpartitions`` が
InstanceSpecifications を表現する場合、この InstanceSpecifications はその
Property が保持する値をモデル化するものとする。

* ``subpartitions`` で呼び出される Behaviors は、この ``subpartitions`` の
  InstanceSpecification と包含元 ActivityPartition の両方に対して要求される制約
  と合致しなければならない。例えば

  * 仕切りは呼び出された Behavior が実行される場所を表す。
  * ``subpartitions`` はこの Property に関する ``Chicago`` のような特定の値を表
    す。場所 Property は Activity を包含する ``context`` BehavioredClassifier の
    ``attribute`` であったり、この Activity 自体の ``attribute`` であったりす
    る。

ActivityPartition が Classifier の ``attribute`` である Property を表現し、別の
仕切りがこの Property を含むならば、その ``superPartition`` はその Classifier ま
たはその Classifier を ``type`` とする Property を表現するものとする。また、
``superPartition`` の外部でない ``subpartitions`` はすべて Classifier の
``attributes`` を表すものとする。

* 実行時において、``subpatitions`` にある Behaviors の呼び出しの対象は、
  ``superPartition`` が表す Classifier のオブジェクトと同じ ``attribute`` の値で
  なければならない。
* ``superPartition`` がこの Classifier を ``context`` とする包含 Activitity の
  ``partition`` である場合、実行時の実行 Activity の context object はこの
  ``superPartition`` が表す Classifier と同じオブジェクトであるものとする。

非外部 ActivityPartition が Classifier を表現し、別の仕切りに含まれている場合、
その ``superPartition`` もまた Classifier を表現するものとし、その
``subpartition`` の Classifier は次のどちらかでなければならない：

* ``superPartition`` が表現する Classifier の

  * ``nestedClassifier`` または
  * ``ownedBehavior``
* ``superPartition`` が表現する Classifier に関連付けられた複合 Association の端
  子

..

   If the latter, then, at runtime, the target for invocations of Behaviors in
   the ``subpartition``, including Operation calls and Signal sends, shall be
   considered to be an instance of the Classifier represented by the
   ``subpartition`` that is linked to an instance of the Classifier represented
   by the ``superPartition`` by the composition Association.

外部 ActivityPartition とは ``isExternal`` が真であるものだ。これは仕切りの構造
の規則に対する作為的な例外だ。

   For example, a dimension partition may have partitions showing the parts of a
   StructuredClassifier. It can then have an external partition that does not
   represent one of the parts, but a completely separate Classifier.

業務モデリングでは外部仕切りを使用して業務外部の実体を模倣できる。

   ActivityPartitions may be used in a way that provides enough information for
   review by high-level modelers, though not enough for execution. For example,
   if a partition represents a Classifier, then Behaviors invoked in that
   partition are the responsibility of instances of the Classifier, but the
   model may or may not say which instance in particular.

モデルがどれが特定のオブジェクトであるかを名言しないというのがミソだ。Operation
の呼び出しはその Classifier 上の Operation に限定されるが、この呼び出しへの入力
ObjectFlow は稼働中にどのオブジェクトを対象にするべきかを示すのには指定されない
かもしれない。

   Another option would be to use ActivationPartitions that represent ``parts``.
   Then, when the Activity executes in the context of a particular object, the
   parts of that object at runtime will be used as targets for the Operation
   calls and Signal sends, as described above.

15.6.3.2 Interruptible Activity Regions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

InterruptibleActivityRegion とは Activity の一部分の停止を支援する ActivityGroup
だ。

* InterruptibleActivityRegion は ActivityNodes しか含まない。
* InterruptibleActivityRegion はその ``source`` が領域内にあり、その ``target``
  が領域外にある特定の ActivityEdges を ``interruptingEdge`` として識別する。

..

   When a token offered along an interruptingEdge is accepted and traverses that
   edge, then the execution of all ``containedNodes`` of the region is
   terminated and all tokens are removed from them.

しかし、``interruptingEdge`` を流れるトークンは依然としてその ``target`` に到着
し、さらに領域内の ``source`` から領域外の ``target`` へ非割り込み辺を流れる供給
トークンも、たとえ流れる間に割り込みが起こっても、依然として``target``に到着す
る。

   AcceptEventActions in the region that do not have ``incoming`` edges are
   enabled only when a token enters the region, even if the token is not
   directed at the AcceptEventAction.

   Do not use an InterruptibleActivityRegion if it is not desired to abort all
   flows in the region in some cases.

例えば ``isSingleExecution`` が真である Activity において、トークンの流れの複数
が同じ Activity を流れることになる。この場合、トークンの一つが領域から離れるから
といって、領域内の流れのすべてを中止することはまず望ましくない。

   Arrange for separate invocations of the Activity to use separate executions
   of the Activity (i.e., ``isSingleExecution`` = false) when employing
   InterruptibleActivityRegions, so tokens from different invocations will not
   affect each other.

15.6.4 Notation
----------------------------------------------------------------------

15.6.4.1 Activity Partitions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ActivityPartition は、通常、水平または垂直の二本の平行線で表記され、一方の端の箱
には仕切りを示す名前を記す。

   Figure 15.66 ActivityPartition notations

これらの線に挟まれて置かれる ActivityNodes と ActivityEdges のいずれもがその仕切
りの中に含まれるとみなされる。この ActivityPartition の表記法は swimlane と俗に
言われる (a)。

``superPartition`` のさらなる仕切りとして ``subpartitions`` を表現すること
で階層的な仕切りを表現することができる (b)。

図式は多次元に分割することも可能で、各 swim cell は複数の仕切りの交差となる
(c)。

   The partitions within each dimension may be grouped into an enclosing
   activity partition with ``isDimension`` = true, whose name is the dimension
   name.

状況によっては、罫線による ActivityPartitions の図式化は現実的ではないことがあ
る。その場合には次に示す代替記法を検討する。

   Figure 15.67 ActivityPartition notations

a. 仕切りの名前を括弧付きで ActivityNode の名前の上に置く。
b. 外側の仕切りはキーワード ``«external»`` を付けてラベルする。

..

   When ActivityPartition swimlane notation is combined with the frame notation
   for Activity (see sub clause 15.2.4), the outside edges of the top level
   partition swimlanes can be merged with the Activity frame.

15.6.4.2 Interruptible Activity Regions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Figure 15.68 InterruptableActivityRegion

* InterruptableActivityRegion はその領域に含まれる節点の周囲に描かれる破線丸角矩
  形で記される。
* ``interruptingEdge`` は稲妻 ActivityEdge で表記される。

   Figure 15.69 InterruptableActivityRegion alternative notation

先述の通り ``interruptingEdge`` の矢印を真っ直ぐにしてジグザグマークを添えてもよ
い。

15.6.5 Examples
----------------------------------------------------------------------

15.6.5.1 Activity Partitions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Figure 15.70 ActivityPartitions using swimlane notation

いつもの例題に swimlanes を明記したもの。上段が ``Order Department`` の担当する
Activity の部分を含む。中段が ``Account Department`` で、下段が ``Customer``
だ。

仕切りをまたぐ ActivityEdges は、どの ``subpartitions`` にも含まれない。

   Figure 15.71 ActivityPartitions using annotation

先の見本から swimlane を外したもの。

丸括弧とキーワード ``«external»`` で所属する ActivityPartition がわかる。

   Figure 15.72 ActivityPartitions using multidimensional swimlane notation

``Make Payment`` は ``Seattle/Accounting Clerk`` swim cell に含まれているが、そ
の実行者と場所は指定されていない。キーワード ``«external»`` が付いている。

15.6.5.2 Interruptible Activity Regions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Figure 15.73 InterruptableActivityRegion example

InterruptableActivityRegion と凹五角形記号の組み合わせは使い易そうだ。

受注、記入、出荷の間に注文取消しが起こると、その流れは停止されて ``Cancel
Order`` が実行される。

   NOTE. If this happens after Fill Order is finished, invoicing might have
   already been initiated (due to the ForkNode after Fill Order).

このフローは InterruptibleActivityRegion の外側にあるため、``Ship Order`` が終了
しても ``Cancel Order`` 要求によって終了することはない。

15.7 Classifier Descriptions
======================================================================

機械生成による節。

15.8 Association Descriptions
======================================================================

機械生成による節。

.. include:: /_include/uml-refs.txt
