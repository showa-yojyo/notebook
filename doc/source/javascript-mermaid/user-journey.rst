=======================================================================
User Journey Diagram
=======================================================================

.. contents::
   :depth: 2

..

  《User journeys describe at a high level of detail exactly what steps
  different users take to complete a specific task within a system, application
  or website. This technique shows the current (as-is) user workflow, and
  reveals areas of improvement for the to-be workflow.》 (`Wikipedia
  <https://en.wikipedia.org/wiki/User_journey>`__)

  Mermaid can render user journey diagrams:

  .. mermaid:: ./uj.mmd
     :align: center
  .. literalinclude:: ./uj.mmd

Mermaid の文書を読むまでこれを知らなかった。いったん知れば何かの役に立つこともあ
るか。

  Each user journey is split into sections, these describe the part of the task
  the user is trying to complete.

  Tasks syntax is

  .. code:: text

     Task name: <score>: <comma separated list of actors>

実際に描画される図式とコードを比較すれば、構文はおのずと理解できる。ただし
``<score>`` の項目については詳細を述べて欲しい。
