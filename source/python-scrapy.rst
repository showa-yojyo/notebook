======================================================================
Scrapy 利用ノート
======================================================================

Scrapy_ の利用に関するいろいろなことを記す。

.. contents:: ノート目次

.. note::

   本稿執筆時の動作環境は次のとおり。

   .. code:: console

      bash$ scrapy version -v
      Scrapy       : 2.4.1
      lxml         : 4.6.2.0
      libxml2      : 2.9.10
      cssselect    : 1.1.0
      parsel       : 1.6.0
      w3lib        : 1.22.0
      Twisted      : 20.3.0
      Python       : 3.9.2 (default, Mar  3 2021, 20:02:32) - [GCC 7.3.0]
      pyOpenSSL    : 20.0.1 (OpenSSL 1.1.1j  16 Feb 2021)
      cryptography : 3.4.6
      Platform     : Linux-4.19.128-microsoft-standard-x86_64-with-glibc2.31

インストール
======================================================================

私の Python 環境は WSL2 上に Miniconda を用いた仮想環境だ。したがってインストール手段はほぼ自明なものになる。

Scrapy_ は Python のサードパーティー製パッケージであるので、
コンソールからの次のコマンド実行のどちらかでインストールしたと記憶している。

* ``conda install -c conda-forge scrapy``
* ``pip install scrapy``

チュートリアル
======================================================================

チュートリアルとしては、公式ドキュメントのチュートリアル Scrapy Tutorial を一通り実施するのが自然だ。
Scrapy_ はフレームワーク指向のパッケージなので、それを利用者に理解させることを優先した指導内容だ。
むしろシェルを先にいじるのがスクレイピングの本質に近いところから始めることになっていいと思うのだが、どうだろう。

Scrapy Tutorial を読み、それを実施したときの私の感想を羅列して示す。

概要
----------------------------------------------------------------------

このチュートリアルを簡単に説明すると、quotes.toscrape.com という有名な名言集のウェブサイトを scrape するというものだ。
Scrapy_ の標準的フレームワークに従うプロジェクトを作成し、コードを書き、テストし、データを集めるという構造のチュートリアルだ。
したがって、読了後は利用者は次のことを習得していることになる：

* プロジェクトの作成方法
* スパイダーの実装方法
* ウェブサイトを crawl してデータを収集する方法
* コンソールでかき集めたデータをエクスポートする方法
* リンクを再帰的にたどるようにスパイダーを変更する方法
* スパイダーに引数を扱わせる方法

プロジェクトを作成する
----------------------------------------------------------------------

Scrapy ではスパイダーというクラスを実装することでスクレイピングの一連の処理を表現するのだが、
その枠組に乗せるためにプロジェクトと呼ばれる定型的なファイルディレクトリー構造を作成する。
このためには次のコマンドを適当なディレクトリーからコンソールで実行する。

.. code:: console

   bash$ scrapy startproject PROJECT_NAME [PROJECT_DIR]
   bash$ cd PROJECT_DIR

チュートリアルでは ``PROJECT_NAME`` を ``tutorial`` と入力する。
``PROJECT_DIR`` は省略するとプロジェクト名がディレクトリー名として採用される。

コマンドが成功すると、ドキュメントにあるようなディレクトリー構造が生じる。
作業ディレクトリーをそこへ ``cd`` する。

スパイダーを実装する
----------------------------------------------------------------------

チュートリアルではファイル ``tutorial/spiders/quotes_spider.py`` を新しく編集するが、
次のように Scrapy のコマンドを利用したものを編集する習慣をつけるとよい：

.. code:: console

   bash$ scrapy genspider quotes quotes.toscrape.com
   bash$ mv quotes.py spiders

コードとドキュメントを読んで次のクラス構成要素を習得すること：

* ``name``: スパイダーの名前はコマンドラインツールやログを扱うときに重要だ。
* ``start_requests()``: このチュートリアルのように自分で実装する場合には
  ``Request`` オブジェクトを return するか yield するということを憶えておくこと。
* ``parse()``: 本来ならばデータを収集して処理するメソッドになる。

このようにして作成したスパイダーを実行するのに、Scrapy のコマンドラインツールを起動する：

.. code:: console

   bash$ scrapy crawl quotes

実行直後から Scrapy のフレームワークからのログが出力され続けるようならばひとまずよしとする。
Scrapy のスケジューラーが ``Request`` オブジェクトを適宜インターネットに飛ばして、得られた応答をもとに
``Response`` オブジェクトを生成して指定されたコールバック関数、
この場合には ``parse()`` をその引数として呼び出すというような仕組みだ。

もう一度書くと、スパイダークラスをテンプレートから生成すると ``start_requests()`` を書かずに済む。
代わりに、フレームワークがクラス属性 ``start_urls`` の URL を順次リクエストするので、
こちらのリストの中身を指定することになる。

ログインリクエストなど、特別な ``Request`` を要するときに ``start_requests()`` を書くと憶えておく。

データを収集する
----------------------------------------------------------------------

Scrapy Tutorial ではこのタイミングでシェルの説明が始まるが、別に分けるほうがいいと思う。
応答オブジェクトからメソッド呼び出しで DOM ノードを再帰的に参照できるという話をしたいだけだろう。

メソッド ``parse()`` に与えられた ``Response`` オブジェクトは、要求したページの DOM オブジェクトを含んでいると思って構わない。
このオブジェクトのメンバーデータ ``selector`` から次の問い合わせメソッドを好きに呼び出すことで欲しいデータを収集する：

* ``.css()``: CSS セレクター式を指定してマッチするノードを選択する
* ``.xpath()``: XPath 式を指定してマッチするノードを選択する

どちらの方式でも戻り値のオブジェクトは ``list`` の特別なサブクラスだ。
特に ``.get()`` や ``.getall()`` で文字列や文字列のリストが得られることを理解すること。

本チュートリアルでは ``parse()`` でページ内にあるデータから ``dict`` オブジェクトをいくつか構築して
``yield`` していることが確認できる。生成するオブジェクトの型については後で詳述がある。

ログを見ると、そのようにして生成した辞書オブジェクトがダンプされていることが確認できる。

データをエクスポートする
----------------------------------------------------------------------

コマンドラインからスパイダーを実行するときに、ふつうは出力先を指定する。
ファイルに出力する場合、Scrapy はその拡張子で出力フォーマットを決定する。

.. code:: console

   bash$ scrapy crawl quotes -O quotes.json
   bash$ scrapy crawl quotes -o quotes.jl
   bash$ scrapy crawl quotes -o quotes.csv
   bash$ scrapy crawl quotes -o quotes.xml

* オプション ``-o`` と ``-O`` の違いはヘルプを参照。
* JSON の巨大なファイルを処理したいのならば JQ_ などのツールを導入するといいらしい。

大規模なクローラーを実装するのであればアイテムパイプラインの導入を検討することとある。

リンクをたどる
----------------------------------------------------------------------

検索サイトやブログのように、ある程度の分量のページを crawl する方法について説明がある。
しかし、あとで ``Crawler`` を習得するのでここに書いてあることを習得する必要は実はない。

* スパイダーのメソッドから対象となるリンクを収集する。

  * 例えば ``response.css(...)`` などの選択メソッドで ``a`` 要素にマッチさせる。
    戻り値の ``href`` 値から ``yield response.follow(url, callback=self.parse)`` などのようにする。
  * URL が複数ある場合には一括して ``yield from response.follow_all(urls, callback=self.parse)`` とできる。

引数を扱う
----------------------------------------------------------------------

コマンドラインから ``-a`` オプションで引数をスパイダーに引き渡すことができる：

.. code:: console

   bash$ scrapy crawl quotes -a KEY1=VALUE1 -a KEY2=VALUE2 -a ...

スパイダー内部から参照するには方法が複数あるようだが、``self.KEY1`` などのようにするやり方もある。

* 安全のため ``getattr(self, KEY1)`` でチェックしてからアクセスするようにすること。
* このような引数はスーパークラスの ``__init__()`` が終了してから有効となる。

基本
======================================================================

ここからはドキュメントの BASIC CONCEPTS 内の節のうち、有用なものを拾って読んでいく。

コマンドラインツール
----------------------------------------------------------------------

構成ファイル ``scrapy.cfg`` と環境変数
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンドラインツール ``scrapy`` は構成ファイル ``scrapy.cfg`` が下記のパスにあるときにロードしに行く。

+ ``/etc/scrapy.cfg`` や ``c:\scrapy\scrapy.cfg``
+ ``~/.config/scrapy.cfg`` と ``~/.scrapy.cfg``
+ プロジェクトディレクトリのルートにある ``scrapy.cfg``

構成ファイルの書式はいわゆる INI ファイルのそれと同じようなものだ。

.. code:: ini

   [settings]
   default = myproject.settings

さらに、以下の環境変数を考慮する：

* ``SCRAPY_SETTINGS_MODULE``
* ``SCRAPY_PROJECT``
* ``SCRAPY_PYTHON_SHELL``

ツールコマンド一覧
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コンソールから ``scrapy COMMAND options args`` のようにして起動するコマンドの一覧。
プロジェクトが必要なものとそうでないものとに分類できる（ここには記さない）。

.. csv-table::
   :delim: @
   :header: command,description,comment

   bench@Run quick benchmark test@今は詳しく知らなくてよい
   check@Check spider contracts commands@自分の書いたスパイダーを調べる
   crawl@Run a spider@ スパイダーをふつうに実行
   edit@Edit spider@テキストエディターでモジュールを開く
   fetch@Fetch a URL using the Scrapy downloader@ふつうは応答の本体を見るがヘッダーを見ることもできる
   genspider@Generate new spider using pre-defined templates@テンプレートからモジュールを生成
   list@List available spiders@ここにスパイダークラスの ``name`` が現れる
   parse@Parse URL (using its spider) and print the results@``parse()`` 相当を指示できる
   runspider@Run a self-contained spider (without creating a project)@スパイダークラスを定義したモジュールだけで実行できる
   settings@Get settings values@構成ファイルで設定されている内容を確認する
   shell@Interactive scraping console@IPython があればそれが走る
   startproject@Create new project@フレームワークに乗るディレクトリー構造を生成する
   version@Print Scrapy version@付随するライブラリーのバージョンも出力できる
   view@Open URL in browser, as seen by Scrapy@

* ``scrapy crawl SPIDER`` がふつうの使い方だ。

  * ``SPIDER`` はプロジェクトにあるスパイダークラスの ``name``
    を指定する。これは ``list`` で確認することもできる。

* ``scrapy edit SPIDER`` は対応するファイルを既定のエディターで開くだけ。
  自分でエディターをコンソールから入力するのと手間はほとんど変わらないだろう。
* ``scrapy fetch --nolog --headers URL`` でヘッダーだけを得られる。
* ``scrapy genspider SPIDER_NAME ALLOWED_DOMAIN``
  の形式で実行するとスパイダークラスのための Python ファイルを生成する。

  * ``--list``, ``-l`` でスパイダーのテンプレの名前を一覧する。

    * ``basic``
    * ``crawl``
    * ``csvfeed``
    * ``xmlfeed``

  * ``--dump=TEMPLATE``, ``-d TEMPLATE`` でテンプレの定義を標準出力に表示できる。
  * ``--template=TEMPLATE``, ``-t TEMPLATE`` でスパイダークラスのテンプレを指定する。
  * ``--edit``, ``-e`` でファイル生成後にそれをエディターを開く。

* ``scrapy parse [options] <url>``
  はプロジェクトにあるスパイダーを使って文字列に関する分析をする。
  オプションを指定して特別なことをするのに利用する。

  * ``-a NAME=VALUE`` でスパイダーに引数を渡す。これは複数あってよい。
    コードではスパイダークラスのメソッドで ``self.NAME`` の形式で
    ``VALUE`` を参照する。
  * ``--output=FILE``, ``-o FILE``:
    スクレイプしたデータを出力するファイルを指定する。

    * これらは append モードで動く。
    * 標準出力は ``FILE`` として ``-`` を指定する。

  * ``--overwrite-output=FILE``, ``-O FILE``: 上記オプションの write 版。
  * ``--output-format=FORMAT``, ``-t FORMAT``: 出力書式を指定する。

    * ただし出力先が標準出力の場合には妙な例外が送出されてダメ。
    * 有効な FORMAT は後述。

  * ``--spider=SPIDER``: スパイダー ``SPIDER``
    を用いるようにする（クラスの定義から自動検出されるものではなく）。
  * ``--callback CALLBACK``, ``-c CALLBACK``: 応答を解釈するコールバックメソッドを指定する。
  * ``--nolinks`` で抽出したリンクを出力しないようにする。
  * ``--noitems`` で抽出したものを出力しないようにする。

* ``scrapy runspider myspider.py`` とすると、プロジェクトを作る必要がないスパイダーを実行できる。
* ``scrapy shell [URL|FILE]`` が基本形。

  * ``scrapy shell -c CODE`` でコードを実行。例えば：
    ``scrapy shell --nolog http://www.example.com/ -c '(response.status, response.url)'``

* ``scrapy startproject <project_name> [project_dir]`` を実行すると
  Scrapy_ が扱えるディレクトリー構造を生成する。
* ``scrapy view <url>`` でブラウザーが開くことになっている。

  * `WSL の Python だと動かない <https://github.com/scrapy/scrapy/issues/4589>`__。

スパイダー
----------------------------------------------------------------------

Scrapy ではスパイダーをクラスで表す。
特定のウェブサイトを這い回っていろいろなページから欲しいデータをかき集める方法を指定するものだ。

スパイダーには反復手順とでもいうようなものがあり、だいたい次のようになる：

1. 最初の URL を這いずり回るべく、リクエストを生成することから始める。
   そのリクエストからダウンロードされた応答を処理する関数を指定する。

   * これはメソッド ``start_requests()`` の呼び出しでなされる。
   * URL を ``start_urls`` に指定する。形式はテンプレコードを参照。

2. コールバック関数では応答すなわちウェブページを分析して、文字列分析したアイテムオブジェクトを返したり、
   ``Request`` オブジェクトを返したり、そういうオブジェクトの iterable
   を返したりする。 ここで返した ``Request``
   オブジェクトがまた（それらが指定する）コールバックに応答が到着する。

   コールバック関数ではふつうは ``Selector`` を利用してページの内容を分析する。
   それから加工したデータをアイテムとして ``yield`` する。

3. 最後に、スパイダーから返されるアイテムを、ふつうはデータベースに保存したり、ファイルに出力したりする。

私が Scrapy_ を使い始めた当初のハードルは上記の 1. と 2. だ。
リクエストと文字列処理の連携が非同期的だというのがわかっていなくて、MJ.NET
のページ遷移で失敗しまくっていた。

クラス ``Spider``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

クラス ``Spider`` がいちばん単純なスパイダーだ。 上述した ``start_urls`` と
``start_requests()`` の連携する既定の実装しか与えない。

主要なプロパティーを表にする：

.. csv-table::
   :delim: @
   :header: name, description, comment

   ``name``@スパイダーの名前@``genspider`` で決まる
   ``allowed_domains``@這いずり回ることを認めるドメイン@リストで指定
   ``start_urls``@這いずり回る URL の始点@リストで指定
   ``logger``@Python 標準のログ機能@``self.logger.info(...)`` のように使う

主要なメソッドを表にする：

.. csv-table::
   :delim: @
   :header: name, description, comment

   ``start_requests()``@ スパイダーが這い回るための ``Request`` の iterable を返す@ジェネレーターとして書くのが無難
   ``parse(response)``@応答を処理する既定のコールバック@応答を処理してデータか URL を返す

* ``start_urls`` を明示的に設定してある場合、``start_requests()``
  を実装せずに済ませることができる。 反対に、``start_requests()``
  を実装して ``start_urls`` を無視するということもできる。

スパイダーに引数を渡す
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コンソールからコマンド ``crawl`` や ``runspider``
を実行するときにオプション ``-a KEY=VALUE`` でスパイダーに引数を渡せる。

.. code:: console

   bash$ scrapy crawl MYSPIDER -a KEY1=VALUE1 -a KEY2=VALUE2 ...

* スパイダークラスで ``def __init__(self, KEY=None, *args, **kwargs)``
  のように書くか、
* メソッド内で ``self.KEY`` の形式で参照する。ただしコマンドラインで指定されていない場合には例外が送出する。

.. todo:: 次のオプションは別途処理される？

   * ``http_user``
   * ``http_pass``
   * ``user_agent``

一般的なスパイダー
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``CrawlSpider``:
  これがふつうのウェブサイドをクロールするのに用いられるスパイダー。

  * プロパティー ``rules`` に基づいてクロールするページが決まる。
    これは ``Rule`` オブジェクトのリスト。
  * メソッド ``parse_start_url()``
    をオーバーライドすることがあるかもしれない。

* ``XMLFeedSpider``:
  その名の示すとおりのものをクロールする。クロールというのか？

  * ``itertag`` を指定。その上でメソッド ``parse_note()``
    をオーバーライドする。
  * 引数 ``response`` の次の引数が XML のノードを表す。これは ``Item``
    オブジェクトを生成して返す。

* ``CSVFeedSpider``: 上記スパイダーの CSV 版。``delimiter``,
  ``quotechar``, ``headers`` などを指定。

  * メソッド ``parse_row()`` をオーバーライドする。引数 ``row``
    は辞書オブジェクト。

* ``SitemapSpider``: sitemap.xml や robots.txt
   をクロールするためのスパイダー。

重要なのはクラス ``CrawlSpider`` だ。

スパイダークラス ``CrawlSpider`` の仕組みを理解するのにクラス
``Rule`` を理解する。これはコンストラクターの引数リストから察せられるように、ページ内の
URL と処理規則とを結合する役を果たす。一部を示す。

.. csv-table::
   :delim: @
   :header: parameter, description, comment

   ``link_extractor``@クロール対象である URL を抽出する ``LinkExtractor`` オブジェクト@後述
   ``callback``@抽出されたリンクを処理する callable@そのような callable は ``Response`` オブジェクトを引数に取る
   ``cb_kwargs``@上記 callable のキーワード引数となる ``dict`` オブジェクト@
   ``follow``@抽出されたリンク先にジャンプするか否かを表す ``bool`` 値@
   ``process_links``@抽出されたリンクのリストをフィルターするための callable@
   ``process_request``@抽出された ``Request`` オブジェクトを処理する callable@これもフィルターのように実装する

セレクター
----------------------------------------------------------------------

セレクターの使い方
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``Response`` オブジェクトの ``.selector`` を経由してメソッド ``.css()``
や ``.xpath()`` で CSS セレクターや XPath を指定することでノードを得るというのが基本形となる。
これらを選択メソッドと呼ぶことにする。

``Response`` オブジェクトに対して同名の選択メソッドを呼び出すこともできる。
これらは本来のメソッドへの単なるショートカットだ。

``Selector`` オブジェクトを直接生成することもできる。セレクターの練習のときにそうするかもしれない。

* コンストラクターの引数は HTML テキストを表す ``str`` オブジェクトか
  ``HtmlResponse`` オブジェクトとなる。

選択メソッドの戻り値は ``SelectorList`` オブジェクトだ。
これに対する次の操作をしっかりと習得すること：

* ``.get()``
* ``.getall()``
* ``.attrib``

CSS セレクターには Scrapy_ による次の拡張仕様が付与されている。

* ``::text`` はテキストノードを選択する。
* ``::attr(name)`` は属性ノードを選択する。

選択メソッドの戻り値はセレクターのリストであるので、その要素に対しても選択メソッドを呼び出せることに注意すること。

要素ノードの属性を選択する手段が複数あることに注意すること。

メソッド ``.re()`` を利用することで ``Selector`` オブジェクトに対して正規表現でフィルターすることができる。
選択メソッドで抽出し切れないときにこれを併用するのだろう。

XPath の使い方
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Scrapy_ に限らず有用なので XPath の基本は別途学習しておくこと。
Scrapy_ をいじるついでに習得してもいい。注意点：

* 絶対パスと相対パスの区別に気をつける（ファイルパスのそれ以上に）。
* 場合によっては ``.css()`` を併用することになる。CSS
  クラスが複数ある要素ノードが絡むなど。
* これは Scrapy_ とは関係なく成り立つのだが、``//node[1]``
  と ``(//node)[1]`` は異なる。
* XPath 関数 ``text()`` を用いると選択メソッドに対する ``.getall()``
  の戻り値が ``str`` のリストになる。
* XPath 関数 ``string()`` を入れ子要素に対して使うと文字列解析が楽になる場合がある。
* XPath 関数 ``contains()`` も使いやすい。

XPath 式で変数を埋め込むことができる。次のコード片はドキュメントより引用した：

.. code:: python

   response.xpath('//div[@id=$val]/a/text()', val='images')
   response.xpath('//div[count(a)=$cnt]/@id', cnt=5)

RSS など、構文解析する対象によっては名前空間外しを必要とする。
アクティブなセレクターに対して ``.remove_namespaces()`` を呼び出してから
``.xpath()`` を呼ばないとまともに値を返さない。

その他発展的なトピックは省略。まずは基本を習得するのだ。

組み込みセレクター
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``Selector``: 応答の内容の特定の部分を選択するための機能

  * ``.attrib`` はノードの属性を表す ``dict`` オブジェクト。
  * ``.xpath()``, ``.css()`` は ``SelectorList`` を返す。
  * ``.get()`` はノードを ``str`` で返す。
  * ``.getall()`` はノードを ``str`` で表したものからなるリストを返す。
  * ``.re()`` は正規表現を適用して ``str`` のリストを返す。
  * ``.remove_namespaces()`` はあまり使いたくないが存在は憶えておくこと。

* ``SelectorList``: 組み込み ``list`` のサブクラスに ``Selector``
  で見てきたメソッドのほとんどを加えたもの

アイテム
----------------------------------------------------------------------

ウェブページにあるデータを構造化することがいちおうスクレイピングの目的だ。
Scrapy_ はクロール機能だけでなく、そのようなデータを取り扱うための機能も備えている。

* スパイダーは抽出データとして key-value の対を定義する Python
  オブジェクトを返して構わない。
* Scrapy_ はアイテムの種類を複数サポートする。処理コードを書くならどんなタイプのアイテムを使っても構わない。

Scrapy がサポートするアイテムの種類
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Python 組み込みの ``dict``
* Scrapy_ が提供するクラス ``Item``
* デコレーター ``dataclass`` に修飾されるクラス
* デコレーター ``attr.s`` に修飾されるクラス

  * サードパーティー製ライブラリー

アイテムオブジェクトを使う
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* クラス ``Item`` のサブクラスの定義方法を理解する
* クラス ``Field`` の性質を理解する
* アイテムオブジェクトの生成方法を習得する

  * ``namedtuple`` に似ている

* アイテムオブジェクトのフィールドを参照する方法を習得する

  * ``item.get(field_name)`` または ``item[field_name]``
  * ``in item`` と ``in item.fields`` の違いを理解する

* アイテムオブジェクトのフィールドに値を代入する方法を習得する

  * ここが ``dict`` との大きな違い

* ``Item`` のサブクラスをさらに派生させることもできる

アイテムについてはこのへんでいいと思う。

Scrapy シェル
----------------------------------------------------------------------

Scrapy シェルは UNIX や Python の IDLE のそれと同様に対話的シェルだ。
スパイダーを走らせることなくスクレイピングコードを素早く試すことができる。
このシェルはデータを抽出するコードをテストするのに使うことを目的としているが、ふつうの
Python シェルとしても利用できる。 XPath 式や CSS
セレクター式を対話的にテストするのに使うといい。

シェルを構成する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

私の環境ではコマンド ``scrapy shell`` で IPython が起動する。
この振る舞いは構成ファイル ``scrapy.cfg`` や環境変数
``SCRAPY_PYTHON_SHELL`` を設定することで変えられる。 とはいっても私は
IPython ユーザーであるので、以下、IPython
がインストールされていることを前提として記す。

シェルを走らせる
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド ``scrapy shell`` の引数に URL やローカルファイルパスを与えるのがふつうだ。
ただし、カレントディレクトリーにあるファイルを指定するときには ``./``
を明示しないと文字列は URL を表すものとして Scrapy に解釈されて失敗する。

.. code:: console

   bash$ scrapy shell https://www.example.com/
   bash$ scrapy shell ./path/to/file.html
   bash$ scrapy shell ../other/path/to/file.html
   bash$ scrapy shell /absolute/path/to/file.html
   bash$ scrapy shell file:///absolute/path/to/file.html

シェルを使う
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

常に利用可能な関数一覧：

.. csv-table::
   :delim: @
   :header: function, description, comment

   ``shelp()``@Scrapy 固有のシェル関数・変数を出力する@その他のオブジェクトも一覧に現れるようだ
   ``fetch(url[, redirect=True])``@新しい応答を取得して関連オブジェクトすべてを更新する@
   ``fetch(request)``@上記とだいたい同じ@こちらのほうが簡単
   ``view(response)``@応答をブラウザーで表示する@自動的に削除されない一時ファイルを生成する

常に利用可能なオブジェクト一覧：

.. csv-table::
   :delim: @
   :header: object, description, comment

   ``crawler``@現在の ``Crawler`` オブジェクト@未習
   ``spider``@与えた URL を処理することができる ``Spider`` オブジェクト@場合によっては ``None``
   ``request``@最後に取得したページの ``Request`` オブジェクト@``fetch()`` により更新
   ``response``@最後に取得したページを含む ``Response`` オブジェクト@
   ``settings``@現在の Scrapy 設定@``dict`` オブジェクト

セッションの例
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ドキュメントにある例を再現するなり、好きなページでアレンジして試すなりすること。

応答を検査するのにスパイダー内からシェルを起動する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

関数 ``scrapy.shell.inspect_response(response, spider)`` を ``parse()``
内から呼び出すなどする。 この機能を ``breakpoint()`` 感覚で利用する。

ただしこのセッションでは ``fetch()`` を利用してはならない。スパイダーが壊れる。

Feed exports
----------------------------------------------------------------------

サードパーティー製ライブラリーの導入など、特別なことをしなくてもエクスポートできるデータ形式：

* JSON
* JSON line
* CSV
* XML

コマンドラインで ``-o output.json`` だの ``-o output.jl``
だのと出力先をファイルで指定するとき、Scrapy はこの拡張子からデータ形式を決定する。

Scrapy がサポートする出力先はファイルだけではない。設定次第では FTP や
Google Cloud Storage なども使える。

エクスポートに使われる項目は次の通り。

.. csv-table::
   :delim: @
   :header: key, description, comment

   ``FEEDS``@ 設定全般を包含する ``dict`` オブジェクト @ 指定必須
   ``FEED_EXPORT_ENCODING`` @ エンコーディング @ 既定では UTF-8
   ``FEED_STORE_EMPTY`` @ 空のアイテムをエクスポートするかどうか @ 既定では ``False``
   ``FEED_EXPORT_FIELDS`` @ エクスポートしたいフィールドの ``list`` オブジェクト @ 指定なしの場合は存在するフィールドすべて
   ``FEED_EXPORT_INDENT`` @ 一階層あたりにのインデント量は空白文字いくつぶんか @ JSON や XML で意味がある
   ``FEED_STORAGES`` @ 追加的な格納先を指定する ``dict`` オブジェクト @ 説明略
   ``FEED_STORAGE_FTP_ACTIVE`` @（説明略）@ FTP など使わない
   ``FEED_STORAGE_S3_ACL`` @（説明略）@ S3 は知らない
   ``FEED_EXPORTERS`` @ 追加的なエクスポート器を指定する ``dict`` オブジェクト @ 使い途があるのか
   ``FEED_EXPORT_BATCH_ITEM_COUNT`` @ 出力先が複数ファイルにわたるときの、チャンクあたりのアイテム数 @ 値を指定するときに初めてそのように動作する

このトピックもあまり興味がないので深く立ち入らないで次に行く。

要求と応答
----------------------------------------------------------------------

クラス ``Request`` と ``Response`` を見ていく。このフレームワークでは重要な要素だ。
後者に対するメソッド呼び出しのほうが圧倒的に多い。

``Request`` のオブジェクトはスパイダー内部で ``yield`` されて Scrapy
のフレームワークがそれを実行する。そして ``Response``
オブジェクトをそのスパイダーに返すというような仕組みだ。

これらのサブクラスの特性を理解しておくことが重要だろう。

クラス ``Request``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コンストラクターの使い方を先に習得する。スパイダーの適当なメソッドから次のような感じで生成する：

.. code:: python

   Request(sample_url, callback=self.parse_sample)
   Request(sample_url, callback=self.parse_sample, cb_kwargs=dict(main_url=response.url)

このようなオブジェクトを ``return`` または ``yield`` すると、新たに
``Response`` オブジェクトを伴って指定したコールバックが呼び出される。

.. code:: python

   def parse_sample(self, response, main_url):
       # ...

クラス ``Request`` の主要フィールド一覧：

.. csv-table::
   :delim: @
   :header: name, description, comment

   ``url`` @ この要求のエスケープ済み URL を表す文字列 @ read-only
   ``method`` @ HTTP メソッドを表す文字列 @ 大文字
   ``headers`` @ HTTP ヘッダーを保持する辞書 @
   ``body`` @ HTTP ボデーそのもの ``bytes`` オブジェクト @ read-only

.. todo:: エラー処理

   エラー処理 (``errback``) については、自作するよりもフレームワークの既定の動作で当分は間に合う。
   ログ出力で十分わかりやすい。

メタ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

属性 ``Request.meta`` は辞書オブジェクトであってどんなデータでも入れておけるが、
Scrapy が特別扱いするキーもある。例えばキー ``download_timeout`` の値はダウンローダーが
タイムアウトまで待機する時間を秒単位で指定されているものとして参照される。
（この項目は設定の ``DOWNLOAD_TIMEOUT`` の影響も受ける）。

応答のダウンロードを中止する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

スパイダークラスで次のようにすると、与えられた応答のダウンロードを中止することができる。
つまり ``bytes_received`` シグナルのハンドラーを次のように書いて、そこで例外 ``StopDownload``
を送出する。

.. code:: python

   def on_bytes_received(self, data, request, spider):
       raise scrapy.exceptions.StopDownload(fail=False)

.. todo::

   ``fail=False`` の指定により、応答に元々の固有の ``errback``
   が呼び出されるのではなく、コールバックが呼び出されるようになる？

``Request`` のサブクラス
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``FormRequest``: 何かを POST するフォームの対応する ``Request``
   と考えてよい。
   例えば、よくあるログインページを通過するにはこれを利用することができる。

   .. code:: python

      def parse(self, response, **kwargs):
          if (uid := getattr(self, 'uid', None)) is None:
              raise KeyError('missing -a uid=your-user-name')
          if (password := getattr(self, 'password', None)) is None:
              raise KeyError('missing -a password=your-password')
          return FormRequest.from_response(
              response,
              formdata={'uid': uid, 'password': password},
              callback=self._after_login)

* ``JsonRequest``: JSON
   リクエストを処理できるクラス。コンストラクターの ``data`` に JSON
   シリアライズ可能なオブジェクトを渡せるということだ。

   .. code:: python

      payload = dict(name1=value1, name2=value2)
      yield JsonRequest(url, data=payload)

クラス ``Response``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

クラス ``Response`` はオブジェクトを直接生成するのではなく、
フレームワークから受け取るのが基本的だ。

主要フィールド：

.. csv-table::
   :delim: @
   :header: name, description, comment

   ``url`` @ 応答の URL を表す文字列 @ read-only
   ``status`` @ HTTP コードを表す数 @ 200 とか 404 とか
   ``headers`` @ HTTP ヘッダーを表す辞書風オブジェクト @ これに対して ``.get()`` や ``.getlist()`` などを呼び出すこともある
   ``body`` @ 応答ボデーを `bytes` で保持する @ read-only
   ``request`` @ `self` を生み出した `Request` オブジェクト @ ``self.request.url`` と ``self.url`` は一般には異なる

主要メソッド：

.. csv-table::
   :delim: @
   :header: name, description, comment

   ``follow(url, ...)`` @ URL への ``Request`` オブジェクトを返す @
   ``follow_all(urls, ...)`` @ 複数 URL それぞれへの ``Request`` オブジェクトを iterable にして返す @ ``Request`` への引数はすべて共通

``Response`` の派生クラス
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Scrapy による派生クラスを記す。
``Response`` については派生クラスを利用者が書くこともできる。

``TextResponse``: クラス ``Response`` にエンコーディングの考え方を導入したものと考えてよい。
したがって次の主要フィールドが有用だ：

.. csv-table::
   :delim: @
   :header: name, description, comment

   ``text`` @ 応答本体を ``str`` で表したもの @ すなわち ``self.body.decode(self.encoding)`` に等しい
   ``encoding`` @ 応答のエンコーディングを表す文字列 @ Scrapy が適宜解決、決定する
   ``selector`` @ 応答本文を対象とする ``Selector`` オブジェクト @ これにより ``self.text`` を解析する

主要メソッドは本質的には追加されていない。

* ``.css()`` や ``.xpath()`` は ``.selector`` の同名メソッドへのショートカットに過ぎない。
* ``.json()`` なるメソッドが提供されているらしいが、詳細不明。

``TextResponse`` にはさらにサブクラスがある。``HtmlResponse`` と ``XmlResponse`` だ。
しかし、これらに固有の性質、機能を利用者が用いることはほぼない。

リンク抽出器
----------------------------------------------------------------------

クラス ``LinkExtractor`` 周辺に関するあれこれを記す。

* ``scrapy.linkextractors.lxmlhtml.LxmlLinkExtractor``
  が真のクラス名だが、
  ``from scrapy.linkextractors import LinkExtractor`` で使える。
* チュートリアルでは crawler クラスの ``rules`` に組み込んでいるが、
  ``Reponse`` オブジェクトさえ手許にあればこれ単体で利用できる。
* コンストラクターとメソッド ``.extract_links()``
  だけ理解すれば十分だ。
* コンストラクター

  * 引数のすべてがキーワード引数。デフォルトでもまともに機能する。
    その場合はページ中にある ``<a>``, ``<area>``
    の集合を抽出するように振る舞うようだ。 引数 ``allow``, ``deny``
    を必要に応じて指定すれば事足りそうだ。
  * 引数 ``restrict_xpaths``, ``restrict_css``
    を利用すれば、あるノード範囲にあるリンクを選択できるだろう。
  * 引数 ``restrict_text`` はリンクテキストを制限する。私の場合は
    ``"東風戦"`` と指定するのだろう。
  * 引数 ``tags`` を使うと ``a``
    以外にもリンクを拾える。すぐに思いつくのは ``img``
    だ。しかしこれには ``href`` はない。
  * そこで引数 ``attrs`` を指定すればいい。``attrs=('src',)``
    とすればいいだろう。

* メソッド ``.extract_links()``

  * ``Response`` オブジェクトを受け取り、``scrapy.link.Link``
    オブジェクトのリストを返す。 ここで、クラス ``Link``
    はドキュメント中のリンクを表す要素を表現するものだ。
    ドキュメントがないので IPython などでインターフェイスを調べる。

* クラス ``Link``

  * 基本的には構造体のようなものと思っていい。憶えておけばいいのは次のものだけ：

    * ``.url``: もちろんリンクの URL を表す文字列だ。コメントでは絶対
      URL だと言っている。
    * ``.text``:
      リンク要素の開始終了タグに囲まれているリンクテキスト文字列。
    * ``.fragment``: URL の ``&#x23;`` から後の文字列を保持する。

設定
----------------------------------------------------------------------

Scrapy の動作をカスタマイズするための設定方法について記す。

設定モジュールを指定する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

環境変数 ``SCRAPY_SETTINGS_MODULE`` に ``myproject.settings`` のような
Python モジュールのパス書式に従う文字列を指定すると、
どの設定を使うのかを Scrapy
に教えることができる。そして、この指定モジュールは Python
標準の検索パスに存在する必要がある。

設定を仕込む
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

色々な仕組みを使って設定を仕込むことができる。それぞれ異なる手続きをとる。
優先度の高い順に次のようになる：

1. コマンドラインオプション
2. スパイダー別の設定
3. プロジェクト設定モジュール
4. コマンド別の既定の設定
5. 既定のグローバル設定

コマンドラインオプションが最も優先度が高い。その他の手段による設定内容を上書きする。
これには ``-s KEY=VALUE``, ``--set KEY=VALUE`` の書式により指定する。

スパイダー別の設定とは、次のように自作スパイダークラスのフィールドに
``custom_settings`` を辞書で与えることで指定するものをいう。

.. code:: python

   class MySpider(scrapy.Spider):
       name = 'myspider'

       custom_settings = {
           KEY: VALUE,
       }

プロジェクト設定モジュールとは、Scrapy プロジェクト内にあるモジュール
``settings.py`` を指す。 なければそれを作成して編集することができる。

前述の Scrapy ツールコマンドそれぞれには固有の既定の設定があり、グローバル設定を上書きする。
そのカスタムコマンドの設定をコマンドクラスの属性 ``default_settings``
に指定する。

グローバル既定設定はモジュール ``scrapy.settings.default_settings`` にある。

設定にアクセスする方法
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

スパイダークラス内からは ``self.settings`` を通じて設定を利用することができる。
これは ``__init__()`` が終了してから有効になることに注意すること。

組み込み設定項目
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

面白そうな項目をいくつかピックアップしておく。

* ``DOWNLOAD_DELAY``
* ``DOWNLOAD_MAXSIZE``
* ``LOG_ENABLED``, ``LOG_LEVEL`` などログ関連
* ``RANDOMIZE_DOWNLOAD_DELAY``
* ``USER_AGENT`` の既定値は Scrapy であることが明白な文字列だ。

応用
======================================================================

この水準に達したら記す。

単体のスクリプトとして実装する
----------------------------------------------------------------------

文書化されていないが、関数 ``scrapy.cmdline.execute()`` というのがある。
ここからコマンド ``scrapy runspider`` を実行するなどの方法が考えられる：

.. code:: python

   #!/usr/bin/env python

   import getpass
   import sys
   import scrapy
   import scrapy.cmdline
   # other import statements...

   class MySpider(scrapy.Spider):
       # definition of spider...

   if __name__ == '__main__':
       user_id = input('Enter your ID: ')
       password = getpass.getpass('Enter password: ')
       cmdline.execute(f"scrapy runspider {sys.argv[0]} -a uid={user_id} -a password={password}".split())

関連リンク
======================================================================

Scrapy_
  公式サイト。

.. _Scrapy: https://scrapy.org/
.. _JQ: https://stedolan.github.io/jq
