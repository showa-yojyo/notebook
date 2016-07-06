======================================================================
12 Packages
======================================================================
UML 2.5 pp. 239-282 に関するノート。

.. todo:: 最低でもあと一回は編集する。

.. contents:: ノート目次
   :depth: 2

12.1 Summary
======================================================================
* Packages は UML の主な包括的な構造化および組織化能力を与える。
  Models に関する特殊化および
  UML に対する拡張を組織化する Profiles に関する特殊化がある。

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

A_packagedElement_owningPackage
  * Package から PackageableElement への composite 関連（単方向）。
  * Package は Namespace であり、所有要素を関連端 packagedElement で表現する。
  * A_ownedMember_namespace を subsets する。

  A_ownedType_package
    * Package から Type への composite 関連（双方向）。
    * Type である内容物への参照を表現する関連。
    * A_packagedElement_owningPackage を subsets する。

  A_nestedPackage_nestingPackage
    * Package から Package への composite 関連（双方向）。
    * Package である内容物への参照を表現する関連。
    * A_packagedElement_owningPackage を subsets する。

A_packageMerge_receivingPackage
  * Package から PackageMerge への composite 関連（双方向）。
  * 関連端 ``receivingPackage`` 側の Package が合併前後で構成要素が増える方を指す。
  * A_ownedElement_owner と A_source_directedRelationship を subsets する。
  * 関連端 ``receivingPackage`` の多重度はちょうど 1 である。
  * cf. A_mergedPackage_packageMerge

A_mergedPackage_packageMerge
  * PackageMerge から Package への関連（単方向）。
  * 関連端 ``mergedPackage`` は合併前後でその構成内容物が変わらない方を指す。
  * A_target_directedRelationship を subsets する。
  * 関連端 ``mergedPackage`` の多重度はちょうど 1 である。
  * cf. A_packageMerge_receivingPackage

12.2.3 Semantics
----------------------------------------------------------------------
12.2.3.1 Package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Package はそれの ``members`` についての名前空間であり、
  ``packagedElement`` で結び付けられた構成員の要素を含み、
  インポートされたものを含む。

* Package の定義は他の Packages の内容を、
  自分の包含要素の合併 (merging) により拡張することが可能である。

* Package をテンプレートとして定義してよく、
  他のテンプレートに対して束縛してもよい。

  * 詳しくは :doc:`./common-structure` を参照。

* URI を Package にとって一意な識別子を与えるように指定することが可能である。
  UML 内部では、プロファイルを除いた場合では、
  前もって決定されたこれにとっての利用法はない。

12.2.3.2 PackageMerge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* PackageMerge とは、
  下で定義される規則集に従って、
  対象の ``mergedPackage`` の内容が
  出処の ``receivingPackage`` に結合されることを示す
  ふたつの Packages 間の有向関係である。

* Generalization と同じように、
  Package は自分自身を合併することは
  直接的、間接的を問わず許されない。

* この能力は、
  さまざまな Packages で定義された要素が同じ ``name`` であり、
  同じ概念を意図するときに用いられるべく設計されている。

* 受け手側 Package に含まれるモデル要素に対する参照のどれもが、
  Package に含まれる増分に対してではなく、
  合併結果に対する参照を含意する。

* Figure 12.2 Illustration of the Meaning of Package Merge

  * P2::A は P1::A の増分を定義する。

  * P3::SubA は P2::A のサブクラスの定義である。
    P3 から見ると、P2::A は P1 と P2 の間のマージ結果の A を表現していると解釈する。

  * P1: ``mergedPackage`` (target)
  * P2: ``receivingPackage`` (source, owner) であると同時に
    ``resultingPackage``

    * マージの before/after で同じところにあるものの呼び方が変わる
      (receiving/resulting) ことがわかればとりあえず読める。

* PackageMerge は
  合併される Package の内容を受け手側の内容と結合することによって、
  （それ自身が変換の集合である）操作として考察することができる。

* PackageMerge の規則を理解するには、
  三種の別個の実体の間をはっきりと見分ける必要がある：

  #. ``mergedPackage``
  #. ``receivingPackage``
  #. 合併変換の結果

.. todo::

   各種用語の導入。

   * この専門用語は Figure 12.3 の図解により表される PackageMerge の概念上の見方に基づく。

* Figure 12.3 Conceptual View of the Package Merge Semantics

  * 図の右側は UML の図式ではない。
  * この B ダッシュを意識することがコツだと言っている。

* PackageMerge の意味は制約と変換の集合で定義される。
  制約は有効な PackageMerge にとっての事前条件を指定し、
  それに対して、変換はその意味的な効果（事後条件）を記述する。
  制約のいくつかが破られていれば
  PackageMerge は ill-formed であり、それを含むモデルは無効ある。

  * その「集合」が pp. 240-245 で文書化されている。
    もしマージの仕様を詳しく把握する状況になったら、ここを参照すること。

* この仕様では、
  他の種類の要素メタタイプ（例えば状態機械や相互作用）の意味が
  複雑かつ領域固有であるので、
  明示的な合併変換は一定の一般的メタモデル
  (Packages, Classes, Associations, Properties, etc.) に
  たいてい見出される要素メタタイプについてしか定義されていない。

12.2.3.3 General Package Merge Rules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* 合併される要素と受け取る要素が一致する (match) とは、
  それらがそれらのメタタイプについての一致規則を満足することを言う。

.. todo:: 規則集を消化する。

12.2.3.4 Package Rules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Package の種類の Elements は ``name`` およびメタタイプにより一致する。

.. todo:: 規則集を消化する。

12.2.3.5 Class and DataType Rules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Class や DataType の種類の Elements は ``name`` およびメタタイプにより一致する。

.. todo:: 規則集を消化する。

12.2.3.6 Property Rules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Property の種類の Elements は ``name`` およびメタタイプにより一致する。

.. todo:: 規則集を消化する。

12.2.3.7 Association Rules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Association の種類の Elements は ``name`` およびメタタイプにより一致する。

.. todo:: 規則集を消化する。

12.2.3.8 Operation Rules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Operation の種類の Elements は ``name``, Parameter の順序および
  Parameter の型により一致する。戻り値の型のいずれも含まない。

.. todo:: 規則集を消化する。

12.2.3.9 Enumeration Rules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* EnumerationLiteral の種類の Elements は
  所有する Enumeration およびリテラル ``name`` により一致する。

.. todo:: 規則集を消化する。

12.2.3.10 Constraint Rules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. todo:: 規則集を消化する。

12.2.3.11 Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Model とはシステムの記述である。
  ここでシステムは、
  最も幅広い意味で意図されていて、
  ソフトウェアやハードウェアだけでなく、組織や工程をも含んでよい。

* Package と同じように、Model は
  モデル化されているシステムを協力して記述する ``members`` の集合を持つ。

* 種々の Models を同じシステムに対して定義することが可能であり、
  典型的にはこの種々の Models は相補的であり、
  種々のシステム利害関係者の観点から定義されている。

* Model は次のものの間にある Abstraction Dependencies を持つことが可能。

  * refinement （標準プロファイル ``«Refine»`` でステレオタイプされる）
  * mapping （例えば標準プロファイル ``«Trace»`` でステレオタイプされる）

12.2.4 Notation
----------------------------------------------------------------------
* Package は大きい矩形の左上に小さい矩形（タブ）を付けた形状で示す。

  * Package の内容物は大きい矩形の内部に示してよい。
  * マルにプラスを付けた記号を使って、
    Package の外部から要素に線を引くような記法がある。

  * PackageImport や ElementImport を通じて持ち込んだ要素は、
    色を変えて描かれることがある。

  * Package の名前は内容物が大きい矩形内にあるかどうかで、場所が異なる。
    タブに記される場合と、大矩形内に記される場合がある。

  * 要素の可視性はいつものように要素名の前に ``+``, ``-`` 等の記号を付して示してもよい。

    * Packages の可視性が protected や package であることは許されない。

  * URI を ``{uri = <uri>}`` の形式でパッケージ名の後に示してよい。

* PackageMerge は開いた矢先を持つ破線矢印を用いて示す。

  * 矢印の向きは ``receivingPackage`` から ``mergedPackage`` である。
  * キーワード ``«merge»`` を破線のそばに示す。

* Model は通常の Package シンボルに小さな三角を大矩形の右上隅に描いたもので記す。

  * 大矩形内部に要素が示されているならば、
    小三角はタブの右側に描いてよい。

  * またはキーワード ``«model»`` をモデル名の上に付記することで、
    あとは通常の Package の記法を用いることもまた許される。

12.2.5 Examples
----------------------------------------------------------------------
* Figure 12.5 Examples of a Package with Members

  * どの図式でも Package の内容物がすべて記されているとは限らないようだ。
  * マルプラスの見本によると、線のスタイルは実線。

* Figure 12.6 Simple Example of Package Merge

  * もっとも基本的な見本と思われる。

* Figure 12.7 Simple Example of Transformed Packages Following the Merges

  * 上述の結果、各パッケージがどういう構成になるかを模式化したもの。
    各要素の意味が明記されていないので、
    このマージ結果の表現が妥当かどうか納得するには、
    先程読み飛ばした規則集を当たらねばならない。

  * ここで用いられている記法は UML の一部ではないので注意。

* Figure 12.8 Introducing Additional Package Merges

  * 空の Package T が上述の R と S をマージする図式。
    T が空であるというのは、図式外で説明されているに過ぎない。

* Figure 12.9 Result of the Additional Package Merges

  * 上述の T のマージ状態を模式化したもの。

* Figure 12.10 Three Models Representing Parts of a System

  * Client, Business, Data からなる三層構造システムの Models の図式。

* Figure 12.11 Two Views of One System Collected in a Container Model

  * Models-in-Model な図式。
    同一図式内にあえて異なる記法（キーワード or 小三角）を併用している。

12.3 Profiles
======================================================================

12.3.1 Summary
----------------------------------------------------------------------
* この章では、メタクラスが
  種々の目的に適合するように拡張できるようになる能力を記述する。

* これは UML メタモデルを J2EE や .NET 等の
  さまざまなプラットフォームや
  領域（リアルタイムまたはサービス志向様式）に合わせる能力も含む。

* この章は OMG MOF_ に対して一貫性がある。

12.3.1.1 Positioning Profiles versus Metamodels, MOF and UML
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* UML は
  モデリングを取り扱うさまざまな OMG の仕様書で
  別々のメタレベルで再利用される。

* Profiles は第一等の拡張能力ではない。
  すなわち、新たなメタモデルを創造することは考慮に入れていない。

* 第一等の拡張性は MOF_ で扱われるが、
  メタモデルレベルにおける制限はひとつもない。
  サブクラスと関連を必要に応じて追加することができる。

* UML を拡張するのがよいかもしれない理由がいくつかある。

  * 特定のプラットフォームやドメインに適合される用語法 (a terminology) を与える。
  * 記法を持たぬ諸構成概念に構文を与える。
  * 既存の諸記号に異なる記法を与える。
  * UML や特定のメタクラス (pl.) にさらなる意味を追加する。
  * UML に存在しない型を追加する。
  * UML の諸構成概念で用いられるやり方に制限を加える Constraints を追加する。
  * あるモデルを別のモデルやコードに変換する際に用いることが可能な情報を追加する。
    例えばモデルと Java コードの間の対応規則の定義など。

* いつ新しいメタモデルを作成するべきか、
  いつプロファイルを作成するべきか、
  あるいはいつ両者を
  （一方は UML ツール利用の場合に、もう一方は MOF ベースのツールの場合に）
  作成するべきかという問いに対する簡単な答えはない。

12.3.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 12.12 Profiles

  * 一見するとグラフの構造がいつもより込み入っている。
  * 新クラスは Profile, ProfileApplication, Stereotype, Image,
    Extension, ExtensionEnd と、いつもより多く登場する。

A_metaclassReference_profile
  * Profile から PackageImport への composite 関連（単方向）。
  * A_packageImport_importingNamespace を subsets する。
  * cf. A_metamodelReference_profile

A_metamodelReference_profile
  * Profile から ElementImport への composite 関連（単方向）。
  * A_elementImport_importingNamespace を subsets する。
  * cf. A_metaclassReference_profile

A_appliedProfile_profileApplication
  * ProfileApplication から Profile への関連（単方向）。
  * Package に適用されている Profile を参照する関連である。
  * A_target_directedRelationship を subsets する。
  * cf. A_profileApplication_applyingPackage

A_profileApplication_applyingPackage
  * Package から ProfileApplication への composite 関連（双方向）。
  * Package が Profile 適用情報を所有する。
  * A_source_directedRelationship と A_ownedElement_owner を subsets する。
  * cf. A_appliedProfile_profileApplication

A_profile_stereotype
  * Stereotype から Profile への関連（単方向）。
  * 自らを直接的にまたは間接的に含む Profile への参照を示す。
  * 関連端 profile は ``{readOnly}`` である。
  * 関連端 profile の多重度は 1 である。

A_icon_stereotype
  * Stereotype から Image への composite 関連（単方向）。
  * Stereotype を図式内でアイコンイメージを用いて表示する際、
    その中身の場所を参照する。
  * A_ownedElement_owner を subsets する。

A_ownedStereotype_owningPackage
  * Package から Stereotype への composite 関連（単方向）。
  * ある適用済み Profile が直接る Stereotype を所有するという意味か。
  * A_packagedElement_owningPackage を subsets/redefines する。
  * 関連端 ownedStereotype は ``{readOnly}`` である。

A_ownedEnd_extension
  * Extension から ExtensionEnd への composite 関連（単方向）。
  * 拡張されているメタクラスへの参照する。
  * A_ownedEnd_owningAssociation を redefines/subsets する。

A_extension_metaclass
  * Class から Extension への関連（双方向）。
  * メタクラスを拡張する Stereotype を参照する関連端を所有する。
  * 関連端は両方とも ``{readOnly}`` である。
  * 関連端の多重度は ``metaclass`` が 1 に対して
    ``extension`` が ``*`` である。

A_type_extensionEnd
  * ExtensionEnd から Stereotype への関連（単方向）。
  * メタクラスを拡張する Stereotype を参照する。
  * A_type_typedElement を redefines/subsets する。

12.3.3 Semantics
----------------------------------------------------------------------
12.3.3.1 Profiles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Profile とは、下に述べるように、
  UML を拡張するのに用いることができるメタモデルの制限された形式である。
  その主要な拡張構成要素は Stereotype である。

12.3.3.1.1 Restricting Availability of UML Elements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* ``metaclassReference`` ElementImports と
  ``metamodelReference`` PackageElements は
  Profile の選別規則を指定するのに用いることが許される。
  この選別規則は Profile が適用されるときに
  どの要素が利用可能であり、どの要素が隠れるのかを決定づける。

* モデルに Profile を適用することはそのモデルを決して変化させるものではない。
  根底にあるモデルの眺めを単に定義するものである。

* メタクラスが隠されている（利用不能となる）ことの影響は次のとおり：

  * 当該メタクラス（またはそのサブクラス）の新たなオブジェクトを生成することはできない。

  * 当該メタクラス（またはそのサブクラス）の既存のオブジェクトは
    もはや図式上で見ることができなくなるか、
    ブラウザー枠内を含む、リストで選択できなくなる。

  * 当該メタクラス（またはそのサブクラス）の既存のオブジェクトに関する
    Relationships は
    もはや図式上で見ることができなくなるか、
    ブラウザー枠内を含む、リストで選択できなくなる。

* 上記をどのように実装するかはツールによって異なってよい。

* 選別規則が Profile で活動的になるためには、
  Profile が厳格モードで適用される必要がある。これには
  ProfileApplication の ``isStrict`` 属性を明示的に true とする必要がある。
  さもなければ選別規則はこの ProfileApplication に関して無視される。

* もっともありがちなことは、
  Profile が UML 自身を ``metamodelReference`` を使ってインポートするときである。

* ElementImports の ``visibility`` および ``alias`` 特性は
  ``metaclassReference`` として用いられるときには無視される。

* ``metaclassReference`` と ``metamodelReference`` の両方が
  Profile に存在すると、後者は無視されて特定のメタクラスだけが
  使用可能になる。

* 詳しくは、次の規則が使われて、
  Profile が厳格モードで適用された後に
  モデル要素が利用可能なのかどうかを決定づける。
  メタクラスおよびそのオブジェクトが利用可能であるとは、それらが

  #. 明示的な ``metaclassReference`` により参照されるか、

  #. ``metaclassReference`` がないときは、
     明示的な ``metamodelReference`` により参照される
     Package の直接的または推移的な ``members`` であるか、

  #. 適用された Profile の ``member`` である Stereotype により
     拡張されているときである。

* Profile が厳格モードで適用されているときは
  他のモデル要素のすべてが隠蔽、利用不能にされる。

* このことは利用可能なメタクラスの互いに素な集合らを指定する
  適用 Profile の組み合わせを無効にする。

* Profile P1 が別の Profile P2 をインポートすると、
  ``metaclassReference`` と ``metamodelReference`` の関連すべてが
  P1 の高さで結合されることになり、選別規則がこの和集合に適用する。

* Profile は Stereotypes ばかりでなく
  Classes, Associations, DataTypes, PrimitiveTypes そして Enumerations を
  定義またはインポートすることができる。

* Profile 定義の Types はその Profile の Properties の型としてか、
  別の Profile 定義の Type の一般化 classifier としてしか用いることはできない。

* Stereotypes は二項 Associations にしか参加することができない。

* ツールが与えることが可能な Profile の能力のもっとも真っ直ぐな実装は、
  Profile メタモデルと同じように、
  実装を基にしたメタモデルを持つことである。

12.3.3.1.2 Integrating and Extending Profiles
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* Profiles を生成、拡張、統合する方法はいくつかある。

* Profile 統合のもっとも簡素な形式は、
  単に複数 Profiles を同じ Package に適用することである。

* ひとつの Profile が別のものの全部または一部を再利用したり、
  他の Profiles を拡張したりすることも可能である。

* 例えば the *Unified Profile for DoDAF and MODAF* (UPDM) Profile は
  Requirement や ViewPoint のような Stereotypes を再利用するために
  SysML Profile に統合することも可能であった。

  .. note::

     この文から始まるパラグラフは面白そうだが、
     パッと見 could や would を含む文が多いので、
     どうも現実にある状況の話題ではなさそうだ。

12.3.3.1.3 MOF-Equivalent Semantics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* この節では Stereotypes とそのオブジェクトの意味を
  MOF_ を使って明確に述べる。

* MOF に対する同じ写像が
  どのように適用プロファイルを XMI を使って直列化するのかを決定するために
  用いられる。

* Profile の場合、Package から継承した `URI` Property が用いられて、
  XMI の Profile のオブジェクトを識別するのに用いられる nsURI を決定付ける。

* UML Standard Profile のような OMG に規範的な Profiles は、
  URI に対して OMG に規範的な名前付け戦略に追随する。

* Profile はちょうど任意のモデルのように
  XMI ファイルとして交換可能であり、
  適用された Profile があるモデルもまた交換可能である。

.. * Figure 12.19 shows...

.. * 下の最初の直列化では
..   Figure 12.19 のモデルがどのようにして交換可能となるのかがわかる。

* Figure 12.13 Using the HomeExample Profile to Extend a Model

  * ステレオタイプ Home で拡張された Interface のオブジェクトを含むモデル。

* ゼロまたはそれを超える Profiles が適用されているモデルの
  XMI 直列化はふたつの論理部分に（物理的に組織化されていてもよい）
  組織化された XMI ファイルである。

  #. モデルの XMI 直列化
  #. モデルまたはそのある部分に対する Profile の適用それぞれに
     対応するオブジェクトの XMI 直列化

* モデルまたはそのある部分に対する Profile の適用を削除することが
  モデル自身の XMI 直列化を修正してはならないので、
  Part (1) にある XMI 要素はすべて
  Part (2) にある XMI 要素のどれに対する参照を持つことはできない。

.. * 下の XMI では Figure 12.13 のモデルがどう XMI に直列化されるかがわかる。

12.3.3.2 Defining Profiles for Non-UML Metamodels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* 理論上、
  この能力はまれにしか、あったとしても、実用上では使われてこなかったが、
  Profiles の能力は UML 以外のメタモデルに
  ついての拡張を定義することが可能である。

* UML に加えて、
  Profile は別の MOF 準拠の参照メタモデルに関係してよい。
  一般に参照メタモデルは、
  典型的にはインポートされたか局地的に所有されたかのどちらかである
  メタクラスからなる。

* Profile を適用することはそのモデルを決して変化させるものではない。
  根底にあるモデルの眺めを単に定義するものである。

  * 先にもこれを記した気がする。

* 一般には、
  プロファイルが適用されると、
  インポートされた参照メタモデルのオブジェクトである
  モデル要素しか見えないはずである。

* 次の規則が使われることで、
  Profile 適用後にモデル要素が利用可能か隠蔽されるかを決定づける。
  モデル要素が利用可能であるとは、
  それらが以下のどれかのメタクラスのオブジェクトである

  #. 明示的な ``metaclassReference`` により参照されるか、

  #. 明示的な ``metamodelReference`` により参照される
     Package に（直接的または推移的に）含まれるか、

  #. 適用された Profile により所有される Stereotype により拡張される。

* Profile が適用されていると他のモデルはすべてが隠蔽される（利用不能となる）。

* もっとも普通の場合は、
  Profile がメタモデル丸ごとを ``metamodelReference`` を使って
  単にインポートするときである。

* Figure 12.14 Specification of an Available Metaclass

  * MyMetamodel はふたつのメタクラス Metaclass1 と Metaclass2 を含む
    メタモデルである。

  * MyProfile は MyMetamodel と Metaclass2 を参照する Profile である。

  * しかし、Metaclass2 に対する明示的なメタクラス参照もある。
    これはメタモデル参照を上書きする。

12.3.3.3 ProfileApplication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ProfileApplication はどの Profiles が Package に適用されているのかを
  記録するのに用いる。

* UML を拡張するひとつまたはそれを超える Profiles は
  思いのままにモデル Package に適用して構わない。

  * Profile を適用するということは、
    Profile の部分として定義された Stereotypes を適用することが
    可能であることを意味する。

* Profile が適用されると、
  適当な Stereotypes のオブジェクトが
  ExtensionEnds が ``isRequired`` が true である
  メタクラスのオブジェクトであるものの要素に対して
  生成される必要がある。

* 一度 Profile が Package に適用されると、
  適用された Profile を自由に取り除くことが許される。

  * Profile を取り除くことは、
    Profile で定義される Stereotypes のオブジェクトである要素すべてが、
    それらが合成集約する Profile 定義の Classes のオブジェクトと
    それらをリンクする Profile 定義の合成 Associations とを含めて、
    削除されることを意味する。

* 別の Profile の ``packagedElement`` である Profile を
  個々に適用することができる。
  とは言うものの、
  入れ子の Profile が Stereotypes を含み、他の Profiles が共に適用されていることを示す
  ために PackageImport を使うことができると、
  その Profile は
  必要とされるメタクラス・メタモデル参照をどれも指定する必要がある。

12.3.3.4 Stereotypes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Stereotype は一つまたはそれを超えるメタクラスについての拡張を定義し、
  固有の用語または記法の用途が
  拡張メタクラスに対して用いられるものを
  上書きや追加できるようにする。

  * Stereotype がメタクラスをいくつか拡張すると、
    どの時点においてもメタクラスのうち
    正確に一つのオブジェクトにしか適用することができない。

* Stereotype とは、それ自身により使われることがあり得ないが、
  それを拡張するメタクラスのうちのひとつと一緒に常に用いられる必要がある、
  メタクラスの限定された一種である。

* ``metaclassReference`` により参照されるか、
  Stereotype を直接または間接的に含むもっとも近い Profile の
  ``metamodelReference`` により参照される Package に含まれるメタクラスはいずれも
  その Stereotype によって拡張することができる。

  * 例えば、その ``metamodelReference`` が UML ならば、
    States, Transitions, Activities, UseCases, Components, Properties, Dependencies,
    etc. はすべて Stereotypes で拡張が可能である。

* Class と同じようにして、Stereotype は Properties を持つことが許されるが、
  それは習慣的に Tag Definitions と呼ばれてきた。
  Stereotype がモデル要素に適用されているとき、
  Tag Definitions の値のことを慣習的に `tag values` という呼び方をする。

* それの Profile または Package は Stereotype にとっての名前空間を定義する。

  * Profiles が Package に適用されていると、
    利用可能な Stereotypes は適用された Profiles により定義され、
    必要ならば、
    異なる Profiles や Packages にある同じ ``name`` の
    Stereotypes を見分けるために、
    完全限定名を使ってこれらの Stereotypes を表示することができる。

  * PackageImport と ElementImport を
    限定されていない ``names`` の使用を許すために用いることができる。

  * 適用された Profile が直接所有する Stereotypes (``ownedStereotypes``) を
    限定名を用いずに用いてよい。

12.3.3.5 Images
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Image クラスは図式中の画像を表示するのに必要な情報を与える。
  Icons は典型的には Image クラスで扱われる。

* 物理的配置や画像形式のような情報は Image クラスにより与えられる。

* ``format`` 特性は内容の形式を示し、
  文字列 ``content`` がどのように解釈されるべきかである。

  * 値 ``SVG``, ``GIF``, ``PNG``, etc. が予約されている。
  * 加えて ``MINE:`` から始まる何らかの値も予約済みとする。

12.3.3.6 Extensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Extension はメタクラスの特性が Stereotype で
  拡張されていることを示すために用いられ、
  クラスに対してステレオタイプを柔軟に追加（そしてあとで除去）
  する能力を与える。

* Extension は Association の一種である。
  Extension の一端はふつうの Property であり、
  他方は ExtensionEnd である。
  前者は Extension と Class とを結び付け、
  対して後者は Extension とその Class を拡張する Stereotype とを結びつける。

* 必要 Extension (``isRequired`` == true) とは、
  この Stereotype のオブジェクトが、
  それが含んでいる Profile が適用されているモデル内の拡張メタクラスの
  オブジェクトそれぞれにリンクされる必要があることを意味する。

* 不要 Extension (``isRequired`` == false) とは、
  この Stereotype のオブジェクトが、
  拡張メタクラスのオブジェクトに自由にリンクし、
  またあとで自由に削除されることが許されることを意味する。

* Figure 12.15 MOF Model Equivalent to Extending "Interface" by the "Home" Stereotype

  * 単一メタクラス拡張について同値な MOF 構成を示す図。
  * Figure 12.19 で示される場合を図解する。

* Constraints は Stereotypes によく追加される。

* Figure 12.16 Example of Multiple Metaclass Extension

  * 複数メタクラス拡張の例。

* Figure 12.17 MOF Model Equivalent to Multiple Metaclass Extension

  * 複数メタクラス拡張に対応する同等な MOF 構成の図。

12.3.3.7 ExtensionEnd
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ExtensionEnd はメタクラスを拡張する際に
  Extension と Stereotype を結ぶのに用いられる。

* ExtensionEnd の既定の多重度は 0..1 である。

12.3.4 Notation
----------------------------------------------------------------------
* Figure 12.18 The Notation for an Extension

  * Extension の記法は矢印である。
  * 矢先は黒塗の三角。
  * 向きは Stereotype から拡張 Class とする。
  * Association と同じ修飾をしてもよいが、通常は省略し、
    航行可能の矢印は決して示さない。

  * ``isRequired`` == true ならば ExtensionEnd の近くに ``{required}`` と記す。

    * 多重度の明記とも関係している。

* Profile は Package と同じ記法を用いる。
  ただし名前の前または上にキーワード ``«profile»`` をつける。

  * ``metaclassReference``, ``metamodelReference`` は
    ``elementImport``, ``packageImport`` とそれぞれ同じ記法プラス
    キーワード ``«reference»``。

* ProfileApplication は破線矢印で示す。

  * 矢先は開く。
  * 向きは Package から各 appiled Profile に向かう。
  * キーワード ``«apply»`` か、
    ``isStrict`` が true ならばキーワード ``«strict»`` を矢印のラベルとする。

* 複数の ``appliedProfiles`` が同名の Stereotypes を持つならば、
  必要に応じてその Stereotype の名前を限定 (qualify) する。

* Stereotype は Class と同じ記法を用いる。
  ただし名前の前または上にキーワード ``«stereotype»`` をつける。

  * モデル要素が図式的に表示されているとき、
    カッコ対が要素の右上に現れる。

  * 複数の Stereotypes が適用されているならば、
    それらの名前をカッコ内に CSV として示す。

  * 拡張モデル要素がキーワードを持つときは、
    ステレオタイプ名はそのキーワードの近くに表示されるだろう。
    一つのカッコに名前をまとめてもよいし、別々のカッコを用いてもよい。

* Stereotype の ``name`` はクラスの命名規約に従い大文字で始めるのが普通。
  しかし Profiles は異なる規約を用いてよい。

* ツールは Stereotypes を表示するのかしないのかを選ぶことができる。

* モデル要素に適用された Stereotype またはその一般化の
  ``ownedAttributes`` の値は次の三者の方法のうちのひとつでわかる。

  #. モデル要素を表す図表ノードに接続された註釈記号の部分として
  #. モデル要素を表す図表ノードの分かれた区画で
  #. 図表ノードで ``name`` 文字列の上または名前文字列の前に

* 区画または註釈記号が使われていると、
  ステレオタイプの名前を区画や註釈に含まれているのみならず、
  ``name`` 文字列の前に guillemets で示してよい。

* Stereotype Property が多価値ならば、<valuestring> は CSV として表示する。

* Stereotype Property の値を表示するのに区画が使われていれば、
  適用された Stereotype それぞれに対して
  その Property の値が表示されることになる追加区画が必要となる。

* 註釈記号の場合、
  またはもしモデル要素の ``name`` の前か上に表示されるならば、
  特定の Stereotype からの Property の値は
  適用された Stereotype の名前が guillemets の対に括られた状態で
  任意で先に来る。

* 区画または註釈記号で表示されているときは、
  名前文字列と値文字列の高々一対が単一行に現れることができる。

12.3.4.1 Icon presentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Stereotype に Images を添えることが、
  その Stereotype が適用されたモデル要素の記法の
  代わりに、またはさらなる普通の記法として可能である。

* Stereotype に ``icon`` に対する値があると、
  参照された Image を
  Stereotype が適用されたモデル要素に対して図式的に添えることができる。

* 図表的表現を持つすべてのモデル要素がアイコンを付けることが可能。
  モデル要素が

  * 箱として図表的に表現されると、
    箱が Image に取って代わられ、モデル要素の ``name`` が Image の下に現れる。
    この表現の選択は、
    モデル要素に単一の Stereotype が適用されており、
    モデル要素の Properties がない場合だけ可能である。

    また別の選択として、Image の縮小版をモデル要素を表現する箱の
    内側上部に表示してもよい。
    複数の Stereotypes が適用されているときは、
    複数の Images を箱で表示してよい。

  * 線として図表的に表現されると、
    Image を線の近くに置いてよい。

  * テキスト記法として図表的に表現されると、
    Image をテキスト表記の左に表示してよい。

* Images のいくつかは Stereotype の ``icon`` Property によって
  参照されてよい。

* モデル要素には既定の表現をするための ``icon`` をすでに使うものもある。
  この典型的な例には Actor モデル要素があり、
  これは「棒人間」のアイコンを用いる。

12.3.5 Examples
----------------------------------------------------------------------
* Figure 12.19 Example of Using an Extension

  * ここで Home はメタクラス Interface を拡張するステレオタイプである。
  * ステレオタイプ Home のオブジェクトは
    クラス Interface のオブジェクトに追加することと
    オブジェクトから除去することが意のままにできる。

* Figure 12.20 Example of a Required Extension

  * Profile が適用されるモデルにあるメタクラス Component の
    オブジェクトはそれぞれが、
    Extension の ``isRequired`` が true であるので、
    ステレオタイプ Bean のオブジェクトに適用するはずである。

  * ``{required}`` が付いているので、
    その Profile が適用されている Component の各オブジェクトは、
    ステレオタイプ Bean のオブジェクトを適用するはずである。

  * モデルはそのような Stereotype が適用されなければ
    well-formed でない。

* Figure 12.21 Defining a Simple EJB Profile

  * ある EJB Profile の簡単な見本。
  * Bean がメタクラス Component に適用されていることを必要とする。
    Bean は抽象的なので、具象サブクラスである Entity か Session の
    どちらかのオブジェクトが Component の各オブジェクトに
    リンクされていなければならない。

* Figure 12.22 Importing a Package from a Profile

  * Types と Factory は素の Package である一方、
    Manufacturer は Profile である。

  * Manufacturer は Types をインポートしているので、
    Device という Stereotype の Properties の ``type`` として
    Color と JavaInteger が用いられる。

  * Profile Manufacturer があとで Package に適用されるならば、
    Types 由来の型は Profile が適用される Package では
    （明示的にパッケージ Types をインポートしない限りは）利用できない。
    この例では Factory が Types を別個にインポートしているのでその限りである。

* Figure 12.23 Profiles Applied to a Package

  * プロファイル Java および EJB が与えられると、
    Package WebShopping にどのようにそれらが適用されればよいのかを示す。

* Figure 12.24 Defining a Stereotype

  * 簡単なステレオタイプ Clock が、
    自在にメタクラス Class のオブジェクトに対して
    （動的に）適用可能であるように定義されている。

* Figure 12.25 Presentation Options for an Extended Class

  * 上記 Clock の数通りの表現例。
  * 本文中にはこの見本のための言及がない。

* Figure 12.26 An Instance Diagram when Defining a Stereotype

  * かなり込み入ったオブジェクト図。
    先ほどの Clock の定義を表現している諸オブジェクトを示している。

  * Clock から左側の理解が重要。

* Figure 12.27 Defining Multiple Stereotypes on Multiple Stereotypes

  * Clock が Component と Class の両方を拡張することを示す。
  * それとは別に Creator という、
    Class を拡張する Stereotype を定義している。

* Figure 12.28 Using a Stereotype

  * クラス StopWatch に Clock を適用した。
    単に ``«Clock»`` をクラス名の上に付記するだけで示せる。

* Figure 12.29 Showing Values of Stereotypes and a Simple Instance Specification

  * 上記の適用の意味するところを表現する図式。

* Figure 12.30 Using Stereotypes and Showing Values

  * StopWatch に Clock と Creator を同時に適用する。
  * ここでは各 Stereotype の Property 値を註釈記法で示してある。

* Figure 12.31 Other Notational Forms for Depicting Stereotype Values

  * Stereotype の Property 値を記述する代わりの記法の例。
  * 属性区画に ``«Clock»`` と断ってから値を列挙。
  * 中括弧記法があるようだ。

* Figure 12.32 Example of a Profile defining Classes and (...)

  * クラス、二項合成（および非合成）関連を定義する、
    とある Profile の見本。

  * Profile IssuesProfile が Profile uml をインポートしていることを
    わざわざ図式内の上部にて断っている。

  * 本文ではこの図に相当する XMI コード全体を掲載している。

* Figure 12.33 Diagram example of applying a profile defining Classes and Associations and  (...)

  * 上記 IssuesProfile の適用例。
  * Profile IssueExample は IssuesProfile を適用している。
  * 重要なのは矢印のラベルに現れる ``«IssueTag»`` の意味だ。

  * 本文ではこの図のオブジェクト部分を表現する XMI コードと、
    リンク部分を表現する XMI コードを分けて掲載している。

12.4 Classifier Descriptions
======================================================================
機械生成による節。

12.5 Association Descriptions
======================================================================
機械生成による節。

.. include:: /_include/uml-refs.txt
