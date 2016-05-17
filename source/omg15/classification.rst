======================================================================
9 Classification
======================================================================
UML 2.5 pp. 97-164 に関するノート。

.. contents:: ノート目次

9.1 Summary
======================================================================
* Classification は組織化のための重要な技法である。
* Classification の具象サブクラスは様々な種類の値を分類するのに用いられる。
* Classification のオブジェクトをどのように生成するかを表現するのに
  InstanceSpecification というものが用いられるらしい。

9.2 Classifiers
======================================================================

9.2.1 Summary
----------------------------------------------------------------------
* Classifier はその Features に応じたオブジェクトの分類（項目）を表現する。
* Classifiers は Generalizations によって階層的構造に組織化されている。
* RedefinableElements は Generalization の階層を背景として再定義されてよい。

9.2.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 9.1 Classifiers

  * Classifier を中心とした図式だが、大量の関連が記されている。
  * 文字が潰れていて PDF ビューワーでズーム率を上げないと読めない。

9.2.3 Semantics
----------------------------------------------------------------------
*Classifier*
  * Namespace, Type, TemplateableElement, RedefinableElement から派生している。
  * Classifier によって分類される値は、その Classifier のインスタンスと呼ぶ。

    * 以降、私のノートでは英単語 instance を訳すときには一律オブジェクトとすることにしてる。

  * 属性 isAbstract が true のときは、その Classifier が抽象型であることを表す。
    すなわち厳密にその型と同じオブジェクトがないことを意味する。

  * 属性 isFinalSpecalization が true ならば、
    その Classifier が final である、すなわち何もこれを継承できないことを意味する。

Generalization
  * Classifiers 間の generalization/specialization を定義する DirectRelationship である。
  * 今更だが、ある Classifier のオブジェクトは、
    それの各 generalization のオブジェクトでもある。

  * 属性 isSubstitutable が true ならば、
    general な Classifier が使えるところすべてで specific な Classifier も使えることを意味する。

    * 仕様書では Circle と Ellipse の例を出して置換可能性について議論している。

*RedefinableElement*
  * NamedElement の一種なのだが、説明文の意味がわからない。

  * 属性 isLeaf が true ならば、その RedefinableElement が再定義を持ってはならないことを表す。

Substitution
  * 2 つの Classifiers の間に成り立つ Realization の一種。
    一方 (substitutingClassifier) が他方 (contract) の指定する契約に従うことを示す。

  * 動的な置換可能性を示唆する。
    サブクラスというよりインターフェイス寄りの概念。

A_inheritedMember_inheritingClassifier
  * Classifier から NamedElement への関連（単方向）。
  * 継承されたメンバーの集合のことをその inheritedMember と呼ぶ。
    特に断りのない限り、private な可視性を持たぬ member である。

  * 関連 A_member_memberNamespace を subsets する。
    * 関連端 inheritedMember は制約 ``{readOnly}`` がある。

A_redefinedElement_redefinableElement
  * RedefinableElement から RedefinableElement への関連（単方向）。
  * 両関連端とも ``{readOnly, union}`` であり、多重度は ``*`` である。

  A_redefinedClassifier_classifier
    * Classifier から Classifier への関連（単方向）。
    * 上記関連を subsets する。

A_redefinitionContext_redefinableElement
  * RedefinableElement から Classifier への単方向関連。
  * 関連端 redefinitionContext は「メンバーがそこから再定義されてもよいような Classifier」を表す。
  * 両関連端とも ``{readOnly, union}`` であり、多重度は ``*`` である。

    * とは言え、UML の仕様書では redefinitionContext が一つを超える事例はない。

A_feature_featuringClassifier
  * Classifier と Feature との間の関連（双方向）。
  * Classifier は Features の集合、
    そのうちのいくつかはその Classifier の attributes と呼ばれる Properties である。
    下記関連のコメント参照。

  * A_member_memberNamespace を subsets する。

    * 両関連端にはさらに ``{readOnly, union}`` も付く。

  A_attribute_classifier
    * Classifier から Property への関連（単方向）。
    * 上記の関連と A_redefinitionContext_redefinableElement を subsets する。

      * 両関連端にはさらに readOnly と union も付く。
      * 関連端 attribute のほうにはさらに ``{ordered}`` が加わっている。

A_collaborationUse_classifier
  * Classifier から CollaborationUse への composite 関連。
  * Classifier は、それを Collaborations に関係させる CollaborationUses を所有してもよい。
    その Collaborations はこの Classifier の外観を描写する。
    :doc:`./structured-classifiers` で述べる。
  * A_ownedElement_owner を subsets する。

  A_representation_classifier
    * Classifier から CollaborationUse への関連（単方向）。
    * 上記関連を subsets する。
    * 関連端 representation の多重度は ``0..1`` である。

A_ownedUseCase_classifier
  * Classifier から UseCase への composite 関連（単方向）。
  * Classifier は UseCases を所有してもよい。18 章で述べる。
  * A_ownedMember_namespace を subsets する。

A_generalization_specific
  * Generalization から Classifier への composite 関連（両方向）。
  * 各 Generalization は specific を general と関係させる。
  * 与えられた Classifier に対し、その specific の推移閉包
    （グラフ論等で頻用する用語）をその specializations と呼ぶ。
  * A_ownedElement_owner と A_source_directedRelationship を subsets する。

A_general_generalization
  * Generalization から Classifier への関連（単方向）。
  * 与えられた Classifier に対し、その general の推移閉包をその generalizations と呼ぶ。
    特に直接の generalizations はその親と呼ばれる。
    もっと言えば Classifier が Class のときには superClasses となる。
  * A_target_directedRelationship を subsets する。

A_general_classifier
  * Classifier から Classifier への関連（単方向）。
  * 説明が見当たらないが、子クラスは親クラスに依存する、くらいの意味か。

A_generalizationSet_generalization
  後述。

A_contract_substitution
  * Substitution から Classifier への関連（単方向）。
  * 意味は上述の Substitution のノートを参照。
  * 関連 A_supplier_supplierDependency を subsets する。

A_substitution_substitutingClassifier
  * Classifier から Substitution への composite 関連（両方向）。
  * 意味は上述の Substitution のノートを参照。

  * contract が実装する Interfaces は
    上記関連の substitutingClassifier もまた実装する必要があるか、
    あるいは substitutingClassifier がより特殊な Interface 型を実装する必要がある。

  * contract が所有するどんな Port も
    上記関連の substitutingClassifier が所有するある Port に match することが必要である。

  * 関連 A_clientDependency_client と A_ownedElement_owner を subsets する。

9.2.4 Notation
----------------------------------------------------------------------
*Classifier*
  * 本来は抽象クラスにつき記法はないが、便宜上デフォルトの記法を与えておく。
  * ダラダラと書いてあるが、基本的にはクラスの記法の説明。
    四角を描いて、区画に区切って、各 Features をそれぞれの記法で記す……。

    * 区画の分類等もここに仕様化されている。

  * 抽象 Classifier の名前 (name) は利用フォントが許す限りイタリック体で示す。
    あるいは名前の後か下に ``{abstract}`` と付記する。

Generalization
  * Classifiers 間を結ぶ矢印で記す。
  * スタイルは実線・白三角矢。向きは general 方向。
  * 同一の general を指す複数の Generalizations を表すのに、
    それらの矢印を分離しても共有してもよい。

RedefinableElement
  * 一般的な記法はない。サブクラスまで待て。

Substitution
  * Dependency の記法を用いる。キーワードは ``«substitute»`` とする。

* Classifier が継承した member は先頭にキャレット記号を付けて示してもよい。
  これは member が Property と Connector のときに使える。

  * inheritedMember に対しても同様の記法を用いて良い。

9.2.5 Examples
----------------------------------------------------------------------
いずれも矢印の向きとスタイルの規約を了解するだけで十分だ。

* Figure 9.2 Generalization notation showing different target styles

  * よくあるクラス継承図。個人的には shared target style の方が好みだ。

* Figure 9.3 Example of Substitution notation

  * Substitution の記法例。

9.3 Classifier Templates
======================================================================

9.3.1 Summary
----------------------------------------------------------------------
* Classifier は TemplateableElement でもある。その辺を見ていく。

9.3.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 9.4 Classifier Templates

  * 字が潰れて読みにくい。閲覧にはズームを 150% にはしたい。
  * この図では Classifier が間接的に ParameterableElement の一種であることがすぐに思い出せない。

9.3.3 Semantics
----------------------------------------------------------------------
RedefinableTemplateSignature
  * RedefinableElement かつ TemplateSignature の一種である。
  * RedefinableTemplateSignature を用いてパラメーター化された Classifier のことを
    template Classifier と呼ぶ。

    * 一方、一つまたはそれ以上の TemplateBindings を持つ Classifier のことを
      bound Classifier と呼ぶ。

  * 特殊化している template Classifier の状況で新しい仮引数 (TemplateParameters) を追加を許す。

ClassifierTemplateParameter
  * TemplateParameter の一種である。
  * その parameteredElement が Classifier である。

    * TemplateParameter は ParameterableElement を parameteredElement として持っている。
      一方、Classifier の親を Type から辿って行くと確かに ParameterableElement が祖先にいる。
      ゆえに、この redefines は成り立つ。

    * Classifier のすべてのサブクラスは引数化、束縛化してよい。
      とにかく TemplateParameters として用いてよい。
      同様に Behavior およびそのすべてのサブクラスもそのようにしてよい。

  * 属性 allowSubstitutable は関連端 constrainingClassifier の適合性の意味合いを制御する。
    後述。

A_ownedTemplateSignature_classifier
  * Classifier から RedefinableTemplateSignature への composite 関連（両方向）。
  * A_redefinitionContext_redefinableElement を subsets する。
  * さらに A_ownedTemplateSignature_template を redefines する。

A_extendedSignature_redefinableTemplateSignature
  * RedefinableTemplateSignature 間の関連（単方向）。
  * RedefinableTemplateSignature はテンプレートである親 Classifier 全ての
    RedefinableTemplateSignature を再定義する。
  * A_redefinedElement_redefinableElement を subsets する。

A_inheritedParameter_redefinableTemplateSignature
  * RedefinableTemplateSignature から TemplateParameter への関連（単方向）。
  * A_parameter_templateSignature を subsets する。
  * 関連端 inheritedMember は ``{readOnly}`` である。

A_parameteredElement_templateParameter
  * ClassifierTemplateParameter と Classifier との間の関連（両方向）。
  * 先述の ClassifierTemplateParameter のノート参照。

    * parameteredElement が存在して抽象でなければ、
      引数として用いられる Classifier は抽象であってはならない。

  * これは既存の同名の関連を redefines する。

A_constrainingClassifier_classifierTemplateParameter
  * ClassifierTemplateParameter から Classifier への関連（単方向）。
  * 関連端 constrainingClassifier は実引数として用いることが可能な引数を制約付ける
    Classifier の集合を指定する。

    * 集合 constrainingClassifier に何か Classifiers があれば、

      * その実引数はそれらのすべてと互換性が必ずある。
        ここで言う互換性とは：

        * allowSubstitutable が true ならば、
          互換性はその contract が constrainingClassifier の一つである
          Substitution をさらに許す。
  
        * allowSubstitutable が false ならば、
          互換性とはその集合のすべてと同じかそれらの特殊化であるという意味とする。

      * 先述の parameteredElement は次のように制限されていなければならない。

        * allowSubstitutable が true ならば、
          互換性はその contract が constrainingClassifier の一つである
          Substitution をさらに許す。

        * allowSubstitutable が false ならば、
          互換性とはその集合のすべてと同じかそれらの特殊化であり、
          さらなる機能はないものとする。

    * constrainingClassifier がない場合、引数になる Classifier に何も制約がない。

9.3.4 Notation
----------------------------------------------------------------------
これは :doc:`./common-structure` の Templates の記法の焼き直しのようだ。

ClassifierTemplateParameter
  * TemplateParameter の記法を、選択自由で制約を含めるように拡張する。
  * 錯覚かもしれないが p. 103 の BNF と p. 104 の例題とで
    ``<constraint>`` の prefix が異なる気がする。

9.3.5 Examples
----------------------------------------------------------------------
* Figure 9.5 Template Class and Bound Class

  * クラステンプレート FArray の図式か。
  * T, k がそれぞれ TemplateParameter である。
  * T は制約なしクラスの、k は LiteralInteger の TemplateParameter である。
  * k の方にはデフォルト値の指定が付いている。
  * AddressList は bound Class である。

* Figure 9.6 Anonymous Bound Class

  * 無名 bound Class の見本。C++ 風に書くと ``FArray<Point>`` を表現する図。

* Figure 9.7 Template Class with constrained Class parameter

  * クラステンプレート Car の図式。
  * CarEngine と n が TemplateParameter である。
  * CarEngine には制約が指定されている。
    読み方は「Engine と呼ばれる Class に適合する」である。
  * n は「LiteralInteger である」という制約が指定されている。

* Figure 9.8 Bound Class

  * これは bound Class の記法の見本。
  * bound Class の名前は DieselCar である。
  * TemplateParameter である CarEngine と n に対して
    DieselEngine と 2 をそれぞれ bind している。

9.4 Features
======================================================================

9.4.1 Summary
----------------------------------------------------------------------
* Feature は Classifier の構造的 (structural) 特徴と振る舞い的 (behavioral) な特徴を表現する。

9.4.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 9.9 Features

  * クラスの他に列挙体がある。

9.4.3 Semantics
----------------------------------------------------------------------
*Feature*
  * RedefinableElement の一種である。
  * Feature はそれに関連している Classifier (featuringClassifier)
    の構造的または振る舞い的特徴を表現する。

  * 属性 isStatic はその特徴が Classifier 自身に関係するのか、
    Classifier の各オブジェクトに関係するのかを示す。

*StructuralFeature*
  * Feature かつ TypedElement かつ MultiplicityElement の一種である。
  * StructuralFeature は Classifier のオブジェクトの構造を指定する。
  * UML では Property は StructuralFeature の唯一の種類であるので、
    ある Classifier の全ての StructuralFeatures は Properties (attributes) である。
  * 属性 isReadOnly は、初期化時に割り当てられた値が更新されてはならないか否かを示す。

*BehavioralFeature*
  * Feature かつ BehavioralFeature の一種である。
  * BehavioralFeature は「呼び出されることで、何かの応答を実行に移すようなもの」である。
  * 属性 concurrency は同一オブジェクトに対する concurrent 呼び出しの意味を指定する。
    型は CallConcurrencyKind という列挙体で、次の 3 通りの値をとる。

    * sequential: 並行性を管理する仕組みが BehavioralFeature に関連しない。

    * guarderd: 同時に複数の BehavioralFeatures を起動しようとすると、
      そのうちの一つだけが開始してよい。
      残りは現在実行中のものが完了するまでブロックされる。

    * concurrent: 同時に複数の BehavioralFeatures を並行に実行してもよい。

  * 属性 isAbstract は BehavioralFeature がそれを実装するような methods を持たないことを示す。

Parameter
  * ConnectableElement かつ MultiplicityElement の一種である。
  * Parameter はある BehavioralFeature の呼び出しに情報を引き渡すために用いられる引数の詳細を示すものである。

    * ConnectableElement はまだ説明がないが、特化された TypedElement である。

  * Parameter に name がない場合、引数リストの位置で識別される。

  * 属性 default: 後述の defaultValue と同様のはず。
  * 属性 direction はその引数の入出力種別を示す。
    型は ParameterDirectionKind という列挙体で、次の 4 通りの値をとる。

    * in
    * inout
    * out
    * return: 一つの BehavioralFeature に対して一つ以下だけあってよい。

  * 属性 effect は Parameter に渡したオブジェクトに何が起こるのかを表すのに用いられる。
    型は ParameterEffectKind という列挙体で、次の 4 つの値を取り得る。

    * create: out, inut, return な Parameter 限定。
    * read
    * update
    * delete: in または input な Parameter 限定。

  * 属性 isException: これはよくわからない。
  * 属性 isStream: :doc:`./common-behavior` で述べる。

ParameterSet
  * この図からは読み取れないが、NamedElement の一種である。
  * 説明文が that だらけで読みにくい。
  * ParameterSet にある Parameters はすべてが入力であるか、
    すべてが出力であるかでなけれならない。
  * 詳しくは 16 章で仕様化する。

A_feature_featuringClassifier
  先述の通り。

A_raisedException_behavioralFeature
  * BehavioralFeature から Type への関連（単方向）。
  * BehavioralFeature はその呼出期間中に例外を送出してもよい。
    この関連はその例外の型を指定する。

A_method_specification
  * BehavioralFeature と Behavior の間の関連（両方向）。
  * 多重度は specification ``0..1`` に対して method ``*`` である。
  * BehavioralFeature の振る舞いの応答を定義する一つの方法は、
    それを実装するような Behavior を一つまたは複数指定することである。
    この関連はその指定を示す。

A_ownedParameter_ownerFormalParam
  * BehavioralFeature から Parameter への composite 関連（単方向）。
  * 関連端 ownedParameter はその BehavioralFeature が呼び出されるときに与えられる
    引数の順序、型、入出力方向の特徴を述べるものである。

    * それゆえ ownedParameter は ``{ordered}`` である。

  * A_ownedMember_namespace を subsets する。

A_ownedParameterSet_behavioralFeature
  * BehavioralFeature から ParameterSet への composite 関連（単方向）。
  * 上述関連の代替？
  * A_ownedMember_namespace を subsets する。

A_defaultValue_owningParameter
  * Parameter から ValueSpecification への composite 関連（単方向）。
  * defaultValue が指定されていれば、
    その BehavioralFeature の呼び出し時に実引数が与えらていない場合に限り、
    この Parameter として評価されて用いられる。
  * A_ownedElement_owner を subsets する。
  * 多重度は両端ともに ``0..1`` である。

A_parameterSet_parameter
  * Parameter と ParameterSet の間の関連（両方向）。
  * 多重度は parameter ``1..*`` に対して parameterSet ``*`` である。

A_condition_parameterSet
  * ParameterSet から Constraint への composite 関連（単方向）。
  * 関連端 condition の意味は、
    入力 ParameterSet のそれが Operation における preconditions と、
    出力 ParameterSet のそれが Operation における postconditions とそれぞれ同じである。
  * A_ownedElement_owner を subsets する。

9.4.4 Notation
----------------------------------------------------------------------
*Feature*
  * static なものには下線を付ける。
  * 再定義したものには ``{redefines <x>}`` のように記す。

*StructuralFeature*
  * const なものには ``{readOnly}`` を用いて示す。

Parameter
  * 文字列で示す。その仕様は BNF で与えられている (p. 108)。
  * 目を引くのは <perm-propery> だ。付加的な情報を示すのに用いる。
    値は ordered, unordered, unique, nonunique, seq の文字列から任意個選べる。

ParameterSet
  * 16 章まで待て。

9.5 Properties
======================================================================

9.5.1 Summary
----------------------------------------------------------------------
* Property は次のものを表現する StructuralFeature である。

  * Classifier::attributes
  * Association::memberEnds
  * StructuralFeature::parts

9.5.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 9.10 Properties

  * Property を中心とした図式である。

9.5.3 Semantics
----------------------------------------------------------------------
Property
  * Property は Classifier::attribute または Association::memberEnd を表現して構わない。

    * モデリングの際には型が Class の Property を関連端に、
      型が DataType の Property を属性用区画に記すのが便利な慣習だ。

  * ConnectableElement かつ StructuralFeature かつ DeploymentTarget である。

  * 属性 aggregation は AggregationKind 型の値を取る。候補値は次のとおり。

    * none: Property は集約の意味を持たない。
    * shared: Property の集約の意味は「共有」である。
      共有集約の正確な意味はモデラーなどによって変化する。
    * composite: Property が複合的に集約されている。
      これは集約の強い形であり、全体・部分の関係を表現していると解釈する。

  * 属性 isDerived が true ならば、Property は派生したものであり、
    その値は他の情報から計算されてもよい。

  * 属性 isComposite が true ならば、
    この Property を含むオブジェクトがそのオブジェクトまたは
    Property が含む値のための container である。

  * 属性 isDerivedUnion:

    * <This means that
      the collection of values denoted by the Property in some context
      is derived by being the strict union of all of the values denoted,
      in the same context,
      by Properties defined to subset it>(pp. 110-111)

    * <Specifies whether the property is derived as the union of
      all of the Properties that are constrained to subset it>(p. 147)

    * ある Property が、
      そのすべての ``{subsets}`` である Properties の和集合と一致するとき、
      その Property は derived union であると呼ぶのだろう。

    * ``{union}`` という表記はその性質を示している。

  * 属性 isID は Property が Classifiers の識別子となる member であることを示せる。
    データベースの主キーや、XML の ID 属性のような役割を果たせる。

    * データベースの類比からすると isID = true な Property が複数あっても構わない。

A_ownedAttribute_interface, A_ownedAttribute_datatype, A_ownedAttribute_class
  * それぞれ Interface, DataType, Class から Property への composite 関連（両方向）。
  * 関連端 ownedAttribute は Classifier の attribute であるということを表している。
  * A_attribute_classifier と A_ownedMember_namespace を subsets する。
    さらに Class 版関連だけはまだ説明されていない関連を subsets または redefines する。

A_memberEnd_association
  * Association と Property 間の関連（両方向）。
  * 関連端 memberEnd は Association の一方の関連端であることを表す。

    * 二項関連においては、Property は同時に ownedAttribute と memberEnd であってもよい。
      どちらか一方の場合、生成されたときに Property は
      関連の位数に従った個数の Classifier のオブジェクトに関連したある値・値の集まりを表現する。
      この Classifiers の集まりをその Property の context を呼ぶ。

      * 何を書いているのかわからない。

  * A_member_memberNamespace を subsets する。

A_ownedEnd_owningAssociation
  これは :doc:`./structured-classifiers` で説明する。

A_qualifier_associationEnd
  * Property から Property への composite 関連（両方向）。
  * 上述の関連端 memberEnd な Property はそれ自身が
    qualifiers として働くような他の Properties を持ってもよい。
  * 関連端 qualifier は ``{ordered}`` である。
  * A_ownedElement_owner を subsets する。

A_defaultValue_owningProperty
  * Propery から ValueSpecification への composite 関連（単方向）。
  * defaultValue が指定されていれば、Property のオブジェクトが生成時に、
    これに対する設定がなければ評価されて、初期値となる。
  * 関連 A_ownedElement_owner を subsets する。
  * 多重度は両端ともに ``0..1`` である。

A_opposite_property
  * Property から Property への関連（単方向）。
  * 説明なし。
  * 多重度は両端ともに ``0..1`` である。

A_subsettedProperty_property
  * Property から Property への関連（単方向）。
  * これは Property が集約であるときに、
    subsetttedProperty が property から重複構成要素を除外した集合であることを表す。

A_redefinedProperty_property
  * Property から Property への関連（単方向）。
  * 説明なし。
  * A_redefinedElement_redefinableElement を subsets する。
  * 多重度は両端ともに ``*`` である。

9.5.4 Notation
----------------------------------------------------------------------
Property の一般的な記法が BNF 記法で仕様化されている。

* PDF のこのページにブックマークを入れておきたい。
* 個人的には prop-modifier がいつも気になっている。
* 集約の記法は :doc:`./structured-classifiers` まで先延ばし。

9.5.5 Examples
----------------------------------------------------------------------
* Figure 9.11 Examples of attributes

  * スラッシュの使い方が複数ある？

* Figure 9.12 Association-like notation for attributes

  * 関連の記法では属性がどう示されるのかを示す。

9.6 Operations
======================================================================

9.6.1 Summary
----------------------------------------------------------------------
* Operation は次のものが所有してもよい BehavioralFeature である。

  * Interface
  * DataType
  * Class

* Operation をテンプレート化してもよいし、
  テンプレート引数として用いてもよい。

9.6.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 9.13 Operations

  * Operation を中心とした図式。
  * 左側は Property の図式とそっくり。

9.6.3 Semantics
----------------------------------------------------------------------
Operation
  * Operation は Interface, DataType, Class のどれかの BehavioralFeature である。
    なおかつ BehavioralFeature と ParameterableElement である。

  * 属性 isOrdered は Operation が戻り値を持つならば、その isOrdered と同じ。

  * 属性 isQuery が true ならば、
    その Operation の呼び出しはそのオブジェクトまたはモデル内のどの要素の状態を修正してはならない。

    * C++ で言うところの const メンバー関数のような概念だろう。
      それより条件が強いように見える。

  * 属性 isUnique は Operation が戻り値を持つならば、その isUnique と同じ。
  * 属性 lower, upper: Operation が戻り値を持つならば、そのそれぞれと同じ。

OperationTemplateParameter
  * パラメーター化要素が Operation である TemplateParameter である。

A_ownedOperation_interface, A_ownedOperation_datatype, A_ownedOperation_class
  * Interface, DataType, Class いずれかから Operation への composite 関連（双方向）。
  * 各 Classifier が Operation(s) を所有してもよいという意味。
  * ownedOperation は ``{ordered}`` である。
  * A_feature_featuringClassifier を subsets する。
  * A_redefinitionContext_redefinableElement を subsets する。
  * A_ownedMember_namespace を subsets する。

A_ownedParameter_operation
  * Operation から Parameter への composite 関連（双方向）。
  * Parameter は Operation の構成要素の一つである。
  * A_ownedParameter_ownerFormalParam を subsets する。

    * ownedParameter の方は ``{ordered, redefines ownedParameter}`` となっている。

A_precondition_preContext, A_postcondition_postContext, A_bodyCondition_bodyContext
  * Operation から Constraint への composite 関連（単方向）。
  * precondition と postcondition は Operation の呼び出しに関する事前条件と事後条件をそれぞれ意味する。
  * bodyCondition は Operation の戻す結果をその仕様が計算する値によって縛りをかける。
  * A_ownedRule_context を subsets する。

A_raisedException_operation
  * Operation から Type への関連（単方向）。
  * Operation はその呼出期間中に例外を送出してもよい。
    そういう場合は上述の postcondition や bodyCondition は成立していると仮定するべきではない。

  * A_raisedException_behavioralFeature を subsets する。

    * 図では operation が ``{subsets}`` で
      raisedException が ``{redefines}`` になっている？

A_redefinedOperation_operation
  * Operation から Operation への関連（単方向）。
  * Operation を継承クラスで再定義することを示す関連だろうか。
  * A_redefinedElement_redefinableElement を subsets する。

A_parameteredElement_templateParameter
  * OperationTemplateParameter と Operation の間の関連（双方向）。
  * 同名関連の redefines である。

9.6.4 Notation
----------------------------------------------------------------------
* Operation のテキストによる表現形式を BNF 記法で仕様化している。
  ザッと見た感じでは Parameter の記法に準じているように見受けられる。

* 次に template Operation の TemplateParameter の記法を仕様化している。
  Operation の名前と Parameters の間に山括弧でリストするというものだ。

* さらに OperationTemplateParameter の記法を仕様化している。
  これは TemplateParameter の記法を拡張することでなされる。

9.6.5 Examples
----------------------------------------------------------------------
テンプレートが絡む記法は山括弧がダブって読みにくくなる。
まるで C++ のコード。

9.7 Generalization Sets
======================================================================

9.7.1 Summary
----------------------------------------------------------------------
* GeneralizationSet は Generalizations を直交にグループ分けする手段を提供する。
* この節で紹介する分類技法は面白い。

9.7.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 9.14 Generalization Sets

  * Figure 9.1 の一部を詳細にしたもの。

9.7.3 Semantics
----------------------------------------------------------------------
困ったことに Examples を先に見たほうが理解しやすい。

GeneralizationSet
  * PackageableElement から派生。
  * 属性 isCovering: Generalizations の特定する Classifiers が完全であるかどうかを示す。
    つまり、Classifier の任意の派生型オブジェクトは、
    ここにある Classifiers の少なくとも一つのもののそれであることが常に成り立つ。

  * 属性 isDisjoint: Generalizations の特定する Classifiers が部分的に重なりを持たないことを示す。
    つまり、Classifier の派生型をここから一つ取った時、
    それはそれ以外のどの型でもないと言っている。

A_generalizationSet_generalization
  * Generalization と GeneralizationSet の間の関連（両方向）。
  * Generalization がどの GeneralizationSet に所属するのかを示す。
  * 両関連端は多重度 ``*`` である。

A_powertypeExtent_powertype
  * Classifier と GeneralizationSet との間の関連（両方向）。
  * この関連が意味するのは、
    GeneralizationSet の各 Generalization に対して、
    特殊化 Classifier が powertype のオブジェクトに一意に関連している、
    ということだ。

    * すなわち powertype オブジェクトと対応する Classifiers が意味的に等価であると扱われる。

9.7.4 Notation
----------------------------------------------------------------------
* Figure 9.15 GeneralizationSets designated by name

  * Generalization の名前をいつもの矢印のラベルに記している。

* Figure 9.16 GeneralizationSets designated by shared target

  * 以前にも見た shared target style による記法。

* Figure 9.17 GeneralizationSet designated by dashed line spanning Generalization arrows

  * 破線を矢印群に交差させることで GeneralizationSet を示す。
  * ラベルを省略しても GeneralizationSet の存在を示唆できるというささやかな利点がある。

* Table 9.1 GeneralizationSet constraints

  * isCovering と isDisjoint の記法は制約の記法に準じる。

* Figure 9.18 GeneralizationSet constraint notation with shared target style
* Figure 9.19 GeneralizationSet constraint notation with dashed line style

  * 制約はラベル内に記す。

* Figure 9.20 Power type notation with shared target style
* Figure 9.21 Power type notation with dashed line style

  * powertype の記法は GeneralizationSet のそれに準じる。
    名前の前にコロンを付す。

9.7.5 Examples
----------------------------------------------------------------------
ここの見本が分かりやすいので、GeneralizationSet の概念を誤解しにくくなっている。

* Figure 9.22 GeneralizationSet notation options

  * 抽象型 Person を異なる基準で specialize していることがよくわかる。

* Figure 9.23 GeneralizationSets and constraints

  * 男か女かにしか分類できないし、これらは互いに排他的な概念なので、
    ラベルに ``{complete, disjoint}`` と記してよい。

* Figure 9.24 Power type example

  * powertype TreeSpecies による Tree の派生モデル。

* Figure 9.25 More power type examples

  * powertype いろいろ。

* Figure 9.26 More than one powertype

  * powertype が複数存在する場合は、ラベルを明確に記すことが重要だ。

9.8 Instances
======================================================================

9.8.1 Summary
----------------------------------------------------------------------
* InstanceSpecification は Classifier のオブジェクトを表現する。

9.8.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 9.27 Instances

  * InstanceSpecification, Slot, InstanceValue をやる。

9.8.3 Semantics
----------------------------------------------------------------------
InstanceSpecification
  * DeploymentTarget, PackageableElement, DeployedArtifact の一種である。
  * モデル化されたシステム内のオブジェクトの在り様を表現する。

  * InstanceSpecification は次のものを表現してよい。

    * 一つ以上の Classifiers によるオブジェクトの分類。いずれかは抽象でもよい。
    * それの classifiers に基づくオブジェクトの種類。
    * そのオブジェクトの StructuralFeatures の値の仕様。それらは Slots に収まる。
    * ValueSpecification による、
      オブジェクトの計算方法、継承方法、構築方法の選択自由の仕様。

  * InstanceSpecification はあるオブジェクトのスナップショットである。
  * InstanceSpecification はあるオブジェクトの性質を部分的にだけ決定するのかもしれないので、
    実際にはその InstanceSpecification の要件を満足するオブジェクトが複数あり得る。

Slot
  * Element の一種である。
  * ある InstanceSpecification がモデル化したオブジェクトが、
    特定の StructuralFeature に対して値を持つということを指定する Element である。

  * Slot の値はその Slot の定義 StructuralFeature に適合する (conform) 必要がある。
  * Slot の値は ValueSpecifications を用いて指定される。

InstanceValue
  * ValueSpecification の一種である。
  * その値が InstanceSpecification を用いて指定される。

A_slot_owningInstance
  * InstanceSpecification から Slot への composite 関連。

A_classifier_instanceSpecification
  * InstanceSpecification から Classifier への関連（単方向）。
  * InstanceSpecification のオブジェクトの種類として参照する。
  * 例えば classifier が

    * Class ならばその Class のオブジェクトの特徴を述べ、
    * Association ならばその Association のリンクの特徴を述べ、
    * 空ならば表現されているオブジェクトの種類を強制しない。

A_definingFeature_slot
  * Slot から StructuralFeature への関連（単方向）。

A_value_owningSlot
  * Slot から ValueSpecification への composite 関連（単方向）。
  * 関連 A_ownedElement_owner を subsets する。
  * value は ``{ordered}`` である。
  * value は型、多重度、等々において前述の definingFeature と適合する必要がある。

A_specification_owningInstanceSpec
  * InstanceSpecification から ValueSpecification への composite 関連（単方向）。
  * もし specification があれば、InstanceSpecification の値を与えるために
    ValueSpecification が評価される。

  * もし InstanceSpecification の参照する classifiers が一つ以上ある場合、
    ValueSpecification の型は少なくとも classifiers の一つには適合する必要がある。

A_instance_instanceValue
  * InstanceValue から InstanceSpecification への関連（単方向）。
  * InstanceValue は参照する InstanceSpecification を所有しない。
    複数の InstanceValues が同じ InstanceSpecification を参照してもよい。

9.8.4 Notation
----------------------------------------------------------------------
InstanceSpecification
  * その classifiers と似た記法で表す。
    オブジェクト名があれば Classifier の名前の前にコロンで区切ってくっつける。
    そして下線を引く。

  * classifiers が Association のものはリンクを表現する。
    関連の記法と同じものを用いて示す。

Slot
  * 対応する StructuralFeature のそれに似た記法を用いて示す。
  * さらにイコール記号を書き、値の仕様が続く。

InstanceValue
  * テキストによる記法またはグラフィカルな記法を用いて出てくる。

その他、細かい条件の下での記法について説明があるが省略。

9.8.5 Examples
----------------------------------------------------------------------
* Figure 9.28 Specification of an Instance of String

  * String 型オブジェクト streetName の図式に見える。
  * これが InstanceSpecification の記法の一つの見本となる。
  * 識別子の下にある引用符で括られた文字列が値である。

* Figure 9.29 Slots with values

  * Slots 付き InstanceSpecification の記法例。

* Figure 9.30 InstanceSpecifications representing two objects connected by a link

  * リンク付き InstanceSpecifications の記法例。

* Figure 9.31 InstanceValue represented textually

  * InstanceValue の記法例。Slot から参照して欲しいようだ。

* Figure 9.32 InstanceValue represented graphically

  * 上記例題を関連の記法？で書き直した。

9.9 Classifier Descriptions
======================================================================
機械生成による節。

9.10 Association Descriptions
======================================================================
機械生成による節。

.. include:: /_include/uml-refs.txt
