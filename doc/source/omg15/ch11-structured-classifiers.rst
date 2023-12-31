======================================================================
11 Structured Classifiers
======================================================================

.. contents::
   :depth: 2

11.1 Summary
======================================================================

   StructuredClassifiers are Classifiers that may have an internal structure
   comprising a network of linked ``roles`` (which can themselves be instances of
   structured classifiers) and an external structure consisting of one or more
   Ports.

StructuredClassifier を定義している。次にその構成要素である Port
と、EncapsulatedClassifier という特殊型を述べている：

   The Ports of EncapsulatedClassifiers act as local agents of remote
   collaborators, allowing EncapsulatedClassifiers to differentiate between them
   but without being directly coupled to them.

11.2 Structured Classifiers
======================================================================

11.2.1 Summary
----------------------------------------------------------------------

   StructuredClassifiers may contain an internal structure of connected elements
   each of which plays a ``role`` in the overall behavior modeled by the
   StructuredClassifier.

11.2.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 11.1 Structured Classifiers

StructuredClassifier, ConnectableElementTemplateParameter, ConnectableElement,
Connector, ConnectorEnd, ``«enumeration»`` ConnectorKind がある。

``A_role_structuredClassifier``
  StructuredClassifier から ConnectableElement への関連（単方向）。

  * 先述したようにこの関連こそが StructuredClassifier の主な意味だ。
  * ``A_member_memberNamespace`` を subsets する。
  * 両端ともに ``{readOnly, union}`` 制約がある。

``A_ownedAttribute_structuredClassifier``
  StructuredClassifier から Property への複合関連（単方向）。

  * ``A_attribute_classifier``, ``A_ownedMember_namespace``,
    ``A_role_structuredClassifier`` を subsets する。
  * 関連端 ``ownedAttributes`` に制約 ``{ordered}`` を付ける。
  * 関連端 ``structuredClassifier`` を ``{redefines}`` する。

``A_part_structuredClassifier``
  StructuredClassifier から Property への単方向関連。

  * 上記 ``ownedAttributes`` で ``isComposite == true`` なものを ``parts`` とす
    る。

    * よって ``parts`` は ``roles`` の部分集合を構成する。

  * 関連端 ``part`` は ``{readOnly}`` だ。

``A_ownedConnector_structuredClassifier``
  StructuredClassifier から Connector への複合関連（単方向）。

  * Connectors を所有するのは StructuredClassifier だ。
  * ``A_feature_featuringClassifier``,
    ``A_redefinitionContext_redefinableElement``, ``A_ownedMember_namespace`` を
    subsets する。

``A_templateParameter_parameteredElement``
  ConnectableElementTemplateParameter と ConnectableElement の関連（双方向）。

  * 同名関連を redefines する。

``A_end_role``
  ConnectableElement と ConnectorEnd の関連（双方向）。

  * Connector の端点を一つ取れば、対応する ``role`` が一意に対応する。
  * 関連端 ``end`` は ``{readOnly}`` だ。

``A_definingEnd_connectorEnd``
  不明。説明文の意味を理解できない。

``A_end_connector``
  Connector から ConnectorEnd への複合関連（単方向）。

  * 先述した定義により関連端 ``end`` の多重度は ``2..*`` だ。
  * 関連端 ``end`` は ``{ordered}`` だ。
  * ``A_ownedElement_owner`` を subsets する。

``A_contract_connector``
  Connector から Behavior への関連（単方向）。

  * その Connector を横断する有効な相互作用のパターンを指定することが許されてい
    る。

``A_type_connector``
  Connector から Association への関連（単方向）。

  * Connector が指定するリンクがどの Association の型のオブジェクトであるかを指
    定することが許されている。

``A_redefinedConnector_connector``
  Connector から Connector への関連。

  * Connector が含む Classifier が何かの特殊化であるときに、再定義することが許されて
    いる。このとき、Association (``type``) や ConnectorEnds (``ends``) の型もそ
    れぞれの特殊化にすることが許されている。さらに ConnectorEnds の Property は
    置き換えてもよい。

11.2.3 Semantics
----------------------------------------------------------------------

11.2.3.1 Connectable Elements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   ConnectableElement is an abstract metaclass. Each ConnectableElement
   represents a participant within the internal structure of a
   StructuredClassifier; these participants are called ``roles``. ``Roles`` may
   be joined by Connectors, and specify configurations of linked instances
   contained or referenced within an instance of the containing
   StructuredClassifier.

まず、ConnectableElement が ``role`` と呼ばれることと、それらが Connector で結合
することを押さえる。ConnectableElement の詳細な意味論はその具象型が与える：

   In general, each ConnectableElement exhibits a set of *effective required
   Interfaces* and a set of *effective provided Interfaces*.

これらの集合が後述する Connector を使用して ConnectableElement の接続可能性を決
定するのに用いられる。

   For ConnectableElements except delegating Ports (see 11.3.3) the effective
   required Interfaces are the required Interfaces, and the effective provided
   Interfaces are the provided Interfaces, derived as follows:

委譲 Port というものを例外的に扱う場合があるということを頭の片隅に入れて読み進め
る。

* ``provided`` Interface は ConnectableElement の ``type`` とその上位型の
  ``type`` により実現される Interfaces の集合（複数形）の和集合からなる。
  Interface によって型付けされている場合は、ちょうどその ``type`` しか含まない集
  合の和からなる。
* ``required`` Interface は ConnectableElement とその上位型の ``type`` により用
  いられる Interfaces の集合（複数形）の和集合からなる。

ConnectableElementTemplateParameter との関係：

   A ConnectableElement may be exposed via a ConnectableElementTemplateParameter
   as a formal parameter for a template.

これに対する意味と記法は ConnectableElement が Property である場合にしか定義され
ない。9.5 節参照。

11.2.3.2 Parts and Roles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

StructuredClassifier の Properties は :doc:`./ch09-classification` で指定される
意味に従う。

Property は ConnectableElement の一種だ。StructuredClassifier の
``ownedAttributes`` のすべてが ``roles`` であり、Connectors を使って接続すること
が可能だ。

   Those ``ownedAttributes`` of a StructuredClassifier that have ``isComposite``
   = true (see 9.5.3) are called its ``parts``.

それゆえ ``parts`` は ``roles`` の部分集合を構成する。

11.2.3.3 Connectors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A Connector specifies *links* (see 11.5 Associations) between two or more
   instances playing owned or inherited ``roles`` within a StructuredClassifier.

* リンクそれぞれはポインターのような簡単なものや、ネットワーク接続のような複雑な
  ものまである。
* リンクそれぞれは引数として渡されたり、変数やスロットに保持されることでオブジェ
  クトが識別されたり、あるいは通信オブジェクトが同じオブジェクトであることで通信
  可能であったりすることを表現することが許される。

Connector と Association の違い：

   In contrast to Associations, which specify links between any suitably-typed
   instance of the associated Classifiers, Connectors specify links between
   instances playing the connected ``roles`` only.

各 Connector は二つ以上の ConnectableElement に接続することが許される。それぞ
れ、包含 StructuredClassifier のオブジェクト化に寄与するオブジェクトの集合を表
す。

ConnectorEnd 定義：

   A ConnectorEnd is an endpoint of a Connector, which attaches the Connector to
   a ConnectableElement.

Connector に対応するリンクは含んでいる StructuredClassifier の生成時に作成するこ
とが許される。そのようなリンクはすべて、含んでいる StructuredClassifier オブジェ
クトが破棄されたときに破棄される。

Connector は Association によって型付けされることがある。その場合、Connector が
指定するリンクは型付けする Association のオブジェクトだ。

次の記述が急所のはずなのだが、難しくて理解できない：

   Each feature of each of the *effective required Interfaces* of each
   ConnectableElement at the end of a Connector must have at least one
   compatible feature among the features of the *effective provided Interfaces*
   of ConnectableElements at the other ends. One feature is compatible with
   another at least in the cases when the two features are the same or when they
   are both properties or operations and the second feature is a redefinition of
   the first.

単一の ConnectableElement に複数の連結器が接続されていることは、その
ConnectableElement を複数の連結器を介して接続された ConnectableElements のすべて
に接続する単一の多項連結器があることと同じ意味になる。

Connectors には種類があり、その値は ``assembly`` か ``delegation`` だ。

ConnectorKind は次のリテラル値の列挙体だ：

``assembly``
  Connector は ``assembly`` Connector だ。
``delegation``
  Connector は ``delegation`` Connector だ。

Behaviors は Connector 全体で有効な相互作用パターンを指定する ``contracts`` とし
て、Connector に関連付けてもよい。

11.2.3.4 Multiplicities and topologies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ConnectableElements の多重度は MultiplicityElement の意味に従い、含んでいる
StructuredClassifier のオブジェクト内部で生成が許されるオブジェクトの個数を制約
する。

* 二項 Connector の場合、ConnectorEnd の多重度は他方の関連端での
  ConnectableElement のオブジェクトそれぞれにリンクすることが許されるオブジェク
  トの個数を示す。
* 多項 Connector の場合、一方の関連端の多重度は他方の関連端それぞれについて、一
  つの特定のオブジェクトを含む集合を参照することが許されるリンクの個数を制約す
  る。

..

   When an instance is removed from a ``role`` of an instance of a
   StructuredClassifier, links that exist due to Connectors between that
   ``role`` and others are destroyed.

ConnectorEnds の多重度およびそれらが相互接続する ConnectableElement の多重度を
マッチングさせた結果のトポロジーは、モデルからいつでも推論可能であるわけではな
い。

11.2.4 Notation
----------------------------------------------------------------------

StructuredClassifier の内部構造は名前が ``internal structure`` で分離区画に示
す。この区画は必須だ。

* 内部構造区画は ``roles`` と連結器を表す記号を含む。
* 内部構造区画は属性区画と操作区画の下にある。

``part`` は内部構造区画の内側で ``part`` を表す実線輪郭の箱記号の図式的な入れ子
で示されることがある。複合ではない ``role`` は破線輪郭の箱記号の図式的な入れ子で
示されることがある。いずれの場合も：

   the box may be called a *part box*, even though strictly-speaking only the
   compositions are ``parts``. Lollipop and socket symbols may optionally be
   shown to indicate the provided and required interfaces of the ``part``, using
   the same notation as for the definition of the ``part’s`` type (see 10.4.4).

Property に対する多重度は、部品箱の右上隅に多重度マークとして示してもかまわな
い。

   When a ``role`` is typed by an EncapsulatedClassifier (see 11.3), any Ports
   of the ``type`` may also be shown as small square symbols overlapping the
   boundary of the part box denoting the ``role``.

* Port の ``name`` はその近くに表示され、多重度は角括弧で囲まれた ``name`` の後
  に表示される。
* 名前と多重度は省略することができる。
* Port の定義（11.3.4 参照）と同じ記法で、Port の provided Interface と required
  Interface を示すために、ロリポップ記号とソケット記号を任意に表示してもよい。

``role`` が Class 以外の Classifier 型の場合、部品箱記号の名前区画には名前の上に
``«component»`` のようなキーワードが適宜含まれる。

Connector は Association と同様の記法で描く：

.. code:: bnf

   <connector> ::= ( [<name>] ‘:’ <associationname> )
       | ([<name>] ‘:’ <associationclassname> )
       | [<name>]

ここで、``<name>`` は Connector の名前、``<associationname>`` または
``<associationclassname>`` はその型である Association または AssociationClass の
それぞれの名前だ。

   Adornments may be shown on the ConnectorEnd using the same notation as
   adornments on Association ends. If no multiplicity is shown, the multiplicity
   matches the multiplicity of the ``role`` the end is attached to.

ConnectorEnd が内部構造の ``part`` または ``role`` のPortに接続され、多重度が表
示されていない場合、ConnectorEnd の多重度は Port の多重と ``role`` の多重度（あ
る場合）の積に等しい。

以降の記法仕様はオプションであり、適合するツールでもそれらを実装するには及ばな
い。

* ``parts`` に単純な Ports があるならば、ball and socket 記法を Ports 間の
  ``assembly`` Connectors を表すのに用いてもよい。
* 単純 Ports を接続するときには ``assembly`` または ``delegation`` に対しての
  普通の Connector 表記法を Port 記号自身へではなく ball and socket 記号へ接続
  されるように（？）示してよい（原文で動詞が二つあるような？）。
* 二つを超える単純 Ports を接続する多項 Connector があり、二つまたはそれを超える
  Ports が同じまたは互換な Interfaces を与えるか要求するときには、Interface を表
  す単一の記号が示されることが可能であり、Components から伸びる線がその記号へ引
  かれることが可能だが、これは channeled ball and socket表記法だ。

内部構造区画は CollaborationUses を表す記号を含んでもよいが、それは 11.7.4 で
記される表記法に従う。

11.2.5 Examples
----------------------------------------------------------------------

   Figure 11.2 Parts and roles

部品箱の例。左の部品箱は（これ単品で）包含するオブジェクトが複合によって ``Wheel``
オブジェクト四つを所有することを表している。

右の破線枠のほうは複合ではないオブジェクト。包含するオブジェクトが ``Engine`` オ
ブジェクト一個または二個を参照することを表している。

* 多重度は箱の右上隅に表示されている。
* 実線が複合で、破線が参照で「持つ」ことを表す？

   Figure 11.3 Parts and roles with Ports

Ports を持つ EncapsulatedClassifiers によって型付けされた特性の部品箱。

``Wheel`` 側からはボールが、``Engine`` 側からはソケットが生えている。どちらも箱
の枠線に重なる小さい四角がある。

   Figure 11.4 Alternative notations for connecting parts and roles with Ports

StructuredClassifier 内の ``parts`` と ``roles`` に単純な Port を接続する表記が
三つある。

* 最初の例は、接続線が Port 記号自体に結合している（内部構造で Ports を接続する
  唯一の必須記法）。
* ボールとソケットが Port の provided Interface と required Interfaces を示す。
* 最後の例はボールとソケットの表記（だけが）用いられている。

   Figure 11.5 Associations compared with Connectors

(i) は見慣れた図式。(ii) は (i) が表現していることに加えて、クラス ``Car`` の内
部構造に ``rear`` と ``e`` が所属していることが指定されている。

   This allows specification of detail that holds only for instances of the
   ``Wheel`` and ``Engine`` classes within the context of the class ``Car``, but
   which will not hold for wheels and engines in general.

内部構造の図式のほうは、クラス ``Wheel`` と ``Engine`` のオブジェクトが、クラス
``Car`` のオブジェクト内でそれぞれの役割を果たしている場合に、さらなる制約を主張
する。これらの制約が ``Wheel`` と ``Engine`` のオブジェクト一般には当てはまらな
い。見慣れた図式の方が表しているのが一般の場合だ。

   Figure 11.6 "Star" Connector pattern

内部構造で ``role`` 役割を果たす各オブジェクトについて、その ``role`` に付属する
Connectors の反対側の端の多重度が低いほど、リンクが多く初期に存在することにな
る。

(i) で定義されるように、端の多重度がそれらが接続されている ``roles`` の多重度と
一致する場合、包含 StructuredClassifier のオブジェクトが作成されるときに作成され
る初期構成は、（``roles`` の多重度で指定される）``roles`` に対応するオブジェクト
の集合がリンクによって完全に接続されていることから構成される。(ii) はそれを表現
している。

   Figure 11.7 "Array" Connector pattern

   Links will be created for each instance playing the connected ``roles``
   according to their ordering until the minimum ConnectorEnd multiplicity is
   reached for both ends of the Connector;

その結果、(ii) が表現するオブジェクトになる。この例ではリンクが二つしか作成され
ていない。

   Figure 11.8 An assembly Connector maps a simple Port of a Component to a
   matching simple Port of another Component.

単純 Ports のついた Component によって型付けされた ``parts`` の記法例と、互換性
のある Ports 間の組み立て Connector を表現するボールとソケット記法（こちらはオプ
ショナル）。

左側の Component 定義を assemble すると右側の parts になると言っている？

   Figure 11.9 An n-ary Connector that assembles four simple Ports using
   channeled ball-and-socket notation.

四項 Connector の channeled ball and socket 記法の見本。

   The two simple Ports that require Person have been channeled into a single
   socket, and the two simple Ports that provide Person (either directly or
   indirectly) have been channeled into a single ball.

* ボールのほうが provided Interfaces; Client is-a Person とのこと。
* ソケットのほうが required Interfaces

11.3 Encapsulated Classifiers
======================================================================

11.3.1 Summary
----------------------------------------------------------------------

   EncapsulatedClassifier extends StructuredClassifier with the ability to own
   Ports, a mechanism for isolating an EncapsulatedClassifier from its
   environment.

11.3.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 11.10 Encapsulated Classifiers

EncapsulatedClassifier と Port の関連を中心とした図式。

``A_ownedPort_encapsulatedClassifier``
  EncapsulatedClassifier から Port への複合関連（単方向）。

  * EncapsulatedClassifier は複数の Ports を定義する能力があり、相異なる通信をそ
    れが起こる Port に基いて区別することが可能になる。
  * ``A_ownedAttribute_structuredClassifier`` を subsets する。
  * 関連端 ``ownedPort`` は ``{readOnly}`` だ。

``A_required_port``
  Port から Interface への関連（単方向）。

  * 関連端 ``required`` は ``port`` を通じて EncapsulatedClassifier から環境への
    依頼を特徴づける Interfaces だ。EncapsulatedClassifier オブジェクトは
    ``required`` Interfaces が所収する Features が、環境下の一つ以上のオブジェク
    トが提示することを期待している。
  * 関連端 ``required`` は ``{readOnly}`` だ。

``A_provided_port``
  Port から Interface への関連（単方向）。

  * 関連端 ``provided`` は ``port`` を通じて EncapsulatedClassifier への、環境が
    作る依頼を特徴づける Interfaces だ。所有者である EncapsulatedClassifier は
    ``provided`` Interfaces が所有する Features を提示する必要がある。
  * 関連端 ``provided`` は ``{readOnly}`` だ。

``A_protocol_port``
  Port から ProtocolStateMachine への関連（単方向）。

  * Port で発生する Operation と Reception の発動の有効な順序を述べるのに
    ProtocolStateMachine を一つ参照してもよい。

``A_redefinedPort_port``
  Port から Port への関連（単方向）。

  * EncapsulatedClassifier が特殊化されているときに Port は再定義してもよい。
    再定義先の Port では Interfaces を追加したり置換したりしてよい。
  * ``A_redefinedProperty_property`` を subsets する。

``A_partWithPort_connectorEnd``
  ConnectorEnd から Property への関連（単方向）。

  * Port-on-Property の場合に ConnectorEnd が参照する実際の接続先 Property を表
    す。

11.3.3 Semantics
----------------------------------------------------------------------
11.3.3.1 Ports
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Ports represent interaction points through which an EncapsulatedClassifier
   communicates with its environment.

* EncapsulatedClassifier に対して Ports を複数定義可能。異なる通信が発生する
  Port に基づいて区別することを可能にする。
* EncapsulatedClassifier の内部を環境から疎結合することで、Ports は
  EncapsulatedClassifier がその環境から独立して定義できるようにし、その Ports が
  課す制約に適合する環境のどれでも EncapsulatedClassifier が再利用可能にする。

   A Port is a Property of an EncapsulatedClassifier that specifies a distinct
   interaction point between that EncapsulatedClassifier and its environment or
   between the Behavior of the EncapsulatedClassifier and its internal
   ``roles``.

* Port は Connectors で接続され、これを通じて EncapsulatedClassifier の
  BehavioralFeatures の呼び出しを要求することが可能だ。
* Port は EncapsulatedClassifier がその環境に提供するサービスと、
  EncapsulatedClassifier がその環境に期待するサービスを指定することが許される。

   The property ``isService``, when true, indicates that this Port is used to
   provide the published functionality of an EncapsulatedClassifier. If false,
   this Port is used to implement the EncapsulatedClassifier but is not part of
   the essential externally-visible functionality of the EncapsulatedClassifier

後者の場合、EncapsulatedClassifier の本質的な外部から見える機能の一部ではないた
め、EncapsulatedClassifier の内部実装やその実装の一部と見なされる他のプロパ
ティーとともに変更または削除することが可能だ。

   The phrase *Port on Part* or more generally *Port on Property* signifies the
   situation where a Property playing a role in a StructuredClassifier is typed
   by an EncapsulatedClassifier that has Ports.

包含 StructuredClassifier 内の Connector はこれらの Ports の一つに接続してもよ
い。このような場合、該当する ConnectorEnd の特性 ``partWithPort`` は接続される実
際の Property を参照する。一般的に、同じ EncapsulatedClassifier によって型付けら
れた構造内の Property が多く存在する場合があり、正しいものを示すために
``partWithPort`` が用いられる。

   The Interfaces associated with a Port specify the nature of the interactions
   that may occur over it.

Port の ``required`` Interfaces はこの Port を通じて EncapsulatedClassifier から
その環境に対して行われることがある要求を特徴づける。この EncapsulatedClassifier
のオブジェクトは、その ``required`` Interfaces が所有する Features が、その環境
内の一つ以上のオブジェクトによって提供されることを期待する。Port の ``provided``
Interfaces はその環境がこの Port を通して行う可能性のある EncapsulatedClassifier
への要求を特徴づける。所有 EncapsulatedClassifier は、``provided``
Interfaces が所有する Features を提供しなければならない。

   As a kind of Property, a Port has a ``type``.

Port の ``provided`` および ``required`` Interfaces は ``isConjugated`` の値によ
り仲介されたそれの ``type`` に、以下のように関係する：

* ``isConjugated`` が ``true`` だと、``provided`` は Port の ``type`` およびそれ
  の上位型が用いる Interfaces の和集合として導出される。それに対して、
  ``required`` は Port の ``type`` およびそれの上位型が実現する Interfaces の和
  集合として、または Port がある Interface によって型付けられている場合には Port
  の``type`` から直接導出される。
* ``isConjugated`` が ``false`` だと、``provided`` は Port の ``type`` とその上
  位型が実現する Interface の和集合として、または Port が Interface によって型付
  けられている場合には Port の ``type`` から直接導出される。``required`` は Port
  の ``type`` とその上位型によって用いられる Interface の和集合として導出される。

..

   The Interfaces do not necessarily establish the exact sequences of
   interactions across the Port.

Port のプロトコルは、この Port で発生することがある Operation と Reception の呼
び出しの有効な手順を記述した ProtocolStateMachine を参照してもよい。

   When an instance of an EncapsulatedClassifier is created, instances
   corresponding to each of its Ports are created and held in the slots
   specified by each Port, in accordance with its ``type`` and multiplicity.
   These instances are referred to as “interaction points” and provide unique
   references.

したがって、EncapsulatedClassifier オブジェクトはその異なる Ports を対象とした
BehavioralFeature の呼び出しのための要求を区別することが可能だ。同様に、そのよう
な要求を Port に差し向けることが可能であり、要求はこの Port に接続された
Connector に対応するリンクによって指定されるように経由させられることになる。

   NOTE. In the following, “requests arriving at a Port” shall mean “request
   occurrences arriving at the interaction point of this instance corresponding
   to this Port.”

..

   A Port has the ability, by setting the property ``isBehavior`` to true, to
   specify that any requests arriving at this Port are handled by the Behavior
   of the instance of the owning EncapsulatedClassifier, rather than being
   forwarded to any contained instances, if any. Such a Port is called a
   :dfn:`behavior Port`.

この EncapsulatedClassifier に定義されたBehavior がない場合、behavior Port に到
着した通信はすべて失われる。

   A :dfn:`delegation` Connector is a Connector that links a Port to a ``role``
   within the owning EncapsulatedClassifier.

* 委譲 Connector は Operation 呼び出しと Signal の転送を表現する。
* 一つ以上の Properties または Properties 上の Ports への委譲 Connector を持つ
  Port に到着した要求は、処理のためにそれらの標的へ渡される。

EncapsulatedClassifier が提供するサービスが、最終的にその内部に複数階層の入れ子
で実現されるような、動作の階層的な分解をモデル化するのに委譲 Connectors を用いる
ことが可能だ。

次の記述で effective の意味が明確になったと思われる：

   As a ConnectableElement, the *effective provided Interfaces* (see 11.2.3) of
   a Port are its provided interfaces, and the *effective required Interfaces*
   are its required Interfaces. However, for a *delegating Port*, i.e., a Port
   that is at an end of a delegation Connector and is not on a ``role`` and that
   is not a behavior Port, the *effective provided Interfaces* are its required
   interfaces and its *effective required Interfaces* are its provided
   interfaces.

その結果、委譲 Port は、あたかも外側の「顔」の共役である内側の「顔」を持っている
かのように、接続に対して動作すると仕様書は説明している。

   If several Connectors are attached on one side of a Port, then any request
   arriving at this Port on a link derived from a Connector on the other side of
   the Port will be forwarded on links corresponding to these Connectors.

これらの要求がすべてのリンクで転送されるか、それらのリンクのうちのどれかだけで転
送されるかは定義されていない。

11.3.4 Notation
----------------------------------------------------------------------

EncapsulatedClassifier の Port は小さい正方形で示す。

* Port の名前を正方形の近くに置く。
* Port 記号は EncapsulatedClassifier を示す矩形記号の境界と重ね合わせてもよい
  し、矩形記号の内側に示してもよい。
* 内部構造区画にある ``parts`` や ``roles`` など、EncapsulatedClassifier の区画
  に視覚的に含まれる要素に Port が接続しているときは、Port 記号はその区画の境界
  の内部に配置するか、重なり合うように配置しなければんらない。

Port の ``type`` を名前に続けてコロンで区切って表示してもよい。

* Port に対する ``isConjugated`` が真の場合、Port の ``type`` はチルダ ``~`` を
  前に付加して示される。
* ``provided`` Interface は Port に付属するロリポップ表記で示してよい。
* ``required`` Interface は Port に付属するソケット表記で示してよい。

動作 Portは、EncapsulatedClassifier を含む記号内に描かれた小さな状態記号に、Port
が線を介して接続されていることで示される。小さな状態記号は包含
EncapsulatedClassifier の Behavior を示す。

   The name of a Port may be suppressed. Every depiction of an unnamed Port
   denotes a different Port from any other Port.

一つの Port に Interfaces が複数関連付けられている場合、これらの Interfaces をカ
ンマで区切って一つの Interface ロリポップに列記してよい。

``required`` Interface の単純 Port から ``provided`` Interface の単純 Port に配
線される Dependency では、ソケットからロリポップへと結ぶ依存関係矢印を表示するか
は記法上任意だ。

11.3.5 Examples
----------------------------------------------------------------------

   Figure 11.11 Port notation

Ports に対する表記法を説明する図だ。

* 図の上側の意味は学習済み。
* 図の下側

  * ``p`` は ``Engine`` 上の Port だ（∵小さい四角の位置）
  * ``p`` の型は ``PowerTrain`` だ（∵ ``p`` のラベル）
  * ``p`` の ``provided`` Interface は ``IPowerTrain`` だ（∵ロリポップのラ
    ベル）
  * ``p`` の ``required`` Interface は ``IFeedback`` だ（∵ソケットのラベ
    ル）
  * ``p`` の多重度は 1 だ（∵明示されていない）
  * ``p`` の ``isConjugated`` は ``false`` だ（∵ ``p`` の名前に ``~`` がな
    い）
  * ``e`` は練習問題とする。

   Figure 11.12 Behavior Port notation

``Engine`` の ``Behavior`` を表す小さな状態記号に接続された動作 Port ``p`` の図
式。

* その ``type`` は先の例同様 ``PowerTrain`` だ。
* ``p`` のラベルの位置と、小さい四角にくっついたオマケの記号に注意。

   Figure 11.13 Port notation showing multiple provided Interfaces

二つの ``provided`` Interfaces, ``OrderEntry`` と ``Tracking`` がある Class
``OrderProcess`` にくっついている Port ``OnlineServices`` を示す。ロリポップに
``provided`` Interfaces の名前を二つまとめて示す。

   Figure 11.14 Port examples

``provided`` Interface だ ``IPowerTrain`` により型付けられた Port ``p`` がある
Class ``Engine`` を示す図。

右側の ``Car`` と ``Boat`` の内部構造それぞれの Port の付き方の違いを説明できる
ようにしておくこと。

* ``Car`` も ``Boat`` も ``Engine`` となる部品を含む。
* ``Car`` は ``Engine`` の Port ``p`` を ``axle`` を介して ``Wheel`` 二つに接続
  する。
* ``Boat`` は ``Engine`` の Port ``p`` を ``shaft`` を介して ``Propeller`` に接
  続する。

この例は Connectors が必ずしも Port を介して部品に接続する必要がないことも示して
いる。Ports が単純であるため、Boat 内の Connector の描写は Figure 11.4 に示され
るどの表記方法でも可能だ。

11.4 Classes
======================================================================

11.4.1 Summary
----------------------------------------------------------------------

   Class is the concrete realization of EncapsulatedClassifier and
   BehavioredClassifier. The purpose of a Class is to specify a classification
   of objects and to specify the Features that characterize the structure and
   behavior of those objects.

この二つの派生型であるから、Class の目的はそうなるのが当然だ。

11.4.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 11.15 Classes

Class は自らを再定義する関連と、何かを所有するといういくつかの関連が加わる程度。

``A_superClass_class``
  Class から Class への関連（単方向）。

  * Class は継承することができる。
  * ``A_general_classifier`` を ``class`` 側で subsets し、``superClass`` 側で
    redefines する。

``A_nestedClassifier_nestingClass``
  Class から Classifier への複合関連（単方向）。

  Class のスコープ内にいくつか Classifiers を入れ子で含めることがあり、Class は
  それらに対する名前空間として振る舞う。

  * ``A_ownedMember_namespace``, ``A_redefinitionContext_redefinableElement`` を
    subsets する。
  * 関連端 ``nestedClassifier`` は ``{ordered}`` だ。

``A_ownedAttribute_class``
  Class から Property への複合関連（双方向）。

  * Class の Features の内 Properties なものだ。
  * Class の Attributes は、その Class が所有する Properties だ。これらの属性の
    うちいくつかは二項 Attributes の関連端を表現する。
  * ``A_attribute_classifier``, ``A_ownedMember_namespace``,
    ``A_ownedAttribute_structuredClassifier`` を subsets する。
    ``ownedAttributes`` は redefines する。
  * 関連端 ``ownedAttributes`` は ``{ordered}`` だ。

``A_ownedOperation_class``
  Class から Operation への複合関連（双方向）。

  * Class の Features の内 Operations なものだ。
  * Class の Operations は（何らかのパラメーターを伴って）オブジェクトの上で発動
    される。
  * ``A_feature_featuringClassifier``, ``A_ownedMember_namespace``,
    ``A_redefinitionContext_redefinableElement`` を subsets する。
  * 関連端 ownedOperation は ``{ordered}`` だ。

``A_ownedReception_class``
  Class から Reception への複合関連（単方向）。

  * ``A_feature_featuringClassifier``, ``A_ownedMember_namespace`` を subsets す
    る。

``A_extension_metaclass``
  Class から Extension への関連（双方向）。

  * 両端ともに ``{readOnly}`` だ。

11.4.3 Semantics
----------------------------------------------------------------------

11.4.3.1 Classes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Class is a kind of EncapsulatedClassifier whose Features are Properties,
   Operations, Receptions, Ports and Connectors.

Class の属性は所有する Properties だ。これらの ``attributes`` の中には二項
Association の端点を表現するものがある。

   Objects of a Class must contain values for each ``attribute`` that is a
   member of that Class, in accordance with the characteristics of the
   ``attribute``, for example its ``type`` and multiplicity.

これは当然そう理解している。

Class でオブジェクトが生成されると、既定値が指定された Class の ``attribute`` そ
れぞれに対して、``attribute`` の初期値がそのオブジェクト生成のために明示的に指定
されていなければ、既定の ValueSpecification が評価されて、オブジェクトに対する
``attribute`` の初期値を設定する。

   Operations of a Class can be invoked on an object, given a particular set of
   values for the parameters of the Operation, according to the semantics
   specified in 9.6.3.

次は private および protected の意味を述べている：

   A Class cannot access private Features of another Class, or protected
   Features on another Class that is not its ancestor.

Class は名前空間としての機能も有する：

   A Class acts as the namespace for various kinds of Classifiers defined within
   its scope, including Classes.

入れ子の Classifiers はその Class を含む名前空間の要員だ。Classifiers の入れ子は
情報隠蔽の理由から用いられる。

   A Class may be designated by setting ``isActive`` to true as active (i.e.,
   each of its instances is an active object). When ``isActive`` is false the
   Class is passive (i.e., each of its instances executes within the context of
   some other object).

突然 active/passive という概念が出現する。その定義はこうだ：

   An active object is an object that, as a direct consequence of its creation,
   commences to execute its ``classifierBehavior``, and does not cease until
   either the complete Behavior is executed or the object is terminated by some
   external object. (This is sometimes referred to as “the object having its own
   thread of control.”)

何やら並行処理を感じさせる記述だ。

* 能動的オブジェクトが他のオブジェクトからの通信に応答する時点は、能動的オブジェ
  クトの Behavior のみにより決定される。呼び出されたオブジェクトによって決定され
  ることはない。
* 能動的オブジェクトの ``classifierBehavior`` が完了すると、そのオブジェクトは終
  了する。

次の記述からは、UML で言う Reception は Qt で言う Slot に相当する概念だと思われ
る：

   A Class’s Receptions specify which Signals the instances of this Class
   handle.

InstanceSpecification を Class に適用する：

   An InstanceSpecification may be used to specify the initial value to be
   created for a Class.

Class のオブジェクトが削除されるときには、その Class の ``parts`` オブジェクト
と Ports に対応するオブジェクトのすべてが再帰的に削除される。

Class は Profiles とメタモデルの定義でメタクラスとして振る舞ってよい。
:doc:`./ch12-packages` で見ていく。

11.4.4 Notation
----------------------------------------------------------------------

Class は Classifier の記号で示す。最も広く用いられる Classifier であるた
め、メタクラスが Class であることを示すキーワードは不要だ。

存在必須区画が四つある。それぞれ ``attributes``, ``operations``, ``receptions``,
``internal structure`` だ。

Class の ``operations`` 区画には :doc:`./ch12-packages` で規定された記法による
``ownedOperations`` を、``receptions`` 区画には :doc:`./ch10-simple-classifiers`
で規定された記法による ``ownedReceptions`` をそれぞれ格納する。

   A usage dependency may relate an InstanceSpecification to a constructor for a
   Class, describing the single value returned by the constructor Operation. The
   Operation is the client, the created instance the supplier.

* Operation が ``client`` であり、生成オブジェクトが ``supplier`` だ。
* InstanceSpecification は Operation が宣言した引数を参照してもよい。
* コンストラクターは所有 Class の単一の戻り値を持つ Operation であり、標準ステレ
  オタイプ ``«Create»`` でマークされる。

..

   The InstanceSpecification that is the supplier of the usage dependency
   represents the default value of the single return result parameter of a
   constructor Operation.

``isActive`` が真である Class は、箱枠の両脇枠を二重にして示してよい。

メタクラスを表現する Class はオプションのステレオタイプ ``«Metaclass»`` をその名
前の上または前に付すことで拡張してよい。:doc:`./ch22-standard-profile` を参照。

11.4.5 Examples
----------------------------------------------------------------------

   Figure 11.16 Class notation variants

同じ Class Window を三通りの記法で示した。右へ行くほど詳細になる。

可視性が指定されていない Operations があるが、実際に指定されている可視性を答えら
れるようにしておくこと。

   Figure 11.17 Class notation: attributes and Operations grouped according to
   visibility

可視性で属性と操作をグループ化できる。どこか C++ のコードを思わせるような記法。

   Figure 11.18 Active Class

能動的 Class では箱枠の両脇を二重線で描く。

   Figure 11.19 Connectors and Parts

``Car`` オブジェクトが生成するときは常に四つの ``Wheel`` オブジェクトが生成され
て、``Car`` オブジェクト内部に合成で保持されることを表している。併せて、前後それ
ぞれの車輪間のリンクもそれぞれ生成される。

   Figure 11.20 Connectors and Parts in a structure diagram using multiplicities

上のものと等価な ``Car`` オブジェクトだ。オブジェクトというよりシステムと見るべ
きなのか。

多重度を記入することで記号の記入の手間と紙幅を節約できる。

   Figure 11.21 An Instance of the Car Class

   It describes the internal structure of the ``Car`` that it creates and how
   the four contained instances of ``Wheel`` will be initialized.

車輪オブジェクトの型名は抑制されている。

   Figure 11.22 InstanceSpecification indicating a constructor

コンストラクター ``makeWindow`` 操作の文頭に標準ステレオタイプ ``«Create»`` を付
す。戻り値の表現だろう、破線矢印で操作名とオブジェクト記号とを結ぶ。

   Figure 11.23 A constructor for the Car Class

実践的なコンストラクターの仕様記法の見本。コンストラクター ``createCar`` の呼び
出しで、矢印の指す構造のあるオブジェクトが作成されることを表す。

   Figure 11.24 Showing that the extended Class is a metaclass

拡張された Class ``Interface`` が実際にはメタクラスだということが明示されてい
る。

11.5 Associations
======================================================================

11.5.1 Summary
----------------------------------------------------------------------

   An Association classifies a set of tuples representing links between typed
   instances. An AssociationClass is both an Association and a Class.

11.5.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 11.25 Associations

新クラスは Association と AssociationClass の二つある。この図式に現れる関連は、
これまで見た関連のすべての中で最も重要だと思われる。

``A_endType_association``
  Association から Type への関連（単方向）。

  * 関連端の型を表現する関連。複数の関連端が同じ型であってもよいので、多重度は
    ``1..*`` になる。
  * ``A_relatedElement_relationship`` を subsets する。
  * 関連端 ``endType`` は ``{readOnly}`` だ。

``A_memberEnd_association``
  Association から Property への関連（双方向）。

  * Association には Properties が表現する関連端 memberEnds を ``2..*`` 個ある。
    各関連端は Association リンク中のその関連端に接続されたオブジェクト群の関与
    を表現する。
  * ``A_member_memberNamespace`` を subsets する。
  * 関連端 memberEnd は ``{ordered}`` だ。

``A_ownedEnd_owningAssociation``
  Association から Property への複合関連（双方向）。

  * 関連端 ``ownedEnd`` は、その Association 自身が所有するような関連端のことだ。
  * ``A_feature_featuringClassifier``,
    ``A_redefinitionContext_redefinableElement``, ``A_ownedMember_namespace``,
    ``A_memberEnd_association`` を subsets する。
  * 関連端 ownedEnd は ``{ordered}`` だ。

``A_navigableOwnedEnd_association``
  Association から Property への関連（単方向）。

  * 上述の ``A_ownedEnd_owningAssociation`` を subsets する。

``A_qualifier_associationEnd``
  Property から Property への複合関連（双方向）。

  * ``A_ownedEnd_owner`` を subsets する。
  * 関連端 ``qualifier`` は ``{ordered}`` だ。

11.5.3 Semantics
----------------------------------------------------------------------

11.5.3.1 Associations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   An Association specifies a semantic relationship that can occur between typed
   instances. It has at least two ``memberEnds`` represented by Properties, each
   of which has the type of the end. More than one end of the Association may
   have the same type.

意味上の関係。

   An Association declares that there can be links between instances whose types
   conform to or implement the associated types.

リンクは Association の ``memberEnd`` それぞれについて一つの値からなる組 (tuple)
で、値のそれぞれは端における型に適合するか、実装したオブジェクトだ。

   Not all links need to be classified by an Association.

   When one or more ends of the Association have ``isUnique`` = false, it is
   possible to have several links associating the same set of instances.

そういう場合には、リンクにはその端の値とは別に、追加的な識別子がある。

   When one or more ends of the Association are ordered, links carry ordering
   information in addition to their end values.

順序関係がある関連端もあるようだ。

N 個の ``memberEnds`` を持つ Association について、任意の N - 1 個の端を選ぶ。選
ばれなかった方の端を構成する Property を oep と呼ぶ。選ばれた N - 1 個の端にある
Classifiers が oep の context となる。特定のオブジェクトを context 端に関連付け
る。

   Then the collection of links of the Association that refer to these specific
   instances will identify a set of instances at oep. The value represented by
   oep (see 9.5.3) is a collection calculated from this set as follows:

* 集合内のオブジェクトすべてがその集まりに出現し、それ以外のものは出現しない。
* oep が unique とマークされている場合、各オブジェクトはそれに接続するリンクの数
  に関係なく、集まりに一度だけ出現する。
* oep が nonunique とマークされている場合、各オブジェクトはそれに接続する各リン
  クに対して集まりに一度出現する。
* oep が ordered とマークされている場合、集まりはリンクの順序情報に従って順序付
  けられる。

..

   The multiplicity of oep constrains this cardinality, or in the case of
   qualified associations, the size of the collection partition that may be
   associated with a qualifier value.

   *Subsetting* of Association ends has the meaning specified for Property (see
   9.5.3).

   *Specialization* is, in contrast to subsetting, a relationship in the domain
   of intentional semantics, which is to say it characterizes the criteria
   whereby membership in the collection is defined, not by the membership.

Association の場合、特化とは、特化 Association によって分類されたリンクが特化さ
れた Association によっても分類されることを意味する。意味的には、特殊化
Association の端からなる集合は、対応する特殊化された Association の端からなる集
合の部分集合であることを意味する。

注意：多項 Associations では端の多重度の下限は通常ゼロだ。多項 Association の端
の多重度の下限が 1 であることは、その他の端に対する値の可能な組み合わせについて
リンク一個（以上）が存在しなければならないことを意味する。

   A binary Association may represent a composite aggregation (i.e., a
   whole/part relationship).

合成は Association の ``part`` 端の ``isComposite`` 属性を ``true`` とすることで
表現する。Association の ``end`` Property は、その関連が二項であり、もう一方の端
が共有にも複合にもマークされていない場合にしか、共有または複合集約としてマークす
ることが許されない。

   An end Property of an Association that is owned by an end Class or that is a
   ``navigableOwnedEnd`` of the Association indicates that the Association is
   navigable from the opposite ends; otherwise, the Association is not navigable
   from the opposite ends.

* 回航可能性が意味するのは、実行時にリンクに関与するオブジェクト、Association の
  オブジェクトが、Association の他方の端にあるオブジェクトから効率的にアクセス可
  能であることだ。
* 端が回航可能でない場合、反対側の端からのアクセスは可能であってもなくても構わな
  い。可能であっても効率的ではない場合がある。

   A qualified Association end has ``qualifiers`` that partition the instances
   associated with an instance at that end, the qualified instance.

* 各分割は ``qualifier`` 値によって指定され、これは各 ``qualifier`` 値に対して一
  つの値からなる組だ。
* 関連付けの他端における多重度は、各分割におけるオブジェクトの個数を決定する。つ
  まり、例えば ``0..1`` は ``qualifier`` 値ごとにオブジェクトが高々一つ存在する
  ことを意味する。下限が ``0`` でない場合、``qualifier`` 値は有限集合でなければ
  ならない。例えば、``qualifier`` 値が列挙によって型付けられているからなどの理由
  による。

Association の存在はモデル内の他の情報から導出することがある。Association の導出
とその端の導出との論理関係は、モデル固有だ。

11.5.3.2 Association Classes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   An AssociationClass is a declaration of an Association that has a set of
   Features of its own.

Association は Association と Class の両方であるゆえ、Features を持つ能力だと
か、``name`` があることだとか、共通する特性の集合がある。これらの特性は同じ構造
(Classifier) から多重継承され、重複しない。したがって、AssociationClass には
``name`` が一つだけあり、Class および Association に定義されている Features の集
合を有する。

   The constraints defined for Class and Association also are applicable for
   AssociationClass, which implies for example that the ``attributes`` of the
   AssociationClass, the ``memberEnds`` of the AssociationClass, and the
   opposite ends of Associations connected to the AssociationClass must all have
   distinct names. Moreover, the specialization and refinement rules defined for
   Class and Association are also applicable to AssociationClass. Redefinition
   is applicable to an AssociationClass nested in the context of a Classifier
   just as it is applicable to a nested Class.

   An AssociationClass inherits the composite Properties
   ``Class::ownedAttribute`` and ``Association::ownedEnd.``

``ownAttribute`` の値はその ``Class`` の属性である ``Property`` であり、
``Association::ownedEnd`` を通じて所有する AssociationClass の端ではない。
``Association::ownedEnd`` の値は AssociationClass の属性ではなく、
AssociationClass が所有する Association の端だ。

   An instance of an AssociationClass has the characteristics both of a link
   representing an instantiation of the AssociationClass as a kind of
   Association, and of an object representing an instantiation of the
   AssociationClass as a kind of Class.


AssociationClass の端すべてが ``isUnique`` だとしても、端 Classes の同じオブジェ
クト集合を関連づける複数のオブジェクトを持つことが可能だ。

   An AssociationClass cannot be a generalization of an Association or a Class.

11.5.4 Notation
----------------------------------------------------------------------

どんな Association も菱形で表すことができ、Association ``memberEnd`` それぞれの
実線は菱形とその端の型である Classifier を結ぶ。二個を超える端のある Association
はこの方法でしか描くことができない。

二項 Association は通常二つの Classifiers を接続する実線、または一つの
Classifier と自身を結ぶ実線で描かれる。

* 実線は折れ線で構わない。線分に UML ツールが処理する便宜以上の意味はない。

Association 記号には次のように修飾をしてもよい：

* Association の名前を名前文字列として Association 記号の付近に、ただし端の名前
  と間違える程度に離した位置に示すことが可能だ。
* Association の名前の前に、または名前が示されていなければ名前の代わりにスラッ
  シュ ``/`` を表示すると、その Association が派生したものであることを示す。
* 特性文字列は Association 記号の付近に、ただし端の特性文字列と間違えわれぬよう
  に、どの端からも十分離れた位置に表示することが許される。

実線として描画される二項 Association で、Association の名前の隣にあるかまたは代
わりとなる、ある端の方向の直線に沿って指し示す黒三角は、その端が Association
の端順序で最後に来ることを示す。

Associations 間の汎化は Association 記号間にある汎化矢印を使って示される。

   An Association end is the connection between the line depicting an
   Association and the icon (often a box) depicting the connected Classifier.

その他、直線の端の近くに置ける記法：

  * 多重度
  * 中括弧で括られた ``<prop-modifier>``
  * ``<visibility>`` 記号

..

   NOTE. If no multiplicity is shown on the diagram, no conclusion may be drawn
   about the multiplicity in the model.

Association の端にある開いた鏃は、その端が回航可能であることを示す。Association
の端にある小さなバツジルシは、その端が回航可能でないことを示す。

   If the Association end is derived, this may be shown by putting a slash in
   front of the name, or in place of the name if no name is shown.

二項 Association は一方の端の ``aggregation`` が ``AggregationKind::shared`` ま
たは ``AggregationKind::composite`` であってよい。

* ``shared`` ならば反対側の関連端を中身のない菱形で修飾する。
* ``composite`` ならば同様に中身の詰まった菱形で修飾する。

..

   Ownership of Association ends by an associated Classifier may be indicated
   graphically by a small filled circle, which for brevity we will term a *dot*.

* ドットは Classifier と関連矢印の間に描く。
* ドットの直径は線の幅よりは大きく、集約菱形よりは小さい。
* ドットの触れた Classifier が表す型の Property をそのモデルが含むことを示す。
  この Property はもう一方の関連端にある Classifier が所有する。

..

   The dot may be used in combination with the other graphic line-path notations
   for Properties of Associations and Association ends. These include
   aggregation type and navigability.

   Explicit end-ownership notation is not mandatory, i.e., a conforming tool may
   not support it.

ドット表記が使用される場合、ドットがないことが Association による所有権を意味す
るように、各図を通して一貫して適用されなければならない。別の言い方をすれば、この
表記をユーザーモデルの二項 Association に適用する場合、ドットは、Classifier に
よって所有されていない端部に対してのみ省略される。このように、この記法が使用され
る文脈では、特定の端にドットがなくても、それらの端の所有権が曖昧になることはな
い。

   Figure 11.26 Graphic notation indicating exactly one Association end owned by
   the Association

この図では、ドットが付いている ``endA`` は Classifier ``B`` が所有すると解釈する
が、ドットの付いていない ``endB`` は曖昧さなしに ``BinaryAssociationAB`` が所有
すると解釈する。

回航可能の表記法は過去において非公式の習慣に従ってよく使われたが、回航可能な端は
他方の端の Classifier により所有され、航行不能な端は Association が所有すると仮
定されていた。この慣習は今では嫌われている。

   Aggregation type, navigability, and end ownership are separate concepts, each
   with their own explicit notation. Association ends owned by classes are
   always navigable, while those owned by associations may be navigable or not.

ここから AssociationClass の記法。

   An AssociationClass is shown as a Class symbol attached to the Association
   path by a dashed line.

* Association パスは菱形を含んでもよい、この場合、Class 記号は破線によって菱形に接
  続された状態で表示されなければならない。
* Association パスと AssociationClass 記号は、同じ基礎モデル要素を表し、単一の名
  前を持つ。この名前は、パス上、Class 記号内、またはその両方に配置することが許さ
  れるが、同じ名前でなければならない。

..

   Association end names appear in the same position as regular Associations,
   not in the attribute compartment of the AssociationClass.

論理的には AssociationClass と Association は同じ意味の実体だが、それらは図式的
には区別される。AssociationClass の記号は線から切り離すことが可能だが、破線はパ
スとClass 記号の両方に接してなければならない。

   When two association lines cross, a conforming tool may provide the option to
   show a small semicircular jog to indicate that the lines do not intersect (as
   in electrical circuit diagrams).

関連端の回航可能性を知らせる矢印とバツのいくつかを非表示にするのが便利であること
が実用上ではよくある。ドット記法同様、図式全体で非表示オプションを適用する。

* 矢印とバツジルシをすべて表示する。回航とその不在を完全に明示する。
* 矢印とバツジルシをすべて抑止する。回航について推論不能だ。
* バツジルシをすべて抑止する。双方向の回航が可能な Association の矢印を抑制し、
  一方向の回航が可能な Association にのみ矢印を表示する。

   If there are two or more aggregations to the same aggregate, a conforming
   tool may as a purely presentational option show them as a tree by merging the
   aggregation ends into a single segment adorned by the solid or hollow
   aggregation diamond symbol.

その単一断片上の装飾は、集約端すべてに適用される。併合された断片に装飾がないこと
は、抑制された装飾に対応する特性が、集約端のすべてに対して等しい値を持つことを意
味するものではない。

   A ``qualifier`` is shown as a small rectangle attached to the end of an
   association path between the final path segment and the symbol of the
   Classifier that it connects to.

* 修飾子矩形は実用的でない場合を除き、付属の Class の矩形よりも小さくする必要が
  ある。
* 修飾子矩形は Association パスの一部であり、Classifier の一部ではない。
* 修飾子矩形は、その ``qualifier`` を所有する ``memberEnd`` を表す Association
  パスの端に取り付けられる。

  * Classifier の一部というより、Association の線の一部として示す。

対象端に取り付けられた多重度は修飾されたオブジェクトと修飾値を対にすることによっ
て選択される対象オブジェクトの集合の取り得る濃度を示す。

   The qualifier attributes are drawn within the qualifier box. There may be one
   or more attributes, shown one to a line.

修飾子属性は、初期値表現に意味がないことを除き、Classifier 属性と同じ表記とする。

   It is permissible (although somewhat rare), to have a qualifier on every end
   of a single association.

   A qualifier may not be suppressed.

11.5.5 Examples
----------------------------------------------------------------------

主題が重要なので、見本が豊富にある。

   Figure 11.27 Binary and ternary Associations

* 黒塗り三角は Player PlayedInYear Year という読み順を示す。

三項 Association が Team, Year, Player の間にあり、それぞれ ``team``,
``season``, ``goleie`` という端子を持つ。

   Figure 11.28 Association ends with various adornments

さまざまな装飾を施した Association 端。

* ``a``, ``b``, ``d`` は ``+`` が付いていて、public であることを示す。
* ``{subsets b}`` の意味をはっきり例示している。この場合は「クラス ``C`` のオ
  ブジェクトにとっては、集合 ``d`` は集合 ``b`` の部分集合だ」の意味だ。

   Figure 11.29 Examples of navigable association-owned ends

Association が所有する端子の表記（ドットなし）だ。

   The third pair EF shows a binary Association with unspecified navigability.
   In a diagram where arrows are only shown for one-way navigable associations,
   this probably signifies bidirectional navigability.

関連端の名前の違いを除けば ``A_f_e`` がおそらく ``A_b_a`` と同値だ。

関連端の名前の違いを除けば ``A_h_g`` と ``A_j_i`` が同値であることに注意。本仕様
書では後者のスタイルを主に採用しているようだ。

   Figure 11.30 Examples of class-owned ends

クラス所有の端子をいくつか。この図式ではクラス所有はドットで示されている。

ドット付きならば Class による所有、そうでなければ Association による所有。

* ``A_b_a`` において、端子 ``b`` と ``a`` は Class ``A``, ``B`` がそれぞれ所有す
  る。Class 所有ゆえ回航可能。
* ``A_d_c`` において、端子 ``d`` は Class ``C`` が所有しており回航可能。端子
  ``c`` は ``A_d_c`` が所有していて回航可能。
* ``A_f_e`` において、端子 ``f`` は Class ``F`` が所有しており回航可能。端子
  ``e`` においてはバツジルシが抑止されているとみなし、これは Association が所有
  していて回航不能と読む。
* ``A_h_g`` において、端子 ``h`` と ``g`` はそれぞれ Class ``G``, ``H`` が所有す
  る。ただし «This is in a diagram where arrows are only shown for one-way
  navigable associations.»

   Figure 11.31 Example of attribute notation for navigable end owned by an end
   Class

Class が所有する Association 端は属性でもあるので、属性表記をこのように用いるこ
とが可能だ。この表記を関連表記法と併用すると、属性が Association 端子でもあるこ
とを完全に明確にすることが可能だ。

   Figure 11.32 Derived supersets (union)

以前理解できなかった derived union の説明。

   The attribute ``A::b`` is derived by being the strict union of all of the
   attributes that subset it. In this case there is just one of these, ``C::d``.

Class ``C`` のオブジェクトにとって ``d`` は ``b`` の部分集合であり、``b`` は
``d`` から導出される。

.. admonition:: 読者ノート

   ``D`` is-a ``B`` であるが、それでも ``b`` が ``d`` から導出される。

..

   Figure 11.33 Composite aggregation is depicted as a black diamond

何度も見てきた複合集約を示す黒ダイヤの見本。

   Figure 11.34 Composite aggregation sharing a source segment

上の関連と同じ。

   The model values for absent adornments on the merged segment, such as
   property modifiers or visibility, may differ.

..

   Figure 11.35 Example AssociationClass Job, which is defined between the two
   Classes Person and Company

AssociationClass 表記例。Association の ``name`` が Class 矩形と Association 矩
形に二個表示されている。どちらの ``Job`` も同一モデル要素を指している。

   Figure 11.36 Example AssociationClass using diamond symbol

上と同じ意味の図式。

   Figure 11.37 Qualified associations

左は ``Bank`` がある場合、特定の ``accountNo`` が高々一人の ``Person`` を識別す
ることを示す。``qualifier`` は Property ``accountNo`` であり、``Bank`` オブジェ
クトを修飾する。

   The ``qualifier`` is owned by the unnamed Property at the ``Bank`` end of the
   Association, i.e., the Property whose type is ``Bank``.

右は ``Square`` を ``Chessboard::rank`` および ``Chessboard::file`` で識別するこ
とを示す。多重度が ``1`` なので、可能な値すべてが個々のマス目を示すということを
図示している。

この場合、``qualifiers`` は型が ``Chessboard`` であるような無名 Association 端子
Property が所有し、一方、型が ``Square`` である Property のほうには
``aggregation`` が ``composite`` であることがマークされている。

11.6 Components
======================================================================

11.6.1 Summary
----------------------------------------------------------------------

概要が妙に長い。

任意の規模および複雑さのソフトウェアシステムを定義するのに用いられる一連の構成
要素を規定する。特に、«a modular unit with well-defined Interfaces that is
replaceable within its environment» である Component を規定する。

   An important aspect of component-based development is the reuse of previously
   constructed Components.

* Component はシステムや部分システム内の自律的な単位であるとみなすことが可能だ。
* Component には一つまたは複数の ``provided`` and/or ``required`` Interfaces が
  ある。Component の内部は、その Interfaces により与えられる以外には隠蔽されてア
  クセスできない。その結果、Components や部分システムは再利用や置換を柔軟にでき
  るようになる。

..

   The aspects of autonomy and reuse also extend to Components at deployment
   time.

Component を実装する成果物は、例えば既存のシステムを更新するために独立して配備さ
れ、再配備されることが可能であることを意図している。

Components パッケージは、論理 Component と物理 Component の両方の仕様と、それら
を実装する成果物、それらが配備および実行されるノードを対応する。

物理 Component の例として次を挙げている：

* EJB
* CORBA
* COM+ and .NET
* WSDL

次の記述がわからない：

   It is anticipated that profiles based around Components will be developed for
   specific component technologies and associated hardware and software
   environments.

11.6.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 11.38 Components

Component と ComponentRealization が新登場する。

``A_required_component``, ``A_provided_component``
  Component から Interface への関連（単方向）。

  * Component がそのサービスの契約をクライアントに指定するのは ``provided``
    Interfaces による。
  * Component が他の Components やシステムのサービスに必要とする契約は
    ``required`` Interfaces による。

``A_packagedElement_component``
  Component から PackageableElement への複合関連（単方向）。

  * ``A_ownedMember_namespace`` を subsets する。

``A_realization_abstraction``
  Component から ComponentRealization への複合関連（双方向）。

  * ``A_ownedElement_owner`` を subsets する。
  * ``A_supplier_supplierDependency`` を subsets する。

``A_realizingClassifier_componentRealization``
  ComponentRealization から Classifier への関連（単方向）。

  * 関連端 ``realizingClassifier`` の多重度は ``1..*`` だ。
  * ``A_clientDependency_client`` を subsets する（向き注意）。

11.6.3 Semantics
----------------------------------------------------------------------

11.6.3.1 Components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A Component represents a modular part of a system that encapsulates its
   contents and whose manifestation is replaceable within its environment.

   A Component is a *self-contained* unit that encapsulates the state and
   behavior of a number of Classifiers. A Component specifies a formal contract
   of the services that it provides to its clients and those that it requires
   from other Components or services in the system in terms of its ``provided``
   and ``required`` Interfaces.

自己完結単位だとか、正式な契約だとかというキーワードを憶えておく。

   A Component is a *substitutable* unit that can be replaced at design time or
   run-time by a Component that offers equivalent functionality based on
   compatibility of its Interfaces. As long as the environment is fully
   compatible with the ``provided`` and ``required`` Interfaces of a Component,
   it will be able to interact with this environment.

Component の置換可能性はその二系統の Interfaces が関係する。システムの拡張性に関
しても Component の新種を用意することでなされる。

   A Component may be manifested by one or more Artifacts, and in turn, that
   Artifact may be deployed to its execution environment. A
   DeploymentSpecification may define values that parameterize the Component’s
   execution. (See Deployments - Clause 19).

Artifact と DeploymentSpecification は Component と何か関係があるらしいことを憶
えておく。

   The ``required`` and ``provided`` Interfaces of a Component allow for the
   specification of StructuralFeatures such as ``attributes`` and Association
   ends, as well as BehavioralFeatures such as Operations and Receptions.|

これで二系統の Interfaces の役割がはっきりしたか。

* Component は ``provided`` Interface を直接実装してもよいし、その実現
  Classifiers が実装してもよいし、それらは継承されてもよい。
* ``required`` および ``provided`` Interfaces は Ports で整理してよい。Ports は
  通常、実行時に対応される ``required`` および ``provided`` Interfaces の名前付
  き集合を定義することを可能にする。

..

   A Component has an *external view* (or “black-box” view) by means of its
   publicly visible Properties and Operations.

アクセスレベルが public である Properties と Operations そのものが外部に対する
ビューだと考えられる。それ以外が black box だということになる。

ProtocolStateMachine などの Behavior を Interface や Port あるいは Component 自
体に付加することで、Operation 呼び出し順序の動的制約を明示し、外部ビューをより正
確に定義することも許される。

   The wiring between Components in a system or other context can be
   structurally defined by using Dependencies between compatible simple Ports,
   or between Usages and matching InterfaceRealizations that are represented by
   sockets and lollipops (see 10.4.4) on Components on Component diagrams.

Dependency をどう構造的に定めるかというのが主題だ。どの間の依存関係なのかは二通
りあると言っていて、Component 図式で見られる。

   A Component also has an internal view (or “white-box” view) by means of its
   private Properties and realizing Classifiers. This view shows how the
   external Behavior is realized internally.

外部ビューの Dependencies は内部ビューで起こり得ることの便利な概要を与えるもので
あり、必ず起こることを規定するわけではない。

   The execution time semantics for an assembly Connector in a Component are
   that requests (signals and operation invocations) travel along an instance of
   a Connector.

異なる ``roles`` に差し向けられた複数の Connector または多（三以上）項 Connector
の実行意味は、要求を発信または処理するオブジェクトが実行時に決定されることを示
す。

Component には UML 標準ステレオタイプが多く存在する。例えば、

   ``«Subsystem»`` to model large-scale Components, and ``«Specification»`` and
   ``«Realization»`` to model Components with distinct specification and
   realization definitions,

仕様一つが実現を複数持つこともある。:doc:`./ch22-standard-profile` 参照。

   A Component may be realized (or implemented) by a number of Classifiers. In
   that case, a Component owns a set of ComponentRealizations to these
   Classifiers.

次の文ではパッケージやインポートという術語が出てくる：

   A component acts like a Package for all model elements that are involved in
   or related to its definition, which should be either owned or imported
   explicitly. Typically the Classifiers that realize a Component are owned by
   it.

Component を実現する Classifiers は、通常その Component がそれらを所有する。

   The ``isDirectlyInstantiated`` property specifies the kind of instantiation
   that applies to a Component.

* 真であれば、Component は設計時に定義はされているが、稼働時（または実行時）には
  Component で指定されたオブジェクトは存在しない。すなわち、Component はそれの実
  現する Classifiers または ``parts`` のオブジェクト化により間接的にオブジェクト
  化される。
* 偽であれば、Component は所在地指定可能であるオブジェクトとしてオブジェクト化さ
  れる。

11.6.4 Notation
----------------------------------------------------------------------

Component はキーワード ``«component»`` を付した Classifier 矩形として示す。
Component アイコンを右隅に示すことを可能にしてもよい。左側から小矩形二つが突き出
たClassifier 矩形だ。この場合はキーワードが非表示でもよい。

属性、操作、内部構造区画はすべて通常の意味でのものだ。

Component の ``provided`` および ``required`` Interfaces はボール・ソケット記法
で示してよい。ここでは、ボールとソケットは Component 矩形から外に突き出る。

   For displaying the full signature of a ``provided`` or ``required`` Interface
   of a Component, the Interfaces can also be displayed as normal expandable
   Classifier rectangles. For this option, the Interface rectangles are
   connected to the Component rectangle by appropriate dependency arrows, as
   specified in 7.7.4 and 10.4.4.

   A conforming tool may optionally support compartments named “provided
   interfaces” and “required interfaces” listing the ``provided`` and
   ``required`` Interfaces by name.

この区画記法が使えると、Component に ``provided`` Interface や ``required``
Interface が大量にあるシナリオにおいて有用な選択肢となり得る。

   Additional optional compartments “realizations” and “artifacts” may be used
   to list the realizing Classifiers (Classifiers reached by following the
   ``realization`` property) and manifesting Artifacts (Artifacts that manifest
   this component - see 19.3).

ComponentRealization は Realization 依存と同じ方法で記される。すなわち鏃が白抜き
三角である一般的な破線矢印だ。

Component の ``packagedElements`` は、:doc:`./ch09-classification` で取り扱った
``ownedMembers`` のオプション区画についての仕様に従い、オプション区画
``"packaged elements"`` に表示してもよい。

11.6.5 Examples
----------------------------------------------------------------------

   Figure 11.39 Example of an overview diagram showing Components and their
   general Dependencies

依存関係の矢印がない Component 同士には依存関係がない。

``Order`` は ``Account`` と ``Product`` に依存しているが、依存の種類は特記されて
いない。

   Figure 11.40 A Component with two provided and three required Interfaces

このようなロリポップとソケットが見えるだけの Component の図式を external view と
呼ぶようだ。

   Figure 11.41 Black box notation showing a listing of provided and required
   interfaces

上記と同じモデルを区画 ``provided interfaces`` と ``required interfaces`` 記法を
用いて表現している。

   Figure 11.42 Optional "white-box" representation of a Component

おそらく上記のモデルの "white box" view を示している。外部ビューに区画
``realizations`` と ``artifacts`` を追加した形だ。前者にリストされているのは実現
Classifiers だ。後者はこの Component の成果物の一覧だ。

   Figure 11.43 Explicit representation of provided and required Interfaces
   using Dependency notation.

Dependency 記法を用いて ``provided`` と ``required`` Interfaces を明示的に表現し
ている。矢印の描き分け方に注意。

   Figure 11.44 A representation of the realization of a complex Component

この図式全体が ComponentRealizations を示している。下側の Classifiers の集合が
Component ``Customer`` を実現している。

   Figure 11.45 An alternative nested representation of a complex Component

区画 ``packaged elements`` の記法例。

``OrderHeader`` と ``LineItem`` は区画 ``realizations`` でリストされるもの同じ。

   Figure 11.46 Example model of a Component, its provided and required
   Interfaces, and wiring through Dependencies

Components 間の配線。込み入った図式。

* 右側の Dependency は ``OrderableItem`` の Usage から ``OrderableItem`` の
  InterfaceRealization へのもの。
* ``/OrderableItem`` は ``Product`` の上位型が実装する Interface であることを示
  す。Component は ``AccountPayable`` が ``OrderHeader`` に依存していることを要
  求している。
* ``AccountPayable`` Ports 間の Dependency は、単純な Ports 間で Dependency が配
  線されている場合、ソケットとボールを結ぶ依存関係の矢印を表示する記法を示してい
  る。

..

   This is illustrated by the Dependency from AccountPayable to OrderHeader,
   which indicates that something about the fact that the Component requires
   AccountPayable is dependent upon OrderHeader.

..

   Figure 11.47 Internal structure of a Component

内部アセンブリーの部品として単純 Ports を持つ Components を含む Component の内部
構造 (white box) を示している。

* アセンブリー Connector はボールとソケットの表記を使用。
* 委譲 Connector は線が単純な Port 自体ではなく、ボールまたはソケットで終わるこ
  とができるという表記オプションを使用。

   Figure 11.48 Delegation Connectors connect externally provided Interfaces to
   the parts that realize or require them.

委譲 Ports から処理 ``parts`` への委譲 Connector を示す。この例では ``internal
strucure`` 区画の ``parts`` は、オプションの ``packaged elements`` 区画に示され
るクラスによって型付けられている。

11.7 Collaborations
======================================================================

11.7.1 Summary
----------------------------------------------------------------------

Collaborations の第一の目的とは、通信要素のシステムがどのように特定の課題または
課題の集合を達成するかを、説明と無関係な部分を取り込むことを必要とせずとも説明す
ることだ。

   A CollaborationUse represents the application of the pattern described by a
   Collaboration to a specific situation involving specific elements playing its
   ``collaborationRoles``.

CollaborationUse は Collaboration が記述するパターンを、それの
``collaborationRoles`` を演じる特定の要素を関わらせる特定の状況に対して適用する
ことを表現する。

11.7.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 11.49 Collaborations

Collaboration と CollaborationUse を見ていく。

``A_collaborationRole_collaboration``
  Collaboration から ConnectableElement への関連（単方向）。

  * ``A_role_structuredClassifier`` を subsets する。

``A_type_collaborationUse``
  CollaborationUse から Collaboration への関連（単方向）

  * 関連端 ``type`` はこの CollaborationUse で使われている Collaboration であ
    る。
  * 関連端 ``type`` の多重度は 1 だ。

``A_roleBinding_collaborationUse``
  CollaborationUse から Dependency への複合関連（単方向）。

  * ``A_ownedElement_owner`` を subsets する。

``A_collaborationUse_classifier``
  Classifier から CollaborationUse への複合関連（単方向）。

  * ``A_ownedElement_owner`` を subsets する。

``A_representation_classifier``
  Classifier から CollaborationUse への関連（単方向）。

  * ``A_collaborationUse_classifier`` を subsets する。

11.7.3 Semantics
----------------------------------------------------------------------

11.7.3.1 Collaborations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Collaborations may be used to explain how a collection of cooperating
   instances achieve a joint task or set of tasks.

Collaboration は通常、その説明に必要な側面しか取り込まず、それ以外を抑制する。し
たがって、あるオブジェクトは複数の異なる Collaboration で同時に
``collaborationRoles`` を果たすことがあるが、Collaboration それぞれはそのオブ
ジェクトの目的に関連する側面のみを表現することになる。

   A Collaboration defines a set of cooperating participants that are needed for
   a given task. The ``collaborationRoles`` of a Collaboration will be played by
   instances when interacting with each other. Their relationships relevant for
   the given task are shown as Connectors between the ``collaborationRoles``.

Collaboration の ``collaborationRoles`` はオブジェクトの使い方を定義する一方、こ
れらの ``collaborationRoles`` を型付ける Classifiers はこれらのオブジェクトに必
要な Property のすべてを指定する。したがって、Collaboration はオブジェクトが
Collaboration に参加するために必要な Property を指定することになる。

CollaborationRole 間の Connectors は参加するオブジェクト間に存在しなければならな
い通信経路を指定する。

   Neither all Features nor all contents of the participating instances nor all
   links between these instances are always required in a particular
   Collaboration. Therefore, a Collaboration is often defined in terms of
   ``collaborationRoles`` typed by Interfaces.

   Collaborations may be specialized from other Collaborations.

* ``collaborationRole`` が特殊化で拡張された場合、特殊化された Collaboration に
  おけるそれの型は汎化 Collaboration におけるそれの型に適合していなければならな
  い。
* ``collaborationRole`` の型の特殊化は、それらの ``collaborationRole`` を実現す
  る Classifiers の対応する特殊化を意味するものではない。それらの
  ``collaborationRoles`` によって定義された制約に適合していれば十分だ。

..

   A Collaboration is not directly instantiable.

その代わり、Collaboration で定義された協力は、Collaboration で定義された
``collaborationRoles`` を果たすオブジェクト間の実際の協力の結果としてもたらされ
る。

11.7.3.2 CollaborationUses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A CollaborationUse represents a particular use of a Collaboration to explain
   the relationships between a set of elements. A CollaborationUse shows how the
   pattern described by a Collaboration is applied in a given *context*
   Classifier, by binding specific ConnectableElements from that context to the
   ``collaborationRoles`` of the Collaboration.

* ある Classifier で、与えられた Collaboration に関連する CollaborationUses が存
  在し、それぞれが異なる形で束縛されることがある。
* 与えられた ``collaborationRole`` または Connector は、同じまたは異なる
  Collaboration の複数の使用に関与してもよい。

..

   The ``roleBindings`` are implemented using Dependencies owned by the
   CollaborationUse. Each collaborationRole in the Collaboration is bound by a
   distinct Dependency and is its ``supplier``. The ``client`` of the Dependency
   is a ConnectableElement that relates in some way to the context Classifier:
   it may be a direct ``collaborationRole`` of the context Classifier, or an
   element reachable by some set of references from the context Classifier.

これらの ``roleBinding`` は背景となる Classifier のどの ConnectableElement が
Collaboration のどの CollaborationRole を担うかを示す。

   Connectors in a Collaboration typing a CollaborationUse must have
   corresponding Connectors between elements bound in the context Classifier,
   and these corresponding Connectors must have the same or more general type
   than the Collaboration Connectors.

   One of the CollaborationUses owned by a Classifier may be singled out as
   representing the Behavior of the Classifier as a whole. This is called the
   Classifier’s ``representation``.

Classifier の ``representation`` に関連する Collaboration は、この Classifier の
StructuralFeatures に対応するオブジェクト（例えば、その ``attributes`` や
``parts``）がどのように相互作用して Classifier の Behavior 全体を生成するかを示
す。

   The representing Collaboration may be used to provide a description of the
   Behavior of the Classifier at a different level of abstraction than is
   offered by the internal structure of the Classifier. The Properties of the
   Classifier are mapped to ``collaborationRoles`` in the Collaboration by the
   ``roleBindings`` of the CollaborationUse.

Collaboration に取り付けられた Behavior のどれもが、CollaborationUses 内に束縛さ
れた ``collaborationRoles`` と Connectors の集合に適用する。例えば、
Collaboration の ``parts`` 間の相互作用は単一の CollaborationUse に束縛さ
れた Classifier ``parts`` に適用される。

   If the same ConnectableElement is used in both the Collaboration and the
   represented element, no ``roleBinding`` is required.

   It is not specified further when client and supplier elements in
   ``roleBindings`` are compatible.

11.7.4 Notation
----------------------------------------------------------------------

Collaboration はその名前を含む破線の楕円形で示す。

``collaborationRoles`` と Connectors で構成された Collaboration の内部構造は破線
楕円内の区画に示してよい。この区画は通常の Classifier の内部構造区画と同じ記法仕
様に従う。

* 代わりに composite structure 図が使える。あるいは通常の Classifier 矩形をキー
  ワード ``«collaboration»`` を付けて使える。

Properties でない ``collaborationRoles`` を有する Collaboration を表す記法は定義
されていない。

Property の代替記法として、楕円形の Collaboration の形状から Collaboration の
Property の型である Classifiers を示す長方形に線を引くことが許される。各線には、
Property の名前によるラベルが付けられる。

CollaborationUse は背景となる Classifier の内部構造区画内部に、発生する名前、
コロン、Collaboration ``type`` の名前を含む破線楕円で示される。

``roleBinding`` ごとに、楕円から ``client`` 要素へ破線が引かれる。
破線は ``client`` 側で ``supplier`` 要素の名前でラベルが付けられる。

   With this notation the Connectors that must exist in the context Classifier
   as a consequence of the bindings may be suppressed.

   An optional notation for CollaborationUse is as a dashed arrow with the
   keyword «occurrence» pointing from the using Classifier to the used
   Collaboration. In conjunction with this the ``roleBindings`` are shown as
   normal Dependency arrows.

このオプションでは、束縛の結果として背景となる Classifier に存在しなければならな
い Connectors が表示される必要がある。

11.7.5 Examples
----------------------------------------------------------------------

   Figure 11.50 The internal structure of the Observer Collaboration

破線楕円全体が Collaboration ``Observer`` だ。

* 区画内にある矩形がこの ``collaborationRoles`` であり、オブジェクトの名前が示し
  てある。
* オブジェクト間の実線が Connector を示す。

   Figure 11.51 Alternative notation for the parts of the Observer Collaboration.

先のものとは異なる記法を適用している。
``CallQueue`` と ``SlidingBarIcon`` の協調関係がより詳細に示されている。

* ``Subject`` ``collaborationRole`` を果たすオブジェクトは CallQueue が指定する Properties を
  所有せねばならない。
* ``Observer`` ``collaborationRole`` についても同様だ。
* これはついでだが、楕円下の Comment が ``Observer`` に対する Constraint を示し
  ている。

   Figure 11.52 The Sale Collaboration

``Sale`` は ``collaborationRoles`` ``buyer`` と ``seller`` の間の Collaboration
だ。

* ``Sale`` は Figure 11.53 で定義される BrokeredSale の定義の一部として二度使用
  されている。
* ``Sale`` は ``seller`` と ``buyer`` という二つの ``collaborationRole`` 間の
  Collaboration だ。
* ``Sale`` に相互作用、つまり他の ``Behavior`` 仕様を付加して、``Sale`` を作る際
  の段階を指定することも可能だ。

   Figure 11.53 The BrokeredSale Collaboration

``BrokeredSale`` は三つの ``collaborationRoles`` (``producer``, ``broker``,
``consumer``) の間の Collaboration だ。

* ``BrokeredSake`` の仕様から、``Sale`` Collaboration の CollaborationUses 二つ
  から構成されていることが読める。
* ``wholesale`` は ``producer`` と ``broker`` がそれぞれ ``seller`` と ``buyer``
  である ``Sale`` であることを示している。
* ``retail`` は ``broker`` と ``consumer`` がそれぞれ ``seller`` と ``buyer`` で
  ある``Sale`` であることを示している。

..

   The Connectors between sellers and buyers are not shown in the two
   occurrences; these Connectors must exist in the ``BrokeredSale``
   Collaboration as a consequence of the Connector defined in ``Sale``. The
   BrokeredSale Collaboration could itself be used as part of a larger
   Collaboration.

   Figure 11.54 A subset of the BrokeredSale Collaboration using
   ``«occurrence»`` and Dependency arrows

11.8 Classifier Descriptions
======================================================================

機械生成による節。

11.9 Association Descriptions
======================================================================

機械生成による節。

.. include:: /_include/uml-refs.txt
