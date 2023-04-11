======================================================================
Gantt diagrams
======================================================================

.. contents::
   :depth: 2

..

  A Gantt chart is a type of bar chart, first developed by Karol Adamiecki in
  1896, and independently by Henry Gantt in the 1910s, that illustrates a
  project schedule and the amount of time it would take for any one project to
  finish. Gantt charts illustrate number of days between the start and finish
  dates of the terminal elements and summary elements of a project.

プロジェクト管理理論を調べると必ず含まれるのがこの図式だ。Mermaid でこれを描くこ
とができる。

A note to users
======================================================================

最初に Gantt チャート一般の構造を理解する。垂直下方向にタスクが並び、上から
下に向かってタスクが完了する。これは Mermaid でも同じだ。

  Mermaid can render Gantt diagrams as SVG, PNG or a MarkDown link that can be
  pasted into docs.

Markdown で記述すると、普通の出力は HTML だから内部的には SVG で表現されることに
なる。

  .. literalinclude:: /_include/g-first.mmd
     :language: default
  .. mermaid:: /_include/g-first.mmd
     :align: center

タスクは所属する区画につき、完了日順に整列されている。

Syntax
======================================================================

  .. literalinclude:: /_include/g-syntax.mmd
     :language: default
  .. mermaid:: /_include/g-syntax.mmd
     :align: center

どれがキーワードでどれがリテラル文字列なのかわからない。

  It is possible to set multiple dependencies separated by space:

  .. literalinclude:: /_include/g-deps.mmd
     :language: default
  .. mermaid:: /_include/g-deps.mmd
     :align: center

タスク ``cherry`` の ``after b a`` の部分が複数依存を定義している。

Title
----------------------------------------------------------------------

  The ``title`` is an *optional* string to be displayed at the top of the Gantt
  chart to describe the chart as a whole.

タイトルはあってもなくても構わない。

Section statements
----------------------------------------------------------------------

  You can divide the chart into various sections, for example to separate
  different parts of a project like development and documentation.

プロジェクトの部署や組ごとにチャートの区画が対応するような造りにするのがコツかも
しれない。

  To do so, start a line with the ``section`` keyword and give it a name. (Note
  that unlike with the title for the entire chart, this name is required.

タイトルとは対照的に、区画名は指定必須だ。

Milestones
----------------------------------------------------------------------

  You can add milestones to the diagrams. Milestones differ from tasks as they
  represent a single instant in time and are identified by the keyword
  ``milestone``. Below is an example on how to use milestones. As you may
  notice, the exact location of the milestone is determined by the initial date
  for the milestone and the "duration" of the task this way: *initial date* +
  *duration*/2.

タスクが区間を表現するのとは対象的に、マイルストーンは瞬間を表現する。

  .. literalinclude:: /_include/g-milestome.mmd
     :language: default
  .. mermaid:: /_include/g-milestome.mmd
     :align: center

マイルストーンの指定方法に若干クセがある。それゆえ、上記 ``Initial milestone``
のコード上の指定は 17:50 よりも早い。

Setting dates
======================================================================

  ``dateFormat`` defines the format of the date input of your gantt elements.
  How these dates are represented in the rendered chart output are defined by
  ``axisFormat``.

Input date format
----------------------------------------------------------------------

  The default input date format is ``YYYY-MM-DD``. You can define your custom
  ``dateFormat``.

  .. code:: text

     dateFormat YYYY-MM-DD

  More info in: <https://day.js.org/docs/en/parse/string-format/>

Mermaid は JavaScript で実装されているので、同じく JavaScript 製パッケージ Day.js
を利用して日付を取り扱うようだ。Gantt チャートではその書式そのままを指定する。

Output date format on the axis
----------------------------------------------------------------------

  The default output date format is YYYY-MM-DD. You can define your custom
  ``axisFormat``, like ``2020-Q1`` for the first quarter of the year 2020.

  .. code:: text

     axisFormat %Y-%m-%d

  More info in: <https://github.com/d3/d3-time-format/tree/v4.0.0#locale_format>

今度は d3-time-format なる JavaScript パッケージを採用。

Axis ticks
----------------------------------------------------------------------

  The default output ticks are auto. You can custom your ``tickInterval``, like
  ``1day`` or ``1week``.

  The pattern is:

  .. code:: javascript

     /^([1-9][0-9]*)(minute|hour|day|week|month)$/;

  More info in: <https://github.com/d3/d3-time#interval_every>

Output in compact mode
======================================================================

  The compact mode allows you to display multiple tasks in the same row. Compact
  mode can be enabled for a gantt chart by setting the display mode of the graph
  via preceeding YAML settings.

  .. literalinclude:: /_include/g-compact-mode.mmd
     :language: default
  .. mermaid:: /_include/g-compact-mode.mmd
     :align: center

コンパクトモードを適用するのに front matter 部分に ``displayMode: compact`` と書
く。チャートの同一行にタスクが複数あり得るようになる。

Comments
======================================================================

これまで見てきた他の図式で用いられてきたコメントの構文と同じだ。``%%`` から行末
までがコメント扱いとなる。

  .. code:: text

     gantt
         title A Gantt Diagram
         %% this is a comment
         dateFormat  YYYY-MM-DD
         section Section
         A task           :a1, 2014-01-01, 30d
         Another task     :after a1  , 20d
         section Another
         Task in sec      :2014-01-12  , 12d
         another task     : 24d

Styling
======================================================================

本文参照。

Today marker
======================================================================

  You can style or hide the marker for the current date. To style it, add a
  value for the ``todayMarker`` key.

  .. code:: text

     todayMarker stroke-width:5px,stroke:#0f0,opacity:0.5

  To hide the marker, set ``todayMarker`` to ``off``.

  .. code:: text

     todayMarker off

Configuration
======================================================================

  ``mermaid.ganttConfig`` can be set to a JSON string with config parameters or
  the corresponding object.

  .. code:: javascript

     mermaid.ganttConfig = {
         titleTopMargin: 25,
         barHeight: 20,
         barGap: 4,
         topPadding: 75,
         sidePadding: 75
     }

Possible configuration params:
----------------------------------------------------------------------

``mirrorActor`` と ``bottomMarginAdj`` というのがある。本文参照。

Interaction
======================================================================

  It is possible to bind a click event to a task. The click can lead to either a
  javascript callback or to a link which will be opened in the current browser
  tab.

チャート上のタスクに対するクリックイベント処理を定義できる。コード例は本書参照。
Flowchart など、他の図式でも定義できるものがある。

  .. code:: text

     click taskId call callback(arguments)
     click taskId href URL

  * ``taskId`` is the id of the task
  * ``callback`` is the name of a javascript function defined on the page
    displaying the graph, the function will be called with the ``taskId`` as the
    parameter if no other arguments are specified.
