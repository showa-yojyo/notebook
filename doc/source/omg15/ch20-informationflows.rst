======================================================================
20 InformationFlows
======================================================================

.. admonition:: 読者ノート

   現在ノート修正中。

.. contents::
   :depth: 2

20.1 Information Flows
======================================================================

20.1.1 Summary
----------------------------------------------------------------------

* InformationFlows パッケージはシステム実体の間の情報の交換を高水準の抽象度で支
  援する。
* InformationFlows はシステムを通じて情報の回覧を一般的な手法で記述する。

  * 同様に InformationItems は実現化の詳細が設計される前でさえ、
    InformationFlows に沿って流れる情報を表現するのに用いられる。

* InformationFlows パッケージの中身は Figure 20.1 で示す。

20.1.2 Abstract Syntax
----------------------------------------------------------------------

* Figure 20.1 Information Flows

  * InformationFlow は PackageableElement と DirectedRelationship の特殊化であ
    る。

    * 関連する型がかなり多くある。

      * Classifier (``conveyed``)
      * Relationship (``realization``)
      * NamedElement (``informationSource``, ``informationTarget``)
      * Connector (``realizingConnector``)
      * ActivityEdge (``realizingActivityEdge``)
      * Message (``realizingMessage``)

  * InformationItem は Classifier の特殊化である。

    * InformationItem は InformationItem (``represented``) に関連する。

20.1.3 Semantics
----------------------------------------------------------------------

* InformationFlows は情報品目の一方通行なある種の情報経路を必要とする。
* InformationFlow の ``sources`` と ``targets`` は伝達された InformationItems や
  Classifiers を送信 (``sources``) または受信 (``targets``) することが可能なオブ
  ジェクトの集合を指定する。

* InformationFlow の ``sources`` と ``targets`` はそれらの型であるか、それらに
  よって含まれている（＝所有されている）かの可能性のあるオブジェクトのすべてを代
  表する。

  * 例えばもし ``source`` または ``target`` が Classifier ならば、それは
    Classifier の潜在的オブジェクトすべてを代表する。

* 情報経路は ``sources`` と ``targets`` の本質に付随したさまざまな方法により実現
  化されることが可能である。

  * Relationships, Connectors, ActivityEdges, Messages によって実現化されること
    が可能である。

* 典型的には InformationFlows は ``sources`` から ``targets`` に流れる
  InformationItems を見分けるのだが、Class などの具象 Classifiers もまた伝達され
  ることが許される。
* InformationItems は ``sources`` から ``targets`` に流れることが可能なたくさん
  の種類の情報をたいへん抽象的なやり方で表現する。
* InformationItems の重要な用途に早い設計段階の間、おそらくは最終的にそれらを定
  義するような詳細なモデリングの決定がなされるよりも以前において、情報を表現する
  というものがある。
* InformationItems はより明確な InformationItems や Classifiers へと分解されてよ
  い。
* InformationItems は Classes の全種類、Interfaces, Signals そして他の
  InformationItems によって実現化されることしか認められない。
* InformationFlows の主要なゴールは情報がモデルのある領域から別の領域へ移動する
  ことを伝達することである。

20.1.4 Notation
----------------------------------------------------------------------

* InformationFlow は Dependency と同じ表記法を用いて表現されるが、キーワード
  ``«flow»`` を破線に添えておく。
* InformationItems の表現はそれらが表示される周辺状況により決定される。

  * InformationFlow の ``«flow»`` 破線に付属するときには、InformationItem の名
    前が適切な線の近くに表示される。
  * InformationFlows と独立して表示されるときには、InformationItems はそれらが
    Classifiers であるゆえ、矩形内部の名前として表現されてよい。矩形にはキーワー
    ド ``«information»`` か黒塗りの二等辺三角形を付ける。
  * InformationFlow の情報経路の実現化に付属するときには、情報経路上の黒塗りの二
    等辺三角形が情報の流れの方向を指示する。
  * InformationItem が他の InformationItems や Classifiers を代表するときには、
    キーワード ``«representation»`` を添えられた破線矢印を用いて接続される。

20.1.5 Examples
----------------------------------------------------------------------

* Figure 20.2 Example of InformationFlows conveying InformationItems

  * ``Company`` から ``Customer`` へ一方的に ``product`` が流れていく。
  * ``Company`` から ``Employee`` へ一方的に ``wage`` が流れていく。

* Figure 20.3 Information Item represented as a classifier

  * 独立した InformationItem の表記例。
  * どちらの ``wage`` も同じ InformationItem を意味する。

* Figure 20.4 Examples of ``«representation»`` notation

  * 左図では ``travel document`` は ``passport`` と ``plane ticket`` の両方を代
    表している。
  * 右図では ``Wage`` は具象クラス ``Salary`` と ``Bonus`` の両方の「代役」とし
    て振る舞う。

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

.. include:: /_include/uml-refs.txt
