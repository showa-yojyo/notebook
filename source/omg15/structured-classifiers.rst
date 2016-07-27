======================================================================
11 Structured Classifiers
======================================================================
UML 2.5 pp. 181-238 に関するノート。

.. todo:: 最低でもあと一回は編集する。

.. contents:: ノート目次
   :depth: 2

11.1 Summary
======================================================================
* StructuredClassifier とは、
  リンクされた ``roles`` のネットワークを形成する内部構造と
  ひとつまたはそれを超える Ports から構成される外部構造を
  持つことが許される Classifier である。

* EncapsulatedClassifiers の Ports は
  遠くにいる協力者らの局地的な代理人として振る舞い、
  EncapsulatedClassifiers が
  それらに直接に結合されることなく、
  それらを識別することをできるようにする。

* Classes, Components, Associations および Collaborations は
  これらの能力を使う具象的メタクラスである。

11.2 Structured Classifiers
======================================================================

11.2.1 Summary
----------------------------------------------------------------------
* StructuredClassifiers は、
  それぞれが StructuredClassifier によりモデル化された
  振る舞い全部で ``role`` を演じるような
  接続要素の、内部構造を含むことが許されている。

* この節を 11.5 節といっしょに読むことが役に立つ。

11.2.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 11.1 Structured Classifiers

  * StructuredClassifier, ConnectableElementTemplateParameter,
    ConnectableElement, Connector, ConnectorEnd
  * «enumeration» ConnectorKind

A_role_structuredClassifier
  * StructuredClassifier から ConnectableElement への関連（単方向）。
  * 先述したようにこの関連こそが StructuredClassifier の主な意味である。
  * A_member_memberNamespace を subsets する。
  * 両端ともに ``{readOnly, union}`` 制約がある。

A_ownedAttribute_structuredClassifier
  * StructuredClassifier から Property への composite 関連（単方向）。
  * A_attribute_classifier, A_ownedMember_namespace,
    A_role_structuredClassifier を subsets する。
  * 関連端 ownedAttributes に制約 ``{ordered}`` を付ける。
  * 関連端 structuredClassifier を ``{redefines}`` する。

A_part_structuredClassifier
  * StructuredClassifier から Property への単方向関連。
  * 上記 ``ownedAttributes`` で ``isComposite == true`` なものを
    ``parts`` とする。

    * よって ``parts`` は ``roles`` の部分集合を構成する。

  * 関連端 ``part`` は ``{readOnly}`` である。

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
  * Connector の端点を一つ取れば、対応する ``role`` が一意に対応する。
  * 関連端 ``end`` は ``{readOnly}`` である。

A_definingEnd_connectorEnd
  不明。説明文の意味を理解できない。

A_end_connector
  * Connector から ConnectorEnd への composite 関連（単方向）。
  * 先述した定義により関連端 ``end`` の多重度は ``2..*`` である。
  * 関連端 ``end`` は ``{ordered}`` である。
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
    このとき、Association (``type``) や ConnectorEnds (``ends``) の型もそれぞれの特殊化にすることが許されている。
    さらに ConnectorEnds の Property は置き換えてもよい。

11.2.3 Semantics
----------------------------------------------------------------------
11.2.3.1 Connectable Elements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ConnectableElement は抽象的クラスである。
  ConnectableElement それぞれは StructuredClassifier の
  内部構造の内部にある参加者を表現する。
  これらの参加者は ``roles`` と呼ばれる。

* ConnectableElement の詳細な意味はその具象型が与える。
  一般的に、ConnectableElement それぞれが
  有効 required Interfaces の集合と
  有効 provided Interfaces の集合を展示する。
  これらの集合は Connectors を用いた ConnectableElements の接続可能性を
  決定するのに用いられる。

* 委譲 Ports を除いた ConnectableElements に対して、
  有効 required Interfaces は required Interfaces であり、
  有効 provided Interfaces は provided Interfaces であり、
  次のように導かれる：

  * provided Interface は ConnectableElement とその上位型の ``type`` により
    実現される Interfaces の集合 (pl.) の和集合を形成する。
    すなわち、それが Interface による型ならば、
    ちょうど ``type`` を含む集合である。

  * required Interface は ConnectableElement とその上位型の ``type`` により
    使われる Interfaces の集合 (pl.) の和集合を形成する。

* ConnectableElement は
  テンプレートに対する仮引数としての
  ConnectableElementTemplateParameter を介して露出されてよい。

11.2.3.2 Parts and Roles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* StructuredClassifier の Properties は
  :doc:`./classification` で指定された意味に従う。

* Property は ConnectableElement の一種である。
  StructuredClassifier の ``ownedAttributes`` のすべては ``roles`` であり、
  Connectors を使って接続することが可能である。

* ``isComposite`` が true の StructuredClassifier の ``ownedAttributes`` は
  それの ``parts`` であるという。
  それゆえ ``parts`` は ``roles`` の部分集合を構成する。

11.2.3.3 Connectors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Connector は StructuredClassifier 内部の
  所有または継承された ``roles`` を演じる
  ふたつまたはそれを超えるオブジェクト間のリンクを指定する。

  * リンクのそれぞれはポインターと同じくらい簡単な何かや、
    ネットワーク接続と同じくらい複雑な何かにより実現されることが許され、
    オブジェクトが通信可能であることを表してよい。

* Associations が関連された Classifiers の
  適切な型のどのオブジェクト間のリンクを指定するのに対して、
  Connectors は接続された ``roles`` しか演じないオブジェクト間の
  リンクを指定する。

* Connector それぞれは
  ふたつまたはそれを超える ConnectableElements に取り付けてよく、
  それぞれは含んでいる StructuredClassifier のオブジェクト化に
  貢献するオブジェクトの集合を表現している。

* ConnectorEnd とは Connector の端点で、
  Connector を ConnectableElement へ取り付けるものである。

* Connectors に対応するリンクは
  含んでいる StructuredClassifier のオブジェクトの生成に続いて
  生成してよい。
  含んでいる StructuredClassifier オブジェクトが破壊されると
  そのようなリンクはすべて破壊される。

* Connector は Association によって型が付けられてよく、
  Connector が指定するリンクが Association 型のオブジェクトの場合である。

* Connector の一端における ConnectableElement それぞれの
  有効 required Interfaces それぞれの機能それぞれは、
  他方の端における ConnectableElements の
  有効 provided Interfaces の機能の中に
  互換機能を少なくともひとつ持つはずである。

* 単一の ConnectableElement に取り付けられた複数の連結器があると、
  その意味は、
  ConnectableElement を
  複数の連結器を介して接続された ConnectableElements のすべてに
  接続する単一の n 項 Connector と同じになる。

* Connectors には種類があり、
  その値は assembly か delegation である。

* ConnectorKind は次のリテラル値の列挙体である：

  * assembly: Connector は assembly Connector である。
  * delegation: Connector は delegation Connector である。

* Behaviors は Connectors に ``contracts`` として結び付けてよく、
  Connector の両端で有効な相互作用パターンを指定する。

11.2.3.4 Multiplicities and topologies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ConnectableElements 上の多重度は
  含む StructuredClassifier のオブジェクト内部で
  生成が許されるオブジェクトの個数を強制し、
  それは MultiplicityElement の意味に従う。

* 二項 Connector に対しては、
  ConnectorEnd の多重度は
  他方の関連端での ConnectableElement のオブジェクトそれぞれに
  リンクしてよいオブジェクトの個数を示す。
  n 項 Connector に対しては、
  一方の関連端の多重度は
  他方の関連端それぞれに対する特定のオブジェクトを含む集合を参照してよい
  リンクの個数を強制する。

* StructuredClassifier のオブジェクトの ``role`` からオブジェクトを取り除くと、
  ``role`` と他のものの間の Connectors によって存在するリンクは破壊される。

* ConnectorEnds の多重度と、
  それらが相互接続する ConnectableElements のそれらとを
  マッチングすることにより生じる位相は、
  モデルから推論することはいつでも可能とは限らない。

11.2.4 Notation
----------------------------------------------------------------------
* StructuredClassifier の内部構造は
  名前が "internal structure" である分離区画に示す。
  この区画は必須である。

* ``part`` は
  内部構造区画の内側で
  ``part`` を表す実線輪郭の箱記号の図式的な入れ子で示してよい。
  合成ではない ``role`` oは
  破線輪郭の箱記号の図式的な入れ子で示してよい。

  * 厳密には合成だけが ``parts`` であるにもかかわらず、
    いずれの場合にも箱を part box と呼んでよい。

* Property に対する多重度は、
  記法を用いて part box の右上隅に描かれた多重度マークとして示してもよい。

* ``role`` が EncapsulatedClassifier 型のときは、
  ``type`` の Ports はいずれも
  ``role`` を表す part box の境界に重なり合う
  小さな四角記号として示してもよい。

* ``role`` が Class でない classifier の型であれば、
  part box 記号の名前区画は名前の上に
  適宜 «component» のようなキーワードを含む。

* Connector は Association に対するそれと同様の表記法を使って描く。

* ConnectorEnd では Association の端での修飾と同じ表記法を使って
  修飾を見せてよい。

* ConnectorEnd が内部構造の ``part`` または ``role`` 上の
  Port に取り付けられており、多重度が示されていなければ、
  ConnectorEnd の多重度は Port の多重度と
  ``role`` の多重度の積に等しい。

* 下の三つの表記法の仕様はオプションである。
  準拠ツールは実装する必要はない。

  * ``parts`` が単純な Ports を持つならば、
    ball and socket 記法を Ports 間の assembly Connectors を表すのに用いてもよい。

  * 単純 Ports を接続するときには
    assembly または delegation に対しての普通の Connector 表記法を
    Port 記号自身へではなく ball and socket 記号へ接続されるように（？）
    示してよい（原文で動詞がふたつあるような？）。

  * ふたつを超える単純 Ports を接続する n 項 Connector があり、
    ふたつまたはそれを超える Ports が同じまたは互換な Interfaces を
    与えるか要求するときには、
    Interface を表す単一の記号が示されることが可能であり、
    Components から伸びる線がその記号へ引かれることが可能であるが、
    これは channeled ball and socket 表記法である。

* 内部構造区画は CollaborationUses を表す記号を含んでもよいが、
  それは 11.7.4 で記される表記法に従う。

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
    どちらも箱の枠線に重なる小さい四角がある。

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

  * 関連端の多重度が付随する ``roles`` の多重度とがマッチしている場合 (i)、
    何か n 部グラフのようなリンク構造に解釈 (ii) する。

* Figure 11.7 "Array" Connector pattern

  * (i) では関連端の多重度が 1 なので、
    リンクの意味は (ii) に示すようにパラレルに解釈する。

* Figure 11.8 An assembly Connector ...

  * 単純 Ports のついた Component 型 ``parts`` の記法例。
  * 選択自由の ball and socket 記法を採用している。
    この記法は互換性のある Ports 間の組み立て Connector を表現する。

* Figure 11.9 An n-ary Connector ...

  * ある 4 項 Connector のための channeled ball and socket 記法の見本。
  * ボールのほうが provided Interfaces; Client is-a Person とのこと。
  * ソケットのほうが required Interfaces

11.3 Encapsulated Classifiers
======================================================================

11.3.1 Summary
----------------------------------------------------------------------
* EncapsulatedClassifier は Ports を所有する能力を持たせるように
  StructuredClassifier を拡張するもので、
  EncapsulatedClassifier を環境から分離する仕組みである。

11.3.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 11.10 Encapsulated Classifiers

  * EncapsulatedClassifier と Port の関連を中心とした図式。

A_ownedPort_encapsulatedClassifier
  * EncapsulatedClassifier から Port への composite 関連（単方向）。

  * EncapsulatedClassifier は複数の Ports を定義する能力があり、
    相異なる通信をそれが起こる Port に基いて区別することが可能になる。

  * A_ownedAttribute_structuredClassifier を subsets する。
  * 関連端 ``ownedPort`` は ``{readOnly}`` である。

A_required_port
  * Port から Interface への関連（単方向）。
  * 関連端 required は ``port`` を通じて
    EncapsulatedClassifier から環境への依頼を特徴づける
    Interfaces である。
    EncapsulatedClassifier オブジェクトは
    required Interfaces が所収する Features が、
    環境下の一つ以上のオブジェクトが提示することを期待している。
  * 関連端 ``required`` は ``{readOnly}`` である。

A_provided_port
  * Port から Interface への関連（単方向）。
  * 関連端 provided は ``port`` を通じて
    EncapsulatedClassifier への、環境が作る依頼を特徴づける
    Interfaces である。
    所有者である EncapsulatedClassifier は
    provided Interfaces が所有する Features を提示する必要がある。
  * 関連端 ``provided`` は ``{readOnly}`` である。

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

11.3.3 Semantics
----------------------------------------------------------------------
11.3.3.1 Ports
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Ports は
  それを EncapsulatedClassifier がそれの環境と連絡を取るために
  相互作用点を表現する。

  * EncapsulatedClassifier の内部をそれの環境から疎結合することにより、
    Ports は EncapsulatedClassifier が環境に依存することなく
    定義できるようにし、
    Ports により課せられる制約に適合する環境のどれにおいても
    EncapsulatedClassifier が再利用可能になる。

* Port とは、
  次のどちらかの別個の相互作用点を指定する
  EncapsulatedClassifier の Property である。

  * EncapsulatedClassifier とそれの環境との間
  * EncapsulatedClassifier の Behavior とそれの内部の ``roles``

* 特性 ``isService`` が true であると、
  この Port が EncapsulatedClassifier の公表された機能を与えるのに
  用いられることを指し示す。

* 成句「Port on Port」、より一般には「Port on Property」は、
  StructuredClassifier で ``role`` を演じる Property が
  Ports を持つ EncapsulatedClassifier により型付けられるという
  状況を知らせる。

* Port に結び付いた Interfaces は
  それを超えて起こり得る相互作用の本質を指定する。

* Property の一種なので、Port は ``type`` を持つ。
  Port の ``provided`` および ``required`` Interfaces は
  ``isConjugated`` の値により仲介された
  それの ``type`` に関係する。

  * ``isConjugated`` が true だと、
    ``provided`` は Port の ``type`` およびそれの上位型により
    用いられる Interfaces の集合 (pl.) の和集合として得られる。
    それに対して、
    ``required`` は Port の ``type`` およびそれの上位型により
    実現される Interfaces の集合 (pl.) の和集合として得られる。
    すなわち、
    Port がある Interface によって型付けられると、
    Port の ``type`` から直接得られる。

  * ``isConjugated`` が false だと、上記の定義があべこべになる。

* Interfaces は
  Port をまたぐ相互作用の正確な順序を必ずしも制定しない。

* EncapsulatedClassifier のオブジェクトが生成すると、
  それの Port それぞれに対応するオブジェクトが生成されて、
  それの ``type`` と多重度どおりに、
  Port それぞれが指定する Slots に収容される。
  これらのオブジェクトは相互作用点 (interaction points) と呼ばれ、
  一意な参照を与える。

* 次において、
  「Port に到着する要求」とは
  「この Port に対応するこのオブジェクトの相互作用点に到着する
  要求の出来事」を意味するものとする。

* 特性 ``isBehavior`` を true とすることにより、
  この Port に到着するどんな要求も、
  含まれているオブジェクトのどれに転送されるのでもなく、
  所有する EncapsulatedClassifier のオブジェクトの
  Behavior により処理される
  ことを指定する能力を Port が有する。
  このような Port は振る舞い Port と呼ばれる。

* 委譲 Connector とは、
  Port と所有する EncapsulatedClassifier で ``role`` を
  リンクする Connector である。

  * 要求の転送を表現する。

* 委譲 Connectors は振る舞いの階層的な分解をモデル化するのに用いられ、
  EncapsulatedClassifier により与えられるサービスは、
  究極的にはその内部に複数階層の深さに入れ子になったもので
  実現されることが許される。

* ConnectableElement であるので、
  Port の有効 provided Interfaces はそれの provided Interfaces であり、
  有効 required Interfaces はそれの required Interfaces である。
  しかし、委譲 Port
  つまり委譲 Connector の一端にあって、
  かつ ``role`` 上にはなく、
  なおかつ振る舞い Port ではない Port に対しては、
  有効 provided Interfaces はそれの required Interfaces であり、
  有効 required Interfaces はそれの provided Interfaces となる。

* Connectors のいくつかが Port の一方の側に取り付けられてるならば、
  Port の反対側のある Connector から得られるリンク上の
  Port に到着する要求はいずれも
  これらの Connectors に対応するリンクで転送されるはずである。

  * これらの要求がすべてのリンクを使って転送されるものなのか、
    またはそれらのリンクのうちのひとつしか使われないものなのかは
    定義されていない。

11.3.4 Notation
----------------------------------------------------------------------
* EncapsulatedClassifier の Port は小さい正方形で示す。

  * Port の名前を正方形の近くに置く。

  * Port 記号は EncapsulatedClassifier を示す矩形記号の境界と重ね合わせてもよいし、
    矩形記号の内側に示してもよい。

  * 内部構造区画にある ``parts`` や ``roles`` のように、
    Port が EncapsulatedClassifier の区画に視覚上含まれる要素に接続しているときは、
    Port 記号はその区画の境界の内部に置かれるか、
    重なり合うはずである。

* Port の ``type`` を名前に続けて示してもよく、コロンで区切られる。

  * Port に対する ``isConjugated`` が true のとき、
    Port の ``type`` はチルダを前に付加して示す。

* behavior Port は線分を通じて、
  含んでいる EncapsulatedClassifier を表す記号の内側に描かれる
  小さい状態記号へ接続されている Port により示す。
  小さい状態記号は含んでいる EncapsulatedClassifier の
  Behavior を示す。

* Port の名前は隠してよい。

* 複数の Interfaces が Port に結びついていると、
  これらの Interfaces は一つの Interface のロリポップで
  列記してよく、それらはカンマで区切られる。

* required Interface の単純 Port から
  provided Interface の単純 Port をつなぐ Dependency では、
  ソケットからロリポップへと結ぶ依存矢印を見せるかどうかは
  表記法上任意である。

11.3.5 Examples
----------------------------------------------------------------------
* Figure 11.11 Port notation

  * Ports に対する表記法を説明する図である。

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

  * 振る舞い Port の p を説明する。
  * p のラベルの位置と、小さい四角にくっついたオマケのシンボルに注意。

* Figure 11.13 Port notation showing multiple provided Interfaces

  * ふたつの provided Interfaces, OrderEntry と Tracking がある
    Class OrderProcess にくっついている Port OnlineServices を示す。

  * ロリポップに provided Interfaces の名前をふたつまとめて示す。

* Figure 11.14 Port examples

  * provided Interface である IPowerTrain により
    型付けられた Port p を持つ Class Engine を示す図。

  * 右側の Car と Boat の内部構造それぞれの
    Port の付き方の違いを説明できるようにしておくこと。

  * 単純 Ports なので、Boat 内部の連結器の描写は
    Figure 11.4 で示された表記法選択肢のどれを使って
    示してもよかった。

11.4 Classes
======================================================================

11.4.1 Summary
----------------------------------------------------------------------
* Class は EncapsulatedClassifier と BehavioredClassifier の
  具象的実現である。
  Class の目的はオブジェクトの分類を指定することと、
  それらのオブジェクトの構造と振る舞いを特徴づける
  Features を指定することである。

11.4.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 11.15 Classes

  * Class は自らを再定義する関連と、
    何かを所有するといういくつかの関連が加わる程度。

A_superClass_class
  * Class から Class への関連（単方向）。
  * Class は継承することができる。
  * A_general_classifier を ``class`` 側で subsets し、
    ``superClass`` 側で redefines する。

A_nestedClassifier_nestingClass
  * Class から Classifier への composite 関連（単方向）。
  * Class のスコープ内にいくつか Classifiers を入れ子で含めることがあり、
    Class はそれらに対する名前空間として振る舞う。

  * A_ownedMember_namespace, A_redefinitionContext_redefinableElement
    を subsets する。
  * 関連端 ``nestedClassifier`` は ``{ordered}`` である。

A_ownedAttribute_class
  * Class から Property への composite 関連（双方向）。
  * Class の Features の内 Properties なものである。
  * Class の Attributes は、その Class が所有する Properties である。
    これらの属性のうちいくつかは二項 Attributes の関連端を表現する。
  * A_attribute_classifier, A_ownedMember_namespace,
    A_ownedAttribute_structuredClassifier
    を subsets する。ownedAttributes は redefines する。
  * 関連端 ``ownedAttributes`` は ``{ordered}`` である。

A_ownedOperation_class
  * Class から Operation への composite 関連（双方向）。
  * Class の Features の内 Operations なものである。
  * Class の Operations は（何らかのパラメーターを伴って）
    オブジェクトの上で発動される。
  * A_feature_featuringClassifier, A_ownedMember_namespace, 
    A_redefinitionContext_redefinableElement
    を subsets する。
  * 関連端 ownedOperation は ``{ordered}`` である。

A_ownedReception_class
  * Class から Reception への composite 関連（単方向）。
  * A_feature_featuringClassifier, A_ownedMember_namespace を subsets する。

A_extension_metaclass
  * Class から Extension への関連（双方向）。
  * 両端ともに ``{readOnly}`` である。

11.4.3 Semantics
----------------------------------------------------------------------
11.4.3.1 Classes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Class とは、
  それの Features が Properties, Operations, Receptions, Ports, Connectors
  である EncapsulatedClassifier の一種である。

  * Class の属性とは、
    Class により所有される Properties である。
    これらの ``attributes`` のいくつかは二項 Associations の端点を
    表現することが許される。

* Class のオブジェクトは
  Class のメンバーである ``attribute`` それぞれに対して、
  例えばそれの ``type`` と多重度のような ``attribute`` の特徴に
  従って、値を含む必要がある。

* Class でオブジェクトが生成されると、
  既定値が指定された Class の ``attribute`` ごとに対して、
  ``attribute`` の初期値がその生成にとって明示的に指定されていなければ、
  既定の ValueSpecification が評価されて、
  オブジェクトに対する ``attribute`` の初期値を設定する。

* Operation の引数に対する値の特定の集合があれば、
  :doc:`./classification` で指定された意味に従い、
  Class の Operations はオブジェクトで発動することが可能でる。

* Class は別のクラスの非公開 Features や、
  また、自分の祖先ではない別のクラスの保護 Features には
  アクセスすることができない。

* Class はスコープ内部で定義されたさまざまな種類の Classifiers
  に対する名前空間として振る舞う。
  入れ子の Classifiers は含む Class の名前空間のメンバーである。
  Classifier の入れ子は情報隠蔽の理由のために用いられる。

* Class は ``isActive`` を true とすることにより
  active であるとされるように指示してよい。
  ``isActive`` が false だとその Class は passive である。

* オブジェクトが active であるとは、
  その生成の直接のなりゆきとして、
  その ``classifierBehavior`` を実行することを開始し、
  完全 Behaviored が実行されるか、
  オブジェクトがある外的オブジェクトにより停止されるかのどちらかまでは
  中断しないオブジェクトである。

* Class の Receptions は
  どの Signals がこの Class のオブジェクトを処理するかを指定する。

* InstanceSpecification を用いて
  Class に対して生成される初期値を指定してもよい。

* Class のオブジェクトが削除されるときには、
  その Class の ``parts`` オブジェクトと Ports に対応する
  オブジェクトのすべてが再帰的に削除される。

* Class は Profiles とメタモデルの定義でメタクラスとして振る舞ってよい。
  :doc:`./packages` で見ていく。

11.4.4 Notation
----------------------------------------------------------------------
* Class の記法は Classifier のそれを用いる。
  最も広く用いられる Classifier であるため、
  Class を指定するようなキーワードは不要である。

* 4 つの存在必須な区画 attributes, operations,
  receptions, internal structure がある。

* Class の operations 区画は
  :doc:`./packages` で指定された表記法を使う
  その ``ownedOperations`` を表す表記法を含む。
  receptions 区画は
  :doc:`./simple-classifiers` で指定された表記法を使う
  ``ownedReceptions`` を含む。

* 使用依存は InstanceSpecification をクラスに対するコンストラクターに
  関係させてよく、コンストラクター Operation により返される
  単一の値を記述する。

  * Operation が ``client`` であり、
    生成オブジェクトが ``supplier`` である。

  * ステレオタイプ «Create» を Class のコンストラクターにマークする。

* ``isActive`` が true な Class を
  箱の枠の垂直辺のどちらとも二重にすることで示してよい。

* メタクラスを表現する Class は
  オプションのステレオタイプ «Metaclass» を
  その名前の上または前に付すことで拡張してよい。
  :doc:`./standard-profile` を参照。

11.4.5 Examples
----------------------------------------------------------------------
* Figure 11.16 Class notation variants

  * 同じ Class Window を 3 通りの記法で示した。右へ行くほど詳細になる。
  * 可視性が指定されていない Operations があるが、
    実際に指定されている可視性を答えられるようにしておくこと。

* Figure 11.17 Class notation: attributes and Operations grouped according to visibility

  * 可視性で属性と操作をグループ化できる。
    どこか C++ のコードを思わせるような記法。

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

  * コンストラクターの操作の文頭に標準ステレオタイプ «Create» を付す。
  * 戻り値の表現だろう、破線矢印で操作名とオブジェクトシンボルとを結ぶ。

* Figure 11.23 A constructor for the Car Class

  * 実践的なコンストラクターの仕様記法の見本。

* Figure 11.24 Showing that the extended Class is a metaclass

  * 拡張された Class Interface が実はメタクラスであるということが
    明白になった。
  * とあるが、わかりやすさは微妙。

11.5 Associations
======================================================================

11.5.1 Summary
----------------------------------------------------------------------
* Association は型のあるオブジェクト間のリンクを表現する
  tuple_ の集合を分類する。

* AssociationClass は Association と Class の両方である。

11.5.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 11.25 Associations

  * 新クラスは Association と AssociationClass のふたつある。
  * この図式に現れる関連は、これまで見た関連のすべての中で最も重要であると思われる。

A_endType_association
  * Association から Type への関連（単方向）。
  * 関連端の型を表現する関連。
    複数の関連端が同じ型であってもよいので、多重度は ``1..*`` になる。
  * A_relatedElement_relationship を subsets する。
  * 関連端 ``endType`` は ``{readOnly}`` である。

A_memberEnd_association
  * Association から Property への関連（双方向）。
  * Association は Properties が表現する関連端 memberEnds を ``2..*`` 個持つ。
    各関連端は Association リンク中のその関連端に接続されたオブジェクト群の関与を表現する。
  * A_member_memberNamespace を subsets する。
  * 関連端 memberEnd は ``{ordered}`` である。

A_ownedEnd_owningAssociation
  * Association から Property への composite 関連（双方向）。
  * 関連端 ``ownedEnd`` は、その Association 自身が所有するような関連端のことである。
  * A_feature_featuringClassifier,
    A_redefinitionContext_redefinableElement,
    A_ownedMember_namespace,
    A_memberEnd_association
    を subsets する。
  * 関連端 ownedEnd は ``{ordered}`` である。

A_navigableOwnedEnd_association
  * Association から Property への関連（単方向）。
  * 上述の A_ownedEnd_owningAssociation を subsets する。

A_qualifier_associationEnd
  * Property から Property への composite 関連（双方向）。
  * A_ownedEnd_owner を subsets する。
  * 関連端 ``qualifier`` は ``{ordered}`` である。

11.5.3 Semantics
----------------------------------------------------------------------
11.5.3.1 Associations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Association は型付けられたオブジェクト間にあり得る意味論的関係を指定する。
  Properties で表される ``memberEnds`` を少なくともふたつ持ち、
  それぞれには端の型がある。

* Association は
  その型が関連した型に対して適合したり実装したりするオブジェクト間の
  リンクが存在することが可能であることを宣言する。
  リンクは Association の ``memberEnd`` それぞれについての
  値の組であり、値それぞれは端における型に適合したり、
  型を実装したりするオブジェクトである。

* リンクの全てが Association によって分類される必要はない。

* Association のひとつまたはそれを超える端で ``isUnique`` が false だと、
  リンクのいくつかを同じオブジェクトの集合に関連させることができる。
  そういう場合には、リンクは端の値とは別にさらなる識別子を含む。

* Association のひとつまたはそれを超える端が順序付けられていると、
  リンクはその端の値に加えて順序情報を含む。

* N 個の ``memberEnds`` がある Association に対して、
  任意の N - 1 個の端を選ぶ。
  その他の端を制定する Property を oep と呼ぶことにして、
  選んだ N - 1 個の端における Classifiers が oep にとっての
  context となるようにする。

* Association の端の部分集合を作ることは
  Property のために指定された意味を持つ。

* 特殊化とは、部分集合を作ることに対して、
  作為的な意味の領域にある関係であり、
  つまり、
  メンバーシップによってではなく、
  集まりにあるメンバーシップが定義されることによって
  規範を特徴付けることである。

* n 項 Associations では端の多重度の下限は典型的にゼロである。
  n 項 Association の端に対する多重度の下限が 1 であることは、
  リンク一個がその他の端に対する値のあり得る組み合わせごとに
  存在するはずであることを含意する。

* 二項 Association は合成集約（全体・部分関係）を表現してよい。

  * 合成は Association の ``part`` 端の ``isComposite`` 属性を
    true とすることで表現する。

  * その関連が二項であり、
    もう一方の端が shared にも composition にも
    特徴づけられていないならば、
    Association の端 Property が shared または composition としてしか
    特徴づけられてはならない。

* 端 Class により所有される Association か、
  Association の ``navigableOwnedEnd`` である Association の端 Property は
  Association が反対側の端 (pl.) から航行可能であることを示す。
  そうでなければ、
  Association は反対側の端 (pl.) から航行可能でない。

  * 航行可能性が意味するのは、
    実行時にリンクに関与するオブジェクト、Association のオブジェクト、は、
    Association の他方の端にあるオブジェクトから効率的にアクセス
    できることである。

  * 端が航行可能でないと、
    反対側の端からのアクセスが可能であってもなくても構わない。
    そしてもし可能ならば、効率的ではないかもしれない。

* 限定された Associaiton 端は
  端におけるオブジェクトに結び付いたオブジェクト、
  被限定オブジェクト、たちを分割する``qualifiers`` を持つ。

  * 各分割は ``qualifier`` 値で指名されるが、
    これは各 ``qualifier`` に対するある値を含む組である。

* 関連の有無はモデルの他の情報より求められてよい。
  Associaiton の派生とその端の派生との間の論理的な関係はモデル固有である。

11.5.3.2 Association Classes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* AssociationClass とは、
  それ自身の Features の集合を持つ Association の宣言である。

* AssociationClass は Association と Class の両方であるゆえ、
  Features を持つ能力だとか、
  ``name`` を持つことだとか、
  共通する特性の集合を持つ。
  これらの特性は同じ構造から複数回継承されて、重複されない。

* AssociationClass は合成 Properties Class::``ownedAttribute`` と
  Association::``ownedEnd`` を継承する。

* AssociationClass のオブジェクトは
  Association の一種としての AssociationClass のオブジェクト化を表す
  リンクと、
  Class の一種としての AssociationClass のオブジェクト化を表す
  オブジェクトの両方の特徴を備える。

* AssociationClass の端すべてが ``isUnique`` が true であるとしても、
  オブジェクトのいくつかに端 Classes のオブジェクトの同じ集合を
  結びつけさせることができる。

* AssociationClass は Association または Class の一般化になり得ない。

11.5.4 Notation
----------------------------------------------------------------------
* どんな Association も
  ダイヤモンドが端の型である Classifier に接続している
  Association ``memberEnd`` それぞれに
  一本の実線の付いた一個のダイヤモンドとして描いてよい。
  二個を超える端を持つ Association はこの方法でしか描くことができない。

* 二項 Association は通常二つの Classifiers を接続する実線として描かれる。
  両者が同じ Classifier の場合は、関連端が重ならないようにして描く。
* 実線は折れ線で構わない。意味も変わらない。

* Association 記号には次のように修飾をしてもよい：

  * Association の名前を名前文字列として Association 記号の付近に、
    ただし端の名前と間違えるほど十分近くではないところに、
    示すことができる。

  * Association の名前の前に、
    または名前が示されていなければ名前の代わりに
    現れるスラッシュは、
    Association を導出されるものとして特徴付ける。

  * 特性文字列は Association 記号の付近に、
    ただし端の特性文字列を間違えぬよう十分離して
    配置することが許される。

* 実線として描画される二項 Association で、
  Association の名前の隣にあるかまたは代わりとなる、
  ある端の方向の直線に沿って指し示す黒三角は、
  その端が Association の端順序で末尾に来るものとすることを示す。

* Associations 間の Generalizations は、
  Association 記号間にある一般化矢印を使って示される。

* Association 端は
  Association を描く直線と
  接続された Classifier を描くアイコン（しばしば箱）との間の接続である。
  名前文字列を直線の端の近くに置いて
  Association 端の名前を示すのもよい。
  名前は選択自由で非表示にできる。

* 直線の端の近くに置ける他の記法各種は次のとおり：

  * 多重度
  * 中括弧で括られた <prop-modifier>
  * <visibility> 記号

* Association の端にある開いた矢先は、その端が航行可能であることを示す。
  Association の端にある小さなバツジルシは、
  その端が航行可能でないことを示す。

* Association 端が導出されていれば、
  これを名前がなければその代わりに、
  名前があればその前にスラッシュを付けることで示してよい。

* 二項 Association は一方の端の ``aggregation`` が
  AggregationKind::shared または AggregationKind::composite であってよい。

  * shared ならば反対側の関連端を中身のないダイヤモンドで修飾する。
  * composite ならば同様に中身の詰まったダイヤモンドで修飾する。

* 関連 Classifier による Association 端の所有権は小さい黒塗りの円で
  図式的に示してよいが、簡潔さのためにドットと呼ぶことにする。

  * ドットは Classifier と関連矢印の間に描く。
    集約記号や航行可能記号と組み合わせて描かれてよい。

  * ドットが示すのは、ドットの触れた Classifier 型の Property を
    そのモデルが含むということである。
    この Property はもう一方の関連端点にある Classifier が所有する。

* 端の所有権の表記法は強制ではない。
  すなわち、準拠ツールがそれを支援しないことがあり得る。

* Figure 11.26 のような場合、
  ドットが付いている endA は Classifier B が所有すると解釈するが、
  ドットの付いていない endB は曖昧さなしに
  BinaryAssociationAB が所有すると解釈する。

* 航行可能の表記法は過去において非公式の習慣に従ってよく使われたが、
  航行可能な端は他方の端の Classifier により所有されると仮定された
  ゆえに、
  航行不可能な端は Association により所有されると仮定されたのであった。
  この慣習は今では嫌われている。

* AssociationClass は破線の Association 経路に取り付けられた
  Class 記号として示す。

* 論理的には AssociationClass と Association は同じ意味の実体であるが、
  それらは図式的には見分けられる。

* 二本の関連線が交差するときには、準拠ツールは
  電気回路図のように交点を半円にして示すオプションを提供してよい。

* 関連端の航行可能性を知らせる矢印とバツのいくつかを
  非表示にするのが便利であることが実用上ではよくある。
  その非表示のオプションが 3 つある。

* ふたつまたはそれを超える集約が同じ集まりを指すならば、
  準拠ツールは純粋に表現上のオプションとして、
  集約端を黒塗りまたは白抜きの集約ダイヤモンド記号で修飾された
  単一の欠片に併合することによる木として示してよい。

* ``qualifier`` は
  最終経路欠片とそれに接続する Classifier の記号の間にある
  関連パスの端に取り付けられた小さな矩形として示す。

  * Classifier の一部というより、Association の線の一部として示す。

* 対象端に取り付けられた多重度は
  限定されたオブジェクトと限定する値を対にすることで
  選択された対象オブジェクトの集合の取り得る濃度を記す。

* 限定子属性は qualifier box の内部に描く。

* いささか珍しいのではあるが、
  限定子を単一の関連の端ごとに持たせることが認められる。

* 限定子を非表示にしてはならない。

11.5.5 Examples
----------------------------------------------------------------------
主題が重要なので、見本が豊富にある。

* Figure 11.27 Binary and ternary Associations

  * 黒塗り三角は Player PlayedInYear Year という読み順を示す。
  * 関連端にある goalie はゴールキーパーの意。

* Figure 11.28 Association ends with various adornments

  * さまざまな修飾の付いた Association 端の例。
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

  * Class により所有された Association 端は属性でもあるので、
    属性表記法が Class により所有された Association 端を表すのに
    用いることが可能である。
    冗長につき普通は非表示となるものなのだが、
    この表記法を関連表記法と共に用いて、
    属性が Association 端でもあることをはっきりとさせてよい。

* Figure 11.32 Derived supersets (union)

  * 以前理解できなかった derived union の説明。
  * 結論を言うと b は d から求められる。
    「b はその部分集合となるような属性の
    全ての strict union を取ると求められる」である。

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
* 本節では任意の大きさと複雑さを持つソフトウェアシステムを
  定義するのに用ることができる構成概念の集合を仕様化する。

* Component を基礎とする開発の重要な様相は
  先に構築した Components の再利用である。

  * Component にはひとつまたはそれを超える
    ``provided`` and/or ``required`` Interfaces があるが、
    Component の内部は、
    それの Interfaces により与えられたもの以外は、
    隠蔽されてアクセスできない。

  * 要求されている Interfaces に関しては
    Component は他の要素に依存してよいかもしれないが、
    Component はカプセル化され、その Dependencies は
    Component は可能な限り独立して扱われることができるように
    設計されている。

* 自律と再利用の様相は配備時における Components にまで及ぶ。

* Components パッケージは論理的な Components と
  物理的な Components の両方の仕様を、
  それらとそれらが配備かつ実行されるノードを実装する成果物と一緒に
  支援する。

11.6.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 11.38 Components

  * Component と ComponentRealization が新登場する。

A_required_component, A_provided_component
  * Component から Interface への関連（単方向）。
  * Component がそのサービスの契約をクライアントに指定するのは
    ``provided`` Interfaces による。
  * Component が他の Components やシステムのサービスに必要とする契約は
    ``required`` Interfaces による。

A_packagedElement_component
  * Component から PackageableElement への composite 関連（単方向）。
  * A_ownedMember_namespace を subsets する。

A_realization_abstraction
  * Component から ComponentRealization への composite 関連（双方向）。
  * A_ownedElement_owner を subsets する。
  * A_supplier_supplierDependency を subsets する。

A_realizingClassifier_componentRealization
  * ComponentRealization から Classifier への関連（単方向）。
  * 関連端 ``realizingClassifier`` の多重度は ``1..*`` である。
  * A_clientDependency_client を subsets する（向き注意）。

11.6.3 Semantics
----------------------------------------------------------------------
11.6.3.1 Components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Component はそれの中身をカプセル化するシステムのモジュール式部品を表現するものであり、
  それの現れるものがその環境の内部で取り替えることができるようなものである。

* Component はいくらかの Classifiers の状態と振る舞いをカプセル化する
  自給自足な構成単位である。

  * Component は
    それのクライアントに与えるのと、
    システムにある他の Components やサービスを必要とするものとの、
    サービスの正式な契約を
    それの ``provided`` および ``required`` Interfaces に関して指定する。

* Component は、
  それの Interfaces の互換性に基づいて等価な機能がある Component により、
  設計時または稼働時に置換可能な構成単位である。

* Component は開発のライフサイクルで終始モデル化されて、
  配置時と稼働時に向けて逐次洗練される。

  * Component は一つまたはそれを超える Artifacts によって具現化されてよく、
    そして次に、その Artifact が実行環境に配備されてよい。
    DeploymentSpecification でその Component の実行を引数にする
    値を定義してよい。
    :doc:`./deployments` 参照。

* Component の ``required`` および ``provided`` Interfaces は
  Operations や Receptions のような BehavioralFeatures だけではなく、
  ``attributes`` や Association 端のような StructuralFeatures の
  仕様も考慮に入れる。

  * Component は ``provided`` Interface を直接実装してもよいし、
    その実現 Classifiers がそうしてもよいし、
    それらが継承されてもよい。

  * ``required`` および ``provided`` Interfaces は
    Ports で任意で組織化されてよい。

* Component は
  それの公的に視認できる Properties と Operations によって
  external view すなわち black-box view を持つ。

* システムまたはその他の状況での Components 間の配線 (wiring) は
  互換性のある単純 Ports 間または、
  Usages と Component 図の Components にあるソケットとロリポップにより
  表される匹敵する InterfaceRealizations との間にある
  Dependencies を用いて構造的に定義することが可能である。

* Component は
  その非公開な Properties と実現 Classifiers によって
  internal view すなわち white-box view を持つ。

* Component にある assembly Connector にとっての実行時の意味とは、
  Connector のオブジェクトに沿って巡回する要求
  （シグナルと操作発動）である。

* Component に適用する UML 標準ステレオタイプがいくつかある。
  例えば巨大な規模の Components をモデル化する «Subsystem» や、
  異なった仕様と実現化の定義で Components をモデル化するには
  «Specification» と «Realization» 等がある。
  ここで、仕様ひとつは複数の実現化を持つことが許される。
  :doc:`./standard-profile` 参照。

* Component はいくらかの Classifiers によって実現（または実装）されてよい。
  その場合、Component はこれらの Classifiers に対する
  ComponentRealizations の集合を所有する。

* Component はその定義に必要とされるか、関係するモデル要素全部に対しては
  Package のように振る舞うが、
  それは所有されているか明示的にインポートされているかの
  どちらかであるはずである。

* ``isIndirectlyInstantiated`` 特性は
  Component に対して適用するオブジェクト化の種類を示す。

  * false であると、Component は addressable オブジェクトとして
    オブジェクト化される。

  * true であると、Component は設計時には定義されるが、
    稼働時（または実行時）には Component により指定されるオブジェクトは
    存在しない。
    すなわち、
    Component は間接的にオブジェクト化されて、
    それの実現する Classifiers または ``parts`` のオブジェクト化の終わりまで。

11.6.4 Notation
----------------------------------------------------------------------
* Component はキーワード «component» を付した Classifier 矩形として示す。

  * 任意で Component アイコン（二つの小四角形が突き出た四角形）
    を右上隅に展示することが可能。この場合はキーワードが非表示でもよい。

* 属性、操作、内部構造区画はすべて通常の意味を持つ。

* Component の ``provided`` および ``required`` Interfaces は
  ボール（ロリポップ）・ソケット記法で示してよい。
  ここでは、ロリポップとソケットは Component の矩形の外に突き出る。

* Component の ``provided`` および ``required`` Interfaces の
  フルネームを表示するために、
  Interfaces は通常の伸張可能な Classifier 矩形として表示することも可能である。
  このオプションを使うときには、
  適切な依存矢印により Interface 矩形を Component 矩形に対して接続する。

  * :doc:`./common-structure` や :doc:`./simple-classifiers` を参照。

* 準拠ツールは任意で "provided interfaces" と "required interfaces" という名前の、
  ``provided`` および ``required`` Interfaces を名前で列記する
  区画を支援してもよい。

* さらなる任意の区画 "realizations" および "artifacts" を
  実現する Classifiers および
  具現化する Artifacts を列記するのに用いてよい。

* ComponentRealization は Realization 依存と同じ方法で記される。
  すなわち矢先が白抜き三角である一般的な破線矢印である。

* Component の ``packagedElements`` は、
  :doc:`./classification` で取り扱った
  ``ownedMembers`` のオプション区画についての仕様に従って、
  オプション区画 "packaged elements" に表示してよい。

11.6.5 Examples
----------------------------------------------------------------------
* Figure 11.39 Example of an overview diagram (...)

  * Order は Account と Product に依存しているが、
    依存の種類は特記されていない。

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

  * Dependency 記法を用いて ``provided`` と ``required`` Interfaces を明示的に表現している。
  * 矢印の描き分け方に注意。

* Figure 11.44 A representation of the realization of a complex Component

  * この図式全体が ComponentRealizations を示している。
  * 下側の Classifiers の集合が Component Customer を実現している。

* Figure 11.45 An alternative nested representation of a complex Component

  * 選択自由の区画 "packaged elements" の記法例。
  * OrderHeader と LineItem は区画 "realizations" でリストされるものと同じ。

* Figure 11.46 Example model of a Component, its provided and required Interfaces, (...)

  * Components 間の配線。込み入った図式。
  * /OrderableItem は Product の上位型が実装する Interface であることを示す。
  * Component は AccountPayable が OrderHeader に依存していることを要求している。

* Figure 11.47 Internal structure of a Component

  * Component の内部構造の white-box view の見本。
  * 区画 "internal structure" に他の Components がいる。
  * 単純 Ports に ball and socket 記法が連結している。

* Figure 11.48 Delegation Connectors connect externally provided Interfaces to the parts (...)

  * この例では区画 "internal structure" にある ``parts`` は、
    区画 "packaged elements" にある Classes を型とする。

11.7 Collaborations
======================================================================

11.7.1 Summary
----------------------------------------------------------------------
* Collaborations の第一の目的とは、
  通信要素のシステムがどのように特定の課題または課題の集合を併せて達成するかを
  説明と無関係である詳細と結び付く必要性なしに説明することである。

* CollaborationUse はそれの ``collaborationRoles`` を演じる
  特定の要素を巻き込む特定の状況への、
  Collaboration によって記述されるパターンの応用を表現する。

11.7.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 11.49 Collaborations

  * Collaboration と CollaborationUse を見ていく。

A_collaborationRole_collaboration
  * Collaboration から ConnectableElement への関連（単方向）。
  * A_role_structuredClassifier を subsets する。

A_type_collaborationUse
  * CollaborationUse から Collaboration への関連（単方向）
  * 関連端 ``type`` はこの CollaborationUse で使われている Collaboration である。
  * 関連端 ``type`` の多重度は 1 である。

A_roleBinding_collaborationUse
  * CollaborationUse から Dependency への composite 関連（単方向）。
  * A_ownedElement_owner を subsets する。

A_collaborationUse_classifier
  * Classifier から CollaborationUse への composite 関連（単方向）。
  * A_ownedElement_owner を subsets する。

A_representation_classifier
  * Classifier から CollaborationUse への関連（単方向）。
  * A_collaborationUse_classifier を subsets する。

11.7.3 Semantics
----------------------------------------------------------------------
11.7.3.1 Collaborations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Collaboration は協調しているオブジェクト群が、
  ある共同の課題や課題の集合を、
  どのように果たすのかを説明するのに用いてよい。

* Collaboration は与えられた課題をこなすのに必要とされる
  共同の参加者の集合を定義する。

* Features 全部も、参加オブジェクトの内容全部も、
  これらのオブジェクトの間にあるリンク全部もいずれも
  特定の Collaboration に常には必要とされない。
  それゆえ Collaboration は Interfaces で型付けられた
  ``collaborationRoles`` によって定義されることがよくある。

* Collaborations は他の Collaborations から特殊化されてよい。

* Collaboration は直接オブジェクト化可能なものではない。

11.7.3.2 CollaborationUses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* CollaborationUse は要素の集合間の関係の説明になる
  Collaboration の特定の利用法を表現する。

* ``roleBinding`` は CollaborationUse が所有する Dependencies を
  使って実装される。

* CollaborationUse を型とする Collaboration にある Connectors は
  対応する Connectors が
  context Classifier に束縛された要素の間にある必要があり、
  これらの対応する Connectors は Collaboration Connectors と
  同じか、より一般の型とする必要がある。

* Classifier が所有する CollaborationUses のうちのひとつを
  総括して Classifier の Behavior を代表するものとして選び出してよい。
  これを Classifier の ``representation`` と呼ぶ。

* Collaboration に取り付けられた Behavior のどれもが
  ``collaborationRoles`` の集合および
  与えられた CollaborationUses で束縛された Connectors に適用する。
  例えば、Collaboration の ``parts`` の間の相互作用は
  単一の CollaborationUse に束縛された Classifier ``parts`` に適用する。

* 同じ ConnectableElement が Collaboration と代表された要素の両方で
  使われると ``roleBinding`` はひとつも要らない。

* ``roleBindings`` の顧客要素と仕入先要素が互換ならば、
  それ以上のことは指定されない。

11.7.4 Notation
----------------------------------------------------------------------
* Collaboration はその名前を含む破線の楕円形で示す。

  * ``collaborationRoles`` と Connectors で構成された
    Collaboration の内部構造を破線楕円内の区画に示してよい。
    この区画は Classifier の内部構造区画と同じ記法仕様に準じる。

* 代わりに composite structure 図が使える。
  あるいは通常の Classifier 矩形をキーワード «collaboration» を付けて使える。

* Properties でない ``collaborationRoles`` を持つ
  Collaboration を表す記法は定義されていない。

* Properties を表す代替表記法を使う場合は、
  楕円形の Collaboration の形から
  Collaboration の Properties の型である Classifiers の記号である矩形へ
  直線を引いてよい。

* CollaborationUse は背景となる Classifier の内部構造区画内部に
  その出来事の名前を含む破線楕円、コロン、
  それに Collaboration ``type`` で示す。

  * ``roleBinding`` ごとに対して、楕円からその ``client`` 要素へ破線がある。
    対して、破線は ``client`` 端上 ``supplier`` 要素の名前でラベルされている。

* CollaborationUse を表す選択自由な記法は、
  破線矢印がキーワード «occurrence» の付いた、
  使う Classifier から使われる Collaboration へ向くようにする。

  * これと共に ``roleBindings`` は普通の Dependency 矢印として示される。

11.7.5 Examples
----------------------------------------------------------------------
* Figure 11.50 The internal structure of the Observer Collaboration

  * 破線楕円全体が Collaboration Observer である。
  * 区画内にある矩形がこの ``collaborationRoles`` であり、
    オブジェクトの名前が示してある。
  * オブジェクト間の実線が Connector を示す。

* Figure 11.51 Alternative notation for the parts of the Observer Collaboration.

  * 先のものとは異なる記法を適用している。詳細な仕様が認められる。

* Figure 11.52 The Sale Collaboration

  * Sale は ``collaborationRoles`` buyer と seller の間の Collaboration である。

* Figure 11.53 The BrokeredSale Collaboration

  * BrokeredSale は 3 つの ``collaborationRoles`` (producer, broker, consumer) の間の Collaboration である。
  * 同時に 2 種類の CollaborationUses (wholesale, retail) を含むことを示している。
    broker だけは両方の CollaborationUses が ``client`` 要素として共有する。

* Figure 11.54 A subset of the BrokeredSale Collaboration using «occurrence» and Dependency arrows

  * わかりにくくなった。

11.8 Classifier Descriptions
======================================================================
機械生成による節。

11.9 Association Descriptions
======================================================================
機械生成による節。

.. include:: /_include/uml-refs.txt
