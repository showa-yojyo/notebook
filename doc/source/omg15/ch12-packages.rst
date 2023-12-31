======================================================================
12 Packages
======================================================================

.. contents::
   :depth: 2

12.1 Summary
======================================================================

   Packages provide the main generic structuring and organizing capability of
   UML. There are specializations for Models and for Profiles which organize
   extensions to UML.

12.2 Packages
======================================================================

12.2.1 Summary
----------------------------------------------------------------------

   This sub clause provides the specification for Packages and Models.

12.2.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 12.1 Packages

* Package, Model, PackageMerge が新しく現れた。
* Type も PackageableElement の一種であることが図では省略してある。

``A_packagedElement_owningPackage``
  Package から PackageableElement への複合関連（単方向）。

  * Package は Namespace であり、所有要素を関連端 ``packagedElement`` で表現す
    る。
  * ``A_ownedMember_namespace`` を subsets する。

  ``A_ownedType_package``
    Package から Type への複合関連（双方向）。

    * Type である内容物への参照を表現する関連。
    * ``A_packagedElement_owningPackage`` を subsets する。

  ``A_nestedPackage_nestingPackage``
    Package から Package への複合関連（双方向）。

    * Package である内容物への参照を表現する関連。
    * ``A_packagedElement_owningPackage`` を subsets する。

``A_packageMerge_receivingPackage``
  Package から PackageMerge への複合関連（双方向）。

  * 関連端 ``receivingPackage`` 側の Package が合併前後で構成要素が増える方を指
    す。
  * ``A_ownedElement_owner`` と ``A_source_directedRelationship`` を subsets す
    る。
  * 関連端 ``receivingPackage`` の多重度はちょうど 1 だ。
  * cf. ``A_mergedPackage_packageMerge``

``A_mergedPackage_packageMerge``
  PackageMerge から Package への関連（単方向）。

  * 関連端 ``mergedPackage`` は合併前後でその構成内容物が変わらない方を指す。
  * ``A_target_directedRelationship`` を subsets する。
  * 関連端 ``mergedPackage`` の多重度はちょうど 1 だ。
  * cf. ``A_packageMerge_receivingPackage``

12.2.3 Semantics
----------------------------------------------------------------------

12.2.3.1 Package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A Package is a namespace for its ``members``, which comprise those elements
   associated via packagedElement (which are said to be *owned* or *contained*),
   and those *imported*.

Package 定義は含まれる要素を併合することで他の Package の内容を拡張することが可
能だ。

   A Package may be defined as a template and bound to other templates: see sub
   clause 7.3, Templates, for further information.

   The URI can be specified to provide a unique identifier for a Package.

UML の内側では、プロファイル (12.3.3) を除いて、これに対する決められた使い方はな
い。例えば、モデル管理機能がモデルの識別のために使用することがある。

* URI はなるべく一意であり、一度割り当てられたらなるべく変更されない。
* URI が再参照可能である必要はない（当然これは許容される）。

12.2.3.2 PackageMerge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A PackageMerge is a directed relationship between two Packages that indicates
   that the contents of the target ``mergedPackage`` are combined into the
   source ``receivingPackage`` according to a set of rules defined below.

* 元要素が対象要素の特徴を自身のそれに概念的に追加し、その結果として双方の特徴を
  兼ね合わせた要素になるという意味で Generalization に似ている。
* サブクラスが継承された特徴で通常は叙述されないのと同じように、受信 Package は
  その ``mergedPackage`` から併合した要素で叙述されることは通常ない。
* モデルの意味論上、明示的な PackageMerges を持つモデルと、すべての併合が実行さ
  れたモデルに違いはない。

   Also, as with Generalization, a Package may not merge itself (directly or
   indirectly).

PackageMerge の能力は、異なる Package で定義された要素が同じ ``name`` を持ち、同
じ概念を表すことを意図している場合に使用されるように設計されている。

   A given base concept may be merged for different purposes, with each purpose
   defined in a separate receiving Package. By selecting different receiving
   packages, it is possible to obtain a custom definition of a concept for a
   specific end.

ある基本概念は、異なる目的のために併合されることがあり、各目的は別々の受信
Package で定義される。

受信 Package に含まれるモデル要素への言及は、その Package に含まれる増分ではな
く、併合結果への言及を意味する。これを図示しているのが Figure 12.2 だ。

   Figure 12.2 Illustration of the Meaning of Package Merge

* ``P2::A`` は ``P1::A`` の増分を定義する。
* ``P3::SubA`` は ``P2::A`` のサブクラスの定義だ。``P3`` から見ると、
  ``P2::A`` は ``P1`` と ``P2`` の間のマージ結果の ``A`` を表現していると解釈
  する。
* ``P1``: ``mergedPackage`` (``target``)
* ``P2``: ``receivingPackage`` (``source``, ``owner``) であると同時に
  ``resultingPackage``

マージの ``before``/``after`` で同じところにあるものの呼び方が変わる
(``receiving``/``resulting``) ことがわかればとりあえず読める。

PackageMerge は併合される Package の内容が受け取る Package の内容と結合される操
作（それ自体が変換の集合である）という見方が可能だ。Packages 二つのある要素が
（定義された規則に従って）合致する場合、それらの内容は以下に指定された
PackageMerge の公式規則に従って一つの結果の要素に（概念上）併合される。

   This operation is akin to “copying down” the features of superclasses into a
   subclass: the fully expanded subclass is the equivalent to the resulting
   package.

PackageMerge の規則を理解するには、三種の異なる実体を明確に区別する必要がある：

#. ``mergedPackage`` (e.g. ``P1`` in Fig. 12.2)
#. ``receivingPackage`` (e.g. ``P2``)
#. 合併変換の結果 (also ``P2``)

``receivingPackage`` は ``resultingPackage`` の役割も果たす。同じモデル要素にこ
のような二重の解釈があると混乱するので、理解を助けるために以下の術語を導入する：

併合されたパッケージ (merged package)
  受領パッケージに併合されるパッケージ（図式中の矢印の目標側パッケージ）。
受領パッケージ (receiving package)
  概念上は、併合の結果を含むパッケージ（図式中の矢印の起点側パッケージ）であるの
  だが、この用語は併合変換が実施される前のパッケージおよびその中身を指すのに用い
  る。
結果パッケージ (resulting package)
  概念上は、併合の結果を含むパッケージだ。モデルでは当然ながらこれは受領パッケー
  ジと同じパッケージだが、この特定の用語は併合変換が実施された後のパッケージおよ
  びその中身を指すのに用いる。
併合された要素 (merged element)
  併合されたパッケージに存在するモデル要素を指す。
受領要素 (receiving element)
  受領パッケージにあるモデル要素。
結果要素 (resulting element)
  併合が実施された後の結果パッケージにあるモデル要素。は、受信パッケージのモデル
  要素です。その要素に合致する（以下に定義する）併合された要素がある場合、その二
  つが結合されて結果要素が生成される（後述）。この用語は、併合が実行される前の要
  素を指すために用いる（「結果」と言っているが「実行される前の」だ）。
要素型 (element type)
  Parameter や StructuralFeature の ``type`` のような、TypedElement のあらゆる種
  類の ``type`` を指す。
要素メタタイプ (element metatype)
  モデル要素の :abbr:`MOF` 型だ。例えば Classifier, Association, Feature だ。

   Figure 12.3 Conceptual View of the Package Merge Semantics

* 図の右側は UML の図式ではない。
* この ``B`` ダッシュを意識することがコツだと言っている。

PackageMerge の意味は制約と変換の集合で定義される。制約は有効な PackageMerge に
に対する事前条件を指定し、一方、変換はその意味上の効果（事後条件）を記述する。制
約がいくつか違反していれば PackageMerge は ill-formed であり、それを含むモデル
は無効だ。

   Different element metatypes have different semantics, but the general
   principle is always the same

結果の要素は併合する前よりも能力が低下することはない。例えば、PackageMerge の結
果として、受け取るモデル要素の回航可能性、多重度、可視性等々が低下することはない
ことを意味する。

   One of the key consequences of this is that model elements in the resulting
   Package are compatible extensions of the corresponding elements in the
   (unmerged) receiving package.

本仕様では、明示的な合併変換は一定の一般的メタモデル (Packages, Classes,
Associations, Properties, etc.) に対してしか定義していない。他の種類の要素メタタ
イプ（例えば状態機械や相互作用）の意味が複雑かつ領域固有であるので、このような変
換はできない。

   Elements of all other kinds of metatypes are transformed according to the
   *default rule*: they are simply deep copied into the resulting package. (This
   rule can be superseded for specific metatypes through profiles or other kinds
   of language extensions.)

12.2.3.3 General Package Merge Rules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

併合される要素と受領要素が合致する (to match) とは、以下の規則群を満たすことを言
う。

CONSTRAINTS
  #. ``«merge»`` 有向グラフに閉路があることは不可能だ。
  #. Package は（直接または間接的に ``owningPackage`` を介して）その Package を
     含む Package を併合することは不可能だ。
  #. Package はそれが含む Package を（直接または間接的に ``packagedElement`` を
     介して）併合することは不可能だ。
  #. メタタイプが Package, Class, DataType, Property, Association, Operation,
     Constraint, Enumeration, EnumerationLiteral の一種ではないような併合された
     要素には、その受領要素が併合された要素の厳密な複製ではない限りは、同じ名前
     とメタタイプを持つ受領要素を持つことは不可能だ。
  #. PackageMerge は併合を実施するのに要求される制約のすべて（この一覧）が成り立
     つとき、かつそのときに限り有効だ。
  #. 合致する型付けられた要素 (e.g., Properties, Parameters) は、適合する型であ
     る必要がある。Classes またはDataTypes 型の場合、適合型とは同一型あるいは共
     通上位型のいずれかだ。それ以外の場合では、適合とは型が同一でなければならな
     いことを意味する。
  #. 受領要素は併合された要素へのどれに対しても明示的な参照があることは不可能
     だ。
  #. 合致する RedefinableElements に関連する再定義は、いずれも矛盾してはならな
     い。

TRANSFORATIONS
  #. （既定の規則）合致する要素のない合併された要素または受領要素は結果の
     Package の中に deep copy される。
  #. 名前とメタタイプが合致し、互いに完全な複製である二つの要素を合併した結果が
     受領要素だ。
  #. 合致した要素はそれらのメタタイプに固有の変換規則に従って結合され、結果は生
     じる Package に含まれる。
  #. 結果パッケージに行き着く型付き要素に対する型参照のすべては、対応する結果
     TypedElements への参照に変換される。それぞれの増分への参照ではない。
  #. 合致する要素全てに対して：

     合致する要素の両方とも private ``visibility`` である場合、結果要素の
     ``visibility`` は private だ。それ以外の場合には、結果要素の ``visibility``
     は public ということになる。
  #. 合致する Classifier 要素全てについて：

     合致する要素が両方とも ``isAbstract`` が真の場合、結果要素は ``isAbstract``
     が真だ。それ以外の場合には、結果要素は ``isAbstract`` が偽だ。
  #. 合致する要素全てについて：

     合致する要素が両方とも ``isFinalSpecialization`` が真である場合、結果要素は
     ``isFinalSpecialization`` が真だ。それ以外の場合には、結果要素は
     ``isFinalSpecialization`` が偽だ。
  #. 合致する要素全てについて：

     合致する要素の両方とも導出されない場合、結果要素もまた導出されない。そうで
     なければ、結果要素は導出される。
  #. 合致する MultiplicityElements 全てに対して：

     結果要素の境界 ``lower`` は合致する要素の境界 ``lower`` のうち、小さいほう
     だ。
  #. 合致する MultiplicityElements 全てに対して：

     結果要素の境界 ``upper`` は合致する要素の境界 ``upper`` のうち、大きいほう
     だ。

  #. 併合される要素か受領要素の一方のモデル要素に適用されるステレオタイプは、ど
     れも対応する結果要素にも適用される。
  #. 合致する RedefinableElements の場合：

     合致する RedefinableElements の異なる再定義は、すべて結果要素に適用される。
  #. 合致する RedefinableElements の場合：

     合致する要素の両方とも ``isLeaf`` が真の場合、結果要素も ``isLeaf`` が
     真だ。それ以外の場合には結果要素は ``isLeaf`` が偽だ。

12.2.3.4 Package Rules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Elements that are kinds of Package match by ``name`` and metatype.

CONSTRAINTS
  #. 併合された Package にある Classifiers のすべては、空でない ``qualifiedName``
     がある必要があり、合併された Package で ``isDistinguishableFrom()`` の値が
     真である必要がある。
  #. 受領 Package にある Classifiers すべては、空でない ``qualifiedName`` がある
     必要があり、受領 Package で ``isDistinguishableFrom()`` の値が真である必要
     がある。

TRANSFORATIONS
  #. 併合された Package の ``nestedPackage`` は受領 Package が合致する
     ``nestedPackage`` をすでに含んでいない限り、結果 Package で同じ ``name`` と
     同じ内容を持つ ``nestedPackage`` に変換される。
  #. 受領 Package の ``elementImport`` である ElementImport は、結果 Package に
     おいて対応する ElementImport に変換される。（インポートされた要素を所有する
     Package への PackageMerge が存在しない限り）インポートされた要素は併合され
     ない。

12.2.3.5 Class and DataType Rules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Elements that are kinds of Class or DataType match by ``name`` and metatype.

TRANSFORATIONS
  #. 併合された Classifier の ``ownedAttributes`` である Properties はすべて、下
     に規定する Property 変換規則に従って、受領 Classifier に併合されて、結果
     Classifier を生成する。
  #. ``nestedClassifiers`` は同じ規則に従って再帰的に併合される。

12.2.3.6 Property Rules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Elements that are kinds of Property match by ``name`` and metatype.

CONSTRAINTS
  #. 合致する Properties の ``isStatic`` の値が同じである必要がある。
  #. 合致する Properties の ``isUnique`` の値が同じである必要がある。
  #. 合致する Properties に関連する Constraints のいずれも競合していない必要があ
     る。

TRANSFORATIONS
  #. 合致する受領 Property のない併合された Properties の場合は、結果 Property
     は併合された Property と同じ結果 Classifier の Property となる。
  #. 合致する受領 Property を有する併合された Properties の場合は、結果 Property
     は同じ名前と特徴がある Property だ。これらの特徴が異なる場合、結果 Property
     の特徴は適切な変換規則の適用により決定される。
  #. 合致 Properties について：

     両方の Property で ``isReadOnly`` が真である場合、結果 Property でも
     ``isReadOnly`` が真だ。そうでない場合は結果 Property では ``isReadOnly`` が
     偽だ。
  #. 合致 Properties について：

     両方の Property で ``isOrdered`` が偽である場合、結果 Property でも
     ``isOrdered`` が偽だ。そうでない場合は結果 Property では ``isOrdered`` が真
     だ。
  #. 合致 Properties について：

     どの Property もある導出和集合の部分集合として指定されていない場合、結果
     Property はその導出和集合の部分集合として指定されない。
  #. 合致 Properties について：

     合致 Properties の異なる制約が、結果 Property にすべて適用される。
  #. 合致 Properties について：

     併合された要素と受領要素の両方またはどちらか一方で ``isUnique`` が偽である
     場合、結果要素は ``isUnique`` が偽であり、そうでなければ結果要素は
     ``isUnique`` が真だ。
  #. 結果 Property に対する ``type`` の値は、結果 Package の対応する ``type`` を
     参照するよう変換される。

12.2.3.7 Association Rules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Elements that are kinds of Association match by ``name`` and metatype.

CONSTRAINTS
  #. これらの規則は二項 Association にしか適用しない。一般の多項 Association の
     併合には既定規則を適用する。
  #. 合致する併合された関連端の ``aggregation`` が composite であると、受領関連
     端でも ``aggregation`` が composite である必要がある。
  #. 合致する併合された関連端が Association により所有されている場合、受領関連端
     はその Association がり所有する必要がある。

TRANSFORATIONS
  #. 合致する Associations の併合は、Classifiers についての規則に従いAssociation
     classifiers を併合し、対応する ``ownedEnd`` Properties を、Propertyes の規
     則と Association 端子の次の規則に従い併合することで達成される。
  #. 合致する関連端の場合：

     どの関連端も ``ownedNavigableEnd`` にない場合、結果関連端も
     ``ownedNavigableEnd`` にはない。それ以外の場合には、結果関連端は
     ``ownedNavigableEnd`` に含まれる。

12.2.3.8 Operation Rules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Elements that are kinds of Operation match by ``name``, Parameter order, and
   Parameter types, not including any return type.

CONSTRAINTS
  #. Operation Parameters とその型は、Properties の定義と同じ型の多重度に対する
     規則に従う必要がある。
  #. 合致する合併された Operation の ``isQuery`` が真の場合、受領 Operation は
     ``isQuery`` が真である必要がある。

TRANSFORATIONS
  #. 合致する受領 Operation のない併合された Operations の場合は、結果 Operation
     は結果 classifier において同じ名前と同じ署名である Operation だ。
  #. 合致する受領 Operation のある併合された Operations の場合は、結果 Operation
     は合致する併合された Operations と受領 Operations の併合結果であり、
     Parameter 変換は上で定義された Property 変換に従って実施される。

12.2.3.9 Enumeration Rules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Elements that are kinds of EnumerationLiteral match by owning Enumeration and
   Literal ``name``.

CONSTRAINTS
  #. 合致する EnumerationLiterals は同じ順序である必要がある。

TRANSFORATIONS
  #. 併合された Enumeration 由来の非合致 EnumerationLiterals は受領 Enumeration
     に含まれる。

12.2.3.10 Constraint Rules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

CONSTRAINTS
  #. Constraints は互いに矛盾があってはならない。

TRANSFORATIONS
  #. 併合されたモデル要素の Constraints はすべて受領モデル要素の Constraints に
     加わる。

12.2.3.11 Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A Model is a description of a system, where ‘system’ is meant in the broadest
   sense and may include not only software and hardware but organizations and
   processes.

* Model は特定の関係者 (certain category of *stakeholders*) のために、ある視点か
  ら、ある抽象度で記述される。
* Model は目的に関連する側面だけが表現されているが、システム全体を網羅している
  という意味で完全だ。

   As a Package, a Model has a set of ``members`` that together describe the
   system being modeled. The organization of these elements varies by the
   modeling method being used.

Model にはシステムの環境の関連部分を記述する要素を含むことがある。

   The environment is typically modeled by Actors and their Interfaces. As these
   are external to the system, they reside outside the Package/Component
   hierarchy. They may be collected in a separate Package, or owned directly by
   the Model as ``packagedElements``.

同じシステムに対して種々の Models を定義することが可能であり、典型的にはこの
Models は相補的であり、種々のシステム利害関係者の観点から定義される。

   With composition of Models, a container model represents a comprehensive view
   of the system given by the different views defined by the contained Models.

   Models can have Abstraction Dependencies between them: refinement
   (stereotyped by ``«Refine»`` from the Standard Profile) or mapping (for
   example stereotyped by ``«Trace»`` from the Standard Profile).

* ``refinement`` （標準プロファイル ``«Refine»`` でステレオタイプされる）
* ``mapping`` （例えば標準プロファイル ``«Trace»`` でステレオタイプされる）

これらは、通常、Model に含まれる要素間の Dependencies によってより詳細に表現され
る。Model それぞれが完全であることを意図しているため、異なる Models の要素間の
Relationships は通常、Models の内容に直接的な影響を与えない。しかし、改良をな
ぞったり、モデル間の相互参照を追跡したりするのに便利だ。

12.2.4 Notation
----------------------------------------------------------------------

Package は大きい矩形であって、その左上に小さい矩形（タブ）を付けた形状で示す。

* Package の ``members`` を大きい矩形の内部に示すことがある。また、Package の外
  部に描かれた ``member`` への分岐線で示すこともある。
* Package に付属する端子には円内にプラス記号 ``+`` が描かれる。

..

   Conformant tools may restrict the use of these notations to
   ``packagedElements``. Optionally, elements that become available for use in
   an importing Package through a PackageImport or an ElementImport may have a
   distinct color or be dimmed to indicate that they are not
   ``packagedElements``.

* Package の ``members`` が大きな矩形の中に表示されていない場合、Package の
  ``name`` を大きな矩形の中に入れる必要がある。
* Package の ``members`` が大きな矩形の中に表示されている場合、Package の
  ``name`` はタブに入れる必要がる。

   The ``visibility`` of a ``packagedElement`` may be indicated by preceding the
   ``name`` by a visibility symbol (``+`` for public and ``-`` for private).

Packages の可視性が protected や package であることは許されない。

   A tool may show visibility by a graphic marker, such as color or font. A tool
   may also show ``visibility`` by selectively displaying those elements that
   meet a given visibility level (e.g., only public elements). A diagram showing
   a Package with ``members`` need not necessarily show all its ``members``; it
   may show a subset of the ``members`` according to some criterion.

   The ``URI`` for a Package may be indicated with the text ``{uri = <uri>}``
   following the Package ``name``.

PackageMerge は開いた鏃の破線矢印を用いて示す (Figure 12.4)。

  * 矢印の向きは ``receivingPackage`` から ``mergedPackage`` だ。
  * キーワード ``«merge»`` を破線のそばに示す。

Model は通常の Package シンボルに小さな三角を大矩形の右上隅に描いたもので記す。

特に Model の ``members`` が大矩形の中に表示されている場合、タブ内の Model
``name`` の右側に三角形を描いてもよい。

A Model may also be notated as a Package, using the ordinary Package symbol with
the keyword ``«model»`` placed above the ``name`` of the Model.

12.2.5 Examples
----------------------------------------------------------------------

   Figure 12.5 Examples of a Package with Members

* 左側のものはただ Package を表示している。
* 中央のものは Package の矩形の境界内にある ``members`` の一部を示している。
  ついでに `URI`` も表示。
* 右のものは代替の所有権表記を使用して ``members`` の一部を示している。

どの図式でも Package の内容物がすべて記されているとは限らないようだ。マルプラス
の見本によると、線のスタイルは実線。

   Figure 12.6 Simple Example of Package Merge

もっとも基本的な見本と思われる。P と Q は R によって併合され、S は Q のみを併合
している。

   Figure 12.7 Simple Example of Transformed Packages Following the Merges

上述の結果、各パッケージがどういう構成になるかを模式化したもの。

* 角括弧内の式（説明目的の記号であって UML ではない）は最終結果を生成するために
  どの要素が併合されたかを示す。
* ``@`` は演算子としての概念的併合変換を示す。
* ``X@Y`` は受領要素 ``X`` と併合された要素 ``Y`` の合致に適用される併合変換から
  の結果要素を表す。

   Figure 12.8 Introducing Additional Package Merges

それ自身の ``packagedElements`` を所有しない Package ``T`` が、先に定義された
Package ``R`` と ``S`` を併合することで、追加的 PackageMerge が導入される。

   Figure 12.9 Result of the Additional Package Merges

上述の ``T`` のマージ状態を模式化したもの。

この Package では ``A``, ``B``, ``C``, ``D`` の定義はすべて一緒にされた。
Package ``Q`` と ``S`` に元々あった Associations の末端の型は、Package ``T`` の
適切な要素を参照するようにすべて更新された。

   Figure 12.10 Three Models Representing Parts of a System

``Client``, ``Business``, ``Data`` からなる三層構造システムの Models の図式。

   Figure 12.11 Two Views of One System Collected in a Container Model

Models-in-Model な図式。同一図式内にあえて異なる記法（キーワード or 小三角）を併
用している。

12.3 Profiles
======================================================================

12.3.1 Summary
----------------------------------------------------------------------

   The Profiles clause describes capabilities that allow metaclasses to be
   extended to adapt them for different purposes.

これは J2EE や .NET 等のさまざまなプラットフォームや領域（リアルタイムまたはサー
ビス志向様式）に UML メタモデルを合わせる能力も含む。

この節 (12.3) は OMG MOF_ に対する整合性がある。

12.3.1.1 Positioning Profiles versus Metamodels, MOF and UML
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   UML is reused at several meta-levels in various OMG specifications that deal
   with modeling.

MOF_ に匹敵する use cases を他の上部構造仕様よりもワンランク上の水準であるメタメ
タレベルで扱う。これを可能にするため、参照メタモデルを MOF_ を用いた定義に対応す
る UML のオブジェクトとして定義する必要がある。したがって、UML プロファイル を定
義する場合、プロファイルのステレオタイプは :doc:`./ane-serialization` で定義され
る。XMI シリアライズが参照されている UML メタモデルの規範版の UML クラスを拡張す
るように。

   Profiles are not a first-class extension capability (i.e., it does not allow
   for creating new metamodels). Rather, the intention of Profiles is to give a
   straightforward mechanism for adapting an existing metamodel with constructs
   that are specific to a particular domain, platform, or method.

* そのような adapting それぞれは Profile にまとめられる。
* Profile を使用して UML に適用される Constraints を削除することは不可能だが、
  Profile に固有の新しい Constraints を追加することは可能だ。他の制限はこの
  Profiles 節に固有のものしかなく、メタモデルをカスタマイズする方法を制限するこ
  とを意図したものは他にない。

   First-class extensibility is handled through MOF_, where there are no
   restrictions at the metamodel level: it is possible to add subclasses and
   associations as necessary.

UML を拡張したくなる理由：

* 特定のプラットフォームやドメインに適合した用語法 (a terminology) を与える。
* 記法のない諸構成概念 (e.g. Action) に構文を与える。
* 既存の諸記号に別の記法を与える。例えばネットワーク内の計算機を表すのに、いつも
  の Node 記号に代わり計算機の絵を使えるようにするなど。
* UML や特定のメタクラスに対してさらなる意味を追加する。
* UML に存在しない型を追加する。例えば連続時間など。
* UML の諸構成概念の用途を制限する Constraints を追加する。例えば多重継承を禁じ
  るなど。
* モデルを別のモデルやコードに変換する際に用いることが可能な情報を追加する。
  例えばモデルと Java コードの間の写像規則の定義など。

いつ新しいメタモデルを作成するべきか、いつプロファイルを作成するべきか、あるいは
いつ両者を（一方は UML ツール用、もう一方は MOF_ ベースのツール用に）作成するべ
きかという問いに対して、簡単な答えはない。

12.3.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 12.12 Profiles

一見するとグラフの構造がいつもより込み入っている。

新クラスは Profile, ProfileApplication, Stereotype, Image, Extension,
ExtensionEnd と、いつもより多く登場する。

``A_metaclassReference_profile``
  Profile から PackageImport への複合関連（単方向）。

  * ``A_packageImport_importingNamespace`` を subsets する。
  * cf. ``A_metamodelReference_profile``

``A_metamodelReference_profile``
  Profile から ElementImport への複合関連（単方向）。

  * ``A_elementImport_importingNamespace`` を subsets する。
  * cf. ``A_metaclassReference_profile``

``A_appliedProfile_profileApplication``
  ProfileApplication から Profile への関連（単方向）。

  * Package に適用されている Profile を参照する関連だ。
  * ``A_target_directedRelationship`` を subsets する。
  * cf. ``A_profileApplication_applyingPackage``

``A_profileApplication_applyingPackage``
  Package から ProfileApplication への複合関連（双方向）。

  * Package が Profile 適用情報を所有する。
  * ``A_source_directedRelationship`` と ``A_ownedElement_owner`` を subsets す
    る。
  * cf. ``A_appliedProfile_profileApplication``

``A_profile_stereotype``
  Stereotype から Profile への関連（単方向）。

  * 自らを直接的にまたは間接的に含む Profile への参照を示す。
  * 関連端 profile は ``{readOnly}`` だ。
  * 関連端 profile の多重度は 1 だ。

``A_icon_stereotype``
  Stereotype から Image への複合関連（単方向）。

  * Stereotype を図式内でアイコンイメージを用いて表示する際、
    その中身の場所を参照する。
  * ``A_ownedElement_owner`` を subsets する。

``A_ownedStereotype_owningPackage``
  Package から Stereotype への複合関連（単方向）。

  * ある適用済み Profile が直接る Stereotype を所有するという意味か。
  * ``A_packagedElement_owningPackage`` を subsets/redefines する。
  * 関連端 ``ownedStereotype`` は ``{readOnly}`` だ。

``A_ownedEnd_extension``
  Extension から ExtensionEnd への複合関連（単方向）。

  * 拡張されているメタクラスへの参照する。
  * ``A_ownedEnd_owningAssociation`` を redefines/subsets する。

``A_extension_metaclass``
  Class から Extension への関連（双方向）。

  * メタクラスを拡張する Stereotype を参照する関連端を所有する。
  * 関連端は両方とも ``{readOnly}`` だ。
  * 関連端の多重度は ``metaclass`` が 1 に対して ``extension`` が ``*`` だ。

``A_type_extensionEnd``
  ExtensionEnd から Stereotype への関連（単方向）。

  * メタクラスを拡張する Stereotype を参照する。
  * ``A_type_typedElement`` を redefines/subsets する。

12.3.3 Semantics
----------------------------------------------------------------------

12.3.3.1 Profiles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A Profile is a restricted form of metamodel that can be used to extend UML,
   as described below.

主な拡張構成要素は Stereotype だ。

12.3.3.1.1 Restricting Availability of UML Elements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   The ``metaclassReference`` ElementImports and ``metamodelReference``
   PackageImports may be used to specify the Profile’s filtering rules. The
   filtering rules determine which UML elements are *available* when the Profile
   is applied and which ones are *hidden*.

注意：あるモデルに Profile を適用しても、そのモデルは何ら変更されない。Profile
は根底にあるモデルのビューを単に定義するだけだ。

メタクラスが隠される（利用不能となる）ことの影響は次のとおり：

* 当該メタクラス（またはそのサブクラス）のオブジェクトを新たに生成することは不能
  になる。
* 当該メタクラス（またはそのサブクラス）の既存のオブジェクトを、図式上で表示した
  り、ブラウザー枠内を含む、リストで選択したりが不能になる。
* 当該メタクラス（またはそのサブクラス）の既存のオブジェクトに関する
  Relationships は図式上で表示したり、ブラウザー枠内を含むリストで選択したりが不
  能になる。

上記で言う「隠す」をどのように実装するかはツールによって異なる場合がある。

Profile の選別規則（後述）を作動させるには、Profile を厳格モードで適用する必要が
ある：

   specifically the ``isStrict`` attribute on the ProfileApplication must be set
   to true; otherwise the filtering rules are ignored for this profile
   application.

最も一般的な事例は、Profile が ``metamodelReference`` を使って UML 自身をイン
ポートする場合だ。

   A conformant tool may provide this as built-in behavior when the user creates
   a Profile. In that case, every UML metaclass is available.

* あるいは、特定のメタクラスを ``metaclassReferences`` を通して参照することもで
  きる。その場合、それらだけが利用可能だ。
* さらなる選択肢は、UML メタクラスの部分集合の ElementImport を含む Package(s)
  への一つ以上のメタモデル参照を使うことだ。

ElementImports の ``visibility`` および ``alias`` 特性は ``metaclassReference``
として用いられるときには無視される。


``metaclassReference`` と ``metamodelReference`` の両方が Profile に存在する場
合、後者は無視されて特定のメタクラスだけが使用可能になる。

詳しくは、Profile が厳格モードで適用された後に、モデル要素が利用可能かどうかを決
定するのに次の規則が使われる。メタクラスおよびそのオブジェクトが利用可能であるの
は、

#. 明示的な ``metaclassReference`` により参照されるか、
#. ``metaclassReference`` がない場合、明示的な ``metamodelReference`` により参照
   される Package の直接的または推移的な ``members`` であるか、
#. （拡張されたメタクラスが利用できない場合であっても、）適用される Profile の
   ``member`` である Stereotype によって拡張されているときだ。

..

   All other model elements are *hidden* (not available) when the Profile is
   applied in Strict mode.

このため、利用可能なメタクラスの重複しない集合を指定する適用プロファイルの組み合
わせは無効となる。

Profile ``P1`` が別の Profile ``P2`` をインポートすると、``metaclassReference``
と ``metamodelReference`` の関連すべてが ``P1`` の水準で結合され、選別規則がこの
和集合に適用する。

   Stereotypes imported from another Profile using ElementImport or
   PackageImport are added to the namespace members of the importing
   profile.Profile Contents.

Profile は Stereotypes ばかりでなく Classes, Associations, DataTypes,
PrimitiveTypes, Enumerations を定義またはインポートすることができる。

   More precisely all the constraints of a CMOF-compliant metamodel apply to a
   UML Profile. These are defined in detail in Section 14.4 of the MOF_ Core
   Specification. The effect of these constraints is that, except for
   Stereotypes and Extensions, all other Types defined or imported in a Profile
   must be exactly one of the Types explicitly mentioned in the above subset and
   that no specialization outside this subset is allowed.

Profile-defined Type という用語は、Profile で定義またはインポートされた CMOF 準
拠の Class, Association, DataType, PrimitiveType, Enumeration に相当する。

   Profile-defined Types can only be used as the type of Properties in that
   Profile or as a general classifier of another Profile-defined Type.

これらは TypedElement の型、InstanceSpecification の classifier, Generalization
関係の一般または特殊 classifier など、Profile が適用されるモデルの Types として
使用することは不可能だ。しかし、これらの型を別の Packageで定義し、Profile とモデ
ル Package の両方で必要に応じてインポートすることで、両方の目的で使用することは
可能だ。

   Stereotypes can participate only in binary Associations. The opposite class
   can be another Stereotype, a non-Stereotype Class that is a
   ``packagedElement`` of a Profile (directly or indirectly), or a UML
   metaclass.

これらの Associations には、反対側のクラスによって型付けられる ``ownAttribute``
特性必要だ。反対側のクラスがステレオタイプでない場合、反対側の特性は他の
クラス・メタクラスではなく、Association 自体の ``ownMember`` でなければならない。

* これらの規則の効果として、Profile 内の Associations は Stereotype を含む必要は
  ないが、その両端を所有してはならない。
* Profile-defined 二項 Association は ``aggregation =
  AggregationKind::composite`` を持つ端子を高々一つ持つことができ、他方の端子は
  ``aggregation = AggregationKind::none`` でなければならない。
* さらに、Stereotype または Profile-defined Class の Property は、その型が
  Profile-defined Class である場合かつその場合に限り、複合集約を持つことが可能で
  あり、Stereotype または Profile-defined Class または DataType の Property は、
  その型が Profile-defined DataType, PrimitiveType, Enumeration のいずれかである
  場合、``aggregation = AggregationKind::none`` を持つ必要がある。

..

   The most direct implementation of the Profile capability that a tool can
   provide is by having a metamodel based implementation, similar to the Profile
   metamodel. However, this is not a requirement of the current standard, which
   requires only the support of the specification, and the standard XMI based
   interchange capacities.

Profile 機能はメタモデルベースの実装を持たないツールでも実装可能なように設計され
ている。

新しい値をモデル要素に取り付けるために用いられる実質的にあらゆる仕組みが、有効な
プロファイル実装として機能することが可能だ。

しかし、そのような値を作成するには、Profile-defined Class や DataTypes のオブ
ジェクトを作成し、その Class や DataTypes が型付ける Properties の値として参照
し、また Profile-defined Association のリンクオブジェクトを作成するために
Profile-defined Class のオブジェクトを参照する、メタモデルとしての限定された機能
が必要となる。

12.3.3.1.2 Integrating and Extending Profiles
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   There is a number of ways to create, extend, and integrate Profiles.

Profile 統合の最も単純な形式は、複数 Profiles を同じ Package に適用するだけだ。

   It is also possible for one Profile to reuse all of or parts of another, and
   to extend other Profiles.

* 他の Class と同様に、Stereotypes も Packages や Profiles で定義することがで
  き、再利用のために共通要素を括ることが可能だ。これらの Stereotypes は他の
  Profiles で参照されたり特殊化されたりすることで、直接再利用することが可能だ。
* 被参照 Stereotype が拡張 Profile の利用者に見えるかどうかについては通常の規則
  が適用される：拡張 Profile を適用した後に他の Profiles の Stereotype が見える
  ようにするには public import が必要だ。

例えば、*Unified Profile for DoDAF and MODAF* (UPDM) Profile は、SysML Profileと
統合して、Requirement や ViewPoint などの Stereotypes を再利用することも可能だろ
う。UPDM は SysML と意味的に整合する方法で ViewPoint を使用するように設計するこ
とも可能だろう。しかし、UPDM はその目的のために特性や関連を追加して ViewPoint を
拡張することも可能だろう。

   The UPDM specification could note to users that ViewPoint is a stereotype in
   UPDM that represents a "placeholder" to ViewPoint in SysML. Users could then
   apply UPDM to a model, and get UPDM's ViewPoint capabilities without any
   coupling with, or need for SysML. UPDM could then provide another compliance
   point that merges with the SysML profile resulting in stereotypes Requirement
   and ViewPoint having the capabilities of both profiles. The SysML::ViewPoint
   would be merged with the UPDM::ViewPoint allowing the shared semantics to be
   supported without making any changes to the existing model.

SysML を含む UPDM を希望する利用者は、この併合された Profile を適用することにな
るだろう。

12.3.3.1.3 MOF-Equivalent Semantics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   This sub clause specifies the semantics of Stereotypes and their instances
   using MOF_.

MOF_ を使用しない実装では、観測可能なすべての方法で、MOF_ の実装であるかのように
動作するように、舞台裏で必要なことを行わなければならないことの意味にとること。

   The same mapping to MOF_ is used to determine how to serialize applied
   profiles using XMI. A Profile is an instance of the UML2 metamodel, not a
   CMOF metamodel. Therefore the MOF to XMI mapping rules do not directly apply
   for instances of a Profile.

Figure 12.15 は、UML2 Profile と同等の CMOF モデルとの間の写像の例だ。この
写像は Profile が XMI としてシリアライズされ、交換される方法を説明し、正式に
指定する手段として使用される。

以下の Profile to CMOF 写像規則を使用すると、XMI 仕様を使用して、Profile および
Profile を適用したモデルが XMI でどのように表現されるかを決定することができる。
写像の中では：

* Profile は CMOF Package に写る。
* Stereotype は、同じ名前と特性を持つ CMOF クラスに写る。
* Metaclass はすでに CMOF クラスなので、それ自身に写る。
* Extension は Association に写る。Extensions 節の Semantics 参照。
* Profile に含まれるその他の要素 (Stereotype 以外の Classes, DataTypes,
  PrimitiveTypes, Enumerations, Associations) は MOF_ 要素として扱われる。
* Stereotype のオブジェクトは Stereotype を表現する CMOF クラスのオブジェクトに
  写る。

     This stereotype instance is compositionally associated with the Element to
     which it applies using a Link that is an instance of the composite
     Association to which the Extension is mapped.

Profile の場合、``URI`` Property は XMI で Profile のオブジェクトを識別するのに用
いられる ``nsURI`` を決定するために用いられる。

   NOTE. By default the ``name`` attribute of the Profile is used for the
   nsPrefix in XMI but this can be overridden by the CMOF tag
   org.omg.xmi.nsPrefix.

UML Standard Profile のような OMG 標準 Profile は、URI の OMG 標準命名法に従って
いる。

   For non-standard profiles a recommended convention is:

   .. code:: text

      nsUri = http://<profileParentQualifiedName>/<version>/<profileName>.xmi
      nsPrefix = <profileName>

* ``<profileParentQualifiedName>`` は Profile を含む Package の修飾名で（もしあ
  れば）、``/`` は ``::`` に置き換えられ，他のすべての不正な XML QName 文字は削
  除される。
* ``<version>`` はバージョン識別子だ。

  OMG 標準プロファイルの場合、これは YYYYMMnn の形式の日付であり、XMI に影響を与
  えずに再発行されるかもしれない仕様ではなく、プロファイル XMI のバージョンを表
  す。
* ``<profileName>`` はプロファイルの ``name`` だ。

Profile は他のモデルと同様に XMI ファイルとして交換可能であり、Profile が適用さ
れたモデルもまた相互に交換可能だ。

Figure 12.19 は UML2 のメタクラスである Interface を拡張した ``Home`` という名前
の Stereotype だ。Figure 12.15 はその例の MOF_ 対応を示すもので、基本的には
``Home`` MOF_ クラスから Interface MOF_ クラスへの Association を導入している。
説明目的で ``Home`` Stereotype に Property ``magic:String`` を加えている。

以下の最初のシリアライズは、Figure 12.19 のモデル（UML2 メタモデルを拡張したプロ
ファイルの定義）がどのように交換されるかを示している。

.. code::xml

   <?xml version="1.0" encoding="UTF-8"?>
   <xmi:XMI xmlns:xmi=http://www.omg.org/spec/XMI/YYYYMMnn ...>
      <uml:Profile xmi:id="id0" xmi:type="uml:Profile" name="HomeExample">
         ...
      </uml:Profile>
      ...
   </xmi:XMI>

..

   Figure 12.13 Using the HomeExample Profile to Extend a Model

ステレオタイプ ``Home`` で拡張された Interface のオブジェクトを含むモデル。

.. admonition:: 読書ノート

   シリアライズの記述が節の終わりまで続くのを割愛。

12.3.3.2 Defining Profiles for Non-UML Metamodels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Profiles 機能を使用して UML 以外のメタモデルの拡張を定義することが理論上可能だ。
そのメタモデルを実装するツールは、何らかのプロファイル適用機構を対処する必要があ
るだろう（本仕様の範囲外）。Profile 定義機構をこのやり方で利用する方法が以下に述
べられる。

   In addition to UML, a Profile may be related to another MOF_-compliant
   *reference metamodel*. In general a reference metamodel typically consists of
   metaclasses that are either imported or locally owned. All metaclasses that
   are extended by a profile have to be members (directly or indirectly) of the
   same reference metamodel. The ``metaclassReference`` ElementImports and
   ``metamodelReference`` PackageImports serve two purposes:

#. プロファイルによってインポートされる参照メタモデル要素を識別し、
#. Profile の選別規則を指定する。選別規則は Profile が適用されたときにメタモデル
   のどの要素が利用可能 (available) で、どの要素が隠匿 (hidden) されるかを決定す
   る。

..

   NOTE. Applying a Profile does not change the underlying model in any way; it
   merely defines a view of the underlying model.

先にもこれを記した気がする。

   In general, only model elements that are instances of imported reference
   metaclasses will be visible when the profile is applied. Instances of all
   other metaclasses will be hidden and further instances may not be created.

何もしなければメタクラスが参照メタモデルによって所有されているモデル要素が目に見
える。これはパッケージインポートの既定規則に従って、参照メタモデルのあらゆる部分
パッケージに推移的に適用される。

   If any metaclass is imported using a ``metaclassReference`` ElementImport,
   then model elements whose metaclasses are the same as that metaclass are
   available. However, a ``metaclassReference`` blocks a ``metamodelReference``
   whenever an element or Package of the referenced metamodel is also referenced
   by a metaclass reference. In such cases, only the elements that are
   explicitly referenced by the metaclassReference will be visible, while all
   other elements of the metamodel Package will be hidden.

このような場合、``metaclassReference`` によって明示的に参照されている要素しか目
に見えず、メタモデル Package の他の全ての要素は隠匿される。

   The following rules are used to determine whether a model element is
   available or hidden after a Profile has been applied. Model elements are
   *available* if they are instances of metaclasses that are:

#. 明示的な ``metaclassReference`` により参照されるか、
#. 明示的な ``metamodelReference`` により参照される Package に（直接的または推
   移的に）含まれるか、
#. 適用された Profile が所有する Stereotype により拡張されている（拡張されたメタ
   クラス自体が見えない場合であっても）。

..

   All other model elements are hidden (not available) when the Profile is
   applied.

最も一般的な場合は、Profile が ``metamodelReference`` を使用してメタモデル全体を
インポートする場合だ。この場合、メタモデル内のメタクラスをオブジェクト化するすべ
ての要素が見える。

   Figure 12.14 Specification of an Available Metaclass

* ``MyMetamodel`` は二つのメタクラス ``Metaclass1`` と ``Metaclass2`` を含むメ
  タモデルだ。
* ``MyProfile`` は ``MyMetamodel`` と ``Metaclass2`` を参照する Profile だ。
* ``Metaclass2`` に対する明示的なメタクラス参照もある。これはメタモデル参照を上
  書きする。
* ただし、Metaclass2 への明示的なメタクラス参照もあり、これはメタモデル参照を
  オーバーライドします。
* ``MyProfile`` を ``MyMetamodel`` に基づく何らかのモデルに適用する
  と、``Metaclass2`` のオブジェクトが表示される。``Metaclass2`` は明示的なメタク
  ラス参照によって参照されているからだ。
* ``Metaclass1`` のオブジェクトのうち、``MyStereotype`` のオブジェクトによって拡
  張されたオブジェクトも見えることになる。
* ``MyStereotype`` によって拡張されていない ``Metaclass1`` のオブジェクトは隠匿
  されたままだ。

..

   If a Profile P1 imports another Profile P2, then all ``metaclassReference``
   and ``metamodelReference`` associations will be combined at the P2 level, and
   the filtering rules apply to this union.

Profile 水準で定義される選別規則はプロファイルがモデルに適用されるときに何をする
のかをモデリングツールに提案するものに過ぎない。

   The ``isStrict`` attribute on a ProfileApplication specifies that the
   filtering rules have to be applied strictly.

ProfileApplication の ``isStrict`` が真である場合、Profile がモデルに適用された
ときに、プロファイルによって定義されたアクセス可能メタクラス以外のメタクラスには
アクセスできないものとする。異なるアクセス可能メタクラスを指定する適用されたプロ
ファイルを組み合わせることを禁止するのだ。

12.3.3.3 ProfileApplication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A ProfileApplication is used to record which Profiles have been applied to a
   Package.

   One or more Profiles that extend UML may be applied at will to a model
   Package. Applying a Profile means that it is possible to apply the
   Stereotypes that are defined as part of the Profile.

* 複数 Profiles を一つの Package に適用することが可能だ、矛盾する Constraints を
  持つ場合、Package を無効にしてしまう可能性がある。
* Profileを適用することは、その入れ子 Profile やインポートされた Profile をす
  べて再帰的に適用することを意味する。
* Profile の public ``members`` である Stereotypes は、その Profile が適用された
  Package の該当するモデル要素に適用してもよい。

Profile が適用されると、ExtensionEnds が ``isRequired`` が真であるメタクラスのオ
ブジェクトである要素に対して、適当な Stereotypes のオブジェクトを生成する必要が
ある。これらのオブジェクトがないモデルは well-formed ではない。

   Once a Profile has been applied to a Package, it is allowed to remove the
   applied Profile at will. Removing a Profile implies that all elements that
   are instances of Stereotypes defined in the Profile are deleted including the
   instances of Profile-defined Classes they compositionally aggregate and the
   instances of Profile-defined composite Associations linking them.

複合集約でない他のオブジェクトも、その定義型が同じモデルに適用された他の
Profile からアクセスできなくなった場合、削除されなければならない。

適用された Profile を削除しても、参照されるメタモデル由来の要素のオブジェクトは
そのまま残る。削除されるのは、Profile に含まれる要素のオブジェクトだけだ。このこ
とが意味するのは、例えば、プロファイル化 UML モデルは、プロファイル対応をしてい
ない他のツールといつでも交換することが可能であり、純粋な UML モデルとして解釈さ
れることだ。

   A Profile which is a ``packagedElement`` of another Profile can be applied
   individually.

ただし、入れ子になった Profile は、Stereotypes を含む場合には必要メタクラスとメ
タモデル参照両方またはどちらか一方を指定しなければならず、PackageImport を使用し
て、共同適用される他の Profile を指示することが可能だ。メタクラスとメタモデル参
照の両方またはどちらか一方は、包含 Profile からは継承されない。

12.3.3.4 Stereotypes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A Stereotype defines an extension for one or more metaclasses, and enables
   the use of specific terminology or notation in place of, or in addition to,
   the ones used for the extended metaclasses.

Stereotype が複数のメタクラスを拡張する場合、どの時点においても、メタクラスのう
ち正確に一つのオブジェクトにしか適用不可能だ。ただし、あるメタクラスのオブジェク
トから Stereotype を切り離して、別のメタクラスのオブジェクトに付け替えることは可能だ。

   A Stereotype is a limited kind of metaclass that cannot be used by itself,
   but must always be used in conjunction with one of the metaclasses it
   extends. Each Stereotype may extend one or more metaclasses through
   association (Extension) rather than generalization/specialization. Similarly,
   a metaclass may be extended by one or more Stereotypes.

Stereotype のオブジェクト S を、UML のメタクラス C に「拡張」（これは特定の種類
の Association である）を使って関連付けることは、型 C のモデル要素を S のオブ
ジェクトによって拡張することが許されることを意味する。モデル水準では S のオブ
ジェクトは、リンク (S から C への Association/Extension) によって C モデル要素
（C のオブジェクト）に関連付けられる。

   Any metaclass referenced by a ``metaclassReference`` or contained in a
   Package referenced by ``metamodelReference`` of the closest Profile directly
   or indirectly containing a Stereotype can be extended by the Stereotype.

例えば、States, Transitions, Activities, Use Cases, Components, Properties,
Dependencies, etc. はその ``metamodelReference`` が UML ならば、すべて
Stereotypes で拡張が可能だ。

Stereotype は Package に含まれることもある。その場合、拡張可能なメタクラスは
Package を含む最も近い親 Profile により参照されるものだ。

   Just like a Class, a Stereotype may have Properties, which have traditionally
   been referred to as Tag Definitions. When a Stereotype is applied to a model
   element, the values of the Properties have traditionally been referred to as
   *tagged values*. Stereotype specializes Class and its Properties have the
   same meaning in Stereotypes as they do in Class.

Stereotype Property は複合集約を持つことが可能だ。Stereotype 上の複合集約
Property の値は、その Stereotype のオブジェクトにより所有される。

プロファイルは、元々適用されていたモデルを変更することなく適用解除が可能であるた
め、モデル内のメタクラスのオブジェクトは、Stereotype オブジェクトやその特性の値
を参照することは不可能だ。

複合集約 Stereotype Property の型は Stereotype またはメタクラスではあり得ない。

* ツール売人は被所有操作・動作を含む拡張性を対応することを選択してもよいが、そう
  することを要求されてはいない。
* ツールは Stereotype ``ownAttributes`` を対応しなければならない。

..

   Its Profile or Package defines the namespace for the Stereotype.

Profiles が Package に適用されている場合、利用可能な Stereotypes は適用された
Profiles により定義され、異なる Profiles や Packages にある同じ ``name`` である
Stereotypes を区別するために、必要ならば完全修飾名を使ってこれらの Stereotypes
を表示することが可能だ。

PackageImport と ElementImport を使って、修飾されていない ``names`` の使用を許す
ことができる。

適用された Profile (``ownedStereotype``) が直接所有する Stereotypes を修飾名なし
で用いてよい。

12.3.3.5 Images
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   The Image class provides the necessary information to display an Image in a
   diagram. Icons are typically handled through the Image class.

   Information such as physical placement or format is provided by the Image
   class.

* Image クラスは、さまざまな形式の画像を表現するための汎用的な方法を用意する。
* 利便性と相互運用性のために、``format`` には定義済みの値がいくつ規定されている
  が、``format`` のとり得る集合は限界がない。

..

   The ``format`` property indicates the format of the ``content``, which is how
   the string content should be interpreted.

* 値 :abbr:`SVG`, :abbr:`GIF`, :abbr:`PNG`, etc. が予約されている。
* 加えて接頭辞 ``MINE:`` も予約済み。これは RFC 3023 で定義された有効 MIME 型が
  続かなければならない。この選択肢は上記の予約値を表現するための代替手段として用
  いることが可能だ。例えば ``MIME: image/svg+xml`` で :abbr:`SVG` を表現すること
  も可能だ。

12.3.3.6 Extensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   An Extension is used to indicate that the properties of a metaclass are
   extended through a Stereotype, and gives the ability to flexibly add (and
   later remove) stereotypes to classes.

   Extension is a kind of Association. One end of the Extension is an ordinary
   Property and the other end is an ExtensionEnd.

前者は Extension と Class に結び付け、対して後者は Extension とその Class を拡張
する Stereotype に結びつける。

A required Extension (isRequired = true) means that an instance of this
Stereotype must be linked to each instance of the extended metaclass in the
model to which the containing Profile has been applied (otherwise the model is
not well-formed). If the extending Stereotype has subclasses, then at most one
instance of the Stereotype or one of its subclasses is required.

* 必要 Extension (``isRequired == true``) とは、この Stereotype のオブジェク
  トが、その Profile が適用されたモデル内の拡張メタクラスのオブ
  ジェクトそれぞれにリンクされていなければならないことを意味する。
* 不要 Extension (``isRequired == false``) とは、この Stereotype のオブジェクト
  が、拡張メタクラスのオブジェクトに自由にリンクし、また後で自由に削除されること
  が許されることを意味する。

  * ただし、同じ Stereotype またはその部分型を同じ要素に二度適用することは不可能
    だ。
  * Stereotype のオブジェクトは拡張メタクラスのオブジェクトが削除される
    か、Stereotype を定義する Profile が Package の ``appliedProfiles`` から削除
    されると削除される。

   Figure 12.15 MOF Model Equivalent to Extending "Interface" by the "Home"
   Stereotype

単一メタクラス拡張について同値な MOF 構成を示す図。

* Figure 12.19 で示した Home という Stereotype が Interface メタクラスを拡張する
  場合を図示している。
* Interface は UML のメタクラスのオブジェクトであり、Home は Stereotype のオブジェクトだ。
* Extension と等価な MOF_ 概念的要素は拡張メタクラスから拡張 Stereotype への合成
  だ。後者は拡張メタクラスが所有する。
* Extension が必要な場合、拡張 Stereotype によって型付けされた Property の多重度
  は 1 だ。

..

   The name of the Property typed by the extended metaclass is:

   .. code:: text

      ‘base_’ extendedMetaclassName

   The name of the Property typed by the extension Stereotype (the ExtensionEnd)
   is:

   .. code:: text

      ‘extension_’ stereotypeName

Stereotype に Constraints が追加されることはよくある。上記の Property は OCL の
回航を表現するために使用してもよい。例えば、次の OCL 式は ``Home`` Interface
に属性を持たせてはならないことを述べている：

.. code:: c++

   self.base_Interface.ownedAttributes->isEmpty()

..

   Figure 12.16 Example of Multiple Metaclass Extension

複数のメタクラスを拡張する例。Stereotype ``TestCase`` はメタクラス Operation と
Behavior の両方を拡張している。

   Figure 12.17 MOF Model Equivalent to Multiple Metaclass Extension

複数メタクラス拡張に対する MOF_ 構成に対応する等価性を図示している。

12.3.3.7 ExtensionEnd
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   An ExtensionEnd is used to tie an Extension to a Stereotype when extending a
   metaclass: it is a ``navigableOwnedEnd`` of the Extension, avoiding an extra
   ``ownedAttribute`` on the extended Class. It is always typed by a Stereotype
   and must always have ``isComposite`` = true.

ExtensionEnd の既定の多重度は ``0..1`` だ。Stereotype が必要な場合は ``1..1`` に
なることもあるが、上限値がこれを超えることはない。

12.3.4 Notation
----------------------------------------------------------------------

Extension の記法は矢印だ。

   Figure 12.18 The Notation for an Extension

* 鏃は黒塗の三角。
* 向きは Stereotype から拡張 Class とする。
* Association と同じ修飾をしてもよいが、通常は省略し、
  回航可能性の矢印は描かない。
* ``isRequired`` が真ならば ExtensionEnd の近くに ``{required}`` と記す。
  ExtensionEnd の多重度 ``0..1`` または ``1`` を、装飾 ``{required}`` の代わりと
  して使用することが可能だ。``isRequired`` がどのように導出されるかによって、多
  重度 ``0..1`` は ``isRequired`` が偽であることに対応する。

Profile は Package と同じ記法を用いる。ただし名前の前または上にキーワード
``«profile»`` をつける。

``Profile::metaclassReference``, ``Profile::metamodelReference`` は
``Package::elementImport``, ``Package::packageImport`` とそれぞれ同じ記法プラス
キーワード ``«reference»`` を付ける。

ProfileApplication は破線矢印で示す。

* 鏃は開く。
* 向きは Package から適用される各 ``appliedProfile`` に向かう。
* 矢印の近辺にキーワード ``«apply»`` か、``isStrict`` が真ならばキーワード
  ``«strict»`` を示す。

..

   If multiple ``appliedProfiles`` have Stereotypes with the same name, it may
   be necessary to qualify the name of the Stereotype (with the profile name).

Stereotype は Class と同じ記法を用いる。ただし名前の前または上にキーワード
``«stereotype»`` をつける。

Stereotype がモデル要素に適用される場合、Stereotype の名前はモデル要素の名前の上
か前、または名前が省略されるか表示されない場合に名前が現れる場所に ``«...»`` の
中に表示される。

NamedElement ではないが図表的表現があるモデル要素では、他に特別な記述がない限
り、Stereotype は図表的表現の右上隅にある ``«...»`` の中に表示することが可能だ。

複数の Stereotypes が適用されているならば、それらの名前を ``«...»`` 内に CSV と
して示す。

拡張モデル要素にキーワードがある場合、ステレオタイプ名はそのキーワードの近くに、
または個別の ``«...»`` で示される。例：

* ``«interface» «Clock»``
* ``«Clock, interface»``

Stereotype の ``name`` はクラスの命名規約に従い大文字で始めるのが普通。しかし
Profiles は異なる規約を用いてよい。

ツールは Stereotypes を表示するのかしないのかを選ぶことができる。

   A tool can choose whether it will display Stereotypes or not. In particular,
   tools can choose not to display *required* stereotypes, but to display only
   the values of their ``ownedAttributes`` if any.

モデル要素に適用される Stereotype またはその一般化の ``ownedAttributes`` の値
は次の三者の方法のうちの一つで示すことが可能だ：

#. モデル要素を表す図表ノードに接続された註釈記号の部分として
#. モデル要素を表す図表ノードの別々の区画で
#. 図表ノードで ``name`` 文字列の上か、それ以外の場合は名前文字列の前に

区画または註釈記号を用いる場合、区画や註釈に含まれるだけでなく、``name`` 文字列
の前に ``«...»`` でステレオタイプ名を示してよい。

   The values are displayed as name-value pairs:

   .. code:: bnf

      <namestring> ‘=’ <valuestring>

   If a Stereotype Property is multi-valued, then the ``<valuestring>`` is
   displayed as a comma-separated list:

   .. code:: bnf

      <valuestring> ::= <value> [‘,’ <value>]*

特定の値には特別な表示規則がある：

* 真偽型 Properties の値を表示する場合、``<namestring>`` が表示されている場合の
  値は真であり、そうでない場合、値は偽であるという規約を用いてもよい。
* 値が NamedElement の ``name`` の場合、その要素の ``qualifiedName`` を表示して
  も可としてよい。

Stereotype Property の値を表示するのに区画を使う場合、Property 値を表示する適用
された Stereotype それぞれに対して区画を追加する必要がある。このような区画の先頭
には、適用される Stereotype の名称が ``«...»`` で表示される。このような区画は、
一般的に区画を使用することができる要素、特に Classifiers と State にしか適用され
ることがない。

註釈記号中やモデル要素の ``name`` の前か上に表示される場合、特定の Stereotype の
Property の値の前に、適用される Stereotype の名前を ``«...»`` で表示することが許
される。

   When displayed in compartments or in a comment symbol, at most one
   namestring-valuestring pair can appear on a single line. When displayed above
   or before a model element’s ``name``, the name-value pairs are separated by
   semicolons and all pairs for a given stereotype are enclosed in braces.

12.3.4.1 Icon presentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   It is possible to attach Images to a Stereotype that can be used in lieu of,
   or in addition to, the normal notation of a model element to which the
   Stereotype is applied.

Stereotype に ``icon`` 値があると、その Stereotype が適用されたモデル要素に参照
される Image を図表的に添えることが可能だ。

図表的表現を有するすべてのモデル要素がアイコンを付けることが可能。
モデル要素が図表的に表現されている場合、

* 箱：箱が Image に取って代わられ、モデル要素の ``name`` が Image の下に現れる。
  この表現方法は、モデル要素に単一の Stereotype が適用されており、モデル要素の
  Properties (e.g. ``ownedAttributes``, ``ownedOperations``) がない場合だけ可
  能。

  また別の選択として、モデル要素を表現する箱の内側や上部に Image の縮小版を表示
  してもよい。複数の Stereotypes が適用されている場合、複数の Images を箱の中に
  表示してよい。
* 線：線の近くに Image を配置してよい。
* テキスト記法：テキスト表記の左に Image を表示してよい。

..

   Several Images may be referenced by a Stereotype’s icon Property.

ツールによっては、箱を置き換えるアイコン、箱内の縮小アイコン、ツリーブラウザー内
のアイコンなど、異なる目的で異なる画像を使用することができる。あるいは一つの画像
を異なる大きさに拡大縮小することを選択することがある。

モデル要素には既定の表現をするためのアイコンをすでに使うものもある。典型的な例に
は Actor モデル要素があり、「棒人間」のアイコンを用いる。

   When a Stereotype with an icon is applied to such a model element, the
   Stereotype’s ``icon`` replaces the default presentation icon within diagrams.

12.3.5 Examples
----------------------------------------------------------------------

   Figure 12.19 Example of Using an Extension

ここで ``Home`` はメタクラス Interface を拡張するステレオタイプだ。

ステレオタイプ ``Home`` のオブジェクトはクラス Interface のオブジェクトに自由に
追加・除去することが可能であり、Profile に固有の情報を Package に動的に追加・除
去する柔軟なやり方を呈している。

   Figure 12.20 Example of a Required Extension

Profile が適用されるモデル内のメタクラス Component のオブジェクトそれぞれ
は、Extension の ``isRequired`` が真であるので、ステレオタイプ ``Bean`` のオブ
ジェクトを適用しなければならない。

モデルはそのような Stereotype が適用されなければ well-formed でない。

   Figure 12.21 Defining a Simple EJB Profile

ある EJB Profile の簡単な見本。

``Bean`` がメタクラス Component に適用されていることを必要とする。``Bean`` は抽
象的なので、具象サブクラスである ``Entity`` か ``Session`` のどちらかのオブジェ
クトが Component の各オブジェクトにリンクされていなければならないことを意味する。

Profile の部分である Constraints は、Profile が Package に適用されたときに評価さ
れ、モデルが well-formed であるためにはこれらの Constraints が満たされている必要
がある。

   Figure 12.22 Importing a Package from a Profile

   In Figure 12.22, the Package named ``Types`` is imported by the Profile named
   ``Manufacturer``. The Enumeration named ``Color`` and the Class named
   ``JavaInteger`` are then used as the type of Properties of the Stereotype
   named Device as well as the standard PrimitiveType ``String``.

Profile ``Manufacturer`` が後で Package に適用される場合、``Types`` 由来の型は
Profile が適用される Package では（明示的にパッケージ ``Types`` をインポートしな
い限りは）利用不可能だ。

Package ``Factory`` が Package ``Types`` をインポートしない限り、クラス
``JavaInteger`` は Stereotype Property の型として使用可能だが、通常の Property
としては使用不可（この例ではインポートしているので使用可能）。

Stereotype ``Device`` が Clas ``TV`` に適用されると、Property ``volume`` の値が
表示される。

   Figure 12.23 Profiles Applied to a Package

プロファイル Java および EJB を考慮すると、これらが Package ``WebShopping`` にど
のように適用されるかを示す。

   Figure 12.24 Defining a Stereotype

簡単なステレオタイプ ``Clock`` が、自在にメタクラス Class のオブジェクトに対して
（動的に）適用可能であるように定義されている。

   Figure 12.25 Presentation Options for an Extended Class

上記 ``Clock`` の数通りの表現例。本文中にはこの見本のための言及がない。

   Figure 12.26 An Instance Diagram when Defining a Stereotype

かなり込み入ったオブジェクト図。先ほどの ``Clock`` の定義を表現している諸オブ
ジェクトを示している。``Clock`` から左側の理解が重要。

   Figure 12.27 Defining Multiple Stereotypes on Multiple Stereotypes

``Clock`` が Component と Class の両方を拡張することを示す。それとは別に
``Creator`` という、Class を拡張する Stereotype を定義している。

   Figure 12.28 Using a Stereotype

クラス ``StopWatch`` に ``Clock`` を適用した。単に ``«Clock»`` をクラス名の上に
付記するだけで示せる。

   Figure 12.29 Showing Values of Stereotypes and a Simple Instance Specification

上記の適用の意味するところを表現する図式。

右側は、オブジェクト図表記を使用して、左側の UML 図の動作と XMI シリアライズを理
解するためになるべく使用される MOF_ 等価なオブジェクトを示す。

Stereotype とメタクラス Class の間の Extension は、Stereotype ``Clock`` のオブ
ジェクトと ``Stop Watch`` という名前の Class の間のリンクをもたらす。

   Figure 12.30 Using Stereotypes and Showing Values

``StopWatch`` に ``Clock`` と ``Creator`` を同時に適用する。ここでは各
Stereotype の Property 値を註釈記法で示してある。

   Figure 12.31 Other Notational Forms for Depicting Stereotype Values

Stereotype の Property 値を記述する代わりの記法の例。属性区画に ``«Clock»`` と
断ってから値を列挙。

   Figure 12.32 Example of a Profile defining Classes and (...)

Profile-defined クラスと二項複合（および非複合）関連を持つ Profile の見本。

* Profile ``IssuesProfile`` が Profile ``uml`` をインポートしていることをわざ
  わざ図式内の上部にて断っている。
* 本文ではこの図に相当する XMI コード全体を掲載している。

   Figure 12.33 Diagram example of applying a profile defining Classes and
   Associations and of creating instances of such Classes. Tools can provide a
   notation similar to that of object diagrams for instances of Profile-defined
   Classes, DataTypes and Associations

上記 ``IssuesProfile`` の適用例。

* Profile ``IssueExample`` は ``IssuesProfile`` を適用している。
* 重要なのは矢印のラベルに現れる ``«IssueTag»`` の意味だ。

本文ではこの図のオブジェクト部分を表現する XMI コードを、Profile-defined 関連の
リンクオブジェクトの有無で分けて二通り掲載している。

12.4 Classifier Descriptions
======================================================================

機械生成による節。

12.5 Association Descriptions
======================================================================

機械生成による節。

.. include:: /_include/uml-refs.txt
