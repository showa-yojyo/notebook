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
* UseCases はシステムの要求、すなわちシステムが何をするためのものであるのかを
  捉える手段のひとつである。
  この章で指定される要の概念は Actors, UseCases, ``subjects`` である。

  * UseCase の ``subject`` それぞれは
    その UseCase が適用する検討中のシステムを表現する。

  * ``subject`` に相互作用する利用者と他のシステムのいずれもが
    Actors として表現される。

* UseCase は挙動の詳細である。

  * UseCase のオブジェクトは対応する UseCase に適合する
    出現する挙動の出来事を参照する。
    こういうオブジェクトは Interactions を用いて記述されることがよくある。

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
* UseCase は任意の個数の ``subjects`` に適用してよい。
  UseCase が ``subject`` に適用するときには、
  その事は ``subject`` によって行われる挙動の集合を指定し、
  Actors または ``subject`` の他の利害関係者に対する値である、
  目に見える結果を生じる。

* UseCase とは示された Behaviors の集合の宣言を表現する
  BehavioredClassifier の一種である。
  UseCase のそれぞれは
  ``subject`` がひとつまたはそれを超える Actors と協調して
  行うことができる何らかの挙動を指定する。

* UseCase の ``subject`` はシステムあるいは
  挙動を有することができる他の要素のいずれか、
  例えば Component や Class などである可能性がある。
  UseCase のそれぞれはその ``subject`` が利用者に対して実現する
  有用な機能の構成単位を指定する。

* UseCases を ``subject`` の（外部からの）要求の仕様と、
  ``subject`` により示される機能の仕様との
  両方に対して利用することが可能である。

* UseCase の挙動は
  事前条件、事後条件、適切な自然言語のテキストによってばかりでなく、
  （その ``ownedBehavior`` 関係を通じて）
  Interactions, Activities, StateMachines のような
  Behaviors の集合により記述されることが可能である。

  * 型がそれの部分である Classifiers として
    UseCase とその Actors を使う
    Collaboration によってでも間接的に記述することができる。

* UseCases には関連した Actors があってもよく、
  それらは UseCase を実現している Classifier のオブジェクトと
  Actor の役割のひとつを演じている利用者が
  どのように影響しあうかを記述する。

* UseCase が 1 を超える多重度の端に Actor と関連すると、
  それはひとつを超える個数の Actor オブジェクトがその UseCase に
  付随することを意味する。

  * 複数の Actors が UseCase に関与する方法は
    持ち合わせている特定の状況に依存するものなので、
    本仕様では定義されない。

* Package または Classifier のどちらも UseCase を所有することが許される。
  所有する Classifier は所有された UseCases が適用する ``subject`` を
  典型的には表すのではあるが、
  Figure 18.10 で図解されるように、この事は必ずしも当てはまらない。

* Actor は関連する UseCases の ``subjects`` と相互に作用する実体が演じる
  役割の型をモデル化する。
  Actors は人間の利用者、外部ソフトウェア、または他のシステムにより
  演じられる役割を表現してよい。

  * Actor は必ずしも特定の物理的実体を表現しないが、
    代わりにその関連する UseCases の詳細に関連の何らかの実体についての
    特定の役割を表現する。

  * 役割 (role) という用語をここでは非公式に用いており、
    本仕様書中の他のどこかに見当たるその用語の
    技術的な定義のいずれも意味しない。

* UseCase が 1 を超える多重度のある Actor に関連があるときには、
  その事は与えられた Actor がその型の複数の UseCases に
  付随する可能性があることを意味する。

18.1.3.2 Extends
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Extend とは、拡張している UseCase で定義された挙動が
  拡張された UseCase で定義された挙動の中に
  いつ、どのように挿し込まれるのかを指定する、
  拡張している UseCase (``extension``) から
  拡張された UseCase (``extendedCase``) への関係性である。

* Extend はひとつまたはそれを超える UseCase で定義された挙動に、
  事によると条件付きで、追加されるべきさらなる挙動があるときに
  利用されるのを意図されている。

* 拡張された UseCase は拡張している UseCase と独立して定義されるし、
  拡張している UseCase と独立して意味がある。
  他方では、
  拡張している UseCase は、それ自身で意味がある必要がなくてもよい
  挙動を典型的に定義する。

  * 同じ拡張している UseCase はひとつより多い UseCase を拡張することが可能である。
    その上、拡張している UseCase は自身を拡張してよい。

* Extend とは、
  ``source`` が拡張している UseCase であり、
  ``target`` が拡張されている UseCase であるような
  DirectedRelationship の一種である。
  それはまた、所有している UseCase の文脈において
  ``name`` があることが可能であるようにする
  NamedElement の一種でもある。

  * Extend 関係自身は ``extension`` によって所有される。

* ExtensionPoint は
  その挙動が Extend 関係により拡張されることが可能となる
  UseCase の挙動にある点を識別する。

* ExtensionPoint の位置を定義する明確なやり方は意図的に未指定である。
  この事は UseCases を自然言語、図表、木、等々のような
  さまざまな書式で指定することが認められていることによる。

* Extend の ``condition`` が欠けているか、あるいは
  拡張された UseCase の実行中に到達した初回時に ture と評価するならば、
  拡張している UseCase の適切な挙動の断片のすべてもまた
  実行されるはずである。

  * ``condition`` が false であれば、これは起こらない。

18.1.3.3 Includes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Include はふたつの UseCases の間の DirectedRelationship であり、
  包含される UseCase (``addition``) の挙動が
  包含されている UseCase (``includingCase``) の挙動に
  挿し込まれるのを示している。

  * Include はまた、
    所有する UseCase (``includingCase``) の文脈で ``name`` が
    あることを可能にするような
    NamedElement の一種でもある。

* Include 関係はふたつまたはそれを超える UseCases の挙動の共通部分が
  あるときに利用されることを意図されている。
  この共通部分はそれから別々の UseCase に引き出されて、
  この部分が共通にある基本 UseCases のすべてによって含まれることになる。

* 包含される UseCase の挙動のすべては、
  包含している UseCase の実行が再開される前に、
  包含される UseCase 内の単一の場所で実行される。

* Include 関係では UseCases の再利用のみならず
  UseCases の階層的合成ができる。

18.1.4 Notation
----------------------------------------------------------------------
* UseCase は楕円として示される。
  名前は楕円に入れるか、楕円の下に置くかどちらかにする。

  * 名前の上にオプションでステレオタイプキーワードを配置してよい。

* UseCases の集合についての ``subject`` を左上隅に名前を記した矩形として示してよい。
  ここで UseCase 楕円はこの矩形の視覚的な内側に位置される。

* ``subject`` classifier についてのこの記法は
  通常の Classifier の記法とは異なることに注意する。
  見出しも区画もない。

* ``subject`` 矩形は ``subject`` classifier が包含される UseCases を所有することを
  意味しないことにも注意する。
  単に UseCases がその classifier に適用するということだ。

* 属性と操作は UseCase 楕円の内部にある区画らに、
  それらがあたかも普通の Classifier 矩形であるかのように、
  同じ内容で示してよい。

* ExtensionPoints は見出しが **extension points** である
  UseCase の区画に列記してよい。
  ExtensionPoint それぞれは UseCase 記号内にテキスト文字列で記す。

* UseCases には他の Associations および
  他の Classifiers についての Dependencies があってよい。

* UseCase により定義された詳細な挙動は
  選ばれた記述手法に従って、別々の図式またはテキストの文章に記録される。

* UseCase を標準の Classifiers 用の矩形記法を用いて示してもよい。
  その場合は楕円アイコンを矩形右上隅に載せる。

* Actor は棒人間アイコンにより表現される。
  Actor の名前はアイコンの近くに書かれる。

* Actor はキーワード «actor» の付いた Classifier 矩形で示してもよい。

* 他の Actor の種類を伝えるアイコンもまた Actor を記すのに用いてよい。

* Classifier により UseCase の入れ子（所有）を、
  UseCase 楕円を別々の区画に Classifier 矩形内に入れ子にすることにより
  選択的に表現してもよい。

* UseCases 間の Extend 関係は先の開いた破線の矢印で示される。
  矢印の方向は拡張している UseCase から拡張されている UseCase に向いている。
  矢印のラベルにはキーワード «extend» が付く。

* UseCases 間の Include 関係は先の開いた破線の矢印で示される。
  矢印の方向は根本の UseCase から包含される UseCase に向いている。
  矢印のラベルにはキーワード «include» が付く。

18.1.5 Examples
----------------------------------------------------------------------
* Figure 18.2 Class diagram of a Package owning a set of UseCases, Actors, and a Subsystem

  * UseCases, Actors,
    および UseCases の ``subject`` である部分システムの集合を所有する
    Package ATMtopPkg に対応するクラス図である。

  * この見本は Customer または Administrator が
    それぞれの関連する UseCases のどれを共用することが許される or
    許されないのかを示す。

    * 多重度の ``0..1`` からそれが読み取れる。

* Figure 18.3 Example Extend

  * UseCase "Perform ATM Transaction" に
    ExtensionPoint "selection" がある。

  * UseCase "Perform ATM Transaction"  はこの ExtensionPoint を経由して
    UseCase "Online Help" に拡張される。
    その条件は「顧客が "HELP" を選択する」である。

* Figure 18.4 Example Include

  * UseCase "Withdraw" は独立して定義された UseCase "Card Identification"
    を包含する。

* Figure 18.5 UseCase using Classifier rectangle notation

  * UseCase "OrderStationery" をクラス用の標準矩形表記法で示している。
  * 矩形右上隅に楕円を描けばよい。
  * 区画 "extension points" は任意だが、記すときはこのようにする。

* Figure 18.6 Actor notation using stick-man

  * 棒人間を描き、その真下に Actor 名を記す。

* Figure 18.7 Actor notation using Class rectangle

  * 矩形を描き、内部にキーワード  «actor» 付き Actor 名を記す。

* Figure 18.8 Actor notation using icon

  * 図像で Actor を表現する例。
    イメージは PC に見えるが Actor 名は "User" とある。

* Figure 18.9 Notation for UseCase owned by Classifier

  * "Make Purchase" は Class "DepartmentStore" の ``ownedUseCase`` である。
  * 区画の名前が "owned use cases" となっているが、
    これは特性名 ``ownedUseCase`` から得られる。

* Figure 18.10 Example ATM system with UseCases and Actors

  * これは前掲 Figure 18.10 と同じ機能だが、
    次の見本で示すように UseCases の所属が別々であったりする。

* Figure 18.11 Example UseCases owned by Packages

  * Package の中身が UseCases になっている。
  * "ATM Services" が "TransactionUseCases" を import しているので、
    ふたつの UseCases が色を変えて描かれている。

* Figure 18.12 Example UseCase with associated StateMachine

  * 左側は UseCase "MakeCall" に StateMachine がその
    ``ownedBehaviors`` のひとつとしてあることを示している。

    * 区画 "owned behaviors" の記載は任意。

    * StateMachine "Call" はここでは矩形プラス
      キーワード «statemachine» のみで示されている。

18.2 Classifier Descriptions
======================================================================
機械生成による節。

18.3 Association Descriptions
======================================================================
機械生成による節。

.. include:: /_include/uml-refs.txt
