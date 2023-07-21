======================================================================
20 InformationFlows
======================================================================

.. contents::
   :depth: 3

20.1 Information Flows
======================================================================

20.1.1 Summary
----------------------------------------------------------------------

InformationFlows パッケージはシステム実体の間の情報の交換を高水準の抽象度で支
援する。

   InformationFlows may be useful during top-down model development,
   representing aspects of models not yet fully specified, and for recording
   less detailed, heuristic representations of more complex model areas.

InformationFlows は巨大であったり複雑であったりするモデルの意図を明確にしたり、
全体的な理解を文書にするのに有用だ。

InformationFlows はシステムを通じた情報の回覧を一般的な手法で記述する。情報の性
質、伝達の仕掛け、交換の順序、制御条件などは規定しない。

   During more detailed modeling, representation and realization links may be
   added to specify which model elements implement an InformationFlow and to
   show how information is conveyed.

同様に InformationItems は実現の詳細が設計前であっても、InformationFlows に沿っ
て流れる情報を表現するのに用いることが可能だ。

20.1.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 20.1 Information Flows

InformationFlow は PackageableElement と DirectedRelationship の特殊化だ。関連す
る型がかなり多くある。

* Classifier (``conveyed``)
* Relationship (``realization``)
* NamedElement (``informationSource``, ``informationTarget``)
* Connector (``realizingConnector``)
* ActivityEdge (``realizingActivityEdge``)
* Message (``realizingMessage``)

InformationItem は Classifier の特殊化だ。

InformationItem は InformationItem (``represented``) に関連する。

20.1.3 Semantics
----------------------------------------------------------------------

InformationFlows は情報品目を一方通行で伝送するべく、ある種の情報経路を必要とす
る。これらは情報経路の実現を指定し、そこを沿って流れる情報を識別する。この経路に
沿って移動する情報を、抽象 InformationItems や具象 Classifiers で表現してもよ
い。

   The sources and targets of an InformationFlow designate sets of objects that
   can send (sources) or receive (targets) conveyed InformationItems or
   Classifiers.

Fig. 20.1 では sources と targets は NamedElements として見えている。

実践では InformationFlow の制約により、sources と targets は次の型のいずれかで
あることが必要だ：

* Actor
* Node
* UseCase
* Artifact
* Class
* Component
* Port
* Property
* Interface
* Package
* ActivityNode
* ActivityPartition
* Behavior
* InstanceSpecification

さらに、source か target が InstanceSpecification の場合には、それがリンクである
ことは不可能だ。InstanceSpecification を Relationship により分類することは許され
ない。

   An InformationFlow’s sources and targets represent all potential instances
   typed or contained (i.e., owned) by them.

例えば、``source`` または ``target`` が

* Classifier である場合、それはその Classifier の潜在的オブジェクトすべてを表現
  する。
* Part である場合、その Part によって指定された役割を果たすことが可能であるオブ
  ジェクトすべてを表現する。
* Package である場合、その Package に含まれる直接または間接的に所属する
  Classifiers の潜在的オブジェクトすべてを表現する。

情報経路は sources と targets の性質に応じて、さまざまな方法で実現可能だ。
Relationships, Connectors, ActivityEdges, Messages により実現可能だ。

   The types of sources and targets must be compatible with the types of
   information that flow along the information channel.

例えば source と target が Collaboration などの複合構造の部分である場合、その情
報経路は Connector で表現されがちだ。

   Multiple sources and targets are allowed, but they must have compatible
   types.

InformationFlows は sources から targets に流れる InformationItems を識別する
が、Class などの具象 Classifiers も伝達されることがある。

InformationItems は ``sources`` から ``targets`` にたいへん抽象的な方法で移動す
ることが可能な多くの種類の情報を表現する。しかし転送される情報の詳細については
elaborate しない。

   InformationItems cannot be instantiated and do not themselves have features,
   generalizations, or associations. In this respect, InformationItems are
   similar to Interfaces -- a constraint in the metamodel enforces the inability
   to instantiate them.

InformationItems の重要な用途に、おそらくは最終的にそれらを定義する詳細なモデリ
ングの決定がなされる以前の、設計初期段階で情報を表現するというものだ。もう一つの
目的は、複雑なモデルの一部を、正確さはやや損なうが、もっと一般的で伝達可能な方法
で抽象化することだ。

   InformationItems may be decomposed into more specific InformationItems or
   Classifiers. Representation links between them express the idea that, in the
   context a particular InformationFlow, specific information is exchanged.

InformationItems は Classes の全種類、Interfaces, Signals, その他の
InformationItems によってしか実現化されることはない。

   The principal goal of InformationFlows is to convey that information moves
   from one area of a model to another.

メタモデルは情報経路の実現と、そこを移動する情報の型に対して寛容だ。
InformationFlows は複数の型の情報経路によって同時に実現することが可能であり、多
様な Classifiers を表現することが可能だ。

20.1.4 Notation
----------------------------------------------------------------------

InformationFlow は Dependency と同じ記法を用いて表現されるが、キーワード
``«flow»`` を破線に添えておく。

InformationItems の表現はそれらが表示される周辺状況により決定される。

* InformationFlow の ``«flow»`` 破線に取り付けられると、InformationItem の名前が
  適切な ``«flow»`` 線の近くに表示される。
* InformationItems はそれらが Classifiers であるゆえ、InformationFlows から独立
  して表示する場合、矩形内部に名前が現れる。この矩形をキーワード
  ``«information»`` か黒塗りの二等辺三角形で修飾する。InformationItem 矩形は属性
  も操作もないので、目に見える部分区画がない。
* InformationFlow の情報経路の実現化に取り付けられると、この情報経路上の黒塗り二
  等辺三角形が情報の移動方向を指す。

     The InformationItem’s name is placed close to the triangle. When
     representing several InformationItems having the same direction, only one
     triangle is shown, with a nearby list of InformationItem names separated by
     commas.

* ある InformationItem が他の InformationItems や Classifiers を表す場合、それら
  はキーワード ``«representation»`` が添えられた破線矢印で接続される。

20.1.5 Examples
----------------------------------------------------------------------

   Figure 20.2 Example of InformationFlows conveying InformationItems

* ``Company`` から ``Customer`` へ一方的に ``product`` が流れていく。
* ``Company`` から ``Employee`` へ一方的に ``wage`` が流れていく。

   Figure 20.3 Information Item represented as a classifier

独立した InformationItem の表記例。どちらの ``wage`` も同じ InformationItem を意
味する。この手の黒塗り三角形は単に矩形を InformationItem として識別するだけで、
方向の意味はない。

   Figure 20.4 Examples of ``«representation»`` notation

左図では ``travel document`` は ``passport`` と ``plane ticket`` の両方を表して
いる。右図では ``Wage`` は具象クラス ``Salary`` と ``Bonus`` の両方の「代役」と
して振る舞う。

   Figure 20.5 InformationItems attached to Connectors

   When InformationItems are displayed on an information channel realizing an
   InformationFlow, triangles indicate the directional flow of information.

図の Connector 線上にある ``a``, ``b``, ``d`` 黒塗り三角が InformationItems だ。
``m1:myC1`` か ``m2:myC`` が InformationItems の source/target だ。

   Figure 20.6 InformationItems attached to Associations

InformationItems ``product`` と ``wage`` がそれぞれの InformationFlow の情報経路
を実現する Association に取り付けられている。

20.2 Classifier Descriptions
======================================================================

機械生成による節。

20.3 Association Descriptions
======================================================================

機械生成による節。

.. include:: /_include/uml-refs.txt
