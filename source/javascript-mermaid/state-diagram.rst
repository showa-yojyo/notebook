=======================================================================
State diagrams
=======================================================================

.. contents::
   :depth: 2

《A state diagram is a type of diagram used in computer science and related
fields to describe the behavior of systems. State diagrams require that the
system described is composed of a finite number of states; sometimes, this is
indeed the case, while at other times this is a reasonable abstraction.》
`Wikipedia <https://en.wikipedia.org/wiki/State_diagram>`__

Mermaid can render state diagrams. The syntax tries to be compliant with the
syntax used in plantUml as this will make it easier for users to share diagrams
between mermaid and plantUml.

.. code:: mermaid

   stateDiagram-v2
       [*] --> Still
       Still --> [*]

       Still --> Moving
       Moving --> Still
       Moving --> Crash
       Crash --> [*]

Older renderer:

.. code:: mermaid

   stateDiagram
       [*] --> Still
       Still --> [*]

       Still --> Moving
       Moving --> Still
       Moving --> Crash
       Crash --> [*]

In state diagrams systems are described in terms of its states and how the
systems state can change to another state via a transitions. The example diagram
above shows three states **Still**, **Moving** and **Crash**. You start in the
state of Still. From Still you can change the state to Moving. In Moving you can
change the state either back to Still or to Crash. There is no transition from
Still to Crash.

.. admonition:: 学習者ノート

   State diagram については図式名が ``stateDiagram`` と
   ``stateDiagram-v2`` の二つ用意されている。上のグラフに関しては描画結果に差は認められない。

States
=======================================================================

A state can be declared in multiple ways. The simplest way is to define a state
id as a description.

.. code:: mermaid

   stateDiagram-v2
       s1

Another way is by using the state keyword with a description as per below:

.. code:: mermaid

   stateDiagram-v2
       state "This is a state description" as s2

Another way to define a state with a description is to define the state id
followed by a colon and the description:

.. code:: mermaid

   stateDiagram-v2
       s2 : This is a state description

.. admonition:: 学習者ノート

   Flowchart のノードの定義法とは異なるようだが、その差を伝えにくい。

Transitions
=======================================================================

Transitions are path/edges when one state passes into another. This is
represented using text arrow, ``-->``.

When you define a transition between two states and the states are not already
defined the undefined states are defined with the id from the transition. You
can later add descriptions to states defined this way.

.. code:: mermaid

   stateDiagram-v2
       s1 --> s2

.. admonition:: 学習者ノート

   Class diagram の構文でも見られた、ノード二つとリンクを同時に定義する記法だ。

It is possible to add text to a transition. To describe what it represents.

.. code:: mermaid

   stateDiagram-v2
       s1 --> s2: A transition

Start and End
=======================================================================

There are two special states indicating the start and stop of the diagram. These
are written with the ``[*]`` syntax and the direction of the transition to it
defines it either as a start or a stop state.

.. code:: mermaid

   stateDiagram-v2
       [*] --> s1
       s1 --> [*]

.. admonition:: 学習者ノート

   開始状態と停止状態を同じ記号で指定することに注意。UML では
   両者を異なる記号で表現すると規定していることを考えると、Mermaid のそれは興味深い。

Composite states
=======================================================================

In a real world use of state diagrams you often end up with diagrams that are
multi-dimensional as one state can have several internal states. These are
called composite states in this terminology.

In order to define a composite state you need to use the state keyword followed
by an id and the body of the composite state between ``{}``. See the example
below:

.. code:: mermaid

   stateDiagram-v2
       [*] --> First
       state First {
           [*] --> second
           second --> [*]
       }

.. admonition:: 学習者ノート

   入れ子を定義する ``state`` 構文を学習すること。

You can do this in several layers:

.. code:: mermaid

   stateDiagram-v2
       [*] --> First

       state First {
           [*] --> Second

           state Second {
               [*] --> second
               second --> Third

               state Third {
                   [*] --> third
                   third --> [*]
               }
           }
       }

You can also define transitions also between composite states:

.. code:: mermaid

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

.. admonition:: 学習者ノート

   その CANNOT は UML の規則か。

Choice
=======================================================================

Sometimes you need to model a choice between two or more paths, you can do so
using ``<<choice>>``.

.. code:: mermaid

   stateDiagram-v2
       state if_state <<choice>>
       [*] --> IsPositive
       IsPositive --> if_state
       if_state --> False: if n < 0
       if_state --> True : if n >= 0

.. admonition:: 学習者ノート

   状態図内の条件分岐の指定はコード量が多くなりがちだ。

Forks
=======================================================================

It is possible to specify a fork in the diagram using ``<<fork>>``.

.. code:: mermaid

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

.. admonition:: 学習者ノート

   ``<<fork>>`` と ``<<join>>`` を学習する。

Notes
=======================================================================

Sometimes nothing says it better then a Post-it note. That is also the case in
state diagrams.

Here you can choose to put the note to the *right of* or to the *left of* a
node.

.. code:: mermaid

       stateDiagram-v2
           State1: The state with a note
           note right of State1
               Important information! You can write
               notes.
           end note
           State1 --> State2
           note left of State2 : This is the note to the left.

.. admonition:: 学習者ノート

   Sequence diagram にある構文と同様だ。しかし、 これは left
   なのか？

Concurrency
=======================================================================

As in plantUml you can specify concurrency using the ``--`` symbol.

.. code:: mermaid

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

.. admonition:: 学習者ノート

   Mermaid コードから連想されるようにして、図式内の部分状態が区画に分かれる。

Setting the direction of the diagram
=======================================================================

With state diagrams you can use the direction statement to set the direction
which the diagram will render like in this example.

.. code:: mermaid

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


.. admonition:: 学習者ノート

   ``direction RL`` を ``direction LR`` やその他に書き換えて表示を確認するといい。

Comments
=======================================================================

Comments can be entered within a state diagram chart, which will be ignored by
the parser. Comments need to be on their own line, and must be prefaced with
``%%`` (double percent signs). Any text after the start of the comment to the
next newline will be treated as a comment, including any diagram syntax

.. code:: mermaid

   stateDiagram-v2
       [*] --> Still
       Still --> [*]
   %% this is a comment
       Still --> Moving
       Moving --> Still %% another comment
       Moving --> Crash
       Crash --> [*]

.. admonition:: 学習者ノート

   Sequence diagram でも利用可能だったものだ。

Styling
=======================================================================

Styling of the a state diagram is done by defining a number of css classes.
During rendering these classes are extracted from the file located at
src/themes/state.scss

.. admonition:: 学習者ノート

   この章ではスタイル付けについての文書がほとんど用意されていないようだ。
