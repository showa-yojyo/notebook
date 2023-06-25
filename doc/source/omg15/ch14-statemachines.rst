======================================================================
14 StateMachines
======================================================================

.. contents::
   :depth: 4

14.1 Summary
======================================================================

StateMachine はその関連概念のパッケージだ：

   The StateMachines package defines a set of concepts that can be used for
   modeling discrete event-driven Behaviors using a finite state-machine
   formalism.

プロトコルとはシステムの部分的相互作用の連なりだ：

   In addition to expressing the Behavior of parts of a system (e.g., the
   Behavior of Classifier instances), state machines can also be used to express
   the valid interaction sequences, called :dfn:`protocols`, for parts of a
   system.

ここで二種類の状態機械が現れた。それらに名称を与える：

   These two kinds of StateMachines are referred to as :dfn:`behavior state
   machines` and :dfn:`protocol state machines` respectively.

UML で用いられる有限状態人形は David Harel の statecharts 形式論をオブジェクト指
向に変奏したものだ。

14.2 Behavior StateMachines
======================================================================

14.2.1 Summary
----------------------------------------------------------------------

挙動 StateMachines は次のどれかを明確に記述することが可能だ：

* 能動的 Class の ``classifierBehavior``
* BehavioredClassifier の ``ownedBehavior`` であって、この BehavioralClassifier
  の ``classifierBehavior`` でないもの
* 単独 Behavior すなわち対応する BehavioredClassifier のないもの
* BehaviorFeature (Operation or Reception) に対応するメソッド

14.2.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 14.1 Behavior StateMachines

まさに機械の名に相応しい図式だ。あまりに関連が多いため、コネクターが一部交差して
しまっている。

新登場クラスが StateMachine, Region, Vertex, Transition, Pseudostate,
ConnectionPointReference, State, FinalState と、とにかく多い。

``A_region_stateMachine``
  StateMachine から Region への複合関連（双方向）。StateMachine が直接所有する
  Regions だ。

  * 関連端 ``region`` の多重度は ``1..*`` だ。必ず一つは存在する。

``A_connectionPoint_stateMachine``
  StateMachine から ConnectionPointReference への複合関連（双方向）。
  StateMachine が ``submachine`` State の一部として用いられているときに定義す
  る。

``A_submachineState_submachine``
  StateMachine から State への関連（双方向）。

  ``submachine`` State の際に StateMachine が参照する ``submachine(s)`` だ。複数
  個を参照する条件は、concurrency が関係してくるらしい。

``A_subvertex_container``
  Region と Vertex の間の複合関連（双方向）。Region が Vertices を所有する。

``A_transition_container``
  Region と Transition の間の複合関連（双方向）。Region が Transitions を所有す
  る。

  * 関連端 ``container`` の多重度が 1 なので、任意の Transition は必ずある
    Regionに属する。

``A_incoming_target``, ``A_outgoing_source``
  Vertex と Transition の間の関連（双方向）。

  * 一つの Transition には ``source`` と ``target`` という Vertex が一つずつ
    対応する。
  * 関連端 ``incoming`` と ``outgoing`` は ``readOnly`` だ。

``A_region_state``
  State から Region への複合関連（双方向）。

  State は StateMachine と同様に Regions を所有する能力がある。ただし関連端
  ``region`` の多重度は ``*`` だ。

``A_stateInvariant_owningState``
  State から Constraint への複合関連（単方向）。

  この State が current であるときに常に成り立つ条件、不変条件だ。

  * 関連端 ``stateInvariant`` の多重度は ``0..1`` なので、オプションだ。

``A_deferrableTrigger_state``
  State から Trigger への複合関連（双方向）。

  State は遅延可能トリガー（後続のある State configuration に到達するまでに処理
  されていればよいトリガー）を任意個所有する。

  * スラッシュの後に書かれているアレ。

``A_entry_state``, ``A_doActivity_state``, ``A_exit_state``
  State から Behavior への参照。

  * Behavior 側関連端の意味については先ほどのノート参照。
  * Behavior 側のいずれの関連端の多重度も ``0..1`` なので、これらの挙動の定義は
    オプションだ。

``A_connection_state``
  State から ConnectionPointReference への複合関連（双方向）。

  * この ``submachine`` State と一緒に用いる ``entry``/``exit`` 接続点（複数形）
    を所有する。
  * cf. ``A_entry_connectionPointReference``, ``A_exit_connectionPointReference``

``A_connectionPoint_state``
  State から Pseudostate への複合関連（双方向）。

  自身が複合 State であるときに限り、その ``entryPoint`` と ``exitPoint`` を定
  義・所有する。

``A_entry_connectionPointReference``, ``A_exit_connectionPointReference``
  ConnectionPointReference から Pseudostate への関連（単方向）。

  対応する ``entryPoint``/``exitPoint`` への関連を示す。

``A_trigger_transition``
  Transition から Trigger への複合関連（単方向）。

  この Transition を引き起こして Triggers だ。

``A_effect_transition``
  Transition から Behavior への複合関連（単方向）。

  関連端 ``effect`` はこの Transition が起こるときに実施される挙動。多重度が
  ``0..1`` なのでオプション。

``A_guard_transition``
  Transition から Constraint への複合関連（単方向）。

  ガード条件を表す。この ``guard`` が ``true`` になれば Transition は使用可能に
  なる。

  * 関連端 ``guard`` の多重度が ``0..1`` なのでオプション。

14.2.3 Semantics
----------------------------------------------------------------------

14.2.3.1 StateMachine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

挙動 StateMachine の構造：

   A *behavior* StateMachine comprises one or more Regions, each Region
   containing a graph (possibly hierarchical) comprising a set of Vertices
   interconnected by arcs representing Transitions.

状態機械の実行は適切な Event の発生により引き起こされる。

   A particular execution of a StateMachine is represented by a set of valid
   path traversals through one or more Region graphs, triggered by the
   dispatching of an Event occurrence that *match* active Triggers in these
   graphs.

経路走査の過程で実行されるのは：

   In the course of such a traversal, a StateMachine instance may execute a
   potentially complex sequence of Behaviors associated with the particular
   elements of the graphs that are being traversed (transition ``effects``,
   state ``entry`` and state ``exit`` Behaviors, etc.)

StateMachine が BehavioredClassifier の context を持つ場合、その Classifier が次
を定義する：

* その StateMachine に適用できる Signal および CallEvent 駆動装置
* その StateMachine が所有する Behaviors が利用できる Features

Signal と CallEvent 各駆動装置は、それぞれこの Classifier の Receptions と
Operation に従って定義される。Features を利用して StateMachine のメッセージイベ
ント駆動装置を定義することが許される。

   If the StateMachine has no BehavioredClassifier context (i.e., it is a
   stand-alone Behavior), then its Triggers do not need to be tied to any
   Receptions or Operations of some Classifier.

例として、このような StateMachine は駆動装置を TemplateParameters として定義され
るかもしれない。TemplateParameters に適切な CallEvent や SignalEvent を束縛する
ことで、異なる ``context`` Classifiers で再利用することが可能だ。

   In situations where a StateMachine specifies the ``method`` of a
   BehavioralFeature (Operation or Reception), the Parameters of the
   StateMachine shall match the Parameters of the BehavioralFeature (see sub
   clause 13.2.3).

これは StateMachine の実行が BehaviorFeature の Parameter を入手するための手段
だ。それ以外の場合、実行中の StateMachine オブジェクトが発送された Event 発生と
その関連データを入手する方法は定義されていない (:doc:`./ch13-common-behavior`)。

   By definition, invocations of StateMachine executions result in triggered
   effects (see sub clause 13.3.3) and, hence, there is an associated event pool
   with such an execution.

StateMachine 実行に対するイベントプールが所属するのは次のどちらかだ：

* その ``context`` の Classifier オブジェクト
* この StateMachine が BehavioralFeature の ``method`` を定義する場合には、この
  挙動機能を所有する Classifier のオブジェクト

..

   Due to its event-driven nature, a StateMachine execution is either *in
   transit* or *in state*, alternating between the two.

関連する Triggers の少なくとも一つに合致するイベントが発送されるときが遷移中 (in
transit) だ。この間、その経路に関連する複数の Behaviors を実行することがある。

   NOTE. A StateMachine execution may be executing Behaviors even when it has
   settled in a stable state configuration, in cases where there are
   ``doActivity`` Behaviors associated with its active state configuration.

14.2.3.2 Regions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Region の定義：

   A Region denotes a behavior fragment that may execute concurrently with its
   orthogonal Regions.

Regions が互いに直交するの意味は、次のどちらかが成り立つことを意味する：

* 同一の State が両方の Regions を所有する。
* 最上層においては同一の StateMachine が両方の Regions を所有する。

Region には active であるという概念がある：

   A Region becomes *active* (i.e., it begins executing) either when its owning
   State is entered or, if it is directly owned by a StateMachine (i.e., it is a
   top level Region), when its owning StateMachine starts executing.

Region それぞれは Vertices と Transitions の集合を所有し、それらはこの Region 内
部の挙動の流れを決定する。

Region は特殊な状態を二つ所有することがある：

   It may have its own **initial** Pseudostate as well as its own FinalState.

既定作動？の定義：

   A *default activation* of a Region occurs if the Region is entered
   implicitly, that is,

State や **history** Pseudostate などの一つを終端とする入方向遷移によって進入す
るのではなく、以下のどちらかだ：

* 包含 State 上で終了する (**local** または **external**) Transition によって
  か、
* 最上層 Region の場合は StateMachine が実行を開始するとき

..

   *Default activation* means that execution starts with the Transition
   originating from the initial Pseudostate of the Region, if one is defined.

Region 内に存在する **initial** Pseudostate が存在しない場合、特定の approach は
定義されていない。モデルが未定義であるとみなすという approach が可能だ。あるい
は、Region を含む State は動作中だが、Region は inactive のままとするのも可能
だ。

   In other words, the containing composite State is treated as a simple (leaf)
   State.

明示的作動？の定義：

   Conversely, an *explicit activation* occurs when a Region is entered by a
   Transition terminating on one of the Region’s contained Vertices.

直交 Regions の一つが明示的に動作中になると、それらも明示的に進入されない限り、
直交する Regions すべてが既定作動中になる。（※複数の直交 Regions は、同じ
**fork** Pseudostate から発生する Transitions によって並行に明示的に進入すること
が可能）。

14.2.3.3 Vertices
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vertex の定義：

   Vertex is an abstract class that captures the common characteristics for a
   variety of different concrete kinds of nodes in the StateMachine graph
   (States, Pseudostates, or ConnectionPointReferences).

例外もあるが、Vertex は任意の個数の Transitions の ``source`` または ``target``
の両方かどちらか一方であることが可能だ。

一般に、Pseudostates と ConnectionPointReferences は複合遷移の実行が単にそれらを
通過し、``incoming`` Transition で到着し、``outgoing`` Transition で間を置かずに
退出するという意味で、推移的 (transitive) である。

しかし、State と FinalState は安定した (stable) Vertices を表し、StateMachine の
実行がそこに入ると、別の State に移動する遷移を引き起こすイベントが発生する
か、StateMachine が終了するまでその中にとどまる。

14.2.3.4 States
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

State の定義：

   A State models a situation in the execution of a StateMachine Behavior during
   which some invariant condition holds.

ほとんどの場合、この条件は明示的に定義されていないが、通常は State に関連する名
前によって暗示される。例えば Figure 14.36 では、これは電話器の挙動のモデル化であ
るが、状態 Idle と Active は電話が使用中と未使用中である状況をそれぞれ表す。

14.2.3.4.1 Kinds of States
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

State の種類は次のように三種類に区別される：

単純 State (``isSimple == true``)
   単純 State は Vertices や Transitions が内部にない。
複合 State (``isComposite == true``)
   複合 State は少なくとも一つの Region を含む。

   複合 State は Region を一つ持つ単純な複合 State と、Regions を複数有する直交
   State のどちらかになる。
部分機械 State (``isSubmachineState == true``)
   部分機械 State は StateMachine 全体を指し、概念的には State の内部に「入れ
   子」になっているとみなされる。

部分状態 (substate) の定義と分類：

部分 State
   複合 State の Region 内にある State
直接部分 State
   他のどの State 内にもない部分 State
間接部分 State
   直接的部分状態でない State

14.2.3.4.2 State configurations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

StateMachine は複数 Regions を含み、それぞれが States を含み、そのうちのいずれか
は複数 Regions を含む……というように、その構成は一般的には複雑だ。

   This complex hierarchy of States is referred to as a :dfn:`state
   configuration` (of a State or a StateMachine).

作動中状態構成の概念：

   An executing StateMachine instance can only be in exactly one state
   configuration at a time, which is referred to as its :dfn:`active state
   configuration`.

StateMachine の実行は、StateMachine の Triggers に合致するイベントの発生に応答し
て、ある作動中状態構成から別の構成に遷移することで表現される。

状態が作動中であることを、作動中状態構成との関係で定義する：

   A State is said to be active if it is part of the active state configuration.

状態状態構成が安定 (stable) であるとは、次の場合を言う：

* その状態構成から遷移可能な Transitions がそれ以上なく、かつ
* その状態構成の ``entry`` Behaviors が（もしあれば）すべてが完了する（ただし
  ``doActivity`` が定義されている場合はその限りでない）。

..

   After it has been created and completed its initial Transition, a
   StateMachine is always “in” some state configuration.

StateMachine のイベントプールで保留中の遅延、完了、またはその他の種類の Event 発
生のときでさえ、構成は安定しているとみなされる。

14.2.3.4.3 State ``entry``, ``exit``, and ``doActivity`` Behaviors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   A State may have an associated ``entry`` Behavior.

この Behavior が定義されていれば **external** Transition によって State に進入す
るときにはいつでも実行される。さらに：

   a State may also have an associated ``exit`` Behavior, which, if defined, is
   executed whenever the State is exited.

   A State may also have an associated ``doActivity`` Behavior.

この Behavior は State に進入した時点で実行を開始し（ただし、State ``entry``
Behavior が完了した後に限る）、State に関連する他の Behaviors と同時に、次の時
間まで実行する：

* それが完了する（この場合、完了イベントが生成される）か、
* State から離れるとき。この場合、``doActivity`` Behavior の実行が中断される。

..

   The ``execution`` of a doActivity Behavior of a State is not affected by the
   firing of an internal Transition of that State.

14.2.3.4.4 State history
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

State 履歴の概念は複合状態の Regions に関係する有用な概念だ。 Region はそれが最
後に終了したときにそれがあった状態構成を追跡する。これにより、次にこの Region が
（割り込み処理から復帰したなど）作動中になったとき、またはその履歴に戻る
**Local** Transition がある場合、同じ状態構成を容易に復元することができる。

履歴 Pseudostates には二種類がある：

深い履歴 (**deepHistory**)
   包含 Region への最も直近の訪問の完全 (full) 状態構成を表す。
浅い履歴 (**shallowHistory**)
   既定進入規則を使って進入された、最新の状態構成の最上位部分状態 (topmost
   substate) にしか復帰しないことを表す。

..

   In cases where a Transition terminates on a history Pseudostate when the
   State has not been entered before (i.e., no prior history) or it had reached
   its FinalState, there is an option to force a transition to a specific
   substate, using the *default history mechanism*.

* これは、履歴 Pseudostate を起点とし、この Pseudostate を含む Region の特定の
  Vertex（これが既定履歴状態だ）で終了する Transition だ。この Transition は実行
  が履歴 Pseudostate に導かれ、その State がそれまで作動中でなかった場合にのみ実
  行される。そうでない場合は、その Region への適切な履歴エントリーが実行される
  （上記）。
* 既定履歴遷移が定義されていない場合、後述のように、Regions の標準既定エントリー
  が実行される。

遅延 Events:

   A State may specify a set of Event types that may be deferred in that State. This means that Event occurrences of those
   types will not be dispatched as long as that State remains active.

その代わり、これらの Event 発生はイベントプールに次のいずれかまで残る：

* これらの Event 型がもはや延期されない状態構成に到達するまで
* 延期された Event 型が、延期された状態を起点とする遷移の Trigger において明示
  的に使用される場合。ある種の上書きオプションだ。

..

   An Event may be deferred by a composite State or submachine States, in which
   case it remains deferred as long as the composite State remains in the active
   configuration.

14.2.3.4.5 Entering a State
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   The semantics of entering a State depend on the type of State and the manner
   in which it is entered.

しかし、どのような場合でも次のことが共通する：

* State の ``entry`` Behavior が（定義されていれば）実行され、その後、到着
  Transition に関連した ``effect`` Behavior が完了した後に実行される。
* State に ``doActivity`` Behavior が定義されている場合、この Behavior は

  * ``entry`` Behavior が実行された後に即座に実行される。
  * 同じ複合遷移の一部として進入した部分状態の ``entry`` Behavior など、State へ
    の進入に関連する後続 Behaviors と同時に (concurrently) 実行される。

上記の説明で単純 State の場合は完全に網羅している。単一 Region からなる複合
States の場合には、次の選択肢がある：

既定進入 (default entry)
  この状況は、複合 State が Transition の直接的 ``target`` である場合に起こる。

  ``entry`` を実行し、``doActivity`` の実行を分岐した後、**initial** Pseudostate
  が定義されていれば、その Vertex から出発 Transition（State の既定 Transition
  として知られている）を経由して State 進入を継続する。

  初期 Pseudostate が定義されていない場合、単一の approach は定義されていない。
明示的進入 (explicit entry)
  到着 Transition またはその継続が複合 State の直接含まれる部分状態で終了した場
  合、その部分状態は作動中となり、その ``entry`` Behavior は含んでいる合成
  State の ``entry`` Behavior の実行後に実行される。

     This rule applies recursively if the Transition terminates on an indirect
     (deeply nested) substate.
浅い履歴進入 (shallow history entry)
  到達 Transition が複合 State のある Region の **shallowHistory** Pseudostateで
  終了する場合、作動中の部分状態は次の項目までこのエントリーの前に直近に作動中
  だった部分状態になる：

     * the most recently active substate is the FinalState, or
     * this is the first entry into this State.
     * In the latter two cases, if a default shallow history Transition is
       defined originating from the **shallowHistory** Pseudostate, it will be
       taken. Otherwise, default State entry is applied.

深い履歴進入 (deep history entry)
  この場合の規則は、``target`` Pseudostate が **deepHistory** 型であることと、
  これより下の作動中状態構成の階層すべてに対して規則が再帰的に適用されること
  を除いて、浅い履歴の場合と同じだ。
入口進入 (entry point entry)
  Transition が **entryPoint** Pseudostate を経由して複合 State に進入する場合、
  その入口を起点としてこの State に進入する出発 Transition に関連する ``effect``
  Behavior だ。

..

   If the composite State is also an orthogonal State with multiple Regions,
   each of its Regions is also entered, either by default or explicitly.

* Transition が複合 State の端で終了する場合、つまり複合 State に入ることがない
  場合、Regions のすべてが上記の既定進入規則を用いて進入される。
* Transition が明示的に一つ以上の Regions に進入する場合（分岐の場合）、これらの
  Regions は明示的進入をされ、他の Regions は既定進入される。

..

   Regardless of how a State is entered, the StateMachine is deemed to be “in”
   that State even before any ``entry`` Behavior or ``effect`` Behavior (if
   defined) of that State start executing.

14.2.3.4.6 Exiting a State
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   When exiting a State, regardless of whether it is simple or composite, the
   final step involved in the exit, *after all other Behaviors associated with
   the exit are completed*, is the execution of the ``exit`` Behavior of that
   State.

``exit`` が本当に最後に実行される。

   If the State has a ``doActivity`` Behavior that is still executing when the
   State is exited, that Behavior is aborted *before* the ``exit`` Behavior
   commences execution.

``doActivity`` があり、かつまだ実行中の場合には abort される。

   When exiting from a composite State, ``exit`` commences with the innermost
   State in the active state configuration. This means that ``exit`` Behaviors
   are executed in sequence starting with the innermost active State.

**exitPoint** Pseudostate を経由して退出する場合、State の ``exit`` Behavior
は、出口点で終了する Transition の ``effective`` Behavior の後に実行される。

   When exiting from an orthogonal State, each of its Regions is exited. After
   that, the ``exit`` Behavior of the State is executed.

State の終了方法にかかわらず、StateMachine は、その State の ``exit`` Behavior
（定義されている場合）の実行が完了した後にのみ、その State から離脱したとみなさ
れる。

カプセル化された複合 States:

   In some modeling situations, it is useful to encapsulate a composite State,
   by not allowing Transitions to penetrate directly into the State to terminate
   on one of its internal Vertices.

用例としては、抽象 Classifier の State の内部が異なる部分型洗練で違ったふうに指
定されることが意図されている場合がある。

   Despite the encapsulation, it is often necessary to bind the internal
   elements of the composite State with incoming and outgoing Transitions.

これは入口点と出口点によって行われ、それらは **entryPoint** と **exitPoint**
Pseudostates によって実現される。

入口点：

   :dfn:`Entry points` represent termination points (``sources``) for incoming
   Transitions and origination points (``targets``) for Transitions that
   terminate on some internal Vertex of the composite State.

後者は事実上、外部からの到着 Transition の継続であり、到着 Transition の
``effect`` Behavior と出発 Transition の ``effect`` Behavior の間に、複合 State
の ``entry`` Behavior の実行（定義されている場合）が発生することを条件とする。

   If there is no outgoing Transition inside the composite State, then the
   incoming Transition simply performs a default State entry.

出口点は入口点の逆のものだ。

   That is, Transitions originating from a Vertex within the composite State can
   terminate on the exit point.

まともなモデルでは、このような Transition は終了する Transition の継続を表す、同
じ出口点から出発する対応する外部 Transition をなるべく持つ。複合 State に
``exit`` Behavior が定義されている場合、その Behavior は、到着される内部
Transition の ``effect`` Behavior の後、かつ出発される外部 Transition の
``effect`` Behavior の前に実行される。

14.2.3.4.7 Submachine States and submachines
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Submachine:

   Submachines are a means by which a single StateMachine specification can be
   reused multiple times. They are similar to encapsulated composite States in
   that they need to bind incoming and outgoing Transitions to their internal
   Vertices.

部分機械はプログラミング言語におけるマクロのように、相異なる Behavior の仕様であ
り、それらが使用される context とは異なる context で定義されることがある。より複
雑な束縛が必要となる。

   This is achieved through the concept of *submachine* State (i.e., States with
   ``isSubmachineState`` = true), which represent references to corresponding
   submachine StateMachines. The concept of ConnectionPointReference is provided
   to support binding between the submachine State and the referenced
   StateMachine.

ConnectionPointReference:

   A ConnectionPointReference represents a point on the submachine State at
   which a Transition either terminates or originates.

* ConnectionPointReference は到着 Transitions に対する部分機械 State への標的で
  あり、出発 Transitions に対する部分機械 State からの出処でもある。
* ConnectionPointReference それぞれは参照される部分機械 StateMachine にある対応
  入口点または出口点と合致する。

部分機械とその仕様の間に要する束縛の仕組みは以上だ。

   A submachine State implies a macro-like insertion of the specification of the
   corresponding submachine StateMachine. It is, therefore, semantically
   equivalent to a composite State.

部分機械 StateMachine の Regions は複合 State の Regions だ。その ``entry``,
``exit``, ``effect`` Behaviors および **initial** Transitions を部分機械 State
が含むように定義される。

   NOTE. Each submachine State represents a distinct instantiation of a
   submachine, even when two or more submachine States reference the same
   submachine.

部分機械 StateMachine はその既定 (**initial**) Pseudostate を経るか、その入口点
のいずれかを経て進入されることが可能だ。

   Entering via the **initial** Pseudostate has the same meaning as for ordinary
   composite States. An entry point is equivalent to a **junction** Pseudostate
   (fork in cases where the composite State is orthogonal):

入口点を経由して進入することは、複合状態の ``entry`` Behavior が実行され、その後
に入口点から目標 Vertex への Transition が実行されることを意味する。

   Any ``guards`` associated with these entry point Transitions must evaluate to
   true in order for the specification to be well formed.

同様に、部分機械 StateMachine は次の結果として退出可能だ：

* その FinalState に到達する
* 部分機械 State を起点とする集団 Transition の起因
* その出口点のどれかを経由する

..

   Exiting via a FinalState or by a group Transition has the same meaning as for
   ordinary composite States.

14.2.3.5 ConnectionPointReference
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

接続点参照は部分機械 State によって参照される StateMachine で定義される入口点・
出口点の（部分機械 State の一部としての）使用法を表す。部分機械 State の接続点参
照は Transitions の出処・目標として使用可能だ。これらは部分機械 State が参照する
部分機械 StateMachine への出入りを表す。

   Connection point references are sources/targets of Transitions implying exits
   out of/entries into the submachine StateMachine referenced by a submachine
   State.

Transition の対象としての入口点接続点参照は Transition の ``target`` が部分機
械 State の部分機械で定義された **entryPoint** Pseudostate であることを含意す
る。

   As a result, the Regions of the submachine StateMachine are entered through
   the corresponding **entryPoint** Pseudostates.

Transition の出処としての出口点接続点参照は Transition の ``source`` が部分機械
State の部分機械で定義された出口点 Pseudostate であることを含意する。

   When a Region of the submachine StateMachine reaches the corresponding exit
   point, the submachine state is exited via this exit point.

14.2.3.6 FinalState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   FinalState is a special kind of State signifying that the enclosing Region
   has completed.

したがって、FinalState への Transition はこの FinalStateを含む Region の挙動の完
了を表す。

14.2.3.7 Pseudostate and PseudostateKind
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A Pseudostate is an abstraction that encompasses different types of transient
   Vertices in the StateMachine graph. Pseudostates are generally used to chain
   multiple Transitions into more complex *compound transitions* (see below).

例えば **fork** Pseudostate に進入する Transition と、それから退出する
Transitionsの集合を組み合わせることで、直交 Regions の集合に進入することが可能で
ある混合 Transition を得る。

Pseudostate の具体的意味は Pseudostate の型に依存し、それは型 PseudostateKind の
``kind`` 属性により定義される。次に種類とその意味について記す：

initial
  Region の開始点。

  * Region が既定作動により進入されたときにその中にある Behavior の実行が開始す
    る点。
  * 高々一つの Transition に対する ``source`` であり、関連する ``effect`` を有す
    ることはあるが、``trigger`` や``guard`` はない。
  * Region には高々一つの **initial** Vertex がある。

deepHistory
  所有 Region の直近の作動状態構成を表現する変数の一種。

  * ここで停止する Transition はその Region をこの Pseudostate と同じ状態構成に
    復元することを意味する。
  * 復元された状態構成にある States すべての ``entry`` Behavior は、より外側の
    State から適切な順序で実行される。
  * 複合 State に対してしか定義不可能であり、その Region 一つに含めることが可能
    である Pseudostate は高々一つだ。

shallowHistory
  その包含 Region の最新作動部分状態を表現する変数の一種。ただしその部分状態の部
  分状態ではない。

  * ここで停止する Transition は、State に進入する意味の全てで Region をその部分
    状態に復元することになる。
  * ここからの単一の出発 Transition は複合 State の部分状態で終了するように定義
    されることがある。

       This substate is the *default shallow history* state of the composite
       State.

  * 複合 State に対してしか定義不可能であり、その Region 一つが含むことが可能な
    のは高々一つだ。
join
  異なる直交 Regions 内の Vertices から始まる二つ以上の Transitions の共通の
  ``target`` Vertex として機能する。

  * ここで停止する Transition は ``guard`` や ``trigger`` を有することが不可能だ。
  * 同期機能がある。進入 Transitions すべてが完了しないと、退出 Transition で実
    行を続行することが不可能だ。
fork
  進入 Transitions を複合 State の直交 Regions の Vertices 上で停止する二つ以上
  の Transitions に分岐する役割がある。

  ここから退出する Transitions は ``guard`` や ``trigger`` を有することが不可能
  だ。
junction
  複数の Transitions を接続して States 間の混合経路をなすのに用いる。

     For example, a **junction** Pseudostate can be used to merge multiple
     incoming Transitions into a single outgoing Transition representing a
     shared continuation path. Or, it can be used to split an incoming
     Transition into multiple outgoing Transition segments with different
     ``guard`` Constraints.

  このような ``guard`` Constraints はこの Pseudostate を含む混合遷移が実行される
  前に評価され、静的条件分岐と呼ばれる。

     It may happen that, for a particular compound transition, the configuration
     of Transition paths and ``guard`` values is such that the compound
     transition is prevented from reaching a valid state configuration.

  このような場合、混合遷移全体が、その Triggers が有効であっても無効になる。

  複数の ``guards`` が真と評価される場合、そのうちの一つが選択される（どう選択さ
  れるかは定義されない）。
choice
  上記 **junction** に似ているが、混合 Transitions 走査がここに到達したときに、
  出発 Transitions のすべてに対する ``guard`` Constraints が動的に評価されるとい
  う違いがある。

     Consequently, **choice** is used to realize a dynamic conditional branch.
     It allows splitting of compound transitions into multiple alternative paths
     such that the decision on which path to take may depend on the results of
     Behavior executions performed in the same compound transition prior to
     reaching the choice point.

  * 複数の ``guards`` が真と評価される場合、そのうちの一つが選択される。
  * どの ``guard`` も真と評価されない場合、そのモデルはまともでないとみなされ
    る。すべての **choice** Pseudostate に対して else ``guard`` を定義しておくと
    避けられる。
entryPoint
  StateMachine または複合 State に対する入口。

  * これらの内部のカプセル化をもたらす。
  * これを所有する StateMachine または複合 State の Region では、ここからその
    Region 内の Vertex への単一 Transition は高々一つだ。

  所有 State に関連する ``entry`` Behavior がある場合、この Behavior は出発
  Transition に関連する Behavior のどれよりも先に実行される。Regions が複数関与
  する場合、この入口点は **fork** Pseudostate として動作する。
exitPoint
  StateMachine または複合 State に対する出口。

  * これらの内部のカプセル化をもたらす。
  * 複合 State または部分機械 State が参照する StateMachine のいずれかの Region
    内の出口点で停止する Transitions は、その状態の停止を意味する。関連する
    ``exit`` Behavior の実行を伴う。
  * State 内の直交 Region からの Transitions 複数がここで停止する場合、この
    Pseudostate は **join** であるかのように動作する。
terminate
  ここに進入することは StateMachine の実行が直ちに停止する。

  * StateMachine は States のいずれも退出せず、``exit`` Behaviors のいずれも実行
    しない。
  * 実行中の ``doActivity`` は自動的に abort される。
  * ここに進入することは DestroyObjectAction を呼び出すことと等価だ。

14.2.3.8 Transitions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Transition 定義：

   A Transition is a single directed arc originating from a ``single`` source
   Vertex and terminating on a single ``target`` Vertex (the ``source`` and
   ``target`` may be the same Vertex), which specifies a valid fragment of a
   StateMachine Behavior. It may have an associated ``effect`` Behavior, which
   is executed when the Transition is traversed (executed).

Transition 走査の期間は未定義だが、ゼロと非ゼロ時間の両方を含む異なる意味上の解
釈を認める。

Transition はより複雑な混合遷移 (compound transition) の一部として実行され、
StateMachine の実行をある安定状態構成から別のものへと移行させる。混合遷移の意味
を以下に述べる。

実行の途中では、Transition オブジェクトは次のどれかであると言う：

到達した (reached)
  その StateMachine の実行がその ``source`` Vertex に到達した（つまりその
  ``source`` State が作動中態構成にある）ときに。
走査した (traversed)
  それが（関連する ``effect`` Behavior と一緒に）目下実行されているときに。
完了した (completed)
  それが ``target`` Vertex に到達した後に。

Transition は Triggers の集合を所有することがあり、それぞれはそれの発生が発送さ
れたときに Transition の走査を引き起こすことがある Event を指定する。

   A Transition ``trigger`` is said to be *enabled* if the dispatched Event
   occurrence matches its Event type.

Transition に Triggers が複数定義されている場合、それらは論理和のようなものだ：

   that is, if *any* of them are enabled, the Transition will be triggered.

14.2.3.8.1 Transition kinds relative to source
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Transition の意味はその ``source`` Vertex との関係に依存して決まる。Transition
の属性 ``kind`` の値によって異なる可能性三つが定義される：

external
  Transition はその ``source`` から退出する、の意。

     If the Vertex is a State, then executing this Transition will result in the
     execution of any associated exit Behavior of that State.
local
  **external** の反対であり、Transition はそれを含む State から退出しない、の
  意。

  * したがって包含 State の ``exit`` は実行されない。
  * ただし **local** Transitions では ``target`` は ``source`` と異なる必要があ
    る。
  * この種の Transition は複合 State 内にしか存在不能だ。
internal
  **local** Transition の特別な場合であり、自己遷移をする。

  * ``source`` と ``target`` が同じ。
  * State に退出されない。再入不能。
  * ``source`` が State の場合に限り定義される。

14.2.3.8.2 High-level (group) Transitions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   Transitions whose ``source`` Vertex is a composite States are called
   :dfn:`high-level` or :dfn:`group` Transitions.

高水準 Transitions が **external** である場合、複合 State の部分状態すべての退出
をもたらし、定義された ``exit`` Behavior を作動中状態構成の最も内側の States か
ら実行する。

高水準 Transitions が **local** である場合、``source`` の ``exit`` と
``target`` の ``entry`` が実行され、包含 State のそれらは実行されない。

14.2.3.8.3 Completion Transitions and completion events
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

特別な Transition として暗黙の駆動装置がある完了 Transition がある。

   The event that enables this trigger is called a :dfn:`completion event` and
   it signifies that all Behaviors associated with the ``source`` State of the
   completion Transition have completed execution.

単純 State の場合、関連する ``entry`` と ``doActivity`` の実行が完了すると、完了
イベントが生成される。これらの Behaviors が定義されていない場合、完了イベントは
この State に進入する時点で生じる。

複合 State または 部分機械 State の場合、完了イベントは以下の状況で生じる：

* 内部の活動 (e.g. ``entry`` and ``doActivity``) のすべてが実行を完了して、かつ
* State が複合 State であれば、その直交 Regions のすべてが FinalState に到達し
  たか、
* State が部分機械 State であれば、その ``submachine`` の実行が FinalState に到
  達した。

完了イベントは発送優先権がある。つまり、イベントプールにある保留中 Event の発生
よりも早くに発送される。

* 複数の直交 Regions に対応する二つ以上の完了イベントが同時に発生した場合、その
  ような完了の発生が処理される順序は定義されない。
* StateMachine の高水準 Regions すべての完了は StateMachine の Behavior の完了に
  対応し、停止に至る。

Transition guards:

   A Transition may have an associated ``guard`` Constraint.

* 偽に評価される ``guard`` を有する Transitions は無効だ。
* 守衛はそれらを含む混合 Transition が有効になる前に評価される。ただし、それが
  **choice** Pseudostate から始まる Transition 上にある場合を除く。
* 関連する ``guard`` を有しない Transition は、真である ``guard`` を有するものと
  して扱われる。

..

   NOTE. A completion Transition may also have a ``guard``.

テスト：

   A ``guard`` constraint may involve tests of orthogonal States of the current
   StateMachine, or explicitly designated States of some reachable object (for
   example, “in State1” or “not in State2”).

State 名はそれらを含む入れ子 States および Regions によって完全修飾され、
``RegionA::State1::Region1::State2::State3`` という形のパス名をひねり出すことが
許される。これは、同じ State 名が異なる複合 State Regions で出現する場合に使用さ
れる。

14.2.3.8.4 Compound transitions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

イベント発生が有効な Transition を引き起こすか、StateMachine 実行が作成される
と、安定状態構成に到達するまで、接続されて入れ子になった Transitions と Vertices
の集合の走査が開始される。一般的な場合では、混合遷移と呼ばれるこの走査の追跡は、
非循環有向グラフで表すことが可能だ。このグラフの根（源）は、以下のいずれかだ：

* Triggers が一つ以上定義された Transition
* 完了 Transition
* 共通の **join** Pseudostate に収束する、相異なる直交 Regions を起点とする
  Transitions の集合
* 最上位 Region つまり StateMachine が所有する Region の **initial** Pseudostate
  を起点とする Transition

..

   Branching in a compound transition execution occurs whenever an executing
   Transition performs a default entry into a State with multiple orthogonal
   Regions, with a separate branch created for each Region, or when a **fork**
   Pseudostate is encountered.

混合遷移の実行結果得られる全体的な挙動は、走査された要素に関連する Behaviors の
実行の半順序集合であり、その要素 (Vertices and Transitions) が遭遇した順番によっ
て決まる。

例えば、複合 State に進入する Transition がその State の部分状態で停止する場合、
この Transition の ``effect`` は複合 State の ``entry`` の実行前に実行され、その
後に部分状態の ``entry`` が実行される。走査中に **fork** Pseudostate に遭遇した
場合、少なくとも概念的には、個々の出発枝の ``effect`` は互いに同時に実行される。

   If a **choice** or **join** point is reached with multiple outgoing
   Transitions with ``guards``, a Transition whose ``guard`` evaluates to true
   will be taken. If more than one ``guard`` evaluates to true, one of these
   Transitions is chosen for continuing the traversal.

* この選択に対するアルゴリズムは未定義。
* **choice** Pseudostate を起点とする Transitions の場合、この Pseudostate に到
  達したときに真と評価される ``guards`` がない場合、まともでないモデルが形成され
  る。

14.2.3.8.5 Transition ownership
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Transition が含まれている Region のほうは直接間接を問わず StateMachine が所有す
る必要があるが、Transition の所有者は明示的に制限されていない。

Transition の所有者として推奨されるのは、その ``source`` と ``target`` の両方を
含む Region であって最も内側のものだ。

14.2.3.9 Event Processing for StateMachines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

14.2.3.9.1 The run-to-completion paradigm
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

StateMachine 実行による Event 発生の処理手順は、:doc:`./ch13-common-behavior` で
定義した一般的な意味に従う。

* StateMachineの、StateMachine は生成時に初期化を実行し、その間に生成によって促
  された初期混合遷移を実行し、その後、待機点に入る。
* StateMachine Behaviors の場合、待機点は安定状態構成で表される。
* イベントプールに格納されている Event が発送されるまでこの状態が維持される。
* この Event が評価され、StateMachine の有効な Trigger と合致し、その Event 発生
  によって引き起こすことが可能である有効な Transition が少なくとも一つあれば、単
  一の StateMachine step が実行される。
* ステップでは混合遷移を実行し、安定状態構成（すなわち次の待機点）で停止する。

この循環は StateMachine が Behavior を完了するか、外部の取次者が非同期で停止する
まで反復する。

   StateMachines can respond to any of the Event types described in Clause 13
   *as well as to completion events*

※先述したが、完了イベントに優先権があり、イベントプール内の保留 Event 発生よりも
早く発送される。

   Event occurrences are detected, dispatched, and processed by the StateMachine
   execution, *one at a time*.

※イベントの発送順序は、様々なスケジューリングアルゴリズムに対応できるように、未
定義のままにしてある。

   This cycle is referred to as the :dfn:`run-to-completion paradigm`, and the
   corresponding StateMachine step is called a :dfn:`run-to-completion step`.

Run-to-Completion とは、例外や、context Classifier オブジェクトや StateMachine実
行の非同期破棄がない場合、保留中の Event 発生が発送されるのは、直前の発生の処理
が完了し、安定状態構成に到達した後であるということだ。

   When an Event occurrence is detected and dispatched, it may result in one or
   more Transitions being *enabled* for firing.

Transition が有効にならず、対応する Event 型が作動中状態構成の
``deferrableTriggers`` 一覧のいずれにもない場合、発送された Event 発生は破棄さ
れ、この run-to-completion step は完了する。

   Due to the presence of orthogonal Regions, it is possible that multiple
   Transitions (in different Regions) can be triggered by the same Event
   occurrence.

* これらの Transitions が実行される順番は未定義のままとする。
* 動作中状態構成の各直交 Region で、入れ子になった直交 Region を含まないもの（最
  下層）は、現在の Event 発生の結果として、高々一つの Transition を引き起こすこ
  とが可能だ。
* 直交 Regions すべてがこの Transition を実行し終わると、現在の Event 発生は完全
  に消費され、run-to-completion step は完了する。

Region にある複数の互いに排他的な Transitions が同じ Event 発生によって有効にな
ることがある。そのような場合、ただ一つが選択されて実行される。その選択アルゴリズ
ムについては後述。

Transition 中には複数の行動 Behaviors が実行されることがある。

   If such a Behavior includes a synchronous invocation call on another object
   executing a StateMachine, then the Transition step is not completed until the
   invoked object method completes its run-to-completion step.

Run-to-completion をさまざまな手段で実装してよい。

   For active Classes, it may be realized by an event-loop running in its own
   thread, and that reads event occurrences from a pool. For passive Classes it
   may be implemented using a monitor.

14.2.3.9.2 Enabled Transitions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Transition が有効であるのは、次の場合、かつその場合に限る：

* その ``source`` States のすべてが作動中状態構成にある。
* Transition の ``triggers`` の少なくとも一つは、送配された Event 発生の Event
  型により合致する Event がある。

     In case of Signal Events, any occurrence of the same or compatible type as
     specified in the Trigger will match. If one of the Triggers is for an
     AnyReceiveEvent, then either a Signal or CallEvent satisfies this Trigger,
     provided that there is no other Signal or CallEvent Trigger for the same
     Transition or any other Transition having the same source Vertex as the
     Transition with the AnyReceiveEvent trigger (see also 13.3.1).

* 起源状態構成から目標状態構成または ``guards`` 条件すべてが真である動的
  **choice** Pseudostate への少なくとも一つの完全経路が存在する場合。

     (Transitions without ``guards`` are treated as if their ``guards`` are
     always true).

同じ Event 発生によって複数の Transition が有効になる可能性があるため、有効にな
ることは Transition を引き起こすのに必要ではあるが十分ではない。

14.2.3.9.3 Conflicting Transitions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   It is possible for more than one Transition to be enabled within a
   StateMachine. If that happens, then such Transitions may be *in conflict*
   with each other.

例えば、同じ State を起点とする Transitions 二つが、同じイベントによって引き起こ
され、異なる ``guards`` を持つ場合を考える。このイベントが発生し、双方の
``guard`` 条件が真である場合、ある run-to-completion step で起こる Transition は
高々一つだ。

   Two Transitions are said to conflict if they both exit the same State, or,
   more precisely, that the intersection of the set of States they exit is
   non-empty.

互いに直交する Regions で発生する Transitions のみが同時に引き起こされてよい。

この制約により、Transitions の集合を実行した結果得られる新しい作動中状態構成がう
まく形成されることが保証される。

14.2.3.9.4 Firing priorities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   In situations where there are conflicting Transitions, the selection of which
   Transitions will fire is based in part on an implicit priority.

競合 Transitions の優先順位は、状態階層における相対的な位置に基づく。定義によれ
ば、部分状態を起点とする Transition は、この部分状態の包含 States を起点とする競
合 Transitions よりも優先度が高い。

Transition の優先順位はその ``source`` State に基いて定義される。

混合遷移内で連鎖する Transitions の優先順位は、最も深く入れ子になった ``source``
State を持つ Transition の優先順位に基づく。

   In general, if t1 is a Transition whose source State is s1, and t2 has source
   s2, then:

   * If s1 is a direct or indirectly nested substate of s2, then t1 has higher
     priority than t2.
   * If s1 and s2 are not in the same state configuration, then there is no
     priority difference between t1 and t2.

14.2.3.9.5 Transition selection algorithm
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

射出する Transitions の集合は、現在の状態構成の Regions にある Transitions で
あって次の諸条件を満たすものだ：

* 集合にある Transitions すべてが有効だ。
* 集合に衝突 Transitions がない。
* 集合外の Transition で、集合内の Transition より優先度の高いものはない。

これは強欲な選択計算法により実装することが可能で、作動中状態構成を走査するという
ものだ。

   States in the active state configuration are traversed starting with the
   innermost nested simple States and working outwards. For each State at a
   given level, all originating Transitions are evaluated to determine if they
   are enabled. This traversal guarantees that the priority principle is not
   violated.

唯一の非自明な問題は、全水準で直交 States 間の Transition 競合を解消することだ。
これは、各直交 State において、そのコンポーネントのいずれかの中の Transition が
射出したら探索を停止することでなされる。

14.2.3.9.6 Transition execution sequence
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**internal** および **local** Transitions を除くどの Transition も ``source``
State から退出し ``target`` State へ進入する。これら二つの States は、複合でもか
まわず、Transition の主始点と主終点としてそれぞれ指定される。

   The :dfn:`main source` is a direct substate of the Region that contains the
   ``source`` States, and the :dfn:`main target` is the substate of the Region
   that contains the ``target`` States.

ある Region から別の Region への Transition は、同じ直後の複合 State では許され
ない。

Transition が有効になり、射出するために選択されると、次の段階が順に行われる：

#. 主始点 State から開始して、その主始点 State を含む States が先に述べた
   State 退出規則に則って退出される。
#. 一連の State 退出は、主始点と主終点の両方を直接または間接的に含む最初の
   Region に到達するまで続行する。

      The Region that contains both the main source and main target states is
      called their :dfn:`least common ancestor`.

   その時点で ``source`` States の部分構成と ``target`` States の部分構成を接続
   する Transition の ``effect`` Behavior が実行される（ここでの部分構成とは、
   least common ancestor の先祖 Region に含まれる完全状態構成の部分集合を指
   す）。

#. 主終点 State を含む States の構成は、主終点 State を含む least common
   ancestor Region の最も外側の State から進入される。Behaviors の実行は State
   進入または複合 State 進入の規則に従う。

この遷移実行法は Figure 14.2 の StateMachine 見本が図解する。

   Figure 14.2 Compound transition example

この場合、StateMachine が State ``S11`` にある間、イベント ``sig`` が発送され
て、次の一連の動作が実行される：

    .. code:: text

       xS11; t1; xS1; t2; eT1; eT11; t3; eT111

入れ子になっている States と Transitions の遷移順序が外側からなのか内側からなの
かが始点に近いか終点に近いかで決まるということが要点のようだ。

14.2.4 Notation
----------------------------------------------------------------------

14.2.4.1 StateMachine Diagrams
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

StateMachine をどのように図式化するかを規定する節だ。

   A StateMachine diagram is a graph that represents a StateMachine. States and
   various other types of Vertices in the StateMachine graph are rendered by
   appropriate State and Pseudostate symbols, while Transitions are generally
   rendered by directed arcs that connect them, or by control symbols
   representing the actions of the Behavior on the Transition.

StateMachine 図は States/Vertices/Pseudostates と Transitions をそれぞれ頂点、辺
とする有向グラフの一種であると考えられる。

14.2.4.2 StateMachine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

StateMachine 再定義をクラス図で描写する場合、Classifier に対する既定矩形記法を用
いることができ、キーワード ``«statemachine»`` が StateMachine の名前の上または前
にある名前区画の中に収める。

StateMachine とその ``context`` Classifier または BehavioralFeatures の間の関連
には特別な図表的表現がない。

14.2.4.3 Region
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Regions を有する複合 State や StateMachine を図示するには、それらのグラフ Region
を破線を引いて tiling して Regions に分割する (Fig. 14.3)。

* 各 Region は任意の名前を持つことが許され、入れ子になった非交和 State とその間
  の Transitions を含む。
* State 全体のテキスト区画は実線により直交 Regions から区切られる。

..

   Figure 14.3 Notation for a composite State with Regions

Regions が二つある複合 State を示す。

14.2.4.4 State
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: 読者ノート

   UML 2.5 と 2.5.1 の仕様書で、この辺りの文書構造に変化があるようだが、
   旧版ではおそらく余分な節が挿入されていて、節番号にズレが生じていた。

まずは State の記法を二種。

   State is shown as a rectangle with rounded corners, with the State name shown
   within (Figure 14.4).

   Optionally, it may have an attached name tab (Figure 14.5).

後者の記法は通常、直交 Regions を有する複合 State の名称を保持するために用いられ
るが、他の場合に用いてもかまわない。

   A State may be subdivided into multiple compartments separated from each
   other by a horizontal line (Figure 14.6).

この図式を観察すると、区画内が Class 記法と若干異なることに気づく。

名前区画
  この区画では State の名前（オプション）を文字列として保持する。

  部分機械 State の場合は、参照される StateMachine の名前を State の名前の後にコ
  ロン ``:`` が続く文字列として示す。
内部 Behaviors 区画
  この区画では State に付随する内部 Behaviors のリストを保持する。リストの各項目
  は次の書式だ：

  .. code:: bnf

     <behavior-type-label> [‘/’ <behavior-expression>]

  ``<behavior-type-label>`` は ``<behavior-expression>`` で指定された Behavior
  が呼び出される状況を分類するもので、次のいずれかだ：

  entry
    対応する式で指定される、当 State への進入時に実行される Behavior ``entry``
    を識別する。
  exit
    対応する式で指定される、当 State からの退出時に実行される Behavior ``exit``
    を識別する。
  do
    モデル化された要素が当 State にある限り、または式で指定される計算が完了する
    までに実行される進行中 Behavior ``doActivity`` を識別する。

  オプションの ``<behavior-expression>`` は、何らかのテキスト表層言語による表現
  であり、製造者固有の言語でも標準的な言語でもよい (16.1)。
内部 Transitions 区画
  この区画では **internal** Transitions のリストを含む。各項目は次の構文で表す：

  .. code:: bnf

     {<trigger>}* [‘[’ <guard>‘]’] [/<behavior-expression>]

  * ``<triger>`` は Triggers に対する記法 (13.3.4)
  * ``<guard>`` は真偽式
  * ``<behavior-expression>`` はオプションであり、Event 発生が **internal**
    Transition の ``trigger`` と ``guard`` に合致する場合に実行される ``effect``
    Behavior の仕様（上の記述も参照のこと）。

分解区画
  複合 State のみこの区画を使える。次の節参照。

テキストによる挙動式の代わりに、State または **internal** Transition に付随する
さまざまな Behaviors を別の図式 (e.g. Activity) で表すことができる。

14.2.4.4.1 Composite State
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   This compartment shows its composition structure in terms of Regions, States,
   and Transition. In addition to the (optional) name and internal Transition
   compartments, the State may have an additional compartment that contains a
   nested diagram.

複合 State の分解を非表示にすることが便利な場合がある。

   For example, there may be a large number of States nested inside a composite
   State and they may simply not fit in the graphical space available for the
   diagram. In that case, the composite State may be represented by a simple
   State graphic with a special “composite” icon, usually in the lower
   right-hand corner (see Figure 14.8).

このアイコンは水平に配置され接続された二つの States から構成され、当該図式では示
されていない分解を持つことを示す、オプションの視覚的な手がかりとなる。その代わり
に、複合 States の内容が別の図式に表示される。

   NOTE. The “hiding” here is purely a matter of graphical convenience and has
   no semantic significance in terms of access restrictions.

複合 State には、その外側の境界に、またはその境界に近接して（内側または外側
に）複数の出入口地点を持つことができる。

   Figure 14.7 Composite State with two States

``Dialing`` は ``Start`` と ``Partial`` ``Dial`` の二つの States を含む複合
State だ（最初の黒丸と最後の二重丸は今は無視）。

   Figure 14.8 Composite State with a hidden decomposition indicator icon

複合 State の分解を非表示にすることは便利だ。メガネのような記号を State 内の
右下に記すことでそのことを示す。

   Figure 14.9 Composite State with Regions

状態 ``Studying`` は三個の Regions からなる。

   Figure 14.10 Composite State with two Regions and entry, exit, and do Behaviors

* ``entry``: この状態 (``LightOn``) に進入する際に履行される Behavior
  (``entry``) だ。
* ``do``: この状態にある間中履行される Behavior (``doActivity``) だ。
* ``exit``: この状態から退出する際に履行される Behavior (``exit``) だ。
* 文書中に記述がないのでこれは憶測になるが、左の Region がメインの照明、右の
  Region がサブの照明を示している。

14.2.4.4.2 Submachine State
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

部分機械 State は通常の State として描かれる。名前区画の文字列は次の構文だ：

.. code:: bnf

   <state-name> ‘:’ <name-of-referenced-StateMachine>

..

   The submachine State symbol may contain the references to one or more
   ``entry`` points and to one or more ``exit`` points.

* これらの接続点参照の表記は部分機械 State の境界上の ``entry``/``exit``
  Pseudostate から構成される。
* 名前は参照される StateMachine 内で定義される対応する入口・出口点の名前だ。
  ConnectionPointReference 参照。

..

   If the submachine StateMachine is entered through its default **initial**
   Pseudostate or if it is exited as a result of the completion of the
   submachine, it is not necessary to use the entry/exit point notation.

同様に、部分機械 State の境界からの明示的なグループ Transition によって退出する
場合は、出口点は必要ない。

   Submachine States invoking the same submachine may occur multiple times in
   the same state diagram with the entry and exit points being part of different
   Transitions.

..

   Figure 14.11 Submachine State example

部分機械 State が参照される StateMachine 図の断片だ。実際の部分機械 StateMachine
は、何らかの名前空間で定義される。

Event ``error1`` が引き起こした Transition は ``FailureSumbachine`` の入口点
``sub1`` にて停止する。Transition ``error3`` は ``FailureSumbachine`` の既定
Transition を取ることを示す。

部分機械の出口点 ``subEnd`` から始まる Transition は ``HandleFailure`` で実行さ
れるものに加えて、Behavior ``fixed1`` を実行する。この Transition は当部分機械内
で引き起こされなければならない。

当部分機械 State が FinalState に到達したときに生成される完了イベントの結果とし
て、右辺から出ていく Transition が取られる。

   NOTE. The same notation would apply to composite States with the exception
   that there would be no reference to a StateMachine in the State name.

..

   Figure 14.12 StateMachine with an exit point as part of the StateMachine
   graph

二つの出口点が定義された StateMachine の見本。入口点と出口点は状態枠上もしくは状
態グラフ内に表示されることがある。この図式はグラフ内に出口点を示した。

   Figure 14.13 StateMachine with an exit point on the border

これは先の図式と同じモデルだが、同じ出口点を状態枠上に示したものだ。

   Figure 14.14 Submachine Sate that uses an exit point

Figure 14.12 や 14.13 で示した StateMachine が部分機械 State で参照されてお
り、State 記号上に出口点のある表現オプションを示す。

複合 States に対する入口点・出口点の記法例は Fig. 14.23 にある。

14.2.4.4.3 State list notation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   State lists provide a graphical shortcut for certain situations that
   sometimes occur in practice.

異なる States を起点とする、同じ Trigger 値を有する ``effect`` フリーの
Transitions 複数だが、すべてが

* 単一の出発 Transition のある共通 **junction** Vertex を目標 State とするか、
* 同じ目標 State で停止するか

であるものは、State 風図表的要素を起点とする単一 Transition のような辺で表しても
よい。辺には起点となる State の名前一覧ラベルが付く。この辺は joint target State
で停止する。

   Figure 14.15 State list notation option

どちらの可能性もある。

   Figure 14.16 Diagram equivalent to Figure 14.15 without using statelists

状態リストを用いない場合の同値の図式。黒丸が joint target State に相当する。

14.2.4.5 FinalState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

FinalState は小さい黒丸を囲む丸で示す。

   Figure 14.17 FinalState notation

FinalState の見本だ。複合 State 内部の States の最も右のもの。

14.2.4.6 Pseudostate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Figure 14.18 initial Pseudostate

**initial** Pseudostate は小さい黒丸。

ClassifierBehavior StateMachine の Region では **initial** Pseudostate からの
Transition は、そのオブジェクトを生成する発生の Event 型でラベル付けられていても
よい。そうでない場合、ラベル付けされていなければならない。ラベル付けられていない
場合、囲んでいる State からの任意の Transition を表す。

   Figure 14.19 shallowHistory Pseudostate

**shallowHistory** Pseudostate は ``H`` を囲む小さい丸で見せる。その Region を直
接囲む State Region に適用する。

   Figure 14.20 deepHistory Pseudostate

**deepHistory** Pseudostate は ``H*`` を囲む小さい丸で見せる。その Region を直
接囲む State Region に適用する。

   Figure 14.21 entryPoint Pseudostate

入口点は StateMachine 図または複合 State の枠上に小さい丸として、関連する名前と
ともに見せる。

   Optionally it may be placed both within the StateMachine diagram and outside
   the border of the StateMachine diagram or composite State.

..

   Figure 14.22 exitPoint Pseudostate

出口点は StateMachine 図または複合 State の枠上にバツの付いた小さい丸として、関
連する名前とともに見せる。

配置位置の選択については入口点と同様。

   Figure 14.23 entryPoint and exitPoints on a composite State

複合 States の入口点と出口点を描く場合の表記法を図解する。

   Alternatively, the “bracket” notation shown in Figure 14.30 and Figure 14.31
   can also be used for the transition-oriented notation.

..

   Figure 14.24 junction Pseudostate with incoming and outgoing Transitions

**junction** は黒丸で見せる。

   Figure 14.25 choice Pseudostates

**choice** Pseudostate は菱形の記号で見せる。NOTE にあるように、場合によっては菱
形内部の条件を略記し、Transitions ラベルに移行することが許される。

   Figure 14.26 terminate Pseudostate

**terminate** Pseudostate はバツで見せる。

   Figure 14.27 fork and join Pseudostates

**fork** と **join** を表す表記法は太い棒だ。

   The bar may have one or more arrows from source States to the bar (when
   representing a join). The bar may have one or more arrows from the bar to
   States (when representing a fork).

Transition 文字列を棒の近くに示してもよい。

14.2.4.7 ConnectionPointReference
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A connection point reference to an entry point has the same notation as an
   entry Pseudostate. The circle is placed on the border of the State symbol of
   a submachine State.

..

   Figure 14.28 Entry point ConnectionPointReference notation

入口点に対する接続点参照は ``entry`` Pseudostate と同じ表記法だ。

   Figure 14.29 Exit point ConnectionPointReference notation

出口点に対する接続点参照は ``exit`` Pseudostate と同じ表記法だ。

   Figure 14.30 Alternative entry point ConnectionPointReference notation

代わりに、入口点に対する接続点参照は「括弧付きの空白」記号を使って見せることもで
きる。記号内のテキストは ``( via <name> )`` とする。ここで ``<name>`` は接続点の名
前とする。

   This notation may only be used if the Transition ending with the connection
   point is defined using the graphical Transition notation, such as the one
   shown in Figure 14.32.

Fig. 14.30 のことだと思われる。

   Figure 14.31 Alternative exit point ConnectionPointReference notation

出口点に対する接続点参照の記法についても、入口点に対するそれの類比で定義される。

14.2.4.8 Transition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Transition を表すテキスト表記法は既定では：

.. code:: bnf

   [<trigger> [‘,’ <trigger>]* [‘[’ <guard>‘]’] [‘/’ <behavior-expression>]]

* ``<trigger>`` は Triggers を表す標準表記法 (13.3.4) だ。
* ``<guard>`` は ``guard`` を表す Boolean 式だ。
* ``<behavior-expression>`` はオプションで、``effect`` Behavior を指定する式だ。
  前に述べられているのと同じ。

代替として、``effect`` Behavior を制御フローに基づく Actions の配列として記述で
きる場合、Transitions と混合遷移には Activities に対して使われる表記法と類似する
を表す図式的表現がある。

   NOTE. Although this alternative notation contains graphical elements
   reminiscent of the notation used for Activities, it is a distinct form
   applicable only to StateMachines, and its elements map to appropriate
   StateMachine concepts.

この表記法は有向グラフの形をしていて、制御フローを表す有向辺で相互接続された
一つ以上の図表記号からなる (Fig. 14.32)。

**initial** Pseudostate を起点とする Transition 以外の場合、標準的な単純 State
記法の形式である開始記号はこの Transition の ``source`` State を表現する。この
Transition が Signal に基づく Trigger を持つ場合、この ``source`` State 記号は
特別な Signal 受信記号を表す辺で接続される。
この Transition に複数 Triggers がある場合、すべて同じ記号に一覧される。

**initial** Pseudostate を起点とする Transition の場合、開始記号は初期記号であ
り、それは **initial** Pseudostate を表すのに使うものと同じだ。つまり黒塗りの
丸だ。この場合、開始記号の直後に Signal 受信記号はない。

経路を停止する終了記号を除いて、次の記号のどれでも、適宜連鎖の中に出現可能だ：

* 動作記号
* 選択点記号
* Signal 送信記号
* 融合記号

これらの有向グラフにある停止記号はいつでも、遷移の ``target`` State を表す State
風記号か最終状態 (FinalState) 記号だ。

14.2.4.8.1 Action symbols
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   Each action symbol is represented by a rectangle with an optional textual
   specification of the action.

これは OpaqueAction または順次実行される一つ以上の Actions を含む SequenceNode
に写像される（このような Actions は混合遷移の適当な Transition の ``effect``
Behavior を指定する Activity の部分だ）。

14.2.4.8.2 Signal receipt symbol
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   The Signal receipt symbol is shown as a five-pointed polygon that looks like
   a rectangle with a triangular notch in one of its sides (either one).

Transition の ``trigger`` に写像され、``effect`` Behavior を指定する Activity に
は写像されない。この Trigger の Signals の名前と ``guards`` は次の書式で記号内に
記述する：

.. code:: bnf

   <trigger> [‘,’ <trigger>]* [‘[’ <guard> ‘]’]

``<trigger>`` は 13.3.4 節に記述されているように指定され、Signal と ``change``
Event 型のみが許可されるという制約がある。駆動装置記号は常に記号の経路の最初にあ
り、混合遷移は高々一つの記号しか持つことが不可能だ。

14.2.4.8.3 Signal send symbol
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   This represents the special action of sending a signal and maps directly to a
   SendSignalAction that is part of the Activity that describes the ``effect``
   Behavior of the corresponding Transition.

Signal 送信記号の記法は SendSignalAction (16.3.4) の記法に対応する。

14.2.4.8.4 Choice point symbol
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   This symbol maps directly to a **choice** Pseudostate and uses the same
   notation.

これはどの Activity の部分でもない。

14.2.4.8.5 Merge symbol
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   A merge symbol is used to join multiple control-flow arcs and maps directly
   to a **junction** Pseudostate and uses the same notation. It is not part of
   any Activity.

..

   Figure 14.32 Symbols for Signal reception, Sending, and Actions on a
   Transition

この図は四つの接続された Transitions からなる混合遷移を示している。

* Idle から菱形の間

  * ``Req(id)`` が Signal 受信記号。
  * 菱形が選択点記号。

* 菱形から黒丸の間（左右それぞれ）

  * ``Minor(id)`` たちが Signal 送信記号。
  * ``MinorReq := id;`` たちがアクション記号。

* 黒丸から Busy の間

  * 黒丸は融合記号。

14.2.4.8.6 Deferred triggers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   A deferrable trigger is shown by listing it within the State followed by a
   slash and the label “defer”.

..

   Figure 14.33 Deferred Trigger notation

``Initializing`` と ``Primed`` のどちらの状態にも ``request/defer`` とある。イベ
ント ``request`` 発生の処理はどちらでも延期されるが、``Operation`` 状態に到達す
れば処理される。

14.2.4.9 TransitionKind
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* 種類が **internal** の Transitions は図式中には明示的に示されない。
* 種類が **local** の Transitions は包含複合 State の境界、またはそれの入口点の
  うちの一つ、または複合 State 内にある Vertex を起点とすることができる。

  * 代わりに、**local** Transitions は ``*`` というテキストを含む状態記号から離
    脱する Transition として示すことも可能だ。
  * この種の Transitions は複合 State の境界上またはその出口点の一つまたは複合
    State 内にある Vertex でしか停止することが不可能だ。
* 種類が **external** の Transitions は ``source`` Vertex の内部または外部の任意
  の Vertex を ``target`` にすることが可能だ。

  * ``source`` に最も近い **external** Transition の部分は、``source`` Vertex の
    境界の外側に描画されなければならない。
  * ``source`` が State または State 上の出口点である **external** 自己
    Transition の場合、State 自体または State 上の入口点を ``target`` にすること
    ができ、State 境界の完全に外側に描かれる。

..

   Figure 14.34 Local Transitions

ここにある Transitions のすべてが **local** だ。

   Figure 14.35 External Transitions

ここにある Transitions のすべてが **external** だ。

14.2.5 Examples
----------------------------------------------------------------------

   Figure 14.36 StateMachine diagram representing a telephone

簡単な電話の StateMachine の図式。

* Idle の右についている黒丸 (**initial** Pseudostate) と、大きい枠の左上外部にあ
  る白丸 (activeEntry) が入口点が見える。
* FinalState に加えて、マルバツ印の aborted なる出口点がある。

部分機械の例は Fig. 14.12 と Fig. 14.13 に見られる。

14.3 StateMachine Redefinition
======================================================================

14.3.1 Summary
----------------------------------------------------------------------

   StateMachines are used for the definition of Behavior (for example, Classes
   that are generalizable).

Class の特殊化の一環として、それの Behavior 定義を特殊化することが要求されてもよ
い。これは再定義を用いて一般 Classifier の Behavior の拡張として、特殊化された
Classifier の Behavior を定義することで達せられる。

14.3.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 14.37 StateMachine redefinition

現れているクラスはすべて前節ですでに述べられている。

ただし、Region, State, Transition の親クラスが RedefinableElement のみとなってい
ることが違う。以前見た Figure 14.1 では Namespace のみが親クラスとして示されてい
た。

``A_extendedStateMachine_stateMachine``, ``A_extendedRegion_region``
  StateMachine/Region から StateMachine/Region への関連（単方向）。これが一つの
  拡張であるような StateMachine/Region を参照。

``A_redefinedState_state``, ``A_redefinedTransition_transition``
  State/Transition から State/Transition への関連（単方向）。これがその再定義で
  あるような State/Transition を参照。

``A_redefinitionContext_region``, ``A_redefinitionContext_state``, ``A_redefinitionContext_transition``
  Region/State/Transition から Classifier への関連（単方向）。これが再定義される
  ことが許容される ``context`` Classifier を参照。

14.3.3 Semantics
----------------------------------------------------------------------

14.3.3.1 StateMachine Extension
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

StateMachine は一つ以上の他の StateMachine を再定義することが可能であり、その場
合、それは再定義された StateMachine の拡張となる。

   A ``region`` of an extension StateMachine can redefine one or more
   ``regions`` of its ``extendedStateMachines``.

拡張 StateMachine の basline 動作は、拡張 StateMachine の ``regions`` と、そ
の ``extendedStateMachine`` のすべての非再定義 ``regions`` のすべての和集合を含
んでいるかのようなものだ。

   An extension StateMachine may also add new ``connectionPoint`` Pseudostates
   or redefine ``connectionPoints`` from any of its ``extendedStateMachines``.

..

   If a StateMachine has a ``context`` BehavioredClassifier (see sub clause
   13.2.3.4), then this BehavioredClassifier is also its ``redefinitionContext``
   (see sub clause 9.2.3.3).

* これには一般的な BehavioredClassifer の ``classifierBehavior`` である
  StateMachine や、一般的な BehavioredClassifier の BehavioralFeature の
  ``method`` を指定するための StateMachine の場合も含まれる。
* ``context`` BehavioredClassifier が特殊化されると、関連するStateMachine は特殊
  化された BehavioredClassifier の ``context`` の対応する StateMachine によって
  拡張される。

14.3.3.2 Region Redefinition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A Region that is a region of an extension StateMachine can redefine a Region
   that is a region of an ``extendedStateMachine`` of that StateMachine. A
   Region that is a region of a redefining State in an extension StateMachine
   (see sub clause 14.3.3.3) can redefine a Region that is a region of the
   redefined State in an ``extendedStateMachine`` of that StateMachine.

* どちらの場合でも、再定義 Region は被再定義 Region の拡張と呼ばれる。
* 拡張 Region の baseline 動作は、次の和集合のようなものだ：

  * 拡張 Region に含まれる Vertices と Transitions
  * 拡張 Region に含まれる非再定義 Vertices と Transitions すべて

14.3.3.3 Vertex Redefinition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A Vertex defined in an extension Region can redefine a Vertex of the same
   kind in the extended Region of the extension Region.

同じ種類。

   A State can only be redefined by a State.

* 再定義する State が ``entry``, ``exit``, ``doActivity`` の全部または一部を指定
  する場合、再定義される State が同様の Behavior を指定するかどうかに関わらず、
  再定義する State に適用されるのは前者の Behavior だ。
* しかし、再定義する State が ``entry``, ``exit``, ``doActivity`` の全部または一
  部を指定しないが、``redifned`` State に適用される対応する Behavior がある場
  合、再定義する State にも ``redefined`` State の Behavior が適用される。

..

   Any ``deferrableTriggers`` applicable to the redefined State also apply to
   the redefining State, and the redefining state can also add new
   ``deferrableTriggers``.

再定義された State が部分機械 State でない場合、再定義 State は次のことが可能
だ：

* 再定義された状態の Regions を再定義する（複合 State の場合）
* 再定義された状態に Regions を追加する
* 再定義された状態の ``connectionPoint`` Pseudostate を再定義する（複合 State の
  場合）
* 再定義された状態に ``connectionPoint`` Pseudostate を追加する

部分機械 State は、その部分機械が再定義された State の部分機械の拡張である部分機
械 State によってしか再定義不可能だ。再定義 State は以下のことが可能だ：

* 再定義された State の ``connection`` ConnectionPointReferences を再定義する。
* 再定義された State に ``connection`` ConnectionPointReferences を追加する。

..

   A FinalState can only be redefined by a FinalState.

   A Pseudostate can only be redefined by a Pseudostate of the same ``kind``.

再定義された Pseudostate がある State の ``connectionPoint`` として所有されてい
る場合、再定義する Pseudostate はその再定義された Pseudostate の所有する State
の再定義の ``connectionPoint`` でなければならない。

   A ConnectionPointReference can only be redefined by a
   ConnectionPointReference whose ``state`` is a redefinition of the state of
   the redefined ConnectionPointReference.

14.3.3.4 Transition Redefinition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A Transition defined in an extension Region can redefine a Transition defined
   in the extended Region of the extension Region.

* 再定義する Transition の ``source`` Vertex は再定義される Transition の
  ``source`` Vertex の再定義でなければならない。
* 再定義する Transition の ``target`` Vertex は再定義される Transition の
  ``target`` Vertex の再定義か、追加された Vertex のどちらかであることが可能だ。
* 再定義される Transition に適用される ``triggers`` は再定義する Transition にも
  適用され、この再定義 Transition は新しい ``triggers`` を追加可能だ。
* 再定義する Transition が ``guard`` Constraint と ``effect`` Behavior の両方ま
  たはどちらか一方を指定する場合、それがこの再定義 Transition に適用される。

     However, if the redefining Transition does not specify a ``guard``
     Constraint and/or ``effect`` behavior, but there is a ``guard`` Constraint
     and/or ``effect`` Behavior that applies to the redefined Transition, then
     the ``guard`` and/or ``effect`` from the redefined Transition also applies
     to the redefining Transition.

14.3.4 Notation
----------------------------------------------------------------------

拡張 StateMachine は、その図式の名前の後にキーワード ``«extended»`` を付けて表示
する (Fig. 14.39, 14.40)。

キーワード ``«extended»`` は拡張 Region, 再定義 Vertex/Transition の名前の後ろに
追加可能であってもよい。

再定義 Vertex/Transition は破線または淡い線で描かれる (Fig 14.39)。

   Vertices and Transitions from an ``extendedStateMachine`` that are *not*
   redefined in an extension StateMachine may also be shown on a diagram of the
   extension StateMachine drawn with either dashed or light-toned lines.

Region, Vertex, Transition が ``isLeaf`` 値が真の場合、キーワード ``«final»`` を
要素名の後ろに追加してもよい。

14.3.5 Examples
----------------------------------------------------------------------

   Figure 14.38 A general StateMachine

``ATM`` StateMachine にある States ``VerifyCard``, ``OutOfService``,
``VerifyTransaction`` が ``«final»`` として指定されている。それらが ``ATM`` の特
殊化において再定義できないことを意味する。他の States はすべて再定義可能だ。

図式内下方にある Transition もまた ``«final»`` と指定されている。これも ATM の拡
張では再定義不可能だ。

   Figure 14.39 An extended StateMachine

上述の図式で示された複合 State ``ReadAmount`` を再定義し、State ``EnterAmount``
を追加した拡張 ``ATM`` の定義だ。

``ReadAmount`` からの State ``SelectedAmount`` と FinalState は、新しい
Transition の ``source`` または ``target`` として機能するように再定義される。

State ``VerifyTransaction`` は新しい State ``EnterAmount`` を ``target`` とする
新しい Transition の ``source`` として機能するように再定義される。

継承した状態は破線で描画されていることに注意。

   Figure 14.40 Adding Transitions

Fig. 14.39 の StateMachine に Transitions を追加してさらに拡張した見本。

14.4 ProtocolStateMachines
======================================================================

14.4.1 Summary
----------------------------------------------------------------------

   ProtocolStateMachines are used to express usage protocols.
   ProtocolStateMachines express the legal sequences of Event occurrences to
   which the Behaviors of an associated BehavioredClassifier must conform.

ProtocolStateMachines は Classifiers, Interfaces, Ports に関連することが可能。

14.4.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 14.41 ProtocolStateMachines

新クラスは ProtocolStateMachine, ProtocolConformance, ProtocolTransition のみ。
グラフが分離しているのが不思議。

``A_conformance_specificMachine``, ``A_generalMachine_protocolConformance``
  前者は ProtocolStateMachine から ProtocolConformance への複合関連（双方向）。
  後者は ProtocolConformance から ProtocolStateMachine への関連（単方向）。

  * 関連端 ``specificMachine``, ``generalMachine`` が ``source``, ``target`` を
    それぞれ subsets する。

``A_referred_protocolTransition``
  ProtocolTransition から Operation への関連（単方向）。

  * Figure 14.42 の ``m1`` が ``preCondition`` に相当する。
  * 関連端 ``referred`` は readOnly だ。

``A_preCondition_protocolTransition``
  ProtocolTransition から Constraint への複合関連（単方向）。

  * Figure 14.42 の ``C1`` が ``preCondition`` に相当する。

``A_postCondition_owningTransition``
  ProtocolTransition から Constraint への複合関連（単方向）。

  ``A_guard_transition`` の ``guard`` と ``transition`` をそれぞれ subsets,
  redefines する関連。

  * Figure 14.42 の ``C2`` が ``preCondition`` に相当する。

14.4.3 Semantics
----------------------------------------------------------------------

14.4.3.1 ProtocolStateMachine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ProtocolStateMachine は Classifier の観点で定義される。

ProtocolStateMachine は Classifier のどの BehavioralFeatures を特定の作法状態
で、どのような条件で呼び出すことが可能なのかを指定することで、許可される呼び出し
手順を規定する。Classifier のオブジェクトの一生の仕様が外部観点から定義される。

ProtocolStateMachines は次を指定することで、Classifier の BehavioralFeatures を
呼び出す順序を定義するのに役立つ：

* 有効に呼び出し可能な挙動慣習（どの状態とどの事前条件なのか）
* 呼び出しの有効な順序
* 呼び出しの期待される効果（事後条件）

..

   ProtocolStateMachine present an external view of the owning Classifier as
   perceived by its collaborators.

* これは、その遷移の駆動装置が機能呼び出しであり、遷移のガード
  (ProtocolTransitions) が呼び出しが有効であるために適用されなければならない事
  前条件を指定する状態機械仕様によって達成される。
* この状態機械の状態、ProtocolStates は、過去の呼び出し系列の帰結であり、慣習の
  状態を捉え、事前条件の一形態でもある。

注：ProtocolStateMachines は Classifier の挙動の "black box" ビューを与えるもの
なので、その States は内部動作 StateMachines の States と必ずしも対応しなくても
よい。

ProtocolStateMachine の解釈はいろいろある：

#. 宣言的 ProtocolStateMachines

   BehavioralFeatures 呼び出す際の合法的な Transitions を指定する。

   * BehaviorFeature 呼び出しの効果は指定されない。
   * 仕様のこの型は context Classifier の利用者に契約を設けるだけだ。

#. 実行可能 ProtocolStateMachines

   あるオブジェクトが受信かつ処理することある Event 発生すべてと、それらが引き起
   こす Transitions を指定する。

   * Behavior 呼び出しに合法な Transitions は引き起こされる Transitions と厳密に
     合致しなければならない。
   * この呼び出しの結果、呼び出された BehaviorFeatures に関連するメソッドを実行
     する。

両者の解釈とも仕様は同じであり、唯一の違いは後者の解釈が規定する直接の動的な意味
合いだ。

   The more sophisticated forms of modeling encountered in behavioral
   StateMachines such as compound Transitions, submachine StateMachines,
   composite States, and concurrent orthogonal Regions, can also be used for
   ProtocolStateMachines.

* 例えば同時 Regions はオブジェクトが同時に作動中 States を複数持つことが可能な
  な作法を表現することを可能にする。
* 部分機械 StateMachines と混合遷移を複雑な ProtocolStateMachines の「因数分解」
  に用いることが可能だ。

..

   A Classifier may have several ProtocolStateMachines. This can be used, for
   example, when a Classifier has multiple parents, each having its own
   ProtocolStateMachine, and the protocols are orthogonal.

この代替は、単純に ProtocolStateMachine を一つ持ち、同時 Regions に別々の
StateMachines を持つことだ。

   The States of ProtocolStateMachines are exposed to the users of their context
   Classifiers.

慣習 State はその context Classifier の exposed 安定状況を表す。つまり
Classifier ``classifier`` が BehaviorFeature 呼び出しを処理していないとき、この
オブジェクトの利用者はその状態構成を知ることが常時可能だ。

   The States of a ProtocolStateMachine cannot have defined ``entry``, ``exit``,
   or ``doActivity`` Behaviors.

14.4.3.2 ProtocolTransition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ProtocolTransition は context Classifier の BehavioralFeature を呼び出すための法
定 Transition を指定する。

   ProtocolTransitions have the following features:

   * a pre-condition (``preCondition``), which specializes the ``guard``
     attribute of Transition,
   * a trigger,
   * a post-condition (``postCondition``).

慣習 Transition は次のことを指定する：

* 関連（参照）される機能は呼び出し可能であるのは、context Classifier のオブジェ
  クトが``origin`` State であり、ガード条件が成り立つ場合だ。
* Transition が完了すると、そのオブジェクトは事後条件が成り立つ ``target`` State
  になる。

..

   ProtocolTransitions do not have an associated ``effect`` Behavior.

BehavioralFeature 呼び出しの結果として実行される ProtocolTransition の結末は暗黙
に了解され、呼び出された BehavioralFeature に対応するメソッドの実行だ。

   In case of other types of Triggers, the consequences are unspecified except
   that a Transition will lead to another State under a specific post-condition,
   regardless of any Behaviors associated with this Transition.

14.4.3.2.1 Unexpected trigger reception
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   The interpretation of the reception of an Event occurrence that does not
   match a valid trigger for the current State, state invariant, or
   pre-condition is not defined

定義されていないので、無視、拒否、遅延、例外送出、アプリケーション停止なども可
能。

意味論上は事前条件違反に相当し、UML では事前定義された Behavior は定義されていな
い。

14.4.3.2.2 Unexpected Behavior
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   The interpretation of an unexpected Behavior, that is an unexpected result of
   a Transition (wrong FinalState or FinalState invariant, or post-condition) is
   also not defined.

しかし、これを ProtocolStateMachine の実装の誤りとしてなるべく解釈する。

14.4.3.2.3 Equivalences to pre- and post-conditions of operations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ProtocolTransition は付随する操作の事前条件と事後条件で意味上は解釈できる。

   Figure 14.42 An example of a ProtocolTransition associated with the operation
   "m1"

``[C1]m1/[c2]`` の読み方を習得すること。状態 ``S1`` において条件 ``C1`` が成
立しているときに操作 ``m1`` が呼びだされ、状態 ``S2`` に到達したときには条件
``C2`` が成立している。

   Figure 14.43 Example of several ProtocolTransitions (...)

ProtocolStateMachine では複数の Transitions が同じ操作 (e.g. Fig 14.43 ``m1``)
を参照することが可能だ。その場合、事前条件と事後条件はすべて以下のように操作の事
前条件に組み合わされる：

.. code:: text

   Operation m1()
   Pre:  in state S1 and condition C1
         or
         in state S3 and condition C3
   Post: if the initial condition was “in state S1 and condition C1”
             then in S2 and C2
         else
         if the initial condition was “in state S3 and condition C3”
             then in S4 and C4

ProtocolStateMachine はその Transitions により参照される BehavioralFeature そ
れぞれに対して法定 ProtocolTransition すべてを指定する。

Unreferred Operations:

   If a BehavioralFeature is not referred by any ProtocolTransition, then the
   operation can be called for any State of the ProtocolStateMachine, and will
   not change the current State or pre- and post-conditions.

14.4.3.2.4 Using other types of Events in ProtocolStateMachines
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

BehavioralFeature の呼び出しとは別に、他の Events は ProtocolStateMachines の挙
動を表現することがある。

BehavioralFeature 呼び出しでない Trigger を慣習 Transition に指定することが可能だ。

   In that case, this specification is a requirement for the environment
   external to the ProtocolStateMachine. That is, it is legal to send an Event
   occurrence of this type to an instance of the context Classifier only under
   the conditions specified by the ProtocolStateMachine.

正確な意味解釈は定義されていない。

14.4.3.3 ProtocolConformance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   ProtocolStateMachines can be refined into more specific
   ProtocolStateMachines. Protocol conformance declares that the specific
   ProtocolStateMachine specifies a protocol that conforms to that specified by
   the general ProtocolStateMachine.

ProtocolStateMachine は Classifier が所有する。総体的な StateMachine と関連され
る具体的な StateMachine を所有する Classifiers は、通常、Generalization または
Realization によって接続もされる。

作法適合性は総体的 ProtocolStateMachine に対して指定された規則と制約（状態不変、
操作の事前条件、事後条件）のすべてが、その具体的 ProtocolStateMachine に適用され
るという宣言を表す。

14.4.4 Notation
----------------------------------------------------------------------

この節は Examples も兼ねているようだ。

14.4.4.1 ProtocolStateMachine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ProtocolStateMachine を表す表記法は挙動 StateMachines についてのそれとたいへん似
ている。StateMachine の名前の近くに置かれたキーワード ``«protocol»`` が
ProtocolStateMachine 図を図表的に差別化する。

   Figure 14.44 ProtocolStateMachine example

戸外が無人になれば扉は閉められる。

   Figure 14.45 Notation for a State with an invariant

ProtocolStateMachine の State に付随する不変式のテキスト表現は、その State の名
前の後ろまたは下に配置することで表され、角括弧で括られる。

14.4.4.2 ProtocolTransition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

通常の StateMachine 表記法を適用する。違いは ProtocolTransitions について
``effect`` Behaviors が指定されていないことと、事後条件が存在可能であることだ。
後者はガード条件と同じ構文。Transition 構文の最後に現れる。

   Figure 14.46 ProtocolTransition notation

スラッシュの後にガード条件と同じ記法で事後条件を記すことがある。

14.5 Classifier Descriptions
======================================================================

機械生成による節。

14.6 Association Descriptions
======================================================================

機械生成による節。

.. include:: /_include/uml-refs.txt
