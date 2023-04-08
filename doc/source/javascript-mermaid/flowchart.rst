=======================================================================
Flowcharts - Basic Syntax
=======================================================================

  All Flowcharts are composed of nodes, the geometric shapes and edges, the arrows
  or lines. The mermaid code defines the way that these nodes and edges are made
  and interact.

  It can also accomodate different arrow types, multi directional arrows, and
  linking to and from subgraphs.

Mermaid 開発陣はフローチャートとは言っているが、汎用の有向グラフとして取り扱うの
がわかりやすい。

.. contents::
   :depth: 2

Node
=======================================================================

  Do not type the word "end" as a Flowchart node. Capitalize all or any one the
  letters to keep the flowchart from breaking, i.e, "End" or "END".

という注意点があるそうなので、何かエラーが出たらこれを意識することにする。

A node (default)
-----------------------------------------------------------------------

  .. code:: text

     ---
     title: Node
     ---
     flowchart LR
         id

いつの間にか Flowchart に対して見出しを与えることが可能になっている。図式の天井
中央にテキストが描画されるようだ。

A node with text
-----------------------------------------------------------------------

次の文法により、ID 文字列とは異なるテキストをノードに書ける：

  .. code:: text

     ---
     title: Node with text
     ---
     flowchart LR
         id1[This is the text in the box]

Graph
=======================================================================

  This declares the flowchart is oriented from top to bottom (``TD`` or ``TB``).

  .. code:: text

     flowchart TD
         Start --> Stop

``flowchart`` に続けて二文字でグラフの向きを指定する。

Flowchart Orientation
=======================================================================

  Possible FlowChart orientations are:

  * ``TB`` - top to bottom
  * ``TD`` - top-down/ same as top to bottom
  * ``BT`` - bottom to top
  * ``RL`` - right to left
  * ``LR`` - left to right

``TB`` と ``TD`` が同じなので実質的には四つあると言える。

Node shapes
=======================================================================

ノード形状はテキスト周りの括弧の組で決まる。

実際に描画させるとやたらスペースをとるノード形状がいくつかある。そういうものはテ
キストを設定しないで利用するのが本来想定されている用途なのだろう。

.. code:: text

   ---
   title: Node shapes
   ---
   flowchart LR
       nodeA(A node with round edges)
       nodeB([A stadium-shaped node])
       nodeC[[A node in a subroutine shape]]
       nodeD[(A node in a cylindrical shape)]
       nodeE((A node in the form of a circle))
       nodeF>A node in an asymmetric shape]
       nodeG{A node rhombus}
       nodeH{{A hexagon node}}
       nodeI[/Parallelogram/]
       nodeJ[\Parallelogram alt\]
       nodeK[/Trapezoid\]
       nodeL[\Trapezoid alt/]

Links between nodes
======================================================================

A link with arrow head
-----------------------------------------------------------------------

  .. code:: text

     flowchart LR
         A-->B

これは有向グラフに用いるといいだろう。

An open link
-----------------------------------------------------------------------

.. code:: text

   flowchart LR
       A --- B

こちらは無向グラフに用いたい。

Text on links
-----------------------------------------------------------------------

次の二つの記法があるがどちらも同様の描画となる。ラベルはエッジの中央になるべく現
れる：

  .. code:: text

     flowchart LR
         A-- This is the text! ---B

または：

  .. code:: text

     flowchart LR
         A---|This is the text|B

A link with arrow head and text
-----------------------------------------------------------------------

次の二つの記法があるがどちらも同様の描画となる。ラベルはエッジの中央になるべく現
れる：

  .. code:: text

     flowchart LR
         A-->|text|B

もしくは：

  .. code:: text

     flowchart LR
         A-- text -->B

Dotted link
-----------------------------------------------------------------------

点線スタイルはしばしば採用したくなるので記法を覚えておく。ドットしか使わないわけ
ではない。

  .. code:: text

     flowchart LR;
        A-.->B;

Dotted link with text
-----------------------------------------------------------------------

記憶しにくい記法だ：

  .. code:: text

     flowchart LR
        A-. text .-> B

Thick link
-----------------------------------------------------------------------

太い線を描く場合には文字 ``=`` をつなげる。これは自然な記法だ。

  .. code:: text

     flowchart LR
        A ==> B

Thick link with text
-----------------------------------------------------------------------

こちらも自然：

  .. code:: text

     flowchart LR
        A == text ==> B

An invisible link
----------------------------------------------------------------------

  This can be a useful tool in some instances where you want to alter the default
  positioning of a node.

昔のバージョンにはなかったリンクのスタイルだ。

  .. code:: text

     flowchart LR
         A ~~~ B

Chaining of links
-----------------------------------------------------------------------

  It is possible declare many links in the same line as per below:

  .. code:: text

     flowchart LR
        A -- text --> B -- text2 --> C

人間にはエッジラベルとノードの見分けがすぐにはつかない。視認性がかなり悪い。

  It is also possible to declare multiple nodes links in the same line as per
  below:

  .. code:: text

     flowchart LR
        a --> b & c--> d

  You can then describe dependencies in a very expressive way. Like the one-liner
  below:

  .. code:: text

     flowchart TB
         A & B--> C & D

Bash における brace expansion, e.g. ``{A,B}{C,D}`` 等々に類似する記法か。

New arrow types
-----------------------------------------------------------------------

  There are new types of arrows supported as per below:

  .. code:: text

     flowchart LR
         A --o B
         B --x C

ベタ塗り●とバツジルシ✕がそれぞれ終端にマークされる。

Multi directional arrows
-----------------------------------------------------------------------

  There is the possibility to use multidirectional arrows.

  .. code:: text

     flowchart LR
         A o--o B
         B <--> C
         C x--x D

想像どおりの印が両端点に描画される。

Minimum length of a link
-----------------------------------------------------------------------

  By default, links can span any number of ranks, but you can ask for any link to
  be longer than the others by adding extra dashes in the link definition.

  In the following example, two extra dashes are added in the link from node *B*
  to node *E*, so that it spans two more ranks than regular links:

  .. code:: text

     flowchart TD
         A[Start] --> B{Is it?}
         B -->|Yes| C[OK]
         C --> D[Rethink]
         D --> B
         B ---->|No| E[End]

これによりエッジ BE が長めに描画される。

  When the link label is written in the middle of the link, the extra dashes must
  be added on the right side of the link. The following example is equivalent to
  the previous one:

  .. code:: text

     flowchart TD
         A[Start] --> B{Is it?}
         B -- Yes --> C[OK]
         C --> D[Rethink]
         D --> B
         B -- No ----> E[End]

ラベル ``No`` とノード ``E`` の間の部分を長くしろと言っている。

  For dotted or thick links, the characters to add are equals signs or dots, as
  summed up in the following table:

  ================= ======== ========= ==========
  Length            1        2         3
  ================= ======== ========= ==========
  Normal            ``---``  ``----``  ``-----``
  Normal with arrow ``-->``  ``--->``  ``---->``
  Thick             ``===``  ``====``  ``=====``
  Thick with arrow  ``==>``  ``===>``  ``====>``
  Dotted            ``-.-``  ``-..-``  ``-...-``
  Dotted with arrow ``-.->`` ``-..->`` ``-...->``
  ================= ======== ========= ==========

点線のときだけ注意すればいいだろう。中程を反復する。

Special characters that break syntax
=======================================================================

  It is possible to put text within quotes in order to render more troublesome
  characters.

怪しいノード形状を採用する場合には引用符を予防的に入れておくことにしよう。

Entity codes to escape characters
-----------------------------------------------------------------------

  It is possible to escape characters using the syntax exemplified here.

  .. code:: text

     flowchart LR
         A["A double quote:#quot;"] -->B["A dec char:#9829;"]

  Numbers given are base 10, so ``#`` can be encoded as ``#35;``. It is also
  supported to use HTML character names.

これは HTML 上で何かを表現するコードを規定するものにしては異例の仕様だと思う。
``&quot;`` を不採用にする理由が何かあったはずだ。

Subgraphs
=======================================================================

部分グラフの構文は次のとおりだ：

  .. code:: text

     subgraph title
         graph definition
     end

上記 ``graph definition`` 部分に Flowchat の中身の文法と同じコードが来る。

  You can also set an explicit id for the subgraph.

  .. code:: text

     flowchart TB
         c1-->a2
         subgraph ide1 [one]
         a1-->a2
         end

こうすると部分グラフの描画領域に ``one`` というラベルテキストが描画される。

flowcharts
=======================================================================

  With the graphtype flowchart it is also possible to set edges to and from
  subgraphs as in the flowchart below.

  .. code:: text

     flowchart TB
         c1-->a2
         subgraph one
         a1-->a2
         end
         subgraph two
         b1-->b2
         end
         subgraph three
         c1-->c2
         end
         one --> two
         three --> two
         two --> c2

エッジの端点がノードではなく部分グラフ領域に接することが可能だということだ。最後
の三つのエッジがその例になっている。

Direction in subgraphs
=======================================================================

  With the graphtype flowcharts you can use the direction statement to set the
  direction which the subgraph will render like in this example.

``LR`` などの方向指定を部分グラフ間でも可能ではあるのだが、グラフ描画エンジンは
その指定すべてを達成することができない場合には遠慮せずに無視するようだ。

Markdown Strings
=======================================================================

  The "Markdown Strings" feature enhances flowcharts and mind maps by offering a
  more versatile string type, which supports text formatting options such as bold
  and italics, and automatically wraps text within labels.

これは最近のバージョンで追加された機能だ。

.. code:: text

   %%{init: {"flowchart": {"htmlLabels": false}} }%%
   flowchart LR
   subgraph "One"
     a("`The **cat**
     in the hat`") -- "edge label" --> b{{"`The **dog** in the hog`"}}
   end
   subgraph "`**Two**`"
     c("`The **cat**
     in the hat`") -- "`Bold **edge label**`" --> d("The dog in the hog")
   end

こんなふうに初期化時設定さえあれば Markdown のインライン装飾文字が使える。

  This feature is applicable to node labels, edge labels, and subgraph labels.

Flowchart 本体のほとんどのテキストで適用可能ということだ。

Interaction
=======================================================================

  It is possible to bind a click event to a node, the click can lead to either a
  javascript callback or to a link which will be opened in a new browser tab.

  .. note::

     This functionality is disabled when using ``securityLevel='strict'``
     and enabled when using ``securityLevel='loose'``.

Markdown 設定により Flowchart ノードに対してはクリックイベントを実装することがで
きる。

  .. code:: text

     click nodeId callback
     click nodeId call callback()

このようなコード片を Flowchart に追加して、クリックイベントを ``callback`` に処
理させる。

  * ``nodeId`` is the id of the node
  * ``callback`` is the name of a javascript function defined on the page
    displaying the graph, the function will be called with the ``nodeId`` as
    parameter.

イベントハンドラーは Markdown コードの外部に別途実装する：

  .. code:: html

     <script>
       const callback = function () {
         alert('A callback was triggered');
       };
     </script>

  The tooltip text is surrounded in double quotes. The styles of the tooltip are
  set by the class ``.mermaidTooltip``.

  .. code:: text

     flowchart LR
         A-->B
         B-->C
         C-->D
         click A callback "Tooltip for a callback"
         click B "http://www.github.com" "This is a tooltip for a link"
         click A call callback() "Tooltip for a callback"
         click B href "http://www.github.com" "This is a tooltip for a link"

ツールチップ表示も URL ジャンプも有用だ。前者はクリックイベントというよりマウス
オーバーで表示される。公式 Live Editor では発動しない。

  Links are opened in the same browser tab/window by default. It is possible to
  change this by adding a link target to the click definition (``_self``,
  ``_blank``, ``_parent`` and ``_top`` are supported):

  .. code:: text

     flowchart LR
         A-->B
         B-->C
         C-->D
         D-->E
         click A "http://www.github.com" _blank
         click B "http://www.github.com" "Open this in a new tab" _blank
         click C href "http://www.github.com" _blank
         click D href "http://www.github.com" "Open this in a new tab" _blank

初心者向けコード例のうち、設定部分を引用する：

  .. code:: html

     <script>
       const callback = function () {
         alert('A callback was triggered');
       };
       const config = {
         startOnLoad: true,
         flowchart: { useMaxWidth: true, htmlLabels: true, curve: 'cardinal' },
         securityLevel: 'loose',
       };
       mermaid.initialize(config);
     </script>

Comments
-----------------------------------------------------------------------

  Comments need to be on their own line, and must be prefaced with ``%%``
  (double percent signs).

コメントは一行丸々を必要とすることに注意。コード行末にコメントすることはできな
い。

  .. code:: text

     flowchart LR
     %% this is a comment A -- text --> B{node}
        A -- text --> B -- text2 --> C

Styling and classes
=======================================================================

Styling links
-----------------------------------------------------------------------

  It is possible to style links. For instance you might want to style a link
  that is going backwards in the flow. As links have no ids in the same way as
  nodes, some other way of deciding what style the links should be attached to
  is required. Instead of ids, the order number of when the link was defined in
  the graph is used. In the example below the style defined in the ``linkStyle``
  statement will belong to the fourth link in the graph:

  .. code:: text

     linkStyle 3 stroke:#ff3,stroke-width:4px,color:red;

エッジには ID の概念がないので、指定するにはその定義順を用いる。順序数をゼロから
数えるものとする。

Styling line curves
----------------------------------------------------------------------

  It is possible to style the type of curve used for lines between items, if the
  default method does not meet your needs.

エッジの曲線的形状を指定する術があり、次のような設定により有効になる：

  .. code:: text

     %%{ init: { 'flowchart': { 'curve': 'stepBefore' } } }%%

  For a full list of available curves, including an explanation of custom curves,
  refer to the `Shapes <https://github.com/d3/d3-shape/blob/main/README.md#curves>`__
  documentation in the d3-shape project.

こちらの JavaScript ライブラリーはモデリングソフト開発経験者としては興味深い。

Styling a node
-----------------------------------------------------------------------

  It is possible to apply specific styles such as a thicker border or a different
  background color to a node.

  .. code:: text

     flowchart LR
         id1(Start)-->id2(Stop)
         style id1 fill:#f9f,stroke:#333,stroke-width:4px
         style id2 fill:#bbf,stroke:#f66,stroke-width:2px,color:#fff,stroke-dasharray: 5 5

この仕様は紛れがない。

次に、ノードそれぞれに対してスタイルを与えるというよりは、スタイルを先に定義して、
ノードがどのスタイルを持つのかを決めるという方法を述べる。

  More convenient than defining the style every time is to define a class of
  styles and attach this class to the nodes that should have a different look.

  A class definition looks like the example below:

  .. code:: text

     classDef className fill:#f9f,stroke:#333,stroke-width:4px;

  Attachment of a class to a node is done as per below:

  .. code:: text

     class nodeId1 className;

スタイル定義を先に行い、ノードに対してスタイルを指定するという方法だ。これによ
り、異なるノードが同じスタイルをコードの複製なしに共有することができる。

  It is also possible to attach a class to a list of nodes in one statement:

  .. code:: text

     class nodeId1,nodeId2 className;

この方式ではノードスタイルをグラフ定義コードでインラインで指定する記法もある：

  .. code:: text

     flowchart LR
         A:::someclass --> B
         classDef someclass fill:#f96;

クラス名がコロンの後に来るので違和感がある。

CSS classes
-----------------------------------------------------------------------

  It is also possible to predefine classes in css styles that can be applied from
  the graph definition as in the example below:

  .. code:: html

     <style>
         .cssClass > rect{
             fill:#FF0000;
             stroke:#FFFF00;
             stroke-width:4px;
         }
     </style>

  .. code:: text

     flowchart LR
         A-->B[AAA<span>BBB</span>]
         B-->D
         class A cssClass

手順としては、先に CSS 側にスタイル規則を決める。次に Flowchart 側で規則名称をス
タイル定義の代わりに書く。

Flowchart 例の ``span`` タグに意味はあるのか？

Default class
-----------------------------------------------------------------------

  If a class is named ``default`` it will be assigned to all classes without
  specific class definitions.

  .. code:: text

     classDef default fill:#f9f,stroke:#333,stroke-width:4px;

図式が一つしかない場合にこの使い方が最も多く用いられると思われる。複数ある場合に
は外部 CSS ファイルの手法を採用したい。

Basic support for fontawesome
=======================================================================

  It is possible to add icons from fontawesome.

  The icons are accessed via the syntax ``fa:#icon class name#``.

  .. code:: text

     flowchart TD
         B["fa:fa-twitter for peace"]
         B-->C[fa:fa-ban forbidden]
         B-->D(fa:fa-spinner);
         B-->E(A fa:fa-camera-retro perhaps?)

Oh My Posh で見られるような特殊記号のためのフォントをどう得るのかが不明。
`Font Awesome <https://fontawesome.com/>`__ をどうにかするのだろうが。

Graph declarations with spaces between vertices and link and without semicolon
======================================================================

  * In graph declarations, the statements also can now end without a semicolon.
    After release 0.2.16, ending a graph statement with semicolon is just
    optional. So the below graph declaration is also valid along with the old
    declarations of the graph.
  * A single space is allowed between vertices and the link. However there should
    not be any space between a vertex and its text and a link and its text. The
    old syntax of graph declaration will also work and hence this new feature is
    optional and is introduced to improve readability.

空白文字を下手に入れるのは有害である可能性があることを覚えておく。

Configuration
======================================================================

Renderer
----------------------------------------------------------------------

  Starting with Mermaid version 9.4, you can use an alternate renderer named elk.
  The elk renderer is better for larger and/or more complex diagrams.

  The elk renderer is an experimenal feature. You can change the renderer to elk
  by adding this directive:

  .. code:: text

     %%{init: {"flowchart": {"defaultRenderer": "elk"}} }%%

  Note that the site needs to use mermaid version 9.4+ for this to work and have
  this featured enabled in the lazy-loading configuration.

Mermaid の遅延ロードの手法はどこに記載があったか？

Width
----------------------------------------------------------------------

  Is it possible to adjust the width of the rendered flowchart.

  This is done by defining ``mermaid.flowchartConfig`` or by the CLI to use a
  json file with the configuration. How to use the CLI is described in the
  mermaidCLI page. ``mermaid.flowchartConfig`` can be set to a JSON string with
  config parameters or the corresponding object.

  .. code:: javascript

     mermaid.flowchartConfig = {
         width: 100%
     }

Mermaid の描画は SVG のようなものなので、ブラウザーのウィンドウを拡縮すると描画
も自然に拡縮される。したがって、ブロック要素の図式ならば 100 パーにしておくのは
ありだろう。
