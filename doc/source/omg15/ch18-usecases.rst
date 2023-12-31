======================================================================
18 UseCases
======================================================================

.. contents::
   :depth: 4

18.1 Use Cases
======================================================================

18.1.1 Summary
----------------------------------------------------------------------

UseCases はシステムの要求、すなわちシステムが何をすることになっているものである
のかを捉える手段の一つだ。主要概念は Actors, UseCases, ``subjects`` だ。

* UseCase の ``subject`` それぞれはその UseCase が適用される検討中のシステムを表
  現する。
* 利用者や ``subject`` に相互作用することがある他のシステムは Actors として表現
  される。

..

   A UseCase is a specification of behavior. An instance of a UseCase refers to
   an occurrence of the emergent behavior that conforms to the corresponding
   UseCase.

こういうオブジェクトは Interactions を用いて記述されがちだ。

18.1.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 18.1 UseCases

* Actor と UseCase は BehavioredClassifier の特殊化だ。
* Extend と Include は NamedElement と DirectedRelationship の両方の特殊化であ
  り、UseCase が所有することがある。

  * Extend は Constraint を一個だけ所有することがある。

* ExtensionPoint を UseCase が複数所有することがある。

18.1.3 Semantics
----------------------------------------------------------------------

18.1.3.1 Use Cases and Actors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

UseCase は任意の個数の ``subjects`` に適用してよい。 UseCase が ``subject`` に適
用する場合、その ``subject`` によって行われる挙動の集合が指定され、その
``subject`` の Actors または他の利害関係者にとって価値のある、目に見える結果が生
じる。

   A UseCase is a kind of BehavioredClassifier that represents a declaration of
   a set of offered Behaviors.

* UseCase のそれぞれは ``subject`` が一つ以上の Actors と協調して行うことが可能
  である挙動を指定する。
* UseCase はその ``subject`` の内部構造を参照することなしに、その ``subject`` の
  供給される Behaviors を定義する。これらの Behaviors はその Actors と
  ``subject`` の相互作用に関与し、その ``subject`` の状態の変化とその環境との通
  信を生じることがある。
* UseCase には異例の挙動やエラー処理など、基本挙動の変種を含めることが可能だ。

UseCase の ``subject`` はシステム、または Component や Class など、挙動を有する
ことがある他の要素である可能性がある。UseCase のそれぞれはその ``subject`` が利
用者に対して実現する有用な機能の単位（それと相互作用する特定の手段）を指定する。

   This functionality must always be completed for the UseCase to complete. It
   is deemed complete if, after its execution, the ``subject`` will be in a
   state in which no further inputs or actions are expected and the UseCase can
   be initiated again, or in an error state.

UseCases を ``subject`` に対する（外部からの）要求の仕様と、``subject`` が供給す
る機能の仕様との両方に対して利用することが可能だ。さらに、UseCases は指定された
``subject`` がそのサービスを行使することが可能であるように、その Actors がその
``subject`` とどのようになるべく相互作用するのかを定義することによって、指定
``subject`` がその環境に対して提示する要件を述べてもよい。

   The behaviors of a UseCase can be described by a set of Behaviors (through
   its ``ownedBehavior`` relationship), such as Interactions, Activities, and
   StateMachines, as well as by pre-conditions, post-conditions and natural
   language text where appropriate.

また、UseCase とその Actors を、その部分を型付ける Classifiers として使う
Collaboration を通して間接的に記述することもある。これらの技法のどちらを採用する
かは、その UseCase 挙動の性質や読者次第だ。これらの記述は組み合わせることが可能
だ (Fig. 18.12)。

UseCases には関連 Actors があってもよく、UseCase を実現している Classifier のオ
ブジェクトと Actor の役割の一つを演じる利用者がどのように相互作用するかを記述す
る。二つの UseCases はそれぞれ個別にその ``subject`` の完全な使用法を記述するた
め、関連付けることは不可能だ。

   When a UseCase has an association to an Actor with a multiplicity that is
   greater than one at the Actor end, it means that more than one Actor instance
   is involved in the UseCase.

複数の Actors がどのように UseCase に関与するかは、具体的な状況により異なり、本
仕様では定義されない。

   A UseCase may be owned either by a Package or by a Classifier.

所有する Classifier は所有される UseCases が適用される ``subject`` を表すのが普
通ではあるが、Fig. 18.10, 18.11 で図解されるように、必ずしも当てはまらない。

Actor は関連する UseCases の ``subjects`` と相互作用する物が果たす役割の型のモデ
ルだ。Actors は人間の利用者、外部ソフトウェア、他のシステムが果たす役割を表現す
ることがある。

Actor は特定の物理的実体を必ずしも表現するものではなく、その関連する UseCases の
詳細に関連する、何らかの実体についての特定の役割を表現する。

   Thus, a single physical instance may play the role of several different
   Actors and, conversely, a given Actor may be played by multiple different
   instances.

役割 (role) という用語をここでは非公式に用いており、本仕様書中の他のどこかに
見当たるその用語の技術的な定義のいずれをも意味しない。

Actor が UseCase に関連し、UseCase 側の多重度が 1 を超える場合、ある Actor がそ
の型の複数の UseCases に関与することが可能であることを意味する。

   The specific nature of this multiple involvement depends on the case on hand
   and is not defined in this specification. Thus, an Actor may initiate
   multiple UseCases in parallel (concurrently) or at different points in time.

18.1.3.2 Extends
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Extend:

   An Extend is a relationship from an extending UseCase (the ``extension``) to
   an extended UseCase (the ``extendedCase``) that specifies how and when the
   behavior defined in the extending UseCase can be inserted into the behavior
   defined in the extended UseCase. The extension takes place at one or more
   specific extension points defined in the extended UseCase.

Extend は少なくとも一つの UseCase で定義された挙動に、条件付きでなるべく追加され
るさらなる挙動がある場合に利用される。

被拡張 UseCase はその拡張 UseCase と独立して定義され、この拡張 UseCase とは独立
して意味を持つ。他方では、拡張 UseCase はそれ自身では必ずしも意味をなさない挙動
を定義する。

   Instead, the extending UseCase defines a set of modular behavior increments
   that augment an execution of the extended UseCase under specific conditions.

同じ拡張 UseCase は複数 UseCase を拡張することが可能だ。その上、拡張 UseCase は
自身が拡張されることもある。

   Extend is a kind of DirectedRelationship, such that the ``source`` is the
   extending UseCase and the ``target`` is the extended UseCase.

また、NamedElement の一種でもあり、所有する UseCase の context において ``name``
を持つことが可能だ。この Extend 関係自体はその ``extension`` が所有する。

   An ExtensionPoint identifies a point in the behavior of a UseCase where that
   behavior can be extended by an Extend relationship. Each ExtensionPoint has a
   unique name within a UseCase.

ExtensionPoint の位置を定義する明確なやり方は意図的に未指定だ。UseCases は自然言
語、図表、樹形図等々、さまざまな形式で指定することが認められているからだ。

   The intuition behind the notion of ``extensionLocation`` is best explained
   through the example of a textually described UseCase: Usually, a UseCase with
   ExtensionPoints consists of a set of finer-grained behavioral fragment
   descriptions, which are most often executed in sequence.

このように UseCase テキストの断片構造化は、元の断片間の適切な挿入点（拡張点）に
補足的な挙動の断片記述を合併することで、元の挙動の記述を拡張してもよい。したがっ
て、拡張 UseCase は通常、被拡張 UseCase の適切な箇所に挿入される一つ以上の挙動断
片記述から構成される。

   An ``extensionLocation``, therefore, is a specification of all the various
   ExtensionPoints in a UseCase where supplementary behavioral increments can be
   merged.

拡張 UseCase 実行中に最初の ExtensionPoint に到達した時点で、Extend の
``condition`` が欠けているか、あるいは被拡張 UseCase の実行中に到達した初回時に
真であると評価される場合、拡張 UseCase の適切な挙動断片のすべてもまた実行され
る。この ``condition`` が偽であれば、このようなことは起こらない。

   The individual fragments are executed as the corresponding ExtensionPoints of
   the extended UseCase are reached. Once a given fragment is completed,
   execution continues with the behavior of the extended UseCase following the
   ExtensionPoint.

複数の UseCase があっても、実行される挙動は一つであることに注意。

18.1.3.3 Includes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Include:

   Include is a DirectedRelationship between two UseCases, indicating that the
   behavior of the included UseCase (the ``addition``) is inserted into the
   behavior of the including UseCase (the ``includingCase``). It is also a kind
   of NamedElement so that it can have a ``name`` in the context of its owning
   UseCase (the ``includingCase``).

包括する UseCase は、包括される UseCase の実行によって生じる変更に依存することが
ある。包括する UseCase の挙動を完全に記述するためには、包括される UseCase が利用
可能であることが必要だ。

   The Include relationship is intended to be used when there are common parts
   of the behavior of two or more UseCases.

この共通部分は、別の UseCase に抽出され、この共通部分を持つすべての基底 UseCases
に包括される。

Include 関係の主な用途は共通部分の再利用であるため、基底 UseCase に残されたもの
は、通常、それ自体で完全なものではなく、包括された部分に依存して意味を持つ。これ
は関係の方向に反射され、基底 UseCase が ``addtion`` に依存し、その逆はないことを
示す。

   All of the behavior of the included UseCase is executed at a single location
   in the included UseCase before execution of the including UseCase is resumed.

Include 関係は UseCases の階層的合成や再利用を可能にする。

18.1.4 Notation
----------------------------------------------------------------------

UseCase の記法：

   A UseCase is shown as an ellipse, either containing the name of the UseCase
   or with the name of the UseCase placed below the ellipse.

ステレオタイプキーワードを名前の上に配置してもかまわない。

   A ``subject`` for a set of UseCases (sometimes called a :dfn:`system
   boundary`) may be shown as a rectangle with its name in the top-left corner,
   with the UseCase ellipses visually located inside this rectangle.

同じモデル UseCase は複数の subject 矩形内に別々の楕円として描かれることがある。

   Where a ``subject`` is a Classifier with a standard stereotype, the keyword
   for the stereotype shall be shown in guillemets above the name of the
   subject.

メタクラスがあいまいな ``subject`` の場合は Classifier のメタクラスに対する記法
に対応するキーワード ``.`` を、その名前の上に «» で囲んで示すものとする。

複数のキーワードやステレオタイプ名が適用される場合、(9.2.4) で定義された記法オプ
ションが適用される。

   The subject notation is illustrated by the example in Figure 18.2 which shows
   a Component with the standard stereotype «Subsystem».

上述の ``subject`` classifier についての記法は通常の Classifier のそれとは異なる
ことに注意する。見出しも区画もない。

   Note also that the ``subject`` rectangle does not imply that the ``subject``
   classifier owns the contained UseCases, but merely that the UseCases apply to
   that classifier.

特に、``subject`` である Classifier を表す境界矩形に視覚的には含まれているように
見える UseCase と、所有者である Classifier の区画に視覚的には含まれているように
見える UseCase との間に混同の余地がある (Fig. 18.9)。

属性と操作は通常の Classifier 矩形と同じ内容で、UseCase 楕円内部にある区画らに表
示されることがある。

   ExtensionPoints may be listed in a compartment of the UseCase with the
   heading **extension points**.

各 ExtensionPoint は、次の構文に従い、UseCase の楕円の記号内の文字列で示される：

.. code:: bnf

   <extension point> ::= <name> [: <explanation>]

説明（オプション）：

   Note that *explanation*, which is optional, may be any informal text or a
   more precise definition of the location in the behavior of the UseCase where
   the extension point occurs, such as the name of a State in a StateMachine, an
   Activity in an activity diagram, a precondition, or a postcondition.

UseCases には他の Classifiers に対する Associations や Dependencies を持つことが
ある。例えば入出力、イベント、挙動を表すのに持つ。

UseCase で定義された詳細な挙動は、選択された記述手法に従って、別々の図式または文
書に記録される。

Fig. 18.5 のように、UseCase を Classifiers の標準的な矩形記法を用いて示してもよ
い。その場合は楕円アイコンを矩形右上隅に付ける。この場合、拡張点はオプション区画
だ。この描写は拡張点や特徴が多い場合に適している。

Actor:

   An Actor is represented by a “stick man” icon with the name of the Actor in
   the vicinity (usually above or below) the icon

Actor をすべての区画を通常の記法で、キーワード ``«actor»`` の付いた Classifier
矩形で示してもよい (Fig. 18.8)。

人間以外の Actor には別の図像を使用するなど、Actor の種類を示す他の図像を使用す
ることが許される。

Classifier による UseCase の入れ子（所有）を、Classifier 矩形内に UseCase 楕円を
入れ子にして別の区画で表現してもよい (9.2.4)。

Extend:

   An Extend relationship between UseCases is shown by a dashed arrow with an
   open arrowhead pointing from the extending UseCase towards the extended
   UseCase.

* 矢印のラベルにはキーワード ``«extend»`` が付く。
* Extend の条件とその ExtensionPoints への参照は、その対応する矢印に付けられた
  Comment 記号 (7.2.4) で、オプションとして示される (Fig. 18.3)。

Include:

   An Include relationship between UseCases is shown by a dashed arrow with an
   open arrowhead pointing from the base UseCase to the included UseCase.

* 矢印のラベルにはキーワード ``«include»`` が付く (Fig. 18.4)。

18.1.5 Examples
----------------------------------------------------------------------

   Figure 18.2 Class diagram of a Package owning a set of UseCases, Actors, and
   a Subsystem

UseCases, Actors および UseCases の ``subject`` である Subsystem からなる集合を
所有する Package ``ATMtopPkg`` に対応するクラス図だ。

* この見本では ``subject`` は Subsystem 標準ステレオタイプを持つ Component だ。
* Subsystem ステレオタイプはメタクラスを示す必要はない。その ``subject`` が必然
  的に Component であるからだ (:doc:`./ch22-standard-profile`)。

..

   The example shows that a Customer or Administrator may or may not participate
   in any of their associated UseCases (hence the ``0..1`` multiplicity).

* UseCase としてはこの見本の UseCase すべてにはそれを開始する Actor がなければな
  らない。それゆえ多重度 ``1`` だ。
* ``Deposit`` と ``Register ATM`` UseCases は ``Bank`` の関与を要する。``Bank``
  のほうは同時に多くの ``Deposit`` と ``Register ATM`` UseCases に関与することが
  可能だ。

..

   Figure 18.3 Example Extend

UseCase ``Perform ATM Transaction`` に ExtensionPoint ``selection`` がある。

この UseCase は ``Perform ATM Transaction`` の発生が ``selection`` 拡張点によっ
て参照される場所にあり、顧客が :kbd:`HELP` キーを選択するたびに UseCase
``On-Line Help`` によってその拡張点を介して拡張される。

``Perform ATM Transaction`` UseCase は ``On-Line Help`` UseCase とは別に定義され
る。

   Figure 18.4 Example Include

UseCase ``Withdraw`` は独立して定義された UseCase ``Card Identification`` を含
む。

   Figure 18.5 UseCase using Classifier rectangle notation

楕円図像を持つ Classifiers に対する標準矩形記法とオプションの拡張点区画。

* 矩形右上隅に楕円を描けばよい。
* 区画 ``extension points`` は任意だが、記すときはこのようにする。

   Figure 18.6 Actor notation using stick-man

棒人間を描き、その真下に Actor 名を記す。

   Figure 18.7 Actor notation using Class rectangle

矩形を描き、内部にキーワード ``«actor»`` 付き Actor 名を記す。

   Figure 18.8 Actor notation using icon

図像で Actor を表現する例。見てくれは PC だが Actor 名は ``User`` とある。

   Figure 18.9 Notation for UseCase owned by Classifier

オプションの ``ownedMember`` 区画を使用している Class の ``ownedUseCase`` の見
本。

* ``Make Purchase`` は Class ``DepartmentStore`` の ``ownedUseCase`` だ。
* 区画の名前が ``owned use cases`` となっているが、これは (9.2.4) で規定されてい
  る規則に従い、特性名 ``ownedUseCase`` から導出されるものだ。

   Figure 18.10 Example ATM system with UseCases and Actors

   UseCases need not be owned by their ``subject``.

これは前掲 Fig. 18.10 と同じ機能だ。ここにある UseCases は ``ATMSystem``
Subsystem に適用される。しかし、次の見本で示すように所属が別々のパッケージだ。

   Figure 18.11 Example UseCases owned by Packages

Package の中身が UseCases になっている。

パッケージ ``ATM Services`` がパッケージ ``TransactionUseCases`` を import して
いるので、名前が共通する UseCases が色を変えて描かれている。

   Figure 18.12 Example UseCase with associated StateMachine

左側はその ``ownedBehaviors`` の一つとして StateMachine を持つ UseCase を示す。
この StateMachine の Classifier 記号はオプション区画 ``owned behaviors`` に示さ
れることがある。

右側はこの StateMachine 内部の詳細を表した状態機械図だ。

StateMachine ``Call`` はここでは矩形プラスキーワード ``«statemachine»`` で示され
ている。

18.2 Classifier Descriptions
======================================================================

機械生成による節。

18.3 Association Descriptions
======================================================================

機械生成による節。

.. include:: /_include/uml-refs.txt
