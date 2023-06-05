======================================================================
7 Common Structure
======================================================================

.. contents::
   :depth: 2

7.1 Summary
======================================================================

この章で仕様化するのは UML の全ての構造的モデリングの礎となるモデリング概念。後
続の章で定義していく諸概念の基底となる抽象概念ばかり。

   However, in order to provide examples of how these basic concepts are applied
   in UML, it is necessary to use these concrete modeling constructs, even
   though they are specified in later clauses. Appropriate forward references
   are provided as necessary

7.2 Root
======================================================================

7.2.1 Summary
----------------------------------------------------------------------

   The root concepts of Element and Relationship provide the basis for all other
   modeling concepts in UML.

7.2.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 7.1 Root

初めて見て意味の分からない記法があるならば、前章
(:doc:`./ch06-additional-information`) を再読したほうがいい。

登場するクラスは Element, Relationship, DirectedRelationship, Comment だ。
Comment を除いてすべて抽象クラスだ。

白い鏃の関連はクラスの継承のようなものという解釈で問題ない。いわゆる is-a 関
係、is-a-kind-of 関係だ。

.. admonition:: 読者ノート

   クラス間の関連、図式中の各種矢印が相当する、について、仕様説明が済んでいない
   要素もある。より独立性の高い関連からノートを取っていく。

``A_ownedElement_owner``
  Element から Element への複合関連（双方向）。

    * 両関連端に点が描画されているので、両方向に所有関係がある。

  * Element は他の Element を所有することができるという性質を表現する関連だ。
  * 関連端 ``ownedElement`` の多重度は ``*`` となっている。任意の Element は、ゼ
    ロ個を含む任意の個数の Element を所有できることを意味する。
  * 関連端 ``owner`` の多重度が ``0..1`` となっている。任意の Element について、
    その所有者がないか、または一個だけあることを意味する。
  * 両関連端共通

    * 制約が ``{readOnly, union}`` となっている。これらについては仕様説明が当分
      ないまま話が進む。
    * 関連端名の前に付いている ``+`` についてはアクセスレベルが公開ということ。
    * 関連端名の前に付いている ``/`` については、「この関連端は別の関連端が継承
      するだろう」という意味だった (p. 18)。

      * ``{union}`` と ``/`` が常に同時に関連端に現れることに気づいた。

``A_ownedComment_owningElement``
  Element から Comment への複合関連（単方向）。

  * 関連端 ``ownedComment`` にだけ開いた鏃がある。これは ``owningComment`` か
    らだけ回航可能であることを意味する。``ownedComment`` から ``owningComment``
    には回航不能だ。
  * 関連端 ``ownedComment`` にだけ点がある。ゆえに ``owningComment`` によって
    所有されていることを意味する。
  * あるモデリング要素がコメントされていることを表す関連。
  * 両側関連端に ``{subsets}`` 制約がある。例えば ``ownedComment`` は ``{subsets
    ownedElement}`` となっている。これは «``ownedComment`` is a subset of
    ``ownedElement``» の意味に取る。反対に «``ownedElement`` is a superset of
    ``ownedComment``» が成り立つと推理したい。巧いことに ``ownedElement`` には
    ``{union}`` という制約があったのだった。

    以下、このような条件を当ノートでは「``A_ownedElement_owner`` を subsets す
    る」のように簡略して表記する。

``A_annotatedElement_comment``
  Comment から Element への関連（単方向）。

  * コメントには必ず何かモデリング要素が関連付けられている。
  * 多重度が両側 ``*`` なので、一つの要素に複数のコメントが付されていてよいし、
    複数要素に対して一つのコメントが付されていてもよい。

``A_relatedElement_relationship``
  Relationship から Element への関連（単方向）。

  * この関連の意味は上記 Relationship を参照。
  * 関連端 ``relatedElement`` の多重度が ``1..*`` なので、空でない要素の集まりに
    関係性を定義できる。
  * 両関連端共通

    * ``{readOnly, union}`` だ。
    * プラス記号とスラッシュ記号が関連端名の前に付いている。

``A_source_directedRelationship``, ``A_target_directedRelationship``
  DirectedRelationship から Element への関連。二つの関連をまとめて記す。

  * この関連の意味は上記 DirectedRelationship を参照。
  * 関連端 ``source`` または ``target`` の多重度が ``1..*`` なので、開始点のない
    関係もあり得ないし、終了点のない関係もあり得ない。また、一つの関係において開
    始点が複数あってよいし、終了点が複数あってもよいし、両方共に複数あってもよ
    い。

これ以降の各 Abstract Syntax の節で示される図式については、必要に応じてここで
やったような方法で新規モデリング要素の意味を汲んでいくことにする。

7.2.3 Semantics
----------------------------------------------------------------------

7.2.3.1 Elements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   An Element is a constituent of a model. Descendants of Element provide
   semantics appropriate to the concept they represent.

Element はすべて、他の Elements を所有する能力を有する。ある Element がモデルか
ら取り除かれると、その ``ownedElements`` のすべてもまた必然的にモデルから取り除
かれる。

   Every Element in a model must be owned by exactly one other Element of that
   model, with the exception of the top-level Packages of the model (see also
   Clause 12 on Packages).

孤立したモデル要素があるのは無意味ということだろうか。

7.2.3.2 Comments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Every kind of Element may own Comments.

Element に対する ``ownedComments`` に追加的な意味はないが、モデルの読者にとって
有用な情報を表現することがある。

7.2.3.3 Relationships
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A Relationship is an Element that specifies some kind of relationship between
   other Elements. Descendants of Relationship provide semantics appropriate to
   the concept they represent.

「子孫がそれらのより具体的な概念に応じた意味を与える」という規則は基本規則のよう
だ。以下、省略する。

   A DirectedRelationship represents a Relationship between a collection of
   ``source`` model elements and a collection of target model elements. A
   DirectedRelationship is said to be directed from the ``source`` elements to
   the ``target`` elements.

無向グラフと有向グラフの違いと同じと考えることにする。

7.2.4 Notation
----------------------------------------------------------------------

この仕様書では Abstract Syntax の節で示した図式の各要素の記法を Notation の節で
仕様化することになっている。しかし、今回は Comment 以外全て抽象クラスなので、記
法が存在しない。それゆえ Comment のみ記法の仕様を述べている。

Comment は「右上が折れた紙切れ」のような図形の中に文字列を記すことで示す。
Comment 記号と ``annotatedElements`` の記号それぞれとを破線で結ぶ。周囲の状況か
ら明らかな場合、または図式中で重要でない場合は、この破線を省略してもよい。

7.2.5 Examples
----------------------------------------------------------------------

   Figure 7.2 Comment notation

特筆すべき事項なし。いちおう断っておくと Account と書かれていないほうが Comment
記号だ。

7.3 Templates
======================================================================

原始的なモデリング要素の仕様の直後でなんとテンプレートの話題になる。UML でのテン
プレートは C++ 等の一部プログラミング言語の定義するそれと似た概念なのだろうか。

7.3.1 Summary
----------------------------------------------------------------------

   Templates are model Elements that are parameterized by other model Elements.

この節ではテンプレートすべてに適用される概念を規定するに留め、特定の種類のテンプ
レートについては :doc:`./ch09-classification` と :doc:`./ch12-packages` で記述さ
れる。

7.3.2 Abstract Syntax
----------------------------------------------------------------------

図表が二つに分割されているが、頭の中で混ぜて覚えてよい。以下雑感。

   Figure 7.3 Templates

TemplateableElement, ParameterableElement, TemplateParameter, TemplateSignature
が新登場。すべて Element から直接派生。

   Figure 7.4 Template bindings

TemplateParameterSubstitution, TemplateBinding が新登場。

``A_ownedTemplateSignature_template``
  TemplateableElement から TemplateSignature への複合関連（双方向）。

  * テンプレートの TemplateSignature はある被束縛要素（複数形）内の実際のモデル
    要素に束縛されるTemplateParameters の集合を定義する。
  * ``A_ownedElement_owner`` を subsets する。
  * 関連端 ``ownedTemplateSignature`` の多重度は ``0..1`` だ。

``A_parameter_templateSignature``
  TemplateSignature から TemplateParameter への関連（単方向）。

  * 他の関連のベースとなる関連だ。
  * 関連端 ``parameter`` の多重度が ``1..*`` だ。
  * 制約 ``{ordered}`` が parameter の方についている。つまり個々の
    TemplateParameter が厳密に順序付けられている。

  ``A_ownedParameter_signature``
    * TemplateSignature から TemplateParameter への複合関連（双方向）。
    * 端的に言えば TemplateSignature とは TemplateParameter の順序付き合成集約で
      ある。この関連はまさにそのことを示す。
    * ``A_ownedElement_owner`` と ``A_parameter_templateSignature`` を subsets
      する。
    * 関連端 ``ownedParameter`` は ``{ordered}`` だ。

``A_default_templateParameter``
  TemplateParameter から ParameterableElement への関連（単方向）。

  * 関連端 ``default`` は仮引数 TemplateParameter の既定値？だ。

  ``A_ownedDefault_templateParameter``
    TemplateParameter から ParameterableElement への複合関連（単方向）。

    * TemplateParameter がデフォルト値を与える目的で ParameterableElement を所有
      することを示す関連。
    * ``A_ownedElement_owner`` と ``A_default_templateParameter`` を subsets す
      る。
    * 両関連端の多重度は ``0..1`` だ。

``A_parameteredElement_templateParameter``
  TemplateParameter から ParameterableElement への関連（両方向）。

  * 関連端 ``parameteredElement`` は、この TemplateParameter が晒す (expose) も
    のであることを示す。

  ``A_ownedParameteredElement_owningTemplateParameter``
    * TemplateParameter から ParameterableElement への複合関連（両方
      向）。
    * TemplateParameter がそれを晒す目的で ParameterableElement を所有することを
      示す関連。
    * ``A_ownedElement_owner`` を subsets する。
    * ``A_parameteredElement_templateParameter`` を片側だけ subsets する。もう片
      側の ``templateParameter`` には制約 ``{redefines}`` が付いている。
    * 両関連端の多重度は ``0..1`` だ。

``A_formal_templateParameterSubstitution``
  TemplateParameterSubstitution から TemplateParameter への関連（単方向）。

  * ある TemplateBinding におけるテンプレート引数代入の仮引数のようなものへの参
    照。
  * 関連端 ``formal`` の多重度は 1 だ。

``A_actual_templateParameterSubstitution``
  * TemplateParameterSubstitution から ParameterableElement への関連（単方向）。
  * ある TemplateBinding におけるテンプレート引数代入の実引数のようなものへの参
    照。
  * 関連端 ``actual`` の多重度は 1 だ。

  ``A_ownedActual_owningTemplateParameterSubstitution``
    TemplateParameterSubstitution から ParameterableElement への複合関連（単方
    向）。

    * 実際に ParameterableElement オブジェクトを所有する意味がある関連。
    * 関連 ``A_ownedElement_owner`` を subsets する。
    * 関連 ``A_actual_templateParameterSubstitution`` の ``actual`` と
      ``templateParameterSubstitution`` をそれぞれ subsets と redefines する。

``A_parameterSubstitution_templateBinding``
  TemplateBinding から TemplateParameterSubstitution への複合関連（双方向）。

  * TemplateBinding は TemplateParameterSubstitution を一つ所有する。
  * 関連 ``A_ownedElement_owner`` を subsets する。

``A_templateBinding_boundElement``
  TemplateableElement から TemplateBinding への複合関連（双方向）。

  * TemplateableElement がこの TemplateBinding による束縛要素であることを示す。
  * 関連 ``A_ownedElement_owner`` と ``A_source_directedRelationship`` を
    subsets する。

``A_signature_templateBinding``
  TemplateParameterSubstitution から TemplateSignature への関連（単方向）。

  * 関連端 ``signature`` はこの TemplateBinding のターゲットテンプレートのための
    ものだ。
  * 関連 ``A_target_directedRelationship`` を subsets する。

7.3.3 Semantics
----------------------------------------------------------------------

7.3.3.1 Templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A TemplateableElement is an Element that can optionally be defined as a
   template and bound to other templates. A template is a TemplateableElement
   that is parameterized using a TemplateSignature. Such a template can be used
   to generate other model Elements using TemplateBinding relationships.

:dfn:`テンプレート` とは TemplateSignature を用いて TemplateableElement を引数化
したものだ。このようなテンプレートは TemplateBinding 関係を用いて、他のモデル要
素を生成するのに利用することが可能だ。

テンプレートは同種の非テンプレート Element と同じやり方で利用することが不可能。
（例：テンプレート Class は TypedElement の ``type`` としては使用不能）。

   The template Element can only be used to generate bound Elements or as part
   of the specification of another template (e.g., a template Class may
   specialize another template Class).

テンプレートの TemplateSignature は、テンプレートの被束縛要素で実際のモデル
Elements に束縛されてよい TemplateParameter の集合を定義する。

:dfn:`被束縛要素 (a bound element)` とは、一つまたはそれ以上のそのような
TemplateBindings を有する TemplateableElement のことだ。

:dfn:`完全被束縛要素 (completely bound element)` とは、その TemplateBinding すべ
てが、束縛されているテンプレートの TemplateParameter すべてを束縛する被束縛要素
だ。

   A completely bound element is an ordinary element and can be used in the same
   manner as a non-bound (and non-template) element of the same kind. For
   example, a completely bound element of a Class template may be used as the
   type of a Typed Element.

A partially bound element is a bound element at least one of whose
TemplateBindings does not bind a TemplateParameter of the template being bound.
A partially bound element is still considered to be a template, parameterized by
the remaining TemplateParameters left unbound by its TemplateBindings.

:dfn:`部分的被束縛要素 (partially bound element)` とは、TemplateBindings のうち
少なくとも一つは束縛されるテンプレートの TemplateParameter を束縛しない被束縛要
素だ。

   A partially bound element is still considered to be a template, parameterized
   by the remaining TemplateParameters left unbound by its TemplateBindings.

7.3.3.2 Template Signature
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   The TemplateParameters for a TemplateSignature specify the formal parameters
   that will be substituted by actual parameters (or the default) in a binding.

TemplateParameter は、その TemplateParameter が含まれる TemplateSignature を所有
するテンプレート内にある ParameterableElement という観点から定義されている。この
ような要素は TemplateParameter によって公開されている (*exposed*) と言う。

* 露出した ParameterableElement を、そのテンプレートが直接間接を問わず所有するこ
  ともあれば、テンプレートモデル内で所有関係がない場合には TemplateParameter 自
  身が所有することもある。
* ParameterableElement はテンプレートの文脈でしか意味を持たず、束縛の文脈では実
  際の Element に置換される。したがって、TemplateParameter によって公開される
  ParameterableElement は、その所有するテンプレートや、元のテンプレートの内部に
  アクセスできる他のテンプレート（テンプレートが特殊化されている場合など）の外部
  で参照することは不可能だ。

   Subclasses of TemplateSignature can also add additional rules that constrain
   what sort of ParameterableElement can be used for a TemplateParameter in the
   context of a particular kind of template.

これはテンプレートプログラミングを考えると納得が行く仕様だ。

   A TemplateParameter may also reference a ParameterableElement as the ``default``
   for this formal parameter in any TemplateBinding that does not provide an
   explicit TemplateParameterSubstitution for the parameter.

公開された ParameterableElement 同様、既定の ParameterableElement は、テンプレー
トが直接所有するか、TemplateParameter 自身が所有するか、どちらかだ。公開されてい
る ParameterableElement が TemplateParameter によって所有されていない場合で
も、TemplateParameter はこの ``default`` ParameterableElement を所有することが許
される。

7.3.3.3 TemplateBinding
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TemplateBinding の定義は次のとおり。実引数と仮引数に関わる：

   A TemplateBinding is a relationship between a TemplateableElement and a
   template that specifies the substitutions of ``actual`` ParameterableElements
   for the ``formal`` TemplateParameters of the template.

A TemplateParameterSubstitution の定義だ：

   A TemplateParameterSubstitution specifies the ``actual`` parameter to be
   substituted for a ``formal`` TemplateParameter within the context of a
   TemplateBinding. If no actual parameter is specified in this binding for a
   formal parameter, then the default ParameterableElement for that formal
   TemplateParameter (if specified) is used.

束縛で ``formal`` 引数に ``actual`` 引数が指定されない場合、その仮
TemplateParameter の ``default`` ParameterableElement が指定されていれば用いられ
る。

テンプレート展開の一般原則：

   The details of how the expansions of multiple bindings, and any other
   Elements owned by the bound element, are combined together to fully specify
   the bound element are specific to the subclasses of TemplateableElement. The
   general principle is that one evaluates the bindings in isolation to produce
   intermediate results (one for each binding), which are then merged to produce
   the final result. It is the way the merging is done that is specific to each
   kind of TemplateableElement.

TemplateableElement は TemplateSignature と TemplateBindings の両方を含んでよ
い。それゆえ TemplateableElement はテンプレートと被束縛要素の両方であってよい。

適合性のあるツールは ``formal`` TemplateParameters のすべてが TemplateBinding の
一部として束縛されねばならない（完全束縛）ことを求めてもよいか、``formal``
TemplateParameters の部分集合だけを束縛する（部分束縛）ことを認めるかもしれな
い。

   In the case of complete binding, the bound element may have its own
   TemplateSignature, and the TemplateParameters from this can be provided as
   actual parameters of the TemplateBinding. In the case of partial binding, the
   unbound formal TemplateParameters act as formal TemplateParameters of the
   bound element, which is thus still a template.

注意として、``default`` がある TemplateParameter は、それに対する暗黙の束縛があ
るので、明示的に TemplateParameterSubstitution が与えられていなくてもいつでも束
縛されている。

7.3.3.4 Bound Element Semantics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TemplateBinding は、対象 TemplateSignature を所有するテンプレートの内容が被束縛
要素に複製され、正式な TemplateParameters として公開された ParameterableElement
が、TemplateBinding で実際のテンプレート引数として指定された対応する
ParameterableElement で置き換えられるかのような整形制約と意味を持つことを含意す
る。しかし：

   However, a bound element does not explicitly contain the model Elements
   implied by expanding the templates to which it binds. Nevertheless, it is
   possible to define an *expanded bound element* that results from actually
   applying the TemplateParameterSubstitution for a bound element to the target
   templates.

形式上、単一の TemplateBinding を使い、その束縛以外の Elements のない被束縛要
素に対する拡張被束縛要素は次のように構成される：

#. TemplateBinding の対象である TemplateSignature に関連付けられたテンプレートを
   複製する。モデル Element の複製は、元モデル Element と同じメタクラスのインス
   タンスで次の状態のものだ：

   a. すべての複合プロパティーの値で、元 Element の対応する値の複製（同じ意味）
      であるもの。
   b. ただし、元要素が（直接または間接的に）所有する要素への参照は、上記の規定に
      従って作成された要素の複製への参照に置き換え、元要素自体への参照は、複製へ
      の参照に置き換えられる。
#. 複製にテンプレートである Elements がある場合は、同じ TemplateBinding を使用し
   て、Generalization 関係を ``general`` 要素の等価な被束縛要素に転送する。複製
   先がテンプレートである関連メソッドを持つ Operation である場合、その
   ``method`` を同じテンプレート束縛を使用して、同等の被束縛要素に置き換える。

      The ``types`` of the ``method`` Parameters thus need to be separately
      templated to match the template parameterization of the Operation.

#. 複製が直接または間接的に所有する各 Element に対して、複製の TemplateParameter
   の ``parameteredElement`` への参照を、TemplateBinding の引数に関連付けられた
   ``actual`` Element への参照に置き換える。もし ``actual`` Element がそれ自体
   TemplateBinding を持つ場合、同等の被束縛 Element を参照する。
#. 複製 TemplateSignature から TemplateBinding で参照されているすべての
   TemplateParameters を削除する。もしこれで TemplateSignature からすべての
   TemplateParameters が削除されるようならば、TemplateSignature を完全に削除す
   る。

被束縛要素に一個を超える TemplateBinding があれば、それぞれの TemplateBinding に
基づいて特定の拡張被束縛 Element を定義することが可能だ：

   The overall expanded bound element is then constructed by merging all the
   TemplateBinding-specific expanded bound elements with any other Elements
   contained by the original bound element.

前述のように、このマージは被束縛 TemplateableElement の種類に依存する。

被束縛要素をモデルに含めることは、対応する拡張結合要素が自動的にモデルに含まれる
ことを要求しない。

他方で、Namespace テンプレートの被束縛要素では、Namespace そのものとみなされる
被束縛要素の ``members`` が参照可能である必要があるかもしれない。

   For example, for a bound element of a Class template, it may be necessary to
   reference Operations of that Class, e.g., from a CallOperationAction.

こういう状況に対応するために、被束縛要素自身に加えて、被束縛要素の拡張被束縛要素
をモデルに含めても差し支えない。

7.3.4 Notation
----------------------------------------------------------------------

TemplateableElement の記法。TemplateableElement に TemplateParameter があれば、
まずは小さい破線の矩形をその要素の右上に置く。破線矩形は TemplateParameter の仮
引数リストを含む。空であってはならない。

----

TemplateParameter の記法。CSV で記すか、一行に一つの仮引数を示す。

.. code:: bnf

   <template-parameter> ::= <template-param-name> [':' <parameter-kind> ] ['=' <default>]

ここで *<parameter-kind>* は公開要素のメタクラス名。 *<template-param-name>* と
*<default>* の構文は ParameteredElement の種類による。

----

被束縛要素の記法は、その種類の他の要素のそれと同じ表記とする。

----

TemplateBinding の記法。破線矢印で示す。

* 始点は被束縛要素
* 終点はテンプレート
* キーワード ``«bind»`` を付す。

束縛情報を CSV で記してよい：

.. code:: bnf

   <template-param-substitution> ::= <template-param-name> ‘->’ <actual-template-parameter>

この構文は仮 TemplateParameter の ``parameteredElement`` の ``name`` または
``qualifiedName`` であり、 ``<actual-template-parameter>`` の種類はその
TemplateParameter に対する ParameteredElement の種類によって異なる。

被束縛要素の束縛の代替表現

   An alternative presentation for the bindings for a bound element is to
   include the binding information within the notation for the bound element.
   The name of the bound element is extended to contain binding expressions with
   the following syntax:

   .. code:: bnf

      [<element-name> ‘:’] <binding-expression> [‘,’ <binding-expression>]*
      <binding-expression> ::= <template-element-name> ‘<‘ <template-param-substitution> [‘,’<template-param-substitution]*‘>’

   and *<template-param-substitution>* is defined as above.

7.4 Namespaces
======================================================================

7.4.1 Summary
----------------------------------------------------------------------

   A Namespace is an Element in a model that contains a set of NamedElements
   that can be identified by ``name``.

Namespace には次のようなものがある：

* Package
* 名前付き Feature
* 入れ子になっている Classifier
* 名前付き Parameter を含む BehavioralFeature

7.4.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 7.5 Namespaces

新登場の記号がいくつかある。

  * VisibilityKind 内の ``«enumeration»`` という記法
  * PackageableElement 内の属性 ``visibility`` の説明が込み入っている。

``A_member_memberNamespace``
  Namespace から NamedElement への関連（単方向）。

  いずれの関連端も ``{readOnly, union}`` かつ多重度が ``*`` だ。

  ``A_ownedMember_namespace``
    Namespace から NamedElement への複合関連（双方向）。

    * ``A_member_memberNamespace`` と ``A_ownedElement_owner`` を subsets してい
      る。
    * 関連端 ``namespace`` の多重度は ``0..1`` になっている。

    ``A_ownedRule_context``
      * Namespace から Constraint への複合関連（双方向）。
      * 関連端 ``context`` の多重度 ``0..1`` に対して、関連端 ``ownedRule`` の多
        重度が ``*`` の関係がある。

  ``A_importedMember_namespace``
    Namespace から PackageableElement への関連（単方向）。

``A_elementImport_importingNamespace``, ``A_packageImport_importingNamespace``
  Namespace から ElementImport, PackageImport それぞれへの複合関連（双方向）。

  * Namespace は他の Namespaces から NamedElements をインポートしてよい。
  * ``A_ownedElement_owner``, ``A_source_directedRelationship`` を subsets して
    いる。関連端 ``importingNamespace`` 側が ``source`` かつ ``owner`` だ。

``A_importedElement_import``, ``A_importedPackage_packageImport``
  前者は ElementImport から PackageableElement への関連（単方向）、後者は
  PackageImport から Package への関連（単方向）。

  * ``A_target_directedRelationship`` を subsets している。

``A_nameExpression_namedElement``
  NamedElement から StringExpression への複合関連（単方向）

  * NamedElement は高々一個の StringExpression を所有できる。

    * テンプレート中では NamedElement には、その subexpressions が
      TemplateParameters が晒す ParameterableElement である関連 StringExpression
      があってよい。

  NamedElement には特性の ``name`` と関連端の ``nameExpression`` の両方があって
  もよい。この場合 ``name`` はその NamedElement の別名として用いることが可能。

  * ``A_ownedElement_owner`` を subsets する。

同時に VisibilityKind を仕様化している。四つの可視性タイプからなる。

7.4.3 Semantics
----------------------------------------------------------------------

7.4.3.1 Namespaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Namespace は NamedElements の入れ物を与えるものであり、これを ``ownedMembers``
と呼ぶ。

* Namespace は他のそれから NamedElement をインポートすることが許される。その場合、
  ``ownedMembers`` とともにインポート対象 Namespace の ``members`` となる。
* ``N`` という ``name`` の Namespace の ``member`` が ``x`` という ``name`` を持
  つNamedElement であるとする。このとき、その ``member`` を ``N::x`` の形式の修
  飾名 (*qualified name*) により参照することが可能だ。

区別が必要なときには、Namespace 名で修飾されていない簡素な名前を非修飾名と呼ぶ。

* Namespace 内部では、ここにある構成員や外部にある非隠蔽名を非修飾名で用いること
  が許される。
* 外部名とは、NamedElement の名前であり、Namespace に隣接する非修飾名で参照され
  ることが許される。外部名は内側の Namespace のすべてのメンバーから区別できるも
  のでない限り、隠蔽される。

Namespace はそれ自身 NamedElement であるので、NamedElement の完全修飾名は、例え
ば ``N1::N2::x`` のように Namespace 名を複数含んでよい。

Namespace に対する ``ownRule`` Constraints は、制約付き要素に対する整形規則を表
す。

   These constraints are evaluated when determining if the constrained elements
   are well-formed.

7.4.3.2 Named Elements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A NamedElement is an Element in a model that may have a ``name``. The
   ``name`` may be used for identification of the NamedElement within Namespaces
   where its name is accessible.

NamedElement の ``name`` はオプションであり、名前がない可能性を与える（空の名前
とは異なる）。

NamedElement を他のものと区別する方法を指定する規則に従えば、Namespace 内に
NamedElement を表示することができる。既定規則では、

* 二つの ``member`` が異なる ``name`` を持っているか、
* 同じ ``name`` であってもそれらのメタクラスが異なり、
* どちらも他方の（直接または間接）サブクラスでない

場合に区別可能だ。 この規則は、署名によって区別される Operation などの特定のケー
スで上書きすることが許される。

NamedElement の可視性は Namespace または Elementへのアクセスにおいて、Element の
使用法を制限する手段を与えるものだ。これは、インポート、一般化、およびアクセス機
構と組み合わせて用いることを意図している。

NamedElement には明示的な ``name`` があることに加えて、NamedElement を表す計算さ
れた名前を指定するのに用いられる StringExpression に関連付けてもかまわない。テン
プレートでは、NamedElement は関連する StringExpression を持ち、その部分式は
TemplateParameters によって公開される ParameteredElement であることが許される。
テンプレートが束縛されるとき、公開された部分式は TemplateParameters に代入された
実際の式で置換される。StringExpression の値は部分式の値を連結した結果の文字列と
なり、NamedElement の名前となる。

NamedElement には ``name`` と ``nameExpression`` の両方が関連付けられていてもよ
い。この場合、``name`` のほうは NamedElement の別名として使用することができ、例
えば Constraint 式でその要素を参照する際に使用することができる。

   This avoids the need to use StringExpressions in textual surface notation,
   which is often cumbersome, although it does not preclude it.

7.4.3.3 Packageable Elements and Imports
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A PackageableElement is a NamedElement that may be owned directly by a
   Package (see Clause 12 on Packages). Any such element may serve as a
   TemplateParameter (see sub clause 7.3 on Templates).

* Package については :doc:`./ch12-packages` 参照。
* ParameterableElement でもあるので、TemplateParameter としても使える。

   An ElementImport is a DirectedRelationship between an importing Namespace and
   a PackageableElement.

* ElementImport はその PackageableElement の名前をインポート対象 Namespace に追
  加するものだ。
* ElementImport の可視性は、インポートしている側の要素のそれと同じか、より制限さ
  れる。

インポートする側の Namespace の外部名と名前が衝突する場合、外部名は
ElementImport によって隠蔽され、非修飾名はインポートした要素を指す。外部名は修飾
名でアクセス可能。

   A PackageImport is a DirectedRelationship between an importing Namespace and
   a Package, indicating that the importing Namespace adds the names of the
   ``members`` of the Package to its own Namespace.

概念的には Package のインポートは、別に定義された ElementImport がない限り、イン
ポートされた Namespace の ``member`` それぞれに対して ElementImport があるのと同じだ。

ある Element に対する ElementImport がある場合、PackageImport による同じ Element
のインポートの可能性よりも優先される。

ElementImports または PackageImports の結果として、区別できない Element が
Namespace にインポートされる場合、その Element はインポートする Namespace に追加
されず、その Namespace で使用するためにそれらの Element の ``name`` を修飾する必
要がある。また、

   If the ``name`` of an imported Element is indistinguishable from an Element
   owned by the importing Namespace, that Element is not added to the importing
   Namespace and the ``name`` of that Element must be qualified in order to be
   used.

インポート形態で構成員の可視性が変わる。

   An Element that is publicly imported is a public member of the importing
   Namespace.

Namespace が Package である場合、他の Namespace がそれを PackageImportする
と、Package の公開 ``ownedMembers`` に加えて、それらの公開 import された構成員が
他の Namespace に追加的にインポートされることを意味する。

Namespace はそれ自身をインポートすることはできず、またそれ自身の ``ownMembers``
をインポートすることもできない。これは、NamedElement がその所有 Namespace で別名
を取得することは不可能であることを意味する。

7.4.4 Notation
----------------------------------------------------------------------

7.4.4.1 Namespaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Namespace には一般的な記法はない。特別な種類のものに固有の記法がある。

7.4.4.2 Name Expressions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   The nameExpression associated with a NamedElement can be shown in two ways,
   depending on whether an alias is required or not.

* 別名なしの場合、StringExpression がモデル Element の名前として現れる。
* 別名ありの場合、StringExpression と別名の両方が現れる。別名、StringExpression
  の順に上下に並ぶ。

いずれの場合も StringExpression はドルマーク ``$`` に挟んで表す。

7.4.4.3 Imports
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PackageImport または ElementImport は頭が開いた破線矢印で表現する。

* 可視性が公開の場合は ``«import»`` を付す。さもなくば ``«access»`` を付す。
* このキーワードの後または下に ``alias`` を示してもよい。
* ElementImport のインポートされた要素が Package の場合、キーワードの前に
  ``«element import»`` を任意に付けることができる。

破線による表記の代替として、一意に識別するテキストを示せる。PackageImport のテキ
スト記法は：

.. code:: bnf

   ‘{import ’ <qualified-name> ‘}’ | ‘{access ’ <qualified-name> ‘}’

ElementImport のテキスト記法は：

.. code:: bnf

   ‘{element import’ <qualified-name> ‘}’ | ‘{element access ’ <qualified-name> ‘}’

``alias`` がある場合には、それを示してもよい：

.. code:: bnf

   ‘{element import ’ <qualified-name> ‘ as ’ <alias> ‘}’ | ‘{element access ’ <qualified-name> ‘as’ <alias> ‘}’

7.4.5 Examples
----------------------------------------------------------------------

7.4.5.1 Name Expressions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Figure 7.6 Template package with string parameters

* テンプレートの記法例も兼ねている。
* 図の上側大枠が Package テンプレート ResourceAllocation というものを示す。
* パッケージ右上の三行が TemplateParameter の記法例。

  * パラメーター Resource と ResourceKind の型？が StringExpression だ。

* ``$a<Resource>Allocation$`` 等のテキストが NamedElement/StringExpression の記
  法例。
* 図の下側の ``«bind»`` リストが TemplateParameterSubstitution の記法例。
  StringExpression の値は普通の文字列のようだ。

7.4.5.2 Imports
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Figure 7.7 Example of element import

下側の矢印およびその付随記号が ElementImport の記法例となる。

   Figure 7.8 Example of element import with aliasing

こちらも ElementImport の記法例で「別名付き」だ。

   Figure 7.9 Examples of public and private package imports

PackageImport の記法例だ。矢印の頭の位置が先程と異なる。

7.5 Types and Multiplicity
======================================================================

型と多重度を同じタイミングで仕様化する。

7.5.1 Summary
----------------------------------------------------------------------

型と多重度は値を含む Element の宣言において、含まれることが許される値の種類と個
数に制約をかけるために用いられる。

7.5.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 7.10 Abstract syntax of types and multiplicity elements

新規クラス TypedElement, Type, MultiplicityElement はすべて抽象。

``A_type_typedElement``
  TypedElement から Type への関連（単方向）。

  * 関連端 ``type`` の多重度は ``0..1`` だ。
  * これは TypedElement のとる値の Type が与えられているかどうかを意味する。
    言語にもよるだろうが、ゼロの場合は任意の型の値になれるようだ。

``A_lowerValue_owningLower``, ``A_upperValue_owningUpper``
  MultiplicityElement から ValueSpecification への複合関連（単方向）。

  * ValueSpecification の仕様は :doc:`./ch08-values` にて。
  * ``A_ownedElement_owner`` を subsets する。
  * 属性値の ``lower``, ``upper`` とは別に関連端 ``lowerValue``, ``upperValue``
    がある。

7.5.3 Semantics
----------------------------------------------------------------------

7.5.3.1 Types and Typed Elements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A Type specifies a set of allowed values known as the instances of the Type.

* Type の種類に応じて、そのオブジェクトは生成されたり破壊されたりする。
* UML における Type はすべて Classifiers だ。:doc:`./ch09-classification` 参照。

   A TypedElement is a NamedElement that, in some way, represents particular values.

* TypedElement の種類としては ValueSpecification や StructuralFeature などがあ
  る。:doc:`./ch08-values` や :doc:`./ch09-classification` を参照。
* TypedElement に関連 Type があれば、TypedElement が表現する値は与えられた Type
  のオブジェクトであるものとする。関連 Type がない TypedElement はどんな値でも表
  現してよい。

7.5.3.2 Multiplicities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A MultiplicityElement is an Element that may be instantiated in some way to
   represent a collection of values.

MultiplicityElement の例としては StructuralFeature や Variable がある。

* MultiplicityElement の多重度とは、それが表す集まりの有効な濃度を指定する（数
  だ）。
* 多重度は濃度に対する制約であり、多重度に対して指定された下限・上限より小さく・
  大きくはならない（多重度が無制限の場合、つまり上限に対する制約がない場合を除
  く）。

MultiplicityElement の多重度を表す ``lower`` および ``upper`` は
ValueSpecifications により指定され、``lowerBound`` に対しては Integer 値を、
``upperBound`` に対しては UnlimitedNatural 値を評価する必要がある。

   A MultiplicityElement is multivalued if it has an upperBound greater than 1
   (including unbounded). A MultiplicityElement that is not multivalued can
   represent at most a single value.

MultiplicityElement は境界値が両方ともゼロである多重度を定義することが可能だ。
この要素のオブジェクト化には値を含まないことが要求される。

   If the MultiplicityElement is specified as ordered (i.e., ``isOrdered`` is
   true), then the collection of values in an instantiation of this Element is
   ordered. This ordering implies that there is a mapping from positive integers
   to the elements of the collection of values.

MultiplicityElement が多値でない場合、``isOrdered`` の値は意味的に影響を及ぼさな
い。

   If the MultiplicityElement is specified as unique (i.e., ``isUnique`` is
   true), then the collection of values in an instantiation of this Element must
   be unique.

MultiplicityElement が多値でない場合、``isUniqueOrdered`` の値は意味的に影響を及
ぼさない。

   Table 7.1 Collection types for MultiplicityElements

``isOrdered`` と ``isUnique`` の値の組み合わせと、それらに対応するコレクションの
型 (e.g. Set, OrderedSet) との対応表だ。詳しくないが Java のクラス名だろうか。

7.5.4 Notation
----------------------------------------------------------------------

7.5.4.1 Multiplicity Element
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MultiplicityElement の記法は体が覚えていると思う：

.. code:: bnf

   <lower-bound> ‘..’ <upper-bound>

厳密に言えば MultiplicityElement は抽象クラスなので記法はないとみなしたい。
その各具象サブクラス固有の記法の定義があるというのが正しい。

``<lower-bound>`` は Integer 型の ValueSpecification で、``<upper-bound>`` は
UnlimitedNatural 型の ValueSpecification だ。星形文字 ``*`` は、無制限の上限を表
す多重度指定の一部として使用される。

   If the lower bound is equal to the upper bound, then an alternate notation is
   to use a string containing just the upper bound.

* 例：``1`` は ``1..1`` の意味に取る。
* 例：``*`` は ``0..*`` の意味に取る。

   The specific notation for the ordering and uniqueness specifications may vary
   depending on the specific kind of MultiplicityElement. A general notation is
   to use a textual annotation containing “ordered” or “unordered” to define the
   ordering, and “unique” or “nonunique” to define the uniqueness.

.. code:: bnf

  <multiplicity> ::= <multiplicity-range> [ [ ‘{‘ <order-designator> [‘,’ <uniqueness-designator> ] ‘}’ ] |
  [ ‘{‘ <uniqueness-designator> [‘,’ <order-designator> ] ‘}’ ] ]
  <multiplicity-range> ::= [ <lower> ‘..’ ] <upper>
  <lower> ::= <value-specification>
  <upper> ::= <value-specification>
  <order-designator> ::= ‘ordered’ | ‘unordered’
  <uniqueness-designator> ::= ‘unique’ | ‘nonunique’

7.5.5 Examples
----------------------------------------------------------------------

   Figure 7.11 Multiplicity within a textual specification

Customer というクラス記号の図式。

* 属性名のすぐ後ろに多重度テキストが現れる見本。
* 角括弧に多重度を書き込む記法は、まるで配列のそれに見える。
* ``{ordered, unique}`` 等にも注意したい。

   Figure 7.12 Multiplicity as an adornment to a symbol

上述の図式と等価なモデルを関連で表記したもの。こちらのほうが見やすい。

7.6 Constraints
======================================================================

7.6.1 Summary
----------------------------------------------------------------------

   A Constraint is an assertion that indicates a restriction that must be
   satisfied by any valid realization of the model containing the Constraint. A
   Constraint is attached to a set of ``constrainedElements``, and it represents
   additional semantic information about those Elements.

よくわからない記述だ。

7.6.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 7.13 Abstract Syntax of Constraints

クラス Constraint とその関連だけを仕様化するようだ。

``A_constrainedElement_constraint``
  Constraint から Element への関連（単方向）。

  * 関連端 ``constrainedElement`` の多重度は ``*`` だ。
  * この ``constrainedElement`` が「制約が付随する対象」だ。

``A_specification_owningConstraint``
  Constraint から ValueSpecification への複合関連（単方向）。

  * ``A_ownedElement_owner`` を subsets する。
  * 一つの Constraint が一つの ValueSpecification を所有する。具体的に言うと
    ``specification`` は「制約が満足されているかどうかを示す値」なので、値として
    は ``true`` か ``false`` をとる。

``A_ownedRule_context``
  前述の通り。

7.6.3 Semantics
----------------------------------------------------------------------

   The specification of a Constraint is given by a ValueSpecification (see
   Clause 8) of type Boolean. The computation of the specification may reference
   the ``constrainedElements`` of the Constraint and also the context of the
   Constraint.

一般に、Constraint の ``context`` には種類が多くある。Constraint の ``context``
は Constraint ``specification`` が評価されるタイミングを決定する。例えば、
Operation の ``precondition`` である Constraint は Operation の呼び出しの開
始時に評価され、``postcondition`` である Constraint は、呼び出しの終了時に評価
される。(9.6)

   A Constraint is evaluated by evaluating its ``specification``.

それが真と評価された場合、その時点で Constraint が満たされる。偽と評価された場
合、Constraint は満たされず、評価が行われたモデルの実現は有効ではない。

7.6.4 Notation
----------------------------------------------------------------------

   Certain kinds of Constraints are predefined in UML, others may be
   user-defined.

基本的には中括弧とブーリアン式を組み合わせた表記になる：

.. code:: bnf

   <constraint> ::= ‘{‘ [ <name> ‘:’ ] <boolean-expression> ‘ }’

ここで、``<name>`` は Constraint の名前、``<boolean-expression>`` は Constraint
``specification`` に適したテキスト表記だ。

最も一般的には、制約文字列をノート記号の中に配置して、それを
``constrainedElement`` の各記号に破線で結ぶという表記法をとる。

単一の ``constrainedElement``（単一の Class または Association など）に適用され
るConstraint の場合、制約文字列は ``constrainedElement`` の記号の近く、できれば
名前の近くに直接配置してもよい（ある場合）。ツールは ``constrainedElement`` を決
定することができるようにしなければならない。

属性など、テキスト文字列の記法をとる Element の場合はその文字列のすぐ後に配置し
てもよい。そのように注釈された Element は Constraint の単一 constrainedElement
となる。

   For a Constraint that applies to two Elements (such as two Classes or two
   Associations), the Constraint may be shown as a dashed line between the
   Elements labeled by the constraint string. (See Figure 7.16 for an example.)

Constraint が二つの Elements の間の破線として示される場合には、一方の端点に鏃を
置いてもかまわない。矢印の方向の意味はこうだ：

   The direction of the arrow is relevant information within the Constraint. The
   Element at the tail of the arrow is mapped to the first position and the
   element at the head of the arrow is mapped to the second position in the
   constrainedElement collection.

同種のパスが三つ以上ある場合 (Generalization, Association, etc.) は、制約文字列は
そのパスすべてを横断する破線に添えてもかまわない。

7.6.5 Examples
----------------------------------------------------------------------

   Figure 7.14 Constraint in a note symbol

ノート記号による Constraint 表記例。

   Figure 7.15 Constraint attached to an attribute

クラスのある属性にその Constraint を示す例。

   Figure 7.16 {xor} constraint

二つの関連に共通する Constraint を示す例。

7.7 Dependencies
======================================================================

7.7.1 Summary
----------------------------------------------------------------------

   A Dependency signifies a supplier/client relationship between model elements
   where the modification of a supplier may impact the client model elements.

影響が一方通行であることが読める。

7.7.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 7.17 Abstract syntax of dependencies

一部テキストが欠けている。

``A_supplier_supplierDependency``
  Dependency から NamedElement への関連（単方向）。

  * ``A_target_directedRelationship`` を subsets する。
  * 関連端 ``supplier`` の多重度は ``1..*`` だ。ゼロではあり得ない。

``A_clientDependency_client``
  Dependency と NamedElement との間の関連（双方向）。

  * ``A_source_directedRelationship`` を subsets する。
  * 関連端 ``client`` の多重度は ``1..*`` だ。ゼロではあり得ない。
  * 関連端 ``clientDependency`` は subsets される予定があるようだ。

``A_mapping_abstraction``
  Abstraction から OpaqueExpression への複合関連（単方向）。

  * 図を見る限り OpaqueExpression によって ``mapping`` を表現する、と解釈でき
    る。
  * ``A_ownedElement_owner`` を subsets する。

7.7.3 Semantics
----------------------------------------------------------------------

7.7.3.1 Dependency
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dependency は ``clients`` の意味が ``suppliers`` なしには完全ではないことを含意
している。

モデル内の Dependency 関係の存在には、いかなる実行時の意味には影響しない。そうい
うものはすべて関連している NamedElement (``client``/``supplier``) の観点から与え
る。

7.7.3.2 Usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A Usage is a Dependency in which one NamedElement requires another
   NamedElement (or set of NamedElements) for its full implementation or
   operation.

Usage は ``client`` の定義または実装による ``supplier`` が用いられるという事実以
外には、``client`` が ``supplier`` をどう用いるかを特定することはない。

7.7.3.3 Abstraction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   An Abstraction is a Dependency that relates two NamedElements or sets of
   NamedElements that represent the same concept at different levels of
   abstraction or from different viewpoints.

この関係性は ``suppliers`` と ``clients`` の間の写像として定義してよい。

``«Derive»``, ``«Refine»``, ``«Trace»`` などの定義済みステレオタイプがある。こ
れは :doc:`./ch22-standard-profile` で仕様化する。

   If an Abstraction has more than one client, the ``supplier`` maps into the
   set of ``clients`` as a group.

例えば、分析水準 Class は設計水準 Class に分割されるかもしれない。このような写像
の状況は ``supplier`` が複数存在する場合も同様だ。

7.7.3.4 Realization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Realization is a specialized Abstraction dependency between two sets of
   NamedElements, one representing a specification (the ``supplier``) and the
   other representing an implementation of that specification (the ``client``).

Realization を段階的な洗練、最適化、変換、テンプレート、モデル合成、フレーム
ワーク合成などをモデル化するために使用することができる。

Realization は ``client`` の集合が、仕様として機能する ``supplier`` の集合の実装
であることを意味する。

「実装」の意味は厳密に定義されているわけではなく、特定のモデリングコンテキストに
関して、より洗練された、または精巧な形式を意味する。

   It is possible to specify a mapping between the specification and
   implementation elements, although this is not necessarily computable.

7.7.4 Notation
----------------------------------------------------------------------

Dependency は破線矢印として示す。

* 矢印は ``client`` から ``supplier`` に向く。
* 矢印のラベルにはオプションとしてキーワード・ステレオタイプを付けてよい。

``clients`` または ``suppliers`` に対する Element の集合を持つことが可能だ。この
場合、一つ以上の矢印の始点と終点が ``clients`` と ``suppliers`` に接続する。お望
みなら破線の接合部に置くことができる。そこに Dependency に関するノートをなるべく
添える。

   A Usage is shown as a Dependency with a «use» keyword attached to it.

   An Abstraction is shown as a Dependency with an «abstraction» keyword or the
   specific predefined stereotype attached to it.

   A Realization is shown as a dashed line with a triangular arrowhead at the
   end that corresponds to the realized Element.

7.7.5 Examples
----------------------------------------------------------------------

   Figure 7.19 An example of an ``«Instantiate»`` Dependency

標準ステレオタイプである ``«Instantiate»`` を適用した Dependency (Usage) だ。
CarFactory のオブジェクトが Car のオブジェクトを作成することを示している。

   Figure 7.20 An example of a ``«use»`` Dependency

Usage の記法例。Order の完全な実装には Line Item を必要とする。

   Figure 7.21 An example of a realization Dependency

Realization の記法例。Business を Owner と Employee の組み合わせで実現した例。見
慣れたクラス図だ。

7.8 Classifier Descriptions
======================================================================

機械生成による節。

7.9 Association Descriptions
======================================================================

機械生成による節。

.. include:: /_include/uml-refs.txt
