======================================================================
Sphinx 利用ノート
======================================================================

本稿は当読書ノートの基盤となる Python パッケージである Sphinx_ の利用に関するノー
トだ。

   Sphinx is a *documentation generator* or a tool that translates a set of
   plain text source files into various output formats, automatically producing
   cross-references, indices, etc. That is, if you have a directory containing a
   bunch of reStructuredText or Markdown documents, Sphinx can generate a series
   of HTML files, a PDF file (via LaTeX), man pages and much more.

.. contents::
   :depth: 3
   :local:

インストール
======================================================================

グローバルにインストールする場合と、プロジェクトの仮想環境にインストールする場合
がある。両方説明する。更新手段は採用するパッケージマネジャーに従う。

グローバルの Python 環境はま共にあるものとする。

グローバルにインストールする
----------------------------------------------------------------------

いつもの Miniconda を使う。インストール成功の確認は :program:`sphinx-build` など
の CLI のバージョンを出力する。

.. sourcecode:: console
   :caption: :program:`conda` を使って Sphinx をインストールする例

   $ conda install -n DEFAULT_ENVNAME sphinx
   （略）
   $ sphinx-build --version
   sphinx-build 8.1.2

プロジェクト個別にインストールする
----------------------------------------------------------------------

プロジェクトディレクトリーに移動して仮想環境を作成したら直ちにインストールすると
いう想定で：

.. sourcecode:: console
   :caption: :program:`pipenv` を使って Sphinx をインストールする例

   $ cd $PROJECT_DIR
   $ pipenv install sphinx
   （略）
   $ pipenv run sphinx-build --version
   sphinx-build 8.1.2

原稿ディレクトリーを初期化する
======================================================================

.. note::

   以下、コマンドラインは Pipenv で用意した仮想環境で実行することを前提とする。

将来的に生成した HTML ファイル群を GitHub に配備するので、プロジェクトディレクト
リーのルートにサブディレクトリー :file:`docs` を作成し、そこを Sphinx 用作業場と
する：

.. sourcecode:: console
   :caption: :program:`sphinx-quickstart` 実行例

   $ cd $PROJECT_DIR
   $ mkdir docs
   $ pipenv run sphinx-quickstart
   （略）

:program:`sphinx-quickstart` 成功後、生成されたファイルを確認すること。

.. admonition:: 読者ノート

   :program:`sphinx-quickstart` は引数なしで実行すると対話的操作によりファイルを
   生成する。ヘルプにあるオプションを十分に指定すれば、ファイルを一気に生成する。

次にやる作業が何になるかは場合による：

* ビルド構成を変える
* 原稿を執筆する
* テーマをいじる
* 拡張を導入する

初期設定
======================================================================

以下の説明では :program:`sphinx-quickstart` の入力は次を仮定する：

.. sourcecode:: console
   :caption: 説明用 :program:`sphinx-quickstart` 入力例

   $ sphinx-quickstart --sep \
       --project 読者ノート \
       --author プレハブ小屋 \
       --release '1.0' \
       --language en \
       --ext-todo \
       --ext-mathjax \
       --ext-githubpages \
       --makefile \
       --no-batchfile

これらの内容は :file:`source/conf.py` に反映される。以降、この構成ファイルを次の
目的で手動で編集する：

* Sphinx 構成項目を調整する
* Sphinx 拡張を増減する
* Sphinx 拡張の構成項目を調整する

ビルド
======================================================================

:file:`Makefile` のあるディレクトリーに移動して：

.. sourcecode:: console
   :caption: Pipenv 仮想環境での :program:`make` 実行例

   $ pipenv run make html

成果物はサブディレクトリー :file:`build/html` 以下の内容すべてだ。

GitHub Pages
======================================================================

GitHub のリポジトリーに Sphinx 用原稿を格納する場合、GitHub Actions の力で push
イベントで次のことを実現したいと考えるのが自然だ：

* 最新の原稿をビルドして HTML ファイルを生成し、
* それを GitHub Pages に公開する。

そのためのワークフロー YAML の記述方法は `Appendix: Deploying a Sphinx project
online <https://www.sphinx-doc.org/en/master/tutorial/deploying.html>`__ にあ
る。まとめておくと：

* リポジトリーの :menuselection:`Settings-->Pages` ページで各種項目を設定する：

  * Publish を有効にする
  * :guilabel:`Source` を :guilabel:`Deploy from a branch` に設定にする
  * :guilabel:`Branch` を設定する：

    * 左ドロップダウンリストを :guilabel:`gh-pages` に設定
    * 右ドロップダウンリストを :file:`Makefile` のあるほうのディレクトリーに設定

* :file:`Makefile` のあるディレクトリーに :program:`pipenv` 用のファイル
  :file:`Pipfile` および :file:`Pipfile.lock` があることを確認する。必要に応じて
  前者に対してサードパーティー製パッケージのバージョン条件を明記する。例えば：

  .. parsed-literal::

     Sphinx >= 7.0
     ipython >= 8.0
     sphinxcontrib-mermaid

* リポジトリーにワークフローファイルを置く。例えば
  :file:`.github/workflows/sphinx.yml` とし、本文の内容にする。

  .. admonition:: 読者ノート

     ステップ Upload artifacts では大容量サイズのファイルを生成することになる。
     開発ブランチのビルドアクションでは行わず、リリースブランチだけで行うように
     書き換えるのが望ましい。

GitHub Actions がわからない場合や、ビルド時間が上限を超えるまでに文書が肥大化し
た場合は、ローカルで Sphinx ビルドをし、得られる生成ファイルを ``gh-pages`` ブラ
ンチに対して ``git push`` することになるだろう。

reStructuredText
======================================================================

ブラウザーに URL <https://www.sphinx-doc.org/en/master/usage/restructuredtext/>
をブックマークしておく。Markdown に較べるとマークアップが複雑なので覚え切れな
い。

reStructuredText の基本
----------------------------------------------------------------------

基本はさすがに丸暗記するほうが効率的だ。

* パラグラフは空行と空行の間のテキストの塊が相当する。
* インラインマークアップ三種類

  * 斜体は米印で囲む。
  * 太字はダブル米印で囲む。
  * コード片はダブルバッククオートで囲む。この三種の中でもっともよく使う。

* リストは行の先頭に米印を付け、空白を挿れ、テキストを配置したものを縦に並べる。

  * 米印の代わりに ``#.`` を使うと番号リストになる。
  * リストを入れ子にするときには、空行を挟む。ここは Markdown と異なる。

* HTML で言う ``<dl>``, ``<dt>``, ``<dd>`` を reST で実現可能。Markdown に優る。
* 引用パラグラフは二種類ある。

  * 周囲のパラグラフに対してインデントしたパラグラフは引用パラグラフとなる。
    当ノートではボックス枠左をピンクで塗る。なるべくこちらを使いたい。
  * 行頭に ``|`` を付けた引用は改行文字を維持する。

* 当ノートでは ``::`` によるリテラルブロックを書かない。
* 表はなるべく ``csv-table`` を用いたい。
* ハイパーリンクのマークアップはよく忘れる。
* 節（セクション）で使う飾り文字は既存の原稿に準拠する。
* 画像は ``.. image::`` 指令を使う。

  * オプションが重要。VS Code の reST モードに補完 snippets を仕込むといい。
  * SVG ファイルを表示する場合にはこれではなく、HTML の ``<object>`` タグを使い
    たい。方法は Inkscape 利用ノートの原稿を参照。

* 置換はほとんど使わない。書くのが面倒だ。
* コメントアウトは覚えておくと便利。

役目
----------------------------------------------------------------------

相互参照
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``:doc:``
   頻出。ページパスを指定してリンクする。リンクテキストを指定することもある。
``:ref:``
   たまに用いる。アンカー :samp:`.. _{anchor-name}:` を手動で定義する必要があ
   る。これが面倒で多用しない。
``:envvar:``
   環境変数をマークアップするのに使いたくなるが、本来はインデックスが生成される。
``:option:``
   コマンドオプションをマークアップするためのものだ。対になる指令
   ``.. option::`` がある。
``:term:``
   本来は術語集指令 ``.. glossary::`` と対で用いるマークアップだ。

コードと数式
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``:code:``
   使わない。ダブルバッククオートで事足りる。
``:math:``
   LaTeX コードをマークアップする。別途 MathJax に数式を描画させるように仕込む。

語義に関するもの
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``:abbr:``
   頻繁に使うはずなのだが、健忘症かと思うくらいに忘れる。そもそも面倒。自分用の
   備忘録に :abbr:`HTML (HyperText Markup Language)` などといちいちタイプしない
   ほうが自然だろう。
``:command:``
   Sphinx 公式によると、OS 水準のコマンドをマークアップするのに使うとのこと。
   cf. ``:program:``.
``:dfn:``
   術語を、その定義時にマークアップする。ダブル米印でマークアップしたいときに思
   い出すべき役目。
``:file:``
   ファイルもしくはディレクトリーパスをマークアップする。中括弧で括られた部分文
   字列は可変であることを示すそうだ。私はこれまで大文字でごまかしていた。
``:guilabel:``
   ツール利用ノートで ``:menuselection:`` と共に頻繁に使う。
``:kbd:``
   キーボードのキーを示すのに用いる。例：
   :kbd:`Home`
   :kbd:`C-x C-f`
   :kbd:`Control-x Control-f`
``:menuselection:``
   ツール利用ノートで ``:guilabel:`` と共に頻繁に使う。タイプするのが面倒なので
   VS Code キーバインドを両者それぞれに設定するといい。
``:program:``
   ``:command:`` の実行形式版として使うという認識でいい。
``:regexp:``
   この役目は何かクセがあったと記憶している。

指令
----------------------------------------------------------------------

Sphinx に搭載されている指令のうち、本ノートで用いるものを記す。

``.. toctree::``
   インデックス系のページで利用。オプションが重要で、VS Code の reST モードにお
   ける補完 snippets を用意することが望ましい。

   * ``:caption:`` を付けるほうが価値が高くならないか一考すること。
   * ``:maxdepth:`` を大きくしないこと。

``.. seealso::``
   関連文書を列挙するのに利用。
:samp:`.. rubric:: {title}`
   便利である可能性が高い。見出しリンクの要らない見出し。
:samp:`.. sourcecode:: {[language]}`
   複数行プログラムコードを示すのに利用。オプション ``:caption:`` をなるべく添え
   ろ。
:samp:`.. literalinclude:: {filename}`
   テキストファイルの中身を reST 原稿内に丸々写す。有用なオプションがある。
``.. glossary::``
   術語集を構成する。``:term:`` と共に用いるはずだ。
``.. math::``
   LaTeX コードを記すことで、MathJax に数式を描画させる。オプション ``:nowrap:``
   を常時指定したい。

ビルド構成
======================================================================

構成ファイル :file:`conf.py` で指定したい項目と目的を述べる。

.. note::

   * :file:`conf.py` の他に :file:`docutils.conf` も使える。
   * ``rst_epilog``, ``rst_prolog`` は何かいい用途がありそうだ。

プロジェクト情報
----------------------------------------------------------------------

基本的には :program:`sphinx-quickstart` が生成した値を採用する。ただ一箇所、コ
ピーライト表示にビルド時の日付を反映させたいので改造する：

.. sourcecode:: python

   from datetime import date

   copyright = f'1999-{date.today().year}, {author}'

公式文書によると ``%Y`` でビルド時点での西暦に置換されるとあるが、されないようだ。
項目 ``version`` および ``release`` は手動で編集するのがいいだろう。

全般
----------------------------------------------------------------------

まず、Sphinx 拡張に手動追加するものがあるのでサブディレクトリーにパスを通す：

.. sourcecode:: python
   :caption: 拡張配置ディレクトリー指定準備コード例

   import sys
   import os

   # If extensions (or modules to document with autodoc) are in another directory,
   # add these directories to sys.path here. If the directory is relative to the
   # documentation root, use os.path.abspath to make it absolute, like shown here.
   sys.path.append(os.path.abspath('./_extension'))

当読者ノートにおける本稿執筆時点での拡張の編成は次のようなものだ：

.. sourcecode:: python
   :caption: ``extensions`` リストにモノを列挙する例

   extensions = [
       'disablesearchindex',
       'IPython.sphinxext.ipython_console_highlighting',
       'IPython.sphinxext.ipython_directive',
       'japanesesupport',
       'sphinx.ext.githubpages',
       'sphinx.ext.mathjax',
       'sphinx.ext.todo',
       'sphinxcontrib.mermaid',]

拡張それぞれについての構成方法は後述する。

その他の項目は次のとおり：

``templates_path``
   リストに ``'_templates'`` を含ませる。

HTML 出力
----------------------------------------------------------------------

もっとも神経を使うのはこの構成区分の設定だ。以下、当ノートの用途を意識した値を述
べる。生成コード量を少なくしたいことと、ライブラリー文書を指向していないことによ
り、ここに挙げる設定が妥当だとみなしている。

``html_theme``
   HTML5 に対応しているテーマを指定するべきだ。既定値の ``alabaster`` はそれを満
   足する。
``html_theme_options``
   この辞書の値を Alabaster の文書を見ながら決めろ。設定値は後述する。
``html_js_files``
   自作 JavaScript ファイルをリストに列挙する。
``html_sidebars``
   テーマが Alabaster なので明示的に指定する必要がある。
   ``html_theme_options['nosidebar']`` を ``True`` にした場合にはテキトーでい
   い。
``html_use_index``
   ``False`` とする。
``html_copy_source``
   ``False`` とする。reST 原稿を配備したくない。
``html_show_sourcelink``
   配備しないものに Sphinx はリンクしないようだが、明示的に ``False`` とする。
``html_show_search_summary``
   ``False`` とする。ライブラリー文書でないので。
``html_show_sphinx``
   ``False`` とする。HTML コードを減らしたいので。

拡張別構成
----------------------------------------------------------------------

``sphinx.ext.mathjax``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``mathjax_path``
   ラッパースクリプトのファイル名を設定する。例えばそれが
   :file:`source/_static/mathjax-v3.js` であるとすると：

   .. sourcecode:: python
      :caption: MathJax スクリプト指定例

      mathjax_path = "mathjax-v3.js"

.. seealso::

   :doc:`/mathjax`

``sphinx.ext.todo``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

この拡張は重要ではないのだが、取り除く機会がないのでそのままにしてある。

``todo_include_todos``
   ``True`` に設定すると HTML に Todo 囲み記事が現れる。

.. todo::

   ノートじゅうに散乱している TODO 項目を一掃する。

``sphinxcontrib.mermaid``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``mermaid_version``, ``mermaid_init_js``
   どちらにも空文字列を代入する。その代わり構成項目 ``html_js_files`` にラッパー
   スクリプトのファイル名を追加する。例えばそれが
   :file:`source/_static/mermaid.js` であるとすると：

   .. sourcecode:: python
      :caption: Mermaid.js スクリプト指定例

      html_js_files = ['mermaid.js']

.. seealso::

   :doc:`javascript-mermaid/index`

拡張
======================================================================

当ノートで利用している拡張について記す。

``sphinx.ext`` から始まる名前の拡張は Sphinx 組み込みの拡張だ。:file:`conf.py`
内のリスト ``extensions`` に含まれるだけで利用可能だ。

:program:`pipenv` でインストールされない拡張については、前述の構成上、サブディレ
クトリー :file:`source/_extensions` に拡張用 Python ファイルを手動で追加する必要
がある。

``sphinx.ext.githubpages``
----------------------------------------------------------------------

この拡張は GitHub の文書配置ルート位置にダミーファイルを配置する。HTML ファイル
を置く場所で Jekyll が働かないようにする意味がある。

   This extension creates :file:`.nojekyll` file on generated HTML directory to
   publish the document on GitHub Pages.

``sphinx.ext.mathjax``
----------------------------------------------------------------------

   This extension puts math as-is into the HTML files. The JavaScript package
   MathJax is then loaded and transforms the LaTeX markup to readable math live
   in the browser.

Sphinx 原稿内の ``math`` directives/roles を変換後 HTML ファイルで数式を描画させ
るためにこの拡張を導入している。

``sphinx.ext.todo``
----------------------------------------------------------------------

Sphinx 原稿内に ``todo`` および ``todolist`` 囲み記事を書けるようにする拡張だ。
これがなくても問題ない。

``IPython.sphinxext.ipython_*``
----------------------------------------------------------------------

原稿に ``ipython`` 指令を記述すると、HTML 変換時によく描画してくれる。

.. ipython::

   In [1]: x = 2

   In [2]: x**3
   Out[2]: 8

先述のように、拡張モジュールはビルド時の Python 環境にインストールされている必要
がある。

.. seealso::

   `IPython Sphinx Directive
   <https://ipython.readthedocs.io/en/stable/sphinxext.html>`__

``sphinxcontrib.mermaid``
----------------------------------------------------------------------

原稿に ``mermaid`` 指令を記述すると HTML 変換時に Mermaid が図式を描画する。

.. mermaid::
   :caption: Mermaid 動作確認

   stateDiagram-v2
     [*] --> Still
     Still --> [*]
     Still --> Moving
     Moving --> Still
     Moving --> Crash
     Crash --> [*]

先述のように、拡張モジュールはビルド時の Python 環境にインストールされている必要
がある。

.. seealso::

   `sphinxcontrib-mermaid · PyPI
   <https://pypi.org/project/sphinxcontrib-mermaid/>`__

``japanesesupport``
----------------------------------------------------------------------

現象を正確に記述するのは難しいのだが、本稿 reST ファイルには通常日本語の文をタイ
プする。私の場合は 70 文字打って改行する。日本語の文字と日本語の文字の間に改行文
字が入ることが普通にある。これが最終的に HTML ファイルになり、ブラウザーで読む。
そこでは改行文字だったものが空白文字に置き換わったかのように描画される。

それの回避策として、<http://sphinx-users.jp/reverse-dict/html/japanese.html> で
入手した :file:`japanesesupport.py` を :file:`source/_extensions` に追加
し、Sphinx 拡張としてロードしている。

.. todo::

   執筆中に次の拡張が存在することに気づく：

   `sphinxcontrib-trimblank · PyPI <https://pypi.org/project/sphinxcontrib-trimblank/>`__

   こちらを使用するほうが良いか？

``disablesearchindex``
----------------------------------------------------------------------

当ノートでは Sphinx の枠組で搭載されている検索機能を完全に排除する。そのための自
作拡張だ。

.. seealso::

   `disable search index generation
   <https://groups.google.com/g/sphinx-users/c/vzSAi8SM3aY>`__

テーマ
======================================================================

先述の理由で `Alabaster <https://alabaster.readthedocs.io/en/latest/>`__ を採用
する。

   Alabaster is a visually (c)lean, responsive, configurable theme for the
   Sphinx documentation system.

レスポンシブとあるので、出力 HTML ファイルは PC でも携帯電話でもブラウザーでいい
感じに表示される。

オプション
----------------------------------------------------------------------

構成ファイルで ``html_theme_options`` の値を辞書で指定する：

.. sourcecode:: python
   :caption: HTML テーマオプション設定例

   html_theme = 'alabaster'
   html_theme_options = {
       # ...
   }

特に重要な項目は次のものだと思う：

``github_button``
   ``False`` とする。``True`` にしておくと、ページを修正したくなるだろう。
``github_repo``
   リポジトリーの名前にする。本ノートならば文字列 ``'notebook'`` だ。
``github_user``
   リポジトリーの所有者名にする。本ノートならば文字列 ``'showa-yojyo'`` とする。
``nosidebar``
   サイドバーを使わないことにするので ``False`` とする。
``show_powered_by``
   ``False`` とする。
``show_relbars``
   サイドバーを使わない代わりにここを ``True`` とする。ページの天井か柱またはそ
   の両方に *next* と *previous* リンクが示される。

スタイルシート
----------------------------------------------------------------------

構成ファイルで指定されるオプションでは対応できない CSS 項目をカスタマイズしたい
場合には、ファイル :file:`source/_static/custom.css` を自分で用意してスタイルを
定義する手法を採る。

オリジナルの CSS は Python ディレクトリーのファイル
:file:`lib/site-packages/alabaster/static/alabaster.css_t` に定義されている。

テンプレート
----------------------------------------------------------------------

サブディレクトリー :file:`source/_templates` に Alabaster を構成する HTML テンプ
レートファイルと同名のファイルを置くことで、対応する内容を上書きすることが可能
だ。

当ノートではフッターを描画するための :file:`layout.html` を次のように改造してあ
る（一部略）：

.. sourcecode:: html+jinja

   {% extends "alabaster/layout.html" %}

   {%- block footer %}
   <div class="footer">
     <ul>
       <li id="footer_logo">
         ...
       </li>
       <li id="footer_copyright">
         Copyright &copy; {{ copyright }}.
       </li>
     </ul>
   </div>
   {%- endblock %}

オリジナルの Jinja2 テンプレートファイルは Python ディレクトリーのサブディレクト
リー :file:`lib/site-packages/alabaster` に配置されている。

関連ノート
======================================================================

* :doc:`/python-pipenv`
* :doc:`/python-jinja2`
* :doc:`/python-pygments`
* :doc:`/github/index`
* :doc:`/mathjax`
* :doc:`/javascript-mermaid/index`
* :doc:`/python-mkdocs`
* :doc:`/ruby-jekyll`

.. _Sphinx: https://www.sphinx-doc.org/en/master/
