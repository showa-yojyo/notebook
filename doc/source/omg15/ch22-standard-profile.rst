======================================================================
22 Standard Profile
======================================================================

.. contents::
   :depth: 2

22.1 Summary
======================================================================

Standard Profile は定義済みの標準ステレオタイプの集合を規定する。UML 適合ツール
は Standard Profile のステレオタイプすべてを支援するものとする。

22.2 Model
======================================================================

   Figure 22.1 Model of StandardProfile

このグラフはとにかくノードが多い。

* 今まで見てきた UML の各種メタクラスの名前はすべて fully qualified な形式で記さ
  れている。
* ステレオタイプはキーワード ``«stereotype»`` が名前の上に付いている。
* ステレオタイプから UML メタクラスに接続する矢印の先の形状がいつもと違って黒塗
  り三角であるが、これは気にしなくてよいか？

22.3 Standard Stereotypes
======================================================================

   Table 22.1 Description of the Stereotypes in the UML StandardProfile

プロファイルに所属するステレオタイプは表形式で記述される。

* 最初の列はステレオタイプに対応するステレオタイプラベルの名前を与える。ステレオ
  タイプの実際の名前はステレオタイプラベルと同じだ。
* 第二の列はステレオタイプが適用するメタクラスを特定する。
* 最後の列はステレオタイプの意味の記述だ。

Classifier に適用するプロファイル：

«Realization»
   オブジェクトの領域を指定し、それらの物理的実装も定義する分類子だ。

      For example, a Component stereotyped by «Realization» will only have
      realizing Classifiers that implement behavior specified by a separate
      «Specification» Component.

   これは «ImplementationClass» とは異なる。そちらはシステム設計者にとって有用な
   属性やメソッドなどの特徴を持つことができるクラスの実現だからだ。
«Specification»
   オブジェクトの物理的な実装を定義することなく、領域を指定する分類子だ。

      For example, a Component stereotyped by «Specification» will only have
      provided and required interfaces, and is not intended to have any
      realizingClassifiers as part of its definition.

   これは «Type» とは異なる。そちらは属性やメソッドなど、分析専門家モデリングシ
   ステムにとって有用な機能を持つことができるからだ。

Artifact に適用するプロファイル：

«File»
   開発されたシステムを背景とする物理的なファイル。
«Document»
   人が読めるファイル。«File» のサブクラス。
«Executable»
   計算機システム上で実行可能であるプログラムファイル。«File» のサブクラス。
«Library»
   静的または動的ライブラリーファイル。«File» のサブクラス。
«Script»
   計算機システムが解釈できるスクリプトファイル。«File» のサブクラス。
«Source»
   実行ファイルにコンパイルできるソースファイル。«File» のサブクラス。

Abstraction に適用するプロファイル：

«Derive»
   モデル要素間の導出関係を表すもので、通常は同じ型であるが、必ずしもそうである
   必要はない。導出依存関係は依頼元が供給元から計算される可能性があることを指定
   する。その写像は計算を指定する。依頼元は、論理的には冗長であっても、効率性な
   どの設計上の理由で実装されることがある。
«Refine»
   分析と設計など、異なる語義水準でのモデル要素間の改良関係を指定する。その写像
   二つの要素またはその集合の関係を指定する。写像は計算可能である場合とそうでな
   い場合があり、一方向性である場合と双方向性である場合がある。

      Refinement can be used to model transformations from analysis to design
      and other such changes.
«Trace»
   モデル要素間の追跡関係を指定する。Traces はモデル間の要件や変更を追跡するため
   に主に用いる。モデルの変更は両方向に起こる可能性があるため、依存関係の方向性
   は多くの場合無視することが可能だ。その写像は両者の関係を指定するが、計算可能
   であることはまれで、通常は略式的だ。

Package に適用するプロファイル：

«Framework»
   システムの全部または一部について、再利用可能な建築様式を指定するモデル要素を
   含むパッケージ。Frameworks には通常、クラス、パターン、テンプレートが含まれ
   る。フレームワークがアプリケーション領域に特化されている場合はアプリケーショ
   ンフレームワークと呼ばれることもある。
«ModelLibrary»
   他のパッケージで再利用されることを意図したモデル要素を含むパッケージ。これ
   は、いくつかのプログラミング言語におけるクラスライブラリーに類似している。モ
   デルライブラリーには、プロファイルやステレオタイプなど、(12.3) で規定されてい
   るメタモデル拡張メタクラスのオブジェクトを含めてはならない。しかし、
   ProfileApplications や Stereotype アプリケーションを含んでよく、モデルライブ
   ラリーは適用された Profile と一緒に使われることが多い。

BehavioralFeature に適用するプロファイル：

«Create»
   指定された特徴が、それに付属する分類子のオブジェクトを作成することを指定
   する。
«Destroy»
   指定された特徴が、それに付属する分類子のオブジェクトを破棄することを指定す
   る。

Usage に適用するプロファイル：

«Call»
   操作から操作への使用依存性。この関係は、その依存関係が適用されるクラス内に操
   作が存在するという意味で、操作を含むクラスに包含されることもある。

      A call dependency specifies that the source operation or an operation in
      the source class invokes the target operation or an operation in the
      target class. A call dependency may connect a source operation to any
      target operation that is within scope including, but not limited to,
      operations of the enclosing classifier and operations of other visible
      classifiers.
«Create»
   依頼元 Classifier が供給元 Classifier のオブジェクトを生成することを意味する
   使用依存性。
«Instantiate»
   依頼元に対する操作が供給元オブジェクトを生成することを示す分類子間の使用依存
   関係。
«Responsibility»
   他の要素との関係における、ある要素の契約または義務。
«Send»
   依頼元が Operation で、供給元が Signal である Usage であって、その Operation
   がその Signal を送信することを指定する。

Model に適用するプロファイル：

«Metamodel»
   あるモデリング言語（例えば MOF_ モデル）のモデリング概念を規定するモデル。
«SystemModel»
   SystemModel はステレオタイプ化されたモデルであり、同じシステムのモデルの集団
   を含む。SystemModel には異なるモデルに含まれるモデル要素間の関係や制約もすべ
   て含まれる。

Class に適用するプロファイル：

«Auxiliary»
   より中心的なクラスや基本的なクラスを支援するクラスで、二次的な論理や制御フ
   ローを実装するのが普通だ。Auxiliary クラスは通常、Focus クラスとともに使用さ
   れ、設計時に部品の二次的な業務論理や制御フローを指定するのに特に便利だ。
«Focus»
   中核論理または制御フローを定義するクラスで、それを支援する一つ以上の補助クラ
   スを指す。Focus クラスは通常一つ以上の Auxiliary クラスとともに使用され、設計
   時に部品の中核業務論理や制御フローを指定するのに特に便利だ。
«Metaclass»
   オブジェクトもまたクラスであるクラス。
«ImplementationClass»
   あるプログラミング言語におけるクラスの実装で、オブジェクトは複数のクラスを持
   つことは許されない。これは、オブジェクトが一度に複数のクラスを持つことがで
   き、時間の経過とともにクラスを獲得したり喪失したりすることがあり、オブジェク
   トが動的に複数のクラスを持つことがある Class とは対照的だ。

      An Implementation class is said to realize a Classifier if it provides all
      of the operations defined for the Classifier with the same behavior as
      specified for the Classifier's operations.

   実装クラスは、複数の異なる Types を実現することが許される。

   ImplementationClass の物理的な属性と関連は、それが実現する分類子の属性と同じ
   である必要はない。その物理的な属性と関連に関して、その操作のメソッドを設ける
   ことが許される。
«Type»
   オブジェクトの物理的な実装を定義することなく、オブジェクトの領域と、そのオブ
   ジェクトに適用可能な操作を指定するクラスだ。属性と関連を持つことはある。型操
   作に対する挙動仕様は、例えば Activity 図を使って表現することがある。オブジェ
   クトは、高々一つの ImplementationClass を持ってよいが、複数の異なる型に適合し
   てもよい。
«Utility»
   オブジェクトを持たないが、静的属性と静的操作の名前付き集団を示すクラス。

Component に適用するプロファイル：

«BuildComponent»
   コンパイルや版管理など、システム水準の開発活動を目的として定義された要素の集
   団。
«Entity»
   業務概念を表す永続的な情報部品。
«Implement»
   それ自身が仕様を持つことを意図していない部品定義。むしろ、その部品が
   Dependency を持つ別の «Specification» のための実装だ。
«Process»
   取引に基づいた部品。
«Service»
   状態を持たない関数的部品。
«Subsystem»
   大規模システムの階層分解の単位。部分システムは間接的にオブジェクト化されるの
   がふつうだ。

      Definitions of subsystems vary widely among domains and methods, and it is
      expected that domain and method profiles will specialize this construct.

   部分システムは特化要素と実現要素を持つように定義されることもある。

.. include:: /_include/uml-refs.txt
