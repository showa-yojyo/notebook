======================================================================
15 Activities
======================================================================

.. admonition:: 読者ノート

   現在ノート修正中。

.. contents::
   :depth: 2

15.1 Summary
======================================================================

* Activity とは、エッジにより相互接続されるノードのグラフとして決定される
  Behavior の一種 (:doc:`./ch13-common-behavior`) である。

  * そのノードの部分集合は、その Activity 全体の低水準の処理手順を具体化する実行
    可能ノードである。
  * オブジェクトノードは実行可能ノードに対して入出力するデータを保持し、オブジェ
    クトフローエッジを端から端まで移動する。
  * 制御ノードは制御フローエッジを経て、実行可能ノードの配列を決定する。

* Activities は手続きの計算を記述することも許されて、他の Activities を発動する
  Activities の階層を形成するか、オブジェクト指向モデルでは、直接的に発動される
  Operations に束縛されたメソッドとして、それらを間接的に発動することも許され
  る。

  * Activities を業務工程工学と仕事の流れに対して組織的モデリングに適用すること
    が認められている。

* この章の残りでは、どのようにして活動モデルが構造化され、さまざまな種類のオブ
  ジェクトと制御ノードが構造化されるのかを述べる。

  * UML では実行可能ノードの唯一の種類は Actions であり、:doc:`./ch16-actions`
    で完全に述べられる。
  * Actions を表す具体的構文は Activities を表す具体的構文の部分集合であり、本章
    で指定される Actions を表す具体的構文もある。

    * Action 表記法は Activity 図でしか現れない。

  * この章では実行可能ノードを使うことで Actions から分離されたある独立性を実現
    するが、それでもなお :doc:`./ch16-actions` と一緒に読む必要がある。

15.2 Activities
======================================================================

15.2.1 Summary
----------------------------------------------------------------------

* Activity は下位ユニットの配列として指定される Behavior であり、制御およびデー
  タフローモデルを使う。

  * 実行の流れは ActivityEdges によって接続される ActivityNodes としてモデル化さ
    れる。
  * ExecutableNode は、算術計算、操作の呼び出し、オブジェクトの内容物の操縦のよ
    うな、従属的挙動の実行であることがある。
  * ActivityNodes は、同期、決定、同時制御のような、制御の流れに関する構成要素を
    も含む。

* この節はノードとエッジのグラフとしての活動モデルの根本的な構造および流れの意味
  を述べる。それから後続の節ではActivity が含んでよい ActivityNodes 各種を述べ、
  どのようにこれらのノードを Activity でグループ化してよいのかを述べる。

15.2.2 Abstract Syntax
----------------------------------------------------------------------

* Figure 15.1 Activities

  * Activity, Variable, ActivityNode, ActivityEdge, ObjectFlow, ControlFlow 周り
    を見ていく。
  * Flow とは Edge の一種らしい。

15.2.3 Semantics
----------------------------------------------------------------------

15.2.3.1 Activities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Activity における ActivityNode 一つの実行は、その Activity にある他の
  ActivityNodes の実行に影響を与えることができ、かつ影響されることができる。

  * ある ActivityNode の別の ActivityNode に対する効果は、それらの ActivityNodes
    の間にある ActivityEdges を渡るトークンの流れにより決定される。

* トークンは Activity で明示的にモデル化されないが、Activity の実行を記述するた
  めに用いられる。

  * オブジェクトトークンは ObjectFlow エッジ上を流れる値の入れ物である。モノに
    よっては ControlFlow 上を流れることができる。
  * 値のないオブジェクトトークンは空トークンと呼ばれる。
  * 制御トークンは ActivityNodes の実行に影響するが、データはどれも運ばず、
    ControlFlow 上しか流れない。

* ActivityEdges は有向辺であり、トークンが ``source`` ActivityNode から
  ``targets`` ActivityNode へ流れる。
* ActivityNodes と ActivityEdges には名前をつけてもよいが、Activity の ``nodes``
  と ``edges`` とがその Activity の内部で一意な名前である必要はない。

  * 例えば、同じような ``nodes`` には同じ名前を与えることが許される。

* Activities は Classes であり、次のような Properties を支援することが許される。

  * その工程がどの程度長く実行するか、それがどの程度高く付くのかということ
  * 実行の行為者、誰に完了を報告するのか、使用中の資源のような、オブジェクトに関
    するリンクを指定する Associations
  * 開始、停止、中断、等々のような、それらのオブジェクトの実行を管理するための
    Operations
  * 開始、一時停止、等々のような、実行の状態を決定する StateMachines

15.2.3.2 Activity Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ActivityNodes は Activity により指定される挙動の個々の段階をモデル化するのに使
  われる。
* ActivityNode が実行を開始することができるようになるのは、指定された条件が
  ``incoming`` ActivityEdges においてそのノードに与えられたトークンを使って成り
  立つときである。それに対して、条件はノードの種類に依存する。
* 複数個の ActivityNodes の相対的な実行順序についての制限は全てが ActivityEdge
  の関係によって明示的に強制される。二つの ActivityNodes が ActivityEdge によっ
  て順序付いていないと、それらは同時に実行することが許される。
* 本文中に出てくる同時実行は、ノードが実行されなければならない順序で必要とされる
  ものはないということを単に意味する。したがって、Activity の実行をノードを任意
  の順で逐次実行してもよいし、ノードを並行実行してもよい。
* ActivityNode は ActivityEdges 複数個の ``source`` でもよいので、同一トークンを
  ``targets`` 複数個に与えることが可能である。しかしながら、同一トークンは一度に
  一つの ``target`` でしか受け取れない。

  * 複数同時に与えても、受け取るのは高々一つのノードであるし、具体的にどのノード
    がトークンを得るのかを完全に決定するものはない。

* ActivityNodes には以下の三種類がある。

  #. ControlNodes: ActivityEdges 上のトークンの流動を管理する交通スイッチのよう
     に振る舞う。
  #. ObjectNodes: ``incoming`` ObjectFlows から受け取ったオブジェクトトークンを
     保持して、その後それらを ``outgoing`` ObjectFlows に対して与えてよい。
  #. ExecutableNodes: Activity の所望の挙動を実際に実施する。

* ActivityNodes のこれら三種のそれぞれは後続の節でさらに述べる。

15.2.3.3 Activity Edges
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ActivityEdges はトークンが流動することができる、二つの ActivityNodes の間の有
  向接続であり、``source``  ActivityNode から ``target`` ActivityNode へと流れ
  る。
* トークンは ActivityEdge の ``source`` ActivityNode によって、そのエッジに向け
  て与えられる。
* ActivityEdge には ``guard`` という、エッジに与えられるトークンそれぞれに対して
  評価される ValueSpecification があることが許される。

  * トークンがこのエッジに与えられたときに評価される。この評価値が ``true`` であ
    ることが、トークンを渡す条件になる。

* 任意の個数のトークンを ActivityEdge に渡すことが可能で、一度に複数グループで
  も、複数回に分割してでもよい。

  * ``weight`` 特性は、同時にエッジを走査する必要のあるトークンの最小個数を命じ
    る。

* ``weight`` に対する弱いけれども簡単な代替法は、単一のトークンが必要データを全
  て運ぶように、情報を大きなオブジェクトたちにグループ分けすることである。

* ActivityEdges には以下の二種類がある：

  * ControlFlow: 制御トークンしか引き渡さない ActivityEdge
  * ObjectFlow: オブジェクトトークンがそれに沿って引き渡すことができる
    ActivityEdge

* ControlFlows とは異なり、下に述べるように、ObjectFlows は多重送受信、
  ObjectNodes からトークンを選択、およびトークンの変換に対しての追加の支援をも備
  えている。

15.2.3.4 Object Flows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* オブジェクトトークンは ObjectFlow 上を通過し、それらの値を介して Activity を通
  してデータを運ぶか、またはデータを運ばない（空トークン）。
* ObjectFlow には単一の入力 Parameter と単一の出力 Parameter がある
  ``transformation`` Behavior があってよい。

  * ``transformation`` Behavior が指定されていると、その Behavior が ObjectFlow
    に与えられたオブジェクトトークンごとに発動されて、トークンの値がその
    Behavior に対して入力として引き渡された状態になる。

* ObjectFlow には単一の入力 Parameter と単一の出力 Parameter がある
  ``selection`` Behavior があってよい。

  * 入力 Parameter は ``unordered``, ``nonunique`` かつ多重度が ``0..*`` である
    ものとする。
  * 出力 Parameter は多重度の上限が 1 であるものとする。
  * オブジェクトトークンを入力として処理して、次のノードに出力を引き渡す。

* ObjectFlow に ``transformation`` と ``selection`` の両方があるならば、新しい
  トークンが ObjectFlow に与えられるときには、まず ``transformation`` Behavior
  が発動されて、その結果の値が ``selection`` 挙動の発動に用いられる。
* トークンが ``target`` ノードに向けて与えられる間に ``transformation`` または
  ``selection`` Behavior が使われるので、そのトークンが ``target`` ノードに受け
  入れられる前に何度も同じトークンで走らされてよい。この事は、その Behavior に副
  作用があってはならないことを意味する。
* 多重送信と多重受信は ActivityPartitions といっしょに使われて、発行購読能力によ
  り決定されるオブジェクトの責任がある Behaviors の間の流れをモデル化する。

15.2.3.5 Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ObjectFlows は Activity でデータを移動することに対する主な方法をもたらす。
  Variables はデータを間接的に引き渡すことに関する代替法をもたらす。
* :doc:`./ch16-actions` で述べるように、Activity の実行中は、Activity の
  Variablesのそれぞれは一つまたはそれを超える値を保持してよい。Variables に値を
  書き出して、続いて値をそれら Variables から読み取る Actions がある。
* Variable の使用は、値が Variable に書き出される点からその値が Variable から読
  み取られる点のすべてへの間接的データ流動経路を効率的に実現する。
* Variable は ConnectableElement の一種であり、それ自体がTypedElement である。
  Variable に保持される値はいずれも Variable の Typed と適合しなければならない。
  :doc:`./ch11-structured-classifiers` および :doc:`./ch07-common-structure` 参
  照。
* Variable は MultiplicityElement でもある。:doc:`./ch07-common-structure` 参
  照。
* Variables は、オブジェクトフロー情報が容易にアクセス可能になることを要求しない
  それら (=Variables?) の応用について、普通のプログラミング言語を活動モデルに翻
  訳することを簡素化するために導入された。

15.2.3.6 Activity Execution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Behavior を継承したので、Activity には ``precondition`` と ``postcondition``
  Constraints があってもよい。これらは Activity の全発動に全体的に適用する。
* Behavior であるので、Activity には Parameters があってもよい。このような
  Parameter それぞれに対し、Activity には 対応する ActivityParameterNode という
  ノードがある。
* Activity が発動されると、その入力 Parameters に引き渡された値はどれもが、オブ
  ジェクトトークンに入れられ、Activity に対して対応する入力
  ActivityParameterNodes に置かれる。これらの ActivityParameterNodes はそれから
  トークンを ``outgoing`` ActivityEdges に与える。
* Activity が最初に発動されると、入力 ActivityParameterNodes 以外のノードは何一
  つどんなトークンも初めに保持しないはずである。
* Activity の続いて起こる発動それぞれで、``isSingleExecution`` 特性は Activity
  の同じ実行が発動すべてに対してトークンを処理するのか、または Activity の別々の
  実行が発動それぞれに対して生成されるのかを示す。
* Activity の単一実行を発動のすべてに対して利用すると、モデル作者は
  ActivityNodes と ActivityEdges を移動するトークンの流れ複数の間の相互作用を考
  慮する必要がある。
* Activity の別々の実行を発動のそれぞれについて利用すると（これは既定である）、
  さまざまな発動から来たトークンらは相互に作用しない。
* もし Activity に ``streaming`` Parameters があるならば、単一実行の途中でさえ
  あっても、さらなるトークンらがその Activity に（対応する
  ActivityParameterNodes を経て）流入出してもよい。
* ``streaming`` Parameters のない Activity の実行が完了するのは、実行している
  ノードがすでになくなり、実行可能なノードがないときか、ActivityFinalNode を用
  いることで明示的に停止されたときである。

  * ``streaming`` Parameters を有する Activity は、その入出力の累積数が規定値に
    達するまでは停止してはならない。

* Activity の実行が完了すると、非 ``streaming`` 出力 Parameters に対応する
  ActivityParameterNodes はすべて、少なくとも対応 Parameter の多重度の下限で与え
  られたとおりの個数の、空でないオブジェクトトークンを保持するものとする。
* 出力 Parameter は ``isException`` を ``true`` とすることで、例外 Parameter と
  みなしてもよい。
* その Activity にある流れ全てを中断する要望があるときに限り、例外 Parameters を
  Activities で使うものとする。

15.2.3.7 Activity Generalization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Activity は Classifier であり、それ自体として、Generalization 関係に参加してよ
  い。
* 一般 Activity から ActivityNode を再定義する特殊 Activity にある ActivityNode
  は、その再定義された ActivityNode を始点または終点としていた継承 ActivityEdges
  のどれもを、その再定義された ActivityNode で置き換えるとみなされる。
* 特殊 Activity を実行するときに使われるノードとエッジの有効な集合は、継承した
  ノードとエッジ（再定義されたノードとエッジを含まない）と、その特殊 Activity で
  定義されたノードとエッジ（再定義するノードとエッジをどれをも含む）との和集合か
  ら構成されている。

15.2.4 Notation
----------------------------------------------------------------------

* 本節では Activities を表す図表的表記法を指定する。この表記法は準拠ツールがテキ
  スト上の具象的構文を代わりに使えるという点で選択自由である。
* Activity の記法は、それが含む ActivityNodes と ActivityEdges の記法の組み合わ
  せたものに、境界と左上に表示された名前が加えたものである。

  * ActivityParameterNodes は Activity の境界上に表示する。
  * Behavior から継承した事前条件と事後条件を、キーワード ``«precondition»``,
    ``«postcondition»`` と共にテキスト上の式としてそれぞれ示す。
  * ``isSingleExecution`` が ``true`` である Activities については、キーワード
    ``«singleExecution»`` を用いる。

* Figure 15.2 Activity notation

  * 図の丸角縁は :doc:`./ana-diagrams` で述べられた枠記法で置き換えてよい。
  * 丸角縁にせよ枠にせよ完全に省略してよい。その場合には ActivityParameterNodes
    は図式内のどの箇所に現れても構わない。

* Figure 15.3 Activity class notation

  * Classes を表す表記法を Activity の特徴を図表化するのに利用することもある。
  * キーワードは ``«activity»`` である。

* Figure 15.4 ActivityNode notation

  * ActivityNodes 各種の記法のカタログ。次の節と :doc:`./ch16-actions` で詳しく
    議論する。

* Figure 15.5 ActivityEdge notation

  * ActivityEdges 各種の記法のカタログ。
  * 矢先はすべて開いた形状を用いる。
  * イラストにはないが ``guards`` を記すには角括弧を用いる。

* ActivityEdge は連結器を使って記すことも許されており、連結器はエッジの名前が中
  に書かれた小さい丸である。

  * ラベルの付いたすべての接続器は、同一 Activity 図で同一ラベルのついた他のもの
    の正確に一つに対して対になっていなければならない。

* Figure 15.6 ActivityEdge connector notation

  * この記法はまともに描くと矢印が長くなるときに採用すればよい。

* Figure 15.7 ActivityEdge notation

  * エッジの重みは中括弧と ValueSpecification の記法を用い
    る。:doc:`./ch08-values` 参照。
  * InterruptibleActivityRegion の ``interruptingEdge`` は稲妻型の矢印とする。

* Figure 15.8 ControlFlow notation

  * 制御フローは二つの行動を接続する矢印で示す。

* Figure 15.9 ObjectFlow notations

  * オブジェクトフローも矢印として示す。
  * Pins を用いる記法のほうがよい？

* Figure 15.10 Specifying selection behavior on an ObjectFlow

  * ``selection`` Behavior の記法にはキーワード ``«selection»`` が註釈記号に置か
    れ、適切な ObjectFlow 記号に取り付けられた状態で明記される。
  * ``transformation`` Behavior はキーワードは ``«transformation»`` を使って同様
    に明記される。

* Figure 15.11 Eliding objects flowing on the edge

  * 複雑な図式では乱雑さを緩和するために、Pins は省略してよい。省略されているこ
    とをわからせるために、小さい正方形を矢印の少し上あたりに表示する。

* 多重送信および多重受信は ObjectFlow を ``«multicast»`` または
  ``«multireceive»`` で註釈することでそれぞれ明記する。

15.2.5 Examples
----------------------------------------------------------------------

* Figure 15.12 Activity node example (...)

  * 次の種類の ActivityNodes の記法の見本となる。

    * ExecutableNodes: ``Receive Order``, ``Fill Order``, etc.
    * ObjectNodes: ``Invoice``
    * ControlNodes:

      * InitialNode: 先頭の黒丸
      * DecisionNode: 始めの方のダイヤモンド
      * ForkNode, JoinNode: Ship Order 前後の縦棒
      * MergeNode: 終わりの方のダイヤモンド
      * ActivityFinalNode: 末尾の目玉

* Figure 15.13 ActivityEdge examples

  * 矢印は ControlFlow か ObjectFlow である。
  * 右上。ObjectNode の前後にある矢印は両方 ObjectFlow である。Invoice オブジェ
    クトの移動を暗示する。

* Figure 15.14 ObjectFlow example

  * 両者の意味は同じ。オブジェクト ``Order`` の移動を暗示している。

* Figure 15.15 Eliding objects flowing on the edge

  * 省略版だとオブジェクトの個数に関わらず小さい正方形が一つになる？

* Figure 15.16 Specifying selection and transformation Behaviors on an ObjectFlow

  * ``selection`` および ``transformation`` Behaviors の見本。註釈頼み。

* Figure 15.17 Linking a class diagram to an object node

  * アクティビティ図内の ObjectNode ``Order`` と、Class ``Order`` を述べるクラス
    図とのリンクを表現している。

* Figure 15.18 Specifying multicast and multireceive on the edge

  * キーワード ``«multicast»`` と ``«multireceive»`` の見本。
  * スイムレーンは送信者と受信者を示す重要な機能である。

* Figure 15.19 ActivityEdge connector example

  * 図式中の fork と merge の間にまともに矢印を描くのは面倒なので、このような
    ワープのような記法の支援がある。

* Figure 15.20 Equivalent model

  * ワープ記法不採用版。

* Figure 15.21 ActivityEdge weight examples

  * 左上。constant weight を要求する例。
  * 右上。変数版。
  * 下。Award Bid に遷移する条件？が weight だけから決定しない例。
    この凹五角形ノードの記法の意味はまだやっていない？

* Figure 15.22 Example of an activity with input parameter

  * ``Requested Order`` とあるのが入力引数に対応する ActivityParameterNode であ
    る。

* Figure 15.23 Part selection workflow example

  * ``Design Part`` におけるノード ``Provide Required Part`` が、下側では
    Activityとして図解化されている。

* Figure 15.24 Trouble ticket workflow example

  * よくあるチケット管理の Activity だろう。

* Figure 15.25 Activity with attributes and operations

  * Activity のクラスの特徴を Class の記法で示す見本。

15.3 Control Nodes
======================================================================

15.3.1 Summary
----------------------------------------------------------------------

* ControlNode は ActivityNode の一種で、Activity 内の他のノード間を流れるトーク
  ンの流れを処理するのに用いる。本節ではInitialNodes, FinalNodes, ForkNodes,
  JoinNodes, MergeNodes, DecisionNodes を含むさまざまな ControlNode の具象型を述
  べる。

15.3.2 Abstract Syntax
----------------------------------------------------------------------

* Figure 15.26 Control Nodes

  * ControlNode は ActivityNode から派生した型で、ControlNode からもかなりの数の
    クラスが派生している。

15.3.3 Semantics
----------------------------------------------------------------------

15.3.3.1 Initial Node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* InitialNode とは、Activity を実行するための開始点として振る舞う ControlNodeで
  ある。

  * Activity に一つを超える InitialNode があっても構わない。Activity に一つを超
    える InitialNode があれば、InitialNode のそれぞれに対してActivity の発動が複
    数の同時制御フローを開始する。

* InitialNode にはいかなる ``incoming`` ActivityEdges があってはならないものと
  し、このことは、Activity が実行を開始すると Activity に所有される InitialNodes
  がいつでも使用可能であるはずであることと、Activity が実行を開始すると単一の制
  御トークンがそういった InitialNode のそれぞれに置かれるということを意味する。

  * InitialNode の ``outgoing`` ActivityEdges はすべてが ControlFlows でなければ
    ならない。

* InitialNodes は ControlNodes がトークンを保持することができず、それらの流れの
  処理しかできないという規則の例外である。

15.3.3.2 Final Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* FinalNode とは Activity のある流れがそこで停止するような ControlNode である。

  * FinalNode には ``outgoing`` ActivityEdges がないものとする。
  * FinalNode は ``incoming`` ActivityEdges により与えられたトークンすべてを受理
    する。

* FinalNode には FlowFinalNode と ActivityFinalNode の 2 種類がある。

  #. FlowFinalNode とは、一つの流れを停止する FinalNode である。FlowFinalNode が
     受理したトークンは全て破壊される。
  #. ActivityFinalNode とは、Activity のすべての流れを停止するノードである。
     Activity に所有される ActivityFinalNode に到達するトークンは、その Activity
     の実行を停止する。

     * Activity の実行の停止は、出力 ActivityParameterNodes 以外の ObjectNodes
       のどれもが保持するトークンのすべてを破壊するものとし、かつ、Activity から
       同期的に呼び出した挙動のどの実行をも停止するものとする。
     * いったん Activity の実行が停止すると、前節で述べたようにその Activity の
       発動は完了する。

* Activity の流れの全てを中止するのが望みでなければ、FlowFinalNode を使う。
  ActivityFinalNode は使わない。

15.3.3.3 Fork Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ForkNode とは、流れを同時に発生する複数の流れに分割する ControlNode である。

  * ForkNode には ``outgoing`` ActivityEdges を複数あってよいけれども、
    ``incoming`` ActivityEdge は厳密に一つあるものとする。
  * ``incoming`` エッジが ControlFlow ならば、``outgoing`` エッジはすべて
    ControlFlows であるものとし、``incoming`` エッジが ObjectFlow ならば、
    ``outgoing`` エッジはすべて ObjectFlows であるものとする。

* ForkNode に与えられたトークンは、そのノードの ``outgoing`` ActivityEdges のす
  べてに与えられる。それらのうちの少なくとも一つが受理されると、与えられたトーク
  ンは発生元から取り除かれ、受理者はトークンの複製を受け入れる。
* ``outgoing`` ActivityEdges の目標ではなく、それらの ``guard`` の失敗が原因で供
  与を受理することに失敗するそれらはどれもが、それらのトークンの複製を受理しない
  ものとする。
* ForkNode から生えている ``outgoing`` ActivityEdges で ``guards`` が使われてい
  ると、防御されたエッジで引き渡されるトークンの到着に依存する下流 JoinNodes が
  ないことをモデル作者が保証するべきである。それが回避できなければ、トークンが防
  御が失敗すると下流 JoinNode へ逸れてもよいように、ForkNode とその防御の付いた
  エッジとの間に DecisionNode を導入するべきである。

15.3.3.4 Join Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* JoinNode は複数の流れを同期するノードである。

  * JoinNode には厳密に一つの ``outgoing`` ActivityEdge があるものとするが、
    ``incoming`` ActivityEdges が複数あることは許される。
  * JoinNode の ``incoming`` エッジのどれかが ObjectFlows であると、
    ``outgoing`` エッジは ObjectFlow であるものとする。そうでなければ
    ``outgoing`` エッジは ControlFlow であるものとする。

* JoinNode には ``joinSpec`` という合流がトークンを放つ条件を決定する
  ValueSpecification があることが許される。

  * JoinNode に ``joinSpec`` があれば、``incoming`` ActivityEdge のどれからでも
    新しいトークンが JoinNode に与えられるときにはいつでもこの
    ValueSpecification が評価される。
* ``joinSpec`` ValueSpecification がテキストによる式で与えられると、
  ``incoming`` エッジの名前を次のものを示すために使ってよい：

  * ControlFlow からの供与の有無を示す Boolean 値
  * ObjectFlow から与えられたオブジェクトトークンに付随する値

* JoinNode に ``joinSpec`` がなければ、これは Boolean 演算子 ``"and"`` のある
  ``joinSpec`` 式に同値である。つまり、暗黙の既定の ``joinSpec`` 条件とは、少な
  くとも一つのトークンで ``incoming`` ActivityEdge のそれぞれで与えられているこ
  とである。
* JoinNode の暗黙または明示的な ``joinSpec`` が ``true`` と評価されると、次の規
  則に従ってトークンが JoinNode の ``outgoing`` ActivityEdge で与えられる。

  #. ``incoming`` エッジで与えられるトークンがすべて制御トークンならば、制御トー
     クンの一つが ``outgoing`` エッジに与えられる。
  #. ``incoming`` エッジで与えられるトークンで、制御トークンとオブジェクトトーク
     ンであるものがあれば、オブジェクトトークンのみが ``outgoing`` エッジに与え
     られる。

     * JoinNode に対して ``isCombinedDuplicate`` が ``true`` ならば、オブジェク
       トトークンが ``outgoing`` エッジに与えられる前に、それらの含む同じ素性の
       オブジェクトは一つのトークンに結合される。

* この規則は、同じ ``incoming`` エッジから与えられる複数トークンの場合を含み、
  JoinNode に与えられるトークンすべてに適用する。
* どのトークンでも JoinNode の ``outgoing`` ActivityEdge に与えられると、さらな
  るトークンが ``outgoing`` エッジに与えられる前に、目標によって受理されるか、ま
  たはエッジ上を走査するのを拒絶される（例えば失敗した防御のため）ものとする。

15.3.3.5 Merge Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* MergeNode とは、複数の流れを同期なしでまとめる制御ノードである。

  * MergeNode には厳密に一つの ``outgoing`` ActivityEdge があるものとする。
  * MergeNode の incoming と outgoing のエッジの型は一致しているものとする。
  * MergeNode の ``outgoing`` エッジが ControlFlow ならば、``incoming`` エッジは
    すべて ControlFlows でなければならず、``outgoing`` エッジが ObjectFlow なら
    ば、``incoming`` エッジはすべて ObjectFlows でなければならない。

* MergeNode の ``incoming`` エッジで与えられたトークンはすべて、``outgoing``
  エッジに与えられる。流れまたはトークンの合流の同期はない。

15.3.3.6 Decision Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* DecisionNode とは、``outgoing`` の流れを選択する ControlNode である。
* DecisionNode は第一 ``incoming`` エッジ上のトークンを受理し、それらを
  ``outgoing`` エッジすべてに与える。
* DecisionNode の ``outgoing`` エッジで防御を有するものがあれば、これらが
  ``incoming`` トークンそれぞれに対して評価される。
* DecisionNode に ``decisionInputFlow`` があれば、第一 ``incoming`` エッジからの
  トークンが``outgoing`` エッジに与えられる前に、第一 ``incoming`` エッジと
  ``decisionInputFlow`` の両方に与えられる必要がある。
* DecisionNode に ``decisionInput`` があれば、これは戻り Parameter はあるがその
  他の出力 Parameters はないBehavior でなければならない。
* DecisionNode の第一 ``incoming`` エッジが ControlFlow であり、DecisionNode に
  は ``decisionInput`` があるが ``decisionInputFlow`` はないならば、
  ``decisionInput`` には入力 Parameters がないものとする。
* DecisionNode の第一 ``incoming`` エッジが ObjectFlow であり、DecisionNode には
  ``decisionInput`` があるが ``decisionInputFlow`` はないならば、
  ``decisionInput`` には入力 Parameter があるものとし、Behavior がそのトークンに
  対して発動されたときには、第一 ``incoming`` エッジで与えられたオブジェクトトー
  クンに含まれる値は、この Parameter を経て引き渡される。
* DecisionNode の第一 ``incoming`` エッジで与えられたトークンは、``guard`` が
  ``false`` に評価される ``outgoing`` エッジのいずれをも走査しないものとする。
* 非決定的な挙動を回避するべく、モデル作者は ``incoming`` トークンそれぞれに対し
  て、高々一つの ``guard`` が ``true`` であると評価されるように取り決めるものと
  する。
* DecisionNodes 限定で、定義済みの ``guard`` ``"else"`` を高々一つの
  ``outgoing`` エッジについて用いて構わない。この防御が ``true`` と評価されるの
  は、DecisionNode から生えている他の ``outgoing`` エッジのどれによってでもトー
  クンを受理しないときに限る。

15.3.4 Notation
----------------------------------------------------------------------

15.3.4.1 Initial and Final Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Figure 15.27 InitialNode notation

  * InitialNodes は黒塗りの丸として記す。
  * 既視感のある黒丸シンボル。

* Figure 15.28 FinalNode notation

  * ActivityFinalNodes は白丸に囲まれた黒丸として記す。
  * FlowFinalNodes はバツが内側にある丸として記す。

15.3.4.2 Fork and Join Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Figure 15.29 ForkNode and JoinNode notation

  * ForkNode と JoinNode の両者に対する表記法は、単に線分である。
  * この線分に ``outgoing``/``incoming`` ActivityEdges のシンボルを必要に応じて
    接続する。

* Figure 15.30 joinSpec notation

  * 位置は線分の付近。
  * 中括弧に ``joinSpec = ...`` を含める。

* Figure 15.31 Combined JoinNode/ ForkNode notation

  * JoinNode と ForkNode が隣接？している状況では、両者を癒着できる。

15.3.4.3 Merge Nodes and Decision Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Figure 15.32 MergeNode notation

  * MergeNodes と DecisionNodes の両者を表す表記法は、ダイヤモンド記号である。
  * MergeNode には二つまたはそれを超える ``incoming`` ActivityEdges および単一の
    ``outgoing`` ActivityEdge が必要である。それに対して、DecisionNode には、あ
    り得る ``decisionInputFlow`` 以外では、単一の ``incoming`` ActivityEdge と複
    数の ``outgoing`` ActivityEdges が必要である。

* Figure 15.33 DecisionNode notation

  * ``decisionInput`` はキーワード ``«decisionInput»`` と共に註釈の記法で示す。
  * ``decisionInputFlow`` はキーワード ``«decisionInputFlow»`` をその矢印のそば
    に添える。

* Figure 15.34 Combined MergeNode/DecisionNode notation

  * MergeNode と DecisionNode は記号を共有することがある。
  * ``incoming``/``outgoing`` ActivityEdges 記号を複数示すことになる。

15.3.5 Examples
----------------------------------------------------------------------

15.3.5.1 Initial Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Figure 15.35 InitialNode example

  * Activity の実行の開始時点において、InitialNode は ``Receive Order``
    ExecutableNode に制御を渡す。

15.3.5.2 Fork and Join Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Figure 15.36 ForkNode example

  * ``Fill Order`` が完了したときに、ForkNode は ``ShipOrder`` と ``SendInvoice``
    の両方に制御を渡す。

* Figure 15.37 JoinNode example

  * JoinNode は ``ShipOrder`` と ``SendInvoice`` の処理を同期するのに使われる。
    両方が完了したときに ``Close Order`` に制御を引き渡す。

* Figure 15.38 ``joinSpec`` example

  * 自動販売機の制御が ``Dispense Drink`` に引き渡されるには、この ``joinSpec``
    にある条件が満たされる必要がある。

15.3.5.3 Merge and Decision Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Figure 15.39 MergeNode example

  * ``Buy Item`` と ``Make Item`` のどちらか一方または両方共が実行されたのかもし
    れない。
  * 場合によっては ``Ship Item`` が二度実行される。

* Figure 15.40 DecisionNode example

  * 角括弧を用いることで分岐条件を柔軟に表現できる。

* Figure 15.41 DecisionNode example with ``decisionInput``

  * ``decisionInput`` の註釈に分岐条件を書き下している。

15.3.5.4 Final Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Figure 15.42 ActivityFinalNode example

  * ``Close Order`` 完了時に FinalNode に至る。Activity は停止する。

* Figure 15.43 ActivityFinalNode example

  * 開始直後の ForkNode で二つの concurrent flows が始まる。
  * とにかくどちらの流れを経ても FinalNode に至る。

* Figure 15.44 ActivityFinalNode example

  * FinalNode を一つにまとめても図の意味は変わらない。
  * ``Notify of Modification`` からは FinalNode に至らないことに注意（なぜか）。

* Figure 15.45 FlowFinalNode example

  * これは ``Build`` Component が反復的に実行すると解釈する。
  * それと同時？に ``Install`` Component が実行していることに注意。

* Figure 15.46 FlowFinalNode and ActivityFinalNode example

  * ActivityFinalNode に至るとすると、左側のループはもはや実行中ではないはず？

15.3.5.5 Various Control Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Figure 15.47 ControlNode examples (...)

  * この Activity には既視感がある。

15.4 Object Nodes
======================================================================

15.4.1 Summary
----------------------------------------------------------------------

* ObjectNode とは ActivityNode の一種であり、Activity の実行中に値を含むオブジェ
  クトトークンを保持するのに用いるものである。

  * 本節ではその具象型三種 ActivityParameterNodes, CentralBufferNodes,
    DataStoreNodes ばかりでなく、ObjectNode 一般の話を述べる。

  * ObjectNode の四番目の種類である Pins は、常に Actions に結び付けられ、
    :doc:`./ch16-actions` で述べられる。

15.4.2 Abstract Syntax
----------------------------------------------------------------------

* Figure 15.48 Object Nodes

  * ObjectNode と関連する要素の役割を理解したい。

15.4.3 Semantics
----------------------------------------------------------------------

15.4.3.1 Object Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ObjectNode は Activity の実行途中にオブジェクトトークンを保持する。
* ObjectNode には同じ値である複数のオブジェクトトークンを含んでよい。そのような
  トークンは通常は結合しない。
* ObjectNodes は TypedElements である。ObjectNode に ``type`` が指定されている
  と、ObjectNode が保持するオブジェクトトークンにはどれもObjectNode の ``type``
  に適合する値があるものとする。

  * ``type`` が指定されていなければ、値はどのような ``type`` であってもよい。
  * 空トークンはオブジェクトノードすべての型を満足する。

* ObjectNodes は States の ``inState`` 集合を指定することも許される。
* ObjectNode はその ``upperBound`` がある場合、それが指定する値を超える個数の
  トークンを含むことは許されない。
* ObjectNode の ``ordering`` は、ノードが保持するトークンを ``outgoing``
  ActivityEdges に与える順序を指定する。この特性は次の値の一つである：

  * ``unordered``: 順序を定義しない。
  * ``FIFO``: ObjectNode が受理した順番で ``outgoing`` エッジに与える。
  * ``LIFO``: ObjectNode が受理したのと逆の順番で ``outgoing`` エッジに与える。
  * ``ordered``: ``selection`` Behavior を用いたモデル作者定義による順序とする。

* ``ordering == ordered`` であるとき、かつそのときに限って、ObjectNode には
  ``selection`` Behavior があるものとする。
* ObjectNode の ``selection`` はそのノードの ``outgoing`` エッジにトークンが一つ
  与えられることになるときにはいつでも実行される。
* ObjectNode の ``selection`` はその ``outgoing`` ObjectFlows の ``selection``
  Behavior のどれによっても上書きされる。
* ``ordering`` のために互いを追い越すトークン（複数形）は、Activity の発動のそれ
  ぞれがその Activity の別々の実行によって処理される場合からは独立している。
* ObjectNode に対する ``isControlType`` が ``true`` であると、ControlFlows が
  ObjectNode に対する ``incoming`` および ``outgoing`` であってよく、オブジェク
  トトークンは ControlFlows に沿って ObjectNode に出入りすることが可能であり、そ
  れらのトークンは ObjectNode の下流に到達される ControlFlows に沿って流れること
  が可能である。

15.4.3.2 Activity Parameter Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Behavior の一種なので、Activity には Parameters があることが許される。
  Activity が発動されると、値を入力 Parameters (``in``/``inout``) で Activity の
  実行の中へ引き渡してよく、値を出力 Parameters (``inout``/``out``/``return``)
  で Activityの実行の外へ引き渡してよい。
* Activity では、Activity の入出力は ActivityParameterNodes を用いて処理され
  る。 ActivityParameterNode それぞれには、そのノードを所有する Activity の
  Parameter 一つが結び付けられる。
* ActivityParameterNode はすべてが ``incoming`` ActivityEdges であるか、すべてが
  ``outgoing`` ActivityEdges であるかのどちらかであるものとする。
* Activity には入力引数、出力引数、戻り値それぞれに対応する
  ActivityParameterNode が一つ、入出力引数それぞれに対応する
  ActivityParameterNodes が二つあるものとする。
* 入力 ActivityParameterNode が非 ``streaming`` Parameter に結び付けられていれ
  ば、含む Activity が発動された時に、その Parameter を用いて引き渡された値はい
  ずれもオブジェクトトークン（複数形）に包み込まれて、Activity 実行の開始点にあ
  るActivityParameterNode に配置される。
* Activity の実行途中では、オブジェクトトークン（複数形）はActivity の出力
  ActivityParameterNodes に流出してよい。
* 入力 ActivityParameterNode 非 ``streaming`` Paramter に結び付けられていれば、
  新しい値がその Parameter に post されるときにはいつでも、その値がオブジェクト
  トークンに包み込まれて、ActivityParameterNode に配置されて、``outgoing`` エッ
  ジすべてに与えられる。

15.4.3.3 Central Buffer Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* CentralBufferNode は ``incoming`` ObjectFlows と ``outgoing`` ObjectFlows の間
  の緩衝材として振る舞う。

15.4.3.4 Data Store Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* DataStoreNode とは、Activity が実行している間じゅうそのオブジェクトトークン
  （複数形）を永続的に保持する CentralBufferNode である。
* DataStoreNode が保持するオブジェクトトークンについての供与を下流のオブジェクト
  ノードが受理すると、その与えられたトークンは（通常の CentralBufferNode の意味
  で） DataStoreNode から取り除かれる。
* DataStoreNode がオブジェクトトークンを受理すると、もしそのトークンがすでにその
  ノードによって保持されているトークンに含まれるオブジェクトと同一のオブジェクト
  を含んでいれば、重複オブジェクトトークンは DataStoreNode 上に配置しないものと
  する。正規の CentralBufferNode とは異なり、DataStoreNode は一意なオブジェクト
  群を含む。
* ``outgoing`` ObjectFlows にある ``selection`` と ``transformation`` Behaviors
  は、まるで問い合わせが実施されたかのように DataStoreNode の外側に情報を出すの
  に利用することが可能である。

15.4.4 Notation
----------------------------------------------------------------------

15.4.4.1 Object Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Figure 15.49 ObjectNode notations

  * ObjectNodes は矩形で示す。
  * ノードを分類する名前を記号の内側に置き、ここで名前とは ObjectNode の``type``
    または ``"name:type"`` の書式でノードの ``name`` と ``type`` を示す。
  * コレクションを表現する ObjectNode はそのようにラベルする。
  * Signal 付きの ObjectNode は矩形ではなく、初心者マークみたいな多角形で示す。
    左が凹で右が凸。

* ObjectNode に States の集合 ``inState`` があれば、この集合にある States の名前
  が中括弧付きカンマ区切りリストとして書かれて、ObjectNode の名前の下に置かれ
  る。

* Figure 15.50 ObjectNode annotations

  * 付随情報の表記法。

* Figure 15.51 Specifying selection behavior on an ObjectNode

  * ObjectNode の ``selection`` Behavior はキーワード ``«selection»`` が付いた註
    釈記号で指定され、ObjectNode 記号に取り付けられる。

15.4.4.2 Activity Parameter Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ActivityParameterNode は ObjectNode として記されるが、付随する Parameter の完
  全テキスト仕様が普通の名前・型ラベルの代わりに ActivityParameterNode をラベル
  付けするのに用いられることは除く。
* Figure 15.52 Notation for stream and exception parameters

  * ``streaming`` Parameter に関連する ActivityParameterNode の記法は、文字列
    ``{stream}`` をノード記号の近くに記すものとする。
  * 例外 Parameter に関連する ActivityParameterNode の記法は、小さな三角をノード
    記号の近くに記すものとする。

* Figure 15.53 Presentation option for flows between pins and parameter nodes

  * Activity の上側の表現と下側の表現は等価である。
  * Parameters は Activity の境界でやり取りする。

15.4.4.3 Central Buffer and Data Store Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Figure 15.54 Optional CentralBufferNode notation

  * CentralBufferNode 記号は ObjectNode の記法に、オプションでキーワード
    ``«centralBuffer»`` を含んでよい。

* Figure 15.55 DataStoreNode notation

  * DataStoreNode はキーワード ``«datastore»`` が付いた ObjectNode として記す。

15.4.5 Examples
----------------------------------------------------------------------

15.4.5.1 Activity Parameter Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Figure 15.56 Example of ActivityParameterNodes for regular and exception
  Parameters

 * ここで見るべきは境界上のノードのみ。
 * ``Rejected Computer`` に三角が付いているので、このノードが例外である。

* Figure 15.57 Example of ActivityParameterNodes for streaming Parameters

  * 入出力どちらの ActivityParameterNodes でも ``streaming`` たり得る。
  * ちなみに ``streaming`` であることと例外であることは両立してはならない。

15.4.5.2 Central Buffer and Data Store Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Figure 15.58 CentralBufferNode example

  * 予備部品と採用部品の区別法を示していないことに注意。

* Figure 15.59 DataStoreNode example

  * ``selection`` Behavior の説明が欲しい。
  * ``Once a year`` というシンボルがあるが、これは Timer の類だろう。

15.5 Executable Nodes
======================================================================

15.5.1 Summary
----------------------------------------------------------------------

* ExecutableNode とは、Activity の所望の挙動全体のうちの一つの段階として実行され
  てよい ActivityNode の一種である。
* ExecutableNodes の具象型はすべてが Actions であり、:doc:`./ch16-actions` で述
  べる。本節では Activity における ExecutableNodes の一般的な意味と、どの
  ExecutableNode についても ExceptionHandler を付属させる能力が有することを議論
  する。

15.5.2 Abstract Syntax
----------------------------------------------------------------------

* Figure 15.60 Executable Nodes

  * ExecutableNode は一つの ObjectNode に関連する ExceptionHandlers を所有する。
  * ExceptionHandler は Classifiers を例外の型として関連付ける。

15.5.3 Semantics
----------------------------------------------------------------------

15.5.3.1 Executable Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ExecutableNode とは、それを含む Activity の実質的な挙動の一段階を実施する
  ActivityNode である。
* ExecutableNode は ``incoming`` ControlFlows すべてがトークンを与えるまで実行し
  ないものとする。つまり ``incoming`` ControlFlows 上には暗黙の合流が存在する。
* ExecutableNode が実行を開始する前に、``incoming`` ControlFlows から与えられる
  トークンすべてを受理する。
* ExecutableNode が実行している間は、ある単独の制御がそれが実行であることを示し
  ているとみなされる。
* ExecutableNode が実行を完了するときは、その実行を表現している制御トークンがそ
  の ExecutableNode から取り除かれ、制御トークン（複数形）がその ExecutableNode
  の ``outgoing`` ControlFlows すべてに与えられる。つまり、ExecutableNode から
  ``outgoing`` ControlFlows への制御の流れの暗黙の分岐点が存在する。

15.5.3.2 Exceptions and Exception Handlers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* 例外とは、実行の完了様式が正常ではないことを確認するために用いられる値である。
* ExecutableNode には ExecutableNode の外側に広まることもある例外（複数形）を対
  処するために使われる ExceptionHandlers が一つまたはそれを超える個数あることが
  許される。その例外たちの ``handlers`` の ``protectedNode`` である。
* ExceptionHandler が例外を捕捉すると、その例外はその処理者に対する
  ``execptionInput`` ObjectNode に設置されているオブジェクトトークンに包み込ま
  れる。
* 例外捕捉後、ExceptionHandler の ``handlerBody`` が実行を完了すると、あたかも
  ``protectedNode`` が正常に完了したかのごとき正確に同じ方法で、制御トークンが
  ExceptionHandler の ``protectedNode`` の ``outgoing`` ControlFlows に与えられ
  る。
* ExceptionHandler の ``handlerBody`` には、``incoming`` にせよ ``outgoing`` に
  せよ ActivityEdges はないものとする。
* ExceptionHandler の ``handlerBody`` には ExceptionHandler の ``protectedNode``
  と同じ ``owner`` があるものとし、 ExceptionHandler の ``exceptionInput`` を所有
  するものとする。
* もし ExecutableNode が例外を広めて、そのノードには ``handlers`` がないか、広
  まった例外に一致する ``handler`` がないならば、その例外はより外側へと広まり続
  ける。

15.5.4 Notation
----------------------------------------------------------------------

15.5.4.1 Executable Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Figure 15.61 ExecutableNode notation

  * ExecutableNode は一般的には丸い角の矩形として描かれる。
  * Actions のさまざまな種類に対するより特殊化した表記法は :doc:`./ch16-actions`
    で述べる。

15.5.4.2 Exception Handlers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Figure 15.62 ExceptionHandler notation

  * ExceptionHandler は稲妻記号で描かれる。

    * 矢印の始点は ``protectedNode`` である。
    * ``exceptionType`` の名前を稲妻のそばに記す。
    * 矢印の終点 ``exceptionInput`` ノードは小さい正方形で示す。

* Figure 15.63 Alternative ExceptionHandler notation

  * 矢印自体を稲妻にする代わりに、ジグザグマークを普通の矢印に添えて
    ExceptionHandler としてもよい。

15.5.5 Examples
----------------------------------------------------------------------

* Figure 15.64 ExceptionHandler example

  * まず逆行列を求め、それからベクトルを乗じることで別のベクトルを得る。
  * 行列が非正則ならば、逆行列演算は失敗するはずで ``SingularMatrix`` 例外が送出
    される。この例外は ``exceptionType`` ``SingularMatrix`` に対する
    ExceptionHandler により処理されるが、それは ``Substitute Vector1 Action`` を
    含む領域を実行する。
  * 逆行列演算またはベクトル乗算のどちらかの処理中に ``Overflow`` 例外が発生する
    と、``Substitute Vector1 Action`` を含む領域が実行される。
  * 行列演算が例外なしで完了するか、ExceptionHandlers のうちの一つがきっかけと
    なったかに関わらず、活動 ``Print Results`` は次に実行される。

15.6 Activity Groups
======================================================================

15.6.1 Summary
----------------------------------------------------------------------

* ActivityGroup は ActivityNodes と ActivityEdges に対する集団化構成要素である。

  * ノードとエッジは一つを超える集団に所属することが可能である。
  * 本節では ActivityGroup の二つの具象型、 ActivityPartitions と
    InterruptibleActivityRegions について述べる。
  * StructuredActivityNode は ActivityGroup の第三種であるが、それらは Actions
    でもあるから :doc:`./ch16-actions` で議論する。

15.6.2 Abstract Syntax
----------------------------------------------------------------------

* Figure 15.65 ActivityGroups

  * ActivityGroup の特殊型として ActivityPartition と
    InterruptibleActivityRegion がある。
  * ActivityGroup は ``subgraph`` を表現するためのものだろう。

15.6.3 Semantics
----------------------------------------------------------------------

15.6.3.1 Activity Partitions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ActivityPartition とは、ある共通の性質を有する ActivityNodes を同一視するため
  に用いるActivityGroup の一種である。
* ActivityPartitions はモデルのトークンの流れには影響を及ぼさない。それらは仕切
  りの ``containedNodes`` と ``containedEdges`` の実行のため発動される Behaviors
  についてのビューを抑制したり、ビューを実現したりする。

  * Constraints は仕切りが表現する要素 (``represents``) の種類に従い、変化する。

    * Classifier: 仕切りで発動した Behaviors は ``represents`` の Classifier のオ
      ブジェクトである責任がある。
    * InstanceSpecification: この仕切りで発動した Behaviors は ``represents`` の
      InstanceSpecification によりモデル化されるオブジェクトである責任がある。
    * Property: この仕切りで発動した Behaviors は ``represents`` の Property に
      より保持されるオブジェクトである責任がある。

* ActivityPartition は上に挙げた以外の他の種類の Elements を表現してもよいが、当
  仕様書はそれらの意味を定義しない。
* ActivityPartition には ``subpartitions`` があってもよい。ActivityPartition の
  ``isDimension`` が ``true`` であれば、それは ``subpartitions`` を収めるための
  寸法？である。
* ActivityPartition が Property を表現し、かつその ``subpartitions`` が
  InstanceSpecifications を表現するならば、InstanceSpecifications は Property が
  保持する値をモデル化するものとする。
* ActivityPartition が Classifier の ``attribute`` である Property を表現し、別
  の仕切りがそれを含むならば、その ``superPartition`` はその Classifier か、
  ``type`` がその Classifier となる Property を表現するものとする。
* 非外部 ActivityPartition が Classifier を表現し、別の仕切りに含まれているなら
  ば、``superPartition`` もまた Classifier を表現するものとし、``subpartition``
  の Classifier は次のどちらかでなければならない。

  * ``superPartition`` が表現する Classifier の ``nestedClassifier`` または
    ``ownedBehavior`` であるか、
  * ``superPartition`` が表現する Classifier に付随した合成 Association の端点末
    尾に含まれる。

* 外部 ActivityPartition とは ``isExternal`` が ``true`` であるものである。これ
  は仕切りの構造の規則に対する作為的な例外である。
* ActivityPartitions を実行のそれとしては不十分ではあるが、高水準のモデル作者に
  よる検討には十分な情報を与えるのに利用してよい。

15.6.3.2 Interruptible Activity Regions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* InterruptibleActivityRegion とは、Activity の一部分の停止を支援する
  ActivityGroup である。

  * InterruptibleActivityRegion は ActivityNodes しか含まない。
  * また、InterruptibleActivityRegion はその ``source`` が領域内に、その
    ``target`` が領域外にあるある ActivityEdges を ``interruptingEdge`` として明
    らかにする。

* 領域にある AcceptEventActions で ``incoming`` エッジがないものは、トークンが
  AcceptEventAction に向かっていないときでさえ、その領域にトークンが入場するとき
  にしか使用可能にはならない。

  * AcceptEventActions の完全な記述については :doc:`./ch16-actions` を参照。

* もし何らかの場合に領域内の流れの全てを中止するのを望まないならば、
  InterruptibleActivityRegion は使わない。

15.6.4 Notation
----------------------------------------------------------------------

15.6.4.1 Activity Partitions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ActivityPartition は、二本の、ふつうは水平か垂直のどちらかの平行な線と、箱の中
  の一端に仕切りに名前のラベルを付けて記す。

* Figure 15.66 ActivityPartition notations

  a. これらの線に挟まれて置かれる ActivityNodes と ActivityEdges のいずれもがそ
     の仕切りの中に含まれるとみなされる。この ActivityPartition の表記法は俗に言
     うswimlane として知られる。
  b. ``superPartition`` のさらなる仕切りとして ``subpartitions`` を表現すること
     で階層的な仕切りを表現することができる。
  c. swim cell のそれぞれは複数の仕切りの交差である。

* 罫線による ActivityPartitions の図式化は実践的ではないことがある。その場合には
  次に示す代替記法を検討する。
* Figure 15.67 ActivityPartition notations

  a. 仕切りの名前を括弧付きで ActivityNode の名前の上に置く。
  b. 外側の仕切りはキーワード ``«external»`` を付けてラベルする。

15.6.4.2 Interruptible Activity Regions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Figure 15.68 InterruptableActivityRegion

  * InterruptableActivityRegion は破線丸角矩形で記す。
  * ``interruptingEdge`` を稲妻 ActivityEdge を使って記す。

* Figure 15.69 InterruptableActivityRegion alternative notation

  * 先述の通り ``interruptingEdge`` の矢印をストレートにしてジグザグマークを添え
    てもよい。

15.6.5 Examples
----------------------------------------------------------------------

15.6.5.1 Activity Partitions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Figure 15.70 ActivityPartitions using swimlane notation

  * いつもの例題に swimlanes を明記したもの。上段が ``Order Department`` の担当
    する Activity の部分を含む。中段が ``Account Department`` で、下段が
    ``Customer`` である。
  * ところで仕切りをまたぐ ActivityEdges は、どの ``subpartitions`` にも含まれな
    い。

* Figure 15.71 ActivityPartitions using annotation

  * 先の見本から swimlane を外したもの。
  * 丸括弧とキーワード ``«external»`` で所属する ActivityPartition がわかる。

* Figure 15.72 ActivityPartitions using multidimensional swimlane notation

  * 紙に描くものである以上、多次元と言っても高々 2 である。

15.6.5.2 Interruptible Activity Regions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Figure 15.73 InterruptableActivityRegion example

  * InterruptableActivityRegion と凹五角形シンボルの組み合わせは使い易そうだ。
  * 受注、記入、出荷の間に注文取消しが起こると、その流れは停止されて ``Cancel
    Order`` ノードが実行される。
  * これが ``Fill Order`` が終了した後に起こると、``Fill Order`` の後の ForkNode
    のために、請求処理はもう初期化してしまったかもしれない。

15.7 Classifier Descriptions
======================================================================

機械生成による節。

15.8 Association Descriptions
======================================================================

機械生成による節。

.. include:: /_include/uml-refs.txt
