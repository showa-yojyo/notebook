======================================================================
8 Values
======================================================================
UML 2.5 pp. 69-96 に関するノート。

.. contents:: ノート目次

8.1 Summary
======================================================================
この章では UML における ValueSpecification を頂点とする、
値指定のためのモデル要素群の仕様を述べていく。

8.2 Literals
======================================================================

8.2.1 Summary
----------------------------------------------------------------------
LiteralSpecification はリテラル値を指定する ValueSpecification である。
LiteralSpecification は ValueSpecification 同様に（まだ）抽象要素で、
この派生要素に UML 標準の「基本型」(PrimitiveType) 要素が同抽象階層に並ぶ設計。

8.2.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 8.1 Literals

  * ここには 6 種類の LiteralSpecification の具象要素が存在する。
    次節で意味を仕様化する。

  * 名前のある関連が一つもない。

8.2.3 Semantics
----------------------------------------------------------------------
*ValueSpecification*
  * これは TypedElement かつ PackageableElement である。
  * 今のところそれ以外の仕様に関する情報が出て来ていない？

*LiteralSpecification*
  * これはリテラル値を指定する ValueSpecification である。

LiteralNull
  * どこで用いられるかに依るが、何らかの空要素を指定する LiteralSpecification である。
  * ゆえに何の属性も持たない。

LiteralString
  * 基本型の文字列の定数値を指定する LiteralSpecification である。
  * value という String 値の属性を持つ。

LiteralInteger
  * 基本型の整数定数値を指定する LiteralSpecification である。
  * value という Integer 値の属性を持つ。
  * デフォルト値は 0 となる。

LiteralBoolean
  * 基本型のブーリアン定数値を指定する LiteralSpecification である。
  * value という Boolean 値の属性を持つ。
  * デフォルト値は false となる。

LiteralUnlimitedNatural
  * 基本型の非負整数定数値を指定する LiteralSpecification である。
  * value という UnlimitedNatural 値の属性を持つ。
  * デフォルト値は 0 となる。

LiteralReal
  * 基本型の実数定数値を指定する LiteralSpecification である。
  * value という Real 値の属性を持つ。

:doc:`./primitive-types` も併せて参照したい。

8.2.4 Notation
----------------------------------------------------------------------
これは普通の記法に準じると思っておいて問題ないだろう。

* LiteralNull の記法は使用する状況に依るが、たいていは "null" のように記す。
* LiteralString は文字列を二重引用符で囲む。引用符自身はリテラル値に含まれない。
* LiteralInteger は十進数の列として示す。
* LiteralBoolean は true または false で示す。
* LiteralUnlimitedNatural で注意を要するのは、その値が unlimited な場合の記法と意味である。
  記法は単にアスタリスク一文字であり、
  意味は「値の上限に指定がない」と指定されていると解釈する。
* LiteralReal の記法は p. 70 の BNF 記法を見る限り、
  C/C++ 言語の double のそれに酷似している感じ。

8.3 Expressions
======================================================================
Expression 系の ValueSpecification の仕様を説明する節。

8.3.1 Summary
----------------------------------------------------------------------
Expressions はある計算から導かれる値を指定する ValueSpecifications である。

8.3.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 8.2 Expressions

  * この図式からは 2 系統の Expression が存在することがわかる。
    Expression 系統と OpaqueExpression である。

8.3.3 Semantics
----------------------------------------------------------------------
Expression
  * ValueSpecification の一種である。
  * よくある数式版構文木の構成要素である。
  * 属性 symbol は文字列。数式の操作方法を表現する。

StringExpression
  * Expression かつ TemplateableElement の一種である。
  * LiteralString または StringExpression のリストを連結させた Expression である。
  * StringExpression の意図はテンプレートの状況における
    NamedElements の名前を指定することに利用するものである。
    StringExpression 全体か、
    一つ以上の subExpressions のどちらか一方が
    TemplateParameters の ParameterableElements として用いられてよい。

OpaqueExpression
  * ValueSpecification の一種である。
  * Behavior の言葉によるか、UML 外言語での記述に基づいた、
    値の集まりの計算を指定する Expression である。
  * 属性 body と language を持つか、
    Behavior と Parameter が関連するかのどちらかの場合がある。

  * もし OpaqueExpression が複数の body 文字列を持つか、
    body 文字列に加えて behavior をも持つならば、
    それらのうちのどれでもが OpaqueExpression を評価するのに用いられてもよい。
    UML の仕様としてはこの選択がどのようになされるかははっきりと決めない。

A_operand_expression
  * Expression から ValueSpecification への composite 関連（単方向）。
  * 関連端 operand には制約 ``{ordered}`` がある。当然だ。

    * もし operands を持たないならば、この Expression は端末ノードを表す。
    * 持つ場合は、この Expression は operands に適用される symbol により
      与えられる演算子を表す。

  * A_ownedElement_owner を subsets する。

A_subExpression_owningExpression
  * StringExpression から StringExpression への composite 関連（双方向）。
  * A_ownedElement_owner を subsets する。
  * 関連端 subExpression は ``{ordered}`` である。

A_behavior_opaqueExpression, A_result_opaqueExpression
  * OpaqueExpression から Behavior への関連（単方向）。
  * この関連は OpaqueExpression::body がない場合に意味を持つ。
  * 関連端 result は ``{readOnly}`` である。

8.3.4 Notation
----------------------------------------------------------------------
Expression
  * 属性 operand がない場合は、単にその symbol で記す。この場合引用符は用いない。
  * 属性 operand がある場合は、symbol と丸括弧とカンマを組み合わせてそれらしく記す。

OpaqueExpression
  * 属性 body と language を保つ場合、それらの記法規則に従い記す。

    * language の名前を中括弧に入れて、対応する各 body の前に表示してもよい。
    * language の名前の大文字小文字はオリジナル通りに表記すること。

8.3.5 Examples
----------------------------------------------------------------------
主に OpaqueExpression のノート。

* 例えば ``a > 0`` みたいな表記は OpaqueExpression であるようだ。
* ``{OCL} i > j and self.size > i`` のようにするらしい。

8.4 Time
======================================================================
ValueSpecification の時間に関係するモデルを説明する節となっている。

8.4.1 Summary
----------------------------------------------------------------------
* TimeExpression と Duration という 2 種類の時間を仕様化する。
  時間と時間の測定にまつわる複雑な観念を無視できるような状況における、
  単純な近似モデルとしての仕様になる。

8.4.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 8.3 Time and Duration

  * 一箇所を除いて左右対称なグラフとなっている。

8.4.3 Semantics
----------------------------------------------------------------------
いくつか用語の説明があるのでまとめたい。

event
  イベント、事象。
  英語辞書で表現されている意味では場所と時間に関わるが、
  ここでは時間のほうだけ拾ってしまってよい。

occur
  起こる。自動詞。

time
  ここで言う時間とは、単にイベントが起こることを命令する (order) 時間軸上の座標である。

duration
  期間でよい。二つのイベントの起こる時間の期間。
  これらのイベントの時間座標の差として計算される値。

entering, exiting
  それぞれ開始、終了の意。

クラスと関連をまとめる。

*Observation*
  * PackageableElement の一種である。
  * 何か NamedElement に関係して起こるイベントの観測を示す。
  * 興味のあるイベントとは、対象の NamedElement がいつ「入られた」または「出られた」かである。

  TimeObservation
    * Observation の一種である。
    * 特定の NamedElement に「入る」か「出る」かの一方を観測する。
    * 属性 firstEvent が true ならば「入る」であり、そうでなければ「出る」を観測する。
    * TimeObservation の結果とは、観測イベントの起こる時点である。

  DurationObservation
    * Observation の一種である。
    * 一つか二つどちらかの NamedElement に関係する期間を観測する。

      * 一つ：観測期間は対象要素の「入る」と「出る」イベントの、
        この順による出来事の間。

      * 二つ：観測期間は一つ目の要素の「入る」か「出る」どちらか一方と、
        続いて起こる二つ目の要素の「入る」か「出る」イベントの間。

    * 属性 firstEvent も一つまたは二つ持つ。意味は TimeObservation のそれと同じ。

TimeExpression, Duration
  * どちらも ValueSpecification の一種である。
  * 特定の時点（期間）を評価する。
  * 多分何か与えられた観測要素の集合に関係する時点（期間）である。
    下記の対応関連のノート参照。

A_expr_timeExpression, A_expr_duration
  * それぞれ TimeExpression, Duration から ValueSpecification への composite な関連（単方向）。
  * A_ownedElement_owner を subsets する。
  * 関連端 expr の多重度は ``0..1`` である。

  * TimeExpression (Duration) が expr を持つ場合、
    TimeExpression (Duration) の結果をもたらすために評価される。

    * expr は単一の値を評価する必要がある。
    * expr は関連端 observation を参照（次に説明する関連の関連端だが）してもよい。

      * observation がない場合、expr はある定数時点（期間）に評価する。

  * TimeExpression (Duration) が expr を持たない場合、
    単一の TimeObservation (DurationObservation) を持ち、
    かつその観測結果 observation がこの TimeExpression (Duration) の値でなければならない。

A_observation_timeExpression, A_observation_duration
  * それぞれ TimeExpression, Duration から Observation への関連（単方向）。
  * 関連端 observation の多重度は ``*`` である。
  * 上記関連のノートを参照。

A_event_timeObservation, A_event_durationObservation
  * それぞれ TimeObservation, DurationObservation から NamedElement への関連（単方向）。
  * 関連端 event の多重度は前者が 1 であり、後者は 1 または 2 である。
    かつ後者の event は ``{ordered}`` である。
    「入」「出」の順だろう。

8.4.4 Notation
----------------------------------------------------------------------
* Observation の記法は、それが参照する NamedElement に線分を結べばよい。
  名前をその線分の NamedElement の反対側の端点付近に示す。

* TimeExpression または Duration はその expr が一つあれば、
  そのテキスト表現により示す。なければ単一の関連 Observation で表現する。

  * Duration はある実装固有のテキスト的書式で与えられる相対時間の値である。
  * Duration はしばしば非負整数である「時間目盛」の個数で表現する。

8.4.5 Examples
----------------------------------------------------------------------
文章しかない。

8.5 Intervals
======================================================================

8.5.1 Summary
----------------------------------------------------------------------
* Interval とは値一組で定義される区間、範囲である。
  対象の Element がある与えられた範囲にあることを断言 (assert) するような
  Constraint で主に用いられる。

* どんな型の値によってでも定義できるが、
  特に便利なのは時間と期間に対してである。
  これらの型はそれぞれ TimeConstraint と DurationConstraint の部分となる。

8.5.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 8.4 Intervals

  * 新規登場の抽象クラスはない。
  * Interval 系と IntervalConstraint 系を仕様化しているのだとわかる。
    両者の継承階層構造が並行している。

8.5.3 Semantics
----------------------------------------------------------------------
Interval
  * ValueSpecification の一種である。
  * 他のふたつの ValueSpecifications (min, max) で指定される。

  TimeInterval, DurationInterval
    * Interval の一種である。
    * それぞれ TimeExpression, Duration の対に関連する Interval である。

IntervalConstraint
  * Constraint の一種である。
  * 詳細が値の範囲で与えられる。

  TimeConstraint, DurationConstraint
    * IntervalConstraint の一種である。
    * 制約になる範囲がそれぞれ TimeInterval, DurationInterval である
      IntervalConstraint である。
    * ともにブーリアン型属性 firstEvent を持つ。
      その多重度は前者が ``0..1`` であり、後者は ``0..2`` である。
      意味は値が true ならば「入」で、そうでなければ「出」である。

    * TimeConstraint は、関連する単一の constrainedElement の時間的制約を与える。

    * DurationConstraint は関連する constrainedElement の個数で意味が違ってくる。
      もし 2 個制約要素がある場合、観測されている期間の開始は、
      一番目の constrainedElement のイベントと二番目のそれのイベントの間にあってよい。

A_min_interval, A_max_interval
  * Interval から ValueSpecification への関連（単方向）。
  * 関連端 min と max の多重度は 1 であり、
    意味的には min の評価値は max のそれを超えない。
  * 下記の関連はこれを redefines する。

  A_min_timeInterval, A_max_timeInterval
    * TimeInterval から TimeExpression への関連（単方向）。

  A_min_durationInterval, A_max_durationInterval
    * DurationInterval から Duration への関連（単方向）。

A_specification_intervalConstraint
  * IntervalConstraint から Interval への composite 関連（単方向）。
  * A_specification_owningConstraint を redefines する。
  * 関連端 specification の多重度は 1 である。
  * 以下の関連はこれを redefines する。

  A_specification_timeConstraint
    * TimeConstraint から TimeInterval への composite 関連（単方向）。

  A_specification_durationConstraint
    * DurationConstraint から DurationInterval への composite 関連（単方向）。

8.5.4 Notation
----------------------------------------------------------------------
* Interval の記法の基本形は ``<min-value> '..' <max-value>`` である。
* IntervalConstraint はその constrainedElement の注釈で示される。
  Constraint の一般的な記法を IntervalConstraint に対して用いてもよい。
  中括弧の間に Interval の記法を適用することになる。

  * TimeConstraint と DurationConstraint のために定義された特別な記法は次節の見本で示す。

8.5.5 Examples
----------------------------------------------------------------------
* Figure 8.5 Example of DurationConstraints and TimeConstraints

  * 何かのシーケンス図で、
    各 Constraint が設計図でよく見かける寸法のような図式で示されていることが理解できる。
    長さの代わりに ``{t..t+3}`` のように注釈されている。

8.6 Classifier Descriptions
======================================================================
機械生成による節。

8.7 Association Descriptions
======================================================================
機械生成による節。

.. include:: /_include/uml-refs.txt
