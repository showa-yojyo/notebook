======================================================================
20 InformationFlows
======================================================================
UML 2.5 pp. 667-674 に関するノート。

.. todo:: 最低でもあと一回は編集する。

.. contents:: ノート目次
   :depth: 2

20.1 Information Flows
======================================================================
20.1.1 Summary
----------------------------------------------------------------------
* InformationFlows パッケージはシステム実体の間の情報の交換を
  高水準の抽象度で支援する。

* InformationFlows は
  システムを通じて情報の回覧を一般的な手法で記述する。

  * 同様に InformationItems は
    実現化の詳細が設計される前でさえ、
    InformationFlows に沿って流れる情報を表現するのに用いられる。

* InformationFlows パッケージの中身は Figure 20.1 で示す。

20.1.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 20.1 Information Flows

  * InformationFlow は PackageableElement と DirectedRelationship の
    特殊化である。

    * 関連する型がかなり多くある。

      * Classifier (conveyed)
      * Relationship (realization)
      * NamedElement (informationSource, informationTarget)
      * Connector (realizingConnector)
      * ActivityEdge (realizingActivityEdge)
      * Message (realizingMessage)

  * InformationItem は Classifier の特殊化である。

    * InformationItem は InformationItem (represented) に関連する。

20.1.3 Semantics
----------------------------------------------------------------------
* InformationFlows は情報品目の一方通行なある種の情報経路を必要とする。

* InformationFlow の sources と targets は
  伝達された InformationItems や Classifiers を
  送信 (sources) または受信 (targets) することが
  可能なオブジェクトの集合を指定する。

* InformationFlow の sources と targets は
  それらの型であるか、
  それらによって含まれている（＝所有されている）かの
  可能性のあるオブジェクトのすべてを代表する。

  * 例えばもし source または target が Classifier ならば、
    それは Classifier の潜在的オブジェクトすべてを代表する。

* 情報経路は
  sources と targets の本質に付随したさまざまな方法により
  実現化されることが可能である。

  * Relationships, Connectors, ActivityEdges, Messages によって
    実現化されることが可能である。

* 典型的には InformationFlows は
  sources から targets に流れる InformationItems を見分けるのだが、
  Class などの具象 Classifiers もまた伝達されることが許される。

* InformationItems は
  sources から targets に流れることが可能な
  たくさんの種類の情報を
  たいへん抽象的なやり方で表現する。

* InformationItems の重要な用途に
  早い設計段階の間、
  おそらくは最終的にそれらを定義するような詳細な
  モデリングの決定がなされるよりも
  以前において、情報を表現するというものがある。

* InformationItems はより明確な InformationItems や
  Classifiers へと分解されてよい。

* InformationItems は Classes の全種類、Interfaces, Signals
  そして他の InformationItems によって実現化されることしか認められない。

* InformationFlows の主要なゴールは
  情報がモデルのある領域から別の領域へ移動することを伝達することである。

20.1.4 Notation
----------------------------------------------------------------------
* InformationFlow は Dependency と同じ表記法を用いて表現されるが、
  キーワード ``«flow»`` を破線に添えておく。

* InformationItems の表現はそれらが表示される周辺状況により決定される。

  * InformationFlow の ``«flow»`` 破線に付属するときには、
    InformationItem の名前が適切な線の近くに表示される。

  * InformationFlows と独立して表示されるときには、
    InformationItems はそれらが Classifiers であるゆえ、
    矩形内部の名前として表現されてよい。
    矩形にはキーワード ``«information»`` か
    黒塗りの二等辺三角形を付ける。

  * InformationFlow の情報経路の実現化に付属するときには、
    情報経路上の黒塗りの二等辺三角形が情報の流れの方向を指示する。

  * InformationItem が他の InformationItems や Classifiers を代表するときには、
    キーワード ``«representation»`` を添えられた破線矢印を用いて
    接続される。

20.1.5 Examples
----------------------------------------------------------------------
* Figure 20.2 Example of InformationFlows conveying InformationItems

  * Company から Customer へ一方的に ``product`` が流れていく。
  * Company から Employee へ一方的に ``wage`` が流れていく。

* Figure 20.3 Information Item represented as a classifier

  * 独立した InformationItem の表記例。
  * どちらの ``wage`` も同じ InformationItem を意味する。

* Figure 20.4 Examples of «representation» notation

  * 左図では ``travel document`` は ``passport`` と ``plane ticket``
    の両方を代表している。

  * 右図では ``Wage`` は具象クラス ``Salary`` と ``Bonus`` の両方の
    「代役」として振る舞う。

* Figure 20.5 InformationItems attached to Connectors

  * 図の ``a``, ``b``, ``d`` 黒三角が InformationItems である。

* Figure 20.6 InformationItems attached to Associations

  * InformationItems が Associations に付属する例。

20.2 Classifier Descriptions
======================================================================
機械生成による節。

20.3 Association Descriptions
======================================================================
機械生成による節。

.. 20.3.1 A_conveyed_conveyingFlow [Association]
.. 20.3.2 A_informationSource_informationFlow [Association]
.. 20.3.3 A_informationTarget_informationFlow [Association]
.. 20.3.4 A_realization_abstraction_flow [Association]
.. 20.3.5 A_realizingActivityEdge_informationFlow [Association]
.. 20.3.6 A_realizingConnector_informationFlow [Association]
.. 20.3.7 A_realizingMessage_informationFlow [Association]
.. 20.3.8 A_represented_representation [Association]

.. include:: /_include/uml-refs.txt
