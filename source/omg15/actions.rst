======================================================================
16 Actions
======================================================================
UML 2.5 pp. 439-562 に関するノート。
本章は記述の分量が多いので、ノート用ファイルを分割するのがよいかもしれない。

.. todo:: 最低でもあと一回は編集する。

.. todo::

   * open end (n.) これがピンと来ないのはマズイ。

   * qualifier value (n.)
     何かを限定する値の意だとは思う。

     C++ だと ``const`` や ``volatile`` を qualifier だと言うのだが、
     ここでは忘れてよい。

   * reduce (v.) 数学とかプログラミングとかでよくある状況での用法での訳。
     ここでは「縮合する」と訳しておく。

   * tool (n.) なぜだか「道具」や「器具」ではしっくりと来ない。

   * unmarshal (v.) のスペリングに注意。
     仕様書では最後の l をどんな場合でも重ねるが、
     辞書によると不定詞では l は一個しかない。

.. contents:: ノート目次
   :depth: 2

16.1 Summary
======================================================================
* Action とは UML に挙動の指定の基本的な単位である。
  Action は入力の集合を取り、出力の集合を生じるが、
  その集合の一方または両方がからであってもよい。
  Action が実行するシステムの状態を変更する Actions もあってよい。

* Actions は Behaviors に、
  特に Activities と Interactions に含まれている。
  これらの Behaviors は Actions がいつ実行するのかと、
  それらが持つ入力が何であるかを決定する。

16.1.1.1 Concrete Syntax
----------------------------------------------------------------------
.. note:: 節番号のレベルがおかしいのは原書通り。

* UML 仕様は Actions を表す図表的表記法の相対的に極小な集合を実現する。

  * 準拠ツールはツール固有の
    標準の Action 抽象的構文へ写像する
    図表的またはテキスト的表現を備えてよい。
    そのような表現は具象的構文と呼ばれる。

* 具象的構文は高水準の構成要素を
  UML 抽象的構文で指定された Actions へ
  写像することが可能である。

* 当仕様でのもっとも原始的な Actions は、
  具体的構文の写像の最大範囲を
  使用可能にするために定義されている。

16.1.1.2 Execution Engines
----------------------------------------------------------------------
.. note:: 節番号のレベルがおかしいのは原書通り。

* 実行機関 (an execution engine) とは UML Actions を実行する道具のことである。
  Actions はさまざまなやり方の特徴を持ったさまざまな実行機関の
  構成要素を使用可能にするために定義される。

* モデル作者は、
  その実行を最適化するの価値があるかもしれない
  領域解決法の特別な知識が彼らにあるときに、
  実行機関に対してヒントを与えることが可能である。

* Actions の実行が実行時の挙動を強制する
  UML の構造的意味の様相に違反するときは、
  Actions の意味は未定義のままとする。

16.2 Actions
======================================================================

16.2.1 Summary
----------------------------------------------------------------------
* 本節では Actions および Pins の初歩的な抽象構文について定義する。
  Pins は Actions に対する入力と出力を指定するのに用いられる。
  OpaqueAction 以外は、Actions の諸々の具象型は後続の節で述べる。

16.2.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 16.1 Actions

  * Action は抽象型で、ExecutableNode から派生している。

    * この図式では差し当たり OpaqueAction が Action のひとつの具象型であることを表している。
    * InputPin と OutputPin とに別々に関連させる。

  * Pin という ObjectNode と MultiplicityElement からの派生要素がある。

    * Pin には InputPin と OutputPin のふたつがある。
    * InputPin には ActionInputPin と ValuePin のふたつがある。
      ActionInputPin は Action を、
      ValuePin は ValueSpecification をそれぞれ関連させる。

16.2.3 Semantics
----------------------------------------------------------------------
16.2.3.1 Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Action とは Behavior に直接的または間接的に含まれる、
  実行可能機能の基本的な単位である。
  Action の実行はモデル化されたシステムにおける
  ある変換や過程を表す。
  システムは計算機システムであるか、さもなければ別のシステムである。

  * Action の実行は別の Behavior の発動をも引き起こしてよい。

* Action を含んでいる Behavior に背景となる BehavioredClassifier があれば、
  その BehavioredClassifier はその Action に対する
  ``context`` Classifiers でもある。

* Action の InputPins と OutputPins が指定するように、
  Action は入力を受け付け、出力を生じる。
  Action の Pin それぞれが、その Action の
  固有の入力または出力についての型および多重度を指定する。

* Action が実行する時間と、
  各実行が受け付ける入力が何であるのかは、
  Action の種類と、
  InputPins の特徴と、
  それが使われる Behavior とによって決定される。
  いったん Action が実行することが決定されると
  その実行に対する一般的な手順は次の通りである：

  #. Action の実行は、
     その Action の InputPins すべてにおける入力データを、
     InputPin それぞれについての多重度 ``upper`` 個まで (up to) 消費する。

  #. Action はそれが完了するまでは実行を続行する。
     実行の詳細な意味と完了の定義は実行される Action の種類に依存する。

  #. 完了したら、Action の実行は OutputPins における
     出力データのどれでもを求めて、停止する。

* Actions の意味の仕様上、
  Behaviors は同じ種類の Action を複数回再利用することが許されていて、
  Action の意味は用法のそれぞれに別個に適用する。

* Action が局所的に再入可能でない (``isLocallyReentrant`` == false) ならば、
  ひとつを超える実行が任意の時点において含んでいる
  Behavior の単独の実行内には存在することは許されない。

* 非再入可能 Behavior (``isReentrant`` == true) に対する CallAction もまた、
  その活動に対する ``isLocallyReentrant`` 特性の値が何であれ、
  あたかも CallAction が局所的に非再入可能であるかのように振る舞うはずである。

* Action についての ``localPrecondition`` と ``localPostcondition`` は、
  Action の実行が開始するときと終了するときに
  それぞれ成り立つべき Constraints である。
  ``localPrecondition`` または ``localPostcondition`` は
  モデル作者が定義する Constraint であるので、
  違反とは UML Action 実行の意味が未定義であることではない。

16.2.3.2 Opaque Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* OpaqueAction とは、
  その仕様が UML 外のテキスト的な具体的構文で与えられてよい Action である。
  何か他の種類の Action が選ばれる前に
  OpaqueAction を一時的な代用として使ってもよい。

* OpaqueAction には、
  その Action の挙動を指定する代用法を表すテキスト Strings の列で構成される
  ``body`` がある。
  ``language`` Strings の対応する列を、
  その ``body`` Strings のそれぞれが解釈されることになる言語を
  指定するのに使ってよい。
  言語を ``body`` Strings と順番に一致する。

* OpaqueAction にひとつを超える ``body`` があれば、
  ``bodies`` のどのものも OpaqueAction の挙動を決定するのに
  使われる可能性がある。
  その選択がどうなされるかについては UML は決定しない。

16.2.3.3 Pins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Pin とは Action についての入力と出力を表現するものである。

  * InputPin が入力を表し、一方 OutputPin が出力を表す。
  * Action に所有される入力と出力の集合のそれぞれは順序付いている。
  * Action の InputPins と OutputPins は Action の種類により決定される。

* Pin は ObjectNode の一種なので、
  指定された Type の値を含むオブジェクトトークンを保持する。

  * Action の InputPin のトークンに保持される値は
    Action の実行に対する入力データを与え、
    Action の実行から生じた出力データは
    オブジェクトトークンに包み込まれて、
    Action の OutputPins に置かれる。

* Pin は属性 ``ordering`` を ObjectNode から、
  属性 ``isOrdered`` を MultiplicityElement から両方継承する。
  これらの属性の値は独立に定めてよい。

  * 例えば ``isOrdered`` が true で ``ordering`` が FIFO であると、
    MultiplicityElement と同じ順序で Pin から値が取られるはずである。

* InputPin とは Action が消費する入力値を保持する Pin である。

* OutputPin とは Action がもたらす出力値を保持する Pin である。

* ValuePins と ActionInputPins は InputPins であるが、
  Action が実行可能であるかどうかの決定では用いられない。

* ValuePin は ValueSpecification を評価することで値を与える。
  Action が他の手段によって使用可能であると、
  ValuePin の ValueSpecification が評価されて、
  その結果が実行を開始するときの Action に対する入力として求められる。

* ActionInputPin は別の Action を実行することで値を与える。
  Action が他の手段によって使用可能であると、
  Action が所有する ActionInputPins のどの ``fromActions`` もまた使用可能になる。

16.2.3.4 Actions and Pins in Activities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Action が（ということは Pins も）が Activity に含まれるならば、
  いつトークンが Pins に出入りするのかと、
  いつその Action が実行するのかは、
  Actions はもちろんのこと Activities の意味によって決定する。

* Activity にある Action を実行することは、
  その InputPins すべてが、
  それらの最小の多重度が指定するとおりに、
  必要なトークンすべてを受け入れるつもりであることを
  必要とする。

* Activity にある Action が実行を完了すると、
  その OutputPins に配置された出力データについての
  オブジェクトトークンは、
  Pins から出ている ``outgoing`` ObjectFlows の
  どれに運び込まれてもよい。

* Action が局所的に再入可能ではない (``isLocallyReentrant`` == false) ならば、
  いったん実行を開始すると、その Action および InputPins は
  実行が終了するまでは運び込まれるトークンをどれも受け付けない。

* 制御 Pin (``isControl`` == true) は
  制御の種類を持つもの (``isControlType`` == true) とする。
  そうすることで ControlFlows と一緒に使ってよくなる。

16.2.4 Notation
----------------------------------------------------------------------
* 本節では Activities で使われる Actions を表す図表的表記法を指定する。
  この表記法は準拠ツールがテキスト上の具象的構文を代わりに使えるという
  点で選択自由である。

16.2.4.1 Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Figure 16.2 Action

  * Actions は丸角矩形を用いて示す。
  * Action の名前や他の説明が記号中に現れてよい。
  * Actions の派生型に特化した記法は後続の節で述べる。

* Figure 16.3 Local pre- and post-conditions

  * 局所的な事前条件と事後条件はそれぞれキーワード
    ``«localPrecondition»`` と ``«localPostcondition»``
    が付いた発動に取り付けられた註釈として示す。

16.2.4.2 Pins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Figure 16.4 Pin notations

  * Pins は ObjectNodes なので、矩形として記す。
    矩形は所有されている Action 記号に取り付けられている
    小さい矩形として記される。

  * Pin の名前をその付近に表示してもよい。
    単に型だけを見せることがよくある。
    両者を示すには ``name: type`` のようにラベルする。

  * Action の Pins は、モデル内にそれが存在しているときでさえ、
    記法の省略が許されている。

* Figure 16.5 Pin notations, with arrows

  * InputPins と OutputPins を区別する ActivityEdges が存在しないときには、
    任意で矢印を Pin 矩形の内部に配置しても構わない。

  * InputPins には Action の方向を指し示す矢印があり、
    OutputPins には Action から離れる方向を指し示す矢印がある。

* Figure 16.6 Standalone Pin notations

  * ある Action の OutputPin が ObjectFlow を介して
    別の Action の同名の InputPin に接続している状況では、
    この図のようなオプションの記法で示すことが許される。

  * この形式は両者の型が同じでないならば避けるべきである。

* 制御 Pins はその Pin 記号付近に ``{control}`` とテキスト的注釈と共に示す。

* ValuePin はその脇に ValueSpecification が書かれている InputPin として記す。

16.2.5 Examples
----------------------------------------------------------------------
16.2.5.1 Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Figure 16.7 Examples of Actions

  * Send Payment の実施後に Accept Payment が実施される。

* Figure 16.8 Example of action using a tool-specific concrete syntax

  * あるツールに固有の具体的構文で表現されたアクションらしい。
    ループ処理をひとつの Action で表してよいようだ。

* Figure 16.9 Example of an action with local pre- and post-conditions

  * Dispense Drink という Action の事前条件と事後条件が詳細に記された例。
    飲み物が自販機から出る前後の状態が普通の英語で仕様化されている。

16.2.5.2 Pins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Figure 16.10 Pin examples

  * 目を引くのは ``{stream}`` や角括弧付きのラベル。

* Figure 16.11 Specifying selection behavior on an ObjectFlow

  * Pin は ObjectNode なので ``selection`` の指定が可能。

* Figure 16.12 Example abstract syntax model showing the use of ActionInputPins

  * ``self.foo->bar(self.baz)`` なるテキストによる具体的構文の式を
    UML 抽象構文式で示したもの。

16.3 Invocation Actions
======================================================================

16.3.1 Summary
----------------------------------------------------------------------
* InvocationAction は直接的または間接的にある Behavior の発動に帰着する
  Action である。

* InvocationActions である CallActions には、

  * Operations や Behaviors を呼び出したり、
  * 以前オブジェクト化された Behaviors を開始したりするものがある。

* さらなる InvocationActions の種類には次を考慮したものがある。

  * 信号とその他のオブジェクトの狙いを付けた送信
  * 利用可能な受信者に向けて信号を一斉送信する能力

16.3.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 16.13 Invocation Actions

  * 抽象型 InvocationAction から派生する型がいくつかある。
    概要に書いてあるとおりのクラス図。

16.3.3 Semantics
----------------------------------------------------------------------
16.3.3.1 Call Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* CallAction は Behavior または Operation を呼び出す InvocationAction である。
  次の 3 種類が存在する。

  #. CallBehaviorAction は直接 Behavior を発動する CallAction である。
  #. CallOperationAction は Operation 呼び出し要求メッセージを
     目標オブジェクトに伝達する CallAction であり、
     伝達先では関連 Behavior の発動を引き起こす。
  #. StartObjectBehaviorAction は直接オブジェクト化された Behavior か、
     あるオブジェクトの classifierBehavior のどちらか一方の実行を開始する
     CallAction である。

* CallAction は
  直接的にか、またはある Operation 呼び出しのどちらかを通じてかで、
  同期的または非同期的に Behavior 発動に帰着する。

  * もし呼び出しが同期的 (isSynchronous) ならば、
    その Action の実行は
    発動された Behavior の実行が（正常にかどうかを問わず）完了するまで
    完了しない。

  * もし呼び出しが非同期的 (!isSynchronous) ならば、
    その Action の実行はその Behavior が発動されるとすぐに完了する。

* もし CallAction が発動する Behavior が再入可能でなければ、
  ひとつを超える実行が任意の与えられた時点において存在してはならない。

* Behaviors と Operations は所有 Parameters の全順序リストを持っていて、
  これらの Parameters はその順序を用いて CallAction の Pins に match される。

* CallAction の実行時には、その argument Pins にある値を、
  対応する入力 Parameters のところにある
  発動される Behavior または Operation に引き渡す。

* もし Parameters のうちのどれが streaming ならば、
  その呼び出しは同期的であるものとする。
  13 章も参照。

* Actions についての実行規則に加えて、
  streaming Parameters を伴う Behavior や Operation を発動する
  CallAction は次の規則も適用する。

  * 通常の規則によって CallAction が実行が可能となるのに先立って、
    すべての InputPins が各 Pin の多重度以上の個数の値を
    差し出してもらう必要がある。

  * CallAction が正常に実行を完了することが可能になる前に、
    ある streaming Parameter に対応している
    CallAction の各実引数 Pin の多重度の下限以上の値が受理されるものとする。

  * 発動された Behavior の実行が正常に完了する前に、
    少なくとも CallAction の各 result Pin の多重度の下限に等しい
    個数の値がその実行が完了するまでの時間内に post されなければならない。

* ParameterSets にグループ化されている Parameters を伴う
  Behavior や Operation を発動する CallAction には特別な規則も併せて適用する。

  * Behavior や Operation が入力 ParameterSets を持つならば、
    CallAction が実行することが許されるときの 16.2.3 節の規則が、
    各入力 ParameterSet にある Parameters に対応している
    InputPins の（多分に重なり合う）集合に個別に適用される。

  * Behavior や Operation が出力 ParameterSets を持ち、
    かつ CallAction が正常完了するならば、
    その CallAction はある出力 ParameterSet に対応している
    OutPins 上にのみ、
    これらの OutPins の多重度の下限値に見合う出力を生じなければならない。
    かつ、オブジェクトトークンがこれらの OutputPins から流出している ActivityEdges に差し出される。

16.3.3.2 Send Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* 送信系 Action は目標オブジェクト (pl.) にオブジェクト (s.) を
  非同期的に伝えるものである。

* 次の 3 種類の送信 Actions がある。

  #. SendSignalAction は Signal オブジェクトを生成してそれを
     目標の InputPin で与えられるオブジェクトに伝える InvocationAction である。

  #. BroadcastSignalAction は SendSignalAction 同様に、
     Signal オブジェクトを生成する InvocationAction である。
     ただし生成オブジェクトをシステム内のすべての利用可能な目標に伝達する。

  #. SendObjectAction は目標の InputPin で与えられるオブジェクトに向けて
     任意の種類のオブジェクトを伝える InvocationAction である。

* SendSignalActions と BroadcastSignalActions は、
  argument InputPins は命令により送信される Signal の Properties に match される。

* 送信系 Action の目標オブジェクト (s./pl.) は局地にあっても遠隔地にあっても構わない。

.. 16.3.3.3 Invocation Actions and Ports

* CallOperationAction, SendSignalAction, SendObjectAction は
  Port を通じて要求を送信する。

* もし onPort が与えられるならば、
  その Port はその Action の target InputPin の type の、
  所有されたまたは継承された feature である必要がある。

* ある Action があるオブジェクトの内側で実行するとは、
  その Action が内部で実行している Behavior 実行の context オブジェクトが
  次のどちらか一方であるときに言われる。

  * 与えられたオブジェクトと同じである
  * 与えられたオブジェクトに（合成リンクによる推移的関係性の意味で）
    直接・間接的に所有される

* CallOperationAction の場合には、
  与えられた Port の provided または required Interface は
  呼び出される Operation を feature として持つ必要がある。

  * ここは長いので後回し。

* onPort を指定していない CallOperationAction, SendSignalAction, SendObjectAction は、
  目標オブジェクトとして「相互作用点」
  （つまり Port で生成したオブジェクト）オブジェクトを用いることもできる。

16.3.4 Notation
----------------------------------------------------------------------
* Figure 16.14 Calling a Behavior

  * CallBehaviorAction の記法は発動される Behavior の名前を持つ
    Action シンボルと同じようにする。
    もし Action の名前が Behavior のそれと異なる場合は、
    代わりに Action 名がシンボルに現れなければならない。

  * Behavior の事前条件と事後条件を先の例と同様に示すことが可能である。
    その際にはキーワード ``«precondition»`` と ``«postcondition»`` を用いる。

* Figure 16.15 Calling an Activity

  * Activity の呼び出しは Action シンボルの内部に逆さのフォークみたいなものを描いて示す。
  * 右側の記法は前章で紹介済み。

* Figure 16.16 Calling an Operation

  * CallOperationAction の記法は CallBehaviorAction とほぼ同様。
    Behavior を Operation に置き換えて理解すればよい。

* Figure 16.17 Calling an Operation, showing the owner name

  * Operation の所有者の名前を任意で Operation の名前の下に見せてよい。
    ``(OwnerClassName::)`` または ``(OwnerClassName::OperationName)``
    の形式の文字列とする。

* Figure 16.18 Sending a Signal

  * SendSignalAction はその名前を内側に配した凸五角形として記す。
    右側が凸。

  * SendObjectAction が常にある Signal を送信することになるように用いられるならば、
    SendSignalAction の記法がその SendObjectAction を表すために利用が可能である。

* Figure 16.19 Exception Pin annotations

  * isException が真である Parameters に対応する Pins は、
    小さい三角形を source 側に示す。

  * Pin の小矩形が省略されているときにも三角形は記す。

* Figure 16.20 Effect Pin annotations

  * Pin に対応する Parameter が指定された effect を持つならば、
    この内容を中括弧に括って、Pin それぞれのエッジのそばに記す。

* Figure 16.21 Stream Pin annotations

  * Pin に対応する Parameter の isStreaming の値を、
    Pin の近くに ``{stream}`` または ``{nonstream}`` で示す。

  * これらが省略されている場合は ``{nonstream}`` であるものとする。

* Figure 16.22 Stream Pin annotations, with filled arrows and rectangles

  * streaming Parameters を示すためにには、さらなる強調を付加してよい。

    * スタンダロンな Pins に接続している矢印の矢先を黒く塗りつぶしてよい。
    * さもなければ Pins 自体を黒く塗りつぶしてよい。

* Figure 16.23 Alternative input/outputs using ParameterSet notation

  * ParameterSet が Pins をグループ化することを示すのに、
    複数 Pins の矩形らを囲む矩形で記す。

  * 引数の AND と OR をこれで見分けるらしい。

16.3.5 Examples
----------------------------------------------------------------------
* Figure 16.24 Invoking an Activity

  * FillOrder という Activity を発動する CallBehaviorAction である。
    逆さフォークに注意。

* Figure 16.25 Sending Signals

  * 何か発注処理のワークフローの一部を示す図式。
  * 五角形の Action で Signal が送信されるが、
    されるということ以外の情報は図からは得られない？

* Figure 16.26 Streaming Pin examples

  * ``{stream}`` のついた Pin の Action は連続的 Behavior と見るのがよさそう。

* Figure 16.27 Exception Pin examples

  * 上のコースは例外送出ケース。

* Figure 16.28 Pin example with effects

  * 中括弧は effect を示す。
  * Place Order が ``Order`` を ``{create}`` して、
    Fill Order が ``Order`` を ``{read}`` する。

* Figure 16.29 Alternative input/outputs using ParameterSets

  * Ship Item の InputPins が（それぞれが）グループ化されているので、
    どちらか一方でも受信すれば Action を開始する。

16.4 Object Actions
======================================================================

16.4.1 Summary
----------------------------------------------------------------------
* オブジェクト Actions は Classifiers のオブジェクトの
  生成、破壊、比較を取り扱う。

* 与えられた Classifier のオブジェクトの読み取りや、
  あるオブジェクトの分類の確認、
  さらに分類の変更をする Actions をも含む。

16.4.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 16.30 Object Actions

  * 10 個近くの派生 Actions がある。
  * 注意深く見ると、InputPin と OutputPin のどちらかしか持たないものと、
    両方を持つものがあることに気づく。

16.4.3 Semantics
----------------------------------------------------------------------
16.4.3.1 Create Object Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* CreateObjectAction は与えられた Classifier の直系オブジェクトを生成し、
  その新しいオブジェクトを result OutputPin 上に配置する Action である。

* もしオブジェクト化される Classifier が Behavior ならば、
  その生成オブジェクトがその Behavior の実行である。
  ただしその実行は生成時にすぐに自動的に開始することはない。

16.4.3.2 Destroy Object Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* DestroyObjectAction とはその対象の InputPin にあるオブジェクトを破壊する Action である。

* もし DestroyObjectAction::isDestroyLinks が真ならば、
  そのオブジェクトが関与するリンクは（リンクオブジェクトは除いて）
  DestroyLinkAction の意味に従いそのオブジェクトと一緒に破壊される。

* 既に破壊されたオブジェクトを破壊することは何ら効果はない。

16.4.3.3 Test Identity Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* TestIdentityAction とは、その InputPins に与えられるふたつの値が
  全く同一のものであるかどうかを調べる Action である。

* もしあるオブジェクトがひとつまたはそれ以上の Classes のオブジェクトであると
  単に分類されるならば、それがもう一方の「同じ」オブジェクトであるかどうかを
  調べることは、オブジェクトの同一性に基づき、
  その StructuralFeatures としての現在の値や、
  それが関与するリンクのどれからも独立している。

* Classes にも DataTypes にも分類されるオブジェクトや、
  その他の種類の Classifiers に分類されるオブジェクトに対する
  TestIdentityAction の結果は定義されないが、
  どの場合においても Action は結果として Boolean 値をもたらす。

16.4.3.4 Read Self Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ReadSelfAction とは、その Action の実行の context オブジェクトを
  その result OutputPin に配置する Action である。

* 例えば、もし ReadSelfAction がある Operation のメソッドである
  Behavior に含まれるならば、それが返す context オブジェクトは
  その Operation 発動の対象であった Operation の所有している
  Classifier のオブジェクトになる。

16.4.3.5 Value Specification Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ValueSpecificationAction とは、
  ある ValueSpecification を評価して、
  結果の値をその result OutputPin に配置する Action である。

16.4.3.6 Read Extent Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ReadExtentAction とは、
  ある Classifier の現在の範囲 (extent) にあるオブジェクトを取得して、
  それらをその result OutputPin に配置する Action である。

  * ある Classifier の範囲とは、
    その特殊型を含むある Classifier の、任意の一時点に存在している、
    すべてのオブジェクトの集合のことである。

* どこにでも存在する Classifier のオブジェクトすべてを作り出すことは、
  ReadExtentAction の実装として一般的には実用的ではない。

16.4.3.7 Reclassify Object Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ReclassifyObjectAction とは、
  どの Classifiers がその object InputPin に与えられるオブジェクトを
  分類するのかを変更する Action である。

* その Action が完了する後で、
  入力オブジェクトは各 newClassifier とによって分類されて
  oldClassifier ではない。

* 入力オブジェクトの同一性は維持され、どの振る舞いも実行されず、
  どのデフォルト値の式も評価されない。

* もし isReplaceAll が真ならば、
  ある newClassifier がもうその入力オブジェクトを分類する場合を除いて、
  そのオブジェクトを扱うために存在する Classifiers すべては
  newClassifiers が追加されるよりも前に取り除かれる。

* オブジェクトから Classifiers を全部取り除くことと、
  どのような新しいものをも追加しないことの効果は定義されていない。

16.4.3.8 Read-Is-Classified-Object Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ReadIsClassifiedObjectAction とは
  その object InputPin に与えられたオブジェクトが、
  何か与えられた Classifier によって分類されているかどうかを決定する
  Action である。

* もし isDirect が真ならば、
  調べる内容はそのオブジェクトが指定 Classifier により直接的に分類されるかどうかであり、
  そのどんな特殊化によってではない。
  反対に isDirect が偽ならば、特殊化をも認める。

16.4.3.9 Start Classifier Behavior Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* StartClassifierBehaviorAction とは
  その object InputPin に与えられたオブジェクトの classifierBehavior の
  実行を開始する Action である。

* これは旧版の UML との互換性のために与えられる型である。
  代わりに StartObjectBehaviorAction を用いることが一般には望ましい。

16.4.4 Notation
----------------------------------------------------------------------
* Figure 16.31 ValueSpecificationAction notation

  * ValueSpecificationAction はその ValueSpecification でラベルされる Action として記す。

* その他の種類のオブジェクトアクション固有の記法はない。

16.4.5 Examples
----------------------------------------------------------------------
* Figure 16.32 ValueSpecificationActions

  * 現実味のない見本だが、定数 5 または 6 を出力する Activity である。

16.5 Link End Data
======================================================================

16.5.1 Summary
----------------------------------------------------------------------
* リンクオブジェクトではないリンク、
  つまり AssociationClass のオブジェクトではない Association のオブジェクトは、
  Action に対して実行時の値を引き渡すことが不可能である。

* その代わり、リンクはその関連端の値により識別する。
  LinkEndData とはそういうリンクの（片側の）関連端の値の仕様であり、
  LinkActions で用いられるリンクの識別に用いられる。

16.5.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 16.33 Link End Data

  * ここに登場する新要素は全て Element から直接派生しているのか。

16.5.3 Semantics
----------------------------------------------------------------------
16.5.3.1 Link End Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* LinkEndData とはあるリンクの一端にある値に
  match するのに用いられる入力を指定する Element である。

* 各 LinkEndData には三つの部分がある。

  #. match されているリンクの end の特定
  #. リンクの与えられた end で期待される値を与える value InputPin
  #. リンクの与えられた end の qualifiers の
     期待される値を与える InputPins を特定する、
     選択自由な QualifierValues

16.5.3.2 Link End Creation Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* LinkEndCreationData とは LinkEndData の特殊型のひとつであり、
  CreateLinkAction によって作成されるリンクの一端を特定するのに用いる。

* オプション isReplaceAll は新しいリンクを
  直前にこの端における値に match したリンク全部で置き換えるかどうかを指定する。

* もし与えられた end が順序付きならば、
  type が UnlimitedNatural であり多重度が 1 の
  ある insertAt InputPin が
  この end での順序付き値で新しいリンクの挿入点を与えるように
  指定されていなければならない。

16.5.3.3 Link End Destruction Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* LinkEndDestructionData とは LinkEndData の特殊型のひとつであり、
  DestroyLinkAction によって破壊されるリンクの一端を特定するのに用いる。

* オプション isDestroyDuplicates が真であれば、
  この end の値に match しているリンク全てが破壊される必要があることを指定する。

* もし与えられた end が順序付きかつ非一意であり、
  isDestroyDuplicates が偽であれば、
  type が UnlimitedNatural であり多重度が 1 の
  ある insertAt InputPin が
  破壊されるリンクのこの end での位置を表す値を与えるように
  指定されていなければならない。

16.5.4 Notation
----------------------------------------------------------------------
* LinkEndData 固有の記法はない。

16.5.5 Examples
----------------------------------------------------------------------
なし。

16.6 Link Actions
======================================================================

16.6.1 Summary
----------------------------------------------------------------------
* LinkActions と ClearAssociationAction は
  Associations とそれらのオブジェクト（リンク）に作用する。

16.6.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 16.34 Link Actions

  * ClearAssociationAction が浮いている。

16.6.3 Semantics
----------------------------------------------------------------------
16.6.3.1 Link Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* LinkAction とはある Association のリンクを
  読み取ったり、生成したり、破壊したりする Action である。
  Association は AssociationClass であってもよい。

16.6.3.2 Read Link Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ReadLinkAction とはある Association の一端の値を取得して、
  それらを result OutputPin に配置する LinkAction である。

* ある ReadLinkAction が実行するときに、次のすべてに match する
  Association の存在するリンクすべての部分集合を特定する。

  * その endData オブジェクトの値
  * その open end 以外の端点すべてについての qualifier values
  * その open end における qualifier values

* ReadLinkAction の result OutputPin は
  その open end と型と順序が同じである必要がある。

16.6.3.3 Create Link Action
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* CreateLinkAction とはリンクを作成する LinkAction である。
* CreateLinkAction は LinkEndCreationData という LinkEndData の特殊型を用いる。
* 順序付き端付き Associations は
  LinkEndCreationData の追加の insertAt InputPin により
  実行時に指定される挿入点によって支援されている。

* その insertAt Pin は type が UnlimitedNatural で多重度が 1 である。

* 抽象型の Association を接続するリンクを作成することの意味は未定義である。

* 他の関連端オブジェクトの初期化の後において、
  作成されているリンクが既に存在するわけではない限りは、
  isReadOnly が真である関連端を持つリンクを作成することの意味は未定義である。

16.6.3.4 Destroy Link Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* DestroyLinkAction とは指定された LinkEndData に match しているリンクを
  破壊する Action である。

* DestroyLinkAction はリンクオブジェクトを破壊することに用いても構わない。
  たとえ破壊するオブジェクトがやはり LinkEndData を用いて同様に指定されているとしても。

* DestroyLinkAction は LinkEndDestructionData という LinkEndData の特殊型を用いる。

* 順序付きかつ非一意な端を持つ Associations は、
  LinkEndDestructionData の追加の destroyAt InputPin により
  実行時に指定される削除位置によって支援されている。

* 他の関連端オブジェクトの初期化の後において、
  その endData に match するリンクがない限りは、
  isReadOnly が真である関連端を持つリンクを破壊することの意味は未定義である。

16.6.3.5 Clear Association Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ClearAssociationAction とはある特定のオブジェクトが関与する
  ある Association のリンク全てを破壊する Action であり、
  AssociationClass のリンクオブジェクトを含む。

16.6.4 Notation
----------------------------------------------------------------------
* LinkActions や ClearAssociationActions に特化した記法は定義されない。

16.6.5 Examples
----------------------------------------------------------------------
なし。

16.7 Link Object Actions
======================================================================

16.7.1 Summary
----------------------------------------------------------------------
* リンクオブジェクト Actions はリンクオブジェクトに作用する、
  AssociationClasses のオブジェクトである。

* LinkActions もまたリンクオブジェクトに作用するが、
  それらを違うように見分ける。

16.7.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 16.35 Link Object Actions

  * ReadLinkObjectEndAction と ReadLinkObjectEndQualifierAction は構造が同じ。

16.7.3 Semantics
----------------------------------------------------------------------
16.7.3.1 Read Link Object End Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ReadLinkObjectEndAction とはあるリンクオブジェクトから
  端オブジェクトをひとつ取得する Action である。

16.7.3.2 Read Link Object End Qualifier Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ReadLinkObjectEndQualifierAction とはあるリンクオブジェクトから
  qualifier 端の値をひとつ取得する Action である。

16.7.3.3 Create Link Object Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* CreateLinkObjectAction とは
  リンクオブジェクトをひとつ作成するための
  CreateLinkAction の特殊化である。

16.7.4 Notation
----------------------------------------------------------------------
* リンクオブジェクトに作用する Actions に特化した記法は定義されない。

16.7.5 Examples
----------------------------------------------------------------------
なし。

16.8 Structural Feature Actions
======================================================================

16.8.1 Summary
----------------------------------------------------------------------
* StructuralFeatureActions は StructuralFeatures の読み書きを支援する。

16.8.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 16.36 Structural Feature Actions

  * StructuralFeatureAction から Read, Write, Clear を派生する。
  * Write から Add と Remove を派生する。

16.8.3 Semantics
----------------------------------------------------------------------
16.8.3.1 Structural Feature Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* StructuralFeatureAction とは、
  静的に指定されたある Classifier の StructuralFeature が与えられ、
  その object InputPin にあるオブジェクトに作用するものである。

* オブジェクトが関与する StructuralFeatures と AssociationClasses は動的分類ゆえ
  繰り返し変化してよいが、
  StructuralFeatureAction の object InputPin の型は単一の Classifier であり、
  その Action に引き渡されるオブジェクトが（直接か間接かを問わず）
  その Classifier により分類されているときに限って、その意味が定義される。

16.8.3.2 Read Structural Feature Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ReadStructuralFeatureAction とは
  StructuralFeature の値を取得して、
  それらを result OutputPin に配置する StructuralFeatureAction である。

* result OutputPin の型と順序はその StructuralFeature のそれらと同じである。

16.8.3.3 Add Structural Feature Value Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* AddStructuralFeatureValueAction とは、
  あるオブジェクトの StructuralFeature ひとつに値を追加するのに用いられる
  StructuralFeatureAction である。

* もし isReplaceAll が真ならば、値の追加というよりは交換のようなことをする。

* 順序付き StructuralFeature に値を追加するには、
  insertAt InputPin に与えられる新しい値を置くための挿入点が必要である。
  これが必要なのは isReplaceAll が偽の場合であり、
  順序なしの StructuralFeatures については省略される。

* もし insertAt InputPin があれば、
  それは型が UnlimitedNatural で多重度が 1 である。

* StructuralFeature の上側の多重度に違反する値を追加することと、
  isReadOnly が真である StructuralFeature に対する、
  そのオブジェクトの初期化後に新しい値を追加すること
  の意味は未定義である。

16.8.3.4 Remove Structural Feature Value Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* RemoveStructuralFeatureValueAction とは
  あるオブジェクトの StructuralFeature ひとつから値を取り除くのに用いられる
  StructuralFeatureAction である。

* 後述の場合を除き、取り除かれる値は value InputPin が与えるものであり、
  これはその StructuralFeature と同じ型で多重度が 1 である。

* もし isRemoveDuplicates が偽で、
  かつ StructuralFeature が順序付きで非一意ならば、
  value InputPin はなく、
  代わって取り除かれる値は removeAt InputPin の位置により与えられる。

* 所有しているオブジェクトの初期化以降において、
  readOnly が真である StructuralFeature の既存の値を取り除くことの意味は未定義とする。

16.8.3.5 Clear Structural Feature Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ClearStructuralFeatureAction とは
  たとえその StructuralFeature の多重度の下限がゼロより大きくても、
  StructuralFeature の値全てを取り除く StructuralFeatureAction である。

* StructuralFeature を所有しているオブジェクトの初期化以降において、
  それが値を持っていないのでもない限りは、
  readOnly が真である StructuralFeature の意味は未定義とする。

16.8.4 Notation
----------------------------------------------------------------------
* StructuralFeatureActions に特化した記法は定義されない。

16.8.5 Examples
----------------------------------------------------------------------
なし。

16.9 Variable Actions
======================================================================

16.9.1 Summary
----------------------------------------------------------------------
* VariableActions は Variables の読み書きを支援する。

16.9.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 16.37 Variable Actions

  * 派生のスタイルが先ほどのものと似ている。

16.9.3 Semantics
----------------------------------------------------------------------
16.9.3.1 Variable Action
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* VariableActions は静的に指定された Variable に作用する。

16.9.3.2 Read Variable Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ReadVariableAction とは Variable の値を取得して
  それらを result OutputPin に配置する VariableAction である。

* result OutputPin の型と順序はその Variable のそれらと同じである。

16.9.3.3 Add Variable Value Action
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* AddVariableValueAction とは値を Variable に追加するためのものである。
* もし isReplaceAll が真ならば、Variable に新しい値が追加される前に
  既存の値は取り除かれる。

* 順序付き Variable に値を追加するには、挿入点が必要である。
  必要になるのは isReplaceAll が偽の順序付き Variable に対してであり、
  順序なし Variable では省略される。

* Variable の多重度の上限に違反する値の追加については意味は未定義とする。

16.9.3.4 Remove Variable Value Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* RemoveVariableValueAction とは Variable から値を取り除く VariableAction である。
* 取り除かれる値は value InputPin 上に与えられ、
  それは Variable と同じ型であり多重度は 1 である。

* isRemoveDuplicates が偽であり、なおかつ
  その Variable が順序付きで非一意ならば、
  value InputPin がなく、
  取り除かれる値は removeAt InputPin の指す位置により与えることで指定される。

16.9.3.5 Clear Variable Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ClearVariableAction とは
  たとえその Variable の多重度の下限がゼロより大きくても、
  Variable の値全てを取り除く VariableAction である。

16.9.4 Notation
----------------------------------------------------------------------
* Figure 16.38 Presentation option for AddVariableValueAction

  * 上下に分かれているが、上の方は抽象的構文とする。

* AddVariableValueAction::isReplaceAll が true であることを
  文字列 ``{replaceAll}`` を変数名の近くに置くことで示すことが可能。

16.9.5 Examples
----------------------------------------------------------------------
なし。

16.10 Accept Event Actions
======================================================================

16.10.1 Summary
----------------------------------------------------------------------
* AcceptEventAction はひとつまたはそれ以上の Events の出来事を待機する。
* もし受理した Event の出来事がある CallEvent を要求するものならば、
  ひとつの ReplyAction をそれに返信するのに用いてよい。
* もし受理した Event の出来事がある SignalEvent を要求するものならば、
  受信した Signal オブジェクトは、

  * 直ちにその属性の値へと unmarshal されるか、
  * 後になって UnmarshallAction を用いてそうされるかの一方であってよい。

16.10.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 16.39 Accept Event Actions

  * Action の派生クラスがまだまだ定義されていく。

16.10.3 Semantics
----------------------------------------------------------------------
16.10.3.1 Accept Event Action
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* AcceptEventAction とはひとつまたはそれ以上の Events を引き起こす Triggers を備えた Action である。

* もし AcceptEventAction を起こす Event 出来事の matching が
  イベントプールから発送されるのであれば、
  そのアクションは利用可能になって続行する。

* SignalEvent を引き起こす trigger のある AcceptEventAction は
  非公式に an accept signal action と呼ばれる。

* TimeEvent を引き起こす trigger のある AcceptEventAction は
  非公式に a wait time action と呼ばれる。

* もし AcceptEventAction の triggers がすべて
  ChangeEvents と CallEvents だけを引き起こすものならば、
  AcceptEventAction は result OutputPins を持たない。

  * ただし AcceptEventAction は AcceptCallAction ではないものとする。

* もし AcceptEventAction::triggers のうちのひとつが AnyReceiveEvent であり、
  Event の出来事が同じ AcceptEventAction にある SignalEvent trigger にも
  CallEvent trigger にも match されないメッセージを扱うのならば、
  Event の出来事は AnyReceiveEvent を引き起こす trigger に match する。

* AcceptEventAction が Activity で用いられるのならば、
  それが利用可能になるときを支配するための特別な規則がある。

16.10.3.2 Accept Call Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* AcceptCallAction とは CallEvent の出来事を処理するために特殊化された
  AcceptEventAction である。

* AcceptCallAction は CallEvent の出来事に match すると、
  普通の AcceptEventAction と同じ方法で誘発される。

* 非同期呼び出しにより誘発された AcceptCallAction は、
  やはりその returnInformation OutputPin に値をもたらすが、
  値を受理する ReplyAction は
  非同期呼び出しにとっての戻り値が与えられると、
  何も起こらずに直ちに完了する。

16.10.3.3 Reply Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ReplyAction とは直前の AcceptCallAction によって受理された
  呼び出しの処理を完了する Action である。

* ReplyAction が実行するときに、
  最初の呼び出し要求メッセージに対する返答メッセージを発生する。
  その replyValue InputPins から得られる値が利用される。

* 返答の情報は複製されたり、オブジェクトに格納されたり、引き渡したりしてもよいが、
  ReplyAction の中で一度だけ利用されてよい。

16.10.3.4 Unmarshall Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* UnmarshallAction とはオブジェクトの StructuralFeatures の値を取得して、
  それらを OutputPins に配置する Action である。

* Signal の所有 Properties には順序があるが、
  Generalization 関係ゆえ
  Classifier もまた他の Classifiers から Properties を継承してもよい。
  この場合、unmarshallType の Properties は順序が付けられ、
  所有 Properties すべては継承された Properties のどれよりも先に来るようになる。

* UnmarshallAction が実行するときに、
  その InputPin からオブジェクトを取り、
  オブジェクトから unmarshallType の Properties の値を取得して、
  これらの値を対応する OutputPins に配置する。

* UnmarshallAction は、例えば、
  isUnmarshall が偽である AcceptEventAction により生成された
  Signal オブジェクトの属性値を得るのに有用である。

16.10.4 Notation
----------------------------------------------------------------------
* Figure 16.40 AcceptEventAction notations

  * AcceptEventAction は一般には凹五角形で記される。左側が凹。
    内側にその name を配してもよい。

  * AcceptEventAction が単一の TimeEvent trigger を持つようなものは、
    砂時計みたいな図形で記す。名前を書くならシンボルの下側である。

16.10.5 Examples
----------------------------------------------------------------------
* Figure 16.41 Implicitly enabled AcceptEventAction

  * Cancel order request は何か Signal を受理するアクションである。
  * Signal の受理が Cancel Order の発動をもたらす。

* Figure 16.42 Explicitly enabled AcceptEventAction

  * 見た印象どおりのアクションが起こる。

* Figure 16.43 Repetitive time event

  * End of month occurred が砂時計の左側に書いてある。

* Figure 16.44 UnmarshallAction

  * Unmarshall Order が Name, Address, Product の attributes に分解する。

16.11 Structured Actions
======================================================================

16.11.1 Summary
----------------------------------------------------------------------
* StructuredActivityNode は ActivityGroup でもある Action である。
  つまり、その実行時の振る舞いを定義する ActivityNodes と ActivityEdges を含む。

* StructuredActivityNodes の特殊型、名前を挙げると
  ConditionalNodes, LoopNodes, SequenceNodes らは、
  それらの中にある ExecutableNodes がどのように実行されるのかという、
  それぞれの型固有の制御意味を定義する。

16.11.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 16.45 Structured Actions

  * StructuredActivityNode は Namespace, Action, ActivityGroup から派生している。
  * その派生型に ConditionalNode, LoopNode, SequenceNode がある。

16.11.3 Semantics
----------------------------------------------------------------------
16.11.3.1 Structured Activity Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* StructuredActivityNode とは ActivityGroup でもあり、
  その振る舞いがそれが含む ActivityNodes と ActivityEdges とで指定される
  Action である。

* StructuredActivityNode はまた Variables の定義をも含んで構わない。

* StructuredActivityNode は使用可能になり、
  Action に関する通常の規則に則った実行を始める。

* StructuredActivityNode の InputPins は、
  これに含まれている ActivityEdges へ至る sources であることが許されている。

* 同様にして、StructuredActivityNode の OutputPins は、
  これに含まれている ActivityEdges の targets であることが許されている。

* StructuredActivityNode に含まれている ActivityEdge は必ず
  エッジの source と target の両者を持ち、それらは

  * StructuredActivityNode に（直接的にでも間接的にでも）含まれるか、
  * StructuredActivityNode に所有される Pin であるものとする。

* もし ActivityEdge の source が StructuredActivityNode の外部にあり、
  target がその内部にあるならば、そのエッジに差し出された物はどれでも、
  StructuredActivityNode が実行を始めるまでは保留されたままになる。

* もし ActivityEdge の source が StructuredActivityNode の内部にあり、
  target がその外部にあるならば、
  StructuredActivityNode が実行しているのではない限り、
  そのエッジには何物も差し出されることはない。

* StructuredActivityNode は Activity の実行の完了にまつわる同じ規則に
  従って実行を完了する。

* StructuredActivityNode がその実行を完了するときに、
  その内部へと進出している実行はすべて停止されて、
  それに含まれるトークンはすべて破壊されるが、
  StructuredActivityNode の OutputPins にある、
  つまり outgoing エッジに向けて差し出されているものは例外とする。

16.11.3.2 Isolation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Behaviors の内側にあったりまたがったりする Actions の実行に備わっている
  concurrent な本質のため、オブジェクトメモリへのアクセスと変更に
  一貫性を保証することは難しくなる可能性がある。

* もしフラグ StructuredActivityNode::mustIsolate が真ならば、
  ノード内部にある Action によるオブジェクトへのどのアクセスも
  ノード外側にある Action によるオブジェクトへのアクセスと
  衝突してはならない。

  * 独立性は不可分性の性質とは異なる。
    後者は Actions のグループが全て正常完了するか、
    全く効能がないかのどちらかを保証するものである。

16.11.3.3 Conditional Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ConditionalNode とは ExecutableNodes の選択対象である集まりの
  いくつかの中から選択して実行する StructuredActivityNode である。

* ConditionalNode が実行を始めるときには、
  その内部にある InitialNodes のどれもが直ちに利用可能となる。

* いったん ConditionalNode が実行中になると、
  predecessorClauses を持たない Clauses のどんな test セクションも実行される。

* もし ConditionalNode::isAssured が真であるならば、
  これは少なくともひとつの test セクションは真を返すことを断言する。

* いったん test セクションの実行手順が終わると、
  もし実行可能な body セクションが厳密にひとつあれば、
  その body セクションは実行される。

* else Clause とは ConditionalNode にあるその他の節全ての後ろにあり、
  その test セクションの結果が常に真となる Clause である。

* body セクションが実行可能状態になるときにはいつでも、
  それ以上の test セクション実行の完了よりも前に本当に実行される。

* ConditionalNode は result OutputPins の順序付き集合を持つ。

* いったん ConditionalNode が実行を完了すると、
  内部で進行中の実行全てが停止されて、
  その内部にあるトークンすべては破壊される。

* ConditionalNode が InputPins を持つことは認められない。

16.11.3.4 Loop Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* LoopNode とは反復的なループを表現する StructuredActivityNode である。

* LoopNode が実行を始めると、その内部にある InitialNodes はどれもが
  直ちに利用可能になる。

* まず LoopNode::setupPart が実行される。
  それが実行を完了するときに、ループの反復的な実行が始まる。

* test セクションには
  LoopNode により見分けられる Boolean 型の
  decider OutputPin を所有している Action がある。

* bodyPart の実行それぞれの後に、
  ループの次の反復に備えて再び test セクションが実行される。

* LoopNode は
  各反復の間に現れる途中の値を保持するのに用いられる
  loopVariable OutputPins の集合を定義することも許される。

* LoopNode が実行を始めるときに、
  ループの初回反復に先立って
  loopVariableInput InputPins にあるトークンは
  対応する loopVariable OutputPins に移される。

* LoopNode に上で述べた以外の InputPins と OutputPins が
  あることは許されない。

16.11.3.5 Sequence Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* SequenceNode は完全な、
  それが含む全ての ActivityNodes の順序を定義する。
  なお ActivityNodes は全て ExecutableNodes であるものとする。

16.11.4 Notation
----------------------------------------------------------------------
* Figure 16.46 Notation for StructuredActivityNode

  * StructuredActivityNode 自体は破線丸角矩形で記す。
  * 矩形上部にキーワード ``«structured»`` を添える。
  * 矩形内に nodes と edges を同封する。

* ConditionalNode, LoopNode, SequenceNode には標準的な記法は定義されない。

16.11.5 Examples
----------------------------------------------------------------------
なし。

16.12 Expansion Regions
======================================================================

16.12.1 Summary
----------------------------------------------------------------------
* ExpansionRegion は入力コレクションの要素に対応している、
  それが含む要素を複数回実行する StructuredActivityNode である。

16.12.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 16.47 Expansion Regions

  * ExpansionRegion と ExpansionNode だけ。
  * ExpansionKind という enumeration がある。

16.12.3 Semantics
----------------------------------------------------------------------
* ExpansionRegion とは値のコレクションのひとつまたはそれ以上を入力として取り、
  それらの値それぞれに対して包含する ActivityNodes と ActivityEdges を実行する
  StructuredActivityNode である。

* ExpansionNode とは ExpansionRegion の境界を超えていく流れを指示するのに用いられる
  ObjectNode である。

* ExpansionRegion に入力 ExpansionNodes が複数あれば、
  異なるコレクションにある要素の種類が変化することが許されているけれども、
  それぞれは同種のコレクション（集合、バッグ、その他）を処理するものとする。

* ExpansionRegion は Action の通常の規則に則って実行を始める。

* ExpansionRegion に包含されている ActivityNodes と ActivityEdges の
  グループは入力コレクションの要素それぞれについて一度だけ実行される。
  これらは ExpansionRegion の expansion executions と呼ばれるものである。

* 一般の StructuredActivityNode の実行と同じ意味の下に、
  各 expansion execution はその他の実行とは独立して進行するが、
  次の特別な規則は除外される。

  * 各 expansion execution 内部では、単一のトークンは
    ExpansionRegion の内側にある source と target のように
    入力 ExpansionNode のついている ActivityEdge それぞれに差し出される。

  * 各 expansion execution は結果として
    ExpansionRegion の内側にあるその source と
    その target としての出力 ExpansionNode とを持つ
    ActivityEdge に差し出されるトークンをもたらしてよい。

  * ExpansionRegion の InputPins 上に配置されたトークンは
    expansion execution それぞれに複製されて、
    InputPins から流出する ActivityEdges 上にあるトークンの
    異なるコピーを各 expansion execution は差し出される。

  * ExpansionRegions はその内側から ExpansionRegion の外に交わる
    OutputPins と ActivityEdges を持ってよい。

* ExpansionRegion が増設物の実行すべてを完了するときには、
  出力コレクションをその出力 ExpansionNodes に差し出す。

* ExpansionRegion::mode はその増設部の実行がどのように進行するかを制御する。

  * parallel: 増設部の実行は concurrently に進行する。
    ただし concurrent の意味はいつものように解釈すること。

  * iterative: 増設部の実行は反復的な順序で起こるものとする。
    あるものが完了してから他のものが始まることが可能になる。

  * stream: 厳密にひとつの増設部の実行があり、
    値はコレクションそれぞれからの流れにより、この実行に差し出される。

16.12.4 Notation
----------------------------------------------------------------------
* Figure 16.48 Expansion Region

  * ExpansionRegion は破線丸角箱で記す。
  * 箱の左上に ExpansionKind の値に対応するキーワード ``«parallel»``, etc. を添える。
  * 入力と出力の ExpansionNodes は小さい短冊のようなシンボルで記す。
    これらは箱の枠上に配置する。
  * ExpansionRegion の内側と外側にある ActivityEdge 矢印は
    入力と出力のノードを見分けることができる。

* Figure 16.49 Shorthand notation for expansion region containing single node

  * 速記法として、リストボックス記法を Action シンボルで直接配置してよい。

* Figure 16.50 Full form of previous shorthand notation

  * 上の見本を完全版で示すとこうなる。

* Figure 16.51 Notation for expansion region with one behavior invocation

  * 単一の CallBehaviorAction を含む ExpansionRegion に採用可能なさらなる速記例。
  * キーワードを使う代わりに ``*`` を右上に記す。複数実行を含意している。

16.12.5 Examples
----------------------------------------------------------------------
* Figure 16.52 Expansion region with two inputs and one output

  * ふたつの入力とひとつの出力を持ち、parallel に実行される ExpansionRegion の見本。
  * 両方のコレクションには同数の要素を持つことを期待している。
  * 内側は入力コレクションの各要素について一度実行される。

* Figure 16.53 Expansion Region

  * ある高速 Fourier 変換計算の断片が ExpansionRegion を含んでいる見本である。

* Figure 16.54 Examples of expansion region shorthand

  * 航空券の予約とホテルの予約が独立かつ parallel である。

* Figure 16.55 Shorthand notation for expansion region

  * Specify Trip Route が複数の Book Flight アクションに帰着することを示す。

16.13 Other Actions
======================================================================

16.13.1 Summary
----------------------------------------------------------------------
* 本節では ReduceAction と RaiseExceptionAction を扱う。
* ReduceAction とはあるコレクションの値らを単一の値にまで縮合するために
  ひとつの Behavior を繰り返し発動する Action である。
* RaiseExceptionAction は例外を送出するための Action である。

16.13.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 16.56 Other Actions

  * ReduceAction は InputPin と OutputPin を両方持つが、
    RaiseExceptionAction は InputPin だけを持つ。

16.13.3 Semantics
----------------------------------------------------------------------
16.13.3.1 Reduce Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ReduceAction とは、
  コレクションの要素を合体して単一の値に縮合する Action である。

* ReduceAction は入力コレクションの中間生成コピーの
  reducer Behavior を繰り返し発動することで実行する。

* 入力コレクションが順序なしであるか、
  または InputPin::isOrdered が偽であれば、
  中間生成コレクションのどの要素が reducer の実引数として選択されたのかが
  不確定となる。

* もし reducer Behavior が可換律かつ結合律を満たす操作であれば、
  順序なしコレクションは ReduceAction の結果を左右しない。
  このことは、
  縮合計算がどのように実行されてよいのかということにかなりの自由さを与える。

* その発動がお互いに影響するような副作用が reducer Behavior にあれば、
  isOrdered が偽である ReduceAction の結果は予測不能であって構わない。

16.13.3.2 Raise Exception Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* RaiseExceptionAction とは例外を発生させる Action である。
  正常に終了するというよりは、常に例外を送出することで完了する。
  execption という InputPin において与えられた値が例外として送出される。

* RaiseExceptionAction 送出された例外に match する ExceptionHandler を
  自分で持つならば、例外はそのハンドラーによって捕捉される。
  そうでなければ、例外はいちばん内側から外側に向かって拡がっていく。

* 例外が StructuredActivityNode の外に伝わるときには
  （ノードにおける ExceptionHandler によって捕捉されている場合も含み）、
  その StructuredActivityNode は停止する。

* RaiseExceptionAction が実行された Behavior の中にある
  ExceptionHandler のどれによっても例外が捕捉されなければ、
  Behavior の実行は停止される。

16.13.4 Notation
----------------------------------------------------------------------
* ReduceActions と RaiseExceptionActions に特化した記法は定義されない。

16.13.5 Examples
----------------------------------------------------------------------
* ReduceAction の例として整数の和をとる演算を reducer として挙げている。
  整数の組 (2, 7, 5, 3) を入力コレクションと仮定すると、
  結果は 11 になるだろう。

* isOrdered が偽の場合はオペランドをどの順で reduce してもよい。

16.14 Classifier Descriptions
======================================================================
機械生成による節。

16.15 Association Descriptions
======================================================================
機械生成による節。

.. include:: /_include/uml-refs.txt
