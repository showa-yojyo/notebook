======================================================================
16 Actions
======================================================================

.. contents::
   :depth: 4

16.1 Summary
======================================================================

   An :dfn:`Action` is the fundamental unit of behavior specification in UML.

* Action は入力の集合を取り、出力の集合を生じる。その集合の一方または両方が空で
  あることがある。
* Action が実行されるシステムの状態を変更するような Actions がある。

   Actions are contained in Behaviors, specifically Activities (as
   ExecutableNodes, see :doc:`Clause 15 <./ch15-activities>`) and Interactions
   (see :doc:`Clause 17 <./ch17-interactions>`). These Behaviors determine when
   Actions execute and what inputs they have.

* Action の抽象的構文と意味は Activity に依るところが大きい。
* Action の具体的構文は Activity 図にしか現れず、表記の一部は前章で定義されてい
  る。
* 本章では Action の構文と意味に焦点を当てる。:doc:`./ch15-activities` と一緒に
  読む必要がある。

16.1.1 Concrete Syntax
----------------------------------------------------------------------

.. admonition:: 読者ノート

   原書では節番号のレベルがおかしいので本ノートでは修正する。

UML 仕様書では Actions の図表記法を比較的最小限に抑えて設けている。ただし、適合
ツールは標準 Action 抽象構文に写像される、ツール固有の図表的またはテキスト的表現
を設ける場合がある。このような表現を具象構文と呼ぶ。

   Concrete syntaxes generally encompass both primitive Actions and the control
   mechanisms provided by Behaviors.

具象構文ではより高水準の構文を UML 抽象的構文で指定された Actions に写像すること
が可能だ。

   For example, creating an object may involve initializing attribute values or
   creating objects for mandatory Associations. The UML specification defines
   the CreateObjectAction to only create the object and requires further Actions
   to initialize attribute values and create objects for mandatory Associations.
   A concrete syntax can support a creation operation including initialization
   as a single unit as a shorthand for several underlying Actions.

一般は、具象構文は各 Action を一対一対応で実装することも、より上位の複合構文を定
義して設計者により多くの能力と利便性を供給することが可能だ。

この仕様では理解しやすく実装しやすい、根源的な動作概念に対する抽象構文と意味を与
える。設計者は精選した具象構文が備えるより高水準の構成要素で仕事することが可能
だ。

   The most primitive Actions in this specification are defined to enable the
   maximum range of concrete syntax mappings. Specifically, a primitive Action
   either carries out a computation or accesses object memory, but never both.

* この方法により、物理的な実装への清浄な写像が可能になる。
* さらに、データ構造を再編成しても計算の詳細に影響しない。

16.1.2 Execution Engines
----------------------------------------------------------------------

.. admonition:: 読者ノート

   原書では節番号のレベルがおかしいので本ノートでは修正する。

まず実行機関の定義から：

   An :dfn:`execution engine` is a tool that executes UML Actions. Actions are
   defined to enable the construction of various execution engines with
   different performance characteristics. An execution engine can optimize the
   execution of a model to meet specific performance requirements, so long as
   the engine stays within the semantics specified for Actions in UML.

例えば、UML の意味論で許される範囲内で最適化されていれば、次のそれぞれを行うもの
はすべて UML の実行機関として有効だ：

* 単一タスクの中で完全に逐次的に動作させる
* クラスの相互作用の大きさに基づいて、異なるプロセッサーにクラスを割り当てる
* クライアントサーバー、あるいは三層アーキテクチャーの中でクラスを割り当てる

..

   Modelers can provide “hints” to the execution engine when they have special
   knowledge of the domain solution that could be of value in optimizing the
   execution.

実行機関はこのようなヒントを検査したり強制したりする必要はない。

   When the execution of Actions violates aspects of UML structural semantics
   that constrain runtime behavior, the semantics of the Actions are left
   undefined.

例えば複合 Association を介してオブジェクトを複数の所有者に結合させることは未定
義だ。この Action を違法とする具象構文もあれば、単一の所有者が確立するまで認める
ものもある。

   However, in the execution of Actions the lower multiplicity bound is ignored
   and the semantics is still as defined. Otherwise, it is impossible to use
   Actions to pass through intermediate stages necessary to construct object
   configurations that satisfy multiplicity constraints.

設計者は最小の多重度が適用される点を決定しなければならないが、これらの点はどこに
でもあるわけではなく、そうでなければオブジェクト構成を変化することが不可能になる
ことだろう。

16.2 Actions
======================================================================

16.2.1 Summary
----------------------------------------------------------------------

Action と Pins の基本的な抽象構文を定義する。OpaqueAction 以外のさまざまな具体的
な Action は後で説明する。

16.2.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 16.1 Actions

Action は抽象型で、ExecutableNode から派生している。

* この図式では差し当たり OpaqueAction が Action の一つの具象型であることを表
  している。
* InputPin と OutputPin とに別々に関連させる。

Pin という ObjectNode と MultiplicityElement からの派生要素がある。

* Pin には {Input,Output}Pin の二つがある。
* InputPin には ActionInputPin と ValuePin の二つがある。ActionInputPin は
  Action を、ValuePin は ValueSpecification をそれぞれ関連させる。

16.2.3 Semantics
----------------------------------------------------------------------

16.2.3.1 Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   An Action is a fundamental unit of executable functionality contained,
   directly or indirectly, within a Behavior.

しかし Action の実行によって別の Behavior が呼び出されることがある (16.3) ことを
考慮すれば：

   An Action is therefore simple from the point of view of the Behavior
   containing it but may be complex in its effect and not atomic.

Action を含んでいる Behavior に ``context`` BehavioredClassifier がある場合、そ
のBehavioredClassifier はその Action に対する ``context`` Classifier でもある。

Action が実行されるときは ``context`` Classifier のオブジェクトの文脈で実行さ
れ、``context`` Classifier がない場合は Behavior の実行オブジェクトの文脈で直接
実行される。(13.2.3) 参照。

Action の入出力と Pin について：

   An Action may accept inputs and produce outputs, as specified by InputPins
   and OutputPins of the Action, respectively. Each Pin on an Action specifies
   the type and multiplicity for a specific input or output of that Action.

Action が実行する時間と、各実行が受理する入力が何であるのかは、Action の種
類、InputPins の特徴、その Action が使われる Behavior によって決定する。Action
が実行することが決定されると、その実行の一般的な手順は次のようになる：

#. Action の実行は、その InputPins すべてにおける入力データを、InputPin それぞれ
   の多重度 ``upper`` 個まで消費する。
#. Action は完了するまで実行を続行する。実行の詳細な意味と完了の定義は実行される
   Action の種類に依存する。
#. Action の実行が完了すると、OutputPins に出力データを渡して停止する。

   ただし、Action が streaming Paramters を持つ Behavior の呼び出しである場
   合、Action の実行は、完了前に streaming 出力 Parameters に対応する OutputPins
   にデータを配送することもできる。

   Action の実行が停止した後、その実行に使用された資源は、その実行を実装する実行
   機関により回収されることがある。このよう資源管理の詳細は本仕様では定義されな
   い。

Actions の意味の仕様上、Behaviors は同じ種類の Action を複数回再利用することが許
されていて、Action の意味はそれぞれの用法に個別に適用する。例えば：

   Activities may have multiple nodes that are instances of the same Action
   metaclass, and each instance has its own values for the properties described
   below, affecting the execution of that particular usage of the Action only.
   The same applies to Interactions with multiple ``actions`` that are instances
   of the same Action metaclass.

次の記述が困る：

   The phrase “an Action” or “the Action” in this specification refers to a
   single instance of an Action metaclass used in a Behavior, separate from the
   other instances of the same Action metaclass that may be used in the Behavior
   or other Behaviors.

局所再入不能と局所再入可能：

   If an Action is not locally reentrant (``isLocallyReentrant`` = false, the
   default), then no more than one execution of it may exist at any given time
   within a single execution of the containing Behavior.

同時に実行可能することが可能かどうかという視点だ。通常であれば Action の実行が開
始される場合でも、同じ Behavior の実行内で実行中の Action がすでにある場合は、新
しい実行が開始されない。

   On the other hand, if an Action is locally reentrant (``isLocallyReentrant``
   = true), then a new execution of it may begin any time the normal rules above
   allow it, even if there are one or more executions already ongoing within the
   same Behavior execution.

再入不能な CallAction の動作の性質：

   A CallAction for a non-reentrant Behavior (``isReentrant`` = true) will also
   act as if the CallAction were locally non- reentrant, whatever the value of
   the ``isLocallyReentrant`` property for the action.

このような Action は、この Action が呼び出さしたものだろうが、他の Action が呼び
出したものだろうが、現在実行中の Behavior がある場合は実行されない (13.2.3,
16.3.3)。

.. admonition:: 読者ノート

   引用文中の true は false ではないかと思う。

Action の局所事前・事後条件：

   The ``localPrecondition`` and ``localPostcondition`` for an Action are
   Constraints that should hold when an execution of an Action starts and
   completes, respectively.

``localPrecondition`` または ``localPostcondition`` はモデル作者が定義する
Constraint であるので、違反とは UML Action 実行の意味が未定義であることではな
い。

これらの条件がどのように強制されるかは、具体的には本仕様では定義されない。

   An execution engine may detect violations statically, if possible, or at
   runtime. The runtime effect of a violation may be an error that stops
   execution, just a warning, or no effect at all, as determined by the
   execution engine.

16.2.3.2 Opaque Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

OpaqueAction の定義。UML で opaque といえば意味するところは：

   An OpaqueAction is an Action whose specification may be given in a textual
   concrete syntax other than UML. An OpaqueAction may also be used as a
   temporary placeholder before some other kind of Action is chosen.

テキスト内容と解釈方法は ``body``, ``language`` で持つ：

   An OpaqueAction has a ``body`` that consists of a sequence of text Strings
   representing alternative means of specifying the behavior of the Action. A
   corresponding sequence of ``language`` Strings may be used to specify the
   languages in which each of the ``body`` Strings is to be interpreted.

* 言語を指定する必要はない。
* 言語が指定されていない場合、``body`` 文字列の解釈は、その形式や OpaqueAction
  の使用方法から暗黙の了解で決定される。

OpaqueAction の本文は複数あり得る：

   If an OpaqueAction has more than one ``body`` String, then any one of the
   ``bodies`` can be used to determine the behavior of the OpaqueAction. The UML
   specification does not determine how this choice is made.

16.2.3.3 Pins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pin の定義：

   A Pin represents an input to an Action or an output from an Action.

* InputPin が入力を表し、OutputPin が出力を表す。
* Action が所有する入力と出力の各集合は順序付けられている。
* Action の InputPins と OutputPins は Action の種類により決定される。

Pin は ObjectNode の一種なので (15.4)、指定された Type の値を含むオブジェクト
トークン (15.2) を保持する。

Action の InputPin のトークンに保持された値は Action の実行に対する入力データを
与え、Action の実行から生じた出力データはオブジェクトトークンで包み込まれて
Action の OutputPins に置かれる。

Pin の多重度について：

   A Pin is also a MultiplicityElement. The multiplicity bounds on a Pin
   constrain the total number of values that may be input or output by a single
   execution of an Action, not the number of tokens it contains (see the
   ``upperBound`` property inherited from ObjectNode).

継承属性 ``ordering`` と ``isOrdered`` について：

   Pin inherits both an ``ordering`` attribute from ObjectNode and an
   ``isOrdered`` attribute from MultiplicityElement. The values of these
   attributes may be set independently.

ただし、``isOrdered`` が真の場合、MultiplicityElement としての Pin 上の値の順序
は、値が Pin に配置された順序になる。ただし、``ordering`` 属性の値によって Pin
から値を取り出す順序が決まる。

例えば ``isOrdered`` が ``true`` で ``ordering`` が ``FIFO`` であると、
MultiplicityElement と同じ順序で Pin から値が取られるはずだ。

他方で ``isOrdered`` が偽の場合、値がその Pin に置かれる順序は不定であり、異なる
``orderings`` の効果は定義されない。

InputPin:

   An InputPin is a Pin that holds input values to be consumed by its Action.

* Action はその InputPins のうちの一つの値が、その ``lower`` 値より小さい場合、実
  行を開始することは不可能だ。
* ``upper`` 値はその Action の単一の実行によって InputPin から消費することが可能
  である値の最大数を決定する。

..

   Tokens consumed by an Action are immediately removed from its InputPins when
   the action begins an execution (except in some cases for
   StructuredActivityNodes, where tokens may remain on InputPins during the
   Action execution - see sub clause 16.11).

OutputPin:

   An OutputPin is a Pin that holds output values produced by an Action.

* 各実行について、Action はそれらの OutputPins の多重度の ``lower`` 値で要求され
  るのと同数以上の値をその Output に入れることができなければ、それ自身を停止する
  ことが不可能だ。以前の実行から OutputPins に残っていることがある値は、この最小
  多重度要件を満たすことには含まれない。
* Ation は一度の実行では、その OutputPin の多重度よりも多くの値を出力に入れるこ
  とは許されない。

ValuePins と ActionInputPins はどんなものか：

   ValuePins and ActionInputPins are InputPins, but are not used in the
   determination of whether an Action is enabled for execution.

* Action に実行を開始する他の方法がない場合、その入力に ValuePins または
  ActionInputPins を持つだけでは Action の実行は有効にならない。
* Action が他の手段で有効化した場合、Action が所有する ValuePins と
  ActionInputPins の指定に従って値が計算され、その結果が実行開始時に Action の入
  力として与えられる。

ValuePin は ValueSpecification を評価することで値を備える。Action が他の手段に
よって有効化されると、その ValuePin の ValueSpecification が評価され、その結果が
Action の実行開始時に入力として与えられる。

ActionInputPin:

   An ActionInputPin provides values by executing another Action. When an Action
   is enabled by other means, the ``fromActions`` on any ActionInputPins owned
   by the Action are also enabled.

``fromActions`` は ActionInputPins を所有する Action の前に実行されなければなら
ず、``fromAction`` の出力は対応する ActionInputPins に置かれる。

この処理は ``fromAction`` のどの ``ActionInputPin`` 上でも再帰する。
ActionInputPins がすべての入力に使用される場合、これは入れ子式の Action モデルで
ある木構造を形成し、Read{Variable,Self}Actions のような入力を持たない Action で
底を打つ。

16.2.3.4 Actions and Pins in Activities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Action およびその Pins が Activity に含まれる場合、トークンがいつこの Pins に出
入りし、いつこの Action が実行されるかは、Actions と同様に Activities の意味に
よって決定される。

Activity にある Action を実行する必要条件：

   Executing an Action in an Activity requires all of its InputPins to be
   offered all necessary tokens, as specified by their minimum multiplicity
   (except for the special cases of ActionInputPins and ValuePins, as discussed
   above).

* Action が実行を開始すると、その InputPins すべては、各 InputPin で許容される最
  大多重度まで、供給されたトークンを一度に受理する。

     InputPins cannot accept more tokens than will be consumed immediately by
     their Actions during a single execution. This ensures that InputPins on
     separate Actions competing for the same tokens do not accept any tokens
     they cannot immediately consume, causing deadlock or starvation as Actions
     wait for tokens accepted by the InputPins of other Actions but not used.

* ある Action の InputPins が受理したトークンは、他のどの Action も消費すること
  は不可能だ。

Activity 内の Action が実行を完了すると、その OutputPins に配置された出力データ
のオブジェクトトークンは、Pins から出発する ObjectFlows のどれに対しても供給され
ることがある。さらに、制御トークンはその Action から出発する ControlFlows 上で供
給されるものとする (15.5)。

局所的再入可能性の性質：

   If an Action is not locally reentrant (``isLocallyReentrant`` = false), then
   once it starts executing, the Action and its InputPins do not accept any
   tokens offered to them until the execution has finished.

この時点で、必要なトークンがまだ利用可能であれば、Action は供給を受理し、新しい
実行を開始することが許される。一方、Action の ``isLocallyReentrant`` が真である
場合、上記の規則が許す限り、いつでも新しい実行を開始することが許される。

制御ピンの性質：

   A control Pin (with ``isControl`` = true) must have a control type
   (``isControlType`` = true), so that they may be used with ControlFlows.

制御 Pins は Actions が Pins に課す制約では無視される。

制御 InputPin に到着したトークンは、その Action に到着した制御トークンと同じ意味
を持つが、制御トークンは制御 Pin に一時的に貯蔵することが可能だ。

トークンは Action から出る ControlFlow に置かれたトークンと同じ意味に従って制御
OutputPin に置かれる。

16.2.4 Notation
----------------------------------------------------------------------

本節では Activities で使われる Actions を表す図表的表記法を既定する。この表記法
はオプションであり、適合性のあるツールがテキストによる具体的な構文を用いてもよ
い。だが、Actions に対する図表的表記を用いるのならば、以下の定義だけが仕様準拠表
記だ。

16.2.4.1 Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Figure 16.2 Action

* Actions は丸角矩形を用いて示す。
* 記号には Action の名前やその他の説明が現れることがある。

Actions の特化型の対する記法は後述。

   Figure 16.3 Local pre- and post-conditions

局所的な事前条件と事後条件はそれぞれキーワード ``«localPrecondition»`` と
``«localPostcondition»`` を呼び出しに取り付けた Comment として示す。

16.2.4.2 Pins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Figure 16.4 Pin notations

   As ObjectNodes, Pins are notated as rectangles (see sub clause 15.4.4).
   However, Pin rectangles may be notated as small rectangles that are attached
   to the symbol for the Action that owns them (see Figure 16.4).

Pin の付近にその名前を表示してもよい。名前に制限はないが、それを流れるオブジェク
トやデータの種類を単に示すだけだ。両者を示すには ``name: type`` のようにラベルす
る。

InvocationActions の Pin に対応する Parameter を Classes 上の BehavioralFeatures
の Parameter と同じテキスト表記を用いて、ラベルで完全に指定することもできる。こ
の場合、Classes 上の BehaviorFeatures の Parameters と同じテキスト表記 (16.3.4)
を使用する。

   Figure 16.5 Pin notations, with arrows

InputPins と OutputPins を区別する ActivityEdges が存在しないときには、この図の
ように矢印を Pin 矩形の内部に配置しても構わない。矢印の向きは Action に対する入
出力の別によって決める。

   Figure 16.6 Standalone Pin notations

ある Action の OutputPin が ObjectFlow を介して別の Action の同名 InputPin に接
続している状況では、この図のようなオプション記法で示すことが許される。

* この記法における単品の Pin は当該モデルにおける OutputPin, InputPin, その間の
  ObjectFlow に対応する。
* この形式は Pin の型が同じでないならばなるべく避けること。

..

   Control Pins are shown with the textual annotation {control} placed near the
   Pin symbol.

   A ValuePin is notated as an InputPin with the ValueSpecification written
   beside it (see sub clause 8.2.4 on textual notation for ValueSpecifications).

16.2.5 Examples
----------------------------------------------------------------------

16.2.5.1 Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Figure 16.7 Examples of Actions

Send Payment の実施後に Accept Payment が実施される。

   Figure 16.8 Example of action using a tool-specific concrete syntax

あるツールに固有の具体的構文で表現されたアクションらしい。ループ処理を一つの
Action で表してよいようだ。

   Figure 16.9 Example of an action with local pre- and post-conditions

``Dispense Drink`` という Action の局所的な事前条件と事後条件が Comment 記法を
使って詳細に記された例。飲み物が自販機から出る前後の状態が普通の英語で仕様化され
ている。

16.2.5.2 Pins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Figure 16.10 Pin examples

* ``Fill Order`` が ``Order`` を生産し、``Ship Order`` がそれを消費する。
* ``Fill Order`` は ``Ship Order`` が開始するために完了する必要がある。
* 右上の図式は両 Actions に Pin 記号を明示した版だ。
* 下の図式では Pin をたくさん描いている。Pin に添えられている角括弧付きのラベル
  が目を引く。

..

   Figure 16.11 Specifying selection behavior on an ObjectFlow

* Pin は ObjectNode なので ``selection`` の指定が可能。
* ``Order`` は ``Order Priority`` に基づいて出荷され、同じ優先度のものは FIFO 方
  式で補充することを意図している。

..

   Figure 16.12 Example abstract syntax model showing the use of ActionInputPins

``self.foo->bar(self.baz)`` なるテキストによる具体的構文の式を UML 抽象構文式で
示したもの。これは難しい。

16.3 Invocation Actions
======================================================================

16.3.1 Summary
----------------------------------------------------------------------

   An InvocationAction is an Action that results, directly or indirectly, in the
   invocation of a Behavior (see sub clause 13.2).

InvocationActions には、Operations や Behaviors を呼び出すための CallActions
や、すでにオブジェクト化された Behaviors を開始するための CallActions がある。

InvocationActions には信号やその他のオブジェクトを標的として送信したり、利用可能
な受信者に向けて信号を一斉送信する能力を有するものある。

16.3.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 16.13 Invocation Actions

抽象型 InvocationAction から派生する型がいくつかある。概要に書いてあるとおりのク
ラス図。

16.3.3 Semantics
----------------------------------------------------------------------

16.3.3.1 Call Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

CallAction の定義から。

   A CallAction is an InvocationAction that calls a Behavior or an Operation.
   There are three kinds of CallActions:

CallBehaviorAction
   Behavior を直接呼び出す CallAction であり、BehavioralFeature を呼び出すことで
   Behavior を呼び出すものではない。
CallOperationAction
   Operation 呼び出し要求メッセージを対象オブジェクトに伝達し、関連 Behavior の
   呼び出しを引き起こすことがある CallAction だ。その対象オブジェクトはこの
   CallOperationAction の ``target`` InputPin から取得する。
StartObjectBehaviorAction
   直接オブジェクト化された Behavior か、あるオブジェクトの
   ``classifierBehavior`` のどちらか一方の実行を開始する CallAction だ。開始する
   オブジェクトはその InputPin から取得する。

      If the input object is an instantiated Behavior that is not already
      executing, then it begins executing. If the input object has a
      classifierBehavior that is not already executing, then it is instantiated
      and started. In either case, if the identified Behavior is already
      executing, then the StartObjectBehavior has no effect.

   注意：入力オブジェクトが新規生成された Behavior でない場合は、
   ``classifierBehavior`` を持つ必要がある。入力オブジェクトが新規生成された
   Behavior である場合、そのオブジェクトは ``classifierBehavior`` をも持っている
   ことがあり、それも開始される。この ``classifierBehavior`` 自体が
   ``classifierBehavior`` を持っている場合、この ``classifierBehavior`` も再帰的
   に開始される。

CallAction は直接的にか、またはある Operation 呼び出しを通じて、同期的または非同
期的 Behavior 呼び出しに帰することがある。

* 呼び出しが同期的 (``isSynchronous`` = true) の場合、呼び出された Behavior の
  実行が（正常かどうかを問わず）完了するまで、その Action の実行は完了しない。
* 呼び出しが非同期的 (``isSynchronous`` = false) の場合、Action の実行はその
  Behavior が呼び出されるとすぐに完了する。非同期呼び出しが完了する
  と、CallAction を包含する Behavior の実行は、Behaviorの実行中に発生した例外条
  件の処理も含め、呼び出された Behaviorの実行とは独立して同時に進行する。

再入不能な Behavior を呼び出すと：

   If the Behavior invoked by a CallAction is not reentrant, then no more than
   one execution of it shall exist at any given time (see sub clause 13.2.2).

再入不能 Behavior の呼び出しは、その Behavior がすでに実行中であるときに新たな実
行を開始することは許されないが、現在の実行が停止したときに新たな実行を開始するこ
とは許される。

   However, a CallAction with ``isLocallyReentrant`` = false shall not start a
   new execution of the Behavior if there is a Behavior execution ongoing that
   was started by the same Action within the same containing Behavior execution,
   but may start it when the current execution terminates (see also sub clause
   16.2.3).

Parameters と Pins の照合仕様：

   Behaviors and Operations have totally ordered lists of owned Parameters, and
   these Parameters are matched to Pins on a CallAction using that ordering.

* CallAction の ``arguments`` Pins は入力 Parameters の部分リストに順番に照合さ
  れ、``result`` Pins は出力 Parameters の部分リストに順番に照合され
  る。
* CallAction の ``arguments`` と ``results`` Pins の型、順序、多重度は、対応する
  Parameters と同じでなければならない。

CallAction を実行すると、その ``argument`` Pins にある値が、対応する入力
Parameters で呼び出された Behavior または Operation に引き渡される。

* 呼び出しが同期的である場合、出力 Parameter に返された値が CallAction の対応す
  る ``result`` Pins のトークンに配置される。
* 出力 Parameter に値がない場合は、対応する ``result`` Pin に空トークンが配置さ
  れる。
* 呼び出しが非同期の場合、結果値を返すことは不可能だ。

引数の一つでも streaming ならば：

   If any of the Parameters are streaming (``isStreaming`` = true), then the
   call must be synchronous (see also the discussion of streaming Behavior
   parameters in sub clause 13.2.3).

* この場合、呼び出し先 Behavior の実行中、CallAction は streaming 入力 Parameter
  に対応する実引数 Pin に、各 Pin の ``upper`` 値までのトークンを受理し続け
  る。Streaming 出力 Parameter に配送された値は、対応する結果 Pins に供給される
  （各 Pin の ``upper`` 値までしか受理されない）。

呼び出し先 Behavior はその実行中に、呼び出し元 CallAction との間のトークンフロー
を streaming Parameter によって入手できるということになる。

Actions についての実行規則に加えて、``streaming`` Parameters のある Behavior や
Operation を呼び出す CallAction には次の規則が適用する：

* CallAction に対する InputPins のすべてで、それぞれの ``lower`` 値以上の個数の
  値が CallAction 実行前に供給されるものとする。

     If all the ``argument`` Pins of the CallAction are for streaming Parameters
     with a ``lower`` multiplicity greater than 0, then at least one shall have
     an offered value before the CallAction can execute.

* CallAction が正常に実行を完了することが可能になる前に、ある ``streaming``
  Parameter に対応する CallAction の ``argument`` Pin それぞれの ``lower`` 値以
  上の個数の値が受理されなければならない。
* 呼び出された Behavior の実行が正常に完了する前に、CallAction の ``result`` Pin
  それぞれの ``lower`` 値以上の値を、その実行完了までに配送されなければならな
  い。

      (Values may be posted to ``result`` Pins corresponding to streaming output
      Parameters before the execution completes.)

  しかし、呼び出し先 Behavior が正常に完了しない場合、``result`` Pin にはその
  ``lower`` 値よりも少ない数の値が配送されてもよい。

ParameterSets にグループ化されている Parameters がある {Behavior,Operation} を呼
び出す CallAction には特別な規則も適用する：

* {Behavior,Operation} に入力 ParameterSets がある場合、CallAction 実行許可時の
  (16.2.3) の規則が、入力 ParameterSet それぞれの Parameters に対応している
  InputPins の（重複する可能性のある）集合に個別に適用される。

     If sufficient data is available to more than one input set, then one is
     chosen non- deterministically.

* {Behavior,Operation} に出力 ParameterSets があり、かつ CallAction が正常完了す
  る場合、この CallAction はある出力 ParameterSet に対応している OutPins 上にし
  か、これらの OutPins の ``lower`` 値に見合う出力を生じないものとする。かつ、オ
  ブジェクトトークンがこれらの OutputPins から出発する ActivityEdges に供給され
  る。

     No object tokens are offered from any other OutputPins, not even null
     tokens.

16.3.3.2 Send Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A send Action is an action that transmits an object asynchronously to one or
   more target objects. As a send Action is always asynchronous, it may have
   ``argument`` inputs, but it has no result outputs. The Action completes as
   soon as the object is sent, whether or not it has been received yet.

非同期であること、結果出力がないこと、送付をもって完了することが特徴だ。次の三種
類の送信 Actions がある：

SendSignalAction
   Signal オブジェクトを生成してそれを対象の InputPin で指定されたオブジェクトに
   伝える InvocationAction だ。

      A SendSignalAction must have ``argument`` InputPins corresponding, in
      order, to each of the (owned and inherited) Properties of the Signal being
      sent, with the same type, ordering and multiplicity as the corresponding
      ``attribute``.

   * 伝達される Signal オブジェクトの Property 値は、その Property に対応する
     ``argument`` InputPin から取られる。
   * 対象オブジェクトによる Signal オブジェクトの処理は (13.2.3), (13.3.3) で述
     べられる。
BroadcastSignalAction
   SendSignalAction 同様に、その ``argument`` InputPins から取った値を使って
   Signal オブジェクトを生成する InvocationActionだ。ただし、Signal オブジェクト
   を単一の対象オブジェクトに送信するのではなく、システム内の利用可能な対象オブ
   ジェクトのすべてに潜在的に伝達する。
SendObjectAction
   その対象の InputPin で指定されたオブジェクトに向けてあらゆる種類のオブジェク
   トを伝える InvocationAction だ。

   * 伝達されるオブジェクトは SendObjectAction の単一要望 InputPin で与えられる。
   * このオブジェクトが Signal インスタンスである場
     合、{Send,Broadcast}SignalAction から送信されたものと同じ方法で対象オブジェ
     クトによって処理される。そうでない場合、オブジェクト受付は AnyReceiveEvent
     を使用してしか処理不能だ (13.3.3)。

{Send,Broadcast}SignalActions では ``argument`` InputPins は送信される Signal の
Properties に順番に照合される。Signal の所有 Property は ordered である
が、Signal は Generalization 関係によって他の Signals の Properties から継承する
こともある。この場合 Property の順序は所有 Properties が継承 Properties の前に来
るようになる。以下略。

   The target object(s) of a send Action may be local or remote. The transmitted
   object may be copied during transmission, so identity may not be preserved.

オブジェクトの伝達方法、それに必要な時間、伝達がさまざまな対象に到達する順序、経
路はすべて未定義だ。

16.3.3.3 Invocation Actions and Ports
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Port がある InvocationAction とそうでないものがある：

   A CallOperationAction, SendSignalAction, or SendObjectAction may send a
   request through a Port by targeting an object having the Port and identifying
   the Port with the Action’s ``onPort`` attribute. Other kinds of
   InvocationActions shall not have a value for the ``onPort`` attribute.

この Port には次の要件がある：

   If ``onPort`` is given, then the Port shall be an owned or inherited
   ``feature`` of the ``type`` of the ``target`` InputPin of the Action.

Action が実行されると、対象オブジェクト自体にメッセージを送信するのではなく、対
象オブジェクトの与えられた Port を通してメッセージを送信、処理される (11.3.3)。

「内側で実行する」という概念：

   An Action is said to execute *inside* an object if the context object of the
   Behavior execution within which the Action is executing is either the same as
   or is directly or indirectly owned (in the sense of transitive composition
   links) by the given object.

例えば、与えられたオブジェクト（あるいはオブジェクトの部分）の ``method`` や
``classifierBehavior`` の中で実行される場合もこれに含まれる。

ある情況での Action に関係する Operation や Reception に注目する：

   In the case of a CallOperationAction, a ``provided`` or ``required``
   Interface of the given Port shall have the called Operation as a ``feature``.
   In the case of a SendSignalAction or a SendObjectAction whose ``object``
   InputPin has a Signal as its ``type``, a ``provided`` or ``required``
   Interface of the given Port may have a Reception for the identified Signal,
   but this is not required. In either case, the relevant Operation or Reception
   (if any) is referred to as the :dfn:`invoked BehavioralFeature` in the
   following rules.

* 呼び出に先 BehavioralFeature がある ``provided`` Interface にはあって、どの
  ``required`` Interface にもない場合、InvocationAction が実行されると、与えられ
  た Port を通して、対象 InputPin で与えられたオブジェクトに呼び出され、その受領
  は (11.3.3) で述べられたように処理される。

     NOTE. This allows an InvocationAction executed inside its target object to
     potentially send a message back into the target object through a
     ``provided`` Interface of one of its own Ports.

* 呼び出し先 BehavioralFeature がある ``required`` Interface にはあって、どの
  ``provided`` Interface にもない場合、InvocationAction が対象 InputPin で与えら
  れるオブジェクトの内部で実行されていると、(11.3.3) で述べられたように、与えら
  れた Port を通して、対象オブジェクトの外部へ呼び出しが転送される。

     If the InvocationAction is being executed other than inside the given
     target object, the semantics are undefined.

* 呼び出し先 BehavioralFeature がある ``provided`` とある ``required`` Interface
  の両方にあるか、または呼び出し先 BehavioralFeature がない場合、この
  InvocationAction が対象の InputPin で与えられるオブジェクトの内部で実行されて
  いれば、与えられた Port を通して対象オブジェクトの外部で呼び出される。そうでな
  い場合、中へ呼び出される。

     NOTE. In this case, if the InvocationAction executes inside its target
     object, it cannot send a message back into the target object, because such
     a message would go out through the required Interface. However, the same
     effect can be achieved by having a Connector that loops from the Port in
     question back to that same Port.

``onPort`` を指定することなしに、{CallOperation,SendSignal,SendObject} の対象オ
ブジェクトとして、「相互作用点」オブジェクト（つまり Port に新規生成されたオブ
ジェクト）を使用することも可能だ。この場合、その要求は相互作用店に直接送られ、こ
の Port の所有者の内部で特定の経路に送られる (11.3.3)。この要求は、当 Portの
``provided`` Interface のいずれかを介して、相互作用点の所有者に行く。

16.3.4 Notation
----------------------------------------------------------------------

``onPort`` の値は特定の InvocationAction を意味する記号の名前文字列にある句 "via
<port>" によって示す。

16.3.4.1 Call Behavior Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Figure 16.14 Calling a Behavior

   A CallBehaviorAction shall be notated as an Action with the ``name`` of the
   invoked Behavior placed inside the Action symbol (see Figure 16.14).

Action の名前が Behavior のそれと異なる場合は、代わりに Action 名が記号に現れる
ものとする。

Behavior の ``precondition`` と ``postcondition`` を Figure 16.3 と同様にして示
すことが可能であるが、キーワード ``«precondition»`` と ``«postcondition»`` を用
いる。

..

   Figure 16.15 Calling an Activity

Activity の呼び出しは Action 記号の内部に熊手みたいな (a rake-style) 記号を置く
ことで示す。

   The rake resembles a miniature hierarchy, indicating that this invocation
   starts another Activity that represents a further decomposition.

右側の図式は代替表記だ。呼び出し先 Activity の内容を角丸巨大矩形の中に表示する。

* ActivityParameterNodes は呼び出し先 Activity の境界線上に表示する。
* ObjectFlows は CallBehaviorAction の Pins に対応する呼び出し先 Activity の
  ActivityParameterNodes にリンクして表示するが、抽象構文では Pins にリンクして
  いる。

抽象構文は記法の選択に関係なく同じだ。

16.3.4.2 Call Operation Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Figure 16.16 Calling an Operation

   A CallOperationAction is notated as an Action with the ``name`` of the
   invoked Operation placed inside the Action symbol

Fig. 16.3 と同様にして示すことが可能。

   Figure 16.17 Calling an Operation, showing the owner name

Operation の ``owner`` の ``name`` を Operation ``name`` の下に
``(OwnerClassName::)`` または ``(OwnerClassName::OperationName)`` の形式で表示す
る。

16.3.4.3 Send Signal and Send Object Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Figure 16.18 Sending a Signal

   A SendSignalAction is notated as a convex pentagon with the ``name`` of the
   Signal placed inside it.

* 右側が凸。
* SendObjectAction が常にある Signal を送信するような形で用いられる場
  合、SendSignalAction 記法をがその SendObjectAction を表すのに利用可能だ。

16.3.4.4 Pin Annotations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Figure 16.19 Exception Pin annotations

``isException`` が真である Parameters に対応する Pins は、小さい三角
形が例外ピンから出発する辺の始点を示す、小さな△の Comment 付きで表示される。

Pin が単品 ObjectNode 記法で示されている場合にも△は記す。

   Figure 16.20 Effect Pin annotations

Pin に対応する Parameter に ``effect`` が指定されている場合、その ``effect`` は
Pin に接続する辺の付近に中括弧で囲んで記す。

   Figure 16.21 Stream Pin annotations

Pin に対応する Parameter の ``isStreaming`` の真偽値は、この Pin 記号の近くに
``{stream}`` または ``{nonstream}`` で示す。

* Pin が単品 ObjectNode 記法で示されている場合にも同様。
* このような中括弧 Comment が省略されている場合は ``{nonstream}`` であるものとす
  る。

Streaming Parameters については図表的表記を用いることでさらに強調することがある：

* 単品の Pin を塗りつぶし矢印で結んで streaming を示すことが可能だ。
* そうでなければ streaming Paramters に対応する Pins を塗りつぶし小矩形で示すこ
  とが可能だ。

..

   Figure 16.22 Stream Pin annotations, with filled arrows and rectangles

* ``streaming`` Parameters を示すためにには、さらなる強調を付加してよい。

  * 単体の Pin に接続している矢印の矢先を黒く塗りつぶしてよい。
  * さもなければ Pins 自体を黒く塗りつぶしてよい。

16.3.4.5 Parameter Sets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

InvocationAction の Pins に出入りする複数の ObjectFlows は通常 "and" 条件として
扱われる。しかし、ある flows のグループ一つが他のグループに対して排他的であるこ
ともある。これは ParameterSets でモデル化されて、一つ以上の Pins を取り囲む矩形
として表記される。

   Figure 16.23 Alternative input/outputs using ParameterSet notation

入力に対する disjunctive normal form を表している。"and" の流れのグループ一つが
"or" のグループ分けによって分離されている。

16.3.5 Examples
----------------------------------------------------------------------

16.3.5.1 Call Behavior Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Figure 16.24 Invoking an Activity

``Fill Order`` という Activity を呼び出す CallBehaviorAction だ。角丸矩形内右下
の逆さフォーク記号に注意。

16.3.5.2 Send Signal Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Figure 16.25 Sending Signals

何か発注処理のワークフローの一部を示す図式。Signals が送られる。

   An order is created (in response to some previous request that is not shown
   in the example). A Signal is sent to the warehouse to fill and ship the
   order. Then an invoice is created and sent to the customer.

16.3.5.3 Pin Annotations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Figure 16.26 Streaming Pin examples

``Order Filling`` は周期的にオブジェクトを放出する（この仕様を ``{stream}`` で
示している）連続的 Behavior であり、必ずしも完了するものではない。

``Order Shipping`` も補充された (``[Filled]``) ``Order`` オブジェクトを周期的に
受理する連続的 Behavior だ。``Order Shipping`` は最初の ``Order`` が到着したとき
に呼び出され、到着するたびに処理することを ``{stream}`` で示している。

..

   Figure 16.27 Exception Pin examples

上のコースは例外送出ケース。△がそれを示す。

..

   Figure 16.28 Pin example with effects

``Order`` を発注する ``Place Order`` Action と、発注された ``Order`` を読み込ん
で処理する ``Fill Order`` Action を示している。

* 中括弧は ``effect`` を示す。
* ``Place Order`` が ``Order`` を ``{create}`` して、``Fill Order`` が
  ``Order`` を ``{read}`` する。

16.3.5.4 Parameter Sets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Figure 16.29 Alternative input/outputs using ParameterSets

``Ship Item`` の InputPins が（それぞれが）グループ化されているので、``Buy
Item`` か ``Make Item`` からのどちらかのアイテムを受信するたびに ``Ship Item``
が開始する。

16.4 Object Actions
======================================================================

16.4.1 Summary
----------------------------------------------------------------------

   Object Actions deal with the creation, destruction and comparison of
   instances of Classifiers.

与えられた Classifier のオブジェクトを読み込んだり、オブジェクトがどのように分類
されているかを調べたり、オブジェクトの分類を変化させたりする Actions もある。

16.4.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 16.30 Object Actions

十個近くの派生 Actions がある。注意深く見ると {Input,Output}Pin のどちらかしかな
いものと、両方があるものがあることに気づく。

16.4.3 Semantics
----------------------------------------------------------------------

16.4.3.1 Create Object Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A CreateObjectAction is an Action that creates a direct instance of a given
   Classifier and places the new instance on its ``result`` OutputPin. The
   Action has no other effect.

オブジェクトが生成される Classifier が Behavior である場合、その生成オブジェクト
がその Behavior の実行だ。ただしその実行は生成時にすぐに自動的に開始することはな
い。StartObjectBehaviorAction (16.3.3) を用いて明示的に開始するものとする。

16.4.3.2 Destroy Object Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A DestroyObjectAction is an Action that destroys the object on its target
   InputPin.

オブジェクトはリンクである場合もある。DestroyLinkAction (16.6) の意味が適用され
る。

オブジェクトが破壊されると、それはどの Classifier とも分類されぬものになる。

リンクの破壊：

   If ``isDestroyLinks`` is true, links in which the object participates are
   destroyed along with the object according to the semantics of
   DestroyLinkAction, except for link objects, which are destroyed according to
   the semantics of DestroyObjectAction with the same attribute values as the
   original DestroyObjectAction.

複合集約オブジェクトの破壊：

   If ``isDestroyOwnedObjects`` is true, objects owned by the object through
   composite aggregation are destroyed according to the semantics of
   DestroyObjectAction with the same attribute values as the original
   DestroyObjectAction.

既に破壊されたオブジェクトを破壊することは効果がない。

16.4.3.3 Test Identity Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A TestIdentityAction is an action that tests if the two values given on its
   InputPins are identical objects. If the two values represent the same object,
   the Boolean value true is placed on the ``result`` OutputPin. Otherwise the
   value false is placed on the ``result`` OutputPin.

* Class 型オブジェクト同士の比較は、オブジェクトの同一性に基づいて行われる。
* DataType 型オブジェクト同士の比較は、同じ値を持つかどうかに基づいて行われる。

  * PrimitiveType 型の場合、UML 外の型の定義によって決定される。
  * Enumeration の場合は EnumerationLiteral の比較で決まる。
  * それ以外の場合は対応する属性同士の比較となる。

比較不能の場合でも、とにかく TestIdentityAction は真偽値を出す。

   The result of a TestIdentityAction for objects that are classified by both
   Classes and DataTypes, or by other kinds of Classifiers, is not defined, but,
   in all cases the Action produces a Boolean result.

16.4.3.4 Read Self Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A ReadSelfAction is an Action that places the context object of the Action
   execution on its result OutputPin. (See sub clause 16.2.3 about context
   objects.)

例えば、ReadSelfAction がある Operation のメソッドである Behavior に含まれている
場合、それが返す context object はその Operation 呼び出し対象である Operation の
所有 Classifier のオブジェクトになる。

ReadSelfAction がどの Behavior の所有 Classifier にも含まれていない Behavior に
含まれている場合、context object はこの Action が実行されている Behavior のオブ
ジェクトになる。

16.4.3.5 Value Specification Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A ValueSpecificationAction is an Action that evaluates a ValueSpecification
   and places the resulting value on its ``result`` OutputPin.

特に、LiteralSpecification を ValueSpecificationAction で定数値を生産するために
使用してもよい。

ValueSpecificationAction で InstanceValue を使用することは CreateObjectAction を
使用してオブジェクトを生成することと似ているが、InstanceValue の
InstanceSpecification の ``slot`` を使用してこの StructuralFeatures に値を与える
ことがある。

16.4.3.6 Read Extent Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A ReadExtentAction is an Action that retrieves the objects in the current
   extent of a Classifier and places them on its ``result`` OutputPin. The
   *extent* of a classifier is the set of all instances of a Classifier
   (including instances of any specializations) that exist at any one time.

よくわからない概念だ。

16.4.3.7 Reclassify Object Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A ReclassifyObjectAction is an Action that changes which Classifiers classify
   the object given on its ``object`` InputPin. It may both add and remove
   Classifiers from the object. Multiple Classifiers may be added and removed at
   one time.

この Action 完了後、入力オブジェクトは各 ``newClassifier`` によって分類さ
れ、``oldClassifier`` によってはされない。

* このオブジェクトが ``oldClassifier`` ではない Classifier によって以前に分類され
  ていた場合は、その Classifier によっても分類される。
* すでに存在する Classifier と重複する ``newClassifier`` を指定しても、入力オブ
  ジェクトを分類していない ``oldClassifier`` を指定しても、``newClassifier`` と
  ``oldClassifier`` の両方として Classifier を指定しても、何の効果もない。
* ``newClassifier`` は抽象型であってはならない。

..

   The identity of the input object is preserved, no behaviors are executed, and
   no default value expressions are evaluated.

``newClassifiers`` は不可分な段階で既存の分類子を置き換えるので、
``oldClassifiers`` と ``newClassifiers`` が共通の構造的特徴や関連を持っていても、
再分類時に構造的特徴値やリンクが失われることはない。

   If ``isReplaceAll`` is *true*, then all existing Classifiers for the object
   are removed before the ``newClassifiers`` are added, except if a
   newClassifier already classifies the input object, in which case this
   Classifier is not removed.

オブジェクトから Classifiers を全部取り除いて、新しいものを何も追加しないことの
効果は定義されない。

16.4.3.8 Read-Is-Classified-Object Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A ReadIsClassifiedObjectAction is an Action that determines whether the
   object given on its ``object`` InputPin is classified by a given Classifier.
   If it is so classified, then a Boolean *true* value is placed on the result
   OutputPin. Otherwise a *false* value is placed on the ``result`` OutputPin.

``isDirect`` が真ならば、調べる内容はそのオブジェクトが指定 Classifier により直
接的に分類されるかどうかであり、その Classifier の特殊化によって分類されるかどう
かは調べられない。反対に ``isDirect`` が偽ならば、特殊化も調べられることがある。

16.4.3.9 Start Classifier Behavior Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A StartClassifierBehaviorAction is an Action that starts the execution of the
   ``classifierBehavior`` of the object given on its ``object`` InputPin.

* この Action は Behavior の実行が開始されると同時に完了し、その後 Behavior が非
  同期に実行される。
* Behavior がすでに実行されている場合、または与えられたオブジェクトが
  ``classifierBehavior`` を持つ Classifier によって分類されていない場
  合、StartClassifierBehaviorAction は何の効果もない。

..

   NOTE. StartClassifierBehaviorAction is provided for compatibility with older
   versions of UML. It is generally preferable to use a
   StartObjectBehaviorAction instead of a StartClassifierBehaviorAction, as a
   StartObjectBehaviorAction allows for the passing of Parameter values and for
   synchronous invocation (see sub clause 16.3).

16.4.4 Notation
----------------------------------------------------------------------

   Figure 16.31 ValueSpecificationAction notation

ValueSpecificationAction はその ValueSpecification でラベルされる Action として
記す。

その他の種類のオブジェクト行動固有の記法はない。

16.4.5 Examples
----------------------------------------------------------------------

   Figure 16.32 ValueSpecificationActions

現実味のない見本だが、定数 5 または 6 を出力する Activity だ。角丸矩形二つとも
ValueSpecificationAction の記号だ。

16.5 Link End Data
======================================================================

16.5.1 Summary
----------------------------------------------------------------------

リンクオブジェクトではないリンク、つまり AssociationClass のオブジェクトではない
Association のオブジェクトは、実行中の値としてAction との間で引き渡すことが不可
能だ。その代わり、リンクはその端の値により識別される。

   LinkEndData is a specification of such values for one end of a link, used in
   the identification of links by LinkActions (as further described in sub
   clause 16.6).

16.5.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 16.33 Link End Data

LinkEndData は Element から直接派生。

LinkEnd{Creation,Destruction}Data は LinkEndData から派生。InputPin を基底クラス
のそれとは別に関連付ける。

16.5.3 Semantics
----------------------------------------------------------------------

16.5.3.1 Link End Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   LinkEndData is an Element that specifies the inputs to be used to match the
   values on one end of a link.

Association 端子それぞれが LinkEndData 要素で個別に識別される。

LinkEndData 要素には三つの部分がある：

#. 照合されるリンクの ``end`` の識別。この Property は Association の
   ``memberEnd`` でなければならない (11.4)。
#. リンクの指定された ``end`` で期待される値を設置する ``value`` InputPin 一つ。

   * この InputPin は ``end`` と同じ ``type`` を持ち、多重度は 1 だ。
   * ReadLinkAction で open end を指定することがあるため、当 InputPin を持つこと
     はオプションだ (16.6)。
#. オプションで、リンクの指定された ``end`` の ``qualifiers`` の期待される値を備
   える InputPins を識別する QualifierValues

   * ``qualifier`` Properties は ``end`` の ``qualifiers`` でなければならない (9.5)。
   * この InputPin は指定された ``qualifier`` と同じ ``type`` であり、多重度は 1
     だ。

16.5.3.2 Link End Creation Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   LinkEndCreationData is a specialized kind of LinkEndData used to identify one
   end of a link to be created by CreateLinkAction (see sub clause 16.6).

正規の LinkEndData が含むものに加え、LinkEndCreationData は次のものも含む：

* オプション ``isReplaceAll`` は新しいリンクがこの ``end`` における値に以前合致
  したリンク全部を置き換えるかどうかを指定する。
* 与えられた ``end`` が順序付きならば、この ``end`` の順序付けられた値における新
  しいリンクの挿入点を設置するために、``type`` が UnlimitedNatural で多重度が 1
  の ``insertAt`` InputPin (16.6) を指定しなければならない。

16.5.3.3 Link End Destruction Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   LinkEndDestructionData is a specialized kind of LinkEndData used to identify
   one end of a link to be destroyed by DestroyLinkAction (see sub clause 16.6).

正規の LinkEndData が含むものに加えて、LinkEndDestructionData は次のものを含む：

* オプション ``isDestroyDuplicates`` が真であれば、この ``end`` の値に合致するリ
  ンク全てを破壊することを指定する。
* 指定された ``end`` が順序付きかつ非一意であり、``isDestroyDuplicates`` が偽で
  あれば、``type`` が UnlimitedNatural であり多重度が 1 である ``destroyAt``
  InputPin (16.6) を、破壊されるリンクのこの ``end`` での位置の値を設置するため
  に指定されていなければならない。

16.5.4 Notation
----------------------------------------------------------------------

LinkEndData 固有の記法はない。

16.5.5 Examples
----------------------------------------------------------------------

なし。

16.6 Link Actions
======================================================================

16.6.1 Summary
----------------------------------------------------------------------

   LinkActions (and ClearAssociationAction) operate on Associations and their
   instances, links. This includes Associations that are AssociationClasses.

ただし、特に AssociationClass のオブジェクトに対して操作する LinkObjectAction に
ついては (16.7) を参照すること。

16.6.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 16.34 Link Actions

ClearAssociationAction が LinkAction 族から浮いている。

16.6.3 Semantics
----------------------------------------------------------------------

16.6.3.1 Link Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A LinkAction is an Action that reads, creates, or destroys links of an
   Association, which may be an AssociationClass. The links acted on are
   identified using LinkEndData, which specifies the values expected on the ends
   of those links (see sub clause 16.5).

* LinkAction の LinkEndData 要素の ``ends`` すべては、同じ Association の
  ``memberEnd`` でなければならない。
* LinkAction の LinkEndData 要素で識別される InputPins はすべて、この LinkAction
  の ``inputValue`` InputPins でなければならない。
* ``isStatic`` 値が真である ``end`` を持つ Associations の意味は未定義だ。

16.6.3.2 Read Link Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A ReadLinkAction is a LinkAction that retrieves values on one end of an
   Association (given the values on all the other ends) and places them on its
   ``result`` OutputPin.

この読み込まれる端子をこの ReadLinkAction の :dfn:`open end` という。

   Exactly one ``endData`` element for a ReadLinkAction must *not* have a
   ``value`` InputPin identified, and its corresponding end is the open end.

リンク読み取りで open end が回航不能だったり、ReadLinkAction の context
Classifier (16.2.3) から、または context Classifier がない場合に包含 Behavior か
ら見えなかったりするリンクを読み取る場合の意味は未定義だ。

ReadLinkAction 実行内容と結果：

   When a ReadLinkAction executes, it identifies the subset of all existing
   links of the Association that match the ``endData`` object values and
   qualifier values for all ends other than the open end and any qualifier
   values given for the open end. The values placed on the ``result`` OutputPin
   are the ones on the open end of this subset of links.

合致するリンクがない場合、ReadLinkAction は、その ``result`` OutputPin に空トー
クンを一つ生産する。

   The result OutputPin of a ReadLinkAction must have the same type and ordering
   as the open end. The multiplicity of the open end must be compatible with
   that of the OutputPin, but they do not have to be the same.

16.6.3.3 Create Link Action
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A CreateLinkAction is a LinkAction for creating links.

* リンクは Actions との間で受け渡しできる値であるとは限らないため、
  CreateLinkAction に OutputPin はない。
* CreateLinkAction はリンクオブジェクトの作成にも使用してよいが、この場合も出力
  値はない。Association が AssociationClass に変更されても、その逆でも、
  CreateLinkAction を変更する必要はない。

..

   The semantics of CreateLinkObjectAction applies to creating link objects with
   CreateLinkAction (see sub clause 16.7).

CreateLinkAction は LinkEndCreationData を使う：

   CreateLinkAction uses a specialization of LinkEndData called
   LinkEndCreationData. It supports the destruction of existing links of the
   Association that connect any of the objects of the new link.

リンクが作成されるとき、この ``isReplaceAll`` オプションは端子ごとに利用可能で、
新しいリンクが作成される前に、指定された端子からの Association のリンクすべてが
破壊される。作成されるリンクがすでに存在する場合は、このオプションでは破壊されない。

Association 端子すべてが順序付けられておらず、一意である場合、同じ Association
によってすでにリンクしているオブジェクト間でリンクを作成しても効果はない。

   Associations with ordered ends are supported with an insertion point
   specified at runtime by an additional ``insertAt`` InputPin on
   LinkEndCreationData

これは ``isReplaceAll`` が偽である場合、順序付けられた Association 端子にとって
は必須であって、順序付けられていない端子では省略される。

   NOTE. Association ends may be ordered even if the upper multiplicity is 1.

``insertAt`` Pin の明細：

* ``insertAt`` Pin は ``type`` が UnlimitedNatural で多重度が 1 だ。
* 現在のリンク数以下の正の整数である挿入点が意味するのは、既存のリンクの配列のそ
  の位置に新しいリンクを挿入することであり、整数 1 は新しいリンクが配列の最初と
  なることを意味する。
* 挿入点に無制限 "*" を指定すると、新しいリンクを配列の末尾に挿入することを意味
  する。
* 値 0 や既存リンク数より大きい値の場合、意味は未定義だ。

..

   Reinserting an existing link at a new position in an ordered, unique end
   moves the link to that position.

抽象型の Association のリンクを作成することの意味は未定義だ。

Association 端子の一つの ``upper`` 値に違反するリンクを作成することの意味は未定
義だ。

リンクが作成された後のその端子の濃度 (11.5.3) がその端子の ``upper`` 値より大き
い場合、新しいリンクはその端子の ``upper`` 値に違反することになる。

   The semantics is undefined for creating a link that has an Association end
   with ``isReadOnly`` = true after initialization of the other end objects,
   unless the link being created already exists (in which case the
   CreateLinkAction has no effect).

すべての読み取り専用端子から新しいリンクに関与するオブジェクトがまだ初期化されて
いるところである限り、リンクを作成することが許される。

   This means that Associations with two or more read-only ends cannot have
   links created unless all the objects to be linked are being initialized.

16.6.3.4 Destroy Link Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A DestroyLinkAction is an Action that destroys links matching specified
   LinkEndData. If there are no matching links, then the DestroyLinkAction has
   no effect.

DestroyLinkAction はリンクオブジェクトを破壊することに用いても構わないが、破壊す
るオブジェクトは LinkEndData を用いて同様に指定する。

   (The DestroyLinkAction thus does not need to be changed if the Association is
   changed to an AssociationClass, or vice versa.)

DestroyObjectAction でリングオブジェクトを破壊する場合は DestroyLinkAction の意
味が適用される。

   DestroyLinkAction uses a specialization of LinkEndData called
   LinkEndDestructionData. It supports destruction of duplicate links of
   Association on ends that are non-unique.

この ``isDestroyDuplicates`` オプションは端子ごとに利用可能で、指定した端子から
の Association の重複リンクすべてを破壊させる。

   Associations with ordered, non-unique ends are supported by a deletion
   position specified at runtime by an additional ``destroyAt`` InputPin on
   LinkEndDestructionData, which is required for ordered, non-unique Association
   ends when ``isDestroyDuplicates`` is false, and omitted for other ends.

* ``destroyAt`` Pin は ``type`` が UnlimitedNatural で多重度が 1 だ。
* 現在のリンク数以下の正の整数である削除点が意味するのは、既存のリンクの配列のそ
  の位置のリンクを破壊することであり、整数 1 は最初のリンクを意味する。
* 値 0 や既存リンク数より大きい値や無制限 "*" の場合、意味は未定義だ。

..

   The semantics are undefined for destroying a link that has an Association end
   with ``isReadOnly`` = true after initialization of the other end objects,
   unless no link matches the ``endData`` (in which case the DestroyLinkAction
   has no effect).

すべての読み取り専用端子からリンクに関与するオブジェクトがまだ初期化されていると
ころである限り、破壊することが許される。

   This means links with two or more read-only ends cannot be destroyed, unless
   all the participating objects are being initialized.

16.6.3.5 Clear Association Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A ClearAssociationAction is an Action that destroys all links of an
   Association in which a particular object participates, including link objects
   of an AssociationClass.

* クリアされる Association は静的に指定される。
* ClearAssociationAction はその Association の ``memberEnds`` の中から一つ以上の
  ものの特化型でなければならない実行中オブジェクトに対する InputPin を持つ。

..

   All links of the Association that have the given object on any end are
   destroyed, even when this violates the minimum multiplicity of any of the
   Association ends.

DestroyObjectAction の意味が ClearAssociationAction でリンクオブジェクトを破壊す
る場合に適用される。

16.6.4 Notation
----------------------------------------------------------------------

LinkActions や ClearAssociationActions に特化した記法は定義されない。

16.6.5 Examples
----------------------------------------------------------------------

なし。

16.7 Link Object Actions
======================================================================

16.7.1 Summary
----------------------------------------------------------------------

   Link object Actions operate on link objects, which are instances of
   AssociationClasses. LinkActions also operate on link objects, but identify
   them differently (see sub clause 16.7).

16.7.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 16.35 Link Object Actions

ReadLinkObjectEnd{,Qualifier}Action は構造が同じ。

16.7.3 Semantics
----------------------------------------------------------------------

16.7.3.1 Read Link Object End Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A ReadLinkObjectEndAction is an action that retrieves an end object from a
   link object.

* オブジェクトを取得する AssociationClass の ``end`` は静的に指定する。
* 読み込まれるリンクオブジェクトは ``object`` InputPin に指定する。
* 指定されたリンクオブジェクトの端子の値は ``result`` OutputPin に置く。

..

   NOTE. This is not the same as reading links of the link object’s Association
   with the specified end as the open end (as described for ReadLinkAction in
   sub clause 16.6).

読み込まれるリンクオブジェクトは、ReadLinkAction のようにリンク端子の値によって
ではなく、他のオブジェクトと同様に識別される。端子の多重度がその Association に
おける ``1..1`` と異なっていても、リンクオブジェクトの各端子にはオブジェクトが厳
密に一つ存在する。これが ReadLinkObjectEndAction の ``result`` の OutputPin が常
に多重度 ``1..1`` を持つ理由だ。

16.7.3.2 Read Link Object End Qualifier Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A ReadLinkObjectEndQualifierAction is an action that retrieves a
   ``qualifier`` end value from a link object.

* 値を取得する ``qualifier`` は静的に指定する。
* ``qualifier`` の所有者は AssociationClass の端子でなければならない。
* 読み込まれるリンクオブジェクトは ``object`` InputPin に指定する。
* 指定されたリンクオブジェクトの指定された ``qualifier`` の値は ``result``
  OutputPin に置く。

16.7.3.3 Create Link Object Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A CreateLinkObjectAction is a specialized CreateLinkAction (see sub clause
   16.6) for creating a link object (an instance of an AssocationClass).

CreateLinkObjectAction は CreateLinkAction と同じリンク作成の意味を持つが、その
``endData`` は AssociationClass のものでなければならず、新しいリンクは
``result`` OutputPin に配置されるリンクオブジェクトでなければならない。

与えられた ``endData`` に合致するリンクオブジェクトがすでに存在し、その
Assocication の端子がすべて一意である場合、これが ``result`` OutputPin に配置さ
れ、新しいリンクオブジェクトは作成されない。

16.7.4 Notation
----------------------------------------------------------------------

リンクオブジェクトに作用する Actions に特化した記法は定義されない。

16.7.5 Examples
----------------------------------------------------------------------

なし。

16.8 Structural Feature Actions
======================================================================

16.8.1 Summary
----------------------------------------------------------------------

   StructuralFeatureActions support the reading and writing of
   StructuralFeatures.

16.8.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 16.36 Structural Feature Actions

StructuralFeatureAction から {Read,Write,Clear}StructuralFeatureAction を派生す
る。

WriteStructuralFeatureAction から {Add,Remove}StructuralFeatureAction を派生す
る。

16.8.3 Semantics
----------------------------------------------------------------------

16.8.3.1 Structural Feature Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A StructuralFeatureAction is given a statically-specified StructuralFeature
   of a Classifier, and an object on which to act on its ``object`` InputPin.

このオブジェクトは、StructuralFeature を所有する Classifier の（直接または間接
の）オブジェクトか、StructuralFeature が二項 Association の所有端子 ``ownedEnd``
である場合は、その Association の反対側の端子の ``type`` のオブジェクトだ。

StructuralFeature がある Assocation の端子である場合、ある
StructuralFeatureAction がこの StructuralFeature を端子とする Association の
LinkAction と同じ意味を持つ。この意味は

* StructuralFeatureAction の context Classifier や包含 Behavior からこの
  StructuralFeature が見えない場合、
* context Classifier がない場合、
* この StructuralFeature の ``isStatic`` が真の場合

には未定義だ。

オブジェクトが関与する StructuralFeatures と Associations は動的な分類 (16.4) に
より、時間の経過とともに変化することがある。ただし：

   However, the type of the ``object`` InputPin of a StructuralFeatureAction is
   a single Classifier, and the semantics are defined only when the object
   passed to the Action is classified by that Classifier (directly or
   indirectly) at the time the Action accepts it and while the Action is
   executing.

この StructuralFeature は、モデル Element としてある StructuralFeatureAction か
ら参照されるため、他の Classifier に同じ名前の StructuralFeature があったとして
も一意に識別される。

   A ReadStructuralFeatureAction reads the values of a StructuralFeature and
   places these values on its ``result`` OutputPin. The other kinds of
   StructuralFeatureActions, WriteStructuralFeatureActions (including
   AddStructuralFeatureValueActions and RemoveStructuralFeatureValueActions) and
   ClearStructuralFeatureActions modify the values of a StructuralFeature.

これらの Actions はオプションで ``result`` OutputPin を持つことが許される。この
オプションを備える場合、変更された入力オブジェクトはこの OutputPin に配置される。

入力オブジェクトがデータ値（すなわち DataType 型オブジェクト）の場合、入力データ
値の複製が ``output`` Pin に置かれるが、適切な StructuralFeature が変更される。

   As a data value does not have an independent identity, the only way to obtain
   the modified data value is through the use of the ``result`` OutputPin.

16.8.3.2 Read Structural Feature Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A ReadStructuralFeatureAction is a StructuralFeatureAction that retrieves the
   values of a StructuralFeature and places them on its ``result`` OutputPin.

* StructuralFeature が ordered であれば、値は順番に OutputPin に配置される。
* StructuralFeature が Assocation 端子の場合、意味は StructuralFeature を open
  end とする ReadLinkAction と同じだ (16.6)。
* 取得された値がない場合（つまり StructuralFeature が空である場合）、
  ReadStructuralFeatureAction はその ``result`` OutputPin に単一の空トークンを生
  産する。

..

   The type and ordering of the ``result`` OutputPin are the same as those of
   the StructuralFeature. The multiplicity of the StructuralFeature must be
   compatible with the multiplicity of the ``result`` OutputPin, but does not
   have to be the same.

例えば、StructuralFeature が単一の値しか許容しない場合でも、この OutputPin の多
重度を設定して複数の値を支援することが可能だ。このようにすると、モデルになった
ReadStructuralFeatureAction は StructuralFeature の多重度の変更に影響されない。

16.8.3.3 Add Structural Feature Value Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   An AddStructuralFeatureValueAction is a StructuralFeatureAction for adding a
   value to a StructuralFeature of an object.

* 追加される値は ``value`` InputPin に与えられる。この InputPin は
  StructuralFeature と同じ ``type`` を持ち、多重度は ``1..1`` だ。
* StructuralFeature が Assocation 端子の場合、意味は CreateLinkAction (16.6) と
  同じで、リンクに関与するのは作用するオブジェクトと新しい値だ。

..

   If ``isReplaceAll`` is true, then the existing values of the StructuralFeature
   are removed before the new value is added, except if the StructuralFeature
   already contains the new value, in which case it is not removed under this
   option.

``isReplaceAll`` が偽で、StructuralFeature が unordered で unique である場合、こ
の StructuralFeature にすでに含まれている値を追加しても、何の影響もない。

順序付けられた StructuralFeature に値を追加するには、``insertAt`` InputPin で与
えられた新しい値を置くための挿入点が必要だ。これは ``isReplaceAll`` が偽の場合に
は順序付けられた StructuralFeatures で必要となり、順序付けられない
StructuralFeatures では省略される。

StructuralFeatures の値は ``upper`` 値が 1 であるときでさえ ordered であってもよ
い。

``insertAt`` Pin の明細再び：

* ``insertAt`` Pin が存在する場合、その ``type`` は UnlimitedNatural であり多重
  度は 1 だ。
* 現在の値の数以下の正の整数である挿入点が意味するのは、既存の値の配列のその位置
  に新しい値を挿入することであり、整数 1 は新しい値が配列の最初となることを意味
  する。
* 挿入点に無制限 "*" を指定すると、新しい値を配列の末尾に挿入することを意味す
  る。
* 値 0 や既存の値の数より大きい値の場合、意味は未定義だ。
* 順序付きかつ一意な StructuralFeature の新しい位置に既存の値を再び挿入すると、
  その位置に値が移動する。このような StructuralFeature の値は順序付き集合である
  ため、これは機能する。
* ``isReplaceAll`` が真のときに挿入点を使用すると、これは無視される。

..

   The semantics are undefined for adding a value that violates the upper
   multiplicity of the StructuralFeature, and for adding a new value to a
   StructuralFeature with ``isReadonly`` = true after initialization of the
   object that would have the value.

16.8.3.4 Remove Structural Feature Value Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A RemoveStructuralFeatureValueAction is a StructuralFeatureAction for
   removing a value from a StructuralFeature of an object.

この特徴が Assocation 端子の場合、意味は DestroyLinkAction と同じで、リンクに関
与するのはこのオブジェクトと削除される値だ。

   Except as given below, the value to be removed is given on the value
   InputPin, which has the same type as the StructuralFeature and a multiplicity
   of ``1..1``.

この結果、StructuralFeature の ``lower`` 値に違反する場合でも、値は削除される。

* StructuralFeature に含まれていない値を削除しても、効果は何もない。
* ``isRemoveDuplicates`` オプションは、一意でない StructuralFeature で指定された
  値の重複をすべて削除するかどうかを示す。

..

   If ``isRemoveDuplicates`` is false and the StructuralFeature is ordered and
   non-unique, then there is no ``value`` InputPin, and the value to be removed
   is instead specified by giving its position on the ``removeAt`` InputPin,
   which has ``type`` UnlimitedNatural and a multiplicity of ``1..1``.

* 現在の値の数以下の正の整数である削除点が意味するのは、既存の値の配列のその位置
  の値を削除することであり、整数 1 は配列の最初の値を意味する。
* 値 0 や既存の値の数より大きい値や無制限 "*" の場合、意味は未定義だ。

所有オブジェクトの初期化後に、``readOnly`` が真である StructuralFeature の既存の
値を取り除く場合の意味は未定義だ。

16.8.3.5 Clear Structural Feature Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A ClearStructuralFeatureAction is a StructuralFeatureAction that removes all
   values of a StructuralFeature, even if lower multiplicity of the
   StructuralFeature is greater than 0.

* StructuralFeature に値がない場合、この動作は効果がない。
* StructuralFeature が Association 端子の場合、意味は与えられたオブジェクトに対
  する ClearAssociationAction と同じだ。

StructuralFeature が値を持たない場合を除き、StructuralFeature を所有するオブジェ
クトの初期化後、``isReadOnly`` が真である StructuralFeature ではその意味は未定義
だ。

16.8.4 Notation
----------------------------------------------------------------------

StructuralFeatureActions に特化した記法は定義されない。

16.8.5 Examples
----------------------------------------------------------------------

なし。

16.9 Variable Actions
======================================================================

16.9.1 Summary
----------------------------------------------------------------------

   VariableActions support the reading and writing of Variables.

16.9.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 16.37 Variable Actions

派生のスタイルが先ほどのものと似ている。

16.9.3 Semantics
----------------------------------------------------------------------

16.9.3.1 Variable Action
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A VariableAction operates on a statically-specified Variable.

この Variable は VariableAction を含む Activity (15.2) または
StructuredActivityNode (16.11) によって定義されたものでなければならない。

16.9.3.2 Read Variable Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A ReadVariableAction is a VariableAction that retrieves the values of a
   Variable and places them on its ``result`` OutputPin.

* その Variable に順序がある場合、値は順番に OutputPin に配置される。
* 取得された値がない場合、Variable が空である場合、ReadVariableAction は、その
  ``result`` OutputPin に単一の空トークンを生じる。

   The type and ordering of the ``result`` OutputPin are the same as those of
   the Variable. The multiplicity of the Variable must be compatible with the
   multiplicity of the ``result`` OutputPin, but does not have to be the same.

例えば、Variable が単一の値しか許容しない場合でも、この OutputPin の多重度を設定
して複数の値を支援することが可能だ。このようにすると、モデルになった
ReadVariableAction は Variable の多重度の変更に影響されない。

16.9.3.3 Add Variable Value Action
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   An AddVariableValueAction is a VariableAction for adding a value to a
   Variable. The value to be added is given on the ``value`` InputPin, which is
   required. This InputPin has the same ``type`` as the Variable and a
   multiplicity of ``1..1`` (that is, a single value is added).

追加される値は ``value`` InputPin に与えられる。この InputPin は Variable と同じ
``type`` を持ち、多重度は ``1..1`` だ。

   If ``isReplaceAll`` is true, then the existing values of the Variable are
   removed before the new value is added, except if the Variable already
   contains the new value, in which case it is not removed under this option.

その Variable の ``lower`` 値が 1 より大きい場合でも、この Action が完了するとそ
の Variable はつねに単一の値を持つ。

``isReplaceAll`` が偽で、Variable が unordered で unique である場合、この
Variable にすでに含まれている値を追加しても、何の影響もない。

   Adding a value to an ordered Variable requires an insertion point for the new
   value using the ``insertAt`` InputPin, which is required for ordered Variable
   when ``isReplaceAll`` is false and omitted for unordered Variable (values of
   a Variable may be ordered or unordered, even if the multiplicity upper bound
   is 1.)

* 現在の値の数以下の正の整数である挿入点が意味するのは、既存の値の配列のその位置
  の値を挿入することであり、整数 1 は新しい値が配列の最初の値になることを意味す
  る。
* 挿入点に無制限 "*" を指定すると、新しい値を配列の最後に挿入することを意味する。
* 値 0 や既存の値の数より大きい値を指定した場合、意味は未定義だ。
* 順序付きかつ一意な Variable の新しい位置に既存の値を再び挿入すると、その位置に
  値が移動する。このような Variable の値は順序付き集合であるため、これは機能す
  る。
* ``isReplaceAll`` が真のときに挿入点を使用すると、これは無視される。

Variable の ``upper`` 値に違反する値を追加する場合の意味は未定義だ。

16.9.3.4 Remove Variable Value Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A RemoveVariableValueAction is a VariableAction for removing a value from a
   Variable.

* 削除される値は Variable と同じ型と多重度 ``1..1`` を持つ ``value`` InputPin に
  与えられる。
* Variable に含まれていない値を削除しようとしても効果はない。
* ``isRemoveDuplicates`` オプションは一意でない Variable 内の指定された値の重複
  をすべて削除するかどうかを示す。

..

   If ``isRemoveDuplicates`` is false and the Variable is ordered and
   non-unique, then there is no ``value`` InputPin, and the value to be removed
   is specified by giving its position on the ``removeAt`` InputPin, which has
   type UnlimitedNatural and a multiplicity of ``1..1``.

* 現在の値の数以下の正の整数である削除点が意味するのは、既存の値の配列のその位置
  の値を削除することであり、整数 1 は配列の最初の値を意味する。
* 値 0 や既存の値の数より大きい値や無制限 "*" の場合、意味は未定義だ。

16.9.3.5 Clear Variable Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A ClearVariableAction is a VariableAction that removes all values of a
   Variable, even if the lower multiplicity of the Variable is greater than 0.

Variable に値がない場合、この Action は効果がない。

16.9.4 Notation
----------------------------------------------------------------------

   Figure 16.38 Presentation option for AddVariableValueAction

上の図式は下の図式の抽象的構文版。

AddVariableValueAction の ``isReplaceAll`` が真である場合、これは変数名の近くに
``{replaceAll}`` というテキスト註釈で示すことが可能だ。

16.9.5 Examples
----------------------------------------------------------------------

なし。

16.10 Accept Event Actions
======================================================================

16.10.1 Summary
----------------------------------------------------------------------

   An AcceptEventAction waits for the occurrence of one or more Events.

受理した Event の発生が CallEvent の場合、ReplyAction をそれに応答するのに用いら
れることがある。受理した Event の発生が SignalEvent の場合、受信した Signal オブ
ジェクトは、

* その属性の値へと直ちに unmarshal されるか、
* UnmarshallAction を用いて後でそうされる。

16.10.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 16.39 Accept Event Actions

Action の派生クラスがまだまだ定義されていく。

Trigger のフォントがドイツ風だが？

16.10.3 Semantics
----------------------------------------------------------------------

16.10.3.1 Accept Event Action
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   AcceptEventAction is an Action with Triggers for one or more Events.

* AcceptEventAction が実行されると、その実行に対する context object のイベント
  プールから、その Triggers のいずれかに合致する Event の発生が発送されるのを待
  つ。
* AcceptEventAction の context object はこの AcceptEventAction が実行される
  Behavior 実行の context object だ。Behavior 実行そのものであることも許される
  (13.2.3)。

   AcceptEventAction is a *wait point* in the sense discussed in sub clause
   13.3.3, except only the AcceptEventAction waits, rather than the whole
   Activity (Activities can have other Actions executing while
   AcceptEventActions are waiting).

AcceptEventAction に合致する Event 発生がイベントプールから発送される場合、その
AcceptEventAction は続行可能になる。ただし、包含 Behavior 実行にこの Event 発生
に合致する Trigger が複数待機しているものがある場合、実際に起こるのはそのうちの
一つしかない。

   If the Trigger on the AcceptEventAction is chosen, then it completes and
   produces output on any ``result`` OutputPins.

受理信号作用：

   An AcceptEventAction with a ``trigger`` for a SignalEvent is informally
   called an :dfn:`accept signal action`.

* ``isUnmarshall`` が偽の場合、受理された SignalEvent 発生に関連付けられた
  Signalオブジェクト が配置される単一の ``result`` OutputPin を持たなければなら
  ない。
* ``isUnmarshal`` が真の場合、SignalEvent の Signal の各属性に対応する
  ``result`` OutputPin を（順番に）持たなければならず、受理された SignalEvent 発
  生に関連付けられた Signal オブジェクトの属性値は、これらの OutputPin に置かれ
  る。

待機時間作用：

   An AcceptEventAction with a ``trigger`` for a TimeEvent is informally called
   a :dfn:`wait time action`.

* 待機時間作用は単一の ``result`` OutputPin を持たなければならない。
* これが TimeEvent 発生を受理すると、その発生時刻の値が ``result`` OutputPin に
  置かれる。

AcceptEventAction が ``result`` を持たない場合もある：

   If the ``triggers`` of an AcceptEventAction are all for ChangeEvents and/or
   CallEvents, then the AcceptEventAction has no ``result`` OutputPins (unless
   the AcceptEventAction is an AcceptCallAction, see below).

この ``triggers`` が ChangeEvent や CallEvent とともに SignalEvent や TimeEvent
を含む場合、この AcceptEventAction は ``isUnmarshall`` が偽でなければならず、単
一の ``result`` OutputPin を持たなければならない。

AnyReceiveEvent:

   If one of the ``triggers`` of an AcceptEventAction is an AnyReceiveEvent, and
   the Event occurrence is for a message that is not matched by a SignalEvent or
   CallEvent ``trigger`` on the same AcceptEventAction, then the Event
   occurrence matches the ``trigger`` for the AnyReceiveEvent

AcceptEventAction が Activity で使われる場合、それがいつ利用可能になるのかを決め
るには特別な規則がある：

   If the AcceptEventAction has no incoming edges, by the usual rules, it is
   enabled when its immediately containing Activity (or StructuredActivityNode)
   begins execution. However, in addition, an AcceptEventAction with no incoming
   edges remains enabled after it accepts an Event occurrence.

Event 発生を受理して値を出力した後でも停止せず、別の Event 発生を待機し続ける。
このような AcceptEventAction は、その直後に包含する Activity (or
StructuredActivityNode) が停止したときに停止する。

16.10.3.2 Accept Call Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   An AcceptCallAction is an AcceptEventAction specialized for the handling of
   CallEvent occurrences.

* CallEvent に対する単一の Trigger を持たなければならない。
* CallEvent で特定された Operation の in と inout の ``ownParameters`` に順番に
  対応する ``result`` OutputPins を持つ。
* 同期呼び出しから戻るために必要な情報を備える ``returnInformation`` OutputPin
  を持つ。

..

   An AcceptCallAction is triggered in the same way as a normal
   AcceptEventAction on matching CallEvent occurrences.

* 呼び出しの後、コールメッセージに関連付けられた実引数値が ``result`` OutputPin
  に置かれる。
* さらに、後続する ReplyAction を実行するのに十分な情報が ``returnInformation``
  OutputPin に置かれる。
* ``returnInformation`` 値の内容は当仕様では定義されておらず、ReplyAction によっ
  てのみ使用される。

非同期呼び出しにより引き起こされた AcceptCallAction は、やはりその
``returnInformation`` OutputPin に値を生じるが、その値を受理する ReplyAction は
非同期呼び出しの戻り値が与えられると、何の効果もなく直ちに完了する。

AcceptCallAction の CallEvent で参照される Operation には関連するメソッド
Behavior があるべきではない。

   Otherwise, a call to the Operation will have the immediate effect of
   executing the method and will not be placed into the event pool for the
   context object.

したがって、Operation に対する呼び出しは AcceptCallAction に送達されることは決し
てない。

16.10.3.3 Reply Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A ReplyAction is an Action that completes the handling of a call that was
   accepted by a previous AcceptCallAction

この二つは復帰情報値で結ばれていて、その ``returnInformation`` OutputPin にある
AcceptCallAction によって生じ、包含 Behavior によって ReplyAction の
``returnInformation`` InputPin に配置される。

ReplyAction は Trigger も特定する。Trigger は ReplyAction が復帰情報値を取得する
AcceptCallAction が所有する CallEvent Trigger となるべく同じだ。

ReplyAction の ``replyValue`` InputPins は CallEvent により特定される Operation
の out, inout, return ``ownedParameters`` に順番に対応するものとする。

   When a ReplyAction executes, it generates a reply message to the original
   call request message, using the values from its ``replyValue`` InputPins.

同期呼び出しの場合、``returnInformation`` InputPin の値は応答メッセージの送信先
となる呼び出し元を識別するために使用される。ただし、``returnInformation`` 値が非
同期呼び出しの結果である場合、応答メッセージは送信されず、ReplyAction は何の効果
もなく完了する。

   The details of transmitting call requests, encoding return information, and
   transmitting replies are not defined in this specification.

応答情報を複製したり、オブジェクトに格納したり、引き渡したりしてもよいが、
ReplyAction の中で一度しか利用されてはならない。

   The semantics are undefined if the same return information value is supplied
   to a second ReplyAction. The semantics are also undefined if the return
   information value is not for a call to the same Operation as identified by
   the ``replyToCall`` Trigger of the ReplyAction.

ReplyAction が同期呼び出しからの復帰情報で実行されない場合、呼び出し元は応答を受
信しないので、それゆえ実行を完了することがないはずだ。このことは違法ではないが、
普通は望ましくない。

16.10.3.4 Unmarshall Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   An UnmarshallAction is an Action that retrieves the values of the
   StructuralFeatures of an object and places them on OutputPins.

* このオブジェクトは ``unmarshallType`` Classifier によって与えられた型と多重度
  ``1..1`` を持つ ``object`` InputPin に与えられる。
* UnmarshallAction は ``unmarshallType`` の各 Properties に順番に対応する
  ``result`` OutputPin を持つ。

Signal に所有された Properties は順序付けられているが、Generalization 関係に起因
して他の Classifiers から Properties を継承してもよい。この場合、

* ``unmarshallType`` の Properties は所有される Properties すべてが継承された
  Properties よりも先に来るように順序付けられる。
* さらに ``unmarshallType`` の祖先二つが Generalization によって直接的または間接
  的に関係している場合、より特殊な Classifier の被所有 Properties は、より一般的
  な Classifier の被所有 Properties よりも先に並ぶ。

     However, in the presence of multiple Generalization, some ancestors of the
     ``unmarshallType`` may not have any such transitive Generalization
     relationship, and no standard ordering is defined between the Properties of
     such ancestors.

UnmarshallAction が実行すると、その InputPin からオブジェクトを取り、そのオブ
ジェクトから ``unmarshallType`` の Properties の値を取得して、これらの値を対応す
るOutputPins に配置する。

UnmarshallAction は、例えば、``isUnmarshall`` が偽である AcceptEventAction によ
り生成された Signal オブジェクトの属性値を得るのに有用だ。

16.10.4 Notation
----------------------------------------------------------------------

   Figure 16.40 AcceptEventAction notations

AcceptEventAction は一般には凹五角形で記される。

* 左側が凹。
* 内側にその ``name`` を配してもよい。

待機時間作用、すなわち単一の TimeEvent ``trigger`` を有する AcceptEventAction
は、砂時計記号で記す。Action の ``name`` を記号の下側に書いてもよい。

16.10.5 Examples
----------------------------------------------------------------------

16.10.5.1 Accept Event Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Figure 16.41 Implicitly enabled AcceptEventAction

注文の取り消しを示す Signal を受理する、単一の SignalEvent ``trigger`` がある
AcceptEventAction の例だ。

* ``Cancel order request`` を受理すると ``Cancel Order`` が呼び出される。
* この Action はそれを含む Activity に入ると有効になるため ControlFlow は発生し
  ない。

..

   Figure 16.42 Explicitly enabled AcceptEventAction

``Process Order`` 後に ``Request Payment`` Signal が送信される (16.3.4)。それか
ら ``Payment confirmed`` AcceptEventAction がそれを受信すると、``Ship Order`` が
行われる。

Signal の受信はそれが送信された後しか有効でない。

..

   Figure 16.43 Repetitive time event

これは単一の TimerEvent ``trigger`` がある AcceptEventAction の例だ。

* 砂時計は待機時間活動の記号だ。
* ``End of month occurred`` が砂時計の左側に書いてある。
* ``Report Meter Reading`` は毎月末に起こる。

16.10.5.2 Unmarshall Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Figure 16.44 UnmarshallAction

``Unmarshall Order`` は ``Order`` から ``Name``, ``Address``, ``Product`` の属性
の値を unmarshal する。

16.11 Structured Actions
======================================================================

16.11.1 Summary
----------------------------------------------------------------------

   A StructuredActivityNode is an Action that is also an ActivityGroup (see sub
   clause 15.6). That is, it contains ActivityNodes and ActivityEdges that
   define its behavior when executed.

さらに、特化種の StructuredActivityNode (ConditionalNodes, LoopNodes,
SequenceNodes) は、その中の ExecutableNodes がどのように実行されるかについて固有
の制御意味を定義する。

ExpansionRegion も StructuredActivityNode の一種だが、ここではなく後で述べられ
る。

16.11.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 16.45 Structured Actions

StructuredActivityNode は Namespace, Action, ActivityGroup から派生している。そ
の派生型に {Conditional,Loop,Sequence}Node がある。

16.11.3 Semantics
----------------------------------------------------------------------

16.11.3.1 Structured Activity Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A StructuredActivityNode is an Action that is also an ActivityGroup (see sub
   clause 15.6) and whose behavior is specified by the ActivityNodes and
   ActivityEdges it so contains.

* StructuredActivityNodeは、それが含む ActivityNode と ActivityEdges を所有する
  ため、節点や辺は StructuredActivityNode 一つにしか直接含まれない。
* StructuredActivityNode は入れ子にすることが許されるが、そのため、辺や節点は入
  れ子になった多数の StructuredActivityNode に間接的に含まれることがある。

Variable 詳細：

   A StructuredActivityNode may also include the definition of Variables.

* これらの Variables および周囲の StructuredActivityNode や Activity で定義され
  た Variables は、StructuredActivityNode 入れ子の StructuredActivityNode 内の
  VariableActions (16.9) によってしか操作することが許されない。
* StructuredActivityNode が実行を開始するとき、その Variables はすべて空だ。

特殊型は別途述べられるので待て：

   The immediately following discussion under this heading is for the semantics
   of a StructuredActivityNode that is not an instance of one of the
   specializations of StructuredActivityNodes.

StructuredActivityNode は有効化され、Action に関する通常の規則に従って実行を開始
する (16.2.3)。

   None of the ``nodes`` within a StructuredActivityNode are enabled until the
   containing StructuredActivityNode begins executing (including InitialNodes
   and AcceptEventActions). At that point, which ``nodes`` are enabled is
   determined in the same way as for the ``nodes`` of an Activity when it begins
   execution (see sub clause 15.2.3).

実行は :doc:`./ch15-activities` にあるように Activity モデルの意味に従って進行す
る。

StructuredActivityNode の InputPins 詳細：

   The InputPins of a StructuredActivityNode may be the ``sources`` for
   ActivityEdges contained in the StructuredActivityNode.

* これによって InputPins に配置されたトークンを StructuredActivityNode 内の
  ActivityNodes が利用可能になる。
* この InputPins はその StructuredActivityNode が実行を開始すると ``outgoing``
  へそのトークンを供給する。

同様に、StructuredActivityNode の OutputPins は、これに含まれる ActivityEdges の
``targets`` であってもよい。トークンに関する仕様も向きを入れ替えれば InputPins
と同様。

StructuredActivityNode に含まれる ActivityEdge の要件：

   An ActivityEdge contained by a StructuredActivityNode must have both its
   ``source`` and ``target`` either be contained (directly or indirectly) in the
   StructuredActivityNode or be a Pin owned by the StructuredActivityNode.

逆に、StructuredActivityNode に含まれない ActivityEdge は、その ``source`` と
``target`` の両方とも StructuredActivityNode に含まれることは許されない。

StructuredActivityNode に出入りする ActivityEdges はこの StructuredActivityNode
の入れ物（直接または間接）によって所有される。

ActivityEdge が StructuredActivityNode の境界を到着方向にまたぐ場合：

   If an ActivityEdge has a ``source`` outside a StructuredActivityNode and a
   ``target`` within it, then any offers made on that edge remain pending until
   the StructuredActivityNode begins execution. While the StructuredActivityNode
   is executing, the ``target`` of the ActivityEdge may accept any offers pending
   from before the execution of the StructuredActivityNode, as well as any
   additional offers made while the StructuredActivityNode is executing, per the
   usual semantics of ActivityNodes.

ActivityEdge が StructuredActivityNode の境界を出発方向にまたぐ場合は、その
StructuredActivityNode が実行中でない限り、その辺上では供給不能だ。この
StructuredActivityNode の実行中、この ActivityEdge から行われた供給は即座に
StructuredActivityNode の外に拡がり、ActivityNode の通常の意味に従ってこの辺の
``target`` がその供給を処理する。

実行停止の詳細：

   A StructuredActivityNode completes execution according to the same rules as
   for the completion of the execution of an Activity (see sub clause 15.2.3),
   including terminating execution due to an ActivityFinalNode (see sub clause
   15.3.3).

ただし、StructuredActivityNode に含まれる ActivityFinalNode は、その中に含まれる
ことがあるActivity や他の StructuredActivityNode ではなく、直に含まれる
StructuredActivityNode とその中身しか停止しない。

実行停止時にトークンの消息はどうなるか：

   When a StructuredActivityNode completes its execution, all executions ongoing
   within it are terminated and all tokens contained in it are destroyed, except
   those on OutputPins of the StructuredActivityNode, which are offered on any
   ``outgoing`` edges.

* StructuredActivityNode の実行中にその OutputPins 上にトークンが蓄積されることが
  あるが、その実行が完了してしまうと、そのトークンらは ``outgoing`` 辺にのみ供給さ
  れる。
* StructuredActivityNode が完了したときにトークンを何も保持していない OutputPins
  はいずれも、それらの ``outgoing`` 辺上で空トークンを供給する。

16.11.3.2 Isolation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

属性 ``mustIsolate`` の意味が述べられている。

   Because of the concurrent nature of the execution of Actions within and
   across Behaviors, it can be difficult to guarantee consistent access and
   modification of object memory. In order to avoid race conditions or other
   concurrency-related problems, it is sometimes necessary to isolate the
   effects of a group of Actions from the effects of Actions outside the group.

このことを StructuredActivityNode およびその派生型の属性 ``mustIsolate`` を真に
設定することで表すことがある。

このフラグが真である場合の仕様：

   If the ``mustIsolate`` flag is true for a StructuredActivityNode, then any
   access to an object by an Action within the node must not conflict with
   access to the object by an Action outside the node. A conflict is defined as
   an attempt to write to the object by one or both of the Actions.

このような競合が潜在的に存在する場合、孤立した StructuredActivityNode の外部にあ
る Action によるこのようなアクセスを StructuredActivityNode の実行と interleave
させてはならない。

   This specification does not define the ways in which this rule may be
   enforced. An execution engine may achieve isolation using a locking
   mechanism, or it may simply sequentialize execution to avoid concurrency
   conflicts, or it may use some other method.

これらの規則に従ってモデルを実行することが不可能な場合、そのモデルは非形式的です。

独立性は不可分性の性質とは異なる。後者は Actions のグループが全て正常完了する
か、全く効果がないかのどちらかであることを保証するものだ。

16.11.3.3 Conditional Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ConditionalNode は実行の分岐と考えられる。

   A ConditionalNode is a StructuredActivityNode that chooses one among some
   number of alternative collections of ExecutableNodes to execute.

* Clause は ConditionalNode の枝一本に相当する。
* 枝は ``test`` 部分と ``body`` 部分で構成される。
* ConditionalNode 内のどの ExecutableNode も、ちょうど一つの Caluse の ``test`` ま
  たは ``body`` に含まれなければならない。

ConditionalNode の実行開始仕様：

   When a ConditionalNode begins execution, any InitialNodes within it are
   immediately enabled. An ExecutableNode contained in the ConditionalNode,
   however, can only become enabled when the ``test`` section or ``body``
   section that contains it is executed, as described below.

``test`` または ``body`` が実行されるときの仕様：

その節内の ExecutableNode のうち、必須入力データがなく、同じ節内に ``source`` を
持つ ControlFlow が到着していないものはすべて有効になり、制御トークンを一つ受領
する。

* ただし、実行中でない節の ExecutableNode への供給は、即座に引き渡されず、保留さ
  れたままであることを除けば、Activities の通常の意味に従い進行する。
* 対象 ExecutableNode はそれを含む節の後の実行の一部として最終的に実行される場
  合、保留中の供給を受理することが許される。

いったん ConditionalNode が実行中になると、``predecessorClauses`` がないその
Clauses の ``test`` 節が実行される。

   Each ``test`` section has an Action owning the ``decider`` OutputPin with
   type Boolean identified by the Clause. The result of a ``test`` section is
   the value placed on the ``decider`` OutputPin. If one or more ``test``
   sections result in a true value, then the corresponding ``body`` sections are
   enabled for execution. Next, any Clauses for which all ``predecessorClauses``
   have ``test`` sections that did not result in a true value have their
   ``test`` sections executed.

``test`` 節の実行が「同時である」と指定されるところでは、モデルがそれらの実行の
順序に何も課さないことを意味する。

* 実行順序を強制するため、ConditionalNode の Clauses 間で専用の制約を指定しても
  よい。

属性 ``isAssured`` と ``isDeterminate`` の仕様：

   If ``isAssured`` is true for a ConditionalNode, this asserts that at least
   one ``test`` section will yield a true value. If ``isDeterminate`` is true,
   this asserts that at most one ``test`` section will yield a true value (the
   ``predecessorClause`` relationship may be used to enforce this assertion).

これらの主張を自動的に検証することは一般には不可能であり、それらを強制する必要は
ないが、実行機関に対して有用な情報を与えることはある。主張に違反する場合、まとも
でないモデルが形成される。

``body`` 節の実行：

   Once the process of executing ``test`` sections finishes, if there is exactly
   one ``body`` section enabled for execution, that ``body`` section is
   executed. If more than one ``body`` section is enabled, only one is actually
   executed, but the choice of which one is non-deterministic.

実行可能な ``body`` がない場合、ConditionalNode の実行は何の効果も足さずに完了す
る。

名前は else だが、C 言語の default のような役回りだ：

   An “else” Clause is a Clause that is a successor to all other clauses in the
   ConditionalNode and whose ``test`` section always results in true.

このような Clause の ``body`` はこの ConditionalNode 内の他の ``body`` が有効に
なっていない場合かつその場合に限り有効になる。これにより、少なくとも一つの
``body`` が ConditionalNode に対して常に実行される。

次の記述は理解できるか：

   Whenever a ``body`` section becomes enabled for execution, it may actually be
   executed before the completion of any further ``test`` section executions. In
   this case, any ongoing ``test`` section executions are terminated and no
   further ``test`` sections are executed.

ConditionalNode には ``result`` OutputPins の順序付き集合がある。

   Each Clause of the ConditionalNode must have a matching set of bodyOutput
   OutputPins, which must identify OutputPins owned by Actions in the body
   section of the Clause.

* すべての Clause は ``result`` OutputPin の一つ一つに対して ``bodyOutput`` を持
  つ必要がある。
* Clause の ``body`` が実行される場合、その実行が完了すると、この Clause の
  ``bodyOutputs`` 上のトークンはすべて ConditionalNode の対応する ``result``
  OutputPinsに移される。

その後、ConditionalNode の実行が完了し、その OutputPin 上のトークンはすべての
``outgoing`` 辺に供給される。

空トークンが生じる情況：

   Any OutputPins that do not hold any tokens when the StructuredActivityNode
   completes offer null tokens on their ``outgoing`` edges. If no test section
   of a ConditionalNode results in a true value, then no ``body`` section is
   executed, no tokens are placed on any ``result`` OutputPins, and null tokens
   are offered from all these OutputPins.

OutputPins はどの ``outgoing`` 辺にも供給される。

   Any OutputPins that do not hold any tokens when the StructuredActivityNode
   completes offer null tokens on their ``outgoing`` edges. If no ``test``
   section of a ConditionalNode results in a true value, then no ``body``
   section is executed, no tokens are placed on any result OutputPins, and null
   tokens are offered from all these OutputPins.

ConditionalNode が実行を完了すると、内部で進行中の実行全てが停止され、その内部に
あるトークンはすべて破壊される。

ConditionalNode の実行中にトークンを受理する ActivityFinalNode をこの
ConditionalNode が直接含む場合、この ConditionalNode は直ちに完了する。この場
合、StructuredActivityNodes の ActivityFinalNode の規則に従い、ConditionalNodeを
直接含む ConditionalNode のみが停止される。

   A ConditionalNode may not have InputPins.

ActivityEdges は ConditionalNode の中と外を往来することが許されていて、
ConditionalNode 内の ExecutableNode の実行の指定元以外、意味は同じだ。

16.11.3.4 Loop Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

LoopNode とは、反復的なループを表現する StructuredActivityNode だ。LoopNode は
``setupPart``, ``test``, ``bodyPart`` で構成され、これらはその LoopNode に含まれ
る ExecutableNodes の部分集合を識別する。LoopNode にある ExecutableNode はいずれ
も ``setupPart``, ``test``, ``bodyPart`` のいずれかに含まれていなければならな
い。

LoopNode が実行を始めると、その内部にある InitialNodes はどれもが直ちに利用可能
になる。しかし、LoopNode に含まれる ExecutableNode は、それを含む ``setupPart``,
``test``, ``bodyPart`` のどれかがが実行されたときにのみ有効になる。

   When a section is executed, any ExecutableNode in the section that has no
   mandatory input data and no incoming ControlFlow *with a source in the same
   section* is enabled and receives a single control token.

* ただし、実行中でない節の ExecutableNode への供給は、即座に引き渡されず、保留さ
  れたままであることを除けば、Activities の通常の意味に従い進行する。
* 対象 ExecutableNode はそれを含む節の後の実行の一部として最終的に実行される場
  合、保留中の供給を受理することが許される。

ループの実行仕様：

   The ``setupPart`` of a LoopNode is executed first. When the ``setupPart`` has
   completed execution, the iterative execution of the loop begins. Execution of
   the ``test`` section may precede or follow execution of the ``bodyPart``,
   depending on whether ``isTestFirst`` is true or false, respectively.

以降の記述では ``isTestFirst`` が真であると仮定する。

   If the ``bodyPart`` is executed first (``isTestFirst`` = false), it is always
   executed at least once, after which the following description applies to
   subsequent iterations.

``test`` 節には LoopNode により識別される Boolean 型の ``decider`` OutputPin を
所有する Action がある。``test`` の実行が完了するとき、``decider`` の値が真であ
れば ``bodyPart`` が実行される。そうでなければこの LoopNode の実行が完了する。

``bodyPart`` の実行するたびに、ループの次の反復に備えて ``test`` 節が再び実行さ
れる。

   A LoopNode may also define a set of ``loopVariable`` OutputPins used to hold
   intermediate values during each loop iteration.

* これらの OutputPins は、反復中にループの ``test`` 節と ``bodyPart`` 節内で保持
  する値を利用できるようにするために、出発 ActivityEdges を持つことが許される。
* LoopNode が ``loopVariable`` OutputPins を持つ場合、``loopVariableInput``
  InputPins, ``bodyOutput`` OutputPins, ``result`` OutputPins の合致集合も持つ必
  要がある。

トークンの移動：

   When the LoopNode begins executing, the tokens on the ``loopVariableInput``
   InputPins are moved to the corresponding ``loopVariable`` OutputPins before
   the first iteration of the loop.

LoopNode の ``bodyPart`` の各実行が完了すると、``loopVariable`` OutputPins に
残っているトークンは破壊され、``bodyOutput`` OutputPins のトークンは対応する
``loopVariable`` OutputPins に複製ーされ、次の反復で利用可能になる。

``test`` が失敗し、ループが完了すると、最後の反復から ``bodyOutput`` 上のトーク
ンは ``result`` に移され、それらの OutputPins から出発する辺すべてに供給される。

   A LoopNode may not have any other InputPins or OutputPins than those
   described above. However, ActivityEdges may cross into and out of a LoopNode,
   as for StructuredActivityNodes in general, and the semantics are the same
   (see above), except that the execution of ExecutableNodes within the LoopNode
   is specified by the iterative looping semantics described above.

特に、ある反復で LoopNode に交差する ActivityEdge から受理したトークンは消費さ
れ、次の反復では利用できない。

16.11.3.5 Sequence Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A SequenceNode defines a complete, sequential ordering of all the
   ActivityNodes it contains, which must all be ExecutableNodes.

SequenceNode が実行されると、その中の各節点が順番に実行される。この SequenceNode
はその節点間に ActivityEdges を含むことがあり、ActivityEdges はこの SequenceNode
の内外を横断することが許される。

SequenceNode の意味は同じ節点と辺を含む一般的な StructuredActivityNode と同等だ
が、このSequenceNode で指定されたように、節点を順次順序付けるために ControlFlow
が追加されている。

16.11.4 Notation
----------------------------------------------------------------------

   Figure 16.46 Notation for StructuredActivityNode

StructuredActivityNode はその ``nodes`` と ``edges`` を囲む角丸矩形の破線で示さ
れ、上部にキーワード ``«structured»`` がある。

{Conditional,Loop,Sequence}Node には標準記法は定義されない。

16.11.5 Examples
----------------------------------------------------------------------

なし。

16.12 Expansion Regions
======================================================================

16.12.1 Summary
----------------------------------------------------------------------

   An ExpansionRegion is a StructuredActivityNode that executes its contained
   elements multiple times corresponding to elements of an input collection.

16.12.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 16.47 Expansion Regions

ExpansionRegion と ExpansionNode だけ。

ExpansionKind という enumeration がある。

16.12.3 Semantics
----------------------------------------------------------------------

   An ExpansionRegion is a StructuredActivityNode that takes as input one or
   more collections of values and executes its contained ActivityNodes and
   ActivityEdges on each value in those collections. If the computation produces
   results, these may be collected into output collections. The number of output
   collections can differ from the number of input collections.

* その計算が結果を生じる場合、出力収集に集められる。
* 出力収集の数は入力収集の数と異なることが可能だ。

   An ExpansionNode is an ObjectNode used to indicate a flow across the boundary
   of an ExpansionRegion.

* 領域の外側からはこれらの節点は収集として表示される。
* 領域の内側からは値はこの収集の要素として表示される。
* 収集とは実行機関が支持する構成要素であり、全体として扱うことも、要素値の集合と
  して扱うことも許されるものだ。

..

   An execution engine may define various kinds of collection types that it
   supports (sets, bags, and so on), individual instances of which may be
   constructed from element values and from which those element values may later
   be obtained.

このような収集オブジェクトは一つのトークン上の一つの値として引き渡される。実行機
関は ExpansionNode に一緒に置かれたトークンの群れで引き渡される値の集合として、
暗黙の了解で収集を支えることもある。

   If an ExpansionRegion has multiple input ExpansionNodes, then each one must
   handle the same kind of collection (set, bag, or so on), although the types
   of the elements in different collections may vary.

* 収集の種類が収集型として表される場合、これが ExpansionNodes の ``type`` として
  用いられる。
* それ以外の場合、ExpansionNodes の ``type`` は収集内の要素の ``type`` を表す。

ExpansionRegion は Action の通常の規則 (16.2.3) に則って実行を始める。

   In addition, if the input ExpansionNodes for the ExpansionRegion have
   collection types, then a collection instance must be placed on each
   ExpansionNode before the ExpansionRegion may begin executing. Otherwise,
   there is no constraint on whether any input ExpansionNode contains any tokens
   (as an ExpansionNode with no token is interpreted as the empty collection in
   this case).

ExpansionRegion が実行開始すると、入力 ExpansionNode 内のトークンすべてを取り除く。

   Then the group of ActivityNodes and ActivityEdges contained in the
   ExpansionRegion is executed once for each element of the input collections.
   These will be referred to as the :dfn:`expansion executions` for the
   ExpansionRegion.

この収集の要素数が異なる場合、拡大実行の数は最小の収集のサイズに等しい。

各拡大実行は、以下の特別な規則を除き、一般的な StructureActivityNode の実行と同
じ意味で、他の実行から独立して進行する：

* 拡大実行それぞれの内部では、入力 ExpansionNode をその ``source`` とし、
  ExpansionRegion の内側に ``target`` があるActivityEdge それぞれに単一のトーク
  ンが供給される。

  このトークンはその入力 ExpansionNode 上の収集の個々の要素を値として含む。この
  ような収集それぞれに、各拡大実行ごとに異なる要素が供給される。

  * 収集が集合でない（一意でない）場合、重複値は異なる要素とみなされる。
  * 収集が順序付けられている場合、各収集からの要素は、各実行（ある実行は入力収集
    の位置 1 から要素をすべて取得し、別の実行は位置 2 からすべて取得し、など）の
    ために、実行数まで順番に整列される。
  * 収集が順序付けられていない場合、個々の要素がどの実行に配送されるかは未定義
    だ。
* 拡大実行それぞれはその ``source`` が ExpansionRegion の内側にあり、その出力
  ExpansionNode を ``target`` とする ActivityEdge にトークンを供給することになっ
  てもかまわない。

  このようなトークンは直ちにこの ExpansionNode に受理され、その ExpansionNode の
  出力収集に追加される。

  * 入力収集と出力収集の両方が順序付けられている場合、各実行が与える値は入力収集
    によってその実行により導かれるのと同じ順序で連結される。
  * 各実行が単一の値を生じる場合、出力収集は最小の入力収集と同じ要素数を持つ。出
    力収集が順序付けられている場合、入力収集の同じ位置の入力に対応する各位置に出
    力を持つ。

       On the other hand, if each execution may or may not produce a value, then
       the output collection will have fewer elements than the input collections
       and the ExpansionRegion will act as a kind of filter. Finally, if each
       execution can produce more than one value, then the output collection may
       end up with a greater number of elements than the input collections.
* ExpansionRegion の InputPins に配置されたトークンは拡大実行ごとに複製され、拡
  大実行のそれぞれが InputPins から出発 ActivityEdges 上のトークンの異なる複製が
  供給される。

     In this way, tokens consumed from an InputPin in one expansion execution do
     not affect the tokens available from the InputPin in other executions (the
     tokens on the InputPin effectively appear to be “constant” across the
     executions).

  同様に、ExpansionRegion の外からそれに交差する ActivityEdges 上供給されるトー
  クンは、各拡大実行に対して複製される。ActivityEdge それぞれの ``target`` が各
  拡大実行内で別々の複製を供給される。
* ExpansionRegions には、その内側から外部へ渡る OutputPins や ActivityEdges が
  あってもかまわない。しかし、ExpansionRegion の内部からそのような OutputPins ま
  たは ActivityEdges にトークンを供給する意味は定義されない。

ExpansionRegion が拡大実行のすべてを完了すると、出力 ExpansionNodes 上の出力収集
をそれらのノードから出発 ActivityEdges のすべてに供給する。

ExpansionRegion が ActivityFinalNode を含む場合、その ActivityFinalNode がいずれ
かの拡大実行内でトークンを受理すると、現在進行中の拡大実行はすべて終了
し、ExpansionRegion 全体としての実行が完了する。この場合でも、出力 ExpansionNode
から出力収集が供給されるものの、その中身は部分的にしか満たされない場合がある。

ExpansionRegion の ``mode`` はその拡大実行の実行がどのように進行するかを制御す
る：

``parallel``
  拡大実行の実行は同時に進行する。これは実行機関が実行を並列に稼動させるか、時間
  上的に重なり合って稼働させることを可能にするが、これは必須ではない。実行を逐次
  的に稼動させるならば、実行順序は定義されない。
``iterative``
  拡大実行の実行は反復的な順序で行うものとする。ある実行が完了してから他のものが
  始まる。

     The first expansion execution begins immediately when the ExpansionRegion
     starts executing, with subsequent executions starting when the previous
     execution is completed.
``stream``
  ちょうど一つの拡大実行があり、各要素は収集それぞれからの流れによりこの実行に供
  給される。入力 ElementNode 上の収集の各要素が ExpansionRegion から出発
  ActivityEdges すべてに、トークンとして一つ一つ別々に供給される。

16.12.4 Notation
----------------------------------------------------------------------

   Figure 16.48 Expansion Region

ExpansionRegion は破線丸角枠で記す。左上隅に ``«parallel»``, ``«iterative»``,
``«stream»`` のいずれかのキーワードがある。

入力と出力の ExpansionNodes は小さい短冊のような記号で記す。これらの記号は破線枠
上に配置する。

ExpansionRegion の内側と外側に ActivityEdge 矢印があれば、入力と出力の拡張節点を
区別されるだろう。そうでない場合に Pins と同様の小矢印を用いることが可能だ。

   Figure 16.49 Shorthand notation for expansion region containing single node

速記法として、ExpansionNode リストボックス記法を Action 記号に直接配置し、この
Action の Pins を置き換えることが許される。

この略記法では

* Behavior の in/input Parameter に対応する入力 ExpansionNode 一つと、
* Behavior の out/inout/return Parameter に対応する出力 ExpansionNode 一つ

が必要だ。

   Figure 16.50 Full form of previous shorthand notation

Fig 16.49 を完全形式で示すとこうなる。

..

   Figure 16.51 Notation for expansion region with one behavior invocation

単一の CallBehaviorAction を含む ExpansionRegion のさらなる省略記法。

これは Fig. 16.49 の記法を使用して示されているが、``mode`` キーワードを使用する
代わりに、右上隅に "*" が置かれている。

* これは「多重実行」を含意している。
* この記法は ``mode`` が parallel である CallBehaviorAction を含む
  ExpansionRegion に写される。

16.12.5 Examples
----------------------------------------------------------------------

   Figure 16.52 Expansion region with two inputs and one output

二つの入力と一つの出力があり、並行実行 («parallel») される ExpansionRegion の見
本。

* 実行は両方の入力が利用可能になるまで始まらない。
* 両方の収集には同数の要素があることを期待している。
* ExpansionRegion 内部は入力収集の各要素について一度ずつ実行される。
  その各実行一回中、各収集から値の組一つが利用可能。
* 各実行は出力 ExpansionNode に結果値を生成する。結果値はすべて入力収集
  と同じ大きさの収集となる。
* 出力収集はすべての並列実行が完了した後、出力 ExpansionNode 上の
  ExpansionRegion の外部で利用可能になる。

..

   Figure 16.53 Expansion Region

ExpansionRegion を含む高速 Fourier 変換計算の断片の見本だ。

* ExpansionRegion の外側で複素数の配列に対する演算がある。
* ``S``, ``Slower``, ``Supper``, ``V`` は配列だ。
* ExpansionRegions 中の式に見える ``cut`` および ``shuffle`` は配列に作用する
  演算だ。
* 領域の内側では、二つの算術演算が入力配列三個 (``lower``, ``upper``, ``root``)
  の要素に対して行われ、出力配列二個 (``nxteven``, ``nxtodd``) が得られる。
* 配列内の異なる位置同士は相互作用しないので、ExpansionRegion はすべての位置で並
  列実行することが可能だ。

..

   Figure 16.54 Examples of expansion region shorthand

単一の Action がある ExpansionRegion の略記法の見本。

航空券の予約とホテルの予約が独立かつ並列だ。

* ``Specify Trip Route`` Action は ``Book Flight`` の集合と ``Book Hotel`` の集
  合を出力する。
* ホテルを独立して予約することも、互いに並行して予約することも、搭乗予約と並行し
  て予約することも許される。

..

   Figure 16.55 Shorthand notation for expansion region

``Specify Trip Route`` が複数の ``Book Flight`` 断片にまとまることが可能で、それ
ぞれを個別に予約する必要がある。

それに渡された集合の各搭乗断片に対して一度ずつ、``Book Flight`` Behavior を複数
回呼び出す。

16.13 Other Actions
======================================================================

16.13.1 Summary
----------------------------------------------------------------------

   ReduceActions for repeatedly invoking a Behavior to reduce a collection of
   values to a single value, and RaiseExceptionAction for raising exceptions.

16.13.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 16.56 Other Actions

ReduceAction には {Input,Output}Pin の両方があるが、RaiseExceptionActionには
InputPin だけがある。

16.13.3 Semantics
----------------------------------------------------------------------

16.13.3.1 Reduce Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A ReduceAction is an Action that reduces a collection to a single value by
   combining the elements of the collection.

* 入力収集は ``collection`` InputPin で与えられる。
* ``reducer`` Behavior は入力 Parameter 一つと出力または戻り Parameter 一つが必
  要だ。
* 収集要素 ``type`` を持つ ``result`` OutputPin が一つある。

..

   An execution engine may define various kinds of collection types that it
   supports (set, bag, and so on), individual instances of which may be
   constructed from element values and from which those element values may later
   be obtained.

このような収集物は単一トークンに単一値として引き渡される。この場合、ReduceAction
の ``collection`` InputPin はその ``type`` が収集型であり、多重度は ``1..1`` で
あるようになるべくする。

代わりに、実行機関は InputPin に一緒に置かれたトークンの一団で渡された値の集合と
して、暗黙の了解で収集を支えてもよい。この場合、ReduceAction の ``collection``
InputPin はこの収集の要素と同じ ``type`` を持ち、多重度は 1 より大きく、通常は
``*`` であるようになるべくする。

   A ReduceAction executes by repeatedly invoking the ``reducer`` Behavior on an
   intermediate copy of the input collection.

この ``reducer`` を呼び出すたびに中間収集から要素が二つ削除され、この呼び出しの
実引数として働く。この呼び出しから返る値が中間収集に追加され、呼び出し前よりサイ
ズが 1 小さくなり、``reducer`` が再び呼び出される。

   This process continues until the collection has only one element. This
   element is then placed on the ``result`` OutputPin and the ReduceAction
   execution completes.

入力収集が順序なしであるか、または InputPin の ``isOrdered`` が偽であれ
ば、中間収集のどの要素が ``reducer`` 呼び出しの実引数として選択されるのかが不確
定となる。

入力収集が順序付けられている場合、または InputPin の ``isOrdered`` が真であれ
ば、中間収集の先頭二つの要素が常に ``reducer`` の呼び出しの実引数として使用さ
れ、呼び出しの結果は収集の最初の要素として追加される。

``reducer`` Behavior が可換律かつ結合律を満たす演算であれば、順序なし収集または
``isOrdered`` が偽であることは ReduceAction の結果に影響しないはずだ。

``reducer`` Behavior が非可換だが結合律を満たす演算（行列の乗算のような）である
場合、中間収集の要素を選択する順序が簡約計算の結果に影響するはずだ。

   If it is desired to avoid nondeterminacy in this case, collections may be
   ordered or ``isOrdered`` set to true, so the ``reducer`` Behavior will be
   applied to adjacent pairs according to the collection order.

その呼び出しが互いに影響し合う可能性がある副作用が ``reducer`` Behavior にある場
合、``isOrdered`` が偽である ReduceAction の結果は予測不能であってもかまわない。

16.13.3.2 Raise Exception Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A RaiseExceptionAction is an Action that causes an exception to occur.

* 正常に終了するのではなく、例外を送出することで完了する。
* ``exception`` InputPin において与えられた値が例外として送出される。

..

   If the RaiseExceptionAction itself has an ExceptionHandler (see sub clause
   15.5) that matches the raised exception, then the exception is caught by that
   handler. Otherwise, the exception propagates outward to the innermost
   containing StructuredActivityNode of the RaiseExceptionAction.

この StructuredActivityNode が発生した例外に合致する ExceptionHandler を持ってい
る場合、この例外はその処理者によって捕捉される。

例外が StructuredActivityNode の外に伝わると（この節点上の ExceptionHandler に
よって捕捉される場合も含め）、その StructuredActivityNode は停止する。捕捉される
場合、処理者の実行後、(15.5.3) のようにこの StructureActivityNode から制御トーク
ンとオブジェクトトークンが供給される。捕捉されない場合にはどちらも供給されない。

RaiseExceptionAction が実行された Behavior 内のある階層の ExceptionHandler で
例外が捕捉されなかった場合、その Behavior の実行は停止する。

* この Behavior が同期的に呼び出された場合、この例外はその Behavior の呼び出し元
  に波及する (cf. 16.3.3)。
* この Behavior が非同期的に呼び出された場合、この例外の波及はこの Behavior の実
  行停止とともに終了する。

16.13.4 Notation
----------------------------------------------------------------------

ReduceActions と RaiseExceptionActions に特化した記法は定義されない。

16.13.5 Examples
----------------------------------------------------------------------

ReduceAction は数のリストをその数の和へ簡約するのに使える。

   Such a ReduceAction has one InputPin for a collection of numbers, one
   OutputPin for a number and an addition function as the ``reducer`` Behavior.

例えば、入力収集に整数の組 :math:`(2, 7, 5, 3)` があるとする。このコレク
ションに加算関数で ReduceAction を適用した結果は 11 だ。

既定の ``isOrdered`` が偽である場合には、これはいくつかのやり方で計算可能だ。例
えば :math:`{(((2 + 7) + 5) + 3),}\,{(2 + (7 + (5 + 3))),}\,{((2 + 7) + (5 +
3)).}`

16.14 Classifier Descriptions
======================================================================

機械生成による節。

16.15 Association Descriptions
======================================================================

機械生成による節。

.. include:: /_include/uml-refs.txt
