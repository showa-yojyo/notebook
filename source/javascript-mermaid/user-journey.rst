=======================================================================
User Journey Diagram
=======================================================================

《User journeys describe at a high level of detail exactly what steps different
users take to complete a specific task within a system, application or website.
This technique shows the current (as-is) user workflow, and reveals areas of
improvement for the to-be workflow.》
(`Wikipedia <https://en.wikipedia.org/wiki/User_journey>`__)

.. contents::
   :depth: 2

Mermaid can render user journey diagrams:

.. code:: mermaid

   journey
       title My working day
       section Go to work
         Make tea: 5: Me
         Go upstairs: 3: Me
         Do work: 1: Me, Cat
       section Go home
         Go downstairs: 5: Me
         Sit down: 5: Me

Each user journey is split into sections, these describe the part of the task
the user is trying to complete.

Tasks syntax is

.. code:: text

   Task name: <score>: <comma separated list of actors>

.. admonition:: 学習者ノート

   実際に描画される図式とコードを比較すれば、構文はおのずと理解できる。
   ただし ``<score>`` の項目については詳細を述べて欲しい。
