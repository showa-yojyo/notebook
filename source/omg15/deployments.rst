======================================================================
19 Deployments
======================================================================
UML 2.5 pp. 651-666 に関するノート。

.. todo::

   * component profile (n.)

.. contents:: ノート目次

19.1 Summary
======================================================================
* Deployments パッケージは、
  システムの実行様式と
  ソフトウェア成果物のシステム要素への割り当てを
  定義するために利用することが可能な構成概念を指定する。

19.2 Deployments
======================================================================

19.2.1 Summary
----------------------------------------------------------------------
* Deployments は論理的か物理的、またはその両方のシステム要素と
  それらに割り当てられる情報科学技術資産との
  間にある関係を捕捉する。

19.2.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 19.1 Deployments

  * NamedElement から抽象クラス DeployedArtifact が特殊化されている。
    そしてそこからクラス Artifact が特殊化されている。
    さらにそこからクラス DeploymentSpecification が特殊化されている。

  * Dependency からクラス Deployment が特殊化されている。

    * Deployment は DeployedArtifact に関連してよく、
      DeploymentSpecification を所有してよい。

  * 今まで何度も目にしてきた抽象クラス DeploymentTarget の仕様が
    ようやく記述される。

    * DeploymentTarget は Deployment を所有してよく、
      PackageableElement に関連してよい。

    * Node, Property, InstanceSpecification は DeploymentTarget の
      特殊化である。特に InstanceSpecification は DeployedArtifact の
      特殊化でもある。

19.2.3 Semantics
----------------------------------------------------------------------
* Deployment はモデル化したシステムの概念的または物理的な要素と
  それに割り当てられる情報資産との間の関係を捕捉する。

  * システム要素は DeployedTargets として、
    情報資産は DeployedArtifacts として表現される。

* 個別の Deployment の関係は、

  * 特定の用途に対して、配置か引数、またはその両者による情報を含む
    DeploymentSpecifications を追加することにより作られることが可能であり、

  * 特定の component profiles で拡張されることが許される。

* DeploymentSpecification 情報は
  DeploymentTarget::deployedElement リンクを経由して
  DeploymentTargets に関連した components に対する実行時入力になる。

* DeployedArtifact と DeploymentTarget の間の Deployment 関係は
  type レベルにおいてと instance レベルにおいて
  定義されることが可能である。

* 複合的な構造からなる複雑なモデルをモデル化することを可能にするために、
  Property は、部分の役目を果たして
  （すなわち composition で所有され）、
  Deployment の target になることが許される。

19.2.4 Notation
----------------------------------------------------------------------
* DeploymentTargets は遠近感のある立方体（これは大げさ）として示される。
  ラベルは DeploymentTarget の名前がコロンを頭に付けた状態で示される。

  * DeploymentTarget に配備されるシステム要素および
    それらに接続する Deployments は、
    遠近感のある立方体の内側に描かれる。

* Deployments は Dependencies と同じく破線矢印の表記法を用いて描かれる。

  * Deployment 関係が DeploymentTarget の絵の中に示されるときには
    ラベルは不必要である。
    DeploymentTarget の絵の外にあるときには
    キーワード ``«deploy»`` を付けて装飾することが可能である。

* DeploymentSpecifications は classifier 矩形として図式的に表示されて、
  キーワード ``«deploymentspec»`` を付けて装飾するのもよい。

19.2.5 Examples
----------------------------------------------------------------------
もはや解説が与えられていない。

* Figure 19.2 A visual representation of the deployment location of artifacts, (...)

  * ``:AppServer1`` という配備対象には
    成果物 ``ShoppingCart.jar`` と ``Order.jar`` を配備する。
    前者は後者に依存関係がある。

* Figure 19.3 Alternative deployment representation of using a dependency (...)

  * 前述の図と同じ意味。
    成果物を遠近感のある立方体の絵の外に描いたので、
    Deployment の矢印にキーワード ``«deploy»`` を付けた。

* Figure 19.4 Textual list based representation of DeployedArtifacts

  * DeployedArtifacts のオブジェクトをテキストの一覧で表現している。

* Figure 19.5 DeploymentSpecification for an artifact (...)

  * type レベルと instance レベルの違い。

* Figure 19.6 DeploymentSpecifications related to the DeployedArtifacts that they parameterize

  * ``ShpiingAppdesc.xml`` と ``Orderdesc.xml`` の違いを説明できない。
    前者は ``ShoppingApp.ear`` の実行時入力という解釈で正しいか。

* Figure 19.7 A DeploymentSpecification for a DeployedArtifact

  * DeploymentSpecification ``Orderdesc.xml`` が実行時入力となる。

19.3 Artifacts
======================================================================
.. todo:: ノート作成

19.3.1 Summary
----------------------------------------------------------------------

19.3.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 19.8 Artifacts

19.3.3 Semantics
----------------------------------------------------------------------

19.3.4 Notation
----------------------------------------------------------------------

19.3.5 Examples
----------------------------------------------------------------------
* Figure 19.9 An Artifact instance
* Figure 19.10 A Manifestation relationship between an Artifact and a Component

19.4 Nodes
======================================================================
.. todo:: ノート作成

19.4.1 Summary
----------------------------------------------------------------------

19.4.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 19.11 Nodes

19.4.3 Semantics
----------------------------------------------------------------------

19.4.4 Notation
----------------------------------------------------------------------

19.4.5 Examples
----------------------------------------------------------------------
* Figure 19.12 Notation for a Device containing an ExecutionEnvironment and (...)
* Figure 19.13 Notation for a ExecutionEnvironment
* Figure 19.14 An instance of a Node
* Figure 19.15 CommunicationPath between AppServer with deployed Artifacts and a DBServer
* Figure 19.16 Deployed component Artifacts on a Node

19.5 Classifier Descriptions
======================================================================
機械生成による節。

.. 19.5.1 Artifact [Class]
.. 19.5.2 CommunicationPath [Class]
.. 19.5.3 DeployedArtifact [Abstract Class]
.. 19.5.4 Deployment [Class]
.. 19.5.5 DeploymentSpecification [Class]
.. 19.5.6 DeploymentTarget [Abstract Class]
.. 19.5.7 Device [Class]
.. 19.5.8 ExecutionEnvironment [Class]
.. 19.5.9 Manifestation [Class]
.. 19.5.10 Node [Class]

19.6 Association Descriptions
======================================================================
機械生成による節。

.. 19.6.1 A_configuration_deployment [Association]
.. 19.6.2 A_deployedArtifact_deploymentForArtifact [Association]
.. 19.6.3 A_deployedElement_deploymentTarget [Association]
.. 19.6.4 A_deployment_location [Association]
.. 19.6.5 A_manifestation_artifact [Association]
.. 19.6.6 A_nestedArtifact_artifact [Association]
.. 19.6.7 A_nestedNode_node [Association]
.. 19.6.8 A_ownedAttribute_artifact [Association]
.. 19.6.9 A_ownedOperation_artifact [Association]
.. 19.6.10 A_utilizedElement_manifestation [Association]

.. include:: /_include/uml-refs.txt
