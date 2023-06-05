======================================================================
16 Actions
======================================================================

.. admonition:: 読者ノート

   現在ノート修正中。

.. contents::
   :depth: 2

16.1 Summary
======================================================================

* Action とは UML に挙動の指定の基本的な単位である。Action は入力の集合を取り、
  出力の集合を生じるが、その集合の一方または両方がからであってもよい。 Action が
  実行するシステムの状態を変更する Actions もあってよい。
* Actions は Behaviors に、特に Activities と Interactions に含まれている。これ
  らの Behaviors は Actions がいつ実行するのかと、それらにある入力が何であるかを
  決定する。

16.1.1.1 Concrete Syntax
----------------------------------------------------------------------

.. note::

   節番号のレベルがおかしいのは原書通り。

* UML 仕様は Actions を表す図表的表記法の相対的に極小な集合を実現する。

  * 準拠ツールはツール固有の標準の Action 抽象的構文へ写像する図表的またはテキス
    ト的表現を備えてよい。そのような表現は具象的構文と呼ばれる。

* 具象的構文は高水準の構成要素を UML 抽象的構文で指定された Actions へ写像するこ
  とが可能である。
* 当仕様でのもっとも原始的な Actions は、具体的構文の写像の最大範囲を使用可能に
  するために定義されている。

16.1.1.2 Execution Engines
----------------------------------------------------------------------

.. note::

   節番号のレベルがおかしいのは原書通り。

* 実行機関 (an execution engine) とは UML Actions を実行する道具のことである。
  Actions はさまざまなやり方の特徴があるさまざまな実行機関の構成要素を使用可能に
  するために定義される。
* モデル作者は、その実行を最適化するの価値があるかもしれない領域解決法の特別な知
  識が彼らにあるときに、実行機関に対してヒントを与えることが可能である。
* Actions の実行が実行時の挙動を強制する UML の構造的意味の様相に違反するときは、
  Actions の意味は未定義のままとする。

16.2 Actions
======================================================================

16.2.1 Summary
----------------------------------------------------------------------

* 本節では Actions および Pins の初歩的な抽象構文について定義する。Pins は
  Actions に対する入力と出力を指定するのに用いられる。OpaqueAction 以外は、
  Actions の諸々の具象型は後続の節で述べる。

16.2.2 Abstract Syntax
----------------------------------------------------------------------

* Figure 16.1 Actions

  * Action は抽象型で、ExecutableNode から派生している。

    * この図式では差し当たり OpaqueAction が Action の一つの具象型であることを表
      している。
    * InputPin と OutputPin とに別々に関連させる。

  * Pin という ObjectNode と MultiplicityElement からの派生要素がある。

    * Pin には InputPin と OutputPin の二つがある。
    * InputPin には ActionInputPin と ValuePin の二つがある。ActionInputPin は
      Action を、ValuePin は ValueSpecification をそれぞれ関連させる。

16.2.3 Semantics
----------------------------------------------------------------------

16.2.3.1 Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Action とは Behavior に直接的または間接的に含まれる、実行可能機能の基本的な単
  位である。 Action の実行はモデル化されたシステムにおけるある変換や過程を表す。
  システムは計算機システムであるか、さもなければ別のシステムである。

  * Action の実行は別の Behavior の発動をも引き起こしてよい。

* Action を含んでいる Behavior に背景となる BehavioredClassifier があれば、その
  BehavioredClassifier はその Action に対する ``context`` Classifiers でもある。
* Action の InputPins と OutputPins が指定するように、Action は入力を受け付け、
  出力を生じる。 Action の Pin それぞれが、その Action の固有の入力または出力に
  ついての型および多重度を指定する。
* Action が実行する時間と、各実行が受け付ける入力が何であるのかは、Action の種類
  と、InputPins の特徴と、それが使われる Behavior とによって決定される。いったん
  Action が実行することが決定されるとその実行に対する一般的な手順は次の通りであ
  る：

  #. Action の実行は、その Action の InputPins すべてにおける入力データを、
     InputPin それぞれについての多重度 ``upper`` 個まで (up to) 消費する。
  #. Action はそれが完了するまでは実行を続行する。実行の詳細な意味と完了の定義は
     実行される Action の種類に依存する。
  #. 完了したら、Action の実行は OutputPins における出力データのどれでもを求め
     て、停止する。

* Actions の意味の仕様上、Behaviors は同じ種類の Action を複数回再利用すること
  が許されていて、Action の意味は用法のそれぞれに別個に適用する。
* Action が局所的に再入可能でない (``isLocallyReentrant == false``) ならば、一つ
  を超える実行が任意の時点において含んでいるBehavior の単独の実行内には存在する
  ことは許されない。
* 非再入可能 Behavior (``isReentrant == true``) に対する CallAction もまた、その
  活動に対する ``isLocallyReentrant`` 特性の値が何であれ、あたかもCallAction が
  局所的に非再入可能であるかのように振る舞うはずである。
* Action についての ``localPrecondition`` と ``localPostcondition`` は、Action
  の実行が開始するときと終了するときにそれぞれ成り立つべき Constraints である。
  ``localPrecondition`` または ``localPostcondition`` はモデル作者が定義する
  Constraint であるので、違反とは UML Action 実行の意味が未定義であることではな
  い。

16.2.3.2 Opaque Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* OpaqueAction とは、その仕様が UML 外のテキスト的な具体的構文で与えられてよい
  Action である。何か他の種類の Action が選ばれる前に OpaqueAction を一時的な代
  用として使ってもよい。
* OpaqueAction には、その Action の挙動を指定する代用法を表すテキスト Strings の
  列で構成される ``body`` がある。``language`` Strings の対応する列を、その
  ``body`` Strings のそれぞれが解釈されることになる言語を指定するのに使ってよ
  い。言語を ``body`` Strings と順番に一致する。
* OpaqueAction に一つを超える ``body`` があれば、``bodies`` のどのものも
  OpaqueAction の挙動を決定するのに使われる可能性がある。その選択がどうなされる
  かについては UML は決定しない。

16.2.3.3 Pins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Pin とは Action についての入力と出力を表現するものである。

  * InputPin が入力を表し、一方 OutputPin が出力を表す。
  * Action に所有される入力と出力の集合のそれぞれは順序付いている。
  * Action の InputPins と OutputPins は Action の種類により決定される。

* Pin は ObjectNode の一種なので、指定された Type の値を含むオブジェクトトークン
  を保持する。

  * Action の InputPin のトークンに保持される値は Action の実行に対する入力デー
    タを与え、Action の実行から生じた出力データはオブジェクトトークンに包み込ま
    れて、Action の OutputPins に置かれる。

* Pin は属性 ``ordering`` を ObjectNode から、属性 ``isOrdered`` を
  MultiplicityElement から両方継承する。これらの属性の値は独立に定めてよい。

  * 例えば ``isOrdered`` が ``true`` で ``ordering`` が ``FIFO`` であると、
    MultiplicityElement と同じ順序で Pin から値が取られるはずである。

* InputPin とは Action が消費する入力値を保持する Pin である。
* OutputPin とは Action がもたらす出力値を保持する Pin である。
* ValuePins と ActionInputPins は InputPins であるが、Action が実行可能であるか
  どうかの決定では用いられない。
* ValuePin は ValueSpecification を評価することで値を与える。Action が他の手段に
  よって使用可能であると、ValuePin の ValueSpecification が評価されて、その結果
  が実行を開始するときの Action に対する入力として求められる。
* ActionInputPin は別の Action を実行することで値を与える。Action が他の手段に
  よって使用可能であると、Action が所有する ActionInputPins のどの
  ``fromActions`` もまた使用可能になる。

16.2.3.4 Actions and Pins in Activities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Action が（ということは Pins も）が Activity に含まれるならば、いつトークンが
  Pins に出入りするのかと、いつその Action が実行するのかは、Actions はもちろん
  のこと Activities の意味によって決定する。
* Activity にある Action を実行することは、その InputPins すべてが、それらの最小
  の多重度が指定するとおりに、必要なトークンすべてを与えられることになることを必
  要とする。
* Activity にある Action が実行を完了すると、その OutputPins に配置された出力
  データについてのオブジェクトトークンは、Pins から出ている ``outgoing``
  ObjectFlows のどれに与えられてもよい。
* Action が局所的に再入可能ではない (``isLocallyReentrant == false``) ならば、
  いったん実行を開始すると、その Action および InputPins は実行が終了するまでは
  与えられるトークンをどれも受け付けない。
* 制御 Pin (``isControl == true``) には制御の種類があるもの (``isControlType ==
  true``) とする。そうすることで ControlFlows と一緒に使ってよくなる。

16.2.4 Notation
----------------------------------------------------------------------

* 本節では Activities で使われる Actions を表す図表的表記法を指定する。この表記
  法は準拠ツールがテキスト上の具象的構文を代わりに使えるという点で選択自由であ
  る。

16.2.4.1 Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Figure 16.2 Action

  * Actions は丸角矩形を用いて示す。
  * Action の名前や他の説明が記号中に現れてよい。
  * Actions の派生型に特化した記法は後続の節で述べる。

* Figure 16.3 Local pre- and post-conditions

  * 局所的な事前条件と事後条件はそれぞれキーワード ``«localPrecondition»`` と
    ``«localPostcondition»`` が付いた発動に取り付けられた註釈として示す。

16.2.4.2 Pins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Figure 16.4 Pin notations

  * Pins は ObjectNodes なので、矩形として記す。矩形は所有されている Action 記号
    に取り付けられている小さい矩形として記される。
  * Pin の名前をその付近に表示してもよい。単に型だけを見せることがよくある。両者
    を示すには ``name: type`` のようにラベルする。
  * Action の Pins は、モデル内にそれが存在しているときでさえ、記法の省略が許さ
    れている。

* Figure 16.5 Pin notations, with arrows

  * InputPins と OutputPins を区別する ActivityEdges が存在しないときには、任意
    で矢印を Pin 矩形の内部に配置しても構わない。
  * InputPins には Action の方向を指し示す矢印があり、OutputPins には Action か
    ら離れる方向を指し示す矢印がある。

* Figure 16.6 Standalone Pin notations

  * ある Action の OutputPin が ObjectFlow を介して別の Action の同名の InputPin
    に接続している状況では、この図のようなオプションの記法で示すことが許される。
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

  * あるツールに固有の具体的構文で表現されたアクションらしい。ループ処理を一つの
    Action で表してよいようだ。

* Figure 16.9 Example of an action with local pre- and post-conditions

  * ``Dispense Drink`` という Action の事前条件と事後条件が詳細に記された例。飲
    み物が自販機から出る前後の状態が普通の英語で仕様化されている。

16.2.5.2 Pins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Figure 16.10 Pin examples

  * 目を引くのは ``{stream}`` や角括弧付きのラベル。

* Figure 16.11 Specifying selection behavior on an ObjectFlow

  * Pin は ObjectNode なので ``selection`` の指定が可能。

* Figure 16.12 Example abstract syntax model showing the use of ActionInputPins

  * ``self.foo->bar(self.baz)`` なるテキストによる具体的構文の式を UML 抽象構文
    式で示したもの。

16.3 Invocation Actions
======================================================================

16.3.1 Summary
----------------------------------------------------------------------

* InvocationAction とは、直接的または間接的に Behavior の発動に帰する Action で
  ある。
* InvocationActions には、Operations または Behaviors を呼び出すもののと、以前オ
  ブジェクト化された Behaviors を開始するものとのCallActions がある。
* さらなる InvocationActions の種類には次を考慮したものがある：

  * 信号とその他のオブジェクトの狙いを付けた送信
  * 利用可能な受信者に向けて信号を一斉送信する能力

16.3.2 Abstract Syntax
----------------------------------------------------------------------

* Figure 16.13 Invocation Actions

  * 抽象型 InvocationAction から派生する型がいくつかある。概要に書いてあるとおり
    のクラス図。

16.3.3 Semantics
----------------------------------------------------------------------

16.3.3.1 Call Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* CallAction とは、Behavior または Operation を呼び出す InvocationAction であ
  る。次の三種類が存在する：

  #. CallBehaviorAction とは、直接 Behavior を発動する CallAction であり、
     Behavior の発動を代わる代わる引き起こす BehavioralFeature を呼び出すことで
     はない。
  #. CallOperationAction とは、Operation 呼び出し要求メッセージを対象オブジェク
     トに伝達する CallAction であり、伝達先では関連 Behavior の発動を引き起こし
     てよい。
  #. StartObjectBehaviorAction とは、直接オブジェクト化された Behavior か、ある
     オブジェクトの ``classifierBehavior`` のどちらか一方の実行を開始する
     CallAction である。

* CallAction は直接的にか、またはある Operation 呼び出しのを通じてのどちらかで、
  同期的または非同期的に Behavior 発動に帰する。

  * 呼び出しが同期的 (``isSynchronous == true``) ならば、発動された Behavior の
    実行が（正常にかどうかを問わず）完了するまでその Action の実行は完了しない。
  * 呼び出しが非同期的 (``isSynchronous == false``) ならば、その Action の実行は
    その Behavior が発動されるとすぐに完了する。

* CallAction が発動する Behavior が再入可能でなければ、それの一つを超える実行は
  与えられた時点のどこにおいても存在しないものとする。
* Behaviors と Operations には所有される Parameters の全順序リストがあり、その順
  序を用いてこれらの Parameters を CallAction の Pins に一致する。
* CallAction を実行すると、その ``argument`` Pins にある値を、対応する入力
  Parameters で発動される Behavior または Operation に引き渡す。
* Parameters のどれもが ``streaming`` (``isStream == true``) ならば、その呼び出
  しは同期的であるものとする。 :doc:`./ch13-common-behavior` も参照。
* Actions についての実行規則に加えて、次の規則が ``streaming`` Parameters を伴
  う、Behavior や Operation を発動する CallAction に適用する。

  * 通常の規則によって CallAction が実行が可能となるのに先立って、CallAction に
    対する InputPins のすべては Pin それぞれの多重度下限値以上の個数の値を与えら
    れるものとする。
  * CallAction が正常に実行を完了することが可能になる前に、ある ``streaming``
    Parameter に対応している CallAction の ``argument`` Pin それぞれの多重度下限
    値以上の個数の値が受理されなければならない。
  * 発動された Behavior の実行が正常に完了する前に、少なくとも CallAction の
    ``result`` Pin それぞれの多重度下限に等しい個数の値がその実行が完了するまで
    の時間内に post されなければならない。
* ParameterSets にグループ化されている Parameters を伴う Behavior や Operation
  を発動する CallAction には特別な規則も適用する。

  * Behavior や Operation に入力 ParameterSets があれば、CallAction が実行するこ
    とが許されるときの 16.2.3 節の規則が、入力 ParameterSet それぞれにある
    Parameters に対応しているInputPins の（重なり合うこともある）集合に個別に適
    用される。

  * Behavior または Operation に出力 ParameterSets があり、かつ CallAction が正
    常完了するならば、その CallAction はある出力 ParameterSet に対応している
    OutPins 上にしかこれらの OutPins の多重度の下限値に見合う出力を生じないのと
    する。かつ、オブジェクトトークンがこれらの OutputPins から流出している
    ActivityEdges に与えられる。

16.3.3.2 Send Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* 送信 Action とは、オブジェクトを一つまたはそれを超える対象オブジェクトに非同期
  的に伝えるものである。送信 Action は常に非同期的なので、``argument`` 入力は
  あってもよいのだが、``result`` 出力はない。Action はオブジェクトが送信されると
  それが受信されたかどうかに関わらず、すぐに完了する。

* 次の三種類の送信 Actions がある。

  #. SendSignalAction とは Signal オブジェクトを生成してそれを対象の InputPin で
     与えられるオブジェクトに伝えるInvocationAction である。
  #. BroadcastSignalAction とは SendSignalAction 同様に、その ``argument``
     InputPins から取った値を使って Signal オブジェクトを生成する
     InvocationAction である。ただし、Signal オブジェクトを単一の対象オブジェク
     トに送信する代わりに、生成オブジェクトをシステム内の利用可能な対象オブジェ
     クトのすべてに潜在的に伝達する。
  #. SendObjectAction とは対象の InputPin で与えられるオブジェクトに向けてどんな
     種類のオブジェクトでも伝える InvocationAction である。

* SendSignalActions と BroadcastSignalActions の場合、``argument`` InputPins を
  順番に送信されている Signal の Properties に一致する。
* 送信 Action の対象オブジェクトは局所にあっても遠隔地にあってもよい。

16.3.3.3 Invocation Actions and Ports
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* CallOperationAction, SendSignalAction, SendObjectAction には、Port があり、そ
  の Action の ``onPort`` 属性を使って Port を特定するオブジェクトを対象とするこ
  とによって、Port を通じて要求を送信する。
* ``onPort`` が与えられるならば、Port は Action の ``target`` InputPin の
  ``type`` の ``feature`` に所有されるか、それを継承するものとする。
* Action があるオブジェクトの内側で実行するとは、その Action が内部で実行してい
  る Behavior の実行の背景にあるオブジェクトが、次のどちらか一方であるときに言わ
  れる。

  * 与えられたオブジェクトと同じであるか、
  * 与えられたオブジェクトに（合成リンクによる推移的関係性の意味で）直接・間接的
    に所有される。

* CallOperationAction の場合には、与えられた Port の ``provided`` または
  ``required`` Interface には呼び出される Operation が ``feature`` としてあるも
  のとする。``object`` InputPin にそれの ``type`` として Signal がある
  SendSignalAction または SendObjectAction の場合、与えられた Port の
  ``provided`` または ``required`` Interface には特定された Signal に対する
  Reception があってよいが、これは必要とはされない。どちらの場合でも、関連のある
  Operation または Reception は次の規則において、発動された BehavioralFeature と
  呼ばれる。

  * 発動された BehavioralFeature がある ``provided`` Interface にはあって、どの
    ``required`` Interface にもないならば、InvocationAction が実行されると、その
    発動は与えられた Port を通り抜けて、対象の InputPin で与えられたオブジェクト
    で作られ、その受領は節 11.3.3 で述べられたように処理される。

    * このことは、InvocationAction が自身が所有する Ports のうちの一つの
      ``provided`` Interface を通してメッセージを送り戻す可能性がある対象オブ
      ジェクトの内側で実行されることを可能にする。

  * 発動された BehavioralFeature がある ``required`` Interface にはあって、どの
    ``provided`` Interface にもないならば、InvocationAction が対象の InputPin で
    与えられたオブジェクトの内部で実行されていると、節 11.3.3 で述べられたよう
    に、与えられた Port を通って、対象オブジェクトの外部へと転送される。
  * 発動された BehavioralFeature がある ``required`` と ``required`` Interface
    の両方にあるか、または発動された BehavioralFeature がないならば、
    InvocationAction が対象の InputPin で与えられたオブジェクトの内部で実行され
    ていると、発動は与えられた Port を通って対象オブジェクトの外部で作られる。

    * この場合は、InvocationAction が対象オブジェクトの内側で実行すると、その対
      象オブジェクトへメッセージを送り戻すことはできない。そういうメッセージは
      ``required`` Interface を通じて出て行こうとするためである。

* 対象オブジェクトとして「相互作用点」（つまり Port で生成したオブジェクト）オブ
  ジェクトを ``onPort`` を指定することなしに、CallOperationAction,
  SendSignalAction, SendObjectAction に対する対象オブジェクトとして用いることも
  できる。

16.3.4 Notation
----------------------------------------------------------------------

* ``onPort`` の値は特定の InvocationAction を意味する記号の名前文字列にある句
  ``via <port>`` によって示す。

16.3.4.1 Call Behavior Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Figure 16.14 Calling a Behavior

  * CallBehaviorAction は Action 記号の内側に置かれた発動された Behavior の名前
    を有する Action として表記されるものとする。
  * Action の名前が Behavior のそれと異なる場合は、代わりに Action 名がシンボル
    に現れるものとする。
  * Behavior の ``precondition`` と ``postcondition`` をFigure 16.3 と同様にして
    示すことが可能であるが、キーワード ``«precondition»`` と ``«postcondition»``
    を用いる。

* Figure 16.15 Calling an Activity

  * Activity の呼び出しは Action 記号の内部に逆さのフォークみたいなものを置くこ
    とによって示す。
  * 右側の記法は前章で紹介済み。

16.3.4.2 Call Operation Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Figure 16.16 Calling an Operation

  * CallOperationAction は発動された Operation の ``name`` が Action 記号の内側
    に置かれた Action として表記される。
  * Action の ``name`` が空でなく、Operation の名前と異なるならば、Action の
    ``name`` が記号の代わりに現れるものとする。
  * Operation の ``precondition`` と ``postcondition`` を Figure 16.3 と同様にし
    て示すことが可能であるが、キーワード ``«precondition»`` と
    ``«postcondition»`` を用いる。

* Figure 16.17 Calling an Operation, showing the owner name

  * Operation の ``owner`` の ``name`` を任意でOperation の ``name`` の下に見せ
    てよい。``(OwnerClassName::)`` または ``(OwnerClassName::OperationName)`` の
    形式の文字列とする。

16.3.4.3 Send Signal and Send Object Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Figure 16.18 Sending a Signal

  * SendSignalAction は Signal の ``name`` がその内側に置かれた凸五角形として記
    される。

    * 右側が凸。

  * SendObjectAction が常にある Signal を結果的に送信するようになるように用いら
    れるならば、SendSignalAction の記法がその SendObjectAction を表すために利用
    できる。

16.3.4.4 Pin Annotations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Figure 16.19 Exception Pin annotations

  * ``isException`` が ``true`` である Parameters に対応する Pins は、小さい三角
    形が例外ピンから出るエッジの始点を註釈するように示す。

  * Pin の小矩形が省略されているときにも三角形は記す。

* Figure 16.20 Effect Pin annotations

  * Pin に対応する Parameter に ``effect`` が指定されていると、これを ``effect``
    を中括弧に括って、エッジと Pin との接点付近に記す。

* Figure 16.21 Stream Pin annotations

  * Pin に対応する Parameter の ``isStreaming`` が ``true`` であるか ``false``
    であるかを、Pin の近くに ``{stream}`` または ``{nonstream}`` でそれぞれ示
    す。
  * これらが省略されている場合は ``{nonstream}`` であるものとする。

* Figure 16.22 Stream Pin annotations, with filled arrows and rectangles

  * ``streaming`` Parameters を示すためにには、さらなる強調を付加してよい。

    * 単体の Pin に接続している矢印の矢先を黒く塗りつぶしてよい。
    * さもなければ Pins 自体を黒く塗りつぶしてよい。

16.3.4.5 Parameter Sets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* InvocationAction の Pins に出入りしている複数の ObjectFlows は典型的には
  ``"and"`` 条件として扱われる。しかし、時々流れのグループの一つは他のものに対し
  て排他的であるようにできる。これは ParameterSets を使ってモデル化されて、一つ
  またはそれを超える Pins を取り囲む矩形として表記される。

* Figure 16.23 Alternative input/outputs using ParameterSet notation

  * ParameterSet が Pins をグループ化することを示すのに、複数 Pins の矩形らを囲
    む矩形で記す。
  * 入力に対する disjunctive normal form を表している。``"and"`` の流れのグルー
    プ一つが ``"or"`` のグループ分けによって分離されている。

16.3.5 Examples
----------------------------------------------------------------------

16.3.5.1 Call Behavior Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Figure 16.24 Invoking an Activity

  * ``Fill Order`` という Activity を発動する CallBehaviorAction である。逆さ
    フォークに注意。

16.3.5.2 Send Signal Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Figure 16.25 Sending Signals

  * 何か発注処理のワークフローの一部を示す図式。
  * 五角形の Action で Signal が送信されるが、されるということ以外の情報は図から
    は得られない？

16.3.5.3 Pin Annotations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Figure 16.26 Streaming Pin examples

  * ``Order Filling`` は周期的にオブジェクトを放出する連続的 Behavior であり、必
    ずしも完了するものではない。

* Figure 16.27 Exception Pin examples

  * 上のコースは例外送出ケース。

* Figure 16.28 Pin example with effects

  * 中括弧は ``effect`` を示す。
  * ``Place Order`` が ``Order`` を ``{create}`` して、``Fill Order`` が
    ``Order`` を ``{read}`` する。

16.3.5.4 Parameter Sets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Figure 16.29 Alternative input/outputs using ParameterSets

  * ``Ship Item`` の InputPins が（それぞれが）グループ化されているので、どちら
    か一方でも受信すれば Action を開始する。

16.4 Object Actions
======================================================================

16.4.1 Summary
----------------------------------------------------------------------

* オブジェクト Actions は Classifiers のオブジェクトの生成、破壊、比較を取り扱
  う。また、与えられた Classifier のオブジェクトの読み取りや、オブジェクトの分類
  の確認、さらに分類の変更をする Actions をも含む。

16.4.2 Abstract Syntax
----------------------------------------------------------------------

* Figure 16.30 Object Actions

  * 10 個近くの派生 Actions がある。
  * 注意深く見ると、InputPin と OutputPin のどちらかしかないものと、両方があるも
    のがあることに気づく。

16.4.3 Semantics
----------------------------------------------------------------------

16.4.3.1 Create Object Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* CreateObjectAction とは、与えられた Classifier の直系オブジェクトを生成し、そ
  の新しいオブジェクトを ``result`` OutputPin 上に配置する Action である。
* オブジェクト化される Classifier が Behavior ならば、その生成オブジェクトがその
  Behavior の実行である。ただしその実行は生成時にすぐに自動的に開始することはな
  い。

16.4.3.2 Destroy Object Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* DestroyObjectAction とは、その対象の InputPin にあるオブジェクトを破壊する
  Action である。
* ``isDestroyLinks`` が ``true`` ならば、そのオブジェクトが関与するリンクは（リ
  ンクオブジェクトは除いて） DestroyLinkAction の意味に従いそのオブジェクトと一
  緒に破壊される。
* 既に破壊されたオブジェクトを破壊することは効果がない。

16.4.3.3 Test Identity Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* TestIdentityAction とは、その InputPins に与えられる二つの値が全く同一のもので
  あるかどうかを調べる Action である。
* オブジェクトが一つまたはそれを超える Classes のオブジェクトであると単に分類さ
  れるならば、それが別の「同じオブジェクト」であるかどうかを調べることは、オブ
  ジェクトの同一性に基づいていて、その StructuralFeatures としての現在の値や、そ
  れが関与するリンクのどれからも独立している。
* オブジェクトが一つまたはそれを超える DataTypes のオブジェクトであると単に分類
  されるならば、それが別の「同じオブジェクト」であるかどうかを調べることは、それ
  が同じ値であるかどうかに依存する。
* Classes にも DataTypes にも分類されるオブジェクトや、その他の種類の
  Classifiers に分類されるオブジェクトに対するTestIdentityAction の結果は定義さ
  れないが、どの場合においても Action は結果として Boolean 値を生じる。

16.4.3.4 Read Self Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ReadSelfAction とは、その Action の実行の背景となるオブジェクトをその
  ``result`` OutputPin に配置する Action である。
* 例えば、ReadSelfAction がある Operation のメソッドである Behavior に含まれるな
  らば、それが返す背景オブジェクトはその Operation 発動の対象であった Operation
  の所有しているClassifier のオブジェクトになる。

16.4.3.5 Value Specification Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ValueSpecificationAction とは、ある ValueSpecification を評価して、結果の値を
  その ``result`` OutputPin に配置する Action である。

16.4.3.6 Read Extent Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ReadExtentAction とは、ある Classifier の現在の範囲 (extent) にあるオブジェク
  トを取得して、それらをその ``result`` OutputPin に配置する Action である。

  * ある Classifier の範囲とは、その特殊型を含むある Classifier の、任意の一時点
    に存在している、すべてのオブジェクトの集合のことである。

* どこにでも存在する Classifier のオブジェクトすべてを作り出すことは、
  ReadExtentAction の実装として一般的には実用的ではない。

16.4.3.7 Reclassify Object Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ReclassifyObjectAction とは、どの Classifiers がその ``object`` InputPin に与
  えられるオブジェクトを分類するのかを変更する Action である。
* その Action が完了する後で、入力オブジェクトは各 ``newClassifier`` とによって
  分類されて ``oldClassifier`` ではない。
* 入力オブジェクトの同一性は維持され、挙動は何も実行されず、どの既定値の式も評価
  されない。
* ``isReplaceAll`` が ``true`` ならば、ある ``newClassifier`` がもうその入力オブ
  ジェクトを分類する場合を除いて、そのオブジェクトを扱うために存在する
  Classifiers すべては ``newClassifiers`` が追加されるよりも前に取り除かれる。
* オブジェクトから Classifiers を全部取り除くことと、どのような新しいものをも追
  加しないことの効果は定義されていない。

16.4.3.8 Read-Is-Classified-Object Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ReadIsClassifiedObjectAction とはその ``object`` InputPin に与えられたオブジェ
  クトが、何か与えられた Classifier によって分類されているかどうかを決定する
  Action である。
* ``isDirect`` が ``true`` ならば、調べる内容はそのオブジェクトが指定 Classifier
  により直接的に分類されるかどうかであり、そのどんな特殊化によってではない。反対
  に ``isDirect`` が ``false`` ならば、特殊化をも認める。

16.4.3.9 Start Classifier Behavior Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* StartClassifierBehaviorAction とはその ``object`` InputPin に与えられたオブ
  ジェクトの ``classifierBehavior`` の実行を開始する Action である。
* これは旧版の UML との互換性のために与えられる型である。代わりに
  StartObjectBehaviorAction を用いることが一般には望ましい。

16.4.4 Notation
----------------------------------------------------------------------

* Figure 16.31 ValueSpecificationAction notation

  * ValueSpecificationAction はその ValueSpecification でラベルされる Action と
    して記す。

* その他の種類のオブジェクトアクション固有の記法はない。

16.4.5 Examples
----------------------------------------------------------------------

* Figure 16.32 ValueSpecificationActions

  * 現実味のない見本だが、定数 5 または 6 を出力する Activity である。

16.5 Link End Data
======================================================================

16.5.1 Summary
----------------------------------------------------------------------

* リンクオブジェクトではないリンク、つまり AssociationClass のオブジェクトではな
  い Association のオブジェクトは、Action に対して実行時の値を引き渡すことが不可
  能である。
* その代わり、リンクはその端の値により識別する。LinkEndData とはそういうリンクの
  （片側の）端の値の仕様であり、LinkActions で用いられるリンクの識別に用いられ
  る。

16.5.2 Abstract Syntax
----------------------------------------------------------------------

* Figure 16.33 Link End Data

  * ここに登場する新要素は全て Element から直接派生しているのか。

16.5.3 Semantics
----------------------------------------------------------------------

16.5.3.1 Link End Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* LinkEndData とは、あるリンクの一端にある値に一致するのに用いられる入力を指定す
  る Element である。
* LinkEndData 要素それぞれには三つの部分がある：

  #. 一致されているリンクの ``end`` の特定
  #. リンクの与えられた ``end`` で期待される値を与える ``value`` InputPin
  #. リンクの与えられた ``end`` の ``qualifiers`` の期待される値を与える
     InputPins を特定する、選択自由な QualifierValues

16.5.3.2 Link End Creation Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* LinkEndCreationData とは、LinkEndData の特殊型の一つであり、CreateLinkAction
  によって作成されるリンクの一端を特定するのに用いる。正規の LinkEndData に含ま
  れるものに加えて、LinkEndCreationData は次のものを含む：

  * オプション ``isReplaceAll`` は新しいリンクを直前にこの端における値に一致した
    リンク全部で置き換えるかどうかを指定する。
  * 与えられた ``end`` が順序付きならば、``type`` が UnlimitedNatural であり多重
    度が 1 のある ``insertAt`` InputPin がこの ``end`` での順序付き値で新しいリ
    ンクの挿入点を与えるように指定されていなければならない。

16.5.3.3 Link End Destruction Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* LinkEndDestructionData とは、LinkEndData の特殊型の一つであり、
  DestroyLinkAction によって破壊されるリンクの一端を特定するのに用いる。正規の
  LinkEndData に含まれるものに加えて、LinkEndDestructionData は次のものを含む：

  * オプション ``isDestroyDuplicates`` が ``true`` であれば、この ``end`` の値に
    一致するリンク全てが破壊されるものとすることを指定する。
  * 与えられた ``end`` が順序付きかつ非一意であり、``isDestroyDuplicates`` が
    ``false`` であれば、``type`` が UnlimitedNatural であり多重度が 1 のある
    ``insertAt`` InputPin が破壊されるリンクのこの ``end`` での位置を表す値を与
    えるように指定されていなければならない。

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

* LinkActions と ClearAssociationAction は Associations とそれらのオブジェクト
  （リンク）に作用する。これには AssociationClasses である Associations を含む。

16.6.2 Abstract Syntax
----------------------------------------------------------------------

* Figure 16.34 Link Actions

  * ClearAssociationAction が浮いている。

16.6.3 Semantics
----------------------------------------------------------------------

16.6.3.1 Link Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* LinkAction とは、ある Association のリンクを読み取ったり、生成したり、破壊した
  りする Action である。 Association は AssociationClass であってもよい。

16.6.3.2 Read Link Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ReadLinkAction とは、ある Association の一端の値を取得して、それらを
  ``result`` OutputPin に配置する LinkAction である。その読み取られている一端
  は、その ReadLinkAction に対する開放端 (open end) と呼ばれる。
* ある ReadLinkAction が実行すると、次のすべてに一致する Association の存在する
  リンクすべての部分集合を特定する。

  * その ``endData`` オブジェクトの値
  * その開放端以外の端点すべてについての qualifier values
  * その開放端における qualifier values

* ReadLinkAction の ``result`` OutputPin はその開放端と型と順序が同じである必要
  がある。

16.6.3.3 Create Link Action
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* CreateLinkAction とは、リンクを作成するための LinkAction である。
* CreateLinkAction は LinkEndCreationData という LinkEndData の特殊型を用いる。
* 順序付き端付き Associations が LinkEndCreationData の追加の ``insertAt``
  InputPin により実行時に指定される挿入点と一緒に支援されているが、それは
  ``isReplaceAll`` が ``false`` であるときの順序付き Association 端にとっては必
  要とされ、順序なし端にとっては省略される。
* Association 端は上限多重度が 1 であるときでさえ順序付きであってよい。
* その ``insertAt`` Pin は ``type`` が UnlimitedNatural で多重度が 1 である。
* 抽象型の Association を接続するためのリンクを作成することの意味は未定義であ
  る。
* 他の関連端オブジェクトの初期化の後において、作成されているリンクが既に存在する
  わけではない限りは、``isReadOnly`` が ``true`` である関連端を有するリンクを作
  成することの意味は未定義である。

16.6.3.4 Destroy Link Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* DestroyLinkAction とは、指定された LinkEndData に一致するリンクを破壊する
  Action である。
* 破壊するオブジェクトはやはり LinkEndData を用いて同様に指定されているのだが、
  DestroyLinkAction はリンクオブジェクトを破壊することに用いても構わない。
* DestroyLinkAction は LinkEndDestructionData という LinkEndData の特殊型を用い
  る。
* 順序付きかつ非一意な端を有する Associations は、LinkEndDestructionData の追加
  の ``destroyAt`` InputPin により実行時に指定される削除位置によって支援されてい
  て、``isDestroyDuplicates`` が ``false`` であるときの順序付き非一意的
  Association 端にとっては必要とされ、他の端に対しては省略される。
* 他の関連端オブジェクトの初期化の後において、その ``endData`` に一致するリンク
  がない限りは、``isReadOnly`` が ``true`` である関連端を有するリンクを破壊する
  ことの意味は未定義である。

16.6.3.5 Clear Association Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ClearAssociationAction とは、ある特定のオブジェクトが関与する Association のリ
  ンク全てを破壊する Action であり、AssociationClass のリンクオブジェクトを含
  む。

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

* リンクオブジェクト Actions はリンクオブジェクトに作用する、AssociationClasses
  のオブジェクトである。 LinkActions もまたリンクオブジェクトに作用するが、それ
  らを違うように見分ける。

16.7.2 Abstract Syntax
----------------------------------------------------------------------

* Figure 16.35 Link Object Actions

  * ReadLinkObjectEndAction と ReadLinkObjectEndQualifierAction は構造が同じ。

16.7.3 Semantics
----------------------------------------------------------------------

16.7.3.1 Read Link Object End Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ReadLinkObjectEndAction とは、あるリンクオブジェクトから端オブジェクトを一つ取
  得する Action である。
* このことは開放端として指定された端を使ってリンクオブジェクトの Association の
  リンクを読み取ることと同じではない。

16.7.3.2 Read Link Object End Qualifier Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ReadLinkObjectEndQualifierAction とは、あるリンクオブジェクトから
  ``qualifier`` 端の値を一つ取得する Action である。

16.7.3.3 Create Link Object Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* CreateLinkObjectAction とは、リンクオブジェクトを一つ作成するための特殊化され
  た CreateLinkAction である。

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

  * ``StructuralFeatureAction`` から ``Read``, ``Write``, ``Clear`` を派生する。
  * ``Write`` から ``Add`` と ``Remove`` を派生する。

16.8.3 Semantics
----------------------------------------------------------------------

16.8.3.1 Structural Feature Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* StructuralFeatureAction とは、静的に指定された Classifier の StructuralFeature
  が与えられると、その ``object`` InputPin にあるオブジェクトに作用するものであ
  る。
* オブジェクトが関与する StructuralFeatures と AssociationClasses は動的分類ゆえ
  繰り返し変化してよいが、StructuralFeatureAction の ``object`` InputPin の型は
  単一の Classifier であり、その Action に引き渡されるオブジェクトが（直接か間接
  かを問わず）その Classifier により分類されているときに限って、その意味が定義さ
  れる。
* ReadStructuralFeatureAction は StructuralFeature の値を読み取り、これらの値を
  その ``result`` OutputPin に置く。

16.8.3.2 Read Structural Feature Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ReadStructuralFeatureAction とは、StructuralFeature の値を取得して、それらをそ
  の ``result`` OutputPin に配置する StructuralFeatureAction である。
* ``result`` OutputPin の型と順序はその StructuralFeature のそれらと同じである。

16.8.3.3 Add Structural Feature Value Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* AddStructuralFeatureValueAction とは、あるオブジェクトの StructuralFeature 一
  つに値を追加するためのStructuralFeatureAction である。
* ``isReplaceAll`` が ``true`` ならば、StructuralFeature の既存の値は、その
  StructuralFeature がすでにその新しい値を含む場合を除外して、新しい値が追加され
  る前に取り除かれる。
* 順序付き StructuralFeature に値を追加するには、``insertAt`` InputPin に与えら
  れる新しい値を置くための挿入点が必要である。これは ``isReplaceAll`` が
  ``false`` のときには順序付き StructuralFeatures に対しては必要とされて、順序な
  しの StructuralFeatures については省略される。
* StructuralFeatures の値は上限多重度が 1 であるときでさえ順序付きであってよい。
* ``insertAt`` InputPin があれば、それは型が UnlimitedNatural で多重度が 1 であ
  る。
* StructuralFeature の上側の多重度に違反する値を追加することと、``isReadOnly``
  が ``true`` である StructuralFeature に対してその値であろうオブジェクトの初期
  化後に新しい値を追加することの意味は未定義である。

16.8.3.4 Remove Structural Feature Value Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* RemoveStructuralFeatureValueAction とは、あるオブジェクトの StructuralFeature
  一つから値を取り除くのに用いられるStructuralFeatureAction である。
* 後述の場合を除き、取り除かれる値は ``value`` InputPin が与えるものであり、これ
  はその StructuralFeature と同じ型で多重度が 1 である。
* ``isRemoveDuplicates`` が ``false`` であり、かつ StructuralFeature が順序付き
  で非一意ならば、``value`` InputPin はなく、代わって取り除かれる値は
  ``removeAt`` InputPin の位置により与えられる。
* 所有するオブジェクトの初期化後に、``readOnly`` が ``true`` である
  StructuralFeature の既存の値を取り除くことの意味は未定義とする。

16.8.3.5 Clear Structural Feature Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ClearStructuralFeatureAction とは、たとえその StructuralFeature の多重度の下限
  がゼロより大きい場合でさえ、StructuralFeature の値全てを取り除く
  StructuralFeatureAction である。
* StructuralFeature を所有するオブジェクトの初期化後に、それに値がないのでない限
  りは、``readOnly`` が ``true`` である StructuralFeature の意味は未定義とす
  る。

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

* ReadVariableAction とは Variable の値を取得してそれらを ``result`` OutputPin
  に配置する VariableAction である。

* ``result`` OutputPin の型と順序はその Variable のそれらと同じである。

16.9.3.3 Add Variable Value Action
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* AddVariableValueAction とは、値を Variable に追加するためのものである。
* ``isReplaceAll`` が ``true`` ならば、Variable の既存の値は、その Variable が
  すでにその新しい値を含む場合を除外して、新しい値が追加される前に取り除かれる。
* 順序付き Variable に値を追加することは、``insertAt`` InputPin を使う新しい値の
  ための挿入点を必要とするが、``isReplaceAll`` が ``false`` のときの順序付き
  Variable に対しては必要とされ。順序なし Variable については省略される。
* Variable の上限多重度に違反する値を追加することについての意味は未定義とする。

16.9.3.4 Remove Variable Value Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* RemoveVariableValueAction とは、Variable から値を取り除く VariableAction であ
  る。
* 取り除かれる値は ``value`` InputPin で与えられ、それは Variable と同じ型であり
  多重度は 1 である。
* ``isRemoveDuplicates`` が ``false`` であり、なおかつその Variable が順序付きで
  非一意ならば、``value`` InputPin はなく、取り除かれる値は ``removeAt``
  InputPin の指す位置を与えることで指定されるが、これは ``type`` が
  UnlimitedNatural であり、多重度は 1 である。

16.9.3.5 Clear Variable Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ClearVariableAction とは、たとえその Variable の多重度の下限がゼロより大きい場
  合でさえ、Variable の値全てを取り除く VariableAction である。

16.9.4 Notation
----------------------------------------------------------------------

* Figure 16.38 Presentation option for AddVariableValueAction

  * 上下に分かれているが、上の方は抽象的構文とする。

* AddVariableValueAction の ``isReplaceAll`` が ``true`` であると、このことはテ
  キストの註釈 ``{replaceAll}`` が変数名の近くにあることでわかる。

16.9.5 Examples
----------------------------------------------------------------------

なし。

16.10 Accept Event Actions
======================================================================

16.10.1 Summary
----------------------------------------------------------------------

* AcceptEventAction は一つまたはそれを超える Events の出来事を待機する。受理した
  Event の出来事が CallEvent を要求するものならば、ReplyAction をそれに返信する
  のに用いてよい。受理した Event の出来事がある SignalEvent を要求するものなら
  ば、受信した Signal オブジェクトは、

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

* AcceptEventAction とは、一つまたはそれを超える Events についての Triggers を備
  えた Action である。
* AcceptEventAction についての一致する Event 出来事が事象プールから発送されるな
  らば、その AcceptEventAction は続行するために使用可能になる。
* SignalEvent を引き起こす ``trigger`` のある AcceptEventAction は信号受理活動
  (an accept signal action) と非公式に呼ばれる。
* TimeEvent を引き起こす ``trigger`` のある AcceptEventAction は待機時間活動 (a
  wait time action) と非公式に呼ばれる。
* AcceptEventAction の ``triggers`` がすべて ChangeEvents または CallEvents また
  はその両方についてのものならば、AcceptEventAction には ``result`` OutputPins
  はない。

  * ただし AcceptEventAction は AcceptCallAction ではないものとする。

* AcceptEventAction の ``triggers`` のうちの一つが AnyReceiveEvent であり、
  Event の出来事が同じ AcceptEventAction にある SignalEvent または CallEvent の
  ``trigger`` に一致されないメッセージに対するものならば、Event の出来事は
  AnyReceiveEvent を引き起こす ``trigger`` に一致する。
* AcceptEventAction が Activity で使われると、それがいつ利用可能になるのかを決め
  る特別な規則がある。

16.10.3.2 Accept Call Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* AcceptCallAction とは、CallEvent の出来事を処理するために特殊化された
  AcceptEventAction である。
* AcceptCallAction は一致する CallEvent の出来事で普通の AcceptEventAction と同
  じ方法で起こされる。
* 非同期呼び出しにより起こされた AcceptCallAction は、やはりその
  ``returnInformation`` OutputPin に値を生じるが、その値を受理する ReplyAction
  は非同期呼び出しにとっての戻り値が与えられると、何も起こらずに直ちに完了する。
* AcceptCallAction の CallEvent で参照される Operation には付随するメソッド
  Behavior があるべきではない。そうではなく、Operation に対する呼び出しはそのメ
  ソッドの実行の直接効果があるはずであり、その背景となるオブジェクトについての事
  象プールへ置かれることはないであろう。このように、Operation に対する呼び出しは
  AcceptCallAction に送達されることは決してない。

16.10.3.3 Reply Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ReplyAction とは直前の AcceptCallAction によって受理された呼び出しの処理を完了
  する Action である。
* ReplyAction が実行すると、最初の呼び出し要求メッセージに対する返答メッセージを
  発生し、その ``replyValue`` InputPins から得られる値を利用する。
* 返答の情報は複製されたり、オブジェクトに格納されたり、引き渡したりしてもよい
  が、ReplyAction の中で一度しか利用されてはならない。
* ReplyAction が同期的呼び出しからの返却情報で決して実行されないならば、呼び出し
  側は決して返答を受信しないので、それゆえ実行を完了することがないはずである。こ
  のことは違法ではないが、普通は望ましくない。

16.10.3.4 Unmarshall Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* UnmarshallAction とは、オブジェクトの StructuralFeatures の値を取得して、それ
  らを OutputPins に配置する Action である。
* Signal の所有された Properties には順序があるが、Generalization 関係のため、
  Classifier は他の Classifiers から Properties を継承してもよい。この場合、所有
  Properties すべては継承された Properties のどれよりも先に来るように
  ``unmarshallType`` の Properties は順序付けられる。
* UnmarshallAction が実行すると、その InputPin からオブジェクトを取り、オブジェ
  クトから ``unmarshallType`` の Properties の値を取得して、これらの値を対応する
  OutputPins に配置する。
* UnmarshallAction は、例えば、``isUnmarshall`` が ``false`` である
  AcceptEventAction により生成されたSignal オブジェクトの属性値を得るのに有用で
  ある。

16.10.4 Notation
----------------------------------------------------------------------

* Figure 16.40 AcceptEventAction notations

  * AcceptEventAction は一般には凹五角形で記される。左側が凹。内側にその
    ``name`` を配してもよい。
  * AcceptEventAction が単一の TimeEvent ``trigger`` を有するようなものは、砂時
    計みたいな記号で記す。名前を書くなら記号の下側である。

16.10.5 Examples
----------------------------------------------------------------------

* Figure 16.41 Implicitly enabled AcceptEventAction

  * ``Cancel order request`` は何か Signal を受理するアクションである。
  * Signal の受理が ``Cancel Order`` の発動をもたらす。

* Figure 16.42 Explicitly enabled AcceptEventAction

  * ``Process Order`` が処理された後に、``Request Payment`` Signal が送信され
    る。``Payment confirmed`` AcceptEventAction がそれを受信すると、``Ship
    Order`` が行われる。

* Figure 16.43 Repetitive time event

  * 砂時計は待機時間活動の記号である。
  * ``End of month occurred`` が砂時計の左側に書いてある。``Report Meter
    Reading`` は毎月末に起こる。

* Figure 16.44 UnmarshallAction

  * ``Unmarshall Order`` は ``Order`` から ``Name``, ``Address``, ``Product`` の
    属性の値を生じる。

16.11 Structured Actions
======================================================================

16.11.1 Summary
----------------------------------------------------------------------

* StructuredActivityNode とは、ActivityGroup でもある Action である。つまり、そ
  の実行時の挙動を定義する ActivityNodes と ActivityEdges を含む。
* StructuredActivityNodes の特殊型、名前を挙げると ConditionalNodes, LoopNodes,
  SequenceNodes らは、それらの中にある ExecutableNodes がどのように実行されるの
  かという、それぞれの型固有の制御の意味を定義する。

16.11.2 Abstract Syntax
----------------------------------------------------------------------

* Figure 16.45 Structured Actions

  * StructuredActivityNode は Namespace, Action, ActivityGroup から派生してい
    る。
  * その派生型に ConditionalNode, LoopNode, SequenceNode がある。

16.11.3 Semantics
----------------------------------------------------------------------

16.11.3.1 Structured Activity Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* StructuredActivityNode とは、ActivityGroup でもあり、その挙動がそれが含む
  ActivityNodes と ActivityEdges とで指定されるAction である。
* StructuredActivityNode は Variables の定義を含んでもよい。
* この表題のすぐ下に続く議論は StructuredActivityNodes の特殊化の一つのオブジェ
  クトでない StructuredActivityNode の意味についてのものである。
* StructuredActivityNode は使用可能であり、Action に関する通常の規則に則った実行
  を始める。
* StructuredActivityNode の InputPins は、これに含まれている ActivityEdges へ至
  る ``sources`` であってよい。
* 同様にして、StructuredActivityNode の OutputPins は、これに含まれている
  ActivityEdges の ``targets`` であってよい。
* StructuredActivityNode に含まれている ActivityEdge には必ずエッジの ``source``
  と ``target`` の両者があり、それらは

  * StructuredActivityNode に（直接的にでも間接的にでも）含まれるか、
  * StructuredActivityNode に所有される Pin であるものとする。

* ActivityEdge の ``source`` が StructuredActivityNode の外部にあり、``target``
  がその内部にあるならば、そのエッジに与えられたものはどれでも、
  StructuredActivityNode が実行を始めるまでは保留されたままになる。
* ActivityEdge の ``source`` が StructuredActivityNode の内部にあり、``target``
  がその外部にあるならば、StructuredActivityNode が実行しているのではない限り、
  そのエッジには何も与えられることはない。
* StructuredActivityNode は Activity の実行の完了にまつわる同じ規則に従って実行
  を完了する。
* StructuredActivityNode がその実行を完了するときに、その内部へと進出している実
  行はすべて停止されて、それに含まれるトークンはすべて破壊されるが、
  StructuredActivityNode の OutputPins にある、つまり ``outgoing`` エッジに向け
  て与えているものは例外とする。

16.11.3.2 Isolation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Behaviors の内側にあったりまたがったりする Actions の実行の同時性のため、オブ
  ジェクトメモリへのアクセスと変更に一貫性を保証することは難しくなる可能性があ
  る。
* もしフラグ ``mustIsolate`` が ``true`` ならば、ノード内部にある Action による
  オブジェクトへのどのアクセスもノード外側にある Action によるオブジェクトへのア
  クセスと衝突してはならない。

  * 独立性は不可分性の性質とは異なる。後者は Actions のグループが全て正常完了す
    るか、全く効能がないかのどちらかを保証するものである。

16.11.3.3 Conditional Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ConditionalNode とは、実行する ExecutableNodes の別の集まりのいくつかから一つ
  を選択する StructuredActivityNode である。
* ConditionalNode が実行を始めるときには、その内部にある InitialNodes のどれもが
  直ちに利用可能となる。
* いったん ConditionalNode が実行中になると、``predecessorClauses`` がない
  Clauses のどんな ``test`` 節も実行される。
* ``test`` 節の実行が「同時である」と指定されるところでは、この事はモデルがそれ
  らの実行の順序に何も課さないことを意味する。
* ConditionalNode について ``isAssured`` が ``true`` であると、これは少なくとも
  一つの ``test`` 節が ``true`` 値を返すはずであることを断言する。
  ``isDeterminate`` が ``true`` であると、これは高々一つの ``test`` 節が
  ``true`` 値を返すはずであることを断言する。
* これらの断言を自動的に確かめることは一般には不可能であり、それらを強いることは
  必要とされないが、実行機関に対して有用な情報を与えることが許される。
* いったん ``test`` 節の実行工程が終わると、実行可能な ``body`` 節が厳密に一つあ
  れば、その ``body`` 節は実行される。
* ``else`` Clause とは、ConditionalNode にある他の節全てに対する後者 (successor)
  であり、``test`` 節が結果として常に ``true`` となる Clause である。
* ``body`` 節が実行可能になるときにはいつでも、さらなる ``test`` 節実行のどの完
  了よりも前に実際に実行されてよい。
* ConditionalNode には ``result`` OutputPins の順序付き集合がある。
* OutputPins はどの ``outgoing`` エッジにも応じられる。
* いったん ConditionalNode が実行を完了すると、内部で進行中の実行全てが停止され
  て、その内部にあるトークンすべては破壊される。
* ConditionalNode に InputPins があることは認められない。

16.11.3.4 Loop Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* LoopNode とは、反復的なループを表現する StructuredActivityNode である。
  LoopNode は ``setupPart``, ``test`` および ``bodyPart`` から構成されていて、
  LoopNode に含まれる ExecutableNodes の部分集合を識別する。LoopNode にある
  ExecutableNode はいずれも ``setupPart``, ``test`` または ``bodyPart`` に含まれ
  ていなければならない。
* LoopNode が実行を始めると、その内部にある InitialNodes はどれもが直ちに利用可
  能になる。
* まず LoopNode の ``setupPart`` が実行される。``setupPart`` が実行を完了する
  と、ループの反復的な実行が始まる。
* ``test`` 節には LoopNode により識別される Boolean 型の ``decider`` OutputPin
  を所有している Action がある。
* ``bodyPart`` の実行それぞれの後に、ループの次の反復に備えて ``test`` 節が再び
  実行される。
* LoopNode は各反復の間に現れる途中の値を保持するのに用いられる ``loopVariable``
  OutputPins の集合を定義してもよい。
* LoopNode が実行を始めると、ループの初回反復に先立って ``loopVariableInput``
  InputPins にあるトークンは対応する ``loopVariable`` OutputPins に移される。
* LoopNode には、上で述べた以外の InputPins と OutputPins があってはならない。

16.11.3.5 Sequence Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* SequenceNode は完全な、それが含む ActivityNodes 全ての順序を定義するが、それら
  は全て ExecutableNodes でなければならない。

16.11.4 Notation
----------------------------------------------------------------------

* Figure 16.46 Notation for StructuredActivityNode

  * StructuredActivityNode は、その ``nodes`` と ``edges`` を囲んでいる、上部に
    キーワード ``«structured»`` のある破線丸角矩形で記される。

* ConditionalNode, LoopNode, SequenceNode には標準的な記法は定義されない。

16.11.5 Examples
----------------------------------------------------------------------

なし。

16.12 Expansion Regions
======================================================================

16.12.1 Summary
----------------------------------------------------------------------

* ExpansionRegion とは、入力コレクションの要素に対応している、それが含む要素を複
  数回実行する StructuredActivityNode である。

16.12.2 Abstract Syntax
----------------------------------------------------------------------

* Figure 16.47 Expansion Regions

  * ExpansionRegion と ExpansionNode だけ。
  * ExpansionKind という enumeration がある。

16.12.3 Semantics
----------------------------------------------------------------------

* ExpansionRegion とは、値のコレクションをを入力として一つまたはそれを超えて取
  り、それらの値それぞれに対して包含する ActivityNodes と ActivityEdges を実行す
  る StructuredActivityNode である。
* ExpansionNode とは、ExpansionRegion の境界を超えていく流れを指示するのに用いら
  れる ObjectNode である。
* 実行機関は、それが支援する（集合、袋、等々）、個々のオブジェクトがそこから要素
  値から構築されてよい、かつ、そこからそれらの要素値が後で得られてよいような、多
  様な種類のコレクション型を定義してよい。
* ExpansionRegion に入力 ExpansionNodes が複数あれば、異なるコレクションにある要
  素の種類が変化することが許されているけれども、それぞれは同種のコレクション（集
  合、袋、等々）を処理するものとする。
* ExpansionRegion は Action についての通常の規則に則って実行を始める。
* ExpansionRegion に含まれる ActivityNodes と ActivityEdges のグループは入力コレ
  クションの要素それぞれについて一度だけ実行される。これらは ExpansionRegion の
  拡大実行 (expansion executions) と呼べるであろう。
* 一般の StructuredActivityNode の実行と同じ意味の下に、各 expansion execution
  はその他の実行とは独立して進行するが、次の特別な規則は除外される。

  * 拡大実行それぞれの内部では、単一のトークンは入力 ExpansionNode がその
    ``source`` であり、その ``target`` が ExpansionRegion の内側にある
    ActivityEdge それぞれに与えられる。
  * 拡大実行それぞれは、その ``source`` が ExpansionRegion の内側にあり、その出
    力 ExpansionNode がその ``target`` となるActivityEdge に与えられるトークンに
    帰着してよい。
  * ExpansionRegion の InputPins 上に配置されたトークンは拡大実行のそれぞれに複
    製されて、拡大実行のそれぞれにはInputPins から流出する ActivityEdges にある
    トークンの異なる複製が与えられるようにする。
  * ExpansionRegions には、その内側から ExpansionRegion の外に交わる OutputPins
    と ActivityEdges があってよい。

* ExpansionRegion が拡大実行のすべてを完了すると、出力コレクションはそれらのノー
  ドから流出する ActivityEdges のいずれの出力 ExpansionNodes に与えられる。
* ExpansionRegion の ``mode`` はその拡大実行の実行がどのように進行するかを制御す
  る。

  ``parallel``
    拡大実行の実行は同時に進行する。これは実行期間が実行を平行に稼動させるか、さ
    もなくば時間上部分的に重なることを可能にするが、これは必要ではない。しかし、
    実行が逐次的に稼動されるならば、それらが稼動される順番は定義されない。
  ``iterative``
    拡大実行の実行は反復的な順序で起こるものとする。あるものが完了してから他のも
    のが始まることが可能になる。
  ``stream``
    厳密に一つの拡大実行の実行があり、値はコレクションそれぞれからの流れにより、
    この実行に与えられる。

16.12.4 Notation
----------------------------------------------------------------------

* Figure 16.48 Expansion Region

  * ExpansionRegion は破線丸角箱で記す。
  * 箱の左上に ExpansionKind の値に対応するキーワード ``«parallel»``, etc. を添
    える。
  * 入力と出力の ExpansionNodes は小さい短冊のような記号で記す。これらは箱の枠上
    に配置する。
  * ExpansionRegion の内側と外側にある ActivityEdge 矢印は入力と出力のノードを見
    分けることができる。

* Figure 16.49 Shorthand notation for expansion region containing single node

  * 速記法として、リストボックス記法を Action 記号で直接配置してよい。

* Figure 16.50 Full form of previous shorthand notation

  * 上の見本を完全版で示すとこうなる。

* Figure 16.51 Notation for expansion region with one behavior invocation

  * 単一の CallBehaviorAction を含む ExpansionRegion に採用可能なさらなる速記
    例。

  * キーワードを使う代わりに ``*`` を右上に記す。複数実行を含意している。

16.12.5 Examples
----------------------------------------------------------------------

* Figure 16.52 Expansion region with two inputs and one output

  * 二つの入力と一つの出力があり、``parallel`` に実行される ExpansionRegion の見
    本。
  * 両方のコレクションには同数の要素があることを期待している。
  * 内側は入力コレクションの各要素について一度実行される。

* Figure 16.53 Expansion Region

  * ExpansionRegion を含む高速 Fourier 変換計算の断片の見本である。
  * ExpansionRegion の外側で複素数の配列の演算がある。
  * ``S``, ``Slower``, ``Supper``, ``V`` は配列である。
  * ExpansionRegions 中の式に見える ``cut`` および ``shuffle`` は配列に作用する
    演算である。
  * 領域の内側では、二つの算術演算が入力配列三個 (``lower``, ``upper``,
    ``root``) の要素に対してなされ、出力配列 2 個 (``nxteven``, ``nxtodd``) を求
    める。
  * 配列内の異なる位置同士は相互作用しないので、ExpansionRegion はすべての位置で
    平行に実行することができる。

* Figure 16.54 Examples of expansion region shorthand

  * 航空券の予約とホテルの予約が独立かつ ``parallel`` である。

* Figure 16.55 Shorthand notation for expansion region

  * ``Specify Trip Route`` が複数の ``Book Flight`` アクションに帰着することを示
    す。

16.13 Other Actions
======================================================================

16.13.1 Summary
----------------------------------------------------------------------

* 本節では Actions のさらなる種類である ReduceAction と RaiseExceptionAction を
  扱う。ReduceAction とは、ある値のコレクションを単一の値にまで縮合するために一
  つの Behavior を繰り返し発動する Action であり、RaiseExceptionAction とは、例
  外を送出するための Action である。

16.13.2 Abstract Syntax
----------------------------------------------------------------------

* Figure 16.56 Other Actions

  * ReduceAction には InputPin と OutputPin の両方があるが、RaiseExceptionAction
    には InputPin だけがある。

16.13.3 Semantics
----------------------------------------------------------------------

16.13.3.1 Reduce Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ReduceAction とは、コレクションの要素を結合することでコレクションを単一の値に
  縮合する Action である。
* 実行機関は、それが支援する（集合、袋、等々）、個々のオブジェクトがそこから要素
  値から構築されてよい、かつ、そこからそれらの要素値が後で得られてよいような、多
  様な種類のコレクション型を定義してよい。

  * これは以前に書いた文をコピーアンドペーストしたものだ。

* 代わりに、実行機関は InputPin で一緒に置かれたトークンの一団に渡された値の集合
  として暗にコレクションを支援してもよい。
* ReduceAction は入力コレクションの中間生成コピーの ``reducer`` Behavior を繰り返
  し発動することで実行する。
* 入力コレクションが順序なしであるか、または InputPin に対する ``isOrdered`` が
  ``false`` であれば、中間生成コレクションのどの要素が ``reducer`` の実引数とし
  て選択されたのかが不確定となる。
* もし ``reducer`` Behavior が可換律かつ結合律を満たす操作であれば、順序なしコレ
  クションまたは ``isOrdered`` が ``false`` であるとReduceAction の結果に普通は
  影響しないはずであり、縮合計算がどう実行されてよいのかということにかなりの自由
  さを与える。
* その発動がお互いに影響するような副作用が ``reducer`` Behavior にあれば、
  ``isOrdered`` が ``false`` である ReduceAction の結果は予測不能であってよい。

16.13.3.2 Raise Exception Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* RaiseExceptionAction とは、例外を発生させる Action である。正常に終了するとい
  うよりは、常に例外を送出することで完了する。``exception`` InputPin において与
  えられた値が例外として送出される。
* RaiseExceptionAction 自身に送出された例外に一致する ExceptionHandler があるな
  らば、例外はそのハンドラーによって捕捉される。そうでなければ、例外はいちばん内
  側から外側に向かって拡がっていく。
* 例外が StructuredActivityNode の外に伝わると（ノードにおける ExceptionHandler
  によって捕捉されている場合も含み）、その StructuredActivityNode は停止する。
* RaiseExceptionAction が実行された Behavior の中にある ExceptionHandler のどれ
  によっても例外が捕捉されなければ、Behavior の実行は停止される。

16.13.4 Notation
----------------------------------------------------------------------

* ReduceActions と RaiseExceptionActions に特化した記法は定義されない。

16.13.5 Examples
----------------------------------------------------------------------

* ReduceAction は数のリストをその数の和へ縮合するのに使える。そのような
  ReduceAction には数のコレクションに対する InputPin が一つと、数に対する
  OutputPin が一つと、``reducer`` Behavior として加算関数とがある。

  * 例えば、入力コレクションに整数の組 :math:`(2, 7, 5, 3)` があると仮定する。
    ReduceAction を加算関数でこのコレクションに適用する結果は 11 である。
  * ``isOrdered`` が既定の ``false`` の場合は、これはいくつかのやり方で、例え
    ば、:math:`(((2+7) + 5) + 3), (2 + (7 + (5 + 3))), ((2 + 7) + (5 + 3))` で計
    算することが可能である。

16.14 Classifier Descriptions
======================================================================

機械生成による節。

16.15 Association Descriptions
======================================================================

機械生成による節。

.. include:: /_include/uml-refs.txt
