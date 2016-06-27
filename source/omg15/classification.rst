======================================================================
9 Classification
======================================================================
UML 2.5 pp. 97-164 に関するノート。

.. contents:: ノート目次
   :depth: 2

9.1 Summary
======================================================================
* 分類は組織化をするのに重要な技法である。
  この章では分類に関する概念を指定する。
  核となる概念とは Classifier すなわち
  その具象サブクラスが値のさまざまな型を分類するのに用いられる
  抽象メタクラスである。

* この章にあるその他のメタクラスは Classifiers の構成要素、
  Classifiers が InstanceSpecifications を使ってオブジェクト化されるモデル、
  そしてこれらの概念すべての間にあるさまざまな関係を表現する。

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

A_inheritedMember_inheritingClassifier
  * Classifier から NamedElement への関連（単方向）。
  * 継承されたメンバーの集合のことをその ``inheritedMember`` と呼ぶ。
    特に断りのない限り、private な可視性を持たぬ ``member`` である。

  * 関連 A_member_memberNamespace を subsets する。

    * 関連端 ``inheritedMember`` は制約 ``{readOnly}`` がある。

A_redefinedElement_redefinableElement
  * RedefinableElement から RedefinableElement への関連（単方向）。
  * 両関連端とも ``{readOnly, union}`` であり、多重度は ``*`` である。

  A_redefinedClassifier_classifier
    * Classifier から Classifier への関連（単方向）。
    * 上記関連を subsets する。

A_redefinitionContext_redefinableElement
  * RedefinableElement から Classifier への単方向関連。
  * 関連端 ``redefinitionContext`` は「メンバーがそこから再定義されてもよいような Classifier」を表す。
  * 両関連端とも ``{readOnly, union}`` であり、多重度は ``*`` である。

    * とは言え、UML の仕様書では ``redefinitionContext`` が一つを超える事例はない。

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
      * 関連端 ``attribute`` のほうにはさらに ``{ordered}`` が加わっている。

A_collaborationUse_classifier
  * Classifier から CollaborationUse への composite 関連。
  * Classifier は、それを Collaborations に関係させる CollaborationUses を所有してもよい。
    その Collaborations はこの Classifier の外観を描写する。
    :doc:`./structured-classifiers` で述べる。
  * A_ownedElement_owner を subsets する。

  A_representation_classifier
    * Classifier から CollaborationUse への関連（単方向）。
    * 上記関連を subsets する。
    * 関連端 ``representation`` の多重度は ``0..1`` である。

A_ownedUseCase_classifier
  * Classifier から UseCase への composite 関連（単方向）。
  * Classifier は UseCases を所有してもよい。
    :doc:`./usecases` で述べる。
  * A_ownedMember_namespace を subsets する。

A_generalization_specific
  * Generalization から Classifier への composite 関連（両方向）。
  * 各 Generalization は ``specific`` を ``general`` と関係させる。
  * 与えられた Classifier に対し、その ``specific`` の推移閉包
    （グラフ論等で頻用する用語）をその specializations と呼ぶ。
  * A_ownedElement_owner と A_source_directedRelationship を subsets する。

A_general_generalization
  * Generalization から Classifier への関連（単方向）。
  * 与えられた Classifier に対し、
    その ``general`` の推移閉包をその ``generalizations`` と呼ぶ。
    特に直接の ``generalizations`` はその親と呼ばれる。
    もっと言えば Classifier が Class のときには ``superClasses`` となる。
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

  * ``contract`` が実装する Interfaces は
    上記関連の substitutingClassifier もまた実装する必要があるか、
    あるいは substitutingClassifier がより特殊な Interface 型を実装する必要がある。

  * ``contract`` が所有するどんな Port も
    上記関連の substitutingClassifier が所有するある Port に match することが必要である。

  * 関連 A_clientDependency_client と A_ownedElement_owner を subsets する。

9.2.3 Semantics
----------------------------------------------------------------------
9.2.3.1 Classifiers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Classifier は Features の集合を持ち、
  それらのいくつかは Classifier の ``attributes`` と呼ばれる Properties である。
  Features のそれぞれは Classifier の ``member`` である
  （:doc:`./common-structure` を参照）。

* Classifier によって分類される値をその Classifier のインスタンスと呼ぶ。

  * 以降、私のノートでは英単語 instance を訳すときは
    一律オブジェクトとする。

* Classifier を再定義することが許される（後述）。

* Classifier は、
  Classifier を Collaborations に結びつける CollaborationUses を所有してよい。
  Collaborations はこの Classifier の様子を記述する。
  :doc:`./structured-classifiers` 参照。

* Classifier は UseCases を所有してよい。
  :doc:`./usecases` 参照。

9.2.3.2 Generalization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Generalizations は
  Classifiers 間の generalization/specialization を定義する。
  Generalization それぞれは ``specific`` な Classifier を
  より ``general`` な Classifier に結びつける。

* Classifier のオブジェクトは、その一般化のそれぞれの（間接的な）オブジェクトでもある。

* Classifier が一般化されるときには、
  それの一般化のあるメンバーは継承される。
  つまり継承する Classifier 自身で定義されたかのように振る舞う。

* 継承されたメンバーの集合は ``inheritedMembers`` と呼ばれる。

* 型の適合とは、
  ある型が別のものに適合するならば、
  最初の型のオブジェクトのいずれも
  その ``type`` が二番目の型であると宣言されている
  TypedElement の値として用いられてよいことを意味する。

* Classifier の ``isAbstract`` 特性は、true のとき、
  Classifier が抽象、
  すなわち、直接オブジェクトがないことを指定する。
  言い換えると、抽象 Classifier のオブジェクトはどれもが
  その特殊化のひとつのオブジェクトであるものとする。

* ある Classifier が別のものを一般化するならば、
  可能な限りの状況のもとで、
  子のオブジェクトは親のオブジェクトに置き換えられる場合とは必ずしも限らない。

  * 例えば、Circle を Ellipse の特殊化として定義してよく、
    そのオブジェクトは Ellipse の特性にアクセスすることを伴う
    環境のすべてで置換可能となるかもしれない。
    だが、もし Ellipse がその長軸の長さしか変更しない振る舞いを定義しようものなら、
    Circle オブジェクトはそのような振る舞いを実装することはどうしても不可能だろう。

  * ``isSubstitutable`` 特性を、
    特殊な Classifier が一般の Classifier が用いられる環境すべてで
    用いられるかどうかを示すのに用いてよい。

9.2.3.3 Redefinition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* 特殊化する Classifier の一般化の ``member`` のどれでもが
  継承される代わりに再定義されることが許される。

* メンバーが再定義されてよい Classifier は ``redefinitionContext`` と呼ばれる。

* 再定義する要素は、
  それが再定義する RedefinableElement に対する整合性があるものとするが、
  ``general`` な状況での制約に矛盾しない、
  特殊化する ``redefinitionContext`` のオブジェクトに特有の
  固有の制約や他の詳細を追加してよい。

* 再定義する要素ひとつが RedefinableElements を複数再定義してよい。

* ``isLeaf`` 特性が true のとき、
  その RedefinableElement が再定義を何も持ってはならないものとすることを指定する。

* 再定義の詳細な意味は RedefinableElement の特殊化のそれぞれについて異なる。

* Classifier 自身は RedefinableElement である。
  Classifier が Class または Interface で入れ子になるときにこれが働いて、
  Classifier は ``redefinitionContext`` になる。

9.2.3.4 Substitution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Substitution とは、
  ``substitutingClassifier`` が ``contract`` Classifier に指定される
  契約に従うことを知らせる、
  ふたつの Classifiers の間の関係である。
  これは
  ``contact`` Classifier のオブジェクトが期待されるところでは
  ``substitutingClassifier`` のオブジェクトが実行時に
  置換可能であることを含意する。

9.2.4 Notation
----------------------------------------------------------------------
9.2.4.1 Classifiers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Classifier は抽象メタクラスである。
  それでもやはり、
  Classifier の具象サブクラスのどれにとっても
  利用可能な既定の表記法を一箇所で定義することは都合が良い。

* Classifier の既定の表記法は、
  Classifier の ``name`` を含む実線矩形であり、
  ``name`` の下部にある水平線により分離された区画がある。

* Classifier に対して既定の表記法を用いるならば、
  Classifier のメタクラスに対応するキーワードを
  ``name`` の上部に guillemets で括って示すものとする。

  * キーワードについては :doc:`./keywords` 参照。

* キーワード（ステレオタイプ名を含む）は Classifier ``name`` の上部に
  guillemets で括られ、プレーンな字面で中央寄せとするべきでもある。

* 抽象 Classifier の ``name`` は利用フォントが許す限りイタリック体で示す。
  あるいは ``name`` の後か下に ``{abstract}`` と示すことも認められる。

* Classifier 形状にある区画のいくらかは必須であり、
  具象構文適合を展示するツールにより支援されるものとする。

* どの区画も非表示にしてよい。

* attributes と名付けられた区画は
  その ``attribute`` 特性を介して到達される Properties を示す
  表記法を含む。この区画は必須かつ非表示でなければ常に他の区画の上部に現れる。

* operations と名付けられた区画は Operations を示す表記法を含む。
* receptions と名付けられた区画は Receptions を示す表記法を含む。

* Features を示す表記法を含む区画はどれもそれらの Features を
  public, private, protected の下にグループ分けされて示してよい。

* 準拠ツールは Features を示す表記法を含む区画の個々の Features を
  非表示にするオプションを与えることが許される。

* 準拠ツールは区画の命名を任意に支援してよい。

* Classifier が Classifiers である ``ownedMembers`` を持つならば、
  準拠ツールは所有される Classifiers とその間の関係を
  所有する Classifier の矩形の区画の別々の内部に入れ子にして図式的に
  示すためのオプションを提供してよい。

* Classifier が Constraints を所有するならば、準拠ツールは
  所有する Classifier の矩形の区画の別々の内部にリストされた
  所有される Constraints を示す区画を実装してよい。

9.2.4.2 Other elements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Generalization は関わり合う Classifiers を表現する記号の間を結ぶ
  白い矢先の矢印として示される。

* 同一の ``general`` Classifier を参照する複数の Generalizations を表すのに、
  それらの矢印を分離しても共有して示してもよい。

* RedefinableElement を表す一般的な表記法はない。

* Substitution は Dependency の記法を用いる。
  キーワードは ``«substitute»`` とする。

* Classifier が継承した ``members`` を
  仮に ``member`` が継承されていなかったら示されたであろうテキスト的表現に対して
  先頭にキャレット記号を付けることで
  Classifier の図式上に示してよい。

* 類似の表記法を Classifier の ``inheritedMembers`` である
  NamedElements のすべてに対して、
  それらが継承されたものであることを示すのに用いてよい。

* 継承された ``members`` を
  非継承 ``members`` と区別しやすくするように
  明るい色で示してもよい。

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
* Classifier は引数として扱えることを知らせる TemplateableElement の一種である。

9.3.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 9.4 Classifier Templates

  * 字が潰れて読みにくい。閲覧にはズームを 150% にはしたい。
  * この図では Classifier が間接的に ParameterableElement の一種であることがすぐに思い出せない。

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
  * 関連端 ``inheritedMember`` は ``{readOnly}`` である。

A_parameteredElement_templateParameter
  * ClassifierTemplateParameter と Classifier との間の関連（両方向）。
  * 先述の ClassifierTemplateParameter のノート参照。

    * ``parameteredElement`` が存在して抽象でなければ、
      引数として用いられる Classifier は抽象であってはならない。

  * これは既存の同名の関連を redefines する。

A_constrainingClassifier_classifierTemplateParameter
  * ClassifierTemplateParameter から Classifier への関連（単方向）。

9.3.3 Semantics
----------------------------------------------------------------------
9.3.3.1 Template and Bound Classifiers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* テンプレートと被束縛要素の用語の意味は :doc:`./common-structure` で定義されている。

* RedefinableTemplateSignature を使って引数化された Classifier は
  テンプレート Classifier と呼ばれる。
  一方、ひとつまたはそれ以上の TemplateBindings を持つ Classifier は
  被束縛 Classifier と呼ばれる。

* テンプレートの一般的な意味は :doc:`./common-structure` で定義されているとおりである。

* 拡張被束縛 Classifier のメンバーを束縛において実引数として用いてよい。

* 被束縛 Classifier は束縛の結果生じるものに加えて中身を持ってよい。

* テンプレート Classifier の引数は TemplateParameter のどんな種類の可能性もある。

* 引数が Classifier のときには、ClassifierTemplateParameter で表現され、
  意味と表記法はこの章で定義される。

* 引数が LiteralSpecification のときには、意味と表記法は
  :doc:`./common-structure` で定義されているとおりである。

* 引数が Operation であるときには、意味と表記法は 9.6 にあるとおりである。
* 引数が Property であるときには、意味と表記法は 9.5 にあるとおりである。

9.3.3.2 Template Classifier specialization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* RedefinableTemplateSignature は
  特殊化するテンプレート Classifier の状況で
  新たな仮 TemplateParameters の追加を許すために
  RedefinableElement と TemplateSignature の両方を特殊化する。

* RedefinableTemplateSignature はテンプレートである
  親 Classifiers のすべての RedefinableTemplateSignatures を再定義する。

9.3.3.3 Classifier Template Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ClassifierTemplateParameter とは、
  ``parameteredElement`` が 
  ParameterableElement の一種であるという能力で Classifier である
  TemplateParameter の一種である。

* Class, Collaboration, Component, DataType, Interface, Signal, UseCase などの
  Classifier のサブクラスはすべて引数として、
  束縛して、TemplateParameters として用いてもよい。
  同様のことが Class のサブクラスとしての Behavior に対しても成り立ち、
  それにより Activity, Interaction, StateMachine などの
  Behavior のサブクラスすべてもそのようにしてよい。

* ClassifierTemplateParameter の ``constrainingClassifier`` 特性は
  引数として用いることが可能な実引数を制約する
  Classifiers の集合を指定する。
  この集合に何か Classifiers があれば、
  実引数はそれらのすべてと互換性が次の意味であるものとする：

  * ``allowSubstitutable`` が true ならば、
    互換性は ``contract`` が ``constrainingClassifier`` である
    Substitution をさらに許す。
 
  * ``allowSubstitutable`` が false ならば、
    互換性とはその集合のすべてと同じであることか、
    ``constrainingClassifiers`` のすべての特殊化であることを意味する。

* なお、
  ``constrainingClassifiers`` があれば、
  ``parameteredElement`` は次のように制約が付くものとする：

  * ``allowSubstitutable`` が true ならば、
    互換性は ``contract`` が ``constrainingClassifier`` である
    Substitution をさらに許す。

  * ``allowSubstitutable`` が false ならば、
    互換性とはその集合のすべてと同じであることか、
    ``constrainingClassifiers`` のすべての直接的特殊化であることを意味し、
    さらなる機能はない。

* すべての場合で、
  ``parameteredElement`` が抽象的でなければ、
  実引数として用いられる Classifier は抽象的ではないものとする。

9.3.4 Notation
----------------------------------------------------------------------
これは :doc:`./common-structure` の Templates の記法の焼き直しのようだ。

* ClassifierTemplateParameter は 
  TemplateParameter が選択自由な型制約を含むように
  表記法を拡張する。

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
* Features は Classifiers の構造的特徴と振る舞いの特徴を表現する。

9.4.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 9.9 Features

  * クラスの他に列挙体がある。

A_feature_featuringClassifier
  先述の通り。

A_raisedException_behavioralFeature
  * BehavioralFeature から Type への関連（単方向）。
  * BehavioralFeature はその呼出期間中に例外を送出してもよい。
    この関連はその例外の型を指定する。

A_method_specification
  * BehavioralFeature と Behavior の間の関連（両方向）。
  * 多重度は ``specification`` ``0..1`` に対して ``method`` ``*`` である。
  * BehavioralFeature の振る舞いの応答を定義する一つの方法は、
    それを実装するような Behavior を一つまたは複数指定することである。
    この関連はその指定を示す。

A_ownedParameter_ownerFormalParam
  * BehavioralFeature から Parameter への composite 関連（単方向）。
  * 関連端 ``ownedParameter`` はその BehavioralFeature が呼び出されるときに与えられる
    引数の順序、型、入出力方向の特徴を述べるものである。

    * それゆえ ``ownedParameter`` は ``{ordered}`` である。

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
  * 多重度は ``parameter`` ``1..*`` に対して
    ``parameterSet`` ``*`` である。

A_condition_parameterSet
  * ParameterSet から Constraint への composite 関連（単方向）。
  * 関連端 condition の意味は、
    入力 ParameterSet のそれが Operation における ``preconditions`` と、
    出力 ParameterSet のそれが Operation における ``postconditions`` とそれぞれ同じである。
  * A_ownedElement_owner を subsets する。

9.4.3 Semantics
----------------------------------------------------------------------
9.4.3.1 Features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Feature それぞれは、
  それの ``featuringClassifier`` と呼ばれる Classifier と関連付けられている。
  Feature は
  ``qualifiers`` として振る舞う Properties を除いて、
  それの ``featuringClassifier`` を表す
  ある構造的または振る舞い的特徴を表現する。

* ``isStatic`` 特性はその特徴が Classifier 自身に関係する (true) のか、
  Classifier のオブジェクトそれぞれに関係するのかを指定する。

9.4.3.2 Structural Features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* StructuralFeature とは Classifier のオブジェクトの構造を指定する
  Classifier の型の付いた Feature である。

* Properties である Classifier の StructuralFeature は
  Classifier の ``attributes`` と呼ばれる。
  UML では Property は StructuralFeature の唯一の種類であるので、
  Classifier の StructuralFeatures の全部は Properties,
  したがって ``attributes`` である。

* Classifier のオブジェクトごとに
  直接または継承した非静的な Classifier の ``attribute`` に対する
  値または値の集まりがある。

  * ``attribute`` の多重度が ``0..1`` であれば、
    値がひとつもないか、
    Type が ``attribute`` の Type に適合する単一の値のどちらかがあるものとする。

  * ``attribute`` の多重度が ``1..1`` であれば、
    Type が ``attribute`` の Type に適合する単一の値があるものとする。

  * ``attribute`` の多重度が ``j..k`` であれば、
    Types のそれぞれが ``attribute`` の Type に適合する
    j 個以上 k 個以下の値の集まりがあるものとする。

  * ``attribute`` の多重度が ``0`` であれば、値がないものとする。

* StructuralFeature に ``isStatic`` が true であると印がついていると、
  上記の点はオブジェクトの個々に対してではなく、
  ある実行スコープの範囲内にある見分けられる個体とみなされる
  Classifier 自身に関係する。

* 意味論的に準拠しているツールで、
  継承した静的 StructuralFeature それぞれは二者択一の意味のうちひとつが
  あるものとする：

  #. 実行スコープ内では
     StructuralFeature の値または値の集まりは、
     継承する Classifier のどれに対しても、
     所有する Classifier の値または値の集まりといつも同じである。
     これらの意味は Java や C# での静的メンバーに対応する。

  #. 実行スコープ内では
     所有する Classifier とそれを継承する Classifier それぞれに、
     StructuralFeature は別々かつ独立した値または値の集まりを持つ。
     これらの意味は Ruby や Smalltalk でのクラスインスタンス変数に対応する。

* StructuralFeature に ``isReadOnly`` が true であると印がついているならば、
  いったんそれが初期値を割り当てられると、更新されてはならない。

9.4.3.3 Behavioral Features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* 非静的 BehavioralFeature は
  それの  ``featuringClassifier`` のオブジェクトが、
  固有の振る舞いの応答を実施することによって、
  BehavioralFeature の発動 (invocation) に反応することを指定する。

* ``ownedParameters`` のリストは、
  BehavioralFeature が発動されるときに与えられ得る、
  または発動が完了するときに出力されたり返されたりする
  引数の順序、型、方向を記述する。

* 方向が in または inout である ``ownedParameters`` は、
  引数は BehavioralFeature を発動するときに与えられる
  ものとすることを定義する。

* BehavioralFeature はその発動の間に例外を送出することが許される。

* BehavioralFeature の振る舞いの応答を定義する方法のひとつは、
  BehavioralFeature を実装する ``methods`` として、
  ひとつまたはそれ以上の Behaviors を指定することである。

  * ``isAbstract`` 特性が true のときには、
    BehavioralFeature はそれを実装する ``methods`` を
    何も持たないことを指定する。

* ``concurrency`` 特性は同一オブジェクトに対する 
  同時に起こる呼び出しの意味を指定する。
  その型とは CallConcurrencyKind という列挙体で、
  次のリテラル値をとる。

  * sequential: 並行性を管理する仕組みは
    ひとつも BehavioralFeature に関連しない。

  * guarderd: 時間的に重なり合う BehavioralFeature の複数発動が
    ひとつのオブジェクトに対して起こることが許されるが、
    ひとつしか開始することを許されない。
    残りは現在実行中の BehavioralFeature が完了するまでブロックされる。

  * concurrent: 時間的に重なり合う BehavioralFeature の複数発動が
    ひとつのオブジェクトに対して起こることが許されて、
    それらのすべてを同時に進行することが許される。

9.4.3.4 Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Parameter は情報を BehavioralFeature の発動に引き渡したり、
  発動から受け取ったりするのに使われる引数の仕様である。

* Parameter に ``defaultValue`` が指定されているならば、
  BehavioralFeature の発動時に実引数が何も渡されないときに限り、
  それは発動時に評価され、この Parameter の実引数として使われる。

* Parameter に ``name`` を与えることが許されており、
  そのときには同じ BehavioralFeature の Parameters の中から
  Parameter を一意に特定する。

  * Parameter に ``name`` がない場合、引数リストの位置で識別される。

* ``direction`` 特性は所有する BehavioralFeature に対して
  値が入力なのか出力なのかその両方なのかを指定する。
  その型は ParameterDirectionKind という列挙体で、
  次のリテラル値からなる。

  * in
  * inout
  * out
  * return

* BehavioralFeature は、
  ひとつを超える Parameter に対して、
  その方向を return にセットするという手段により、
  return Parameter と印をつけることは許されない。

* ``effect`` 特性は、
  Parameter に入出力されたオブジェクトに何を起こすかを指定するのに用いてよい。
  型は ParameterEffectKind という列挙体であり、
  次のリテラル値からなる。

  * create: out, inut, return な Parameter 限定。
  * read
  * update
  * delete: in または input な Parameter 限定。

* ``isException`` 特性は出力 Parameters に適用する。

* ``isStream`` 特性は、true であるときに、
  ストリーミング Parameter を示す。
  ストリーミング Parameter は
  この機能を実装する Behavior のどれもが、
  この Parameter 上でストリーミングな振る舞いを呈するという期待を表す。
  :doc:`./common-behavior` で述べる。

* BehavioralFeature が所有する ParameterSet とは、
  その BehavioralFeature を実装する Behaviors が使ってよい
  入力または出力の代用の集合を与える要素である。

  * ParameterSet にある Parameters はすべてが
    同じ BehavioralFeature の入力であるか、
    すべてが同じ BehavioralFeature の出力であるものとする。

  * すべてが入力の ParameterSet は入力 ParameterSet と呼ばれ、
    すべてが出力の ParameterSet は出力 ParameterSet と呼ばれる。

* ParameterSets のより詳細な意味と見本は :doc:`./actions` で見つけられる。

9.4.4 Notation
----------------------------------------------------------------------
* Feature に対する一般的な表記法はない。
  サブクラスはそれらに特有の表記法を定義する。

* 静的 Features は下線を付ける。

* Features がリストで示されるところでは、
  Features のリストの最終要素として省略記号 ``(...)`` を
  さらなる Features が存在するがそのリストには示されていないことを示すのに
  用いてよい。

* 読み取り専用 StructuralFeature は
  その StructuralFeature の表記法の一部として ``{readOnly}`` を使って示す。

* Feature 再定義は
  Feature 上に ``{redefines <x>}`` 特性文字列を使用して明示的に表記するか、
  別の Feature と isDistinguishableFrom() を使っても区別できない Feature を
  所有 Classifier のより一般な Classifiers のうちのひとつにあることをもって
  暗に示すかのどちらかでよい。

* Parameter は p. 108 の BNF の形式のテキスト文字列として示す。

  * 目を引くのは <perm-propery> だ。付加的な情報を示すのに用いる。
    値は ordered, unordered, unique, nonunique, seq の文字列から任意個選べる。

* Activity 図の ParameterSets の表記法は :doc:`./actions` で見つけられる。
  他の図式での ParameterSets の表記法はない。

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

9.6.3 Semantics
----------------------------------------------------------------------
9.6.3.1 Operations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

9.6.3.2 Template Operations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
OperationTemplateParameter
  * パラメーター化要素が Operation である TemplateParameter である。

9.6.3.3 Operation Template Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
