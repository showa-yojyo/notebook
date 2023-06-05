======================================================================
6 Additional Information
======================================================================

.. contents::

6.1 Specification Simplification
======================================================================

   This specification has been extensively re-written from its previous version
   to make it easier to read by removing redundancy and increasing clarity. In
   particular, the following major changes have been made since UML 2.4.1:

ということなのだが、私は UML 2.4.1 を知らないのでここにある一覧を読み飛ばす。

   However, the metamodel itself remains unchanged from UML 2.4.1
   superstructure, with a few exceptions:

同じくこの一覧を読み飛ばす。

6.2 Architectural Alignment
======================================================================

Model Driven Architecture (MDA_) 構想とは、ソフトウェア開発のモデル駆動型な取り
組みを支援する業界全体におよぶ技術仕様の集合のための概念上の様式だ。MDA_ におい
て UML と MOF_ と関連仕様が言語を提供したり、モデルを生成・変換したりすることで
重要な役割を果たす。

   The abstract syntax of UML is specified using a UML model called the UML
   metamodel. This metamodel uses constructs from a constrained subset of UML
   that is identified in the MOF 2 specification and used for constructing
   metamodels.

メタモデル内のクラスはメタクラスと呼ばれる。例えば次章
(:doc:`./ch07-common-structure`) で仕様化するメタクラス Element は UML メタモデ
ル内の抽象クラスだ。

   Classes in a metamodel are called :dfn:`metaclasses`. So, for example, the
   UML metaclass Element is an abstract class in the UML metamodel: which also
   means that it can be viewed from the MOF perspective as an instance of the
   metaclass Class, whose isAbstract property has the value true. Another such
   instance is the UML metaclass Comment, which has an attribute named body,
   which can in turn be viewed from the MOF perspective as an instance of the
   metaclass Property whose name property has the value “body”.

UML メタクラス Element は

* UML メタモデルにおける抽象クラスだ。
* MOF の観点からはプロパティー ``isAbstract`` の値が ``true`` であるようなメタク
  ラス Class のインスタンスだ。

もう一つ例を挙げると、UML メタクラス Comment は：

* ``body`` という属性がある。
* MOF の観点からはプロパティー ``name`` の値が ``body`` であるようなメタクラス
  Property のインスタンスだ。

   The fact that UML is defined using itself is no more surprising than the fact
   that many programming languages have compilers written in the language
   itself, or that recursive functions (such as the factorial function) can be
   defined using themselves.

バージョン 2.4.1 は MOF 2.x メタモデル、これは UML 2.x メタモデルを含むが、有
効な UML 2.x モデルである。これは早いバージョンと比較して相当な簡素化と調整が
なされた。

   It is expected that future versions of MOF and UML will continue to be
   aligned in this manner.

UML と MOF の間のメタモデルと関係のさらなる議論は MOF 2 Core 仕様の中で見つけら
れる。

6.3 On the Semantics of UML
======================================================================

6.3.1 Models and What They Model
----------------------------------------------------------------------

モデルとはいつでも何かのモデルだ。モデル化をしようとしているものは一般的にある論
述のある範囲の内部にあるシステムとみなすことが可能だ。

現行システムの場合と計画中システムの場合とで、モデルが表現できるものが異なる：

   For an existing system, the model may represent an analysis of the properties
   and behavior of the system. For a planned system, the model may represent a
   specification of how the system is to be constructed and behave.

UML モデルが何から構成されているかが述べられる：

   A UML model consists of three major categories of model elements, each of
   which may be used to make statements about different kinds of *individual
   things* within the system being modeled (termed simply “individuals” in the
   following). These categories are:

Classifiers
   「分類する者」くらいの意味で、仕様書ではこう述べられている：

      A classifier describes a set of objects. An object is an individual with a
      state and relationships to other objects. The state of an object
      identifies the values for that object of properties of the classifier of
      the object.
Events
   起こり得る事象 (occurrences) の集合の特徴を述べるものだ。

      An :dfn:`occurrence` is something that happens that has some consequence
      with regard to the system.

Behaviors
   可能な実行 (executions) の集合の特徴を述べるものだ。

      An execution is a performance of a set of actions (potentially over some
      period of time) that may generate and respond to occurrences of events,
      including accessing and changing the state of objects.

次の記述が興味深い：

   However, these are again just model elements, making statements about the
   individuals being modeled. As for any model, such statements can be
   incomplete, imprecise, and abstract, according to the purpose of the model,
   and may turn out to be wrong (or even be asserted as counterfactual). The
   individuals being modeled, on the other hand, are always complete, precise,
   and concrete within their domain.

次の文言から始まる最後のパラグラフの要旨がつかめない：

   The execution of behaviors within a modeled system may result in the creation
   and destruction of objects within that system.

6.3.2 Semantic Areas
----------------------------------------------------------------------

UML のモデリング構成要素を、次の意味論的カテゴリーに分類して考える：

* Structural Semantics
* Behavioral Semantics

構造的意味論は、モデル化されている領域内の個体に関する UML 構造モデル要素の意味
を定義するもので、ある特定の時点において真である可能性がある。構造的という修飾に
は静的という意味合いがあることに注意。

行動的意味論は、UML の行動モデル要素の意味を定義するもので、モデル化された領域の
個体が時間とともにどのように変化するかについて記述するものだ。こちらは動的である
ことを示唆する。

   Figure 6.1 shows a more detailed delineation of the semantic areas of UML
   within these categories and the notional layering of these areas.

この図は「土台」から見ていくのが理解が良さそうだ。この仕様書の造りをそのまま示し
ているとも読める。

Structural Modeling
  Common Structure
    型、名前空間、関係、依存といった基本的概念共通の土台。

    :doc:`./ch07-common-structure` で議論する。

    Values
      :doc:`./ch08-values` で議論する。
    Classifiers
      データ型、クラス、シグナル、インターフェイス、コンポーネント等を指す。

      :doc:`./ch09-classification`, :doc:`./ch10-simple-classifiers`,
      :doc:`./ch11-structured-classifiers` で議論する。
    Packages
      パッケージおよびプロファイルという概念がある。

      :doc:`./ch12-packages` で議論する。
Behavioral Modeling
  Common Behavior
    動作の実行・処理のための枠組みを与える基礎構造。

    :doc:`./ch13-common-behavior` で議論する。

    Actions
      UML での動作の基本構成単位である。より細やかな挙動を定義するのに用いられ
      る。

      :doc:`./ch16-actions` で議論する。

      State Machines
        :doc:`./ch14-statemachines` で議論する。
      Activities
        :doc:`./ch15-activities` で議論する。
      Interactions
        :doc:`./ch17-interactions` で議論する。
Supplemental Modeling
  その他の補助的な構成概念。構造的でも行動的でもある。

  Use Cases
    :doc:`./ch18-usecases` で議論する。
  Deployments
    :doc:`./ch19-deployments` で議論する。
  Information Flows
    :doc:`./ch20-informationflows` で議論する。

6.3.3 Stable and Transient Behavioral Semantics
----------------------------------------------------------------------

前節で見た構造的意味論は、対象となるモデルのある瞬間を切り取って表現したものでは
あるが、それでも特定の行動的な観点をモデル化する能力をも含んでいる。例えば：

* 分類子には、それに何らかの動作を求めるために呼び出し可能な動作機能があってもか
  まわない。
* クラスは active であるとモデル化されてもよい。そのクラスのオブジェクトが何か自
  律的な挙動を呈することを意味する。

主要構造モデリングの構成要素の動作特性は：

   The behavioral characteristics of primarily structural modeling constructs
   make high-level statements about the behavior of a system that may generally
   be verified when the system is in a stable state at some specific point in
   time.

* どのようにしてシステムが以前の状態からその状態にどう至ったのかについては定義
  しない。ただこの変化をもたらすために何らかの挙動が起きたはずであるということ
  だ。
* 時間経過に伴う挙動の詳しい定義は、挙動モデリング構成要素の利用を必要とする。

多くの場合に UML モデル内のある構造要素は、その構造的要素のために鑑別される高水
準の挙動を実現するための詳細な挙動を定義する、関連する行動要素が存在することにな
る。

* 例えばクラスには、それが所有する操作 (operation) にその詳細な挙動を定義する関
  連メソッド (method) があってもよい。
* アクティブクラスには、その自律的な挙動を詳らかにする分類子の挙動があってもよ
  い。

UML において意味の差異が特に重要な領域は次だと言っている：

Operational behaviors
  操作とは、クラスのオブジェクトに対して直接発動 (invoke) することが許される、ク
  ラスの挙動に関する機能だ。:doc:`./ch09-classification` 参照。

  操作の定義には、操作の入力および出力引数の型、モデル化されているシステムの状態
  に関する事前条件、事後条件といった概念を含めることが許される。

  操作にはメソッドがあることも許されているが、それは要求される挙動の詳細な定
  義である。:doc:`./ch13-common-behavior` 参照。

     It is a modeler responsibility to ensure that the detailed behavior modeled
     by the method of the operation meets the behavioral requirements given by
     the pre- and postconditions of the operation. Note, however, that the
     postcondition is not required to hold during the *transient* execution of
     the method behavior, but only at the *stable* point of the completion of
     execution of that behavior. A class may also have *invariant* conditions
     that must be true before and after the execution of the operation but may
     be violated during the course of the execution of the operation method.

Property default values
   特性の意味論では、既定値がある特性がオブジェクト化されるときに、その特性に何ら
   かの固有設定が不在であれば、既定値が評価されてその特性の初期値を与えることが規
   定されている (:doc:`./ch09-classification`)。

      Thus, when instantiating a classifier, all its attributes (i.e., properties
      of the classifier) with default values should be properly initialized once
      any behavior required to instantiate the classifier completes. However, a
      create object action is specified to create an object with its attributes
      initially having no initial values, whether or not those attributes have
      default values in the classifier of the object (see sub clause 16.4.3).

Active class behaviors
   活性クラスは、そのようなクラスのオブジェクトが生成するときに、そのオブジェク
   トが生成の直接の帰結としてそれの挙動の実行を開始するようなクラスだ。
   :doc:`./ch11-structured-classifiers` 参照。

   オブジェクト生成作用は、関連する挙動の実行を開始することなくオブジェクトを生
   成するように規定されている。:doc:`./ch16-actions` 参照。

      Instead, it is necessary to use a start object behavior action to execute
      those behaviors (see sub clause 16.3.3). Therefore, when modeling the
      detailed behavior of the instantiation of a classifier, it is a modeler
      responsibility to ensure that the modeled behavior properly starts the
      classifier behavior of an instance of an active class, after that instance
      is created. (This behavior may also be encapsulated in a constructor
      operation for the class.)

   仕様の終盤を読まないと理解不能だが、最後の一文がやはり気になる。

6.4 How to Read this Specification
======================================================================

6.4.1 Specification Format
----------------------------------------------------------------------

   The rest of this document contains the technical content of this
   specification.

だから本腰を入れて読むならばここからがいい。

この仕様書の構成方法と、各章の構造を説明しているだけ。

UML の諸概念は節に分類した。例えば、状態機械モデリングに関連する概念の全ては状
態機械節に、活動モデリングに関連する概念のすべては活動節に集約される。

前方参照を最小限にするべく各章を配列している。

仕様書をリファレンスとして利用されることを意図している。つまり配列順序によらず
に読まれることを想定している。そこで本文中では閲覧や検索の便宜を図るべく、相互
参照をふんだんに設けている。

各章が含む節 (sub clause) の構造は次のようになっている：

Abstract Syntax
   MOF モデル（先程書いたように UML メタモデルである）の言葉で定義された図式
Semantics
   その節が説明している全ての概念の意味
Notation
   その節が説明している全ての概念の記法
Examples
   その節の概念を図説する意図がある見本

各種文体規約：

* イタリック体は強調のために用いる。
* メタクラス名は capitalize して表記するものの、テキスト中では名詞であるかのよ
  うに用いる。必要に応じて複数形にする。
* プロパティー名は 8 ポイントの Arial フォントを用いる。こちらも必要に応じて複
  数形にする。PDF で仕様書を見るときにはプロパティー名が「浮いて」見えるので
  便利。

テキスト表記による図式説明では BNF の変種を用いる。これは記法として潰しが効くの
で引用したいのだが、reST と相性が悪いので、原文の p. 17 をしょっちゅう参照するこ
と。

   Diagrams appearing in the Notation and Examples subdivisions have been
   produced by a variety of tools, and may differ in stylistic details such as
   fonts, line thicknesses, size of arrowheads, etc. Such differences are not
   material to the specification.

Notation の節では図式は白地に黒で描画されることを想定している。適合性のある UML
ツールは他の配色を採用しても構わないのだが、その場合は：

   the word “black” shall be interpreted as “solid”, “white” shall be
   interpreted as “un-filled”, and “gray” shall be interpreted as “a
   distinguishable color between solid and un-filled”.

各章の最後の二節は機械生成による。

* Classifier Descriptions
* Association Descriptions

当ノートではこれらを飛ばす。その代わり、直前の節で言及の見つからなかった情報のた
めにここを参考にはしている。

6.4.2 Diagram Format
----------------------------------------------------------------------

   The following conventions are adopted for all metamodel diagrams throughout
   this specification.

かなり重要な約束なので、読み飛ばすことは考えられない。規約項目からいくつか拾って
みる：

メタクラスは、多くのダイアグラムに表示されることがありますが、主要な役割を果たす
のは、メタクラスのセマンティクスが記述されているダイアグラムに隣接する、1つのダ
イアグラムだけです。主役のメタクラスは、その属性コンパートメントを展開して表示さ
れ、副役のメタクラスは、そのヘッダー長方形だけで表示されます。

* 一つのメタクラスが色々な図式に現れるが、そのメタクラスが主役を張るものはただ一
  つだけだ。それはそのメタクラスの意味が記述されている図式に隣接している。主メタ
  クラスはその属性区画を展開して表記され、副メタクラスはヘッダー矩形だけで表記さ
  れる。

  * 実は同様のことが前節でも書かれている。

* ドット記法。関連の末端の所有権を示すために用いられる。ドットは、ドットに触れら
  れたクラスを型とするプロパティを、もう一方の末端のクラスが所有することを示す。

  * 詳しくは :doc:`./ch11-structured-classifiers` の該当する節で述べられている。
  * 当ノートでは association end を関連端（点）と書くことにする。

* 矢印記法。関連端点の回航可能性（当ノートではよい日本語表現が見つからない間は英
  単語をそのまま記すことにする）を示すのに用いる。

  * 定義上、クラス所有の関連端点すべてが回航可能とする。
  * 慣習上、メタモデル内の全ての関連所有端点は回航不能とする。

* «An association with neither end marked by navigability arrows means that the
  association is navigable in both directions.»

* 特殊化と再定義。関連端点近くに適用する制約情報表示ラベルを付す。

  ``{subsets endA}``
    「この制約が適用される関連端は、関連端 ``endA`` の部分集合である」を意味す
    る。

    .. admonition:: 読者ノート

       この文書では <X subsets Y> という言い回しが頻出するが、意味は <X is a
       subset of Y> である。

  ``{redefines endA}``
    「この制約が適用される関連端は、関連端 ``endA`` を再定義する」を意味する。

  ここで関連端 ``endA`` は既存の関連の要素であることを想定している。

* 関連端に多重度が示されていないならば、それは多重度がちょうど 1 であることを示
  唆する。
* 関連端にラベルが付いていないならば、その端点の既定の名前は、付随するクラスの名
  前から、頭文字を小文字に変えたものとする。

  ただ、回航不能関連端に関しては、しばしばラベルを付けないことがある（名前が
  Association Descriptions の節に文書化されている場合であっても）。

* 明示的に命名されていない関連については、次の生成規則に従い「構築」する (p. 19)。
  ここで ``<association-end-nameX>`` はそれぞれの関連端の名前とする：

  .. code:: text

     "A_" <association-end-name1> "_" <association-end-name2>

  つまり、関連の名前はその両端点の名前から一意に決まるということだ。

  * 視覚的には矢印が ``name2`` から ``name1`` に向いていることが極めて多い。
  * この記法はたいへん便利なので、次章以降のノートで私も多用する。

.. note::

   ドット記法と矢印記法と ``{subsets}`` を例示するためのイラストをここに載せる。
   左側のクラス図は次章の最初に出て来るものであり、右側の文の羅列はここにある矢
   印から読み取れる、所有権や回航可能性の情報である。矢印自体は例えば
   ``A_relatedElement_relationship`` のように呼ぶことができる。

   .. figure:: /_images/omg15-diagram-format.png
      :align: center
      :alt: Diagram Format

6.5 Acknowledgements
======================================================================

仕様書の著者、技術支援提供者、査読者、投稿者、寄稿者等々に対する謝意を表してい
る。

6.5.1 Primary Authors
----------------------------------------------------------------------

   The following people wrote this specification, incorporating the work of
   authors of earlier versions of UML:

七名。

6.5.2 Technical Support
----------------------------------------------------------------------

   The following people provided technical support for this specification,
   including writing tools to generate portions of the document and to validate
   the OCL:

四名。

6.5.3 Reviewers
----------------------------------------------------------------------

   In addition to the authors and technical supporters, the following people
   provided invaluable contributions by reviewing some or all of the
   specification in detail:

十五名。

6.5.4 Submitters
----------------------------------------------------------------------

   The following companies were submitters of this specification:

十法人。

.. include:: /_include/uml-refs.txt
