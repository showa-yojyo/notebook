======================================================================
19 Deployments
======================================================================

.. contents::
   :depth: 3

19.1 Summary
======================================================================

   The Deployments package specifies constructs that can be used to define the
   execution architecture of systems and the assignment of software artifacts to
   system elements.

* 最新のアプリケーションの大部分に十分な、合理的な配備モデルをもたらす。
* より精巧な配備モデルが必要な場合は、プロファイルやメタモデルを通してパッケージ
  を拡張し、特定のハードウェアやソフトウェアの環境を表現することが可能だ。

19.2 Deployments
======================================================================

19.2.1 Summary
----------------------------------------------------------------------

Deployments はシステムの論理的か物理的、またはその両方の要素と、それらに割り当て
られた情報科学技術資産との間にある関係を捕捉する。

19.2.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 19.1 Deployments

NamedElement から抽象クラス DeployedArtifact が特殊化されている。そしてそこから
クラス Artifact が特殊化されている。さらにそこからクラス DeploymentSpecification
が特殊化されている。

Dependency からクラス Deployment が特殊化されている。Deployment は
DeployedArtifact に関連してよく、DeploymentSpecification を所有してよい。

今まで何度も目にしてきた抽象クラス DeploymentTarget の仕様がようやく記述される。

* DeploymentTarget は Deployment を所有してよく、PackageableElement に関連してよ
  い。
* Node, Property, InstanceSpecification は DeploymentTarget の特殊化だ。特に
  InstanceSpecification は DeployedArtifact の特殊化でもある。

19.2.3 Semantics
----------------------------------------------------------------------

Deployment はモデル化したシステムの特定の概念的・物理的要素とそれに割り当てられ
る情報資産との間の関係を捕捉する。

* システム要素は DeployedTargets として、情報資産は DeployedArtifacts として表現
  される。
* Deployed{Targets,Artifacts} は直接オブジェクト化不能な抽象クラスだ。

..

   Individual Deployment relationships can be tailored for specific uses by
   adding DeploymentSpecifications containing configurational and/or parametric
   information and may be extended in specific component profiles.

例えば、プロファイルが DeploymentSpecification に追加する標準的かつ非規範的なス
テレオタイプには、タグ付き値 {thread, process, none} を持つ «concurrencyMode»
と、タグ付き値 {transaction, nestedTransaction, none} を持つ «transactionMode»
がある。

DeploymentSpecification 情報はそれらの ``deployedElement`` リンクを介して、
DeploymentTargets に関連付けられた部品に対する実行時に入力される。

   Using these links, DeploymentSpecifications can be targeted at specific
   container types, as long as the containers are kinds of Components.

DeploymentSpecification は Artifacts であるため、Deployment 関係の要素として捉え
ることができる。さらに、DeploymentSpecification は ExecutionEnvironments である
DeploymentTargets にしか関連付け不能だ。

   The Deployment relationship between a DeployedArtifact and a DeploymentTarget
   can be defined at the “type” level and at the “instance” level.

型レベルでは、Deployment は DeploymentTargets の種類を DeployedArtifacts の種類
に接続する。一方、オブジェクトレベルでは、Deployment は特定の DeploymentTargets
オブジェクトを特定の DeployedArtifacts オブジェクトに接続する。

* 例えば、型レベルの Deployment は、"application server" と "order entry request
  handler" を接続するかもしれない。対照的に、オブジェクトレベルでは、六個の相異
  なる "request handler" オブジェクトに対して、三つ特定のアプリケーションサービ
  スが DeploymentTargets になってもかまわない。

複合的な構造からなる複雑なモデルをモデル化する場合、部分として機能する Property
は、Deployment の対象になることが許される。同様に、

   InstanceSpecifications can be DeploymentTargets in a Deployment relationship,
   if they represent a Node that functions as a part within an encompassing Node
   composition hierarchy, or if they represent an Artifact.

19.2.4 Notation
----------------------------------------------------------------------

DeploymentTargets は遠近感のある直方体で表現される。ラベルは DeploymentTarget の
名前の頭に ``:`` を付ける。

* DeploymentTarget に配備されるシステム要素およびそれらに接続する Deployments は
  その直方体の内側に描かれることがある。
* 配備されるシステム要素を要素名のテキスト一覧の形式で表示すること可能だ。

Deployments は Dependencies と同じく破線矢印の記法を用いて描かれる。

* Deployment 関係が DeploymentTarget の記号中に示される場合、ラベルは不要だ。
  DeploymentTarget 記号外にある場合にはキーワード ``«deploy»`` で装飾することが
  可能だ。
* Deployment 矢印は DeployedArtifacts から DeployedTargets へ向いているのが通例
  だ。

DeploymentSpecifications は classifier 矩形として図式的に表示されて、キーワード
``«deploymentspec»`` で装飾してもよい。

* 通常の依存矢印を使用して、箱に配備された部品に取り付けてもよい。

19.2.5 Examples
----------------------------------------------------------------------

もはや解説が与えられていない。

   Figure 19.2 A visual representation of the deployment location of artifacts,
   including a dependency between them, inside a DeployedTarget graphic.

``:AppServer1`` という配備対象には成果物 :file:`ShoppingCart.jar` と
:file:`Order.jar` を配備する。前者は後者に依存関係がある。

   Figure 19.3 Alternative deployment representation of using a dependency
   called «deploy» used when DeployedArtifacts are visually outside their
   DeployedTarget graphics

前述の図と同じ意味。成果物を遠近感のある立方体の絵の外に描いたので、 Deployment
の矢印にキーワード ``«deploy»`` を付けた。

   Figure 19.4 Textual list based representation of DeployedArtifacts

DeployedArtifacts のオブジェクトをテキストの一覧で表現している。

   Figure 19.5 DeploymentSpecification for an artifact. On the left, a
   type-level specification, and on the right, an instance-level specification.

型として指定するかオブジェクトとして指定するかが異なる。

   Figure 19.6 DeploymentSpecifications related to the DeployedArtifacts that
   they parameterize.

:file:`ShoppingAppdesc.xml` と :file:`Orderdesc.xml` の違いを説明できない。前者
は :file:`ShoppingApp.ear` の実行時入力という解釈で正しいか。

   Figure 19.7 A DeploymentSpecification for a DeployedArtifact

DeploymentSpecification :file:`Orderdesc.xml` が実行時入力となる。

19.3 Artifacts
======================================================================

19.3.1 Summary
----------------------------------------------------------------------

   An Artifact represents some (usually reifiable) item of information that is
   used or produced by a software development process or by operation of a
   system.

モデルファイル、ソースファイル、スクリプト、実行ファイル、データベーステーブル、
開発納品物、書類、メールは Artifacts の例だ。

19.3.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 19.8 Artifacts

Artifact は DeployedArtifact の特殊化であり、同時に Classifier の特殊化だ。後者
の性質により、任意個の Operations (``ownedOperations``) と Properties
(``ownedAttributes``) を所有することが許される。

Artifact は任意の個数の Artifacts を入れ子にできる。その場合は子を
``ownedMembers`` として所有することになる。

Artifact は Manifestations (``manifestation``) を所有することがある。

Manifestation は Abstraction の特殊化だ。

Manifestation は PackageableElement 一つに関連が付けられる。

19.3.3 Semantics
----------------------------------------------------------------------

Artifacts は DeployedArtifact という抽象観念を練りあげて具体化するものだ。

   They represent concrete elements in the physical world, may have Properties
   representing their features and Operations that can be performed their
   instances, and may be multiply-instantiated so that different instances may
   be deployed to various DeploymentTargets, each with separate property values

より複雑な Artifacts は複合的な階層に組織化することで作成することが可能だ。部品
の DeploymentSpecification を Artifact 一つに含めることが許され、部品とその引数
を単一の Artifact オブジェクトとして配備することが許される。

   Artifacts may be extended to better represent the needs of specific
   information items.

* プロファイルはファイルの集合をモデル化するために Artifact を拡張することがある。
* UML では Artifacts 用の標準ステレオタイプをいくつか定義している。``«source»``
  と ``«executable»`` など。必要次第ではさらに特殊化してよい。例えば EJB プロ
  ファイルでは実行可能な Java アーカイブのために ``«executable»`` のサブクラスと
  して ``«jar»`` を定義することがあるかもしれない。

..

   An Artifact may embody, or manifest, a number of model elements.

その Artifact はそれぞれが何らかの PackageableElement の利用を表す
Manifestation を所有する。

プロファイルは、特定の具体化の形式を示すために、Manifestation 関係を拡張すること
がある。例えば、«tool generated» と «custom code» は一つの Artifact に具現化され
た異なる Classes に対する二つの Manifestations であるかもしれない。

19.3.4 Notation
----------------------------------------------------------------------

Artifact はキーワード ``«artifact»`` を付けた普通の Class 矩形で示される。

* またはアイコンで表すこともある (e.g. Fig. 19.9)。
* Artifact オブジェクトの名前の下線を省略してもよい。

Manifestation は Abstraction と同じように記される。すなわち、鏃が開いた破線矢印
を用い、キーワード ``«manifest»`` をラベルとする。

19.3.5 Examples
----------------------------------------------------------------------

   Figure 19.9 An Artifact instance

クラス矩形の右上隅のアイコンが Artifact 用のものであればよい。

   Figure 19.10 A Manifestation relationship between an Artifact and a Component

Artifact ``Order.jar`` から Component ``Order`` に Manifestation の矢印が向かっ
ている。

19.4 Nodes
======================================================================

19.4.1 Summary
----------------------------------------------------------------------

   Nodes elaborate and reify the abstract notion of DeploymentTargets.

* Nodes は入れ子にすることが可能であり、CommunicationPaths を用いて任意の複雑性を
  有するシステムへ接続することが可能だ。
* Nodes はハードウェア装置またはソフトウェア実行環境のどちらか一方を表現する。

19.4.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 19.11 Nodes

* Node は DeployedTarget および Class の特殊化だ。
* Node の特徴は単に自身を入れ子にできるというだけか。
* Node は Device と ExecutionEnvironment を特殊化するためにあるだけか。
* CommunicationPath は Association の特殊化だ。
* Device, ExecutionEnvironment, CommunicationPath は特に性質がない。

19.4.3 Semantics
----------------------------------------------------------------------

   A Node is computational resource upon which Artifacts may be deployed, via
   Deployment relationships, for execution.

* 上級モデリング応用では Nodes は入れ子によって定義される複雑な内部構造を持ち、
  特定の状況を表現するために相互接続されることがある。
* Nodes の内部構造は他の Nodes によってしか構成されることが不能だ。
* Deployments に関与するうえに、Nodes はそこに配備された Artifacts の
  Manifestation 関係から導出される関連要素の集合を取得する。

..

   Nodes may be further sub-typed as Devices and ExecutionEnvironments.

* Devices は物理的な機械の構成部品を表現する。
* ExecutionEnvironments は応用構成部品が実行時に必要とする標準ソフトウェアシステ
  ムを表現する。
* 特定のプロファイルでは、例えば ``«OS»``, ``«workflow engine»``, ``«database
  system»``, ``«J2EE container»`` のような ExecutionEnvironments に対するステレ
  オタイプを定義することがあるかもしれない。

..

   A Device is a physical computational resource with processing capability upon
   which Artifacts may be deployed for execution.

* Device は名前空間の所有権を通じて、またはそれ自体が Devices によって型付けられる
  属性を通じて、複雑になることがある。物理的な計算体系全体がこの方法で構成要素に分
  解されることがある。
* Devices の例を挙げると、``«application server»``, ``«client workstation»``,
  ``«mobile device»``, ``«embedded device»`` といったものになるだろう。

通常、ExecutionEnvironments は、Node で定義された複合関係によって、何らかの、多
くの場合より上位の Device または一般的なシステム Node に割り当てられる。

ExecutionEnvironments は入れ子にすることが可能だ。

ExecutionEnvironment は、配備された要素によって呼び出されるシステムレベルのサー
ビスに対する明示的なインターフェースを持つことがある。そのような場合、ソフトウェ
アの ExecutionEnvironment サービスはなるべく明示的にモデル化される。次に、適切な
タイプのアプリケーション部品が、特定の ExecutionEnvironment 節点または
DeployedArtifacts の Manifestations 関係に、Deployment 関係で配置される。

各部品の Deployment について、これらのサービスの観点は、特定の種類の
ExecutionEnvironment の DeploymentSpecification の特性によって決定してもよい。

   Nodes can be connected to represent specific network topologies using
   CommunicationPaths defining specific connections between Node instances.

CommunicationPath は二つの DeploymentTargets の間の Association であり、これを通
じてこの二つが Signals と Messages を交換することがある。

19.4.4 Notation
----------------------------------------------------------------------

Node は DeploymentTarget と同じ図像的表現を用いて描かれる。

Device はキーワード ``«device»`` を付した Node 図像として示される。

ExecutionEnvironment はキーワード ``«executionEnvironment»`` を付した Node とし
て示される。

Nodes 間の CommunicationPaths は通常の Association リンクと同じものを用いて描か
れる。

キーワード ``«deploy»`` 付きの破線矢印は、Node が外部に描かれた DeployedArtifact
を支える能力を示す。代わりに、Node 記号の内側に DeployedArtifact 図像を入れ子に
して示してもかまわない。

19.4.5 Examples
----------------------------------------------------------------------

もはや解説がない。

   Figure 19.12 Notation for a Device containing an ExecutionEnvironment and
   connected to another Device by a CommunicationPath link

* ``:AppServer`` と ``:DBServer`` の二つの Devices がリンクしている。
* ExecutionEnvironment ``:J2EEServer`` が ``:AppServer`` に含まれている。

   Figure 19.13 Notation for a ExecutionEnvironment

Fig. 19.12 の ``:J2EEServer`` と同じ。

   Figure 19.14 An instance of a Node

Fig. 19.12 の ``:AppServer`` のガワ。

   Figure 19.15 CommunicationPath between AppServer with deployed Artifacts and
   a DBServer

``AppServer`` と ``DBServer`` の間のリンクに注目すればいい。多重度を記してよい。

   Figure 19.16 Deployed component Artifacts on a Node

Fig. 19.2 と同じ。

19.5 Classifier Descriptions
======================================================================

機械生成による節。

19.6 Association Descriptions
======================================================================

機械生成による節。

.. include:: /_include/uml-refs.txt
