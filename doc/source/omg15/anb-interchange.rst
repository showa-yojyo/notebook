======================================================================
Annex B: UML Diagram Interchange
======================================================================

.. contents::
   :depth: 3

B.1 Summary
======================================================================

この付録では、図表上の形状の位置や配線のような、設計者が支配する UML モデルの純
粋に図表的な一面の相互交換 (UML DI) を可能にする。

   This information must be interchanged between tools to reproduce UML diagrams
   reliably.

UML ツールは交換された図式情報と交換された抽象構文のオブジェクトとの間に与えられ
るリンクによって、UML のどの部分が交換されていない図表的一面を指定しているかを判
断することが可能だ。

UML DI は Diagram Definition (DD_), とりわけその Diagram Interchange (DI) と
Diagram Common (DC) パッケージに基づく。

   UML diagrams are interchanged by instantiating classes and associations in
   UML abstract syntax and in UML DI, then linking them together by reference.

   Figure B.1 UML Diagram Interchange Architecture

この図式では、左下に UML の抽象構文の UseCase のオブジェクト、そしてそれを参照す
る UML DI の UMLShape のオブジェクトが示されている。UMLShape のオブジェクトは図
式上の図像の位置と、それに含まれるラベルを指定する。

   Stereotypes can be based on elements of UML DI and applied to instances of
   those elements.

   Receivers of interchange files containing instances of UML DI elements
   *render* the instances visually as specified by UML.

ほとんどの場合、描画は UML DI オブジェクト、参照される UML 抽象構文のオブジェク
ト、および記法の UML 仕様によって与えられる位置と大きさしか使用せずに決定するこ
とが可能だ。

UML が同じ抽象構文に対して複数の記法を与えている場合、UML DI にはどの記法を用い
る必要があるのかを指示する追加情報が含まれる。

B.2 Generic
======================================================================

B.2.1 Summary
----------------------------------------------------------------------

UML DI の Generic 部分には複数の種類の UML 図式に共通する図表的外観が含まれる。

B.2.2 UML Diagrams and Diagram Elements
----------------------------------------------------------------------

   Figure B.2 UML Diagrams and Diagram Elements

DI の Diagram と DiagramElement を UMLDiagram と UMLDiagramElement それぞれに特
化して UMLDiagram を具象化し、特性と関連を加えて、継承特性を再定義する。

   UMLDiagramElement is the most general class for UML DI.

UMLDiagramElement は DI の DiagramElement から ``modelElement`` を再定義し、
UMLDiagramElements が他の言語要素ではなくUML 要素の記法であるように制限する。

UMLDiagramElement は DI の DiagramElement から ``ownedElement`` を再定義し、
UMLDiagramElements が UMLDiagramElements しか所有せず、かつ整列されるように制限
する（読者ノート：図表要素の z-ordering に影響するようだ）。

``isIcon`` は矩形以外の幾何学的図形で表示する選択肢のあるモデル要素や、鏃を開い
た実線以外の線で表示する選択肢のあるモデル要素のために導入されているものだ。

   A value of true for ``isIcon`` indicates the alternative notation shall be
   rendered.

UMLDiagramElement に関して注意すること：

* ``ownedElements`` はそれらの ``owningElements`` の ``bounds`` と交わらない
  ``bounds`` を有することがある。
* ``ownedElements`` の ``modelElements`` は ``owningElements`` の
  ``modelElements`` とは異なる ``owners`` を持つことがある。

..

   UMLDiagram is the most general class for UML diagrams, and is the root of the
   diagram taxonomy defined in this Annex (also see in Figure A.5 in :doc:`Annex
   A <./ana-diagrams>`).

* UMLDiagram は Packages による所有権を表すために PackageableElement から特殊化
  されている。
* ``isFrame`` は図式の枠を見せる必要があるかどうかを指示する。
* ``heading`` はその ``headedDiagram`` があれば、それと同じ ``modelElement`` を
  持たなければならない。
* ``isISO`` は ISO 表記法規則に準じる必要があるかどうかを指示する。
* ``isInheritedLighter`` は継承要素を薄い色で見せるかどうかを指示する。

B.2.3 UML Shapes and Edges
----------------------------------------------------------------------

   Figure B.3 UML Shapes and Edges

DI の Shape と Edge を UMLShape と UMLEdge にそれぞれ特殊化し、具象化して継承さ
れた特性を再定義する。

   UMLShape is the most general class for UMLDiagramElements that are never
   rendered as lines.

* UMLLabels ではなく、``modelElements`` がなく、少なくとも一つの
  ``modelElement`` がある単一の UMLLabel をただ一つの ``ownedElement`` とする
  UMLShapes は、註釈記号として描画されるものとする。
  このような UMLShapes と他の UMLDiagramElements とを接続する UMLEdges は破線を
  用いて描画されるものとする。
* 三つ以上の端子がある Dependency を示す矢印は、その Dependency を
  ``modelElement`` として持つ UMLEdges と、その Dependency を ``modelElement``
  として持つ UMLShapeである ``source`` または ``target`` のいずれかとして交換さ
  れる。

     If the ``bounds`` of the UMLShape give an area greater than zero, it shall
     be rendered as a dot, otherwise nothing is rendered for the UMLShape.

  Dpendency を註釈する UMLLabels はすべて UMLShapes が所有するものとする。

..

   UMLEdge is the most general class for UMLDiagramElements that are always
   rendered as lines.

DI の Edge ``source`` と ``target`` を再定義し、UMLDiagramElements をリンクする
UMLEdges を制限する。

B.2.4 Labels
----------------------------------------------------------------------

   Figure B.4 Labels

   The model in Figure B.4 specializes UMLShape into the most general class for
   shapes that shall be rendered only as character strings (UMLLabel), and
   specializes it into various kinds of labels used in multiple kinds of
   UMLDiagrams.

UMLLabel の特殊化により、交換ファイルの受領者は ``modelElements`` のどの部分が表
示されることを意図しているのか、どの部分が変更されたときに描画を更新することがで
きるかを判断できるようになる。

   Specializations of UMLLabel are introduced only when it is ambiguous or
   cumbersome to determine which portions of the ``modelElements`` are intended
   to be shown by parsing text as UML specifies.

文字列の多くは、UMLLabel の特殊化でない UMLLabal オブジェクトと交換される。

UMLLabels のすべては少なくとも一つの ``modelElement`` があるものとする。ただし
UMLLabel にしか分類されず、その特殊化のいずれでもないようなものは除く。

UMLLabel は、UMLDiagramElement の外側に配置される場合を含め、ラベルが貼られる
UMLDiagramElement がもしあればそれと同じ ``modelElements`` でなければならず、そ
の UMLDiagramElement の ``ownedElements`` でなければならない。

   All UMLLabels shall have values of false for ``isIcon``.

UMLLabels は、常に、描画されるテキストを指定するものとし、BNF がある場合にはそれ
を含め、``modelElement`` の各種類をラベル付けするための UML 仕様に準拠するものと
する。

   The specializations of UMLLabel are for showing information about the
   portions of their ``modelElements`` defined by the type of the
   ``modelElement`` Property.

UMLNameLabel の ``modelElement`` は ``name`` と ``visibility`` を表す Properties
を持つ NamedElements に限定される。

必要な情報をすべて表示する特化型がない場合には UMLLabel を直接使用する。

   UMLNameLabels are for showing information about NamedElements, which always
   includes their ``name``, or ``nameExpression``, or ElementImport ``alias`` if
   the NamedElement is imported, and may also include package containment
   (qualified names) and visibility.

..

   UMLKeywordLabels are for showing various kinds of information about
   modelElements using wording and punctuation specified by UML between
   guillemets (see :doc:`Annex C <./anc-keywords>`).

* UMLKeywords はちょうど一つの ``modelElement`` を持つものとする。
* ``text`` は、«» とキーワードのみを含むものとする。

..

   UMLTypedElementLabel is for showing name, type, and role information about
   exactly one Slot, InstanceSpecification, InstanceValue, or element with a
   ``type``, such as TypedElement or Connector.

UMLTypedElementLabels を交換することについて注意する点がある：

* ``modelElement`` が Slot の場合、その ``text`` には ``definingFeature`` の
  ``name``, ``definingFeature`` の ``type`` の ``name``, ``modelElement`` の
  ``value`` を含めることが許される。
* ``modelElement`` が InstanceSpecification または InstanceValue である場合、そ
  の ``text`` は

  * InstanceSpecification または
  * InstanceValue の ``instance``

  の ``name`` と、

  * InstanceSpecification の ``classifiers`` または
  * InstanceValue の ``instance``

  の ``names`` を含んでよい。
* ``modelElement`` が ``specification`` のある InstanceSpecification である場
  合、その ``text`` は ``specification`` を含んでよい。
* ``modelElement`` が StructuredClassifier を ``classifier`` として持つ
  InstanceSpecification の ``slot`` の ``value`` である InstanceValue であり、そ
  の UMLTypedElementLabel がその InstanceSpecification を ``modelElement`` とし
  て有する UMLCompositeStructureDiagram 内でその InstanceValue を
  ``modelElement`` としてある形で見えている場合、その ``text`` にはその
  UMLTypedElementLabel の ``modelElement`` である InstanceValue を所有する Slot
  の ``definingFeature`` である Property の ``name`` を含んでよい。
* TypedElements や Connectors のように ``modelElement`` に ``type`` がある場合、
  その ``text`` はその ``modelElement`` の ``name`` およびその ``modelElement``
  の ``type`` の ``name`` を含んでよい。

..

   UMLRedefinesLabel is for showing information about exactly one
   RedefinableElement, which may include the ``name`` of the
   ``redefinedElement``.

B.2.5 Compartmentable Shapes
----------------------------------------------------------------------

   Figure B.5 UML Compartmentable Shapes

UMLDiagramElement と UMLShape を UMLCompartmentableShape と UMLCompartment にそ
れぞれ特殊化し、それらを具象化、特性を追加し、隔離された内容を有する形状を表すた
めに、継承された特性を再定義する。

   UMLCompartmetableShape is the most general class for UML elements that may
   have information shown in separated portions inside their shapes, usually
   arranged linearly and separated by solid lines (*compartments*).

* UMLCompartment は UMLDiagramElement から ``ownownElement`` を subset
  し、UMLCompartment で表される、縦に並んで表示される区画を指定する。
* UMLCompartment は UMLDiagramElement の ``ownedElement`` を subset して、縦に並
  べられた区画の内容を指定する。
* UMLCompartment は ``modelElement`` を持たない。

区画の表題は ``modelElements`` がない UMLLabels として、また UMLCompartments の
最初の ``orderedElement`` として交換されなければならない。

B.2.6 Stereotype Applications
----------------------------------------------------------------------

   Figure B.6 Stereotype Application Labels

UMLLabel を UMLStereotypePropertyValueLabel に特殊化し、UML 抽象構文要素に適用す
る Stereotypes の Property の値を示す関連を導入する。

   UMLStereotypePropertyValueLabels have ``attributes`` of Stereotypes as
   ``modelElements``, and give the Element to which the Stereotype is applied.

UMLStereotypePropertyValueLabels は適用された Stereotypes の値を示す文字列とし
て、UML で規定された構文 (12.3.4) で描かれなければならない。

UMLStereotypePropertyValueLabels は次の ``ownedElements`` だ：

* ``modelElements`` を持たない UMLEdges の ``source`` または ``target`` である、
  ``modelElements`` を持たない UMLShape. この UMLEdges の他方の端子はその
  ``stereotypedElements`` である ``modelElements`` を持つ UMLShapes だ。
* すべての UMLStereotypePropertyValueLabels が次を持つ UMLCompartments:

  * その ``stereotypedElement`` としてこの UMLCompartment の ``ownningElement``
    の ``modelElement`` を持ち、かつ
  * その ``modelElements`` としてこの UMLCompartment の ``ownningElement`` の
    ``modelElement`` に適用する同じ Stereotype の Properties.

Stereotype 適用の交換に関する他の注意点：

* UML 抽象構文要素に適用する Stereotypes は：

  * テキストで示されることがあり、UML 抽象構文要素に適用されたステレオタイプは、
    設計者定義の Stereotypes を ``modelElement`` として持ち、その Stereotypes が
    適用された ``modelElement`` を持つ UMLDiagramElement の ``ownedElement`` で
    ある UMLLabels と交換される。
  * 設計者定義図像で示されることがあり、その図像は Stereotypes で指定され、UML
    DI ではなく UML 抽象構文で交換される。描画規則は (12.3.4) と後述で規定。

* 次の条件をすべて満たす UMLShapes は ``icon`` として描画されるものとす
  る。Stereotypesが適用されていないときには描画されるアイコンはこの場合は描画さ
  れない：

  * ``modelElement`` にちょうど一つの Stereotype が適用されていて ``icon`` に対
    する値があって、
  * ``isIcon`` に対する値が真であって、
  * ``isIcon`` に対する値が偽である場合に矩形で描画される。

* 次の条件を満たす UMLShapes は Stereotype ``icon`` として描画されるものとする：

  * Stereotype を ``icon`` に対する値のある ``modelElement`` として有して、
  * ``modelElement`` に Stereotype が適用された ``modelElements`` がある
    UMLDiagramElements の ``ownedElements`` であり、
  * ``isIcon`` に対する値が真。

  これらの UMLShapes は次のいずれかの場所で描画されるものとする：

  * ``isIcon`` の値が偽である UMLShapes のために描画される幾何的図形の内側。また
    は、
  * それらの ``owningElements`` である UMLEdges について描画された線の近く。
  * それらの ``owningElements`` である UMLLabels について描画された文字列の左
    側。

B.2.7 UML Styles
----------------------------------------------------------------------

   Figure B.7 UML Styles

DI Style を UML で最も一般的なスタイルクラス UMLStyle へ特化して具体化
し、UMLDiagramElement に継承されたスタイル関係の特性を再定義する。

   UMLStyle introduces properties to specify the name and size of fonts used in
   rendering UMLDiagramElements. The ``fontSize`` is given in typographical
   points.

B.3 Structure
======================================================================

B.3.1 Summary
----------------------------------------------------------------------

UML DI の Structure 部分は構造図の図表的な一面とその内容を表す。

B.3.2 Structure Diagrams
----------------------------------------------------------------------

   Figure B.8 Structure Diagrams

UMLStructureDiagrams はいずれも ``modelElements`` がないが、例外として
UMLCompositeStructureDiagrams はちょうど一つある。

UMLStructureDiagrams はすべて関連付けのための図表的オプション
UMLDiagramWithAssociations を持つ。

UMLDiagramWithAssociations 注意点：

* これらの図式では ``isAssociationDotShow`` で指されるように、関連を表すのにドッ
  ト記法を用いても用いなくてもよい。これらの図式は ``navigabilityNotation`` と
  ``nonnavigabilityNotation`` でそれぞれ指されるように、常に（開いた鏃の矢印で）
  航路を示すことも、一方向の関連のみ示すことも、（バツジルシで）決して示さなくて
  もよい。
* ``navigabilityNotation`` と ``nonnavigabilityNotation`` で決定される回航可能記
  法は ``modelElements`` として Associations を持つ UMLEdges や ``classifier``
  として Associations を持つ InstanceSpecifications や Properties や Slots に適
  用する。
* 関連線の間の Generalization の矢印は Generalizations を ``modelElements`` とす
  る UMLEdges として交換され、Associations を ``modelElements`` とする UMLEdges
  である ``sources`` と ``targets`` は交換される。
* GeneralizationSets を示す破線は GeneralizationSets を ``modelElements`` とする
  UMLShapes として交換される。
* 修飾された Association ``memberEnds`` 記法は、その ``memberEnd`` を
  ``modelElement`` とする UMLShapes, Association を ``modelElement`` とする
  UMLEdges が所有する UMLShapes, ``qualifiers`` (UMLProperty) を
  ``modelElements`` とする UMLLabels が所有する UMLShapes として交換される。
* ``modelElements`` として InstanceSpecifications があり、リンクを示すことを目的
  とした UMLShapes 間の UMLEdges は、``modelElements`` として
  InstanceSpecifications を持ち、``classifier`` としてリンクを分類する
  Association を持つ。その Association ``memberEnds`` の ``names`` を示す
  UMLLabels は Slot を ``modelElemets`` として持つ。

UMLStructureDiagrams 注意点：

* 線で示される Properties または Slots は、Properties または Slots が
  ``modelElements`` である UMLEdges とそれぞれ交換される。
* Packages を ``modelElements`` として持つ UMLShape で、その内側に UMLShapes が
  描画されていない場合、Package の ``name`` はタブではなく、大きい方の矩形に示
  す。そうでない場合はタブに示す。キーワードや図像装飾も同様だ。
* Namespace と NamedElement を ``modelElement`` として持つ UMLShapes の間にある
  ``modelElements`` のない UMLEdges は、その Namespace 端子にマルに囲まれた十字
  で示される。
* Interfaces を ``modelElements`` として持ち、玉またはソケット記法で描画される
  UMLClassifierShapes は Dependencies が次の間にある ``modelElements`` として持
  つ UMLEdgesの ``source`` または ``target`` であることが許される：

  #. Interfaces を必要とするか支給する Ports
  #. InterafaceRealization または Interface を ``suppliers`` とする Usage
     Dependencies
* ``required`` Interfaces と ``provided`` Interfaces を表す玉とソケット記法は
  ``isIcon`` の値が真である UMLClassifierShapes として交換される。

     The lines between these notations and port rectangles are interchanged as
     UMLEdges with InterfaceRealization or Usage Dependencies as
     ``modelElements`` with the Interfaces as ``suppliers``, which determine
     whether the UMLClassifierShapes shall be rendered as balls or sockets (used
     Interfaces are ``required`` and realized Interfaces are ``provided``).

UMLCompositeStructureDiagram は StructuredClassifier である ``modelElements``
か、または StructuredClassifier である ``classifier`` を持つ
InstanceSpecification である ``modelElements`` を持つ (B.2.4)。

特に UMLCompositeStructureDiagrams の内容物に関する注意点：

* Interfaces を ``modelElements`` として持ち、玉またはソケット記法で描画される
  UMLClassifierShapes は、Interfaces を必要とするか支給する Ports である
  ``roles`` を持つ ConnectorEnds を ``modelElements`` として持つ Connectors を持
  つ UMLEdgesの ``source`` または ``target`` であることが許される。
* Connectors を ``modelElements`` とする UMLEdges は、Connector ``end``
  ``roles`` が ``partWithPort`` の値を持つ Ports であり、ちょうど一つの
  Interface を必要とするか支給する場合、Interfaces を ``modelElements`` とする
  UMLClassifierShapes を ``source`` か ``target`` あるいはその両方とし、玉または
  ソケット記法で描画してよい。
* ``modelElements`` に Interfaces を持ち、玉またはソケット記法 (B.3.3) で描画さ
  れる UMLClassifierShapes は、``partWithPort`` の値を持つ Ports であり、ちょう
  ど一つの Interface を要求または支給する ``end`` ``roles`` を持つ Connectors を
  見せるために、（玉がソケットの中にあり、両者の間に線がないように）互いに近接し
  て描画してよい。

     These UMLClassifierShapes may be the ``source`` or ``target`` of multiple
     UMLEdges that have all InterfaceRealization or all Usage Dependencies as
     ``modelElements`` when the Connector has more than two ``ends``.

UMLProfileDiagrams 注意点：

* Stereotype 定義は UMLClassifierShapes と共に示されるものとする (B.3.3)。
* Extensions を ``modelElements`` として持つ UMLEdges は、回航可能矢印や他の関連
  装飾を伴わず、鏃が黒塗りの実線矢印として描画されるものとする。
* ProfileApplications を ``modelElements`` とする UMLEdges は鏃が開いた破線矢印
  として描画される。

Template 署名矩形は TemplateSignatures を ``modelElements`` とする UMLShapes と
して交換され、それはこの TemplateSignature を ``modelElement`` とする単一の
UMLLabel かまたは UMLLabel 一つにつき TemplateParameter 一つを ``modelElement``
とする UMLLabels を含むものとする。

B.3.3 Classifier Shapes
----------------------------------------------------------------------

   Figure B.9 Classifier Shapes

UMLCompartmentableShape を UMLClassifierShape に特殊化し、特性を追加し、ちょうど
一つの Classifier を見せるように制限する。

* UMLClassifierShape は ``feature`` 区画で示される ``modelElements`` に対して
  ``isIndentForVisibility`` を導入。特徴が可視性の見出しの下でインデントされて表
  示されることを示す。
* ``isDoubleSided`` を導入。``isActive`` の値が真の Class で、矩形として表示され
  る ``modelElements`` に対して垂直辺を二重線で引くかどうかを示す。

UMLClassifierShapes 注意点：

* ``ownedElements`` UMLClassifierShapes であり、``modelElements`` として
  Classifiers を持ち、UMLLabel の特殊化のどれにも分類されない UMLLabels には、そ
  の Classifier の情報を示す UML が指定するテキストをもたせるものとする。
* UMLClassifierShape ``compartments`` にテキスト順に示される Classifier
  ``features`` は ``modelElements`` として単独 Feature それぞれを有する
  UMLLabels と交換されるものとする。
* UMLClassifierShape ``compartments`` でテキスト順に示される Classifier
  ``features`` の下に現れる省略記号は ``modelElements`` のない UMLLabels とし
  て、また UMLCompartments の ``orderedElement`` の最後のものとして交換されるも
  のとする。
* Components を ``modelElements`` とする UMLClassifierShapes は、
  ``modelElements`` として、その Components の ``required`` と ``provided``
  Interfaces を持つ ``ownedElements`` として UMLLabels を持つ ``ownedElements``
  として UMLCompartments を持つことが許される。ここで、この UMLLabals は
  Interfaces の ``names`` を示す。
* さらに (B.3.3) も参照すること。

B.3.4 Multiplicity and Association End Labels
----------------------------------------------------------------------

   Figure B.10 Multiplicity and Association End Labels

UMLLabel を UMLMultiplicityLabel と UMLAssociationEndLabel に特殊化し、それぞれ
ちょうど一つの MultiplicityElement または Association ``memberEnd`` に関する情報
を表示するように制限する。

UMLMultiplicityLabels と UMLAssociationEndLabels に関する注意：

* UMLCompartments にあるテキストで示される Properties に関する情報は、たとえその
  Property が Association ``memberEnd`` であろうと、 Multiplicity が示されていよ
  うと、UMLMultiplicityLabels や UMLAssociationEndLabel ではなく、直接 UMLLabel
  (B.3.3) を用いて交換されるものとする。
* UMLMultiplicityLabel は MultiplicityElement が定義する ``modelElements`` の部
  分に関する情報を見せるのに用いるものであって、Property のような
  ``modelElements`` を分類するであろう MultiplicityElement の他の特殊化ではな
  い。
* ConnectorEnds は UMLMultiplicityLabel で示すものとする。ConnectorEnds により導
  入される唯一の非導出 Property である ``role`` は、Connector を
  ``modelElements`` とする UMLEdges の ``targets`` により示され、ConnectorEnd の
  唯一の一般化は MultiplicityElement だ。

     Information about ``definingEnds`` of ConnectorEnds is shown with
     UMLAssociationEndLabels (``definingEnds`` are Properties).
* UMLAssociationEndLabels は UMLMultiplicityLabel で示されるもの以外の
  Association ``memberEnds`` に関する情報を示すのに用いられるものとする。

     Multiple UMLAssociationEndLabels can have the same ``modelElement``, each
     showing its own aspect of the ``modelElement``.
* ExtensionEnds を ``modelElements`` として持つ UMLAssociationEndLabels は、その
  ``modelElements`` が ``lower`` の値が 1 であるときにしか用いることが許されな
  い。この場合、UMLAssociationEndLabels の ``text`` の値は ``{required}`` である
  ものとする。

B.3.5 Association, Connector, and Link Shapes
----------------------------------------------------------------------

   Figure B.11 Association, Connector, and Link Shapes

UMLShape を UMLAssociationOrConnectorOrLinkShape に特殊化して、特性を一つ追加
し、Association ``classifier`` を持つ Association か InstanceSpecification か
Connector をちょうど一つ見せるように制限する。また、その ``modelElement`` の表示
方法を示す ``kind`` を導入する。

端の数に関係なく、ひし形からちょうど2本の線
は、Properties（UMLAsstionationOrConnectorOrLinkShapeのAssociationモデル要素の
memberEnds、または、 InstanceSpecification モデル要素
UMLAssociationOrConnectorOrLinkShape の分類子である Association の memberEnd）、
または ConnectorEnds （Connector モデル要素 UMLAssociationOrConnectorOrLinkShape
の両端）のいずれかであるモデル要素を持つ UMLEdges と相互交換しなければならない。


``kind`` の値が ``diamond`` である UMLAssociationOrConnectorOrLinkShapes は菱型
として描画されるものとし、

* 二つの ``memberEnds`` がある Association ``classifier`` か、
* 二つの ``ends`` がある Connector か、
* 二つの ``memberEnds`` がある Association ``classifier`` がある
  InstanceSpecification

のいずれかの ``modelElement`` を持つものとする。

   (when there are more than two ends these elements are always shown this way,
   and the notation shall be interchanged with UMLShapes).

端子の個数に関係なく、菱形から生えるちょうど二本の線は Properties または
ConnectorEnds のいずれかである ``modelElements`` を持つ UMLEdges と交換されるも
のとする。

* 上記 Properties は次のいずれかだ：

  * «the ``memberEnds`` of the Association ``modelElement`` of the
    UMLAssociationOrConnectorOrLinkShape»
  * «``memberEnds`` of an Association that is a ``classifier`` of the
    InstanceSpecification ``modelElement`` UMLAssociationOrConnectorOrLinkShape»

* 上記 ConnectorEnds は «the ``ends`` of a Connector ``modelElement`` of
  UMLAssociationOrConnectorOrLinkShape» だ。

``kind`` の値が ``triangle`` である UMLAssociationOrConnectorOrLinkShapes はそれ
と同じ ``modelElement`` を持つ UMLEdge を註釈する黒塗りの三角形として描画される
ものとする。

B.4 Behavior
======================================================================

B.4.1 Summary
----------------------------------------------------------------------

UML DI の Behavior 部分は挙動図の外観とその内容を捉える。

B.4.2 Behavior Diagrams
----------------------------------------------------------------------

   Figure B.12 Behavior Diagrams

UMLDiagram を挙動に関する要素を描写する図式を表すための最も一般的なクラス
UMLBehaviorDiagram に特化し、それをさまざまな種類の挙動図へと特化する。
UMLBehaviorDiagrams は高々一個の ``modelElement`` を持つように制限されており、そ
れは Behavior でなければならない。

UMLUseCaseDiagrams には ``modelElements`` がない。内容に関する注意：

* UMLCase 記法は UMLClassifierShapes と交換され、``isIcon`` の値が真のときは楕円
  として、偽のときには矩形として描画されるものとする。
* Actor 記法は UMLClassifierShapes と交換され、``isIcon`` の値が真のときは棒人形
  として、偽のときには矩形として描画されるものとする。
* Actors を示す設計者定義の図像は Stereotype ``icons`` で指定してかまわない。
* Extends と Includes 記法は Extends と Includes を ``modelElements`` とする
  UMLEdges と交換されるものとする。
* Extends を ``modelElements`` として持つ UMLShapes は註釈記号として描画され、特
  化型でない UMLLabels をその二つしかない ``ownedElements`` として持つものとす
  る。この UMLLabels はその Extend の ``condition`` または
  ``extensionLocations`` を ``modelElements`` として持ち、それぞれ UML が指定する
  構文で、この ``condition`` ``specification`` または ``extensionLocation``
  ``names`` を与える ``text`` を持つものとする。

     UMLEdges between such UMLShapes and other UMLDiagramElements shall have no
     ``modelElements`` and be rendered with dashed lines.

UMLStateMachineDiagrams はちょうど一個の ``modelElement`` を持つように制限されて
おり、それは StateMachine でなければならない。

* ``isCollapseStateIcon`` を導入。複合 States を表す UMLShapes に非複合 States
  と区別する小さい図像を含めるかどうかを指示する。
* ``isInheritedDashed`` を導入。``modelElement`` として継承した State を持つ
  UMLShapes の境界を破線にするかどうかを指示する。
* ``isInheritedDashed`` と継承した ``isInheritedLighter`` は

     cannot both have a value of true at the same time, and one of them must
     have a value of true for UMLStateMachineDiagrams that show inherited
     States.

StateMachines は「フローチャート」様式で表示してもよい。そこでは Transition
``triggers`` は凹五角形で示され、Transition ``effects`` にある SequenceNodes に
ある ``executableNodes`` は SendSignalActions であるときを除いて、角丸矩形として
示され、凸五角形として示される。

* フローチャート様式とは ``isTransitionOriented`` の値が真である
  StateMachineDiagrams だ。
* Transitions に関するこの情報は ``isTransitionOriented`` の値が真である
  StateMachineDiagrams ではテキストでしか表示されない。

Transition 指向 UMLStateMachineDiagram は ``modelElements`` として Triggers や
ExecutableNodes を持つ UMLShape を ``ownedElements`` として持つことが許される。
``source`` または ``target`` としてこれらの UMLShape を持つ UMLEdges は
``modelElements`` としてTransitions を持たなければならず、``source`` または
``target`` として同じ UMLShape を共有する UMLEdges では、``modelElements`` は同
じでなければならない。

   In transition-oriented UMLStateMachineDiagrams, UMLEdges that have
   Transitions as ``modelElements``, and have as ``source`` or ``target``
   UMLShapes with States as ``modelElements`` with a value true for
   ``isSubmachineState``, where the Transition’s corresponding ``source`` or
   ``target`` is a ConnectionPointReference, the ConnectionPointReference shall
   be shown textually overlaying the line rendered by the UMLEdge, with
   semicircles at both ends of the text.

このテキストは ConnectionPointReference を ``modelElement`` として持つ UMLLabel
と交換される。

UMLStateMachineDiagrams 注意点：

* 互いに隣接する Regions を ``modelElements`` として持つ UMLShapes は、それらの
  間を結ぶ破線で描画されるものとする。
* その StateMachines または States にある唯一の Regions は示されない。

UMLActivityDiagrams はちょうど一個の ``modelElement`` を持つように制限されてお
り、それは Activity でなければならない。

UMLActivityDiagram は ``isActivityFrame`` を導入。図式の枠を五角形の見出しがない
角丸矩形にするかどうかを示す。``isActivityFrame`` の値が真である場合、

* ``isFrame`` の値は偽だ。
* その Activity の ``name`` は図式の種類を示すことなく、図式の左上に
  UMLNameLabel で表示される。

UMLActivityDiagrams 注意点：

* CallBehaviorActions を ``modelElements`` として持ち、かつ Activities を
  ``behaviors`` として持つ UMLShapes は、折りたたまれていると、その内側にある熊
  手型の記号で描画されるものとする。開いたときにはこの ``behavior`` は枠記法で表
  示されるものとする。そこでは ``modelElements`` として ActivityEdges を持つ
  UMLEdges と、``modelElements`` として Activity またはその
  ActivityParameterNodes を持つ ``source`` または ``targets`` として UMLShapes
  を含む枠表記で表示されるものとする。
* InputPins と OutputPins の情報のいくつかは次のように図表的に示してよい：

  * ``modelElement`` として単一の InputPin または OutputPin を持ち、``isIcon``
    の値が真である UMLShapes は、InputPins に対してはその隣りにある丸矩形に、
    OutputPins に対してはその外に向けられた矩形に、小矢印が描画されるものとする。

       If the InputPin or OutputPin corresponds to a Parameter that has a value
       of true for ``isStream`` the UMLShape shall be rendered as filled,
       inverting the arrow, if any.
  * ``isStream`` の値が真であり、``isIcon`` の値が真である Parameter に対応する
    ``modelElement`` として単一の InputPin または OutputPin を持つ UMLShapes
    は、その中の矢印を反転し、黒塗りで描画されるものとする。

* OutputPins と InputPins の間の ObjectFlows は次のように略記法を用いて示してよ
  い：

  * UMLEdges は、それらの ``source`` または ``target`` が同じ UMLShape であり、
    複数の Pins が ``modelElements`` である場合、同じ ActivityEdge を
    ``modelElement`` として持つものとする。
    UMLShapes は小正方形として描画され、その近くに UMLLabel が描画されることがあ
    る。これらの UMLEdges は ObjectFlows を ``modelElements`` として持ち、
    ``isIcon`` の値が真であり、複数の Pins を ``modelElements`` として持ち、全て
    の Pins が ``isStream`` の値が真である Parameter に対応する ``source`` また
    は ``target`` のUMLShape である場合、黒塗りの矢印で表示されるものとする。
  * ObjectFlows を ``modelElements`` に持つ UMLEdges が Actions を
    ``modelElements`` に持つ同じ UMLShape を ``source`` と ``target`` に持つ場
    合、小さい正方形が線の近くに描画されるものとする。

       The small square shall be interchanged with a UMLShape with the same
       ObjectFlows as ``modelElement`` as the UML Edge (a single UMLEdge may
       have multiple ObjectFlows as ``modelElement``).

* 単一の UMLShape を、ActivityEdge の ``target`` と ``source`` である二つの
  ControlNodes の略記法として、次のように用いることが許される：

  * 単一の UMLShape は ``modelElements`` として MergeNode, ActivityEdge,
    DecisionNode を持つことが許される。MergeNode と DecisionNode がそれぞれこの
    ActivityEdge の ``source`` と ``target`` となる。

    * UMLEdges that have such UMLShapes as ``target`` have an ActivityEdge as
      ``modelElement`` with the MergeNode as ``target``.
    * UMLEdges that have such UMLShape as ``source`` have an ActivityEdge as
      ``modelElement`` with the DecisionNode as ``source``.
  * 単一の UMLShape は ``modelElements`` として JoinNode, ActivityEdge, ForkNode
    を持つことが許される。ここで JoinNode と ForkNode がそれぞれこの
    ActivityEdge の ``source`` と ``target`` となる。

    * UMLEdges that have such UMLShapes as ``target`` have an ActivityEdge as
      ``modelElement`` with the JoinNode as ``target``.
    * UMLEdges that have such UMLShape as ``source`` have an ActivityEdge as
      ``modelElement`` with the ForkNode as ``source``.
* UMLEdges は ExecptionHandler の ``handlerBody`` を ``modelElement`` として持つ
  UMLShapes を ``targets`` として持つことが許される。``isIcon`` が真であるこれら
  の UMLEdges はジグザグ線として描画され、偽ならばジグザグ印がその線の近くに描画
  されるものとする。
* ちょうど一つの ``inputElement``, ``outputElement``, Action ``node`` とちょうど
  二つの ObjectFlow ``edges`` がある ExpansionRegions を、二種類ある略記法の一つ
  を使って示してよく、それらは両方とも ExpansionRegion が ``modelElement`` であ
  る UMLShape を含み、Action ``node`` が ``modelElement`` である UMLLabel を含
  み、UMLShape の中央に描画される。
* ExpansionRegion はちょうど一つの ``inputElement``, ``outputElement``, Action
  ``node`` と、ObjectFlow ``edges`` を二つ持ち、次の二種類の略記法のいずれかで示
  すことが許される。どちらも ExpansionRegion を ``modelElement`` とし、Action
  ``node`` を ``modelElement`` とする UMLLabel を含む UMLShape を含み、UMLShape
  の中央に描画される。

  * 一つは、UMLShape の境界上に ExpansionRegion の ``inputElement`` と
    ``outputElement`` を ``modelElements`` とする他の UMLShapes を二つ持ち、この
    二つの他の UMLShapes は最初の UMLShapes の ``ownedElements`` であるとし、か
    つそれぞれ ObjectFlows を ``modelElements`` とする UMLEdges 二つの
    ``target`` と ``source`` とし、この ObjectFlows はその ``inputElement`` と
    ``outputElement`` をそれぞれ ``target`` と ``source`` とする。
    ``modelElement`` として ExpansionRegion を持つこの UMLSShape は、左上に
    ExpansionRegion の ``mode`` を示す ``modelElement`` として ExpansionRegionを
    持つ UMLKeywordLabel である追加的 ``ownedElement`` を持つものとする。
  * もう一つの記法は並列 ``mode`` ExpansionRegions 専用だ。``inputElement`` と
    ``outputElement`` を表示することは許されない。

       The UMLShape with ExpansionRegion as ``modelElement`` shall be the
       ``target`` and ``source`` of the two UMLEdges with ObjectFlows as
       ``modelElements`` described above, respectively, and shall have an
       additional ``ownedElement`` in the upper right that is a UMLLabel with
       the ExpansionRegion as ``modelElement``, and the value “*” for text.

* 割り込み活動辺は割り込み可能区域により識別される。InterruptibleRegion の
  ``interruptingEdges`` であり、``isIcon`` の値が真である ActivityEdges を
  ``modelElement`` として持つ UMLEdges はジグザグ線として表示される。偽である場
  合、ActivityEdges を ``modelElement`` として持つ UMLShapes は、線の近くにジグ
  ザグの絵として描画される。
* ``isActivityFrame`` の値が真である UMLActivityDiagram の ``modelElement`` であ
  る Activity の ``ownedElements`` である ActivityPartitions を
  ``modelElements`` とする UMLSpapes の外側の線分を融合してもよい。
* ActivityEdge 連結器記法は同じ ActivityEdge を ``modelElements`` として持ち、そ
  の ActivityEdge を ``modelElement`` として持つ UMLLabels を ``ownedElements``
  として有する UMLShapes と交換されるものとする。
* UMLActivityDiagrams 内の UMLLabels については (B.4.3) を見ろ。

UMLInteractionDiagrams にはちょうど一個の ``modelElement`` を持つように制限され
ており、それは Interaction でなければならない。

   UMLInteractionDiagram introduced ``kind``, which affects the rendering of
   diagram contents in some cases. For example, UMLShapes with alt
   CombinedFragments as ``modelElements`` in UMLInteractionDiagrams with the
   value overview for ``kind`` shall be rendered as rhombuses.

``kind`` の値が ``table`` である場合、UMLLabels ではなく UMLShapes である
``ownedElements`` は矩形として描かれる (B.4.5)。UMLInteractionDiagram では、図式
上の生存線を破線で描画するかどうかを指定する ``isLifelineDashed`` も導入されてい
る。

UMLInteractionDiagrams 注意点：

* Interactions の Properties は図式の左上隅の下（五角形の見出しの下）にテキスト
  として示してよく、Classes 内の Proerties の表記と同じ方法で UMLLables と交換さ
  れる。これらの UMLLabels は UMLEdges の ``source`` または ``target`` である他
  のUMLShapes に表示されることがある。これらの UMLShapes は付箋として、UMLEdges
  は破線として描かれるものとする。
* GeneralOrderings を ``modelElements`` として持つ UMLEdges は黒塗りの鏃が線の中
  間にある矢印で描かれなければならない。鏃は別々の UMLShape として交換されてはな
  らない。
* Messages を ``modelElements`` とする UMLEdges で、``messageKind`` の値として喪
  失または発見を持つものは、``target`` または ``source`` 端子に、それぞれ小さな
  黒塗りの円が描かれる。円は別々の UMLShape として交換されてはならない。
* ``modelElements`` として CombinedFragments を持ち、``interactionOperand`` の値
  が par であり、``isIcon`` の値が真である UMLShapes は、形状の上下に中括弧を付
  けて描く（余領域記法）ものとする。
* CombinedFragments はすべて ``interactionOperand`` に関わらず、その UMLShapes
  の左上隅の五角形にテキストを表示するものとする。ここでテキストは
  CombinedFragments を ``modelElements`` とする UMLLabels と交換され、事によると
  複数のラベルが五角形ごとにある。余ったラベルは直接入れ子になった結合断片を
  ``modelElements`` として持つ。
* ExecutionSpecifications を ``modelElements`` として持ち、``isIcon`` の値が真で
  ある UMLShapes は、陰影のある塗りつぶしパターンで描かれるものとする。

B.4.3 Activity Diagram Labels
----------------------------------------------------------------------

UMLActivityDiagrams にある UMLLabels に関する注意点：

* UMLActivityDiagrams の ``ownedElements`` であり、``modelElements`` として
  Activities を持つ UMLLabel の特殊化のどれにも分類されない UMLLabels には、その
  Activity に関する情報の種類を指示するキーワードから始まる ``text`` を ``«`` と
  ``»`` に括って記述されなければならない。
* ActivityParameterNodes を ``modelElements`` とする UMLShapes の
  ``ownedElements`` であり、 Parameters を ``modelElements`` とし、UMLLabel の特
  殊化のどれにも分類されない UMLLabels には、その Parameter に関する情報を与える
  ``text`` を、UML が指定する構文で記すものとする。
* CallOperationAction を ``modelElements`` とする UMLShapes の ``ownedElements``
  であり、 Classes または Operations を ``modelElements`` とし、UMLLabel の特殊
  化のどれにも分類されない UMLLabels には、その Class または Operation またはそ
  の両方の ``name`` を与える ``text`` があり、UML が指定する構文で記すものとす
  る。
* UMLShapes の ``ownedElements`` であり、``modelElements`` に Actions を持ち、
  ``modelElements`` に ActivityPartitions を持つ UMLLabel で、特殊化のどれにも分
  類されない UMLLabels には、ActivityPartitions の ``name`` を与える ``text`` を
  UML が指定する構文で記すものとする。
* ``modelElements`` がない UMLShapes の ``ownedElements`` であり、
  ``modelElements`` として ActivityNodes を持ち、UMLLabel の特殊化のどれにも分類
  されない UMLLabels には、UML が指定するキーワードで始まる ``text`` を ``«`` と
  ``»`` に括って記述されなければならない。
* ObjectNodes を ``modelElements`` とする UMLShape の ``ownedElements`` であ
  り、State を ``modelElements`` とし、UMLLabel の特殊化のどれでもない UMLLabel
  は、UMLLabel の ``modelElements`` の ``names`` を角括弧で囲んだ ``,`` 区切りの
  リストとして描かれるものとする。
* UMLLabel の特殊化のどれでもない、中括弧で括られた ``text`` を持つ UMLLabels に
  は、``modelElements`` として ActivityNodes または ActivityEdges を持ち、その
  ``text`` は ``modelElements`` の特性の値を UML が指定する構文で与えるものとす
  る。
* UMLLabel の特殊化のどれでもない、角括弧で括られた ``text`` を持つ UMLLabels に
  は、``modelElements`` として ActivityEdges を持つものとし、角括弧の間の
  ``text`` は ActivityEdges の ``guard`` を示すものとする。
* UMLLabels は Parameters を ``modelElements`` として 持ち、CallActions の
  InputPins または OutputPins を ``modelElements`` として持つ UMLShapes の近くに
  配置することで、InvocationActions の ``behaviors`` や ``operations`` の
  Parameters を示すことが許される。
* InputPins または OutputPins を示す UMLShapes の近くにある UMLLabels は次に示す
  略記法を交換するのに用いてよい：

  * ActivityParameterNode を ``source`` とする ObjectFlow の ``target`` として
    InputPin を持つ Actions は、その Action, その InputPin,
    ActivityParameterNode の ``parameter`` の ``name`` のみを UMLLabel として表
    示し、その ``parameter`` を ``modelElement`` として交換した略記法で示してよ
    い (15.4.4)。
  * ActivityParameterNode を ``target`` とする ObjectFlow の ``source`` として
    OutputPin を持つ Actions は、その Action, その OutputPin, その近くの
    ActivityParameterNode の ``parameter`` の ``name`` のみを、その
    ``modelElement`` としてその ``parameter`` と UMLLabel として交換した略記法で
    示してよい (15.4.4)。
  * 他の Action の OutputPin を ``source`` とする ObjectFlow の ``target`` とし
    て InputPin を持ち、FlowFinal を ``target`` とする ObjectFlow の ``source``
    である OutputPin を持つ AddVariableValueActions は、もう一方のAction, その
    OutputPin, その ``variable`` を ``modelElement`` とする UMLLabel により示さ
    れる AddVariableValueActions の ``variable`` の ``name`` の近くのみを示す略
    記法で示してよい (16.9.4)。
  * ReadVariableActions である ``fromActions`` を持つ ActionInputPins はこの
    ActionInputPin とその近くの ReadVariableAction の ``variable`` の ``name``
    のみを UMLNameLabelとして交換し、その ``variables`` を ``modelElement`` とす
    る略記法で示してよい。
  * ReadSelfObjectActions である ``fromActions`` を持つ ActionInputPins はこの
    ActionInputPin とその近くの文字列 ``self`` のみを UMLLabel として表示し、こ
    の ReadSelfObjectAction を ``modelElement`` として交換した略記法で示してよ
    い。
  * ValueSpecificaionAction である ``fromActions`` を持つ ActionInputPins はこの
    ActionInputPin とその近くのこの ValueSpecificaionAction の ``value`` のみを
    UMLLabel として表示し、この ``value`` を ``modelElement`` として交換した略記
    法で示してよい。
* ActivityPartitions の見出しはそれらの ActivityPartition を ``modelElement`` と
  する UMLLabels と交換されるものとする。

B.4.4 State Shapes
----------------------------------------------------------------------

   Figure B.13 State Shapes

UMLCompartmentableShape を UMLStateShape に特殊化し、特性を一つ追加し、少なくと
も一つの States を示すように制限する。``isTabbed`` を導入。これはその形状の上部
にタブを追加して State の名前を表示するかどうかを指示する。

UMLStateShape は状態リスト表記を交換する際に複数 ``modelElements`` を持つこと
が許される (14.2.4)。

   In this case, the ``names`` of the ``modelElements`` are shown by a UMLLabel
   with the same ``modelElements``, with the UMLStateShape as ``owningElement``,
   and the UMLLabel shall be rendered as a comma delimited list of the ``names``
   of its ``modelElements``.

UMLStateShapes の内容に関する注意点：

* ``entry``, ``do``, ``exit`` Behaviors を示す UMLLabals には、その Behaviors を
  ``modelElements`` とし、UML が規定する構文の ``text`` を持つものとする。
* 内部または局所 Transitions を示す UMLLabals には、その Transitions を
  ``modelElements`` として持ち、UML が指定する構文の ``text`` を持つ。
* UMLStateShapes の ``ownedElements`` であり、States を ``modelElements`` として
  持ち、UMLLabel のどの特殊化でもない UMLLabels は、その State に関する情報を与
  える UML により規定される ``text`` を持つものとする。

B.4.5 Interaction Tables
----------------------------------------------------------------------

   Figure B.14 Interaction Shapes

UMLLabel を UMLInteractionTableLabel に特殊化し、UMLInteractionDiagrams の表形式
におけるラベルに対して特性を追加する。

UMLInteractionTableLabels は UMLInteractionDiagram の ``ownedElement`` であり、
``kind`` に ``table`` を持つ単一の UMLShape の ``ownedElement`` である UMLShape
の ``ownedElement`` でなければならない。これらの UMLShape はすべて、表全体、およ
び表の各マス目に対して一つずつ、矩形として描かれるものとする。

* 表全体はこの UMLInteractionDiagram の ``ownedElement`` の一つ
* 各マス目は ``ownedElements`` の第二層

表全体の UMLShapes はそれらの ``owningElement`` の ``modelElement`` と同じ
InteractionDiagram を ``modelElement`` として持つものとする。マス目用の UMLShape
は表用の UMLShape 内の ``ownedElement`` とし、``ownedElement`` は複数持たないも
のとし、UMLInteractionTableLabel であるものとする。

最上行のマス目用 UMLShape は ``modelElement`` を持たない ``ownedElement`` を一つ
持つものとする。一方、マス目用の UMLShape 全てとそれらの ``ownedElements`` は
ちょうど一つの ``modelElement`` を持つものとする。同じ列のマス目用
UMLInteractionTableLabels はすべて同じ ``kind`` の値を持つものとする。

B.5 Information Flows
======================================================================

InformationFlows に関係した UMLDiagramElements についての注意点：

* InformationFlows を ``modelElements`` として持つ UMLLabels は ``conveyed`` の
  種類の ``names`` を示す。この InformationFlows の複数 ``conveyed`` ``names``
  は CSV として表示される一つの UMLLabel で示されるものとし、同じ UMLLabel に対
  して複数の ``modelElements`` が存在するか、同じ ``modelElement`` に対して複数
  の ``conveyed`` ``names`` が存在するか、あるいはその両方が原因であってもかまわ
  ない。
* InformationFlows を ``modelElements`` とし、``isIcon`` の値が真である
  UMLShapes は同じ InformationFlows を ``modelElements`` として持つ UMLEdges と
  重なり、その ``informationTarget`` の方を向いて整列された、黒塗りの三角形として
  描かれるものとする。

     There shall be one triangle for all InformationFlows going in the same
     direction realized by the same element (a maximum of two triangles for the
     same realizing element).

B.6 UML Notations and UML DI Representations
======================================================================

本節では UML の表記法が UML DI を利用してどのようにモデル化されるのかを示すこと
で付録 B を要約する。付録 B のすべて、またはここまでの記法のすべてを網羅するもの
ではない。

Table B.1 と B.2 はそれぞれ形状と辺を網羅している。

* Notation 列は UML 記法の見本だ。
* Diagram elements 列は記法に対応する UML DI 要素だ。包含階層的に表現している。

  同じ入れ物を持つ要素は、左から右へ、上から下へと、左の列に示された記法に従って
  並べられる。

  各要素について、図表要素の型が与えられ、その後に ``modelElement`` の型が続き、
  場合によってはその図表要素に適用される他の制約が括弧で括られる。

      The type of modelElement is followed by a ‘+’ when multiple
      ``modelElements`` of this type can be assigned to one diagram element.

* Ref 列では記法が定義されている Notation 節と図表、および UML DI 表現が定義され
  ている Annex B 節を参照する。

B.7 Classifier Descriptions
======================================================================

機械生成による節。

B.8 Association Descriptions
======================================================================

機械生成による節。

.. include:: /_include/uml-refs.txt
