======================================================================
Web components
======================================================================

.. contents::
   :depth: 2

Web components とは、自己完結型のコンポーネントを作るための標準規格の集合であ
り、独自のプロパティーやメソッドを持つカスタム HTML 要素、カプセル化された DOM
とスタイルだ。

From the orbital height
======================================================================

<https://javascript.info/webcomponents-intro> ノート。

現在のところ、これらの標準は開発中だ。十分にサポートされていて、最新の HTML/DOM
標準に統合されている機能もあれば、まだ草稿の段階である機能もある。おそらく
Google Chrome がこれらの機能に関して最も up-to-date だと考えられる。

What's common between...
----------------------------------------------------------------------

国際宇宙ステーションは、

* 多くの部品から構成され、
* それぞれの部品には細かい部品がたくさん入っている。
* 部品はたいへん複雑で、普通のウェブサイトよりもずっと複雑だ。
* 部品を、異なる国、異なる言語を話すチームが国際的に開発している。

このような複雑な装置はどのようにして作られるのだろうか。どのような原理を借りれ
ば、同じ水準の信頼性と拡張性を持つ開発ができるだろうか。あるいは、少なくともそれ
に近いだろうか。

Component architecture
----------------------------------------------------------------------

複雑なソフトウェアを開発する際のよく知られたルールは、「複雑なソフトウェアを作る
な」だ。もし何かが複雑になったら、より単純な部分に分割し、最もわかりやすい方法で
接続することだ。

ユーザーインターフェースは、視覚的な構成要素に分割することができる。それぞれの構
成要素は、ページ上に独自の場所を持ち、きちんと説明された仕事を遂行することがで
き、他の要素から分離されている。例えば、Twitter のようなウェブサイトを見ると、コ
ンポーネントに自然に分割できる。

コンポーネントとは何か、どうやって決めるのか。それは直感、経験、常識から出てく
る。通常、コンポーネントとは、それが何を行い、どのようにページと相互作用するかと
いう観点から説明できる、独立した視覚的な実体のことだ。Twitter の UI の例では、
ページには塊があり、それぞれが独自の役割を担っているので、これをコンポーネントと
するのが論理的だ。

コンポーネントには次のものがある：

* 独自の JavaScript クラス。
* DOM 構造はそのクラスによってのみ管理され、外部のコードはそれにアクセスしない（カプセル化の原則）。
* 適用される CSS スタイル。
* API: イベント、クラスメソッドなど、他のコンポーネントと相互作用するためのもの。

コンポーネントを構築するためのフレームワークや開発手法は数多く存在し、それぞれが
独自の機能を備えている。通常、コンポーネントらしさを実現するために、特別なCSS ク
ラスや規約、つまり CSS スコープや DOM カプセル化などが用いられる。

Web components はそのためのブラウザー機能を内蔵している。それらをこれ以上模倣す
る必要はない。

* 自作要素：カスタムの HTML 要素を定義する。
* Shadow DOM: コンポーネントの内部 DOM を作成し、他から隠す。
* CSS スコープ定義：コンポーネントの Shadow DOM 内部のみに適用するスタイルを宣言する。
* イベント再標的：カスタムコンポーネントをより開発に適したものにする。

Custom elements
======================================================================

<https://javascript.info/custom-elements> ノート。

独自のメソッド、プロパティー、イベントなどを持つ、クラスで記述されたカスタムHTML
要素を作成することができる。いったん自作要素を定義すれば、組み込み HTML要素
と同等に使用できる。 ``<easy-tabs>``, ``<sliding-carousel>``,
``<beautiful-upload>`` などのタグを使えるように、特別なクラスを定義し、あたかも
それらが HTML の一部であるかのように使用できるのだ。

自作要素は二種類ある：

1. 自律的な自作要素。抽象クラス ``HTMLElement`` を拡張した「全く新しい」要
   素。
2. カスタマイズされた組み込み要素。``HTMLButtonElement`` などをベースにカスタマ
   イズされたボタンなど、組み込み要素を拡張したもの。

まず自律的な要素をやる。自作要素を作成するには、その要素に関するいくつかの詳
細をブラウザーに伝える必要がある。どのように表示するか、要素がページに追加または
削除されたときに何をするか、等。これを特別なメソッドを持つクラスを作成することで
行う。メソッドの数は少なく、すべてオプショナルなので簡単だ。

.. code:: javascript

   class MyElement extends HTMLElement {
       // 本書参照
   }

   // let the browser know that <my-element> is served by our new class
   customElements.define("my-element", MyElement);

これによって、タグ ``<my-element>`` のある HTML 要素に対して、
``MyElement`` インスタンスが生成され、前述のメソッドが呼び出されるようになった。
JavaScript からでも

.. code:: javascript

   document.createElement('my-element')

を使うことができる。

自作要素名には記号 ``-`` が必要だ。例えば、``my-element`` と
``super-button`` は有効な名前だが、``myelement`` は無効な名前だ。組み込み HTML
要素とカスタム HTML 要素の間で名前の衝突が起きないようにするために、そのように規
定されている。

Example: "time-formatted"
----------------------------------------------------------------------

例えば、HTML には日付・時刻を表す ``<time>`` が既に存在する。しかし、これだけで
は何の書式化もできない。そこで、言語を意識した美しい書式で時刻を表示する
``<time-formatted>`` を作成する。

.. code:: javascript

   class TimeFormatted extends HTMLElement {
       connectedCallback() {
           let date = new Date(this.getAttribute('datetime') ?? Date.now());
           this.innerHTML = new Intl.DateTimeFormat("default", {
               /* 本書参照 */;
           }).format(date);
       }
   }

   customElements.define("time-formatted", TimeFormatted);

このクラスは ``connectedCallback()`` というメソッド一つだけを持っている。ブラウ
ザーは ``<time-formatted>`` がページに追加されたとき（または HTML 解析器がそれを
検出したとき）これを呼び出し、ブラウザー全体で十分にサポートされている組み込みの
``Intl.DateTimeFormat`` データフォーマッターを使用して、きれいにフォーマットされ
た時間を表示する。

.. code:: html

   <time-formatted datetime="2019-12-01"
     year="numeric" month="long" day="numeric"
     hour="numeric" minute="numeric" second="numeric"
     time-zone-name="short"
   ></time-formatted>

----

``customElements.define`` 呼び出し前に ``<time-formatted>`` 要素にブラウザーが遭
遇しても、それはエラーではない。その要素はまだ未定義であり、非標準のタグと同じ扱
いになる。このような未定義要素は CSS セレクターの ``:not(:defined)`` でスタイル
を与えられる。

``customElement.define`` が呼ばれると、それらは「アップグレード」される。それ
ぞれについて新しい ``TimeFormatted`` インスタンスが生成され、
``connectedCallback`` が呼ばれる。これらは ``:defined`` となる。

自作要素に関する情報を取得するためのメソッド：

* ``customElements.get(name)``: 与えられた ``name`` の自作要素のクラスを返
  す。
* ``customElements.whenDefined(name)``: 与えられた ``name`` の自作要素が定義
  されたときに resolve する ``Promise`` を返す。

----

上記の例で ``connectedCallback()`` で要素の内容を作成していることに注意。仮にコン
ストラクターで内容を作成すると、早過ぎるのだ。ブラウザーはこの段階ではまだ属性を
処理できておらず、 ``getAttribute()`` を呼び出すと ``null`` が返される。これではレ
ンダリング不能だ。さらに、本当に必要なときまで作業を遅らせることは、能率の点でも
優っている。

メソッド ``connectedCallback()`` は、要素がページに追加されたときに起動される。単
に他の要素に子として追加されるだけでなく、実際にページの一部になる。つまり、切り
離された DOM を構築し、要素を生成し、後で使用するための準備をすることができる。
実際にレンダリングされるのはページ内に追加されたときだけだ。

Observing attributes
----------------------------------------------------------------------

現在の ``<time-formatted>`` の実装では、要素がレンダリングされた後、それ以上の属
性変更は何の効果もない。HTML 要素としては奇妙なことだ。そこで、これを修正する。

``observedAttributes()`` で属性のリストを提供することで、属性を観察することがで
きる。このような属性については、その属性が変更されたときに
``attributeChangedCallback()`` が呼び出される。他のリストされていない属性に対し
ては呼び出されない。これは性能上の理由による。

属性が変更されたときに自動更新されるようにする：

.. code:: javascript

   class TimeFormatted extends HTMLElement {
       render() {
           // 従来と同様
       }

       connectedCallback() {
           if (!this.rendered) {
               this.render();
               this.rendered = true;
           }
       }

       static get observedAttributes() {
           return ['datetime', 'year', 'month', 'day', 'hour', 'minute', 'second', 'time-zone-name'];
       }

       attributeChangedCallback(name, oldValue, newValue) {
           this.render();
       }
   }

   customElements.define("time-formatted", TimeFormatted);

   // 別の場所
   setInterval(() => elem.setAttribute('datetime', new Date()), 1000);

レンダリングのロジックは ``render()`` メソッドに移された。要素がページに挿入され
たときに一度だけ呼び出されるものとする。``observedAttributes()`` にリストされて
いる属性が変更されると、``attributeChangedCallback()`` が起動し、要素を再描画す
る。

最終的にライブタイマーを容易に作成することができる。

Rendering order
----------------------------------------------------------------------

HTML 解析器 が DOM を構築するとき、要素は親から子へと順番に処理される。これは、
自作要素にとって重要な結果をもたらす。例えば、自作要素が ``connectedCallback()``
で``innerHTML`` にアクセスしようとすると何も得られない。

自作要素に情報を渡したい場合は、属性を使うことができる。これはすぐに利用できる。
または、もし本当に子要素が必要なら、遅延ゼロの ``setTimeout()`` で子要素へのアク
セスを延期してもよい。

この解決策も完璧ではない。入れ子になった自作要素も自分自身を初期化するために
``setTimeout()`` を使用する場合、それらはキューに入る。すなわち、外側の
``setTimeout()`` が最初に発生し、次に内側のものが発生する。つまり、外側の要素が
内側の要素より先に初期化を終えてしまうのだ。

.. code:: html

   <user-info id="outer">
     <user-info id="inner"></user-info>
   </user-info>

次のように実装すると、外側の要素が内側の要素よりも先に初期化を終えていることを確
認できる：

.. code:: javascript

   connectedCallback() {
       alert(`${this.id} connected.`);
       setTimeout(() => alert(`${this.id} initialized.`));
   }

入れ子になった要素の準備ができた後に発生する組み込みコールバックはない。必要であ
れば、そのようなものを独自に実装することができる。例えば、内側の要素は初期化など
のイベントを dispatch し、外側の要素はそれを listen して反応させることができる。

Customized built-in elements
----------------------------------------------------------------------

特殊なボタンを作るのであれば、既存の ``<button>`` の機能を再利用するのが自然だ。
組み込み HTML 要素は、そのクラスを継承して拡張したりカスタマイズしたりすることが
できる。ボタンは ``HTMLButtonElement`` インスタンスなので、これをベースに作って
みる。

1. ``HTMLButtonElement`` を自作クラスで拡張する。
2. ``customElements.define()`` の第三引数にタグを指定する。同じ DOM クラスを共有
   する異なるタグが存在する可能性があるため、 ``extends`` の指定が必要だ。
3. 自作要素を使用するために通常の ``<button>`` タグを挿入するが、
   ``is="hello-button"`` を追加する。

.. code:: html

   <script>
   // The button that says "hello" on click
   class HelloButton extends HTMLButtonElement {
       constructor() {
           super();
           this.addEventListener('click', () => alert("Hello!"));
       }
   }

   customElements.define('hello-button', HelloButton, {extends: 'button'});
   </script>

   <button is="hello-button">Click me</button>
   <button is="hello-button" disabled>Disabled</button>

新しいボタンは組み込みボタンを拡張したものだ。スタイルや属性など、標準的な機能を
維持する。

.. admonition:: 学習者ノート

   動的にサブクラスを定義できるようなものだ。

Tasks
----------------------------------------------------------------------

Live timer element
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

現在の時刻を表示するために 要素を定義しろ。

1. これは内部で ``<time-formatted>`` を使うべきだ。機能を重複させるべきではな
   い。
2. 毎秒刻め。
3. 刻みごとに、カスタムイベント ``tick`` が生成され、現在の日付を
   ``event.detail`` に入れろ。

.. code:: html

   <live-timer id="elem"></live-timer>

   <script>
   elem.addEventListener('tick', event => console.log(event.detail));
   </script>

1. ページから要素が削除されたとき、``setInterval`` をクリアすること。そうでなけ
   れば、もう必要ないにもかかわらず、カチカチと音を立て続けることになる。そし
   て、ブラウザーはこの要素とそれによって参照されるものからメモリーをクリアする
   ことができない。
2. 現在の日付は ``elem.date`` としてアクセスできる。すべてのクラスのメソッドとプ
   ロパティーは、当然ながら要素のメソッドとプロパティーだ。

Shadow DOM
======================================================================

<https://javascript.info/shadow-dom> ノート。

Shadow DOM はカプセル化のために機能する。これにより、コンポーネントはそれ自身の
「影」の DOM 木を持つことができ、主ページから誤ってアクセスされることはないし、
スタイルに関するハウスルールなどを決めることもできる。

Built-in shadow DOM
----------------------------------------------------------------------

``<input type="range">`` などを、ブラウザーは内部で DOM/CSS を使って描画してい
る。この DOM 構造は開発者向けツールで見られる。 Google Chrome の場合、開発ツール
の Show user agent shadow DOM オプションを有効にする必要がある。

.. admonition:: 学習者ノート

   このオプションがどこにあるのか不明。

.. code:: html

   <input type="range">
       #shadow-root (user-agent)
       <div>
           <div pseudo="-webkit-slider-runnable-track" id="track"></div>
           <div id="thumb"></div>
       </div>
   </input>

この ``#shadow-root`` の下に表示されるものを shadow DOM と呼ぶ。

通常の JavaScript の呼び出しやセレクターでは、組み込み shadow DOM 要素を取得でき
ない。これらは通常の子要素ではなく、強力なカプセル化技術なのだ。上の例では、便利
な属性 ``pseudo`` があることがわかる。これは非標準的なもので、歴史的な理由から存
在する。この属性は、CSS で部分要素のスタイルを指定するために用いられる。

.. code:: css

   input::-webkit-slider-runnable-track {
       background: red;
   }

時系列的には、ブラウザーが DOM の内部構造を使ってコントロールを実装する実験を始
めたのが ``pseudo`` の嚆矢で、その後、開発者が同様のことを行えるように shadow DOM
が標準化された。

この先は現代の shadow DOM 標準を使用する。

Shadow tree
----------------------------------------------------------------------

DOM 要素は、二種類の DOM 部分木があり得る。

1. Light tree: 通常の DOM 部分木であって、HTML の子要素で構成されている。これま
   での章で見てきた部分木はすべて light だ。
2. Shadow tree: HTML に反映されない、のぞき見されない隠れた DOM 部分木。

要素が両方を持つ場合、ブラウザーは shadow tree しか描画しない。しかし、
shadow tree と light tree の間にある種の合成を設定することも可能だ（詳細は後述）。

Shadow tree を自作要素で使用して、コンポーネント内部を隠したり、コンポーネント固
有のスタイルを適用したりすることができる。たとえば、本書の ``<show-hello>`` 要素
は shadow tree でその内部 DOM を隠蔽する。 Google Chrome の開発ツールで結果の
DOM を見ると、内容物すべてが ``#shadow-root`` の下にあることがわかる。

.. code:: html

   <show-hello name="John">
       #shadow-root (open)
       <p>Hello, John</p>
   </show-hello>

最初に ``elem.attachShadow({mode: ...})`` 呼び出しが shadow tree を生成する。制
約が二つある：

1. 要素一つにつき shadow root を一つしか生成できない。
2. ``elem`` は自作要素か、次のうちの一つでなければならない：

   * article
   * aside
   * blockquote
   * body
   * div
   * footer
   * h1...h6
   * header
   * main
   * nav
   * p
   * section
   * span

オプション ``mode`` は、カプセル化レベルを設定する。

* "open": shadow root が ``elem.shadowRoot`` として利用可能。どんなコードでも
  ``elem`` の shadow tree にアクセスすることができる。
* "closed": ``elem.shadowRoot`` は常に ``null`` となる。

``attachShadow()`` が返す参照によってしか shadow DOM にアクセスできない。
``<input type="range">`` のようなブラウザーネイティブの shadow tree は閉じてい
る。それらにアクセスする方法はない。

``attachShadow()`` が返す shadow root は要素のようなもので、 ``innerHTML`` や
``append()`` などの DOM メソッドを使用して、shadow root に情報を入力することがで
きる。

Shadow root を持つ要素は shadow tree host と呼ばれ、プロパティー ``host`` とし
て利用可能だ。

Encapsulation
----------------------------------------------------------------------

Shadow DOM はメインドキュメントから強く分離される。

1. Shadow DOM の要素は light DOM の ``querySelector`` からは見えない。特に、
   Shadow DOM の要素は light DOM の要素と矛盾する ID を持つ可能性がある。それら
   は shadow tree の中でのみ一意的でなければならない。
2. Shadow DOM は独自のスタイルシートを持つ。外部 DOM からのスタイルルールは適用
   されない。

ドキュメントからのスタイルは shadow tree に影響を与えない。
Shadow tree の要素を取得するには、木の内側から問い合わせを実行する必要がある。

Template element
======================================================================

<https://javascript.info/template-element> ノート。

組み込み ``<template>`` 要素は、HTML マークアップテンプレート置場として機能す
る。ブラウザーはその内容を無視し、構文の妥当性のチェックしかしないが、
JavaScript でそれにアクセスし、他の要素を作成するのに利用できる。

``<template>`` の内容は、通常は適切な囲みタグを必要とするものであっても、有効な
HTML であれば何でもよい。例えば、テーブルの行 ``<tr>`` をそこに置くことができ
る。通常、``<tr>`` を例えば ``<div>`` の中に置こうとすると、ブラウザーは無効な
DOM 構造を検出し、それを「修正」して ``<table>`` を周囲に追加する。一方、
``<template>`` は、そこに置いたものをそのまま保持する。

``<template>`` にはスタイルやスクリプトを入れることもできる。

ブラウザーは ``<template>`` 内容物を「文書の外にある」と見なす。つまりスタイルは
適用されず、スクリプトは実行されず、``<video autoplay>`` は実行されない、など。
内容物は、ページに挿入された時点で生を受ける（スタイルが適用され、スクリプトが実
行され、……といった具合だ）。

Inserting template
----------------------------------------------------------------------

テンプレートの内容物はプロパティー ``content`` に DOM ノードの特殊な型である
``DocumentFragment`` として利用可能だ。これを他の DOM ノードと同じように扱うこと
ができるが、特別な特性が一つある。これをどこかに挿入すると、代わりにその子（複数
形）が挿入される。

本書のコードを示す：

.. code:: html

   <template id="tmpl">
     <script>
       alert("Hello");
     </script>
     <div class="message">Hello, world!</div>
   </template>

   <script>
     let elem = document.createElement('div');
     elem.append(tmpl.content.cloneNode(true));
     document.body.append(elem);
   </script>

スクリプト部分を読むと、ページ内の ``template`` 要素への ``cloneNode()`` 呼び出
しがあることがわかる。これは ``template`` ではなく、その子である ``script`` およ
び ``div`` の二つを複製するということになる。複製を新規作成した ``div`` の末尾に
差し込んでいる。実行ボタンを押せば上の解読が正しそうだと思える。

----

前章の shadow DOM の例（に似たもの）を ``template`` を使って書き換える。
Shadow DOM 版はこういう感じ：

.. code:: javascript

   elem.attachShadow({mode: 'open'});
   elem.shadowRoot.innerHTML = `
       <style> p { font-weight: bold; } </style>
       <p id="message">Hello from the shadows!</p>
   `;

これがこうなる：

.. code:: javascript

   elem.attachShadow({mode: 'open'});
   elem.shadowRoot.append(tmpl.content.cloneNode(true));
   elem.shadowRoot.getElementById('message').innerHTML = "Hello from the shadows!";

``tmpl.content`` を複製して挿入する行では、その ``DocumentFragment`` として、そ
の子である ``style``, ``p`` が代わりに挿入される。

これらは shadow DOM を形成する。

Shadow DOM slots, composition
======================================================================

<https://javascript.info/slots-composition> ノート。

タブ、メニュー、イメージギャラリーなど、多くの種類のコンポーネントがレンダリング
のために中身を必要とする。組み込み ``<select>`` が ``<option>`` を期待するよう
に、自作 ``<custom-tabs>`` や ``<custom-menu>`` は実際のタブ中身やメニュー項目が
渡されることを期待するだろう。

.. code:: html

   <custom-menu>
     <title>Candy menu</title>
     <item>Lollipop</item>
     <item>Fruit Toast</item>
     <item>Cup Cake</item>
   </custom-menu>

与えられたタイトルとアイテムから、自作メニューを適切に描画したりイベント処理をし
たりする必要がある。

どのように実装するのか？要素の内容を解析して、DOM ノードを動的にコピーして並べ替
えることもできる。それでもいいが、要素を shadow DOM に移動する場合、ドキュメント
からの CSS スタイルはそこに適用されないので、視覚的スタイルが失われる可能性があ
る。また、そのために追加的なコーディングが必要だ。

幸いなことに、その必要はない。Shadow DOM は ``<slot>`` 要素をサポートしてお
り、light DOM からの中身で自動的に埋まる。

Named slots
----------------------------------------------------------------------

簡単な例で、スロットがどのように機能するかを見る。本書のコードでは
``<user-card>`` shadow DOM がスロットを二つ持ち、light DOM から埋められる。

スクリプトコードで ``innerHTML`` として現れている shadow DOM では、 ``<slot
name="X">`` が挿入ポイント、つまり ``slot="X"`` 要素が描画される場所を定義してい
る。

すると、ブラウザーは「合成」をする。HTML コードで現れている Light DOM から要素を
取得し、shadow DOM の対応するスロットに描画する。最終的には、データを埋めること
ができるコンポーネントが完成する。

.. admonition:: 学習者ノート

   本書では合成を考慮しないスクリプト実行後の DOM 構造がここに書かれている。これ
   は Google Chrome の検証ツールで示されるものと同じだ。

これで、この要素は light と shadow の両方の DOM を持つようになった。

描画するには、shadow DOM の各 ``<slot name="...">`` に対して、ブラウザーは light
DOM で同じ名前の ``<slot="...">`` を見つける。これらの要素はスロットの内部で描画
される。その結果を平坦化 DOM と呼ぶ。

しかし、平坦化 DOM は描画とイベント処理のためだけに存在する。実際にはドキュメン
ト内のノードは移動していないのだ。このことは ``querySelectorAll()`` を実行すれば
簡単に確認できる。ノードはまだ元の場所にある。

つまり、平坦化 DOM は、スロットを挿入することで shadow DOM から派生したものだ。
ブラウザーはこれを描画し、スタイル継承やイベント伝達に用いる。しかし JavaScript
では平坦化前のままのドキュメントを見ている。

----

トップレベルの子しか ``slot="..."`` 属性を持てない。属性 ``slot="..."``
は、shadow host の直接の子要素に対してしか有効でない。入れ子要素では無視される。
次の例では二番目の ``<span>`` は ``<user-card>`` の最上位の子ではないので無視さ
れる。

.. code:: html

   <user-card>
     <span slot="username">John Smith</span>
     <div>
       <span slot="birthday">01.01.2001</span>
     </div>
   </user-card>

----

Light DOM 内に同じスロット名を持つ要素が複数ある場合、それらは順番にスロットに追
加される。

Slot fallback content
----------------------------------------------------------------------

``<slot>`` の中に何かを入れると、それが既定の中身になる。対応する中身に相当する
ものが light DOM にない場合、ブラウザーはその ``<slot>`` の中の何かを表示する。
たとえば、この shadow DOM の断片で light DOM に ``slot="username"`` がない場
合、Anonymous が表示される：

.. code:: html

   <div>Name:
     <slot name="username">Anonymous</slot>
   </div>

Default slot: first unnamed
----------------------------------------------------------------------

Shadow DOM の ``<slot>`` で名前を持たない最初のものが既定スロットだ。これは、他
の場所でスロット化されていない light DOM のノードすべてを得る。

例えば shadow DOM を次のようにする：

.. code:: html

   <div>Name:
     <slot name="username"></slot>
   </div>
   <div>Birthday:
     <slot name="birthday"></slot>
   </div>
   <fieldset>
     <legend>Other information</legend>
     <slot></slot>
   </fieldset>

ノート：この ``<slot></slot>`` が既定スロットとなる。

対応する light DOM を次のようにしてみる：

.. code:: html

   <user-card>
     <div>I like to swim.</div>
     <span slot="username">John Smith</span>
     <span slot="birthday">01.01.2001</span>
     <div>...And play volleyball too!</div>
   </user-card>

スロットされていない light DOM の中身である ``<div>`` 要素二つは、すべて Other
information の次要素として入る（本書の平坦化 DOM 参照）。要素は次々とスロットに
追加されるので、スロットされていない両方の情報が一緒に既定スロットに入る。

Menu example
----------------------------------------------------------------------

本章冒頭の ``<custom-menu>`` を考える。スロットを使って、要素を分散させることが
できる。``<custom-menu>`` を次のように定義する：

.. code:: html

   <custom-menu>
     <span slot="title">Candy menu</span>
     <li slot="item">Lollipop</li>
     <li slot="item">Fruit Toast</li>
     <li slot="item">Cup Cake</li>
   </custom-menu>

これに対応する、適切なスロットを持つ shadow DOM テンプレートをこうする：

.. code:: html

   <template id="tmpl">
     <style> /* menu styles */ </style>
     <div class="menu">
       <slot name="title"></slot>
       <ul><slot name="item"></slot></ul>
     </div>
   </template>

1. ``<span slot="title">`` は ``<slot name="title">`` に入る。
2. ``<li slot="item">`` が複数あるが、``<slot name="item">`` は一つしかない。そ
   のような ``<li slot="item">`` はすべて ``<slot name="item">`` に次々と追加さ
   れ、リストを形成する。

本書の平坦化 DOM の模式図を参照。有効な DOM において、``<li>`` は ``<ul>`` の直
接の子でなければならない。しかし、これは平坦化 DOM であり、コンポーネントがどの
ように描画されるかを記述するもので、ここではそのようなことは自然に起こる。

あとは、リストを開閉するためのクリックハンドラーを追加して ``<custom-menu>`` が
完成する（本書で実装例を示している）。イベントやメソッドなど、より多くの機能を追
加することも可能だ。

Updating slots
----------------------------------------------------------------------

外側のコードでメニュー項目を動的に追加削除したければどうするだろうか。ブラウザー
はスロットを監視し、スロットの要素が追加削除された場合に描画を更新する。ま
た、light DOM ノードはコピーされず、スロットに描画されるだけなので、その内部の変
更はすぐに顕在化する。

そのため、描画を更新するために何かする必要はない。しかし、コンポーネントコードが
スロットの変更について知りたい場合は、イベント ``slotchange`` を利用できる。

本書では、メニュー項目を一秒後に動的に挿入し、タイトルを二秒後に変更するコードを
示している。ここでイベント ``slotchange`` が二つある。

1. 初期化時

   light DOM から ``slot="title"`` が対応するスロットに入ったときにすぐに引き起
   こされる。

2. 一秒後

   新しい ``<li slot="item">`` が追加されたときに引き起こされる。

なお、二秒後 ``slot="title"`` の内容が変更されるが、イベント ``slotchange`` は発
射しない。スロットが変更されないから。スロットされた要素内の中身を変更するのだ
が、別のことだ。

JavaScript から light DOM の内部変更を追跡したい場合、より汎用的な
``MutationObserver`` の仕組みを利用することもできる。

Slot API
----------------------------------------------------------------------

前に見たように、JavaScript は平坦化せずに実際の DOM を見る。しかし、shadow tree
が ``{mode: 'open'}`` を持っていれば、どの要素がスロットに割り当てられているか、
逆に、その中の要素によってスロットを把握することができるのだ。

* ``slot.assignedNodes({flatten: true/false})``: スロットに割り当てられた DOM
  ノードを返す。オプション ``flatten`` は ``false`` が既定値だ。明示的に
  ``true`` に設定すると、平坦化 DOM をより深く調べ、入れ子コンポーネントの場合は
  入れ子スロットを返し、ノードが割り当てられていない場合はフォールバック用の値を
  返す。
* ``slot.assignedElements({flatten: true/false})``: スロットに割り当てられた DOM
   要素。ただし要素ノード限定。

これらのメソッドは、スロットされた中身を表示するだけでなく、JavaScript で
それを追跡する必要がある場合に便利だ。例えば ``<custom-menu>`` コンポーネントが
何を表示しているかを知りたい場合、イベント ``slotchange`` を追跡し、
``slot.assignedElements()`` から項目を得られる。

Shadow DOM styling
======================================================================

<https://javascript.info/shadow-dom-style> ノート。

Shadow DOM は ``<style>`` タグと ``<link rel="stylesheet" href="...">`` タグの両
方を含んでも構わない。後者の場合、スタイルシートが HTTP キャッシュされるので、同
じテンプレートを使用するコンポーネントのためにまたぞろダウンロードされることはな
い。

一般的な規則として、ローカルスタイルは shadow tree 内部でのみ機能し、ドキュメン
トスタイルはその外部で機能する。しかし、例外がいくつかある。

:host
----------------------------------------------------------------------

セレクター ``:host`` は shadow host すなわち shadow tree を含む要素を選択するも
のだ。

例えば、``<custom-dialog>`` 要素を中央揃えで作成したいとする。そのためには、
``<custom-dialog>`` 要素自体にスタイルを設定する必要がある。

.. admonition:: 学習者ノート

   本書のコードを観察すると、 ``<template>`` で ``:host`` スタイルを
   中央揃えとなるように設定していることがわかる。

Cascading
----------------------------------------------------------------------

Shadow host（ここでは ``<custom-dialog>`` 自体が相当する）は light DOM に存在す
るため、ドキュメントの CSS 規則の影響を受ける。ローカルに ``:host`` でスタイル付
けされたプロパティーと、ドキュメントでスタイル付けされたプロパティーがある場合、
後者が優先される。

これはたいへん便利で、その ``:host`` 規則で既定のコンポーネントスタイルを設定
し、ドキュメントでそれを容易に上書きできる。例外は、ローカルプロパティーが
``!important`` とラベル付けされている場合だ。このようなプロパティーではローカル
スタイルが優先される。

:host(selector)
----------------------------------------------------------------------

``:host(selector)`` は ``:host`` と同じだが、与えられたセレクター ``selector``
にshadow host がマッチする場合にしか適用されない。

例えば、``<custom-dialog>`` が属性 ``centered`` を持っている場合にのみ、中央寄せ
にしたい場合は次でいい：

.. code:: html
   :force:

   <template id="tmpl">
     <style>
       :host([centered]) {
         position: fixed;
         left: 50%;
         top: 50%;
         transform: translate(-50%, -50%);
         border-color: blue;
       }

       :host {
         display: inline-block;
         border: 1px solid red;
         padding: 10px;
       }
     </style>
     <slot></slot>
   </template>

   ...

   <script>
   customElements.define(...);
   </script>

   <custom-dialog centered>
     Centered!
   </custom-dialog>

   <custom-dialog>
     Not centered.
   </custom-dialog>

これで、中央寄せ用スタイルが最初のダイアログ ``<custom-dialog centered>`` にのみ
適用されるようになる。

セレクターの ``:host`` 一族を利用して、コンポーネントの主要な要素にスタイルを設
定できる。これらのスタイルを、``!important`` でない限り、ドキュメントによって上
書きできる。

Styling slotted content
----------------------------------------------------------------------

スロットの状況を考えてみる。スロットされた要素は light DOM から来るので、ドキュ
メントスタイルを使用する。ローカルスタイルはスロットされた中身に影響しない。

本書の例では、スロット付き ``<span>`` はドキュメントスタイルに従って太字になり、
ローカルスタイルから ``background`` を得ることはない。結果は太字であって、赤には
ならない。

コンポーネント内のスロット要素にスタイルを設定したい場合、選択肢が二つある。
一つ目は、``<slot>`` 自身にスタイルを設定し、CSS の継承の仕組みに頼ることだ。こ
こでは ``<span>John Smith</span>`` が太字になるが、これは ``<slot>`` とその中身
の間で CSS の継承が有効であるからだ。しかし、CSS 自体では、プロパティーすべてが
継承されるわけではない。

.. code:: javascript

   this.shadowRoot.innerHTML = `
     <style>
     slot[name="username"] { font-weight: bold; }
     </style>
     Name: <slot name="username"></slot>
   `;

二つ目の選択肢は ``::slotted(selector)`` 疑似クラスを使うことだ。これは二つの条
件に基づいて要素をマッチングする。

1. それはスロットされた要素であり、light DOM から来たものであること。スロットの
   名前は問題にならない。ただ、どんなスロット付き要素であれ、その要素自身だけで
   あって、その子要素は含まれない。
2. その要素が ``selector`` にマッチする。

本書の例では ``::slotted(div)`` は ``<div slot="username">`` を厳密に選択するの
であって、その子要素は選択しない。

.. code:: javascript

   this.shadowRoot.innerHTML = `
     <style>
     ::slotted(div) { border: 1px solid red; }
     </style>
     Name: <slot name="username"></slot>
   `;

``::slotted`` はスロットの中にそれ以上降りることができない。そのようなセレクター
は無効となる。また、``::slotted`` は CSS でしか使えない。例えば
``querySelector()`` では使えない。

CSS hooks with custom properties
----------------------------------------------------------------------

メインドキュメントからコンポーネントの内部要素にスタイルを設定するにはどうすれば
よいだろう。 ``<custom-dialog>`` や ``<user-card>`` には ``:host`` などのセレク
ターが規則を適用するが、その内部の shadow DOM 要素にはどのようにスタイルを設定す
るのだろうか。ドキュメントから直接 shadow DOM スタイルに影響を与えられるセレク
ターはない。

しかし、コンポーネントと対話するためのメソッドを公開するのと同じように、スタイル
を設定するための CSS 変数を公開することは可能だ。

自作 CSS プロパティーは、light と shadow の両方のすべてのレベルに存在する。
たとえば、shadow DOM では ``--user-card-field-color`` CSS 変数を使用してフィール
ドのスタイルを設定でき、外側のドキュメントでその値を設定できる。そして、このプロ
パティーを ``<user-card>`` の外部文書で宣言すればよい。

自作 CSS プロパティーは shadow DOM を貫通し、どこでも見えるので、内側の
``.field`` 規則はそれを利用することになる。

.. code:: html

   <style>
     user-card {
       --user-card-field-color: green;
     }
   </style>

   <template id="tmpl">
     <style>
       .field {
         color: var(--user-card-field-color, black);
       }
     </style>
     <!-- slot を含む user-card 型の定義がここに来る -->
   </template>

   <script>
   customElements.define('user-card', class extends HTMLElement {
     connectedCallback() {
       // 自作要素をいつものように実装する
     }
   });
   </script>

   <user-card>
     <!-- span slot="X" 要素群からなる user-card データの定義がここに来る -->
   </user-card>

Shadow DOM and events
======================================================================

<https://javascript.info/shadow-dom-events> ノート。

Shadow tree の背後にある考え方とは、コンポーネントの内部実装の詳細をカプセル化す
ることだ。例えば、クリックイベントが ``<user-card>`` コンポーネントの shadow DOM
の内部で発生したとする。しかし、メインドキュメントのスクリプトは、特にコンポーネ
ントが第三者ライブラリーから来ている場合、 shadow DOM の内部について知るよしもな
い。

そこで、詳細をカプセル化しておくために、ブラウザーはイベントを標的し直す。
Shadow DOM で発生したイベントは、コンポーネントの外側で捕捉された場合、ホスト要
素を標的としている。

本書で示している簡単な例では、次のハンドラーをイベント源のタグ名をダイアログボッ
クスに表示するように定義している。

* ``customElements`` に対する ``this.shadowRoot.firstElementChild.onclick``
* ``document.onclick``

前者と後者をそれぞれ内部標的、外部標的と呼んでいるようだ。ボタンをクリックする
と、メッセージが次のように表示される：

1. 内部標的では ``BUTTON`` と出る。内部イベントハンドラーは、正しい標的である
   shadow DOM 内の要素を得る。
2. 外部標的では ``USER-CARD`` と出る。文書イベントハンドラーは、標的として
   shadow host を得る。

イベント再標的があることはたいへん素晴らしいことだ。外部ドキュメントがコンポーネ
ント内部について知る必要がない。イベントは、その観点からは ``<user-card>`` 上で
起こった。

Light DOM に物理的に存在するスロット要素においてイベントが起きた場合、再標的は発
生しない。

たとえば、本書の例でユーザーが ``<span slot="username">`` をクリックした場合、イ
ベントの対象は shadow ハンドラーと light ハンドラーの両方で、まさにこの ``span``
要素だ。

.. code:: html

   <user-card id="userCard">
     <span slot="username">John Smith</span>
   </user-card>

   <script>
   customElements.define('user-card', class extends HTMLElement {
     connectedCallback() {
       this.attachShadow({mode: 'open'});
       this.shadowRoot.innerHTML = `<div>
         <b>Name:</b> <slot name="username"></slot>
       </div>`;

       this.shadowRoot.firstElementChild.onclick = ...
     }
   });

   userCard.onclick = ...;
   </script>

John Smith をクリックすると、内側と外側の両方のハンドラーで、標的は
``<span slot="username">`` だ。これは light DOM の要素であることから再標的はない。

一方、クリックが shadow DOM に由来する要素、たとえば ``<b>Name</b>`` で発生した
場合、 shadow DOM から bubble out すると、その ``event.target`` は
``<user-card>`` にリセットされる。

Bubbling, event.composedPath()
----------------------------------------------------------------------

イベントバブリングの目的のために、平坦化 DOM が用いられる。つまり、スロット付き
の要素があり、その内部のどこかでイベントが起こると、``<slot>`` まで泡が浮き、さ
らに上へと泡が浮く。

オリジナルのイベント対象への完全パスを、すべての shadow 要素を含めて
``event.composedPath()`` で得られる。メソッド名が示すように、合成後にそのパスが
得られる。

前述の例の平坦化 DOM はこうなっている：

.. code:: html

   <user-card id="userCard">
     #shadow-root
     <div>
       <b>Name:</b>
       <slot name="username">
         <span slot="username">John Smith</span> <!-- ここをクリックする -->
       </slot>
     </div>
   </user-card>

``<span slot="username">`` をクリックすると、``event.composedPath()`` は配列

.. code:: javascript

   [span, slot, div, shadow-root, user-card, body, html, document, window]

を返す。これはまさに、合成後の平坦化 DOM における、対象要素を起点とする親子関係
に関する昇鎖だ。

----

Shadow tree の詳細は ``{mode: 'open'}`` である木に対してしか与えられない。 Shadow
tree が ``{mode: 'closed'}`` で生成された場合、構成パスはホスト ``user-card`` か
ら開始されて上がっていく。これは shadow DOM を扱う他のメソッドと同様の原則だ。閉
じた木の内部は完全に隠蔽されている。

event.composed
----------------------------------------------------------------------

イベントのほとんどが shadow DOM 境界を正常に通り抜けるが、そうでないイベントもわ
ずかに存在する。これは ``composed`` イベントオブジェクトプロパティーによって制御
される。これが ``true`` の場合、そのイベントは境界を通り抜ける。そうでない場合
は、shadow DOM の内部からしか捕捉できない。

仕様 UI Events を見てみると、イベントのほとんどが ``composed: true`` となってい
る。

タッチイベントとポインタイベントもすべて ``composed: true`` だが、
``composed: false`` であるイベントもある。

* ``mouseenter``, ``mouseleave``: 元々 bubble up をまったくしないイベントだ。
* ``load``, ``unload``, ``abort``, ``error``,
* ``select``,
* ``slotchange``.

これらのイベントは、イベント対象が存在する同じ DOM 内の要素上でしか捕捉すること
ができない。

Custom events
----------------------------------------------------------------------

自作イベントを dispatch する場合、``bubbles`` と ``composite`` の両方のプロパ
ティーを ``true`` にして、コンポーネントの bubble up と bubble out を行う必要が
ある。

たとえば、ここでは ``div#inner`` を ``div#outer`` の shadow DOM 内に作成し、それ
に対してイベントを二つ発射させている。``composed: true`` を指定したイベントだけ
が、ドキュメントの外に出て来る。

.. code:: javascript

   /*
   div(id=outer)
     #shadow-dom
       div(id=inner)
   */

   document.addEventListener('test', event => alert(event.detail));

   inner.dispatchEvent(new CustomEvent('test', {
     bubbles: true,
     composed: true,
     detail: "composed"
   }));

   inner.dispatchEvent(new CustomEvent('test', {
     bubbles: true,
     composed: false,
     detail: "not composed"
   }));
