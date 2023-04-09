======================================================================
State diagrams
======================================================================

  Mermaid can render state diagrams. The syntax tries to be compliant with the
  syntax used in PlantUml as this will make it easier for users to share
  diagrams between mermaid and PlantUml.

.. contents::
   :depth: 2

.. mermaid::
   :align: center

   stateDiagram-v2
       [*] --> Still
       Still --> [*]

       Still --> Moving
       Moving --> Still
       Moving --> Crash
       Crash --> [*]

State diagram については図式名が ``stateDiagram`` と ``stateDiagram-v2`` の二つ
用意されている。以下、後者を用いる。

States
======================================================================

  A state can be declared in multiple ways. The simplest way is to define a
  state with just an id:

  .. code:: text

     stateDiagram-v2
         stateId

  Another way is by using the ``state`` keyword with a description as per below:

  .. code:: text

     stateDiagram-v2
         state "This is a state description" as s2

  Another way to define a state with a description is to define the state id
  followed by a colon and the description:

  .. code:: text

     stateDiagram-v2
         s2 : This is a state description

Flowchart のノードの定義法とは異なるようだが、実現したいことは同じようだ。

Transitions
======================================================================

  Transitions are path/edges when one state passes into another. This is
  represented using text arrow, ``-->``.

  When you define a transition between two states and the states are not already
  defined the undefined states are defined with the id from the transition. You
  can later add descriptions to states defined this way.

  .. code:: text

     stateDiagram-v2
         s1 --> s2

Class diagram の構文でも見られた、ノード二つとリンクを同時に定義する記法だ。

  It is possible to add text to a transition. To describe what it represents.

  .. code:: text

     stateDiagram-v2
         s1 --> s2: A transition

矢印にテキストをオーバーレイしたい状況がない。

Start and End
======================================================================

  There are two special states indicating the start and stop of the diagram.
  These are written with the ``[*]`` syntax and the direction of the transition
  to it defines it either as a start or a stop state.

  .. code:: text

     stateDiagram-v2
         [*] --> s1
         s1 --> [*]

開始状態と停止状態を同じ記号で指定することに注意。描画では UML 様式になる。

Composite states
======================================================================

入れ子を定義する ``state`` 構文を学習する。

  In a real world use of state diagrams you often end up with diagrams that are
  multidimensional as one state can have several internal states. These are
  called composite states in this terminology.

  In order to define a composite state you need to use the state keyword
  followed by an id and the body of the composite state between ``{}``. See the
  example below:

  .. code:: text

     stateDiagram-v2
         [*] --> First
         state First {
             [*] --> second
             second --> [*]
         }

入れ子を多段にすることもできる（引用省略）。

  You can also define transitions also between composite states:

  .. code:: text

     stateDiagram-v2
         [*] --> First
         First --> Second
         First --> Third

         state First {
             [*] --> fir
             fir --> [*]
         }
         state Second {
             [*] --> sec
             sec --> [*]
         }
         state Third {
             [*] --> thi
             thi --> [*]
         }

  *You cannot define transitions between internal states belonging to different
  composite states*

その CANNOT は UML の規則か。

Choice
======================================================================

次は状態分岐の構文を習う。

  Sometimes you need to model a choice between two or more paths, you can do so
  using ``<<choice>>``.

  .. code:: text

     stateDiagram-v2
         state if_state <<choice>>
         [*] --> IsPositive
         IsPositive --> if_state
         if_state --> False: if n < 0
         if_state --> True : if n >= 0

状態図内の条件分岐の指定はコード量が多くなりがちだ。

Forks
======================================================================

``<<fork>>`` と ``<<join>>`` を学習する。図式内で暗い棒として表現される。

  It is possible to specify a fork in the diagram using ``<<fork>>``.

.. code:: text

      stateDiagram-v2
       state fork_state <<fork>>
         [*] --> fork_state
         fork_state --> State2
         fork_state --> State3

       state join_state <<join>>
         State2 --> join_state
         State3 --> join_state
         join_state --> State4
         State4 --> [*]

Notes
======================================================================

UML 仕様書で言うところのコメントに相当するものを定義することが可能だ。
次の例のように ``note ... of ...`` と ``end note`` の間にテキストを指示する。

  Here you can choose to put the note to the *right of* or to the *left of* a
  node.

  .. code:: text

     stateDiagram-v2
         State1: The state with a note
         note right of State1
             Important information! You can write
             notes.
         end note
         State1 --> State2
         note left of State2 : This is the note to the left.

Sequence diagram にある構文と同様だ。しかし、これは left なのか？

Concurrency
======================================================================

  As in PlantUml you can specify concurrency using the ``--`` symbol.

遷移指定の間に水平罫線のイメージでこれを記す。コードから連想されるように図式内の
部分状態が区画に分かれる。

  .. code:: text

     stateDiagram-v2
         [*] --> Active

         state Active {
             [*] --> NumLockOff
             NumLockOff --> NumLockOn : EvNumLockPressed
             NumLockOn --> NumLockOff : EvNumLockPressed
             --
             [*] --> CapsLockOff
             CapsLockOff --> CapsLockOn : EvCapsLockPressed
             CapsLockOn --> CapsLockOff : EvCapsLockPressed
             --
             [*] --> ScrollLockOff
             ScrollLockOff --> ScrollLockOn : EvScrollLockPressed
             ScrollLockOn --> ScrollLockOff : EvScrollLockPressed
         }

Setting the direction of the diagram
======================================================================

  With state diagrams you can use the direction statement to set the direction
  which the diagram will render like in this example.

  .. code:: text

     stateDiagram
         direction LR
         [*] --> A
         A --> B
         B --> C
         state B {
             direction LR
             a --> b
         }
         B --> D

Class diagram と同じ仕様だ。``direction RL`` を ``direction LR`` やその他に書き
換えて表示を確認するといい。

Comments
======================================================================

Sequence diagram や Class diagram のコメントと同じ仕様と思いきや：

  Comments can be entered within a state diagram chart, which will be ignored by
  the parser. Comments need to be on their own line, and must be prefaced with
  ``%%`` (double percent signs). Any text after the start of the comment to the
  next newline will be treated as a comment, including any diagram syntax

  .. code:: text

     stateDiagram-v2
         [*] --> Still
         Still --> [*]
     %% this is a comment
         Still --> Moving
         Moving --> Still %% another comment
         Moving --> Crash
         Crash --> [*]

本文の記述と異なり、この例の ``%% another comment`` 部分も描画を見るとコメント扱いだ。

Styling with classDefs
======================================================================

最近になってこの節が執筆されたようだ。

  As with other diagrams (like flowcharts), you can define a style in the
  diagram itself and apply that named style to a state or states in the diagram.

  These are the current limitations with state diagram classDefs:

  1. Cannot be applied to start or end states
  2. Cannot be applied to or within composite states

入れ子構造の内側にはスタイルを指定しにくいということだろう。

  You define a style using the ``classDef`` keyword, which is short for "class
  definition" (where "class" means something like a CSS class) followed by a
  name for the style, and then one or more property-value pairs. Each
  property-value pair is a valid CSS property name followed by a colon (``:``)
  and then a value.

次の定義例は ``movement`` という名前のスタイルを定義しており、テキストを斜体で描
画する：

  .. code:: text

     classDef movement font-style:italic;

次の定義例はプロパティーを複数指定する：

  .. code:: text

     classDef badBadEvent fill:#f00,color:white,font-weight:bold,stroke-width:2px,stroke:yellow

Apply classDef styles to states
----------------------------------------------------------------------

定義した ``classDef`` を状態ノードなどに割り当てる方法を習得しよう。

  1. use the ``class`` keyword to apply a ``classDef`` style to one or more
     states in a single statement, or
  2. use the ``:::`` operator to apply a ``classDef`` style to a state as it is
     being used in a transition statement (e.g. with an arrow to/from another
     state)

State diagram コード片の例。``movement`` および `` badBadEvent`` を ``classDef``
名とする。まずキーワード記法では次のようになる：

.. code:: text

   class Crash badBadEvent
   class Moving, Crash movement

トリプルコロン記法では次のように、エッジ指定行のノードの右側に ``classDef`` 名を
付加すればいい：

.. code:: text

   [*] --> Still:::notMoving
   Still --> [*]
   Still --> Moving:::movement
   Moving --> Still
   Moving --> Crash:::movement
   Crash:::badBadEvent --> [*]

Spaces in state names
----------------------------------------------------------------------

  Spaces can be added to a state by first defining the state with an id and then
  referencing the id later.

States 節で述べた仕様とスタイル指定の複合が成立するという記述だ。
