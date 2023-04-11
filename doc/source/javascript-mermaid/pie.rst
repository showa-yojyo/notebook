======================================================================
Pie chart diagrams
======================================================================

.. contents::
   :depth: 2

..

  Mermaid can render Pie Chart diagrams.

  .. literalinclude:: /_include/p-pets.mmd
     :language: default
  .. mermaid:: /_include/p-pets.mmd
     :align: center

円グラフを HTML 上に描きたくなる状況が思い浮かばぬが、習得しよう。

Syntax
======================================================================

  Drawing a pie chart is really simple in mermaid.

  .. code:: text

     [pie] [showData] (OPTIONAL)
          [title] [titlevalue] (OPTIONAL)
           "[datakey1]" : [dataValue1]
           "[datakey2]" : [dataValue2]
           "[datakey3]" : [dataValue3]
           ...

円グラフを多用する執筆者は、上のテキストをエディターのスニペッツにしておくといい
かもしれない。

Example
======================================================================

.. literalinclude:: /_include/p-elements.mmd
   :language: default
.. mermaid:: /_include/p-elements.mmd
   :align: center

Configuration
======================================================================

オプション ``textPosition`` はスライスラベルの軸方向の位置を ``0.0`` から ``1.0``
までの値で指定する。この数は中心から円周までに対応する。
