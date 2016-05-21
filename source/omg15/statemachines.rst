======================================================================
14 StateMachines
======================================================================
UML 2.5 pp. 303-370 に関するノート。

.. todo::

   訳語検討。

   * enter (v.) 入場する。
   * exit (v.) 退場する。

   * protocol (n.) 通信手順。
     辞書には儀礼とか典礼ともあり、むしろここではこれらが相応しい？

   * submachine (n.) そのまま綴る。意味は本文でじっくり解説する通り。

   * trigger (n.) 普通はカタカナで「トリガー」とするのが一般的だが、
     実験的に「引き金」や、もっと踏み込んで「撃鉄」なども採用する。

.. contents:: ノート目次

14.1 Summary
======================================================================
* 有限状態機械の形式論を用いて、
  離散的なイベント駆動の Behaviors をモデリングするのに用いられる概念の集合を定義する。

* あるシステムの部分の Behavior を表現することに加えて、
  妥当な相互作用の連続するもの（プロトコルと呼ばれる）を表現するのにも用いられる。

* これらの二種類はそれぞれ behavior state machines と protocol state machines と呼ばれる。

* UML で用いられる有限状態機械の特有な表現形式は、
  David Harel の statecharts 形式論のオブジェクト指向な変種に基づく。

14.2 Behavior StateMachines
======================================================================

14.2.1 Summary
----------------------------------------------------------------------
* Behavior StateMachines を次のものを明確に記述することに用いることが可能だ。

  * 能動的な Class の classifierBehavior
  * BehavioredClassifier の classifierBehavior ではない ownedBehavior
  * 該当する BehavioredClassifier を持たない Behavior
  * BehaviorFeature に対応するメソッド（つまり Operation か Reception のこと）

14.2.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 14.1 Behavior StateMachines

  * まさに機械の名に相応しい図式である。
    あまりに関連が多いため、一部コネクターが交差してしまっている。

  * 新登場クラスが
    StateMachine, Region, Vertex, Transition,
    Pseudostate, ConnectionPointReference, State, FinalState
    と、とにかく多い。

14.2.3 Semantics
----------------------------------------------------------------------

StateMachine
  * Behavior の一種。
  * ひとつ以上の Regions を構成する。
  * StateMachine の実行は適切な Event の出来事が誘発する。

  * もし StateMachine が BehavioredClassifier の一種の context があるならば、
    その Classifier はどの Signal と CallEvent の Triggers が
    StateMachine にとって適用可能なのかを定義する。

    * 反対に StateMachine がスタンダロンな Behavior であれば、
      それの Triggers は何らかの Classifier のどんな Receptions や Operations にも
      つながっている必要はない。

  * StateMachine がある BehavioralFeature の method を指定する情況では、
    その StateMachine の Parameters はその BehavioralFeature のそれに
    match するものとする。

  * 定義から、StateMachine の実行の発動は triggered effects に帰着する。
    それゆえ、そのような実行に結び付くイベントプールがある。
    そのプールは

    * StateMachine の context Classifier オブジェクトか、
    * その StateMachine がある BehavioralFeature の method を定義するものであれば、
      その BehavioralFeature を所有している Classifier のオブジェクトに所属する。

  * そのイベント駆動型という性質のため、
    StateMachine の実行は in transit か in state のどちらかであり、
    両者を行ったり来たりする。

Region
  * Namespace の一種。
  * Region はそれの直交する Regions を用いて同時に (concurrently) 実行してもよい、
    ある振る舞いの断片を記述する。

    * Regions が互いに直交するの意味は、次のどちらか一方を意味する。

      * 同一の State が Regions を所有する。
      * 最上位において同一の StateMachine が Regions を所有する。

  * Region は Vertices と Transitions の集合で構成されているグラフを含む。
  * Region には自身の FinalState はもちろん、自身の initial Pseudostate もあってよい。

  * もし暗に Region に入るならば、その Region の default activation が起こる。
  * 反対に Region が含む Vertices のひとつにおいて終了となる
    ある Transition から Region に入るときには explicit activation が起こる。

Vertex
  * NamedElement の一種。
  * StateMachine グラフの各ノード型のための抽象クラスである。
  * Vertex はどんな個数の Transitions の source and/or target であり得る（例外アリ）。

  State
    * Namespace の一種。
    * State とはある StateMachine Behavior の実行におけるひとつの情況をモデル化するものである。
    * stable

    * State には次の 3 種類の特徴があり、
      それぞれブーリアン型属性でわかる。

      * simple State (isSimple): 内部に Vertices も Transitions もない。
      * composite State (isComposite): 少なくともひとつの Region を含む。

        * substate: composite State の Region 内部に囲まれた State をそう呼ぶ。
        * direct substate: その他のどの State 内にもない substate をそう呼ぶ。
        * indirect substate: direct でない substate をそう呼ぶ。

      * submachine State (isSubmachineState): 入れ子になった StateMachine を参照する。

    * States の複雑な階層は State または StateMachine の state configuration と呼ばれる。

      * 実行中のある一時点での state configuration は active state configuration と呼ばれる。
      * ある State が active であるとは、それが active state configuration の部分であることを指す。
      * ある state configuration が stable であるとは、

        * その state configuration からそれ以上遷移可能な Transitions がなく、
        * すべての entry Behaviors が（もしあれば）完了したことを言う。

    * State に entry, exit, doActivity という Behavior にそれぞれひとつ関連づけてよい。

      * entry: 外部の Transition を通じてその State に入場するときにいつでも実行される。
      * exit: その State を退場するときにいつでも実行される。
      * doActivity: この仕様は少々複雑なので注意。

    .. todo::

       * histories: 動作記録を表現する Pseudostate が二種類ある。
       * entering: 思いのほか複雑な意味がある。
       * exiting: これも。

    * Submachines は単一の StateMachine 仕様を複数回再利用可能にする方法である。

      * プログラミング言語におけるマクロのように、相異なる Behavior の仕様である。
        State::isSubmachineState はこれを達成する属性である。

      * ひとつの submachine State は該当する submachine StateMachine の
        仕様のマクロ的な付け加えを含意する。ある合成 State と意味としては等価である。

    FinalState
      * State の一種。
      * FinalState は包囲している Region が完了したことを知らせる特別な種類の State である。
      * FinalState へ連絡する Transition はその FinalState を含んでいる
        Region の振る舞い (pl.) の完了を表現する。

  ConnectionPointReference
    * Vertex の一種。
    * ConnectionPointReference は
      ある submachine State が参照する StateMachine が定義する
      entry/exit 点の使用 (usage) を表現するものである。

    * Transitions の sources/targets として利用されることが可能である。
      それらは submachine State が参照する submachine StateMachine に対する出入りを表現する。

    * transitive

  Pseudostate
    * Vertex の一種。
    * Pseudostate とは StateMachine グラフ内の
      transient Vertices の種々の型を取り囲む抽象的概念である。
      Pseudostates は通常、複数の Transitions をより複雑な
      複合遷移 (compound transitions) となるように連鎖させるのに用いる。

    * Pseudostate の意味は PseudostateKind 型の属性 kind で定義される種類に依る。
      次に種類と意味を記す。

      * initial: Region の開始点。
      * deepHistory: 所有 Region の直近の active state configuration を表現する変数の一種。
      * shallowHistory: deepHistory のようなものだが、
        その substate の substates とはならないもの。
      * join: ふたつ以上の Transitions の共通の target Vertex として役に立つ。
      * fork: ふたつ以上の Transitions に分裂するのに適う。
      * junction: 複数の Transitions を接続して States 間の複合パスを作るのに用いる。
      * choice: junction に似ているが、
        出て行く Transitions すべての guard Constraints を動的に評価する点が異なる。
      * entryPoint: StateMachine または composite State のための入口。
      * exitPoint: StateMachine または composite State のための出口。
      * terminate: ここに入ることは StateMachine の実行が直ちに終結することを暗示する。

    * transitive

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

  * Transition の意味はその source Vertex との関係に依存して決まる。
    Transition::kind の値が定義する。取り得る値は以下の 3 通り。

    * external: その Transition はその source から退場する、の意。
    * local: その Transition はそれを含む State から退場しない、の意。
    * internal: その Transition は自己遷移をする、の意。

  * 合成 States を source とする Transitions は
    high-level または group Transitions と呼ばれる。

  * Transition には guard という Constraint が関連していてもよい。

    * 偽に評価される guard を持つ Transitions は使用無効である。
    * 評価されるタイミングは、それを含む複合 Transition が利用可能になる前である。
    * 関連する guard がない Transition は、
      あたかもそれが常に真に評価される guard を持つかのように取り扱われる。

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

  * Transition の所有者は明示的に制限されていない。
    含まれている Region は直接間接を問わずその StateMachine が必ず所有するものではあるが。

    * 提案される所有者は、
      その source と vertex の両方を含む Region のうち最も内側のものである。

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

  * State を水平線で区切って複数区画に分割してもよい。
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
  * shallowHistory は``H`` を丸で囲む。
  * deepHistory は``H*`` を丸で囲む。
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

  * アクションシンボルは矩形で表現する。アクションのテキストでの仕様をつけてもよい。

  * Signal 受信シンボルは独特な凹五角形で表現する。
    中には ``<trigger>`` や ``<guard>`` を用いたテキストが含まれる。

  * Signal 送信シンボルの記法は SendSignalAction の記法に対応する。
    16 章参照。

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
  なおかつさらなる要素を含んでもよい。

* Regions を追加してもよい。
  継承した Regions は拡張によって再定義される。

  * States と Vertices を継承して、
    そして StateMachine の Regions の States と Transitions を再定義してよい。

.. 14.3.3.1.1 State redefinition

* 簡単な State をひとつ以上の Regions による合成 State になるように再定義（拡張）してもよい。
* 合成 State は次のように再定義（拡張）できる。

  * 新しい Regions を追加する。
  * 継承した Regions に Vertices と Transitions を追加する。
  * もし一般化 State が何も持っていなければ、
    entry/exit/doActivity Behaviors を追加する。
  * States と Transitions を再定義する。

* State の再定義は StateMachine 全体に適用する。

* submachine State もまた再定義してもよい。
  再定義された submachine StateMachine と同じ entry/exit ポイントを持つという条件の下で、
  submachine StateMachine は他の submachine StateMachine で置き換えてもよい。

* 複数の一般化 Classifiers の場合は、
  拡張 StateMachine が
  新しい Region に加えて、各一般化 Classifiers の StateMachines についての
  直交した Regions になることを拡張は暗示する。

.. 14.3.3.1.2 Transition redefinition

* 拡張 StateMachine の Transition はその拡張の中で再定義してもよい。
* Transitions はそれらの effect と target State を置き換えさせることができ、
  一方 source と trigger State はそのまま保たれる。

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
  State の名前に続いてラベル ``«final»`` を追加してもよい。

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
    それらの States は内部の behavioral StateMachines の States と必ずしも対応しなくてもよい。

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
    サブマシン StateMachines と複合遷移が用いられることがある。

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

    * 参照された機能が背景にある Classifier のオブジェクトの上で発動されることが可能である。
    * その Transition の完了にあたり、そのオブジェクトは事後条件が満たされている target State となるものである。

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
