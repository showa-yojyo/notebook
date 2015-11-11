======================================================================
用語集
======================================================================
本節の目的は Git_ の文書やヘルプテキストを読解するために十分な語彙を私が身に付けることだ。
これを書くか読むことでそれらを十分理解できるようになることを期待する。

.. contents::

記号関連
======================================================================
コマンドラインの例で頻出する ``<tree-ish>`` や ``[<refspec> ...]`` といった何かの読み方について記す。
:doc:`commands` ではこの記号を多用するかもしれない。

基本規則
----------------------------------------------------------------------
Git のマニュアルでなくても通用する規則も多い。

* 括弧の中に書かれている文字列は、普通は実際に入る文字列を意味する。

* 四角い括弧で括られている引数は、指定の有無が任意であることを意味する。
  括られていない引数は、指定が必須であることを意味する。

* 三角の括弧で括られている引数は、実際には状況に応じた「固有名詞」的な文字列を指示する。

  例えば ``<animal>`` のような引数ならば、
  動物の名前なり ID なりを指示するという意味にとる。
  一般的には ``animal`` というリテラルを指示するわけではない。

* 括弧に括られていない文字列は、実際にその文字列通りにタイプすることを意味する。

* 単語が複数形になっていたり、記号 ``...`` における引数は、
  実際には引数を複数個指示してよいことを意味する。
  複数の値を入力するには、各値を空白文字で区切って入力する。

* 縦棒 ``|`` は「または」を意味する。
  適宜丸括弧も用いる。

頻出するコマンドライン引数の記号集
----------------------------------------------------------------------
コマンドのヘルプでよく見かける ``--parameter=<value>`` の形式をした文字列の読み方に関するメモ。

``<arg>``, ``<argument>``
  汎用。単に何らかの実引数を意味するというだけ。

``<attr>``, ``<attribute>``
  汎用。属性の値を意味する。

``<blob>``
  用語集を参照。
  形式としては SHA-1 値を指示する。

``<branch>``, ``<branchname>``
  ブランチの名前を普通のテキストで指示する。
  特に言及がなければローカルのブランチの名前となる。

  .. hint::

     普通はコマンド ``git branch`` で指示できそうな名前がわかる。

     .. code-block:: console

        $ git branch
           develop
         * feature-comp
           master

     または ``$GIT_DIR/refs/heads`` 以下のファイル名も参考になる。
     下の例で、なぜ ``master`` がないのかを説明できるようにしておきたい。

     .. code-block:: console

        $ ls .git/refs/heads
        develop  feature-comp

     さらにファイル ``$GIT_DIR/info/refs`` の表を見てもよい。
     ブランチ ``feature-comp`` がないのは、
     リモートリポジトリーに push しないようにしているからだと思う。

     .. code-block:: console

        $ grep refs/heads/ .git/info/refs
        7e93a8dc8c013297281c13cb95005f617b96635f        refs/heads/develop
        23c20aee7dab3293d546958f204932f4e44845bb        refs/heads/master

``<cmd>``, ``<command>``
  シェル操作の観点で言うコマンドの意味であることが多い。
  具体的にはユーティリティーツールを実行するためのコマンドライン片だったり、
  ユーザー定義のシェル関数の呼び出しだったりする。

``<commit>``
  コミットを特定することのできる名前を指示する。
  次のどちらかになるはず。

  * ``HEAD``, ``HEAD~3``, etc. のような特別な名前またはそれに基づくテキスト表現
  * 具体的な SHA-1 値

``<commit-ish>``
  用語集を参照。
  広義の ``<commit>`` と解釈して差し支えない。

``<directory>``
  ディレクトリーパスを指定する。
  リポジトリーが処理できる限り、形式は絶対パスでも相対パスでも構わない。

``<file>``, ``<filename>``
  ファイル名をテキストで指定する。

``<hash>``
  用語集を参照。
  形式としては SHA-1 値を指示する。

``<head>``
  用語集を参照。

  .. hint::

     * ディレクトリー ``$GIT_DIR/refs/heads`` 以下のファイル名が head の一覧になる。
     * ファイル ``$GIT_DIR/info/refs`` の ``/heads/`` を含む行が head の一覧になる。

``<message>``, ``<msg>``
  任意のテキストを意味する。

``<mode>``
  Git コマンドによって指定する値が異なる。

  * commit --clean: ``(strip|whitespace|verbatim|scissors|default)``
  * commit --untracked-files:  ``(no|normal|all)``
  * diff, log, status --word-diff: ``(color|plain|porcelain|none)``
  * reset: ``--(soft|mixed|hard|merge|keep)``
  * tag --cleanup: ``(verbatim|whitespace|strip)``
  * etc.

``<n>``, ``<N>``, ``<num>``, etc.
  数字を指示する。
  普通は非負の整数になる。

``<object>``
  任意の型のオブジェクトの名前を指定する。
  少なくとも以下の形式で与えることはできる。

  * SHA-1 値
  * 文字列 ``HEAD`` およびその派生記号
  * ``<tag>`` として認められる値
  * ``<head>`` として認められる値

  より詳細な情報はヘルプ参照。本当に細かいのでここに記すのは難しい。

``<path>``
  ファイルパスを指定する。
  リポジトリーが処理できる限り、形式は絶対パスでも相対パスでも構わない。

``<pathspec>``
  用語集を参照。
  リポジトリー内部に限定して ``<path>`` を抽象的にした概念。

``<ref>``, ``<refname>``
  用語集を参照。

  .. hint::

     * ディレクトリー ``$GIT_DIR/refs`` 以下のパスが ref 一つ一つを示す。
     * ファイル ``$GIT_DIR/info/refs`` の各行が ref 一つ一つを示す。

``<remote>``, ``<repo>``, ``<repository>``
  リモートリポジトリーの名前を ``origin`` のようにテキストで指定する。

  .. hint::

     * コマンド ``git remote [show]`` で該当する名前の一覧を得られる。

       .. code-block:: console

          $ git remote
          origin

     * ディレクトリー ``$GIT_DIR/refs/remotes`` 直下の各ディレクトリー名が該当する。
     * ファイル ``$GIT_DIR/config`` の各 ``[remote "XXX"]`` の ``XXX`` が該当する。
     * ファイル ``$GIT_DIR/info/refs`` の文字列 ``/remotes/`` を含む行について、
       このパターンの直後の単語が該当する。

``<rev>``, ``<revision>``
  commit の object name を指示する。

``<sha1>``, ``<SHA-1>``, etc,
  SHA-1 値を意味する。
  一般に、40 ケタ全部を指定しても、先頭の数ケタを指定してもコマンドが認識してくれる。

``<tag>``, ``<tagname>``
  タグの名前をテキストまたは SHA-1 によって指示する。

  .. hint::

     * コマンド ``git tag [-l|--list]`` で該当する名前の一覧を得られる。

       .. code-block:: console

          $ git tag
          1.1
          1.2
          1.2.1
          1.3

     * ディレクトリー ``$GIT_DIR/refs/tags`` 直下の各ディレクトリー名が該当する。
     * ファイル ``$GIT_DIR/info/refs`` の文字列 ``/tags/`` を含み、
       かつ ``^{}`` を含まない行について、このパターンの直後の単語が該当する。

``<tree>``
  用語集を参照。
  ツリーの object name を指示する SHA-1 値。

``<tree-ish>``
  用語集を参照。
  広義の ``<tree>`` と解釈して差し支えない。

``<type>``
  用語集の object type を参照。
  文字列 ``(blob|tree|commit|tag)`` を指示する。

``<upstream>``
  SHA-1 値というより普通の文字列で upstream branch から branch を除いた文字列を指示する？

``<url>``
  URL をテキストで指示する。

用語集
======================================================================
コンソールで次のコマンドを実行すると、Git 用語集のヘルプドキュメントを閲覧できる。

.. code-block:: console

   $ git help glossary

以下、これを知らないとマニュアルが読めないという程度に重要なもの、
誤解しやすいもの、理解が怪しいものを選んで、
私なりの解釈を多分に含んだ説明文を記す。
併せて、英単語の日本語訳もなるべく付記する。

bare repository
  作業ファイルを一切含まないリポジトリー。
  純度 100 パーセントのリポジトリーとでも言えようか。

  ``XXX.git`` の形になっているリポジトリーのこと。
  例えば GitHub に置いてあるリポジトリーはこの形式だ。
  いつも作業をしているところにある ``.git`` は bare ではない？

  :日本語訳: ベアリポジトリー（英単語をカタカナで書くだけ）

blob object
  ファイルの中身をバイナリーデータとして表現したもの。
  ディレクトリー群 ``$GIT_DIR/objects/xx`` 以下にあるファイル群は blob である。

  辞書で blob を引くと Binary Large Object を意味すると解説している。
  ただし Git の用途では必ずしも「大きい」オブジェクトとは限らない。
  サイズの小さいテキストファイルの blob はやはり小さい。

  :日本語訳: （訳さない）

commit
  用語 commit には名詞的用法と動詞的用法がある。

  名詞として commit と言えば、履歴のある一点を指す。
  Git では commit と呼んでいる概念は、他のバージョン管理システムの修辞法では
  revision とか version とか別の呼び名で表現しているかもしれない。

  あとは commit object のことを commit を呼ぶ場合がある。
  読み手、聞き手が文脈で判断する。

  動詞としては、履歴にプロジェクトの新しくなった状態を格納する行為を意味する。
  コマンドでは ``git commit`` の実行に対応する。

  :日本語訳: コミット（英単語をカタカナで書くだけ）

commit object
  一つの commit を表現するためオブジェクトを意味する。
  親コミット、著者、日付、等々の情報からなる。

  :日本語訳: コミットオブジェクト（英単語をカタカナで書くだけ）

commit-ish
  次のオブジェクトは commit-ish であるという。

  * コミットオブジェクトそのもの
  * あるコミットオブジェクトを指すタグオブジェクト
  * 指す先のオブジェクトを再帰的に辿ると、
    最終的にあるコミットオブジェクトを指すタグオブジェクト

  :日本語訳: （訳さない）

fast-forward
  今いるコミットに対する別のブランチの変更を取り込むのに、
  その変更が現在のコミットの子孫になるようなマージを意味する。
  リモート追跡ブランチで頻繁に起こる現象。

  詳しくは git-merge(1) Manual Page の FAST-FORWARD MERGE の節を参照。

  :日本語訳: （調査中。早送りということはあるまい）
  :cf.: rebase

hash
  オブジェクトの ID

  :日本語訳: ハッシュ（英単語をカタカナで書くだけ）
  :同義語: object name

head
  あるブランチの末端コミットへの名前あり参照。

  例外的な運用をしていなければ、
  ディレクトリー ``$GIT_DIR/refs/heads`` にブランチ名と同じ名前のファイルがある。
  ここには SHA-1 値が書いてあり、これが末端コミット ``HEAD^`` の ID である。

  :日本語訳: （調査中）

HEAD
  現在のブランチ。

  :日本語訳: （訳さない）

index
  インデックスはファイルの集合で、それらの内容をオブジェクトとして格納する。
  あるいは、作業コピーを格納したものであるともみなせる。

  .. hint::

     物理的にはファイル ``$GIT_DIR/index`` である。

  :日本語訳: インデックス（英単語をカタカナで書くだけ）

object
  Git における格納物の最小単位を object と呼ぶ。

  * オブジェクトの特定方法、つまり ID は一つの SHA-1 値である。cf. object name
  * オブジェクトは一度生成されたら、その一部または全部が変更することはない。

  :日本語訳: オブジェクト（英単語をカタカナで書くだけ）
  :関連用語: object name, object type

object name
  オブジェクトの ID
  SHA-1 値で表現される。

  :日本語訳: オブジェクト名

object type
  オブジェクトの型。

  :日本語訳: オブジェクト型
  :関連用語: commit, tree, tag, blob

origin
  デフォルトの upstream repository の名前。

  * 大抵のプロジェクトには追跡用途に最低一つの upstream プロジェクトがある。
    デフォルトで origin がそれに充てられる。

  * 追跡先の更新を fetch 系コマンドでダウンロードすると、
    リモート追跡ブランチ ``origin/<name-of-upstream-branch>`` に影響を及ぼす。

  * ``git branch -r`` や ``git branch -a`` を使って見てみよう。

  :日本語訳: （訳さない）

pathspec
  ファイルパスを表現する文字ベースのパターン。

  Git コマンドにおける、ファイルパスを表現する文字ベースのパターンのことを pathspec と呼ぶ。
  直感的にはファイルパスそのものやワイルドカード (globbing) は pathspec の一つであると思って構わない。
  また、より特殊な pathspec の記法も存在するようだ。
  例えば ``git ls-files ':(top)*'`` を実行すると、作業ディレクトリーが作業コピー内のどこにいようが
  ルート以下にあるすべてのバージョン管理対象のファイルが表示される。

  :日本語訳: （訳さない）

rebase
  あるブランチから別のブランチへ、一連のコミット列を再適用することを意味する。
  それから再適用先ブランチの head をリセットする。

  詳しくは git-rebase(1) Manual Page のアスキーアートがなかなかよいのでそれを見ておく。

  :日本語訳: （訳さない）
  :cf.: fast-forward

ref
  普通は ``refs/`` で始まる名前で、それが何か object name を指すもの、
  または別の ref を指すものは ref であるという。

  * 便宜上、フルネームではなく短縮形の名前が利用可能な場合がある。
  * ref は階層的な名前空間である。
    ズバリ ``$GIT_DIR/refs`` 以下のディレクトリーレイアウトがそれを反映している。
  * ``refs`` で始まらないような名前でも ref であることがある。
    例えば HEAD がそうだ。

  :日本語訳: （訳さない）

reflog
  百聞は一見にしかずで、適当な作業コピーで ``git reflog`` してみるとイメージが大づかみできるだろう。
  作業コピーにおける作業履歴のような概念だろう。

  .. hint::

     .. code-block:: console

        $ git reflog
        3f97afa HEAD@{0}: checkout: moving from develop to feature-comp
        3f97afa HEAD@{1}: merge feature-comp: Fast-forward
        fe2ad65 HEAD@{2}: checkout: moving from feature-comp to develop
        3f97afa HEAD@{3}: commit: (git) Modify the order of contents.
        c12867d HEAD@{4}: commit: (terminology.rst) Draft.
        fe2ad65 HEAD@{5}: checkout: moving from develop to feature-comp
        fe2ad65 HEAD@{6}: merge feature-comp: Fast-forward
        5222302 HEAD@{7}: checkout: moving from feature-comp to develop
        fe2ad65 HEAD@{8}: commit: (envvars.rst) Draft.
        5222302 HEAD@{9}: checkout: moving from develop to feature-comp
        5222302 HEAD@{10}: merge feature-comp: Fast-forward
        ...

     危険なのであまりやりたくないが、
     あるコマンドで任意のコミットにリポジトリーの状態を巻き戻せる。

  :日本語訳: （訳さない）

refspec
  コマンド fetch と push が、リモートの ref とローカルの ref との対応関係を示すのに refspec を用いる。

  ヘルプには上の文言のようなことしかない？

  :日本語訳: （訳さない）

remote repository
  同じプロジェクトのリポジトリーではあるが、別のどこかに存在するリポジトリーを意味する。
  本当に遠隔地にあるとは限らない。
  インターネットの向こう側のディスク内に存在するのかもしれないし、
  同じマシンのディスク内かもしれない。

  * コマンド fetch と push はリモートリポジトリーとやり取りをする代表的なもの。
  * コマンド remote は場所に関する情報にアクセスできる。

  :日本語訳: リモートリポジトリー（英単語をカタカナで書くだけ）

remote-tracking branch
  別のリポジトリーから変更分を追いかけるのに用いる ref である。

  * ``refs/remotes/<repository>/<branch>`` のような文字列で表現されている。
  * これに対して直接修正を施したり、ローカルコミットを作ることはしない。

  :日本語訳: リモート追跡ブランチ、または単に追跡ブランチ。

repository
  ドキュメントではこの用語の定義をかなり詳細に与えているが、
  私は「ディレクトリー ``$GIT_DIR`` 以下全部」くらいの認識で困らない。

  :日本語訳: リポジトリー（英単語をカタカナで書くだけ）

revision
  コミットと同じ。
  ただし名詞的用法に限定できる。

  :日本語訳: リビジョン（英単語をカタカナで書くだけ）
  :同義語: commit

tag
  Git では任意のオブジェクトにタグを付けることができるようだ。タグにもタグを付けられる？
  よくある運用はコミットにタグを付けるというものだ。

  :日本語訳: タグ（英単語をカタカナで書くだけ）

tree
  次のどちらか一方を意味する。

  #. working tree
  #. blob と tree objects が従属している状態の tree object

  .. hint::

     次の例で両方の意味のツリーを示す。

     .. code-block:: console

        $ git log -1
        commit 3f97afac08976e5530105d85ec8d4173a2357cf7
        Author: showa_yojyo <yojyo@hotmail.com>
        Date:   Mon Nov 9 23:21:05 2015 +0900

            (git) Modify the order of contents.
        $ git cat-file -p 3f97afac
        tree 1a427ad7ae362ec203ec6d63af905ccf4d51fc47
        parent c12867de32453e32a130704bfaaf208cae672758
        author showa_yojyo <yojyo@hotmail.com> 1447078865 +0900
        committer showa_yojyo <yojyo@hotmail.com> 1447078865 +0900

        (git) Modify the order of contents.
        $ git cat-file -p 1a427ad7
        100644 blob 1b68ffbd137f9292b3708e22c0fbe21d10945908    .gitignore
        100644 blob 3415147e9f28037f1c48ab8debc2f54e3e7b37c3    LICENSE
        100644 blob 59dc8d67cc99c51ff62460cacf9ac40de50a315a    Makefile
        100644 blob f12be8a1b634c601f6323931dc2bede6a95f829c    Makefile.vars.sample
        100644 blob dc7e509932fb6676cc62ff0ccef588bd563fd368    README.rst
        100644 blob 4b5a998d1e5ea95560aa9355e2b8c60bc51aa504    gh-pages.sh
        040000 tree 73911bc143b8e65edb26b60ad130660ea77be8a2    source
        040000 tree 3357f429c967f53990cd17337f31301a9aa1f3b1    tools

  :日本語訳: ツリー（英単語をカタカナで書くだけ）
  :cf.: working tree

tree-ish
  次のオブジェクトは tree-ish であるという。

  * ツリーオブジェクトそのもの
  * commit-ish;
    コミットからは、そのトップディレクトリーに対応するツリーオブジェクトが得られることによる。
  * commit-ish を指すタグオブジェクト
  * 指す先のオブジェクトを再帰的に辿ると、
    ある commit-ish が得られるタグオブジェクト。

  :日本語訳: （訳さない）

tree object
  次の項目群のリストを含むオブジェクトである。

  * ファイル名
  * モード
  * 関連する blob/tree objects への refs

  .. hint:: 例を既に tree の項目の囲み記事で示した。

  :日本語訳: ツリーオブジェクト（英単語をカタカナで書くだけ）

upstream branch
  マージ元としてのデフォルトのブランチ。
  ``A`` の upstream branch が ``origin/B`` であるならば、
  ``A`` は ``origin/B`` を追跡している、という。

  :日本語訳: （調査中）

working tree
  現在 checkout されているファイル群からなる tree の意。

  通常は HEAD コミットのツリーと、
  ローカルでの未コミット変更分をひっくるめたものを意味する。

  :日本語訳: 作業コピー（暫定訳）

参考文献
======================================================================
`Utility Conventions <http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap12.html>`_
  POSIX.1-2008 という仕様書の一部。
  コマンドラインユーティリティーの引数の記述法についての規定。

.. include:: /_include/git-refs.txt
