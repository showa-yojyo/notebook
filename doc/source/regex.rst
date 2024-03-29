======================================================================
正規表現学習ノート
======================================================================

自分の正規表現技術を見直そう。勘だけで使い続けていると行き詰まるのは必至。

.. contents::

資料
======================================================================

`Regular expression - Wikipedia <https://en.wikipedia.org/wiki/Regular_expression>`__
   Wikipedia の正規表現に関する記述だ。公平性と専門性のバランスが良い。特に
   Syntax の節をよく読んでおきたい。
`PCRE - Perl Compatible Regular Expressions <https://www.pcre.org/>`__
   PCRE 公式サイト。PCRE は Perl 5 と同じ構文、語義を使って正規表現パターンマッ
   チを実装する機能を備えるライブラリーだ。

教材
----------------------------------------------------------------------

`Regular Expressions - Wikibooks <https://en.wikibooks.org/wiki/Regular_Expressions>`__
   教科書。こちらは読みやすさ重視か。用語集が便利。
`20 Small Steps to Become a Regex Master <https://dev.to/awwsmm/20-small-steps-to-become-a-regex-master-mpc>`__
   この記事の水準の正規表現を習得しているかどうかをまず確認しろ。著者は正規表現
   達人の基準を lookaround 習得辺りに見据えているようだ。
`RegexOne <https://regexone.com/>`__
   学習する正規表現の構成物をページ右柱を見ればわかるようになっている。言語別案
   内もうれしい。
`Rex Egg <https://www.rexegg.com/>`__
   自家製単語境界の技法や、パスワード文字列の条件と lookahead それぞれの個数の関
   係、ゼロ幅合致の用途など、実践にも理論にも質が良い。黒帯の記事群は相当難し
   いところがある。
`Regular-Expressions.info`_
   主要正規表現エンジン機能表が便利だ。エンジンごとに特定の機能が利用可能である
   かどうかを調べるのに最適。プログラマーはブラウザーのブックマークに追加してお
   くのが良い。

ツール
----------------------------------------------------------------------

自分で書いた正規表現を検証するためのツールを確保しておきたい。JavaScript の正規
表現エンジンで事足りるならばブラウザーの開発ツールコンソールを使えばよい。それ以
外のプログラミング言語版の正規表現を検証するには、次のような便利なものを利用した
い：

`regex101: build, test, and debug regex <https://regex101.com/>`__
   正規表現と対象テキストを入力してマッチや置換を実行するオンラインツール。
   :guilabel:`FLAVOR` を所望の正規表現方言に設定して用いる。学習時は主に PCRE2で
   検証する。特定のエンジンを試したい時に限って Python などに変更するという使い
   方でいい。

   処理時間を表示するのもうれしい。デバッガーも面白そうだ。これ一本で事足りるか
   もしれない。
`RegexPlanet <https://www.regexplanet.com/>`__:
   正規表現検証ツールとレシピ集をふるまっている Web サイト。見出しによると Go,
   Haskell, Java, JavaScript, .Net, Perl, PHP, PostgreSQL, Python, Ruby, Tcl,
   XRegExp に対応している。
`PowerGREP <https://www.powergrep.com/>`__
   «Windows grep Software to Search (and Replace) through Files and Folders on
   Your PC and Network» とのことだ。YouTube に誰かの利用時撮影ビデオがある。

上述教材各サイトにあるツール紹介記事に細かい用途に応じたツールレビューがある。

メモ
======================================================================

先述の教材から気になる記述を抜き出してとりあえず列挙しておく。

* 「優れた正規表現」をルール化するのは容易ではない。
* NFA と DFA のどちらかを選べる場合、通常は NFA が最も速い。実際、現代の言語では
  これが最も一般的な実装だ。
* 式を評価するために括弧が必要だが、データを捕捉する必要がない場合は
  :regexp:`(?: ... )` 構文を使う。
* 可能な限りアンカーを指定する。バックトラックの手間が省けることもある。
* 相互排他的なトークンを連続させるのは美しい。
* ドットを控えめに使う。
* ドットは最も誤用されるメタ文字だ。
* :regexp:`\\h` が使えるならば :regexp:`\\s` に優先して使うほうがいい。
* :regexp:`\\v` が使えるならば :regexp:`[\\r\\n]` に優先して使うほうがいい。
* 正規表現をどこまで完璧にするかは、その正規表現で何をしたいかによって決まる。
  ユーザーの入力を検証するのであれば、完璧でなければならない。
* 入力を検証する前に、文字列前後の空白を除去しておく。
* Python に :regexp:`\\z` はない。
* 正規表現エンジンに捕捉を back track させたくない場合は atomic group を使用する
  ことが可能だ。
* 正規表現によっては前方参照という概念があり得る。
* アクセント付きのアルファベットは一文字ではない場合がある。
* Unicode には平仮名および片仮名という区分が設けられている。それを利用した正規表
  現記号列がある。
* Lookaround が絡む正規表現を組み立てることが難し過ぎる。
* ソースコードで置換テキストを文字列定数として指定する場合、プログラミング言語に
  よって文字列定数内で特別な扱いを受ける文字をプログラマーが知っていなければなら
  ない。
* :program:`grep` で複数行モードはあり得ない。
* GNU :program:`grep` は Linux で最もよく使われている :program:`grep` の一種だ。
  テキスト指向エンジンと正規表現指向エンジンの両方を使う。後方参照を使用する場合
  は正規表現指向エンジンを使用する。それ以外の場合はより高速なテキスト指向エンジ
  ンを使用する。
* 基本正規表現つまり :abbr:`BRE` は現在でも使われている最も古い正規表現だ。GNU
  ユーティリティーの :program:`grep`, :program:`ed`, :program:`sed` がこれを使用
  している。
* JavaScript のすべての実装で正規表現がまったく同じように動作する。
* PowerShell の正規表現はそれと明示しないと大文字小文字を区別しない。
* 正規表現を作成する際には、何に合致させないかを考えることの方が重要だ。
* Quantifiers を入れ子にする正規表現は破滅的になりがちだ。バックトラック禁止表現
  を身に着けておくといい。
* 境界 :regexp:`\\b` は、その左と右の文字の性質が異なる位置と考えられる。
* Lookaround を応用した区切りパターン正規表現の組み立て方を知っておくと便利。
* Python ``re`` モジュールはゼロ幅マッチでは分割しない？
* Python ``re`` は主要正規表現エンジンの中で二番目に悪い。
* 主要な正規表現エンジンの中で JavaScript は最悪であり、その差は歴然としている。
* ``++`` は諦めない。
* :regexp:`.*?` は高く付く。
* :regexp:`(?R)` は「正規表現全体をここに貼り付け、元の :regexp:`(?R)` を置き換
  える」だ。例えば :regexp:`A(?R)?Z` は ``AZ``, ``AAZZ``, ``AAAZZZ``, ... のすべ
  てを表す。
* 再帰正規表現には出口パターンを含めろ。
* 必ず失敗するパターンを知っていると便利。
* 条件式で lookbehind を使うのは、マッチの前に何らかのテキストがあることを確認し
  たい場合に便利だ。

.. _Regular-Expressions.info: https://www.regular-expressions.info/refflavors.html
