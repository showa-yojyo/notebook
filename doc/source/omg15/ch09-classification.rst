======================================================================
9 Classification
======================================================================

.. admonition:: 読者ノート

   現在ノート修正中。

.. contents::
   :depth: 2

9.1 Summary
======================================================================

分類は組織化において重要な技法だ。この章では分類に関する概念を規定する。中核概念
は Classifier すなわちその具象サブクラスが値の異なる種類の値を分類するのに用いら
れる抽象メタクラスだ。

この章のその他のメタクラスは Classifiers の構成要素、InstanceSpecifications を
使った Classifiers のオブジェクト化モデル、そしてこれらの概念すべての間にあるさ
まざまな関係を表現する。

9.2 Classifiers
======================================================================

9.2.1 Summary
----------------------------------------------------------------------

   A Classifier represents a classification of instances according to their
   Features.

* Classifier は Generalization によって階層的構造に組織化されている。
* RedefinableElements は Generalization の階層の文脈で再定義してもよい。

9.2.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 9.1 Classifiers

Classifier を中心とした図式だが、大量の関連が記されている。

``A_inheritedMember_inheritingClassifier``
  Classifier から NamedElement への関連（単方向）。

  * 継承されたメンバーの集合のことをその ``inheritedMember`` と呼ぶ。特に断りの
    ない限り、private な可視性ではない ``member`` だ。
  * 関連 ``A_member_memberNamespace`` を subsets する。

    * 関連端 ``inheritedMember`` は制約 ``{readOnly}`` がある。

``A_redefinedElement_redefinableElement``
  RedefinableElement から RedefinableElement への関連（単方向）。

  * 両関連端とも ``{readOnly, union}`` であり、多重度は ``*`` だ。

  ``A_redefinedClassifier_classifier``
    Classifier から Classifier への関連（単方向）。

    * 上記関連を subsets する。

``A_redefinitionContext_redefinableElement``
  RedefinableElement から Classifier への単方向関連。

  * 関連端 ``redefinitionContext`` は「メンバーがそこから再定義されてもよいよう
    な Classifier」を表す。
  * 両関連端とも ``{readOnly, union}`` であり、多重度は ``*`` だ。

    * とは言え、UML の仕様書では ``redefinitionContext`` が一つを超える事例はな
      い。

``A_feature_featuringClassifier``
  Classifier と Feature との間の関連（双方向）。

  * Classifier は Features の集合、そのうちのいくつかはその Classifier の
    ``attributes`` と呼ばれる Properties だ。下記関連のコメント参照。

  * ``A_member_memberNamespace`` を subsets する。

    * 両関連端にはさらに ``{readOnly, union}`` も付く。

  ``A_attribute_classifier``
    Classifier から Property への関連（単方向）。

    * 上記の関連と ``A_redefinitionContext_redefinableElement`` を subsets す
      る。

      * 両関連端にはさらに ``readOnly`` と ``union`` も付く。
      * 関連端 ``attribute`` のほうにはさらに ``{ordered}`` が加わっている。

``A_collaborationUse_classifier``
  Classifier から CollaborationUse への複合関連。

  * Classifier は、それを Collaborations に関係させる CollaborationUses を所有し
    てもよい。その Collaborations はこの Classifier の外観を描写する。
    :doc:`./ch11-structured-classifiers` で述べる。
  * ``A_ownedElement_owner`` を subsets する。

  ``A_representation_classifier``
    Classifier から CollaborationUse への関連（単方向）。

    * 上記関連を subsets する。
    * 関連端 ``representation`` の多重度は ``0..1`` だ。

``A_ownedUseCase_classifier``
  Classifier から UseCase への複合関連（単方向）。

  * Classifier は UseCases を所有してもよい。:doc:`./ch18-usecases` で述べる。
  * ``A_ownedMember_namespace`` を subsets する。

``A_generalization_specific``
  Generalization から Classifier への複合関連（両方向）。

  * 各 Generalization は ``specific`` を ``general`` と関係させる。
  * 与えられた Classifier に対し、その ``specific`` の推移閉包（グラフ論等で頻用
    する用語）をその specializations と呼ぶ。
  * ``A_ownedElement_owner`` と ``A_source_directedRelationship`` を subsets す
    る。

``A_general_generalization``
  Generalization から Classifier への関連（単方向）。

  * 与えられた Classifier に対し、その ``general`` の推移閉包をその
    ``generalizations`` と呼ぶ。特に直接の ``generalizations`` はその親と呼ばれ
    る。もっと言えば Classifier が Class のときには ``superClasses`` となる。
  * ``A_target_directedRelationship`` を subsets する。

``A_general_classifier``
  Classifier から Classifier への関連（単方向）。

  * 説明が見当たらないが、子クラスは親クラスに依存する、くらいの意味か。

``A_generalizationSet_generalization``
  後述。

``A_contract_substitution``
  Substitution から Classifier への関連（単方向）。

  * 意味は上述の Substitution のノートを参照。
  * 関連 ``A_supplier_supplierDependency`` を subsets する。

``A_substitution_substitutingClassifier``
  Classifier から Substitution への複合関連（両方向）。

  * 意味は上述の Substitution のノートを参照。
  * ``contract`` が実装する Interfaces は上記関連の ``substitutingClassifier``
    もまた実装する必要があるか、あるいは ``substitutingClassifier`` がより特殊な
    Interface 型を実装する必要がある。
  * ``contract`` が所有するどんな Port も上記関連の ``substitutingClassifier``
    が所有するある Port に match することが必要だ。
  * 関連 ``A_clientDependency_client`` と ``A_ownedElement_owner`` を subsets す
    る。

9.2.3 Semantics
----------------------------------------------------------------------

9.2.3.1 Classifiers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A Classifier has a set of Features, some of which are Properties called the
   ``attributes`` of the Classifier. Each of the Features is a ``member`` of the
   Classifier (see sub clause 7.4 Namespaces).

Classifier によって分類される値をその Classifier のオブジェクトと呼ぶ。

.. admonition:: 読者ノート

   私の UML ノートでは英単語 instance をオブジェクトと訳している。

Classifier を再定義することが許される。

Classifier は、Classifier を Collaborations に関連付ける CollaborationUses を所
有してもよい。Collaborations はこの Classifier の様子を記述するものだ。
:doc:`./ch11-structured-classifiers` 参照。

Classifier は UseCases を所有してよい。:doc:`./ch18-usecases` 参照。

9.2.3.2 Generalization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Generalizations define generalization/specialization relationships between
   Classifiers. Each Generalization relates a ``specific`` Classifier to a more
   ``general`` Classifier. Given a Classifier, the transitive closure of its
   ``general`` Classifiers is often called its :dfn:`generalizations`, and the
   transitive closure of its ``specific`` Classifiers is called its
   :dfn:`specializations`. The immediate ``generalizations`` are also called the
   Classifier’s parents, and where the Classifier is a Class, its
   ``superClasses`` (see 11.4).

汎化関係と特化関係の定義でもある。

   An instance of a Classifier is also an (indirect) instance of each of its
   generalizations. Any Constraints applying to instances of the generalizations
   also apply to instances of the Classifier.

チワワのオブジェクトは犬のオブジェクトでもあると言っている。

   When a Classifier is generalized, certain members of its generalizations are
   :dfn:`inherited`, that is they behave as though they were defined in the
   inheriting Classifier itself. For example, an inherited member that is an
   ``attribute`` may have a value or collection of values in any instance of the
   inheriting Classifier, and an inherited member that is an Operation may be
   invoked on an instance of the inheriting Classifier.

チワワは犬の ``attribute`` を持ったり、犬の Operation メンバーを呼ぶことが許され
る。

   The set of members that are inherited is called the ``inheritedMembers``.
   Unless specified differently for a particular kind of Classifier, the
   ``inheritedMembers`` are ``members`` that do not have private visibility.

継承メンバーは private でない。

   Type conformance means that if one Type conforms to another, then any
   instance of the first Type may be used as the value of a TypedElement whose
   ``type`` is declared to be the second Type.

Classifier は Type であり、それ自身とその一般化のすべてに対して適合する。

   The ``isAbstract`` property of Classifier, when true, specifies that the
   Classifier is abstract, i.e., has no direct instances:

抽象 Classifier のオブジェクトはすべて、その特殊化の一つのオブジェクトでなければ
ならない。

ある分類子（親）が別の分類子（子）を一般化する場合、子のオブジェクトがあらゆる状
況下で親のオブジェクトと置換可能であるとは限らない：

   For example, Circle may be defined as a specialization of Ellipse, and its
   instances would be substitutable in every circumstance involving accessing
   the properties of an Ellipse. However, if Ellipse were to define a stretch
   behavior that modifies the length of its major axis only, then a Circle
   object would be unable to implement such a behavior.

特性 ``isSubstitutable`` を、特定の Classifier が一般 Classifier が用いられ
る状況すべてにおいて使用可能かどうかを示すのに用いてよい。

9.2.3.3 Redefinition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Any ``member`` (that is a kind of RedefinableElement) of a generalization of
   a specializing Classifier may be redefined instead of being inherited.
   Redefinition is done in order to augment, constrain, or override the
   redefined ``member(s)`` in the context of instances of the specializing
   Classifier.

この場合、再定義 ``member`` は、再定義された ``member`` の代わりに特化Classifier
の構造または動作に与する。特化 Classifier のオブジェクトの文脈で再定義された
``member`` への参照は、再定義された ``member`` に解決されるものとする。

   The Classifier from which the member may be redefined is called the
   ``redefinitionContext``.

``redefinitionContext`` は RedefinableElement の種類ごとに定義され、``member``
の ``owner`` であることが多いが、常にそうとは限らない。

再定義要素一つが RedefinableElements 複数を再定義してもよい。

   The ``isLeaf`` property, when true for a particular RedefinableElement,
   specifies that it shall have no redefinitions.

   The detailed semantics of redefinition vary for each specialization of
   RedefinableElement.

再定義された要素とその再定義要素との間には、次のようなさまざまな種類の互換性があ
る：

* 名前互換性（再定義要素が被再定義要素と同じ ``name`` を持つ）
* 構造的互換性（被再定義要素のクライアントに見えるプロパティーが再定義要素のプロ
  パティーでもある）
* 動作的互換性（再定義要素が被再定義要素の代替となる）

   Classifier is itself a RedefinableElement. This can come into play when a
   Classifier is nested in a Class or Interface, which becomes the
   ``redefinitionContext``.

特化クラスまたはインターフェイスの文脈で Classifier を再定義すると、特化クラスま
たはインターフェイスのオブジェクトから再定義された Classifier への参照が、再定義
された Classifier に解決される効果がある。

9.2.3.4 Substitution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A Substitution is a relationship between two Classifiers which signifies that
   the ``substitutingClassifier`` complies with the contract specified by the
   ``contract`` Classifier. This implies that instances of the
   ``substitutingClassifier`` are runtime substitutable where instances of the
   ``contract`` Classifier are expected.

これは ``contact`` Classifier のオブジェクトが期待されるところでは
``substitutingClassifier`` のオブジェクトが実行時に置換可能であることを含意す
る。

Substitution は Specialization とは異なり、構造の継承を意味しない。公開された契
約の遵守のみを意味する。そのことは次を必要とする：

* ``contract`` Classifier が実装する Interface は ``substutingClassifier`` も実装
  するか、``substutingClassifier`` がより特殊な Interface 型を実装する。
* ``contract`` Classifier が所有する Port は ``substutingClassifier`` が所有する
  Port と合致する。

9.2.4 Notation
----------------------------------------------------------------------

9.2.4.1 Classifiers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Classifier は抽象メタクラスだ。それでもやはり、Classifier の具象サブクラスのどれ
にとっても利用可能な既定の表記法を一箇所で定義しておくことは都合が良い。

Classifier の既定の表記法は、Classifier の ``name`` を含む実線矩形であり、
``name`` の下部にある水平線により分離された区画がある。

   The ``name`` of the Classifier should be centered in boldface. For those
   languages that distinguish between uppercase and lowercase characters,
   Classifier ``names`` should begin with an uppercase character.

Classifier に対して既定の表記法を用いるならば、Classifier のメタクラスに対応する
キーワードを ``name`` の上部に guillemets で括って示すものとする。

  * キーワードについては :doc:`./anc-keywords` 参照。
  * メタクラスが Class であることを示すキーワードは必要ない。

キーワード（ステレオタイプ名を含む）はなるべく Classifier ``name`` の上部に
guillemets で括られ、プレーンな字面で中央寄せとする。

抽象 Classifier の ``name`` は利用フォントが許す限りイタリック体で示す。あるい
は ``name`` の後か下に ``{abstract}`` というテキスト注釈付きで示すことも認めら
れる。

Classifier 形状にある区画のいくらかは必須であり、具象構文に対する適合性がある
ツールで対応されるものとする。それ以外はオプション。

どの区画も非表示にしてよい。抑制された区画には、区切り線は引かれない。非表示の場
合、その中の要素の有無について推論を行うことはできない。

``attributes`` と名付けられた区画はその ``attribute`` 特性を介して到達される
Properties を示す表記法を含む。この区画は必須で、非表示でなければ常に他の区画の
上部に現れる。

``operations`` と名付けられた区画は Operations を示す表記法を含む。
``attributes`` 区画のすぐ下に表示される。この区画は Operation を所有する
Classifier のために使用される。

``receptions`` と名付けられた区画は Receptions を示す表記法を含む。この区画は必
須で、``operations`` 区画のすぐ下にある。この区画は Receptions を所有する
Classifier のために使用される。

   Any compartment which contains notation for Features may show those Features
   grouped under the literals public, private and protected, representing their
   ``visibility``.

Classifier が Constraints を所有するならば、適合性があるツールは所有する
Classifier の矩形の別の区画内にリストされた所有 Constraints を示す区画を実装して
よい。その場合、区画名は ``constraints`` だ。

9.2.4.2 Other elements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

汎化の矢印では鏃は白かと思っていたが、塗りなしが正解だ：

   A Generalization is shown as a line with a hollow triangle as an arrowhead
   between the symbols representing the involved Classifiers. The arrowhead
   points to the symbol representing the ``general`` Classifier.

同一の ``general`` Classifier を参照する複数の Generalizations を表すのに、それ
らの別々の矢印で表現しても共有して示しても、鏃を共有する様式の矢印で示してもかま
わない。

RedefinableElement を表す一般的な表記法はない。

Substitution は Dependency の記法を用いる。キーワードは ``«substitute»`` とす
る。

Classifier が継承した ``members`` を仮に ``member`` が継承されていなかったら示さ
れたであろうテキスト的表現に対して先頭にキャレット記号を付けることで Classifier
の図式上に示してよい。継承されたプロパティーの記法は次のように定義される：

.. code:: bnf

   <inherited-property> ::= ’^’ <property>

同様に、継承された Connectorの表記は：

.. code:: bnf

   <inherited-connector> ::= ’^’ <connector>

Classifier の ``inheritedMembers`` である NamedElements のすべて
に対して、継承されたものであることを示すのに、これと類比的な表記を用いてよい。

9.2.5 Examples
----------------------------------------------------------------------

いずれも矢印の向きとスタイルの規約を了解するだけで十分だ。

   Figure 9.2 Generalization notation showing different target styles

よくあるクラス継承図。個人的には shared target style の方が好みだ。

   Figure 9.3 Example of Substitution notation

Substitution の記法例。この図式は一般的な Window クラスが特定の環境において
Resizable Window クラスで代用可能であることを表現する。

9.3 Classifier Templates
======================================================================

9.3.1 Summary
----------------------------------------------------------------------

   Classifier is a kind of TemplateableElement signifying that a Classifier may
   be parameterized.

PackageableElement を介して ParameterableElement の一種であり、Classifier は仮
TemplateParameter であり、テンプレートの束縛で実引数として指定されることがある。

9.3.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 9.4 Classifier Templates

この図では Classifier が間接的に ParameterableElement の一種であることがすぐに思
い出せないかもしれない。

``A_ownedTemplateSignature_classifier``
  Classifier から RedefinableTemplateSignature への複合関連（両方向）。

  * ``A_redefinitionContext_redefinableElement`` を subsets する。
  * さらに ``A_ownedTemplateSignature_template`` を redefines する。

``A_extendedSignature_redefinableTemplateSignature``
  RedefinableTemplateSignature 間の関連（単方向）。

  * RedefinableTemplateSignature はテンプレートである親 Classifier 全ての
    RedefinableTemplateSignature を再定義する。
  * ``A_redefinedElement_redefinableElement`` を subsets する。

``A_inheritedParameter_redefinableTemplateSignature``
  RedefinableTemplateSignature から TemplateParameter への関連（単方向）。

  * ``A_parameter_templateSignature`` を subsets する。
  * 関連端 ``inheritedMember`` は ``{readOnly}`` だ。

``A_parameteredElement_templateParameter``
  ClassifierTemplateParameter と Classifier との間の関連（両方向）。

  * 先述の ClassifierTemplateParameter のノート参照。

    * ``parameteredElement`` が存在して抽象でなければ、
      引数として用いられる Classifier は抽象であってはならない。

  * これは既存の同名の関連を redefines する。

``A_constrainingClassifier_classifierTemplateParameter``
  ClassifierTemplateParameter から Classifier への関連（単方向）。

9.3.3 Semantics
----------------------------------------------------------------------

9.3.3.1 Template and Bound Classifiers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

テンプレートと被束縛要素の用語の意味は :doc:`./ch07-common-structure` で定義され
ている。

   A Classifier that is parameterized using a RedefinableTemplateSignature is
   called a :dfn:`template Classifier`, while a Classifier with one or more
   TemplateBindings is called a :dfn:`bound Classifier`.

7.3.3 節の仕様のままでは、内容が被束縛要素にどのようにマージされるかの詳細は未解
決だ。

   In the case of Classifier the semantics are equivalent to inserting an
   anonymous general bound Classifier representing the intermediate result for
   each binding, and specializing all these intermediate results by the bound
   Classifier.

拡張された被束縛 Classifier の構成員は、束縛において実引数として用いてよい。

被束縛 Classifier は、その束縛から生じるものの他に内容を持ってもよい。

   The parameters of a template Classifier can be any kind of TemplateParameter.
   Semantics and notation are only defined when the parameter is a Classifier, a
   LiteralSpecification, a Property or an Operation.

* 引数が Classifier のときには、ClassifierTemplateParameter で表現され、意味と表
  記法はこの章で規定する。
* 引数が LiteralSpecification のときには、意味と表記法は
  :doc:`./ch07-common-structure` で定義されているとおりだ。
* 引数が Operation であるときには、意味と表記法は 9.6 にあるとおりだ。
* 引数が Property であるときには、意味と表記法は 9.5 にあるとおりだ。

9.3.3.2 Template Classifier specialization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   RedefinableTemplateSignature specializes both TemplateSignature and
   RedefinableElement in order to allow the addition of new formal
   TemplateParameters in the context of a specializing template Classifier.

   A RedefinableTemplateSignature redefines the RedefinableTemplateSignatures of
   all parent Classifiers that are templates.

拡張（再定義）署名の仮 TemplateParameters すべては、拡張署名の仮
TemplateParameters として、拡張署名のために局地的に指定された任意の
TemplateParameters とともに含まれる。

9.3.3.3 Classifier Template Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   ClassifierTemplateParameter is a TemplateParameter where the
   ``parameteredElement`` is a Classifier in its capacity of being a kind of
   ParameterableElement.

Classifier のサブクラスは TemplateParameters として引数化、束縛、使用することが
できる。Class のサブクラスである Behavior も同様で、Behavior のすべてのサブクラ
スが該当する。

ClassifierTemplateParameter の ``constrainingClassifier`` 特性は引数として使用可
能である実引数を制約する Classifiers の集合を指定する。この集合に Classifier が
存在する場合、その引数は、以下の意味で、すべての Classifiers と互換性があるもの
とする：

* ``allowSubstitutable`` が真ならば、互換性は ``contract`` が
  ``constrainingClassifier`` である Substitution をさらに許す。
* ``allowSubstitutable`` が偽ならば、互換性とは ``constrainingClassifiers`` すべ
  てと同じであることか、その特殊化であることを意味する。

さらに ``constrainingClassifiers`` があれば、``parameteredElement`` は次のように
制約が付くものとする：

* ``allowSubstitutable`` が真ならば、互換性は ``contract`` が
  ``constrainingClassifier`` である Substitution を追加的に認める。
* ``allowSubstitutable`` が偽ならば、互換性とは ``constrainingClassifiers`` すべ
  てと同じであるか、直接的特殊化されたものであり、さらなる機能はないことを意味す
  る。

すべての場合で、``parameteredElement`` が抽象的でなければ、実引数として用いられ
る Classifier は抽象的ではないものとする。

   In all cases, if the parameteredElement is not abstract then the Classifier
   used as an argument shall not be abstract.

これとは別に、特性 ``constrainingClassifier`` が空である場合、引数として使用でき
る Classifier には制約がない。この場合、``parameteredElement`` は汎化も機能も持
たず、``allowSubstitutable`` は偽でなければならない。

9.3.4 Notation
----------------------------------------------------------------------

これは :doc:`./ch07-common-structure` の Templates の記法の焼き直しのようだ。

被束縛 Classifier が Property の型として直接使用される場
合、``<template-param-name>`` はその表記において Property の ``<prop-type>`` と
して機能する。

   The general notation for template parameters specified in 7.3.4 is extended
   for the parameters of a template Classifier to include the following:

   .. code:: bnf

      <template-parameter> ::= <classifier-template-parameter> | <operation-template-parameter> | <connectable-element-template-parameter>

ClassifierTemplateParameter は TemplateParameter の表記を拡張して、オプションの
型制約を含むようにしたものだ：

.. code:: bnf

   <classifier-template-parameter> ::= <parameter-name> [ ‘:‘ <parameter-kind> ] [‘>’ <constraint>] [‘=’ <default>]
   <constraint> ::= [‘{contract}’] <classifier-name>*
   <default> ::= <classifier-name>

*<parameter-kind>* は ``parameteredElement`` のメタクラスを表す。クラスであれば抑
止されても構わない。

*<constraint>* の *<classifier-name>* は、先述の意味論で指定された意味を持つ
``constrainingClassifier`` を指定する（0個以上あってもよい）。``{contract}`` オ
プションは ``allowSubstitutable`` が真であることを示す。

9.3.5 Examples
----------------------------------------------------------------------

   Figure 9.5 Template Class and Bound Class

クラステンプレート ``FArray`` の図式か。

* ``T``, ``k`` がそれぞれ TemplateParameter だ。
* ``T`` は制約なしクラスの、``k`` は LiteralInteger の TemplateParameter だ。
* ``k`` の方には既定値の指定が付いている。
* ``AddressList`` は被束縛 Class だ。

   Figure 9.6 Anonymous Bound Class

匿名被束縛 Class の見本。C++ 風に書くと ``FArray<Point>`` を表現する図。 Pointク
ラス を ``T`` に代入する無名束縛クラス。``k`` の代入がないため、既定値 10 が使用
される。

   Figure 9.7 Template Class with constrained Class parameter

二つの仮引数 ``CarEngine`` と ``n`` を持つクラステンプレート ``Car`` の図式。

* TemplateParameter ``CarEngine`` には ``Engine`` という Class に適合する制約が
  指定されている。
* ``n`` は LiteralInteger だ。

   Figure 9.8 Bound Class

これは被束縛 Class の記法の見本。三輪のディーゼル車のクラスを定義する。

* 被束縛 Class の名前は ``DieselCar`` だ。
* TemplateParameter である ``CarEngine`` と ``n`` に対して ``DieselEngine`` と
  ``2`` をそれぞれ束縛している。

9.4 Features
======================================================================

9.4.1 Summary
----------------------------------------------------------------------

   Features represent structural and behavioral characteristics of Classifiers.

9.4.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 9.9 Features

クラスの他に列挙体がある。

``A_feature_featuringClassifier``
  先述の通り。

``A_raisedException_behavioralFeature``
  BehavioralFeature から Type への関連（単方向）。

  * BehavioralFeature はその呼出期間中に例外を送出してもよい。この関連はその例外
    の型を指定する。

``A_method_specification``
  BehavioralFeature と Behavior の間の関連（両方向）。

  * 多重度は ``specification`` ``0..1`` に対して ``method`` ``*`` だ。
  * BehavioralFeature の挙動の応答を定義する一つの方法は、それを実装するような
    Behavior を一つまたは複数指定することだ。この関連はその指定を示す。

``A_ownedParameter_ownerFormalParam``
  BehavioralFeature から Parameter への複合関連（単方向）。

  * 関連端 ``ownedParameter`` はその BehavioralFeature が呼び出されるときに与え
    られる引数の順序、型、入出力方向の特徴を述べるものだ。

    * それゆえ ``ownedParameter`` は ``{ordered}`` だ。

  * ``A_ownedMember_namespace`` を subsets する。

``A_ownedParameterSet_behavioralFeature``
  BehavioralFeature から ParameterSet への複合関連（単方向）。

  * 上述関連の代替？
  * ``A_ownedMember_namespace`` を subsets する。

``A_defaultValue_owningParameter``
  Parameter から ValueSpecification への複合関連（単方向）。

  * ``defaultValue`` が指定されていれば、その BehavioralFeature の呼び出し時に実
    引数が与えらていない場合に限り、この Parameter として評価されて用いられる。
  * ``A_ownedElement_owner`` を subsets する。
  * 多重度は両端ともに ``0..1`` だ。

``A_parameterSet_parameter``
  Parameter と ParameterSet の間の関連（両方向）。

  * 多重度は ``parameter`` ``1..*`` に対して ``parameterSet`` ``*`` だ。

``A_condition_parameterSet``
  ParameterSet から Constraint への複合関連（単方向）。

  * 関連端 ``condition`` の意味は、入力 ParameterSet のそれが Operation における
    ``preconditions`` と、出力 ParameterSet のそれが Operation における
    ``postconditions`` とそれぞれ同じだ。
  * ``A_ownedElement_owner`` を subsets する。

9.4.3 Semantics
----------------------------------------------------------------------

9.4.3.1 Features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Each Feature is associated with a Classifier called its
   ``featuringClassifier``. The Feature represents some structural or behavioral
   characteristic for its ``featuringClassifier``, except for Properties acting
   as ``qualifiers`` (see 9.5.3).

ここはまだわからない。

   The ``isStatic`` property specifies whether the characteristic relates to the
   Classifier’s instances considered individually (``isStatic`` = false), or to
   the Classifier itself (``isStatic`` = true).

その機能が static であるか否かが明示的に指定されていない場合、static でないと指
定されたとみなす。

9.4.3.2 Structural Features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A StructuralFeature is a typed Feature of a Classifier that specifies the
   structure of instances of the Classifier.

StructuralFeature の主旨はオブジェクトの構造にある。

   The StructuralFeatures of a Classifier that are Properties are called the
   ``attributes`` of the Classifier (see 9.2.3).

UML では Property は唯一の StructuralFeatur であるので、Classifier の
StructuralFeatures は全部 Properties であり、すなわち ``attributes`` だ。

Classifier の各オブジェクトには Classifier の直接または継承した非静的
``attributes`` の値（の集まり）が次のように存在する：

* ``attribute`` の多重度が ``0..1`` であれば、値が一つもないか、Type が
  ``attribute`` の Type に適合する単一の値が存在するかのいずれかでなければならな
  い。
* ``attribute`` の多重度が ``1..1`` であれば、その Type が ``attribute`` の Type
  に適合する単一の値が存在しなければならない。
* ``attribute`` の多重度が ``j..k`` で ``k`` が 1 でない場合、``j`` 個以上 ``k``
  個以下の値の集まりが存在して、それぞれは Types が ``attribute``
  の Type に適合しなければならない。
* ``attribute`` の多重度が ``0`` であれば、値が存在しないものとする。

StructuralFeature に ``isStatic`` が ``true`` であると、上記の各項目はオブジェク
ト個々に対してではなく、ある実行有効範囲内で識別可能な個体とみなされる
Classifier 自身に関係する。

適合性のあるツールでは、継承された静的 StructuralFeature のそれぞれが次の二者択
一の一方でなければならない：

#. Java や C# の静的メンバー流：

      Within an execution scope, the value or collection of values of the
      StructuralFeature is always the same for any inheriting Classifier as its
      value or collection of values for the owning Classifier.

#. Ruby や Smalltalk でのクラスオブジェクト変数流：

      Within an execution scope, the StructuralFeature has a separate and
      independent value or collection of values for its owning Classifier and
      for each Classifier that inherits it.

最後に ``isReadOnly`` の仕様だ：

   If a StructuralFeature is marked with ``isReadOnly`` true, then it may not be
   updated once it has been assigned an initial value. Conversely, when
   ``isReadOnly`` is false (the default), the value may be modified.

9.4.3.3 Behavioral Features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A non-static BehavioralFeature specifies that an instance of its
   ``featuringClassifier`` will react to an *invocation* of the BehavioralFeature
   by carrying out a specific behavioral response.

呼び出しだとか、応答だとかというキーワードを憶えておく。

   The list of ``ownedParameters`` describes the order, type, and direction of
   arguments that may be given when the BehavioralFeature is invoked, or which
   are output and returned when the invocation completes.

メンバー関数の引数リストに対応する概念だろう。

* 方向が ``in`` または ``inout`` である ``ownedParameters`` は、
  BehavioralFeature を呼び出すときに与えられる引数を定義する。
* 方向が ``out``, ``inout``, ``return`` のいずれかである ``ownedParameters``
  は、呼び出しに成功したときに出力、返される引数を定義する。

例外送出の概念がある：

   A BehavioralFeature may raise an exception during its invocation. Possible
   exception types may be specified by attaching them to the BehavioralFeature
   using the ``raisedException`` association.

BehavioralFeature と Behavior の関係：

   One way to define the behavioral response of a BehavioralFeature is to
   specify one or more Behaviors as ``methods`` that implement the
   BehavioralFeature.

特性 ``isAbstract`` が ``true`` のとき、BehavioralFeature にはそれを実装する
``methods`` が何もないことを指定する。より特殊な BehavioralFeature から実装が与
えられることを期待する。

同時呼び出しについて：

   The ``concurrency`` property specifies the semantics of concurrent calls to
   the same instance.

この特性の型は CallConcurrencyKind という列挙体で、次のリテラル値をとる：

``sequential``
  同時実行を管理する仕組みは一つも BehavioralFeature に関連しない。
``guarderd``
  時間的に重なり合う BehavioralFeature の複数発動が一つのオブジェクトに対し
  て起こることが許されるが、開始が許されるのは一つしかない。残りは現在実行
  中の BehavioralFeature が完了するまでブロックされる。
``concurrent``
  時間的に重なり合う BehavioralFeature の複数呼び出しが一つのオブジェクトに対し
  て起こることが許されて、それらのすべてが同時に進行することを許す。

9.4.3.4 Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A Parameter is a specification of an argument used to pass information into
   or out of an invocation of a BehavioralFeature.

Parameter にも Type と Multiplicity の概念があり、以前テンプレートの章で見た仕様
と同様なのでノートを省略する。

次の概念はよく知られている：

   If a ``defaultValue`` is specified for a Parameter, then it is evaluated at
   invocation time and used as the argument for this Parameter if and only if no
   argument is supplied at invocation of the BehavioralFeature.

引数の名前について。なければ引数リストにおける位置で識別される：

   A Parameter may be given a ``name``, which then identifies the Parameter
   uniquely within the Parameters of the same BehavioralFeature. If it is
   unnamed, it is distinguished only by its position in the ordered list of
   Parameters.

引数には方向性がある：

   The ``direction`` property specifies whether a value is passed into, out of,
   or both into and out of the owning BehavioralFeature.

その型は ParameterDirectionKind という列挙体で、次のリテラル値からなる：

  * ``in``
  * ``inout``
  * ``out``
  * ``return``

BehavioralFeature では複数の Parameter を ``return`` としてマークすることは許さ
れない。

   The ``effect`` property may be used to specify what happens to objects passed
   in or out of a Parameter.

これは設計者の意図の宣言という意味合いが強い。実行中に複数の効果がある場合もあ
る。型は ParameterEffectKind という列挙体であり、次のリテラル値からなる：

* ``create``
* ``read``
* ``update``
* ``delete``

この特性は ``direction`` の取る値とも整合性を取る必要がある：

   Only ``in`` and ``inout`` Parameters may have a ``delete`` ``effect``. Only
   ``out``, ``inout``, and ``return`` Parameters may have a ``create``
   ``effect``.

引数が例外であるかどうかという概念がある：

   The ``isException`` property applies to output Parameters.

BehavioralFeature の呼び出し中に ``isException`` が true の Parameter に出力され
ると、同じ呼び出し中にその BehavioralFeature の他の出力に出力されることが排除さ
れる。

次に述べられる概念がよくわからない。UNIX のパイプのようなものか？

   The ``isStream`` property, when true, designates a streaming Parameter. A
   streaming Parameter expresses the expectation that any Behavior implementing
   this feature will exhibit streaming behavior on this Parameter - see sub
   clause 13.2.

BehavioralFeature が所有する ParameterSet とは、その BehavioralFeature を実装
する Behaviors が使ってよい入力または出力の代替集合を与える要素だ。

* ParameterSet にある Parameters はすべてが同じ BehavioralFeature の入力である
  か、すべてが同じ BehavioralFeature の出力であるものとする。
* すべてが入力の ParameterSet は入力 ParameterSet と呼ばれ、すべてが出力の
  ParameterSet は出力 ParameterSet と呼ばれる。

   A BehavioralFeature with input ParameterSets may only accept inputs from
   Parameters in one of the sets per invocation.

出力についても同様のことしか受け付けられない。

   The semantics of ``conditions`` on input and output ParameterSets of
   BehavioralFeatures is the same as Operation ``preconditions`` and
   ``postconditions``, respectively, but apply to only to invocations that
   accept inputs to or return outputs from Parameters in the ParameterSet having
   the ``condition``.

ParameterSets のより詳細な意味と見本は :doc:`./ch16-actions` で見つけられる。

9.4.4 Notation
----------------------------------------------------------------------

Feature に対する一般的な記法はない。サブクラスが特有の記法を定義する。

* 静的 Features は下線を付ける。
* Features が一覧で示される場合、Features のリストの最終要素として省略記号
  ``(...)`` を、その一覧には示されていないがさらなる Features が存在することを示
  すのに用いてよい。
* 読み取り専用 StructuralFeature はその記法の一部として ``{readOnly}`` を使って
  示す。
* Feature 再定義は Feature 上に ``{redefines <x>}`` 特性文字列を使用して明示的に
  表記するか、所有 Classifier のより一般な Classifiers のうちの一つに別の
  Featureと ``isDistinguishableFrom()`` を使って、区別できない Feature をあるこ
  とをもって暗に表記してよい。

Parameter テキスト文字列として示す：

.. code:: bnf

   <parameter> ::= [<direction>] <parameter-name> ’:’ <type-expression>
     [’[’ <multiplicity-range> ’]’] [’=’ <default>]
     [’{’ <parm-property> [’,’ <parm-property>]* ’}’]
   <direction> ::= ’in’ | ’out’ | ’inout’
   <parm-property> ::= ’ordered’ | ’unordered’
     | ’unique’ | ’nonunique’
     | ’seq’ | ’sequence’

* ``<direction>`` は省略時は ``in`` とする。
* ``<default>`` は Parameter の既定値に対する値指定を定義する式とする。
* ``<parm-property>`` は Parameter に適用される追加的特性値を示す。最後の
  ``seq``, ``sequence`` は読まないとわからない：

     ’seq’ or ’sequence’ applies when there is a multi-valued Parameter and
     means that its values constitute an ordered bag, i.e., ``isUnique`` = false
     and ``isOrdered`` = true.

  ドラクエの道具袋のようなデータ構造か？

Activity 図の ParameterSets の記法は :doc:`./ch16-actions` で見つけられる。その
他の図式では ParameterSets の記法はない。

9.5 Properties
======================================================================

9.5.1 Summary
----------------------------------------------------------------------

   Properties are StructuralFeatures that represent the ``attributes`` of
   Classifiers, the ``memberEnds`` of Associations, and the ``parts`` of
   StructuredClassifiers.

9.5.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 9.10 Properties

Property を中心とした図式だ。

``A_ownedAttribute_interface``, ``A_ownedAttribute_datatype``, ``A_ownedAttribute_class``
  それぞれ Interface, DataType, Class から Property への複合関連（両方向）。

  * 関連端 ownedAttribute は Classifier の ``attribute`` であるということを表し
    ている。
  * ``A_attribute_classifier`` と ``A_ownedMember_namespace`` を subsets する。
    さらに Class 版関連だけはまだ説明されていない関連を subsets または redefines
    する。

``A_memberEnd_association``
  Association と Property 間の関連（両方向）。

  * 関連端 ``memberEnd`` は Association の一方の関連端であることを表す。

    * 二項関連においては、Property は同時に ``ownedAttribute`` と ``memberEnd``
      であってもよい。どちらか一方の場合、生成されたときに Property は関連の位数
      に従った個数の Classifier のオブジェクトに関連したある値・値の集まりを表現
      する。この Classifiers の集まりをその Property の ``context`` と呼ぶ。

  * ``A_member_memberNamespace`` を subsets する。

``A_ownedEnd_owningAssociation``
  これは :doc:`./ch11-structured-classifiers` で説明する。

``A_qualifier_associationEnd``
  Property から Property への複合関連（両方向）。

  * 上述の関連端 ``memberEnd`` な Property にはそれ自身が ``qualifiers`` として
    働くような他の Properties があってもよい。
  * 関連端 ``qualifier`` は ``{ordered}`` だ。
  * ``A_ownedElement_owner`` を subsets する。

``A_defaultValue_owningProperty``
  Propery から ValueSpecification への複合関連（単方向）。

  * 関連 ``A_ownedElement_owner`` を subsets する。
  * 多重度は両端ともに ``0..1`` だ。

``A_opposite_property``
  Property から Property への関連（単方向）。

  * 説明なし。
  * 多重度は両端ともに ``0..1`` だ。

``A_subsettedProperty_property``
  Property から Property への関連（単方向）。

  * これは Property が集約であるときに、``subsetttedProperty`` が ``property``
    から重複構成要素を除外した集合であることを表す。

``A_redefinedProperty_property``
  Property から Property への関連（単方向）。

  * 説明なし。
  * ``A_redefinedElement_redefinableElement`` を subsets する。
  * 多重度は両端ともに ``*`` だ。

9.5.3 Semantics
----------------------------------------------------------------------

Property は属性か要因端子：

   A Property may represent an ``attribute`` of a Classifier, a ``memberEnd`` of
   an Association, or in some cases both simultaneously.

一般的なモデリングシナリオで便利な慣習は、型が Class の一種である Property が
Association 端子である一方、他方では型が DataType の一種である Property はそう
ではないとうものだ。

Propertyは、1つまたは複数のオブジェクトの宣言された状態を、値または値に対する名
前付き関係で表します。

* Property が Classifier の非静的 ``attribute`` である場合、値は、オブジェクトの
  スロットに保持されることによってClassifier のオブジェクトに関連する。
* Property が Association の ``memberEnd`` である場合、値は、Association の他方
  の端にあるオブジェクトか、または Association のその他の端子におけるオブジェク
  トだ。
* Property が Classifier の静的 ``attribute`` である場合、値は、ある実行有効域で
  Classifier 自体に関連する。

..

   A Property that is a ``memberEnd`` may itself have other Properties that
   serve as ``qualifiers``.

* Property が ``ownedAttribute`` を介して Association 以外の Classifier によって
  所有される場合、その Classifier の ``attribute`` を表す。
* Property が ``memberEnd`` を介して Association 以外に関連する場合、それは
  Association の端子を表す。二項関連の場合、その両方が同時に存在してもよい。

いずれの場合も：

   when instantiated a Property represents a value or collection of values
   associated with an instance of one (or in the case of a ternary or
   higher-order association, more than one) Classifier.

``defaultValue`` の仕様：

   If there is a ``defaultValue`` specified for a Property, this default is
   evaluated when an instance of the Property is created -略-

``isDerived`` の仕様：

   If a Property has ``isDerived`` = true, it is derived and its value or values
   may be computed from other information.

Property は間接的に RedefinableElement の一種であり、Property は再定義することが
許される。その際：

   The ``name`` and ``visibility`` of a Property are not required to match those
   of any Property it redefines.

既定値の再定義に関する優先順位：

   If a Property has a specified default, and the Property redefines another
   Property with a specified default, then the redefining Property’s default is
   used in place of the more general default from the redefined Property.

時には、一つのオブジェクトがオブジェクトの集合をまとめるのに用いられる状況をモデ
ル化するために Property が用いられることがあり、これは :dfn:`集約 (aggregation)`
と呼ばれる。

   To represent such circumstances, a Property has an ``aggregation`` property,
   of type AggregationKind; the instance representing the whole group is
   classified by the owner of the Property, and the instances representing the
   grouped individuals are classified by the type of the Property.

AggregationKind は次のリテラル値からなる列挙型だ：

``none``
  Property に集約の意味がないことを示す。
``shared``
  Property に共有集約の意味があることを示す。共有集約の正確な意味は応用領域と設
  計者によって異なる。
``composite``
  Property が複合的に集約されていることを示す。集約している方が構成されたオブ
  ジェクトの存在と保存に責任を持つ。

よく知られているが複合集約の特徴を引用する：

   Composite aggregation is a strong form of aggregation that requires a
   ``part`` object be included in at most one composite object at a time. If a
   composite object is deleted, all of its part instances that are objects are
   deleted with it.

.. admonition:: 読者ノート

   原文は instance と object を明らかに使い分けている。私は両者のニュアンスの
   差を全く理解していない。

複合は、他動的削除特性を持つ有向非循環グラフで結合されることがある。グラフのある
部分のオブジェクトを削除すると、そのオブジェクトの下の部分グラフのオブジェクトす
べても削除されるのだ。

``subsettedProperty`` の説明。重複を除外して集めるということを憶えておく：

   A Property may be marked as the subset of another ``subsettedProperty``. In
   this case, calculate a set by eliminating duplicates from the collection of
   values denoted by the subsetting property in some context. Then that set
   shall be included in (or the same as) a set calculated by eliminating
   duplicates from the collection of values denoted by the ``subsettedProperty``
   in the same context.

``isDerivedUnion`` の説明：

   A Property may be marked as being a derived union, by setting
   ``isDerivedUnion`` to true. This means that the collection of values denoted
   by the Property in some context is derived by being the strict union of all
   of the values denoted, in the same context, by Properties defined to subset
   it.

ある Property が、そのすべての ``{subsets}`` である Properties の和集合と一致す
るとき、その Property は導出和集合であると呼ぶのだろう。

導出和集合としてマークされた属性が ``isOrded`` が真でマークされ、特定の文脈でそ
れの部分集合特性のすべてが ordered か、上限が 1 であるとマークされた属性で、その
文脈での ``Classifier::allAttributes()`` 操作の値が well-defined な順序を与える
とき、和集合の順序は ``allAttributes()`` の結果に出現する順序で部分集合特性を評
価して結果を連結して定義される。

   A Property may be marked, via the property ``isID``, as being (part of) the
   identifier (if any) for Classifiers of which it is a member.

この解釈は未解決だが、RDB のテーブルの主キーや XML の ID 属性などの実装に写像さ
れる可能性がある。

   Property specializes ParameterableElement to specify that a Property may be
   exposed as a formal ConnectableElementTemplateParameter (see 11.2.3), and
   provided as an actual parameter in a binding of a template.

テンプレート内で Property TemplateParameter は他の任意のアクセスできる Property
と同じように使用することが許される。テンプレート内の Property TemplateParameter
へのあらゆる参照は最終的に被束縛要素内の実 Property への参照となる。

9.5.4 Notation
----------------------------------------------------------------------

Property の特殊化のいくつかには追加の表記形式がある。これらは、それらのクラスの
適切な記法のサブクラスで扱う。

.. code:: bnf

   <property> ::= [<visibility>] [‘/’] <name> [‘:’ <prop-type>]
       [‘[‘ <multiplicity-range> ‘]’]
       [‘=’ <default>]
       [‘{‘ <prop-modifier> [‘,’ <prop-modifier>]* ’}’]

   <visibility> ::= ‘+’ | ‘-‘ | ‘#’ | ‘~’

* ``/`` は Property が導出されていることを示す。
* Property に名前がない場合は ``<name>`` は空文字列となる。

.. code:: bnf

   <prop-modifier> ::= ‘readOnly’ | ‘union’
       | ‘subsets’ <property-name>
       | ‘redefines’ <property-name>
       | ‘ordered’ | ‘unordered’
       | ‘unique’ | ‘nonunique’
       | ‘seq’ | ‘sequence’
       |‘id’ | <prop-constraint>

* ``union`` は Property がその部分集合の導出和集合であることを意味する。
* ``subsets <property-name>`` は Property が ``<property-name>`` で識別される
  Property の真部分集合であることを意味する。``<property-name>`` は修飾されてい
  てもかまわない。
* ``id`` は Property がクラスの識別子の一部であることを意味する。
* ``<prop-constraint>`` は Property に適用される制約を指定する式だ。

修飾子 (qualifiers) の記法は :doc:`./ch11-structured-classifiers` で定義する。

Property の集約に対する記法は :doc:`./ch11-structured-classifiers` で定義する。

   In a Classifier, the type, visibility, default, multiplicity, property string
   may be suppressed from being displayed, even if there are values in the
   model.

Classifier においては、属性の個々の特性が連続する文字列としてではなく、縦に並ん
で表示されることがある。

集約矢印には始点側にダイヤモンドマーカーしか示されることが認められない：

   In a Classifier, an attribute may also be shown using association notation,
   where only an aggregation adornment (hollow or filled diamond) may be shown
   at the tail of the arrow.

Property によるテンプレート Classifier の引数化に用いられる
ConnectableElementTemplateParameter の記法：

.. code:: bnf

   <connectable-element-template-parameter> ::= <property-name> ‘: Property’

9.5.5 Examples
----------------------------------------------------------------------

   Figure 9.11 Examples of attributes

* ``ClassB::id`` は ``ClassA::name`` の再定義とある。再定義ではメンバー名が変わ
  ることもあるようだ。
* ``ClassB`` の ``Integer = 7`` は ``height`` メンバーに相当する。脱字ではない？
* ``ClassB::width`` は ``Class::width`` の再定義であって、導出ではない。

   Figure 9.12 Association-like notation for attributes

属性が関連の記法でどう示されるのかを示す。

9.6 Operations
======================================================================

9.6.1 Summary
----------------------------------------------------------------------

   An Operation is a BehavioralFeature that may be owned by an Interface,
   DataType or Class. Operations may also be templated and used as template
   parameters.

9.6.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 9.13 Operations

Operation を中心とした図式。左側は Property の図式とそっくり。

``A_ownedOperation_interface``, ``A_ownedOperation_datatype``, ``A_ownedOperation_class``
  Interface, DataType, Class いずれかから Operation への複合関連（双方向）。

  * 各 Classifier が Operation(s) を所有してもよいという意味。
  * ``ownedOperation`` は ``{ordered}`` だ。
  * ``A_feature_featuringClassifier`` を subsets する。
  * ``A_redefinitionContext_redefinableElement`` を subsets する。
  * ``A_ownedMember_namespace`` を subsets する。

``A_ownedParameter_operation``
  Operation から Parameter への複合関連（双方向）。

  * Parameter は Operation の構成要素の一つだ。
  * ``A_ownedParameter_ownerFormalParam`` を subsets する。

    * ownedParameter の方は ``{ordered, redefines ownedParameter}`` となってい
      る。

``A_precondition_preContext``, ``A_postcondition_postContext``, ``A_bodyCondition_bodyContext``
  Operation から Constraint への複合関連（単方向）。

  * ``precondition`` と ``postcondition`` は Operation の呼び出しに関する事前条
    件と事後条件をそれぞれ意味する。
  * ``bodyCondition`` は Operation の戻す結果をその仕様が計算する値によって縛り
    をかける。
  * ``A_ownedRule_context`` を subsets する。

``A_raisedException_operation``
  Operation から Type への関連（単方向）。

  * Operation はその呼出期間中に例外を送出してもよい。そういう場合は上述の
    ``postcondition`` や ``bodyCondition`` は成立していると仮定するべきではな
    い。

  * ``A_raisedException_behavioralFeature`` を subsets する。

    * 図では ``operation`` が ``{subsets}`` で ``raisedException`` が
      ``{redefines}`` になっている？

``A_redefinedOperation_operation``
  Operation から Operation への関連（単方向）。

  * Operation を継承クラスで再定義することを示す関連だろうか。
  * ``A_redefinedElement_redefinableElement`` を subsets する。

``A_parameteredElement_templateParameter``
  * OperationTemplateParameter と Operation の間の関連（双方向）。
  * 同名関連の redefines だ。

9.6.3 Semantics
----------------------------------------------------------------------

9.6.3.1 Operations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Operation は Interface, DataType, または Class の BehavioralFeature だ。
Operation はその ``featuringClassifier`` のオブジェクトに対して直接呼び出すこと
ができる。Operation はそのような呼び出しに対して ``name``, ``type``, Parameters,
Constraints を指定する。

戻り値があれば、Operation の型はこの Parameter のそれと同じだ。それ以外の場合に
は Operation に型はない。

   The ``preconditions`` for an Operation define conditions that shall be true
   when the Operation is invoked. These ``preconditions`` may be assumed by an
   implementation of this Operation. The behavior of an invocation of an
   Operation when a ``precondition`` is not satisfied is not defined in UML.

Operation に対する ``precondition`` は Operation が呼び出されるときに真でなけれ
ばならない条件を定義する。

Operation の ``postcondition`` は、``precondition`` が満たされ、Operation 呼び出
しが正常に完了したときに真となる条件を定義する。

次の ``bodyCondition`` の仕様がよくわからない：

   The ``bodyCondition`` for an Operation constrains the return result to a
   value calculated by the specification of the ``bodyCondition``. This value
   should satisfy the ``postconditions``, if any.

戻り値はこの条件から制約をかけられ、さらに事後条件もなるべく満たす。

   The ``bodyCondition`` differs from ``postconditions`` in that the
   ``bodyCondition`` may be overridden when an Operation is redefined, whereas
   ``postconditions`` may only be added during redefinition.

事後条件がその内容を取り消す方向に上書きされるのはおかしいのは理解できる。この比
較からすると ``bodyCondition`` は Operation の実装に対する条件なのかもしれない。

Operation は呼び出し中に例外を送出してよい：

   When an exception is raised, it should not be assumed that the
   ``postconditions`` or ``bodyCondition`` of the Operation are satisfied.

Operation の再定義について：

   An Operation may be redefined in a specialization of the
   ``featuringClassifier``. This redefinition may add new ``preconditions`` or
   ``postconditions``, add new ``raisedExceptions``, or otherwise refine the
   specification of the Operation.

事前・事後条件は追加なら許される。例外を追加するのが許されているのは微妙ではない
か。

次の記述は Operation の再定義における引数と戻り値の型の変化仕様についてだ：

   Different type-conformance systems adopt different schemes for how the types
   of parameters and results may vary when an Operation is redefined in a
   specialization.

:dfn:`不変性 (invariance)`
  型が変化しなくてもよい
:dfn:`共変性 (covariance)`
  引数型が特化型に特化してもよい
:dfn:`反変性 (contravariance)`
  引数型が特化型に汎化してもよい

   If the ``isQuery`` property is true, an invocation of the Operation shall not
   modify the state of the instance or any other element in the model.

C++ で言うところの ``const`` メンバー関数のような概念よりも強い。

9.6.3.2 Template Operations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Operation specializes TemplateableElement in order to support specification
   of template Operations and bound Operations. Bound Operations must be owned
   by a Classifier.

元の操作が Behavior で定義されている場合、被束縛要素はその Behavior と整合する分
Classifier によって所有されているものとする。つまり、次のいずれか一つが成り立つ：

* 束縛された操作がテンプレートと同じ Classifier に現れる。
* 束縛された操作がテンプレート所有者の部分型に現れる
* テンプレートが静的クラスで副作用なしに定義され、束縛された操作がどこにでも現れ
  る。

9.6.3.3 Operation Template Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   An Operation may be exposed by a template as a formal template parameter via
   an OperationTemplateParameter.

OperationTemplateParameter は TemplateParameter の一種で、引数となる要素が
Operation であることを表すものだ。テンプレート Classifier の中では、
OperationTemplateParameter はアクセス可能な他の Operation と同様に使用することが
許される。

テンプレート内の OperationTemplateParameterへの参照は、結局、束縛された
Classifier 内の実 Operation への参照となる。例えば、OperationTemplateParameter
の呼び出しは実 Operation への呼び出しとなる。

   A default for an OperationTemplateParameter must be an Operation with the
   same parameter types, directions, and multiplicities as the exposed
   Operation.

9.6.4 Notation
----------------------------------------------------------------------

Operation のテキスト表記法：

.. code:: bnf

   [<visibility>] <name> ‘(‘ [<parameter-list>] ‘)’
       [‘:’ [<return-type>] [‘[‘ <multiplicity-range> ‘]’]
              [‘{‘ <oper-property> [‘,’ <oper-property>]* ‘}’]]

   <parameter-list> ::= <parameter> [‘,’<parameter>]*

   <oper-property> ::= ‘redefines’ <oper-name>
       | ‘query’ | ‘ordered’ | ‘unordered’
       | ‘unique’ | ‘nonunique’
       | ‘seq’ | ‘sequence’
       | <oper-constraint>

* ``<return-type>`` は Operation に戻り Parameter が定義されている場合、その型。
* ``<oper-property>`` は Operation の特性を示す。

  * ``redefines <oper-name>`` は、``<oper-name>`` で識別される継承された
    Operation を再定義することを意味する。``<oper-name>`` は修飾してもよい。
  * ``query`` は Operation がシステムの状態を変化させないことを意味する。
  * ``<oper-constraint>`` には Operation に適用される制約を指定する。引数リスト
    は抑制してもよい。

----

   The TemplateParameters of a template Operation are in a list between the name
   of the Operation and the Parameters of the Operation.

.. code:: bnf

   [<visibility>] <name> ‘<‘ <template-parameter-list> ‘>’ ‘(‘ [<parameter-list>] ‘)’
       [‘:’ [<return-type>] [‘[‘ <multiplicity> ‘]’]
              [‘{‘ <oper-property> [‘,’ <oper-property>]* ‘}’]]

   The TemplateParameter bindings of a bound template Operation are in a list
   between the name of the Operation and the Parameters of the Operation.

.. code:: bnf

   [<visibility>] <name> ‘<<‘ <binding-expression-list> ‘>>’ ‘(‘ [<parameter-list>] ‘)’
       [‘:’ [<return-type>] [‘[‘ <multiplicity> ‘]’]
              [‘{‘ <oper-property> [‘,’ <oper-property>]* ‘}’]]

   <binding-expression-list> ::= <binding-expression> [‘,’ <binding-expression>]*

仮 TemplateParameters と TemplateParameter 束縛の記法では、Operation は
``<operation-name> '('<parameter-list> ')'`` と表記される。

OperationTemplateParameter の記法は TemplateParameter の記法を拡張したものだ：

.. code:: bnf

   <operation-template-parameter> ::= <parameter> [ ‘: Operation’] [‘=’ <default>]

   <parameter> ::= <operation-name> ‘(’ <parameter-list> ‘)’

   <default> ::= <operation-name ‘(’ <parameter-list> ‘)’

クラス図における例外やストリーミング Operation に対する Parameter は、特性文字列
に ``exception`` や ``stream`` というキーワードがある。

9.6.5 Examples
----------------------------------------------------------------------

通常 Operation の例：

.. code:: text

   display ()
   -hide ()
   +createWindow (location: Coordinates, container: Container [0..1]): Window
   +toString (): String

テンプレート操作の例：

.. code:: text

   f <T:Class>(x : T)

そのテンプレート Operation を束縛したもの：

.. code:: text

   f << T -> Window >>(x : Window)

ただし引数は抑制してよい。引数は束縛から計算される。

9.7 Generalization Sets
======================================================================

9.7.1 Summary
----------------------------------------------------------------------

   GeneralizationSet provides a way to group Generalizations into orthogonal
   dimensions. A GeneralizationSet may be associated with a Classifier called
   its powertype.

9.7.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 9.14 Generalization Sets

Figure 9.1 の一部を詳細にしたもの。

``A_generalizationSet_generalization``
  Generalization と GeneralizationSet の間の関連（両方向）。

  * Generalization がどの GeneralizationSet に所属するのかを示す。
  * 両関連端は多重度 ``*`` だ。

``A_powertypeExtent_powertype``
  Classifier と GeneralizationSet との間の関連（両方向）。

  * この関連が意味するのは、GeneralizationSet の各 Generalization に対して、特殊
    化 Classifier が ``powertype`` のオブジェクトに一意に関連している、というこ
    とだ。

    * すなわち ``powertype`` オブジェクトと対応する Classifiers が意味的に等価で
      あると扱われる。

9.7.3 Semantics
----------------------------------------------------------------------

Generalization をグループ化して、汎化の直交次元を表現することが許される。各グ
ループを表現するのが GeneralizationSet だ。

   The ``generalizationSet`` property designates the GeneralizationSets to which
   the Generalization belongs.

特定の GeneralizationSet に含まれる Generalization すべては、同じ一般 Classifier
を持つものとする。

GeneralizationSet の ``isCovering`` 特性は、その集合にある Generalizations の
特定の Classifiers が完全であるかどうかを次の意味で示す：

   if ``isCovering`` is true, then every instance of the general Classifier is
   an instance of (at least) one of the specific Classifiers.

特性 ``isDisjoint`` はそのセット内の Generalizations の特定の Classifiers が重な
り合ってもよいかどうかを次の意味で指定する：

   if isDisjoint is true, then no instance of any of the specific Classifiers
   may also be an instance of any other of the specific Classifiers.

どちらの特性も既定値は偽だ。

GeneralizationSet は任意で ``powertype`` と呼ばれる Classifier と関連付けてよ
い。

   This means that for every Generalization in the GeneralizationSet, the
   specializing Classifier is uniquely associated with an instance of the
   powertype,

べき乗型のオブジェクトと GeneralizationSet の特殊化との間には一対一対応があ
り、べき乗型のオブジェクトおよび対応する Classifiers は意味的に等価なものと
して扱うことが許される。

9.7.4 Notation
----------------------------------------------------------------------

Generalization 関係の線分に名前があるとき、その名前はその Generalization が所属
する GeneralizationSet を指定する。同一名を持つ Generalization 関係すべてが同一
の GeneralizationSet に属す。

   Figure 9.15 GeneralizationSets designated by name

Generalization の名前をいつもの矢印のラベルに記している。

   Figure 9.16 GeneralizationSets designated by shared target

以前にも見た shared target style による記法。見れば意味は汲める。

ここまでのいずれの表記方法でも、Generalization の矢印にラベルがない場合、モデル
内に GeneralizationSet が存在するかどうかを図から判断することは不可能だ。

   Figure 9.17 GeneralizationSet designated by dashed line spanning
   Generalization arrows

同じセットの一部であることを意味する別々の矢印のついた線に破線を引いて、
GeneralizationSet を指定することが許される。前の図と同様に、GeneralizationSet
は、各行が個別にラベル付けされるのではなく、単一の名前でラベル付けされている。ラ
ベルは省略することが許される。

* 破線を矢印群に交差させることで GeneralizationSet を示す。

   Table 9.1 GeneralizationSet constraints

``{complete, disjoint}``
   GeneralizationSet が網羅されており、その特定の Classifiers に共通のオブジェク
   トがないことを示す。
``{incomplete, disjoint}``
   GeneralizationSet が網羅されておらず、その特定の Classifiers に共通のオブジェ
   クトがないことを示す。
``{complete,overlapping}``
   GeneralizationSet が網羅されており、その特定の Classifiers が共通のオブジェク
   トを持つことを示す。
``{incomplete,overlapping}``
   GeneralizationSet が網羅されておらず、その特定の Clasifiers が共通のオブジェ
   クトを持つことを示す。

* 制約はどちらの順序で現れてもよい
* 既定値は ``{incomplete, overlapping}``
* 制約が一つしか表示されない場合、もう一つの制約がその既定値をとる。

図式的には、GeneralizationSet 制約は、Figure 9.18 に示すような一般的な矢印の表
記、または Figure 9.19 に示すような破線の表記のいずれであっても、集合の隣に配置
される。

   Figure 9.18 GeneralizationSet constraint notation with shared target style
   Figure 9.19 GeneralizationSet constraint notation with dashed line style

----

   Power type specification is indicated by placing the name of the powertype
   Classifier—preceded by a colon—next to the corresponding GeneralizationSet.

   Figure 9.20 Power type notation with shared target style

共有の鏃表記。

   Figure 9.21 Power type notation with dashed line style

破線表記の場合の表記。

9.7.5 Examples
----------------------------------------------------------------------

ここの見本が分かりやすいので、GeneralizationSet の概念を誤解しにくくなっている。

   Figure 9.22 GeneralizationSet notation options

抽象クラス ``Person`` が ``Woman`` および ``Man`` に特殊化されている。独立し
て、``Employee`` に特殊化されている。``Woman`` と ``Man`` への特殊化が
GeneralizationSet を一つ、Employee への特殊化が別の GeneralizationSet を構成して
いる。この見本はさまざまな記法を用いている。

抽象型 ``Person`` を異なる基準で特殊化していることがよくわかる。

   Figure 9.23 GeneralizationSets and constraints

男か女かにしか分類できないし、これらは互いに排他的な概念なので、ラベルに
``{complete, disjoint}`` と記してよい。

   Person is also specialized as Employee, and this single specialization is
   expressed as ``{incomplete}``, which means that a Person may either be an
   Employee or not.

この図から、Person は Man or Woman と Employee or not の組み合わせで四通りの選択
肢があると読める。

   Figure 9.24 Power type example

関係に注目して分析する：

* いちばん上の関係は «each Tree Species classifies zero or more instances of
  Tree, and each Tree is classified as exactly one Tree Species» であることを示
  す。
* Tree Species から垂直に伸びている二本の関係は «each Tree Species is identified
  with a Leaf Pattern and has a general location in any number of Geographic
  Locations» であることを示す。
* 直角に折れた関係は «each Tree has an actual location at a particular
  Geographic Location» であることを示す。

Tree のサブクラスはわかりやすい。

Tree GeneralizationSet の powertype は TreeSpecies のオブジェクトが Tree のサブ
クラスと一対一対応することを指定する。

   Figure 9.25 More power type examples

``powertype`` いろいろ。GeneralizationSet でコロンで始まる名前は ``powertype``
であることを示す。

* ``incomplete`` をラベルに含む継承は、それ以外のサブクラスの存在があってもよい
  ことを示す。
* ``:XXXX`` をラベルに含む継承は、サブクラスのどれもが XXXX 型オブジェクトと等価
  であることを示す。

   Figure 9.26 More than one powertype

部分型の集まりにラベルを付けることは、型に ``powertype`` が複数存在するときに
はますます重要になる。この図はそれを示す。

* Policy は Life, Health, Property/Casualty, またはその他の Insurance Line とし
  て分類されることがある。
* 同じ Policy は Policy Coverage Type が Group または Individual に分類されるこ
  とがある。

9.8 Instances
======================================================================

9.8.1 Summary
----------------------------------------------------------------------

   InstanceSpecifications represent instances of Classifiers in a modeled
   system. They are often used to model example configurations of instances.

オブジェクトの仕様だ。部分的に表現されたものであってもかまわない：

   They may be partial or complete representations of the instances that they
   correspond to.

9.8.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 9.27 Instances

InstanceSpecification, Slot, InstanceValue をやる。

``A_slot_owningInstance``
  InstanceSpecification から Slot への複合関連。

``A_classifier_instanceSpecification``
  InstanceSpecification から Classifier への関連（単方向）。
  InstanceSpecification のオブジェクトの種類として参照する。例えば
  ``classifier`` が

  * Class ならばその Class のオブジェクトの特徴を述べ、
  * Association ならばその Association のリンクの特徴を述べ、
  * 空ならば表現されているオブジェクトの種類を強制しない。

``A_definingFeature_slot``
  Slot から StructuralFeature への関連（単方向）。

``A_value_owningSlot``
  Slot から ValueSpecification への複合関連（単方向）。

  * 関連 ``A_ownedElement_owner`` を subsets する。
  * ``value`` は ``{ordered}`` だ。
  * ``value`` は型、多重度、等々において前述の ``definingFeature`` と適合する必
    要がある。

``A_specification_owningInstanceSpec``
  InstanceSpecification から ValueSpecification への複合関連（単方向）。

  * もし ``specification`` があれば、InstanceSpecification の値を与えるために
    ValueSpecification が評価される。
  * もし InstanceSpecification の参照する ``classifiers`` が一つ以上ある場合、
    ValueSpecification の型は少なくとも ``classifiers`` の一つには適合する必要が
    ある。

``A_instance_instanceValue``
  InstanceValue から InstanceSpecification への関連（単方向）。

  InstanceValue は参照する InstanceSpecification を所有しない。複数の
  InstanceValues が同じ InstanceSpecification を参照してもよい。

9.8.3 Semantics
----------------------------------------------------------------------

   An InstanceSpecification represents the possible or actual existence of
   instances in a modeled system and completely or partially describes those
   instances.

Slot 仕様：

   A Slot specifies that an instance modeled by an InstanceSpecification has a
   value or values for a specific StructuralFeature

この StructuralFeature は、直接属性、継承属性、汎化におけるプライベート属性、ま
たは分類子が Association である場合の ``memberEnd`` であって、再定義
StructuralFeature を除く、Slot を所有する InstanceSpecification の分類子に関連し
ているものでなければならない。

   The values in a Slot shall conform to the defining StructuralFeature of the
   Slot (in type, multiplicity, etc.).

Slot の値は ValueSpecification で指定する。

InstanceSpecification は次のものを表現してよい：

* 一つ以上の Classifiers によって分類されたオブジェクト。
* それの ``classifiers`` に基づくオブジェクトの種類。例えば、

  * ``classifier`` が Class である InstanceSpecification はその Class のオブジェ
    クトを記述し、
  * ``classifier`` が Association である InstanceSpecification はその
    Association のリンクを記述する。
  * ``classifier`` が指定されていない場合、InstanceSpecification は表現されるオ
    ブジェクトの種類を制約しない。
  * 異なる種類の ``classifiers`` が指定された場合、その意味は定義されない。

* オブジェクトの StructuralFeatures の値の仕様。値は Slots に格納される。

     Not all StructuralFeatures of all Classifiers of the InstanceSpecification
     need be represented by Slots, in which case the InstanceSpecification is a
     partial description.

* ValueSpecification による、オブジェクトを計算、導出、構築する方法についてのオ
  プショナルな仕様。

     If the InstanceSpecification has one or more ``classifiers``, then the type
     of the ValueSpecification must conform to at least one of those
     ``classifiers``.

..

   An InstanceSpecification may specify the actual existence of an instance in a
   modeled system. Or, an InstanceSpecification may provide an illustration or
   example of a possible instance in a modeled system.

オブジェクトは InstanceSpecification の ``classifier`` それぞれに適合
し、InstanceSpecification の各スロットで示される値を持つ特性を持つ。

   Having no ``slot`` in an InstanceSpecification for some properties does not
   mean that the represented instance does not have the property, but merely
   that the property is not of interest in the model.

同様に、実際のオブジェクトは InstanceSpecification のモデル化された分類子の特殊
化に適合するかもしれないが、この事実はモデルにおいて興味深いものではないかもしれ
ない。

InstanceSpecification はある時点におけるオブジェクト、スナップショットを表して
よい。

ここまでの記述からすると当たり前だが：

   It is important to keep in mind that InstanceSpecification is a model element
   and should not be confused with the instance that it is modeling. As an
   InstanceSpecification may only partially determine the properties of an
   instance, there may actually be multiple instances in the modeled system that
   satisfy the requirements of the InstanceSpecification.

InstanceValue 仕様：

   An InstanceValue is a kind of ValueSpecification whose value is specified
   using an InstanceSpecification.

InstanceValue の各評価は、InstanceSpecification に適合する個別のオブジェクトをも
たらすとみなされる。InstanceSpecification に ``specification`` がある場合、その
ValueSpecification は InstanceValueの値を与えるために評価される。そうでない場
合、InstanceValue は InstanceSpecification で特定された各分類子のオブジェクトであ
る値を作成することで評価される。それから：

   Any ``slots`` in the InstanceSpecification then provide values for the
   corresponding StructuralFeatures of the instance by evaluating the
   ValueSpecifications associated with those ``slots``.

``slot`` が与えられていない StructuralFeature は、それが ``defaultValue`` を持つ
Property であればそれを評価することで得られる値を持ち、そうでなければ値を持たな
い。

InstanceValue は、それが参照する InstanceSpecification を所有するのではなく、複
数の InstanceValue が同じ InstanceSpecification を参照することが許される。

9.8.4 Notation
----------------------------------------------------------------------

InstanceSpecification はその ``classifiers`` と似た記法を用いて描かれるが、
Classifier の名前が現れる代わりに、もしあればオブジェクト名、コロン、
Classifier の名前（たち）を連結し、下線を引く。

``classifier`` が Association である InstanceSpecification はリンクを表
現し、Association の同じ記法を用いて示すが、実線のパスは Classifiers ではなく
InstanceSpecifications を接続する。

オブジェクト仕様との接続からそれが Association ではなくリンクを表すことが明らか
な場合は、下線を引いた名前を表示する必要はない。

端子名は端子を修飾してもよい。回航矢印を表示してもよいが、表示する場合は
Association の端子の回航と一致させなければならない。

   NOTE. Names are optional for Classifiers and InstanceSpecifications. The
   absence of a name in a diagram does not necessarily reflect its absence in
   the underlying model.

無名 (unnamed) Classifier の匿名 (anonymous) InstanceSpecification 標準表記は下
線のついたコロンだ。

InstanceSpecification がその ``specification`` として ValueSpecification を持つ
場合、ValueSpecification は名前の後に等号 ``=`` を付けて表示するか、名前の下に等
号を付けずに表示する。

InstanceSpecification が名前を含む図形（矩形など）を用いて表示される場
合、ValueSpecification はその図形内に表示される。

   Slots are shown using similar notation to that of the corresponding
   StructuralFeatures.

StructuralFeature が区画内にテキストで示される場合、その Slot は
StructuralFeature 名または修飾名に等号 ``=`` と値指定が続くテキストで示してもよ
い。

   An InstanceValue may appear using textual or graphical notation. When
   textual, as may appear for the value of a Slot, the name of the
   InstanceSpecification is shown.

InstanceValue である Slot 値は代わりにリンクに似た図式的表記法を用いて示してよ
い。

StructuredClassifier により分類される InstanceSpecification では、その役目を果た
すオブジェクトを表す入れ子の矩形を含んでよい。このような入れ子
InstanceSpecificationの名前文字列の記法は次のとおり：

.. code:: bnf

   {<name> [‘/’ <rolename>] | ‘/’ <rolename>} [‘:’ <classifiername> [‘,’ <classifiername>]*]

InstanceSpecification の名前の後には、そのオブジェクトが果たす役割の名前が続くこ
とがある。オブジェクトが役割を果たす場合にのみ存在することが許される。

InstanceSpecification が Slot 値と役割を示す入れ子の矩形の両方を含む場合、それは
対応する StructuredClassifier の属性と内部構造区画に類する区画に分割される。

9.8.5 Examples
----------------------------------------------------------------------

   Figure 9.28 Specification of an Instance of String

String 型オブジェクト ``streetName`` の図式に見える。値が ``S. Crown Street`` で
あることを示している。

これが InstanceSpecification の記法の一つの見本となる。識別子の下にある引用符で
括られた文字列が値だ。

   Figure 9.29 Slots with values

Slots 付き InstanceSpecification の記法例。

Figure 9.30 InstanceSpecifications representing two objects connected by a link

リンク付き InstanceSpecifications の記法例。

   Figure 9.31 InstanceValue represented textually

InstanceValue の記法例。InstanceValue をテキスト表記で表される Slot の値として定
義する。Slot から参照して欲しいようだ。

   Figure 9.32 InstanceValue represented graphically

上記例題を関連の記法？で書き直したもの。

9.9 Classifier Descriptions
======================================================================

機械生成による節。

9.10 Association Descriptions
======================================================================

機械生成による節。

.. include:: /_include/uml-refs.txt
