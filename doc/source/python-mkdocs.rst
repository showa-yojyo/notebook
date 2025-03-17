======================================================================
MkDocs 利用ノート
======================================================================

.. |mkdocs| replace:: :program:`mkdocs`
.. |mkdocs.yml| replace:: :file:`mkdocs.yml`

.. contents:: 章見出し
   :local:

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
   the :file:`mkdocs.yml` configuration file, and then start the server by
   running the ``mkdocs serve`` command

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

プロジェクト構成
----------------------------------------------------------------------

MkDocs_ プロジェクトの構成手段は YAML ファイル |mkdocs.yml| を用いる。プロジェク
ト基点ディレクトリーにこのファイルを安置、プロジェクト構成を記述する。

プロジェクト情報
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

台割と配置
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

次の項目のうち、ファイルパターンを指定するものについては、その指定書式はファイル
:file:`.gitignore` での規則に従う。

``draft_docs``
   ``docs_dir`` に存在するファイルのうち、コマンド ``mkdocs serve`` で閲覧するが、
   コマンド ``mkdocs build`` ではそうしないものの集合を指定する。
``exclude_docs``
   論理的には ``docs_dir`` に存在するファイルの集合を値に取る。本来ならばビルド
   入力となるファイルを、ここに指定することで除外する。
``nav``
   サイト全体にわたるサイドバーの整形と台割を決定する項目だ。詳しく述べる。

   詳しく
``not_in_nav``
   サイトには含めたいが、サイドバーからは除外したいページがある場合、対応する入
   力ファイルを指示する。

   項目 ``exclude_docs`` で指示したファイルをこの項目で改めて指示する必要はない。
``validation``
   リンクを検証するときの |mkdocs| の診断メッセージの厳密度を指示する。この度合
   いはコマンド ``mkdocs build --strict`` で用いられる。

   このノードの有効構造は二通りあるが、面倒なので単純なほうの項目名を記す：

   ``absolute_links``
      上記 ``nav`` に指定されているある絶対パスが、外部パスを指している可能性ア
      リ。

      あるいは外部アドレスを指すリンクのうち、よく似たパスの入力ファイルがある。
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

   それぞれの値は ``warn``, ``info``, ``ignore`` のいずれか。

ビルド時に必要な情報
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs_dir``
   入力ディレクトリー。既定値 ``docs/`` を用いたいので指定しない。
``extra``
   その他の仕様。
``extra_css``
   追加的 CSS パスの配列。
``extra_javascript``
   追加的 JavaScript インクルード仕様の配列。
``extra_templates``
   詳細不明
``site_dir``
   出力ディレクトリー。既定値 ``site/`` を用いたいので指定しない。
``theme``
   テーマ仕様。

書式オプション
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``markdown_extensions``
   詳細不明
``plugins``
   プラグイン配列または辞書

使用方法・コツ
======================================================================

.. todo::

   * テーマ
   * 生編集サーバー
   * プラグイン
   * :file:`docs` 中の特別なファイル

     * :file:`images/favicon.ico`

   * :file:`site` 微調整

     * ``sitemap.xml``
     * ``mkdocs/search_index.json``
   * :file:`index.md` と :file:`README.md`
   * テンプレート

頻出コマンド
----------------------------------------------------------------------

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

テーマ
----------------------------------------------------------------------

内蔵テーマは二つだ。

* ``mkdocs``
* ``readthedocs``

サードパーティー製テーマは次で見つけろ：

* `MkDocs Themes <https://github.com/mkdocs/mkdocs/wiki/MkDocs-Themes>`__
* TBD

テーマによって機能が異なる。

構成は全テーマ共通のものとテーマ個別のものとに分かれる。テーマ ``mkdocs`` なら：

* ``color_mode: light|dark|auto``
* ``user_color_mode_toggle: ????``
* ``nav_style: primary|dark|light``
* ``highlightjs: True|False`` と highlight.js 関連構成項目
* ``shortcuts``: これは使いたい
* ``navigation_depth: 2``
* ``locale: en``: 英語のまま使いたい

テーマをカスタマイズする
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

カスタマイズ方法は CSS や JavaScript が必要な程度の微調整から、テンプレートの上
書きなどが必要な複雑なものまでにわたる。

前者は ``docs_dir`` を用いる。CSS と JavaScript は構成項目 ``extra_css`` と
``extra_javascript`` それぞれに追加的に指定が可能。ここにファイル名を指示する。
このような追加的ファイルは MkDocsが生成する HTML ファイルで、然るべき部分の後ろ
に追加される。

後者は ``custom_dir`` を用いる。既存のテーマを上書きすることになる。上書きする
ファイルをディレクトリーに格納し、それを :file:`mkdocs.yml` で指示するという方法
だ。

.. sourcecode:: yaml
   :caption: :file:`mkdocs.yml`
   :force:

   theme:
     name: mkdocs
     custom_dir: custom_theme/

基底テーマにないファイルを置いても無視されるわけではない。

テンプレートシステムは Jinja2 を採用している。

.. seealso::

   :doc:`/python-jinja2`

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

`highlight.js <https://highlightjs.org/>`__
   TBW

.. include:: /_include/python-refs-core.txt
.. _Jekyll: https://jekyllrb.com/
.. _MkDocs: https://www.mkdocs.org/
