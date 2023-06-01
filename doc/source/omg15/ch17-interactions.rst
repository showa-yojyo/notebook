======================================================================
17 Interactions
======================================================================

UML 2.5 pp. 563-636 に関するノート。

.. contents:: ノート目次
   :depth: 2

17.1 Summary
======================================================================

17.1.1 Overview
----------------------------------------------------------------------

* Interactions はいくらかの異なる状況で利用される。

  * 相互作用の状況を共通の理解が必要な個人設計者や集団が理解するのを達成するため
    に Interactions は用いられる。
  * Interactions はより詳細な設計曲面の間も用いられる。

* 本章では用語「形跡」を「出来事の列」(sequence of occurrences) の意で用いる。こ
  の意味は trace-semantics の範囲での普通の用途によく対応し、Interactions の意
  味を記述するのに望ましい方法である。
* Interaction 仕様は許可された形跡と却下された形跡に半順序 (partial ordering) 制
  約を課す。

  * 半順序とは、任意の与えられた system trace において、事象（複数形）が起こるこ
    とが可能（または不可能）な順序を制限するものである。

* Interaction パッケージは Interactions を表現するのに必要となる概念を記述するも
  ので、それらの目的に依存する。

  * 相互作用はいくつかの型の図式、Sequence Diagrams, Interaction Overview
    Diagrams, Communication Diagrams に示すことができる。
  * Timing Diagrams と Interaction Tables のようなオプションな図式型はおまけであ
    る。

* Interactions は様々な詳細さの度合いで、計算機システム設計の専門家、潜在的なエ
  ンドユーザー、未来のシステムの利害関係者らにより、理解されたり製造されたりし得
  るシステムを記述するための共通の仕組みである。
* 典型的には Interactions は設計者または稼動システムにより提示されると、その場合
  はその Interactions は完全な物語を語ることはない。
* Interaction の最も明白な特徴 (aspects) は生存線 (lifelines) の間にあるメッセー
  ジである。メッセージの列が状況の理解に重要であると考えられる。
* 我々は交互配置 (interleaving) という言葉を、次の意味を表すものとして用いる。

  二つまたはそれを超える形跡を異なる形跡から来た事象が結果の形跡にどのような順序
  で現れても構わないように併合することであり、その一方、同じ形跡内にある事象は元
  の順序関係のまま残る。

17.1.2 Basic trace model
----------------------------------------------------------------------

* :doc:`./ch13-common-behavior` では Behaviors の実行の一般的な意味を述べた。
  Interactions とは姿を現す挙動をモデル化する Behaviors の一種である。

  * この章では一つの形跡を ``<e1, e2, ..., en>`` のように記すことにする。

* 一つの Interaction の意味は対 ``[P, I]`` の記法で表現される。ここで ``P`` は有
  効な形跡の集合であり、``I`` は無効な形跡の集合である。

  * :math:`P \cup I` が形跡の全集合である必要はない。
  * 二つの Interactions が等価となるのは、両者の形跡集合の対が等しいときである。

17.1.3 Partial ordering constraints on valid and invalid traces
----------------------------------------------------------------------

* 有効な形跡の集合は形跡にある出来事の発生の半順序によって制限されている。無効な
  形跡の集合も同様である。
* 相互作用図において垂直線それぞれが工程の時系列を記述する。ここで時間はページの
  下へ向かって進む。
* ある相互作用における事例らは原則的に互いに独立して作用する。
* 時間はオブジェクト軸それぞれの上端から下端へと経過するが、正確な時間尺度は仮定
  されない。
* 別々のオブジェクトの事象はメッセージを通じて整列されるか、または一般化した整列
  の仕組みを通じて整列される。

  * メッセージはそれが消費されるよりも前にまず送信されなければならない。
  * 推移的かつ反対称的かつ非反射的な二項関係は半順序であると呼ばれる。

17.1.4 Interaction Diagram Variants
----------------------------------------------------------------------

* 相互作用図には種々の変種がある。それぞれについて別個の節でその記法を定義してい
  く。

  Sequence Diagrams
    これがもっとも普通の変種。Message が Lifelines 間を交わすのを焦点に当てる。
  Communication Diagrams
    通信する Lifelines の間にある有向辺が引き渡された Messages とそれらの順序の
    記述で装飾される、建築学的景色を通じて相互作用を示す。
  Interaction Overview Diagrams
    制御の流れの概観を促進する方法で相互作用を定義する。一部 Activity 図と類似し
    た記法要素がある。これらの要素の記法と目的は両者で同じではあるが、詳細な意味
    はまったく異なるので、設計者は Overview 図を Activity 図であるかのように解釈
    するべきではない。
  Timing Diagrams
    図の主な目的が時間について思考することであるときに相互作用を示すのに用いられ
    る。UML 2.5 に準拠するツールは Timing Diagrams を実装する必要はない。

* 本章にある変種に加えて、Interaction Tables を用いるさらなるオプション記法があ
  る。 :doc:`./and-tabular-notation` 参照。

17.2 Interactions
======================================================================

17.2.1 Summary
----------------------------------------------------------------------

* 本節では 5 個程度のメタクラスの構文、意味、記法を仕様化する。

17.2.2 Abstract Syntax
----------------------------------------------------------------------

* Figure 17.1 Interactions

  * まず抽象クラス InteractionFragment が NamedElement から特殊化されている。
    そして InteractionFragment から残りの 4 メタクラスが特殊化されている。

  * メタクラス Interaction は InteractionFragment であると同時に
    Behavior でもある。

17.2.3 Semantics
----------------------------------------------------------------------

17.2.3.1 Interactions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Interactions は取り囲む Classifier の挙動の構成単位である。Interactions は
  Classifier の ConnectableElements の間を行き交うメッセージを使った情報のやり取
  りに集中する。
* Interaction の意味は形跡の集合の対として与えられる。その二つの形跡の集合は有効
  な形跡と無効な形跡を表現する。

  * これら二つの集合の和は必ずしも形跡全体を網羅する必要はない。
  * 含まれていない形跡はこの Interaction には全く記述されないので、我々はそれら
    が有効か無効かを知ることはできない。

* 一つの形跡は事象の出来事の連続列の一つであり、そのそれぞれはモデルにある
  OccurrenceSpecification により記述される。
* 無効な形跡の集合は Negative CombinedFragment または Assertion CombinedFragment
  の用途に関連する。

  * 前者の場合、無効な形跡の集合は明示的に指定される。
  * 後者のものは有効な形跡の集合のみを明示的に指定することで無効な形跡の集合を暗
    に指定する。簡単のために、我々は他の構成要素のすべてに対して有効な形跡しか述
    べない。

* Behavior として Interaction は一般化可能かつ再定義可能である。 Interaction を
  特殊化することは、さらなる形跡をオリジナルのそれらに対して単に追加することであ
  る。この特殊化で定義される形跡は、和集合によって継承した Interaction のそれら
  と結合される。

* Interaction を所有している classifier を特殊化してもよいし、その特殊化で
  Interaction を再定義してもよい。Interaction の再定義とは、再定義する
  Interaction を再定義されるものに交換することを単に意味し、そしてこの交換は所有
  者の基底型にある InteractionUses に対しても影響する。この事は Behavior の他の
  種類の再定義と同様である。

* 形式的な Gate は Interaction の内側の境界部に取り付けられ、その Interaction の
  InteractionUse を通して具象送信者と受信者を確立するリンク点を与えることができ
  るようにする。

17.2.3.2 Interaction Fragments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* InteractionFragment の意味とは、形跡の集合の一対である。
* InteractionFragment は取り囲む Interaction に直接含まれるか、CombinedFragment
  の InteractionOperand の内側に含まれるかのどちらかであることが許される。
  CombinedFragment はそれ自身が InteractionFragment なので、Interaction の内部に
  InteractionFragments の入れ子の深さが複数存在してもよい。

17.2.3.3 Occurrence Specifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* OccurrenceSpecification の意味とは、単にその単一の OccurrenceSpecification の
  形跡である。
* OccurrenceSpecification の理解とより深い意味は関連 Message とそれが伝える情報
  とに依存する。

17.2.3.4 Execution Specifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Interactions の形跡の意味とは、``<start, finish>`` とみなした Execution がわか
  るだけである。それらの間に出来事があってもよい。

  * 典型的に開始出来事と終了出来事は（ある Message の）受信
    OccurrenceSpecification と（ある応答 Message の）送信
    OccurrenceSpecification のようなOccurrenceSpecifications を表現するはずであ
    る。

17.2.3.5 State Invariants
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Constraint は稼働中に評価されるものである。

  * Constraint は明示的にモデル化されないアクションすべてが実行し終わるように、
    次の OccurrenceSpecification の実行の直前に評価される。
  * Constraint が ``true`` ならば、その形跡は有効な形跡である。反対に ``false``
    ならば、その形跡は無効な形跡である。
  * 言い換えると、``false`` な Constraint である StateInvariant のある形跡のすべ
    ては無効であると判断される。

17.2.4 Notation
----------------------------------------------------------------------

17.2.4.1 Interaction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Sequence 図における Interaction を表す記法は実線矩形である。

  * 矩形の左上隅に五角形を描き、そこに文字列 ``sd`` と Interaction 名と引数をこ
    の順に記す。

* 五角形の記述子の内側の記法は Behaviors の名前を表すのに用いる記法一般に従う。
* Interaction 図は局所的な属性の定義を含むことが許される。その構文は一般にはクラ
  ス記号区画で示されるものと同じである。

  * これらの属性が現れることが許されるのは、図の枠の上部付近または図のどこかの註
    釈記号内部である。

17.2.4.2 InteractionFragment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* InteractionFragment については一般的な記法がない。特定のサブクラスが独自の記法
  を定義する。

17.2.4.3 OccurrenceSpecification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* OccurrenceSpecifications は単に

  * Messages の両端もしくは
  * ExecutionSpecification の開始・終了

  における構文的な点である。

17.2.4.4 ExecutionSpecification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ExecutionSpecifications は生存線上の細い（灰色か白色の）矩形として表現される。
* または ExecutionSpecification を幅広のラベル付き矩形により表現してもよく、ラベ
  ルはたいていは実行されたアクションを識別する。
* ある Signal の属性を読み取るというような不可分な活動（複数形）を参照する
  ExecutionSpecification の代わりに、Action 全体がただ一つの
  OccurrenceSpecification に関連していることを強調する目的で、Action 記号は線の
  付いた受領 OccurrenceSpecification に関連してもよい。
* Figure 17.2 Overlapping ExecutionSpecifications

  * 同一生存線上で重なり合う ExecutionSpecifications はやはり重なり合う矩形で表
    現される。

17.2.4.5 StateInvariant
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* 起こり得る関連 Constraint は生存線上に中括弧に囲まれたテキストで示される。
* 準拠ツールは StateInvariant を OccurrenceSpecification に関連した Note として
  示してもよい。
* 状態記号は Lifeline により表現されるオブジェクトの状態を調べる制約の等価性を表
  現する。
* 領域は状態（複数形）の直交領域を表現する。識別子は状態を部分的に定義しさえすれ
  ばよい。

17.2.4.6 Formal Gate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* 形式的な Gate は枠の内側にある単なる点であり、メッセージの端点である。それらに
  は明示的な名前があってもよい。

17.2.5 Examples
----------------------------------------------------------------------

* Figure 17.3 An example of an Interaction in the form of a Sequence Diagram

  * 矢印がメッセージ。
  * 明らかにメッセージ ``CardOut`` と ``OK`` が非同期的に見える。
  * 最後のメッセージ ``Unlock`` の出口が形式的 Gate の例である。

* Figure 17.4 OccurrenceSpecification

  * メッセージ ``msg`` の矢印の根本が OccurrenceSpecification の例である。
  * 先と同様に矢印の矢先が図枠に至っている点が形式的 Gate の例である。

* Figure 17.5 Sequence Diagram with time and timing concepts

  * 以前やった時間にまつわる記法が再録されているので復習したい。例えば
    ``CardOut`` は 0 から 13 時間単位の間じゅう継続するように強制されている。

17.3 Lifelines
======================================================================

17.3.1 Summary
----------------------------------------------------------------------

* メタクラス Lifeline の構文法、意味、および表記法を仕様化する。

17.3.2 Abstract Syntax
----------------------------------------------------------------------

* Figure 17.6 Lifelines

  * Lifeline は NamedElement の一種。
  * 継承関係よりも関連のほうが多い。

17.3.3 Semantics
----------------------------------------------------------------------

17.3.3.1 Lifelines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* 相互作用図において Lifeline はある工程のタイムラインを記述する。ここで時間は
  ページの下に向かって進む。
* 同一タイムライン上の事象はページの下に向かって線形に整列されているが、それらが
  平行に結合した断片の内部で起こる場合、すなわちそれらがある coregion 内部にある
  生存線に沿う場合は除外する。
* Lifeline に沿う OccurrenceSpecifications の順番はこれらの
  OccurrenceSpecifications が発生する順番を示している。
* Interaction にある Lifeline の意味とは、この Lifeline の
  OccurrenceSpecifications しか選択しないInteraction の意味のことである。

17.3.4 Notation
----------------------------------------------------------------------

17.3.4.1 Lifeline
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Lifeline は「見出し」となる矩形と、参加者の生存線を表現する破線スタイルの垂直
  線とからなる記号で示される。
* (pp. 570-571) 矩形の内部に表示される、生存線を識別する情報の書式
  ``<lifelineident>`` は少々ごちゃごちゃしている。

  * この BNF の構文的には空文字列も認められるようだが、ダメである。

* Lifeline の見出しの形状はこの生存線が表現する部品用の classifier に基づく。見
  出しは往々にしてその名前を含む白い矩形になる。
* 名前が ``self`` ならば、Lifeline が表現するものは、自身を所有する Interaction
  を囲む classifier のオブジェクトを表現する。
* ExecutionSpecification を描写するには、Lifeline の線を覆う薄い灰色か白色の矩形
  を当てはめる。

17.3.5 Examples
----------------------------------------------------------------------

* Lifelines は先述した Figure 17.3 を参照。
* ExecutionSpecification の記法を参照するには後述する Figure 17.14 を参照。

17.4 Messages
======================================================================

17.4.1 Summary
----------------------------------------------------------------------

* 本節ではメタクラス Message およびその関連型の構文法、意味、表記法を指定する。
  全部合わせて 7 個の型を扱う。

17.4.2 Abstract Syntax
----------------------------------------------------------------------

* Figure 17.7 Messages

  * Message と MessageEnd は NamedElement の一種である。
  * MessageEnd には特殊型が直接、間接合わせて三個ある。
  * Message のある属性を実現するために列挙型
    MessageKind と MessageSort がある。

17.4.3 Semantics
----------------------------------------------------------------------

17.4.3.1 Messages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* 完全 Message の意味とは、単純に形跡 ``<sendEvent, receiveEvent>`` のことであ
  る。
* 消失 Message とは、送信事象の発生がどこであるかが知られているが、受信事象の発
  生がない Message のことである。意味としては形跡 ``<sendEvent>`` である。
* 発見 Message とは受信事象の発生がどこであるか知られているが、（既知の）送信事
  象の発生がない Message である。意味としては形跡 ``<receiveEvent>`` である。
* Message の ``signature`` は Operation または Signal の一方を参照する。 Message
  の名前は参照される Operation または Signal の名前と同じであるものとする。
* Message ``signature`` が Operation であるならば、Message は次のうちの一つを表
  す。

  * もし ``messageSort`` が ``synchCall`` または ``asyncCall`` ならば、Message
    は Operation に対する同期的または非同期的な呼び出しおよび Operation の実行の
    開始を表す。
  * もし ``messageSort`` が ``reply`` ならば、Message はその Operation に対する
    非同期的呼び出しの戻り値を表す。

* Message ``signature`` が Signal であるならば、``messageSort`` は
  ``asyncSignal`` であるものとし、Message は Signal オブジェクトの非同期的な送信
  と受信を表す。
* Message の実引数は ValueSpecification である。
* Message が応答ならば、それの実引数それぞれは高々一つの作用対象がある
  Expression であるものとする。
* 応答 Message の実引数 Expression の記号は実引数の代入対象 (assignment target)
  を表し、そこに実引数の戻り値が代入されることになるものとする。そういった代入対
  象の記号を表すための次の値らには標準の解釈がある。

  Unknown
    空文字列であり、未知の代入対象を表す。
  Interaction Parameter
    包囲する Interaction の ``ownedParameter`` の修飾なしの名前であり、出力、入
    出力、戻り値 Parameter のいずれかであるものとする。
  Attribute
    包囲する相互作用の背景となる Behavior の属性の名前または Message の受信
    Lifeline の（おそらく修飾ありの）名前である。

* 他の値で代入対象記号として許されているものがあるが、それらの解釈は本仕様で定義
  されていない。

17.4.3.2 Message Ends
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* MessageEnd のサブクラスはそれらが表す概念に相応しい特有の意味を定義する。

17.4.3.3 Message Occurrence Specifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* MessageOccurrenceSpecification は二つの Lifelines の間にあるメッセージに関連す
  る送信事象や受信事象を表す。

17.4.3.4 Destruction Occurrence Specifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* DestructionOccurrenceSpecification はそれを含む生存線により記述されるオブジェ
  クトの破壊を表す。

17.4.3.5 Gates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Gate とは、Message ごとに具体的な送信者と受信者を確立する Interaction や
  InteractionUse や CombinedFragment の境界上で用いられる MessageEnd である。
* Gate オブジェクトは、二つの Message オブジェクトを結びつける対になった仕方で存
  在するので、それ自身明示的には整列されない。Gates は次のどちらかのものの間に接
  続点を与える MessageEnds である。

  * InteractionUse の外側にある Message と Interaction の内側にある Message
  * CombinedFragment の外側にある Message と、CombinedFragment 内の
    InteractionOperand の内側にある Message

* MessageOccurrenceSpecifications は次の規則に則った半順序が入る。

  * MessageOccurrenceSpecification オブジェクトが所有される Lifeline 上で整列さ
    れており、
  * MessageOccurrenceSpecification オブジェクトは Message オブジェクトを横断して
    整列されているか、一致した gates の一対を通じてリンクされた Message オブジェ
    クトの一対を横断して整列されている。

* Message オブジェクト自体は整列されない。
* Gates は 4 種類あり、それらの関連により区別される。

  #. ``formal`` Gate は Interaction に関連しており、Interaction の境界内側に取り
     付けられたリンク点を備え、Interaction の内側の Message を、ある ``actual``
     Gate が別の Interaction の InteractionUse の外側に取り付けられた MessageEnd
     として有する Interaction の Message に（から）伝えるものである。
  #. ``actual`` Gate は InteractionUse に関連しており、InteractionUse の境界外側
     に取り付けられたリンク点を備え、InteractionUse の内側のメッセージを、
     InteractionUse に参照される Interaction の内側のメッセージに（から）伝える
     ものである。
  #. ``inner`` CombinedFragment Gate は CombinedFragment に関連しており、
     CombinedFragment の境界内側に取り付けられたリンク点を備え、CombinedFragment
     の内側にある MessageEnd の Message を、 CombinedFragment の外側にある
     MessageEnd のMessage に（から）伝えるものである。
  #. ``outer`` CombinedFragment Gate は CombinedFragment に関連しており、
     CombinedFragment の境界外側に取り付けられたリンク点を備え、CombinedFragment
     の外側にある MessageEnd の Message を、 CombinedFragment の内側にある
     MessageEnd のMessage に（から）伝えるものである。

* Gates は明示的にも暗黙的にも名前を付けられる。後者の場合、メッセージの方向と
  メッセージの名前を連結することで識別子を構築する。例えば ``out_CardOut`` のよ
  うになる。
* Gates は名前によって、同名の ``actual`` Gate と一致した ``formal`` Gate に、そ
  して同名の ``outer`` CombinedFragment Gate に一致した ``inner``
  CombinedFragment Gateに一致される。
* 一致した Gates に対する Messages は対応しなければならない。同じ方向を向いてい
  るばかりではなく、それらに同一の名前と ``messageSort`` と ``signature`` 特性値
  とがあれば Messages は対応する。

17.4.4 Notation
----------------------------------------------------------------------

17.4.4.1 Message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Message は送信者 MessageEnd から受信者 MessageEnd までの線分として示される。線
  分や矢先の形状は Message の性質を表す。

  * ``messageSort == asynchCall || asynchSignal`` ⇒ 矢先を開く
  * ``messageSort == synchCall`` ⇒ 矢先を塗りつぶす
  * ``messageSort == reply`` ⇒ 破線
  * ``messageSort == createMessage`` ⇒ 破線＋開いた矢先
  * ``messageSort == deleteMessage`` ⇒ DestructionOccurrenceSpecification で終わ
    る
  * 消失 Message ⇒ 終点を小黒丸とする
  * 発見 Message ⇒ 始点を小黒丸とする
  * Communication 図における Messages は番号とかも添える。後述。

* 図中の Message ラベルの構文は BNF で定義されている (pp. 575-576)。
* もし応答 Message の同一性が明白ならば、ラベルを省いて図を簡単にすることが許さ
  れる。

17.4.4.2 DestructionOccurrenceSpecification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Figure 17.8 DestructionOccurrenceSpecification symbol

  * DestructionOccurrenceSpecification は Lifeline の底部にバツ印を記すことで示
    す。

17.4.4.3 Gate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Gates は枠上の単なる点であり、メッセージの端点である。

17.4.5 Examples
----------------------------------------------------------------------

* 先述の Figure 17.3 では非同期 Messages しか見なかった。こういう Messages は互
  いに追い抜いてもよい。
* 後述の Figure 17.14 では応答に伴う同期メソッド呼び出しを見る。またオブジェクト
  を生成することを表現する Message も見る。
* 後述の Figure 17.26 では Communication 図ではどのように Messages が記されるの
  かを見る。
* メッセージ識別のテキスト的構文の種々の適用のいくらかを Figure 17.14 で見られ
  る。

17.5 Occurrences
======================================================================

17.5.1 Summary
----------------------------------------------------------------------

* 本節では次のメタクラスの構文法、意味、表記法を指定する。

  * ActionExecutionSpecification
  * BehaviorExecutionSpecification
  * ExecutionOccurrenceSpecification
  * GeneralOrdering

17.5.2 Abstract Syntax
----------------------------------------------------------------------

* Figure 17.9 Occurrences

  * ExecutionSpecification の派生元が図では示されていないが、先述の
    InteractionFragment である。

  * ActionExecutionSpecification と BehaviorExecutionSpecification は兄弟。

17.5.3 Semantics
----------------------------------------------------------------------

17.5.3.1 Action Execution Specificiations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ActionExecutionSpecification はアクションから生じるメッセージを相互作用が指定
  するのに用いられる。このアクションらは他の挙動によって所有されていてよい。

17.5.3.2 Behavior Execution Specifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* BehaviorExecutionSpecification は挙動から生じるメッセージを相互作用が指定する
  のに用いられる。

17.5.3.3 Execution Occurrence Specifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ExecutionOccurrenceSpecification はある生存線上において ExecutionSpecification
  の開始事象もしくは終了事象を表現する。

17.5.3.4 General Orderings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* GeneralOrdering はあり得る列の集合を制限する。OccurrenceSpecifications の半順
  序は GeneralOrderings の集合により強制される。

17.5.4 Notation
----------------------------------------------------------------------

17.5.4.1 ActionExecutionSpecificiation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* 17.2.4.4 参照。

17.5.4.2 BehaviorExecutionSpecification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* 17.2.4.4 参照。

17.5.4.3 ExecutionOccurrenceSpecification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ExecutionOccurrenceSpecification は生存線上の ExecutionSpecification を表す垂
  直な箱の始点または終点によって表現される (Figure 17.2)。

17.5.4.4 GeneralOrdering
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* GeneralOrdering は二つの OccurrenceSpecifications を接続する点線として示され
  る。

  * 矢印の方向を示す記号は線分の中ほどに描かれる。矢印の矢先には描かない。

17.5.5 Examples
----------------------------------------------------------------------

* Figure 17.10 Example showing GeneralOrdering in a sequence diagram

  * 図式中の斜めに走っている線分が GeneralOrdering の見本だと言っている。

17.6 Fragments
======================================================================

17.6.1 Summary
----------------------------------------------------------------------

* 本節では次のメタクラスの構文法、意味、表記法を指定する。

  * InteractionOperand
  * InteractionConstraint
  * CombinedFragment
  * ConsiderIgnoreFragment
  * Continuation
  * InteractionOperatorKind: これは列挙体。

17.6.2 Abstract Syntax
----------------------------------------------------------------------

* Figure 17.11 Fragments

  * InteractionConstraint と InteractionOperatorKind を除いて抽象クラス
    InteractionFragment の直接的または間接的特殊型である。

    * そのうち InteractionOperand は Namespace の一種でもある。

  * InteractionConstraint は Constraint の特殊型である。
  * InteractionOperatorKind はやたら literals が多い。

17.6.3 Semantics
----------------------------------------------------------------------

.. todo::

   クロスリファレンスのすべてに誤植があるような気がするので問い合わせる。
   17.6.3.x の x が欠けている。当ノートで勝手に訂正する。

17.6.3.1 Interaction Operands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* InteractionOperand は CombinedFragment の内部にある領域である。意味の計算には
  ``true`` な防御の InteractionOperands しか含まれない。防御がない場合は、この事
  を ``true`` の防御を意味するものと解釈する。

  * 後述の 17.6.3.3 参照。

* InteractionOperand の意味は暗黙の **seq** 演算により結合された、その構成要素た
  る InteractionFragments により与えられる。

  * 後述の 17.6.3.3 参照。

17.6.3.2 Interaction Constraints
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* InteractionConstraints は常に CombinedFragments と共に用いられる。

  * 後述の 17.6.3.3 参照。

17.6.3.3 Combined Fragments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* CombinedFragment の意味はその ``interactionOperator`` に、
  ``interactionOperator`` の種類それぞれに対して、下に説明するように依存する。

* CombinedFragment に関連する Gates は CombinedFragment とそれが取り囲んでいる物
  との間の構文上のインターフェイスを表現する。これはインターフェイスが他の
  InteractionFragments に向けられていることを意味する。

17.6.3.4 Consider Ignore Fragments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ConsiderIgnoreFragment は Ignore または Consider の ``interactionOperator`` 値
  がある CombinedFragment である。

  * 後述の 17.6.3.15 参照。

17.6.3.5 Continuations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Continuations は Alternative CombinedFragments と（弱）順序と共にあるときしか
  意味をなさない。
* Alternative CombinedFragment の InteractionOperand が名前が X という
  Continuation で終わるならば、その Continuation X から始まっている
  InteractionFragments しか追加できない。

17.6.3.6 Interaction Operator Kind Values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* CombinedFragment の意味を決定するのに ``interactionOperator`` の値は重要であ
  り、``interactionOperator`` 列挙値それぞれに対して下に指定されるとおりである。

17.6.3.7 Alternatives
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``interactionOperator`` **alt** は CombinedFragment が挙動の選択肢の一つを表現
  することを示す。
* 選択肢一つを定義する形跡の集合は、作用対象の（防御された）形跡の和集合である。
* ``else`` によって防御される作用対象は包囲している CombinedFragment にある他の
  防御すべての論理和の否定となる防御である。
* もしどの作用対象にも ``true`` に評価する防御がないならば、どの作用対象も実行さ
  れず、包囲している InteractionFragment の残りが実行される。
* もし内側の CombinedFragment Gate が **alt** CombinedFragment の
  InteractionOperand のどれかに用いられているならば、同名の Gate がその **alt**
  CombinedFragment の InteractionOperand それぞれによって用いられるものとする。

17.6.3.8 Option
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``interactionOperator`` **opt** は CombinedFragment がその単独の作用対象が起こ
  るのか、何も起こらないのか一方となるような挙動の選択肢一つを表現することを示
  す。

17.6.3.9 Break
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``interactionOperator`` **break** は、作用対象が包囲している
  InteractionFragment の残りの代わりに行われるシナリオであるという意味で、
  CombinedFragment がシナリオの中断を表現することを示す。
* ``interactionOperator`` **break**  のある CombinedFragment は包囲している
  InteractionFragment の Lifelines すべてを覆うべきである。

17.6.3.10 Parallel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``interactionOperator`` **par** は CombinedFragment が作用対象の挙動の間の平行
  な合流を表現することを示す。
* 平行な合流は作用対象内部にある OccurrenceSpecifications の順序を乱すことなく作
  用対象の OccurrenceSpecifications が交互配置されてもよいような手段すべてを記述
  する形跡の集合を定義する。

17.6.3.11 Weak Sequencing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``interactionOperator`` **seq** は CombinedFragment が作用対象の挙動の間におけ
  る弱配列を表現することを示す。
* 弱配列はこれらの性質を有する形跡の集合により定義される：

  #. 作用対象のそれぞれの内部にある OccurrenceSpecifications の順序は結果に維持
     される。
  #. 異なる作用対象からの異なる生存線上の OccurrenceSpecifications はどのような
     順序になってもよい。
  #. 異なる作用対象からの同一生存線上の OccurrenceSpecifications は、最初の作用
     対象の OccurrenceSpecification がその次の作用対象のそれの前に来るような順序
     になる。

* 作用対象が参加者の互いに素である集合にあるときに弱配列は一つの平行な合流へ縮合
  する。

17.6.3.12 Strict Sequencing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``interactionOperator`` **strict** は CombinedFragment が作用対象の挙動の間に
  おける強配列を表現することを明示する。

17.6.3.13 Negative
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ``interactionOperator`` ``neg`` は無効であると定義される形跡を
  CombinedFragmentが表現することを明示する。

* ``interactionOperator`` ``neg`` を有する CombinedFragment を定義した形跡の集合
  はそのただ一つの作用対象により与えられた形跡の集合に等しく、有効な形跡というよ
  りは無効な集合であるというだけに過ぎない。

17.6.3.14 Critical Region
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``interactionOperator`` **critical** は CombinedFragment が危急区域を表現する
  ことを示す。

  * 他の OccurrenceSpecifications によって領域の形跡が交互配置され得ないというの
    が危急区域の意味である。

* 包囲している構成要素らの形跡の集合は危急区域により制限される。

17.6.3.15 Ignore / Consider
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``interactionOperator`` **ignore** は CombinedFragment 内部には示されていない
  メッセージの種類がいくつかあることを示す。
* 反対に ``interactionOperator`` **consider** は CombinedFragment 内部ではどの
  メッセージを重んじるべきかを示す。

17.6.3.16 Assertion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``interactionOperator`` **assert** は CombinedFragment がある断定を表現するこ
  とを示す。

17.6.3.17 Loop
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``interactionOperator`` **loop** は CombinedFragment があるループを表現するこ
  とを示す。ループ作用対象は繰り返しの回数である。
* 防御には Boolean 式に加えてループの繰り返し回数の下限と上限を含めてよい。
* ループが指定のある独立した InteractionConstraint を含むと、ループで指定された
  反復の最小数に関係なく、その指定が実行中は ``true`` と評価するときにループが続
  行するだけである。

17.6.4 Notation
----------------------------------------------------------------------

17.6.4.1 InteractionOperand
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* InteractionOperands は水平な破線で分離される。InteractionOperands は協力して枠
  にはまった CombinedFragment を構成する。
* Sequence 図の InteractionOperand の内側では InteractionFragments の順序は単に
  垂直方向の上から与えられる。

17.6.4.2 InteractionConstraint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* InteractionConstraint は最初の事象発生が起こる生存線を覆う角括弧で示され、その
  事象の上に位置し、含んでいる Interaction または InteractionOperand の中にあ
  る。
* InteractionConstraint が省略されているときには ``true`` が仮定される。

17.6.4.3 CombinedFragment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Sequence 図の CombinedFragment の表記は実線の矩形である。演算子はその矩形の左
  上隅の五角形中に示される。
* 一つを超える演算子が五角形の記述子中に示されてもかまわない。これは入れ子になっ
  た CombinedFragment の速記法である。
* CombinedFragment の作用対象は CombinedFragment のグラフ領域をタイル貼りするこ
  とで示される。

  * 水平の破線を用いて作用対象に対応する領域群に分割する。

17.6.4.4 ConsiderIgnoreFragment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ConsiderIgnoreFragment の表記は、**consider** または **ignore** が演算子を示す
  CombinedFragments のすべてについて同じである。
* **ignore** と **consider** は一つの矩形の中に他の種の演算子と共に結びつくこと
  が可能であることに注意。

17.6.4.5 Continuation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Continuations は States と同じ記号で示されるが、一つを超える Lifeline を覆うこ
  とが許される。
* Continuations はまた Interaction Overview 図の動線上に現れてもよい。
* InteractionFragment で単独である Continuation は包囲する InteractionFragment
  の末端にあると考えられる。

17.6.4.6 InteractionOperatorKind
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* InteractionOperatorKind の値は CombinedFragment 枠の左上隅の小区画でテキストと
  して与えられる。後述する特別な表記法がある。

17.6.4.7 Strict interactionOperator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* 表記法上は、含まれる部品の垂直座標がある Lifeline 上だけでなく
  CombinedFragment の全範囲において重要であることを意味する。

17.6.4.8 Ignore / Consider interactionOperator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* 17.6.4.4 参照。

17.6.4.9 Loop interactionOperator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* BNF 記法による仕様の引用符が釣り合っていない。

17.6.4.10 Parallel interactionOperator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* 準拠ツールは単一 Lifeline 内にある "coregion area" の速記法を用いてよい。
* この "coregion" とは、平行に結合された部品を表す速記法であり、ある Lifeline 上
  の事象発生（または他の入れ子になった部品）の順序が取るに足らない普通の状況で用
  いられる。

17.6.5 Examples
----------------------------------------------------------------------

* InteractionOperand の見本については Figure 17.14 を参照。
* InteractionConstraints の見本については Figure 17.14, Figure 17.27 を参照。
* 多彩な ``interactionOperators`` のある CombinedFragments の見本については
  Figure 17.12, Figure 17.13, Figure 17.14 を参照。
* Figure 17.12 Critical Region

  * 米国における 911 呼び出しの処理が切れ目なく処理されなければならないことを示
    している。
  * 演算子 **par** と **critical** の見本。

* Figure 17.13 Loop CombinedFragment

  * 演算子 **loop** の見本。防御付きの方は入れ子になっている。

* Figure 17.14 CombinedFragment

  * 演算子 **alt** の見本。モデルに意味がないので理解しにくい。

* Figure 17.15 Continuation

  * Sequence 図が二つに分割されていて、左側の図中の **ref** 区画が右側の
    Sequence 図自体に対応している。

* Figure 17.16 Continuation interpretation

  * 前述の左右の Sequence 図を合体させるとこれと等価になる。

* Figure 17.17 Ignore, ``consider``, ``assert`` with StateInvariants

  * 図の見出しに ``sd M Ignore {t, r}`` とあるので、メッセージタイプが ``t`` お
    よび ``r`` のものは無視されている。実システムではこれらのメッセージを処理す
    るだろうが、この図では取り扱わないと言っているだけだ。
  * ``Y`` にある ``mystate`` は StateInvariant の例。これ以降の事象が起こるのに
    先立って実行時に直接評価される。
  * ``consider`` 部品に入れ子になっている ``assert`` 部品は、メッセージ ``v`` が
    いったんここで発生すると、メッセージ ``q`` が起こることを期待していることを
    意味する。
  * ``{Y.p == 15}`` なる StateInvariant は ``Y`` の次の事象発生に先立って評価さ
    れる。

17.7 Interaction Uses
======================================================================

17.7.1 Summary
----------------------------------------------------------------------

* 本節では次のメタクラスの構文法、意味、表記法を指定する。

  * InteractionUse
  * PartDecomposition

17.7.2 Abstract Syntax
----------------------------------------------------------------------

* Figure 17.18 InteractionUses

  * InteractionUse は InteractionFragment の特殊型。ValueSpecification に二種類
    の composition 関連、Gate に composition 関連、Interaction に関連がある。
  * PartDecomposition は InteractionUse の特殊型。Lifeline から参照される。

17.7.3 Semantics
----------------------------------------------------------------------

17.7.3.1 Interaction Uses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* InteractionUse の意味とは、仮引数を置き換える実引数のようなものに束縛されてい
  る総称的な部分のすべてであるばかりでなく、入口が解決される被参照 Interaction
  の意味の形跡の集合でもある。
* 実 Gate は InteractionUse の外側の境界に付属されてよい。その InteractionUse に
  より被参照 Interaction にある具体的な送信者と受信者を確率するリンク点を与え
  る。

17.7.3.2 Part Decompositions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Interaction の側にある Interaction 内部にある生存線の Decomposition は厳密に
  InteractionUse として解釈される。
* 分解された Lifeline は InteractionUse として解釈されるので、PartDecomposition
  の意味は入口と引数が一致される分解により参照される Interaction の意味である。
* CombinedFragment が大域外 (extra-global) であるということが描写するのは、分解
  された Lifeline を覆う同じ演算子の CombinedFragment がその Interaction にある
  ということである。

17.7.4 Notation
----------------------------------------------------------------------

17.7.4.1 InteractionUse
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* InteractionUse は演算子が **ref** と呼ばれる CombinedFragment 記号として示され
  る。

  * 名前の構文はここにある BNF の通りに記す。

* 実引数の構文は 17.4.4 で説明されている。

17.7.4.2 PartDecomposition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* PartDecomposition は 17.3.4 節で見られるように Lifeline の見出しにある参照する
  節により示される。
* 部品分解が分解された生存線の下にインラインで示されて、分解節が ``strict`` であ
  れば、これはインライン分解内にある部分生存線すべての上にある構成要素が強配列で
  整列されることを意味する。
* 大域外 CombinedFragment は矩形枠を分解 Interaction の境界の外側に行くようにす
  る。

17.7.4.2.1 Style Guidelines
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 分解に伴う Interaction の名前はその名前、分解されている Part の型名と、分解を
  生じている Interaction の名前とを含めることに利がある。

17.7.5 Examples
----------------------------------------------------------------------

* Figure 17.19 InteractionUse

  * 左上隅に **ref** のタグの付いた矩形が InteractionUse の見本である。
  * ``EstablishAccess`` のほうは実引数まで記してある。一方 ``OpenDoor`` のほう
    は、これは引数をとらないのか、そういうのは記されていない。

* Figure 17.20 InteractionUse with value return

  * Lifeline ``a_op_b`` がこの Interaction の戻り値。
  * Lifeline ``w`` がこの Interaction の入出力引数。
  * InteractionUse は ``a_util_b`` という何かを参照している。

    * オブジェクト ``:xx`` の属性 ``xc`` に戻り値 9 を代入することを示す。
    * 入出力引数 ``w`` の出力としての値が 12 であることを示す。

* Figure 17.21 PartDecomposition - the decomposed part

  * 右の Lifeline の見出しの 2 行目に ``ref AC_UserAccess`` と記されている。この
    一本に見える Lifeline が実は次に示す sd と等価だ。

* Figure 17.22 PartDecomposition - the decomposition

  * 前述の ``ACSystem`` を分解がこの図である。この ``AC_UserAccess`` はクラス
    ACSystem が所有する Interaction である。

  * ACSystem を覆う UserAccess の構成要素に一致する大域的な構成要素が
    ``AC_UserAccess`` にある。

  * 左上隅に **opt** とあるのが extra-global CombinedFragment の例である。この構
    成概念が UserAccess のある CombinedFragment に対応する。

  * ``:AccessPoint`` の下に付いている ``p1`` と ``p2`` は ``inner``
    ConnectableElements である。

* Figure 17.23 Sequence Diagrams where two Lifelines refer to (...)

  * ``sd N`` 内の右向きの ``m3`` はそれぞれ別物らしい。
  * ``sd N`` 内の左向きのメッセージを受け取る順序は任意である。このことを示すの
    が、角括弧で挟まれた部分 (coregion) である。

    * この coregion 内で成立している条件が StateInvariant ``{x == 2}`` である。

* Figure 17.24 Describing Collaborations and their binding

  * 図には示されていないが ``A`` と ``B`` はそれぞれ ``superA`` と ``superB`` の
    特殊型。ゆえに ``E`` のような ``W`` の CollaborationUse の binding が認められ
    る。

17.8 Sequence Diagrams
======================================================================

* Interaction Diagram のもっとも普通の種類は Sequence Diagram であり、これは数々
  の Lifelines の間を飛び交う Message に集中する。
* Sequence Diagram は Interaction を Lifelines 上にあるそれらに対応する
  OccurrenceSpecifications と一緒に、交わされる Messages の配列に集中することに
  より記述する。
* Sequence Diagrams により記述される Interactions は Interactions パッケージにあ
  るメタクラスらの意味を理解することへの基礎を形作る。

17.8.1 Sequence Diagram Notation
----------------------------------------------------------------------

17.8.1.1 Graphic Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Table 17.1 に Sequence Diagrams に含めることができる図表要素一覧が示されてい
  る。

17.8.1.2 Graphic Paths
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Table 17.2 に上述の要素間に描かれる各種経路の記号一覧が与えられている。
* Interactions は包囲している Classifier の挙動の構成単位の集合体。Interactions
  は Classifier の ConnectableElements 間を往来する Messages と一緒に情報の通行
  に焦点を合わせる。

17.8.2 Example Sequence Diagram
----------------------------------------------------------------------

* Figure 17.25 Overview of Metamodel elements of a Sequence Diagram

  * 上の Interaction ``N`` は説明してもらわなくてももう理解できる。
  * 下のオブジェクト図で理解が漏れそうなのは OccurrenceSpecifications だろう。
  * Interaction モデルとしては瑣末なオブジェクトはメタモデルから省いてあると断り
    がある。例えば Part ``s`` や Class ``B`` や Message が参照する連結器は示され
    ていない。

17.9 Communication Diagrams
======================================================================

* Communication Diagrams は内部構造の設計概念とこれがメッセージの往来にどう対応
  するのかが中心になるLifelines 間の相互作用に関心を集中するものだ。
* Communication Diagrams は InteractionUses や CombinedFragments のような構造化
  の機構を用いない簡単な Sequence Diagrams に対応する。

17.9.1 Communication Diagram Notation
----------------------------------------------------------------------

17.9.1.1 Graphic Paths
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: 読者ノート

   見出しの文言は編集ミスと思われる。

* Table 17.3 では Communication Diagrams の構成要素各種の記法がまとめられてい
  る。と言ってもノードが Frame と Lifeline の二つしかない。

17.9.1.2 Graphic Paths
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Table 17.4 は項目が一つしかない図表である。Message はラベル付き実線で記され
  る。

17.9.1.3 Sequence expression
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Message のラベルを BNF 記法で与えている。
* 輪番式は輪番項のドット区切りリストにコロンが続くものである。
* 各項は全相互作用内部の手続きに関する入れ子の深さを表現する。例えば Message
  ``3.1.4`` は ``3.1`` 内の ``3.1.3`` に続く。
* 輪番項の ``name`` は制御の concurrent thread を表現する。例えば Message
  ``3.1a`` と ``3.1b`` は ``3.1`` 内で concurrent である（どちらを先に実施しても
  よいし、平行に実施してもよい、の意）。
* ``recurrence`` は条件付きか反復実行を表現する。UML としてはその書式を規定しな
  い。

17.9.2 Example Communication Diagram
----------------------------------------------------------------------

* Figure 17.26 Communication diagram

  * メッセージ ``m1`` と ``m3`` が concurrently に送られている。

17.10 Interaction Overview Diagrams
======================================================================

* Interaction Overview Diagrams は制御フローの概観を促進するように Activity
  Diagrams の変種を通じて Interactions を定義する。
* Interaction Overview Diagrams はノードが Interactions もしくは
  InteractionUsers である制御の流れの概観に関心を集中させる。

17.10.1 Interaction Overview Diagram Notation
----------------------------------------------------------------------

17.10.1.1 Graphic Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Interaction Overview Diagrams は Interactions を表現する Activity Diagrams の
  特殊化である。

  * Activity Diagrams の ObjectNodes の代わりに、Interaction Overview Diagrams
    には（インラインの） Interactions か InteractionUses のどちらか一方しかな
    い。
  * Alternative CombinedFragments は DecisionNode と対応する MergeNode で表現さ
    れる。
  * Parallel CombinedFragments は ForkNode と対応する JoinNode で表現される。
  * Loop CombinedFragments は簡単な輪（複数形）で表現される。
  * Interaction Overview Diagrams では分岐と接合は正しく入れ子になっているものと
    する。Activity Diagrams よりも制限が厳しい。
  * Interaction Overview Diagrams は Interaction Diagrams の他の形式を包囲する枠
    と同じ種類の枠にはめられている。

* Table 17.5 では Interaction Overview Diagrams のノード三種が表になっている。
* Interaction Overview Diagrams はノードが Interactions か InteractionUses のど
  ちらかである Activity 図表記法を使う。Interaction Overview Diagrams は
  Interactions を Messages と Lifelines を消し去って記述する一つの手段である。
  もっとも純粋な形式では、Activities はすべて InteractionUses であり、それから
  Messages も Lifelines も図式中に全く現れなくなる。

17.10.2 Examples of Interaction Overview Diagrams
----------------------------------------------------------------------

* Figure 17.27 Interaction Overview Diagram representing a High Level
  Interaction diagram

  * パッと見た限り、本文で言うように Activity 図のノード系要素が Interaction や
    InteractionUse に置き換わっている図式に見える。
  * これは Figure 17.19 で示した挙動を別のやり方で記述したもので、時間的拘束をい
    くつか加えてある。

17.11 Timing Diagrams
======================================================================

* Timing Diagrams は線形の時間軸に沿った Lifelines の内部と間を変化する条件に集
  中する。
* Timing Diagrams は個々の classifiers と classifiers の相互作用の両方の挙動を記
  述するもので、モデル化された Lifelines の条件において変化を引き起こす事象の発
  生の時間に注意を集める。

17.11.1 Timing Diagram Notation
----------------------------------------------------------------------

17.11.1.1 Graphic Nodes and Paths
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Table 17.6 で Timing 図の記号すべてが表にまとまっている。

17.11.2 Examples of Timing Diagrams
----------------------------------------------------------------------

* Timing 図では時間上の状態の変化や構造的な要素の他の状態がわかる。用いられる形
  式は少しはある。
* Interactions の主要な形式としての Sequence Diagrams は時間の観測と時間的制約を
  描いてもよい。
* Figure 17.28 A Lifeline for a discrete object

  * Figure 17.5 の ``:User`` を Timing Diagram で描いたもの。
  * ``:User`` は ``Idle`` と ``WaitCard`` と ``WaitAccess`` の状態を行ったり来た
    りするようで、その時間的推移がこの図から読み取れる。

* Figure 17.29 Compact Lifeline with States

  * 上述の図の <more economical and compact> 版。

* Figure 17.30 Timing Diagram with more than one Lifeline and with Messages

  * ``:User`` に加えて ``:ACSystem`` の Lifeline も記述している。
  * これは図を読むときに定規が要る気がする。時間軸上の目盛りとグラフが遠い。

17.12 Classifier Descriptions
======================================================================

機械生成による節。

17.13 Association Descriptions
======================================================================

機械生成による節。

.. include:: /_include/uml-refs.txt
