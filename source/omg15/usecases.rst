======================================================================
18 UseCases
======================================================================
UML 2.5 pp. 637-650 に関するノート。

.. todo:: 最低でもあと一回は編集する。

.. contents:: ノート目次
   :depth: 2

18.1 Use Cases
======================================================================
18.1.1 Summary
----------------------------------------------------------------------
* UseCases はシステムの要求、すなわちシステムが何をすると想定されるかを
  捉える手段のひとつである。

  * 要の概念は Actors, UseCases, UseCase::subjects である。

* UseCase は振る舞いの詳細である。

  * UseCase のオブジェクトは偶然に起こる (emergent) 振る舞いの出来事を参照する。
    こういうオブジェクトは往々にして Interactions を用いて記述される。

18.1.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 18.1 UseCases

  * Actor と UseCase は BehavioredClassifier の特殊化である。
  * Extend と Include は NamedElement と DirectedRelationship の
    両方の特殊化であり、UseCase が所有する可能性がある。

    * Extend は Constraint を一個だけ所有する可能性がある。

  * ExtensionPoint を UseCase が複数所有する可能性がある。

18.1.3 Semantics
----------------------------------------------------------------------
18.1.3.1 Use Cases and Actors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* UseCase は任意の個数の subjects に適用してよい。

* UseCase とは差し出された Behaviors の集合ひとつの宣言を表現する
  BehavioredClassifier の一種である。

* UseCase::subject はシステムあるいは振る舞いを持つ任意の他の要素、
  例えば Component や Class などである可能性がある。

* UseCases は subject の（外部からの）要求の仕様に対してと、
  subject により差し出される機能の仕様に対してとの
  両方に利用されることが可能である。

* UseCase の振る舞いは
  事前条件、事後条件、適切な自然言語のテキストによってばかりでなく、
  （その ownedBehavior 関係を通じて）
  Interactions, Activities, StateMachines のような
  Behaviors の集合により記述されることが可能である。

* UseCases は関連した Actors を持つことが許されており、
  それらは UseCase を実現している Classifier のオブジェクトと
  Actor の役割のひとつを演じている利用者がどのように影響しあうかを記述する。

* UseCase が 1 を超える多重度のある Actor に関連があるときには、
  それは UseCase にひとつを超える個数だけの Actor オブジェクトが
  伴われることを意味する。

* UseCase は Package または Classifier のどちらかにより所有されることが許される。

* Actor は関連した UseCases::subjects と相互に作用する実体が演じる
  役割の型をモデル化する。
  Actors は人間の利用者、外部ソフトウェア、または他のシステムにより
  演じられる役割を表現してよい。

  * Actor は必ずしも特定の物理的実体を表現しないが、
    代わりにその関連した UseCases の詳細に関連のある実体についての
    特定の役割を少しは表現する。

  * 役割 (role) という用語をここでは非公式に用いたのであり、
    本仕様書中の他のどこかに見当たるその用語の
    技術的な定義のいずれも含意しない。

* UseCase が 1 を超える多重度のある Actor に関連があるときには、
  それは与えられた Actor がその型の複数の UseCases に伴われる可能性があることを
  意味する。

18.1.3.2 Extends
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Extend とは、拡張している UseCase で定義された振る舞いが
  拡張された UseCase で定義された振る舞いの中に
  いつ、どのように挿し込まれるのかを指定する、
  拡張している UseCase (Extend::extension) から
  拡張された UseCase (Extend::extendedCase) への関係性である。

* Extend はひとつまたはそれ以上の UseCase で定義された振る舞いに、
  事によると条件付きで、追加されるべきさらなる振る舞いが少しはあるときに
  利用されるのを意図されている。

* 拡張された UseCase は拡張している UseCase と独立して定義されるし、
  そこに意義がある。

  * 同じ拡張している UseCase はひとつより多い UseCase を拡張することが可能である。
    その上、拡張している UseCase は自身を拡張されてよい。

* Extend は DirectedRelationship の一種であり、
  source が拡張している UseCase であり、
  target が拡張されている UseCase であるようなものである。
  それは所有している UseCase の context で name を持つことが可能にするために
  NamedElement の一種でもある。

* ExtensionPoint は
  その振る舞いが Extend 関係により拡張されることが可能となる
  UseCase の振る舞いにある点を識別する。

* ExtensionPoint の位置を定義する明確なやり方は意図的に未指定である。
  UseCases が自然言語だの図表だのさまざまな書式で指定されることが
  認められていることによる。

* Extend::condition が欠けているか、あるいは
  拡張された UseCase の実行中に届いた最初の時に真と評価するならば、
  拡張している UseCase の適切な振る舞いの部品のすべてもまた
  実行されるのである。

18.1.3.3 Includes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Include はふたつの UseCases の間の DirectedRelationship であり、
  包含される UseCase (Include::addition) の振る舞いが
  包含されている UseCase (Include::includingCase) の振る舞いに
  挿し込まれるのを示している。

* Include 関係はふたつまたはそれ以上の UseCases の振る舞いの部分に共通
  するものがあるときに利用されることを意図されている。

* 包含される UseCase の振る舞いのすべては、
  包含している UseCase の実行が再開される前に、
  包含される UseCase 内の一地点にて実行される。

* Include 関係は UseCases の再利用のみならず
  UseCases の階層的合成を許す。

18.1.4 Notation
----------------------------------------------------------------------
* UseCase は楕円として示される。
  名前は楕円に入れるか、楕円の下に置くかどちらかにする。

  * 名前の上にオプションでステレオタイプキーワードを配置してよい。

* UseCases の集合に関連する subject を左上隅に名前を記した矩形として示してよい。
  ここで UseCase 楕円はこの矩形の内側に視覚的に位置される。

* subject classifier のこの記法は通常の Classifier の記法とは異なることに注意する。
  見出しも区画もない。

* subject 矩形は subject classifier が包含される UseCases を所有することを
  意味しないことにも注意する。
  単に UseCases がその classifier に適用するということだ。

* 属性と操作は UseCase 楕円の内部にある区画らに、
  それらがあたかも普通の Classifier 矩形であるかのように、
  同じ内容で示してよい。

* ExtensionPoints は見出しが ``extension points`` である
  UseCase の区画にリストしてよい。

* UseCases は他の Associations および
  他の Classifiers についての Dependencies を持ってよい。

* UseCase により定義された詳細な振る舞いは
  選んだ記述手法に従って、別々の図式またはテキストの文章に記録される。

* UseCase は標準の Classifiers 用の矩形記法を用いて示されてもよい。
  その場合は楕円アイコンを矩形右上隅に載せる。

* Actor は棒人間アイコンにより表現される。
  Actor の名前はアイコンの近くに書かれる。

* Actor はキーワード ``«actor»`` の付いた Classifier 矩形で示してもよい。

* 他の Actor の種類を伝えるアイコンもまた Actor を記すのに用いてよい。

* Classifier により UseCase の入れ子（所有）は
  UseCase 楕円を別々の区画に Classifier 矩形内に入れ子にすることにより
  選択的に表現されてもよい。

* UseCases 間の Extend 関係は先の開いた破線の矢印で示される。
  矢印の方向は拡張している UseCase から拡張されている UseCase に向いている。
  矢印のラベルにはキーワード ``«extend»`` が付く。

* UseCases 間の Include 関係は先の開いた破線の矢印で示される。
  矢印の方向は基の UseCase から包含される UseCase に向いている。
  矢印のラベルにはキーワード ``«include»`` が付く。

18.1.5 Examples
----------------------------------------------------------------------
* Figure 18.2 Class diagram of a Package owning a set of UseCases, Actors, and a Subsystem

  * UseCases, Actors, UseCase::subject である Subsystem を所有する
    Package ATMtopPkg に対応するクラス図（？）。

  * この見本は Customer または Administrator が
    それぞれの関連する UseCases のどれを共用することが許される or
    許されないのかを示す。

    * 多重度の ``0..1`` からそれが読み取れる。

* Figure 18.3 Example Extend

  * UseCase ``Perform ATM Transaction`` に
    ExtensionPoint ``selection`` がある。

  * UseCase ``Perform ATM Transaction``  はこの ExtensionPoint を経由して
    UseCase ``Online Help`` に拡張される。
    その条件は「顧客が ``HELP`` を選択する」である。

* Figure 18.4 Example Include

  * UseCase ``Withdraw`` は独立して定義された UseCase ``Card Identification``
    を包含する。

* Figure 18.5 UseCase using Classifier rectangle notation

  * UseCase ``OrderStationery`` をクラス用の標準矩形表記法で示している。
  * 矩形右上隅に楕円を描けばよい。
  * 区画 ``extension points`` は任意だが、記すときはこのようにする。

* Figure 18.6 Actor notation using stick-man

  * 棒人間を描き、その真下に Actor 名を記す。

* Figure 18.7 Actor notation using Class rectangle

  * 矩形を描き、内部にキーワード  ``«actor»`` 付き Actor 名を記す。

* Figure 18.8 Actor notation using icon

  * 図像で Actor を表現する例。
    イメージは PC に見えるが Actor 名は ``User`` とある。

* Figure 18.9 Notation for UseCase owned by Classifier

  * ``Make Purchase`` は Class ``DepartmentStore`` の ownedUseCase である。
  * 区画の名前が ``owned use cases`` となっているが、
    これは特性名 ownedUseCase から得られる。

* Figure 18.10 Example ATM system with UseCases and Actors

  * これは前掲 Figure 18.10 と同じ機能だが、
    次の見本で示すように UseCases の所属が別々であったりする。

* Figure 18.11 Example UseCases owned by Packages

  * Package の中身が UseCases になっている。
  * ``ATM Services`` が ``TransactionUseCases`` を import しているので、
    ふたつの UseCases が色を変えて描かれている。

* Figure 18.12 Example UseCase with associated StateMachine

  * 左側は UseCase ``MakeCall`` が StateMachine をその
    ownedBehaviors のひとつとして持つことを示している。

    * 区画 ``owned behaviors`` の記載は任意。

    * StateMachine ``Call`` はここでは矩形プラスキーワード ``«statemachine»``
      のみで示されている。

18.2 Classifier Descriptions
======================================================================
機械生成による節。

18.3 Association Descriptions
======================================================================
機械生成による節。

.. 18.3.1 A_addition_include [Association]
.. 18.3.2 A_condition_extend [Association]
.. 18.3.3 A_extend_extension [Association]
.. 18.3.4 A_extendedCase_extend [Association]
.. 18.3.5 A_extensionLocation_extension [Association]
.. 18.3.6 A_extensionPoint_useCase [Association]
.. 18.3.7 A_include_includingCase [Association]
.. 18.3.8 A_subject_useCase [Association]

.. include:: /_include/uml-refs.txt
