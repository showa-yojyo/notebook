======================================================================
18 UseCases
======================================================================

UML 2.5 pp. 637-650 に関するノート。

.. contents:: ノート目次
   :depth: 2

18.1 Use Cases
======================================================================

18.1.1 Summary
----------------------------------------------------------------------

* UseCases はシステムの要求、すなわちシステムが何をするためのものであるのかを捉
  える手段の一つである。この章で指定される要の概念は Actors, UseCases,
  ``subjects`` である。

  * UseCase の ``subject`` それぞれはその UseCase が適用する検討中のシステムを表
    現する。
  * ``subject`` に相互作用する利用者と他のシステムのいずれもが Actors として表現
    される。

* UseCase は挙動の詳細である。

  * UseCase のオブジェクトは対応する UseCase に適合する出現する挙動の出来事を参
    照する。こういうオブジェクトは Interactions を用いて記述されることがよくあ
    る。

18.1.2 Abstract Syntax
----------------------------------------------------------------------

* Figure 18.1 UseCases

  * Actor と UseCase は BehavioredClassifier の特殊化である。
  * Extend と Include は NamedElement と DirectedRelationship の両方の特殊化であ
    り、UseCase が所有する可能性がある。

    * Extend は Constraint を一個だけ所有する可能性がある。

  * ExtensionPoint を UseCase が複数所有する可能性がある。

18.1.3 Semantics
----------------------------------------------------------------------

18.1.3.1 Use Cases and Actors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* UseCase は任意の個数の ``subjects`` に適用してよい。 UseCase が ``subject`` に
  適用するときには、その事は ``subject`` によって行われる挙動の集合を指定し、
  Actors または ``subject`` の他の利害関係者に対する値である、目に見える結果を生
  じる。
* UseCase とは示された Behaviors の集合の宣言を表現する BehavioredClassifier の
  一種である。UseCase のそれぞれは ``subject`` が一つまたはそれを超える Actors
  と協調して行うことができる何らかの挙動を指定する。
* UseCase の ``subject`` はシステムあるいは挙動を有することができる他の要素のい
  ずれか、例えば Component や Class などである可能性がある。UseCase のそれぞれ
  はその ``subject`` が利用者に対して実現する有用な機能の構成単位を指定する。
* UseCases を ``subject`` の（外部からの）要求の仕様と、``subject`` により示され
  る機能の仕様との両方に対して利用することが可能である。
* UseCase の挙動は事前条件、事後条件、適切な自然言語のテキストによってばかりでな
  く、（その ``ownedBehavior`` 関係を通じて） Interactions, Activities,
  StateMachines のようなBehaviors の集合により記述されることが可能である。

  * 型がそれの部分である Classifiers として UseCase とその Actors を使う
    Collaboration によってでも間接的に記述することができる。

* UseCases には関連した Actors があってもよく、それらは UseCase を実現している
  Classifier のオブジェクトとActor の役割の一つを演じている利用者がどのように影
  響しあうかを記述する。
* UseCase が 1 を超える多重度の端に Actor と関連すると、それは一つを超える個数の
  Actor オブジェクトがその UseCase に付随することを意味する。

  * 複数の Actors が UseCase に関与する方法は持ち合わせている特定の状況に依存す
    るものなので、本仕様では定義されない。

* Package または Classifier のどちらも UseCase を所有することが許される。所有す
  る Classifier は所有された UseCases が適用する ``subject`` を典型的には表すの
  ではあるが、Figure 18.10 で図解されるように、この事は必ずしも当てはまらない。
* Actor は関連する UseCases の ``subjects`` と相互に作用する実体が演じる役割の型
  をモデル化する。 Actors は人間の利用者、外部ソフトウェア、または他のシステムに
  より演じられる役割を表現してよい。

  * Actor は必ずしも特定の物理的実体を表現しないが、代わりにその関連する
    UseCases の詳細に関連の何らかの実体についての特定の役割を表現する。
  * 役割 (role) という用語をここでは非公式に用いており、本仕様書中の他のどこかに
    見当たるその用語の技術的な定義のいずれも意味しない。

* UseCase が 1 を超える多重度のある Actor に関連があるときには、その事は与えられ
  た Actor がその型の複数の UseCases に付随する可能性があることを意味する。

18.1.3.2 Extends
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Extend とは、拡張している UseCase で定義された挙動が拡張された UseCase で定義
  された挙動の中にいつ、どのように挿し込まれるのかを指定する、拡張している
  UseCase (``extension``) から拡張された UseCase (``extendedCase``) への関係性で
  ある。
* Extend は一つまたはそれを超える UseCase で定義された挙動に、事によると条件付き
  で、追加されるべきさらなる挙動があるときに利用されるのを意図されている。
* 拡張された UseCase は拡張している UseCase と独立して定義されるし、拡張している
  UseCase と独立して意味がある。他方では、拡張している UseCase は、それ自身で意
  味がある必要がなくてもよい挙動を典型的に定義する。

  * 同じ拡張している UseCase は一つより多い UseCase を拡張することが可能である。
    その上、拡張している UseCase は自身を拡張してよい。

* Extend とは、``source`` が拡張している UseCase であり、``target`` が拡張されて
  いる UseCase であるような DirectedRelationship の一種である。それはまた、所有
  している UseCase の文脈において``name`` があることが可能であるようにする
  NamedElement の一種でもある。

  * Extend 関係自身は ``extension`` によって所有される。

* ExtensionPoint はその挙動が Extend 関係により拡張されることが可能となる
  UseCaseの挙動にある点を識別する。
* ExtensionPoint の位置を定義する明確なやり方は意図的に未指定である。この事は
  UseCases を自然言語、図表、木、等々のようなさまざまな書式で指定することが認め
  られていることによる。
* Extend の ``condition`` が欠けているか、あるいは拡張された UseCase の実行中に
  到達した初回時に ture と評価するならば、拡張している UseCase の適切な挙動の断
  片のすべてもまた実行されるはずである。

  * ``condition`` が ``false`` であれば、これは起こらない。

18.1.3.3 Includes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Include は二つの UseCases の間の DirectedRelationship であり、包含される
  UseCase (``addition``) の挙動が包含されている UseCase (``includingCase``) の挙
  動に挿し込まれるのを示している。

  * Include はまた、所有する UseCase (``includingCase``) の文脈で ``name`` があ
    ることを可能にするようなNamedElement の一種でもある。

* Include 関係は二つまたはそれを超える UseCases の挙動の共通部分があるときに利用
  されることを意図されている。この共通部分はそれから別々の UseCase に引き出され
  て、この部分が共通にある基本 UseCases のすべてによって含まれることになる。
* 包含される UseCase の挙動のすべては、包含している UseCase の実行が再開される前
  に、包含される UseCase 内の単一の場所で実行される。
* Include 関係では UseCases の再利用のみならず UseCases の階層的合成ができる。

18.1.4 Notation
----------------------------------------------------------------------

* UseCase は楕円として示される。名前は楕円に入れるか、楕円の下に置くかどちらかに
  する。

  * 名前の上にオプションでステレオタイプキーワードを配置してよい。

* UseCases の集合についての ``subject`` を左上隅に名前を記した矩形として示してよ
  い。ここで UseCase 楕円はこの矩形の視覚的な内側に位置される。
* ``subject`` classifier についてのこの記法は通常の Classifier の記法とは異なる
  ことに注意する。見出しも区画もない。
* ``subject`` 矩形は ``subject`` classifier が包含される UseCases を所有すること
  を意味しないことにも注意する。単に UseCases がその classifier に適用するという
  ことだ。
* 属性と操作は UseCase 楕円の内部にある区画らに、それらがあたかも普通の
  Classifier 矩形であるかのように、同じ内容で示してよい。
* ExtensionPoints は見出しが **extension points** である UseCase の区画に列記し
  てよい。ExtensionPoint それぞれは UseCase 記号内にテキスト文字列で記す。
* UseCases には他の Associations および他の Classifiers についての Dependencies
  があってよい。
* UseCase により定義された詳細な挙動は選ばれた記述手法に従って、別々の図式または
  テキストの文章に記録される。
* UseCase を標準の Classifiers 用の矩形記法を用いて示してもよい。その場合は楕円
  アイコンを矩形右上隅に載せる。
* Actor は棒人間アイコンにより表現される。Actor の名前はアイコンの近くに書かれ
  る。
* Actor はキーワード ``«actor»`` の付いた Classifier 矩形で示してもよい。
* 他の Actor の種類を伝えるアイコンもまた Actor を記すのに用いてよい。
* Classifier により UseCase の入れ子（所有）を、UseCase 楕円を別々の区画に
  Classifier 矩形内に入れ子にすることにより選択的に表現してもよい。
* UseCases 間の Extend 関係は先の開いた破線の矢印で示される。矢印の方向は拡張し
  ている UseCase から拡張されている UseCase に向いている。矢印のラベルにはキー
  ワード ``«extend»`` が付く。
* UseCases 間の Include 関係は先の開いた破線の矢印で示される。矢印の方向は根本の
  UseCase から包含される UseCase に向いている。矢印のラベルにはキーワード
  ``«include»`` が付く。

18.1.5 Examples
----------------------------------------------------------------------

* Figure 18.2 Class diagram of a Package owning a set of UseCases, Actors, and a
  Subsystem

  * UseCases, Actors および UseCases の ``subject`` である部分システムの集合を所
    有するPackage ATMtopPkg に対応するクラス図である。
  * この見本は Customer または Administrator がそれぞれの関連する UseCases のど
    れを共用することが許される or許されないのかを示す。

    * 多重度の ``0..1`` からそれが読み取れる。

* Figure 18.3 Example Extend

  * UseCase ``"Perform ATM Transaction"`` に ExtensionPoint ``"selection"`` があ
    る。
  * UseCase ``"Perform ATM Transaction"`` はこの ExtensionPoint を経由して
    UseCase ``"Online Help"`` に拡張される。その条件は「顧客が "HELP" を選択す
    る」である。

* Figure 18.4 Example Include

  * UseCase ``"Withdraw"`` は独立して定義された UseCase ``"Card
    Identification"`` を包含する。

* Figure 18.5 UseCase using Classifier rectangle notation

  * UseCase ``"OrderStationery"`` をクラス用の標準矩形表記法で示している。
  * 矩形右上隅に楕円を描けばよい。
  * 区画 ``"extension points"`` は任意だが、記すときはこのようにする。

* Figure 18.6 Actor notation using stick-man

  * 棒人間を描き、その真下に Actor 名を記す。

* Figure 18.7 Actor notation using Class rectangle

  * 矩形を描き、内部にキーワード  ``«actor»`` 付き Actor 名を記す。

* Figure 18.8 Actor notation using icon

  * 図像で Actor を表現する例。イメージは PC に見えるが Actor 名は ``"User"`` と
    ある。

* Figure 18.9 Notation for UseCase owned by Classifier

  * ``"Make Purchase"`` は Class ``"DepartmentStore"`` の ``ownedUseCase`` であ
    る。
  * 区画の名前が ``"owned use cases"`` となっているが、これは特性名
    ``ownedUseCase`` から得られる。

* Figure 18.10 Example ATM system with UseCases and Actors

  * これは前掲 Figure 18.10 と同じ機能だが、次の見本で示すように UseCases の所属
    が別々であったりする。

* Figure 18.11 Example UseCases owned by Packages

  * Package の中身が UseCases になっている。
  * ``"ATM Services"`` が ``"TransactionUseCases"`` を import しているので、二つ
    の UseCases が色を変えて描かれている。

* Figure 18.12 Example UseCase with associated StateMachine

  * 左側は UseCase ``"MakeCall"`` に StateMachine がその ``ownedBehaviors`` の一
    つとしてあることを示している。

    * 区画 ``"owned behaviors"`` の記載は任意。
    * StateMachine "Call" はここでは矩形プラスキーワード ``«statemachine»`` のみ
      で示されている。

18.2 Classifier Descriptions
======================================================================

機械生成による節。

18.3 Association Descriptions
======================================================================

機械生成による節。

.. include:: /_include/uml-refs.txt
