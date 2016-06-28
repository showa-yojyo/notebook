======================================================================
15 Activities
======================================================================
UML 2.5 pp. 371-438 に関するノート。

.. todo:: 最低でもあと一回は編集する。

.. todo::

   訳語検討。

   * activity (n.)
   * concurrent (adj.) 本文中にあるように、必ずしも「同時に起こる」とは限らない。
   * flow (n.) 「流れ」で済ませたい。

.. contents:: ノート目次
   :depth: 2

15.1 Summary
======================================================================
* Activity とは ノードとエッジのグラフとして指定される Behavior の一種である。

  * ノードの部分集合は実行可能ノード (executable nodes) である。
  * オブジェクトノード (object nodes) は

    #. 実行可能ノードの入出力するデータを保持し、
    #. オブジェクトフロー (object flow) エッジを横断する。

  * 制御ノード (control nodes) は制御フロー (control flow) エッジを経て、
    実行可能ノードの配列を指定する。

* Activities は手続きの計算を記述することも許される。

  #. 他の Activities を発動する Activities の階層を形成するものか、
  #. 直接的に発動される Operations に束縛したメソッドとして
     間接的に発動されることも許される。

* Activities は
  business process engineering と workflow のための
  組織的モデリングにも適用されることが認められている。

15.2 Activities
======================================================================

15.2.1 Summary
----------------------------------------------------------------------
* Activity は下位ユニットの配列として指定される Behavior である。

  * 実行の流れは ActivityNodes と ActivityEdges とがモデル化する。
  * ExecutableNode は下位の振る舞い（算術計算のような）の実行であることがある。

* この節はノードとエッジのグラフとしての activity model の
  根本的な構造および流れの意味を述べる。
  後続の小節では ActivityNodes 各種を述べる。

15.2.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 15.1 Activities

  * Activity, Variable, ActivityNode, ActivityEdge, ObjectFlow, ControlFlow 周りを見ていく。
  * Flow とは Edge の一種らしい。

15.2.3 Semantics
----------------------------------------------------------------------
15.2.3.1 Activities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Activity とは ActivityNodes と ActivityEdge からなる有向グラフである。
* Activity の実行を記述するのに、トークンという仮想的なモデルを用いる。

  * オブジェクトトークンは値を運ぶもので、ObjectFlow 上を流れる。
    モノによっては ControlFlow 上を流れることができる。
  * 値のないオブジェクトトークンは空トークンと呼ばれる。
  * 制御トークンはノードの実行に影響するが、値は運ばず、
    ControlFlow 上に限り流れる。

* ActivityNodes と ActivityEdges には名前をつけてもよく、
  その Activity の内部で一意な名前を持たせることが必要でない。

  * というのも、Activity からすると nodes も edges も
    自身の ownedElements であって ownedMembers ではないからである。

  * 例えば、同じような nodes には同じ名前を与えることが許される。

15.2.3.2 Activity Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ActivityNode は Activity の振る舞いの一段階をモデル化する要素である。
* ノードに差し出されたトークンが指定条件を満たしていれば実行可能となる。
  条件はノードの種類に依存するものである。

* 複数ノードの実行順序は ActivityEdges の関係が明示的に制限する。
* 本文中に出てくる concurrent という用語は、基本的には
  「要求される実行順序というものはない」の意である。
  したがって、対象ノードを任意の順で逐次実行しても並行実行してもよろしい。

* ノードは複数のエッジの source であってもよいので、
  同一トークンを複数の targets に差し出すことが可能である。
  ただし、同一トークンは同一タイミングで受け取れるだけということだ。

  * 複数同時に差し出せても、受け取るのは高々ひとつのノードであるし、
    具体的にどのノードがトークンを得るのかを完全に決定するものはない。

* ActivityNodes には以下の 3 種類がある。詳細は後続の節にて仕様化される。

  * ControlNode: 交通スイッチのように振る舞う。
  * ObjectNode: オブジェクトトークンを保持する。
  * ExecutableNode: 所望の振る舞いを実際に実施する。

15.2.3.3 Activity Edges
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ActivityEdges は Activity 内のノード間を接続する有向エッジを表現する。
* ActivityEdge は guard という ValueSpecification を持つことが許される。

  * これはトークンがこのエッジに差し出されたときに評価される。
    この評価値が真であることが、トークンを渡す条件になる。

* 任意の個数のトークンをエッジに渡すことが可能で、一度でも複数回に分けてもよい。

  * 属性 weight が示すのは、同時にエッジを通り抜ける必要のある個数の最小値である。

* ActivityEdges には以下の 2 種類がある。詳細は後続の節にて仕様化される。

  * ControlFlow: 制御トークン専用エッジ。
  * ObjectFlow: オブジェクトトークンを持てるエッジ。

15.2.3.4 Object Flows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* オブジェクトトークンは ObjectFlow 沿いに通過する。

* ObjectFlow は transformation Behavior というものを持ってもよい。

  * この Behavior は単一の入力引数と単一の出力引数を持つ。
  * 差し出されたオブジェクトトークンを入力として処理し、
    この出力を次のノードに差し出す。

* ObjectFlow は selection Behavior というものを持ってもよい。

  * 入力は unordered, nonunique かつ多重度が ``0..*`` であるものとする。
  * 出力は多重度が 1 であるものとする。
  * オブジェクトトークンを入力として処理して、次のノードに出力を引き渡す。

* ObjectFlow が transformation と selection の両者を持つならば、
  先に transformation が発動されて、
  その出力が selection の発動に用いられる。

* 本文中にある理由により、これらの Behaviors は副作用を持ってはならない。

.. 15.2.3.5 Variables

* Activity 内でデータをやり取りするもう一つの手段が Variables によるものである。

* Activity の実行中は各 Variable はひとつ以上の値を保持してよい。
  これらにアクセスするための Actions がある。
  :doc:`./actions` で述べる。

15.2.3.6 Activity Execution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Activity は事前条件と事後条件を持ってもよい。
  これらの条件は Activity 内の全発動に全体的に適用される。

* Activity は Parameters を持ってもよい。
  このような Parameter に対応した ActivityParameterNode というノードを持つ。
  詳しくは後述する。

  * Activity が起動したときに入力引数として引き渡された値は、
    オブジェクトトークンに入れられ、
    （それらは）対応する入力 ActivityParameterNodes に配置される。
    そのあとにトークンは外向エッジに差し出される。

* 属性 isSingleExecution が示すのは、
  その Activity の同一の実行が全ての発動に対してトークンを処理するのか、
  またはその Activity の別々の実行が各発動に対して生成されるのかということである。

  * 単一実行を利用するならば、
    モデル作者はグラフ中を移動するトークンストリーム複数の相互作用を考慮する必要がある。

  * 別々の実行を利用するならば、
    いくつかの発動からやって来たトークンらは相互に作用しない。
    こちらの方式がデフォルトである。

* もし Activity が streaming Parameters を持つならば、
  単一実行の途中でさえあっても、
  そのときはさらなるトークンらがその Activity に流入、流出してもよい。

* streaming Parameters を持たない Activity の実行が完了するのは、

  #. もう実行しているノードがなくなり、実行可能なノードがないときか、
  #. ActivityFinalNode を用いることで明示的に停止されたときである。

* streaming Parameters を持つ Activity は、
  その入出力の累積数が規定値に達するまでは停止してはならない。

* Activity の実行が完了するときには、
  非 streaming 出力 Parameters に対応しているすべての ActivityParameterNodes が
  それらの対応 Parameter の多重度が示すだけの（空でない）オブジェクトトークンを保持するものとする。

* 出力 Parameter はその isException を true にさせることで、例外 Parameter としてもよろしい。

* Activity 内の全ての流れを中断する要望があるときに限り、例外 Parameters を使うものとする。

15.2.3.7 Activity Generalization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Activity を特殊化してもよい。

  * 特殊 Activity は nodes と edges を継承する。
  * ActivityNodes と ActivityEdges を特殊 Activity 中において定義し直してもよい。

* ノードの再定義もエッジの再定義も、置き換えの考え方による。

15.2.4 Notation
----------------------------------------------------------------------
* Activity の記法は、それが含む ActivityNodes と ActivityEdges の
  記法の組み合わせたものに、枠を加えて名前を左上に表示するものとする。

* ActivityParameterNodes は Activity の枠上に表示する。
* Behavior から継承した事前条件と事後条件は、
  キーワード ``«precondition»``, ``«postcondition»``
  と共にテキストとしてそれぞれ示される。

* isSingleExecution が真である Activities にはキーワード ``«singleExecution»`` を用いる。

* Figure 15.2 Activity notation

  * 丸角は Annex A で述べられた枠記法で置き換えてよろしい。
  * 丸角にせよ枠にせよ完全に省略してよろしい。
    その場合には ActivityParameterNodes は図式内のどのような箇所に現れても構わない。

* Figure 15.3 Activity class notation

  * Activity の機能群を図表化するのに Class 記法を利用することもある。
  * キーワードは ``«activity»`` である。

* Figure 15.4 ActivityNode notation

  * ActivityNodes 各種の記法のカタログ。次の節で詳しく議論する。

* Figure 15.5 ActivityEdge notation

  * ActivityEdges 各種の記法のカタログ。
  * 矢先はすべて開いた形状を用いる。
  * イラストにはないが guards を記すには角括弧を用いる。

* Figure 15.6 ActivityEdge connector notation

  * この記法はまともに描くと矢印が長くなるときに採用すればよい。

* Figure 15.7 ActivityEdge notation

  * エッジの weight は中括弧と ValueSpecification の記法を用いる。
  * InterruptibleActivityRegion の interruptingEdge は稲妻型の矢印とする。

* Figure 15.8 ControlFlow notation

  * 制御フローはふたつのアクションを接続する矢印として示す。

* Figure 15.9 ObjectFlow notations

  * オブジェクトフローも矢印として示す。
  * Pins を用いる記法のほうがよい？

* Figure 15.10 Specifying selection behavior on an ObjectFlow

  * selection Behavior の記法にはキーワード ``«selection»`` とコメントを用いる。
  * transformation Behavior も同様にする。キーワードは ``«transformation»`` とする。

* Figure 15.11 Eliding objects flowing on the edge

  * 図式が散らかるのを緩和するために、Pins はある程度省略してよろしい。
    省略されていることをわからせるために、
    矢印の少し上あたりに小さい四角を表示する。

15.2.5 Examples
----------------------------------------------------------------------
* Figure 15.12 Activity node example (...)

  * 代表的な ActivityNodes の記法の見本となる。

* Figure 15.13 ActivityEdge examples

  * 右上。ObjectNode の前後にある矢印は両方 ObjectFlow である。
    Invoice オブジェクトの移動を暗示する。

* Figure 15.14 ObjectFlow example

  * 両者の意味は同じ。オブジェクト Order の移動を暗示している。

* Figure 15.15 Eliding objects flowing on the edge

  * 省略版だとオブジェクトの個数に関わらず小さい四角がひとつになる？

* Figure 15.16 Specifying selection and transformation Behaviors on an ObjectFlow

  * selection および transformation Behaviors の見本。コメント頼み。

* Figure 15.17 Linking a class diagram to an object node

  * アクティビティ図内の ObjectNode Order と、
    Class Order を述べるクラス図とのリンクを表現している。

* Figure 15.18 Specifying multicast and multireceive on the edge

  * キーワード ``«multicast»`` と ``«multireceive»`` の見本。
  * スイムレーンは送信者と受信者を示す重要な機能である。

* Figure 15.19 ActivityEdge connector example

  * 図式中の fork と merge の間にまともに矢印を描くのは面倒なので、
    このようなワープのような記法の支援がある。

* Figure 15.20 Equivalent model

  * ワープ記法不採用版。

* Figure 15.21 ActivityEdge weight examples

  * 左上。constant weight を要求する例。
  * 右上。変数版。
  * 下。Award Bid に遷移する条件？が weight だけから決定しない例。
    この凹五角形ノードの記法の意味はまだやっていない？

* Figure 15.22 Example of an activity with input parameter

  * Requested Order とあるのが入力引数に対応する ActivityParameterNode である。

* Figure 15.23 Part selection workflow example

  * Design Part におけるノード Provide Required Part が、
    下側では Activity として図解化されている。

* Figure 15.24 Trouble ticket workflow example

  * よくあるチケット管理の Activity だろう。

* Figure 15.25 Activity with attributes and operations

  * Activity を Class の記法で示す見本。

15.3 Control Nodes
======================================================================

15.3.1 Summary
----------------------------------------------------------------------
* ControlNode は ActivityNode の一種で、Activity 内のトークンの流れを処理するのに用いる。
* 本節では数個ある ControlNode の具象型を述べる。

15.3.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 15.26 Control Nodes

  * ControlNode は ActivityNode から派生した型で、
    ControlNode からもかなりの数のクラスが派生している。

15.3.3 Semantics
----------------------------------------------------------------------
15.3.3.1 Initial Node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* InitialNode は Activity の実行の開始するノードとして振る舞う。
* ひとつの Activity にひとつを超える InitialNode があっても構わない。
  各点から concurrent な制御フローが開始することになる。

* InitialNode はどんな incoming エッジをも持ってはならない。
* InitialNode の outgoing エッジはすべて ControlFlows であるものとする。
* InitialNodes は ControlNodes はトークンを保持できないという規則の例外である。
  場合によってはトークンがとどまることがある。

15.3.3.2 Final Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* FinalNode は Activity 中のある流れが停止するノードである。
* FinalNode は outgoing エッジを持ってはならない。
* FinalNode は incoming エッジから差し出されるトークンをすべて受理する。
* FinalNode には FlowFinalNode と ActivityFinalNode の 2 種類がある。

  * FlowFinalNode はひとつの流れを終了するノードである。

    * ここで受理したトークンは全て消滅する。

  * ActivityFinalNode は Activity 内のすべての流れを停止するノードである。
    トークンがここに到達することで、Activity の実行が停止する。

    * Activity の実行の停止はすべての ObjectNodes が保持するトークンを
      破棄するものとする。かつ、Activity から同期的に呼び出したすべての
      振る舞いの実行を停止するものとする。

    * いったん Activity の実行が停止すると、
      前節で述べたようにその発動は完了する。

15.3.3.3 Fork Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ForkNode はひとつの流れを複数の concurrent な流れ (pl.) に分割するノードである。
* ForkNode は厳密にひとつの incoming エッジを持つものとする。
* ForkNode の incoming と outgoing のエッジの型は一致しているものとする。

* ForkNode に差し出されたトークンは、そのノードのすべての outgoing エッジに差し出される。
  もしその差し出しのうちの少なくともひとつが受理されれば、
  差し出されたトークンは発生元から取り除かれ、受理者はそのコピーを受け入れる。

* ガードの失敗が原因でトークンを受理することに失敗する outgoing エッジは、
  それらトークンのコピーを受け入れてはならない。

* もしある ForkNode から生えている outgoing エッジでガードが利用されているならば、
  下流には ガードされたエッジを通じて渡されるトークンの到着に
  依存する JoinNodes がないことをモデル作者が保証しなくてはならない。
  それが回避できなければ、フォークとガード付きエッジとの間に
  DecisionNode を導入しなくてはならない。

15.3.3.4 Join Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* JoinNode は複数の流れを同期するノードである。
* JoinNode は厳密にひとつの outgoing エッジを持つものとする。
* JoinNode の incoming と outgoing のエッジの型は一致しているものとする。

* JoinNode は joinSpec という ValueSpecification を持つことが許される。
  これは合流がトークンを放つ条件を決定するものである。

  * ノードが joinSpec を持つ場合は、incoming エッジから新しいトークンが
    差し出されるといつでもこの条件が評価される。

  * もし joinSpec がテキスト表現で与えられるならば、
    incoming エッジの名前を使用して次のものを表してよい。

    #. ControlFlow からの差し出しの有無を示すブーリアン値か、
    #. ObjectFlow から差し出されたオブジェクトトークンに結び付けられた値

  * JoinNode が joinSpec を持たないならば、
    ブーリアン演算の AND で示される表現の joinSpec を持つものと等価として扱う。

  * JoinNode::joinSpec が真と評価されるとき、
    次の規則に従ってトークンが差し出される。

    #. incoming エッジで差し出されるすべてのトークンが制御トークンならば、
       ひとつの制御トークンが outgoing エッジに差し出される。

    #. incoming エッジで差し出されるトークンが制御トークンとオブジェクトトークンならば、
       オブジェクトトークンのみが outgoing エッジに差し出される。

       * JoinNode::isCombinedDuplicate が真ならば、
         複数トークンは重複があればそれらをまとめてから
         outgoing エッジに差し出される。

15.3.3.5 Merge Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* MergeNode は複数の流れを同期せずに結合する制御ノードである。
* MergeNode は厳密にひとつの outgoing エッジを持つものとする。
* MergeNode の incoming と outgoing のエッジの型は一致しているものとする。
* MergeNode に差し出されたトークンは、
  そのノードのすべての outgoing エッジに差し出される。
* 流れまたはトークンの合流の同期はない。

15.3.3.6 Decision Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* DecisionNode は outgoing の流れをひとつ選択するノードである。

* DecisionNode は第一 incoming エッジ上のトークンを受理し、
  それらをすべての outgoing エッジに差し出す。

* DecisionNode の outgoing エッジでガードを持つものがあれば、
  それらが各 incoming トークンに対して評価される。

* DecisionNode が decisionInputFlow を持つならば、
  第一 incoming エッジからのトークンが outgoing エッジに差し出されるよりも前に、
  第一 incoming エッジと decisionInputFlow の両方に差し出される必要がある。

* DecisionNode が decisionInput を持つならば、
  これは戻り値は持つがその他の出力引数は持たない Behavior である必要がある。

* DecisionNode の第一 incoming エッジが ControlFlow であり、
  DecisionNode が decisionInput を持つが decisionInputFlow を持たぬならば、
  decisionInput は入力引数を持ってはならない。

* DecisionNode の第一 incoming エッジが ObjectFlow であり、
  DecisionNode が decisionInput を持つが decisionInputFlow を持たぬならば、
  decisionInput は入力 Parameter を持たねばならない。

  * そして、第一 incoming エッジで差し出されたオブジェクトトークンに含まれる値は、
    Behavior がそのトークンに関係して発動されたときには、
    この Parameter を経て引き渡される。

* DecisionNode の第一 incoming エッジが差し出したトークンは、
  guard が偽に評価される outgoing エッジを通り抜けてはならない。

* 振る舞いが非決定的になることを回避するべく、
  モデル作者は各 incoming トークンに対して高々ひとつの
  guard が真であると評価されるように取り決めるものとする。

* 定義済みの guard ``else`` を高々ひとつの outgoing エッジに用いて構わない。
  このガードが真であると評価されるのは、
  DecisionNode から生えているその他のどの outgoing エッジも
  トークンを受理しないときに限る。

15.3.4 Notation
----------------------------------------------------------------------
* Figure 15.27 InitialNode notation

  * 既視感のある黒丸シンボル。

* Figure 15.28 FinalNode notation

  * ActivityFinal は黒丸を丸で囲むシンボル。
  * FlowFinalNode はマルバツシンボル。

* Figure 15.29 ForkNode and JoinNode notation

  * 両者とも太めの線分として記すが、向きは任意でよいらしい。
  * この線分に outgoing/incoming ActivityEdges のシンボルを必要に応じて接続する。

* Figure 15.30 joinSpec notation

  * 位置は線分の付近。
  * 中括弧に ``joinSpec = ...`` を含める。

* Figure 15.31 Combined JoinNode/ ForkNode notation

  * JoinNode と ForkNode が隣接？している状況では、両者を癒着できる。

* Figure 15.32 MergeNode notation

  * MergeNode 自体は白ダイヤモンドシンボルで表す。
  * ふたつ以上の incoming ActivityEdges および
    ひとつの outgoing ActivityEdge を持つ必要がある。

* Figure 15.33 DecisionNode notation

  * DecisionNode 自体は白ダイヤモンドシンボルで表す。
  * ひとつの incoming ActivityEdge および
    ふたつ以上の outgoing ActivityEdges を持つ必要がある。
  * decisionInput はキーワード ``«decisionInput»`` と共にコメントの記法で示す。
  * decisionInputFlow はキーワード ``«decisionInputFlow»`` をその矢印のそばに添える。

* Figure 15.34 Combined MergeNode/DecisionNode notation

  * MergeNode と DecisionNode はシンボルを共有することがある。
  * incoming/outgoing ActivityEdges シンボルを複数示すことになる。

15.3.5 Examples
----------------------------------------------------------------------
* Figure 15.35 InitialNode example

  * InitialNode から無条件で Receive Order ノードに至る。

* Figure 15.36 ForkNode example

  * Fill Order が完了したときに、ShipOrder と SendInvoice の
    両方に制御を引き渡す。

* Figure 15.37 JoinNode example

  * ShipOrder と SendInvoice の両方が完了したときに（同期）、
    Close Order に制御を引き渡す。

* Figure 15.38 joinSpec example

  * 自動販売機の制御が Dispense Drink に引き渡されるには、
    この joinSpec にある条件が満たされる必要がある。

* Figure 15.39 MergeNode example

  * 要注意。場合によっては Ship Item が二度実行される。

* Figure 15.40 DecisionNode example

  * 角括弧を用いることで分岐条件を柔軟に表現できる。

* Figure 15.41 DecisionNode example with decisionInput

  * decisionInput のコメントに分岐条件を書き下している。

* Figure 15.42 ActivityFinalNode example

  * Close Order 完了時に無条件で FinalNode に至る。

* Figure 15.43 ActivityFinalNode example

  * 開始直後の ForkNode でふたつの concurrent flows が始まる。
  * とにかくどちらの流れを経ても FinalNode に至る。

* Figure 15.44 ActivityFinalNode example

  * FinalNode をひとつにまとめても図の意味は変わらない。
  * Notify of Modification からは FinalNode に至らないことに注意（なぜか）。

* Figure 15.45 FlowFinalNode example

  * これは Build Component が反復的に実行すると解釈する。
  * それと同時？に Install Component が実行していることに注意。

* Figure 15.46 FlowFinalNode and ActivityFinalNode example

  * ActivityFinalNode に至るとすると、左側のループはもはや実行中ではないはず？

* Figure 15.47 ControlNode examples (...)

  * この Activity には既視感がある。

15.4 Object Nodes
======================================================================

15.4.1 Summary
----------------------------------------------------------------------
* ObjectNode は ActivityNode の一種で、
  Activity の実行中に値を含むオブジェクトトークンを保持するのに用いる。

* 本節では ObjectNode 一般の話を述べ、その具象型 3 種を述べる。

15.4.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 15.48 Object Nodes

  * ObjectNode と関連する要素の役割を理解したい。

15.4.3 Semantics
----------------------------------------------------------------------
15.4.3.1 Object Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ObjectNode は Activity の実行途中にオブジェクトトークンを保持する。

* ObjectNode は同じ値を持つ複数のオブジェクトトークンを含んでよい。

* ObjectNodes は TypedElements である。

* ObjectNodes は States の inState 集合を指定することも許される。

* ObjectNode はその upperBound がある場合、
  それが指定する値を超える個数のトークンを含むことは許されない。

* ObjectNode::ordering はどういう順序で
  その outgoing エッジに差し出されるトークンを決めるかを指定する。

  * unordered: 順序を定義しない。
  * FIFO
  * LIFO
  * ordered: selection Behavior を用いたモデル作者定義による順序とする。

* ObjectNode::ordering の値が ordered であるときに限り、
  この ObjectNode は selection Behavior を持たねばならない。

* ObjectNode::selection はそのノードの outgoing エッジにトークンがひとつ
  差し出された時にはいつでも実行される。

* ObjectNode::selection はそのノードの outgoing ObjectFlows で定義されている
  どの selection を以ってでも上書きされる。

* ordering のためにお互いを追い越すトークン (pl.) は、
  Activity の各発動がその Activity の別々の実行によって処理される
  場合からは独立している。

* ObjectNode::isControlType が真ならば、
  ControlFlows はそのノードの incoming および outgoing になってよろしい。
  オブジェクトトークン (pl.) は ControlFlows をたどることが可能である。

15.4.3.2 Activity Parameter Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Activity は Behavior の一種なので Parameters を持つことが許される。

* Activity の入出力は ActivityParameterNodes を用いて処理される。

* ActivityParameterNode は次のどちらか一方であるものとする。

  * すべてのエッジが incoming である
  * すべてのエッジが outgoing である

* Activity は
  入力引数、出力引数、戻り値それぞれに対応する ActivityParameterNode をひとつ、
  入出力引数それぞれに対応する ActivityParameterNodes をふたつ持たねばならない。

* 入力 ActivityParameterNode が非 streaming 引数に結び付けられていれば、
  Activity が発動された時に、その引数を用いて引き渡された値はいずれも
  オブジェクトトークン (pl.) に wrap され、
  Activity 実行の開始点にある ActivityParameterNode に配置される。

* Activity の実行途中では、オブジェクトトークン (pl.) は
  その Activity の出力 ActivityParameterNodes に流出してよい。

* 入力 ActivityParameterNode 非 streaming 引数に結び付けられていれば、
  新しい値がその引数に post されるときにはいつでも、
  その値がオブジェクトトークンに wrap されて、
  ActivityParameterNode に配置されて、すべての outgoing エッジに差し出される。

15.4.3.3 Central Buffer Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* CentralBufferNode は incoming ObjectFlows と outgoing ObjectFlows の間の
  緩衝材として振る舞う。
  具体的に言うと ordering に従ってオブジェクトトークンが処理される。

15.4.3.4 Data Store Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* DataStoreNode は Activity が実行している間は
  そのオブジェクトトークン (pl.) を永続的に保持する CentralBufferNode である。

* DataStoreNode が保持するオブジェクトトークンへの差し入れを
  下流のノードが受理するときに、
  差し出したトークンは（通常の CentralBufferNode の意味で）
  DataStoreNode から取り除かれる。

* DataStoreNode がオブジェクトトークンを受理するときに、
  もしそのノードがすでに同一のトークンを保持していれば、
  その DataStoreNode 上に重複してトークンを配置してはならない。
  CentralBufferNode とは異なり、DataStoreNode は一意なオブジェクト群を含む。

* outgoing ObjectFlows 上の selection と transformation Behaviors は、
  DataStoreNode の外側にある情報を取得するのに利用することが可能。

15.4.4 Notation
----------------------------------------------------------------------
* Figure 15.49 ObjectNode notations

  * ObjectNode は矩形とテキストで示す。
  * コレクションを表現する ObjectNode はそのようにラベルに示す。
  * Signal 付きの ObjectNode は矩形ではなく、初心者マークみたいな多角形で示す。
    左が凹で右が凸。

* Figure 15.50 ObjectNode annotations

  * 付随情報の表記法。

* Figure 15.51 Specifying selection behavior on an ObjectNode

  * ObjectNode の selection Behavior はコメントの記法を用いて示す。
  * キーワード ``«selection»`` が必要。

* Figure 15.52 Notation for stream and exception parameters

  * streaming Parameter に関連する ActivityParameterNode の記法は、
    文字列 ``{stream}`` をノードシンボルの近くに記すものとする。

  * 例外 Parameter に関連する ActivityParameterNode の記法は、
    小さな三角のシンボルをノードシンボルの近くに記すものとする。

* Figure 15.53 Presentation option for flows between pins and parameter nodes

  * Activity の上側の表現と下側の表現は等価である。
  * Parameters は Activity の境界でやり取りする。

* Figure 15.54 Optional CentralBufferNode notation

  * ObjectNode の記法に、オプションでキーワード ``«centralBuffer»`` を付けるものとする。

* Figure 15.55 DataStoreNode notation

  * ObjectNode の記法に、キーワード ``«datastore»`` を付けるものとする。

15.4.5 Examples
----------------------------------------------------------------------
* Figure 15.56 Example of ActivityParameterNodes for regular and exception Parameters

 * ここで見るべきは境界上のノードのみ。
 * Rejected Computer に三角が付いているので、
   このノードが例外である。

* Figure 15.57 Example of ActivityParameterNodes for streaming Parameters

  * 入出力どちらの ActivityParameterNodes でも streaming たり得る。
  * ちなみに streaming であることと例外であることは両立してはならない。

* Figure 15.58 CentralBufferNode example

  * 予備部品と採用部品の区別法を示していないことに注意。

* Figure 15.59 DataStoreNode example

  * selection Behavior の説明が欲しい。
  * Once a year というシンボルがあるが、これは Timer の類だろう。

15.5 Executable Nodes
======================================================================

15.5.1 Summary
----------------------------------------------------------------------
* ExecutableNode は ActivityNode の一種で、
  Activity の所望の振る舞い全体のうちの
  ひとつの段階として実行される。

* 本節では ExecutableNode の一般的な意味と、
  どの ExecutableNode も ExceptionHandler を
  付属させる能力を有することについて議論する。

* ExecutableNode のすべての具象型は Action であり、
  :doc:`./actions` で述べる。

15.5.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 15.60 Executable Nodes

  * ExecutableNode はひとつの ObjectNode に関連する ExceptionHandlers を所有する。
  * ExceptionHandler は Classifiers を例外の型として関連付ける。

15.5.3 Semantics
----------------------------------------------------------------------
15.5.3.1 Executable Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ExecutableNode はそれを含む Activity の実質的な (substantive) 振る舞いのステップを
  実施する ActivityNode である。

* ExecutableNode はすべての incoming ControlFlows がトークンを差し出すまでは
  実行してはならない。
  つまり、incoming ControlFlows 上には暗黙の join が存在する。

* ExecutableNode が実行を開始する前に、
  incoming ControlFlows において差し出されたすべてのトークンを受理する。

* ExecutableNode が実行している限り、
  ある単独の制御がそれが実行であることを示しているとみなされる。

* ExecutableNode が実行を完了するときは、
  その実行を表現している制御トークンがそのノードから取り除かれ、
  制御トークン (pl.) がそのノードの outgoing ControlFlows すべてに差し出される。
  つまり、ノードから outgoing ControlFlows の間に暗黙の fork が存在する。

15.5.3.2 Exceptions and Exception Handlers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* 例外とは、ある実行の完了様式が正常ではないことを確認するために用いられる値である。

* ExecutableNode は
  ExecutableNode (protectedNode) の外側に広まることもある例外 (pl.) を対処するための
  ExceptionHandlers (handlers) をひとつ以上持つことが許される。

* ExceptionHandler が例外を捕捉するならば、
  その例外はハンドラー用の execptionInput ノード上に設置されている
  あるオブジェクトトークンに wrap される。

* 例外捕捉後、ExceptionHandler::handlerBody が実行を完了するときに、
  あたかも protectedNode が正常に完了したかのごとき同じ方法で、
  制御トークンが ExceptionHandler::protectedNode の
  outgoing ControlFlows で差し出される。

* ExceptionHandler::handlerBody は incoming にせよ outgoing にせよ
  ActivityEdges を持ってはならない。

* ExceptionHandler::handlerBody は ExceptionHandler::protectedNode と同じ
  owner を持たねばならない。
  また、ExceptionHandler::exceptionInput を所有せねばならない。

* もし ExecutableNode がある例外を広めるのに、
  そのノードが handlers も
  広まった例外に match する handler も持たなければ、
  その例外はより外側へと広まり続ける。

15.5.4 Notation
----------------------------------------------------------------------
* Figure 15.61 ExecutableNode notation

  * ExecutableNode シンボルは角丸矩形。
  * ただし特殊型では記法も特殊化されるだろう。

* Figure 15.62 ExceptionHandler notation

  * ExceptionHandler は稲妻矢印として記す。

    * 矢印の始点は protectedNode である。
    * exceptionType の名前を稲妻のそばに記す。
    * 矢印の終点 exceptionInput ノードは小さい四角で示す。

* Figure 15.63 Alternative ExceptionHandler notation

  * 矢印自体を稲妻にする代わりに、ジグザグマークを
    普通の矢印に添えて ExceptionHandler としてもよろしい。

15.5.5 Examples
----------------------------------------------------------------------
* Figure 15.64 ExceptionHandler example

  * 何らかの（方程式を解く？）行列演算の Activity で、例外送出の仕様を表現している。
  * 逆行列が求まらない例外と、オーバーフローの例外を区別している。
  * 経過がどうあれ、Print Results は実行される。

15.6 Activity Groups
======================================================================

15.6.1 Summary
----------------------------------------------------------------------
* ActivityGroup はノードとエッジをグループ化する構成要素である。
* ノードとエッジは一個を超えるグループに所属することが可能である。
* 本節では ActivityGroup のふたつの具象型について述べる。

* StructuredActivityNode という具象型が存在するが、
  これについては :doc:`./actions` で議論する。

15.6.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 15.65 ActivityGroups

  * ActivityGroup の特殊型として ActivityPartition と InterruptibleActivityRegion がある。
  * ActivityGroup は subgraph を表現するためのものだろう。

15.6.3 Semantics
----------------------------------------------------------------------
15.6.3.1 Activity Partitions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ActivityPartition は ActivityGroup の一種で、
  何らかの共通する性質を持つ ActivityNodes を同一視するために用いるものである。

* ActivityPartitions はモデルのトークンの流れには影響を及ぼさない。
  その仕切りの containedNodes と containedEdges の実行によって
  発動する Behaviors について制約を加えたりビューを与えたりするものである。

  * 仕切りが表現する要素 (ActivityPartition::represents) の種類に従い、
    制約は異なる。

    * Classifier: この仕切りで発動した Behaviors は
      represents の Classifier のオブジェクトである責任がある。

    * InstanceSpecification: この仕切りで発動した Behaviors は
      represents の InstanceSpecification によりモデル化されるオブジェクトである責任がある。

    * Property: この仕切りで発動した Behaviors は
      represents の Property により保持されるオブジェクト (s./pl.) である責任がある。

  * ActivityPartition は上に挙げた以外の Elements を表現してもよろしいが、
    当仕様書はそれらの意味を定義しない。

* ActivityPartition は subpartitions を持ってよい。
  もし ActivityPartition::isDimension が真ならば、
  それは subpartitions を収めるための仕切りである。

* ActivityPartition がある Property を表現し、
  かつその subpartitions が InstanceSpecifications を表現するならば、
  その InstanceSpecifications はその Property が保持する値をモデル化するものとする。

* ActivityPartition がある Classifier::attribute Property を表現し、
  別の仕切りがそれを含むならば、
  その superPartition はその Classifier か、
  その Classifier が type となるある Property を表現するものとする。

* 非外部 ActivityPartition がある Classifier を表現し、
  別の仕切りに含まれているならば、その superPartition もまた
  ある Classifier を表現するものとし、
  その subpartition の Classifier は次のどちらかである必要がある。

  #. Classifier::nestedClassifier または Classifier::ownedBehavior である
  #. composition 関連の末尾に含まれる

* 外部 ActivityPartition とは isExternal の値が true であるものを指す。
  これは仕切りの構造の規則に対する作為的な例外である。

* ActivityPartitions は、
  実行のそれとしては不十分ではあるが、
  高水準のモデル作者によるレビューには不足のない情報を
  提供するのに利用されてもよい。

15.6.3.2 Interruptible Activity Regions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* InterruptibleActivityRegion は Activity の
  ある一部分の停止を支援する ActivityGroup である。

  * InterruptibleActivityRegion は ActivityNodes しか含まない。

* AcceptEventActions うんぬんは :doc:`./actions` でやろう。

* もし何らかの場合に領域内のすべてのフローを中止するのを望まないならば、
  InterruptibleActivityRegion を使わない。

15.6.4 Notation
----------------------------------------------------------------------
* Figure 15.66 ActivityPartition notations

  * 罫線を駆使して ActivityPartition を記す。
    この記法を swimlane と呼ぶ。

* Figure 15.67 ActivityPartition notations

  * 罫線による ActivityPartitions の図式化は実践的ではないことがある。
    その場合にはここで示す代替記法を検討する。

* Figure 15.68 InterruptableActivityRegion

  * InterruptableActivityRegion は破線丸角矩形で記す。
  * その interruptingEdge を先述の記法で記す。

* Figure 15.69 InterruptableActivityRegion alternative notation

  * 先述の通り interruptingEdge の矢印をストレートにしてジグザグマークを添えてもよい。

15.6.5 Examples
----------------------------------------------------------------------
* Figure 15.70 ActivityPartitions using swimlane notation

  * いつもの例題に swimlanes を明記したもの。
  * ところで swimlanes をまたぐ ActivityEdges は、
    どのサブ ActivityPartition の所属でもない。

* Figure 15.71 ActivityPartitions using annotation

  * 先の見本から swimlane を外したもの。
  * 丸括弧とキーワード ``«external»`` で所属する ActivityPartition がわかる。

* Figure 15.72 ActivityPartitions using multidimensional swimlane notation

  * 紙に描くものである以上、多次元と言っても高々 2 である。

* Figure 15.73 InterruptableActivityRegion example

  * InterruptableActivityRegion と凹五角形シンボルの組み合わせは使い易そうだ。

15.7 Classifier Descriptions
======================================================================
機械生成による節。

15.8 Association Descriptions
======================================================================
機械生成による節。

.. 15.8.1 A_containedEdge_inGroup [Association]
.. 15.8.2 A_containedNode_inGroup [Association]
.. 15.8.3 A_decisionInputFlow_decisionNode [Association]
.. 15.8.4 A_decisionInput_decisionNode [Association]
.. 15.8.5 A_edge_activity [Association]
.. 15.8.6 A_edge_inPartition [Association]
.. 15.8.7 A_exceptionInput_exceptionHandler [Association]
.. 15.8.8 A_exceptionType_exceptionHandler [Association]
.. 15.8.9 A_group_inActivity [Association]
.. 15.8.10 A_guard_activityEdge [Association]
.. 15.8.11 A_handlerBody_exceptionHandler [Association]
.. 15.8.12 A_handler_protectedNode [Association]
.. 15.8.13 A_inInterruptibleRegion_node [Association]
.. 15.8.14 A_inPartition_node [Association]
.. 15.8.15 A_inState_objectNode [Association]
.. 15.8.16 A_incoming_target_node [Association]
.. 15.8.17 A_interruptingEdge_interrupts [Association]
.. 15.8.18 A_joinSpec_joinNode [Association]
.. 15.8.19 A_node_activity [Association]
.. 15.8.20 A_outgoing_source_node [Association]
.. 15.8.21 A_parameter_activityParameterNode [Association]
.. 15.8.22 A_partition_activity [Association]
.. 15.8.23 A_redefinedEdge_activityEdge [Association]
.. 15.8.24 A_redefinedNode_activityNode [Association]
.. 15.8.25 A_represents_activityPartition [Association]
.. 15.8.26 A_selection_objectFlow [Association]
.. 15.8.27 A_selection_objectNode [Association]
.. 15.8.28 A_structuredNode_activity [Association]
.. 15.8.29 A_subgroup_superGroup [Association]
.. 15.8.30 A_subpartition_superPartition [Association]
.. 15.8.31 A_transformation_objectFlow [Association]
.. 15.8.32 A_upperBound_objectNode [Association]
.. 15.8.33 A_variable_activityScope [Association]
.. 15.8.34 A_weight_activityEdge [Association]

.. include:: /_include/uml-refs.txt
