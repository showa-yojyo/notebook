======================================================================
Annex B: UML Diagram Interchange
======================================================================
UML 2.5 pp. 685-742 に関するノート。
ここまで書いておいて何だが、読み返せたものではない。
もっと簡潔にしよう。

.. contents:: ノート目次
   :depth: 2

B.1 Summary
======================================================================
* この付録は、
  設計者が支配力のある UML モデルの、
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
  UML で指定されたとおりにオブジェクトを視覚的に描画 (render) する。

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

  * DI:: のついているメタクラスについては、
    前述の別仕様書を参照すれば詳細はわかる。

  * DI::Diagram と DI::DiagramElement を
    UMLDiagram と UMLDiagramElement それぞれに特殊化してある。

* UMLDiagramElement は UML DI を表現するためのもっとも一般的なクラスである。

  * UMLDiagramElement は DI::DiagramElement::``modelElement`` を再定義することで、
    UMLDiagramElements が他の言語要素ではなく
    UML 要素の表記法であるように限定する。

  * UMLDiagramElement は DI::DiagramElement::``ownedElement`` を再定義することで、
    UMLDiagramElements が UMLDiagramElements だけを所有し、
    かつ整列される（図表要素の z-ordering に影響する）ように限定する。

  * UMLDiagramElement::``isIcon`` は ``modelElements`` に対して、
    矩形ではなく幾何的な形状を用いて見せるオプションであるか、
    線を先が開いた実線矢印ではなく、線で見せるオプションである。

    * UMLShapes は同時に両方の表記法を用いてよい。
      交換時には同じ ``modelElement`` があるふたつの
      UMLShapes になる。

* UMLDiagramElement に関して注意することをいくつか挙げる。

  * ``ownedElements`` の ``bounds`` には
    ``owningElements`` の ``bounds`` と交わらなくてもよい。

  * ``ownedElements`` の ``modelElements`` には
    ``owningElements`` の ``modelElements`` とは異なる
    ``owners`` があってもよい。

* UMLDiagram は UML 図式を表すためのもっとも一般的なクラスであり、
  当付録で定義された図式分類の根底である。

  * UMLDiagram は Packages による所有権を表すために
    PackageableElement から特殊化されている。

  * ``isFrame`` は図式の枠を見せる必要があるかどうかを指示する。
  * ``isISO`` は ISO 表記法規則に準じる必要があるかどうかを指示する。
  * ``isInheritedLighter`` は継承要素を
    明るい色で見せる必要があるかどうかを指示する。

B.2.3 UML Shapes and Edges
----------------------------------------------------------------------
* Figure B.3 UML Shapes and Edges

  * DI::Shape と DI::Edge を UMLShape と UMLEdge にそれぞれ特殊化することで、
    それらを具象型にし、継承された特性を再定義する。

* UMLShape は線として表現されることが全くない UMLDiagramElements を表すための
  最も一般的なクラスである。

  * UMLLabels ではなく、
    ``modelElements`` がなく、
    ただひとつの ``ownedElement`` として単独の UMLLabel に
    少なくともひとつの ``modelElement`` があるような UMLShapes は、
    註釈記号として描画されるものとする。
    そのような UMLShapes と他の UMLDiagramElements とを接続する
    UMLEdges は破線を用いて描画されるものとする。

  * ふたつを超える端点がある Dependency を示す矢印 (pl.) は
    ``modelElement`` として Dependency があり、かつ
    ``modelElement`` として Dependency がある UMLShape がある
    ``source`` または ``target`` の一方を有する UMLEdges として交換される。

* UMLEdge は常に線として描画される UMLDiagramElements を表すための
  最も一般的なクラスである。
  DI::Edge から継承した ``source`` と ``target`` を再定義して、
  UMLEdges が UMLDiagramElements 同士をリンクするように限定する。

B.2.4 Labels
----------------------------------------------------------------------
* Figure B.4 Labels

  * UMLShape を文字列としてしか描画されてはならない形状を表すための
    最も一般的なクラス (UMLLabel) に特殊化する。
    そして UMLLabel を数種の UMLDiagrams で用いられる
    さまざまな種類のラベルに特殊化する。

* UMLLabels のすべては少なくともひとつの ``modelElement`` があるものする。
  ただし UMLLabel にしか分類されず、
  その特殊化のいずれでもないようなものは除く。

* UMLLabel の特殊化は ``modelElement`` Property の ``type`` が定義する
  ``modelElements`` の部分部分に関する情報を示す目的がある。
  例えば、UMLNameLabel::``modelElement`` は NamedElements に限定される。
  これらは ``name`` と ``visibility`` を表す Properties があり、
  かつ UMLNameLabel が示す ``modelElement`` の部分となる。

* UMLNameLabels は NamedElements についての情報を示す目的があり、
  常に ``name`` または ``namedExpression`` または
  NamedElement がインポートされたときは ElementImport ``alias`` を含む。
  また、ラベルはパッケージの封じ込め（限定名）と可視性を含んでもよい。

* UMLKeywordLabels は ``«`` と ``»`` に挟まれる、
  UML が仕様化した文言と句読点を用いる
  ``modelElements`` に関するさまざまな種類の情報を示す目的がある。

* UMLTypedElementLabel は
  ちょうどひとつの Slot, InstanceSpecification, InstanceValue, 
  または TypedElement や Connector といった ``type`` のある要素についての
  名前、型、役割の情報を示すものである。
  UMLTypedElementLabels を交換することについて注意する点がある：

  * ``modelElement`` が Slot であると、
    ``text`` は ``definingFeature`` の ``name`` と、
    ``definingFeature`` の ``type`` の ``name`` と、
    それに ``modelElement`` の ``value`` を含んでもよい。

  * ``modelElement`` が InstanceSpecification または
    InstanceValue であると、
    ``text`` は InstanceSpecification の ``name`` または
    InstanceValue の ``instance`` の ``name`` と、
    InstanceSpecification の ``classifiers`` の ``names`` または
    InstanceValue の ``instance`` の ``names`` を含んでもよい。

  * ``modelElement`` が ``specification`` のある InstanceSpecification であれば、
    ``text`` は ``specification`` を含んでもよい。

  * ``modelElement`` が ``classifier`` として StructuredClassifier のある
    InstanceSpecification の ``slot`` の ``value`` である
    InstanceValue であり、
    UMLTypedElementLabel が
    その InstanceValue が ``modelElement`` とする形で、
    その InstanceSpecification を ``modelElement`` として有する
    UMLCompositeStructureDiagram に見えていれば、
    ``text`` はその UMLTypedElementLabel の ``modelElement`` である
    InstanceValue を所有している Slot の
    ``definingFeature`` を定義している Property の ``name`` を含んでもよい。

  * ``modelElement`` に ``type`` があって、
    それが TypedElements`` か ``Connectors`` であれば、
    ``text`` は ``modelElement`` の ``name`` および
    その ``modelElement`` の ``type`` の ``name`` を含んでもよい。

* UMLRedefinesLabel はちょうどひとつの RedefinableElement についての
  情報を示すものであり、
  ``redefinedElement`` の ``name`` を含んでよい。

B.2.5 Compartmentable Shapes
----------------------------------------------------------------------
* Figure B.5 UML Compartmentable Shapes

  * UMLDiagramElement と UMLShape を
    UMLCompartmentableShape と UMLCompartment にそれぞれ特殊化して、
    隔離された内容の形状を表すために、
    具象型とし、特性を追加し、継承された特性を再定義する。

* UMLCompartmentableShape はその形状の内部にある
  隔離された部分に情報を示すことを許す UML 要素を表す最も一般的なクラスであり、
  いつも線形に配列されて、実線により分離されるものである。

* 区画の表題は
  ``modelElements`` がない UMLLabels として交換可能であるものとし、
  かつ UMLCompartments の ``orderedElement`` の最初のものとして
  交換可能であるものとする。

B.2.6 Stereotype Applications
----------------------------------------------------------------------
* Figure B.6 Stereotype Application Labels

  * UMLLabel を UMLStereotypePropertyValueLabel に特殊化することで、
    UML 抽象構文要素に適用する
    Stereotypes の Property の値を示すための関連を導入する。

* UMLStereotypePropertyValueLabels には
  Stereotypes の ``attributes`` が ``modelElements`` としてあり、
  Stereotype が適用される Element を与える。

* Stereotype 適用の交換に関する他の注意点を挙げる：

  * UML 抽象構文要素に適用される Stereotypes はテキスト的に示しても
    図表的に示してもよい。

  * 次の条件を満たす UMLShapes は ``icon`` として描画されるものとする。
    適用されている Stereotypes がないときにはどのような描画アイコンも
    この場合は描画されない。

    * ``modelElement`` にちょうどひとつの Stereotype が適用されていて
      ``icon`` に対する値があって、
    * ``isIcon`` に対する値が true であって、
    * ``isIcon`` に対する値が false であるときに矩形で描画される。

  * 次の条件を満たす UMLShapes は
    Stereotype ``icon`` として描画されるものとする：

    * Stereotype を ``icon`` に対する値のある ``modelElement`` として有して、

    * ``modelElement`` に Stereotype が適用された ``modelElements`` がある
      UMLDiagramElements の ``ownedElements`` であり、

    * ``isIcon`` に対する値が true である。

    これらの UMLShapes は次のいずれかの場所で描画されるものとする：

    * それらの ``owningElements`` である UMLShapes について
      描画された幾何的図形の内側であるが、
      それらが ``isIcon`` に対して false の値であるものとする。

    * それらの ``owningElements`` である UMLEdges について
      描画された線の近く。

    * それらの ``owningElements`` である UMLLabels について
      描画された文字列の左側の方。

B.2.7 UML Styles
----------------------------------------------------------------------
* Figure B.7 UML Styles

  * DI::Style を UML におけるスタイルを表す最も一般的なクラス
    UMLStyle へと特殊化することで、それを具象型にし、特性を追加し、
    UMLDiagramElement の継承されたスタイルに関係する特性を再定義する。

* UMLStyle は UMLDiagramElements を描画するのに利用されるフォントの
  名前およびサイズを指定する特性を導入する。

  * ``fontSize`` はポイント単位で与えられる。

B.3 Structure
======================================================================

B.3.1 Summary
----------------------------------------------------------------------
* UML DI の Structure 部分は構造の図表の外観とその中身を捕捉する。

B.3.2 Structure Diagrams
----------------------------------------------------------------------
* Figure B.8 Structure Diagrams

  * UMLStructureDiagram の特殊化クラスが多い。

  * UMLDiagram を構造の要素を描写する図式を表すための
    最も一般的なクラス UMLStructureDiagram へと間接的に特殊化して、
    それをさまざまな種類の構造の図表へと特殊化する。

* UMLStructureDiagrams はいずれも ``modelElements`` がないが、
  例外として UMLCompositeStructureDiagrams は除く。
  これらはちょうどひとつあり、
  すべてに関連 (UMLDiagramWithAssociations) を表すための図表的オプションがある。

* UMLDiagramWithAssociations の内容に関して注意点をいくつか挙げる。

  * これらの図式はドット記法を関連を表すのに用いてよいし、用いなくてもよい。
    どちらになるのかは ``isAssociationDotShow`` により指示される。

  * ``navigabilityNotation`` と ``nonnavigabilityNotation`` で決定される
    航行可能記法は
    Associations を ``modelElements`` とする UMLEdges や、
    Association を ``classifier`` とする InstanceSpecifications や、
    Properties や Slots に適用する。

  * 関連線の間にある Generalization の矢印 (pl.) は
    UMLEdges が ``modelElements`` である Generalizations と交換されて、
    UMLEdges である ``sources`` と ``targets`` は
    Associations が（線で示される AssociationClasses もこれに含まれる）
    ``modelElements`` であるものと交換される。

  * Generalizations を示す破線は
    GeneralizationSets が ``modelElements`` である UMLShapes と交換される。

  * 限定された Association ``memberEnds`` を表す記法は、
    ``memberEnd`` が ``modelElement`` である UMLShapes と交換され、
    ``modelElement`` として Association を有する UMLEdges により所有され、
    ``qualifiers`` (UMLProperty) が ``modelElements`` である UMLLabels を所有する。

  * ``modelElements`` として InstanceSpecifications がある
    UMLShapes の間にある UMLEdges と
    リンクを示すつもりであるそれは、
    ``classifier`` としてリンクを分類する Association がある
    ``modelElements`` として InstanceSpecifications がある。

* UMLStructureDiagrams の内容に関して注意点をいくつか挙げる。

  * 線で示される Properties または Slots は、
    Properties または Slots が ``modelElements`` である
    UMLEdges とそれぞれ交換される。

  * Packages が ``modelElements`` であり、
    それらの内側に描画される UMLShapes のない UMLShapes は
    Package の ``name`` をタブにではなく、大きい方の矩形に示す。
    そうでない UMLShapes はタブに ``name`` を示す。

  * ``modelElement`` として Namespace と NamedElement のある
    UMLShapes の間にある、``modelElements`` のない UMLEdges は、
    Namespace 端点でマルに囲まれた十字線を用いて示される。

  * Interfaces が ``modelElements`` であり、
    ball or socket 記法で描画される UMLClassifierShapes は
    ``modelElements`` として次に記すものの間にある Dependencies がある
    UMLEdges の ``source`` または ``target`` であってよい。

    #. Interfaces を要求するか供給する Ports
    #. ``suppliers`` として Interfaces がある
       InterafaceRealization または Usage Dependencies

  * ``required`` と ``provided`` Interfaces を表す ball and socket 記法は
    ``isIcon`` の値が true である UMLClassifierShapes と交換される。

* UMLCompositeStructureDiagrams には、
  StructuredClassifiers または
  StructuredClassifier である ``classifier`` のある InstanceSpecifications である
  ``modelElements`` がある。

* UMLCompositeStructureDiagrams に限定して内容に関する注意点をいくつか挙げる：

  * Interfaces が ``modelElements`` であり、
    ball or socket 記法で描画される UMLClassifierShapes は、
    Interfaces を要求するか提供する Ports である
    ``roles`` のある ConnectorEnds のある
    ``modelElements`` として Connectors のある
    UMLEdges の ``source`` または ``target`` であってよい。

  * Connectors が ``modelElements`` である UMLEdges は、
    ``source`` か ``target`` あるいはその両方として
    Interfaces が ``modelElements`` である UMLClassifierShapes があってよく、
    ball or socket 記法で描画してよい。
    このとき、Connector ``end`` ``roles`` は
    ``partWithPort`` に値がある Ports であり、
    ちょうどひとつの Interface を要求または提供する。

  * Interfaces が ``modelElements`` であり、
    ball or socket 記法で描画される UMLClassifierShapes は、
    ``partWithPort`` に値がある Ports であり、
    ちょうどひとつの Interface を要求または提供する
    ``end`` ``roles`` と共に Connectors を見せるために、
    （ボールがソケットの中にあり、それらの間に線がないように）
    お互いの近くに描画してよい。

* UMLProfileDiagrams に関する注意点をいくつか挙げる：

  * Stereotype 定義は UMLClassifierShapes と共に示されるものとする。

  * Extensions が ``modelElements`` である UMLEdges は、
    矢先が黒塗りの実線矢印として描画されるものとする。
    なお、矢印には航行可能矢印や他の関連装飾は付かない。

  * ProfileApplications が ``modelElements`` である UMLEdges は
    矢先が開いた破線矢印として描画されるものとする。

* Template signature 矩形は TemplateSignatures が ``modelElements`` である
  UMLShapes と交換されるものとし、それは
  TemplateSignature が ``modelElement`` である単独の UMLLabel か、
  UMLLabel ごとの TemplateParameter が ``modelElement`` である
  複数の UMLLabels のどちらかを含む。

B.3.3 Classifier Shapes
----------------------------------------------------------------------
* Figure B.9 Classifier Shapes

  * UMLCompartmentableShape を UMLClassifierShape に特殊化することで、
    特性を追加し、ちょうどひとつの Classifier を見せるように制限する。

* UMLClassifierShapes に関する注意をいくつか挙げる：

  * ``ownedElements`` UMLClassifierShapes であり、
    ``modelElements`` として Classifiers があり、
    UMLLabel の特殊化のどれにも分類されない UMLLabels は、
    UML で指定されたテキストに Classifier の情報を与えさせるものとする。

  * UMLClassifierShape ``compartments`` の中にテキスト的に
    整って示された Classifier ``features`` は
    ``modelElements`` として単独の Feature それぞれを有する
    UMLLabels と交換されるものとする。

  * UMLClassifierShape ``compartments`` の中にテキスト的に整って示された
    Classifier ``features`` の下に現れる省略記号 ``...`` は
    ``modelElements`` のない UMLLabels と交換されるものとし、
    UMLCompartments::``orderedElement`` の最後のものとして扱われる。

  * ``modelElements`` として Components がある UMLClassifierShapes は
    ``modelElements`` として Components の
    ``required`` または ``provided`` Interfaces の付いた
    ``ownedElements`` として UMLLabels がある。
    ``ownedElements`` として UMLCompartments があってもよい。
    ここで、UMLLabals は Interfaces の ``names`` を示す。

B.3.4 Multiplicity and Association End Labels
----------------------------------------------------------------------
* Figure B.10 Multiplicity and Association End Labels

  * UMLLabel を UMLMultiplicityLabel と UMLAssociationEndLabel に特殊化することで、
    ただひとつの MultiplicityElement または
    ただひとつの Association ``memberEnd`` についての情報を見せるように
    それぞれ制限する。

* UMLMultiplicityLabels と UMLAssociationEndLabels に関する注意をいくつか挙げる：

  * UMLCompartments にあるテキストで示される Properties に関する情報は
    UMLMultiplicityLabels でも UMLAssociationEndLabel でもなく、
    UMLLabel を用いて直接交換されるものとする。
    たとえ Property が Association ``memberEnd`` であろうと、
    Multiplicity が示されていようとそのようにする。

  * UMLMultiplicityLabel は
    Property のような ``modelElements`` を分類するであろう
    MultiplicityElement の他の特殊化ではなく、
    MultiplicityElement が定義する ``modelElements`` の部分に関する情報を
    見せるのに用いるものとする

  * ConnectorEnds は UMLMultiplicityLabel を用いて示すものとする。
    ConnectorEnds により取り入れられた唯一の非由来 Property つまり ``role`` は、
    ``modelElements`` として Connectors がある
    UMLEdges の ``targets`` により示され、
    ConnectorEnd の唯一の一般化は MultiplicityElement である。

  * UMLAssociationEndLabels は、
    UMLMultiplicityLabel を用いて示されるもの以外の
    Association ``memberEnds`` に関する情報を示すのに用いられるものとする。

  * ``modelElements`` として ExtensionEnds がある UMLAssociationEndLabels は、
    ``modelElements`` が ``lower`` の値が 1 であるときにだけしか
    用いられないものとする。
    この場合には
    UMLAssociationEndLabels は ``text`` の値が ``{required}`` であるものとする。

B.3.5 Association, Connector, and Link Shapes
----------------------------------------------------------------------
* Figure B.11 Association, Connector, and Link Shapes

  * UMLShape を UMLAssociationOrConnectorOrLinkShape に特殊化して、
    特性を追加し、ちょうどひとつの Association, Connector, または
    Association classifier の付いた InstanceSpecification を見せるように制限する。

* ``kind`` の値が diamond である UMLAssociationOrConnectorOrLinkShapes は
  菱型として描画されるものとし、
  ふたつの ``memberEnds`` がある Association ``classifier`` か、
  ふたつの ``ends`` がある Connector か、
  またはふたつの ``memberEnds`` がある
  Association ``classifier`` がある InstanceSpecification
  のいずれかである ``modelElement`` があるものとする。

* kind の値が ``triangle`` である UMLAssociationOrConnectorOrLinkShapes は
  それと同じ ``modelElement`` がある UMLEdge を註釈する
  黒塗りの三角形として描画されるものとする。

B.4 Behavior
======================================================================

B.4.1 Summary
----------------------------------------------------------------------
* UML DI の Behavior 部分は挙動の図表の外観とその中身を捕捉する。

B.4.2 Behavior Diagrams
----------------------------------------------------------------------
* Figure B.12 Behavior Diagrams

  * UMLDiagram を挙動の要素を描写する図式を表すための
    最も一般的なクラス UMLBehaviorDiagram に特殊化して、
    それをさまざまな種類の挙動の図表へと特殊化する。

  * UMLBehaviorDiagrams は一個を超える ``modelElement`` がないように制限されており、
    それは Behavior でなければならない。

* UMLUseCaseDiagrams には ``modelElements`` はない。

  * UMLCase 表記法は UMLClassifierShapes と交換されるものとし、
    これらは ``isIcon`` の値が true のときには楕円として、
    値が false のときには矩形として描画される。

  * Actor 表記法は UMLClassifierShapes と交換されるものとし、
    これらは ``isIcon`` の値が true のときには棒人形として、
    値が false のときには矩形として描画される。

  * Actors を示す設計者定義のアイコンを Stereotype ``icons`` を以って指定してよい。

  * Extends と Includes 表記法は
    Extends と Includes が ``modelElements`` である
    UMLEdges と交換されるものとする。

  * Extends が ``modelElements`` である UMLShapes は註釈記号として描画されるものとし、
    特化版でない UMLLabels を
    そのふたつしかない ``ownedElements`` として有する。

* UMLStateMachineDiagrams はちょうど一個の ``modelElement`` があるように制限されており、
  それは StateMachine でなければならない。

  * ``isCollapseStateIcon`` は合成 States を表す UMLShapes が
    合成でない States と区別する小さいアイコンを
    含むものとするかどうかを指示する。

  * ``isInheritedDashed`` は継承した State を ``modelElement`` とする
    UMLShapes の境界を破線とするかどうかを指示する。

* ``isTransitionOriented`` の値が true である StateMachineDiagrams では
  StateMachines はフローチャート様式で示してよく、
  Transition ``triggers`` は凹五角形として示され、
  Transition ``effects`` にある SequenceNodes にある ``executableNodes`` は、
  SendSignalActions であるときを除いて、
  角の丸い矩形として示され、凸五角形として示される。

* UMLStateMachineDiagrams の内容に関する注意点：

  * 互いに隣接している Regions が ``modelElements`` である UMLShapes は、
    それらの間を結ぶ破線で描画されるものとする。

  * StateMachines または States にそれしかないというような Regions は示されない。

* UMLActivityDiagrams はちょうど一個の ``modelElement`` があるように制限されており、
  それは Activity でなければならない。

  * ``isActivityFrame`` は図式枠を五角形見出しのない
    丸角矩形とするものかどうかを指示する。

    * ``isActivityFrame`` が true のときには
      必ず ``isFrame`` は false であるものとする。

* UMLActivityDiagrams の内容に関する注意点：

  * CallBehaviorActions が ``modelElements`` であり、
    かつ Activities が ``behaviors`` である UMLShapes は、
    折りたたまれていると、
    その内側にある熊手型の記号で描画されるものとする。

  * InputPins と OutputPins の情報は次のようにして図表的に示してよい：

    * 単一の InputPin または OutputPin が ``modelElement`` であり、
      ``isIcon`` の値が true である UMLShapes は、
      InputPins に対しては 矩形内にある小さい矢印が
      それらが隣接する丸い矩形を向いているように、
      OutputPins に対しては離れる方向を向いているように
      描画されるものとする。

    * 単一の InputPin または OutputPin が
      ``isStream`` の値が true である Parameter に対応する
      ``modelElement`` であり、
      かつ ``isIcon`` の値が true である UMLShapes は、
      その内側に黒塗りの逆矢印として描画されるものとする。

  * OutputPins と InputPins の間の ObjectFlows は次のようにして
    速記法を用いて示してよい：

    * UMLEdges は、
      それらの ``source`` または ``target`` が
      複数の Pins が ``modelElements`` である UMLShape と同じであるときには、
      それらには ``modelElement`` と同じ ActivityEdge があるものとする。

    * ObjectFlows が、
      UMLEdges が ``source`` と ``target`` として
      Actions が ``modelElements`` である同じ UMLShapes のある
      ``modelElements`` である UMLEdges は、
      線の近くにある小さい正方形を使って描画されるものとする。

  * 次に記すように、単一の UMLShape を
    ActivityEdge の ``target`` と ``source`` であるふたつの
    ControlNodes の代わりとなる速記法として用いてよい。

    * 単一の UMLShape には、
      ``modelElements`` として
      MergeNode, ActivityEdge, DecisionNode があってもよい。
      ここで MergeNode と DecisionNode がそれぞれ
      ActivityEdge の ``source`` と ``target`` である。

    * 単一の UMLShape には、
      ``modelElements`` として 
      JoinNode, ActivityEdge, ForkNode があってもよい。
      ここで JoinNode と ForkNode がそれぞれ
      ActivityEdge の ``source`` と ``target`` である。

  * UMLEdges には
    ExecptionHandler の ``handlerBody`` を ``modelElement`` とする UMLShapes を
    ``targets`` としてあってもよい。
    これらの ``isIcon`` が true である UMLEdges は
    ジグザグ線として描画されるものとし、
    false ならばジグザグマークが線の近くにあるように描画されるものとする。

  * ちょうどひとつの ``inputElement``, ``outputElement``, Action ``node`` と
    ちょうどふたつの ObjectFlow ``edges`` がある ExpansionRegions を、
    二種類ある略記法のひとつを使って示してよく、
    それらは両方とも
    ExpansionRegion が ``modelElement`` である UMLShape を含み、
    Action ``node`` が ``modelElement`` である UMLLabel を含み、
    UMLShape の中央に描画される。

    * ひとつ目の表記法は、
      UMLShape の境界上に
      ExpansionRegion の ``inputElement`` と ``outputElement`` が
      ``modelElements`` であるふたつの他の UMLShapes があるものする。
      ただし、このふたつの他の UMLShapes は
      最初の UMLShapes の ``ownedElements`` であるものとし、
      かつ ObjectFlows が ``modelElements`` である
      ふたつの UMLEdges のそれぞれ ``target`` と ``source`` であるものする。
      ただし、ObjectFlows には
      ``inputElement`` と ``outputElement`` がそれぞれ
      ``target`` と ``source`` としてあるものとする。

    * もうひとつの表記法は平行 ``mode`` の ExpansionRegions のみについてのものである。
      それは ``inputElement`` と ``outputElement`` を見せてはならない。

  * 割り込み活動エッジは割り込み可能な区域により見分ける。

  * ActivityPartitions が
    ``isActivityFrame`` が値 true である
    UMLActivityDiagram の ``modelElement`` である
    Activity の ``ownedElements`` である ``modelElements`` である
    UMLSpapes の線分の外側は、
    活動枠と併合してもよい。

  * ActivityEdge 連結器記法は
    ``modelElements`` と同じ ActivityEdge がある
    UMLShapes と交換されるものとし、
    ``ownedElements`` として
    その ActivityEdge が ``modelElement`` である
    UMLLabels を有するものとする。

* UMLInteractionDiagrams にはちょうど一個の
  ``modelElement`` があるように制限されており、
  それは Interaction でなければならない。

  * ``isLifelineDashed`` は生存線を破線で描画するものと
    するかどうかを指示する。

* UMLInteractionDiagrams の内容に関する注意点：

  * Interactions の Properties を
    図式の左上隅の下（表題の五角形の下）にテキストとして示してよく、
    Classes の Properties を表す表記法と同じように UMLLabels と交換される。

  * GeneralOrderings が ``modelElements`` である UMLEdges は
    黒塗りの矢先が線の中間にあるように描画するものとする。

  * Messages が
    紛失または発見を ``messageKind`` の値とする ``modelElements`` である UMLEdges は
    小さな黒塗りの円がそれぞれ ``target`` または ``source`` 端にあるように
    描画するものとする。

  * ``interactionOperand`` の値が **par** である ``modelElements`` である
    CombinedFragments があり、
    かつ ``isIcon`` の値が true である UMLShapes は、
    形状の上部と下部に中括弧として描画するものとする。

  * ``interactionOperand`` に関わらず、すべての CombinedFragments は
    テキストをそれらの UMLShapes の左上隅の五角形にあるように示すものとする。
    ここでテキストは CombinedFragments を ``modelElements`` とする
    UMLLabels と交換され、
    事によると複数のラベルが五角形ごとにある。

  * ExecutionSpecifications が ``isIcon`` の値が true である
    ``modelElements`` である UMLShapes は
    陰ったパターンを使って描画するものとする。

B.4.3 Activity Diagram Labels
----------------------------------------------------------------------
* UMLActivityDiagrams に用いられる UMLLabels に関する注意点：

  * UMLActivityDiagrams の ``ownedElements`` であり、
    Activities を ``modelElements`` とし、
    UMLLabel の特殊化のどれによっても分類されない
    UMLLabels には、
    Activity について示す情報の種類を指示する
    ``«`` と ``»`` に括られた
    UML が指定するキーワードから始まる ``text`` があるものとする。

  * ActivityParameterNodes が ``modelElements`` である
    UMLShapes の ``ownedElements`` であり、
    Parameters を ``modelElements`` とし、
    UMLLabel の特殊化のどれによっても分類されない
    UMLLabels には、
    Parameter についての情報を与える ``text`` があり、
    UML が指定する構文で記すものとする。

  * CallOperationAction が ``modelElements`` である
    UMLShapes の ``ownedElements`` であり、
    Classes または Operations を ``modelElements`` とし、
    UMLLabel の特殊化のどれによっても分類されない
    UMLLabels には、
    Class または Operation またはその両方の ``name`` を与える ``text`` があり、
    UML が指定する構文で記すものとする。

  * Actions が ``modelElements`` である
    UMLShapes の ``ownedElements`` であり、
    ActivityPartitions を ``modelElements`` とし、
    UMLLabel の特殊化のどれによっても分類されない
    UMLLabels は、
    ActivityPartitions の ``name`` を与える ``text`` を
    UML が指定する構文で記すものとする。

  * ``modelElements`` がない UMLShapes の ``ownedElements`` であり、
    ``modelElements`` として ActivityNodes があり、
    UMLLabel の特殊化のどれにも分類されていない UMLLabels には、
    UML により指定されたキーワードが guillemets に括られたもので始まり、
    その ActivityNode についてわかる情報の種類を示す
    ``text`` があるものとする。

  * 中括弧で括られた ``text`` があり、
    UMLLabel の特殊化のどれによっても分類されない
    UMLLabels には、
    ``modelElements`` として ActivityNodes または ActivityEdges があるものとし、
    ``text`` は ``modelElements`` の特性の値を
    UML が指定する構文で与えるものとする。

  * 角括弧で括られた ``text`` があり、
    UMLLabel の特殊化のどれによっても分類されない
    UMLLabels には、
    ``modelElements`` として ActivityEdges があるものとし、
    角括弧の間の ``text`` は
    ActivityEdges の ``guard`` を示すものとする。

  * UMLLabels は ``modelElements`` として Parameters があってもよく、
    InvocationActions の ``behaviors`` や ``operations`` の
    Parameters を示すために、
    CallActions の InputPins または OutputPins を
    ``modelElements`` とする UMLShapes の近くにおいてよい。

  * InputPins または OutputPins を示す
    UMLShapes の近くにある UMLLabels は次に示す速記法を
    交換するのに用いてよい。

    * ActivityParameterNode が ``source`` である ObjectFlow の
      ``target`` として InputPin がある Actions は、
      Action, InputPin, そして
      ``parameter`` が ``modelElement`` である UMLLabel として交換される
      ActivityParameterNode の ``parameter`` の ``name`` だけを示す
      速記法で示してよい。

    * ActivityParameterNode が ``target`` である ObjectFlow の
      ``source`` として OutputPin がある Actions は、
      Action, OutputPin, そして
      ``parameter`` が ``modelElement`` である UMLLabel として交換される
      ActivityParameterNode の ``parameter`` の ``name`` のすぐ近くだけを示す
      速記法で示してよい。

    * 別の Action の OutputPin が ``source`` である ObjectFlow の
      ``target`` として InputPin があり、
      ``target`` として FlowFinal がある ObjectFlow の ``source`` である
      OutputPin がある AddVariableValueActions は、
      もう一方の Action, OutputPin, そして
      ``variable`` が ``modelElement`` である UMLLabel により示される
      AddVariableValueActions の ``variable`` の ``name`` のすぐ近くだけを示す
      速記法で示してよい。

    * ReadVariableActions である ``fromActions`` と一緒の ActionInputPins は
      ActionInputPin と
      ``variable`` が ``modelElement`` である UMLNameLabel として交換される
      ReadVariableAction の ``variable`` の ``name`` のすぐ近くだけを示す
      速記法で示してよい。

    * ReadSelfObjectActions である ``fromActions`` と一緒の ActionInputPins は
      ActionInputPin と
      ReadSelfObjectAction が ``modelElement`` である UMLLabel として交換される
      文字列 ``self`` のすぐ近くだけを示す
      速記法で示してよい。

    * ValueSpecificationActions である ``fromActions`` と一緒の ActionInputPins は
      ActionInputPin と
      ``value`` が ``modelElement`` である UMLLabel として交換される
      ValueSpecificationAction の ``value`` のすぐ近くだけを示す
      速記法で示してよい。

  * ActivityPartitions の表題は
    それらの ActivityPartition が ``modelElement`` である
    UMLLabels と交換されるものとする。

B.4.4 State Shapes
----------------------------------------------------------------------
* Figure B.13 State Shapes

  * UMLCompartmentableShape を UMLStateShape に特殊化することで、
    特性をひとつ追加し、ひとつまたはそれを超える States を示すように制限する。

    * ``isTabbed`` は形状の上部にタブを追加して、
      State の名前を表示するものとするかどうかを指示する。

* UMLStateShapes の内容に関する注意点：

  * ``entry``, ``do``, ``exit`` Behaviors を示す UMLLabals には、
    その Behaviors が ``modelElements`` としてあるものとし、
    ``text`` は UML で指定された構文であるものとする。

  * 内部または局所 Transitions を示す UMLLabals には、
    その Transitions が ``modelElements`` としてあるものとし、
    ``text`` は UML で指定された構文であるものとする。

  * UMLStateShapes の ``ownedElements`` であり、
    ``modelElements`` として States があり、
    UMLLabel のどの特殊化にも分類されない UMLLabels は、
    UML で指定された ``text`` に
    State に関する情報を与えさせるものとする。

B.4.5 Interaction Tables
----------------------------------------------------------------------
* Figure B.14 Interaction Shapes

  * UMLLabel を UMLInteractionTableLabel に特殊化して、
    UMLInteractionDiagrams の表形式を利用したラベルのために
    特性を追加する。

* UMLInteractionTableLabels は
  ``kind`` が表の値である UMLInteractionDiagram の ``ownedElement`` である
  単一の UMLShape の ``ownedElements`` である
  UMLShapes の ``ownedElements`` であるものとする。

B.5 Information Flows
======================================================================
* InformationFlows に関係した UMLDiagramElements についての注意点：

  * InformationFlows が ``modelElements`` である UMLLabels は
    ``conveyed`` の種類の ``names`` を示す。

  * InformationFlows が ``modelElements`` であり、
    ``isIcon`` の値が true である UMLShapes は、
    ``modelElements`` として同じ InformationFlows がある
    UMLEdges と共に重なりつつ整列して、
    黒塗りの三角形として描画するものとし、
    形状は ``informationTarget`` の方を指し示す。

B.6 UML Notations and UML DI Representations
======================================================================
* 本節では UML の表記法が UML DI を利用してどのように
  モデル化される必要があるのかを示すことで付録 B を要約する。

* 付録 B のすべて、または前章までの表記法のすべては網羅しない。

* 左の列は UML の表記法の見本である。
* 中央の列は表記法に対応する UML DI 要素を示す。
  要素は何となく階層的に表現されている。

  * 図式要素の型が与えられ、
    次に括弧内に ``modelElement`` の型が、
    時として図式に適用する他の制約が続く。

    * ひとつの図式に ``modelElement`` の型を
      複数割り当てることが可能なときには
      型名にプラス記号が付く。

* 右の列はその表記法が定義された Notation 節なり Figure なりへの参照である。

B.7 Classifier Descriptions
======================================================================
機械生成による節。

B.8 Association Descriptions
======================================================================
機械生成による節。

.. include:: /_include/uml-refs.txt
