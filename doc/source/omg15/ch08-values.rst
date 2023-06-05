======================================================================
8 Values
======================================================================

.. contents::
   :depth: 2

8.1 Summary
======================================================================

この章で値の仕様が述べられている。

   In general, a ValueSpecification is a model element that is considered
   semantically to yield zero or more values.

8.2 Literals
======================================================================

8.2.1 Summary
----------------------------------------------------------------------

LiteralSpecification とはリテラル値を指定する ValueSpecification である。

UML 標準 PrimitiveTypes のそれぞれに対して LiteralSpecification の異なる種類があ
り、それぞれ次の対応するテキストによるリテラル表記法がある：

* 「値が欠けている」ことを表現するリテラル
* 「空」リテラル

8.2.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 8.1 Literals

* ここには六種類の LiteralSpecification の具象要素が存在する。
* 名前のある関連が一つもない。

8.2.3 Semantics
----------------------------------------------------------------------

#. LiteralNull は値の欠損を明示的にモデル化するために用いられることを意図してい
   る。

   下限がゼロである多重度の MultiplicityElement においては、これは空集合に対応す
   る。Element に対して値がないことを指定することに相当する。

#. LiteralString は PrimitiveType String の定数値を指定する。

   String は文字の列として指定されるものの、String 値は UML では組み込み型とみな
   され、ゆえに内部構造は UML 意味論の一部として指定されない。

#. LiteralInteger は PrimitiveType Integer の定数値を指定する。
#. LiteralBoolean は PrimitiveType Boolean の定数値を指定する。
#. LiteralUnlimitedNatural は PrimitiveType UnlimitedNatural の定数値を指定す
   る。
#. LiteralReal は PrimitiveType Real の定数値を指定する。

:doc:`./ch21-primitive-types` も併せて参照したい。

8.2.4 Notation
----------------------------------------------------------------------

   LiteralSpecifications are notated textually.

* LiteralNull の記法は使用する状況に依って異なる。たいていは ``"null"`` のように記
  す。
* LiteralString は二重引用符で囲まれた一連の文字として示す。引用符自身はリテラル
  値に含まれない。用いられる文字集合は unspecified とする。
* LiteralInteger は十進数の列として示す。
* LiteralBoolean は ``true`` または ``false`` で示す。
* LiteralUnlimitedNatural で注意を要するのは、その値が ``unlimited`` な場合の記
  法と意味だ。記法は単にアスタリスク ``*`` 一文字であり、意味は「値の上限に指定
  がない」と指定されていると解釈する。

     not a value of “infinity”

* LiteralReal の記法は p. 70 の BNF 記法を見る限り、C/C++ 言語の ``double`` の
  それに酷似している：

     .. code:: bnf

        <natural-literal> ::= ('0'..'9')+
        <decimal-literal> ::= ['+' | '-' ] <natural-literal> | ['+' | '-' ] [<natural-literal>] '.' <natural-literal>
        <real-literal> ::= <decimal-literal> [ ('e' | 'E') ['+' | '-' ] <natural-literal> ]

8.3 Expressions
======================================================================

8.3.1 Summary
----------------------------------------------------------------------

   Expressions are ValueSpecifications that specify values resulting from a
   computation.

8.3.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 8.2 Expressions

この図式からは二系統の Expression が存在することがわかる。Expression 系統と
OpaqueExpression だ。

``A_operand_expression``
  Expression から ValueSpecification への複合関連（単方向）。

  * 関連端 ``operand`` には制約 ``{ordered}`` がある。当然だ。

    * もし ``operands`` がないならば、この Expression は端末ノードを表す。
    * ある場合は、この Expression は ``operands`` に適用される記号により与えられ
      る演算子を表す。

  * ``A_ownedElement_owner`` を subsets する。

``A_subExpression_owningExpression``
  StringExpression から StringExpression への複合関連（双方向）。

  * ``A_ownedElement_owner`` を subsets する。
  * 関連端 ``subExpression`` は ``{ordered}`` である。

``A_behavior_opaqueExpression``, ``A_result_opaqueExpression``
  * OpaqueExpression から Behavior への関連（単方向）。
  * この関連は ``OpaqueExpression::body`` がない場合に意味がある。
  * 関連端 ``result`` は ``{readOnly}`` である。

8.3.3 Semantics
----------------------------------------------------------------------

8.3.3.1 Expression
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   An Expression is specified as a tree structure. Each node in this tree
   structure consists of a ``symbol`` and an ``optional`` set of operands.

Expression はまずは ``operands`` のそれぞれを評価し、その結果に対して Expression
``symbol`` により描写される演算を実行することで評価される。

8.3.3.2 StringExpression
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A StringExpression is an Expression that specifies a String value that is
   derived by concatenating a list of substrings.

部分文字列は LiteralString ``operands`` のリストまたは StringExpression
``subExpressions`` のリストとして与えられる。両者を混在することは許されない。

StringExpression の用途は Template の文脈で NamedElement の名前を指定するもの
だ。

StringExpression 全体か、``subExpressions`` の一つ以上を TemplateParameters の
ParameterableElements として利用してよく、NamedElement の名前をそのテンプレート
内で引数化することを許す。

8.3.3.3 Opaque Expression
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

冒頭から何を言っているのか：

   An OpaqueExpression specifies the computation of a set of values either in
   terms of a UML Behavior or based on a textual statement in a language other
   than UML.

OpaqueExpression にはその値を計算する代替手段を表現するテキスト Strings の列で構
成される本体、``body`` があってもよい。UML はこれがどのような言語に対して解釈さ
れるかを定義しない。

   An OpaqueExpression may also be defined by a UML Behavior (see sub clause
   13.2) that is restricted to have only in Parameters and a return Parameter.

OpaqueExpression の値は Behavior を呼び出し、戻り Parameter で値を返すことで与え
られる。入力 Parameter は Behavior に値を渡すのに用いられる。

   If an OpaqueExpression has more than one ``body`` String, or a ``behavior``
   in addition to one or more ``body`` Strings, then any one of the ``bodies``
   or the ``behavior`` may be used to evaluate the OpaqueExpression.

UML はこの選択がどのようになされるかは決定しない。

8.3.4 Notation
----------------------------------------------------------------------

8.3.4.1 Expressions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``operands`` がない Expression は単にその ``symbol`` により表記する。この場合引
用符は用いない。

``operands`` がある Expression はその ``symbol`` とその ``operands`` を含むカン
マ区切りの丸括弧で表記してもよい。

8.3.4.2 OpaqueExpression
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

OpaqueExpression に ``body`` 文字列がある場合、これらの文字列は、その
OpaqueExpression を含む要素の文脈で表示するのに使用される。``body`` 文字列に対応
する言語が指定されている場合、適合性のあるツールが許可される言語を制限したり、特
定の既定言語を想定したりすることもかまわない。

   If ``languages`` are specified for an OpaqueExpression, then a ``language``
   name may be displayed in braces (``{}``) before the ``body`` String to which
   it corresponds.

8.3.5 Examples
----------------------------------------------------------------------

8.3.5.1 Expressions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   .. code:: text

      xor
      else
      plus(x, 1)
      x + 1

8.3.5.2 Opaque Expressions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   .. code:: text

      a > 0
      {OCL} i > j and self.size > i
      average hours worked per week

8.4 Time
======================================================================

8.4.1 Summary
----------------------------------------------------------------------

この節では、簡素な時間モデルに基づいた値を生じる TimeExpression と Duration を定
義する。この簡素なモデルは、時間と時間の測定にまつわる複雑な様相を安全に無視でき
る状況のための近似を意図している。次のことをカバーしていない：

   For example, in many distributed systems there is no global notion of time,
   only the notion of local time relative to each distributed element of the
   system. This relativity of time is not accounted for in the simple time
   model, nor are the effects resulting from imperfect clocks with finite
   resolution, overflows, drift, skew, etc.

8.4.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 8.3 Time and Duration

一箇所を除いて左右対称なグラフとなっている。

``A_expr_timeExpression``, ``A_expr_duration``
  それぞれ TimeExpression, Duration から ValueSpecification への複合関連（単方
  向）。

  * ``A_ownedElement_owner`` を subsets する。
  * 関連端 ``expr`` の多重度は ``0..1`` である。

  * TimeExpression (Duration) に ``expr`` がある場合、TimeExpression (Duration)
    の結果をもたらすために評価される。

    * ``expr`` は単一の値を評価する必要がある。
    * ``expr`` は関連端 observation を参照（次に説明する関連の関連端だが）しても
      よい。

      * ``observation`` がない場合、``expr`` はある定数時点（期間）に評価する。

  * TimeExpression (Duration) に ``expr`` がない場合、単一の TimeObservation
    (DurationObservation) があり、かつその観測結果 ``observation`` がこの
    TimeExpression (Duration) の値でなければならない。

``A_observation_timeExpression``, ``A_observation_duration``
  それぞれ TimeExpression, Duration から Observation への関連（単方向）。

  * 関連端 ``observation`` の多重度は ``*`` である。
  * 上記関連のノートを参照。

``A_event_timeObservation``, ``A_event_durationObservation``
  それぞれ TimeObservation, DurationObservation から NamedElement への関連（単方
  向）。

  * 関連端 ``event`` の多重度は前者が 1 であり、後者は 1 または 2 である。かつ後
    者の ``event`` は ``{ordered}`` である。「入」「出」の順だろう。

8.4.3 Semantics
----------------------------------------------------------------------

8.4.3.1 Time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

UML の構造に関するモデリング構成は特定の時点における実体の性質をモデル化するのに
用いられる。これに対して動作モデリング構成は、これらの性質が時間の経過につれてど
のように変換するかをモデリングするのに用いられる。

   An :dfn:`event` is a specification of something that may occur at a specific
   point in time when something of interest happens relative to the properties
   and behaviors being modeled, such as the change in value of a Property or the
   beginning of execution of an Activity.

定義が続く。

   :dfn:`Time` in this conception is simply a coordinate that orders the
   occurrence of events.

順序集合であるほうの時だ。時刻と言ったほうがいいかもしれない。

   A :dfn:`duration` is the period of time between two event occurrences,
   computed as the difference of the time coordinates of those events.

モデル Element に動作効果があれば、この効果はある持続時間にわたり発生することが
許される。

   The starting event of this duration is known as :dfn:`entering` the Element
   and the ending event is known as :dfn:`exiting` the Element.

逆に、この両者が決定されれば持続時間も決定される。

8.4.3.2 Observations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   An Observation denotes the observation of events that may occur relative to
   some other part of a model.

Observation はモデル内の NamedElement に対して行われる。関心のある出来事は参照先
の NamedElement が進入したり退出したりするときだ。参照される NamedElement が動作
要素でない場合、NamedElement に進入してから退出するまでの持続時間はゼロとみなさ
れる。

   There are two kinds of Observations, TimeObservations and
   DurationObservations.

   A TimeObservation observes either entering or exiting a specific
   NamedElement.

``firstEvent`` が真ならば進入イベントを、そうでなければ退場イベントを観測する。
結果は、観測されたイベントが発生した時刻だ。

   A DurationObservation observes a duration relative to either one or two
   NamedElements.

* 一つの場合：観測期間は対象要素の進入事象と退出事象の連続して発生する間の期間。
* 二つの場合：観測期間は最初の要素の進入または退出事象と、それに続く要素の
  の進入または退出事象との間の持続時間。

8.4.3.3 TimeExpression
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A TimeExpression is a ValueSpecification that evaluates to the time
   coordinate for an instant in time, possibly relative to some given set of
   observations.

TimeExpression に ``expr`` があれば、これが評価されて TimeExpression の結果を生
じる。TimeExpression に ``expr`` あるが ``observation`` がない場合、``expr`` は
ある定時間値に評価される。

TimeExpression に ``expr`` がない場合、単一の TimeObservation を持ち、その観測の
結果がその TimeExpression の値でなければならない。

8.4.3.4 Duration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   A Duration is a ValueSpecification that evaluates to some duration in time,
   possibly relative to some given set of ``observations``.

TimeExpression ``expr`` に関する性質が Duration にも当てはまる。前節参照。

8.4.4 Notation
----------------------------------------------------------------------

8.4.4.1 Observations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Observation の記法は、それが参照する NamedElement に付けられた線分で示されること
がある。名前をその線分の NamedElement の反対側の端点付近に示す。

8.4.4.2 Time Expressions and Durations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TimeExpression または Duration はその ``expr`` があれば、そのテキスト表現により
示す。なければ単一の関連 Observation で表現する。

Duration はある実装固有のテキスト形式で与えられる相対時間の値である。しばしば非
負整数である「時間目盛」の個数で表現される。

8.4.5 Examples
----------------------------------------------------------------------

Time はよく数値座標を使って表現されるが、TimeExpression の ``expr`` が数値に評
価される必要があり、単位はモデルの慣習で決まることがある。

Duration は相対時間の値であり、しばしば非負の数として表現される。この場
合、DurationExpression の ``expr`` は非負の数に評価されなければならない。

8.5 Intervals
======================================================================

8.5.1 Summary
----------------------------------------------------------------------

   An Interval is a range between two values, primarily for use in Constraints
   that assert that some other Element has a value in the given range.

Intervals は値の型あらゆるものに対して定義できるが、TimeConstraints と
DurationConstraints の一部として用いると特に便利だ。

8.5.2 Abstract Syntax
----------------------------------------------------------------------

   Figure 8.4 Intervals

* 新規登場の抽象クラスはない。
* Interval 系と IntervalConstraint 系を仕様化しているのだとわかる。両者の継承階
  層構造が並行している。

``A_min_interval``, ``A_max_interval``
  Interval から ValueSpecification への関連（単方向）。

  * 関連端 ``min`` と ``max`` の多重度は 1 であり、意味的には ``min`` の評価値は
    ``max`` のそれを超えない。
  * 下記の関連はこれを redefines する。

  ``A_min_timeInterval``, ``A_max_timeInterval``
    TimeInterval から TimeExpression への関連（単方向）。

  ``A_min_durationInterval``, ``A_max_durationInterval``
    DurationInterval から Duration への関連（単方向）。

``A_specification_intervalConstraint``
  IntervalConstraint から Interval への複合関連（単方向）。

  * ``A_specification_owningConstraint`` を redefines する。
  * 関連端 ``specification`` の多重度は 1 である。
  * 以下の関連はこれを redefines する。

  ``A_specification_timeConstraint``
    TimeConstraint から TimeInterval への複合関連（単方向）。

  ``A_specification_durationConstraint``
    DurationConstraint から DurationInterval への複合関連（単方向）。

8.5.3 Semantics
----------------------------------------------------------------------

8.5.3.1 Intervals
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   An Interval is a ValueSpecification specified using two other
   ValueSpecifications, the ``min`` and the ``max``.

これらの値に収まる値の集合。標準的な意味解釈は ``min`` と ``max`` は同じ型であっ
て、その型に全順序が定義されている Interval の対してしか与えられない。

時間の制約と一緒に利用する Interval の特殊化が二つある：

* TimeInterval は TimeExpressions により与えられる二つの時間値の間の範囲を指定す
  る。
* DurationInterval は Durations により与えられる二つの期間値の間の範囲を指定す
  る。

8.5.3.2 IntervalConstraint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   An IntervalConstraint defines a Constraint whose specification is given by an
   Interval (see also sub clause 7.6 on Constraints).

IntervalConstraint の ``constrainedElements`` はその Interval で指定された範囲内
の値を持つことが保証される。``constrainedElement`` がこの範囲外の値を持つ場
合、IntervalConstraint は違反となる。

時間の制約を指定するのに利用する IntervalConstraint の特殊化が二つある。

   A TimeConstraint defines an IntervalConstraint on a single
   ``constrainedElement`` in which the constraining Interval is a TimeInterval.
   A DurationConstraint defines an IntervalConstraint on either one or two
   ``constrainedElements`` in which the constraining Interval is a
   DurationInterval.

もし ``constrainedElements`` が二つあれば、観測される持続時間の開始は、最初の
``constrainedElement`` の事象と次のそれの事象の間にあることが許される。

8.5.4 Notation
----------------------------------------------------------------------

8.5.4.1 Intervals
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bnf

   <interval> ::= <min-value> ‘..’ <max-value>

TimeInterval は Interval の表記法を使って示され、ValueSpecification 要素それぞれ
が TimeExpression だ。

DurationInterval は ValueSpecification 要素それぞれが Duration である Interval
の表記法を使って示される。

8.5.4.2 Interval Constraints
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

IntervalConstraint はその ``constrainedElement`` の注釈として示される。
Constraints の一般的な記法を IntervalConstraint に対して用いてもよく、Interval
の指定は上記のようにテキストで表記される。

単一の ``constrainedElement`` の TimeConstraint は ``constrainedElement`` の図
表的な表現とTimeConstraint の TimeInterval のテキスト表現の間にある小さい線分
として示されることがある。

DurationConstraint はその ``constrainedElement`` を関連付ける図表的な表現を使用
して示されることがある。しかし、使用される記法は DurationConstraint が現れる図式
型に固有だ。

8.5.5 Examples
----------------------------------------------------------------------

   Figure 8.5 Example of DurationConstraints and TimeConstraints

Message の持続時間と OccurrenceSpecification 二つの間の持続時間に関連する
DurationConstraints の図式。Message の受信に関連する TimeConstraints も示されて
いる。

何かのシーケンス図で、各 Constraint が設計図でよく見かける寸法のような図式で示さ
れていることが理解できる。長さの代わりに ``{t..t+3}`` のように注釈されている。

8.6 Classifier Descriptions
======================================================================

機械生成による節。

8.7 Association Descriptions
======================================================================

機械生成による節。

.. include:: /_include/uml-refs.txt
