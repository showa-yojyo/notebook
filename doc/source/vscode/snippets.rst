======================================================================
Snippets
======================================================================

VS Code の snippets 機能は、テンプレートというよりは、ループや条件文などの定型
コード入力を支援する機能だと考えた方がいい。:program:`Emacs` の expand-abbrev と
同等以上のことをできる。

.. attention::

   :doc:`./index` 冒頭の前提条件に留意すること。

.. contents::

基本
======================================================================

:doc:`./intellisense` で述べたように、IntelliSense のポップアップに他の候補と併
せて混ざって snippets が表示される。Snippets だけの一覧が必要ならば、コマンド
:guilabel:`Snippets: Insert Snippet` を直接呼び出す。

ショートカットキーでテンプレとしての snippet をエディターに置くのが普通だ。タブ
補完を有効にした状態で :kbd:`Tab` キーを押せばいい。展開可能状態の snippet が置
かれる。

.. code:: json

   {
       "editor.tabCompletion": "on"
   }

組み込み Snippets
======================================================================

VS Code には次の言語用の snippets を組み込みで定義している：

* JavaScript
* TypeScript
* Markdown
* PHP

例えばエディターの言語モードが JavaScript モードであるときには、
``trycatch``, ``dowhile``, ``for`` などの snippets が用意されている。
このことはコマンド :guilabel:`Insert Snippet` を実行すると表示されるドロップダウ
ンリストの :guilabel:`JavaScript Language Basics` というグループの存在により確認
される。

拡張 Snippets
======================================================================

Side Bar :guilabel:`EXTENSIONS: MARKETPLACE` 検索欄でフィルター
:menuselection:`Category --> Snippets` を適用すると、追加的 snippets を含む拡張
が検索できる。

拡張機能が用意している Snippets を利用可能にするには、インストール後に VS Code
を再起動して当該拡張を有効にすることが必要だ。

自作 Snippets
======================================================================

ユーザー独自の snippets を定義することも可能だ。まず、専用の設定ファイルにアクセ
スする手段を知る必要がある。次のいずれかの方法でまず対象となる設定ファイルを間接
的に決定する：

* メインメニューから :menuselection:`File --> Preferences --> Configure User Snippets`
  を選択
* コマンドパレットから :guilabel:`Configure User Snippets` を選択

すると :guilabel:`Select Snippets File or Create Snippets` というポップアップ付
きの入力欄が現れる。目的に応じて snippets を定義する先を決める。

言語モードの snippets を増やしたいならば、言語名に ``.json`` が付いた項目を選択
する。必要に応じてファイルが生成され、snippet の定義オブジェクトを記入すればい
い。

言語モードに関係がない場合、さらに選択肢がある。

作用域
======================================================================

各 snippet には作用域という属性がある。現在のエディターに関連する snippets しか
補完候補として表示されないように必要なものだ。次のいずれかの作用域がある：

1. 言語モードから決定される作用域
2. ワークスペースから決定される作用域

言語モードから決定される作用域
-----------------------------------------------------------------------

単一言語のユーザー定義 snippets は、特定の言語の snippet ファイルで定義される。
コマンド :guilabel:`Preferences: Configure User Snippets` の一覧にある言語名 +
``.json`` の形式をとる項目を選択すると、設定ファイルにアクセスする。このような
snippets は、それが定義されている言語を編集しているときしか補完候補に挙がり得な
い。

多言語および大域的ユーザー定義 snippets はすべて拡張子が ``.code-snippets``
の JSON ファイルで定義される。この種の設定ファイルでは、snippet 定義に任意の個数
の言語識別子を取るプロパティー ``scope`` を追加できることに注意する。指定されて
いない場合、当該 snippet はすべての言語で補完候補に挙がり得る。

ユーザー定義 snippet のほとんどは一つの言語を作用域とするため、言語固有の
snippet ファイルで定義される。

ワークスペースから決定される作用域
-----------------------------------------------------------------------

ワークスペースを作用域とする snippets 設定ファイルがあり得る。
この場合も拡張子が ``.code-snippets`` という JSON ファイルで snippets を管理する。

コマンド :guilabel:`Preferences: Configure User Snippets` の一覧にある項目
:guilabel:`New Snippets file for ''...` を選択すると、設定ファイルが生成する。
これはワークスペースの ``.vscode`` 内に配置される。

ワークスペース snippets ファイルは、そのワークスペースで働くプロジェクトメンバー間で
snippets を共有するのに用いられる。

ワークスペース snippets はユーザー snippets 同様にプロパティー ``scope`` を指定でき、
特定の言語を作用域に指示できる。

構文
=======================================================================

まず公式文書の例を引用する。これはユーザーレベル snippets であり、具体的には
ファイル :file:`/path/to/Code/User/snippets/javascript.json` に定義されている
JSON オブジェクトの一部ということだ：

.. code:: json

   {
       "For Loop": {
           "prefix": ["for", "for-const"],
           "body": ["for (const ${2:element} of ${1:array}) {", "\t$0", "}"],
           "description": "A for loop."
       }
   }

基本事項を一気に列挙しておく：

* プロパティー自体が snippet の名前だ。この場合は ``For Loop`` という文字列が
  IntelliSense 等の補完候補リストの項目ラベル名となる。
* 値のオブジェクトが snippet の仕様を表現する。

  ``prefix``
      IntelliSense でこの snippet を表示するためのトリガー文字列を定義する。
      合致がこの配列の値対して行われるので、例えば ``fc`` とタイプすると
      ``for-const`` に合致するだろう。

  ``body``
      Snippet 本文。この文字列がエディターに展開され、変数を処理し始める。

      * この例のように文字列配列で指定すると、展開時に複数行として結合される。
      * 改行文字と埋め込みタブ文字は展開時の文脈に即して整形される。

  ``description``
      IntelliSense 補完候補ポップアップにメモのように表示される文言。

* ``body`` 文字列中にプレースホルダー ``$0``, ``$1``, ... を含めることもできる。

  * :kbd:`Tab` キーで次のプレースホルダーにジャンプ。その時点でプレースホルダー
    を編集したり、次のプレースホルダーにジャンプしたりすることができます。
  * コロン ``:`` の後の文字列がもしあれば、それは既定値を指示している。この例だ
    と ``${2:element}`` は、プレースホルダー 2 の入力をスキップすると文字列
    ``element`` が適用されるということだ。
  * プレースホルダーの探索順序は、1, 2, ... だ。0 は特別で、常に最後に来るオプ
    ショナスケースだ。この位置にキャレットがある状態で snippet 展開が終了する。

本文構文についてさらに詳しく述べる。

タブ移動
-----------------------------------------------------------------------

展開中、snippet 本体がプレースホルダーを含んでいれば、:kbd:`Tab` を押すことでそれらの
間を番号順に移動する。

* 前述のように ``$0`` は展開終了直後のキャレットの位置を指示する特別なものだ。
* 同一番号のプレースホルダーを複数含むことができる。その場合、複数キャレットモー
  ドと同様の挙動となる。

プレースホルダー
-----------------------------------------------------------------------

公式にはプレースホルダーは既定値が指定された ``$1``, ``$2`` などのことを言うようだ。
区別する必要性が感じられないので、本稿では値があろうがなかろうか、どちらもプレー
スホルダーと呼ぶ。

* :kbd:`Tab` を押してプレースホルダーが移動すると、キーボードで編集しやすいよう
  に対象部分が選択状態になる。
* ``${1:another${2:placeholder}}`` のように入れ子にしてもよい。

ドロップダウンリスト
-----------------------------------------------------------------------

プレースホルダーにドロップダウンリストを仕掛けて、そこから文字列を選べるようにす
る機能がある。日記で使っているものを引用する：

.. code:: text

   ${2|晴れ,曇り,雨|}

このプレースホルダーに焦点が合っていると、人は :kbd:`↑` と :kbd:`↓` を押すことで
入力文字列を選択し、この位置にそれを挿入する。

変数
-----------------------------------------------------------------------

この `一覧 <https://code.visualstudio.com/docs/editor/userdefinedsnippets#_variables>`__
にあるように、エディター固有の情報、日付・時刻、ランダム要素を変数として参照できる。

変数変換
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:program:`Bash` の変数のように、変数の値を挿入する前に加工することができる。
変数名の後に文字 ``/`` で三つの部分に分けて、それぞれで変換のための指定をする：

.. code:: text

   ${PLACEHOLDER_OR_VARIABLE/PART1/PART2/PART3}

``PLACEHOLDER_OR_VARIABLE`` はプレースホルダー番号 ``1``, ``2``, ... か、また
は変数名を指定する。

``PART1`` ではプレースホルダー番号または変数の値に対して合致する正規表現パター
ンを書く。正規表現は JavaScript 方式で指定する。

``PART2`` では書式またはリテラル文字列を指定する。書式については説明が難しいので
公式文書でも文章の形式では述べられていない。文法定義から急所を抜粋する：

.. code:: text

   transform   ::= '/' regex '/' (format | text)+ '/' options
   format      ::= '$' int | '${' int '}'
                   | '${' int ':' '/upcase' | '/downcase' | '/capitalize' | '/camelcase' | '/pascalcase' '}'
                   | '${' int ':+' if '}'
                   | '${' int ':?' if ':' else '}'
                   | '${' int ':-' else '}' | '${' int ':' else '}'
   int         ::= [0-9]+
   text        ::= .*
   if          ::= text
   else        ::= text

これによると、どうやら ``PART1`` の大文字小文字を変換したり、場合分けして（ここ
が文書化されていない）リテラル文字列（のはず）を選択したりできるはずだ。後で試す。

``PART3`` には必要ならば正規表現オプションを書く。なければ空にしておく。

.. admonition:: 利用者ノート

   変数変換をユーザー用設定ファイルに一時的に定義して、挙動をよく確認しておく。
   ``$TM_SELECTED_TEXT``, ``$CLIPBOARD`` を上手く使いたい。

   クリップボードにある複数行からなるテキストを変換するための snippet を定義する
   とき、改行文字が ``\r\n`` であることに注意を要する。VS Code 内でカット＆ペー
   ストするときに ``\n`` になる状況にも対応するべく、正規表現パターン中の改行を
   ``\r?\n`` のように書くかもしれない。
