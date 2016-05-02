======================================================================
10 Simple Classifiers
======================================================================
UML 2.5 pp. 165-180 に関するノート。

.. contents:: ノート目次

10.1 Summary
======================================================================
この章では複雑な内部構造でない Classifier 各種を詳細に記す。

10.2 DataTypes
======================================================================

10.2.1 Summary
----------------------------------------------------------------------
* DataType はそのオブジェクトたちが値にのみによって見分けのつくような Type である。

  * C/C++ 用語の POD に相当する概念と思われる。

10.2.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 10.1: DataType を中心に置いた図式。

  * 新登場の要素は DataType, PrimitiveType, Enumeration, EnumerationLiteral である。

10.2.3 Semantics
----------------------------------------------------------------------
DataType
  * 値ベースで扱える Classifier である。
  * もし DataType が attributes を持つならば、それは構造化されていると言う。

    * 構造化された DataType のオブジェクト同士が等しいとは、
      それらの構造と対応する attributes の値が等しいとき、かつそのときに限る。

PrimitiveType
  * あらかじめ定義されている DataType であり、どんな部分構造をも持たない。
  * PrimitiveType は代数が入っていてよい。その演算は UML の外部で定義される。
    実行時の PrimitiveType のオブジェクトは、数学的な要素に対応する値である。

Enumeration
  * DataType の一種。その各値がユーザー定義の EnumerationLiteral の一つに対応する。

EnumerationLiteral
  * Enumeration の要素を定義する InstanceSpecification である。
  * EnumerationLiteral に対応する値は不変 (immutable) であり、
    等価性を調べるための比較がなされてもよい。

A_ownedAttribute_datatype
  :doc:`./classification` Figure 9.10 で見た。

A_ownedOperation_datatype
  :doc:`./classification` Figure 9.13 で見た。

A_ownedLiteral_enumeration
  * Enumeration から EnumerationLiteral への composite 集約（両端ドット）。
  * A_ownedMember_namespace を subsets する関連。
  * ownedLiteral は ``{ordered}`` である。

A_classifier_enumerationLiteral
  * EnumerationLiteral から Enumeration への関連（単方向）。
  * A_classifier_instanceSpecification を redefines した関連。
  * EnumerationLiterals はその状態を変化することが許されないので、
    Enumeration の任意の属性は ``{readOnly}`` である必要がある。

10.2.4 Notation
----------------------------------------------------------------------
DataType
  * Classifier の記法を用いて、キーワード ``«dataType»`` と一緒に示す。

PrimitiveType
  * 同様にキーワード ``«primitive»`` と一緒に示す。

Enumeration
  * またしても同様にキーワード ``«enumeration»`` と一緒に示す。
  * EnumerationLiteral を一行当たり一個、列挙していく。

10.2.5 Examples
----------------------------------------------------------------------
* Figure 10.2: PrimitiveType Integer の記法例。区画なし。
* Figure 10.3: DataType 二種類の記法例。
* Figure 10.4: Enumeration VisibilityKind の記法例。これはどこかで見た覚えがある。

10.3 Signals
======================================================================

10.3.1 Summary
----------------------------------------------------------------------
Signal と Reception を定義する。
これらはオブジェクト同士の非同期通信をモデル化するのに用いられる。

10.3.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 10.5 は比較的小さな図式。

  * 概要通り Signal と Reception からなる関連図。

10.3.3 Semantics
----------------------------------------------------------------------
.. note::

   困ったことに respond, react, reply を日本語で表現すると同じ言葉になってしまう。
   辞書を当たると、これらの単語の意味合いが微妙に異なるようだ。

Signal
  * Classifier の一種。
  * 反応が受信者側で返信なしに非同期的に引き起こされる、オブジェクト間の通信の一種の詳細。

Reception
  * BehavioralFeature の一種。
  * ある Signal の受領に反応する支度の整った Class または Interface を指定する。

A_ownedAttribute_owningSignal
  * Signal から Property への composite 集約関連（単方向）。
  * A_attribute_classifier と A_ownedMember_namespace を subsets している。
  * 関連端 ownedAttribute は通信が伝送するデータを表現する。

    * 制約 ``{ordered}`` がある。

A_signal_reception
  * Reception から Signal への単方向関連。
  * Reception が Signal にマッチするのは、
    受信した Signal が signal の派生型である場合である。

10.3.4 Notation
----------------------------------------------------------------------
Signal
  * Classifier の記法を用いて、キーワード ``«signal»`` と一緒に示す。

Reception
  * Operation の記法を用いて、キーワード ``«signal»`` と一緒に示す。
    このキーワードは name の前に書くようだ。

10.3.5 Examples
----------------------------------------------------------------------
* Figure 10.6

  * IAlerm がふたつの Receptions を定義している。
  * ふたつの Signals の存在を定義している。
  * Reception の名前が Signal のそれにマッチしていることに注目。
    さらに、図では表現し切れていないが、
    パラメーターが Signal の属性にマッチすることにも注意。

10.4 Interfaces
======================================================================

10.4.1 Summary
----------------------------------------------------------------------
Interfaces は InterfaceRealizations を通じてその Interfaces を実装する
BehavioredClassifiers によって実装された、首尾一貫した (coherent) システムを宣言する。
変な日本語になった。

10.4.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 10.7

  * 概要で言及された Interface, InterfaceRealization, BehavioredClassifier を擁する図式。
  * 関連端の制約の記述に一部誤りがある。

10.4.3 Semantics
----------------------------------------------------------------------
Interface
  * 首尾一貫したシステムを共に構成する、
    public な Features の集合と責務を表現する Classifier である。

  * Interfaces はオブジェクト化されることは許されない。
    代わりに詳細を BehavioredClassifier が実装、実現する。

    * 一つの BehavioredClassifier が複数の Interfaces を実装してもよいし、
      複数の BehavioredClassifiers が一つの Interface を実装してもよい。

InterfaceRealization
  * BehavioredClassifier と Interface の間の Realization である。
    BehavioredClassifier は、Interface およびその親が所有する
    Features の集合を支える (support) ことで
    Interface が指定する契約に従う。

*BehavioredClassifier*
  * BehavioredClassifier が実現する Interfaces の集合のことをその provided Interfaces という。
  * BehavioredClassifier と対応する Interfaces との間の Usage が指定する Interfaces を required Interfaces という。

A_ownedAttribute_interface, A_ownedOperation_interface
  これらの関連は既に述べている。

A_ownedReception_interface
  * Interface から Reception への composite 関連（単方向ドット）。
  * A_feature_featuringClassifier と A_ownedMember_namespace を両方 subsets している。

A_nestedClassifier_interface
  * Interface から Classifier への composite 関連（単方向）。
  * Interface 内部で入れ子で定義されたすべての Classifiers への参照。特に説明なし。
  * A_ownedMember_namespace, A_redefinitionContext_redefinableElement を subsets する。

A_redefinedInterface_interface
  * Interface から Interface への関連（単方向）。
  * Interface が再定義するすべての Interfaces への参照。特に説明なし。
  * A_redefinedClassifier_classifier を subsets する。

A_protocol_interface
  * Interface から ProtocolStateMachine への composite 関連（単方向ドット）。
  * 関連端 protocol がもしあれば、
    それはイベント列と関連端 interface が述べる Operations と Receptions の事前・事後条件を指定する。

A_contract_interfaceRealization
  * InterfaceRealization から Interface への単方向関連。
  * その Interface を実現する Classifier のオブジェクトが果たさなければならない契約を表す。
  * 関連 A_supplier_supplierDependency を subsets している。
    図中の制約表示は誤りと思われる。

A_interfaceRealization_implementingClassifier
  * BehavioredClassifier から InterfaceRealization への composite 関連（両方向）。
  * この BehavioredClassifier が実装である Interfaces へ参照する InterfaceRealization の集合。
  * 関連 A_clientDependency_client とA_ownedElement_owner を subsets する。
    こちらも図中の制約表示は誤りと思われる。

A_ownedBehavior_behavioredClassifier
  * BehavioredClassifier から Behavior への composite 関連（単方向）。
  * BehavioredClassifier が Bahaviors を所有することを示す。
  * A_ownedMember_namespace を subsets する。

A_classifierBehavior_behavioredClassifier
  * BehavioredClassifier から Behavior への関連（単方向）。
  * BehavioredClassifier 自身の振る舞いを指定する Behavior である。
  * 上述の A_ownedBehavior_behavioredClassifier を redefines または subsets する。

10.4.4 Notation
----------------------------------------------------------------------
Interface
  * Classifier の記法を用いて、キーワード ``«interface»`` と一緒に示す。
  * ボールとかロリポップとかと呼ばれるラベル付きマルで示す。
    これをその Interface を実現する BehavioredClassifier に実線で結ぶ。

Usage
  * Classifier から Interface への依存だが、このときは Interface を半円、
    ソケットと呼ぶ形状で示す。

10.4.5 Examples
----------------------------------------------------------------------
* Figure 10.8

  * ISensor は ProximitySensor の provided Interface である。
  * このグラフは一つの InterfaceRealization を示していることになる。

* Figure 10.9

  * ISensor の前にキャレットが付いていることに注意。
  * CapacitiveSensor が ISensor を継承することを示している？

* Figure 10.10

  * ISensor とは書いていないが、
    このソケットが TheftAlerm の required Interface である。

* Figure 10.11

  * これまで出てきたイラストを別の表現にし、いくつか情報を加えたもの。
  * ISensor を長方形記法で表現。キーワード ``«interface»`` に注意。
  * InterfaceRealization を破線矢印で表現。矢頭は白三角である。
  * Usage を破線矢印で表現。キーワード ``«use»`` に注意。矢頭は開く。

* Figure 10.12

  * IAlerm と ISensor の間に 1:1 の関連が付いている。
    これが意味するところは、

    #. ISensor の任意の実装は属性 theAlarm を実現するのに必要な情報を維持する必要があり、
    #. また同様な必要が IAlerm と theSensor に対してある。

    本文中ではこれを mutually coupled と表現している。

  * IBuzzer は IAlarm の実装がアクセス可能でなければならない Interface の特徴を述べている。

10.5 Classifier Descriptions
======================================================================
機械生成による節。

10.6 Association Descriptions
======================================================================
機械生成による節。

.. include:: /_include/uml-refs.txt
