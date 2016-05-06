======================================================================
11 Structured Classifiers
======================================================================
UML 2.5 pp. 181-238 に関するノート。

.. contents:: ノート目次

11.1 Summary
======================================================================
* StructuredClassifier = 内部構造 + 外部構造 な Classifier

  * 内部構造 = roles をリンクしたネットワーク
  * 外部構造 = Ports

* EncapsulatedClassifier = ?

11.2 Structured Classifiers
======================================================================

11.2.1 Summary
----------------------------------------------------------------------
* StructuredClassifier は接続された要素群の内部構造を持つことが許されている。
  各要素はこの StructuredClassifier がモデル化する全体の振る舞いの一つの role を演じる。

* この節を 11.5 節といっしょに読むことが役に立つ。

11.2.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 11.1

  * StructuredClassifier, ConnectableElementTemplateParameter,
    ConnectableElement, Connector, ConnectorEnd
  * «enumeration» ConnectorKind

11.2.3 Semantics
----------------------------------------------------------------------
*StructuredClassifier*
  * Classifier の一種。意味は概要に記した。

*ConnectableElementTemplateParameter*
  * TemplateParameter の一種である。
  * あるテンプレートの正式 (formal) なパラメーターとして
    ConnectableElement を晒すのに介されるクラスである。

*ConnectableElement*
  * TypedElement かつ ParameterableElement である抽象クラス。
  * StructuredClassifier の内部構造中の一つの構成員 (roles) を表現する。
  * ConnectableElements の接続可能性を確定するのに用いられる、

    * effective required Interfaces という集合と、
    * effective provided Interfaces という集合を

    各 ConnectableElement は見せる。

  * Property は ConnectableElement の一種である。

Connector
  * Feature の一種である。
  * Connector は StructuredClassifier 内部の roles を演じる 2 つ以上のオブジェクト間のリンク (pl.) を明確にするものである。

    * よく考えると、タコ足のようなトポロジーでも Connector の定義に含まれている。

  * 属性 kind は ``{readOnly}`` な ConnectorKind 値である。
    次のどちらかを値として取る

    * assembly: delegation でない。
    * delegation: Ports にだけ関係する。

ConnectorEnd
  * MultiplicityElement の一種である。
  * 一つの Connector の端点であり、
    その Connector を一つの ConnectableElement へ取り付ける。

A_role_structuredClassifier
  * StructuredClassifier から ConnectableElement への単方向関連。
  * 先述したようにこの関連こそが StructuredClassifier の主な意味である。
  * 関連 A_member_memberNamespace を subsets している。
  * 両端ともに ``{readOnly, union}`` 制約がある。

A_ownedAttribute_structuredClassifier
  * StructuredClassifier から Property への composite 関連（単方向）。
  * A_attribute_classifier, A_ownedMember_namespace, A_role_structuredClassifier を subsets する。
  * 関連端 ownedAttributes に制約 ``{ordered}`` を付ける。
  * 関連端 structuredClassifier を ``{redefines}`` する。

A_part_structuredClassifier
  * StructuredClassifier から Property への単方向関連。
  * 上記 ownedAttributes で ``isComposite == true`` なものを parts とする。
  * 関連端 part は ``{readOnly}`` である。

A_ownedConnector_structuredClassifier
  * StructuredClassifier から Connector への composite 関連（単方向）。
  * Connectors を所有するのは StructuredClassifier である。
  * A_feature_featuringClassifier,
    A_redefinitionContext_redefinableElement,
    A_ownedMember_namespace を subsets する。

A_templateParameter_parameteredElement
  * ConnectableElementTemplateParameter と ConnectableElement の関連（双方向）。
  * 同名関連を redefines する。

A_end_role
  * ConnectableElement と ConnectorEnd の関連（双方向）。
  * Connector の端点を一つ取れば、対応する role が一意に対応する。
  * 関連端 end は ``{readOnly}`` である。

A_definingEnd_connectorEnd
  不明。説明文の意味を理解できない。

A_end_connector
  * Connector から ConnectorEnd への composite 関連（単方向）。
  * 先述した定義により関連端 end の多重度は ``2..*`` である。
  * 関連端 end は ``{ordered}`` である。
  * A_ownedElement_owner を subsets する。

A_contract_connector
  * Connector から Behavior への関連（単方向）。
  * その Connector を横断する有効な相互作用のパターンを指定することが許されている。

A_type_connector
  * Connector から Association への関連（単方向）。
  * Connector が指定するリンクがどの Association の型のオブジェクトであるかを指定することが許されている。

A_redefinedConnector_connector
  * Connector から Connector への関連。
  * Connector が含む Classifier が何かの特殊化であるときに、再定義することが許されている。
    このとき、Association (type) や ConnectorEnds (ends) の型もそれぞれの特殊化にすることが許されている。
    さらに ConnectorEnds の Property は置き換えてもよい。

11.2.4 Notation
----------------------------------------------------------------------
* StructuredClassifier の内部構造はズバリ "internal structure" とラベルされた区画で示す。
* part は箱を入れ子で実線で描くことで示す。
* role は箱を入れ子で破線で描くことで示す。
  なお、どちらの場合でも part box と呼ばれる。
* part の provided/required Interfaces を示すのには、
  例のロリポップ・ソケット記法を用いて示してもよい。

* Property の多重度はいつもの記法を用いて part box の右上に記す。

少し先の仕様に関する記法も導入している。

* role が EncapsulatedClassifier 型のとき、その Ports はすべて小さな四角で示す。
  その role を表す part box の枠に重なるように置く。
* role が Class 以外の型のとき、適宜 ``«component»`` のようなキーワードを名前に応じて添える。

* Connector の記法は Association のそれに準じる。
  type があるときにはその Association の名前を含めることも許されている。

* parts が単純な Ports を持つときには、ball-and-socket 記法を用いてもよい。
* n 項 Connector には channeled ball-and-socket 記法というものがある。

11.2.5 Examples
----------------------------------------------------------------------
* Figure 11.2 Parts and roles

  * part boxes の見本である。
  * 左の実線枠のほうは composition によるオブジェクト。
    Wheel オブジェクト 4 つを所有するオブジェクトを示す。

    * 多重度 4 を箱の右上に記す。

  * 右の破線枠のほうは composite でないオブジェクト。
    Engine オブジェクト 1 or 2 個を参照するオブジェクトを示す。

    * 多重度 1..2 を角括弧で示す。

* Figure 11.3 Parts and roles with Ports

  * Ports あり EncapsulatedClassifiers 型属性の part boxes の見本である。
  * Wheel 側からはボールが、Engine 側からはソケットが生えている。
    箱の枠線に重なる小さい四角がある。

* Figure 11.4 Alternative notations for connecting parts and roles with Ports

  * Ports シンボル同士を接合する線が、
    内部構造の Ports の接続を示すのに唯一要求されている記法である。

  * ボールとソケットがそれぞれ Ports の provided, required Interfaces を指し示す。
    これらの出現は選択自由である。

* Figure 11.5 Associations compared with Connectors

  * ``(ii)`` rear と e がクラス Car の内部構造に所属している。
  * クラス Car という状況ではこれが成り立つと言っているだけで、
    Wheel と Engine が一般にはこの関連は成り立たない。
  * ``(i)`` の表現では、Engine の任意の個数のオブジェクトが Wheel の任意の個数のオブジェクトにリンクできる。

* Figure 11.6 "Star" Connector pattern

  * 関連端の多重度が付随する roles の多重度とがマッチしている場合 (i)、
    何か n 部グラフのようなリンク構造に解釈 (ii) する。

* Figure 11.7 "Array" Connector pattern

  * (i) では関連端の多重度が 1 なので、リンクの意味は (ii) に示すようにパラレルに解釈する。

* Figure 11.8 An assembly Connector ...

  * 単純 Ports のついた Component 型 parts の記法例。
  * 選択自由の ball-and-socket 記法を採用している。
    この記法は互換性のある Ports 間の組み立て Connector を表現する。

* Figure 11.9 An n-ary Connector ...

  * ある 4 項 Connector のための channeled ball-and-socket 記法の見本。
  * ボールのほうが provided Interfaces; Client is-a Person とのこと。
  * ソケットのほうが required Interfaces

11.3 Encapsulated Classifiers
======================================================================

11.3.1 Summary
----------------------------------------------------------------------
* EncapsulatedClassifier は Ports を所有する能力のある StructuredClassifier である。
* これは EncapsulatedClassifier を環境から分離する仕組みである。

11.3.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 11.10 Encapsulated Classifiers

  * EncapsulatedClassifier と Port の関連を中心とした図式。

11.3.3 Semantics
----------------------------------------------------------------------
*EncapsulatedClassifier*
  * 概要に記した性質のある StructuredClassifier の一種である。

Port
  * Port とは EncapsulatedClassifier の Property であり、
    次のどちらかの間の個々の相互作用点を指定するものである。

    * EncapsulatedClassifier 自身とそれがある環境
    * EncapsulatedClassifier の Behavior と内部の roles

  * 属性 isBehavior はこれが behavior Port であるかを示す。

    この Port に到着したどんな要求でも、所有者の EncapsulatedClassifier オブジェクトの
    Behavior が処理するという Port である。

  * 属性 isConjugated は provided/required Interfaces が
    Property::type にどのように関係するのかを示す。

  * 属性 isService は Port が EncapsulatedClassifier の公開機能を
    提供するのに用いられるか、または実装するのかどうかを示す。

A_ownedPort_encapsulatedClassifier
  * EncapsulatedClassifier から Port への composite 関連（単方向）。
  * A_ownedAttribute_structuredClassifier を subsets する。
  * 関連端 ownedPort は ``{readOnly}`` である。

A_required_port
  * Port から Interface への関連（単方向）。
  * 関連端 required は port を通じて
    EncapsulatedClassifier から環境への依頼を特徴づける
    Interfaces である。
    EncapsulatedClassifier オブジェクトは
    required Interfaces が所収する Features が、
    環境下の一つ以上のオブジェクトが提示することを期待している。
  * 関連端 required は ``{readOnly}`` である。

A_provided_port
  * Port から Interface への関連（単方向）。
  * 関連端 provided は port を通じて
    EncapsulatedClassifier への、環境が作る依頼を特徴づける
    Interfaces である。
    所有者である EncapsulatedClassifier は
    provided Interfaces が所有する Features を提示する必要がある。
  * 関連端 provided は ``{readOnly}`` である。

A_protocol_port
  * Port から ProtocolStateMachine への関連（単方向）。
  * Port で発生する Operation と Reception の発動の有効な順序を述べるのに
    ProtocolStateMachine を一つ参照してもよい。

A_redefinedPort_port
  * Port から Port への関連（単方向）。
  * EncapsulatedClassifier が特殊化されているときに Port は再定義してもよい。
    再定義先の Port では Interfaces を追加したり置換したりしてよい。
  * A_redefinedProperty_property を subsets する。

A_partWithPort_connectorEnd
  * ConnectorEnd から Property への関連（単方向）。
  * Port-on-Property の場合に ConnectorEnd が参照する実際の接続先 Property を表す。

11.3.4 Notation
----------------------------------------------------------------------
* EncapsulatedClassifier の Port は小さい四角で示す。

  * Port の名前を四角のそばに置く。

    * Port の名前は隠してもよい。

  * Port の四角は EncapsulatedClassifier の枠に重ねても、内側に置いてもよい。
  * Port が区画の内側にある（ように見える）要素に接続しているときは、
    四角はその枠に関して先ほどの規則に準じて置くこと。

* Port の type を名前に続けて示してもよい。

  * 名前とはコロンで区切る。
  * isConjugated な Port の場合は、type の前に ``~`` を示す。

* behavior Port は EncapsulatedClassifier 内に何か描かれている小さいシンボルに接続されている。

* Port が複数の Interfaces に関連するならば、
  一つの Interface のロリポップにそれらをカンマで区切ってリストしてよい。

* required Interface の単純 Port から provided Interface の単純 Port をつなぐ Dependency の場合、
  ソケットからロリポップへ依存矢印を結ぶかどうかは記法上は自由。

11.3.5 Examples
----------------------------------------------------------------------
* Figure 11.11 Port notation

  * 図の上側の意味は学習済み。
  * 図の下側

    * p は Engine 上の Port である（∵小さい四角の位置）
    * p の型は PowerTrain である（∵p のラベル）
    * p の provided Interface は IPowerTrain である（∵ロリポップのラベル）
    * p の required Interface は IFeedback である（∵ソケットのラベル）
    * p の多重度は 1 である（∵明示されていない）
    * p の isConjugated は false である（∵p の名前に ``~`` がない）
    * e は練習問題とする。

* Figure 11.12 Behavior Port notation

  * p のラベルの位置と、小さい四角にくっついたオマケのシンボルに注意。

* Figure 11.13 Port notation showing multiple provided Interfaces

  * ロリポップに provided Interfaces の名前をふたつまとめて示す。

* Figure 11.14 Port examples

  * 右側の Car と Boat の内部構造それぞれの
    Port の付き方の違いを説明できるようにしておくこと。

11.4 Classes
======================================================================
仕様書の 11 章の中盤でようやくクラスの仕様が与えられる。

11.4.1 Summary
----------------------------------------------------------------------
* Class は EncapsulatedClassifier と BehavioredClassifier の具体的な実現である。
* Class の目的はオブジェクトの分類を指定することと、
  それらオブジェクトの構造と振る舞いを特徴づける Features を指定することである。

11.4.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 11.15 Classes

  * Class は自らを再定義する関連と、
    何かを所有するといういくつかの関連が加わる程度。

11.4.3 Semantics
----------------------------------------------------------------------
Class
  * それの Features が Properties, Operations, Receptions, Ports, Connectors
    である一種の EncapsulatedClassifier である。

  * Class は別のクラスの private な Features にアクセスする能力はない。
    また、自分の祖先ではない別のクラスの protected な Features にもアクセスできない。

  * 属性 isAbstract: 説明がない？

  * 属性 isActive: Class には active/passive という概念がある。
    それを示すブーリアン値。

    * Class が active であることと、
      その Class のオブジェクトそれぞれが active であることは同値。

    * あるオブジェクトが active であるとは、
      その classifierBehavior を実行開始して、
      それが完了するか、外部のオブジェクトから停止させられるかしなければ
      終わらないようなもの。

A_superClass_class
  * Class から Class への関連（単方向）。
  * Class は継承することができる。
  * A_general_classifier を class 側で subsets し、
    superClass 側で redefines する。

A_nestedClassifier_nestingClass
  * Class から Classifier への composite 関連（単方向）。
  * Class のスコープ内にいくつか Classifiers を入れ子で含めることがあり、
    Class はそれらに対する名前空間として振る舞う。

    * 入れ子は情報の隠蔽の役に立つ。

  * A_ownedMember_namespace, A_redefinitionContext_redefinableElement
    を subsets する。
  * 関連端 nestedClassifier は ``{ordered}`` である。

A_ownedAttribute_class
  * Class から Property への composite 関連（双方向）。
  * Class の Features の内 Properties なものである。
  * Class の Attributes は、その Class が所有する Properties である。
    これらの属性のうちいくつかは二項 Attributes の関連端を表現する。
  * A_attribute_classifier, A_ownedMember_namespace, A_ownedAttribute_structuredClassifier
    を subsets する。ownedAttributes は redefines する。
  * 関連端 ownedAttributes は ``{ordered}`` である。

A_ownedOperation_class
  * Class から Operation への composite 関連（双方向）。
  * Class の Features の内 Operations なものである。
  * Class の Operations は（何らかのパラメーターを伴って）オブジェクトの上で発動される。
  * A_feature_featuringClassifier, A_ownedMember_namespace, A_redefinitionContext_redefinableElement
    を subsets する。
  * 関連端 ownedOperation は ``{ordered}`` である。

A_ownedReception_class
  * Class から Reception への composite 関連（単方向）。
  * Class の持つ Receptions はどの Signals をこの Class のオブジェクトが扱うのかを指定する。
  * A_feature_featuringClassifier, A_ownedMember_namespace を subsets する。

A_extension_metaclass
  * Class から Extension への関連（双方向）。
  * Class は Profiles と metamodels の定義中で metaclass として振る舞ってよい。
    12 章で見ていく。
  * 両端ともに ``{readOnly}`` である。

11.4.4 Notation
----------------------------------------------------------------------
* Class の記法は Classifier のそれを用いる。

* 最も広く用いられる Classifier であるため、
  Class を指定するようなキーワードは不要である。

* 4 つの存在必須な区画 attributes, operations, receptions, internal structure がある。

* ステレオタイプ ``«Create»`` を Class のコンストラクターにマークする。

* Class::isActive が true なものについては、
  箱の枠の垂直辺両方を二重にして示すことがある。

* ステレオタイプ ``«Metaclass»`` を用いることがある。22 章で見ていく。

11.4.5 Examples
----------------------------------------------------------------------
* Figure 11.16 Class notation variants

  * 同じ Class Window を 3 通りの記法で示した。右へ行くほど詳細になる。
  * 可視性が指定されていない Operations があるが、
    実際に指定されている可視性を答えられるようにしておくこと。

* Figure 11.17 Class notation: attributes and Operations grouped according to visibility

  * 可視性で属性と操作をグループ化できる。どこか C++ のコードを思わせるような記法。

* Figure 11.18 Active Class

  * 枠の一部を二重線で描く。

* Figure 11.19 Connectors and Parts

  * Car オブジェクトが生成するときは常に
    4 つの Wheel オブジェクトが composition で生成する。
  * 併せて、前後それぞれの車輪間のリンクも生成する。

* Figure 11.20 Connectors and Parts in a structure diagram using multiplicities

  * 上のものと等価な Car オブジェクトである。
  * 多重度を記入することでシンボルの記入の手間と紙幅を節約する。

* Figure 11.21 An Instance of the Car Class

  * いちばん気になる部分のラベルが欠けている？

* Figure 11.22 InstanceSpecification indicating a constructor

  * コンストラクターの操作の文頭に標準ステレオタイプ ``«Create»`` を付す。
  * 戻り値の表現だろう、破線矢印で操作名とオブジェクトシンボルとを結ぶ。

* Figure 11.23 A constructor for the Car Class

  * 実践的なコンストラクターの仕様記法の見本。

* Figure 11.24 Showing that the extended Class is a metaclass

  * 拡張された Class Interface が実は metaclass であるということが明らさまになった。
  * とあるが、わかりやすさは微妙。

11.5 Associations
======================================================================

11.5.1 Summary
----------------------------------------------------------------------
* Association は型のあるオブジェクト間のリンクを表現する tuple_ の集合を分類する。
* AssociationClass は Association と Class の両方である。

11.5.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 11.25 Associations

  * 新クラスは Association と AssociationClass のふたつある。
  * この図式に現れる関連は、これまで見た関連のすべての中で最も重要であると思われる。

11.5.3 Semantics
----------------------------------------------------------------------
Association
  * Relationship かつ Classifier の一種である。
  * 形のあるオブジェクトの間に出て来る (occur) 意味関係を指定する。

  * isDerived: この Association が他のモデル要素（他の Associations 等）
    から得られるものかどうかを指定する。

  * この関連の関連端の isUnique の値が false であるとき、
    いくつかのリンクにオブジェクトの同じ集合を関連付けることが可能である。

  * この関連の関連端の isOrdered の値が true であるとき、
    リンクは関連端の値に加え、順序情報を携える。

  * N 個の memberEnds からなる Association に対して、
    任意の N - 1 個の関連端を選ぶ。
    その他の関連端を形成する Property を oep と呼ぶことにしよう。
    選んだ N - 1 個の関連端における Classifiers が oep の context となる。

  * 関連端の subset は Property のそれと同じ意味である。

  * 関連の specialization とは、
    特殊化している Association が分類するリンクが、
    特殊化されている Association もまた分類することを意味する。

  * 二項 Association は composite 集約（全体・部分関係）を表現してよい。

    * composition であることは関連端 part 側の属性 isComposite を true にすることで表現する。
    * 関連端 Property が shared または composition として印をつけてよいのは、
      その関連が二項かつ他方の関連端が shared 印も composition 印も付いていないときに限る。

AssociationClass
  * AssociationClass は Association と Class の両方である。
    ということは Classifier を二度継承することになるが、
    そこは重複しないで受け継ぐものとする。

A_endType_association
  * Association から Type への関連（単方向）。
  * 関連端の型を表現する関連。
    複数の関連端が同じ型であってもよいので、多重度は ``1..*`` になる。
  * A_relatedElement_relationship を subsets する。
  * 関連端 endType は ``{readOnly}`` である。

A_memberEnd_association
  * Association から Property への関連（双方向）。
  * Association は Properties が表現する関連端 memberEnds を ``2..*`` 個持つ。
    各関連端は Association リンク中のその関連端に接続されたオブジェクト群の関与を表現する。
  * A_member_memberNamespace を subsets する。
  * 関連端 memberEnd は ``{ordered}`` である。

A_ownedEnd_owningAssociation
  * Association から Property への composite 関連（双方向）。
  * 関連端 ownedEnd は、その Association 自身が所有するような関連端のことである。
  * A_feature_featuringClassifier,
    A_redefinitionContext_redefinableElement,
    A_ownedMember_namespace,
    A_memberEnd_association
    を subsets する。
  * 関連端 ownedEnd は ``{ordered}`` である。

A_navigableOwnedEnd_association
  * Association から Property への関連（単方向）。
  * ある Association のある end Property が、ある end Class によって所有されているとする。
    このとき、その Association が反対側の ends から navigable であることを示唆する。

    * 実行時に、リンクに関与するオブジェクトは反対側の ends のオブジェクトから
      効率的にアクセスできることを意味する概念が navigability である。

    * もしある関連端が navigable でないならば、
      反対側の関連端からそれにアクセス可能かもしれないし、そうでないかもしれない。
      そしてもしアクセス可能ならば、効率的ではないだろう。

  * 上述の A_ownedEnd_owningAssociation を subsets する。

A_qualifier_associationEnd
  * Property から Property への composite 関連（双方向）。
  * qualified 関連端は qualifiers という、
    関連端におけるオブジェクトに関連するオブジェクト群を仕切るものを持つ。
    各仕切りに qualifiers の一つの値が対応する。

  * A_ownedEnd_owner を subsets する。
  * 関連端 qualifier は ``{ordered}`` である。

11.5.4 Notation
----------------------------------------------------------------------
やや細かくノートをとりたい。

* どんな Association もダイヤモンド付き実線で描かれる。
* 二項 Association は通常二つの Classifiers を接続する実線として描かれる。
  両者が同じ Classifier の場合は、関連端が重ならないようにして描く。
* 実線は折れ線で構わない。意味も変わらない。

* Association 記号自体（関連端ではなく）にある種の装飾をしてもよい。

* 二項 Association の装飾として、黒三角が描かれることがある。
  文書目的のためだけに描かれるもの。

* Associations 間の Generalizations は、一つの generatization 矢印で示される。

* 関連端は Association を示す線と Classifier を示すアイコン（箱）との間の接続である。
  名前をその近くに置いてもよい。これは選択自由で非表示にできる。

* 関連端の近くに置ける各種記法は次のとおり。

  * 多重度
  * 中括弧で括られたアレ
  * 可視性を示す記号

* 先の開いた矢印は、そちら側は navigable な関連端である。
  小さなバツジルシがあれば、そちら側は navigable でない関連端である。

* 関連端が派生であるとき、名前の前にスラッシュを付けることでそのことを示してよい。

* 二項 Association は一つの関連端の aggregation の値として
  shared または composite を持ってよい。

  * shared ならば反対側の関連端に中身のないダイヤモンドを装飾する。
  * composite ならば同様に中身の詰まったダイヤモンドを装飾する。

* 関連 Classifier による関連端の所有権を示すのには小さいマル、通称ドットを用いる。

  * ドットは Classifier と関連矢印の間に描く。
    集約記号や navigability 記号と組み合わせて描かれてよい。

  * ドットが示すのは、ドットの触れた Classifier 型の Property を
    そのモデルが含むということである。
    この Property はもう一方の関連端点にある Classifier が所有する。

* 関連端の所有権を明示することは強制ではない。

  * Figure 11.26 のような場合、
    ドットが付いている endA は Classifier B が所有すると解釈するが、
    ドットの付いていない endB は曖昧さなしに BinaryAssociationAB が所有すると解釈する。

* AssociationClass は破線の Association に付着した Class として示す。

* 別々の関連線が図式内で交差する場合、電気回路図のように交点を半円にしてよい。

* 実用上、関連の navigability を表す矢印とバツを非表示にするのが便利である。
  その非表示のオプションが 3 つある。

* qualifier は関連端に付随する小さな矩形で示す。

  * Classifier の一部というより、Association の線の一部として示す。
  * 属性は qualifier box の内部に描く。記法は Classifier の属性と同じである。
  * qualifier を非表示にしてはならない。

11.5.5 Examples
----------------------------------------------------------------------
主題が重要なので、見本が豊富にある。

* Figure 11.27 Binary and ternary Associations

  * この例では偶然 Year が navigable なので有り難みがわかりにくいが、
    Association の名前を黒三角付きで直接記すことで、向きを表せるのは一般には助かる。

  * 関連端にある goalie はゴールキーパーの意。

* Figure 11.28 Association ends with various adornments

  * ``{subsets x}`` の意味をはっきり例示している。
    この場合は「クラス C のオブジェクトにとっては、
    集合 d は集合 b の部分集合である」の意味だ。

* Figure 11.29 Examples of navigable association-owned ends

  * 関連端の名前の違いを除けば EF がおそらく AB と同値である。
  * 関連端の名前の違いを除けば GH と IJ が同値であることに注意。
    本仕様書では主に IJ のスタイルを採用しているようだ。

* Figure 11.30 Examples of class-owned ends

  * ドット付きならば Class による所有、そうでなければ Association による所有。
  * EF の E 側にバツジルシを描いてもよい。
  * 関連端の名前の違いを除けば GH は AB と同値である。

* Figure 11.31 Example of attribute notation for navigable end owned by an end Class
* Figure 11.32 Derived supersets (union)

  * 以前理解できなかった derived union の説明もある。
  * 結論を言うと b は d から得られる。図式としては違和感があるが。
    「b はその部分集合となるような属性の全ての strict union を取ると得られる」である。

* Figure 11.33 Composite aggregation is depicted as a black diamond

  * 何度も見てきた composite 集約を示す黒ダイヤの見本。

* Figure 11.34 Composite aggregation sharing a source segment

  * 上の関連と同じ。

* Figure 11.35 Example AssociationClass Job, ...

  * AssociationClass を Association の線に対して破線を結ぶことで示す。
  * Job が二度現れているが、同一のモデル要素である。

* Figure 11.36 Example AssociationClass using diamond symbol

  * 上と同じ。

* Figure 11.37 Qualified associations

  * qualified Association の例。思ったよりも箱が大きい。
  * 左は Person を Bank::accountNo で識別することを示す。
  * 右は Square を Chessboard::rank および Chessboard::file で識別することを示す。

11.6 Components
======================================================================

11.6.1 Summary
----------------------------------------------------------------------
* 本節では任意の大きさと複雑さを持つソフトウェアシステムを定義するのに用いる構造の集合を仕様化する。
* Component とは何か、Component ベースの開発の要点は何か、等々。

  * 先に構築した Component の再利用は、Component ベースの開発の重要な観点。
  * Component は provided/required Interfaces を有する。
  * Component は可能な限り独立したものとして扱われるように設計されている。

* Components パッケージは論理的なものと物理的なものの両面の仕様化を支える。

11.6.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 11.38 Components

  * Component と ComponentRealization が新登場する。

11.6.3 Semantics
----------------------------------------------------------------------
Component
  * Component は Class の一種である。

  * Component は中身をカプセル化するシステムの一つのモジュール部品を表現し、
    それの manifestation がその環境の内部で取り替えることができるようなものである。

  * Component はいくらかの Classifiers の状態と振る舞いをカプセル化する自給自足な構成単位である。

  * Component は一つ以上の Artifacts によって表明 (manifested) される。
    そしてその Artifact が実行環境に配備される。
    ある DeploymentSpecification でその Component の実行をパラメーター化する値を定義してよい。
    19 章で見ていく。

  * システムまたはその他の状況での Components 間の配線 (wiring) は
    互換性のある単純 Ports 等々の間の Dependencies を用いて定義することが可能である。

  * Component は external view というものを持つ。
    その public な Properties と Operations によった view である。

  * Component は internal view というものを持つ。
    その private な Properties と実現 Classifiers によった view である。

  * Component に適用する UML 標準ステレオタイプがいくつかある。
    ``«Subsystem»``, ``«Specification»``, ``«Realization»`` 等ある。

  * isIndirectlyInstantiated: Component に適用するオブジェクト化の種類を示す。
    ここの説明文、意味がわからない。

ComponentRealization
  * Realization の一種。
  * Component はいくらかの Classifiers によって実現（または実装）されてよい。
    その場合、Component はそういう Classifiers への ComponentRealizations の集合を所有する。

A_required_component, A_provided_component
  * Component から Interface への関連（単方向）。
  * Component がそのサービスの契約をクライアントに指定するのは provided Interfaces による。
  * Component が他の Components やシステムのサービスに必要とする契約は required Interfaces による。
  * これらの Interfaces が等価な機能を有する Components 同士は、
    設計時または実行において置換可能である。

  * Component は provided Interface を直接実装してもよいし、
    その実現 Classifiers が実装してもよいし、
    継承してもよい。

  * required/provided Interfaces は Ports を通じて組織化されてよい。

A_packagedElement_component
  * Component から PackageableElement への composite 関連（単方向）。
  * Component はその定義に係る全てのモデル要素に対してはある Package のように振る舞う。
    そういうものは所有されるか明示的にインポートされるかのどちらかであるべきだ。
    典型的には Component を実現する Classifiers はその Component が所有する。

  * A_ownedMember_namespace を subsets する。

A_realization_abstraction
  * Component から ComponentRealization への composite 関連（双方向）。
  * 意味は上記 ComponentRealization のノート参照。

  * A_ownedElement_owner を subsets する。
  * A_supplier_supplierDependency を subsets する（向き注意）。

A_realizingClassifier_componentRealization
  * ComponentRealization から Classifier への関連（単方向）。
  * 意味は上記 ComponentRealization のノート参照。

  * 関連端 realizingClassifier の多重度は ``1..*`` である。
  * A_clientDependency_client を subsets する（向き注意）。

11.6.4 Notation
----------------------------------------------------------------------
* Component は Classifier の記法プラスキーワード ``«component»`` で示す。

  * オプションでコンポーネントアイコン（二つの小四角形が突き出た四角形）
    を右上隅に展示することが可能。この場合はキーワードが非表示でもよい。

  * 属性、操作、内部構造すべてが通常の意味を持つ。

  * Component の provided/required Interfaces はボール・ソケット記法で示してよい。
    それらの棒が Component の矩形から突き出るように描く。

* ComponentRealization は Realization 依存と同じ記法。
  すなわち一般的な破線矢印、矢の頭を白い三角とする。

* Component::packagedElements は選択自由の区画 "packaged elements" に展示してよい。

11.6.5 Examples
----------------------------------------------------------------------
* Figure 11.39 Example of an overview diagram (...)

  * Order は Account と Product に依存しているが、依存の種類は特記されていない。

* Figure 11.40 A Component with two provided and three required Interfaces

  * このようなロリポップとソケットが見えるだけの Component の図式を
    external view と呼ぶようだ。

* Figure 11.41 Black box notation showing a listing of provided and required interfaces

  * 上記と同じモデルを表現している。
  * 選択自由の区画 "provided interfaces" と "required interfaces" を用いている。

* Figure 11.42 Optional "white-box" representation of a Component

  * おそらく上記のモデルの "white box" view を示している。
  * さらに選択自由の区画 "realizations" と "artifacts" を用いている。
    前者にリストされているのは実現 Classifiers である。
    後者はこの Component の成果物の一覧になる。

* Figure 11.43 Explicit representation of provided and required Interfaces (...)

  * Dependency 記法を用いて provided/required Interfaces を明示的に表現している。
  * 矢印の描き分け方に注意。

* Figure 11.44 A representation of the realization of a complex Component

  * この図式全体が ComponentRealizations を示している。
  * 下側の Classifiers の集合が Component Customer を実現している。

* Figure 11.45 An alternative nested representation of a complex Component

  * 選択自由の区画 "packaged elements" の記法例。
  * OrderHeader と LineItem は区画 "realizations" でリストされるものと同じ。

* Figure 11.46 Example model of a Component, its provided and required Interfaces, (...)

  * Components 間の配線。込み入った図式。
  * /OrderableItem は Product のスーパータイプが実装する Interface であることを示す。
  * Component は AccountPayable が OrderHeader に依存していることを要求している。

* Figure 11.47 Internal structure of a Component

  * Component の内部構造の white-box view の見本。
  * 区画 "internal structure" に他の Components がいる。
  * 単純 Ports に ball-and-socket 記法が連結している。

* Figure 11.48 Delegation Connectors connect externally provided Interfaces to the parts (...)

  * この例では区画 "internal structure" にある parts は、
    区画 "packaged elements" にある Classes を型とする。

11.7 Collaborations
======================================================================

11.7.1 Summary
----------------------------------------------------------------------
* Collaborations の主な目的は、
  通信要素のシステムがどのように特定の課題を達成するかを説明することである。

* CollaborationUse はその collaborationRoles を演じている特定の要素が絡んでいる特定の状況に対して、
  Collaboration によって記述されるパターンの応用を表現する。

11.7.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 11.49 Collaborations

  * Collaboration と CollaborationUse を見ていく。

11.7.3 Semantics
----------------------------------------------------------------------
Collaboration
  * StructuredClassifier と BehavioredClassifier の両方の一種である。
  * Collaboration は協調しているオブジェクト群が、
    ある共同のタスクやタスクの集合を、
    どのように果たすのかを説明するのに用いられる。

CollaborationUse
  * NamedElement の一種である。
  * CollaborationUse は要素群の間の関係を表現する
    Collaboration の特定の利用法を説明するために表現する。

A_collaborationRole_collaboration
  * Collaboration から ConnectableElement への関連（単方向）。

  * ある与えられたオブジェクトは同時に複数の異なる Collaborations の
    collaborationRoles を演じてもよい。

  * collaborationRoles 間の Connectors はどういう通信路が
    参加オブジェクト間に存在する必要があるのかを指定する。

  * 特定の Collaboration において、
    全ての Features や、参加オブジェクトの全ての中身や、
    オブジェクト間の全てのリンクは必ずしも必要ではない。
    それゆえ、collaborationRoles は Interfaces によって定義されることがよくある。

  * Collaborations は他の Collaborations から特殊化されてよい。
    特殊化先の collaborationRoles の型は、特殊化元のそれの型に適合している必要がある。

  * Collaboration は直接オブジェクト化できるものではない。

  * A_role_structuredClassifier を subsets する。

A_type_collaborationUse
  * CollaborationUse から Collaboration への関連（単方向）
  * 関連端 type はこの CollaborationUse で使われている Collaboration である。
  * 関連端 type の多重度は 1 である。

A_roleBinding_collaborationUse
  * CollaborationUse から Dependency への composite 関連（単方向）。
  * roleBindings はその CollaborationUse が所有する Dependencies を使って実装される。
  * もし同じ ConnectableElement が Collaboration とその表現要素の両方で用いられているならば、
    roleBindings は必要ない。
  * roleBindings 中の client 要素と supplier 要素が互換性があるとき以上のことは仕様化されていない。

  * A_ownedElement_owner を subsets する。

A_collaborationUse_classifier
  * Classifier から CollaborationUse への composite 関連（単方向）。

  * 一つの Classifier の内側には与えられた Collaboration に関係する
    CollaborationUses が複数あってよい。

  * A_ownedElement_owner を subsets する。

A_representation_classifier
  * Classifier から CollaborationUse への関連（単方向）。

  * Classifier が所有する CollaborationUses の一つを
    その Classifier を総括する Behavior を代表するものとして拾い出してよい。
    これをその Classifier の representation と呼ぶ。

  * A_collaborationUse_classifier を subsets する。

11.7.4 Notation
----------------------------------------------------------------------
* Collaboration は破線の楕円で示す。

  * その名前を楕円内に含める。
  * collaborationRoles と Connectors で構成された内部構造を楕円内の区画に示してよい。
    この区画は Classifier の内部構造区画と同じ記法仕様に準じる。

* 代わりに composite structure 図が使える。
  あるいは通常の Classifier 矩形をキーワード ``«collaboration»`` を付けて使える。

* Properties でない collaborationRoles を持つ Collaboration の記法は定義がない。

* Collaboration の楕円とその Properties の矩形を離して描いて線で結ぶ記法もある。

* CollaborationUse は背景となる Classifier の内部構造区画内部に示す。

  * 各 roleBinding に対して、楕円からその client 要素へ破線がある。

* CollaborationUse の選択自由な記法は、キーワード ``«occurrence»`` 付きの破線矢印を、
  使う側の Classifier から使われる側の Collaboration へ結ぶ方法。

  * これと共に roleBindings は普通の Dependency 矢印として示される。

11.7.5 Examples
----------------------------------------------------------------------
* Figure 11.50 The internal structure of the Observer Collaboration

  * 破線楕円全体が Collaboration Observer である。
  * 区画内にある矩形がこの collaborationRoles であり、オブジェクトの名前が示してある。
  * オブジェクト間の実線が Connector を示す。

* Figure 11.51 Alternative notation for the parts of the Observer Collaboration.

  * 先のものとは異なる記法を適用している。詳細な仕様が認められる。

* Figure 11.52 The Sale Collaboration

  * Sale は collaborationRoles buyer と seller の間の Collaboration である。

* Figure 11.53 The BrokeredSale Collaboration

  * BrokeredSale は 3 つの collaborationRoles (producer, broker, consumer) の間の Collaboration である。
  * 同時に 2 種類の CollaborationUses (wholesale, retail) を含むことを示している。
    broker だけは両方の CollaborationUses が client 要素として共有する。

* Figure 11.54 A subset of the BrokeredSale Collaboration using «occurrence» and Dependency arrows

  * わかりにくくなった。

11.8 Classifier Descriptions
======================================================================
機械生成による節。

11.9 Association Descriptions
======================================================================
機械生成による節。

.. include:: /_include/uml-refs.txt
