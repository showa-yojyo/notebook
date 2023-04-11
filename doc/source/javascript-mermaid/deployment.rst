======================================================================
Deployment
======================================================================

Mermaid v10 でモジュールのインポートと初期化を一気に行えるようになったようだ。
ノートを少しでも更新しておく。

.. contents::
   :depth: 2

Four ways of using mermaid
======================================================================

  1. Using the Mermaid Live Editor at `mermaid.live <https://mermaid.live>`__.
  2. Using `mermaid plugins <https://mermaid.js.org/ecosystem/integrations.html>`__
     with programs you are familiar with.
  3. Calling the Mermaid Javascript API.
  4. Deploying Mermaid as a dependency.

  .. note::

     It is our recommendation that you review all approaches, and choose the one
     that is best for your project.

この方法群のうち、2. と 3. を習得したい。1. だけでは自作の HTML ページに図式を表
示させることができない。4. の重要度がよくわからない。

1. Using the Live Editor
======================================================================

この節ではライブエディターの特徴が述べられている。

  Available at `mermaid.live <https://mermaid.live>`__

:guilabel:`Code` セクションでは、生の Mermaid コードを書いたり編集したりすること
ができ、その横にあるパネル :guilabel:`Preview` で描画結果を即座に確認できる。そ
れから :guilabel:`Configuration` セクションは、図式の外観や動作を変更するために
ある。手許に Mermaid コードをチェックする環境がまったくない場合には上記ウェブ
ページが有用だ。キーワード補完機能はここにしかないかもしれない。

.. mermaid::

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

Editing History
-----------------------------------------------------------------------

  Your code will be autosaved every minute into the Timeline tab of History which
  shows the most recent 30 items.

  You can manually save code by clicking the Save icon in the History section. It
  can also be accessed in the Saved tab. This is stored in the browser storage
  only.

実際にグラフを編集してから :guilabel:`Timeline` を確認すると、今実行したばかりの
コマンド名がよくわからない。

Saving a Diagram
-----------------------------------------------------------------------

  You may choose any of the methods below, to save it

  We recommend that you save your diagram code on top of any method you choose,
  in order to make edits and modifications further down the line.

開発陣の言うことは正しい。出力結果よりも入力であるテキストのほうが重要だ。

Editing your diagrams
-----------------------------------------------------------------------

  Editing is as easy as pasting your Diagram code, into the :guilabel:`code`
  section of the ``Live Editor``.

Loading from Gists
-----------------------------------------------------------------------

  The Gist you create should have a code.mmd file and optionally a
  :file:`config.json`.

まずは Gist に新しくページ（実体はリポジトリー）を追加して、`例
<https://gist.github.com/sidharthv96/6268a23e673a533dcb198f241fd7012a>`__ のよう
な構成にする。Mermaid 書式のテキストファイルと、必要ならば :file:`config.json`
を添える。あとは Live Editor の UI を見れば指定方法は理解できる。

2. Using Mermaid Plugins
======================================================================

  You can generate mermaid diagrams from within popular applications using
  plug-ins. It can be done in the same way, you would use the Live Editor.

個人的に注目しているのは次のものだ：

VS Code `Markdown Preview Mermaid Support <https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid>`__
  当ノートもこれを利用して編集している。
Sphinx `sphinxcontrib-mermaid <https://github.com/mgaitan/sphinxcontrib-mermaid>`__
  読者ノート用に確認する。

なお、Jekyll ブログの Markdown ファイルから Mermaid を利用するにはプラグインでは
なく、HTML テンプレートを上書きして次の節の手法に帰着させることにする。

3. Calling the Javascript API
=======================================================================

  You will also need a text editing tool like Notepad++ to generate a .html file.
  It is then deployed by a web browser (such as Firefox, Chrome, Safari, but not
  Internet Explorer).

  The API works by pulling rendering instructions from the source
  :file:`mermaid.js` in order to render diagrams on the page.

テキストエディターで HTML ファイルを編集する能力と JavaScript の取り扱いを理解し
ていれば十分だろう。

Requirements for the Mermaid API
-----------------------------------------------------------------------

自分の HTML ファイルに Mermaid を組み込むために必要な事項が何であるかを見ていく。

  When writing the .html file, we give two instructions inside the html code to
  the web browser:

  a. The mermaid code for the diagram we want to create.
  b. The importing of mermaid library through the :file:`mermaid.esm.mjs` or
     :file:`mermaid.esm.min.mjs` and the ``mermaid.initialize()`` call, which
     dictates the appearance of diagrams and also starts the rendering process.

これは Mermaid v10.1.0 での記載だ。図式の記述と描画の初期化を与えるのだ。

  a. The embedded mermaid diagram definition inside a ``<pre class="mermaid">``:

  .. code:: html

     <body>
       Here is a mermaid diagram:
       <pre class="mermaid">
             graph TD
             A[Client] --> B[Load Balancer]
             B --> C[Server01]
             B --> D[Server02]
       </pre>
     </body>

  Notes: Every Mermaid chart/graph/diagram definition, should have separate
  ``<pre>`` tags.

Mermaid 図式オブジェクト一つに対して ``<pre>`` タグ一つを対応させるように HTML
を記述する。

  b. The import of mermaid and the ``mermaid.initialize()`` call.

  ``mermaid.initialize()`` call takes all the definitions contained in all the
  ``<pre class="mermaid">`` tags that it finds in the html body and renders them
  into diagrams. Example:

Jekyll で Markdown の三重バッククオートによる ``mermaid`` ブロックを定義すると、
Jekyll がこのブロックコードをクラスが ``mermaid`` である ``div`` タグに変換する
ものと期待する。Sphinx のプラグインでも同様の挙動をする。

  c. The ``mermaid.initialize()`` call.

  ``mermaid.initialize()`` call takes all the definitions contained in all the
  ``<div class="mermaid">`` tags that it finds in the html body and renders them
  into diagrams. Example:

  .. code:: html

     <body>
       <script type="module">
         import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
         mermaid.initialize({ startOnLoad: true });
       </script>
     </body>

  .. note::

     Rendering in Mermaid is initialized by ``mermaid.initialize()`` call.
     However, doing the opposite lets you control when it starts looking for
     ``<pre>`` tags inside the web page with ``mermaid.initialize()``. This is
     useful when you think that not all ``<pre>`` tags may have loaded on the
     execution of :file:`mermaid.esm.min.mjs` file.

  ``startOnLoad`` is one of the parameters that can be defined by
  ``mermaid.initialize()``

  =========== ================================= ======= ===========
  Parameter   Description                       Type    Values
  =========== ================================= ======= ===========
  startOnLoad Toggle for Rendering upon loading Boolean true, false
  =========== ================================= ======= ===========

おそらく ``windows.onload`` のイベントハンドラーに Mermaid ブロックを図式化する
処理を追加するような指示を表している。

.. admonition:: 学習者ノート

   Sphinx で sphinxcontrib-mermaid プラグインを有効にする場合の例をここに示す。

   :file:`conf.py` で例えばこのように定義する：

   .. code:: python

      mermaid_version = ""
      mermaid_init_js = ""
      html_js_files = [
          'mermaid.js',
          # etc.
      ]

   :file:`_static` ディレクトリーにスクリプトファイル :file:`mermaid.js` を次の
   ような内容で保存する（よりスマートなコードにしたい）：

   .. code:: javascript

      window.addEventListener('load', () => {
          const MERMAID_CLASS_NAME = '.mermaid';
          if (!document.querySelector(MERMAID_CLASS_NAME)) {
              return;
          }

          const js = document.createElement("script");
          js.src = "https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js";
          js.onload = () => {
              mermaid.initialize({
                  startOnLoad: true,
                  theme: 'base',
                  themeVariables: {
                      primaryColor: 'white',
                      lineColor: 'black',
                      textColor: 'black',
                      primaryBorderColor: 'black',
                      // etc.
                  },
              });
              mermaid.init(undefined, document.querySelectorAll(MERMAID_CLASS_NAME));
          };
          document.head.appendChild(js);
      });

   こうすると、rst ファイルに ``mermaid`` ディレクティブのあった HTML だけが上記
   URL から Mermaid のメインスクリプトをダウンロードして、図式を描くはずだ。

Working Examples
-----------------------------------------------------------------------

  Here is a full working example of the mermaidAPI being called through the CDN:

  .. code:: html

     <html>
       <body>
         Here is one mermaid diagram:
         <pre class="mermaid">
                 graph TD
                 A[Client] --> B[Load Balancer]
                 B --> C[Server1]
                 B --> D[Server2]
         </pre>

         And here is another:
         <pre class="mermaid">
                 graph TD
                 A[Client] -->|tcp_123| B
                 B(Load Balancer)
                 B -->|tcp_456| C[Server1]
                 B -->|tcp_456| D[Server2]
         </pre>

         <script type="module">
           import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
           mermaid.initialize({ startOnLoad: true });
         </script>
       </body>
     </html>

CDN からロードするモジュールを取り込む ``script`` タグを ``body`` 終了直前に
置いていることに注意する。初期化もこのタグ内で行う。

  **Another Option:** In this example mermaid.js is referenced in ``src`` as a
  separate JavaScript file, in an example Path.

  .. code:: html

     <html lang="en">
       <head>
         <meta charset="utf-8" />
       </head>
       <body>
         <pre class="mermaid">
                 graph LR
                 A --- B
                 B-->C[fa:fa-ban forbidden]
                 B-->D(fa:fa-spinner);
         </pre>
         <pre class="mermaid">
                 graph TD
                 A[Client] --> B[Load Balancer]
                 B --> C[Server1]
                 B --> D[Server2]
         </pre>
         <script type="module">
           import mermaid from 'The/Path/In/Your/Package/mermaid.esm.mjs';
           mermaid.initialize({ startOnLoad: true });
         </script>
       </body>
     </html>

インポートするモジュールの場所しか違いがない。

4. Adding Mermaid as a dependency
=======================================================================

  1. install node v16, which would have :program:`npm`
  2. download :program:`yarn` using :program:`npm` by entering the command below:
     :command:`npm install -g yarn`
  3. After :program:`yarn` installs, enter the following command: :command:`yarn
     add mermaid`
  4. To add Mermaid as a Dev Dependency :command:`yarn add -dev mermaid`

NPM だけではなく、もう一つのツール :program:`yarn` をインストールして Mermaid へ
の依存関係を定義すると読める。パッケージ管理ツールが二つあるということか。あ
と、Node のバージョンはより新しくても通じるだろうか。

  Comments from Knut Sveidqvist, creator of mermaid:

  * In early versions of mermaid, the ``<script src>`` tag was invoked in the
    ``<head>`` part of the web page. Nowadays we can place it in the ``<body>`` as
    seen above. Older parts of the documentation frequently reflects the previous
    way which still works.

開発者は Mermaid を準備するための ``script`` タグを HTML の ``head`` 部分に置い
て欲しくないと考えているように取れる。
