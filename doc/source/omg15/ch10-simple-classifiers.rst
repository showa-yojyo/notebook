======================================================================
10 Simple Classifiers
======================================================================

.. admonition:: 読者ノート

   現在ノート修正中。

.. contents::
   :depth: 2

10.1 Summary
======================================================================

* この章では複雑な内部構造でない Classifier 各種を詳細に記す。

10.2 DataTypes
======================================================================

10.2.1 Summary
----------------------------------------------------------------------

* DataTypes はオブジェクトたちが値によってしか区別されない Types をモデル化する。

  * C/C++ 用語の POD に相当する概念と思われる。

10.2.2 Abstract Syntax
----------------------------------------------------------------------

* Figure 10.1: DataTypes

  * DataType を中心に置いた図式。
  * 新登場の要素は DataType, PrimitiveType, Enumeration, EnumerationLiteral であ
    る。

``A_ownedAttribute_datatype``
  :doc:`./ch09-classification` Figure 9.10 で見た。

``A_ownedOperation_datatype``
  :doc:`./ch09-classification` Figure 9.13 で見た。

``A_ownedLiteral_enumeration``
  * Enumeration から EnumerationLiteral への composite 集約（両方向）。
  * ``A_ownedMember_namespace`` を subsets する関連。
  * ``ownedLiteral`` は ``{ordered}`` である。

``A_classifier_enumerationLiteral``
  * EnumerationLiteral から Enumeration への関連（単方向）。
  * ``A_classifier_instanceSpecification`` を redefines する。
  * EnumerationLiterals はその状態を変化することが許されないので、Enumeration の
    任意の属性は ``{readOnly}`` である必要がある。

10.2.3 Semantics
----------------------------------------------------------------------

10.2.3.1 DataTypes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* DataType とは Classifier の一種である。 DataType は Class とは値によってしか識
  別されないという点が異なる。
* DataType に ``attributes`` があるならば、それは構造化された DataType と呼ばれ
  る。

  * 構造化された DataType のオブジェクト同士は、それらの構造と対応する
    ``attributes`` の値が等しいとき、かつそのときに限り等しいとみなされる。

* DataType は引数化したり、束縛したり、TemplateParameters として用いてよい。

10.2.3.2 Primitive Types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* PrimitiveType はあらかじめ定義されている DataType であり、どんな部分構造もな
  い。

  * PrimitiveType には代数があってよく、演算は UML の外部で定義される。実行時の
    PrimitiveType のオブジェクトは、UML の外側で定義された数学的な要素に対応する
    値である。

    * 例えば Intergers がそうである。
    * ここで言う代数というのは、数学の一研究分野というよりは、代数的構造があるモ
      デル程度の意味のほうに解釈したい。

10.2.3.3 Enumerations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Enumeration は DataType の一種である。 Enumeration の値それぞれがそれのユー
  ザー定義の一つに対応する。
* Enumeration は Classifier の specialization なので、一般化関係に関与することが
  可能である。

  * 特殊化された Enumeration には、新しい EnumerationLiteral を定義してよい。

* EnumerationLiteral は Enumeration の実行時拡張の要素を定義する。

  * EnumerationLiteral に対応する値は不変 (immutable) であり、等価性を調べるため
    に比較してもよい。

* EnumerationLiteral にはその内部で識別するのに用いられる必要がある名前がある。

  * EnumerationLiteral の名前は一般用途のために限定される (be qualified) ものと
    する。

10.2.4 Notation
----------------------------------------------------------------------

* DataType は Classifier の記法（矩形）を用いて、キーワード ``«dataType»`` と一
  緒に指名するか、それが参照される際に DataType の名前で指名する。
* PrimitiveType はキーワード ``«primitive»`` を PrimitiveType の名前の上または後
  ろに記して同様に指名する。
* Enumeration も同様に指名する。Enumeration の名前をキーワード ``«enumeration»``
  を名前の上または後ろに記した区画の上部に置く。

  * EnumerationLiterals のリストは、操作区画の下にある ``literals`` と名付けられ
    た区画に、一行当たり一個を列挙してよい。

10.2.5 Examples
----------------------------------------------------------------------

* Figure 10.2 PrimitiveType Notation

  * PrimitiveType Integer の記法例。区画なし。

* Figure 10.3 DataType Notation

  * DataType 二種類の記法例。
  * Person のある属性の型 FullName の仕様が左側のボックスである。

* Figure 10.4 Enumeration Notation

  * Enumeration VisibilityKind の記法例。
    これは :doc:`./ch07-common-structure` で見た覚えがある。

10.3 Signals
======================================================================

10.3.1 Summary
----------------------------------------------------------------------

* Signals と Receptions はオブジェクト同士の非同期通信をモデル化するのに用いられ
  る。

10.3.2 Abstract Syntax
----------------------------------------------------------------------

* Figure 10.5 Signals

  * 比較的小さな図式。
  * 概要にある通り Signal と Reception からなる関連図。

``A_ownedAttribute_owningSignal``
  * Signal から Property への composite 関連（単方向）。
  * ``A_attribute_classifier`` と ``A_ownedMember_namespace`` を subsets する。
  * 関連端 ``ownedAttribute`` は通信が伝送するデータを表現する。

    * 制約 ``{ordered}`` がある。

``A_signal_reception``
  * Reception から Signal への関連（単方向）。
  * Reception が Signal にマッチするのは、
    受信した Signal が ``signal`` の特殊化である場合である。

10.3.3 Semantics
----------------------------------------------------------------------

10.3.3.1 Signals
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Signal とは、反応が返信なしに受信者側で非同期的に引き起こされるオブジェクト間
  の通信の一種の詳細である。

  * Signal はそれを処理する Classifiers とは独立して定義される。

* Signal の送信者は応答を待機することをブロックしようとはせずに、即時に実行を継
  続する。

  * 与えられた Signal に結びついた Reception を宣言することで、Classifier はその
    オブジェクト（複数形）はその Signal あるいはその派生型を受信する能力のあると
    いうことを指定し、指名された Behavior を使ってそれに対して反応するものであ
    る。

* Signal は引数化したり、束縛したり、TemplateParameters として用いてよい。

10.3.3.2 Receptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Reception は、所有する Class または Interface が Signal の受領に反応する支度を
  整っていることを指定する。

  * オブジェクトが受信した Signal にどのように応じるかの詳細は、Reception に関連
    づいたと Behavior の種類と、所有する Classifier や Interface に依る。
    :doc:`./ch13-common-behavior` でやる予定。

  * Reception の名前は Signal の名前と同じである。
  * Reception には Signal の属性が名前、型、多重度においてマッチする入力
    Parameters だけがあることが許される。

10.3.4 Notation
----------------------------------------------------------------------

* Signal はキーワード ``«signal»`` の付いた Classifier の記号で描かれる。
* Reception はキーワード ``«signal»`` を用いて、Operations を表すのと同じ表記法
  を使って、受領区画に示される。

10.3.5 Examples
----------------------------------------------------------------------

* Figure 10.6

  * ``IAlerm`` が二つの Receptions を定義している。
  * 二つの Signals の存在を定義している。
  * Reception の名前が Signal のそれにマッチしていることに注目。さらに、図では表
    現し切れていないが、パラメーターが Signal の属性にマッチすることにも注意。

10.4 Interfaces
======================================================================

10.4.1 Summary
----------------------------------------------------------------------

* Interfaces は InterfaceRealizations を通じて Interfaces を実装する
  BehavioredClassifiers で実装された首尾一貫した (coherent) サービスを宣言する。

10.4.2 Abstract Syntax
----------------------------------------------------------------------

* Figure 10.7

  * 概要で言及された Interface, InterfaceRealization, BehavioredClassifier を擁
    する図式。
  * 関連端の制約の記述に一部誤りがある。

``A_ownedAttribute_interface``, ``A_ownedOperation_interface``
  これらの関連は既に述べている。

``A_ownedReception_interface``
  * Interface から Reception への composite 関連（単方向）。
  * ``A_feature_featuringClassifier`` と ``A_ownedMember_namespace`` を両方
    subsets する。

``A_nestedClassifier_interface``
  * Interface から Classifier への composite 関連（単方向）。
  * Interface 内部で入れ子で定義されたすべての Classifiers への参照。特に説明な
    し。
  * ``A_ownedMember_namespace``, ``A_redefinitionContext_redefinableElement`` を
    subsets する。

``A_redefinedInterface_interface``
  * Interface から Interface への関連（単方向）。
  * Interface が再定義するすべての Interfaces への参照。特に説明なし。
  * ``A_redefinedClassifier_classifier`` を subsets する。

``A_protocol_interface``
  * Interface から ProtocolStateMachine への composite 関連（単方向）。
  * 関連端 ``protocol`` がもしあれば、それはイベント列と関連端 ``interface`` が
    述べる Operations と Receptions の事前・事後条件を指定する。

``A_contract_interfaceRealization``
  * InterfaceRealization から Interface への関連（単方向）。
  * その Interface を実現する Classifier のオブジェクトが果たさなければならない
    契約を表す。
  * 関連 ``A_supplier_supplierDependency`` を subsets している。図中の制約表示は
    誤りと思われる。

``A_interfaceRealization_implementingClassifier``
  * BehavioredClassifier から InterfaceRealization への composite 関連（両方
    向）。
  * この BehavioredClassifier が実装である Interfaces へ参照する
    InterfaceRealization の集合。
  * 関連 ``A_clientDependency_client`` と ``A_ownedElement_owner`` を subsets す
    る。こちらも図中の制約表示は誤りと思われる。

``A_ownedBehavior_behavioredClassifier``
  * BehavioredClassifier から Behavior への composite 関連（単方向）。
  * BehavioredClassifier が Behaviors を所有することを示す。
  * ``A_ownedMember_namespace`` を subsets する。

  ``A_classifierBehavior_behavioredClassifier``
    * BehavioredClassifier から Behavior への関連（単方向）。
    * BehavioredClassifier 自身の挙動を指定する Behavior である。
    * 上述の ``A_ownedBehavior_behavioredClassifier`` を redefines または
      subsets する。

10.4.3 Semantics
----------------------------------------------------------------------

10.4.3.1 Interfaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Interface とは、公開 Features の集合と、一体となって首尾一貫したサービスを構成
  する責務の宣言を表現する Classifier の一種である。
* Interfaces はオブジェクト化されることは許されない。代わりに Interface 仕様は
  BehavioredClassifier によって実装または実現される。このことは、
  BehavioredClassifier は Interface の仕様に適合する公開の facade を表現すること
  を意味する。

  * 与えられた BehavioredClassifier が複数の Interfaces を実装してもよいし、
    Interface が異なる BehavioredClassifiers のいくつかにより実装されてもよい。

* Interfaces は実現している BehavioredClassifiers が支配 (possess) するものとす
  る公開 Features と責務のグループ（複数形）を、仕切ったり特徴付ける手段を与える。

  * Interface が ``attribute`` を宣言するならば、これは必ずしも実現する
    BehavioredClassifier にその実装でそういう ``attribute`` が必ずあるということ
    を意味しないで、外側の観測者に対してはそのように現れるということにしか過ぎな
    い。

* BehavioredClassifier により実現される Interfaces の集合はそれの ``provided``
  Interfaces であり、それはその BehavioredClassifier のオブジェクトがクライアン
  トに提供するサービスと責務を表現する。Interfaces は ``required`` Interfaces を
  指定するのにも用いてよく、BehavioredClassifier と対応する Interfaces との間の
  Usage 依存により指定される。
* Interfaces により所有される Properties は、実現する BehavioredClassifier が型
  と Property の多重度の情報を維持し、その情報の取得及び修正を促進するべきである
  ことを暗に示す。
* Interfaces は、事象列、Operations に関する事前・事後条件、Interface により記述
  される Receptions を指定する ProtocolStateMachine を所有してよい。
* Interface は引数化したり、束縛したり、TemplateParameters として用いてよい。
* BehavioredClassifier と Interface の間の InterfaceRealization 関係は、
  Interface およびその親 Interfaces の任意のものにより所有される Features の集合
  を支援することで、BehavioredClassifier が Interface により指定される契約に適
  合することを暗に示す。

10.4.4 Notation
----------------------------------------------------------------------

* Interface は Classifier の既定の記法をキーワード ``«interface»`` と共に使って
  指名してよい。
* 代わりとして、BehavioredClassifier から Interface への InterfaceRealization 依
  存では、Interface の名前でラベルが付けられ、この Interface を実現する
  BehavioredClassifier への実線で取り付けられた、円つまりボール、しばしばロリ
  ポップとも呼ばれるものにより Interface を表現することにより示してよい。
* Classifier から Interface への Usage 依存は、Interface の名前でラベルが付けら
  れ、この Interface を要求する Classifier への実線で取り付けられた、半円つまり
  ソケットでInterface を表現することにより示してよい。
* BehavioredClassifier の一般化を継承した Interfaces は、図式ではロリポップを通
  して記してよい。これらの Interfaces は図式ではキャレット記号が Interface の名
  前の前に来ることで示される。
* Dependency がソケットとロリポップを使って表現されている Usage から
  InterfaceRealization へ配線されていれば、依存矢印はソケットをロリポップへ接合
  して示してよい。

10.4.5 Examples
----------------------------------------------------------------------

* Figure 10.8 ISensor is a provided Interface of ProximitySensor

  * ``ProximitySensor`` から ``ISensor`` への InterfaceRealization がボール（ロ
    リポップ）表記法を使って示されている。
  * ``ISensor`` は ``ProximitySensor`` の ``provided`` Interface である。

* Figure 10.9 ISensor, a provided Interface of ProximitySensor, (...)

  * 継承された ``provided`` Interface に対するロリポップ表記法。
  * ``ISensor`` の前にキャレットが付いていることに注意。
  * ``CapacitiveSensor`` が ``ISensor`` を継承することを示している？

* Figure 10.10 ISensor is a required Interface of TheftAlarm

  * ``TheftAlarm`` から ``ISensor`` への Usage 依存をソケット表記法を使って示し
    ている。
  * ``ISensor`` とは書いていない（書き忘れだろう）が、このソケットが
    ``TheftAlerm`` の ``required`` Interface である。

* Figure 10.11 Alternative notation for required and provided Interface

  * これまで出てきたイラストを別の表現にし、いくつか情報を加えたもの。
  * ``ISensor`` を長方形記法で表現。キーワード ``«interface»`` に注意。
  * InterfaceRealization を破線矢印で表現。矢頭は白三角である。
  * Usage を破線矢印で表現。キーワード ``«use»`` に注意。矢頭は開く。

* 二つまたはそれを超える Interfaces がアプリケーション固有の依存を通じて相互に
  結合する事例が実際にはよくある。そういう状況では、Interface のそれぞれは多者間
  の通信規約で特有の役目を表現する。

* Figure 10.12 A set of collaborating Interfaces

  * ``IAlerm`` と ``ISensor`` の間に一対一の関連が付いている。これが意味するとこ
    ろは、

    #. ``ISensor`` のどんな実装も ``theAlarm`` 特性を実現するのに
       必要な情報を維持しなければならず、
    #. ``IAlerm`` と ``theSensor`` ついても同様である。

  * ``IBuzzer`` は ``IAlarm`` の実装がアクセス可能でなければならない Interface
    の特徴を述べている。

10.5 Classifier Descriptions
======================================================================

機械生成による節。

10.6 Association Descriptions
======================================================================

機械生成による節。

.. include:: /_include/uml-refs.txt
