======================================================================
Sequence Diagrams
======================================================================

.. contents::
   :depth: 2

..

  Mermaid can render sequence diagrams.

  .. mermaid:: ./sd-first.mmd
     :align: center
  .. literalinclude:: ./sd-first.mmd

UML シーケンス図は使い所が多いのでありがたい。

Syntax
======================================================================

Participants
----------------------------------------------------------------------

  The participants can be defined implicitly as in the first example on this
  page. The participants or actors are rendered in order of appearance in the
  diagram source text. Sometimes you might want to show the participants in a
  different order than how they appear in the first message. It is possible to
  specify the actor's order of appearance by doing the following:

  .. code:: text

     sequenceDiagram
         participant Alice
         participant Bob
         Alice->>Bob: Hi Bob
         Bob->>Alice: Hi Alice

参加者を明示的に宣言しておくことの利点は、図式中のライフラインの配列を調整できる
ということだ。コード中の ``participant`` の行を入れ替えて描画結果を見比べると検
証できる。

Actors
----------------------------------------------------------------------

  If you specifically want to use the actor symbol instead of a rectangle with
  text you can do so by using actor statements as per below.

  .. code:: text

     sequenceDiagram
         actor Alice
         actor Bob
         Alice->>Bob: Hi Bob
         Bob->>Alice: Hi Alice

棒人間を描けるのなら Use Case Diagram も Mermaid には対応して欲しいものだ。

Aliases
----------------------------------------------------------------------

  The actor can have a convenient identifier and a descriptive label.

  .. code:: text

     sequenceDiagram
         participant A as Alice
         participant J as John
         A->>J: Hello John, how are you?
         J->>A: Great!

この機能は ``as`` の後ろにある単語のほうがラベルとして描画される。

Grouping / Box
----------------------------------------------------------------------

この機能はシーケンス図を水平に区切ることで部分シーケンス図を形成する。

  The actor(s) can be grouped in vertical boxes. You can define a color (if not,
  it will be transparent) and/or a descriptive label using the following
  notation:

  .. code:: text

     box Aqua Group Description
     ... actors ...
     end
     box Group without description
     ... actors ...
     end
     box rgb(33,66,99)
     ... actors ...
     end

次の例は正常に描画される実践的なものだ：

  .. mermaid:: ./sd-boxes.mmd
     :align: center
  .. literalinclude:: ./sd-boxes.mmd

Messages
======================================================================

  Messages can be of two displayed either solid or with a dotted line.

  .. code:: text

     [Actor][Arrow][Actor]:Message text

  There are six types of arrows currently supported:

  ======== ================================================
  Type     Description
  ======== ================================================
  ``->``   Solid line without arrow
  ``-->``  Dotted line without arrow
  ``->>``  Solid line with arrowhead
  ``-->>`` Dotted line with arrowhead
  ``-x``   Solid line with a cross at the end
  ``--x``  Dotted line with a cross at the end.
  ``-)``   Solid line with an open arrow at the end (async)
  ``--)``  Dotted line with a open arrow at the end (async)
  ======== ================================================

シーケンス図では実線と点線は要求と応答をそれぞれ表す。閉じた矢印と開いた矢印は同
期的か非同期的かをそれぞれ表す。バツジルシの矢印は不明。

Activations
======================================================================

  It is possible to activate and deactivate an actor. ``(de)activation`` can be
  dedicated declarations:

  .. code:: text

     sequenceDiagram
         Alice->>John: Hello John, how are you?
         activate John
         John-->>Alice: Great!
         deactivate John

UML の仕様としては、activation 要素は、オブジェクトがメッセージに応答しているこ
とを示すものだ。メッセージを受信したときに開始し、オブジェクトがメッセージの処理
を終了したときに終了する。

  There is also a shortcut notation by appending ``+``/``-`` suffix to the
  message arrow:

  .. code:: text

     sequenceDiagram
         Alice->>+John: Hello John, how are you?
         John-->>-Alice: Great!

同じ見てくれの図式が得られる。

  Activations can be stacked for same actor:

  .. mermaid:: ./sd-activation.mmd
     :align: center
  .. literalinclude:: ./sd-activation.mmd

活性区間が重なり合うように描画される。

Notes
======================================================================

  It is possible to add notes to a sequence diagram. This is done by the notation
  ``Note [ right of | left of | over ] [Actor]: Text`` in note content

  See the example below:

  .. code:: text

     sequenceDiagram
         participant John
         Note right of John: Text in note

実際に注釈要素が描画される位置は、John 全体に対して決まるようだ。垂直方向座標は
シーケンスのその時点に対応して決まる。

  It is also possible to create notes spanning two participants:

  .. code:: text

     sequenceDiagram
         Alice->John: Hello John, how are you?
         Note over Alice,John: A typical interaction

キーワード ``over`` の引数に参加者をカンマ区切りで与えればいい。注釈要素が両者全
体にまたがるように描画される。

  It is also possible to add a line break (applies to text input in general)

HTML タグ ``<br/>`` をテキスト中に直接記入すればいい。

Loops
======================================================================

  It is possible to express loops in a sequence diagram. This is done by the
  notation

  .. code:: text

     loop Loop text
     ... statements ...
     end

  See the example below:

  .. code:: text

     sequenceDiagram
         Alice->John: Hello John, how are you?
         loop Every minute
             John-->Alice: Great!
         end

キーワード ``loop`` の引数は反復条件を表すテキストということだ。

Alt
======================================================================

  It is possible to express alternative paths in a sequence diagram. This is
  done by the notation

  .. code:: text

     alt Describing text
     ... statements ...
     else
     ... statements ...
     end

当然だが、``alt`` 節だけでなく ``else`` 節の右側にも describing text を指定する
ことが許される。

  or if there is sequence that is optional (if without else).

  .. code:: text

     opt Describing text
     ... statements ...
     end

これらの両方のブロックを用いた例：

  .. mermaid:: ./sd-alt-opt.mmd
     :align: center
  .. literalinclude:: ./sd-alt-opt.mmd

シーケンス図の ``alt`` はプログラミング言語でいう ``if`` 文のような構文だが、
``elif`` に相当するものがない。

Parallel
======================================================================

これもよく使いたくなるので覚えておく。

  It is possible to show actions that are happening in parallel.

  This is done by the notation

  .. code:: text

     par [Action 1]
     ... statements ...
     and [Action 2]
     ... statements ...
     and [Action N]
     ... statements ...
     end

自然な文法だ。キーワード ``par`` の引数は実行条件を表すテキストなのだが、ない場
合は空でいい。

  It is also possible to nest parallel blocks.

  .. mermaid:: ./sd-par.mmd
     :align: center
  .. literalinclude:: ./sd-par.mmd

異種の構造化ブロックを入れ子にしたい場合がよくあるし、Mermaid はそれを対応してい
るはずだ。

Critical Region
======================================================================

最近になってシーケンス図で対応されるブロックの種類が拡充されたようだ。

  It is possible to show actions that must happen automatically with conditional
  handling of circumstances.

  This is done by the notation

  .. code:: text

     critical [Action that must be performed]
     ... statements ...
     option [Circumstance A]
     ... statements ...
     option [Circumstance B]
     ... statements ...
     end

  See the example below:

  .. mermaid:: ./sd-critical.mmd
     :align: center
  .. literalinclude:: ./sd-critical.mmd

主要機能説明時に言及されていなかったが、矢印を自身に向けることも許されている。

Break
======================================================================

  It is possible to indicate a stop of the sequence within the flow (usually used
  to model exceptions).

  This is done by the notation

  .. code:: text

     break [something happened]
     ... statements ...
     end

なお、ブロック ``break`` を用いるのは、例外処理をモデル化するためであることが多
い。

  See the example below:

  .. code:: text

     sequenceDiagram
         Consumer-->API: Book something
         API-->BookingService: Start booking process
         break when the booking process fails
             API-->Consumer: show failure
         end
         API-->BillingService: Start billing process

このコードはコンパクトだが、描画すると比較的複雑で驚く。

Background Highlighting
======================================================================

  It is possible to highlight flows by providing colored background rects. This
  is done by the notation

  The colors are defined using rgb and rgba syntax.

  .. code:: text

     rect rgb(0, 255, 0)
     ... content ...
     end
     rect rgba(0, 0, 255, .1)
     ... content ...
     end

ブロック ``rect`` はシーケンス図を垂直に区切る。この要素の着想は HTML における
``div`` タグの利用と一緒だろう。

  See the examples below:

  .. code:: text

     sequenceDiagram
         participant Alice
         participant John

         rect rgb(191, 223, 255)
         note right of Alice: Alice calls John.
         Alice->>+John: Hello John, how are you?
         rect rgb(200, 150, 255)
         Alice->>+John: John, can you hear me?
         John-->>-Alice: Hi Alice, I can hear you!
         end
         John-->>-Alice: I feel great!
         end
         Alice ->>+ John: Did you want to go to the game tonight?
         John -->>- Alice: Yeah! See you there.

背景色が強い ``rect`` を過剰に入れ子を構成すると見苦しくなることがわかる。

Comments
======================================================================

  Comments can be entered within a sequence diagram, which will be ignored by
  the parser. Comments need to be on their own line, and must be prefaced with
  ``%%`` (double percent signs). Any text after the start of the comment to the
  next newline will be treated as a comment, including any diagram syntax.

  .. code:: text

     sequenceDiagram
         Alice->>John: Hello John, how are you?
         %% this is a comment
         John-->>Alice: Great!

これは ``flowchart`` にもある機能だ。このコメント要素は図式クラス全てに対して有
効な構文であって欲しい。

Entity codes to escape characters
======================================================================

  .. code:: text

     sequenceDiagram
         A->>B: I #9829; you!
         B->>A: I #9829; you #infin; times more!

これも ``flowchart`` 同様の運用となる。

``sequenceNumbers``
======================================================================

手順に番号を振りたい場合には有用な機能だ。

  It is possible to get a sequence number attached to each arrow in a sequence
  diagram. This can be configured when adding mermaid to the website as shown
  below:

  .. code:: html

     <script>
       mermaid.initialize({
         sequence: { showSequenceNumbers: true },
       });
     </script>

図式単位で番号機能の有無を分ける場合には ``sequenceDiagram`` に ``autonumber`` と
書くことでそうする：

  .. code:: text

     sequenceDiagram
         autonumber
         Alice->>John: Hello John, how are you?
         loop Healthcheck
             John->>John: Fight against hypochondria
         end
         Note right of John: Rational thoughts!
         John-->>Alice: Great!
         John->>Bob: How about you?
         Bob-->>John: Jolly good!

この図式にはなぜか見覚えがある。

Actor Menus
======================================================================

  Actors can have popup-menus containing individualized links to external pages.

いきなりジャンプするのではなく、リンクを含むメニューをポップアップがあり得るとい
う。

  This can be configured by adding one or more link lines with the format:

  .. code:: text

     link <actor>: <link-label> @ <link-url>

単一の参加者に複数のリンクを割り当てるには、このパターンを複数書くことになる：

  .. code:: text

     sequenceDiagram
         participant Alice
         participant John
         link Alice: Dashboard @ https://dashboard.contoso.com/alice
         link Alice: Wiki @ https://wiki.contoso.com/alice
         link John: Dashboard @ https://dashboard.contoso.com/john
         link John: Wiki @ https://wiki.contoso.com/john
         Alice->>John: Hello John, how are you?
         John-->>Alice: Great!
         Alice-)John: See you later!

マウスを参加者要素の上に動かすとメニューが出現する。そこには Dashboard と Wiki
の項目がある。と以前記したが、これを加筆している時点で機能していない。

Advanced Menu Syntax
----------------------------------------------------------------------

  There is an advanced syntax that relies on JSON formatting. If you are
  comfortable with JSON format, then this exists as well.

  This can be configured by adding the links lines with the format:

  .. code:: text

     links <actor>: <json-formatted link-name link-url pairs>

  An example is below:

  .. code:: text

     sequenceDiagram
         participant Alice
         participant John
         links Alice: {"Dashboard": "https://dashboard.contoso.com/alice", "Wiki": "https://wiki.contoso.com/alice"}
         links John: {"Dashboard": "https://dashboard.contoso.com/john", "Wiki": "https://wiki.contoso.com/john"}
         Alice->>John: Hello John, how are you?
         John-->>Alice: Great!
         Alice-)John: See you later!

この例は前の例と同じメニューを実装している。こちらもこのメモを加筆している時点で
機能していない。

Styling
======================================================================

  Styling of a sequence diagram is done by defining a number of css classes.
  During rendering these classes are extracted from the file located at
  :file:`src/themes/sequence.scss`.

この SCSS ファイルパスの言及が唐突な感じがする。

Classes used
----------------------------------------------------------------------

Flowchart のような、Mermaid ブロック中で即席でスタイルを定義する方式はないだろう
か。

Sample stylesheet
----------------------------------------------------------------------

この例を見ると CSS とは規則が違う。

Configuration
======================================================================

  Is it possible to adjust the margins for rendering the sequence diagram.

  .. code:: javascript

     mermaid.sequenceConfig = {
         diagramMarginX: 50,
         diagramMarginY: 10,
         boxTextMargin: 5,
         noteMargin: 10,
         messageMargin: 35,
         mirrorActors: true
     };

マージン調整くらいしかカスタマイズがないように読めてしまうが、次の節で示されるよ
うにフォントの指定も可能だ。

Possible configuration parameters
----------------------------------------------------------------------

長いので本書を参照。
