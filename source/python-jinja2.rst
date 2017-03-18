======================================================================
Jinja2 利用ノート
======================================================================

.. contents:: ノート目次
   :depth: 3

.. note::

   本稿執筆時の動作環境は次のとおり。

   * OS

     * Windows XP Home Edition SP3
     * Windows 7 Home Premium x64 SP1
     * Windows 10 Home x64

   * Python およびパッケージ

     * Python_: 2.6.6, 2.7.3, 3.4.1, 3.5.0, 3.5.2
     * Jinja2_: 2.5.5, 2.6, 2.8

関連リンク
======================================================================
Jinja2_
  公式サイト。

Jinja2 とは何なのか
======================================================================
* Jinja2 Documentation によると <general purpose templating language> とのこと。
  Python で動くライブラリーであると同時に、テンプレートを何かする言語でもある。

* Jinja という名前は日本語の神社から来ているらしい。
  その理由は：
  <it's the name of a Japanese temple and temple and template share
  a similar pronunciation> (Jinja2 Documentation, "Why is it called Jinja?")

インストール方法
======================================================================
* :ref:`python-pkg-proc` の工程どおりにインストールすればよい。

* オフラインで読めるようにドキュメントも確保しておく。
  ありがたいことに、日本語訳も存在する（アドレス忘れた）。

Python コードを書く
======================================================================

Hello world
----------------------------------------------------------------------
Jinja2 Documentation から引用：

>>> from jinja2 import Template
>>> template = Template('Hello {{ name }}!')
>>> template.render(name='John Doe')
'Hello John Doe!'

:code:`jinja2.Template.render` の引数は dict オブジェクトかキーワード引数。
これをテンプレートのコンテキストという。

クラス Environment
----------------------------------------------------------------------
コンフィグレーションクラスと思えばよい。

.. code-block:: python3

   from jinja2 import Environment, PackageLoader
   env = Environment(loader=PackageLoader('yourapplication', 'templates'))
   template = env.get_template()
   print(template.render(name='y', age='5'))

* コンストラクタの引数はすべてキーワード引数。
  個人的によく使うキーワード引数をメモしておくと後で役に立つ。

  :code:`autoescape`
     XML コード用のエスケープをやってくれる。

  :code:`newline_sequence`
     デフォルト値が ``'\n'`` なので Windows 環境では注意する。

  :code:`loader`
     ローダーを指定。
     テンプレートをどこかからオブジェクトへロードする。

     なおローダーを指定しないで利用することも可能。
     その場合は :code:`get_template` ではなく :code:`from_string` を利用して
     テンプレートオブジェクトを得ることになる。

* :code:`get_loader` メソッドの最初の引数としてテンプレート名を指示する。
  その意味は Environment オブジェクトに結びついているローダーの型によって変わる。

クラス Template
----------------------------------------------------------------------
* 先の Hello world の例のように、直接コンストラクターからオブジェクトを生成することもできるが、
  Template オブジェクトは通常 Environment オブジェクトの
  :code:`get_template` メソッドから得る。

  ただし、ローダーを指定せずに Environment を生成した場合は、
  :code:`from_string` メソッドで Template オブジェクトを得ることになる。

  .. code-block:: python3

     MY_TEMPLATE = 'Hello {{ name }}!'

     env = Environment()
     # ...
     template = env.from_string(MY_TEMPLATE)
     print(template.render(name='John Doe'))

* :code:`render` メソッドはテンプレートテキストとキーワード引数を加工して、
  ユニコード文字列を一気に返す。

各種 Loader
----------------------------------------------------------------------
* ローダーは Environment オブジェクトが持っている。

* <Loaders are responsible for loading templates from a resource
  such as the file system> (Jinja2 Documentation) だそうなので、
  リソースが何であるかによって利用するべきローダーが決まるのだろう。

.. code-block:: text

   BaseLoader
       FileSystemLoader
       PackageLoader
       DictLoader
       FunctionLoader
       (and more)

* テンプレファイルを基にテキストファイルを量産するという使い方を検討するならば、
  FileSystemLoader を選ぶのが筋。習得の対象をこれ一本に絞ろう。

  * コンストラクターの引数はテンプレファイル置き場フォルダー（必須）
    とエンコーディング（オプショナル）。

テンプレートの記法
======================================================================
テンプレートテキストは定型文と可変部分からなるものだから、
可変部分を集中して研究しよう。

以下、デフォルト設定の Environment オブジェクトを利用すると仮定してメモをとる。

初歩的なテンプレートの例
----------------------------------------------------------------------
Jinja2 Documentation からそのまま引用してきたテンプレート例を示す。

.. code-block:: jinja

   <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
   <html lang="en">
   <head>
       <title>My Webpage</title>
   </head>
   <body>
       <ul id="navigation">
       {% for item in navigation %}
           <li><a href="{{ item.href }}">{{ item.caption }}</a></li>
       {% endfor %}
       </ul>

       <h1>My Webpage</h1>
       {{ a_variable }}
   </body>
   </html>

* ``{% ... %}`` や ``{{ ... }}`` が可変部分。
   それ以外の部分はすべて定型文。

   * ``{% ... %}`` は変数宣言・代入やループ処理といったものを実行をさせる。
   * ``{{ ... }}`` は結果の表示をさせる。

テンプレートに変数を埋め込む方法
----------------------------------------------------------------------
``{{ foo }}`` と書くと、Python コードからテンプレートの :code:`render` 関数の
キーワード引数 ``foo`` に何らかのオブジェクトを渡した場合に、
そのオブジェクトに対する :code:`print` 結果がそこにテキスト化される。

* 渡さなかった場合どうなるのか、あとで試すこと。

``{{ foo.bar }}`` と書くと、うまくいけば実引数オブジェクトの ``bar``
属性オブジェクトに対する :code:`print` 結果がそこにテキスト化される。

* ``bar`` 属性のないオブジェクトを渡した場合どうなるのか、確認すること。

* 変数名は Python 2.x 系の流儀に従い正規表現
  ``[a-zA-Z_][a-zA-Z0-9_]*`` にマッチする文字列でなければならない。

フィルター
----------------------------------------------------------------------
``{{ ... }}`` の出力結果をある程度加工する能力がある。
これをフィルターと呼んでいるようだ。

* 「引数を取るフィルター」というものがあり、関数呼び出しのような記法で指示する。

* フィルターは組み込みのものと、自作のものが使えるようだ。

  * 自作の場合、Python コードでフィルター関数をまず書く。
    次に Environment オブジェクトの :code:`filters` リストに関数を追加する。

    Jinja2 Documentation に :code:`datetime`
    オブジェクトを書式を与えてテキスト化するサンプルが紹介されている。

  * フィルターの名前（識別子）は正規表現
    ``[a-zA-Z_][a-zA-Z0-9_]*(\.[a-zA-Z_][a-zA-Z0-9_]*)*`` にマッチすることになる。
    ドットが現れるのは、関数の存在するパッケージによるものだろう。

* 全体の記法は変数名の右側にパイプ記号とフィルター呼び出しを追記していく。
  UNIX のシェルコマンドラインみたいなイメージだろう。
  例えば ``{{ list|join(', ') }}`` と書くと、CSV テキストが展開される。

* ただし、組み込みのフィルター一覧を見ると個人的には用はない。

条件分岐
----------------------------------------------------------------------
ある条件の成り立つときには違うものを書きたいときに利用する機能。

.. code-block:: jinja

   {% if loop.index is even %}
   <td class="black_cell">
   {% else %}
   <td class="white_cell">
   {% endif %}

* ``if`` の次に書く表現をテストと呼ぶ。
  テストには組み込み型のものと自作のものが使える。

  * 自作の場合、Python コードでテスト関数をまず書く。
    次に Environment オブジェクトの :code:`tests` リストに関数を追加する。

    Jinja2 Documentation に整数オブジェクトを与えて、
    それが素数か否かのテストを自作する例が紹介されている。

  * テスト名（識別子）はフィルターと同様に正規表現
    ``[a-zA-Z_][a-zA-Z0-9_]*(\.[a-zA-Z_][a-zA-Z0-9_]*)*`` にマッチすることになる。

* 使えそうな組み込み型テスト：
  ``defined/undefined``, ``even``/``odd``/``divisibleby`` くらいか。

コメント
----------------------------------------------------------------------
``{# ... #}`` 部分がコメントとなる。複数行にまたがっても可。

空白文字を制御する方法
----------------------------------------------------------------------
テンプレートタグにマイナス記号をくっつけると、前後の空白文字がカットできる。

.. code-block:: jinja

   {% for item in seq -%}
       {{ item }}
   {%- endfor %}

もしマイナス記号を省いた場合、スペース 4 つと改行文字 2 個が各
``item`` の前と後ろにそれぞれ出力される。
というより、改行、スペース 4 個、
``item`` が来て改行、といった方が正確か。

特別な文字をエスケープする方法
----------------------------------------------------------------------
``{{ raw }} ... {{ endraw }}`` を利用するのがいい。

テンプレートを継承する方法
----------------------------------------------------------------------
ポイントを簡単におさえたメモを残しておく。
用語は自分流のものに書き換える。

* 自分用のスクリプトでテンプレート継承を利用することはまれ。

* 親テンプレート・子テンプレート

  * 親では、子でいわばオーバーライドさせたいテキスト部分を
    ``{% block ブロック名 %}`` と ``{% endblock %}`` で囲む。

    * しばしばブロックが別のブロックを含むことがある。
    * しばしばブロックが空になることがある。

  * 子はテンプレートの書き方がぜんぜん違う。

    * ``{% extends テンプレファイルパス %}`` で親を指示する。

    * 以降はブロックのオーバーライドの羅列となる。

    * ``{{ super() }}`` で親ブロックの内容を展開することができる。
    * ``{{ self.ブロック名() }}`` で同じ内容を展開することができる。
      わかりにくい。

  * 子テンプレート全体が評価されてから ``extends`` が評価される。
    親子両方に同名マクロがある場合は要注意。
    マクロ定義が親のそれで上書きされるだろう。

各種制御構造
----------------------------------------------------------------------

``for`` ブロック
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
定型文を反復処理で生成するのに ``for`` 構文は欠かせない。

* ``{% for ... %}`` ... ``{% endfor %}`` の内部では、
  ``loop.index0``, ``loop.length``, ``loop.cycle()``, etc. といった、
  ループに関連する特別な変数が利用できる。

* Python の :code:`for` ループのような ``else`` 処理が記述できる。

* 次のコード例のように、再帰ループを記述することができる。

  .. code-block:: jinja

     <ul class="sitemap">
     {%- for item in sitemap recursive %}
         <li><a href="{{ item.href|e }}">{{ item.title }}</a>
         {%- if item.children -%}
             <ul class="submenu">{{ loop(item.children) }}</ul>
         {%- endif %}</li>
     {%- endfor %}
     </ul>

* ``{% break %}`` や ``{% continue %}`` もサポート。

``if`` ブロック
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
条件次第で出力するテキストを変えたい場合は当然起りうる。
``if`` の出番はそんなときだろう。

* 基本的には Python の :code:`if` と同じような感じで書ける。
  ``else`` や ``elif`` もある。最後に ``endif`` で締め括る必要がある。

* 通常の ``if`` 構文の他に、inline if expression という使い方がある。

  .. code-block:: text

     <do something> if <something is true> else <do something else>

``macro`` ブロック
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
テンプレート中にマクロを定義できる。
Jinja2 で言うマクロというのは、プログラミング言語的関数みたいなもの。

.. code-block:: jinja

   {% macro input(name, value='', type='text', size=20) -%}
       <input type="{{ type }}" name="{{ name }}" value="{{ value|e }}" size="{{ size }}">
   {%- endmacro %}

   <p>{{ input('username') }}</p>
   <p>{{ input('password', type='password') }}</p>

* マクロブロックは ``{% macro マクロ名(引数リスト) %}`` ... ``{% endmacro %}``
  で定義する。

* マクロ呼び出しは ``{{ マクロ名(実引数リスト) }}`` の形になる。

* 色々と特殊な変数がある。

  * :code:`varargs` - list オブジェクト。位置パラメータが格納される。
  * :code:`kwargs` - dict オブジェクト。キーワード引数が格納される。
  * etc.

``call`` ブロック
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
マクロ展開中に、マクロ呼び出し元の何かを展開する機能。
Jinja2 Documentation からそのまま引用した例だが：

.. code-block:: jinja

   {% macro render_dialog(title, class='dialog') -%}
   <div class="{{ class }}">
       <h2>{{ title }}</h2>
       <div class="contents">
           {{ caller() }}
       </div>
   </div>
   {%- endmacro %}

   {% call render_dialog('Hello World') %}
       This is a simple dialog rendered by using a macro and
       a call block.
   {% endcall %}

上のテンプレートの ``call`` ブロックが展開されると次のテキストになるようだ。

.. code-block:: text

   <div class="dialog">
       <h2>Hello World</h2>
       <div class="contents">

       This is a simple dialog rendered by using a macro and
       a call block.

       </div>
   </div>

#. マクロ ``render_dialog`` が展開されて、
#. マクロブロック内の ``caller`` ブロックに呼び出し元ブロックがそのまま展開される。

``call`` は引数を取ることもできるが、複雑になるのでノートを控える。

``filter`` ブロック
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
縦棒のフィルターではなく、ブロック形式のフィルターというものだ。
``{% filter フィルター名 %}`` ... ``{% endfilter %}`` で囲んだブロックは、
その部分全体がフィルターされる。

変数のセット
----------------------------------------------------------------------
Python コードよろしく、変数を定義することができる。

.. code-block:: jinja

   {% set 変数名 = 式 %}

``include`` 文
----------------------------------------------------------------------
テンプレートファイルが別のテンプレートファイルをインクルードする機能。

.. code-block:: jinja

   {% include テンプレファイルパス %}
   {% include テンプレファイルパス ignore missing %}
   {% include テンプレファイルパス ignore missing with context %}
   {% include テンプレファイルパス ignore missing without context %}

* ``ignore missing`` は「ファイルが存在しない場合はインクルードを無視する」の意。
* ``with context`` 等は「インクルード時点での変数やマクロの定義状態をどう取り扱うか」
  を決めるものだろう。よく調べていない。

``import`` 文
----------------------------------------------------------------------
使わなそうなのでパス。

応用例を考える
======================================================================
Jinja2 を利用して何かテキストデータを作成してみよう。

簡易日記テキストファイル
----------------------------------------------------------------------
事始めということで、簡単な日記ファイル作成スクリプトを作ってみよう。

テンプレ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
次の内容のテキストファイルを :file:`diary.txt_t` として保存する。

.. code-block:: jinja

   {#- 簡単な日記テンプレ -#}

   {#- 曜日名の配列
       0 が月曜日に相当するように宣言すること。
   -#}
   {%- set dows = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun") -%}

   {#- 日付タイトル部のテキスト生成 -#}
   {%- macro day_title(year, month, day2) -%}
   {{ '%d/%02d/%02d (%s)'|format(year, month, day2[0], dows[day2[1]]) }}
   {%- endmacro -%}

   {#- 以下テンプレート本体 -#}

   ==================================================
   {{ year }} 年 {{ month }} 月の日記
   ==================================================
   {% for d in days %}
   {%- if d[0] %}
   --------------------------------------------------
   {{ day_title(year, month, d) }}
   --------------------------------------------------
   （この日の日記をここに書く）
   {% endif -%}
   {%- endfor -%}

* メンテのことを考えてコメントをふんだんに盛り込むこと。
  さらに、コメントブロックにはハイフン付きを利用して、
  空白文字がテンプレ本文に影響を与えないようにするのがコツ。

* ここには書かなかったが、テンプレで参照する引数の説明も添えるのがよいだろう。

* テンプレファイルの文字エンコーディングは覚えておくこと。
  Python コードを書くときにローダーオブジェクトに :code:`encoding` を
  指示してやらねばならない。

Python コード
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
次の内容のコードを :file:`diary.txt_t` のあるディレクトリーに保存し、
その場で実行すると :file:`diary-2011-04.txt` のような、
手動で日記を書くためのテキストファイルができる。

.. code-block:: python3

   from jinja2 import Environment, FileSystemLoader
   from calendar import Calendar
   import datetime

   # the path to the template(s)
   tmpldir = '.'
   env = Environment(
       loader=FileSystemLoader(tmpldir, encoding='utf-8'),
       autoescape=False)
   tmpl = env.get_template('diary.txt_t')

   # Generate blank diary for this month.
   today = datetime.date.today()
   y, m = today.year, today.month
   cal = Calendar()

   # Output it to a text file.
   with open('diary-{:04d}-{:02d}.txt'.format(y, m), 'w') as fout:
       fout.write(tmpl.render(
           year=y, month=m, days=cal.itermonthdays2(y, m)))

例が単純過ぎるので、全部 Python コードに埋め込みたくなるのをグッと我慢。

実行結果
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: text

   ==================================================
   2011 年 4 月の日記
   ==================================================

   --------------------------------------------------
   2011/04/01 (Fri)
   --------------------------------------------------
   （この日の日記をここに書く）

   --------------------------------------------------
   2011/04/02 (Sat)
   --------------------------------------------------
   （この日の日記をここに書く）

   <<以下省略...>>

想像通りのものができたが、これではある意味テンプレートからテンプレートを作ったことになる。
とは言え Jinja2 の本来の用途がわかったのでよしとする。
この例で言うと、日記本文もあらかじめどこかに生のテキストの形で存在してしかるべきなわけだ。

TODO
======================================================================
.. todo::

   * Git_ を利用した開発版 Jinja2_ の作業コピー取得をやってみる。

     これは難しくないからやってもやらなくてもよい。
     おそらく次のようなことをするだけで十分。

     .. code-block:: console

        $ pip uninstall jinja2
        $ git clone https://github.com/mitsuhiko/jinja2.git
        $ cd jinja2
        $ pip install -e .

   * Extension 全般。

.. include:: /_include/python-refs-core.txt
.. _Jinja2: http://jinja.pocoo.org/
.. _Git: http://git-scm.org/
.. _MarkupSafe: http://github.com/mitsuhiko/markupsafe
