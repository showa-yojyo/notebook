======================================================================
MkDocs 利用ノート
======================================================================

.. |highlight.js| replace:: `highlight.js`_
.. |mkdocs| replace:: :program:`mkdocs`
.. |mkdocs.yml| replace:: :file:`mkdocs.yml`

.. contents:: 章見出し
   :local:

.. todo::

   * :file:`site` 微調整

     * ``sitemap.xml``
     * ``mkdocs/search_index.json``
   * :file:`index.md` と :file:`README.md`

概要
======================================================================

MkDocs_ による自己紹介：

   MkDocs is a **fast**, **simple** and **downright gorgeous** static site
   generator that's geared towards building project documentation. Documentation
   source files are written in Markdown, and configured with a single YAML
   configuration file.

原稿が Markdown 書式で記述され、文書構築構成を YAML ファイルで行うという様式は
Jekyll_ と同じだが、MkDocs_ は Ruby ではなく Python で実装されている。コマンド実
行で HTTP サーバーが走り出し、HTML ファイルを供給するようになるという動作も共通
している：

   MkDocs comes with a built-in dev-server that lets you preview your
   documentation as you work on it. Make sure you're in the same directory as
   the |mkdocs.yml| configuration file, and then start the server by running the
   ``mkdocs serve`` command

このコマンドで作動しているサーバーは自動リロードに対応している。構築構成、文書
ディレクトリー、テーマーディレクトリーに変更が生じた場合、生で再構築する。

.. seealso::

   :doc:`/python-sphinx`
      MkDocs_ とは異なり、Sphinx_ は Markdown ではなく reStructuredText を既定の
      原稿書式とする。また、HTTP サーバーを自前で持っていない。
   :doc:`/ruby-jekyll`
      MkDocs_ は、上述のように Jekyll_ とは共通点が多い。

インストール・更新・アンインストール
======================================================================

複数人で共用するプロジェクトの開発環境に |mkdocs| をインストールする事例では、そ
のプロジェクトの定める手順に従え。README や :file:`pyproject.toml` を読めば判明
する。

自分が所有する作業用仮想環境にインストールするならば、愛用している仮想環境ツール
がインストールコマンドを実装している場合にはそれを使え。私ならば Miniconda_ であ
るから、例えば次のようにする：

.. sourcecode:: console
   :caption: 現在の conda 仮想環境に |mkdocs| をインストールする
   :force:

   conda install -c conda-forge mkdocs

インストール手順の説明は以上だ。MkDocs_ の更新、アンインストールの手順は、対応す
る条件におけるインストール手順に合致する手順を選べ。例えば :program:`conda` を
使っているのならば ``conda uninstall mkdocs`` を走らせる。

.. seealso::

   :doc:`/python-miniconda`

構成・カスタマイズ
======================================================================

プログラムとしての |mkdocs| 自体を構成する手段（ドットファイルなど）はおそらくな
い。

MkDocs_ プロジェクトの構成手段は既定では YAML ファイル |mkdocs.yml| を用いる。プ
ロジェクト基点ディレクトリーにこのファイルを安置、プロジェクト構成を記述する。

プロジェクト情報
----------------------------------------------------------------------

``copyright``
   ページ下部に記入される copyright 文言を与える。
``repo_name``
   レポジトリーの名称。下記 ``repo_url`` が GitHub のそれである場合、この値は
   |mkdocs| が適切に割り当てるので、こちらは特に指定しない。
``repo_url``
   プロジェクトレポジトリーの URL を指定する。
``remote_branch``
   既定値である ``gh-pages`` をそのまま採用したいので、特に指定しない。
``remote_name``
   既定値 ``origin`` をそのまま採用するはずなので、特に指定しない。
``site_author``
   :samp:`<meta name="author" content="{site_author}">`
``site_description``
   :samp:`<meta name="description" content="{site_description}">` を生じる。
``site_name``
   トップページに関しては :samp:`<title>{site_name}</title>` を生じる。その他の
   ページもページ固有の表題に `site_name` の値が付加される。
``site_url``
   トップページに関しては :samp:`<link rel="cannonical" url="{site_url}">` を生
   じる。その他のページではこれに対応する ``link`` 要素の ``url`` 値は
   `site_url` の値から始まる。

台割と配置に関する構成項目
----------------------------------------------------------------------

次の項目のうち、ファイルパターンを指定するものについては、その指定書式はファイル
:file:`.gitignore` での規則に従う。

``draft_docs``
   ``docs_dir`` に存在するファイルのうち、コマンド ``mkdocs serve`` で閲覧するが、
   コマンド ``mkdocs build`` ではそうしないものの集合を指定する。
``exclude_docs``
   論理的には ``docs_dir`` に存在するファイルの集合を値に取る。本来ならばビルド
   入力となるファイルを、ここに指定することで除外する。
``nav``
   サイト全体にわたるサイドバーの整形と台割を決定する項目だ。リンクテキストと
   パスのペアの配列。
``not_in_nav``
   サイトには含めたいが、サイドバーからは除外したいページがある場合、対応する入
   力ファイルを指示する。

   項目 ``exclude_docs`` で指示したファイルをこの項目で改めて指示する必要はない。
``validation``
   リンクを検証するときの |mkdocs| の診断メッセージの厳密度を指示する。この度合
   いはコマンド ``mkdocs build --strict`` で用いられる。

   下位項目のそれぞれの値は ``warn``, ``info``, ``ignore`` のいずれか。

   このノードの有効構造は二通りあるが、面倒なので単純なほうの項目名を記す：

   ``absolute_links``
      上記 ``nav`` に指定されているある絶対パスが、外部パスを指している可能性ア
      リ。

      あるいは外部アドレスを指すリンクのうち、よく似たパスの入力ファイルがある。

      この項目だけは値 ``relative_to_docs`` を受け付ける。これを設定すると ``/``
      で始まる Markdown リンクはすべて ``docs_dir`` からの相対リンクとみなされる。
   ``anchors``
      アンカー指定を含むハイパーリンクが入力ファイルにあるが、そのリンク先ファイ
      ルは実際には当該アンカーを有していない。
   ``not_found``
      上記 ``nav`` に指定されている参照が、実際には入力に存在しないか、あるいは
      除外済みだ。
   ``omitted_files``
      サイト構築の入力ファイルのうち、``nav`` に現れないものがある。
   ``unrecognized_link``
      相対 URL としては解決不能なリンクがある。

ビルドに関する構成項目
----------------------------------------------------------------------

``docs_dir``
   入力ディレクトリー。既定値 ``docs`` を用いたいので指定しない。
``extra``
   任意の辞書を指定可能だ。カスタムテーマを採用する場合に、テーマから参照される
   定数をここに定義するという使用法がある。
``extra_css``
   追加的 CSS パスの配列。相対パスは ``docs_dir`` を基点として解決される。

   生成 HTML ファイルの内容としては ``head`` 要素内の ``link`` 要素として反映さ
   れる。
``extra_javascript``
   追加的 JavaScript ファイルの配列。配列の要素は JavaScript ファイルの URL また
   はインクルード仕様とする。後者の場合、MkDocs_ は次のキーを認識する：

   ``async``, ``defer``
      生成される ``script`` 要素の属性に対応。
   ``type``
      生成される ``script`` 要素の属性 ``type`` に対応。モジュールインポートを求
      める場合には値として文字列 ``module`` を指示しろ。
   ``path``
      生成される ``script`` 要素の属性 ``src`` に対応。

   生成 HTML ファイルの内容としては ``head`` 要素内の ``script`` 要素として反映
   される。
``extra_templates``
   使用者独自の Jinja2_ テンプレートファイルの配列か。実体は ``docs_dir`` 以下に
   あることを想定していると公式文書から読める。

   指定方式は ``extra_css`` などと同様。
``site_dir``
   出力ディレクトリー。既定値 ``site`` を用いたいので指定しない。
``theme``
   テーマ仕様。値はテーマ名を示す文字列または辞書だ。テーマ名の場合は内蔵テーマ
   名かインストール済みのテーマ名である必要がある。辞書の場合、下記のキーが有効
   だ：

   ``custom_dir``
      カスタムテーマを含むディレクトリー。やらないと思うが絶対パス指定が可能であ
      り、その場合はローカルファイルシステムのルートからのパスと解釈される。
   ``locale``
      サイト全体の言語テーマを構築するのに用いる言語地域を ISO 639-1 言語コード
      で指示する。無効値や未実装値を指定すると既定の言語地域が設定されたものとし
      て処理される。

      検索プラグインを機能させる場合、そこで言語を明示的に設定しない場合にこの値
      が参照される。
   ``name``
      テーマ名。
   ``static_templates``
      静的ページとして扱う雛形の配列。各要素はテーマのテンプレートディレクトリー
      か、テーマを構成する ``custom_dir`` に配置するものとする。

   その他はテーマ固有のキーだ。

生リロードに関する構成項目
----------------------------------------------------------------------

どうしても使いたいオプションは ``use_directory_urls: false`` だろう。

``dev_addr``
   コマンドラインオプション ``--dev-addr`` に対応。

   既定値 ``127.0.0.1:8000`` を用いたいので指定しない。
``strict``
   コマンドラインオプション ``--strict`` に対応。すなわち、警告の処理方法を指示
   する。警告が発生したときに処理を停止する場合には ``true`` とする。既定値は
   ``false``.
``use_directory_urls``
   このオプションは生成ファイルに対するディレクトリー構造をある程度制御する。

   値が ``false`` である場合、原稿ファイルに対応する名前の HTML ファイルを出力す
   る。値が ``true`` である場合、原稿ファイルに対応する名前のディレクトリーがま
   ず出力され、そこに :file:`index.html` が出力する。

   この値を ``false`` にしたい。明示的に指示する。
``watch``
   コマンド ``mkdocs serve`` を実行するときに更新をチェックする対象となるディレ
   クトリー群を追加的に指示可能。

   コマンドラインオプション ``-w``/``--watch`` に対応。ただし、パス形式は構成
   ファイルのあるディレクトリーからの相対パスに限定される。

拡張機能に関する構成項目
----------------------------------------------------------------------

当初は軽視していたが、重要であるかもしれない。

``hooks``
   配列型項目であり、プラグイン実体としてロードされる Python スクリプトのパスを
   要素とする。

   .. todo::

      何かを作って試す。

``markdown_extensions``
   配列型項目であり、Python Markdown に対する `Extensions
   <https://python-markdown.github.io/extensions/>`__ を指示する。リンク先の文書
   の表にある Entry Point 列の値を配列要素として取り得る。

   標準 Markdown 文法から逸脱した記法を導入しているので、GitHub リポジトリーのプ
   レビューなどでは拡張部のコードが露出することになる。

   ``admonition``
      reStructuredText と同様の囲み記事を実装。
   ``abbr``
      略語とその脚注を自動リンクさせる。入力 Markdown 内に次のパターンを挿れてお
      くと、本文に現れる `abbreviation` のすべてが出力 HTML ファイル内で
      :samp:`<abbr title="{phrase}">{abbreviation}</abbr>` タグで囲まれるという
      挙動だ：

      | :samp:`*[{abbreviation}]: {phrase}`
   ``codehilite``
      プログラミングコード関連。詳細不明。
   ``def_list``
      HTML の ``dl``, ``dt``, ``dd`` に相当。
   ``fenced_code``
      ブロックレベルのプログラミングコード。Markdown 標準のそれより機能が多い。
      詳細不明。
   ``footnotes``
      脚注を実装。本文に挿れたパターン :samp:`[^{anchor}]` が脚注を表すパターン
      :samp:`[^{anchor}]: {body}` に相互にハイパーリンクする。
   ``meta``
      いわゆる front matter を認識させる。しかしそのデータを出力 HTMLファイルで
      活用することはない。
   ``nl2br``
      Markdown での改行を HTML にも反映させるかどうかを決める。日本語文書を執筆
      する場合には無効にするのが自然だと考えられる。
   ``tables``
      Markdown 式でない罫線表を書くことができるようになる？
   ``toc``
      Sphinx の ``contents`` ディレクティブ相当。目次を表示させたい場所にマー
      カー ``[TOC]`` を挿れると、その下位の文書構造見出し列から目次を生成して置
      き換える。

      明示的に指定する可能性が高いオプション：

      ``marker``
         上記の ``[TOC]`` が既定値だが、変更したい場合にはここで上書きしろ。
      ``title``
         "Table of Contents" など、見出し一覧自体の見出し。全ページ共通？
      ``toc_depth``
         見出し一覧に採用する節の深さ。"2-6" のように指定することが可能。
``plugins``
   プラグイン配列または辞書。この構成を |mkdocs.yml| に書く場合、MkDocs 既定値は
   なかったことになり、プラグイン構成のすべてを自分で記す必要がある。

   既定値は ``search`` しか含まない配列だ。

   プラグインには独自のオプションキーがあるものの、どのプラグインにもオプション
   ``enabled`` がある。普通は環境変数を組み合わせて真偽を決める。

   .. admonition:: 利用者ノート

      おそらくだが、プラグイン固有のオプションは ``enabled`` が真である場合に限
      り |mkdocs| が解釈を試みる対象となる。

   ``search``
      検索エンジン LUNR_ を既定で採用している。このプラグインの構成もここで行
      う。

      ``lang``
         ISO 639-1 言語コードで識別される、索引を構築する際に使用する言語の配列。

         既定値は英語のみ (``[en]``) だが、テーマの ``locale`` が設定されていれ
         ばそちらが採用される。
      ``prebuild_index``
         この項目の存在は Node.js が動くサーバーを持っていなければ忘れていい。
      ``indexing``
         索引作成対象。索引が膨大な記憶的資源を占有するような文書に対して特に有
         効。値を ``full``, ``sections``, ``titles`` から選べ。この順に索引が大
         きい。
      ``min_search_length``
         検索文字列の最小長。既定では三文字より短いものは無視される。
      ``separator``
         索引を作成する際に用いられる単語の区切り文字を正規表現で指定する。

それ以外の構成関連機能
----------------------------------------------------------------------

ここに記す機能はすべて、実戦投入段階までは使わないと考えられる。

.. rubric:: 環境変数を参照する

次のパターンを値に含めると、この部分の値が環境変数 `env_var_name` の値に置き換わ
る：

| :samp:`!ENV {env_var_name}`

.. rubric:: 構成ファイルのあるディレクトリーを参照する

文字列 ``!relative`` はその構成ファイルのあるディレクトリーを指す。

* ``!relatve $config_dir`` は |mkdocs.yml| を含むディレクトリーパス。
* ``!relatve $docs_dir`` は項目 ``docs_dir`` のあるディレクトリーパス。

.. rubric:: 構成ファイルを継承する

構成ファイルを継承することが可能。項目名 ``INHERIT`` に値として親構成ファイルの
パスを指定する手段による。

コマンドライン
======================================================================

頻出コマンドを次に示す。

``mkdocs --version``
   バージョンだけでなく、|mkdocs| のパスと Python バージョンも出力する。
:samp:`mkdocs {command-name} --help`
   コマンド `command-name` のヘルプを出力する。
:samp:`mkdocs new --verbose {proj_dir}`
   ディレクトリー :file:`proj_dir` に MkDocs プロジェクトを新規作成する。既定の
   ディレクトリーを構成し、必要ファイルを生成する。
``mkdocs serve -o``
   HTTP サーバーを起動し、さらにプロジェクトのトップページをブラウザーで開く。
``mkdocs build``
   成果物をディレクトリー :file:`site` に出力する。出荷用。
``mkdocs gh-deploy``
   文書をビルドし、GitHub Pages に配備する。
:samp:`mkdocs gh-deploy --config-file {config} --remote-branch {branch}`
   GitHub Pages ではなく、個人または組織レポジトリーに文書を配備する場合のコマン
   ド例。作業ディレクトリーを MkDocs プロジェクト用のディレクトリーから個人また
   は組織レポジトリーのローカルコピーに :command:`cd` してから走らせる。

その他のコマンドについて簡単に記す。

``mkdocs get-deps -v``
   構成ファイルの内容から依存パッケージを特定し、PyPI からダウンロードする。手動
   で実行する場合にはオプション ``-v`` を使用すると進捗がわかりやすい。

テーマ
======================================================================

MkDocs_ におけるテーマという術語は、Sphinx_ や Jekyll_ におけるそれと同一と考え
る。ビルド文書の容貌に整合した調子を適用するための枠組だ。Mkdocs_ 内蔵テーマは次
の二つであり、それぞれを試してみると自作文書の見栄えがよその既存プロジェクトの
Web サイトにそっくりであることが確認できる：

* ``mkdocs``: MkDocs_, Hatch_ など
* ``readthedocs``

サードパーティー製テーマは `MkDocs Themes
<https://github.com/mkdocs/mkdocs/wiki/MkDocs-Themes>`__ で探すことが可能。適用
方法はそれぞれの仕様書に記載されている。一般的にはテーマにより機能が異なる。

テーマ構成のあり方
----------------------------------------------------------------------

テーマを構成する要素は全テーマで共通するものとテーマ個別のものとに分類して考えた
い。

MkDocs テーマ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

次に示すのは内蔵テーマの一つである ``mkdocs`` の固有構成要素だ：

``analytics``
   Google Analytics に関係する項目。使用しないので割愛。
``color_mode``
   ページ描画に関する明暗モード。値は ``auto``, ``dark``, ``light`` から指定す
   る。読者の利便性を第一に考えろ。
``highlightjs``
   既定値 ``True`` をそのまま採用したいので、明示的に上書きしないようにする。

   |highlight.js| を使用してのコードブロック内のプログラミングコードの強調描画を
   オンにする。
``hljs_style``
   |highlight.js| を用いる場合、その配色仕様を `Examples
   <https://highlightjs.org/examples>`__ で確認可能な名前で指定する。既定値は
   ``github`` だ。もう一つの有力な配色仕様は Visual Studio 系だろう。
``hljs_style_dark``
   ページ描画の明暗モードが ``dark`` のときに |highlight.js| が処理するコードブ
   ロックのテーマ。
``hljs_languages``
   |highlight.js| は特別に要求しないと強調表示を行えない言語がある。この構成項目
   はそのような言語を配列で指定する。
``nav_style``
   平たく言うとページ天井の背景色。値は ``primary``, ``dark``, ``light`` から指
   定する。

   この構成要素は ``color_mode`` とは独立している。したがって、この二つの値の組
   み合わせによっては天井の文字色と背景色の対比が低くなり、つまり可読性が低下す
   る。
``navigation_depth``
   サイドバーの木の深さ。既定値 2 より大きくしたい場合に明示的に設定する。
``shortcuts``
   ページ内でのキーバインドを定義可能。目玉機能だと感じる。コマンドは四つある：

   .. csv-table::
      :delim: @
      :header-rows: 1
      :widths: auto

      項目 @ コマンド動作 @ キーコード @ キー
      ``help`` @ キーバインドをポップアップ表示する @ 191 @ :kbd:`?`
      ``next`` @ 次のページを要求 @ 78 @ :kbd:`N`
      ``previous`` @ 前のページを要求する @ 80 @ :kbd:`P`
      ``search`` @ 検索ポップアップを表示する @ 83 @ :kbd:`S`

   キーを番号で指定する必要があることに注意。

   例えば Hatch_ の用例が素晴らしいので猿真似したい。
``user_color_mode_toggle``
   これを ``True`` にしておくと、上述した明暗モードを切り替える操作盤がページ内
   に出現する。

Read the Docs テーマ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

次に示すのは内蔵テーマの一つである ``readthedocs`` の固有構成要素だ。要素のいく
つかは ``mkdocs`` と共通する。

``analytics``
   先述のものと同じ。
``collapse_navigation``
   現在のページのサイドバーに当該ページ節の見出ししか含めないようにする。
``highlightjs``
   先述のものと同じ。
``hljs_languages``
   先述のものと同じ。
``include_homepage_in_sidebar``
   サイドバーメニューにホームページを表示するか否か。含めたくない場合に値
   ``False`` を指示する。
``locale``
   先述のものと同じ。
``logo``
   画像パスを設定することでプレーンテキストの ``site_name`` 文字列の代わりにロゴ
   タイプ画像を表示することが可能。指定しない場合は ``null`` とする。
``navigation_depth``
   先述のものと同じ。
``prev_next_buttons_location``
   ページ移動ボタンを ``bottom``, ``both``, ``none``, ``top`` のいずれかに指定す
   る。既定では ``bottom`` が設定される。
``sticky_navigation``
    ページをスクロールするとサイドバーがメインページの内容と共にスクロールさせた
    い場合に ``True`` を指示する。
``titles_only``
   サイドバーにページタイトルしか含めない場合には ``True`` を指示する。

.. admonition:: 利用者ノート

   サイドバーが仕様どおりに動作しない。

テーマをカスタマイズする
----------------------------------------------------------------------

カスタマイズ方法は CSS や JavaScript が必要な程度の微調整から、テンプレートの上
書きなどが必要な複雑なものまでにわたる。

前者は ``docs_dir`` を用いる。CSS と JavaScript は構成項目 ``extra_css`` と
``extra_javascript`` それぞれに追加的に指定が可能。ここにファイル名を指示する。
例えば Read the Docs テーマにおけるサイドバーの背景色を変えたい場合には、対応する
CSS クラスの背景色を指定したファイルを作ればよい。次のような内容の CSS ファイルを

.. sourcecode:: css
   :caption: 例えば :file:`docs/css/override.css` とする
   :force:

   div .wy-side-nav-search {
       background-color: deeppink;
   }

.. sourcecode:: yaml
   :caption: ``extra_css`` 指定例
   :force:

   extra_css:
     - css/override.css

後者は ``custom_dir`` を用いる。既存のテーマを上書きすることになる。上書きする
ファイルをこの構成項目ディレクトリーに格納し、それを |mkdocs.yml| で指示するとい
う方法だ。例えば、Favicon ファイルを自作のものに差し替える場合にはこちらの方式を
採る必要がある。

.. sourcecode:: yaml
   :caption: |mkdocs.yml| における ``custom_dir`` 指定例
   :force:

   theme:
     name: mkdocs
     custom_dir: custom_theme/

Favicon ファイルを自作のものに差し替えるにはファイル

| :file:`custom_theme/img/favicon.ico`

を作成すればよい。

オリジナルのファイル構成は Python インストールディレクトリーの
:file:`site-packages/mkdocs/themes/mkdocs` で確認可能。Jinja2_ 用テンプレートを
確認、複製するときもここから参照して、必要ならテンプレートファイルを
:file:`custom_dir/` の適切なサブディレクトリーに置き、Jinja2_ 方式で「オーバーラ
イド」することになる。Sphinx_ と考え方は同じだ。

.. seealso::
   Jinja2_ については :doc:`/python-jinja2` を見て思い出せ。

資料集
======================================================================

MkDocs_ は難しいツールではないので、機能を詳細に解説することを目的とする記事は多
くは存在しない。

MkDocs_
   公式文書。これだけを熟読することで習得は十分可能だ。
`MkDocs - Full Stack Python <https://www.fullstackpython.com/mkdocs.html>`__
   MkDocs_ をどう発音するのかがわかる。
`GETTING STARTED WITH MKDOCS: A BEGINNER'S GUIDE <https://medium.com/@TemitopeVictoria/getting-started-with-mkdocs-a-beginners-guide-e6dcdcc98493>`__
   入門記事。内容はバランス良くまとまっている。開発環境は Windows を想定。
`System Health Lab Mkdocs Tutorial and Template <https://tutorial-mkdocs.systemhealthlab.com/>`__
   入門記事。チュートリアルで構成。GitHub テンプレリポジトリーから作業を始める。
   この手の Markdown 仕様の解説は初めて見た。
`A beginner guide to using MKDocs <https://coreyodonis.hashnode.dev/a-beginner-guide-to-using-mkdocs>`__
   入門記事。プラグインに関する記述が少々ある。
`MKDocs: The Ideal Tool for Effective Documentation <https://medium.com/cranecloud/mkdocs-the-ideal-tool-for-effective-documentation-31da0666bb05>`__
   なぜ MkDocs_ が良いのかを説明している。
`Learn / MkDocs <https://learn.openwaterfoundation.org/owf-learn-mkdocs/>`__
   MkDocs_ 利用環境のセットアップと、利用に必要な情報や作業を順序立てて述べてい
   る。
`Read the Docs user documentation <https://docs.readthedocs.com/platform/stable/>`__
   Read the Docs は Git ワークフローを使用して文書をここに配備する。最新の原稿
   ファイルを GitHub に push すると文書を更新作成する。
|highlight.js|
   構文強調スクリプト。対応言語数が二百近くあり、テーマが豊富。
LUNR_
   既定の検索エンジンは JavaScript で実装されている。

.. include:: /_include/python-refs-core.txt
.. _Hatch: https://hatch.pypa.io/
.. _`highlight.js`: https://highlightjs.org/
.. _Jekyll: https://jekyllrb.com/
.. _Jinja2: http://jinja.pocoo.org/
.. _LUNR: https://lunrjs.com/
.. _MkDocs: https://www.mkdocs.org/
