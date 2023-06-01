======================================================================
12 Packages
======================================================================

UML 2.5 pp. 239-282 に関するノート。

.. contents:: ノート目次
   :depth: 2

12.1 Summary
======================================================================

* Packages は UML の主な包括的な構造化および組織化能力を与える。Models に関する
  特殊化および UML に対する拡張を組織化する Profiles に関する特殊化がある。

12.2 Packages
======================================================================

12.2.1 Summary
----------------------------------------------------------------------

* この節では Packages と Models の仕様を与える。

12.2.2 Abstract Syntax
----------------------------------------------------------------------

* Figure 12.1 Packages

  * Package, Model, PackageMerge が新しく現れた。
  * Type も PackageableElement の一種であることが図では省略してある。

``A_packagedElement_owningPackage``
  * Package から PackageableElement への composite 関連（単方向）。
  * Package は Namespace であり、所有要素を関連端 ``packagedElement`` で表現す
    る。
  * ``A_ownedMember_namespace`` を subsets する。

  ``A_ownedType_package``
    * Package から Type への composite 関連（双方向）。
    * Type である内容物への参照を表現する関連。
    * ``A_packagedElement_owningPackage`` を subsets する。

  ``A_nestedPackage_nestingPackage``
    * Package から Package への composite 関連（双方向）。
    * Package である内容物への参照を表現する関連。
    * ``A_packagedElement_owningPackage`` を subsets する。

``A_packageMerge_receivingPackage``
  * Package から PackageMerge への composite 関連（双方向）。
  * 関連端 ``receivingPackage`` 側の Package が合併前後で構成要素が増える方を指
    す。
  * ``A_ownedElement_owner`` と ``A_source_directedRelationship`` を subsets す
    る。
  * 関連端 ``receivingPackage`` の多重度はちょうど 1 である。
  * cf. ``A_mergedPackage_packageMerge``

``A_mergedPackage_packageMerge``
  * PackageMerge から Package への関連（単方向）。
  * 関連端 ``mergedPackage`` は合併前後でその構成内容物が変わらない方を指す。
  * ``A_target_directedRelationship`` を subsets する。
  * 関連端 ``mergedPackage`` の多重度はちょうど 1 である。
  * cf. ``A_packageMerge_receivingPackage``

12.2.3 Semantics
----------------------------------------------------------------------

12.2.3.1 Package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Package はそれの ``members`` についての名前空間であり、``packagedElement`` で
  結び付けられた構成員の要素を含み、インポートされたものを含む。
* Package の定義は他の Packages の内容を、自分の包含要素の合併 (merging) により
  拡張することが可能である。
* Package をテンプレートとして定義してよく、他のテンプレートに対して束縛してもよ
  い。

  * 詳しくは :doc:`./ch07-common-structure` を参照。

* URI を Package にとって一意な識別子を与えるように指定することが可能である。
  UML 内部では、プロファイルを除いた場合では、前もって決定されたこれにとっての利
  用法はない。

12.2.3.2 PackageMerge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* PackageMerge とは、下で定義される規則集に従って、対象の ``mergedPackage`` の内
  容が出処の ``receivingPackage`` に結合されることを示す二つの Packages 間の有
  向関係である。
* Generalization と同じように、Package は自分自身を合併することは直接的、間接的
  を問わず許されない。
* この能力は、さまざまな Packages で定義された要素が同じ ``name`` であり、同じ概
  念を意図するときに用いられるべく設計されている。
* 受け手側 Package に含まれるモデル要素に対する参照のどれもが、Package に含まれ
  る増分に対してではなく、合併結果に対する参照を含意する。
* Figure 12.2 Illustration of the Meaning of Package Merge

  * ``P2::A`` は ``P1::A`` の増分を定義する。
  * ``P3::SubA`` は ``P2::A`` のサブクラスの定義である。``P3`` から見ると、
    ``P2::A`` は ``P1`` と ``P2`` の間のマージ結果の ``A`` を表現していると解釈
    する。
  * ``P1``: ``mergedPackage`` (``target``)
  * ``P2``: ``receivingPackage`` (``source``, ``owner``) であると同時に
    ``resultingPackage``

    * マージの ``before``/``after`` で同じところにあるものの呼び方が変わる
      (``receiving``/``resulting``) ことがわかればとりあえず読める。

* PackageMerge は合併される Package の内容を受け手側の内容と結合することによっ
  て、（それ自身が変換の集合である）操作として考察することができる。
* PackageMerge の規則を理解するには、三種の別個の実体の間をはっきりと見分ける必
  要がある：

  #. ``mergedPackage``
  #. ``receivingPackage``
  #. 合併変換の結果

* この専門用語は Figure 12.3 の図解により表される PackageMerge の概念上の見方に
  基づく。

  併合されたパッケージ (merged package)
    受領パッケージに併合されることになるパッケージ。

  受領パッケージ (receiving package)
    概念上の、併合の結果を含むパッケージであるのだが、この用語は併合変換が実施さ
    れる前のパッケージおよびそれの中身を参照するのに用いる。

  結果パッケージ (resulting package)
    概念上の、併合の結果を含むパッケージである。モデルでは当然ながらこれは受領
    パッケージと同じであるが、この特別の用語は併合変換が実施された後のパッケージ
    およびそれの中身を参照するのに用いる。

  併合された要素 (merged element)
    併合されたパッケージに存在するモデル要素。

  受領要素 (receiving element)
    受領パッケージにあるモデル要素。

  結果要素 (resulting element)
    併合が実施された後の結果パッケージにあるモデル要素。

  要素型 (element type)
    Parameter や StructuralFeature の ``type`` のような、TypedElement のどんな種
    類の ``type`` をも指す。

  要素メタタイプ (element metatype)
    モデル要素の MOF 型である。例えば Classifier, Association, Feature である。

* Figure 12.3 Conceptual View of the Package Merge Semantics

  * 図の右側は UML の図式ではない。
  * この ``B`` ダッシュを意識することがコツだと言っている。

* PackageMerge の意味は制約と変換の集合で定義される。制約は有効な PackageMergeに
  とっての事前条件を指定し、それに対して、変換はその意味的な効果（事後条件）を記
  述する。制約のいくつかが破られていれば PackageMerge は ill-formed であり、それ
  を含むモデルは無効ある。

  * その「集合」が pp. 240-245 で文書化されている。もしマージの仕様を詳しく把握
    する状況になったら、ここを参照すること。

* この仕様では、他の種類の要素メタタイプ（例えば状態機械や相互作用）の意味が複雑
  かつ領域固有であるので、明示的な合併変換は一定の一般的メタモデル (Packages,
  Classes, Associations, Properties, etc.) にたいてい見出される要素メタタイプに
  ついてしか定義されていない。

12.2.3.3 General Package Merge Rules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* 合併される要素と受領要素が一致する (match) とは、それらがそれらのメタタイプに
  ついての一致規則を満足することを言う。

CONSTRAINTS
  #. ``«merge»`` 有向グラフに閉路はあり得ない。
  #. Package はそれに含まれている Package を合併することはできない。
  #. Package はそれが含む Package を合併することはできない。
  #. メタタイプが Package, Class, DataType, Property, Association, Operation,
     Constraint, Enumeration または EnumerationLiteral の一種ではないような併合
     された要素には、その受領要素が併合された要素のそのままのコピーではない限り
     は、同じ名前とメタタイプの受領要素はあり得ない。
  #. PackageMerge は併合を実施するのに要求される制約のすべてが成り立つとき、かつ
     そのときに限って有効である。
  #. 型付けられた要素の一致は適合する型である必要がある。Classes または
     DataTypesである型の場合、適合型は同一の型あるいは共通する上位型のいずれかで
     ある。他のすべての場合では、適合とは型が同一であることを意味する。
  #. 受領要素は併合された要素のどれに対しても明示的な参照があることはあり得な
     い。
  #. 一致する RedefinableElements に結び付いた再定義はいずれも矛盾してはならな
     い。

TRANSFORATIONS
  #. （既定の規則）一致する要素のない合併された要素または受領要素は結果のパッ
     ケージの中に deep copy される。
  #. 二つの要素を一致するお互いのそっくりなコピーである名前とメタタイプに合併
     する結果が受領要素になる。
  #. 一致する要素はそれらのメタタイプに固有の変換規則に従って連結され、結果は生
     じる Package に含まれる。
  #. 結果パッケージに行き着く型の付いた要素に対する型参照のすべては対応する結果
     TypedElements への参照に変換される。
  #. 一致する要素全ての場合、一致する要素の両方とも private ``visibility`` であ
     ると、結果要素は private ``visibility`` である。そうでなければ、結果要素は
     public ``visibility`` である。
  #. 一致する Classifier 要素全ての場合、一致する要素の両方とも ``isAbstract``
     が ``true`` だと、結果要素は ``isAbstract`` が ``true`` である。そうでなけれ
     ば、結果要素は ``isAbstract`` が ``false`` である。
  #. 一致する Classifier 要素全ての場合、一致する要素の両方とも
     ``isFinalSpecialization`` が ``true`` だと、結果要素は
     ``isFinalSpecialization`` が ``true`` である。そうでなければ、結果要素は
     ``isFinalSpecialization`` が ``false`` である。
  #. 一致する要素全ての場合、一致する要素の両方とも導出されないならば、結果要素
     もまた導出されない。そうでなければ、結果要素は導出される。
  #. 一致する MultiplicityElements 全ての場合、結果要素の ``lower`` は一致する要
     素の ``lower`` の小さいほうである。
  #. 一致する MultiplicityElements 全ての場合、結果要素の ``upper`` は一致する要
     素の ``upper`` の大きいほうである。
  #. 併合された要素か受領要素の一方にあるモデル要素に適用されたステレオタイプは
     どれもが対応する結果要素にも適用される。
  #. 一致する RedefinableElements の場合、一致する RedefinableElements の異なる
     再定義はすべてが結果要素に適用される。
  #. 一致する RedefinableElements の場合、一致する要素の両方とも ``isLeaf`` が
     ``true`` だと、結果要素も ``isLeaf`` が ``true`` である。そうでなければ、結
     果要素は ``isLeaf`` が ``false`` である。

12.2.3.4 Package Rules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Package の種類の Elements は ``name`` およびメタタイプにより一致する。

CONSTRAINTS
  #. 合併された Package にある Classifiers のすべてに空でない ``qualifiedName``
     がある必要があり、合併された Package で ``isDistinguishableFrom()`` の値が
     ``true`` となる。
  #. 受領 Package にある Classifiers のすべてに空でない ``qualifiedName`` がある
     必要があり、受領 Package で ``isDistinguishableFrom()`` の値が ``true`` と
     なる。

TRANSFORATIONS
  #. 併合された Package からの ``nestedPackage`` は受領 Package が一致する
     ``nestedPackage`` をまだ含まない限り、同じ ``name`` と内容が結果の Package
     にある ``nestedPackage`` に変換される。
  #. 受領 Package の ``elementImport`` である ElementImport は生じる Package の
     対応する ElementImport に変換される。

12.2.3.5 Class and DataType Rules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Class や DataType の種類の Elements は ``name`` およびメタタイプにより一致す
  る。

TRANSFORATIONS
  #. 併合された Classifier の ``ownedAttributes`` である Properties はすべてが受
     領 Classifier に併合されて、下に指定される Property 変換規則に従って、結果
     の Classifier を生じる。
  #. ``nestedClassifiers`` は同じ規則に従って再帰的に併合される。

12.2.3.6 Property Rules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Property の種類の Elements は ``name`` およびメタタイプにより一致する。

CONSTRAINTS
  #. 一致する Properties の ``isStatic`` の値が同じである必要がある。
  #. 一致する Properties の ``isUnique`` の値が同じである必要がある。
  #. 一致する Properties に結び付いた Constraints のいずれも矛盾があってはならな
     い。

TRANSFORATIONS
  #. 一致する受領 Property のない併合された Properties の場合は、結果 Property
     は併合された Property と同じ結果 Classifier にある Property である。
  #. 一致する受領 Property を有する併合された Properties の場合は、結果 Property
     は同じ名前と特徴が異なるものを除いた特徴があるProperty である。
  #. （以下略）

12.2.3.7 Association Rules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Association の種類の Elements は ``name`` およびメタタイプにより一致する。

CONSTRAINTS
  #. これらの規則は二項 Association にしか適用しない。
  #. 一致する併合された関連端の ``aggregation`` が composite であると、受領関連
     端の ``aggregation`` が composite である必要がある。
  #. 一致する併合された関連端が Association により所有されていると、受領関連端は
     その Association により所有されている必要がある。

TRANSFORATIONS
  #. 一致する Associations の併合は、Properties についての規則に従い、かつ関連端
     についての規則に従って、Association classifiers の併合とそれらの対応する
     ``ownedEnd`` Properties の併合によって達成される。
  #. 一致する関連端の場合、もしどの関連端も ``ownedNavigableEnd`` になければ、結
     果の関連端もまた ``ownedNavigableEnd`` にない。他の場合のすべてにおいては、
     結果の関連端は ``ownedNavigableEnd`` にある。

12.2.3.8 Operation Rules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Operation の種類の Elements は ``name``, Parameter の順序および Parameter の型
  により一致する。戻り値の型のいずれも含まない。

CONSTRAINTS
  #. Operation Parameters とその型は、Properties に対して定義されたかのように、
     型と多重度に対する同じ規則に適合する必要がある。
  #. 一致する合併された Operation の ``isQuery`` が ``true`` だと、受領
     Operation は ``isQuery`` が ``true`` である必要がある。

TRANSFORATIONS
  #. 一致する受領 Operation のない併合された Operations の場合は、結果 Operation
     は同じ名前と同じ signature が結果 classifier にある Operation である。
  #. 一致する受領 Operation を有する併合された Operations の場合は、結果
     Operation は一致する併合された Operations と受領 Operations の併合の結果で
     あり、 Parameter 変換が上で定義された Property 変換に従って実施されている。

12.2.3.9 Enumeration Rules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* EnumerationLiteral の種類の Elements は所有する Enumeration およびリテラル
  ``name`` により一致する。

CONSTRAINTS
  #. 一致する EnumerationLiterals は同じ順序である必要がある。

TRANSFORATIONS
  #. 併合された Enumeration 由来の一致しない EnumerationLiterals は受領
     Enumeration に含まれる。

12.2.3.10 Constraint Rules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

CONSTRAINTS
  #. Constraints は互いに矛盾がないようにする必要がある。

TRANSFORATIONS
  #. 併合されたモデル要素の Constraints はすべて受領モデル要素の Constraints に
     加わる。

12.2.3.11 Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Model とはシステムの記述である。ここでシステムは、最も幅広い意味で意図されてい
  て、ソフトウェアやハードウェアだけでなく、組織や工程をも含んでよい。
* Package と同じように、Model にはモデル化されているシステムを協力して記述する
  ``members`` の集合がある。
* 種々の Models を同じシステムに対して定義することが可能であり、典型的にはこの
  種々の Models は相補的であり、種々のシステム利害関係者の観点から定義されてい
  る。
* Model には次のものの間にある Abstraction Dependencies があることが可能。

  * ``refinement`` （標準プロファイル ``«Refine»`` でステレオタイプされる）
  * ``mapping`` （例えば標準プロファイル ``«Trace»`` でステレオタイプされる）

12.2.4 Notation
----------------------------------------------------------------------

* Package は大きい矩形の左上に小さい矩形（タブ）を付けた形状で示す。

  * Package の内容物は大きい矩形の内部に示してよい。
  * マルにプラスを付けた記号を使って、 Package の外部から要素に線を引くような記
    法がある。
  * PackageImport や ElementImport を通じて持ち込んだ要素は、色を変えて描かれる
    ことがある。
  * Package の名前は内容物が大きい矩形内にあるかどうかで、場所が異なる。タブに記
    される場合と、大矩形内に記される場合がある。
  * 要素の可視性はいつものように要素名の前に ``+``, ``-`` 等の記号を付して示して
    もよい。

    * Packages の可視性が protected や package であることは許されない。

  * URI を ``{uri = <uri>}`` の形式でパッケージ名の後に示してよい。

* PackageMerge は開いた矢先の破線矢印を用いて示す。

  * 矢印の向きは ``receivingPackage`` から ``mergedPackage`` である。
  * キーワード ``«merge»`` を破線のそばに示す。

* Model は通常の Package シンボルに小さな三角を大矩形の右上隅に描いたもので記す。

  * 大矩形内部に要素が示されているならば、小三角はタブの右側に描いてよい。
  * またはキーワード ``«model»`` をモデル名の上に付記することで、あとは通常の
    Package の記法を用いることもまた許される。

12.2.5 Examples
----------------------------------------------------------------------

* Figure 12.5 Examples of a Package with Members

  * どの図式でも Package の内容物がすべて記されているとは限らないようだ。
  * マルプラスの見本によると、線のスタイルは実線。

* Figure 12.6 Simple Example of Package Merge

  * もっとも基本的な見本と思われる。

* Figure 12.7 Simple Example of Transformed Packages Following the Merges

  * 上述の結果、各パッケージがどういう構成になるかを模式化したもの。各要素の意味
    が明記されていないので、このマージ結果の表現が妥当かどうか納得するには、先程
    読み飛ばした規則集を当たらねばならない。
  * ここで用いられている記法は UML の一部ではないので注意。

* Figure 12.8 Introducing Additional Package Merges

  * 空の Package ``T`` が上述の ``R`` と ``S`` をマージする図式。``T`` が空であ
    るというのは、図式外で説明されているに過ぎない。

* Figure 12.9 Result of the Additional Package Merges

  * 上述の ``T`` のマージ状態を模式化したもの。

* Figure 12.10 Three Models Representing Parts of a System

  * ``Client``, ``Business``, ``Data`` からなる三層構造システムの Models の図
    式。

* Figure 12.11 Two Views of One System Collected in a Container Model

  * Models-in-Model な図式。同一図式内にあえて異なる記法（キーワード or 小三角）
    を併用している。

12.3 Profiles
======================================================================

12.3.1 Summary
----------------------------------------------------------------------

* この章では、メタクラスが種々の目的に適合するように拡張できるようになる能力を記
  述する。
* これは UML メタモデルを J2EE や .NET 等のさまざまなプラットフォームや領域（リ
  アルタイムまたはサービス志向様式）に合わせる能力も含む。
* この章は OMG MOF_ に対して一貫性がある。

12.3.1.1 Positioning Profiles versus Metamodels, MOF and UML
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* UML はモデリングを取り扱うさまざまな OMG の仕様書で別々のメタレベルで再利用さ
  れる。
* Profiles は第一等の拡張能力ではない。すなわち、新たなメタモデルを創造すること
  は考慮に入れていない。
* 第一等の拡張性は MOF_ で扱われるが、メタモデルレベルにおける制限は一つもな
  い。サブクラスと関連を必要に応じて追加することができる。
* UML を拡張するのがよいかもしれない理由がいくつかある。

  * 特定のプラットフォームやドメインに適合される用語法 (a terminology) を与え
    る。
  * 記法のない諸構成概念に構文を与える。
  * 既存の諸記号に異なる記法を与える。
  * UML や特定のメタクラス（複数形）にさらなる意味を追加する。
  * UML に存在しない型を追加する。
  * UML の諸構成概念で用いられるやり方に制限を加える Constraints を追加する。
  * あるモデルを別のモデルやコードに変換する際に用いることが可能な情報を追加す
    る。例えばモデルと Java コードの間の対応規則の定義など。

* いつ新しいメタモデルを作成するべきか、いつプロファイルを作成するべきか、あるい
  はいつ両者を（一方は UML ツール利用の場合に、もう一方は MOF ベースのツールの場
  合に）作成するべきかという問いに対する簡単な答えはない。

12.3.2 Abstract Syntax
----------------------------------------------------------------------

* Figure 12.12 Profiles

  * 一見するとグラフの構造がいつもより込み入っている。
  * 新クラスは Profile, ProfileApplication, Stereotype, Image, Extension,
    ExtensionEnd と、いつもより多く登場する。

``A_metaclassReference_profile``
  * Profile から PackageImport への composite 関連（単方向）。
  * ``A_packageImport_importingNamespace`` を subsets する。
  * cf. ``A_metamodelReference_profile``

``A_metamodelReference_profile``
  * Profile から ElementImport への composite 関連（単方向）。
  * ``A_elementImport_importingNamespace`` を subsets する。
  * cf. ``A_metaclassReference_profile``

``A_appliedProfile_profileApplication``
  * ProfileApplication から Profile への関連（単方向）。
  * Package に適用されている Profile を参照する関連である。
  * ``A_target_directedRelationship`` を subsets する。
  * cf. ``A_profileApplication_applyingPackage``

``A_profileApplication_applyingPackage``
  * Package から ProfileApplication への composite 関連（双方向）。
  * Package が Profile 適用情報を所有する。
  * ``A_source_directedRelationship`` と ``A_ownedElement_owner`` を subsets す
    る。
  * cf. ``A_appliedProfile_profileApplication``

``A_profile_stereotype``
  * Stereotype から Profile への関連（単方向）。
  * 自らを直接的にまたは間接的に含む Profile への参照を示す。
  * 関連端 profile は ``{readOnly}`` である。
  * 関連端 profile の多重度は 1 である。

``A_icon_stereotype``
  * Stereotype から Image への composite 関連（単方向）。
  * Stereotype を図式内でアイコンイメージを用いて表示する際、
    その中身の場所を参照する。
  * ``A_ownedElement_owner`` を subsets する。

``A_ownedStereotype_owningPackage``
  * Package から Stereotype への composite 関連（単方向）。
  * ある適用済み Profile が直接る Stereotype を所有するという意味か。
  * ``A_packagedElement_owningPackage`` を subsets/redefines する。
  * 関連端 ``ownedStereotype`` は ``{readOnly}`` である。

``A_ownedEnd_extension``
  * Extension から ExtensionEnd への composite 関連（単方向）。
  * 拡張されているメタクラスへの参照する。
  * ``A_ownedEnd_owningAssociation`` を redefines/subsets する。

``A_extension_metaclass``
  * Class から Extension への関連（双方向）。
  * メタクラスを拡張する Stereotype を参照する関連端を所有する。
  * 関連端は両方とも ``{readOnly}`` である。
  * 関連端の多重度は ``metaclass`` が 1 に対して ``extension`` が ``*`` である。

``A_type_extensionEnd``
  * ExtensionEnd から Stereotype への関連（単方向）。
  * メタクラスを拡張する Stereotype を参照する。
  * ``A_type_typedElement`` を redefines/subsets する。

12.3.3 Semantics
----------------------------------------------------------------------

12.3.3.1 Profiles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Profile とは、下に述べるように、UML を拡張するのに用いることができるメタモデル
  の制限された形式である。その主要な拡張構成要素は Stereotype である。

12.3.3.1.1 Restricting Availability of UML Elements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* ``metaclassReference`` ElementImports と ``metamodelReference``
  PackageElementsは Profile の選別規則を指定するのに用いることが許される。この選
  別規則は Profile が適用されるときにどの要素が利用可能であり、どの要素が隠れる
  のかを決定づける。
* モデルに Profile を適用することはそのモデルを決して変化させるものではない。根
  底にあるモデルの眺めを単に定義するものである。
* メタクラスが隠されている（利用不能となる）ことの影響は次のとおり：

  * 当該メタクラス（またはそのサブクラス）の新たなオブジェクトを生成することはできない。
  * 当該メタクラス（またはそのサブクラス）の既存のオブジェクトはもはや図式上で見
    ることができなくなるか、ブラウザー枠内を含む、リストで選択できなくなる。
  * 当該メタクラス（またはそのサブクラス）の既存のオブジェクトに関する
    Relationships はもはや図式上で見ることができなくなるか、ブラウザー枠内を含
    む、リストで選択できなくなる。

* 上記をどのように実装するかはツールによって異なってよい。
* 選別規則が Profile で活動的になるためには、Profile が厳格モードで適用される必
  要がある。これには ProfileApplication の ``isStrict`` 属性を明示的に ``true``
  とする必要がある。さもなければ選別規則はこの ProfileApplication に関して無視さ
  れる。
* もっともありがちなことは、Profile が UML 自身を ``metamodelReference`` を使っ
  てインポートするときである。
* ElementImports の ``visibility`` および ``alias`` 特性は
  ``metaclassReference`` として用いられるときには無視される。
* ``metaclassReference`` と ``metamodelReference`` の両方が Profile に存在する
  と、後者は無視されて特定のメタクラスだけが使用可能になる。
* 詳しくは、次の規則が使われて、Profile が厳格モードで適用された後にモデル要素が
  利用可能なのかどうかを決定づける。メタクラスおよびそのオブジェクトが利用可能で
  あるとは、それらが

  #. 明示的な ``metaclassReference`` により参照されるか、
  #. ``metaclassReference`` がないときは、明示的な ``metamodelReference`` により
     参照されるPackage の直接的または推移的な ``members`` であるか、
  #. 適用された Profile の ``member`` である Stereotype により拡張されているとき
     である。

* Profile が厳格モードで適用されているときは他のモデル要素のすべてが隠蔽、利用不
  能にされる。
* このことは利用可能なメタクラスの互いに素な集合らを指定する適用 Profile の組み
  合わせを無効にする。
* Profile ``P1`` が別の Profile ``P2`` をインポートすると、
  ``metaclassReference`` と``metamodelReference`` の関連すべてが ``P1`` の高さで
  結合されることになり、選別規則がこの和集合に適用する。
* Profile は Stereotypes ばかりでなく Classes, Associations, DataTypes,
  PrimitiveTypes そして Enumerations を定義またはインポートすることができる。
* Profile 定義の Types はその Profile の Properties の型としてか、別の Profile
  定義の Type の一般化 classifier としてしか用いることはできない。
* Stereotypes は二項 Associations にしか参加することができない。
* ツールが与えることが可能な Profile の能力のもっとも真っ直ぐな実装は、Profile
  メタモデルと同じように、実装を基にしたメタモデルを持つことである。

12.3.3.1.2 Integrating and Extending Profiles
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Profiles を生成、拡張、統合する方法はいくつかある。
* Profile 統合のもっとも簡素な形式は、単に複数 Profiles を同じ Package に適用す
  ることである。
* 一つの Profile が別のものの全部または一部を再利用したり、他の Profiles を拡
  張したりすることも可能である。
* 例えば the *Unified Profile for DoDAF and MODAF* (UPDM) Profile は Requirement
  や ViewPoint のような Stereotypes を再利用するために SysML Profile に統合する
  ことも可能であった。

  .. admonition:: 読者ノート

     この文から始まるパラグラフは面白そうだが、パッと見 could や would を含む文
     が多いので、どうも現実にある状況の話題ではなさそうだ。

12.3.3.1.3 MOF-Equivalent Semantics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* この節では Stereotypes とそのオブジェクトの意味を MOF_ を使って明確に述べる。
* MOF に対する同じ写像がどのように適用プロファイルを XMI を使って直列化するのか
  を決定するために用いられる。
* Profile の場合、Package から継承した `URI` Property が用いられて、XMI の
  Profile のオブジェクトを識別するのに用いられる ``nsURI`` を決定付ける。
* UML Standard Profile のような OMG に規範的な Profiles は、URI に対して OMG に
  規範的な名前付け戦略に追随する。
* Profile はちょうど任意のモデルのように XMI ファイルとして交換可能であり、適用さ
  れた Profile があるモデルもまた交換可能である。

.. * Figure 12.19 shows...

.. * 下の最初の直列化では
..   Figure 12.19 のモデルがどのようにして交換可能となるのかがわかる。

* Figure 12.13 Using the HomeExample Profile to Extend a Model

  * ステレオタイプ ``Home`` で拡張された Interface のオブジェクトを含むモデル。

* ゼロまたはそれを超える Profiles が適用されているモデルの XMI 直列化は二つの
  論理部分に（物理的に組織化されていてもよい）組織化された XMI ファイルである。

  #. モデルの XMI 直列化
  #. モデルまたはそのある部分に対する Profile の適用それぞれに対応するオブジェク
     トの XMI 直列化

* モデルまたはそのある部分に対する Profile の適用を削除することがモデル自身の
  XMI 直列化を修正してはならないので、 Part (1) にある XMI 要素はどれもがPart
  (2) にある XMI 要素のどれに対する参照もできない。

.. * 下の XMI では Figure 12.13 のモデルがどう XMI に直列化されるかがわかる。

12.3.3.2 Defining Profiles for Non-UML Metamodels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* 理論上、この能力はまれにしか、あったとしても、実用上では使われてこなかったが、
  Profiles の能力は UML 以外のメタモデルについての拡張を定義することが可能であ
  る。
* UML に加えて、Profile は別の MOF 準拠の参照メタモデルに関係してよい。一般に参
  照メタモデルは、典型的にはインポートされたか局地的に所有されたかのどちらかであ
  るメタクラスからなる。
* Profile を適用することはそのモデルを決して変化させるものではない。根底にあるモ
  デルの眺めを単に定義するものである。

  * 先にもこれを記した気がする。

* 一般には、プロファイルが適用されると、インポートされた参照メタモデルのオブジェ
  クトであるモデル要素しか見えないはずである。
* 次の規則が使われることで、Profile 適用後にモデル要素が利用可能か隠蔽されるかを
  決定づける。モデル要素が利用可能であるとは、それらが以下のどれかのメタクラスの
  オブジェクトである

  #. 明示的な ``metaclassReference`` により参照されるか、
  #. 明示的な ``metamodelReference`` により参照される Package に（直接的または推
     移的に）含まれるか、
  #. 適用された Profile により所有される Stereotype により拡張される。

* Profile が適用されていると他のモデルはすべてが隠蔽される（利用不能となる）。

* もっとも普通の場合は、Profile がメタモデル丸ごとを ``metamodelReference`` を
  使って単にインポートするときである。

* Figure 12.14 Specification of an Available Metaclass

  * ``MyMetamodel`` は二つのメタクラス ``Metaclass1`` と ``Metaclass2`` を含むメ
    タモデルである。
  * ``MyProfile`` は ``MyMetamodel`` と ``Metaclass2`` を参照する Profile であ
    る。
  * しかし、``Metaclass2`` に対する明示的なメタクラス参照もある。これはメタモデ
    ル参照を上書きする。

12.3.3.3 ProfileApplication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ProfileApplication はどの Profiles が Package に適用されているのかを記録するの
  に用いる。
* UML を拡張する一つまたはそれを超える Profiles は思いのままにモデル Package
  に適用して構わない。

  * Profile を適用するということは、Profile の部分として定義された Stereotypes
    を適用することが可能であることを意味する。

* Profile が適用されると、適当な Stereotypes のオブジェクトが ExtensionEnds が
  ``isRequired`` が ``true`` であるメタクラスのオブジェクトであるものの要素に対
  して生成される必要がある。

* 一度 Profile が Package に適用されると、適用された Profile を自由に取り除くこ
  とが許される。

  * Profile を取り除くことは、Profile で定義される Stereotypes のオブジェクトで
    ある要素すべてが、それらが合成集約する Profile 定義の Classes のオブジェクト
    とそれらをリンクする Profile 定義の合成 Associations とを含めて、削除される
    ことを意味する。

* 別の Profile の ``packagedElement`` である Profile を個々に適用することができ
  る。とは言うものの、入れ子の Profile が Stereotypes を含み、他の Profiles が共
  に適用されていることを示すために PackageImport を使うことができると、その
  Profile は必要とされるメタクラス・メタモデル参照をどれも指定する必要がある。

12.3.3.4 Stereotypes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Stereotype は一つまたはそれを超えるメタクラスについての拡張を定義し、固有の用
  語または記法の用途が拡張メタクラスに対して用いられるものを上書きや追加できるよ
  うにする。

  * Stereotype がメタクラスをいくつか拡張すると、どの時点においてもメタクラスの
    うち正確に一つのオブジェクトにしか適用することができない。

* Stereotype とは、それ自身により使われることがあり得ないが、それを拡張するメタ
  クラスのうちの一つと一緒に常に用いられる必要がある、メタクラスの限定された一
  種である。
* ``metaclassReference`` により参照されるか、Stereotype を直接または間接的に含む
  もっとも近い Profile の ``metamodelReference`` により参照される Package に含ま
  れるメタクラスはいずれもその Stereotype によって拡張することができる。

  * 例えば、その ``metamodelReference`` が UML ならば、States, Transitions,
    Activities, UseCases, Components, Properties, Dependencies, etc. はすべて
    Stereotypes で拡張が可能である。

* Class と同じようにして、Stereotype に Properties があることが許されるが、それ
  は習慣的に Tag Definitions と呼ばれてきた。Stereotype がモデル要素に適用され
  ているとき、Tag Definitions の値のことを慣習的に `tag values` という呼び方をす
  る。

* それの Profile または Package は Stereotype にとっての名前空間を定義する。

  * Profiles が Package に適用されていると、利用可能な Stereotypes は適用された
    Profiles により定義され、必要ならば、異なる Profiles や Packages にある同じ
    ``name`` のStereotypes を見分けるために、完全限定名を使ってこれらの
    Stereotypes を表示することができる。

  * PackageImport と ElementImport を限定されていない ``names`` の使用を許すため
    に用いることができる。
  * 適用された Profile が直接所有する Stereotypes (``ownedStereotypes``) を限定
    名を用いずに用いてよい。

12.3.3.5 Images
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Image クラスは図式中の画像を表示するのに必要な情報を与える。Icons は典型的には
  Image クラスで扱われる。
* 物理的配置や画像形式のような情報は Image クラスにより与えられる。
* ``format`` 特性は内容の形式を示し、文字列 ``content`` がどのように解釈されるべ
  きかである。

  * 値 ``SVG``, ``GIF``, ``PNG``, etc. が予約されている。
  * 加えて ``MINE:`` から始まる何らかの値も予約済みとする。

12.3.3.6 Extensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Extension はメタクラスの特性が Stereotype で拡張されていることを示すために用い
  られ、クラスに対してステレオタイプを柔軟に追加（そしてあとで除去）する能力を与
  える。
* Extension は Association の一種である。Extension の一端はふつうの Property で
  あり、他方は ExtensionEnd である。前者は Extension と Class とを結び付け、対し
  て後者は Extension とその Class を拡張する Stereotype とを結びつける。
* 必要 Extension (``isRequired == true``) とは、この Stereotype のオブジェク
  トが、それが含んでいる Profile が適用されているモデル内の拡張メタクラスのオブ
  ジェクトそれぞれにリンクされる必要があることを意味する。
* 不要 Extension (``isRequired == false``) とは、この Stereotype のオブジェ
  クトが、拡張メタクラスのオブジェクトに自由にリンクし、またあとで自由に削除され
  ることが許されることを意味する。
* Figure 12.15 MOF Model Equivalent to Extending "Interface" by the "Home"
  Stereotype

  * 単一メタクラス拡張について同値な MOF 構成を示す図。
  * Figure 12.19 で示される場合を図解する。

* Constraints は Stereotypes によく追加される。
* Figure 12.16 Example of Multiple Metaclass Extension

  * 複数メタクラス拡張の例。

* Figure 12.17 MOF Model Equivalent to Multiple Metaclass Extension

  * 複数メタクラス拡張に対応する同等な MOF 構成の図。

12.3.3.7 ExtensionEnd
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ExtensionEnd はメタクラスを拡張する際に Extension と Stereotype を結ぶのに用い
  られる。
* ExtensionEnd の既定の多重度は ``0..1`` である。

12.3.4 Notation
----------------------------------------------------------------------

* Figure 12.18 The Notation for an Extension

  * Extension の記法は矢印である。
  * 矢先は黒塗の三角。
  * 向きは Stereotype から拡張 Class とする。
  * Association と同じ修飾をしてもよいが、通常は省略し、
    航行可能の矢印は決して示さない。

  * ``isRequired`` == ``true`` ならば ExtensionEnd の近くに ``{required}`` と記
    す。

    * 多重度の明記とも関係している。

* Profile は Package と同じ記法を用いる。ただし名前の前または上にキーワード
  ``«profile»`` をつける。

  * ``metaclassReference``, ``metamodelReference`` は ``elementImport``,
    ``packageImport`` とそれぞれ同じ記法プラスキーワード ``«reference»``。

* ProfileApplication は破線矢印で示す。

  * 矢先は開く。
  * 向きは Package から各 ``appiled`` Profile に向かう。
  * キーワード ``«apply»`` か、``isStrict`` が ``true`` ならばキーワード
    ``«strict»`` を矢印のラベルとする。

* 複数の ``appliedProfiles`` に同名の Stereotypes があれば、必要に応じてその
  Stereotype の名前を限定 (qualify) する。
* Stereotype は Class と同じ記法を用いる。ただし名前の前または上にキーワード
  ``«stereotype»`` をつける。

  * モデル要素が図式的に表示されているとき、カッコ対が要素の右上に現れる。
  * 複数の Stereotypes が適用されているならば、それらの名前をカッコ内に CSV とし
    て示す。
  * 拡張モデル要素にキーワードがあるときは、ステレオタイプ名はそのキーワードの近
    くに表示されるだろう。一つのカッコに名前をまとめてもよいし、別々のカッコを用
    いてもよい。

* Stereotype の ``name`` はクラスの命名規約に従い大文字で始めるのが普通。しかし
  Profiles は異なる規約を用いてよい。
* ツールは Stereotypes を表示するのかしないのかを選ぶことができる。
* モデル要素に適用された Stereotype またはその一般化の ``ownedAttributes`` の値
  は次の三者の方法のうちの一つでわかる。

  #. モデル要素を表す図表ノードに接続された註釈記号の部分として
  #. モデル要素を表す図表ノードの分かれた区画で
  #. 図表ノードで ``name`` 文字列の上または名前文字列の前に

* 区画または註釈記号が使われていると、ステレオタイプの名前を区画や註釈に含まれて
  いるのみならず、``name`` 文字列の前に guillemets で示してよい。
* Stereotype Property が多価値ならば、``<valuestring>`` は CSV として表示する。
* Stereotype Property の値を表示するのに区画が使われていれば、適用された
  Stereotype それぞれに対してその Property の値が表示されることになる追加区画が
  必要となる。
* 註釈記号の場合、またはもしモデル要素の ``name`` の前か上に表示されるならば、特
  定の Stereotype からの Property の値は適用された Stereotype の名前が
  guillemetsの対に括られた状態で任意で先に来る。
* 区画または註釈記号で表示されているときは、名前文字列と値文字列の高々一対が単一
  行に現れることができる。

12.3.4.1 Icon presentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Stereotype に Images を添えることが、その Stereotype が適用されたモデル要素の
  記法の代わりに、またはさらなる普通の記法として可能である。
* Stereotype に ``icon`` に対する値があると、参照された Image をStereotype が適
  用されたモデル要素に対して図式的に添えることができる。
* 図表的表現を有するすべてのモデル要素がアイコンを付けることが可能。モデル要素が

  * 箱として図表的に表現されると、箱が Image に取って代わられ、モデル要素の
    ``name`` が Image の下に現れる。この表現の選択は、モデル要素に単一の
    Stereotype が適用されており、モデル要素の Properties がない場合だけ可能であ
    る。

    また別の選択として、Image の縮小版をモデル要素を表現する箱の内側上部に表示し
    てもよい。複数の Stereotypes が適用されているときは、複数の Images を箱で表
    示してよい。

  * 線として図表的に表現されると、Image を線の近くに置いてよい。
  * テキスト記法として図表的に表現されると、Image をテキスト表記の左に表示してよ
    い。

* Images のいくつかは Stereotype の ``icon`` Property によって参照されてよい。
* モデル要素には既定の表現をするための ``icon`` をすでに使うものもある。この典型
  的な例には Actor モデル要素があり、これは「棒人間」のアイコンを用いる。

12.3.5 Examples
----------------------------------------------------------------------

* Figure 12.19 Example of Using an Extension

  * ここで ``Home`` はメタクラス Interface を拡張するステレオタイプである。
  * ステレオタイプ ``Home`` のオブジェクトはクラス Interface のオブジェクトに追
    加することとオブジェクトから除去することが意のままにできる。

* Figure 12.20 Example of a Required Extension

  * Profile が適用されるモデルにあるメタクラス Component のオブジェクトはそれぞ
    れが、Extension の ``isRequired`` が ``true`` であるので、ステレオタイプ
    ``Bean`` のオブジェクトに適用するはずである。

  * ``{required}`` が付いているので、その Profile が適用されている Component の
    各オブジェクトは、ステレオタイプ ``Bean`` のオブジェクトを適用するはずであ
    る。
  * モデルはそのような Stereotype が適用されなければ well-formed でない。

* Figure 12.21 Defining a Simple EJB Profile

  * ある EJB Profile の簡単な見本。
  * ``Bean`` がメタクラス Component に適用されていることを必要とする。``Bean``
    は抽象的なので、具象サブクラスである ``Entity`` か ``Session`` のどちらかの
    オブジェクトが Component の各オブジェクトにリンクされていなければならない。

* Figure 12.22 Importing a Package from a Profile

  * ``Types`` と ``Factory`` は素の Package である一方、``Manufacturer`` は
    Profileである。
  * ``Manufacturer`` は ``Types`` をインポートしているので、``Device`` という
    Stereotype の Properties の ``type`` として ``Color`` と ``JavaInteger`` が
    用いられる。
  * Profile ``Manufacturer`` があとで Package に適用されるならば、``Types`` 由来
    の型は Profile が適用される Package では（明示的にパッケージ ``Types`` をイ
    ンポートしない限りは）利用できない。この例では ``Factory`` が ``Types`` を別
    個にインポートしているのでその限りである。

* Figure 12.23 Profiles Applied to a Package

  * プロファイル Java および EJB が与えられると、Package ``WebShopping`` にどの
    ようにそれらが適用されればよいのかを示す。

* Figure 12.24 Defining a Stereotype

  * 簡単なステレオタイプ ``Clock`` が、自在にメタクラス Class のオブジェクトに対
    して（動的に）適用可能であるように定義されている。

* Figure 12.25 Presentation Options for an Extended Class

  * 上記 ``Clock`` の数通りの表現例。
  * 本文中にはこの見本のための言及がない。

* Figure 12.26 An Instance Diagram when Defining a Stereotype

  * かなり込み入ったオブジェクト図。先ほどの ``Clock`` の定義を表現している諸オ
    ブジェクトを示している。
  * ``Clock`` から左側の理解が重要。

* Figure 12.27 Defining Multiple Stereotypes on Multiple Stereotypes

  * ``Clock`` が Component と Class の両方を拡張することを示す。
  * それとは別に ``Creator`` という、Class を拡張する Stereotype を定義してい
    る。

* Figure 12.28 Using a Stereotype

  * クラス ``StopWatch`` に ``Clock`` を適用した。単に ``«Clock»`` をクラス名の
    上に付記するだけで示せる。

* Figure 12.29 Showing Values of Stereotypes and a Simple Instance Specification

  * 上記の適用の意味するところを表現する図式。

* Figure 12.30 Using Stereotypes and Showing Values

  * ``StopWatch`` に ``Clock`` と ``Creator`` を同時に適用する。
  * ここでは各 Stereotype の Property 値を註釈記法で示してある。

* Figure 12.31 Other Notational Forms for Depicting Stereotype Values

  * Stereotype の Property 値を記述する代わりの記法の例。
  * 属性区画に ``«Clock»`` と断ってから値を列挙。
  * 中括弧記法があるようだ。

* Figure 12.32 Example of a Profile defining Classes and (...)

  * クラス、二項合成（および非合成）関連を定義する、とある Profile の見本。

  * Profile ``IssuesProfile`` が Profile ``uml`` をインポートしていることをわざ
    わざ図式内の上部にて断っている。
  * 本文ではこの図に相当する XMI コード全体を掲載している。

* Figure 12.33 Diagram example of applying a profile defining Classes and
  Associations and  (...)

  * 上記 ``IssuesProfile`` の適用例。
  * Profile ``IssueExample`` は ``IssuesProfile`` を適用している。
  * 重要なのは矢印のラベルに現れる ``«IssueTag»`` の意味だ。
  * 本文ではこの図のオブジェクト部分を表現する XMI コードと、リンク部分を表現す
    る XMI コードを分けて掲載している。

12.4 Classifier Descriptions
======================================================================

機械生成による節。

12.5 Association Descriptions
======================================================================

機械生成による節。

.. include:: /_include/uml-refs.txt
