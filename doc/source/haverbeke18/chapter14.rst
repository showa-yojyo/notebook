======================================================================
The Document Object Model
======================================================================

`Eloquent JavaScript <https://eloquentjavascript.net/>`__ Chapter 14 の読書ノート。

Web ページをブラウザーで開くと、第 12 章の解析器がプログラムを解析するのと同じよ
うに、ブラウザーはページの HTML テキストを解析する。文書構造のモデルを構築し、こ
のモデルを使って画面にページを描画する。本章ではこのモデルを学ぶ。

この章の内容は Web スクレイピングの初等知識が満載なので、必ず履修すること。

.. contents:: ノート目次

Document structure
======================================================================

* HTML 文書を入れ子になった箱の集合と考えることができる。
* 文書を表現するのにブラウザーが使うデータ構造は木構造をしている。それぞれの枝に
  はオブジェクトが存在し、それによって何が何であるかを知る。このモデルを短く
  :dfn:`DOM` と呼ぶ。
* 大域変数 ``document`` はこれらのオブジェクトにアクセスするのに使える。

  * プロパティー ``document.documentElement`` は ``<html>`` タグを表すオブジェク
    トを参照している。
  * すべての HTML 文書には ``<head>`` と ``<body>`` が一つずつあるので、プロパ
    ティー ``document.head`` と ``document.body`` もまた存在し、対応するオブジェ
    クトそれぞれを参照している。

Trees
======================================================================

* 第 12 章の構文木の構造はブラウザーの文書のそれに酷似している。各ノードは他の
  ノード、子を参照することが許され、その子らもまた自身の子があっても構わない。こ
  の形は、要素が自分と似た部分要素を含むことができるという、典型的な入れ子構造
  だ。
* ここでは分岐した構造であり、循環がなく、単一の根があるものを :dfn:`木` と呼ぶ
  ことにする。

  * 循環がないというのは、節が直接的にも間接的にも自分自身を含まないことを意味す
    る。
  * DOM の場合は ``document.documentElement`` が根となる。

* 木構造は計算機科学によく登場する。HTML 文書などの再帰的構造を表現するだけでな
  く、ソート済みデータを管理するのにもよく用いられる。要素の検索や挿入が配列より
  効率的にできるからだ。

DOM では HTML のタグを表す要素のノードは文書の構造を決定する。要素ノードは子ノー
ドを持つことができる。

* ``document.body`` は子ノードとしてテキストやコメントを持つこともある。
* DOM ノードオブジェクトにはプロパティー ``nodeType`` があり、この値でノードの種
  類を識別する。

  * 要素は ``Node.ELEMENT_NODE``
  * テキストは ``Node.TEXT_NODE``
  * コメントは ``Node.COMMENT_NODE``

The standard
======================================================================

* DOM のインターフェイスが JavaScript らしくない理由は、それが JavaScript のため
  だけに設計されたものではないからだ。そうではなく、DOM は他のシステムからも使用
  できる、言語中立的なインターフェイスを志向している。そのため JavaScript からす
  ると残念な点がいくつかある。

  * 要素ノードのプロパティー ``childNodes`` は配列のようなオブジェクトではある
    が、実際の型は ``NodeList`` というものであり、便利なメソッドである ``slice``
    や ``map`` などが備わっていない。
  * これは単に設計が悪いだけだが、新しいノードを作成して、すぐに子や属性を追加す
    る方法がない。代わりに、まずノードを作成してから、副作用を使って子や属性を一
    つずつ追加していくしかない。

* DOM を多用するコードは長く、繰り返しが多く、醜くなりがちだ。そこで、JavaScript
  で独自の抽象化を施して、改良された方法を設計することになる。多くのライブラリー
  にはそのようなツールが備わっている。

Moving through the tree
======================================================================

* 本書 p. 235 の図式で示されるように、DOM ノードは近隣のノードへのリンクを豊富に
  含んでいる。

  * ``childNodes``, ``firstChild``, ``lastChild``
  * ``previousSibling``, ``nextSibling``
  * ``parentNode``

* 親と子のリンクさえあれば木のどのノードにも移動することができる。
* プロパティー ``firstChild`` と ``lastChild`` はそれぞれ最初と最後の子要素を指
  す。子のないノードの場合には ``null`` になっている。
* プロパティー ``previousSibling`` と ``nextSibling`` は隣接するノードを指す。同
  じ親であり、それぞれノード自身の直前と直後にあるノードだ。該当するノードがない
  場合には ``null`` になる。
* プロパティー ``children`` は ``childNode`` のようではあるが、要素ノードしか含
  まず、他の種類の子ノードを含まない。

  * テキストノードに興味がないなどの場合に便利。

入れ子構造を扱うときには再帰関数がしばしば役に立つ。次の関数は、文書をスキャンし
て指定する文字列を含むテキストノードを検索する：

.. code:: javascript

   function talksAbout(node, string) {
       if (node.nodeType == Node.ELEMENT_NODE) {
           for (let child of node.childNodes) {
               if (talksAbout(child, string)) {
                   return true;
               }
           }
           return false;
       } else if (node.nodeType == Node.TEXT_NODE) {
           return node.nodeValue.indexOf(string) > -1;
       }
   }

* テキストノードのプロパティー ``nodeValue`` は、そのノードが表現する文字列を値
  とする。

Finding elements
======================================================================

``getElementBy`` 系のメソッドを理解する。

* 要素ノードのメソッド ``getElementByTagName`` は、そのノードの子孫ノードの集合
  から、指定するタグ名の要素をすべて集めて、前述の配列のようなオブジェクトとして
  返す。
* 特定の単一ノードを見つけるには、そのノードに ``id`` 属性を与えて、メソッド
  ``document.getElementById`` を使う。
* メソッド ``getElementsByClassName`` は属性 ``class`` が指定された文字列である
  ような要素すべてを返す。

Changing the document
======================================================================

DOM のデータ構造は、ほとんどすべてを変更できる。文書木の形は親子関係を変更するこ
とで改変することができる。

* ノードメソッド ``remove`` は、現在の親ノードからノードを取り除く。
* 子ノードを追加するには、次が使える：

  * ``appendChild``
  * ``insertBefore``

  .. code:: html

     <p>One</p>
     <p>Two</p>
     <p>Three</p>
     <script>
     let paragraphs = document.body.getElementsByTagName("p");
     document.body.insertBefore(paragraphs[2], paragraphs[0]);
     </script>

  同一ノードは文書中に一つの場所にしか存在できない。したがって、段落 ``Three``
  を段落 ``One`` の前に挿入すると、まず ``One`` を文書から取り除いてから先頭に挿
  入する。結果は ``Three`` / ``One`` / ``Two`` となる。

  * 既存のノードをどこかに挿入する操作は、それを現在の位置から除去するという操作
    を暗黙的に伴うことに注意。

* メソッド ``replaceChild`` は子ノードを別のノードで置換するために使われる。

  * このメソッドは新ノードと旧ノードを引数に取る。
  * 置換されるノードは、メソッドの要素の子でなければならない。
  * ``insertBefore`` 同様、最初の引数が新ノードであることに注意を要する。

Creating nodes
======================================================================

文書中の ``<img alt="XXXX">`` すべてをテキスト ``XXXX`` に置き換えるスクリプトを
書きたいとする。こうなると、画像タグを削除するだけでなく、代わりとなる新しいテキ
ストノードを追加する必要がある。それにはメソッド ``document.createTextNode`` を
使う。

.. code:: javascript

   function replaceImages() {
       let images = document.body.getElementsByTagName("img");
       for (let i = images.length - 1; i >= 0; i--) {
           let image = images[i];
           if (image.alt) {
               let text = document.createTextNode(image.alt);
               image.parentNode.replaceChild(text, image);
           }
       }
   }

* ループで画像を後ろから始めることに注意。あるいは ``Array.from`` を使って作業用
  の配列を作成する手法もある。

要素ノードを作成するにはメソッド ``document.createElement`` を使う。タグの名前を
引数に取って、その新しい空のノードを返す。

Attributes
======================================================================

* リンクに対する ``href`` がそうであるように、要素の属性には、DOM オブジェクト上
  の同名のプロパティーでアクセスできるものがある。
* HTML ではノードに任意の属性を設定することが許されている。こういう場合には先ほ
  どにプロパティーとしては表示されない。メソッド ``getAttribute``,
  ``setAttribute`` を使って扱う必要がある。

  .. code:: html

     <p data-classified="secret">The launch code is 00000000.</p>
     <p data-classified="unclassified">I have two feet.</p>
     <script>
     let paras = document.body.getElementsByTagName("p");
     for (let para of Array.from(paras)) {
         if (para.getAttribute("data-classified") == "secret") {
             para.remove();
         }
     }
     </script>

* 自作の属性の名前は、他の属性と衝突しないようにすること。
* よく使われる属性に ``class`` があるが、これは JavaScript のキーワードでもあ
  る。この属性にアクセスするプロパティーは ``className`` という。

  * ``getAttribute``, ``setAttribute`` を使えば ``"class"`` でもよい。

Layout
======================================================================

* 要素の型によってレイアウトが異なる。

  * ``<p>`` や ``<h1>`` のように、画面の幅全体を使って個別の行に表示されるものを
    :dfn:`ブロック要素` と呼ぶ。
  * ``<a>`` や ``<strong>`` など、周囲のテキストと同じ行に表示されるものを
    :dfn:`インライン要素` と呼ぶ。

* 要素のサイズと位置は JavaScript からアクセスできる。

  * プロパティー ``offsetWidth``, ``offsetHeight`` は、要素が占める空間をピクセ
    ル単位で与える。
  * プロパティー ``clientWidth``, ``clientHeight`` は、要素の空間的大きさを示
    す。枠は無視する。

* 画面上の要素の正確な位置を知る最も効果的な方法はメソッド
  ``getBoundingClientRect`` だ。

  * これはプロパティーとして ``top``, ``bottom``, ``left``, ``right`` を持つオブ
    ジェクトを返す。各プロパティーは、画面左上からの相対的なピクセル単位での変位
    を示す。

    * 文書全体に対する相対的な位置を示したいならば、現在のスクロール位置を加味す
      る。変数 ``pageXOffset`, ``pageYOffset`` が使える。

* レイアウトはひじょうに手間がかかる。ブラウザーエンジンは文書が変更されるたびに
  ただちにレイアウトし直すのではなく、できる限り遅延する。変更した JavaScript プ
  ログラムの実行が終了すると再計算して、変更後の文書を描画する。
* DOM レイアウト情報を読み取ることと DOM を変更することを交互に反復するプログラ
  ムは多くのレイアウト計算を強いる。その結果、動作が著しく遅くなる。

Styling
======================================================================

* HTML の要素には既定のスタイリングがある。これを ``style`` 属性で上書きすること
  ができる。

  .. code:: html

     <p><a href=".">Normal link</a></p>
     <p><a href="." style="color: green">Green link</a></p>

  * 属性 ``style`` には複数の宣言を含めることができる。一つ一つの宣言を ``;`` で
    区切ればよい。

* JavaScript コードは、要素のスタイルを直接操作することができる。このプロパ
  ティー ``style`` には、可能なすべてのスタイルプロパティーを保持する。

  * これらのプロパティーの値は文字列であり、要素のスタイルの特定の観点を変更する
    ために書くことができる。

    .. code:: javascript

       let para = document.getElementById("para");
       console.log(para.style.color);
       para.style.color = "magenta";

* スタイルプロパティー名には ``font-family`` のようにハイフンを含むものがある。
  このようなプロパティー名は、JavaScript ではドット記法が使えず扱いにくいため、
  そのようなプロパティーに対するスタイルオブジェクトのプロパティー名は、ハイフン
  が取り除かれ、後ろの文字が大文字になるという規則がある。この場合には
  ``style.fontFamily`` となる。

Cascading styles
======================================================================

* HTML のスタイルシステムは CSS と呼ばれている。
* スタイルシートとは、文書内の要素にスタイルを与えるための規則の集合体だ。
* スタイルシートは ``<style>`` タグの中に記述する。

  .. code:: html

     <style>
     strong {
         font-style: italic;
         color: gray;
     }
     </style>

* 名前にある cascading とは、このような複数の規則を組み合わせて要素の最終的なス
  タイルを生成することを意味する。
* 同じプロパティーの値を複数の規則が定義する場合、最近読まれた規則を優先する。
* そのノードに直接適用される属性 ``style`` にあるスタイルを最も優先する。

CSS の規則では、タグ名以外にも指定の対象とすることができる。

* ``.abc`` に対する規則は属性 ``class`` の値が ``abc`` である要素全てにかかる。
* ``#abc"`` に対する規則は属性 ``id`` の値が ``xyz`` である要素にかかる。

最近に定義された規則を優先するという法則は、規則の :dfn:`指定度` (specificity)
が同じ場合にのみ成り立つ。

* 規則の指定度とは、合致する要素をどの程度正確に記述するのかを示す指標であって、
  数と要素の種類によって決定するものだ。

  * これは CSS の仕様書を確認するのがいい。

Query selectors
======================================================================

CSS セレクターはスタイルシートでスタイルの適用対象となる要素を特定するために使わ
れる記法だ。これを使えば DOM 要素を効果的に見つけることができる。

メソッド ``querySelectorAll`` は文書オブジェクトと要素ノードの両方で定義されてい
て、セレクター式を文字列で受け取り、それに合致する要素全てからなる ``NodeList``
を返す。

.. code:: html

   <p>And if you go chasing<span class="animal">rabbits</span></p>
   <p>And you know you're going to fall</p>
   <p>Tell 'em a <span class="character">hookah smoking <span class="animal">caterpillar</span></span></p>
   <p>Has given you the call</p>

   <script>
     function count(selector) {
         return document.querySelectorAll(selector).length;
     }

     console.log(count("p")); // → 4; All <p> elements:
     console.log(count(".animal")); // → 2; Class animal
     console.log(count("p .animal")); // → 2; Animal inside of <p>
     console.log(count("p > .animal")); // → 1; Direct child of <p>
   </script>

* ``getElementsByTagName`` などとは異なり、``querySelectorAll`` の返すオブジェク
  トは生のものではない。このあと文書を変更してもそれは変化しない。
* 配列のように扱うのならば、やはり ``Array.from`` を呼び出す必要がある。

メソッド ``querySelector`` も同様に動作する。こちらは特定の単一の要素が欲しい場
合に役に立つ。

Positioning and animating
======================================================================

* スタイルプロパティー ``position`` は、強力な方法でレイアウトに影響を与える。

  * 既定値は ``static`` というものだ。これは要素が文書内の通常の場所にあることを
    意味する。
  * 値 ``relative`` に設定すると、要素は文書内の空間を占有することはするのだがス
    タイルプロパティー ``top`` と ``left`` のを使用して、通常の場所からの相対的
    な位置に移動させることができる。
  * 値 ``absolute`` に設定されている場合、その要素は通常の文書フローから削除され
    る。つまり、空間を取らなくなり、他の要素と重なる可能性がある。

* また、``top`` および ``left`` プロパティを使用して、プロパティー ``position``
  が``static`` ではないような包囲要素の左上隅に対して絶対的に（そのような包囲要
  素が存在しない場合には文書に対して相対的に）位置を決めることができる。

これを利用してアニメーションを作れる。本書 p. 247 のコードは楕円を動き回るネコの
絵を描画する。

.. code:: html

   <p style="text-align: center">
   <img src="img/cat.png" style="position: relative">
   </p>

   <script>
     let cat = document.quaerySelector("img");
     let angle = Math.PI / 2;
     function animate(time, lastTime) {
         if (lastTime != null) {
             angle += (time - lastTime) * 0.001;
         }
         cat.style.top = (Math.sin(angle) * 20) + "px";
         cat.style.left = (Math.cos(angle) * 200) + "px";
         requestAnimationFrame(newTime => animate(newTime, time));
     }
     requestAnimationFrame(animate);
   </script>

興味のあるポイントだけ記すと：

* 画像はページの中央に置かれ、相対位置が与えられる。その ``top`` と ``left`` を
  反復的に更新して移動させる。
* 関数 ``requestAnimationFrame`` はブラウザーが画面を再描画する準備ができたとき
  に関数 ``animate`` を実行させるようにスケジュールをしている。

  * 関数 ``animate`` はまた ``requestAnimationFrame`` を呼び出し、次の更新をスケ
    ジュールする。

    * 次の更新はブラウザーのウィンドウがアクティブであれば、一秒間に約 60 回発生
      する。

* これをループで書こうものなら、ページはフリーズして画面には何も描画されない。
  JavaScript の実行中にはブラウザーは画面を更新しないことに注意する。したがって
  アニメーションには上記のようなコードが必要だ。
* アニメーションそれ自体は三角関数を単純に応用して点を運動させるものなのでメモを
  割愛する。
* 数値に ``"px"`` を明示的に付けて、ピクセル単位で位置を表現していることをブラウ
  ザーに伝える。これを忘れると、スタイルは値がゼロでない限り無視される（というこ
  とは結局つねに無視される）。

Summary
======================================================================

* JavaScript は DOM というデータ構造ごしに、ブラウザーが表示する文書を検査・干渉
  することができる。
* DOM はデータ構造が木のように整理されていて、文書の論理構造に対応するように要素
  が階層的に配置されている。

  * 要素を表すオブジェクトには ``parentNode`` や ``childNodes`` などのプロパ
    ティーがある。これらは木の中をたどるのに使える。

* 文書を描画する方法はスタイリングにより左右される。ノードに直接スタイルを指定し
  たり、ある一定のノードの集合に合致する規則を定義したりする方法がある。
* スタイルのプロパティーには ``color`` や ``display`` などというものがたくさんあ
  る。
* JavaScript では要素のプロパティー ``style`` を通じてスタイルを直接できる。

Exercises
======================================================================

Build a table
----------------------------------------------------------------------

HTML のテーブルは、以下のようなタグ構造をしている：

.. code:: html

   <table>
     <tr>
       <th>name</th>
       <th>height</th>
       <th>place</th>
     </tr>
     <tr>
       <td>Kilimanjaro</td>
       <td>5895</td>
       <td>Tanzania</td>
     </tr>
   </table>

各行に対して ``<table>`` タグは ``<tr>`` タグを一つ含んでいる。これらの ``<tr>``
タグの中には見出しセル ``<th>`` や通常のセル ``<td>`` などのセル要素を置くことが
できる。

**問題** 名前、高さ、場所のプロパティーがあるオブジェクトの配列である山のデータ
セットが与えられた場合、そのオブジェクトを列挙する表の DOM 構造を生成しろ。キー
ごとに一列、オブジェクトごとに一行、それに加えてまた、最上部に ``<th>`` 要素を持
つヘッダー行を設け、列名を列挙すること。

* これを、データ中の最初のオブジェクトのプロパティー名を取ることで、列が自動的に
  オブジェクトから得られるように書け。
* できあがったテーブルを属性 ``id`` が ``mountains`` である要素に追加して、文書
  内で表示されるようにしろ。
* これができたら、数値を含むセルを右揃えにするためにプロパティー
  ``style.textAlign`` を ``right`` に設定しろ。

**解答** いちばん単純なコードをまず書く：

.. code:: javascript

   function buildTable(mountains){
       const table = document.createElement('table');
       // header row
       const tr = table.appendChild(document.createElement('tr'))
       for(const text of ["name", "height", "place"]){
           const th = tr.appendChild(document.createElement('th'));
           th.appendChild(document.createTextNode(text));
       }

       // regular rows
       for(const mountain of mountains){
           const tr = table.appendChild(document.createElement('tr'))
           const {name, height, place} = mountain;
           for(let i of [name, height, place]){
               const td = tr.appendChild(document.createElement('td'));
               td.appendChild(document.createTextNode(i));
           }
       }

       return table;
   }

テーブルヘッダー行を自動生成するには：

.. code:: javascript

   if(montains.length == 0){
       return table;
   }

   const tr = table.appendChild(document.createElement('tr'))
   const columns = Object.keys(mountains[0]);
   for(const colName of columns){
       const th = tr.appendChild(document.createElement('th'));
       th.appendChild(document.createTextNode(colName));
   }

できあがったテーブルを属性 ``id`` が ``mountains`` である要素に追加するコードは次のようになる：

.. code:: javascript

   const mountains = [
       {name: "Killmanjaro", height: 5895, place: Tanzania},
       // ...
   ];

   document.getElementById("mountains").appendChild(buildTable(mountains));

右揃えはテーブル作成後ならば：

.. code:: javascript

   document.querySelectorAll('#mountains > table > tr > td:nth-child(2)');
   nodes.forEach(node => node.style.textAlign = "right");

Elements by tag name
----------------------------------------------------------------------

メソッド ``document.getElementsByTagName`` は、指定されたタグ名を持つすべての子
要素を返す。

**問題** ノードとタグ名を引数にとり、与えられたタグ名を持つすべての子孫要素ノー
ドを含む配列を返す関数として、これの独自版を実装しろ。

ある要素のタグ名を調べるには、その要素のプロパティー ``nodeName`` を使え。ただ
し、これはタグ名をすべて大文字で返す。これを補うには文字列メソッド
``toLowerCase`` または ``toUpperCase`` を使え。

**解答** これで良いと思われる：

.. code:: javascript

   function getAncestors(node, tagName){
       return Array.from(node.querySelectorAll(tagName));
   }

The cat's hat
----------------------------------------------------------------------

**問題** 先ほどの猫のアニメーションを拡張して、猫と帽子の両方が楕円の反対側を周
回するようにしろ。

* あるいは、帽子が猫の周りを回るようにしろ。
* あるいは、アニメーションを他の面白い方法に変えろ。

複数のオブジェクトの配置を容易にするには、絶対配置に切り替えるのがよいだろう。つ
まり、``top`` と ``left`` は文書の左上を基準にしてカウントされる。負の座標を使用
すると表示されているページの外側に画像が移動してしまうのを避けるのに、位置の値に
固定のピクセル数を追加することができる。

**解答** こういうのは得意。

.. code:: html

   <p style="text-align: center">
     <img id="cat" src="img/cat.png" style="position: absolute">
     <img id="hat" src="img/hat.png" style="position: absolute">
   </p>

   <script>
     const a = 400, b = 200;
     const centerX = a, centerY = b;
     const marginX = 20, marginY = 20;

     const cat = document.querySelector("img#cat");
     const hat = document.querySelector("img#hat");
     let angle = Math.PI / 2;

     const x = theta => marginX + centerX + (a * Math.cos(theta)) + "px";
     const y = theta => marginY + centerY + (b * Math.sin(theta)) + "px";

     function animate(time, lastTime) {
       if (lastTime != null) {
         angle += (time - lastTime) * 0.001;
       }
       cat.style.left = x(angle);
       cat.style.top = y(angle);

       hat.style.left = x(angle + Math.PI);
       hat.style.top = y(angle + Math.PI);

       requestAnimationFrame(newTime => animate(newTime, time));
     }
     requestAnimationFrame(animate);
   </script>

帽子を猫中心に回すには、帽子用の楕円のため定数を追加したり、属性設定関数の引数を
拡張したりするといいだろう。

以上
