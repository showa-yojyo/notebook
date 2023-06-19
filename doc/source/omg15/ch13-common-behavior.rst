======================================================================
13 Common Behavior
======================================================================

.. contents::
   :depth: 2

13.1 Summary
======================================================================

本章では UML における動作モデリングすべての基礎となる中核概念を規定する。挙動モ
デリングは、Classifier や StructuralFeature のオブジェクトが時間とともにどのよう
に変化するかをモデル化するものだ。

   UML provides Behavior, Event, and Trigger constructs to model the
   corresponding fundamental concepts of behavioral modeling.

   :dfn:`Behavior` is the basic concept for modeling dynamic change.

挙動は直接的にか、挙動を宿す能動的オブジェクト (active object) を生成することに
よって実行 (execute) されることがある。

挙動は、それら自体が特有の個々の挙動を実行しているような一つ以上の関与オブジェク
トの相互作用から生じるものである (emergent) 場合もある。

   Dynamic behavior results in :dfn:`events` of interest that occur at specific
   points in time.

動的な挙動は特定の時点で発生する関心のある事象をもたらす。このようなイベントは、
何らかの値の変化や時間の経過によって発生する暗黙的なものであったり、操作が呼び出
されたときや非同期信号 (signal) を受信したときに発生する明示的なものであったりす
る。

   The occurrence of an event may then :dfn:`trigger` new behavior, or change the
   course of already executing behavior.

明示的な事象は、ある挙動で実行に移された操作の呼び出しや信号の送信などの動作が、
別の挙動での応答を引き起こすことが可能である、挙動間の通信のための基本的な仕組み
を設ける。

この章の残りは Behaviors, Events, Triggers の基本的 UML モデリングの仕組みのさら
なる詳細を述べる。

13.2 Behaviors
======================================================================

13.2.1 Summary
----------------------------------------------------------------------

   This sub clause introduces the framework for modeling behavior in UML. The
   concrete subtypes of Behavior, described in subsequent clauses, then provide
   different mechanisms to specify behaviors.

UML はいろいろな挙動の仕様の仕組みを支援している：

* 有限オートマトンをモデル化する StateMachines: :doc:`./ch14-statemachines`
* Petri ネット的グラフを用いて定義される Activities: :doc:`./ch15-activities`
* 事象発生の半順序連続列をモデル化する Interactions:
  :doc:`./ch17-interactions`

   These behavioral specification mechanisms differ in their expressive power
   and domain of applicability. This means that not all behaviors can be
   described by each of the mechanisms.

それでも挙動の多くは一つ以上の枠組で記述可能だ。あるいは、枠組を複数使用して、同
じ挙動の異なるモデルを与えることも可能だ。

13.2.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 13.1 Behaviors

Behavior を中心に据えたクラス図。新登場するクラスにはその他に OpaqueBehavior と
FunctionBehavior がある。

``A_classifierBehavior_behavioredClassifier``
  BehavioredClassifier から Behavior への関連（単方向）。

``A_method_specification``
  BehavioralFeature から Behavior への関連（双方向）。

``A_precondition_behavior``
  Behavior から Constraint への複合関連（単方向）。

  * ``A_ownedRule_context`` を subsets する。

``A_postcondition_behavior``
  Behavior から Constraint への複合関連（単方向）。

  * ``A_ownedRule_context`` を subsets する。

``A_ownedParameterSet_behavior``
  Behavior から Parameter への関連複合関連（単方向）。

    * Behavior が非同期的に発動されたならば、
      挙動の実行が完了するときにはどんな結果値も失われる。

  * ``A_ownedMember_namespace`` を subsets する。
  * ``ownedParameter`` は ordered だ。

``A_ownedParameterSet_behavior``
  Behavior から ParameterSet への関連複合関連（単方向）。

  * 入力 ParameterSets を伴う Behavior は一実行当たり、一つの集合の Parameters
    から入力を受け入れられるだけ。
  * 出力 ParameterSets を伴う Behavior は一実行当たり、一つの集合の Parameters
    に出力を与えられるだけ。
  * ``A_ownedMember_namespace`` を subsets する。

``A_ownedBehavior_behavioredClassifier``
  BehavioredClassifier から Behavior への複合関連（単方向）。

``A_context_behavior``
  Behavior から BehavioredClassifier への関連（単方向）。

13.2.3 Semantics
----------------------------------------------------------------------

13.2.3.1 Behaviors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A Behavior is a specification of events that may occur dynamically over time
   (see also sub clause 13.3 on the explicit modeling of Events in UML).

この仕様は次のどれでもいい：

* どのような状況でどのようなイベントが発生するかを具体的に示すもの
* 出現する挙動を示すもの
* イベントの発生順序を例示するもの

Behavior はすべて、少なくとも一つのイベント、すなわちその呼び出しのイベントを定
義する。

   A Behavior may be invoked directly, via a BehavioralFeature that it
   implements as a ``method`` or as the ``classifierBehavior`` of a
   BehavioredClassifier.

実行トレースの概念を定義：

   On each invocation, the subsequent actual sequence of event occurrences due
   to the invocation, consistent with the specification of the Behavior, is
   called an :dfn:`execution trace` for the Behavior.

実行トレースは常に Behavior の起動から始まり、（終了しない場合）無限に続くことも
あれば、終了 (termination) イベントが発生した時点で終わることもあり、その場合、
Behavior の実行は完了 (complete) したと言われる。

Behavior は正常に (normally) 完了することもあり、例外の送出をもって完了すること
もある。後者の場合は、Behavior が同期的に起動されたならば、例外 (15.5.3) は呼び
出し側に伝わる。

   Behaviors in UML are kinds of Classes, which means that they may be
   instantiated as objects. An object that is an instance of a Behavior is known
   as a behavior *execution*.

Bahvior を呼び出すことはそのオブジェクト生成に相当し、各 Behavior の実行に対応す
る特定の実行トレースが存在する。

   Since a Behavior is a Class, it may be specialized and may also itself own
   StructuralFeatures and BehavioralFeatures.

Behavior を実行すると、その属性の読み取りや変更など、これらの機能にアクセスする
ことが許される。Behavior の public な構成要素も Class の機能と同様、Behavior 外
部から参照することが許される。

再入可能概念の定義：

   A Behavior may be invoked many times. A :dfn:`reentrant` Behavior (i.e., one
   with its ``isReentrant`` property equal to true) may be invoked again before
   a previous invocation has completed (this is the default). On the other hand,
   a :dfn:`non-reentrant` Behavior (i.e, one with its ``isReentrant`` property
   equal to false) shall not be invoked again if a previous invocation has not
   completed.

再入可能な Behavior はいつでも実行中 Behaviore を多く持つことが許されるが、
再入不能な Behavior は高々一つの未完了の実行をいつでも持たなければならない。

呼び出し側の Bahvior がすでに未完了の実行を持つ再入不能 Behavior を呼び出そうと
した場合、呼び出し側はその実行が完了するまで（実行が完了しない場合は際限なく）ブ
ロックしなければならない。

Behavior を同期性で二分できる：

   A Behavior may be invoked :dfn:`synchronously` or :dfn:`asynchronously`.

事前条件：

   The ``preconditions`` for a Behavior define conditions that shall be true
   when the Behavior is invoked. These ``preconditions`` may be assumed in the
   detailed specification of the Behavior.

事前条件が満たされていない Behavior の呼び出しの意味は意図的に未定義とする。

事後条件：

   The ``postconditions`` for a Behavior define conditions that will be true
   when the invocation of the Behavior completes successfully, assuming the
   preconditions were satisfied.

事後条件はその Bahvior の詳細仕様において満たされるものとする。

13.2.3.2 Behavior Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Bahvior には Parameters を持つものもある：

   A Behavior may have Parameters (see sub clause 9.4) that provide the ability
   to pass values into and out of Behavior executions.

実引数、既定値：

   When a Behavior is invoked, *argument* values may be provided corresponding
   to Parameters with direction “in” or “inout”, as constrained by the
   multiplicity of those Parameters. If such an input Parameter has a
   ``defaultValue``, and no explicit argument value is given for it, then the
   ``defaultValue`` is evaluated to provide argument values for the Parameter
   (even if the Parameter has a multiplicity lower bound of 0, so having no
   value would be valid for it).

実引数は呼び出される Behavior の実行経過に影響するのに利用可能だ。

Behavior は結果を出す：

   When a Behavior execution completes, it may produce *result* values
   corresponding to Parameters with direction “inout,” “out,” and “return,” as
   constrained by the multiplicity of those Parameters.

* 出力 Parameter に ``defaultValue`` がある場合、明示的な結果がなければそれが評
  価される。
* 多重度の概念があるので、結果が空である場合がある。
* 非同期的に呼び出された場合、完了すると結果値が失われる。

次は引数における streaming の概念だ。現代的なプログラミング言語における
coroutine や generator の yield 文でやり取りする実体のようなものだろう。

   Parameters may also be marked as :dfn:`streaming` (i.e., have the
   ``isStreaming`` property be true). Such Parameters allow values to be passed
   into and out of a Behavior execution any time during its course, rather than
   just on invocation and completion.

呼び出し元が streaming 出力 Parameters から放り込まれた値を取得可能にするために
は、呼び出し元 Behavior が同期的に呼び出される必要がある。

   A reentrant Behavior shall not have streaming Parameters,

複数の実行が同時に進む可能性があり、どの実行がストリーム値を送受するかがあいまい
になる。

   A Behavior may have one or more output Parameters marked as ``isException`` =
   true.

この場合、実行が完了したとき、これらの Parameters はいずれも値を持たないか、一つ
だけ値を持ち、他の引数（例外その他）は値を持たないものとする。

注意として例外 Parameter の値を返すことは例外の発生 (15.5.3) とはみなされないと
ある。

そういえば ParameterSet というものがあった：

   A Behavior with input ParameterSets can only accept inputs from Parameters in
   one of the sets per execution. A Behavior with output ParameterSets can only
   post outputs to the Parameters in one of the sets per execution.

ParameterSet の ``preconditions`` と ``postconditions`` の意味は Behavior のそれ
らそれぞれと同じですが、指定された Parameters からなる集合にしか適用されない。

13.2.3.3 Opaque and Function Behaviors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

OpaqueBehavior の定義：

   An OpaqueBehavior is a Behavior whose specification is given in a textual
   language other than UML.

したがって、その言葉を含む実体が存在する。何の言葉で述べられているのかを示すもの
もある：

   An OpaqueBehavior has a ``body`` that consists of a sequence of text Strings
   representing alternative means of specifying the required behavior. A
   corresponding sequence of ``language`` Strings may be used to specify the
   languages in which each of the body Strings is to be interpreted.

言語を指定する必要はなく、未指定の場合には解釈は ``body`` の仕様状況から暗黙的に
決まる。

OpaqueBehavior に一つを超える ``body`` String があれば、そのうちの任意の一つを
OpaqueBehavior の挙動を決定するのに使うことが可能だ。

FunctionBehavior の定義：

   A FunctionBehavior is an OpaqueBehavior that does not access or modify any
   objects or other external data.

* FunctionBehavior の実行中は、外部にある物を伴う通信や相互作用は何であれ禁止。
* 計算時間量は定義されない。
* ある入力値に対しては FunctionBehavior は例外を送出してよい。その場合、計算内容
  は放棄される。

FunctionBehaviors は入力実引数の集合を出力結果値の集合に変換するような関数を表現
する。

* FunctionBehaviors の実行はその実引数にのみ依存して、結果の値を計算すること以外
  の効果はない。
* FunctionBehaviors としてモデル化される関数の例として、初等算術、論理値、文字列
  関数がある。

おそらく副作用のない関数というものだ。

13.2.3.4 Behaviored Classifiers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A BehavioredClassifier is a Classifier that may have ``ownedBehaviors``, at
   most one of which may be considered to specify the behavior of the
   BehavioredClassifier itself.

逆に、BehavioredClassifier の ``ownBehavior`` である Behavior は、この
BehavioredClassifier を ``context`` として持っている。この仕様は ``context``
BehavioredClassifier の機能とそこから見える他の要素も参照することを許す。

Behavior の ``context`` は所有関係の鎖をたどって決まる：

   A Behavior that is not directly an ownedBehavior of a BehavioredClassifier
   may nevertheless still have a context. To determine the context of a Behavior
   that is not directly an ownedBehavior, find the first BehavioredClassifier
   reached by following the chain of ownership relationships from the Behavior,
   if any. If there is such a BehavioredClassifier, then it is the ``context``,
   unless it is itself a Behavior with a non-empty context, in which case this
   is also the ``context`` for the original Behavior.

例えば、BehavioredClassifier が所有する StateMachine の ``entry`` Behavior の
``context`` は StateMachine ではなく、StateMachine を所有する Classifier だ。

   A Behavior that is owned directly by a Class as a ``nestedClassifier`` (see
   sub clause 11.4), rather than as an ``ownedBehavior``, does *not* have the
   Class as its ``context``. The ``nestedClassifiers`` of a Class are simply
   nested in the Class considered as a Namespace.

可視性によっては Behavior 自体が Class の外に見える場合もあるものの、単独の
Behavior としての意味が Class 内に入れ子になることによって他の影響を受けることは
ない。

Behavior に ``context`` がある場合、その Behavior の実行には ``context``
BehavioredClassifier のオブジェクトである *context object* が必ず付随する。

``context`` BehavioredClassifier を持たない Behavior も単独 Behavior として呼び
出すことが許される。この場合、Behavior の実行はそれ自身の context object として
機能する。

   The Behavior execution also serves as its own context object in the case that
   the ``context`` BehavioredClassifier is not instantiable, that is, if it is a
   Component with ``isIndirectlyInstantiated`` = true (see sub clause 11.6) or a
   Collaboration (see sub clause 11.7).

以上のように、Behavior が明示的にオブジェクト化可能な ``context``
BehavioredClassifier を持っているかどうかにかかわらず、Behavior の実行は常に
context object を持つ。

   A BehavioredClassifier may have a distinguished ``ownedBehavior`` called its
   ``classifierBehavior``.

この挙動には、所有者である Classifier がその存命中に経験する可能性のあることを記
述する。

BehavioredClassifier の ``classifierBehavior`` は BehavioredClassifier オブジェ
クトが生成され、それを context object とする実行が行われたときに呼び出されるとみ
なされる。オブジェクトが破棄されると実行は終了する。

   The precise semantics of a ``classifierBehavior`` depend on the kind of
   BehavioredClassifier that owns it.

例えば、Collaboration の ``classifierBehavior`` と Class のそれとでは、表現する
挙動の意味が異なる。

   However, a passive Class (with ``isActive`` = false) shall not have a
   ``classifierBehavior``.

13.2.3.5 Behavioral Features and Methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   There are two kinds of BehavioralFeatures: Operations (see sub clause 9.6)
   and Receptions (see sub clause 10.3). Of the different kinds of
   BehavioredClassifiers in UML, only Classes may have BehavioralFeatures and
   only active Classes may have Receptions (see sub clause 11.4).

Class のオブジェクトに対して Operation を呼び出したり、Signal オブジェクトを送信
したりすることは、特定された BehavioralFeature を実行するようにオブジェクトに対
する要求 (request) だ。

Operation の呼び出しは、呼び出される特定の操作を識別する。一方、Signal のオブ
ジェクトの受信は、この Signal またはその直接的または間接的な一般化を参照する受信
オブジェクトのあらゆる Reception に対する要求であると考えられる。

   A BehavioralFeature of a Class may be implemented by one or more ``method``
   Behaviors.

このような BehavioralFeature は、所有者である Class のオブジェクトが
BehavioralFeature の要求に対して、その機能の実装 ``methods`` の一つを呼び出して
応答することを指定する。

* Behavior は、その ``specification`` と呼ばれる高々一つの BehavioralFeature の
  ``method`` でなければならない。
* Behavior の ``specification`` は、その Behavior が ``ownBehavior`` である
  Class の所有または継承された ``member`` でなければならない。
* BehavioralFeature に複数の ``method`` を関連付けることは可能だが、Class
  (Behavior の ``owner``) と BehavioralFeature (Behavior の``specification``) の
  特定のペアに対する Behavior は高々一つでなければならない。つまり、
  BehavioralFeature 一つは、所有する Class とその Class の直接または間接のサブク
  ラスの両方に ``methods`` を持つことができるが、Class 一つにつき ``method`` は
  一つまでとする。

..

   The receiving object becomes the context object for the execution of any
   invoked methods.

Reception の ``methods`` は常に非同期で起動される。Operation の ``methods`` は呼
び出し方によって、同期的にも非同期的にも起動することがある。

   The method resolution process shall be based on the BehavioralFeature being
   requested, the object receiving the request and any data values associated
   with the request (i.e., Operation input parameter values or Signal attribute
   values).

ただし、UML は適合する UML ツールが特定の解決プロセスをサポートすることを義務づ
けていない。解決プロセスで ``methods`` が特定されない場合、何が起こるかは未定義
だ。

CallEvent に対する単純なオブジェクト指向解決過程の記述を割愛。

   A method of an Operation shall have Parameters corresponding to the
   Parameters of the Operation. Similarly, a ``method`` of a Reception shall
   have Parameters corresponding to the attributes of the Signal referenced by
   the Reception, which are considered as effective “in” Parameters of the
   Reception.

要求に関連するデータ値（入力 Operation 引数値または Signal 属性値）は、
``method`` 引数を介して要求により呼び出された ``methods`` に渡される。同期的な
Operation 呼び出しの場合、``method`` 実行による出力 Parameter 値は、対応する
Operation 出力引数を介して Operation 呼び出し元へも引き渡される。

   However, no specific approach is defined for matching the Parameters of the
   ``method`` to the Parameters of the BehavioralFeature.

可能なものは次のどれかか、その組み合わせとなる：

* 完全一致。対応する Parameters の ``type`` が順序正しく同じである必要がある。
* 共変一致。``method`` の Parameter の ``type`` が BehavioralFeature の
  Parameter の ``type`` の派生型であってもかまわない。
* 反変一致。``method`` の Parameter の ``type`` が BehavioralFeature の
  Parameter の ``type`` の基底型でよい。

13.2.4 Notation
----------------------------------------------------------------------

Behavior の各種サブクラスの記法は後続の章で定義する。

Signals と Receptions の記法は :doc:`./ch10-simple-classifiers` に記載する。

能動的 Class の記法は :doc:`./ch11-structured-classifiers` に記載する。

13.2.5 Examples
----------------------------------------------------------------------

なし。

13.3 Events
======================================================================

13.3.1 Summary
----------------------------------------------------------------------

   An Event is a something that may occur at a specific instant in time.

Event 一つに対して発生は複数ある場合があり、それらは相異なる時刻に起こる場合があ
る。

   Of particular importance are Events that trigger a response within a
   Behavior.

そのような Events で UML が明示的にモデル化するものは次だ：

* TimeEvents: 特定の時刻または期間後に起こる。
* ChangeEvents: 特定の真偽値が真になると起こる。
* MessageEvents: メッセージ (message) の受信で起こる。

メッセージとは «a communication from one Behavior to another requesting an
Operation call or Signal reception» だ。

13.3.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 13.2 Events

Trigger と Event 系のクラス図。Event には直接のサブクラスが先述した三種あり、そ
のうち一つの MessageEvent にだけはさらに直接のサブクラスがやはり三種ある。

``A_event_trigger``
  Trigger から Event への関連（単方向）。単一の Event をいくつかの異なる
  Triggers で用いてよい。

``A_port_trigger``
  Trigger から Port への関連（単方向）。

  その事象が MessageEvent である必要がある場合に、Trigger は一つ以上の Ports を
  指定してよいこの場合は Trigger は指定 Ports の一つを通じて受信したメッセージの
  ための事象の出来事に単に合致する。

``A_operation_callEvent``
  CallEvent から Operation への関連（単方向）。メッセージは ``operation`` の呼び
  出しを要求する。

``A_signal_signalEvent``
  SignalEvent から Signal への関連（単方向）。メッセージは ``signal`` オブジェク
  トの受信を要求する。

``A_changeExpression_changeEvent``
  ChangeEvent から ValueSpecification への複合関連（単方向）。

  * ChangeEvent は式 ``changeExpression`` の値が ``false`` から ``true`` になる
    ときに起こるものだ。
  * ``A_ownedElement_owner`` を subsets する。

``A_when_timeEvent``
  TimeEvent から TimeExpression への複合関連（単方向）。TimeEvent の起こる瞬間を
  指定する TimeExpression だ。

  * ``A_ownedElement_owner`` を subsets する。

13.3.3 Semantics
----------------------------------------------------------------------

13.3.3.1 Event Dispatching
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   An Event is the specification of some occurrence that may potentially trigger
   behavioral effects. A Trigger specifies a specific point in the definition of
   a Behavior at which an Event occurrence may have such an effect.

Event は PackageableElement であり、Events がその用途とは独立してモデル化するこ
とを可能にする。

Trigger は常により大きな挙動仕様 (StateMachine Transition, AcceptEventAction,
etc.) の部分として現れる。

   A single Event may be used in several different Triggers.

Behavior の context object は関連 Behavior 実行の全てについて Event 発生の処理を
仲介する。

Event 発生が context object に認識されると、即時に効果を発揮する場合もあれば、遅
れて効果を出すように保存される場合もある。即効性は BehavioralFeature の
``method`` の呼び出しのような、Event により決定付けられる Behavior の直接呼び出
しにより表明される。

   A triggered effect is manifested by the storage of the occurrence in the
   *event pool* of the object and the later consumption of the occurrence by an
   ongoing Behavior execution that reaches a Trigger that matches the Event
   corresponding to the occurrence in the pool.

イベントプールにあるイベントはこのように処理されるのが一般的だ：

   In general, when a Behavior execution comes to a *wait point* where it needs
   a Trigger to continue, the event pool of its context object is examined for
   an event that satisfies the outstanding Trigger (or Triggers). If the pool
   contains an event occurrence that satisfies one of the Triggers, the
   occurrence is removed from the pool and *dispatched* to the Behavior, which
   continues its execution as specified.

この Event 発生に関連するデータは、引き起こされた Behavior がさらに実行する際に
利用可能になる。

同じ context object を使う Behaviors すべてはそのオブジェクトのイベントプールを
共有するが、プール内の Event 発生は一つの Behavior しか消費することが不可能だ。

   There is no requirement for a specific order in which Event occurrences in an
   event pool are examined or dispatched.

イベントプールに待機点で Triggers を何も満足させない発生がある場合、
BehavioredClassifiers の一般的な意味上は、その発生をどうするかは指定していない。

13.3.3.2 Message Events
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A message is a communication in which a sender makes a request for either an
   Operation call or Signal reception by a receiver.

この通信は二つの事象を伴う。メッセージを送信するイベントとメッセージを受信するイ
イベントだ。

* 送信イベントは UML ではモデル要素ではない。
* 送信イベントは InvaocationActions の実行時に暗黙のうちに存在し、イベントの発生
  を Interactions でモデル化することが可能だ。

MessageEvent はメッセージの受信を明白にモデル化したもので、そのイベントの発生に
応答する Trigger を指定することを可能にするためのものだ。

メッセージは次のものを含む：

* 要求に関連するデータ（Operation 引数に対する実引数または Signal 属性に対する
  値）
* 要求の性質についての情報（つまり呼び出された BehavioralFeature の情報）
* 同期呼び出しの場合、呼び出された Behavior からの返信を可能にするのに十分な情報

..

   While each message is targeted at exactly one receiver object and caused by
   exactly one sending object, an occurrence of a sending event may result in a
   number of messages being generated (as in SignalBroadcastAction, see sub
   clause 16.3).

* メッセージの受信者は、送信者と同一である場合もあれば、現地にある場合もあれば、
  遠隔地にある場合もある。
* メッセージの送信方法、送信に要する時間、送信内容がその受信者オブジェクトに到達
  する順序、受信者オブジェクトに到達するための経路は未定義だ。

メッセージの受信は MessageEvent の発生として表明される。

* CallEvent とは、特定の Operation が呼び出されることを要求するメッセージのため
  の MessageEvent だ。
* SignalEvent とは、特定の Signal のオブジェクトの受信を要求するメッセージのため
  の MessageEvent だ。
* AnyReceiveEvent とは、他の関係 Trigger のどれによっても明示的に処理されること
  のないメッセージの MessageEvent だ。

..

   In the case of a CallEvent for an Operation or a SignalEvent for a Signal
   that matches a Reception on the receiver, if the Operation or Reception has
   one or more ``methods``, then the ``method`` resolution process described for
   Behavioral Features and Methods in sub clause 13.2.3 shall be carried out to
   determine a method to be used to handle a MessageEvent occurrence.

* そうして ``method`` が特定される場合、それがメッセージ要求に応答するために呼び
  出される。さもなくば、MessageEvent の発生が受信オブジェクトのイベントプールに
  保存される。
* イベントプールから発送された MessageEvent の発生が受信側の Behavior 仕様で定義
  された Trigger に合致すると、この Behavior 内部での応答が実行される。

..

   A Trigger for an AnyReceiveEvent may be triggered by the receipt of any
   message (Signal send or Operation call).

* ただし、メッセージに明示的に合致する適切な SignalEvent または CallEvent
  Trigger がある場合には、AnyReceiveEvent Trigger はそのメッセージによって引き起
  こされない。
* AnyReceiveEvent Trigger に関連する他の Triggers は、この Trigger の context に
  依存する。特に、Transitions に関する 14.2 節と AcceptEventActions に関する
  16.10 節を参照。
* SendObjectAction によって送信されるような SignalInstance 以外のオブジェクトを
  含むメッセージの受信によって AnyReceiveEvent が引き起こされることもある
  (16.3.3)。

Trigger は Port を一つ以上指定することもでき、その場合、Trigger のイベントは
MessageEvent でなければならない。

    In this case the Trigger only matches event occurrences for messages
    received through one of the specified Ports

13.3.3.3 Change Events
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A ChangeEvent occurs when a Boolean changeExpression becomes true.

例えば、ある Attribute 値の変化や、ある Association に対応するリンクが参照する値
の変化の結果として発生することがある。

ChangeEvent は暗黙的に発生するものであり、明示的な作用の結果ではない。

   An occurrence is considered to be generated any time the value of the
   ``changeExpression`` changes from false to true.

ただし、``changeExpression`` がいつ評価されるのか、発生が消費される前に関連した
``changeExpression`` 値が偽に戻っても、ChangeEvent 発生が検出可能なまま残ってい
るかのどうかは、特に定義されていない。

13.3.3.4 Time Events
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A TimeEvent specifies an instant in time at which it occurs.

* その瞬間は TimeExpression (8.4) を使って指定される。
* TimeEvent が絶対的時刻である場合、TimeExpression の評価から得られる時間が
  TimeEvent が発生する絶対的時刻だ。
* TimeEvent が相対的時刻である場合、TimeEvent はある Trigger の context で使用さ
  れなければならず、発生時刻はこの Trigger のために決定された開始時刻に対して相
  対的なものでなければならない。

Behavior はイベント発生を発送されることがある Triggers が一つ以上ある時点で待機
点になることがある。このような未済 Trigger に相対 TimeEvent がある場合、この
TimeEvent の開始時刻は Behavior が待機点に到達した時刻となる。

13.3.4 Notation
----------------------------------------------------------------------

Triggers で使用される文脈以外では Events に関する記法はない。Trigger は Event の
種類に基いてテキストで表記される：

.. code:: bnf

   <trigger> ::= <call-event> | <signal-event> | <any-receive-event> | <time-event> | <change-event>

ここで各 ``<xxxx-event>`` は対応する Event の記法だ。

CallEvent は原因 Operation の名前で示され、その後に代入指定を続けてもよい：

.. code:: bnf

   <call-event> ::= <name> [‘(‘ [<assignment-specification>] ‘)’]
   <assignment-specification> ::= <assigned-name> [‘,’ <assigned-name>]*

* ``<assigned-name>`` は Operation の対応する Parameter の実引数の、引き起こされ
  る Behavior に対する context object の Property または Variable への暗黙的な代
  入だ。
* ``<assignment-specification>`` は Operation に Parameters がある場合でも省略す
  ることが許される。

SignalEvent は原因 Signal の名前で示される。その後に代入仕様が続いてもよい：

.. code:: bnf

   <signal-event> ::= <name> [‘(‘ [<assignment-specification>] ‘)’]
   <assignment-specification> ::= <attr-name> [‘,’<attr-name>]*

* ``<assignment-specification>`` は CallEvent に対して定義されたものだ。

どの AnyReceiveEvent についても ``all`` と記す：

.. code:: bnf

   <any-receive-event> ::= ‘all’

ChangeEventは、``when`` の後に真偽 ValueSpecification が続くことで示される。
:doc:`./ch08-values` 参照：

相対 TimeEvent は ``after`` の後に TimeExpression を付けて表記する。例えば
``"after 5 seconds"`` など。絶対 TimeEvent は ``at`` の後に TimeExpression を続
けることで指定する。例えば``"at Jan. 1, 2000, Noon"`` など：

.. code:: bnf

   <change-event> ::= ‘when’ <value-specification>

   <time-event> ::= <relative-time-event> | <absolute-time-event>
   <relative-time-event> ::= ‘after’ <time-expression>
   <absolute-time-event> ::= ‘at’ <time-expression>

13.3.5 Examples
----------------------------------------------------------------------

なし。

13.4 Classifier Descriptions
======================================================================

機械生成による節。

13.5 Association Descriptions
======================================================================

機械生成による節。

.. include:: /_include/uml-refs.txt
