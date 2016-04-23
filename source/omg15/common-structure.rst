======================================================================
7 Common Structure
======================================================================
UML 2.5 pp. 21-68 に関するノート。この章からノートを簡素にしたい。

.. contents:: ノート目次

7.1 Summary
======================================================================
この章で仕様化するのは UML の全ての構造的モデリングの礎となるモデリング概念。
後続の章で定義していく諸概念の基底となる抽象概念ばかり。

7.2 Root
======================================================================
最初なので少々丁寧にノートを取る。

7.2.1 Summary
----------------------------------------------------------------------
* Element と Relationship が UML の残り全てのモデリング要素の基底である。

7.2.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 7.1 を初めて見て意味の分からない記法があるならば、
  前章を再読したほうがいい。

7.2.3 Semantics
----------------------------------------------------------------------
登場するクラスは 4 つ。

*Element*
  すべての要素の基底。

  * 他の Element を所有することができるという性質を有する。
  * その特殊なケースなのだが Comment を所有することができる。

*Relationship*
  複数 Elements 間のある種の関係性を指定する Element である。

  * 意味はさらなる具象クラスで決まる。

*DirectedRelationship*
  特殊な Relationship で、
  ある Element(s) と別の Element(s) との関係性を表現する。

  * 一方の要素群を source(s) と呼び、他方を target(s) を呼ぶ。
  * 「向きの付いた」というのは、この source から target への向きを意味する。

Comment
  読んで字のごとし。

  * Element に付随する情報・説明等を余白に書き込みたくなるが、
    それを正式に仕様化した概念なのだろう。

クラス間の関連、図式中の各種矢印が相当する、について、
仕様説明が済んでいない要素もある。
より独立性の高い関連からノートを取っていく。

* 白い矢先の関連はクラスの継承のようなものという解釈で問題ない。

* Element 自身から自身への関連 (A_ownedElement_owner)

  owner
    * 多重度が ``0..1`` となっている。
      任意の Element について、その所有者がないか、または 1 個だけあることを意味する。

    * 関連端点に黒菱型が描画されている。ゆえに composite である。
      言葉を変えると「owner の生存期間が終わると ownedElement のそれも終わる」。

  ownedElement
    * 多重度が ``*`` となっている。
      任意の Element は、ゼロ個を含む任意の個数の Element を所有できることを意味する。

  owner と ownedElement 共通
    * 制約が ``{readOnly, union}`` となっている。これらについては当分仕様説明がない。

    * 関連端名の前に付いている ``+`` については今のところよくわからない。
      アクセスレベルが公開ということか。

    * 関連端名の前に付いている ``/`` については、
      「この関連端は別の関連端が継承するだろう」という意味だった (p. 18)。

    * 関連端点にドットが描画されているので、両方向に所有関係がある。
      すなわち owner から ownedElement に、
      反対に ownedElement から owner にたどり着くことができる。

* Relationship から Element への関連 (A_relatedElement_relationship)

  relationship
    * こちらの端点にはドットがない。

    * 多重度が ``*`` なので、
      「relatedElement の同一の集まりに、複数の異なる関係性が存在する」ことがあり得ると読める。

    * 場合によってはゼロもあるのだが、何の意味がある？
      無関係に集まった Element 群くらいの意味になるのか？

  relatedElement
    * こちらの端点にはドットがあり、開いた矢先を持つ。
      ゆえに反対側である relationship によって所有されていると読める。

    * 多重度が ``1..*`` なので、空でない要素の集まりに関係性を定義できる。

  両端点共通
    * ``{readOnly, union}`` である。やはり union は集合論で用いられる意味と同じか？
    * プラス記号とスラッシュ記号が関連端名の前に付いている。

* DirectedRelationship から Element への関連 (A_source_directedRelationship, A_target_directedRelationship)

  ふたつの関連をまとめて記す。

  directedRelationship
    * 見るべきポイントは制約  ``{subsets relationship}`` だ。
      これは関連端 directedRelationship が上述の関連端 relationship の部分集合である、の意だ。

    * ある関連端が既存の関連端の部分集合であるとはどういう意味か、微妙なところがある。

  source, target 共通
    * 「向きという概念のある関連」という概念ゆえ、向きの開始・終了点を Element が表現する。
      こちら側だけに開いた矢先とドットが付いているので、
      source や target 側から directedRelationship にたどり着くことはない。

    * 制約 ``{subsets relatedElement}`` については先ほどと同様の様式の解釈でよい。
    * プラス記号とスラッシュ記号が関連端名の前に付いている。
      後続の新規導入構文で継承されるのだろう。

次の関連の意味を解釈することをノートを取るための練習問題とする。

* Element から Comment への関連 (A_ownedComment_owningElement)
* Comment から Element への関連 (A_annotatedElement_comment)

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

  * 文脈から明らかな場合、または図式中で重要でない場合は、
    この破線を隠してもよい。

7.2.5 Examples
----------------------------------------------------------------------
* Figure 7.2 Comment notation のみ。特筆すべき事項なし。

7.3 Templates
======================================================================
原始的なモデリング要素の仕様の直後でなんとテンプレートの話題になる。
UML でのテンプレートは C++ 等の一部プログラミング言語の定義するそれと似た概念なのだろうか。
読んでみよう。

7.3.1 Summary
----------------------------------------------------------------------
* Template は他のモデル Element によってパラメーター化されるモデル Element である。
* この節ではテンプレート周辺の概念を導入するにとどめ、詳細は 9 章と 12 章に譲る。

7.3.2 Abstract Syntax
----------------------------------------------------------------------
図表が二つに分割されているが、頭の中で混ぜて覚えてよい。以下雑感。

* Figure 7.3 で、一部関連端名のスラッシュが抜けていると思われるものがある。

7.3.3 Semantics
----------------------------------------------------------------------
登場する抽象クラスとクラスをまとめておく。

*TempleatableElement*
  * <A TemplateableElement is an Element that can optionally be defined
    as a template and bound to other templates>(p. 24)
  * 後述する TemplateSignature を ``0..1`` 個所有できる。
  * 後述する TemplateBinding を任意個所有できる。

*ParameterableElement*
  * TemplateParameter や TemplateParameterSubstitution によって所有される要素？

TemplateSignature
  * 単なる TemplateParameter の順序付き composite に見える。

TemplateParameter
  * 読んで字のごとくテンプレートパラメーターを表す要素だろう。
  * ParameterableElement に対する 2 系統の関連 (default/parameteredElement) がある。

TemplateParameterSubstitution
  * <A TemplateParameterSubstitution
    specifies the actual parameter to be substituted for a formal
    TemplateParameter within the context of a TemplateBinding>(p. 24)
  * TemplateParameter を 1 個、ParameterableElement を 1 個と関連している。

TemplateBinding
  * TemplateableElement と TemplateSignature の DirectedRelationship である。

    * TemplateableElement と TemplateSignature がそれぞれ source, target である。

  * TemplateParameterSubstitution を composite で関連する。

登場する関連のうち、初めて目にする制約を持つ物をまとめておく。

A_parameter_templateSignature
  * TemplateSignature から TemplateParameter への一方通行。
  * 制約 ``{ordered}`` が parameter の方についている。
    つまり個々の TemplateParameter が厳密に順序付けられている。

A_ownedParameter_signature
  * TemplateSignature と TemplateParameter の関連だが、
    両端とも上述の関連の subsets になっている。

  * 制約を見ると、前節で定義を見た関連 (A_ownedElement_owner) を再利用している。
    これにより TemplateSignature が TemplateParameter の composite であることが示されている。

  * ドット記法が所有権が双方向であることを示す？

A_parameteredElement_templateParameter, A_default_templateParameter
  * TemplateParameter から ParameterableElement への関連は 2 系統ある。
    それらの基になる関連。
    要するに「パラメーター化要素」「デフォルトの要素」だろう。

A_ownedParameteredElement_owningTemplateParameter, A_ownedDefault_templateParameter
  * いつもの所有関連と上述の関連それぞれから subsets された関連となる。
  * 関連端 owned ホニャララの多重度は両者とも ``0..1`` である。
  * 後者の関連端 templateParameter は制約 ``{redefines templateParameter}`` が付いている。
    これはどういうことだろう？

.. todo:: 主にイタリック体で記されている用語のノート。

   * template
   * bound [element]
   * (completely | partially | expanded) bound element
   * exposed
   * etc.

7.3.4 Notation
----------------------------------------------------------------------
次の各要素の記法を BNF で定義している (p. 26)。

* <template-parameter>
* <template-param-substition>

  代入の記号として ``->`` を用いる。たぶん ``T -> int`` のように書ける。

7.4 Namespaces
======================================================================

7.4.1 Summary
----------------------------------------------------------------------
名前のある要素、名前空間、パッケージ可能な要素、インポート等のモデリング概念を導入する。

7.4.2 Abstract Syntax
----------------------------------------------------------------------
Figure 7.5 をじっくり見る。新登場の記号がいくつかある。

* VisibilityKind 内の ``«enumeration»`` という記法
* PackageableElement 内の属性 visibility の説明が込み入っている。

7.4.3 Semantics
----------------------------------------------------------------------
ここで仕様化された（抽象）クラスを記す。

*NamedElement*
  * その名前 (name) で識別することができる Element である。
  * 特に所属する名前空間を省略せずに表記するときの名前を qualifiedName という属性で持つ。
  * 名前の他に visibility という VisibilityKind 型の値が付随している。

*Namespace*
  * NamedElement の集合を所有する NamedElement オブジェクトである。
    これは ownedMember という関連端名で示されている。

  * その他に PackageableElement, ElementImport, PackageImport, Constraint に関連する。

*PackageableElement*
  * Package が直接所有することのできる NamedElement である。
  * かつ ParameterableElement でもあるので、TemplateParameter としても使える。
  * NamedElement から継承した属性 visibility のデフォルト値は public である？

ElementImport
  * Namespace と PackageableElement との間の DirectedRelationship である。
  * かつ PackageableElement でもある。
  * 属性には alias と visibility がある。後者はデフォルトで public である？

PackageImport
  * Namespace と Package との間の DirectedRelationship である。
  * 属性には visibility がある。デフォルトで public である？

.. note:: ここまで出てきた要素名で、まだ仕様化されていないものがいくつかある。

ここで仕様化された関連を記す。

A_member_memberNamespace
  * Namespace から NamedElement への関連。この方向にのみ navigable である。
  * いずれの関連端点も ``{readOnly, union}`` かつ多重度が ``*`` である。
  * 次の 2 関連によって subsets されている。

  A_ownedMember_namespace
    * Namespace から NamedElement への関連。双方向に所有権？
    * A_ownedElement_owner をも subsets している。
    * Namespace が NamedElement の composite になっている。
    * 関連端 namespace の多重度は ``0..1`` になっている。
    * 次の関連によって subsets されている。

    A_ownedRule_context
      * Namespace から Constraint への関連。
      * Namespace は Constraint の composite である。
        関連端 context の多重度 ``0..1`` に対して、
        関連端 ownedRule の多重度が ``*`` の関係がある。

  A_importedMember_namespace
    * Namespace から PackageableElement への関連。

A_elementImport_importingNamespace, A_packageImport_importingNamespace
  * これらは Namespace から ElementImport, PackageImport それぞれへの composite な関連である。
  * 2 種類の関連 A_ownedElement_owner, A_source_directedRelationship を subsets している。
    関連端 importingNamespace 側が source かつ owner である。

A_importedElement_import, A_importedPackage_packageImport
  * 前者は ElementImport から PackageableElement への関連、
    後者は PackageImport から Package への関連である。

  * 両者とも関連 A_target_directedRelationship から派生している。
    ElementImport と PackageImport が directedRelationship を、
    PackageableElement と Package が target をそれぞれ subsets している。

A_nameExpression_namedElement
  * NamedElement は高々 1 個の StringExpression を所有できる。
  * 関連 A_ownedElement_owner から派生したものだ。

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
* Figure 7.6 はテンプレートの例も兼ねている。

  * 図の上側大枠が Package テンプレート ResourceAllocation というものを示す。
  * パッケージ右上の 3 行が TemplateParameter の記法例。

    * パラメーター Resource と ResourceKind の型？が StringExpression である。

  * ``$a<Resource>Allocation$`` 等のテキストが NamedElement/StringExpression の記法例。

  * 図の下側の ``«bind»`` リストが TemplateParameterSubstitution の記法例。
    StringExpression の値は普通の文字列のようだ。

* Figure 7.7 の下側の矢印およびその付随記号が ElementImport の記法例となる。

* Figure 7.8 も ElementImport の記法例で「別名付き」である。

* Figure 7.9 は PackageImport の記法例である。
  矢印の頭の位置が先程と異なる。

7.5 Types and Multiplicity
======================================================================
型と多重度を同じタイミングで仕様化する。

7.5.1 Summary
----------------------------------------------------------------------
型と多重度は値を含む Element の宣言に用いられる。
そのような値の種類と個数に縛りをかける目的がある。

7.5.2 Abstract Syntax
----------------------------------------------------------------------
Figure 7.10 にて新たに登場するクラスと関連を観察しておく。

* クラスはすべて抽象。

7.5.3 Semantics
----------------------------------------------------------------------
ここで仕様化された（抽象）クラスを記す。

*Type*
  * 型の概念を説明するのは難しい気がする。
  * UML における Type はすべて Classifier である。9 章参照。

*TypedElement*
  * 何らかの手段で特定の値を表現するような NamedElement である。
  * この派生概念を 8 章で仕様化するらしい。

*MultiplicityElement*
  * 多重度は何らかの手段で値の集まりを表現するために生成される Element である。
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

関連について記す。

A_type_typedElement
  * TypedElement から Type への関連。多重度は ``0..1`` だ。
    これは TypedElement のとる値の Type が与えられているかどうかを意味する。
    言語にもよるだろうが、ゼロの場合は任意の型の値になれるようだ。

A_lowerValue_owningLower, A_upperValue_owningUpper
  * MultiplicityElement から ValueSpecification への関連。
    ValueSpecification の仕様は 8 章にて。

  * A_ownedElement_owner から制約 subsets で派生した関連。
  * 属性値の lower, upper とは別に関連端点 lowerValue, upperValue があるのか。

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
* Figure 7.11 は Customer というクラスシンボルの図式。

  * 属性名のすぐ後ろに多重度テキストが現れる見本。
  * 角括弧に多重度を書き込む記法は、まるで配列のそれに見える。
  * ``{ordered, unique}`` 等にも注意したい。

* Figure 7.12 は上述の図式と等価なモデルを関連で表記したもの。

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
Figure 7.13 を見ると、クラス Constraint とその関連だけを仕様化するようだ。

7.6.3 Semantics
----------------------------------------------------------------------
Constraint
  * PackageableElement から派生している。

A_constrainedElement_constraint
  * Constraint から Element への関連。
  * 関連端 constrainedElement の多重度は ``* {ordered}`` である。
  * この constrainedElement が「制約が付随する対象」である。

A_specification_owningConstraint
  * Constraint から ValueSpecification への関連。
  * A_ownedElement_owner から制約 subsets で派生された関連。
  * 一つの Constraint が一つの ValueSpecification を所有する。
    具体的に言うと、specification は「制約が満足されているかどうかを示す値」なので、
    値としては true か false をとる。

A_ownedRule_context
  * Namespace から Constraint への関連。
  * 双方向に所有権？
  * この context は「制約を評価する際に参照対象となる」のか？

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
* Figure 7.14 はノートシンボルによる Constraint 表記例。
* Figure 7.15 はクラスのある属性にその Constraint を示す例。
* Figure 7.16 は二つの関連に共通する Constraint を示す例。

7.7 Dependencies
======================================================================
依存性を仕様化する。

7.7.1 Summary
----------------------------------------------------------------------
* Dependency は要素間の supplier/client 関係を意味する。
  supplier の修正が client に強く影響してよい。

7.7.2 Abstract Syntax
----------------------------------------------------------------------
Figure 7.17 は一部テキストが欠けている。

7.7.3 Semantics
----------------------------------------------------------------------
Dependency
  * DirectedRelationship かつ PackageableElement な概念。
    client の意味が supplier なしには完全ではないことを含意している。
  * モデル内の Dependency 関係の存在は、いかなる実行時の意味を持たない。
    そういうのは関連づいている NamedElement (client/supplier) が与える。

Usage
  * より特殊な Dependency である。
    ある NamedElement がその完全な実装や操作のために必要とする別の NamedElement(s) があるとき、
    その依存性を表す。

Abstraction
  * より特殊な Dependency である。
    ある抽象水準や視点では同じ概念を表現する NamedElements に関係する Dependency のこと？
  * この関係性は suppliers と clients との間の写像として定義してよい。
  * ``«Derive»``, ``«Refine»``, ``«Trace»`` などの定義済みステレオタイプを持つ。
    これは 22 章で仕様化する。

Realization
  * より特殊な Abstraction である。
    これは NamedElements の集合 2 つの間の Abstraction であり、
    一方 (supplier) は仕様を、他方 (client) は実装を表現する。

A_supplier_supplierDependency
  * Dependency から NamedElement への単方向関連。
  * A_target_directedRelationship の subsets 関連。
  * 関連端 supplier の多重度は ``1..*`` である。ゼロではあり得ない。

A_clientDependency_client
  * NamedElement と Dependency との間の双方向関連。
  * A_source_directedRelationship の subsets 関連。
  * 関連端 client の多重度は ``1..*`` である。ゼロではあり得ない。
  * 関連端 clientDependency は subsets される予定があるようだ。

A_mapping_abstraction
  * Abstraction から OpaqueExpression への composite 関連。
  * 図を見る限り OpaqueExpression によって mapping を表現する、と解釈できる。

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
* Figure 7.19 は謎のキーワード ``«Instantiate»`` を適用した Dependency の記法例。
* Figure 7.20 は Usage の記法例。
* Figure 7.21 は Realization の記法例。見慣れたクラス図だ。

7.8 Classifier Descriptions
======================================================================
機械生成による節。

7.9 Association Descriptions
======================================================================
機械生成による節。

.. include:: /_include/uml-refs.txt
