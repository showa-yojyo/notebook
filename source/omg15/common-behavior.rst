======================================================================
13 Common Behavior
======================================================================
UML 2.5 pp. 283-302 に関するノート。
ノートにあまり時間をかけたくないが、
面倒なので見えているテキストを訳す場合がある。

.. todo::

   個人的に訳すのが厳しい、訳したくない、訳に納得していない英単語集。

   * automaton (n.) ここはそのままカタカナで。
     「状態機械」は state machine に使いたい。
     原文では複数形の automata で記されていたとしても
     ここでは「オートマトン」と書くかもしれない。

   * emergent (adj.) 「不意に起こる」ぐらいの意味のはず。

   * event (n.) ふつうは「イベント」とするが、
     当ノートでは実験的に「事象」で統一してみる。
     イベントプールが事象プールになるが、気にしない。

   * invoke (v.), etc. 「発動する」とした。
     「呼び出す」で十分伝わるかもしれない。

   * occurrence(s) (n.) 「出来事」か「発生」か気分次第。

   * streaming (n.) これはどうしよう。

   * trigger (v.) 何かの引き金になる、
     何かのきっかけになる、何かを誘発する、等々。

.. contents:: ノート目次

13.1 Summary
======================================================================
* この章では UML にある振る舞いに関するモデリング全ての根底となる核心の概念を挙げていく。
* UML は振る舞いに関するモデリングの基礎概念をモデル化するために、
  Behavior, Event, Trigger という構成要素を提供する。

  * Behavior は動的な変化をモデリングするための根本的な概念である。

    * Behavior は直接起動によるか、
      その振る舞いを務める (hosts) アクティブオブジェクトの生成を通じて実行されてよい。

    * Behavior は
      それら自身が特有の個々の振る舞いを実施している、
      ひとつ以上の関与オブジェクトの相互作用から生じてもよい。

  * 動的な振る舞いは、結果的に特定の時点で起こる重要な (of interest) 事象に終わる。

    * そういう事象は暗黙でよく、
      ある値またはある時間の範囲の経過の変化の上に起こっているものである。

    * その上明示的でもよく、
      ある操作が呼ばれたり、
      ある非同期信号が受信されたときに起こっているものである。

  * 事象の出来事は新しい振る舞いを引き起こしてよい。
    または、すでに実行中の振る舞いの経路を変えてよい。

    * 明示的な事象は振る舞い (pl.) の間の通信のために根本的な仕組みを提供する、
      そこではある振る舞い、
      例えばある操作を呼び出すことや信号を送るというような、
      振る舞いの中で実行に移されるひとつのアクションが、
      別の振る舞いの中での応答のきっかけとなることが可能だ。

* この章の残りは Behaviors, Events, Triggers の基本的 UML モデリングの仕組みをさらに詳述する。
  これらの仕組みは後続の章で仕様化される UML の振る舞いのモデリング構成要素全部の屋台骨を提供する。

13.2 Behaviors
======================================================================

13.2.1 Summary
----------------------------------------------------------------------
* 本節では UML での振る舞いをモデリングするための屋台骨を導入する。
  Behavior の具象型（後続の章で述べる）は振る舞いを指定する異なる仕組みを与える。

* UML はさまざまな振る舞いに関する仕様を支援している。
  これらの仕様の仕組みは表現力と適応領域において異なる。

  * 有限オートマトン (pl.) をモデル化する StateMachines: 14 章
  * Petri ネット的グラフ (pl.) を用いて定義される Activities: 15 章
  * 事象発生の半順序連続列 (pl.) をモデル化する Interactions: 17 章

13.2.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 13.1 Behaviors

  * Behavior を中心に据えたクラス図。
    新登場するクラスにはその他に OpaqueBehavior と FunctionBehavior がある。

13.2.3 Semantics
----------------------------------------------------------------------
*Behavior*
  * Class の一種。
  * TODO: 13.2.3.1 の最初のパラグラフ前半がわからない。

  * Behavior を次のように直接呼び出してよい。

    * それが method として実装する BehaviorFeature を介して
    * BehavioredClassifier の classifierBehavior として

  * 発動ごとに、その発動に因る後続する実際の事象発生列は、
    その Behavior のための execution trace と呼ばれる。

    * Behavior は正常に完了してよいか、
      または結果として例外の送出で完了してよい。

  * UML では Behaviors は Classes の一種であり、
    それは Behaviors をオブジェクト化してよいということを意味する。
    Behavior のオブジェクトは振る舞いの実行 (behavior execution) として知られる。

    * Behavior を発動することはその Behavior をオブジェクト化することに相当し、
      各 Behavior 実行に対応する特有の execution trace がある。

  * Behavior は Class であるがゆえに、それは特殊化されてもよいし、
    自身が StructuralFeatures や BehavioralFeatures を所有してもよい。

  * 再入可能 (reentrant) な Behavior は、
    その直前の発動が完了するよりも先に再度発動されてよい。
    そうでない Behavior は、発動者が存在する実行が完了するまで
    使用を制限する (block) 必要がある。

  * Behavior は同期的に、または非同期的に発動されてよい。

OpaqueBehavior
  * Behavior の一種。
  * その詳細が UML とは別のテキストに基づく言語で与えられる Behavior である。
  * body は要求される振る舞いを記述した文字列からなり、
    それに対応する language は何の言語で解釈するべきかを示す文字列からなる。

FunctionBehavior
  * OpaqueBehavior の一種。
  * どんなオブジェクトや他の外部データをも、アクセスしたり変更したりしない。
    FunctionBehavior の実行中は、
    何であれ外部にある物を伴う通信や相互作用は禁止である。

  * 計算時間量は定義されない。
  * ある一定の入力値に対しては例外を送出してよい。
    その場合は計算内容は放棄される。

  * FunctionBehaviors は入力実引数の集合を
    出力結果値の集合に変換するような関数を表現する。

  * FunctionBehaviors の実行はその実引数にのみ依存して、
    結果の値を計算すること以外の効果を持たない。

  * FunctionBehaviors としてモデル化されるであろう関数には、
    初等的算術、論理値、文字列関数がある。

A_classifierBehavior_behavioredClassifier
  * BehavioredClassifier から Behavior への関連（単方向）。
  * 先述の Behavior のノート参照。

  * classifierBehavior の厳密な意味は、それを所有する BehavioredClassifier の種類に従う。

    * Collaboration::classifierBehavior なら全ての部分の emergent な振る舞いを表現する。
    * Class::classifierBehavior なら部分とは離れたその Classのオブジェクトの振る舞いを表現する。

  * 受動的 (passive) な Class は classifierBehavior を持つことはならない。

A_method_specification
  * BehavioralFeature から Behavior への関連（両方向）。
  * 先述の Behavior のノート参照。

A_precondition_behavior
  * Behavior から Constraint への composite 関連（単方向）。
  * 事前条件、つまり Behavior が発動されるときに真でなければならない条件を定義する Constraints である。
    事前条件が満足されていないときにおける Behavior の発動の意味は意図的に未定義である。
  * A_ownedRule_context を subsets する。

A_postcondition_behavior
  * Behavior から Constraint への composite 関連（単方向）。
  * 事後条件、つまり Behavior の発動が成功裡に完了するときに真となるだろう条件を定義する Constraints である。
  * A_ownedRule_context を subsets する。

A_ownedParameterSet_behavior
  * Behavior から Parameter への関連 composite 関連（単方向）。
  * Behavior は振る舞いの実行に対して値 (pl.) を入出力する能力を与える Parameters を持ってよい。

    * Behavior が非同期的に発動されたならば、
      振る舞いの実行が完了するときにはどんな結果値も失われる。

  * Parameters は streaming として印を付けられてよい。
    振る舞いの実行中の任意の時点で、値を入出力することを許容するものである
    （値が引き渡されるのは普通は発動時か完了時である）。

    * 入力引数が streaming な場合と、出力引数が streaming な場合、等がある。
    * 発動者が streaming な出力引数を得ることを可能にするべく、
      発動された Behavior は同期的に発動される必要がある。

    * 再入可能な Behavior は streaming Parameters を持たない必要がある。

  * Behavior は isException が true である出力 Parameters をひとつ以上持ってよい。
    この場合は実行完了時に

    * どの Parameters も値を持ってはならないか、
    * ちょうどひとつが値を持つ必要があり、それ以外がどんな値も持ってはならない。

  * A_ownedMember_namespace を subsets する。
  * ownedParameter は ordered である。

A_ownedParameterSet_behavior
  * Behavior から ParameterSet への関連 composite 関連（単方向）。
  * 入力 ParameterSets を伴う Behavior は一実行当たり、
    ひとつの集合の Parameters から入力を受け入れられるだけ。
  * 出力 ParameterSets を伴う Behavior は一実行当たり、
    ひとつの集合の Parameters に出力を差し出せるだけ。
  * A_ownedMember_namespace を subsets する。

A_ownedBehavior_behavioredClassifier
  * BehavioredClassifier から Behavior への composite 関連（単方向）。
  * ownedBehaviors のうちの高々ひとつが BehavioredClassifier 自身の振る舞いと見なされる。

A_context_behavior
  * Behavior から BehavioredClassifier への関連（単方向）。
  * ある BehavioredClassifier の ownedBehavior である Behavior は、
    その BehavioredClassifier を自分の context として持つ。
  * どの BehavioredClassifier::ownedBehavior でもない Behavior であっても、
    やはり context のようなものがある。
    ある種の chain-rule により特定できる (pp. 286-287) ようだ。

13.2.4 Notation
----------------------------------------------------------------------
* Behavior の各種サブクラスの記法は後続の章で定義する。
* Signals と Receptions の記法は :doc:`./simple-classifiers` で取り扱った。
* アクティブ Class の記法は :doc:`./structured-classifiers` で取り扱った。

13.2.5 Examples
----------------------------------------------------------------------
なし。

13.3 Events
======================================================================

13.3.1 Summary
----------------------------------------------------------------------
* Event とはある特定の瞬間に起こり得る何かである。
  Event はたくさんの発生を持つことが許され、
  それらは相異なる時刻において起こることが許される。
  この道理だと
  本当は Events は UML において Classifiers ではないが、
  ひとつの Event をそれの発生 (pl.) の分類項目であるとみなすことができる。

* とりわけ重要なのはある Behavior の内側にある応答を誘発する Events である。

  * TimeEvents: ある特定時刻またはある期間の後に起こる。

  * ChangeEvents: ある特定のブーリアン値が true になるときに起こる。

  * MessageEvents: あるメッセージの受領時に起こる。

    * メッセージとはある Behavior から、
      ある Operation 呼び出しまたは Signal 受信を依頼している
      別の Behavior への通信のことである。

13.3.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 13.2 Events

  * Trigger と Event 系のクラス図。
    Event には直接のサブクラスが先述した 3 種あり、
    そのうちひとつの MessageEvent にだけはさらに直接のサブクラスが
    やはり 3 種ある。

13.3.3 Semantics
----------------------------------------------------------------------
Trigger
  * NamedElement の一種。
  * Trigger は常に何か大きな振る舞いに関する仕様の一部として現れる。

*Event*
  * PackageableElement の一種。
  * Event とは潜在的に振る舞いにかかわる作用を誘発してよい何らかの出来事の詳細である。

  * Behavior execution の context オブジェクトは 
    その関連した Behavior executions の全てに対して、
    Event 発生の処理を仲介する。

  * ある context オブジェクトがある Event 発生を認識するときに、
    それは immediate effect か triggered effect のどちらかを持ってよい。

    * その Event が決める Behavior の、
      例えば BehavioralFeature の method などの
      直接発動が immediate effect を表す。

    * オブジェクトの事象プール (event pool) にある出来事の格納所と、
      進行中の Behavior execution による出来事の後の消費が
      triggered effect を表す。

  * 一般に、Behavior execution が Trigger を続行することを必要とする
    待機点 (wait point) になるときに、
    残っている (outstanding) Trigger(s) を満たす事象を求めて
    その context オブジェクトの事象プールが調べられる。
    もしプールが Triggers のひとつを満たす事象の出来事を含むならば、
    その出来事はプールから取り除かれて Behavior に送達され、
    その Behavior はその実行を指定されたように続行する。

    * 何を書いたのか全然わからない。

  * 同じ context オブジェクトを使うすべての Behaviors は
    そのオブジェクトの事象プールを共有するが、
    そのプールにあるどの Event の出来事もただひとつの Behavior が消費できる。

  * 事象プールにある Event の出来事同士には、
    調べられたり送達されたりすることの順序についての要件はない。

  *MessageEvent*
    * Event の一種。

    * メッセージとは
      Operation 呼び出しか受信者による Signal 受信のどちらかに対して、
      送信者が依頼する通信である。

    * この通信はふたつの事象を伴う。
      すなわち、メッセージを送信する事象と
      メッセージを受信する事象である。

    * 事象を送信することは、
      それらが暗に InvaocationActions の実行中にあり、
      そのような事象の出来事が Interactions でモデル化されることができるけれども、
      UML は 明示的なモデル要素としてモデル化していない。
      他方で MessageEvent はメッセージの受信の明示的なモデルである。
      その event の出来事に応じる Trigger を指定することができる。

    * メッセージは次のものを含む

      * 依頼に関連したデータ（Operation 引数には実引数、Signal 属性には値）
      * 依頼の本質に関する情報（つまり発動された BehavioralFeature の）
      * 同期的発動に対しては、発動された Behavior からの返信の復帰を可能にさせるのに十分な情報

    * 各メッセージが正確にひとつの受信オブジェクトを標的とされて、
      正確にひとつの送信オブジェクトによってもたらされる限りは、
      送信事象の出来事の結果としていくらかのメッセージが発生されてよい。

    * メッセージの受信者は送信者と同じでよいし、局所的でも遠隔的でもよい。

    * 次のものは未定義とする。

      * メッセージの伝送の方法
      * メッセージを伝送するのに必要な時間量
      * 伝送 (pl.) がそれらの受信オブジェクトに到着する順序
      * 受信オブジェクトに到着するための経路

    * メッセージの受信は MessageEvent の出来事として表される。

    CallEvent
      * MessageEvent の一種。
      * CallEvent は 
        特定の Operation が呼び出されることを要求しているメッセージのための
        MessageEvent である。

    SignalEvent
      * MessageEvent の一種。
      * SignalEvent は
        特定の Signal のオブジェクトの受信を要求しているメッセージのための
        MessageEvent である。

      * ある Operation のための CallEvent または
        受信者の Reception に match する Signal のための SignalEvent の場合に、
        もしその Operation なり Reception なりがひとつ以上の methods を持つならば、
        そのメソッド解決処理、
        MessageEvent の出来事を扱うのに用いられる method の決定が実施される必要がある。

        もしある method がそう特定されれば、それがメッセージ依頼に応じるために発動される。
        さもなくば、MessageEvent の出来事が受信オブジェクトの事象プールに保存される。
        ある MessageEvent の出来事が事象プールから発送されて、
        その受信者のための Behavior の仕様に定義された Trigger に match するときに、
        その Behavior の内部での反応の実行をもたらす。

    AnyReceiveEvent
      * MessageEvent の一種。
      * AnyReceiveEvent は
        どのその他の関係 Trigger によって明示的に処理されることのないあらゆるメッセージのための
        MessageEvent である。

      * AnyReceiveEvent のための Trigger は、
        どんなメッセージの受信がきっかけになってもよい。
        ただし、メッセージに明示的に match する SignalEvent か CallEvent の Trigger が
        ある場合には AnyReceiveEvent の Trigger は働かない。

  ChangeEvent
    * Event の一種。

    * ChangeEvent はブーリアン式 changeExpression が真になるときに起こる。
      例えば、ある属性の値の変化や、
      ある関連に対応するリンクが参照する値の変化した結果かもしれない。

    * ChangeEvent は暗黙的に起こり、何らかの明示的な作用の結果ではない。

    * ある出来事は
      changeExpression の値が false から true に変化する任意のときに
      発生されるものとみなされる。

      * ただし、changeExpression が評価されるとき等は明示的には定義されていない。

  TimeEvent
    * Event の一種。
    * TimeEvent はそれが起こる瞬間がいつなのかを指定する。
      絶対時間でも相対時間でも指定される。

      * isRelative の値で判定。

    * Behavior は事象発生 (pl.) が発送されてよい
      Triggers を一つ以上持つ待機点に到達してよい。
      もしそのような未済 Trigger が相対 TimeEvent を持つならば、
      その TimeEvent のための開始時刻は Behavior が待機点に到達した時刻である。

A_event_trigger
  * Trigger から Event への関連（単方向）。
  * 単一の Event をいくつかの異なる Triggers で用いてよい。

A_port_trigger
  * Trigger から Port への関連（単方向）。
  * その事象が MessageEvent である必要がある場合に、
    Trigger はひとつ以上の Ports を指定してよい
    この場合は Trigger は指定 Ports のひとつを通じて受信したメッセージのための
    事象の出来事に単に match する。

A_operation_callEvent
  * CallEvent から Operation への関連（単方向）。
  * メッセージは operation の呼び出しを要求する。

A_signal_signalEvent
  * SignalEvent から Signal への関連（単方向）。
  * メッセージは signal オブジェクトの受信を要求する。

A_changeExpression_changeEvent
  * ChangeEvent から ValueSpecification への composite 関連（単方向）。
  * ChangeEvent は式 changeExpression の値が
    false から true になるときに起こるものである。
  * A_ownedElement_owner を subsets する。

A_when_timeEvent
  * TimeEvent から TimeExpression への composite 関連（単方向）。
  * TimeEvent の起こる瞬間を指定する TimeExpression である。
  * A_ownedElement_owner を subsets する。

13.3.4 Notation
----------------------------------------------------------------------
* Trigger の記法はテキストによる。例によって BNF による仕様が記されている (pp. 291-292)。
* Trigger の記法はそれが参照する Event の種類に基づく。

  * CallEvent ならば引き起こされる Operation の名前が必要。
  * SignalEvent ならば引き起こされる Signal の名前が必要。
  * AnyReceiveEvent ならば単に ``all`` と記す。
  * ChangeEvent ならば ``when`` プラスブーリアン式。
  * TimeEvent ならば ``after`` プラス TimeExpression または
    ``at`` プラス TimeExpression のどちらかになる。

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
