======================================================================
Deployment
======================================================================

.. contents::
   :depth: 2

Four ways of using mermaid
======================================================================

1. Using the Mermaid Live Editor at `mermaid.live <https://mermaid.live>`__.
2. Using mermaid plugins with programs you are familiar with.
3. Calling the Mermaid Javascript API.
4. Deploying Mermaid as a dependency.

.. note::

   It is our recommendation that you review all approaches, and choose the
   one that is best for your project.

.. admonition:: 学習者ノート

   この方法群のうち、2. と 3. を習得したい。

1. Using the Live Editor
======================================================================

Available at `mermaid.live <https://mermaid.live>`__

.. code:: mermaid

   graph TB
       A[Enter Chart Definition]
       B[Preview]
       C{Decide}
       D[Keep]
       E[Edit Definition]
       F[Save Image and Code]

       A --> B --> C
       C --> D --> F --> B
       C --> E --> B

.. admonition:: 学習者ノート

   ``Code`` セクションでは、生の Mermaid
   コードを書いたり編集したりすることができ、 その横にあるパネル ``Preview``
   で描画結果を即座に確認できる。それから ``Configuration``
   セクションは、図式の外観や動作を変更するためにある。 手許に Mermaid
   コードをチェックする環境がまったくない場合には上記ウェブページが有用だ。
   キーワード補完機能はここにしかないかもしれない。

Editing History
-----------------------------------------------------------------------

Your code will be autosaved every minute into the Timeline tab of History which
shows the most recent 30 items.

You can manually save code by clicking the Save icon in the History section. It
can also be accessed in the Saved tab. This is stored in the browser storage
only.

.. admonition:: 学習者ノート

   実際にグラフを編集してから Timeline
   を確認すると、今実行したばかりのコマンド名がよくわからない。

Saving a Diagram
-----------------------------------------------------------------------

You may choose any of the methods below, to save it

**We recommend that you save your diagram code on top of any method you choose,
in order to make edits and modifications further down the line.**

.. admonition:: 学習者ノート

   開発陣の言うことは正しい。出力結果よりも入力であるテキストのほうが重要だ。

Editing your diagrams
-----------------------------------------------------------------------

Editing is as easy as pasting your **Diagram code**, into the ``code`` section
of the ``Live Editor``.

Loading from Gists
-----------------------------------------------------------------------

The Gist you create should have a code.mmd file and optionally a config.json.

.. admonition:: 学習者ノート

   まずは Gist に新しくページ（実体はリポジトリー）を追加して、
   `例 <https://gist.github.com/sidharthv96/6268a23e673a533dcb198f241fd7012a>`__
   のような構成にする。 Mermaid 書式のテキストファイルと、必要ならば config.json
   を添える。 あとは Live Editor の UI を見れば指定方法は理解できる。

2. Using Mermaid Plugins
======================================================================

You can generate mermaid diagrams from within popular applications using
plug-ins. It can be done in the same way, you would use the Live Editor.

.. admonition:: 学習者ノート

   個人的に注目しているのは次のものだ：

   * VS Code `Markdown Preview Mermaid
     Support <https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid>`__:
     当ノートもこれを利用して編集している。
   * Sphinx
     `sphinxcontrib-mermaid <https://github.com/mgaitan/sphinxcontrib-mermaid>`__:
     読者ノート用に確認する。

3. Calling the Javascript API
=======================================================================

This method can be used with any common web server like Apache, IIS, nginx, node
express.

You will also need a text editing tool like Notepad++ to generate a .html file.
It is then deployed by a web browser (such as Firefox, Chrome, Safari, but not
Internet Explorer).

The API works by pulling rendering instructions from the source ``mermaid.js``
in order to render diagrams on the page.

.. admonition:: 学習者ノート

   最初のパラグラフは無視する。

Requirements for the Mermaid API
-----------------------------------------------------------------------

When writing the .html file, we give three instructions inside the html code to
the web browser:

a. A reference for fetching the online mermaid renderer, through the
   ``mermaid.js`` or ``mermaid.min.js``.

b. The mermaid code for the diagram we want to create.

c. The ``mermaid.initialize()`` call, which dictates the appearance of diagrams
   and also starts the rendering process.

.. admonition:: 学習者ノート

   この三点セットが Mermaid 利用の基本だ。
   実際の利用ではこれを変形して実現することになるはずだ。

**a. A reference to the external CDN in a ``<script src>`` tag, or a reference to mermaid.js as a separate file.:**

.. code:: html

   <body>
       <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
   </body>

.. admonition:: 学習者ノート

   素の HTML と Jekyll 仕様のブログとでは、この ``script``
   タグの位置がかなり異なる。

**b. The embedded mermaid diagram definition inside a ``<div class="mermaid">``:**

.. code:: html

   <body>
       Here is a mermaid diagram:
       <div class="mermaid">
           graph TD
           A[Client] --> B[Load Balancer]
           B --> C[Server01]
           B --> D[Server02]
       </div>
   </body>

**Notes**: Every Mermaid chart/graph/diagram definition, should have separate
``<div>`` tags.

.. admonition:: 学習者ノート

   Jekyll で Markdown の三重バッククオートによる ``mermaid``
   ブロックを定義すると、 Jekyll がこのブロックコードをクラスが ``mermaid``
   である ``div`` タグに変換するものと期待する。 Sphinx
   のプラグインでも同様の挙動をするはずなので、この後すぐに確認したい。

**c. The ``mermaid.initialize()`` call.**

``mermaid.initialize()`` call takes all the definitions contained in all the
``<div class="mermaid">`` tags that it finds in the html body and renders them
into diagrams. Example:

.. code:: html

   <body>
       <script>
           mermaid.initialize({ startOnLoad: true });
       </script>
   </body>

.. note::

   Rendering in Mermaid is initialized by ``mermaid.initialize()`` call.
   You can place ``mermaid.initialize()`` inside ``mermaid.min.js`` for brevity.
   However, doing the opposite lets you control when it starts looking for
   ``<div>`` tags inside the web page with ``mermaid.initialize()``. This is
   useful when you think that not all ``<div>`` tags may have loaded on the
   execution of ``mermaid.min.js`` file.

``startOnLoad`` is one of the parameters that can be defined by
``mermaid.initialize()``

=========== ================================= ======= ===========
Parameter   Description                       Type    Values
=========== ================================= ======= ===========
startOnLoad Toggle for Rendering upon loading Boolean true, false
=========== ================================= ======= ===========

.. admonition:: 学習者ノート

   おそらく ``windows.onload`` のイベントハンドラーに Mermaid
   ブロックを 図式化する処理を追加するような指示を表している。

Working Examples
-----------------------------------------------------------------------

Here is a full working example of the mermaidAPI being called through the CDN:

.. code:: html

   <html>
       <body>
           <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
           <script>
               mermaid.initialize({ startOnLoad: true });
           </script>

           Here is one mermaid diagram:
           <div class="mermaid">
               graph TD
               A[Client] --> B[Load Balancer]
               B --> C[Server1]
               B --> D[Server2]
           </div>

           And here is another:
           <div class="mermaid">
               graph TD
               A[Client] -->|tcp_123| B
               B(Load Balancer)
               B -->|tcp_456| C[Server1]
               B -->|tcp_456| D[Server2]
           </div>
       </body>
   </html>

**Another Option:** In this example mermaid.js is referenced in ``src`` as a
separate JavaScript file, in an example Path.

.. code:: html

   <html lang="en">
       <head>
           <meta charset="utf-8" />
       </head>
       <body>
           <div class="mermaid">
               graph LR
               A --- B
               B-->C[fa:fa-ban forbidden]
               B-->D(fa:fa-spinner);
           </div>
           <div class="mermaid">
               graph TD
               A[Client] --> B[Load Balancer]
               B --> C[Server1]
               B --> D[Server2]
           </div>
           <script src="The\Path\In\Your\Package\mermaid.js"></script>
           <script>
               mermaid.initialize({ startOnLoad: true });
           </script>
       </body>
   </html>

4. Adding Mermaid as a dependency
=======================================================================

1. install node v16, which would have npm
2. download yarn using npm by entering the command below: ``npm install -g yarn``
3. After yarn installs, enter the following command: ``yarn add mermaid``
4. To add Mermaid as a Dev Dependency ``yarn add -dev mermaid``

.. admonition:: 学習者ノート

   この記述は私が NPM に疎いために意図するところが汲み取れない。

**Comments from Knut Sveidqvist, creator of mermaid:**

* In early versions of mermaid, the ``<script src>`` tag was invoked in the
  ``<head>`` part of the web page. Nowadays we can place it in the ``<body>``
  as seen above. Older parts of the documentation frequently reflects the
  previous way which still works.

.. admonition:: 学習者ノート

   開発者は Mermaid を準備するための ``script`` タグを HTML の
   ``head`` 部分に置いて欲しくないと考えているように取れる。
