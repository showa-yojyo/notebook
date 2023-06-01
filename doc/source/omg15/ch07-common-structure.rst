======================================================================
7 Common Structure
======================================================================

UML 2.5 pp. 21-68 に関するノート。

.. contents:: ノート目次
   :depth: 2

7.1 Summary
======================================================================

この章で仕様化するのは UML の全ての構造的モデリングの礎となるモデリング概念。後
続の章で定義していく諸概念の基底となる抽象概念ばかり。

7.2 Root
======================================================================

7.2.1 Summary
----------------------------------------------------------------------

* Element と Relationship の根源的な概念は、UML におけるモデリング概念のその他全
  ての基盤を与える。

7.2.2 Abstract Syntax
----------------------------------------------------------------------

* Figure 7.1 Root

  * 初めて見て意味の分からない記法があるならば、前章
    (:doc:`./ch06-additional-information`) を再読したほうがいい。

  * 登場するクラスは 4 つ。Element, Relationship, DirectedRelationship, Comment
    である。Comment を除いてすべて抽象クラスである。

    * 白い矢先の関連はクラスの継承のようなものという解釈で問題ない。いわゆる
      is-a 関係、is-a-kind-of 関係である。

.. note::

   クラス間の関連、図式中の各種矢印が相当する、について、仕様説明が済んでいない
   要素もある。より独立性の高い関連からノートを取っていく。

``A_ownedElement_owner``
  * Element から Element への composite 関連（双方向）。

    * 両関連端にドットが描画されているので、両方向に所有関係がある。

  * Element は他の Element を所有することができるという性質を表現する関連である。
  * 関連端 ``ownedElement`` の多重度は ``*`` となっている。任意の Element は、ゼ
    ロ個を含む任意の個数の Element を所有できることを意味する。以下同様。
  * 関連端 ``owner`` の多重度が ``0..1`` となっている。任意の Element について、
    その所有者がないか、または 1 個だけあることを意味する。以下同様。
  * 両関連端共通

    * 制約が ``{readOnly, union}`` となっている。これらについては当分仕様説明が
      ないまま話が進む。
    * 関連端名の前に付いている ``+`` についてはアクセスレベルが公開ということ。
      以下同様。
    * 関連端名の前に付いている ``/`` については、「この関連端は別の関連端が継承
      するだろう」という意味だった (p. 18)。以下同様。

      * ``{union}`` と ``/`` が常に同時に関連端に現れることに気づいた。

``A_ownedComment_owningElement``
  * Element から Comment への composite 関連（単方向）。

    * 関連端 ``ownedComment`` にだけ開いた矢先がある。これは ``owningComment``
      からだけ navigable であることを意味する。``ownedComment`` から
      ``owningComment`` には navigable ではない。以下同様。
    * 関連端 ``ownedComment`` にだけドットがある。ゆえに ``owningComment`` に
      よって所有されていることを意味する。以下同様。

  * あるモデリング要素がコメントされていることを表す関連。
  * 両側関連端に ``{subsets}`` 制約がある。例えば ``ownedComment`` は ``{subsets
    ownedElement}`` となっている。これは <``ownedComment`` is a subset of
    ``ownedElement``> の意味に取る。反対に <``ownedElement`` is a superset of
    ``ownedComment``> が成り立つと推理したい。上手いことに ``ownedElement`` には
    ``{union}`` という制約があったのだった。

    以下、このような条件を当ノートでは「``A_ownedElement_owner`` を subsets す
    る」のように簡略して表記する。

``A_annotatedElement_comment``
  * Comment から Element への関連（単方向）。
  * コメントには必ず何かモデリング要素が関連付けられている。
  * 多重度が両側 ``*`` なので、一つの要素に複数のコメントが付されていてよいし、
    複数要素に対して一つのコメントが付されていてもよい。

``A_relatedElement_relationship``
  * Relationship から Element への関連（単方向）。
  * この関連の意味は上記 Relationship を参照。
  * 関連端 ``relatedElement`` の多重度が ``1..*`` なので、空でない要素の集まりに
    関係性を定義できる。
  * 両関連端共通

    * ``{readOnly, union}`` である。
    * プラス記号とスラッシュ記号が関連端名の前に付いている。

``A_source_directedRelationship``, ``A_target_directedRelationship``
  * DirectedRelationship から Element への関連。二つの関連をまとめて記す。
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

* Element とはすべての UML メタクラスの基底クラスである。
* あらゆる Element は他の Elements を所有することができるという性質を有する。あ
  る Element がモデルから取り除かれるときには、その ``ownedElements`` のすべても
  また必ずモデルから取り除かれる。

7.2.3.2 Comments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Element のあらゆる種類は Comments を所有することが許される。Element に対する
  ``ownedComments`` は何も意味を追加しないが、モデルの読者にとって有用な情報を表
  現することが許される。

7.2.3.3 Relationships
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Relationship とは、他の Elements の間のある種の関係性を指定する Element であ
  る。Relationship の「子孫」がそれらが表現する概念に相応しい意味を与える。
* DirectedRelationship とは、``source`` モデル要素の集まりと ``target`` モデル
  要素の集まりの間のRelationship を表現するものである。

  * DirectedRelationship は ``source`` 要素から ``target`` 要素へ向いていると言
    う。

7.2.4 Notation
----------------------------------------------------------------------

この仕様書では Abstract Syntax の節で示した図式の各要素の記法を Notation の節で
仕様化することになっている。しかし、今回は Comment 以外全て抽象クラスなので、記
法が存在しない。それゆえ Comment のみ記法の仕様を述べている。

* Comment は「右上が折れた紙切れ」のような図形の中に文字列を記すことで示す。
* Comment シンボルと ``annotatedElements`` のシンボルそれぞれとを破線で結ぶ。

  * 周囲の状況から明らかな場合、または図式中で重要でない場合は、この破線を隠して
    もよい。

7.2.5 Examples
----------------------------------------------------------------------

* Figure 7.2 Comment notation

  * 特筆すべき事項なし。
  * いちおう断っておくと Account と書かれていないほうが Comment である。

7.3 Templates
======================================================================

原始的なモデリング要素の仕様の直後でなんとテンプレートの話題になる。UML でのテン
プレートは C++ 等の一部プログラミング言語の定義するそれと似た概念なのだろうか。

7.3.1 Summary
----------------------------------------------------------------------

* Templates とは、他のモデル Elements によってパラメーター化されるモデル
  Elements である。
* この節ではテンプレート周辺の概念を導入するにとどめ、詳細は
  :doc:`./ch09-classification` と :doc:`./ch12-packages` に譲る。

7.3.2 Abstract Syntax
----------------------------------------------------------------------

図表が二つに分割されているが、頭の中で混ぜて覚えてよい。以下雑感。

* Figure 7.3 Templates

  * TemplateableElement, ParameterableElement, TemplateParameter,
    TemplateSignature が新登場。すべて Element の直接派生クラス。

* Figure 7.4 Template bindings

  * TemplateParameterSubstitution, TemplateBinding が新登場。

``A_ownedTemplateSignature_template``
  * TemplateableElement から TemplateSignature への composite 関連（双方向）。
  * テンプレートの TemplateSignature はある被束縛要素（複数形）内の実際のモデル要素
    に束縛されるTemplateParameters の集合を定義する。
  * ``A_ownedElement_owner`` を subsets する。
  * 関連端 ``ownedTemplateSignature`` の多重度は ``0..1`` である。

``A_parameter_templateSignature``
  * TemplateSignature から TemplateParameter への関連（単方向）。
  * 他の関連のベースとなる関連である。
  * 関連端 ``parameter`` の多重度が ``1..*`` である。
  * 制約 ``{ordered}`` が parameter の方についている。つまり個々の
    TemplateParameter が厳密に順序付けられている。

  ``A_ownedParameter_signature``
    * TemplateSignature から TemplateParameter への composite 関連（双方向）。
    * 端的に言えば TemplateSignature とは TemplateParameter の順序付き合成集約で
      ある。この関連はまさにそのことを示す。
    * ``A_ownedElement_owner`` と ``A_parameter_templateSignature`` を subsets
      する。
    * 関連端 ``ownedParameter`` は ``{ordered}`` である。

``A_default_templateParameter``
  * TemplateParameter から ParameterableElement への関連（単方向）。
  * 関連端 ``default`` は仮引数 TemplateParameter のデフォルト値？である。

  ``A_ownedDefault_templateParameter``
    * TemplateParameter から ParameterableElement への composite 関連（単方
      向）。
    * TemplateParameter がデフォルト値を与える目的で ParameterableElement を所有
      することを示す関連。
    * ``A_ownedElement_owner`` と ``A_default_templateParameter`` を subsets す
      る。
    * 両関連端の多重度は ``0..1`` である。

``A_parameteredElement_templateParameter``
  * TemplateParameter から ParameterableElement への関連（両方向）。
  * 関連端 ``parameteredElement`` は、この TemplateParameter が晒す (expose) も
    のであることを示す。

  ``A_ownedParameteredElement_owningTemplateParameter``
    * TemplateParameter から ParameterableElement への composite 関連（両方
      向）。
    * TemplateParameter がそれを晒す目的で ParameterableElement を所有することを
      示す関連。
    * ``A_ownedElement_owner`` を subsets する。
    * ``A_parameteredElement_templateParameter`` を片側だけ subsets する。もう片
      側の ``templateParameter`` には制約 ``{redefines}`` が付いている。
    * 両関連端の多重度は ``0..1`` である。

``A_formal_templateParameterSubstitution``
  * TemplateParameterSubstitution から TemplateParameter への関連（単方向）。
  * ある TemplateBinding におけるテンプレート引数代入の仮引数のようなものへの参
    照。
  * 関連端 ``formal`` の多重度は 1 である。

``A_actual_templateParameterSubstitution``
  * TemplateParameterSubstitution から ParameterableElement への関連（単方向）。
  * ある TemplateBinding におけるテンプレート引数代入の実引数のようなものへの参
    照。
  * 関連端 ``actual`` の多重度は 1 である。

  ``A_ownedActual_owningTemplateParameterSubstitution``
    * TemplateParameterSubstitution から ParameterableElement への composite 関
      連（単方向）。
    * 実際に ParameterableElement オブジェクトを所有する意味がある関連。
    * 関連 ``A_ownedElement_owner`` を subsets する。
    * 関連 ``A_actual_templateParameterSubstitution`` の ``actual`` と
      ``templateParameterSubstitution`` をそれぞれ subsets と redefines する。

``A_parameterSubstitution_templateBinding``
  * TemplateBinding から TemplateParameterSubstitution への composite 関連（双方向）。
  * TemplateBinding は TemplateParameterSubstitution を一つ所有する。
  * 関連 ``A_ownedElement_owner`` を subsets する。

``A_templateBinding_boundElement``
  * TemplateableElement から TemplateBinding への composite 関連（双方向）。
  * TemplateableElement がこの TemplateBinding による束縛要素であることを示す。
  * 関連 ``A_ownedElement_owner`` と ``A_source_directedRelationship`` を
    subsets する。

``A_signature_templateBinding``
  * TemplateParameterSubstitution から TemplateSignature への関連（単方向）。
  * 関連端 ``signature`` はこの TemplateBinding のターゲットテンプレートのための
    ものである。
  * 関連 ``A_target_directedRelationship`` を subsets する。

7.3.3 Semantics
----------------------------------------------------------------------

7.3.3.1 Templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* TemplateableElement とは、テンプレートとして任意に定義可能で、他のテンプレート
  に束縛可能な Element のことである。

  * テンプレートとは、TemplateSignature を用いて引数化される TemplateableElement
    のことである。
  * そのようなテンプレートは TemplateBinding を用いて、他のモデル要素を生成する
    のに利用することが可能である。

* テンプレートは同種の非テンプレート要素と同じやり方で利用することが不可能。
* テンプレートの TemplateSignature は、テンプレートを表す被束縛要素にある実際の
  モデル Elements に束縛されてよい TemplateParameters の集合を定義する。

  * 被束縛要素 (a bound element) とは、一つまたはそれを超えるそういう
    TemplateBindings を有するTemplateableElement のことである。

* 完全被束縛要素 (completely bound element) とは、そのすべての TemplateBindings
  が束縛されているテンプレートのTemplateParameter すべてを束縛する被束縛要素であ
  る。
* 部分的被束縛要素 (partially bound element) とは、その TemplateBindings のうち
  少なくとも一つは束縛されているテンプレートの TemplateParameter を束縛しない被
  束縛要素である。

7.3.3.2 Template Signature
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* TemplateSignature を構成する TemplateParameters は実引数（またはデフォルト値）
  により代入される仮引数を指定する。

  * TemplateParameter は TemplateParameter がその一部である TemplateSignature を
    所有するテンプレートの内側に含まれる ParameterableElement に関して定義され
    る。そのような要素は TemplateParameter によって露出されている (be exposed)
    という。

* 露出した ParameterableElement を、そのテンプレートが直接間接を問わず所有してよ
  く、または TemplateParameter 自身が所有してよいが、要素が所有権関連をテンプ
  レートモデル内に別に持たない状況である。
* TemplateParameter は ParameterableElement を、引数に対して明示的な
  TemplateParameterSubstitution を与えない任意の TemplateBinding にあるこの仮引
  数のために、``default`` として参照することも許される。

  * 露出した ParameterableElement と同様に、デフォルト ParameterableElement はテ
    ンプレートによってでも、TemplateParameter 自身によってでも直接所有されてよ
    い。

7.3.3.3 TemplateBinding
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* TemplateBinding とは、テンプレートの ``formal`` TemplateParameters へ
  ``actual`` ParameterableElements を代入することを指定する TemplateableElement
  とテンプレートの間の DirectedRelationship である。

  * TemplateParameterSubstitution とは、TemplateBinding の状況において
    ``actual`` 引数が ``formal`` TemplateParameter に代入されることを指定するもの
    である。

* 被束縛要素には複数の束縛があってよく、事によると同じテンプレートに適用される。
* TemplateableElement は TemplateSignature と TemplateBindings の両方を含んでよ
  い。それゆえ TemplateableElement はテンプレートと被束縛要素の両方であってよ
  い。
* 準拠ツールは ``formal`` TemplateParameters のすべてが TemplateBinding の部分と
  して束縛されねばならない（完全束縛）ことを必要としてよいか、``formal``
  TemplateParameters の部分集合だけが束縛される（部分束縛）ことを認めてよい。

7.3.3.4 Bound Element Semantics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* TemplateBinding はあたかも対象の TemplateSignature を所有するテンプレートの内
  容が被束縛要素にコピーされたかのように被束縛要素には同じ well-formedness 制約
  と意味があることを含意するが、TemplateBinding において ``formal``
  TemplateParameters として露出された任意の ParameterableElements へ ``actual``
  テンプレート引数として指定された対応する ParameterableElements を代入すること
  である。
* 形式上は、単独の TemplateBinding を使い、その束縛から以外の要素のない被束縛要
  素に対する拡張被束縛要素は次のように構成される：

  #. TemplateBinding の対象である TemplateSignature に関連付いたテンプレートを複
     製する。
  #. 複製がテンプレートである Elements を何であれ特殊化するならば、``general``
     要素に向けて同じ TemplateBinding を用いて、Generalization 関係を等価な被束
     縛要素に方向転換する。複製がテンプレートでもある関連 ``method`` を有する
     Operation であれば、同じテンプレート束縛を用いて、その ``method`` を等価な
     被束縛要素で置き換える。
  #. 複製により直接的または間接的に所有される Element それぞれに対して、複製の
     TemplateParameter の ``parameteredElement`` への参照のどれもを
     TemplateBinding にある引数に関連付けられた ``actual`` Element への参照に置
     き換える。
  #. TemplateBinding で参照されている TemplateParameters を複製の
     TemplateSignature からすべて取り除く。もしこれが TemplateSignature から
     TemplateParameters を全部取り除こうものならば、TemplateSignature 丸ごとを取
     り除く。

* 被束縛要素に一個を超える TemplateBinding があれば、固有の拡張被束縛要素を
  TemplateBinding それぞれに基いた定義が可能である。
* モデルにある被束縛要素を含むことは、対応する拡張被束縛要素がモデルに含まれると
  いうことを自動的には要求しない。
* 他方では被束縛要素が Namespace テンプレートの代わりになるならば、Namespace 自
  身としてみなされる被束縛要素の ``members`` を参照することが可能である必要があ
  ることが許される。
* こういう状況に対応するために、被束縛要素自身に加えて、被束縛要素の代わりの拡張
  被束縛要素をモデルに含めても差し支えない。

7.3.4 Notation
----------------------------------------------------------------------

* TemplateableElement に TemplateParameters があれば、まずは小さい破線の矩形をそ
  の要素の右上に置く。

  * 破線矩形は TemplateParameters の仮引数リストを含む。空であってはならない。
  * この仮引数リストは CSV で記すか、一行に一つの仮引数を示す。
  * 一つの TemplateParameter の記法 <template-parameter> は BNF で定義されている
    (p. 26)。

* 被束縛要素の記法は、その種類の他の要素のそれと同じとする。
* TemplateBinding は破線矢印で示す。

  * 向きは被束縛要素からテンプレートとする。
  * キーワード ``«bind»`` をラベルに付す。
  * 束縛情報 <template-param-substition> を CSV で記してよい。BNF で定義されてい
    る (p. 26)。

    * 代入の記号として ``->`` を用いる。たぶん ``T -> int`` のように書ける。

7.4 Namespaces
======================================================================

7.4.1 Summary
----------------------------------------------------------------------

* Namespace とは ``name`` によって見分けることが可能な NamedElements の集合を含
  む、モデルにある要素である。

7.4.2 Abstract Syntax
----------------------------------------------------------------------

* Figure 7.5 Namespaces

  * 新登場の記号がいくつかある。

    * VisibilityKind 内の ``«enumeration»`` という記法
    * PackageableElement 内の属性 ``visibility`` の説明が込み入っている。

``A_member_memberNamespace``
  * Namespace から NamedElement への関連（単方向）。
  * いずれの関連端も ``{readOnly, union}`` かつ多重度が ``*`` である。

  ``A_ownedMember_namespace``
    * Namespace から NamedElement への composite 関連（双方向）。
    * ``A_member_memberNamespace`` と ``A_ownedElement_owner`` を subsets してい
      る。
    * 関連端 ``namespace`` の多重度は ``0..1`` になっている。

    ``A_ownedRule_context``
      * Namespace から Constraint への composite 関連（双方向）。
      * 関連端 ``context`` の多重度 ``0..1`` に対して、関連端 ``ownedRule`` の多
        重度が ``*`` の関係がある。

  ``A_importedMember_namespace``
    * Namespace から PackageableElement への関連（単方向）。

``A_elementImport_importingNamespace``, ``A_packageImport_importingNamespace``
  * Namespace から ElementImport, PackageImport それぞれへの composite 関連（双
    方向）。
  * Namespace は他の Namespaces から NamedElements をインポートしてよい。
  * ``A_ownedElement_owner``, ``A_source_directedRelationship`` を subsets して
    いる。関連端 ``importingNamespace`` 側が ``source`` かつ ``owner`` である。

``A_importedElement_import``, ``A_importedPackage_packageImport``
  * 前者は ElementImport から PackageableElement への関連（単方向）、後者は
    PackageImport から Package への関連（単方向）。

  * ``A_target_directedRelationship`` を subsets している。

``A_nameExpression_namedElement``
  * NamedElement から StringExpression への composite 関連（単方向）
  * NamedElement は高々 1 個の StringExpression を所有できる。

    * テンプレート中では NamedElement には、その subexpressions が
      TemplateParameters が晒す ParameterableElement である関連 StringExpression
      があってよい。

  * NamedElement には特性の ``name`` と関連端の ``nameExpression`` の両方があっ
    てもよい。この場合 ``name`` はその NamedElement の別名として用いることが可
    能。

  * ``A_ownedElement_owner`` を subsets する。

同時に VisibilityKind を仕様化している。4 つの可視性タイプからなる。

7.4.3 Semantics
----------------------------------------------------------------------

7.4.3.1 Namespaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Namespace は NamedElements の容器を与えるものであり、
  中身の方はその ``ownedMembers`` と呼ばれる。

  * もし Namespace のある ``member`` が ``N`` という ``name`` の NamedElement な
    らば、その ``member`` を ``N::x`` の形式の限定名 (qualified name) により参照
    することが可能である。

* 区別が必要なときには、Namespace 名を使って限定されていない簡素な名前を非限定
  名として参照してよい。
* Namespace 自身は NamedElement であるので、NamedElement の完全限定名は、例えば
  ``N1::N2::x`` のように Namespace 名を複数含んでよい。
* Namespace にちなんだ ``ownedRule`` Constraints は制約の付いた要素に対する
  well-formedness 規則を表現する。これらの制約は制約の付いた要素が well-formed
  かどうかを決定するときに評価される。

7.4.3.2 Named Elements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* NamedElement とは、``name`` を有することが許される、モデル内の Element であ
  る。
* NamedElements はある NamedElement が別のものとどのように区別が付くのかを指定す
  る規則に従って Namespace 内に現れてよい。その既定の規則とは、二つの
  ``members`` が見分けがつくのは、それらが異なる ``names`` であるか、同じ
  ``names`` であるかである。
* NamedElement の可視性は Element の用途を抑制する手段を与えるが、それは
  Namespaces においてか、Element へのアクセスにおいてのどちらかである。
* NamedElement には明示的な ``name`` があることに加えて、NamedElement を表す計算
  された名前を指定するのに用いてよいStringExpression に関連付けられてよい。
* NamedElement にはそれに関連する ``name`` と ``nameExpression`` の両方があって
  よい。

7.4.3.3 Packageable Elements and Imports
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* PackageableElement とは Package が直接所有することのできる NamedElement であ
  る。

  * Package については :doc:`./ch12-packages` 参照。
  * かつ ParameterableElement でもあるので、TemplateParameter としても使える。
  * NamedElement から継承した属性 ``visibility`` のデフォルト値は ``public`` で
    ある？

* ElementImport とは Namespace と PackageableElement との間の
  DirectedRelationship である。

  * ElementImport はその PackageableElement の名前をインポート先 Namespace に追
    加するものである。
  * その ElementImport の可視性は、インポート元の要素のそれと同じか、より制限さ
    れたものかのどちらかになる。

* 名前衝突の際には、名前空間の外側の名前が隠蔽される。外側のものをアクセスするに
  は限定名を用いることで可能になる。
* PackageImport とは Namespace と Package との間の DirectedRelationship である。
  この関係は Namespace が対象の Package の ``members`` の名前を、自身の
  Namespace に追加することを意味する。
* もし見分けの付かない Elements が Namespace にインポートされようとした場合、そ
  の Elements は対象の Namespace に追加されない。それらをそこで用いるためには名
  前を限定する必要がある。
* publicly にインポートした Element はインポート先 Namespace の public member で
  ある。

.. note::

   ここまで出てきた要素名で、まだ仕様化されていないものがいくつかある。

7.4.4 Notation
----------------------------------------------------------------------

7.4.4.1 Namespaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Namespace には一般的な記法はない。特別な種類のものに固有の記法がある。

7.4.4.2 Name Expressions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* NamedElement はその ``nameExpression`` (StringExpression) で表現する。これには
  別名ありなしで二つの記法がある。いずれの場合も StringExpression はドルマーク
  ``$`` に挟んで表す。

7.4.4.3 Imports
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* PackageImport/ElementImport は頭が開いた破線矢印で表現する。

  * ``visibility = public`` の場合は ``«import»`` を付す。さもなくば
    ``«access»`` を付す。
  * このキーワードの後または下に ``alias`` を示してもよい。

* PackageImport/ElementImport の代替表記として一意に識別するテキストを示せる。
  BNF 記法の仕様が p. 29 にある。

7.4.5 Examples
----------------------------------------------------------------------

7.4.5.1 Name Expressions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Figure 7.6 Template package with string parameters

  * テンプレートの記法例も兼ねている。
  * 図の上側大枠が Package テンプレート ResourceAllocation というものを示す。
  * パッケージ右上の三行が TemplateParameter の記法例。

    * パラメーター Resource と ResourceKind の型？が StringExpression である。

  * ``$a<Resource>Allocation$`` 等のテキストが NamedElement/StringExpression の
    記法例。
  * 図の下側の ``«bind»`` リストが TemplateParameterSubstitution の記法例。
    StringExpression の値は普通の文字列のようだ。

7.4.5.2 Imports
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Figure 7.7 Example of element import

  * 下側の矢印およびその付随記号が ElementImport の記法例となる。

* Figure 7.8 Example of element import with aliasing

  * こちらも ElementImport の記法例で「別名付き」である。

* Figure 7.9 Examples of public and private package imports

  * PackageImport の記法例である。矢印の頭の位置が先程と異なる。

7.5 Types and Multiplicity
======================================================================

型と多重度を同じタイミングで仕様化する。

7.5.1 Summary
----------------------------------------------------------------------

* 型と多重度は値を含む Element の宣言に用いられる。そのような値の種類と個数に制
  約を与える目的がある。

7.5.2 Abstract Syntax
----------------------------------------------------------------------

* Figure 7.10 Abstract syntax of types and multiplicity elements

  * 新規クラス TypedElement, Type, Multiplicity はすべて抽象。

``A_type_typedElement``
  * TypedElement から Type への関連（単方向）。
  * 関連端 ``type`` の多重度は ``0..1`` だ。
  * これは TypedElement のとる値の Type が与えられているかどうかを意味する。
    言語にもよるだろうが、ゼロの場合は任意の型の値になれるようだ。

``A_lowerValue_owningLower``, ``A_upperValue_owningUpper``
  * MultiplicityElement から ValueSpecification への composite 関連（単方向）。
  * ValueSpecification の仕様は :doc:`./ch08-values` にて。
  * ``A_ownedElement_owner`` を subsets する。
  * 属性値の ``lower``, ``upper`` とは別に関連端 ``lowerValue``, ``upperValue``
    がある。

7.5.3 Semantics
----------------------------------------------------------------------

7.5.3.1 Types and Typed Elements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Type とは、その Type のオブジェクトとして知られている値の取り得る集合を指定す
  るものである。

  * Type の種類に応じて、そのオブジェクトは生成または消滅されてよい。
  * UML における Types はすべて Classifiers である。:doc:`./ch09-classification`
    参照。

* TypedElement とは、何らかの手段で特定の値を表現する NamedElement である。

  * TypedElement の種類としては ValueSpecification や StructuralFeature がある。
    :doc:`./ch08-values` や :doc:`./ch09-classification` を参照。

* TypedElement に関連 Type があれば、TypedElement で表現される値はどれもが与えら
  れた Type のオブジェクトであるものとする。

7.5.3.2 Multiplicities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* MultiplicityElement とは、何らかの手段で値の集まりを表現するためにオブジェクト
  化してよいElement である。
* 集まりの濃度（これは数学由来の用語だろう）とは、その集まりに含まれる値の個数で
  ある。MultiplicityElement の多重度は、それが表す集まりの有効な濃度を指定する。

* MultiplicityElement の多重度を表す ``lower`` および ``upper`` は
  ValueSpecifications により指定され、``lowerBound`` に対しては Integer 値を、
  ``upperBound`` に対しては UnlimitedNatural 値を評価する必要がある。

* MultiplicityElement は境界値が両方ともゼロである多重度を定義することが可能であ
  る。

* 属性 ``isOrdered`` は値の集まりが順序付けられているか否かを示す。
* 属性 ``isUnique`` は一意な値の集まりか否かを示す。
* Table 7.1 の ``isOrdered`` と ``isUnique`` の値の組み合わせと、それらに対応す
  るコレクションの型 (e.g. Set, OrderedSet) の名前が面白い。詳しくないが Java の
  クラス名だろうか。

7.5.4 Notation
----------------------------------------------------------------------

7.5.4.1 Multiplicity Element
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

7.6.1 Summary
----------------------------------------------------------------------

* Constraint とは、Constraint を含むモデルの有効な実現のすべてによって満足されて
  いなければならない制限を示す断言である。

7.6.2 Abstract Syntax
----------------------------------------------------------------------

* Figure 7.13 Abstract Syntax of Constraints

  * クラス Constraint とその関連だけを仕様化するようだ。

``A_constrainedElement_constraint``
  * Constraint から Element への関連（単方向）。
  * 関連端 ``constrainedElement`` の多重度は ``*`` である。
  * この ``constrainedElement`` が「制約が付随する対象」である。

``A_specification_owningConstraint``
  * Constraint から ValueSpecification への composite 関連（単方向）。
  * ``A_ownedElement_owner`` を subsets する。
  * 一つの Constraint が一つの ValueSpecification を所有する。具体的に言うと
    ``specification`` は「制約が満足されているかどうかを示す値」なので、値として
    は ``true`` か ``false`` をとる。

``A_ownedRule_context``
  前述の通り。

7.6.3 Semantics
----------------------------------------------------------------------

* Constraint の ``specitication`` は Boolean 型の ValueSpecification により与え
  られる。その計算には ``constrainedElements`` と ``context`` を参照してよい。
* 一般には Constraint の ``owners`` としては様々な種類の Elements が考えられる。
  唯一の制限は、所有者である Element は ``constrainedElements`` へのアクセス手段
  が必要であるということだ。

  * Constraint の ``owner`` はいつ Constraint の ``specitication`` が評価される
    のかを決定する。例えば、Operation の ``precondition`` である Constraint は発
    動の開始時に評価され、一方 ``postcondition`` である Constraint は発動の締め
    くくりに評価される。

* Constraint はその ``specitication`` を評価することで評価される。``true`` に評
  価されるならば、Constraint はその時点において満足されている。

7.6.4 Notation
----------------------------------------------------------------------

* Constraint の記法には UML 定義のものとユーザー定義のものとがある。
* 基本的には中括弧とブーリアン式を組み合わせた表記になる。何なら中括弧の中に（真
  偽を評価できるならば）自然言語で文を書いても構わないようだ。
* より一般的には、制約文字列をノートシンボルの中に配置して、それを
  ``constrainedElement`` の表すシンボルに破線で結ぶという表記法をとる。
* テキスト文字列の記法をとる Element に対しては、その文字列のすぐ後に制約文字列
  を配置してもよい。
* 複数要素に同一 Constraint を示す場合、まずそれらの要素間に破線を引き、そのラベ
  ルに制約文字列を使う。

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

7.7.1 Summary
----------------------------------------------------------------------

* Dependency はモデル要素間の supplier の修正が client に強く影響するような
  supplier/client 関係を意味する。

7.7.2 Abstract Syntax
----------------------------------------------------------------------

* Figure 7.17 Abstract syntax of dependencies

  * 一部テキストが欠けている。

``A_supplier_supplierDependency``
  * Dependency から NamedElement への関連（単方向）。
  * ``A_target_directedRelationship`` を subsets する。
  * 関連端 ``supplier`` の多重度は ``1..*`` である。ゼロではあり得ない。

``A_clientDependency_client``
  * Dependency と NamedElement との間の関連（双方向）。
  * ``A_source_directedRelationship`` を subsets する。
  * 関連端 ``client`` の多重度は ``1..*`` である。ゼロではあり得ない。
  * 関連端 ``clientDependency`` は subsets される予定があるようだ。

``A_mapping_abstraction``
  * Abstraction から OpaqueExpression への composite 関連（単方向）。
  * 図を見る限り OpaqueExpression によって ``mapping`` を表現する、と解釈でき
    る。
  * ``A_ownedElement_owner`` を subsets する。

7.7.3 Semantics
----------------------------------------------------------------------

7.7.3.1 Dependency
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Dependency は ``clients`` の意味が ``suppliers`` なしには完全ではないことを含
  意している。
* モデル内の Dependency 関係の存在には、いかなる実行時の意味はない。そういうのは
  関連づいている NamedElement (``client``/``supplier``) が与える。

7.7.3.2 Usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Usage とは、ある NamedElement がその完全な実装や操作のために必要とする別の
  NamedElement または NamedElements の集合を必要とする Dependency である。

7.7.3.3 Abstraction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Abstraction とは、異なる抽象水準における or 異なる視点から同じ概念を表現する、
  二個の NamedElements または NamedElements の集合に関係する Dependency である。
* この関係性は ``suppliers`` と ``clients`` との間の写像として定義してよい。
* ``«Derive»``, ``«Refine»``, ``«Trace»`` などの定義済みステレオタイプがある。こ
  れは :doc:`./ch22-standard-profile` で仕様化する。

7.7.3.4 Realization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Realization とは NamedElements の集合 2 つの間の特殊化された Abstraction 依存
  であり、一方 (``supplier``) は仕様を、他方 (``client``) は実装を表現する。

7.7.4 Notation
----------------------------------------------------------------------

* Dependency は破線矢印として示す。

  * 矢印は ``client`` から ``supplier`` に向く。
  * 矢印のラベルにはオプションとしてキーワード・ステレオタイプを付けてよい。
  * 複数の ``clients``/``suppliers`` がある場合、矢印を束ねる。
    お望みなら小さいドットを破線の分岐点に置くことができる。

* Usage の記法は Dependency に準じ、キーワード ``«use»`` を添える。
* Abstraction の記法は Dependency に準じ、キーワード ``«abstraction»`` または固
  有の定義済みステレオタイプを添える。

* Realization は頭が白三角の破線矢印として示す。

7.7.5 Examples
----------------------------------------------------------------------

* Figure 7.19 An example of an ``«Instantiate»`` Dependency

  * 謎のキーワード ``«Instantiate»`` を適用した Dependency の記法例。
  * 画質が荒いので破線に見えないのがまずい。

* Figure 7.20 An example of a ``«use»`` Dependency

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
