======================================================================
8 Values
======================================================================

UML 2.5 pp. 69-96 に関するノート。

.. contents:: ノート目次
   :depth: 2

8.1 Summary
======================================================================

* この章では値の仕様を述べる。一般には、ValueSpecification とは意味論的にゼロ個
  以上の値をもたらすとみなされるモデル要素である。
* 次の各節で UML で利用可能な ValueSpecifications のさまざまな種類を述べる。

8.2 Literals
======================================================================

8.2.1 Summary
----------------------------------------------------------------------

* LiteralSpecification とはリテラル値を指定する ValueSpecification である。UML
  標準 PrimitiveTypes のそれぞれに対して LiteralSpecification の別々の種類のもの
  があり、それぞれ対応するテキストによるリテラル表記法に、「値が欠けている」こ
  とを表現する「空」リテラルを共にする。

8.2.2 Abstract Syntax
----------------------------------------------------------------------

* Figure 8.1 Literals

  * ここには 6 種類の LiteralSpecification の具象要素が存在する。次節で意味を仕
    様化する。
  * 名前のある関連が一つもない。

8.2.3 Semantics
----------------------------------------------------------------------

* LiteralSpecifications は 6 種類存在する。

  #. LiteralNull は値の欠損を明示的に模すために用いられることを意図されている。

     * 下限がゼロである多重度の MultiplicityElement においては、これは空集合に対
       応する。 Element に対して値を何も指定しないことと同値である。

  #. LiteralString は PrimitiveType String の定数値を指定する。

     * String は文字の列として指定されるものの、String 値は UML では組み込み型と
       みなされ、ゆえに内部構造は UML 意味論の部分として指定されない。

  #. LiteralInteger は PrimitiveType Integer の定数値を指定する。
  #. LiteralBoolean は PrimitiveType Boolean の定数値を指定する。
  #. LiteralUnlimitedNatural は PrimitiveType UnlimitedNatural の定数値を指定す
     る。
  #. LiteralReal は PrimitiveType Real の定数値を指定する。

* :doc:`./ch21-primitive-types` も併せて参照したい。

8.2.4 Notation
----------------------------------------------------------------------

* LiteralSpecifications はテキスト的に表記される。

  * LiteralNull の記法は使用する状況に依るが、たいていは ``"null"`` のように記
    す。
  * LiteralString は文字列を二重引用符で囲む。引用符自身はリテラル値に含まれな
    い。
  * LiteralInteger は十進数の列として示す。
  * LiteralBoolean は ``true`` または ``false`` で示す。
  * LiteralUnlimitedNatural で注意を要するのは、その値が ``unlimited`` な場合の
    記法と意味である。記法は単にアスタリスク一文字であり、意味は「値の上限に指定
    がない」と指定されていると解釈する。
  * LiteralReal の記法は p. 70 の BNF 記法を見る限り、C/C++ 言語の ``double`` の
    それに酷似している感じ。

8.3 Expressions
======================================================================

8.3.1 Summary
----------------------------------------------------------------------

* Expressions とは、計算から生じる値を指定する ValueSpecifications である。

8.3.2 Abstract Syntax
----------------------------------------------------------------------

* Figure 8.2 Expressions

  * この図式からは 2 系統の Expression が存在することがわかる。
    Expression 系統と OpaqueExpression である。

``A_operand_expression``
  * Expression から ValueSpecification への composite 関連（単方向）。
  * 関連端 ``operand`` には制約 ``{ordered}`` がある。当然だ。

    * もし ``operands`` がないならば、この Expression は端末ノードを表す。
    * ある場合は、この Expression は ``operands`` に適用される記号により与えられ
      る演算子を表す。

  * ``A_ownedElement_owner`` を subsets する。

``A_subExpression_owningExpression``
  * StringExpression から StringExpression への composite 関連（双方向）。
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

* Expression は木構造として指定される。

  * この木構造の各ノードは ``symbol`` と ``operands`` の任意の集合とで構成され
    る。
  * もし ``operands`` がなければ、Expression は終端ノードを表現する。あるなら
    ば、Expression は ``operands`` に適用する ``symbol`` により与えられる演算子
    を表現する。

* Expression はまずは ``operands`` のそれぞれを評価し、次に Expression
  ``symbol`` により描写される演算を実施することで評価されて、その結果
  ``operand`` 値を生じる。

8.3.3.2 StringExpression
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* StringExpression とは、部分文字列を連結することで得られる String 値を指定する
  Expression である。

  * 部分文字列（複数形）はLiteralString ``operands`` のリストとしてか、
    StringExpression ``subExpressions`` のリストとしてかの、どちらか一方で与えら
    れる。両者を混ぜることは許されない。

* StringExpression の意図は Templates での NamedElements の名前を指定することに
  利用するものである。

  * StringExpression 全体か、``subExpressions`` の一つまたはそれを超えるどちらか
    一方がTemplateParameters の ParameterableElements として用いられてよく、
    NamedElement の名前がそのテンプレートの内側で引数化されることを許す。

8.3.3.3 Opaque Expression
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* OpaqueExpression は UML Behavior の言葉によるか、UML 以外の言語でのテキストの
  言明に基づいたものかのどちらかの値の集合の計算を指定する。
* OpaqueExpression には値を計算する手段の代替を表現するテキスト Strings の列から
  なる ``body`` があってよい。
* OpaqueExpression には戻り値以外の Parameters がないように制限された UML
  Behavior により定義されてもよい。
* もし OpaqueExpression に一つを超える ``body`` 文字列があるか、一つまたはそ
  れを超える ``body`` 文字列に加えて ``behavior`` をもあるならば、``bodies`` や
  ``behavior`` のうちのどれもが OpaqueExpression を評価するのに用いられてもよ
  い。UML の仕様としてはこの選択がどのようになされるかは決定しない。

8.3.4 Notation
----------------------------------------------------------------------

8.3.4.1 Expressions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``operands`` がない Expression は単にその ``symbol`` により表記する。

  * この場合引用符は用いない。

* ``operands`` がある Expression は ``symbol`` により表記してよく、続いてその
  ``operands`` を含む丸括弧を記し、カンマで区切る。

8.3.4.2 OpaqueExpression
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* OpaqueExpression が一つまたはそれを超える ``body`` Strings を有するとき、こ
  れらはそれの含む要素の文脈で OpaqueExpression を表示するのに用いられる。
* OpaqueExpression に対して ``languages`` が指定されていれば、対応する各
  ``body`` String の前に``language`` の名前を中括弧に入れて表示してよい。
* ``language`` にその言語名を定義する仕様があるならば、OpaqueExpression で使わ
  れるその言語名がその言語仕様で現れる通りに正確に綴られ大文字で書かれるべきであ
  る。

8.3.5 Examples
----------------------------------------------------------------------

8.3.5.1 Expressions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* 例えば ``a > 0`` みたいな表記は OpaqueExpression であるようだ。

8.3.5.2 Opaque Expressions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``{OCL} i > j and self.size > i`` のようにするらしい。

8.4 Time
======================================================================

8.4.1 Summary
----------------------------------------------------------------------

* この節では、簡素な時間モデルに基づいた値を生じる TimeExpression と Duration を
  定義する。

  * この簡素なモデルは、時間と時間の測定にまつわる複雑な様相を安全に無視できる状
    況のための近似を意図している。

8.4.2 Abstract Syntax
----------------------------------------------------------------------

* Figure 8.3 Time and Duration

  * 一箇所を除いて左右対称なグラフとなっている。

``A_expr_timeExpression``, ``A_expr_duration``
  * それぞれ TimeExpression, Duration から ValueSpecification への composite な
    関連（単方向）。
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
  * それぞれ TimeExpression, Duration から Observation への関連（単方向）。
  * 関連端 ``observation`` の多重度は ``*`` である。
  * 上記関連のノートを参照。

``A_event_timeObservation``, ``A_event_durationObservation``
  * それぞれ TimeObservation, DurationObservation から NamedElement への関連（単
    方向）。
  * 関連端 ``event`` の多重度は前者が 1 であり、後者は 1 または 2 である。かつ後
    者の ``event`` は ``{ordered}`` である。「入」「出」の順だろう。

8.4.3 Semantics
----------------------------------------------------------------------

8.4.3.1 Time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* UML の構造に関するモデリング構成要素が特定の時点における実体の性質を模すのに用
  いられる。

  * 事象 (event) とは、Property の値の変化や Activity の実行の開始など、モデル化
    されようとしている性質と挙動に関して興味のある何かが起こる (happen) 特定の時
    点に起こり (occur) 得る何かの仕様である。

* この概念での時間 (time) とは、単に事象の発生を整理する座標である。
* 期間 (duration) は二つの事象の発生の間の時間の期間 (period) であり、それらの事
  象の時間座標の差として計算される。

  * モデル Element に挙動の効果があれば、この効果はある期間上に起こり得る。この
    期間の開始事象は Element の入場 (entering) として知られ、終了事象は Element
    の退場として知られる。

8.4.3.2 Observations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Observation はモデルのある他の部分に相対して起こることがある事象の観測を描写す
  る。

  * 何か NamedElement に関係して起こるイベントの観測を示す。
  * 興味のある事象は、参照 NamedElement にいつ入場されるのかと退場されるのかであ
    る。

* Observations は二種類あり、TimeObservations と DurationObservations である。
* TimeObservation は特定の NamedElement への入場か退場のどちらかを観測する。

  * ``firstEvent`` が ``true`` ならば入場事象を、そうでなければ退場事象を観測す
    る。

* DurationObservation は一つか二つどちらかの NamedElements に関する期間を観測す
  る。

  * 一つ：観測期間は対象要素の入場事象と退場事象の、この順による出来事の間。
  * 二つ：観測期間は一つ目の要素の入場事象か退場事象どちらか一方と、続いて起こる
    二つ目の要素の入場事象か退場事象の間。
  * 属性 ``firstEvent`` も一つまたは二つある。意味は TimeObservation のそれと同
    じ。

8.4.3.3 TimeExpression
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* TimeExpression とは、ある時間的瞬間の時間座標を評価する ValueSpecification で
  あり、事によると与えられた ``observations`` の集合に関する。
* TimeExpression に ``expr`` があれば、これが TimeExpression の結果を生じるため
  に評価される。
* TimeExpression に ``expr`` がなければ、それには単一の TimeObservation が必要で
  あり、その ``observation`` の結果は ``TimeExpression`` の値である。

8.4.3.4 Duration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Duration とは、何らかの期間を時間で評価する ValueSpecification であり、事によ
  ると与えられた ``observations`` の集合に関する。
* Duration に ``expr`` があれば、これが DurationExpression の結果を生じるために
  評価される。
* Duration に ``expr`` がなければ、それは単一の DurationObservation が必要であ
  り、その ``observation`` の結果は ``Duration`` の値である。

8.4.4 Notation
----------------------------------------------------------------------

8.4.4.1 Observations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Observation の記法は、それが参照する NamedElement に線分を結べばよい。名前をそ
  の線分の NamedElement の反対側の端点付近に示す。

8.4.4.2 Time Expressions and Durations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* TimeExpression または Duration はその ``expr`` が一つあれば、そのテキスト表現
  により示す。なければ単一の関連 Observation で表現する。

  * Duration はある実装固有のテキスト的書式で与えられる相対時間の値である。
  * Duration はしばしば非負整数である「時間目盛」の個数で表現する。

8.4.5 Examples
----------------------------------------------------------------------

* Time はよく数値座標を使って表現されるが、TimeExpression の ``expr`` が数値に評
  価されるべき場合には、モデルでの慣習により当然とされることが認められる単位であ
  る。
* Duration は相対時間の値であり、それとして、期間の間を経過した参照時計上の時間
  目盛の Integer 個数など、しばしば非負の数として表現される。

8.5 Intervals
======================================================================

8.5.1 Summary
----------------------------------------------------------------------

* Interval とは値一組で定義される区間、範囲であり、何か他の Element が与えられた
  範囲にある値であることを断言するConstraints での用途を主とする。
* Intervals は値の型のどれに対しても定義できるが、対応する TimeConstraints と
  DurationConstraints の一部としての時間と期間に対して特に便利である。

8.5.2 Abstract Syntax
----------------------------------------------------------------------

* Figure 8.4 Intervals

  * 新規登場の抽象クラスはない。
  * Interval 系と IntervalConstraint 系を仕様化しているのだとわかる。
    両者の継承階層構造が並行している。

``A_min_interval``, ``A_max_interval``
  * Interval から ValueSpecification への関連（単方向）。
  * 関連端 ``min`` と ``max`` の多重度は 1 であり、意味的には ``min`` の評価値は
    ``max`` のそれを超えない。
  * 下記の関連はこれを redefines する。

  ``A_min_timeInterval``, ``A_max_timeInterval``
    * TimeInterval から TimeExpression への関連（単方向）。

  ``A_min_durationInterval``, ``A_max_durationInterval``
    * DurationInterval から Duration への関連（単方向）。

``A_specification_intervalConstraint``
  * IntervalConstraint から Interval への composite 関連（単方向）。
  * ``A_specification_owningConstraint`` を redefines する。
  * 関連端 ``specification`` の多重度は 1 である。
  * 以下の関連はこれを redefines する。

  ``A_specification_timeConstraint``
    * TimeConstraint から TimeInterval への composite 関連（単方向）。

  ``A_specification_durationConstraint``
    * DurationConstraint から DurationInterval への composite 関連（単方向）。

8.5.3 Semantics
----------------------------------------------------------------------

8.5.3.1 Intervals
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Interval は他の二つの ValueSpecifications, ``min`` と ``max`` で指定される
  ValueSpecification である。

* 時間の制約と一緒に利用する Interval の特殊化が二つある。

  * TimeInterval は TimeExpressions により与えられる二つの時間値の間の範囲を指
    定する。
  * DurationInterval は Durations により与えられる二つの期間値の間の範囲を指定
    する。

8.5.3.2 IntervalConstraint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* IntervalConstraint はその詳細が Interval で与えられる Constraint を定義する。
* 時間の制約を指定するのに利用する IntervalConstraint の特殊化が二つある。

  * TimeConstraint は制約する Interval が TimeInterval である単一の
    ``constrainedElement`` に対するIntervalConstraint を定義する。
  * DurationConstraint は制約する Interval が DurationInterval である
    ``constrainedElements`` の一つまたは二つのどちらか一方に対する
    IntervalConstraint を定義する。

    * もし 2 個の ``constrainedElements`` があれば、観測されようとしている期間の
      開始は、一番目の ``constrainedElement`` にある事象と二番目のそれにある事象
      の間にあることが許される。

8.5.4 Notation
----------------------------------------------------------------------

8.5.4.1 Intervals
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Interval の記法は ``<min-value> '..' <max-value>`` である。
* TimeInterval は ValueSpecification 要素のそれぞれが TimeExpression となる
  Interval の表記法を使って示される。
* DurationInterval は ValueSpecification 要素のそれぞれが Duration となる
  Interval の表記法を使って示される。

8.5.4.2 Interval Constraints
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* IntervalConstraint はその ``constrainedElement`` の注釈として示される。
  Constraints の一般的な記法を IntervalConstraint に対して用いてもよいが、上記の
  ようにテキストで記された Interval の仕様を共にする。
* 単一の ``constrainedElement`` の TimeConstraint は ``constrainedElement`` の図
  表的な表現とTimeConstraint の TimeInterval のテキスト表現の間にある小さい線分
  として示してよい。

8.5.5 Examples
----------------------------------------------------------------------

* Figure 8.5 Example of DurationConstraints and TimeConstraints

  * 何かのシーケンス図で、各 Constraint が設計図でよく見かける寸法のような図式で
    示されていることが理解できる。長さの代わりに ``{t..t+3}`` のように注釈されて
    いる。

8.6 Classifier Descriptions
======================================================================

機械生成による節。

8.7 Association Descriptions
======================================================================

機械生成による節。

.. include:: /_include/uml-refs.txt
