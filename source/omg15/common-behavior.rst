======================================================================
13 Common Behavior
======================================================================
UML 2.5 pp. 283-302 に関するノート。
ノートにあまり時間をかけたくないが、
面倒なので見えているテキストを訳す場合がある。

.. todo:: 誤訳や変な解釈がいかにもありそうなので、発覚次第修正する。

.. todo::

   個人的に訳すのが厳しい、訳したくない、訳に納得していない英単語集。

   * automaton (n.) ここはそのままカタカナで。
     「状態機械」は state machine に使いたい。
     原文では複数形の automata で記されていたとしても
     ここでは「オートマトン」と書くかもしれない。

   * behavior (n.) 「振る舞い」「挙動」「行動」を気まぐれに使い分ける。
     字数を費やしたくない都合上、「挙動」を多用する。

   * context (n.)「文脈」を避けたい場合は
     「前後」「状況」「背景」「脈絡」など？

   * emergent (adj.) 「不意に起こる」ぐらいの意味のはず。

   * event (n.) ふつうは「イベント」とするが、
     当ノートでは実験的に「事象」で統一してみる。
     イベントプールが事象プールになるが、気にしない。

   * invoke (v.), etc. 「発動する」とした。
     「呼び出す」で十分伝わるかもしれない。

   * occurrence(s) (n.) これは instance(s) の Event 版と言える。
     「出来事」か「発生」か気分次第。

   * streaming (n.) これはどうしよう。

   * trigger (v.) 何かの引き金になる、
     何かのきっかけになる、何かを誘発する、等々。

.. contents:: ノート目次
   :depth: 2

13.1 Summary
======================================================================
* この章では UML にある挙動のモデリング全ての
  根底にある核心の概念を指定する。

* UML は
  Behavior, Event そして Trigger という構成要素を与えることで、
  対応する挙動のモデリングの基礎概念をモデル化する。

* Behavior は動的な変化をモデリングするための根本的な概念である。

  * Behavior は直接の発動によってか、
    挙動を務める (hosts) アクティブオブジェクトの生成によって
    実行してよい。

  * Behavior はまた突発的であってもよく、
    それら自身が特有の個々の挙動を実施して、
    ひとつまたはそれを超える関与オブジェクトの相互作用から生じるものである。

* 動的な挙動は、特定の時点で起こる興味のある事象に帰着する。

  * そういう事象は暗黙でよく、
    ある値またはある時間の範囲の経過の変化の際に発生する。

  * それらは明示的でもよく、
    操作が呼ばれたり、非同期信号が受信されたりすると発生する。

* 事象の発生は新しい挙動のきっかけになることができ、
  または、もう実行しているの挙動の経路を変えてよい。

  * 明示的な事象は挙動間の連絡にとっての根本的な仕組みをこうして与えて、
    そこでは、例えば操作を呼び出すことや信号を送ることのような、
    ある挙動で実行に移される行動が、
    別の挙動での応答のきっかけとなり得る。

* この章の残りは Behaviors, Events そして Triggers の
  基本的 UML モデリングの仕組みのさらなる詳細を述べる。
  これらの仕組みは後続の章で仕様化される UML の挙動のモデリング構成要素
  全部の屋台骨を用意する。

13.2 Behaviors
======================================================================

13.2.1 Summary
----------------------------------------------------------------------
* 本節では UML での挙動をモデリングするための屋台骨を導入する。
  Behavior の具象下位型（後続の章で述べる）は、
  さまざまな仕組みを用意することで挙動を指定する。

* UML はいろいろな挙動の仕様の仕組みを支援している：

  * 有限オートマトンをモデル化する StateMachines: :doc:`./statemachines`
  * Petri ネット的グラフを用いて定義される Activities: :doc:`./activities`
  * 事象発生の半順序連続列をモデル化する Interactions: :doc:`./interactions`

* これらの挙動の仕様の仕組みはそれらの表現力および適用性の領域の点で異なる。

13.2.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 13.1 Behaviors

  * Behavior を中心に据えたクラス図。
    新登場するクラスにはその他に OpaqueBehavior と FunctionBehavior がある。

A_classifierBehavior_behavioredClassifier
  * BehavioredClassifier から Behavior への関連（単方向）。

A_method_specification
  * BehavioralFeature から Behavior への関連（両方向）。

A_precondition_behavior
  * Behavior から Constraint への composite 関連（単方向）。
  * A_ownedRule_context を subsets する。

A_postcondition_behavior
  * Behavior から Constraint への composite 関連（単方向）。
  * A_ownedRule_context を subsets する。

A_ownedParameterSet_behavior
  * Behavior から Parameter への関連 composite 関連（単方向）。

    * Behavior が非同期的に発動されたならば、
      振る舞いの実行が完了するときにはどんな結果値も失われる。

  * A_ownedMember_namespace を subsets する。
  * ``ownedParameter`` は ordered である。

A_ownedParameterSet_behavior
  * Behavior から ParameterSet への関連 composite 関連（単方向）。
  * 入力 ParameterSets を伴う Behavior は一実行当たり、
    ひとつの集合の Parameters から入力を受け入れられるだけ。
  * 出力 ParameterSets を伴う Behavior は一実行当たり、
    ひとつの集合の Parameters に出力を差し出せるだけ。
  * A_ownedMember_namespace を subsets する。

A_ownedBehavior_behavioredClassifier
  * BehavioredClassifier から Behavior への composite 関連（単方向）。

A_context_behavior
  * Behavior から BehavioredClassifier への関連（単方向）。

13.2.3 Semantics
----------------------------------------------------------------------
13.2.3.1 Behaviors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Behavior とは長い時間に亘って動的に発生してよい事象の詳細である。

  * Behavior は
    それが ``method`` としてか、
    それが BehavioredClassifier の ``classifierBehavior`` として
    実装する BehaviorFeature で直接発動してよい。

* 各発動で、発動のため続いて起こる実際の事象の発生列は、
  Behavior の詳細に整合性を保っているが、
  Behavior についての execution trace と呼ばれる。

  * Behavior は正常に完了してよいか、
    例外の送出を結果として完了してよい。
    この場合は、Behavior が同期的に起動されたならば、
    例外は呼び出し側に伝えられる。

* UML では Behaviors は Classes の一種であり、
  それは Behaviors をオブジェクト化してよいということを意味する。
  Behavior のオブジェクトは振る舞いの実行 (behavior execution) として知られる。

  * Behavior を発動することはその Behavior をオブジェクト化することに相当し、
    Behavior 実行それぞれに対応する固有の execution trace がある。

* Behavior は Class であるがゆえに、それを特殊化してよいし、
  自身が StructuralFeatures や BehavioralFeatures を所有してもよい。

* Behavioral を複数回発動してよい。
  再入可能な (reentrant) Behavior は、
  その直前の発動が完了するよりも先にもう一度発動されてよい。
  再入可能でない Behavior は、
  先の発動が完了していなければ再度発動してはならないものとする。

* Behavior を同期的に、または非同期的に発動してよい。

* Behavior に対する ``preconditions`` は Behavior が発動される際に
  真であるものとする条件を定義する。
  ``precondition`` が成り立たないときの Behavior の発動の意味は
  意図的に未定義である。

* Behavior に対する ``postconditions`` は
  ``preconditions`` が成り立っていたという仮定で、
  Behavior の発動が成功に完了すると真となるはずの条件を定義する。

13.2.3.2 Behavior Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Behavior は実行に値を引き渡すのと、
  実行から値を受け取る能力のある Parameters を持ってよい。

* Behavior が発動されると、
  入力方向または入出力方向が
  それらの多重度によって強制された
  Parameters に対応している実引数の値が与えられる。

* Behavior の実行が完了すると、
  入出力、出力、そして戻り値方向が
  それらの多重度によって強制された
  Parameters に対応している結果の値をもたらしてよい。

* Parameters はストリーミングとして特徴付けてよい
  （すなわち ``isStreaming`` 特性が true である）。
  そのような Parameters は発動時と完了時以外にも、
  Behavior の実行途中の任意の時点で値を入出力することができる。

* 発動者がストリーミング出力 Parameters から値を得ることを可能にするためには、
  ストリーム出力が発動者で非同期的な応答のきっかけになる可能性があるときでさえ、
  発動された Behavior は同期的に発動される必要がある。

* 再入可能な Behavior はストリーミング Parameters を持たないものとする。
  複数の実行が同時に進む可能性があり、
  どの実行がストリーム値を受領したり提示したりしようとするのかが
  あいまいになろうとするためである。

* Behavior は
  ``isException`` が true である出力 Parameters を
  ひとつまたはそれを超える個数持ってよい。

* 入力 ParameterSets のある Behavior は
  実行ごとに集合のうちのひとつの
  Parameters からの入力を受け付けるしかできない。

13.2.3.3 Opaque and Function Behaviors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* OpaqueBehavior とは
  その詳細が UML 以外のテキスト言語で与えられる Behavior である。

* OpaqueBehavior は
  要求される挙動を記述する別の手段を表すテキスト Strings の列からなる
  ``body`` を持つ。

* 言語を指定する必要はない。

* OpaqueBehavior がひとつを超える ``body`` String を持つならば、
  ``bodies`` の任意のひとつが OpaqueBehavior の挙動を決定付けるのに使うことができる。

* FunctionBehavior とは
  どんなオブジェクトや他の外部データをも、アクセスしたり変更したりしない
  OpaqueBehavior である。

  * FunctionBehavior の実行中は、
    何であれ外部にある物を伴う通信や相互作用は禁止である。

  * 計算時間量は定義されない。

  * ある入力値に対しては FunctionBehavior は例外を送出してよい。
    その場合、計算内容は放棄される。

* FunctionBehaviors はこのように入力実引数の集合を
  出力結果値の集合に変換するような関数を表現する。

  * FunctionBehaviors の実行はその実引数にのみ依存して、
    結果の値を計算すること以外の効果を持たない。

  * FunctionBehaviors としてモデル化されるかもしれない関数の例として、
    初等的算術、論理値、文字列関数がある。

13.2.3.4 Behaviored Classifiers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* BehavioredClassifier とは ``ownedBehaviors`` を持ってよい Classifier であり、
  そのうちの高々ひとつが BehavioredClassifier 自身の挙動を指定するのに考慮される
  ものである。

* BehavioredClassifier の直接の ``ownedBehavior`` ではない Behavior は
  それでもなお ``context`` を持つ。

* Class により
  ``ownedBehavior`` としてではなく、
  ``nestedClassifier`` として直接所有される Behavior は、
  それの ``context`` としては Class を持たない。

* Behavior が ``context`` を持つならば、
  Behavior の実行は
  ``context`` BehavioredClassifier のオブジェクトである
  関連脈絡オブジェクトをいつでも持つ。

* BehavioredClassifier は、それの ``classifierBehavior`` と呼ばれる
  目立った ``ownedBehavior`` を持ってよい。

* ``classifierBehavior`` の正確な意味はそれを所有する BehavioredClassifier の
  種類に依存する。

  * ``isActive`` が false である Class は
    ``classifierBehavior`` を持たないものとする。

13.2.3.5 Behavioral Features and Methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* BehavioralFeatures には二種類、つまり Operations および Receptions がある。

* Class の BehavioralFeature をひとつまたはそれを超える ``method`` Behaviors
  が実装してよい。

* 受領オブジェクトは発動された ``method`` のいずれの実行の間においても
  脈絡オブジェクトになる。

* Reception の ``methods`` はいつでも非同期的に発動され、
  それに対して Operation の ``method`` は同期的にも非同期的にもどちらにも
  発動されてよいが、Operation がどう呼び出されたかに依存する。

* ``method`` の解決手順は要求されている BehavioralFeature と、
  要求を受信するオブジェクトと、
  そして要求に結び付いたデータの値のどれでもとに基くものとする。

* 次のものは
  高々ひとつの ``method`` が識別されているように常になる CallEvent に対する
  簡単なオブジェクト指向な解決手順である：

    受信オブジェクトの Class が CallEvent で識別された Operation について
    ``method`` を所有するならば、
    その ``method`` は解決の結果である。
    そうでなければ、
    受信オブジェクトの Class の基底クラスを Operation についての ``method`` で
    あるか調べ、
    ``method`` が見つかるか、階層の根に到達するまでは
    このようにして一般化の階層を上がっていく。

* Operation の ``method`` は Operation の Parameters に
  対応する Parameters を持つものとする。

* しかしながら、
  ``method`` の Parameters を
  BehavioralFeature の Parameters に一致することについて
  特定の扱い方は定義されていない。

  * 厳密一致。対応する Parameters の ``type`` が順序正しく同じである必要がある。

  * 共変一致。``method`` の Parameter の ``type`` が
    BehavioralFeature の Parameter の ``type`` の派生型でよい。

  * 反変一致。``method`` の Parameter の ``type`` が
    BehavioralFeature の Parameter の ``type`` の基底型でよい。

  * またはそれについての組み合わせ。

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
* Event とは、
  ある特定の瞬間に起こり得る何かである。
  ひとつの Event はたくさんの発生を持ってよく、
  それらは相異なる時刻において起こってよい。
  この道理だと、
  Events は実際には UML の Classifiers ではないが、
  Event をそれの発生の分類項目であるとみなすことができる。

* とりわけ重要なのは Behavior の内側で応答のきっかけになる Events である。
  UML で明示的にモデル化してよいそのような Events は次を含む：

  * TimeEvents: 特定の時刻または期間の後に起こる。

  * ChangeEvents: 特定のブーリアン値が true になると起こる。

  * MessageEvents: メッセージの受信で起こる。

13.3.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 13.2 Events

  * Trigger と Event 系のクラス図。
    Event には直接のサブクラスが先述した 3 種あり、
    そのうちひとつの MessageEvent にだけはさらに直接のサブクラスが
    やはり 3 種ある。

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
  * メッセージは ``operation`` の呼び出しを要求する。

A_signal_signalEvent
  * SignalEvent から Signal への関連（単方向）。
  * メッセージは ``signal`` オブジェクトの受信を要求する。

A_changeExpression_changeEvent
  * ChangeEvent から ValueSpecification への composite 関連（単方向）。
  * ChangeEvent は式 changeExpression の値が
    false から true になるときに起こるものである。
  * A_ownedElement_owner を subsets する。

A_when_timeEvent
  * TimeEvent から TimeExpression への composite 関連（単方向）。
  * TimeEvent の起こる瞬間を指定する TimeExpression である。
  * A_ownedElement_owner を subsets する。

13.3.3 Semantics
----------------------------------------------------------------------
13.3.3.1 Event Dispatching
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Event とは、
  潜在的に挙動の結果のきっかけとなってよいある出来事の詳細である。

  * Event は PackageableElement であり、
    Events がその利用と独立してモデル化されることを可能にする。

  * しかし Trigger は常にある大きな挙動の仕様の一部として現れる。

  * 単一の Event はいくつかの異なる Triggers で用いてよい。

* 13.2.3 節で論じたように、
  Behavior の実行はいつでも関連脈絡オブジェクト
  （実行それ自身であってよい）を持つ。

  * 脈絡オブジェクトは
    それの関連した Behavior 実行の全てについて
    Event 発生の処理を仲介する。

  * ある脈絡オブジェクトが Event 発生を認めると、
    それは即時効果を持つか、
    それは遅れたきっかけとなった効果のために保存されてよい。

  * 即時効果は
    BehavioralFeature の ``method`` の発動のような、
    Behavior の直接発動により、
    Event により決定付けられるものとして表明される。

  * きっかけとなった効果は、
    オブジェクトの事象プールにある出来事の保管場と、
    プールの出来事に対応する Event と一致する Trigger に到達する
    進行中の Behavior 実行による出来事の遅れた消費とによって表明される。

* 一般に、Trigger が続行することを必要とする
  待機点に Behavior 実行が着くと、
  それの脈絡オブジェクトの事象プールで
  残っている Trigger(s) を満足する事象があるか調べられる。

  * プールが Triggers の中のひとつを満足する事象の出来事を含んでいると、
    その出来事はプールから取り除かれて Behavior に送達され、
    指定されたようにそれの実行を続行する。

* 同じ脈絡オブジェクトを使う Behaviors はすべてが
  そのオブジェクトの事象プールを共有するが、
  ひとつの Behavior しか
  そのプールにある Event の出来事のどれでもを消費することができない。

* 事象プールにある Event の出来事が調べられるか送達されるかという
  特別の順序についての要件はない。

  * 事象プールが待機点にある Triggers を何も満足させない出来事を含むならば、
    BehavioredClassifiers の一般的な意味は何がそれに対して起こるかを指定しない。

13.3.3.2 Message Events
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* メッセージとは、
  送信者が Operation 呼び出しか受信者による Signal 受信のどちらかを
  要求する通信である。

  * この通信はふたつの事象を伴う。
    すなわち、メッセージを送信する事象と
    メッセージを受信する事象である。

  * しかしながら、事象を送信することは、
    それらが暗に InvaocationActions の実行中にあり、
    そのような事象の出来事が Interactions でモデル化されることが可能ではあるが、
    UML にある明示的なモデル要素としてモデル化されていない。
    その一方で MessageEvent はメッセージの受信の明示的なモデルであり、
    その事象の出来事に応答する Trigger を指定することを可能にするためのものである。

* メッセージは次のものを含む：

  * 要求に結び付くデータ（Operation 引数に対しては実引数、Signal 属性に対しては値）
  * 依頼の性質の情報（つまり発動された BehavioralFeature である）
  * 同期的な発動に対しては、
    発動された Behavior からの返信の復帰を可能にさせるのに十分な情報

* 各メッセージが正確にひとつの受信オブジェクトから対象とされて、
  正確にひとつの送信オブジェクトによって引き起こされる限りは、
  送信事象の出来事は発生されているメッセージをいくらか生じてよい。

  * メッセージの受信者は送信者と同じでよく、
    それが局所的でもよく、遠隔的でもよい。

  * メッセージの伝送の方法、
    メッセージを伝送するのに必要な時間量、
    伝送 (pl.) がそれらの受信オブジェクトに到着する順序、および
    受信オブジェクトに到着するための経路は未定義とする。

* メッセージの受信は MessageEvent の出来事として表明される。

  * CallEvent とは、
    特定の Operation が呼び出されることを要求するメッセージのための
    MessageEvent である。

  * SignalEvent とは、
    特定の Signal のオブジェクトの受信を要求するメッセージのための
    MessageEvent である。

  * AnyReceiveEvent とは、
    他の関係 Trigger のどれによっても明示的に処理されることのない
    メッセージのどれもに対する MessageEvent である。

* Operation に対する CallEvent
  または受信者の Reception に一致する Signal に対する SignalEvent の場合、
  その Operation なり Reception なりが
  ひとつまたはそれを超える ``methods`` を持つならば、
  13.2.3 節で述べた ``method`` 解決処理が
  MessageEvent の出来事を処理するのに用いられる ``method`` を決定付けるのに
  実施されるものとする。

  * ``method`` がそうして特定されると、
    それがメッセージ要求に応答するために発動される。
    さもなくば、MessageEvent の出来事が受信オブジェクトの事象プールに保存される。

  * MessageEvent の出来事が事象プールから発送されて、
    受信者についての Behavior の仕様で定義された Trigger に一致すると、
    その Behavior の内部での応答の実行を引き起こす。

* AnyReceiveEvent に対する Trigger は、
  メッセージのどんな受信がきっかけになってもよい。
  ただし、メッセージに明示的に一致する適切な SignalEvent または CallEvent Trigger が
  ある場合には、
  AnyReceiveEvent の Trigger はそのメッセージによって誘発されない。

* Trigger はひとつまたはそれを超える Ports を指定してもよく、
  その場合には Trigger の事象は MessageEvent であるものとする。
  この場合、Trigger は指定された Ports のひとつを通じて受信したメッセージに
  対する事象の出来事にしか一致しない。

13.3.3.3 Change Events
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ChangeEvent はブーリアン式 ``changeExpression`` が true になると発生する。
  例えば、これはある Attribute の変化や、
  ある Association に対応するリンクが参照する値の変化で
  生じるものである可能性がある。

  * ChangeEvent は暗黙的に起こるものであり、
    明示的な作用のどれによる結果でもない。

* ある出来事は
  ``changeExpression`` の値が false から true に変化するどんなときにも
  発生されるものとみなされる。

13.3.3.4 Time Events
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* TimeEvent はそれが発生する時間の瞬間を指定する。
  その瞬間は TimeExpression を使って指定される。

* 13.3.3.1 節で論じたように、
  事象の出来事が送達されてよいところで利用可能な、
  ひとつまたはそれを超える Triggers を持つ待機点に
  Behavior は到達してよい。

  * もしそのような未済 Trigger が相対 TimeEvent を持つならば、
    その TimeEvent についての開始時刻は Behavior が待機点に到達した時刻である。

13.3.4 Notation
----------------------------------------------------------------------
* Triggers での使用の脈絡外での Events に対する表記法はない。
  Trigger は Event の種類に基いてテキストで記される。

* CallEvent はきっかけとする Operation の名前で記し、
  オプションで代入仕様を続ける。

* SignalEvent はきっかけとする Signal の名前で記し、
  オプションで代入仕様を続ける。

* AnyReceiveEvent はいずれも ``all`` と記す。

* ChangeEvent は ``when`` を記し、
  Boolean ValueSpecification を続ける。
  :doc:`./values` 参照。

* 相対 TimeEvent は ``after`` を記し、
  "after 5 seconds" のような TimeExpression を続ける。
  絶対 TimeEvent は ``at`` を記し、
  "at Jan. 1, 2000, Noon" のような TimeExpression を続けることで指定する。

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
