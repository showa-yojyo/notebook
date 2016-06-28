======================================================================
12 Packages
======================================================================
UML 2.5 pp. 239-282 に関するノート。

.. todo:: 最低でもあと一回は編集する。

.. contents:: ノート目次
   :depth: 2

12.1 Summary
======================================================================
* Packages は UML の主な包括的な構造化、組織化能力を提供する。
* UML に拡張を組織化する特殊化 Models と Profiles がある。

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

12.2.3 Semantics
----------------------------------------------------------------------
Package
  * TemplateableElement, Namespace, PackageableElement の一種である。

  * Package は他の Packages の内容物を、
    自分の包含要素の合併 (merging) を通じて拡張することが可能である。

  * Package は TemplateableElement なのでテンプレートとして定義して、
    他のテンプレートに束縛してもよい。

  * URI: Package を一意に特定する識別子を提供するように指定可能である。
    UML 内部では、プロファイルを除けば、URI の前もって決定された利用法というものはない。

PackageMerge
  * DirectedRelationship の一種である。
  * PackageMerge はふたつの Packages 間の有向関係である。
    一方の Package の中身が他方の Package に結合されるという関係である。

  * Package は直接的、間接的を問わず、自分自身を合併することは許されない。

  * Figure 12.2 Illustration of the Meaning of Package Merge

    * P2::A は P1::A の増分を定義する。

    * P3::SubA は P2::A のサブクラスの定義である。
      P3 から見ると、P2::A は P1 と P2 の間のマージ結果の A を表現していると解釈する。

    * P1: mergedPackage (target)
    * P2: receivingPackage (source, owner) であると同時に resultingPackage

      * マージの before/after で同じところにあるものの呼び方が変わる
        (receiving/resulting) ことがわかればとりあえず読める。

  * Figure 12.3 Conceptual View of the Package Merge Semantics

    * 図の右側は UML の図式ではない。
    * この B ダッシュを意識することがコツだと言っている。

 * PackageMerge の意味は制約と変換の集合で定義される。
   制約は妥当な PackageMerge の事前条件を指定し、
   一方、変換はその意味的な効果（事後条件のような）の特徴を描く。
   もし制約のいくつかが破られていれば、
   その PackageMerge は ill-formed であり、それを含むモデルは不正なものである。

   その「集合」が pp. 240-245 で文書化されている。
   もしマージの仕様を詳しく把握する状況になったら、ここを参照すること。

Model
  * Package の一種である。
  * Model というのはあるシステムの記述である。
    最も広義の意味でのシステムであり、ソフトウェアやハードウェアだけでなく、
    組織や工程をも意味する。

  * viewpoint: Model がシステムを記述する見地。
    異なる Models が同じシステムを定義することも可能である。
    大抵はこれらは相補的になっていて、
    それぞれはシステムの相異なる利害関係者の見地から定義されている。

  * Model は次のものの間の Abstraction Dependencies を持つことが可能。

    * refinement （標準プロファイル ``«Refine»`` でステレオタイプされる）
    * mapping （例えば標準プロファイル ``«Trace»`` でステレオタイプされる）

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
  * 関連端 receivingPackage 側の Package が合併前後で構成要素が増える方を指す。
  * A_ownedElement_owner と A_source_directedRelationship を subsets する。
  * 関連端 receivingPackage の多重度はちょうど 1 である。
  * cf. A_mergedPackage_packageMerge

A_mergedPackage_packageMerge
  * PackageMerge から Package への関連（単方向）。
  * 関連端 mergedPackage は合併前後でその構成内容物が変わらない方を指す。
  * A_target_directedRelationship を subsets する。
  * 関連端 mergedPackage の多重度はちょうど 1 である。
  * cf. A_packageMerge_receivingPackage

12.2.4 Notation
----------------------------------------------------------------------
* Package は大きい矩形の左上に小さい矩形（タブ）を付けた形状で示す。

  * Package の内容物は大きい矩形の内部に示してよい。
  * マルにプラスを付けた記号を使って、Package の外部から要素に線を引くような記法がある。

  * PackageImport や ElementImport を通じて持ち込んだ要素は、
    色を変えて描かれることがある。

  * Package の名前は内容物が大きい矩形内にあるかどうかで、場所が異なる。
    タブに記される場合と、大矩形内に記される場合がある。

  * 要素の可視性はいつものように要素名の前に ``+``, ``-`` 等の記号を付して示してもよい。

    * Packages の可視性が protected や package であることは許されない。

  * URI を ``{uri = <uri>}`` の形式でパッケージ名の後に示してよい。

* PackageMerge は開いた矢先を持つ破線矢印を用いて示す。

  * 矢印の向きは receivingPackage から mergedPackage である。
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
この節の概要は妙に長い。

* メタクラスを、それらを異なる目的に適合するように拡張することを許す能力について記述する。
* UML メタモデルを J2EE や .NET 等の異なるプラットフォームに仕立てる能力も含む。
* この節は OMG MOF_ に対して一貫性がある。

.. todo::

   MOF_ という OMG によるモデリング仕様が存在する。
   それを UML との関係性をかなりの紙幅を割いて記述している。
   私のノートではひとまず省略する。

* UML を拡張するのがよいかもしれない理由がいくつかある。

  * 特定のプラットフォームやドメインに適合される用語法 (a terminology) を与える。
  * 記法を持たぬ諸構成概念に構文を与える。
  * 既存の諸シンボルに異なる記法を与える。
  * UML や特定のメタクラス (pl.) にさらなる意味 (semantics) を追加する。
  * UML に存在しない型を追加する。
  * UML の諸構成概念で用いられるやり方に制限を加える Constraints を追加する。
  * あるモデルを別のモデルやコードに変換する際に用いることが可能な情報を追加する。
    例えばモデルと Java コードの間の対応規則の定義など。

* いつ新しいメタモデルやプロファイルを作成するかという問いに対する簡単な答えはない。

12.3.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 12.12 Profiles

  * 一見するとグラフの構造がいつもより込み入っている。
  * 新クラスは Profile, ProfileApplication, Stereotype, Image,
    Extension, ExtensionEnd と、いつもより多く登場する。

12.3.3 Semantics
----------------------------------------------------------------------
Profile
  * Package の一種である。
  * Profile は UML を拡張するのに用いることが可能なメタモデルの制限の付いた形式である。
    その主要な拡張構成要素は Stereotype である。

  .. todo:: ここも記述が多い。しかも固有名詞が多すぎる。

ProfileApplication
  * DirectedRelationship の一種である。
  * ProfileApplication は Package にどの Profiles が適用されているのかを記録するのに用いる。
  * Profile を適用するということは、

    * その Profile の部分として定義された Stereotypes を適用することが可能であることを意味する。
    * そのすべての入れ子とインポートした Profiles を再帰的に適用するということである。

  * Profile が適用されるときには、
    適当な Stereotypes のオブジェクト (pl.) が
    isRequired が true である ExtensionEnd と共に、
    メタクラスのオブジェクト (pl.) である Profile の要素 (pl.) のために
    生成されていなければならない。

  * 一度 Profile が Package に適用されると、適用された Profile を自由に取り除くことが許されている。

    * 適用 Profile の除去は、
      被参照メタモデル要素オブジェクト (pl.) に対しては何も構わないでそのまま残す。
      削除 Profile 要素オブジェクト (pl.) だけが除去対象。

  * 別の Profile の packagedElement である Profile を個々に適用することができる。
    しかし入れ子 Profile は、
    もしそれが Stereotypes を何であっても含んでおり、
    PackageImport をその他の Profiles が共に適用されることを示すのに使ってもよいならば、
    いくらでも必要とされるメタクラス・メタモデルの参照 (pl.) を指定する必要がある。

Stereotype
  * Class の一種である。
  * Stereotype は一つ以上のメタクラスのための拡張を定義する。
    そして、拡張メタクラスのための固有の用語や記法を上書きしたり追加したりすることを可能とする。

  * Stereotype がいくつかのメタクラスを拡張するならば、
    それは任意の時点においてその諸メタクラスのうちの一つだけのオブジェクトに適用される。

  * Stereotype は generatization/specialization というよりは、
    関連 (Extension) を通じてメタクラスを拡張してよい。
    同様に、メタクラスは Stereotypes により拡張されてよい。

  * 例えばその metamodelReference が UML ならば、
    States, Transitions, Activities, UseCases, Components, Properties, Dependencies,
    etc. はすべて Stereotypes によって拡張が可能である。

  * Stereotype は Class と同じように Properties を持ってよい。
    慣習的に Tag Definitions という呼び方をする。
    Stereotype がモデル要素に適用されているとき、
    Tag Definitions の値のことを慣習的に tag values という呼び方をする。

  * 異なる Profiles または Packages にある同じ名前の Stereotypes を見分けるために、
    Profiles/Packages が定義する名前空間を利用して、
    必要に応じて名前を限定 (qualify) してよい。

  * PackageImport と ElementImport は限定されていない (unqualified) 名前の使用を許すために用いられることが可能。

  * 適用された Profile が直接所有する Stereotypes (ownedStereotypes) は、
    限定されていない名前を用いることなしに用いられてよい。

Image
  * Element の一種である。
  * Image は図式中の画像を表示するのに必要な情報を提供する。

  * content: 画像の生データ？
  * format: content の形式を示す。値 ``SVG``, ``GIF``, ``PNG``, etc. が予約されている。
    加えて ``MINE:`` から始まる何らかの値も予約済みとする。

Extension
  * Association の一種である。
  * Extension はあるメタクラスの特性が Stereotype を通じて拡張されていることを示すために用いる。
  * また、ステレオタイプをクラスに柔軟に追加（そして後で削除）する能力を与える。

  * Extension の一方の関連端はふつうの Property であり、
    他方は ExtensionEnd である。
    前者は Extension と Class とを結び、
    後者は Extension とその Class を拡張する Stereotype とを結ぶ。

  * isRequired: Stereotype のオブジェクトが、
    それが含んでいる Profile が適用されているモデル内の拡張メタクラスの
    各オブジェクトにリンクされる必要があるかどうかを示す。

ExtensionEnd
  * Property の一種である。
  * メタクラスを拡張する際に Extension と Stereotype を結ぶのに用いられる。

A_metaclassReference_profile
  * Profile から PackageImport への composite 関連（単方向）。
  * TODO: 語るべきことが多すぎる。
  * A_packageImport_importingNamespace を subsets する。
  * cf. A_metamodelReference_profile

A_metamodelReference_profile
  * Profile から ElementImport への composite 関連（単方向）。
  * TODO: 語るべきことが多すぎる。
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
  * 関連端の多重度は metaclass が 1 に対して extension が ``*`` である。

A_type_extensionEnd
  * ExtensionEnd から Stereotype への関連（単方向）。
  * メタクラスを拡張する Stereotype を参照する。
  * A_type_typedElement を redefines/subsets する。

12.3.4 Notation
----------------------------------------------------------------------
* Extension の記法は矢印である。

  * 矢先は黒三角。
  * 向きは Stereotype から拡張 Class とする。
  * Association と同じ装飾をしてもよいが、通常は省略する。
    なお navigability の矢印は決して示さない。
  * isRequired == true ならば ExtensionEnd の近くに ``{required}`` と記す。

    * 多重度の明記とも関係している。

* Profile は Package と同じ記法を用いる。
  ただし名前の前または上にキーワード ``«profile»`` をつける。

* metaclassReference, metamodelReference は
  elementImport, packageImport とそれぞれ同じ記法プラスキーワード ``«reference»``。

* ProfileApplication は破線矢印で示す。

  * 矢先は開く。
  * 向きは Package から各 appiled Profile に向かう。
  * キーワード ``«apply»`` か、
    isStrict が true ならばキーワード ``«strict»`` を矢印のラベルとする。

* 複数の appliedProfiles が同名の Stereotypes を持つならば、
  必要に応じてその Stereotype の名前を限定 (qualify) する。

* Stereotype は Class と同じ記法を用いる。

  * ただし名前の前または上にキーワード ``«stereotype»`` をつける。
  * モデル要素がグラフィカルに表示されているとき、カッコ対が要素の右上に現れる。
  * 複数の Stereotypes が適用されているならば、
    それらの名前をカッコ内に CSV として示す。
  * 拡張モデル要素がキーワードを持つときは、
    ステレオタイプ名はそのキーワードの近くに表示されるだろう。
    一つのカッコに名前をまとめてもよいし、別々のカッコを用いてもよい。

* Stereotype の名前はクラスの命名規約に従い大文字で始めるのが普通。
  しかし Profiles は異なる規約を用いてよい。

* Stereotype に Images を添えることが、
  適用されたモデル要素の記法の代わりとしても、追加の記法としても可能。

  * Stereotype が icon 値を持つとき、参照 Image を被適用モデル要素に添えることが可能。
  * グラフィカルな表現を持つすべてのモデル要素がアイコンを付けることが可能。

    * 箱に対しては、箱自体がアイコンに取って代わられ、モデル名が Image の下に現れる。
      この表現選択は適用する Stereotype が一つだけであり、
      なおかつモデル要素の Properties が存在しない場合に可能。

      また別の選択として、Image の縮小版を箱の内側上部に表示してもよい。
      複数の Stereotypes が適用されているときは、複数の Images を箱の内部に表示してよい。

    * 線の場合、線の近くに Image を置いてよい。

    * テキスト記法の場合、テキストの左に Image を表示してよい。

  * Stereotype の icon は複数の Images を参照してよい（この日本語で伝わるか？）。

  * いくつかのモデル要素はすでにデフォルトの表現を用いている。
    例えば Actor は棒人間のアイコンを用いる。

12.3.5 Examples
----------------------------------------------------------------------
* Figure 12.19 Example of Using an Extension

  * Home は Interface を拡張するステレオタイプである。

* Figure 12.20 Example of a Required Extension

  * ``{required}`` が付いているので、
    その Profile が適用されている Component の各オブジェクトは、
    ステレオタイプ Bean のオブジェクトを適用していなければならない。

* Figure 12.21 Defining a Simple EJB Profile

  * ある EJB Profile の簡単な見本。
  * 先程と同様に Bean が Component に適用されていることを必要とする。
    Bean は抽象らしいので、具象サブクラスである Entity か Session の
    どちらかのオブジェクトが Component の各オブジェクトにリンクされていなければならない。

* Figure 12.22 Importing a Package from a Profile

  * Types と Factory は素の Package である一方、Manufacturer は Profile である。
  * Manufacturer は Types をインポートしているので、
    Device という Stereotype の属性の型 (type) として Color と JavaInteger が用いられる。

  * 仮にある Package が Manufacturer を適用するとき、
    Types 由来の型はその Package では（明示的に然るべきインポートをしない限りは）利用できない。
    この例では Factory が Types を別個にインポートしているのでその限りである。

* Figure 12.23 Profiles Applied to a Package

  * 与えられたプロファイル Java および EJB に対して、
    Package WebShopping にどのようにそれらが適用されるかを示す。

* Figure 12.24 Defining a Stereotype

  * 簡単なステレオタイプ Clock が、
    自在に（動的に）メタクラス Class のオブジェクトに対して
    適用可能であるように定義されている。

* Figure 12.25 Presentation Options for an Extended Class

  * 上記 Clock の数通りの表現例。
  * 本文中にはこの見本のための言及がない。

* Figure 12.26 An Instance Diagram when Defining a Stereotype

  * かなり込み入ったオブジェクト図。
    先ほどの Clock の定義を表現している諸オブジェクトを示している。

  * Clock から左側の理解が重要。

* Figure 12.27 Defining Multiple Stereotypes on Multiple Stereotypes

  * Clock が Component と Class の両方を拡張することを示す。
  * それとは別に Creator という、Class を拡張する Stereotype を定義している。

* Figure 12.28 Using a Stereotype

  * クラス StopWatch に Clock を適用した。
    単に ``«Clock»`` をクラス名の上に付記するだけで示せる。

* Figure 12.29 Showing Values of Stereotypes and a Simple Instance Specification

  * 上記の適用の意味するところを表現する図式。

* Figure 12.30 Using Stereotypes and Showing Values

  * StopWatch に Clock と Creator を同時に適用する。
  * ここでは各 Stereotype の Property 値をコメント記法で示してある。

* Figure 12.31 Other Notational Forms for Depicting Stereotype Values

  * Stereotype の Property 値を記述する代わりの記法の例。
  * 属性区画に ``«Clock»`` と断ってから値を列挙。
  * 中括弧記法があるようだ。

* Figure 12.32 Example of a Profile defining Classes and (...)

  * クラス、二項合成（および非合成）関連を定義する、とある Profile の見本。
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
