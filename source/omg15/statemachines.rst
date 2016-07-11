======================================================================
14 StateMachines
======================================================================
UML 2.5 pp. 303-370 に関するノート。

.. todo:: 最低でもあと一回は編集する。

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
  * 対応する BehavioredClassifier を持たない Behavior
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
    これらの振る舞いの定義はオプションである。

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
  * 関連端 ``effect`` はこの Transition が発火するときに実施される振る舞い。
    多重度が ``0..1`` なのでオプション。

A_guard_transition
  * Transition から Constraint への composite 関連（単方向）。
  * ガード条件を表す。この ``guard`` が真になれば
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

* 合成 State が Regions を複数持つ直交 State でもあると、
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
  * 部分機械 State を起点とするグループ Transition のきっかけ
  * その出口点のどれかを経て

* FinalState を経て退場するのと、
  グループ Transition によって退場するのは、
  普通の合成 States の場合は同じ意味を持つ

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
Transition
  * Namespace の一種。
  * Transition とは、単一の source Vertex を始点とし、
    単一の target Vertex を終点とする単方向リンクである。

  * Transitions はより複雑な複合遷移の一部として実行される。

  * 実行の途中において、Transition オブジェクトは次のどれかであると言う。

    * reached: StateMachine 実行が source Vertex に到達したときに。
    * traversed: それが目下実行されているとき。
    * completed: それが target Vertex 到達した後で。

  * Transition は Triggers の集合を所有してよい。

14.2.3.8.1 Transition kinds relative to source
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* Transition の意味はその source Vertex との関係に依存して決まる。
  Transition::kind の値が定義する。取り得る値は以下の 3 通り。

  * external: その Transition はその source から退場する、の意。
  * local: その Transition はそれを含む State から退場しない、の意。
  * internal: その Transition は自己遷移をする、の意。

14.2.3.8.2 High-level (group) Transitions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* 合成 States を source とする Transitions は
  high-level または group Transitions と呼ばれる。

* Transition には guard という Constraint が関連していてよい。

  * 偽に評価される guard を持つ Transitions は使用無効である。
  * 評価されるタイミングは、それを含む複合 Transition が利用可能になる前である。
  * 関連する guard がない Transition は、
    あたかもそれが常に真に評価される guard を持つかのように取り扱われる。

14.2.3.8.3 Completion Transitions and completion events
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

14.2.3.8.4 Compound transitions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* Event の出来事が利用可能な Transition の引き金となるか、
  または StateMachine の実行が生成したときには、
  ある stable state configuration に至るまでの間、
  接続されて入れ子になった Transitions と Vertices の集合の横断 (traversal) が新しく始まることがある。
  一般の場合に、この横断の軌跡は複合遷移 (compound transition) として知られる。

  * 複合遷移は非循環有向グラフである。
  * このグラフの root (source) は次のうちのひとつであることがある。

    * ひとつ以上の Triggers が定義された状態の Transition
    * 完了 Transition
    * ある共通の join Pseudostate 上に集まる、
      相異なる直交 Regions から始まる Transitions の集合
    * 最上位 Region の initial Pseudostate から始まる Transition

  * and more

14.2.3.8.5 Transition ownership
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* Transition の所有者は明示的に制限されていない。
  含まれている Region は直接間接を問わずその StateMachine が必ず所有するものではあるが。

  * 提案される所有者は、
    その source と vertex の両方を含む Region のうち最も内側のものである。

14.2.3.9 Event Processing for StateMachines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. todo:: Event Processing for StateMachines

14.2.4 Notation
----------------------------------------------------------------------
StateMachine 図はある StateMachine を表現するグラフである。
States および Vertices は適当なシンボルで描画される。
Transitions はそれらのシンボルを結ぶ有向辺で普通は描画される。

StateMachine
  * デフォルトの Classifier 向けの矩形記法が利用可能。
  * キーワード ``«statemachine»`` を StateMachine の名前の前または上に置く。

Region
  * Regions を有する合成 State や StateMachine は、
    破線を引いて全体を Regions に分割するような描き方をする。

  * 一個だけ Region を持つものは、そのグラフ Region 内部の
    入れ子になった状態図を見せることで示される。

  * Figure 14.3 Notation for a composite State with Regions を参考にするとよい。

State
  * 状態名を内部に示した、角の丸い矩形で示す。
  * あるいは矩形形状のタブをつけ、そこに State の名前を示す。
    このスタイルは普通は合成 State の名前を出すのに用いられるが、
    他の場合で用いても構わない。

  * State を水平線で区切って複数区画に分割してよい。
    区画の構成は次のようになる。

    * name
    * internal Behaviors
    * internal Transitions
    * decomposition

  * 合成 State

    * 合成 State はひとつ以上の entry/exitPoints をその状態の枠の外側
      もしくは枠の十分近いところ（内でも外でも可）に記してよい。

    * Figure 14.7 Composite State with two States

      * Dialing は Start と Partial Dial のふたつの States を含む合成 State である。

    * Figure 14.8 Composite State with a hidden decomposition indicator icon

      * 合成 State の分解を非表示にすることは便利である。
      * 非表示であることを、メガネのようなシンボルを State 内の右下に記すことで示す。

    * Figure 14.9 Composite State with Regions

      * 状態 Studying は 3 個の Regions からなる。

    * Figure 14.10 Composite State with two Regions and entry, exit, and do Behaviors

      * entry: この状態 (LightOn) に入場する際に履行される Behavior (entry) である。
      * do: この状態にある間中履行される Behavior (doActivity) である。
      * exit: この状態から退場する際に履行される Behavior (exit) である。
      * 文書中に記述がないのでこれは憶測になるが、
        左の Region がメインの照明、右の Region がサブの照明を示している。

FinalState
  * 小さい黒丸を囲む丸で示す。
  * Figure 14.17 FinalState notation 参照。

PseudostateState
  * 見本となる図は Figure 14.18 から Figure 14.27 まで。
    PseudostateKind によって描画法が異なる。

  * initial は黒丸で示す。
  * shallowHistory は ``H`` を丸で囲む。
  * deepHistory は ``H*`` を丸で囲む。
  * entryPoint はStateMachine 図等の枠上に小さい丸として関連する名前とともに示す。
  * exitPoint はバツを丸で囲むシンボルと関連する名前とともに、
    entryPoint と同様にして示す。
  * junction は黒丸で示す。
  * choice はダイヤモンドで示す。
  * terminate はバツで示す。
  * fork と join は共に太い棒として示す。
    棒に接続している Transitions の出入り状況で両者を区別すればよい。

ConnectionPointReference
  * 見本となる図は Figure 14.28 から Figure 14.31 まで。
  * Pseudostate の entryPoint と exitPoint の記法と同じになるが、
    シンボルは対象の State または submachine State の枠上に配置する。
  * 代替記法があり、丸ベースのシンボルを用いずに、
    テキスト ``(via <name>)`` を State へ至る Transition の矢印上に配置するというものである。

Transition
  * テキストによる記法では
    ``<trigger>``, ``<guard>``, ``<behavior-expression>`` が使える。

  * アクションシンボルは矩形で表現する。アクションのテキストでの仕様をつけてよい。

  * Signal 受信シンボルは独特な凹五角形で表現する。
    中には ``<trigger>`` や ``<guard>`` を用いたテキストが含まれる。

  * Signal 送信シンボルの記法は SendSignalAction の記法に対応する。
    :doc:`./actions` 参照。

  * 選択点シンボルは choice Pseudostate と同じ記法を使う。

  * マージシンボルは junction Pseudostate と同じ記法を使う。

  * Figure 14.32 Symbols for Signal reception, Sending, and Actions on a Transition

    * Idle からダイヤモンドの間

      * ``Req(id)`` が Signal 受信シンボル。
      * ダイヤモンドが選択点シンボル。

    * ダイヤモンドから黒丸の間（左右それぞれ）

      * ``Minor(id)`` たちが Signal 送信シンボル。
      * ``MinorReq := id;`` たちがアクションシンボル。

    * 黒丸から Busy の間

      * 黒丸はマージシンボル。

  * 遅延可能トリガーは State の内側にリストし、
    スラッシュ記号とラベル ``defer`` を付けることで示す。

  * Figure 14.33 Deferred Trigger notation

    * Initializing と Primed のどちらの状態にも ``request/defer`` とある。
      イベント ``request`` は Operational に到達するとすぐに処理される。

14.2.5 Examples
----------------------------------------------------------------------
* Figure 14.36 StateMachine diagram representing a telephone

  * 簡単な電話のための StateMachine の図式。
  * Idle の右についている黒丸 (initial Pseudostate) と、
    大きい枠の左上外部にある白丸 (activeEntry) が入口候補。

  * FinalState に加えて、マルバツ印の aborted が出口候補。

14.3 StateMachine Redefinition
======================================================================

14.3.1 Summary
----------------------------------------------------------------------
* StateMachines は Behavior の定義に用いる。
* Class の特殊化の一部として、
  それの Behavior の定義を特殊化する必要があることがある。
  特殊化された Behavior の定義は「再定義」を用いて達成する。

14.3.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 14.37 StateMachine redefinition

  * 現れているクラスはすべて前節ですでに述べられている。
  * ただし、Region, State, Transition の親クラスが
    RedefinableElement のみとなっていることが違う。
    以前見た Figure 14.1 では Namespace のみが親クラスとして示されていた。

14.3.3 Semantics
----------------------------------------------------------------------
.. 14.3.3.1 StateMachine Extension

* StateMachine は一般化可能。
  特殊化 StateMachine は 一般化 StateMachine のひとつの拡張である。

  * 新たな Regions, Vertices, Transitions を追加してよい。
  * Regions と States を再定義してよい。
  * Transitions を再定義してよい。

* これは Classifier の特殊化の一部としてなされる。

* 特殊化 StateMachine はその一般化 StateMachine のすべての要素を持つだろう、
  なおかつさらなる要素を含んでよい。

* Regions を追加してよい。
  継承した Regions は拡張によって再定義される。

  * States と Vertices を継承して、
    そして StateMachine の Regions の States と Transitions を再定義してよい。

.. 14.3.3.1.1 State redefinition

* 簡単な State をひとつ以上の Regions による合成 State になるように再定義（拡張）してよい。
* 合成 State は次のように再定義（拡張）できる。

  * 新しい Regions を追加する。
  * 継承した Regions に Vertices と Transitions を追加する。
  * もし一般化 State が何も持っていなければ、
    entry/exit/doActivity Behaviors を追加する。
  * States と Transitions を再定義する。

* State の再定義は StateMachine 全体に適用する。

* submachine State もまた再定義してよい。
  再定義された submachine StateMachine と同じ entryPoints/exitPoints を持つという条件の下で、
  submachine StateMachine は他の submachine StateMachine で置き換えてよい。

* 複数の一般化 Classifiers の場合には、拡張は次のことを含意する。
  その拡張 StateMachine は、
  別個の新規 Region に加えて、一般化 Classifiers の StateMachines のそれぞれを
  直交 Regions にする。

.. 14.3.3.1.2 Transition redefinition

* 拡張 StateMachine の Transition はその拡張の中で再定義してよい。
* Transitions はそれらの effect と target State を置き換えさせることができ、
  一方 source と trigger State はそのまま保たれる。

A_extendedStateMachine_stateMachine, A_extendedRegion_region
  * StateMachine/Region から StateMachine/Region への関連（単方向）。
  * これがひとつの拡張であるような StateMachine/Region を参照。

A_redefinedState_state, A_redefinedTransition_transition
  * State/Transition から State/Transition への関連（単方向）。
  * これがその再定義であるような State/Transition を参照。

A_redefinitionContext_region, A_redefinitionContext_state, A_redefinitionContext_transition
  * Region/State/Transition から Classifier への関連（単方向）。
  * これが再定義されることが許容される context Classifier を参照。

14.3.4 Notation
----------------------------------------------------------------------
* 一般 Classifier 中の StateMachine の拡張である StateMachine は、
  その StateMachine の名前に関連してキーワード ``«extended»`` を持つだろう。

* 同様に、継承した Region が拡張されたか、
  State が拡張されたことを示すのに
  キーワード ``«extended»`` を要素の名前に続けて記す。

* StateMachine 内の継承した要素、Region または State は
  破線または軽い調子の線のどちらかで描かれる。

* State が終端状態 (a leaf state) ならば、
  State の名前に続いてラベル ``«final»`` を追加してよい。

14.3.5 Examples
----------------------------------------------------------------------
この例題は理解しやすい。

* Figure 14.38 A general StateMachine

  * VerifyCard, OutOfService, VerifyTransaction の各 State が
    final として指定されている。
    これらは再定義不可能。

    * その他の States は再定義可能である。

  * 図式内下方にある Transaction もまた final と指定されている。
    それの effect Behavior と target State は再定義不可能。

* Figure 14.39 An extended StateMachine

  * 上述の図式で示された StateMachine を特殊化したもの。

  * 利用者が所望の金額を入力できるように、合成状態 ReadAmount を拡張する。
    状態 EnterAmount とひとつの Transition を追加することによって定義する。

    * 継承した状態は破線で描画されていることに注意。

  * その上さらに、
    継承した状態 VerifyTransaction から
    新しく導入した状態 ReadAmount::EnterAmount に遷移するような
    Transition を追加する。

* Figure 14.40 Adding Transitions

  * 特殊化 StateMachine に Transitions を追加する見本。

14.4 ProtocolStateMachines
======================================================================

14.4.1 Summary
----------------------------------------------------------------------
* ProtocolStateMachines は慣習協定 (usage protocols) を表現するのに用いられる。

* ProtocolStateMachines は
  ある関連した BehavioredClassifier の Behavior が適合する必要がある
  Event の出来事 (pl.) の合法な順序を表現する。

* Classifier の振る舞いに関する機能 (pl.) の発動順序を定義するのには、
  StateMachine の記法は便利な方法である。

* ProtocolStateMachines は Classifiers, Interfaces, Ports に関連することが可能。

14.4.2 Abstract Syntax 
----------------------------------------------------------------------
* Figure 14.41 ProtocolStateMachines

  * 新クラスは ProtocolStateMachine, ProtocolConformance, ProtocolTransition のみ。
  * グラフが分離しているのが不思議。

14.4.3 Semantics
----------------------------------------------------------------------
ProtocolStateMachine
  * StateMachine の一種。
  * ProtocolStateMachine はいつでもある Classifier を背景に定義される。
  * その Classifier のオブジェクトの lifecycle のとある仕様は外界の立場が定義する。

  * 次のものを指定することによって
    Classifier の BehavioralFeatures がどの順番で発動するのかを定義するには
    ProtocolStateMachines が役に立つ。

    * BehavioralFeatures が正当に発動する behavioral context
    * 発動の正当な順序
    * 発動の期待される成果

  * ProtocolStateMachines は、
    その協力者たちが認める (perceive) ように
    所有している Classifier の外観を提示する。

  * ProtocolStateMachines は Classifier の振る舞いの black box な展望を与えるものなので、
    それらの States は内部の behavioral StateMachines の States と必ずしも対応しなくてよい。

  * ProtocolStateMachine の解釈は異なることがある。

    #. 宣言的 ProtocolStateMachines
    #. 実行可能 ProtocolStateMachines

  * 振る舞いに関する StateMachines で遭遇した、
    複合 Transitions や合成 States 等のより精巧なモデリング形式は
    ProtocolStateMachines をモデル化するのにも利用可能である。
    例えば concurrent Regions は
    オブジェクトがいくつかの active States を同時に持つような
    通信手順を表現することを可能にする。

  * 複雑な ProtocolStateMachines を「因数分解」するのに
    submachine StateMachines と複合遷移が用いられることがある。

  * Classifier はいくつかの ProtocolStateMachines を持ってよい。

  * ProtocolStateMachines の States はそれらの context Classifiers の利用者に晒される。
  * その Classifier のオブジェクトがどんな BehavioralFeature 発動も処理していないときには、
    このオブジェクトの利用者はいつでもそれの状態構成を知ることができる。
  * ProtocolStateMachine の State は entry/exit/doActivity Behaviors を定義できない。

ProtocolTransition
  * Transition の一種。
  * ProtocolTransition はその背景にある Classifier の
    ある BehavioralFeature の発動に関しての
    法的な Transition を指定する。

  * ProtocolTransitions は事前条件、撃鉄、事後条件を持つ。

  * ProtocolTransition は次のことを指定する。

    * 操作 referred が Classifier のオブジェクトを背景に発動されることが可能であること。
    * その Transition の完了にあたり、
      そのオブジェクトは事後条件が満たされている target State となるものであること。

  * ProtocolTransitions は関連する effect Behavior を持たない。
    ある BehavioralFeature 発動の結果として実行される
    ProtocolTransition の結果は言外である。

  * Figure 14.42 An example of a ProtocolTransition (...)

    * ``[C1]m1/[c2]`` の読み方を習得すること。
      状態 S1 において条件 C1 が成立しているときに操作 m1 が呼びだされ、
      状態 S2 に到達したときには条件 C2 が成立している。

  * Figure 14.43 Example of several ProtocolTransitions (...)

    * 上記例題の複数版。単に操作 m1 が共通していることに注意すれば十分。

ProtocolConformance
  * DirectedRelationship の一種（図から漏れている）。

  * ProtocolStateMachines はより独特なものへ改良することができる。
    ProtocolConformance は
    一般版 ProtocolStateMachine 用に指定された各規則と制約が
    改良版 ProtocolStateMachine に適用するという宣言を表現する。

  * ProtocolStateMachine は Classifier が所有する。
    ある一般版 StateMachine 所有者である Classifiers と
    ある関連した独自の StateMachine とは、
    通常は Generalization または Realization が接続する。

A_conformance_specificMachine, A_generalMachine_protocolConformance
  * 前者は ProtocolStateMachine から ProtocolConformance への composite 関連（双方向）。
  * 後者は ProtocolConformance から ProtocolStateMachine への関連（単方向）。
  * 関連端 specificMachine, generalMachine が source, target をそれぞれ subsets する。

A_referred_protocolTransition
  * ProtocolTransition から Operation への関連（単方向）。
  * 先ほどの見本中の ``m1`` が preCondition に相当する。
  * 関連端 referred は readOnly である。

A_preCondition_protocolTransition
  * ProtocolTransition から Constraint への composite 関連（単方向）。
  * 先ほどの見本中の ``C1`` が preCondition に相当する。

A_postCondition_owningTransition
  * ProtocolTransition から Constraint への composite 関連（単方向）。
  * A_guard_transition の guard と transition をそれぞれ subsets, redefines する関連。
  * 先ほどの見本中の ``C2`` が preCondition に相当する。

14.4.4 Notation
----------------------------------------------------------------------
この節は Examples も兼ねているようだ。

* Figure 14.44 ProtocolStateMachine example

  * 振る舞いに関する StateMachines の記法とたいへん似ている。
  * 図式名の右にキーワード ``«protocol»`` を置く。
  * 戸外が無人になれば扉は閉められる。

* Figure 14.45 Notation for a State with an invariant

  * State 名の右または下に角括弧で不変条件を明記することもできる。

* Figure 14.46 ProtocolTransition notation

  * effect のない Transition として記す。
  * スラッシュの後にガード条件と同じ記法で事後条件を記すことがある。

14.5 Classifier Descriptions
======================================================================
機械生成による節。

14.6 Association Descriptions
======================================================================
機械生成による節。

.. include:: /_include/uml-refs.txt
