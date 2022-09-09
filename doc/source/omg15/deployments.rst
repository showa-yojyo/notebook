======================================================================
19 Deployments
======================================================================
UML 2.5 pp. 651-666 に関するノート。

.. todo::

   * component profile (n.)
   * deliverables (n.) これは artifacts と同義かもしれない。

.. contents:: ノート目次
   :depth: 2

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

  * 配置か引数、またはその両者による情報を含む
    DeploymentSpecifications を追加することにより
    特定の用途に対して合うようにすることが可能であり、

  * 特定の component profiles で拡張されることが許される。

* DeploymentSpecification 情報は
  それらの ``deployedElement`` リンクを経由して
  DeploymentTargets に関連した components に対する実行時入力になる。

* DeployedArtifact と DeploymentTarget の間の Deployment 関係は
  "type" レベルにおいてと "instance" レベルにおいて
  定義することが可能である。

* 複合的な構造からなる複雑なモデルをモデル化することを可能にするために、
  Property は、部分の役目を果たして
  （すなわち composition で所有され）、
  Deployment の対象になることが許される。

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
    キーワード «deploy» を付けて装飾することが可能である。

* DeploymentSpecifications は classifier 矩形として図式的に表示されて、
  キーワード «deploymentspec» を付けて装飾するのもよい。

19.2.5 Examples
----------------------------------------------------------------------
もはや解説が与えられていない。

* Figure 19.2 A visual representation of the deployment location of artifacts, (...)

  * ":AppServer1" という配備対象には
    成果物 "ShoppingCart.jar" と "Order.jar" を配備する。
    前者は後者に依存関係がある。

* Figure 19.3 Alternative deployment representation of using a dependency (...)

  * 前述の図と同じ意味。
    成果物を遠近感のある立方体の絵の外に描いたので、
    Deployment の矢印にキーワード «deploy» を付けた。

* Figure 19.4 Textual list based representation of DeployedArtifacts

  * DeployedArtifacts のオブジェクトをテキストの一覧で表現している。

* Figure 19.5 DeploymentSpecification for an artifact (...)

  * type レベルと instance レベルの違い。

* Figure 19.6 DeploymentSpecifications related to the DeployedArtifacts that they parameterize

  * "ShpiingAppdesc.xml" と "Orderdesc.xml" の違いを説明できない。
    前者は "ShoppingApp.ear" の実行時入力という解釈で正しいか。

* Figure 19.7 A DeploymentSpecification for a DeployedArtifact

  * DeploymentSpecification "Orderdesc.xml" が実行時入力となる。

19.3 Artifacts
======================================================================
19.3.1 Summary
----------------------------------------------------------------------
* Artifact は
  ソフトウェア開発工程やシステムの操作によって
  利用されたり生産されたりする
  情報の（通常具体化可能な）項目を表現する。

  * モデルファイル、ソースファイル、スクリプト、実行ファイル、
    データベーステーブル、開発納品物、書類、メールは
    Artifacts の例である。

19.3.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 19.8 Artifacts

  * Artifact は DeployedArtifact の特殊化であり、
    同時に Classifier の特殊化である。
    後者の性質により、任意個の Operations (``ownedOperations``) と
    Properties (``ownedAttributes``) を所有することが許される。

  * Artifact は任意の個数の Artifacts を入れ子にできる。
    その場合は子を ``ownedMembers`` として所有することになる。

  * Artifact は Manifestations (``manifestation``) を所有することが許されている。

  * Manifestation は Abstraction の特殊化である。
  * Manifestation は PackageableElement ひとつに関連が付けられる。

19.3.3 Semantics
----------------------------------------------------------------------
* Artifacts は DeployedArtifact の抽象観念を
  練りあげて具体化するものである。

* より複雑な Artifacts は、複合的な階層にそれらを組織化することにより
  作成されることが可能である。

* Artifacts は特定の情報項目の要求するものをよりよく表現するために
  拡張されることが許される。

  * UML では Artifacts 用の標準ステレオタイプをいくつか定義していて、
    «source» と «executable» はその例である。

    * 必要次第ではさらに特殊化してよい。
      例えば «jar» を実行可能な Java アーカイブのために
      «executable» のサブクラスとして定義することがあるかもしれない。

* Artifact はモデル要素のいくらかを具体化するか、
  明白にするかが認められる。
  そういった Artifact は Manifestations を所有し、
  それぞれは何か PackageableElement の利用を表現している。

  * Profiles は Manifestation 関係を拡張して、
    特定の具体化の形式 (pl.) を指し示すことが許される。
    例えば «tool generated» と «custom code» は
    Artifact に具体化された異なる Classes に対しての
    ふたつの Manifestations であるかもしれない。

19.3.4 Notation
----------------------------------------------------------------------
* Artifact はキーワード «artifact» を付けた普通の Class 矩形を用いて
  示される。

  * またはアイコンにより描かれてもよい。
  * Artifact オブジェクトの名前の下線は省略されていてもよい。

* Manifestation は Abstraction と同じように記される。
  すなわち、破線の矢先が開いた矢印を用い、
  キーワード «manifest» をラベルとする。

19.3.5 Examples
----------------------------------------------------------------------
* Figure 19.9 An Artifact instance

  * クラス矩形の右上隅のアイコンが Artifact 用のものであればよい。

* Figure 19.10 A Manifestation relationship between an Artifact and a Component

  * Artifact ``Order.jar`` から Component ``Order`` に
    Manifestation の矢印が向かっている。

19.4 Nodes
======================================================================
19.4.1 Summary
----------------------------------------------------------------------
* Nodes は DeployedTargets の抽象観念を
  練りあげて具体化するものである。
  Nodes は入れ子にすることも、
  CommunicationPaths を用いて任意の複雑性を有するシステムへ接続させることもできる。
  典型的に Nodes はハードウェア装置またはソフトウェア実行環境の
  どちらか一方を表現する。

19.4.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 19.11 Nodes

  * Node は DeployedTarget および Class の特殊化である。
  * Node の特徴は単に自身を入れ子にできるというだけか。
  * Node は Device と ExecutionEnvironment を特殊化するためにあるだけか。
  * CommunicationPath は Association の特殊化である。
  * Device, ExecutionEnvironment, CommunicationPath は特に性質がない。

19.4.3 Semantics
----------------------------------------------------------------------
* Node とはその上に Artifacts が配備されてよい計算の手段であり、
  Deployment 関係を通じて配備され、実行を目的とする。

* Nodes は Devices と ExecutionEnvironments としてさらに特殊化されてよい。

  * Devices は物理的な機械の構成部品を表現する。
  * ExecutionEnvironments はアプリケーション構成部品が
    実行時に要求する標準のソフトウェアシステムを表現する。

    * 特定の profiles は ExecutionEnvironments のために、
      例えば «OS», «workflow engine», «database system»,
      ``«J2EE container»`` のような
      stereotypes を定義することがあるかもしれない。

* Device とは
  Artifacts が実行をする目的で配備されることを許される処理能力を有する
  物理的な計算上の手段である。

  * Devices の例を挙げると、
    «application server», «client workstation»,
    «mobile device», «embedded device» といったものになるだろう。

* 典型的に ExecutionEnvironments は
  往々にして高水準な Device や一般のシステム Node に
  Node 上で定義される合成関係を通じて割り当てられる。

* Nodes は
  固有の network topologies を表現するために、
  Node オブジェクト間の特定の接続を定義する CommunicationPaths を用いて
  接続されることが可能である。

  * CommunicationPath はふたつの DeploymentTargets の間の
    Association であり、
    それを通じてふたつの目標物が Signals と Messages を交換する。

19.4.4 Notation
----------------------------------------------------------------------
* Node は DeploymentTarget と同じ表現を用いて描かれる。
* Device はキーワード «device» を付した Node として示される。
* ExecutionEnvironment はキーワード «executionEnvironment» を
  付した Node として示される。
* Nodes 間の CommunicationPaths は通常の Association リンクと同じものを
  用いて描かれる。
* キーワード «deploy» 付きの破線矢印は、
  ノードが外部に描かれた DeployedArtifact を支援する能力を示す。
  そうする代わりに、Node シンボルの内側に
  DeployedArtifact の絵を入れ子にすることで示されてよい。

19.4.5 Examples
----------------------------------------------------------------------
もはや解説がない。

* Figure 19.12 Notation for a Device containing an ExecutionEnvironment and (...)
* Figure 19.13 Notation for a ExecutionEnvironment
* Figure 19.14 An instance of a Node
* Figure 19.15 CommunicationPath between AppServer with deployed Artifacts and a DBServer
* Figure 19.16 Deployed component Artifacts on a Node

19.5 Classifier Descriptions
======================================================================
機械生成による節。

19.6 Association Descriptions
======================================================================
機械生成による節。

.. include:: /_include/uml-refs.txt
