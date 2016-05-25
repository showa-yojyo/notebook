======================================================================
7 Common Structure
======================================================================
UML 2.5 pp. 21-68 に関するノート。

.. contents:: ノート目次

7.1 Summary
======================================================================
この章で仕様化するのは UML の全ての構造的モデリングの礎となるモデリング概念。
後続の章で定義していく諸概念の基底となる抽象概念ばかり。

7.2 Root
======================================================================

7.2.1 Summary
----------------------------------------------------------------------
* Element と Relationship が UML の残り全てのモデリング要素の基底である。

7.2.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 7.1 Root

  * 初めて見て意味の分からない記法があるならば、
    前章 (:doc:`./additional-information`) を再読したほうがいい。

  * 登場するクラスは 4 つ。
    Element, Relationship, DirectedRelationship, Comment である。
    Comment を除いてすべて抽象クラスである。

7.2.3 Semantics
----------------------------------------------------------------------
*Element*
  * すべての UML メタクラスの基底クラスである。
  * 他の Element を所有することができるという性質を有する。
  * その特殊なケースなのだが Comment を所有することができる。

*Relationship*
  * 複数 Elements 間のある種の関係性を指定する Element である。
  * 意味はさらなる具象クラスで決まる。

*DirectedRelationship*
  * Relationship の一種で、
    ある Element(s) と別の Element(s) との関係性を表現する。

  * 一方の要素群を source(s) と呼び、他方を target(s) を呼ぶ。
  * 「向きの付いた」というのは、この source から target への向きを意味する。

Comment
  * 読んで字のごとし。
  * Element に付随する情報・説明等を余白に書き込みたくなるが、
    それを正式に仕様化した概念なのだろう。

  * body: コメント本文を表現するための文字列。

.. note::

   クラス間の関連、図式中の各種矢印が相当する、について、
   仕様説明が済んでいない要素もある。
   より独立性の高い関連からノートを取っていく。

   * 白い矢先の関連はクラスの継承のようなものという解釈で問題ない。
     いわゆる is-a 関係、is-a-kind-of 関係である。

A_ownedElement_owner
  * Element から Element への composite 関連（双方向）。

    * 両関連端にドットが描画されているので、両方向に所有関係がある。

  * Element は他の Element を所有することができるという性質を表現する関連である。

  * ある Element がモデルから取り除かれるときには、
    すべての ownedElements もまたそのモデルから取り除かれる必要がある。

  * 関連端 ownedElement の多重度は ``*`` となっている。
    任意の Element は、ゼロ個を含む任意の個数の Element を所有できることを意味する。
    以下同様。

  * 関連端 owner の多重度が ``0..1`` となっている。
    任意の Element について、その所有者がないか、または 1 個だけあることを意味する。
    以下同様。

  * 両関連端共通

    * 制約が ``{readOnly, union}`` となっている。
      これらについては当分仕様説明がないまま話が進む。

    * 関連端名の前に付いている ``+`` については
      アクセスレベルが公開ということ。
      以下同様。

    * 関連端名の前に付いている ``/`` については、
      「この関連端は別の関連端が継承するだろう」という意味だった (p. 18)。
      以下同様。

      * ``{union}`` と ``/`` が常に同時に関連端に現れることに気づいた。

A_ownedComment_owningElement
  * Element から Comment への composite 関連（単方向）。

    * 関連端 ownedComment にだけ開いた矢先を持つ。
      これは owningComment からだけ navigable であることを意味する。
      ownedComment から owningComment には navigable ではない。
      以下同様。

    * 関連端 ownedComment にだけドットがある。
      ゆえに owningComment によって所有されていることを意味する。
      以下同様。

  * あるモデリング要素がコメントされていることを表す関連。

  * 両側関連端に ``{subsets}`` 制約がある。
    例えば ownedComment は ``{subsets ownedElement}`` となっている。
    これは <ownedComment is a subset of ownedElement> の意味に取る。
    反対に <ownedElement is a superset of ownedComment> が成り立つと推理したい。
    上手いことに ownedElement には ``{union}`` という制約があったのだった。

    以下、このような条件を当ノートでは
    「A_ownedElement_owner を subsets する」のように簡略して表記する。

A_annotatedElement_comment
  * Comment から Element への関連（単方向）。
  * コメントには必ず何かモデリング要素が関連付けられている。
  * 多重度が両側 ``*`` なので、
    一つの要素に複数のコメントが付されていてよいし、
    複数要素に対して一つのコメントが付されていてもよい。

A_relatedElement_relationship
  * Relationship から Element への関連（単方向）。
  * この関連の意味は上記 Relationship を参照。
  * 関連端 relatedElement の多重度が ``1..*`` なので、
    空でない要素の集まりに関係性を定義できる。

  * 両関連端共通

    * ``{readOnly, union}`` である。
    * プラス記号とスラッシュ記号が関連端名の前に付いている。

A_source_directedRelationship, A_target_directedRelationship
  * DirectedRelationship から Element への関連。
    ふたつの関連をまとめて記す。
  * この関連の意味は上記 DirectedRelationship を参照。
  * 関連端 source または target の多重度が ``1..*`` なので、
    開始点のない関係もあり得ないし、終了点のない関係もあり得ない。
    また、一つの関係において開始点が複数あってよいし、
    終了点が複数あってもよいし、両方共に複数あってもよい。

これ以降の各 Abstract Syntax の節で示される図式については、
必要に応じてここでやったような方法で新規モデリング要素の意味を汲んでいくことにする。

7.2.4 Notation
----------------------------------------------------------------------
この仕様書では Abstract Syntax の節で示した図式の各要素の記法を
Notation の節で仕様化することになっている。
しかし、今回は Comment 以外全て抽象クラスなので、記法が存在しない。
それゆえ Comment のみ記法の仕様を述べている。

* Comment は「右上が折れた紙切れ」のような図形の中に文字列を記すことで示す。
* Comment シンボルと annotatedElement(s) のシンボルそれぞれとを破線で結ぶ。

  * 周囲の状況から明らかな場合、または図式中で重要でない場合は、
    この破線を隠してもよい。

7.2.5 Examples
----------------------------------------------------------------------
* Figure 7.2 Comment notation

  * 特筆すべき事項なし。

7.3 Templates
======================================================================
原始的なモデリング要素の仕様の直後でなんとテンプレートの話題になる。
UML でのテンプレートは C++ 等の一部プログラミング言語の定義するそれと似た概念なのだろうか。

7.3.1 Summary
----------------------------------------------------------------------
* Template は他のモデル Element によってパラメーター化されるモデル Element である。
* この節ではテンプレート周辺の概念を導入するにとどめ、詳細は
  :doc:`./classification` と 
  :doc:`./packages` に譲る。

7.3.2 Abstract Syntax
----------------------------------------------------------------------
図表が二つに分割されているが、頭の中で混ぜて覚えてよい。以下雑感。

* Figure 7.3 Templates

  * TemplateableElement, ParameterableElement,
    TemplateParameter, TemplateSignature が新登場。
    すべて Element の直接派生クラス。

* Figure 7.4 Template bindings

  * TemplateParameterSubstitution, TemplateBinding が新登場。

7.3.3 Semantics
----------------------------------------------------------------------
*TempleatableElement*
  * Element の一種である。
  * 任意でテンプレートとして定義され、
    他のテンプレートに束縛されることのできる Element である。
    そのようなテンプレートは TemplateBinding という関係を用いて、
    他のモデル要素を生成 (generate) するために利用することが可能。

  * テンプレートは同種の非テンプレート要素と同じやり方で利用することが不可能。
  * テンプレート要素は次のどちらかの目的でのみ利用可能。

    * 被束縛要素を生成する
    * 他のテンプレートの詳細の一部になる

  * TemplateableElement は TemplateSignature と TemplateBindings の両方を含んでよい。
    ゆえに TemplateableElement はテンプレートと被束縛要素の両方であってよい。

*ParameterableElement*
  * Element の一種である。
  * TemplateParameter や TemplateParameterSubstitution によって所有される要素？
  * 露出した ParameterableElement を、そのテンプレートが直接間接を問わず所有してよい。

TemplateSignature
  * Element の一種である。
  * ある TemplateSignature にとっての TemplateParameters は、
    一つの束縛の中で実引数（またはデフォルト）で置換されるであろう仮引数を指定する。

  * テンプレート (template) とは、
    TemplateSignature を用いてパラメーター化された TemplateableElement のことである。

  * TemplateSignature のサブクラスは、
    ある特別な種類のテンプレートの状況下で、
    どの種類の ParameterableElement が TemplateParameter に用いられるのかを
    制約する規則をさらに追加することも可能だ。

TemplateParameter
  * Element の一種である。
  * TemplateParameter はその TemplateParameter が部分となる
    TemplateSignature を所有するテンプレートの内部に含まれる
    ParameterableElement に関して定義される。
    そういう要素はその TemplateParameter によって晒されている (to be exposed) と言われる。

    * もっとよい日本語はないか？

TemplateParameterSubstitution
  * <A TemplateParameterSubstitution
    specifies the actual parameter to be substituted for a formal
    TemplateParameter within the context of a TemplateBinding>(p. 24)

TemplateBinding
  * TemplateableElement からテンプレートへの DirectedRelationship である。
  * TemplateBinding はそのテンプレートの仮引数 (formal parameter) に代入する
    実引数 (actual parameter) の TemplateParameterSubstitutions を指定する。

  * テンプレートの TemplateSignature は
    現実のモデル Elements に束縛されてよい TemplateParameters の集合を一つ定義する。

    * 被束縛要素 (a bound element) とは、
      一つまたはそれ以上のそういう TemplateBindings を持つ
      TemplateableElement である。

    * 完全被束縛要素 (completely bound element) とは、
      そのすべての TemplateBindings が束縛されているテンプレートの
      TemplateParameter すべてを束縛する被束縛要素である。

    * 部分的被束縛要素 (partially bound element) とは、
      その TemplateBindings のうち少なくとも一つは束縛されているテンプレートの
      TemplateParameter を束縛しない被束縛要素である。

A_ownedTemplateSignature_template
  * TemplateableElement から TemplateSignature への composite 関連（双方向）。
  * テンプレートの TemplateSignature は 
    ある被束縛要素 (pl.) 内の実際のモデル要素に束縛される
    TemplateParameters の集合を定義する。
  * A_ownedElement_owner を subsets する。
  * 関連端 ownedTemplateSignature の多重度は ``0..1`` である。

A_parameter_templateSignature
  * TemplateSignature から TemplateParameter への関連（単方向）。
  * 他の関連のベースとなる関連である。
  * 関連端 parameter の多重度が ``1..*`` である。
  * 制約 ``{ordered}`` が parameter の方についている。
    つまり個々の TemplateParameter が厳密に順序付けられている。

  A_ownedParameter_signature
    * TemplateSignature から TemplateParameter への composite 関連（双方向）。
    * 端的に言えば TemplateSignature とは TemplateParameter の順序付き合成集約である。
      この関連はまさにそのことを示す。
    * A_ownedElement_owner と A_parameter_templateSignature を subsets する。
    * 関連端 ownedParameter は ``{ordered}`` である。

A_default_templateParameter
  * TemplateParameter から ParameterableElement への関連（単方向）。
  * 関連端 default は仮引数 TemplateParameter のデフォルト値？である。

  A_ownedDefault_templateParameter
    * TemplateParameter から ParameterableElement への composite 関連（単方向）。
    * TemplateParameter がデフォルト値を与える目的で
      ParameterableElement を所有することを示す関連。
    * A_ownedElement_owner と A_default_templateParameter を subsets する。
    * 両関連端の多重度は ``0..1`` である。

A_parameteredElement_templateParameter
  * TemplateParameter から ParameterableElement への関連（両方向）。
  * 関連端 parameteredElement は、この TemplateParameter が晒す (expose) ものであることを示す。

  A_ownedParameteredElement_owningTemplateParameter
    * TemplateParameter から ParameterableElement への composite 関連（両方向）。
    * TemplateParameter がそれを晒す目的で
      ParameterableElement を所有することを示す関連。
    * A_ownedElement_owner を subsets する。
    * A_parameteredElement_templateParameter を片側だけ subsets する。
      もう片側の templateParameter には制約 ``{redefines}`` が付いている。
    * 両関連端の多重度は ``0..1`` である。

A_formal_templateParameterSubstitution
  * TemplateParameterSubstitution から TemplateParameter への関連（単方向）。
  * ある TemplateBinding におけるテンプレート引数代入の仮引数のようなものへの参照。
  * 関連端 formal の多重度は 1 である。

A_actual_templateParameterSubstitution
  * TemplateParameterSubstitution から ParameterableElement への関連（単方向）。
  * ある TemplateBinding におけるテンプレート引数代入の実引数のようなものへの参照。
  * 関連端 actual の多重度は 1 である。

  A_ownedActual_owningTemplateParameterSubstitution
    * TemplateParameterSubstitution から ParameterableElement への composite 関連（単方向）。
    * 実際に ParameterableElement オブジェクトを所有する意味がある関連。
    * 関連 A_ownedElement_owner を subsets する。
    * 関連 A_actual_templateParameterSubstitution の
      actual と templateParameterSubstitution をそれぞれ subsets と redefines する。

A_parameterSubstitution_templateBinding
  * TemplateBinding から TemplateParameterSubstitution への composite 関連（双方向）。
  * TemplateBinding は TemplateParameterSubstitution を一つ所有する。
  * 関連 A_ownedElement_owner を subsets する。

A_templateBinding_boundElement
  * TemplateableElement から TemplateBinding への composite 関連（双方向）。
  * TemplateableElement がこの TemplateBinding による束縛要素であることを示す。
  * 関連 A_ownedElement_owner と A_source_directedRelationship を subsets する。

A_signature_templateBinding
  * TemplateParameterSubstitution から TemplateSignature への関連（単方向）。
  * 関連端 signature はこの TemplateBinding のターゲットテンプレートのためのものである。
  * 関連 A_target_directedRelationship を subsets する。

.. todo::

   テンプレートに関する諸概念の意味 (pp. 25-26) を何とかまとめる。

7.3.4 Notation
----------------------------------------------------------------------
* TemplateableElement が TemplateParameters を持つならば、
  まずは小さい破線の矩形をその要素の右上に置く。

  * 破線矩形は TemplateParameters の仮引数リストを含む。
    空であってはならない。

  * この仮引数リストは CSV で記すか、一行に一つの仮引数を示す。

  * 一つの TemplateParameter の記法 <template-parameter> は
    BNF で定義されている (p. 26)。

* 被束縛要素の記法は、その種類の他の要素のそれと同じとする。

* TemplateBinding は破線矢印で示す。

  * 向きは被束縛要素からテンプレートとする。
  * キーワード ``«bind»`` をラベルに付す。
  * 束縛情報 <template-param-substition> を CSV で記してよい。
    BNF で定義されている (p. 26)。

    * 代入の記号として ``->`` を用いる。
      たぶん ``T -> int`` のように書ける。

7.4 Namespaces
======================================================================

7.4.1 Summary
----------------------------------------------------------------------
名前のある要素、名前空間、パッケージ可能な要素、インポート等のモデリング概念を導入する。

7.4.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 7.5 Namespaces

  * 新登場の記号がいくつかある。

    * VisibilityKind 内の ``«enumeration»`` という記法
    * PackageableElement 内の属性 visibility の説明が込み入っている。

7.4.3 Semantics
----------------------------------------------------------------------
*Namespace*
  * NamedElement の集合を所有する NamedElement である。
    これは ownedMember という関連端名で示されている。

  * もし Namespace のある member が N という name を持つ NamedElement ならば、
    その member を N::x の形式の限定名 (qualified name) により参照することが可能である。

    * この手のルールが色々と説明されているが、
      私には自明なのでノートを省略する。

*NamedElement*
  * Element の一種。
  * モデル内の名前を持ってよい要素である。
  * name: この値で NamedElement を見分ける。
  * qualifiedName: 特に所属する名前空間を省略せずに表記するときの名前。
  * visibility: VisibilityKind 型の値。

  * NamedElements は
    ある NamedElement が別のものとどのようにして見分けがつくのかを指定する規則に従って
    Namespace 内に現れてよい。

    * その既定の規則とは、二つの members が見分けがつくのは、
      それらが異なる names を持つか、同じ names を持つかである。

*PackageableElement*
  * Package が直接所有することのできる NamedElement である。

    * Package については :doc:`./packages` 参照。

  * かつ ParameterableElement でもあるので、TemplateParameter としても使える。
  * NamedElement から継承した属性 visibility のデフォルト値は public である？

ElementImport
  * Namespace と PackageableElement との間の DirectedRelationship である。
  * かつ PackageableElement でもある。
  * ElementImport はその PackageableElement の名前をインポート先 Namespace に追加するものである。

    * その ElementImport の可視性は、
      インポート元の要素のそれと同じか、より制限されたものかのどちらかになる。

  * 名前衝突の際には、名前空間の外側の名前が隠蔽される。
    外側のものをアクセスするには限定名を用いることで可能になる。

  * 属性には alias と visibility がある。後者はデフォルトで public である？

PackageImport
  * Namespace と Package との間の DirectedRelationship である。
  * この関係は Namespace が対象の Package の members の名前を、
    自身の Namespace に追加することを意味する。

  * もし見分けの付かない Elements が Namespace にインポートされようとした場合、
    その Elements は対象の Namespace に追加されない。
    それらをそこで用いるためには名前を限定する必要がある。

  * publicly にインポートした Element はインポート先 Namespace の public member である。

  * 属性には visibility がある。デフォルトで public である？

.. note:: ここまで出てきた要素名で、まだ仕様化されていないものがいくつかある。

A_member_memberNamespace
  * Namespace から NamedElement への関連（単方向）。
  * いずれの関連端も ``{readOnly, union}`` かつ多重度が ``*`` である。

  A_ownedMember_namespace
    * Namespace から NamedElement への composite 関連（双方向）。
    * A_member_memberNamespace と A_ownedElement_owner を subsets している。
    * 関連端 namespace の多重度は ``0..1`` になっている。

    A_ownedRule_context
      * Namespace から Constraint への composite 関連（双方向）。
      * 関連端 ownedRules はある Namespace のために
        拘束された要素 (pl.) のための well-formed な規則を表現する。

      * 関連端 context の多重度 ``0..1`` に対して、
        関連端 ownedRule の多重度が ``*`` の関係がある。

  A_importedMember_namespace
    * Namespace から PackageableElement への関連（単方向）。

A_elementImport_importingNamespace, A_packageImport_importingNamespace
  * Namespace から ElementImport, PackageImport それぞれへの composite 関連（双方向）。
  * Namespace は他の Namespaces から NamedElements をインポートしてよい。

  * A_ownedElement_owner, A_source_directedRelationship を subsets している。
    関連端 importingNamespace 側が source かつ owner である。

A_importedElement_import, A_importedPackage_packageImport
  * 前者は ElementImport から PackageableElement への関連（単方向）、
    後者は PackageImport から Package への関連（単方向）。

  * A_target_directedRelationship を subsets している。

A_nameExpression_namedElement
  * NamedElement から StringExpression への composite 関連（単方向）
  * NamedElement は高々 1 個の StringExpression を所有できる。

    * テンプレート中では NamedElement は
      その subexpressions が TemplateParameters が晒す ParameterableElement である、
      関連 StringExpression を持ってよい。

  * NamedElement は property の name と関連端の nameExpression を両方持ってよい。
    この場合、name はその NamedElement の別名として用いることが可能。

  * A_ownedElement_owner を subsets する。

同時に VisibilityKind を仕様化している。4 つの可視性タイプからなる。

7.4.4 Notation
----------------------------------------------------------------------
* Namespace には一般的な記法はない。特別な種類のものに固有の記法がある。
* NamedElement はその nameExpression (StringExpression) で表現する。
  これには別名ありなしで二つの記法がある。
  いずれの場合も StringExpression はドルマーク ``$`` に挟んで表す。

* PackageImport/ElementImport は頭が開いた破線矢印で表現する。

  * visibility = public の場合は ``«import»`` を付す。
    さもなくば ``«access»`` を付す。

  * このキーワードの後または下に alias を示してもよい。

* PackageImport/ElementImport の代替表記として一意に識別するテキストを示せる。
  BNF 記法の仕様が p. 29 にある。

7.4.5 Examples
----------------------------------------------------------------------
* Figure 7.6 Template package with string parameters

  * テンプレートの記法例も兼ねている。

  * 図の上側大枠が Package テンプレート ResourceAllocation というものを示す。
  * パッケージ右上の 3 行が TemplateParameter の記法例。

    * パラメーター Resource と ResourceKind の型？が StringExpression である。

  * ``$a<Resource>Allocation$`` 等のテキストが NamedElement/StringExpression の記法例。

  * 図の下側の ``«bind»`` リストが TemplateParameterSubstitution の記法例。
    StringExpression の値は普通の文字列のようだ。

* Figure 7.7 Example of element import

  * 下側の矢印およびその付随記号が ElementImport の記法例となる。

* Figure 7.8 Example of element import with aliasing

  * こちらも ElementImport の記法例で「別名付き」である。

* Figure 7.9 Examples of public and private package imports

  * PackageImport の記法例である。
    矢印の頭の位置が先程と異なる。

7.5 Types and Multiplicity
======================================================================
型と多重度を同じタイミングで仕様化する。

7.5.1 Summary
----------------------------------------------------------------------
型と多重度は値を含む Element の宣言に用いられる。
そのような値の種類と個数を拘束する目的がある。

7.5.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 7.10 Abstract syntax of types and multiplicity elements

  * 新規クラス TypedElement, Type, Multiplicity はすべて抽象。

7.5.3 Semantics
----------------------------------------------------------------------
ここで仕様化された（抽象）クラスを記す。

*Type*
  * PackageableElement の一種。
  * Type とは、その Type のオブジェクトとして知られている取り得る値の集合を指定するものである。
  * Type の種類に応じて、そのオブジェクトは生成または消滅されてよい。
  * UML における Types はすべて Classifiers である。
    :doc:`./classification` 参照。

*TypedElement*
  * NamedElement の一種。
  * 何らかの手段で特定の値を表現する。
  * TypedElement の種類としては ValueSpecification や StructuralFeature がある。
    :doc:`./values` や :doc:`./classification` を参照。

*MultiplicityElement*
  * Element の一種。
  * 多重度は何らかの手段で値の集まりを表現するために生成される。
  * 属性 isOrdered は値の集まりが順序付けられているか否かを示す。
  * 属性 isUnique は一意な値の集まりか否かを示す。

    * デフォルトが true であることに注意。

  * 属性 lower および upper は多重度の下限および上限を表現する。

    * 値の与え方と読み方についてはもう慣れているのでノートに残さない。
      一つだけ記す。両方ゼロにしてもよい (p. 34)。

    * これらの属性は派生クラスで再定義されることになる。

  * Table 7.1 の isOrdered と isUnique の値の組み合わせと、
    それらに対応するコレクションの型 (e.g. Set, OrderedSet) の名前が面白い。
    詳しくないが Java のクラス名だろうか。

A_type_typedElement
  * TypedElement から Type への関連（単方向）。
  * 関連端 type の多重度は ``0..1`` だ。
  * これは TypedElement のとる値の Type が与えられているかどうかを意味する。
    言語にもよるだろうが、ゼロの場合は任意の型の値になれるようだ。

A_lowerValue_owningLower, A_upperValue_owningUpper
  * MultiplicityElement から ValueSpecification への composite 関連（単方向）。
  * ValueSpecification の仕様は :doc:`./values` にて。
  * A_ownedElement_owner を subsets する。
  * 属性値の lower, upper とは別に関連端 lowerValue, upperValue がある。

7.5.4 Notation
----------------------------------------------------------------------
* MultiplicityElement の記法はこれまでさんざんやっているような気がする。
  ``<lower-bound> '..' <upper-bound>`` というものだ。

  * 厳密に言えば MultiplicityElement は抽象クラスなので記法はないとみなしたい。
    その各具象サブクラス固有の記法の定義があるというのが正しい。

  * 関連端にだけでなく、クラス属性の名前の後にも角括弧付きで記すことができる。
  * より一般的な場合の記法は p. 35 に仕様化されている。

7.5.5 Examples
----------------------------------------------------------------------
* Figure 7.11 Multiplicity within a textual specification

  * Customer というクラスシンボルの図式。
  * 属性名のすぐ後ろに多重度テキストが現れる見本。
  * 角括弧に多重度を書き込む記法は、まるで配列のそれに見える。
  * ``{ordered, unique}`` 等にも注意したい。

* Figure 7.12 Multiplicity as an adornment to a symbol

  * 上述の図式と等価なモデルを関連で表記したもの。

7.6 Constraints
======================================================================
制約を仕様化する。

7.6.1 Summary
----------------------------------------------------------------------
日本語に訳しにくいので丸々引用する。
<A Constraint is an assertion that indicates a restriction that must be
satisfied by any valid realization of the model containing the Constraint>
(p. 35)

7.6.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 7.13 Abstract Syntax of Constraints

  * クラス Constraint とその関連だけを仕様化するようだ。

7.6.3 Semantics
----------------------------------------------------------------------
Constraint
  * PackageableElement の一種である。
  * Constraint の specitication は Boolean 型の ValueSpecification により与えられる。
    その計算には constrainedElements と context を参照してよい。

  * 一般には Constraint の owners としては様々な種類の Elements が考えられる。
    唯一の制限は、所有者である Element は constrainedElements へのアクセスを持つ必要があるということだ。

    * 所有者はいつ Constraint の specitication が評価されるのかを決定する。
      例えばある Operation の precondition である Constraint ならば、
      その操作の発動開始時に評価される。

A_constrainedElement_constraint
  * Constraint から Element への関連（単方向）。
  * 関連端 constrainedElement の多重度は ``* {ordered}`` である。
  * この constrainedElement が「制約が付随する対象」である。

A_specification_owningConstraint
  * Constraint から ValueSpecification への composite 関連（単方向）。
  * A_ownedElement_owner を subsets する。
  * 一つの Constraint が一つの ValueSpecification を所有する。
    具体的に言うと、specification は「制約が満足されているかどうかを示す値」なので、
    値としては true か false をとる。

A_ownedRule_context
  前述の通り。

7.6.4 Notation
----------------------------------------------------------------------
* Constraint の記法には UML 定義のものとユーザー定義のものとがある。
* 基本的には中括弧とブーリアン式を組み合わせた表記になる。
  何なら中括弧の中に（真偽を評価できるならば）自然言語で文を書いても構わないようだ。

* より一般的には、制約文字列をノートシンボルの中に配置して、
  それを constrainedElement の表すシンボルに破線で結ぶという表記法をとる。
* テキスト文字列の記法をとる Element に対しては、
  その文字列のすぐ後に制約文字列を配置してもよい。
* 複数要素に同一 Constraint を示す場合、
  まずそれらの要素間に破線を引き、そのラベルに制約文字列を使う。

7.6.5 Examples
----------------------------------------------------------------------
* Figure 7.14 Constraint in a note symbol

  * ノートシンボルによる Constraint 表記例。

* Figure 7.15 Constraint attached to an attribute

  * クラスのある属性にその Constraint を示す例。

* Figure 7.16 {xor} constraint

  * 二つの関連に共通する Constraint を示す例。

7.7 Dependencies
======================================================================
依存性を仕様化する。

7.7.1 Summary
----------------------------------------------------------------------
* Dependency は要素間の supplier/client 関係を意味する。
  supplier の修正が client に強く影響してよい。

7.7.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 7.17 Abstract syntax of dependencies

  * 一部テキストが欠けている。

7.7.3 Semantics
----------------------------------------------------------------------
Dependency
  * DirectedRelationship かつ PackageableElement の一種である。
  * client の意味が supplier なしには完全ではないことを含意している。
  * モデル内の Dependency 関係の存在は、いかなる実行時の意味を持たない。
    そういうのは関連づいている NamedElement (client/supplier) が与える。

Usage
  * Dependency の一種である。
  * ある NamedElement がその完全な実装や操作のために
    必要とする別の NamedElement(s) があるとき、
    その依存性を表す。

Abstraction
  * Dependency の一種である。
  * ある抽象水準や視点では同じ概念を表現する NamedElements に関係する Dependency のこと？
  * この関係性は suppliers と clients との間の写像として定義してよい。
  * ``«Derive»``, ``«Refine»``, ``«Trace»`` などの定義済みステレオタイプを持つ。
    これは :doc:`standard-profile` で仕様化する。

Realization
  * Abstraction の一種である。
  * これは NamedElements の集合 2 つの間の Abstraction であり、
    一方 (supplier) は仕様を、他方 (client) は実装を表現する。

A_supplier_supplierDependency
  * Dependency から NamedElement への関連（単方向）。
  * A_target_directedRelationship を subsets する。
  * 関連端 supplier の多重度は ``1..*`` である。ゼロではあり得ない。

A_clientDependency_client
  * Dependency と NamedElement との間の関連（双方向）。
  * A_source_directedRelationship を subsets する。
  * 関連端 client の多重度は ``1..*`` である。ゼロではあり得ない。
  * 関連端 clientDependency は subsets される予定があるようだ。

A_mapping_abstraction
  * Abstraction から OpaqueExpression への composite 関連（単方向）。
  * 図を見る限り OpaqueExpression によって mapping を表現する、と解釈できる。
  * A_ownedElement_owner を subsets する。

7.7.4 Notation
----------------------------------------------------------------------
* Dependency は破線矢印として示す。

  * 矢印は client から supplier に向く。
  * 矢印のラベルにはオプションとしてキーワード・ステレオタイプを付けてよい。
  * 複数の clients/suppliers がある場合、矢印を束ねる。
    お望みなら小さいドットを破線の分岐点に置くことができる。

* Usage の記法は Dependency に準じ、キーワード ``«use»`` を添える。
* Abstraction の記法は Dependency に準じ、
  キーワード ``«abstraction»`` または固有の定義済みステレオタイプを添える。

* Realization は頭が白三角の破線矢印として示す。

7.7.5 Examples
----------------------------------------------------------------------
* Figure 7.19 An example of an «Instantiate» Dependency

  * 謎のキーワード ``«Instantiate»`` を適用した Dependency の記法例。
  * 画質が荒いので破線に見えないのがまずい。

* Figure 7.20 An example of a «use» Dependency

  * Usage の記法例。

* Figure 7.21 An example of a realization Dependency

  * Realization の記法例。見慣れたクラス図だ。

7.8 Classifier Descriptions
======================================================================
機械生成による節。

7.9 Association Descriptions
======================================================================
機械生成による節。

.. include:: /_include/uml-refs.txt
