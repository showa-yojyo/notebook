=======================================================================
Class diagrams
=======================================================================

.. contents::
   :depth: 2

..

  Mermaid can render class diagrams.

  .. mermaid:: ./cd-animals.mmd
     :align: center
  .. literalinclude:: ./cd-animals.mmd

Syntax
=======================================================================

Class
-----------------------------------------------------------------------

まず、クラス部分の描画構成について述べている。

  A single instance of a class in the diagram contains three compartments:

  * The top compartment contains the name of the class. It is printed in bold
    and centered, and the first letter is capitalized. It may also contain
    optional annotation text describing the nature of the class.
  * The middle compartment contains the attributes of the class. They are
    left-aligned and the first letter is lowercase.
  * The bottom compartment contains the operations the class can execute. They
    are also left-aligned and the first letter is lowercase.

クラスノードの中が区画三つで垂直に分割されていて、それらは上からクラス名、属性リ
スト、操作リストを含む。テキストのスタイルはある程度固定されている。

次のように ``classDiagram`` 行でクラス図を宣言する。これはクラス一つを含む。

  .. code:: text

     ---
     title: Bank example
     ---
     classDiagram
         class BankAccount
         BankAccount : +String owner
         BankAccount : +Bigdecimal balance
         BankAccount : +deposit(amount)
         BankAccount : +withdrawl(amount)

タイトルはあってもなくても構わない。

Define a class
-----------------------------------------------------------------------

  There are two ways to define a class:

  * Explicitly using keyword ``class`` like ``class Animal`` which would define
    the ``Animal`` class.
  * Via a relationship which defines two classes at a time along with their
    relationship. For instance, ``Vehicle <|-- Car``.

  .. code:: text

     classDiagram
         class Animal
         Vehicle <|-- Car

第二の定義法はクラス二つをその関連と同時に定義すると取れる。

  Naming convention: a class name should be composed only of alphanumeric
  characters (including unicode), and underscores.

SHOULD であって MUST ではないことに注意。

Class labels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  In case you need to provide a label for a class, you can use the following syntax:

  .. code:: text

     classDiagram
         class Animal["Animal with a label"]
         class Car["Car with *! symbols"]
         Animal --> Car

  You can also use backticks to escape special characters in the label:

この構文はクラス図を模式的に用いるときに使えるか。

Defining Members of a class
-----------------------------------------------------------------------

  Mermaid distinguishes between attributes and functions/methods based on if the
  parenthesis ``()`` are present or not. The ones with ``()`` are treated as
  functions/methods, and all others as attributes.

  There are two ways to define the members of a class, and regardless of
  whichever syntax is used to define the members, the output will still be same.
  The two different ways are:

  * Associate a member of a class using ``:`` (colon) followed by member name,
    useful to define one member at a time. For example:

    .. code:: text

       classDiagram
           class BankAccount
           BankAccount : +String owner
           BankAccount : +BigDecimal balance
           BankAccount : +deposit(amount)
           BankAccount : +withdrawal(amount)

  * Associate members of a class using ``{}`` brackets, where members are
    grouped within curly brackets. Suitable for defining multiple members at
    once. For example:

    .. code:: text

       classDiagram
       class BankAccount{
           +String owner
           +BigDecimal balance
           +deposit(amount)
           +withdrawl(amount)
       }

後者の記法のほうがコード量が少なくて済む。あと、インデントをどうするかは取り決め
た方がいい。

Return Type
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Optionally you can end a method/function definition with the data type that
  will be returned (note: there must be a space between the final ``)`` and the
  return type).

戻り値の言明はオプショナル。

Generic Types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Members can be defined using generic types, such as ``List<int>``, for fields,
  parameters, and return types by enclosing the type within ``~`` (tilde).
  Nested type declarations such as ``List<List<int>>`` are supported.

  Generics can be represented as part of a class definition and also in the
  parameters or the return value of a method/function:

  .. code:: text

     classDiagram
       class Square~Shape~{
           int id
           List~int~ position
           setPoints(List~int~ points)
           getPoints() List~int~
       }

       Square : -List~string~ messages
       Square : +setMessages(List~string~ messages)
       Square : +getMessages() List~string~
       Square : +getDistanceMatrix() List~List~int~~

完全ではないが、C++ でいうクラステンプレートを対応している。プログラミング言語に
よっては上記の対応で事足りるのだろう。

Visibility
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

UML 準拠の記号が使える：

  To specify the visibility of a class member (i.e. any attribute or method),
  these notations may be placed before the member's name, but it is optional:

  * ``+`` Public
  * ``-`` Private
  * ``#`` Protected
  * ``~`` Package/Internal

抽象メソッド、静的メソッドの表現方法は次のようにする。後者の記法はフィールドにも
適用可能：

  You can also include additional *classifiers* to a method definition by adding
  the following notations to the end of the method, i.e.: after the ``()``:

  * ``*`` Abstract e.g.: ``someAbstractMethod()*``
  * ``$`` Static e.g.: ``someStaticMethod()$``

Defining Relationship
=======================================================================

  A relationship is a general term covering the specific types of logical
  connections found on class and object diagrams.

  .. code:: text

     [classA][Arrow][ClassB]

何の説明もなしに構文らしきものが記されている。クラス名とクラス名の間に矢印を指定
するということだ。

  There are different types of relations defined for classes under UML which are
  currently supported:

  ========= =============
  Type      Description
  ========= =============
  ``<|--``  Inheritance
  ``*--``   Composition
  ``o--``   Aggregation
  ``-->``   Association
  ``--``    Link (Solid)
  ``..>``   Dependency
  ``..|>``  Realization
  ``..``    Link (Dashed)
  ========= =============

欲しい矢印は全部あると思う。各種 association の理解に自身がない場合は UML の仕様
書を参照すること。ここに書き写してもいいか？

  We can use the labels to describe nature of relation between two classes.
  Also, arrowheads can be used in opposite directions as well:

  .. mermaid:: ./cd-relationships.mmd
     :align: center
  .. literalinclude:: ./cd-relationships.mmd

関係の名前を矢印の中央に描画することが可能だ。「矢印を逆向きにも使える」というの
はたいへん興味深い仕様だ。

Labels on Relations
-----------------------------------------------------------------------

前節でのラベル機能をなぜか繰り返して述べる。

  It is possible to add a label text to a relation:

  .. code:: text

     [classA][Arrow][ClassB]:LabelText

この用法を採用するのは珍しいかもしれない。

Two-way relations
-----------------------------------------------------------------------

  Relations can logically represent an N:M association:

  .. code:: text

     classDiagram
         Animal <|--|> Zebra

  Here is the syntax:

  .. code:: text

     [Relation Type][Link][Relation Type]

多方向関係の表現は難解なところがあるので私は使わないが、いちおうチェックする。
矢印の記法は単方向に準じる。

Cardinality / Multiplicity on relations
=======================================================================

  Multiplicity notations are placed near the ends of an association.

  The different cardinality options are:

  * ``1`` Only 1
  * ``0..1`` Zero or One
  * ``1..*`` One or more
  * ``*`` Many
  * ``n`` n
  * ``0..n`` zero to n
  * ``1..n`` one to n

  Cardinality can be easily defined by placing the text option within quotes
  ``"`` before or after a given arrow. For example:

  .. code:: text

     [classA] "cardinality1" [Arrow] "cardinality2" [ClassB]:LabelText

多重度の表現は基本的なので習得する。

  .. mermaid:: ./cd-cardinal.mmd
     :align: center
  .. literalinclude:: ./cd-cardinal.mmd

描画が怪しい。

Annotations on classes
=======================================================================

  It is possible to annotate classes with a specific marker text which is like
  meta-data for the class, giving a clear indication about its nature. Some common
  annotations examples could be:

  * ``<<Interface>>`` To represent an Interface class
  * ``<<Abstract>>`` To represent an abstract class
  * ``<<Service>>`` To represent a service class
  * ``<<Enumeration>>`` To represent an enum

  Annotations are defined within the opening ``<<`` and closing ``>>``. There are
  two ways to add an annotation to a class and regardless of the syntax used
  output will be same. The two ways are:

  * In a *separate line* after a class is defined. For example:

    .. code:: text

       classDiagram
         class Shape
           <<interface>> Shape
           Shape : noOfVertices
           Shape : draw()

  * In a *nested structure* along with class definition. For example:

    .. code:: text

       classDiagram
           class Shape{
               <<interface>>
               noOfVertices
               draw()
           }
           class Color{
               <<enumeration>>
               RED
               BLUE
               GREEN
               WHITE
               BLACK
           }

クラス記法（と勝手に呼んでいる）の場合にはクラス名の直後？に annotation を宣言す
る。

Comments
=======================================================================

Sequence diagram のコメントと同じ仕様だ。``%%`` マーカーを行頭に置くと行全体がコメ
ントとなり、行の途中からコメントを入れることはできない。

Setting the direction of the diagram
=======================================================================

  With class diagrams you can use the direction statement to set the direction in
  which the diagram will render:

  .. mermaid:: ./cd-direction.mmd
     :align: center
  .. literalinclude:: ./cd-direction.mmd

``direction RL`` を ``direction LR`` やその他に書き換えて表示を確認するといい。

Interaction
=======================================================================

Sequence diagram が対応しているのと同じ機能だ。現在私のブラウザーでツールチップ
が表示されないのも同じ。

  You would define these actions on a separate line after all classes have been
  declared.

  .. code:: text

     action className "reference" "tooltip"
     click className call callback() "tooltip"
     click className href "url" "tooltip"

  * *action* is either ``link`` or ``callback``, depending on which type of
    interaction you want to have called
  * *className* is the id of the node that the action will be associated with
  * *reference* is either the url link, or the function name for callback.
  * (*optional*) tooltip is a string to be displayed when hovering over element
    (note: The styles of the tooltip are set by the class .mermaidTooltip.)
  * note: callback function will be called with the nodeId as parameter.

Examples
-----------------------------------------------------------------------

Sequence diagram で見たように ``securityLevel:'loose'`` の指定が急所となる。例は
本文を参照。当ノートでは割愛。

Styling
=======================================================================

Styling a node
-----------------------------------------------------------------------

  It is possible to apply specific styles such as a thicker border or a
  different background color to individual nodes. This is done by predefining
  classes in css styles that can be applied from the graph definition using the
  ``cssClass`` statement or the ``:::`` short hand.

Flowchart の要領でクラスを表現する四角いオブジェクトにスタイルを与えることができ
る。

  .. code:: html

     <style>
       .styleClass > rect {
         fill: #ff0000;
         stroke: #ffff00;
         stroke-width: 4px;
       }
     </style>

何回見ても SVG のスタイルに見える。

  Then attaching that class to a specific node:

  .. code:: text

         cssClass "nodeId1" cssClass;

  It is also possible to attach a class to a list of nodes in one statement:

  .. code:: text

         cssClass "nodeId1,nodeId2" cssClass;

  A shorter form of adding a class is to attach the classname to the node using
  the ``:::`` operator:

  .. code:: text

     classDiagram
         class Animal:::styleClass

  Or:

  .. code:: text

     classDiagram
         class Animal:::styleClass {
             -int sizeInFeet
             -canEat()
         }

  ``cssClasses`` cannot be added using this shorthand method at the same time as
  a relation statement.

  Due to limitations with existing markup for class diagrams, it is not
  currently possible to define css classes within the diagram itself. Coming
  soon!

スタイル定義を図式単品に対して書き込めないのは、ちょっとしたクラス図を示したい場
合には不便かもしれない。そういう状況で凝ったスタイリングをしようとは考えないだろ
うが。

Default Styles
-----------------------------------------------------------------------

  The main styling of the class diagram is done with a preset number of css
  classes. During rendering these classes are extracted from the file located at
  :file:`src/themes/class.scss`.

事情は Sequence diagram のときと同じだ。本ノートでは割愛。本文を参照。

Configuration
=======================================================================

  Coming soon

いつになったら来るのだ。
