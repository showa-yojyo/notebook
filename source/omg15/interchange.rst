======================================================================
Annex B: UML Diagram Interchange
======================================================================
UML 2.5 pp. 685-742 に関するノート。

.. contents:: ノート目次
   :depth: 2

B.1 Summary
======================================================================
* この付録は、
  設計者が支配力を持つ UML モデルの、
  例えば図表上の形状の位置と点々の道筋を決める線のような、
  純粋に図表的な外観の交換 (UML DI) を可能にする。

* UML DI は Diagram Definition (DD_) に基づくものであり、
  とりわけその中の Diagram Interchange (DI) と
  Diagram Common (DC) パッケージに基づく。

* Figure B.1 UML Diagram Interchange Architecture

  * UML DI は DI からクラスと関連を特殊化し、
    UML 抽象構文の要素を参照することで、
    それらの要素の図式交換を指定する。

  * 図の左下にある UML の抽象構文による UseCase オブジェクトを
    UML DI の UMLShape のオブジェクトが参照している。
    この ``shape`` は図式上における図表の位置と含むラベル ``label`` を指定する。

* UML 準拠ツールは MOF 等価な意味のあるステレオタイプの適用および
  XMI 直列化 (serialization) を与えるものとする。

* UML DI 要素のオブジェクトを含んでいる交換ファイルの受信者は
  UML で指定されたとおりにオブジェクトを視覚的に表現 (render) する。

  * ほとんどの場合、描画は UML DI オブジェクトが与える位置と大きさ、
    参照されている UML 抽象構文のオブジェクトおよび
    UML における表記法の仕様しか使わずに決定されることが可能である。

  * UML が同じ抽象構文を意味する複数の表記法を与える場合には、
    UML DI はどの表記法が用いられる必要があるのかを指示する追加情報を含む。

B.2 Generic
======================================================================

B.2.1 Summary
----------------------------------------------------------------------
* UML DI の Generic 部分は複数の種類の UML 図式に共通な図表の外観を捕捉する。

B.2.2 UML Diagrams and Diagram Elements
----------------------------------------------------------------------
* Figure B.2 UML Diagrams and Diagram Elements

  * ``DI::`` のついているメタクラスについては、
    前述の別仕様書を参照すれば詳細はわかる。

  * DI::Diagram と DI::DiagramElement を
    UMLDiagram と UMLDiagramElement それぞれに特殊化してある。

* UMLDiagramElement は UML DI を表現するためのもっとも一般的なクラスである。

  * UMLDiagramElement は DI::DiagramElement::modelElement を再定義することで、
    UMLDiagramElements が他の言語要素ではなく
    UML 要素の表記法であるように限定する。

  * UMLDiagramElement は DI::DiagramElement::ownedElement を再定義することで、
    UMLDiagramElements が UMLDiagramElements だけを所有し、
    かつ整列される（図表要素の z-ordering に影響する）ように限定する。

  * UMLDiagramElement::isIcon は modelElements に対して、
    矩形ではなく幾何的な形状を用いて見せるオプションであるか、
    線を先が開いた実線矢印ではなく、線で見せるオプションである。

    * UMLShapes は同時に両方の表記法を用いてよい。
      交換時には同じ modelElement を持つふたつの
      UMLShapes になる。

* UMLDiagramElement に関して注意することをいくつか挙げる。

  * UMLDiagramElement::ownedElements の bounds は
    owningElements の bounds と共通部分を持たなくてよい。

  * UMLDiagramElement::ownedElements の modelElements は
    owningElements の modelElements とは異なる owners を持ってよい。

* UMLDiagram は UML 図式を表すためのもっとも一般的なクラスであり、
  当付録で定義された図式分類の根底である。

  * UMLDiagram は Packages による所有権を表すために
    PackageableElement から特殊化されている。

  * UMLDiagram::isFrame は図式の枠を見せる必要があるかどうかを指示する。
  * UMLDiagram::isISO は ISO 表記法規則に準じる必要があるかどうかを指示する。
  * UMLDiagram::isInheritedLighter は継承要素を
    明るい色で見せる必要があるかどうかを指示する。

B.2.3 UML Shapes and Edges
----------------------------------------------------------------------
* Figure B.3 UML Shapes and Edges

  * DI::Shape と DI::Edge を UMLShape と UMLEdge にそれぞれ特殊化することで、
    それらを具象型にし、継承された特性を再定義する。

* UMLShape は線として表現されることが全くない UMLDiagramElements を表すための
  最も一般的なクラスである。

  * UMLLabels ではないし、modelElements を持たないし、
    ただひとつの ownedElement として単独の UMLLabel に
    少なくともひとつの modelElement があるような UMLShapes は、
    必ず註釈記号として描画されるものとする。
    そのような UMLShapes と他の UMLDiagramElements とを接続する
    UMLEdges は必ず破線を用いて描画されるものとする。

  * ふたつを超える端点を持つ Dependency を示す矢印 (pl.) は
    modelElement として Dependency を持ち、かつ
    modelElement として Dependency を持つ UMLShape を持つ
    source または target の一方を持つ UMLEdges として交換される。

* UMLEdge は常に線として描画される UMLDiagramElements を表すための
  最も一般的なクラスである。
  DI::Edge から継承した source と target を再定義して、
  UMLEdges が UMLDiagramElements 同士をリンクするように限定する。

B.2.4 Labels
----------------------------------------------------------------------
* Figure B.4 Labels

  * UMLShape を文字列としてしか描画されてはならない形状を表すための
    最も一般的なクラス (UMLLabel) に特殊化する。
    そして UMLLabel を数種の UMLDiagrams で用いられる
    さまざまな種類のラベルに特殊化する。

* UMLLabels のすべては少なくともひとつは modelElement を持つものする。
  ただし UMLLabel にしか分類されず、
  その特殊化のいずれでもないようなものは除く。

* UMLLabel の特殊化は modelElement Property の type が定義する
  modelElements の部分部分に関する情報を示す目的がある。
  例えば、UMLNameLabel::modelElement は NamedElements に限定される。
  これらは name と visibility を表す Properties を持ち、
  かつ UMLNameLabel が示す modelElement の部分となる。

* UMLNameLabels は NamedElements についての情報を示す目的があり、
  常に name または namedExpression または
  NamedElement がインポートされたときは ElementImport alias を含む。
  また、ラベルはパッケージの containment（限定名）と可視性を含んでもよい。

* UMLKeywordLabels は ``«`` と ``»`` に挟まれる、
  UML が仕様化した文言と句読点を用いる
  modelElements に関するさまざまな種類の情報を示す目的がある。

* UMLTypedElementLabel は
  ちょうどひとつの Slot, InstanceSpecification, InstanceValue, 
  または TypedElement や Connector といった type のある要素についての
  名前、型、役割の情報を示すものである。

* UMLRedefinesLabel はちょうどひとつの RedefinableElement についての
  情報を示すものであり、redefinedElement の name を含んでよい。

B.2.5 Compartmentable Shapes
----------------------------------------------------------------------
* Figure B.5 UML Compartmentable Shapes

  * UMLDiagramElement と UMLShape を
    UMLCompartmentableShape と UMLCompartment にそれぞれ特殊化して、
    隔離された内容を持つ形状を表すために、
    具象型とし、特性を追加し、継承された特性を再定義する。

* UMLCompartmentableShape はその形状の内部にある
  隔離された部分に情報を示すことを許す UML 要素を表す最も一般的なクラスであり、
  いつも線形に配列されて、実線により分離されるものである。

* 区画のコマは
  modelElements を持たない UMLLabels として交換可能であるものとし、
  かつ UMLCompartments の orderedElement の最初のものとして
  交換可能であるものとする。

B.2.6 Stereotype Applications
----------------------------------------------------------------------
* Figure B.6 Stereotype Application Labels

  * UMLLabel を UMLStereotypePropertyValueLabel に特殊化することで、
    UML 抽象構文要素に適用する
    Stereotypes の Property の値を示すための関連を導入する。

* UMLStereotypePropertyValueLabels は Stereotypes の attributes を
  modelElements として持ち、Stereotype が適用される Element を与える。

* Stereotype 適用の交換に関する他の注意点を挙げる。

  * UML 抽象構文要素に適用される Stereotypes はテキスト的に示しても
    図表的に示してもよい。

  * 次の条件を満たす UMLShapes は icon として描画されるものとする。
    適用されている Stereotypes がないときにはどのような描画アイコンも
    この場合は描画されない。

    * modelElement がちょうどひとつの Stereotype が適用されていて
      icon の値を持つ
    * isIcon の値が ``true`` である
    * isIcon の値が ``false`` であるときに矩形で描画される

  * 次の条件を満たす UMLShapes は Stereotype icon として描画されるものとする。

    * Stereotype を icon を表す値を持つ modelElement として持つ
    * modelElement に Stereotype が適用された modelElements を持つ
      UMLDiagramElements の ownedElements である
    * isIcon の値が ``true`` である

B.2.7 UML Styles
----------------------------------------------------------------------
* Figure B.7 UML Styles

  * DI::Style を UML におけるスタイルを表す最も一般的なクラス
    UMLStyle へと特殊化することで、それを具象型にし、特性を追加し、
    UMLDiagramElement の継承されたスタイルに関係する特性を再定義する。

* UMLStyle は UMLDiagramElements を描画するのに利用されるフォントの
  名前およびサイズを指定する特性を導入する。

  * UMLStyle::fontSize はポイント単位で与えられる。

B.3 Structure
======================================================================
.. todo:: ノート作成

B.3.1 Summary
----------------------------------------------------------------------

B.3.2 Structure Diagrams
----------------------------------------------------------------------
* Figure B.8 Structure Diagrams

B.3.3 Classifier Shapes
----------------------------------------------------------------------
* Figure B.9 Classifier Shapes

B.3.4 Multiplicity and Association End Labels
----------------------------------------------------------------------
* Figure B.10 Multiplicity and Association End Labels

B.3.5 Association, Connector, and Link Shapes
----------------------------------------------------------------------
* Figure B.11 Association, Connector, and Link Shapes

B.4 Behavior
======================================================================
.. todo:: ノート作成

B.4.1 Summary
----------------------------------------------------------------------

B.4.2 Behavior Diagrams
----------------------------------------------------------------------
* Figure B.12 Behavior Diagrams

B.4.3 Activity Diagram Labels
----------------------------------------------------------------------

B.4.4 State Shapes
----------------------------------------------------------------------
* Figure B.13 State Shapes

B.4.5 Interaction Tables
----------------------------------------------------------------------
* Figure B.14 Interaction Shapes

B.5 Information Flows
======================================================================
.. todo:: ノート作成

B.6 UML Notations and UML DI Representations
======================================================================
.. todo:: ノート作成

* Table B.1 UML Shapes
* Table B.2 UML Edges

B.7 Classifier Descriptions
======================================================================
機械生成による節。

.. B.7.1 UMLActivityDiagram [Class]
.. B.7.2 UMLAssociationEndLabel [Class]
.. B.7.3 UMLAssociationOrConnectorOrLinkShape [Class]
.. B.7.4 UMLAssociationOrConnectorOrLinkShapeKind [Enumeration]
.. B.7.5 UMLBehaviorDiagram [Abstract Class]
.. B.7.6 UMLClassDiagram [Class]
.. B.7.7 UMLClassifierShape [Class]
.. B.7.8 UMLCompartment [Class]
.. B.7.9 UMLCompartmentableShape [Class]
.. B.7.10 UMLComponentDiagram [Class]
.. B.7.11 UMLCompositeStructureDiagram [Class]
.. B.7.12 UMLDeploymentDiagram [Class]
.. B.7.13 UMLDiagram [Abstract Class]
.. B.7.14 UMLDiagramElement [Abstract Class]
.. B.7.15 UMLDiagramWithAssociations [Abstract Class]
.. B.7.16 UMLEdge [Class]
.. B.7.17 UMLInteractionDiagram [Class]
.. B.7.18 UMLInteractionDiagramKind [Enumeration]
.. B.7.19 UMLInteractionTableLabel [Class]
.. B.7.20 UMLInteractionTableLabelKind [Enumeration]
.. B.7.21 UMLKeywordLabel [Class]
.. B.7.22 UMLLabel [Class]
.. B.7.23 UMLMultiplicityLabel [Class]
.. B.7.24 UMLNameLabel [Class]
.. B.7.25 UMLNavigabilityNotationKind [Enumeration]
.. B.7.26 UMLObjectDiagram [Class]
.. B.7.27 UMLPackageDiagram [Class]
.. B.7.28 UMLProfileDiagram [Class]
.. B.7.29 UMLRedefinesLabel [Class]
.. B.7.29 UMLRedefinesLabel [Class]
.. B.7.30 UMLShape [Class]
.. B.7.31 UMLStateMachineDiagram [Class]
.. B.7.32 UMLStateShape [Class]
.. B.7.33 UMLStereotypePropertyValueLabel [Class]
.. B.7.34 UMLStructureDiagram [Abstract Class]
.. B.7.35 UMLStyle [Class]
.. B.7.36 UMLTypedElementLabel [Class]

B.8 Association Descriptions
======================================================================
機械生成による節。

.. B.8.1 A_UMLActivityDiagram_modelElement_umlDiagramElement [Association]
.. B.8.2 A_UMLAssociationEndLabel_modelElement_umlDiagramElement [Association]
.. B.8.3 A_UMLBehaviorDiagram_modelElement_umlDiagramElement [Association]
.. B.8.4 A_UMLClassifierShape_modelElement_umlDiagramElement [Association]
.. B.8.5 A_UMLCompartment_elementInCompartment_owningCompartment [Association]
.. B.8.6 A_UMLCompartmentableShape_compartmentedShape_shape [Association]
.. B.8.7 A_UMLDiagramElement_localStyle_styledElement [Association]
.. B.8.8 A_UMLDiagramElement_modelElement_umlDiagramElement [Association]
.. B.8.9 A_UMLDiagramElement_ownedElement_owningElement [Association]
.. B.8.10 A_UMLDiagramElement_sharedStyle_styledElement [Association]
.. B.8.11 A_UMLDiagram_heading_headedDiagram [Association]
.. B.8.12 A_UMLEdge_source_sourceEdge [Association]
.. B.8.13 A_UMLEdge_target_targetEdge [Association]
.. B.8.14 A_UMLInteractionDiagram_modelElement_umlDiagramElement [Association]
.. B.8.15 A_UMLMultiplicityElement_modelElement_umlDiagramElement [Association]
.. B.8.16 A_UMLNameLabel_modelElement_umlDiagramElement [Association]
.. B.8.17 A_UMLRedefines_modelElement_umlDiagramElement [Association]
.. B.8.18 A_UMLStateMachine_modelElement_umlDiagramElement [Association]
.. B.8.19 A_UMLStateShape_modelElement_umlDiagramElement [Association]
.. B.8.20 A_UMLStereotypePropertyValueLabel_modelElement_umlDiagramElement [Association]
.. B.8.21 A_UMLStereotypePropertyValueLabel_stereotypedElement_labelShowingStereotypeValue [Association]

.. include:: /_include/uml-refs.txt
