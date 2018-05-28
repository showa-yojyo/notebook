======================================================================
14 StateMachines
======================================================================
UML 2.5 pp. 303-370 に関するノート。

.. todo:: 誤訳や変な解釈がいかにもありそうなので、発覚次第修正する。

.. todo::

   訳語検討。

   * configuration (n.) ここでは「配置」とする。

   * enter (v.) 入場する。
   * exit (v.) 退場する。

   * orthogonal (adj.) 「直交の」だが、
     たいていの場合、幾何学的な意味あいでとは限らない。

   * protocol (n.) 通信等の手順。
     「約束によって成り立っている規則」くらいの意味だろう。
     辞書には儀礼とか典礼ともあり、むしろここではこれらが相応しい？

   * submachine (n.) 「部分機械」と機械的に訳すことにする。
   * substate (n.) 「部分状態」。

   * trigger (n.) 普通はカタカナで「トリガー」とするのが一般的だが、
     実験的に「引き金」や、踏み込んで「撃鉄」なども採用する。

.. contents:: ノート目次
   :depth: 2

14.1 Summary
======================================================================
* StateMachines パッケージは、
  有限状態機械の形式論を使って離散的イベント駆動の Behaviors を
  モデリングすることに対して用いることができる概念の集合を定義する。

  * システムの部分の Behavior を表現することに加えて、
    状態機械は有効な相互作用の連続、プロトコルと呼ばれるもの
    を表現するために用いることもできる。

  * これらの StateMachines の二種類はそれぞれ
    挙動状態機械 (behavior state machines) と
    規約状態機械 (protocol state machines) と呼ばれる。

* UML で用いられる有限状態機械の特有の表現形式は、
  David Harel の statecharts 形式論のオブジェクト指向の変種に基づく。

14.2 Behavior StateMachines
======================================================================

14.2.1 Summary
----------------------------------------------------------------------
* Behavior StateMachines を次のどれを
  明確に記述することに用いることが可能だ。

  * 能動的な Class の ``classifierBehavior``
  * BehavioredClassifier の ``classifierBehavior`` でない ``ownedBehavior``
  * 対応する BehavioredClassifier のない Behavior
  * BehaviorFeature (Operation or Reception) に対応するメソッド

14.2.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 14.1 Behavior StateMachines

  * まさに機械の名に相応しい図式である。
    あまりに関連が多いため、一部コネクターが交差してしまっている。

  * 新登場クラスが
    StateMachine, Region, Vertex, Transition,
    Pseudostate, ConnectionPointReference, State, FinalState
    と、とにかく多い。

A_region_stateMachine
  * StateMachine から Region への composite 関連（双方向）。
  * StateMachine が直接所有する Regions である。
  * 関連端 ``region`` の多重度は ``1..*`` である。必ずひとつは存在する。

A_connectionPoint_stateMachine
  * StateMachine から ConnectionPointReference への composite 関連（双方向）。
  * StateMachine が ``submachine`` State の一部として用いられているときに定義する。

A_submachineState_submachine
  * StateMachine から State への関連（双方向）。
  * ``submachine`` State の際に StateMachine が参照する ``submachine(s)`` である。
    複数個を参照する条件は、concurrency が関係してくるらしい。

A_subvertex_container
  * Region と Vertex の間の composite 関連（双方向）。
  * Region が Vertices を所有する。

A_transition_container
  * Region と Transition の間の composite 関連（双方向）。
  * Region が Transitions を所有する。
  * 関連端 ``container`` の多重度が 1 なので、
    任意の Transition は必ずある Region に属する。

A_incoming_target, A_outgoing_source
  * Vertex と Transition の間の関連（双方向）。
  * ひとつの Transition には ``source`` と ``target`` という
    Vertex がひとつずつ対応する。
  * 関連端 ``incoming`` と ``outgoing`` は readOnly である。

A_region_state
  * State から Region への composite 関連（双方向）。
  * State は StateMachine と同様に Regions を所有する能力がある。
    ただし関連端 ``region`` の多重度は ``*`` である。

A_stateInvariant_owningState
  * State から Constraint への composite 関連（単方向）。
  * この State が current であるときに常に成り立つ条件、不変条件である。
  * 関連端 ``stateInvariant`` の多重度は ``0..1`` なので、オプションである。

A_deferrableTrigger_state
  * State から Trigger への composite 関連（双方向）。
  * State は遅延可能トリガー（後続のある State configuration に到達するまでに
    処理されていればよいトリガー）を任意個所有する。
  * スラッシュの後に書かれているアレ。

A_entry_state, A_doActivity_state, A_exit_state
  * State から Behavior への参照。
  * Behavior 側関連端の意味については先ほどのノート参照。
  * Behavior 側のいずれの関連端の多重度も ``0..1`` なので、
    これらの挙動の定義はオプションである。

A_connection_state
  * State から ConnectionPointReference への composite 関連（双方向）。
  * この ``submachine`` State と一緒に用いる entry/exit 接続点 (pl.) を所有する。
  * cf. A_entry_connectionPointReference, A_exit_connectionPointReference

A_connectionPoint_state
  * State から Pseudostate への composite 関連（双方向）。
  * 自身が合成 State であるときに限り、その entryPoint と exitPoint を定義・所有する。

A_entry_connectionPointReference, A_exit_connectionPointReference
  * ConnectionPointReference から Pseudostate への関連（単方向）。
  * 対応する entryPoint/exitPoint への関連を示す。

A_trigger_transition
  * Transition から Trigger への composite 関連（単方向）。
  * この Transition を誘発してよい Triggers である。

A_effect_transition
  * Transition から Behavior への composite 関連（単方向）。
  * 関連端 ``effect`` はこの Transition が発火するときに実施される挙動。
    多重度が ``0..1`` なのでオプション。

A_guard_transition
  * Transition から Constraint への composite 関連（単方向）。
  * ガード条件を表す。この ``guard`` が true になれば
    Transition は使用可能になる。
  * 関連端 ``guard`` の多重度が ``0..1`` なのでオプション。

14.2.3 Semantics
----------------------------------------------------------------------
14.2.3.1 StateMachine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* 挙動 StateMachine はひとつまたはそれを超える Regions を構成し、
  Region のそれぞれは
  Transitions を表す辺によって相互に接続されている
  Vertices の集合を（もしかすると階層的に）構成するグラフを含んでいる。

* StateMachine に BehavioredClassifier 脈絡の一種があれば、
  その Classifier は
  どの Signal と CallEvent の引き金が StateMachine にとって適用可能なのか、
  そしてどの Features が StateMachine が所有する Behaviors にとって
  適用可能なのかを定義する。

* StateMachine に BehavioredClassifier 脈絡がなければ、
  つまり Behavior が単独動作するものならば、
  それの Triggers は何か Classifier の Receptions や Operations のどれにも
  結び付いている必要がない。

* StateMachine が BehavioralFeature (Operation or Reception) の
  ``method`` を指定する場合には、
  StateMachine の Parameters はその BehavioralFeature の Parameters に
  一致するものとする。

* 定義から、StateMachine の実行の発動はきっかけとなった効果に帰着する。
  それゆえ、そのような実行に結び付いた事象プールがある。

* それのイベント駆動型という性質のため、
  StateMachine の実行は in transit か in state のどちらかであり、
  両者を行ったり来たりする。

* StateMachine の実行は、
  それが安定状態配置で落ち着いたとき、
  それの活性状態配置に結び付いた ``doActivity`` Behaviors が
  ある場合であっても、
  Behaviors を実行していることが許される。

14.2.3.2 Regions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Region は、それの直交する Regions と共に
  同時に実行することが許される挙動の断片を記す。

  * Regions が互いに直交するの意味は、次のどちらかを意味する。

    * 同一の State が Regions を所有する。
    * 最上位において同一の StateMachine が Regions を所有する。

  * Region それぞれは Vertices と Transitions の集合を所有し、
    それは Region 内部の挙動の流れを決定付ける。

  * Region にはそれ自身の FinalState はもちろん、
    自身の **initial** Pseudostate があってよい。

* Region の既定の活性化は Region が暗黙的に入場されると、
  すなわち、それの成分の Vertices を終端とする流入 Transition を
  経由せずに入場されると発生する。

* 既定の活性化とは、
  実行が Region の **initial** Pseudostate を起点とする Transition で開始する
  ことを意味する。

* 逆に、
  Region が Region が含む Vertices のひとつを終端とする
  Transition により入場されると、
  明示的な活性化が発生する。

14.2.3.3 Vertices
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Vertex とは、
  StateMachine グラフにある異なる具象型ノード
  (States, Pseudostates, or ConnectionPointReferences)
  の色々なものに共通する特徴を捉える抽象的クラスである。

  * 下で述べるある例外の場合には、
    Vertex はどんな個数の Transitions の ``source`` または ``target``
    またはその両方であり得る。

* Vertices の個々の種類の意味は下で述べる。

14.2.3.4 States
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* State は
  その間中に何らかの不変条件が成り立つ
  StateMachine Behavior の実行における情況をモデル化する。

  * たいていの場合、この状況は明示的に定義されず、暗黙的にされ、
    ふつうは State に結び付いた名前で定義される。

  * 例えば Figure 14.36 では、これは電話器の挙動のモデル化であるが、
    状態 Idle と Active は電話が使用中と未使用中である状況をそれぞれ表す。

14.2.3.4.1 Kinds of States
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* State の次の 3 種類が区別される：

  単純 State (``isSimple`` = true)
    単純 State には内部的な Vertices も Transitions もない。

  合成 State (``isComposite`` = true)
    合成 State は少なくともひとつの Region を含む。

  部分機械 State (``isSubmachineState`` = true)
    部分機械 State は StateMachine 丸ごとを参照し、
    これは概念的にはこの State の内部に「入れ子」になっていると考えられる。

* 合成 State の Region で取り囲まれた State はどれでもが
  その合成 State の部分状態であると呼ばれる。

  直接的部分状態
    他のどの State 内にもない部分状態をそう呼ぶ。

  間接的部分状態
    直接的部分状態でない State をそう呼ぶ。

14.2.3.4.2 State configurations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* 一般には、StateMachine には Regions が複数あり得て、
  それぞれは自身の States を含み、
  それらの中には自身の Regions 等による複数合成物であるものもあってよい。

  * States の複雑な階層は State または StateMachine の状態配置と呼ばれる。

  * 実行している StateMachine オブジェクトは
    一度に厳密に一つの状態配置にならないが、
    このことはそれの活性状態配置と呼ばれる。

* State が活性であるとは、それが活性状態配置の部分であるときを言う。

* 状態配置が安定であるとは、

  * その状態配置からそれ以上遷移可能な Transitions がなく、
  * その状態配置の ``entry`` Behaviors が（もしあれば）すべてが
    完了したときである。

* StateMachine は生成して最初の Transition を完了した後に、
  いつでも何らかの状態配置になる。

* Event の発生の遅延、完了、または他の種類のいずれかが
  その StateMachine の事象プールで未決になっているときでさえ、
  配置は安定していると考えられる。

14.2.3.4.3 State entry, exit, and doActivity Behaviors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* State には付随する ``entry`` Behavior があってよい。
  この Behavior が定義されていれば、
  State が **external** Transition を通じて入場したときにはいつでも実行される。

  * さらに、State には付随する ``exit`` Behavior があってよい。
    これが定義されていると、State が退場するときにはいつでも実行される。

* State には ``doActivity`` Behavior があってもよい。
  この Behavior は State に入場されると
  （ただし State ``entry`` Behavior が完了した後に）
  実行を開始し、
  State に付随してよい他の Behaviors のどれとも同時に、
  次に挙げるものまで実行する。

  * それが完了する（完了事象が生成される場合）か、
  * State が退場されるとき。
    それは ``doActivity`` Behavior の実行が中断される場合である。

* State の ``doActivity`` Behavior の実行は
  その State の **internal** Transition の発射の影響を受けない。

14.2.3.4.4 State history
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* State 履歴の概念は David Harel によって
  原作の状態図表形式論で導入された。
  Region がそれが最後に退場したときの状態配置を追跡するということによる
  合成 States の Regions に付随する便利な概念であり、

* 履歴 Pseudostates には二種類がある。

  * 深い履歴 (**deepHistory**) は最近訪れた Region の完全な状態配置を表す。
  * 浅い履歴 (**shallowHistory**) は最近の状態配置の
    最上位の部分状態のみに対する復帰を表し、
    既定の入場規則を使って入場される。

* State が以前に入場されていない（つまり先だっての履歴がない）ときか、
  それの FinalState に到達したときに、
  Transition が履歴 Pseudostate で停止すると、
  遷移を特定の部分状態に強制する選択肢、既定の履歴機構を使うこと、がある。

* State はその State で遅延してよい Event の型の集合を指定してよい。

* Event は合成 State または部分機械 States によって遅延されてよいが、
  合成 State が活性配置のままである限りは、
  それは遅延されたままという状況である。

14.2.3.4.5 Entering a State
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* State に入場するという意味は、
  State の型と入場方式に依存して決まる。

  * いずれの場合も、
    流入 Transition に付随した ``effect`` のどれもが完了した後に、
    State の ``entry`` Behavior が（定義されていれば）入場時に実行される。

  * その上、
    ``doActivity`` Behavior が State に対して定義されていれば、
    この Behavior は先の ``entry`` の完了直後に実行を開始する。

* 単一 Region からなる合成 States の場合には、次の選択肢がある。

  既定の入場
    合成 State が Transition の直接的 ``target`` であるときにこの状況になる。

  明示的入場
    流入 Transition やその連続物が合成 State の直接的に含まれた部分状態で
    停止すれば、その部分状態は活性化して、
    その ``entry`` Behavior は含んでいる合成 State の
    ``entry`` Behavior の実行の後に実行される。

  浅い履歴の入場
    流入 Transition が合成 State の Region の **shallowHistory** Pseudostate で
    停止すれば、活性部分状態はこの入場に先立つ最近活性だった部分状態となる。

  深い履歴の入場
    この場合の規則は、
    ``target`` Pseudostate が **deepHistory** 型であることと、
    このものの下の活性状態配置のすべての階層に対して
    規則が再帰的に適用されることを除いて、
    浅い履歴の場合と同じである。

  入口点入場
    Transition が **entryPoint** Pseudostate を通じて合成 State に入場すれば、
    その入口点を起点とし、その State に入り込む
    流出 Transition に付随する ``effect`` Behavior が
    （合成 State の ``entry`` Behavior が実行された後に）実行される？

* 合成 State が Regions を複数有する直交 State でもあると、
  その Regions のそれぞれもまた既定入場または明示的入場により入場される。

* どのように State に入場するかに関わらず、
  たとえその State の ``entry`` や ``effect`` が（定義されていれば）
  実行を開始する前であっても、
  StateMachine はその State に「なる」と考えられる。

14.2.3.4.6 Exiting a State
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* State を退場する際には、それが単純であるか合成であるかに関係なく、
  出口において必然的に起こる最終段階は、
  出口に付随する他の Behaviors すべてが完了後の、
  その State の ``exit`` Behavior の実行である。

  * State の退場時に ``doActivity`` がまだ実行中ならば、
    それは ``exit`` の実行開始前に中断される。

* 合成 State からの退場時は、
  活性状態配置の最も内側の State の ``exit`` が開始する。

* 直交 State からの退場時は、
  その Region のそれぞれが退場される。
  その後に State の ``exit`` Behavior が実行される。

* どのように State を退場するかに関わらず、
  その State の ``exit`` Behavior が実行完了した後にしか
  StateMachine はその State を離脱したと考えられない。

* Transitions が State に直接入り込むのを認めず、
  その内部の Vertices のひとつで停止しないようにすることで、
  合成 State をカプセル化することが有用であるモデリング状況がある。

* 入口点は流入 Transitions については停止点 (``sources``) を表す。
  合成 State の内部 Vertex のなにかで停止する Transitions については
  開始点 (``targets``) を表す。

* 出口点は入口点の逆のものである。

14.2.3.4.7 Submachine States and submachines
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* 部分機械は単一の StateMachine 仕様を複数回再利用可能にする方法である。

  * プログラミング言語におけるマクロのように、相異なる Behavior の仕様である。
    ``isSubmachineState`` はこれを達成する属性である。

* 部分機械 State は該当する部分機械 StateMachine の
  仕様のマクロ的な付け加えを含意する。
  それはゆえに、意味としては合成 State と同値である。

* たとえ二個またはそれを超える部分機械 States が
  同じ部分機械を参照するときでも、
  部分機械 State のそれぞれは部分機械の区別されたオブジェクト化を表す。

* 部分機械 StateMachine はその既定の (**initial**) Pseudostate を経てか、
  あるいはその入口点のどれかを経て入場されることができる。

* 同様に、部分機械 StateMachine は次の結果として退場されることができる。

  * その FinalState に到達する
  * 部分機械 State を起点とする集団 Transition のきっかけ
  * その出口点のどれかを経て

* FinalState を経て退場するのと、
  集団 Transition によって退場するのは、
  普通の合成 States の場合は同じ意味である。

14.2.3.5 ConnectionPointReference
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* 上で述べたように、
  ConnectionPointReference は
  部分機械 State で参照される StateMachine で定義された
  入口点・出口点の（部分機械 State の部分としての）用法を表す。

* ConnectionPointReferences は、
  部分機械 State により参照される部分機械 StateMachine からの出口点
  またはそれへの入口点を含意する
  Transitions の ``sources`` または ``targets`` である。

* Transition の対象としての入口点の ConnectionPointReference は、
  Transition の ``target`` が
  部分機械 State の部分機械で定義された
  **entryPoint** Pseudostate であることを含意する。

* Transition の出処としての出口点の ConnectionPointReference は、
  Transition の ``source`` が
  部分機械 State の部分機械で定義された
  出口点 Pseudostate であることを含意する。

14.2.3.6 FinalState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* FinalState とは、
  取り囲んでいる Region が完了したことを知らせる
  特別な種類の State である。
  このように、FinalState へ遷移する Transition は
  その FinalState を含んでいる Region の挙動の完了を表す。

14.2.3.7 Pseudostate and PseudostateKind
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Pseudostate とは StateMachine グラフ内にある
  一時滞在 Vertices の種々の型を取り囲む抽象的概念である。
  Pseudostates は通常、複数の Transitions をより複雑な
  複合遷移となるように連鎖させるのに用いる。

* Pseudostate の特別な意味は Pseudostate の型に依存し、
  それは型 PseudostateKind の ``kind`` 属性に定義される。
  次に種類と意味を記す。

  initial
    Region の開始点。

  deepHistory
    所有 Region の直近の活性状態配置を表現する変数の一種。

  shallowHistory
    **deepHistory** のようなものだが、
    その部分状態の部分状態ではないもの。

  join
    ふたつ以上の Transitions の共通の ``target`` Vertex として役に立つ。

  fork
    ふたつ以上の Transitions に分岐するのに適う。

  junction
    複数の Transitions を接続して States 間の複合パスを作るのに用いる。

  choice
    **junction** に似ているが、
    流出 Transitions すべての ``guard`` Constraints を動的に評価する点が異なる。

  entryPoint
    StateMachine または合成 State に対する入口。

  exitPoint
    StateMachine または合成 State に対する出口。

  terminate
    ここに入場することは StateMachine の実行が直ちに停止することを暗示する。

14.2.3.8 Transitions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Transition とは、
  単一の ``source`` Vertex を始点とし、
  単一の ``target`` Vertex を終点とする単方向リンクであり、
  StateMachine Behavior の有効な断片を指定するものである。

  * ここで ``source`` と ``target`` は同じ Vertex であることが許される。
  * Transition には関連する ``effect`` Behavior があってもよく、
    Transition が走査されるときに実行される。

* Transition 走査の期間は未定義であるが、
  さまざまな意味上の解釈を考慮して、
  ゼロと非ゼロ時間の両方を含んでいる。

* Transitions は、
  StateMachine 実行をある安定状態配置から別の配置へと持っていく
  より複雑な複合遷移の一部として実行される。

* 実行の途中では、Transition オブジェクトは次のどれかであると言う。

  reached
    その StateMachine 実行の実行が
    その ``source`` Vertex に到達した
    （つまりその ``source`` State が活性状態配置にある）とき。

  traversed
    それが（関連する ``effect`` Behavior のどれとも一緒に）
    目下実行されているとき。

  completed
    それが ``target`` Vertex に到達した後。

* Transition は Triggers の集合を所有してよく、
  それぞれはそれの出来事が発送されたときに
  Transition の走査のきっかけになれる Event を指定する。

14.2.3.8.1 Transition kinds relative to source
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* Transition の意味はその ``source`` Vertex との関係に依存して決まる。
  三個の異なる可能性が定義されており、
  Transition の ``kind`` 属性の値に依存している。

  external
    Transition はその ``source`` から退場する、の意。

  local
    **external** の反対であり、
    Transition はそれを含む State から退場しない、の意。

  internal
    自己遷移をする **local** Transition の特別な場合であり、
    State が決して退場されないようになり、
    この Transition が実行されるときに
    出口 Behavior も入口 Behavior も実行されないことを意味する。

14.2.3.8.2 High-level (group) Transitions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* ``source`` Vertex が合成 States である Transitions は、
  高水準または集団 Transitions と呼ばれる。

14.2.3.8.3 Completion Transitions and completion events
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* 特別な種類の Transition は完了 Transition であり、暗黙の Trigger がある。
  合成または部分機械 States の場合は、
  完了事象は次の条件で生成される：

  * 内部の活動（例えば ``entry`` と ``doActivity`` Behaviors）のすべてが
    実行を完了して、

  * State が合成 State であれば、
    その直交 Regions のすべてが FinalState に到達したか、

  * State が部分機械 State であれば、
    その ``submachine`` StateMachine の実行が FinalState に到達した。

* 完了事象は発送優先権がある。
  つまり、それらは事象プールにある未決 Event の出来事の
  どれよりも早くに発送される。

* Transition に付随する ``guard`` Constraint があってよい。

  * false に評価される ``guard`` を有する Transitions は使用不能である。

  * 評価されるタイミングは、
    それを含む複合 Transition が利用可能になる前である。

  * 付随する ``guard`` がない Transition は、
    あたかもそれが常に true に評価される ``guard`` があるかのように取り扱われる。

14.2.3.8.4 Compound transitions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* 先に述べたように、
  Event の出来事が利用可能な Transition のきっかけとなったり、
  または StateMachine の実行が生成したりすると、
  安定状態配置に至るまでは、
  これは接続されて入れ子になった Transitions と Vertices の集合の
  走査を新しく始まることがある。
  一般の場合に、この走査の追跡は複合遷移として知られていて、
  非循環有向グラフとして表すことができる。
  このグラフの根は次のうちのひとつであるはずである。

  * ひとつまたはそれを超える Triggers が定義された Transition

  * 完了 Transition

  * ある共通の **join** Pseudostate に収束する
    相異なる直交 Regions を起点とする Transitions の集合

  * 最上位 Region の **initial** Pseudostate を起点とする Transition

* 複合遷移で実行の分岐が生じるのは、

  * Transtion を実行することが
    直行する Regions が複数あり、
    別々の分岐が Region それぞれに対して生成されている
    State への既定の入場を実施するときのいつでもか、

  * または **fork** Pseudostate に遭遇したときである。

* ``guards`` のある流出 Transtions が複数ある
  **choice** または **join** 点に到着すると、
  Transtion の ``guard`` が true と評価するものが取られる。

14.2.3.8.5 Transition ownership
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* Transition が含まれている Region は
  直接間接を問わず StateMachine が所有する必要があるのだが、
  Transition の所有者は明示的に制限されていない。

  * Transition の推奨される所有者は、
    その ``source`` と ``vertex`` の両方を含む Region の
    最も内側のものである。

14.2.3.9 Event Processing for StateMachines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
14.2.3.9.1 The run-to-completion paradigm
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* StateMachine 実行による Event 出来事の処理手順は、
  :doc:`./common-behavior` で定義した一般的な意味に従う。

* StateMachine は完了事象に対してだけではなく、
  :doc:`./common-behavior` で記述した Event の種類のどれに対しても
  応答することができる。

* 上で説明したように、
  完了事象には優先権があり、事象プールにある未決 Event 出来事のどれよりも早く
  送達されるものである。

* Event 出来事は StateMachine 実行によって一つずつ検知、送達、処理される。

* さまざな予定決定計算法を考慮に入れて、
  事象送達の順序は未定義のままにしてある。

* ???

* Event 出来事が検知されて送達されると、
  ひとつまたはそれを超える Transitions が点火可能になることが許される。

* 直交 Regions があるため、
  （異なる Regions にある）複数の Transitions を
  同じ Event 出来事がきっかけとして起こることができる。

* 上で言ったように、
  Region にある複数の互いに排他的な Transitions が
  同じ Event 出来事によって点火可能になることが可能である。

* Transition の間じゅうずっと、行動 Behaviors がいくつか実行されてよい。

* Run-to-completion をさまざまな手段で実装してよい。

* Run-to-completion は、
  実行している StateMachine は割り込まれないことを
  含意するものと誤って解釈されることがよくあるが、
  これは当然、時間に繊細なシステムでは優先権逆転問題に誘導しようとする。

14.2.3.9.2 Enabled Transitions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* Transition は次の時に、かつその時に限って使用可能になる：

  * その ``source`` States のすべてが活性状態配置にある。

  * Transition の ``triggers`` の少なくともひとつに
    送達された Event 出来事の Event 型により一致する Event がある。

  * 起点状態配置から目標状態配置または
    ``guards`` 条件すべてが true である
    動的な **choice** Pseudostate の
    どちらかに至る完全経路が少なくともひとつ存在する。

* ひとつを超える Transition が同じ Event 出来事によって
  使用可能になることが認められているので、
  Transition の点火が使用可能になることは必要だが十分条件ではない。

14.2.3.9.3 Conflicting Transitions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* ひとつを超える Transition が StateMachine では使用可能になることができる。
  もしそれが起こるならば、そのような Transitions は互いに相容れなくてよい。

* ふたつの Transitions が衝突するとは、
  それら両方が同じ State を退場することを、
  より正確には、
  それらが退場する States の集合の共通部分が空ではないことである。

* State の **internal** Transition は
  その State からの退場の原因になる Transitions にしか衝突しない。

14.2.3.9.4 Firing priorities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* 衝突する Transitions がある状況では、
  どの Transitions が点火するかという選択は、
  暗黙の優先権にいくらか基づく。

* Transition の優先権はその ``source`` State に基いて定義される。

* 一般に、t1 を ``source`` State が s1 の Transition とし、
  t2 に ``source`` s2 があるものとするならば：

  * s1 が s2 の直接または間接的に入れ子になった部分状態ならば、
    t1 には t2 よりも高い優先権がある。

  * s1 と s2 が同じ状態配置になければ、
    t1 と t2 の間に優先権の違いはない。

14.2.3.9.5 Transition selection algorithm
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* 点火することになる Transitions の集合は、
  次の諸条件を満たす現在の状態配置の Regions にある Transitions である：

  * 集合にある Transitions すべてが使用可能である。
  * 集合には衝突 Transitions がない。
  * 集合にある Transition よりも高い優先権のある
    集合の外側に Transition があるということがない。

* これは強欲な選択計算法により実装することができ、
  活性状態配置の直截な走査を伴う。

14.2.3.9.6 Transition execution sequence
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* **internal** および **local** Transitions を除き、
  どの Transition も ``source`` State の退場および
  ``target`` State の入場をもたらす。
  これらふたつの States は、合成でもよいが、
  Transition の主始点と主終点としてそれぞれ指名される。

* 主始点は ``source`` States を含む Region の直接部分状態であり、
  主終点は ``target`` States を含む Region の直接部分状態である。

* ある Region から同じ直接取り囲む合成 State にある
  別の Region への Transition は許されない。

* いったん Transition が使用可能となって点火するように選択されると、
  次の処置がこの順に実施される：

  #. 主始点 State から開始して、
     その主始点 State を含む States が
     先に述べた State 退場規則に則って退場される。

  #. 主始点と主終点の両方を直接または間接的に含む最初の Region に到達するまで、
     State 退場の系列が続行する。

  #. 主終点 State を含む States の配置に入場し、
     主終点 State を含む Region の最小共通先祖にある
     最も外側の State で開始する。

* この遷移実行法は Figure 14.2 の StateMachine 見本が図解する。

* Figure 14.2 Compound transition example

  * この場合、StateMachine が State S11 にある間、
    事象 sig が送達されて、次の行動の列が実行されるはずである：

    xS11; t1; xS1; t2; eT1; eT11; t3; eT111

  * 要点は入れ子になっている States と Transitions の遷移順序が
    外側からなのか内側からなのかが始点に近いか終点に近いかで
    決まるということのようだ。

14.2.4 Notation
----------------------------------------------------------------------
14.2.4.1 StateMachine Diagrams
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* StateMachine 図は StateMachines を明確に定義する。

* StateMachine 図は StateMachine を表すグラフである。
  StateMachine グラフにある States およびさまざまな型の Vertices は
  適当な State および Pseudostate 記号で描画される。
  それに対して、Transitions は普通はそれらを接続する有向辺か、
  Transition の Behavior の動作を表す制御器号によって描画される。

14.2.4.2 StateMachine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* クラス図で StateMachine 再定義を描くときは、
  Classifier に対する既定の矩形表記法を用いることができ、
  キーワード «statemachine» が StateMachine の名前の上または前にある。

* StateMachine とその ``context`` Classifier または BehavioralFeatures の
  間の関連には特別な図表的表現がない。

14.2.4.3 Region
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Regions を有する合成 State や StateMachine は、
  破線を引いて全体を Regions に分割するような描き方をする。

* Figure 14.3 Notation for a composite State with Regions

  * Regions がふたつある合成 State を示す。

14.2.4.4 表題不明
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* 一個だけ Region を有する合成 State や StateMachine は、
  グラフ Region で入れ子になった状態図を見せることで示される。

14.2.4.5 State
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Figure 14.4 State notation

  * State は名前が内部に示されている角の丸い矩形として示す。

* Figure 14.5 State with a name tab

  * あるいは名前タブを取り付けてよい。
  * 名前タブは矩形であり、普通は State の上辺外側に安置されて、
    その State の名前を含む。
    これは普通は直交 Regions のある合成 State の名前を持つのに用いられるが、
    他の場合でも用いて構わない。

* Figure 14.6 State with compartments

  * State を水平線で区切って複数区画に分割してよい。
  * 区画の構成は次のようになる。

    名前区画
      この区画では State の名前（オプション）を文字列として保持する。
      部分機械 State の場合は、参照される StateMachine の名前を
      State の名前の後にコロンが続く文字列として示す。

    内部 Behaviors 区画
      この区画では State に付随する内部 Behaviors のリストを保持する。
      書式説明省略。

    内部 Transitions 区画
      この区画では **internal** Transitions のリストを含む。
      書式説明省略。

    分解区画
      合成 State のみこの区画を使える。次の節参照。

代わりに、テキストの挙動式の代わりに、
State または **internal** Transition に付随するさまざまな Behaviors を
適切な図表上の表現を使って別々の図式に表すことができる。

14.2.4.5.1 Composite State
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* 分解区画では Regions, States, Transition に関してその合成構造がわかる。

* 合成 State の分解を非表示にすることが便利な場合がある。

* ここでの「非表示」とは純粋に図表上の便宜の事柄であって、
  アクセス制限に関しての意味はない。

* 合成 State には
  ひとつまたはそれを超える ``entry`` 点と ``exit`` 点が、
  境界の外側にあるか、
  その境界の十分近いところ（内でも外でも可）にあってよい。

* Figure 14.7 Composite State with two States

  * Dialing は Start と Partial Dial のふたつの States を含む合成 State である。

* Figure 14.8 Composite State with a hidden decomposition indicator icon

  * 合成 State の分解を非表示にすることは便利である。
  * 非表示であることを、メガネのようなシンボルを State 内の右下に記すことで示す。

* Figure 14.9 Composite State with Regions

  * 状態 Studying は 3 個の Regions からなる。

* Figure 14.10 Composite State with two Regions and entry, exit, and do Behaviors

  * entry: この状態 (LightOn) に入場する際に履行される Behavior (``entry``) である。
  * do: この状態にある間中履行される Behavior (``doActivity``) である。
  * exit: この状態から退場する際に履行される Behavior (``exit``) である。
  * 文書中に記述がないのでこれは憶測になるが、
    左の Region がメインの照明、右の Region がサブの照明を示している。

14.2.4.5.2 Submachine State
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* 部分機械 State は通常の State として描かれる。

* 部分機械 State 記号はひとつまたはそれを超える ``entry`` 点への参照と、
  ひとつまたはそれを超える ``exit`` 点への参照とを含んでよい。

* 部分機械 StateMachine が既定の **initial** Pseudostate を通って入場されるか、
  部分機械の完了の結果として退場されるならば、
  入場点と退場点の表記法を使う必要はない。

* 同じ部分機械を発動する部分機械 States は、
  入場点と退場点が異なる Transitions の部分となっている
  同じ状態図に複数回現れてよい。

* Figure 14.11 Submachine State example

  * 部分機械 State (FailureSumbachine) が参照される
    StateMachine 図のある断片である。

  * Event "error1" がきっかけとなる Transition は FailureSumbachine の
    入場点 "sub1" にて停止するはずである。
    Transition "error3" は FailureSumbachine の既定の Transition を取る含みがある。

  * 部分機械の退場点 "subEnd" から始まる Transition は、
    StateMachine HandleFailure で実行されるものばかりでなく、
    Behavior "fixed1" を実行するはずである。

  * State の名前で StateMachine に対する参照がないかもしれないということを除き、
    同じ表記法を合成 States に対して適用するだろう。

* Figure 14.12 StateMachine with an exit point as part of the StateMachine graph

  * ふたつの退場点が定義された StateMachine の見本。

* Figure 14.13 StateMachine with an exit point on the border

  * 同じ StateMachine を StateMachine の枠上に入場点・退場点を記して示す。

* Figure 14.14 Submachine Sate that uses an exit point

  * Figure 14.13 で示した StateMachine が部分機械 State で参照されており、
    State 記号上に退場点のある表現オプションを示す。

14.2.4.5.3 State list notation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* State リストは実際上時々起こるある状況に対して図表上の略記法を与える。

* これらは純粋に対応する抽象的構文表現がない表記法の形式である。

* 異なる States から始まる同じ Trigger 値を有する
  ``effect`` のない複数の Transitions で、すべてが

  * 単一の流出 Transition のある共通 **junction** Vertex を終点とするか、
  * 同じ終点 State で停止するか

  であるものは、始まりの States の名前の列記でラベルが付いた、
  State のような図表要素から始まる
  単一の Transition のような辺で表してよい。

* Figure 14.15 State list notation option

  * 両者の可能性があることがわかる。

* Figure 14.16 Diagram equivalent to Figure 14.15 without using statelists

  * 状態リストを用いることなしの同値の図。

14.2.4.6 FinalState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* FinalState は小さい黒丸を囲む丸で示す。

* Figure 14.17 FinalState notation

  * FinalState の見本である。合成 State 内部の States の最も右のもの。

14.2.4.7 Pseudostate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Figure 14.18 initial Pseudostate

  * **initial** Pseudostate は小さい黒丸を囲む丸で見せる。

* Figure 14.19 shallowHistory Pseudostate

  * **shallowHistory** Pseudostate は ``H`` を囲む小さい丸で見せる。

* Figure 14.20 deepHistory Pseudostate

  * **deepHistory** Pseudostate は ``H*`` を囲む小さい丸で見せる。

* Figure 14.21 entryPoint Pseudostate

  * 入場点 は StateMachine 図または合成状態の枠上に小さい丸で、
    関連する名前とともに見せる。

* Figure 14.22 exitPoint Pseudostate

  * 退場点は StateMachine 図または合成状態の枠上にバツの付いた小さい丸で、
    関連する名前とともに見せる。

* Figure 14.23 entryPoint and exitPoints on a composite State

  * 合成 States の入場点と退場点を描く場合の表記法を図解する。

* Figure 14.24 junction Pseudostate with incoming and outgoing Transitions

  * **junction** は黒丸で見せる。

* Figure 14.25 choice Pseudostates

  * **choice** Pseudostate はダイヤモンド形の記号で見せる。

* Figure 14.26 terminate Pseudostate

  * **terminate** Pseudostate はバツで見せる。

* Figure 14.27 fork and join Pseudostates

  * **fork** と **join** を表す表記法は太い棒である。

14.2.4.8 ConnectionPointReference
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Figure 14.28 Entry point ConnectionPointReference notation

  * 入場点に対する接続点参照は ``entry`` Pseudostate と同じ表記法である。

* Figure 14.29 Exit point ConnectionPointReference notation

  * 退場点に対する接続点参照は ``exit`` Pseudostate と同じ表記法である。

* Figure 14.30 Alternative entry point ConnectionPointReference notation

  * 代わりに、
    入場点に対する接続点参照は「括弧付きの余白」記号を使って見せることもできる。

  * テキスト ``(via <name>)`` を State へ至る Transition の矢印上に配置するというものである。

* Figure 14.31 Alternative exit point ConnectionPointReference notation

  * 退場点に対する接続点参照は「括弧付きの余白」記号を使って見せることもできる。

14.2.4.9 Transition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Transition を表す既定のテキスト表記法は BNF 式
  ``<trigger>``, ``<guard>``, ``<behavior-expression>`` により定義される。

  * ``<trigger>`` は Triggers を表す標準表記法である。
  * ``<guard>`` は ``guard`` を表す Boolean 式である。
  * ``<behavior-expression>`` はオプションで、
    何らかの言語で書かれた ``effect`` Behavior を指定する式である。

* 代替として、
  ``effect`` Behavior を Actions の配列に基づいた制御フローとして
  記述できるならば、
  Activities に対して使われる表記法と類似する、
  Transitions と複合遷移を表す図式的表現がある。

* この代替表記法は Activities を表すのに使われる表記法を
  思い起こさせる図表要素を含むものの、
  StateMachines に対してしか適用できない異なる形式であり、
  その要素は適当な StateMachine の概念に写像する。

* この表記法は有向グラフの形をしていて、
  制御フローを表す有向辺で相互接続された、
  ひとつまたはそれを超える図表記号からなる。

* Transition が **initial** Pseudostate から始まると、
  開始記号は初期記号であり、
  それは **initial** Pseudostate を表すのに使うものと同じである。
  つまり黒塗りの丸である。

* 経路を停止する終了記号を除いて、
  次の記号のどれもが適切に連鎖して現れることができる。

  * 行動記号
  * 選択点記号
  * Signal 送信記号
  * 合併記号

* これらの有向グラフにある停止記号はいつでも
  遷移の ``target`` State を表す State 似の記号か
  最終状態記号である。

14.2.4.9.1 Action symbols
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* 行動記号それぞれはオプションのテキストの行動仕様のある矩形で表す。

14.2.4.9.2 Signal receipt symbol
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* Signal 受信記号は独特な凹五角形で表現する。
  中には ``<trigger>`` や ``<guard>`` を用いたテキストが含まれる。

14.2.4.9.3 Signal send symbol
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* これは信号を送信する特別な行動を表し、
  対応する Transition の ``effect`` Behavior を記述する
  Activity の部分である
  SendSignalAction へ直接写像する。

  * Signal 送信シンボルの記法は SendSignalAction の記法に対応する。
    :doc:`./actions` 参照。

14.2.4.9.4 Choice point symbol
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* この記号は **choice** Pseudostate へ直接写像し、同じ記法を使う。
* どの Activity の部分でもない。

14.2.4.9.5 Merge symbol
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* 併合記号は複数の制御フロー辺を合流するのに使われて、
  **junction** Pseudostate へ直接写像し、
  同じ表記法を使う。
  どの Activity の部分でもない。

* Figure 14.32 Symbols for Signal reception, Sending, and Actions on a Transition

  * Idle からダイヤモンドの間

    * ``Req(id)`` が Signal 受信シンボル。
    * ダイヤモンドが選択点シンボル。

  * ダイヤモンドから黒丸の間（左右それぞれ）

    * ``Minor(id)`` たちが Signal 送信シンボル。
    * ``MinorReq := id;`` たちがアクションシンボル。

  * 黒丸から Busy の間

    * 黒丸はマージシンボル。

14.2.4.9.6 Deferred triggers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* 遅延可能な引き金は State の内側にリストし、
  スラッシュ記号とラベル ``defer`` を付けることで示す。

* Figure 14.33 Deferred Trigger notation

  * Initializing と Primed のどちらの状態にも ``request/defer`` とある。
    イベント ``request`` は Operational に到達するとすぐに処理される。

14.2.4.10 TransitionKind
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* 種類が **internal** の Transitions は図式中に明示的には見られない。

* 種類が **local** の Transitions は
  含む合成 State の境界、
  それの入場点のうちのひとつ、
  または合成 State にある Vertex から始まることができる。

* 種類が **external** の Transitions は
  ``source`` Vertex の内部に含まれる Vertex のいずれかか、
  外部にある Vertex のいずれかで終わることができる。

* Figure 14.34 Local Transitions

  * ここにある Transitions のすべてが **local** である。

* Figure 14.35 External Transitions

  * ここにある Transitions のすべてが **external** である。

14.2.5 Examples
----------------------------------------------------------------------
* Figure 14.36 StateMachine diagram representing a telephone

  * 簡単な電話のための StateMachine の図式。
  * Idle の右についている黒丸 (**initial** Pseudostate) と、
    大きい枠の左上外部にある白丸 (activeEntry) が入口候補。

  * FinalState に加えて、マルバツ印の aborted が出口候補。

14.3 StateMachine Redefinition
======================================================================

14.3.1 Summary
----------------------------------------------------------------------
* StateMachines は例えば一般化できる Classes のような Behavior の定義に用いる。
  Class の特殊化の一部として、
  それの Behavior の定義を特殊化することが必要とされてよい。
  これは
  再定義を用いる一般の Classifier の Behavior の拡張として、
  特殊化された Classifier の Behavior を定義することにより果たされる。

14.3.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 14.37 StateMachine redefinition

  * 現れているクラスはすべて前節ですでに述べられている。
  * ただし、Region, State, Transition の親クラスが
    RedefinableElement のみとなっていることが違う。
    以前見た Figure 14.1 では Namespace のみが親クラスとして示されていた。

A_extendedStateMachine_stateMachine, A_extendedRegion_region
  * StateMachine/Region から StateMachine/Region への関連（単方向）。
  * これがひとつの拡張であるような StateMachine/Region を参照。

A_redefinedState_state, A_redefinedTransition_transition
  * State/Transition から State/Transition への関連（単方向）。
  * これがその再定義であるような State/Transition を参照。

A_redefinitionContext_region, A_redefinitionContext_state, A_redefinitionContext_transition
  * Region/State/Transition から Classifier への関連（単方向）。
  * これが再定義されることが許容される ``context`` Classifier を参照。

14.3.3 Semantics
----------------------------------------------------------------------
14.3.3.1 StateMachine Extension
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* StateMachine は一般化可能。
  特殊化 StateMachine は 一般 StateMachine の拡張であり、

  * 新たな Regions, Vertices, Transitions を追加してよい。

  * Regions と States を再定義してよい。
    例えば、単純 States は合成 States として再定義することができ、
    それに対して合成 States は States と Transitions を追加することで
    再定義することができる。

  * Transitions を再定義してよい。

* これは Classifier の特殊化の一部としてなされる。すなわち、
  一般 Classifier により所有される StateMachine ``behaviors`` と
  ``classifierBehaviors`` は
  一般 Classifier の BehavioralFeatures のメソッドを指定する
  StateMachines として特殊化することができる。

* 特殊化 StateMachine には一般 StateMachine の要素が
  すべてあるはずであり、
  かつさらなる要素を含んでよい。

  * Regions を追加してよい。
    継承した Regions は拡張によって再定義してよい。つまり、
    States および Vertices を継承して、
    StateMachine の Regions の States と Transitions を再定義してよい。

14.3.3.1.1 State redefinition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* 単純 State を再定義（拡張）して、
  ひとつまたはそれを超える Regions による合成 State になるようにしてよい。
  合成 State は次のように再定義（拡張）できる。

  * 新しい Regions を追加する。

  * 継承した Regions に Vertices と Transitions を追加する。

  * もし一般 State に何もなければ、
    ``entry``/``exit``/``doActivity`` Behaviors を追加する。

  * States と Transitions を再定義する。

* State の再定義は StateMachine 全体に適用する。

* 部分機械 State も再定義してよい。
  部分機械 StateMachine は他の部分機械 StateMachine で置き換えてよく、
  ただし、再定義された部分機械 StateMachine と
  同じ入場点・退場点があるという条件が付く。
  とは言え、追加で入場点・退場点があることは許される。

* 一般 Classifiers が複数の場合は、拡張は、
  拡張 StateMachine が個別の新規 Region の他に、
  一般 Classifiers の StateMachines のそれぞれに対して
  直交 Regions を得ることを含意する。

14.3.3.1.2 Transition redefinition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* 拡張 StateMachine の Transition はその StateMachine 拡張で再定義してよい。
  Transitions はそれらの ``effect`` と ``target`` State を
  置き換えさせることができるが、
  その一方 ``source`` State と ``trigger`` はそのままである。

14.3.4 Notation
----------------------------------------------------------------------
* 一般 Classifier での StateMachine の拡張である StateMachine には、
  StateMachine の名前が関連するキーワード «extended» があるはずである。

  * 同様に、継承 Region が拡張されたか、
    State が拡張されたことを示すのに
    キーワード «extended» を要素の名前に追加される。

  * StateMachine 内の継承要素か Region か State は
    破線または軽い調子の線のどちらかで描かれる。

  * State が終端状態 (``isLeaf`` == true) ならば、
    State の名前に従う付加的なラベルを追加してよく、
    キーワード «final» が含まれる。

14.3.5 Examples
----------------------------------------------------------------------
* Figure 14.38 A general StateMachine

  * ATM StateMachine にある States
    VerifyCard, OutOfService, VerifyTransaction が
    **final** として指定されているが、
    それらが ATM の特殊化において再定義できないことを意味する。

    * 他の States はすべて再定義可能である。

  * 図式内下方にある Transition もまた **final** と指定されている。
    それの ``effect`` Behavior も ``target`` State も
    再定義できないことを意味する。

* Figure 14.39 An extended StateMachine

  * 上述の図式で示された StateMachine を特殊化したもの。

  * ATM StateMachine がある Class の特殊化である Class の StateMachine が
    State と Transition を追加することで合成 State を拡張することで
    定義されていて、
    利用者が希望額を記入できるようになっている。

  * さらに継承 State から始まり新規導入 State に至る
    Transition が追加されている。

    * 継承した状態は破線で描画されていることに注意。

* Figure 14.40 Adding Transitions

  * 特殊化 StateMachine に Transitions を追加する見本。

14.4 ProtocolStateMachines
======================================================================

14.4.1 Summary
----------------------------------------------------------------------
* ProtocolStateMachines は慣習規約を表現するのに用いられる。
  ProtocolStateMachines は
  関連した BehavioredClassifier の Behaviors が従う必要がある
  Event の出来事の合法な順序を表現する。

* StateMachine の記法は
  Classifier の挙動の特徴の発動の順序を定義するのに
  便利な手段である。

* ProtocolStateMachines は Classifiers, Interfaces, Ports に関連することが可能。

14.4.2 Abstract Syntax 
----------------------------------------------------------------------
* Figure 14.41 ProtocolStateMachines

  * 新クラスは ProtocolStateMachine, ProtocolConformance, ProtocolTransition のみ。
  * グラフが分離しているのが不思議。

A_conformance_specificMachine, A_generalMachine_protocolConformance
  * 前者は ProtocolStateMachine から ProtocolConformance への composite 関連（双方向）。
  * 後者は ProtocolConformance から ProtocolStateMachine への関連（単方向）。
  * 関連端 ``specificMachine``, ``generalMachine`` が 
    ``source``, ``target`` をそれぞれ subsets する。

A_referred_protocolTransition
  * ProtocolTransition から Operation への関連（単方向）。
  * Figure 14.42 の ``m1`` が ``preCondition`` に相当する。
  * 関連端 ``referred`` は readOnly である。

A_preCondition_protocolTransition
  * ProtocolTransition から Constraint への composite 関連（単方向）。
  * Figure 14.42 の ``C1`` が ``preCondition`` に相当する。

A_postCondition_owningTransition
  * ProtocolTransition から Constraint への composite 関連（単方向）。
  * A_guard_transition の ``guard`` と ``transition`` をそれぞれ subsets, redefines する関連。
  * Figure 14.42 の ``C2`` が ``preCondition`` に相当する。

14.4.3 Semantics
----------------------------------------------------------------------
14.4.3.1 ProtocolStateMachine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ProtocolStateMachine は Classifier の背景でいつでも定義される。

* ProtocolStateMachines は
  Classifier の BehavioralFeatures が発動される順序を定義するのに
  次のものを指定することによって役に立つ：

  * BehavioralFeatures が合法的に発動する挙動的背景（状態と事前条件）
  * 発動の合法的な順序
  * 発動の期待される成果（事後条件）

* ProtocolStateMachines は、
  その協力者たちに気づいてもらえるように、
  所有している Classifier の外観を提示する。

* ProtocolStateMachines は Classifier の挙動の "black box" な展望を
  与えるものなので、
  それらの States は内部の挙動的 StateMachines の States と
  必ずしも対応しなくてよい。

* ProtocolStateMachine の解釈は異なることがある。

  #. 宣言的 ProtocolStateMachines

     これは BehavioralFeatures の発動に対する合法的な Transitions を指定する。

  #. 実行可能 ProtocolStateMachines

     これはあるオブジェクトが
     受信かつ処理してよい Event 出来事のすべてを、
     これらがきっかけとなる Transitions と共に指定する。

* 両者の解釈に対する仕様は同じであり、
  唯一の違いは後者の解釈が規定する直接の動的な意味合いである。

* 複合 Transitions や、部分機械 StateMachines や、
  合成 States や、同時直交 Regions などの
  挙動的 StateMachines で出くわすモデリングの
  より洗練された形式は、
  ProtocolStateMachines をモデル化するのにも利用できる。

  * 例えば同時 Regions は
    オブジェクトにいくつかの活性 States が同時にあるような
    規約を表現することを可能にする。

  * 部分機械 StateMachines と複合遷移を
    複雑な ProtocolStateMachines の「因数分解」に
    用いることができる。

* Classifier には ProtocolStateMachines がいくつかあってよい。

* ProtocolStateMachines の States はそれらの状況 Classifiers の利用者に晒される。

  * Classifier のオブジェクトが BehavioralFeature の発動のどれをも処理していないと、
    このオブジェクトの利用者はいつでもそれの状態配置を知ることができる。

* ProtocolStateMachine の State には
  ``entry``/``exit``/``doActivity`` Behaviors を定義できない。

14.4.3.2 ProtocolTransition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ProtocolTransition はその背景にある Classifier の
  BehavioralFeature の発動について合法的な Transition を指定する。

* ProtocolTransitions には事前条件、撃鉄、事後条件がある。

* ProtocolTransition は次のことを指定する。

  * 付随する（参照される）特徴が
    状況 Classifier のオブジェクトで
    発動されるのが可能である。

  * Transition の完了にあたり、
    そのオブジェクトが事後条件が成り立つ ``target`` State にいるはずである。

* ProtocolTransitions には付随する ``effect`` Behavior がない。
  BehavioralFeature の発動の結果として実行される
  ProtocolTransition の結果は言外である。
  つまり、
  発動された BehavioralFeature に対応するメソッドの実行である。

14.4.3.2.1 Unexpected trigger reception
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* 現在の State に対する合法的な引き金に一致しない Event 出来事の
  受領の解釈、状態不変、または事前条件は定義されない。
  （例えば、それを無視、拒絶、または遅延できる、
  または例外を送出できる、
  あるいは適用はエラーで停止できる）

14.4.3.2.2 Unexpected Behavior
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* 予期しない Behavior の解釈、つまり
  Transition の予期しない結果
  （誤った FinalState, FinalState 不変性、事後条件）
  もまた定義されない。
  これを ProtocolStateMachine の実装の誤りとして解釈するべきである。

14.4.3.2.3 Equivalences to pre- and post-conditions of operations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* ProtocolTransition は
  付随する操作の事前条件と事後条件の言葉で意味上は解釈できる。

* Figure 14.42 An example of a ProtocolTransition (...)

  * ``[C1]m1/[c2]`` の読み方を習得すること。
    状態 S1 において条件 C1 が成立しているときに操作 m1 が呼びだされ、
    状態 S2 に到達したときには条件 C2 が成立している。

* Figure 14.43 Example of several ProtocolTransitions (...)

  * 上記例題の複数版。単に操作 m1 が共通していることに注意すれば十分。

* ProtocolStateMachine はその Transitions により参照される
  BehavioralFeature それぞれに対する合法的な ProtocolTransition すべてを
  指定する。

* BehavioralFeature が ProtocolTransition のどれからも参照されていなければ、
  ProtocolStateMachine の State のどれに対しても操作を呼び出すことができ、
  その操作は現在の State や事前条件、事後条件を変更しないはずである。

14.4.3.2.4 Using other types of Events in ProtocolStateMachines
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* BehavioralFeatures の発動の他に、
  ProtocolStateMachines の挙動を表現するために
  他の Events を用いてもよい。

14.4.3.3 ProtocolConformance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ProtocolStateMachines はより特殊な ProtocolStateMachines へ改良することができる。
  ProtocolConformance は、
  特殊 ProtocolStateMachine が
  一般 ProtocolStateMachine によって指定された規約に
  準拠する規約を指定することを宣言する。

* ProtocolStateMachine は Classifier が所有する。
  一般版 StateMachine 所有者である Classifiers と
  付随する特殊版 StateMachine とを、
  Generalization または Realization が一般には接続する。

* ProtocolConformance は
  一般版 ProtocolStateMachine に対する規則と制約のどれもが
  特殊版 ProtocolStateMachine に対して適用する
  という宣言を表す。

14.4.4 Notation
----------------------------------------------------------------------
この節は Examples も兼ねているようだ。

14.4.4.1 ProtocolStateMachine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ProtocolStateMachine を表す表記法は
  挙動の StateMachines についてのそれとたいへん似ている。
  StateMachine の名前の近くに置かれたキーワード «protocol» が
  ProtocolStateMachine 図を図表的に差別化する。

* Figure 14.44 ProtocolStateMachine example

  * 戸外が無人になれば扉は閉められる。

* Figure 14.45 Notation for a State with an invariant

  * ProtocolStateMachine の State に付随するテキストの不変式は、
    その State の名前の後ろまたは下に配置することで表され、
    角括弧で括られる。

14.4.4.2 ProtocolTransition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* 通常の StateMachine 表記法が適用する。
  違いは ProtocolTransitions について ``effect`` Behaviors が
  指定されていないことと、事後条件が存在できることである。

* Figure 14.46 ProtocolTransition notation

  * スラッシュの後にガード条件と同じ記法で事後条件を記すことがある。

14.5 Classifier Descriptions
======================================================================
機械生成による節。

14.6 Association Descriptions
======================================================================
機械生成による節。

.. include:: /_include/uml-refs.txt
