======================================================================
10 Simple Classifiers
======================================================================

.. contents::
   :depth: 2

10.1 Summary
======================================================================

   This clause specifies various kinds of Classifier that do not have complex
   internal structure.

10.2 DataTypes
======================================================================

10.2.1 Summary
----------------------------------------------------------------------

   DataTypes model Types whose instances are distinguished only by their value.

C/C++ 用語の POD に相当する概念と思われる。

10.2.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 10.1: DataTypes

DataType を中心に置いた図式。新登場の要素は DataType, PrimitiveType,
Enumeration, EnumerationLiteral だ。

``A_ownedAttribute_datatype``
  :doc:`./ch09-classification` Figure 9.10 で見た。

``A_ownedOperation_datatype``
  :doc:`./ch09-classification` Figure 9.13 で見た。

``A_ownedLiteral_enumeration``
  Enumeration から EnumerationLiteral への複合集約（双方向）。

  * ``A_ownedMember_namespace`` を subsets する関連。
  * ``ownedLiteral`` は ``{ordered}`` だ。

``A_classifier_enumerationLiteral``
  EnumerationLiteral から Enumeration への関連（単方向）。

  * ``A_classifier_instanceSpecification`` を redefines する。
  * EnumerationLiterals はその状態を変化することが許されないので、Enumeration の
    任意の属性は ``{readOnly}`` である必要がある。

10.2.3 Semantics
----------------------------------------------------------------------

10.2.3.1 DataTypes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A DataType is a kind of Classifier.

Class とは異なり、DataType のオブジェクトはその値によってしか識別されない。同じ
値である DataType のオブジェクトはすべて等しいとみなされる。

   If a DataType has ``attributes`` (i.e., Properties owned by it and in its
   namespace) it is called a :dfn:`structured` DataType.

構造化 DataType のオブジェクトはその ``attributes`` に合致する属性値を含む。構造
化 DataType のオブジェクト同士は、構造が同じで、対応する ``attributes`` の値が等
しいとき、かつそのときに限り等しいとみなされる。

   A DataType may be parameterized, bound, and used as TemplateParameters.

10.2.3.2 Primitive Types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A PrimitiveType defines a predefined DataType, without any substructure.

PrimitiveType には UML の外部で定義される代数や演算があってよい。 PrimitiveType
の実行時オブジェクトは UML の外側で定義された数学的要素に対応する値だ。

* 例えば Interger がそうだ。
* ここで言う代数というのは、代数的構造があるモデル程度の意味のほうに解釈したい。

10.2.3.3 Enumerations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Enumeration is a kind of DataType. Each value of an Enumeration corresponds
   to one of its user-defined EnumerationLiterals.

Classifier の特殊化として、Enumeration は汎化関係に関与することが許される。他の
それを特殊化する Enumeration は、汎化する Enumeration で定義されていない新しい
EnumerationLiterals を定義できる。この場合、適用できるリテラルは、継承されたリテ
ラルと局所で定義されたリテラルからなる。

   An EnumerationLiteral defines an element of the run-time extension of an
   Enumeration.

EnumerationLiteral に対応する値は不変 (immutable) であり、等価比較をすることが許
される。EnumerationLiteral はその存在中に変更することは許されないので、
Enumeration の属性はすべて読み取り専用でなければならない。

   An EnumerationLiteral has a name that shall be used to identify it within its
   Enumeration.

* EnumerationLiteral はその Enumeration 内でそれを識別するための名前を持つ。
* EnumerationLiteral の名前はその Enumeration 内が有効域となり、
* その Enumeration内で一意でなければならない。
* EnumerationLiteral の名前は一般的用途には修飾されて（指名される）ものとする。

10.2.4 Notation
----------------------------------------------------------------------

DataType はキーワード ``«dataType»`` を伴う Classifier の記法（矩形）で指定され、
属性などで参照される際には DataType の名前で指定される。

* 名前区画の下には属性一覧を示す区画が配置される。
* 属性一覧区画の下には Operation 区画が配置される。

..

   A PrimitiveType is similarly designated with the keyword ``«primitive»``
   above or before the name of the PrimitiveType.

   An Enumeration is similarly designated.

* Enumeration の名前は上部区画に置かれ、キーワード ``«enumeration»`` を名前の上
  または前に置かれる。
* EnumerationLiterals の一覧は操作区画の下にある ``literals`` という区画に、一行
  に一個ずつ列挙してよい。
* 属性区間と操作区画を抑制してもよく、典型的には空だ。

10.2.5 Examples
----------------------------------------------------------------------

   Figure 10.2 PrimitiveType Notation

PrimitiveType Integer の記法例。区画なし。

   Figure 10.3 DataType Notation

DataType 二種類の記法例。やはり POD 構造体を指向した概念だと思って良さそうだ。
Person のある属性の型 FullName の仕様が左側のボックスだ。

   Figure 10.4 Enumeration Notation

Enumeration VisibilityKind の記法例。これは :doc:`./ch07-common-structure` で見
た覚えがある。

10.3 Signals
======================================================================

10.3.1 Summary
----------------------------------------------------------------------

非同期処理要素を二つ扱う。

   Signals and Receptions are used to model asynchronous communication between
   objects.

10.3.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 10.5 Signals

比較的小さな図式。概要にある通り Signal と Reception からなる関連図。

``A_ownedAttribute_owningSignal``
  Signal から Property への複合関連（単方向）。

  * ``A_attribute_classifier`` と ``A_ownedMember_namespace`` を subsets する。
  * 関連端 ``ownedAttribute`` は通信が伝送するデータを表現する。

    * 制約 ``{ordered}`` がある。

``A_signal_reception``
  Reception から Signal への関連（単方向）。

  * Reception が Signal にマッチするのは、受信した Signal が ``signal`` の特殊化
    である場合だ。

10.3.3 Semantics
----------------------------------------------------------------------

10.3.3.1 Signals
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A Signal is a specification of a kind of communication between objects in
   which a reaction is asynchronously triggered in the receiver without a reply.

受信側のオブジェクトは 13.3 節に規定されるとおりに Signal を処理する。

通信データは Signal の ``attributes`` として表現される。

Signal はそれを処理する Classifiers とは独立して定義される。

   The sender of a Signal will not block waiting for a reply but continue
   execution immediately.

Classifier はある Signal に関連する Reception を宣言することで、そのオブジェクト
がその Signal またはその部分型を受信し、指定された Behavior で応答することを指定
する。

   A Signal may be parameterized, bound, and used as TemplateParameters.

10.3.3.2 Receptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A Reception specifies that its owning Class or Interface is prepared to react
   to the receipt of a Signal.

受信した Signal が Reception の ``signal`` を特殊化したものである場合、Reception
は Signal に合致する。

オブジェクトが受信した Signal にどのように反応するかの詳細は、Reception に関連す
る Behavior の種類と、その所有する Classifier や Interface に依存する。
:doc:`./ch13-common-behavior` でやる予定。

Reception の名前は Signal の名前と同じだ。

Reception には Signal の属性が名前、型、多重度において合致する入力 Parameters を
持つことしか許されない。

10.3.4 Notation
----------------------------------------------------------------------

Signal はキーワード ``«signal»`` の付いた Classifier 記号で描かれる。

Reception はキーワード ``«signal»`` を用いた、Operation を表すのと同じ記法で受信
区画に表現される。

10.3.5 Examples
----------------------------------------------------------------------

   Figure 10.6 Reception Notation

``IAlerm`` は二つの Receptions を定義した Interface であって、同じ図式内に
Signals も二つ定義している。

Reception の名前が Signal のそれに合致していることに注目。さらに、図では表現し切
れていないが、引数が Signal の属性に合致することにも注意。

10.4 Interfaces
======================================================================

10.4.1 Summary
----------------------------------------------------------------------

   Interfaces declare coherent services that are implemented by
   BehavioredClassifiers that implement the Interfaces via InterfaceRealizations.

訳しにくい。

10.4.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 10.7 Interfaces

概要で言及された Interface, InterfaceRealization, BehavioredClassifier を擁する
図式。関連端の制約の記述に一部誤りがある。

``A_ownedAttribute_interface``, ``A_ownedOperation_interface``
  これらの関連は既に述べている。

``A_ownedReception_interface``
  Interface から Reception への複合関連（単方向）。

  * ``A_feature_featuringClassifier`` と ``A_ownedMember_namespace`` を両方
    subsets する。

``A_nestedClassifier_interface``
  Interface から Classifier への複合関連（単方向）。

  * Interface 内部で入れ子で定義されたすべての Classifiers への参照。特に説明な
    し。
  * ``A_ownedMember_namespace``, ``A_redefinitionContext_redefinableElement`` を
    subsets する。

``A_redefinedInterface_interface``
  Interface から Interface への関連（単方向）。

  * Interface が再定義するすべての Interfaces への参照。特に説明なし。
  * ``A_redefinedClassifier_classifier`` を subsets する。

``A_protocol_interface``
  Interface から ProtocolStateMachine への複合関連（単方向）。

  * 関連端 ``protocol`` がもしあれば、それはイベント列と関連端 ``interface`` が
    述べる Operations と Receptions の事前・事後条件を指定する。

``A_contract_interfaceRealization``
  InterfaceRealization から Interface への関連（単方向）。

  * その Interface を実現する Classifier のオブジェクトが果たさなければならない
    契約を表す。
  * 関連 ``A_supplier_supplierDependency`` を subsets している。図中の制約表示は
    誤りと思われる。

``A_interfaceRealization_implementingClassifier``
  BehavioredClassifier から InterfaceRealization への複合関連（双方向）。

  * この BehavioredClassifier が実装である Interfaces へ参照する
    InterfaceRealization の集合。
  * 関連 ``A_clientDependency_client`` と ``A_ownedElement_owner`` を subsets す
    る。こちらも図中の制約表示は誤りと思われる。

``A_ownedBehavior_behavioredClassifier``
  BehavioredClassifier から Behavior への複合関連（単方向）。

  * BehavioredClassifier が Behaviors を所有することを示す。
  * ``A_ownedMember_namespace`` を subsets する。

  ``A_classifierBehavior_behavioredClassifier``
    BehavioredClassifier から Behavior への関連（単方向）。

    * BehavioredClassifier 自身の挙動を指定する Behavior だ。
    * 上述の ``A_ownedBehavior_behavioredClassifier`` を redefines または
      subsets する。

10.4.3 Semantics
----------------------------------------------------------------------

10.4.3.1 Interfaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   An Interface is a kind of Classifier that represents a declaration of a set
   of public Features and obligations that together constitute a coherent
   service.

Interface は契約を指定する。Interface を実現する Classifier のオブジェクトは、
その契約を履行するものとする。

Interface に関連する義務は、制約（事前条件や事後条件など）または儀礼 (protocol)
仕様の形をしており、Interface を介した相互作用に命令の制限を課すことが許される。

   Interfaces may not be instantiated. Instead, an Interface specification is
   *implemented* or *realized* by a BehavioredClassifier

これは、BehavioredClassifier が Interface の仕様に適合する公開正面を設置すること
を意味する。

   NOTE. A given BehavioredClassifier may implement more than one Interface and
   that an Interface may be implemented by a number of different
   BehavioredClassifiers.

Interface と BehavioredClassifier の対応は一対一対応にならないほうが普通。

   Interfaces provide a way to partition and characterize groups of public
   Features and obligations that realizing BehavioredClassifiers shall possess.

Interface は実装方法を特定するものではなく、単に BehavioredClassifiers を実現す
るために必要なものを特定するものだ。BehavioredClassifiers は Interface に準拠し
た ``attributes``, Operation, 外部から観測可能な Behavior からなる公開正面を設置
するものとする。

* Interface が ``attribute`` を宣言する場合、必ずしも実現 BehavioredClassifier
  に本当にそれらが存在するという意味ではない。外側の観測者に対してはそのように見
  えるということに過ぎない。

次に provided/required Interface という術語が（初めて？）述べられる：

   The set of Interfaces realized by a BehavioredClassifier are its *provided*
   Interfaces, which represent the services and obligations that instances of
   that BehavioredClassifier offer to their clients. Interfaces may also be used
   to specify *required* Interfaces, which are specified by a Usage dependency
   between the BehavioredClassifier and the corresponding Interfaces.

必須 Interfaces は BehavioredClassifier がその機能を発揮し、利用側に対する自らの
義務を果たすために必要なサービスを規定する。

   Properties owned by Interfaces (including Association ends) imply that the
   realizing BehavioredClassifier should maintain information corresponding to
   the type and multiplicity of the Property and facilitate retrieval and
   modification of that information.

例によって、Interface 上で宣言された Property は、実現する BehavioredClassifier
上にそのような Property が存在することを必ずしも意味しない（例えば、同等の get
および set 操作）。

ProtocolStateMachine に関する記述：

   Interfaces may own a ProtocolStateMachine that specifies event sequences and
   pre/post conditions for the Operations and Receptions described by the
   Interface. A BehavioredClassifier realizing an Interface shall comply with
   the ProtocolStateMachine owned by the Interface.

Interface は引数化したり、束縛したり、TemplateParameters として用いてよい。

   An InterfaceRealization relationship between a BehavioredClassifier and an
   Interface implies that the BehavioredClassifier conforms to the contract
   specified by the Interface by supporting the set of Features owned by the
   Interface, and any of its parent Interfaces.

* BehavioralFeatures については、実現する BehavioredClassifier は Interface が定
  義する Operation または Reception ごとに Operation または Reception をそれぞれ
  持つことになる。
* Property については、実現する BehavioredClassifier は Property によって表現さ
  れる状態を維持する機能を備えることになる。

実現する BehavioredClassifier の Property に直接写像してもよいが、
BehavioredClassifier の StateMachine や、状態情報の取得を支援する Operation と状
態情報を変更する Operation のペアで支援してもよい。

10.4.4 Notation
----------------------------------------------------------------------

   An Interface may be designated using the default notation for Classifier (see
   9.2.4) with the keyword ``«interface»``.

特定の特別な依存関係は次の記法も許される：

   Alternatively an InterfaceRealization dependency from a BehavioredClassifier
   to an Interface may be shown by representing the Interface by a circle or
   *ball*, often also called *lollipop*, labeled with the name of the Interface,
   attached by a solid line to the BehavioredClassifier that realizes this
   Interface.

Usage にはソケットという記法を用いる：

   The Usage dependency from a Classifier to an Interface is shown by
   representing the Interface by a half-circle or *socket*, labeled with the
   name of the Interface, attached by a solid line to the Classifier that
   requires this Interface.

BehavioredClassifier の一般化を継承した Interface は、ロリポップで図示することが
許される。これらの Interface はそ名前の前にキャレット記号 ``^`` を付けて図示され
る。

ソケットとロリポップを使って表現された Usage から InterfaceRealization に
Dependency が配線されている場合、両者を結ぶ依存関係矢印を表示してもよい。

10.4.5 Examples
----------------------------------------------------------------------

   Figure 10.8 ISensor is a provided Interface of ProximitySensor

``ProximitySensor`` から ``ISensor`` への InterfaceRealization がボール（ロ
リポップ）記法を使って示されている。

``ISensor`` は ``ProximitySensor`` の provided Interface だ。

   Figure 10.9 ISensor, a provided Interface of ProximitySensor, (...)

継承された provided Interface に対するロリポップ記法だ。

* ``ISensor`` の前にキャレット ``^`` が付いていることに注意。
* ``CapacitiveSensor`` が ``ISensor`` を継承することを示している？

   Figure 10.10 ISensor is a required Interface of TheftAlarm

``TheftAlarm`` から ``ISensor`` への Usage 依存をソケット記法を使って示してい
る。

``ISensor`` とは書いていない（書き忘れだろう）が、このソケットが ``TheftAlerm``
の required Interface だ。

   Figure 10.11 Alternative notation for required and provided Interface

これまで出てきたイラストを矩形記法で表現したもの。情報が増えている。

* ``ISensor`` を長方形記法で表現。キーワード ``«interface»`` に注意。
* InterfaceRealization を破線矢印で表現。鏃は白三角だ。
* Usage を破線矢印で表現。キーワード ``«use»`` に注意。鏃は開く。

二つ以上の Interfaces がアプリケーション固有の依存関係を通じて相互結合される事例
が実際にはよくある。そういう状況では、Interface それぞれは多者間の通信規約におけ
る特定の役割を果たす。次の例がそれを示す。

   Figure 10.12 A set of collaborating Interfaces

``IAlerm`` と ``ISensor`` の間に双方向の規約関連が付いている。

* ``ISensor`` のどんな実装も ``theAlarm`` 特性を実現するのに必要な情報を保持しな
  ければならず、
* ``IAlerm`` と ``theSensor`` ついても同様だ。

``IBuzzer`` は ``IAlarm`` の実装がアクセス可能でなければならない Interface を記
述している。

10.5 Classifier Descriptions
======================================================================

機械生成による節。

10.6 Association Descriptions
======================================================================

機械生成による節。

.. include:: /_include/uml-refs.txt
