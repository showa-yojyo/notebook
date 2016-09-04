======================================================================
Pygments 利用ノート
======================================================================

.. contents:: ノート目次

.. note::

   本稿執筆時の動作環境は次のとおり。

   * OS

     * Windows XP Home Edition SP3
     * Windows 7 Home Premium x64 SP1
     * Windows 10 Home x64

   * Python およびパッケージ

     * Python_: 2.6.6, 2.7.3, 3.4.1, 3.5.0, 3.5.2
     * Pygments_: 1.4, 1.6, 2.0.2, 2.1.3

関連リンク
======================================================================
Pygments_
  公式サイト。

Pygments とは何だ
======================================================================
「プログラムコード片を表すテキストを入力とし、
部分部分に着色等の装飾を指示する命令コードを付加したテキストを出力する
Python_ 製パッケージ」とでも言えばいいのだろうか。

インストール
======================================================================
正しいインストール方法はいつものように複数ある。
:ref:`python-pkg-proc` に図示しておいた。
普通は Sphinx のインストールを済ませていると思われるので、
その依存パッケージである Pygments もすでに利用可能になっているはずだ。

アップグレードの方法もインストールとほぼ同様なので省略する。

開発版コードをダウンロード
----------------------------------------------------------------------
Mercurial_ とやらが必要なのでパス。

ドキュメントも確保する
----------------------------------------------------------------------
学習の都合上、
`公式サイト <http://pygments.org/download/>`__
からオフライン用のドキュメント一式をダウンロードしておくとよいだろう。

いきなり使ってみる
======================================================================
ドキュメントの Introduction and Quick Start を読みながらメモ。

* 簡単に言うと Pygments の設計様式は 4 本柱。
  よく読むと大事なのはこのうちの 2 本だけか。

  * ``lexers``: ソースコードを解析して、
    これはキーワード、これはリテラル文字列、等々というふうに分類する。

    * この処理をトークンに分解すると言う。
    * プログラミング言語毎に専用の lexer が存在する。

  * ``filters``: lexer からの出力（トークンストリーム）をテキスト的な加工をするときに利用する。

  * ``formatters``: 処理結果を何らかの書式で出力する。
    HTML, XML, LaTeX, RTF, etc...

  * ``styles``: キーワードやコメントをどうハイライトするのかを決める役割がある。

Python コードから Pygments の機能を利用する
----------------------------------------------------------------------
ドキュメントに紹介されている例を検討してみる。
ここでは PythonLexer に代えて Python3Lexer を適用してみる。

.. code-block:: python3

   from pygments import highlight
   from pygments.lexers import Python3Lexer
   from pygments.formatters import HtmlFormatter
  
   code = 'print("Hello World")'
   print(highlight(code, Python3Lexer(), HtmlFormatter()))

これは「Python のソースコードを HTML コード片に変換する」例のごく単純なもので、
最後に :code:`highlight` 関数で締めくくっている。

出力結果を示す。

.. code-block:: html

   <div class="highlight"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Hello World&quot;</span><span class="p">)</span>
   </pre></div>

何が highlight なのかと言うと、HTML コードに装飾用のマークアップが付いていることが認められる。

* コード片全体が ``highlight`` というクラスの ``DIV`` タグに囲まれている。
* 丸括弧が ``p`` というクラスの ``SPAN`` タグに囲まれている。
* キーワード ``print`` が ``nb`` というクラスの ``SPAN`` タグに囲まれている。
* リテラル文字列 ``Hello World`` が ``s2`` というクラスの ``SPAN`` タグに囲まれている。
  ついでに言うと、ダブルクォーテーションがエスケープ済み。

どうやら CSS を自分で好きに書けば、ハイライト（色付けやら何やら）を実現できるということか。

以上の単純な例から、目的に応じて処理したい言語に対応する
lexer と出力結果に対応する formatter を見つけたり自作したりすればよさそうだということが読み取れる。

コマンドラインツールを利用する
----------------------------------------------------------------------
Pygments をインストールすると、
:file:`Scripts` フォルダーに :file:`pygmentize` という実行ファイルができる。
ファイルを受け取って、

* コンソールウィンドウに出力するときは文字通りハイライトしたテキストを出力する。
* ファイルに出力するときは、前述の形式でテキストを出力する。

が、実際やってみると前者はコントロール文字をガンガン出力するだけで読めたものではない。
もっぱら後者の用法で利用する。

.. code-block:: console

   # HTML 形式で出力し、ファイル名を test.html と指定。
   $ pygmentize -f html -o test.html test.py

   # スタイル colorful の定義、つまり CSS コードを画面に出力させる。
   $ pygmentize -f html -S colorful

   # -N オプションで入力ファイル名から lexer を推測する。
   $ pygmentize -N test.txt

   # -L オプションで利用可能なコンポーネントを画面にリスト。
   $ pygmentize -L lexers

   # -H オプションでより詳しい説明を画面に出力する。
   $ pygmentize -H lexer python

コンポーネント
======================================================================
さっき言った 4 本柱を見ていく。

Lexers
----------------------------------------------------------------------

個人的に利用する可能性が高い lexers を aliases 形式でここにメモっておく。
名前をおぼえるには aliases 形式が応用が効く。
Sphinx_ の ``code-block`` ディレクティブの引数がこの aliases と一致することに注意。

.. code-block:: text

   ('bash', 'sh')
   ('cpp', 'c++')
   ('css',)
   ('django', 'jinja')
   ('html',)
   ('make', 'makefile', 'mf', 'bsdmake')
   ('python', 'py')
   ('python3', 'py3')
   ('tex', 'latex')
   ('text',)
   ('xml',)
   ('xslt',)
   ('rst', 'rest', 'restructuredtext')

* 最初に全ての lexers をザッと眺めておくと、
  自分が使うであろう lexer の当たりがつけやすい。

* :code:`pygments.lexers.get_all_lexers` 関数で、各 lexer を表現する
  :code:`(name, aliases, filetypes, mimetypes)` を指すイテレータが得られる。

  * :code:`name` は文字列。特に使わない。
  * :code:`aliases` は文字列の tuple で、これのいずれかを引数にして関数
    :code:`get_lexer_by_name` に渡すと、対応する lexer オブジェクトが得られる。
  * :code:`filetypes` 等も使わない。

* もし「言語 XXX の lexer は存在するだろうか」と思ったら、
  XXX のファイル拡張子を知っているならば、関数
  :code:`guess_lexer_by_filename` をダミー文字列と共に呼び出してみる。

Formatters
----------------------------------------------------------------------
いつもお世話になるのは :code:`pygments.formatters.html.HtmlFormatter` クラスだが、
意外にたくさんの formatters が用意されている。画像もアリなのか。

* ImageFilter 系を利用するには、別途 PIL パッケージのインストールが必要だそうだ。
* RtfFormatter は MS Word にコピー＆ペーストができるデータを出力するようだ。
* SvgFormatter は実験段階らしい。

Filters
----------------------------------------------------------------------
これに関しては特にノートを取るようなことはない。
大文字小文字を変換したり、空白文字を目に見える文字に置換したりするのに利用するものだ。

Styles
----------------------------------------------------------------------
* スタイルというのは出力が HTML または LaTeX のときに適用される。
* 基本的にここをいじりまわすことはなさそうだ。

.. include:: /_include/python-refs-core.txt
.. _Pygments: http://pygments.org/
.. _Mercurial: http://selenic.com/mercurial/
